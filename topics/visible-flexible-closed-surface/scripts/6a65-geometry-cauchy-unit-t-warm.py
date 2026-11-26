#!/usr/bin/env python3
"""Full new half-core supplier for a global R201 unit-T fit.

Central cylinder, real finite Cauchy ramp, exact-form R137 coast, a complete
Cartesian Hermite connector, and the original R205 tail all appear. Raw and
arclength-normalized full jets are returned at arbitrary (s,u). C2 repair of
the last short ramp cell is an explicit new field, not an exact PDE claim.
Raw coefficients and sample tables are written only outside the repository.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
from collections import OrderedDict
import numpy as np
from scipy.integrate import solve_ivp
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cauchy_warm_tail',HERE/'6a65-geometry-central-cauchy-tail.py')
tail=importlib.util.module_from_spec(spec);sys.modules[spec.name]=tail;spec.loader.exec_module(tail)
p=tail.parent;ports=p.ports;core=p.core


def S9stable(t):
    t=np.asarray(t);x=np.minimum(t,1-t)
    small=x**5*(126+x*(-420+x*(540+x*(-315+70*x))))
    return np.where(t<=.5,small,1-small)


def smooth_scalar_turn(t,L,f0,v,fc=.8):
    """Monotone slope with fifth-order arrival at both affine end slopes.

    Integral S9^2=38251/92378, integral S9^3=17141/46189 exactly.
    The unique convex mixing coefficient pays the actual end radius.
    """
    I2,I3=38251/92378,17141/46189
    target=(v-(fc-f0)/L)/(1+v);beta=(target-I2)/(I3-I2)
    if not 0<=beta<=1:raise ValueError('Selected length/radii need a different explicit scalar turn design')
    t=float(np.clip(t,0,1));S=float(S9stable(t));q=(1-beta)*S*S+beta*S**3
    dq=(2*(1-beta)*S+3*beta*S*S)*630*t**4*(1-t)**4
    gx,gw=np.polynomial.legendre.leggauss(16);gx=(gx+1)/2;gw=gw/2
    if t<=.5:
        Sq=S9stable(t*gx);integ=t*np.sum(((1-beta)*Sq**2+beta*Sq**3)*gw)
        f=f0+L*(v*t-(1+v)*integ);fs=v-(1+v)*q
    else:
        x=t+(1-t)*gx;Sq=S9stable(x);small=(1-x)**5*(126+(1-x)*(-420+(1-x)*(540+(1-x)*(-315+70*(1-x)))))
        one_minus_q=small*((1-beta)*(1+Sq)+beta*(1+Sq+Sq**2))
        f=fc+L*(1-t)-L*(1+v)*(1-t)*np.sum(one_minus_q*gw)
        small0=(1-t)**5*(126+(1-t)*(-420+(1-t)*(540+(1-t)*(-315+70*(1-t)))))
        fs=-1+(1+v)*small0*((1-beta)*(1+S)+beta*(1+S+S*S))
    return float(f),float(fs),float(-(1+v)/L*dq),float(beta)


def collect_ramp(source_samples,prefix,ramp=.18,v=.15,modes=191,nodes=33):
    raw=json.loads(Path(source_samples).read_text());seed=raw['inheritedGapLengthDesign']['centralSeed'];A,B=seed['actualCentralA'],seed['actualCentralB']
    candidate=p.Candidate(A,B,ramp,v);flow=p.hybrid.Hybrid(candidate,modes,2,30000)
    y=flow.initial();y[flow.shape_size:].reshape(flow.work,12)[:,2]=13/128
    sx=np.linspace(0,ramp,nodes);start=time.time()
    sol=solve_ivp(flow.rhs,(0,ramp),y,method='DOP853',rtol=2e-12,atol=2e-14/(1+flow.active_wave)**2,
        max_step=.0005,t_eval=sx)
    if sol.status!=0 or sol.t[-1]!=ramp:raise RuntimeError('Cauchy ramp did not reach its endpoint')
    coefficients=[];diagnostics=[]
    for s,state in zip(sx,sol.y.T):
        data=flow.frame(float(s),state);native=np.asarray(data['values'],float)
        _,_,fss=candidate.profile([s]);f=float(candidate.profile([s])[0][0]);K=-float(fss[0])/f
        l=(native[:,1]**2+K)/native[:,0]
        P,V,Aacc=native[:,2:5],native[:,5:8],l[:,None]*native[:,11:14]
        coefficients.append(np.fft.fft(np.stack((P,V,Aacc),axis=1),axis=0)/flow.work)
        diagnostics.append(flow.diagnostics(float(s),state))
    path=Path(str(prefix)+'-ramp-master.npz')
    np.savez_compressed(path,sx=sx,coefficients=np.stack(coefficients),wave=np.fft.fftfreq(flow.work,1/flow.work),
        centralA=A,centralB=B,centralLength=13/128,a0=candidate.ellipse.a0,ramp=ramp,v=v,modes=modes)
    report=dict(schema='6a65-real-Cauchy-ramp-C2-Hermite-master-nodes-v1',nfev=sol.nfev,status=sol.status,
        nodes=nodes,workAngles=flow.work,maximumMetric=max(x['metric'] for x in diagnostics),
        maximumOwnCurvature=max(x['actual_curvature'] for x in diagnostics),maximumProjectionDefect=max(x['projection_defect'] for x in diagnostics),
        outputSHA256=hashlib.sha256(path.read_bytes()).hexdigest(),seconds=time.time()-start,
        interiorNodesAreDOP853DenseInterpolants=True,exactContinuumCertificate=False)
    Path(str(prefix)+'-ramp-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report),flush=True)
    return path


def curve_from_master(path):
    d=np.load(path);raw=core.Curve.__new__(core.Curve)
    raw.modes=d['curve_modes'];raw.coeff=d['curve_coefficients'];raw.degree=int(d['degree']);raw.panels=128;raw.gauss=16
    gx,gw=np.polynomial.legendre.leggauss(16);raw.gx=(gx+1)/2;raw.gw=gw/2;raw.cuts=np.linspace(0,2*np.pi,129);raw.planar=False
    p.reset_arc(raw)
    return tail.fixed_module.FixedRadiusCurve(raw,float(d['exact_target_radius']))


def developed_tail_port(amplitude,Z,u,radius):
    """R205 at any radius, with the ORIGINAL .34/.8 profile held fixed."""
    u=np.asarray(u);count=len(u);U=ports.constant(u,count);U[1]=1;su,cu=ports.sincos(U);y=radius*su
    sign=np.where(y[0]<0,-1.,1.);ay=sign*y[0];active=ay>.34
    x=(y*sign[None,:]-ports.constant(.34,count))/.46;x[:,~active]=0
    alpha=amplitude*(126*ports.power(x,5)-420*ports.power(x,6)+540*ports.power(x,7)-315*ports.power(x,8)+70*ports.power(x,9))
    sn,cs=ports.sincos(alpha);ayjet=amplitude/.46*630*ports.mul(ports.power(x,4),ports.power(ports.constant(1,count)-x,4))*sign[None,:]
    cp=cs;hp=sn*sign[None,:];cpp=-ports.mul(sn,ayjet);hpp=ports.mul(cs,ayjet)*sign[None,:]
    gx,gw=np.polynomial.legendre.leggauss(48);gx=(gx+1)/2;gw=gw/2
    length=np.maximum(0,ay-.34);xx=length[:,None]*gx/.46
    alphaq=amplitude*(126*xx**5-420*xx**6+540*xx**7-315*xx**8+70*xx**9)
    C=sign*(np.minimum(ay,.34)+length*np.sum(np.cos(alphaq)*gw,axis=1));H=length*np.sum(np.sin(alphaq)*gw,axis=1)
    P=np.stack((radius*cu[0],C,Z-H),axis=1)
    Pu=np.stack((-radius*su[0],cp[0]*radius*cu[0],-hp[0]*radius*cu[0]),axis=1)
    Puu=np.stack((-radius*cu[0],cpp[0]*(radius*cu[0])**2-cp[0]*radius*su[0],-hpp[0]*(radius*cu[0])**2+hp[0]*radius*su[0]),axis=1)
    Vj=np.stack((-cu,-ports.mul(cp,su),ports.mul(hp,su)),axis=-1)
    Aj=np.stack((np.zeros_like(cu),ports.mul(cpp,ports.mul(su,su)),-ports.mul(hpp,ports.mul(su,su))),axis=-1)
    return dict(P=P,V=Vj[0],A=Aj[0],Pu=Pu,Vu=Vj[1],Au=Aj[1],Puu=Puu,Vuu=2*Vj[2],Auu=2*Aj[2],f=radius,fs=-1.,fss=0.)


def packet_from_port(port):
    return dict(X=port['P'],Xs=port['V'],Xss=port['A'],Xu=port['Pu'],Xsu=port['Vu'],Xuu=port['Puu'],
                Xssu=port['Au'],Xsuu=port['Vuu'],f=port['f'],fs=port['fs'],fss=port['fss'])


def connector(t,L,left,right):
    out=ports.connector_at(t,L,left,right)
    pu=np.stack([left['Pu'],left['Vu'],left['Au'],right['Pu'],right['Vu'],right['Au']])
    puu=np.stack([left['Puu'],left['Vuu'],left['Auu'],right['Puu'],right['Vuu'],right['Auu']])
    out['Xssu']=np.einsum('i,ijk->jk',ports.hermite_weights(t,L,2),pu)
    out['Xsuu']=np.einsum('i,ijk->jk',ports.hermite_weights(t,L,1),puu)
    return out


class WarmMaster:
    def __init__(self,ramp_master,coast_master,*,amplitude=.8746432018013935,Z=.51,right_length=.75,coast_length=.05):
        d=np.load(ramp_master);self.sx=d['sx'];self.coefficients=d['coefficients'];self.wave=d['wave']
        self.A,self.B=float(d['centralA']),float(d['centralB']);self.c=float(d['centralLength']);self.ramp=float(d['ramp']);self.v=float(d['v'])
        self.central=ports.ellipse_curve(self.A,self.B,self.c);self.candidate=p.Candidate(self.A,self.B,self.ramp,self.v)
        self.curve=curve_from_master(coast_master);self.coast=coast_length;self.L=right_length;self.amplitude=amplitude;self.Z=Z
        self.ramp_end=self.c+self.ramp;self.coast_end=self.ramp_end+self.coast;self.cut=self.coast_end+self.L;self.cuff=self.cut+.48
        self.cache=OrderedDict();self.angle_cache=None
    def cached(self,key,make):
        if key in self.cache:self.cache.move_to_end(key);return self.cache[key]
        value=make();self.cache[key]=value
        while len(self.cache)>8:self.cache.popitem(last=False)
        return value
    def angles(self,u):
        key=np.asarray(u).tobytes()
        if self.angle_cache is not None and self.angle_cache[0]==key:return self.angle_cache[1]
        theta=self.central.theta(u);h=np.sqrt(self.A*self.A*np.sin(theta)**2+self.B*self.B*np.cos(theta)**2)
        tu=self.central.a/h;tuu=-self.central.a**2*(self.A*self.A-self.B*self.B)*np.sin(theta)*np.cos(theta)/h**4
        phase=np.exp(1j*theta[:,None]*self.wave);out=(phase,tu,tuu);self.angle_cache=(key,out);return out
    def coast_port(self,sigma,u):
        return self.cached(('coast',float(sigma),np.asarray(u).tobytes()),lambda:ports.ruling_port(self.curve,self.v,sigma,u))
    def cut_port(self,u):
        return self.cached(('cut',np.asarray(u).tobytes()),lambda:developed_tail_port(self.amplitude,self.Z,u,.8))
    def ramp_port(self,index,u,repair=True):
        if index==0:return ports.central_port(self.A,self.B,self.c,u)
        if index==len(self.sx)-1 and repair:return self.coast_port(0.,u)
        phase,tu,tuu=self.angles(u);co=self.coefficients[index]
        val=np.einsum('uk,kcj->ucj',phase,co).real
        dt=np.einsum('uk,kcj->ucj',phase,co*(1j*self.wave[:,None,None])).real
        dtt=np.einsum('uk,kcj->ucj',phase,co*(-self.wave[:,None,None]**2)).real
        du=dt*tu[:,None,None];duu=dtt*tu[:,None,None]**2+dt*tuu[:,None,None]
        f,fs,fss=self.candidate.profile([self.sx[index]])
        return dict(P=val[:,0],V=val[:,1],A=val[:,2],Pu=du[:,0],Vu=du[:,1],Au=du[:,2],
            Puu=duu[:,0],Vuu=duu[:,1],Auu=duu[:,2],f=float(f[0]),fs=float(fs[0]),fss=float(fss[0]))
    def scalar(self,s):
        if s<=self.c:return self.central.a,0.,0.,'central'
        if s<=self.ramp_end:
            f,fs,fss=self.candidate.profile([s-self.c]);return float(f[0]),float(fs[0]),float(fss[0]),'ramp'
        if s<=self.coast_end:return self.curve.a+self.v*(s-self.ramp_end),self.v,0.,'coast'
        if s<=self.cut:
            t=(s-self.coast_end)/self.L
            f,fs,fss,beta=smooth_scalar_turn(t,self.L,self.curve.a+self.v*self.coast,self.v)
            return f,fs,fss,'right_connector'
        if s<=self.cuff+1e-12:return .8-(s-self.cut),-1.,0.,'R205_tail'
        raise ValueError('Requested s is beyond the explicit fixed flat cuff')
    def jet(self,s,u):
        u=np.asarray(u,float).reshape(-1);f,fs,fss,segment=self.scalar(float(s))
        if segment=='central':out=packet_from_port(ports.central_port(self.A,self.B,s,u))
        elif segment=='ramp':
            x=s-self.c;j=min(len(self.sx)-2,max(0,np.searchsorted(self.sx,x,side='right')-1));L=self.sx[j+1]-self.sx[j]
            out=connector((x-self.sx[j])/L,L,self.ramp_port(j,u),self.ramp_port(j+1,u))
        elif segment=='coast':out=packet_from_port(self.coast_port(s-self.ramp_end,u))
        elif segment=='right_connector':out=connector((s-self.coast_end)/self.L,self.L,self.coast_port(self.coast,u),self.cut_port(u))
        else:out=packet_from_port(developed_tail_port(self.amplitude,self.Z,u,f))
        out.update(f=f,fs=fs,fss=fss,segment=segment);return out
    def normalized(self,s,u,quadrature=1024):
        """Exact integral formula evaluated by a declared Fourier quadrature.

        C=arclength mean, a=perimeter/(2pi), lambda=f/a. The implicit angular
        map and ALL s,u two jets are differentiated before evaluating them.
        No rigorous Fourier quadrature remainder is claimed here.
        """
        u=np.asarray(u,float).reshape(-1);ug=2*np.pi*np.arange(quadrature)/quadrature;q=self.jet(s,ug)
        f,fs,fss=q['f'],q['fs'],q['fss'];base=self.jet(s,u)
        if q['segment'] in ('central','coast','R205_tail') or abs(s-self.cut)<1e-12:
            base.update(normalizationScale=1.,rawAverageRadius=f,mean=np.mean(q['X'],axis=0),materialInverseResidual=0.,
                        exactPieceBypass=True,unitT=base['Xu']/f);return base
        h=np.linalg.norm(q['Xu'],axis=1)
        if np.min(h)<=1e-6:raise ValueError('Raw angular curve is not regular on the normalization grid')
        hs=np.einsum('ij,ij->i',q['Xu'],q['Xsu'])/h
        hss=(np.sum(q['Xsu']**2,axis=1)+np.einsum('ij,ij->i',q['Xu'],q['Xssu']))/h-hs**2/h
        a,as_,ass=np.mean(h),np.mean(hs),np.mean(hss)
        M=np.mean(q['X']*h[:,None],axis=0)
        Ms=np.mean(q['Xs']*h[:,None]+q['X']*hs[:,None],axis=0)
        Mss=np.mean(q['Xss']*h[:,None]+2*q['Xs']*hs[:,None]+q['X']*hss[:,None],axis=0)
        C=M/a;Cs=(Ms-C*as_)/a;Css=(Mss-2*Cs*as_-C*ass)/a
        lam=f/a;lams=(fs-lam*as_)/a;lamss=(fss-2*lams*as_-lam*ass)/a
        wave=np.fft.fftfreq(quadrature,1/quadrature);co=np.fft.fft(np.stack((h,hs,hss),axis=1),axis=0)/quadrature
        nonzero=wave!=0;weights=co[nonzero]/(1j*wave[nonzero,None]);mom=np.asarray([a,as_,ass])
        def integrals(v):return v[:,None]*mom+(np.exp(1j*v[:,None]*wave[nonzero])-1)@weights
        v=u.copy();residual=np.inf
        for _ in range(9):
            I=integrals(v).real;raw=self.jet(s,v);hv=np.linalg.norm(raw['Xu'],axis=1);residual=I[:,0]-u*a
            if np.max(np.abs(residual))<5e-13:break
            v=np.clip(v-residual/hv,0,2*np.pi)
        else:raise RuntimeError('Actual arclength inverse did not reach its residual tolerance')
        X,S,U,SS,SU,UU=(raw[k] for k in ['X','Xs','Xu','Xss','Xsu','Xuu'])
        hv=np.linalg.norm(U,axis=1);hsv=np.einsum('ij,ij->i',U,SU)/hv;hvv=np.einsum('ij,ij->i',U,UU)/hv
        vs=(u*as_-I[:,1])/hv;vss=(u*ass-I[:,2]-2*hsv*vs-hvv*vs**2)/hv
        vu=a/hv;vuu=-a*a*hvv/hv**3;vsu=(as_-(hsv+hvv*vs)*vu)/hv
        Q=X-C;Qs=S+U*vs[:,None]-Cs
        new=dict(X=C+lam*Q,Xs=Cs+lams*Q+lam*Qs,
            Xss=Css+lamss*Q+2*lams*Qs+lam*(SS+2*SU*vs[:,None]+UU*vs[:,None]**2+U*vss[:,None]-Css),
            Xu=lam*U*vu[:,None],Xsu=lams*U*vu[:,None]+lam*((SU+UU*vs[:,None])*vu[:,None]+U*vsu[:,None]),
            Xuu=lam*(UU*vu[:,None]**2+U*vuu[:,None]),f=f,fs=fs,fss=fss,segment=q['segment'],
            normalizationScale=lam,rawAverageRadius=a,mean=C,materialInverseResidual=float(np.max(np.abs(residual))),
            exactPieceBypass=False,unitT=U/hv[:,None])
        return new


def main():
    ap=argparse.ArgumentParser();sub=ap.add_subparsers(dest='command',required=True)
    col=sub.add_parser('collect');col.add_argument('source_samples');col.add_argument('output_prefix')
    export=sub.add_parser('export');export.add_argument('ramp_master');export.add_argument('coast_master');export.add_argument('output_prefix')
    export.add_argument('--angles',type=int,default=128);export.add_argument('--quadrature',type=int,default=1024)
    export.add_argument('--Z',type=float,default=.51);export.add_argument('--amplitude',type=float,default=.8746432018013935)
    args=ap.parse_args()
    if args.command=='collect':collect_ramp(args.source_samples,args.output_prefix);return
    prefix=Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh output prefix required')
    start=time.time();master=WarmMaster(args.ramp_master,args.coast_master,Z=args.Z,amplitude=args.amplitude)
    sx=np.unique(np.r_[np.linspace(0,master.c,5),master.c+master.sx,
        master.ramp_end+np.linspace(0,master.coast,5),master.coast_end+np.linspace(0,master.L,33),
        master.cut+np.array([0,.1,.2,.3,.4,.46,.48])])
    u=2*np.pi*np.arange(args.angles)/args.angles;rows=[];saved={k:[] for k in ['rawX','rawXu','X','Xs','Xu','Xss','Xsu','Xuu','unitT','mean','f','fs','fss']}
    for j,s in enumerate(sx):
        raw=master.jet(float(s),u);norm=master.normalized(float(s),u,args.quadrature)
        rd=ports.diagnostics(raw,master.A);nd=ports.diagnostics(norm,master.A)
        for key in saved:
            value=raw['X'] if key=='rawX' else raw['Xu'] if key=='rawXu' else norm[key]
            saved[key].append(value)
        rows.append(dict(s=float(s),segment=norm['segment'],raw=rd,normalized=nd,scale=norm['normalizationScale'],
            inverseResidual=norm['materialInverseResidual'],discreteUnitTClosure=float(np.linalg.norm(np.mean(norm['unitT'],axis=0)))))
        if j%10==0 or j==len(sx)-1:print(json.dumps(dict(sample=j,total=len(sx),s=float(s),segment=norm['segment'],metric=nd['maximumRelativeMetric'],G=nd['maximumAbsGError'],curvature=nd['maximumOwnCurvature'])),flush=True)
    sample_path=Path(str(prefix)+'-samples.npz');np.savez_compressed(sample_path,s=sx,u=u,**{key:np.asarray(value) for key,value in saved.items()})
    original=master.ramp_port(len(master.sx)-1,u,repair=False);repaired=master.coast_port(0.,u)
    repair={key:float(np.max(np.linalg.norm(original[key]-repaired[key],axis=1))) for key in ['P','V','A','Pu','Vu','Puu']}
    extrema={key:max(row['normalized'][key] for row in rows) for key in ['maximumRelativeMetric','maximumOwnCurvature','maximumAbsGError','maximumRadius','maximumAbsY','maximumZ','maximumAbsProfileSlope']}
    report=dict(schema='6a65-complete-central-Cauchy-R137-R205-unit-T-warm-supplier-v1',
        parameters=dict(centralLength=master.c,rampLength=master.ramp,coastLength=master.coast,rightLength=master.L,
            physicalCut=master.cut,physicalFlatCuff=master.cuff,v=master.v,A=master.amplitude,Z=master.Z,
            fCentral=master.central.a,fRampEnd=master.curve.a,fCoastEnd=master.curve.a+master.v*master.coast,fCut=.8,fCuff=.32),
        repairedLastRampCell=dict(length=float(master.sx[-1]-master.sx[-2]),oldToExactPortTwoJetDifference=repair,
            replacementIsExplicitNewC2Field=True),
        scalarProfile='constant; v*S9 ramp; affine coast; monotone S9^2/S9^3 slope turn with fifth-order flat arrival; original R205 affine tail',
        scalarTurnBeta=smooth_scalar_turn(.5,master.L,master.curve.a+master.v*master.coast,master.v)[3],
        normalization='exact arclength-integral definition, evaluated with declared Fourier quadrature; preserves complete exact endpoint two-jets',
        angles=args.angles,quadrature=args.quadrature,normalizedExtrema=extrema,rows=rows,
        maximumDiscreteUnitTClosure=max(row['discreteUnitTClosure'] for row in rows),
        exactC2Definition=True,nonflatConnectorsNotSolved=True,continuousCertificate=False,
        outputSHA256=hashlib.sha256(sample_path.read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        seconds=time.time()-start)
    Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({key:report[key] for key in ['parameters','repairedLastRampCell','normalizedExtrema','maximumDiscreteUnitTClosure','outputSHA256','seconds']}),flush=True)


if __name__=='__main__':main()
