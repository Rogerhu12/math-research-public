#!/usr/bin/env python3
"""Fixed-g Gauss-Newton with low-memory physical Sobolev inner CG on every original row and column."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
def get(p):return json.loads(Path(p).read_text())
def write(p,x):
    with Path(p).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
def run(a):
    here=Path(__file__).parent
    supp=load(here/'2ecf-polar-raised-physical-ray-position-source.py','GNphysical_supplier')
    saved,de,full,caches,mods,*_=supp.validate_prepared(a)
    basis=load(here/'2ecf-polar-fixed-prefix-position-basis.py','GNphysical_basis').restrict(full)[0]
    stream=mods['stream'];area=load(a.scripts/'6a65-geometry-area-ratio-power-two.py','GNphysical_area')
    scan=load(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','GNphysical_value')
    cfg=stream.point.PointConfig(**de['pointConfig'])
    grid={k:(c,basis.matrices(c.nodes),{n:.5*np.asarray(w) for n,w in saved['caches'][k]['weights'].items()}) for k,c in caches.items()}
    prec=stream.BandedSobolev(basis,np.concatenate([v[0].nodes for v in grid.values()]),np.concatenate([v[2]['metric'] for v in grid.values()]),de['recipe']['preconditioner'])
    st=get(a.state)
    assert st['preparedSHA256']==sha(a.prepared) and st['modelDefinition']['basis']==basis.definition
    z=np.array(st['z']).reshape(basis.nb,basis.na)
    same=st.get('streamedGNEntrySHA256')==sha(__file__)
    own=st.get('ownExtendedAcceptedSteps',0) if same else 0
    model=dict(basis=basis.definition,pointConfig=de['pointConfig'],rows=4291840,originalFullThirteenAndArea=True,
        frozenSource=de['sourceIdentity'],preconditioner=prec.definition,innerCGIterations=a.iterations,damping=a.damping,
        streamedBlockRadials=8,sourceEntrySHA256=sha(supp.__file__),solveEntrySHA256=sha(__file__))
    if same and st['modelDefinition']!=model:raise ValueError('Changed own matrix-free epoch')
    def apply(direction=None):
        grad=np.zeros_like(z);quadratic=0.;rows=0
        for cache,mat,weights in grid.values():
            na=len(cache.u)
            for first in range(0,len(cache.nodes),8):
                sl=slice(first,first+8);mm=tuple(op[sl] for op in mat);ns=cache.nodes[sl]
                j0,f=cache(ns,na);j=j0+basis.packet(mm,z,na)
                w={k:v[sl,None]/na for k,v in weights.items()}
                pt=stream.point.PointLinearized(j.swapaxes(1,2),f,cfg,w);ar=area.AreaPacket(j,f,w['metric'],.5)
                if direction is None:r=pt.residual;ra=ar.residual
                else:
                    dj=basis.packet(mm,direction,na);r=pt.jvp(dj.swapaxes(1,2));ra=ar.jvp(dj[:,1],dj[:,2])
                g=pt.vjp(r).swapaxes(1,2);gs,gu=ar.vjp(ra);g[:,1]+=gs;g[:,2]+=gu
                grad+=basis.packet_adjoint(mm,g);quadratic+=np.vdot(r,r)+np.vdot(ra,ra);rows+=r.size+ra.size
        assert rows==4291840
        return prec.transpose(grad),float(quadratic)
    def value(coeff):
        vals=[]
        for key,(c,mat,w) in grid.items():
            v=scan.evaluate(stream,stream.point,area,c.jets+basis.packet(mat,coeff,len(c.u)),c.radius,c.nodes,c.u,cfg,saved['caches'][key]['weights'])
            vals.append(v)
        return dict(R2=sum(x['R2'] for x in vals),metric=max(x['metric'] for x in vals),curvature=max(x['curvature'] for x in vals),held=min(x['held'] for x in vals),rows=sum(x['actualRows'] for x in vals))
    base=value(z);history=[]
    if not same and abs(base['R2']-st['evaluation']['squaredNorm'])>1e-8:raise ArithmeticError('Warm source or weights changed')
    for step in range(a.steps):
        gradient,base2=apply();res=-gradient;cg=res.copy();inn=np.zeros_like(cg);norm=float(res@res);trace=[];checks=[]
        if abs(base2-base['R2'])>1e-8*max(base2,1):raise ArithmeticError('Block residual disagrees with full point operator')
        for j in range(a.iterations):
            pz=prec.unpack(cg);hessian,jv2=apply(pz)
            symmetry=abs(cg@hessian-jv2)/max(1.,jv2);checks.append(symmetry)
            if symmetry>2e-9:raise ArithmeticError('Physical normal violates streamed adjoint identity')
            hessian+=a.damping*cg;alpha=norm/(cg@hessian);inn+=alpha*cg;res-=alpha*hessian
            new=float(res@res);trace.append(float(np.sqrt(new))/max(1.,np.linalg.norm(gradient)))
            if new<1e-15:break
            cg=res+(new/norm)*cg;norm=new
        dz=prec.unpack(inn);slope=float(gradient@inn);accepted=False;trials=[]
        if step==0 and not same:
            # Directional derivative of the actual full 14-row objective at the new source.
            unit=dz/max(1.,np.linalg.norm(dz));eps=1e-5
            fd=(value(z+eps*unit)['R2']-value(z-eps*unit)['R2'])/(2*eps)
            exact=2*slope/max(1.,np.linalg.norm(dz));fd_relative=abs(fd-exact)/max(1.,abs(exact))
            if fd_relative>2e-4:raise ArithmeticError('New streamed physical derivative failed')
        else:fd_relative=None
        for alpha in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125):
            new=value(z+alpha*dz);trials.append(dict(alpha=alpha,**new))
            if new['R2']<base['R2'] and new['R2']<=base['R2']+2e-4*alpha*slope:
                own+=1;z+=alpha*dz;accepted=True;break
        rec=dict(ownAccepted=own,accepted=accepted,baseline=base,trials=trials,CGResiduals=trace,adjointResiduals=checks,
            finiteDifference=fd_relative,physicalPredictedSlope=slope)
        history.append(rec);print(own,accepted,new['R2'],new['metric'],new['curvature'],new['held'],flush=True)
        if not accepted:break
        base=new;out=dict(modelDefinition=model,preparedSHA256=sha(a.prepared),streamedGNEntrySHA256=sha(__file__),
            ownExtendedAcceptedSteps=own,parentStateSHA256=sha(a.state),z=z.ravel().tolist(),acceptance=rec,fixedG=True,finiteOnly=True)
        write(str(a.prefix)+f'-step{step+1:02}-state.json',out)
    write(str(a.prefix)+'-report.json',dict(sourceSHA256=sha(__file__),includesEveryPhysicalRow=True,ownAccepted=own,
        inputStateSHA256=sha(a.state),iterations=a.iterations,damping=a.damping,history=history))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','prepared','state','prefix'):p.add_argument('--'+k,required=True,type=Path)
    p.add_argument('--steps',type=int,default=3);p.add_argument('--iterations',type=int,default=4);p.add_argument('--damping',type=float,default=.06);run(p.parse_args())
