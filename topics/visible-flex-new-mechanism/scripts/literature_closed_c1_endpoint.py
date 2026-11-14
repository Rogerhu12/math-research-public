#!/usr/bin/env python3
"""R79 closed-C1 operator space, exact endpoint class, and pure P1 response.

This is a new research target. The previous three-moment failure is retained.
The actual compiler is public-Actions-only; --toy-only uses artificial symbolic
polynomials. Everything remains diagonal tau(q), not full unsymmetrized T.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import sys
import time

import literature_linear_third_bridge_quotient as quotient

local = quotient.local
exact = quotient.exact
words = quotient.words
EXPECTED_QUOTIENT_SHA256 = "0627875fe06950c9e7c360baaf0429451697a460e2cf10aa6b3434c501363bd2"
SCHEMA = "visible-flex-closed-C1-endpoint-and-pure-P1-v1"


def restrict_static(geo, *, h=None, k=None, omega=None):
    """Exact rational state substitution. log(h) is used only at h=1."""
    substitutions = {local.H: h, local.K: k, local.O: omega}
    out = {}
    for key, expr in geo.terms.items():
        if any(key[i] for i in (local.V,local.W,local.HV,local.KW)):
            raise ValueError("a static endpoint substitution contains velocity")
        target = list(key)
        coefficient = F(1)
        if h is not None and key[local.LH]:
            if F(h) != 1:
                raise ValueError("no numerical approximation of log(h) in exact endpoints")
            continue
        for index, value in substitutions.items():
            if value is None:
                continue
            value = F(value)
            if index == local.H and value <= 0:
                raise ValueError("positive h required")
            coefficient *= value**target[index]
            target[index] = 0
        target = tuple(target)
        out[target] = out.get(target,geo.ring.number(0))+coefficient*expr
    return local.GExpr(geo.ring,out)


def integrate_polynomial_from(geo, index, base):
    """Coefficientwise exact integral in k or omega from the stated base."""
    if index not in (local.K,local.O):
        raise ValueError("only the polynomial endpoint coordinates k and omega")
    out = {}
    base = F(base)
    for key, expr in geo.terms.items():
        if any(key[i] for i in (local.V,local.W,local.HV,local.KW,local.LH)):
            raise ValueError("polynomial endpoint primitive contains nonstatic/log data")
        power = key[index]
        if power < 0:
            raise ValueError("the actual geometry is polynomial in k and omega")
        high = local.gshift(key,index)
        low = list(key);low[index] = 0;low = tuple(low)
        out[high] = out.get(high,geo.ring.number(0))+expr/F(power+1)
        out[low] = out.get(low,geo.ring.number(0))-base**(power+1)*expr/F(power+1)
    return local.GExpr(geo.ring,out)


def endpoint_potential(residual, *, h_base=1, k_base=1, omega_base=1):
    """R79 F=integral a(v,omega*)dv + 2 integral b(k,u)du.

    This is a chosen raw representative. Its horizontal derivative equals R
    only modulo the R79 compatibility space, which is checked afterwards.
    """
    a = residual+residual.partial(local.H).shift(local.H)
    b = residual.partial(local.H).shift(local.H,2).scale(-1)
    a_at_base_h = restrict_static(a,h=h_base)
    b_at_base_h = restrict_static(b,h=h_base)
    first = integrate_polynomial_from(restrict_static(a_at_base_h,omega=omega_base),
                                      local.K,k_base)
    second = integrate_polynomial_from(b_at_base_h,local.O,omega_base).scale(2)
    return first+second


def scalar_value(geo, *, h=1, k=1, omega=1):
    value = restrict_static(geo,h=h,k=k,omega=omega)
    if set(value.terms)-{local.GZERO}:
        raise AssertionError("an endpoint value still has a geometry variable")
    return value.terms.get(local.GZERO,geo.ring.number(0))


def profile_labels(pieces, components):
    raw, labels = [], []
    for component in components:
        for key, value in sorted(pieces[component].terms.items()):
            raw.append(value)
            labels.append({"kind": "R79_closed_C1" if component in (
                "h_shape_obstruction","contact_closure") else "R77_weight_three",
                "component":component,"geometry":list(key),
                "monomial":quotient.geometry_label(key)})
    return raw,labels


def original_relation(raw, coefficients, columns, ring):
    return raw-sum((c*columns[index] for index,c in coefficients.items()),ring.number(0))


def row_check(raw, span, raw_columns, normalizer, fresh):
    coefficients,remainder = span.reduce(normalizer.expression(raw))
    row = {"coefficients":quotient.coefficient_rows(coefficients),
           "remainder":normalizer.word.summary(remainder)}
    if not remainder.terms:
        row["fresh_original_zero_sha256"] = quotient.fresh_zero(
            original_relation(raw,coefficients,raw_columns,raw.ring),fresh)
    return row,remainder


def pure_response(ring,tau,A):
    q = ring.jet()
    return (ring.variation(tau,A(q,q))-2*A(q,tau))/8


def small_toys():
    limits = exact.Limits(seconds=60,nodes=50000,atoms=10000,terms=15000,
                         rewrites=25000,memory_mib=1024)
    ring = exact.Ring(limits)
    n = quotient.ProfileNormalizer(ring,25000,15000)
    fresh = quotient.ProfileNormalizer(ring,25000,15000)
    q,x = ring.jet(),ring.x()
    p1,p2,controlled = q**3,q*q.D()**2,x*q**3
    # Artificial endpoint potential F=k^2*omega*p1 + omega^3*p2.
    model_potential = local.GExpr(ring,{
        local.gshift(local.gshift(local.GZERO,local.K,2),local.O):p1,
        local.gshift(local.GZERO,local.O,3):p2})
    residual = model_potential.partial(local.K)+model_potential.partial(local.O).shift(local.H,-1).scale(F(1,2))
    residual += local.GExpr(ring,{local.gshift(local.gshift(local.GZERO,local.H),local.K):controlled})
    potential = endpoint_potential(residual)
    difference = residual-potential.partial(local.K)-potential.partial(local.O).shift(local.H,-1).scale(F(1,2))
    span = quotient.ExactWordSpan([n.expression(controlled)],limits)
    for expr in difference.terms.values():
        row,remainder = row_check(expr,span,[controlled],n,fresh)
        if remainder.terms:
            raise AssertionError("artificial horizontal endpoint potential quotient")
    value = scalar_value(potential,k=-1,omega=-1)-scalar_value(potential,k=1,omega=1)
    desired = -2*p1-2*p2
    row,remainder = row_check(value-desired,span,[controlled],n,fresh)
    if remainder.terms:
        raise AssertionError("artificial plus-to-minus orientation")
    # Artificial symmetric bilinear A(f,g)=fg checks the pure-response sign.
    A = lambda f,g:f*g
    response = pure_response(ring,p1,A)
    if n.expression(response-q**4/8).terms:
        raise AssertionError("Frechet response divided by eight")
    endpoint_raw = p2+3*controlled
    target = -pure_response(ring,endpoint_raw,A)+5*pure_response(ring,controlled,A)
    effective = target+pure_response(ring,endpoint_raw,A)
    response_span = quotient.ExactWordSpan([n.expression(pure_response(ring,controlled,A))],limits)
    coeff,remainder = response_span.reduce(-n.expression(effective))
    if remainder.terms or coeff.get(0)!=-5:
        raise AssertionError("effective target includes plus endpoint response")
    fresh_residual = effective+sum((c*pure_response(ring,controlled,A) for c in coeff.values()),ring.number(0))
    quotient.fresh_zero(fresh_residual,fresh)
    return {"artificial_horizontal_potential_mod_control":True,
            "plus_one_to_minus_one_endpoint_orientation":True,
            "two_integrals_and_right_endpoint_not_reset":True,
            "pure_response_factor_one_eighth":True,
            "target_plus_endpoint_plus_control_sign":True,
            "positive_relation_verified_from_original_expressions":True,
            "actual_local_or_reciprocal_compiler_called":False,
            "profile_or_geometry_values_evaluated":False}


def dependencies():
    data = Path(quotient.__file__).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest!=EXPECTED_QUOTIENT_SHA256:
        raise RuntimeError("old C1 producer changed; explicitly bind the new source")
    return {"previous_C1_producer":{"filename":Path(quotient.__file__).name,
                                    "bytes":len(data),"sha256":digest},
            "mathematical_dependencies":quotient.dependency_info()}


def run_research(args,payload):
    limits = exact.Limits(args.max_seconds,args.max_coefficient_nodes,args.max_profile_atoms,
                          args.max_terms,args.max_IBP_calls,args.max_memory_mib,args.max_rational_bits)
    ring = exact.Ring(limits)
    n = quotient.ProfileNormalizer(ring,args.max_IBP_calls,args.max_terms)
    fresh = quotient.ProfileNormalizer(ring,args.max_IBP_calls,args.max_terms)
    target_raw = None
    if not args.skip_pure_response:
        # The frozen constant extractor walks the complete coefficient DAG
        # and intentionally rejects general geometry nodes. Compile it before
        # the variable-geometry density, without changing either old compiler.
        payload["phase"]="compile_constant_part_before_general_geometry_nodes"
        target_raw,target_records=exact.compile_reciprocal_target(ring)
        payload["constant_compiler_records"]=target_records
    payload["phase"]="compile_local_and_R79_compatibility_operators"
    raw,records,expanded = local.compile_local_third(ring)
    pieces = local.decompose(raw,n.legacy)
    R = pieces["residual_k"]
    payload["raw_local"]=raw.summary()
    payload["decomposition"]={key:value.summary() for key,value in pieces.items() if isinstance(value,local.GExpr)}
    payload["compiler_records"]=records
    payload["expanded_coefficient_nodes"]=expanded
    q = ring.jet()
    ops = exact.operator_basis(ring)
    commutators,commutator_labels=[],[]
    for i,j in itertools.combinations(range(8),2):
        commutators.append(ops[i](q,ops[j](q,q))-ops[j](q,ops[i](q,q)))
        commutator_labels.append({"kind":"R71_diagonal_third_commutator",
                                  "pair":[exact.PARAMETERS[i],exact.PARAMETERS[j]]})
    c3,c3_labels=profile_labels(pieces,("area","cubic"))
    closed,closed_labels=profile_labels(pieces,("h_shape_obstruction","contact_closure"))
    c3,c3_labels,_=quotient.independent_labels(c3,c3_labels,n)
    closed,closed_labels,_=quotient.independent_labels(closed,closed_labels,n)
    raw_columns=commutators+c3+closed
    labels=commutator_labels+c3_labels+closed_labels
    normal_columns=[n.expression(value) for value in raw_columns]
    span=quotient.ExactWordSpan(normal_columns,limits)
    payload["reachable_space"]={**span.summary(),"R71_columns":len(commutators),
                                 "C3_coefficient_columns":len(c3),"closed_C1_coefficient_columns":len(closed),
                                 "reachability_source":"R71, R77 and R79; not inferred from the representative rank"}
    payload["phase"]="construct_and_verify_entire_endpoint_potential"
    potential=endpoint_potential(R,h_base=1,k_base=1,omega_base=1)
    horizontal=potential.partial(local.K)+potential.partial(local.O).shift(local.H,-1).scale(F(1,2))
    difference=(R-horizontal).normalized(n.legacy)
    # Both endpoints have h=1, so the prior h-primitive has zero endpoint jump.
    old_jump=scalar_value(pieces["potential_h"],k=-1,omega=-1)-scalar_value(pieces["potential_h"],k=1,omega=1)
    quotient.fresh_zero(old_jump,fresh)
    endpoint_raw=scalar_value(potential,k=-1,omega=-1)-scalar_value(potential,k=1,omega=1)
    rows,unresolved=[],[]
    readable={}
    for key,value in sorted(difference.terms.items()):
        row,remainder=row_check(value,span,raw_columns,n,fresh)
        row.update(geometry=list(key),monomial=quotient.geometry_label(key))
        rows.append(row)
        if remainder.terms:
            unresolved.append({"geometry":list(key),"monomial":row["monomial"],"residual":row["remainder"]})
            if len(unresolved)<=4:readable["unresolved_horizontal_coefficient_"+str(len(unresolved))]=remainder
    endpoint_row,endpoint_class=row_check(endpoint_raw,span,raw_columns,n,fresh)
    readable["endpoint_raw"]=n.expression(endpoint_raw)
    readable["endpoint_class"]=endpoint_class
    payload["endpoint_potential"]={
        "raw_geometry_expression":potential.summary(),
        "base_state":{"h":"1","k":"1","omega":"1"},
        "terminal_state":{"h":"1","k":"-1","omega":"-1"},
        "formula":"F=int_1^k a(1,v,1)dv + 2 int_1^omega b(1,k,u)du; a=R+hR_h, b=-h^2 R_h",
        "horizontal_difference_geometry_rows":len(rows),
        "all_rows_verified_from_original_profiles":not unresolved,
        "unresolved":unresolved,
        "anchored_P_h_endpoint_jump_exactly_zero":True,
        "endpoint_raw_terms":len(endpoint_raw.terms),"endpoint_raw_sha256":ring.digest(endpoint_raw),
        "endpoint_class":n.word.summary(endpoint_class),
        "endpoint_class_zero_verified":not endpoint_class.terms,
        "nonzero_representative_is_not_a_nonzero_actual_function_certificate":True}
    # Compare the actual endpoint class with the older selected formal moments.
    reference={p:R.terms.get(quotient.reference_key(p),ring.number(0)) for p in (-1,0,1)}
    old_three=-4*reference[-1]-2*reference[0]-4*reference[1]
    comparison_row,comparison_remainder=row_check(endpoint_raw-old_three,span,raw_columns,n,fresh)
    readable["endpoint_minus_old_three_moments"]=comparison_remainder
    payload["old_three_moment_comparison"]={
        "formal_expression":"endpoint - (-4*L_minus - 2*L_zero - 4*L_plus)",
        "identity_mod_reachable_verified":not comparison_remainder.terms,
        "residual":n.word.summary(comparison_remainder)}
    certificate={"schema":SCHEMA+"-relations","geometry_variable_order":list(local.NAMES),
                 "reachable_columns":labels,"horizontal_rows":rows,
                 "endpoint_reduction":endpoint_row,"old_three_moment_comparison":comparison_row,
                 "scope":"diagonal only; endpoint residuals and all raw column sources are retained"}
    if args.skip_pure_response:
        payload["pure_P1"]={"not_run":True}
    else:
        payload["phase"]="test_true_pure_target_plus_full_endpoint_class"
        A=exact.positive_constant_operator(ring)
        response_columns=[pure_response(ring,value,A) for value in raw_columns]
        response_span=quotient.ExactWordSpan([n.expression(value) for value in response_columns],limits)
        effective=target_raw+pure_response(ring,endpoint_raw,A)
        coeff,remainder=response_span.reduce(-n.expression(effective))
        result={"effective_target":"original reciprocal pure P1 target + H_A(full plus-to-minus C1 endpoint representative)",
                "response_space":response_span.summary(),
                "original_target_sha256":ring.digest(target_raw),"endpoint_source_sha256":ring.digest(endpoint_raw),
                "effective_target_raw_terms":len(effective.terms),"effective_target_raw_sha256":ring.digest(effective),
                "effective_target_word":n.word.summary(n.expression(effective)),
                "span_remainder":n.word.summary(remainder),
                "verified_original_whole_function_identity":False,
                "endpoint_representative_verified_for_true_bridge":not unresolved,
                "all_phase_channels_satisfied":False,
                "negative_is_not_function_nonmembership":True}
        certificate["pure_P1_coefficients"]=quotient.coefficient_rows(coeff)
        if not remainder.terms:
            check=effective+sum((c*response_columns[i] for i,c in coeff.items()),ring.number(0))
            result["fresh_original_zero_sha256"]=quotient.fresh_zero(check,fresh)
            result["verified_original_whole_function_identity"]=True
        payload["pure_P1"]=result
        readable["effective_pure_target"]=n.expression(effective)
        readable["pure_target_span_remainder"]=remainder
    payload["phase"]="save_reproducible_relations"
    data=quotient.canonical_bytes(certificate)+b"\n"
    certificate_path=args.out.with_name(args.out.stem+"-relations.json")
    if len(data)>1000000:
        import gzip
        certificate_path=certificate_path.with_suffix(".json.gz")
        data=gzip.compress(data,mtime=0)
    if len(data)>=5000000:
        raise exact.formal.CompilationBudgetExceeded("relation artifact exceeds 5 MB")
    certificate_path.parent.mkdir(parents=True,exist_ok=True);certificate_path.write_bytes(data)
    payload["relation_artifact"]={"filename":certificate_path.name,"bytes":len(data),
                                  "sha256":hashlib.sha256(data).hexdigest()}
    export,_=words.readable_export(n.word,readable,{},[])
    export["schema"]=SCHEMA+"-expressions"
    export["relation"]="endpoint and effective target are raw actual expressions; labelled span remainders are exact rewrites, not nonmembership certificates"
    export.pop("elimination_coefficients",None)
    payload["readable_expressions"]=quotient.write_json(
        args.expressions_out or args.out.with_name(args.out.stem+"-expressions.json"),export)
    payload["word_statistics"]=n.word.stats
    payload["actual_sizes"]={"coefficient_DAG_nodes":len(ring.algebra.c.nodes),
                             "profile_atoms":len(ring.p.atoms),"history_states":len(ring.algebra.c.state_rhs)}
    payload["completion"],payload["phase"]="complete","finished"


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--expressions-out",type=Path)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--skip-pure-response",action="store_true")
    parser.add_argument("--max-seconds",type=int,default=240)
    parser.add_argument("--max-coefficient-nodes",type=int,default=600000)
    parser.add_argument("--max-profile-atoms",type=int,default=80000)
    parser.add_argument("--max-terms",type=int,default=100000)
    parser.add_argument("--max-IBP-calls",type=int,default=300000)
    parser.add_argument("--max-memory-mib",type=int,default=2048)
    parser.add_argument("--max-rational-bits",type=int,default=8192)
    args=parser.parse_args()
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS")=="true" and
                                 os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"):
        parser.error("the complete research target runs only in the named public Actions repo")
    if any(value<=0 for key,value in vars(args).items() if key.startswith("max_")):
        parser.error("positive resource bounds required")
    sys.setrecursionlimit(12000)
    started=time.monotonic()
    payload={"schema":SCHEMA,"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             "github":{key:os.environ.get(key) for key in
                       ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")},
             "completion":"not_started","phase":"dependencies_and_artificial_checks",
             "profile_scope":"ordinary complex diagonal q; no claim about complete unsymmetrized T(f;g,j)",
             "right_anchor":"I=integral_r^xi, J=-I; all left tails retained",
             "geometry_relation":"omega_s=k_s/(2h), h>0; a common physical profile interval for all actual controls",
             "control_theorems":["R71","R77","R79"],
             "representative_rank_is_not_actual_dimension":True,
             "normalizer_complete":False,"closed_C1_reachability_inferred_from_rank":False,
             "actual_baseline_bridge_parameters_produced":False,
             "all_phase_P1_satisfied":False,"P0_satisfied":False,
             "fourth_ruling_satisfied":False,"finite_isometric_family_certified":False,
             "profile_or_geometry_values_evaluated":False,
             "limits":{key:value for key,value in vars(args).items() if key.startswith("max_")}}
    code=0
    try:
        payload["dependencies"]=dependencies()
        payload["artificial_checks"]=small_toys()
        if args.toy_only:
            payload["completion"],payload["phase"]="toy_only","finished"
        else:run_research(args,payload)
    except exact.formal.CompilationBudgetExceeded as error:
        payload["completion"],payload["budget_failure"]="resource_budget_exceeded",str(error);code=2
    except Exception as error:
        payload["completion"],payload["error_type"],payload["error"]="implementation_check_failed",type(error).__name__,str(error);code=1
    payload["elapsed_seconds"]=time.monotonic()-started
    payload["peak_resident_mib_linux"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    data=json.dumps(payload,indent=2,sort_keys=True,allow_nan=False)+"\n"
    if len(data.encode())>=95000:
        rows=payload.get("endpoint_potential",{}).get("unresolved",[])
        payload["endpoint_potential"]["unresolved_count"]=len(rows)
        payload["endpoint_potential"]["unresolved"]=rows[:12]
        payload["summary_excerpted_full_relations_retained"]=True
        data=json.dumps(payload,indent=2,sort_keys=True,allow_nan=False)+"\n"
    if len(data.encode())>=95000:raise RuntimeError("summary exceeds 95 KB")
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(data,encoding="utf-8")
    print(json.dumps({"output":str(args.out),"bytes":len(data.encode()),
                      "sha256":hashlib.sha256(data.encode()).hexdigest(),"completion":payload["completion"]}))
    raise SystemExit(code)


if __name__=="__main__":main()
