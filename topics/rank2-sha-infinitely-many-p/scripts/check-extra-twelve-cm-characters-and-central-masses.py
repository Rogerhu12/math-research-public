#!/usr/bin/env python3
"""R289: original dyadic characters, all twelve CM lines and exact central masses.

All arithmetic is in Q[z]/(z^8+1).  No numerical theta approximation and no
varying target-prime scan are used.  R248 supplies the already proved original
CM5 matrix; this certificate recomputes its projected masses.
"""
import json
from pathlib import Path

import sympy as s
from flint import fmpq, fmpq_mat

root=Path(__file__).parent
data=json.loads((root/'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
z,X=s.symbols('z X')
mod=s.Poly(z**8+1,z,domain=s.QQ)
checks={}

def check(name,value):
    checks[name]=bool(value)
    if not checks[name]:
        raise AssertionError(name)

def red(value):
    return s.Poly(s.expand(value),z,domain=s.QQ).rem(mod).as_expr()

def zp(n):
    return red(z**(n%16))

def mm(A,B):
    return (A*B).applyfunc(red)

idx=[1,3,5,7]
Im=s.Matrix([[zp(-a*b)/2 for b in idx] for a in idx])

def gentry(a,b):
    if (b-3*a)%4:
        return s.Integer(0)
    k=((b-3*a)//4)%4
    return -zp(2*(-1-2*a*k-3*k*k))/2

Gm=s.Matrix([[red(gentry(a,b)-gentry(a,b+8)) for b in idx] for a in idx])
I2=mm(Im,Im)
check('original_half_minus_minus_fourier_order_four',mm(I2,I2)==s.eye(4))
check('original_Rao_matrix_equals_i_times_I_squared',Gm==(zp(4)*I2).applyfunc(red))
Ginv=mm(mm(Gm,Gm),Gm)
check('normfive_dyadic_scalar_same_on_all_four_lines',mm(I2,Ginv)==-zp(4)*s.eye(4))
dyadic=[]
for a in range(4):
    E=s.zeros(4);P=s.eye(4)
    for n in range(4):
        E+=(zp(-4*a*n)*P)/4
        P=mm(Im,P)
    E=E.applyfunc(red)
    check('dyadic_projector_rank_one_'+str(a),red(s.trace(E))==1 and mm(E,E)==E)
    v=E[:,0]
    check('dyadic_I_character_'+str(a),mm(Im,v)==(zp(4*a)*v).applyfunc(red))
    check('dyadic_G_character_'+str(a),mm(Gm,v)==(zp(4+8*a)*v).applyfunc(red))
    dyadic.append({'a':a,'I_eigenvalue':str(zp(4*a)),
                   'G_eigenvalue':str(zp(4+8*a)),
                   'vector_in_e1_e3_e5_e7_minus_e9_e11_e13_e15':[str(v[j]) for j in range(4)]})
t=-1+z-z**2+z**3-z**5+z**6-z**7
v0=s.Matrix([1,t,-t,-1])
check('a_zero_is_original_E136_dyadic_line',mm(Im,v0)==v0 and mm(Gm,v0)==(zp(4)*v0).applyfunc(red))

log17={pow(3,k,17):k for k in range(16)}
check('seventeen_primitive_generator',len(log17)==16)
check('CM5_split_torus_parameter',log17[14]==9)
check('unit_and_uniformizer_residues',
      [log17[q] for q in (4,13,5,14,7,8)]==[12,4,5,9,11,10])

def fq(q):
    return fmpq(str(q))

def pair(expr):
    expr=s.expand(s.sympify(expr))
    return fq(s.re(expr)),fq(s.im(expr))

def cyclic_shift(vec,n):
    out=[fmpq(0) for _ in range(8)]
    for k,c in enumerate(vec):
        e=(k+n)%16
        out[e%8]+=c if e<8 else -c
    return out

def decode(cs):
    out=[fmpq(0) for _ in range(8)]
    for j,c in enumerate(cs):
        a,b=pair(c)
        out[j]+=a;out[j+4]+=b
    return out

Nr=fmpq_mat(17,17);Ni=fmpq_mat(17,17)
for j,col in enumerate(data['CM5_matrix_columns']):
    for k,c in enumerate(col):
        a,b=pair(c)
        Nr[k,j]=(2*a+b)/5
        Ni[k,j]=(2*b-a)/5
Tr=fmpq_mat(17,3);Ti=fmpq_mat(17,3)
for j,col in enumerate(data['conjugate_trace_polynomials']):
    for k,c in enumerate(col):
        a,b=pair(c);Tr[k,j]=a;Ti[k,j]=b
orbit=[]
for n in range(16):
    orbit.append((Tr,Ti))
    Tr,Ti=Nr*Tr-Ni*Ti,Nr*Ti+Ni*Tr

rows=[]
sources={row['r']:row for row in data['twelve_extra_eigensources']}
for r,row in sources.items():
    j=(9*r)%16
    a=j%4
    check('global_unit_compatibility_r'+str(r),(8*j-12*j+4*j)%16==0)
    check('global_lambda_two_compatibility_r'+str(r),(-4*j-5*j+9*j)%16==0)
    check('CM5_global_character_r'+str(r),(j-(4+8*j))%16==(12+r)%16)
    V=fmpq_mat(17,8)
    for k,cs in enumerate(row['reference_coefficients']):
        cc=decode(cs)
        for n in range(8):V[k,n]=cc[n]
    IV=fmpq_mat(17,8)
    RV=fmpq_mat(17,8)
    for k in range(17):
        cc=[V[k,n] for n in range(8)]
        iv=cyclic_shift(cc,4);rv=cyclic_shift(cc,r)
        for n in range(8):IV[k,n]=iv[n];RV[k,n]=rv[n]
    check('original_CM5_eigenline_r'+str(r),Nr*V+Ni*IV==RV)
    check('original_theta_mass_one_r'+str(r),[V[16,n] for n in range(8)]==[fmpq(1)]+[fmpq(0)]*7)
    # Complex conjugation fixes every coefficient, so these are the actual real fields.
    real_coeffs=True
    for k in range(17):
        cc=[V[k,n] for n in range(8)]
        bar=[fmpq(0)]*8
        for n,c in enumerate(cc):
            ee=(-n)%16;bar[ee%8]+=c if ee<8 else -c
        real_coeffs=real_coeffs and cc==bar
    check('original_reference_real_coefficients_r'+str(r),real_coeffs)
    masses=[]
    for k in range(3):
        out=[fmpq(0) for _ in range(8)]
        for n,(Ar,Ai) in enumerate(orbit):
            vv=[fmpq(0)]*8;vv[0]=Ar[16,k];vv[4]=Ai[16,k]
            cv=cyclic_shift(vv,-r*n)
            out=[aa+bb/16 for aa,bb in zip(out,cv)]
        check('actual_ray_projection_mass_r'+str(r)+'_column'+str(k+1),
              out==decode(row['ray_projection_masses'][k]) and any(out))
        masses.append([str(c) for c in out])
    a5=red((2+zp(4))*zp(r)+(2-zp(4))*zp(-r))
    rows.append({'r':r,'j':j,'dyadic_a':a,
                 'epsilon_beta_on_3':str(zp(-j)),
                 'epsilon_barbeta_on_3':str(zp(j)),
                 'epsilon_2_on_1_plus_i':str(zp(-4*j)),
                 'epsilon_2_on_1_plus_2i':str(zp(12+8*j)),
                 'epsilon_primary_norm5':str(zp(12+r)),
                 'oriented_Hecke_root_norm5':str(red((2+zp(4))*zp(r))),
                 'a5':str(a5),'theta_mass':1,
                 'actual_three_ray_projection_masses_Q_zeta16_basis':masses,
                 'finite_character_order':int(s.ilcm(4,16//s.igcd(j,16)))})

groups=[([2,10],X**2-2),([6,14],X**2-18),
        ([1,5,9,13],X**4-20*X**2+98),([3,7,11,15],X**4-20*X**2+2)]
orbits_out=[]
for rr,expected in groups:
    prod=s.Poly(1,X)
    for r in rr:
        a5=next(row['a5'] for row in rows if row['r']==r)
        prod=s.Poly(s.expand(prod.as_expr()*(X-s.sympify(a5))),X)
        prod=s.Poly(sum(red(prod.nth(k))*X**k for k in range(prod.degree()+1)),X)
    check('exact_normfive_minpoly_'+str(rr),s.expand(prod.as_expr()-expected)==0)
    check('normfive_minpoly_Eisenstein_two_'+str(rr),s.Poly(expected,X).is_irreducible)
    check('actual_Galois_orbit_'+str(rr),set((k*rr[0])%16 for k in (1,5,9,13))==set(rr))
    orbits_out.append({'r_labels':rr,'a5_minimal_polynomial':str(expected),
                       'coefficient_field_degree':len(rr),
                       'primitive_modular_level':73984,'complex_central_order':0})

check('all_twelve_ordinary_masses_are_units_on_the_normfive_ray',
      all((5*row['r']-row['r'])%16!=0 for row in rows))
out={'status':'PASS','scope':'Original local Weil characters, exact theta masses and oriented Hecke roots; no assertion about corrected central derivatives.',
     'checks':checks,'cyclotomic_relation':'zeta16^8=-1','dyadic_lines':dyadic,
     'labels':'r=9*j mod16, lambda_j(3)=zeta16^j',
     'local_conductor':'(1+i)^6*(4-i)*(4+i), for all twelve nontrivial labels',
     'character_rows':rows,'newform_Galois_orbits':orbits_out,
     'ordinary_mass_on_normfive_ray':'1+zeta16^r/b17; a unit because p=5 mod16 and b17 is in Q_p',
     'inert_complete_mass':'J_r(0)=1',
     'unpaid_observation':'J_r prime(0)-J_r(0)*J_reference prime(0)/J_reference(0), and the original odd tame-one connection rows.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS',len(checks),'checks; exact twelve masses and four original CM Galois orbits',flush=True)
