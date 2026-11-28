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
        av=abs(v)
        support=np.zeros_like(av,dtype=bool)
        for c in (.205,.846):
            support |= (av>=c-source.ANGULAR_RAMP)&(av<=c+.102+source.ANGULAR_RAMP)
        mask=((kind==0)|(kind==2))&support&(ell>weak.physical.H)&(ell<=endpoint)
        if not np.any(mask):
            return
        s,d=self.s[mask],ell[mask]
        ring=build.target(phase)
        _,T,N,k,ks=ring.jets(s)
        f,fs,fss=source.support(build.ring,s)
        p,pd,pdd=source.depth(d)
        h=weak.physical.H
        g,gd,gdd=source.step((d-h)/h)
        # One constant continuation per physical pulse. The true f vanishes with
        # all necessary angular jets before any U collar. No k_lambda' / k_lambda
        # spike is introduced at the native narrow angular slope.
        ratio=weak.B0/(weak.B0+phase*weak.INCREMENT/(.100*.998))
        amp=1+(ratio-1)*g
        ad=(ratio-1)*gd/h
        add=(ratio-1)*gdd/h**2
        u=amp*p
        ud=amp*pd+ad*p
        udd=amp*pdd+2*ad*pd+add*p
        ref=pd/weak.B0
        moved=ud/weak.B0
        C=np.sqrt(1+(ref-moved)*(ref+moved))
        Cd=(ref*pdd-moved*udd)/(weak.B0*C)
        b,bx,bs=u*f,ud*f,u*fs
        bxx,bxs,bss=udd*f,ud*fs,u*fss
        E=1+k*b
        zero=np.zeros_like(d)
        vec,col=source.vec,source.col
        # Both tangent vectors and their physical derivatives are taken from G.
        # The normal component of G_sigma on straight angular tapers is retained.
        want=(None,vec(C,-col(bx)*N),vec(zero,col(E)*T-col(bs)*N),
              vec(Cd,-col(bxx)*N),vec(zero,col(k*bx)*T-col(bxs)*N),
              vec(zero,col(ks*b+2*k*bs)*T+col(k*E-bss)*N))
        G,Gd,Gs=weak.fields.frames(want)
        F,Fd,Fs=weak.fields.frames(source.ring_jets(build.ring,d,s))
        trans=weak.fields.trans
        M=G@trans(F)
        Md=Gd@trans(F)+G@trans(Fd)
        Ms=Gs@trans(F)+G@trans(Fs)
        delta,ds=ring.angular_data(s)
        X,Xdelta=weak.fields.rotation(delta,0)
        Xt=trans(X)
        K=M@Xt
        Kr=xr[mask,None,None]*(Md@Xt)
        Ks=ring.length*(Ms@Xt)+M@trans(ds[:,None,None]*Xdelta)
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
    """Exact homogeneous comparison X_lambda-W-d, independent of the numerical collar blend."""
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
    # On the true narrow target shoulders, f still equals 1/k_* but k_lambda
    # genuinely varies. Its unscaled physical curl is (k0-rho*k_lambda)m*T.
    v=np.concatenate([c+np.array([.00006,.0001,.00014,.09986,.09990,.09994]) for c in (.206,.847)])
    v=np.r_[-v,v]
    shoulders=np.r_[(1+v)/ring.length,(3+ring.LU-v)/ring.length]
    R,S=np.meshgrid(rs,shoulders,indexing="ij")
    slope=R747Frame(build,phase,R,S,3)
    got=slope.curl(slope.q0)
    _,ts,_,kt,_=ring.jets(shoulders)
    kb=build.ring.jets(shoulders)[3]
    ff=source.support(build.ring,shoulders)[0]
    amp=weak.B0/(weak.B0+phase*weak.INCREMENT/(.100*.998))
    material=vec(np.zeros((len(rs),len(shoulders))),
             (ap[:,None]*ff*(kb-amp*kt))[...,None]*ts)
    predicted=xr[:,None,None]*per*material/slope.det.reshape(R.shape)[...,None]
    slope_diff=float(np.max(np.linalg.norm(got-predicted,axis=-1)))
    slope_mass=float(np.max(np.linalg.norm(material,axis=-1)))
    if not np.isfinite([slope_diff,slope_mass]).all() or slope_diff>2.e-8 or slope_mass>.000101:
        raise ArithmeticError("R747 changing native shoulders disagree with the analytic nonzero curl")

    return dict(phase=phase,source="R742",input_seed="R747",degree_for_zero_probe=3,
         labels=ss,depths=ell,absolute_native_derivative_defects=absolute,
         relative_native_derivative_defects=scaled,derivative_names=["r","s","rr","rs","ss"],
         native_cartesian_curl=cpeak,changing_shoulder_material_peak=slope_mass,
         changing_shoulder_cartesian_defect=slope_diff,changing_shoulder_labels=shoulders,
         quadrature_advance_48=inc,
         primitive_32_48_max=float(np.max(abs(inc-alt))),analytic_reference_P=vec(px,yz),
         scope="zero controls at d>=2h; homogeneous five jets and changing shoulder curl; full-disk qualification independent")
