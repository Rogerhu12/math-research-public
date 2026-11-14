#!/usr/bin/env python3
"""Recover the *scalar* p^2 Robert finite input from published R198 inputs.

This is new recovery source, not a byte-for-byte copy of the lost R380 code.
All arithmetic is exact.  No old scalar output or its expected logarithm is
used as an arithmetic input.  Only this script's checkpoint may be resumed.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

from flint import fmpz_mod_poly_ctx, fq_default_ctx, fq_default_poly_ctx

PORDER = 43
INPUT = Path(__file__).resolve().parents[1] / 'notes/r198_p_squared_robert_certificate.json'
HERE = Path(__file__).resolve().parent


def dump(path, data):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2) + '\n')
    tmp.replace(path)


def coords(v):
    return [str(int(c)) for c in v.to_list()]


def pneg(P):
    return None if P is None else (P[0], -P[1])


def padd(P, Q, a):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u:
        if y + v == 0:
            return None
        lam = (3*x*x+a)/(2*y)
    else:
        lam = (v-y)/(u-x)
    r = lam*lam-x-u
    return (r, lam*(x-r)-y)


def jdbl(P, a):
    X, Y, Z = P
    if Z == 0 or Y == 0:
        return (X*0+1, X*0+1, X*0)
    A, B = X*X, Y*Y
    C = B*B
    D = 2*((X+B)*(X+B)-A-C)
    E = 3*A+a*(Z*Z)*(Z*Z)
    F = E*E
    V = F-2*D
    return (V, E*(D-V)-8*C, 2*Y*Z)


def jadd(P, Q, a):
    if Q is None:
        return P
    X, Y, Z = P
    if Z == 0:
        return (Q[0], Q[1], Q[0]*0+1)
    Z2 = Z*Z
    U, S = Q[0]*Z2, Q[1]*Z2*Z
    H, R = U-X, 2*(S-Y)
    if H == 0:
        return jdbl(P, a) if R == 0 else (X*0+1, X*0+1, X*0)
    HH = H*H
    I = 4*HH
    J, V = H*I, X*I
    r = R*R-J-2*V
    return (r, R*(V-r)-2*Y*J, (Z+H)*(Z+H)-Z2-HH)


def pmul(P, n, a):
    if P is None or n == 0:
        return None
    if n < 0:
        return pmul(pneg(P), -n, a)
    R = (P[0]*0+1, P[0]*0+1, P[0]*0)
    for bit in bin(n)[2:]:
        R = jdbl(R, a)
        if bit == '1':
            R = jadd(R, P, a)
    X, Y, Z = R
    if Z == 0:
        return None
    zi = Z.inverse()
    return (X*zi*zi, Y*zi*zi*zi)


def on(P, a, b):
    return P is None or P[1]*P[1] == P[0]**3+a*P[0]+b


def ip(P, ii):
    return None if P is None else (-P[0], ii*P[1])


def beta_point(P, a, ii):
    return padd(pneg(P), pmul(ip(P, ii), 2, a), a)


def velu(a, b, P, ell):
    R, ker, ts, ws = P, [], a*0, a*0
    for k in range(1, (ell+1)//2):
        assert R is not None and on(R, a, b), ('kernel', k)
        u, v = R
        w, t = 4*v*v, 6*u*u+2*a
        ker.append((u, t, w))
        ts += t
        ws += w+u*t
        R = padd(R, P, a)
    return {'a': a-5*ts, 'b': b-7*ws, 'ker': ker}


def phi(E, P):
    if P is None:
        return None
    ds = [P[0]-u for u, t, w in E['ker']]
    if any(d == 0 for d in ds):
        return None
    pre, acc = [], P[0]*0+1
    for d in ds:
        pre.append(acc)
        acc *= d
    invs = [None]*len(ds)
    back = acc.inverse()
    for j in range(len(ds)-1, -1, -1):
        invs[j] = back*pre[j]
        back *= ds[j]
    x, fac = P[0], P[0]*0+1
    for (u,t,w), d in zip(E['ker'], invs):
        d2 = d*d
        x += t*d+w*d2
        fac -= t*d2+2*w*d2*d
    R = (x, P[1]*fac)
    assert on(R, E['a'], E['b']), 'Velu image equation'
    return R


def psi11(x, a, b):
    x2=x*x; x3=x2*x; x4=x2*x2; x6=x3*x3
    a2=a*a; b2=b*b; v=4*(x3+a*x+b); v2=v*v
    o3=3*x4+6*a*x2+12*b*x-a2
    e4=2*(x6+5*a*x4+20*b*x3-5*a2*x2-4*a*b*x-8*b2-a2*a)
    o33=o3*o3*o3
    o5=v2*e4-o33
    e6=o3*(o5-e4*e4)
    o7=o5*o33-v2*e4*e4*e4
    return o7*o5*o5*o5-v2*e4*e6*e6*e6


def discr(a, b):
    return -16*(4*a*a*a+27*b*b)


def scalar(c):
    v=c.to_list()
    assert all(int(z)==0 for z in v[1:]), 'Fq coordinate'
    return int(v[0]) if v else 0


def miller(P, Q, n, a):
    R, f = P, P[0]*0+1
    def line(U,V):
        if U[0] == V[0] and U[1]+V[1] == 0:
            return Q[0]-U[0]
        s=(3*U[0]*U[0]+a)/(2*U[1]) if U[0]==V[0] else (V[1]-U[1])/(V[0]-U[0])
        W=padd(U,V,a)
        num=Q[1]-U[1]-s*(Q[0]-U[0])
        return num/(Q[0]-W[0]) if W is not None else num
    for bit in bin(n)[3:]:
        f=f*f*line(R,R); R=padd(R,R,a)
        if bit=='1':
            f=f*line(R,P); R=padd(R,P,a)
    assert R is None
    return f


def resultant(f, g, field):
    """Exact Euclidean resultant, with all leading-coefficient factors."""
    out=field.one()
    while g.degree()>0:
        m,n=f.degree(),g.degree()
        r=f%g
        if r.is_zero():
            return field.zero()
        if (m*n)&1:
            out=-out
        out*=g.leading_coefficient()**(m-r.degree())
        f,g=g,r
    return out*g.constant_coefficient()**f.degree()


def setup(C):
    q=int(C['q']); pc=fmpz_mod_poly_ctx(q)
    F2=fq_default_ctx(modulus=pc([1,0,1]), check_prime=False)
    ii=F2.gen(); a=F2(-1); zero=F2(0)
    cv=lambda pair:F2([int(x) for x in pair])
    P=tuple(map(cv,C['P'])); P2=(ii,1-ii)
    T5=tuple(map(cv,C['T5_beta'])); zeta=cv(C['zeta_Weil'])
    assert q%172==171 and ((q+1)//43)%43==11
    assert on(P,a,zero) and pmul(P,43,a) is None
    assert scalar(P[0]) and scalar(P[1])
    assert on(P2,a,zero) and pmul(P2,2,a)==(zero,zero)
    assert beta_point(P2,a,ii)==P2
    assert on(T5,a,zero) and pmul(T5,5,a) is None and beta_point(T5,a,ii) is None
    assert -miller(P,ip(P,ii),43,a)/miller(ip(P,ii),P,43,a)==zeta
    assert zeta**43==1 and zeta!=1
    # Scalar layer: kill the anti-p direction <iP>, not the scalar direction.
    E=velu(a,zero,ip(P,ii),43); S=phi(E,P)
    assert S is not None and pmul(S,43,E['a']) is None
    back=velu(E['a'],E['b'],S,43)
    assert back['a']==-(43**4) and back['b']==0
    X=pc.gen(); den=pc.one()
    for u,t,w in back['ker']:
        den*=(X-scalar(u))**2
    num=X*den
    for u,t,w in back['ker']:
        d=X-scalar(u)
        num+=scalar(t)*(den//d)+scalar(w)*(den//(d*d))
    f=num-(43**2)*scalar(P[0])*den
    assert f.degree()==43 and f.is_monic() and f.gcd(f.derivative()).is_one()
    # f(W-i)=A(W)-i B(W), so W=x_Q+i and i=A(W)/B(W).
    A=pc.zero(); B=pc.zero()
    for coefficient in reversed(f.coeffs()):
        A,B=X*A-B+coefficient, A+X*B
    modulus=A*A+B*B
    assert modulus.degree()==86 and modulus.is_monic()
    assert modulus.gcd(modulus.derivative()).is_one()
    # We prove irreducibility below from the actual Frobenius translation.
    F=fq_default_ctx(modulus=modulus, check_prime=False, check_modulus=False)
    W=F.gen()
    ev=lambda poly:F([int(c) for c in poly.coeffs()])
    i=ev(A)/ev(B); x=W-i
    assert i*i==-1
    dval=F(0); nval=F(0); ndval=F(0); ddval=F(0)
    def evalx(poly):
        out=F(0)
        for c in reversed(poly.coeffs()): out=out*x+int(c)
        return out
    assert evalx(f)==0
    dval=evalx(den); nval=evalx(num)
    derivative=(evalx(num.derivative())*dval-nval*evalx(den.derivative()))/(dval*dval)
    Q=(x,F(43**3*scalar(P[1]))/derivative)
    emb=lambda z:F(int(z.to_list()[0]) if z.to_list() else 0)+(int(z.to_list()[1]) if len(z.to_list())>1 else 0)*i
    embp=lambda V:None if V is None else tuple(emb(z) for z in V)
    Ee={'a':emb(E['a']), 'b':emb(E['b']), 'ker':[(emb(u),emb(t),emb(w)) for u,t,w in E['ker']]}
    Se=embp(S)
    assert on(Q,Ee['a'],Ee['b']) and pmul(Q,43,Ee['a'])==Se
    assert phi({'a':emb(back['a']),'b':emb(back['b']),'ker':[(emb(u),emb(t),emb(w)) for u,t,w in back['ker']]},Q)==tuple(emb(z)*43**(2+j) for j,z in enumerate(P))
    # Over every residue-field factor, Q has exact order p^2 and Frobenius
    # translates it by 16S.  Its x-coordinate consequently has orbit 43;
    # adjoining i gives orbit 86.  The squarefree degree-86 algebra is a field.
    Qf=tuple(z.frobenius() for z in Q)
    assert Qf==padd(Q,pmul(Se,16,Ee['a']),Ee['a']), 'marked q Frobenius'
    assert i.frobenius()==-i
    F2p=fq_default_poly_ctx(F2)
    f2=F2p([F2(int(c)) for c in f.coeffs()])
    def normS(v):
        # Substitute W=X+i and reduce modulo f(X).  Then take the degree-43
        # resultant in Fq[i][X], avoiding repeated long finite-field powers.
        AA=pc.zero(); BB=pc.zero()
        for coefficient in reversed(v.to_list()):
            AA,BB=(X*AA-BB+int(coefficient))%f,(AA+X*BB)%f
        g=F2p([F2(int(AA[j]))+int(BB[j])*ii for j in range(43)])
        return resultant(f2,g,F2)
    assert normS(F(2))==F2(2)**43
    assert normS(i)==ii**43
    assert normS(x)==F2(-int(f[0]))
    initial={'P':P,'E':E,'S':S,'Q':Q}
    return locals()


def evaluate_row(state, D):
    P,E,S,Q=state['P'],state['E'],state['S'],state['Q']
    F,F2,emb,embp=D['F'],D['F2'],D['emb'],D['embp']
    ae,be=emb(E['a']),emb(E['b'])
    P2bar=embp(phi(E,D['P2']))
    assert on(Q,ae,be) and pmul(Q,43,ae)==embp(S)
    den=F(1)
    # mu_42 means the genuine Teichmuller lifts modulo p^2, k^43 mod 1849.
    lifts=[pow(k,43,1849) for k in range(1,43)]
    assert all(pow(k,42,1849)==1 for k in lifts) and len(set(lifts))==42
    for lift in lifts:
        R=padd(P2bar,pmul(Q,lift,ae),ae)
        v=psi11(R[0],ae,be)
        assert v!=0
        den*=v
    u=emb(discr(E['a'],E['b'])**420)/den
    base=F2(1); R=padd(D['P2'],P,D['a'])
    for k in range(1,43):
        base*=psi11(R[0],D['a'],D['zero'])
        R=padd(R,P,D['a'])
    assert R==D['P2']
    u0=F2(64)**420/base
    norm=D['normS'](u)
    assert norm==u0, ('exact scalar norm',state['index'])
    return u, {'index':state['index'], 'u_s':coords(u), 'base_u0':coords(u0), 'norm_S':coords(norm), 'norm_ratio':'1'}


def advance(state,D):
    P,E,S,Q=state['P'],state['E'],state['S'],state['Q']
    Pn=beta_point(P,D['a'],D['ii'])
    En=velu(D['a'],D['zero'],ip(Pn,D['ii']),43)
    Sn=phi(En,Pn)
    five=velu(E['a'],E['b'],phi(E,D['T5']),5)
    beta=D['F2'](-1)+2*D['ii']; b2=beta**2; b3=beta**3
    assert five['a']==(b2*b2)*En['a'] and five['b']==(b3*b3)*En['b']
    assert tuple(z/d for z,d in zip(phi(five,S),(b2,b3)))==Sn
    em=D['emb']; ep=D['embp']
    fe={'a':em(five['a']), 'b':em(five['b']), 'ker':[(em(u),em(t),em(w)) for u,t,w in five['ker']]}
    raw=phi(fe,Q)
    Qn=tuple(z/d for z,d in zip(raw,(em(b2),em(b3))))
    Qn=padd(Qn,pmul(ep(Sn),-22,em(En['a'])),em(En['a']))
    assert on(Qn,em(En['a']),em(En['b'])) and pmul(Qn,43,em(En['a']))==ep(Sn)
    return {'P':Pn,'E':En,'S':Sn,'Q':Qn,'index':state['index']+1}


def gaussian_mul(a,b,n):
    return ((a[0]*b[0]-a[1]*b[1])%n,(a[0]*b[1]+a[1]*b[0])%n)


def main():
    global INPUT, HERE
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=INPUT)
    parser.add_argument('--outdir', type=Path, default=HERE)
    parser.add_argument('--check', type=Path)
    parser.add_argument('--stop-after',type=int,default=44)
    parser.add_argument('--resume',action='store_true')
    args=parser.parse_args()
    INPUT=args.input
    HERE=args.outdir
    HERE.mkdir(parents=True, exist_ok=True)
    start=time.time()
    C=json.loads(INPUT.read_text()); D=setup(C)
    q=D['q']; F=D['F']; i=D['i']
    print(json.dumps({'stage':'setup PASS','seconds':round(time.time()-start,3),'field_degree':86,'Frobenius_translation':16,'source_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest()}),flush=True)
    result={'status':'IN_PROGRESS','input_file':INPUT.name,'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
      'q':str(q),'p':43,'f43':[str(int(z)) for z in D['f'].coeffs()],
      'f86':[str(int(z)) for z in D['modulus'].coeffs()], 'i_in_f86':coords(i),
      'Q_initial':[coords(v) for v in D['Q']], 'source_model':'W=x_Q+i; kernel <iP>; hat_phi(Q)=P',
      'q_Frobenius_translation':16,'S_generator_translation':1,'Kq_Frobenius_S_exponent':32,
      's_on_mu_p2':87,'CM_tame_correction_scalar':22,'rows':[],'actual_C_computed':False,'actual_L_computed':False}
    path=HERE/'r380_scalar_recovery_checkpoint.json'
    old=json.loads(path.read_text()) if args.resume and path.exists() else None
    if old:
        for key in ['input_sha256','f43','f86','i_in_f86','Q_initial']:
            assert result[key]==old[key], ('recovery mismatch',key)
    state={**D['initial'],'index':0}; WA=F(1); WB=F(1); wh=(1,0)
    for j in range(min(args.stop_after,44)):
        if old and j<len(old['rows']):
            row=old['rows'][j]; u=F([int(z) for z in row['u_s']])
            assert row['index']==j and row['norm_ratio']=='1'
        else:
            u,row=evaluate_row(state,D)
        WA*=u**wh[0]; WB*=u**wh[1]
        wh=gaussian_mul(wh,(352,197),1849)
        state=advance(state,D)
        result['rows'].append(row)
        result['next_index']=j+1
        result['Q_next']=[coords(z) for z in state['Q']]
        result['WA']=coords(WA); result['WB']=coords(WB)
        dump(path,result)
        print(json.dumps({'stage':'row PASS','row':j,'norm_ratio':'1','seconds':round(time.time()-start,3)}),flush=True)
    if args.stop_after<44:
        return
    initial=D['initial']
    assert state['P']==pmul(initial['P'],5,D['a'])
    assert state['S']==pmul(initial['S'],5,initial['E']['a'])
    assert state['Q']==pmul(initial['Q'],pow(5,43,1849),D['emb'](initial['E']['a']))
    assert state['E']['a']==initial['E']['a'] and state['E']['b']==initial['E']['b']
    assert wh==(1,0)
    print(json.dumps({'stage':'all 44 norms and exact closures PASS','seconds':round(time.time()-start,3)}),flush=True)
    # Direct high-order projection.  q^43 fixes x_Q and sends i to -i.
    # The exponent (q^86-1)/p^2 factors as (q^43-1)(q^43+1)/p^2.
    exponent=(q**43+1)//1849
    assert (q**43+1)%1849==0
    zeta=D['emb'](D['zeta'])
    logs=[]; powers=[]
    # Compute conjugation W->W-2i by Horner, rather than a q^43 exponent.
    Wconj=D['W']-2*i
    def conjugate(v):
        out=F(0)
        for c in reversed(v.to_list()): out=out*Wconj+int(c)
        return out
    assert conjugate(i)==-i and conjugate(D['x'])==D['x']
    for name,v in [('real_high_weight',WA),('imaginary_high_weight',WB)]:
        power=(conjugate(v)/v)**exponent
        cur=F(1); log=None
        for j in range(43):
            if cur==power:
                log=j; break
            cur*=zeta
        assert log is not None, 'high residue in original mu_43'
        logs.append(log); powers.append(coords(power))
        print(json.dumps({'stage':'high projection PASS','coordinate':name,'log':log,'seconds':round(time.time()-start,3)}),flush=True)
    result.update({'status':'PASS','all_44_norm_ratios':'1','psi11_evaluations':3696,
      'closure_Q_multiplier':pow(5,43,1849),'closure_PS_multiplier':5,'high_projection_logs':logs,
      'high_projection_powers':powers,'high_exponent':'(q^86-1)/43^2',
      'chi_minus_projector':'sum omegahat^j sigma^j; no /44',
      'all_norms_and_markings_verified':True,'seconds':round(time.time()-start,3)})
    if args.check:
        expected=json.loads(args.check.read_text())
        for key in result:
            if key not in {'seconds','input_file'}:
                assert result[key]==expected[key], ('certificate mismatch',key)
    dump(HERE/'r380_scalar_recovery_certificate.json',result)
    print(json.dumps({k:result[k] for k in ['status','all_44_norm_ratios','high_projection_logs','closure_Q_multiplier','seconds','actual_C_computed','actual_L_computed']}),flush=True)


if __name__=='__main__':
    main()
