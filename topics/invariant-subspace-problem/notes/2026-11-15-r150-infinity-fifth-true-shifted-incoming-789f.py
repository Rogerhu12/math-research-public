#!/usr/bin/env python3
"""R150 original natural infinity fifth jets with true shifted incoming.

Fork of the paid fifth envelope, source SHA256
0e8a04b75d85708305cbcb645da4df13348aabf3b71951cc2ff72bd05f5513ba.
Rebuild its lost temporary first-through-fourth matrices and verify every paid
canonical hash.  Preserve all13 original R3 and all12 R4 residuals with their
actual H3 source corrections.  Add them to the old nine fifth head columns.
The sole new low system is1088x628.  Its complete kernel is used to construct
actual original lambda0..lambda5, verified on all6188 source rows at every
order.  If18 independent heads are obtained, the paid same-operator field
lower bound gives exact beta5=1.  Otherwise report only the true envelope.
No Q value is inferred from the field high quotient, no full high-normal
surjectivity is assumed, and no higher incoming completeness is claimed.
Large matrices remain temporary; permanent output is the small receipt.
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

CHECKPOINT_FORMAT="r150-infinity-fifth-shifted-incoming-temporary-v1"

def checkpoint_binding(a):
    named={
        "script":sha(__file__),"firstGenerator":sha(a.generator),
        "secondGenerator":sha(a.normal_generator),
        "firstReceipt":sha(a.first_connection_receipt),
        "pureSecondReceipt":sha(a.second_pure_receipt),
        "normalSecondReceipt":sha(a.second_normal_receipt),
        "thirdReceipt":sha(a.third_receipt),"completeCubicReceipt":sha(a.complete_cubic_receipt),
        "fourthReceipt":sha(a.fourth_receipt),
        "jetActions":sha(a.jet_actions),"fieldFull32Receipt":sha(a.field_receipt),
    }
    return hashlib.sha256(json.dumps(named,sort_keys=True,separators=(",",":"))
                          .encode("ascii")).hexdigest(),named

def checkpoint_manifest(a):
    return Path(a.checkpoint_dir)/"fifth-joint-high-low-checkpoint.json"

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
    with gzip.open(temporary,"wt",encoding="utf-8",compresslevel=1) as f:
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
    coeff={}; values3={}; quad3={}
    for j in range(2,11):
        Z=moment(j); F=F3(Z); Fn=F3(neg(Z))
        values3[j]=F
        quad3[(j,j)]=[(F[i]+Fn[i])/2 for i in range(17)]
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
    for j in range(2,11):
        for k in range(j+1,11):
            F=F3(add(moment(j),moment(k)))
            quad3[(j,k)]=[F[i]-values3[j][i]-values3[k][i] for i in range(17)]
    hashes["P3"]=m.matrix_hash(P3)
    return P3,quad1,seed3,hashes,coeff,quad3

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

def fourth_coefficients(m,n,paid_hashes):
    K=m.fmpq_mat([[m.ORIGINAL_K[5-i][5-j] for j in range(6)] for i in range(6)])
    J2=m.polynomial_power_kernel(K,2)
    J3=m.polynomial_power_kernel(K,3)
    J3inv=J3.inv()
    require(J3inv*J3==m.fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)]),
            "Original J3 inverse failed")
    p=[[K[i,k] for i in range(6)] for k in range(5)]
    y=[[m.ONE if i==k else m.ZERO for i in range(6)] for k in range(5)]
    maps=[]
    for k in range(5):
        B=m.fmpq_mat([[p[k][i-j] if 0<=i-j<6 else m.ZERO
                       for j in range(11)] for i in range(16)])
        maps.append(J3inv*B*J2)
    hashes={"J2":m.matrix_hash(J2),"J3":m.matrix_hash(J3)}
    for k in range(5):
        hashes["L_y"+str(k)]=m.matrix_hash(maps[k])
    for key in ("J2","J3","L_y0","L_y1","L_y2","L_y3"):
        require(hashes[key]==paid_hashes[key],"Paid physical map changed: "+key)

    def moment(j):
        return [m.sequence(j+k,comb(j+k,k)) for k in range(5)]
    def add(A,B):
        return [m.add_vectors(A[k],B[k]) for k in range(5)]
    def neg(A):
        return [m.scale_vector(A[k],-1) for k in range(5)]
    def lp(t,v):
        return m.fmpq_mat([[sum((t[i+j+k]*v[k] for k in range(6)),m.ZERO)
                             for j in range(6)] for i in range(6)])
    def contract(t,Q):
        return [sum((t[i+j+k]*Q[j,k] for j in range(6) for k in range(6)),m.ZERO)
                for i in range(6)]

    def F4(jets):
        M=[m.hankel(v) for v in jets]
        KM=[K*X for X in M]
        KMK=[X*K for X in KM]
        tensors=[]; quadratic=[]; tau=[]
        for k in range(5):
            l=m.fmpq_mat(16,1)
            Q=m.fmpq_mat(6,6)
            for r in range(k+1):
                l+=maps[r]*m.column(jets[k-r])
                Q+=M[r]*K*M[k-r]
            tensors.append(m.values(l))
            quadratic.append(Q)
            tau.append(sum((m.trace(KM[r]*KM[k-r]) for r in range(k+1)),m.ZERO))
        N=4*quadratic[4]
        gamma=[m.ZERO]*6
        for r in range(5):
            N+=6*lp(tensors[r],p[4-r])
            gp=m.values(quadratic[r]*m.column(p[4-r]))
            gc=contract(tensors[r],KMK[4-r])
            gamma=[gamma[i]+2*tau[r]*y[4-r][i]+8*gp[i]-12*gc[i]
                   for i in range(6)]
        KNK=K*N*K
        polar=[sum((KNK[i,j] for i in range(6) for j in range(6)
                    if i+j==degree),m.ZERO) for degree in range(11)]
        return polar+gamma

    tangent=[moment(0),moment(1)]
    seed4=[0]*6+[-328,-272,-440,-80,216]+[0]*6
    for jets,d in ((tangent[0],0),(tangent[1],1),(neg(tangent[0]),0),
                   (neg(tangent[1]),-1),(add(tangent[0],tangent[1]),1)):
        require(F4(jets)==[m.fmpq(d*d*x) for x in seed4],
                "True all17 infinity pure fourth coefficient failed")
    coeff={}
    for j in range(2,11):
        Z=moment(j); F=F4(Z); Fn=F4(neg(Z))
        modes=[[(F[i]-Fn[i])/2 for i in range(17)]]
        for A in tangent:
            FA,Fs=F4(A),F4(add(A,Z))
            modes.append([Fs[i]-F[i]-FA[i] for i in range(17)])
        coeff[j]=modes
    cols=[(a,degree-a,j) for degree in range(5)
          for a in range(degree+1) for j in range(2,11)]
    rows=[(i,a,degree-a) for i in range(17) for degree in range(4)
          for a in range(degree+1)]
    require(len(rows)==170 and len(cols)==135,"Original degree3 source range")
    idx={t:j for j,t in enumerate(cols)}
    P4=m.fmpq_mat(170,135)
    for rr,(i,a,b) in enumerate(rows):
        for j in range(2,11):
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                P4[rr,idx[(a+da,b+db,j)]]+=coeff[j][mode][i]

    # The complete original u^2 quadratic-normal coefficient is also needed.
    second_eval,second_hashes=n.build_second_evaluator(m,K)
    for key,value in second_hashes.items():
        require(value==paid_hashes[key],"Paid second physical evaluator changed")
    def moment2(j):
        return [m.sequence(j+k,comb(j+k,k)) for k in range(3)]
    def plus2(A,B):
        return [m.add_vectors(A[k],B[k]) for k in range(3)]
    def minus2(A):
        return [m.scale_vector(A[k],-1) for k in range(3)]
    values2={}
    quad2={}
    for j in range(2,11):
        Z=moment2(j)
        F=second_eval(Z);Fn=second_eval(minus2(Z))
        values2[j]=F[2]
        quad2[(j,j)]=[(F[2][i]+Fn[2][i])/2 for i in range(17)]
    for j in range(2,11):
        for k in range(j+1,11):
            F=second_eval(plus2(moment2(j),moment2(k)))[2]
            quad2[(j,k)]=[F[i]-values2[j][i]-values2[k][i] for i in range(17)]
    hashes["P4"]=m.matrix_hash(P4)
    return P4,quad2,seed4,hashes

def fifth_coefficients(m,paid_hashes):
    K=m.fmpq_mat([[m.ORIGINAL_K[5-i][5-j] for j in range(6)] for i in range(6)])
    J2=m.polynomial_power_kernel(K,2)
    J3=m.polynomial_power_kernel(K,3)
    J3inv=J3.inv()
    require(J3inv*J3==m.fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)]),
            "Original J3 inverse failed")
    p=[[K[i,k] for i in range(6)] for k in range(6)]
    y=[[m.ONE if i==k else m.ZERO for i in range(6)] for k in range(6)]
    maps=[]
    for k in range(6):
        B=m.fmpq_mat([[p[k][i-j] if 0<=i-j<6 else m.ZERO
                       for j in range(11)] for i in range(16)])
        maps.append(J3inv*B*J2)
    hashes={"J2":m.matrix_hash(J2),"J3":m.matrix_hash(J3)}
    for k in range(6):
        hashes["L_y"+str(k)]=m.matrix_hash(maps[k])
    for key in ("J2","J3","L_y0","L_y1","L_y2","L_y3","L_y4"):
        require(hashes[key]==paid_hashes[key],"Paid physical map changed: "+key)

    def moment(j):
        return [m.sequence(j+k,comb(j+k,k)) for k in range(6)]
    def add(A,B):
        return [m.add_vectors(A[k],B[k]) for k in range(6)]
    def neg(A):
        return [m.scale_vector(A[k],-1) for k in range(6)]
    def lp(t,v):
        return m.fmpq_mat([[sum((t[i+j+k]*v[k] for k in range(6)),m.ZERO)
                             for j in range(6)] for i in range(6)])
    def contract(t,Q):
        return [sum((t[i+j+k]*Q[j,k] for j in range(6) for k in range(6)),m.ZERO)
                for i in range(6)]
    def F5(jets):
        M=[m.hankel(v) for v in jets]
        KM=[K*X for X in M]
        KMK=[X*K for X in KM]
        tensors=[]; quadratic=[]; tau=[]
        for k in range(6):
            l=m.fmpq_mat(16,1); Q=m.fmpq_mat(6,6)
            for r in range(k+1):
                l+=maps[r]*m.column(jets[k-r])
                Q+=M[r]*K*M[k-r]
            tensors.append(m.values(l)); quadratic.append(Q)
            tau.append(sum((m.trace(KM[r]*KM[k-r]) for r in range(k+1)),m.ZERO))
        N=4*quadratic[5]; gamma=[m.ZERO]*6
        for r in range(6):
            N+=6*lp(tensors[r],p[5-r])
            gp=m.values(quadratic[r]*m.column(p[5-r]))
            gc=contract(tensors[r],KMK[5-r])
            gamma=[gamma[i]+2*tau[r]*y[5-r][i]+8*gp[i]-12*gc[i]
                   for i in range(6)]
        KNK=K*N*K
        polar=[sum((KNK[i,j] for i in range(6) for j in range(6)
                    if i+j==degree),m.ZERO) for degree in range(11)]
        return polar+gamma
    tangent=[moment(0),moment(1)]
    seed5=[0]*5+[720,-336,992,-2880,-3008,-1760]+[0]*6
    direct=[m.ZERO]*11
    for order,g in ((2,-2),(3,-8),(4,24)):
        for a0 in range(6-order):
            b0=5-order-a0
            for i in range(6):
                for j in range(6):
                    direct[i+j]+=4*g*p[a0][i]*p[b0][j]
    require(direct==[m.fmpq(x) for x in seed5[:11]],
            "Independent fifth pure geometric convolution failed")
    for jets,d in ((tangent[0],0),(tangent[1],1),(neg(tangent[0]),0),
                   (neg(tangent[1]),-1),(add(tangent[0],tangent[1]),1)):
        require(F5(jets)==[m.fmpq(d*d*x) for x in seed5],
                "All17 original infinity pure fifth coefficients failed")
    coeff={}
    for j in range(2,11):
        Z=moment(j); F=F5(Z); Fn=F5(neg(Z))
        modes=[[(F[i]-Fn[i])/2 for i in range(17)]]
        for A in tangent:
            FA,Fs=F5(A),F5(add(A,Z))
            modes.append([Fs[i]-F[i]-FA[i] for i in range(17)])
        coeff[j]=modes
    cols=[(a,degree-a,j) for degree in range(5)
          for a in range(degree+1) for j in range(2,11)]
    rows=[(i,a,degree-a) for i in range(17) for degree in range(4)
          for a in range(degree+1)]
    require(len(rows)==170 and len(cols)==135,"Original degree3 source range")
    idx={t:j for j,t in enumerate(cols)}
    P5=m.fmpq_mat(170,135)
    for rr,(i,a,b) in enumerate(rows):
        for j in range(2,11):
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                P5[rr,idx[(a+da,b+db,j)]]+=coeff[j][mode][i]
    hashes["P5"]=m.matrix_hash(P5)
    return P5,seed5,hashes

def make_high_action(m,linear,order,high_rows,three_index):
    M=m.fmpq_mat(2295,990)
    for rr,(i,aa,bb,j,k) in enumerate(high_rows):
        for l in range(2,11):
            tr=tuple(sorted((j,k,l)))
            for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                M[rr,three_index[(aa+da,bb+db)+tr]]+=linear[l][mode][order][i]
    return M

def make_cubic_low_action(m,quad,one_rows,pairs,three_index):
    M=m.fmpq_mat(1088,990)
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        for j,k in pairs:
            M[170+rr,three_index[(aa,bb)+tuple(sorted((j,k,l)))]]+=quad[(j,k)][i]
    return M


def run(a,result):
    check_new_inputs(a)
    require(sha(a.generator)==FIRST_SHA256,"Paid first generator SHA mismatch")
    require(sha(a.normal_generator)==SECOND_SHA256,"Paid second generator SHA mismatch")
    n=module_at("r150_paid_second_normal",a.normal_generator)
    m=module_at("r150_paid_first",a.generator)
    binding,binding_inputs=checkpoint_binding(a)
    result["parameters"]["checkpointBinding"]=binding
    result["parameters"]["checkpointInputBytes"]=binding_inputs
    first=n.read_paid_first(a.first_connection_receipt)
    pure=n.read_paid_pure(a.second_pure_receipt)
    second=result_at(a.second_normal_receipt)
    third=result_at(a.third_receipt)
    complete=result_at(a.complete_cubic_receipt)
    fourth=result_at(a.fourth_receipt)
    require(fourth.get("scriptSHA256")=="3f9b473fe0a015f11586637348ab234fd800fe0910246f43c01f5a4d5127af1d"
            and field(fourth,"independentFourthLeadingCount")==9
            and field(fourth,"all6188OriginalSourcesRetainedInProof"),
            "Paid original fourth canonical section missing")
    fourth_paid=fourth["parameters"]
    require(third.get("scriptSHA256")=="eaad9fbcecd3035965de02c9e20e2c4a2372641f3bf6a97a0b99422887bf7d93"
            and field(third,"thirdConnectionEnvelopeRank")==1
            and field(third,"all6188OriginalSourcesRetainedInProof"),
            "Paid original third canonical section missing")
    require(complete.get("scriptSHA256")=="42f91004ab4cbd248e7856902bb190ebf3a80fcb43cfe20a7bec27232c49791c"
            and field(complete,"highSourceRank")==988
            and field(complete,"highSourceKernelDimension")==2
            and field(complete,"all3383NonautomaticSourceRowsVerified"),
            "Paid complete cubic high-source operator missing")
    third_paid=third["parameters"];complete_paid=complete["parameters"]
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

    P3,quad1,seed3,third_hashes,linear3,quad3=third_coefficients(m,second_hashes["originalJetSHA256"])
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
            "Paid original third augmented matrix changed")
    for key,M in (("A1TransposeLowNormalSHA256",A1low),
                  ("all13ThirdResidualColumnsSHA256",R3),
                  ("fixedLeft2FirstCoefficientSHA256",lam1),
                  ("fixedLeft2SecondCoefficientSHA256",lam2)):
        require(m.matrix_hash(M)==third_paid[key],"Paid third section changed: "+key)
    for key,value in third_hashes.items():
        require(value==third_paid["originalThirdJetSHA256"][key],
                "Paid third physical coefficient changed: "+key)
    cert3,rank3,piv3,free3=extract_final_kernel(m,oldM3,592,582,583)
    require(free3==list(range(592,604))
            and m.matrix_hash(cert3)==third_paid["completeThirdCorrectionSHA256"],
            "Paid original third full canonical correction changed")
    Z3=m.submatrix(cert3,range(592,605),range(12))
    f1=lam1*Z3
    f2=lam2*Z3
    add2=Q*m.submatrix(cert3,range(585,592),range(12))
    for i in range(135):
        for j in range(12):
            f2[i,j]+=add2[i,j]
    f3=m.submatrix(cert3,range(585),range(12))
    require(m.matrix_zero(oldM3*cert3),"Paid all1088 third rows failed")
    result["parameters"].update({
        "allPaidThirdCanonicalHashesVerified":True,
        "originalThirdLeadingCount":12,
        "fixedThirdFirstCoefficientSHA256":m.matrix_hash(f1),
        "fixedThirdSecondCoefficientSHA256":m.matrix_hash(f2),
        "fixedThirdThirdCoefficientSHA256":m.matrix_hash(f3),
        "fixedThirdLeadingSHA256":m.matrix_hash(Z3),
    })
    incoming={"R3":R3,"lam1":lam1,"lam2":lam2}
    del oldM3,cert3,add2

    P4,quad2,seed4,fourth_hashes=fourth_coefficients(
        m,n,third_paid["originalThirdJetSHA256"])
    A2low=make_J(m,2,P2,linear,quad2,pure_rows,one_rows,two_index,pairs)
    # make_J's A0/A1 formula has no pure coefficient; A2 has a real pure seed.
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        A2low[170+rr,one_index[(aa,bb+2,l)]]+=seed2[i]
    from0=m.fmpq_mat(1088,13)
    p4q=P4*q0
    for row,(i,aa,bb) in enumerate(pure_rows):
        from0[row,pure_index[(aa,bb+2)]]=seed4[i]
        for j in range(3):
            from0[row,10+j]=p4q[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        target=one_index[(aa,bb+2,l)]
        for j in range(3):
            from0[170+rr,10+j]=seed4[i]*q0[target,j]
    Rlow=from0*Z3+A2low*f2+A1low*f3
    term=P3*f1
    for row in range(170):
        for j in range(12):
            Rlow[row,j]+=term[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        target=one_index[(aa,bb+2,l)]
        for j in range(12):
            Rlow[170+rr,j]+=seed3[i]*f1[target,j]
    del from0,A2low,term

    triples=[(i,j,k) for i in range(2,11)
             for j in range(i,11) for k in range(j,11)]
    three_cols=[(aa,degree-aa,i,j,k) for degree in range(3)
                for aa in range(degree+1) for i,j,k in triples]
    high_rows=[(i,aa,degree-aa,j,k) for i in range(17)
               for degree in range(2) for aa in range(degree+1)
               for j,k in pairs]
    three_index={t:j for j,t in enumerate(three_cols)}
    Rhigh=m.fmpq_mat(2295,12)
    for rr,(i,aa,bb,j,k) in enumerate(high_rows):
        target=two_index[(aa,bb+2,j,k)]
        for col in range(12):
            Rhigh[rr,col]=seed2[i]*f2[target,col]
    high_residual_hash=m.matrix_hash(Rhigh)
    low_residual_hash=m.matrix_hash(Rlow)
    result["parameters"].update({
        "originalFourthJetSHA256":fourth_hashes,
        "pureFourthSeedEquationOrder":seed4,
        "all17PureFourthCoefficientsVerified":True,
        "fourthLowResidualSHA256":low_residual_hash,
        "fourthHighResidualSHA256":high_residual_hash,
        "realA2PureTimesSecondNormalCoefficientRetained":True,
        "all3383FourthResidualSourceRowsRetained":True,
        "all2805ThreeNormalResidualRowsZeroByNormalDegree":True,
    })

    paid_high=load_phase(m,a,binding,"high-fourth-lifts",result)
    if paid_high is None:
        High=m.fmpq_mat(2295,990)
        for rr,(i,aa,bb,j,k) in enumerate(high_rows):
            for l in range(2,11):
                tr=tuple(sorted((j,k,l)))
                for mode,(da,db) in enumerate(((0,0),(1,0),(0,1))):
                    cc=three_index[(aa+da,bb+db)+tr]
                    High[rr,cc]+=linear[l][mode][0][i]
        require(m.matrix_hash(High)==complete_paid["highSourceMatrixSHA256"],
                "Paid complete H3 high operator changed")
        HighAug=m.join_columns(High,Rhigh)
        reduced,highrank=HighAug.rref()
        hpiv=m.pivot_columns(reduced,highrank)
        require(sum(c<990 for c in hpiv)==988,"Paid H3 rank changed")
        hfree=[c for c in range(1002) if c not in set(hpiv)]
        require([c for c in hfree if c<990]==[164,494],
                "Paid H3 free coordinates changed")
        Tall=m.fmpq_mat(1002,len(hfree))
        for j,c in enumerate(hfree):
            Tall[c,j]=1
            for i,p in enumerate(hpiv):
                Tall[p,j]=-reduced[i,c]
        require(m.matrix_zero(HighAug*Tall),
                "All2295 complete high fourth-lift rows failed")
        N=m.submatrix(Tall,range(990),[0,1])
        require(m.matrix_hash(N)==complete_paid["highSourceKernelSHA256"],
                "Paid full H3 canonical kernel changed")
        high_meta={
            "augmentedMatrixSHA256":m.matrix_hash(HighAug),
            "rank":highrank,"freeIndices":hfree,
            "fourthHighResidualSHA256":high_residual_hash,
            "fourthLowResidualSHA256":low_residual_hash,
            "all2295HighFourthLiftRowsVerified":True,
            "paidHighKernelCanonicalSHA256":m.matrix_hash(N),
        }
        del High,HighAug,reduced
        save_phase(m,a,binding,"high-fourth-lifts",Tall,high_meta,result)
    else:
        Tall,high_meta=paid_high
        highrank=high_meta["rank"];hfree=high_meta["freeIndices"]
        require(Tall.nrows()==1002 and Tall.ncols()==1002-highrank
                and high_meta["fourthHighResidualSHA256"]==high_residual_hash
                and high_meta["fourthLowResidualSHA256"]==low_residual_hash
                and high_meta["all2295HighFourthLiftRowsVerified"],
                "Saved actual high lift has incompatible new residual")
        N=m.submatrix(Tall,range(990),[0,1])
        require(m.matrix_hash(N)==complete_paid["highSourceKernelSHA256"],
                "Saved high lift did not retain the paid H3 canonical kernel")
    Y=m.submatrix(Tall,range(990),range(Tall.ncols()))
    Zhigh=m.submatrix(Tall,range(990,1002),range(Tall.ncols()))
    require(m.matrix_zero(m.submatrix(Zhigh,range(12),[0,1])),
            "Paid high-kernel columns acquired false leading coordinates")
    result["parameters"].update({
        "highFourthAugmentedRank":highrank,
        "highFourthLeadingDimension":1002-highrank-2,
        "highFourthAugmentedSHA256":high_meta["augmentedMatrixSHA256"],
        "highFourthKernelSHA256":m.matrix_hash(Tall),
        "all2295HighFourthLiftRowsVerified":True,
        "allPaidCompleteCubicOperatorHashesVerified":True,
    })
    reserve_for_next_step(a,"joint low fourth columns")

    paid_low=load_phase(m,a,binding,"low-fourth-columns",result)
    if paid_low is None:
        Low=m.fmpq_mat(1088,990)
        for rr,(i,aa,bb,l) in enumerate(one_rows):
            for j,k in pairs:
                cc=three_index[(aa,bb)+tuple(sorted((j,k,l)))]
                Low[170+rr,cc]+=quad0[(j,k)][i]
        require(m.matrix_hash(Low)==complete_paid["completeCubicLowActionSHA256"],
                "Paid full K3 low action changed")
        require(m.matrix_hash(Low*N)==complete_paid["legalCubicKernelLowImageSHA256"],
                "Paid two-column legal cubic low image changed")
        Corr=Low*Y+Rlow*Zhigh
        low_meta={
            "highFourthKernelSHA256":m.matrix_hash(Tall),
            "fourthLowResidualSHA256":low_residual_hash,
            "completeK3LowActionSHA256":m.matrix_hash(Low),
            "allJointHighLiftColumnsTransported":True,
        }
        del Low
        save_phase(m,a,binding,"low-fourth-columns",Corr,low_meta,result)
    else:
        Corr,low_meta=paid_low
        require(Corr.nrows()==1088 and Corr.ncols()==Tall.ncols()
                and low_meta["highFourthKernelSHA256"]==m.matrix_hash(Tall)
                and low_meta["fourthLowResidualSHA256"]==low_residual_hash
                and low_meta["completeK3LowActionSHA256"]==
                    complete_paid["completeCubicLowActionSHA256"]
                and low_meta["allJointHighLiftColumnsTransported"],
                "Saved low joint columns have incompatible high lift")
    require(m.matrix_hash(m.submatrix(Corr,range(1088),[0,1]))==
            complete_paid["legalCubicKernelLowImageSHA256"],
            "Joint low columns lost the paid homogeneous H3 image")
    reserve_for_next_step(a,"final fourth low1088 correction RREF")

    M4=m.join_columns(base,Corr)
    reduced,lowrank=M4.rref()
    lpiv=m.pivot_columns(reduced,lowrank)
    require(sum(c<592 for c in lpiv)==582
            and sum(c<594 for c in lpiv)==584,
            "Paid low base and complete cubic prefix ranks changed")
    lfree=[c for c in range(592,M4.ncols()) if c not in set(lpiv)]
    cert=m.fmpq_mat(M4.ncols(),len(lfree))
    for j,c in enumerate(lfree):
        cert[c,j]=1
        for i,p in enumerate(lpiv):
            cert[p,j]=-reduced[i,c]
    require(m.matrix_zero(M4*cert),"All1088 joint fourth low rows failed")
    if lfree:
        all_leading=Zhigh*m.submatrix(cert,range(592,M4.ncols()),range(len(lfree)))
        lr,leading_rank=all_leading.rref()
        independent=m.pivot_columns(lr,leading_rank)
        selected=m.submatrix(cert,range(M4.ncols()),independent)
        leading=m.submatrix(all_leading,range(12),independent)
        actual_high=Y*m.submatrix(selected,range(592,M4.ncols()),range(leading_rank))
    else:
        leading_rank=0
        selected=m.fmpq_mat(M4.ncols(),0)
        leading=m.fmpq_mat(12,0)
        actual_high=m.fmpq_mat(990,0)
    require(m.matrix_zero(M4*selected),"Selected complete fourth low identity failed")
    require(0<=leading_rank<=12,"Fourth leading rank")
    sum_four=17-leading_rank
    dmax=max(43,40+leading_rank)
    dsub=max(39,35+leading_rank)
    result.update({
        "status":"completed",
        "independentFourthLeadingCount":leading_rank,
        "sumFirstFourConnectionRanksUpperBound":sum_four,
        "fullInfinityMaximalMinorOrderLowerBound":dmax,
        "fullInfinitySubmaximalMinorOrderLowerBound":dsub,
    })
    result["parameters"].update({
        "lowFourthMatrixShape":[1088,M4.ncols()],
        "lowFourthAugmentedRank":lowrank,
        "lowFourthAugmentedSHA256":m.matrix_hash(M4),
        "completeLowFourthCorrectionSHA256":m.matrix_hash(selected),
        "actualHighFourthCorrectionSHA256":m.matrix_hash(actual_high),
        "leadingAnnihilatorSHA256":m.matrix_hash(leading),
        "leadingAnnihilatorsInPaidTwelveBasis":
            [[str(leading[i,j]) for i in range(12)] for j in range(leading_rank)],
        "independentFourthLeadingCount":leading_rank,
        "sumFirstFourConnectionRanksUpperBound":sum_four,
        "fullInfinityMaximalMinorOrderLowerBound":dmax,
        "fullInfinitySubmaximalMinorOrderLowerBound":dsub,
        "all1088LowFourthCorrectionRowsVerified":True,
        "all2295HighFourthCorrectionRowsVerifiedByFullKernel":True,
        "all3383NonautomaticOriginalSourceRowsVerified":True,
        "all2805ThreeNormalSourceRowsZeroByNormalDegree":True,
        "all6188OriginalSourcesRetainedInProof":True,
        "tenOtherPureLeftFunctionalsExactForAllParameters":True,
        "fourthCorrectionAmbiguityAtThirdCoefficientRetained":True,
        "notAFullFourthConnectionLowerBound":True,
        "quarticAndQuinticNormalTargetCorrectionsNotExcluded":True,
        "oldNormalFormsRecomputed":False,
        "largeMacaulayMatrixConstructed":False,
        "largeRecomputableDataPersisted":False,
    })

    # The entire previous fourth section is fixed by actual full-matrix hashes.
    require(leading_rank==9 and lowrank==587 and highrank==988,
            "Paid fourth ranks changed")
    for key,M in (
        ("completeLowFourthCorrectionSHA256",selected),
        ("actualHighFourthCorrectionSHA256",actual_high),
        ("leadingAnnihilatorSHA256",leading),
        ("lowFourthAugmentedSHA256",M4),
        ("highFourthKernelSHA256",Tall)):
        require(m.matrix_hash(M)==fourth_paid[key],"Paid fourth canonical matrix changed: "+key)
    require(high_meta["augmentedMatrixSHA256"]==fourth_paid["highFourthAugmentedSHA256"]
            and m.matrix_hash(f1)==fourth_paid["fixedThirdFirstCoefficientSHA256"]
            and m.matrix_hash(f2)==fourth_paid["fixedThirdSecondCoefficientSHA256"]
            and m.matrix_hash(f3)==fourth_paid["fixedThirdThirdCoefficientSHA256"],
            "Paid fourth high and previous jet hashes changed")
    for key,value in fourth_hashes.items():
        require(value==fourth_paid["originalFourthJetSHA256"][key],
                "Paid fourth physical map changed: "+key)
    g0=Z3*leading
    g1=f1*leading
    g2=f2*leading
    g3=f3*leading
    B4=m.submatrix(selected,range(585,592),range(9))
    extra=Q*B4
    for i in range(135):
        for j in range(9):
            g3[i,j]+=extra[i,j]
    g4=m.submatrix(selected,range(585),range(9))
    g4high=actual_high
    result["parameters"].update({
        "allPaidFourthCanonicalHashesVerified":True,
        "fixedFourthLeadingCount":9,
        "fixedFourthLeadingInThirteenBasisSHA256":m.matrix_hash(g0),
        "fixedFourthFirstCoefficientSHA256":m.matrix_hash(g1),
        "fixedFourthSecondCoefficientSHA256":m.matrix_hash(g2),
        "fixedFourthThirdCoefficientSHA256":m.matrix_hash(g3),
        "fixedFourthFourthLowCoefficientSHA256":m.matrix_hash(g4),
        "fixedFourthFourthHighCoefficientSHA256":m.matrix_hash(g4high),
        "fifthFourthCoefficientAmbiguityIsOriginalQ":True,
    })
    incoming.update({"Z3":Z3,"f1":f1,"f2":f2,"f3":f3,
        "Y4":m.submatrix(Y,range(990),range(2,14)),
        "Z4":m.submatrix(Zhigh,range(12),range(2,14)),
        "C4":m.submatrix(Corr,range(1088),range(2,14))})
    del M4,reduced,cert,selected,leading,actual_high,Tall,Corr,N,extra,B4
    reserve_for_next_step(a,"original fifth physical coefficients")

    P5,seed5,fifth_hashes=fifth_coefficients(m,fourth_paid["originalFourthJetSHA256"])
    # Extend the actual original linear-normal coefficients through order3.
    lin3={j:[[linear[j][mode][r] for r in range(3)]+[linear3[j][mode]]
             for mode in range(3)] for j in range(2,11)}
    A3low=make_J(m,3,P3,lin3,quad3,pure_rows,one_rows,two_index,pairs)
    A2low=make_J(m,2,P2,linear,quad2,pure_rows,one_rows,two_index,pairs)
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        target=one_index[(aa,bb+2,l)]
        A3low[170+rr,target]+=seed3[i]
        A2low[170+rr,target]+=seed2[i]
    from0=m.fmpq_mat(1088,13)
    p5q=P5*q0
    for row,(i,aa,bb) in enumerate(pure_rows):
        from0[row,pure_index[(aa,bb+2)]]=seed5[i]
        for j in range(3):
            from0[row,10+j]=p5q[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        target=one_index[(aa,bb+2,l)]
        for j in range(3):
            from0[170+rr,10+j]=seed5[i]*q0[target,j]
    R5low=from0*g0+A3low*g2+A2low*g3+A1low*g4
    term=P4*g1
    for row in range(170):
        for j in range(9):
            R5low[row,j]+=term[row,j]
    for rr,(i,aa,bb,l) in enumerate(one_rows):
        target=one_index[(aa,bb+2,l)]
        for j in range(9):
            R5low[170+rr,j]+=seed4[i]*g1[target,j]
    K31=make_cubic_low_action(m,quad1,one_rows,pairs,three_index)
    R5low+=K31*g4high
    H31=make_high_action(m,linear,1,high_rows,three_index)
    R5high=H31*g4high
    for rr,(i,aa,bb,j,k) in enumerate(high_rows):
        target=two_index[(aa,bb+2,j,k)]
        for col in range(9):
            R5high[rr,col]+=seed3[i]*g2[target,col]+seed2[i]*g3[target,col]
    low5sha=m.matrix_hash(R5low);high5sha=m.matrix_hash(R5high)
    result["parameters"].update({
        "originalFifthJetSHA256":fifth_hashes,
        "pureFifthSeedEquationOrder":seed5,
        "all17PureFifthCoefficientsVerified":True,
        "independentPureFifthConvolutionVerified":True,
        "completeA3LowTransposeSHA256":m.matrix_hash(A3low),
        "completeA2LowTransposeSHA256":m.matrix_hash(A2low),
        "cubicA1LowActionSHA256":m.matrix_hash(K31),
        "cubicA1HighActionSHA256":m.matrix_hash(H31),
        "fifthLowResidualSHA256":low5sha,
        "fifthHighResidualSHA256":high5sha,
        "allThreeActualHighFifthTermsRetained":True,
        "pureA3TimesSecondNormalAndPureA2TimesThirdNormalRetained":True,
        "A1TimesActualFourthCubicCorrectionRetained":True,
        "all3383FifthResidualSourceRowsRetained":True,
        "all2805ThreeNormalFifthResidualRowsZeroByNormalDegree":True,
    })
    del from0,p5q,term,A2low,A3low,K31,H31,lin3
    reserve_for_next_step(a,"joint fifth high2295 correction")

    saved=load_phase(m,a,binding,"high-fifth-lifts",result)
    if saved is None:
        H30=make_high_action(m,linear,0,high_rows,three_index)
        require(m.matrix_hash(H30)==complete_paid["highSourceMatrixSHA256"],
                "Paid original H3 changed in fifth page")
        Aug5=m.join_columns(H30,R5high)
        rr,rh5=Aug5.rref()
        pv=m.pivot_columns(rr,rh5)
        require(sum(c<990 for c in pv)==988,"Paid H3 prefix rank changed")
        fv=[c for c in range(999) if c not in set(pv)]
        require([c for c in fv if c<990]==[164,494],"Paid H3 free coordinates changed")
        T5=m.fmpq_mat(999,len(fv))
        for j,c in enumerate(fv):
            T5[c,j]=1
            for i,p in enumerate(pv):
                T5[p,j]=-rr[i,c]
        require(m.matrix_zero(Aug5*T5),"All2295 fifth high source rows failed")
        N5=m.submatrix(T5,range(990),[0,1])
        require(m.matrix_hash(N5)==complete_paid["highSourceKernelSHA256"],
                "Fifth high kernel lost the paid homogeneous section")
        meta5={
            "augmentedMatrixSHA256":m.matrix_hash(Aug5),
            "rank":rh5,"freeIndices":fv,
            "fifthLowResidualSHA256":low5sha,"fifthHighResidualSHA256":high5sha,
            "all2295HighFifthLiftRowsVerified":True,
        }
        del H30,Aug5,rr
        save_phase(m,a,binding,"high-fifth-lifts",T5,meta5,result)
    else:
        T5,meta5=saved
        rh5=meta5["rank"];fv=meta5["freeIndices"]
        require(T5.nrows()==999 and T5.ncols()==999-rh5
                and meta5["fifthLowResidualSHA256"]==low5sha
                and meta5["fifthHighResidualSHA256"]==high5sha
                and meta5["all2295HighFifthLiftRowsVerified"],
                "Saved fifth high lifts do not match actual source")
        N5=m.submatrix(T5,range(990),[0,1])
        require(m.matrix_hash(N5)==complete_paid["highSourceKernelSHA256"],
                "Saved fifth high kernel did not retain canonical homogeneous basis")
    Y5=m.submatrix(T5,range(990),range(T5.ncols()))
    Z5=m.submatrix(T5,range(990,999),range(T5.ncols()))
    require(m.matrix_zero(m.submatrix(Z5,range(9),[0,1])),
            "Homogeneous fifth high columns acquired false leading terms")
    result["parameters"].update({
        "highFifthMatrixShape":[2295,999],
        "highFifthAugmentedRank":rh5,
        "highFifthAugmentedSHA256":meta5["augmentedMatrixSHA256"],
        "highFifthKernelSHA256":m.matrix_hash(T5),
        "highFifthLeadingDimension":999-rh5-2,
        "all2295HighFifthLiftRowsVerified":True,
    })
    reserve_for_next_step(a,"joint fifth low columns")
    saved=load_phase(m,a,binding,"low-fifth-columns",result)
    if saved is None:
        K30=make_cubic_low_action(m,quad0,one_rows,pairs,three_index)
        require(m.matrix_hash(K30)==complete_paid["completeCubicLowActionSHA256"],
                "Paid K3 low action changed in fifth page")
        require(m.matrix_hash(K30*N5)==complete_paid["legalCubicKernelLowImageSHA256"],
                "Paid homogeneous cubic low image changed")
        C5=K30*Y5+R5low*Z5
        metaC5={
            "highFifthKernelSHA256":m.matrix_hash(T5),
            "fifthLowResidualSHA256":low5sha,
            "completeK3LowActionSHA256":m.matrix_hash(K30),
            "allJointHighFifthLiftColumnsTransported":True,
        }
        del K30
        save_phase(m,a,binding,"low-fifth-columns",C5,metaC5,result)
    else:
        C5,metaC5=saved
        require(C5.nrows()==1088 and C5.ncols()==T5.ncols()
                and metaC5["highFifthKernelSHA256"]==m.matrix_hash(T5)
                and metaC5["fifthLowResidualSHA256"]==low5sha
                and metaC5["completeK3LowActionSHA256"]==complete_paid["completeCubicLowActionSHA256"]
                and metaC5["allJointHighFifthLiftColumnsTransported"],
                "Saved fifth low columns do not match high source")
    require(m.matrix_hash(m.submatrix(C5,range(1088),[0,1]))==
            complete_paid["legalCubicKernelLowImageSHA256"],
            "Fifth low columns lost homogeneous H3 image")
    reserve_for_next_step(a,"fifth final low1088 correction")
    incoming.update({"q0":q0,"Q":Q,"base":base,
        "g0":g0,"g1":g1,"g2":g2,"g3":g3,"g4":g4,"g4high":g4high,
        "Y5":Y5,"Z5":Z5,"C5":C5})
    return complete_fifth_with_incoming(a,result,m,binding,incoming)


# New bounded consumer.  All old computations above this function are rebuilt
# from the paid hashes.  This part adds the missing shifted R3/R4 incoming.
ACTIONS17_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
FIELD_FULL32_SHA="14f396c3969ea90694d06e6f26fe75299bf2e678381b491ddb6cb78b93826815"
PAID_INPUT_SHA={
 "first_connection_receipt":"03c80c0185cc7ea19a6b8aec57f3fcb905f4b6299c5bad2fdc872229bce85548",
 "second_pure_receipt":"a16ecefa8669222653aacd1a8fb7fb10c858e44d91a117b09db7a851f1da6b98",
 "second_normal_receipt":"cf9d9439fb2ca44921cb4f2614cf3400d5045783e4e9842321c0fdb3aef540da",
 "third_receipt":"8df6d0f6ec01a1fcebd9234adc963ad2e73ab3481089f2d5063d805fdfb58f45",
 "complete_cubic_receipt":"1d9420ac3d318a5058c7f47acda6942f9126cd21c5871de2b4d4618ecf60688b",
 "fourth_receipt":"df342766441ffed18a1d2dd56405ecd2885b01cd4cb7ecf5e69b2ad725e25a35",
}
def check_new_inputs(a):
    require(sha(a.jet_actions)==ACTIONS17_SHA,"Pinned original all-source actions17")
    require(sha(a.field_receipt)==FIELD_FULL32_SHA,"Paid original full32 field receipt")
    for key,want in PAID_INPUT_SHA.items():
        require(sha(getattr(a,key))==want,"Paid original prefix receipt "+key)
    fld=result_at(a.field_receipt)
    spec=field(fld,"smallSeriesSmith")
    require(fld["field"]==31 and fld["fullConstantRankModulo31"]==4340
            and fld["fullGenericRankModulo31"]==4354
            and fld["all6188OriginalJetResidualCoordinatesRetained"]
            and spec["complete"] and spec["formalKernelRank"]==13
            and spec["paidExponents"]==[1,1,1,1,3,4,4,4,5,6,7,8,10,11],
            "Actual same-natural-operator field spectrum and all source rows")
    return fld

def new_vertical(m,blocks):
    require(blocks and len({X.ncols() for X in blocks})==1,"Vertical exact columns")
    M=m.fmpq_mat(sum(X.nrows() for X in blocks),blocks[0].ncols())
    row=0
    for X in blocks:
        for i in range(X.nrows()):
            for c in range(X.ncols()):
                M[row+i,c]=X[i,c]
        row+=X.nrows()
    return M

def complete_fifth_with_incoming(a,result,m,binding,d):
    check_new_inputs(a)
    j=module_at("r150_original_infinity_fifth_actions17",a.jet_actions)
    coeff=j.original_coefficients(m,"infinity",5)
    for key,want in result["parameters"]["originalFifthJetSHA256"].items():
        require(coeff["physical"][key]==want,"Independent original coefficient hash "+key)
    require([len(j.source_rows(r)) for r in range(4)]==[170,918,2295,2805]
            and [len(j.target_columns(r)) for r in range(4)]==[20,135,450,990],
            "All actual normal-stratum dictionaries")
    one=lambda M:m.submatrix(M,range(135),range(M.ncols()))
    two=lambda M:m.submatrix(M,range(135,585),range(M.ncols()))
    I12=m.fmpq_mat([[int(i==c) for c in range(12)] for i in range(12)])
    I9=m.fmpq_mat([[int(i==c) for c in range(9)] for i in range(9)])
    require(d["Z4"]==I12 and m.submatrix(d["Z5"],range(9),range(2,11))==I9
            and m.matrix_zero(m.submatrix(d["Z5"],range(9),range(2))),
            "Actual high target coordinates are the original identities")

    h0p=m.fmpq_mat(20,13);h0n=m.fmpq_mat(135,13)
    pindex={x:i for i,x in enumerate(j.target_columns(0))}
    pure_ids=[pindex[(aa,degree-aa+2,())] for degree in range(4) for aa in range(degree+1)]
    exact_ids=[i for i,(aa,bb,mon) in enumerate(j.target_columns(0)) if bb<=1]
    require(len(pure_ids)==len(exact_ids)==10 and len(set(pure_ids+exact_ids))==20,
            "Twenty original pure coefficients")
    for c,i in enumerate(pure_ids): h0p[i,c]=1
    for i in range(135):
        for c in range(3): h0n[i,10+c]=d["q0"][i,c]
    second=[{0:h0p,1:h0n},{1:d["lam1"]},{1:one(d["lam2"]),2:two(d["lam2"])}]
    third=[{0:h0p*d["Z3"],1:h0n*d["Z3"]},{1:d["f1"]},
           {1:one(d["f2"]),2:two(d["f2"])},{1:one(d["f3"]),2:two(d["f3"])}]
    fourth=[{0:h0p*d["g0"],1:h0n*d["g0"]},{1:d["g1"]},
            {1:one(d["g2"]),2:two(d["g2"])},{1:one(d["g3"]),2:two(d["g3"])},
            {1:one(d["g4"]),2:two(d["g4"]),3:d["g4high"]}]
    cache={}
    def act(order,sr,section,nc):
        R=m.fmpq_mat(len(j.source_rows(sr)),nc)
        for td,X in section.items():
            if td<sr or td>sr+2 or m.matrix_zero(X): continue
            if td==sr and not any(coeff["pure"][order]): continue
            key=(order,sr,td)
            M=cache.get(key)
            if M is None:
                M=j.block(m,coeff,order,sr,td)
                if M.nrows()*M.ncols()<=500000: cache[key]=M
            R+=M*X
        return R
    def residual(co,order,nc):
        out=[]
        for sr in range(4):
            R=m.fmpq_mat(len(j.source_rows(sr)),nc)
            for k,sec in enumerate(co):
                if k<=order: R+=act(order-k,sr,sec,nc)
            out.append(R)
        return new_vertical(m,out)
    def verify(co,order,nc,label):
        for k in range(order+1):
            require(m.matrix_zero(residual(co,k,nc)),label+" original6188 order"+str(k))
        return (order+1)*6188*nc

    checks=verify(second,2,13,"Paid second")
    checks+=verify(third,3,12,"Paid third")
    checks+=verify(fourth,4,9,"Paid fourth")
    R3=residual(second,3,13);R4=residual(third,4,12);R5=residual(fourth,5,9)
    require(m.submatrix(R3,range(1088),range(13))==d["R3"]
            and m.matrix_zero(m.submatrix(R3,range(1088,6188),range(13))),
            "All original third incoming including every high row")
    Y4=d["Y4"];C4=d["C4"]
    require(m.submatrix(R4,range(1088),range(12))+new_vertical(m,[act(0,sr,{3:Y4},12)
            for sr in (0,1)])==C4,
            "All low fourth incoming after its actual original high lift")
    # Check the high cancellation independently; no high rank assumption.
    for sr,offset in ((2,1088),(3,3383)):
        require(m.matrix_zero(m.submatrix(R4,range(offset,offset+len(j.source_rows(sr))),range(12))
                             +act(0,sr,{3:Y4},12)),
                "All high fourth incoming cancellation sector"+str(sr))
    Y5=d["Y5"];Z5=d["Z5"]
    low5=new_vertical(m,[act(0,sr,{3:Y5},11) for sr in (0,1)]) \
         +m.submatrix(R5,range(1088),range(9))*Z5
    require(low5==d["C5"],"All actual fifth high-lift residual columns")
    for sr,offset in ((2,1088),(3,3383)):
        require(m.matrix_zero(m.submatrix(R5,range(offset,offset+len(j.source_rows(sr))),range(9))*Z5
                             +act(0,sr,{3:Y5},11)),
                "All high fifth incoming cancellation sector"+str(sr))
    M=m.join_columns(m.join_columns(m.join_columns(d["base"],d["R3"]),C4),d["C5"])
    require([M.nrows(),M.ncols()]==[1088,628],"Only1088 by628 new low system")
    prepmeta={"allOriginalIncomingResidualsVerified":True,
              "originalSecondProducts":3*6188*13,"originalThirdProducts":4*6188*12,
              "originalFourthProducts":5*6188*9,
              "ranges":{"lowCorrection":[0,585],"QFirstIncoming":[585,592],
                        "secondShiftR3":[592,605],"thirdShiftR4":[605,617],
                        "fifthHighLift":[617,628]},
              "oldFourthHighTargetIdentityVerified":True,
              "allHighIncomingRowsVerified":True}
    save_phase(m,a,binding,"complete-incoming-low-matrix",M,prepmeta,result)
    reserve_for_next_step(a,"new1088 by628 exact kernel")
    cached=load_phase(m,a,binding,"complete-incoming-low-kernel",result)
    if cached is None:
        rr,r=M.rref()
        piv=m.pivot_columns(rr,r);pset=set(piv);free=[c for c in range(628) if c not in pset]
        K=m.fmpq_mat(628,len(free))
        for c,f in enumerate(free):
            K[f,c]=1
            for i,p in enumerate(piv): K[p,c]=-rr[i,f]
        require(m.matrix_zero(M*K),"All1088 rows of complete incoming kernel")
        km={"rank":r,"pivots":piv,"freeColumns":free,
            "all1088KernelProductsVerified":True,
            "actualPrefixRanks":{"base592":sum(p<592 for p in piv),
             "throughR3":sum(p<605 for p in piv),"throughR4":sum(p<617 for p in piv),
             "allIncomingBeforeNineHeads":sum(p<619 for p in piv)}}
        save_phase(m,a,binding,"complete-incoming-low-kernel",K,km,result)
    else:
        K,km=cached
        require([K.nrows(),K.ncols()]==[628,628-km["rank"]]
                and km["all1088KernelProductsVerified"] and m.matrix_zero(M*K),
                "Complete actual low kernel checkpoint")
    leads=Z5*m.submatrix(K,range(617,628),range(K.ncols()))
    lr,h=leads.rref();ind=m.pivot_columns(lr,h)
    selected=m.submatrix(K,range(628),ind)
    z=Z5*m.submatrix(selected,range(617,628),range(h))
    require(7<=h<=8,"Actual independent fifth heads versus paid field lower bound")
    x=m.submatrix(selected,range(585),range(h))
    b=m.submatrix(selected,range(585,592),range(h))
    v3=m.submatrix(selected,range(592,605),range(h))
    v4=m.submatrix(selected,range(605,617),range(h))
    alpha5=m.submatrix(selected,range(617,628),range(h))
    # Entire lower jets are shifted.  All signs are the original augmented-
    # kernel signs; no in-coker cancellation substitutes for a true cochain.
    co=[
      {0:h0p*d["g0"]*z,1:h0n*d["g0"]*z},
      {0:h0p*d["Z3"]*v4,1:d["g1"]*z+h0n*d["Z3"]*v4},
      {0:h0p*v3,1:one(d["g2"])*z+d["f1"]*v4+h0n*v3,2:two(d["g2"])*z},
      {1:one(d["g3"])*z+one(d["f2"])*v4+d["lam1"]*v3,
       2:two(d["g3"])*z+two(d["f2"])*v4},
      {1:one(d["g4"])*z+one(d["f3"])*v4+one(d["lam2"])*v3+d["Q"]*b,
       2:two(d["g4"])*z+two(d["f3"])*v4+two(d["lam2"])*v3,
       3:d["g4high"]*z},
      {1:one(x),2:two(x),3:Y4*v4+Y5*alpha5}
    ]
    exact=m.fmpq_mat(20,10)
    for c,i in enumerate(exact_ids): exact[i,c]=1
    for k,sec in enumerate(co):
        for td,X in list(sec.items()):
            sec[td]=m.join_columns(X,exact if k==0 and td==0 else m.fmpq_mat(X.nrows(),10))
    total=h+10
    head=new_vertical(m,[co[0][0],co[0][1]])
    _,headrank=head.rref();require(headrank==total,"All original fifth heads independent")
    blocks=[];ranges={};offset=0
    for k,sec in enumerate(co):
        for td,X in sorted(sec.items()):
            key="lambda"+str(k)+"Normal"+str(td)
            ranges[key]={"start":offset,"stop":offset+X.nrows(),"matrixSHA256":m.matrix_hash(X)}
            blocks.append(X);offset+=X.nrows()
    pack=new_vertical(m,blocks)
    candidate={"order":5,"chart":"infinity","leadingColumns":total,"ranges":ranges,
               "originalLeadingRank":headrank,"fullOriginalVerificationComplete":False,
               "incomingShifts":"u^2 times all13 original left2; u times all12 original left3; u^4 Q",
               "leadingInPaidNineBasis":[[str(z[i,c]) for c in range(h)] for i in range(9)]}
    save_phase(m,a,binding,"actual-fifth-cochains-candidate",pack,candidate,result)
    reserve_for_next_step(a,"all six original coefficient identities")
    checks+=verify(co,5,total,"New fifth complete incoming")
    candidate["fullOriginalVerificationComplete"]=True
    candidate["allSixOrdersAll6188OriginalSourceRowsVerified"]=True
    candidate["originalProductCoordinates"]=6*6188*total
    save_phase(m,a,binding,"actual-fifth-cochains-verified",pack,candidate,result)
    exact_rank=(1 if h==8 else None)
    result.update({"status":"completed","outcome":("full-infinity-fifth-exact-one" if h==8
                  else "verified-fifth-incoming-envelope-only"),
         "independentFifthLeadingCount":h,"fullFifthLeadingDimension":total,
         "fullInfinityFifthConnectionRank":exact_rank,
         "fullInfinityMaximalMinorOrderLowerBound":46+h,
         "fullInfinitySubmaximalMinorOrderLowerBound":40+h})
    result["parameters"].update({
       "originalOperator":"same natural infinity u=1/s; original17 equation units and full6188 sources",
       "allOriginalCoefficientHashesVerified":True,"allOriginalIncomingResidualsVerified":True,
       "newLowMatrixShape":[1088,628],"newLowRank":km["rank"],
       "actualLowPrefixRanks":km["actualPrefixRanks"],"completeLowKernelDimension":K.ncols(),
       "independentNonexactFifthHeads":h,"fullFifthLeadingDimension":total,
       "newCochainSHA256":m.matrix_hash(pack),"newCochainShape":[pack.nrows(),pack.ncols()],
       "newCochainRanges":ranges,"allSixOrdersAll6188OriginalSourceRowsVerified":True,
       "newFinalOriginalProductCoordinates":6*6188*total,
       "originalProductCoordinatesIncludingRestoredAncestors":checks,
       "fullFirstFourRanksByPaidActualQUpperAndSameFieldLower":[4,0,1,3],
       "paidFifthFieldRankLowerBound":1,"fullInfinityFifthConnectionRank":exact_rank,
       "fullFirstFiveRanks":([4,0,1,3,1] if h==8 else None),
       "fullConnectionExactOnlyByFullHeadAndFieldLowerSandwich":h==8,
       "normalFourFiveCorrectionsNotAssumedZero":True,
       "completeHigherIncomingBeyondFifthNotClaimed":True,
       "characteristicZeroHighQuotient26NotClaimed":True,
       "fullInfinityLength66NotClaimed":True,
       "fullInfinityMaximalMinorOrderLowerBound":46+h,
       "fullInfinitySubmaximalMinorOrderLowerBound":40+h,
       "temporaryOnly":True,"largeDataUploadedOrCommitted":False})

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--generator",required=True)
    p.add_argument("--normal-generator",required=True)
    p.add_argument("--jet-actions",required=True)
    p.add_argument("--field-receipt",required=True)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--first-connection-receipt",required=True)
    p.add_argument("--second-pure-receipt",required=True)
    p.add_argument("--second-normal-receipt",required=True)
    p.add_argument("--third-receipt",required=True)
    p.add_argument("--complete-cubic-receipt",required=True)
    p.add_argument("--fourth-receipt",required=True)
    p.add_argument("--checkpoint-dir",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=180.0)
    a=p.parse_args()
    require(a.remaining_seconds>0,"Positive actual shared time required")
    require(512<=a.memory_mib<=4096,"Explicit bounded memory")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    result={
        "format":"r150-infinity-fifth-shifted-incoming-v1",
        "status":"started","arithmetic":"exact rational python-flint",
        "scriptSHA256":sha(__file__),
        "parameters":{
            "naturalParameter":"u=1/s",
            "chart":"infinity after exact reversal and co-moving moments",
            "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
            "newOriginalCoefficientOrder":5,
            "highMatrixShape":[2295,1002],
            "largestMatrixEntryCountBound":2295*1002,
            "fixedThirdSection":"original complete1088x605 canonical correction",
            "thirdLeadingCount":12,
            "checkpointDirectory":str(Path(a.checkpoint_dir)),
            "checkpointFormat":CHECKPOINT_FORMAT,"checkpointTemporaryOnly":True,
            "sourceMultiplierTransport":
                "m_j=sum_(k<=j)binom(j,k)u^(j-k)n_k; invertible on all degree<=3 monomials",
            "targetLeftTransport":"A_new=T A_old V implies lambda_old=T^T lambda_new",
        },
    }
    def alarm(signum,frame):
        raise TimeoutError("Shared original fifth-jet budget exhausted")
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=0
    try:
        run(a,result)
    except TimeoutError as exc:
        result["status"]="incomplete";result["error"]=str(exc);code=75
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);code=1
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
            "independentFifthLeadingCount":result.get("independentFifthLeadingCount"),
            "sumFirstFiveConnectionRanksUpperBound":
                result.get("sumFirstFiveConnectionRanksUpperBound"),
            "fullInfinityMaximalMinorOrderLowerBound":
                result.get("fullInfinityMaximalMinorOrderLowerBound"),
        }),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
