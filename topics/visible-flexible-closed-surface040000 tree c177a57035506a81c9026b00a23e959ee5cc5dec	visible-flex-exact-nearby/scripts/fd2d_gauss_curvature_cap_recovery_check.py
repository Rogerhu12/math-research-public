"""Small actual R134 recovery check; use an unused output filename."""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from fd2d_gauss_curvature_cap_recovery import project_gauss_curvature_cap
from fd2d_gauss_curvature_cap_nearest_recovery import project_fixed_m_nearest_gauss_cap


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    arg=ap.parse_args()
    if arg.out.exists(): raise FileExistsError(arg.out)
    started=time.monotonic()
    rng=np.random.default_rng(134)
    C=7.0
    count=384
    n=rng.normal(0,9,count);m=rng.normal(0,9,count);l=rng.normal(0,9,count)
    K=rng.uniform(-C*C,C*C,count)
    # Exact zero branches, cap corners, and preservation outside the chosen branch.
    n=np.r_[n,[0,-1,0,0,7,-7,.1]]
    m=np.r_[m,[0,0,7,0,0,0,.2]]
    l=np.r_[l,[2,3,0,0,7,-7,.3]]
    K=np.r_[K,[0,0,-49,49,49,49,.02]]
    preserve=np.zeros(len(n),bool);preserve[-2:]=True
    simple=project_gauss_curvature_cap(n,m,l,K,C,preserve)
    near=project_fixed_m_nearest_gauss_cap(n,m,l,K,C,preserve)
    # A dense independent n grid is only a finite comparison, never a root certificate.
    excess=0.
    for i in range(0,count,5):
        mm=near['m'][i];a=K[i]+mm*mm
        d=np.sqrt(max((C-K[i]/C)**2-4*mm*mm,0))
        hi=(C+K[i]/C+d)/2
        lo=abs(a)/hi if hi>0 else 0
        if a == 0 or lo <= 0: continue
        grid=np.linspace(lo,hi,4097)
        cg=(grid-n[i])**2+(a/grid-l[i])**2
        own=(near['n'][i]-n[i])**2+(near['l'][i]-l[i])**2
        excess=max(excess,float(own-np.min(cg)))
    diagnostics=near['diagnostics']
    passed=(diagnostics['preserved_bitwise'] and
            diagnostics['active_max_gauss_defect']<1e-10 and
            diagnostics['active_max_curvature']<=C+1e-10 and
            diagnostics['frobenius_change_squared']<=simple['diagnostics']['frobenius_change_squared']+1e-9 and
            excess<1e-8)
    here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-r134-recovery-finite-check-v1',passed=bool(passed),
                actual_execution=True,point_count=len(n),simple=simple['diagnostics'],
                fixed_m_nearest=diagnostics,dense_grid_energy_excess=excess,
                sources={p.name:digest(p) for p in [Path(__file__),here/'fd2d_gauss_curvature_cap_recovery.py',here/'fd2d_gauss_curvature_cap_nearest_recovery.py']},
                seconds=time.monotonic()-started,
                scope='Finite random/edge check only; does not reproduce inaccessible saved-75%-state reports.')
    arg.out.parent.mkdir(parents=True,exist_ok=True)
    arg.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,allow_nan=False))
    if not passed: raise SystemExit(1)
if __name__=='__main__':main()
