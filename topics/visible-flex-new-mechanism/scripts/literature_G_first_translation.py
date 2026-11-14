#!/usr/bin/env python3
"""R122: the first true translation derivative of G modulo complete R8.

Only consumes published original expressions.  No forcing, local-density or W
compiler.  One weight-zero block; a proved membership stops the whole orbit.
A failed word reduction is not a nonmembership certificate.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_static_G_rational_dual as seed

static=seed.static
old=seed.old
dual=seed.dual
poly=seed.poly
colored=seed.colored
exact=seed.exact
formal=seed.formal
blocks=seed.blocks
MODES=seed.MODES
SCHEMA="visible-flex-G-first-translation-original-v1"
G_DRIVER_SHA="0872f0fc8b561a547342d530239e35c6ac9a37a5bddc5c472bf16c0df73ac477"
G_MAIN_BYTES=13817
G_MAIN_SHA="743594e95eedda896410cc20a30949675899e075bacc262fa5192388dbeba7f9"
G_PUBLICATION_BYTES=32065
G_PUBLICATION_SHA="6392f3554aa656c4ab7cadc11c56ed2e4ee5d8a250b857a7d9a1014e8be0e4cc"
G_RUN="43647225907"
G_COMMIT="b466c3782ae5e3b1a68572065b7505d45e6d8a99"
G_DIR=Path(__file__).resolve().parents[1]/"notes"/("actions-"+G_RUN+"-1-static_g_rational_dual")
ZERO_SHA=seed.ZERO_SHA

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()

def sha(value):
    return hashlib.sha256(value).hexdigest()

def source_identity():
    value=seed.sources()
    if value["driver"]["sha256"]!=G_DRIVER_SHA:
        raise ValueError("explicitly rebind the completed original G producer")
    value["G_input_producer"]=value.pop("driver")
    value["driver"]=static.identity(__file__)
    return value

def bind_G_certificate(args,report):
    raw=static.checked_bytes(args.G_report,100000)
    publication_raw=static.checked_bytes(args.G_publication,100000)
    if (len(raw)!=G_MAIN_BYTES or sha(raw)!=G_MAIN_SHA
        or len(publication_raw)!=G_PUBLICATION_BYTES or sha(publication_raw)!=G_PUBLICATION_SHA):
        raise ValueError("the completed G certificate/publication identity changed")
    value=json.loads(raw)
    publication=json.loads(publication_raw)
    checkpoint=value.get("checkpoint",{})
    witness=checkpoint.get("dual_certificate",{})
    if (value.get("schema")!=seed.SCHEMA or value.get("completion")!="complete"
        or value.get("github_repository")!=static.REPOSITORY
        or value.get("github_run_id")!=G_RUN or value.get("github_sha")!=G_COMMIT
        or value.get("source_hashes",{}).get("driver",{}).get("sha256")!=G_DRIVER_SHA
        or not checkpoint.get("universal_G_not_in_full_R8_by_true_weight_decomposition")
        or not witness.get("rational_nonmembership_certified")
        or witness.get("control_columns")!=7
        or witness.get("modular_pivot_determinant")!=1896063777
        or witness.get("modular_augmented_determinant")!=2093208697):
        raise ValueError("a completed original G nonmembership certificate is required")
    if (publication.get("schema")!="visible-new-mechanism-actions-v1"
        or publication.get("repository")!=static.REPOSITORY
        or str(publication.get("run_id"))!=G_RUN
        or publication.get("source_commit")!=G_COMMIT
        or publication.get("lane")!="static_g_rational_dual"):
        raise ValueError("G terminal-publication provenance")
    outputs=[x for x in publication.get("outputs",[]) if x.get("path")==args.G_report.name]
    if len(outputs)!=1 or any(outputs[0].get(k)!=v for k,v in (
        ("bytes",len(raw)),("sha256",sha(raw)),("raw_bytes",len(raw)),("raw_sha256",sha(raw)))):
        raise ValueError("G main bytes were not bound by the terminal publisher")
    key="topics/visible-flex-new-mechanism/scripts/literature_static_G_rational_dual.py"
    if publication.get("source_files",{}).get(key)!={
            "bytes":16444,"sha256":G_DRIVER_SHA}:
        raise ValueError("G producer source missing from terminal receipt")
    report["completed_G_input"]={"run":G_RUN,"commit":G_COMMIT,
        "main":{"filename":args.G_report.name,"bytes":len(raw),"sha256":sha(raw)},
        "publication":{"filename":args.G_publication.name,"bytes":len(publication_raw),
                       "sha256":sha(publication_raw)},
        "original_G_nonmembership_consumed":True,"old_seven_columns_reevaluated":False}

class TranslationGenerator:
    """True simultaneous right-anchor translation: N(x)=1, N(jets)=0.

    N commutes with I from the moving common right endpoint.  Every original
    primitive has positive profile degree, so its empty right collar pays
    the endpoint term.  This is not the full xi derivative of the input.
    """
    def __init__(self,ring):
        self.ring=ring
        self.atom_cache={}
        self.monomial_cache={}
        self.degree_atoms={}
        self.degree_monomials={}

    def atom(self,index):
        if index not in self.atom_cache:
            node=self.ring.p.atoms[index]
            if node[0]=="jet":
                value=self.ring.number(0)
            elif node[0]=="int_right":
                if self.ring.p.weight(node[1])<=0:
                    raise ValueError("moving-anchor translation requires positive profile degree")
                value=self.monomial(node[1]).I()
            else:
                raise ValueError("unsupported original atom in translation")
            self.atom_cache[index]=value
        return self.atom_cache[index]

    def monomial(self,key):
        if key not in self.monomial_cache:
            power,atoms=key
            if power<0:
                raise ValueError("this finite translation chain excludes coordinate poles")
            value=self.ring.number(0)
            if power:
                value+=power*self.ring.monomial((power-1,atoms))
            for atom,count in Counter(atoms).items():
                rest=list(atoms)
                rest.remove(atom)
                value+=count*self.ring.monomial((power,tuple(rest)))*self.atom(atom)
            self.monomial_cache[key]=value
            self.ring.limits.check()
        return self.monomial_cache[key]

    def expression(self,value):
        result=self.ring.number(0)
        for key,coefficient in value.terms.items():
            result+=coefficient*self.monomial(key)
        return result

    def atom_degree(self,index):
        if index not in self.degree_atoms:
            node=self.ring.p.atoms[index]
            if node[0]=="jet":
                value=0
            elif node[0]=="int_right":
                value=self.monomial_degree(node[1])
            else:
                raise ValueError("unsupported atom for finite translation degree")
            self.degree_atoms[index]=value
        return self.degree_atoms[index]

    def monomial_degree(self,key):
        if key not in self.degree_monomials:
            if key[0]<0:
                raise ValueError("negative coordinate powers are outside finite translation")
            self.degree_monomials[key]=key[0]+sum(self.atom_degree(a) for a in key[1])
        return self.degree_monomials[key]

    def degree(self,value):
        return max((self.monomial_degree(key) for key in value.terms),default=-1)

class ExactShift:
    """Independent finite pullback x->x+d, fixed transported jets and I."""
    def __init__(self,ring,shift):
        self.ring,self.shift=ring,F(shift)
        self.atoms,self.monomials={},{}
    def atom(self,index):
        if index not in self.atoms:
            node=self.ring.p.atoms[index]
            if node[0]=="jet":
                value=self.ring.monomial((0,(index,)))
            elif node[0]=="int_right":
                if self.ring.p.weight(node[1])<=0:
                    raise ValueError("unpaid moving right boundary")
                value=self.monomial(node[1]).I()
            else:
                raise ValueError("unsupported shift atom")
            self.atoms[index]=value
        return self.atoms[index]
    def monomial(self,key):
        if key not in self.monomials:
            if key[0]<0:
                raise ValueError("polynomial shift only")
            value=(self.ring.x()+self.shift)**key[0]
            for atom in key[1]:
                value*=self.atom(atom)
            self.monomials[key]=value
        return self.monomials[key]
    def expression(self,value):
        return sum((c*self.monomial(key) for key,c in value.terms.items()),self.ring.number(0))

def fresh_zero(ring,target,columns,coefficients):
    """Recombine original expressions, then prove both original functions zero."""
    normalizer=colored.ColoredNormalizer(ring)
    checks={}
    for mode in MODES:
        difference=target[mode]
        for index,amount in coefficients.items():
            difference-=amount*columns[index][mode]
        verified=normalizer.word.expression(difference)
        if verified.terms:
            raise AssertionError("a proposed original identity did not reverify")
        checks[str(mode)]={"original_difference_sha256":ring.digest(difference),
            "verified_zero_sha256":verified.digest()}
    return checks

def raw_evaluation(args,ring,target,templates,labels,retained,report,remaining):
    context=poly.PolynomialContext(args.prime,2,3,seconds=remaining,
        max_degree=args.max_degree,memory_mib=args.memory_mib,max_operations=args.max_operations)
    try:
        _,_,profiles=dual.fixed_profiles(context,args.bump_power)
        evaluator=poly.RawExpressionEvaluator(ring.p,context,context.colors)
        target_values={mode:evaluator.expression(value) for mode,value in target.items()}
        points=[F(j,args.points+1) for j in range(1,args.points+1)]
        row_labels=[{"t":str(t),"xi":str(context.left+context.width*t),
                     "mode":mode,"component":component}
                    for t in points for mode in MODES for component in ("real","imaginary")]
        def rows(modes):
            return [v for t in points for mode in MODES for v in modes[mode].value(t)]
        b=rows(target_values)
        quadratic=exact.operator_basis(context)
        values=[]
        records=[]
        for index in retained:
            label=labels[index]
            third=poly.EvaluatedThirdOperator(ring.p,context,templates[label["third_index"]])
            value=blocks.full_response(context,third,quadratic[label["quadratic_index"]])
            values.append(rows(value))
            records.append({"original_block_column":index,
                "modes":{str(mode):{"sha256":value[mode].digest(),
                                  "degree":len(value[mode].coefficients)-1} for mode in MODES}})
            report["checkpoint"]["original_evaluated_columns"]=len(values)
            context.check(0)
        matrix=[[column[i] for column in values] for i in range(len(row_labels))]
        witness=poly.full_column_dual(matrix,b,args.prime)
        if witness["rational_nonmembership_certified"]:
            witness["selected_evaluation_labels"]=[
                row_labels[i] for i in witness["selected_augmented_rows"]]
        return {"fixed_profiles":profiles,"same_fixed_pair_for_all_modes_and_columns":True,
            "row_count":len(row_labels),"all_evaluation_labels":row_labels,
            "matrix_sha256":sha(canonical(matrix)),"target_sha256":sha(canonical(b)),
            "original_evaluated_controls":records,
            "target_mode_polynomials":{str(mode):{"sha256":target_values[mode].digest(),
                "degree":len(target_values[mode].coefficients)-1} for mode in MODES},
            "dual_certificate":witness}
    finally:
        report["coefficient_checkpoint"]=context.coefficient_report()

def study(args,report,started):
    limits=exact.Limits(args.max_seconds,500000,100000,120000,500000,args.memory_mib,8192)
    ring=colored.ColoredRing(limits)
    report["phase"]="bound_original_G_and_published_nonmembership"
    bind_G_certificate(args,report)
    templates,original,_=seed.load_G_and_bound(args,ring,report)
    generator=TranslationGenerator(ring)
    target={mode:generator.expression(value) for mode,value in original.items()}
    grade=blocks.ScalingGrading(ring)
    if any(set(grade.split(value))-{0} for value in target.values()):
        raise AssertionError("the true translation of a weight-one target must have weight zero")
    report["translation"]={"order":1,"rule":"N(x)=1; N(jets)=0; N(I F)=I(N F)",
        "common_right_anchor_transport_explicit":True,
        "full_xi_derivative_used_as_translation":False,
        "original_G_sha256":{str(m):ring.digest(v) for m,v in original.items()},
        "original_NG_sha256":{str(m):ring.digest(v) for m,v in target.items()},
        "finite_coordinate_degree_upper_bound":max(generator.degree(v) for v in original.values()),
        "new_raw_terms":{str(m):len(v.terms) for m,v in target.items()}}
    normalizer=colored.ColoredNormalizer(ring)
    target_vector=colored.vector_from_modes(target,normalizer)
    report["target_word_representative"]={"terms":len(target_vector),
        "sha256":colored.vector_digest(target_vector),"independence_not_assumed":True}
    if not target_vector:
        report["checkpoint"]={"outcome":"target_zero_verified",
            "fresh_original_checks":fresh_zero(ring,target,[],{}),
            "orbit_dimension_exact":1,"further_translation_orders_needed":False}
        report["completion"]="complete"
        return

    labels=[]
    for i,wi in enumerate(blocks.PARAMETER_WEIGHTS):
        for j,wj in enumerate(blocks.THIRD_WEIGHTS):
            if wi+wj==0:
                labels.append({"quadratic_index":i,"quadratic_name":exact.PARAMETERS[i],
                    "third_index":j,"third_weight":wj,
                    "v2_original_third_index":blocks.EXPECTED_KEPT[j],
                    "third_original_sha256":ring.digest(templates[j])})
    report["all_original_response_columns"]=labels
    report["response_coverage"]={"full_E8":True,"all_W36":True,
        "weight":0,"columns":len(labels),"physical_seven_dimensional_subspace_not_substituted":True}
    template_checks=[]
    for j in sorted({x["third_index"] for x in labels}):
        difference=templates[j]-grade.project(templates[j],blocks.THIRD_WEIGHTS[j])
        proof=normalizer.word.expression(difference)
        if proof.terms:
            raise AssertionError("bound true third basis weight changed")
        template_checks.append({"third_index":j,"zero_sha256":proof.digest()})
    report["template_weight_checks"]=template_checks
    quadratics=exact.operator_basis(ring)
    columns=[]
    vectors=[]
    report["phase"]="complete_weight_zero_original_responses"
    for index,label in enumerate(labels):
        third=colored.ThirdOperator(ring,templates[label["third_index"]])
        value=blocks.full_response(ring,third,quadratics[label["quadratic_index"]])
        vector=colored.vector_from_modes(value,normalizer)
        columns.append(value);vectors.append(vector)
        label["original_mode_sha256"]={str(m):ring.digest(v) for m,v in value.items()}
        label["word_terms"]=len(vector);label["word_sha256"]=colored.vector_digest(vector)
        report["checkpoint"]={"completed_original_columns":len(columns),"total_columns":len(labels),
            "identity_or_nonmembership_proved":False}
        ring.substitution_cache.clear()
        limits.formal.time_check()
        print(json.dumps({"phase":report["phase"],"columns":len(columns),"of":len(labels)}),flush=True)

    regularity=dual.reachable_jet_bound(ring,list(target.values())+
        [value for modes in columns for value in modes.values()])
    report["input_regularity"]=regularity
    if regularity["maximum_input_jet"]>args.bump_power-1:
        raise ValueError("increase the fixed bump power before using this higher-jet block")
    report["phase"]="sound_original_response_upper_bound"
    span=colored.JointSpan(vectors,limits)
    retained=span.independent
    dependencies=[]
    for index,vector in enumerate(vectors):
        if index in retained:
            continue
        coefficients,remainder=span.reduce(vector)
        if remainder or not set(coefficients).issubset(retained):
            raise AssertionError("retained original spanning certificate")
        target_relation=columns[index]
        checks=fresh_zero(ring,target_relation,columns,coefficients)
        dependencies.append({"discarded_original_column":index,
            "retained_original_coefficients":[[j,str(c)] for j,c in sorted(coefficients.items())],
            "fresh_original_checks":checks})
    report["response_upper_bound"]={"original_columns":len(labels),
        "retained_original_columns":retained,
        "proved_true_response_dimension_upper_bound":len(retained),
        "verified_original_dependencies":dependencies,
        "representative_rank_not_promoted_to_independence":True}
    coefficients,remainder=span.reduce(target_vector)
    report["word_remainder"]={"terms":len(remainder),"sha256":colored.vector_digest(remainder),
        "nonmembership_claimed_from_remainder":False}
    report["candidate_coefficients"]=[[j,str(c)] for j,c in sorted(coefficients.items())]
    if not remainder:
        checks=fresh_zero(ring,target,columns,coefficients)
        report["checkpoint"]={"outcome":"member_identity_verified",
            "same_coefficients_for_both_modes":[[j,str(c)] for j,c in sorted(coefficients.items())],
            "fresh_original_checks":checks,"orbit_dimension_exact":1,
            "further_translation_orders_needed":False}
        report["completion"]="complete"
        return

    report["phase"]="original_rational_weight_zero_evaluation"
    remaining=args.max_seconds-(time.monotonic()-started)
    if remaining<=0:
        raise poly.PolynomialBudgetExceeded("time budget before original rational evaluation")
    report["checkpoint"]={"completed_original_columns":len(labels),
        "proved_response_upper_bound":len(retained),"original_evaluated_columns":0}
    report["original_evaluation"]=raw_evaluation(args,ring,target,templates,labels,retained,
                                                report,remaining)
    witness=report["original_evaluation"]["dual_certificate"]
    certified=witness["rational_nonmembership_certified"]
    report["checkpoint"]={"outcome":"nonmember_certified" if certified else "undecided",
        "proved_response_upper_bound":len(retained),"dual_certificate":witness,
        "universal_NG_nonmember_in_full_R8":certified,
        "orbit_dimension_lower_bound":2 if certified else 1,
        "orbit_dimension_exact":None,"further_translation_orders_computed":False,
        "fixed_test_pair_all_other_weights_excluded":False}
    report["completion"]="complete"

def small_toy():
    limits=exact.Limits(seconds=30,nodes=10000,atoms=5000,terms=5000,
                        rewrites=10000,memory_mib=256)
    ring=colored.ColoredRing(limits)
    q,qb,x=ring.color("q"),ring.color("qbar"),ring.x()
    N=TranslationGenerator(ring)
    value=x*x*q.I()+(x*q*qb.D()).I()*q
    expected=2*x*q.I()+(q*qb.D()).I()*q
    checks={}
    def same(a,b,label):
        if (a-b).terms:
            raise AssertionError(label)
        checks[label]=True
    same(N.expression(value),expected,"explicit_coordinate_and_nested_primitive_derivative")
    same(N.expression(expected),2*q.I(),"second_translation_not_full_profile_derivative")
    same(N.expression(N.expression(expected)),ring.number(0),"finite_third_translation_zero")
    same(N.expression(value.I()),N.expression(value).I(),"true_translation_commutes_with_right_primitive")
    same(N.expression(value.D()),N.expression(value).D(),"true_translation_commutes_with_total_derivative")
    shift=F(3,2)
    taylor=value+shift*N.expression(value)+shift**2*N.expression(N.expression(value))/2
    same(ExactShift(ring,shift).expression(value),taylor,"finite_shift_equals_true_nilpotent_exponential")
    grade=blocks.ScalingGrading(ring)
    for weight,part in grade.split(value).items():
        if set(grade.split(N.expression(part)))-{weight-1}:
            raise AssertionError("translation weight")
    checks["translation_lowers_true_affine_weight"]=True
    if N.degree(value)!=2:
        raise AssertionError("finite coordinate degree through nested integrals")
    checks["exact_coordinate_degree_bound"]=True
    dependency=seed.artificial_toys()
    return {"checks":checks,"all_passed":all(checks.values()) and dependency["all_passed"],
        "existing_small_interfaces":dependency,"original_G_read":False,
        "research_profile_evaluated":False,"research_compiler_called":False}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--source-report",type=Path,default=static.DEFAULT_DIR/"local-fourth-quotient.json")
    parser.add_argument("--source-report-sha256",default=static.REPORT_SHA)
    parser.add_argument("--source-run",default=static.SOURCE_RUN)
    parser.add_argument("--source-commit",default=static.SOURCE_COMMIT)
    parser.add_argument("--publication-receipt",type=Path,default=static.DEFAULT_DIR/"receipt.json")
    parser.add_argument("--publication-receipt-sha256",default=static.PUBLICATION_SHA)
    parser.add_argument("--input-export",type=Path,default=static.DEFAULT_DIR/"local-fourth-quotient-original-expressions.json.gz")
    parser.add_argument("--export-sha256",default=static.EXPORT_SHA)
    parser.add_argument("--third-receipt",type=Path,default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--block-receipt",type=Path,default=static.DEFAULT_DIR/"local-fourth-quotient-weight-+1.json")
    parser.add_argument("--G-report",type=Path,default=G_DIR/"static-G-rational-dual.json")
    parser.add_argument("--G-publication",type=Path,default=G_DIR/"receipt.json")
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-degree",type=int,default=256)
    parser.add_argument("--max-operations",type=int,default=10000000)
    parser.add_argument("--points",type=int,default=24)
    parser.add_argument("--bump-power",type=int,default=8)
    parser.add_argument("--prime",type=int,default=2147483647)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2500000)
    args=parser.parse_args()
    if (min(args.max_seconds,args.memory_mib,args.max_degree,args.max_operations,args.points,
            args.max_main_bytes,args.max_full_report_bytes)<=0 or args.bump_power<8):
        parser.error("positive bounded budgets and bump power at least eight")
    if args.prime%4!=3 or args.points+1>=args.prime:
        parser.error("the checked prime must be 3 mod 4 and exceed query denominators")
    if not 10000<=args.max_main_bytes<100000:
        parser.error("small main report must reserve 10000..99999 bytes")
    if args.max_main_bytes+args.max_full_report_bytes>static.TOTAL_BYTES:
        parser.error("total published output ceiling")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
                                 and os.environ.get("GITHUB_REPOSITORY")==static.REPOSITORY):
        parser.error("genuine original-expression research only in this public repository Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},"completed_blocks":[],
        "scope":"one original first-translation universal membership block, complete two modes",
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "max_degree":args.max_degree,"max_operations":args.max_operations,
            "main_bytes":args.max_main_bytes,"complete_report_bytes":args.max_full_report_bytes},
        "old_forcing_recompiled":False,"W_recompiled":False,"local_density_recompiled":False,
        "old_G_separation_reevaluated":False,"full_fourth_cost_paid":False,
        "ruling_paid":False,"finite_isometric_family_constructed":False}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["phase"]="small_artificial_translation_interfaces"
            report["toy"]=small_toy();report["completion"]="toy_passed"
        else:
            study(args,report,started)
    except (formal.CompilationBudgetExceeded,poly.PolynomialBudgetExceeded) as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    if "translation" in report:
        report.setdefault("checkpoint",{})["original_translation_target"]=report["translation"]
    if "response_upper_bound" in report:
        upper=report["response_upper_bound"]
        report.setdefault("checkpoint",{})["response_upper_bound"]={
            "original_columns":upper["original_columns"],
            "retained_original_columns":upper["retained_original_columns"],
            "proved_true_response_dimension_upper_bound":upper["proved_true_response_dimension_upper_bound"],
            "verified_original_dependency_count":len(upper["verified_original_dependencies"]),
            "verified_original_dependencies_sha256":sha(canonical(upper["verified_original_dependencies"])),
            "complete_original_dependency_proofs_in_full_report":True}
    if "completed_G_input" in report:
        report.setdefault("checkpoint",{})["completed_G_input"]=report["completed_G_input"]
    if "input_regularity" in report:
        report.setdefault("checkpoint",{})["input_regularity"]=report["input_regularity"]
    positive=(report.get("checkpoint") or {}).get("same_coefficients_for_both_modes")
    if positive is not None and len(canonical(positive))>16000:
        report["positive_identity_coefficients"]=positive
        del report["checkpoint"]["same_coefficients_for_both_modes"]
        report["checkpoint"]["positive_coefficients"]={
            "count":len(positive),"sha256":sha(canonical(positive)),
            "complete_rational_coefficients_in_full_report":True}
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    written=static.publish_report(args.output,report,args.max_main_bytes,args.max_full_report_bytes)
    if written["completion"]=="output_limit":
        code=2
    print(json.dumps({"output":str(args.output),**written}),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
