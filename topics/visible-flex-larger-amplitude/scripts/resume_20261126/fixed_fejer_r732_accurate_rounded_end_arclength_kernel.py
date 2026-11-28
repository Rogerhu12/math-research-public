#!/usr/bin/env python3
"""R732 accurate rounded end, central length equation and full material reference.

This independent kernel encloses the accurate mathematical functions on entire
angular/material intervals. It does not replay a working root, quadrature or
normal solve. The five terminal pieces use their actual backward coordinate; a
crossing query returns every active one-sided box and its componentwise hull.
The original outward Interval implementation is reused by whole
source identity; its legacy CLI and mean hypotheses are not used.

Every numerical operation below is executed only by public repository Actions.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path

SCHEMA = "complete-R732-accurate-polynomial-length-arclength-kernel-v1"
ARITHMETIC_SOURCE_SHA256 = "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"
WORKING_LENGTH_SOURCE_SHA256 = "032b6c68570c75a849daa2a5a335a9546cf31e1c3c0ad8a7ee4eb0dee3cb0420"
REFERENCE_SOURCE_SHA256 = "831447a2d50b54029abcf6cd6d441bca7239771b1fd405463db55e1da7646116"
THEOREM_NAME = "R732-rounded-cap-exact-terminal-metric-and-full-reference.md"
THEOREM_BYTES = 16954
THEOREM_SHA256 = "02db235b89acd0d950f91fc798b72792d843b096393dc9cf42f451556b5d4ec8"
TAIL_PROOF_BYTES = 10831
TAIL_PROOF_SHA256 = "143ccaf9af8596c1803fc23de7691fa1dea36ec042d86ffafa2cc010b3f0252e"
HANDLE_LENGTH = "1/512"
MAXIMUM_CONTRACTION = "3/4"
PULSE_FLATNESS = 6
BASELINE_LENGTH_UPPER = "99/50"
RIGHT_LENGTH_LOWER = "41/20"
DESIGN_COEFFICIENTS = ("7/16","-3/40","3/112","-1/84","1/176","-3/1144","1/1040")
PARTIAL_KEYS = ("L","L_xi","L_xixi","L_phi","L_xiphi","L_phiphi")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Complete accurate R732 arithmetic requires public Actions")


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def encode(value):
    if isinstance(value,F):return str(value)
    if hasattr(value,"json") and callable(value.json):return value.json()
    if isinstance(value,dict):return {str(k):encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [encode(v) for v in value]
    if value is None or type(value) in (bool,int,str):return value
    raise TypeError("Accurate R732 evidence contains exact rational/interval data only")


def file_record(path):
    p=Path(path).resolve()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))


def _fraction(value):
    if type(value) is bool or type(value) is float:
        raise TypeError("Decode a finite binary word explicitly before exact arithmetic")
    return F(value)


def _power_two(exponent):
    return F(1<<exponent,1) if exponent>=0 else F(1,1<<(-exponent))


def round_binary64_exact(value):
    """Exact nearest/even normal binary64 rational; these seven inputs are normal."""
    q=_fraction(value)
    if q==0:return F(0)
    sign=-1 if q<0 else 1;q=abs(q)
    exponent=q.numerator.bit_length()-q.denominator.bit_length()
    if q<_power_two(exponent):exponent-=1
    if not -1022<=exponent<=1023:
        raise ValueError("Only the declared finite normal design coefficients are used")
    unit=_power_two(exponent-52)
    scaled=q/unit;n,r=divmod(scaled.numerator,scaled.denominator)
    twice=2*r
    if twice>scaled.denominator or (twice==scaled.denominator and n%2):n+=1
    return sign*n*unit


class LengthEnclosureUnavailable(ArithmeticError):
    pass


def definition():
    return dict(schema=SCHEMA,arithmetic_source_sha256=ARITHMETIC_SOURCE_SHA256,
        actual_reference_source_sha256=REFERENCE_SOURCE_SHA256,
        working_length_source_sha256=WORKING_LENGTH_SOURCE_SHA256,
        theorem=dict(name=THEOREM_NAME,bytes=THEOREM_BYTES,sha256=THEOREM_SHA256),
        eta=HANDLE_LENGTH,xi_max=MAXIMUM_CONTRACTION,pulse_flatness=PULSE_FLATNESS,
        psi="(1-(2*t-1)^12)^7",
        complete_polynomial_degree=89,
        exact_length_equation="L_c(xi,phi)=integral_0^1 |G_t| dt = S-L_end",
        rounded_terminal="R732 (2)-(7) exact backward material position and tangent",
        terminal_deep_definition="R690 (3),(6) through 2b and R732 (4) blend",
        tail_proof=dict(bytes=TAIL_PROOF_BYTES,sha256=TAIL_PROOF_SHA256),
        original_material_domain="0<=s<=S",
        exact_inverse_equation="ell(t,phi)=integral_0^t |G_u| du = s",
        complete_implicit_angle_order=2,complete_material_t_derivative_order=3,
        global_root_residual_bound="|xi-xi*| <= |L_c(xi)-C| / ((Clo-L0plus)/(3/4)), C=S-L_end",
        root_derivative_bound_applies_to_true_root=True,
        derivative_bound_not_asserted_on_every_point_of_a_coarse_axis_box=True,
        polynomial_arithmetic="exact rational power coefficients and centered derivative ranges",
        integral_arithmetic="even Taylor polynomial plus full interval derivative remainder",
        original_working_Gauss_values_or_discrete_AD_used_as_exact=False,
        old_R709_R722_R726_R727_mean_certificates_inherited=False)


def _add_poly(a,b):
    n=max(len(a),len(b))
    return [(a[j] if j<len(a) else F(0))+(b[j] if j<len(b) else F(0)) for j in range(n)]


def _scale_poly(a,c):
    return [v*c for v in a]


def _multiply_poly(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def _bernstein_power(values):
    n=len(values)-1;out=[F(0)]*(n+1)
    for i,value in enumerate(values):
        for j in range(i,n+1):
            out[j]+=value*math.comb(n,i)*math.comb(n-i,j-i)*((-1)**(j-i))
    return out


def _translate(poly,centre):
    """Exact coefficients of p(centre+x), no interval cancellation at this step."""
    out=[F(0)]
    for value in reversed(poly):
        new=[F(0)]*(len(out)+1)
        for i,coefficient in enumerate(out):
            new[i]+=centre*coefficient;new[i+1]+=coefficient
        new[0]+=value;out=new
    while len(out)>1 and out[-1]==0:out.pop()
    return out


def _polynomial_derivative_coefficients(poly,left,right,order,I,bits):
    """All p^(j)(t)/j! on the complete closed t interval."""
    centre=(left+right)/2;radius=(right-left)/2
    shifted=_translate(poly,centre);out=[]
    for j in range(order+1):
        if j>=len(shifted):
            out.append(I(0,0,bits));continue
        lo=hi=shifted[j]
        for k in range(j+1,len(shifted)):
            coefficient=math.comb(k,j)*shifted[k]
            magnitude=coefficient*radius**(k-j)
            if (k-j)%2:
                lo-=abs(magnitude);hi+=abs(magnitude)
            else:
                lo+=min(F(0),magnitude);hi+=max(F(0),magnitude)
        out.append(I(lo,hi,bits))
    return out



class AccurateRoundedEnd:
    """Enclose the five pieces at true backward material distance on the closed end."""

    b = F(1, 1000)
    d = F(7, 50)
    height = F(13, 50)
    trig_degree = 16
    smooth = (0, 0, 0, 10, -15, 6)
    integrated_smooth = (0, 0, 0, 0, F(5, 2), -3, 1)
    pieces = ("deep", "blend", "constant", "ease", "vertical")

    def __init__(self, polynomial, width, kappa, proof_path):
        self.p = polynomial
        self.width, self.kappa = _fraction(width), _fraction(kappa)
        if self.width != F(5764607523034235, 288230376151711744) or self.kappa != F(3, 2):
            raise ValueError("Use the actual binary FullHold out width and fixed curvature")
        if 2*self.b > self.width/8:
            raise ValueError("The two initial pieces must be inside the original pure deep tail")
        self.tail_proof = file_record(proof_path)
        if (self.tail_proof["bytes"] != TAIL_PROOF_BYTES
                or self.tail_proof["sha256"] != TAIL_PROOF_SHA256):
            raise ValueError("Use the complete R690 tail proof and its actual formulas")
        self.zero, self.one = polynomial.point(0), polynomial.point(1)
        self.M, _ = self.deep_bounds(2*self.b)
        self.A = polynomial.point(self.b/(2*self.d)) + self.box(0, self.M)
        self.pi = polynomial.k.pi_bounds(polynomial.bits)
        self.uc = 2*self.b + self.d*(self.pi/2-self.A)-self.b/2
        self.uf = self.uc+self.b
        self.end_angle = self.pi/2-self.b/(2*self.d)
        self.angle_polys = {
            "blend": _scale_poly(self.integrated_smooth, self.b/self.d),
            "ease": _scale_poly(_add_poly((F(1,2),-1), self.integrated_smooth), self.b/self.d)}
        self.trig_primitives = {}
        for branch, coefficients in self.angle_polys.items():
            for sine in (False, True):
                poly, power = [F(0)], [F(1)]
                for j in range(self.trig_degree+1):
                    if j % 2 == int(sine):
                        term = F((-1)**(j//2), math.factorial(j))
                        poly = _add_poly(poly, _scale_poly(power, term))
                    power = _multiply_poly(power, coefficients)
                self.trig_primitives[branch,sine] = [F(0)] + [
                    q/(j+1) for j,q in enumerate(poly)]
        xb, hb = self.deep_position(polynomial.point(self.b))
        self.xb, self.hb = xb, hb
        self.x2, self.h2 = self.blend_position(self.one)
        sn, cs = polynomial.trig(self.end_angle)
        self.xc, self.hc = self.constant_position(sn, cs)
        self.xf, self.hf = self.ease_position(self.one)
        # Independent R732 (5)-(7) bounds hold for the entire exact end.
        self.xf = self.xf.intersect(self.d, self.d+5*self.b/2)
        self.hf = self.hf.intersect(self.d, self.d+5*self.b/2)
        self.L = self.uf+self.height-self.hf
        self.Rv = polynomial.R+self.xf
        self.Z = polynomial.H0-self.height
        if (not F(33,100)<self.L.lo<=self.L.hi<F(35,100)
                or not F(281,400)<self.Rv.lo<=self.Rv.hi<F(713,1000)):
            raise LengthEnclosureUnavailable("The actual end scalar enclosures are too wide")
        self.boundaries = [self.zero, polynomial.point(self.b),
            polynomial.point(2*self.b), self.uc, self.uf, self.L]
        self.counts = {piece:0 for piece in self.pieces}

    def box(self, left, right):
        return self.p.I(left,right,self.p.bits)

    def deep_bounds(self, hi):
        """Whole R690 (3),(6) envelope, including every turn down to u=0."""
        if hi==0:return F(0), F(0)
        # Enlarge the interval before applying monotonicity to each power.
        Y = min(F(32), self.width/hi)
        if Y<4:raise ValueError("The R690 decreasing Gaussian envelope needs Y>=4")
        exponent=Y*Y
        weight=F(3,8)**(exponent.numerator//exponent.denominator)
        return (self.kappa*self.width*weight,
            self.kappa*weight*(2*Y**3+8*Y**5+4*Y**9))

    def deep_position(self, u):
        M,_ = self.deep_bounds(u.hi)
        return u*self.box(1-M*M/2,1), u*self.box(0,M)

    @staticmethod
    def value(poly, x):
        value=F(0)
        for q in reversed(poly):value=value*x+q
        return value

    def monotone_polynomial(self, poly, v, increasing):
        left=self.value(poly,v.lo);right=self.value(poly,v.hi)
        return self.box(left,right) if increasing else self.box(right,left)

    def unit_v(self, v):
        return v.intersect(0,1)

    def primitive(self, branch, sine, v):
        """Integral in v of the exact ideal trigonometric function, including its Taylor remainder."""
        coefficients=self.trig_primitives[branch,sine]
        bound=(self.b/(2*self.d))**(self.trig_degree+1)/math.factorial(self.trig_degree+1)
        # Sine and cosine are nonnegative over this entire polynomial angle range.
        left=self.value(coefficients,v.lo)-v.lo*bound
        right=self.value(coefficients,v.hi)+v.hi*bound
        return self.box(max(F(0),left),min(v.hi,right))

    def blend_position(self,v):
        # R732 (4) integrated by parts: 0<=alpha-alpha0<=M at every v.
        shift=self.box(-self.M*v.hi,self.M*v.hi)
        return (self.xb+self.b*(self.primitive("blend",False,v)+shift),
                self.hb+self.b*(self.primitive("blend",True,v)+shift))

    def constant_position(self,sine,cosine):
        sa,ca=self.p.trig(self.A)
        return self.x2+self.d*(sine-sa),self.h2+self.d*(ca-cosine)

    def ease_position(self,v):
        # delta=pi/2-alpha, so cos(alpha)=sin(delta), sin(alpha)=cos(delta).
        return (self.xc+self.b*self.primitive("ease",True,v),
                self.hc+self.b*self.primitive("ease",False,v))

    def fields(self, branch, u):
        self.p.check()
        if branch=="deep":
            x,h=self.deep_position(u)
            M,P=self.deep_bounds(u.hi)
            alpha=self.box(0,M)
            curvature=self.box(-P,P)
            sine,cosine=self.p.trig(alpha)
        elif branch=="blend":
            v=self.unit_v((u-self.b)/self.b)
            chi=self.monotone_polynomial(self.smooth,v,True)
            ideal=self.monotone_polynomial(self.angle_polys["blend"],v,True)
            M,P=self.deep_bounds(min(2*self.b,u.hi))
            alpha=ideal+self.box(0,M)
            curvature=(1-chi)*self.box(-P,P)+chi/self.d
            sine,cosine=self.p.trig(alpha)
            x,h=self.blend_position(v)
        elif branch=="constant":
            alpha=self.A+(u-2*self.b)/self.d
            sine,cosine=self.p.trig(alpha)
            curvature=self.p.point(1/self.d)
            x,h=self.constant_position(sine,cosine)
        elif branch=="ease":
            v=self.unit_v((u-self.uc)/self.b)
            delta=self.monotone_polynomial(self.angle_polys["ease"],v,False)
            alpha=self.pi/2-delta
            cosine,sine=self.p.trig(delta)
            curvature=(1-self.monotone_polynomial(self.smooth,v,True))/self.d
            x,h=self.ease_position(v)
        elif branch=="vertical":
            alpha=self.pi/2
            cosine,sine,curvature=self.zero,self.one,self.zero
            x,h=self.xf,self.hf+u-self.uf
        else:
            raise ValueError("Unknown rounded end piece")
        self.counts[branch]+=1
        return dict(u=u,alpha=alpha,curvature=curvature,cosine=cosine.intersect(0,1),
            sine=sine.intersect(0,1),x=x,h=h)

    def boxes(self, chart, u):
        rows=[]
        k=self.p.k
        e,e1,e2=chart["e"]
        ez=[self.zero,self.zero,self.one]
        for index, branch in enumerate(self.pieces):
            lower,upper=self.boundaries[index:index+2]
            a,b=max(u.lo,lower.lo),min(u.hi,upper.hi)
            if a>b:continue
            f=self.fields(branch,self.box(a,b))
            c,s,curv=f["cosine"],f["sine"],f["curvature"]
            r=self.p.R+f["x"]
            z=self.p.H0-f["h"]
            T=k.vadd(k.vscale(e,-c),k.vscale(ez,s))
            Ts=k.vadd(k.vscale(e,-curv*s),k.vscale(ez,-curv*c))
            Tphi=k.vscale(e1,-c)
            rows.append(dict(branch=branch,backward_scalar_bounds=f,
                T0=T,T0_s=Ts,T0_phi=Tphi,T0_phiphi=k.vscale(e2,-c),
                exact_reference_primitive_sixjets=dict(
                    F=k.vadd(k.vscale(e,r),k.vscale(ez,z)),Fs=T,Fss=Ts,
                    Fphi=k.vscale(e1,r),Fsphi=Tphi,Fphiphi=k.vscale(e2,r))))
        return rows

    def metadata(self):
        return dict(tail_proof=self.tail_proof,actual_binary_width=str(self.width),
            actual_tail_kappa=str(self.kappa),b=str(self.b),d=str(self.d),
            relative_height=str(self.height),original_pure_exponential_interval=["0",str(2*self.b)],
            whole_deep_angle_upper=str(self.M),A=self.A,uc=self.uc,uf=self.uf,
            xf=self.xf,hf=self.hf,L=self.L,Rv=self.Rv,Z=str(self.Z),
            material_boundaries=self.boundaries,ordered_piece_names=list(self.pieces),
            ideal_trig_primitive_Taylor_degree=self.trig_degree,
            actual_deep_turns_truncated=False,
            exact_Gram_reference_only_material_interval=["0",str(self.b)])

class ExactR732Polynomials:
    """Complete degree-89 G and its xi/phi/t derivatives, without sampling."""

    def __init__(self,arithmetic_module,*,core_coefficients,S,R,H0,kappa0,
                 proof_path,tail_proof_path,tail_width,tail_kappa,bits=192,budget_check=None):
        require_actions()
        k=arithmetic_module
        if sha(k.__file__)!=ARITHMETIC_SOURCE_SHA256:
            raise ValueError("Use the complete original exact outward arithmetic source")
        if type(bits) is not int or not 64<=bits<=1024:
            raise ValueError("Keep the complete declared outward precision")
        self.k,self.I,self.bits=k,k.Interval,bits
        self.check=(lambda **kwargs:None) if budget_check is None else budget_check
        self.S,self.R=self.box(S),self.box(R)
        self.H0,self.kappa0=_fraction(H0),_fraction(kappa0)
        self.core=tuple(_fraction(v) for v in core_coefficients)
        expected=tuple(round_binary64_exact(F(q)) for q in DESIGN_COEFFICIENTS)+(F(0),)*153
        if self.core!=expected:
            raise ValueError("R732 uses all 160 exact source-defined fixed Fejer coefficients")
        if (not F(237,100)<self.S.lo<=self.S.hi<F(119,50)
                or not F(9,16)<self.R.lo<=self.R.hi<F(57,100)
                or not F(97,50)<self.H0<F(39,20)
                or not 0<self.kappa0<F(1,4)):
            raise LengthEnclosureUnavailable("The complete actual R732 scalar/height hypothesis is unpaid")
        self.proof=file_record(proof_path)
        if self.proof["bytes"]!=THEOREM_BYTES or self.proof["sha256"]!=THEOREM_SHA256:
            raise ValueError("Read the complete published R732 proof bytes")
        self.eta=F(HANDLE_LENGTH);self.xi_max=F(MAXIMUM_CONTRACTION)
        self.gamma=F(5,4)*self.kappa0*self.eta**2
        self.L0plus=F(BASELINE_LENGTH_UPPER);self.Lrightminus=F(RIGHT_LENGTH_LOWER)
        self.end=AccurateRoundedEnd(self,tail_width,tail_kappa,tail_proof_path)
        self.C=self.S-self.end.L
        self.gap=self.C.lo-self.L0plus
        if self.gap<=0 or self.Lrightminus<=self.C.hi:
            raise LengthEnclosureUnavailable("Both complete R732 length endpoint margins are required")
        self.root_slope_lower=self.gap/self.xi_max
        self.polynomials={}
        controls=dict(A=(1,1,1,0,0,0),B=(0,0,0,1,1,1),
            D=(0,0,1,0,0,0),Z=(0,1,2,-2,-1,0))
        for name,values in controls.items():
            self.polynomials[name]=_bernstein_power([F(v) for v in values])
        # 1-(2t-1)^12 has exact degree-12 Bernstein coefficients 0,2,0,2,...,0.
        pulse_base=_bernstein_power([F(0 if j%2==0 else 2) for j in range(13)])
        pulse=[F(1)]
        for _ in range(7):pulse=_multiply_poly(pulse,pulse_base)
        self.polynomials["psi"]=pulse
        for name in ("A","B","D"):
            self.polynomials["psi_"+name]=_multiply_poly(pulse,self.polynomials[name])
        self.instantiation=dict(schema=SCHEMA+"-complete-theorem-instantiation",
            definition=definition(),precision_bits=self.bits,complete_fixed_core_coefficients=[str(v) for v in self.core],
            accurate_S=self.S,accurate_R=self.R,exact_fixed_seed_H0=str(self.H0),
            accurate_central_length=self.C,accurate_terminal=self.end.metadata(),
            exact_kappa0=str(self.kappa0),eta=str(self.eta),xi_max=str(self.xi_max),
            L0_upper=str(self.L0plus),L_ximax_lower=str(self.Lrightminus),
            exact_positive_length_gap=str(self.gap),
            exact_true_root_Lxi_lower=str(self.root_slope_lower),
            proof_record=self.proof,whole_domain_over_pi=["0","2"],
            strict_left_length_margin=str(self.C.lo-self.L0plus),
            strict_right_length_margin=str(self.Lrightminus-self.C.hi),
            accurate_rational_design_not_working_scalar_carrier=True)
        self.identity=canonical(encode(self.instantiation))
        self.counts=dict(complete_fixed_chart_evaluations=0,complete_polynomial_jet_evaluations=0)

    def point(self,value):
        return self.I(_fraction(value),_fraction(value),self.bits)

    def box(self,value):
        if hasattr(value,"lo") and hasattr(value,"hi"):
            return self.I(value.lo,value.hi,self.bits)
        if isinstance(value,(tuple,list)) and len(value)==2:
            return self.I(_fraction(value[0]),_fraction(value[1]),self.bits)
        return self.point(value)

    def trig(self,value):
        value=self.box(value);pi=self.k.pi_bounds(self.bits)
        if value.hi-value.lo>=2*pi.lo:
            return self.I(-1,1,self.bits),self.I(-1,1,self.bits)
        middle=(value.lo+value.hi)/2;p=(pi.lo+pi.hi)/2
        quotient=middle/(2*p)
        nearest=(quotient+F(1,2)).numerator//(quotient+F(1,2)).denominator
        reduced=value-2*nearest*pi
        return self.k.trig_boxes(reduced,order=64)

    def chart(self,phi):
        self.check();phi=self.box(phi);zero=self.point(0)
        theta=phi;rho=self.point(1);rhop=zero;rhopp=zero;p=self.point(1);pp=zero
        for j,c in enumerate(self.core,1):
            if c==0:continue
            n=2*j;sine,cosine=self.trig(n*phi);q=1-n*n
            theta=theta+F(q,n)*c*sine
            rho=rho+q*c*cosine;rhop=rhop-n*q*c*sine;rhopp=rhopp-n*n*q*c*cosine
            p=p+c*cosine;pp=pp-n*c*sine
        eps=F(1,1<<53)
        rho=rho.intersect(F(1,4)-553*eps,F(25,4)+553*eps)
        st,ct=self.trig(theta);sp,cp=self.trig(phi)
        er=[ct,st,zero];et=[-st,ct,zero];nr=[cp,sp,zero];nt=[-sp,cp,zero]
        e1=self.k.vscale(et,rho)
        e2=self.k.vsub(self.k.vscale(et,rhop),self.k.vscale(er,rho**2))
        gamma=self.k.vadd(self.k.vscale(nr,p),self.k.vscale(nt,pp))
        gamma1=self.k.vscale(nt,rho)
        gamma2=self.k.vsub(self.k.vscale(nt,rhop),self.k.vscale(nr,rho))
        self.counts["complete_fixed_chart_evaluations"]+=1
        return dict(phi=phi,theta=theta,rho=rho,rho_phi=rhop,
            e=[er,e1,e2],Gamma=[gamma,gamma1,gamma2],
            rho_n=[self.k.vscale(nr,rho),
                self.k.vadd(self.k.vscale(nr,rhop),self.k.vscale(nt,rho)),
                self.k.vadd(self.k.vscale(nr,rhopp-rho),self.k.vscale(nt,2*rhop))],
            full_fixed_core_identity=canonical([str(v) for v in self.core]))

    def partials(self,chart,xi,left,right,order):
        """Taylor coefficients in t; angular entries are actual derivatives."""
        self.check()
        left,right=_fraction(left),_fraction(right);xi=self.box(xi)
        if not 0<=left<=right<=1 or xi.lo<0 or xi.hi>self.xi_max:
            raise ValueError("Retain the complete physical t/xi domain")
        if type(order) is not int or not 0<=order<=90:
            raise ValueError("Declare a complete polynomial derivative order")
        if chart["full_fixed_core_identity"]!=canonical([str(v) for v in self.core]):
            raise ValueError("The complete original fixed chart changed")
        ranges={name:_polynomial_derivative_coefficients(poly,left,right,order,
            self.I,self.bits) for name,poly in self.polynomials.items() if name!="psi"}
        zero=self.point(0);result={}
        for q in range(3):
            for a in range(2):
                rows=[]
                for j in range(order+1):
                    if a:
                        A=-ranges["psi_A"][j]
                        B=-ranges["psi_B"][j]
                        D=-ranges["psi_D"][j]
                    else:
                        A=ranges["A"][j]-xi*ranges["psi_A"][j]
                        B=ranges["B"][j]-xi*ranges["psi_B"][j]
                        D=ranges["D"][j]-xi*ranges["psi_D"][j]
                    row=self.k.vadd(self.k.vscale(chart["Gamma"][q],A),
                        self.k.vadd(self.k.vscale(chart["e"][q],self.end.Rv*B),
                            self.k.vscale(chart["rho_n"][q],self.gamma*D)))
                    if not a and not q:
                        row[2]=row[2]+self.eta*ranges["Z"][j]+self.end.Z*ranges["B"][j]
                    rows.append(row)
                result[(a,q)]=rows
        self.counts["complete_polynomial_jet_evaluations"]+=1
        return result

    def metadata(self):
        if (file_record(self.proof["path"])!=self.proof or
                file_record(self.end.tail_proof["path"])!=self.end.tail_proof):
            raise ValueError("The complete R732 proof changed during accurate evaluation")
        return encode(dict(schema=SCHEMA,source_sha256=sha(__file__),
            mathematical_input_identity_sha256=self.identity,
            complete_theorem_instantiation=self.instantiation,actual_counts=self.counts))


def _series_add(a,b):
    return [x+y for x,y in zip(a,b)]


def _series_scale(a,value):
    return [x*value for x in a]


def _series_mul(a,b):
    n=min(len(a),len(b));zero=a[0].other(0)
    return [sum((a[j]*b[k-j] for j in range(k+1)),zero) for k in range(n)]


def _series_reciprocal(a):
    if a[0].lo<=0<=a[0].hi:
        raise LengthEnclosureUnavailable("A full integral derivative denominator remains unpaid")
    out=[1/a[0]];zero=a[0].other(0)
    for n in range(1,len(a)):
        out.append(-sum((a[j]*out[n-j] for j in range(1,n+1)),zero)/a[0])
    return out


def _series_sqrt(a):
    if a[0].lo<=0:
        raise LengthEnclosureUnavailable("Complete speed positivity is not separated on this t cell")
    out=[a[0].sqrt()];zero=a[0].other(0)
    for n in range(1,len(a)):
        out.append((a[n]-sum((out[j]*out[n-j] for j in range(1,n)),zero))/(2*out[0]))
    return out


def _vector_series_dot(a,b,*,same=False):
    zero=a[0][0].other(0);n=len(a[0])
    out=[zero]*n
    for x,y in zip(a,b):out=_series_add(out,_series_mul(x,y))
    if same:out[0]=sum((v[0]**2 for v in a),zero)
    return out


def speed_partial_series(polynomial,chart,xi,left,right,order,*,positive_speed_range=None):
    parts=polynomial.partials(chart,xi,left,right,order+1)
    def tangent(key):
        return [[(j+1)*parts[key][j+1][axis] for j in range(order+1)] for axis in range(3)]
    U,X,P,XP,PP=(tangent(key) for key in ((0,0),(1,0),(0,1),(1,1),(0,2)))
    squared=_vector_series_dot(U,U,same=True)
    if positive_speed_range is not None:
        bound=polynomial.box(positive_speed_range)
        if bound.lo<=0:raise ValueError("A previously complete positive speed bound is required")
        squared[0]=squared[0].intersect(bound.lo**2,bound.hi**2)
    speed=_series_sqrt(squared)
    inv=_series_reciprocal(speed);inv3=_series_mul(_series_mul(inv,inv),inv)
    ux=_vector_series_dot(U,X);up=_vector_series_dot(U,P)
    xx=_vector_series_dot(X,X,same=True)
    xp=_series_add(_vector_series_dot(X,P),_vector_series_dot(U,XP))
    pp=_series_add(_vector_series_dot(P,P,same=True),_vector_series_dot(U,PP))
    return dict(L=speed,L_xi=_series_mul(ux,inv),
        L_xixi=_series_add(_series_mul(xx,inv),_series_scale(_series_mul(_series_mul(ux,ux),inv3),-1)),
        L_phi=_series_mul(up,inv),
        L_xiphi=_series_add(_series_mul(xp,inv),_series_scale(_series_mul(_series_mul(ux,up),inv3),-1)),
        L_phiphi=_series_add(_series_mul(pp,inv),_series_scale(_series_mul(_series_mul(up,up),inv3),-1)))


class CompleteLengthIntegrator:
    """Full-domain interval Taylor integration, with one explicit split budget."""

    def __init__(self,polynomial,chart,*,panels=128,taylor_degree=16,
                 maximum_splits=8192,width_goal="1/1000000000000"):
        require_actions()
        if type(polynomial) is not ExactR732Polynomials:
            raise ValueError("Use the whole exact R732 polynomial source")
        if type(panels) is not int or panels<1:
            raise ValueError("Keep a complete positive initial partition")
        if type(taylor_degree) is not int or not 4<=taylor_degree<=64 or taylor_degree%2:
            raise ValueError("Use a declared even Taylor degree in 4..64")
        if type(maximum_splits) is not int or maximum_splits<0 or F(width_goal)<=0:
            raise ValueError("Keep the original complete accurate refinement budget")
        self.p,self.chart=polynomial,chart
        self.panels,self.degree=panels,taylor_degree
        self.maximum_splits,self.width_goal=maximum_splits,F(width_goal)
        self.splits=0;self.leaves=0;self.integrals=0

    def _cell(self,left,right,xi):
        self.p.check(leaves=1);self.leaves+=1
        degree=self.degree;centre=(left+right)/2;width=right-left
        at=speed_partial_series(self.p,self.chart,xi,centre,centre,degree-1)
        whole=speed_partial_series(self.p,self.chart,xi,left,right,degree)
        result={};tails={}
        for name in PARTIAL_KEYS:
            value=self.p.point(0)
            for j in range(0,degree,2):
                value=value+at[name][j]*width**(j+1)/((1<<j)*(j+1))
            tail=whole[name][degree]*width**(degree+1)/((1<<degree)*(degree+1))
            bound=value+tail
            crude=whole[name][0]*width
            result[name]=bound.intersect(crude.lo,crude.hi)
            tails[name]=tail.abs_upper()
        if whole["L"][0].lo<=0:
            raise LengthEnclosureUnavailable("A complete t cell still lacks a positive exact speed")
        return dict(left=left,right=right,integral=result,
            taylor_remainder_absolute_upper=tails,
            complete_speed_range=whole["L"][0],taylor_degree=degree)

    def _resolve(self,left,right,xi):
        pending=[(left,right)];complete=[]
        while pending:
            a,b=pending.pop()
            try:complete.append(self._cell(a,b,xi))
            except LengthEnclosureUnavailable:
                if self.splits>=self.maximum_splits:raise
                mid=(a+b)/2;self.splits+=1
                pending.extend(((mid,b),(a,mid)))
        return complete

    def integrate(self,xi,*,left=F(0),right=F(1),refine=True):
        left,right=F(left),F(right);xi=self.p.box(xi)
        if not 0<=left<=right<=1:
            raise ValueError("Integrate only a complete explicitly declared t interval")
        if left==right:
            zero=self.p.point(0)
            return dict(integrals={name:zero for name in PARTIAL_KEYS},
                left=left,right=right,complete_leaf_cover=[],speed_range=None,
                taylor_remainder_absolute_upper={name:F(0) for name in PARTIAL_KEYS},
                width_goal_met=True,taylor_remainder_goal_met=True,
                whole_interval_included=True,
                mathematical_input_identity_sha256=self.p.identity,
                accurate_phi_interval=self.chart["phi"],xi_interval=xi)
        # Intersections with the fixed complete initial partition retain both endpoints.
        cuts=sorted({left,right}|{F(j,self.panels) for j in range(1,self.panels)
            if left<F(j,self.panels)<right})
        active=[]
        for a,b in zip(cuts,cuts[1:]):active.extend(self._resolve(a,b,xi))
        def tail_totals():
            return {name:sum((row["taylor_remainder_absolute_upper"][name]
                for row in active),F(0)) for name in PARTIAL_KEYS}
        tails=tail_totals()
        while (refine and max(tails.values())>self.width_goal
                and self.splits<self.maximum_splits):
            self.p.check()
            index=max(range(len(active)),key=lambda j:max(
                active[j]["taylor_remainder_absolute_upper"].values()))
            old=active[index];mid=(old["left"]+old["right"])/2
            self.splits+=1
            replacement=self._resolve(old["left"],mid,xi)+self._resolve(mid,old["right"],xi)
            active[index:index+1]=replacement;tails=tail_totals()
        active.sort(key=lambda item:item["left"])
        if (active[0]["left"]!=left or active[-1]["right"]!=right
                or any(a["right"]!=b["left"] for a,b in zip(active,active[1:]))):
            raise ValueError("The complete exact integral cover changed")
        sums={name:sum((row["integral"][name] for row in active),self.p.point(0))
            for name in PARTIAL_KEYS}
        speed=self.p.I(min(row["complete_speed_range"].lo for row in active),
            max(row["complete_speed_range"].hi for row in active),self.p.bits)
        self.integrals+=1
        return dict(integrals=sums,left=left,right=right,xi_interval=xi,
            mathematical_input_identity_sha256=self.p.identity,
            accurate_phi_interval=self.chart["phi"],
            complete_leaf_cover=active,speed_range=speed,
            taylor_remainder_absolute_upper=tails,
            width_goal_met=max(v.hi-v.lo for v in sums.values())<=self.width_goal,
            taylor_remainder_goal_met=max(tails.values())<=self.width_goal,
            whole_interval_included=True,
            interval_width_from_true_phi_or_xi_variation_is_retained=True)

    def metadata(self):
        return dict(schema=SCHEMA+"-complete-integral-budget",initial_panels=self.panels,
            taylor_degree=self.degree,maximum_splits=self.maximum_splits,
            actual_splits=self.splits,actual_leaf_evaluations=self.leaves,
            complete_integrals=self.integrals,width_goal=str(self.width_goal),
            partial_cells_are_true_exact_integrals_not_working_Gauss_interpolants=True)


class CompleteAccurateLengthRoot:
    """One complete angular interval; exact unique root and both angular jets."""

    def __init__(self,polynomial,phi,*,candidate_xi,candidate_xi_phi,
                 candidate_xi_phiphi,candidate_source,bound_field_scope,panels=128,
                 taylor_degree=16,maximum_splits=8192,
                 width_goal="1/1000000000000",inverse_steps=64,
                 inverse_width="1/1000000000000000000000000"):
        require_actions()
        if type(polynomial) is not ExactR732Polynomials:
            raise ValueError("Use this complete exact R732 polynomial implementation")
        self.p,self.k=polynomial,polynomial.k
        self.phi=polynomial.box(phi);self.chart=polynomial.chart(self.phi)
        self.candidate=tuple(_fraction(v) for v in (
            candidate_xi,candidate_xi_phi,candidate_xi_phiphi))
        if not 0<=self.candidate[0]<=polynomial.xi_max:
            raise ValueError("The source-bound working candidate must retain its declared range")
        if not isinstance(candidate_source,dict) or not candidate_source:
            raise ValueError("Retain the complete actual candidate/source attribution")
        self.candidate_source=json.loads(json.dumps(encode(candidate_source)))
        required_scope=("actual_input_identity_sha256","current_full_point_sha256",
            "complete_current_model_identity_sha256","complete_seed_model_identity_sha256",
            "fixed_target_identity_sha256")
        if (not isinstance(bound_field_scope,dict)
                or set(bound_field_scope)!=set(required_scope)
                or any(not is_digest(bound_field_scope[k]) for k in required_scope)):
            raise ValueError("Bind the actual whole input/model/point/seed/target identities")
        self.bound_field_scope=dict(bound_field_scope)
        if type(inverse_steps) is not int or inverse_steps<1 or F(inverse_width)<=0:
            raise ValueError("Retain the complete inverse-arclength refinement budget")
        self.inverse_steps,self.inverse_width=inverse_steps,F(inverse_width)
        self.integrator=CompleteLengthIntegrator(polynomial,self.chart,panels=panels,
            taylor_degree=taylor_degree,maximum_splits=maximum_splits,width_goal=width_goal)
        candidate_integral=self.integrator.integrate(polynomial.point(self.candidate[0]))
        residual=candidate_integral["integrals"]["L"]-polynomial.C
        radius=residual.abs_upper()/polynomial.root_slope_lower
        lo=max(F(0),self.candidate[0]-radius)
        hi=min(polynomial.xi_max,self.candidate[0]+radius)
        if lo>hi:
            raise ValueError("The complete residual enclosure contradicts the proved unique root")
        self.xi=polynomial.I(lo,hi,polynomial.bits)
        global_residual_interval=self.xi
        true_root_integral=self.integrator.integrate(self.xi)
        refinement=None
        raw_derivative=true_root_integral["integrals"]["L_xi"]
        if raw_derivative.lo>0:
            # Here the derivative is genuinely positive on the ENTIRE initial
            # xi interval and every phi, so an ordinary mean-value step is valid.
            proposed=polynomial.point(self.candidate[0])-residual/raw_derivative
            improved=self.xi.intersect(proposed.lo,proposed.hi)
            if improved.lo!=self.xi.lo or improved.hi!=self.xi.hi:
                refinement=dict(previous_interval=self.xi,
                    complete_derivative_integral=true_root_integral,
                    full_interval_Lxi=raw_derivative,
                    exact_candidate=str(self.candidate[0]),candidate_residual=residual,
                    mean_value_updated_interval=improved)
                self.xi=improved
                true_root_integral=self.integrator.integrate(self.xi)
        partial=true_root_integral["integrals"]
        # This intersection is used only at the already-proved true root. It is
        # not an interval Newton derivative bound for arbitrary xi in this box.
        denominator=partial["L_xi"].intersect(polynomial.root_slope_lower,
            partial["L_xi"].hi)
        self.xi_phi=-partial["L_phi"]/denominator
        self.xi_phiphi=-(partial["L_phiphi"]+2*partial["L_xiphi"]*self.xi_phi
            +partial["L_xixi"]*(self.xi_phi**2))/denominator
        self.speed_range=true_root_integral["speed_range"]
        if self.speed_range is None or self.speed_range.lo<=0:
            raise LengthEnclosureUnavailable("The full t-domain exact speed is unpaid")
        self.bounds=dict(xi=self.xi,xi_phi=self.xi_phi,xi_phiphi=self.xi_phiphi,
            true_root_L_xi=denominator,complete_exact_speed=self.speed_range,
            candidate_residual=residual,global_residual_radius=str(radius),
            saved_root_word_error_upper=str((self.xi-self.candidate[0]).abs_upper()),
            saved_first_angle_word_error_upper=str((self.xi_phi-self.candidate[1]).abs_upper()),
            saved_second_angle_word_error_upper=str((self.xi_phiphi-self.candidate[2]).abs_upper()))
        record=dict(schema=SCHEMA+"-unique-length-root",
            source_sha256=sha(__file__),mathematical_input_identity_sha256=polynomial.identity,
            complete_theorem_instantiation=polynomial.instantiation,
            accurate_phi_interval=self.phi,complete_actual_candidate_source=self.candidate_source,
            bound_field_scope=self.bound_field_scope,
            exact_saved_candidate_values=[str(v) for v in self.candidate],
            candidate_residual_integral=candidate_integral,
            true_root_partial_derivative_integral=true_root_integral,
            bounds=self.bounds,global_residual_root_interval=global_residual_interval,
            full_interval_mean_value_refinement=refinement,whole_t_interval=["0","1"],
            full_angular_interval_not_a_literal_sample=True,
            root_existence_attribution="R732 global complete length endpoint margins and convexity",
            global_convex_residual_bound_applied=True,
            root_uniqueness_domain=["0",str(polynomial.xi_max)],
            true_root_strictly_inside_domain=True,
            raw_candidate_not_promoted_to_exact_root=True,
            old_mean_root_or_cap_uniqueness_inherited=False,
            inverse_or_reference_field_enclosures_not_yet_produced=True)
        self.root_record=encode(record)
        self.root_identity=canonical(self.root_record)
        self.root_record["identity_sha256"]=self.root_identity
        self.query_counts=dict(complete_inverse_calls=0,complete_inverse_iterations=0,
            complete_reference_boxes=0,complete_partial_integrals=0)
        self._queries={}

    def _combined(self,partials):
        p=partials
        return [p["L"],
            p["L_phi"]+p["L_xi"]*self.xi_phi,
            p["L_phiphi"]+2*p["L_xiphi"]*self.xi_phi
                +p["L_xixi"]*(self.xi_phi**2)+p["L_xi"]*self.xi_phiphi]

    def _range_partials(self,left,right):
        return {name:row[0] for name,row in speed_partial_series(
            self.p,self.chart,self.xi,F(left),F(right),0,
            positive_speed_range=self.speed_range).items()}

    def _arc(self,t):
        """ell and its two fixed-t angular derivatives, evaluated on a whole t box."""
        t=self.p.box(t)
        if t.lo<0 or t.hi>1:raise ValueError("Retain the original complete inverse domain")
        zero=self.p.point(0)
        if t.lo==t.hi==0:
            return dict(jets=[zero,zero,zero],integration_side="exact core",
                complete_fixed_integral=None,variable_limit_cell=None)
        if t.lo==t.hi==1:
            return dict(jets=[self.p.C,zero,zero],integration_side="exact central length",
                complete_fixed_integral=None,variable_limit_cell=None,
                exact_root_length_identity_used=True)
        side="prefix" if t.lo+t.hi<=1 else "suffix"
        if side=="prefix":
            fixed=self.integrator.integrate(self.xi,left=F(0),right=t.lo)
        else:
            fixed=self.integrator.integrate(self.xi,left=t.hi,right=F(1))
        values=dict(fixed["integrals"]);variable=None
        if t.lo<t.hi:
            ranges=self._range_partials(t.lo,t.hi)
            width=self.p.I(0,t.hi-t.lo,self.p.bits)
            variable=dict(left=t.lo,right=t.hi,complete_integrand_ranges=ranges,
                unknown_limit_width=width,
                formula="integral over a prefix/suffix of the entire declared t cell")
            for name in PARTIAL_KEYS:values[name]=values[name]+width*ranges[name]
        combined=self._combined(values)
        if side=="suffix":
            # The root relation L_c(xi(phi),phi)=C=S-L_end is exact and C is angle-independent.
            combined=[self.p.C-combined[0],-combined[1],-combined[2]]
        self.query_counts["complete_partial_integrals"]+=1
        return dict(jets=combined,integration_side=side,
            complete_fixed_integral=fixed,variable_limit_cell=variable,
            exact_root_length_identity_used=(side=="suffix"))

    def _speed_on(self,t):
        parts=self.p.partials(self.chart,self.xi,t.lo,t.hi,1)
        velocity=parts[(0,0)][1]
        bound=self.k.norm_box(velocity)
        return bound.intersect(self.speed_range.lo,self.speed_range.hi)

    def _physical_interval(self,left,right):
        if (not isinstance(left,(tuple,list)) or not isinstance(right,(tuple,list))
                or len(left)!=2 or len(right)!=2):
            raise ValueError("Retain both complete exact affine material addresses")
        left,right=tuple(_fraction(q) for q in left),tuple(_fraction(q) for q in right)
        lo=left[0]*self.p.S+left[1];hi=right[0]*self.p.S+right[1]
        before=lo
        after=(1-right[0])*self.p.S-right[1]
        width=(right[0]-left[0])*self.p.S+(right[1]-left[1])
        if (before.lo<0 or after.lo<0 or width.lo<0
                or (left!=right and width.hi<=0)):
            raise LengthEnclosureUnavailable("The complete material interval is not ordered in [0,S]")
        return left,right,self.p.I(lo.lo,hi.hi,self.p.bits)

    def _central_inverse(self,left,right,target):
        self.query_counts["complete_inverse_calls"]+=1
        if left==right==(F(0),F(0)):
            return self.p.point(0),dict(target=target,exact_endpoint=0,iterations=[])
        interval=self.p.I(0,1,self.p.bits);history=[]
        for iteration in range(self.inverse_steps):
            self.p.check()
            if interval.hi-interval.lo<=self.inverse_width:break
            centre=(interval.lo+interval.hi)/2
            arc=self._arc(self.p.point(centre))
            residual=arc["jets"][0]-target
            speed=self._speed_on(interval)
            proposed=self.p.point(centre)-residual/speed
            updated=interval.intersect(max(F(0),proposed.lo),min(F(1),proposed.hi))
            history.append(dict(iteration=iteration,previous_interval=interval,
                exact_trial_t=str(centre),complete_arc_integral=arc,
                residual=residual,complete_segment_speed=speed,
                outward_updated_interval=updated))
            self.query_counts["complete_inverse_iterations"]+=1
            if updated.lo==interval.lo and updated.hi==interval.hi:break
            interval=updated
        return interval,dict(target=target,exact_affine_left=[str(q) for q in left],
            exact_affine_right=[str(q) for q in right],iterations=history,
            inverse_width_goal=str(self.inverse_width),
            width_goal_met=interval.hi-interval.lo<=self.inverse_width,
            complete_monotone_inverse_enclosed=True,
            width_goal_not_promoted_to_an_existence_condition=True)

    def _central_box(self,left,right,target):
        t,inverse=self._central_inverse(left,right,target)
        arc=self._arc(t);ell,ell_phi,ell_phiphi=arc["jets"]
        part=self.p.partials(self.chart,self.xi,t.lo,t.hi,3)
        def G(a,q,order):
            return self.k.vscale(part[(a,q)][order],math.factorial(order))
        position=G(0,0,0);U=G(0,0,1);Ut=G(0,0,2);Utt=G(0,0,3)
        angle=self.k.vadd(G(0,1,0),self.k.vscale(G(1,0,0),self.xi_phi))
        angle2=self.k.vadd(self.k.vadd(G(0,2,0),
            self.k.vscale(G(1,1,0),2*self.xi_phi)),
            self.k.vscale(G(1,0,0),self.xi_phiphi))
        Uphi=self.k.vadd(G(0,1,1),self.k.vscale(G(1,0,1),self.xi_phi))
        Upphi=self.k.vadd(self.k.vadd(G(0,2,1),
            self.k.vscale(G(1,1,1),2*self.xi_phi)),
            self.k.vscale(G(1,0,1),self.xi_phiphi))
        Utphi=self.k.vadd(G(0,1,2),self.k.vscale(G(1,0,2),self.xi_phi))
        speed=self.k.norm_box(U).intersect(self.speed_range.lo,self.speed_range.hi)
        vt=self.k.dot(U,Ut)/speed;vp=self.k.dot(U,Uphi)/speed
        tp=-ell_phi/speed
        tpp=-(ell_phiphi+2*vp*tp+vt*(tp**2))/speed
        W1=self.k.vadd(Uphi,self.k.vscale(Ut,tp))
        W2=self.k.vadd(self.k.vadd(Upphi,self.k.vscale(Utphi,2*tp)),
            self.k.vadd(self.k.vscale(Utt,tp**2),self.k.vscale(Ut,tpp)))
        tangent,_=self.k.normalized_jets(U,W1,W2,
            norm_lower=speed.lo,norm_upper=speed.hi)
        Ts=self.k.vsub(self.k.vscale(Ut,1/(speed**2)),
            self.k.vscale(U,self.k.dot(U,Ut)/(speed**4)))
        Fphi=self.k.vadd(angle,self.k.vscale(U,tp))
        Fphiphi=self.k.vadd(self.k.vadd(angle2,self.k.vscale(Uphi,2*tp)),
            self.k.vadd(self.k.vscale(Ut,tp**2),self.k.vscale(U,tpp)))
        result=dict(schema=SCHEMA+"-complete-reference-box",
            source_sha256=sha(__file__),root_identity_sha256=self.root_identity,
            mathematical_input_identity_sha256=self.p.identity,
            bound_field_scope=self.bound_field_scope,
            accurate_phi_interval=self.phi,
            exact_affine_left=[str(_fraction(q)) for q in left],
            exact_affine_right=[str(_fraction(q)) for q in right],
            accurate_inverse_t=t,complete_inverse_attribution=inverse,
            complete_fixed_t_arc_attribution=arc,xi_jets=[self.xi,self.xi_phi,self.xi_phiphi],
            exact_inverse_angle_jets=[tp,tpp],positive_exact_speed=speed,
            T0=tangent[0],T0_phi=tangent[1],T0_phiphi=tangent[2],T0_s=Ts,
            exact_reference_primitive_sixjets=dict(
                F=position,Fs=tangent[0],Fss=Ts,Fphi=Fphi,
                Fsphi=tangent[1],Fphiphi=Fphiphi),
            material_and_angular_chain_order_complete=True,
            clipped_central_interval_included=True,
            reference_only_not_current_corrected_normal_field=True,
            branch="central",clipped_central_material_interval=target,
            working_inverse_root_or_finite_difference_used_as_exact=False,
            original_working_reference_word_errors_compared=False)
        return result

    def reference_box(self,left,right):
        left,right,s=self._physical_interval(left,right)
        key=canonical([[str(v) for v in side] for side in (left,right)])
        if key in self._queries:return self._queries[key]
        end=self.p.end
        # Use the affine backward addresses before interval evaluation. At the
        # exact cap query (S,S) this returns the single point zero.
        low_u=(1-right[0])*self.p.S-right[1]
        high_u=(1-left[0])*self.p.S-left[1]
        u=self.p.I(low_u.lo,high_u.hi,self.p.bits)
        rows=[]
        if u.hi>=end.L.lo and s.lo<=self.p.C.hi:
            # Extend the inverse by its endpoint for uncertain crossover points.
            # The image of min(s,C) always exists on the compact central curve.
            central=self.p.I(max(F(0),min(s.lo,self.p.C.lo)),min(s.hi,self.p.C.hi),self.p.bits)
            rows.append(self._central_box(left,right,central))
        if u.lo<=end.L.hi and s.hi>=self.p.C.lo:
            end_domain=self.p.I(max(F(0),u.lo),min(u.hi,end.L.hi),self.p.bits)
            rows.extend(end.boxes(self.chart,end_domain))
        if not rows:raise ValueError("The physical reference cover cannot be empty")
        def hull(vectors):
            return [self.p.I(min(v[j].lo for v in vectors),
                max(v[j].hi for v in vectors),self.p.bits) for j in range(3)]
        keys=("T0","T0_phi","T0_phiphi","T0_s")
        components={name:hull([row[name] for row in rows]) for name in keys}
        six={name:hull([row["exact_reference_primitive_sixjets"][name] for row in rows])
            for name in ("F","Fs","Fss","Fphi","Fsphi","Fphiphi")}
        result=dict(schema=SCHEMA+"-complete-reference-box",
            source_sha256=sha(__file__),root_identity_sha256=self.root_identity,
            mathematical_input_identity_sha256=self.p.identity,
            bound_field_scope=self.bound_field_scope,accurate_phi_interval=self.phi,
            exact_affine_left=[str(v) for v in left],exact_affine_right=[str(v) for v in right],
            original_S=self.p.S,accurate_central_length=self.p.C,
            original_material_interval=s,backward_material_interval=u,
            terminal_material_boundaries=end.boundaries,
            complete_material_piece_boxes=rows,exact_reference_primitive_sixjets=six,
            material_and_angular_chain_order_complete=True,
            entire_original_material_interval_included=True,
            reference_only_not_current_corrected_normal_field=True,
            working_inverse_root_or_finite_difference_used_as_exact=False,
            original_working_reference_word_errors_compared=False,**components)
        self.query_counts["complete_reference_boxes"]+=1
        self._queries[key]=result
        return result

    def metadata(self):
        return encode(dict(schema=SCHEMA+"-complete-root-and-reference-metadata",
            source_sha256=sha(__file__),complete_polynomial=self.p.metadata(),
            root=self.root_record,root_identity_sha256=self.root_identity,
            complete_integral_budget=self.integrator.metadata(),
            actual_reference_query_counts=self.query_counts,actual_end_piece_evaluations=self.p.end.counts,
            complete_inverse_budget=dict(steps=self.inverse_steps,width=str(self.inverse_width)),
            old_v_d_w_lambda_or_profile_mean_inherited=False,
            all_current_normal32_and_corrected_field_obligations_separate=True))


def is_digest(value):
    return (isinstance(value,str) and len(value)==64
        and all(c in "0123456789abcdef" for c in value))


def _pair(value):
    if (not isinstance(value,(tuple,list)) or len(value)!=2
            or any(type(v) is not str for v in value)):
        raise ValueError("Keep a complete serialized exact rational interval")
    lo,hi=F(value[0]),F(value[1])
    if lo>hi:raise ValueError("Reversed saved accurate interval")
    return lo,hi


def _proof_record(record):
    if (not isinstance(record,dict) or not isinstance(record.get("path"),str)
            or record.get("bytes")!=THEOREM_BYTES or record.get("sha256")!=THEOREM_SHA256):
        raise ValueError("Keep the exact complete R732 proof record")
    return record


def _instantiation(value):
    if (not isinstance(value,dict)
            or value.get("schema")!=SCHEMA+"-complete-theorem-instantiation"
            or value.get("definition")!=definition()
            or value.get("complete_fixed_core_coefficients")!=
                [str(round_binary64_exact(F(q))) for q in DESIGN_COEFFICIENTS]+["0"]*153):
        raise ValueError("The exact complete R732 mathematical input changed")
    bits=value.get("precision_bits")
    if type(bits) is not int or not 64<=bits<=1024:
        raise ValueError("Keep the declared full outward precision")
    slo,shi=_pair(value["accurate_S"]);rlo,rhi=_pair(value["accurate_R"])
    H,kappa=F(value["exact_fixed_seed_H0"]),F(value["exact_kappa0"])
    if (not F(237,100)<slo<=shi<F(119,50)
            or not F(9,16)<rlo<=rhi<F(57,100)
            or not F(97,50)<H<F(39,20) or not 0<kappa<F(1,4)):
        raise ValueError("The full published theorem hypothesis is missing")
    end=value["accurate_terminal"]
    tail=end["tail_proof"]
    if (not isinstance(tail.get("path"),str) or tail.get("bytes")!=TAIL_PROOF_BYTES
            or tail.get("sha256")!=TAIL_PROOF_SHA256
            or F(end["actual_binary_width"])!=F(5764607523034235,288230376151711744)
            or F(end["actual_tail_kappa"])!=F(3,2)
            or end["original_pure_exponential_interval"]!=["0","1/500"]
            or end["exact_Gram_reference_only_material_interval"]!=["0","1/1000"]
            or end["actual_deep_turns_truncated"] is not False
            or [F(end[key]) for key in ("b","d","relative_height")]!=[F(1,1000),F(7,50),F(13,50)]
            or end["ordered_piece_names"]!=list(AccurateRoundedEnd.pieces)
            or end["ideal_trig_primitive_Taylor_degree"]!=AccurateRoundedEnd.trig_degree):
        raise ValueError("Keep both original proofs and the whole rounded-end definition")
    elo,ehi=_pair(end["L"]);xlo,xhi=_pair(end["xf"]);hlo,hhi=_pair(end["hf"])
    u0,u1=_pair(end["uf"]);r0,r1=_pair(end["Rv"])
    clo,chi=_pair(value["accurate_central_length"])
    if (not F(33,100)<elo<=ehi<F(35,100) or elo>u0+F(13,50)-hhi
            or ehi<u1+F(13,50)-hlo or r0>rlo+xlo or r1<rhi+xhi
            or not F(281,400)<r0<=r1<F(713,1000) or F(end["Z"])!=H-F(13,50)
            or clo>slo-ehi or chi<shi-elo
            or end["material_boundaries"][3:]!=[end["uc"],end["uf"],end["L"]]):
        raise ValueError("Keep the actual terminal integrals, end radius and central length")
    expected=dict(eta=HANDLE_LENGTH,xi_max=MAXIMUM_CONTRACTION,
        L0_upper=BASELINE_LENGTH_UPPER,L_ximax_lower=RIGHT_LENGTH_LOWER,
        exact_positive_length_gap=str(clo-F(BASELINE_LENGTH_UPPER)),
        exact_true_root_Lxi_lower=str((clo-F(BASELINE_LENGTH_UPPER))/F(MAXIMUM_CONTRACTION)),
        whole_domain_over_pi=["0","2"],
        strict_left_length_margin=str(clo-F(BASELINE_LENGTH_UPPER)),
        strict_right_length_margin=str(F(RIGHT_LENGTH_LOWER)-chi),
        accurate_rational_design_not_working_scalar_carrier=True)
    if any(value.get(key)!=entry for key,entry in expected.items()):
        raise ValueError("Do not replace the actual complete endpoint-margin instantiation")
    _proof_record(value["proof_record"])
    return clo,chi,F(expected["exact_true_root_Lxi_lower"])


def _integral_record(value,*,left,right,xi,phi,mathematical_identity):
    if (not isinstance(value,dict) or F(value.get("left"))!=left
            or F(value.get("right"))!=right
            or value.get("xi_interval")!=xi or value.get("accurate_phi_interval")!=phi
            or value.get("mathematical_input_identity_sha256")!=mathematical_identity
            or value.get("whole_interval_included") is not True):
        raise ValueError("Bind the whole exact integral to the same mathematical interval")
    leaves=value["complete_leaf_cover"]
    if not isinstance(leaves,list) or not leaves:
        raise ValueError("A positive full interval needs its complete leaf cover")
    edge=left;sums={name:[F(0),F(0)] for name in PARTIAL_KEYS}
    speed_lo=None;speed_hi=None
    for leaf in leaves:
        a,b=F(leaf["left"]),F(leaf["right"])
        if a!=edge or not a<b<=right:
            raise ValueError("Missing, reordered or overlapping accurate integral cell")
        if type(leaf["taylor_degree"]) is not int or leaf["taylor_degree"]%2 or leaf["taylor_degree"]<4:
            raise ValueError("Keep the actual complete even Taylor rule")
        v0,v1=_pair(leaf["complete_speed_range"])
        if v0<=0:raise ValueError("Every full integral cell requires positive accurate speed")
        speed_lo=v0 if speed_lo is None else min(speed_lo,v0)
        speed_hi=v1 if speed_hi is None else max(speed_hi,v1)
        for name in PARTIAL_KEYS:
            lo,hi=_pair(leaf["integral"][name]);sums[name][0]+=lo;sums[name][1]+=hi
            if F(leaf["taylor_remainder_absolute_upper"][name])<0:
                raise ValueError("A complete outward remainder cannot be negative")
        edge=b
    if edge!=right:raise ValueError("The complete integral suffix is missing")
    for name in PARTIAL_KEYS:
        lo,hi=_pair(value["integrals"][name])
        if lo>sums[name][0] or hi<sums[name][1]:
            raise ValueError("The claimed complete integral omits a leaf contribution")
    vlo,vhi=_pair(value["speed_range"])
    if not 0<vlo<=speed_lo<=speed_hi<=vhi:
        raise ValueError("Keep the speed bound on the whole original t domain")
    return {name:_pair(value["integrals"][name]) for name in PARTIAL_KEYS}



def _pair_add(a,b):
    return a[0]+b[0],a[1]+b[1]


def _pair_neg(a):
    return -a[1],-a[0]


def _pair_mul(a,b):
    values=[x*y for x in a for y in b]
    return min(values),max(values)


def _pair_square(a):
    return (F(0) if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),
        max(a[0]**2,a[1]**2))


def _pair_div(a,b):
    if b[0]<=0<=b[1]:raise ValueError("The saved exact denominator contains zero")
    return _pair_mul(a,(1/b[1],1/b[0]))

def validate_root_domain_attribution(value,*,mathematical_input,phi_interval,
        candidate_source,bound_field_scope,source_by_role,current_full_point_sha256):
    """Pure metadata/algebra validator; no function, root or science evaluation."""
    if not isinstance(value,dict) or value.get("schema")!=SCHEMA+"-unique-length-root":
        raise ValueError("Use the new complete R732 root-domain attribution")
    expected_math=encode(mathematical_input)
    if (value.get("complete_theorem_instantiation")!=expected_math
            or value.get("mathematical_input_identity_sha256")!=canonical(expected_math)
            or value.get("accurate_phi_interval")!=encode(phi_interval)
            or value.get("complete_actual_candidate_source")!=encode(candidate_source)
            or value.get("bound_field_scope")!=bound_field_scope
            or bound_field_scope.get("current_full_point_sha256")!=current_full_point_sha256
            or not is_digest(current_full_point_sha256)):
        raise ValueError("The exact reference proof belongs to another source/point/whole angle")
    source=source_by_role["accurate_length"]
    proof=source_by_role["R732_proof"]
    if (source.get("sha256")!=value.get("source_sha256")
            or type(source.get("bytes")) is not int or source["bytes"]<=0
            or not isinstance(source.get("path"),str)
            or proof!=expected_math["proof_record"]):
        raise ValueError("Keep the producer's complete actual source and original proof records")
    _proof_record(proof)
    if source_by_role["R690_proof"]!=expected_math["accurate_terminal"]["tail_proof"]:
        raise ValueError("Keep the original full deep-tail proof attribution")
    copy=dict(value);identity=copy.pop("identity_sha256",None)
    if not is_digest(identity) or canonical(copy)!=identity:
        raise ValueError("The complete R732 root record changed")
    slo,shi,sigma=_instantiation(expected_math)
    candidate=value["exact_saved_candidate_values"]
    if (not isinstance(candidate,list) or len(candidate)!=3
            or any(type(v) is not str for v in candidate)):
        raise ValueError("Retain all three actual saved length-root words")
    xi=F(candidate[0]);maximum=F(MAXIMUM_CONTRACTION)
    if not 0<=xi<=maximum:raise ValueError("The candidate left the declared physical xi domain")
    phi=encode(phi_interval);mathid=canonical(expected_math)
    scale=1<<expected_math["precision_bits"]
    low=F((xi*scale).numerator//(xi*scale).denominator,scale)
    high=-F((-xi*scale).numerator//(-xi*scale).denominator,scale)
    candidate_box=[str(low),str(high)]
    candidate_integral=_integral_record(value["candidate_residual_integral"],
        left=F(0),right=F(1),xi=candidate_box,phi=phi,mathematical_identity=mathid)
    bounds=value["bounds"];f0,f1=_pair(bounds["candidate_residual"])
    if f0>candidate_integral["L"][0]-shi or f1<candidate_integral["L"][1]-slo:
        raise ValueError("The complete accurate residual does not include the original S minus the full rounded-end length")
    radius=max(abs(f0),abs(f1))/sigma
    if F(bounds["global_residual_radius"])!=radius:
        raise ValueError("Keep the complete convex residual radius")
    glo,ghi=_pair(value["global_residual_root_interval"])
    if (glo<0 or ghi>maximum or glo>max(F(0),xi-radius)
            or ghi<min(maximum,xi+radius)):
        raise ValueError("The complete global convex residual enclosure was narrowed without proof")
    xlo,xhi=_pair(bounds["xi"])
    refinement=value.get("full_interval_mean_value_refinement")
    if refinement is None:
        if (xlo,xhi)!=(glo,ghi):raise ValueError("An unrecorded root refinement changed the domain")
    else:
        if (refinement.get("previous_interval")!=value["global_residual_root_interval"]
                or refinement.get("exact_candidate")!=str(xi)
                or refinement.get("candidate_residual")!=bounds["candidate_residual"]
                or refinement.get("mean_value_updated_interval")!=bounds["xi"]):
            raise ValueError("Retain the complete full-interval mean-value refinement")
        initial=_integral_record(refinement["complete_derivative_integral"],
            left=F(0),right=F(1),xi=value["global_residual_root_interval"],
            phi=phi,mathematical_identity=mathid)
        raw=_pair(refinement["full_interval_Lxi"])
        if not 0<raw[0]<=initial["L_xi"][0]<=initial["L_xi"][1]<=raw[1]:
            raise ValueError("The refinement needs positivity on the ENTIRE xi interval")
        if not glo<=xi<=ghi:raise ValueError("The mean-value segment left its complete derivative box")
        quotient=_pair_div((f0,f1),raw)
        required_lo=max(glo,xi-quotient[1])
        required_hi=min(ghi,xi-quotient[0])
        if (required_lo>required_hi or xlo>required_lo or xhi<required_hi
                or xlo<glo or xhi>ghi):
            raise ValueError("The mean-value updated interval omits a possible true root")
    true_integral=_integral_record(value["true_root_partial_derivative_integral"],
        left=F(0),right=F(1),xi=bounds["xi"],phi=phi,mathematical_identity=mathid)
    d0,d1=_pair(bounds["true_root_L_xi"])
    if not 0<d0<=max(sigma,true_integral["L_xi"][0])<=true_integral["L_xi"][1]<=d1:
        raise ValueError("Keep the true-root-only positive derivative enclosure")
    first_expected=_pair_div(_pair_neg(true_integral["L_phi"]),(d0,d1))
    first=_pair(bounds["xi_phi"])
    if first[0]>first_expected[0] or first[1]<first_expected[1]:
        raise ValueError("The complete first implicit angle jet was narrowed without proof")
    numerator=_pair_add(true_integral["L_phiphi"],
        _pair_add(_pair_mul((F(2),F(2)),_pair_mul(true_integral["L_xiphi"],first)),
            _pair_mul(true_integral["L_xixi"],_pair_square(first))))
    second_expected=_pair_div(_pair_neg(numerator),(d0,d1))
    second=_pair(bounds["xi_phiphi"])
    if second[0]>second_expected[0] or second[1]<second_expected[1]:
        raise ValueError("The complete second implicit angle jet was narrowed without proof")
    v0,v1=_pair(bounds["complete_exact_speed"])
    iv0,iv1=_pair(value["true_root_partial_derivative_integral"]["speed_range"])
    if not 0<v0<=iv0<=iv1<=v1:
        raise ValueError("Retain the complete original inverse speed proof")
    required=dict(whole_t_interval=["0","1"],
        full_angular_interval_not_a_literal_sample=True,
        root_existence_attribution="R732 global complete length endpoint margins and convexity",
        global_convex_residual_bound_applied=True,
        root_uniqueness_domain=["0",str(maximum)],true_root_strictly_inside_domain=True,
        raw_candidate_not_promoted_to_exact_root=True,
        old_mean_root_or_cap_uniqueness_inherited=False,
        inverse_or_reference_field_enclosures_not_yet_produced=True)
    if any(value.get(key)!=entry for key,entry in required.items()):
        raise ValueError("The complete new root attribution was replaced by a legacy boolean")
    for name,old in (("xi",candidate[0]),("xi_phi",candidate[1]),("xi_phiphi",candidate[2])):
        lo,hi=_pair(bounds[name])
        error_name={"xi":"saved_root_word_error_upper",
            "xi_phi":"saved_first_angle_word_error_upper",
            "xi_phiphi":"saved_second_angle_word_error_upper"}[name]
        if F(bounds[error_name])<max(abs(lo-F(old)),abs(hi-F(old))):
            raise ValueError("Every actual saved length-root angular word keeps its own error")
    return dict(schema=SCHEMA+"-validated-root-attribution",root_identity_sha256=identity,
        mathematical_input_identity_sha256=mathid,
        current_full_point_sha256=current_full_point_sha256,
        actual_bound_field_scope=dict(bound_field_scope),
        complete_global_scalar_root_uniqueness_used=True,
        old_mean_or_R727_cap_claim_used=False)


def validate_reference_box_attribution(value,*,root_identity,mathematical_identity,
        bound_field_scope,phi_interval,left,right,source_sha256,mathematical_input):
    if (not isinstance(value,dict) or value.get("schema")!=SCHEMA+"-complete-reference-box"
            or value.get("source_sha256")!=source_sha256
            or value.get("root_identity_sha256")!=root_identity
            or value.get("mathematical_input_identity_sha256")!=mathematical_identity
            or value.get("bound_field_scope")!=bound_field_scope
            or value.get("accurate_phi_interval")!=encode(phi_interval)
            or value.get("exact_affine_left")!=[str(F(q)) for q in left]
            or value.get("exact_affine_right")!=[str(F(q)) for q in right]):
        raise ValueError("The full R732 radial reference box changed its actual attribution")
    math_source=encode(mathematical_input)
    if (canonical(math_source)!=mathematical_identity
            or value.get("original_S")!=math_source.get("accurate_S")
            or value.get("accurate_central_length")!=math_source.get("accurate_central_length")
            or value.get("terminal_material_boundaries")!=math_source["accurate_terminal"]["material_boundaries"]):
        raise ValueError("Use the same exact whole end and central-length instantiation")
    _instantiation(math_source)
    S=_pair(value["original_S"]);C=_pair(value["accurate_central_length"])
    boundaries=[_pair(entry) for entry in value["terminal_material_boundaries"]]
    left=tuple(F(q) for q in left);right=tuple(F(q) for q in right)
    def affine(k,b):
        return _pair_add(_pair_mul((k,k),S),(b,b))
    s=_pair(value["original_material_interval"]);u=_pair(value["backward_material_interval"])
    if (s[0]>affine(*left)[0] or s[1]<affine(*right)[1]
            or u[0]>affine(1-right[0],-right[1])[0]
            or u[1]<affine(1-left[0],-left[1])[1]):
        raise ValueError("The reported material interval omits a point of its affine domain")
    L=boundaries[-1];expected=[]
    if u[1]>=L[0] and s[0]<=C[1]:expected.append("central")
    if u[0]<=L[1] and s[1]>=C[0]:
        eu=(max(F(0),u[0]),min(u[1],L[1]))
        for i,branch in enumerate(AccurateRoundedEnd.pieces):
            if max(eu[0],boundaries[i][0])<=min(eu[1],boundaries[i+1][1]):
                expected.append(branch)
    rows=value["complete_material_piece_boxes"]
    if not expected or [row["branch"] for row in rows]!=expected:
        raise ValueError("The full reference requires every touching central and terminal piece")
    for row in rows:
        if row["branch"]=="central":
            lo,hi=_pair(row["accurate_inverse_t"]);vlo,vhi=_pair(row["positive_exact_speed"])
            mlo,mhi=_pair(row["clipped_central_material_interval"])
            if (not 0<=lo<=hi<=1 or not 0<vlo<=vhi
                    or mlo>max(F(0),min(s[0],C[0])) or mhi<min(s[1],C[1])
                    or row.get("root_identity_sha256")!=root_identity
                    or row.get("bound_field_scope")!=bound_field_scope
                    or row.get("accurate_phi_interval")!=encode(phi_interval)
                    or row.get("source_sha256")!=source_sha256
                    or row.get("mathematical_input_identity_sha256")!=mathematical_identity):
                raise ValueError("Keep the complete central inverse, scope and positive speed")
        else:
            index=AccurateRoundedEnd.pieces.index(row["branch"])
            a,b=_pair(row["backward_scalar_bounds"]["u"])
            if a>max(eu[0],boundaries[index][0]) or b<min(eu[1],boundaries[index+1][1]):
                raise ValueError("The terminal piece excludes part of its closed physical interval")
            for field in ("alpha","curvature","sine","cosine","x","h"):
                _pair(row["backward_scalar_bounds"][field])
    def enclose_rows(combined,vectors):
        if len(combined)!=3 or any(len(v)!=3 for v in vectors):
            raise ValueError("The complete piece hull needs three spatial components")
        for index,entry in enumerate(combined):
            lo,hi=_pair(entry)
            for vector in vectors:
                a,b=_pair(vector[index])
                if lo>a or hi<b:raise ValueError("The reported union omits a one-sided sixjet")
    for key in ("T0","T0_phi","T0_phiphi","T0_s"):
        enclose_rows(value[key],[row[key] for row in rows])
    for key in ("F","Fs","Fss","Fphi","Fsphi","Fphiphi"):
        enclose_rows(value["exact_reference_primitive_sixjets"][key],
            [row["exact_reference_primitive_sixjets"][key] for row in rows])
    for name in ("T0","T0_phi","T0_phiphi","T0_s"):
        if not isinstance(value[name],list) or len(value[name])!=3:
            raise ValueError("Every accurate reference vector has all three components")
        for entry in value[name]:_pair(entry)
    six=value["exact_reference_primitive_sixjets"]
    if set(six)!={"F","Fs","Fss","Fphi","Fsphi","Fphiphi"}:
        raise ValueError("The entire primitive physical sixjet is required")
    for row in six.values():
        if not isinstance(row,list) or len(row)!=3:raise ValueError("Keep complete physical vectors")
        for entry in row:_pair(entry)
    for name in ("material_and_angular_chain_order_complete","entire_original_material_interval_included",
                 "reference_only_not_current_corrected_normal_field"):
        if value.get(name) is not True:raise ValueError("The accurate full-domain scope changed")
    if (value.get("working_inverse_root_or_finite_difference_used_as_exact") is not False
            or value.get("original_working_reference_word_errors_compared") is not False):
        raise ValueError("Do not promote unproved working field arrays")
    return dict(root_identity_sha256=root_identity,
        current_full_point_sha256=bound_field_scope["current_full_point_sha256"],
        full_material_interval_bound=True,complete_reference_four_vectors_present=True,
        current_normal32_or_complete_corrected_field_not_certified_here=True)
