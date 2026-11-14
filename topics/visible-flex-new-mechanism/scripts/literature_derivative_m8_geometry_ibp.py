#!/usr/bin/env python3
"""Apply R129's exact horizontal geometry IBP to already published packets.

No original profile DAG, m8 substitution or response formula is evaluated.
The complete normalized L2 and original L4 are imported with all coefficients.
Actual packet calculations run only in this public repository's Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import json
import os
from pathlib import Path
import resource
import time

import literature_derivative_m8_tail_quotient as source

first, projection, constraint = source.first, source.projection, source.constraint
factors, Packet = source.factors, source.Packet
canonical, sha, identity = source.canonical, source.sha, source.identity
SCHEMA = "visible-flex-complete-derivative-m8-horizontal-IBP-v1"
SOURCE_DRIVER_SHA = "5c7bb457eec0b68b31b2e7250cf89eb7901660ffac289ccf7854a8c47c198705"
H, K, O, U, W, A, B, LOGH, J, ELL = range(10)
GZERO = (0,)*10


def dependencies():
    previous = source.dependencies()
    if previous["driver"]["sha256"] != SOURCE_DRIVER_SHA:
        raise ValueError("bind the published complete derivative consumer explicitly")
    return {"driver":identity(__file__), "complete_derivative_source":previous}


def shift(key, index, power=1):
    answer = list(key)
    answer[index] += power
    return tuple(answer)


class GeometryPackets:
    """Ten exact geometric exponents with original (P,A,R) vector coefficients."""
    def __init__(self, ring, terms=None):
        self.ring = ring
        self.terms = {tuple(key):packet.copy() for key,packet in (terms or {}).items()
                      if not packet.empty()}
        if any(len(key)!=10 for key in self.terms):
            raise ValueError("no geometric coordinate may be truncated")

    def add_term(self, key, packet, amount=F(1)):
        if amount and not packet.empty():
            self.terms.setdefault(key,Packet()).add(packet,amount,self.ring)
            if self.terms[key].empty():
                del self.terms[key]
        return self

    def plus(self, other, amount=F(1)):
        answer=GeometryPackets(self.ring,self.terms)
        for key,packet in other.terms.items():
            answer.add_term(key,packet,amount)
        return answer

    def shifted(self, index, power=1, amount=F(1)):
        answer=GeometryPackets(self.ring)
        for key,packet in self.terms.items():
            answer.add_term(shift(key,index,power),packet,amount)
        return answer

    def partial(self, index):
        answer=GeometryPackets(self.ring)
        for key,packet in self.terms.items():
            if key[index]:
                answer.add_term(shift(key,index,-1),packet,F(key[index]))
            if index==H and key[LOGH]:
                answer.add_term(shift(shift(key,LOGH,-1),H,-1),packet,F(key[LOGH]))
        return answer

    def horizontal_state_derivative(self):
        # X=d_h, Y=d_k+(2h)^(-1)d_omega, while u,w are held fixed.
        return (self.partial(H).shifted(U)
            .plus(self.partial(K).shifted(W))
            .plus(self.partial(O).shifted(H,-1).shifted(W,amount=F(1,2))))

    def total_derivative(self):
        if any(key[J] or key[ELL] for key in self.terms):
            raise ValueError("R129 boundary potentials contain jets through order two only")
        return (self.horizontal_state_derivative()
            .plus(self.partial(U).shifted(A))
            .plus(self.partial(W).shifted(B))
            .plus(self.partial(A).shifted(J))
            .plus(self.partial(B).shifted(ELL)))

    def selected(self, predicate):
        return GeometryPackets(self.ring,{key:packet for key,packet in self.terms.items()
                                         if predicate(key)})

    def check(self, columns, allowed_weights=None):
        for key,packet in self.terms.items():
            if any(key[i]<0 for i in (U,W,A,B,J,ELL,LOGH)):
                raise ValueError("jets and log powers must remain actual nonnegative powers")
            if allowed_weights is not None and factors.geometry_weight(key) not in allowed_weights:
                raise ValueError("wrong real geometric derivative weight")
            packet.verify(columns,self.ring)
        self.ring.guard()

    def zero(self):
        return not self.terms


def quadratic_normal_form(value):
    potential=GeometryPackets(value.ring)
    for key,packet in value.terms.items():
        if key[J] or key[ELL] or key[A]+key[B]>1:
            raise ValueError("full L2 has an unexpected jet pattern")
        if key[A] or key[B]:
            if key[U] or key[W] or key[A]+key[B]!=1:
                raise ValueError("L2 acceleration coefficient must have weight zero")
            index=A if key[A] else B
            velocity=U if index==A else W
            potential.add_term(shift(shift(key,index,-1),velocity),packet)
    normal=value.plus(potential.total_derivative(),F(-1))
    if any(key[A] or key[B] or key[J] or key[ELL] or key[U]+key[W]!=2
           for key in normal.terms):
        raise AssertionError("R129 L2 reduction retained a nonquadratic velocity term")
    return potential,normal


def quartic_normal_form(value):
    third_potential=GeometryPackets(value.ring)
    for key,packet in value.terms.items():
        if key[J] or key[ELL]:
            if key[J]+key[ELL]!=1 or key[A] or key[B] or key[U]+key[W]!=1:
                raise ValueError("every actual weight-four third jet must have its one velocity factor")
            index=J if key[J] else ELL
            acceleration=A if index==J else B
            third_potential.add_term(shift(shift(key,index,-1),acceleration),packet)
    no_third=value.plus(third_potential.total_derivative(),F(-1))
    if any(key[J] or key[ELL] for key in no_third.terms):
        raise AssertionError("third geometry jets did not cancel in the complete polynomial")

    velocity_potential=GeometryPackets(value.ring)
    for key,packet in no_third.terms.items():
        if key[A]+key[B]==1:
            if key[U]+key[W]!=2:
                raise ValueError("weight-four acceleration-linear part has a wrong velocity degree")
            index=A if key[A] else B
            velocity=U if index==A else W
            velocity_potential.add_term(shift(shift(key,index,-1),velocity),packet,F(1,3))
        elif key[A]+key[B] not in (0,2):
            raise ValueError("weight-four acceleration degree exceeds two")

    normal=no_third.plus(velocity_potential.total_derivative(),F(-1))
    accel=normal.selected(lambda key:key[A]+key[B]==2)
    linear=normal.selected(lambda key:key[A]+key[B]==1)
    quartic=normal.selected(lambda key:key[A]+key[B]==0)
    if any(key[U] or key[W] or key[J] or key[ELL] for key in accel.terms):
        raise AssertionError("acceleration quadratic part has another jet")
    if any(key[U]+key[W]!=4 or key[J] or key[ELL] for key in quartic.terms):
        raise AssertionError("velocity quartic part is not complete")

    # Recover H from the coefficient of b: C_b = u H. Verify both full packets.
    h=GeometryPackets(value.ring)
    for key,packet in linear.terms.items():
        if key[B]:
            if key[B]!=1 or key[A] or key[U]<1:
                raise AssertionError("the remaining b coefficient is not exactly u H")
            h.add_term(shift(shift(key,B,-1),U,-1),packet)
    if any(key[U]+key[W]!=1 or key[A] or key[B] or key[J] or key[ELL]
           for key in h.terms):
        raise AssertionError("the complete H is not velocity-linear")
    expected=h.shifted(U).shifted(B).plus(h.shifted(W).shifted(A),F(-1))
    if not linear.plus(expected,F(-1)).zero():
        raise AssertionError("both non-symmetric v squared times a terms must be retained exactly")

    potential=third_potential.plus(velocity_potential)
    return potential,normal,{"acceleration_quadratic":accel,
        "area_acceleration":linear,"area_multiplier_H":h,"velocity_quartic":quartic}, {
        "third_jet_potential":third_potential,"velocity_cubic_potential":velocity_potential}


def load_complete_source(args,columns,ring,report):
    fields=(args.source_report,args.source_report_sha256,args.source_publication_receipt,
            args.source_publication_sha256,args.source_certificate,args.source_certificate_sha256,
            args.source_run,args.source_commit)
    if not all(fields):
        raise ValueError("all eight published complete derivative source bindings are required")
    main,raw=source.read_explicit_main(args.source_report,args.source_report_sha256)
    if (main.get("schema")!=source.SCHEMA or main.get("completion")!="complete"
        or str(main.get("github_run_id"))!=args.source_run
        or main.get("github_sha")!=args.source_commit
        or main.get("source_hashes")!=source.dependencies()):
        raise ValueError("bind the successful complete derivative calculation")
    metadata=main.get("complete_certificate")
    if not metadata or metadata.get("stored_sha256")!=args.source_certificate_sha256:
        raise ValueError("the exact full derivative certificate is required")
    publication_raw=projection.checked_bytes(args.source_publication_receipt,95000)
    if sha(publication_raw)!=args.source_publication_sha256:
        raise ValueError("published derivative receipt SHA mismatch")
    publication=json.loads(publication_raw)
    binding=source.bind_publication(publication,run=args.source_run,commit=args.source_commit,
        lane="derivative_m8_tail_quotient",main_name=args.source_report.name,
        main_bytes=len(raw),main_sha=sha(raw),export=metadata,driver=main["source_hashes"]["driver"])
    data=first.read_bound_gzip(args.source_certificate,metadata)
    if (data.get("schema")!=source.SCHEMA+"-certificate"
        or data.get("source_hashes")!=main["source_hashes"]
        or str(data.get("github_run_id"))!=args.source_run
        or data.get("github_sha")!=args.source_commit
        or data.get("geometry_names")!=list(factors.GEOMETRY_NAMES)
        or data.get("geometric_integration_by_parts_applied") is not False
        or data.get("actual_period_sign_or_reachability_asserted") is not False):
        raise ValueError("original complete derivative certificate scope changed")
    answer={}
    for name,weight in (("matrix_normalized_L2",2),("original_L4",4)):
        terms={}
        for row in data["groups"][name]["geometry_coefficients"]:
            key=tuple(row["geometry_key"])
            if key in terms or len(key)!=10 or factors.geometry_weight(key)!=weight:
                raise ValueError("complete derivative geometry packets overlap or are malformed")
            terms[key]=Packet(first.polynomial_from_rows(row["complete_polynomial"]),
                {int(i):F(value) for i,value in row["original_response_coefficients"]},
                first.polynomial_from_rows(row["complete_remainder"]))
        value=GeometryPackets(ring,terms)
        value.check(columns,{weight})
        answer[weight]=value
    report["complete_derivative_input"]={"publication":binding,
        "compact_main_sha256":sha(raw),"publication_receipt_sha256":sha(publication_raw),
        "complete_certificate":metadata,
        "source_geometric_coefficients":{str(w):len(v.terms) for w,v in answer.items()},
        "whole_R124_correction_retained":True,"original_N2_and_v2_v4_retained":True,
        "old_profile_substitutions_recomputed":False,"old_response_formulas_recomputed":False}
    return answer


def packet_rows(value):
    return [{"geometry_key":list(key),**packet.rows()} for key,packet in sorted(value.terms.items())]


def semantic_support(value):
    """Observe every coefficient; R85/R88 is never used to clip or reject data."""
    scopes={"complete_polynomial":[],"original_response_part":[],"complete_remainder":[]}
    for key,packet in value.terms.items():
        response=dict(packet.polynomial)
        source.add_sparse(response,packet.remainder,F(-1),value.ring)
        scopes["complete_polynomial"].append(packet.polynomial)
        scopes["original_response_part"].append(response)
        scopes["complete_remainder"].append(packet.remainder)
    answer={}
    for name,polynomials in scopes.items():
        support=set();below=set();coefficient_count=below_count=below_geometry=0
        nonzero_geometry=0
        for polynomial in polynomials:
            rows={row for row,coefficient in polynomial.items() if coefficient}
            low={row for row in rows if row[1]<25}
            support.update(rows);below.update(low)
            coefficient_count+=len(rows);below_count+=len(low)
            nonzero_geometry+=bool(rows);below_geometry+=bool(low)
        answer[name]={
            "geometry_coefficients_with_nonzero_polynomial":nonzero_geometry,
            "nonzero_monomial_coefficients":coefficient_count,
            "distinct_monomials":len(support),
            "minimum_r_power":min((row[1] for row in support),default=None),
            "maximum_r_power":max((row[1] for row in support),default=None),
            "maximum_total_degree":max((sum(row) for row in support),default=None),
            "below_r25_geometry_coefficients":below_geometry,
            "below_r25_monomial_coefficients":below_count,
            "below_r25_distinct_rows":[list(row) for row in sorted(below)],
            "below_r25_coefficients_all_zero":not below}
    answer["semantic_observation_only_no_clipping_or_failure_gate"]=True
    return answer


def actual(args,report):
    if (os.environ.get("GITHUB_ACTIONS","").lower()!="true"
        or os.environ.get("GITHUB_REPOSITORY")!=source.REPOSITORY):
        raise RuntimeError("the real horizontal geometry target is restricted to public Actions")
    started=time.monotonic()
    ring=projection.TailRing(args.max_seconds,args.memory_mib,args.max_operations)
    columns,weights,pivots,ranks=constraint.load_response_columns(args,report)
    inputs=load_complete_source(args,columns,ring,report)
    P1,N2=quadratic_normal_form(inputs[2])
    P3,N4,parts,potential_parts=quartic_normal_form(inputs[4])
    for weight,potential,normal in ((2,P1,N2),(4,P3,N4)):
        potential.check(columns,{weight-1});normal.check(columns,{weight})
        difference=inputs[weight].plus(potential.total_derivative(),F(-1)).plus(normal,F(-1))
        if not difference.zero():
            raise AssertionError("whole original P/A/R identity L=D_s potential+normal failed")
    combined=N2.plus(N4)
    groups={};full_groups={}
    targets=[("normal_velocity_quadratic",N2,{2}),
             ("normal_full_weight_four",N4,{4}),
             ("normal_complete_derivative_density",combined,{2,4})]
    targets += [(name,value,{4}) for name,value in parts.items() if name!="area_multiplier_H"]
    for name,value,allowed in targets:
        groups[name],full_groups[name]=source.summarize(name,value.terms,columns,weights,pivots,ring,allowed)
    support={name:semantic_support(value) for name,value in (
        ("normal_velocity_quadratic",N2),("normal_full_weight_four",N4),
        ("normal_complete_derivative_density",combined))}
    certificate={"schema":SCHEMA+"-certificate","github_run_id":report["github_run_id"],
        "github_sha":report["github_sha"],"source_hashes":report["source_hashes"],
        "complete_derivative_input":report["complete_derivative_input"],
        "input_response":report["input_response"],"geometry_names":list(factors.GEOMETRY_NAMES),
        "groups":full_groups,"normal_semantic_support":support,
        "boundary_potential_weight_one":packet_rows(P1),
        "boundary_potential_weight_three":packet_rows(P3),
        "boundary_potential_components":{name:packet_rows(value) for name,value in potential_parts.items()},
        "complete_area_multiplier_H":packet_rows(parts["area_multiplier_H"]),
        "real_omega_derivative":"omega_s=k_s/(2h)",
        "all_complete_original_P_A_R_identity_differences_zero":True,
        "boundary_vanishes_condition":"constant germs imply h_s=k_s=h_ss=k_ss=0",
        "weight_zero_endpoint_potentials_removed":False,
        "actual_M0_path_or_period_sign_evaluated":False}
    exported=source.write_complete_certificate(args.out.with_name(args.out.stem+"-certificate.json.gz"),certificate)
    report.update(completion="complete",complete_certificate=exported,groups=groups,
        normal_semantic_support=support,
        all_complete_original_P_A_R_identity_differences_zero=True,
        both_nonsymmetric_velocity_squared_acceleration_terms_kept=True,
        all_horizontal_coefficient_chain_rule_terms_kept=True,
        maximum_remaining_geometry_jet_order=max(
            (2 if key[A] or key[B] else 1 if key[U] or key[W] else 0
             for key in combined.terms),default=0),
        endpoint_potential_packets={"weight_one":len(P1.terms),"weight_three":len(P3.terms)},
        original_profile_formula_evaluations=0,response_formula_evaluations=0,
        actual_geometry_or_period_sign_evaluated=False,
        linear_operations=ring.linear_operations,polynomial_operations=ring.operations,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,task_complete=False)
    return report


def toy_only():
    ring=projection.TailRing(40,256,100000)
    def artificial(terms):
        return GeometryPackets(ring,{key:Packet({(0,0):F(value)},{},{(0,0):F(value)})
                                     for key,value in terms.items()})
    def key(**powers):
        value=list(GZERO)
        for index,power in powers.items():
            value[int(index)]=power
        return tuple(value)
    # omega*a gives exact -u*w/(2h), and u*j gives -a^2.
    omega_a=artificial({key(**{str(O):1,str(A):1}):1})
    p1,n2=quadratic_normal_form(omega_a)
    expected2=artificial({key(**{str(H):-1,str(U):1,str(W):1}):F(-1,2)})
    uj=artificial({key(**{str(U):1,str(J):1}):1})
    p3,n4,parts,details=quartic_normal_form(uj)
    expected4=artificial({key(**{str(A):2}):-1})
    # u*w*a has a genuine non-gradient residual after cubic homotopy.
    uwa=artificial({key(**{str(U):1,str(W):1,str(A):1}):1})
    pp,nn,pieces,ignored=quartic_normal_form(uwa)
    expected_area=artificial({key(**{str(U):1,str(W):1,str(A):1}):F(1,3),
                              key(**{str(U):2,str(B):1}):F(-1,3)})
    log=artificial({key(**{str(LOGH):2,str(U):1}):1})
    log_expected=artificial({key(**{str(LOGH):1,str(H):-1,str(U):1}):2})
    checks={
        "real_omega_chain_rule_survives":n2.plus(expected2,F(-1)).zero(),
        "third_jet_term_pays_acceleration_square":n4.plus(expected4,F(-1)).zero(),
        "both_nonsymmetric_acceleration_terms_survive":nn.plus(expected_area,F(-1)).zero(),
        "Laurent_log_chain_rule_is_exact":log.partial(H).plus(log_expected,F(-1)).zero(),
        "complete_P_A_R_boundary_identity":(
            uwa.plus(pp.total_derivative(),F(-1)).plus(nn,F(-1)).zero()),
        "no_research_input_or_profile_evaluated":True}
    if not all(checks.values()):
        raise AssertionError("new artificial horizontal IBP checks failed")
    return {"completion":"complete","mode":"small_artificial_development_only",
            "checks":checks,"all_passed":True,"task_complete":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out",required=True,type=Path)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--source-report",type=Path)
    parser.add_argument("--source-report-sha256")
    parser.add_argument("--source-publication-receipt",type=Path)
    parser.add_argument("--source-publication-sha256")
    parser.add_argument("--source-certificate",type=Path)
    parser.add_argument("--source-certificate-sha256")
    parser.add_argument("--source-run")
    parser.add_argument("--source-commit")
    parser.add_argument("--response-report",type=Path,default=first.RESPONSE_DIRECTORY/"full-m8-tail-response.json")
    parser.add_argument("--response-publication-receipt",type=Path,default=first.RESPONSE_DIRECTORY/"receipt.json")
    parser.add_argument("--response-certificate",type=Path,default=first.RESPONSE_DIRECTORY/first.RESPONSE_EXPORT["filename"])
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-operations",type=int,default=3000000)
    args=parser.parse_args()
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","github_run_id":os.environ.get("GITHUB_RUN_ID"),
            "github_sha":os.environ.get("GITHUB_SHA"),"task_complete":False}
    failed=False
    try:
        report["source_hashes"]=dependencies()
        report.update(toy_only() if args.toy_only else actual(args,report))
    except Exception as error:
        failed=True
        report.update(completion="incomplete",error_type=type(error).__name__,error=str(error),
                      new_mathematical_conclusion_published=False,task_complete=False)
    report["wall_seconds"]=time.monotonic()-started
    raw=canonical(report)+b"\n"
    if len(raw)>95000:
        exported=first.write_gzip(args.out.with_name(args.out.stem+"-full-report.json.gz"),report)
        report={key:report[key] for key in ("schema","completion","github_run_id","github_sha", "source_hashes",
            "complete_certificate","complete_derivative_input","input_response","wall_seconds",
            "normal_semantic_support",
            "error_type","error","task_complete") if key in report}
        report.update(compact_fallback=True,complete_report=exported)
        raw=canonical(report)+b"\n"
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(raw)
    print(json.dumps({"filename":args.out.name,"bytes":len(raw),"sha256":sha(raw)},sort_keys=True),flush=True)
    if failed:
        raise SystemExit(1)


if __name__=="__main__":
    main()
