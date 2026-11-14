#!/usr/bin/env python3
"""Exact complete degree136 CM19 matrix and full partial reflection D33.
Consumes the same canonical fiber implementation as R466.
No target-prime sampling.
"""
from pathlib import Path
import runpy,json,time
from concurrent.futures import ProcessPoolExecutor,as_completed
P=Path(__file__).resolve().parents[1]
h=runpy.run_path(str(P/'scripts/check-r466-fixed-two-division-source.py'))
Q,Mat=h['Q'],h['Mat']; basis=[[h['fq'](i==j)for i in range(23)]for j in range(23)]
def fiber(i):return h['cm19_fiber']((i,basis))
def dec(d):return tuple(Mat([[Q(x)for x in row]for row in d[k]])for k in ('real','delta'))
if __name__=='__main__':
 start=time.monotonic();rows={}
 with ProcessPoolExecutor(max_workers=2)as pool:
  fs=[pool.submit(fiber,a)for a in range(1,24)]
  for f in as_completed(fs):
   a,v=f.result();rows[a]=v;print('CM19 full standard fiber',a,'elapsed',round(time.monotonic()-start,1),flush=True)
 vi=Mat([[Q(a)**(3*j)for j in range(23)]for a in range(1,24)]).inv()
 n19=tuple(vi*Mat([[rows[a][j][k]for j in range(23)]for a in range(1,24)])for k in(0,1))
 n7=dec(json.load(open(P/'notes/2026-11-14-theta-degree136-cm7-exact.json'))['matrix']);ii=h['identity'](23);km=h['km'];kp=h['kp'];ks=h['ks'];om=h['fq'](Q(-1,2),Q(1,2));om2=h['fp'](om,2)
 assert km(n7,n19)==km(n19,n7)
 D=ks(km(n19,kp(n7,16,ii)),om2)
 assert km(D,D)==ii and km(D,n7)==km(n7,D)
 out={'field':'Q(delta), delta^2=-3','normalization':'N19=M_gamma19/gamma19, gamma19=4+delta','basis':'sigma^136*x^2*X^j, j=0,...,22','fiber_targets':list(range(1,24)),'matrix':h['serialize_matrix'](n19),'D33':h['serialize_matrix'](D),'D33_involution':True,'commutes_CM7':True}
 (P/'notes/2026-11-14-theta-degree136-cm19-exact.json').write_text(json.dumps(out,indent=2)+'\n')
 print('COMPLETE',round(time.monotonic()-start,1),flush=True)
