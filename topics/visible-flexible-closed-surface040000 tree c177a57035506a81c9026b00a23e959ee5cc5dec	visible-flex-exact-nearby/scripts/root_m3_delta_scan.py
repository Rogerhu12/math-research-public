#!/usr/bin/env python3
"""Explore genuinely recomputed m3 tail ports at several physical cell scales.
Design changes only; not a convergence study or a nonlinear tail assertion.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json,subprocess,sys,time
from pathlib import Path
from scipy.optimize import brentq
from root_general_prefix_scan import install,describe
root=Path(__file__).resolve().parents[1];notes=root/'notes'
source=Path(os.environ.get('VISIBLE_FLEX_SOURCE_ROOT',str(root.parents[1])))
old=Path(os.environ.get('VISIBLE_FLEX_ELLIPSE_NOTES',str(notes)))
backward=install(old,source)
base=json.loads((notes/'root_cut_tail_cap002_p160_config.json').read_text())
report=dict(scope=__doc__,rows=[]);start=time.time()
for delta0 in [.02,.04,.06,.1,.16,.25]:
    w=.5;cap=.02
    tag=('delta%g'%delta0).replace('.','p')
    cfg={**base,'wCut':w,'slopeCap':cap,'delta0':delta0}
    inp=notes/('root_m3_p160_'+tag+'_config.json');out=notes/('root_m3_p160_'+tag+'_linear.json')
    inp.write_text(json.dumps(cfg,indent=2)+'\n')
    row=dict(config=cfg)
    try:
        proc=subprocess.run(['node',str(root/'scripts/root_cut_tail_general_linear.mjs'),str(inp),str(out),'1','256','32','3'],env={**os.environ,'VISIBLE_FLEX_SOURCE_ROOT':str(source)},capture_output=True,text=True)
        if proc.returncode:raise RuntimeError(proc.stderr[-1200:])
        d=json.loads(out.read_text());D=d['rows'][0]['cutSlope'];threshold=d['rows'][0]['linearTPositivityAmplitudeThreshold']
        r=cfg['rCut'];port=dict(cut=dict(radius=r,backgroundSlope=w,backgroundSecond=-7*w/r,E=1+w*w,Ep=-14*w*w/r),linearModes=[3],linearSlope=[D])
        row.update(tail=d['rows'][0],tail_stats=d['stats'],roots=[])
        for u,v in [(.25,.4),(.3,.45)]:
            pcfg=dict(direction='outward',vu=u,vd=v,ramp=.4,cycles=1,cut_radius=r,cut_slope=w)
            previous=None
            for delta in [.015,.035,.06,.1,.16]:
                val=float(backward({**pcfg,'delta':delta},port)[1].core[1])
                if previous and previous[1]*val<0:
                    rt=brentq(lambda x:float(backward({**pcfg,'delta':x},port)[1].core[1]),previous[0],delta,xtol=2e-11)
                    rr=describe(backward,{**pcfg,'delta':rt},port);rr['tail_threshold_ratio']=rr['terminal_height_first_order']/threshold;row['roots'].append(rr)
                previous=(delta,val)
    except Exception as e:row['error']=repr(e)
    report['rows'].append(row);report['elapsed_seconds']=time.time()-start
    (notes/'root_m3_tail_delta_scan.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(delta0=delta0,w=w,cap=cap,D=row.get('tail',{}).get('cutSlope'),threshold=row.get('tail',{}).get('linearTPositivityAmplitudeThreshold'),roots=row.get('roots'),error=row.get('error'))),flush=True)
