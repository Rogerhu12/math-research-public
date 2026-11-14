"""Optional numerical policy for small changes after a real finite DN success.

This module is not installed in fast07. It constructs a subclass of the
already selected original Coordinator; it changes only its next initial
continuation increment. Original residuals, failure classification, requests,
successful-packet handling, budget, final Jacobian/audit and return remain.
"""
import math
import numpy as np


def coordinator_class(original):
    class SmallHeightCoordinator(original):
        def __init__(self, *args, direct_relative_limit=0.01, **kwargs):
            if (not isinstance(direct_relative_limit, (int, float))
                    or isinstance(direct_relative_limit, bool)
                    or not math.isfinite(direct_relative_limit)
                    or not 0 < direct_relative_limit <= 1):
                raise ValueError('A finite explicit small-height threshold in (0,1] is required')
            self.direct_relative_limit = float(direct_relative_limit)
            self._pending_height_goal = None
            self._nominal_height_policy = None
            super().__init__(*args, **kwargs)

        def _select_height_increment(self, external_request, phase):
            relative = None
            direct = False
            # The original solve still validates the requested type, shape,
            # finite values and actual response. No old seed is called good.
            if self.good is not None:
                goal = self._pending_height_goal
                origin = np.asarray(self.good['height'], dtype=float)
                if (goal.dtype.kind in 'fiu' and goal.shape == origin.shape
                        and np.all(np.isfinite(goal))):
                    reference = float(np.max(np.abs(origin)))
                    delta = float(np.max(np.abs(goal.astype(float)-origin)))
                    if reference > 0 and math.isfinite(delta):
                        ratio = delta/reference
                        if math.isfinite(ratio):
                            relative = ratio
                            direct = relative <= self.direct_relative_limit
                    elif delta == 0:
                        relative, direct = 0., True
            selected = dict(self._nominal_height_policy)
            if direct:
                selected.update(initial_step='1', maximum_step='1')
            self.journal({
                'event': 'external-height-increment-policy',
                'external_request': external_request, 'selection_phase': phase,
                'state': self.state, 'physical_calls': self.port.calls,
                'known_successful_origin_call': self.good['call'] if self.good else None,
                'relative_height_change_inf': relative,
                'direct_relative_limit': self.direct_relative_limit,
                'selected_initial_step': selected['initial_step'],
                'selected_maximum_step': selected['maximum_step'],
                'minimum_step': selected['minimum_step'],
                'maximum_physical_requests': selected['maximum_physical_requests'],
                'small_jump_direct_trial': direct,
                'scope': 'Numerical target scheduling only. Every actual target uses the original nonlinear residual and success criterion; a recognized failure halves from the last real success.'})
            self.policy = selected

        def _accept(self, height, response, packet, physical):
            had_good = self.good is not None
            super()._accept(height, response, packet, physical)
            if not had_good and self._pending_height_goal is not None:
                # Original solve has actually accepted its bootstrap packet.
                # It reads initial_step only after this point. Thus a new run
                # may use a direct small first update without pretending its
                # saved seed was already solved by this worker.
                self._select_height_increment(self.external_id, 'after-actual-bootstrap')

        def solve(self, height, jacobian=True, audit=False):
            nominal_policy = self.policy
            self._nominal_height_policy = nominal_policy
            self.policy = dict(nominal_policy)
            try:
                self._pending_height_goal = np.asarray(height).copy()
                if self.good is not None:
                    self._select_height_increment(self.external_id+1, 'before-external-target')
                return super().solve(height, jacobian=jacobian, audit=audit)
            finally:
                self.policy = nominal_policy
                self._pending_height_goal = None
                self._nominal_height_policy = None
    return SmallHeightCoordinator
