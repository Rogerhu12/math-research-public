#!/usr/bin/env python3
"""Recovered implementation of the original-g joint common-cut prefix BVP.

Reconstructed after the 2026-11-26 local executor became unavailable.
This is a new source identity; the earlier local exit-137 attempts are not
claimed as executions of this file. The mathematical source remains the
same original M12 curve, original exact-root metric, exact integrated-tail
endpoint, and common-cut-v2 C2 correction.

The r=.6 common cut is an INTERNAL tail interface, not the flat terminal.
All internal prefix interfaces move together. Exact central and common-cut
0/1/2 traces are held in this prefix consumer. Full tail and cuff extension
remain separate work. No finite residual is called an exact isometry.
"""
from __future__ import annotations
import argparse,gc,gzip,hashlib,importlib.util,io,json,math,resource,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import lsmr

HERE=Path(__file__).resolve().parent
def module(name,filename):
    spec=importlib.util.spec_from_file_location(name,HERE/filename)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result
bvp=module('recovered_prefix_bvp','6a65-m12-positive-ramp-position-bvp.py')
traces=module('recovered_prefix_traces','6a65-m12-positive-ramp-signed-coast-seam.py')
stream=module('recovered_prefix_stream','6a65-streaming-cartesian-full-gram.py')
ad=bvp.ad;LD=np.longdouble
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def midpoint(packet):return ad.base.ld((Q(packet['lo'])+Q(packet['hi']))/2)
def rss():
    try:
        record=Path('/proc/self/status').read_text().splitlines()
        return {line.split(':')[0]:line.split(':',1)[1].strip() for line in record if line.startswith(('VmRSS:','VmHWM:'))}
    except OSError:return {}

class ExactMetric:
    """Numerical evaluator of the one fixed original exact-root metric."""
    def __init__(self,meta,bridge,source_end):
        cfg=meta['frozen_profile']
        self.delta,self.vu,self.vd,self.eps,self.eta=[Q(float(cfg[k])) for k in ('delta','vu','vd','ramp','ramp_eta')]
        self.Tu=self.delta/(self.vu*(1-self.eps));self.Td=self.delta/(self.vd*(1-self.eps))
        self.prefix=self.Tu+self.Td
        self.L=midpoint(bridge['exact_L']);self.pt=midpoint(bridge['exact_pt']);self.ps=midpoint(bridge['exact_ps'])
        self.total=ad.base.ld(self.prefix)+self.L
        self.native_end=LD(source_end);self.lam=self.native_end/self.total
        self.lambda_certificate=bridge['arclength_rescale']
        self.breakpoints=[]
        for start,T in ((Q(0),self.Tu),(self.Tu,self.Td)):
            e,h=self.eps,self.eta
            for u in (Q(0),e*h,e*(1-h),e,1-e,1-e+e*h,1-e*h,Q(1)):
                self.breakpoints.append(ad.base.ld(start+T*u)/self.total)
        self.breakpoints+=list(np.linspace(float(ad.base.ld(self.prefix)/self.total),1,17))
        q,w=np.polynomial.legendre.leggauss(32)
        self.gx=(np.asarray(q,LD)+1)/2;self.gw=np.asarray(w,LD)/2

    def primitive(self,t):
        t=np.clip(np.asarray(t,LD),0,1);eta=ad.base.ld(self.eta);z=np.minimum(t,1-t);x=z/eta
        small=z<eta
        F0=np.where(small,eta/(1-eta)*(x**3-x**4/2),(z-eta/2)/(1-eta))
        P0=np.where(small,eta**2/(1-eta)*(x**4/4-x**5/10),(z*z/2-eta*z/2+3*eta*eta/20)/(1-eta))
        F=np.where(t<=LD('.5'),F0,1-F0);P=np.where(t<=LD('.5'),P0,LD('.5')-(1-t)+P0)
        Fp=np.where(small,(3*x*x-2*x**3)/(1-eta),1/(1-eta))
        return P,F,Fp

    def turn(self,z,T,v,base,sign):
        T=ad.base.ld(T);v=ad.base.ld(v);R=T*ad.base.ld(self.eps)
        z=np.asarray(z,LD);P,F,Fp=self.primitive(z/R);Pr,Fr,Fpr=self.primitive((T-z)/R)
        a=base+sign*v*(z-R/2);ap=np.full_like(z,sign*v);app=np.zeros_like(z)
        a=np.where(z<R,base+sign*v*R*P,a);ap=np.where(z<R,sign*v*F,ap);app=np.where(z<R,sign*v/R*Fp,app)
        a=np.where(z>T-R,base+sign*ad.base.ld(self.delta)-sign*v*R*Pr,a)
        ap=np.where(z>T-R,sign*v*Fr,ap);app=np.where(z>T-R,-sign*v/R*Fpr,app)
        return a,ap,app

    def profile(self,s):
        s=np.asarray(s,LD);a,ap,app=self.turn(s,self.Tu,self.vu,LD(1),1)
        b,bp,bpp=self.turn(s-ad.base.ld(self.Tu),self.Td,self.vd,1+ad.base.ld(self.delta),-1)
        down=s>ad.base.ld(self.Tu)
        a,ap,app=np.where(down,b,a),np.where(down,bp,ap),np.where(down,bpp,app)
        ids=s>=ad.base.ld(self.prefix)
        if np.any(ids):
            x=s[ids]-ad.base.ld(self.prefix);t=x/self.L
            phi=self.pt*(3*t*t-2*t*t*t)+self.L*self.ps*(t*t*t-t*t)
            phip=self.pt*(6*t-6*t*t)/self.L+self.ps*(3*t*t-2*t)
            q=t[:,None]*self.gx
            qp=self.pt*(3*q*q-2*q*q*q)+self.L*self.ps*(q*q*q-q*q)
            a[ids]=1-x*np.sum(np.sin(qp)*self.gw,axis=-1)
            ap[ids]=-np.sin(phi);app[ids]=-np.cos(phi)*phip
        return a,ap,app

class CommonCutPower:
    """Same M64 polynomial, padded and corrected only for a query span."""
    def __init__(self,old,M,start,left,width,mesh,h,corrections):
        self.old,self.M,self.start,self.left,self.width=old,M,start,left,width
        self.oldM=(old.shape[-1]-2)//3
        self.mesh,self.h,self.corrections=mesh,h,corrections
        self.shape=(old.shape[0],6,3*M+2)
    def __getitem__(self,i):
        if not isinstance(i,(int,np.integer)):raise TypeError('One radial span at a time')
        p=np.zeros((6,3*self.M+2),LD);q=self.old[i]
        p[:,0]=q[:,0];p[:,-1]=q[:,-1]
        for axis in range(3):p[:,axis*self.M+1:axis*self.M+self.oldM+1]=q[:,axis*self.oldM+1:(axis+1)*self.oldM+1]
        if i>=self.start:
            a=(self.mesh[i]-self.left)/self.width;h=self.h[i]/self.width
            for j in range(6):
                for degree,corr in zip((3,4,5),self.corrections):
                    if degree>=j:p[j]+=math.comb(degree,j)*a**(degree-j)*h**j*corr
        return p

class CommonCutSource(ad.base.Source):
    """Original common-cut-v2 definition from the exact recovered tail sum."""
    def __init__(self,data,meta_path,bridge_path,endpoint_report,endpoint_cache):
        super().__init__(data,meta_path)
        report=json.loads(Path(endpoint_report).read_text());bridge=json.loads(Path(bridge_path).read_text())
        if sha(endpoint_cache)!=report['endpoint_cache_sha256'] or report['manifest_sha256']!=self.meta['tail_manifest_sha256']:
            raise ValueError('Recovered tail endpoint identity mismatch')
        if sha(bridge_path)!=self.meta['bridge_parameter_certificate_sha256']:
            raise ValueError('Exact bridge identity mismatch')
        self.metric=ExactMetric(self.meta,bridge,self.end)
        with np.load(endpoint_cache,allow_pickle=False) as z:
            exact=[Q(int(a),int(b)) for a,b in zip(z['endpoint_numerator'],z['endpoint_denominator'])]
            endpoint=np.asarray([ad.base.ld(q) for q in exact],LD)
            cut_traces=[endpoint,np.asarray(z['first'],LD),np.asarray(z['second'],LD)]
            pm,hm=z['planar_modes'].copy(),z['height_modes'].copy()
        M=int(self.meta['modes']);oldM=self.M;P=len(pm)
        if M<max(oldM,max(abs((pm-1)//3)),max(hm//3)):raise ValueError('Incomplete common Fourier basis')
        T=np.zeros((3,3*M+2),LD);lookup={int(k):j for j,k in enumerate(pm)}
        for order,row in enumerate(cut_traces):
            def get(k):return row[lookup[k]] if k in lookup else LD(0)
            T[order,0]=get(1)
            for j in range(1,M+1):
                a,b=get(1+3*j),get(1-3*j);T[order,j]=a+b;T[order,M+j]=a-b
            for j,k in enumerate(hm):T[order,-1 if k==0 else 2*M+int(k)//3]=-row[P+j]
        with np.load(io.BytesIO(gzip.decompress(Path(data).read_bytes())),allow_pickle=False) as raw:
            stored=np.asarray(raw['jets'][:,-1,:],LD)
            mean=sum((Q.from_float(float(x)) for x in raw['mean_increments']),Q(0))
        Y=np.zeros_like(T);Y[:,0]=stored[:,0];Y[:,-1]=stored[:,-1]
        for axis in range(3):Y[:,axis*M+1:axis*M+oldM+1]=stored[:,axis*oldM+1:(axis+1)*oldM+1]
        Y[0,-1]=ad.base.ld(mean)
        c=ad.base.ld(Q(bridge['physical_cut_radius_exact']));w=LD('.5');wr=-7*w/c;E=1+w*w
        k=-1/np.sqrt(E);k2=-w*wr/(E*E);lam=self.metric.lam
        T[0,0]+=c;T[1,0]+=1
        self.cut_height=Y[0,-1]-T[0,-1]
        T[0,-1]=Y[0,-1];T[1,-1]-=w;T[2,-1]-=wr
        target=np.stack((T[0],k/lam*T[1],(k*k*T[2]+k2*T[1])/(lam*lam)))
        delta=target-Y;delta[0,-1]=0
        start=int(self.meta['correction_start_index']);left=self.mesh[start];width=self.end-left
        corrections=np.stack((10*delta[0]-4*width*delta[1]+width*width*delta[2]/2,
                              -15*delta[0]+7*width*delta[1]-width*width*delta[2],
                              6*delta[0]-3*width*delta[1]+width*width*delta[2]/2))
        self.power=CommonCutPower(self.power,M,start,left,width,self.mesh,self.h,corrections)
        self.M=M;self.cut_delta=delta;self.common_cut_target=target
        self.source_identity={'data_sha256':sha(data),'common_meta_sha256':sha(meta_path),
                              'bridge_sha256':sha(bridge_path),'endpoint_report_sha256':sha(endpoint_report),
                              'endpoint_cache_sha256':sha(endpoint_cache),
                              'original_common_cut_producer_sha256':self.meta['common_cut_implementation_sha256']}

    def chart_all(self,s):
        x=LD(s)/self.end
        if x<0 or x>1+LD('1e-18'):raise ValueError('Outside full common-cut prefix')
        j=min(np.searchsorted(self.sx,x,side='right')-1,len(self.sc)-1);j=max(0,j)
        h=x-self.sx[j];p=self.sc[j]
        e=((p[3]*h+p[2])*h+p[1])*h+p[0]
        ep=((3*p[3]*h+2*p[2])*h+p[1])/self.end
        epp=(6*p[3]*h+2*p[2])/(self.end*self.end)
        if x>=LD('.75'):
            t=4*x-3;z=1-10*t**3+15*t**4-6*t**5
            zp=4/self.end*(-30*t*t+60*t**3-30*t**4)
            zpp=(4/self.end)**2*(-60*t+180*t*t-120*t**3)
            e,ep,epp=e*z,ep*z+e*zp,epp*z+2*ep*zp+e*zpp
        return self.warp*e,self.warp*ep,self.warp*epp

    def chart(self,s):return self.chart_all(s)[:2]

    def point(self,x,u):
        """Own two-jets in physical s and true material u; x=s/S*."""
        s=self.end*LD(x);u=np.asarray(u,LD)
        e,ep,epp=self.chart_all(s);psi=u.copy()
        for unused in range(12):psi-=(psi-e*np.sin(3*psi)/3-u)/(1-e*np.cos(3*psi))
        if np.max(abs(psi-e*np.sin(3*psi)/3-u))>LD('2e-17'):
            raise ArithmeticError('Material-angle inversion residual')
        i=min(max(0,int(np.searchsorted(self.mesh,s,side='right')-1)),len(self.h)-1)
        c,d=self.coefficients(i,s);t=(s-self.mesh[i])/self.h[i];p=self.power[i]
        dd=20*p[5]
        for k in range(4,1,-1):dd=dd*t+k*(k-1)*p[k]
        dd/=self.h[i]**2
        M=self.M;k=np.arange(3,3*M+1,3,dtype=LD);co,si=np.cos(k[:,None]*psi),np.sin(k[:,None]*psi)
        def terms(a):
            R=a[0]+a[1:M+1]@co;T=a[M+1:2*M+1]@si;Z=a[-1]+a[2*M+1:3*M+1]@co
            Rp=-(k*a[1:M+1])@si;Tp=(k*a[M+1:2*M+1])@co;Zp=-(k*a[2*M+1:3*M+1])@si
            Rpp=-(k*k*a[1:M+1])@co;Tpp=-(k*k*a[M+1:2*M+1])@si;Zpp=-(k*k*a[2*M+1:3*M+1])@co
            return np.stack((R,T,Z),axis=-1),np.stack((Rp-T,Tp+R,Zp),axis=-1),np.stack((Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp),axis=-1)
        X,Xp,Xpp=terms(c);Xs,Xsp,_=terms(d);Xss,_,_=terms(dd)
        rho=1-e*np.cos(3*psi);nu=-ep*np.sin(3*psi)/3
        uss=-epp*np.sin(3*psi)/3;usp=-ep*np.cos(3*psi);upp=3*e*np.sin(3*psi)
        ps=-nu/rho;pu=1/rho
        pss=-(uss+2*usp*ps+upp*ps*ps)/rho
        psu=-(usp+upp*ps)/(rho*rho);puu=-upp/(rho*rho*rho)
        col=lambda q:q[:,None];lam=self.metric.lam
        out=[X,lam*(Xs+col(ps)*Xp),col(pu)*Xp,
             lam*lam*(Xss+2*col(ps)*Xsp+col(ps*ps)*Xpp+col(pss)*Xp),
             lam*(col(pu)*Xsp+col(ps*pu)*Xpp+col(psu)*Xp),col(pu*pu)*Xpp+col(puu)*Xp]
        cp,sp=np.cos(psi),np.sin(psi)
        def cart(v):return np.stack((cp*v[:,0]-sp*v[:,1],sp*v[:,0]+cp*v[:,1],v[:,2]),axis=-1).astype(float)
        return np.stack([cart(v) for v in out])


class FixedPortBasis(bvp.Basis):
    def __init__(self,mesh,order,total):
        super().__init__(mesh,order)
        self.total=float(total);self.full_nb=self.nb;self.nb-=6
        if self.nb<2:raise ValueError('Insufficient interior basis')
    def matrices(self,x):
        return [csr_matrix(self.spline(x,nu=j)[:,3:-3]/self.total**j) for j in range(3)]

def mesh_and_quadrature(src,elements,gauss):
    mesh=np.unique(np.r_[np.linspace(0,1,elements+1),np.asarray(src.metric.breakpoints,float),
                         np.asarray(src.sx,float),.75,float(src.common_start/src.end)])
    mesh=mesh[(mesh>=0)&(mesh<=1)];mesh[0]=0;mesh[-1]=1
    mesh=mesh[np.r_[True,np.diff(mesh)>1e-13]]
    x,w=np.polynomial.legendre.leggauss(gauss)
    nodes=((mesh[:-1]+mesh[1:])[:,None]/2+(mesh[1:]-mesh[:-1])[:,None]*x/2).ravel()
    weights=((mesh[1:]-mesh[:-1])[:,None]*w/2*float(src.metric.total)).ravel()
    return mesh,nodes,weights

def background(src,central,x,N,cache=None):
    if cache is None:cache={}
    if N not in cache:
        u,rho,rhop=bvp.central_chart(central,N)
        old=traces.old_port_traces(src,LD(0),u,rho,rhop,src.metric.lam)
        theta=np.arange(N)*2*np.pi/N;normalized=ad.FixedRadiusCurve(central,1.)
        target=np.zeros_like(old)
        for j in range(3):target[0,j]=normalized.derivative(theta,j)
        target[1,0,:,2]=1
        cache[N]=(u,rho,rhop,target-old)
    u,rho,rhop,delta=cache[N];data=[]
    h=ad.base.ld(src.metric.Tu*src.metric.eps)
    poly=np.asarray([[1,0,0,-10,15,-6],[0,h,0,-6*h,8*h,-3*h],
                     [0,0,h*h/2,-3*h*h/2,3*h*h/2,-h*h/2]],LD)
    pd=poly[:,1:]*np.arange(1,6,dtype=LD)/h;pdd=pd[:,1:]*np.arange(1,5,dtype=LD)/h
    for z in x:
        p=src.point(z,u);p[2]*=rho[:,None];p[4]*=rho[:,None]
        p[5]=p[5]*rho[:,None]**2+(p[2]/rho[:,None])*rhop[:,None]
        s=LD(z)*src.metric.total
        if s<=h:
            t=s/h;v=np.polynomial.polynomial.polyval(t,poly.T)
            dv=np.polynomial.polynomial.polyval(t,pd.T);ddv=np.polynomial.polynomial.polyval(t,pdd.T)
            p[0]+=np.einsum('a,and->nd',v,delta[:,0]);p[1]+=np.einsum('a,and->nd',dv,delta[:,0])
            p[2]+=np.einsum('a,and->nd',v,delta[:,1]);p[3]+=np.einsum('a,and->nd',ddv,delta[:,0])
            p[4]+=np.einsum('a,and->nd',dv,delta[:,1]);p[5]+=np.einsum('a,and->nd',v,delta[:,2])
        data.append(p)
    a=np.asarray(src.metric.profile(np.asarray(x,LD)*src.metric.total)[0],float)
    return np.asarray(data),a[:,None]*rho[None,:]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--endpoint-report',type=Path,required=True)
    ap.add_argument('--endpoint-cache',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--elements',type=int,default=80);ap.add_argument('--order',type=int,default=32)
    ap.add_argument('--angular',type=int,default=384);ap.add_argument('--gauss',type=int,default=6)
    ap.add_argument('--iterations',type=int,default=800);ap.add_argument('--newton',type=int,default=1)
    ap.add_argument('--block',type=int,default=24);args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    if args.angular<=2*(3*args.order+1):raise ValueError('Angular basis aliases')
    if args.block<1 or args.newton<1:raise ValueError('Positive block and Newton counts required')
    start=time.monotonic();meta=HERE.parent/'notes'/ad.base.META_NAME
    bridge=HERE.parent/'notes/2026-11-09-db6f-root-exact-bridge-m12.json'
    src=CommonCutSource(args.data,meta,bridge,args.endpoint_report,args.endpoint_cache)
    unused,central_c=ad.exact_section(args.data,Q(0));central=ad.NativeCurve(central_c,512,32)
    mesh,x,weights=mesh_and_quadrature(src,args.elements,args.gauss)
    basis=FixedPortBasis(mesh,args.order,src.metric.total)
    print(json.dumps({'phase':'source-ready','prefix_radius_at_cut':float(src.metric.profile([src.metric.total])[0][0]),
                      'lambda_numerical':float(src.metric.lam),'elements':len(mesh)-1,'unknowns':basis.nb*basis.na,'memory':rss()}),flush=True)
    cache={};source_background=lambda xx,NN:background(src,central,xx,NN,cache)
    coeff=np.zeros((basis.nb,basis.na))
    initial=stream.observe(basis,x,weights,source_background,coeff,args.angular,args.block)
    print(json.dumps({'initial':initial,'memory':rss()}),flush=True)
    rows=[];adjoint_error=None
    for step in range(args.newton):
        op=stream.StreamingLinearized(basis,x,weights,source_background,coeff,args.angular,args.block)
        if step==0:
            rng=np.random.default_rng(2718);a=rng.normal(size=op.shape[1]);z=rng.normal(size=op.shape[0])
            aa=np.dot(op.matvec(a),z);zz=np.dot(a,op.rmatvec(z));adjoint_error=abs(aa-zz)/max(1,abs(aa),abs(zz))
            if adjoint_error>1e-10:raise ArithmeticError('Global J/JT mismatch')
            del a,z;gc.collect()
        print(json.dumps({'phase':'operator-ready','memory':rss()}),flush=True)
        scale=1e9;rhs=-op.residual.ravel()*scale;del op.residual;gc.collect()
        solution=lsmr(op.operator,rhs,atol=1e-10,btol=1e-10,conlim=1e12,maxiter=args.iterations)
        change=op.unpack(solution[0])/scale;before=op.statistics
        del op,rhs;gc.collect()
        accepted=None;attempts=[]
        for alpha in (1.,.5,.25,.125,.0625):
            stat=stream.observe(basis,x,weights,source_background,coeff+alpha*change,args.angular,args.block)
            attempts.append({'alpha':alpha,**stat})
            if stat['weighted_energy']<before['weighted_energy'] and stat['metric_peak']<=1.05*before['metric_peak']:
                accepted=alpha;coeff+=alpha*change;break
        row={'step':step,'lsmr_stop':int(solution[1]),'lsmr_iterations':int(solution[2]),'lsmr_residual':float(solution[3])/scale,
             'condition_estimate':float(solution[6]),'accepted_alpha':accepted,'attempts':attempts,'memory':rss()}
        rows.append(row);print(json.dumps(row),flush=True)
        if accepted is None:break
    omesh,ox,ow=mesh_and_quadrature(src,args.elements,args.gauss+2)
    old_observation=stream.observe(basis,ox,ow,source_background,np.zeros_like(coeff),2*args.angular,args.block)
    new_observation=stream.observe(basis,ox,ow,source_background,coeff,2*args.angular,args.block)
    boundary=basis.matrices([0.,1.]);boundary_error=[float(np.max(abs(m@coeff))) for m in boundary]
    np.savez_compressed(str(args.out)+'.field.npz',coefficients=coeff,unit_knots=basis.knots,
                        planar_modes=basis.pm,vertical_modes=basis.zm,
                        central_c_numerator=np.asarray([str(q.numerator) for q in central_c]),
                        central_c_denominator=np.asarray([str(q.denominator) for q in central_c]))
    out={'schema':'6a65-original-M12-global-common-cut-prefix-joint-position-BVP-recovered-v1','script_sha256':sha(__file__),
         'source':src.source_identity,'linear_operator_sha256':sha(HERE/'6a65-m12-positive-ramp-position-bvp.py'),
         'streaming_operator_sha256':sha(HERE/'6a65-streaming-cartesian-full-gram.py'),
         'field_sha256':sha(str(args.out)+'.field.npz'),'original_exact_metric_unchanged':True,
         'exact_bridge_root_used':True,'physical_length_numerical':float(src.metric.total),'lambda_numerical':float(src.metric.lam),
         'basis_unit_coordinate':'x=s/S_star=native/S0; saved binary unit knots, exact S_star from original bridge root',
         'elements':len(mesh)-1,'order':args.order,'unknowns':int(coeff.size),'angular':args.angular,'gauss':args.gauss,
         'analytic_adjoint_relative_error':float(adjoint_error),'initial_training':initial,'rows':rows,
         'independent_observer_before':old_observation,'independent_observer_after':new_observation,
         'independent_peak_physical_s':float(ox[new_observation['peak_radial_index']]*src.metric.total),
         'central_and_common_cut_0_1_2_jet_correction_max':boundary_error,
         'central_reference':'Exact arclength normalization of original rational central curve to f=1; Xs=ez, Xss=0; installed over the whole first ramp by full two-jet Hermite correction before solving',
         'all_internal_prefix_interfaces_free':True,'common_cut_is_internal_tail_seam_not_flat_terminal':True,
         'tail_and_true_flat_collar_not_solved_in_this_run':True,'continuous_metric_certificate':False,
         'whole_closed_surface_constructed':False,'block':args.block,
         'resident_high_water_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(out,indent=2,allow_nan=False))

if __name__=='__main__':main()
