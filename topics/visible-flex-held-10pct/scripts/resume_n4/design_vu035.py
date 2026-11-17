#!/usr/bin/env python3
import json,hashlib,numpy as np
from pathlib import Path
from scipy.optimize import root
from physical_linear_design import PhysicalDesign,geometry
D=PhysicalDesign('bundle','mode4_port24.json');base=json.loads(Path('root03-profile.json').read_text());base['vu']=.35
rows=[]
def fun(x):
 p=dict(base,delta=float(x[0]),vd=float(x[1]));a=D.linear(p,2,2e-11);v=a['core'][:,1];rows.append(dict(delta=p['delta'],vd=p['vd'],tau=v.tolist()));return v
res=root(fun,[.0301,.2485],tol=2e-10)
p=dict(base,delta=float(res.x[0]),vd=float(res.x[1]));a=D.linear(p,12,2e-12);g=geometry(D.profile(p),halfwidth=.147,cylinder_length=.54)
out=dict(success=bool(res.success),message=res.message,profile=p,tau=a['core'][:,1].tolist(),logs=a['logs'].tolist(),geometry=g,iterations=rows,scope='Actual finite linear port design; no nonlinear surface or strict interval geometry certificate')
Path('vu035-profile.json').write_text(json.dumps(p,indent=2)+'\n');Path('vu035-design.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='iterations'},indent=2))
