#!/usr/bin/env python3
"""Actual-fixed Fejer R722 posterior mean and complete six-control radial boxes.

This is an independent accurate-function implementation. It consumes a complete
source-bound ActualNormalPacketPoint and never calls the working field solver.
The original pure scalar/Hermite and reference-error mathematics are reused with
explicit new bindings. Whole angular intervals are genuinely evaluated here;
a literal-angle fee is not relabelled as a continuous enclosure.

All interval/integral evaluations require the public repository Actions.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import cmp_to_key
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

SCHEMA = "actual-fixed-fejer-meridian-batched-R722-complete-accurate-reference-control-radial-boxes-v1"
INPUT_SHA = "d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7"
ROTATION_SHA = "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b"
MEAN_SHA = "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0"
SEED_MATH_SHA = "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"
SCALAR_SHA = "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6"
POSTERIOR_MEAN_NAME = "fixed_fejer_meridian_batched_producer_R722_posterior_mean_jets.py"
POSTERIOR_MEAN_SHA = "4fc252f8977f4f4246d2cc13583efc0bccd4b28742df3a797d1c266cdd1eac7d"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Accurate same-field radial evaluation requires public Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def load(name, path, digest):
    if sha(path) != digest:
        raise ValueError("Changed complete accurate source: "+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if sha(path) != digest or sha(module.__file__) != digest:
        raise ValueError("A complete accurate module changed while loading")
    return module


def encode(value):
    if isinstance(value, F):
        return str(value)
    if hasattr(value, "json") and callable(value.json):
        return value.json()
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    if value is None or type(value) in (bool, int, str):
        return value
    if type(value) is float and math.isfinite(value):
        # Only pre-existing source-bound JSON metadata reaches this branch.
        # All accurate arithmetic in this module uses Fraction or Interval.
        return value
    raise TypeError("Keep exact arithmetic and finite original source-bound metadata")


def affine(value):
    if (not isinstance(value, (tuple, list)) or len(value) != 2
            or any(isinstance(q, bool) for q in value)):
        raise ValueError("An accurate physical address is alpha*S+beta")
    return tuple(F(q) for q in value)


def midpoint(left, right):
    return tuple((a+b)/2 for a, b in zip(left, right))


def _convert(value, cls, bits):
    if hasattr(value, "lo") and hasattr(value, "hi"):
        return cls(value.lo, value.hi, bits)
    if isinstance(value, dict):
        return {k: _convert(v, cls, bits) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_convert(v, cls, bits) for v in value]
    return value


class EnclosureUnavailable(ArithmeticError):
    pass


class WorkBudget:
    def __init__(self, *, seconds, maximum_leaf_evaluations):
        require_actions()
        if (not isinstance(seconds, (int, float)) or isinstance(seconds, bool)
                or not math.isfinite(seconds) or seconds <= 0
                or type(maximum_leaf_evaluations) is not int or maximum_leaf_evaluations < 1):
            raise ValueError("Declare positive complete accurate work budgets")
        self.started = time.monotonic()
        self.deadline = self.started+seconds
        self.maximum = maximum_leaf_evaluations
        self.leaves = 0

    def check(self, *, leaves=0):
        if type(leaves) is not int or leaves < 0:
            raise ValueError("A work count is a nonnegative integer")
        if self.leaves+leaves > self.maximum or time.monotonic() >= self.deadline:
            raise EnclosureUnavailable("The declared accurate work budget is exhausted; obligations remain")
        self.leaves += leaves

    def metadata(self):
        return dict(actual_leaf_evaluations=self.leaves,
            maximum_leaf_evaluations=self.maximum,
            elapsed_seconds_binary64_hex=float(time.monotonic()-self.started).hex(),
            exhausted=(self.leaves >= self.maximum or time.monotonic() >= self.deadline))


class AccurateFieldGeometry:
    """The complete actual mathematical field, independent of working quadrature."""

    def __init__(self, actual, rotation_module, *, bits=160, rho_leaf_budget=8192,
                 inverse_steps=64, inverse_width="1/1000000000000000000000000",
                 budget):
        require_actions()
        if (sha(type(actual).__init__.__code__.co_filename) != INPUT_SHA
                or sha(rotation_module.__file__) != ROTATION_SHA
                or sha(actual.seed_fees.__file__) != SEED_MATH_SHA
                or sha(actual.continuous_module.__file__) != SCALAR_SHA):
            raise ValueError("Bind the complete actual input and all exact mathematical modules")
        if type(bits) is not int or not 64 <= bits <= 1024:
            raise ValueError("Use a declared complete outward precision")
        if type(rho_leaf_budget) is not int or rho_leaf_budget < 1:
            raise ValueError("Use a positive complete global-rho enclosure budget")
        if type(inverse_steps) is not int or inverse_steps < 1:
            raise ValueError("Use a positive exact inverse-chart refinement budget")
        self.actual, self.r, self.k = actual, rotation_module, actual.seed_fees
        self.bits, self.budget = bits, budget
        self.I = rotation_module.Interval
        self.scalar, self.d, self.context = actual.scalar, actual.scalar.d, actual.context
        self.mean_module = load("_actual_normal_whole_reference_mean",
            actual.paths["mean_integrals"], MEAN_SHA)
        self.posterior_mean_module = load("_actual_complete_R722_posterior_mean",
            actual.topic/"scripts"/"resume_20261126"/POSTERIOR_MEAN_NAME, POSTERIOR_MEAN_SHA)
        self.posterior_mean = self.posterior_mean_module.PosteriorMeanKernel(
            actual, self.k, self.mean_module)
        self.S = self.from_deep(self.scalar.exact_affine_box((F(1), F(0))))
        radius = self.context.model["radius_complete_enclosure"]
        self.R = self.I(F(radius["lower_exact"]), F(radius["upper_exact"]), bits)
        self.H = self.r.binary_word(actual.height.hex())
        self.H0 = self.r.binary_word(actual.seed["initial_height_hex"])
        self.core = tuple(self.r.binary_word(float(v).hex()) for v in actual.core)
        self.fixed_core = tuple(self.r.binary_word(float(v).hex()) for v in self.context.core)
        if self.S.lo <= 0 or self.R.lo <= 0 or len(self.core) != 160 or len(self.fixed_core) != 160:
            raise ValueError("Keep positive exact scalar length/radius and all actual core coefficients")
        if (self.context.model["T0"] != self.mean_module.REFERENCE_UNIT_LAW
                or not 0 <= F(self.context.full.old_ap_bound) < 1
                or not 0 < F(self.context.full.out) < F(1, 40)
                or F(self.context.full.kp) != F(3, 2)):
            raise ValueError("The complete proved unit/nonnegative original reference branch changed")
        self.unit_reference_provenance = dict(
            complete_reference_source_sha256=actual.reference_model["source_sha256"],
            actual_complete_model_T0=self.context.model["T0"],
            old_prefix_ap_bound=str(self.context.full.old_ap_bound),
            exact_tail_width=str(self.context.full.out), exact_tail_kappa=str(self.context.full.kp),
            proved_references=["R669 section 2", "R690 sections 2, 2.1, 2.3"],
            structural_unit_and_nonnegative_vertical=True,
            sampled_norm_or_working_clamp_used_as_proof=False)
        self.support = tuple(tuple(F(v) for v in pair)
            for pair in actual.seed["exact_relative_support_intervals"])
        self.central = tuple(tuple(F(v) for v in pair)
            for pair in actual.seed["exact_relative_central_intervals"])
        self.delta = F(actual.seed["exact_relative_boundary_each_end_length"])
        self.beta = F(actual.seed["exact_relative_boundary_total_length"])
        self.profile_delta = F(actual.seed["exact_profile_delta"])
        if len(self.support) != 2 or len(self.central) != 2 or self.beta != 4*self.delta:
            raise ValueError("Keep the two complete supports and all four boundary layers")
        for i, ((a, b), (ca, cb)) in enumerate(zip(self.support, self.central)):
            if (not 0 < a < ca < cb < b < 1 or ca-a != self.delta or b-cb != self.delta
                    or (i and self.support[i-1][1] >= a)):
                raise ValueError("The complete exact supported seed partition changed")
        self.Lc = self.S*sum((b-a for a, b in self.central), F(0))
        self.bubble = tuple(tuple(F(v) for v in row)
            for row in actual.model["exact_relative_bubble_nodes"])
        self.gamma = tuple(F(v) for v in actual.model["exact_relative_gamma_nodes"])
        if (len(self.bubble) != 2 or any(len(row) != 3 or not 0 < row[0] < row[1] < row[2] < 1
                for row in self.bubble) or len(self.gamma) != 3
                or not 0 < self.gamma[0] < self.gamma[1] < self.gamma[2] < 1):
            raise ValueError("All literal endpoint and added-shape controls are required")
        qwords = actual.model["frozen_moment_Q_definition"]["Q0_binary64_hex"]
        if len(qwords) != 2 or any(len(m) != 3 or any(len(row) != 3 for row in m) for m in qwords):
            raise ValueError("Retain every one of the eighteen frozen Q words")
        self.Q0 = [[[self.point(self.r.binary_word(v)) for v in row] for row in matrix]
                   for matrix in qwords]
        self.fixed_rho = self.prove_rho(self.fixed_core, rho_leaf_budget)
        self.current_rho = (self.fixed_rho if self.core == self.fixed_core
                            else self.prove_rho(self.core, rho_leaf_budget))
        self.inverse_steps = inverse_steps
        self.inverse_width = F(inverse_width)
        if self.inverse_width <= 0:
            raise ValueError("Use a positive inverse-chart interval goal")
        self.omega = actual.continuous_module.ExactOmegaBounds(actual, self.scalar)
        self.all_omega_zero = bool(actual.np.all(actual.omega == 0))
        self.plan = self.make_plan()
        self.counts = dict(whole_scalar_calls=0, whole_seed_piece_calls=0,
            exact_omega_piece_calls=0, exact_control_piece_calls=0,
            accurate_core_inverse_calls=0, complete_reference_means=0)
        self.identity = canonical(encode(dict(schema=SCHEMA, source_sha256=sha(__file__),
            complete_actual_input_identity=actual.identity, precise_field_model=actual.model_identity,
            rotation_source_sha256=ROTATION_SHA, reference_math_source_sha256=SEED_MATH_SHA,
            complete_mean_integral_source_sha256=MEAN_SHA, whole_scalar_source_sha256=SCALAR_SHA,
            posterior_mean_source_sha256=POSTERIOR_MEAN_SHA,
            posterior_mean_theorem_sha256=self.posterior_mean_module.THEOREM_SHA256,
            posterior_mean_definition_identity_sha256=self.posterior_mean.definition_identity,
            precision_bits=bits, complete_exact_radial_plan=self.plan,
            fixed_rho_proof=self.fixed_rho, current_rho_proof=self.current_rho,
            inverse_steps=inverse_steps, inverse_width=self.inverse_width,
            all_outer_variables_retained=True, working_mesh_is_not_the_accurate_domain=True,
            no_working_normal_root_or_field_replayed=True)))

    def point(self, value):
        return self.I(F(value), F(value), self.bits)

    def from_deep(self, value):
        return self.I(F(value[0], self.d.SCALE), F(value[1], self.d.SCALE), self.bits)

    def to_seed(self, value):
        return _convert(value, self.k.Interval, self.bits)

    def from_seed(self, value):
        return _convert(value, self.I, self.bits)

    def deep(self, value):
        return self.d.box(value.lo, value.hi)

    def trig(self, value):
        return tuple(self.from_deep(v) for v in self.d.sine_cosine(self.deep(value)))

    def compare(self, left, right):
        left, right = affine(left), affine(right)
        if left == right:
            return 0
        v = self.scalar.exact_affine_box(tuple(b-a for a, b in zip(left, right)))
        if v[0] > 0:
            return -1
        if v[1] < 0:
            return 1
        raise EnclosureUnavailable("Distinct affine cuts cannot be ordered by the current exact S enclosure")

    def relative(self, left, right):
        a, b = affine(left), affine(right)
        lo, hi = self.point(a[0])+a[1]/self.S, self.point(b[0])+b[1]/self.S
        return self.I(lo.lo, hi.hi, self.bits)

    def width(self, left, right):
        return self.from_deep(self.scalar.width_box(affine(left), affine(right)))

    def series(self, core, angle):
        d = self.d
        pbox = self.deep(angle)
        theta, rho, rhop, support, supportp = pbox, d.ONE, d.ZERO, d.ONE, d.ZERO
        for m, c in enumerate(core, 1):
            if c == 0:
                continue
            nu = 2*m
            sine, cosine = d.sine_cosine(d.scale(pbox, nu))
            q = 1-nu*nu
            theta = d.add(theta, d.scale(sine, F(q, nu)*c))
            rho = d.add(rho, d.scale(cosine, q*c))
            rhop = d.add(rhop, d.scale(sine, -nu*q*c))
            support = d.add(support, d.scale(cosine, c))
            supportp = d.sub(supportp, d.scale(sine, nu*c))
        return dict(theta=self.from_deep(theta), rho=self.from_deep(rho),
            rhop=self.from_deep(rhop), support=self.from_deep(support),
            supportp=self.from_deep(supportp))

    def prove_rho(self, core, maximum_leaves):
        lower = 1-sum((abs((1-(2*m)**2)*c) for m, c in enumerate(core, 1)), F(0))
        upper = 2-lower
        if lower > 0:
            return dict(method="complete exact Fourier L1", lower=lower, upper=upper,
                all_coefficients_used=True, whole_angle_domain_over_pi=["0", "2"])
        pi = self.from_seed(self.k.pi_bounds(self.bits))
        pending, proved = [(F(0), F(2))], []
        while pending:
            self.budget.check()
            a, b = pending.pop()
            angle = self.I(a, b, self.bits)*pi
            rho = self.series(core, angle)["rho"]
            if rho.lo > 0:
                proved.append((a, b, rho.lo, rho.hi))
            else:
                if len(proved)+len(pending)+2 > maximum_leaves:
                    raise EnclosureUnavailable("Whole-circle accurate core rho positivity remains unpaid")
                middle = (a+b)/2
                pending.extend(((middle, b), (a, middle)))
        return dict(method="complete exact closed angular-interval cover",
            lower=min(v[2] for v in proved), upper=max(v[3] for v in proved),
            whole_angle_domain_over_pi=["0", "2"], all_coefficients_used=True,
            complete_positive_cells=[list(v) for v in sorted(proved)])

    def fixed_chart(self, phi):
        q = self.series(self.fixed_core, phi)
        rho = q["rho"].intersect(self.I(self.fixed_rho["lower"], self.fixed_rho["upper"], self.bits))
        st, ct = self.trig(q["theta"])
        sn, cn = self.trig(phi)
        z = self.point(0)
        er, et, nr, nt = [ct, st, z], [-st, ct, z], [cn, sn, z], [-sn, cn, z]
        e1 = self.r.vscale(et, rho)
        e2 = self.r.vadd(self.r.vscale(et, q["rhop"]), self.r.vscale(er, -(rho**2)))
        gamma = self.r.vadd(self.r.vscale(nr, q["support"]), self.r.vscale(nt, q["supportp"]))
        gamma1 = self.r.vscale(nt, rho)
        gamma2 = self.r.vadd(self.r.vscale(nt, q["rhop"]), self.r.vscale(nr, -rho))
        return dict(phi=phi, theta=q["theta"], rho=rho, rho_phi=q["rhop"],
            e=[er, e1, e2], et=et, Gamma=[gamma, gamma1, gamma2],
            boundary_Tphi_norm_upper=self.r.norm_upper(e1),
            boundary_Tphiphi_norm_upper=self.r.norm_upper(e2))

    def inverse_at(self, value):
        self.budget.check()
        target = self.series(self.fixed_core, self.point(value))["theta"]
        trial = self.point(value)
        residual = self.series(self.core, trial)["theta"]-target
        lower, upper = self.current_rho["lower"], self.current_rho["upper"]
        root = trial-residual/self.I(lower, upper, self.bits)
        for _ in range(self.inverse_steps):
            self.budget.check()
            if root.hi-root.lo <= self.inverse_width:
                break
            centre = self.point((root.lo+root.hi)/2)
            q = self.series(self.core, root)
            derivative = q["rho"].intersect(self.I(lower, upper, self.bits))
            at_centre = self.series(self.core, centre)["theta"]-target
            refined = root.intersect(centre-at_centre/derivative)
            if refined.lo == root.lo and refined.hi == root.hi:
                break
            root = refined
        self.counts["accurate_core_inverse_calls"] += 1
        return root

    def core_and_cap(self, phi):
        fixed = self.fixed_chart(phi)
        if self.core == self.fixed_core:
            psi, gamma = phi, fixed["Gamma"]
        else:
            lower, upper = self.inverse_at(phi.lo), self.inverse_at(phi.hi)
            psi = self.I(lower.lo, upper.hi, self.bits)
            q = self.series(self.core, psi)
            rho = q["rho"].intersect(self.I(self.current_rho["lower"], self.current_rho["upper"], self.bits))
            sine, cosine = self.trig(psi)
            z = self.point(0)
            er, et = [cosine, sine, z], [-sine, cosine, z]
            gamma = [self.r.vadd(self.r.vscale(er, q["support"]), self.r.vscale(et, q["supportp"])),
                self.r.vscale(et, fixed["rho"]),
                self.r.vadd(self.r.vscale(et, fixed["rho_phi"]),
                    self.r.vscale(er, -(fixed["rho"]**2)/rho))]
        cap = [self.r.vscale(v, self.R) for v in fixed["e"]]
        cap[0][2] = cap[0][2]+self.H
        refcap = [self.r.vscale(v, self.R) for v in fixed["e"]]
        refcap[0][2] = refcap[0][2]+self.H0
        if self.core == self.fixed_core:
            difference = [[self.point(0) for _ in range(3)] for _ in range(3)]
        else:
            difference = [[gamma[j][a]-fixed["Gamma"][j][a] for a in range(3)] for j in range(3)]
        # Cap horizontal/angular terms are exactly the same functions, not two
        # independent interval copies. Only the literal free-height difference remains.
        difference[0][2] = difference[0][2]-(self.H-self.H0)
        return dict(core=gamma, cap=cap, reference_core=fixed["Gamma"], reference_cap=refcap,
            centered_endpoint_difference=difference, rho0=fixed["rho"],
            fixed_chart=fixed, accurate_current_normal_angle=psi,
            accurate_global_current_rho_proof=self.current_rho)

    def region(self, point):
        for i, ((a, b), (ca, cb)) in enumerate(zip(self.support, self.central)):
            if self.compare((a, F(0)), point) < 0 and self.compare(point, (b, F(0))) < 0:
                if self.compare(point, (ca, F(0))) < 0:
                    return "boundary_left", i
                if self.compare((cb, F(0)), point) < 0:
                    return "boundary_right", i
                return "central", i
        return "outside", None

    def make_plan(self):
        cuts = set(tuple(v) for v in self.context.nodes)
        for support, central in zip(self.support, self.central):
            cuts.update((v, F(0)) for v in support+central)
            ca, cb = central
            for quarter in range(4):
                a, b = F(quarter, 4), F(quarter+1, 4)
                for t in (a, a+self.profile_delta, b-self.profile_delta, b):
                    cuts.add((ca+(cb-ca)*t, F(0)))
        for triple in (*self.bubble, self.gamma):
            cuts.update((q, F(0)) for q in triple)
        ordered = sorted(cuts, key=cmp_to_key(self.compare))
        if ordered[0] != (F(0), F(0)) or ordered[-1] != (F(1), F(0)):
            raise ValueError("The complete accurate radial domain changed")
        result, cell = [], 0
        nodes = self.context.nodes
        for index, (left, right) in enumerate(zip(ordered, ordered[1:])):
            if self.compare(left, right) >= 0:
                raise ValueError("Every complete radial leaf needs positive width")
            while cell+1 < len(nodes)-1 and self.compare(left, nodes[cell+1]) >= 0:
                cell += 1
            if self.compare(nodes[cell], left) > 0 or self.compare(right, nodes[cell+1]) > 0:
                raise ValueError("The full exact radial piece crosses an original quintic cell")
            kind, support = self.region(midpoint(left, right))
            result.append(dict(id="r"+str(index), left=list(left), right=list(right),
                original_cell=cell, kind=kind, support_index=support, depth=0))
        return result

    def children(self, leaf):
        left, right = affine(leaf["left"]), affine(leaf["right"])
        middle = midpoint(left, right)
        return [dict(leaf, id=leaf["id"]+"/"+str(i), left=list(a), right=list(b),
            depth=leaf["depth"]+1) for i, (a, b) in enumerate(((left, middle), (middle, right)))]

    def _s5(self, t):
        t = t.intersect(self.I(0, 1, self.bits))
        value = lambda u: u**3*(10-15*u+6*u*u)
        v = self.I(value(t.lo), value(t.hi), self.bits).intersect(self.I(0, 1, self.bits))
        derivative = (30*(t**2)*((1-t)**2)).intersect(self.I(0, F(15, 8), self.bits))
        return v, derivative

    def cutoff(self, leaf):
        left, right = affine(leaf["left"]), affine(leaf["right"])
        i = leaf["support_index"]
        relative = self.relative(left, right)
        if leaf["kind"] == "boundary_left":
            t, sign = (relative-self.support[i][0])/self.delta, 1
        elif leaf["kind"] == "boundary_right":
            t, sign = (self.support[i][1]-relative)/self.delta, -1
        else:
            raise ValueError("Only a complete boundary piece has a normalization cutoff")
        value, dt = self._s5(t)
        return value, sign*dt/(self.delta*self.S)

    def original_reference(self, leaf, fixed):
        boxes, pieces = self.scalar.enclose(affine(leaf["left"]), affine(leaf["right"]))
        self.counts["whole_scalar_calls"] += 1
        b, c, bs, cs = [self.from_deep(v) for v in boxes]
        b = b.intersect(self.I(-1, 1, self.bits))
        c = c.intersect(self.I(0, 1, self.bits))
        e0, e1, e2 = fixed["e"]
        z = self.point(0)
        T = self.r.vadd(self.r.vscale(e0, b), [z, z, c])
        Ts = self.r.vadd(self.r.vscale(e0, bs), [z, z, cs])
        return dict(jets=[T, self.r.vscale(e1, b), self.r.vscale(e2, b)],
            Ts=Ts, whole_scalar_piece_descriptions=pieces,
            accurate_scalar_jets=dict(b=b,c=c,bs=bs,cs=cs))

    def reference_piece(self, leaf, fixed, mean):
        self.counts["whole_seed_piece_calls"] += 1
        original = self.original_reference(leaf, fixed)
        kind = leaf["kind"]
        if kind == "outside":
            return dict(jets=original["jets"], Ts=original["Ts"],
                accurate_scalar_jets=original["accurate_scalar_jets"])
        fields = mean["intervals"]
        d = [fields[k] for k in ("d", "d_phi", "d_phiphi")]
        w = [fields[k] for k in ("w", "w_phi", "w_phiphi")]
        d, w = self.from_seed(d), self.from_seed(w)
        if kind.startswith("boundary"):
            chi, chis = self.cutoff(leaf)
            Y = [self.r.vadd(self.r.vscale(original["jets"][j], 1-chi),
                            self.r.vscale(d[j], chi)) for j in range(3)]
            Ys = self.r.vadd(self.r.vscale(original["Ts"], 1-chi),
                self.r.vscale(self.r.vadd(d[0], self.r.vscale(original["jets"][0], -1)), chis))
            nu = self.k.cap_floor(mean["accurate_root_vertical_lower"], self.bits)
            jets, norms = self.k.normalized_jets(*self.to_seed(Y), norm_lower=nu, norm_upper=1)
            jets, radius = self.from_seed(jets), self.from_seed(norms[0])
            Ts = self.r.vadd(self.r.vscale(Ys, 1/radius),
                self.r.vscale(Y[0], -self.r.dot(Y[0], Ys)/(radius**3)))
            return dict(jets=jets, Ts=Ts,
                accurate_scalar_jets=original["accurate_scalar_jets"])
        if kind != "central":
            raise ValueError("Unknown complete supported-reference radial piece")
        ca, cb = self.central[leaf["support_index"]]
        t = ((self.relative(leaf["left"], leaf["right"])-ca)/(cb-ca)).intersect(self.I(0, 1, self.bits))
        profile = self.k.central_profile_enclosures(self.to_seed(t), self.profile_delta,
            self.to_seed(self.S*(cb-ca)))
        h, hs = self.from_seed(profile["h"]), self.from_seed(profile["h_s"])
        l0, l1, l2 = [self.from_seed(fields[k]) for k in ("lambda", "lambda_phi", "lambda_phiphi")]
        alpha, alpha1, alpha2, alphas = h*l0, h*l1, h*l2, hs*l0
        sine, cosine = self.trig(alpha)
        value = self.r.vadd(self.r.vscale(d[0], cosine), self.r.vscale(w[0], sine))
        tangent = self.r.vadd(self.r.vscale(d[0], -sine), self.r.vscale(w[0], cosine))
        first = self.r.vadd(self.r.vadd(self.r.vscale(d[1], cosine), self.r.vscale(w[1], sine)),
                           self.r.vscale(tangent, alpha1))
        second = self.r.vadd(self.r.vadd(self.r.vscale(d[2], cosine), self.r.vscale(w[2], sine)),
            self.r.vscale(self.r.vadd(self.r.vscale(d[1], -sine), self.r.vscale(w[1], cosine)), 2*alpha1))
        second = self.r.vadd(self.r.vadd(second, self.r.vscale(tangent, alpha2)),
                             self.r.vscale(value, -(alpha1**2)))
        return dict(jets=[value, first, second], Ts=self.r.vscale(tangent, alphas),
            accurate_scalar_jets=original["accurate_scalar_jets"])

    def omega_piece(self, leaf, phi):
        self.counts["exact_omega_piece_calls"] += 1
        cell = leaf["original_cell"]
        origin = self.context.nodes[cell]
        width = self.width(origin, self.context.nodes[cell+1])
        a = self.from_deep(self.scalar.exact_affine_box(tuple(q-p for p,q in zip(origin,affine(leaf["left"])))))
        b = self.from_deep(self.scalar.exact_affine_box(tuple(q-p for p,q in zip(origin,affine(leaf["right"])))))
        low, high = (a/width).lo, (b/width).hi
        low, high = max(F(0), low), min(F(1), high)
        if low > high:
            raise ValueError("The accurate subcell has an inconsistent original-cell address")
        _, polynomials = self.omega.prepare_cell(cell)
        jets = [[self.point(0) for _ in range(3)] for _ in range(3)]
        radial = [self.point(0) for _ in range(3)]
        for mode, polynomial in enumerate(polynomials):
            if polynomial is None:
                continue
            channel, nu = self.omega.channels[mode], self.omega.frequencies[mode]
            value = self.from_deep(self.omega.restricted_range(polynomial[0], low, high))
            derivative = self.from_deep(self.omega.restricted_range(polynomial[1], low, high))
            sine, cosine = self.trig(phi*nu)
            angular = ([cosine, -nu*sine, -(nu*nu)*cosine] if channel == 1
                       else [sine, nu*cosine, -(nu*nu)*sine])
            for j in range(3):
                jets[j][channel] = jets[j][channel]+value*angular[j]
            radial[channel] = radial[channel]+derivative*angular[0]
        return jets, radial

    def bubble_piece(self, leaf, triple):
        left, right = affine(leaf["left"]), affine(leaf["right"])
        a, m, b = triple
        zero = self.point(0)
        if self.compare(right, (a,F(0))) <= 0 or self.compare((b,F(0)), left) <= 0:
            return zero, zero
        relative = self.relative(left, right)
        if self.compare(right, (m,F(0))) <= 0:
            if self.compare(left, (a,F(0))) < 0:
                raise ValueError("The exact integration partition must split every control support endpoint")
            value, derivative = self._s5((relative-a)/(m-a))
            return value, derivative/((m-a)*self.S)
        if self.compare((m,F(0)), left) <= 0:
            if self.compare((b,F(0)), right) < 0:
                raise ValueError("The exact integration partition must split every control support endpoint")
            value, derivative = self._s5((relative-m)/(b-m))
            return 1-value, -derivative/((b-m)*self.S)
        raise ValueError("Split at the exact original bubble peak; do not select a branch by rounding")

    def control_piece(self, leaf, fixed):
        self.counts["exact_control_piece_calls"] += 1
        zero, one = self.point(0), self.point(1)
        er, et = fixed["e"][0], fixed["et"]
        rotation = [[er[i], et[i], [zero,zero,one][i]] for i in range(3)]
        matrices = [self.r.matrix_product(self.r.matrix_product(rotation, Q),
                    self.r.transpose(rotation)) for Q in self.Q0]
        values = [self.bubble_piece(leaf, t) for t in self.bubble]
        old = [[sum((values[k][0]*matrices[k][i][j] for k in range(2)), zero)
                for j in range(3)] for i in range(3)]
        old_s = [[sum((values[k][1]*matrices[k][i][j] for k in range(2)), zero)
                  for j in range(3)] for i in range(3)]
        Z = [[zero,-one,zero],[one,zero,zero],[zero,zero,zero]]
        def commutator(matrix):
            left, right = self.r.matrix_product(Z,matrix), self.r.matrix_product(matrix,Z)
            return [[left[i][j]-right[i][j] for j in range(3)] for i in range(3)]
        C, C2 = commutator(old), None
        C2 = commutator(C)
        p = [[fixed["rho"]*C[i][j] for j in range(3)] for i in range(3)]
        pp = [[fixed["rho_phi"]*C[i][j]+fixed["rho"]**2*C2[i][j]
               for j in range(3)] for i in range(3)]
        gamma, gamma_s = self.bubble_piece(leaf,self.gamma)
        W = [[[self.S*matrix[i][j] for j in range(3)]
            +[(gamma if i==j else zero) if order==0 else zero for j in range(3)]
            for i in range(3)] for order,matrix in enumerate((old,p,pp))]
        Ws = [[self.S*old_s[i][j] for j in range(3)]
            +[gamma_s if i==j else zero for j in range(3)] for i in range(3)]
        return W, Ws

    def lift_piece(self, leaf):
        x = self.relative(leaf["left"],leaf["right"]).intersect(self.I(0,1,self.bits))
        value, derivative = self._s5(x)
        h = 1-value
        hp = -derivative/self.S
        hpp = -60*x*(1-x)*(1-2*x)/(self.S**2)
        return h, hp, hpp

    def metadata(self):
        return encode(dict(schema=SCHEMA,source_sha256=sha(__file__),identity=self.identity,
            actual_input_identity=self.actual.identity, precision_bits=self.bits,
            accurate_S=self.S,accurate_R=self.R,current_H=str(self.H),frozen_H=str(self.H0),
            fixed_rho_proof=self.fixed_rho,current_rho_proof=self.current_rho,
            complete_exact_radial_plan=self.plan,actual_counts=self.counts,
            unit_reference_provenance=self.unit_reference_provenance,
            posterior_mean=self.posterior_mean.metadata(),
            no_working_field_or_root_or_J_evaluations=True,
            continuous_normal_branch_or_geometry_certified=False))


def reference_mean_adapter(geometry, phi, actual_anchor):
    """New whole-angle binding around unchanged complete radial mean formulas.

    The parent constructor is deliberately not invoked: it binds one literal API
    actual batch/literal angle. This adapter first binds the genuine full fixed Fejer
    input, then reuses only the source-pinned complete mathematical methods on
    an independently produced whole angular box.
    """
    require_actions()
    g, parent, k = geometry, geometry.mean_module.ActualMeanBatch, geometry.k
    if actual_anchor not in g.actual.seed_rows:
        raise ValueError("An accurate whole-angle comparison needs an actual recorded reference candidate")
    working = g.actual.seed_rows[actual_anchor]
    fixed = g.fixed_chart(phi)

    class WholeMean(parent):
        def __init__(self):
            self.repo, self.context, self.seed = g.actual.repo, g.context, g.actual.seed
            self.k, self.I, self.bits = k, k.Interval, g.bits
            self.scalar, self.d = g.scalar, g.d
            self.S, self.R, self.H = g.to_seed(g.S), g.to_seed(g.R), g.H0
            self.core, self.support, self.central = g.fixed_core, g.support, g.central
            self.delta, self.beta, self.Lc = g.delta, g.beta, g.to_seed(g.Lc)
            chart = g.to_seed(fixed)
            chart["literal_phi_hex"] = actual_anchor
            self.angles = [chart]
            v = [k.point_vector(working[key]) for key in ("v","v_phi","v_phiphi")]
            lo, hi = k.point_norm(v[0],g.bits)
            if lo <= 0 or v[0][2] <= 0:
                raise EnclosureUnavailable("The actual candidate does not resolve its positive normalization chart")
            intervals = [[self.I(q,q,g.bits) for q in part] for part in v]
            direction, radius = k.normalized_jets(*intervals,norm_lower=lo,norm_upper=hi)
            zeta = v[0][2]/hi
            self.candidates = [dict(v=intervals,d=direction,radius=radius,
                direction_vertical_lower=zeta,boundary_normalization_lower=k.cap_floor(zeta,g.bits))]
            self.plan = self.make_plan()
            self.counts = dict(scalar_whole_interval_calls=0,complete_leaf_enclosures=0,
                complete_boundary_leaf_enclosures=0,complete_complement_leaf_enclosures=0,
                literal_angle_count=1)
    return WholeMean(), working


def enclose_reference_mean(geometry, phi, actual_anchor, *, maximum_splits,
                           width_goal, taylor_order=64, profile_series_order=64):
    require_actions()
    g, k = geometry, geometry.k
    if type(maximum_splits) is not int or maximum_splits < 0 or F(width_goal) <= 0:
        raise ValueError("Use explicit complete reference integral refinement budgets")
    adapter, working = reference_mean_adapter(g,phi,actual_anchor)
    leaves = {}
    def evaluate(description):
        g.budget.check(leaves=1)
        return adapter.leaf(description)
    for description in adapter.plan:
        if description["kind"] != "central":
            leaves[description["id"]] = evaluate(description)
    def total():
        complement = [[F(0),F(0)] for _ in range(2)]
        boundary = [[[[F(0),F(0)] for _ in range(3)] for _ in range(3)]]
        for leaf in leaves.values():
            values = adapter.decode_integral(leaf)
            if leaf["contribution"] == "complement_scalar_b_c":
                for a, value in enumerate(values):
                    complement[a][0] += value.lo
                    complement[a][1] += value.hi
            else:
                for j in range(3):
                    for a in range(3):
                        boundary[0][j][a][0] += values[0][j][a].lo
                        boundary[0][j][a][1] += values[0][j][a].hi
        return adapter.assemble_sums(complement,boundary)
    result = total()
    splits = 0
    while F(result["maximum_total_equation_component_L1_width"]) > F(width_goal) and splits < maximum_splits:
        g.budget.check()
        key = max(leaves, key=lambda name: adapter.leaf_score(leaves[name]))
        parent_leaf = leaves[key]
        children = adapter.children(parent_leaf["description"])
        evaluated = [evaluate(child) for child in children]
        del leaves[key]
        leaves.update({child["description"]["id"]:child for child in evaluated})
        splits += 1
        result = total()
    row = result["angles"][0]
    try:
        mean = g.posterior_mean.mean_jet_bounds(g,working,result,adapter.plan,
            list(leaves.values()),encode(phi),bits=g.bits,
            taylor_order=taylor_order,profile_series_order=profile_series_order)
    except g.posterior_mean_module.PosteriorDomainUnavailable as error:
        raise EnclosureUnavailable(str(error)) from error
    except ValueError as error:
        if str(error) in (
                "Actual R711 amplitude candidate is not proved inside (0,pi)",
                "Current outward data cannot resolve the positive full-profile derivative"):
            raise EnclosureUnavailable(str(error)) from error
        raise
    g.counts["complete_reference_means"] += 1
    evidence = dict(schema="same-actual-reference-whole-angle-R722-posterior-mean-enclosure-v1",
        actual_input_identity=g.actual.identity, geometry_identity=g.identity,
        complete_actual_mean_candidate=g.actual.seed_row_sources[working["actual_completed_batch_index"]],
        candidate_literal_phi_hex=actual_anchor, accurate_phi_interval=phi,
        exact_partition=adapter.plan, complete_active_leaves=list(leaves.values()),
        all_original_mean_radial_pieces_included=True, exact_central_Lc_v_used=True,
        complete_accurate_total_equation=result, actual_splits=splits,
        width_goal=str(F(width_goal)),
        width_goal_met=F(result["maximum_total_equation_component_L1_width"]) <= F(width_goal),
        sufficient_R709_inequalities_verified_on_this_whole_interval=row[
            "all_pointwise_R709_sufficient_inequalities_proved"],
        posterior_R722_existence_verified_on_this_whole_interval=True,
        complete_posterior_mean_root_domain=mean["root_domain_attribution"],
        structural_boundary_unit_proof=g.unit_reference_provenance,
        complete_pointwise_theorem_source_sha256=POSTERIOR_MEAN_SHA,
        complete_shared_R710_R711_math_source_sha256=SEED_MATH_SHA,
        complete_R722_theorem_sha256=g.posterior_mean_module.THEOREM_SHA256,
        whole_interval_bounds_computed_here=True,
        original_literal_only_consumer_did_not_certify_this_whole_interval=True,
        normal_roots_or_whole_surface_certified=False)
    return mean, evidence


class AccurateAngleOracle:
    """Complete radial integral of true f and every control-frame angular jet."""

    def __init__(self, geometry, phi, actual_anchor, *, radial_depth=0,
                 mean_maximum_splits=8192, mean_width_goal="1/1000000000000",
                 first_exp_degree=24, maximum_exp_degree=128):
        require_actions()
        self.g, self.r, self.bits = geometry, geometry.r, geometry.bits
        if not isinstance(phi,self.r.Interval) or phi.bits != self.bits:
            raise ValueError("Use an exact complete angular interval")
        if type(radial_depth) is not int or not 0 <= radial_depth <= 20:
            raise ValueError("Use an explicit complete dyadic radial refinement depth")
        self.phi, self.anchor = phi, actual_anchor
        self.endpoints = geometry.core_and_cap(phi)
        self.mean, self.mean_evidence = enclose_reference_mean(geometry,phi,actual_anchor,
            maximum_splits=mean_maximum_splits,width_goal=mean_width_goal)
        self.rotations = self.r.ExactRotationJets(bits=self.bits,
            first_degree=first_exp_degree,maximum_degree=maximum_exp_degree)
        self.leaves = [dict(v) for v in geometry.plan]
        for _ in range(radial_depth):
            self.leaves = [child for leaf in self.leaves for child in geometry.children(leaf)]
        self.inputs, self.evaluations = {}, {}
        self.calls = 0
        self.zero_controls = [[geometry.point(0) for _ in range(6)] for _ in range(3)]
        self.zero_closure_jets = self.evaluate(self.zero_controls)["closure_jets"]

    def _input(self, leaf):
        key = leaf["id"]
        if key not in self.inputs:
            g = self.g
            seed = g.reference_piece(leaf,self.endpoints["fixed_chart"],self.mean)
            omega, omega_s = g.omega_piece(leaf,self.phi)
            W, Ws = g.control_piece(leaf,self.endpoints["fixed_chart"])
            self.inputs[key] = dict(seed=seed,omega=omega,omega_s=omega_s,W=W,Ws=Ws,
                exact_width=g.width(leaf["left"],leaf["right"]))
        return self.inputs[key]

    def corrected(self, leaf, controls, *, frame=True, radial=False):
        self.g.budget.check(leaves=1)
        data = self._input(leaf)
        result = self.rotations.corrected(data["seed"]["jets"],data["seed"]["Ts"],
            data["omega"],data["omega_s"],data["W"],data["Ws"],controls,
            complete_control_frame=frame,radial=radial)
        return result, data

    def evaluate(self, controls):
        self.g.budget.check()
        self.r.require_shape(controls,(3,6),self.bits)
        key = canonical(encode(controls))
        if key in self.evaluations:
            return self.evaluations[key]
        self.calls += 1
        zero = self.g.point(0)
        integral = [[zero for _ in range(3)] for _ in range(3)]
        difference = [[zero for _ in range(3)] for _ in range(3)]
        frame = [[[zero for _ in range(6)] for _ in range(3)] for _ in range(3)]
        symbolic_zero = [self.g.all_omega_zero and all(v.lo == 0 == v.hi
            for row in controls[:j+1] for v in row) for j in range(3)]
        for leaf in self.leaves:
            corrected, data = self.corrected(leaf,controls,frame=True,radial=False)
            width = data["exact_width"]
            for j,name in enumerate(("T","Tphi","Tphiphi")):
                for a in range(3):
                    integral[j][a] = integral[j][a]+width*corrected[name][a]
                    if not symbolic_zero[j]:
                        difference[j][a] = difference[j][a]+width*(corrected[name][a]-data["seed"]["jets"][j][a])
                    for l in range(6):
                        frame[j][a][l] = frame[j][a][l]+width*corrected["complete_control_frame"][j][a][l]
        closure = [[(self.endpoints["centered_endpoint_difference"][j][a]+difference[j][a])/self.g.S
                     for a in range(3)] for j in range(3)]
        frame = [[[v/self.g.S for v in row] for row in jet] for jet in frame]
        result = dict(closure_jets=closure,complete_control_frame=frame,
            total_integral=integral,accurate_centered_integral_difference=difference,
            whole_radial_domain=True,whole_phi_interval=self.phi,
            exact_zero_difference_orders=[j for j,paid in enumerate(symbolic_zero) if paid],
            symbolic_zero_is_exact_function_identity_not_working_residual_replacement=True,
            all_original_omega_cells_and_six_control_columns_retained=True)
        self.evaluations[key] = result
        return result

    def physical_cells(self, controls):
        """All complete radial leaves, with a valid moving partial-integral box."""
        total = self.evaluate(controls)["total_integral"]
        zero = self.g.point(0)
        prefix = [[zero for _ in range(3)] for _ in range(3)]
        # The exact current metric profile satisfies a_deep(S)=R and a_s=b.
        # These are full original-scalar integrals, not corrected-seed integrals.
        scalar_suffix = [zero for _ in range(len(self.leaves)+1)]
        for index in range(len(self.leaves)-1,-1,-1):
            data = self._input(self.leaves[index])
            scalar_suffix[index] = (scalar_suffix[index+1]
                +data["exact_width"]*data["seed"]["accurate_scalar_jets"]["b"])
        for index,leaf in enumerate(self.leaves):
            value,data = self.corrected(leaf,controls,frame=False,radial=True)
            width = data["exact_width"]
            partial = [[prefix[j][a]+self.r.Interval(0,width.hi,self.bits)*value[name][a]
                        for a in range(3)] for j,name in enumerate(("T","Tphi","Tphiphi"))]
            h,hp,hpp = self.g.lift_piece(leaf)
            fields = self.r.physical_sixjet_boxes(core=self.endpoints["core"],cap=self.endpoints["cap"],
                total_integral=total,partial_integral=partial,meridian=value,
                h=h,hp=hp,hpp=hpp,rho0=self.endpoints["rho0"],bits=self.bits)
            scalar = data["seed"]["accurate_scalar_jets"]
            a_deep = (self.g.R-scalar_suffix[index+1]
                -self.r.Interval(0,width.hi,self.bits)*scalar["b"])
            target = dict(a_deep=a_deep,**scalar,accurate_S=self.g.S,accurate_R=self.g.R,
                fixed_scalar_metric_identity_sha256=self.g.context.scalar_identity,
                enclosure_formula="a_deep(s)=R-integral_s^S b; complete exact-width whole-leaf suffix",
                full_same_scalar_infinite_tail_included=True,
                working_observation_or_quadrature_values_treated_as_exact=False)
            yield dict(exact_radial_leaf=leaf,accurate_phi_interval=self.phi,
                physical_sixjets=fields,accurate_fixed_scalar=target,
                all_same_field_radial_and_angular_chains_retained=True,
                original_working_physical_field_arrays_compared=False)
            for j,name in enumerate(("T","Tphi","Tphiphi")):
                for a in range(3):
                    prefix[j][a] = prefix[j][a]+width*value[name][a]

    def metadata(self):
        return encode(dict(schema="actual-fixed-fejer-accurate-R722-complete-normal-angle-oracle-v1",
            source_sha256=sha(__file__),actual_input_identity=self.g.actual.identity,
            geometry_identity=self.g.identity,accurate_phi_interval=self.phi,
            original_actual_candidate_angle=self.anchor,
            complete_radial_leaf_count=len(self.leaves),actual_integral_enclosures=self.calls,
            all_accurate_endpoint_integrals_and_frame_columns_computed_here=True,
            mean_evidence=self.mean_evidence,rotation_evidence=self.rotations.metadata(),
            numerical_mesh_and_gauss_carriers_not_used_as_exact_integrals=True,
            branch_gluing_or_working_field_word_errors_paid=False))
