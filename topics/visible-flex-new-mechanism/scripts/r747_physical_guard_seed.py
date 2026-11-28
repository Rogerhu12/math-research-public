"""R747 physical rotation seed for the full changed R742 guard, in native material labels."""
import hashlib
from pathlib import Path
import numpy as np
import r742_changed_sleeves as source

weak = source.weak
PHYSICAL_FILES = ("r747_physical_guard_seed.py","r747_guard_disk_solver.py")


class R747Frame(source.R742Frame):
    def __init__(self,build,phase,r,s,degree):
        super().__init__(build,phase,r,s,degree)
        if phase==0:
            return
        _,_,xr,_,_,_,ell=build.profile.read(self.r)
        endpoint=source.CUTOFF+source.WIDTH
        _,kind,v=build.ring.label(self.s)
        main=(kind==0)|(kind==2)
        av=abs(v)
        active=np.zeros_like(main)
        for c in (.206,.847):
            # The target curvature differs from the source strictly inside this
            # interval. At either end rho=1 on a true open neighborhood.
            active |= (av>c-.0002)&(av<c+.1002)
        mask=main&active&(ell>weak.physical.H)&(ell<=endpoint)
        if not np.any(mask):
            return
        s=self.s[mask]
        d=ell[mask]
        target=build.target(phase)
        _,_,_,k0,k0s=build.ring.jets(s)
        _,T,N,k,ks=target.jets(s)
        if np.any(k*k0<=0):
            raise ArithmeticError("R747 target curvature changes sign on the true constant-source band")
        per=target.length
        rho=k0/k
        rho_s=per*(k0s-rho*ks)/k
        f,fs,_=source.support(build.ring,s)
        _,ap,app=source.depth(d)
        m=f*ap
        m_r=xr[mask]*f*app
        m_s=per*fs*ap
        loss=(1-rho)*(1+rho)
        C=np.sqrt(1+loss*m*m)
        angle=np.arctan2(-m*loss*(1+m*m)/(C+rho),C+rho*m*m)
        da_dm=-loss/(C*(C+rho))
        da_drho=m/C
        h=weak.physical.H
        g,gd,_=source.step((d-h)/h)
        ar=g*da_dm*m_r+gd*xr[mask]*angle/h
        ass=g*(da_dm*m_s+da_drho*rho_s)
        angle=g*angle

        basis=np.zeros((len(s),3,3))
        basis[:,0,0]=1.
        basis[:,1:,1],basis[:,1:,2]=T,N
        bs=np.zeros_like(basis)
        bs[:,1:,1]=(k*per)[:,None]*N
        bs[:,1:,2]=-(k*per)[:,None]*T
        local,local_derivative=weak.fields.rotation(angle,1)
        bt=np.swapaxes(basis,-1,-2)
        K=basis@local@bt
        Ka=basis@local_derivative@bt
        Kr=ar[:,None,None]*Ka
        Ks=bs@local@bt+basis@local@np.swapaxes(bs,-1,-2)+ass[:,None,None]*Ka
        original=self.base[mask]
        self.br[mask]=Kr@original+K@self.br[mask]
        self.bs[mask]=Ks@original+K@self.bs[mask]
        self.base[mask]=K@original


class R747Build(source.R742Build):
    frame_type=R747Frame

    def __init__(self,baseline=weak.BASELINE,modes=8192,steps=12,order=48):
        super().__init__(baseline,modes,steps,order)
        self.identity.update(rotation_seed="R747 native exact constant-curvature guard coframe",
                      original_material="R742",guard_seed_onset=[weak.physical.H,2*weak.physical.H])
        self.integration_ell_breaks=np.unique(np.r_[self.integration_ell_breaks,
                                           weak.physical.H*np.array([1.,1.25,1.5,1.75,2.])])

    @property
    def seed_identity(self):
        info=super().seed_identity
        for name in PHYSICAL_FILES:
            info["physics_sha256"][name]=hashlib.sha256((Path(__file__).resolve().parent/name).read_bytes()).hexdigest()
        return info


def primitive_advance(d,reciprocal,rho,order):
    """Rationalized X_lambda-W-d at each constant-support label."""
    z,w=np.polynomial.legendre.leggauss(order)
    value=np.zeros_like(rho)
    loss=(1-rho)*(1+rho)
    lower=0.
    for upper in (source.DEPTH_JOIN,source.CUTOFF,source.CUTOFF+source.WIDTH):
        end=min(float(d),upper)
        if end>lower:
            q=lower+(end-lower)*(1+z)/2
            ap=source.depth(q)[1]
            m2=(reciprocal[:,None]*ap[None,:])**2
            term=loss[:,None]*m2
            value+=(end-lower)/2*((term/(1+np.sqrt(1+term)))@w)
        if d<=upper:
            break
        lower=upper
    return value


def homogeneous_probe(build,phase):
    """Independent exact beta, both native first derivatives, and actual Cartesian curl of the zero seed."""
    depths=np.array([3*weak.physical.H,.0004,source.DEPTH_JOIN,.02,.25,source.CUTOFF,
                     .512,.520,.525,.5299,source.CUTOFF+source.WIDTH])
    rs=build.radius_at(depths)
    v=np.concatenate([c+np.array([.0002,.05,.0998]) for c in (.206,.847)])
    v=np.r_[-v,v]
    ring=build.target(phase)
    ss=np.r_[(1+v)/ring.length,(3+ring.LU-v)/ring.length]
    r,s=np.meshgrid(rs,ss,indexing="ij")
    frame=R747Frame(build,phase,r,s,3)
    kr,br,bs,brs,brr,bss=frame.read(frame.q0,True)
    _,_,xr,_,xrr,_,ell=build.profile.read(rs)
    _,T,N,k,_=ring.jets(ss)
    _,_,_,k0,_=build.ring.jets(ss)
    f=source.support(build.ring,ss)[0]
    rho=k0/k
    per=ring.length
    p,ap,app=source.depth(ell)
    m=ap[:,None]*f
    md=app[:,None]*f
    loss=(1-rho)*(1+rho)
    C=np.sqrt(1+loss*m*m)
    A=1+p[:,None]*f*k0
    def vec(a,b):
        return np.concatenate((a[...,None],b),axis=-1)
    zero=np.zeros_like(m)
    pd=vec(C,-(rho*m)[...,None]*N)
    ps=vec(zero,A[...,None]*T)
    pdd=vec(loss*m*md/C,-(rho*md)[...,None]*N)
    pds=vec(zero,(k0*m)[...,None]*T)
    pss=vec(zero,(k*A)[...,None]*N)
    expected=(xr[:,None,None]*pd,per*ps,
              xr[:,None,None]**2*pdd+xrr[:,None,None]*pd,
              per*xr[:,None,None]*pds,per**2*pss)
    diffs=[np.linalg.norm(a-b,axis=-1) for a,b in zip((br,bs,brr,brs,bss),expected,strict=True)]
    raw=kr/frame.det.reshape(r.shape)[...,None]
    cpeak=float(np.max(np.linalg.norm(raw,axis=-1)))
    absolute=[float(a.max()) for a in diffs]
    scaled=[float(np.max(e/np.maximum(1.,np.linalg.norm(a,axis=-1)))) for e,a in zip(diffs,expected,strict=True)]
    if not np.isfinite(np.r_[scaled,cpeak]).all() or max(scaled+[cpeak])>2.e-8:
        raise ArithmeticError("R747 zero-seed closed constant guard disagrees with its physical differentiated field: "+str((scaled,cpeak)))
    inc=np.array([primitive_advance(x,f,rho,48) for x in ell])
    alt=np.array([primitive_advance(x,f,rho,32) for x in ell])
    gamma=ring.jets(ss)[0]
    px=weak.physical.W+ell[:,None]+inc
    yz=gamma-(p[:,None]*f*rho)[...,None]*N
    return dict(phase=phase,source="R742",input_seed="R747",degree_for_zero_probe=3,
         labels=ss,depths=ell,absolute_native_derivative_defects=absolute,
         relative_native_derivative_defects=scaled,derivative_names=["r","s","rr","rs","ss"],
         native_cartesian_curl=cpeak,quadrature_advance_48=inc,
         primitive_32_48_max=float(np.max(abs(inc-alt))),analytic_reference_P=vec(px,yz),
         scope="constant curvature open portions, zero controls and d>=2h; independent full-disk qualification remains required")
