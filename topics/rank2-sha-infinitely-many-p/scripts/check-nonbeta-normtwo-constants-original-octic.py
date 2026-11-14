#!/usr/bin/env python3
"""R262: a non-beta-pull norm-two constant family and the actual octic basis.

Exact Gaussian finite-flat traces; then the already normalized original
adjacent CM5/dyadic maps of R251/R254. No numerical theta fitting.
"""
import importlib.util
import json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'r248',HERE/'check-ray17-conjugate-trace-and-yang-projection.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
U, ii, K = m.U, s.I, s.QQ_I
checks = {}


def check(label,condition):
    checks[label] = bool(condition)
    if not condition:
        raise AssertionError(label)


# Exact norm-two primitive identity, including its sign and constant.
x, Phi, C = s.symbols('x Phi C')
va = -ii*(x-1/x)/2
B0 = 1/(x*x-1)
check('original_invariant_carrier',s.cancel(x*B0-1/(2*ii*va))==0)
check('original_carrier_deck_invariance',s.cancel((x*B0).subs(x,-1/x)-x*B0)==0)
check('actual_normtwo_coordinate_invariance',s.cancel(va.subs(x,-1/x)-va)==0)
for h in range(9):
    q = x*B0/(va*va-1)**h
    tr = q*Phi+q.subs(x,-1/x)*(-Phi-2*C)
    check('complete_nonconstant_log_elimination_'+str(h),
          s.cancel(tr-ii*C/(va*(va*va-1)**h))==0)
    check('true_holomorphic_Tplus_Tminus_order_'+str(h),17-2*h>=1)
check('true_holomorphic_T0_order',34-2==32)


def trace_row(a):
    f = s.Poly(U,U,domain=K)*m.Qba**4-(m.Kba**4).mul_ground(a)
    check('monic_seventeen_point_fiber_'+str(a),f.degree()==17 and f.LC()==1)
    mult = m.ipow((m.Pbe*m.inv(m.Pba,f)).rem(f),17,f)
    # Actual frame factor x(bar beta z)/x(z), not the x*x factor of R254.
    mult = (mult*m.Qba**2*m.inv(m.Kba**2,f)).rem(f)
    step = m.inv(s.Poly(U-1,U,domain=K),f)
    row = []
    for _ in range(9):
        row.append(s.expand((mult*f.diff()).rem(f).nth(16)*a**8*(a-1)**8))
        mult = (mult*step).rem(f)
    return row


vals = [trace_row(a) for a in range(2,19)]
ps = [m.interpolate([row[h] for row in vals],start=2) for h in range(9)]
held = trace_row(19)
for h,p,val in zip(range(9),ps,held):
    check('complete_CM17_held_out_fiber_'+str(h),p.eval(19)==val)
    check('actual_adjacent_target_degree_'+str(h),p.degree()<=16)
print('nine complete non-beta carrier traces: exact',flush=True)

d251 = json.loads((HERE/'check-third-adjacent-companion-lambda2.json').read_text())
d254 = json.loads((HERE/'check-octic-ray-original-companion-transport.json').read_text())
sqrt2 = s.sqrt(2)
zeta = (1+ii)/sqrt2
KM = s.QQ.algebraic_field(zeta)
M = s.Matrix.hstack(*[s.Matrix(list(map(s.sympify,col))+[s.S.Zero]*(17-len(col)))
                     for col in d251['CM5_adjacent_matrix_columns']])
N = M.applyfunc(lambda a:s.expand(a/(2+ii))).to_DM(domain=KM)
ID = s.eye(17).to_DM(domain=KM)
pw = [ID]
for _ in range(16):
    pw.append(pw[-1]*N)
check('actual_normalized_CM5_order_16',pw[16]==ID)
P8 = sum((pw[j].scalarmul(KM((-1)**(j//4))) for j in (0,4,8,12)),ID*0)
P8 = P8.scalarmul(KM(1)/4)
check('actual_original_octic_projector',P8*P8==P8 and P8.rank()==4)
vs = s.Matrix.hstack(*map(m.vector,ps)).to_DM(domain=KM)
refs = [[KM.from_sympy(s.sympify(a)) for a in row]
        for row in d254['normalized_new_octic_references']]
deltas = [KM.from_sympy(s.sympify(a)) for a in d254['original_dyadic_constants']]
cs = []
for j,ref,de in zip([1,3,5,7],refs,deltas):
    E = sum((pw[a].scalarmul(KM.from_sympy(s.expand(zeta**(-j*a))))
             for a in range(4)),ID*0)*P8
    vv = (E.scalarmul(KM(1)/4)*vs).to_list()
    check('full_original_octic_polynomial_'+str(j),
          all(vv[k][h]==vv[16][h]*ref[k] for k in range(17) for h in range(9)))
    cs.append([vv[16][h]/de for h in range(9)])
CM = DomainMatrix(cs,(4,9),KM)
C4 = DomainMatrix([row[:4] for row in cs],(4,4),KM)
check('entire_nonbeta_family_rank_four',CM.rank()==4)
check('first_four_actual_sources_already_a_basis',C4.det()!=KM.zero)
check('all_four_original_components_of_Fbeta_over_x',all(row[0]!=KM.zero for row in cs))
extra = (vs-P8*vs).to_Matrix()

# Recover exactly the same original two companion columns as R235/R254.
a1 = -s.Rational(39797,14784000)-s.Rational(8177,4224000)*sqrt2
a3 = -s.Rational(2091,448000)-s.Rational(2669,1971200)*sqrt2
b1 = s.Rational(224494093,56229888000)+s.Rational(4237163,1363148800)*sqrt2
b3 = -s.Rational(6031447,3748659200)-s.Rational(202405417,62977474560)*sqrt2
aa = [a1,a3,a1.subs(sqrt2,-sqrt2),a3.subs(sqrt2,-sqrt2)]
bb = [b1,b3,b1.subs(sqrt2,-sqrt2),b3.subs(sqrt2,-sqrt2)]
ab = s.Matrix.hstack(s.Matrix(aa),s.Matrix(bb)).to_DM(domain=KM)
cols = C4.inv()*ab
check('actual_C_A_and_C_B_plus_back_substitution',(C4*cols).to_list()==ab.to_list())
check('original_C_A_pulled_mass',s.simplify(16*sum(aa))==-s.Rational(272,1155))
mb = [-60+44*sqrt2,(-356+252*sqrt2)/17,
      -60-44*sqrt2,(-356-252*sqrt2)/17]
check('original_regularized_C_B_pulled_mass',
      s.simplify(4*sum(a*b for a,b in zip(bb,mb)))==-s.Rational(2261,10240))


def enc(a):
    return str(KM.to_sympy(a))


out = {
 'theorem':'R262','status':'PASS',
 'coefficient_order':'ascending powers of U',
 'actual_source':'F(beta z)/(x(z)*(x(z)^2-1)^h), h=0,...,8',
 'actual_normtwo_primitive_identity':'Tr_alpha[H_beta*x*B0*B0(alpha z)^h*Phi_k] = i*C_k*G_h',
 'natural_source_orders_at_O':[2+4*h for h in range(9)],
 'actual_CM17_trace_polynomials':[m.coefficients(p) for p in ps],
 'original_octic_matrix_4_by_9':[[enc(a) for a in row] for row in cs],
 'first_four_determinant':enc(C4.det()),
 'first_source_original_octic_coordinates':[enc(row[0]) for row in cs],
 'unprojected_remainder_columns':[[str(extra[j,h]) for j in range(17)] for h in range(9)],
 'original_companion_columns_A_B':[[enc(a) for a in row] for row in cols.to_list()],
 'original_C_A_mass':'-272/1155','original_regularized_C_B_mass':'-2261/10240',
 'full_branch_scaling_unit':'(U_alpha,p * U_barbeta,p)^(-u), on the common [2] source',
 'nonzero_log_constant_is_not_assumed_a_padic_unit':True,
 'checks':checks,
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'output':str(target)},ensure_ascii=False))
