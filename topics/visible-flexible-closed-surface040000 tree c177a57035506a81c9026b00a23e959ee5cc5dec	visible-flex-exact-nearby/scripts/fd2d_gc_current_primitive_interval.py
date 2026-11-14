"""R125 zero-end primitives for the current physical-s/ruling-atlas field.

The exact finite primitive is independent of a nonlinear solver. Its
coefficients are exact rational inputs, not a claimed approximation error.
Actual complete forcing-minus-polynomial and initial compatibility bounds
remain necessary. This module never substitutes a finite sample residual
or the old NativeLogField packet for those bounds.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json

from flint import arb

from fd2d_gc_current_native_interval import (
    aq, rational, rational_pair, interval, angle_interval, square,
    bound_record, require_positive, UnresolvedInterval)

SCHEMA='fd2d-current-R125-physical-s-zero-end-primitive-v1'


def _array3(values):
    result=tuple(tuple(tuple(rational(v) for v in row) for row in component)
                 for component in values)
    if len(result)!=3 or not result[0] or not result[0][0]:
        raise ValueError('Expected three vector components and positive radial/angular sizes')
    shape=(3,len(result[0]),len(result[0][0]))
    if any(len(component)!=shape[1] or any(len(row)!=shape[2] for row in component)
           for component in result):
        raise ValueError('All finite Fourier/polynomial coefficient shapes must agree')
    return result


def _encoded(values):
    return [[[rational_pair(v) for v in row] for row in component] for component in values]


def _horner(coefficients,t):
    answer=arb(0)
    for coefficient in reversed(coefficients):
        answer=answer*t+aq(coefficient)
    return answer


def _fourier_polynomial(cosine,sine,t,angle,angular_derivative=0):
    output=[]
    for ccomp,scomp in zip(cosine,sine):
        answer=arb(0)
        for mode in range(len(ccomp[0])):
            frequency=2*mode
            c=_horner([row[mode] for row in ccomp],t)
            s=_horner([row[mode] for row in scomp],t)
            sn,cs=(frequency*angle).sin_cos()
            if angular_derivative==0:
                answer+=c*cs+s*sn
            elif angular_derivative==1:
                answer+=frequency*(-c*sn+s*cs)
            else:
                raise ValueError('Only the actual primitive and its first angular derivative are needed')
        output.append(answer)
    return tuple(output)


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def norm_upper(vector):
    # The result is an outward Arb endpoint. No binary64 rounded norm is
    # fed back into a rigorous recurrence.
    return sum((square(x) for x in vector),arb(0)).sqrt().upper()


class ExactZeroEndPrimitive:
    """A physical-s cell polynomial P(t,xi), t=(s-left)/(right-left).

    Coefficient arrays have shape (3, radial_degree+1, angular_modes+1).
    The angular basis is cos(2*k*xi), sin(2*k*xi); sine k=0 must be zero.
    P approximates the COMPLETE connection vector (-a Rn,a Rm,-a G).
    The third component must not be silently discarded.
    """
    def __init__(self,left,right,cosine,sine,*,field_binding_sha256,provenance):
        self.left,self.right=map(rational,(left,right))
        if self.left>=self.right:
            raise ValueError('A primitive cell needs positive exact physical length')
        self.length=self.right-self.left
        self.cosine,self.sine=_array3(cosine),_array3(sine)
        shape=lambda a:(len(a),len(a[0]),len(a[0][0]))
        if shape(self.cosine)!=shape(self.sine):
            raise ValueError('Cosine and sine packets have different shapes')
        if any(row[0]!=0 for component in self.sine for row in component):
            raise ValueError('The unused sine zero mode must be exactly zero')
        if (not isinstance(field_binding_sha256,str) or len(field_binding_sha256)!=64
                or any(c not in '0123456789abcdef' for c in field_binding_sha256)):
            raise ValueError('An explicit actual interval-field binding is required')
        self.field_binding_sha256=field_binding_sha256
        self.provenance=dict(provenance)
        self.mean_cos,self.q_cos=self._primitive(self.cosine)
        self.mean_sin,self.q_sin=self._primitive(self.sine)
        self.exact_identities=self._identities()
        if not all(self.exact_identities.values()):
            raise ArithmeticError('The exact polynomial primitive identity failed')
        encoded=self.definition(include_hash=False)
        self.packet_sha256=hashlib.sha256(json.dumps(encoded,sort_keys=True,
            separators=(',',':')).encode()).hexdigest()

    def _primitive(self,values):
        means=[];primitives=[]
        for component in values:
            mean=tuple(sum((row[k]/(j+1) for j,row in enumerate(component)),F(0))
                       for k in range(len(component[0])))
            q=[[F(0) for unused in mean] for unused in range(len(component)+1)]
            for j,row in enumerate(component):
                for k,value in enumerate(row):
                    q[j+1][k]+=self.length*value/(j+1)
            for k,value in enumerate(mean):q[1][k]-=self.length*value
            means.append((mean,));primitives.append(tuple(tuple(row) for row in q))
        return tuple(means),tuple(primitives)

    def _identities(self):
        zero_left=zero_right=derivative=True
        for original,mean,q in ((self.cosine,self.mean_cos,self.q_cos),
                                (self.sine,self.mean_sin,self.q_sin)):
            for component,mcomp,qcomp in zip(original,mean,q):
                for k in range(len(component[0])):
                    zero_left &= qcomp[0][k]==0
                    zero_right &= sum((row[k] for row in qcomp),F(0))==0
                    for j,row in enumerate(component):
                        wanted=row[k]-(mcomp[0][k] if j==0 else 0)
                        derivative &= (j+1)*qcomp[j+1][k]/self.length==wanted
        return dict(q_left_exact_zero=bool(zero_left),q_right_exact_zero=bool(zero_right),
                    q_s_exact_P_minus_mean=bool(derivative),
                    angular_jet_of_zero_endpoint_exact_zero=bool(zero_left and zero_right))

    def definition(self,include_hash=True):
        packet=dict(schema=SCHEMA,field_binding_sha256=self.field_binding_sha256,
            left_exact=rational_pair(self.left),right_exact=rational_pair(self.right),
            coefficient_semantics='Exact rational finite polynomial in t, complete D2 cosine/sine vector in xi',
            cosine=_encoded(self.cosine),sine=_encoded(self.sine),
            mean_cosine=_encoded(self.mean_cos),mean_sine=_encoded(self.mean_sin),
            primitive_cosine=_encoded(self.q_cos),primitive_sine=_encoded(self.q_sin),
            exact_identities=self.exact_identities,provenance=self.provenance,
            actual_H_minus_P_bound_supplied=False,
            moving_chart_term='+(U_s/U_xi)*q_xi, at fixed physical material u',
            commutator_term='q cross alpha, alpha=(m,-l,0)',
            connection_vector='(-a*Rn,+a*Rm,-a*G)',
            continuous_global_certificate=False)
        if include_hash:packet['packet_sha256']=self.packet_sha256
        return packet

    def polynomial_boxes(self,radial_lo,radial_hi,angular_lo,angular_hi,*,angle_unit='pi'):
        lo,hi=map(rational,(radial_lo,radial_hi))
        if not self.left<=lo<=hi<=self.right:
            raise ValueError('The box must lie in this exact primitive cell')
        t=interval((lo-self.left)/self.length,(hi-self.left)/self.length)
        angle=angle_interval(angular_lo,angular_hi,angle_unit)
        P=_fourier_polynomial(self.cosine,self.sine,t,angle)
        mean=_fourier_polynomial(self.mean_cos,self.mean_sin,arb(0),angle)
        if lo==hi and lo in (self.left,self.right):
            q=qxi=(arb(0),arb(0),arb(0))
        else:
            q=_fourier_polynomial(self.q_cos,self.q_sin,t,angle)
            qxi=_fourier_polynomial(self.q_cos,self.q_sin,t,angle,1)
        return dict(P=P,mean=mean,q=q,q_xi=qxi,
                    q_s=tuple(a-b for a,b in zip(P,mean)),
                    exact_zero_endpoints=self.exact_identities)

    def conditional_box(self,connection,chart,radial_lo,radial_hi,angular_lo,angular_hi,
                        *,field_binding_sha256,angle_unit='pi',actual_H_minus_P=None):
        """Interval R125 algebra after the exact zero-end cancellation.

        A tighter independently proved H-P box can replace a direct
        subtraction. It must be for this complete forcing and this exact
        polynomial; its proof/identity belongs in the caller's certificate.
        """
        if field_binding_sha256!=self.field_binding_sha256:
            raise ValueError('The primitive belongs to a different actual saved field')
        p=self.polynomial_boxes(radial_lo,radial_hi,angular_lo,angular_hi,angle_unit=angle_unit)
        remainder=(tuple(a-b for a,b in zip(connection['h_vector'],p['P']))
                   if actual_H_minus_P is None else tuple(actual_H_minus_P))
        if len(remainder)!=3:
            raise ValueError('All three Maurer--Cartan forcing components are required')
        drift=chart.drift();commutator=cross(p['q'],connection['alpha'])
        E=tuple(mean+error+drift*angular+crosspart for mean,error,angular,crosspart in
                zip(p['mean'],remainder,p['q_xi'],commutator))
        return dict(E=E,E_norm_upper=norm_upper(E),
            Q_e1_norm_upper=norm_upper(p['q'][1:]),Q_norm_upper=norm_upper(p['q']),
            q=p['q'],q_xi=p['q_xi'],remainder=remainder,
            field_binding_sha256=self.field_binding_sha256,primitive_sha256=self.packet_sha256,
            physical_Us_term_included=True,Gauss_third_component_included=True,
            conditional_on_actual_complete_interval_inputs=True,
            continuous_global_certificate=False)


def propagate_piece_budget(length,d_left,k_left,E_upper,Qe1_upper,a_lower):
    """One R125 cell, conditional on valid complete bounds and initial data.

    Matrix skew symmetry, not an exponential Gronwall bound, propagates the
    defect. Each exact-zero primitive vanishes at both cell ends.
    """
    h=aq(length)
    if not h>0 or not a_lower>0:
        raise ValueError('A positive physical cell length and actual radius lower bound are needed')
    if any(not q>=0 for q in (d_left,k_left,E_upper,Qe1_upper)):
        raise ValueError('Budget inputs must be nonnegative outward bounds')
    d_right=(d_left+h*E_upper).upper()
    k_right=(k_left+h*d_left+h*h*E_upper/2+h*Qe1_upper).upper()
    ratio=k_right/a_lower
    metric=(2*ratio+ratio*ratio).upper()
    return dict(d_right=d_right,k_right=k_right,relative_metric_upper=metric,
        conditional_on_complete_piece_and_initial_bounds=True,
        initial_compatibility_paid_by_this_function=False,continuous_global_certificate=False)
