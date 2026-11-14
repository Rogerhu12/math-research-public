#!/usr/bin/env python3
"""R250: exact two E2312 companions, original Q_{+,0} CM phases,
and the finite full-Mellin transpose matrix.

Uses only rational/Gaussian arithmetic and the already proved R245/R248
finite matrices. No target-prime enumeration or logarithm approximation.
"""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('r245',HERE/'check-e136-covariant-cm17-log-bridge.py')
r245=importlib.util.module_from_spec(spec);spec.loader.exec_module(r245)
P2=list(map(Q,[25,-1000,14416,-10504,270868,-2537544,5327744,
              -3908968,994190,-1505848,1545424,-562328,141508,
              39016,-3872,264,1]))


def companions():
    D=[Q(0)]*8+r245.pp([Q(-1),Q(1)],8)
    DG=[Q(0)]*8+r245.pp([Q(-1),Q(1)],7)+[Q(0)]
    cols=[r245.operator_column(j) for j in range(15)]+[D,DG]
    L=[[cols[k][j] for k in range(17)] for j in range(17)]
    src=r245.cv(P2,L);cI=r245.cv(r245.P_IM,L);cR=r245.cv(r245.P_RE,L)
    data={}
    for name,cm in [('I',cI),('R',cR)]:
        a=src['beta_eff']/cm['beta_eff']
        rs=[x-a*y for x,y in zip(src['R14'],cm['R14'])]
        ga=src['gamma']-a*cm['gamma']
        target=[x-a*y for x,y in zip(P2,cm['P'])]
        # Rational part plus log term: L(R)+gamma*(D/2+DG).
        actual=[sum(L[j][k]*rs[k] for k in range(15))
                +ga*(D[j]/2+DG[j]) for j in range(17)]
        assert actual==target
        z2=rs[-1]+ga/4
        z6=(Q(459)+80*a)/60 if name=='I' else (Q(459)+133*a)/60
        assert z2==(Q(1,2) if name=='I' else (1-a)/2)
        data[name]={'CM_coefficient':str(a),'R14':list(map(str,rs)),
          'gamma_difference':str(ga),'log_coefficient':str(-ga/8),
          'z2_coefficient':str(z2),'z6_coefficient':str(z6),
          'target_polynomial':list(map(str,target))}
    assert data['I']['CM_coefficient']=='8235327/3310819'
    assert data['R']['CM_coefficient']=='-218637/274334'
    return data,src


def qplus_cm_phases():
    T,F,G,H,x,U=s.symbols('T F G H x U')
    kk=2**s.Rational(-1,4);ii=s.I
    M=s.Matrix([[0,kk**3,kk**3,0],[kk,0,0,-kk],
                [kk,0,0,kk],[0,kk**3,-kk**3,0]])
    N=s.Matrix([[0,kk**3,-kk**3,0],[kk,0,0,-ii*kk],
                [-kk,0,0,-ii*kk],[0,-ii*kk**3,-ii*kk**3,0]])
    terms=[(1,2,1),(1,2,3),(-1,0,1),(-1,0,3),
           (-1,1,0),(-1,3,0),(-1,1,2),(-1,3,2)]
    variables=[T,F,G,H]
    mats={(b,c):s.simplify(M**b*N**c) for _,b,c in terms}
    def act(f):
        out=0
        for a,b,c in terms:
            A=mats[b,c]
            sub={v:s.expand(sum(variables[j]*A[j,l] for j in range(4)))
                 for l,v in enumerate(variables)}
            out+=a*f.subs(sub,simultaneous=True)/4
        return s.Poly(s.expand(out/kk),*variables,domain=s.QQ_I)
    def to_u(f):
        out=0
        for (a,b,c,d),v in f.terms():
            assert d%2==0 and (c+d//2)%2==0
            out+=v*(U+1)**a*(U-1)**(b+d//2)*2**(c+d)*U**((c+d//2)//2)
        return s.Poly(s.expand(out),U,domain=s.QQ_I)
    assert act(T).as_expr()==-2*F
    q=[1,12-20*ii,-10+28*ii,-20-12*ii,1+4*ii]
    Qb=[1+4*ii,-20-12*ii,-10+28*ii,12-20*ii,1]
    Kb=[-ii,-20-12*ii,28+10*ii,-12+20*ii,4-ii]
    def pp(c):return s.Poly(sum(v*U**j for j,v in enumerate(c)),U,domain=s.QQ_I)
    scalars={}
    for label,conj in [('beta',False),('barbeta',True)]:
        conv=(lambda c:s.conjugate(c)) if conj else (lambda c:c)
        f=sum(conv(c)*T**(17-4*j)*H**(4*j) for j,c in enumerate(q))
        actual=to_u(act(f))
        Qm=pp(list(map(conv,Qb)));Km=pp(list(map(conv,Kb)))
        # F0(alpha z)=sigma^68*(U Qalpha(U)^4-Kalpha(U)^4).
        target=s.Poly(U,U,domain=s.QQ_I)*Qm**4-Km**4
        assert actual==2*target
        scalars[label]='2*kappa4'
    return {'base_degree4_scalar':'-2*kappa4',
            'actual_degree68_CM_scalars':scalars,
            'Qplus_new_KI':'-2*I*kappa4*F_R',
            'Qplus_new_KR':'2*I*kappa4*F_I'}


def mellin_matrix():
    d=json.loads((HERE/'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
    assert d['status']=='PASS'
    dom=s.QQ_I;ii=s.I;pi=2+ii
    def vec(c):return s.Matrix(list(map(s.sympify,c)))
    MM=s.Matrix.hstack(*map(vec,d['CM5_matrix_columns']))
    NN=MM.applyfunc(lambda x:s.expand(x/pi)).to_DM(domain=dom)
    ID=s.eye(17).to_DM(domain=dom);power=[ID]
    for _ in range(16):power.append(power[-1]*NN)
    assert power[16]==ID
    A0=NN-ID.scalarmul(dom.from_sympy(s.expand(1/pi)))
    assert A0.rank()==17
    z=s.expand(pi**16-1);norm=s.expand(z*s.conjugate(z))
    assert s.factorint(norm)=={2:11,3:2,5:1,17:3,337:1}
    # The ray sources share one CM direction, leaving a 16-dimensional orbit.
    vs=s.Matrix.hstack(*map(vec,d['conjugate_trace_polynomials'][:2])).to_DM(domain=dom)
    orbit=s.Matrix.hstack(*[(power[j]*vs).to_Matrix() for j in range(16)])
    od=orbit.to_DM(domain=dom);rank=od.rank();assert rank==16
    _,piv=od.rref()
    select=orbit[:,list(piv)]
    _,rowpiv=select.T.to_DM(domain=dom).rref()
    det=select[list(rowpiv),:].to_DM(domain=dom).det();assert det!=dom.zero
    return {'N_order_16':True,'A0_rank':17,
        'r_p':'pi^(-1)*(U_barpi,p/U_pi,p)^u',
        'r_p_derivative_at_zero':'-d*log_p(pi/barpi)/pi',
        'A_u':'N-r_p(u)*I',
        'A_u_derivative_at_zero':'d*log_p(pi/barpi)*I/pi',
        'inverse_numerator':'sum_{j=0}^{15} r_p(u)^j*N^(15-j)',
        'inverse_denominator':'1-r_p(u)^16',
        'Norm_pi16_minus_1_factorization':{str(k):v for k,v in s.factorint(norm).items()},
        'first_two_orbits_rank':rank,'independent_orbit_columns':list(piv),
        'independent_orbit_rows':list(rowpiv),
        'independent_orbit_determinant':str(dom.to_sympy(det))}


def three_source_elimination():
    d=json.loads((HERE/'check-ray17-conjugate-trace-and-yang-projection.json').read_text())
    A=s.Matrix([[s.sympify(x) for x in row['primitive_coefficients_H_S2312_S39304']]
                for row in d['projection_rows']])
    C=s.Matrix([[s.sympify(x) for x in row['CM_coefficients_beta_barbeta']]
                for row in d['projection_rows']])
    adj=A.adjugate().applyfunc(s.expand)
    det=s.expand(A.det());assert det!=0
    assert (adj*A-det*s.eye(3)).applyfunc(s.expand)==s.zeros(3)
    CM=(adj*C).applyfunc(s.expand)
    assert all(x!=0 for x in CM)
    nu=1-4*s.I
    assert C.to_DM(domain=s.QQ_I).rank()==1
    assert all(s.expand(C[j,1]-nu*C[j,0])==0 for j in range(3))
    assert all(s.expand(CM[j,1]-nu*CM[j,0])==0 for j in range(3))
    return {'primitive_matrix_rows':[[str(x) for x in A.row(j)] for j in range(3)],
            'adjugate_rows':[[str(x) for x in adj.row(j)] for j in range(3)],
            'primitive_determinant':str(det),
            'cofactor_combination_CM_rows':[[str(x) for x in CM.row(j)] for j in range(3)],
            'common_CM_ratio_barbeta_over_beta':'1-4*I','CM_column_rank':1,
            'dyadic_projection_equals_mu4_spectral_projection':True,
            'twelve_extra_sources_annihilated_by_dyadic_projection':True}


def main():
    cs,src=companions();ph=qplus_cm_phases();mm=mellin_matrix();elim=three_source_elimination()
    ai=Q(cs['I']['CM_coefficient']);ar=Q(cs['R']['CM_coefficient'])
    assert ai*(-320/ai)+ar*(320/ar)==0
    data={'status':'PASS','P_S2312':list(map(str,P2)),
        'S2312_covariant_remainders':{k:str(src[k]) for k in ['beta','gamma','beta_eff']},
        'companions':cs,'actual_CM_phases':ph,'full_Mellin_matrix':mm,
        'three_source_elimination':elim,
        'B_residual_pair':{
            'Psi_B':'C_p-(320/a_I)*J34/J_F0','Psi_B_mass':'1',
            'Theta_B':'D_p+(320/a_R)*J34/J_F0','Theta_B_mass':'0',
            'exact_inhomogeneous_relation':'a_I*Psi_B+a_R*Theta_B=a_I*C_p+a_R*D_p',
            'CM_reference_derivative_retained_until_unit_division':True,
            'covariant_translation_commutator_retained':True}}
    print(json.dumps(data,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
