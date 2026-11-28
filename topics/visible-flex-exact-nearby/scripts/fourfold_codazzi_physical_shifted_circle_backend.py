"""Complete old-circle primitives on a physical carrier and an independent rank block.

Every unknown analytic remainder is retained on the original GLW strip.
The primitive uses its actual physical Fourier label, not the input label.
Scientific invocation belongs to a new public Actions owner.
"""
from fractions import Fraction as Q
from flint import acb,arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_collar_signed_laurent_enclosure import Field,WIDTH,DEGREE
from fourfold_codazzi_true_phase_original_inputs import check


def disk_rectangle(radius):
    r=arb(radius).upper()
    check(r.is_finite() and r>=0,"complete analytic error radius")
    return acb(arb(0,r),arb(0,r))


class Column:
    """exp(4 i sign j phi)*oscillatory + physical, on one complete input band."""
    __slots__=("oscillatory","physical","mean_zero")

    def __init__(self,oscillatory,physical=None,mean_zero=False):
        check(isinstance(oscillatory,Field),"complete shifted amplitude field")
        if physical is None:physical=Field.scalar(0)
        check(isinstance(physical,Field),"complete unshifted physical rank field")
        self.oscillatory,self.physical,self.mean_zero=oscillatory,physical,bool(mean_zero)


class Backend:
    def __init__(self,lo,hi,sign):
        check(type(lo) is int and type(hi) is int and 97<=lo<=hi and sign in (-1,1),
              "actual positive input labels and original frequency sign")
        check(lo==hi or lo>DEGREE,"every possible exceptional physical zero has its own complete label")
        self.lo,self.hi,self.sign=lo,hi,sign
        self.primitive_remainder=(arb.pi()/8).upper()
        self.mean_remainder=(-4*exact(WIDTH)*lo).exp().upper()

    def constant(self,a):return Field.scalar(a)

    def add(self,*xs):
        check(bool(xs),"nonempty signed addition")
        if isinstance(xs[0],Column):
            check(all(isinstance(x,Column) for x in xs),"matching physical column types")
            o=sum((x.oscillatory for x in xs),Field.scalar(0))
            p=sum((x.physical for x in xs),Field.scalar(0))
            return Column(o,p,all(x.mean_zero for x in xs))
        check(not any(isinstance(x,Column) for x in xs),"matching scalar or coefficient types")
        return sum(xs)

    def scale(self,a,x):
        if isinstance(x,Column):
            return Column(x.oscillatory.scale(a),x.physical.scale(a),x.mean_zero)
        if isinstance(x,Field):return x.scale(a)
        return a*x

    def coeff_Pi(self,f):
        check(isinstance(f,Field),"physical coefficient mean")
        return f.coeff(0)+disk_rectangle(f.error)

    def coeff_P(self,f):return f-Field.scalar(self.coeff_Pi(f))

    def real_ball(self,value):
        z=acb(value)
        check(z.is_finite() and z.imag.contains(0),"independently qualified real physical scalar")
        return z.real

    def coeff_exp(self,f):
        # Field.exponential includes its whole positive Taylor remainder.
        return f.exponential()

    def _primitive_field(self,f,shifted):
        values=[]
        for h,z in enumerate(f.p,f.lo):
            if shifted:
                lower=min(self.sign*self.lo+h,self.sign*self.hi+h)
                upper=max(self.sign*self.lo+h,self.sign*self.hi+h)
            else:lower=upper=h
            if lower==upper==0:
                values.append(acb(0))
                continue
            check(lower>0 or upper<0,"zero-free physical primitive band or a removed exact zero")
            k=arb(lower).union(arb(upper))
            values.append(z/acb(0,4*k))
        # Conjugating the real sawtooth convolution multiplies its kernel
        # by a unit-modulus input phase. Its strip-sup norm is still pi/8.
        return Field(f.lo,values,f.error*self.primitive_remainder)

    def coeff_I(self,f):return self._primitive_field(f,False)

    def coeff_T(self,f,g):return self.coeff_P(f*self.coeff_P(g))

    def Pi(self,x):
        check(isinstance(x,Column),"mean of the complete physical column")
        if x.mean_zero:return acb(0)
        a=x.oscillatory
        finite=a.coeff(-self.sign*self.lo) if self.lo==self.hi else acb(0)
        return self.coeff_Pi(x.physical)+finite+disk_rectangle(a.error*self.mean_remainder)

    def P(self,x):
        if x.mean_zero:return x
        return Column(x.oscillatory,x.physical-Field.scalar(self.Pi(x)),True)

    def I(self,x):
        return Column(self._primitive_field(x.oscillatory,True),
                      self._primitive_field(x.physical,False),True)

    def mul(self,f,x):
        check(isinstance(f,Field) and isinstance(x,Column),"coefficient before the full physical column")
        return Column(f*x.oscillatory,f*x.physical)

    def T(self,f,x):return self.P(self.mul(f,self.P(x)))

    def rank_vector(self,f,mean):
        # The coefficient has physical output labels h, independently of j.
        # It must not be stored as a constant multiplying the oscillatory block.
        return Column(Field.scalar(0),f.scale(mean))

    def R(self,f,g,x):
        return self.P(self.rank_vector(f,self.Pi(self.mul(g,self.P(x)))))

    def partial(self,x):
        """Only finite trials can be differentiated without a further strip loss.

        No derivative of an unknown analytic remainder is manufactured.
        The full explicit JI inverse does not call this operation.
        """
        check(x.oscillatory.error==0 and x.physical.error==0,
              "only a whole finite trial, or separately proved derivative jets")
        fields=[]
        for shifted,f in ((True,x.oscillatory),(False,x.physical)):
            values=[]
            for h,z in enumerate(f.p,f.lo):
                k=arb(self.sign*self.lo+h).union(arb(self.sign*self.hi+h)) if shifted else arb(h)
                values.append(z*acb(0,4*k))
            fields.append(Field(f.lo,values))
        return Column(*fields,mean_zero=True)

    def finite_trial(self,x):
        """One possible finite dyadic proposal; subsequent q,p remain mandatory.

        It does not solve or certify any original inverse. A public owner
        must persist and read back these exact coefficients before using it.
        """
        def midpoint(f):
            return Field(f.lo,[acb(z.real.mid(),z.imag.mid()) for z in f.p])
        return self.P(Column(midpoint(x.oscillatory),midpoint(x.physical)))
