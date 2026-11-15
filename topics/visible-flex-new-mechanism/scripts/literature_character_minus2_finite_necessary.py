#!/usr/bin/env python3
"""One finite exact necessary system for weight -2 positive characters.

Consume the completed R163 fourteen-family head, without rebuilding forcing,
responses, old normal forms, or any profile evaluation.  R164 fixes the same
normalized eight-matrix multiplier.  Exact rational necessary rows are formed
from local tests and a fixed small polynomial-path table.  A floating LP may
propose Farkas supports; only verified nonnegative rational identities can
exclude all nonzero character coordinates.  Feasibility is only an outer test.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from math import gcd, lcm
import os
from pathlib import Path
import resource
import time

SCHEMA = "visible-flex-character-minus2-finite-rational-necessary-v1"
HEAD_SCHEMA = "visible-flex-complete-character-head-minus2-v1"
REPOSITORY = "Rogerhu12/math-research-public"
HEAD_DRIVER = {"filename": "literature_character_head_minus2.py", "bytes": 58856,
    "sha256": "fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11"}
FAMILIES = ("F0","Q2_0","Q2_1","Q2_2","A_hh","A_hk","A_kk","H1","H2",
            "Q4_0","Q4_1","Q4_2","Q4_3","Q4_4")
EXPONENT = {"F0":0,"Q2_0":0,"Q2_1":1,"Q2_2":2,"A_hh":2,"A_hk":1,
            "A_kk":0,"H1":2,"H2":1,**{"Q4_"+str(i):i for i in range(5)}}
PARAMETERS = ("p0","p1","p2","r0","r1","s0","s1","t1")
K_POINTS = tuple(F(v) for v in (-2,-1,0,1,2))
PSD_DIRECTIONS = ((1,0),(0,1),(1,1),(1,-1),(1,2),(2,1),(1,-2),(2,-1))
TIMES = tuple(F(v) for v in ("1/16","1/4","1","4","16"))
PATHS = (
    ("h_axis","1","0","0"), ("k_axis","0","0","1"),
    ("mixed_plus","1","0","1"), ("mixed_minus","1","0","-1"),
    ("decreasing_p","-1/2","0","1"), ("crossing_k","1","1","-2"))
RHO = (F(0),F(0),F(0),F(0),F(35),F(-84),F(70),F(-20))


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()


def sha(value):
    return hashlib.sha256(value).hexdigest()


def identity(path):
    path=Path(path);raw=path.read_bytes()
    return {"filename":path.name,"bytes":len(raw),"sha256":sha(raw)}


class Limit(RuntimeError):
    pass


class Budget:
    def __init__(self,seconds=240,memory_mib=1024,bits=16384):
        self.started=time.monotonic();self.seconds=seconds
        self.memory_mib=memory_mib;self.bits=bits;self.operations=0
    def check(self,row=None):
        self.operations+=1
        if time.monotonic()-self.started>self.seconds:
            raise Limit("declared elapsed-time ceiling")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024>self.memory_mib:
            raise Limit("polled resident-memory ceiling")
        if row is not None and any(max(abs(x.numerator).bit_length(),x.denominator.bit_length())>self.bits
                                   for x in row.values()):
            raise Limit("exact-rational coefficient bit ceiling")
    def remaining(self):
        self.check();return max(.01,self.seconds-(time.monotonic()-self.started))


def row_add(*items):
    out={}
    for row,amount in items:
        amount=F(amount)
        for i,c in row.items():
            out[i]=out.get(i,F(0))+amount*c
            if not out[i]:
                del out[i]
    return out


def unit(i):
    return {i:F(1)}


def serial_row(row):
    return [[i,str(c)] for i,c in sorted(row.items())]


def read_row(raw,n):
    out={}
    for i,c in raw:
        if not isinstance(i,int) or not 0<=i<n or i in out:
            raise ValueError("invalid exact normal-coordinate row")
        c=F(c)
        if c:
            out[i]=c
    return out


def primitive(row,equality=False):
    if not row:
        return {}
    denominator=1
    for c in row.values():
        denominator=lcm(denominator,c.denominator)
    values={i:c.numerator*(denominator//c.denominator) for i,c in row.items()}
    divisor=0
    for c in values.values():
        divisor=gcd(divisor,abs(c))
    if equality and values[min(values)]<0:
        divisor=-divisor
    return {i:F(c//divisor) for i,c in values.items()}


class RowTable:
    def __init__(self,budget,equality=False):
        self.rows=[];self.records=[];self.keys={};self.budget=budget;self.equality=equality
        self.zero_rows=0
    def add(self,row,reason):
        self.budget.check(row)
        row=primitive(row,self.equality)
        if not row:
            self.zero_rows+=1;return None
        key=tuple(sorted(row.items()))
        if key in self.keys:
            self.records[self.keys[key]]["additional_reason_count"]+=1
            return self.keys[key]
        index=len(self.rows);self.keys[key]=index;self.rows.append(row)
        self.records.append({"index":index,"coefficients":serial_row(row),"reason":reason,
                             "additional_reason_count":0})
        return index


def rref(rows,n,budget):
    """Exact equality reduction; no numerical rank or function-rank assertion."""
    basis={}
    for incoming in rows:
        v=dict(incoming)
        while v:
            budget.check(v);p=min(v)
            if p not in basis:
                scale=v[p];basis[p]={i:c/scale for i,c in v.items()};break
            v=row_add((v,1),(basis[p],-v[p]))
    for p in sorted(basis,reverse=True):
        for q in sorted(basis):
            if q<p and p in basis[q]:
                basis[q]=row_add((basis[q],1),(basis[p],-basis[q][p]))
                budget.check(basis[q])
    free=[i for i in range(n) if i not in basis]
    position={j:i for i,j in enumerate(free)}
    transform=[]
    for j in range(n):
        if j in position:
            transform.append(unit(position[j]))
        else:
            if any(k in basis for k in basis[j] if k!=j):
                raise AssertionError("RREF pivot was not eliminated")
            transform.append({position[k]:-c for k,c in basis[j].items() if k!=j})
    for row in rows:
        if substitute(row,transform):
            raise AssertionError("exact null parametrization failed")
    return basis,free,transform


def substitute(row,transform):
    return row_add(*((transform[i],c) for i,c in row.items()))


def apply_row(row,point):
    return sum((c*point[i] for i,c in row.items()),F(0))


# All path integration below is polynomial arithmetic over Q, not quadrature.
def ptrim(p):
    p=list(map(F,p))
    while p and not p[-1]:p.pop()
    return tuple(p)


def padd(*items):
    out=[]
    for poly,scale in items:
        scale=F(scale)
        if len(out)<len(poly):out.extend([F(0)]*(len(poly)-len(out)))
        for i,c in enumerate(poly):out[i]+=scale*c
    return ptrim(out)


def pmul(a,b):
    if not a or not b:return ()
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[i+j]+=x*y
    return ptrim(out)


def ppow(a,n):
    if not isinstance(n,int) or n<0:raise ValueError("nonnegative polynomial power required")
    result=(F(1),)
    while n:
        if n&1:result=pmul(result,a)
        n//=2
        if n:a=pmul(a,a)
    return result


def pdiff(p):
    return ptrim([i*p[i] for i in range(1,len(p))])


def pintegral(p):
    return sum((c/F(i+1) for i,c in enumerate(p)),F(0))


def peval(p,x):
    value=F(0)
    for c in reversed(p):value=value*x+c
    return value


def family_value(poly,k):
    return row_add(*((row,k**power) for power,row in poly.items()))


def path_integrals(families,alpha,kappa,beta,budget):
    alpha,kappa,beta=map(F,(alpha,kappa,beta))
    if min(F(1),1+alpha)<=0:raise ValueError("the fixed monotone-rho path requires p>0")
    p=padd(((1,),1),(RHO,alpha));k=padd(((kappa,),1),(RHO,beta))
    dp,dk=pdiff(p),pdiff(k);ddp,ddk=pdiff(dp),pdiff(dk)
    z=padd((pmul(dp,dp),6),(pmul(p,ddp),-2))
    area=padd((pmul(pmul(p,dp),ddk),-2),(pmul(dk,z),-1))
    kpowers={0:(F(1),)}
    def integrate_family(name,factor):
        out={}
        for degree,value in sorted(families[name].items()):
            budget.check()
            if degree not in kpowers:kpowers[degree]=ppow(k,degree)
            amount=pintegral(pmul(kpowers[degree],factor))
            out=row_add((out,1),(value,amount))
        budget.check(out);return out
    p4=ppow(p,4);minusdp=padd((dp,-2))
    a=integrate_family("F0",p4);b={};c={}
    for i in range(3):
        factor=pmul(pmul(ppow(minusdp,i),ppow(p,4-i)),ppow(dk,2-i))
        b=row_add((b,1),(integrate_family("Q2_"+str(i),factor),1))
    parts=[
        ("A_hh",ppow(z,2)),("A_hk",pmul(pmul(ppow(p,2),z),ddk)),
        ("A_kk",pmul(p4,ppow(ddk,2))),
        ("H1",pmul(pmul(p,minusdp),area)),
        ("H2",pmul(pmul(ppow(p,2),dk),area))]
    parts += [("Q4_"+str(i),pmul(pmul(ppow(minusdp,i),ppow(p,4-i)),ppow(dk,4-i)))
              for i in range(5)]
    for name,factor in parts:c=row_add((c,1),(integrate_family(name,factor),1))
    return a,b,c,{"p_coefficients":[str(x) for x in p],"k_coefficients":[str(x) for x in k],
        "Z_coefficients":[str(x) for x in z],"D_coefficients":[str(x) for x in area],
        "p_positive_lower_bound":str(min(F(1),1+alpha)),
        "omega_prime_coefficients":[str(x) for x in padd((pmul(ppow(p,2),dk),F(1,2)))],
        "polynomial_only_C3_at_constant_extension":True,
        "necessary_for_Cinf_paths_by_C2_flat_approximation":True}


def reference_data(data,n):
    ref=data["reference_matrix"]
    if ref.get("coordinate_order")!=list(PARAMETERS):
        raise ValueError("the true E8 coordinate order changed")
    mat=[[F(v) for v in row] for row in ref["matrix_columns_are_reference_states"]]
    inv=[[F(v) for v in row] for row in ref["inverse"]]
    if len(mat)!=8 or len(inv)!=8 or any(len(x)!=8 for x in mat+inv):
        raise ValueError("eight by eight reference matrix required")
    for i in range(8):
        for j in range(8):
            if sum((mat[i][k]*inv[k][j] for k in range(8)),F(0))!=F(i==j):
                raise ValueError("published reference inverse failed exact multiplication")
    def derivative_rows(name):
        rows=data[name]
        if [row["reference_index"] for row in rows]!=list(range(8)):
            raise ValueError("eight reference derivative rows required")
        return [read_row(row["coefficients"],n) for row in rows]
    cr=derivative_rows("static_translation_reference_coefficients")
    dr=derivative_rows("static_scaling_reference_coefficients")
    c=[row_add(*((cr[i],inv[i][j]) for i in range(8))) for j in range(8)]
    d=[row_add(*((dr[i],inv[i][j]) for i in range(8))) for j in range(8)]
    mu=[d[0],row_add((d[1],F(1,2))),row_add((d[2],F(1,3))),row_add((d[3],-1)),
        row_add((c[6],F(1,3)),(c[0],F(-4,3))),
        row_add((c[6],F(1,3)),(c[0],F(2,3))),d[6],row_add((d[7],F(1,2)))]
    mu_ref=[row_add(*((mu[j],mat[j][i]) for j in range(8))) for i in range(8)]
    return mat,inv,c,d,mu,mu_ref


def add_lie_compatibility(c,d,eq):
    rows=[d[4],d[5],c[3],row_add((c[4],1),(d[3],1)),
          row_add((c[5],1),(d[3],1)),row_add((c[7],1),(d[6],-2)),
          row_add((c[1],1),(d[0],-1),(d[6],F(1,2))),
          row_add((c[2],1),(d[1],-1),(d[7],F(1,4)))]
    for j,row in enumerate(rows):
        eq.add(row,{"kind":"R164_automatic_true_cocycle_compatibility","index":j})


def original_pair(data,roots):
    out={}
    for mode in (-4,-2):
        name=roots[str(mode)]
        if name not in data["roots"]:raise ValueError("bound original root absent")
        for raw,num,den in data["roots"][name]:
            power,atoms=raw
            if not isinstance(power,int) or power<0 or any(
                    not isinstance(j,int) or not 0<=j<len(data["profile_atoms"]) for j in atoms):
                raise ValueError("malformed original monomial")
            key=(mode,power,tuple(atoms))
            if key in out:raise ValueError("duplicate original monomial")
            value=F(num,den)
            if value:out[key]=value
    return out


def literal_original_relations(data,normal,eq):
    """Only literal proportional original vectors; no old rank/NF is recomputed."""
    signatures={}
    def signature(pair):
        if not pair:return None,F(0)
        factor=pair[min(pair)]
        return tuple((key,c/factor) for key,c in sorted(pair.items())),factor
    response=data["archived_R_basis_records"]
    if len(response)!=40:raise ValueError("the published complete R_-2 basis must have forty columns")
    for record in response:
        pair=original_pair(data,record["roots"]);key,scale=signature(pair)
        if key is not None and key not in signatures:
            signatures[key]=("R",record["original_column"],scale)
    proofs=[]
    for record in normal:
        pair=original_pair(data,record["roots"]);key,scale=signature(pair);i=record["index"]
        if key is None:
            row=unit(i);proof={"normal_index":i,"kind":"literal_original_zero"}
        elif key in signatures:
            kind,j,previous_scale=signatures[key];ratio=scale/previous_scale
            row=unit(i) if kind=="R" else row_add((unit(i),1),(unit(j),-ratio))
            proof={"normal_index":i,"kind":"literal_original_proportional_to_"+kind,
                   "previous_index":j,"rational_ratio":str(ratio)}
        else:
            signatures[key]=("normal",i,scale);continue
        eq.add(row,proof);proofs.append(proof)
    return proofs


def construct_system(data,budget):
    normal=data["normal_family_records"];n=len(normal)
    if n>5000 or [r["index"] for r in normal]!=list(range(n)):
        raise Limit("normal-coordinate list exceeds the declared 5000-column interface")
    eq=RowTable(budget,True);ineq=RowTable(budget)
    fields={family:{} for family in FAMILIES}
    for record in normal:
        family=record["family"];state=tuple(record["state_key"])
        if (family not in fields or len(state)!=4 or record["weight"]!=-2
            or any(not isinstance(x,int) for x in state) or any(x<0 for x in state[1:])
            or state in fields[family]):
            raise ValueError("complete family/state identity changed")
        for mode,name in record["roots"].items():
            if mode not in ("-4","-2") or data["original_root_sha256"].get(name)!=record["original_mode_sha256"][mode]:
                raise ValueError("normal record original-root SHA mismatch")
        if set(record["roots"])!={"-4","-2"}:raise ValueError("both full modes are required")
        fields[family][state]=unit(record["index"])
    literal=literal_original_relations(data,normal,eq)
    for j,record in enumerate(data["head_translation_presentation"]):
        eq.add(read_row(record["coefficients"],n),
               {"kind":"complete_R163_translation_denominator","record":j,
                "family":record["family"],"state_key":record["state_key"]})
    mat,inv,c,d,mu,mu_ref=reference_data(data,n)
    add_lie_compatibility(c,d,eq)
    corrected={family:dict(values) for family,values in fields.items()}
    coords=data["eight_reference_coordinate_polynomials"]
    for dw in (0,2):
        rows=coords[str(dw)]
        if len(rows)!=8:raise ValueError("same eight reference coordinate polynomials required")
        for i,entries in enumerate(rows):
            for record in entries:
                state=tuple(record["state_key"]);velocity=tuple(record["velocity"])
                if (len(state)!=4 or len(velocity)!=2 or any(v<0 for v in velocity)
                    or sum(velocity)!=dw):
                    raise ValueError("matrix coordinate state/velocity shape")
                if dw==0:
                    family="F0"
                else:
                    family="Q2_"+str(velocity[0])
                value=row_add((corrected[family].get(state,{}),1),
                              (mu_ref[i],-F(record["coefficient"])))
                if value:corrected[family][state]=value
                elif state in corrected[family]:del corrected[family][state]
    kfamilies={}
    for family in FAMILIES:
        exponent=-2-EXPONENT[family];poly={}
        for state,row in sorted(corrected[family].items()):
            h,k,omega,logh=state
            if h==exponent and omega==0 and logh==0:
                poly[k]=row
            else:
                eq.add(row,{"kind":"R164_corrected_scalar_covariance",
                    "family":family,"state_key":list(state),"required_h_power":exponent})
        kfamilies[family]=poly
    # R163 exact F0 reference zeros, using F0 itself rather than raw L0 reference roots.
    for i,state in enumerate(data["reference_matrix"]["basis_states_h_k_omega"]):
        h,k,omega=map(F,state)
        if h!=1:raise ValueError("reference h must be one")
        row=row_add(*((value,k**key[1]*omega**key[2]) for key,value in fields["F0"].items() if not key[3]))
        eq.add(row,{"kind":"R163_exact_F0_reference_zero","reference_index":i})
    for k in K_POINTS:
        ineq.add(family_value(kfamilies["F0"],k),{"kind":"static","k":str(k)})
        ineq.add(row_add((family_value(kfamilies["Q4_4"],k),1),
                         (family_value(kfamilies["A_hh"],k),F(25,9))),
                 {"kind":"fixed_k_sharp_highest","k":str(k)})
        for x,y in PSD_DIRECTIONS:
            row=row_add((family_value(kfamilies["A_hh"],k),x*x),
                        (family_value(kfamilies["A_hk"],k),x*y),
                        (family_value(kfamilies["A_kk"],k),y*y))
            ineq.add(row,{"kind":"acceleration_PSD_rational_direction","k":str(k),"direction":[x,y]})
    paths=[]
    for label,alpha,kappa,beta in PATHS:
        a,b,cost,metadata=path_integrals(kfamilies,alpha,kappa,beta,budget)
        paths.append({"label":label,"alpha":alpha,"kappa":kappa,"beta":beta,**metadata,
                      "A":serial_row(a),"B":serial_row(b),"C":serial_row(cost)})
        ineq.add(a,{"kind":"path_time_limit_A","path":label})
        ineq.add(cost,{"kind":"path_time_limit_C","path":label})
        for t in TIMES:
            ineq.add(row_add((a,t*t),(b,t),(cost,1)),
                     {"kind":"complete_path_at_positive_rational_t","path":label,"t":str(t),
                      "t_is_duration_squared":True})
    basis,free,transform=rref(eq.rows,n,budget)
    reduced=RowTable(budget)
    for i,row in enumerate(ineq.rows):
        reduced.add(substitute(row,transform),{"original_inequality_index":i})
    return {"normal_coordinate_count":n,"normal_coordinate_metadata":normal,
        "equalities":eq,"inequalities":ineq,"reduced":reduced,"rref":basis,
        "free":free,"transform":transform,"paths":paths,"literal_proofs":literal,
        "mu":mu,"c":c,"d":d,"kfamilies":kfamilies,
        "ambient_original_functions_assumed_independent":False}


def solve_affine(rows,rhs,n,preferred,budget):
    """An exact candidate solver, with explicit values for the free unknowns."""
    basis={}
    for incoming,value in zip(rows,rhs):
        row=dict(incoming);value=F(value)
        while row:
            budget.check(row);p=min(row)
            if p not in basis:
                scale=row[p];basis[p]=({i:c/scale for i,c in row.items()},value/scale);break
            known,known_rhs=basis[p];amount=row[p]
            row=row_add((row,1),(known,-amount));value-=amount*known_rhs
        else:
            if value:return None
    answer=[F(preferred[i]) for i in range(n)]
    for p in sorted(basis,reverse=True):
        row,value=basis[p]
        answer[p]=value-sum((c*answer[i] for i,c in row.items() if i!=p),F(0))
    if any(apply_row(row,answer)!=value for row,value in zip(rows,rhs)):
        raise AssertionError("exact affine reconstruction did not solve its equations")
    return answer


def verify_farkas(rows,target,multipliers):
    if any(v<0 for v in multipliers.values()):return False
    return row_add(*((rows[i],v) for i,v in multipliers.items()))==target


def rational_dual_proposal(rows,target,n,budget):
    """HiGHS only selects a support. Fractions alone authorize a certificate."""
    import numpy as np
    from scipy.optimize import linprog
    scales=[max(abs(c) for c in row.values()) for row in rows]
    normalized=[{j:c/scales[i] for j,c in row.items()} for i,row in enumerate(rows)]
    array=np.zeros((len(rows),n))
    for i,row in enumerate(normalized):
        for j,c in row.items():array[i,j]=float(c)
    b=np.array([float(target.get(j,0)) for j in range(n)])
    result=linprog(np.zeros(len(rows)),A_eq=array.T,b_eq=b,bounds=(0,None),method="highs",
                   options={"time_limit":min(15.,budget.remaining())})
    proposal={"scipy_status":int(result.status),"success":bool(result.success),
              "floating_result_is_not_a_certificate":True}
    if not result.success:return None,proposal
    full=result.x
    for threshold in (1e-9,1e-12,0.):
        support=[i for i,x in enumerate(full) if x>threshold]
        if not support or len(support)>max(32,4*n):continue
        equations=[{a:normalized[i].get(j,F(0)) for a,i in enumerate(support)
                    if normalized[i].get(j,F(0))} for j in range(n)]
        rhs=[target.get(j,F(0)) for j in range(n)]
        preferred=[F(float(full[i])).limit_denominator(10**8) for i in support]
        exact=solve_affine(equations,rhs,len(support),preferred,budget)
        if exact is None or any(x<0 for x in exact):continue
        multipliers={i:c/scales[i] for i,c in zip(support,exact) if c}
        if verify_farkas(rows,target,multipliers):
            return multipliers,{**proposal,"exact_nonnegative_identity_verified":True}
    return None,{**proposal,"exact_support_reconstruction_failed":True}


def rational_outer_candidate(rows,n,budget):
    import numpy as np
    from scipy.optimize import linprog
    if n==0:return None,None
    arr=np.zeros((len(rows),n))
    for i,row in enumerate(rows):
        scale=max(abs(c) for c in row.values())
        for j,c in row.items():arr[i,j]=float(c/scale)
    for j in range(n):
        for sign in (1,-1):
            objective=np.zeros(n);objective[j]=-sign
            result=linprog(objective,A_ub=-arr,b_ub=np.zeros(len(rows)),bounds=[(-1,1)]*n,
                method="highs",options={"time_limit":min(10.,budget.remaining())})
            if not result.success or sign*result.x[j]<=1e-8:continue
            advisory={"coordinate":j,"sign":sign,"floating_objective":float(sign*result.x[j]),
                      "not_a_real_functional_or_positivity_certificate":True}
            for denominator in (1000,10**6,10**9):
                point=[F(float(x)).limit_denominator(denominator) for x in result.x]
                if any(point) and all(abs(x)<=1 for x in point) and all(apply_row(row,point)>=0 for row in rows):
                    return point,advisory
            active=[dict(row) for row,value in zip(rows,arr@result.x) if abs(value)<1e-8]
            rhs=[F(0)]*len(active)
            for i,value in enumerate(result.x):
                if abs(abs(value)-1)<1e-8:
                    active.append(unit(i));rhs.append(F(1 if value>0 else -1))
            preferred=[F(float(x)).limit_denominator(10**8) for x in result.x]
            point=solve_affine(active,rhs,n,preferred,budget)
            if (point is not None and any(point) and all(abs(x)<=1 for x in point)
                and all(apply_row(row,point)>=0 for row in rows)):
                return point,advisory
            return None,advisory
    return None,None


def certify_zero(system,budget):
    rows=system["reduced"].rows;n=len(system["free"]);certificates=[]
    if not n:
        return {"all_coordinates_forced_zero":True,"reason":"exact_equalities_alone",
                "certificates":[],"outer_candidate":None}
    if not rows:
        return {"all_coordinates_forced_zero":False,"reason":"no_nonzero_necessary_inequalities",
                "certificates":[],"outer_candidate":[str(F(i==0)) for i in range(n)]}
    for j in range(n):
        for sign in (1,-1):
            budget.check()
            target={j:F(sign)}
            certificate,proposal=rational_dual_proposal(rows,target,n,budget)
            if certificate is None:
                point,advisory=rational_outer_candidate(rows,n,budget)
                return {"all_coordinates_forced_zero":False,"reason":"not_all_exact_dual_identities_produced",
                    "certificates":certificates,"first_unproved_coordinate":j,
                    "first_unproved_sign":sign,"failed_proposal":proposal,
                    "outer_candidate":None if point is None else list(map(str,point)),
                    "candidate_is_only_for_the_necessary_outer_system":True,
                    "floating_advisory":advisory}
            certificates.append({"free_coordinate":j,"normal_coordinate":system["free"][j],"sign":sign,
                "nonnegative_multipliers":serial_row(certificate),"exact_target":serial_row(target),
                "original_reduced_rows_verified_exactly":True})
    return {"all_coordinates_forced_zero":True,"reason":"both_Farkas_signs_for_every_free_coordinate",
            "certificates":certificates,"outer_candidate":None}


def source_identity():
    here=Path(__file__).resolve()
    candidates=[here.parent/HEAD_DRIVER["filename"],
                here.parent.parent/"pending_derivative_factors"/HEAD_DRIVER["filename"]]
    producer=next((p for p in candidates if p.is_file()),None)
    if producer is None or identity(producer)!=HEAD_DRIVER:
        raise ValueError("frozen complete-head producer source missing or changed")
    return {"driver":identity(here),"consumed_complete_head_producer":HEAD_DRIVER,
            "profile_or_forcing_helpers_imported":False}


def read_json_bound(path,wanted,max_bytes=100000):
    raw=Path(path).read_bytes()
    if len(raw)>max_bytes or sha(raw)!=wanted:raise ValueError("bound small JSON identity changed")
    return json.loads(raw),raw


def check_publication(value,run,commit,lane,main_name,raw,metadata):
    if (value.get("schema")!="visible-new-mechanism-actions-v1"
        or value.get("repository")!=REPOSITORY or str(value.get("run_id"))!=run
        or value.get("source_commit")!=commit or value.get("lane")!=lane):
        raise ValueError("head publication run/source/lane changed")
    key="topics/visible-flex-new-mechanism/scripts/"+HEAD_DRIVER["filename"]
    if value.get("source_files",{}).get(key)!={k:HEAD_DRIVER[k] for k in ("bytes","sha256")}:
        raise ValueError("head publication producer binding changed")
    for name,wanted in (
        (main_name,{"bytes":len(raw),"sha256":sha(raw),"raw_bytes":len(raw),"raw_sha256":sha(raw)}),
        (metadata["filename"],{"bytes":metadata["stored_bytes"],"sha256":metadata["stored_sha256"],
                              "raw_bytes":metadata["raw_bytes"],"raw_sha256":metadata["raw_sha256"]})):
        found=[r for r in value.get("outputs",[]) if r.get("path")==name]
        if len(found)!=1 or any(found[0].get(k)!=v for k,v in wanted.items()):
            raise ValueError("head publication output binding changed")


def load_head(args,report):
    main,raw=read_json_bound(args.head_report,args.head_report_sha256)
    publication,praw=read_json_bound(args.head_publication,args.head_publication_sha256)
    metadata=main.get("portable_head_export") or {}
    if (main.get("schema")!=HEAD_SCHEMA or main.get("completion")!="complete"
        or main.get("head_generation_complete") is not True
        or main.get("source_hashes",{}).get("driver")!=HEAD_DRIVER
        or str(main.get("github_run_id"))!=args.head_run or main.get("github_sha")!=args.head_commit):
        raise ValueError("only a genuinely completed head presentation can be consumed")
    check_publication(publication,args.head_run,args.head_commit,args.head_lane,args.head_report.name,raw,metadata)
    packed=args.head_export.read_bytes()
    if (args.head_export.name!=metadata["filename"] or len(packed)!=metadata["stored_bytes"]
        or sha(packed)!=metadata["stored_sha256"] or len(packed)>4800000):
        raise ValueError("complete head gzip identity changed")
    with gzip.open(args.head_export,"rb") as stream:decoded=stream.read(40000001)
    if len(decoded)>40000000 or len(decoded)!=metadata["raw_bytes"] or sha(decoded)!=metadata["raw_sha256"]:
        raise ValueError("complete head raw identity changed")
    data=json.loads(decoded)
    if (data.get("schema")!=HEAD_SCHEMA+"-original-expressions"
        or data.get("content_scope")!="complete-fourteen-weight-minus2-families-and-translation-presentation"
        or data.get("all_fourteen_families_complete") is not True
        or data.get("all_planned_contractions_present") is not True
        or data.get("planned_contractions")!=data.get("completed_contractions")
        or data.get("target_weight")!=-2 or data.get("source_hashes")!=main.get("source_hashes")
        or str(data.get("github_run_id"))!=args.head_run or data.get("github_sha")!=args.head_commit):
        raise ValueError("partial or mismatched head artifact must not be used for positivity")
    report["input"]={"run":args.head_run,"commit":args.head_commit,"lane":args.head_lane,
        "main":{"filename":args.head_report.name,"bytes":len(raw),"sha256":sha(raw)},
        "publication":{"filename":args.head_publication.name,"bytes":len(praw),"sha256":sha(praw)},
        "export":metadata,"source_hashes":main["source_hashes"]}
    return data


def system_certificate(system,decision):
    return {"normal_coordinate_count":system["normal_coordinate_count"],
        "normal_coordinate_metadata":system["normal_coordinate_metadata"],
        "equalities":system["equalities"].records,
        "inequalities":system["inequalities"].records,
        "reduced_inequalities":system["reduced"].records,
        "rref_equalities":[{"pivot":p,"coefficients":serial_row(row)} for p,row in sorted(system["rref"].items())],
        "free_normal_coordinates":system["free"],
        "normal_coordinates_as_free_linear_forms":[serial_row(row) for row in system["transform"]],
        "normalized_multiplier":[serial_row(row) for row in system["mu"]],
        "translation_c":[serial_row(row) for row in system["c"]],
        "scaling_d":[serial_row(row) for row in system["d"]],
        "corrected_scalar_k_polynomials":{name:[[k,serial_row(row)] for k,row in sorted(poly.items())]
                                         for name,poly in system["kfamilies"].items()},
        "literal_original_relations":system["literal_proofs"],"complete_path_integrals":system["paths"],
        "decision":decision,"original_response_NF_or_profile_evaluation_performed":False,
        "all_true_positive_characters_embed_in_this_outer_system":True,
        "outer_system_feasibility_does_not_prove_a_true_character":True}


def toy_only():
    budget=Budget(45,512);checks={}
    # Whole-coordinate normalization: equalities parametrize all, not a single J value.
    basis,free,transform=rref([{0:F(1),1:F(-2)}],3,budget)
    assert free==[1,2] and transform[0]=={0:F(2)}
    checks["all_generating_coordinates_exactly_parameterized"]=True
    # A non-diagonal reference change must not confuse reference and E8 indices.
    fake={"reference_matrix":{"coordinate_order":list(PARAMETERS),
        "matrix_columns_are_reference_states":[[str(F(i==j)+(F(2) if (i,j)==(0,1) else 0)) for j in range(8)] for i in range(8)],
        "inverse":[[str(F(i==j)-(F(2) if (i,j)==(0,1) else 0)) for j in range(8)] for i in range(8)]},
        "static_translation_reference_coefficients":[{"reference_index":i,"coefficients":[[i,"1"]]} for i in range(8)],
        "static_scaling_reference_coefficients":[{"reference_index":i,"coefficients":[[i,"2"]]} for i in range(8)]}
    _,_,c,d,mu,_=reference_data(fake,8)
    assert c[1]=={0:F(-2),1:F(1)} and mu[1]=={0:F(-2),1:F(1)}
    checks["reference_derivatives_are_converted_to_E8_coordinates"]=True
    # All fourteen terms, at an artificial rational jet, have exactly the stated denominator cancellation.
    p,dp,ddp,dk,ddk=map(F,(2,3,5,7,11));rp=-2*dp/p
    z=6*dp*dp-2*p*ddp;r2=z/(p*p);area=-2*p*dp*ddk-dk*z
    a=F(1);bb=list(map(F,(2,3,4)));aa,ab,ac,h1,h2=map(F,(5,6,7,8,9));qq=list(map(F,range(10,15)))
    left=p**4*(a+sum(bb[i]*rp**i*dk**(2-i) for i in range(3))
        +aa*r2*r2+ab*r2*ddk+ac*ddk*ddk
        +(h1*rp+h2*dk)*(rp*ddk-dk*r2)
        +sum(qq[i]*rp**i*dk**(4-i) for i in range(5)))
    right=p**4*a+sum(bb[i]*(-2*dp)**i*p**(4-i)*dk**(2-i) for i in range(3))
    right+=aa*z*z+ab*p*p*z*ddk+ac*p**4*ddk*ddk+p*(-2*h1*dp+h2*p*dk)*area
    right+=sum(qq[i]*(-2*dp)**i*p**(4-i)*dk**(4-i) for i in range(5))
    assert left==right
    checks["all_fourteen_rational_path_terms_and_area_sign"]=True
    expected=pmul((F(0),F(0),F(0),F(140)),ppow((F(1),F(-1)),3))
    assert pdiff(RHO)==expected and peval(RHO,F(0))==0 and peval(RHO,F(1))==1
    assert all(peval(pdiff(pdiff(RHO)),x)==0 for x in (F(0),F(1)))
    checks["rho_monotonicity_and_finite_flat_endpoint_jets"]=True
    families={name:{} for name in FAMILIES}
    families["F0"]={0:unit(0)};families["A_hh"]={0:unit(1)};families["H1"]={0:unit(2)}
    a,b,cost,path=path_integrals(families,"1","0","1",budget)
    assert not b and a[0]>0 and cost[1]>0 and cost[2]>0
    assert tuple(map(F,path["D_coefficients"]))==padd((ppow(pdiff(RHO),3),-6))
    checks["artificial_path_integrals_keep_a_nonzero_area_contribution"]=True
    for t in TIMES:assert t*t-t+1>0
    checks["time_tests_allow_a_negative_middle_layer"]=True
    eq=RowTable(budget,True);iq=RowTable(budget)
    eq.add({0:F(-2)},{});iq.add({0:F(-2)},{})
    assert eq.rows==[{0:F(1)}] and iq.rows==[{0:F(-1)}]
    checks["inequality_normalization_never_reverses_its_sign"]=True
    toy_roots={"profile_atoms":[["jet","q",0]],"roots":{
        "r4":[[[0,[0]],1,1]],"r2":[],
        "n4":[[[0,[0]],2,1]],"n2":[]}}
    toy_roots["archived_R_basis_records"]=[{"original_column":i,"roots":{"-4":"r4","-2":"r2"}} for i in range(40)]
    normal=[{"index":0,"roots":{"-4":"n4","-2":"n2"}}]
    et=RowTable(budget,True);proofs=literal_original_relations(toy_roots,normal,et)
    assert et.rows==[{0:F(1)}] and proofs[0]["rational_ratio"]=="2"
    checks["literal_two_mode_R_proportionality_is_an_exact_relation"]=True
    rows=[{0:F(1)},{0:F(-1)},{1:F(1)},{1:F(-1)}]
    assert verify_farkas(rows,{0:F(-1)},{1:F(1)})
    assert not verify_farkas(rows,{0:F(-1)},{0:F(-1)})
    assert not verify_farkas(rows,{0:F(-1)},{0:F(1)})
    checks["Farkas_checker_rejects_negative_multipliers_and_wrong_targets"]=True
    result=certify_zero({"reduced":type("Rows",(),{"rows":rows})(),"free":[0,1]},budget)
    assert result["all_coordinates_forced_zero"] and len(result["certificates"])==4
    checks["floating_support_has_to_be_reconstructed_and_verified_over_Q"]=True
    result=certify_zero({"reduced":type("Rows",(),{"rows":[{0:F(1)}]})(),"free":[0]},budget)
    assert not result["all_coordinates_forced_zero"] and result["outer_candidate"] is not None
    checks["a_nonzero_outer_cone_is_not_falsely_excluded"]=True
    answer=solve_affine([{0:F(1),1:F(2)}],[F(3)],2,[F(0),F(1)],budget)
    assert answer==[F(1),F(1)]
    assert solve_affine([{0:F(1)},{0:F(1)}],[F(0),F(1)],1,[F(0)],budget) is None
    checks["exact_support_reconstruction_detects_inconsistent_equations"]=True
    metadata={"filename":"toy.gz","stored_bytes":4,"stored_sha256":"a"*64,"raw_bytes":8,"raw_sha256":"b"*64}
    raw=b"{}\n";source_key="topics/visible-flex-new-mechanism/scripts/"+HEAD_DRIVER["filename"]
    pub={"schema":"visible-new-mechanism-actions-v1","repository":REPOSITORY,"run_id":"toy",
         "source_commit":"c"*40,"lane":"toy","source_files":{source_key:{k:HEAD_DRIVER[k] for k in ("bytes","sha256")}},
         "outputs":[{"path":"toy.json","bytes":3,"sha256":sha(raw),"raw_bytes":3,"raw_sha256":sha(raw)},
                    {"path":"toy.gz","bytes":4,"sha256":"a"*64,"raw_bytes":8,"raw_sha256":"b"*64}]}
    check_publication(pub,"toy","c"*40,"toy","toy.json",raw,metadata)
    pub["outputs"][1]["raw_sha256"]="d"*64
    try:check_publication(pub,"toy","c"*40,"toy","toy.json",raw,metadata)
    except ValueError:pass
    else:raise AssertionError("a changed raw export SHA was accepted")
    checks["publication_binding_rejects_an_altered_raw_export"]=True
    return {"checks":checks,"all_passed":all(checks.values()),
            "real_head_or_profile_data_read":False,"research_coefficients_or_paths_evaluated":False,
            "artificial_rational_arithmetic_only":True}


def write_outputs(args,report,certificate):
    args.output.parent.mkdir(parents=True,exist_ok=True)
    if certificate is not None:
        raw=canonical(certificate);packed=gzip.compress(raw,mtime=0)
        if len(raw)>30000000 or len(packed)>args.max_certificate_bytes:
            raise Limit("complete necessary-system certificate output ceiling")
        path=args.output.with_name(args.output.stem+"-certificate.json.gz")
        path.write_bytes(packed)
        report["complete_necessary_certificate"]={"filename":path.name,"stored_bytes":len(packed),
            "stored_sha256":sha(packed),"raw_bytes":len(raw),"raw_sha256":sha(raw),
            "contains_all_exact_rows_and_Farkas_multipliers":True}
    compact=dict(report)
    data=canonical(compact)+b"\n"
    if len(data)>args.max_main_bytes and "input" in compact:
        bounded_input=dict(compact["input"])
        full_sources=bounded_input.pop("source_hashes",None)
        if full_sources is not None:
            bounded_input["source_hashes_bound_in_consumed_head_main"]={"sha256":sha(canonical(full_sources))}
        compact["input"]=bounded_input
        data=canonical(compact)+b"\n"
    if len(data)>=100000 or len(data)>args.max_main_bytes:
        raise Limit("compact main text ceiling")
    args.output.write_bytes(data)
    return {"output":str(args.output),"completion":report["completion"],"bytes":len(data),
            "sha256":sha(data),"positive_weight_minus2_character_excluded":report.get("positive_character_excluded",False)}


def actual(args,report,ctx,budget):
    report["phase"]="read_one_completed_original_character_head"
    data=load_head(args,report);budget.check()
    report["phase"]="construct_exact_normalized_necessary_rows"
    print(json.dumps({"phase":report["phase"]}),flush=True)
    system=construct_system(data,budget);del data
    ctx["system"]=system;ctx["decision"]=None
    report["system"]={"all_normal_coordinates":system["normal_coordinate_count"],
        "exact_external_equality_rows":len(system["equalities"].rows),
        "external_equality_rank":len(system["rref"]),"free_external_coordinates":len(system["free"]),
        "exact_necessary_inequality_rows":len(system["inequalities"].rows),
        "nonzero_distinct_reduced_rows":len(system["reduced"].rows),
        "literal_original_relations":len(system["literal_proofs"]),
        "fixed_polynomial_paths":len(PATHS),"positive_rational_t_values":list(map(str,TIMES)),
        "k_test_points":list(map(str,K_POINTS)),"PSD_rational_directions":[list(v) for v in PSD_DIRECTIONS],
        "external_rank_is_not_true_function_head_rank":True,
        "all_generating_coordinates_are_covered_by_the_zero_test":True}
    report["phase"]="propose_and_exactly_verify_finite_rational_dual_identities"
    print(json.dumps({"phase":report["phase"],**report["system"]}),flush=True)
    decision=certify_zero(system,budget);ctx["decision"]=decision
    excluded=decision["all_coordinates_forced_zero"]
    report.update(completion="complete",phase="finite_necessary_system_complete",
        positive_character_excluded=excluded,
        outcome=("all_true_positive_weight_minus2_characters_excluded_by_exact_outer_system"
                 if excluded else "finite_necessary_system_did_not_exclude_every_nonzero_coordinate"))
    report["decision"]={k:v for k,v in decision.items() if k not in ("certificates","outer_candidate")}
    report["decision"]["exact_dual_certificates"]=len(decision.get("certificates",[]))
    report["decision"]["nonzero_exact_outer_candidate_saved"]=decision.get("outer_candidate") is not None
    report["checkpoint"]={"target_weight":-2,"complete_head_consumed":True,
        "all_true_positive_characters_embed_in_the_test":True,
        "both_signs_of_all_free_coordinates_certified":excluded,
        "only_weight_minus2_excluded":excluded,"all_positive_characters_excluded":False,
        "true_character_existence_claimed":False,"complete_period_or_ruling_paid":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    for name in ("head-report","head-publication","head-export"):
        parser.add_argument("--"+name,type=Path)
    for name in ("head-report-sha256","head-publication-sha256","head-run","head-commit","head-lane"):
        parser.add_argument("--"+name)
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--rational-bits",type=int,default=16384)
    parser.add_argument("--max-main-bytes",type=int,default=95000)
    parser.add_argument("--max-certificate-bytes",type=int,default=4500000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.rational_bits,args.max_main_bytes,args.max_certificate_bytes)<=0:
        parser.error("positive explicit resource/output budgets required")
    if args.max_main_bytes>=100000 or args.max_main_bytes+args.max_certificate_bytes>4800000:
        parser.error("main <100KB and total published outputs <=4.8MB")
    inputs=[args.head_report,args.head_publication,args.head_export,args.head_report_sha256,
            args.head_publication_sha256,args.head_run,args.head_commit,args.head_lane]
    if not args.toy_only and not all(inputs):
        parser.error("actual consumption requires complete published head run/source/main/receipt/export binding")
    if not args.toy_only and (os.environ.get("GITHUB_ACTIONS")!="true"
                              or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        parser.error("all real head/path-integration/LP research only in this public repository Actions")
    started=time.monotonic();budget=Budget(args.max_seconds,args.memory_mib,args.rational_bits)
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),"github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "github_sha":os.environ.get("GITHUB_SHA"),"target_weight":-2,"source_hashes":{},
        "limits":{"elapsed_seconds":args.max_seconds,"polled_memory_mib":args.memory_mib,
            "rational_bit_ceiling":args.rational_bits,"main_bytes":args.max_main_bytes,
            "complete_certificate_bytes":args.max_certificate_bytes},
        "positive_character_excluded":False,"complete_action_positivity_proved":False,
        "function_space_head_rank_computed":False,"old_basis_or_forcing_recomputed":False,
        "profile_values_or_geometry_ODE_evaluated":False,"old_normal_forms_recomputed":False,
        "new_rational_state_path_integrals_permitted_only_in_actual":True,
        "floating_status_is_never_a_mathematical_certificate":True}
    ctx={};code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["toy"]=toy_only();report.update(completion="toy_passed",phase="new_artificial_interfaces_only")
        else:actual(args,report,ctx,budget)
    except Limit as error:
        code=2;report.update(completion="resource_limit",error=str(error))
    except Exception as error:
        code=1;report.update(completion="implementation_check_failed",
            error={"type":type(error).__name__,"message":str(error)})
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    certificate=None
    if "system" in ctx:
        certificate={"schema":SCHEMA+"-certificate","source_hashes":report["source_hashes"],
            "input":report.get("input"),"target_weight":-2,
            **system_certificate(ctx["system"],ctx.get("decision"))}
    try:written=write_outputs(args,report,certificate)
    except Limit as error:
        report.update(completion="output_limit",error=str(error),positive_character_excluded=False,
            mathematical_exclusion_not_claimed_without_complete_saved_certificate=True)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        failed={k:report[k] for k in ("schema","completion","phase","github_repository",
            "github_run_id","github_sha","source_hashes","target_weight","elapsed_seconds",
            "peak_rss_mib","error") if k in report}
        failed.update(positive_character_excluded=False,
            mathematical_exclusion_not_claimed_without_complete_saved_certificate=True)
        if "input" in report:
            failed["input_identity_sha256"]=sha(canonical(report["input"]))
        raw=canonical(failed)+b"\n";args.output.write_bytes(raw)
        written={"output":str(args.output),"completion":"output_limit","bytes":len(raw),"sha256":sha(raw)}
        code=2
    print(json.dumps(written),flush=True)
    return code


if __name__=="__main__":
    raise SystemExit(main())
