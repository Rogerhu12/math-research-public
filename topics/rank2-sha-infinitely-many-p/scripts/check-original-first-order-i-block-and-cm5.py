#!/usr/bin/env python3
"""R283 work: actual i-type first-order primitive and true CM5 trace."""
import importlib.util
import json
from pathlib import Path
import sys

import sympy as s
from flint import fmpq, fmpq_mat

root=Path(__file__).parent
spec=importlib.util.spec_from_file_location('r248',root/'check-ray17-conjugate-trace-and-yang-projection.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
U=m.U
dom=m.dom
checks={}


def check(name,value):
    checks[name]=bool(value)
    if not checks[name]:
        raise AssertionError(name)


def matrix_domain(mat):
    return mat.applyfunc(s.expand).to_DM().convert_to(dom)


def row(a):
    f=s.Poly(U,U,domain=dom)*m.Qp**4-(m.Kp**4).mul_ground(a)
    ub=(s.Poly(U,U,domain=dom)*m.Qb**4*m.inv(m.Kb**4,f)).rem(f)
    mult=m.ipow((m.Pb*m.inv(m.Pp,f)).rem(f),17,f)
    mult=(mult*m.inv(m.ipow(ub,8,f)*m.ipow(ub-1,8,f),f)).rem(f)
    ratio_num=m.Qb**3*m.Kb*m.Pp
    ratio_den=m.Qp**3*m.Kp*m.Pb
    mult=(mult*ratio_num*m.inv(ratio_den,f)).rem(f)
    vals=[]
    for j in range(17):
        tr=(mult*f.diff()).rem(f).nth(4)
        vals.append(s.expand(tr*a**8*(a-1)**8))
        mult=(mult*ub).rem(f)
    return vals


if '--reuse-i-matrix' in sys.argv:
    cache=json.loads(Path(__file__).with_suffix('.json').read_text())
    Mi=s.Matrix.hstack(*[s.Matrix([s.sympify(z) for z in col])
                        for col in cache['CM5_matrix_columns']])
    check('true_i_type_CM5_trace_held_fiber',cache['checks']['true_i_type_CM5_trace_held_fiber'])
else:
    vals=[row(a) for a in range(2,19)]
    cols=[m.interpolate([v[j] for v in vals],start=2) for j in range(17)]
    held=row(19)
    check('true_i_type_CM5_trace_held_fiber',all(c.eval(19)==v for c,v in zip(cols,held)))
    Mi=s.Matrix.hstack(*map(m.vector,cols))
L=s.diag(*[-4*(17-j) for j in range(17)])
dat=json.loads((root/'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
Mp=s.Matrix.hstack(*[s.Matrix([s.sympify(c) for c in col]+[0]*(17-len(col)))
                     for col in dat['CM5_matrix_columns']])
Ni=(Mi/m.pi).applyfunc(s.expand_complex)
ND=matrix_domain(Ni)
check('normalized_i_type_order_16',(ND**16-ND.eye((17,17),dom)).is_zero_matrix)
charpoly=s.factor(Ni.charpoly().as_expr(),extension=s.I)
xx=Ni.charpoly().gen
check('normalized_i_type_characteristic_polynomial',
      s.expand(charpoly-(xx+1)*(xx**16-1))==0)
rank_data={}
for c in (s.Integer(1),s.expand_complex(m.pi/m.pib),s.expand_complex(m.pib/m.pi)):
    delta=(Mp*L-c*L*Mi).applyfunc(s.expand)
    rank_data[str(c)]=matrix_domain(delta).rank()
    print('mult',c,'rank',rank_data[str(c)],flush=True)

# Exact original angular primitives; these are fixed, already certified inputs.
original=json.loads((root/'check-original-three-ordinary-adjoint.json').read_text())
v=s.symbols('v')
def poly(cs,var=U):
    return s.Poly(sum(s.sympify(c)*var**j for j,c in enumerate(cs)),var,domain=dom)
BA=poly(original['angular_primitive_B_A'],v)
BB=poly(original['angular_primitive_B_B'],v)
ZH=poly(original['angular_primitive_Z_H'],v)
QA=poly(original['source_coefficients_ascending']['A'],v)
QB=poly(original['source_coefficients_ascending']['B'],v)
QH=poly(original['source_coefficients_ascending']['H_angular'],v)
a0,b0=BA.nth(0),BB.nth(0)
BAB=BA.mul_ground(b0)-BB.mul_ground(a0)
PGH=s.Poly(s.expand(-U**17*ZH.as_expr().subs(v,1/U)/4),U,domain=dom)
PGAB=s.Poly(s.expand(-U**17*BAB.as_expr().subs(v,1/U)/4),U,domain=dom)
SA=s.Poly(s.expand(U**17*QA.as_expr().subs(v,1/U)),U,domain=dom)
SB=s.Poly(s.expand(U**17*QB.as_expr().subs(v,1/U)),U,domain=dom)
PH=s.Poly(s.expand(U**16*QH.as_expr().subs(v,1/U)),U,domain=dom)
check('H_actual_first_order_primitive',L*m.vector(PGH)==m.vector(PH))
check('AB_primitive_boundary_exact',BAB.nth(0)==0 and BAB.nth(1)==0)
check('two_actual_primitive_degrees',PGH.degree()==15 and PGAB.degree()==15)

# The other, untwisted, odd block has a genuine one-dimensional boundary.
MU=s.zeros(18,17)
for j in range(17):
    MU[j,j]=70-4*j
    MU[j+1,j]=4*j-68
ell=s.Matrix([[s.Rational(4**(17-j),(35-2*j)*s.binomial(34-2*j,17-j))
               for j in range(18)]])
check('untwisted_rank_seventeen',MU.rank()==17)
check('untwisted_actual_cokernel',ell*MU==s.zeros(1,17) and ell[17]==1)
ve18=lambda P:s.Matrix([P.nth(j) for j in range(18)])
check('A_boundary_is_original_BA_zero',(ell*ve18(SA))[0]==-a0/2)
check('B_boundary_is_original_BB_zero',(ell*ve18(SB))[0]==-b0/2)
check('AB_actual_source_return',MU*m.vector(PGAB)==b0*ve18(SA)-a0*ve18(SB))

# Exact norm-two branch, including the pole that the formal plus branch misses.
ww=-4*U/(U-1)**2
alpha=1+s.I
def pull_positive_primitive(B):
    return s.cancel(alpha*((U-1)**34*(U+1)*B.as_expr().subs(v,ww)
                         -B.nth(0)*(U-1)**35)/(16*U))
pulled={}
for name,B in [('A',BA),('B',BB)]:
    raw=pull_positive_primitive(B)
    polar=alpha*B.nth(0)/(8*U)
    regular=s.Poly(s.cancel(raw-polar),U,domain=dom)
    check(name+'_only_T0_cubic_pole',s.cancel(raw-regular.as_expr()-polar)==0
          and regular.degree()==32)
    pulled[name]={'regular_polynomial':[str(regular.nth(j)) for j in range(33)],
                  'coefficient_of_sigma136_y_over_U':str(s.expand(alpha*B.nth(0)/8))}
PABpull=s.Poly(s.cancel(alpha*(U-1)**34*(U+1)*BAB.as_expr().subs(v,ww)/(16*U)),U,domain=dom)
PHpull=s.Poly(s.cancel(alpha*(U-1)**35*ZH.as_expr().subs(v,ww)/(16*U)),U,domain=dom)
check('AB_normtwo_J_plus',s.expand(PABpull.as_expr()-U**33*PABpull.as_expr().subs(U,1/U))==0)
check('H_normtwo_J_minus',s.expand(PHpull.as_expr()+U**33*PHpull.as_expr().subs(U,1/U))==0)
check('both_normtwo_primitives_holomorphic',PABpull.degree()==32 and PHpull.degree()==32)

# Both actual odd CM lines, with their complete original theta normalization.
CMi=m.Qbe**3*m.Kbe
CMibar=m.Qba**3*m.Kba
check('two_odd_twisted_CM_lines',all(s.expand(z)==0 for z in Mi*m.vector(CMi)+m.pi*m.vector(CMi))
      and all(s.expand(z)==0 for z in Mi*m.vector(CMibar)+m.pi*m.vector(CMibar)))
CMeven=s.Poly(U,U,domain=dom)*m.Qbe**4+m.Kbe**4
CMboundary=s.expand((ell*ve18(CMeven))[0])
check('known_theta_CM_boundary_nonzero',CMboundary!=0)
def gaussian(z):
    return dom.to_sympy(dom.from_sympy(s.expand(z)))
ca=dom.to_sympy(-dom.from_sympy(a0)/(2*dom.from_sympy(CMboundary)))
cb=dom.to_sympy(-dom.from_sympy(b0)/(2*dom.from_sympy(CMboundary)))
def lift_untwisted(S):
    coeff=[s.Integer(0)]*18
    for j in range(17,0,-1):
        coeff[j-1]=s.expand((S.nth(j)-(70-4*j)*coeff[j])/(4*j-72))
    out=s.Poly(sum(coeff[j]*U**j for j in range(17)),U,domain=dom)
    check('CM_boundary_lift_'+str(len([k for k in checks if k.startswith('CM_boundary_lift_')])),
          all(s.expand(z)==0 for z in MU*m.vector(out)-ve18(S)))
    return out
PGAc=lift_untwisted(SA-CMeven.mul_ground(ca))
PGBc=lift_untwisted(SB-CMeven.mul_ground(cb))
check('CM_corrected_primitives_return_AB',PGAc.mul_ground(b0)-PGBc.mul_ground(a0)==PGAB)
check('CM_corrected_primitives_actual_first_jets',s.expand(PGAc.nth(16)-ca/4)==0
      and s.expand(PGBc.nth(16)-cb/4)==0)

def fq(z):
    return fmpq(str(z))
def pair(z):
    z=s.expand(z)
    return fq(s.re(z)),fq(s.im(z))
Nr=fmpq_mat(17,17);Nj=fmpq_mat(17,17)
for j in range(17):
    for k in range(17):
        ar,ai=pair(Ni[k,j]);Nr[k,j]=ar;Nj[k,j]=ai
x=fmpq_mat(17,1,[fq(PGH.nth(j)) for j in range(17)])
y=fmpq_mat(17,1)
orbit=[]
for n in range(16):
    orbit.append((x,y))
    x,y=Nr*x-Nj*y,Nr*y+Nj*x
realblock=fmpq_mat(34,32)
for j,(x,y) in enumerate(orbit):
    for k in range(17):
        realblock[k,j]=x[k,0];realblock[k+17,j]=y[k,0]
        realblock[k,j+16]=-y[k,0];realblock[k+17,j+16]=x[k,0]
check('H_primitive_all_sixteen_characters',realblock.rank()==32)
reduced,rk=realblock.transpose().rref()
rank_rows=[next(j for j in range(34) if reduced[n,j]) for n in range(rk)]
minor=fmpq_mat(32,32,[realblock[i,j] for i in rank_rows for j in range(32)])
rank_det=minor.det()
check('H_primitive_exact_rank_minor',rank_det!=0)
xx=fmpq_mat(17,1);yy=fmpq_mat(17,1)
for j,(x,y) in enumerate(orbit):
    xx+=(-1)**j*x;yy+=(-1)**j*y
xx/=16;yy/=16
vCM=s.Matrix([s.Rational(str(xx[j,0]))+s.I*s.Rational(str(yy[j,0])) for j in range(17)])
aa,bb=s.symbols('aa bb')
B=s.Matrix.hstack(m.vector(CMi),m.vector(CMibar))
sol=s.solve(list((B*s.Matrix([aa,bb])-vCM)[:2]),(aa,bb))
check('H_primitive_exact_CM_projection',all(s.expand(z)==0 for z in B*s.Matrix([sol[aa],sol[bb]])-vCM))
cmfirst=s.expand(-sum(sol[z]*P.nth(16) for z,P in [(aa,CMi),(bb,CMibar)]))
check('H_primitive_CM_projection_first_jet_nonzero',cmfirst==s.Rational(200236036963,1079445540569088))

# The native untwisted odd block: true finite trace, not a conjugate matrix.
def row_untwisted(a):
    f=s.Poly(U,U,domain=dom)*m.Qp**4-(m.Kp**4).mul_ground(a)
    ub=(s.Poly(U,U,domain=dom)*m.Qb**4*m.inv(m.Kb**4,f)).rem(f)
    mult=m.ipow((m.Kb*m.inv(m.Kp,f)).rem(f),65,f)
    mult=(mult*m.Qp*m.Pb*m.inv(m.Qb*m.Pp,f)).rem(f)
    vals=[]
    for j in range(17):
        vals.append((mult*f.diff()).rem(f).nth(4))
        mult=(mult*ub).rem(f)
    return vals
if '--reuse-i-matrix' in sys.argv and 'untwisted_i_CM5_matrix_columns' in cache:
    Mui=s.Matrix.hstack(*[s.Matrix([s.sympify(z) for z in col])
                         for col in cache['untwisted_i_CM5_matrix_columns']])
    check('untwisted_i_CM5_held_fiber',cache['checks']['untwisted_i_CM5_held_fiber'])
else:
    uv=[row_untwisted(a) for a in range(2,19)]
    ucols=[m.interpolate([vv[j] for vv in uv],start=2) for j in range(17)]
    uh=row_untwisted(19)
    check('untwisted_i_CM5_held_fiber',all(P.eval(19)==vv for P,vv in zip(ucols,uh)))
    Mui=s.Matrix.hstack(*map(m.vector,ucols))
CMui=m.Qbe*m.Kbe*m.Dbe
CMuibar=m.Qba*m.Kba*m.Dba
ucmv=Mui*m.vector(CMui)
ucmp=next(j for j in range(17) if CMui.nth(j))
ucme=s.expand(ucmv[ucmp]/CMui.nth(ucmp))
check('untwisted_odd_CM_reference_eigenline',all(s.expand(z)==0 for z in ucmv-ucme*m.vector(CMui))
      and all(s.expand(z)==0 for z in Mui*m.vector(CMuibar)-ucme*m.vector(CMuibar)))
print('untwisted CM eigenvalue',ucme,flush=True)
Uni=(Mui/ucme).applyfunc(s.expand)
UND=matrix_domain(Uni)
check('untwisted_normalized_order_sixteen',(UND**16-UND.eye((17,17),dom)).is_zero_matrix)
ug=s.symbols('X')
ucp=UND.charpoly()
uch=s.factor(sum(dom.to_sympy(cc)*ug**(17-j) for j,cc in enumerate(ucp)),extension=s.I)
print('untwisted normalized characteristic polynomial',uch,flush=True)
expected_uch=(ug-1)**2*(ug+1)*(ug-s.I)*(ug+s.I)*(ug**4-s.I)**2*(ug**4+s.I)
check('untwisted_exact_characteristic_polynomial',s.expand(uch-expected_uch)==0)
Ur=fmpq_mat(17,17);Uj=fmpq_mat(17,17)
for j in range(17):
    for k in range(17):
        rr,jj=pair(Uni[k,j]);Ur[k,j]=rr;Uj[k,j]=jj
def make_orbit(P):
    pairs=[pair(P.nth(j)) for j in range(17)]
    x=fmpq_mat(17,1,[rr for rr,jj in pairs]);y=fmpq_mat(17,1,[jj for rr,jj in pairs])
    orb=[]
    for n in range(16):
        orb.append((x,y));x,y=Ur*x-Uj*y,Ur*y+Uj*x
    return orb
def orbit_rank_certificate(orbits):
    vv=[vec for orb in orbits for vec in orb]
    nn=len(vv)
    mat=fmpq_mat(34,2*nn)
    for j,(x,y) in enumerate(vv):
        for k in range(17):
            mat[k,j]=x[k,0];mat[k+17,j]=y[k,0]
            mat[k,j+nn]=-y[k,0];mat[k+17,j+nn]=x[k,0]
    rr,rank=mat.rref()
    colp=[next(j for j in range(2*nn) if rr[n,j]) for n in range(rank)]
    selected=fmpq_mat(34,rank,[mat[i,j] for i in range(34) for j in colp])
    tr,rank2=selected.transpose().rref()
    rowp=[next(j for j in range(34) if tr[n,j]) for n in range(rank2)]
    minor=fmpq_mat(rank,rank,[mat[i,j] for i in rowp for j in colp])
    return {'complex_rank':rank//2,'real_minor_rows':rowp,'real_minor_columns':colp,
            'real_minor_determinant':str(minor.det())}
orbits_u={name:make_orbit(P) for name,P in [('AB',PGAB),('A_CM',PGAc),('B_CM',PGBc)]}
rank_u={name:orbit_rank_certificate([orb]) for name,orb in orbits_u.items()}
rank_u['joint_A_B_CM']=orbit_rank_certificate([orbits_u['A_CM'],orbits_u['B_CM']])
print('untwisted actual primitive orbit ranks',{name:rr['complex_rank'] for name,rr in rank_u.items()},flush=True)

out={'status':'PASS','checks':checks,
     'basis':'V_i=(W*x/y)=-x*theta*sigma^67; V_i*U^j, j=0..16',
     'CM5_matrix_columns':[[str(s.expand(Mi[i,j])) for i in range(17)] for j in range(17)],
     'normalization':'N_i=M_i/(2+i)',
     'normalized_characteristic_polynomial':str(charpoly),
     'L_diagonal':[-4*(17-j) for j in range(17)],
     'connection_commutator_ranks':rank_data,
     'untwisted_i_CM5_matrix_columns':[[str(s.expand(Mui[i,j])) for i in range(17)] for j in range(17)],
     'untwisted_odd_CM_eigenvalue':str(ucme),
     'untwisted_normalized_characteristic_polynomial':str(uch),
     'original_H_primitive_P':[str(PGH.nth(j)) for j in range(17)],
     'original_AB_primitive_P':[str(PGAB.nth(j)) for j in range(17)],
     'untwisted_first_order_matrix_rows':[[str(z) for z in rr] for rr in MU.tolist()],
     'untwisted_cokernel':[str(z) for z in ell],
     'original_boundary_constants':{'A':str(a0),'B':str(b0)},
     'normtwo_A_B_regular_plus_pole':pulled,
     'normtwo_AB_primitive_polynomial':[str(PABpull.nth(j)) for j in range(33)],
     'normtwo_H_primitive_polynomial':[str(PHpull.nth(j)) for j in range(33)],
     'theta_twice_beta_CM_polynomial':[str(CMeven.nth(j)) for j in range(18)],
     'theta_twice_beta_CM_boundary':str(CMboundary),
     'CM_boundary_compensation_coefficients':{'A':str(ca),'B':str(cb)},
     'CM_corrected_A_primitive_polynomial':[str(PGAc.nth(j)) for j in range(17)],
     'CM_corrected_B_primitive_polynomial':[str(PGBc.nth(j)) for j in range(17)],
     'untwisted_actual_primitive_orbit_certificates':rank_u,
     'twisted_odd_CM_polynomial':[str(CMi.nth(j)) for j in range(17)],
     'untwisted_odd_CM_polynomial':[str(CMui.nth(j)) for j in range(17)],
     'H_primitive_CM_coefficients':[str(sol[aa]),str(sol[bb])],
     'H_primitive_CM_first_jet':str(cmfirst),
     'H_primitive_complex_Krylov_rank':16,
     'H_primitive_rank_certificate_rows':rank_rows,
     'H_primitive_rank_certificate_determinant':str(rank_det),
     'scope':'Actual finite theta transport; no central vanishing propagated from L being invertible.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS',len(checks),'checks; trace(M_i)=',s.expand(s.trace(Mi)),flush=True)
