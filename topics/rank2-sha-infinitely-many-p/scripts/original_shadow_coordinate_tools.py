#!/usr/bin/env sage-python
"""Consume the SAME original PASS receipts and the R882 RR front.

No q-prefix is used as an existence certificate.  This module is the explicit
R881 low-kernel reader of two characteristic-zero maps already certified by
their full original elliptic identities.  It keeps actual RR functions and
returns them in process for the relative degree-18 source consumer.
"""
import os
if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import importlib.util
import json
import time
from pathlib import Path
from sage.all import (GF, FunctionField, PolynomialRing, PowerSeriesRing,
                      matrix, vector)

STARTED=time.monotonic()

def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=True)

def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()

def progress(stage,**kw):
    print("RANK2_SHADOW_COORD_STAGE "+canonical(dict(
        stage=stage,elapsed_seconds=time.monotonic()-STARTED,**kw)),flush=True)

def _import_file(stem,name):
    path=Path(__file__).with_name(stem)
    spec=importlib.util.spec_from_file_location(name,str(path))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def certificate_weight(receipt,kind):
    if kind=="P":
        flag="certified_original_map"
        status="certified_original_rational_hecke_hom"
        weights=(4,6)
    else:
        assert kind=="F"
        flag="certified_original_first_factor"
        status="certified_original_first_factor"
        weights=(2,4)
    assert receipt.get(flag) is True, "The SAME original char-zero certificate must have passed."
    assert receipt.get("source") and receipt.get("run_id")
    cases=[c for c in receipt["cases"] if c.get("status")==status]
    assert len(cases)==1
    case=cases[0]
    k=int(case["weight"])
    assert k in weights
    assert case["last_exact_certificate"]["full_0_through_bound_identity"] is True
    return k

def map_rational(a,image,target):
    return target(a.numerator()(image))/target(a.denominator()(image))

def map_simple_function(f,timage,Timage,target):
    ans=target.zero()
    for a in reversed(f.list()):
        ans=ans*Timage+map_rational(a,timage,target)
    return ans

def constant_extension(context,k2):
    assert context["model"]=="eta48"
    B=context["field"]
    K2=FunctionField(k2,"t_eta")
    t=K2.gen()
    P=PolynomialRing(K2,"T")
    co=[map_rational(a,t,K2) for a in B.polynomial().list()]
    B2=K2.extension(P(co),"T")
    T=B2.gen()
    tt=B2(t)
    def inject(f):
        return map_simple_function(f,tt,T,B2)
    assert inject(B.gen())==T
    return B2,tt,T,inject

def prime_residue(z,fp):
    assert z**int(fp.cardinality())==z
    co=z.polynomial().list()
    assert all(c==0 for c in co[1:])
    return fp(co[0]) if co else fp.zero()

def row_serial(row):
    out=[]
    for z in row:
        co=z.polynomial().list()
        out.append([int(c) for c in co])
    return out

def extend_actual_M2(context,precision):
    k=context["constants"]
    ev=context["tate_evaluator"]
    bas=context["rr_bases"][1]
    raw=[ev.term_lower_bound(a,i) for f in bas
         for i,a in enumerate(f.list()) if a]
    ev.prepare(max(1,int(precision)-min(raw,default=0)))
    rows=[]
    progress("same actual M2 RR jets",precision=int(precision),dimension=len(bas))
    for i,f in enumerate(bas):
        row,_=ev.expansion(f,precision)
        rows.append(row)
        if i%8==7 or i+1==len(bas):
            progress("same M2 Tate rows",completed=i+1,total=len(bas))
    assert len(bas)==120 and matrix(k,[r[:205] for r in rows]).rank()==120
    old=context["rr_jets"][1]
    assert all(rows[i][:old.ncols()]==list(old.row(i)) for i in range(120))
    return rows

def complete_product_recipes(context,rows2,maximum_power,precision):
    """Actual finite-field rank selects full L(mD) products; no assumed span."""
    k=context["constants"]
    recipes={1:[(i,) for i in range(120)]}
    SS=PowerSeriesRing(k,"Q",default_prec=precision)
    two=[SS(r).add_bigoh(precision) for r in rows2]
    series={1:two}
    for m in range(2,maximum_power+1):
        sturm=204*m+1
        expected=204*m-84
        assert precision>=sturm
        selected,selected_rows,seen=[],[],set()
        prev=series[m-1]
        for i in range(120):
            batch_recipes,batch_rows=[],[]
            for rr,ss in zip(recipes[m-1],prev):
                rrnew=tuple(sorted((i,)+rr))
                if rrnew in seen:
                    continue
                seen.add(rrnew)
                ps=(two[i]*ss).add_bigoh(sturm)
                batch_recipes.append(rrnew)
                batch_rows.append([ps[j] for j in range(sturm)])
            if not batch_rows:
                continue
            all_recipes=selected+batch_recipes
            all_rows=selected_rows+batch_rows
            pivots=tuple(matrix(k,all_rows).transpose().pivots())
            selected=[all_recipes[j] for j in pivots]
            selected_rows=[all_rows[j] for j in pivots]
            progress("actual RR product rank",power=m,weight=2*m,
                     rank=len(selected),expected=expected,batches=i+1)
            if len(selected)==expected:
                break
        assert len(selected)==expected, "Actual products did not give the full required RR space."
        recipes[m]=selected
        output=[]
        for rr in selected:
            ps=SS.one().add_bigoh(precision)
            for i in rr:
                ps*=two[i]
            output.append(ps.add_bigoh(precision))
        series[m]=output
        assert matrix(k,[[p[j] for j in range(sturm)] for p in output]).rank()==expected
    return recipes,series

def canonical_kernel(M,split):
    """Choose one exact finite-field kernel vector; ratio uniqueness is R881."""
    E=M.echelon_form()
    piv=tuple(E.pivots())
    assert len(piv)<M.ncols(), "The certified map must have a nonzero reduced ratio kernel."
    free=next(j for j in range(M.ncols()) if j not in set(piv))
    sol=vector(M.base_ring(),M.ncols())
    sol[free]=1
    for i,j in enumerate(piv):
        sol[j]=-E[i,free]
    assert (M*sol).is_zero()
    assert any(sol[j]!=0 for j in range(split,len(sol)))
    return sol,dict(rank=len(piv),nullity=M.ncols()-len(piv),
                    free_column=free,solution_sha256=digest(row_serial(sol)))

def solve_packet(series,local_row,weight,field):
    L=204*weight+1
    N=L+1
    R=PowerSeriesRing(field,"Q",default_prec=N)
    ss=[R([field(s[i]) for i in range(N)]).add_bigoh(N)
        for s in series[weight//2]]
    yy=R([field(z) for z in local_row[:N]]).add_bigoh(N)
    ys=[(yy*s).add_bigoh(N) for s in ss]
    dim=len(ss)
    M=matrix(field,N,2*dim,lambda i,j:
        ((field.zero() if i==0 else ss[j][i-1])
           if j<dim else -ys[j-dim][i]))
    sol,meta=canonical_kernel(M,dim)
    AA=sum((sol[j]*ss[j] for j in range(dim)),R.zero())
    BB=sum((sol[dim+j]*ss[j] for j in range(dim)),R.zero())
    assert BB!=0 and BB.valuation()>=1
    assert AA.valuation()==BB.valuation()-1
    assert (R.gen()*AA-yy*BB).add_bigoh(N)==0
    meta.update(kind="P",weight=weight,last_QY_index=L,
                B_order=int(BB.valuation()))
    return sol,meta

def solve_first(series,local_row,weight,field):
    L=204*weight+612
    N=L+1
    R=PowerSeriesRing(field,"Q",default_prec=N)
    aa=[R([field(s[i]) for i in range(N)]).add_bigoh(N)
        for s in series[(weight+6)//2]]
    bb=[R([field(s[i]) for i in range(N)]).add_bigoh(N)
        for s in series[weight//2]]
    yy=R([field(z) for z in local_row[:N]]).add_bigoh(N)
    yb=[(yy*s).add_bigoh(N) for s in bb]
    da,db=len(aa),len(bb)
    M=matrix(field,N,da+db,lambda i,j:
             aa[j][i] if j<da else -yb[j-da][i])
    sol,meta=canonical_kernel(M,da)
    AA=sum((sol[j]*aa[j] for j in range(da)),R.zero())
    BB=sum((sol[da+j]*bb[j] for j in range(db)),R.zero())
    assert BB!=0 and AA.valuation()==BB.valuation()
    assert (AA-yy*BB).add_bigoh(N)==0
    meta.update(kind="F",weight=weight,last_index=L,B_order=int(BB.valuation()))
    return sol,meta

def actual_function_from_solution(sol,ar,br,two,target,cache):
    def product(recipe):
        if recipe not in cache:
            cache[recipe]=product(recipe[:-1])*two[recipe[-1]]
        return cache[recipe]
    da=len(ar)
    A=sum((target(sol[i])*product(rr) for i,rr in enumerate(ar) if sol[i]),target.zero())
    B=sum((target(sol[da+i])*product(rr) for i,rr in enumerate(br) if sol[da+i]),target.zero())
    assert B!=0
    return A/B

def generalized_eta_evaluator(front,k):
    class E(front.Eta48TateEvaluator):
        def eval_unit_polynomial(self,p):
            key=tuple(str(c) for c in p.list())
            if key not in self.cache:
                self.cache[key]=p(self.tseries)
            return self.cache[key]
    return E(k)

def original_cube_root(B,value,evaluator,label):
    P=PolynomialRing(B,"cube_root")
    zz=P.gen()
    fac=(zz**3-value).factor()
    candidates=[]
    for ff,mm in fac:
        assert mm==1
        if ff.degree()==1:
            root=-ff[0]/ff[1]
            row,_=evaluator.expansion(root,1)
            if row[0]==1:
                candidates.append(root)
    assert len(candidates)==1, "Keep the unique original cusp cube root, not an arbitrary branch."
    root=candidates[0]
    assert root**3==value
    progress("original cube branch",source=label,linear_factors=sum(f.degree()==1 for f,m in fac))
    return root

def build_reduced_maps(rr,local,first_certificate,packet_certificate):
    assert rr["prime"]==local["prime"] and rr["model"]=="eta48"
    kP=certificate_weight(packet_certificate,"P")
    kF=certificate_weight(first_certificate,"F")
    precision=max(204*kP+2,204*kF+613)
    assert len(local["first"]["vF"])>=204*kF+613
    assert len(local["packet"][0]["QY"])>=204*kP+2
    assert len(local["packet"][1]["QY"])>=204*kP+2
    maxpower=max(kP//2,(kF+6)//2)
    rows2=extend_actual_M2(rr,precision)
    recipes,series=complete_product_recipes(rr,rows2,maxpower,precision)
    fp=rr["constants"]
    k2=local["constants"]
    B2,tt,T,inject=constant_extension(rr,k2)
    two=[inject(f) for f in rr["rr_bases"][1]]
    cache={():B2.one()}
    front=_import_file("produce-original-shadow-rr-eta48.py","original_shadow_eta48_reader")
    evaluator=generalized_eta_evaluator(front,k2)

    progress("original F finite low kernel",weight=kF)
    firstrow=[prime_residue(z,fp) for z in local["first"]["vF"]]
    fsol,fmeta=solve_first(series,firstrow,kF,fp)
    vF=actual_function_from_solution(
        fsol,recipes[(kF+6)//2],recipes[kF//2],two,B2,cache)
    D=T**3/(T+27)**4
    RF=original_cube_root(B2,(vF**2-17*D)/(D*(T+27)),evaluator,"F")
    pcoords={}
    pmetadata=[]
    for i in (0,1):
        progress("original P finite low kernel",embedding=i,weight=kP)
        field=fp if i==0 else k2
        row=([prime_residue(z,fp) for z in local["packet"][0]["QY"]]
             if i==0 else local["packet"][1]["QY"])
        psol,pmeta=solve_packet(series,row,kP,field)
        Y=actual_function_from_solution(
            psol,recipes[kP//2],recipes[kP//2],two,B2,cache)
        vv=B2(local["packet"][i]["vnew"])
        RP=original_cube_root(B2,Y*(Y+vv)/(T+27)**2,evaluator,"P_"+str(i))
        pcoords[i]={"Y":Y,"R":RP,"vnew":vv,
                    "a17":local["packet"][i]["a17"],
                    "lambda":local["packet"][i]["lambda"],
                    "v":local["packet"][i]["v"]}
        pmetadata.append(dict(embedding=i,**pmeta))
    # The second non-real embedding is actual constant-field conjugation.
    # It is not the original point-factor Artin operator.
    frob=k2.hom([k2.gen()**rr["prime"]])
    cfrob=B2.hom([B2.gen(),B2(B2.base_field().gen())],base_morphism=frob)
    pcoords[2]={key:(cfrob(val) if key in ("Y","R","vnew") else val**rr["prime"])
                for key,val in pcoords[1].items()}
    assert pcoords[2]["a17"]==local["a_roots"][2]
    assert pcoords[2]["R"]**3==pcoords[2]["Y"]*(
        pcoords[2]["Y"]+pcoords[2]["vnew"])/(T+27)**2
    # Retain an independent low-germ check if the third input was generated.
    if 2 in local["packet"]:
        Y=pcoords[2]["Y"]
        # QY regularity is checked via the already selected denominator kernel:
        assert [z**rr["prime"] for z in local["packet"][1]["QY"]]==local["packet"][2]["QY"]

    out={"prime":rr["prime"],"constants":k2,"field":B2,"t_eta":tt,"T":T,
         "U":inject(rr["U"]),"V":inject(rr["V"]),
         "base_injection":inject,"F":{"v":vF,"R":RF},
         "P":pcoords,"sigma_a_index":local["sigma_a_index"],
         "original_a_roots":local["a_roots"],"omega":local["omega"],
         "first_certificate":first_certificate,"packet_certificate":packet_certificate}
    summary={"kind":"rank2_original_good_prime_reduced_maps",
             "status":"certified_original_reductions",
             "prime":rr["prime"],"model":"eta48","P_weight":kP,"F_weight":kF,
             "first_source":first_certificate["source"],"first_run":first_certificate["run_id"],
             "packet_source":packet_certificate["source"],"packet_run":packet_certificate["run_id"],
             "first_kernel":fmeta,"packet_kernels":pmetadata,
             "CM_embedding_order":"a0 in F_r, then omega*a0, omega^2*a0; original sigma retained separately",
             "all_original_cube_branches_selected_at_infinity":True,
             "source_level":10404,"packet_level":2601,"RR_base_level":867,
             "original_shadow_computed":False}
    return out,summary
