"""Actual two-anchor surface from the Gauss chart, full nonlocal actions, and paid-source projection."""
import numpy as np
from r726_closed_spinor_fourier import public
from r738_negative_tail_and_macro_source import bump,THETA
from r748_single_height_development import smooth_join
from r748_paid_material_height_projection import original_fixed_reference
from r758_material_jet_and_angles import vecjet
from r758_spherical_generating_function import canonical


def common_material(base,grid):
    """Use the inherited 64-point definition, including signed zeros of the actual source slope."""
    public();r=grid.r;v=base.paid(r);k,dk=bump(r)
    on=(r<.085)|(r>.21)
    axis=np.stack((np.sin(v['omega']),np.zeros(len(r)),np.cos(v['omega'])),axis=-1)
    dw=np.sum(v['center'][:,2]*axis,axis=1);slope=np.sum(v['center'][:,1]*axis,axis=1)
    w=2.01*base.M*k-np.where(on,slope,0.);wp=2.01*base.M*dk-np.where(on,dw,0.)
    E,Ep=original_fixed_reference(base,r)
    if base.order!=64 or not 10.87<base.M<10.89:raise ValueError('Genuine original R738 Base64 scalar required.')
    return dict(w=w,wp=wp,E=E,Ep=Ep,same_reference_order=base.order,peak_mu_lower=.372,
          actual_signed_square_discrepancy=float(abs(1+w*w-E).max()),
          actual_derivative_discrepancy=float(abs(2*w*wp-Ep).max()))


def full(grid,phi,material,theta,labels,x,band=(.105,.175),center_from_mean=False):
    public();par=x[2:];r=grid.r[:,None,None]
    got=canonical(grid,phi,material['w'],material['wp'],material['E'],material['Ep'],theta,labels,par,material['peak_mu_lower'])
    shape=got['shape'];P,T,n=got['P'],got['T'],got['n'];m=got['speed'];mP=tuple(m*z for z in P)
    def tri(t,i,k):return vecjet(t,i,k,shape)
    er=lambda angle:np.column_stack((np.cos(angle)*np.cos(phi),np.sin(phi),-np.sin(angle)*np.cos(phi)))
    et=lambda angle:np.column_stack((-np.cos(angle)*np.sin(phi),np.cos(phi),np.sin(angle)*np.sin(phi)))
    outer=(er(0.),et(0.),-er(0.));inner=(er(theta),et(theta),-er(theta))
    F=tuple(grid.primitive_from_outer(tri(mP,0,j),r[-1,0,0]*e) for j,e in enumerate(outer))
    raw_center=np.mean(F[0][0],axis=0)
    C=np.array([raw_center[0],0.,raw_center[2]]) if center_from_mean else np.array([x[0],0.,x[1]])
    delta=[r[0,0,0]*v-F[j][0] for j,v in enumerate(inner)];delta[0]=delta[0]+C
    ch,cp,cpp=smooth_join(grid.r,*band)
    pos=F[0]+ch*delta[0];dr=tri(mP,0,0)+cp*delta[0];dp=F[1]+ch*delta[1]
    rr=tri(mP,1,0)+cpp*delta[0];rp=tri(mP,0,1)+cp*delta[1];pp=F[2]+ch*delta[2]
    actual=(pos,dr,dp/r,rr,rp/r,pp/r**2)
    N,Nr,Np=tri(n,0,0),tri(n,1,0),tri(n,0,1)
    T0=tri(T,0,0);Tphi=tri(T,0,1);Tr=tri(T,1,0)
    P0=tri(P,0,0);Pphi=tri(P,0,1);scalar=got['scalar']
    dot=lambda p,q:np.sum(p*q,axis=-1)
    r2=r[:,:,0];speed=m.value
    scphi=(r2*(dot(Tphi,Nr)+dot(T0,tri(n,1,1)))-
         speed*(dot(Pphi,Np)+dot(P0,tri(n,0,2))))
    curlvec=scalar[...,None]*N
    integ=grid.primitive_from_outer(curlvec,np.zeros_like(N[-1]))
    L=F[1]-r*T0
    differentiated_integrand=scphi[...,None]*N+scalar[...,None]*Np
    Li=grid.primitive_from_outer(differentiated_integrand,np.zeros_like(N[-1]))
    Lp=F[2]-r*Tphi
    E=material['E'][:,None]
    gram=(dot(dr,dr)/E-1,dot(dr,dp/r)/np.sqrt(E),dot(dp/r,dp/r)-1)
    cap=[]
    for ix,angle,c in ((0,theta,C),(-1,0.,np.zeros(3))):
        u,v=er(angle),et(angle);rad=r[ix,0,0]
        known=(c+rad*u,u,v,np.zeros_like(u),v/rad,-u/rad)
        cap.append([float(np.linalg.norm((z[ix]-a).real,axis=-1).max()) for z,a in zip(actual,known)])
    return dict(actual_six=actual,actual_Gram=gram,design_n=N,design_P=P0,design_T=T0,normal_scalar=scalar,
               normal_scalar_phi=scphi,prescribed_center=C,radially_developed_center=raw_center,
               all_angle_inner_mismatch=tuple(delta),exact_rim_six_read=cap,
               developed_outer_angular_defect=L,scalar_integral=integ,
               scalar_compatibility_diagnostics=dict(
                  integrated_angle_error=float(abs((L-integ).real).max()),integrated_angle_derivative_error=float(abs((Lp-Li).real).max()),
                  prescribed_connection_errors=[float(abs(got[k].real).max()) for k in
                    ('literal_Jacobian_difference','literal_connection_phi_difference','literal_connection_r_difference','literal_common_E_difference')],
                  physical_curl_vector_error=float(abs((tri(mP,0,1)-(T0+r*Tr)-curlvec).real).max()),
                  implicit_roots_and_jet_errors=got['implicit_jet_residuals'],
                  positive_chart_guards=got['canonical_positive_bounds']),
               exact_continuous_Gram_or_whole_reach_established=False)


def source_target(six):
    """All six donor coordinates must be supplied on the VERY SAME material grid, once."""
    F,D,Y,rr,rp,pp=six;N=np.cross(D,Y);mag=np.sqrt(np.sum(N*N,axis=-1))
    if np.any(mag<=0) or not np.all(np.isfinite(mag)):raise FloatingPointError('Actual R748 transfer surface is singular.')
    return dict(n=N/mag[...,None],position=F,first=[D,Y],second=[rr,rp,pp])


def full_action(grid,phi,material,theta,labels,x,direction):
    """One actual nonlocal column/direction. The caller pays one such call for every material column."""
    h=2e-24;q=full(grid,phi,material,theta,labels,np.asarray(x,complex)+1j*h*np.asarray(direction))
    return dict(six=tuple(z.imag/h for z in q['actual_six']),normal=q['design_n'].imag/h,
       three_Gram=tuple(z.imag/h for z in q['actual_Gram']),scalar=q['normal_scalar'].imag/h,
       scalar_phi=q['normal_scalar_phi'].imag/h,mean_center=q['radially_developed_center'].imag/h,
       actual_inner_position_row=q['all_angle_inner_mismatch'][0].imag/h)

