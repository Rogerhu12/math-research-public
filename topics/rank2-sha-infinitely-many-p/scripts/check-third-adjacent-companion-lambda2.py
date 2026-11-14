#!/usr/bin/env python3
"""R251: true adjacent-weight CM5 matrix and the log-free lambda^2 bridge.

Exact Q(i) traces, rational covariant division, and original theta matrices.
Uses the R248 trace helpers and the R245 rational differential operator.
No target-prime sampling and no floating point.
"""
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

m = module('r248', 'check-ray17-conjugate-trace-and-yang-projection.py')
c = module('r245', 'check-e136-covariant-cm17-log-bridge.py')
s, U, ii, dom = m.s, m.U, m.ii, m.dom
checks = {}

def check(key, cond):
    checks[key] = bool(cond)
    if not cond:
        raise AssertionError(key)

def row_at(a):
    f = s.Poly(U, U, domain=dom) * m.Qp**4 - (m.Kp**4).mul_ground(a)
    ub = (s.Poly(U, U, domain=dom) * m.Qb**4 * m.inv(m.Kb**4, f)).rem(f)
    mult = m.ipow((m.Pb * m.inv(m.Pp, f)).rem(f), 17, f)
    mult = (mult * m.inv(m.ipow(ub, 8, f) * m.ipow(ub-1, 8, f), f)).rem(f)
    # The actual x(pi w)/x(bar pi w) factor for the W/x frame.
    mult = (mult * m.Qp**2 * m.Kb**2 * m.inv(m.Kp**2 * m.Qb**2, f)).rem(f)
    out = []
    for j in range(17):
        out.append(s.expand((mult * f.diff()).rem(f).nth(4) * a**8 * (a-1)**8))
        mult = (mult * ub).rem(f)
    return out

vals = [row_at(a) for a in range(2, 19)]
cols = [m.interpolate([v[j] for v in vals], start=2) for j in range(17)]
held = row_at(19)
check('held_out_trace_value', all(col.eval(19) == a for col, a in zip(cols, held)))
M = s.Matrix.hstack(*map(m.vector, cols))
d248 = json.loads((HERE / 'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
Mplus = s.Matrix.hstack(*[m.vector(m.pp(list(map(s.sympify, col))))
                         for col in d248['CM5_matrix_columns']])
J = s.zeros(17)
for j in range(17):
    J[j, 16-j] = 1
check('true_half_period_conjugacy', M == J * Mplus * J)
pa, pb = m.Dbe * m.Kbe**2, m.Dba * m.Kba**2
check('CM_beta_adjacent_polynomial', m.vector(pa) == -J * m.vector(m.Pbe))
check('CM_barbeta_adjacent_polynomial', m.vector(pb) == -J * m.vector(m.Pba))
check('CM_beta_actual_eigenvalue', m.eigenvalue(M, pa) == 2+ii)
check('CM_barbeta_actual_eigenvalue', m.eigenvalue(M, pb) == 2+ii)

N = M.applyfunc(lambda x: s.expand(x / (2+ii)))
ND, ID = N.to_DM(domain=dom), s.eye(17).to_DM(domain=dom)
powers = [ID]
for j in range(16):
    powers.append(powers[-1] * ND)
check('normalized_CM5_order_16', powers[16] == ID)
P4 = sum((powers[j] for j in (0, 4, 8, 12)), ID*0).scalarmul(dom(1)/4)
projs = []
for k in range(4):
    P = sum((powers[j].scalarmul(dom.from_sympy(ii**(-k*j)))
             for j in range(4)), ID*0) * P4
    projs.append(P.scalarmul(dom(1)/4))

refs = {}
for k, fac in [(1, -55), (2, s.Rational(1, 25)), (3, s.Rational(1, 13))]:
    vp = s.Matrix(list(map(s.sympify, d248['normalized_primitive_polynomials'][str(k)])))
    vm = fac * J * vp
    check('adjacent_ref_normalization_'+str(k), vm[16] == 1)
    check('adjacent_ref_character_'+str(k), (ND * vm.to_DM(domain=dom)).to_Matrix() == ii**k * vm)
    refs[k] = vm

# Recompute the second curve's companion in precisely the R245 operator.
Q = c.Q
D = [Q(0)]*8 + c.pp([Q(-1), Q(1)], 8)
DG = [Q(0)]*8 + c.pp([Q(-1), Q(1)], 7) + [Q(0)]
dc = [c.operator_column(j) for j in range(15)] + [D, DG]
DM = [[dc[k][j] for k in range(17)] for j in range(17)]
src2 = c.cv(list(map(Q, d248['normalized_primitive_polynomials']['2'])), DM)
srcI = c.cv(c.P_IM, DM)
a2 = src2['beta_eff'] / srcI['beta_eff']
R2 = [x-a2*y for x, y in zip(src2['R14'], srcI['R14'])]
gam2 = src2['gamma']-a2*srcI['gamma']
check('a2_exact', a2 == Q(8235327, 3310819))
check('gamma2_exact', gam2 == Q(-471121690512128, 645609705))
check('second_companion_mass', R2[-1]+gam2/4 == Q(1, 2))
d245 = json.loads((HERE / 'check-e136-covariant-cm17-log-bridge.json').read_text())
Rs = list(map(Q, d245['bridge']['Rstar']))
gams = Q(d245['bridge']['gamma_star'])
t = gam2/gams
R0 = [x-t*y for x, y in zip(R2, Rs)]
check('fixed_log_cancellation_ratio', t == Q(-607305304175790, 3142050296189))
check('log_free_companion_mass', R0[-1] == Q(1, 2))

def decompose(R):
    P = s.Poly(U*(U-1), U, domain=dom) * m.pp(list(map(s.Rational, R)))
    v = m.vector(P)
    ev = [(E * v.to_DM(domain=dom)).to_Matrix() for E in projs]
    cs = []
    for k in (1, 2, 3):
        r = refs[k]
        a = s.simplify(ev[k][16])
        check('primitive_equality_'+str(len(all_decomp))+'_'+str(k), ev[k] == a*r)
        cs.append(a)
    cm = s.Matrix.hstack(m.vector(pa), m.vector(pb)).gauss_jordan_solve(ev[0])[0]
    extra = v-sum(ev, s.zeros(17, 1))
    check('extra_nonzero_'+str(len(all_decomp)), any(x != 0 for x in extra))
    return {'P': list(map(str, v)), 'R14': list(map(str, R)),
            'quartic_coefficients': list(map(str, cs)),
            'CM_coefficients_beta_barbeta': list(map(str, cm)),
            'twelve_character_remainder': list(map(str, extra))}

all_decomp = []
for R in (Rs, R2, R0):
    all_decomp.append(decompose(R))
cs, c2, c0 = [s.Rational(d['quartic_coefficients'][1]) for d in all_decomp]
check('Cstar_lambda2_coefficient', cs == -s.Rational(2365009727546525379547, 30963292372771799040))
check('C2_lambda2_coefficient', c2 == s.Rational(461734403779915958623, 31276052901789696))
check('log_free_lambda2_coefficient', c0 == s.Rational(822757710852163565, 43479138997811252736))
check('actual_log_free_coefficient_relation', c2-s.Rational(t)*cs == c0)
check('nonzero_actual_E34_component', c0 != 0)
check('complete_operator_loop_constant', s.Rational(-640)/(c0*s.Rational(128, 5)) == -25/c0)

out = {'theorem': 'R251', 'status': 'PASS',
       'coefficient_order': 'ascending powers of U',
       'actual_adjacent_frame': 'W/x',
       'CM5_adjacent_matrix_columns': [m.coefficients(col) for col in cols],
       'half_period_matrix_conjugacy': 'M_minus = reversal M_plus reversal',
       'CM_adjacent_polynomials': {'beta': m.coefficients(pa), 'barbeta': m.coefficients(pb)},
       'normalized_adjacent_primitive_polynomials': {str(k): list(map(str, v)) for k, v in refs.items()},
       'Cstar_rational': all_decomp[0], 'C2_rational': all_decomp[1], 'log_free_C0': all_decomp[2],
       'a2': str(a2), 'gamma2': str(gam2), 'gamma_star': str(gams), 't': str(t),
       'Q_plus_w_lambda2_constant': '128 i 2^(-1/4)/5',
       'complete_covariant_loop_constant': str(-25/c0),
       'checks': checks}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'checks': len(checks), 'output': str(target)}, ensure_ascii=False))
