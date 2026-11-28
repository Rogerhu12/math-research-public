"""Exact rational material-piece specification for a smoothed R651 input."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb


def add(p, q):
    return tuple((p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
                 for i in range(max(len(p),len(q))))


def scale(p, a):
    return tuple(a*x for x in p)


def multiply(p, q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,v in enumerate(p):
        for j,w in enumerate(q):
            out[i+j]+=v*w
    return tuple(out)


def compose(p, q):
    out=(F(0),)
    for v in reversed(p):
        out=add(multiply(out,q),(v,))
    while len(out)>1 and out[-1]==0:
        out=out[:-1]
    return out


def derivative(p):
    return tuple(j*p[j] for j in range(1,len(p))) or (F(0),)


def derivative_bound(p):
    # Exact Bernstein convex-hull upper bound on sixteen local pieces.
    d=derivative(p)
    n=len(d)-1
    upper=F(0)
    for j in range(16):
        coefficients=compose(d,(F(j,16),F(1,16)))
        for i in range(n+1):
            value=sum(F(comb(i,k),comb(n,k))*coefficients[k]
                      for k in range(min(i+1,len(coefficients))))
            upper=max(upper,abs(value))
    return upper


@dataclass(frozen=True)
class Piece:
    h: tuple
    k: tuple
    duration: object
    control: object
    h_speed_numerator: F
    k_speed_numerator: F


class PhysicalBase:
    """p is the exact rational parameter object of an R651 candidate."""
    def __init__(self,p,epsilon):
        eps=F(epsilon)
        if not 0<eps<F(1,2):
            raise ValueError("Cubic-edge smoothing requires 0 < epsilon < 1/2")
        self.parameters=p
        self.epsilon=eps
        H,a=F(p["H"]),F(p["a"])
        levels=[2*H*F(y) for y in p["levels"]]
        order=p["order"]
        durations=[F(v) for v in p["durations"]]
        if (len(levels)!=4 or sorted(order)!=list(range(4)) or order[0]!=0 or
                levels[0]!=H or H<=0 or a<=0 or len(durations)!=4):
            raise ValueError("The original four stationary heights and a valid physical first leg are required")
        self.pieces=[]
        self.eta_min=self.eta_max=F(0)
        eta=F(0)
        self.total_k_variation=F(0)
        self.h_min=self.h_max=H
        self.k_min=self.k_max=F(0)
        chi=tuple(map(F,(0,0,0,0,35,-84,70,-20)))
        step=tuple(map(F,(0,0,0,10,-15,6)))
        psi=tuple(map(F,(0,1,0,4,-7,3)))
        def append(h,k,duration,control=None):
            self.pieces.append(Piece(h,k,duration,control,derivative_bound(h),derivative_bound(k)))
        def moving(h0,h1,k0,k1,T,center=False):
            nonlocal eta
            if T<=0 or (h1!=h0 and k1!=k0):
                raise ValueError("A moving physical segment must be positive and axis-aligned")
            if k1!=k0:
                eta+=(k1-k0)/(2*h0)
            self.eta_min=min(self.eta_min,eta)
            self.eta_max=max(self.eta_max,eta)
            self.total_k_variation+=abs(k1-k0)
            self.h_min=min(self.h_min,h0,h1)
            self.h_max=max(self.h_max,h0,h1)
            self.k_min=min(self.k_min,k0,k1)
            self.k_max=max(self.k_max,k0,k1)
            profile=psi if center else step
            pieces=[(F(0),1-eps,"none"),(1-eps,F(1),"right")] if center else [
                (F(0),eps,"left"),(eps,1-eps,"none"),(1-eps,F(1),"right")]
            for lo,hi,side in pieces:
                z=compose(profile,(lo,hi-lo))
                if side=="left":
                    z=multiply(z,chi)
                elif side=="right":
                    back=compose(chi,(F(1),F(-1)))
                    z=add((F(1),),multiply(add(z,(F(-1),)),back))
                hp=add((h0,),scale(z,h1-h0))
                kp=add((k0,),scale(z,k1-k0))
                append(hp,kp,T*(hi-lo))
        moving(H,H,F(0),-a,durations[0],True)
        for j,index in enumerate(order):
            h=levels[index]
            extra=p.get("excursion")
            if extra is not None and extra["level"]==index:
                other,T,hold=F(extra["other_k"]),F(extra["leg_duration"]),F(extra["hold"])
                if hold<0:
                    raise ValueError("A fixed physical dwell cannot have negative duration")
                moving(h,h,-a,other,T)
                if hold>0:
                    append((h,),(other,),hold)
                moving(h,h,other,-a,T)
            append((h,),(-a,),None,index)
            if j<3:
                moving(h,levels[order[j+1]],-a,-a,durations[j+1])

    def physical_enclosure(self,q,taus):
        q=[F(float(v)) for v in q]
        tau=[F(float(v)) for v in taus]
        if len(q)!=256 or len(tau)!=4 or min(tau)<=0:
            raise ValueError("256 shape coordinates and four positive physical durations are required")
        times=[t.duration if t.control is None else tau[t.control] for t in self.pieces]
        length=sum(times)
        hs=[F(1,1+j*j) for j in range(129)]
        ks=[F(1,1+(2*j+1)**2) for j in range(127)]
        pi_upper=F(22,7)
        f=sum(abs(v)*s for v,s in zip(q[:129],hs))
        g=sum(abs(v)*s for v,s in zip(q[129:],ks))
        fx=sum(abs(v)*s*j*pi_upper for j,(v,s) in enumerate(zip(q[:129],hs)))
        gx=sum(abs(v)*s*(2*j+1)*pi_upper/2 for j,(v,s) in enumerate(zip(q[129:],ks)))
        minimum=self.h_min-f
        if minimum<=0:
            return {"sufficient_bounds_closed":False,"reason":"positive_height_lower_enclosure_unclosed"}
        error=gx/(2*minimum)+f*self.total_k_variation/(2*self.h_min*minimum)
        values={"min_h":minimum,"max_h":self.h_max+f,
            "abs_k":max(abs(self.k_min),abs(self.k_max))+g,
            "abs_eta":max(abs(self.eta_min),abs(self.eta_max))+error,
            "abs_gamma":max(t.h_speed_numerator/T for t,T in zip(self.pieces,times))+fx/length,
            "abs_upsilon":max(t.k_speed_numerator/T for t,T in zip(self.pieces,times))+gx/length,
            "physical_length":length}
        closed=(values["min_h"]>F(4,5) and values["max_h"]<3 and values["abs_k"]<2
                and values["abs_eta"]<1 and values["abs_gamma"]<6 and values["abs_upsilon"]<6
                and F(21,10)<=length<=F(79,10))
        return {"sufficient_bounds_closed":closed,"exact_rational_bounds":{k:str(v) for k,v in values.items()},
                "failure_of_sufficient_bounds_is_not_a_point_violation":True}
