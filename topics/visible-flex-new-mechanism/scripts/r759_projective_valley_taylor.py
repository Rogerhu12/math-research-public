"""Outward true R745 material Taylor transfer, parameter derivative and projective cones."""
from fractions import Fraction as F
from flint import arb
from r689_continuous_native_field_balls_20261128 import Jet, pack_ball, unball

H=F('.56'); RAMP=F('.018'); TOP=F('.006'); EPS=F('.0002')
START=tuple(map(F,('.081','.124','.167')))
MID=tuple(map(F,('.102','.145','.188')))
RIM={-1:F('.075'),1:F('.22')}; RHO={-1:F(15,44),1:F(1)}; EDGE={-1:F(1,64),1:F(1,128)}
CUT={s:RIM[s]-s*RHO[s]*EDGE[s] for s in RIM}
PARAM_SCALE=F(1,100)

def a(x):return arb(str(x)) if not isinstance(x,arb) else x

def cover(low,high):return unball((str(low),str(high)))

def endpoints(v):return (v.lower(),v.upper())

def union(values):
    if not all(t.is_finite() for t in values):raise ArithmeticError('Nonfinite projective image.')
    return unball((str(min(t.lower() for t in values).fmpq()),str(max(t.upper() for t in values).fmpq())))

def knots(s):
    q={*CUT.values(),CUT[-1]+EPS,CUT[1]-EPS,*MID}
    for start in START:
        for c in (start,start+RAMP,start+RAMP+TOP,start+2*RAMP+TOP):q.update((c-EPS,c+EPS))
    return sorted((p for p in q if s*(p-MID[1])>=0),reverse=s==1)

def ramp(x,pick):
    if pick<=-EPS:return Jet.cast(0)
    if pick>=EPS:return x
    t=(x+EPS)/(2*EPS)
    return 280*EPS*t**5*(F(1,20)+t*(-F(1,10)+t*(F(1,14)-t/56)))

def height(r,pick):
    for start in START:
        if start-EPS<pick<start+2*RAMP+TOP+EPS:
            u=pick-start; x=r-start
            if u>RAMP+TOP/2:u=2*RAMP+TOP-u;x=2*RAMP+TOP-x
            if u>=RAMP+EPS:return Jet.cast(H)
            return (ramp(x,u)-ramp(x-RAMP,u-RAMP))*(H/RAMP)
    return Jet.cast(0)

def slope(r,pick,v):
    h=height(r,pick); variable=MID[0]<pick<MID[2]
    if variable:val=Jet.cast(v)
    else:
        s=-1 if pick<MID[0] else 1
        edge=RHO[s]*EDGE[s]; loc=(-s*(pick-RIM[s])-edge)/EPS
        if loc<0:y=Jet.cast(edge)
        elif loc>1:y=Jet.cast(edge+EPS/2)
        else:
            t=(-s*(r-RIM[s])-edge)/EPS
            y=edge+EPS*(t-t**4*(F(5,2)-3*t+t*t))
        w=(y/RHO[s])**4/2;val=w/(1+w*w).sqrt()
    b=val+(1-val/H)*h; root=(1-b*b).sqrt();w=b/root
    if not w.c[0]>0:raise ArithmeticError('Radial range needs subdivision.')
    dw=(1-h/H)*PARAM_SCALE/(root**3) if variable else Jet.cast(0)
    return w,dw

def mm(a,b):return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])

def plus(a,b):return tuple(x+y for x,y in zip(a,b))

def dmul(a,b):return mm(a[0],b[0]),plus(mm(a[1],b[0]),mm(a[0],b[1]))

def block_norm(z):
    a,d=z
    return max((abs(a[i])+abs(a[i+1])+abs(d[i])+abs(d[i+1])).upper() for i in (0,2))

def identity():return ((a(1),a(0),a(0),a(1)),(a(0),)*4)

def gen(r,h,pick,scale,j,v):
    w,dw=slope(r,pick,v);k=j*j
    z=h/r
    aa=[k*z,z*scale/w,-k*(k-1)*z*w/scale,(1-k)*z]
    dd=[Jet.cast(0),-z*scale*dw/(w*w),-k*(k-1)*z*dw/scale,Jet.cast(0)]
    return [(tuple(q.c[i] for q in aa),tuple(q.c[i] for q in dd)) for i in range(Jet.order+1)]

def sweep(g,n,terminal):
    entries=[identity()]
    for i in range(1,n+1):
        v=dmul(g[0],entries[i-1]);v=[list(block) for block in v]
        for k in range(1,i):
            t=dmul(g[k],entries[i-k-1]);v=[[x+y for x,y in zip(b,c)] for b,c in zip(v,t)]
        entries.append(tuple(tuple(x/i for x in b) for b in v))
    if terminal:return entries[-1]
    return tuple(tuple(sum((z[p][k] for z in entries),a(0)) for k in range(4)) for p in range(2))

def transfer(left,right,j,v,order,truncation):
    """Local scaled coordinates (f,y/scale); remainder controls the entire dual 4x4 operator."""
    pick=(left+right)/2;h=right-left
    Jet.order=0
    try:
        w,_=slope(Jet.cast(pick),pick,v.mid());scale=w.c[0].mid()
        radial=Jet([cover(min(left,right),max(left,right))]); w0,dw=slope(radial,pick,v)
        # Reject singular interval ranges before taking derivatives.
        if not w0.c[0].is_finite() or not scale>0:return None
        z=gen(radial,h,pick,scale,j,v)[0]; size=block_norm(z)
        if not size < a('0.65'):return None
        Jet.order=order
        whole=gen(Jet([radial.c[0],a(h)]),h,pick,scale,j,v)
        last=sweep(whole,order+1,True);err=(block_norm(last)*size.exp()).upper()
        if not err< a(truncation):return None
        local=gen(Jet([a(left),a(h)]),h,pick,scale,j,v)
        total=sweep(local,order,False);rad=arb(0,err)
        return scale,tuple(x+rad for x in total[0]),tuple(x+rad for x in total[1]) if MID[0]<pick<MID[2] else (a(0),)*4,err,a(right/left)
    except (ArithmeticError,ValueError,ZeroDivisionError):return None
    finally:Jet.order=0

def send_cone(state,step):
    """state = [dominant axis,physical scale,slope,scaled valley derivative]."""
    oldaxis,oldscale,z,dz=state;scale,M,N,_,true_det=step
    # Input coordinates always have physical y divided by the chart scale.
    factor=oldscale/scale if oldaxis==0 else scale/oldscale
    z=z*factor; dz=dz*factor
    starts=endpoints(z)
    def component(C,row,t):return C[2*row+oldaxis]+C[2*row+1-oldaxis]*t
    candidates=[]
    for axis in (0,1):
        den=component(M,axis,z)
        if not den.contains(0):candidates.append((abs(den).lower(),axis,den))
    if not candidates:raise ArithmeticError('Both candidate projective denominators meet zero.')
    _,axis,den=max(candidates,key=lambda q:q[0]);other=1-axis
    # The true det is positive, hence each given transfer maps a connected
    # slope interval monotonically; evaluating both endpoints avoids ball wrapping.
    out=union([component(M,other,t)/component(M,axis,t) for t in starts])
    # The scaled physical fundamental matrix has trace 1/r in this cell.
    determinant=true_det * (1 if oldaxis==axis else -1)
    d=(component(N,other,z)-out*component(N,axis,z))/den+determinant*dz/(den**2)
    if not all(t.is_finite() for t in (out,d)):raise ArithmeticError('Nonfinite derivative of projective image.')
    return axis,scale,out,d

def align(state,axis,scale):
    oldaxis,oldscale,z,d=state
    factor=oldscale/scale if oldaxis==0 else scale/oldscale; z=z*factor;d=d*factor
    if oldaxis==axis:return z,d/a(PARAM_SCALE)
    if z.contains(0):raise ArithmeticError('No common projective chart at the matching summit.')
    return 1/z,-d/(a(PARAM_SCALE)*z**2)
