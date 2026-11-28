"""Material development from a genuine all-angle Gauss map. Both real caps and all three translations."""
import math
import numpy as np
from r758_material_jet_and_angles import J,cosine,sine,vecjet
from r748_single_height_development import smooth_join
from r703_material_geometry_observer import ActualPose,barrier,cones,relmetric
from r683_proper_phase_metric_transport_20261128 import shell,shell_ok


def dot(a,b):return np.sum(a*b,axis=-1)


def radial(a):
    return J.pack({(0,k):a.a.get((1,k),0.) for k in range(3)})


def components(v,der,shape):return vecjet(v,*der,shape)


def angular_primitive_frame(grid,phi,n,mu):
    """Independent northern frame; true material derivatives, no summing Fourier means or parity assumptions."""
    n0,n1,n2=n;one=1+n2
    if np.any(one.value.real<=0):raise FloatingPointError('Northern frame denominator not separated.')
    X=(1-n0*n0/one,-n0*n1/one,-n0)
    Y=(-n0*n1/one,1-n1*n1/one,-n1)
    A=(n1*radial(n0)-n0*radial(n1))/one
    shape=(len(grid.r),len(phi))
    coeff={}
    for k,b in enumerate((phi,np.ones_like(phi),np.zeros_like(phi))):
        ar=np.broadcast_to(A.jet(0,k),shape)
        coeff[0,k]=grid.primitive_from_outer(-ar,b)/(2 if k==2 else 1)
        coeff[1,k]=-ar/(2 if k==2 else 1)
    delta=J.pack(coeff);cs,sn=cosine(delta),sine(delta)
    P=tuple(cs*x+sn*y for x,y in zip(X,Y))
    T=tuple(-sn*x+cs*y for x,y in zip(X,Y))
    return P,T,delta


def cap_fields(phi,angle):
    co,si=np.cos(phi),np.sin(phi);c,s=np.cos(angle),np.sin(angle)
    er=np.stack((c*co,si,-s*co),axis=-1)
    et=np.stack((-c*si,co,s*si),axis=-1)
    return er,et,-er


def develop(grid,phi,material,native,center,theta,band=(.105,.175)):
    """Return actual joined F at physical materials and complete proposed connection/curl diagnostics."""
    phi=np.asarray(phi);center=np.asarray(center);r=grid.r[:,None,None]
    if center.shape!=(3,):raise ValueError('All three physical center components are required.')
    m=J(np.sqrt(material['E'])[:,None],(material['Ep']/(2*np.sqrt(material['E'])))[:,None])
    shape=(len(r),len(phi));n,P,T=(native[k] for k in ('n','P','T'));mu=1-1/m
    refP,refT,phase=angular_primitive_frame(grid,phi,n,mu)
    tri=lambda y,i,k:components(y,(i,k),shape)
    nn,nr,nphi=tri(n,0,0),tri(n,1,0),tri(n,0,1)
    p,t=tri(P,0,0),tri(T,0,0);tphi=tri(T,0,1)
    outer=cap_fields(phi,0.);inner=cap_fields(phi,theta)
    mP=tuple(m*v for v in P)
    # Angular jets of the SAME outer radial development. Actual material phi never moves in these integrals.
    raw=tuple(grid.primitive_from_outer(tri(mP,0,k),r[-1,0,0]*v) for k,v in enumerate(outer))
    displacement_integrands=[tri(mP,0,k) for k in range(3)]
    radial_integrands=[tri(mP,1,k) for k in range(3)]
    lam,lp,lpp=smooth_join(grid.r,*band)
    corrections=[];rim_errors=[];xyz=np.zeros_like(center)
    for idx,C,cap,weight,wprime,wpprime in ((0,center,inner,lam,lp,lpp),(-1,xyz,outer,1-lam,-lp,-lpp)):
        z=r-r[idx,0,0]
        v0=[r[idx,0,0]*v-raw[k][idx]+(C if k==0 else 0) for k,v in enumerate(cap)]
        v1=[v-displacement_integrands[k][idx] for k,v in enumerate(cap)]
        v2=[-a[idx] for a in radial_integrands]
        def patch(k):
            f=v0[k]+z*v1[k]+z*z*v2[k]/2
            fr=v1[k]+z*v2[k]
            return weight*f,wprime*f+weight*fr,wpprime*f+2*wprime*fr+weight*v2[k]
        corrections.append(tuple(patch(k) for k in range(3)))
        rim_errors.append((v0,v1,v2))
    def lift(k,i):return corrections[0][k][i]+corrections[1][k][i]
    F=raw[0]+lift(0,0);Fr=displacement_integrands[0]+lift(0,1);Fphi=raw[1]+lift(1,0)
    Frr=radial_integrands[0]+lift(0,2);Frphi=displacement_integrands[1]+lift(1,1);Fpp=raw[2]+lift(2,0)
    six=(F,Fr,Fphi/r,Frr,Frphi/r,Fpp/r**2)
    scalar=r[...,0]*dot(t,nr)-m.value*dot(p,nphi)
    scphi=r[...,0]*(dot(tphi,nr)+dot(t,tri(n,1,1)))-m.value*(dot(tri(P,0,1),nphi)+dot(p,tri(n,0,2)))
    true_curl=displacement_integrands[1]-t-r*tri(T,1,0)
    der_curl=displacement_integrands[2]-tphi-r*tri(T,1,1)
    D=raw[1]-r*t;Dp=raw[2]-r*tphi
    cone=grid.primitive_from_outer(scalar[...,None]*nn,np.zeros_like(nn[-1]))
    dcone=grid.primitive_from_outer(scphi[...,None]*nn+scalar[...,None]*nphi,np.zeros_like(nn[-1]))
    A=dot(Fr,Fr)/m.value**2-1;B=dot(Fr,Fphi/r)/m.value;C=dot(Fphi/r,Fphi/r)-1
    maxreal=lambda y:float(np.max(np.abs(y.real)))
    physical_rims=[]
    for idx,C0,cap in ((0,center,inner),(-1,xyz,outer)):
        er,et,epp=cap;rr=r[idx,0,0]
        known=(C0+rr*er,er,et,np.zeros_like(er),et/rr,epp/rr)
        physical_rims.append([maxreal(x[idx]-y) for x,y in zip(six,known)])
    return dict(actual_six=six,actual_Gram=(A,B,C),design_n=nn,design_P=p,design_T=t,
          normal_scalar=scalar,normal_scalar_phi=scphi,complete_curl=true_curl,
          tangential_curl=(dot(true_curl,p),dot(true_curl,t)),complete_curl_phi=der_curl,
          prescribed_center=center,radially_developed_center=raw[0][0].mean(axis=0),
          inner_and_outer_unadjusted_six=rim_errors,all_angle_inner_mismatch=tuple(rim_errors[0][0]),
          exact_rim_six_read=physical_rims,developed_outer_angular_defect=D,scalar_integral=cone,
          diagnostics=dict(Jacobian=maxreal(dot(nn,np.cross(nr,nphi))-mu.jet(1,0)),
            connection_r=maxreal(dot(t,tri(P,1,0))),connection_phi=maxreal(dot(t,tri(P,0,1))-(1-mu.value)),
            orthogonal=[maxreal(dot(a,b)-v) for a,b,v in ((nn,nn,1),(p,p,1),(t,t,1),(nn,p,0),(nn,t,0),(p,t,0))],
            right_handed=maxreal(np.cross(p,t)-nn),radial_frame_validation=[maxreal(tri(q,0,0)-v) for q,v in ((refP,p),(refT,t))],
            actual_cap_phase_radial_development=maxreal(phase.value[0]-phi),
            vector_curl_minus_normal=maxreal(true_curl-scalar[...,None]*nn),
            scalar_angular_integral_errors=[maxreal(D-cone),maxreal(Dp-dcone)],
            full_vector_angular_integral_errors=[maxreal(D-grid.primitive_from_outer(true_curl,np.zeros_like(nn[-1]))),
                maxreal(Dp-grid.primitive_from_outer(der_curl,np.zeros_like(nn[-1])))],
            raw_rim_angular_maxima=[[[maxreal(t) for t in group] for group in end] for end in rim_errors]),
          exact_continuous_global_solution=False)


def shell3(grid,phi,six,center,E,deep=None,theta=np.arcsin(.27)):
    """Evaluate the actual all-angle shell; all radial peg bounds use the full horizontal center norm."""
    from types import SimpleNamespace
    from r738_whole_material_macro_continuation_20261128 import mixed_envelopes
    vals,ten=cones(six,theta);a,b,d,det,L,M,K=ten
    mean=(d*L-2*b*M+a*K)/(2*det);gauss=(L*K-M*M)/det
    curv=abs(mean)+np.sqrt(np.maximum(0.,mean*mean-gauss));rel=relmetric(ten,np.sqrt(E)[:,None])
    ctr=six[0].mean(axis=1);ctr[0]=center;ctr[-1]=0
    xy=float(np.linalg.norm(center[:2]));profile=SimpleNamespace(r=grid.r,b=.22,theta=theta)
    pose=ActualPose(profile,ctr)
    info=shell(pose,None,dict(r=grid.r,q=np.zeros_like(grid.r)),dict(U=(six[0]-ctr[:,None,:])/grid.r[:,None,None]),
            dict(actual_center=[xy,center[2]],min_outer_normal=float(vals[4].min()),min_inner_normal=float(vals[5].min()),
                 max_abs_curvature=float(curv.max())))
    info['actual_center_xyz']=center.tolist();info['horizontal_center_radius_for_peg']=xy
    del info['actual_inner_center_xz']
    proxy=ctr.copy();proxy[0]=[xy,0.,center[2]]
    deep_ok=deep is not None and all(z['available'] for z in deep)
    mixed=mixed_envelopes(six,(proxy,),deep,info) if deep_ok else None
    i,j=np.unravel_index(rel.argmax(),rel.shape);k,l=np.unravel_index(curv.argmax(),curv.shape)
    margin=min(.0115-xy,.0426-abs(center[2]));violation=sum(max(0.,-v) for name,v in info.items()
          if (name.endswith('margin') or name.endswith('normal_min') or name.endswith('dominance')))
    violation+=max(0.,-margin)+max(0.,info['sampled_whole_D_upper_estimate']-1)
    if deep_ok:violation+=max(0.,-mixed['mixed_support_margin_estimate'])+max(0.,mixed['mixed_diameter_upper_estimate']-1)
    else:violation+=1
    return dict(shell=info,pose_margin=margin,deep_pass=deep_ok,mixed=mixed,eta=float(rel[i,j]),
          eta_at=[grid.r[i],phi[j]],curvature=float(curv[k,l]),curvature_at=[grid.r[k],phi[l]],
          violation=float(violation),shell_pass=bool(deep_ok and mixed['admissible'] and shell_ok(info) and margin>0))


def projected_geodesic_rows(S,center,nphi,ndirs,weight,theta=np.arcsin(.27)):
    """Necessary terminal tangent-cone bound at every named 3D direction and labelled meridian."""
    if nphi%2 or ndirs<8:raise ValueError('Both antipodal material generators and complete direction tests are required.')
    t=np.arange(nphi)*2*np.pi/nphi;Eo=cap_fields(t,0.)[0];Ei=cap_fields(t,theta)[0]
    beta=np.arange(ndirs)*2*np.pi/ndirs
    planar=np.stack((np.cos(beta),np.zeros_like(beta),np.sin(beta)),axis=1)
    z=1-2*(np.arange(ndirs)+.5)/ndirs;angle=np.arange(ndirs)*(np.pi*(3-np.sqrt(5.)))
    sphere=np.stack((np.sqrt(1-z*z)*np.cos(angle),np.sqrt(1-z*z)*np.sin(angle),z),axis=1)
    v=np.vstack((planar,sphere,-sphere,np.eye(3),-np.eye(3)))
    A=np.arccos(np.clip(Ei@v.T,-1.,1.));B=np.arccos(np.clip(Eo@v.T,-1.,1.));rho=.03
    if np.max(abs(A-B))*rho>=S.real:raise FloatingPointError('Real two-ended tangent cones do not intersect.')
    mid=(A+B-S/rho)/2;over=mid.real>0
    cap=np.where(over,rho*(np.sin(A)+np.sin(B)-2*np.sin(np.where(over,mid,0.))),S-rho*(A-np.sin(A)+B-np.sin(B)))
    gap=((.22*Eo-.075*Ei)-center)@v.T-cap
    return (weight*barrier((gap+.0002)/.145,.0005)/np.sqrt(gap.size)).ravel(),float(-gap.real.max())
