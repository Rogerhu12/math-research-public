#!/usr/bin/env python3
"""R254: actual octic ray -> conjugate CM17 trace -> original companions.

Exact arithmetic only.  The global degree bounds are proved in R254;
the held-out values here check the implementation, not the degree bounds.
Uses the published R248 CM functions and R251 adjacent CM5 matrix.
"""
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as Q
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location(
    'r248', HERE / 'check-ray17-conjugate-trace-and-yang-projection.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
U, V, ii = m.U, m.V, s.I
sqrt2 = s.sqrt(2)
zeta8 = (1+ii)/sqrt2
field = s.QQ.algebraic_field(zeta8)
checks = {}


def check(label, condition):
    checks[label] = bool(condition)
    if not condition:
        raise AssertionError(label)


def enc(a):
    return str(field.to_sympy(a))


def matrix_enc(a):
    return [[enc(x) for x in row] for row in a.to_list()]


# Original signed mu_4 orbit, using x(z +/- P) and y^2=x^3-x.
X, A = s.symbols('X A')
M = (X+A)*(X*A-1)
dd = (X-A)**2
n2 = 4*(X**3-X)*(A**3-A)
pair = s.cancel(2*dd**2*(M**2+n2-dd**2) /
                ((M**2+n2-dd**2)**2-4*M**2*n2))
num = 8*(U+1)*(V+1)*(3*(U**2+1)*(V-1)**2+U*(-6*V**2+28*V-6))
den = (V-1)**2*(U**2+1)-2*(V**2+6*V+1)*U
check('original_signed_four_orbit',
      s.cancel(pair-pair.subs(A, -A)-X*A*(num/den**2).subs({U:X**2,V:A**2})) == 0)
check('actual_z2_orbit_coefficient',
      s.cancel(s.limit(U*num/den**2, U, s.oo)-24*(V+1)/(V-1)**2) == 0)

# The exact four ray numerators, normalized by the actual z^2 coefficient.
m.dom = field
K = s.Poly(m.K.as_expr(), V, domain=field)
g = s.Poly(m.g.as_expr(), V, domain=field)
C = s.Poly(3*V**2-6*V-1, V, domain=field)
D = s.Poly(V**4+12*V**3+30*V**2-36*V+9, V, domain=field)
kg = (D*m.inv(C**2, K)).rem(K)
ks = [s.Poly(1, V, domain=field)]
gs = [s.Poly(V, V, domain=field)]
for _ in range(4):
    ks.append((ks[-1]*m.comp(kg, gs[-1], K)).rem(K))
    gs.append(m.comp(g, gs[-1], K))
check('triplication_fourth_x_sign', ks[4] == s.Poly(-1, V, domain=field))
check('triplication_fourth_U_identity', gs[4] == gs[0])
b = (s.Poly(24*(V+1), V, domain=field)*m.inv(s.Poly((V-1)**2, V, domain=field), K)).rem(K)
characters = [1,3,5,7]
bs, bi = [], []
for k in characters:
    bk = sum(((ks[j]*m.comp(b, gs[j], K)).mul_ground(s.expand(zeta8**(-k*j)))
              for j in range(4)), s.Poly(0, V, domain=field)).rem(K)
    invbk = m.inv(bk, K)
    check('nonzero_actual_second_mass_'+str(k),
          (bk*invbk).rem(K) == s.Poly(1, V, domain=field))
    bs.append(bk)
    bi.append(invbk)
Db = s.Poly(m.Dbe.as_expr(), U, domain=field)


def ray_values(a):
    q = (s.Poly(num.subs(U,a), V, domain=field)*
         m.inv(s.Poly(den.subs(U,a)**2, V, domain=field), K)).rem(K)
    qs = [(ks[j]*m.comp(q, gs[j], K)).rem(K) for j in range(4)]
    out = []
    for h,k in enumerate(characters):
        v = (sum((qs[j].mul_ground(s.expand(zeta8**(-k*j))) for j in range(4)),
                 s.Poly(0,V,domain=field))*bi[h]).rem(K)
        check('ray_descends_'+str(a)+'_'+str(k), v.degree() <= 0)
        out.append(s.expand(v.nth(0)*Db.eval(a)**2))
    return out


rows = [ray_values(a) for a in range(16)]
nums = [m.interpolate([row[j] for row in rows]) for j in range(4)]
held = ray_values(16)
for k,n,a in zip(characters, nums, held):
    check('ray_numerator_degree_and_normalization_'+str(k), n.degree()==15 and n.LC()==1)
    check('ray_held_out_value_'+str(k), n.eval(16)==a)
print('four original octic rational functions: exact', flush=True)

# The actual conjugate CM17 trace, computed first as a Gaussian linear map.
m.dom = s.QQ_I
dom = m.dom


def trace_row(a):
    f = s.Poly(U,U,domain=dom)*m.Qba**4-(m.Kba**4).mul_ground(a)
    check('CM17_monic_degree_'+str(a), f.degree()==17 and f.LC()==1)
    mult = m.ipow((m.Pbe*m.inv(m.Pba,f)).rem(f),17,f)
    # x(z)*x(bar beta z): essential for the actual W/x target frame.
    mult = (mult*s.Poly(U,U,domain=dom)*m.Qba**2*
            m.inv(m.Kba**2*m.Dbe**2,f)).rem(f)
    row = []
    for _ in range(16):
        row.append(s.expand((mult*f.diff()).rem(f).nth(16)*a**8*(a-1)**8))
        mult = (mult*s.Poly(U,U,domain=dom)).rem(f)
    return row


values = [trace_row(a) for a in range(2,19)]
transfer = [m.interpolate([row[j] for row in values],start=2) for j in range(16)]
held = trace_row(19)
check('CM17_held_out_full_trace', all(p.eval(19)==v for p,v in zip(transfer,held)))
traces = [[s.expand(sum(transfer[j].nth(h)*n.nth(j) for j in range(16)))
           for h in range(17)] for n in nums]
print('complete conjugate CM17 trace: exact', flush=True)

# The same actual adjacent CM5 matrix as R251, not an auxiliary operator.
d251 = json.loads((HERE/'check-third-adjacent-companion-lambda2.json').read_text())
Mminus = s.Matrix.hstack(*[s.Matrix(list(map(s.sympify,col))+[s.S.Zero]*(17-len(col)))
                          for col in d251['CM5_adjacent_matrix_columns']])
N = Mminus.applyfunc(lambda x:s.expand(x/(2+ii))).to_DM(domain=field)
ID = s.eye(17).to_DM(domain=field)
powers = [ID]
for _ in range(16):
    powers.append(powers[-1]*N)
check('actual_normalized_CM5_order_16', powers[16]==ID)
P8 = sum((powers[j].scalarmul(field((-1)**(j//4))) for j in (0,4,8,12)),ID*0)
P8 = P8.scalarmul(field(1)/4)
check('actual_octic_projector', P8*P8==P8 and P8.rank()==4)
VS = s.Matrix.hstack(*[s.Matrix(t) for t in traces]).to_DM(domain=field)
refs, coeffs, projectors = [], [], []
for j in characters:
    E = sum((powers[h].scalarmul(field.from_sympy(s.expand(zeta8**(-j*h))))
             for h in range(4)),ID*0)*P8
    E = E.scalarmul(field(1)/4)
    check('actual_rank_one_projector_'+str(j), E*E==E and E.rank()==1)
    vv = (E*VS).to_list()
    check('four_nonzero_projection_masses_'+str(j), all(x!=field.zero for x in vv[16]))
    v = [row[0]/vv[16][0] for row in vv]
    check('full_projected_polynomial_equality_'+str(j),
          all(vv[h][k]==vv[16][k]*v[h] for h in range(17) for k in range(4)))
    refs.append(v)
    coeffs.append(vv[16])
    projectors.append(E)
check('octic_projector_partition', sum(projectors,ID*0)==P8)
Cnew = DomainMatrix(coeffs, (4,4), field)
check('four_ray_octic_matrix_invertible', Cnew.det()!=field.zero)
extras = (VS-P8*VS).to_list()
check('all_thirteen_dimensional_remainders_present',
      all(any(row[k]!=field.zero for row in extras) for k in range(4)))

# Original quarter-point transport, with exactly R246's phase and rho.
w, S = s.symbols('w S')
x = ii-2*(1-ii)*w-4*w*w
xi = s.series(1/x,w,0,3).removeO()
sv = s.series(xi*xi,w,0,3).removeO()
g17 = s.series(s.exp(17*((1+ii)*w/2-ii*w*w/2)),w,0,3).removeO()
V1 = 1+(-5+2*sqrt2)*S+(11-4*sqrt2)*S**2+(-15+10*sqrt2)*S**3
V3 = 1+(63-70*sqrt2)*S/17+(-77+44*sqrt2)*S**2/17+(5+2*sqrt2)*S**3/17
old_refs = [V1,V3,V1.subs(sqrt2,-sqrt2),V3.subs(sqrt2,-sqrt2)]
deltas = []
for j,p in zip(characters,old_refs):
    jet2 = s.expand(s.series(g17*xi*p.subs(S,sv),w,0,3).removeO()).coeff(w,2)
    delta = field.from_sympy(s.simplify(ii*jet2/16))
    check('actual_dyadic_octic_constant_'+str(j),delta!=field.zero)
    deltas.append(delta)
expected_delta = [ii*(70-47*sqrt2)/4,ii*(16-7*sqrt2)/4,
                  ii*(70+47*sqrt2)/4,ii*(16+7*sqrt2)/4]
check('four_exact_dyadic_constants',deltas==list(map(field.from_sympy,expected_delta)))

# Check all seventeen coordinates of each actual dyadic image independently
# of its CM5 eigentype.  The global degree bound makes these coordinates a
# triangular basis, so this verifies the whole transported section.
ORDER = 66
GI = s.QQ_I


def smul(a,b,limit=ORDER):
    zero = a[0]*b[0]*0
    out = [zero]*(limit+1)
    for j,x in enumerate(a[:limit+1]):
        if x:
            for h,y in enumerate(b[:limit+1-j]):
                if y:
                    out[j+h] += x*y
    return out


def sexp(a):
    zero = a[0]*0
    out = [zero+1]+[zero]*ORDER
    for n in range(1,ORDER+1):
        out[n] = sum((j*a[j]*out[n-j] for j in range(1,n+1)),zero)/n
    return out


xj = [GI.zero]*(ORDER+1)
xj[0],xj[1] = GI.from_sympy(ii),GI.from_sympy(-2+2*ii)
for n in range(ORDER-1):
    xj[n+2] = (6*sum((xj[h]*xj[n-h] for h in range(n+1)),GI.zero)
               -GI(2)*(n==0))/((n+1)*(n+2))
xi_j = [1/xj[0]]+[GI.zero]*ORDER
for n in range(1,ORDER+1):
    xi_j[n] = -sum((xj[h]*xi_j[n-h] for h in range(1,n+1)),GI.zero)/xj[0]
lj = [GI.zero]*(ORDER+1)
lj[1] = GI.from_sympy(17*(1+ii)/2)
for n in range(ORDER-1):
    lj[n+2] = 17*xi_j[n]/((n+1)*(n+2))
quarter_base = smul(sexp(lj),xi_j)
quarter_s = smul(xi_j,xi_j)
quarter_basis = [quarter_base]
for _ in range(3):
    quarter_basis.append(smul(quarter_basis[-1],quarter_s))

uu = [Q(0)]*(ORDER+2)
uu[1] = Q(1)
for n in range(ORDER):
    cube = sum((uu[a]*uu[b]*uu[n-a-b]
                for a in range(n+1) for b in range(n+1-a)),Q(0))
    uu[n+2] = -2*cube/((n+1)*(n+2))
u2 = smul(uu,uu)
u4 = smul(u2,u2)
lt = [Q(0)]*(ORDER+1)
for n in range(ORDER-1):
    lt[n+2] = 68*u2[n]/((n+1)*(n+2))
base = smul(sexp(lt),[(n+1)*uu[n+1] for n in range(ORDER+1)])
pw = u2
origin_basis = []
for _ in range(17):
    origin_basis.append(smul(base,pw))
    pw = smul(pw,u4)
for j,p,v,delta in zip(characters,old_refs,refs,deltas):
    pc = [field.from_sympy(s.Poly(p,S).nth(h)) for h in range(4)]
    good = True
    for n in range(2,ORDER+1,4):
        lhs = field.from_sympy(ii)*field(2**n)/64*sum(
            (pc[h]*field.from_sympy(GI.to_sympy(quarter_basis[h][n]))
             for h in range(4)),field.zero)
        rhs = delta*sum((v[16-h]*field.from_sympy(s.Rational(origin_basis[h][n]))
                         for h in range(17)),field.zero)
        good = good and lhs==rhs
    check('complete_17_coordinate_original_dyadic_image_'+str(j),good)

Cold = DomainMatrix([[a/deltas[j] for a in row] for j,row in enumerate(coeffs)],(4,4),field)
check('original_R235_octic_transport_invertible',Cold.det()!=field.zero)

# Both original companion columns, without dropping C_B's CM regularization.
a1 = -s.Rational(39797,14784000)-s.Rational(8177,4224000)*sqrt2
a3 = -s.Rational(2091,448000)-s.Rational(2669,1971200)*sqrt2
b1 = s.Rational(224494093,56229888000)+s.Rational(4237163,1363148800)*sqrt2
b3 = -s.Rational(6031447,3748659200)-s.Rational(202405417,62977474560)*sqrt2
aa = [a1,a3,a1.subs(sqrt2,-sqrt2),a3.subs(sqrt2,-sqrt2)]
bb = [b1,b3,b1.subs(sqrt2,-sqrt2),b3.subs(sqrt2,-sqrt2)]
ab = s.Matrix.hstack(s.Matrix(aa),s.Matrix(bb)).to_DM(domain=field)
coeff_original = Cold.inv()*ab
check('exact_original_A_B_columns',(Cold*coeff_original).to_list()==ab.to_list())
check('A_mass_unchanged',s.simplify(16*sum(aa))==-s.Rational(272,1155))
mass_b = [-60+44*sqrt2,(-356+252*sqrt2)/17,
          -60-44*sqrt2,(-356-252*sqrt2)/17]
check('regularized_B_mass_unchanged',
      s.simplify(4*sum(x*y for x,y in zip(bb,mass_b)))==-s.Rational(2261,10240))

# Complete Mellin left-normal ordering, through all four shifted weights.
ww = s.symbols('W0:5')


def ED(p):
    return s.expand(sum(s.diff(p,ww[j])*ww[j+1] for j in range(4)))


Ps = [[s.S.One]]
for k in range(4):
    before = Ps[-1]
    row = []
    for h in range(k+2):
        v = before[h-1] if h else 0
        if h<=k:
            v += (k+1-ww[0])*before[h]-ED(before[h])
        row.append(s.expand(v))
    Ps.append(row)
check('second_order_full_connection_polynomial',Ps[2]==[
    ww[0]**2-3*ww[0]+ww[1]+2,3-2*ww[0],s.S.One])
check('all_highest_Euler_terms_one',all(row[-1]==1 for row in Ps))

out = {
 'theorem':'R254','status':'PASS','characters':characters,
 'zeta8':str(zeta8),'coefficient_order':'ascending powers of U (or V where specified)',
 'signed_orbit_kernel_numerator':str(num),'signed_orbit_kernel_denominator':str(den),
 'actual_ray_masses_divided_xP':[m.coefficients(b) for b in bs],
 'actual_ray_mass_inverse_certificates':[m.coefficients(b) for b in bi],
 'normalized_ray_numerators':[m.coefficients(n) for n in nums],
 'ray_denominator':m.coefficients(Db),
 'Gaussian_CM17_transfer_columns':[m.coefficients(c) for c in transfer],
 'actual_CM17_traces':[[str(a) for a in t] for t in traces],
 'normalized_new_octic_references':[[enc(x) for x in v] for v in refs],
 'ray_to_normalized_new_octic':matrix_enc(Cnew),
 'original_dyadic_constants':list(map(enc,deltas)),
 'ray_to_original_R235_octic':matrix_enc(Cold),
 'new_projection_determinant':enc(Cnew.det()),
 'original_projection_determinant':enc(Cold.det()),
 'thirteen_dimensional_remainders':[[enc(row[k]) for row in extras] for k in range(4)],
 'original_companion_columns_A_B':matrix_enc(coeff_original),
 'complete_Mellin_left_normal_polynomials':[[str(v) for v in row] for row in Ps],
 'checks':checks,
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'output':str(target)},ensure_ascii=False))
