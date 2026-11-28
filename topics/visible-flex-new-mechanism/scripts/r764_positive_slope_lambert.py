"""R764 even second harmonic, real 6/10 circle germs and the complete cap frame."""
import numpy as np
from r726_closed_spinor_fourier import public
from r758_material_jet_and_angles import J,root,sine,cosine,implicit,vecjet
from r762_high_regular_circle import Two,sin,cos,sqrt_two
from r762_material_hamiltonian import ramp_ratio,rows as shared_rows
from r762_signed_lambert_material_frame import tilt
from r764_positive_slope_material import A0,B0,LOWER,UPPER,PEAK,RATIO

K=np.sqrt(2/3)


def high(r,mu,w,side,h):
    r0=LOWER if side==-1 else UPPER
    z=r-r0
    on=abs(z)<h
    tail=side*z>0
    q=J(np.where(on,z/h,0.),np.where(on,1/h,0.))
    u=J(np.where(on&tail,side*z/.002,0.),np.where(on&tail,side/.002,0.))
    Q=10-15*u+6*u*u
    # Positive slope is proportional to u^3 Q(u) (.01-.002u)^4.
    den=3+u*((-15+12*u)/Q-.008/(.01-.002*u))
    rt=side*.002*u/den
    x=J(np.where(on&~tail,-side*z/.0025,0.),np.where(on&~tail,-side/.0025,0.))
    rc=-side*ramp_ratio(x)
    m=root(1+w*w)
    G=m*m/(m+1)*rt.at(tail,rc)
    c=np.where(tail,6/7,10/11)
    env=(1-q*q)**5
    v=(c*q*env).at(on,0.)
    vp=(c*(env-10*q*q*(1-q*q)**4)/h).at(on,0.)
    d=(v+G*vp).at(on,0.)
    d=d.at(z!=0,J(np.zeros_like(r),dr=1/h))
    return v,d,1.,13.


def radial_rows(r,mu,w,cal,labels):
    native=[(deg,max(1,j),kind) for deg,j,kind in labels if deg not in (20,21)]
    if any(deg<0 or deg>15 for deg,_,_ in native):
        raise ValueError('R764 has two high circles and no interior simple slope reversal.')
    common,b_bounds,d_bounds=shared_rows(r,mu,w,cal,native)
    sub=iter(zip(common,b_bounds,d_bounds))
    values=[]
    cache={}
    for deg,j,kind in labels:
        if deg in (20,21):
            if deg not in cache:
                cache[deg]=high(r,mu,w,-1 if deg==20 else 1,cal['high_zero_window'])
            b,d,bo,do=cache[deg]
            values.append((b,d,j,kind,bo,do))
        else:
            (b,d,_,_),bo,do=next(sub)
            values.append((b,d,j,kind,bo/max(1,j),do/max(1,j)))
    return values


def tail(r,mu,ps,nu,phase):
    rho=np.where(r<PEAK,RATIO[-1],RATIO[1])
    slope=.5*(.00785/rho)**4
    m=np.sqrt(1+slope*slope)
    cut=slope**2/(m*(m+1))
    small=.5*.00785**4
    ms=np.sqrt(1+small**2)
    unit=np.sqrt(2)*small/np.sqrt(ms*(ms+1))
    gain=-nu*unit*phase
    xi=np.where(r<PEAK,r-A0,B0-r)
    deep=(xi<.00795)&(mu.value.real<cut)
    u=(mu/cut).at(deep,1.)
    polynomial=5+u*(-10+u*(10+u*(-5+u)))
    return gain*u*polynomial,(5*gain/cut)*(1-u)**4,deep,gain*ps*polynomial/(2*cut),gain,unit


def curve(t):
    v=K*sin(2*t)
    return v,2*K*cos(2*t),-3*v,sin(4*t)/4


def circle_velocity(t,gain):
    tt=Two(t,1.,0.)
    v,p,j,prim=curve(tt)
    s=1-p
    w=gain*gain
    lam=sqrt_two(1-w*(s*s+v*v)/4)
    f=-s*j+v
    x=-lam*j+w*s*f/(4*lam)
    y=lam+w*v*f/(4*lam)
    d=w*(-v+prim)/2
    c,k=cos(d),sin(d)
    ratio=-(x*c+y*k)/(y*c-x*k)
    return ratio.x,ratio.d,ratio.dd


def canonical(grid,phi,w,wp,E,Ep,theta,labels,par,calibration):
    public()
    if calibration.get('material_definition')!='R764-positive-cutoff':
        raise ValueError('The new positive material and its new integral are required.')
    M=calibration['M']
    if not 10.87<M<10.89 or not 0<=theta<=np.arcsin(.27):
        raise ValueError('Wrong calibration or physical angle.')
    coeff=np.asarray(par)
    if len(coeff)!=1+len(labels) or not 0<coeff[0].real<=.01:
        raise ValueError('Use one positive regular-circle scale followed by all native Hamiltonians.')
    if any(not isinstance(j,(int,np.integer)) or j<0 or trig not in ('sin','cos')
           or (j==0 and trig!='cos') for _,j,trig in labels):
        raise ValueError('Invalid actual material frequency.')
    r=np.asarray(grid.r)[:,None]
    w=J(np.asarray(w)[:,None],np.asarray(wp)[:,None])
    m=J(np.sqrt(E)[:,None],(np.asarray(Ep)/(2*np.sqrt(E)))[:,None])
    if np.any(w.value.real>0):raise ValueError('The physical upward source uses the negative Lambert slope.')
    mu=w*w/(m*(1+m))
    ps=np.sqrt(2)*w/root(m*(1+m))
    phase=theta/np.arcsin(.27)
    e,q,deep,deep_ratio,gain,unit=tail(r,mu,ps,coeff[0],phase)
    angle,g,peak=tilt(r,mu,M,theta)
    cal=dict(calibration)
    h0=float(cal.get('high_zero_window',1.e-5))
    if not 0<h0<=1.e-5:raise ValueError('Unsupported true high-circle window.')
    h=h0*phase**2
    cal['high_zero_window']=h if phase else h0
    rows=radial_rows(r,mu,w,cal,labels)
    bs,ds=J(0.),J(0.);hb=hd=0.
    if phase:
        for side,center in ((-1,LOWER),(1,UPPER)):
            bv,dv,bb,dd=high(r,mu,w,side,h)
            bs+=h/center*bv;ds+=h/center*dv
            hb=max(hb,h/center*bb);hd=max(hd,h/center*dd)
    amp=30*hb;grad=100*hb;shift=30*hd;width0=10*hd
    grouped={}
    for a,(bv,dv,j,kind,bb,dd) in zip(coeff[1:],rows):
        amp+=abs(a.real)*j*bb;grad+=abs(a.real)*j*j*bb
        shift+=abs(a.real)*j*dd;width0+=abs(a.real)*dd
        old_b,old_d=grouped.get((j,kind),(J(0.),J(0.)))
        grouped[j,kind]=old_b+a*bv,old_d+a*dv
    if amp>=1 or peak>=.395:raise FloatingPointError('Unseparated material area radius.')
    pmax=np.sqrt(2*.395*(1+amp))+abs(gain.real)
    radius=pmax+1.83*abs(gain.real)
    if radius>=np.sqrt(2):raise FloatingPointError('Lambert graph crosses its hemisphere.')
    angular=pmax+np.sqrt(2*.395)*grad/(2*np.sqrt(1-amp))+2.45*abs(gain.real)
    ny_rate=(1+radius**2/(4*np.sqrt(1-radius**2/4)))*angular
    gr=(15*abs(theta)/(8*peak))*2/(3*np.sqrt(3))
    v=abs(coeff[0].real*phase)
    qc=10*v*(1.64*np.sqrt(1+amp)+.82*grad/(2*np.sqrt(1-amp))+4.65*v)
    lower=1-shift-qc-gr*ny_rate
    if lower<=0:raise FloatingPointError('The full-circle angular Jacobian is not separated.')
    shape=(len(r),len(phi));phij=J(np.asarray(phi)[None,:],dp=1.)
    mask=np.flatnonzero((abs(r[:,0]-LOWER)<=h)|(abs(r[:,0]-UPPER)<=h)) if phase else []
    def local(t):
        if not len(mask):return J(0.),J(0.),J(0.)
        small=J.pack({k:np.broadcast_to(x,shape)[mask] for k,x in t.a.items()})
        out=[]
        for value in circle_velocity(small,gain):
            terms={}
            for k,x in value.a.items():
                a=np.zeros(shape,dtype=np.asarray(x).dtype);a[mask]=x;terms[k]=a
            out.append(J.pack(terms))
        return out
    def raw(t):
        corr,c1,c2=local(t)
        H=mu*bs*corr;D=ds*corr;Dt=ds*c1;fac=1+bs*c1;ft=bs*c2
        for (j,kind),(bv,dv) in grouped.items():
            if kind=='sin':z,zt=sine(j*t),j*cosine(j*t)
            else:z,zt=cosine(j*t),-j*sine(j*t)
            H+=mu*bv*z;D+=dv*z;Dt+=dv*zt;fac+=bv*zt;ft-=bv*j*j*z
        scale=root(fac+deep_ratio.at(deep,0.)**2)
        A=ps*scale;At=ps*ft/(2*scale)
        if phase:
            regular=root((ps*ps*fac+e*e).at(~deep,1.))
            A=A.at(deep,-regular);At=At.at(deep,-mu*ft/regular)
        sn,cs=sine(t),cosine(t);v,vp,vs,prim=curve(t)
        x=(A-e*vp)*cs-e*v*sn;y=(A-e*vp)*sn+e*v*cs
        xt=(At-e*vs)*cs-A*sn;yt=(At-e*vs)*sn+A*cs
        lam=root(1-(x*x+y*y)/4);ny=lam*y
        nyt=lam*yt-y*(x*xt+y*yt)/(4*lam)
        delta=D+q*(-A*v+e*prim)+g*ny
        dt=Dt+q*(-At*v-A*vp+e*(1+v*vs))+g*nyt
        extra=(-A*e*v+e*e*prim)/2
        return delta,dt,(x,y,lam,ny,H,extra)
    def real(t):
        f,d,_=raw(J(t))
        return np.broadcast_to(f.value.real,shape),np.broadcast_to(1+d.value.real,shape)
    def both(t):
        f,d,_=raw(t);return f,d
    t,err=implicit(phij,(shape,real,both),1+width0+2*np.pi*(qc+gr*ny_rate))
    _,_,(x,y,lam,ny,H,extra)=raw(t)
    nx,nz=lam*x,1-(x*x+y*y)/2
    pole=(nx,ny,1+nz)
    ex=tuple(i-nx*v/(1+nz) for i,v in zip((1,0,0),pole))
    ey=tuple(i-ny*v/(1+nz) for i,v in zip((0,1,0),pole))
    delta=(1-mu)*phij+mu*t+H+extra
    c,s=cosine(delta),sine(delta);cg,sg=cosine(angle),sine(angle)
    def rotate(v):
        x,y,z=v
        return cg*x+sg*z,y,-sg*x+cg*z
    n=rotate((nx,ny,nz))
    P=rotate(tuple(c*x+s*y for x,y in zip(ex,ey)))
    T=rotate(tuple(-s*x+c*y for x,y in zip(ex,ey)))
    vec=lambda value,i,j:vecjet(value,i,j,shape)
    dot=lambda x,y:np.sum(x*y,axis=-1)
    n0,nr,nt=vec(n,0,0),vec(n,1,0),vec(n,0,1)
    p0,t0=vec(P,0,0),vec(T,0,0)
    return dict(n=n,P=P,T=T,speed=m,shape=shape,scalar=r*dot(t0,nr)-m.value*dot(p0,nt),
        canonical_positive_bounds=[lower,1-amp,1-radius**2/2],
        whole_rotated_nz_lower=np.cos(theta)*(1-radius**2/2)-np.sin(theta)*radius,
        actual_scale=float(np.real(gain)),signed_lambert_scale=unit,
        high_circle_regular_scale=float(np.real(gain)),high_circle_window=h,
        source_peak_mu=peak,implicit_jet_residuals=[err],material_angles_phi=phij.value[0],
        literal_Jacobian_difference=dot(n0,np.cross(nr,nt))-mu.jet(1,0),
        literal_connection_phi_difference=dot(t0,vec(P,0,1))-(1-mu.value),
        literal_connection_r_difference=dot(t0,vec(P,1,0)),
        literal_common_E_difference=1+w.value**2-np.asarray(E)[:,None],periodic_real_map_definition=True)
