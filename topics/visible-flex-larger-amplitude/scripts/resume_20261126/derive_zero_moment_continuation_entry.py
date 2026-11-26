#!/usr/bin/env python3
"""Pure full-source derivation of a SAME final-equation continuation candidate.

This script only transforms complete byte-pinned Python sources and checks
ASTs. It imports no scientific module and runs no field/root/J calculation.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

ROOT = None
POLICY_SOURCE = "@dataclass(frozen=True)\nclass EndpointContinuationPolicy:\n    initial_step: float = .25\n    minimum_step: float = 1./65536\n    growth: float = 1.5\n    shrink: float = .5\n    maximum_stage_attempts: int = 64\n    predictor: bool = True\n\n    def __post_init__(self):\n        for name in ('initial_step', 'minimum_step', 'growth', 'shrink'):\n            value = float(getattr(self, name))\n            if not math.isfinite(value):\n                raise ValueError('Finite continuation parameter required: '+name)\n            object.__setattr__(self, name, value)\n        if not (0 < self.minimum_step <= self.initial_step <= 1\n                and self.growth >= 1 and 0 < self.shrink < 1):\n            raise ValueError('Use a positive bounded continuation step and honest growth/shrink policy')\n        count = int(self.maximum_stage_attempts)\n        if count != self.maximum_stage_attempts or count < 1:\n            raise ValueError('Use a positive complete per-angle continuation stage-attempt budget')\n        object.__setattr__(self, 'maximum_stage_attempts', count)\n        if not isinstance(self.predictor, bool):\n            raise TypeError('Continuation predictor policy must be an explicit boolean')\n\n    def metadata(self):\n        return dict(schema='fixed-final-endpoint-residual-continuation-policy-v1',\n            initial_step=self.initial_step, minimum_step=self.minimum_step,\n            growth=self.growth, shrink=self.shrink,\n            maximum_stage_attempts=self.maximum_stage_attempts, predictor=self.predictor,\n            equation='H(z,lambda;x,phi)=C(z;x,phi)-(1-lambda)*C(0;x,phi)',\n            origin='lambda=0,z=0 at the SAME fixed original x,phi,Q',\n            target='lambda=1 and a fresh read of the ORIGINAL C(z;x,phi)=0',\n            rejected_stage='restore the exact last accepted z and lambda, then shrink the lambda step',\n            corrector='same complete C/Cz and original per-stage Newton/Armijo/ball policy',\n            auxiliary_parameter_is_physical_t=False,\n            target_metric_changed=False, current_free_point_changed_by_continuation=False,\n            numerical_stage_trajectory_differentiated=False,\n            implicit_derivatives_use_final_original_equation=True,\n            exact_branch_existence_or_uniqueness_certified=False)\n\n\n"
METHOD_SOURCE = '    def _continuation_value(self, z, data):\n        self.endpoint_continuation_counts[\'equation_angle_evaluations\'] += len(z)\n        return self._C0(z, data)\n\n    def _continuation_jacobian(self, z, data):\n        self.endpoint_continuation_counts[\'jacobian_angle_evaluations\'] += len(z)\n        return self._C0_jacobian(z, data)\n\n    def _continuation_summary(self):\n        record = self._last_continuation_batch\n        if record is None:\n            return None\n        result = {key: record[key] for key in (\n            \'schema\', \'current_full_point_sha256\', \'angle_count\', \'material_angles_binary64_hex\',\n            \'initial_endpoint_residual_norms\', \'final_parameters\',\n            \'stage_attempts_by_angle\', \'accepted_stages_by_angle\',\n            \'rejected_stages_by_angle\', \'corrector_updates_by_angle\',\n            \'all_final_parameters_reached_one\', \'final_original_equation_checked\',\n            \'auxiliary_parameter_is_not_physical_t\',\n            \'complete_continuous_branch_certified\')}\n        result.update(minimum_completed_parameter=min(record[\'final_parameters\'], default=None),\n            maximum_completed_parameter=max(record[\'final_parameters\'], default=None),\n            actual_total_stage_attempts=sum(record[\'stage_attempts_by_angle\']),\n            actual_total_accepted_stages=sum(record[\'accepted_stages_by_angle\']),\n            actual_total_rejected_stages=sum(record[\'rejected_stages_by_angle\']),\n            actual_total_corrector_updates=sum(record[\'corrector_updates_by_angle\']),\n            actual_batch_stage_count=len(record[\'stages\']))\n        return result\n\n    def _continuation_corrector(self, data, anchor, start, target, needed):\n        """Same complete C and C_z, with a fixed residual offset for this stage.\n\n        A rejected stage never changes the accepted (z,lambda) pair. Every\n        accepted numerical update remains in the original open branch ball.\n        Values are detached; only the final original endpoint equation is\n        subsequently used by the untouched 3/6/9 implicit derivative chain.\n        """\n        count = len(start)\n        z = start.detach().clone()\n        success = ~needed\n        failed = torch.zeros(count, dtype=torch.bool)\n        advances = np.zeros(count, dtype=np.int64)\n        reasons = [\'not requested\' if not bool(needed[j]) else \'unresolved\'\n                   for j in range(count)]\n        last_alpha = [None]*count\n        last_trial_norm = [None]*count\n        last_candidate_norm = [None]*count\n        last_norm = [None]*count\n        offset = (1-target)[:, None]*anchor\n        for iteration in range(self.policy.maximum_iterations+1):\n            value = self._continuation_value(z, data)-offset\n            norms = torch.linalg.vector_norm(value, dim=-1)\n            active = needed & ~success & ~failed\n            finite = torch.isfinite(value).all(-1) & torch.isfinite(norms)\n            for j in torch.nonzero(active).flatten().tolist():\n                last_norm[j] = float(norms[j]) if bool(finite[j]) else None\n            bad = active & ~finite\n            for j in torch.nonzero(bad).flatten().tolist():\n                reasons[j] = \'nonfinite complete continuation residual\'\n            failed |= bad\n            done = active & finite & (norms <= self.policy.tolerance)\n            success |= done\n            for j in torch.nonzero(done).flatten().tolist():\n                reasons[j] = \'complete continuation residual tolerance met\'\n            active = needed & ~success & ~failed\n            if not bool(active.any()):\n                break\n            if iteration == self.policy.maximum_iterations:\n                for j in torch.nonzero(active).flatten().tolist():\n                    reasons[j] = \'declared per-stage Newton budget exhausted\'\n                failed |= active\n                break\n            try:\n                matrix = self._continuation_jacobian(z, data)\n            except EndpointRootFailure as error:\n                for j in torch.nonzero(active).flatten().tolist():\n                    reasons[j] = \'complete continuation Jacobian unavailable: \'+str(error)\n                failed |= active\n                break\n            direction = torch.zeros_like(z)\n            work = active.clone()\n            for j in torch.nonzero(active).flatten().tolist():\n                try:\n                    direction[j] = torch.linalg.solve(matrix[j], value[j, :, None])[:, 0]\n                except RuntimeError as error:\n                    work[j] = False\n                    failed[j] = True\n                    reasons[j] = \'actual stage linear solve failed: \'+str(error)\n                if bool(work[j]) and not bool(torch.isfinite(direction[j]).all()):\n                    work[j] = False\n                    failed[j] = True\n                    reasons[j] = \'nonfinite actual stage Newton direction\'\n            if not bool(work.any()):\n                continue\n            accepted = ~work\n            next_z = z.clone()\n            alpha = torch.ones(count, dtype=torch.float64)\n            for _ in range(self.policy.maximum_backtracks):\n                candidate = z-alpha[:, None]*direction\n                candidate_norm = torch.linalg.vector_norm(candidate, dim=-1)\n                admissible = (candidate_norm < self.policy.branch_radius) & torch.isfinite(candidate).all(-1)\n                pending = work & ~accepted\n                use_candidate = pending & admissible\n                # Unusable or already resolved rows are evaluated at the\n                # unchanged current point; the true complete batch count is paid.\n                trial = torch.where(use_candidate[:, None], candidate, z)\n                trial_value = self._continuation_value(trial, data)-offset\n                trial_norm = torch.linalg.vector_norm(trial_value, dim=-1)\n                for j in torch.nonzero(pending).flatten().tolist():\n                    last_alpha[j] = float(alpha[j])\n                    last_candidate_norm[j] = (float(candidate_norm[j])\n                        if bool(torch.isfinite(candidate_norm[j])) else None)\n                    last_trial_norm[j] = (float(trial_norm[j])\n                        if bool(torch.isfinite(trial_norm[j])) else None)\n                good = (pending & admissible & torch.isfinite(trial_norm)\n                    & ((trial_norm <= self.policy.tolerance)\n                       | (trial_norm < (1-self.policy.armijo*alpha)*norms)))\n                next_z[good] = candidate[good]\n                accepted |= good\n                self.endpoint_counts[\'root_line_search_evaluations\'] += count\n                self.endpoint_continuation_counts[\'backtrack_angle_evaluations\'] += count\n                if bool(accepted.all()):\n                    break\n                alpha[work & ~accepted] *= .5\n            bad = work & ~accepted\n            for j in torch.nonzero(bad).flatten().tolist():\n                reasons[j] = \'no same-stage complete residual Armijo decrease inside the original ball\'\n            failed |= bad\n            advanced = work & accepted\n            advances[advanced.cpu().numpy()] += 1\n            z = next_z\n        # Every claimed stage success is checked again at its returned z.\n        final = self._continuation_value(z, data)-offset\n        norm = torch.linalg.vector_norm(final, dim=-1)\n        inside = torch.linalg.vector_norm(z, dim=-1) < self.policy.branch_radius\n        valid = torch.isfinite(final).all(-1) & torch.isfinite(norm) & inside & (norm <= self.policy.tolerance)\n        success = needed & success & valid\n        for j in torch.nonzero(needed & ~success).flatten().tolist():\n            if reasons[j] == \'complete continuation residual tolerance met\':\n                reasons[j] = \'returned same-stage residual or original ball check failed\'\n        records = [dict(angle_index=j, requested=bool(needed[j]),\n            parameter_target=float(target[j]), successful=bool(success[j]),\n            actual_newton_updates=int(advances[j]), reason=reasons[j],\n            final_stage_residual_norm=(float(norm[j]) if bool(torch.isfinite(norm[j])) else None),\n            correction_norm=(float(torch.linalg.vector_norm(z[j]))\n                if bool(torch.isfinite(z[j]).all()) else None),\n            last_newton_residual_norm=last_norm[j], last_alpha=last_alpha[j],\n            last_trial_residual_norm=last_trial_norm[j],\n            last_candidate_correction_norm=last_candidate_norm[j])\n            for j in range(count) if bool(needed[j])]\n        return z.detach(), success, advances, records\n\n    def _solve_roots(self, data, *, literal_phi_hex):\n        """Detached residual continuation, ending at the original C(z)=0.\n\n        Auxiliary lambda is neither the physical flex parameter nor a changed\n        target metric. Its successful finite stages are numerical trajectory\n        records only; no existence, uniqueness or cross-angle branch theorem\n        is inferred from them.\n        """\n        count = len(data[\'core\'][0])\n        if len(literal_phi_hex) != count or any(float.fromhex(v).hex() != v for v in literal_phi_hex):\n            raise ValueError(\'Continuation roots need every original literal material angle\')\n        self.endpoint_continuation_counts[\'batches\'] += 1\n        self._last_continuation_batch = dict(\n            schema=\'actual-same-endpoint-equation-residual-continuation-batch-v1\',\n            current_full_point_sha256=self._current_point_sha256,\n            angle_count=count, material_angles_binary64_hex=list(literal_phi_hex),\n            initial_endpoint_residual_norms=[],\n            final_parameters=[0.]*count, stage_attempts_by_angle=[0]*count,\n            accepted_stages_by_angle=[0]*count, rejected_stages_by_angle=[0]*count,\n            corrector_updates_by_angle=[0]*count, stages=[],\n            all_final_parameters_reached_one=False,\n            final_original_equation_checked=False,\n            auxiliary_parameter_is_not_physical_t=True,\n            complete_continuous_branch_certified=False)\n        log = self._last_continuation_batch\n        policy = self.continuation_policy\n        with torch.no_grad():\n            z = torch.zeros((count, 3), dtype=torch.float64)\n            anchor = self._continuation_value(z, data).detach()\n            norm0 = torch.linalg.vector_norm(anchor, dim=-1)\n            log[\'initial_endpoint_residual_norms\'] = [\n                float(norm0[j]) if bool(torch.isfinite(norm0[j])) else None for j in range(count)]\n            if not bool(torch.isfinite(anchor).all()) or not bool(torch.isfinite(norm0).all()):\n                self._fail(\'Nonfinite original endpoint residual at continuation origin\')\n            parameter = torch.zeros(count, dtype=torch.float64)\n            # An already accurate original root needs no auxiliary stages.\n            parameter[norm0 <= self.policy.tolerance] = 1.\n            step = torch.full((count,), policy.initial_step, dtype=torch.float64)\n            attempts = np.zeros(count, dtype=np.int64)\n            accepted_stages = np.zeros(count, dtype=np.int64)\n            rejected_stages = np.zeros(count, dtype=np.int64)\n            updates = np.zeros(count, dtype=np.int64)\n            while bool((parameter < 1).any()):\n                needed = parameter < 1\n                exhausted = needed.cpu().numpy() & (attempts >= policy.maximum_stage_attempts)\n                if bool(exhausted.any()):\n                    log.update(final_parameters=parameter.tolist(),\n                        stage_attempts_by_angle=attempts.tolist(),\n                        accepted_stages_by_angle=accepted_stages.tolist(),\n                        rejected_stages_by_angle=rejected_stages.tolist(),\n                        corrector_updates_by_angle=updates.tolist())\n                    self._fail(\'Declared continuation stage-attempt budget exhausted before lambda=1\',\n                        residual=float(torch.linalg.vector_norm(self._continuation_value(z, data), dim=-1).max()),\n                        correction=float(torch.linalg.vector_norm(z, dim=-1).max()),\n                        angles=np.flatnonzero(exhausted).tolist())\n                before = parameter.clone()\n                target = torch.minimum(torch.ones_like(parameter), parameter+step)\n                target[~needed] = 1.\n                delta = target-parameter\n                stalled = needed & (delta <= 0)\n                if bool(stalled.any()):\n                    self._fail(\'No positive representable continuation parameter step\',\n                        angles=torch.nonzero(stalled).flatten().tolist())\n                start = z.clone()\n                predictor_used = torch.zeros(count, dtype=torch.bool)\n                predictor_reason = [\'not requested\']*count\n                if policy.predictor:\n                    try:\n                        matrix = self._continuation_jacobian(z, data)\n                    except EndpointRootFailure as error:\n                        matrix = None\n                        for j in torch.nonzero(needed).flatten().tolist():\n                            predictor_reason[j] = \'Jacobian unavailable; last accepted z retained: \'+str(error)\n                    if matrix is not None:\n                        for j in torch.nonzero(needed).flatten().tolist():\n                            try:\n                                tangent = torch.linalg.solve(matrix[j], -anchor[j, :, None])[:, 0]\n                                candidate = z[j]+delta[j]*tangent\n                                if (bool(torch.isfinite(candidate).all())\n                                        and float(torch.linalg.vector_norm(candidate)) < self.policy.branch_radius):\n                                    start[j] = candidate\n                                    predictor_used[j] = True\n                                    predictor_reason[j] = \'same-equation tangent predictor used\'\n                                else:\n                                    predictor_reason[j] = \'predictor outside original ball or nonfinite; last accepted z retained\'\n                            except RuntimeError as error:\n                                predictor_reason[j] = \'predictor linear solve failed; last accepted z retained: \'+str(error)\n                else:\n                    for j in torch.nonzero(needed).flatten().tolist():\n                        predictor_reason[j] = \'predictor explicitly disabled; last accepted z retained\'\n                attempts[needed.cpu().numpy()] += 1\n                self.endpoint_continuation_counts[\'stage_attempt_angle_count\'] += int(needed.sum())\n                self.endpoint_continuation_counts[\'predictor_angle_count\'] += int(predictor_used.sum())\n                self.endpoint_continuation_counts[\'predictor_fallback_angle_count\'] += int((needed & ~predictor_used).sum())\n                corrected, success, stage_updates, stage_records = self._continuation_corrector(\n                    data, anchor, start, target, needed)\n                updates += stage_updates\n                self.endpoint_counts[\'root_iterations\'] += int(stage_updates.sum())\n                self.endpoint_continuation_counts[\'corrector_newton_updates\'] += int(stage_updates.sum())\n                failed = needed & ~success\n                z[success] = corrected[success]\n                parameter[success] = target[success]\n                accepted_stages[success.cpu().numpy()] += 1\n                rejected_stages[failed.cpu().numpy()] += 1\n                self.endpoint_continuation_counts[\'accepted_stage_angle_count\'] += int(success.sum())\n                self.endpoint_continuation_counts[\'rejected_stage_angle_count\'] += int(failed.sum())\n                for item in stage_records:\n                    j = item[\'angle_index\']\n                    item.update(parameter_before=float(before[j]), actual_parameter_increment=float(delta[j]),\n                        predictor_used=bool(predictor_used[j]), predictor_reason=predictor_reason[j],\n                        accepted_parameter_after=float(parameter[j]),\n                        rejected_stage_did_not_change_accepted_z_or_parameter=not bool(success[j]))\n                log[\'stages\'].append(dict(batch_stage=len(log[\'stages\']),\n                    angle_records=stage_records))\n                log.update(final_parameters=parameter.tolist(),\n                    stage_attempts_by_angle=attempts.tolist(),\n                    accepted_stages_by_angle=accepted_stages.tolist(),\n                    rejected_stages_by_angle=rejected_stages.tolist(),\n                    corrector_updates_by_angle=updates.tolist())\n                # Increase only after a complete successful correction; every\n                # rejected stage returns to exactly the prior accepted pair.\n                step[success] = torch.minimum(torch.ones_like(step[success]), delta[success]*policy.growth)\n                step[failed] = delta[failed]*policy.shrink\n                too_small = failed & (step < policy.minimum_step)\n                if bool(too_small.any()):\n                    self._fail(\'Continuation step exhausted before the original endpoint equation was reached\',\n                        residual=float(torch.linalg.vector_norm(self._continuation_value(z, data), dim=-1).max()),\n                        correction=float(torch.linalg.vector_norm(z, dim=-1).max()),\n                        angles=torch.nonzero(too_small).flatten().tolist())\n            log.update(final_parameters=parameter.tolist(),\n                stage_attempts_by_angle=attempts.tolist(),\n                accepted_stages_by_angle=accepted_stages.tolist(),\n                rejected_stages_by_angle=rejected_stages.tolist(),\n                corrector_updates_by_angle=updates.tolist())\n            log[\'all_final_parameters_reached_one\'] = bool((parameter == 1).all())\n            # The final acceptance reads original C, with no homotopy offset.\n            final_value = self._continuation_value(z, data)\n            final_norm = torch.linalg.vector_norm(final_value, dim=-1)\n            inside = torch.linalg.vector_norm(z, dim=-1) < self.policy.branch_radius\n        if (not log[\'all_final_parameters_reached_one\']\n                or not bool(torch.isfinite(final_norm).all())\n                or bool((final_norm > self.policy.tolerance).any())\n                or not bool(inside.all())):\n            self._fail(\'Returned continuation candidate has unpaid ORIGINAL endpoint residual or ball\',\n                residual=float(final_norm.max()),\n                correction=float(torch.linalg.vector_norm(z, dim=-1).max()))\n        log[\'final_original_equation_checked\'] = True\n        try:\n            A = self._continuation_jacobian(z, data)\n        except (EndpointRootFailure, RuntimeError) as error:\n            self._fail(\'Actual final ORIGINAL endpoint Jacobian read failed: \'+str(error))\n        try:\n            singular = torch.linalg.svdvals(A)[..., -1]\n        except RuntimeError as error:\n            self._fail(\'Actual final endpoint Jacobian diagnostic failed: \'+str(error))\n        if not bool(torch.isfinite(singular).all()):\n            self._fail(\'Nonfinite actual final endpoint singular-value diagnostic\')\n        self.endpoint_counts[\'root_angles_solved\'] += count\n        self.maximum_endpoint_root_residual = max(self.maximum_endpoint_root_residual,\n                                                  float(final_norm.max()))\n        self.maximum_endpoint_correction_norm = max(self.maximum_endpoint_correction_norm,\n                                                    float(torch.linalg.vector_norm(z, dim=-1).max()))\n        self.minimum_endpoint_sample_singular_value = min(self.minimum_endpoint_sample_singular_value,\n                                                          float(singular.min()))\n        records = [dict(numerical_endpoint_residual_norm=float(final_norm[j]),\n            endpoint_correction_norm=float(torch.linalg.vector_norm(z[j])),\n            numerical_iterations=int(updates[j]),\n            actual_endpoint_smallest_singular_value=float(singular[j]),\n            numerical_root_tolerance_met=True, uniform_IFT_conditions_verified=False,\n            exact_continuous_root_certified=False,\n            material_angle_binary64_hex=literal_phi_hex[j],\n            continuation_final_parameter=float(parameter[j]),\n            continuation_stage_attempts=int(attempts[j]),\n            continuation_accepted_stages=int(accepted_stages[j]),\n            continuation_rejected_stages=int(rejected_stages[j]),\n            original_endpoint_equation_read_without_offset=True)\n            for j in range(count)]\n        return z.detach(), A.detach(), records\n\n'
OPERATOR_SHA = '44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e'
GEOMETRY_SHA = 'e4a3271d829a1fc52080b0ac1bdb719f5a13065f23223e64288c77ea6bbc514c'
DRIVER_SHA = 'ff500abfa24de27c22f8a8993b9104cc265c5c96289a927c18755d318fbf0766'
LAUNCHER_SHA = '082bb92e0e9f01067cf1bd8ecaae65cb559e38bba90dd79b97bf492c11d758f4'
READER_SHA = 'c942aa60db84698215e53dd2427a19c693ca73e6c3c8553ef0b73fa75edf295a'
OPERATOR_SCHEMA = 'complete-direct-R690-frozen-Q-residual-continuation-zero-endpoint-layer-v1'
GEOMETRY_SCHEMA = 'complete-frozen-Q-residual-continuation-SO3-geometry-and-all-rows-v1'
DRIVER_SCHEMA = 'complete-independent-fixed-deep-frozen-Q-endpoint-continuation-SO3-QP-v1'


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def read(path, expected):
    source = Path(path).read_text()
    if digest(source) != expected:
        raise ValueError('Changed complete source '+str(path))
    return source


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Need one exact full-source replacement: '+old[:120])
    return text.replace(old, new)


def check(text, name):
    tree = ast.parse(text, filename=name)
    compile(tree, name, 'exec')
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [key.value for key in node.keys if isinstance(key, ast.Constant)]
            if len(keys) != len(set(keys)):
                raise ValueError('Repeated literal dict key in '+name)
    if any(line.rstrip() != line for line in text.splitlines()):
        raise ValueError('Trailing whitespace in '+name)
    return tree


def methods(tree, class_name):
    cls = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == class_name)
    return {node.name: ast.dump(node, include_attributes=False)
        for node in cls.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}


def write(name, text):
    check(text, name)
    (ROOT/name).write_text(text)
    return digest(text)


def main():
    global ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('moment-operator', 'moment-geometry', 'moment-driver', 'moment-launcher', 'moment-reader', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    ROOT = args.outdir.resolve()
    ROOT.mkdir(parents=True, exist_ok=True)
    original_operator = read(args.moment_operator, OPERATOR_SHA)
    original_geometry = read(args.moment_geometry, GEOMETRY_SHA)
    original_driver = read(args.moment_driver, DRIVER_SHA)
    original_launcher = read(args.moment_launcher, LAUNCHER_SHA)
    original_reader = read(args.moment_reader, READER_SHA)
    policy = POLICY_SOURCE
    new_methods = METHOD_SOURCE
    op = once(original_operator,
        "SCHEMA = 'complete-direct-R690-SO3-frozen-moment-Q-zero-endpoint-layer-v1'",
        "SCHEMA = "+repr(OPERATOR_SCHEMA)+"\nCONTINUATION_DERIVED_FROM_SHA256 = "+repr(OPERATOR_SHA))
    op = once(op, 'class EndpointRootFailure(ValueError):', policy+'class EndpointRootFailure(ValueError):')
    op = once(op, 'bubble_nodes, frozen_moment_input, endpoint_policy=None):',
        'bubble_nodes, frozen_moment_input, endpoint_policy=None, continuation_policy=None):')
    op = once(op, "        self.base_source_sha256 = expected_base_source_sha256",
        "        self.continuation_policy = (EndpointContinuationPolicy() if continuation_policy is None\n"
        "                                    else continuation_policy)\n"
        "        if not isinstance(self.continuation_policy, EndpointContinuationPolicy):\n"
        "            raise TypeError('Use one explicit immutable EndpointContinuationPolicy')\n"
        "        self.endpoint_continuation_counts = dict(batches=0, equation_angle_evaluations=0,\n"
        "            jacobian_angle_evaluations=0, stage_attempt_angle_count=0,\n"
        "            accepted_stage_angle_count=0, rejected_stage_angle_count=0,\n"
        "            predictor_angle_count=0, predictor_fallback_angle_count=0,\n"
        "            corrector_newton_updates=0, backtrack_angle_evaluations=0)\n"
        "        self._last_continuation_batch = None\n"
        "        self.base_source_sha256 = expected_base_source_sha256")
    op = once(op,
        "            root_branch='local root in the declared open Euclidean endpoint-coordinate ball; uniform existence/uniqueness remains to be certified',",
        "            root_numerical_method='detached residual continuation to the SAME final endpoint equation',\n"
        "            root_continuation_policy=self.continuation_policy.metadata(),\n"
        "            continuation_derived_from_complete_moment_source_sha256=CONTINUATION_DERIVED_FROM_SHA256,\n"
        "            root_branch='numerical continuation from lambda=0,z=0 inside the same open ball; exact existence, uniqueness and cross-angle association remain unproved',")
    op = once(op,
        "            root_policy=self.policy.metadata(),\n            failed_candidate_is_not_an_accepted_field=True,",
        "            root_policy=self.policy.metadata(),\n"
        "            continuation_policy=self.continuation_policy.metadata(),\n"
        "            continuation_summary=self._continuation_summary(),\n"
        "            failed_candidate_is_not_an_accepted_field=True,")
    start, end = op.index('    def _solve_roots(self, data):'), op.index('    def _finish_jets(')
    op = op[:start]+new_methods+op[end:]
    op = once(op, "            endpoint_root_policy=self.policy.metadata(),",
        "            endpoint_root_policy=self.policy.metadata(),\n"
        "            endpoint_continuation_policy=self.continuation_policy.metadata(),\n"
        "            endpoint_continuation_counts=dict(self.endpoint_continuation_counts),\n"
        "            endpoint_continuation_last_summary=self._continuation_summary(),\n"
        "            endpoint_continuation_last_batch=self._last_continuation_batch,\n"
        "            continuation_counts_scope='actual complete-batch direct C evaluations and separate Cz evaluations (including their internal C graph); Newton updates include subsequently rejected continuation stages',\n"
        "            continuation_trajectory_differentiated=False,\n"
        "            final_implicit_J_uses_original_endpoint_equation=True,\n"
        "            auxiliary_parameter_is_physical_t=False,")
    op = once(op, '            z, A, records = self._solve_roots(subset)',
        '            z, A, records = self._solve_roots(subset, literal_phi_hex=[keys[i] for i in missing])')
    old_methods = methods(ast.parse(original_operator), 'ZeroClosureOperator')
    new_map = methods(check(op, 'operator'), 'ZeroClosureOperator')
    changed = {'__init__', '_fail', '_solve_roots', '_get_roots', 'metadata'}
    for name in old_methods:
        if name not in changed and new_map.get(name) != old_methods[name]:
            raise ValueError('Unpaid original physical/implicit method change: '+name)
    oh = write('so3_zero_moment_continuation_operator.py', op)
    geom = once(original_geometry,
        "SCHEMA = 'complete-frozen-moment-Q-zero-SO3-world-geometry-and-original-192-amplitude-rows-v1'",
        'SCHEMA = '+repr(GEOMETRY_SCHEMA))
    geom = once(geom,
        "OPERATOR_SCHEMA = 'complete-direct-R690-SO3-frozen-moment-Q-zero-endpoint-layer-v1'",
        'OPERATOR_SCHEMA = '+repr(OPERATOR_SCHEMA))
    geom = once(geom, "ENDPOINT_SOURCE_SHA256 = "+repr(OPERATOR_SHA), "ENDPOINT_SOURCE_SHA256 = "+repr(oh))
    gh = write('so3_zero_moment_continuation_geometry.py', geom)
    driver = once(original_driver,
        "SCHEMA = 'complete-independent-axisymmetric-fixed-deep-frozen-moment-Q-zero-SO3-QP-v1'",
        'SCHEMA = '+repr(DRIVER_SCHEMA))
    driver = driver.replace('so3_zero_closure_moment_operator.py', 'so3_zero_moment_continuation_operator.py')
    driver = driver.replace('so3_zero_closure_moment_geometry.py', 'so3_zero_moment_continuation_geometry.py')
    driver = once(driver, OPERATOR_SHA, oh)
    driver = once(driver, GEOMETRY_SHA, gh)
    flags = (
        "    p.add_argument('--endpoint-continuation-initial-step', type=float, default=.25)\n"
        "    p.add_argument('--endpoint-continuation-minimum-step', type=float, default=1./65536)\n"
        "    p.add_argument('--endpoint-continuation-growth', type=float, default=1.5)\n"
        "    p.add_argument('--endpoint-continuation-shrink', type=float, default=.5)\n"
        "    p.add_argument('--endpoint-continuation-stage-attempts', type=int, default=64)\n"
        "    p.add_argument('--endpoint-continuation-predictor', type=int, choices=(0,1), default=1)\n")
    marker = "    p.add_argument('--endpoint-root-branch-radius', type=float, default=.5)\n"
    driver = once(driver, marker, marker+flags)
    policy_creation = (
        "    continuation_policy = endpoint.EndpointContinuationPolicy(\n"
        "        initial_step=args.endpoint_continuation_initial_step,\n"
        "        minimum_step=args.endpoint_continuation_minimum_step,\n"
        "        growth=args.endpoint_continuation_growth, shrink=args.endpoint_continuation_shrink,\n"
        "        maximum_stage_attempts=args.endpoint_continuation_stage_attempts,\n"
        "        predictor=bool(args.endpoint_continuation_predictor))\n")
    driver = once(driver, "    bubble_nodes = [[getattr(args, 'endpoint_bubble_'+str(i)+'_'+position)",
        policy_creation+"    bubble_nodes = [[getattr(args, 'endpoint_bubble_'+str(i)+'_'+position)")
    driver = once(driver,
        "bubble_nodes=bubble_nodes, frozen_moment_input=frozen_moment_input, endpoint_policy=root_policy)",
        "bubble_nodes=bubble_nodes, frozen_moment_input=frozen_moment_input, endpoint_policy=root_policy,\n"
        "        continuation_policy=continuation_policy)")
    driver = once(driver, "        moment_Q_recomputed_from_current_free_point=False,",
        "        moment_Q_recomputed_from_current_free_point=False,\n"
        "        endpoint_continuation_is_an_auxiliary_numerical_method=True,\n"
        "        endpoint_continuation_changes_fixed_g=False,\n"
        "        endpoint_continuation_trajectory_differentiated=False,\n"
        "        endpoint_continuation_final_equation_is_original_C=True,")
    driver = once(driver,
        "            endpoint_root_policy=root_policy.metadata(), exact_relative_bubble_nodes=q.model['exact_relative_bubble_nodes'],",
        "            endpoint_root_policy=root_policy.metadata(),\n"
        "            endpoint_continuation_policy=continuation_policy.metadata(),\n"
        "            exact_relative_bubble_nodes=q.model['exact_relative_bubble_nodes'],")
    old_tail = original_driver[original_driver.index('    def save_report():'):]
    if driver[driver.index('    def save_report():'):] != old_tail:
        raise ValueError('Do not change the complete actual field/QP/Phase I/true line-search body')
    dh = write('fullclosed_zero_moment_continuation_so3_qp.py', driver)
    launcher = once(original_launcher, DRIVER_SHA, dh)
    launcher = launcher.replace('fullclosed_zero_moment_so3_qp.py',
                                'fullclosed_zero_moment_continuation_so3_qp.py')
    launcher = once(launcher, marker, marker+flags)
    launcher = once(launcher,
        "schema='public-actions-complete-independent-frozen-moment-Q-zero-SO3-command-v1'",
        "schema='public-actions-complete-frozen-Q-endpoint-continuation-SO3-command-v1'")
    lh = write('launch_zero_moment_continuation_so3_actions.py', launcher)
    reader = once(original_reader, DRIVER_SHA, dh)
    reader = reader.replace('fullclosed_zero_moment_so3_qp.py',
                            'fullclosed_zero_moment_continuation_so3_qp.py')
    reader = reader.replace('complete-independent-axisymmetric-fixed-deep-frozen-moment-Q-zero-SO3-QP-v1',
                            DRIVER_SCHEMA)
    reader = reader.replace('complete-direct-R690-SO3-frozen-moment-Q-zero-endpoint-layer-v1',
                            OPERATOR_SCHEMA)
    reader = once(reader, "        'endpoint_counts', 'last_root_failure')",
        "        'endpoint_counts', 'last_root_failure', 'endpoint_continuation_policy',\n"
        "        'endpoint_continuation_counts', 'endpoint_continuation_last_summary')")
    anchor = "    base = value['base_complete_metadata']\n"
    reader = once(reader, anchor,
        "    if (value.get('endpoint_continuation_policy') != model.get('root_continuation_policy')\n"
        "            or value.get('endpoint_continuation_policy') != working_evaluation.get('endpoint_continuation_policy')\n"
        "            or value.get('continuation_trajectory_differentiated') is not False\n"
        "            or value.get('final_implicit_J_uses_original_endpoint_equation') is not True\n"
        "            or value.get('auxiliary_parameter_is_physical_t') is not False):\n"
        "        raise ValueError('Keep the auxiliary continuation and final original implicit equation distinct')\n"+anchor)
    reader = once(reader, "    return dict(current=current, all_attempted={key: value[key] for key in names},",
        "    return dict(current=current, all_attempted={key: value[key] for key in names},\n"
        "        continuation_policy=value['endpoint_continuation_policy'],\n"
        "        actual_continuation_counts=value['endpoint_continuation_counts'],\n"
        "        last_continuation_summary=value['endpoint_continuation_last_summary'],\n"
        "        complete_last_continuation_batch=value['endpoint_continuation_last_batch'],\n"
        "        continuation_counts_scope=value['continuation_counts_scope'],")
    anchor = "    seed = report.get('direct_base_seed')\n"
    reader = once(reader, anchor,
        "    if (working.get('endpoint_continuation_policy') != model.get('root_continuation_policy')\n"
        "            or report.get('endpoint_continuation_is_an_auxiliary_numerical_method') is not True\n"
        "            or report.get('endpoint_continuation_changes_fixed_g') is not False\n"
        "            or report.get('endpoint_continuation_trajectory_differentiated') is not False\n"
        "            or report.get('endpoint_continuation_final_equation_is_original_C') is not True):\n"
        "        raise ValueError('This source is a complete same-final-equation continuation entry')\n"+anchor)
    reader = once(reader,
        "schema='actual-complete-independent-frozen-moment-Q-zero-SO3-scalar-readout-v1'",
        "schema='actual-complete-frozen-Q-endpoint-continuation-SO3-scalar-readout-v1'")
    rh = write('read_zero_moment_continuation_so3_report.py', reader)
    output = dict(operator=oh, geometry=gh, driver=dh, launcher=lh, reader=rh,
        complete_operator_original_methods_unchanged=sorted(set(old_methods)-changed),
        scientific_calculation_run=False, old_driver_from_save_report_to_EOF_byte_identical=True)
    (ROOT/'source-derivation.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
