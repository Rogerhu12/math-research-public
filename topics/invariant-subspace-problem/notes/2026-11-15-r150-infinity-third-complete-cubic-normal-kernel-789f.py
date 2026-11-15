#!/usr/bin/env python3
"""R150: complete degree<=5 cubic-normal correction kernel at infinity.

Bind all PAID first/second/third data and the paid single-cubic-column trial.
The new correction has all990 target coordinates c^a d^b z_i z_j z_k,
a+b<=2.  Its full2295 rows on source multipliers with exactly2 normal
factors are imposed as a homogeneous kernel H3.  H3 includes the original
linear normal terms AND both tangent-linear normal terms of F0.
Sources with3 normal factors give >=4 normal output and are exactly zero.

Only after the complete H3 kernel N is verified do we add its actual
low1088 image K3*N to the paid A0.T correction space.  A second small RREF
constructs actual third left jets.  No high-source equations are dropped.
The previous legal cubic evaluation column is explicitly recovered inside
N and its full low-column SHA is bound to the actual paid trial.

All matrices remain job-temporary.  No old NF/Dixon is rerun.  Positive
residual rank is only an upper bound; quartic/quintic normal target
corrections have not been excluded.
"""
import argparse
import hashlib
import gzip
import importlib.util
import json
from math import comb
import os
from pathlib import Path
import resource
import signal
import time

FIRST_SHA256="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
SECOND_SHA256="6cb201867c430b4375dbe93cb411ad1e74bea39571261d1ecfec233e4b397517"

def require(ok,message):
    if not ok:
        raise AssertionError(message)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def field(result,key):
    return result.get(key,result.get("parameters",{}).get(key))

def result_at(path):
    obj=json.loads(Path(path).read_text())
    obj=obj.get("result",obj)
    require(obj.get("status")=="completed","Paid input incomplete")
    return obj


CHECKPOINT_FORMAT="r150-complete-cubic-kernel-temporary-v1"

def checkpoint_binding(a):
    named={
        "script":sha(__file__),"firstGenerator":sha(a.generator),
        "secondGenerator":sha(a.normal_generator),
        "firstReceipt":sha(a.first_connection_receipt),
        "pureSecondReceipt":sha(a.second_pure_receipt),
        "normalSecondReceipt":sha(a.second_normal_receipt),
        "thirdReceipt":sha(a.third_receipt),"cubicReceipt":sha(a.cubic_receipt),
    }
    return hashlib.sha256(json.dumps(named,sort_keys=True,separators=(",",":"))
                          .encode("ascii")).hexdigest(),named

def checkpoint_manifest(a):
    return Path(a.checkpoint_dir)/"complete-cubic-kernel-checkpoint.json"

def read_manifest(a,binding):
    path=checkpoint_manifest(a)
    if not path.exists():
        return {"format":CHECKPOINT_FORMAT,"binding":binding,"phases":{}}
    obj=json.loads(path.read_text())
    require(obj.get("format")==CHECKPOINT_FORMAT and obj.get("binding")==binding,
            "Checkpoint does not match exact source and semantic input bytes")
    require(obj.get("temporaryOnly") is True,"Checkpoint temporary-only contract")
    return obj

def load_phase(m,a,binding,phase,result):
    man=read_manifest(a,binding)
    entry=man["phases"].get(phase)
    if entry is None:
        return None
    path=Path(a.checkpoint_dir)/entry["file"]
    require(path.parent==Path(a.checkpoint_dir),"Checkpoint filename escapes directory")
    require(path.stat().st_size==entry["bytes"] and sha(path)==entry["sha256"],
            "Checkpoint actual matrix bytes/hash changed")
    with gzip.open(path,"rt",encoding="utf-8") as f:
        p=json.load(f)
    require(p.get("format")==CHECKPOINT_FORMAT and p.get("binding")==binding
            and p.get("phase")==phase and p.get("complete") is True,
            "Incomplete or incompatible actual matrix checkpoint")
    nr,nc=p["shape"]
    rows=p["matrix"]
    require(len(rows)==nr and all(len(row)==nc for row in rows),
            "Checkpoint full matrix dimensions")
    M=m.fmpq_mat([[m.fmpq(x) for x in row] for row in rows])
    require(m.matrix_hash(M)==p["matrixSHA256"],"Checkpoint exact rational matrix SHA")
    result["parameters"].setdefault("resumedPhases",[]).append(phase)
    result["parameters"]["checkpointManifestSHA256"]=sha(checkpoint_manifest(a))
    return M,p["metadata"]

def save_phase(m,a,binding,phase,M,metadata,result):
    directory=Path(a.checkpoint_dir)
    directory.mkdir(parents=True,exist_ok=True)
    man=read_manifest(a,binding)
    payload={
        "format":CHECKPOINT_FORMAT,"binding":binding,"phase":phase,
        "complete":True,"shape":[M.nrows(),M.ncols()],
        "matrixSHA256":m.matrix_hash(M),"metadata":metadata,
        "matrix":[[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())],
    }
    temporary=directory/(phase+".tmp.json.gz")
    with gzip.open(temporary,"wt",encoding="utf-8") as f:
        json.dump(payload,f,sort_keys=True,separators=(",",":"))
    digest=sha(temporary)
    final=directory/(phase+"-"+digest+".json.gz")
    os.replace(temporary,final)
    man["temporaryOnly"]=True
    man["phases"][phase]={"file":final.name,"bytes":final.stat().st_size,
                          "sha256":digest,"matrixSHA256":payload["matrixSHA256"]}
    path=checkpoint_manifest(a);tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(man,sort_keys=True,indent=2))
    os.replace(tmp,path)
    result["parameters"]["checkpointManifestSHA256"]=sha(path)
    result["parameters"]["checkpointPhases"]=man["phases"]

def reserve_for_next_step(a,label):
    if a._deadline-time.monotonic()<4.0:
        raise TimeoutError("Verified temporary checkpoint saved; resume before "+label)

def third_coefficients(m,paid_hashes):
    K=m.fmpq_mat([[m.ORIGINAL_K[5-i][5-j] for j in range(6)] for i in range(6)])
    J2=m.polynomial_power_kernel(K,2)
    J3=m.polynomial_power_kernel(K,3)
    J3inv=J3.inv()
    require(J3inv*J3==m.fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)]),
            "Original J3 inverse failed")
    p=[[K[i,k] for i in range(6)] for k in range(4)]
    y=[[m.ONE if i==k else m.ZERO for i in range(6)] for k in range(4)]
    maps=[]
    for k in range(4):
        B=m.fmpq_mat([[p[k][i-j] if 0<=i-j<6 else m.ZERO
                       for j in range(11)] for i in range(16)])
        maps.append(J3inv*B*J2)
    hashes={"J2":m.matrix_hash(J2),"J3":m.matrix_hash(J3)}
    for k in range(4):
        hashes["L_y"+str(k)]=m.matrix_hash(maps[k])
    for key in ("J2","J3","L_y0","L_y1","L_y2"):
        require(hashes[key]==paid_hashes[key],"Paid physical map changed: "+key)

    def moment(j):
        return [m.sequence(j+k,comb(j+k,k)) for k in range(4)]
    def add(A,B):
        return [m.add_vectors(A[k],B[k]) for k in range(4)]
    def neg(A):
        return [m.scale_vector(A[k],-1) for k in range(4)]
    def lp(t,v):
        return m.fmpq_mat([[sum((t[i+j+k]*v[k] for k in range(6)),m.ZERO)
                             for j in range(6)] for i in range(6)])
    def contract(t,Q):
        return [sum((t[i+j+k]*Q[j,k] for j in range(6) for k in range(6)),m.ZERO)
                for i in range(6)]

    def F3(jets):
        M=[m.hankel(v) for v in jets]
        KM=[K*X for X in M]
        KMK=[X*K for X in KM]
        tensors=[]; quadratic=[]; tau=[]
        for k in range(4):
            l=m.fmpq_mat(16,1)
            Q=m.fmpq_mat(6,6)
            for r in range(k+1):
                l+=maps[r]*m.column(jets[k-r])
                Q+=M[r]*K*M[k-r]
            tensors.append(m.values(l))
            quadratic.append(Q)
            tau.append(sum((m.trace(KM[r]*KM[k-r]) for r in range(k+1)),m.ZERO))
        N=4*quadratic[3]
        gamma=[m.ZERO]*6
        for r in range(4):
            N+=6*lp(tensors[r],p[3-r])
            gp=m.values(quadratic[r]*m.column(p[3-r]))
            gc=contract(tensors[r],KMK[3-r])
            gamma=[gamma[i]+2*tau[r]*y[3-r][i]+8*gp[i]-12*gc[i]
                   for i in range(6)]
        KNK=K*N*K
        polar=[sum((KNK[i,j] for i in range(6) for j in range(6)
                    if i+j==degree),m.ZERO) for degree in range(11)]
        return polar+gamma

    tangent=[moment(0),moment(1)]
    seed3=[0]*7+[80,128,96,48]+[0]*6
    for jets,d in ((tangent[0],0),(tangent[1],1),(neg(tangent[0]),0),
                   (neg(tangent[1]),-1),(add(tangent[0],tangent[1]),1)):
        require(F3(jets)==[m.fmpq(d*d*x) for x in seed3],
                "True all17 infinity pure third coefficient failed")
    coeff={}
    for j in range(2,11):
        Z=moment(j); F=F3(Z); Fn=F3(neg(Z))
        modes=[[(F[i]-Fn[i])/2 for i in range(17)]]
        for A in tangent:
            FA,Fs=F3(A),F3(add(A,Z))
            modes.append([Fs[i]-F[i]-FA[i] for i in range(17)])
        coeff[j]=modes
    cols=[(a,degree-a,j) for degree in range(5)
          for a in range(degree+1) for j in range(2,11)]
    rows=[(i,a,degree-a) for i in range(17) for degree in range(4)
          for a in range(degree+1)]
    idx={t:j for j,t in enumerate(cols)}
    P3=m.fmpq_mat(170,135)
    for rr,(i,a,b) in enumerate(rows):
        for j in range(2,11):
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                P3[rr,idx[(a+da,b+db,j)]]+=coeff[j][mode][i]

    # A1.T on the second-normal part of the paid second correction.
    # This uses exactly the original paid first physical evaluator.
    first_eval,first_hashes=m.original_jet_evaluator(K)
    for key in first_hashes:
        require(first_hashes[key]==paid_hashes[key],"Paid first evaluator map mismatch")
    first_normal={}
    quad1={}
    for j in range(2,11):
        Z=m.shifted_jet(j)
        F=first_eval(*Z)
        Fn=first_eval(*(m.scale_vector(v,-1) for v in Z))
        first_normal[j]=F
        quad1[(j,j)]=[(F[1][i]+Fn[1][i])/2 for i in range(17)]
    for j in range(2,11):
        for k in range(j+1,11):
            A=m.shifted_jet(j);B=m.shifted_jet(k)
            Fs=first_eval(*(m.add_vectors(A[r],B[r]) for r in range(2)))
            quad1[(j,k)]=[Fs[1][i]-first_normal[j][1][i]-first_normal[k][1][i]
                          for i in range(17)]
    hashes["P3"]=m.matrix_hash(P3)
    return P3,quad1,seed3,hashes

def make_J(m,order,P,linear,quadratic,pure_rows,one_rows,two_index,pairs):
    J=m.fmpq_mat(1088,585)
    for rr,(i,a,b) in enumerate(pure_rows):
        for col in range(135):
            J[rr,col]=P[rr,col]
        for j,k in pairs:
            J[rr,two_index[(a,b,j,k)]]+=quadratic[(j,k)][i]
    for rr,(i,a,b,l) in enumerate(one_rows):
        row=170+rr
        for j in range(2,11):
            x,y=min(j,l),max(j,l)
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                J[row,two_index[(a+da,b+db,x,y)]]+=linear[j][mode][order][i]
    return J

def extract_final_kernel(m,M,start,expected_prefix,expected_rank=None):
    R,rank=M.rref()
    piv=m.pivot_columns(R,rank)
    prefix=sum(c<start for c in piv)
    require(prefix==expected_prefix,"Paid leading block rank changed")
    if expected_rank is not None:
        require(rank==expected_rank,"Paid augmented rank changed")
    free=[c for c in range(start,M.ncols()) if c not in set(piv)]
    C=m.fmpq_mat(M.ncols(),len(free))
    for j,c in enumerate(free):
        C[c,j]=1
        for i,p in enumerate(piv):
            C[p,j]=-R[i,c]
    require(m.matrix_zero(M*C),"Full original correction multiplication failed")
    return C,rank,piv,free

def run(a,result):
    require(sha(a.generator)==FIRST_SHA256,"Paid first generator SHA mismatch")
    require(sha(a.normal_generator)==SECOND_SHA256,"Paid second generator SHA mismatch")
    n=module_at("r150_paid_second_normal",a.normal_generator)
    m=module_at("r150_paid_first",a.generator)
    binding,binding_inputs=checkpoint_binding(a)
    result["parameters"]["checkpointBinding"]=binding
    result["parameters"]["checkpointInputBytes"]=binding_inputs
    result["parameters"]["checkpointTemporaryOnly"]=True
    first=n.read_paid_first(a.first_connection_receipt)
    pure=n.read_paid_pure(a.second_pure_receipt)
    second=result_at(a.second_normal_receipt)
    third=result_at(a.third_receipt)
    require(third.get("scriptSHA256")=="eaad9fbcecd3035965de02c9e20e2c4a2372641f3bf6a97a0b99422887bf7d93"
            and field(third,"thirdConnectionEnvelopeRank")==1
            and field(third,"all1088ThirdLeftJetCorrectionRowsVerified")
            and field(third,"all6188OriginalSourcesRetainedInProof"),
            "Paid complete third envelope missing or changed")
    third_paid=third["parameters"]
    cubic=result_at(a.cubic_receipt)
    require(cubic.get("scriptSHA256")=="2fa2c0c158327c9b2a2bfdc8962bed1b67a94bc5d8bd866d1fdde65ec9bd0082"
            and field(cubic,"thirdConnectionEnvelopeRank")==1
            and field(cubic,"all6188OriginalSourcesRetainedInProof"),
            "Paid single-cubic trial missing or changed")
    cubic_paid=cubic["parameters"]
    require(field(second,"fullSecondConnectionRankUpperBound")==0
            and field(second,"all1088ExactSecondLeftJetCorrectionRowsVerified")
            and field(second,"all6188OriginalSourcesRetainedInProof"),
            "Paid complete second connection was not zero")
    second_hashes=second["parameters"]
    pure_hashes=field(pure,"matrixSHA256")

    P,cols,pure_rows,linear,quad0,seed2,physical=n.build_original_coefficients(m)
    P0,P1,P2=P
    Q,r0,pivcols,_=m.nullspace(P0)
    U,rt,pivrows,_=m.nullspace(P0.transpose())
    C=U.transpose()*P1*Q
    V,rc,_,_=m.nullspace(C)
    require(r0==rt==128 and rc==4 and V.ncols()==3,"Paid first-page dimensions")
    for key,M in (("P0",P0),("P1",P1),("Q",Q),("leftKernel",U),
                  ("connecting",C),("annihilators",V)):
        require(m.matrix_hash(M)==first["matrixSha256"][key],
                "Paid first matrix hash mismatch: "+key)
    for key in ("J2","J3","L_y0","L_y1","L_y2"):
        require(physical[key]==second_hashes["originalJetSHA256"][key],
                "Paid second physical coefficient mismatch: "+key)
    require(m.matrix_hash(P2)==second_hashes["originalJetSHA256"]["P2"],
            "Paid P2 matrix changed")
    q0=Q*V
    target=P1*q0
    W=m.fmpq_mat(135,3)
    small=m.submatrix(P0,pivrows,pivcols).solve(
        m.submatrix(target,pivrows,range(3)))
    for i,p in enumerate(pivcols):
        for j in range(3):
            W[p,j]=small[i,j]
    require(P0*W==target,"All170 first corrections failed")
    require(m.matrix_hash(W)==first["matrixSha256"]["originalCorrection"],
            "Paid first correction section changed")

    pairs=[(j,k) for j in range(2,11) for k in range(j,11)]
    two_cols=[(a,degree-a,j,k) for degree in range(4)
              for a in range(degree+1) for j,k in pairs]
    one_rows=[(i,a,degree-a,j) for i in range(17) for degree in range(3)
              for a in range(degree+1) for j in range(2,11)]
    one_index={t:j for j,t in enumerate(cols)}
    two_index={t:135+j for j,t in enumerate(two_cols)}
    J0=make_J(m,0,P0,linear,quad0,pure_rows,one_rows,two_index,pairs)
    J1=m.fmpq_mat(1088,7)
    P1Q=P1*Q
    for i in range(170):
        for j in range(7):
            J1[i,j]=P1Q[i,j]
    R2=m.fmpq_mat(1088,3)
    rp=P2*q0-P1*W
    for i in range(170):
        for j in range(3):
            R2[i,j]=rp[i,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        for j in range(3):
            R2[170+rr,j]=seed2[i]*q0[one_index[(aa,bb+2,l)],j]
    base=m.join_columns(J0,J1)
    M2=m.join_columns(base,R2)
    require(m.matrix_hash(M2)==second_hashes["augmentedMatrixSHA256"],
            "Paid full second augmented matrix changed")
    Ncert,r2,piv2,free2=extract_final_kernel(m,M2,592,582,582)
    require(free2==[592,593,594],"Paid second leading identity changed")
    require(sum(c<585 for c in piv2)==578,"Paid A0 correction rank changed")
    require(m.matrix_hash(Ncert)==second_hashes["completeCorrectionSHA256"],
            "Paid complete second correction section changed")
    Hnormal=m.submatrix(Ncert,range(585),range(3))
    Bnormal=m.submatrix(Ncert,range(585,592),range(3))
    del M2,Ncert

    pure_cols=[(aa,degree-aa+2) for degree in range(4) for aa in range(degree+1)]
    pure_index={t:j for j,t in enumerate(pure_cols)}
    S2=m.fmpq_mat(170,10)
    for rr,(i,aa,bb) in enumerate(pure_rows):
        S2[rr,pure_index[(aa,bb+2)]]=seed2[i]
    require(m.matrix_hash(S2)==pure_hashes["S"],"Paid pure second seed matrix changed")
    small_aug=m.join_columns(P0,P1Q)
    _,rsmall,acols,_=m.nullspace(small_aug)
    _,rsmallT,arows,_=m.nullspace(small_aug.transpose())
    require(rsmall==rsmallT==132,"Paid pure second correction rank changed")
    Pcert=m.fmpq_mat(142,10)
    unit=m.submatrix(small_aug,arows,acols)
    sol=unit.solve(m.submatrix(S2,arows,range(10)))
    for i,col in enumerate(acols):
        for j in range(10):
            Pcert[col,j]=sol[i,j]
    require(small_aug*Pcert==S2,"All1700 pure second corrections failed")
    require(m.matrix_hash(Pcert)==pure_hashes["completeOriginalCorrection"],
            "Paid pure second correction section changed")
    Wpure=m.submatrix(Pcert,range(135),range(10))
    Bpure=m.submatrix(Pcert,range(135,142),range(10))

    lam1=m.join_columns(-Q*Bpure,-W+Q*Bnormal)
    lam2=m.fmpq_mat(585,13)
    for i in range(135):
        for j in range(10):
            lam2[i,j]=-Wpure[i,j]
    for i in range(585):
        for j in range(3):
            lam2[i,10+j]=Hnormal[i,j]
    require(lam1.ncols()==13,"All13 fixed left2 jets retained")
    result["parameters"].update({
        "allPaidFirstHashesVerified":True,
        "allPaidSecondHashesVerified":True,
        "all1700PureSecondCorrectionRowsVerified":True,
        "all1088NormalSecondCorrectionRowsVerified":True,
        "paidSecondNormalCanonicalSectionRetained":True,
        "paidSecondPureCanonicalSectionRetained":True,
        "fixedLeft2FirstCoefficientSHA256":m.matrix_hash(lam1),
        "fixedLeft2SecondCoefficientSHA256":m.matrix_hash(lam2),
    })

    P3,quad1,seed3,third_hashes=third_coefficients(m,second_hashes["originalJetSHA256"])
    A1low=make_J(m,1,P1,linear,quad1,pure_rows,one_rows,two_index,pairs)
    R3=m.fmpq_mat(1088,13)
    np3=P3*q0
    for row,(i,aa,bb) in enumerate(pure_rows):
        R3[row,pure_index[(aa,bb+2)]]=seed3[i]
        for j in range(3):
            R3[row,10+j]=np3[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        row=170+rr
        target=one_index[(aa,bb+2,l)]
        for j in range(3):
            R3[row,10+j]=seed3[i]*q0[target,j]
    # A2.T lambda1, including its true pure F2 term on one-normal sources.
    term=P2*lam1
    for row in range(170):
        for j in range(13):
            R3[row,j]+=term[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        target=one_index[(aa,bb+2,l)]
        for j in range(13):
            R3[170+rr,j]+=seed2[i]*lam1[target,j]
    # A1.T lambda2 keeps all second-normal output coordinates.
    R3+=A1low*lam2
    oldM3=m.join_columns(base,R3)
    require(m.matrix_hash(oldM3)==third_paid["thirdAugmentedMatrixSHA256"],
            "Paid complete third augmented matrix changed")
    for key,M in (("A1TransposeLowNormalSHA256",A1low),
                  ("all13ThirdResidualColumnsSHA256",R3),
                  ("fixedLeft2FirstCoefficientSHA256",lam1),
                  ("fixedLeft2SecondCoefficientSHA256",lam2)):
        require(m.matrix_hash(M)==third_paid[key],"Paid third section changed: "+key)
    for key,value in third_hashes.items():
        require(value==third_paid["originalThirdJetSHA256"][key],
                "Paid third physical coefficient changed: "+key)
    del oldM3

    triples=[(i,j,k) for i in range(2,11)
             for j in range(i,11) for k in range(j,11)]
    three_cols=[(aa,degree-aa,i,j,k) for degree in range(3)
                for aa in range(degree+1) for i,j,k in triples]
    high_rows=[(i,aa,degree-aa,j,k) for i in range(17)
               for degree in range(2) for aa in range(degree+1)
               for j,k in pairs]
    three_index={t:j for j,t in enumerate(three_cols)}
    require(len(three_cols)==990 and len(high_rows)==2295,
            "Complete cubic-normal source/target counts changed")
    paid_high=load_phase(m,a,binding,"high-kernel",result)
    if paid_high is None:
        High=m.fmpq_mat(2295,990)
        for rr,(i,aa,bb,j,k) in enumerate(high_rows):
            for l in range(2,11):
                tr=tuple(sorted((j,k,l)))
                for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                    cc=three_index[(aa+da,bb+db)+tr]
                    High[rr,cc]+=linear[l][mode][0][i]
        high_hash=m.matrix_hash(High)
        N,rhigh,hpiv,hfree=m.nullspace(High)
        require(N.nrows()==990 and N.ncols()==990-rhigh,
                "Complete high-source kernel dimension failed")
        # The paid helper verified every one of the2295 rows, not a row subset.
        high_meta={
            "matrixSHA256":high_hash,"rank":rhigh,"freeIndices":hfree,
            "all2295HighSourceKernelRowsVerified":True,
            "allFreeCoordinateIdentitiesVerified":True,
        }
        del High
        save_phase(m,a,binding,"high-kernel",N,high_meta,result)
    else:
        N,high_meta=paid_high
        rhigh=high_meta["rank"];hfree=high_meta["freeIndices"]
        high_hash=high_meta["matrixSHA256"]
        require(high_meta["all2295HighSourceKernelRowsVerified"]
                and high_meta["allFreeCoordinateIdentitiesVerified"]
                and N.nrows()==990 and N.ncols()==990-rhigh
                and len(hfree)==N.ncols(),
                "Saved full high-source kernel identity metadata")
    n_high=N.ncols()
    require(n_high>0,"Paid cubic direction disappeared from high-source kernel")
    v={j:Q[one_index[(0,0,j)],0] for j in range(2,11)}
    require([str(v[j]) for j in range(2,11)]==
            cubic_paid["cubicNormalEvaluationVector"],
            "Paid fixed cubic evaluation vector changed")
    require(all(sum((linear[j][0][0][i]*v[j] for j in range(2,11)),m.ZERO)==0
                for i in range(17)),"All17 paid linear identities at v failed")
    cube=m.fmpq_mat(990,1)
    for j,k,l in triples:
        cube[three_index[(0,0,j,k,l)],0]=v[j]*v[k]*v[l]
    cubecoords=m.submatrix(cube,hfree,[0])
    require(N*cubecoords==cube,"Paid cubic direction not recovered in full kernel")
    result["parameters"].update({
        "completeCubicTargetCount":990,"completeHighSourceRowCount":2295,
        "highSourceMatrixSHA256":high_hash,
        "highSourceRank":rhigh,"highSourceKernelDimension":n_high,
        "highSourceKernelSHA256":m.matrix_hash(N),
        "highSourceKernelFreeIndices":hfree,
        "all2295HighSourceKernelRowsVerified":True,
        "allHighKernelFreeCoordinateIdentitiesVerified":True,
        "paidCubicColumnRecoveredInFullHighKernel":True,
    })
    reserve_for_next_step(a,"low1088 image construction")

    paid_low=load_phase(m,a,binding,"low-image",result)
    if paid_low is None:
        Low=m.fmpq_mat(1088,990)
        # Pure sources cannot reach a cubic-normal target through quadratic F0.
        for rr,(i,aa,bb,l) in enumerate(one_rows):
            for j,k in pairs:
                tr=tuple(sorted((j,k,l)))
                cc=three_index[(aa,bb)+tr]
                Low[170+rr,cc]+=quad0[(j,k)][i]
        require(m.matrix_hash(Low*cube)==
                cubic_paid["cubicNormalOriginalCorrectionColumnSHA256"],
                "Complete construction did not reproduce paid cubic low column")
        Added=Low*N
        low_hash=m.matrix_hash(Low)
        del Low
        low_meta={
            "matrixSHA256":low_hash,"highSourceKernelSHA256":m.matrix_hash(N),
            "fullLowActionAppliedToAllHighKernelColumns":True,
            "paidSingleCubicLowColumnVerified":True,
        }
        save_phase(m,a,binding,"low-image",Added,low_meta,result)
    else:
        Added,low_meta=paid_low
        low_hash=low_meta["matrixSHA256"]
        require(low_meta["highSourceKernelSHA256"]==m.matrix_hash(N)
                and low_meta["fullLowActionAppliedToAllHighKernelColumns"]
                and low_meta["paidSingleCubicLowColumnVerified"]
                and Added.nrows()==1088 and Added.ncols()==n_high,
                "Saved full low action has incompatible high-source basis")
    require(m.matrix_hash(Added*cubecoords)==
            cubic_paid["cubicNormalOriginalCorrectionColumnSHA256"],
            "Saved or fresh low image lost the paid cubic column")
    del cube,cubecoords
    reserve_for_next_step(a,"final low1088 correction RREF")
    extendedA0=m.join_columns(J0,Added)
    extendedBase=m.join_columns(extendedA0,J1)
    M3=m.join_columns(extendedBase,R3)
    start=592+n_high
    require(M3.nrows()==1088 and M3.ncols()==start+13,
            "Extended low third matrix dimensions")
    result["parameters"].update({
        "allPaidThirdHashesVerified":True,
        "allPaidSingleCubicTrialBindingsVerified":True,
        "originalThirdJetSHA256":third_hashes,
        "all17PureThirdCoefficientsVerified":True,
        "pureThirdSeedEquationOrder":seed3,
        "A1TransposeLowNormalSHA256":m.matrix_hash(A1low),
        "all13ThirdResidualColumnsSHA256":m.matrix_hash(R3),
        "completeCubicLowActionSHA256":low_hash,
        "legalCubicKernelLowImageSHA256":m.matrix_hash(Added),
        "lowThirdMatrixShape":[1088,start+13],
        "thirdAugmentedMatrixSHA256":m.matrix_hash(M3),
    })

    reduced,rank=M3.rref()
    piv=m.pivot_columns(reduced,rank)
    a0rank=sum(c<585+n_high for c in piv)
    baserank=sum(c<start for c in piv)
    require(579<=a0rank<=578+n_high and 583<=baserank<=582+n_high,
            "Complete cubic enlargement did not retain paid one-column trial")
    free=[c for c in range(start,start+13) if c not in set(piv)]
    cert=m.fmpq_mat(start+13,len(free))
    for j,c in enumerate(free):
        cert[c,j]=1
        for i,p in enumerate(piv):
            cert[p,j]=-reduced[i,c]
    require(m.matrix_zero(M3*cert),"All1088 extended low third corrections failed")
    k=rank-baserank
    require(0<=k<=1 and len(free)==13-k,"Paid third upper bound was not preserved")
    leading=m.submatrix(cert,range(start,start+13),range(len(free)))
    for j,c in enumerate(free):
        for l,d in enumerate(free):
            require(leading[d-start,j]==(1 if j==l else 0),
                    "Third leading annihilator independence failed")
    cubic_coeff=N*m.submatrix(cert,range(585,585+n_high),range(len(free)))
    result["parameters"]["actualCubicNormalThirdCorrectionSHA256"]=m.matrix_hash(cubic_coeff)
    result["parameters"]["all2295HighRowsZeroForActualThirdCorrection"]=True
    result["parameters"]["highRowsVerifiedByCompleteKernelTimesActualCoefficients"]=True
    third_upper=k
    dmax=44-k
    dsub=40-k
    result.update({
        "status":"completed",
        "thirdConnectionEnvelopeRank":k,
        "fullThirdConnectionRankUpperBound":third_upper,
        "fullInfinityMaximalMinorOrderLowerBound":dmax,
        "fullInfinitySubmaximalMinorOrderLowerBound":dsub,
    })
    result["parameters"].update({
        "A0TransposeExtendedRank":a0rank,
        "baseRank":baserank,"augmentedRank":rank,
        "thirdConnectionEnvelopeRank":k,
        "fullThirdConnectionRankUpperBound":third_upper,
        "fullInfinityMaximalMinorOrderLowerBound":dmax,
        "fullInfinitySubmaximalMinorOrderLowerBound":dsub,
        "leadingAnnihilatorsInPaidThirteenBasis":
            [[str(leading[i,j]) for i in range(13)] for j in range(len(free))],
        "leadingFreeIndices":[c-start for c in free],
        "all1088ThirdLeftJetCorrectionRowsVerified":True,
        "all2805ThreeNormalSourceRowsZeroByNormalDegree":True,
        "all3383NonautomaticSourceRowsVerified":True,
        "all6188OriginalSourcesRetainedInProof":True,
        "tenOtherPureLeftFunctionalsExactForAllParameters":True,
        "completeThirdCorrectionSHA256":m.matrix_hash(cert),
        "leadingAnnihilatorSHA256":m.matrix_hash(leading),
        "notAFullThirdConnectionLowerBound":True,
        "quarticAndQuinticNormalTargetCorrectionsNotExcluded":True,
        "smallSourceRelationsAssumedToLift":False,
        "oldNormalFormsRecomputed":False,
        "largeMacaulayMatrixConstructed":False,
        "largeRecomputableDataPersisted":False,
    })

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--generator",required=True)
    p.add_argument("--normal-generator",required=True)
    p.add_argument("--first-connection-receipt",required=True)
    p.add_argument("--second-pure-receipt",required=True)
    p.add_argument("--second-normal-receipt",required=True)
    p.add_argument("--third-receipt",required=True)
    p.add_argument("--cubic-receipt",required=True)
    p.add_argument("--checkpoint-dir",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=30.0)
    a=p.parse_args()
    require(a.remaining_seconds>0,"Positive actual shared time required")
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
    started=time.monotonic()
    a._deadline=started+a.remaining_seconds
    result={
        "format":"r150-infinity-third-complete-cubic-normal-kernel-v1",
        "status":"started","arithmetic":"exact rational python-flint",
        "scriptSHA256":sha(__file__),
        "parameters":{
            "naturalParameter":"u=1/s",
            "chart":"infinity after exact reversal and co-moving moments",
            "generatorSHA256":sha(a.generator),
            "normalGeneratorSHA256":sha(a.normal_generator),
            "firstReceiptSHA256":sha(a.first_connection_receipt),
            "secondPureReceiptSHA256":sha(a.second_pure_receipt),
            "secondNormalReceiptSHA256":sha(a.second_normal_receipt),
            "paidThirdReceiptSHA256":sha(a.third_receipt),
            "paidSingleCubicReceiptSHA256":sha(a.cubic_receipt),
            "sharedSeconds":a.remaining_seconds,"memoryMiB":512,
            "checkpointDirectory":str(Path(a.checkpoint_dir)),
            "checkpointFormat":CHECKPOINT_FORMAT,
            "highSourceMatrixShape":[2295,990],
            "largestMatrixEntryCountBound":2295*990,
            "lowMatrixColumnCount":"605 + computed highSourceKernelDimension",
            "cubicTargetOrder":"degree=0..2;a=0..degree;2<=i<=j<=k<=10",
            "highSourceOrder":"eq=0..16;degree=0..1;a=0..degree;2<=j<=k<=10",
            "leadingOrder":"ten d^2*c^a*d^b pure functionals, then three paid normal jets",
            "pureOrder":"degree=0..3;a=0..degree;monomial c^a*d^(degree-a+2)",
            "sourceMultiplierTransport":
                "m_j=sum_(k<=j)binom(j,k)u^(j-k)n_k; invertible on all degree<=3 monomials",
            "targetLeftTransport":"A_new=T A_old V implies lambda_old=T^T lambda_new",
        },
    }
    def alarm(signum,frame):
        raise TimeoutError("Shared original third-jet budget exhausted")
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(a,result)
    except BaseException as exc:
        result["status"]="incomplete"
        result["error"]=type(exc).__name__+": "+str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        cp=checkpoint_manifest(a)
        if cp.exists():
            result["parameters"]["checkpointManifestSHA256"]=sha(cp)
            result["parameters"]["checkpointManifestBytes"]=cp.stat().st_size
            result["parameters"]["checkpointTemporaryOnly"]=True
        result["elapsedSeconds"]=time.monotonic()-started
        path=Path(a.out);path.parent.mkdir(parents=True,exist_ok=True)
        raw=json.dumps(result,sort_keys=True,indent=2).encode("utf-8")
        require(len(raw)<100000,"Small receipt contract exceeded")
        temp=path.with_name(path.name+".tmp");temp.write_bytes(raw);os.replace(temp,path)
        print(json.dumps({
            "status":result["status"],"receipt":str(path),
            "receiptBytes":len(raw),"receiptSHA256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"],
            "thirdConnectionEnvelopeRank":result.get("thirdConnectionEnvelopeRank"),
            "fullThirdConnectionRankUpperBound":result.get("fullThirdConnectionRankUpperBound"),
            "fullInfinityMaximalMinorOrderLowerBound":
                result.get("fullInfinityMaximalMinorOrderLowerBound"),
        }),flush=True)

if __name__=="__main__":
    main()
