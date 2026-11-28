"""R762 regular high-order zero circles and their exact angular velocity; public Actions."""
import numpy as np
from r758_material_jet_and_angles import J,sine,cosine,root

K=np.sqrt(2/3)
SOURCE_SLOPE=1.e-8
SOURCE_M=np.sqrt(1+SOURCE_SLOPE**2)
SOURCE_MU=SOURCE_SLOPE**2/(SOURCE_M*(1+SOURCE_M))
REG_SCALE=5.e-4*SOURCE_SLOPE


class Two:
    """Independent angle derivatives, over the underlying full material Taylor algebra."""
    def __init__(self,x,d=0.,dd=0.):
        self.x,self.d,self.dd=x,d,dd
    @staticmethod
    def wrap(v):
        return v if isinstance(v,Two) else Two(v)
    def __add__(self,other):
        o=self.wrap(other)
        return Two(self.x+o.x,self.d+o.d,self.dd+o.dd)
    __radd__=__add__
    def __neg__(self):
        return Two(-self.x,-self.d,-self.dd)
    def __sub__(self,o):return self+(-self.wrap(o))
    def __rsub__(self,o):return self.wrap(o)+(-self)
    def __mul__(self,other):
        o=self.wrap(other)
        return Two(self.x*o.x,self.d*o.x+self.x*o.d,
                   self.dd*o.x+2*self.d*o.d+self.x*o.dd)
    __rmul__=__mul__
    def __truediv__(self,other):
        o=self.wrap(other)
        v=self.x/o.x
        d=(self.d-v*o.d)/o.x
        return Two(v,d,(self.dd-2*d*o.d-v*o.dd)/o.x)
    def __rtruediv__(self,o):return self.wrap(o)/self


def sin(t):
    if not isinstance(t,Two):return sine(t)
    a,b=sine(t.x),cosine(t.x)
    return Two(a,b*t.d,b*t.dd-a*t.d*t.d)


def cos(t):
    if not isinstance(t,Two):return cosine(t)
    a,b=cosine(t.x),sine(t.x)
    return Two(a,-b*t.d,-b*t.dd-a*t.d*t.d)


def sqrt_two(v):
    z=root(v.x)
    d=v.d/(2*z)
    return Two(z,d,(v.dd-2*d*d)/(2*z))


def shapes(t):
    sn,cs=sin(t),cos(t)
    s2,c2=sin(2*t),cos(2*t)
    s3,c3=sin(3*t),cos(3*t)
    s4,c4=sin(4*t),cos(4*t)
    b=1+K*c2-(1+K)*cs
    bp=-2*K*s2+(1+K)*sn
    bs=1-3*K*c2
    v=.5*s3-1.5*sn
    vp=1.5*(c3-cs)
    vs=-4*s3
    bb=-K*s2-.25*s4+(1+K)*(-1+1.5*K)*sn+.5*K*(1+K)*s3
    def primitive_sine(n,c):return (1-c)/n
    p1,p2,p3,p4,p5=(primitive_sine(n,c) for n,c in (
        (1,cs),(2,c2),(3,c3),(4,c4),(5,cos(5*t))))
    bv=-4*p3-2*K*(p5+p1)+2*(1+K)*(p4+p2)
    vb=(.5+2.25*K)*p3-(1.5+3*K)*p1-.75*K*p5
    vv=sin(6*t)/6+1.5*s2-.75*s4
    return sn,cs,b,bp,bs,v,vp,vs,bb,bv,vb,vv


def coefficient(r,mu,phase):
    """Signed material needs the plus square root only on this positive-slope component."""
    region=(r>=.0848)&(r<=.2102)
    ramp=region&(mu.value.real>SOURCE_MU/2)&(mu.value.real<SOURCE_MU)
    core=region&(mu.value.real<=SOURCE_MU/2)
    u=(2*mu/SOURCE_MU-1).at(ramp,0.)
    # Symmetric degree-nine step. The endpoints carry four flat derivatives.
    S=u**5*(126+u*(-420+u*(540+u*(-315+70*u))))
    dS=630*u**4*(1-u)**4
    raw=J(1.).at(core,(1-S).at(ramp,0.))
    gain=REG_SCALE*phase
    return gain*raw,(-2*gain*dS/SOURCE_MU).at(ramp,0.),region,gain


def velocity(t,ratio,gain):
    """Return -P.N_t/(T.N_t) and its first two native angle derivatives."""
    vals=shapes(Two(t,1.,0.))
    _,_,b,bp,bs,v,vp,vs,bb,bv,vb,vv=vals
    u=1-ratio*bp-vp
    l=ratio*b+v
    f=ratio*bs+vs
    sq=gain*gain
    lam=sqrt_two(1-sq*(u*u+l*l)/4)
    along=-u*f+l
    vx=-lam*f+sq*u*along/(4*lam)
    vy=lam+sq*l*along/(4*lam)
    rot=sq*(-l+ratio*ratio*bb+ratio*(bv+vb)+vv)/2
    c,s=cos(rot),sin(rot)
    result=-(vx*c+vy*s)/(vy*c-vx*s)
    return result.x,result.d,result.dd
