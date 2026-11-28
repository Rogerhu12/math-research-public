"""R738 geometry and high-accuracy continuous tail input at real material radii."""
import math
import numpy as np
from scipy.integrate import quad,solve_ivp
from r734_true_dyadic_tail import I,D,B,L0,ONE,projective,reduced_cell,widths
from r726_closed_spinor_fourier import lift,add,mul,neg,inv,stereo

A0,B0=.075,.22
THETA=np.arcsin(.27)
WEIGHT=1/32
SIGNS=(-1,1)
MODES=(2,3)
FIRST={-1:-3,1:-2}
RATIO={-1:15/44,1:1.}
HALFWIDTH=.0025
TILT_NORMAL=np.array([np.sin(THETA),0.,np.cos(THETA)])
ZAXIS=np.array([0.,0.,1.])


def stepp(t):
    t=np.asarray(t);v=np.clip(t,0.,1.)
    h=v**3*(10+v*(-15+6*v))
    d=30*v**2*(1-v)**2
    dd=60*v*(1-v)*(1-2*v)
    return h,d,dd


def ramp(r,c):
    v=np.asarray(r)-c;x=np.clip(v/HALFWIDTH,-1.,1.)
    norm=35/32
    aa=x-x**3+3*x**5/5-x**7/7+16/35
    bb=x**2/2-3*x**4/4+x**6/2-x**8/8-1/8
    val=np.where(v<=-HALFWIDTH,0.,np.where(v>=HALFWIDTH,v,norm*(v*aa-HALFWIDTH*bb)))
    der=np.where(v<=-HALFWIDTH,0.,np.where(v>=HALFWIDTH,1.,norm*aa))
    return val,der


def bump(r):
    r=np.asarray(r)
    z=[ramp(r,c) for c in (.0875,.1475,.2075)]
    value=z[0][0]-2*z[1][0]+z[2][0];dx=z[0][1]-2*z[1][1]+z[2][1]
    active=(r>.085)&(r<.21)
    return np.where(active,value,0.),np.where(active,dx,0.)


def H_and_derivative(t,L):
    delta=L/B0;half=delta/2
    a,da,_=stepp((t-.5-half)/half);b,db,_=stepp((t-.75+delta)/(2*delta))
    c,dc,_=stepp((t-1+delta)/half)
    h=(1-a)/2+b-c/2;ht=-da/(2*half)+db/(2*delta)-dc/(2*half)
    return h,ht


def bounds_t(L):
    d=L/B0
    return np.array([.5,.5+d/2,.5+d,.75-d,.75+d,1-d,1-d/2,1.])


def actual_cell(x):
    # x is the positive mother distance, and L0=2^-9.
    n=int(np.floor(np.log2((1/512)/x)))
    L=np.ldexp(1/512,-n)
    if x>L:n-=1;L*=2
    if x<L/2:n+=1;L/=2
    return n,L


def w_actual(sign,x):
    if x==0:return 0.,0.
    edge=np.ldexp(1/512,-FIRST[sign])
    if x>=edge:
        return .5*x**4,-sign*2*x**3
    n,L=actual_cell(x);t=x/L;h,h_t=H_and_derivative(t,L)
    logterm=math.log(256/x**2)
    w=WEIGHT*x**5*math.exp(float(h)*logterm)
    dwdx=w*((5-2*h)/x+float(h_t)*logterm/L)
    return w,-sign*dwdx


def checked_line(source,sign,j,book,depth):
    side='outer' if sign==1 else 'inner'
    data=source['completed_modes'][side+str(j)]
    if data['kind']!='certified_tail_port':raise ValueError('Original R734 line not completed.')
    line=tuple(I(*v) for v in data['paid_outer_lines'][-1]['line'])
    if data['paid_outer_lines'][-1]['cell']!=0:raise ValueError('Wrong R734 cut index.')
    lines={}
    for n in range(-1,FIRST[sign]-1,-1):
        key=f'r738_certified_line_{sign}_{j}_{n}'
        if key in book.records:row=book.records[key]['data']
        else:
            for lev in range(depth+1):
                m=reduced_cell(j,n,lev,book,sign)
                cand=projective(m,line)
                if cand is not None and widths(cand)[1]<=D('.025') and cand[0].distance_from_zero()>0:
                    row=book.once(key,lambda:dict(cell=n,depth=lev,line=[v.bounds() for v in cand]));break
            else:return dict(available=False,failed_cell=n,certified_so_far=lines)
        line=tuple(I(*v) for v in row['line']);lines[str(n)]=row
    n=FIRST[sign];L=L0/(I(2)**n);r=B-sign*L
    f=ONE;k=j*j
    y=sign*(B/r)**(2*k)*I('.03125')*L**4*line[1]/line[0]
    w=I('.5')*L**4;fp=k/r+y/w;fpp=sign*(4/L)*(fp-k/r)
    U=r*y/(k-1);Up=-w*fp;Upp=sign*(4/L)*w*fp-w*fpp
    rho=I(15)/44 if sign==-1 else ONE
    def physical(v):return [(x/rho**m).bounds() for m,x in enumerate(v)]
    return dict(available=True,first=n,negative_cells=lines,physical_radius=(r*rho).bounds(),
                physical_distance=(L*rho).bounds(),f_0_1_2=physical((f,fp,fpp)),
                U_0_1_2=physical((U,Up,Upp)),V_0_1_2=physical(tuple(-u/j for u in (U,Up,Upp))))


def native_dense_at(pack,t):
    i=max(0,min(len(pack['start'])-1,np.searchsorted(pack['start'],t,side='right')-1))
    u=(t-pack['start'][i])/pack['width'][i]
    val=np.zeros_like(pack['old'][i])
    for k,coef in enumerate(reversed(pack['coeff'][i])):
        val+=coef;val*=u if k%2==0 else 1-u
    return val+pack['old'][i]


def propagated_curve(source,j,sign,nmax,rtol,count,book):
    """Two real endpoint rays and their midpoint, in the actual R734 enclosure at nmax+1."""
    if nmax!=-1:raise ValueError("This finite input extends only the genuinely new negative cells; the complete n>=0 tail is bounded from its existing receipts.")
    s0=source['completed_modes'][('outer' if sign==1 else 'inner')+str(j)]
    row=next((v for v in s0['paid_outer_lines'] if v['cell']==nmax+1),None)
    if row is None:raise ValueError('A matching paid positive cell is needed at the launch depth.')
    a,b=[v for v in row['line']]
    if b!=['1','1']:raise ArithmeticError('The input outer rays need the certified Z=1 chart.')
    # Outward conversion of the two tight decimal endpoints to native binary values.
    xs=[np.nextafter(float(a[0]),-np.inf),np.nextafter(float(a[1]),np.inf)]
    x=np.array([[xs[0],sum(xs)/2,xs[1]],[1.,1.,1.]])
    cells={};k=j*j;Bstar=256*k*(k-1)/B0**2
    for n in range(nmax,FIRST[sign]-1,-1):
        L=np.ldexp(1/512,-n);parts=bounds_t(L)
        y=x.copy();y[1]/=16
        sections=[]
        def rhs(t,state):
            F,Z=state.reshape(2,3)
            h,_=H_and_derivative(t,L);lp=2*np.log(L*t)-np.log(256.);r=1-sign*L*t/B0
            aa=r**(-2*k)*t**(-5)*np.exp(h*lp)
            bb=Bstar*r**(2*k-2)*t**3*np.exp((1-h)*lp)
            return np.r_[-aa*Z,bb*F]
        for piece,(lo,hi) in enumerate(zip(parts,parts[1:])):
            def integrate():
                sol=solve_ivp(rhs,(lo,hi),y.ravel(),method='DOP853',rtol=rtol,atol=rtol*1.e-4,dense_output=True)
                count['new_actual_high_accuracy_RHS']+=sol.nfev;count['new_segment_dense_solutions']+=1
                if not sol.success:raise ArithmeticError('Native actual tail continuation failed: '+sol.message)
                ins=sol.sol.interpolants
                return dict(start=np.array([v.t_old for v in ins]),width=np.array([v.h for v in ins]),
                    old=np.stack([v.y_old for v in ins]),coeff=np.stack([v.F for v in ins]),end=sol.y[:,-1].reshape(2,3))
            key=f'native_{sign}_{j}_{nmax}_{rtol.hex()}_{n}_{piece}'.replace('.','p').replace('+','u')
            pack=book.once(key,integrate);y=pack['end'];sections.append(pack)
        scale=y[1].copy()
        if np.any(abs(scale)<1.e-8):raise ArithmeticError('High-precision tail normalization changed chart.')
        cells[n]=(parts,sections,scale)
        x=y/scale[None,:]
    L=np.ldexp(1/512,-FIRST[sign]);r=B0-sign*L
    scale_phys=(B0/r)**k/x[0]
    for n in range(FIRST[sign],nmax+1):
        parts,sections,scale=cells[n]
        # Each cell's raw output is scale times its normalized ray at its larger distance.
        alpha=scale_phys/scale
        cells[n]=(parts,sections,alpha)
        scale_phys=alpha
    return cells


def mode_at(cells,j,sign,rphys):
    rho=RATIO[sign];rb=rphys/rho;x=abs(rb-B0)
    if x==0 or rphys==(A0 if sign==-1 else B0):return np.zeros((2,3,3))
    n,L=actual_cell(x);t=x/L
    if n not in cells:
        # Only a dyadic seam with a few ulps of coordinate conversion may choose its adjacent cell.
        adj=n+1 if n<min(cells) else n-1
        if adj not in cells or min(abs(t-.5),abs(t-1))>4.e-9:
            raise ValueError('Native mode radius lies outside the paid finite continuation.')
        n=adj;L=np.ldexp(1/512,-n);t=x/L
    cuts,sections,alpha=cells[n];t=np.clip(t,.5,1.)
    i=max(0,min(len(sections)-1,np.searchsorted(cuts,t,side='right')-1))
    F,Z=native_dense_at(sections[i],t).reshape(2,3)*alpha[None,:]
    k=j*j;f=(rb/B0)**k*F;y=sign*(B0/rb)**k*WEIGHT*L**4*Z
    w,wp=w_actual(sign,x);fp=k*f/rb+y/w;fpp=-(wp/w)*(y/w)
    U=rb*y/(k-1);Up=-w*fp;Upp=-wp*fp-w*fpp
    def divided(v,d,h):
        return np.stack((v/rb,(d/rb-v/rb**2),(h/rb-2*d/rb**2+2*v/rb**3)))/np.array([rho,rho**2,rho**3])[:,None]
    return np.stack(((k-1)/j*divided(U,Up,Upp),-j*divided(f,fp,fpp)))


def rotated_stereo_b(z,omega):
    c=np.cos(omega);s=np.sin(omega)
    def rot(a):
        out=np.empty_like(a);out[:,::2]=c*a[:,::2]-s*a[:,1::2]
        out[:,1::2]=s*a[:,::2]+c*a[:,1::2]
        return out
    unit=lift(rot,stereo(z,-1))
    first=lift(lambda v:v[:,:1],unit);one=(np.ones_like(first[0]),np.zeros_like(first[0]),np.zeros_like(first[0]))
    den=add(one,neg(first))
    if np.any(den[0].real<=.05):raise FloatingPointError('Finite tilted spinor left its declared physical chart.')
    return mul(lift(lambda v:v[:,1:],unit),inv(den))


def native_tail_spinor(directions,amplitude,sign,K):
    # directions[j] has axes d/e, radial derivative, radial sample.
    n=directions[2].shape[-1]
    ar=np.zeros((3,n,2*K+1),dtype=np.result_type(*amplitude,float))
    br=np.zeros_like(ar)
    for j,amp in zip(MODES,amplitude):
        d,e=amp*directions[j]/8
        l,h=2*(j-1)-1,2*j-1
        ar[:,:,l]-=d;ar[:,:,h]+=d;ar[:,:,l+1]-=e;ar[:,:,h+1]+=e
        br[:,:,l]-=d;br[:,:,h]-=d;br[:,:,l+1]-=e;br[:,:,h+1]-=e
    return tuple(ar),rotated_stereo_b(tuple(br),THETA if sign==-1 else 0.)
