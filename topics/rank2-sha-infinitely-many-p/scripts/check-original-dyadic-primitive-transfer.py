#!/usr/bin/env python3
"""R287 exact fixed-source certificate.

All theta source coefficients and original CM5 matrices are read from the
published R277/R283 certificates in this same directory.  The old odd CM5
matrix is independently recomputed by exact traces of five fixed degree-five
fibers.  Q0+ is evaluated with the actual eight Heisenberg translations over
Q(i,kappa,y), kappa^4=1/2.  No target primes or numerical reconstruction occur.
"""
import json
from pathlib import Path

def compute_v():
    import json, importlib.util
    from pathlib import Path
    import sympy as s
    from flint import fmpq, fmpq_mat

    root=Path(__file__).resolve().parent
    sp=importlib.util.spec_from_file_location('r248',root/'check-ray17-conjugate-trace-and-yang-projection.py')
    m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    U=m.U
    src=json.loads((root/'check-original-three-ordinary-adjoint.json').read_text())
    dat=json.loads((root/'check-original-first-order-i-block-and-cm5.json').read_text())

    def pair(z):
        z=s.expand(s.sympify(z)); return fmpq(str(s.re(z))),fmpq(str(s.im(z)))
    def gm(A):
        a,b=fmpq_mat(A.rows,A.cols),fmpq_mat(A.rows,A.cols)
        for j in range(A.cols):
            for i in range(A.rows): a[i,j],b[i,j]=pair(A[i,j])
        return a,b
    def cmul(A,B,C,D): return A*C-B*D,A*D+B*C
    def eye(n):return fmpq_mat(n,n,[int(i==j) for i in range(n) for j in range(n)])
    def realify(A,B):
        nr,nc=A.nrows(),A.ncols()
        return fmpq_mat(2*nr,2*nc,[
            A[i,j] if i<nr and j<nc else -B[i,j-nc] if i<nr else
            B[i-nr,j] if j<nc else A[i-nr,j-nc]
            for i in range(2*nr) for j in range(2*nc)])
    def serial(a,b):
        return [[str(a[i,j])+(' + '+str(b[i,j])+'*I' if b[i,j] else '')
                 for j in range(a.ncols())] for i in range(a.nrows())]

    def at(a):
        f=s.Poly(U,U,domain=m.dom)*m.Qp**4-(m.Kp**4).mul_ground(a)
        ub=(s.Poly(U,U,domain=m.dom)*m.Qb**4*m.inv(m.Kb**4,f)).rem(f)
        vb=m.inv(ub,f)
        factor=m.ipow((m.Qb*m.inv(m.Qp,f)).rem(f),16,f)
        factor=(factor*m.Pb*m.inv(m.Pp,f)*m.Kp**3*m.inv(m.Kb**3,f)).rem(f)
        ans=[]
        for j in range(1,5):
            term=(factor*m.ipow(vb,j,f)).rem(f)
            ans.append(s.expand((term*f.diff()).rem(f).nth(4)))
        return ans

    fibers=[at(a) for a in range(2,7)]
    evalmat=s.Matrix([[s.Rational(1,a**j) for j in range(1,5)] for a in range(2,6)])
    Mold=(evalmat.inv()*s.Matrix(fibers[:4])).applyfunc(s.expand)
    assert all(s.expand(sum(Mold[k,j]/s.Integer(6)**(k+1) for k in range(4))-fibers[4][j])==0 for j in range(4))
    S=(-s.I*Mold/(2+s.I)).applyfunc(s.expand_complex)
    Sr,Si=gm(S)
    S2r,S2i=cmul(Sr,Si,Sr,Si)
    S4r,S4i=cmul(S2r,S2i,S2r,S2i)
    assert S4r==fmpq_mat(4,4) and S4i==eye(4)

    Nr,Ni=fmpq_mat(17,17),fmpq_mat(17,17)
    for j,col in enumerate(dat['CM5_matrix_columns']):
        for i,c in enumerate(col):
            a,b=pair(c); Nr[i,j]=(2*a+b)/5; Ni[i,j]=(2*b-a)/5
    N2r,N2i=cmul(Nr,Ni,Nr,Ni)
    N4r,N4i=cmul(N2r,N2i,N2r,N2i)
    Ar,Ai=N4i,-N4r # -i*N_i^4.
    Q0r,Q0i=eye(17),fmpq_mat(17,17)
    Projr,Proji=eye(17),fmpq_mat(17,17)
    for j in range(1,4):
        Q0r,Q0i=cmul(Q0r,Q0i,Ar,Ai)
        Projr+=Q0r;Proji+=Q0i
    Projr/=4;Proji/=4
    assert realify(Projr,Proji).rank()==8
    z=json.loads((root/'check-original-three-ordinary-adjoint.json').read_text())
    zh=list(map(fmpq,z['angular_primitive_Z_H']))
    pr=fmpq_mat(17,1,[-zh[17-j]/4 for j in range(17)]);pi=fmpq_mat(17,1)
    pr,pi=cmul(Projr,Proji,pr,pi)

    dr=fmpq_mat(1,4);di=fmpq_mat(1,4,[fmpq(-13,32),fmpq(5,32),fmpq(3,32),fmpq(-11,32)])
    Obr,Obi=fmpq_mat(4,4),fmpq_mat(4,4)
    rhsr,rhsi=fmpq_mat(4,1),fmpq_mat(4,1)
    for k in range(4):
        for j in range(4): Obr[k,j],Obi[k,j]=dr[0,j],di[0,j]
        rhsr[k,0],rhsi[k,0]=pr[16,0],pi[16,0]
        dr,di=cmul(dr,di,Sr,Si)
        pr,pi=cmul(Nr,Ni,pr,pi)
    Ob=realify(Obr,Obi)
    assert Ob.det()!=0
    rhs=fmpq_mat(8,1,[rhsr[i,0] for i in range(4)]+[rhsi[i,0] for i in range(4)])
    sol=Ob.inv()*rhs
    cr=fmpq_mat(4,1,[sol[i,0] for i in range(4)])
    ci=fmpq_mat(4,1,[sol[i+4,0] for i in range(4)])

    R=[]
    for j in range(1,5):
        R.append(s.Poly(s.expand(s.Rational(16**j,8)*U**(j-1)*(U-1)**(2*j-2)*(U+1)**(18-4*j)*(U**2-6*U+1)),U))
    RM=fmpq_mat(17,4,[fmpq(str(r.nth(k))) for k in range(17) for r in R])
    kr,ki=RM*cr,RM*ci
    Lu=fmpq_mat(18,17)
    for j in range(17): Lu[j,j]=70-4*j;Lu[j+1,j]=4*j-68
    lr,li=Lu*kr,Lu*ki
    def source(cs):
        return s.Matrix([s.sympify(cs[17-j]) if 0<=17-j<len(cs) else 0 for j in range(18)])
    PA=source(src['source_coefficients_ascending']['A'])
    PB=source(src['source_coefficients_ascending']['B'])
    CB=s.Matrix(list(map(s.sympify,dat['theta_twice_beta_CM_polynomial'])))
    old=s.Matrix.hstack(PA,PB,CB,CB.conjugate())
    Oldr,Oldi=gm(old)
    er=-lr
    ei=fmpq_mat(18,1,[fmpq(8,11)*fmpq(str(PA[i]))-li[i,0] for i in range(18)])
    joinedr=fmpq_mat(18,5,[Oldr[i,j] if j<4 else er[i,0] for i in range(18) for j in range(5)])
    joinedi=fmpq_mat(18,5,[Oldi[i,j] if j<4 else ei[i,0] for i in range(18) for j in range(5)])
    assert realify(Oldr,Oldi).rank()==8
    delta_rank=realify(joinedr,joinedi).rank()//2

    ka=s.Matrix(list(map(s.sympify,dat['CM_corrected_A_primitive_polynomial'])))
    kb=s.Matrix(list(map(s.sympify,dat['CM_corrected_B_primitive_polynomial'])))
    cm=s.Matrix(list(map(s.sympify,dat['untwisted_odd_CM_polynomial'])))
    prim=s.Matrix.hstack(ka,kb,cm,cm.conjugate())
    Primr,Primi=gm(prim)
    pjr=fmpq_mat(17,5,[Primr[i,j] if j<4 else kr[i,0] for i in range(17) for j in range(5)])
    pji=fmpq_mat(17,5,[Primi[i,j] if j<4 else ki[i,0] for i in range(17) for j in range(5)])
    primitive_rank=realify(pjr,pji).rank()//2

    ans={'status':'PASS','old_odd_CM5_matrix':[[str(Mold[i,j]) for j in range(4)] for i in range(4)],
         'normalized_forward_source_S':serial(Sr,Si),
         'S_fourth_power':'+I','true_Piv_complex_rank':4,
         'forward_first_jet_polynomial_top_row':['-13*I/32','5*I/32','3*I/32','-11*I/32'],
         'first_jet_observability_determinant_norm':str(Ob.det()),
         'V_KH_old_coefficients_v1_v4':[serial(cr,ci)[j][0] for j in range(4)],
         'V_KH_native_odd_polynomial':[serial(kr,ki)[j][0] for j in range(17)],
         'complete_VL_minus_LV_native_even_polynomial':[serial(er,ei)[j][0] for j in range(18)],
         'A_B_CMtheta_plus_full_commutator_rank':delta_rank,
         'two_original_primitives_two_true_CM_plus_VKH_rank':primitive_rank}
    assert delta_rank==5 and primitive_rank==5
    return ans


def compute_q():
    import json
    from pathlib import Path
    from flint import fmpq, fmpq_mat
    import sympy as s

    ROOT=Path(__file__).resolve().parent
    dat=json.loads((ROOT/'check-original-first-order-i-block-and-cm5.json').read_text())
    Z=lambda:[fmpq(0) for _ in range(16)]
    def atom(a=0,b=0,c=0,n=1):
        v=Z();v[a+4*b+8*c]=fmpq(n);return v
    ONE=atom();II=atom(b=1);KAP=atom(a=1)
    def add(a,b):return [x+y for x,y in zip(a,b)]
    def sub(a,b):return [x-y for x,y in zip(a,b)]
    def scale(a,c):return [x*c for x in a]
    def pair(z):
        z=s.expand(s.sympify(z));return fmpq(str(s.re(z))),fmpq(str(s.im(z)))
    def gauss(z):
        a,b=pair(z);v=Z();v[0]=a;v[4]=b;return v
    TABLE=[]
    for i in range(16):
        ai,bi,ci=i%4,(i//4)%2,i//8
        row=[]
        for j in range(16):
            aj,bj,cj=j%4,(j//4)%2,j//8
            a,b,c=ai+aj,bi+bj,ci+cj
            row.append((a%4+4*(b%2)+8*(c%2),fmpq((-1)**(b//2),2**(a//4)),c//2))
        TABLE.append(row)
    YD=fmpq(0)
    def mul(a,b):
        z=Z();an=[(j,x) for j,x in enumerate(a) if x];bn=[(j,x) for j,x in enumerate(b) if x]
        for i,x in an:
            for j,y in bn:
                k,c,d=TABLE[i][j]
                z[k]+=x*y*c*(YD if d else 1)
        return z

    def mpow(a,n):
        r=ONE
        for _ in range(n):r=mul(r,a)
        return r

    def mid():return [[ONE if i==j else Z() for j in range(4)] for i in range(4)]
    def mmul(a,b):
        return [[sumv(mul(a[i][k],b[k][j]) for k in range(4)) for j in range(4)] for i in range(4)]
    def sumv(vs):
        z=Z()
        for v in vs:z=add(z,v)
        return z

    def matpow(a,n):
        r=mid()
        for _ in range(n):r=mmul(r,a)
        return r
    K3=atom(a=3)
    M=[[Z(),KAP,KAP,Z()], [K3,Z(),Z(),K3], [K3,Z(),Z(),scale(K3,-1)], [Z(),scale(KAP,-1),KAP,Z()]]
    N=[[Z(),KAP,scale(KAP,-1),Z()], [K3,Z(),Z(),scale(mul(II,K3),-1)], [scale(K3,-1),Z(),Z(),scale(mul(II,K3),-1)], [Z(),scale(mul(II,KAP),-1),scale(mul(II,KAP),-1),Z()]]
    assert matpow(M,4)==mid() and matpow(N,4)==mid()
    # The substitution for the operator M^k N^j is N^j M^k.
    terms=[(0,1,1),(0,3,1),(2,1,1),(2,3,1),(1,0,1),(3,0,1),(1,2,-1),(3,2,-1)]
    maps=[(mmul(matpow(N,j),matpow(M,k)),sgn) for k,j,sgn in terms]
    polys={nm:[gauss(c) for c in dat['CM_corrected_'+nm+'_primitive_polynomial']] for nm in ('A','B')}

    def eval_fiber(a):
        nonlocal YD
        YD=fmpq(a**3-a)
        coords=[atom(n=a*a+1),atom(n=a*a-1),atom(n=2*a),atom(c=1,n=2)]
        ans={nm:Z() for nm in polys}
        for mm,sgn in maps:
            co=[sumv(mul(c,x) for c,x in zip(row,coords)) for row in mm]
            ap=[ONE];bp=[ONE]
            ac,bc=add(co[0],co[1]),sub(co[0],co[1])
            for j in range(16):ap.append(mul(ap[-1],ac));bp.append(mul(bp[-1],bc))
            bas=[mul(co[3],mul(ap[j],bp[16-j])) for j in range(17)]
            for nm,ps in polys.items():
                val=sumv(mul(c,b) for c,b in zip(ps,bas))
                ans[nm]=add(ans[nm],scale(val,fmpq(-sgn,8*2**17)))
        for nm,ansv in ans.items():
            assert ansv[:8]==[fmpq(0)]*8,(nm,a,'even_y')
            ans[nm]=ansv[8:]
        return ans

    fibers=[]
    xs=[2,4,5,6,7]
    for a in xs:
        fibers.append(eval_fiber(a))
    U=s.symbols('U')
    RP=[s.Poly(s.expand(s.Rational(16**j,8)*U**(j-1)*(U-1)**(2*j-2)*(U+1)**(18-4*j)*(U**2-6*U+1)),U) for j in range(1,5)]
    RM=fmpq_mat(17,4,[fmpq(str(r.nth(k))) for k in range(17) for r in RP])
    ev=fmpq_mat(4,4,[fmpq(str(r.eval(a*a))) for a in xs[:4] for r in RP])
    assert ev.det()!=0
    inv=ev.inv()
    res={}
    qs={}
    for nm in polys:
        vals=fmpq_mat(4,8,[fibers[i][nm][k] for i in range(4) for k in range(8)])
        cs=inv*vals
        for k in range(8):
            assert sum(fmpq(str(RP[j].eval(xs[4]**2)))*cs[j,k] for j in range(4))==fibers[4][nm][k]
        # The exact common scalar is kappa^{-1}=2*kappa^3.
        assert all(cs[j,k]==0 for j in range(4) for k in (0,1,2,4,5,6))
        qr=fmpq_mat(4,1,[cs[j,3]/2 for j in range(4)])
        qi=fmpq_mat(4,1,[cs[j,7]/2 for j in range(4)])
        qs[nm]=(RM*qr,RM*qi)
        res[nm]={'kappa_times_Q0plus_old_coefficients': [str(qr[j,0])+(' + '+str(qi[j,0])+'*I' if qi[j,0] else '') for j in range(4)],
                 'kappa_times_Q0plus_native_polynomial':[str(qs[nm][0][j,0])+(' + '+str(qs[nm][1][j,0])+'*I' if qs[nm][1][j,0] else '') for j in range(17)]}
    return {'status':'PASS','field':'Q(i,kappa), kappa^4=1/2','four_fit_fibers_x':xs[:4],'independent_held_fiber_x':xs[4],'results':res}


def compute_joint(qq,vv):
    import json
    from pathlib import Path
    from flint import fmpq,fmpq_mat
    import sympy as s
    ROOT=Path(__file__).resolve().parent
    dat=json.loads((ROOT/'check-original-first-order-i-block-and-cm5.json').read_text())
    src=json.loads((ROOT/'check-original-three-ordinary-adjoint.json').read_text())
    U,x=s.symbols('U x')
    def pair(z):
     z=s.expand(s.sympify(z));return fmpq(str(s.re(z))),fmpq(str(s.im(z)))
    def vec(z):
     ps=list(map(pair,z));return fmpq_mat(len(ps),1,[a for a,b in ps]),fmpq_mat(len(ps),1,[b for a,b in ps])
    def hcat(ms):
     n=ms[0].nrows();return fmpq_mat(n,sum(a.ncols() for a in ms),[a[i,j] for i in range(n) for a in ms for j in range(a.ncols())])
    def realify(A,B):
     nr,nc=A.nrows(),A.ncols()
     return fmpq_mat(2*nr,2*nc,[A[i,j] if i<nr and j<nc else -B[i,j-nc] if i<nr else B[i-nr,j] if j<nc else A[i-nr,j-nc] for i in range(2*nr) for j in range(2*nc)])
    def serial(a,b):
     return [[str(a[i,j])+(' + '+str(b[i,j])+'*I' if b[i,j] else '') for j in range(a.ncols())] for i in range(a.nrows())]
    def cmul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
    def cdiv(a,b):
     d=b[0]*b[0]+b[1]*b[1];return (a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d

    def minor(A,B):
     nr,nc=A.nrows(),A.ncols(); mat=[[(A[i,j],B[i,j]) for j in range(nc)] for i in range(nr)];ids=list(range(nr));pivs=[];det=(fmpq(1),fmpq(0));sgn=1
     for j in range(nc):
      k=next((k for k in range(j,nr) if mat[k][j]!=(0,0)),None)
      if k is None:return None
      if k!=j:mat[j],mat[k]=mat[k],mat[j];ids[j],ids[k]=ids[k],ids[j];sgn=-sgn
      piv=mat[j][j];det=cmul(det,piv);pivs.append(ids[j])
      for k in range(j+1,nr):
       if mat[k][j]!=(0,0):
        fac=cdiv(mat[k][j],piv)
        for l in range(j,nc):
         pr=cmul(fac,mat[j][l]);mat[k][l]=(mat[k][l][0]-pr[0],mat[k][l][1]-pr[1])
     # Row order is the selected pivot order. Its determinant is the product of pivots (no swap sign).
     return {'row_indices':pivs,'determinant_real':str(det[0]),'determinant_imag':str(det[1])}

    Lu=fmpq_mat(18,17)
    for j in range(17):Lu[j,j]=70-4*j;Lu[j+1,j]=4*j-68
    rs=[];ims=[]
    for nm in ('A','B'):
     a,b=vec(qq['results'][nm]['kappa_times_Q0plus_native_polynomial']);rs.append(a);ims.append(b)
    a,b=vec(vv['V_KH_native_odd_polynomial']);rs.append(a);ims.append(b)
    FR,FI=hcat(rs),hcat(ims)
    PA=fmpq_mat(18,1,[fmpq(src['source_coefficients_ascending']['A'][17-j]) if 0<=17-j<len(src['source_coefficients_ascending']['A']) else 0 for j in range(18)])
    PB=fmpq_mat(18,1,[fmpq(src['source_coefficients_ascending']['B'][17-j]) if 0<=17-j<len(src['source_coefficients_ascending']['B']) else 0 for j in range(18)])
    cbR,cbI=vec(dat['theta_twice_beta_CM_polynomial'])
    s2=16*U*(U-1)**2/(U+1)**4
    R289=s.Poly(s.cancel((U+1)**17*(1-18*s2**2+16*s2**3+s2**4)),U)
    R289v=fmpq_mat(18,1,[fmpq(str(R289.nth(j))) for j in range(18)])
    DR,DI=-Lu*FR,-Lu*FI
    for j in range(18):DR[j,1]-=R289v[j,0]/320;DI[j,2]+=fmpq(8,11)*PA[j,0]
    OR=hcat([PA,PB,cbR,cbR]);OI=hcat([fmpq_mat(18,1),fmpq_mat(18,1),cbI,-cbI])
    JR,JI=hcat([OR,DR]),hcat([OI,DI])
    kpR,kpI=vec(dat['CM_corrected_A_primitive_polynomial']);kqR,kqI=vec(dat['CM_corrected_B_primitive_polynomial']);cmR,cmI=vec(dat['untwisted_odd_CM_polynomial'])
    PR,PI=hcat([kpR,kqR,cmR,cmR]),hcat([kpI,kqI,cmI,-cmI])
    KR,KI=hcat([PR,FR]),hcat([PI,FI])
    plus=fmpq_mat(18,18)
    for j in range(18):
     D=s.Poly(s.expand((x-1)**(34-2*j)*(x+1)**(2*j)+(x+1)**(34-2*j)*(x-1)**(2*j)),x)
     for k in range(18):plus[k,j]=(fmpq(k==j)+fmpq(k==17-j)+fmpq(str(D.nth(2*k)))/2**17)/4
    OffR,OffI=DR-plus*DR,DI-plus*DI
    bplusR,bplusI=hcat([PB,OffR]),hcat([fmpq_mat(18,1),OffI])
    ans={'status':'PASS',
     'image_triple_rank':realify(FR,FI).rank()//2,
     'original_four_plus_three_full_commutators_rank':realify(JR,JI).rank()//2,
     'original_four_primitive_plus_three_images_rank':realify(KR,KI).rank()//2,
     'B_plus_three_offblock_rank':realify(bplusR,bplusI).rank()//2,
     'full_commutator_minor':minor(JR,JI),
     'V_single_full_commutator_minor':minor(hcat([OR,fmpq_mat(18,1,[DR[j,2] for j in range(18)])]),hcat([OI,fmpq_mat(18,1,[DI[j,2] for j in range(18)])])),
     'V_single_primitive_minor':minor(hcat([PR,fmpq_mat(17,1,[FR[j,2] for j in range(17)])]),hcat([PI,fmpq_mat(17,1,[FI[j,2] for j in range(17)])])),
     'primitive_image_minor':minor(KR,KI),
     'B_plus_offblock_minor':minor(bplusR,bplusI),
     'three_normalized_image_coefficients':serial(FR,FI),
     'three_normalized_full_commutator_coefficients':serial(DR,DI)}

    assert ans['image_triple_rank']==3
    assert ans['original_four_plus_three_full_commutators_rank']==7
    assert ans['original_four_primitive_plus_three_images_rank']==7
    assert ans['B_plus_three_offblock_rank']==4
    # The full off-block is multiplication by 20U-54, on the actual old odd block.
    RP=[s.Poly(s.Rational(16**j,8)*U**(j-1)*(U-1)**(2*j-2)*(U+1)**(18-4*j)*(U**2-6*U+1),U) for j in range(1,5)]
    RM=fmpq_mat(17,4,[fmpq(str(r.nth(k))) for k in range(17) for r in RP])
    RMul=fmpq_mat(18,4,[fmpq(str(s.Poly(-(20*U-54)*r.as_expr(),U).nth(k))) for k in range(18) for r in RP])
    assert Lu*RM-plus*Lu*RM==RMul
    PBexpr=sum(s.Rational(str(PB[k,0]))*U**k for k in range(18))
    PBval=s.factor(PBexpr.subs(U,s.Rational(27,10)))
    assert PBval!=0
    cs=[]
    for nm in ('A','B'):cs.append(vec(qq['results'][nm]['kappa_times_Q0plus_old_coefficients']))
    cs.append(vec(vv['V_KH_old_coefficients_v1_v4']))
    ans['old_four_basis_three_image_minor']=minor(hcat([a for a,b in cs]),hcat([b for a,b in cs]))
    ans['offblock_multiplier_ascending']=['-54','20']
    ans['B_value_at_27_over_10']=str(PBval)
    return ans


def main():
    vv=compute_v()
    qq=compute_q()
    joint=compute_joint(qq,vv)
    ans={'status':'PASS','target_prime_scan':False,
         'arithmetic':'exact rational/Gaussian arithmetic and kappa^4=1/2',
         'V_H':vv,'Q_A_B':qq,'joint':joint}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps({'status':'PASS',
          'V_single_source_ranks':[vv['A_B_CMtheta_plus_full_commutator_rank'],vv['two_original_primitives_two_true_CM_plus_VKH_rank']],
          'joint_full_commutator_rank':joint['original_four_plus_three_full_commutators_rank'],
          'joint_primitive_rank':joint['original_four_primitive_plus_three_images_rank'],
          'offblock_multiplier':joint['offblock_multiplier_ascending'],
          'B_value_at_27_over_10':joint['B_value_at_27_over_10']},indent=2))

if __name__=='__main__':
    main()
