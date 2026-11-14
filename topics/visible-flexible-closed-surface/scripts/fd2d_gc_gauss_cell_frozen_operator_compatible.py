"""Strict R152/R153 background adapter for the frozen-operator thin class.

The original R152 hybrid intentionally accepts exactly its actual R153
background class. Do not change that check or pretend a new class has the
old name. This wrapper uses the original R155 background-view function
to produce the real old R153 class only for that branch. The old complete
cell formula and Jacobian are called unchanged. Cached angular operators
remain usable by node evaluations and the separate terminal increment;
the R152/R153 background branch deliberately uses original operators.
"""
from __future__ import annotations
import copy
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE
from fd2d_gc_raw_bump_positive_gauss import PositiveGaussRawBumpDAE
from fd2d_gc_gauss_cell_positive_trace import gauss_cell_positive_trace as _original_cell
from fd2d_gc_frozen_operator_projections import _FrozenProjectionOperatorsMixin, _CLASSES

_COMPATIBLE_CLASSES = {}


def _is_plain_background(view):
    return (type(view) is PositiveGaussRawBumpDAE
            and not hasattr(view, '_frozen_operator_projection_cache'))


class _OriginalR153BackgroundOnly:
    def coast_background_view(self):
        # Directly execute the frozen original construction. Its object
        # really has the old mathematical class; no class-name spoofing.
        view = PositiveTraceRawBumpDAE.coast_background_view(self)
        view._operator_cache = {}
        for name in ('_frozen_operator_projection_cache', '_frozen_operator_packet_context'):
            if hasattr(view, name):
                delattr(view, name)
        # Previously created plain-background caches are safe to reuse;
        # a derived view retaining the new operator mixin is not used in
        # this deliberately original-operator branch.
        cell = getattr(view, '_cell_gauss_view_cache', None)
        if cell is not None and not _is_plain_background(cell[1]['view']):
            view._cell_gauss_view_cache = None
        known = getattr(view, '_positive_known_coast_view', None)
        if known is not None and not _is_plain_background(known[1]):
            delattr(view, '_positive_known_coast_view')
        for name in ('_chunked_gauss_codazzi_views', '_interior_constraint_point_cache'):
            if hasattr(view, name):
                delattr(view, name)
        if type(view) is not PositiveGaussRawBumpDAE:
            raise TypeError('The original R155 method did not return the exact original R153 class')
        return view


def gauss_cell_positive_trace_frozen_operator_compatible(problem, vector, *,
        order=2, high_weight=1., jacobian=True):
    """Same complete cell equations/J; only the background view adapter differs."""
    if not isinstance(problem, _FrozenProjectionOperatorsMixin):
        return _original_cell(problem, vector, order=order, high_weight=high_weight,
                              jacobian=jacobian)
    base = type(problem)
    if isinstance(problem, _OriginalR153BackgroundOnly):
        local = problem
    else:
        if base not in _CLASSES.values():
            raise TypeError('Only the registered pure frozen-operator thin classes are supported')
        if base not in _COMPATIBLE_CLASSES:
            _COMPATIBLE_CLASSES[base] = type('OriginalR153Background_'+base.__name__,
                (_OriginalR153BackgroundOnly, base), {'__module__': __name__})
        local = copy.copy(problem)
        local.__class__ = _COMPATIBLE_CLASSES[base]
    answer = _original_cell(local, vector, order=order, high_weight=high_weight,
                            jacobian=jacobian)
    # Preserve only runtime view caches that the unchanged original cell
    # consumer created. No field, parameter, shape or definition is copied.
    for name in ('_positive_known_coast_view', '_cell_gauss_view_cache'):
        if hasattr(local, name):
            setattr(problem, name, getattr(local, name))
    answer['info'] = dict(answer['info'],
        runtime_operator_cache_compatibility=dict(
            actual_R153_background_class='fd2d_gc_raw_bump_positive_gauss.PositiveGaussRawBumpDAE',
            old_strict_identity_check_unchanged=True,
            original_complete_cell_formula_and_Jacobian_called=True,
            mathematical_fields_or_finite_equations_changed=False,
            operator_projection_cache_used_in_R152_R153_background=False,
            prepared_geometry_reference_cache_still_shared=True,
            node_and_separate_terminal_operator_cache_left_enabled=True,
            no_process_global_class_patch=True))
    return answer
