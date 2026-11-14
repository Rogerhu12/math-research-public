"""R170 thin finite-provider domain and QP-row integration.

The existing saved-mesh complete-field formulas are inherited. A genuine
new provider selects the genuine R170 tail class and replaces only the
selected tail search-domain predicate. The old field representation tag
continues to name the same formulas; a separate mandatory packet binds
the new search domain. No Context, QP driver, or active source is modified.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import (
    MidpointRefinedFixedTailDAE, checkpoint_arrays as original_checkpoint_arrays)
from fd2d_dyadic_bernstein_tail import (
    DyadicBernsteinControlBox, DyadicBernsteinFlatDevelopableFamily)

HERE = Path(__file__).resolve().parent
SCHEMA = 'fd2d-explicit-dyadic-Bernstein-tail-search-domain-v1'
DOMAIN_KIND = 'degree15_eight_dyadic_Bernstein_box'


def tail_search_domain_definition():
    return dict(schema=SCHEMA, domain_kind=DOMAIN_KIND,
        control_box=DyadicBernsteinControlBox().definition(),
        tail_parameter_count=16,
        inherited_polynomial_basis_tag='positive_bernstein',
        basis_tag_is_not_global_control_box=True,
        tail_class='fd2d_dyadic_bernstein_tail.DyadicBernsteinFlatDevelopableFamily',
        exact_cut_condition='P>=0 proves the actual PSD tail; zero raw cut correction and flat cut remain required',
        raw_profile_atlas_lifting_nonlinear_functions_changed=False,
        old_parameter_domain_global_tail_min_max_replaced=True,
        central_and_profile_domain_predicates_unchanged=True,
        source_sha256=identity(__file__)['sha256'],
        domain_source_sha256=identity(HERE/'fd2d_dyadic_bernstein_tail.py')['sha256'],
        inherited_restore_source_sha256=identity(HERE/'fd2d_gc_midpoint_refined_positive_trace_v3.py')['sha256'],
        inherited_raw_domain_source_sha256=identity(HERE/'fd2d_gc_raw_bump_dae.py')['sha256'])


class DyadicTailRefinedDAE(MidpointRefinedFixedTailDAE):
    """Fixed-tail actual mesh restoration, explicit larger tail domain."""
    def __init__(self, source, *, saved_field, split_cells=(), **kwargs):
        saved = load_npz(saved_field) if isinstance(saved_field,(str,Path)) else saved_field
        if int(saved.get('tail_parameter_count', -1)) != 16:
            raise ValueError('Select the explicit independent degree-15 tail layout')
        declared = saved.get('tail_search_domain_definition')
        expected = tail_search_domain_definition()
        if declared is not None and json.loads(str(declared)) != expected:
            raise ValueError('Different saved tail domain or defining source')
        if 'tail_search_domain_kind' in saved and str(saved['tail_search_domain_kind']) != DOMAIN_KIND:
            raise ValueError('Different explicit tail search-domain kind')
        # The inherited constructor checks the unchanged mathematical
        # packets and the actual saved mesh. It does not evaluate a tail
        # control or run parameter_domain. This new class owns that domain.
        super().__init__(source, saved_field=saved, split_cells=split_cells, **kwargs)
        self.tail_control_box = DyadicBernsteinControlBox()
        self.tail_class = DyadicBernsteinFlatDevelopableFamily
        self.tail_search_domain_definition = expected
        self.tail_search_domain_kind = DOMAIN_KIND
        initial = self.tail_control_box.certificate(saved['parameters'][self.tail_parameter_slice])
        if not initial['passed']:
            raise ValueError('Initial controls need an explicitly recorded R170 repair before this factory')
        self.initial_tail_domain_certificate = initial

    def parameter_domain(self, vector, central_curvature_maximum=None,
                         central_curvature_minimum=0.):
        """RawBumpDAE's same non-tail predicates, exact R170 tail predicate."""
        _, p = self.unpack(vector)
        if not np.all(np.isfinite(p)):
            return False
        if not self.tail_control_box.certificate(p[self.tail_parameter_slice])['passed']:
            return False
        if central_curvature_maximum is not None:
            n = self.seed+self.core_basis@p[self.central_slice]
            if (n.min() < central_curvature_minimum or n.min() <= 0.
                    or n.max() > central_curvature_maximum):
                return False
        delta = p[self.profile_parameter_slice]
        if self.profile_domain is not None:
            dom = self.profile_domain
            if np.any(dom['matrix']@delta < dom['lower']):
                return False
        try:
            self.operators(delta)
        except (FloatingPointError, ValueError):
            return False
        return True

    def parameter_layout(self):
        out = super().parameter_layout()
        out['tail_search_domain_definition'] = self.tail_search_domain_definition
        out['tail_global_variable_box_required'] = False
        out['tail_two_sided_linear_row_count'] = 128
        return out


def create_dyadic_tail_problem(source, *, saved_field, split_cells=(), **kwargs):
    """Explicit new entry; no class replacement of an existing live object."""
    return DyadicTailRefinedDAE(source, saved_field=saved_field,
                               split_cells=split_cells, **kwargs)


def scaled_tail_linear_constraints(problem, parameters, parameter_scale):
    """Embed R170 increment rows in the actual full parameter coordinates.

    z is the scaled QP unknown: dp=parameter_scale*z. This helper returns
    only tail rows. The caller removes the old per-control tail Bounds,
    keeps all original central/profile/gap constraints, and performs the
    actual merit evaluation after any explicit parameter repair.
    """
    if getattr(problem, 'tail_search_domain_kind', None) != DOMAIN_KIND:
        raise TypeError('Require the explicitly selected new domain provider')
    p, scale = np.asarray(parameters,float), np.asarray(parameter_scale,float)
    P = int(problem.parameter_count)
    ts = problem.tail_parameter_slice
    if (p.shape != (P,) or scale.shape != (P,) or ts.stop-ts.start != 16
            or not np.all(np.isfinite(p)) or not np.all(np.isfinite(scale)) or np.any(scale <= 0)):
        raise ValueError('Require the actual finite parameter layout and positive scaling')
    packet = problem.tail_control_box.linear_constraints(p[ts])
    matrix = np.zeros((128, P))
    matrix[:,ts] = packet['matrix']*scale[None,ts]
    return dict(matrix=matrix, lower=packet['lower'], upper=packet['upper'],
        unscaled_tail_matrix=packet['matrix'],
        lower_exact=packet['lower_exact'], upper_exact=packet['upper_exact'],
        parameter_layout=problem.parameter_layout(),
        tail_slice=[ts.start,ts.stop],
        scaled_matrix_and_rhs_are_binary64_representatives=True,
        exact_acceptance_uses='tail_control_box.certificate(actual_b)',
        old_tail_variable_box_must_be_removed=True,
        no_new_constraint_on_central_or_profile_parameters=True)


def checkpoint_arrays(problem, vector, candidate_sha256, *, refinement_definition):
    if getattr(problem, 'tail_search_domain_kind', None) != DOMAIN_KIND:
        raise TypeError('Require the explicit new-domain provider')
    _, p = problem.unpack(vector)
    certificate = problem.tail_control_box.certificate(p[problem.tail_parameter_slice])
    if not certificate['passed']:
        raise ValueError('Do not label a domain-violating checkpoint accepted under R170')
    out = original_checkpoint_arrays(problem, vector, candidate_sha256,
                                    refinement_definition=refinement_definition)
    # These are evaluations of a previous vector, not field definitions.
    # A caller may add newly computed diagnostics after this transport.
    dropped = []
    for name in ('full_gauss_nodes','codazzi_cells','omitted_codazzi_cells'):
        if name in out:
            dropped.append(name)
            del out[name]
    out['tail_search_domain_kind'] = np.array(DOMAIN_KIND)
    out['tail_search_domain_definition'] = np.array(json.dumps(problem.tail_search_domain_definition,sort_keys=True))
    out['tail_search_domain_certificate'] = np.array(json.dumps(certificate,sort_keys=True))
    out['tail_domain_transport_diagnostics'] = np.array(json.dumps(dict(
        inherited_evaluated_arrays_removed=dropped, new_F_or_J_evaluated=False,
        caller_may_attach_new_actual_diagnostics=True),sort_keys=True))
    return out
