#!/usr/bin/env python3
"""Finite nonzero test of exact nested M12 transfer and storage two-jet bounds.

This uses exact rational de Boor evaluation independent of knot insertion.
It is a synthetic coefficient/kernel check, not an actual M12 solved field.
The production transfer CLI still requires its actual old field and R226.
"""
from __future__ import annotations
import argparse,bisect,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def rational_spline_value(t,c,p,x):
    if x==t[-1]:k=len(c)-1
    else:k=bisect.bisect_right(t,x)-1
    work=[list(c[k-p+j]) for j in range(p+1)]
    for r in range(1,p+1):
        for j in range(p,r-1,-1):
            denominator=t[j+1+k-r]-t[k-p+j]
            if denominator<=0:raise ArithmeticError('Degenerate selected de Boor interval')
            alpha=(x-t[k-p+j])/denominator
            work[j]=[(1-alpha)*a+alpha*b for a,b in zip(work[j-1],work[j])]
    return work[p]
def derivative(t,c,p):
    out=[]
    for j in range(len(c)-1):
        delta=t[j+p+1]-t[j+1]
        out.append([p*(b-a)/delta for a,b in zip(c[j],c[j+1])])
    return t[1:-1],out,p-1
def cartesian(coeff,pm,zm,quarter,du):
    cosine=[1,0,-1,0];sine=[0,1,0,-1];out=[Q(0),Q(0),Q(0)]
    for value,k in zip(coeff[:len(pm)],pm):
        k=int(k);phase=(k*quarter+du)%4;factor=Q(k**du)
        out[0]+=value*factor*cosine[phase];out[1]+=value*factor*sine[phase]
    for value,k in zip(coeff[len(pm):],zm):
        k=int(k);out[2]+=value*Q(k**du)*cosine[(k*quarter+du)%4]
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True)
    ap.add_argument('--consumer',type=Path,default=Path(__file__).with_name('6a65-m12-exact-radial-angular-warm-transfer.py'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();began=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh finite transfer report required')
    m=load('finite_exact_radial_transfer',args.consumer)
    helper_path=args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py'
    if sha(helper_path)!=m.BOEHM_SHA:raise ValueError('Different exact Boehm helper')
    b=load('independently_checked_Boehm_helper',helper_path)
    mesh=list(map(m.fq,[0.,.125,.3,.5,.7,.875,1.]))
    t=[Q(0)]*6+mesh[1:-1]+[Q(1)]*6
    inserted=list(map(m.fq,[.2,.5,.5,.625]))
    nt=sorted(t+inserted);newmesh=sorted(set(nt))
    pm=np.arange(-3,4)*3+1;zm=np.arange(4)*3
    npm=np.arange(-5,6)*3+1;nzm=np.arange(6)*3
    rng=np.random.default_rng(261818)
    old=[[Q(int(v),2**50) for v in row] for row in rng.integers(1,1000000,size=(len(t)-12,len(pm)+len(zm)))
         *rng.choice([-1,1],size=(len(t)-12,len(pm)+len(zm)))]
    m.check_knots(t,list(map(float,mesh)));m.check_knots(nt,list(map(float,newmesh)))
    stored,bounds,count=m.transfer(old,t,pm,zm,nt,npm,nzm,b)
    oldfull=[[Q(0)]*len(old[0]) for _ in range(3)]+old+[[Q(0)]*len(old[0]) for _ in range(3)]
    newfree=[[m.fq(v) for v in row] for row in stored]
    newfull=[[Q(0)]*len(newfree[0]) for _ in range(3)]+newfree+[[Q(0)]*len(newfree[0]) for _ in range(3)]
    points=sorted(set(newmesh+[(a+b)/2 for a,b in zip(newmesh,newmesh[1:])]))
    oldstate=(t,oldfull,5);newstate=(nt,newfull,5);evaluations=0;maximum_squared_error=Q(0)
    ratios={};endpoint_max=Q(0)
    for radial in range(3):
        for angular in range(3-radial):
            maximum_ratio=Q(0)
            for x in points:
                oldv=rational_spline_value(*oldstate,x);newv=rational_spline_value(*newstate,x)
                for angle in range(4):
                    va=cartesian(oldv,pm,zm,angle,angular);vb=cartesian(newv,npm,nzm,angle,angular)
                    delta=[a-b for a,b in zip(vb,va)];square=sum(v*v for v in delta)
                    bound=bounds[radial,angular]
                    if square>bound*bound:raise ArithmeticError('Exact actual storage error escaped the continuous bound')
                    if bound:maximum_ratio=max(maximum_ratio,square/(bound*bound))
                    maximum_squared_error=max(maximum_squared_error,square);evaluations+=1
                    if x in (0,1):endpoint_max=max(endpoint_max,sum(abs(v) for v in vb))
            ratios[str((radial,angular))]=float(maximum_ratio)
        if radial<2:
            oldstate=derivative(*oldstate);newstate=derivative(*newstate)
    if not maximum_squared_error or endpoint_max:
        raise ArithmeticError('Nonzero rounding and exact zero endpoint jets both required')
    old_modes={('planar',int(v)) for v in pm}|{('height',int(v)) for v in zm}
    new_modes=[('planar',int(v)) for v in npm]+[('height',int(v)) for v in nzm]
    new_columns=[j for j,name in enumerate(new_modes) if name not in old_modes]
    if np.count_nonzero(stored[:,new_columns]):raise ArithmeticError('New Fourier modes are not exactly zero')
    result={'schema':'6a65-M12-radial-angular-warm-nonzero-finite-check-v1',
        'script_sha256':sha(__file__),'consumer_sha256':sha(args.consumer),'exact_Boehm_source_sha256':sha(helper_path),
        'seed':261818,'old_shape':[len(old),len(old[0])],'new_shape':list(stored.shape),
        'old_nonzero_coefficients':sum(v!=0 for row in old for v in row),
        'inserted_knots_counting_multiplicity':count,'max_interior_multiplicity':3,
        'new_angular_columns_exactly_zero':True,'complete_boundary_two_jets_exactly_zero':True,
        'exact_rational_native_six_jet_comparisons':evaluations,
        'nonzero_actual_storage_rounding_seen':True,
        'max_squared_error_over_continuous_bound_squared':ratios,
        'continuous_native_storage_bounds':{str(k):m.show(v) for k,v in bounds.items()},
        'actual_exit':0,'all_checks_passed':True,'actual_old_M12_field_consumed':False,
        'production_main_physical_R226_binding_executed':False,'new_field_solve_performed':False,
        'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False))
if __name__=='__main__':main()
