#!/usr/bin/env python3
"""Fit the true open height and angular tangent angle of every full R317-family ring, with its frozen target and original closed tail."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solveh_banded,LinAlgError

def module(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def prolong(kn,c,m,old,split):
    if m<old:raise ValueError('Parent angular fields would be lost')
    if split:
        bs=BSpline(kn,np.pad(c,((3,3),(0,0))),5,axis=0)
        u=np.unique(kn)
        for x in u[:-1]+np.diff(u)/2:bs=bs.insert_knot(x)
        kn=bs.t.copy();c=bs.c[3:-3]
    G=np.zeros((len(c),2*m+1))
    G[:,:old+1]=c[:,:old+1];G[:,m+1:m+1+old]=c[:,old+1:]
    return kn,G
def raw_report(J,Q,b2,m):
    _,e,_=m.gram(J,Q[:,None],np.ones((len(Q),1)),np.sqrt(b2))
    k,_=m.curvature(J)
    return dict(peak=float(e.max()),rms=float(np.mean(e**2)**.5),curvature=float(k.max()))
def main():
    p=argparse.ArgumentParser()
    for key in ('scripts','work','physical-source','cut','comparison','refinement-source','adjacent-source','two-scalar-source','parent','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--heat-source',type=Path);p.add_argument('--seed',type=Path);p.add_argument('--split',action='store_true')
    p.add_argument('--angular-strength',type=float,default=1.)
    p.add_argument('--angular-families',type=int,default=12);p.add_argument('--steps',type=int,default=5);p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    if not 0<=a.angular_strength<=1:raise ValueError('Angular target strength must lie in [0,1]')
    phys=module(a.physical_source,'actual_two_port_source');api=module(a.cut,'actual_two_port_cut')
    ref=module(a.refinement_source,'actual_two_port_spans');adj=module(a.adjacent_source,'actual_two_port_material_nodes')
    two=module(a.two_scalar_source,'actual_ring_angular_chart');micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','actual_old_R262')
    geo=phys.NormalCurve();api.true_arc_position=phys.true_arc_position;heatdata=None
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z or str(z['cutSHA'])!=sha(a.cut) or a.low!=phys.LOW:raise ValueError('Wrong complete annular parent')
        if 'heatGain' in z:
            if a.heat_source is None or str(z['heatSourceSHA'])!=sha(a.heat_source):raise ValueError('Missing exact heat orbit')
            old=z['heatInletXYZ'].copy();extra=z['heatInletProfiles'].copy();heatdata=[float(z[k]) for k in ('heatGain','heatOrder','heightOrder','heatAmplitude','heatLate')]
        elif 'physicalInletProfiles' in z:
            old=z['inletNativeXYZ'].copy();extra=z['physicalInletProfiles'].copy()
        else:old=z['actualPhysicalXYZ'].copy();extra=None
        if extra is not None and str(z['inletProfileSourceSHA'])!=sha(a.adjacent_source):raise ValueError('Different physical inlet profiles')
        oldkn=z['knots'].copy();a.modes=int(z['modes']);mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
    if heatdata:heat=module(a.heat_source,'actual_parent_heat_orbit')
    src=micro.Source(a);m=a.angular_families
    if a.seed:
        with np.load(a.seed,allow_pickle=False) as s:
            if float(s['angularStrength'])!=a.angular_strength:raise ValueError('Different angular representation strength')
            if str(s['parentSHA'])!=sha(a.parent) or str(s['twoScalarSHA'])!=sha(a.two_scalar_source):raise ValueError('Incompatible two-scalar parent')
            kn,seed=prolong(s['knots'].copy(),s['heightAndAngle'].copy(),m,int(s['angularFamilies']),a.split)
    else:
        n=len(oldkn)-12;kn,seed=prolong(oldkn,np.zeros((n,2*m+1)),m,m,a.split)
    a.spans=len(np.unique(kn))-1
    def model(nr,n,nt,shift):
        th,ang=adj.node_angles(src,phys,geo,a,n,nt,shift);period=2*np.pi/3
        th=np.sort(np.r_[0.,th[(th>1e-11)&(th<period-1e-11)],period]);th=th[np.r_[True,np.diff(th)>1e-11]]
        ss=adj.SourceAt(src,th);mm=adj.AtAngles(micro,th)
        # ref.cut_grid's Nyquist check assumes a full native circle; this
        # evaluator directly evaluates analytic modes on a D3 sector instead.
        M=a.modes;a.modes=0
        try:G=ref.cut_grid(api,mm,ss,geo,a,kn,metric,nr,len(th),shift)
        finally:a.modes=M
        q=G.t*src.S;J=G.base.copy()
        if heatdata:
            gain,ho,hg,t,l=heatdata
            H=heat.HeatOrbit(phys,geo,a,ss,api,th,int(ho),int(hg),t,l)
            J+=gain*H.correction(q,J)
        B=api.Bvals(q,oldkn)
        shape=None
        if extra is not None:shape=adj.angles_profile(phys,api,ss,geo,a,len(th),shift)[0]
        for j,(r,d) in enumerate(src.base.O):
            J[:,j]+=mm.fft_forward(B[r]@old,M,len(th),th[0],d)
            if shape is not None:
                c=B[r]@extra
                for k in range(3):J[:,j,:,k]+=c@shape[d,k]
        R=two.Rings(src,api,a,kn,metric,q,th,J,m)
        return R,dict(actualRadial=len(q),sectorNodes=len(th),materialTargets=ang,original=raw_report(J,R.Q,R.b2,micro))
    G,ga=model(97,264,16,False);T,ta=model(149,387,27,True)
    X=seed.copy();base=G.report(X,micro);baseT=T.report(X,micro);hist=[];checks=[]
    for it in range(a.steps):
        before=G.report(X,micro);other=T.report(X,micro);top=max(before['peak'],other['peak']);best=None
        for power in (.55,1.5):
            ab,grad,wt=two.assemble(G,X,power)
            if not checks:
                rng=np.random.default_rng(309317);h=rng.standard_normal(X.shape);h/=np.linalg.norm(h)
                e=2e-7;v=G.state(X+e*h);w=G.state(X-e*h)
                flat=lambda a:np.stack((a[8],np.sqrt(2)*a[9]))*wt[None]
                Jv=(flat(v)-flat(w))/(2*e);gfd=float(np.sum((flat(v)+flat(w))/2*Jv))
                Hh=ab[0]*h.ravel()
                for k in range(1,min(len(ab),h.size)):
                    A=ab[k,:h.size-k]
                    Hh[k:]+=A*h.ravel()[:-k];Hh[:-k]+=A*h.ravel()[k:]
                c1=abs(gfd-float(grad@h.ravel()))/max(1e-12,np.linalg.norm(flat(v))*np.linalg.norm(Jv))
                r1=abs(float(Hh@h.ravel())-np.sum(Jv**2))/max(1e-20,np.sum(Jv**2))
                checks=[float(c1),float(r1)]
                if max(checks)>1e-5:raise ArithmeticError('Two-field physical differential mismatch '+str(checks))
            sc=1/np.sqrt(np.maximum(1e-25,ab[0]));n=len(sc)
            for k in range(min(n,len(ab))):ab[k,:n-k]*=sc[k:]*sc[:n-k]
            dg=ab[0].copy()
            for mu in (1e-11,1e-8,1e-5,.001):
                ab[0]=dg+mu
                try:dx=(sc*solveh_banded(ab,-sc*grad,lower=True,check_finite=False)).reshape(X.shape)
                except LinAlgError:continue
                opts=[]
                for t in 2.**(-np.arange(0,21)/2):
                    y=X+t*dx
                    try:peak=max(float(G.state(y)[11].max()),float(T.state(y)[11].max()))
                    except ValueError:continue
                    if peak<top*(1-1e-11):opts.append((peak,float(t)))
                for peak,t in sorted(opts):
                    if best is not None and peak>=best[0]:break
                    y=X+t*dx;r=G.report(y,micro);s=T.report(y,micro)
                    if r['curvature']>max(a.curvature_guide,before['curvature']+1e-6) or s['curvature']>max(a.curvature_guide,other['curvature']+1e-6):continue
                    if min(r['minimumSupport'],s['minimumSupport'])<min(.115,before['minimumSupport'],other['minimumSupport']):continue
                    best=(peak,y,r,s,t,mu,power);break
            if best is not None:break
        if best is None:break
        _,X,r,s,t,mu,pow0=best;hist.append(dict(step=it+1,alpha=t,diagonalDamping=mu,weightPower=pow0,training=r,shifted=s));print('ACCEPT_ACTUAL_RINGS',it+1,r,s,flush=True)
    del G,T
    U,ua=model(205,663,49,False);initial=U.report(seed,micro);end=U.report(X,micro)
    path=a.out.with_suffix('.npz')
    with path.open('xb') as o:np.savez_compressed(o,parentSHA=sha(a.parent),entrySHA=sha(__file__),twoScalarSHA=sha(a.two_scalar_source),knots=kn,heightAndAngle=X,angularFamilies=m,angularStrength=a.angular_strength)
    output=dict(schema='R317-full-D3-rings-open-height-and-horizontal-angle-with-fixed-angular-speed-v1',
                entrySHA=sha(__file__),twoScalarSHA=sha(a.two_scalar_source),parentSHA=sha(a.parent),seedSHA=sha(a.seed) if a.seed else None,stateSHA=sha(path),fieldSHA=src.source_sha,
                angularStrength=a.angular_strength,freePhysicalScalars=X.size,frozenMetricVariables=0,radialSpans=a.spans,grid=[ga,ta,ua],initial=base,initialSecondary=baseT,accepted=hist,physicalJacobianCheck=checks,
                projectedInitialHoldout=initial,independent=end,scope='The continuous curve definition uses its D3-centered angular primitive. At unit angular strength the exact target G is prescribed on the part q<=liftEnd before blending back to the actual boundary speed. Reported E,F, curvature and support are finite quadrature observations from independent material-angle grids.')
    with a.out.open('x') as o:json.dump(output,o,indent=2);o.write('\n')
    print('END_ACTUAL_RINGS',end,flush=True)
if __name__=='__main__':main()
