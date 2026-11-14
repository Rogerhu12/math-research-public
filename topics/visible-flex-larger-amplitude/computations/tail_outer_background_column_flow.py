#!/usr/bin/env python3
"""Validated outer background columns from the actual positive moment panels.

For a fixed GLOBAL mu_star the gauged linear height equation is q'=a*v,
v'=-b*q, with a,b positive on every real outer source, including all caps
and valley controls. R26 real panel widths and w/r boxes enclose both
positive integrals; the frozen R29 Peano matrices enclose the true flow.
This is a finite-mode background column / inverse-input computation. It
does not assert a nonlinear outer solution or a full-frequency Schur gate.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record, dyadic_endpoint
from closure_real_head_green_enclosure import ball
from closure_real_linear_head_enclosure import peano_matrix, positive_scale_bounds, range_record
from closure_projective_interval_column import ProjectiveColumn
from closure_split_joint_io import read, digest, iter_array, metadata_without_array


FROZEN = {
    "closure_real_linear_head_enclosure.py": "1b8023b53eeca7a0ef28816a99b1b7d4a43f025c2482afae9e88db572e174b8e",
    "closure_projective_interval_column.py": "45997a1d5be6326a1ebbe85ac4240ea7d9dde1c2fb6acdf832460dade89e4f97",
    "closure_real_head_source_enclosure.py": "97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47",
    "closure_split_joint_io.py": "cd03e2fc375e19c8b4d291b601e423a37c584a3e4402957c9f377e82b8cce390",
}


def state_record(column):
    return dict(pivot=column.pivot, sign=column.sign,
                absolute_lower=dyadic_endpoint(column.absolute_lower),
                absolute_upper=dyadic_endpoint(column.absolute_upper),
                ratio=ball_record(column.ratio))


def matrix_from_basis(columns):
    vectors = [column.values() for column in columns]
    return [[vectors[j][i] for j in range(2)] for i in range(2)]


def positive_integrals(row, mode, rc, mu_star, sqrt12):
    r, w, width = (ball(row[key]) for key in ("radius", "w", "width"))
    if not all(x > 0 for x in (r, w, width)):
        raise ArithmeticError("A real positive panel range is missing")
    u = mode*mode-4
    nu = arb(mode*mode*(mode*mode-1))/12
    # These are enclosures of the SAME true integrals, using dr as the
    # positive measure. No assumption about the sign of w_x is used.
    A = sqrt12*mu_star*(rc/r)**(2*u)*r**(-8)*width/w
    B = nu*sqrt12/mu_star*(r/rc)**(2*u)*r**6*width*w
    if not A > 0 or not B > 0:
        raise ArithmeticError("The actual positive integral range lost positivity")
    return A, B, r, w


def physical_caps(column, major, mode, r, w, rc, mu_star, sqrt12):
    initial = column.absolute_uppers()
    within = [sum((major[i][j]*initial[j] for j in range(2)), arb(0)).upper()
              for i in range(2)]
    u = mode*mode-4
    q = (abs((r/rc)**u).upper()*within[0]).upper()
    xi_global = (abs((rc/r)**u).upper()*within[1]).upper()
    H = (r**4*q).upper()
    P = (mode*r**3*q/w).upper()
    K = (mode*mode*r**3*q/w+sqrt12*mu_star*xi_global/(r**4*w*w)).upper()
    return dict(Q=q, global_Xi=xi_global, H=H, P=P, K=K)


def endpoint_record(column, mode, radius, rc, mu_star, sqrt12):
    u = mode*mode-4
    qbounds = positive_scale_bounds(column.component_bounds(0), (radius/rc)**u)
    xbounds = positive_scale_bounds(column.component_bounds(1), (rc/radius)**u)
    hbounds = positive_scale_bounds(qbounds, radius**4)
    return dict(Q=range_record(qbounds), H_per_unit_shallow_Q=range_record(hbounds),
                global_Xi=range_record(xbounds),
                height_chart_excludes_zero=bool(hbounds[0] > 0 or hbounds[1] < 0),
                projective_state=state_record(column))


def analytic_energy_step(row, previous_balance):
    """All-mode true PK propagation budget in a constant panel frame.

    u=(P,K/b), b>0 is one chosen exact dyadic per panel. The Euclidean
    logarithmic norm is at most d+m*gamma. Frame jumps are paid separately;
    no differentiability of the panelwise frame or sign of ell is assumed.
    """
    r, rx, ell = (ball(row[key]) for key in ("radius", "radius_x", "log_w_x"))
    s = rx/r
    if not s > 0:
        raise ArithmeticError("The true source speed/radius ratio must be positive")
    balance = (1+abs(ell).upper()/s.lower()).sqrt().upper()
    dx = exact_q(F(row["x_right"])-F(row["x_left"]))
    gamma = (abs(s*balance+ell/balance).upper()*dx/2).upper()
    forward = (max((-s-ell).upper(), (-2*ell).upper())*dx).upper()
    backward = (max((s+ell).upper(), (2*ell).upper())*dx).upper()
    if previous_balance is not None:
        forward += max(arb(0), (previous_balance/balance).log().upper())
        backward += max(arb(0), (balance/previous_balance).log().upper())
    return balance, gamma, forward.upper(), backward.upper()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cell-manifests", nargs="+", type=Path, required=True)
    p.add_argument("--columns", type=Path, required=True)
    p.add_argument("--ready", type=Path, required=True)
    p.add_argument("--modes", default="2,4")
    p.add_argument("--max-product", default="1/64")
    p.add_argument("--precision", type=int, default=192)
    p.add_argument("--rss-limit-mib", type=int, default=40)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh actual flow output")
    modes = [int(value) for value in args.modes.split(",")]
    if modes != sorted(set(modes)) or any(m < 2 or m > 92 or m % 2 for m in modes):
        raise ValueError("Use explicit distinct positive even modes within the paid low46 window")
    product_gate = exact_q(F(args.max_product))
    if not 0 < product_gate < 1:
        raise ValueError("The positive Peano product gate must lie in(0,1)")
    ctx.prec = args.precision
    began = time.monotonic()
    def memory_gate(stage):
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss > 1024*args.rss_limit_mib:
            failure_path = args.out.with_name(args.out.stem+"-memory-failure.json")
            if not failure_path.exists():
                failure_path.write_text(json.dumps(dict(
                    status="Owned finite-flow RSS gate failed; process will stop",
                    stage=stage, peak_RSS_KiB=rss, limit_MiB=args.rss_limit_mib,
                    elapsed_seconds=time.monotonic()-began,
                    source_sha256=digest(Path(__file__)), arguments=vars(args),
                    complete_outer_solution_claimed=False), indent=2, default=str)+"\n")
            raise MemoryError("The finite outer-flow stream exceeded its stated RSS cap")
    memory_gate("startup")
    sources = {name: digest(Path(__file__).with_name(name)) for name in FROZEN}
    if sources != FROZEN:
        raise ValueError("A frozen validated linear-flow dependency changed")
    sources[Path(__file__).name] = digest(Path(__file__))
    ready = read(args.ready)
    hashes = {str(path): digest(path) for path in [args.ready, args.columns]+args.cell_manifests}
    columns = metadata_without_array(args.columns, "cell_rows")
    if (columns["start_physical_node"] != 12 or columns["modes"] != list(range(2, 93, 2))
            or hashes[str(args.ready)] not in columns["input_hashes"].values()):
        raise ValueError("The true complete46 inner linear columns use another source")
    endpoint_rows = {row["mode"]: row for row in columns["endpoint_rows"]}
    manifests = [read(path) for path in args.cell_manifests]
    cells = [item["cell"] for item in manifests]
    if not cells or cells != list(range(11, min(cells)-1, -1)):
        raise ValueError("This first implementation starts at node12 and covers consecutive outward cells")
    for item in manifests:
        if (not all(item["checks"].values())
                or sorted(row["source_segment"] for row in item["groups"]) != list(range(9))
                or hashes[str(args.ready)] not in item["original_metadata"]["input_hashes"].values()):
            raise ValueError("An entire true outer source/moment cell is required")
        original_sources = item["original_metadata"]["source_hashes"]
        if (original_sources.get("tail_outer_positive_moment_panels.py") !=
                "d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b"
                or original_sources.get("closure_real_outer_radius.py") !=
                "bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe"):
            raise ValueError("A true outer mathematical panel provider changed")
    reference_inputs = manifests[0]["original_metadata"]["input_hashes"]
    if any(item["original_metadata"]["input_hashes"] != reference_inputs for item in manifests[1:]):
        raise ValueError("All outer cells must retain the same R26 radius anchoring ledger")
    memory_gate("inputs-loaded")
    params = ready["rationalDeepModel"]["physicalParameters"]
    rc = exact_q(params["rCuff"])
    d0 = exact_q(F(ready["rationalDeepModel"]["exactSourceConstants"]["delta0"]))
    mu_star = exact_q(params["epsilonScale"])*(arb(11)/4*(d0*arb(2)**(-11)).log()).exp()
    sqrt12 = arb(12).sqrt()
    start_radius = ball(manifests[0]["original_metadata"]["inner_radius"])
    if not rc > 0 or not mu_star > 0 or not start_radius > rc:
        raise ValueError("The true node12 and fixed positive mu11 normalization are required")
    active = {}
    initial_rows = []
    for m in modes:
        slope = ball(endpoint_rows[m]["raw_worker_slope"])
        scale = (start_radius/rc)**(m*m-4)
        active[m] = dict(phi=ProjectiveColumn([1/scale, scale*slope]),
                         basis=[ProjectiveColumn([arb(1), arb(0)]),
                                ProjectiveColumn([arb(0), arb(1)])])
        initial_rows.append(dict(mode=m, exact_shallow_Q=1,
                                 mu11_true_linear_slope=endpoint_rows[m]["raw_worker_slope"],
                                 b0_initial=state_record(active[m]["phi"])))
    records, count, max_product = [], 0, arb(0)
    phase_total, forward_total, backward_total = arb(0), arb(0), arb(0)
    first_balance, previous_balance = None, None
    failure = None
    location = None
    for item in manifests:
        n = item["cell"]
        caps = {m: {name: arb(0) for name in ("Q", "global_Xi", "H", "P", "K")} for m in modes}
        cell_max = arb(0)
        cell_count = 0
        cell_phase, cell_forward, cell_backward = arb(0), arb(0), arb(0)
        try:
            for group in sorted(item["groups"], key=lambda row: row["source_segment"]):
                path = Path(group["path"])
                if digest(path) != group["sha256"]:
                    raise ValueError("A true source group changed")
                hashes[str(path)] = group["sha256"]
                group_count = 0
                for i, row in enumerate(iter_array(path, "panels")):
                    if row["segment"] != group["source_segment"]:
                        raise ValueError("A source row belongs to another original segment")
                    balance, phase, df, db = analytic_energy_step(row, previous_balance)
                    if first_balance is None:
                        first_balance = balance
                    previous_balance = balance
                    cell_phase = (cell_phase+phase).upper()
                    cell_forward = (cell_forward+df).upper()
                    cell_backward = (cell_backward+db).upper()
                    for m in modes:
                        location = dict(cell=n, segment=row["segment"], panel=i, mode=m,
                                        x_left=row["x_left"], x_right=row["x_right"])
                        A, B, r, w = positive_integrals(row, m, rc, mu_star, sqrt12)
                        product = (A.upper()*B.upper()).upper()
                        if not product <= product_gate:
                            raise ArithmeticError("This true panel needs further source subdivision for the declared Peano product gate")
                        T, major, unused = peano_matrix(A, B)
                        c = physical_caps(active[m]["phi"], major, m, r, w, rc, mu_star, sqrt12)
                        for name, value in c.items():
                            caps[m][name] = max(caps[m][name], value)
                        active[m]["phi"].advance(T)
                        for column in active[m]["basis"]:
                            column.advance(T)
                        cell_max = max(cell_max, product)
                    count, cell_count, group_count = count+1, cell_count+1, group_count+1
                    if count % 64 == 0:
                        memory_gate("panel-stream")
                if group_count != group["panels"]:
                    raise ValueError("A complete true source group was not propagated")
                print(json.dumps(dict(event="outer_background_segment", cell=n,
                                      segment=group["source_segment"], panels=group_count,
                                      seconds=time.monotonic()-began,
                                      peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
                memory_gate("complete-source-group")
            if cell_count != item["panels"]:
                raise ValueError("The complete true cell was not propagated")
            radius = ball(item["original_metadata"]["outer_radius"])
            rows = []
            for m in modes:
                matrix = matrix_from_basis(active[m]["basis"])
                determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
                if not determinant.contains(1):
                    raise ArithmeticError("The independently propagated true basis columns lost the exact determinant-one identity")
                rows.append(dict(mode=m, b0_endpoint=endpoint_record(active[m]["phi"], m, radius, rc, mu_star, sqrt12),
                                 complete_cell_b0_caps={key: ball_record(value) for key, value in caps[m].items()},
                                 global_gauge_fundamental_matrix=[[ball_record(x) for x in row] for row in matrix],
                                 determinant_interval=ball_record(determinant), exact_determinant=1,
                                 basis_states=[state_record(v) for v in active[m]["basis"]]))
            max_product = max(max_product, cell_max)
            phase_total = (phase_total+cell_phase).upper()
            forward_total = (forward_total+cell_forward).upper()
            backward_total = (backward_total+cell_backward).upper()
            record = dict(cell=n, endpoint_physical_node=n, radius=ball_record(radius), panels=cell_count,
                          maximum_AB=ball_record(cell_max), modes=rows,
                          all_mode_homogeneous_energy=dict(
                              cell_phase_upper=ball_record(cell_phase),
                              cumulative_phase_upper=ball_record(phase_total),
                              physical_forward_log_prefactor_upper=ball_record((forward_total+previous_balance.log()).upper()),
                              physical_backward_log_prefactor_upper=ball_record((backward_total+first_balance.log()).upper()),
                              bound="For every even m>=2, ||Phi_PK||_2 <= exp(log_prefactor + m*phase); this is a homogeneous propagation bound only"))
            records.append(record)
            checkpoint = args.out.with_name(args.out.stem+f"-completed-cell{n:03d}.json")
            if checkpoint.exists():
                raise FileExistsError("Use a fresh flow checkpoint prefix")
            checkpoint.write_text(json.dumps(dict(status="Complete true finite background columns through this outward node",
                completed_cells=[r["cell"] for r in records], record=record,
                input_hashes=hashes, source_hashes=sources, mu_star=ball_record(mu_star),
                checkpoint_scope="Exact enclosure recovery only; no nonlinear or full-frequency inverse assertion"), indent=2)+"\n")
        except (ArithmeticError, ValueError, MemoryError) as error:
            failure = dict(type=type(error).__name__, message=str(error), location=location,
                           interpretation="A validated enclosure/coverage gate failed; no singularity or nonexistence is inferred")
            break
    result = dict(
        status="Complete stated finite true outer background flow" if failure is None else "Incomplete true outer background enclosure; explicit failed gate preserved",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        cells_requested=cells, cells_completed=[r["cell"] for r in records], modes=modes,
        ready_sha256=hashes[str(args.ready)], real_inner_columns_sha256=hashes[str(args.columns)],
        start_physical_node=12, end_physical_node=cells[-1],
        global_mu_star=ball_record(mu_star), mu_star_definition="epsilonScale*(delta0*2^-11)^(11/4), fixed on the ENTIRE outer flow",
        initial_b0_rows=initial_rows, cell_rows=records, panels=count,
        maximum_AB=ball_record(max_product), max_product=args.max_product,
        failure=failure, finite_background_flow_complete=failure is None,
        all46_modes_paid=modes == list(range(2, 93, 2)) and failure is None,
        entire_outer_range_paid=cells == list(range(11, -1, -1)) and failure is None,
        nonlinear_Schur_inverse_paid=False, full_frequency_source_kernel_paid=False,
        complete_outer_solution_claimed=False,
        input_hashes=hashes, source_hashes=sources,
        no_new_source_quadrature=True, source_mathematics="Same exact radius/w ranges and positive physical-width measure; no extrapolation of uncapped source formulas",
        source_to_v_column="(r/rc)^(m^2-4)*r^4*w^2/(sqrt(12)*mu_star) times the full normalized K source",
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(event="complete" if failure is None else "failed_gate", output=str(args.out),
                          cells_completed=result["cells_completed"], failure=failure,
                          seconds=result["elapsed_seconds"], peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)
    if failure is not None:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
