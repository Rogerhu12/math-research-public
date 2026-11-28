"""Outward full-angle, all omitted-cell physical estimates for exact Padé coefficients and the same Hermite F."""
from r734_true_dyadic_tail import I,D,ZERO as Z,ONE as O,B,monotone_trans as trans

def fp(x):return I(D.from_float(float(x)))
def exp(x):return trans(x,'exp')
def root(x):return trans(x,'sqrt')

def magnitude(sp,x):
    co=sp.coefficients(x);wave=[0]+[v for j in range(1,sp.K+1) for v in (j,j)];out=[]
    for c in co:
        vals=[fp(max(abs(a) for a in c[:sp.splines,j]))+sum((fp(abs(a)) for a in c[sp.splines:,j]),Z) for j in range(len(wave))]
        out.append([sum((a*int(j)**k for a,j in zip(vals,wave)),Z) for k in (0,1,2)])
    return out

def generator(u,v,base,quot):
    a,b,c=u;d,e,f=v;U=exp(a);G=d+d*d;H=1+2*d
    return (U*(base*G+quot),U*(base*(b*G+e*H)+quot*b),
            U*(base*((c+b*b)*G+2*b*e*H+f*H+2*e*e)+quot*(c+b*b)))

def gains(o,step):
    # Each of the two CF4 right factors uses sum |weights|=sqrt(3)/3 < .578.
    tau=I('.578')*step*o[0];d=1+tau/3
    return I('1.156')*o[0],I('1.156')*d*o[1],I('1.156')*(d*o[2]+I('.578')*step*(O/3+d*d)*o[1]**2)+2*step*(I('.578')*d*o[1])**2

def both(sp,x,r,depth):
    u,v=magnitude(sp,x);gap=max((fp(b)-fp(a)).hi for a,b in zip(r[:-1],r[1:]))
    step=I(gap);G=gains(generator(u,v,I(25),I(24)),step);t=I('.145000000000001')
    R1=1+t*G[1];R2=R1**2+t*G[2]
    return [one(s,depth,u,v,R1,R2,x[:3]) for s in (-1,1)]

def one(side,depth,u,v,R1,R2,C):
    ratio=I(15)/44 if side==-1 else O
    width=ratio/(512*2**depth)+I('1e-16');L=I(2)/(512*2**depth)
    W=8*L**3;V=8*(5*L**2+I(15)/4*B*L*trans(1024/L**2,'ln'))/ratio
    # Here chi is identically 0, kappa=W/m and h'/kappa=-W'/m^2 even on each true turning circle.
    Om=generator(u,v,W/I('.0749'),V);G=gains(Om,width)
    def local(y):return (y[0],y[0]*R1+y[1],y[0]*R2+2*y[1]*R1+y[2])
    Ld=local(G);La=local(Om)
    # For each phi-jet, a cubic Hermite velocity has |V'_h|<=1.5 |delta V|/h + 2 max|A|.
    d=[I('1.5')*(W*V*z+2*g)+2*(W*V*z+2*a) for z,g,a in zip((O,R1,R2),Ld,La)]
    rr=I('.0749');pos=width**2*d[0]/2;dv=width*d[0];dh=width**2*d[1]/(2*rr);mix=width*d[1]/rr;ph=width**2*d[2]/(2*rr**2)
    e=dv+dh;cross=e+dv*dh
    if e.hi>=D('.4') or cross.hi>=D('.4'):return dict(available=False,side=side,reason='Deep Cartesian tangent bound too wide.')
    dn=2*cross/(1-cross);k=(I(max(d[0].hi,(ph+dn/rr).hi))+mix+dn/rr)/(1-e)**2;eta=W*W+2*e+e**2
    if side==-1:
        cx,cy,cz=map(fp,C);off=root(cx**2+cy**2)
    else:cz=off=Z
    rad=(I('.075')+width if side==-1 else I('.22'))+off+pos
    height=((I('.075')+width)*I('.271') if side==-1 else Z)+pos
    lo,hi=cz-height,cz+height;ht=-lo-I('.045');wall=rad+(I('2.914') if ht.hi>=0 else I('2.9'))*ht+I('.18492')
    ok=((3*k).hi<D(100) and dn.hi<D('.2') and (rad+I('.06')).hi<D('.28499') and wall.hi<D('.4215'))
    return dict(available=bool(ok),side=side,principal_curvature_upper=str(k.hi),normalized_metric_operator_upper=str(eta.hi),
       normal_displacement_upper=str(dn.hi),max_radius_upper=str(rad.hi),minimum_z_lower=str(lo.lo),maximum_z_upper=str(hi.hi),
       velocity_radial_angular_0_1_2_upper=[str(v.hi) for v in d],global_P_phi_and_P_phiphi_upper=[str(R1.hi),str(R2.hi)],
       exact_math_discrete_Pade_and_C2_Hermite=True,IEEE_roundoff_or_continuous_central_certificate=False)
