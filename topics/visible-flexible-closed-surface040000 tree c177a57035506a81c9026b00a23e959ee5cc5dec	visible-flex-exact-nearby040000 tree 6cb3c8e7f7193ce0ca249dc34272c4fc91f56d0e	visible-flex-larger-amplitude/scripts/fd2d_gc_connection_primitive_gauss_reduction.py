"""Same exact R180 primitive, with the third component combined first.

No field function is reevaluated or changed.  For q=v-L and
v=(-a*n,a*m,0), alpha=(m,-l,0),

  -a*G + (q cross alpha)_3
       = -a_ss + L_1*l + L_2*m.

Both genuine enclosures are intersected; the full Gauss contribution is
preserved algebraically, not dropped as a solver constraint.
"""
from __future__ import annotations
from pathlib import Path

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_primitive_interval_v2 import norm_upper

PARENT_SHA256='2a5f3e966751f787ce53bb7ee420cfc3480be78e925fe16ab203965a15f3931b'


def reduce_gauss_component(packet):
    parent=identity(Path(__file__).with_name('fd2d_gc_connection_endpoint_primitive.py'))
    if parent['sha256']!=PARENT_SHA256:
        raise ValueError('The full endpoint primitive definition changed')
    if (not packet.get('complete_actual_endpoint_functions_used')
            or packet.get('radial_derivatives_n_s_m_s_used_by_E') is not False
            or not packet['endpoint_linear'][2].is_zero()):
        raise ValueError('Supply an actual complete R180 endpoint primitive packet')
    actual=packet['actual'];profile=actual['profile']
    unused,m,l=actual['fields']
    L1,L2,unused=packet['endpoint_linear']
    reduced=-profile.a_ss+L1*l.value+L2*m.value
    original=packet['E'][2]
    lo=max(original.lower(),reduced.lower())
    hi=min(original.upper(),reduced.upper())
    if lo>hi:
        raise ArithmeticError('Two exact algebraic enclosures of the same E3 are disjoint')
    enclosure=lo.union(hi)
    out=dict(packet)
    out['E']=(packet['E'][0],packet['E'][1],enclosure)
    out['E_norm_upper']=norm_upper(out['E'])
    out.update(enclosure_source=identity(__file__),parent_formula_source=parent,
        original_E3_enclosure=original,combined_E3_enclosure=reduced,
        combined_E3_formula='-a_ss+(L_v)_1*l+(L_v)_2*m',
        full_Gauss_contribution_retained_algebraically=True,
        same_primitive_and_mathematical_E=True,
        point_or_interval_field_reevaluated=False)
    return out


__all__=['reduce_gauss_component']
