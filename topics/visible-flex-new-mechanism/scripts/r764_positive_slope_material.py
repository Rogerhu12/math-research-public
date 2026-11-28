"""New R764 metric, exact cutoff polynomial and both material two-jets. Public Actions only."""
from math import comb
import numpy as np
from r726_closed_spinor_fourier import public
from r738_negative_tail_and_macro_source import A0,B0,RATIO,THETA,HALFWIDTH,bump,stepp,w_actual
from r738_real_macro_reference import SEPARATORS

LOWER=.085
PEAK=.1475
UPPER=.21


def central(r):
    """Same real convolution, with a stable fifth-order germ at both actual endpoints."""
    r=np.asarray(r)
    b,d=bump(r)
    sign=np.where(r<PEAK,1.,-1.)
    x=np.where(r<PEAK,r-LOWER,UPPER-r)/HALFWIDTH
    active=(x>=0)&(x<2)
    u=np.where(active,x,0.)
    f=2/5-2*u/5+u*u/7-u**3/56
    fp=-2/5+2*u/7-3*u*u/56
    return (np.where(active,(35/32)*HALFWIDTH*u**5*f,b),
            np.where(active,sign*(35/32)*u**4*(5*f+u*fp),d))


def cutoff_remainder(xi,rho):
    """Integral from xi to .01 of the quartic germ times the true quintic cutoff."""
    y=np.clip((.01-np.asarray(xi))/.002,0.,1.)
    total=np.zeros_like(y)
    for i in range(5):
        coeff=comb(4,i)*.01**(4-i)*(-.002)**i
        for j,weight in ((3,10),(4,-15),(5,6)):
            total+=coeff*weight*y**(i+j+1)/(i+j+1)
    return .001*total/rho**4


def one_tail(base,r,need_positions):
    side=-1 if r<PEAK else 1
    rho=RATIO[side]
    rim=A0 if side==-1 else B0
    xi=abs(r-rim)
    # At the two nominal joins the true cutoff is exactly zero.
    if (r>=LOWER if side==-1 else r<=UPPER):return 0.,0.,0.
    base.count['r764_native_positive_tail_slope_evaluations']=base.count.get('r764_native_positive_tail_slope_evaluations',0)+1
    w,d=w_actual(side,xi/rho)
    u=np.clip((.01-xi)/.002,0.,1.)
    if xi<=.008:
        c,cr=1.,0.
    else:
        S,Sp,_=stepp(u)
        c=float(S)
        cr=side*float(Sp)/.002
    if not need_positions:return c*w,c*d/rho+cr*w,0.
    rest=cutoff_remainder(xi,rho)
    if xi<.008:
        base.count['r764_true_tail_primitive_queries']=base.count.get('r764_true_tail_primitive_queries',0)+2
        rest+=side*(base.slope_height(side,xi/rho)-base.slope_height(side,.008/rho))
    return c*w,c*d/rho+cr*w,side*float(rest)


def material(base,r,*,positions=False):
    public()
    if base.order!=64 or not 10.87<base.M<10.89:
        raise ValueError('R764 fixes the authenticated actual R738 Base64 calibration scalar.')
    r=np.asarray(r)
    b,db=central(r)
    tail=np.array([one_tail(base,float(v),positions) for v in r])
    W=2.01*base.M*b+tail[:,0]
    Wp=2.01*base.M*db+tail[:,1]
    if np.any(W<0):raise ArithmeticError('The new positive material acquired a negative physical slope.')
    return dict(W=W,Wp=Wp,w=-W,wp=-Wp,E=1+W**2,Ep=2*W*Wp,k=b,kp=db,
        tail=tail,calibration_M=base.M,same_reference_order=64,material_definition='R764-positive-cutoff')


def material_integral(grid,W):
    """New R764 scalar primitive; no R755/R757 material row can be used here."""
    m=np.sqrt(1+W*W)
    mu=W*W/(m*(m+1))
    prefix=np.empty_like(mu);prefix[0]=0.
    for i,j,h in grid.cells:
        local=h*(grid.P-grid.P[0])@mu[i+1:j]
        prefix[i+1:j+1]=prefix[i]+local[1:]
    other=grid.primitive_from_outer(mu,np.array(0.))
    return dict(material_I=((grid.r-A0)*mu-prefix)/(B0-A0),
        new_mu_primitive=prefix,dual_primitive_difference=float(abs(prefix-(other-other[0])).max()))


def geometry(base,r,phi,s):
    """Full geometric seed, outer plane fixed. Each call evaluates a new R764 position and six fields."""
    public()
    if not 0<=s<=1:raise ValueError('Geometric phase outside [0,1].')
    r=np.asarray(r);phi=np.asarray(phi)
    m=material(base,r,positions=True)
    base.count['r764_omega_quadrature_nodes']=base.count.get('r764_omega_quadrature_nodes',0)+len(r)*base.order
    omega=s*base.omega(r);angle_r=-s*base.M*m['k']/r
    cap_in=one_tail(base,A0,True)[2]
    cap_out=one_tail(base,B0,True)[2]
    C=np.zeros((len(r),3))
    for i,r0 in enumerate(r):
        for l,h in zip(SEPARATORS[:-1],SEPARATORS[1:]):
            lo=max(r0,l)
            if lo>=h:continue
            t=(lo+h)/2+(h-lo)*base.X/2
            base.count['r764_new_center_quadrature_nodes']=base.count.get('r764_new_center_quadrature_nodes',0)+base.order
            base.count['r764_omega_quadrature_nodes']+=base.order**2
            ang=s*base.omega(t);k=central(t)[0]
            factor=-(2.01-s)*base.M*(h-lo)/2
            C[i,0]+=factor*np.dot(base.W,k*np.sin(ang))
            C[i,2]+=factor*np.dot(base.W,k*np.cos(ang))
    tt=m['tail'][:,2]
    C[:,0]+=tt*np.sin(omega)
    C[:,2]+=tt*np.cos(omega)-cap_out
    sn=np.sin(phi)[None,:];cs=np.cos(phi)[None,:];rr=r[:,None]
    Z=(2.01-s+s*cs)*(base.M*m['k'][:,None])+m['tail'][:,0,None]
    Zr=(2.01-s+s*cs)*(base.M*m['kp'][:,None])+m['tail'][:,1,None]
    a=angle_r[:,None]
    shape=Z.shape
    def rotate(x,y,z):
        c=np.cos(omega)[:,None];t=np.sin(omega)[:,None]
        return np.stack((np.broadcast_to(c*x+t*z,shape),np.broadcast_to(y,shape),
                         np.broadcast_to(-t*x+c*z,shape)),axis=-1)
    er=rotate(cs,sn,0.);et=rotate(-sn,cs,0.)
    six=(C[:,None,:]+rr[:,:,None]*er,rotate(cs,sn,Z),rr[:,:,None]*et,
         rotate(a*Z,0.,Zr-a*cs),rotate(-sn,cs,-s*base.M*m['k'][:,None]*sn),-rr[:,:,None]*er)
    return dict(six=six,actual_relative_center=C[0] if r[0]==A0 else None,
        inner_tail_frame_translation=cap_in,outer_tail_frame_translation=cap_out,
        original_calibration_order=base.order,unresolved_deep_primitive_absolute_bound=2*np.ldexp(1/512,-26)**4,
        exact_fixed_metric_at_geometric_s_zero=(s==0),
        full_seeds_reach_and_macro_proved_in_paper=True,actual_numerical_quadrature_is_continuous_certificate=False)
