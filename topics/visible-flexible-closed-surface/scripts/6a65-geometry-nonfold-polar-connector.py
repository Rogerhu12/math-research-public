#!/usr/bin/env python3
"""New nonfolded polar connector with complete analytic endpoint two jets.

This file does not alter the certified prefix or the active q1 Cartesian model.
The radius metric is supplied independently; no perimeter of this new field
is silently declared to be its target metric. Positivity checks are sampled
unless a separate continuous angular certificate is explicitly supplied.
"""
from __future__ import annotations
import os
for _key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[_key]="1"
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.special import comb


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m
    spec.loader.exec_module(m);return m


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def mul(a,b):
    if a.shape[0]!=b.shape[0]:raise ValueError("Same Taylor order required")
    out=np.zeros(np.broadcast_shapes(a.shape,b.shape))
    for k in range(a.shape[0]):
        for j in range(k+1):out[k]+=a[j]*b[k-j]
    return out


def inv(a):
    out=np.zeros_like(a);out[0]=1/a[0]
    for k in range(1,len(a)):
        out[k]=-sum(a[j]*out[k-j] for j in range(1,k+1))/a[0]
    return out


def sqrt(a):
    out=np.zeros_like(a);out[0]=np.sqrt(a[0])
    for k in range(1,len(a)):
        out[k]=(a[k]-sum((out[j]*out[k-j] for j in range(1,k)),np.zeros_like(a[0])))/(2*out[0])
    return out


def diff(a):
    out=np.zeros_like(a)
    for j in range(len(a)-1):out[j]=(j+1)*a[j+1]
    return out


def dotxy(a,b):return mul(a[:,:,0],b[:,:,0])+mul(a[:,:,1],b[:,:,1])
def crossxy(a,b):return mul(a[:,:,0],b[:,:,1])-mul(a[:,:,1],b[:,:,0])


def higher_coast_port(master,sigma,u):
    """R137 frame differentiation: P through u4, V through u3, A through u2."""
    ports=master._ports;core=ports.core
    u=np.asarray(u,float).reshape(-1);v=master.v;curve=master.curve
    out=core.at_material(curve.a,v,sigma,u,lambda t:ports.inlet_high(curve,t,v))
    t=out["material_u"]-out["material_shift"]
    data=ports.inlet_high(curve,t,v);count=len(u)
    nj=ports.constant(data["n"],count);mj=ports.constant(data["m"],count)
    for j,suffix in ((1,"_u"),(2,"_uu"),(3,"_uuu")):
        nj[j]=data["n"+suffix]/math.factorial(j)
        mj[j]=data["m"+suffix]/math.factorial(j)
    kj=ports.mul(mj,ports.inv(nj));one=ports.constant(1,count)
    k2=ports.mul(kj,kj);a=curve.a;f=a+v*sigma
    r0=a/v;delta=sigma*(2*r0+sigma)
    W=delta*ports.inv(r0*one+ports.sqrt(r0*r0*one+delta*(one+k2)))
    H=a*one+v*ports.mul(one+k2,W)
    D=a*one+ports.mul(W,v*(one+k2)-ports.diff(kj))
    nn=a/(f*f)*ports.mul(nj,ports.mul(ports.mul(H,H),ports.inv(D)))
    mm=a*a/(f*f)*ports.mul(ports.mul(nj,kj),ports.mul(H,ports.inv(D)))
    ll=ports.mul(ports.mul(mm,mm),ports.inv(nn));tu=ports.mul(H,ports.inv(D))
    def Du(x):return ports.mul(tu,ports.diff(x))
    n,m,l=nn[0],mm[0],ll[0]
    nu,mu,lu=Du(nn)[0],Du(mm)[0],Du(ll)[0]
    nuu,muu,luu=Du(Du(nn))[0],Du(Du(mm))[0],Du(Du(ll))[0]
    e1,e2,N=out["e1"],out["e2"],out["N"]
    def frame(a,b,c):return a[:,None]*e1+b[:,None]*e2+c[:,None]*N
    def derivative(a,b,c,au,bu,cu):
        return frame(au-v*b-f*m*c,v*a+bu-f*n*c,f*m*a+f*n*b+cu)
    Nu=frame(-f*m,-f*n,np.zeros_like(n))
    Nuu=frame(-f*mu+f*v*n,-f*nu-f*v*m,-f*f*(m*m+n*n))
    P3a=-f**3*m*n;P3b=-f*(v*v+f*f*n*n);P3c=f*f*(nu-v*m)
    Puuu=frame(P3a,P3b,P3c)
    Puuuu=derivative(P3a,P3b,P3c,-f**3*(mu*n+m*nu),
        -2*f**3*n*nu,f*f*(nuu-v*mu))
    V2a=-v*v-f*f*m*m;V2b=-f*f*m*n;V2c=f*(v*n+mu)
    Vuu=frame(V2a,V2b,V2c)
    Vuuu=derivative(V2a,V2b,V2c,-2*f*f*m*mu,
        -f*f*(mu*n+m*nu),f*(v*nu+muu))
    return dict(P=out["X"],V=out["X_s"],A=out["X_ss"],
        Pu=out["X_u"],Vu=out["X_su"],Au=lu[:,None]*N+l[:,None]*Nu,
        Puu=out["X_uu"],Vuu=Vuu,Auu=luu[:,None]*N+2*lu[:,None]*Nu+l[:,None]*Nuu,
        Puuu=Puuu,Puuuu=Puuuu,Vuuu=Vuuu,f=f,fs=v,fss=0.)


def higher_tail_port(master,u,radius=.8):
    """The ORIGINAL R205 profile .34/.8; differentiate its one master function."""
    ports=master._ports;warm=master._warm
    u=np.asarray(u,float).reshape(-1);count=len(u)
    U=ports.constant(u,count);U[1]=1;su,cu=ports.sincos(U);y=radius*su
    sign=np.where(y[0]<0,-1.,1.);active=sign*y[0]>.34
    x=(y*sign[None,:]-ports.constant(.34,count))/.46;x[:,~active]=0
    alpha=master.amplitude*(126*ports.power(x,5)-420*ports.power(x,6)
        +540*ports.power(x,7)-315*ports.power(x,8)+70*ports.power(x,9))
    sn,cs=ports.sincos(alpha)
    cp=cs;hp=sn*sign[None,:]
    Puj=np.stack((-radius*su,ports.mul(cp,radius*cu),-ports.mul(hp,radius*cu)),axis=-1)
    Vj=np.stack((-cu,-ports.mul(cp,su),ports.mul(hp,su)),axis=-1)
    out=warm.developed_tail_port(master.amplitude,master.Z,u,radius)
    out.update(Puuu=2*Puj[2],Puuuu=6*Puj[3],Vuuu=6*Vj[3])
    return out


def packed(port,name):
    out=np.zeros((5,len(port[name]),3))
    for j in range(5):
        key=name+"u"*j
        if key in port:out[j]=port[key]/math.factorial(j)
    return out


def endpoint_clock(port,u):
    P,V,A=(packed(port,key) for key in ("P","V","A"))
    R2=dotxy(P,P);rec=inv(R2)
    phiu=mul(crossxy(P,diff(P)),rec)
    phis=mul(crossxy(P,V),rec)
    phiss=mul(crossxy(P,A),rec)-2*mul(mul(dotxy(P,V),rec),phis)
    x,y=P[0,:,:2].T
    phi=u+np.arctan2(y*np.cos(u)-x*np.sin(u),x*np.cos(u)+y*np.sin(u))
    q=np.stack((phi,phiu[0],phiu[1]))
    qs=np.stack((phis[0],phis[1],2*phis[2]))
    qss=np.stack((phiss[0],phiss[1],2*phiss[2]))
    return dict(phi=q,phis=qs,phiss=qss,phiuSeries=phiu,
        phisSeries=phis,phissSeries=phiss,P=P,V=V,A=A)


def polar_profiles(clock):
    """Values and first two polar-angle derivatives of all physical s-port jets."""
    P,V,A=(clock[key] for key in ("P","V","A"))
    rho=sqrt(dotxy(P,P));rec=inv(rho)
    rs=mul(dotxy(P,V),rec)
    rss=mul(dotxy(V,V)+dotxy(P,A)-mul(rs,rs),rec)
    ru,ruu=diff(rho),diff(diff(rho));rsu=diff(rs)
    pu=clock["phiuSeries"];ps=clock["phisSeries"];pss=clock["phissSeries"]
    us=-mul(ps,inv(pu))
    uss=-mul(pss+2*mul(diff(ps),us)+mul(diff(pu),mul(us,us)),inv(pu))
    fixed_rs=rs+mul(ru,us)
    fixed_rss=rss+2*mul(rsu,us)+mul(ruu,mul(us,us))+mul(ru,uss)
    Z=P[:,:,2];ZS=V[:,:,2];ZSS=A[:,:,2]
    fixed_zs=ZS+mul(diff(Z),us)
    fixed_zss=ZSS+2*mul(diff(ZS),us)+mul(diff(diff(Z)),mul(us,us))+mul(diff(Z),uss)
    def angular_taylor(a):
        # u(theta) derivatives; return Taylor coefficients in theta.
        return np.stack((a[0],a[1]/pu[0],
            a[2]/pu[0]**2-a[1]*pu[1]/(2*pu[0]**3)))
    R,RS,RSS=(angular_taylor(a) for a in (rho,fixed_rs,fixed_rss))
    Z,ZS,ZSS=(angular_taylor(a) for a in (Z,fixed_zs,fixed_zss))
    logR=np.stack((np.log(R[0]),R[1]/R[0],
        R[2]/R[0]-.5*(R[1]/R[0])**2))
    logRS=mul(RS,inv(R))
    logRSS=mul(RSS,inv(R))-mul(logRS,logRS)
    derivatives=lambda a:np.stack((a[0],a[1],2*a[2]))
    return dict(logrho=np.stack([derivatives(a) for a in (logR,logRS,logRSS)]),
        z=np.stack([derivatives(a) for a in (Z,ZS,ZSS)]),
        rho=np.stack([derivatives(a) for a in (R,RS,RSS)]))


def bernstein(t,n):
    k=np.arange(n+1)
    return comb(n,k,exact=False)*(t**k)*((1-t)**(n-k))


class NonfoldPolarConnector:
    def __init__(self,scripts,ramp,coast,*,right_length=.7956739498716915,
                 amplitude=.8746432018013935,Z=.51,velocity_degree=31):
        self.scripts=Path(scripts).resolve()
        self.warm=module(self.scripts/"6a65-geometry-cauchy-unit-t-warm.py","nonfold_complete_warm")
        self.master=self.warm.WarmMaster(ramp,coast,amplitude=amplitude,Z=Z,
            right_length=right_length,coast_length=.02)
        self.master._ports=self.warm.ports;self.master._warm=self.warm
        self.L=right_length;self.degree=velocity_degree
        if self.degree<5:raise ValueError("Velocity degree >=5 required")
        self.b=self.master.coast_end;self.S=self.master.cut;self.cuff=self.master.cuff
        self.providers=(lambda u:higher_coast_port(self.master,self.master.coast,u),
                        lambda u:higher_tail_port(self.master,u))
        self.clock_cache=None
        self.identities=dict(sourceSHA256=sha(__file__),
            rampMasterSHA256=sha(ramp),coastMasterSHA256=sha(coast),
            warmSourceSHA256=sha(self.scripts/"6a65-geometry-cauchy-unit-t-warm.py"),
            analyticPortSourceSHA256=sha(self.scripts/"6a65-geometry-r137-two-connectors.py"))
    def endpoint_clocks(self,u):
        key=np.asarray(u).tobytes()
        if self.clock_cache is not None and self.clock_cache[0]==key:return self.clock_cache[1]
        out=[endpoint_clock(provider(u),u) for provider in self.providers]
        self.clock_cache=(key,out)
        return out
    def inverse(self,side,theta):
        u=np.asarray(theta,float).reshape(-1).copy()
        for iteration in range(15):
            port=self.providers[side](u);clock=endpoint_clock(port,u)
            error=np.arctan2(np.sin(clock["phi"][0]-theta),np.cos(clock["phi"][0]-theta))
            if np.any(clock["phi"][1]<=0):raise ArithmeticError("Polar inverse orientation failed")
            if np.max(abs(error))<5e-14:return polar_profiles(clock),float(np.max(abs(error)))
            u-=error/clock["phi"][1]
        raise ArithmeticError("Actual endpoint angle inverse failed")
    def connector(self,s,u):
        u=np.asarray(u,float).reshape(-1);t=(float(s)-self.b)/self.L
        if not -2e-15<=t<=1+2e-15:raise ValueError("Connector s outside its physical domain")
        t=float(np.clip(t,0,1));L=self.L
        left_clock,right_clock=self.endpoint_clocks(u)
        clock_data=np.concatenate([np.stack([x["phi"],x["phis"],x["phiss"]])
            for x in (left_clock,right_clock)],axis=0)
        clock=np.stack([np.einsum("i,ijk->jk",self.warm.ports.hermite_weights(t,L,j),clock_data)
            for j in range(3)])
        theta=clock[0,0]
        left,er0=self.inverse(0,theta);right,er1=self.inverse(1,theta)
        logrho_data=np.concatenate([left["logrho"],right["logrho"]],axis=0)
        Q=np.stack([np.einsum("i,ijk->jk",self.warm.ports.hermite_weights(t,L,j),logrho_data)
            for j in range(3)])
        R=np.exp(Q[0,0]);Rs=R*Q[1,0];Rt=R*Q[0,1]
        Rss=R*(Q[2,0]+Q[1,0]**2)
        Rst=R*(Q[1,1]+Q[1,0]*Q[0,1])
        Rtt=R*(Q[0,2]+Q[0,1]**2)
        n=self.degree;lz,rz=left["z"],right["z"]
        controls=np.empty((n+1,3,len(u)))
        controls[0]=lz[1];controls[1]=lz[1]+L*lz[2]/n
        controls[-1]=rz[1];controls[-2]=rz[1]-L*rz[2]/n
        inner=((n+1)*(rz[0]-lz[0])/L-
            controls[0]-controls[1]-controls[-2]-controls[-1])/(n-3)
        controls[2:-2]=inner
        zcontrols=np.concatenate([lz[0][None],lz[0][None]+L/(n+1)*np.cumsum(controls,axis=0)],axis=0)
        z=np.einsum("i,ijk->jk",bernstein(t,n+1),zcontrols)
        zs=np.einsum("i,ijk->jk",bernstein(t,n),controls)
        zss=np.einsum("i,ijk->jk",bernstein(t,n-1),n/L*np.diff(controls,axis=0))
        er=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=1)
        et=np.stack((-np.sin(theta),np.cos(theta),np.zeros_like(theta)),axis=1)
        ez=np.asarray([0.,0.,1.])
        Y=R[:,None]*er+z[0,:,None]*ez
        Ys=Rs[:,None]*er+zs[0,:,None]*ez
        Yt=Rt[:,None]*er+R[:,None]*et+z[1,:,None]*ez
        Yss=Rss[:,None]*er+zss[0,:,None]*ez
        Yst=Rst[:,None]*er+Rs[:,None]*et+zs[1,:,None]*ez
        Ytt=(Rtt-R)[:,None]*er+2*Rt[:,None]*et+z[2,:,None]*ez
        ts,tu,tss,tsu,tuu=clock[1,0],clock[0,1],clock[2,0],clock[1,1],clock[0,2]
        out=dict(X=Y,Xs=Ys+Yt*ts[:,None],Xu=Yt*tu[:,None],
            Xss=Yss+2*Yst*ts[:,None]+Ytt*ts[:,None]**2+Yt*tss[:,None],
            Xsu=Yst*tu[:,None]+Ytt*(ts*tu)[:,None]+Yt*tsu[:,None],
            Xuu=Ytt*tu[:,None]**2+Yt*tuu[:,None])
        clock_controls=np.stack((left_clock["phi"][1],
            left_clock["phi"][1]+L*left_clock["phis"][1]/5,
            left_clock["phi"][1]+2*L*left_clock["phis"][1]/5+L*L*left_clock["phiss"][1]/20,
            right_clock["phi"][1]-2*L*right_clock["phis"][1]/5+L*L*right_clock["phiss"][1]/20,
            right_clock["phi"][1]-L*right_clock["phis"][1]/5,right_clock["phi"][1]))
        out.update(segment="new_polar_monotone_height_connector",
            minimumClockControl=float(np.min(clock_controls)),
            minimumHeightControl=float(np.min(controls[:,0])),
            minimumInteriorHeightControl=float(np.min(inner[0])),
            minimumRho=float(np.min(R)),minimumThetaU=float(np.min(tu)),
            minimumFixedThetaZs=float(np.min(zs[0])),
            maximumInverseResidual=max(er0,er1),
            polarCrossSquared=tu**2*(R**2*zs[0]**2+(zs[0]*Rt-Rs*z[1])**2+R**2*Rs**2))
        return out
    def jet(self,s,u):
        if self.b<=s<=self.S:return self.connector(s,u)
        return self.master.normalized(float(s),np.asarray(u,float),1024)


def comparison(a,b):
    return {key:float(np.max(np.linalg.norm(a[key]-b[key],axis=1)))
        for key in ("X","Xs","Xu","Xss","Xsu","Xuu")}


def check(source):
    u=np.asarray([.173,.947,1.737,2.197,3.641,5.897])
    ports=[]
    for side,s in enumerate((source.b,source.S)):
        analytic=source.connector(s,u)
        original=source.warm.packet_from_port(source.providers[side](u))
        ports.append(comparison(analytic,original))
    s=source.b+.413*source.L
    center=source.connector(s,u)
    errors=[]
    for h in (1e-4,3e-5,1e-5):
        sm=source.connector(s-h,u);sp=source.connector(s+h,u)
        um=source.connector(s,u-h);up=source.connector(s,u+h)
        finite=dict(Xs=(sp["X"]-sm["X"])/(2*h),Xu=(up["X"]-um["X"])/(2*h),
            Xss=(sp["Xs"]-sm["Xs"])/(2*h),Xsu=(up["Xs"]-um["Xs"])/(2*h),
            Xuu=(up["Xu"]-um["Xu"])/(2*h))
        errors.append(dict(h=h,maximumDerivativeDifference={key:float(
            np.max(np.linalg.norm(finite[key]-center[key],axis=1))) for key in finite}))
    geometric=np.sum(np.cross(center["Xs"],center["Xu"])**2,axis=1)
    return dict(fullTwoJetEndpointDifferences=ports,finiteDifferenceChecks=errors,
        polarCrossSquaredIdentityMaxError=float(np.max(abs(geometric-center["polarCrossSquared"]))),
        endpointFunctionsNotFourierProjected=True,
        allMetricsAndCurvaturesStillRequireTheirOwnFullFieldEvaluation=True)


def geometry_statistics(jet,centralA):
    X,S,U,SS,SU,UU=(jet[key] for key in ("X","Xs","Xu","Xss","Xsu","Xuu"))
    normal=np.cross(S,U);det=np.sum(normal**2,axis=1);area=np.sqrt(det)
    unit=normal/area[:,None]
    E=np.sum(S*S,axis=1);F=np.sum(S*U,axis=1);G=np.sum(U*U,axis=1)
    L=np.sum(SS*unit,axis=1);M=np.sum(SU*unit,axis=1);N=np.sum(UU*unit,axis=1)
    trace=(G*L-2*F*M+E*N)/det;gauss=(L*N-M*M)/det
    kappa=abs(trace)/2+np.sqrt(np.maximum(0,trace**2/4-gauss))
    witness=np.asarray([0.,centralA,0.])
    held=np.minimum(np.linalg.norm(X-witness,axis=1),np.linalg.norm(X+witness,axis=1))
    stats=dict(minAreaElement=float(np.min(area)),maxOwnCurvature=float(np.max(kappa)),
        maximumRadius=float(np.max(np.linalg.norm(X,axis=1))),
        maximumAbsoluteY=float(np.max(abs(X[:,1]))),minimumHeldDistance=float(np.min(held)),
        minimumZ=float(np.min(X[:,2])),maximumZ=float(np.max(X[:,2])),
        minimumMeridionalSpeed=float(np.min(np.sqrt(E))),maximumMeridionalSpeed=float(np.max(np.sqrt(E))))
    if "f" in jet:
        f=jet["f"];e=E-1;ff=F/f;g=G/(f*f)-1
        metric=abs(e+g)/2+np.sqrt(((e-g)/2)**2+ff*ff)
        stats.update(maxRelativeMetric=float(np.max(metric)),maxAbsEError=float(np.max(abs(e))),
            maxAbsNormalizedF=float(np.max(abs(ff))),maxAbsGError=float(np.max(abs(g))),
            minNormalizedGramDeterminant=float(np.min(det/(f*f))),
            minAreaRatio=float(np.min(area/f)))
    return stats


def main():
    ap=argparse.ArgumentParser();ap.add_argument("mode",choices=("check","geometry"))
    ap.add_argument("--scripts",type=Path,required=True);ap.add_argument("--ramp-master",type=Path,required=True)
    ap.add_argument("--coast-master",type=Path,required=True);ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--angles",type=int,default=128);ap.add_argument("--radials",type=int,default=33)
    args=ap.parse_args()
    if args.output.exists():raise FileExistsError("Fresh own-field report required")
    start=time.monotonic()
    source=NonfoldPolarConnector(args.scripts,args.ramp_master,args.coast_master)
    report=dict(schema="6a65-analytic-polar-monotone-height-full-six-jets-v1",mode=args.mode,
        sourceIdentities=source.identities,
        parameters=dict(b=source.b,S=source.S,cuff=source.cuff,L=source.L,
            centralA=source.master.A,centralB=source.master.B,
            amplitude=source.master.amplitude,Z=source.master.Z,velocityDegree=source.degree),
        continuousAngularPositivityCertified=False,continuousReachCertified=False,
        exactIsometryClaimed=False,originalFrozenTargetMetricNotChanged=True,
        actualResearchAcceptedSteps=0,checks=check(source))
    if args.mode=="geometry":
        u=2*np.pi*np.arange(args.angles)/args.angles;rows=[]
        for j,s in enumerate(np.linspace(source.b,source.S,args.radials)):
            jets=source.connector(float(s),u);stats=geometry_statistics(jets,source.master.A)
            rows.append(dict(s=float(s),geometry=stats,**{key:jets[key] for key in (
                "minimumClockControl","minimumHeightControl","minimumInteriorHeightControl",
                "minimumRho","minimumThetaU","minimumFixedThetaZs","maximumInverseResidual")}))
            if j%4==0:print(json.dumps(dict(radial=j,total=args.radials,s=float(s),**stats)),flush=True)
        report["rows"]=rows
        report["extrema"]={key:(min if key.startswith("min") else max)(r["geometry"][key] for r in rows)
            for key in rows[0]["geometry"]}
        report["originalFrozenMetricBaselineNotComputed"]=True
    report["seconds"]=time.monotonic()-start
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({key:value for key,value in report.items() if key!="rows"},allow_nan=False),flush=True)


if __name__=="__main__":main()
