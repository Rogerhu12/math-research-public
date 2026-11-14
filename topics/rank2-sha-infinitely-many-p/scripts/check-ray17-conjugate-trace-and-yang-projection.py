#!/usr/bin/env python3
"""Exact rational ray functions and conjugate CM17 theta trace.

R248: exact fixed rational functions, finite flat traces and Yang projections.
The proof supplies the global degree bounds; interpolation uses exact Q(i)
arithmetic. No varying target prime, theta approximation or dense level-4624
matrix is used. Requires SymPy; python-flint is optional for speed.
"""
import json
import sympy as s

U,V=s.symbols('U V')
ii=s.I
dom=s.QQ_I
PR=[-15,256,9512,-51616,135756,161344,998200,-4052192,
    6022934,-4457856,1410136,-9568,-156884,53824,1736,-32,1]
PI=[-8,1832,-16968,49384,9816,-676792,1877912,-2859384,
    198888,2926200,-2286808,423608,89800,4120,-3704,-40,0]
def pp(c,var=U):
    return s.Poly(sum(a*var**j for j,a in enumerate(c)),var,domain=dom)

Pbe=pp([a-ii*b for a,b in zip(PR,PI)])
Pba=pp([a+ii*b for a,b in zip(PR,PI)])
Qbe=pp([1+4*ii,-20-12*ii,-10+28*ii,12-20*ii,1])
Qba=pp([1-4*ii,-20+12*ii,-10-28*ii,12+20*ii,1])
Kbe=pp([-ii,-20-12*ii,28+10*ii,-12+20*ii,4-ii])
Kba=pp([ii,-20+12*ii,28-10*ii,-12-20*ii,4+ii])
Dbe,rr=s.div(Pbe,Qbe**2); assert rr.is_zero
Dba,rr=s.div(Pba,Qba**2); assert rr.is_zero
K=s.Poly(Kbe.as_expr().subs(U,V),V,domain=dom)
g=s.Poly(((1+4*ii)*V**3-(20+12*ii)*V**2+(-11+28*ii)*V+14-20*ii)/4,V,domain=dom)

def comp(f,g,k):
    res=s.Poly(0,k.gens[0],domain=dom)
    for c in f.all_coeffs():
        res=(res*g+s.Poly(c,k.gens[0],domain=dom)).rem(k)
    return res

def inv(f,k):
    return s.invert(f,k)

def ipow(f,j,k):
    out=s.Poly(1,k.gens[0],domain=dom)
    while j:
        if j&1:out=(out*f).rem(k)
        f=(f*f).rem(k);j//=2
    return out

def coefficients(f):
    return [str(f.nth(j)) for j in range(f.degree()+1)]

def interpolate(vals,start=0):
    # Integer-spaced Newton interpolation; only exact Gaussian rationals.
    ds=list(vals); out=s.Poly(0,U,domain=dom); basis=s.Poly(1,U,domain=dom)
    for j in range(len(vals)):
        out+=basis.mul_ground(ds[0])
        ds=[s.expand(b-a) for a,b in zip(ds,ds[1:])]
        basis=(basis*s.Poly(U-start-j,U,domain=dom)).mul_ground(s.Rational(1,j+1))
    return s.Poly(out,U,domain=dom)

def ray_numerators():
    b=inv(s.Poly(V-1,V,domain=dom),K)
    bs=[b]
    for _ in range(3):bs.append(comp(bs[-1],g,K))
    rks=[sum((bs[j].mul_ground(4*ii**(k*j)) for j in range(4)),s.Poly(0,V,domain=dom)).rem(K) for k in (1,2,3)]
    rinv=[inv(r,K) for r in rks]
    num=4*(U**4*V**3-3*U**4*V**2+3*U**4*V-U**4
      +U**3*V**4+34*U**3*V**3-20*U**3*V**2-18*U**3*V+3*U**3
      -3*U**2*V**4-20*U**2*V**3-82*U**2*V**2-20*U**2*V-3*U**2
      +3*U*V**4-18*U*V**3-20*U*V**2+34*U*V+U-V**4+3*V**3-3*V**2+V)
    den=U**2*V**2-2*U**2*V+U**2-2*U*V**2-12*U*V-2*U+V**2-2*V+1
    res=s.Poly(s.resultant(K.as_expr(),den,V),U,domain=dom).monic()
    assert res==Dbe
    vals=[[],[],[]]
    for a in range(17):
        n=s.Poly(num.subs(U,a),V,domain=dom)
        d=s.Poly(den.subs(U,a)**2,V,domain=dom)
        q=(n*inv(d,K)).rem(K)
        qs=[q]
        for _ in range(3):qs.append(comp(qs[-1],g,K))
        for k in (1,2,3):
            ch=sum((qs[j].mul_ground(ii**(k*j)) for j in range(4)),s.Poly(0,V,domain=dom)).rem(K)
            v=(ch*rinv[k-1]).rem(K)
            assert v.degree()==0 or v.is_zero
            vals[k-1].append(s.expand(v.nth(0)*Dbe.eval(a)**2))
    out=[interpolate(v) for v in vals]
    for p in out:assert p.degree()==16 and p.LC()==1
    return out

def trace_at(n,a):
    # U(bar beta z)=U*Qbar(U)^4/Kbar(U)^4.
    f=s.Poly(U,U,domain=dom)*(Qba**4)-(Kba**4).mul_ground(a)
    assert f.degree()==17 and f.LC()==1
    ratio=(Pbe*inv(Pba,f)).rem(f)
    source=(ipow(ratio,17,f)*n*inv(Dbe**2,f)).rem(f)
    tr=(source*f.diff()).rem(f).nth(16)
    return s.expand(tr*a**8*(a-1)**8)


def mass_at_infinity(n):
    # The other sixteen points form four mu_4 orbits on ker(bar beta).
    f=Kba.monic()
    ratio=(Pbe*inv(Pba,f)).rem(f)
    source=(ipow(ratio,17,f)*n*inv(Dbe**2,f)).rem(f)
    return s.expand(1+4*(source*f.diff()).rem(f).nth(3))


pi=2+ii;pib=2-ii;eta=1-2*ii;etab=1+2*ii
Qp=s.Poly(U-eta,U,domain=dom);Kp=s.Poly(pi*U-ii,U,domain=dom)
Qb=s.Poly(U-etab,U,domain=dom);Kb=s.Poly(pib*U+ii,U,domain=dom)
Pp=s.Poly((U-eta)**2*((U-eta)*(pi*U-ii)+4*U*(pi*eta-ii))/pi,U,domain=dom)
Pb=s.Poly((U-etab)**2*((U-etab)*(pib*U+ii)+4*U*(pib*etab+ii))/pib,U,domain=dom)


def cm5_row_at(a):
    f=s.Poly(U,U,domain=dom)*Qp**4-(Kp**4).mul_ground(a)
    assert f.degree()==5 and f.LC()==1
    ub=(s.Poly(U,U,domain=dom)*Qb**4*inv(Kb**4,f)).rem(f)
    mult=ipow((Pb*inv(Pp,f)).rem(f),17,f)
    mult=(mult*inv(ipow(ub,8,f)*ipow(ub-1,8,f),f)).rem(f)
    vals=[]
    for j in range(17):
        tr=(mult*f.diff()).rem(f).nth(4)
        vals.append(s.expand(tr*a**8*(a-1)**8))
        mult=(mult*ub).rem(f)
    return vals


def vector(p):
    return s.Matrix([p.nth(j) for j in range(17)])


def cm5_matrix():
    vals=[cm5_row_at(a) for a in range(2,19)]
    cols=[interpolate([v[j] for v in vals],start=2) for j in range(17)]
    held=cm5_row_at(19)
    assert all(col.eval(19)==v for col,v in zip(cols,held))
    return s.Matrix.hstack(*map(vector,cols)),cols


def eigenvalue(M,p):
    v=vector(p);w=M*v;ind=next(j for j in range(17) if v[j])
    z=s.simplify(w[ind]/v[ind])
    assert all(s.expand(w[j]-z*v[j])==0 for j in range(17))
    return z


def extra_characters(ND,traces):
    """All twelve exact eigensources over Q(i)[Z]/(Z^4-i).

    They are recorded as holomorphic theta sources, without attaching an
    elliptic-curve or unproved arithmetic interpretation.
    """
    Z=s.symbols('Z');qd=s.Poly(Z**4-ii,Z,domain=dom)
    vs=s.Matrix.hstack(*map(vector,traces)).to_DM(domain=dom)
    ps=[vs]
    for _ in range(15):ps.append(ND*ps[-1])
    ps=[p.to_Matrix() for p in ps]
    def elems(r,k):
        out=[]
        for n in range(17):
            cs=[s.Integer(0)]*4
            for j in range(16):
                e=(-r*j)%16
                cs[e%4]+=ii**(e//4)*ps[j][n,k]/16
            out.append(s.Poly(sum(s.expand(c)*Z**a for a,c in enumerate(cs)),
                              Z,domain=dom))
        return out
    def enc(f):return [str(f.nth(j)) for j in range(4)]
    data=[]
    for r in range(16):
        if r%4==0:continue
        vv=[elems(r,k) for k in range(3)]
        assert all(not v[16].is_zero for v in vv)
        iv=s.invert(vv[0][16],qd)
        ref=[(v*iv).rem(qd) for v in vv[0]]
        assert ref[16]==s.Poly(1,Z,domain=dom)
        scalars=[v[16] for v in vv]
        for k in range(3):
            assert all((v-scalars[k]*ref[n]).rem(qd).is_zero
                       for n,v in enumerate(vv[k]))
        data.append({'r':r,'eigenvalue':'zeta16**'+str(r),
            'coefficient_encoding':'[1,zeta16,zeta16**2,zeta16**3] over Q(i)',
            'reference_coefficients':list(map(enc,ref)),
            'reference_mass':['1','0','0','0'],
            'ray_coefficients':list(map(enc,scalars)),
            'ray_projection_masses':list(map(enc,scalars)),
            'ray_projection_masses_nonzero':[True,True,True]})
    return data


def yang_projections(M,traces):
    PH=pp(list(reversed(list(map(s.Rational,(
        '1','-567/55','5799/55','-17527/55','-18057/11','25927/5',
        '-154733/55','-8103/11','94949/55','-136101/55','135253/55',
        '-70277/55','25169/55','-765/11','177/55','-1/55'))))))
    assert eigenvalue(M,Pbe)==2+ii
    assert eigenvalue(M,Pba)==2+ii
    assert eigenvalue(M,PH)==-1+2*ii
    N=M.applyfunc(lambda x:s.expand(x/(2+ii)))
    ND=N.to_DM(domain=dom);ID=s.eye(17).to_DM(domain=dom)
    powers=[ID]
    for _ in range(16):powers.append(powers[-1]*ND)
    assert powers[16]==ID
    char=s.Poly.from_list([dom.to_sympy(c) for c in ND.charpoly()],U,domain=dom)
    assert char==s.Poly((U-1)*(U**16-1),U,domain=dom)
    P4=sum((powers[j] for j in (0,4,8,12)),ID*0).scalarmul(dom(1)/4)
    projs=[]
    for k in range(4):
        P=sum((powers[j].scalarmul(dom.from_sympy(ii**(-k*j)))
               for j in range(4)),ID*0)*P4
        projs.append(P.scalarmul(dom(1)/4))
    refs={1:vector(PH)}
    for k in (2,3):
        eig=(ND-ID.scalarmul(dom.from_sympy(ii**k))).nullspace().to_Matrix()
        assert eig.rows==1
        v=eig.row(0).T;assert v[16]!=0
        refs[k]=v.applyfunc(lambda x:s.simplify(x/v[16]))
    cm1=vector(Pbe);cm2=vector(Pba)
    expected_H=[(886234888+2448712079*ii)/2**26,
                (-3413940145+2467870350*ii)/2**26,
                (2127156460+228850985*ii)/2**26]
    rows=[];extras=[]
    for k,tp in enumerate(traces,1):
        v=vector(tp);vd=v.to_DM(domain=dom)
        es=[(P*vd).to_Matrix() for P in projs]
        coeff=[]
        for j in (1,2,3):
            ref=refs[j];ind=next(q for q in range(17) if ref[q])
            a=s.simplify(es[j][ind]/ref[ind])
            assert all(s.expand(x)==0 for x in es[j]-ref*a)
            coeff.append(a)
        assert s.expand(coeff[0]-expected_H[k-1])==0
        assert all(a!=0 for a in coeff)
        cm=s.Matrix.hstack(cm1,cm2).gauss_jordan_solve(es[0])[0]
        extra=v-sum(es,s.zeros(17,1))
        assert all(x==0 for x in (P4*extra.to_DM(domain=dom)).to_Matrix())
        extras.append(extra)
        rows.append({'ray_character_power':k,
            'primitive_coefficients_H_S2312_S39304':list(map(str,coeff)),
            'primitive_reference_masses':['0','1','1'],
            'primitive_projection_masses':['0',str(coeff[1]),str(coeff[2])],
            'primitive_projection_masses_nonzero':[False,True,True],
            'CM_coefficients_beta_barbeta':list(map(str,cm)),
            'CM_reference_masses':['1','1'],
            'CM_projection_masses':list(map(str,cm)),
            'CM_projection_masses_nonzero':[True,True],
            'extra_polynomial':list(map(str,extra)),
            'extra_mass':str(extra[16]),'total_mass':str(tp.nth(16))})
    emat=s.Matrix.hstack(*extras)
    assert emat.to_DM(domain=dom).rank()==3
    minor=s.expand(emat[[0,1,2],:].det());assert minor!=0
    return {'normalized_primitive_polynomials':{
                str(k):list(map(str,v)) for k,v in refs.items()},
            'CM5_over_2_plus_i_has_order_16':True,
            'CM5_normalized_characteristic_polynomial':'(X-1)*(X**16-1)',
            'projection_rows':rows,
            'twelve_extra_eigensources':extra_characters(ND,traces),
            'extra_columns_rank':3,'extra_minor_rows_0_1_2':str(minor)}


def main():
    ns=ray_numerators()
    traces=[]
    for n in ns:
        vals=[trace_at(n,a) for a in range(2,19)]
        out=interpolate(vals,start=2)
        assert out.eval(19)==trace_at(n,19)
        assert out.nth(16)==mass_at_infinity(n)
        traces.append(out)
    M,cols=cm5_matrix()
    data={'status':'PASS','coefficient_order':'ascending powers of U',
          'D_beta':coefficients(Dbe),
          'normalized_ray_numerators':[coefficients(n) for n in ns],
          'conjugate_trace_polynomials':[coefficients(t) for t in traces],
          'CM5_P_pi':coefficients(Pp),'CM5_P_barpi':coefficients(Pb),
          'CM5_matrix_columns':[coefficients(c) for c in cols],
          **yang_projections(M,traces)}
    print(json.dumps(data,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()

