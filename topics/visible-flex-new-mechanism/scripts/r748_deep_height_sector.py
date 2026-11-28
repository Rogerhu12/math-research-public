"""All-angle, all-depth two-jet bounds relative to the true tilted cap, for one declared height extension."""
from math import comb
from r734_true_dyadic_tail import I,D,ZERO,ONE,B,monotone_trans


def hi(a):return I(a.hi)
def f64(a):return I(D.from_float(float(a)))
def vec(a):return (a,ZERO,ZERO)
def plus(a,b):return tuple(hi(x+y) for x,y in zip(a,b))
def times(a,b):return tuple(hi(sum((comb(k,j)*a[j]*b[k-j] for j in range(k+1)),ZERO)) for k in range(3))
def invnorm(a,lo):
    u=ONE/lo
    return hi(u),hi(a[1]*u**2),hi(a[2]*u**2+2*a[1]**2*u**3)
def rootnorm(a,lo):
    return hi(monotone_trans(a[0],'sqrt')),hi(a[1]/(2*lo)),hi(a[2]/(2*lo)+a[1]**2/(4*lo**3))
def pair(a,e=None):return a,e or vec(ZERO)
def total(y):return plus(*y)
def add(x,y):return plus(x[0],y[0]),plus(x[1],y[1])
def product(x,y):return times(x[0],y[0]),plus(times(x[1],total(y)),times(x[0],y[1]))
def inverse(x,lo):
    p=invnorm(x[0],lo);s=invnorm(total(x),lo)
    return p,times(x[1],times(p,s))
def root(x,lo):
    p=rootnorm(x[0],lo);q=rootnorm(total(x),lo)
    return p,times(x[1],invnorm(plus(p,q),2*lo))
def qmax(*a):return I(max(z.hi for z in a))


def one_side(sign,coeff,rate,depth,center):
    # coeff is the declared literal real polynomial multiplying t^(10+i*pi/log2).
    # Use the actual finite OLD/rim distance as well as the intended dyadic material distance.
    ratio=I(15)/44 if sign==-1 else ONE;r0,r1=I('.0749'),I('.2201')
    nominal=(ONE/512)/(2**depth);width=ratio*nominal+I('1e-16')
    # An outward-rounded sampled edge may cross its seam into the adjacent larger mother cell.
    L=2*nominal
    t=width*f64(abs(rate))
    if t.hi>=1:raise ValueError('Selected depth must be inside the same original cut.')
    amp={}
    for d in range(3):
        for j in range(4):
            terms=[]
            for k,row in enumerate(coeff):
                exponent=10+k
                factor=ONE
                for n in range(d):factor*=exponent-n+5
                terms.append(factor*t**(exponent-d)*f64(abs(rate))**d*
                       sum((f64(abs(z))*int(m)**j for m,z in enumerate(row)),ZERO))
            amp[d,j]=hi(sum(terms,ZERO))
    # On all subsequent dyadic cells, L log(1024/L²) and L² decrease.
    w=8*L**3;wp=8*(5*L**2+I(15)/4*B*L*monotone_trans(1024/L**2,'ln'))/ratio
    tilt=I('.271') if sign==-1 else ZERO
    ur=pair((tilt+w,tilt,tilt),tuple(amp[1,j] for j in range(3)))
    urr=pair(vec(wp),tuple(amp[2,j] for j in range(3)))
    up=pair((tilt*r1,)*3,tuple(amp[0,j+1] for j in range(3)))
    E=pair(vec(1+w**2));Ei=pair(vec(ONE));Ep=pair(vec(2*w*wp))
    A2=add(E,product(ur,ur))
    na=(tilt+w+amp[1,0])**2+(tilt+amp[0,1]/r0)**2
    if na.hi>=D('.19'):return dict(available=False,side=sign,reason='positive whole-sector chart not proved',max_slope2=str(na.hi))
    lo=I('.9');sqe=pair(vec(hi(monotone_trans(1+w*w,'sqrt'))))
    A=root(A2,lo)
    s=root(add(pair(vec(ONE)),add(product(product(ur,ur),Ei),product(product(up,up),pair(vec(1/r0**2))))),lo)
    gamma=product(product(Ep,Ei),pair(vec(ONE/2)))
    diff=add(urr,product(ur,gamma))
    Bp=product(product(product(product(sqe,up),diff),pair(vec(ONE/r0))),
               product(inverse(A2,lo**2),inverse(s,lo)))
    ar=product(add(Ep,product(pair(vec(I(2))),product(ur,urr))),inverse(product(pair(vec(I(2))),A),2*lo))
    # Both developments are integrated from the nearest real cap. At that anchor the angle is
    # atan2(sin(phi),cos(theta)cos(phi)), whose first two derivatives have modulus <2 and <3.
    beta=pair((ZERO,2+width*Bp[0][1],3+width*Bp[0][2]),tuple(hi(width*z) for z in Bp[1]))
    p1,p2=beta[0][1:];q1,q2=total(beta)[1:];d0,d1,d2=beta[1]
    P=pair((ONE,p1,p2+p1*p1),(d0,d0*q1+d1,d0*(q2+q1*q1)+d2+(p1+q1)*d1))
    # Vector norms use |e^{ib}−e^{icu}| ≤ |b−cu| for the actual real branch.
    V=product(A,P)
    Urr=add(product(ar,P),product(product(A,Bp),P))
    dp=width*V[1][0]+amp[0,0]
    dR=V[1][0]+amp[1,0];dT=(width*V[1][1]+amp[0,1])/r0
    dRR=Urr[1][0]+amp[2,0];dRT=(V[1][1]+amp[1,1])/r0
    dTT=(width*V[1][2]+amp[0,2])/r0**2
    dg=dR+dT;dn0=I('1.001')*dg+dR*dT
    if max(dg.hi,dn0.hi)>=D('.4'):return dict(available=False,side=sign,reason='material differential envelope too wide')
    dn=2*dn0/(1-dn0)
    # Actual b entries differ from the revolved source by normal and true physical two-jet errors.
    h0=I('4.4');h1=1/r0
    db=qmax(dRR+dn*h0,dTT+dn*h1)+dRT+dn*h1
    k=(h0*I('1.001')**2+db)/(1-dg)**2
    eta=2*I('1.001')*dg+dg*dg
    cx,cz=(f64(center[0]),f64(center[1])) if sign==-1 else (ZERO,ZERO)
    rad=(I('.075')+width if sign==-1 else I('.22'))+I(cx.norm())+dp+width*w
    rz=(I('.075')+width)*tilt+dp+width*w
    low=cz-rz;high=cz+rz;h=-low-I('.045')
    side=rad+(I('2.914') if h.hi>=0 else I('2.9'))*h+I('.18492')
    ok=(3*k).hi<100 and dn.hi<D('.2') and (rad+I('.06')).hi<D('.28499') and side.hi<D('.4215') and low.lo>D('-.075') and high.hi<D('.06')
    return dict(available=bool(ok),side=sign,last_finite_cell_depth=depth,normalized_metric_operator_upper=str(eta.hi),
             principal_curvature_upper=str(k.hi),normal_displacement_upper=str(dn.hi),
             position_perturbation_upper=str(dp.hi),max_radius_upper=str(rad.hi),minimum_z_lower=str(low.lo),
             maximum_z_upper=str(high.hi),side_left_upper=str(side.hi),
             relative_physical_twojet_bounds=[str(z.hi) for z in (dp,dR,dT,dRR,dRT,dTT)],
             includes_all_deeper_dyadic_scales=True,declared_literal_deep_height_coefficients=True)

