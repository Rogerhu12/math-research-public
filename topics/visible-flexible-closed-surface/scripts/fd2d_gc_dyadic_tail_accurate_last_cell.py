"""R172 accurate last cell with the explicit, larger R170 tail domain.

This is a new constructor and schema. The closed original constructor is
never called with changed or synthetic controls. All interval evaluation
methods are inherited verbatim from its bound source; they evaluate the
same full polynomial and do not require global control coefficients to
be nonnegative. The physical profile must bind these actual field bytes.
"""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

import numpy as np

from fd2d_gc_archive_arrays import load_npz, identity
from fd2d_gc_current_native_interval import aq, rational
from fd2d_gc_accurate_last_cell import AccurateLastCell, declared
from fd2d_gc_r136_arb_profile import R136ArbProfile, ends
from fd2d_dyadic_bernstein_tail import DyadicBernsteinControlBox
from fd2d_gc_dyadic_tail_problem import (
    tail_search_domain_definition, DOMAIN_KIND)
from fd2d_gc_terminal_angular_majorant import terminal_angular_majorant

HERE=Path(__file__).resolve().parent
SCHEMA='fd2d-R170-accurate-last-P1-cell-physical-tail-v1'
PARENT_SOURCE_SHA256='8c8b8fefd5a3d459833e2b20b472710c54aebbf3ed00028e9740ef0843f6f435'
REPRESENTATION='ruling_atlas_coast_Gauss_l_terminal_positive_trace_fixed_tail_degree_v1'


class DyadicTailAccurateLastCell(AccurateLastCell):
    """Explicit R170 archive + accurate physical profile terminal consumer.

    ``box`` takes normalized accurate labels in [0,1]. At exactly one it
    returns only angular jets of the true tail. It does not set a radial
    derivative at the all-zero curvature arcs. ``angular_majorant`` supplies
    the R174 integrable one-sided angular bound instead.
    """
    def __init__(self, field_arrays, profile_packet, *, profile_sha256=None):
        parent=identity(HERE/'fd2d_gc_accurate_last_cell.py')
        if parent['sha256']!=PARENT_SOURCE_SHA256:
            raise ValueError('The frozen inherited interval formulas changed')
        self.parent_formula_source=parent
        self.field_path,self.packet_path=Path(field_arrays),Path(profile_packet)
        saved=load_npz(field_arrays)
        if (str(saved.get('tail_search_domain_kind',''))!=DOMAIN_KIND or
            declared(saved,'tail_search_domain_definition')!=tail_search_domain_definition()):
            raise ValueError('This constructor requires the explicit R170 archive domain')
        if (str(saved.get('representation_kind',''))!=REPRESENTATION or
                str(saved.get('tail_kind',''))!='positive_bernstein'):
            raise ValueError('The complete field or polynomial-basis definition differs')
        self.tail_search_domain_definition=declared(saved,'tail_search_domain_definition')
        self.profile=R136ArbProfile.from_packet(profile_packet,expected_sha256=profile_sha256)
        field_identity=identity(field_arrays)
        if field_identity['sha256']!=self.profile.inputs['field_arrays']['sha256']:
            raise ValueError('Accurate profile must bind the identical new actual field bytes')
        self.K=int(saved['modes']);self.e=self.K+1;self.d=2*self.K+1
        counts=[int(saved[k]) for k in
                ('central_parameter_count','tail_parameter_count','profile_count')]
        mesh=np.asarray(saved['mesh']);raw=np.asarray(saved['corrections'])
        parameters=np.asarray(saved['parameters'])
        if (counts!=[self.K,16,7] or self.K<1 or
                mesh.dtype!=np.float64 or mesh.ndim!=1 or len(mesh)<2 or
                raw.dtype!=np.float64 or raw.shape!=(len(mesh),3*self.K+2) or
                parameters.dtype!=np.float64 or parameters.shape!=(sum(counts),) or
                not all(np.all(np.isfinite(a)) for a in (mesh,raw,parameters)) or
                np.any(np.diff(mesh)<=0) or not np.all(raw[-1]==0)):
            raise ValueError('Require the actual explicit layout, P1 mesh and zero final raw row')
        self.mesh=tuple(rational(x) for x in mesh)
        self.raw=raw
        self.parameters=tuple(rational(x) for x in parameters)
        self.central=counts[0]
        self.tail=self.parameters[counts[0]:sum(counts[:2])]
        self.tail_control_certificate=DyadicBernsteinControlBox().certificate(self.tail)
        if not self.tail_control_certificate['passed']:
            raise ValueError('The actual exact R170 local-coefficient domain failed')
        if (declared(saved,'tail_search_domain_certificate')!=self.tail_control_certificate):
            raise ValueError('Saved R170 certificate differs from the actual parameters')
        self.b,self.E=self.mesh[-2:]
        self.S=self.profile.end
        self.length=self.S-aq(self.b)
        if not self.length>0:
            raise ValueError('The accurate physical last cell must have positive width')
        seed=declared(saved,'seed_weight_definition')
        atlas=declared(saved,'angular_atlas_definition')
        gauss=declared(saved,'gauss_l_definition')
        terminal=declared(saved,'positive_trace_definition')
        protected=[seed['end'],atlas['exit_transition'][1],gauss['support'][1],
                   terminal['ramp_stop'],float(np.max(saved['profile_supports'])),
                   float(np.asarray(saved['blend'])[-1])]
        if any(rational(value)>=self.b for value in protected):
            raise ValueError('The full completed cell must be in the exact protected terminal region')
        if rational(terminal['cut'])!=self.E:
            raise ValueError('The actual saved cut labels differ')
        self.weight_start=rational(float(.42*float(self.E)))
        self.weight_length=rational(float(.58*float(self.E)))
        if self.weight_start+self.weight_length!=self.E or self.weight_start>=self.b:
            raise ValueError('The saved scalar tail weight must attain exactly one at its label')
        last=self.profile.pieces[-1]
        if not aq(self.b)>last['s0']:
            raise ValueError('The entire last raw cell must belong to the accurate terminal piece')
        self.last_piece=last['index']
        self.c0=tuple(rational(v) for v in self.raw[-2])
        self.inputs=dict(field_arrays=field_identity,profile_packet=identity(profile_packet),
                         source=identity(__file__))

    def definition(self):
        result=AccurateLastCell.definition(self)
        result.pop('binding_sha256')
        result['schema']=SCHEMA
        result['tail_geometry']['controls']='actual sixteen exact binary64 rationals in the R170 eight-piece local Bernstein domain'
        result['tail_search_domain_kind']=DOMAIN_KIND
        result['tail_search_domain_definition']=self.tail_search_domain_definition
        result['tail_search_domain_certificate']=self.tail_control_certificate
        result['parent_formula_source']=self.parent_formula_source
        result['sources']=[identity(HERE/name) for name in (
            'fd2d_gc_dyadic_tail_accurate_last_cell.py',
            'fd2d_gc_accurate_last_cell.py','fd2d_dyadic_bernstein_tail.py',
            'fd2d_gc_dyadic_tail_problem.py','fd2d_gc_r136_arb_profile.py',
            'fd2d_gc_terminal_angular_majorant.py')]
        result['legacy_constructor_or_global_control_guard_invoked']=False
        result['inherited_full_polynomial_interval_methods_unchanged']=True
        result['radial_II_jets_at_cut_assigned']=False
        result['R174_angular_majorant_method']='angular_majorant(); conditional true-body remainder needs actual initial norms'
        result['binding_sha256']=hashlib.sha256(json.dumps(result,sort_keys=True,
                                                    separators=(',',':')).encode()).hexdigest()
        return result

    def angular_majorant(self):
        last=self.profile.pieces[self.last_piece]
        if (last['kind']!='phase_bridge' or last['raw'].get('exact_endpoint_phase')!='-pi/2'
                or last['raw'].get('ps0')!=0 or last['raw'].get('ps1')!=0):
            raise ValueError('The explicit R174 cubic terminal phase hypotheses are not present')
        lower,upper=ends(self.length)
        return terminal_angular_majorant(self.tail,self.c0,self.K,
            cell_length_lower=lower,cell_length_upper=upper,
            phase_length=last['L_exact'],phase0=last['p0_exact'])
