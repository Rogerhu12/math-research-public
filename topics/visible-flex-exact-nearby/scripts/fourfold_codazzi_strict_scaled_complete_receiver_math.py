"""WSM finishing: complete new strict ordered residual and same whole receiver.

No entry point, I/O, FLINT import, old producer import or old target invocation.
The complete finite ordered calculus below is written in this NEW module and
takes only the new per-index working coefficients. Its algebraic identities
are the already proved WUA/O/WNR identities, not a call to their old producer.

The full even-mean-zero projection precedes the SAME original angular J.
All ten words, all internal means, five retained powers and every terminal
remain. The existing local patch, physical mean solution, all 3070 jumps,
positive/root terms, four endpoints and whole finite factors are read only.
No high-input norm, physical inverse, smallness or finite determinant is claimed.
"""
from __future__ import annotations
import copy
from fractions import Fraction
from math import factorial

N0=388
MAX_PRIMITIVE_STEPS=6
RETAINED_MAX_POWER=5
TERMINAL_POWER=4
PW_CUT=Fraction(2333968743003,10000000000000)
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
        # This is the already saved COMPLETE same reflected point budget.
        # Its original whole t/rho comparison and factor two are not rerun.
        self.point = api.read_up(profile["complete_reflected_point_upper"][patch_name])
        self.point_single = api.read_up(profile["single_signed_pointwise_upper"][patch_name])
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


def _angle_records(sink,api,path,jet):
    jet.need(4,0)
    values=[]
    for q in range(5):
        values.append(sink.emit(list(path)+["angle_"+str(q)],
                               api.ex(factorial(q))*jet.c[0,q]))
    return values

def complete_new_strict_N6(session,saved_profile,support,scalar_api,publish_graph,progress_state):
    """One complete new strict residual: ten ordered words and every terminal."""
    name="strict_complete_ordered_N6"
    require(name not in session.public_completed,"no complete strict target replay")
    sink=support.NodeSink(scalar_api,name,progress_state,publish_graph)
    session.progress=progress_state
    progress_state["current_stage"]="finite_private_strict_source_prework"
    algebra=support.OrdinaryAlgebra(scalar_api)
    bundle=support.read_complete_strict_bundle(
        session,saved_profile,scalar_api,algebra.factory)
    require(set(bundle["complete_patches"])=={"strict"}
            and bundle["block_rows_include_complete_reflected_assembly"] is True,
            "one complete strict patch and full signed profile")
    sink.doc.update({
      "conclusion_kind":"complete_new_per_index_strict_ordered_scalar_N6",
      "patch":"strict","original_input_frequency":"n=4|j|",
      "original_input_normalization_power":[7,6],
      "retained_inverse_powers":[1,2,3,4,5],
      "exactly_cancelled_inverse_powers":[-2,-1,0],
      "terminal_inverse_power_before_input":4,
      "terminal_column_power_after_input":[-17,6],
      "exact_ordered_identities":dict(EXACT_IDENTITIES),
      "complete_operator_term_order":list(ORDERED_SCALAR_TERMS),
      "angular_predecessor_identity":copy.deepcopy(session.inputs.angular_source_identity),
      "relative_angular_predecessor_identity":copy.deepcopy(session.inputs.relative_angular_source_identity),
      "ordinary_same_function_fallback_routes":copy.deepcopy(
          bundle["ordinary_same_function_fallback_routes"]),
      "private_mixed_tables_published_as_certificate":False,
      "all_complete_operator_words_and_terminals_retained":True,
      "complete_final_even_mean_zero_projection_before_same_J":True,
      "positive_low_books_are_not_subtracted_and_not_claimed_zero":True,
      "complete_genuine_potential_in_full_transport_cancellation":True,
      "single_reflected_point_budget_is_old_whole_record":True,
      "old_point_comparison_and_factor_two_recomputed":False,
      "same_old_local_mean_jump_and_endpoint_targets_not_evaluated":True,
    })
    sink.copy("complete_original_reflected_point_upper",
              bundle["complete_reflected_point_upper"]["strict"])
    calc=_FiniteCalculator(algebra,bundle["complete_patches"]["strict"],bundle,"strict")
    progress_state["current_finite_call_counts"]=calc.call_counts
    progress_state["completed_ordered_words"]=[]
    def save_word(word,state):
        progress_state["current_stage"]="ordered_word:"+word
        if state is None:
            return
        _angle_records(sink,algebra,
          ["complete_operator_term_records",word,"retained_ordinary_angles_0_4"],
          _weighted_retained(algebra,state.poly))
        sink.emit(["complete_operator_term_records",word,"complete_terminal_nminus4_upper"],
                  state.tail)
        progress_state["completed_ordered_words"].append(word)
    unused_amplitude,terminal,pieces,retained,prezero=calc.compute(save_word)
    require(tuple(pieces)==ORDERED_SCALAR_TERMS,"all ten actual ordered words")
    for power in range(1,6):
        jet=retained.get(power,algebra.zero(4,0,"exact_absent_inverse_power"))
        _angle_records(sink,algebra,
            ["complete_retained_by_inverse_power",str(power)],jet)
    sink.emit(["complete_terminal_nminus4_upper"],terminal)
    for power in (-2,-1,0):
        jet=prezero.get(power,algebra.zero(0,0,"exact_absent_low_book"))
        sink.emit(["positive_low_degree_books_before_exact_identity",str(power)],jet.c[0,0])
    sink.doc["actual_finite_bookkeeping_counts"]=dict(
        calc.call_counts,complete_J_parity_checks=calc.verified_parity_calls)
    saved=sink.finish({
      "whole_positive_norm_subtraction_used":False,
      "retained_coefficients_and_all_exact_terminals_are_complete":True,
      "ordinary_normalization_and_same_function_fallback_precede_ordered_calculus":True,
      "full_ordered_means_not_inferred_from_placeholder_names":True,
      "scalar_sup_not_relabelled_A0":True,
      "independent_positive_root_and_waist_terms_not_paid_by_this_node":True})
    session.public_completed.add(name)
    return saved

def _at(value,path):
    for part in path:
        value=value[part]
    return value

def _complete_old_selected(wrt,which):
    require(which in ("whole","reduced"),"same original error coordinate")
    choice=wrt["whole_candidate_choices"][which]
    require(choice["all_candidates_retained"] is True
            and choice["prior_wins_equal_saved_upper"] is True
            and choice["selected_record_path"] in
                (choice["new_record_path"],choice["prior_record_path"]),
            "whole original candidate selection")
    record=_at(wrt,choice["selected_record_path"])
    require(isinstance(record,dict) and set(record)=={"ball"},"full selected original record")
    return record,list(choice["selected_record_path"])

def complete_new_whole_receiver(original_documents,admission,saved_profile,saved_N6,
                                support,api,publish_graph,progress_state):
    """Same full operator: only new strict coefficients/profile are substituted."""
    require(admission.get("complete") is True
            and admission.get("all_complete_original_bytes_and_scopes_verified") is True,
            "complete immutable originals")
    for doc,name in ((saved_profile,"strict_complete_angular_profile"),
                     (saved_N6,"strict_complete_ordered_N6")):
        require(doc["complete"] is True and doc["kind"]==support.NODE_KIND
                and doc["node_name"]==name and doc["retained_scope"]==support.complete_scope(),
                "complete published same-domain predecessor")
    require(saved_N6["all_complete_operator_words_and_terminals_retained"] is True
            and saved_N6["complete_final_even_mean_zero_projection_before_same_J"] is True,
            "complete same ordered scalar source")
    wrt=original_documents["prior_WRT"]
    require(wrt["kind"]=="complete_exact_retained_profile_terminal_refinement"
            and wrt["complete"] is True and wrt["proved"] is True
            and wrt["actual_returncode"]==0,
            "complete current WRT whole operator predecessor")
    require(wrt["parameters"]["input_order"]==[-4,3]
            and wrt["parameters"]["original_PW_cut"]==str(PW_CUT)
            and wrt["parameters"]["original_true_interfaces"]==3070
            and wrt["parameters"]["physical_mean_coordinates"]==2
            and wrt["retained_scope"]["complete_WMT_physical_mean_and_both_stored_means_read_only"] is True
            and wrt["retained_scope"]["all_four_waist_endpoints_and_positive_root_terms_read_only"] is True,
            "same original natural domain, PW cut and complete remaining tuple")
    sink=support.NodeSink(api,"strict_complete_whole_receiver",progress_state,publish_graph)
    sink.doc.update({
      "conclusion_kind":"complete_new_strict_candidate_for_same_whole_and_reduced_waist_row",
      "input_order":[-4,3],"original_PW_cut":str(PW_CUT),
      "original_true_interfaces":3070,"physical_mean_coordinates":2,
      "old_complete_remaining_tuple_not_recomputed":True,
      "entire_local_patch_and_current_local_receiver_fees_read_only":True,
      "whole_candidate_operator":wrt["parameters"]["same_operator_domain"],
      "same_complete_genuine_trial":True,
      "ordinary_dr_lengths_only_on_ordinary_sources":True,
      "no_jump_length_factor":True,
      "Calg_only_in_whole_Dinfinity_only_in_reduced":True,
      "full_finite_factors_mean_rows_Theta_nu_and_radial_head_retained":True,
      "finite_signed_inverse_or_smallness_claimed":False})
    original=wrt["copied_original_scalar_records"]
    old={}
    needed=(
      "strict_reflected_point_profile","strict_Jminus5_3","strict_IJminus2","strict_J0",
      "sqrt_two_upper","ell_plus_one_fourth_upper","sqrt_ell_plus_upper","collar_raw_mean",
      "N_minus5_3_upper","ell_minus_negative_fourth_upper","strict_primitive_mean",
      "N_minus4_3_upper","C_O","C_R","jump_collar","C_1","jump_strict",
      "dyadic_one_third","dyadic_two_thirds","Bessel_prefactor",
      "Rplus","waist_endpoint","RF","Lrec","Calg","D_infinity")
    for key in needed:
        old[key]=sink.copy(key,original[key])
    old_graphs=wrt["complete_new_graphs"]
    for key in ("local_B_c_upper","local_T_c_upper"):
        old[key]=sink.copy(key,old_graphs["complete_actual_inverse_and_patch_union"]["new_records"][key])
    for key in ("two_one_sixth_upper","dyadic_one_sixth_upper"):
        old[key]=sink.copy(key,old_graphs["complete_terminal_summation_constants"]["new_records"][key])
    prior_paths={}
    for which in ("whole","reduced"):
        record,path=_complete_old_selected(wrt,which)
        old["prior_"+which]=sink.copy("prior_"+which,record)
        prior_paths[which]=path
    r=saved_N6["new_records"]
    angles=[]
    for q in range(5):
        v1=api.read_up(r["complete_retained_by_inverse_power"]["1"]["angle_"+str(q)])
        v2=api.read_up(r["complete_retained_by_inverse_power"]["2"]["angle_"+str(q)])
        angles.append(sink.emit(["strict_regrouping","ordinary_angles_0_4","angle_"+str(q)],
                                v1+v2/api.ex(N0)))
    weights=saved_profile["new_records"]["full_output_block_weights"]
    retained={}
    for window in ("five_thirds","two"):
        retained[window]=sink.emit(
          ["strict_regrouping","complete_retained_"+window+"_profile_upper"],
          sum_upper(api,(api.read_up(weights[window]["angle_"+str(q)])*angles[q]
                         for q in range(5))))
    moved=sum_upper(api,(
        api.read_up(r["complete_retained_by_inverse_power"][str(k)]["angle_0"])
           /api.ex(N0)**(k-3) for k in (3,4,5)))
    C3=sink.emit(["strict_regrouping","complete_terminal_nminus3_upper"],
        api.read_up(r["complete_terminal_nminus4_upper"])/api.ex(N0)
        +old["strict_reflected_point_profile"]*moved)
    Bc=sink.emit(["same_inverse_and_union","strict_B_c_upper"],
        old["two_one_sixth_upper"]*old["strict_Jminus5_3"]*retained["five_thirds"])
    Bt=sink.emit(["same_inverse_and_union","strict_B_t_upper"],
        old["two_one_sixth_upper"]*old["strict_IJminus2"]*retained["two"])
    Tc=sink.emit(["same_inverse_and_union","strict_T_c_upper"],old["strict_J0"]*C3)
    Tt=sink.emit(["same_inverse_and_union","strict_T_t_upper"],Tc/api.ex(4))
    Bu=sink.emit(["same_inverse_and_union","complete_collar_B_union_upper"],
        max_upper(api,(Bc,old["local_B_c_upper"])))
    Tu=sink.emit(["same_inverse_and_union","complete_collar_T_union_upper"],
        max_upper(api,(Tc,old["local_T_c_upper"])))
    collar=sink.emit(["original_radial_and_receiving","complete_collar_retained_and_mean_ordinary_upper"],
        old["sqrt_two_upper"]*old["ell_plus_one_fourth_upper"]*Bu
        +old["sqrt_ell_plus_upper"]*old["collar_raw_mean"]*old["N_minus5_3_upper"])
    strict=sink.emit(["original_radial_and_receiving","complete_strict_retained_and_mean_ordinary_upper"],
        api.ex(PW_CUT)*(old["ell_minus_negative_fourth_upper"]*Bt
                       +old["strict_primitive_mean"]*old["N_minus4_3_upper"]))
    Rc=sink.emit(["original_radial_and_receiving","complete_collar_retained_mean_and_jumps_received_upper"],
        old["C_O"]*collar+old["C_R"]*old["jump_collar"])
    Rs=sink.emit(["original_radial_and_receiving","complete_strict_retained_mean_and_jumps_received_upper"],
        old["C_1"]*(strict+old["jump_strict"]))
    Ec=sink.emit(["original_radial_and_receiving","complete_collar_terminal_received_upper"],
        old["C_O"]*old["sqrt_two_upper"]*old["ell_plus_one_fourth_upper"]*Tu)
    Es=sink.emit(["original_radial_and_receiving","complete_strict_terminal_received_upper"],
        old["C_1"]*api.ex(PW_CUT)*old["ell_minus_negative_fourth_upper"]*Tt)
    Et=sink.emit(["original_radial_and_receiving","complete_terminal_received_sum_upper"],Ec+Es)
    Nc=sink.emit(["new_negative_receiver","complete_collar_dyadic_contribution_upper"],
        Rc*old["dyadic_one_third"])
    Ns=sink.emit(["new_negative_receiver","complete_strict_dyadic_contribution_upper"],
        Rs*old["dyadic_two_thirds"])
    Nt=sink.emit(["new_negative_receiver","complete_terminal_dyadic_contribution_upper"],
        Et*old["dyadic_one_sixth_upper"])
    negative=sink.emit(["new_negative_receiver","complete_same_negative_error_upper"],
        old["Bessel_prefactor"]*(Nc+Ns+Nt))
    nonroot=sink.emit(["whole_and_reduced","complete_nonroot_source_sum_upper"],
        old["Rplus"]+negative+old["waist_endpoint"])
    allsource=sink.emit(["whole_and_reduced","complete_all_source_sum_upper"],nonroot+old["RF"])
    received=sink.emit(["whole_and_reduced","complete_whole_received_source_upper"],
        old["Lrec"]*allsource)
    whole=sink.emit(["whole_and_reduced","complete_same_whole_error_upper"],old["Calg"]+received)
    redreceived=sink.emit(["whole_and_reduced","complete_reduced_received_source_upper"],
        old["Lrec"]*nonroot)
    reduced=sink.emit(["whole_and_reduced","complete_same_reduced_error_upper"],
        old["D_infinity"]+redreceived)
    choices={}
    for which,value in (("whole",whole),("reduced",reduced)):
        choose_new=bool(value<old["prior_"+which])
        new_path=["new_records","whole_and_reduced","complete_same_"+which+"_error_upper"]
        prior_path=["copied_original_records","prior_"+which]
        choices[which]={
          "selected_label":"new_complete_strict_per_index_candidate" if choose_new
                           else "prior_complete_WRT_selected",
          "selected_record_path":new_path if choose_new else prior_path,
          "new_record_path":new_path,"prior_record_path":prior_path,
          "prior_source_record_path":prior_paths[which],
          "prior_wins_equal_saved_upper":True,"both_complete_candidates_retained":True}
    sink.doc["whole_candidate_choices"]=choices
    return sink.finish({
      "new_local_mean_jump_positive_root_or_endpoint_targets":0,
      "no_old_negative_or_whole_upper_subtraction":True,
      "actual_reflected_point_factor_two_not_paid_twice":True,
      "terminal_one_sixth_sum_read_from_complete_prior_WRT":True,
      "complete_whole_and_reduced_compared_separately_same_operator":True,
      "same_angular_J_and_original_PW_C1_CO_CR_windows":True,
      "old_successful_graphs_and_original_failed_parent_status_preserved":True})
