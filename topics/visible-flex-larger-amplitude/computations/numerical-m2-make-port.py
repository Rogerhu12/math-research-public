#!/usr/bin/env python3
"""Package a sampled finite linear DN, without changing its physical parameters."""
import argparse,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--linear',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--compare',type=Path)
p.add_argument('--preserve-port',type=Path,help='Retain every existing low-mode DN value exactly and append only genuinely computed higher modes')
p.add_argument('--scope',default='Frozen physical m2 tail design; finite linear cusp-aware DN only. No nonlinear or infinite-tail closure.')
a=p.parse_args();r=json.loads(a.linear.read_text());c=r['cut'];origin=a.source_topic/'source-origin.json'
source={'linear_run':str(a.linear),'linear_sha256':hashlib.sha256(a.linear.read_bytes()).hexdigest(),'steps':r['steps'],'far':r['far'],'source_revision':json.loads(origin.read_text())['source_revision'] if origin.exists() else None}
if a.compare:
 old=json.loads(a.compare.read_text());by={x['mode']:x['slope'] for x in old['rows']};d=[{'mode':x['mode'],'difference':x['slope']-by[x['mode']]} for x in r['rows'] if x['mode'] in by]
 source['comparison']={'file':str(a.compare),'sha256':hashlib.sha256(a.compare.read_bytes()).hexdigest(),'differences':d,'max_absolute_difference':max(abs(x['difference']) for x in d)}
port={'scope':a.scope,'parameters':r['config'],'cut':{'radius':c['r'],'backgroundSlope':c['w'],'backgroundSecond':c['wr'],'E':c['E'],'Ep':c['Ep']},'modes':[x['mode'] for x in r['rows']],'linearSlope':[x['slope'] for x in r['rows']],'source':source}
if a.preserve_port:
 old=json.loads(a.preserve_port.read_text());n=len(old['linearSlope'])
 if old['parameters']!=port['parameters'] or old['cut']!=port['cut']:raise ValueError('Preserved port physical parameters or cut differ')
 if n>len(port['linearSlope']) or old['modes']!=port['modes'][:n]:raise ValueError('Preserved port is not the exact low-mode basis prefix')
 difference=[x-y for x,y in zip(port['linearSlope'][:n],old['linearSlope'])]
 port['linearSlope'][:n]=old['linearSlope']
 source['preserved_low_modes']={'base_port':str(a.preserve_port),'base_port_sha256':hashlib.sha256(a.preserve_port.read_bytes()).hexdigest(),'count':n,'values_preserved_exactly':True,'recomputed_max_absolute_difference':max(map(abs,difference),default=0.),'added_modes':port['modes'][n:]}
a.out.write_text(json.dumps(port,indent=2)+'\n')
print(json.dumps({'port':str(a.out),'first_slope':port['linearSlope'][0],'modes':len(port['modes']),'comparison':source.get('comparison',{}).get('max_absolute_difference')}))
