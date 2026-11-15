#!/usr/bin/env python3
"""R351: complete seven-state literal-chain adjoint; requestless Actions API.

No science runs on import. All arithmetic entries require the original
public Actions environment and the same explicit Decimal50 context.
No parent, new shape, candidate, trial or accepted nonzero field is invented.
"""
from __future__ import annotations
from decimal import Decimal
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import traceback

SCHEMA = "literal-seven-state-three-output-adjoint-and-sampled-shape-response-v1"
BASE_NAME = "geometry_20261115_nine_control_decimal_literal_model.py"
BASE_BYTES = 23719
BASE_SHA256 = "2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75"
FAMILY_SHA256 = "086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629"
NODE_COUNT, CELL_COUNT, FULL_ROWS = 699, 698, 112
_BASE = None


class AdjointInputError(ValueError):
    pass


class AdjointBudgetStop(RuntimeError):
    pass


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Scientific arithmetic is restricted to this public repository Actions")


def file_identity(path):
    raw = Path(path).read_bytes()
    return dict(name=Path(path).name, bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest())


def load_base():
    global _BASE
    require_actions()
    if _BASE is None:
        path = Path(__file__).with_name(BASE_NAME)
        actual = file_identity(path)
        if actual["bytes"] != BASE_BYTES or actual["sha256"] != BASE_SHA256:
            raise AdjointInputError("Frozen Decimal literal base bytes differ")
        name = "_r351_frozen_literal_" + BASE_SHA256[:16]
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise AdjointInputError("Cannot load the explicitly pinned literal base")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        _BASE = module
    return _BASE


def bound_source(record, label):
    if not isinstance(record, dict):
        raise AdjointInputError(label + " requires an explicit source identity")
    name = record.get("name")
    if (not isinstance(name, str) or name != Path(name).name
            or not name.endswith(".py") or "/" in name or "\\" in name):
        raise AdjointInputError(label + " must be a computation basename")
    actual = file_identity(Path(__file__).with_name(name))
    if actual["bytes"] != record.get("bytes") or actual["sha256"] != record.get("sha256"):
        raise AdjointInputError(label + " source bytes differ")
    return actual


def decimal_copy(value, shape, label):
    if not shape:
        if not isinstance(value, Decimal) or not value.is_finite():
            raise AdjointInputError(label + " must retain an existing finite Decimal word")
        return value
    if not isinstance(value, (tuple, list)) or len(value) != shape[0]:
        raise AdjointInputError(label + " has the wrong complete shape")
    return [decimal_copy(x, shape[1:], label + "[" + str(i) + "]")
            for i, x in enumerate(value)]


def metadata_copy(value, label):
    try:
        return json.loads(json.dumps(value, sort_keys=True, ensure_ascii=True,
                                     allow_nan=False, separators=(",", ":")))
    except (TypeError, ValueError) as error:
        raise AdjointInputError(label + " must be ordinary finite provenance metadata") from error


def vector_comparison(base, actual, expected):
    if len(actual) != len(expected):
        raise AdjointInputError("Compared complete vector dimensions differ")
    return dict(length=len(actual),
        word_equal=all(str(a) == str(e) for a, e in zip(actual, expected)),
        actual_canonical_sha256=base.digest(actual),
        expected_canonical_sha256=base.digest(expected),
        differing_coordinates=[dict(coordinate=i, actual=a, expected=e)
            for i, (a, e) in enumerate(zip(actual, expected)) if str(a) != str(e)])


def transpose_action(matrix, right, zero):
    return [[sum((matrix[k][i]*right[k][j] for k in range(len(matrix))), zero)
             for j in range(len(right[0]))] for i in range(len(matrix[0]))]


class SevenStateAdjoint:
    """One actual persistent point; full local ten-column variations.

    binding contains producer {name,bytes,sha256}, the actual
    expected_literal_binding_sha256, nine actual_parameter_words, and explicit
    parameter_origin metadata. This checks supplied identities; it does not
    independently fetch a historical log or certify historical acceptance.
    """
    def __init__(self, model, state, binding, *, event_sink=None, deadline=None):
        require_actions()
        self.b = b = load_base()
        self.event_sink = event_sink or (lambda event: None)
        self.deadline = deadline
        self.started = time.monotonic()
        self.stage = "bind actual persistent model/state"
        self.complete = False
        self.A, self.C, self.cell_word_checks = [], [], []
        self.reverse_rows_completed = 0
        self.terminal = None
        self.node_weights = self.mid_weights = self.start_cotangent = None
        self.shape_results = []
        self.failure = None
        self.counts = dict(local_forward_calls=0, local_forward_columns=0,
            terminal_forward_calls=0, terminal_forward_columns=0, reverse_cells=0,
            sampled_shape_attempts=0, sampled_shape_returns=0,
            scientific_primal_model_evaluate_calls=0, original_model_response_calls=0,
            trial_or_optimizer_calls=0)
        if not isinstance(binding, dict):
            raise AdjointInputError("Require the actual source/parameter binding")
        producer = bound_source(binding.get("producer"), "Independent producer")
        origin = metadata_copy(binding.get("parameter_origin"), "Parameter origin")
        if not isinstance(origin, dict) or not origin:
            raise AdjointInputError("Parameter origin must be explicit")
        if getattr(model, "M", None) != FULL_ROWS:
            raise AdjointInputError("Retain all original112 terminal rows and columns")
        original_binding = dict(model.binding)
        expected = original_binding.pop("canonical_binding_sha256", None)
        if expected != b.digest(original_binding):
            raise AdjointInputError("Actual literal binding has inconsistent canonical bytes")
        if expected != binding.get("expected_literal_binding_sha256"):
            raise AdjointInputError("Supplied point belongs to another literal model")
        if (original_binding.get("schema") != b.MODEL_SCHEMA
                or original_binding.get("decimal_digits") != b.PRECISION
                or original_binding.get("parameter_dimension") != 9
                or original_binding.get("original_mesh_nodes") != NODE_COUNT):
            raise AdjointInputError("The required original literal model contract differs")
        if original_binding.get("original149_primal_source_sha256", BASE_SHA256) != BASE_SHA256:
            raise AdjointInputError("A derivative wrapper bound another primal source")
        self.parameters = decimal_copy(state["parameters"], [9], "actual parameters")
        if binding.get("actual_parameter_words") != [str(x) for x in self.parameters]:
            raise AdjointInputError("Parameter provenance differs from persistent words")
        self.h = decimal_copy(model.h, [CELL_COUNT], "literal cell widths")
        self.x = decimal_copy(model.x, [NODE_COUNT], "literal nodes")
        self.mid = decimal_copy(model.mid, [CELL_COUNT], "literal midpoints")
        self.controls = decimal_copy(model.controls, [NODE_COUNT, 2, 9], "original node controls")
        self.controls_mid = decimal_copy(model.controls_mid, [CELL_COUNT, 2, 9], "original mid controls")
        self.J = decimal_copy(model.J, [FULL_ROWS, FULL_ROWS], "complete original terminal J")
        self.target = decimal_copy(model.target, [3], "original three targets")
        self.gamma = decimal_copy(model.gamma, [], "original cut scale")
        self.eh = decimal_copy(model.eh, [], "original height sign")
        self.exactly_diagonal = bool(model.exactly_diagonal)
        if self.exactly_diagonal != original_binding["exactly_diagonal_as_original_record"]:
            raise AdjointInputError("The original diagonal branch identity changed")
        self.scalar_nodes = decimal_copy(state["scalar_nodes"], [NODE_COUNT, 2], "actual scalar nodes")
        self.scalar_middle = decimal_copy(state["scalar_middle"], [CELL_COUNT, 2], "actual scalar midpoints")
        self.q = decimal_copy(state["ratio"], [NODE_COUNT], "actual node ratios")
        self.qm = decimal_copy(state["ratio_mid"], [CELL_COUNT], "actual midpoint ratios")
        radius = decimal_copy(state["radius"], [NODE_COUNT], "actual radius state")
        modes = decimal_copy(state["modes"], [NODE_COUNT, 3, 2], "actual three-mode state")
        self.frames = [[radius[i]] + [v for pair in modes[i] for v in pair] for i in range(NODE_COUNT)]
        self.original_equation = decimal_copy(state["equation"], [3], "actual original equations")
        self.original_full_right = decimal_copy(state["full_right"], [FULL_ROWS], "actual full right residual")
        fixed_start = [b.ONE, b.ONE, b.ZERO, b.ONE, b.ZERO, b.ONE, b.ZERO]
        if self.frames[0] != fixed_start:
            raise AdjointInputError("This helper fixes the original parameter-independent start")
        self.binding = dict(schema=SCHEMA,
            actual_helper_source=file_identity(__file__), independent_producer=producer,
            frozen_primal_source=dict(name=BASE_NAME, bytes=BASE_BYTES, sha256=BASE_SHA256),
            original_nine_family_source_sha256=FAMILY_SHA256,
            literal_model_binding=original_binding, literal_model_binding_sha256=expected,
            actual_parameter_words=[str(x) for x in self.parameters], parameter_origin=origin,
            historical_parameter_acceptance_independently_fetched_here=False,
            retained_state_projection_canonical_sha256=b.digest(dict(
                parameters=self.parameters, frames=self.frames, q=self.q, qm=self.qm,
                scalar_nodes=self.scalar_nodes, scalar_middle=self.scalar_middle,
                equation=self.original_equation, full_right=self.original_full_right)),
            retained_projection_is_not_the_complete_original_state_file=True,
            actual_used_decimal_coefficients_canonical_sha256=b.digest(dict(
                h=self.h, nodes=self.x, middle=self.mid, controls=self.controls,
                controls_mid=self.controls_mid, terminal_J=self.J,
                target=self.target, gamma=self.gamma, eh=self.eh)),
            actual_decimal_coefficient_digest_is_not_a_new_independent_binary64_source_audit=True,
            original_mesh_and_controls_are_fixed_literal_tables=True,
            complete_original_terminal_J_kept=True,
            terminal_inputs_gamma_eh_J_target_fixed_by_model_definition=True,
            actual_original_diagonal_branch=self.exactly_diagonal,
            original_start_is_fixed_parameter_independent=True,
            original_height_not_in_three_equation_state_but_final_circle_still_required=True,
            no_parameter_projection_to_binary64=True,
            new_shape_or_parameter_family_selected=False, accepted_nonzero_field_claimed=False)
        self.binding["canonical_sha256"] = b.digest(self.binding)

    def _check_deadline(self):
        require_actions()
        if self.deadline is not None and time.monotonic() >= self.deadline:
            raise AdjointBudgetStop("Explicit operation wall deadline reached between operations")

    def _emit(self, kind, **fields):
        self.event_sink(dict(kind=kind, helper_schema=SCHEMA,
            stage=self.stage, counts=dict(self.counts), **fields))

    def _matrix(self, q, r):
        b = self.b
        speed = [a*c for a, c in zip(q, r)]
        vertical = [b.sqrt_positive(b.ONE-a*a) for a in speed]
        # The frozen body uses q/r/s/z only; no caller method override.
        return b.LiteralCircleModel.matrix(None, q, r, speed, vertical)

    def _cell(self, x, z, h):
        b = self.b
        ql, qm, qr = z
        rl = x[0]
        left = -b.ONE-h*(ql+b.TWO*qm)/6-h*h*qm*ql/12
        right = b.ONE-h*(qr+b.TWO*qm)/6+h*h*qm*qr/12
        if b.value(right) == 0 or not b.value(right).is_finite():
            raise b.NumericalFailure("Original radius cell denominator failed")
        rr = -left*rl/right
        rm = (rl+rr)/b.TWO-h*(qr*rr-ql*rl)/8
        if any(b.value(r) <= 0 or not b.value(r).is_finite() for r in (rl, rm, rr)):
            raise b.NumericalFailure("Original local radius positivity failed")
        matrices = self._matrix([ql, qm, qr], [rl, rm, rr])
        answer = [rr]
        for k in range(3):
            bl, bm, br = matrices[0][k], matrices[1][k], matrices[2][k]
            ml, mr = b.m2m(bm, bl), b.m2m(bm, br)
            left_mode = [[-(b.ONE if a == c else b.ZERO)-h*(bl[a][c]+b.TWO*bm[a][c])/6
                          -h*h*ml[a][c]/12 for c in range(2)] for a in range(2)]
            right_mode = [[(b.ONE if a == c else b.ZERO)-h*(br[a][c]+b.TWO*bm[a][c])/6
                           +h*h*mr[a][c]/12 for c in range(2)] for a in range(2)]
            prior = x[1+2*k:3+2*k]
            rhs = [-v for v in b.m2v(left_mode, prior)]
            solved = b.solve2(right_mode, rhs)
            if any(not b.value(v).is_finite() for v in solved):
                raise b.NumericalFailure("Original local low-mode transfer is nonfinite")
            answer.extend(solved)
        return answer

    def _terminal(self, x, q):
        b = self.b
        matrices = self._matrix([q], [x[0]])[0]
        modes = [x[1+2*k:3+2*k] for k in range(3)]
        velocity = [b.m2v(matrices[k], modes[k]) for k in range(3)]
        native = [b.ZERO]*FULL_ROWS
        for k in range(3):
            native[k] = self.eh*self.target[k]*modes[k][1]
        full = [-self.gamma*sum((self.J[j][k]*native[k] for k in range(FULL_ROWS)), b.ZERO)
                for j in range(FULL_ROWS)]
        for k in range(3):
            full[k] = full[k]+self.target[k]*velocity[k][1]
        unit = [velocity[k][1]-self.gamma*self.eh*self.J[k][k]*modes[k][1] for k in range(3)]
        equation = unit if self.exactly_diagonal else full[:3]
        return equation, full

    def build(self):
        require_actions()
        if self.complete or self.A or self.terminal is not None or self.failure is not None:
            raise AdjointInputError("Build once; a partial build is not silently resumed")
        b = self.b
        try:
            with b.precision_context():
                self.stage = "all698 local seven-state/three-ratio variations"
                for j in range(CELL_COUNT):
                    self._check_deadline()
                    inputs = self.frames[j] + [self.q[j], self.qm[j], self.q[j+1]]
                    jets = [b.Jet(v, [b.ONE if i == k else b.ZERO for k in range(10)])
                            for i, v in enumerate(inputs)]
                    self.counts["local_forward_calls"] += 1
                    self.counts["local_forward_columns"] += 10
                    answer = self._cell(jets[:7], jets[7:], self.h[j])
                    if any(not x.v.is_finite() or any(not d.is_finite() for d in x.d) for x in answer):
                        raise b.NumericalFailure("Nonfinite local seven-by-ten variation")
                    self.A.append([list(v.d[:7]) for v in answer])
                    self.C.append([list(v.d[7:]) for v in answer])
                    actual = [v.v for v in answer]
                    self.cell_word_checks.append(dict(cell=j,
                        **vector_comparison(b, actual, self.frames[j+1])))
                    if (j+1) % 32 == 0 or j+1 == CELL_COUNT:
                        self._emit("literal-adjoint-local-progress", cells_formed=j+1,
                                   remaining_cells=CELL_COUNT-j-1)
                self._check_deadline()
                self.stage = "complete112 terminal rows and original three equations"
                inputs = self.frames[-1] + [self.q[-1]]
                jets = [b.Jet(v, [b.ONE if i == k else b.ZERO for k in range(8)])
                        for i, v in enumerate(inputs)]
                self.counts["terminal_forward_calls"] += 1
                self.counts["terminal_forward_columns"] += 8
                eq, full = self._terminal(jets[:7], jets[7])
                if any(not b.value(x).is_finite() or
                       (isinstance(x, b.Jet) and any(not a.is_finite() for a in x.d))
                       for x in eq+full):
                    raise b.NumericalFailure("Nonfinite complete terminal variation")
                def derivative(v):
                    return list(v.d) if isinstance(v, b.Jet) else [b.ZERO]*8
                eqd, fd = [derivative(v) for v in eq], [derivative(v) for v in full]
                self.terminal = dict(equation_state_J=[row[:7] for row in eqd],
                    equation_direct_q=[row[7] for row in eqd],
                    full112_state_J=[row[:7] for row in fd],
                    full112_direct_q=[row[7] for row in fd],
                    equation_word_comparison=vector_comparison(b, [b.value(x) for x in eq], self.original_equation),
                    full112_word_comparison=vector_comparison(b, [b.value(x) for x in full], self.original_full_right),
                    full_original_J_rows_and_columns_consumed=True,
                    fixed_input_theta_variation_is_zero_by_definition=True,
                    terminal_direct_profile_ratio_term_retained=True)
                self.stage = "three-column reverse propagation and shared-ratio scatter"
                lam = b.transpose(self.terminal["equation_state_J"])
                nodes = [[b.ZERO]*3 for unused in range(NODE_COUNT)]
                mids = [[b.ZERO]*3 for unused in range(CELL_COUNT)]
                nodes[-1] = list(self.terminal["equation_direct_q"])
                for j in range(CELL_COUNT-1, -1, -1):
                    self._check_deadline()
                    local = transpose_action(self.C[j], lam, b.ZERO)
                    for k in range(3):
                        nodes[j][k] = nodes[j][k]+local[0][k]
                        mids[j][k] = mids[j][k]+local[1][k]
                        nodes[j+1][k] = nodes[j+1][k]+local[2][k]
                    lam = transpose_action(self.A[j], lam, b.ZERO)
                    self.reverse_rows_completed += 1
                    self.counts["reverse_cells"] += 1
                if any(not v.is_finite() for array in (nodes, mids, lam) for row in array for v in row):
                    raise b.NumericalFailure("Nonfinite three-column reverse weights")
                self.node_weights, self.mid_weights, self.start_cotangent = nodes, mids, lam
                self.complete = True
                self.stage = "complete local adjoint; no new candidate evaluated"
        except Exception as error:
            self.failure = dict(stage=self.stage, exception=repr(error),
                complete_traceback=traceback.format_exc(),
                resource_partial=isinstance(error, AdjointBudgetStop),
                scientific_nonexistence_inferred=False)
            raise
        finally:
            self._emit("literal-adjoint-build-result", report=self.report())
        return self

    def report(self):
        require_actions()
        b = self.b
        arrays = dict(A=self.A, C=self.C)
        if self.terminal is not None:
            arrays["terminal"] = self.terminal
        if self.node_weights is not None:
            arrays.update(node_weights=self.node_weights,
                midpoint_weights=self.mid_weights, start_cotangent=self.start_cotangent)
        return dict(schema=SCHEMA, complete=self.complete, stage=self.stage,
            binding=self.binding, counts=dict(self.counts),
            local_cells_required=CELL_COUNT, local_cells_formed=len(self.A),
            local_unvisited_suffix=list(range(len(self.A), CELL_COUNT)),
            reverse_cells_completed=self.reverse_rows_completed,
            reverse_unvisited_prefix=list(range(CELL_COUNT-self.reverse_rows_completed)),
            terminal_complete=self.terminal is not None,
            terminal_original_equation_word_comparison=(None if self.terminal is None else
                self.terminal["equation_word_comparison"]),
            terminal_original_full112_word_comparison=(None if self.terminal is None else
                self.terminal["full112_word_comparison"]),
            local_primal_seven_state_comparisons=len(self.cell_word_checks),
            local_primal_word_mismatch_cells=[
                row["cell"] for row in self.cell_word_checks if not row["word_equal"]],
            local_word_comparisons_complete_canonical_sha256=b.digest(self.cell_word_checks),
            local_word_mismatches_are_observations_not_new_acceptance_gates=True,
            formed_arrays=[dict(name=name, canonical_sha256=b.digest(value))
                           for name, value in arrays.items()],
            start_cotangent=self.start_cotangent,
            direct_terminal_ratio_response=(None if self.terminal is None else self.terminal["equation_direct_q"]),
            elapsed_wall_seconds=format(time.monotonic()-self.started, ".9f"), failure=self.failure,
            computed_linearization="rounded Decimal50 of original real-expression local arithmetic",
            identical_rounding_to_original_full_forward_not_claimed=True,
            exact_derivative_or_interval_error_or_rank_certificate_claimed=False,
            native_current_tail_or_nonlinear_final_checks_completed=False,
            future_new_shape_primal_domain_and_full112_evaluation_still_required=True)

    def formed_arrays(self):
        """Actual in-memory arrays; no upload, file persistence or implicit printing."""
        require_actions()
        if not self.complete:
            raise AdjointInputError("Complete arrays require a complete build")
        return dict(local_state_J=self.A, local_ratio_J=self.C,
            complete_terminal=self.terminal, node_weights=self.node_weights,
            midpoint_weights=self.mid_weights, start_cotangent=self.start_cotangent,
            complete_local_word_checks=self.cell_word_checks)

    def _shape_binding(self, binding, *, original_axis=None):
        b = self.b
        if original_axis is not None:
            return dict(kind="original-nine-control-table-column", column=original_axis,
                family_source_sha256=FAMILY_SHA256,
                literal_model_binding_sha256=self.binding["literal_model_binding_sha256"],
                actual_parameter_words=self.binding["actual_parameter_words"],
                source_table_shapes=dict(nodes=[NODE_COUNT, 2, 9], midpoints=[CELL_COUNT, 2, 9]),
                original_control_array_identities={
                    name:self.binding["literal_model_binding"]["arrays"][name]
                    for name in ("controls", "controls_mid")},
                represents_a_new_nonlinear_family=False)
        if not isinstance(binding, dict) or binding.get("kind") != "independent-sampled-scalar-shape":
            raise AdjointInputError("A new sampled shape requires its own explicit source/definition")
        if binding.get("coefficient_is_an_original_nine_parameter") is not False:
            raise AdjointInputError("A new shape coefficient is outside the original nine coordinates")
        source = bound_source(binding.get("source"), "New shape definition")
        if source["sha256"] in (BASE_SHA256, FAMILY_SHA256):
            raise AdjointInputError("New shapes require their own defining source")
        definition = metadata_copy(binding.get("definition"), "New shape definition")
        coordinates = metadata_copy(binding.get("coordinate_contract"), "Shape coordinate contract")
        if (not isinstance(definition, dict)
                or any(not definition.get(key) for key in ("family_schema", "formula", "support", "zero_jet_proof_reference"))
                or not isinstance(coordinates, dict)
                or coordinates.get("derivative_column") != "derivative with respect to original scalar-table coordinate"):
            raise AdjointInputError("Bind actual shape values/derivatives in the original coordinate")
        if coordinates.get("literal_mesh_canonical_sha256") != b.digest(dict(nodes=self.x, middle=self.mid)):
            raise AdjointInputError("Shape samples refer to another fixed node/midpoint mesh")
        return dict(kind=binding["kind"], source=source, definition=definition,
            coordinate_contract=coordinates, coefficient_is_an_original_nine_parameter=False,
            smoothness_and_zero_jets_proved_by_samples_alone=False,
            new_nonlinear_family_and_complete_primal_not_supplied_by_this_helper=True)

    def _sampled_shape_response(self, node_pairs, middle_pairs, shape_binding, *, original_axis=None):
        if not self.complete:
            raise AdjointInputError("Build the complete original local adjoint first")
        b = self.b
        self.counts["sampled_shape_attempts"] += 1
        self.stage = "bind one actual sampled shape"
        event = dict(kind="literal-adjoint-sampled-shape", returned=False)
        forward_cells = 0
        try:
            self._check_deadline()
            nodes = decimal_copy(node_pairs, [NODE_COUNT, 2], "shape node value/derivative")
            mids = decimal_copy(middle_pairs, [CELL_COUNT, 2], "shape midpoint value/derivative")
            source = self._shape_binding(shape_binding, original_axis=original_axis)
            event["shape_binding"] = source
            with b.precision_context():
                self.stage = "one explicit sampled-shape contraction"
                def ratios(samples, scalars, original):
                    actions, differences = [], []
                    for j, (hp, ap, recorded_q) in enumerate(zip(samples, scalars, original)):
                        actual = b.Jet(ap[1], [hp[1]])/b.Jet(ap[0], [hp[0]])
                        actions.append(actual.d[0])
                        if str(actual.v) != str(recorded_q):
                            differences.append(dict(index=j, reformed_ratio=actual.v, original_ratio=recorded_q))
                    return actions, differences
                dq, qdiff = ratios(nodes, self.scalar_nodes, self.q)
                dqm, qmdiff = ratios(mids, self.scalar_middle, self.qm)
                adjoint = []
                for k in range(3):
                    node_sum = sum((self.node_weights[j][k]*dq[j] for j in range(NODE_COUNT)), b.ZERO)
                    mid_sum = sum((self.mid_weights[j][k]*dqm[j] for j in range(CELL_COUNT)), b.ZERO)
                    adjoint.append(node_sum+mid_sum)
                # Forward action of the same formed local linear system, not
                # another nonlinear evaluate, model Jacobian or FD call.
                dx = [b.ZERO]*7
                for j in range(CELL_COUNT):
                    self._check_deadline()
                    dz = [dq[j], dqm[j], dq[j+1]]
                    ax, cz = b.mv(self.A[j], dx), b.mv(self.C[j], dz)
                    dx = [a+c for a, c in zip(ax, cz)]
                    forward_cells += 1
                eq = [a+c*dq[-1] for a, c in zip(
                    b.mv(self.terminal["equation_state_J"], dx), self.terminal["equation_direct_q"])]
                full = [a+c*dq[-1] for a, c in zip(
                    b.mv(self.terminal["full112_state_J"], dx), self.terminal["full112_direct_q"])]
                if any(not a.is_finite() for a in adjoint+eq+full+dx):
                    raise b.NumericalFailure("Nonfinite complete sampled-shape action")
                result = dict(schema=SCHEMA, complete=True, shape_binding=source,
                    actual_parameter_words=self.binding["actual_parameter_words"],
                    literal_model_binding_sha256=self.binding["literal_model_binding_sha256"],
                    shape_sample_identity=dict(nodes_shape=[NODE_COUNT, 2], middle_shape=[CELL_COUNT, 2],
                        nodes_canonical_sha256=b.digest(nodes), middle_canonical_sha256=b.digest(mids)),
                    ratio_action_identity=dict(nodes_canonical_sha256=b.digest(dq),
                        middle_canonical_sha256=b.digest(dqm)),
                    ratio_reformation_word_differences=dict(nodes=qdiff, middle=qmdiff),
                    adjoint_complete_three_response=adjoint,
                    formed_local_forward_complete_three_response=eq,
                    actual_adjoint_minus_formed_forward=[a-c for a, c in zip(adjoint, eq)],
                    complete112_formed_local_forward_response=full,
                    complete112_response_canonical_sha256=b.digest(full),
                    complete_forward_cells=forward_cells,
                    terminal_state_action=dx, direct_terminal_q_action=dq[-1],
                    direct_terminal_three_contribution=[a*dq[-1] for a in self.terminal["equation_direct_q"]],
                    initial_state_action=[b.ZERO]*7,
                    fixed_start_justification="Original r0=1 and three (1,0) states are parameter-independent",
                    actual_full3_merit_directional_action=b.dot(self.original_equation, adjoint),
                    actual_full3_merit_directional_action_from_local_forward=b.dot(self.original_equation, eq),
                    original_three_equations=self.original_equation,
                    original_full3_merit=b.dot(self.original_equation, self.original_equation)/b.TWO,
                    original_Armijo_coefficient_exact_binary64_lift=b.ARM,
                    new_trial_or_acceptance_performed=False,
                    action_sign_or_smallest_singular_value_certified=False,
                    original_caller_domain_FD_circle_native_final_obligations_unchanged=True)
                self.counts["sampled_shape_returns"] += 1
                self.shape_results.append(result)
                event.update(returned=True, result=result)
                return result
        except Exception as error:
            event.update(exception=repr(error), complete_traceback=traceback.format_exc(),
                forward_cells_completed=forward_cells,
                unvisited_forward_suffix=list(range(forward_cells, CELL_COUNT)),
                resource_partial=isinstance(error, AdjointBudgetStop),
                scientific_nonexistence_inferred=False)
            raise
        finally:
            self._emit("literal-adjoint-shape-result", original_event=event)

    def sampled_shape_response(self, node_pairs, middle_pairs, shape_binding):
        """Distinct new shape; never an overwritten original nine coordinate."""
        require_actions()
        return self._sampled_shape_response(node_pairs, middle_pairs, shape_binding)

    def original_nine_response(self, *, already_computed_reference=None,
                               reference_literal_binding_sha256=None):
        """All original columns; optional existing same-point axis-nine report.

        No original evaluate/response/FD call is made. The supplied reference
        report must contain actual_parameters, physical_seed,
        complete_three_row_response and forward_column_count. Its actual
        literal binding is supplied separately and must match this model.
        """
        require_actions()
        b = self.b
        columns = []
        try:
            for column in range(9):
                self._check_deadline()
                nodes = [[row[0][column], row[1][column]] for row in self.controls]
                mids = [[row[0][column], row[1][column]] for row in self.controls_mid]
                columns.append(self._sampled_shape_response(nodes, mids, None, original_axis=column))
            response = b.transpose([row["adjoint_complete_three_response"] for row in columns])
            full = b.transpose([row["complete112_formed_local_forward_response"] for row in columns])
            comparison = dict(provided=False, original_forward_recomputed_here=False)
            if already_computed_reference is not None:
                record = already_computed_reference
                if reference_literal_binding_sha256 != self.binding["literal_model_binding_sha256"]:
                    raise AdjointInputError("Bind the existing forward reference to this actual literal model")
                if (record.get("forward_column_count") != 9
                        or [str(x) for x in record.get("actual_parameters", [])] != self.binding["actual_parameter_words"]):
                    raise AdjointInputError("Existing original response refers to another point/seed count")
                reference = decimal_copy(record["complete_three_row_response"], [3, 9],
                                         "existing original full response")
                seed = decimal_copy(record["physical_seed"], [9, 9], "existing original axis seed")
                if [[str(x) for x in row] for row in seed] != [[str(x) for x in row] for row in b.eye(9)]:
                    raise AdjointInputError("Original axis-nine comparison requires its recorded identity seed")
                with b.precision_context():
                    comparison.update(provided=True,
                        reference_canonical_sha256=b.digest(reference),
                        existing_reference_report_canonical_sha256=b.digest(record),
                        complete_original_three_by_nine_response=reference,
                        actual_adjoint_minus_original_forward=[
                            [response[i][j]-reference[i][j] for j in range(9)] for i in range(3)],
                        complete112_original_response_canonical_sha256=record.get("complete112_response_canonical_sha256"),
                        independent_full112_original_response_words_not_supplied=True,
                        discrepancy_is_not_a_new_acceptance_or_accuracy_gate=True)
            result = dict(schema=SCHEMA, complete=True, original_nine_columns_attempted=9,
                complete_three_by_nine_adjoint_response=response,
                complete112_by_nine_formed_local_forward_response=full,
                original_axes=[dict(column=i, result_canonical_sha256=b.digest(row))
                               for i, row in enumerate(columns)],
                existing_original_forward_comparison=comparison,
                original_parameters_unchanged=True, no_new_control_basis_or_rank_claim=True)
            self._emit("literal-adjoint-original-nine-result", result=result)
            return result
        except Exception as error:
            self._emit("literal-adjoint-original-nine-partial",
                completed_original_columns=len(columns), unvisited_original_columns=list(range(len(columns), 9)),
                completed_column_result_identities=[b.digest(row) for row in columns],
                exception=repr(error), complete_traceback=traceback.format_exc(),
                resource_partial=isinstance(error, AdjointBudgetStop))
            raise
