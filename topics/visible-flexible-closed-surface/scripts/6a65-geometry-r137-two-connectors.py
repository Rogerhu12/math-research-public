#!/usr/bin/env python3
"""Concrete new C2 half-core: central cylinder / Hermite / R137 / Hermite / R205.

The two nonlinear connectors are unsolved. Their complete E/F/G and own
curvature are measured, including full fixed Cartesian endpoint jets.
No Fourier projection of R137 output jets is used to define the connectors.
All raw reports and optional arrays must be written outside the repository.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, time
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('r137_new_inlet',HERE/'6a65-geometry-r137-exact-inlet-consumer.py')
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
O=core.ORDER
mul,inv,sqrt,diff,dot,cross,scale=core.mul,core.inv,core.sqrt,core.diff,core.dot,core.cross,core.scale


def constant(x,n):
    y=np.zeros((O+1,n));y[0]=x;return y


def power(x,k):
    out=constant(1,x.shape[1])
    for _ in range(k):out=mul(out,x)
    return out


def sincos(x):
    s=np.zeros_like(x);c=np.zeros_like(x);s[0]=np.sin(x[0]);c[0]=np.cos(x[0])
    for k in range(1,O+1):
        s[k]=sum(j*x[j]*c[k-j] for j in range(1,k+1))/k
        c[k]=-sum(j*x[j]*s[k-j] for j in range(1,k+1))/k
    return s,c


def inlet_high(curve,u,v):
    """The same master curve as the consumer, now also n/m third derivatives."""
    u=np.asarray(u).reshape(-1);theta=curve.theta(u)
    gamma=np.stack([curve.derivative(theta,j)/math.factorial(j) for j in range(O+1)])
    gp=diff(gamma);speed=sqrt(dot(gp,gp));recip=inv(speed)
    T=scale(recip,gp);lam=curve.a*recip
    def Du(x):return scale(lam,diff(x)) if x.ndim==3 else mul(lam,diff(x))
    Tu=Du(T);q=sqrt(dot(Tu,Tu));U=scale(inv(q),Tu);V=cross(T,U)
    r=v*inv(q);one=constant(1,len(u));rad=one-mul(r,r)
    if np.any(rad[0]<=0):raise ValueError('Actual new inlet has |T_u| <= v')
    d=-scale(r,U)+scale(sqrt(rad),V);N=cross(d,T)
    du=Du(d);duu=Du(du);Tuu=Du(Tu);Nu=Du(N);Nuu=Du(Nu)
    n=dot(Tu,N)/curve.a;m=dot(du,N)/curve.a
    nu,mu=Du(n),Du(m);nuu,muu=Du(nu),Du(mu);nuuu,muuu=Du(nuu),Du(muu)
    return dict(u=u,X=gamma[0],X_u=curve.a*T[0],X_uu=curve.a*Tu[0],
        e1=d[0],e1_u=du[0],e1_uu=duu[0],e2=T[0],e2_u=Tu[0],e2_uu=Tuu[0],
        N=N[0],N_u=Nu[0],N_uu=Nuu[0],n=n[0],m=m[0],n_u=nu[0],m_u=mu[0],
        n_uu=nuu[0],m_uu=muu[0],n_uuu=nuuu[0],m_uuu=muuu[0])


def ruling_port(curve,v,sigma,u):
    out=core.at_material(curve.a,v,sigma,u,lambda t:inlet_high(curve,t,v))
    t=out['material_u']-out['material_shift'];data=inlet_high(curve,t,v);count=len(u)
    nj=constant(data['n'],count);mj=constant(data['m'],count)
    for j,suffix in [(1,'_u'),(2,'_uu'),(3,'_uuu')]:
        nj[j]=data['n'+suffix]/math.factorial(j);mj[j]=data['m'+suffix]/math.factorial(j)
    kj=mul(mj,inv(nj));one=constant(1,count);k2=mul(kj,kj);a=curve.a;f=a+v*sigma
    r0=a/v;delta=sigma*(2*r0+sigma)
    W=delta*inv(r0*one+sqrt(r0*r0*one+delta*(one+k2)))
    H=a*one+v*mul(one+k2,W);D=a*one+mul(W,v*(one+k2)-diff(kj))
    nj_new=a/(f*f)*mul(nj,mul(mul(H,H),inv(D)))
    mj_new=a*a/(f*f)*mul(mul(nj,kj),mul(H,inv(D)))
    lj=mul(mul(mj_new,mj_new),inv(nj_new));t_u=mul(H,inv(D))
    def Du(x):return mul(t_u,diff(x))
    nu=Du(nj_new)[0];mu=Du(mj_new)[0];lu=Du(lj)[0];luu=Du(Du(lj))[0]
    n,m,l=nj_new[0],mj_new[0],lj[0]
    e1,e2,N=out['e1'],out['e2'],out['N']
    Nu=-f*(m[:,None]*e1+n[:,None]*e2)
    Nuu=(-f*mu+f*v*n)[:,None]*e1+(-f*nu-f*v*m)[:,None]*e2-(f*f*(m*m+n*n))[:,None]*N
    Vuu=-(v*v+f*f*m*m)[:,None]*e1-(f*f*m*n)[:,None]*e2+(f*(v*n+mu))[:,None]*N
    return dict(P=out['X'],V=out['X_s'],A=out['X_ss'],Pu=out['X_u'],Vu=out['X_su'],
        Au=lu[:,None]*N+l[:,None]*Nu,Puu=out['X_uu'],Vuu=Vuu,
        Auu=luu[:,None]*N+2*lu[:,None]*Nu+l[:,None]*Nuu,
        f=f,fs=v,fss=0.,source='one analytic R137 port; no projected independent jets',
        numericalIdentities={'secondJetRankOne':float(np.max(np.linalg.norm(out['X_ss']-l[:,None]*N,axis=1))),
        'mixedJetFrame':float(np.max(np.linalg.norm(out['X_su']-v*e2-f*m[:,None]*N,axis=1)))})


def ellipse_curve(A,B,z):
    theta=2*np.pi*np.arange(16)/16
    c=core.Curve(np.stack((A*np.cos(theta),B*np.sin(theta),np.full(16,z)),axis=1),3)
    c.coeff[:]=0;idx={int(k):j for j,k in enumerate(c.modes)}
    c.coeff[idx[0],2]=z;c.coeff[idx[1],0]=A/2;c.coeff[idx[-1],0]=A/2
    c.coeff[idx[1],1]=-1j*B/2;c.coeff[idx[-1],1]=1j*B/2
    lo=c.cuts[:-1];length=np.diff(c.cuts);q=lo[:,None]+length[:,None]*c.gx
    speed=np.linalg.norm(c.derivative(q.ravel(),1),axis=1).reshape(q.shape)
    lengths=length*np.sum(speed*c.gw,axis=1);c.cumulative=np.r_[0,np.cumsum(lengths)]
    c.perimeter=c.cumulative[-1];c.a=c.perimeter/(2*np.pi)
    return c


def central_port(A,B,z,u):
    c=ellipse_curve(A,B,z);data=inlet_high(c,u,.003);zeros=np.zeros_like(data['X']);vertical=zeros.copy();vertical[:,2]=1
    return dict(P=data['X'],V=vertical,A=zeros,Pu=data['X_u'],Vu=zeros,Au=zeros,
        Puu=data['X_uu'],Vuu=zeros,Auu=zeros,f=c.a,fs=0.,fss=0.,source='exact ellipse cylinder')


def r205_port(amplitude,Z,u,radius=.8,flat=.34):
    count=len(u);U=constant(u,count);U[1]=1;su,cu=sincos(U);y=radius*su
    sign=np.where(y[0]<0,-1.,1.);abs_y=sign*y[0];active=abs_y>flat
    x=(y*sign[None,:]-constant(flat,count))/(radius-flat)
    x[:,~active]=0
    alpha=amplitude*(126*power(x,5)-420*power(x,6)+540*power(x,7)-315*power(x,8)+70*power(x,9))
    sn,cs=sincos(alpha)
    alpha_y=amplitude/(radius-flat)*630*mul(power(x,4),power(constant(1,count)-x,4))*sign[None,:]
    cp=cs;hp=sn*sign[None,:];cpp=-mul(sn,alpha_y);hpp=mul(cs,alpha_y)*sign[None,:]
    gx,gw=np.polynomial.legendre.leggauss(48);gx=(gx+1)/2;gw=gw/2
    lengths=np.maximum(0,abs_y-flat);yy=flat+lengths[:,None]*gx
    xx=(yy-flat)/(radius-flat);al=amplitude*(126*xx**5-420*xx**6+540*xx**7-315*xx**8+70*xx**9)
    C=sign*(np.minimum(abs_y,flat)+lengths*np.sum(np.cos(al)*gw,axis=1))
    H=lengths*np.sum(np.sin(al)*gw,axis=1)
    P=np.stack((radius*cu[0],C,Z-H),axis=1)
    Pu=np.stack((-radius*su[0],cp[0]*radius*cu[0],-hp[0]*radius*cu[0]),axis=1)
    Puu=np.stack((-radius*cu[0],cpp[0]*(radius*cu[0])**2-cp[0]*radius*su[0],
                 -hpp[0]*(radius*cu[0])**2+hp[0]*radius*su[0]),axis=1)
    Vj=np.stack((-cu,-mul(cp,su),mul(hp,su)),axis=-1)
    Aj=np.stack((np.zeros_like(cu),mul(cpp,mul(su,su)),-mul(hpp,mul(su,su))),axis=-1)
    return dict(P=P,V=Vj[0],A=Aj[0],Pu=Pu,Vu=Vj[1],Au=Aj[1],Puu=Puu,Vuu=2*Vj[2],Auu=2*Aj[2],
        f=radius,fs=-1.,fss=0.,source='R205 true developed annulus master function')


# Coefficients in ascending powers of normalized physical coordinate.
HCOEFF=np.asarray([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],
                  [0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]])


def hermite_weights(t,L,derivative=0):
    coefficients=HCOEFF.copy()
    for _ in range(derivative):coefficients=coefficients[:,1:]*np.arange(1,coefficients.shape[1])
    return coefficients@np.asarray([t**j for j in range(coefficients.shape[1])])*np.asarray([1,L,L*L,1,L,L*L])/L**derivative


def connector_at(t,L,left,right):
    w=hermite_weights(t,L);ws=hermite_weights(t,L,1);wss=hermite_weights(t,L,2)
    p=np.stack([left['P'],left['V'],left['A'],right['P'],right['V'],right['A']])
    pu=np.stack([left['Pu'],left['Vu'],left['Au'],right['Pu'],right['Vu'],right['Au']])
    puu=np.stack([left['Puu'],left['Vuu'],left['Auu'],right['Puu'],right['Vuu'],right['Auu']])
    values=np.asarray([left['f'],left['fs'],left['fss'],right['f'],right['fs'],right['fss']])
    result={key:np.einsum('i,ijk->jk',weights,field) for key,weights,field in
            [('X',w,p),('Xs',ws,p),('Xss',wss,p),('Xu',w,pu),('Xsu',ws,pu),('Xuu',w,puu)]}
    result.update(f=float(w@values),fs=float(ws@values),fss=float(wss@values));return result


def diagnostics(jets,marker):
    X,S,U,SS,SU,UU=(jets[k] for k in ['X','Xs','Xu','Xss','Xsu','Xuu']);f=jets['f']
    E=np.sum(S*S,axis=1);F=np.sum(S*U,axis=1);G=np.sum(U*U,axis=1);det=E*G-F*F
    normal=np.cross(S,U);area=np.linalg.norm(normal,axis=1);normal/=area[:,None]
    bss=np.sum(SS*normal,axis=1);bsu=np.sum(SU*normal,axis=1);buu=np.sum(UU*normal,axis=1)
    tr=(G*bss-2*F*bsu+E*buu)/det;K=(bss*buu-bsu*bsu)/det
    curv=np.abs(tr)/2+np.sqrt(np.maximum(0,tr*tr/4-K))
    e=E-1;ff=F/f;g=G/(f*f)-1
    metric=np.abs(e+g)/2+np.sqrt(((e-g)/2)**2+ff*ff)
    held=np.minimum(np.linalg.norm(X-np.asarray([0,marker,0]),axis=1),np.linalg.norm(X+np.asarray([0,marker,0]),axis=1))
    return dict(maximumRelativeMetric=float(np.max(metric)),maximumOwnCurvature=float(np.max(curv)),
        maximumAbsEError=float(np.max(np.abs(e))),maximumAbsNormalizedF=float(np.max(np.abs(ff))),
        maximumAbsGError=float(np.max(np.abs(g))),minimumArea=float(np.min(area)),
        maximumRadius=float(np.max(np.linalg.norm(X,axis=1))),maximumAbsY=float(np.max(np.abs(X[:,1]))),
        maximumZ=float(np.max(X[:,2])),minimumZ=float(np.min(X[:,2])),minimumHeld=float(np.min(held)),
        minimumRadiusProfile=f,maximumRadiusProfile=f,maximumAbsProfileSlope=abs(jets['fs']))


def scan(L,left,right,angles,radials,marker):
    report=None;where={}
    for t in np.linspace(0,1,radials):
        d=diagnostics(connector_at(float(t),L,left,right),marker)
        if report is None:report=d.copy();where={k:float(t) for k in d}
        else:
            for key,value in d.items():
                worse=value<report[key] if key.startswith('minimum') else value>report[key]
                if worse:report[key]=value;where[key]=float(t)
    boundary={}
    for t,p in [(0.,left),(1.,right)]:
        j=connector_at(t,L,left,right)
        boundary[str(t)]={name:float(np.max(np.linalg.norm(j[key]-p[name],axis=1))) for key,name in
            [('X','P'),('Xs','V'),('Xss','A'),('Xu','Pu'),('Xsu','Vu'),('Xuu','Puu')]}
    return dict(length=L,angles=angles,radials=radials,finite=report,radialLocations=where,boundaryTwoJetMismatch=boundary)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('source_samples');ap.add_argument('output')
    ap.add_argument('--coast-length',type=float,default=.35);ap.add_argument('--right-length',type=float,default=.75)
    ap.add_argument('--cut-height',type=float,default=.56);ap.add_argument('--angles',type=int,default=512)
    ap.add_argument('--radials',type=int,default=65);args=ap.parse_args();start=time.time()
    if Path(args.output).exists():raise ValueError('Fresh report path required')
    raw=json.loads(Path(args.source_samples).read_text());seed=raw['inheritedGapLengthDesign']['centralSeed']
    A,B=seed['actualCentralA'],seed['actualCentralB'];c=13/128;u=2*np.pi*np.arange(args.angles)/args.angles
    curve=core.Curve([p['X'] for p in raw['points']],96,planar=True);v=.003
    inner=central_port(A,B,c,u);entry=ruling_port(curve,v,0.,u);exitp=ruling_port(curve,v,args.coast_length,u)
    outer=r205_port(raw['tailAmplitude'],args.cut_height,u)
    left_length=raw['s']-c
    report=dict(schema='6a65-R137-two-real-Cartesian-Hermite-connectors-v1',
        sourceSHA256=hashlib.sha256(Path(args.source_samples).read_bytes()).hexdigest(),
        scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        parameters=dict(centralLength=c,leftLength=left_length,coastLength=args.coast_length,rightLength=args.right_length,
            totalToCut=c+left_length+args.coast_length+args.right_length,v=v,coastA=curve.a,centralA=A,centralB=B,
            centralMetricRadius=inner['f'],tailAmplitude=raw['tailAmplitude'],trueCutHeight=args.cut_height),
        actualR137PortIdentities={'entry':entry['numericalIdentities'],'exit':exitp['numericalIdentities']},
        left=scan(left_length,inner,entry,args.angles,args.radials,A),
        right=scan(args.right_length,exitp,outer,args.angles,args.radials,A),
        unchangedExactPieces=['central ellipse cylinder','new affine R137 coast','R205 developed tail'],
        exactDefinition='Cartesian quintic Hermite matching complete P,V,A endpoint functions; plus zero unknown correction',
        angularJetDefinition='analytic master curve and R137 frame identities; no independent endpoint Fourier projection',
        completeMetricUsesAllThreeComponents=True,nonflatConnectorsUnsolved=True,continuousCertificate=False,
        actualFreeOptimizationSteps=0,seconds=time.time()-start)
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))


if __name__=='__main__':main()
