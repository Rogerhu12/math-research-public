#!/usr/bin/env python3
"""R464: the complete characteristic-zero CM7 matrix and fixed delta sources.

All fibers are exact in Q(delta), delta^2=-3.  Matrix columns are the complete
theta basis sigma^N*x^offset*(1,X,...,X^d), X=x^3.  The normalization is
N7=M_gamma/gamma, gamma=(5+delta)/2.  No target-prime scan is used.
"""
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import argparse
import gzip
import json
import time
from flint import fmpq as Q, fmpq_mat as Mat, fmpq_poly as Poly

ZERO=(Q(0),Q(0))
ONE=(Q(1),Q(0))
def fq(a=0,b=0):
    return (Q(a),Q(b))
def fa(x,y): return (x[0]+y[0],x[1]+y[1])
def fn(x): return (-x[0],-x[1])
def fs(x,y): return fa(x,fn(y))
def fm(x,y): return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def fi(x):
    den=x[0]*x[0]+3*x[1]*x[1]
    assert den
    return (x[0]/den,-x[1]/den)
def fp(x,n):
    out=ONE
    if n<0:x,n=fi(x),-n
    while n:
        if n&1:out=fm(out,x)
        x=fm(x,x);n//=2
    return out
def ptrim(A):
    while len(A)>1 and A[-1]==ZERO:A.pop()
    return A
def pa(A,B):
    return ptrim([fa(A[i] if i<len(A) else ZERO,B[i] if i<len(B) else ZERO)
                  for i in range(max(len(A),len(B)))])
def ps(A,c): return ptrim([fm(x,c) for x in A])
def pm(A,B):
    C=[ZERO]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        if x==ZERO:continue
        for j,y in enumerate(B):
            if y!=ZERO:C[i+j]=fa(C[i+j],fm(x,y))
    return ptrim(C)
def pd(A,B):
    A=A[:];quot=[ZERO]*max(1,len(A)-len(B)+1)
    ib=fi(B[-1])
    while A!=[ZERO] and len(A)>=len(B):
        k=len(A)-len(B);v=fm(A[-1],ib);quot[k]=v
        for j,b in enumerate(B):A[k+j]=fs(A[k+j],fm(v,b))
        ptrim(A)
    return ptrim(quot),A

def exact_fiber_row(args):
    N,offset,a=args
    d=(N//2-offset)//3
    rem=N//2-offset-3*d
    gamma=(Q(5,2),Q(1,2))
    gb=(Q(5,2),Q(-1,2))
    r=(Q(2,7),Q(-6,7));rb=(Q(2,7),Q(6,7))
    ga=fm(fp(gamma,2),fq(a))
    F=[fn(fm(ga,fp(r,2))),fm(r,fa(fm(fq(7),r),fq(24))),ZERO,
       fm(fq(2),fm(ga,r)),fa(fm(fq(28),r),fq(12)),ZERO,fn(ga),ONE]
    def red(A):
        A=A[:]
        for i in range(len(A)-1,6,-1):
            v=A[i]
            if v!=ZERO:
                for j in range(7):A[i-7+j]=fs(A[i-7+j],fm(v,F[j]))
        return ptrim(A[:7])
    def rm(A,B): return red(pm(A,B))
    def rp(A,n):
        out=[ONE]
        while n:
            if n&1:out=rm(out,A)
            A=rm(A,A);n//=2
        return out
    def ri(A):
        r0,r1,s0,s1=F,A,[ZERO],[ONE]
        while r1!=[ZERO]:
            q,r2=pd(r0,r1)
            s2=pa(s0,ps(pm(q,s1),fq(-1)))
            r0,r1,s0,s1=r1,r2,s1,s2
        assert len(r0)==1 and r0[0]!=ZERO
        ans=red(ps(s0,fi(r0[0])))
        assert rm(A,ans)==[ONE]
        return ans
    q=[fn(r),ZERO,ZERO,ONE]
    qb=[fn(rb),ZERO,ZERO,ONE]
    Nb=[fm(rb,fa(fm(fq(7),rb),fq(24))),ZERO,ZERO,
        fa(fm(fq(28),rb),fq(12)),ZERO,ZERO,ONE]
    T1=rm([ZERO,ONE],Nb)
    V1=ps(rp(qb,2),fp(gb,2))
    U,W=rp(T1,3),rp(V1,3)
    Up,Wp=[[ONE]],[[ONE]]
    for j in range(d):
        Up.append(rm(Up[-1],U));Wp.append(rm(Wp[-1],W))
    # One common frame for every basis column, with normalization 1/gamma.
    frame=ps(rm(rp(ri(q),N),rm(rp(T1,offset),rp(V1,rem))),
             fm(fp(gamma,-N-1),fq(Q(1,a**offset))))
    traces=[fq(7)]
    for k in range(1,7):
        v=fm(fq(k),F[7-k])
        for j in range(1,k):v=fa(v,fm(F[7-j],traces[k-j]))
        traces.append(fn(v))
    values=[]
    for j in range(d+1):
        E=rm(frame,rm(Up[j],Wp[d-j]))
        val=ZERO
        for i,c in enumerate(E):val=fa(val,fm(c,traces[i]))
        values.append([str(val[0]),str(val[1])])
    return a,values

def km(A,B):
    R,I=A;S,J=B
    return (R*S-3*(I*J),R*J+I*S)
def ka(A,B):return (A[0]+B[0],A[1]+B[1])
def kn(A):return (-A[0],-A[1])
def ks(A,c):
    return (c[0]*A[0]-3*c[1]*A[1],c[0]*A[1]+c[1]*A[0])
def kp(A,n,identity):
    out=identity
    while n:
        if n&1:out=km(out,A)
        A=km(A,A);n//=2
    return out
def kzero(rows,cols):return (Mat(rows,cols),Mat(rows,cols))
def kvec(v):return (Mat([[x] for x in v]),Mat(len(v),1))
def serialize_matrix(A):
    return {"real":[[str(A[0][i,j]) for j in range(A[0].ncols())] for i in range(A[0].nrows())],
            "delta":[[str(A[1][i,j]) for j in range(A[1].ncols())] for i in range(A[1].nrows())]}
def serialize_field(x):return [str(x[0]),str(x[1])]
def get_entry(A,i,j=0):return (A[0][i,j],A[1][i,j])

def spectral_mass_polynomial(masses,tau):
    """Mass of the lambda eigensource, as a quadratic modulo lambda^3=tau."""
    out=[ZERO,ZERO,ZERO]
    for j,mass in enumerate(masses):
        e=(-j)%18
        out[e%3]=fa(out[e%3],fm(mass,fp(tau,e//3)))
    return [fm(x,fq(Q(1,18))) for x in out]

def source_polynomials():
    X=Poly([0,1])
    p13=[Q(0),Q(10880,14847),Q(-13504,14847),Q(6269,9898),Q(-6523,59388),Q(-37,33936)]
    p15=[Q(0),Q(923,1470),Q(107,5880),Q(11399,15680),Q(-15919,94080),Q(-37,53760)]
    sources=[]
    for P in (p13,p15):
        a=Poly([0])
        for j in range(1,6):
            a+=P[j]*Q(-1,27)**j*X**(10-2*j)*(X+4)**(3*j-1)
        a=8*3**16*(X+1)*(X-8)*a
        sources.append([a[j] for j in range(18)])
    originals=[
        [Q(-128,7),Q(-80,7),Q(-12,7),Q(-53,7),Q(1)],
        [Q(-2048),Q(12032),Q(8128),Q(400),Q(-208),Q(1)],
        [Q(1024),Q(-6784),Q(-14912),Q(-272),Q(272),Q(1)],
    ]
    pulls=[]
    for P in originals:
        a=Poly([0])
        for j,c in enumerate(P):
            a+=c*Q(-1,27)**j*X**(10-2*j)*(X+4)**(3*j+2)
        a=-3**15*a
        pulls.append([a[j] for j in range(18)])
    return sources,pulls

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--degree",type=int,default=102)
    ap.add_argument("--offset",type=int,default=0)
    ap.add_argument("--workers",type=int,default=2)
    ap.add_argument("--output",default=str(Path(__file__).with_suffix(".json")))
    args=ap.parse_args()
    N,o=args.degree,args.offset
    assert N%2==0
    d=(N//2-o)//3;size=d+1
    targets=list(range(1,size+1))
    start=time.monotonic()
    rows={}
    if args.workers==1:
        iterator=map(exact_fiber_row,[(N,o,a) for a in targets])
        for a,row in iterator:
            rows[a]=row
            print(f"exact degree {N} fiber {a}/{size}, {time.monotonic()-start:.1f}s",flush=True)
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            futs=[pool.submit(exact_fiber_row,(N,o,a)) for a in targets]
            for fut in as_completed(futs):
                a,row=fut.result();rows[a]=row
                print(f"exact degree {N} fiber {a}/{size}, {time.monotonic()-start:.1f}s",flush=True)
    V=Mat([[Q(a**(3*j)) for j in range(size)] for a in targets])
    Vi=V.inv()
    MR=Vi*Mat([[Q(rows[a][j][0]) for j in range(size)] for a in targets])
    MI=Vi*Mat([[Q(rows[a][j][1]) for j in range(size)] for a in targets])
    M=(MR,MI)
    I=(Mat([[int(i==j) for j in range(size)] for i in range(size)]),Mat(size,size))
    assert km((V,Mat(size,size)),M)==(
        Mat([[Q(rows[a][j][0]) for j in range(size)] for a in targets]),
        Mat([[Q(rows[a][j][1]) for j in range(size)] for a in targets]))
    report={"field":"Q(delta), delta^2=-3","curve_b":1,
            "normalization":"N7=M_gamma/gamma, gamma=(5+delta)/2",
            "degree":N,"offset":o,"dimension":size,
            "basis":"sigma^N*x^offset*(1,X,...,X^d), X=x^3",
            "fiber_targets":targets,"matrix":serialize_matrix(M)}
    print(f"complete exact matrix interpolated, {time.monotonic()-start:.1f}s",flush=True)
    if N==102 and o==0:
        M3=kp(M,3,I);M6=km(M3,M3);M9=km(M6,M3);M12=km(M6,M6)
        assert km(M12,M6)==I
        report["exact_N7_power18_identity"]=True
        M15=km(M12,M3)
        annihilator=kzero(size,size)
        for power in (I,M3,M6,M9,M12,M15):annihilator=ka(annihilator,power)
        assert annihilator==kzero(size,size)
        report["exact_whole_annihilator"]="1+N7^3+N7^6+N7^9+N7^12+N7^15=0"
        ray_a,ray_b,mod=1428552127,2161889730,204
        invnorm=pow((ray_a**2-ray_a*ray_b+ray_b**2)%mod,-1,mod)
        gray=((ray_a**2-ray_b**2)*invnorm%mod,(2*ray_a*ray_b-ray_b**2)*invnorm%mod)
        inv7=pow(7,-1,mod);g7=(8*inv7%mod,5*inv7%mod);g9=(1,0)
        for j in range(9):
            aa,bb=g9;cc,dd=g7
            g9=((aa*cc-bb*dd)%mod,(aa*dd+bb*cc-bb*dd)%mod)
        assert gray==g9==(67,0)
        report["ordinary_core"]={
            "formula":"K102=-N7^9; whole Heisenberg ratio mod 204 and S(delta z) absolute anchor",
            "ratio_pi_mod204":list(gray),"ratio_gamma7_mod204":list(g7),
            "ratio_gamma7_ninth_mod204":list(g9)}
        om=(Q(-1,2),Q(1,2));om2=(Q(-1,2),Q(-1,2))
        taus=[fq(-1),om,om2,fn(om),fn(om2)]
        powers=[I,M3,M6,M9,M12]
        blockprojectors=[]
        for tau in taus:
            P=[ONE];den=ONE
            for other in taus:
                if other==tau:continue
                P=pm(P,[fn(other),ONE]);den=fm(den,fs(tau,other))
            P=ps(P,fi(den))
            Proj=kzero(size,size)
            for k,c in enumerate(P):Proj=ka(Proj,ks(powers[k],c))
            trace=ZERO
            for j in range(size):trace=fa(trace,get_entry(Proj,j,j))
            blockprojectors.append(Proj)
            assert trace[1]==0 and trace[0].denominator==1
            print("N7^3 block",serialize_field(tau),"dimension",str(trace[0]),flush=True)
        assert sum((get_entry(P,j,j)[0] for P in blockprojectors for j in range(size)),Q(0))==18
        report["N7_cubed_block_dimensions"]=[
            {"eigenvalue":serialize_field(tau),"dimension":str(sum((get_entry(P,j,j)[0] for j in range(size)),Q(0)))}
            for tau,P in zip(taus,blockprojectors)]
        sourcevecs,pulls=source_polynomials()
        pullvecs=[kvec(v) for v in pulls]
        lambdas=[fq(-1),fn(om),fn(om2)]
        for v,lam in zip(pullvecs,lambdas):assert km(M,v)==ks(v,lam)
        report["arithmetic_pullback_basis"]={
            label:serialize_matrix(v) for label,v in zip(["S(delta z)","H3(delta z)","H5(delta z)"],pullvecs)}
        outputs=[]
        for label,coefs in zip(["A13","A15"],sourcevecs):
            v=kvec(coefs);orbit=[v]
            for j in range(1,18):orbit.append(km(M,orbit[-1]))
            assert km(M,orbit[-1])==v
            arithmetic=[]
            for idx,lam in enumerate(lambdas):
                part=kzero(size,1)
                for j,w in enumerate(orbit):part=ka(part,ks(w,fp(lam,-j)))
                part=ks(part,fq(Q(1,18)))
                leadidx=16 if idx==0 else 17
                coeff=fm(get_entry(part,leadidx),fi(get_entry(pullvecs[idx],leadidx)))
                assert part==ks(pullvecs[idx],coeff)
                arithmetic.append({"source":["S(delta z)","H3(delta z)","H5(delta z)"][idx],
                                   "eigenvalue":serialize_field(lam),"coefficient":serialize_field(coeff),
                                   "mass":serialize_field(get_entry(part,17))})
            blocks=[km(P,v) for P in blockprojectors]
            a_constant=Q(-37,33936) if label=="A13" else Q(-37,53760)
            positive_mass=fa(get_entry(blocks[1],17),get_entry(blocks[2],17))
            negative_mass=fa(fa(get_entry(blocks[0],17),get_entry(blocks[3],17)),get_entry(blocks[4],17))
            assert positive_mass==fq(-a_constant) and negative_mass==fq(a_constant)
            assert blocks[0]==ka(ka(ks(pullvecs[0],tuple(Q(x) for x in arithmetic[0]["coefficient"])),
                                      ks(pullvecs[1],tuple(Q(x) for x in arithmetic[1]["coefficient"]))),
                                      ks(pullvecs[2],tuple(Q(x) for x in arithmetic[2]["coefficient"])))
            outputs.append({"label":label,"polynomial_coefficients_ascending":[str(x) for x in coefs],
                            "arithmetic_components":arithmetic,
                            "ordinary_central_mass_divided_by_lambda":serialize_field(fq(-2*a_constant)),
                            "complete_mass_orbit":[serialize_field(get_entry(w,17)) for w in orbit],
                            "individual_external_spectral_mass_polynomials":[
                              {"relation":"eigenvalue^3=tau","tau":serialize_field(tau),
                               "coefficients_ascending":[serialize_field(c) for c in
                                 spectral_mass_polynomial([get_entry(w,17) for w in orbit],tau)]}
                              for tau in taus[1:]],
                            "N7_cubed_blocks":[{"eigenvalue":serialize_field(tau),
                               "source":serialize_matrix(w),"mass":serialize_field(get_entry(w,17))}
                               for tau,w in zip(taus,blocks)]})
            print(label,"arithmetic coefficients",
                  [x["coefficient"] for x in arithmetic],flush=True)
        report["sources"]=outputs
    payload=json.dumps(report,separators=(",",":"))+"\n"
    output=Path(args.output)
    if len(payload.encode())>1_000_000:
        if output.suffix!=".gz":output=output.with_suffix(output.suffix+".gz")
        with gzip.open(output,"wt") as f:f.write(payload)
    else:output.write_text(payload)
    print(json.dumps({"status":"complete exact matrix and assertions passed",
                      "elapsed_seconds":time.monotonic()-start,
                      "output":str(output),"bytes":output.stat().st_size}),flush=True)

if __name__=="__main__":main()

