"""Explicit R172 last-cell completion on the accurate R171 metric domain.

The saved endpoint is a numerical label E, not the analytic physical cut S.
This is a new, explicitly bound finite representation.  Only the final raw
P1 cell and its scalar tail weight are pulled back by sigma; radius and K
are evaluated at physical s.  No old finite residual or body is transferred.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

import numpy as np
from flint import arb

from fd2d_gc_archive_arrays import load_npz, identity
from fd2d_gc_current_native_interval import (
    Jet, ProfileBox, aq, rational, rational_pair, interval, angle_interval,
    bound_record, hull_jets, jet_power, compose_R155, UnresolvedInterval)
from fd2d_gc_r136_arb_profile import R136ArbProfile, ends

SCHEMA = 'fd2d-accurate-last-P1-cell-physical-tail-v1'


def declared(saved, key):
    return json.loads(str(saved[key]))


class AccurateLastCell:
    """Interval consumer for the explicitly completed terminal cell.

    Inputs to box() are normalized accurate last-cell labels 0<=t<=1.
    The old coordinate sigma=b+(E-b)t is an exact rational at rational t;
    the physical coordinate is s=b+(S-b)t.  A cut query has angular jets
    only; it does not manufacture radial II derivatives.
    """
    def __init__(self, field_arrays, profile_packet, *, profile_sha256=None):
        self.field_path, self.packet_path = Path(field_arrays), Path(profile_packet)
        saved = load_npz(field_arrays)
        self.profile = R136ArbProfile.from_packet(profile_packet,
                                                   expected_sha256=profile_sha256)
        if identity(field_arrays)['sha256'] != self.profile.inputs['field_arrays']['sha256']:
            raise ValueError('Accurate profile and actual field must have identical input bytes')
        self.K = int(saved['modes']); self.e = self.K+1; self.d = 2*self.K+1
        counts = [int(saved[k]) for k in ('central_parameter_count','tail_parameter_count','profile_count')]
        self.mesh = tuple(rational(x) for x in saved['mesh'])
        self.raw = np.asarray(saved['corrections'])
        self.parameters = tuple(rational(x) for x in saved['parameters'])
        if (counts != [self.K,16,7] or self.raw.shape != (len(self.mesh),3*self.K+2)
                or not np.all(np.isfinite(self.raw)) or not np.all(self.raw[-1] == 0)):
            raise ValueError('Explicit actual layout and zero final correction are required')
        self.b, self.E = self.mesh[-2:]
        self.S = self.profile.end
        self.length = self.S-aq(self.b)
        if not self.length > 0:
            raise ValueError('Accurate last-cell width must be strictly positive')
        self.central = counts[0]
        self.tail = self.parameters[counts[0]:sum(counts[:2])]
        if not all(F(0) <= v <= F(6,5) for v in self.tail):
            raise ValueError('This version binds the original positive-control domain')
        seed = declared(saved,'seed_weight_definition')
        atlas = declared(saved,'angular_atlas_definition')
        gauss = declared(saved,'gauss_l_definition')
        terminal = declared(saved,'positive_trace_definition')
        protected = [seed['end'], atlas['exit_transition'][1],
                     gauss['support'][1], terminal['ramp_stop'],
                     float(np.max(saved['profile_supports'])),
                     float(np.asarray(saved['blend'])[-1])]
        if any(rational(v) >= self.b for v in protected):
            raise ValueError('The entire final cell must have identity atlas, no seed/coast/bumps, and trace weight one')
        if rational(terminal['cut']) != self.E:
            raise ValueError('The saved terminal label differs from the saved P1 endpoint')
        # Retain the actual scalar constants produced by the old evaluator.
        # Their exact sum is checked, not inferred from decimal .42+.58.
        self.weight_start = rational(float(.42*float(self.E)))
        self.weight_length = rational(float(.58*float(self.E)))
        if self.weight_start+self.weight_length != self.E or self.weight_start >= self.b:
            raise ValueError('This version requires the original scalar tail weight to attain exactly one at E')
        last = self.profile.pieces[-1]
        if not aq(self.b) > last['s0']:
            raise ValueError('The whole final raw cell must lie inside the accurate last profile piece')
        self.last_piece = last['index']
        self.c0 = tuple(rational(v) for v in self.raw[-2])
        self.inputs = dict(field_arrays=identity(field_arrays),profile_packet=identity(profile_packet),
                          source=identity(__file__))

    def definition(self):
        data = dict(schema=SCHEMA, inputs=self.inputs,
            physical_target_binding=self.profile.input_binding_sha256,
            saved_last_left=rational_pair(self.b),saved_endpoint_label=rational_pair(self.E),
            accurate_endpoint=bound_record(self.S),accurate_last_width=bound_record(self.length),
            accurate_minus_saved_endpoint=bound_record(self.S-aq(self.E)),
            coordinate='s=b+(S-b)*t; sigma=b+(E-b)*t; 0<=t<=1',
            raw='same saved last-cell Fourier coefficients, affine in t',
            tail_weight='original clipped S5((sigma-weight_start)/weight_length)',
            weight_start=rational_pair(self.weight_start),weight_length=rational_pair(self.weight_length),
            tail_geometry=dict(cut_radius='4/5',flat_radius='17/50',width='23/50',
                               controls='original sixteen exact binary64 rationals'),
            full_affine='raw(sigma,u)+eta(sigma)*T(a_accurate(s),u)',
            terminal='R155 positive trace using K_accurate(s); trace weight exactly one',
            identity_chart_on_entire_completed_cell=True,seed_coast_and_bumps_zero=True,
            old_array_bytes_changed=False,old_field_equal_on_completed_cell_claimed=False,
            physical_target_g_changed=False,old_finite_F_or_body_transferred=False,
            cut_radial_II_jets_assigned=False,whole_surface_certificate=False)
        data['binding_sha256'] = hashlib.sha256(json.dumps(data,sort_keys=True,
                                                     separators=(',',':')).encode()).hexdigest()
        return data

    def coordinates(self, lo, hi):
        lo,hi=map(rational,(lo,hi))
        if not 0 <= lo <= hi <= 1:
            raise ValueError('Use normalized labels in the accurate final cell')
        t=interval(lo,hi)
        return dict(t=t,s=aq(self.b)+self.length*t,
            sigma=interval(self.b+(self.E-self.b)*lo,self.b+(self.E-self.b)*hi),
            sigma_s=aq(self.E-self.b)/self.length)

    def raw_box(self, lo, hi, angular_lo, angular_hi, *, angle_unit='pi'):
        q=self.coordinates(lo,hi); angle=angle_interval(angular_lo,angular_hi,angle_unit)
        factor=1-q['t']; derivative=-1/self.length
        def series(offset,count,sine):
            out=[arb(0) for unused in range(5)]
            for j in range(count):
                k=j+1 if sine else j;f=2*k;sn,cs=(f*angle).sin_cos()
                basis,first=(sn,f*cs) if sine else (cs,-f*sn)
                v=aq(self.c0[offset+j]);c=factor*v;ds=derivative*v
                out[0]+=c*basis;out[1]+=ds*basis;out[2]+=c*first
                out[3]-=f*f*c*basis;out[4]+=ds*first
            return Jet(*out)
        return (series(0,self.e,False),series(self.e,self.K,True),series(self.d,self.e,False))

    def weight_box(self, lo, hi):
        q=self.coordinates(lo,hi)
        z=Jet((q['sigma']-aq(self.weight_start))/aq(self.weight_length),
              q['sigma_s']/aq(self.weight_length),arb(0),arb(0),arb(0))
        return jet_power(z,3)*(10-15*z+6*z.squared())

    def profile_box(self, lo, hi):
        lo,hi=map(rational,(lo,hi));q=self.coordinates(lo,hi)
        if lo == hi == 1:return self.profile.endpoint_jets()
        p=self.profile.pieces[self.last_piece]
        lower=ends((aq(self.b)+self.length*aq(lo)-p['s0'])/p['L'])[0]
        upper=ends((aq(self.b)+self.length*aq(hi)-p['s0'])/p['L'])[1]
        # The exact label t=1 is the accurate cut, even when its enclosure
        # has a tiny positive width.  Restriction to the actual piece is exact.
        return self.profile.piece_box(self.last_piece,max(F(0),lower),min(F(1),upper))

    def tail_shape_box(self, radius, angular_lo, angular_hi, *, angle_unit='pi'):
        angle=angle_interval(angular_lo,angular_hi,angle_unit)
        u=Jet(angle,arb(0),arb(1),arb(0),arb(0));sn,cs=u.sin(),u.cos()
        y=radius*sn;c=aq(F(17,50));w=aq(F(23,50));pieces=[]
        if not (y.value>c or y.value<-c):pieces.append(Jet.constant(0))
        for sign in (-1,1):
            z=(sign*y-c)/w;zl,zr=ends(z.value)
            if zr<=0:continue
            if zl>=1:pieces.append(Jet.constant(0));continue
            if zl<0 or zr>1:pieces.append(Jet.constant(0))
            v=Jet(interval(max(F(0),zl),min(F(1),zr)),z.s,z.xi,z.xixi,z.sxi)
            k=Jet.constant(0)
            for j,coefficient in enumerate(self.tail):
                k+=aq(F(630*comb(15,j),1)*coefficient/F(23,50))*jet_power(v,j+4)*jet_power(1-v,19-j)
            pieces.append(k)
        if not pieces:pieces=[Jet.constant(0)]
        k=hull_jets(pieces)
        return (k*cs.squared(),-k*sn*cs,k*sn.squared())

    def box(self, lo, hi, angular_lo, angular_hi, *, angle_unit='pi', include_terminal=True):
        lo,hi=map(rational,(lo,hi));p=self.profile_box(lo,hi)
        if lo == hi == 1:
            fields=self.tail_shape_box(Jet.constant(F(4,5)),angular_lo,angular_hi,angle_unit=angle_unit)
            return dict(fields=tuple(f.angular_only() for f in fields),profile=p,
                        cut=True,radial_II_jets_assigned=False)
        radius=Jet(p['a'],p['a_s'],arb(0),arb(0),arb(0))
        tail=self.tail_shape_box(radius,angular_lo,angular_hi,angle_unit=angle_unit)
        raw=self.raw_box(lo,hi,angular_lo,angular_hi,angle_unit=angle_unit)
        eta=self.weight_box(lo,hi)
        fields=tuple(r+eta*t for r,t in zip(raw,tail))
        if include_terminal:
            if hi==1:raise UnresolvedInterval('Use the proved endpoint value and separate one-sided bounds for a box touching degenerate K=0')
            K=ProfileBox(p['a'],p['a_s'],p['a_ss'],p['a_sss']).curvature_jet()
            fields=compose_R155(fields,Jet.constant(1),K)
        return dict(fields=fields,raw=raw,weight=eta,tail=tail,profile=p,
                    cut=False,radial_II_jets_assigned=True)

    def raw_coordinate_change_bounds(self):
        """Uniform common-physical-domain raw differences, orders u^0,u,u^2.

        Full-field differences additionally include the weight/tail and
        nonlinear map; these raw estimates are not a surface error claim.
        """
        difference=abs(self.S-aq(self.E))
        ratio=difference/abs(self.length)
        groups=((0,self.e,False),(self.e,self.K,True),(self.d,self.e,False))
        values=[]
        for offset,count,sine in groups:
            sums=[sum((abs(self.c0[offset+j])*(2*(j+1 if sine else j))**order
                       for j in range(count)),F(0)) for order in range(3)]
            values.append([ratio*aq(v) for v in sums])
        raw_frobenius=(values[0][0]**2+2*values[1][0]**2+values[2][0]**2).sqrt()
        weight_difference=aq(F(15,8))*difference/aq(self.weight_length)
        affine_frobenius=raw_frobenius+weight_difference*aq(F(4725,736))
        return dict(value_u_uu_by_n_m_l=values,
            exact_endpoint_shift= difference,
            delta_sigma_bound=difference,
            derivative_scale_change=abs(aq(self.E-self.b)/self.length-1),
            scalar_tail_weight_difference=weight_difference,
            affine_II_value_frobenius_bound=affine_frobenius,
            complete_positive_trace_II_value_frobenius_bound=arb(2).sqrt()*affine_frobenius,
            comparison='Original raw/weight coordinate with the same accurate g and R132 tail; not the old floating program',
            full_field_or_body_bound=False)
