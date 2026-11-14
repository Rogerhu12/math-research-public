#!/usr/bin/env python3
"""R480: exact CM19 on the actual degree72 inputs and the degree4 line."""
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import runpy,json,time
BASE=Path(__file__).resolve().parents[1]
H=runpy.run_path(str(BASE/"scripts/check-r466-fixed-two-division-source.py"))
for key in ("Q","Mat","Poly","fq","fa","fn","fs","fm","fi","fp","pa","ps","pm","pd","ptrim",
            "km","ka","ks","kp","kvec","identity","kinv","rank","cols","get_entry","serialize_matrix"):
    globals()[key]=H[key]
ZERO,ONE=fq(0),fq(1)

def fiber(args):
    N,offset,a=args
    J=(N-2*offset)//6
    assert 2*offset+6*J==N
    gamma,q=H["q19_polynomial"]()
    gb=(gamma[0],-gamma[1])
    qb=[(x[0],-x[1])for x in q]
    ng=H["qmap"](q,19);nb=[(x[0],-x[1])for x in ng]
    F=pa(ng,ps(pm(q,q),fm(fq(-a),fp(gamma,2))))
    def red(A):
        A=A[:]
        for i in range(len(A)-1,18,-1):
            v=A[i]
            if v!=ZERO:
                for j in range(19):A[i-19+j]=fs(A[i-19+j],fm(v,F[j]))
        return ptrim(A[:19])
    def rm(A,B):return red(pm(A,B))
    def rp(A,n):
        out=[ONE]
        while n:
            if n&1:out=rm(out,A)
            A=rm(A,A);n//=2
        return out
    def ri(A):
        r0,r1,s0,s1=F,A,[ZERO],[ONE]
        while r1!=[ZERO]:
            q0,r2=pd(r0,r1)
            r0,r1,s0,s1=r1,r2,s1,pa(s0,ps(pm(q0,s1),fq(-1)))
        assert len(r0)==1 and r0[0]!=ZERO
        out=red(ps(s0,fi(r0[0])))
        assert rm(A,out)==[ONE]
        return out
    T=red(nb);V=ps(rp(qb,2),fp(gb,2))
    U,W=rp(T,3),rp(V,3)
    Up,Wp=[[ONE]],[[ONE]]
    for j in range(J):Up.append(rm(Up[-1],U));Wp.append(rm(Wp[-1],W))
    frame=ps(rm(rp(ri(q),N),rp(T,offset)),fm(fp(gamma,-N-1),fq(Q(1,a**offset))))
    traces=[fq(19)]
    for k in range(1,19):
        val=fm(fq(k),F[19-k])
        for j in range(1,k):val=fa(val,fm(F[19-j],traces[k-j]))
        traces.append(fn(val))
    vals=[]
    for j in range(J+1):
        poly=rm(frame,rm(Up[j],Wp[J-j]))
        val=ZERO
        for k,c in enumerate(poly):val=fa(val,fm(c,traces[k]))
        vals.append(val)
    return a,vals

def decode(data):
    return tuple(Mat([[Q(x)for x in row]for row in data[part]])for part in ("real","delta"))
def main():
    start=time.monotonic()
    rows={}
    with ProcessPoolExecutor(max_workers=2)as ex:
        futs=[ex.submit(fiber,(72,0,a))for a in range(1,14)]
        for fut in as_completed(futs):
            a,row=fut.result();rows[a]=row
    V=Mat([[Q(a)**(3*j)for j in range(13)]for a in range(1,14)])
    Vi=V.inv()
    N=tuple(Vi*Mat([[rows[a][j][k]for j in range(13)]for a in range(1,14)])for k in (0,1))
    raw=json.loads((BASE/"notes/2026-11-14-literature-degree72-cm7-exact.json").read_text())
    M=decode(raw["matrix"])
    I=identity(13)
    assert km(M,N)==km(N,M)
    assert kp(N,6,I)==I
    assert km(M,(M[0],-M[1]))==I and km(N,(N[0],-N[1]))==I
    data=json.loads((BASE/"scripts/check-r474-six-sigma-two-output-core.json").read_text())
    F1=kvec([Q(x)for x in data["F72_N7_eigen_one"]])
    F2=kvec([Q(x)for x in data["F72_N7_eigen_omega_squared"]])
    out={"normalization":"N19=M_gamma/gamma, gamma=4+delta; b=1; degree72 basis sigma72 X^j",
         "matrix":serialize_matrix(N),"input_fibers":list(range(1,14)),
         "F_components":[]}
    omega=fq(Q(-1,2),Q(1,2))
    eigenpairs=[(fq(1),fn(fp(omega,2))),(fp(omega,2),fq(-1))]
    for (name,v),(lam7,lam19) in zip((("F1",F1),("Fomega2",F2)),eigenpairs):
        assert km(M,v)==ks(v,lam7) and km(N,v)==ks(v,lam19)
        joint=H["eig_project"](N,lam19,H["eig_project"](M,lam7,I,6),6)
        assert rank(joint)==1
        orbit=[];cur=v
        for j in range(24):
            orbit.append(cur);cur=km(N,cur)
        r=rank(cols(orbit))
        print(name,"N19 cyclic rank",r,flush=True)
        out["F_components"].append({"name":name,"orbit_rank":r,
            "eigen_N7":[str(x)for x in lam7],"eigen_N19":[str(x)for x in lam19],
            "joint_dimension":1,
            "first_image":serialize_matrix(km(N,v))})
    _,small=fiber((4,2,1))
    assert small==[fq(-1)]
    out["Theta_squared_N19"]=[[str(x)for x in small[0]]]
    print("Theta squared N19",out["Theta_squared_N19"],flush=True)
    # The complete first-axis new-line projector, applied to both actual inputs.
    pdat=json.loads((BASE/"scripts/check-r477-rank-one-companion.json").read_text())
    P=decode(pdat["rank_one_projector"])
    fdat=json.loads((BASE/"scripts/check-r471-original-six-sigma-normtwo-factor.json").read_text())
    upoly=Poly([Q(x)for x in fdat["theta4_in_sigma32_x_frame"]])**2
    raw136=json.loads((BASE/"scripts/check-r466-fixed-two-division-source.json").read_text())
    new=kvec([Q(x)for x in raw136["new_source_b1_polynomial"]])
    masses=[]
    for v in (F1,F2):
        fv=Poly([v[0][j,0]for j in range(13)])
        product=fv*upoly
        projected=km(P,kvec([product[j]for j in range(23)]))
        c=get_entry(projected,21)
        assert c[1]==0 and projected==ks(new,c)
        masses.append(str(c[0]))
    assert masses==["5824/9","11648/9"]
    out["actual_companion_masses"]=masses
    M136=decode(json.loads((BASE/"notes/2026-11-14-theta-degree136-cm7-exact.json").read_text())["matrix"])
    N136=decode(json.loads((BASE/"notes/2026-11-14-theta-degree136-cm19-exact.json").read_text())["matrix"])
    I136=identity(23)
    assert km(M136,(M136[0],-M136[1]))==I136
    assert km(N136,(N136[0],-N136[1]))==I136
    E1=H["eig_project"](M136,fq(1),I136)
    Pref=ks(ka(E1,ks(km(N136,E1),fn(fp(omega,2)))),fq(Q(1,2)))
    assert rank(Pref)==1 and km(Pref,Pref)==Pref and km(Pref,P)==H["kzero"](23,23)
    refmasses=[];href=None
    for v in (F1,F2):
        product=Poly([v[0][j,0]for j in range(13)])*upoly
        projected=km(Pref,kvec([product[j]for j in range(23)]))
        c=get_entry(projected,22)
        assert c[1]==0
        refmasses.append(str(c[0]))
        normalized=ks(projected,fi(c))
        if href is None:href=normalized
        else:assert href==normalized
    assert refmasses==["2/27","-2/27"]
    out["actual_reference_companion_masses_b1"]=refmasses
    out["Href_mass_one"]=serialize_matrix(href)
    chis=[fn(omega),fq(-1)];taus=[fp(omega,2),fq(1)]
    expected=[[P,H["kzero"](23,23)],[Pref,P],[H["kzero"](23,23),Pref]]
    # Substitute the actual simultaneous characters to check each entire W operator.
    for row in range(3):
        for k in range(2):
            if row<2:
                evalue=fm(chis[k],fi(fm(omega,chis[row])))
                coeff=fm(omega,fm(taus[row],fi(taus[k])))
            else:
                evalue=fn(chis[k])
                coeff=fm(fp(omega,2),fi(taus[k]))
            E=H["eig_project"](M136,evalue,I136)
            val=ks(ka(E,ks(km(N136,E),fn(coeff))),fq(Q(1,2)))
            assert val==expected[row][k]
    out["companion_only_arithmetic_projection_table"]=[["new","zero"],["reference","new"],["zero","reference"]]
    out["simultaneous_characters"]=[
        {"N7":[str(x)for x in fn(omega)],"N19":[str(x)for x in fp(omega,2)]},
        {"N7":["-1","0"],"N19":["1","0"]}]
    out["new_companion_eigenpairs"]=[
        {"N7":[str(x)for x in fn(fp(omega,2))],"N19":["-1","0"]},
        {"N7":[str(x)for x in fn(omega)],"N19":[str(x)for x in fn(omega)]}]
    T=Mat([[1,4],[2,-9]])
    assert T.det()==-17
    assert T*Mat([[72,0],[0,4]])*T.transpose()==Mat([[136,0],[0,612]])
    assert (-17)%7!=0 and (-17)%19!=0
    out["output_matrix"]=[[str(T[i,j])for j in range(2)]for i in range(2)]
    out["full_fiber_determinant"]="-17"
    out["elapsed_seconds"]=round(time.monotonic()-start,3)
    Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
    print("Full degree72 CM19 and degree4 fiber passed.",out["elapsed_seconds"],"s")
if __name__=="__main__":main()

