"""True material generators for the R762 Lambert map; native high-order zero-circle velocities."""
import numpy as np
from r758_material_jet_and_angles import J,root

A=.075
B=.22
SPAN=B-A
CENTERS={-1:.085,1:.21}
RATIO={-1:15/44,1:1.}
WINDOW=1e-5


def genuine_integral_data(base,grid,mu):
    """A new scalar integral on the same material; R755 A,L,S are different scientific objects."""
    r=grid.r
    out=grid.primitive_from_outer(mu,np.array(0.))
    # Right cumulative primitive subtracts two almost equal large central quantities near the inner cap.
    # Integrate from the LEFT directly using the identical shifted Gauss polynomial in every full cell.
    prefix=np.empty_like(mu);prefix[0]=0.
    for i,j,h in grid.cells:
        local=h*(grid.P-grid.P[0])@mu[i+1:j]
        prefix[i+1:j+1]=prefix[i]+local[1:]
    # At the inner actual zero, only the true phase constant matters; keep both finite primitive comparisons.
    origin=np.array([.084,.085,.21,.211])
    measured=base.paid(origin);axis=np.array([np.sin(np.arcsin(.27)),0.,np.cos(np.arcsin(.27))])
    center=measured['center'][:,0]
    mag={-1:2*np.dot(center[0]-center[1],axis),1:-2*(center[3,2]-center[2,2])}
    constants={}
    for s,rho in RATIO.items():
        H=mag[s]+.1*rho*((.01/rho)**5-(.009/rho)**5)
        if H<=0:raise ArithmeticError('The actual upper quartic tail germ did not give a positive primitive.')
        constants[str(s)]=float(H)
    return dict(material_I=((r-A)*mu-prefix)/SPAN,tail_edge_magnitude=constants,
        scalar_integral_from_a=prefix,primitive_dual_difference=float(abs(prefix-(out-out[0])).max()),
        queried_physical_radii=len(r),new_scalar_integral=True,original_DOP_repeats=0)


def ramp_ratio(s):
    P=2/5-s*2/5+s**2/7-s**3/56
    Pp=-2/5+2*s/7-3*s*s/56
    return .0025*s*P/(5*P+s*Pp)


def high_circle(r,w,side,edge,window,*,with_plateau=False):
    """B,D and B_abs,D_abs for the real kth-order germs on both sides; D_r=1/window at the circle."""
    if not 0<window<=WINDOW:raise ValueError('High-order physical speed window too wide.')
    c=CENTERS[side];rho=RATIO[side];z=r-c
    on=abs(z)<window;tail=side*z>0
    q=J(np.where(on,z/window,0.),np.where(on,1/window,0.))
    u=J(np.where(on&tail,side*z/.002,0.),np.where(on&tail,side/.002,0.))
    dist=.01-.002*u
    H=edge+.1*rho*((dist/rho)**5-(.01/rho)**5)
    omega=.5*(dist/rho)**4;omega_s=-.004*(dist/rho)**3/rho
    Q=10-15*u+6*u*u;Qp=-15+12*u
    Z=15000*(1-u)**2*H-u*Q*omega
    Zs=15000*(-2*(1-u)*H-.002*(1-u)**2*omega)-(Q+u*Qp)*omega-u*Q*omega_s
    # Z = w/u²; 2Z+uZs is separated even on u=0.
    if np.any((2*Z.value+u.value*Zs.value).real<=0):raise ArithmeticError('Unseparated actual quartic high-zero germ.')
    tail_ratio=(side*.002)*u*Z/(2*Z+u*Zs)
    s=J(np.where(on&~tail,-side*z/.0025,0.),np.where(on&~tail,-side/.0025,0.))
    central_ratio=-side*ramp_ratio(s)
    m=root(1+w*w)
    G=m*m/(m+1)*tail_ratio.at(tail,central_ratio)
    scale=np.where(tail,4/5,10/11)
    env=(1-q*q)**5
    S=(q*env*scale).at(on,0.)
    Sp=((env-10*q*q*(1-q*q)**4)*scale/window).at(on,0.)
    D=(S+G*Sp).at(on,0.)
    # The two one-sided normalized slopes converge to this common value exactly.
    D=D.at(z!=0,J(np.zeros_like(r),dr=1/window))
    if with_plateau:
        chi=((1-q*q)**6).at(on,0.)
        dchi=(chi-12*G*q*env/window).at(on,0.)
        return S,D,1.,13.,chi,dchi,20.
    return S,D,1.,13.


def rows(r,mu,w,calibration,labels):
    """Each label is (degree,j,'sin'|'cos'); bounds already include the angular frequency."""
    if not isinstance(calibration,dict) or 'material_I' not in calibration:
        raise ValueError('The actual material-integral receipt and the two tail germs are required.')
    i0=np.asarray(calibration['material_I'])[:,None]
    if i0.shape!=r.shape:raise ValueError('I must use the same complete real radial grid.')
    f=(r-A)/SPAN
    I=J(i0,dr=mu.jet(1,0)*f)/.395
    m=root(1+w*w)
    c=m*m/(m+1)
    basis={};result=[];bmax=[];dmax=[]
    for degree,j,trig in labels:
        if not isinstance(j,(int,np.integer)) or j<1 or trig not in ('sin','cos'):
            raise ValueError('All material Fourier harmonics have positive integral frequency and actual parity.')
        if degree not in basis:
            if degree in (20,21):
                side=-1 if degree==20 else 1
                basis[degree]=high_circle(r,w,side,calibration['tail_edge_magnitude'][str(side)],
                    float(calibration.get('high_zero_window',WINDOW)))
            elif degree in (22,23):
                side=-1 if degree==22 else 1
                scale=1e-7 if side==-1 else 1e-9
                t=w/scale;active=(abs(t.value.real)<1)&((r<=.1475) if side==-1 else (r>.1475))
                u=t.at(active,0.);z=(1-u*u)**6
                v=(u*z).at(active,0.)
                vd=(v+c*u*(z-12*u*u*(1-u*u)**5)).at(active,0.)
                basis[degree]=(v,vd,1.,15.)
            elif 0<=degree<=15:
                d,p=divmod(degree,3)
                spatial=I**d;sp=d*I**(d-1) if d else J(0.)
                # Distinct physical loops at the same mu retain their own integral coordinate I.
                v=(w/m)**p
                wv=(p*v/(m*m)) if p else J(0.)
                h=spatial*v
                dh=h+c*spatial*wv+mu*f*v*sp/.395
                basis[degree]=(h,dh,1.,1+1.04*p+d)
            else:raise ValueError('Unknown registered true material radial feature.')
        v,d,vb,db=basis[degree]
        result.append((v,d,int(j),trig));bmax.append(j*vb);dmax.append(j*db)
    return result,np.asarray(bmax),np.asarray(dmax)
