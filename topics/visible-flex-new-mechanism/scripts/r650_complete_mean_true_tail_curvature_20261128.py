#!/usr/bin/env python3
"""Whole cap-to-mouth curvature of the same R643 normalized trial (R650).

Consume the existing R648 connection object and both actual paid receipts.
All new operations are outward inequalities. Old germ transfer, quadrature,
field evaluation, Jacobians, finite primitives, and stencil work stay paid.
"""
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SOURCE648 = 'r648_complete_mean_true_tail_connection_20261128.py'
SOURCE649 = 'r649_complete_offsolution_curvature_20261128.py'
SHA648 = '82258e61964f97f89c27c192c85acb1d52f43b63a486dcc53fde2bd3cefb875f'
SHA649 = 'a2f765c580d7209b8549f10547d17c39b71a84b33dcbb0d9008311017e2a23fb'
for name, digest in ((SOURCE648, SHA648), (SOURCE649, SHA649)):
    if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest:
        raise ValueError('the published tail or curvature formulas differ')
import r648_complete_mean_true_tail_connection_20261128 as connection
import r649_complete_offsolution_curvature_20261128 as curvature

paid, bounds, I = connection.paid, connection.bounds, connection.I
upper = bounds.upper
read = paid.supplied_interval
SCHEMA = 'r650-complete-true-tail-actual-normalized-curvature-v1'


class Poly:
    """An upper bound with nonnegative coefficients in the true variable u."""
    def __init__(self, coefficients):
        self.c = tuple(upper(x if isinstance(x, I) else I(x)) for x in coefficients)

    def __add__(self, other):
        other = pol(other)
        size = max(len(self.c), len(other.c))
        result = [I(0)] * size
        for seq in (self.c, other.c):
            for i, a in enumerate(seq):
                result[i] = result[i] + a
        return Poly(result)

    __radd__ = __add__

    def __mul__(self, other):
        other = pol(other)
        result = [I(0)] * (len(self.c) + len(other.c) - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                result[i+j] = result[i+j] + a*b
        return Poly(result)

    __rmul__ = __mul__

    def __truediv__(self, denominator):
        denominator = denominator if isinstance(denominator, I) else I(denominator)
        bounds.positive(denominator)
        return self * (1 / denominator)

    def whole(self, tail, power):
        """sup W^power P on u>=U, paid termwise at each actual maximum."""
        if not isinstance(power, int) or power < 1:
            raise ValueError('polynomial absorption needs a strictly positive W power')
        result = I(0)
        for k, a in enumerate(self.c):
            # The rational k/power need not be exactly representable.
            stationary = I(k) / I(power)
            x = I(max(tail.U.lo, stationary.lo), max(tail.U.lo, stationary.hi))
            result += a * (x ** k) * bounds.exp_i(-power*x)
        return upper(tail.A ** power * result)


def pol(value):
    return value if isinstance(value, Poly) else Poly((value,))


def sym(interval):
    return I(-interval.hi, interval.hi)


def basis_derivative(knots, i, degree, order):
    if order == 0:
        return I(1)
    result = I(0)
    for left in (i, i+1):
        if knots[left] == knots[left+degree]:
            continue
        width = paid.literal_interval(knots[left+degree])-paid.literal_interval(knots[left])
        bounds.positive(width)
        result += degree * basis_derivative(knots, left, degree-1, order-1) / width
    return upper(result)


class CompleteTrueTailCurvature:
    def __init__(self, existing):
        bounds.public_only()
        module = sys.modules.get(type(existing).__module__)
        if (module is None or type(existing).__name__ != 'CompleteTrueTailConnection'
                or Path(module.__file__).resolve() != (HERE / SOURCE648).resolve()):
            raise ValueError('the already-used R648 object for this same actual tail is required')
        self.conn, self.tail = existing, existing.tail
        self.counts = {'new_third_jet_reference_passes': 0, 'new_angular_third_jet_passes': 0,
                       'new_mean_four_Gaussian_third_jet_sums': 0, 'new_whole_tail_curvature_calls': 0}
        ell = self.tail.ell
        self.L1 = Poly((0, 0, 3, 1)) / ell
        self.L2 = Poly((0, 0, 0, 6, 4, 1)) / (ell ** 2)
        self.LW2 = self.L1*self.L1 + self.L2
        self.gauss3 = {}
        self.ref3 = self._reference()
        self.seed3 = self._angular(self.tail.response)

    def _germ3(self, j, C):
        rc = self.tail.rc
        return (self.L1*(1+j*j/rc+j*j/rc**2) + self.L2*(1+j*j/rc))*C

    def _gaussian3(self, k, existing_column):
        if k in self.gauss3:
            return self.gauss3[k]
        tail = self.tail
        u, ell = tail.U, tail.ell
        a = paid.literal_interval(tail.joint.owned.policy['tail_gaussian_denominator'])
        bounds.positive(a)
        if (9/u-2*u/a+3).hi >= 0 or existing_column['degree'] != k:
            raise ArithmeticError('whole Gaussian third-jet monotonicity is unresolved')
        d1 = (k*u+2*u**3/a)/ell
        d2 = (k*u**2+6*u**4/a)/ell**2
        d3 = (2*k*u**3+24*u**5/a)/ell**3
        K0 = existing_column['over_W_threejet_upper'][0]
        self.gauss3[k] = upper((d1**3+3*d1*d2+d3)*K0)
        return self.gauss3[k]

    def _reference(self):
        c, tail = self.conn, self.tail
        model = tail.model
        original = model.old.old
        literal = lambda text: json.loads(text, parse_float=Decimal)
        legacy = literal(model.driver.weak.RAW_Q_JSON)
        knots = literal(model.driver.weak.RAW_KNOT_JSON)
        ref = literal(model.original_q_json)
        nb = int(original.nb)
        count = len(knots)-6
        if (int(original.bs.k) != 5 or nb != count+4
                or paid.CurrentModelTailAnchor._snapshot(tail) != c.source_snapshot):
            raise ValueError('actual source coefficients, full knots or supports differ')
        previous = c.reference_extension_receipt
        normal = tail.contract['old_envelope_and_force_normalizations']
        scales = [read(x) for x in normal['mode_height_scales']]
        C = read(normal['envelope_scale'])
        degree = 2+2*read(tail.contract['physical_alpha'])
        width = read(tail.contract['physical_R'])-tail.mouth
        u, ell, gamma = tail.U, tail.ell, I(1)/10000
        bounds.positive(C, width, *scales)
        if (15/u-4*gamma*u**3/ell**4+3).hi >= 0:
            raise ArithmeticError('quartic envelope third-jet monotonicity unresolved')
        d1 = 4*gamma*u**5/ell**5+degree/width
        d2 = 20*gamma*u**6/ell**6+degree/width**2
        d3 = 120*gamma*u**7/ell**7+2*degree/width**3
        envelope = tail.reference_construction_receipt['old_envelope_bound']
        G3 = upper((d1**3+3*d1*d2+d3)*envelope['quartic_value_over_W'])
        B3 = G3
        for j, scale in zip((2, 4, 6, 8), scales):
            cj = tail.seed_ratio[j]
            B3 += (self._germ3(j, cj)*(2*cj) + 6*cj**2).whole(tail, 1)/scale**2
        B3 = upper(B3/C)
        B0, B1 = envelope['value_over_W'], envelope['radial_derivative_over_W']
        B2 = previous['new_complete_envelope_second_radial_ratio']
        B = (B0, B1, B2, B3)
        basis = tail.original_basis_receipt
        Q = (basis['whole_tail_basis_value_bounds'], basis['whole_tail_basis_derivative_bounds'],
             previous['all_original_spline_second_derivative_bounds'],
             [basis_derivative(knots, i, 5, 3) for i in range(count)]+[I(0)]*4)
        # All four pre-tanh modes including the canonical512 subtraction.
        # Keep the individual jets here because a third composition derivative
        # needs their mixed products. No second-jet field/ODE is re-evaluated.
        amp = tail.amplitude
        modes = (2, 4, 6, 8)
        jets = {(a,b): pol(0) for a,b in ((1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2))}
        for m, j in enumerate(modes):
            coef = amp if m == 0 else paid.absolute(amp*paid.literal_interval(legacy[m]))
            germ = tail.seed_ratio[j]
            vv = [pol(coef*germ) for _ in range(3)]+[self._germ3(j, germ)*coef]
            for i in range(nb):
                ci = paid.absolute(amp*paid.literal_interval(legacy[4+m*nb+i]))
                q0,q1,q2,q3 = [row[i] for row in Q]
                products = (B[0]*q0, B[1]*q0+B[0]*q1, B[2]*q0+2*B[1]*q1+B[0]*q2,
                            B[3]*q0+3*B[2]*q1+3*B[1]*q2+B[0]*q3)
                for n in range(4):
                    vv[n] += products[n]*ci
            for a,b in jets:
                jets[a,b] += vv[a]*j**b
        vr,vq,vrr,vrt,vtt = (jets[i] for i in ((1,0),(0,1),(2,0),(1,1),(0,2)))
        sigma, W = I(3)/20, tail.W_upper
        M2, M3 = 2*W/sigma, 4*W**2/sigma**2
        ans = {
            'rrr': 2*(jets[3,0]+3*vrr*vr*M2+vr*vr*vr*M3),
            'rrt': jets[2,1]+(vrr*vq+2*vrt*vr)*M2+vr*vr*vq*M3,
            'rtt': jets[1,2]+(2*vrt*vq+vtt*vr)*M2+vr*vq*vq*M3}
        for idx,j in enumerate(range(4,23,2)):
            self._add_germ(ans, j, tail.seed_ratio[j], paid.absolute(amp*paid.literal_interval(ref[idx+1])))
        self._add_germ(ans, 4, tail.raw_ratio[4], previous['original_forced_raw_j4_coefficient_abs'])
        self.counts['new_third_jet_reference_passes'] += 1
        return ans

    def _add_germ(self, ans, j, C, amount):
        ans['rrr'] += self._germ3(j, C)*amount
        ans['rrt'] += j*amount*C
        ans['rtt'] += j*j*amount*C

    def _angular(self, response):
        tail, m = self.tail, self.tail.model
        ans = dict(self.ref3)
        if len(response) != m.nq:
            raise ValueError('all actual angular response coordinates are required')
        for idx,j in enumerate(range(4,23,2)):
            self._add_germ(ans, j, tail.seed_ratio[j],
                           paid.absolute(tail.amplitude*paid.literal_interval(float(response[idx]))))
        for mi, mode in enumerate(m.modes):
            for ki, degree in enumerate(m.tail_degrees):
                j,k = int(mode),int(degree)
                i = m.tail_start+mi*len(m.tail_degrees)+ki
                coef = paid.absolute(tail.amplitude*paid.literal_interval(float(response[i])))
                col = tail.gaussian_columns[j,k]
                _,K1,K2 = col['over_W_threejet_upper']
                ans['rrr'] += self._gaussian3(k,col)*coef
                ans['rrt'] += j*K2*coef
                ans['rtt'] += j*j*K1*coef
        self.counts['new_angular_third_jet_passes'] += 1
        return ans

    def _radial(self, j, extra, box, d1, d2, e1, e2):
        """Powers are factored: d1,d2 bound |p_r|/W,|p_rr|/W;
        e1,e2 bound |E'|/W²,|E''|/W². Zeros isolate implicit terms.
        """
        tail = self.tail
        rc, rm, E, z = tail.rc, tail.mouth, tail.Ehi, tail.W_upper**2
        beta, u = box['beta_lower'], box['u_lower']
        b = rc*beta
        pb, C, B, M = [pol(box[k]) for k in ('P','C_over_W','B_over_W','M_upper')]
        q,t,pt = [pol(j[k]) for k in ('q','t','rt')]
        prt,tr = extra['rrt'],extra['rtt']
        br = (q*pt*z+rm)/b
        ur2 = (e1/2+pb*pb*rm/b**2+pb*d1*rm**2/b**2+pb*pb*br*rm**2/b**3)/u
        Cr = e1*t*z+tr*E+pb+d1*rm
        Br = prt+pt/rc+q/rc**2
        Mr = 1+(d1*t+pb*tr+2*q*pt/rc+q*q/rc**2)*z
        R2 = (C*d1+B*B*E+e1*M/2)*box['omega_upper']
        Dr2 = Cr*d1+C*d2+e1*B*B*z+2*B*Br*E+e2*M/2+e1*Mr/2
        log_omega = 2*pol(1)/rc+3*br/b+3*ur2.whole(tail,2)/u
        Rr2 = Dr2*box['omega_upper']+R2*log_omega
        return dict(R2=R2, Rr2=Rr2, br=br, ur2=ur2, Br=Br)

    def _phase(self, jet, ext, box, radial, d1, e1, F2):
        tail = self.tail
        rc, rm, z = tail.rc, tail.mouth, tail.W_upper**2
        beta, u = box['beta_lower'], box['u_lower']
        b = rc*beta
        root_hi, root_lo = bounds.sqrt_i(tail.Ehi), bounds.sqrt_i(tail.Elo)
        amin = box['N_lower']/root_hi
        au = box['N_upper']/u
        bounds.positive(amin)
        cs, cv = I(22)/28, I(22)/14
        Pa = cs*au  # subtracting the angular constant is optional for this bound
        pb,B = pol(box['P']),pol(box['B_over_W'])
        q,t,pt = [pol(jet[k]) for k in ('q','t','rt')]
        br,ur2,Br,R2,Rr2 = [radial[k] for k in ('br','ur2','Br','R2','Rr2')]
        Gabs = R2.whole(tail, 2)
        urabs = ur2.whole(tail, 2)
        v2 = pb*q/b
        vr2 = (d1*q+pb*pt)/b+pb*q*br/b**2
        ut2 = (pb*pt*rm**2/b**2+pb*pb*q*t*z*rm**2/b**4)/u
        ut = ut2.whole(tail, 2)
        K2 = pb*B*rm**2/(u*b**3)
        Kr2 = (2*pb*B*rm+(d1*B+pb*Br)*rm**2)/(u*b**3)+K2*(br*3/b+urabs/u)
        Kt2 = ((pt*B+pb*(ext['rtt']+t/rc))*rm**2/(u*b**3)
               +K2*(q*t*3*z/b**2+ut/u))
        ar_abs = (Kt2+R2).whole(tail,2)
        utr2 = v2*ar_abs+vr2*au+br*K2+Kr2*rm
        Nr = (pol(1)/b+br*rm/b**2
              +(2*pb*t*rm+(d1*t+pb*ext['rtt'])*rm**2)*z/b**3
              +3*pb*t*br*rm**2*z/b**4)
        h2 = (K2+R2*cs)/amin+R2*Pa/amin**2
        Q2 = R2*cs+R2*Pa/amin
        Qr2 = (Rr2*cs+(K2+R2*cs)*Gabs/amin
               +Rr2*Pa/amin+R2*Pa*Gabs/amin**2)
        HT2 = F2*box['N_upper']/amin
        HJ2 = F2*ut/amin+Q2*rm/amin
        H2 = HT2+HJ2
        h_abs = h2.whole(tail, 2)
        dbr = br/amin+pol(rm*Gabs)/amin**2
        HrT2 = R2*box['N_upper']/amin**2+F2*Nr/amin+HJ2*h_abs
        HrJ2 = R2*ut/amin**2+F2*utr2.whole(tail,2)/amin+dbr*Q2+Qr2*rm/amin+HT2*h_abs
        Hr2 = HrT2+HrJ2
        S2 = H2*cv/root_lo
        Ss2 = (Hr2/tail.Elo+H2*e1.whole(tail,2)/(2*tail.Elo**2))*cv
        Ps1 = d1/tail.Elo+pb*e1.whole(tail,2)/(2*tail.Elo**2)
        U0s2 = ur2/tail.Elo+e1*root_hi/(2*tail.Elo**2)
        # Both components are projections of the SAME globally defined vector.
        # Orthogonal projections have real operator norm one even as theta varies.
        sabs, ssabs = sym(S2.whole(tail,2)), sym(Ss2.whole(tail,2))
        arc = dict(r=I(rc.lo,rm.hi), r_s=1/I(root_lo.lo,root_hi.hi),
            P=sym((pb/root_lo).whole(tail,1)), P_s=sym(Ps1.whole(tail,1)),
            q=sym(q.whole(tail,1)), t=sym(t.whole(tail,1)), q_s=sym((pt/root_lo).whole(tail,1)),
            U0=I(u.lo,root_hi.hi)/I(root_lo.lo,root_hi.hi), U0_s=sym(U0s2.whole(tail,2)),
            k=I((amin/au).lo,(au/amin).hi), h=sym((h2/root_lo).whole(tail,2)),
            sT=sabs, sn=sabs, ssT=ssabs, ssn=ssabs)
        return arc, dict(Q=Q2, H=H2, Hr=Hr2, S=S2, Ss=Ss2, U0s=U0s2), Ps1

    def _a_difference(self, jet, box):
        """|a-E**(-1/2)|/W² without a whole-window F divided at smaller r."""
        lo = bounds.sqrt_i(self.tail.Elo)
        b,u,rc = box['beta_lower'], box['u_lower'], self.tail.rc
        q,t,p = jet['q'],jet['t'],box['P']
        return upper((q**2/(rc**2*b*(1+b))+p*t/(rc*b**3))/u
                     +p**2/(b**2*u*lo*(lo+u)))

    def evaluate(self, response, original_tail_receipt, connection_receipt, *, tau=None):
        bounds.public_only()
        c, tail = self.conn, self.tail
        model = tail.joint
        response = model._check(response)
        if (model.guard() != c.provenance
                or paid.CurrentModelTailAnchor._snapshot(tail) != c.source_snapshot):
            raise ValueError('the actual frozen source or tail state differs')
        expected = {'schema': connection.SCHEMA, 'producer_sha256': SHA648,
            'joint_model_sha256': model.model_sha256, 'same_target_sha256': model.identity.target_sha256,
            'actual_response_sha256': paid.json_sha(response.tolist()),
            'fixed_seed_response_sha256': connection.tail_module.SEED_RESPONSE_SHA,
            'fixed_seed_paid_FINAL_sha256': connection.tail_module.SEED_FINAL_SHA,
            'same_actual_source_snapshot_sha256': c.source_snapshot,
            'same_literal_source_contract_sha256': tail.contract_sha,
            'consumed_preceding_tail_receipt_sha256': paid.json_sha(original_tail_receipt),
            'old_source_error_accounting': tail.contract['source_error_accounting'],
            'unresolved_original_source_errors': tail.unresolved}
        if any(connection_receipt.get(k) != v for k,v in expected.items()):
            raise ValueError('the paid R648 connection must bind the same R643 response and receipt')
        def from_receipt(key):
            return {k: read(v) for k,v in connection_receipt[key].items()}
        actual = from_receipt('complete_actual_five_jet_over_W_bound')
        box = from_receipt('whole_actual_trial_positive_box')
        angular = model.angular_response(response)
        extra = self.seed3 if angular.tobytes() == tail.response.tobytes() else self._angular(angular)
        ms = [read(v) for v in original_tail_receipt['actual_new_mean_over_W_threejet_upper']]
        mean_coeff = response[model.mean_start:]
        if (len(mean_coeff) != 94 or original_tail_receipt['mean_columns_zero_here_by_true_support'] != 90
                or original_tail_receipt['mean_Gaussian_degree_list'] != [0,1,2,3]):
            raise ValueError('the complete actual mean basis is required')
        mean3 = I(0)
        for k in range(4):
            coef = paid.absolute(tail.amplitude*paid.literal_interval(float(mean_coeff[61+28+k])))
            mean3 += coef*self._gaussian3(k,tail.mean_gaussian[k])
        self.counts['new_mean_four_Gaussian_third_jet_sums'] += 1
        e1 = self.L1*c.Er_WWr+c.Er_W2
        s1 = self.L1*c.seed_sr_Wr+c.seed_sr_W
        # First isolate E'' in <R0>_r, then s*'' in <Rseed>_r. The final
        # trial has its genuinely free m''' and uses no implicit denominator.
        ref = self._radial(c.reference, self.ref3, c.reference_box, self.L1+c.reference['rr'],
                           self.LW2+self.ref3['rrr'], e1, pol(0))
        e2 = 2*ref['Rr2']/(c.reference_box['omega_lower']*c.reference_box['M_lower'])
        sd = self.L1+s1+c.seed['rr']
        seed = self._radial(c.seed, self.seed3, c.seed_box, sd, self.LW2+self.seed3['rrr'], e1, e2)
        s2 = seed['Rr2']/c.seed_kappa
        d1 = self.L1+s1+ms[2]+actual['rr']
        d2 = self.LW2+s2+mean3+extra['rrr']
        rad = self._radial(actual, extra, box, d1, d2, e1, e2)
        F2 = pol(self._a_difference(c.reference,c.reference_box)+self._a_difference(actual,box))
        arc, fields, Ps1 = self._phase(actual,extra,box,rad,d1,e1,F2)
        evidence = {
            'same_field_identity': {k: expected[k] for k in ('joint_model_sha256','same_target_sha256',
                'actual_response_sha256','fixed_seed_response_sha256','same_literal_source_contract_sha256')},
            'continuous_enclosure_status': ('conditional_on_declared_input_errors' if tail.unresolved
                                            else 'all_declared_input_errors_enclosed'),
            'unresolved_errors': list(tail.unresolved)}
        self.counts['new_whole_tail_curvature_calls'] += 1
        # R649 checks the actual area and the off-solution shape operator. Its
        # metric bound can be wider than the cancellation-preserving R648 eta.
        try:
            shape = curvature.actual_arc_curvature(arc,input_evidence=evidence,tau=tau)
        except ArithmeticError as error:
            if str(error) != 'the actual cell has no proved positive geometric denominator':
                raise
            shape = {'same_field_evidence':evidence,'regular_arc_inputs':arc,
                     'curvature_unresolved':'the whole-tail arc box does not separate a required geometric denominator'}
        weighted = {'reference_abs_Esecond':(2,e2),'seed_abs_ssecond':(1,s2),
                    'trial_abs_prr':(1,d2),'trial_abs_R':(2,rad['R2']),
                    'trial_abs_Rr_and_Gr':(2,rad['Rr2']),'trial_abs_F':(2,F2),
                    'trial_abs_Ps':(1,Ps1)}
        weighted.update({'trial_abs_'+k:(2,v) for k,v in fields.items()})
        return paid.tree_intervals({'schema':SCHEMA,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'existing_R648_source_sha256':SHA648,'existing_R649_source_sha256':SHA649,
            'consumed_R648_receipt_sha256':paid.json_sha(connection_receipt),
            'cap_to_original_mouth_r':arc['r'], 'whole_u_lower':tail.U,
            'actual_same_field_and_source_errors':evidence,'old_source_error_accounting':tail.contract['source_error_accounting'],
            'third_jet_normalized_over_W': {name:{k:v.c for k,v in jets.items()}
                for name,jets in (('reference',self.ref3),('fixed_seed',self.seed3),('actual_trial',extra))},
            'actual_four_mean_Gaussian_third_over_W':upper(mean3),
            'pointwise_positive_polynomials':{k:{'power_of_true_W':d,'coefficients_ascending':v.c,
                'whole_interval_absolute_upper':v.whole(tail,d)} for k,(d,v) in weighted.items()},
            'same_R648_whole_tail_relative_metric_upper':connection_receipt['whole_true_tail_actual_relative_metric_operator_upper'],
            'R649_same_actual_tail_curvature':shape, 'current_consumer_counts':dict(self.counts),
            'whole_body_reach_fixed_metric_family_or_README_completion':False})
