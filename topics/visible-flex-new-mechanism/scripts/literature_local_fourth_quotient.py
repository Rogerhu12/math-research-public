#!/usr/bin/env python3
"""R109 local fourth density with true derivatives before zero histories.

The first bounded research target is geometry-derivative weight zero.
No old constant-pair target or full fourth history forcing is compiled.
--toy-only runs small artificial algebra/IO checks, not a research target.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

import literature_colored_profile_algebra as colored
import literature_closed_c1_endpoint as endpoint
import literature_full_phase_bridge_exact as producer
import literature_full_phase_rational_dual as dual
import literature_local_third_bridge_decompose as local
import literature_pure_bulk_exact_membership as exact
import literature_range_profile_algebra as formal
import literature_total_P1_scaling_blocks as blocks

SCHEMA="visible-flex-R109-local-fourth-quotient-static-v1"
TOTAL_OUTPUT_BYTES=4800000
MODES=(-4,-2)
GZERO=(0,)*8

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()

def sha(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def dependencies():
    result=producer.dependencies()
    if result["driver"]["sha256"]!=dual.PRODUCER_SHA:
        raise ValueError("explicitly rebind the original colored decomposition source")
    result["v2_producer"]=result.pop("driver")
    for name,module in (("endpoint",endpoint),("dual_receipt_reader",dual),("scaling_interfaces",blocks)):
        result[name]=dual.file_identity(module.__file__)
    result["driver"]=dual.file_identity(__file__)
    return result

def jet_weight(key):
    return key[local.V]+key[local.W]+2*key[local.HV]+2*key[local.KW]

class ZeroStateCoefficients:
    """Specialize only after required real derivatives have been compiled."""
    def __init__(self,algebra,static=True):
        self.a,self.c=algebra,algebra.c
        self.static,self.cache=static,{}
        self.histories_seen=set()
    def node(self,index):
        if index in self.cache:
            return self.cache[index]
        self.a.budget.time_check()
        value=self.c.nodes[index]
        tag=value[0]
        if tag=="st":
            self.histories_seen.add(value[1]);out=self.c.zero
        elif tag=="c":
            out=index
        elif tag=="g":
            out=self.c.zero if self.static and value[2] else index
        elif tag=="add":
            out=self.c.linear((F(n,d),self.node(child)) for child,n,d in value[1])
        elif tag=="mul":
            out=self.c.multiply(self.c.constant(F(value[1],value[2])),
                self.c.multiply_powers((self.node(child),power) for child,power in value[3]))
        else:
            raise ValueError(("unknown coefficient node",value))
        self.cache[index]=out
        return out
    def expression(self,value):
        return formal.Separated(self.a,{m:self.node(c) for m,c in value.terms.items()})
    def field(self,field):
        # cov() resolves the actual state_rhs before the zero-value map.
        components,dx,cov=field.components,field.dx(),field.cov()
        cov_dx=tuple(x.dx() for x in cov)
        return {"value":tuple(self.expression(x) for x in components),
            "dx":tuple(self.expression(x) for x in dx),
            "cov":tuple(self.expression(x) for x in cov),
            "cov_dx":tuple(self.expression(x) for x in cov_dx)}

def local_forcing(compiler,pairs,specializer):
    """R56 R with true J_s and (T_xi)_s computed using covariant products."""
    zero,c=compiler.zero,compiler.a.c
    J,Tx,Ts,Js,Txs=zero,zero,zero,zero,zero
    for weight,left,right in pairs:
        J=J.add(compiler.dot(left["value"],right["value"]).scale(weight))
        Tx=Tx.add(compiler.dot(left["dx"],right["dx"]).scale(weight))
        Ts=Ts.add(compiler.dot(left["cov"],right["cov"]).scale(weight))
        Js=Js.add(compiler.dot(left["cov"],right["value"]).add(
            compiler.dot(left["value"],right["cov"])).scale(weight))
        Txs=Txs.add(compiler.dot(left["cov_dx"],right["dx"]).add(
            compiler.dot(left["dx"],right["cov_dx"])).scale(weight))
    h,gamma=specializer.node(compiler.h),specializer.node(compiler.gamma)
    ih,ih2=c.power(h,-1),c.power(h,-2)
    B=J.coefficient(ih).scale(F(1,2))
    P=Tx.primitive().coefficient(ih).scale(F(-1,2))
    Bs=Js.coefficient(ih).scale(F(1,2)).add(
        B.coefficient(c.multiply(gamma,ih)).scale(-1))
    Ps=Txs.primitive().coefficient(ih).scale(F(-1,2)).add(
        P.coefficient(c.multiply(gamma,ih)).scale(-1))
    k=specializer.node(compiler.k)
    K0,lam,z=map(specializer.expression,(compiler.K0,compiler.lam,compiler.z))
    R=Ts.coefficient(ih2).scale(F(1,2)).add(
        K0.multiply(P),lam.multiply(Ps).scale(-1),
        z.coefficient(k).add(compiler.a.scalar(
            c.multiply(c.add(c.power(k,2),c.one),ih)).scale(-1)).multiply(B),
        Bs.coefficient(c.multiply(gamma,ih2)).scale(-1))
    return {"period_rhs":R,"ruling_integrand":Tx,"P":P,"B":B,"P_s":Ps,"B_s":Bs}

def compile_static_local_v(ring,report):
    """Restore original lower fields only; do not compile old fourth roots."""
    comp=local.SharedCompiler(ring.algebra)
    A=comp.initial("q")
    B,_=comp.forcing_range([(1,A,A)],2,"R109_B",True)
    U,_=comp.forcing_range([(1,A,B)],3,"R109_U",True)
    V,_=comp.forcing_range([(1,A,B.conjugate())],3,"R109_V",True)
    state_count=len(ring.algebra.c.state_rhs)
    fields={"A":A,"Ab":A.conjugate(),"B":B,"Bb":B.conjugate(),
        "U":U,"Ub":U.conjugate(),"V":V,"Vb":V.conjugate()}
    for field in fields.values():
        field.cov()
    zero=ZeroStateCoefficients(ring.algebra,static=True)
    values={name:zero.field(field) for name,field in fields.items()}
    pairs={"P":("B","B"),"Q":("B","Bb"),"R":("A","U"),
        "S":("A","V"),"T":("A","Vb"),"J":("Ab","U")}
    output={name:local_forcing(comp,[(1,values[a],values[b])],zero)["period_rhs"]
        for name,(a,b) in pairs.items()}
    combinations={
        -4:[("P",F(-1,16)),("R",F(-1,4))],
        -2:[("P",F(1,8)),("Q",F(1,8)),("R",F(1,4)),("S",F(1,4)),
            ("T",F(-1,4)),("J",F(-1,4))]}
    expansion=local.GeometryExpansion(ring.algebra,ring.limits)
    result={}
    for mode,terms in combinations.items():
        raw=comp.zero.add(*(output[name].scale(c) for name,c in terms))
        result[mode]=expansion.separated(raw,ring)
        if any(jet_weight(key) or key[local.LH] for key in result[mode].terms):
            raise AssertionError("static derivative-weight projection failed")
        if any(ring.p.weight(m)!=4 for value in result[mode].terms.values() for m in value.terms):
            raise AssertionError("full local fourth profile degree")
    report["local_v_compilation"]={
        "original_lower_order_records":comp.records,
        "compiled_real_lower_state_count":state_count,
        "state_count_after_local_fourth":len(ring.algebra.c.state_rhs),
        "new_fourth_history_states":len(ring.algebra.c.state_rhs)-state_count,
        "specialized_history_values":len(zero.histories_seen),
        "full_old_fourth_forcing_compiled":False,
        "history_derivatives_specialized_to_zero":False,
        "differentiate_before_specialize":True,
        "period_modes":{str(mode):value.summary() for mode,value in result.items()}}
    if report["local_v_compilation"]["new_fourth_history_states"]:
        raise AssertionError("local target introduced fourth histories")
    return result

class ScalarGeo:
    """Small exact Laurent algebra for the already proved R73 matrix formula."""
    def __init__(self,terms=None):
        self.terms={tuple(k):F(v) for k,v in (terms or {}).items() if v}
    @classmethod
    def number(cls,value):
        return cls({GZERO:F(value)})
    @classmethod
    def variable(cls,index):
        key=list(GZERO);key[index]=1
        return cls({tuple(key):F(1)})
    def __add__(self,other):
        other=other if isinstance(other,ScalarGeo) else self.number(other)
        return ScalarGeo(local.sadd(self.terms,other.terms))
    __radd__=__add__
    def __neg__(self):
        return ScalarGeo({k:-v for k,v in self.terms.items()})
    def __sub__(self,other):
        return self+(-other if isinstance(other,ScalarGeo) else -F(other))
    def __rsub__(self,other):
        return -self+other
    def __mul__(self,other):
        other=other if isinstance(other,ScalarGeo) else self.number(other)
        out={}
        for a,c in self.terms.items():
            for b,d in other.terms.items():
                key=local.gmul(a,b);out[key]=out.get(key,F(0))+c*d
        return ScalarGeo(out)
    __rmul__=__mul__
    def __truediv__(self,other):
        return self*(other**-1) if isinstance(other,ScalarGeo) else self*(1/F(other))
    def __pow__(self,n):
        if n<0:
            if len(self.terms)!=1:
                raise ValueError("only a nonzero Laurent monomial may be inverted")
            key,value=next(iter(self.terms.items()))
            return ScalarGeo({tuple(n*x for x in key):value**n})
        result=self.number(1)
        for _ in range(n):
            result=result*self
        return result

def pointwise_matrix():
    h,k,o,hs,ks=(ScalarGeo.variable(i) for i in (local.H,local.K,local.O,local.V,local.W))
    d=h*o-k;ds=hs*o-ks/2;Q=1+d*d
    a0=k*o*o-(k*k+1)*o/h
    a1=2*k*o-(k*k+1)/h
    lam0,lam1=ds/(h*h),hs/(h*h)
    delta=hs*Q/h-2*d*ds
    result=[-k*Q/(2*h),-k*d,-k*h/2,
        (a0*Q+lam0*delta)/(8*h),(a1*Q+lam1*delta)/(8*h),
        (a0*d-lam0*ds)/4,(a1*d-lam1*ds)/4,(h*a1-hs*lam1)/8]
    if any(jet_weight(key) not in (0,2) for item in result for key in item.terms):
        raise AssertionError("raw matrix derivative weights")
    return result

def restore_bound_W(ring,receipt,pieces,normalizer):
    """Return the byte-bound published 36 templates, with no endpoint target."""
    all_templates,labels,_=producer.control_templates(ring,pieces,normalizer)
    recorded=receipt["all_original_control_templates"]
    if len(labels)!=len(recorded):
        raise AssertionError("published 152 original full-third templates changed")
    for found,want in zip(labels,recorded):
        if found["original_template_sha256"]!=want["original_template_sha256"]:
            raise AssertionError("original third template hash changed")
    kept=receipt["pre_response_reduction"]["retained_original_indices"]
    if kept!=blocks.EXPECTED_KEPT:
        raise AssertionError("published complete W basis changed")
    templates=[all_templates[i] for i in kept]
    binding={"receipt_sha256":dual.RECEIPT_SHA,"run_id":"43633746055",
        "retained_original_indices":kept,
        "raw_template_hashes":[ring.digest(x) for x in templates],
        "original_152_hashes_matched":True,"old_116_relations_recomputed":False,
        "true_dimension_source":"published original dependencies and R87 exact original evaluation minor"}
    return templates,binding

def restore_third_and_potential(ring,receipt,report,bound_callback=None):
    normalizer=colored.ColoredNormalizer(ring)
    density,records,count=producer.compile_colored_local(ring)
    pieces=producer.raw_decomposition(density,normalizer)
    templates,binding=restore_bound_W(ring,receipt,pieces,normalizer)
    report["bound_W"]={**binding,"colored_records_sha256":sha(records),"expanded_local_nodes":count}
    if bound_callback is not None:
        bound_callback(templates)
    vectors=[producer.third_vector(value,normalizer) for value in templates]
    span=colored.JointSpan(vectors,ring.limits)
    if len(span.independent)!=36:
        raise AssertionError("bound independent W columns lost rank")
    rawN=(pieces["potential_acc"]+pieces["potential_h"]
        +endpoint.endpoint_potential(pieces["residual_k"],h_base=1,k_base=1,omega_base=1))
    staticN=local.GExpr(ring,{key:value for key,value in rawN.terms.items() if jet_weight(key)==0})
    reduced,certificates={},[]
    fresh=colored.ColoredNormalizer(ring)
    for key,value in sorted(staticN.terms.items()):
        coefficients,residual=span.reduce(producer.third_vector(value,normalizer))
        representative=producer.third_from_vector(residual,normalizer)
        original=value-representative-sum((c*templates[j] for j,c in coefficients.items()),ring.number(0))
        check=fresh.word.expression(original)
        if check.terms:
            raise AssertionError("local N quotient used an unproved original third identity")
        if representative.terms:
            reduced[key]=representative
        certificates.append({"geometry_key":list(key),"raw_sha256":ring.digest(value),
            "representative_sha256":ring.digest(representative),
            "true_W_coefficients":[[j,str(c)] for j,c in sorted(coefficients.items())],
            "fresh_original_difference_zero_sha256":check.digest()})
    result=local.GExpr(ring,reduced)
    report["local_N_potential"]={
        "formula":"P_acc + P_h + raw R79 F*(k,omega), base (1,1,1)",
        "pointwise_mod_W_source":"R109 section 2; full colored R77/R79 actual coefficient identities",
        "same_right_anchor":True,"raw_all_weight_summary":rawN.summary(),
        "raw_static_summary":staticN.summary(),"reduced_static_summary":result.summary(),
        "constant_potential_was_set_zero":False,
        "coefficient_reconstruction_certificates":certificates,
        "reduction_changes_local_density_only_by_R8":True}
    report["bound_W"]["coefficient_span_representative_rank"]=len(span.independent)
    return templates,result

def build_local_density(ring,localv,N,report):
    zero=ring.number(0)
    target={mode:dict(expr.terms) for mode,expr in localv.items()}
    matrix=pointwise_matrix()
    basis=exact.operator_basis(ring)
    cache={};count=0
    for index,coordinate in enumerate(matrix):
        coefficients={key:value for key,value in coordinate.terms.items() if jet_weight(key)==0}
        if not coefficients:
            continue
        for nkey,template in N.terms.items():
            token=(index,template.key())
            if token not in cache:
                cache[token]=blocks.full_response(ring,colored.ThirdOperator(ring,template),basis[index])
            for mkey,scalar in coefficients.items():
                key=local.gmul(nkey,mkey)
                for mode,value in cache[token].items():
                    target[mode][key]=target[mode].get(key,zero)-scalar*value
                count+=1
    answer={mode:local.GExpr(ring,rows) for mode,rows in target.items()}
    report["local_density"]={
        "formula":"v^[0] - sum_i m_i^[0] B_Ei(N^[0]_representative)",
        "projection":"geometry derivative weight 0 only; not all derivative weights",
        "same_complete_two_modes":True,"pointwise_matrix_source":"R73 equations (6),(9),(10)",
        "static_matrix_coefficients":[[[list(key),str(value)] for key,value in sorted(item.terms.items())
            if jet_weight(key)==0] for item in matrix],
        "distinct_quadratic_potential_responses":len(cache),"geometry_products":count,
        "mode_summary":{str(mode):value.summary() for mode,value in answer.items()},
        "lower_history_solved_or_reset":False,"ruling_removed":False}
    return answer

def zero_modes(ring):
    return {mode:ring.number(0) for mode in MODES}

def serialize_expressions(ring,named):
    """Original reachable atom DAG; portable without any research recompile."""
    seen=set()
    def visit(monomial):
        for index in monomial[1]:
            if index in seen:
                continue
            node=ring.p.atoms[index]
            if node[0]=="int_right":
                visit(node[1])
            elif node[0]!="jet":
                raise ValueError("unexpected profile atom")
            seen.add(index)
    for value in named.values():
        for monomial in value.terms:
            visit(monomial)
    ordered=sorted(seen);positions={old:new for new,old in enumerate(ordered)}
    def monomial(value):
        return [value[0],[positions[i] for i in value[1]]]
    atoms=[]
    for old in ordered:
        node=ring.p.atoms[old]
        if node[0]=="jet":
            atoms.append(list(node))
        else:
            if any(positions[i]>=positions[old] for i in node[1][1]):
                raise AssertionError("original right primitive DAG not topological")
            atoms.append(["int_right",monomial(node[1])])
    roots={name:[[monomial(m),v.numerator,v.denominator] for m,v in sorted(value.terms.items())]
        for name,value in sorted(named.items())}
    return {"anchor":"I(F)=integral_r^xi F; all input colors zero on the same right collar",
        "profile_atoms":atoms,"roots":roots,
        "original_root_sha256":{name:ring.digest(value) for name,value in sorted(named.items())}}

def save_export(path,ring,templates,target,report,maximum):
    named={f"W{j}":value for j,value in enumerate(templates)}
    records=[]
    for mode,geo in target.items():
        for index,(key,value) in enumerate(sorted(geo.terms.items())):
            name=f"L{mode}_{index}"
            named[name]=value
            records.append({"mode":mode,"geometry_key":list(key),"root":name})
    data={"schema":SCHEMA+"-original-expressions","source_hashes":report["source_hashes"],
        "bound_W":report["bound_W"],"geometry_names":list(local.NAMES),
        "projection":"derivative weight zero","local_roots":records,
        "content_scope":"W-and-local-static-density" if target else "W-only",
        **serialize_expressions(ring,named)}
    raw=canonical(data);stored=gzip.compress(raw,mtime=0)
    if len(stored)>maximum:
        raise formal.CompilationBudgetExceeded("portable export byte budget")
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(stored)
    metadata={"filename":path.name,"stored_bytes":len(stored),
        "stored_sha256":hashlib.sha256(stored).hexdigest(),"raw_bytes":len(raw),
        "raw_sha256":hashlib.sha256(raw).hexdigest(),"root_count":len(named),
        "profile_atom_count":len(data["profile_atoms"]),"content_scope":data["content_scope"],
        "contains_original_expression_not_only_hashes":True}
    return metadata

def decode_expressions(ring,data):
    """Return dict[str, Expr], checking every original content hash."""
    translated=[]
    def monomial(raw):
        power,indices=raw
        if not isinstance(power,int) or power<0 or any(not 0<=i<len(translated) for i in indices):
            raise ValueError("malformed portable profile monomial")
        return (power,tuple(sorted(translated[i] for i in indices)))
    for atom in data["profile_atoms"]:
        if atom[0]=="jet":
            if len(atom)!=3 or not isinstance(atom[2],int) or atom[2]<0:
                raise ValueError("portable jet")
            translated.append(ring.p.jet(atom[1],atom[2])[1][0])
        elif atom[0]=="int_right":
            value=monomial(atom[1])
            if not ring.p.weight(value):
                raise ValueError("portable primitive lacks positive profile degree")
            translated.append(ring.p.primitive(value)[1][0])
        else:
            raise ValueError("portable atom kind")
    roots={}
    for name,rows in data["roots"].items():
        terms={}
        for raw,n,d in rows:
            key=monomial(raw)
            if key in terms:
                raise ValueError("duplicate portable expression monomial")
            terms[key]=F(n,d)
        roots[name]=exact.Expr(ring,terms)
        if ring.digest(roots[name])!=data["original_root_sha256"][name]:
            raise ValueError("portable original expression identity mismatch")
    return roots

def load_export(path,expected_sha,ring,report,receipt):
    stored=path.read_bytes()
    if len(stored)>TOTAL_OUTPUT_BYTES or hashlib.sha256(stored).hexdigest()!=expected_sha:
        raise ValueError("bind exact published original-expression bytes")
    with gzip.open(path,"rb") as stream:
        raw=stream.read(40000001)
    if len(raw)>40000000:
        raise ValueError("portable raw byte limit")
    data=json.loads(raw)
    if (data.get("schema")!=SCHEMA+"-original-expressions"
        or data.get("source_hashes")!=report["source_hashes"]
        or data.get("content_scope")!="W-and-local-static-density"
        or data.get("projection")!="derivative weight zero"
        or data.get("geometry_names")!=list(local.NAMES)
        or data["bound_W"]["receipt_sha256"]!=dual.RECEIPT_SHA
        or data["bound_W"]["retained_original_indices"]!=blocks.EXPECTED_KEPT):
        raise ValueError("portable source, projection or W identity changed")
    roots=decode_expressions(ring,data)
    templates=[roots[f"W{j}"] for j in range(36)]
    expected=[receipt["all_original_control_templates"][j]["original_template_sha256"]
        for j in blocks.EXPECTED_KEPT]
    if [ring.digest(value) for value in templates]!=expected:
        raise ValueError("portable W hashes differ from the public proof")
    target={mode:{} for mode in MODES}
    for row in data["local_roots"]:
        mode,key=row["mode"],tuple(row["geometry_key"])
        if mode not in target or len(key)!=8 or jet_weight(key) or key in target[mode]:
            raise ValueError("portable local geometry/mode record")
        target[mode][key]=roots[row["root"]]
    report["bound_W"]=data["bound_W"]
    report["portable_original_expression_export"]={"filename":path.name,"stored_bytes":len(stored),
        "stored_sha256":expected_sha,"raw_bytes":len(raw),"raw_sha256":hashlib.sha256(raw).hexdigest(),
        "consumed_existing_export":True,"content_scope":data["content_scope"]}
    report["restored_without_recompilation"]={"actual_lower_fields_compiled":False,
        "local_v_recompiled":False,"local_N_recompiled":False,"all_original_root_hashes_verified":True}
    return templates,{mode:local.GExpr(ring,rows) for mode,rows in target.items()}

def run_weight_block(ring,templates,target,weight,report):
    grade=blocks.ScalingGrading(ring)
    normalizer=colored.ColoredNormalizer(ring)
    basis=exact.operator_basis(ring)
    labels,columns=[],[]
    working={}
    for ai,aw in enumerate(blocks.PARAMETER_WEIGHTS):
        for ti,tw in enumerate(blocks.THIRD_WEIGHTS):
            if aw+tw!=weight:
                continue
            original=templates[ti]
            if ti not in working:
                projected=grade.project(original,tw)
                if normalizer.word.expression(original-projected).terms:
                    raise AssertionError("bound third basis true scaling weight")
                working[ti]=normalizer.expression(projected)
            response=blocks.full_response(ring,colored.ThirdOperator(ring,working[ti]),basis[ai])
            columns.append(colored.vector_from_modes(response,normalizer))
            labels.append({"column":len(labels),"quadratic_index":ai,
                "quadratic_name":exact.PARAMETERS[ai],"third_index":ti,
                "v2_original_third_index":blocks.EXPECTED_KEPT[ti],
                "third_original_sha256":ring.digest(original)})
    span=colored.JointSpan(columns,ring.limits)
    fresh=colored.ColoredNormalizer(ring);dependencies=[]
    for j,vector in enumerate(columns):
        if j in span.independent:
            continue
        coeffs,residual=span.reduce(vector)
        if residual:
            raise AssertionError("column span bookkeeping")
        combined={i:ring.number(0) for i in range(8)}
        label=labels[j]
        combined[label["quadratic_index"]]+=templates[label["third_index"]]
        for i,c in coeffs.items():
            label=labels[i]
            combined[label["quadratic_index"]]-=c*templates[label["third_index"]]
        sums=zero_modes(ring)
        for ai,value in combined.items():
            if value.terms:
                blocks.add_modes(sums,blocks.full_response(ring,colored.ThirdOperator(ring,value),basis[ai]))
        checks={mode:fresh.word.expression(value) for mode,value in sums.items()}
        if any(value.terms for value in checks.values()):
            raise AssertionError("R8 dependency failed original-template verification")
        dependencies.append({"column":j,"coefficients":[[i,str(c)] for i,c in sorted(coeffs.items())],
            "fresh_original_zeros":{str(mode):value.digest() for mode,value in checks.items()}})
    keys=set().union(*(set(value.terms) for value in target.values()))
    solved,unresolved=[],[]
    for key in sorted(keys):
        raw={mode:grade.project(target[mode].terms.get(key,ring.number(0)),weight) for mode in MODES}
        if not any(value.terms for value in raw.values()):
            continue
        vector=colored.vector_from_modes(raw,normalizer)
        coeffs,residual=span.reduce(vector)
        row={"geometry_key":list(key),"original_modes_sha256":{str(mode):ring.digest(v) for mode,v in raw.items()},
            "representative_terms":len(vector),"coefficients":[[i,str(c)] for i,c in sorted(coeffs.items())],
            "remainder_terms":len(residual),"remainder_sha256":colored.vector_digest(residual)}
        if residual:
            row["remainder_preview"]=producer.readable_vector(residual,12)
            row["functional_nonmembership_proved"]=False
            unresolved.append(row)
        else:
            difference=dict(raw)
            combined={i:ring.number(0) for i in range(8)}
            for j,c in coeffs.items():
                label=labels[j]
                combined[label["quadratic_index"]]+=c*templates[label["third_index"]]
            for ai,value in combined.items():
                if value.terms:
                    blocks.add_modes(difference,blocks.full_response(ring,
                        colored.ThirdOperator(ring,value),basis[ai]),-1)
            checks={mode:fresh.word.expression(v) for mode,v in difference.items()}
            if any(value.terms for value in checks.values()):
                raise AssertionError("local coefficient member failed original full-mode check")
            row["fresh_original_zero_sha256"]={str(mode):v.digest() for mode,v in checks.items()}
            solved.append(row)
        report["coefficient_checkpoint"]={"weight":weight,"solved":len(solved),"unresolved":len(unresolved)}
    return {"weight":weight,"response_columns":labels,
        "true_response_dimension_upper_bound":len(span.independent),
        "representative_rank":len(span.independent),
        "verified_original_response_dependencies":dependencies,
        "paid_geometry_coefficients":solved,"unresolved_geometry_coefficients":unresolved,
        "outcome":"coefficientwise_membership_verified" if not unresolved else "coefficientwise_identity_not_found",
        "U4_quotient_nonzero_proved":False,
        "negative_scope":"nonzero representatives are not functional nonmembership; a local coefficient alone does not prove a nonzero constrained path integral"}

def small_toys():
    limits=exact.Limits(seconds=45,nodes=20000,atoms=5000,terms=10000,rewrites=30000,memory_mib=256)
    ring=colored.ColoredRing(limits);comp=local.SharedCompiler(ring.algebra)
    q=ring.algebra.profile(ring.p.jet("toy",0))
    rhs=ring.algebra.c.geometry("h")
    state=ring.algebra.c.state(rhs,("artificial",))
    left=formal.Field(comp,(q.coefficient(state),comp.zero,comp.zero))
    right=formal.Field(comp,(q,comp.zero,comp.zero))
    _,old=comp.forcing_range([(1,left,right)],2,"artificial_cross",False)
    for static in (False,True):
        zero=ZeroStateCoefficients(ring.algebra,static=static)
        new=local_forcing(comp,[(1,zero.field(left),zero.field(right))],zero)
        expansion=local.GeometryExpansion(ring.algebra,limits)
        comparison={**old,"P_s":old["P"].ds(),"B_s":old["B"].ds()}
        for name in ("period_rhs","P","B","P_s","B_s"):
            difference=zero.expression(comparison[name]).add(new[name].scale(-1))
            if expansion.separated(difference,ring).terms:
                raise AssertionError(("artificial true derivative comparison",static,name))
        if not expansion.separated(new["B_s"],ring).terms:
            raise AssertionError("zero history value still has nonzero actual derivative")
    h,k,o,hs,ks=(ScalarGeo.variable(i) for i in (local.H,local.K,local.O,local.V,local.W))
    d=h*o-k;ds=hs*o-ks/2
    a0=k*o*o-(k*k+1)*o/h;t0=(h*a0-hs*ds/(h*h))/8
    coords=pointwise_matrix()
    if (coords[0]/4+coords[6]/2-t0).terms:
        raise AssertionError("published R73 pointwise trace identity")
    a,b,c=(ring.color(name) for name in ("a","b","c"))
    key=list(GZERO);key[local.K]=2;key[local.O]=1
    potential=local.GExpr(ring,{tuple(key):a*b*c})
    R=potential.partial(local.K)+potential.partial(local.O).shift(local.H,-1).scale(F(1,2))
    N=endpoint.endpoint_potential(R)
    if (R-N.partial(local.K)-N.partial(local.O).shift(local.H,-1).scale(F(1,2))).terms:
        raise AssertionError("artificial horizontal potential")
    P=lambda x,y:x*y
    M=lambda x,y:x.D()*y.D()
    p,aa,bb=(ring.color(name) for name in ("p","aa","bb"))
    Rfree=-P(aa,bb)+2*P(p,M(p,aa))
    Cprime=-(M(aa,aa)+2*P(aa,bb))/3+(M(p,P(p,aa))+P(p,M(p,aa))+P(p,P(p,bb)))*F(2,3)
    Btau=2*P(aa,bb)-2*M(aa,aa)-8*P(p,M(p,aa))+4*M(p,P(p,aa))+4*P(p,P(p,bb))
    if (Rfree-Cprime+Btau/6).terms:
        raise AssertionError("artificial R109 one-sixth factor")
    packed=serialize_expressions(ring,{"artificial":(a*b.D()).I()+a.D()*c})
    other=colored.ColoredRing(limits)
    restored=decode_expressions(other,packed)
    if other.digest(restored["artificial"])!=packed["original_root_sha256"]["artificial"]:
        raise AssertionError("artificial portable DAG round trip")
    return {"true_cov_before_zero_history":True,"positive_jet_and_static_cases":True,
        "P_s_and_B_s_keep_zero_value_history_derivatives":True,
        "published_pointwise_matrix_trace_zero":True,"artificial_horizontal_potential":True,
        "R109_minus_one_sixth_identity":True,"artificial_portable_original_DAG_round_trip":True,
        "genuine_local_fourth_target_compiled":False,"profile_or_geometry_evaluated":False}

def write_report(path,report,maximum):
    raw=(json.dumps(report,sort_keys=True,indent=2,allow_nan=False)+"\n").encode()
    if len(raw)>maximum:
        report={"schema":SCHEMA,"completion":"output_limit","phase":report.get("phase"),
            "full_report_bytes":len(raw),"full_report_sha256":hashlib.sha256(raw).hexdigest(),
            "source_hashes":report.get("source_hashes"),"completed_blocks":report.get("completed_blocks",[]),
            "coefficient_checkpoint":report.get("coefficient_checkpoint"),
            "portable_W_expression_export":report.get("portable_W_expression_export"),
            "portable_original_expression_export":report.get("portable_original_expression_export"),
            "new_mathematical_conclusion":False}
        raw=(json.dumps(report,sort_keys=True,indent=2)+"\n").encode()
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)
    return len(raw),hashlib.sha256(raw).hexdigest(),report["completion"]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--input-receipt",type=Path,default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--input-export",type=Path)
    parser.add_argument("--export-sha256")
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--weights",default="2,1,0")
    parser.add_argument("--max-seconds",type=float,default=300)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-report-bytes",type=int,default=250000)
    parser.add_argument("--max-export-bytes",type=int,default=3500000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.max_report_bytes,args.max_export_bytes)<=0:
        parser.error("positive bounded resources required")
    if args.max_export_bytes+args.max_report_bytes>TOTAL_OUTPUT_BYTES:
        parser.error("reserve main report inside the 4.8 MB total output limit")
    if bool(args.input_export)!=bool(args.export_sha256):
        parser.error("a portable export requires its published SHA256")
    weights=[int(x) for x in args.weights.split(",")]
    if len(weights)!=len(set(weights)) or len(weights)>11 or any(x<-8 or x>2 for x in weights):
        parser.error("distinct requested affine weights inside [-8,2]")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"):
        parser.error("actual local target runs only in this public repository Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"dependencies","source_hashes":{},
        "github_sha":os.environ.get("GITHUB_SHA"),"github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "scope":"derivative-weight-zero projection of R109 full-phase local density modulo complete R8",
        "all_derivative_weights_computed":False,"all_geometry_coefficients_independently_realizable":False,
        "complete_U4_equals_R8_proved":False,"P0_or_ruling_paid":False,
        "finite_isometric_family_constructed":False,"completed_blocks":[],
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "coefficient_nodes":400000,"profile_atoms":100000,"expression_terms":100000,
            "rewrite_calls":1000000,"rational_bits_during_elimination":8192,
            "report_bytes":args.max_report_bytes,"compressed_export_bytes":args.max_export_bytes,
            "total_published_bytes":TOTAL_OUTPUT_BYTES}}
    code=0
    try:
        report["source_hashes"]=dependencies()
        if args.toy_only:
            report["phase"]="small_artificial_checks"
            report["toy"]=small_toys();report["completion"]="toy_passed"
        else:
            receipt=dual.read_receipt(args.input_receipt)
            limits=exact.Limits(args.max_seconds,400000,100000,100000,1000000,args.memory_mib,8192)
            ring=colored.ColoredRing(limits)
            if args.input_export:
                report["phase"]="consume_bound_original_expression_export"
                templates,target=load_export(args.input_export,args.export_sha256,ring,report,receipt)
            else:
                report["phase"]="original_lower_fields_true_cov_then_local_static_fourth"
                v=compile_static_local_v(ring,report)
                report["phase"]="pointwise_colored_potential_and_bound_W"
                def early_basis_export(templates):
                    path=args.output.with_name(args.output.stem+"-W-original-expressions.json.gz")
                    report["portable_W_expression_export"]=save_export(
                        path,ring,templates,{},report,min(args.max_export_bytes,1000000))
                templates,N=restore_third_and_potential(ring,receipt,report,early_basis_export)
                report["phase"]="local_density_minus_pointwise_matrix_potential_response"
                target=build_local_density(ring,v,N,report)
            grade=blocks.ScalingGrading(ring)
            report["target_profile_weight_inventory"]={
                str(mode):{str(key):grade.inventory(value) for key,value in geo.terms.items()}
                for mode,geo in target.items()}
            if not args.input_export:
                path=args.output.with_name(args.output.stem+"-original-expressions.json.gz")
                report["phase"]="portable_original_expression_export"
                report["portable_original_expression_export"]=save_export(
                    path,ring,templates,target,report,args.max_export_bytes)
            published=0 if args.input_export else (
                report["portable_original_expression_export"]["stored_bytes"]
                +report.get("portable_W_expression_export",{}).get("stored_bytes",0))
            if published+args.max_report_bytes>TOTAL_OUTPUT_BYTES:
                raise formal.CompilationBudgetExceeded("both exports plus main report output budget")
            for weight in weights:
                report["phase"]="R8_static_local_weight_"+str(weight)
                block=run_weight_block(ring,templates,target,weight,report)
                path=args.output.with_name(args.output.stem+f"-weight-{weight:+d}.json")
                data={"schema":SCHEMA+"-block","github_sha":report["github_sha"],
                    "source_hashes":report["source_hashes"],
                    "portable_input":report["portable_original_expression_export"],**block}
                raw=(json.dumps(data,sort_keys=True,indent=2)+"\n").encode()
                if len(raw)>args.max_report_bytes:
                    raise formal.CompilationBudgetExceeded("individual coefficient block output budget")
                if published+len(raw)+args.max_report_bytes>TOTAL_OUTPUT_BYTES:
                    raise formal.CompilationBudgetExceeded("total outputs with main report reserved")
                path.write_bytes(raw);published+=len(raw)
                report["completed_blocks"].append({"weight":weight,"filename":path.name,
                    "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"outcome":block["outcome"],
                    "paid":len(block["paid_geometry_coefficients"]),
                    "unresolved":len(block["unresolved_geometry_coefficients"]),
                    "response_upper_bound":block["true_response_dimension_upper_bound"]})
                print(json.dumps({"phase":"completed_local_density_block","weight":weight,
                    "outcome":block["outcome"],"seconds":time.monotonic()-started}),flush=True)
                if block["unresolved_geometry_coefficients"]:
                    report["stopped_after_first_unresolved_block"]=True
                    break
            report["compiler_inventory"]={"coefficient_nodes":len(ring.algebra.c.nodes),
                "profile_atoms":len(ring.p.atoms),"lower_order_histories":len(ring.algebra.c.state_rhs)}
            report["completion"]="complete"
    except formal.CompilationBudgetExceeded as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    size,digest,completion=write_report(args.output,report,args.max_report_bytes)
    if completion=="output_limit":
        code=2
    print(json.dumps({"completion":completion,"output":str(args.output),
        "bytes":size,"sha256":digest}),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
