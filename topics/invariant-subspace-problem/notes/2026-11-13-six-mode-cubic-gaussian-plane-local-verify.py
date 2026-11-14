"""Exact local upper bound and cube obstruction at the positive isotropic plane.

Only the standard library and the already published original R3 matrix formula
are used. All jets use rational arithmetic; finite-field nonzero determinants
are used solely to certify nonzero rational determinants/resultants.
"""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import itertools
import json
import math

path=Path(__file__).with_name('2026-11-13-six-mode-cubic-local-jacobian-cube-verify.py')
spec=importlib.util.spec_from_file_location('original_cubic_exact',path)
alg=importlib.util.module_from_spec(spec)
spec.loader.exec_module(alg)


def transpose(A): return [list(row) for row in zip(*A)]
def mm(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def conv(a,b):
    return [sum(a[i]*b[k-i] for i in range(max(0,k-len(b)+1),min(len(a),k+1)))
            for k in range(len(a)+len(b)-1)]


def tail(head):
    h=list(map(Q,head))
    for j in range(3,11): h.append(5*h[j-1]-Q(32,5)*h[j-2]+Q(8,5)*h[j-3])
    return h


def bareiss(M):
    A=[list(row) for row in M];last=1;sign=1;n=len(A)
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:A[pivot],A[k]=A[k],A[pivot];sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=p*A[i][j]-A[i][k]*A[k][j]
                assert v%last==0
                A[i][j]=v//last
            A[i][k]=0
        last=p
    return sign*A[-1][-1]


def mod(x,p=103):
    x=Q(x)
    assert x.denominator%p
    return x.numerator%p*pow(x.denominator%p,-1,p)%p


def solve_mod(A,b=None,p=103):
    n=len(A);A=[[x%p for x in row]+([b[i]%p] if b is not None else []) for i,row in enumerate(A)]
    det=1
    for k in range(n):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None:return 0,None
        if pivot!=k:A[pivot],A[k]=A[k],A[pivot];det=-det
        v=A[k][k];det=det*v%p;iv=pow(v,-1,p)
        A[k]=[x*iv%p for x in A[k]]
        for i in range(n):
            if i==k:continue
            v=A[i][k];A[i]=[(x-v*y)%p for x,y in zip(A[i],A[k])]
    return det%p,([row[-1] for row in A] if b is not None else None)


def sylvester_residue(f,g):
    M=[]
    for row in [f,g]:
        for shift in range(3):M.append([0]*shift+list(row)+[0]*(2-shift))
    return solve_mod(M)[0]


def uniform_y_hessian():
    K=[[Q(x) for x in row] for row in alg.K]
    Hb=[];E=[]
    for j in range(3):
        h=tail([int(i==j) for i in range(3)])
        H=[[h[i+k] for k in range(6)] for i in range(6)];Hb.append(H)
        KHk=mm(mm(K,H),K)
        q=[sum(KHk[i][k] for i in range(6) for k in range(6) if i+k==m) for m in range(11)]
        E.append(transpose([conv(q,[K[i][k] for i in range(6)]) for k in range(6)]))
    pairs=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    coeff=[]
    for i,j in pairs:
        U=mm(mm(Hb[i],K),Hb[j])
        if i==j:assert all(not x for row in U for x in row)
        else:assert all(U[a][b]+U[b][a]==0 for a in range(6) for b in range(6))
        C=mm(transpose(E[i]),mm(alg.Ji,E[j]))
        if i==j:C=[[-36*x for x in row] for row in C]
        else:C=[[-36*(C[a][b]+C[b][a]) for b in range(6)] for a in range(6)]
        coeff.append(C)
    den=math.lcm(*(x.denominator for C in coeff for row in C for x in row))
    integer=[[[int(x*den) for x in row] for row in C] for C in coeff]
    specs=[([0,1,2,3,4],[0,1,2,3,4]),
           ([0,1,2,3,4],[0,1,2,3,5]),
           ([0,1,2,3,5],[0,1,2,3,5])]
    count=0
    # Each of these three determinants is homogeneous of degree 10 in h0,h1,h2.
    # On h0=1 it has total degree <=10; the triangular grid is unisolvent.
    for u in range(11):
        for v in range(11-u):
            mons=[1,u,v,u*u,u*v,v*v]
            M=[[sum(t*C[i][j] for t,C in zip(mons,integer)) for j in range(6)] for i in range(6)]
            for rows,cols in specs:
                assert bareiss([[M[i][j] for j in cols] for i in rows])==0
                count+=1
    assert count==198
    return coeff[0],count


def candidate_linear_nonzero(vy,ie,hh):
    p=103;f=[52565262336,6080833024,-43931504,3725]
    f=[x*pow(f[-1]%p,-1,p)%p for x in f]
    assert f==[35,5,76,1]
    def add(a,b):return [(x+y)%p for x,y in zip(a,b)]
    def scale(a,c):return [x*c%p for x in a]
    def mul(a,b):
        c=[0]*5
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
        for i in [4,3]:
            for j in range(3):c[i-3+j]=(c[i-3+j]-c[i]*f[j])%p
        return c[:3]
    def matrix(a):return transpose([mul(a,[int(i==j) for i in range(3)]) for j in range(3)])
    den=scale([(-704)%p,5,0],160)
    den_norm,inverse=solve_mod(matrix(den),[1,0,0]);assert den_norm==37
    A=mul(scale([271360%p,(-46784)%p,521%p],-1),inverse)
    B=add(A,[0,1,0])
    assert A==[35,4,59] and B==[35,5,59]
    r=[A,B,[0]*3,[0]*3,[0]*3,[1,0,0]]
    one=[0]*3;second=[0]*3
    for i in range(6):one=add(one,scale(r[i],mod(vy[i])))
    for i in range(6):
        for j in range(6):second=add(second,scale(mul(r[i],r[j]),mod(hh[i+j])))
    value=scale(mul(one,second),-6)
    for i,j,k in itertools.product(range(6),repeat=3):
        value=add(value,scale(mul(mul(r[i],r[j]),r[k]),-mod(ie[i+j+k])))
    assert value==[40,94,2]
    norm,_=solve_mod(matrix(value));assert norm==57
    return dict(monic_cubic_mod103=f,candidate_linear_coefficient_mod103=value,
                candidate_denominator_norm_mod103=den_norm,
                candidate_linear_norm_mod103=norm)


def verify():
    hyy,count=uniform_y_hessian()
    hh=tail([1,0,0]);base=[Q(0)]*6+hh
    alg.CUTOFF=1;Hess=[[Q(0) for _ in range(17)] for _ in range(17)]
    for j in range(17):
        x=[alg.P(t) for t in base];x[j]=x[j]+alg.P({(0,1):Q(1)})
        R,g,_=alg.formula(x)
        assert not R.d.get((0,0),0)
        for i in range(17):
            assert not g[i].d.get((0,0),0)
            Hess[i][j]=g[i].d.get((0,1),Q(0))
    assert Hess==transpose(Hess)
    assert [row[:6] for row in Hess[:6]]==hyy
    solved=[0,1,2,3,9,10,11,12,13,14,15,16]
    M=[[Hess[i][j] for j in solved] for i in solved]
    det,_=alg.eliminate(M);assert mod(det)==81
    directions=[(1,0),(0,1),(1,1),(1,-1),(1,2)]
    values=[];records=[];first_data=None
    for u,v in directions:
        alg.CUTOFF=3;x=[alg.P(t) for t in base]
        x[4]=alg.P({(0,1):Q(u)});x[5]=alg.P({(0,1):Q(v)})
        for order in [1,2,3]:
            _,g,_=alg.formula(x)
            rhs=[-g[i].d.get((0,order),Q(0)) for i in solved]
            d,solution=alg.eliminate(M,rhs);assert d==det
            for i,c in zip(solved,solution):x[i]=x[i]+alg.P({(0,order):c})
        _,g,ell=alg.formula(x)
        assert all(not g[i].d.get((0,j),0) for i in range(17) for j in range(3))
        # These include ALL twelve eliminated gradients and ALL three graph-parameter gradients.
        assert all(not g[i].d.get((0,3),0) for i in solved+[6,7,8])
        normal=[g[i].d.get((0,3),Q(0)) for i in [4,5]]
        if (u,v)==(1,0):
            vy=[x[i].d.get((0,1),Q(0)) for i in range(6)]
            el1=[t.d.get((0,1),Q(0)) for t in ell]
            ie=[sum(c*z for c,z in zip(row,el1)) for row in alg.Ji]
            first_data=(vy,ie)
        alg.CUTOFF=4;R,_=alg.formula(x,grad=False)
        assert all(not R.d.get((0,j),0) for j in range(4))
        values.append(R.d.get((0,4),Q(0)))
        records.append((u,v,normal))
    c0,c4,summ,diff,c12=values
    c2=(summ+diff)/2-c0-c4;mix=(summ-diff)/2
    c3=(c12-c0-16*c4-4*c2-2*mix)/6;c1=mix-c3
    coefficients=[c0,c1,c2,c3,c4]
    for u,v,normal in records:
        exact=[4*c0*u**3+3*c1*u*u*v+2*c2*u*v*v+c3*v**3,
               c1*u**3+2*c2*u*u*v+3*c3*u*v*v+4*c4*v**3]
        assert normal==exact
    denominator=math.lcm(*(c.denominator for c in coefficients))
    integer=[int(c*denominator) for c in coefficients]
    common=math.gcd(*integer);integer=[c//common for c in integer]
    primitive_mod=[c%103 for c in integer]
    assert primitive_mod==[90,27,54,83,62]
    q=primitive_mod
    gu=[4*q[0]%103,3*q[1]%103,2*q[2]%103,q[3]]
    gv=[q[1],2*q[2]%103,3*q[3]%103,4*q[4]%103]
    gradient_resultant=sylvester_residue(gu,gv);assert gradient_resultant==71
    # Exact left functionals are specified by solving their first two entries
    # against gu,gv. Their denominator is the nonzero first-two-row minor.
    minor=(gu[0]*gv[1]-gu[1]*gv[0])%103;assert minor==25
    pure=[]
    for j in [2,3]:
        _,a=solve_mod([[gu[0],gu[1]],[gv[0],gv[1]]],[(-gu[j])%103,(-gv[j])%103])
        row=[a[0],a[1],int(j==2),int(j==3)]
        pure.append([row[i]*[1,3,3,1][i]%103 for i in range(4)])
    assert pure==[[93,95,3,0],[0,16,0,1]]
    cube_resultant=sylvester_residue(*pure);assert cube_resultant==101
    candidate=candidate_linear_nonzero(*first_data,hh)
    return dict(all_pass=True,base_y=[0]*6,base_H=list(map(str,hh)),
                uniform_y_hessian_degree=2,schur_minor_degree_bound=10,
                exact_triangular_interpolation_nodes=66,exact_zero_five_minors=count,
                eliminated_variables_zero_based=solved,
                morse_block_determinant=str(det),morse_block_det_mod103=81,
                full_gradient_cubic_checks=17*4,
                eliminated_and_parameter_gradients_vanish_through_degree3=True,
                remaining_two_cubics_equal_quartic_gradient=True,
                transverse_quartic_primitive_integer_coefficients=list(map(str,integer)),
                transverse_quartic_scale=str(Q(common,denominator)),
                transverse_quartic_mod103=primitive_mod,
                quartic_gradient_sylvester_mod103=gradient_resultant,
                pure_cube_obstruction_coefficients_mod103=pure,
                pure_cube_resultant_mod103=cube_resultant,
                candidate=candidate,
                scope="Exact local data, including all seventeen gradients and the three-parameter Hessian identity. The accompanying local-algebra proof yields Br^5 membership for every r and Br^3 nonmembership for each of the three original first directions. No global cyclicity is claimed.")


if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
