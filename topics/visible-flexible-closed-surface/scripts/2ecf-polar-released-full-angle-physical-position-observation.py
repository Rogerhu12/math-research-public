#!/usr/bin/env python3
"""Stream the actual full-XYZ perturbation on all original rows and an independent released-tail grid."""
import argparse
import importlib.util
import os
from pathlib import Path
import sys
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'): os.environ[k]='1'
import numpy as np
def local(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
here=Path(__file__).parent
hi=local(here/'2ecf-polar-released-full-angle-physical-position-normal.py','direct_physical_full_angle')
base,ext,c=hi.base,hi.ext,hi.c
def run(a):
    m=hi.clock.PhysicalField(a);active=base.read(a.perturbation);raw=np.array(active['coefficients'])
    assert active['baseSpatialSHA256']==base.sha(a.spatial) and active['originalFieldSHA256']==base.sha(a.field)
    clock=base.read(a.clock) if a.clock else None
    assert (base.sha(a.clock) if a.clock else None)==active['clockSHA256']
    target=base.read(a.closed)['closedTrueTargetSHA256']
    if clock:
        assert clock['previousTargetSHA256']==target
        alpha=np.array(clock['targetCoefficients'])
        target=clock['newTargetSHA256']
        if np.any(alpha):assert target==c.target_hash(clock['previousTargetSHA256'],m.b,m.T,clock['metricSpans'],alpha)
    assert target==active['targetSHA256']
    p,ind=base.read(a.prepared),base.read(a.independent)
    st=local(a.scripts/'6a65-cartesian-complete-stream.py','actual_complete_full_xyz')
    ar=local(a.scripts/'6a65-geometry-area-ratio-power-two.py','actual_area_full_xyz')
    groups={k:(np.asarray(g['nodes']),np.asarray(g['angles']),g['files']['jets'],g['files']['radius'],g['weights']) for k,g in p['caches'].items()}
    groups['independent']=(np.asarray(ind['physicalNodes']),np.asarray(ind['angles']),ind['files']['jets'],ind['files']['radius'],None)
    ns=m.S+(m.T-m.S)*(np.arange(193)+.371)/193;groups['tail193x272']=(ns,2*np.pi*(np.arange(272)+.417)/272,None,None,None)
    old=st.point.PointConfig
    class New(old):
        def __post_init__(self):
            vals={k:getattr(self,k) for k in self.__dataclass_fields__};vals['height_maximum']=.0195;old(**vals)
    Z=.415+m.sol['raisedCuffDelta'];cfg=New(**dict(p['definition']['pointConfig'],true_cuff_height=Z,height_maximum=.635-Z))
    out={}
    for name,(ns,u,jp,rp,w) in groups.items():
        js=np.load(jp,mmap_mode='r') if jp else None;rr=np.load(rp,mmap_mode='r')[:,0] if rp else .8+m.S-ns
        rad=ext.apply_target(ns,rr,m.b,m.S,m.g);rv=np.ones_like(ns);dv=np.zeros_like(ns)
        if clock:
            B,D=c.spline(ns,m.b,m.T,clock['metricSpans'])[:2];rv=np.exp(B@alpha[0]);dv=D@alpha[0];rad*=np.exp(B@alpha[1])
        stats=None;area=0.;mi=999.
        for j in range(0,len(ns),6):
            ss=ns[j:j+6];v=np.array(js[j:j+6],copy=True) if js is not None else np.empty((len(ss),6,len(u),3))
            ac=(ss>=m.b)&(ss<=m.T)
            if np.any(ac):
                n=ss[ac];v[ac]=m.compose(n,u,clock) if clock else m.grid(n,u)
                v[ac]+=hi.XYZ(n,u,m.b,m.T,active['spans'],active['modes']).apply(raw)
            for i in np.flatnonzero(ss>m.T):
                q=ext.flat_port(u,rr[j+i]);v[i]=np.stack([q[k] for k in ('P','V','Pu','A','Vu','Puu')]);v[i,0,:,2]+=m.sol['raisedCuffDelta']
            v=hi.warp(v,rv[j:j+6],dv[j:j+6]);f=rad[j:j+6,None]
            W={k:(np.ones((len(ss),1)) if w is None else .5*np.array(w[k][j:j+6])[:,None])/len(u) for k in ('curvature','metric','geometry')}
            pt=st.point.PointLinearized(v.swapaxes(1,2),f,cfg,W);b=st._block_statistics(pt,ss,len(u))
            for key in ('worstMetric','worstCurvature'):b[key]['u']+=float(u[0])
            stats=st._merge_statistics(stats,b);packet=ar.AreaPacket(v,f,W['metric'],.5)
            area+=packet.stats['squaredNorm'];mi=min(mi,float(packet.stats['minAreaRatio']))
        out[name]=dict(metric=stats['maxRelativeMetric'],curvature=stats['maxCurvature'],held=stats['minHeldDistance'],R2=stats['squaredNorm']+area if w is not None else None,worstMetric=stats['worstMetric'],worstCurvature=stats['worstCurvature'],area=mi,geometry=stats['geometryMaximumViolations'],actualRows=14*len(ns)*len(u))
        print(name,out[name]['metric'],out[name]['curvature'],out[name]['held'],flush=True)
    base.stores(a.output,dict(entrySHA256=base.sha(__file__),perturbationSHA256=base.sha(a.perturbation),fieldSHA256=base.sha(a.field),spatialSHA256=base.sha(a.spatial),clockSHA256=active['clockSHA256'],targetSHA256=target,groups=out))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','spatial','closed','clock','perturbation','output'):p.add_argument('--'+k,type=Path)
    run(p.parse_args())
