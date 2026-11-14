#!/usr/bin/env python3
"""Stream two separate high-frequency material kernels from saved true panels.

This computes no source values, quadrature, ODE, or new fundamental matrix.
It preserves the original q continuous strip, then optionally applies the
already defined cellwise strong V scaling.  The 2/279 coefficient is used
ONLY for DQ(L_low) acting on a low input and producing the near band.
Complete mean/inverse remainder and Q(new variation) are not removed.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import digest, read, iter_array, metadata_without_array


FAMILIES = ("d1", "d_lambda", "low_to_near_quadratic")
STRIP_DEFINITION = "tau(r)=tau_inner-(tau_inner-tau_outer)*integral_inner^r btau/integral_cell btau"


def exact_endpoint(item):
    m, e = int(item["mantissa"]), int(item["binary_exponent"])
    return Fraction(m << e, 1) if e >= 0 else Fraction(m, 1 << (-e))


def exact_chosen(item):
    if item["lower"] != item["upper"]:
        raise ValueError("A chosen envelope or endpoint must be an exact dyadic")
    return exact_endpoint(item["lower"])


def same_interval(a, b):
    return a["lower"] == b["lower"] and a["upper"] == b["upper"]


class Monitor:
    def __init__(self, path, limit):
        self.path, self.limit = path, limit * 1024
        self.began = time.monotonic()
        self.events = 0

    def record(self, event, **fields):
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        row = dict(event=event, seconds=time.monotonic()-self.began,
                   peak_RSS_KiB=rss, **fields)
        with self.path.open("a") as f:
            f.write(json.dumps(row, separators=(",", ":"))+"\n")
        self.events += 1
        if rss > self.limit:
            raise MemoryError("This stream job exceeded its explicit RSS limit")
        return row


def run_band(args, band, density, panels, panel_meta, sigma, monitor):
    """Upper bounds for each output cell, with source in one fixed cell."""
    lo, hi = band
    rr = {r["cell"]: r for r in density["rows"]}
    states = {name: arb(0) for name in FAMILIES}
    out, previous_B = [], None
    source = args.source_cell
    for n in range(source, args.target_first-1, -1):
        r, meta = rr[n], panel_meta[n]
        B = ball(r["B"])
        k = ball(meta["k"])
        if not B >= 120 or not k > 0:
            raise ValueError("The stated two-material coefficient gate failed")
        if previous_B is not None:
            interface = max(arb(1), (B/previous_B).upper())
            for name in FAMILIES:
                states[name] = (interface*states[name]).upper()
            oldtau = exact_chosen(rr[n+1]["tau_outer"])
            newtau = exact_chosen(r["tau_inner"])
            if newtau > oldtau:
                raise ValueError("The original outward strip interface increases")
            # A possible downward strip jump only helps; do not charge it twice.
        q = max(arb(0), (1-arb(lo)/B).upper())
        maximum = {name: arb(0) for name in FAMILIES}
        witnesses = {name: None for name in FAMILIES}
        count, last_segment, last_x = 0, 0, Fraction(0)
        for i, g in enumerate(iter_array(panels[n], "panels")):
            segment = int(g["segment"])
            left, right = map(lambda z: Fraction(*z), (g["x_left"], g["x_right"]))
            if segment == last_segment:
                if left != last_x:
                    raise ValueError("A true source panel gap or overlap was found")
            elif segment == last_segment+1 and last_x == 1 and left == 0:
                last_segment = segment
            else:
                raise ValueError("The nine real source segments are not ordered")
            if not left < right <= 1:
                raise ValueError("Invalid true source panel")
            last_x = right
            V, a, w = (ball(g[key]) for key in ("V", "V_over_w", "w"))
            material = ball(g["material_cV_over_w"])
            radial = ball(g["radial_log_increment"])
            variation = ball(g["log_w_variation"])
            down = ball(g["log_w_down_variation"]).upper()
            if not (V > 0 and a > 0 and w > 0 and w <= arb(1)/2
                    and material > 0 and radial > 0 and variation >= 0 and down >= 0):
                raise ArithmeticError("A complete positive panel enclosure is required")
            Jlo = (material.lower()/k.upper()).lower()
            Jhi = (material.upper()/k.lower()).upper()
            growth = (q*down).exp().upper()
            propagation = (q*down-lo*Jlo).exp().upper()
            emitted = {name: arb(0) for name in FAMILIES}
            if n == source:
                # d1 dr=(V^2/w)dlog(r), d_lambda dr=(V^2/w)|dlog(w)|.
                # Both are bounded by d=k*V*chi, using the SAME q strip.
                mass1 = (V.upper()*a.upper()*radial.upper()).upper()
                massl = (V.upper()*a.upper()*variation.upper()).upper()
                common = (k.upper()*V.upper()*(-(-lo*Jhi).expm1())/lo).upper()
                e1 = min(mass1, common)
                el = min(massl, common)
                Ecoef = (2*(1+w.upper()**2)).upper()
                # The exact signed-frequency support of low+low -> near gives
                # D=(1+|j|)(1+|b|)>=279.  B>=120,w<=1/2 bound every
                # d_lambda component coefficient by 2/279; never apply
                # this coefficient to d1 or to the complete remainder.
                mixed = min((Ecoef*mass1+arb(2)/279*massl).upper(),
                            (Ecoef*common).upper())
                emitted = dict(d1=(growth*e1).upper(),
                               d_lambda=(growth*el).upper(),
                               low_to_near_quadratic=(growth*mixed).upper())
            for name in FAMILIES:
                within = ((growth*states[name]+emitted[name])/V.lower()).upper()
                if within > maximum[name]:
                    maximum[name] = within
                    witnesses[name] = dict(panel=i, segment=segment,
                                           x_left=g["x_left"], x_right=g["x_right"])
                states[name] = (propagation*states[name]+emitted[name]).upper()
            count += 1
            if count % 256 == 0:
                monitor.record("panel", band=[lo, hi], cell=n, panels=count)
        if last_segment != 8 or last_x != 1:
            raise ValueError("The whole cell was not covered")
        factor = exact_q(sigma[source]**2/sigma[n])
        # Separate radial suprema of the two physical components cost the
        # same factor2 retained in the original causal Green proof.
        qgamma = {name: (2*(1+hi)*maximum[name]).upper() for name in FAMILIES}
        sgamma = {name: (factor*qgamma[name]).upper() for name in FAMILIES}
        out.append(dict(output_cell=n, source_cell=source, panels=count,
                        q_gamma={name: ball_record(v) for name, v in qgamma.items()},
                        gamma={name: ball_record(v) for name, v in sgamma.items()},
                        witnesses=witnesses,
                        exact_source_scale=[str((sigma[source]**2/sigma[n]).numerator),
                                            str((sigma[source]**2/sigma[n]).denominator)]))
        previous_B = B
        monitor.record("cell", band=[lo, hi], cell=n, panels=count)
    return dict(first_mode=lo, last_mode=hi, rows=out)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("material-summary", "q-density", "out"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--same-tau-density", type=Path)
    p.add_argument("--source-cell", type=int, default=13)
    p.add_argument("--target-first", type=int, default=12)
    p.add_argument("--band", action="append", default=[])
    p.add_argument("--rss-limit-mib", type=int, default=100)
    args = p.parse_args()
    if not 12 <= args.target_first <= args.source_cell <= 23:
        raise ValueError("Only existing complete true shallow panels12..23 are used")
    bands = [tuple(map(int, x.split(":"))) for x in (args.band or ["94:96"])]
    if any(len(b) != 2 or b[0] < 94 or b[1] > 192 or b[0] > b[1]
           or b[0] % 2 or b[1] % 2 for b in bands):
        raise ValueError("Use even near-cover bounds94..192; actual support remains94..184")
    resource_path = args.out.with_name(args.out.name+"-resource.jsonl")
    if args.out.exists() or resource_path.exists():
        raise FileExistsError("Use a fresh output and resource prefix")
    ctx.prec = 192
    monitor = Monitor(resource_path, args.rss_limit_mib)
    hashes = {str(path): digest(path) for path in (args.material_summary, args.q_density)}
    summary, density = read(args.material_summary), read(args.q_density)
    if not all(density["gates"].values()):
        raise ValueError("The q continuous strip and complete mean domains must be paid")
    qhash = hashes[str(args.q_density)]
    panel_entries = {r["cell"]: r for r in summary["cells"]}
    panels, metadata = {}, {}
    for n in range(args.target_first, args.source_cell+1):
        e = panel_entries[n]
        path = Path(e["file"])
        if digest(path) != e["sha256"]:
            raise ValueError("A completed true material panel package changed")
        hashes[str(path)] = e["sha256"]
        meta = metadata_without_array(path, "panels")
        if (meta["cell"] != n or qhash not in meta["input_hashes"].values()
                or meta["strip_definition"] != STRIP_DEFINITION):
            raise ValueError("The material belongs to a different whole continuous strip")
        row = next(r for r in density["rows"] if r["cell"] == n)
        for key in ("B", "tau_inner", "tau_outer"):
            if not same_interval(meta[key], row[key]):
                raise ValueError("The panel and density norm differ: "+key)
        if not same_interval(meta["k"], density["k"]):
            raise ValueError("The q source damping coefficient differs")
        panels[n], metadata[n] = path, meta
        monitor.record("material-identity", cell=n)
    sigma = {r["cell"]: Fraction(1) for r in density["rows"]}
    target_density_hash = qhash
    if args.same_tau_density:
        target = read(args.same_tau_density)
        target_density_hash = digest(args.same_tau_density)
        hashes[str(args.same_tau_density)] = target_density_hash
        origin = target.get("continuous_strip_origin", {})
        if (origin.get("path") != str(args.q_density) or origin.get("sha256") != qhash
                or not all(target["gates"].values())):
            raise ValueError("The target must explicitly use the entire original q strip")
        if [r["cell"] for r in target["rows"]] != [r["cell"] for r in density["rows"]]:
            raise ValueError("The target complete cell domain differs")
        for qr, sr in zip(density["rows"], target["rows"]):
            for key in ("B", "Q_coefficient", "mu_lower", "mu_upper", "w_lower",
                        "normalized_width_upper", "TV_log_w_upper", "tau_inner", "tau_outer"):
                if not same_interval(qr[key], sr[key]):
                    raise ValueError("The strong same-strip physical shape differs: "+key)
            qx = exact_chosen(qr["canonical_total_envelope"])
            sx = exact_chosen(sr["canonical_total_envelope"])
            if not qx > 0 or not sx > 0:
                raise ValueError("The cellwise physical scales must be positive")
            sigma[qr["cell"]] = sx/qx
    result = dict(
        status="Separate true-panel high material kernels; no new nonlinear joint gate",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        source_cell=args.source_cell, target_first=args.target_first,
        actual_near_support=[94, 184], comparison_cover_last_maximum=192,
        continuous_strip_origin=dict(path=str(args.q_density), sha256=qhash,
                                     definition=STRIP_DEFINITION),
        target_density_sha256=target_density_hash,
        material_definitions=dict(d1="V^2/(r*w)", d_lambda="abs(w_r/w)*V^2/w"),
        mixed_source="2*(1+w^2)*d1+(2/279)*d_lambda; only DQ(low centre)low input -> near output",
        separate_component_supremum_factor=2,
        full_mean_inverse_remainder_unchanged=True,
        complete_quadratic_new_variation_unchanged=True,
        support_omissions="Only the stated quadratic centre-linear source is restricted; no complete-source or far graph column is removed",
        source_scale="Each source-cell kernel scales by sigma_source^2/sigma_output under the explicitly identical q strip",
        bands=[run_band(args, b, density, panels, metadata, sigma, monitor) for b in bands],
        input_hashes=hashes,
        source_hashes={name: digest(Path(__file__).with_name(name)) for name in
                       (Path(__file__).name, "closure_split_joint_io.py",
                        "closure_real_head_source_enclosure.py", "closure_real_head_green_enclosure.py")},
        source_values_recomputed=False, new_radial_quadratures=0,
        new_ODE_or_fundamental_matrix_integrations=0,
        original_combined_kernel_replaced=False, complete_head_closed=False)
    result["resource"] = monitor.record("completed", bands=len(bands))
    payload = (json.dumps(result, indent=2)+"\n").encode()
    if args.out.suffix == ".gz":
        payload = gzip.compress(payload, mtime=0)
    if len(payload) >= 5_000_000:
        raise ValueError("The output exceeds the per-file repository cap")
    args.out.write_bytes(payload)
    print(json.dumps(dict(output=str(args.out), sha256=hashlib.sha256(payload).hexdigest(),
                          resource=result["resource"],
                          scope="separate material kernel only; full strong closure unpaid")), flush=True)


if __name__ == "__main__":
    main()
