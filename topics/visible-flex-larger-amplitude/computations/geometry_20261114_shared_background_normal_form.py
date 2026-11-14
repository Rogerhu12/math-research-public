#!/usr/bin/env python3
"""Prepare an exact shared-node C2 background from one actual closed bundle.

The source background table remains untouched.  Its actual rendered scalar
0/1/2 jets define a NEW, explicit real quintic position function between
shared nodes.  This is a finite-field definition, not a claim that the old
independently evaluated height/w/wr table was already a C2 primitive.
The actual cap height and flat cuff jets are retained exactly.  Full cut
corrections must be formed anew against THIS background; their exact mean
component and all endpoint selection identities are retained below.

No tail or BVP is solved, no metric is changed, and no previous continuous
geometry envelope is inherited.  All actual numerical work is restricted
to this public repository's Actions.  Module-level polynomial helpers use
only the Python standard library and exact rational arithmetic.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction as Q
import gzip
import hashlib
import json
from math import comb, factorial
import os
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
SCHEMA = "actual-closed-shared-background-quintic-normal-form-v1"
LOADER_SHA = "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6"


def exact(value):
    if isinstance(value, Q):
        return value
    if isinstance(value, int):
        return Q(value)
    n, d = value.as_integer_ratio()
    return Q(int(n), int(d))


def qrecord(value):
    value = exact(value)
    return dict(numerator_hex=hex(value.numerator),
                denominator_hex=hex(value.denominator))


def qread(record):
    return Q(int(record["numerator_hex"], 16),
             int(record["denominator_hex"], 16))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, record):
    raw = (json.dumps(record, sort_keys=True, indent=2,
                     ensure_ascii=False, allow_nan=False)+"\n").encode()
    if len(raw) >= 1_000_000 and not str(path).endswith(".gz"):
        raise ValueError("A large exact descriptor requires an explicit gzip output")
    if str(path).endswith(".gz"):
        raw = gzip.compress(raw, mtime=0)
    if len(raw) >= 5_000_000:
        raise ValueError("The complete descriptor needs genuine chunking before publication")
    with Path(path).open("xb") as stream:
        stream.write(raw)


def hermite(left, right, width):
    """R245/R249 real shared-node quintic in u=(r-r_left)/width."""
    y0, v0, a0 = map(exact, left)
    y1, v1, a1 = map(exact, right)
    h = exact(width)
    if h <= 0:
        raise ValueError("Exact background nodes must increase strictly")
    c0, c1, c2 = y0, h*v0, h*h*a0/2
    A, B, C = y1-c0-c1-c2, h*v1-c1-2*c2, h*h*a1-2*c2
    return (c0, c1, c2, 10*A-4*B+C/2, -15*A+7*B-C, 6*A-3*B+C/2)


def differentiated(coefficients, width, derivative):
    if not 0 <= derivative <= 5:
        raise ValueError("A quintic has only six polynomial derivative orders")
    h = exact(width)
    return tuple(exact(coefficients[k])*Q(factorial(k),factorial(k-derivative))/h**derivative
                 for k in range(derivative, len(coefficients)))


def evaluate(coefficients, unit):
    value, u = Q(0), exact(unit)
    for coefficient in reversed(coefficients):
        value = value*u+exact(coefficient)
    return value


def bernstein(coefficients):
    """Exact power-to-Bernstein conversion, on the whole unit interval."""
    n = len(coefficients)-1
    return tuple(sum((exact(coefficients[k])*Q(comb(j,k),comb(n,k))
                      for k in range(j+1)), Q(0)) for j in range(n+1))


def polynomial_bounds(coefficients, width, derivative):
    control = bernstein(differentiated(coefficients, width, derivative))
    return dict(lower=qrecord(min(control)), upper=qrecord(max(control)),
                bernstein_coefficients=[qrecord(v) for v in control])


class SharedBackground:
    """Exact node/position API; no implicit float or continuous source claim."""
    def __init__(self, radii, nodal_jets):
        self.radii = tuple(map(exact, radii))
        self.nodal = tuple(tuple(map(exact, row)) for row in nodal_jets)
        if (len(self.radii) < 2 or len(self.radii) != len(self.nodal)
                or any(len(row) != 3 for row in self.nodal)
                or any(a >= b for a,b in zip(self.radii,self.radii[1:]))):
            raise ValueError("Retain all strictly increasing shared 0/1/2 background nodes")
        self.coefficients = tuple(hermite(self.nodal[i],self.nodal[i+1],b-a)
            for i,(a,b) in enumerate(zip(self.radii,self.radii[1:])))
        for i,c in enumerate(self.coefficients):
            width = self.radii[i+1]-self.radii[i]
            for order in range(3):
                derivative = differentiated(c,width,order)
                if (evaluate(derivative,Q(0)) != self.nodal[i][order]
                        or evaluate(derivative,Q(1)) != self.nodal[i+1][order]):
                    raise AssertionError("The exact shared-node Hermite endpoint identity failed")

    @classmethod
    def from_record(cls, record):
        if record.get("schema") != SCHEMA or not record.get("finished"):
            raise ValueError("Use a complete explicitly defined background descriptor")
        if canonical_sha(record["exact_background"]) != record["exact_background_payload_sha256"]:
            raise ValueError("The retained exact-background payload hash differs")
        nodes = record["exact_background"]["nodes"]
        obj = cls([qread(row["radius"]) for row in nodes],
                  [[qread(v) for v in row["jets"]] for row in nodes])
        expected = [[qrecord(v) for v in c] for c in obj.coefficients]
        actual = [row["power_coefficients"] for row in record["exact_background"]["cells"]]
        if expected != actual:
            raise ValueError("The retained real coefficients differ from the same shared nodes")
        return obj

    def evaluate_exact(self, radius, derivative=0):
        r = exact(radius)
        if derivative not in (0,1,2) or not self.radii[0] <= r <= self.radii[-1]:
            raise ValueError("Use only the represented background interval and 0/1/2 jets")
        at = min(bisect_right(self.radii,r)-1,len(self.radii)-2)
        h = self.radii[at+1]-self.radii[at]
        return evaluate(differentiated(self.coefficients[at],h,derivative),
                        (r-self.radii[at])/h)

    def encode(self):
        cells = []
        for i,c in enumerate(self.coefficients):
            h = self.radii[i+1]-self.radii[i]
            y0,v0,a0 = self.nodal[i]
            y1,v1,a1 = self.nodal[i+1]
            defect = y1-y0-h*(v0+v1)/2-h*h*(a0-a1)/12
            cells.append(dict(index=i, width=qrecord(h),
                power_coefficients=[qrecord(v) for v in c],
                continuous_jet_bounds=[polynomial_bounds(c,h,d) for d in range(3)],
                R245=dict(compatibility_defect=qrecord(defect),
                    C0_difference_from_left_anchored_integrated_cubic_velocity_bound=qrecord(abs(defect)),
                    C1_difference_bound=qrecord(Q(15,8)*abs(defect)/h),
                    C2_difference_bound_squared=qrecord(Q(100,3)*defect*defect/h**4),
                    cause_not_assigned_to_roundoff=True,
                    primitive_or_target_metric_error_bound=False)))
        return dict(nodes=[dict(index=i,radius=qrecord(r),jets=[qrecord(v) for v in jets])
                           for i,(r,jets) in enumerate(zip(self.radii,self.nodal))],
                    cells=cells, exact_endpoint_identities_checked=6*len(cells),
                    shared_global_C2_position_function=True,
                    angular_derivatives_of_scalar_background_identically_zero=True)


def prepare_from_bundle(paths, plan, assembly, background, saved, A, bindings):
    """Called only with one successful, source-checked load_full_bundle result."""
    import numpy as np

    rows = background["rows"]
    radii = [exact(row["r"]) for row in rows]
    expected = list(map(exact,plan["background_radii"]))
    if radii != expected or radii != sorted(set(radii)):
        raise ValueError("Retain this plan's entire ordered, distinct background query table")
    if (radii[0] != exact(A.cuff) or radii[-1] != exact(A.cut)
            or background["inputs"]["plan"]["sha256"] != sha(paths["plan"])
            or background["profile_fingerprint"] != plan["profile_fingerprint"]):
        raise ValueError("The complete source background anchors or plan identity differ")
    if exact(A.sigma) != -1:
        raise ValueError("This wrapper retains the actual reflected positive-radius construction")
    # Same separate scalar operations and NumPy arrays as RefinedAssembly.tail_jets.
    # Their OUTPUT values, at their actual dtype, become the selected exact jets.
    height,w,wr = (np.array([row[key] for row in rows])
                   for key in ("heightFromRToCut","w","wr"))
    output_jets = (A.offset-A.sigma*height,A.sigma*w,A.sigma*wr)
    if any(not np.all(np.isfinite(value)) for value in output_jets):
        raise ValueError("The actual background table contains a nonfinite scalar jet")
    nodal = [tuple(exact(value[i]) for value in output_jets) for i in range(len(rows))]
    if (nodal[0] != (exact(A.cap_height),Q(0),Q(0))
            or exact(rows[-1]["heightFromRToCut"]) != 0
            or nodal[-1][0] != exact(A.offset)):
        raise ValueError("The original cuff/cap or zero-height cut anchor is not exact as declared")
    result = SharedBackground(radii,nodal)
    encoded = result.encode()
    source_table = [dict(radius=qrecord(radii[i]),
        source_height_w_wr=[qrecord(exact(row[key])) for key in ("heightFromRToCut","w","wr")],
        source=row.get("source"),cell=row.get("cell"),segment=row.get("segment"),
        sourceX=qrecord(exact(row["sourceX"])) if "sourceX" in row else None,
        radialResidual=qrecord(exact(row["radialResidual"])),
        splitPrimitiveDifference=qrecord(exact(row["splitPrimitiveDifference"])))
        for i,row in enumerate(rows)]
    M = int(saved.M)
    if exact(saved.quintic.x[-1]) != exact(A.L):
        raise ValueError("The complete prefix cut must be its original shared terminal node")
    core = [exact(value) for value in saved.core]
    if len(core) != M:
        raise ValueError("Keep the complete core of this actual physical field")
    means = []
    for state in saved.quintic.nodal:
        z = [exact(value) for value in state[-1,2*M+1:]]
        if len(z) != M+1:
            raise ValueError("Keep the full physical height, including z0")
        means.append(z[0]+sum((Q(1-4*m*m,2)*core[m-1]*z[m]
                              for m in range(1,M+1)),Q(0)))
    v,b = exact(A.ap),exact(A.app)
    if v >= 0:
        raise ValueError("The closing radial chart orientation differs")
    target = (means[0],means[1]/v,means[2]/v**2-b*means[1]/v**3)
    fft = np.asarray(A.outer_coeff)
    if fft.shape != (3,A.tail.N//2+1,3) or not np.all(np.isfinite(fft)):
        raise ValueError("Retain all actual outer FFT node coefficients and jets")
    binary = np.asarray(fft,dtype="<c16",order="C")
    if not np.array_equal(binary.astype(np.clongdouble),fft):
        raise ValueError("The actual FFT data changed precision; do not create a binary64 shadow")
    fft_hash = hashlib.sha256(str(binary.shape).encode()+b"\0"+binary.tobytes()).hexdigest()
    zero_mode = tuple(exact(value[0,2].real) for value in fft)
    native = tuple(result.nodal[-1][j]+exact(A.sigma)*zero_mode[j] for j in range(3))
    mean_delta = tuple(target[j]-native[j] for j in range(3))
    if tuple(native[j]+mean_delta[j] for j in range(3)) != target:
        raise AssertionError("The exact complete material mean correction failed")
    # Distinguish the old cut_difference source (readout geometry) from the
    # actual tail_jets table.  A true new correction must use this new B.
    g = A.tail.rows[-1]["geometry"]
    old_wr = g["w"]*g["dlogwdx"]/g["drdx"]
    old_native_background = tuple(map(exact,(A.offset,A.sigma*g["w"],A.sigma*old_wr)))
    shift = tuple(result.nodal[-1][j]-old_native_background[j] for j in range(3))
    if exact(A.cap_height) <= 0:
        raise ValueError("The existing two fixed caps need their positive original height")
    return dict(schema=SCHEMA,finished=True,source_sha256=sha(__file__),
        complete_field_binding=bindings,
        exact_background=encoded,exact_background_payload_sha256=canonical_sha(encoded),
        selected_table_output_dtypes=[str(value.dtype) for value in output_jets],
        source_table=source_table,exact_scalar_encoding="actual scalar.as_integer_ratio(); no float conversion or decimal shadow",
        selected_source_table_012_node_difference=[qrecord(Q(0)) for _ in range(3)],
        old_background_source_is_not_a_continuous_table_interpolant=True,
        source_primitive_continuous_error_envelope_certified=False,
        source_radial_inverse_and_split_diagnostics_are_not_certificates=True,
        original_deep_omission_record=background.get("conditional_rotational_deep_omission"),
        cuff=dict(radius=qrecord(radii[0]),preserved_cap_height=qrecord(result.nodal[0][0]),
            slope=qrecord(Q(0)),second=qrecord(Q(0)),
            flat_contact_with_the_unchanged_fixed_cap_exact=True,
            all_original_markers_unchanged=True),
        complete_cut=dict(radius=qrecord(radii[-1]),
            original_physical_s012_material_means=[qrecord(x) for x in means],
            exact_source_chart_v_b=[qrecord(v),qrecord(b)],
            target_radial_material_means=[qrecord(x) for x in target],
            own_shared_background_jets=[qrecord(x) for x in result.nodal[-1]],
            complete_outer_FFT_node_dtype=str(fft.dtype),
            complete_outer_FFT_coefficients_sha256=fft_hash,
            original_FFT_zero_mode_jets=[qrecord(x) for x in zero_mode],
            new_native_total_material_means=[qrecord(x) for x in native],
            required_full_outer_correction_mean_jets=[qrecord(x) for x in mean_delta],
            source_old_cut_background_jets=[qrecord(x) for x in old_native_background],
            new_minus_old_cut_background_jets=[qrecord(x) for x in shift],
            full_correction_definition="Delta_i(theta) = exact complete registered prefix radial jet i - own exact circle/FFT/shared-background native jet i; retain all theta modes and use the R258 exact-width Hermite selectors",
            reusing_old_floating_delta_without_reforming_it_authorized=False,
            mean_component_alone_suffices_for_full_cut_matching=False,
            exact_full_cut_matching_follows_only_after_full_correction_is_installed=True),
        interpretation=dict(new_explicit_finite_background_field=True,
            literal_original_table_already_C2_claimed=False,
            target_metric_or_original_scalar_parameters_changed=False,
            new_tail_or_BVP_solve=False,
            previous_continuous_operator_curvature_reach_or_held_bounds_inherited=False,
            normal_form_metric_curvature_and_position_normal_envelopes_still_required=True,
            each_compared_field_must_bind_its_own_background_descriptor=True,
            target_metric_source_frozen_while_field_background_may_be_refined=True,
            R258_cardinal_differences_unchanged_if_only_this_background_and_its_mean_cut_correction_are_changed=True,
            descriptor_does_not_itself_render_or_accept_a_new_closed_surface=True),
        actual_delta_E_certified=False,task_completed=False)


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Execute the actual background preparation only in this public repository's Actions")
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("directory","checkpoint","port","config","tail-response","complete","source-topic","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--basename",default="surface")
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError("Keep original evidence; use a new descriptor output")
    if sha(HERE/"geometry_20261114_full_state_continuous_cover.py") != LOADER_SHA:
        raise ValueError("The complete bundle loader changed")
    from geometry_20261114_full_state_continuous_cover import load_full_bundle
    start = time.monotonic()
    bundle = load_full_bundle(a)
    report = prepare_from_bundle(*bundle)
    report["scientific_execution_repository"] = os.environ.get("GITHUB_REPOSITORY")
    report["scientific_execution_commit"] = os.environ.get("GITHUB_SHA")
    report["elapsed_seconds"] = time.monotonic()-start
    a.out.parent.mkdir(parents=True,exist_ok=True)
    write(a.out,report)
    print(json.dumps(dict(event="shared-background-defined",output=str(a.out),
        nodes=len(report["exact_background"]["nodes"]),
        exact_endpoint_identities=report["exact_background"]["exact_endpoint_identities_checked"],
        full_cut_correction_still_to_be_installed=True,actual_geometric_acceptance=False)),flush=True)


if __name__ == "__main__":
    main()
