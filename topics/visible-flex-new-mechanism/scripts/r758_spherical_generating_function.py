"""Exact canonical material charts, explicit frame phase, and the remaining normal compatibility equation."""
import numpy as np
from r726_closed_spinor_fourier import public
from r758_material_jet_and_angles import J,arcsine,cosine,implicit,root,sine,taper,vecjet

U0=.5
SEPARATE=.24
OSC=np.pi/(2*np.log(2.))


def bounded_rows(mu,labels,r):
    """Each tuple is (side, degree>=1, upper power, angular mode>=1, 0/cos/sin)."""
    t=mu/U0
    if np.any(t.value.real<0) or np.any(t.value.real>1):raise FloatingPointError('Canonical input left its declared area disk.')
    positive=t.value.real>0;safe=t.at(positive,1.)
    # Two radial jets of the source are unnecessary. The logarithm is used only behind t^degree.
    phase=J(OSC*np.log(safe.value),dr=OSC*safe.jet(1,0)/safe.value)
    cache=[];rowmax=[]
    for side,d,power,m,trig in labels:
        if side not in (-1,0,1) or d<1 or power<0 or m<1 or trig not in (0,1,2):
            raise ValueError('Invalid registered radial/angular Hamiltonian label.')
        env=(1-t)**power
        t_env_prime=(-power*t*(1-t)**(power-1)) if power else J(0.)
        if side:
            before=(mu.value.real<SEPARATE)&((r<=.1475) if side==-1 else (r>.1475))
            base=(1-mu/SEPARATE).at(before,0.)
            db=(-6*(mu/SEPARATE)*base**5).at(before,0.)
            cut=base**6
            t_env_prime=t_env_prime*cut+env*db;env=env*cut
        wave,waveprime=((J(1.),J(0.)) if trig==0 else (cosine(phase),-sine(phase)*OSC) if trig==1
                        else (sine(phase),cosine(phase)*OSC))
        w=t**d*wave*env
        dw=t**d*((d+1)*wave*env+waveprime*env+wave*t_env_prime)
        cache.append((m,w,dw))
        # t|((1-t)^q)'| <= 1, likewise the scaled compact sextic.
        rowmax.append(m*(d+1+(OSC if trig else 0.)+int(power>0)+int(side!=0)))
    return cache,np.array(rowmax)


def canonical(grid,phi,w,wp,E,Ep,theta,labels,par,paid_peak_lower=None):
    public()
    r=grid.r[:,None];phi=np.asarray(phi)
    if len(labels)!=len(par):raise ValueError('All genuine canonical coefficients are required.')
    w=J(np.asarray(w)[:,None],np.asarray(wp)[:,None]);m=J(np.sqrt(E)[:,None],(Ep/(2*np.sqrt(E)))[:,None])
    phi=J(phi[None,:],dp=1.)
    mu=w**2/(m*(m+1));shape=(len(r),phi.value.shape[1])
    rows,bounds=bounded_rows(mu,labels,r)
    coef=np.asarray(par);lip=float(abs(coef.real)@bounds)
    amp=float(abs(coef.real)@np.array([q[0] for q in rows]))
    if lip>=.88 or amp>=.9:raise FloatingPointError('All-circle monotone canonical denominators not established.')
    if np.max(mu.value.real)*(1+amp)>=.725:raise FloatingPointError('The requested full disk exceeds the positive chart.')
    grouped={}
    for a,(j,b,d) in zip(coef,rows):
        prev=grouped.get(j,(J(0),J(0)))
        grouped[j]=(prev[0]+a*b,prev[1]+a*d)
    def terms(z,final=False):
        hu=J(0);hup=J(0);h=J(0);factor=J(1)
        for j,(b,d) in grouped.items():
            ang=z*j;sn=sine(ang);cs=cosine(ang)
            hu+=d*sn;hup+=j*d*cs
            if final:h+=mu*b*sn;factor+=j*b*cs
        return (hu,hup,h,factor) if final else (hu,hup)
    def field0(z):
        z0=np.zeros(shape);jac=np.ones(shape)
        for j,(_,d) in grouped.items():
            z0+=d.value.real*np.sin(j*z);jac+=j*d.value.real*np.cos(j*z)
        return z0,jac
    Phi,e0=implicit(phi,(shape,field0,terms),max(1.,lip+.01))
    _,_,h,factor=terms(Phi,True);U=mu*factor
    alpha=arcsine((w/m)*root(factor*(2-U)/(2-mu)))
    # Both branches must agree on an open belt about the actual material peak. Evaluate its
    # prescribed center independently of whether the requested ordinary angular lattice sees a minimum.
    mid=np.flatnonzero(r[:,0]==.1475)
    if len(mid)==1:raw_peak=float(mu.value.real[mid[0],0])
    elif paid_peak_lower is not None:raw_peak=paid_peak_lower
    else:raise ValueError('Include the true seam or provide its identified actual source lower bound.')
    umin=raw_peak*(1-amp)
    if umin<=1-np.cos(.85):raise FloatingPointError('Shared high-latitude seam not secured on its complete circle.')
    gamma,v=taper(alpha,r<=.1475,theta)
    def k0(z):return v.value.real*np.sin(z),1+v.value.real*np.cos(z)
    psi,e1=implicit(Phi,(shape,k0,lambda z:(v*sine(z),v*cosine(z))),1.)
    ca=1-U;sa=(w/m)*root(factor*(2-U)/(2-mu))
    cs,ss=cosine(psi),sine(psi);cg,sg=cosine(gamma),sine(gamma)
    def rotate(x,y,z):return cg*x+sg*z,y,-sg*x+cg*z
    n=rotate(sa*cs,sa*ss,ca)
    ex=rotate(ca*cs,ca*ss,-sa);ey=rotate(-ss,cs,J(0.))
    delta=(1-mu)*(phi-Phi)+h+(1-U)*(Phi-psi)
    cd,sd=cosine(delta),sine(delta)
    P=tuple(cd*x+sd*y for x,y in zip(ex,ey));T=tuple(-sd*x+cd*y for x,y in zip(ex,ey))
    N0=vecjet(n,0,0,shape);Nr=vecjet(n,1,0,shape);Np=vecjet(n,0,1,shape)
    P0=vecjet(P,0,0,shape);T0=vecjet(T,0,0,shape)
    dot=lambda x,y:np.sum(x*y,axis=-1)
    scalar=r*dot(T0,Nr)-m.value*dot(P0,Np)
    return dict(n=n,P=P,T=T,speed=m,shape=shape,scalar=scalar,
          canonical_positive_bounds=[1-lip,1-amp,umin],implicit_jet_residuals=[e0,e1],
          literal_Jacobian_difference=dot(N0,np.cross(Nr,Np))-mu.jet(1,0),
          literal_connection_phi_difference=dot(T0,vecjet(P,0,1,shape))-(1-mu.value),
          literal_connection_r_difference=dot(T0,vecjet(P,1,0,shape)),
          literal_common_E_difference=(1+w.value**2)-np.asarray(E)[:,None],
          material_angles_phi=phi.value[0],periodic_real_map_definition=True)

