"""Thin exact-input interval pieces for the current independent-tail field.

This is not a complete interval evaluator for the affine seed/reference/tail
lifting, the base phase profile, or the ruling atlas.  Those unpaid inputs
are deliberately explicit in ``definition``.  The module supplies the
actual saved P1/Fourier correction, compact physical bumps, declared scalar
weights, the exact cut angular trace, and conditional interval jet algebra
for R153/R155 and the physical Gauss--Codazzi residual.  No floating point
sample is promoted to a continuous enclosure.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

import numpy as np
from flint import arb

from fd2d_gc_archive_arrays import identity
from fd2d_gc_independent_tail_native_field import IndependentTailPositiveTraceNativeField

SCHEMA = 'fd2d-current-independent-tail-interval-pieces-v1'


class UnresolvedInterval(ValueError):
    """A box needs subdivision or an unpaid ingredient; not a bad-field witness."""


def rational(value):
    if isinstance(value, F):
        return value
    if isinstance(value, (float, np.floating)):
        return F.from_float(float(value))
    if isinstance(value, (int, np.integer)):
        return F(int(value))
    return F(value)


def rational_pair(value):
    q = rational(value)
    return [str(q.numerator), str(q.denominator)]


def aq(value):
    q = rational(value)
    return arb(q.numerator)/q.denominator


def interval(lo, hi):
    lo, hi = rational(lo), rational(hi)
    if lo > hi:
        raise ValueError('Interval endpoints are reversed')
    return aq(lo).union(aq(hi))


def angle_interval(lo, hi, unit='pi'):
    q = interval(lo, hi)
    if unit == 'pi':
        return arb.pi()*q
    if unit == 'radians':
        return q
    raise ValueError('Angle units are exact multiples of pi or exact rational radians')


def power(value, degree):
    """Integer multiplication only; Arb generic real powers across zero are avoided."""
    if degree < 0 or int(degree) != degree:
        raise ValueError('Expected a nonnegative integer power')
    result = arb(1)
    for unused in range(int(degree)):
        result *= value
    return result


def square(value):
    if value >= 0 or value <= 0:
        return value*value
    end = abs(value).upper()
    return arb(0).union(end*end)


def bound_record(value):
    if value is None:
        return None
    if not value.is_finite():
        raise UnresolvedInterval('A finite interval was not obtained')
    def binary(x):
        mantissa, exponent = x.man_exp()
        return [str(mantissa), int(exponent)]
    return dict(lower_binary=binary(value.lower()), upper_binary=binary(value.upper()),
                lower_display=float(value.lower()), upper_display=float(value.upper()))


def require_positive(value, name):
    if not value > 0:
        raise UnresolvedInterval(name+' has no strictly positive lower enclosure')


def _add(a, b):
    return None if a is None or b is None else a+b


def _sum_products(*pairs):
    if any(a is None or b is None for a, b in pairs):
        return None
    return sum((a*b for a, b in pairs), arb(0))


@dataclass(frozen=True)
class Jet:
    """Scalar native jet in physical s and computational xi, one radial side.

    Missing s/sxi remain missing.  Angular-only cut data cannot accidentally
    acquire a zero radial derivative by an algebraic operation.
    """
    value: arb
    s: arb | None = None
    xi: arb | None = None
    xixi: arb | None = None
    sxi: arb | None = None

    @staticmethod
    def constant(value):
        v = value if isinstance(value, arb) else aq(value)
        return Jet(v, arb(0), arb(0), arb(0), arb(0))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Jet) else Jet.constant(value)

    def __add__(self, other):
        q = Jet.coerce(other)
        return Jet(self.value+q.value, _add(self.s,q.s), _add(self.xi,q.xi),
                   _add(self.xixi,q.xixi), _add(self.sxi,q.sxi))

    __radd__ = __add__

    def __neg__(self):
        return Jet(*(-v if v is not None else None for v in
                     (self.value,self.s,self.xi,self.xixi,self.sxi)))

    def __sub__(self, other):
        return self+-Jet.coerce(other)

    def __rsub__(self, other):
        return Jet.coerce(other)+-self

    def __mul__(self, other):
        q = Jet.coerce(other)
        return Jet(self.value*q.value,
            _sum_products((self.s,q.value),(self.value,q.s)),
            _sum_products((self.xi,q.value),(self.value,q.xi)),
            _sum_products((self.xixi,q.value),(2*self.xi if self.xi is not None else None,q.xi),
                          (self.value,q.xixi)),
            _sum_products((self.sxi,q.value),(self.s,q.xi),(self.xi,q.s),(self.value,q.sxi)))

    __rmul__ = __mul__

    def unary(self, value, first, second):
        return Jet(value,
            None if self.s is None else first*self.s,
            None if self.xi is None else first*self.xi,
            None if self.xi is None or self.xixi is None else second*square(self.xi)+first*self.xixi,
            None if self.s is None or self.xi is None or self.sxi is None
                else second*self.s*self.xi+first*self.sxi)

    def reciprocal(self):
        if not (self.value > 0 or self.value < 0):
            raise UnresolvedInterval('A quotient denominator box contains zero')
        inv = 1/self.value
        return self.unary(inv,-inv*inv,2*inv*inv*inv)

    def __truediv__(self, other):
        return self*Jet.coerce(other).reciprocal()

    def __rtruediv__(self, other):
        return Jet.coerce(other)*self.reciprocal()

    def squared(self):
        # A tighter nonnegative value enclosure, with the same exact jet.
        product = self*self
        return Jet(square(self.value),product.s,product.xi,product.xixi,product.sxi)

    def sqrt(self):
        require_positive(self.value,'square-root radicand')
        root = self.value.sqrt()
        return self.unary(root,1/(2*root),-1/(4*root*root*root))

    def sin(self):
        sn, cs = self.value.sin_cos()
        return self.unary(sn,cs,-sn)

    def cos(self):
        sn, cs = self.value.sin_cos()
        return self.unary(cs,-sn,-cs)

    def angular_only(self):
        return Jet(self.value,None,self.xi,self.xixi,None)

    def record(self):
        return {name:bound_record(getattr(self,name)) for name in
                ('value','s','xi','xixi','sxi')}


def jet_power(value, degree):
    result = Jet.constant(1)
    for unused in range(degree):
        result = result*value
    return result


def hull_jets(jets):
    jets = list(jets)
    if not jets:
        raise ValueError('No boxes to enclose')
    def one(name):
        items = [getattr(q,name) for q in jets]
        if any(q is None for q in items):
            return None
        result = items[0]
        for q in items[1:]:
            result = result.union(q)
        return result
    return Jet(*(one(k) for k in ('value','s','xi','xixi','sxi')))


def step5_jet(lo, hi, start, stop):
    """Continuous value/first derivative of the exact clipped quintic weight."""
    lo, hi, start, stop = map(rational,(lo,hi,start,stop))
    if lo > hi or start >= stop:
        raise ValueError('Invalid radial box or quintic support')
    if hi <= start:
        return Jet.constant(0)
    if lo >= stop:
        return Jet.constant(1)
    tl, tr = max(F(0),(lo-start)/(stop-start)), min(F(1),(hi-start)/(stop-start))
    t = interval(tl,tr)
    def exact_step(q):
        return q*q*q*(10-15*q+6*q*q)
    # Monotonicity gives the value hull, avoiding a wide dependency bound.
    value = interval(exact_step(tl),exact_step(tr))
    derivative = 30*square(t)*square(1-t)/aq(stop-start)
    if lo < start or hi > stop:
        derivative = derivative.union(arb(0))
    return Jet(value,derivative,arb(0),arb(0),arb(0))


def reflected_step5_jet(lo, hi, exit_point, rim):
    q = step5_jet(-rational(hi),-rational(lo),-rational(exit_point),
                  -rational(exit_point)+rational(rim))
    return Jet(q.value,-q.s,q.xi,q.xixi,q.sxi)


def compose_R153(fields, weight, K):
    """Conditional exact R153 jet algebra; no sampled n floor is a proof."""
    n,m,l = fields
    if weight.value.is_zero() and weight.s is not None and weight.s.is_zero():
        return tuple(fields)
    require_positive(n.value,'R153 active n')
    changed_l = (1-weight)*l+weight*(K+m.squared())/n
    return n,m,changed_l


def compose_R155(fields, weight, K):
    """Interior R155 algebra only.  Exact cut uses its separate tail method."""
    n,m,l = fields
    if weight.value.is_zero() and weight.s is not None and weight.s.is_zero():
        return tuple(fields)
    if not K.value >= 0:
        raise UnresolvedInterval('Active terminal K has no nonnegative enclosure')
    h = ((n-l).squared()+4*m.squared()+4*K).sqrt()
    increment = weight*(h-n-l)/2
    return n+increment,m,l+increment


@dataclass(frozen=True)
class ProfileBox:
    a: arb
    a_s: arb
    a_ss: arb
    a_sss: arb | None = None

    def curvature_jet(self):
        require_positive(self.a,'physical radius a')
        K = -self.a_ss/self.a
        Ks = (None if self.a_sss is None else
              -self.a_sss/self.a+self.a_ss*self.a_s/(self.a*self.a))
        return Jet(K,Ks,arb(0),arb(0),arb(0) if Ks is not None else None)


@dataclass(frozen=True)
class ChartBox:
    U_xi: arb
    U_s: arb
    U_xixi: arb | None = None
    U_sxi: arb | None = None

    def drift(self):
        require_positive(self.U_xi,'actual chart U_xi')
        return self.U_s/self.U_xi


def physical_jet(field, chart):
    """True material derivatives from native jets, including the U_s drift."""
    h, v = chart.U_xi, chart.drift()
    fu = None if field.xi is None else field.xi/h
    fs = None if field.s is None or field.xi is None else field.s-v*field.xi
    fuu = (None if fu is None or field.xixi is None or chart.U_xixi is None
           else (field.xixi-fu*chart.U_xixi)/(h*h))
    fsu = (None if field.sxi is None or field.xixi is None or field.xi is None
           or chart.U_xixi is None or chart.U_sxi is None else
           (field.sxi-v*field.xixi)/h-field.xi*(chart.U_sxi-v*chart.U_xixi)/(h*h))
    return dict(value=field.value,s=fs,u=fu,uu=fuu,su=fsu)


def connection_box(fields, profile, chart):
    """R119 full SO(3) forcing. Caller must supply actual continuous boxes.

    n_s,m_s,l_u suffice; l_s is not requested. The third vector component
    carries the actual Gauss defect rather than silently imposing Gauss.
    """
    require_positive(profile.a,'physical radius a')
    n,m,l = [physical_jet(q,chart) for q in fields]
    if any(q is None for q in (n['s'],m['s'],m['u'],l['u'])):
        raise UnresolvedInterval('Actual n_s,m_s,m_u,l_u boxes have not all been supplied')
    a, c = profile.a, profile.a_s/profile.a
    G = l['value']*n['value']-square(m['value'])+profile.a_ss/a
    Rn = n['s']-m['u']/a-c*(l['value']-n['value'])
    Rm = m['s']-l['u']/a+2*c*m['value']
    return dict(G=G,Rn=Rn,Rm=Rm,
        h_vector=(-a*Rn,a*Rm,-a*G),alpha=(m['value'],-l['value'],arb(0)),
        physical_fields=(n,m,l),physical_metric_coordinates='s,u',
        complete_field_enclosures_are_caller_obligations=True,
        continuous_global_certificate=False)


class CurrentNativeIntervalPieces:
    """Binds the complete unchanged native definition and exact raw inputs.

    The existing reader validates the actual declared native family. It is
    not called for numerical value samples by any interval method below.
    """
    def __init__(self, definition_path):
        self.definition_path = Path(definition_path)
        self.original_definition = json.loads(self.definition_path.read_text())
        self.reader = IndependentTailPositiveTraceNativeField.from_definition(self.definition_path)
        r = self.reader
        self.mesh = tuple(rational(v) for v in r.nodes)
        self.K, self.e, self.d = r.K, r.e, r.d
        self.coefficients = r.values
        self.parameters = tuple(rational(v) for v in r.parameters)
        self.profile_supports = tuple(tuple(rational(v) for v in row) for row in r.profile.supports)
        self.layout = r.explicit_parameter_layout
        self.entry, self.exit = map(rational,r.gauss_l_definition['support'])
        self.length = rational(r.coast_reference.length)
        self.rim = rational(float(r.coast_reference.length*r.reference_rim_fraction))
        self.trace_start,self.trace_stop,self.cut = (rational(r.positive_trace_definition[k])
                                                   for k in ('start','ramp_stop','cut'))
        self.tail_radius = rational(r.tail.cut_radius)
        self.tail_flat = rational(r.tail.flat_radius)
        self.tail_width = rational(r.tail.width)
        self._cell_cache = {}
        binding = dict(schema=SCHEMA, native_definition_identity=identity(self.definition_path),
            arrays_identity=identity(r.arrays_path), interval_source=identity(__file__),
            parameter_layout=self.layout, mesh_exact=[rational_pair(v) for v in self.mesh])
        self.binding_sha256 = hashlib.sha256(json.dumps(binding,sort_keys=True,
            separators=(',',':')).encode()).hexdigest()
        self.binding = binding

    def definition(self):
        return dict(schema=SCHEMA,binding_sha256=self.binding_sha256,binding=self.binding,
            original_native_definition=self.original_definition,
            exact_input_semantics='Saved binary64 knots, Fourier coefficients and parameters are exact dyadic inputs; arithmetic evaluation is enclosed with Arb.',
            current_coordinate='physical s=x; native angle xi is the full saved ruling atlas',
            exact_parameter_layout=self.layout,angular_modes=self.K,
            coast_rim_exact=rational_pair(self.rim),
            coast_exit_minus_entry_minus_length_exact=rational_pair(self.exit-self.entry-self.length),
            available_interval_parts=['complete saved raw P1 Fourier value/s/xi/xixi/sxi',
                'declared scalar quintic windows', 'physical compact bump increments through derivative 3',
                'accurate cut positive-Bernstein angular value and first/second angular jets',
                'conditional actual R153/R155 jet composition',
                'conditional material-u transformation and all three R119 defects'],
            unpaid_interval_parts=['full affine central/reference/tail lifting away from the cut',
                'base phase-profile values/integrals and all physical a jets',
                'complete ruling/transition atlas U_xi,U_s and required angular jets',
                'R155 one-sided degenerate cut derivative boxes',
                'actual forcing polynomial remainder for each R125 primitive cell',
                'initial frame/position compatibility and final complete posterior'],
            old_NativeLogField_interval_reused_as_current=False,
            field_changed=False,physical_g_changed=False,mesh_changed=False,
            continuous_global_certificate=False)

    def structural_partition(self):
        """Exact saved mesh and known representation boundaries, with names.

        This does not claim all internal phase-polynomial breakpoints are
        included. A future base-profile interval packet adds its own splits.
        """
        records = {}
        def add(q,label):
            q=rational(q)
            if self.mesh[0] <= q <= self.mesh[-1]:
                records.setdefault(q,[]).append(label)
        for j,q in enumerate(self.mesh):add(q,'saved_node_'+str(j))
        for j,pair in enumerate(self.profile_supports):
            for k,q in enumerate(pair):add(q,'bump_%d_%d'%(j,k))
        for key in ('start','end'):
            add(self.reader.seed_weight_definition[key],'seed_'+key)
        for key in ('entry_transition','coast','exit_transition'):
            for j,q in enumerate(self.reader.angular_atlas_definition[key]):add(q,'atlas_'+key+'_'+str(j))
        for j,q in enumerate(self.reader.blend_interval):add(q,'original_blend_'+str(j))
        for q,label in ((self.entry,'coast_entry'),(self.entry+self.rim,'exact_left_plateau'),
                        (self.exit-self.rim,'exact_right_plateau'),(self.exit,'coast_exit'),
                        (self.trace_start,'terminal_start'),(self.trace_stop,'terminal_ramp_stop'),
                        (self.cut,'accurate_cut')):add(q,label)
        for j,q in enumerate(self.reader.gauss_l_definition['gauss_plateau']):add(q,'stored_plateau_'+str(j))
        return dict(points=[dict(exact=rational_pair(q),labels=records[q]) for q in sorted(records)],
                    includes_saved_mesh_and_representation_boundaries=True,
                    base_profile_internal_analytic_pieces_complete=False)

    def _cell(self, cell):
        cell=int(cell)
        if not 0 <= cell < len(self.mesh)-1:
            raise ValueError('Cell index is outside the actual saved mesh')
        if cell not in self._cell_cache:
            left,right=self.mesh[cell:cell+2]
            c0=tuple(rational(v) for v in self.coefficients[cell])
            c1=tuple(rational(v) for v in self.coefficients[cell+1])
            slope=tuple((b-a)/(right-left) for a,b in zip(c0,c1))
            if len(self._cell_cache)>=8:self._cell_cache.pop(next(iter(self._cell_cache)))
            self._cell_cache[cell]=(left,right,c0,c1,slope)
        return self._cell_cache[cell]

    def raw_box(self, cell, radial_lo, radial_hi, angular_lo, angular_hi, *, angle_unit='pi'):
        left,right,c0,unused,slope=self._cell(cell)
        lo,hi=map(rational,(radial_lo,radial_hi))
        if not left <= lo <= hi <= right:
            raise ValueError('Use one explicitly selected original P1 cell, including its one-sided endpoints')
        angle=angle_interval(angular_lo,angular_hi,angle_unit)
        coeff=[interval(a+(lo-left)*v,a+(hi-left)*v) if v>=0 else
               interval(a+(hi-left)*v,a+(lo-left)*v) for a,v in zip(c0,slope)]
        ds=list(map(aq,slope))
        def series(offset,count,sine):
            out=[arb(0) for unused in range(5)]
            for j in range(count):
                k=j+1 if sine else j
                f=2*k;sn,cs=(f*angle).sin_cos()
                basis,derivative=(sn,f*cs) if sine else (cs,-f*sn)
                c,v=coeff[offset+j],ds[offset+j]
                out[0]+=c*basis;out[1]+=v*basis;out[2]+=c*derivative
                out[3]-=f*f*c*basis;out[4]+=v*derivative
            return Jet(*out)
        return dict(fields=(series(0,self.e,False),series(self.e,self.K,True),series(self.d,self.e,False)),
            field_order=('n','m','l'),scope='raw correction only, not complete actual field',
            binding_sha256=self.binding_sha256,cell=int(cell),
            radial_exact=[rational_pair(lo),rational_pair(hi)],
            angular_exact=[rational_pair(angular_lo),rational_pair(angular_hi)],angle_unit=angle_unit,
            radial_derivative_side='selected saved cell; no average of adjacent P1 slopes',
            all_saved_angular_modes_included=True)

    def scalar_weights(self, lo, hi):
        seed=self.reader.seed_weight_definition
        coast=step5_jet(lo,hi,self.entry,self.entry+self.rim)*reflected_step5_jet(lo,hi,self.exit,self.rim)
        return dict(seed=1-step5_jet(lo,hi,seed['start'],seed['end']),coast=coast,
                    terminal=step5_jet(lo,hi,self.trace_start,self.trace_stop))

    def bump_increments(self, lo, hi, derivative_order=3):
        lo,hi=map(rational,(lo,hi))
        if lo>hi or not 0<=int(derivative_order)<=3:
            raise ValueError('Use an ordered physical interval and derivatives 0 through 3')
        deltas=self.parameters[self.reader.profile_parameter_slice]
        answer=[arb(0) for unused in range(int(derivative_order)+1)]
        for delta,(left,right) in zip(deltas,self.profile_supports):
            if delta==0 or hi<=left or lo>=right:continue
            width=right-left
            t=interval(max(F(0),(lo-left)/width),min(F(1),(hi-left)/width))
            for d in range(len(answer)):
                value=arb(0)
                for k in range(d+1):
                    j=d-k
                    factor=comb(d,k)*factorial(5)//factorial(5-k)
                    factor*=((-1)**j)*factorial(5)//factorial(5-j)
                    value+=factor*power(t,5-k)*power(1-t,5-j)
                value*=aq(1024*delta/(width**d))
                if lo<left or hi>right:value=value.union(arb(0))
                answer[d]+=value
        return dict(increments=tuple(answer),scope='compact physical bumps only; base a not enclosed',
                    exact_support_differences=True,binding_sha256=self.binding_sha256)

    def exact_cut_angular_box(self, angular_lo, angular_hi, *, angle_unit='pi'):
        """Entire positive-tail angular trace, including kappa=0 arcs.

        No radial II derivative is returned. This is the saved exact cut
        bypass only, not an interior-to-cut regularity proof for R155.
        """
        if max(self.reader.blend_interval[1],self.reader.angular_atlas_definition['exit_transition'][1])>=float(self.cut):
            raise ValueError('The saved cut chart must be the material identity on a neighborhood')
        if not np.all(self.reader.values[-1]==0):
            raise ValueError('Accurate tail trace requires saved cut correction exactly zero')
        angle=angle_interval(angular_lo,angular_hi,angle_unit)
        u=Jet(angle,None,arb(1),arb(0),None)
        sn,cs=u.sin(),u.cos()
        y=aq(self.tail_radius)*sn
        radius=aq(self.tail_flat);width=aq(self.tail_width)
        controls=self.parameters[self.reader.tail_parameter_slice]
        degree=len(controls)-1
        pieces=[]
        if not (y.value>radius or y.value<-radius):
            pieces.append(Jet(arb(0),None,arb(0),arb(0),None))
        for sign in (-1,1):
            absolute=sign*y.value
            if absolute.upper()<=radius.lower():continue
            raw=(absolute-radius)/width
            low=max(arb(0),raw.lower());high=min(arb(1),raw.upper())
            if low>high:
                pieces.append(Jet(arb(0),None,arb(0),arb(0),None));continue
            # Only the value is restricted to the relevant branch; complete
            # angle derivative boxes remain valid, albeit sometimes wider.
            q=Jet(low.union(high),None,sign*y.xi/width,sign*y.xixi/width,None)
            kappa=Jet.constant(0).angular_only()
            for j,coefficient in enumerate(controls):
                kappa+=aq(630*comb(degree,j)*coefficient/self.tail_width)*jet_power(q,j+4)*jet_power(1-q,degree-j+4)
            pieces.append(kappa)
            if raw.upper()>1:pieces.append(Jet(arb(0),None,arb(0),arb(0),None))
        kappa=hull_jets(pieces)
        fields=(kappa*cs.squared(),-kappa*sn*cs,kappa*sn.squared())
        return dict(fields=fields,field_order=('n','m','l'),binding_sha256=self.binding_sha256,
            scope='complete accurate cut angular trace only',chart='u=xi',cut_exact=rational_pair(self.cut),
            radial_II_derivatives_assigned=False,interior_R155_cut_limit_certified=False,
            continuous_angular_box=True)
