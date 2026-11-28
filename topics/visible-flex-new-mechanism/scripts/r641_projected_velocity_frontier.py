"""Exact remaining R641 paths and the inward physical velocity model on the three-end graph."""
from types import SimpleNamespace
import time
import numpy as np
from r641_paid48_source_chart import Paid48Chart
from r641_center_implicit_length_faces import CompleteCone, PhysicalFaces, source
from r632_exact_pending_polynomial_frontier import FrontierBoxes
from r632_extremum_physical_faces import near_bound

LD = source.LD


class ExtendedFrontier(FrontierBoxes):
    @staticmethod
    def key(extended, alpha, length):
        # The 256 original coordinates are binary64; b, alpha and L are long double.
        return (np.asarray(extended[:-1], float).tobytes(), source.shapes.ld_text(extended[-1]),
                source.shapes.ld_text(alpha), source.shapes.ld_text(length))

    @FrontierBoxes.latest_record.setter
    def latest_record(self, value):
        self.latest = value

    def certify(self, graph, extended, alpha, length):
        if (tuple(extended[:-1]) == getattr(self,"pending_q",None)
                and self.key(extended,alpha,length) != self.pending_key):
            raise RuntimeError("The paid trial's b, alpha or L changed before use of its exact qualification")
        return super().certify(graph,extended,alpha,length)

    def close(self, graph, extended, alpha, length, record):
        # The common exact-cell engine expects an order-zero array at index 0.
        # All 257 columns of the actual projected representation are included.
        layout = SimpleNamespace(h_coeff=[graph.extended_h_coeff], k_coeff=[graph.extended_k_coeff],
            background_h_coeff=[graph.background_h_coeff], background_k_coeff=[graph.background_k_coeff],
            knots=graph.knots, clock=graph.clock)
        # Keep the original long-double basis for later unfinished fields also.
        layout.extended_h_coeff, layout.extended_k_coeff = graph.extended_h_coeff, graph.extended_k_coeff
        # PhysicalBoxes needs unwrapped offsets, unlike the exact-cell interface.
        # Complete each original named field separately so the two layouts never mix.
        missing = record.get("unevaluated_fields", [])
        partial = {**record, "unevaluated_fields": []}
        result = super().close(layout, extended, alpha, length, partial)
        if result["state"] != "all_four_represented_polynomial_fields_certified" or not missing:
            return result
        coefficients = self.ordinary.physical_coefficients(graph, extended, alpha, length)
        for index, name in enumerate(missing):
            field, _ = self.ordinary.certify_field(name, coefficients[name])
            result["fields"][name] = field
            if field["state"] == "pending":
                return self.close(graph, extended, alpha, length, {**result, "state":"pending",
                    "inflight_polynomial_field":field, "unevaluated_fields":missing[index+1:]})
            if field["state"] != "certified_represented_polynomial":
                result["state"] = field["state"]
                result["unevaluated_fields"] = missing[index+1:]
                return result
        return result


class TwoPaidRootsChart(Paid48Chart):
    def scalar_root(self, q):
        if np.array_equal(q, np.asarray(self.pending_root["shape_parameters"], dtype=LD)):
            self.latest_scalar_root = {**self.pending_root, "same_unexecuted_candidate_root_reused":True}
            self.latest_geometry["scalar_P_root"] = self.latest_scalar_root
            source.shapes.COUNTS["source_closed_scalar_root_reuses"] += 1
            return LD(self.pending_root["actual_control_LD_decimal"]), self.latest_scalar_root
        return super().scalar_root(q)


class VelocityFaces:
    def __init__(self, graph, curve, args):
        self.center_length = PhysicalFaces(curve, args.center_activity_distance, args.length_activity_distance)
        layout = SimpleNamespace(k_coeff=[graph.extended_k_coeff[:,:,:-1]], knots=graph.knots,
            background_h_coeff=[graph.background_h_coeff], background_k_coeff=[graph.background_k_coeff])
        # kappa's explicit b-column vanishes. The actual implicit b derivative
        # enters both physical alpha and length in the velocity chain.
        self.velocity = near_bound(layout, curve, "upsilon", args.velocity_activity_distance)
        self.normals = list(self.center_length.normals)
        if self.velocity is not None:
            self.normals.append({k:v for k,v in self.velocity.items() if k!="row"})

    def bases(self, end_row=None):
        for mask, tangent in self.center_length.bases(end_row):
            yield mask, tangent
            if self.velocity is not None:
                restricted = self.velocity["row"] @ tangent
                if np.any(restricted):
                    sub = source.complete_nullspace([restricted], tangent.shape[1])
                    yield mask+["upsilon"], tangent@sub

    def feasible(self, direction, active):
        feasible, signs = self.center_length.feasible(direction, active)
        if self.velocity is not None:
            row = self.velocity["row"]
            value = float(row@direction)
            tol = 32*len(direction)*np.finfo(float).eps*np.linalg.norm(row)*np.linalg.norm(direction)
            signs["upsilon"] = value
            acceptable = abs(value)<=tol if "upsilon" in active else value>=0.
            feasible = feasible and acceptable
        return bool(feasible), signs


class VelocityCone(CompleteCone):
    def __init__(self, current, graph, args, retained, iteration, enforce_ends):
        self.current, self.clock = current, graph.clock
        self.physical = VelocityFaces(graph, current["data"]["curve"], args)
        self.end_row = current["jacobian"][0] if enforce_ends else None
        self.factors = []
        self.record = retained["latest_original_physical_cone_model"] = {
            "state":"building","iteration":iteration,"normals":self.physical.normals,
            "actual_remaining_true_end_rows_enforced":int(enforce_ends),
            "all_256_input_columns":True,"faces":[],"damped_models":[]}
        started = time.monotonic()
        try:
            for active, tangent in self.physical.bases(self.end_row):
                record = {"active":active,"dimension":tangent.shape[1],"state":"pending"}
                self.record["faces"].append(record)
                self.clock.check("before_R641_true_velocity_face_factor")
                label = f"R641_velocity_{iteration}_" + "_".join(active)
                factor = source.EuclideanCompleteRowFactor(current["jacobian"]@tangent,
                    -current["residual"], self.clock, source.COUNTS, label)
                self.factors.append((active, tangent, factor))
                record.update(state="completed", factor_id=factor.receipt["factor_id"])
            self.record["state"] = "completed"
        finally:
            self.record["factor_seconds_including_partial"] = time.monotonic()-started

    def solve(self, penalty):
        d, rec = super().solve(penalty)
        velocity = self.physical.velocity
        if velocity is None or not np.any(d):
            return d, rec
        other = self.physical.center_length
        # Keep all other near-bound physical rows, and any qualified end row,
        # unchanged while adding an inward component.
        other_mask = [r["field"] for r in other.normals]
        tangent = next(B for mask,B in other.bases(self.end_row) if mask==other_mask)
        row = velocity["row"]
        inward = tangent@(tangent.T@row)
        pairing, initial = float(row@inward), float(row@d)
        baseline = rec["selected"]["model_decrease"]
        tests = rec["strict_velocity_trials"] = []
        if pairing<=0 or baseline<=0:
            return d,rec
        target = min(.01, .01*np.linalg.norm(d)*np.linalg.norm(inward))
        for shrink in (1., .1, .01, .001):
            desired = shrink*target
            if initial>=desired:
                break
            candidate = d + (desired-initial)/pairing*inward
            delta = self.current["jacobian"]@candidate
            gain = float(-self.current["residual"]@delta-(delta@delta+penalty*(candidate@candidate))/2)
            active = [a for a in rec["selected"]["face"] if a!="upsilon"]
            good, signs = self.physical.feasible(candidate, active)
            tests.append({"target":float(desired),"signs":signs,"gain":gain,"feasible":good})
            if good and signs["upsilon"]>0 and gain>=.99*baseline:
                rec["strict_velocity_selected"] = len(tests)-1
                return candidate, rec
        return d, rec
