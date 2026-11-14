#!/usr/bin/env python3
"""Integrate the current complete moving first-symbol finite part.

The strict part consumes the original169 high-seven scalar germs, all
candidate modes and exact continuity offsets. Only the common root piece
uses fresh complete Arb scalar jets. Both nonintegrable root terms are
removed analytically. This is the integral Xi from the accompanying
strict-symbol theorem; complete Airy/positive-return identification is
explicitly not claimed.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import time

from flint import arb, arb_poly, arb_series, ctx

from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_final_continuous_value_repair import iter_repair
from fourfold_codazzi_phase_complete_Arb_high_scalar_jets import FullArbScalarTarget
from fourfold_codazzi_phase_scalar_cache_jets import normalized_true_jets, read
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_metric_defect import record, save, sha

CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
REPAIR = "6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc"
COVER = "94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3"
ROOT = "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
OBJECT = "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
NU = Fraction(-2572625729470897, 72057594037927936)
N = 32


def fraction(value):
    return Fraction.from_float(float(value))


def exact_point(value):
    """The exact binary midpoint of an Arb point; not a float roundtrip."""
    a, e = map(int, value.mid().man_exp())
    return Fraction(a*2**e) if e >= 0 else Fraction(a, 2**(-e))


def actual_width(value):
    return (2*value.rad()).upper()


def angular_moments(states, count=8):
    """Every signed Laurent coefficient participates, including v's mean."""
    U, V = [], []
    for n in range(count):
        uu, vv = [arb(0)]*(2*N+1), [arb(0)]*(2*N+1)
        vv[N] = states[N][n]
        for j in range(1, N+1):
            uu[N+j] = -states[j-1][n]/2
            uu[N-j] = states[j-1][n]/2
            vv[N+j] = vv[N-j] = states[N+j][n]/2
        U.append(arb_poly(uu))
        V.append(arb_poly(vv))
    def product(a, b):
        out = []
        for n in range(count):
            z = arb_poly([])
            for h in range(n+1):
                z += a[h]*b[n-h]
            out.append(z)
        return out
    # The odd physical field is i U. All remaining products are real.
    UU, VV = product(U, U), product(V, V)
    u2 = arb_series([-z[2*N] for z in UU], prec=count)
    v2 = arb_series([z[2*N] for z in VV], prec=count)
    u4, u2v2, v4, cross = [], [], [], []
    for n in range(count):
        a = c = e = t = arb(0)
        for h in range(n+1):
            a += (UU[h]*UU[n-h])[4*N]
            c -= (UU[h]*VV[n-h])[4*N]
            e += (VV[h]*VV[n-h])[4*N]
            t -= sum((4*j*states[j-1][h]*states[N+j][n-h]
                      for j in range(1, N+1)), arb(0))
        u4.append(a); u2v2.append(c); v4.append(e); cross.append(t)
    return dict(u2=u2, v2=v2,
        u4=arb_series(u4, prec=count),
        u2v2=arb_series(u2v2, prec=count),
        v4=arb_series(v4, prec=count),
        uvphi_minus_vuphi=arb_series(cross, prec=count))


class Consumer:
    def __init__(self, args):
        self.args = args
        self.started = time.monotonic()
        self.base = args.topic.resolve()
        self.inputs = dict(candidate=args.candidate, cover=args.scalar_cover,
            repair=args.repair, root=args.root_germ, object=args.object)
        self.expected = dict(candidate=CANDIDATE, cover=COVER, repair=REPAIR,
            root=ROOT, object=OBJECT)
        for name, path in self.inputs.items():
            if sha(path) != self.expected[name]:
                raise ValueError("a current exact input changed: "+name)
        self.cover, self.repair, self.root = (
            read(self.inputs[name]) for name in ("cover", "repair", "root"))
        if (not self.cover["complete"] or not self.repair["complete"]
                or not self.root["complete"]
                or self.repair["derived_definition_sha256"] != CENTRE
                or self.cover["configuration"]["exact_nu"] != str(NU)
                or self.cover["exact_affine_offset"] != "0"):
            raise ValueError("a complete same-centre eta0 input is required")
        self.saved = load_candidate(args.candidate)
        self.meta = json.loads(str(self.saved["metadata"]))
        self.alpha = Fraction(self.meta["exact_float_amplitude"])
        if (self.meta["object_sha256"] != OBJECT or int(self.meta["modes"]) != N
                or Fraction(self.meta["exact_float_nu"]) != NU
                or self.saved["piece_coefficients"].shape != (4, 6144, 65)):
            raise ValueError("the full current candidate identity changed")
        self.nodes = list(map(fraction, self.saved["radial_nodes"]))
        self.root_piece = int(self.root["actual_candidate_piece"])
        if self.root_piece != 2549:
            raise ValueError("the common actual root candidate piece changed")
        self.offsets = []
        for piece, offset, _ in iter_repair(self.saved, self.alpha):
            self.offsets.append(offset)
            if piece == self.root_piece:
                break
        saved_root_offset = tuple(map(Fraction,
            self.repair["special_piece_offsets"][str(self.root_piece)]["physical_offset"]))
        if self.offsets[-1] != saved_root_offset or len(self.offsets) != self.root_piece+1:
            raise ValueError("the complete exact continuity prefix differs")
        self.root_lo, self.root_hi = map(Fraction, self.root["root_interval"])
        self.cut = self.root_lo-args.cut_gap
        if not self.nodes[self.root_piece] < self.cut < self.root_lo:
            raise ValueError("the chosen root collar is not wholly in its true candidate piece")
        self.strict_stop = Fraction(self.cover["exact_complete_interval"][1])
        if not 0 < self.cut < self.strict_stop < self.root_lo:
            raise ValueError("the strict cut leaves the genuine complete scalar cover")
        self.provider = FullArbScalarTarget(args.object, Fraction(0), args.exponential_bits, 7)
        self.polynomial_cache = {}
        self.rows, self.rejected = [], []
        self.strict_integral = arb(0)
        self.cursor = Fraction(0)
        self.scalar_inputs = []
        self.state = dict(kind="current_complete_moving_first_symbol_finite_part",
            complete=False, finite_part_enclosure_complete=False,
            source_sha256=sha(__file__), candidate_sha256=CANDIDATE,
            continuous_centre_definition_sha256=CENTRE,
            exact_alpha=str(self.alpha), exact_nu=str(NU),
            actual_affine_parameter="eta_0", exact_affine_offset="0",
            explicit_family_parameter_delta="0", whole_original_eta=False,
            actual_R31_selected_delta_interval_not_consumed=True,
            inputs={name:dict(path=str(path), sha256=self.expected[name])
                    for name, path in self.inputs.items()},
            requested_interval_width=str(args.width_goal),
            exact_strict_cut=str(self.cut), exact_root_collar_gap_from_original_lower=str(args.cut_gap),
            original169_scalar_models_recomputed=False,
            only_true_common_root_scalar_jet_evaluations_are_new=True,
            all65_state_coefficients_and_even_mean_retained=True,
            full_Laurent_products_no_Fourier_projection=True,
            old_pointwise_R0_zero_assumption_used=False,
            integral_is_Xi_from_complete_strict_symbol_theorem=True,
            full_return_beta_identification_not_claimed=True,
            current_root_Airy_positive_port_and_strong_constants_not_paid=True,
            true_PDE_solution_branch_and_full_inverse_not_claimed=True,
            public_run_id=os.environ.get("GITHUB_RUN_ID"),
            public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            failure=None)

    def checkpoint(self, label):
        self.state.update(stage=label, seconds=time.monotonic()-self.started,
            exact_completed_strict_prefix=str(self.cursor),
            completed_strict_integral=record(self.strict_integral),
            accepted_strict_rows=len(self.rows), rejected_strict_rows=len(self.rejected),
            scalar_inputs=self.scalar_inputs, rows=self.rows, rejected_cells=self.rejected)
        save(self.args.partial, self.state)

    def candidate_states(self, piece, left, right, s, inward=False):
        count = 8
        if piece not in self.polynomial_cache:
            cc = self.saved["piece_coefficients"][:, piece, :]
            self.polynomial_cache[piece] = [
                [exact_arb(self.alpha*fraction(cc[k, j])) for k in range(4)]
                for j in range(65)]
        x = arb_series([real_interval(left-self.nodes[piece], right-self.nodes[piece]),
                        -1 if inward else 1], prec=count)
        result = []
        for j, cc in enumerate(self.polynomial_cache[piece]):
            z = arb_series([cc[0]], prec=count)
            for coefficient in cc[1:]:
                z = z*x+coefficient
            z += exact_arb(self.offsets[piece][j])
            result.append(z)
        result[N] += s
        return result

    def strict_jets(self, row, piece, left, right):
        sc = {name:arb_series(normalized_true_jets(row, name, left, right), prec=8)
              for name in ("beta", "q", "gamma", "s")}
        states = self.candidate_states(piece, left, right, sc["s"])
        moments = angular_moments(states)
        q, b = sc["q"], sc["beta"]
        eta = -sc["gamma"]*states[N]
        if not q[0] > 0 or not eta[0] > 0:
            raise ArithmeticError("the full strict q or eta denominator does not separate from zero")
        h = q.derivative()/(2*q)
        U2, V2, U4, UV, V4, cross = (moments[k] for k in
            ("u2", "v2", "u4", "u2v2", "v4", "uvphi_minus_vuphi"))
        square = 1+2*U2+2*q*q*V2+U4-2*q*q*UV+q**4*V4
        Xi = (h*h+2*h*b*(1+U2+q*q*V2)+b*b*square)/(eta*q)-2*b*q*cross
        if Xi.prec < 7 or any(not Xi[j].is_finite() for j in range(7)):
            raise ArithmeticError("the complete strict sixth derivative is missing")
        return Xi

    def integrate_cell(self, row, scalar_sha, piece, left, right, depth):
        middle = (left+right)/2
        point = self.strict_jets(row, piece, middle, middle)
        whole = self.strict_jets(row, piece, left, right)
        h = exact_arb((right-left)/2)
        central = sum((2*point[j]*h**(j+1)/(j+1) for j in (0, 2, 4)), arb(0))
        remainder = (2*abs(whole[6])*h**7/7).upper()
        value = central+arb(0, remainder)
        allocation = exact_arb(self.args.width_goal*Fraction(1, 4)*(right-left)/self.cut)
        if not actual_width(value) <= allocation:
            self.rejected.append(dict(interval=[str(left),str(right)], depth=depth,
                width=record(actual_width(value)), allocation=record(allocation),
                complete_Taylor_remainder=record(remainder)))
            if depth >= self.args.max_depth:
                raise ArithmeticError("a complete strict Taylor integral exhausted its declared subdivision budget")
            self.integrate_cell(row, scalar_sha, piece, left, middle, depth+1)
            self.integrate_cell(row, scalar_sha, piece, middle, right, depth+1)
            return
        if left != self.cursor:
            raise ArithmeticError("a strict integral cell leaves a gap or overlaps its predecessor")
        self.strict_integral += value
        self.cursor = right
        self.rows.append(dict(interval=[str(left),str(right)], actual_candidate_piece=piece,
            scalar_native_sha256=scalar_sha, depth=depth,
            complete_signed_integral=record(value), complete_sixth_derivative_Taylor_fee=record(remainder)))

    def integrate_strict(self):
        cursor_scalar = Fraction(0)
        for germ in self.cover["germs"]:
            path = self.base/Path(germ["path"])
            if sha(path) != germ["sha256"]:
                raise ValueError("an original high-seven scalar germ changed")
            native = read(path)
            if not native["complete"] or native["configuration"] != self.cover["configuration"]:
                raise ValueError("a complete same-configuration scalar germ is required")
            self.scalar_inputs.append(dict(germ_index=germ["germ_index"],path=str(path),sha256=germ["sha256"]))
            for row in native["rows"]:
                a, b = map(Fraction, row["interval"])
                if a != cursor_scalar:
                    raise ValueError("the immutable scalar cells fail chronological coverage")
                cursor_scalar = b
                if a >= self.cut:
                    break
                left, end = a, min(b, self.cut)
                while left < end:
                    piece = bisect_right(self.nodes, left)-1
                    right = min(end, self.nodes[piece+1])
                    self.integrate_cell(row, germ["sha256"], piece, left, right, 0)
                    left = right
            self.checkpoint("strict-germ-"+str(germ["germ_index"]))
            print(dict(stage="strict", germ=germ["germ_index"],
                complete_point=str(self.cursor), rows=len(self.rows),
                integral=self.strict_integral.str(18), seconds=time.monotonic()-self.started), flush=True)
            if self.cursor == self.cut:
                break
        if self.cursor != self.cut:
            raise ArithmeticError("the complete strict target interval was not covered")

    def refine_root(self):
        lo, hi = self.root_lo, self.root_hi
        history = []
        for step in range(6):
            whole, germ = self.provider.coefficients(lo, hi, NU)
            if not whole["K1"] > 0:
                raise ArithmeticError("the whole true root derivative loses its positive sign")
            middle = (lo+hi)/2
            point, pointgerm = self.provider.coefficients(middle, middle, NU)
            if germ != pointgerm:
                raise ValueError("a root Newton step crossed an intrinsic germ")
            image = exact_arb(middle)-point["K"]/whole["K1"]
            nl = max(lo, exact_point(image.lower()))
            nh = min(hi, exact_point(image.upper()))
            if not lo <= nl < nh <= hi:
                raise ArithmeticError("the directed true root image has no certified nonempty intersection")
            history.append(dict(step=step,old_interval=[str(lo),str(hi)],
                complete_K_at_midpoint=record(point["K"]),
                complete_whole_K1=record(whole["K1"]),
                directed_mean_value_image=record(image),new_interval=[str(nl),str(nh)],
                actual_scalar_germ=list(map(str,germ))))
            lo, hi = nl, nh
            if hi-lo < Fraction(1, 2**self.args.root_precision_bits):
                break
        if not hi-lo < Fraction(1, 2**self.args.root_precision_bits):
            raise ArithmeticError("the actual fixed-eta0 root was not refined to the declared precision")
        self.state["original_unique_root_enclosure"] = list(map(str,(self.root_lo,self.root_hi)))
        self.state["actual_eta0_root_enclosure"] = list(map(str,(lo,hi)))
        self.state["root_refinement"] = history
        self.root_lo_new, self.root_hi_new = lo, hi
        self.checkpoint("root-refined")

    def root_decomposition(self, left, right, point):
        values, germ = self.provider.coefficients(left, right, NU)
        if not values["K1"] > 0:
            raise ArithmeticError("the root factor requires the full positive K derivative")
        def scalar(name):
            return arb_series([(-1)**j*values[name+(str(j) if j else "")]/math.factorial(j)
                               for j in range(8)], prec=8)
        # k(rho)=integral_0^1 K_r(rstar-t*rho)dt. Its normalized jth
        # derivative lies in (-1)^j K^(j+1)/(j+1)! on the full interval.
        k = arb_series([(-1)**j*values["K"+str(j+1)]/math.factorial(j+1)
                        for j in range(7)], prec=7)
        b, gamma, s = scalar("beta"), scalar("gamma"), scalar("s")
        states = self.candidate_states(self.root_piece, left, right, s, inward=True)
        moments = angular_moments(states)
        eta = -gamma*states[N]
        if not eta[0] > 0 or not k[0] > 0:
            raise ArithmeticError("the complete root eta and k denominators lack positive gaps")
        hupper = self.root_hi_new-self.cut
        rhovalue = arb(0) if point else real_interval(Fraction(0), hupper)
        rho = arb_series([rhovalue,1], prec=8)
        U2, V2, U4, UV, V4, cross = (moments[n] for n in
            ("u2","v2","u4","u2v2","v4","uvphi_minus_vuphi"))
        sqrtk = k.sqrt()
        common = eta*sqrtk
        a = k.derivative()/(4*k)-b
        mean_a0 = a-b*(U2+rho*k*V2)
        mean_a0_squared = (a*a-2*a*b*(U2+rho*k*V2)
            +b*b*(U4+2*rho*k*UV+rho*rho*k*k*V4))
        A = 1/(16*common)
        B = mean_a0/(2*common)
        C = mean_a0_squared/common
        D = 4*b*b*sqrtk*UV/eta+2*b*sqrtk*cross
        result = dict(A=A,B=B,C=C,D=D)
        for name, order in dict(A=6,B=5,C=4,D=3).items():
            if result[name].prec <= order or not result[name][order].is_finite():
                raise ArithmeticError("a complete root derivative is unavailable: "+name)
        return result, dict(actual_scalar_germ=list(map(str,germ)),
            complete_k_positive_gap=record(k[0].lower()),
            complete_eta_positive_gap=record(eta[0].lower()),
            complete_intrinsic_provider_details=self.provider.last_details)

    def integrate_root(self):
        p, pd = self.root_decomposition(self.root_lo_new, self.root_hi_new, True)
        w, wd = self.root_decomposition(self.cut, self.root_hi_new, False)
        h = real_interval(self.root_lo_new-self.cut, self.root_hi_new-self.cut)
        value = arb(0)
        point_coefficients = {}
        for name, maximum, shift, sign in (("A",5,Fraction(-3,2),1),
            ("B",4,Fraction(-1,2),1),("C",3,Fraction(1,2),1),
            ("D",2,Fraction(3,2),-1)):
            point_coefficients[name] = []
            for n in range(maximum+1):
                exponent = Fraction(n)+shift
                contribution = sign*p[name][n]*(h**exact_arb(exponent))/exact_arb(exponent)
                value += contribution
                point_coefficients[name].append(dict(order=n,normalized_derivative=record(p[name][n]),
                    exact_integrated_power=str(exponent),complete_contribution=record(contribution)))
        tail = (sum((abs(w[name][order]) for name,order in
                     (("A",6),("B",5),("C",4),("D",3))),arb(0))
                *h**exact_arb(Fraction(9,2))/exact_arb(Fraction(9,2))).upper()
        root_integral = value+arb(0,tail)
        self.state["root_finite_part"] = dict(
            exact_physical_collar_left=str(self.cut),root_to_cut_length=record(h),
            point_provider=pd,whole_provider=wd,
            g0=record(p["A"][0]),g1=record(p["A"][1]+p["B"][0]),
            actual_finite_Taylor_terms=point_coefficients,
            complete_next_normalized_derivatives={name:record(w[name][order])
                for name,order in (("A",6),("B",5),("C",4),("D",3))},
            complete_root_Taylor_remainder=record(tail),
            complete_signed_root_finite_part=record(root_integral),
            both_exact_nonintegrable_root_terms_subtracted=True,
            root_value_K_equals_zero_used_as_proved_root_identity=True,
            no_formal_zero_substitution_into_numerical_K_ball=True)
        total = self.strict_integral+root_integral
        width = actual_width(total)
        goodwidth = bool(width < exact_arb(self.args.width_goal))
        self.state.update(finite_part_enclosure_complete=True,
            complete_signed_first_symbol_finite_part=record(total),
            complete_interval_width=record(width), requested_interval_width_met=goodwidth,
            minus_quarter_of_integral_with_no_return_identification=record(-total/4),
            genuine_root_scalar_evaluations=self.provider.evaluations,
            complete_scalar_germs_consumed=len(self.scalar_inputs))
        gates = [
            ("the original complete scalar cover reaches the chosen strict cut", self.cursor == self.cut),
            ("the complete exact continuous candidate offset reaches its true root piece",len(self.offsets)==2550),
            ("the actual eta0 unique root is rigorously refined",self.root_hi_new-self.root_lo_new<Fraction(1,2**self.args.root_precision_bits)),
            ("the full root finite part is a finite interval",root_integral.is_finite()),
            ("every complete strict integral and full finite part is finite",self.strict_integral.is_finite() and total.is_finite()),
            ("the requested whole finite-part interval width is met",goodwidth),
        ]
        self.state["gates"] = [dict(name=n,passed=bool(v)) for n,v in gates]
        self.state["complete"] = all(bool(v) for _,v in gates)
        self.checkpoint("complete" if self.state["complete"] else "complete-wide-enclosure")
        save(self.args.out,self.state)
        print(dict(complete=self.state["complete"],finite_part=total.str(30),width=width.str(14),
            minus_quarter=(-total/4).str(30),all_return_identification_still_open=True,
            seconds=time.monotonic()-self.started),flush=True)
        if not self.state["complete"]:
            raise ArithmeticError("the complete finite-part enclosure is valid but misses its requested width")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic",type=Path,default=Path.cwd())
    parser.add_argument("--candidate",type=Path,required=True)
    parser.add_argument("--scalar-cover",type=Path,required=True)
    parser.add_argument("--repair",type=Path,required=True)
    parser.add_argument("--root-germ",type=Path,required=True)
    parser.add_argument("--object",type=Path,required=True)
    parser.add_argument("--cut-gap",type=Fraction,default=Fraction(1,262144))
    parser.add_argument("--width-goal",type=Fraction,default=Fraction(1,1000))
    parser.add_argument("--max-depth",type=int,default=14)
    parser.add_argument("--bits",type=int,default=256)
    parser.add_argument("--exponential-bits",type=int,default=192)
    parser.add_argument("--root-precision-bits",type=int,default=140)
    parser.add_argument("--partial",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("run this mathematical integration in the public repository's real Actions job")
    if args.out.exists() or args.partial.exists():
        raise FileExistsError("preserve every actually executed finite-part prefix")
    if not 0<args.width_goal<1 or not 0<args.cut_gap<Fraction(1,100000):
        raise ValueError("an explicit strict interval width and true local root collar are required")
    ctx.prec=args.bits;ctx.cap=8
    work=None
    try:
        work=Consumer(args)
        work.checkpoint("inputs-verified")
        work.refine_root()
        work.integrate_strict()
        work.integrate_root()
    except Exception as exc:
        if work is not None:
            work.state["failure"]=f"{type(exc).__name__}: {exc}"
            work.state["complete"]=False
            work.checkpoint("failed-original-prefix-preserved")
            if not args.out.exists():
                save(args.out,work.state)
        raise


if __name__=="__main__":
    main()
