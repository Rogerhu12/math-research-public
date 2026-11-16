#!/usr/bin/env python3
"""R580: a complete complex-angle strip and infinite Fourier/DFT-alias bound.

This optional observer consumes the SAME R553 record and original DFS
retirement through an actual R575 owner.  It evaluates no new field, target,
root, trigonometric grid, FFT, or BVP.  Strict real joint positivity gives a
constructive rational strip; no adaptive scientific gate is introduced.
All bound arithmetic belongs only to the named public Actions.
Author: ChatGPT (AI, amplitude agent), 2026-11-16.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R580-same-evaluation-analytic-angle-projection-v1"
REFERENCE_NAME = "geometry_20261116_same_evaluation_full_angle_projection_defect.py"
REFERENCE_SHA = "d2cfc1e35509486dd77f5f2ae4aecba3c0527b2e16b910be69540a73f3c2d6b7"
REFERENCE_SCHEMA = "R575-same-evaluation-complete-angle-projection-defect-v1"
PHYSICAL_LAYOUT = "r0..rM,t1..tM,z0..zM"
MATH_ERRORS = (ArithmeticError, ValueError, TypeError, KeyError, IndexError)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Evaluate this observer only in the named public Actions")


def exact(value):
    if isinstance(value, (bool, float)):
        raise TypeError("Use exact rational lifts, not bool or float")
    if isinstance(value, (Q, int, str)):
        return Q(value)
    raise TypeError("Expected Fraction, integer, or an exact rational string")


def encoded(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: encoded(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encoded(item) for item in value]
    return value


def canonical(value):
    return (json.dumps(encoded(value), sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def value_identity(value):
    raw = canonical(value)
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def source_identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def reference_grid(m, n):
    require(type(m) is int and m >= 1, "Use the actual positive integer M")
    require(type(n) is int and n % 2 == 0 and n >= 4*m+4,
            "Use the original even N with every retained bin below Nyquist")


def relative_dyadic_bounds(value, bits):
    """Positive relative enclosure by integer division, with no underflow."""
    x = exact(value)
    require(x >= 0 and type(bits) is int and bits >= 1,
            "Nonnegative bound and a positive integer enclosure precision")
    if x == 0:
        return Q(0), Q(0)
    def two(exponent):
        return Q(1 << exponent) if exponent >= 0 else Q(1,1 << -exponent)
    exponent = x.numerator.bit_length()-x.denominator.bit_length()
    if x < two(exponent):
        exponent -= 1
    scale = two(exponent-bits)
    ratio = x/scale
    mantissa = ratio.numerator//ratio.denominator
    lower = mantissa*scale
    upper = lower if lower == x else (mantissa+1)*scale
    # 2^bits <= mantissa: a positive exact input has a positive lower
    # endpoint, regardless of its exponent.  No machine float is used.
    return lower, upper



def exponential_upper(value, bits, terms, work):
    """Outward exp(x) from a complete positive Taylor-tail bound and squaring."""
    x = exact(value)
    require(x >= 0 and type(terms) is int and terms >= 1,
            "Nonnegative argument and positive finite upper-sum term count")
    if x == 0:
        return Q(1)
    reduced, squarings = x, 0
    while reduced > Q(1,2):
        work("positive_exp_range_reduction",squarings=squarings)
        reduced /= 2
        squarings += 1
    term, total = Q(1), Q(1)
    for k in range(1,terms+1):
        work("complete_positive_exp_upper_sum",term_index=k)
        term = term*reduced/k
        total += term
    # Every omitted ratio is <= reduced/(L+2)<1; all omitted terms
    # are covered by this infinite geometric upper sum.
    next_term = term*reduced/(terms+1)
    tail = next_term/(1-reduced/(terms+2))
    upper = relative_dyadic_bounds(total+tail,bits)[1]
    for k in range(squarings):
        work("outward_positive_exp_squaring",squaring=k,total=squarings)
        upper = relative_dyadic_bounds(upper*upper,bits)[1]
    return upper

def power_sum_bounds(r_interval, exponent, bits, work):
    """Outward bounds for r^n and sum_{j=0}^{n-1}r^j, every term retained.

    Concatenation uses P[a+b]=P[a]*P[b], S[a+b]=S[a]+P[a]*S[b].
    This avoids giant exact rational r^N and avoids subtracting rounded
    powers from one.  Bounds are for one fixed exact r in the input interval.
    """
    require(type(exponent) is int and exponent >= 0, "Nonnegative integer exponent")
    lo, hi = r_interval
    require(Q(0) < lo <= hi <= Q(1), "A positive interval containing exact r<1")
    def down(value):
        return relative_dyadic_bounds(value,bits)[0]
    def up(value):
        return relative_dyadic_bounds(value,bits)[1]
    def merge(left, right):
        n, pl, pu, sl, su = left
        k, ql, qu, tl, tu = right
        length = n+k
        # All products use the ORIGINAL left/right bounds in this expression.
        new_pl = down(pl*ql)
        new_pu = min(Q(1),up(pu*qu))
        new_sl = down(sl+pl*tl)
        new_su = up(su+pu*tu)
        if length:
            new_sl = max(Q(1),new_sl)
            new_su = min(Q(length),new_su)
        return length,new_pl,new_pu,new_sl,new_su
    answer = (0,Q(1),Q(1),Q(0),Q(0))
    block = (1,lo,hi,Q(1),Q(1))
    remaining = exponent
    while remaining:
        work("complete_positive_power_sum",exponent=exponent,remaining=remaining)
        if remaining & 1:
            answer = merge(answer,block)
        remaining //= 2
        if remaining:
            block = merge(block,block)
    n, pl, pu, sl, su = answer
    return dict(exponent=n,power=[pl,pu],complete_geometric_sum=[sl,su])


def conditional_exponential_projection_bound(strip_half_width, vector_sup,
        field_modes, angular_count, *, exponential_terms, enclosure_bits, budget_check):
    """Conditional exact-reference bound; supplied words do not prove a strip.

    Assumptions: the same rotating C^3-valued vector is holomorphic on the
    full |Im(phi)|<=h strip, bounded by C there, pi-periodic and real with
    parity (even,odd,even) on the real circle. sigma is fixed. This function
    certifies no floating FFT, table/profile/root formation or actual coverage.
    Relative dyadic rounding is directed BOUND formation, never solver data.
    """
    actions()
    reference_grid(field_modes,angular_count)
    h, upper = exact(strip_half_width),exact(vector_sup)
    require(h > 0 and upper >= 0,"A positive strip and nonnegative full-vector bound")
    require(type(exponential_terms) is int and exponential_terms >= 1,
            "A positive finite Taylor term count, including all terms 0..L")
    require(type(enclosure_bits) is int and enclosure_bits >= 1,
            "A positive integer bound-enclosure precision")
    require(callable(budget_check),"Use the actual original budget callback")
    def work(phase,**position):
        budget_check()
    x,term,total = 2*h,Q(1),Q(1)
    for k in range(1,exponential_terms+1):
        work("positive_exponential_lower_sum",term_index=k)
        term = term*x/k
        total += term
    # exp(2h)>=S_L>1, hence r=1/S_L>=exp(-2h), strictly r<1.
    # No omitted positive exponential remainder is relabelled zero.
    r = Q(1)/total
    require(Q(0) < r < Q(1),"Exact reciprocal positive sum is below one")
    r_lo,r_hi = relative_dyadic_bounds(r,enclosure_bits)
    r_hi = min(Q(1),r_hi)
    gap_lo,gap_hi = relative_dyadic_bounds(1-r,enclosure_bits)
    require(gap_lo > 0,"Relative rounding retains the exact positive gap")
    # r_hi may equal one. The independently enclosed positive gap is used;
    # it is never silently replaced by 1-r_hi or rejected as a new domain gate.
    m,half_n = field_modes,angular_count//2
    powers = {}
    for exponent in (m+1,half_n-m,2*m+1,half_n):
        if exponent not in powers:
            powers[exponent] = power_sum_bounds((r_lo,r_hi),exponent,enclosure_bits,work)
    work("complete_infinite_geometric_sums")
    tail_raw = 2*upper*powers[m+1]["power"][1]/gap_lo
    alias_raw = (2*upper*powers[half_n-m]["power"][1]
        *powers[2*m+1]["complete_geometric_sum"][1]
        /(gap_lo*powers[half_n]["complete_geometric_sum"][0]))
    tail = relative_dyadic_bounds(tail_raw,enclosure_bits)[1]
    alias = relative_dyadic_bounds(alias_raw,enclosure_bits)[1]
    alias_used = min(alias,tail)
    defect = relative_dyadic_bounds(tail+alias_used,enclosure_bits)[1]
    signed = []
    for j in range(-m,m+1):
        work("retained_signed_bin_metadata",mode=j)
        signed.append(2*j)
    return encoded(dict(schema=SCHEMA+"-conditional-uniform-bound",
        field_modes=m,angular_count=angular_count,physical_size=3*m+2,
        physical_layout=PHYSICAL_LAYOUT,
        physical_angle_coordinate="phi, not q=phi/(2*pi) and not material angle",
        component_frame="rotating cylindrical components",
        vector_norm="Hermitian Euclidean norm of all three complex components",
        strip_half_width=h,complete_strip_vector_sup=upper,
        actual_complete_strip_and_fixed_branch_are_required_not_inferred_from_words=True,
        exact_coefficient_formula="||v_hat[k]|| <= C*exp(-abs(k)*h)",
        component_period="pi (also 2*pi)",component_parity=["even","odd","even"],
        retained_signed_frequencies=signed,retained_frequency_count=2*m+1,
        reference_grid=dict(count=angular_count,first_index=0,
            last_index=angular_count-1,formula="phi_l=2*pi*l/N",
            repeated_endpoint_included=False,Nyquist_index=half_n,
            largest_retained_index=2*m,retained_Nyquist=False),
        rational_exponential_majorant=dict(
            L=exponential_terms,all_indices_included=[0,exponential_terms],
            exact_r_definition="r=1/sum_{k=0}^L (2h)^k/k!",
            direction="exp(-2h) <= r < 1",
            exact_sum_is_defined_by_the_returned_h_and_L_not_an_unreturned_input=True,
            r_enclosure=[r_lo,r_hi],positive_one_minus_r_enclosure=[gap_lo,gap_hi],
            enclosure_bits=enclosure_bits,
            complete_power_sum_enclosures=[powers[k] for k in sorted(powers)],
            no_transcendental_rounding_or_unbounded_remainder_omitted=True,
            finite_enclosure_precision_may_widen_but_never_discard_terms=True),
        exact_tail_formula="2*C*r^(M+1)/(1-r)",
        exact_complete_alias_formula="2*C*r^(N/2-M)*S_(2M+1)(r)/((1-r)*S_(N/2)(r)), S_n=sum_(j=0)^(n-1) r^j",
        continuous_Fourier_tail_upper=tail,
        all_retained_alias_sum_upper=alias,
        alternative_alias_upper_from_disjoint_omitted_bins=tail,
        alias_upper_used=alias_used,
        uniform_reconstructed_projection_defect_upper=defect,
        returned_bounds_include_all_directed_enclosure_rounding=True,
        complete_infinite_even_tail_and_all_integer_aliases_included=True,
        both_R_and_Z_means_retained=True,
        T_mean_zero_only_by_the_stated_real_parity=True,
        extra_factor_three_not_applied_to_the_full_vector_norm=True,
        actual_FFT_trig_profile_root_and_RHS_formation_bound=False,
        actual_solver_residual_or_relative_metric_floor_bound=False,
        fixed_grid_parity_projection_not_claimed_to_commute_with_arbitrary_phase=True))


class BoundAnalyticProjection:
    """One actual R575/R553 context; no B2 availability or acceptance prerequisite."""

    def __init__(self, projection_observer, *, strip_width_cap, exponential_terms):
        actions()
        module = sys.modules.get(type(projection_observer).__module__)
        require(module is not None and getattr(module, "__file__", None) is not None,
                "The actual R575 defining module is unavailable")
        row = source_identity(module.__file__)
        require(Path(row["file"]).parent == HERE
                and Path(row["file"]).name == REFERENCE_NAME
                and row["sha256"] == REFERENCE_SHA
                and module.SCHEMA == REFERENCE_SCHEMA
                and getattr(module, "BoundProjectionDefect", None) is type(projection_observer),
                "Bind the actual frozen R575 class owner, not a same-name view")
        self.reference, self.R = projection_observer, module
        self.tubes, self.T = projection_observer.tubes, projection_observer.T
        self.api = projection_observer.api
        self.field, self.current = projection_observer.field, projection_observer.current
        self.M, self.N = projection_observer.M, projection_observer.N
        self.sqrt_bits = projection_observer.sqrt_bits
        self.budget_check = projection_observer.budget_check
        reference_grid(self.M, self.N)
        require(self.tubes.field is self.field and self.tubes.current is self.current
                and self.tubes.api is self.api and self.tubes.M == self.M
                and self.tubes.N == self.N and self.field.saved.N == self.N,
                "The same actual field, target owner, coefficient tube and quadrature")
        # The actual R575 constructor has already bound the original R553
        # class, coefficient definition, full R521 and five DFT source files.
        # Check the real sqrt defining module too; no first-path class search.
        _, sqrt_source = module.actual_defining_module(self.api.sqrt_bounds,
            module.MAJORANT_NAME, module.MAJORANT_SHA)
        self.width_cap = exact(strip_width_cap)
        require(self.width_cap > 0, "An explicit positive rational strip width cap")
        require(type(exponential_terms) is int and exponential_terms >= 1,
                "Use an explicit positive exponential term count")
        self.exponential_terms = exponential_terms
        self.policy = dict(requested_strip_width_cap=self.width_cap,
            exponential_terms=exponential_terms, inherited_sqrt_bits=self.sqrt_bits,
            full_exponential_factor_method="range-reduced positive Taylor sum plus complete geometric tail and outward squaring",
            width_rule="min(cap,W_lower/(2*W1),P_lower/(2*P1)); omit a ratio only when its nonnegative slope is zero",
            relative_dyadic_enclosure_bits=self.sqrt_bits,
            no_adaptive_angular_grid_or_width_search=True)
        self.policy_identity = value_identity(self.policy)
        self.binding = dict(schema=SCHEMA+"-binding", source=source_identity(__file__),
            actual_R575_source=row, actual_R575_binding=projection_observer.describe(),
            actual_R521_sqrt_source=sqrt_source, bound_policy=self.policy,
            bound_policy_identity=self.policy_identity,
            field_modes=self.M, angular_count=self.N, physical_size=3*self.M+2,
            physical_layout=PHYSICAL_LAYOUT,
            same_actual_R553_return_and_original_retirement_required=True,
            R575_B2_availability_or_success_not_required=True,
            original_budget_callback_reused=True,
            no_new_clock_child_acceptance_or_cleanup_permission=True)
        self.observed = self.committed = self.split = self.terminal = 0
        self.paid = self.unpaid = 0
        self.min_width = self.min_W_gap = self.min_P_gap = None
        self.max_sup = Q(0)
        self.first_unpaid = self.last_unpaid = self.last_observed = None
        self.pending = None
        self.exp_factors = None
        self.exp_factors_identity = None

    def describe(self):
        return encoded(copy.deepcopy(self.binding))

    def work(self, phase, **position):
        if self.pending is not None:
            self.pending.update(phase=phase, position=position)
        self.budget_check()

    def finished(self, result):
        answer = encoded(result)
        self.pending = None
        return answer

    def sqrt(self, value):
        self.work("original_R521_rational_sqrt")
        return self.api.sqrt_bounds(value, self.sqrt_bits)

    def ensure_exp_factors(self):
        if self.exp_factors is None:
            values = []
            for j in range(1,self.M+1):
                def work(phase, **position):
                    self.work(phase, mode=j, frequency=2*j, **position)
                values.append(exponential_upper(2*j*self.width_cap,self.sqrt_bits,
                    self.exponential_terms,work))
            # Publish the cache only after every finite frequency completed.
            # It depends only on this object's fixed policy, M and precision.
            self.exp_factors = tuple(values)
            self.exp_factors_identity = value_identity(values)
        return self.exp_factors

    def strip_from_record(self, record):
        T, api, m = self.T, self.api, self.M
        tube, angular = record["coefficient_tube"], record["angular_box"]
        scalar, joint = record["scalar_box"], record["joint_invariants"]
        coefficients = tube["complete_coefficient_box"]
        require(len(coefficients) == 3*m+2, "All physical coefficients and both means")
        absolute = []
        for j, row in enumerate(coefficients):
            self.work("complete_coefficient_bounds", coefficient=j)
            absolute.append(T.absolute(T.pair(row)))
        # e_rot is NOT d_rot_phi. These are the actual cylindrical finite
        # polynomials, including the connection terms n^2+1 and 2*n.
        factors = self.ensure_exp_factors()
        d_slope, e_slope = [Q(0)]*3, [Q(0)]*3
        for j in range(1, m+1):
            self.work("complete_finite_strip_slopes", mode=j, frequency=2*j)
            n = 2*j
            r, t, z = absolute[j], absolute[m+j], absolute[2*m+1+j]
            u = (n*r+t, n*t+r, n*z)
            v = ((n*n+1)*r+2*n*t, (n*n+1)*t+2*n*r, n*n*z)
            for k in range(3):
                d_slope[k] += n*factors[j-1]*u[k]
                e_slope[k] += n*factors[j-1]*v[k]
        require(len(angular["d"]) == 3 and len(angular["e"]) == 3
                and len(joint["cross"]) == 3, "Complete real three-vector boxes")
        self.work("actual_real_vector_norms")
        D = api.norm_upper([T.absolute(T.pair(v)) for v in angular["d"]], self.sqrt_bits)
        E = api.norm_upper([T.absolute(T.pair(v)) for v in angular["e"]], self.sqrt_bits)
        C0 = api.norm_upper([T.absolute(T.pair(v)) for v in joint["cross"]], self.sqrt_bits)
        a, b = api.norm_upper(d_slope, self.sqrt_bits), api.norm_upper(e_slope, self.sqrt_bits)
        A, mu, nu = (T.pair(scalar[key]) for key in ("A", "mu", "nu"))
        q, W, P = (T.pair(joint[key]) for key in ("d_squared", "W", "P"))
        require(A[0] > 0 and mu[0] > 0 and W[0] > 0 and P[0] > 0
                and q[0] >= 0, "The original same-cell complete real positive domain")
        nu_abs = T.absolute(nu)
        h0 = self.width_cap
        self.work("constructive_positive_strip")
        C1 = D*b + E*a + a*b*h0
        Q1 = 2*D*a + a*a*h0
        W1 = 2*C0*C1 + C1*C1*h0
        q_cap = q[1]+h0*Q1
        P1 = A[1]*A[1]*mu[1]*mu[1]*W1 + nu_abs*nu_abs*Q1*(
            q_cap*q_cap + q_cap*q[1] + q[1]*q[1])
        w_cap = W[0]/(2*W1) if W1 > 0 else None
        p_cap = P[0]/(2*P1) if P1 > 0 else None
        caps = [h0]
        if w_cap is not None:
            caps.append(w_cap)
        if p_cap is not None:
            caps.append(p_cap)
        constructive_h = min(caps)
        h = relative_dyadic_bounds(constructive_h,self.sqrt_bits)[0]
        dd, de, dc, dq, dw, dp = (h*v for v in (a, b, C1, Q1, W1, P1))
        W_gap, P_gap = W[0]-dw, P[0]-dp
        require(h > 0 and W_gap > 0 and P_gap > 0,
                "Constructed exact positive denominator and right-half-plane margins")
        Dh, Eh, Ch, Qh = D+dd, E+de, C0+dc, q[1]+dq
        sqrt_P_upper = self.sqrt(P[1]+dp)[1]
        B_direct = (Qh+Dh*Dh)*Eh
        direct_sup = (nu_abs*Qh*B_direct+sqrt_P_upper*Ch)/(A[0]*W_gap)
        # Real-base comparison gives a second valid complex sup.  The identity
        # ||V(theta)||=mu is used ONLY at the real base, never at complex z.
        delta_dot = D*de+E*dd+dd*de
        B0_upper = self.sqrt(q[1]*W[1])[1]
        delta_B = dq*E+Qh*de+delta_dot*D+(D*E+delta_dot)*dd
        sqrt_denominator = self.sqrt(P_gap)[0]+self.sqrt(P[0])[0]
        delta_sqrt = dp/sqrt_denominator
        delta_numerator = (delta_sqrt*C0+sqrt_P_upper*dc
            +nu_abs*(dq*B0_upper+Qh*delta_B))
        near_real_sup = mu[1]+(delta_numerator+A[1]*dw*mu[1])/(A[0]*W_gap)
        exact_sup_candidate = min(direct_sup, near_real_sup)
        bound = relative_dyadic_bounds(exact_sup_candidate,self.sqrt_bits)[1]
        require(bound >= 0, "Nonnegative complete complex-vector sup")
        return dict(
            field_modes=m, angular_count=self.N,
            complete_coefficient_box_identity=value_identity(coefficients),
            complete_frequency_count=m, frequencies=[2*j for j in range(1,m+1)],
            full_coefficient_count=3*m+2, both_means_retained_in_real_base_and_state=True,
            scalar_box=dict(A=A, nu=nu, mu=mu,
                actual_same_target_return_identity=value_identity(scalar["actual_same_target_return"]),
                these_scalars_are_constant_in_physical_angle=True,
                rho_not_inserted_into_P_or_Frenet_velocity=True),
            actual_joint_box_identity=value_identity(joint),
            actual_real_bounds=dict(D=D,E=E,C0=C0,Q=q,W=W,P=P,nu_abs=nu_abs),
            complete_component_slopes=dict(d=d_slope,e=e_slope,a=a,b=b,
                inequality="||d(theta+iy)-d(theta)||<=a*|y|; similarly e with b, for |y|<=h0",
                finite_trig_bound="|sin/cos(n*(theta+iy))-sin/cos(n*theta)| <= n*exp(n*h0)*|y| <= n*U_n*|y|",
                complete_actual_exp_factor_identity=self.exp_factors_identity,
                exp_factor_definition="U_n is the outward complete exponential upper bound at n*h0, with all n=2..2M",
                exp_factors_shared_only_inside_this_same_policy_observer=True,
                r0_and_z0_zero_in_angle_differences_not_deleted_from_original_state=True),
            constructive_width=dict(h0=h0, C1=C1, Q1=Q1, W1=W1, P1=P1,
                W_half_margin_cap=w_cap, P_half_margin_cap=p_cap,
                positive_constructive_half_width=constructive_h,
                chosen_half_width=h,relative_dyadic_bits=self.sqrt_bits,
                chosen_width_is_rounded_down_without_underflow=True,
                zero_slope_ratio_is_absent_not_a_division_by_zero=True,
                no_search_or_additional_domain_split=True),
            complete_complex_differences=dict(d=dd,e=de,cross=dc,Q=dq,W=dw,P=dp),
            complex_denominator_abs_lower=W_gap,
            complex_P_real_part_lower=P_gap,
            real_positive_sqrt_branch_is_single_valued_on_right_half_plane=True,
            complex_bilinear_invariants_not_Hermitian_squares=True,
            full_C3_Hermitian_norm_upper=bound,
            returned_complex_sup_rounded_up_at_inherited_sqrt_bits=True,
            two_sup_bounds=dict(direct=direct_sup,from_real_base=near_real_sup,
                B_direct=B_direct,B0_real_upper=B0_upper,delta_dot=delta_dot,
                delta_B=delta_B,delta_sqrt_P=delta_sqrt,
                sqrt_P_abs_upper=sqrt_P_upper,delta_numerator=delta_numerator,
                real_velocity_norm_mu_not_used_as_a_complex_identity=True),
            velocity_formula="(sigma*sqrt(P)*(d cross e)-nu*Q*(Q*e-(d dot e)*d))/(A*W)",
            fixed_sigma_required=True, identical_bounds_for_both_fixed_signs=True,
            actual_worker_root_or_sigma_not_identified=True,
            full_real_circle_not_inferred_from_this_local_angular_leaf=True)

    def inspect(self, cell, actual_tube_record):
        self.budget_check()
        piece = self.field.pieces[cell["piece_index"]]
        if piece["kind"] != "prefix":
            return None
        self.observed += 1
        self.last_observed = copy.deepcopy(cell)
        self.pending = dict(scope="original_prefix_cell", original_cell=copy.deepcopy(cell),
            phase="validate_same_return", position={})
        result = dict(schema=SCHEMA+"-cell", original_cell=copy.deepcopy(cell),
            bound_policy_identity=self.policy_identity, available=False,
            source_tube_record_identity=(value_identity(actual_tube_record)
                if isinstance(actual_tube_record,dict) else None),
            analytic_strip=None,reasons=[],error=None,
            local_leaf_not_a_complete_Fourier_certificate=True,
            original_metric_decision_not_changed=True)
        try:
            require(isinstance(actual_tube_record,dict)
                and actual_tube_record.get("schema") == self.R.TUBE_SCHEMA+"-cell"
                and actual_tube_record.get("original_cell") == cell,
                "Use the actual same-cell R553 return")
            if actual_tube_record.get("available") is not True:
                result["reasons"].append("original_same_cell_positive_joint_tube_unpaid")
                result["R553_reasons"] = copy.deepcopy(actual_tube_record.get("reasons"))
                result["R553_error"] = copy.deepcopy(actual_tube_record.get("error"))
                return self.finished(result)
            tube, angular = actual_tube_record["coefficient_tube"], actual_tube_record["angular_box"]
            require(tube["field_modes"] == self.M and tube["physical_size"] == 3*self.M+2
                and self.T.pair(tube["radial"]) == self.T.pair(cell["radial"])
                and tube["prefix_span"] == piece["prefix_span"],
                "The actual radial coefficient owner and complete layout")
            require(self.T.pair(angular["angular"]) == self.T.pair(cell["angular"])
                and angular["complete_frequency_count"] == self.M
                and angular["frequencies"] == [2*j for j in range(1,self.M+1)],
                "The actual complete closed physical-angle cell")
            lo, hi = self.T.pair(angular["angular"])
            require(Q(0) <= lo <= hi <= Q(1), "Original q in [0,1], phi=2*pi*q")
            result["analytic_strip"] = self.strip_from_record(actual_tube_record)
            result["available"] = True
            return self.finished(result)
        except MATH_ERRORS as error:
            result["error"] = dict(type=type(error).__name__,message=str(error),
                actual_phase=copy.deepcopy(self.pending))
            result["reasons"].append("actual_analytic_strip_ingredient_unpaid")
            return self.finished(result)
        # RuntimeError resource stops, MemoryError, KeyboardInterrupt and
        # SystemExit are deliberately not caught or retried. pending retains
        # the exact current cell/phase for the original recovery summary.

    def commit_original_retirement(self, cell, diagnostic, *, split):
        if self.field.pieces[cell["piece_index"]]["kind"] != "prefix":
            return None
        self.committed += 1
        if split:
            self.split += 1
            return dict(original_prefix_cell_split=True,
                all_original_children_retain_analytic_strip_responsibility=True)
        self.terminal += 1
        good = (isinstance(diagnostic,dict)
            and diagnostic.get("schema") == SCHEMA+"-cell"
            and diagnostic.get("original_cell") == cell
            and diagnostic.get("bound_policy_identity") == self.policy_identity
            and diagnostic.get("available") is True)
        commit_error = None
        if good:
            try:
                item = diagnostic["analytic_strip"]
                h = exact(item["constructive_width"]["chosen_half_width"])
                C = exact(item["full_C3_Hermitian_norm_upper"])
                W_gap = exact(item["complex_denominator_abs_lower"])
                P_gap = exact(item["complex_P_real_part_lower"])
                require(h > 0 and C >= 0 and W_gap > 0 and P_gap > 0
                        and item["field_modes"] == self.M and item["angular_count"] == self.N,
                        "Complete same-cell strip values and actual finite dimensions")
            except MATH_ERRORS as error:
                good = False
                commit_error = dict(type=type(error).__name__,message=str(error))
        if not good:
            self.unpaid += 1
            row = dict(original_cell=copy.deepcopy(cell),
                reasons=(["same_cell_analytic_strip_not_returned"] if not isinstance(diagnostic,dict)
                    else copy.deepcopy(diagnostic.get("reasons"))),
                evaluation_error=(None if not isinstance(diagnostic,dict)
                    else copy.deepcopy(diagnostic.get("error"))),
                retirement_record_error=commit_error,terminal_analytic_strip_paid=False)
            if self.first_unpaid is None:
                self.first_unpaid = row
            self.last_unpaid = row
            return row
        self.paid += 1
        self.min_width = h if self.min_width is None else min(self.min_width,h)
        self.max_sup = max(self.max_sup,C)
        self.min_W_gap = W_gap if self.min_W_gap is None else min(self.min_W_gap,W_gap)
        self.min_P_gap = P_gap if self.min_P_gap is None else min(self.min_P_gap,P_gap)
        return dict(original_cell=copy.deepcopy(cell),terminal_analytic_strip_paid=True,
            actual_complete_local_record_identity=value_identity(diagnostic),
            no_local_strip_relabelled_a_global_circle_bound=True)

    def summary(self, *, original_coverage, complete_cell_ledger, original_error,
                original_stop, close_errors):
        tube = self.tubes.summary(original_coverage=original_coverage,
            complete_cell_ledger=complete_cell_ledger,original_error=original_error,
            original_stop=original_stop,close_errors=close_errors)
        counters_match = (self.observed == self.tubes.observed_prefix_cells
            and self.committed == self.tubes.committed_prefix_cells
            and self.split == self.tubes.split_prefix_cells
            and self.terminal == self.tubes.terminal_prefix_leaves
            and self.paid == self.terminal and self.unpaid == 0)
        complete = (tube.get("complete_prefix_constant_cover") is True
            and counters_match and self.terminal > 0 and self.pending is None)
        bound, final_error = None, None
        if complete:
            self.pending = dict(scope="global_strip_projection",phase="begin",position={})
            try:
                bound = conditional_exponential_projection_bound(self.min_width,self.max_sup,
                    self.M,self.N,exponential_terms=self.exponential_terms,
                    enclosure_bits=self.sqrt_bits,
                    budget_check=lambda: self.work("global_exact_exponential_and_alias_bound"))
                self.pending = None
            except MATH_ERRORS as error:
                complete = False
                final_error = dict(type=type(error).__name__,message=str(error),
                    actual_phase=copy.deepcopy(self.pending))
                self.pending = None
        # A resource exception from the global bound propagates unchanged.
        # The caller's original recovery may then call this metadata summary
        # with its actual stop/error; complete is false and no bound is retried.
        return encoded(dict(schema=SCHEMA+"-necessary",binding=self.binding,
            actual_R553_summary_identity=value_identity(tube),
            actual_complete_exp_factor_identity=self.exp_factors_identity,
            complete_original_cell_ledger=copy.deepcopy(complete_cell_ledger),
            original_coverage_object_in_same_result="coverage",
            original_all_DFS_and_R553_complete=tube.get("complete_prefix_constant_cover") is True,
            observed_prefix_cells=self.observed,committed_prefix_cells=self.committed,
            split_prefix_cells=self.split,terminal_prefix_leaves=self.terminal,
            paid_terminal_analytic_strips=self.paid,unpaid_terminal_analytic_strips=self.unpaid,
            exact_original_retirement_counters_match=counters_match,
            complete_prefix_analytic_projection_bound=complete,
            global_prefix_exact_reference_projection_bound=bound,
            global_strip_half_width=(self.min_width if complete else None),
            global_complex_vector_sup=(self.max_sup if complete else None),
            observed_paid_leaf_extrema=dict(strip_half_width=self.min_width,
                complex_vector_sup=self.max_sup,W_gap=self.min_W_gap,P_gap=self.min_P_gap,
                these_are_not_global_without_the_complete_original_cover=True),
            first_unpaid_terminal=self.first_unpaid,last_unpaid_terminal=self.last_unpaid,
            last_observed_cell=self.last_observed,actual_unfinished_operation=self.pending,
            global_bound_formation_error=final_error,
            complete_each_local_input_error_and_result_remains_in_original_cell_ledger=True,
            ledger_rows_not_claimed_fully_transported_by_this_summary=True,
            current_frontier_and_all_unvisited_roots_remain_in_original_coverage=True,
            both_reflected_sheets_and_all_original_prefix_pieces_required=True,
            R575_B2_or_metric_success_not_an_additional_gate=True,
            no_guarantee_of_smaller_bound_or_same_resource_frontier=True,
            phase_scope=dict(
                established_base_defect_may_be_pulled_back_by_the_actual_common_phase=True,
                real_world_orthogonal_registration_and_reflection_preserve_vector_norm=True,
                complex_world_rotation_not_assumed_unitary=True,
                fixed_grid_parity_projection_not_claimed_to_commute_with_arbitrary_translation=True,
                rho_and_material_pullback_and_cap_gluing_responsibilities_unchanged=True),
            unpaid=["actual floating FFT/trig/profile/root and RHS formation difference",
                "nominal scalar versus the same accurate C target RHS difference",
                "original literal cubic residual and comparison-path membership",
                "actual worker root and fixed sigma identification",
                "tail/collar/cut-patch/cap coefficient references",
                "angular target rho, boundary anchors and full relative-metric floor"],
            original_BVP_native_FD_fullDN_metric_and_DFS_predicates_changed=False,
            new_field_query_grid_clock_child_or_cleanup_started=False))


def bind_loaded_analytic_projection_defect(projection_observer, *,
        strip_width_cap, exponential_terms):
    """Actual R575 context; no required B2 evaluation or success."""
    return BoundAnalyticProjection(projection_observer,
        strip_width_cap=strip_width_cap,exponential_terms=exponential_terms)
