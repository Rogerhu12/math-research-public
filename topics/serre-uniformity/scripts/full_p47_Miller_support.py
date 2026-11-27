#!/usr/bin/env python3
"""Isolated actual full47 support values and eight short coarse derivative jets.

This process imports python-flint and NEVER Sage.  It consumes the eight
certified CM labels, not a new complete auxiliary scan.  All selected angle
fibers retain their actual coarse multiplicities and full Frobenius orbits.
"""
import argparse
import hashlib
import importlib.util
from importlib.metadata import version
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REPO="Rogerhu12/math-research-public"
P,Q=47,4513
IDS=[0,76,77,100,108,141,196,220]
START=time.monotonic()
DEADLINE=None
TANGENTS=PRE+"scripts/full_p47_eight_CM_tangents.py"
TRANSFER=PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py"
TR_REQUEST=PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json"
CM_REQUEST=PRE+"notes/full-p47-CM-height-move-request.json"
I_STD=(0,46,1,0)
ONE=(1,0,0,1)
# R1105: public run45968484065/job140402824955; these are original
# derivative (not Taylor-coefficient) receipts.  The same rebuilt grid pays
# the comparison below, with no second seed/torsion computation.
CERTIFIED_LOW_JET_HASHES={
    "0": {
        "coarse_tangent95_sha256": "a8bb8a93e48b8508002ef8db853733a0785d41ff103c8c0bbb72e98ccb29354c",
        "heat_jets95_sha256": "b0a394cb0db9ae2804920ab9c2d767619d905c55cd9613ec29ca09f45d19cc1e",
        "G1_grid_sha256": "6d65eb6cfa14b23f7568d6de553b252b50a474a74e668f84d6e537a129921329"
    },
    "76": {
        "coarse_tangent95_sha256": "25f16f989716b2d7b3d80bd217bda8de3c0738dbfea0a65fb9eee2608c21233e",
        "heat_jets95_sha256": "1948b2c153fc0b244d097de49f611653ab8d91ca30ee84b87f5e51ec588cf0e0",
        "G1_grid_sha256": "979d166e9ee0fafd4de96796a7ce15d4af2ade0a32bfce526e576d6a23650acf"
    },
    "77": {
        "coarse_tangent95_sha256": "0e2265efba451a84394a870e3c8321d90d7541900a964bd4c0d04b09b52a6c91",
        "heat_jets95_sha256": "b1b76bee51bdade3f3dee904c631139f0bb26652fa6c124dccc8c7ad59dc8250",
        "G1_grid_sha256": "dde8dabb768917ab7d8e2362c06d7b44bce7c8f487d0196a25a7505863e12326"
    },
    "100": {
        "coarse_tangent95_sha256": "7aa3de36e17d42d4a5e32b24e5d3b610082390725efa77806f89e8ad5300463f",
        "heat_jets95_sha256": "40aff556f26e6771cc0e8807c38e8aaab9a6920f2b4ec5d0778875030eb5c2d8",
        "G1_grid_sha256": "7e2677dbfc610a7e306bc1a5fe9f0a19f54a1ef1f692293987243f28aba180aa"
    },
    "108": {
        "coarse_tangent95_sha256": "db3808c45948dbcea8fc08b95c48eb3a54101e733331f513f27f39f1cac550cb",
        "heat_jets95_sha256": "358c4687bd56812ebc09c9232919681b4eb2e5db4a75c28e21496e7a67ee4c02",
        "G1_grid_sha256": "4548dc9089588e4f0830e30e4c13249e14e133dd297a4e136bb9eb44295d7966"
    },
    "141": {
        "coarse_tangent95_sha256": "3cb7cc4c045604b4de037ea31348d13af728bbff8c2776916b427649544062c0",
        "heat_jets95_sha256": "924a12b24cd6b6280b2e4dfb38d2a09e001a914ad773ba7ef6edf2e1b15e5e7c",
        "G1_grid_sha256": "c11f5a157c6bb4f9e4438f0d392ee24823d7973080270544cfc6acabc74ac0fd"
    },
    "196": {
        "coarse_tangent95_sha256": "0cdb616c7ba3dc81e3bc2fd6e56381bfb44dfdf2552af53b9cf5b586303fdd58",
        "heat_jets95_sha256": "28860af123882cf3f67c4bfb785212e39f150ba76f5bd721a66c090a33a1f338",
        "G1_grid_sha256": "5016bb66bd604b3fac6ba69f80dc02abb09e2216d84f0a24692f132655530689"
    },
    "220": {
        "coarse_tangent95_sha256": "c319cf9e27820e348e091b337b57f1beba9edb9b5c313d7feee4b22c0c14f62d",
        "heat_jets95_sha256": "329978f5b83da6eb84cc23eff2d9b9069ebb737d3d4a7e27e71bad8bdea9695e",
        "G1_grid_sha256": "3540a9a4a714c9264685dc71e7759532d3dae02c279efd66cfe4e92d8bf079b6"
    }
}

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,field_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def check_budget():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("The isolated original support budget was reached.")

def stop(signum,frame):
    raise TimeoutError("The isolated original support budget was reached.")

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def mm(a,b):
    return ((a[0]*b[0]+a[1]*b[2])%P,(a[0]*b[1]+a[1]*b[3])%P,
            (a[2]*b[0]+a[3]*b[2])%P,(a[2]*b[1]+a[3]*b[3])%P)

def inv_matrix(a):
    d=(a[0]*a[3]-a[1]*a[2])%P
    k=pow(d,-1,P)
    return (k*a[3]%P,-k*a[1]%P,-k*a[2]%P,k*a[0]%P)

def conjugate(g,a):
    return mm(mm(g,a),inv_matrix(g))

def sign_class(a):
    negative=tuple(-x%P for x in a)
    return min(tuple(a),negative)

def all_cartans():
    out=[]
    for a in range(P):
        for c in range(1,P):
            b=(-1-a*a)*pow(c,-1,P)%P
            I=(a,b,c,-a%P)
            if I==sign_class(I):
                if mm(I,I)!=(46,0,0,46):
                    raise ArithmeticError("An original nonsplit matrix is invalid.")
                out.append(I)
    if len(out)!=1081:
        raise ArithmeticError("The complete original necklace set changed.")
    return out

def cartan_frame(I):
    a,b,c,d=I
    norm=pow(c,-1,P)
    r,s=next((r,s) for r in range(P) for s in range(P)
             if (r*r+s*s)%P==norm)
    B=((r+a*s)%P,(-s+a*r)%P,c*s%P,c*r%P)
    if (B[0]*B[3]-B[1]*B[2])%P!=1 or mm(I,B)!=mm(B,I_STD):
        raise ArithmeticError("The actual norm rescaling changed the Weil phase.")
    return B

def apply(B,label):
    a,b=label
    return ((B[0]*a+B[1]*b)%P,(B[2]*a+B[3]*b)%P)

def encode(value):
    return [int(c)%Q for c in value.to_list()]

def frob(value,n=1):
    for _ in range(n):
        value=value.frobenius()
    return value

def conv(a,b,n,zero):
    result=zero
    for i in range(n+1):
        result+=a[i]*b[n-i]
    return result

def series_product(a,b,n,zero):
    return [conv(a,b,k,zero) for k in range(n+1)]

def inverse_series(a,n,one,zero):
    if a[0].is_zero():
        raise ArithmeticError("A short physical model has singular denominator.")
    out=[zero for _ in range(n+1)]
    out[0]=one/a[0]
    for k in range(1,n+1):
        out[k]=-sum((a[i]*out[k-i] for i in range(1,k+1)),zero)/a[0]
    return out

def base_flow(curve,n,j_order):
    field=curve.field
    zero,one=field.zero(),field.one()
    a2=[zero for _ in range(n+1)]
    a=[zero for _ in range(n+1)]
    b=[zero for _ in range(n+1)]
    a[0],b[0]=curve.a,curve.b
    for k in range(n):
        a2[k+1]=(conv(a2,a2,k,zero)/12+4*a[k])/(k+1)
        a[k+1]=(conv(a2,a,k,zero)/3+6*b[k])/(k+1)
        b[k+1]=(conv(a2,b,k,zero)/2-4*conv(a,a,k,zero)/3)/(k+1)
    if not 1<=j_order<=n<=5:
        raise ArithmeticError("The original short-flow precision changed.")
    aa=series_product(a,a,j_order,zero)
    aaa=series_product(aa,a,j_order,zero)
    bb=series_product(b,b,j_order,zero)
    delta=[4*aaa[k]+27*bb[k] for k in range(j_order+1)]
    ji=inverse_series(delta,j_order,one,zero)
    j=series_product([6912*x for x in aaa],ji,j_order,zero)
    return a2,a,b,j

def point_flow(curve,point,e0,base,n):
    zero=curve.field.zero()
    a2,a,b,j=base
    e=[zero for _ in range(n+1)]
    x=[zero for _ in range(n+1)]
    y=[zero for _ in range(n+1)]
    e[0],x[0],y[0]=e0,point[0],point[1]
    for k in range(n):
        xx=[conv(x,x,h,zero) for h in range(k+1)]
        exx=sum((e[i]*xx[k-i] for i in range(k+1)),zero)
        e[k+1]=(conv(a2,e,k,zero)/12-conv(x,e,k,zero)-y[k])/(k+1)
        x[k+1]=(conv(a2,x,k,zero)/6+2*conv(e,y,k,zero)+
                  2*xx[k]+4*a[k]/3)/(k+1)
        y[k+1]=(conv(a2,y,k,zero)/4+3*conv(x,y,k,zero)+
                  3*exx+conv(e,a,k,zero))/(k+1)
    xx=series_product(x,x,n,zero)
    xxx=series_product(xx,x,n,zero)
    yy=series_product(y,y,n,zero)
    ax=series_product(a,x,n,zero)
    if any(yy[k]!=xxx[k]+ax[k]+b[k] for k in range(n+1)):
        raise ArithmeticError("The full short CM flow failed the physical curve equation.")
    return tuple(e)

def original_native_grid(module,curve,pp,qq,order,j_reduced):
    ep,eq=module.seed_eisenstein(curve,pp),module.seed_eisenstein(curve,qq)
    points={(1,0):pp,(0,1):qq}
    values={(1,0):ep,(0,1):eq}
    for n in range(2,P):
        for axis,initial,ei in ((0,pp,ep),(1,qq,eq)):
            old=(n-1,0) if axis==0 else (0,n-1)
            new=(n,0) if axis==0 else (0,n)
            point,slope=module.add_with_slope(curve,points[old],initial)
            points[new]=point
            values[new]=values[old]+ei+slope
    for b in range(1,P):
        check_budget()
        for a in range(1,P):
            label,old=(a,b),(a-1,b)
            point,slope=module.add_with_slope(curve,points[old],pp)
            points[label]=point
            values[label]=values[old]+ep+slope
    inverse={module.point_key(pt):lab for lab,pt in points.items()}
    if len(inverse)!=2208:
        raise ArithmeticError("The actual full47 grid is incomplete.")
    columns=[inverse[module.point_key(curve.frobenius(pt))] for pt in (pp,qq)]
    fm=(columns[0][0],columns[1][0],columns[0][1],columns[1][1])
    if (fm[0]*fm[3]-fm[1]*fm[2])%P!=1:
        raise ArithmeticError("Actual Frobenius did not preserve the fixed Weil root.")
    if j_reduced==1728%Q:
        ii=curve.field(95)
        images=[(-pt[0],ii*pt[1]) for pt in (pp,qq)]
        columns=[inverse[module.point_key(pt)] for pt in images]
        auto=(columns[0][0],columns[1][0],columns[0][1],columns[1][1])
        if auto!=I_STD or ii*ii!=-curve.field.one():
            raise ArithmeticError("The original Gaussian Cartan/automorphism changed.")
        automorphisms=[ONE,auto]
    elif j_reduced==0:
        rho=curve.field(next(r for r in range(2,Q) if pow(r,3,Q)==1))
        images=[(rho*pt[0],pt[1]) for pt in (pp,qq)]
        columns=[inverse[module.point_key(pt)] for pt in images]
        auto=(columns[0][0],columns[1][0],columns[0][1],columns[1][1])
        if (auto[0]-auto[3])%P or (auto[1]+auto[2])%P or (
                (auto[0]+auto[3])%P!=P-1 or
                (auto[0]*auto[3]-auto[1]*auto[2])%P!=1 or
                mm(auto,auto)==ONE or mm(mm(auto,auto),auto)!=ONE):
            raise ArithmeticError("The original cubic Cartan/automorphism changed.")
        automorphisms=[ONE,auto,mm(auto,auto)]
    else:
        automorphisms=[ONE]
    e_center=2 if j_reduced==1728%Q else (3 if j_reduced==0 else 1)
    if order!=2*e_center-1:
        raise ArithmeticError("The actual eight-center Taylor order changed.")
    low_order=e_center-1
    base=base_flow(curve,order,e_center)
    jets={}
    hasher=hashlib.sha256()
    old_hasher=hashlib.sha256()
    for label in sorted(points):
        point,e=points[label],values[label]
        negative=(-label[0]%P,-label[1]%P)
        if points[negative]!=curve.neg(point) or values[negative]!=-e:
            raise ArithmeticError("The original odd G1 normalization failed.")
        image=apply(fm,label)
        if points[image]!=curve.frobenius(point) or values[image]!=e.frobenius():
            raise ArithmeticError("The actual G1 input failed Frobenius transport.")
        curve.check(point)
        row=point_flow(curve,point,e,base,order)
        x,y=point
        original=[e]
        if low_order>=1:
            original.append(-x*e-y)
        if low_order>=2:
            original.append(-2*e*e*y-4*x*x*e-2*curve.a*e-2*x*y)
        factorials=(1,1,2)
        if any(row[k]*factorials[k]!=original[k] for k in range(low_order+1)):
            raise ArithmeticError("New Taylor jets changed an original G1 low derivative.")
        jets[label]=row
        hasher.update(canonical([list(label),module.point_key(point),
                                 [encode(v) for v in row]])+b"\n")
        old_hasher.update(canonical([list(label),module.point_key(point),
            [[int(c) for c in value.to_list()] for value in original]])+b"\n")
    for label,row in jets.items():
        negative=(-label[0]%P,-label[1]%P)
        image=apply(fm,label)
        if any(jets[negative][k]!=-row[k] or
               jets[image][k]!=row[k].frobenius() for k in range(order+1)):
            raise ArithmeticError("A new short heat jet lost exact oddness/Frobenius.")
    return jets,base[3],fm,automorphisms,{
        "point_count":2208,"power_series_order":order,
        "grid_sha256":hasher.hexdigest(),"frobenius_matrix":list(fm),
        "geometric_automorphism_matrices":[list(a) for a in automorphisms],
        "original_low_heat_order":low_order,
        "original_low_G1_grid_sha256":old_hasher.hexdigest(),
        "all_new_jets_odd_and_Frobenius":True,
        "G1_normalization":"original short-model 47e(P)=-sum of slopes",
        "KS_flow":"A2'=A2^2/12+4A; A'=A2*A/3+6B; B'=A2*B/2-4A^2/3"}

class Evaluation:
    def __init__(self,curve,jets,descriptors):
        self.curve,self.jets,self.descriptors=curve,jets,descriptors
        self.half=[(a,b) for a in range(P) for b in range(P)
                   if (a or b) and (a,b)<(-a%P,-b%P)]
        self.groups={h:[] for h in range(1,P)}
        for a,b in self.half:
            h=(a*a+b*b)%P
            if not h:
                raise ArithmeticError("An actual nonsplit norm vanished.")
            self.groups[h].append((a,b))
        if len(self.half)!=1104 or any(len(v)!=24 for v in self.groups.values()):
            raise ArithmeticError("The full two-phase norm fibers are incomplete.")
        self.requested={}
        for index,(a,c,d) in enumerate(descriptors):
            self.requested.setdefault((int(c),int(d)),[]).append((index,int(a)))
        self.zeta=[curve.field(pow(2,h,Q)) for h in range(P)]
        self.cache={}

    def evaluate(self,I,order):
        cache_key=(tuple(I),order)
        if cache_key in self.cache:
            return self.cache[cache_key]
        field=self.curve.field
        zero=field.zero()
        B=cartan_frame(I)
        total_rows={}
        for (c,d),rows in self.requested.items():
            check_budget()
            first,second={},{}
            for h,labels in self.groups.items():
                f=[zero for _ in range(order+1)]
                g=[zero for _ in range(order+1)]
                for a,b in labels:
                    left=self.jets[apply(B,(a,b))]
                    right=self.jets[apply(B,((d*a-c*b)%P,(c*a+d*b)%P))]
                    conjugated=self.jets[apply(B,((d*a+c*b)%P,(-c*a+d*b)%P))]
                    for k in range(order+1):
                        f[k]+=2*conv(left,right,k,zero)
                        g[k]+=2*conv(left,conjugated,k,zero)
                first[h],second[h]=f,g
            for index,a in rows:
                result=[zero for _ in range(order+1)]
                for h in range(1,P):
                    for k in range(order+1):
                        result[k]+=(self.zeta[(a*h)%P]*first[h][k]+
                                    self.zeta[(-a*h)%P]*second[h][k])
                total_rows[index]=tuple(result)
        if len(total_rows)!=95:
            raise ArithmeticError("The complete actual95 source was not evaluated.")
        output=[total_rows[i] for i in range(95)]
        self.cache[cache_key]=output
        return output

def coarse_jet(module,rows,jseries,stabilizer):
    """Actual ratios need only the first j coefficient, including at ramification."""
    e=stabilizer
    if e not in (1,2,3) or len(jseries)!=e+1 or (
            len(rows)!=95 or any(len(row)!=2*e for row in rows)):
        raise ArithmeticError("The original coarse/projective jet dimensions changed.")
    if any(not a.is_zero() for a in jseries[1:e]):
        raise ArithmeticError("The actual coarse j parameter has a forbidden lower term.")
    je=jseries[e]
    if je.is_zero():
        raise ArithmeticError("The actual coarse j parameter lost its leading term.")
    lead=[row[e-1] for row in rows]
    pivot=next((i for i,x in enumerate(lead) if not x.is_zero()),None)
    if pivot is None:
        raise ArithmeticError("The original logarithmic source has a basepoint at the CM center.")
    zero=je-je
    one=je/je
    denominator=list(rows[pivot][e-1:2*e])
    inverse=inverse_series(denominator,e,one,zero)
    values=[]
    derivatives=[]
    coarse=[]
    for row in rows:
        if any(not v.is_zero() for v in row[:e-1]):
            raise ArithmeticError("The original stabilizer character did not descend.")
        quotient=series_product(list(row[e-1:2*e]),inverse,e,zero)
        if any(not a.is_zero() for a in quotient[1:e]):
            raise ArithmeticError("A projective section ratio has a forbidden fine coefficient.")
        coarse.append(module.base_integer(row[e-1]/(e*je)))
        values.append(module.base_integer(quotient[0]))
        derivatives.append(module.base_integer(quotient[e]/je))
    if values[pivot]!=1 or derivatives[pivot]!=0:
        raise ArithmeticError("The denominator ratio did not normalize exactly.")
    return coarse,values,derivatives,pivot

def worker(req,output,seconds):
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Only the pinned public Actions may evaluate actual points.")
    if any(name=="sage" or name.startswith("sage.") for name in sys.modules):
        raise RuntimeError("The actual field worker must never import Sage.")
    global DEADLINE
    DEADLINE=START+seconds
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    if version("python-flint")!="0.9.0":
        raise RuntimeError("Wrong pinned python-flint version.")
    old=load_module("actual_tangents_for_Miller",TANGENTS)
    if old.field_runtime_libraries():
        raise RuntimeError("A native FLINT runtime preceded the isolated wheel import.")
    from flint import fq_default_ctx,nmod_poly
    libraries=old.field_runtime_libraries()
    if len(libraries)!=1 or any("python_flint.libs" not in Path(path).parts
                                for path in libraries):
        raise RuntimeError("The field worker did not isolate the wheel FLINT library.")
    transfer=load_module("actual_transfer_for_Miller",TRANSFER)
    old.DEADLINE=DEADLINE
    transfer.STARTED,transfer.DEADLINE=START,DEADLINE
    cmreq=json.loads((ROOT/CM_REQUEST).read_text())
    trreq=json.loads((ROOT/TR_REQUEST).read_text())
    descriptors=cmreq["Hodge_descriptors"]
    if len(descriptors)!=95:
        raise RuntimeError("The original logarithmic descriptor input changed.")
    _,roles,character_rows,p_models,candidates=transfer.candidate_input(ROOT,trreq,nmod_poly)
    cm_rows=transfer.consume_known_cm(candidates,trreq["certified_cm_rows"])
    byid={int(r["candidate_id"]):r for r in cm_rows}
    if sorted(byid)!=IDS:
        raise ArithmeticError("The eight original CM labels changed.")
    zeta0=next(z for z in range(2,Q) if pow(z,P,Q)==1)
    if zeta0!=2:
        raise ArithmeticError("The fixed actual4513 Weil root is not 2.")
    log0={pow(zeta0,i,Q):i for i in range(P)}
    beta=transfer.circle_values(zeta0,list(range(2,P-2,2)),log0)
    allI=all_cartans()
    result={"protocol":"full-p47-Miller-support-v1","prime":P,
        "coefficient_prime":Q,"descriptor_sha256":digest(descriptors),
        "fields":[],"points":[],"centers":[],"angle_images":{},
        "family_receipts":[],"target_jet_receipt":[]}
    for identifier in IDS:
        check_budget()
        cm=byid[identifier]
        target=[c*beta[r]%P for c,r in zip(candidates[identifier]["vector"],roles)]
        curve,pp,qq,marking=old.select_actual_model(
            transfer,fq_default_ctx,cm,target,roles,zeta0,beta)
        j=int(cm["j_rational"])%Q
        e_center=2 if j==1728%Q else (3 if j==0 else 1)
        order=2*e_center-1
        jets,jseries,fm,autos,grid_receipt=original_native_grid(
            old,curve,pp,qq,order,j)
        evaluator=Evaluation(curve,jets,descriptors)
        central=evaluator.evaluate(I_STD,order)
        coarse_values,values,derivatives,pivot=coarse_jet(old,central,jseries,e_center)
        factorials=(1,1,2)
        old_derivatives=[[old.base_integer(row[k]*factorials[k])
                          for k in range(e_center)] for row in central]
        original_coarse,original_KS=old.coarse_tangent_vector(
            old_derivatives,old.base_integer(curve.a),old.base_integer(curve.b),j)
        low_receipt={
            "coarse_tangent95_sha256":digest(coarse_values),
            "heat_jets95_sha256":digest(old_derivatives),
            "G1_grid_sha256":grid_receipt["original_low_G1_grid_sha256"]}
        if (low_receipt!=CERTIFIED_LOW_JET_HASHES[str(identifier)] or
                original_coarse!=coarse_values or
                digest(coarse_values)!=req["certified_CM_tangent95_sha256"][str(identifier)]):
            raise ArithmeticError("The new grid/source/coarse values disagree with R1105.")
        if jseries[0]!=curve.field(j):
            raise ArithmeticError("The short flow starts at the wrong actual j invariant.")
        pivot_inverse=pow(coarse_values[pivot],-1,Q)
        if values!=[value*pivot_inverse%Q for value in coarse_values]:
            raise ArithmeticError("Projective constants do not equal normalized original tangents.")
        result["centers"].append({"candidate_id":identifier,
            "j_rational":cm["j_rational"],"coarse_parameter":"j-j_CM",
            "denominator_index":pivot,"ratio_values":values,"ratio_dz":derivatives,
            "coarse_tangent95_sha256":digest(coarse_values)})
        result["target_jet_receipt"].append({"candidate_id":identifier,
            "ratio_values_sha256":digest(values),"ratio_dz_sha256":digest(derivatives),
            "coarse_tangent95_sha256":digest(coarse_values),"denominator_index":pivot,
            "power_series_order":order,"j_series_order":e_center,
            "j_series":[encode(a) for a in jseries],
            "R1105_low_receipt":low_receipt,"R1105_KS_formula":original_KS,
            "old_low_jets_exact_match":True})
        emit("actual_CM_projective_first_jet",**result["target_jet_receipt"][-1])
        def coarse_key(I):
            return min(sign_class(conjugate(g,I)) for g in autos)
        center_key=coarse_key(I_STD)
        angles={0,2,4}
        if identifier==141:
            angles.update((5,20))
        if identifier==0:
            angles.add(12)
        image_counts={c:{} for c in angles}
        all_coarse=set()
        for I in allI:
            product=mm(I_STD,I)
            c=(-(product[0]+product[3])*pow(2,-1,P))%P
            c=min(c,P-c)
            if c in angles:
                key=coarse_key(I)
                if key==center_key:
                    raise ArithmeticError("A nonidentity raw angle met the actual canonical center.")
                image_counts[c][key]=image_counts[c].get(key,0)+1
                all_coarse.add(key)
        for c,counts in image_counts.items():
            if sum(counts.values())!=(24 if c==0 else 48):
                raise ArithmeticError("A complete original angle fiber lost raw degree.")
        unseen=set(all_coarse)
        point_id={}
        closed=[]
        while unseen:
            first=min(unseen)
            orbit=[]
            current=first
            while current not in orbit:
                if current not in all_coarse:
                    raise ArithmeticError("The selected actual support is not Frobenius stable.")
                orbit.append(current)
                current=coarse_key(conjugate(fm,current))
            if current!=first:
                raise ArithmeticError("The actual geometric point Frobenius orbit did not close.")
            representative=min(orbit)
            orbit=orbit[orbit.index(representative):]+orbit[:orbit.index(representative)]
            f=len(orbit)
            if marking["field_degree"]%f:
                raise ArithmeticError("A closed actual point is not defined in the original torsion field.")
            stabilizer=sum(1 for g in autos if sign_class(conjugate(g,representative))==
                           sign_class(representative))
            if stabilizer not in (1,2,3):
                raise ArithmeticError("Unexpected actual coarse stabilizer.")
            rows=evaluator.evaluate(representative,stabilizer-1)
            leading=[row[stabilizer-1] for row in rows]
            if any(any(not a.is_zero() for a in row[:stabilizer-1]) for row in rows):
                raise ArithmeticError("An actual coarse support frame has forbidden lower terms.")
            pivot=next((i for i,a in enumerate(leading) if not a.is_zero()),None)
            if pivot is None:
                raise ArithmeticError("The certified degree167 embedding has a basepoint.")
            normalized=[a/leading[pivot] for a in leading]
            if any(frob(a,f)!=a for a in normalized):
                raise ArithmeticError("Actual support ratios did not descend to the closed point.")
            for h in range(1,f):
                if f%h==0 and all(frob(a,h)==a for a in normalized):
                    raise ArithmeticError("The original embedding detected a shorter point orbit.")
            pid="%d:%s"%(identifier,",".join(map(str,representative)))
            for point in orbit:
                if point in point_id:
                    raise ArithmeticError("Closed point orbits overlap.")
                point_id[point]=pid
                unseen.discard(point)
            record={"id":pid,"field_id":str(identifier),"degree":f,
                    "values95":[encode(a) for a in normalized],
                    "native_Cartan":list(representative),
                    "effective_stabilizer":stabilizer,
                    "projective_pivot":pivot,"geometric_orbit":[list(a) for a in orbit]}
            closed.append(record)
            result["points"].append(record)
        for c,counts in image_counts.items():
            grouped={}
            for key,mult in counts.items():
                pid=point_id[key]
                if pid in grouped and grouped[pid]!=mult:
                    raise ArithmeticError("Actual coarse multiplicity is not constant on a closed orbit.")
                grouped[pid]=mult
            degree=sum(grouped[row["id"]]*row["degree"]
                       for row in closed if row["id"] in grouped)
            if degree!=(24 if c==0 else 48):
                raise ArithmeticError("Closed point grouping changed the complete raw angle degree.")
            result["angle_images"]["%d:%d"%(identifier,c)]=[
                [pid,grouped[pid]] for pid in sorted(grouped)]
        result["fields"].append({"id":str(identifier),
            "degree":marking["field_degree"],
            "modulus":[int(c)%Q for c in curve.field.modulus()]})
        receipt={"candidate_id":identifier,"actual_marking":marking,
            "new_short_grid":grid_receipt,"selected_angles":sorted(angles),
            "geometric_support_count":len(all_coarse),
            "closed_support_count":len(closed),
            "closed_support_sha256":digest(closed),
            "angle_images_sha256":digest({str(c):result["angle_images"][
                "%d:%d"%(identifier,c)] for c in sorted(angles)}),
            "target_ratio_values_sha256":digest(values),"target_ratio_dz_sha256":digest(derivatives),
            "coarse_tangent95_sha256":digest(coarse_values)}
        result["family_receipts"].append(receipt)
        emit("actual_Miller_support_family",**receipt)
    if [r["candidate_id"] for r in result["centers"]]!=IDS:
        raise ArithmeticError("The eight actual target jets are incomplete.")
    temp=Path(str(output)+".tmp")
    temp.write_text(json.dumps(result,sort_keys=True,separators=(",",":")))
    temp.replace(output)
    signal.setitimer(signal.ITIMER_REAL,0)
    emit("actual_Miller_support_receipt",status="complete",
         result_sha256=digest(result),closed_point_count=len(result["points"]),
         scope="New actual angle-support values and eight coarse first jets; no Miller alpha or QC rank inferred.")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--request",required=True)
    parser.add_argument("--output",required=True)
    parser.add_argument("--seconds",required=True,type=int)
    args=parser.parse_args()
    raw=Path(args.request).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The isolated worker request hash changed.")
    req=json.loads(raw)
    if req["execution_id"]!="full-p47-finite-third-kind-v1":
        raise RuntimeError("Wrong isolated finite support request.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Pinned worker source changed: "+path)
    if not 1<=args.seconds<=int(req["field_worker_seconds"]):
        raise RuntimeError("Unexpected isolated worker arithmetic budget.")
    worker(req,Path(args.output),args.seconds)

if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("actual_Miller_support_receipt",status="incomplete",
             exception_type=type(exc).__name__,message=str(exc))
        traceback.print_exc()
        sys.exit(1)
