#!/usr/bin/env python3
"""Récupère les fiches Infofacture ARS 2025, sans attribuer de note non vérifiée.
Utilise Hub'Eau (liaison commune -> UDI) et les PDF officiels AtlaSanté.
Le résultat n'est publié que si les contrôles de couverture réussissent.
"""
from __future__ import annotations
import concurrent.futures as cf
import datetime as dt
import io
import json
import pathlib
import re
import time
from collections import defaultdict
import fitz
import requests

ROOT=pathlib.Path(__file__).resolve().parents[1]
YEAR=2025
HUB='https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/communes_udi'
PDF='https://carto.atlasante.fr/IHM/cartes/infofactures/AQUASISED/{y}/INFOFACTURE-{udi}-{y}.pdf'
SESSION=requests.Session();SESSION.headers.update({'User-Agent':'Alouette-Cartographie-Eau/1.0 (sources publiques; contact via site presse)','Accept':'application/json,application/pdf,*/*'})

def get(url,params=None):
    error=None
    for attempt in range(3):
        try:
            response=SESSION.get(url,params=params,timeout=22)
            if response.status_code==404:return None
            response.raise_for_status()
            if len(response.content)>12_000_000:raise ValueError('réponse trop volumineuse')
            return response
        except (requests.RequestException,ValueError) as exc:
            error=exc;time.sleep(.6*(attempt+1))
    raise RuntimeError(f'Erreur de récupération {url}: {error}')

def commune_networks(item):
    code,_=item
    response=get(HUB,{'code_commune':code,'annee':YEAR,'size':200})
    if response is None:return code,[]
    data=response.json();entries=data.get('data',[])
    networks={str(x.get('code_reseau','')).strip().zfill(9):x.get('nom_reseau') or '' for x in entries if x.get('code_reseau')}
    return code,[{'udi':k,'nom':v} for k,v in networks.items()]

def lire_note_pdf(pdf_bytes,udi):
    if not pdf_bytes.startswith(b'%PDF-'):return None
    doc=fitz.open(stream=pdf_bytes,filetype='pdf')
    page=doc[0]
    # Ces proportions correspondent à la case de l'indicateur GLOBAL, et non aux lettres de la légende.
    r=page.rect
    rect=fitz.Rect(r.width*.685,r.height*.160,r.width*.775,r.height*.220)
    words=page.get_text('words',clip=rect)
    grades=[w[4] for w in words if w[4] in ('A','B','C','D')]
    # Le score doit être unique et visuellement isolé dans son cadre.
    grade=grades[0] if len(grades)==1 else None
    full=page.get_text('text')
    if not grade or not re.search(r'\b2025\b',full) or 'Indicateur' not in full:return None
    # Conclusion, conservée en citation courte si lisible ; pas d'inférence de molécule.
    conclusion=''
    lines=[x.strip() for x in full.splitlines() if x.strip()]
    for i,line in enumerate(lines):
        if ('eau distribuée' in line.lower() or "l'eau distribuée" in line.lower()) and len(line)>35:
            conclusion=line[:230];break
    return {'note':grade,'source':PDF.format(y=YEAR,udi=udi),'conclusion':conclusion,'extraction':'case globale du PDF ARS'}

def grade_pdf(udi):
    response=get(PDF.format(y=YEAR,udi=udi))
    return lire_note_pdf(response.content,udi) if response else None

def main():
    communes=json.loads((ROOT/'communes-vendee.json').read_text())
    if len(communes)!=253:raise RuntimeError('Le référentiel communal ne contient pas 253 communes')
    mapping={};errors=[]
    with cf.ThreadPoolExecutor(max_workers=5) as pool:
        futures={pool.submit(commune_networks,item):item[0] for item in communes.items()}
        for future in cf.as_completed(futures):
            try:code,networks=future.result();mapping[code]=networks
            except Exception as exc:errors.append(f'{futures[future]} : {exc}')
    if errors or len(mapping)!=len(communes):
        raise RuntimeError(f'{len(errors)} erreur(s) sur les liaisons UDI : '+ ' ; '.join(errors[:5]))
    all_udis={n['udi'] for networks in mapping.values() for n in networks}
    if len(all_udis)<20:raise RuntimeError(f'Seulement {len(all_udis)} réseaux trouvés : couverture probablement insuffisante')
    evidence={};missing=[]
    with cf.ThreadPoolExecutor(max_workers=4) as pool:
        futures={pool.submit(grade_pdf,udi):udi for udi in sorted(all_udis)}
        for future in cf.as_completed(futures):
            udi=futures[future]
            try:
                item=future.result()
                if item:evidence[udi]=item
                else:missing.append(udi)
            except Exception:missing.append(udi)
    if len(evidence)<20:raise RuntimeError(f'Seulement {len(evidence)} fiches classées : collecte insuffisante, référentiel existant conservé')
    results={}
    for code,nets in mapping.items():
        details=[]
        for entry in nets:
            grade=evidence.get(entry['udi'])
            details.append({'udi':entry['udi'],'nom':entry['nom'],**(grade or {'note':None,'source':None,'conclusion':'Fiche manquante ou extraction incertaine'})})
        notes={x['note'] for x in details if x['note']}
        valid=bool(details) and all(x['note'] for x in details)
        note=next(iter(notes)) if valid and len(notes)==1 else None
        results[code]={'nom':communes[code],'note':note,'multi':valid and len(notes)>1,'reseaux':details}
    output={'annee':YEAR,'mis_a_jour':dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),'statut':'extraction automatisée, vérification éditoriale recommandée','communes':results,'reseaux':evidence,'statistiques':{'communes':len(results),'reseaux_identifies':len(all_udis),'fiches_lues':len(evidence),'fiches_manquantes':len(missing),'communes_classees':sum(bool(x['note']) for x in results.values()),'communes_multi_notes':sum(bool(x['multi']) for x in results.values())}}
    (ROOT/'qualite-2025.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(output['statistiques'],ensure_ascii=False))

if __name__=='__main__':main()
