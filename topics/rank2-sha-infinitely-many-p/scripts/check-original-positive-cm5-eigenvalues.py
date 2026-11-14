#!/usr/bin/env python3
"""R284: exact three-source CM5 eigenvalues; no target-prime scan."""
import json,importlib.util
from pathlib import Path
import sympy as s
P=Path(__file__).parent
sp=importlib.util.spec_from_file_location('r248',P/'check-ray17-conjugate-trace-and-yang-projection.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
U=m.U;dom=m.dom;d=json.loads((P/'check-original-three-ordinary-adjoint.json').read_text())
def reverse17(cs):return s.Poly(sum(s.sympify(c)*U**(17-j) for j,c in enumerate(cs)),U,domain=dom)
sources={'A':reverse17(d['source_coefficients_ascending']['A']),'B':reverse17(d['source_coefficients_ascending']['B']),'Cbeta':s.Poly(U,U,domain=dom)*m.Qbe**4+m.Kbe**4}
rows=[]
for a in range(2,20):
 f=s.Poly(U,U,domain=dom)*m.Qp**4-(m.Kp**4).mul_ground(a)
 ub=(s.Poly(U,U,domain=dom)*m.Qb**4*m.inv(m.Kb**4,f)).rem(f)
 mult=m.ipow((m.Kb*m.inv(m.Kp,f)).rem(f),68,f)
 vals={name:s.expand(((mult*m.comp(poly,ub,f)).rem(f)*f.diff()).rem(f).nth(4)) for name,poly in sources.items()}
 rows.append(vals)
eig={}
for name,poly in sources.items():
 lam=dom.to_sympy(dom.from_sympy(rows[0][name])/dom.from_sympy(poly.eval(2)))
 assert all(s.expand(row[name]-lam*poly.eval(a))==0 for a,row in zip(range(2,20),rows)),name
 eig[name]=str(lam)
print(eig)
out={'status':'PASS','source_frame':'sigma^68','operator':'[2+i]_*[2-i]^*','eigenvalues':eig,'fibers':list(range(2,20)),'traces':[{name:str(z) for name,z in row.items()} for row in rows]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
