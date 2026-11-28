"""R762 signed material Gauss map and exact cap spin. Science runs only in public Actions."""
import numpy as np
from r726_closed_spinor_fourier import public
from r738_negative_tail_and_macro_source import bump
from r758_material_jet_and_angles import J, cosine, implicit, root, sine, vecjet

from r762_high_regular_circle import coefficient, shapes, velocity, SOURCE_MU

A, B = .075, .22
LEFT, PEAK, RIGHT = .085, .1475, .21
WIDTH = .0025
BPEAK = .06 - 2*WIDTH*(35/32)/8


def tail_perturbation(r, mu, coefficient):
    """Change at true quartic distances; no positive-width tail is fixed to zero."""
    ratio = np.where(r < PEAK, 15/44, 1.)
    slope = .5*(.00785/ratio)**4
    mc = np.sqrt(1+slope**2)
    muc = slope**2/(mc*(1+mc))
    small_slope = .5*.00785**4
    small_m = np.sqrt(1+small_slope**2)
    unit = np.sqrt(2)*small_slope/np.sqrt(small_m*(1+small_m))
    size = coefficient*unit
    distance = np.where(r < PEAK, r-A, B-r)
    active = (distance < .00795) & (mu.value.real < muc)
    u = (mu/muc).at(active, 1.)
    # 1-(1-u)^5 in a form that retains the true deep-cell leading term.
    smooth = u*(5+u*(-10+u*(10+u*(-5+u))))
    eps = size*smooth
    q = (5*size/muc)*(1-u)**4
    return eps, q, unit


def tilt(r, mu, calibration, theta):
    """Regular material phase across the two preimages and the real central turn."""
    k = 2.01*calibration
    mstar = np.sqrt(1+(k*BPEAK)**2)
    peak = 1-1/mstar
    central = (r > LEFT) & (r < RIGHT)
    z = r-PEAK
    top = central & (abs(z)<WIDTH)
    exterior = central & ~top
    regular = root((1-mu/peak).at(exterior, 1.))
    b, db = bump(r)
    bj = J(b, db)
    m = root(1+(k*bj)**2)
    zz = J(np.where(top,z,0.), np.where(top,1.,0.))
    t = zz/WIDTH
    d = (35/(32*WIDTH))*(1-t*t/2+t**4/5-t**6/28)
    local = k*zz*root(d*(BPEAK+bj)/(m*mstar*peak*(m+mstar)))
    sign = np.where(r<=PEAK,-1.,1.)
    y = local.at(top,(sign*regular).at(exterior,sign))
    angle = (theta*(.5-1.25*y**3+.75*y**5)).at(central,np.where(r<=PEAK,theta,0.))
    rate = ((15*theta/(8*peak))*y*(1-y*y)).at(central,0.)
    return angle, rate, peak


def canonical(grid,phi,w,wp,E,Ep,theta,labels,par,calibration,*,hamiltonian=None):
    """One real signed Gauss field. The backend gives rows (B,D,j,trig) and two bound arrays.

    H=mu*B*trig(j*t), H_r=mu_r*D*trig(j*t). Each full-material bound includes j.
    The first parameter controls the nonconstant zero-area circles. Others use labels.
    """
    public()
    if hamiltonian is None:
        from r762_material_hamiltonian import rows as hamiltonian
    r = np.asarray(grid.r)[:,None]
    wj = J(np.asarray(w)[:,None],np.asarray(wp)[:,None])
    m = J(np.sqrt(E)[:,None],(np.asarray(Ep)/(2*np.sqrt(E)))[:,None])
    mu = wj**2/(m*(1+m))
    signed_p = np.sqrt(2)*wj/root(m*(1+m))
    coef = np.asarray(par)
    if not len(coef) == 1+len(labels):
        raise ValueError('One actual zero-circle scale and every Hamiltonian column are required.')
    fixed_M = calibration['M'] if isinstance(calibration,dict) else calibration
    if not 10.87<fixed_M<10.89 or not 0<=theta<.274:
        raise ValueError('The R762 all-material chart guards use this R738 source and cap range.')
    phase = theta/np.arcsin(.27)
    eps_coef = coef[0]*phase**2
    eps, q, unit = tail_perturbation(r,mu,eps_coef)
    high_eta = eps_coef*unit
    reg, regq, region, gain = coefficient(r,mu,phase)
    ratio = high_eta/gain if phase else 0.
    if abs(np.real(ratio))>1:
        raise FloatingPointError('The regular high-circle tangent requires |epsilon/e|<=1.')
    B0,D0=J(0.),J(0.)
    bscale,dscale=0.,0.
    window=0.
    if phase:
        if not isinstance(calibration,dict):
            raise ValueError('Actual quartic tail primitives are required for the high-zero frame.')
        from r762_material_hamiltonian import high_circle
        window = min(1.e-5,float(calibration.get('high_zero_window',1.e-5)))*phase**2
        for side,r0 in ((-1,LEFT),(1,RIGHT)):
            v,s,vb,ds=high_circle(r,wj,side,calibration['tail_edge_magnitude'][str(side)],window)
            B0 += (window/r0)*v
            D0 += (window/r0)*s
            bscale=max(bscale,window*vb/r0)
            dscale=max(dscale,window*ds/r0)
    angle, rate, peak = tilt(r,mu,fixed_M,theta)
    if any(not isinstance(j,(int,np.integer)) or j<0 or (j==0 and trig!='cos')
           for _,j,trig in labels):
        raise ValueError('Use nonnegative frequencies and cosine for the material mean.')
    native_labels = [(degree,max(1,j),trig) for degree,j,trig in labels]
    native, b_abs, d_abs = hamiltonian(r,mu,wj,calibration,native_labels)
    rows = [(v,d,j,trig) for (v,d,_,_),(_,j,trig) in zip(native,labels)]
    if not len(rows)==len(labels)==len(b_abs)==len(d_abs):
        raise ValueError('Every genuine Hamiltonian row is needed.')
    coeff = coef[1:]
    modes = [j for _,_,j,_ in rows]
    if any(not np.isfinite(v) or v<0 for v in (*b_abs,*d_abs)):
        raise ValueError('Full-material positive majorants are required for all rows.')
    amp = sum(abs(a.real)*v for a,j,v in zip(coeff,modes,b_abs) if j)
    grad = sum(abs(a.real)*j*v for a,j,v in zip(coeff,modes,b_abs))
    shift = sum(abs(a.real)*d for a,j,d in zip(coeff,modes,d_abs) if j)
    shift0 = sum(abs(a.real)*d/max(1,j) for a,j,d in zip(coeff,modes,d_abs))
    amp += 100*bscale
    grad += 500*bscale
    shift += 100*dscale
    shift0 += 20*dscale
    if amp>=1 or peak>=.395:
        raise FloatingPointError('The genuine area radius is not positively separated.')
    e = abs(eps_coef.real)
    pmax = np.sqrt(2*.395*(1+amp))
    R = pmax+abs(gain)+5.1*e*unit+3.61*abs(gain)
    if R>=np.sqrt(2):
        raise FloatingPointError('Lambert field leaves the open hemisphere.')
    angular = pmax+abs(gain)+np.sqrt(2*.395)*grad/(2*np.sqrt(1-amp))+3.45*e*unit+4*abs(gain)
    ny_bound = (1+R*R/(4*np.sqrt(1-R*R/4)))*angular
    rate_bound = (15*abs(theta)/(8*peak))*(2/(3*np.sqrt(3)))
    cost = 10*e*(3.45*np.sqrt(1+amp)+3.64*grad/(2*np.sqrt(1-amp))+12.6*e)
    # The two coefficient transitions have disjoint physical supports.
    weak=np.sqrt(2*SOURCE_MU)
    reg_cost=(5*abs(gain)/SOURCE_MU)*(abs(gain)+3*(weak*np.sqrt(1+amp)+abs(gain))
              +weak*grad/np.sqrt(1-amp)+2*(3.45*e*unit+4*abs(gain)))
    cost=max(cost,reg_cost)
    lower = 1-shift-cost-rate_bound*ny_bound
    if lower<=0:
        raise FloatingPointError('The full material angular map is not separated.')
    width = 1+shift0+2*np.pi*(cost+rate_bound*ny_bound)
    grouped = {}
    for a,(v,d,j,kind) in zip(coeff,rows):
        if not isinstance(j,(int,np.integer)) or j<0 or kind not in ('sin','cos'):
            raise ValueError('Unknown material Fourier row.')
        bv,bd = grouped.get((j,kind),(J(0.),J(0.)))
        grouped[j,kind] = bv+a*v,bd+a*d

    shape0 = (len(r),len(phi))
    high_rows=np.flatnonzero((abs(r[:,0]-LEFT)<=window)|(abs(r[:,0]-RIGHT)<=window)) if phase else []
    def high_velocity(t):
        if len(high_rows)==0:
            return J(0.),J(0.),J(0.)
        local=J.pack({k:np.broadcast_to(value,shape0)[high_rows] for k,value in t.a.items()})
        result=[]
        for high in velocity(local,ratio,gain):
            data={}
            for k,value in high.a.items():
                full=np.zeros(shape0,dtype=np.asarray(value).dtype)
                full[high_rows]=value
                data[k]=full
            result.append(J.pack(data))
        return result
    def raw(t):
        sn,cs,b,bp,bs,v,vp,vs,bb,bv,vb,vv=shapes(t)
        corr,dc,dcc=high_velocity(t)
        H=mu*B0*corr
        D=D0*corr
        Dt=D0*dc
        mult=1+B0*dc
        mult_t=B0*dcc
        for (j,kind),(rv,rd) in grouped.items():
            if kind == 'sin':
                trig,der = sine(j*t), j*cosine(j*t)
            else:
                trig,der = cosine(j*t), -j*sine(j*t)
            H += mu*rv*trig
            D += rd*trig
            Dt += rd*der
            mult += rv*der
            mult_t -= rv*(j*j)*trig
        scale = root(mult)
        p = signed_p*scale
        pt = signed_p*mult_t/(2*scale)
        active=region & (reg.value.real>0)
        regular_p=root((p*p+reg*reg).at(active,1.))
        pt=(mu*mult_t/regular_p).at(active,pt)
        p=regular_p.at(active,p)
        l=eps*b+reg*v
        lt=eps*bp+reg*vp
        sharp=eps*bs+reg*vs
        x=(p-lt)*cs-l*sn
        y=(p-lt)*sn+l*cs
        xt=(pt-sharp)*cs-p*sn
        yt=(pt-sharp)*sn+p*cs
        lam=root(1-(x*x+y*y)/4)
        ny=lam*y
        nyt=lam*yt-y*(x*xt+y*yt)/(4*lam)
        delta_phi=(D+q*(-p*b+eps*bb+reg*bv)
                   +regq*(-p*v+eps*vb+reg*vv)+rate*ny)
        derivative=(Dt+q*(-pt*b-p*bp+b*sharp)
                    +regq*(-pt*v-p*vp+reg+v*sharp)+rate*nyt)
        phase_extra=(-p*l+eps**2*bb+eps*reg*(bv+vb)+reg**2*vv)/2
        return delta_phi,derivative,(x,y,lam,ny,H,phase_extra)

    phij = J(np.asarray(phi)[None,:],dp=1.)
    def real(u):
        f,df,_ = raw(J(u))
        return np.broadcast_to(f.value.real,shape0),np.broadcast_to(1+df.value.real,shape0)
    def differentiated(t):
        f,df,_ = raw(t)
        return f,df
    t,err = implicit(phij,(shape0,real,differentiated),width)
    _,_,(x,y,lam,ny,H,phase_extra) = raw(t)
    nx,nz = lam*x,1-(x*x+y*y)/2
    pole = (nx,ny,1+nz)
    ex = tuple(c-nx*v/(1+nz) for c,v in zip((1,0,0),pole))
    ey = tuple(c-ny*v/(1+nz) for c,v in zip((0,1,0),pole))
    # b(0)=b'(0)=0 fixes the material meridian of the raw lift. D(r,0) may move.
    delta = (1-mu)*phij+mu*t+H+phase_extra
    cd,sd = cosine(delta),sine(delta)
    cg,sg = cosine(angle),sine(angle)
    def rotate(v):
        x,y,z = v
        return cg*x+sg*z,y,-sg*x+cg*z
    n = rotate((nx,ny,nz))
    P = rotate(tuple(cd*u+sd*v for u,v in zip(ex,ey)))
    T = rotate(tuple(-sd*u+cd*v for u,v in zip(ex,ey)))
    def extract(field,i,j):
        return vecjet(field,i,j,shape0)
    dot = lambda a,b: np.sum(a*b,axis=-1)
    n0,nr,nt = (extract(n,i,j) for i,j in ((0,0),(1,0),(0,1)))
    p0,t0 = extract(P,0,0),extract(T,0,0)
    scalar = r*dot(t0,nr)-m.value*dot(p0,nt)
    return dict(n=n,P=P,T=T,speed=m,shape=shape0,scalar=scalar,
        canonical_positive_bounds=[lower,1-amp,1-R**2/2],
        whole_rotated_nz_lower=np.cos(abs(theta))*(1-R**2/2)-np.sin(abs(theta))*R,
        signed_lambert_scale=unit,actual_scale=float(np.real(high_eta)),high_circle_regular_scale=gain,
        high_circle_window=window,
        source_peak_mu=peak,implicit_jet_residuals=[err],material_angles_phi=phij.value[0],
        literal_Jacobian_difference=dot(n0,np.cross(nr,nt))-mu.jet(1,0),
        literal_connection_phi_difference=dot(t0,extract(P,0,1))-(1-mu.value),
        literal_connection_r_difference=dot(t0,extract(P,1,0)),
        literal_common_E_difference=1+wj.value**2-np.asarray(E)[:,None],
        periodic_real_map_definition=True)
