#!/usr/bin/env python3
"""Continue the actual adjacent-port R262 cut with a compensated inverse-curvature heat patch, one physical amplitude, all XYZ and the same fixed g."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.linalg import solveh_banded,LinAlgError

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser()
    for key in ('scripts','work','physical-source','cut','comparison','refinement-source','angular-source','direct-source','profile-source','adjacent-source','heat-source','parent','out'):
        p.add_argument('--'+key,required=True,type=Path)
    p.add_argument('--split',action='store_true');p.add_argument('--modes',type=int,default=0)
    p.add_argument('--steps',type=int,default=4);p.add_argument('--heat-order',type=int,default=64)
    p.add_argument('--height-order',type=int,default=48);p.add_argument('--amplitude',type=float,default=None)
    p.add_argument('--late',type=float,default=.46);p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    phys=module(a.physical_source,'heat_r317_actual_radius');api=module(a.cut,'heat_actual_cut')
    ref=module(a.refinement_source,'heat_true_span_grid');ar=module(a.angular_source,'heat_native_solver_model')
    adj=module(a.adjacent_source,'heat_r317_nodes');core=module(a.profile_source,'heat_cauchy_profiles')
    direct=module(a.direct_source,'heat_banded_operator');heat=module(a.heat_source,'heat_orbit')
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','heat_r262_old_actual')
    if sha(a.physical_source)!='94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6':raise ValueError('Require the actual R317 support source')
    geo=phys.NormalCurve();api.true_arc_position=phys.true_arc_position
    core.profiles=lambda api,s,g,aa,n,sh:adj.angles_profile(phys,api,s,g,aa,n,sh)
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z or str(z['cutSHA'])!=sha(a.cut) or a.low!=phys.LOW:raise ValueError('Different original cut')
        if 'heatGain' in z:
            oldX=z['heatInletXYZ'].copy();previous=z['heatInletProfiles'].copy()
        else:
            oldX=z['inletNativeXYZ'].copy() if 'physicalInletProfiles' in z else z['actualPhysicalXYZ'].copy()
            previous=z['physicalInletProfiles'].copy() if 'physicalInletProfiles' in z else np.zeros((len(oldX),3))
        if 'inletProfileSourceSHA' in z and str(z['inletProfileSourceSHA'])!=sha(a.adjacent_source):raise ValueError('Different physical inlet profiles')
        gain=float(z['heatGain']) if 'heatGain' in z else 0.
        if 'heatGain' in z:
            if str(z['heatSourceSHA'])!=sha(a.heat_source):raise ValueError('Different heat orbit')
            a.heat_order=int(z['heatOrder']);a.height_order=int(z['heightOrder']);a.late=float(z['heatLate']);a.amplitude=float(z['heatAmplitude'])
        oldkn=z['knots'].copy();m0=int(z['modes']);mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
        frozen={k:z[k].copy() for k in ('fieldSHA','sourceSHA','comparisonSHA','cutSHA','S','T','fullGate','fullSleeve','liftEnd','lam','low','anchor','metricQ','metricW')}
    a.modes=a.modes or m0;a.material_modes=a.modes
    kn,seed=direct.transfer(oldkn,oldX,a.modes,a.split);a.spans=len(np.unique(kn))-1
    extra=core.prolong_extra(oldkn,previous,a.split)
    src=micro.Source(a)
    if (src.S,src.T)!=(a.S,a.T):raise ValueError('Wrong physical arc')
    if a.amplitude is None:a.amplitude=float(np.log(src.pos.src.metric.profile(np.array([a.full_sleeve+a.full_gate]))[0][0]))
    if not a.amplitude>=0 or not 0<a.late<1:raise ValueError('Heat time or blend geometry outside its domain')
    def model(nr,n,nt,sh):
        th,angular=adj.node_angles(src,phys,geo,a,n,nt,sh)
        ss=adj.SourceAt(src,th);mm=adj.AtAngles(micro,th)
        G,fi=core.joint_model(ref,api,mm,ss,geo,ar,direct,a,kn,oldkn,oldX,metric,nr,len(th),sh,previous)
        q=G.G.t*src.S;ix=(q>a.full_sleeve)&(q<a.full_sleeve+a.full_gate)
        base=G.base[ix].copy();raw=base.copy()
        oldB=api.Bvals(q[ix],oldkn)
        for i,(r,d) in enumerate(G.orders):
            raw[:,i]-=mm.fft_forward(oldB[r]@oldX,m0,len(th),th[0],d)
            C=oldB[r]@previous
            for j in range(3):raw[:,i,:,j]-=C@G.phi[d,j,-3:]
        H=heat.HeatOrbit(phys,geo,a,ss,api,th,a.heat_order,a.height_order,a.amplitude,a.late)
        correction=H.correction(q[ix],raw)
        def change(k):
            G.base[ix]=base+k*correction
        change(gain)
        return G,change,ix,correction,dict(angular=angular,rows=len(q),correctedRows=int(ix.sum()),maxPhysicalDisplacement=float(np.linalg.norm(correction[:,0],axis=-1).max()),initialSectionLift=float(np.linalg.norm(H.delta[0],axis=-1).max()))
    G,cg,ix,D,gn=model(101,216,13,False);T,ct,_,_,tn=model(157,321,23,True)
    X=np.zeros(G.shape);init=G.report(X);initTest=T.report(X);g0=gain
    def observe(x,k):
        cg(k);ct(k);return G.report(x),T.report(x)
    fullheat=observe(X,1.);observe(X,gain)
    def choose(dx,dk,pre,tpre):
        peak=max(pre['peak'],tpre['peak']);candidates=[]
        for alpha in 2.**(-np.arange(0,23)/2):
            y=X+alpha*dx;k=gain+alpha*dk
            cg(k);ct(k);pe=max(G.metrics(y)[3].max(),T.metrics(y)[3].max())
            if pe<peak*(1-1e-11):candidates.append((pe,float(alpha)))
        for _,alpha in sorted(candidates):
            y=X+alpha*dx;k=gain+alpha*dk;r,s=observe(y,k)
            if r['curvature']<=max(a.curvature_guide,pre['curvature']+1e-6) and s['curvature']<=max(a.curvature_guide,tpre['curvature']+1e-6) and min(r['minimumSupport'],s['minimumSupport'])>=min(.115,pre['minimumSupport'],tpre['minimumSupport']):
                return max(r['peak'],s['peak']),y,k,r,s,alpha
        return None
    hist=[];agree=None
    if gain==0:
        opts=[v for dk in (1.,-1.) if (v:=choose(np.zeros_like(X),dk,init,initTest)) is not None]
        if opts:
            _,X,gain,r,s,al=min(opts,key=lambda z:z[0]);hist.append(dict(kind='physical heat amplitude alone',gain=gain,training=r,shifted=s))
    for it in range(a.steps):
        before,secondary=observe(X,gain);best=None
        for power in (.7,1.6):
            cg(gain);ct(gain);ab,grad=direct.assemble(G,X,power)
            op,res,sc0=G.linear(X,power);sc0=sc0.ravel()
            v,u,_,err=G.metrics(X)
            ww=np.maximum(.04,err/max(1e-30,float(err.max())))**power/np.sqrt(err.size)
            dq=D[:,1];du=D[:,2];dot=lambda a,b:np.einsum('ijk,ijk->ij',a,b)
            col=np.zeros((3,)+err.shape)
            col[0,ix]=2*dot(v[ix],dq)/G.Q[ix]
            col[1,ix]=np.sqrt(2)*(dot(v[ix],du)+dot(u[ix],dq))/(G.rho[ix]*np.sqrt(G.Q[ix]*G.W[ix]))
            col[2,ix]=2*dot(u[ix],du)/(G.rho[ix]**2*G.W[ix])
            col=(col*ww[None]).ravel();sa=1/np.sqrt(max(1e-28,float(col@col)))
            sc=1/np.sqrt(np.maximum(ab[0],1e-25));n=len(sc)
            b=op.rmatvec(col)*(sc/sc0)*sa;ga=sa*float(col@res)
            if agree is None:
                cg(gain+1e-5);plus=G.metrics(X)[2];cg(gain-1e-5);minus=G.metrics(X)[2];cg(gain)
                fd=((plus-minus)*ww[None]/2e-5).ravel()
                agree=float(np.linalg.norm(fd-col)/max(1e-20,np.linalg.norm(col)))
                if agree>5e-6:raise ArithmeticError('Physical amplitude differential mismatch '+str(agree))
            for k in range(min(len(ab),n)):ab[k,:n-k]*=sc[k:]*sc[:n-k]
            diag=ab[0].copy()
            for mu in (1e-10,1e-7,1e-4,.003):
                ab[0]=diag+mu
                try:two=solveh_banded(ab,np.stack((-sc*grad,b),axis=1),lower=True,check_finite=False)
                except LinAlgError:continue
                y,z=two.T;sch=sa**2*float(col@col)+mu-float(b@z)
                if sch<=1e-15:continue
                da=(-ga-float(b@y))/sch
                dx=(sc*(y-z*da)).reshape(X.shape)
                o=choose(dx,sa*da,before,secondary)
                if o is not None and (best is None or o[0]<best[0]):best=(*o,mu,power,sch)
            if best is not None:break
        if best is None:break
        _,X,gain,r,s,al,mu,pow0,sch=best;hist.append(dict(step=it+1,alpha=al,gain=gain,damping=mu,weight=pow0,scaledSchur=sch,training=r,shifted=s))
        print('ACCEPT_HEAT',it+1,gain,r,s,flush=True)
    total=core.merged_native(G,seed,X,a.modes);outExtra=extra+X[:,-3:]
    del G,T,cg,ct,D
    F,cf,_,_,fn=model(211,621,47,False)
    cf(g0);initialHeld=F.report(np.zeros_like(X));cf(gain);end=F.report(X)
    state=a.out.with_suffix('.npz')
    with state.open('xb') as file:
        np.savez_compressed(file,**frozen,heatInletXYZ=total,heatInletProfiles=outExtra,inletProfileSourceSHA=sha(a.adjacent_source),heatGain=gain,heatSourceSHA=sha(a.heat_source),heatOrder=a.heat_order,heightOrder=a.height_order,heatLate=a.late,heatAmplitude=a.amplitude,metricKnots=mk,knots=kn,modes=a.modes,spans=a.spans)
    report=dict(schema='R317-active-physical-compensated-inverse-curvature-heat-cut-v1',entrySHA256=sha(__file__),heatSourceSHA256=sha(a.heat_source),parentSHA256=sha(a.parent),stateSHA256=sha(state),fieldSHA256=src.source_sha,
                heatTime=a.amplitude,lateGate=a.late,JacksonOrder=a.heat_order,heightPolynomialOrder=a.height_order,initialGain=g0,finalHeatGain=gain,
                physicalDefinition='The upper part beyond the actual gate end, same frozen metric, true central section with original material clock and all end 2-jets are retained. The parent native plus three profiles and the additional physical heat gain define the full changed prefix.',
                actualPositionVariables=int(X.size)+1,metricVariables=0,physicalAmplitudeDifferentialAgreement=agree,grids=[gn,tn,fn],initial=init,initialShifted=initTest,
                unitHeatGainOnParent=fullheat,accepted=hist,initialIndependent=initialHeld,independent=end)
    with a.out.open('x') as file:json.dump(report,file,indent=2);file.write('\n')
    print('END_ACTUAL_HEAT',end,flush=True)
if __name__=='__main__':main()
