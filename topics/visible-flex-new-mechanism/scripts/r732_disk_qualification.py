"""Reconstruct the actual R732 position. Compute finite geometry, preserve unresolved continuum gates."""
from pathlib import Path
import hashlib
import os
import numpy as np
from scipy.spatial import ConvexHull,cKDTree,distance
from r688_actual_r664_window_collars import require_public,quadrature
from r732_closed_ring import Ring
from r732_compensated_pulses import H,gate
from r732_physical_disk import A,L,W,R0,EPS,ANGULAR_KNOTS,col,dot
from r732_disk_fields import Frame,rotation,apply,collar_jets


def tail_weight(r):
    t=(r-.15)/.52
    return 1-gate(t),-gate(t,1)/.52,-gate(t,2)/.52**2


def product_grid(frame_builder,rs,ss):
    r,s=np.meshgrid(rs,ss,indexing='ij')
    return frame_builder(r,s)


def true_breaks(build,radii):
    ell=np.r_[H*np.array([.5,1,1.002,1.5,1.998,2,3,4]),.025*np.array([.002,.004,.5,.996,.998])+H,
              A,A+.01,A+L*np.asarray(ANGULAR_KNOTS)]
    # A distinct source may insert real meridian sections with their own physical join loci.
    turn=build.identity.get('fillet_start_ell',A)+L*np.array([.002,.006,.994,.998])
    add=build.radius_at(np.r_[ell,turn,getattr(build,'integration_ell_breaks',[])])
    return np.unique(np.r_[0.,R0*np.array([.25,.251,.50,.749,.75,1.]),.15,.16,.67,.68,radii,add,1.])


def integrate(build,phase,q,degree,radii,ss,order):
    """Integrate only the change from the actual source differential; no replay of the source as quadrature."""
    cuts=true_breaks(build,radii)
    at=np.searchsorted(cuts,radii)
    x,w=quadrature(order)
    pieces=np.empty((len(cuts)-1,len(ss),2,3))
    for i in range(0,len(pieces),3):
        lo=cuts[i:i+3];hi=cuts[i+1:i+4];n=len(hi);lo=lo[:n];half=(hi-lo)/2
        radial=(lo[:,None]+half[:,None]*(1+x)).ravel()
        def increment(r,s):
            f=Frame(build,phase,r,s,degree)
            _,br,_,brs,_,_=f.read(q,True)
            return np.stack((br-f.j0[1].reshape(br.shape),brs-f.j0[4].reshape(br.shape)),axis=-2)
        data=product_grid(increment,radial,ss).reshape(n,order,len(ss),2,3)
        pieces[i:i+n]=half[:,None,None,None]*np.einsum('k,ikabc->iabc',w,data)
    tails=np.concatenate((np.cumsum(pieces[::-1],axis=0)[::-1],np.zeros((1,len(ss),2,3))),axis=0)
    b,bs,_=build.boundary_jets(phase,ss);a,as_,_=build.boundary_jets(0.,ss)
    fixed=np.stack((b-a,bs-as_),axis=-2)
    return fixed[None]-tails[at],fixed-tails[0]


def reconstructed(build,phase,q,degree,radii,ss,order,mean=None,need_all=True):
    delta,b=integrate(build,phase,q,degree,radii,ss,order)
    if mean is None:
        mark=np.flatnonzero(np.mod(ss,1.)==0.)
        if not len(mark):raise ValueError('R732 centre requires the original s=0 anchor')
        mean=b[mark[0],0]
    w,wp,wpp=tail_weight(radii)
    R,S=np.meshgrid(radii,ss,indexing='ij');f=Frame(build,phase,R,S,degree)
    kr,br,bt,brs,brr,bss=f.read(q,True)
    j=tuple(a.reshape(R.shape+(3,)) for a in f.j0)
    shift=b[:,0]-mean
    P=j[0]+delta[:,:,0]-w[:,None,None]*shift
    Pr=br-wp[:,None,None]*shift
    Ps=j[2]+delta[:,:,1]-w[:,None,None]*b[None,:,1]
    if not need_all:return Ps-j[2]
    Prr=brr-wpp[:,None,None]*shift
    Prs=brs-wp[:,None,None]*b[None,:,1]
    return P,Pr,Ps,Prr,Prs,mean,j,kr/col(f.det.reshape(R.shape)),b


def center_jets(build,phase,q,degree,mean):
    # Core Cartesian material variables (r cos(phi),r sin(phi)); base rotation is I there.
    from numpy.polynomial.chebyshev import chebval,chebder
    t=np.array([chebval(0,b) for b in np.eye(degree+1)])
    dt=np.array([chebval(0,chebder(b)) for b in np.eye(degree+1)])
    indices=[(i,j) for i in range(degree+1) for j in range(degree+1-i)]
    coef=np.asarray(q).reshape(-1,3)
    a=np.array([t[i]*t[j] for i,j in indices])@coef
    ax=np.array([dt[i]*t[j] for i,j in indices])@coef
    ay=np.array([t[i]*dt[j] for i,j in indices])@coef
    M=np.eye(3);X=np.zeros((3,3));Y=X.copy()
    for i in range(3):
        V,D=rotation(np.asarray(a[i]),i);U=M@D
        X=X@V+ax[i]*U;Y=Y@V+ay[i]*U;M=M@V
    p0=np.r_[build.profile.endx,build.ring.origin]
    e=np.array([0.,EPS/R0,0.]);v=np.array([0.,0.,EPS/R0])
    zero=np.zeros(3)
    new=tuple(p[None] for p in (p0+mean,M@e,M@v,X@e,.5*(X@v+Y@e),Y@v))
    old=tuple(p[None] for p in (p0,e,v,zero,zero,zero))
    return new,old


def geometry(j,j0):
    _,a,b,aa,ab,bb=j
    n=np.cross(a,b);area=np.linalg.norm(n,axis=-1)
    if not np.all(area>1.e-14):raise ArithmeticError('actual reconstructed immersion lost a physical tangent')
    n=n/col(area)
    def gram(u,v):
        return np.stack((dot(u,u),dot(u,v),dot(u,v),dot(v,v)),axis=-1).reshape(u.shape[:-1]+(2,2))
    g=gram(a,b);g0=gram(j0[1],j0[2]);C=np.linalg.inv(np.linalg.cholesky(g0))
    ev=np.linalg.eigvalsh(C@g@np.swapaxes(C,-1,-2))
    II=np.stack([dot(n,u) for u in (aa,ab,ab,bb)],axis=-1).reshape(g.shape)
    inv=np.linalg.inv(np.linalg.cholesky(g))
    k=np.linalg.eigvalsh(inv@II@np.swapaxes(inv,-1,-2))
    return n,g0,np.max(abs(ev-1),axis=-1),k


def disk_lift(build,phase,q,degree,r,ss,order,fd):
    P,Pr,Ps,Prr,Prs,mean,j0,K,b=reconstructed(build,phase,q,degree,r,ss,order)
    lo=reconstructed(build,phase,q,degree,r,ss-fd,order,mean,False)
    hi=reconstructed(build,phase,q,degree,r,ss+fd,order,mean,False)
    Pss=j0[5]+(hi-lo)/(2*fd)
    j=P,Pr,Ps,Prr,Prs,Pss
    n,g0,metric,k=geometry(j,j0)
    cj,c0=center_jets(build,phase,q,degree,mean)
    cn,cg,ce,ck=geometry(cj,c0)
    return dict(P=P,N=n,jets=j,g0=g0,metric=metric,curvature=k,curl=K,centre=cj[0],centre_n=cn,
                centre_metric=ce,centre_curvature=ck,centre_g0=cg,centre_jets=cj,source_jets=j0,source_center=c0[0],
                centre_drift=b[:,0]-mean,boundary_derivative_drift=b[:,1])


def point_cloud(build,phase,one,s):
    ring=build.target(phase)
    right=np.concatenate((one['P'].reshape(-1,3),one['centre']))
    nr=np.concatenate((one['N'].reshape(-1,3),one['centre_n']))
    sign=np.array([-1.,1.,1.]);left=right*sign;nl=nr*sign
    # The cap parametrization has inward or outward orientation; the tested inequality uses both signs.
    p,T,N,k,_=ring.jets(s)
    xs=np.linspace(-W,W,17)[1:-1]
    cyl=np.column_stack((np.repeat(xs,len(s)),np.tile(p,(len(xs),1))))
    nc=np.tile(np.column_stack((np.zeros_like(k),N)),(len(xs),1))
    return np.r_[right,left,cyl],np.r_[nr,nl,nc]


def chords(P,N,tau):
    tree=cKDTree(P)
    worst=0.;close=0;bad=0;seen=0;witness=None
    for i in range(0,len(P),24):
        block=tree.query_ball_point(P[i:i+24],2*tau+1.e-10)
        for k,js in enumerate(block):
            a=i+k;j=np.asarray(js,dtype=int);j=j[j>a]
            if not len(j):continue
            d=P[j]-P[a];sq=dot(d,d)
            w=2*tau*np.maximum(abs(d@N[a]),abs(dot(d,N[j])))-sq
            seen+=len(j);close+=int(np.sum(sq<1.e-12))
            bad+=int(np.sum(w>5.e-12))
            z=np.argmax(w)
            if w[z]>worst:worst=float(w[z]);witness=[a,int(j[z])]
    return dict(radius=tau,indexed_points=len(P),near_pairs=seen,tiny_pairs_roundoff_sensitive=close,
                excess_above_5e_12=bad,max_squared_excess=worst,witness=witness,
                continuum_pairs_and_positive_fill_distance='open')


def diameter(P):
    ids=ConvexHull(P).vertices
    pts=P[ids];best=0.
    for i in range(0,len(pts),64):
        best=max(best,float(np.max(distance.cdist(pts[i:i+64],pts,'sqeuclidean'))))
    return np.sqrt(best)


def qualify(build,phase,q,degree,level=1,outdir=None):
    """One full physical phase; does not turn finite labels or finite phase spacing into a certificate."""
    require_public()
    r,s=build.nodes(level,'qualification')
    order=max(6,4+2*int(level)); fd=2.4e-7/(build.ring.length*level)
    val=disk_lift(build,phase,q,degree,r,s,order,fd)
    # Independent quadrature and angular derivative on sparse labels of this *same* geometry and controls.
    rs=r[::3];ss=s[::4]
    ref=disk_lift(build,phase,q,degree,rs,ss,order+4,fd/2)
    # Both computations use the same original s=0 anchor and physical reconstruction.
    diffs=[float(np.max(np.linalg.norm(a[::3,::4]-b,axis=-1))) for a,b in zip(val['jets'],ref['jets'])]
    pt,n=point_cloud(build,phase,val,s)
    src=dict(P=val['source_jets'][0],N=val['N'],centre=val['source_center'],centre_n=val['centre_n'])
    sourcepts,_=point_cloud(build,0.,src,s)
    maxerr=float(max(np.max(val['metric']),np.max(val['centre_metric']),np.max(ref['metric'])))
    maxk=float(max(np.max(abs(val['curvature'])),np.max(abs(val['centre_curvature'])),np.max(abs(ref['curvature']))))
    qsha=hashlib.sha256(np.asarray(q,dtype='<f8').tobytes()).hexdigest()
    out=dict(phase=float(phase),degree=int(degree),q_sha256=qsha,disk_metric_max=maxerr,
             disk_curvature_max=maxk,disk_cartesian_curl_max=float(np.max(np.linalg.norm(val['curl'],axis=-1))),
             second_scale_jet_max_differences=diffs,
             physical_centre_collapsed_and_jets_evaluated=True,
             max_source_to_phase_union_diameter_sample=float(diameter(np.r_[pt,sourcepts])),
             zmax=float(np.max(pt[:,2])),zmin=float(np.min(pt[:,2])),xmax=float(np.max(abs(pt[:,0]))),
             source_zmax_sample=float(np.max(sourcepts[:,2])),source_zmax_bound=.349,
             given_far_seat_z=float(build.target(phase).line.position(np.asarray(1.))[1]+.20),
             all_sampled_normal_pairs=chords(pt,n,1/10.4),
             all_material_and_all_time='open',full_shell_qualification=False)
    # This compares actual compensated collar frames on the original Cauchy data. Archive h^4Q coefficients,
    # not an order-one position subtraction divided by h^2.
    out['true_compensated_pulses']=[dict(c=p.c,modes=p.modes,radial_steps=p.steps,rhs_work=p.count,
                                            min_signed_n=p.min_n,max_unscaled_Q=p.highest_correction)
                                      for p in build.pulses(phase)]
    _,_,xr,_,xrr,_,ell=build.profile.read(r)
    narrow=np.flatnonzero(ell<=H)
    mismatch=np.zeros(6)
    for i in narrow:
        point,xx,sig,xxx,xsig,ssig=collar_jets(build,phase,np.full_like(s,ell[i]),s,True)
        per=build.ring.length
        expected=(point,xr[i]*xx,per*sig,xr[i]**2*xxx+xrr[i]*xx,xr[i]*per*xsig,per**2*ssig)
        for j,(actual,want) in enumerate(zip(val['jets'],expected)):
            mismatch[j]=max(mismatch[j],np.max(np.linalg.norm(actual[i]-want,axis=-1)))
    out['prescribed_open_band_jet_errors']=mismatch.tolist()
    out['checks_distinct']=dict(physical_curvature='each refined actual Hessian',
        normal_pairs='both ordered normals on both full disks and cylinder',
        original_cauchy_rows='actual compensated thin collar and two U arcs',
        centre='regular Cartesian material point')
    root=Path(outdir or os.environ.get('R732_ARTIFACT_DIR','r732-physical-artifacts'))
    root.mkdir(parents=True,exist_ok=True)
    name=f'phase-{float(phase):.12g}-deg{degree}-L{level}-{qsha[:12]}.npz'
    path=root/name
    np.savez_compressed(path,phase=phase,q=q,degree=degree,r=r,s=s,source_g=val['g0'],
                        source_jets=np.array(val['source_jets']),physical_jets=np.array(val['jets']),
                        physical_center_jets=np.array(val['centre_jets']),source_center_g=val['centre_g0'],
                        metric=val['metric'],principal_curvatures=val['curvature'],cartesian_curl=val['curl'],
                        centre_drift=val['centre_drift'],boundary_derivative_drift=val['boundary_derivative_drift'])
    out['physical_archive']=str(path);out['archive_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    return out

