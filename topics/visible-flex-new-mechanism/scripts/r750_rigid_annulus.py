"""R750 fixed physical core and the native three-axis field on the R743 annulus."""
import hashlib
from pathlib import Path

import numpy as np
import r743_early_material_disk as early

weak, space = early.weak, early.space
HERE = Path(__file__).resolve().parent
BLEND = (.065,.765)
FLAT_START = space.TOTAL-weak.physical.L*.0005
CLOSE_ELL = space.TOTAL-weak.physical.L*.00025
FREE_END = FLAT_START
FREE_WIDTH = .035


def turn(phase):
    return weak.fields.rotation(np.asarray(.5074*phase),0)[0]


def core_shift(build,phase):
    ring=build.target(phase)
    return np.r_[-.42*np.sqrt(phase),ring.origin-build.ring.origin]


def prescribed(build,phase,p):
    origin=np.r_[build.profile.endx,build.ring.origin]
    return origin+core_shift(build,phase)+(p-origin)@turn(phase).T


def skew(a):
    m=np.zeros(a.shape[:-1]+(3,3),dtype=a.dtype)
    m[...,0,1],m[...,0,2],m[...,1,0]=-a[...,2],a[...,1],a[...,2]
    m[...,1,2],m[...,2,0],m[...,2,1]=-a[...,0],-a[...,1],a[...,0]
    return m


def cross_part(a):
    return np.stack((a[...,2,1]-a[...,1,2],a[...,0,2]-a[...,2,0],a[...,1,0]-a[...,0,1]),axis=-1)


def relative_blend(base,br,bs,desired,g,gr):
    """Normalized quaternion interpolation, including both derivatives of the actual base."""
    trans=weak.fields.trans
    rel=trans(base)@desired
    a=.5*np.sqrt(1+np.trace(rel,axis1=-2,axis2=-1))
    if not np.isfinite(a).all() or a.min()<.68:
        raise ArithmeticError('R750 physical relative angle lost its proved positive scalar')
    v=cross_part(rel)/(4*a[:,None])
    raw=np.column_stack((1+g*(a-1),g[:,None]*v))
    norm=np.linalg.norm(raw,axis=-1)
    n=raw/norm[:,None]
    k=skew(n[:,1:]); k2=k@k
    rot=np.eye(3)+2*n[:,0,None,None]*k+2*k2
    def derive(db,dg):
        drel=trans(db)@desired
        da=np.trace(drel,axis1=-2,axis2=-1)/(8*a)
        dv=cross_part(drel)/(4*a[:,None])-v*(da/a)[:,None]
        q=np.column_stack((dg*(a-1)+g*da,dg[:,None]*v+g[:,None]*dv))
        dn=(q-n*np.sum(n*q,axis=-1)[:,None])/norm[:,None]
        dk=skew(dn[:,1:])
        dr=2*(dn[:,0,None,None]*k+n[:,0,None,None]*dk+dk@k+k@dk)
        return db@rot+base@dr
    return base@rot,derive(br,gr),derive(bs,np.zeros_like(gr))


# Both old R743 field families are retained on the free annulus. These radial
# knots additionally resolve the two formerly locked open intervals.
RELEASE_KNOTS = (
    np.array([weak.physical.H,3e-8,.00007,.001,.015,.035,early.EARLY+.003]),
    np.array([early.FORCED_END,.050149,.051,.053,.065,.085,.110]),
)


def flat_step(t):
    z=np.clip(t,0.,1.)
    return z**3*(10+z*(-15+6*z)),30*z*z*(1-z)**2


def extra_tags(degree):
    modes=(0,) if degree==3 else (0,1,-1)
    angular=[('mode',m) for m in modes]
    kinds=('wide',) if degree==3 else ('wide','nested')
    angular.extend(('edge',side,sign,c,kind) for side in (0,2) for sign in (-1,1)
                   for c in (.206,.847) for kind in kinds)
    local=(0,2) if degree==3 else (0,1,2,3)
    return [('release',j,i,m) for j in range(len(RELEASE_KNOTS)) for i in local for m in angular]


def tags(degree):
    return space.tagged_terms(degree)+extra_tags(degree)


def padded(q,old,new):
    source=dict(zip(tags(old),np.asarray(q).reshape(-1,3),strict=True))
    return np.asarray([source.get(tag,np.zeros(3)) for tag in tags(new)]).ravel()


def add_releases(frame,build,ell,er):
    _,kind,v=build.ring.label(frame.s)
    w,wv,_=weak.physical.native_w(v)
    vs=np.where(kind==0,build.ring.length,np.where(kind==2,-build.ring.length,0.))
    w=np.where(vs!=0,w,0.)
    ws=wv*vs
    shapes=space.edge_shapes(build,frame.s)
    angular={}
    for m in (0,1,-1,2,-2,3,-3):
        arg=2*np.pi*abs(m)*frame.s
        if m>=0:
            angular['mode',m]=(np.cos(arg),-2*np.pi*m*np.sin(arg))
        else:
            angular['mode',m]=(np.sin(arg),-2*np.pi*m*np.cos(arg))
    for k,val in shapes.items():
        angular[('edge',*k)]=val
    radial=[]
    for j,knots in enumerate(RELEASE_KNOTS):
        vals,ders=space.cubic(ell,knots)
        width=2e-8 if j==0 else .00008
        a,ad=flat_step((ell-knots[0])/width)
        b,bd=flat_step((knots[-1]-ell)/.008)
        eps=a*b
        deps=ad*b/width-a*bd/.008
        radial.append((vals*eps[:,None],er[:,None]*(ders*eps[:,None]+vals*deps[:,None])))
    extra=extra_tags(frame.degree)
    n=frame.B.shape[1]
    B,Br,Bs=(np.pad(x,((0,0),(0,len(extra)))) for x in (frame.B,frame.Br,frame.Bs))
    for col,(_,j,i,m) in enumerate(extra,n):
        b,bs=angular[m]
        if j==0:
            b,bs=b*w,bs*w+b*ws
        u,ur=radial[j]
        B[:,col]=u[:,i]*b
        Br[:,col]=ur[:,i]*b
        Bs[:,col]=u[:,i]*bs
    frame.B,frame.Br,frame.Bs=B,Br,Bs
    frame.ncols=3*B.shape[1]
    frame.q0=np.zeros(frame.ncols)


def meridian_seed(frame,build,phase,idx,ell):
    # The ratio equals one on all basal sectors with w=0. Unlike an invented
    # angular extrapolation of the constant-pulse ratio, this is their rigid
    # local solution and exactly closes the R752 early strip.
    s=frame.s[idx]
    _,kind,v=build.ring.label(s)
    w,wv,_=weak.physical.native_w(v)
    vs=np.where(kind==0,build.ring.length,np.where(kind==2,-build.ring.length,0.))
    w=np.where(vs!=0,w,0.)
    rho0=weak.B0/(weak.B0+phase*weak.INCREMENT/.0998)
    rho=1-(1-rho0)*w
    rho_s=-(1-rho0)*wv*vs
    ring=build.target(phase)
    _,t,n,k,_=ring.jets(s)
    e=np.zeros((len(s),3,3)); es=np.zeros_like(e)
    e[:,0,0]=1.;e[:,1:,1],e[:,1:,2]=t,n
    es[:,1:,1]=(k*ring.length)[:,None]*n
    es[:,1:,2]=-(k*ring.length)[:,None]*t
    et,est=weak.fields.trans(e),weak.fields.trans(es)
    th=np.empty_like(ell);kmer=np.empty_like(ell)
    ss=ell<=weak.FILLET_START
    if np.any(ss):
        th[ss],kmer[ss],_=build.profile.s.angle_jet(ell[ss]-early.EARLY)
    if np.any(~ss):
        y=(ell[~ss]-weak.FILLET_START)/weak.physical.L
        th[~ss]=np.pi/2*weak.physical.sym_step(y)
        kmer[~ss]=np.pi/2*(weak.physical.mollifier_cdf((y-.001)/.0005)
                   -weak.physical.mollifier_cdf((y-.999)/.0005))/(.998*weak.physical.L)
    _,er,_=space.ell_data(frame.r[idx])
    st,ct=np.sin(th),np.cos(th)
    cp=np.sqrt(1-(rho*st)**2)
    if not np.isfinite(cp).all() or np.min(cp)<=.05:
        raise ArithmeticError('R750 meridian seed was extended past its designated fillet cut')
    om=np.arcsin(rho*st)-th
    om=np.where(w==0,0.,om)
    dr=np.where(w==0,0.,(rho*ct/cp-1)*kmer*er)
    ds=rho_s*st/cp
    m,ma=weak.fields.rotation(om,1)
    u=e@m@et;ua=e@ma@et
    us=es@m@et+e@m@est+ds[:,None,None]*ua
    delta,delta_s=ring.angular_data(s)
    x,xa=weak.fields.rotation(delta,0)
    frame.base[idx],frame.br[idx],frame.bs[idx]=u@x,dr[:,None,None]*ua@x,us@x+u@(delta_s[:,None,None]*xa)


class R750Frame(early.R743Frame):
    def __init__(self,build,phase,r,s,degree):
        super().__init__(build,phase,r,s,degree)
        ell,er,_=space.ell_data(self.r)
        add_releases(self,build,ell,er)
        v=(FREE_END-ell)/FREE_WIDTH
        mask,md=flat_step(v)
        mask_r=-md*er/FREE_WIDTH
        self.Br=self.Br*mask[:,None]+self.B*mask_r[:,None]
        self.Bs=self.Bs*mask[:,None]
        self.B=self.B*mask[:,None]

        q=turn(phase)
        lo,hi=BLEND
        selected=np.flatnonzero((ell>early.EARLY)&(ell<hi))
        if phase and len(selected):
            meridian_seed(self,build,phase,selected,ell[selected])
        finish=ell>=hi
        self.base[finish]=q
        self.br[finish]=0.
        self.bs[finish]=0.
        mid=(ell>lo)&(ell<hi)
        if phase and np.any(mid):
            z=(ell[mid]-lo)/(hi-lo)
            h=early.gate(z)
            hr=early.gate(z,1)*er[mid]/(hi-lo)
            base,br,bs=relative_blend(self.base[mid],self.br[mid],self.bs[mid],q,h,hr)
            self.base[mid],self.br[mid],self.bs[mid]=base,br,bs


class R750Build(early.R743Build):
    frame_type=R750Frame
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.identity.update(problem='R750 hard rigid disk and two-physical-edge annulus',
            tip_angle=.5074,tip_translation='-.42*sqrt(lambda)',
            exact_inner_flat_start_ell=FLAT_START,closure_anchor_ell=CLOSE_ELL,
            physical_free_taper=[FREE_END-FREE_WIDTH,FREE_END],initial_frame_fillet_and_S_blend=list(BLEND))
        knots=np.array([0.,.002,.004,.5,.996,.998,1.])
        self.integration_ell_breaks=np.unique(np.r_[self.integration_ell_breaks,
            BLEND[0]+(BLEND[1]-BLEND[0])*knots,FREE_END-FREE_WIDTH*knots,
            FLAT_START,CLOSE_ELL,*RELEASE_KNOTS,weak.physical.H+2e-8,
            early.FORCED_END+.00008,RELEASE_KNOTS[0][-1]-.008,RELEASE_KNOTS[1][-1]-.008])

    def nodes(self,level,purpose):
        r,s=super().nodes(level,purpose)
        offset={'train':.5,'validation':.319,'qualification':.173}[purpose]
        knots=np.array([0.,.002,.004,.5,.996,.998,1.])
        x=np.sort(np.r_[knots,knots[:-1]+offset*np.diff(knots)])
        ell=np.r_[BLEND[0]+(BLEND[1]-BLEND[0])*x,FREE_END-FREE_WIDTH*x,
                  FLAT_START,CLOSE_ELL,*RELEASE_KNOTS,weak.physical.H+2e-8,
                  early.FORCED_END+.00008,RELEASE_KNOTS[0][-1]-.008,RELEASE_KNOTS[1][-1]-.008]
        return np.unique(np.r_[r,self.radius_at(ell)]),s

    @property
    def seed_identity(self):
        info=super().seed_identity
        for name in ('r750_rigid_annulus.py','r750_relative_boundary.py','r750_annulus_solver.py'):
            info['physics_sha256'][name]=hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        return info


def center_from_source(original,build,phase,q,degree,mean):
    zeros=np.zeros(3*(degree+1)*(degree+2)//2)
    _,source=original(build,0.,zeros,degree,np.zeros(3))
    if not np.allclose(mean,core_shift(build,phase),rtol=0,atol=1.e-14):
        raise ValueError('R750 reconstructed centre must be the prescribed material translation')
    qt=turn(phase).T
    return (prescribed(build,phase,source[0]),*(v@qt for v in source[1:])),source



def release_probe(build,phase):
    points=np.array([.00005,.05014]);sv=np.array([.2061,.84625])
    ss=(1+sv)/build.ring.length
    r=build.radius_at(points)
    frame=R750Frame(build,phase,r,ss,3)
    old=len(space.tagged_terms(3))
    active=np.max(abs(frame.B[:,old:]),axis=1)
    if not np.isfinite(active).all() or np.min(active)<=0:
        raise ArithmeticError('both actual R752 witness coordinates require three nonzero rotation columns')
    curl=frame.curl(frame.q0)
    _,er,_=space.ell_data(r)
    native=curl*frame.det[:,None]/(er[:,None]*build.ring.length)
    if not np.isfinite(native).all() or np.linalg.norm(native[1])>1.e-10:
        raise ArithmeticError('R750 zero seed must rigidly transport the whole early basal S witness')
    return dict(phase=phase,ell=points,s=ss,material_v=sv,release_value_maxima=active,
                zero_seed_signed_ell_sigma_curl=native,
                original_scalar_columns=old,appended_scalar_columns=frame.B.shape[1]-old)
