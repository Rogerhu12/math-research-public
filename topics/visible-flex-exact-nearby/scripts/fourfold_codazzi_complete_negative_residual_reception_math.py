"""WNR: complete finite ordered scalar residual, true jumps and PW reception.
No entry point. No file or network access. No old producer import.
The caller validates and saves the new extension/J/mean module's complete
patches before passing their outward typed bounds to these routines.

All Jet coefficients are normalized ordinary derivative norm bounds.
Decoded WGS geometry and amplitudes are C^k/sup bounds, not Wiener norms.
The only operator 1/4 below acts on the actual periodic I in L2.
Amplitude primitives use the exact finite profile identity instead.

The positive polynomial is a coefficientwise majorant of an ordered exact
expansion. Coefficients of input degrees -2,-1,0 are removed only AFTER
assembling the full Q, by WUA.7, WUA.13 and WUA.23. No interval bounds are
subtracted. Every projection mean and exact terminal I or J remains.
"""
from __future__ import annotations
from fractions import Fraction
from math import factorial

N0 = 388
MAX_PRIMITIVE_STEPS = 6
RETAINED_MAX_POWER = 5
TERMINAL_POWER = 4
PATCH_NAMES = ("strict", "local")
PROFILE_WINDOWS = ("0", "-5/3", "-2")
ORIGINAL_INTERFACE_COUNT = 3070
ORIGINAL_GENUINE_JOIN_COUNT = 2549
ORIGINAL_ARTIFICIAL_INTERFACE_COUNT = 521
ORDERED_SCALAR_TERMS = (
    "D0_squared",
    "eta_squared_K_dphi_squared",
    "minus_B_D0",
    "minus_tQ_D0",
    "minus_RQ_J_D0",
    "plus_tQ_B",
    "plus_RQ_J_B",
    "minus_B_radial",
    "plus_Dcal_commutator_B",
    "minus_K_VAC",
)
EXACT_IDENTITIES = {
    "scalar": "Q=D0^2+eta^2*K*dphi^2-(B+tQ+RQ*J)D0+(tQ+RQ*J)B-B_r+[Dcal,B]-K*VAC",
    "commutator": "[Dcal,P*a*I*b*P]=P*(d*a_phi*I*b+d*a*P*b-a*P*(b*d)+a*I*(b*d)_phi-a*I*b*Pi*d_phi)*P",
    "primitive": "I U(v)=n^-1 P U(H^-1 v)-n^-1 I U(A_n H^-1 v)",
    "mean": "Pi U(v)=-n^-1 Pi U(A_n H^-1 v)",
    "inverse": "J=Jpr*sum_{k=0}^5(-L*Jpr)^k+J*(-L*Jpr)^6",
    "profile_phi": "dphi U(v)=U(n*H*v+v_phi-n^-1*V*T_phi*E12*v)",
    "profile_D": "D U(v)=U(n*H_D*v+Dv-n^-1*V*DT*E12*v)",
    "jump": "[w1_r]=(Qfold/2)*[[x,+i*epsilon*y],[+i*epsilon*y,x/T]]*([Fa],[Fb])",
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def positive_power(api, value, numerator, denominator=1, label="positive power"):
    require(isinstance(numerator, int) and isinstance(denominator, int)
            and denominator > 0, "rational exponent")
    if numerator < 0:
        base = api.lower(value, label)
    else:
        base = api.up(value)
        if base == 0:
            require(numerator > 0, "zero to nonpositive power")
            return api.ex(0)
    return api.up(base ** (api.ex(numerator) / api.ex(denominator)))

def complete_record(api, value):
    rec = api.record(api.up(value))
    return rec, api.read_up(rec)

def complete_lower(api, value, label):
    rec, working = api.lower_record(value, label)
    return rec, api.lower(working, label + " retained")

def sum_upper(api, values):
    return api.up(sum(values, api.ex(0)))

def max_upper(api, values):
    vv = [api.up(x) for x in values]
    require(bool(vv), "empty complete domain union")
    return max(vv)

def ordinary_angles(api, jet, maximum=4):
    jet.need(maximum, 0)
    return [api.up(api.ex(factorial(q)) * jet.c[0, q])
            for q in range(maximum + 1)]

def records_with_work(api, mapping):
    doc, work = {}, {}
    for key, value in mapping.items():
        doc[key], work[key] = complete_record(api, value)
    return doc, work

def angle_records_with_work(api, jet, maximum=4):
    doc, work = [], []
    for value in ordinary_angles(api, jet, maximum):
        rec, upper = complete_record(api, value)
        doc.append(rec)
        work.append(upper)
    return doc, work

def profile_receiver(api, profile, patch_name, window, ordinary_amplitude):
    row = profile["complete_block_receiver_weights"][patch_name][window]
    require(len(row) == 5 and len(ordinary_amplitude) == 5,
            "one complete C4 full-output profile receiver")
    # The owner of this row has already included both actual phases,
    # all low outputs, the angle maps and the original reflected normalization.
    require(profile["block_rows_include_complete_reflected_assembly"] is True,
            "missing original reflected block normalization")
    weights = [api.read_up(r) for r in row]
    return sum_upper(api, (weights[q] * ordinary_amplitude[q] for q in range(5)))

class _State:
    """Exact-expression majorant: sum n^-k U(v_k) plus an L2 terminal.
    tail bounds n^-4 b_n(rho), already with the declared reflected factor.
    parity is the actual assembled physical parity, not inferred from norms.
    """
    def __init__(self, poly, tail, parity, projected=False, deferred_outer_P=False):
        require(parity in ("even", "odd"), "actual parity must be specified")
        self.poly = dict(poly)
        self.tail = tail
        self.parity = parity
        self.projected = bool(projected or parity == "odd")
        self.deferred_outer_P = bool(deferred_outer_P)
        require(not self.deferred_outer_P or self.projected,
                "a deferred outer P must remain an actual projected expression")

class _FiniteCalculator:
    def __init__(self, api, patch, profile, patch_name):
        self.a = api
        self.patch = patch
        self.name = patch_name
        self.zero_value = api.ex(0)
        self.one_value = api.ex(1)
        self.primitive_norm = api.ex(1) / api.ex(4)
        physical = patch["physical_coefficients"]
        geometry = patch["geometry"]
        self.J0 = api.read_up(patch["same_J"]["J0_upper"])
        self.L0 = api.read_up(patch["same_J"]["L0_upper"])
        self.eta_lower = api.read_lower(patch["same_J"]["eta_lower"], patch_name + " eta")
        self.eta_inverse = api.up(api.ex(1) / self.eta_lower)
        single = api.read_up(profile["single_signed_pointwise_upper"][patch_name])
        t_lower = api.read_lower(profile["whole_t_over_rho_lower"],
                                 "whole t/rho for profile comparison")
        comparison = max_upper(api, [api.ex(1), positive_power(api, t_lower, -1, 4)])
        # One signed genuine column is the profile input. The actual real
        # reflected column is bounded by this fixed factor, exactly once.
        self.point = api.up(api.ex(2) * single * comparison)
        self.point_single = single
        self.point_comparison = comparison
        self.Hinv = geometry["H_inverse_entry_sum"]
        self.T = geometry["T_absolute_jet"]
        self.x = geometry["X_phi_jet"]
        self.y = geometry["T_phi_absolute_jet"]
        self.V = patch["potential"]["V_of_T_jet"]
        self.X = geometry["X_derivative_jet"]
        self.Tsigned_derivatives = geometry["T_derivative_absolute_jet"]
        self.coefficients = {}
        for key, parity, angular_scalar in (
            ("U", 1, False), ("V", 0, False), ("beta", 0, True),
            ("K", 0, True), ("eta", 0, True), ("d", 1, False),
            ("ell", 1, False), ("L11", 0, False), ("L22", 0, False)):
            jet = physical[key]
            self.coefficients[key] = (jet, parity, angular_scalar)
        for key in ("U", "V", "d", "ell", "L11", "L22"):
            base, parity, scalar = self.coefficients[key]
            self.coefficients[key + "_phi"] = (
                base.derivative(da=1, p=0, label=key + "_phi"), 1-parity, False)
            self.coefficients[key + "_r"] = (
                base.derivative(dr=1, p=0, label=key + "_r"), parity, scalar)
        for key in ("U", "V"):
            base, parity, _ = self.coefficients[key]
            self.coefficients[key + "_phiphi"] = (
                base.derivative(da=2, p=0, label=key + "_phiphi"), parity, False)
            self.coefficients[key + "_rphi"] = (
                base.derivative(dr=1, da=1, p=0, label=key + "_rphi"), 1-parity, False)
        for key in ("beta", "K"):
            base, parity, scalar = self.coefficients[key]
            self.coefficients[key + "_r"] = (
                base.derivative(dr=1, p=0, label=key + "_r"), parity, scalar)
        eta_r = physical["eta"].c[1, 0]
        local_tQ = api.constant(api.up(eta_r * self.eta_inverse), 13, 0, "eta_r_over_eta")
        self.coefficients["tQ"] = (
            self.jadd(local_tQ, self.coefficients["d_phi"][0],
                      self.coefficients["L11"][0]), 0, False)
        self.last_terminals = {}
        self.call_counts = {"primitive_calls": 0, "mean_calls": 0,
                            "complete_J_calls": 0, "max_primitive_depth": 0,
                            "max_mean_depth": 0}
        self.verified_parity_calls = 0

    def jadd(self, *jets):
        require(bool(jets), "empty jet sum")
        return self.a.add(*jets, m=min(t.m for t in jets), p=min(t.p for t in jets),
                          label="complete_positive_coefficient_sum")

    def jmul(self, *jets):
        require(bool(jets), "empty jet product")
        return self.a.mul(*jets, m=min(t.m for t in jets), p=min(t.p for t in jets),
                          label="complete_ordered_coefficient_product")

    def jscale(self, jet, value):
        return self.a.scale(jet, self.a.up(value))

    def angular(self, jet):
        return jet.part(jet.m, 0)

    def zero(self, parity, projected=False):
        return _State({}, self.a.ex(0), parity, projected)

    def add(self, *states):
        require(bool(states), "empty state sum")
        nonzero = [s for s in states if s.poly or s.tail != 0]
        parity = nonzero[0].parity if nonzero else states[0].parity
        require(all(s.parity == parity for s in nonzero), "ordered parity mismatch")
        poly = {}
        for state in states:
            for power, jet in state.poly.items():
                poly[power] = self.jadd(poly[power], jet) if power in poly else jet
        deferred = any(s.deferred_outer_P for s in states)
        require(not deferred or all(s.projected for s in nonzero),
                "the common final P cannot be joined to an unprojected expression")
        return _State(poly, sum_upper(self.a, (s.tail for s in states)), parity,
                      all(s.projected for s in nonzero), deferred)

    def scaled(self, state, value):
        value = self.a.up(value)
        return _State({k:self.jscale(v, value) for k,v in state.poly.items()},
                      self.a.up(state.tail * value), state.parity, state.projected,
                      state.deferred_outer_P)

    def profile_only(self, state):
        return _State(state.poly, self.a.ex(0), state.parity, state.projected,
                      state.deferred_outer_P)

    def retire(self, power, jet, operator_upper=1):
        require(power >= TERMINAL_POWER, "terminal lost its complete inverse power")
        value = self.a.ex(operator_upper) if isinstance(operator_upper, int) else operator_upper
        return self.a.up(self.point * jet.c[0,0] * value *
                         positive_power(self.a, self.a.ex(N0), TERMINAL_POWER-power))

    def trim(self, state):
        poly, tail = {}, state.tail
        for power, jet in state.poly.items():
            if power > RETAINED_MAX_POWER:
                tail = self.a.up(tail + self.retire(power, jet))
            else:
                require(power >= -2, "unqualified positive derivative order")
                poly[power] = jet
        return _State(poly, tail, state.parity, state.projected, state.deferred_outer_P)

    def mean_fee(self, power, jet):
        """Exact Pi identity, with all branches retained until n^-4 is reached."""
        self.call_counts["mean_calls"] += 1
        pending = {power:self.angular(jet)}
        total = self.a.ex(0)
        for depth in range(MAX_PRIMITIVE_STEPS + 1):
            self.call_counts["max_mean_depth"] = max(self.call_counts["max_mean_depth"], depth)
            following = {}
            for degree, value in pending.items():
                if degree >= TERMINAL_POWER:
                    total = self.a.up(total + self.retire(degree, value))
                    continue
                require(depth < MAX_PRIMITIVE_STEPS, "finite mean recursion did not reach its true order")
                hv = self.jmul(self.angular(self.Hinv), value)
                phi = hv.derivative(da=1, p=0, label="complete_mean_Hinverse_derivative")
                potential = self.jmul(self.angular(self.V), self.angular(self.y), hv)
                for kk, vv in ((degree+1, phi), (degree+2, potential)):
                    following[kk] = self.jadd(following[kk], vv) if kk in following else vv
            pending = following
            if not pending:
                break
        require(not pending, "complete finite mean remainder missing")
        return total

    def project(self, state):
        if state.projected or state.parity == "odd":
            return _State(state.poly, state.tail, state.parity, True, state.deferred_outer_P)
        mean = sum_upper(self.a, (self.mean_fee(k,v) for k,v in state.poly.items()))
        return _State(state.poly, self.a.up(state.tail + mean), state.parity, True)

    def mean(self, state):
        require(not state.deferred_outer_P, "deferred local P is only for the final full sum")
        if state.projected or state.parity == "odd":
            return self.zero("even")
        fee = sum_upper(self.a, (self.mean_fee(k,v) for k,v in state.poly.items()))
        return _State({}, self.a.up(state.tail + fee), "even", False)

    def coefficient(self, name):
        return self.coefficients[name]

    def product_coefficient(self, *names):
        rows = [self.coefficient(k) if isinstance(k,str) else k for k in names]
        return (self.jmul(*(r[0] for r in rows)),
                sum(r[1] for r in rows) % 2, all(r[2] for r in rows))

    def multiply(self, coefficient, state):
        jet, flip, scalar = self.coefficient(coefficient) if isinstance(coefficient,str) else coefficient
        require(not state.deferred_outer_P or scalar,
                "nonconstant multiplier cannot cross the deferred local outer P")
        parity = state.parity if flip == 0 else ("odd" if state.parity == "even" else "even")
        out = _State({k:self.jmul(self.angular(jet), self.angular(v))
                      for k,v in state.poly.items()},
                     self.a.up(jet.c[0,0] * state.tail), parity,
                     bool(state.projected and scalar), state.deferred_outer_P)
        return self.trim(out)

    def primitive(self, state):
        """At most six exact one-step identities; all means and final I remain."""
        self.call_counts["primitive_calls"] += 1
        require(not state.deferred_outer_P, "local outer P must reach the full Q before any primitive")
        parity = "odd" if state.parity == "even" else "even"
        result = _State({}, self.a.up(state.tail * self.primitive_norm), parity, True)
        pending = {k:self.angular(v) for k,v in state.poly.items()}
        for depth in range(MAX_PRIMITIVE_STEPS):
            self.call_counts["max_primitive_depth"] = max(
                self.call_counts["max_primitive_depth"], depth+1)
            following = {}
            for degree, value in pending.items():
                if degree > RETAINED_MAX_POWER:
                    result.tail = self.a.up(result.tail +
                        self.retire(degree, value, self.primitive_norm))
                    continue
                hv = self.jmul(self.angular(self.Hinv), value)
                contribution = _State({degree+1:hv}, self.a.ex(0), parity, False)
                contribution = self.trim(self.project(contribution))
                result = self.add(result, contribution)
                phi = hv.derivative(da=1, p=0, label="complete_primitive_Hinverse_derivative")
                potential = self.jmul(self.angular(self.V), self.angular(self.y), hv)
                for kk, vv in ((degree+1, phi), (degree+2, potential)):
                    following[kk] = self.jadd(following[kk], vv) if kk in following else vv
            pending = following
            if not pending:
                break
        for degree, value in pending.items():
            result.tail = self.a.up(result.tail +
                self.retire(degree, value, self.primitive_norm))
        result.projected = True
        return self.trim(result)

    def nonlocal_word(self, a_name, b_name, state, scalar_names=()):
        out = self.project(state)
        out = self.multiply(b_name, out)
        out = self.primitive(out)
        out = self.multiply(a_name, out)
        if scalar_names:
            out = self.multiply(self.product_coefficient(*scalar_names), out)
        return self.project(out)

    def L(self, state):
        require(state.parity == "odd", "L input is the actual odd space")
        base = self.profile_only(state)
        out = self.add(self.project(self.multiply("ell", self.project(base))),
                       self.scaled(self.nonlocal_word("V_phi","U",base,("beta",)), self.a.ex(2)))
        out.tail = self.a.up(out.tail + self.L0 * state.tail)
        return self.project(out)

    def M(self, state):
        require(state.parity == "even", "C lower operator input is even")
        return self.add(self.project(self.multiply("ell", self.project(state))),
                        self.scaled(self.nonlocal_word("U_phi","V",state,("beta",)), self.a.ex(2)))

    def B(self, state):
        require(state.parity == "even", "B input is even")
        return self.add(self.project(self.multiply("L22",self.project(state))),
                        self.scaled(self.nonlocal_word("V_phi","V",state,("beta","K")), self.a.ex(2)))

    def E(self, state):
        require(state.parity == "odd", "E input is odd")
        return self.add(self.project(self.multiply("L11",self.project(state))),
                        self.scaled(self.nonlocal_word("U_phi","U",state,("beta",)), self.a.ex(2)))

    def J(self, state):
        """Finite exact J identity; already terminal pieces use the whole J0."""
        self.call_counts["complete_J_calls"] += 1
        require(not state.deferred_outer_P, "local outer P must reach the full Q before J")
        require(state.parity == "even" and state.projected,
                "J only acts on the qualified even mean-zero space")
        self.verified_parity_calls += 1
        result = _State({}, self.a.up(self.J0 * state.tail), "odd", True)
        pending = self.profile_only(state)
        for unused in range(MAX_PRIMITIVE_STEPS):
            if not pending.poly:
                break
            jp = self.scaled(self.primitive(pending), self.eta_inverse)
            result = self.add(result, self.profile_only(jp))
            # Jpr's terminal E and the exact -J L E are grouped before
            # any additional finite inverse expansion.
            result.tail = self.a.up(result.tail + (self.a.ex(1) + self.J0*self.L0)*jp.tail)
            next_state = self.L(self.profile_only(jp))
            result.tail = self.a.up(result.tail + self.J0 * next_state.tail)
            pending = self.profile_only(next_state)
        for degree, value in pending.poly.items():
            result.tail = self.a.up(result.tail + self.retire(degree,value,self.J0))
        result.projected = True
        return self.trim(result)

    def local_commutator(self, coefficient, state):
        jet, flip, scalar = self.coefficient(coefficient)
        derivative = (jet.derivative(da=1,p=0),1-flip,False)
        first = self.multiply(self.product_coefficient("d",derivative), self.project(state))
        second = self.multiply(coefficient,
                   self.mean(self.multiply("d_phi",self.project(state))))
        return self.project(self.add(first,second))

    def primitive_commutator(self, a_name, b_name, state):
        """The five exact O.15 order-zero terms, including the last mean rank."""
        aa, aflip, _ = self.coefficient(a_name)
        a_phi = (aa.derivative(da=1,p=0),1-aflip,False)
        bd = self.product_coefficient(b_name,"d")
        bd_phi = (bd[0].derivative(da=1,p=0),1-bd[1],False)
        p = self.project(state)
        first = self.multiply(self.product_coefficient("d",a_phi),
                    self.primitive(self.multiply(b_name,p)))
        second = self.multiply(self.product_coefficient("d",a_name),
                    self.project(self.multiply(b_name,p)))
        third = self.multiply(a_name,self.project(self.multiply(bd,p)))
        fourth = self.multiply(a_name,self.primitive(self.multiply(bd_phi,p)))
        fifth = self.multiply(a_name,self.primitive(self.multiply(b_name,
                    self.mean(self.multiply("d_phi",p)))))
        return self.project(self.add(first,second,third,fourth,fifth))

    def L_radial(self, state):
        p = self.project(state)
        local = self.project(self.multiply("ell_r",p))
        terms = [
            self.nonlocal_word("V_phi","U",p,("beta_r",)),
            self.nonlocal_word("V_rphi","U",p,("beta",)),
            self.nonlocal_word("V_phi","U_r",p,("beta",)),
        ]
        return self.add(local,self.scaled(self.add(*terms),self.a.ex(2)))

    def B_radial(self, state):
        p = self.project(state)
        local = self.project(self.multiply("L22_r",p))
        terms = [
            self.nonlocal_word("V_phi","V",p,("beta_r","K")),
            self.nonlocal_word("V_phi","V",p,("beta","K_r")),
            self.nonlocal_word("V_rphi","V",p,("beta","K")),
            self.nonlocal_word("V_phi","V_r",p,("beta","K")),
        ]
        return self.add(local,self.scaled(self.add(*terms),self.a.ex(2)))

    def commutator_L(self, state):
        return self.add(self.local_commutator("ell",state),
            self.scaled(self.multiply("beta",
                self.primitive_commutator("V_phi","U",state)),self.a.ex(2)))

    def commutator_B(self, state):
        return self.add(self.local_commutator("L22",state),
            self.scaled(self.multiply(self.product_coefficient("beta","K"),
                self.primitive_commutator("V_phi","V",state)),self.a.ex(2)))

    def derivative_N(self, a_phi_name, a_phiphi_name, b_name, state):
        p = self.project(state)
        first = self.multiply(a_phiphi_name,self.primitive(self.multiply(b_name,p)))
        second = self.multiply(a_phi_name,self.project(self.multiply(b_name,p)))
        return self.project(self.scaled(self.multiply("beta",
                                self.add(first,second)),self.a.ex(2)))

    def RQ(self, state):
        require(state.parity == "odd", "RQ input is the same odd state")
        p = self.project(state)
        local = self.project(self.multiply(
            self.product_coefficient("eta","L11_phi"),p))
        derivative_ne = self.multiply("eta",
            self.derivative_N("U_phi","U_phiphi","U",p))
        le = self.L(self.E(p))
        tql = self.project(self.multiply("tQ",self.L(p)))
        return self.project(self.add(self.L_radial(p),self.commutator_L(p),
                                      local,derivative_ne,le,tql))

    def VAC(self, state):
        p = self.project(state)
        local = self.project(self.multiply(
            self.product_coefficient("eta","ell_phi"),p))
        derivative_nc = self.multiply("eta",
            self.derivative_N("U_phi","U_phiphi","V",p))
        n_a_dphi = self.add(
            self.multiply("V_phi",self.project(self.multiply("U",p))),
            self.multiply("V_phi",self.primitive(self.multiply("U_phi",p))))
        n_a_dphi = self.project(self.scaled(self.multiply(
            self.product_coefficient("beta","eta"),n_a_dphi),self.a.ex(2)))
        return self.project(self.add(local,derivative_nc,n_a_dphi,self.L(self.M(p))))

    def local_derivative(self, poly, direction):
        """Only on pure amplitudes, before any exact I/J/mean terminal."""
        require(direction in ("D","phi"), "local derivative direction")
        a = self.a
        if direction == "phi":
            first_phase = self.x
            second_phase = self.y
        else:
            d = self.coefficients["d"][0]
            first_phase = self.jadd(
                self.X.derivative(dr=1,p=max(0,self.X.p-1)),
                self.jmul(d,self.x))
            second_phase = self.jadd(
                self.Tsigned_derivatives.derivative(dr=1,p=max(0,self.Tsigned_derivatives.p-1)),
                self.jmul(d,self.y))
        one = a.constant(a.ex(1),self.T.m,self.T.p,"one")
        Hsum = self.jadd(self.jscale(first_phase,a.ex(2)),
                        self.jmul(self.jadd(one,self.T),second_phase))
        Vphase = self.jmul(self.V,second_phase)
        out = {}
        for degree, value in poly.items():
            if direction == "phi":
                low = value.derivative(da=1)
            else:
                low = self.jadd(value.derivative(dr=1),
                        self.jmul(self.coefficients["d"][0],value.derivative(da=1)))
            contributions = (
                (degree-1,self.jmul(Hsum,value)),
                (degree,low),
                (degree+1,self.jmul(Vphase,value)),
            )
            for kk,vv in contributions:
                out[kk] = self.jadd(out[kk],vv) if kk in out else vv
        return out

    def compute(self, on_complete_term):
        require(callable(on_complete_term), "complete-word progress recorder is required")
        amplitudes = self.patch["amplitudes"]
        base = {0:self.jadd(*amplitudes["w0_pair"]),
                1:self.jadd(*amplitudes["w1ext_pair"])}
        d1raw = self.local_derivative(base,"D")
        d2raw = self.local_derivative(d1raw,"D")
        phi1raw = self.local_derivative(base,"phi")
        phi2raw = self.local_derivative(phi1raw,"phi")
        base_state = self.project(_State({k:self.angular(v) for k,v in base.items()},
                                         self.a.ex(0),"even",False))
        d1 = self.project(_State({k:self.angular(v) for k,v in d1raw.items()},
                                 self.a.ex(0),"even",False))
        # Global P D^2 and P dphi^2 are kept outside. There is no
        # differentiated artificial mean remainder in either local term.
        d2 = _State({k:self.angular(v) for k,v in d2raw.items()},
                    self.a.ex(0),"even",True,True)
        ph2 = _State({k:self.angular(v) for k,v in phi2raw.items()},
                     self.a.ex(0),"even",True,True)
        eta2K = self.product_coefficient("eta","eta","K")
        # Each completed ordered word is recorded immediately. This callback
        # only records the current new graph; it never reruns a word or calls
        # an old scientific producer. The common Bf is calculated once.
        pieces, shared = {}, {}
        def Bf():
            if "Bf" not in shared:
                shared["Bf"] = self.B(base_state)
            return shared["Bf"]
        builders = (
            ("D0_squared", lambda: d2),
            ("eta_squared_K_dphi_squared", lambda: self.multiply(eta2K,ph2)),
            ("minus_B_D0", lambda: self.B(d1)),
            ("minus_tQ_D0", lambda: self.project(self.multiply("tQ",d1))),
            ("minus_RQ_J_D0", lambda: self.RQ(self.J(d1))),
            ("plus_tQ_B", lambda: self.project(self.multiply("tQ",Bf()))),
            ("plus_RQ_J_B", lambda: self.RQ(self.J(self.project(Bf())))),
            ("minus_B_radial", lambda: self.B_radial(base_state)),
            ("plus_Dcal_commutator_B", lambda: self.commutator_B(base_state)),
            ("minus_K_VAC", lambda: self.multiply("K",self.VAC(base_state))),
        )
        for name, build in builders:
            on_complete_term(name, None)
            pieces[name] = build()
            on_complete_term(name, pieces[name])
        require(tuple(pieces)==ORDERED_SCALAR_TERMS,"complete ordered Q term set")
        combined = self.trim(self.add(*pieces.values()))
        require(combined.deferred_outer_P and combined.projected,
                "the actual final P on the whole ordered scalar sum was lost")
        # This is exact analytic cancellation of the fully assembled symbol.
        # Its positive norm majorants are NEVER subtracted from each other.
        require(self.patch["qualifications"]["complete_WUA_transport_cancellation"] is True,
                "missing full genuine first-transport identity")
        require(self.patch["qualifications"]["same_original_reflected_column"] is True,
                "different trial or profile normalization")
        discarded = [k for k in combined.poly if k <= 0]
        require(all(k in (-2,-1,0) for k in discarded),"unproved lower degree")
        retained = {k:v for k,v in combined.poly.items() if k >= 1}
        require(all(k <= RETAINED_MAX_POWER for k in retained),"finite cutoff escaped")
        for value in retained.values():
            value.need(4,0)
        complete = self.a.zero(4,0,"complete_retained_r_n")
        for degree,value in retained.items():
            complete = self.a.add(complete,
                self.a.scale(value.part(4,0),
                    positive_power(self.a,self.a.ex(N0),1-degree)),
                m=4,p=0,label="complete_retained_r_n")
        return complete,combined.tail,pieces,retained,combined.poly

# ---------------------------------------------------------------------------
# Complete scientific nodes and recoverable current-node prefixes.
# The driver owns publication, receipts, and every failure artifact.
# ---------------------------------------------------------------------------
def _publish(publish_graph, node_name, document):
    require(callable(publish_graph), "a complete atomic publication callback is required")
    saved = publish_graph(node_name, document)
    require(isinstance(saved, dict) and saved == document,
            "the callback must return the complete unchanged persisted JSON document")
    return saved

class _Node:
    """Retain each completed scientific record before any later arithmetic."""
    def __init__(self, name, metadata, progress_state):
        require(isinstance(progress_state, dict), "mutable scientific progress dictionary")
        require(name not in progress_state,
                "a completed or partial scientific node must never be silently recomputed")
        self.name = name
        self.doc = dict(metadata)
        require(self.doc.get("complete") is False, "a new node begins incomplete")
        self.progress = {
            "kind":"recoverable_new_scientific_node_prefix_v1",
            "node_name":name,
            "complete":False,
            "persisted_complete_node":False,
            "current_stage":"initializing",
            "completed_record_paths":[],
            "completed_ordered_words":[],
            "complete_scientific_document_prefix":self.doc,
        }
        progress_state[name] = self.progress

    def stage(self, label):
        self.progress["current_stage"] = label

    def put(self, path, value, scientific_record=False):
        require(isinstance(path, tuple) and bool(path), "one explicit node field path")
        target = self.doc
        for i, part in enumerate(path[:-1]):
            following = path[i+1]
            if isinstance(part, int):
                require(isinstance(target,list) and part >= 0, "list node field")
                while len(target) <= part:
                    target.append(None)
                if target[part] is None:
                    target[part] = [] if isinstance(following,int) else {}
                target = target[part]
            else:
                require(isinstance(target,dict), "dictionary node field")
                if part not in target:
                    target[part] = [] if isinstance(following,int) else {}
                target = target[part]
        last = path[-1]
        if isinstance(last,int):
            require(isinstance(target,list) and last >= 0, "list record field")
            while len(target) <= last:
                target.append(None)
            require(target[last] is None, "an existing scientific record cannot be overwritten")
            target[last] = value
        else:
            require(isinstance(target,dict) and last not in target,
                    "an existing node field cannot be overwritten")
            target[last] = value
        if scientific_record:
            self.progress["completed_record_paths"].append(list(path))
        return value

    def record(self, api, path, value):
        rec, working = complete_record(api,value)
        self.put(path,rec,True)
        return working

    def lower(self, api, path, value, label):
        rec, working = complete_lower(api,value,label)
        self.put(path,rec,True)
        return working

    def angles(self, api, path, jet, maximum=4):
        jet.need(maximum,0)
        working=[]
        for q in range(maximum+1):
            value=api.up(api.ex(factorial(q))*jet.c[0,q])
            working.append(self.record(api,path+(q,),value))
        return working

    def records(self, api, path, builders):
        # Builders are lazy so each record is retained before the next
        # scientific value is evaluated. No Arb basic-operation log is made.
        working={}
        for key, build in builders:
            require(callable(build),"one lazy complete scientific scalar")
            working[key]=self.record(api,path+(key,),build())
        return working

    def finish(self,publish_graph):
        self.doc["complete"]=True
        self.progress["complete"]=True
        self.stage("complete_graph_before_atomic_publication")
        saved=_publish(publish_graph,self.name,self.doc)
        self.progress["persisted_complete_node"]=True
        self.stage("complete_graph_read_back")
        return saved

def _typed_upper(api, value):
    return api.read_up(value) if isinstance(value, dict) else api.up(value)

def _typed_lower(api, value, label):
    return api.read_lower(value, label) if isinstance(value, dict) else api.lower(value, label)

def _validate_bundle(bundle):
    require(isinstance(bundle, dict) and set(bundle["complete_patches"]) == set(PATCH_NAMES),
            "the complete strict/local union is required")
    require(bundle["block_rows_include_complete_reflected_assembly"] is True,
            "the full signed block and reflected restriction qualification is missing")
    for name in PATCH_NAMES:
        p=bundle["complete_patches"][name]
        require(p["qualifications"]["complete_WUA_transport_cancellation"] is True
                and p["qualifications"]["same_original_reflected_column"] is True
                and p["positive_Jet_subtraction_used_to_prove_cancellation"] is False,
                "incomplete actual trial or cancellation qualification")
    require(bundle["complete_whole_error_claimed"] is False,
            "this predecessor bundle is not a whole waist error conclusion")

def _weighted_retained(api, poly, maximum=4):
    answer=api.zero(maximum,0,"complete_weighted_retained_amplitude")
    for degree,jet in poly.items():
        if degree < 1:
            continue
        require(degree <= RETAINED_MAX_POWER,"retained inverse power outside exact cutoff")
        jet.need(maximum,0)
        answer=api.add(answer,
            api.scale(jet.part(maximum,0),
                      positive_power(api,api.ex(N0),1-degree)),
            m=maximum,p=0,label="complete_weighted_retained_amplitude")
    return answer

def complete_ordered_residual_patch(bundle,patch_name,api,publish_graph,progress_state):
    """One complete patch node; each finished word survives any later exception."""
    require(callable(publish_graph),"atomic complete-graph callback")
    _validate_bundle(bundle)
    require(patch_name in PATCH_NAMES,"one qualified real patch")
    node=_Node("N6_"+patch_name,{
        "kind":"complete_ordered_scalar_N6_residual_patch_v1",
        "complete":False,
        "patch":patch_name,
        "original_input_frequency":"n=4|j|",
        "original_input_normalization_power":[7,6],
        "retained_inverse_powers":[1,2,3,4,5],
        "exactly_cancelled_inverse_powers":[-2,-1,0],
        "terminal_inverse_power_before_input":4,
        "terminal_column_power_after_input":[-17,6],
        "terminal_band_power_after_signed_slot_bound":[-7,3],
        "exact_ordered_identities":dict(EXACT_IDENTITIES),
        "complete_operator_term_order":list(ORDERED_SCALAR_TERMS),
        "positive_low_books_are_not_subtracted_and_not_claimed_zero":True,
        "three_zero_degrees_use_full_WUA_transport_and_genuine_potential":True,
        "complete_final_even_mean_zero_P_retained":True,
        "deferred_outer_P_only_crossed_radial_scalars":True,
        "all_internal_projections_and_mean_functionals_retained":True,
        "terminal_I_and_J_receive_only_their_actual_complete_L2_bounds":True,
        "single_column_to_reflected_terminal_factor":2,
        "block_rows_use_full_signed_carrier_then_isometric_restriction":True,
        "WGS_amplitude_sup_bounds_not_relabelled_Wiener_A0":True,
        "old_scientific_targets_recomputed":0,
    },progress_state)
    calc=_FiniteCalculator(api,bundle["complete_patches"][patch_name],bundle,patch_name)
    node.progress["current_finite_call_counts"]=calc.call_counts
    node.records(api,("point_profile_records",),[
        ("single_signed_point_profile_upper",lambda:calc.point_single),
        ("whole_t_over_rho_comparison_upper",lambda:calc.point_comparison),
        ("complete_reflected_point_profile_upper",lambda:calc.point),
    ])
    def save_word(name,state):
        node.stage("ordered_word:"+name)
        if state is None:
            return
        path=("complete_operator_term_records",name)
        node.angles(api,path+("complete_retained_amplitude_ordinary_angles_0_4",),
                    _weighted_retained(api,state.poly))
        node.record(api,path+("complete_terminal_nminus4_upper",),state.tail)
        node.progress["completed_ordered_words"].append(name)
    amplitude,C6,pieces,retained,prezero=calc.compute(save_word)
    node.stage("complete_retained_polynomial_and_terminal")
    for degree in range(1,RETAINED_MAX_POWER+1):
        jet=retained.get(degree,api.zero(4,0,"exact_absent_inverse_power"))
        node.angles(api,("complete_retained_by_inverse_power",str(degree)),jet)
    amplitude_work=node.angles(api,("complete_retained_r_n_ordinary_angles_0_4",),amplitude)
    node.records(api,("complete_retained_profile_block_records",),[
        ("complete_retained_Hminus5_3_profile_block_upper",
         lambda:profile_receiver(api,bundle,patch_name,"-5/3",amplitude_work)),
        ("complete_retained_Hminus2_profile_block_upper",
         lambda:profile_receiver(api,bundle,patch_name,"-2",amplitude_work)),
    ])
    node.record(api,("complete_terminal_nminus4_upper",),C6)
    for degree in (-2,-1,0):
        jet=prezero.get(degree,api.zero(0,0,"absent_low_book"))
        node.record(api,("positive_low_degree_books_before_exact_identity",str(degree)),jet.c[0,0])
    node.put(("actual_finite_bookkeeping_counts",),
             dict(calc.call_counts,complete_J_parity_checks=calc.verified_parity_calls))
    saved=node.finish(publish_graph)
    return decode_ordered_residual_node(saved,patch_name,api),saved

def complete_true_jump_graph(bundle,api,publish_graph,progress_state):
    """The actual disjoint interface tuple, bounded without a new native array."""
    require(callable(publish_graph),"atomic complete-graph callback")
    _validate_bundle(bundle)
    info=bundle["true_jump_interface"]
    require(info["total_original_interfaces"]==ORIGINAL_INTERFACE_COUNT
            and info["each_subset_count_upper"]==ORIGINAL_INTERFACE_COUNT
            and info["all_original_interfaces_in_strict_patch"] is True
            and info["actual_subsets_disjoint_at_original_PW_cut"] is True
            and info["waist_cut_and_root_endpoints_are_not_artificial_jumps"] is True
            and info["j2_exactly_zero_only_for_the_continuous_completed_WUA_trial"] is True,
            "the complete original interface/receiver partition is not qualified")
    rlo=Fraction(1191984371497,5000000000000)
    rhi=Fraction(2383968743003,10000000000000)
    rc=Fraction(76285779072683,320000000000000)
    cpw=Fraction(2333968743003,10000000000000)
    require(Fraction(info["collar_rho_lower"])==rlo-rc
            and Fraction(info["strict_rho_lower"])==rlo-cpw
            and 0<cpw<rc<rlo<rhi,
            "true seam lower distances or original PW cut changed")
    node=_Node("true_jumps",{
        "kind":"complete_true_interface_jump_graph_v1",
        "complete":False,
        "exact_jump_identity":EXACT_IDENTITIES["jump"],
        "both_off_diagonal_signs_are_positive_i_epsilon":True,
        "h2_state_jump_is_exactly_zero":True,
        "h1_state_jump_is_same_J_of_complete_f_radial_jump":True,
        "Bext_KT_w0_is_C1_and_adds_no_jump":True,
        "original_total_interfaces":ORIGINAL_INTERFACE_COUNT,
        "original_genuine_polynomial_joins":ORIGINAL_GENUINE_JOIN_COUNT,
        "original_conservative_artificial_interfaces":ORIGINAL_ARTIFICIAL_INTERFACE_COUNT,
        "each_actual_disjoint_subset_count_upper":ORIGINAL_INTERFACE_COUNT,
        "actual_jump_tuple_contains_each_interface_once":True,
        "two_subset_count_envelopes_do_not_duplicate_the_actual_tuple":True,
        "new_potential_transition_or_estimation_split_introduces_no_jump":True,
        "no_new_root_discrepancy_relabelled_as_a_seam":True,
        "no_radial_length_factor_on_impulses":True,
        "collar_input_window":"H^-2/3 plus H^-1; second state jump exactly zero",
        "strict_input_window":"H^-1 plus H^-1; first jump measured through I and second jump exactly zero",
        "original_PW_cut":str(cpw),
        "old_scientific_targets_recomputed":0,
    },progress_state)
    patch=bundle["complete_patches"]["strict"]
    g=patch["geometry"];m,p=4,0
    node.stage("full_forcing_difference_and_exact_jump_matrix")
    T=g["T_absolute_jet"].part(m,p)
    tl=_typed_lower(api,g["strict_T_lower"],"strict true-seam |T| lower")
    invT=api.reciprocal(T,tl,m,p,"strict_true_jump_T_inverse")
    x=g["X_phi_jet"].part(m,p);y=g["T_phi_absolute_jet"].part(m,p)
    Q=g["Q"].part(m,p)
    matrix=api.add(x,api.scale(y,api.ex(2)),api.mul(x,invT,m=m,p=p),
                   m=m,p=p,label="complete_jump_matrix_entry_sum")
    node.angles(api,("complete_jump_matrix_ordinary_angles_0_4",),matrix)
    # Sum the full one-sided forcing bounds; never subtract two norm uppers.
    one_side=api.add(g["Fa"],g["Fb"],m=m,p=p,
                    label="complete_one_sided_forcing_pair")
    two_sides=api.scale(one_side,api.ex(2))
    node.angles(api,("complete_full_forcing_two_side_ordinary_angles_0_4",),two_sides)
    jump=api.scale(api.mul(Q,matrix,two_sides,m=m,p=p),
                   api.ex(1)/api.ex(2),label="complete_true_w1_radial_jump")
    jump_work=node.angles(api,("complete_w1_radial_jump_ordinary_angles_0_4",),jump)
    node.stage("complete_jump_profile_and_original_impulse_receivers")
    path=("new_complete_records",)
    cr53=node.record(api,path+("complete_jump_Hminus5_3_profile_block_upper",),
                    profile_receiver(api,bundle,"strict","-5/3",jump_work))
    cr2=node.record(api,path+("complete_jump_Hminus2_profile_block_upper",),
                   profile_receiver(api,bundle,"strict","-2",jump_work))
    rho_c=node.lower(api,("complete_positive_distance_lowers",
                        "complete_collar_seam_rho_lower"),
                     api.ex(rlo-rc),"all collar seam root distances")
    rho_s=node.lower(api,("complete_positive_distance_lowers",
                        "complete_strict_seam_rho_lower"),
                     api.ex(rlo-cpw),"all strict seam root distances")
    j=patch["same_J"]
    gm53=_typed_upper(api,j["Gamma_minus5_3"])
    gm2=_typed_upper(api,j["Gamma_minus2"]);ci=_typed_upper(api,j["cI"])
    two16=positive_power(api,api.ex(2),1,6)
    node.record(api,path+("complete_collar_jump_sum_upper",),
        api.ex(ORIGINAL_INTERFACE_COUNT)*two16*gm53*cr53*
        positive_power(api,rho_c,-1,4,"true collar seam rho"))
    node.record(api,path+("complete_strict_jump_sum_upper",),
        api.ex(ORIGINAL_INTERFACE_COUNT)*two16*ci*gm2*cr2*
        positive_power(api,rho_s,-1,4,"true strict seam rho"))
    saved=node.finish(publish_graph)
    return decode_true_jump_node(saved,api),saved

def complete_negative_reception_graph(bundle,residual_by_patch,jumps,
                                      old_receiver_records,api,publish_graph,progress_state):
    """The same whole negative ordinary-source plus all-jump operator."""
    require(callable(publish_graph),"atomic complete-graph callback")
    _validate_bundle(bundle)
    require(set(residual_by_patch)==set(PATCH_NAMES),"both complete N6 patch graphs")
    require(set(old_receiver_records)=={"C_O","C_R","C_1"},
            "the three complete original received maps, without recomputation")
    node=_Node("negative_reception",{
        "kind":"complete_original_negative_source_and_jump_reception_v1",
        "complete":False,
        "input_window":"original natural high reflected H^-4/3, n=4|j|>=388",
        "output_window":"the original complete PW/SP waist state Y0",
        "copied_complete_original_receiver_records":dict(old_receiver_records),
        "source_block_powers":{"collar":[-5,3],"strict":[-2,1]},
        "dyadic_gain_after_original_input_Hminus4_3":[[1,3],[2,3]],
        "physical_mean_source_and_feedback_in_M_terms_retained":True,
        "second_ordinary_source_and_second_state_jump_exactly_zero":True,
        "ordinary_radial_dr_and_original_receiver_cut_retained":True,
        "orthogonality_used_only_between_original_input_bands":True,
        "full_low_output_leakage_and_two_evolving_means_retained":True,
        "no_root_trace_window_substituted_for_the_mixed_source_window":True,
        "positive_correction_root_finite_and_endpoint_terms_are_separate":True,
        "whole_waist_error_or_incoming_inverse_claimed":False,
        "old_scientific_targets_recomputed":0,
    },progress_state)
    old={k:api.read_up(v) for k,v in old_receiver_records.items()}
    mean=bundle["complete_mean"]
    CF=_typed_upper(api,mean["CF"]);Z=_typed_upper(api,mean["Z"])
    two16=positive_power(api,api.ex(2),1,6)
    patch_work={}
    for name in PATCH_NAMES:
        node.stage("complete_B_T_M_patch:"+name)
        patch=bundle["complete_patches"][name]
        j=patch["same_J"];km=patch["mean"];r=residual_by_patch[name]
        J0=api.read_up(j["J0_upper"])
        gm53=_typed_upper(api,j["Gamma_minus5_3"])
        gm2=_typed_upper(api,j["Gamma_minus2"]);ci=_typed_upper(api,j["cI"])
        k0=_typed_upper(api,km["k0"]);rm=_typed_upper(api,km["Rm0"])
        ik=_typed_upper(api,km["Ik0"]);irm=_typed_upper(api,km["IRm0"])
        patch_work[name]=node.records(api,("complete_patch_B_T_M_records",name),[
            ("B_c_upper",lambda:two16*gm53*r["C_r_minus5_3"]),
            ("B_t_upper",lambda:two16*ci*gm2*r["C_r_minus2"]),
            ("T_c_upper",lambda:J0*r["C6"]),
            ("T_t_upper",lambda:J0*r["C6"]/api.ex(4)),
            ("M_c_upper",lambda:CF*k0+Z*rm),
            ("M_t_upper",lambda:CF*ik+Z*irm),
        ])
    node.stage("complete_patch_union_and_radial_measures")
    union=node.records(api,("complete_collar_patch_union_records",),[
        ("complete_collar_B_union_upper",
         lambda:max_upper(api,(v["B_c_upper"] for v in patch_work.values()))),
        ("complete_collar_T_union_upper",
         lambda:max_upper(api,(v["T_c_upper"] for v in patch_work.values()))),
        ("complete_collar_M_union_upper",
         lambda:max_upper(api,(v["M_c_upper"] for v in patch_work.values()))),
    ])
    ell_plus=api.ex(Fraction(1,200))
    cpw=api.ex(Fraction(2333968743003,10000000000000))
    ellminus_exact=Fraction(1191984371497,5000000000000)-Fraction(2333968743003,10000000000000)
    ellminus=node.lower(api,("complete_original_collar_length_lower",),
                        api.ex(ellminus_exact),"original collar length lower")
    N=api.ex(N0)
    powers=node.records(api,("complete_power_and_radial_measure_records",),[
        ("N_minus5_6_upper",lambda:positive_power(api,N,-5,6)),
        ("N_minus5_3_upper",lambda:positive_power(api,N,-5,3)),
        ("N_minus1_2_upper",lambda:positive_power(api,N,-1,2)),
        ("N_minus4_3_upper",lambda:positive_power(api,N,-4,3)),
        ("sqrt_two_upper",lambda:positive_power(api,api.ex(2),1,2)),
        ("ell_plus_one_fourth_upper",lambda:positive_power(api,ell_plus,1,4)),
        ("sqrt_ell_plus_upper",lambda:positive_power(api,ell_plus,1,2)),
        ("ell_minus_negative_fourth_upper",lambda:positive_power(api,ellminus,-1,4)),
    ])
    node.stage("complete_ordinary_sources")
    col=node.record(api,("complete_ordinary_source_records",
                        "complete_collar_ordinary_source_upper"),
        powers["sqrt_two_upper"]*powers["ell_plus_one_fourth_upper"]*(
            union["complete_collar_B_union_upper"]+
            union["complete_collar_T_union_upper"]*powers["N_minus5_6_upper"])+
        powers["sqrt_ell_plus_upper"]*union["complete_collar_M_union_upper"]*
            powers["N_minus5_3_upper"])
    st=node.record(api,("complete_ordinary_source_records",
                       "complete_strict_ordinary_primitive_source_upper"),
        cpw*(powers["ell_minus_negative_fourth_upper"]*(
            patch_work["strict"]["B_t_upper"]+
            patch_work["strict"]["T_t_upper"]*powers["N_minus1_2_upper"])+
            patch_work["strict"]["M_t_upper"]*powers["N_minus4_3_upper"]))
    node.stage("input_dyadic_sum_and_complete_received_map")
    dyadic_work={}
    for numerator,label in ((1,"one_third"),(2,"two_thirds")):
        decay=positive_power(api,N,-numerator,3)
        ratio=positive_power(api,api.ex(2),-2*numerator,3)
        denominator=api.lower(api.ex(1)-ratio,"complete dyadic input square-sum denominator")
        value=decay*positive_power(api,denominator,-1,2)
        dyadic_work[label]=node.record(api,("complete_input_dyadic_square_sum_records",label),value)
    prefactor=node.record(api,("complete_input_Bessel_prefactor_upper",),
                          positive_power(api,api.ex(3),4,3))
    received=node.records(api,("complete_received_part_records",),[
        ("complete_received_collar_source_and_jump_upper",
         lambda:old["C_O"]*col+old["C_R"]*jumps["C_col_J"]),
        ("complete_received_strict_source_and_jump_upper",
         lambda:old["C_1"]*(st+jumps["C_st_J"])),
    ])
    node.record(api,("complete_negative_source_and_all_jump_upper",),
        prefactor*(received["complete_received_collar_source_and_jump_upper"]*
                    dyadic_work["one_third"]+
                   received["complete_received_strict_source_and_jump_upper"]*
                    dyadic_work["two_thirds"]))
    saved=node.finish(publish_graph)
    return decode_negative_reception_node(saved,api),saved


# Pure record readers. The driver validates the entire frozen shape, immutable
# binding, dependency hashes and original scope before reusing a complete node.
# They perform no target construction and never call the finite calculator.
def decode_ordered_residual_node(saved,patch_name,api):
    require(saved.get("kind")=="complete_ordered_scalar_N6_residual_patch_v1"
            and saved.get("complete") is True and saved.get("patch")==patch_name
            and patch_name in PATCH_NAMES,"not the same complete residual patch")
    require(saved["complete_final_even_mean_zero_P_retained"] is True
            and saved["all_internal_projections_and_mean_functionals_retained"] is True,
            "incomplete retained projection/mean scope")
    return {
        "C_r_minus5_3":api.read_up(saved["complete_retained_profile_block_records"]
                                 ["complete_retained_Hminus5_3_profile_block_upper"]),
        "C_r_minus2":api.read_up(saved["complete_retained_profile_block_records"]
                                ["complete_retained_Hminus2_profile_block_upper"]),
        "C6":api.read_up(saved["complete_terminal_nminus4_upper"]),
    }

def decode_true_jump_node(saved,api):
    require(saved.get("kind")=="complete_true_interface_jump_graph_v1"
            and saved.get("complete") is True,"not a complete true jump graph")
    require(saved["original_total_interfaces"]==ORIGINAL_INTERFACE_COUNT
            and saved["actual_jump_tuple_contains_each_interface_once"] is True,
            "a different original jump tuple")
    return {
        "C_col_J":api.read_up(saved["new_complete_records"]["complete_collar_jump_sum_upper"]),
        "C_st_J":api.read_up(saved["new_complete_records"]["complete_strict_jump_sum_upper"]),
    }

def decode_negative_reception_node(saved,api):
    require(saved.get("kind")=="complete_original_negative_source_and_jump_reception_v1"
            and saved.get("complete") is True,"not a complete original negative receiver")
    require(saved["whole_waist_error_or_incoming_inverse_claimed"] is False
            and saved["positive_correction_root_finite_and_endpoint_terms_are_separate"] is True,
            "a negative subtotal cannot be relabelled as the whole operator")
    return {"C_negative":api.read_up(saved["complete_negative_source_and_all_jump_upper"])}
