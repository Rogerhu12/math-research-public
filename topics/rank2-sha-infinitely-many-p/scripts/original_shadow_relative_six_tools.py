#!/usr/bin/env sage-python
"""R880(C), R882, R883: the SAME original relative-six shadow consumer.

All arithmetic is run only in public research Actions.  Inputs are in-process
actual RR functions and the two SAME successful characteristic-zero map receipts.
No candidate local ODE solution is treated as a map.  No basis, divisor, or
recomputable point table is written to the repository or to a release.

The source is the normalization of degree 288 over k(t_eta), equivalently the
original relative degree-six Y=X_0(3468)->X_0(867).  All nine original pairs are retained via four full divisors and the proved
whole W and constant-reflection identities.  All cusps, common intersections, and residue degrees remain.
The optional divisor_method is global (default) or local; local retains the same
source through the complete original Kummer tower over the existing quotient.
The explicit trace_method is tate (default), scalar, or compare; compare runs
both exact readers at every contributing closed point in the SAME torsion basis.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Mathematical execution is restricted to the public research Actions.")

import hashlib
import json
import time
from pathlib import Path
from sage.all import (ZZ, GF, PolynomialRing, EllipticCurve, matrix, vector, identity_matrix)

STARTED = time.monotonic()
ORIGINAL_PAIRS = ((0,1),(1,2),(2,0))

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=True)

def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()

def progress(stage, **kw):
    print("RANK2_ORIGINAL_SHADOW_STAGE "+canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)

def ff_coordinates(x):
    return [int(c) for c in x.polynomial().list()]

def point_coordinates(P):
    if P.is_zero():
        return {"infinity":True}
    return {"x":ff_coordinates(P[0]),"y":ff_coordinates(P[1])}

def function_fingerprint(f):
    h=hashlib.sha256()
    for c in f.list():
        h.update(str(c.numerator()).encode())
        h.update(b"/")
        h.update(str(c.denominator()).encode())
        h.update(b";")
    return h.hexdigest()

def place_fingerprint(Q):
    if hasattr(Q,"fingerprint"):
        return Q.fingerprint()
    h=hashlib.sha256()
    h.update(str(int(Q.degree())).encode())
    h.update(b":")
    for f in Q.prime_ideal().gens():
        h.update(function_fingerprint(f).encode())
        h.update(b";")
    return h.hexdigest()

def constant_value(f, k):
    """Read a proven constant of k(t)[T]; do not choose a new residue embedding."""
    if f.parent() is k:
        return f
    coeffs=f.list()
    assert not any(coeffs[1:])
    a=coeffs[0] if coeffs else f.parent().base_field().zero()
    n,d=a.numerator(),a.denominator()
    assert n.degree()<=0 and d.degree()==0
    return k(n[0])/k(d[0])

def hecke2_level3():
    """Exact integer Faber/Newton construction for T_3, including its norm sign."""
    ell=2
    bound=ell*(ell+1)
    sigma=[ZZ(0)]*(bound+1)
    for d in range(1,bound+1):
        for n in range(d,bound+1,d):
            sigma[n]+=d
    ld=[ZZ(0)]+[-12*sigma[n]+(36*sigma[n//3] if n%3==0 else 0)
                    for n in range(1,bound+1)]
    eta=[ZZ(1)]
    for n in range(1,bound+1):
        num=sum((ld[j]*eta[n-j] for j in range(1,n+1)),ZZ(0))
        assert num%n==0
        eta.append(num//n)
    ZX=PolynomialRing(ZZ,"X_phi")
    X=ZX.gen()
    bc=[ZX(c) for c in eta]
    bc[1]-=X
    fab=[ZX.zero()]
    for n in range(1,bound+1):
        f=-n*bc[n]-sum((fab[j]*bc[n-j] for j in range(1,n)),ZX.zero())
        assert f.degree()==n and f.leading_coefficient()==1
        fab.append(f)
    Zq=PolynomialRing(ZZ,"q_phi")
    short=Zq(eta[:ell+2])
    powers=[ZX.zero()]
    for k in range(1,ell+2):
        ep=(short**k).truncate(k+1)
        f=ZX((ell+1)*ep[k])
        for n in range(-k,0):
            f+=ep[k+n]*fab[-ell*n]
            if n%ell==0:
                f+=ell*ep[k+n]*fab[-n//ell]
        powers.append(f)
    es=[ZX.one()]
    for n in range(1,ell+2):
        num=sum(((-1)**(j-1)*es[n-j]*powers[j]
                    for j in range(1,n+1)),ZX.zero())
        assert all(ZZ(c)%n==0 for c in num.list())
        es.append(ZX([ZZ(c)//n for c in num.list()]))
    terms={}
    for n,e in enumerate(es):
        for i,c in enumerate(e.list()):
            if c:
                terms[(i,ell+1-n)]=ZZ((-1)**n*c)
    assert terms[(0,3)]==terms[(3,0)]==1
    assert all(terms.get((j,i),0)==c for (i,j),c in terms.items())
    serial=[[i,j,str(terms[(i,j)])] for i,j in sorted(terms)]
    progress("exact level3 Phi2", nonzero_terms=len(terms), sha256=digest(serial))
    return terms

def evaluate_phi(terms,x,y,zero):
    maxx=max(i for i,j in terms)
    maxy=max(j for i,j in terms)
    xp=[x**i for i in range(maxx+1)]
    yp=[y**j for j in range(maxy+1)]
    return sum((c*xp[i]*yp[j] for (i,j),c in terms.items()),zero)

def phi_modulo(terms,x,modulus):
    """Reduce the full original Phi(x,Z) modulo a small actual Hecke polynomial."""
    R=modulus.parent()
    z=R.gen()
    maxx=max(i for i,j in terms)
    maxy=max(j for i,j in terms)
    xp=[x**i for i in range(maxx+1)]
    co=[R.base_ring().zero() for _ in range(maxy+1)]
    for (i,j),c in terms.items():
        co[j]+=c*xp[i]
    out=R.zero()
    for c in reversed(co):
        out=(out*z+c)%modulus
    return out

def unique_parallel_17(source_neighbor, central_middle, phi2, phi17, L, label):
    R=PolynomialRing(L,"Z_parallel")
    z=R.gen()
    m=evaluate_phi(phi2,central_middle,z,R.zero()).monic()
    assert m.degree()==3
    rem=phi_modulo(phi17,source_neighbor,m)
    common=m.gcd(rem).monic()
    assert common.degree()==1, "Keep the actual coprime-Hecke common endpoint."
    value=-common[0]
    assert m(value)==0 and rem(value)==0
    progress("actual parallel endpoint", label=label,
             root_sha256=function_fingerprint(value))
    return value

def cleared_eta_relation(B):
    """Return the actual selected eta48 relation, with no arbitrary twelfth root."""
    co=B.polynomial().list()
    kt=co[0].denominator().parent()
    den=kt.one()
    for a in co:
        den=den.lcm(a.denominator())
    cc=[a.numerator()*(den//a.denominator()) for a in co]
    return cc,den

def unique_endpoint_eta(Ti,Vi,cleared,den,L,label):
    R=PolynomialRing(L,"Z_eta_endpoint")
    z=R.gen()
    m=z**12-Ti/Vi
    rem=R.zero()
    for a in reversed(cleared):
        rem=(rem*Ti+R(a.list()))%m
    common=m.gcd(rem).monic()
    assert common.degree()==1, "The original eta endpoint is fixed by (T_i,V_i)."
    value=-common[0]
    assert den(value)!=0 and m(value)==0 and rem(value)==0
    progress("actual eta endpoint", label=label,
             root_sha256=function_fingerprint(value))
    return value

def build_relative_six_field(base,phi17):
    """base is the actual eta48 k(t)[T] context, optionally already over k=F_r^2."""
    B=base["field"]
    K=B.base_field()
    t=K.gen()
    assert B.degree()==48
    R=PolynomialRing(K,"y_source")
    y=R.gen()
    num=y**2*(y**2-9)**2
    den=(y**2-1)**2
    co=B.polynomial().list()
    degree=len(co)-1
    poly=R(co[-1])
    denpower=R.one()
    for a in reversed(co[:-1]):
        denpower*=den
        poly=poly*num+a*denpower
    poly=poly.monic()
    assert degree==48 and poly.degree()==288
    assert poly.gcd(poly.derivative()).degree()==0
    progress("relative six direct model", degree_over_eta=288,
             polynomial_sha256=digest([str(a) for a in poly.list()]))
    # Irreducibility is the original connected degree-six cover of R883.
    # This directly presents the same field; it is not an arbitrary factor.
    L=K.extension(poly,"y_source")
    ys=L.gen()
    vs=ys**2-1
    TL=ys**2*(ys**2-9)**2/vs**2
    tt=L(t)
    iB=B.hom([TL,tt])
    assert iB(base["T"])==TL
    UL,VL=iB(base["U"]),iB(base["V"])
    assert VL==TL/tt**12
    assert evaluate_phi(phi17,TL,UL,L.zero())==0
    assert evaluate_phi(phi17,UL,VL,L.zero())==0
    W=L.hom([(ys+3)/(ys-1),tt])
    assert W(W(ys))==ys and W(tt)==tt and W(TL)==TL
    assert W(UL)==UL and W(VL)==VL
    N0=5*vs+8-ys*(vs-8)
    T0=N0**3/vs**4-27
    T2=(vs-2)**3/vs-27
    assert W(T0)==T2 and W(T2)==T0
    phi2=hecke2_level3()
    assert evaluate_phi(phi2,TL,T0,L.zero())==0
    assert evaluate_phi(phi2,TL,T2,L.zero())==0
    U0=unique_parallel_17(T0,UL,phi2,phi17,L,"q0/U")
    V0=unique_parallel_17(U0,VL,phi2,phi17,L,"q0/V")
    cleared,common_den=cleared_eta_relation(B)
    t0=unique_endpoint_eta(T0,V0,cleared,common_den,L,"q0/eta")
    U2,V2,t2=W(U0),W(V0),W(t0)
    assert t0**12==T0/V0 and t2**12==T2/V2
    q0=B.hom([T0,t0])
    # The q2 map is an actual deck transport, not a separately chosen root.
    def q2(f):
        return W(q0(f))
    assert q0(base["U"])==U0 and q0(base["V"])==V0
    assert q2(base["T"])==T2 and q2(base["U"])==U2 and q2(base["V"])==V2
    progress("relative six original endpoints complete",
             original_source_level=10404, quotient_level=3468,
             base_level=867, relative_degree=6,
             W_source_x_multiplier="2/(y_source-1)")
    return dict(field=L,eta=tt,ys=ys,vs=vs,T=TL,U=UL,V=VL,N0=N0,
                inject_base=iB,W=W,q0=q0,q2=q2,T0=T0,T2=T2,U0=U0,U2=U2,
                V0=V0,V2=V2,t0=t0,t2=t2,phi2_terms=phi2)

def fixed_artin_constants(maps):
    k=maps["constants"]
    r=int(maps["prime"])
    omega=maps["omega"]
    assert omega**2+omega+1==0
    roots=maps["original_a_roots"]
    perm=maps["sigma_a_index"]
    assert perm==[2,0,1] or tuple(perm)==(2,0,1)
    assert all(roots[perm[i]]==omega**2*roots[i] for i in range(3))
    assert roots[0]**r==roots[0]
    a0=roots[0]
    R=PolynomialRing(k,"theta17")
    theta_roots=(R.gen()**2-a0).roots(multiplicities=False)
    assert len(theta_roots)==2
    theta=sorted(theta_roots,key=lambda z:tuple(ff_coordinates(z)))[0]
    assert theta**6==k(17)
    assert theta**r==-theta
    alpha=-1+2*omega
    def ell(v):
        return ((21905009-23122022*omega)
                +(112353990182+54575060764*omega)*v
                +(305813+148546*omega)*v**2)/k(25505280)
    embeddings=[0,perm[0],perm[perm[0]]]
    assert len(set(embeddings))==3
    v0=k(maps["P"][0]["v"])
    target=k(2)**32*v0
    assert target**r==target
    h0=target**pow(3,-1,r-1)
    assert h0**3==target and h0**r==h0
    hh=[h0]
    for j in range(2):
        vv=k(maps["P"][embeddings[j]]["v"])
        hh.append(alpha*hh[-1]/ell(vv))
    last_v=k(maps["P"][embeddings[2]]["v"])
    assert alpha*hh[2]/ell(last_v)==omega*h0
    rows=[]
    for j,i in enumerate(embeddings):
        pc=maps["P"][i]
        vv=k(pc["v"])
        lam=k(pc["lambda"])
        vnew=constant_value(pc["vnew"],k)
        assert hh[j]**3==k(2)**32*vv
        dnew=lam*hh[j]/k(2048)
        assert 2*dnew**3==vnew and dnew!=0
        rows.append(dict(artin_index=j,embedding=i,h=hh[j],dnew=dnew,
                         vnew=vnew,a17=k(pc["a17"]),scale=lam))
    progress("actual Artin constants fixed",
             geometric_prime=r,
             sigma_a_index=[int(i) for i in perm],
             ordered_packet_embeddings=embeddings,
             theta17=ff_coordinates(theta),
             h0=ff_coordinates(h0),
             constant_rows_sha256=digest([
                 {z:(int(v) if isinstance(v,int) else ff_coordinates(v))
                  for z,v in row.items()} for row in rows]))
    return dict(theta17=theta,rows=rows,omega=omega)

def build_actual_maps_on_six(rr,maps):
    """Only actual certified reductions reach this point."""
    from original_shadow_coordinate_tools import certificate_weight
    certificate_weight(maps["first_certificate"],"F")
    certificate_weight(maps["packet_certificate"],"P")
    assert rr["prime"]==maps["prime"] and rr["model"]=="eta48"
    six=build_relative_six_field(maps,rr["phi17_terms"])
    L=six["field"]
    ys,vs,N0=six["ys"],six["vs"],six["N0"]
    const=fixed_artin_constants(maps)
    theta=const["theta17"]
    iB=six["inject_base"]
    vF=iB(maps["F"]["v"])
    RF=iB(maps["F"]["R"])
    epsilon=-six["T"]*ys*(vs-8)*vs**3/(vs+4)**6
    # R883(24): the factor (v_s+4)/v_s is essential.
    f0=(vs+4)/vs*RF/theta**2
    yF=vF/(epsilon*theta**3)
    assert yF**2==vs*f0**3+1
    W=six["W"]
    assert (2/(ys-1))*W(f0)==f0
    assert W(yF)==-yF
    rows=[]
    for constrow in const["rows"]:
        i=constrow["embedding"]
        pc=maps["P"][i]
        Y0=six["q0"](pc["Y"])
        RP0=six["q0"](pc["R"])
        Y2,RP2=W(Y0),W(RP0)
        dnew=L(constrow["dnew"])
        vnew=L(constrow["vnew"])
        x0=N0**2/vs**3*RP0/dnew**2
        x2=(vs-2)**2/vs*RP2/dnew**2
        y0=2*Y0/vnew+1
        y2=2*Y2/vnew+1
        assert y0**2==vs*x0**3+1
        assert y2**2==vs*x2**3+1
        assert W(y0)==y2
        assert (2/(ys-1))*W(x0)==x2
        rows.append(dict(x0=x0,y0=y0,x2=x2,y2=y2))
        progress("actual pair coordinates on six", artin_index=constrow["artin_index"],
                 q0_y_sha256=function_fingerprint(y0),
                 q2_y_sha256=function_fingerprint(y2))
    # R883(D): this is constant conjugation, not absolute Frobenius pullback.
    k=maps["constants"]
    r=int(maps["prime"])
    constant_frob=k.hom([k.gen()**r])
    conjugate=L.hom([ys,L(L.base_field().gen())],base_morphism=constant_frob)
    assert conjugate(ys)==ys and conjugate(six["eta"])==six["eta"]
    assert conjugate(f0)==f0 and conjugate(yF)==-yF
    for i in range(3):
        star=(-i)%3
        u=0 if i==0 else -1
        phase=maps["omega"]**u
        for tag in ("x0","x2"):
            assert conjugate(rows[i][tag])==phase*rows[star][tag]
        for tag in ("y0","y2"):
            assert conjugate(rows[i][tag])==rows[star][tag]
    progress("actual constant-reflection identities checked",
             F_sign=-1,reflection="c_infinity times epsilon",
             A_images=["A0","omega^2*A2","omega^2*A1"])
    six.update(prime=int(maps["prime"]),constants=maps["constants"],
               omega=maps["omega"],F_x_over_xs=f0,F_y=yF,
               A=rows,artin_constants=const,
               first_certificate=maps["first_certificate"],
               packet_certificate=maps["packet_certificate"])
    return six

def verified_torsion_basis(k,omega,r):
    ell=(r+1)//6
    assert (r,ell) in ((29,5),(41,7))
    E=EllipticCurve(k,[0,0,0,0,1])
    # Enumerate this fixed small field directly.  E.points() delegates to
    # PARI, where a legitimate coefficient-field name such as omega can
    # collide with a built-in symbol.  All geometric points are retained.
    points=[E(0)]
    for xx in k:
        rhs=xx**3+1
        if rhs==0:
            points.append(E([xx,k(0)]))
        elif rhs.is_square():
            yy=rhs.sqrt()
            points.extend((E([xx,yy]),E([xx,-yy])))
    assert len(set(points))==len(points)==(r+1)**2
    torsion={6*P for P in points}
    assert len(torsion)==ell**2
    def order_key(P):
        if P.is_zero():
            return (0,)
        return (1,tuple(ff_coordinates(P[0])),tuple(ff_coordinates(P[1])))
    ordered=sorted(torsion,key=order_key)
    P=next(P for P in ordered if not P.is_zero())
    cyclic={j*P for j in range(ell)}
    Q=next(Q for Q in ordered if Q not in cyclic)
    table={}
    for i in range(ell):
        for j in range(ell):
            R=i*P+j*Q
            assert R not in table
            table[R]=(i,j)
    assert set(table)==torsion
    def cm(R):
        return E(0) if R.is_zero() else E([omega*R[0],R[1]])
    col0,col1=table[cm(P)],table[cm(Q)]
    M=matrix(GF(ell),[[col0[0],col1[0]],[col0[1],col1[1]]])
    assert M**2+M+identity_matrix(GF(ell),2)==0
    def frobenius(R):
        return E(0) if R.is_zero() else E([R[0]**r,R[1]**r])
    fcol0,fcol1=table[frobenius(P)],table[frobenius(Q)]
    C=matrix(GF(ell),[[fcol0[0],fcol1[0]],[fcol0[1],fcol1[1]]])
    assert C**2==(-r)*identity_matrix(GF(ell),2)
    assert C*M==M**2*C
    assert C.trace()==0 and C.det()==GF(ell)(r)
    progress("verified target torsion basis", ell=ell,
             E_order=len(points), first=point_coordinates(P),second=point_coordinates(Q),
             actual_CM_matrix=[[int(z) for z in row] for row in M.rows()],
             actual_r_Frobenius_matrix=[[int(z) for z in row] for row in C.rows()])
    return dict(curve=E,ell=ell,basis=(P,Q),coordinates=table,CM_matrix=M,
                Frobenius_matrix=C,cm=cm,frobenius=frobenius)

def prime_vector(z,fp,dimension):
    v=[fp(c) for c in z.polynomial().list()]
    assert len(v)<=dimension
    return vector(fp,v+[fp.zero()]*(dimension-len(v)))

def read_fixed_field_point(S,kQ,omega_res,omega_k,k,Etgt,r,d):
    if S.is_zero():
        return Etgt(0)
    assert kQ.cardinality()==ZZ(r)**(2*d)
    assert S[0]**(r*r)==S[0] and S[1]**(r*r)==S[1]
    fp=GF(r)
    dim=2*d
    cols=[prime_vector(kQ.one(),fp,dim),prime_vector(omega_res,fp,dim)]
    A=matrix(fp,dim,2,lambda i,j:cols[j][i])
    piv=tuple(A.transpose().pivots())
    assert len(piv)==2
    inv=matrix(fp,[[A[i,j] for j in range(2)] for i in piv]).inverse()
    out=[]
    for z in (S[0],S[1]):
        vv=prime_vector(z,fp,dim)
        co=inv*vector(fp,[vv[i] for i in piv])
        assert A*co==vv
        out.append(k(co[0])+k(co[1])*omega_k)
    return Etgt(out)

def prepare_normalized_geometry(six,rr=None,divisor_method="global"):
    """Full original divisors: native normalization or the same-field local tower."""
    assert divisor_method in ("global","local")
    L=six["field"]
    engine=None
    if divisor_method=="local":
        assert rr is not None
        from original_shadow_local_divisor_tools import OriginalLocalDivisorEngine
        engine=OriginalLocalDivisorEngine(rr,six)
        divisor=engine.divisor
        poles=engine.poles
        progress("same original local divisor backend selected",
                 quotient=engine.kind,source_degree_over_eta=288)
    else:
        progress("relative six normalization finite start",degree_over_eta=288)
        L.maximal_order()
        progress("relative six normalization finite complete")
        L.maximal_order_infinite()
        progress("relative six normalization infinite complete")
        divisor=lambda f:f.divisor()
        poles=lambda f:f.divisor_of_poles()
    TD=divisor(six["T"])
    vD=divisor(six["vs"])
    cusps=set(TD.support())
    assert sum(int(Q.degree()) for Q in cusps)==108
    assert set(vD.support()).issubset(cusps)
    ram=[Q for Q in vD.support() if int(vD.multiplicity(Q))%3]
    assert all(TD.multiplicity(Q)<0 for Q in ram)
    assert sum(int(Q.degree()) for Q in ram)==54
    assert TD.degree()==vD.degree()==0
    progress("complete geometric boundary",quotient_cusps_degree=108,
             cubic_ramified_cusps_degree=54,known_quotient_genus=559,
             known_original_genus=1729,geometric_counts_not_rational_point_counts=True)
    divisors=[]
    for j,row in enumerate(six["A"]):
        dd={}
        for tag in ("x0","x2"):
            dd[tag]=divisor(row[tag])
        for tag in ("y0","y2"):
            dd[tag+"_poles"]=poles(row[tag])
            assert dd[tag+"_poles"].degree()==2256
        divisors.append(dd)
        progress("whole endpoint divisors cached",artin_index=j)
    fD=divisor(six["F_x_over_xs"])
    yFpoles=poles(six["F_y"])
    first_degree=int(yFpoles.degree())
    assert first_degree>0
    progress("actual first map degree from the already cached full divisor",
             first_map_degree=first_degree,
             chosen_cyclic_presentation=("A_bq2 output" if first_degree<2256 else "F output"))
    return dict(T_divisor=TD,vs_divisor=vD,cusps=cusps,
                endpoint_divisors=divisors,F_x_divisor=fD,F_y_poles=yFpoles,
                first_map_degree=first_degree,divisor_method=divisor_method,
                function_divisor=divisor,local_divisor_engine=engine)

def complete_pair_shadow(six,geometry,torsion,a,b,trace_method="tate",tate_reader=None):
    assert trace_method in ("tate","scalar","compare")
    assert (tate_reader is not None)==(trace_method in ("tate","compare"))
    L=six["field"]
    k=six["constants"]
    r=int(six["prime"])
    ell=torsion["ell"]
    E0=torsion["curve"]
    va=six["vs"]
    first_degree=geometry["first_map_degree"]
    # R883(F): choose between two integral, cyclically identical shadows.
    # dF is read from the true cached divisor, never supplied by a table.
    if first_degree<2256:
        presentation="A_bq2 output: (A_aq0 - Frobenius F)"
        xp=six["F_x_over_xs"]
        yp=six["F_y"]
        a0=six["A"][a]["x0"]
        y1=six["A"][a]["y0"]
        aD=geometry["endpoint_divisors"][a]["x0"]
        input_xD=geometry["F_x_divisor"]
        p1=geometry["endpoint_divisors"][a]["y0_poles"]
        p2=r*geometry["F_y_poles"]
        output_x=six["A"][b]["x2"]
        output_y=six["A"][b]["y2"]
        output_xD=geometry["endpoint_divisors"][b]["x2"]
        output_y_poles=geometry["endpoint_divisors"][b]["y2_poles"]
        expected=2256+r*first_degree
    else:
        presentation="F output: (A_bq2 - Frobenius A_aq0)"
        xp=six["A"][a]["x0"]
        yp=six["A"][a]["y0"]
        a0=six["A"][b]["x2"]
        y1=six["A"][b]["y2"]
        aD=geometry["endpoint_divisors"][b]["x2"]
        input_xD=geometry["endpoint_divisors"][a]["x0"]
        p1=geometry["endpoint_divisors"][b]["y2_poles"]
        p2=r*geometry["endpoint_divisors"][a]["y0_poles"]
        output_x=six["F_x_over_xs"]
        output_y=six["F_y"]
        output_xD=geometry["F_x_divisor"]
        output_y_poles=geometry["F_y_poles"]
        expected=2256*(r+1)
    c0=va**((r-2)//3)*xp**r
    y2=yp**r
    g=y1-y2
    assert g!=0
    progress("complete intersection divisor start",endpoint_pair=[a,b],
             cyclic_presentation=presentation,first_map_degree=first_degree,
             expected_degree=expected)
    gD=geometry["function_divisor"](g)
    E=gD+p1+p2
    assert E.is_effective() and E.degree()==expected
    cD=((r-2)//3)*geometry["vs_divisor"]+r*input_xD
    xout=a0*output_x/c0
    xoutD=aD+output_xD-cD
    total=E0(0)
    record_hash=hashlib.sha256()
    counts={"closed_places":0,"ramified_degree":0,"common_degree":0,
            "extra_degree":0,"extra_closed_places":0,"extra_output_infinity_degree":0,
            "nonzero_six_trace_places":0,"maximum_residue_degree":0,
            "cuspidal_intersection_degree":0}
    support=E.list()
    progress("complete intersection divisor factored",endpoint_pair=[a,b],
             closed_places=len(support),full_degree=int(E.degree()))
    for idx,(Q,ee) in enumerate(support):
        e=int(ee)
        d=int(Q.degree())
        assert e>0 and d>0
        counts["closed_places"]+=1
        counts["maximum_residue_degree"]=max(counts["maximum_residue_degree"],d)
        if Q in geometry["cusps"]:
            counts["cuspidal_intersection_degree"]+=e*d
        vv=int(geometry["vs_divisor"].multiplicity(Q))
        rec={"place_sha256":place_fingerprint(Q),"residue_degree":d,
             "intersection_multiplicity":e,"vs_valuation":vv}
        if vv%3:
            counts["ramified_degree"]+=e*d
            rec["boundary"]="ramified: exact 3-torsion, killed by 6"
        else:
            s=vv//3
            ax=s+int(aD.multiplicity(Q))
            cx=2*s+int(cD.multiplicity(Q))
            py1=int(p1.multiplicity(Q))
            py2=int(p2.multiplicity(Q))
            assert (py1>0)==(py2>0), "A single pole cannot lie in the full effective intersection."
            if py1 and py2:
                assert py1%3==0 and py2%3==0
                common=min(py1//3,py2//3)
            elif ax>0 and cx>0:
                common=min(ax,cx)
            else:
                common=0
            extra=e-3*common
            assert extra>=0
            counts["common_degree"]+=3*common*d
            counts["extra_degree"]+=extra*d
            rec.update(xA_valuation=ax,xB_valuation=cx,common_multiplicity=common,
                       extra_multiplicity=extra)
            if extra:
                assert ax==cx
                counts["extra_closed_places"]+=1
                if output_y_poles.multiplicity(Q)>0:
                    counts["extra_output_infinity_degree"]+=extra*d
                    rec["output"]="O by the actual projective extension"
                else:
                    assert xoutD.multiplicity(Q)>=0
                    kQ,from_kQ,to_kQ=Q.residue_field()
                    assert kQ.cardinality()==ZZ(r)**(2*d)
                    xx=to_kQ(xout)
                    yy=to_kQ(output_y)
                    assert yy**2==xx**3+1
                    EQ=EllipticCurve(kQ,[0,0,0,0,1])
                    P=EQ([xx,yy])
                    # R883(A,G): both methods read the SAME complete [6]trace.
                    # The actual residue embedding is fixed before any pairing.
                    embed_base=lambda c:to_kQ(L(c))
                    omega_res=embed_base(six["omega"])
                    assert omega_res**2+omega_res+1==0
                    trace_audit={"trace_method":trace_method}
                    Tate_point=None
                    scalar_point=None
                    if trace_method in ("tate","compare"):
                        Tate_point,pairing_audit=tate_reader.six_trace(
                            P,kQ,embed_base,d)
                        trace_audit["reduced_Tate"]=pairing_audit
                    if trace_method in ("scalar","compare"):
                        # Full d is retained here, never d modulo ell.
                        numerator=ZZ(1)-ZZ(-r)**d
                        assert numerator%ell==0
                        scalar=numerator//ell
                        S=scalar*P
                        assert ell*S==EQ(0)
                        scalar_point=read_fixed_field_point(
                            S,kQ,omega_res,six["omega"],k,E0,r,d)
                        trace_audit["scalar_bits"]=int(abs(scalar).nbits())
                    if trace_method=="compare":
                        assert Tate_point==scalar_point
                        trace_audit["same_basis_full_point_comparison"]=True
                    Sbase=scalar_point if trace_method=="scalar" else Tate_point
                    assert ell*Sbase==E0(0)
                    if not Sbase.is_zero():
                        counts["nonzero_six_trace_places"]+=1
                    # Only now is this an ell-torsion point; the full original
                    # intersection multiplicity extra remains in the record.
                    total+=extra*Sbase
                    rec.update(trace_audit=trace_audit,
                               six_trace=point_coordinates(Sbase),
                               weighted_trace=point_coordinates(extra*Sbase))
            else:
                rec["boundary"]="three equal lift contributions sum to zero"
        record_hash.update(canonical(rec).encode())
        record_hash.update(b"\n")
        if idx%20==19 or idx+1==len(support):
            progress("complete closed-point trace",endpoint_pair=[a,b],
                     processed=idx+1,total_places=len(support),
                     residue_degree_max=counts["maximum_residue_degree"])
    assert counts["ramified_degree"]+counts["common_degree"]+counts["extra_degree"]==expected
    assert ell*total==E0(0)
    coord=torsion["coordinates"][total]
    out=dict(endpoint_pair=[a,b],trace_method=trace_method,
             full_intersection_degree=expected,
             first_map_degree=first_degree,cyclic_presentation=presentation,
             six_times_trace=point_coordinates(total),torsion_coordinates=list(coord),
             complete_closed_records_sha256=record_hash.hexdigest(),**counts)
    progress("original pair complete",**out)
    return total,out

def read_full_artin(six,torsion,points):
    """Use all 18x9 rows, and independently check the already proved 9-term formula."""
    from original_shadow_coefficient_tools import original_two_axis_shadow_readout
    r=six["prime"]
    ell=torsion["ell"]
    degree=6 if ell==5 else 3
    coeff=GF(ZZ(ell)**degree,"zeta_coefficient")
    zeta=coeff.multiplicative_generator()**((coeff.cardinality()-1)//9)
    assert zeta**9==1 and zeta**3!=1
    omega=zeta**6
    zetas=[omega**j*zeta for j in range(3)]
    M=torsion["CM_matrix"]
    raw=[[vector(GF(ell),torsion["coordinates"][points[a][b]])
          for b in range(3)] for a in range(3)]
    labels=[]
    full=[]
    characters={pair:[] for pair in ORIGINAL_PAIRS}
    for l in range(9):
        for e in range(2):
            labels.append("sigma^%s*epsilon^%s"%(l,e))
            rows=[]
            for a in range(3):
                row=[]
                u,ap=divmod(a+l,3)
                for b in range(3):
                    v,bp=divmod(b+l,3)
                    value=(-1)**e*(M**((l-2*u+v)%3))*raw[ap][bp]
                    row.append([int(z) for z in value])
                rows.append(row)
            full.append(rows)
            for j,k in ORIGINAL_PAIRS:
                chars=characters[(j,k)]
                chi_sigma=omega/(zetas[j]*zetas[k])
                chars.append(chi_sigma**l*(-1)**e)
    assert [omega/(zetas[j]*zetas[k]) for j,k in ORIGINAL_PAIRS]==[zeta**7,zeta**4,zeta]
    result=original_two_axis_shadow_readout(
        prime=r,ell=ell,coefficient_field=coeff,zeta9=zeta,
        cm_matrix_omega=[[int(z) for z in row] for row in M.rows()],
        artin_labels=labels,complete_trace_vectors=full,
        character_values_by_pair=characters,
        first_certificate=six["first_certificate"],
        packet_certificate=six["packet_certificate"])
    Mc=M.change_ring(coeff)
    I=identity_matrix(coeff,2)
    eomega=(Mc-omega**2*I)/(omega-omega**2)
    check={}
    for j,k in ORIGINAL_PAIRS:
        v=vector(coeff,2)
        for a in range(3):
            for b in range(3):
                v+=zetas[j]**a*zetas[k]**b*vector(coeff,raw[a][b])/coeff(9)
        v=eomega*v
        assert tuple(v)==result["readouts"][(j,k)]
        check["%s,%s"%(j,k)]=[ff_coordinates(z) for z in v]
    return {
        "character_field_size":str(coeff.cardinality()),
        "zeta9":ff_coordinates(zeta),"omega_coefficient":ff_coordinates(omega),
        "artin_rows_sha256":digest(full),
        "original_pair_labels":["g10,g16","g16,g4","g4,g10"],
        "full_18_by_9_equals_native_9_term_formula":True,
        "cm_sign_projected_before_scalar_CM_substitution":True,
        "readouts":check,
        "nonzero_original_pairs":[list(p) for p in result["nonzero_original_pairs"]],
        "point_multiplier":6,
        "certificate_sources":result["certificate_sources"],
    }

def consume_original_relative_six(rr,maps,trace_method="tate",divisor_method="global"):
    """Main consumer; both divisor backends and all trace modes retain the same source."""
    assert divisor_method in ("global","local")
    assert trace_method in ("tate","scalar","compare")
    six=build_actual_maps_on_six(rr,maps)
    torsion=verified_torsion_basis(six["constants"],six["omega"],six["prime"])
    tate_reader=None
    if trace_method in ("tate","compare"):
        from original_shadow_tate_trace_tools import OriginalTateTraceReader
        tate_reader=OriginalTateTraceReader(torsion,six["prime"])
        progress("actual reduced Tate trace calibration",
                 trace_method=trace_method,**tate_reader.calibration)
    else:
        progress("original complete scalar trace selected",trace_method=trace_method)
    geometry=prepare_normalized_geometry(six,rr,divisor_method)
    points=[[None]*3 for _ in range(3)]
    summaries=[]
    # R883(C,D): whole [6] traces are symmetric, and the actual constant
    # reflection determines the other two unordered pairs.  No local trace
    # degree is reduced here: every computed point already is the full trace.
    computed_pairs=((0,0),(0,1),(1,1),(1,2))
    for a,b in computed_pairs:
        P,summary=complete_pair_shadow(
            six,geometry,torsion,a,b,trace_method,tate_reader)
        points[a][b]=points[b][a]=P
        summaries.append(summary)
    cm=torsion["cm"]
    frob=torsion["frobenius"]
    points[0][2]=points[2][0]=-cm(frob(points[0][1]))
    points[2][2]=-cm(cm(frob(points[1][1])))
    assert frob(points[0][0])==-points[0][0]
    assert frob(points[1][2])==-cm(points[1][2])
    assert all(torsion["ell"]*P==torsion["curve"](0)
               for row in points for P in row)
    readout=read_full_artin(six,torsion,points)
    # R883(E): an exact point test, independently checked against all original
    # character readouts.  This uses only complete geometric ell-torsion points.
    Atest=points[0][0]-cm(cm(points[1][2]))
    Ctest=points[1][1]+cm(frob(points[0][1]))
    assert frob(Atest)==-Atest
    detector=not Atest.is_zero() or not Ctest.is_zero()
    assert bool(readout["nonzero_original_pairs"])==detector
    assert len(readout["nonzero_original_pairs"]) in (0,3)
    point_test={"A":point_coordinates(Atest),"C":point_coordinates(Ctest),
                "A_coordinates":list(torsion["coordinates"][Atest]),
                "C_coordinates":list(torsion["coordinates"][Ctest]),
                "equivalent_to_all_three_original_nonzero_readouts":True,
                "detected_nonzero":detector}
    result={
        "kind":"rank2_same_original_relative_six_frobenius_shadow",
        "status":"complete_original_shadow",
        "prime":six["prime"],"ell":torsion["ell"],
        "trace_method":trace_method,
        "divisor_method":divisor_method,
        "RR_method":rr.get("rr_method",rr["model"]),
        "Tate_trace_reader":tate_reader.summary() if tate_reader is not None else None,
        "every_contributing_point_compared_in_same_basis":trace_method=="compare",
        "original_source_level":10404,"relative_six_level":3468,"RR_base_level":867,
        "source_genus":1729,"relative_six_genus":559,
        "degree_over_eta":288,"computed_complete_divisors":[list(p) for p in computed_pairs],
        "all_nine_original_pairs_accounted":True,
        "remaining_pairs_via_proved_W_and_constant_reflection":True,
        "actual_r_Frobenius_matrix":[[int(z) for z in row]
                                    for row in torsion["Frobenius_matrix"].rows()],
        "two_exact_point_detector":point_test,
        "all_cusps_and_residue_degrees_retained":True,
        "first_factor_x_correction":"(v_s+4)/v_s",
        "pair_summaries":summaries,
        "original_artin_readout":readout,
        "original_rational_AJ_detected_nonzero":bool(readout["nonzero_original_pairs"]),
        "canonical_cycle_substituted":False,
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    print("RANK2_ORIGINAL_SHADOW_RESULT "+canonical(result),flush=True)
    print("RANK2_ORIGINAL_SHADOW_SHA256 "+digest(result),flush=True)
    return result
