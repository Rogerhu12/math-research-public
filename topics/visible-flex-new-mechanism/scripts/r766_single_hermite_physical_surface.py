"""Same continuous-in-phi, C2-in-r physical F and every derivative of that one representative."""
import numpy as np
from r703_material_geometry_observer import cones
from r738_negative_tail_and_macro_source import THETA
from r761_unrestricted_frame_and_solid import cap_fields, dot, smooth_join


def all_six(frame,sp,x):
    g=frame.read(sp,x);rr=frame.r;ph=frame.phi;r=rr[:,None,None];h=np.diff(rr)[:,None,None]
    matter=frame.original.mat;m=matter['m'][:,None,None];mr=matter['mr'][:,None,None]
    R=g['rotation'];Rr=g['rotation_slopes']
    V=[m*rot[...,0] for rot in R];A=[mr*rot[...,0]+m*sr[...,0] for rot,sr in zip(R,Rr)]
    inner=cap_fields(ph,THETA);outer=cap_fields(ph,0.);center=x[:3];raw=[]
    # This is the exact integral of the declared cubic Hermite velocity, componentwise.
    for k in range(3):
        segment=h*((V[k][:-1]+V[k][1:])/2+h*(A[k][:-1]-A[k][1:])/12)
        F=np.empty_like(V[k]);F[-1]=rr[-1]*outer[k];F[:-1]=F[-1]-np.cumsum(segment[::-1],axis=0)[::-1]
        raw.append(F)
    lam,lp,lpp=smooth_join(rr,.105,.175);boundary=[];patches=[]
    for at,cap,cc,chi,chip,chipp in ((0,inner,center,lam,lp,lpp),(-1,outer,np.zeros_like(center),1-lam,-lp,-lpp)):
        d=r-rr[at];p=[rr[at]*cap[k]+(cc if k==0 else 0)-raw[k][at] for k in range(3)]
        v=[cap[k]-V[k][at] for k in range(3)];w=[-a[at] for a in A]
        boundary.append((p,v,w));block=[]
        for k in range(3):
            z=p[k]+d*v[k]+d*d*w[k]/2;zp=v[k]+d*w[k]
            block.append((chi*z,chip*z+chi*zp,chipp*z+2*chip*zp+chi*w[k]))
        patches.append(block)
    def lift(k,n):return patches[0][k][n]+patches[1][k][n]
    zeta=raw[0]+lift(0,0);Fr=V[0]+lift(0,1);Fphi=raw[1]+lift(1,0)
    Frr=A[0]+lift(0,2);Frp=V[1]+lift(1,1);Fpp=raw[2]+lift(2,0)
    six=(zeta,Fr,Fphi/r,Frr,Frp/r,Fpp/r**2)
    P,T,N=[R[0][...,j] for j in range(3)];nphi=R[1][...,2];nr=Rr[0][...,2]
    curl=V[1]-T-r*Rr[0][...,1];curlp=V[2]-R[1][...,1]-r*Rr[1][...,1]
    scalar=dot(curl,N);scalar_phi=dot(curlp,N)+dot(curl,nphi)
    Fm=dot(Fr,Fr)/m[...,0]**2-1;Fq=dot(Fr,Fphi/r)/m[...,0];Fp=dot(Fphi/r,Fphi/r)-1
    peak=lambda v:float(np.max(abs(np.real(v))))
    rims=[]
    for i,cap,cc in ((0,inner,center),(-1,outer,np.zeros_like(center))):
        er,et,minus_er=cap;z=rr[i]
        ref=(cc+z*er,er,et,np.zeros_like(er),et/z,minus_er/z)
        rims.append([peak(t[i]-p) for t,p in zip(six,ref)])
    return dict(actual_six=six,actual_Gram=(Fm,Fq,Fp),complete_curl=curl,normal_scalar=scalar,
        normal_scalar_phi=scalar_phi,design_P=P,design_T=T,design_n=N,cap_six=rims,
        frame=g,inner_and_outer_unadjusted_six=boundary,developed_center=raw[0][0].mean(axis=0),
        diagnostics=dict(declared_Gauss_identity=peak(g['literal_Gauss']),physical_SO3_orthogonality=peak(np.swapaxes(R[0],-1,-2)@R[0]-np.eye(3)),
            determinant_error=peak(np.linalg.det(R[0])-1),complete_frame_angular_connection=[peak(x) for x in g['actual_Xphi_errors']],
            k_ell_GaussMap_jacobian_defect=peak(dot(N,np.cross(nr,nphi))+matter['mr'][:,None]/m[...,0]**2*-1),
            full_vector_curl=peak(np.linalg.norm(curl.real,axis=-1)),actual_C2_Hermite_velocity=True))


def midpoint(a,b,da,db,h):
    return (a+b)/2+h*(da-db)/8,1.5*(b-a)/h-(da+db)/4


def compared(first,second,coarse,fine):
    """A real independent two-half-step transfer and the between-node derivative defect of the full coarse frame."""
    r=first.r;h=np.diff(r)[:,None,None,None]
    if not np.array_equal(r,second.r[::2]):raise ValueError('Independent transfer must retain every actual coarse point.')
    g,gg=coarse['frame'],fine['frame'];Rv,Rs=g['rotation'],g['rotation_slopes'];Nr,Ns=gg['rotation'],gg['rotation_slopes']
    x,y=second.original.mat,gg; ir=slice(1,None,2)
    b=x['m'][ir,None]/second.r[ir,None];om=b*y['ell'][ir];av=y['a'][ir];zero=np.zeros_like(om)
    skew=np.stack((zero,zero,-av,zero,zero,-om,av,om,zero),axis=-1).reshape(av.shape+(3,3))
    def norms(it):return [float(np.max(abs(t))) for t in it]
    matrices=[];speeds=[];slope_gap=[]
    for V,D,Y,S in zip(Rv,Rs,Nr,Ns):
        mid,dm=midpoint(V[:-1],V[1:],D[:-1],D[1:],h)
        matrices.append(float(abs(mid-Y[ir]).max()));speeds.append(float(abs(dm-S[ir]).max()));slope_gap.append(dm)
    mid,_=midpoint(Rv[0][:-1],Rv[0][1:],Rs[0][:-1],Rs[0][1:],h)
    return dict(independent_native_S0_S1_S2=norms(q-t[::2] for q,t in zip(Rv,Nr)),
        independent_common_F_and_five=norms(q-t[::2] for q,t in zip(coarse['actual_six'],fine['actual_six'])),
        midpoint_frame_angular_jets_vs_halfstep=matrices,midpoint_physical_radial_jets_vs_halfstep=speeds,
        sampled_true_Hermite_frame_ODE_defect=float(abs(slope_gap[0]-mid@skew).max()),
        whole_radial_continuous_integrator_accuracy_bound=None)
