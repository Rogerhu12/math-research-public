#!/usr/bin/env python3
"""Independent full39 query operator: retain complete38 and add RIGHT-RMS459.

The original generic RMS compiler receives the real right fraction and
same-call complete endpoint J/P at459/460. All22 LEFT and16 direct original
MID blocks retain their mathematical formulas and order; RIGHT459 is last.
The exact union is32 physical nodes, without a fictitious node461 zero B
column. Complete H still retains node461 and all other outside response.
No native/full-DN solve, scientific acceptance change or root proof occurs.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.interpolate import CubicHermiteSpline

import geometry_20261114_full_angle_domain_operator as frozen
import geometry_20261114_full_angle_domain_direction_probe as angular


HERE = Path(__file__).resolve().parent
SCHEMA = "captured-thirty-nine-query-original-RMS-and-collocation-midpoint-domain-v1"
FROZEN_OPERATOR_SHA = "af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7"
ORIGIN_THIRTY_SEVEN_OPERATOR_SHA = "2e189fbf48ddeb5bb2ffba60047ee544bc39b22c6fe5073a91dad6bb2a1074e3"
ORIGIN_THIRTY_SEVEN_OPERATOR_NAME = "geometry_20261115_thirty_seven_query_domain_operator.py"
ORIGIN_THIRTY_EIGHT_OPERATOR_NAME = "geometry_20261115_thirty_eight_query_domain_operator.py"
ORIGIN_THIRTY_EIGHT_OPERATOR_SHA = "f1684f4b23d1b50d97779ae79bb90554307a524c0a8932de6af824ca1fa98e17"
LEFT_INTERVALS = (462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 475, 477, 479, 480, 481, 482, 484, 485, 486, 487)
MID_INTERVALS = (471, 472, 473, 475, 477, 479, 480, 481, 482, 483, 484, 485, 486, 487, 489, 490)
LEFT_FRACTION = 0.17267316464601146
RIGHT_FRACTION = 0.8273268353539885
RIGHT_INTERVALS = (459,)
QUERY_SPECS = tuple(
    dict(kind="left-RMS", interval=j, fraction=LEFT_FRACTION)
    for j in LEFT_INTERVALS) + tuple(
    dict(kind="collocation-midpoint", interval=j, fraction=.5)
    for j in MID_INTERVALS) + tuple(
    dict(kind="right-RMS", interval=j, fraction=RIGHT_FRACTION)
    for j in RIGHT_INTERVALS)
QUERY_INTERVALS = tuple(row["interval"] for row in QUERY_SPECS)
CAPTURE_INTERVALS = tuple(sorted(set(QUERY_INTERVALS)))
ZERO_LAYOUT_NODES = ()
QUERY_ENDPOINT_NODES = tuple(sorted(set(CAPTURE_INTERVALS) |
    {j+1 for j in CAPTURE_INTERVALS}))
# Derive the complete layout from the actual typed query endpoint union.
# No previous local dimension or zero block is copied into this source.
LOCAL_LAYOUT_NODES = QUERY_ENDPOINT_NODES
ADDED_QUERY_SPECS = (dict(kind="right-RMS", interval=459, fraction=RIGHT_FRACTION),)


def source_identity(capture):
    if frozen.sha(Path(frozen.__file__)) != FROZEN_OPERATOR_SHA:
        raise ValueError("The original captured full-angle operator changed")
    origin = HERE/ORIGIN_THIRTY_SEVEN_OPERATOR_NAME
    if frozen.sha(origin) != ORIGIN_THIRTY_SEVEN_OPERATOR_SHA:
        raise ValueError("The frozen thirty-seven-query implementation origin changed")
    complete38 = HERE/ORIGIN_THIRTY_EIGHT_OPERATOR_NAME
    if frozen.sha(complete38) != ORIGIN_THIRTY_EIGHT_OPERATOR_SHA:
        raise ValueError("The complete original38 implementation origin changed")
    return {**capture.sources, ORIGIN_THIRTY_SEVEN_OPERATOR_NAME:ORIGIN_THIRTY_SEVEN_OPERATOR_SHA,
        ORIGIN_THIRTY_EIGHT_OPERATOR_NAME:ORIGIN_THIRTY_EIGHT_OPERATOR_SHA,
        Path(__file__).name:frozen.sha(__file__)}


def capture_queries(problem, state, intervals=QUERY_INTERVALS):
    """Deduplicate endpoint capture only; preserve every distinct query row."""
    if tuple(intervals) != QUERY_INTERVALS:
        raise ValueError("Use all22 left-RMS,16 original midpoints and the complete RIGHT459 query")
    return frozen.EndpointJacobianCapture(problem, state, intervals=CAPTURE_INTERVALS)


class _RMSCaptureView:
    """One typed RMS subset of the SAME complete original J/P capture.

    A view adds no Jacobian call and changes no captured endpoint words.
    The independent original RMS compiler receives its real left/right
    fraction; no RIGHT query is relabelled as a LEFT query.
    """
    def __init__(self, complete, intervals):
        self._complete = complete
        self.intervals = tuple(intervals)

    def __getattr__(self, name):
        return getattr(self._complete, name)


def query_value(problem, state, spec):
    """No whole flow/J call. A midpoint returns the original supplied row."""
    j = spec["interval"]
    if spec["kind"] == "collocation-midpoint":
        return float(problem.mid[j]), np.asarray(state["middle"][j])
    expected = {"left-RMS":LEFT_FRACTION, "right-RMS":RIGHT_FRACTION}.get(spec["kind"])
    if expected is None or spec["fraction"] != expected:
        raise ValueError("Unknown original query kind/fraction pair")
    station = float(problem.x[j]+spec["fraction"]*problem.h[j])
    values, rhs = np.asarray(state["y"])[j:j+2], np.asarray(state["f"])[j:j+2]
    if not np.all(np.isfinite(values)) or not np.all(np.isfinite(rhs)):
        return station, np.full(problem.flow.dimension, np.nan)
    return station, CubicHermiteSpline(problem.x[j:j+2], values, rhs, axis=0)(station)


def selected_actual_angles(problem, state):
    """Read every modeled query at the same actually evaluated real trial."""
    arrays, reports = [], []
    for group, spec in enumerate(QUERY_SPECS):
        station, query = query_value(problem, state, spec)
        finite = bool(np.all(np.isfinite(query)))
        if finite:
            with np.errstate(invalid="ignore", divide="ignore", over="ignore"):
                margin = angular.angular_values(problem.flow, station, query)["beta"]
        else:
            margin = np.full(problem.flow.q.N, np.nan)
        arrays.append(np.asarray(margin).tolist())
        reports.append(dict(query_index=group, **spec, station=station,
            original_query_input_finite=finite,
            original_query_source=("state.middle[j] and problem.mid[j]"
                if spec["kind"] == "collocation-midpoint" else
                "original CubicHermiteSpline at this original left/right RMS station"),
            original_query_array=frozen.array_identity(query),
            original_beta_squared=angular.angle_summary(margin, problem.flow.q.N),
            whole_flow_recomputed=False, Jacobian_recomputed=False))
    return arrays, reports


class ThirtyNineQueryDomainOperator(frozen.FullAngleDomainOperator):
    """The same sparse full-coordinate interface, now with thirty-nine typed blocks."""
    def __init__(self, problem, state, capture, fraction=LEFT_FRACTION, input_identity=None):
        frozen.require_actions()
        capture.assert_matches(problem, state)
        if tuple(capture.intervals) != CAPTURE_INTERVALS or float(fraction) != LEFT_FRACTION:
            raise ValueError("Preserve all26 actual captured cells and both original typed RMS rules")
        sources = source_identity(capture)
        started = time.monotonic()
        # Compile all twenty-two declared left-RMS rows from the same capture.
        # All sixteen retained original midpoints keep the original formula.
        left = frozen.FullAngleDomainOperator(problem, state,
            _RMSCaptureView(capture, LEFT_INTERVALS),
            fraction=LEFT_FRACTION, input_identity=input_identity)
        right_rms = frozen.FullAngleDomainOperator(problem, state,
            _RMSCaptureView(capture, RIGHT_INTERVALS),
            fraction=RIGHT_FRACTION, input_identity=input_identity)
        self.__dict__.update(left.__dict__)
        self.capture = capture
        self.node_indices = frozen.readonly(np.unique(np.r_[CAPTURE_INTERVALS,
            np.asarray(CAPTURE_INTERVALS)+1]))
        self.left_component_model_sha256 = left.model_sha256
        self.right_component_model_sha256 = right_rms.model_sha256
        self.right_unit_jet_sha256 = right_rms.unit_jet_sha256
        self.right_hermite_weights = right_rms.hermite_weights
        self.sources = sources
        self.intervals = QUERY_INTERVALS
        self.fraction = None
        self.rows = len(QUERY_SPECS)*self.N
        self.shape = (self.rows, self.chart.size)
        self.query_specs = tuple(dict(row) for row in QUERY_SPECS)
        self._queries = [dict(q, kind="left-RMS", fraction=LEFT_FRACTION,
            query_index=i) for i, q in enumerate(left._queries)]
        self.query_reports = [dict(row, kind="left-RMS", query_index=i,
            original_query_source="unchanged original left-RMS CubicHermiteSpline")
            for i, row in enumerate(left.query_reports)]
        self.factor_identities = [dict(row, kind="left-RMS", query_index=i)
            for i, row in enumerate(left.factor_identities)]
        blocks = [dict(block, kind="left-RMS", fraction=LEFT_FRACTION,
            station=left._queries[i]["station"], query_index=i)
            for i, block in enumerate(left.local_blocks)]
        original_middle = frozen.real64(state["middle"],
            (self.chart.m-1, self.flow.dimension), "original returned middle states")
        original_mid = frozen.real64(problem.mid, (self.chart.m-1,), "original midpoint stations")
        self._original_midpoint_values = frozen.readonly(original_middle[list(MID_INTERVALS)])
        self._original_midpoint_stations = frozen.readonly(original_mid[list(MID_INTERVALS)])
        self.midpoint_base_identity = dict(
            whole_original_middle=frozen.array_identity(original_middle),
            whole_original_mid=frozen.array_identity(original_mid),
            selected_original_middle=frozen.array_identity(self._original_midpoint_values),
            selected_original_mid=frozen.array_identity(self._original_midpoint_stations))
        gd, ge, direct, beta = [], [], [], []
        for i, j in enumerate(MID_INTERVALS):
            group = len(LEFT_INTERVALS)+i
            h, station = float(problem.h[j]), float(original_mid[j])
            query = original_middle[j]
            values = angular.angular_values(self.flow, station, query)
            d, e, Q, v, W = (values[name] for name in ("first", "second", "Q", "cross", "W"))
            a, nu = values["scalar"][:2]
            arrays = (query, d, e, Q, v, W, values["beta"], values["scalar"])
            if (not all(np.all(np.isfinite(value)) for value in arrays)
                    or a <= 0 or np.any(Q <= 0) or np.any(W <= 0)
                    or np.any(values["beta"] <= 0)):
                raise FloatingPointError("Every added original midpoint angle needs a positive finite base margin")
            factor = nu*nu/(a*a)
            gd.append((-6*factor*Q**2/W)[:, None]*d
                +(2*factor*Q**3/W**2)[:, None]*np.cross(e, v))
            ge.append((2*factor*Q**3/W**2)[:, None]*np.cross(v, d))
            ga, gnu = 2*nu*nu*Q**3/(a**3*W), -2*nu*Q**3/(a*a*W)
            controls = frozen.real64(np.asarray(self.flow.profile.control_jets(station)),
                (3, self.k), "complete original midpoint scalar control jets")
            direct.append(ga[:, None]*controls[0]+gnu[:, None]*controls[1])
            beta.append(values["beta"])
            algebraic = .5*(self._y[j]+self._y[j+1])-h*(self._f[j+1]-self._f[j])/8
            self._queries.append(dict(query_index=group, kind="collocation-midpoint",
                interval=j, fraction=.5, h=h, station=station, value=frozen.readonly(query)))
            self.query_reports.append(dict(query_index=group, kind="collocation-midpoint",
                interval=j, fraction=.5, station=station,
                left=float(self._mesh[j]), right=float(self._mesh[j+1]),
                phi_grid="2*pi*arange(N)/N", N=self.N, a=float(a), returned_ap=float(nu),
                beta_squared_min=float(np.min(values["beta"])),
                beta_squared_min_angle_index=int(np.argmin(values["beta"])),
                original_normal_vs_cross_formula_max=frozen._maximum(values["beta"]-values["cross_beta"]),
                original_query_source="direct state.middle[j] and problem.mid[j]",
                original_midpoint_query=frozen.array_identity(query),
                original_midpoint_formula_reconstruction_max=frozen._maximum(query-algebraic),
                original_midpoint_station=float(original_mid[j]),
                original_scalar_control_jets=frozen.array_identity(controls),
                midpoint_replaced_by_RMS_or_spline=False))
        gd, ge, direct = np.stack(gd), np.stack(ge), np.stack(direct)
        gamma = np.empty((len(MID_INTERVALS), self.N, self.n), dtype=np.float64)
        unit, digest = np.zeros(self.n), hashlib.sha256()
        for column in range(self.n):
            unit[column] = 1.
            _, dcol, ecol = self.flow.q.jet(unit)
            frozen.real64(dcol, (self.N, 3), "original midpoint unit first jet")
            frozen.real64(ecol, (self.N, 3), "original midpoint unit second jet")
            digest.update(int(column).to_bytes(8, "little"))
            digest.update(dcol.tobytes(order="C")); digest.update(ecol.tobytes(order="C"))
            gamma[:, :, column] = (np.einsum("anc,nc->an", gd, dcol)
                +np.einsum("anc,nc->an", ge, ecol))
            unit[column] = 0.
        if not np.all(np.isfinite(gamma)) or not np.all(np.isfinite(direct)):
            raise FloatingPointError("The complete added midpoint Gamma/Pi are nonfinite")
        self.midpoint_unit_jet_sha256 = digest.hexdigest()
        gamma.setflags(write=False); direct.setflags(write=False)
        self._factor_cache = left._factor_cache + tuple(dict(Gamma=gamma[i], Pi=direct[i])
            for i in range(len(MID_INTERVALS)))
        pstart = self.chart.physical_size+self.chart.free
        pcols = np.arange(pstart, self.chart.size, dtype=np.int64)
        for i, j in enumerate(MID_INTERVALS):
            group, g, h = len(LEFT_INTERVALS)+i, gamma[i], float(problem.h[j])
            endpoint = capture.records[j]
            JL, JR = endpoint["left"]["physical"], endpoint["right"]["physical"]
            PL, PR = endpoint["left"]["parameter"], endpoint["right"]["parameter"]
            # Derivative of the ORIGINAL middle construction, with every
            # nodal RHS chain and the direct query scalar term retained.
            lblock = .5*g+(h/8)*(g@JL)
            rblock = .5*g-(h/8)*(g@JR)
            pblock = (h/8)*((g@PL)-(g@PR))+direct[i]
            if j:
                lcols = np.arange((j-1)*self.n, j*self.n, dtype=np.int64)
                left_kind = "physical-node"
            else:
                lcols = np.arange(self.chart.physical_size, pstart, dtype=np.int64)
                lblock = lblock@self.chart.inlet
                left_kind = "exact-free-inlet-core"
            rcols = np.arange(j*self.n, (j+1)*self.n, dtype=np.int64)
            cols = np.concatenate((lcols, rcols, pcols))
            if len(set(cols.tolist())) != len(cols):
                raise ValueError("An original midpoint block must not duplicate a global column")
            row = np.concatenate((lblock, rblock, pblock), axis=1)/self._scale[cols][None, :]
            row = frozen.readonly(frozen.real64(row, name="complete original midpoint rows"))
            self.factor_identities.append(dict(query_index=group, kind="collocation-midpoint",
                interval=j, Gamma=frozen.array_identity(g), Pi=frozen.array_identity(direct[i])))
            nl = len(lcols)
            blocks.append(dict(query_index=group, kind="collocation-midpoint", interval=j,
                fraction=.5, station=float(problem.mid[j]), rows=row,
                B_left=row[:, :nl], B_right=row[:, nl:nl+self.n], B_p=row[:, nl+self.n:],
                global_columns=frozen.readonly(cols), row_slice=slice(group*self.N, (group+1)*self.N),
                left_kind=left_kind, left_column_count=nl,
                Gamma_identity=self.factor_identities[group]["Gamma"],
                Pi_identity=self.factor_identities[group]["Pi"]))
        # Append the complete independent original RIGHT-RMS block AFTER all38
        # retained blocks. Every local row, J/P chain and direct scalar term
        # is compiled by the unchanged generic original RMS operator.
        right_offset = len(LEFT_INTERVALS)+len(MID_INTERVALS)
        self._queries.extend(dict(q, kind="right-RMS", fraction=RIGHT_FRACTION,
            query_index=right_offset+i) for i, q in enumerate(right_rms._queries))
        self.query_reports.extend(dict(row, kind="right-RMS", query_index=right_offset+i,
            original_query_source="unchanged original RIGHT-RMS CubicHermiteSpline")
            for i, row in enumerate(right_rms.query_reports))
        self.factor_identities.extend(dict(row, kind="right-RMS", query_index=right_offset+i)
            for i, row in enumerate(right_rms.factor_identities))
        for i, block in enumerate(right_rms.local_blocks):
            group = right_offset+i
            blocks.append(dict(block, query_index=group, kind="right-RMS",
                fraction=RIGHT_FRACTION, station=right_rms._queries[i]["station"],
                row_slice=slice(group*self.N, (group+1)*self.N)))
        self._factor_cache += right_rms._factor_cache
        self.beta_squared = frozen.readonly(np.concatenate(
            (left.beta_squared, *beta, right_rms.beta_squared)))
        # Every declared local column now belongs to an actual query block.
        # The retained left-RMS484 already supplies the actual node484 columns;
        # the complete H still retains all of its original couplings.
        self.block_column_union_indices = frozen.readonly(np.unique(np.concatenate(
            [block["global_columns"] for block in blocks])))
        physical_layout = np.concatenate([np.arange((j-1)*self.n, j*self.n,
            dtype=np.int64) for j in LOCAL_LAYOUT_NODES])
        self.local_indices = frozen.readonly(np.concatenate((physical_layout, pcols)))
        self.zero_layout_indices = frozen.readonly(np.empty(0, dtype=np.int64))
        if not np.array_equal(self.local_indices, self.block_column_union_indices):
            raise ValueError("All declared local columns must belong to the actual thirty-nine-query blocks")
        for block in blocks:
            block["local_columns"] = frozen.readonly(np.searchsorted(self.local_indices, block["global_columns"]))
        self.local_blocks, self.local_shape = tuple(blocks), (self.rows, len(self.local_indices))
        self.block_identities = [dict(query_index=b["query_index"], kind=b["kind"], interval=b["interval"],
            fraction=b["fraction"], station=b["station"], rows=frozen.array_identity(b["rows"]),
            global_columns=frozen.array_identity(b["global_columns"]),
            local_columns=frozen.array_identity(b["local_columns"])) for b in blocks]
        self.build_seconds = time.monotonic()-started
        model = dict(schema=SCHEMA, sources=self.sources, base=self.base_identity,
            query_specs=self.query_specs, query_reports=self.query_reports,
            complete_local_indices=frozen.array_identity(self.local_indices),
            block_column_union=frozen.array_identity(self.block_column_union_indices),
            zero_layout_columns=frozen.array_identity(self.zero_layout_indices),
            local_layout_nodes=LOCAL_LAYOUT_NODES, zero_layout_nodes=ZERO_LAYOUT_NODES,
            original_midpoint_base=self.midpoint_base_identity, N=self.N,
            beta_squared=frozen.array_identity(self.beta_squared), blocks=self.block_identities,
            current_left_component_model_sha256=self.left_component_model_sha256,
            current_right_component_model_sha256=self.right_component_model_sha256,
            original_right_unit_jet_sha256=self.right_unit_jet_sha256,
            original_right_hermite_weights=self.right_hermite_weights,
            original_unit_jet_sha256=self.unit_jet_sha256,
            midpoint_unit_jet_sha256=self.midpoint_unit_jet_sha256)
        self.model_sha256 = hashlib.sha256(json.dumps(model, sort_keys=True,
            separators=(",", ":"), allow_nan=False).encode()).hexdigest()

    def description(self):
        report = super().description()
        report.update(schema=SCHEMA, source_sha256=self.sources,
            implementation_origin_source_sha256=ORIGIN_THIRTY_EIGHT_OPERATOR_SHA,
            configured_in_independent_source_not_mutated_parent_module=True,
            fraction=None, query_specs=[dict(row) for row in self.query_specs],
            intervals=list(QUERY_INTERVALS), capture_intervals=list(CAPTURE_INTERVALS),
            left_RMS_fraction=LEFT_FRACTION, right_RMS_fraction=RIGHT_FRACTION,
            original_collocation_midpoint_fraction=.5,
            row_order="all22 original left-RMS then16 original midpoints then RIGHT-RMS459; each full physical phi index0..N-1",
            query_kind_and_fraction_are_per_block=True,
            added_original_queries=[dict(row) for row in ADDED_QUERY_SPECS],
            original_left_RMS487_retained=True,
            original_left_RMS464_retained=True,
            original_left_RMS486_retained=True,
            original_midpoint486_retained=True,
            original_midpoint471_retained=True,
            original_midpoint483_retained=True,
            original_midpoint472_retained=True,
            original_midpoint489_retained=True,
            original_midpoint490_retained=True,
            query_extension_reference="complete frozen38 query set; actual98 is the independent first parent",
            original_left_RMS462_retained=True,
            original_right_RMS459_explicitly_added=True,
            original_left_RMS463_retained=True,
            original_left_RMS471_separately_retained=True,
            original_midpoint487_retained=True,
            original_midpoint479_retained=True,
            original_left_RMS479_separately_retained=True,
            original_midpoint480_retained=True,
            original_midpoint485_retained=True,
            original_left_RMS466_retained=True,
            original_left_RMS484_retained=True,
            original_midpoint484_retained=True,
            original_left_RMS485_retained=True,
            original_left_RMS465_retained=True,
            original_midpoint487_uses_direct_state_middle_and_problem_mid=True,
            original_left_RMS487_uses_original_CubicHermiteSpline=True,
            original_left_RMS480_separately_retained=True,
            original_left_RMS467_retained=True,
            original_left_RMS468_retained=True,
            original_left_RMS469_retained=True,
            original_midpoint481_retained=True,
            original_left_RMS481_separately_retained=True,
            original_left_RMS482_separately_retained=True,
            original_midpoint482_separately_retained=True,
            complete_capture_support_unchanged_from_parent=False,
            capture_interval_set_expanded=True,
            capture_endpoint_union_unchanged_from_original38=False,
            complete_capture_adds_new_endpoint=True,
            added_original_capture_endpoints=[459,460],
            added_original_capture_intervals=[459],
            added_capture_intervals=[459],
            actual_query_endpoint_nodes=list(QUERY_ENDPOINT_NODES),
            actual_query_endpoint_count=len(QUERY_ENDPOINT_NODES),
            declared_exact_local_nodes=list(LOCAL_LAYOUT_NODES),
            declared_local_layout_is_contiguous=False,
            node461_remains_in_complete_H_outside_response=True,
            declared_exact_local_dimension=len(self.local_indices),
            actual_block_column_union=frozen.array_identity(self.block_column_union_indices),
            actual_block_column_union_dimension=len(self.block_column_union_indices),
            zero_layout_nodes=list(ZERO_LAYOUT_NODES),
            zero_layout_columns=frozen.array_identity(self.zero_layout_indices),
            declared_local_layout_equals_actual_B_column_union=True,
            original_node484_actual_B_columns_retained=True,
            complete_capture_includes_original_endpoint484=True,
            complete_original_A_still_contains_all_nodes=True,
            complete_capture_includes_original_endpoint466=True,
            complete_capture_includes_original_endpoint467=True,
            retained_midpoint480_reuses_captured_endpoint480_and481=True,
            retained_midpoint485_uses_original_endpoint485_and486=True,
            retained_left_RMS466_uses_original_endpoint466_and467=True,
            retained_left_RMS484_uses_original_endpoint484_and485=True,
            retained_midpoint484_reuses_captured_endpoint484_and485=True,
            retained_left_RMS485_reuses_captured_endpoint485_and486=True,
            retained_left_RMS465_uses_captured_endpoint465_and466=True,
            retained_midpoint479_reuses_captured_endpoint479_and480=True,
            retained_left_RMS487_uses_captured_endpoint487_and488=True,
            retained_left_RMS464_uses_captured_endpoint464_and465=True,
            retained_left_RMS486_uses_captured_endpoint486_and487=True,
            retained_midpoint486_uses_same_captured_endpoint486_and487=True,
            retained_midpoint471_reuses_captured_endpoint471_and472=True,
            retained_midpoint483_uses_captured_endpoint483_and484=True,
            retained_midpoint472_reuses_captured_endpoint472_and473=True,
            retained_midpoint489_uses_captured_endpoint489_and490=True,
            retained_midpoint490_uses_captured_endpoint490_and491=True,
            original_midpoint489_and490_use_direct_state_middle_and_problem_mid=True,
            retained_left_RMS462_uses_captured_endpoint462_and463=True,
            added_right_RMS459_uses_captured_endpoint459_and460=True,
            retained_left_RMS463_uses_captured_endpoint463_and464=True,
            original_midpoint483_uses_direct_state_middle_and_problem_mid=True,
            original_midpoint471_uses_direct_state_middle_and_problem_mid=True,
            original_midpoint486_uses_direct_state_middle_and_problem_mid=True,
            retained_midpoint487_uses_same_captured_endpoint487_and488=True,
            complete_B_capture_support_unchanged_from_parent=False,
            complete_B_endpoint_and_local_support_unchanged_from_original38=False,
            complete_B_capture_includes_original_endpoint465=True,
            complete_capture_includes_original_endpoint468=True,
            complete_capture_includes_original_endpoint469=True,
            retained_midpoint481_reuses_captured_endpoint481_and482=True,
            complete_capture_includes_original_endpoint483=True,
            left_component_uses_read_only_interval_view_of_same_capture=True,
            right_component_uses_read_only_interval_view_of_same_capture=True,
            current_right_component_model_sha256=self.right_component_model_sha256,
            right_original_unit_jet_sha256=self.right_unit_jet_sha256,
            right_and_left_original_unit_jet_bytes_equal=(self.right_unit_jet_sha256==self.unit_jet_sha256),
            original_right_hermite_weights=self.right_hermite_weights,
            full_B_correction_support_not_restricted_by_C_baseline=True,
            original_midpoint_base_identity=self.midpoint_base_identity,
            original_midpoint_queries_use_state_middle_and_problem_mid=True,
            midpoint_linear_chain=".5*(dyL+dyR)-h*(dfR-dfL)/8, including all nodal J/P and direct scalar controls",
            midpoint_replaced_by_RMS_or_spline=False,
            current_left_component_model_sha256=self.left_component_model_sha256,
            midpoint_original_unit_jet_sha256=self.midpoint_unit_jet_sha256,
            added_midpoint_and_original_left_unit_jet_bytes_equal=(self.midpoint_unit_jet_sha256==self.unit_jet_sha256),
            all_current_midpoint_endpoint_pairs_from_same_original_capture=True,
            second_complete_Jacobian_constructed=False,
            original_scientific_domain_and_acceptance_gates_replaced=False)
        return report

    def verify(self, state, direction=None):
        """Original implementation thresholds, with the actual typed query chain."""
        frozen.require_actions()
        self.capture.assert_matches(self.problem, state)
        if (not frozen.bits_equal(np.asarray(state["middle"])[list(MID_INTERVALS)], self._original_midpoint_values)
                or not frozen.bits_equal(np.asarray(self.problem.mid)[list(MID_INTERVALS)], self._original_midpoint_stations)):
            raise ValueError("The original captured midpoint inputs changed")
        rng, reports = np.random.default_rng(26520261114), []
        for kind in ("all-coordinates", "shared-endpoints-and-controls", "controls-and-zero-support-core"):
            z = rng.standard_normal(self.chart.size)
            if kind == "shared-endpoints-and-controls":
                masked = np.zeros_like(z); masked[self.local_indices] = z[self.local_indices]; z = masked
            elif kind == "controls-and-zero-support-core":
                z[:self.chart.physical_size] = 0
            w = rng.standard_normal(self.rows)
            Bz, BTw = self.matvec(z), self.rmatvec(w)
            a, b = float(Bz@w), float(z@BTw)
            denominator = max(1., float(np.linalg.norm(Bz)*np.linalg.norm(w)),
                float(np.linalg.norm(z)*np.linalg.norm(BTw)))
            local, lt = self.local_matvec(z[self.local_indices]), self.local_rmatvec(w)
            outside = np.ones(self.chart.size, dtype=bool); outside[self.local_indices] = False
            reports.append(dict(kind=kind, forward_dual=a, transpose_dual=b,
                normwise_adjoint_error=abs(a-b)/denominator,
                local_forward_relative_error=frozen._maximum(local-Bz)/max(1., frozen._maximum(Bz)),
                local_transpose_relative_error=frozen._maximum(lt-BTw[self.local_indices])/max(1., frozen._maximum(BTw)),
                transpose_outside_declared_support_max=frozen._maximum(BTw[outside])))
        directions = []
        if direction is not None:
            directions.append(("actual-supplied-scaled-direction", np.array(
                self._vector(direction, self.chart.size, "actual scaled direction"), copy=True)))
        seeded = np.zeros(self.chart.size)
        seeded[self.local_indices] = rng.standard_normal(len(self.local_indices))
        seeded[self.chart.physical_size:self.chart.physical_size+self.chart.free] = rng.standard_normal(self.chart.free)
        directions.append(("seeded-local-physical-core-and-controls", seeded))
        complex_reports = []
        for kind, scaled in directions:
            lifted = self.chart.lift_direction(scaled/self._scale)
            step, chosen = 1e-25, self.node_indices
            augmented = self._y[chosen].astype(complex)+1j*step*lifted[chosen]
            actual_rhs = self.flow(self._mesh[chosen], augmented.T).T
            if not np.all(np.isfinite(actual_rhs)):
                complex_reports.append(dict(kind=kind, finite=False,
                    reason="Original complete endpoint complex RHS is nonfinite"))
                continue
            direct, real_query_differences = [], []
            for query in self._queries:
                j = query["interval"]
                positions = np.searchsorted(chosen, [j, j+1])
                if query["kind"] == "collocation-midpoint":
                    L, R = positions
                    actual_query = .5*(augmented[L]+augmented[R])-query["h"]*(actual_rhs[R]-actual_rhs[L])/8
                else:
                    actual_query = CubicHermiteSpline(self._mesh[j:j+2],
                        augmented[positions], actual_rhs[positions], axis=0)(query["station"])
                values = angular.angular_values(self.flow, query["station"], actual_query)["beta"]
                direct.append(np.imag(values)/step)
                real_query_differences.append(dict(query_index=query["query_index"],
                    kind=query["kind"], interval=j,
                    complex_real_part_vs_saved_original_query_max=frozen._maximum(np.real(actual_query)-query["value"])))
            direct = np.concatenate(direct); predicted = self.matvec(scaled)
            finite = bool(np.all(np.isfinite(direct)) and np.all(np.isfinite(predicted)))
            difference = direct-predicted
            absolute = frozen._maximum(difference) if finite else None
            denominator = max(1., frozen._maximum(direct), frozen._maximum(predicted)) if finite else None
            worst = int(np.argmax(abs(difference))) if finite else None
            group = worst//self.N if finite else None
            per_query = []
            if finite:
                for i, spec in enumerate(QUERY_SPECS):
                    sl = slice(i*self.N, (i+1)*self.N)
                    den = max(1., frozen._maximum(direct[sl]), frozen._maximum(predicted[sl]))
                    per_query.append(dict(query_index=i, **spec,
                        maximum_absolute_error=frozen._maximum(difference[sl]),
                        maximum_relative_error=frozen._maximum(difference[sl])/den))
            complex_reports.append(dict(kind=kind, finite=finite,
                scaled_direction=frozen.array_identity(scaled),
                original_complex_derivative=frozen.array_identity(direct),
                compiled_derivative=frozen.array_identity(predicted),
                maximum_absolute_error=absolute,
                maximum_relative_error=absolute/denominator if finite else None,
                worst_row=worst, worst_query_index=group,
                worst_query_kind=QUERY_SPECS[group]["kind"] if finite else None,
                worst_interval=QUERY_SPECS[group]["interval"] if finite else None,
                worst_angle_index=worst%self.N if finite else None,
                query_errors=per_query, actual_query_real_part_diagnostics=real_query_differences,
                full_augmented_original_RHS_used=True, unique_endpoint_count=len(chosen),
                midpoint_chain_is_original_collocation_formula=True,
                complex_chart_expand_not_used=True))
        adj = max(row["normwise_adjoint_error"] for row in reports)
        local = max(max(row["local_forward_relative_error"], row["local_transpose_relative_error"],
            row["transpose_outside_declared_support_max"]) for row in reports)
        finite = all(row["finite"] for row in complex_reports)
        error = max(row["maximum_relative_error"] for row in complex_reports) if finite else None
        return dict(schema=SCHEMA, model_sha256=self.model_sha256,
            query_specs=[dict(row) for row in QUERY_SPECS],
            adjoint_and_local_checks=reports, original_complex_chain_checks=complex_reports,
            maximum_normwise_adjoint_error=adj, maximum_local_full_action_error=local,
            maximum_original_complex_chain_relative_error=error,
            implementation_thresholds=dict(adjoint_and_local=5e-12, original_complex_chain=5e-5),
            implementation_check_passed=bool(adj<=5e-12 and local<=5e-12 and finite and error<=5e-5),
            actual_supplied_direction_checked=direction is not None,
            second_complete_Jacobian_constructed=False, native_tail_called=False,
            new_scientific_acceptance_gate=False,
            scope="all22 LEFT,16 MID and original RIGHT459; each complete2048 finite phi grid")

    def export(self, directory, row_chunk=256):
        """All thirty-nine kinds, original midpoint inputs and original fixed factors."""
        frozen.require_actions()
        directory = Path(directory); directory.mkdir(parents=True, exist_ok=True)
        if self._factor_cache is None:
            raise RuntimeError("The fixed original factors were already exported")
        row_chunk = int(row_chunk)
        if not 1 <= row_chunk <= 256:
            raise ValueError("Use at most256 raw angular rows per artifact part")
        files = []
        def save(name, metadata=None, **arrays):
            path = directory/name
            if path.exists():
                raise FileExistsError("Do not overwrite actual fixed-model bytes: "+str(path))
            np.savez_compressed(path, **arrays)
            files.append(dict(path=name, sha256=frozen.sha(path), bytes=path.stat().st_size,
                query=metadata, arrays={k:frozen.array_identity(v) for k,v in arrays.items()}))
        save("base-and-local-layout.npz", mesh=self._mesh, y=self._y, rhs=self._f,
            coordinate_scale=self._scale, local_indices=self.local_indices,
            beta_squared=self.beta_squared, node_indices=self.node_indices)
        save("original-collocation-midpoint-inputs.npz",
            metadata=dict(kind="collocation-midpoint", intervals=list(MID_INTERVALS), fraction=.5),
            intervals=np.asarray(MID_INTERVALS, dtype=np.int64),
            original_middle=self._original_midpoint_values,
            original_mid=self._original_midpoint_stations)
        for i, block in enumerate(self.local_blocks):
            metadata = dict(query_index=i, kind=block["kind"], interval=block["interval"],
                fraction=block["fraction"], station=block["station"])
            for lo in range(0, self.N, row_chunk):
                hi = min(self.N, lo+row_chunk)
                save(f"query-{i:02d}-{block['kind']}-interval-{block['interval']:05d}-rows-{lo:05d}-{hi:05d}.npz",
                    metadata=metadata, rows=block["rows"][lo:hi],
                    global_columns=block["global_columns"], local_columns=block["local_columns"],
                    Gamma=self._factor_cache[i]["Gamma"][lo:hi], Pi=self._factor_cache[i]["Pi"][lo:hi],
                    beta_squared=self.beta_squared[block["row_slice"]][lo:hi],
                    angle_indices=np.arange(lo, hi, dtype=np.int64))
        for i, entry in enumerate(self.capture.pool.values()):
            save(f"endpoint-{entry['node']:05d}-variant-{i:02d}.npz",
                physical_J=entry["physical"], parameter_P=entry["parameter"])
        manifest = self.description(); manifest["files"] = files
        manifest["artifact_scope"] = "all thirty-nine typed finite B/Gamma/Pi grids, original middle/mid bytes and original A endpoint factors"
        path = directory/"manifest.json"
        if path.exists():
            raise FileExistsError("Do not overwrite the actual mixed-query manifest")
        path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False, allow_nan=False)+"\n")
        self._factor_cache = None
        return dict(directory=str(directory), manifest=str(path), manifest_sha256=frozen.sha(path),
            model_sha256=self.model_sha256, file_count=len(files)+1,
            total_file_bytes=sum(row["bytes"] for row in files)+path.stat().st_size,
            query_specs=[dict(row) for row in QUERY_SPECS])
