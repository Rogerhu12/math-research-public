#!/usr/bin/env python3
"""Real R824-origin normal source adapter for the unchanged original R825 derivative arithmetic."""
import argparse
import importlib.util
from pathlib import Path
import sys
import time

DERIVATIVE_NAME="R825_original_normal_derivative_inputs.py"
DERIVATIVE_SHA="89579f796e0f62132b37aa081719f7e7a7d62b87e7ef789d19289a8edaa462e1"
FRAMEWORK_SHA="849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
PROOF_SHA="73f9f293f0a0526a2f1eed8b62aea562b659090b546d1e122c0e12dbd1f90930"
METHOD_SHA="fa3d8a19fa1dfdecbd68a903667b506e94a338a073c19bde2a907afe83d227af"
NORMAL_RESULT="R809-original-A-B-normal-coordinates-from-R824"
NORMAL_SHA="cdc381fc5e1b9dfab705608f1d62a8ab80b282984479499a6edd635ea05fa62b"
BASIS_SHA="dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d"
S5_INDEX_SHA="f6f6f0ee2bae106ef474d2cff32c743b1d8e0a886f80c26aaf8708c89ea1c119"

def source_sha(path):
    import hashlib
    digest=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1024*1024),b""):
            digest.update(block)
    return digest.hexdigest()

scripts=Path(__file__).resolve().parent
assert source_sha(scripts/"R811_original_regular_multipliers.py")==FRAMEWORK_SHA
assert source_sha(scripts/DERIVATIVE_NAME)==DERIVATIVE_SHA
loader=importlib.util.spec_from_file_location("R825_R824_frozen_derivative_arithmetic",scripts/DERIVATIVE_NAME)
base=importlib.util.module_from_spec(loader)
loader.loader.exec_module(base)
flint,framework=base.flint,base.framework
Retained,BudgetStop,guard=base.Retained,base.BudgetStop,base.guard
sha,read,save,spec,plain,fingerprint=base.sha,base.read,base.save,base.spec,base.plain,base.fingerprint
producer_identity,same_producer=base.producer_identity,base.same_producer
FREE,S5,EPS,FIELD,TARGETS,CHARTS,SCOPE=base.FREE,base.S5,base.EPS,base.FIELD,base.TARGETS,base.CHARTS,base.SCOPE
RESULT="R825-original-normal-derivatives-from-R824-normal-vectors"
FINAL="p41-original-normal-derivatives-from-R824-certificate.json"

def relation_source_identity(item):
    value={key:item[key] for key in
           ("result","run_id","source_commit","core_sha256","manifest_sha256")}
    name=item["certificate_name"]
    value["certificate"]={"file":name,"sha256":item["files"][name]}
    return value

class Job(base.Job):
    def __init__(self,args):
        self.args,self.out,self.started=args,args.output,time.monotonic()
        self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["requested_stage"]==SCOPE and self.item["producer_inputs_pending"] is False
        assert self.item["requested_targets"]==list(TARGETS) and self.item["matrix_row_block_size"]==16
        assert sha(__file__)==self.item["core_sha256"]
        assert sha(args.proof)==self.item["R825_proof_sha256"]==PROOF_SHA
        assert sha(args.method)==self.item["R825_adapter_method_sha256"]==METHOD_SHA
        assert self.item["derivative_framework"]==DERIVATIVE_NAME
        assert self.item["derivative_framework_sha256"]==DERIVATIVE_SHA
        assert sha(framework.__file__)==self.item["framework_sha256"]==FRAMEWORK_SHA
        assert flint.__version__=="0.9.0"
        assert set(self.item["retained_artifacts"])=={"R809","R809_basis","R815","R820"}
        self.inputs={label:Retained(args.retained,label,self.item["retained_artifacts"][label])
                     for label in ("R809","R809_basis","R815","R820")}
        self.r809,self.r815,self.r820=(self.inputs[label] for label in ("R809","R815","R820"))
        self.r809_basis=self.inputs["R809_basis"]
        c9,c15,c20=(p.certificate for p in (self.r809,self.r815,self.r820))
        assert self.r809.identity["result"]==NORMAL_RESULT
        assert self.r809.identity["core_sha256"]==NORMAL_SHA
        assert self.r809_basis.identity["result"]=="R809-original-S5-normal-coordinates"
        assert self.r809_basis.identity["core_sha256"]==BASIS_SHA
        cbasis=self.r809_basis.certificate
        assert c9["completed_scope"]=="A_and_B_only_from_one_true_R824_relation"
        assert c9["completed_rational_RHS_columns"]==28
        assert c9["all28_rational_RHS_columns_verified_in_all1380_rows"] is True
        assert c9["external_S5_references_keep_their_original_configuration"] is True
        assert c9["normal_function_equation"]=="y=normal(A)/normal(B)"
        assert c9["original_R824_denominator_and_content_reinserted"] is False
        assert c9["synthetic_original_R809_or_R787_result_created"] is False
        assert c9["original_S5_producer"]==relation_source_identity(self.r809_basis.identity)
        assert self.r809.tag["source_identities"]["R809"]==relation_source_identity(self.r809_basis.identity)
        assert self.r809.tag["original_S5_configuration_sha256"]==fingerprint(self.r809_basis.tag)
        assert c9["actual_R824_source"]==self.r809.tag["actual_R824_source"]
        assert c9["actual_R824_relation"]==self.r809.tag["actual_R824_relation"]
        assert c9["original_b_model"]==cbasis["original_b_model"]
        assert cbasis["normal_basis_rank"]==FREE and cbasis["normal_basis_degrees"]==EPS
        assert cbasis["S5_dimension"]==S5 and cbasis["qY_count"]==69
        assert cbasis["full_real_coordinates"]==1380
        assert cbasis["all_requested_targets_verified_in_all1380_rows"] is True
        assert cbasis["coefficient_field_basis"]==FIELD
        assert c9["actual_sigma_integer_n"]==cbasis["actual_sigma_integer_n"]
        assert self.r809.tag["actual_sigma_integer_n"]==self.r809_basis.tag["actual_sigma_integer_n"]
        assert self.r815.identity["result"]=="R815-original-normal-derivation-operators"
        assert self.r820.identity["result"]=="R820-original-cusp-finite-algebra-and-ideals"
        assert c9["actual_A_B_normal_vectors_computed"] is True
        assert set(TARGETS)<=set(c9["completed_target_groups"])
        assert c9["normal_basis_rank"]==FREE and c9["normal_basis_degrees"]==EPS
        assert c9["S5_dimension"]==S5 and c9["full_real_coordinates"]==1380
        assert c9["original_scalar_and_field_normalizations_preserved"] is True
        assert c9["coefficient_field_basis"]==FIELD
        assert c15["completed_scope"]=="original_normal_derivation_operators"
        assert c15["requested_targets"]==["g","Gamma"]
        assert c15["normal_affine_basis_rank"]==FREE and c15["normal_basis_degrees"]==EPS
        assert c15["coefficient_field_basis"]=="Q in the unchanged original K-normal basis"
        for key in ("original_Mg_computed","original_normal_derivation_connection_computed",
                    "all_complete_polynomial_defining_identities_verified",
                    "all_original_scalar_and_field_normalizations_preserved","normal_integral_basis_preserved"):
            assert c15[key] is True
        assert c15["Gamma_exact_nested_commutator_points"]==list(range(7))
        assert c15["Mg_exact_commutator_points"]==list(range(7))
        assert c20["completed_scope"]=="two_original_cusp_finite_algebra_kernels"
        assert c20["normal_basis_rank"]==FREE and c20["normal_basis_degrees"]==EPS
        assert c20["actual_cusp_colengths"]=={"tau":20,"sigma":20}
        assert c20["original_two_chart_cusp_ideals_computed"] is True
        assert c20["complete_polynomial_kernels_certified"] is True
        assert c20["same_original_cusp_field_and_two_chart_transitions_verified"] is True
        free=self.r809_basis.tag["original_graded_free_basis"]
        assert self.r815.tag["original_R805_free_basis"]==free
        assert self.r820.tag["original_R805_free_basis"]==free
        same_producer(self.r809_basis.tag["basis_producers"]["R805"],
                      self.r820.tag["producer_identities"]["R805"])
        same_producer(self.r815.tag["R806_producer"],
                      self.r820.tag["producer_identities"]["R806"])
        assert c15["actual_sigma_integer_n"]==self.r809.tag["actual_sigma_integer_n"]==1
        assert self.r820.tag["actual_pencil_n"]==1
        self.s5_spec=c9["S5_basis_index"]
        assert self.s5_spec==cbasis["S5_basis_index"]==self.r809.tag["original_S5_basis_index"]
        assert self.s5_spec["sha256"]==S5_INDEX_SHA
        self.s5=self.r809_basis.indexed(self.s5_spec)
        assert self.s5["dimension"]==S5 and self.s5["normal_affine_basis_rank"]==FREE
        assert self.s5["normal_basis_degrees"]==EPS
        assert self.s5["original_graded_free_basis"]==free
        assert self.s5["integer_scale"]==str(82**10)
        assert self.s5["all_original_term_phases_and_scales_verified"] is True
        self.mapping=[(a,power) for a in range(FREE) for power in range(6-EPS[a])]
        assert len(self.mapping)==len(self.s5["basis_rows"])==S5
        for i,((a,power),entry) in enumerate(zip(self.mapping,self.s5["basis_rows"])):
            assert entry["index"]==i
            assert (entry["normal_basis_index"],entry["z_degree"],entry["normal_basis_degree"])==(a,power,EPS[a])
        self.targets,self.target_specs={},{}
        for target in TARGETS:
            entry=c9["normal_vectors"][target]
            value=self.r809.indexed(entry)
            assert value["target"]==target and value["normal_basis_rank"]==FREE
            assert value["normal_basis_degrees"]==EPS and value["regular_degree_bound"]==5
            assert value["coefficient_field_basis"]==FIELD and value["S5_basis_index"]==self.s5_spec
            assert value["original_b_model"]==c9["original_b_model"]
            assert value["target_configuration"]==c9["completed_target_configurations"][target]
            assert value["target_configuration_sha256"]==fingerprint(value["target_configuration"])
            assert value["target_configuration"]["basis_configuration_sha256"]==fingerprint(self.r809.tag)
            for key in ("all14_original_field_columns_retained","normal_vector_actually_nonzero",
                        "all1380_original_coordinates_verified","weighted_polynomial_support_verified",
                        "original_field_and_scalar_normalizations_preserved"):
                assert value[key] is True
            self.targets[target],self.target_specs[target]=value,entry
        self.operators,self.operator_specs={},c15["operator_indices"]
        assert set(self.operator_specs)=={"g","Gamma"}
        for target,bound,kind in (("g",3,"multiplication"),("Gamma",2,"normal_derivation_connection")):
            value=self.r815.indexed(self.operator_specs[target])
            assert value["target"]==target and value["field_component"]==0
            assert value["operator_kind"]==kind and value["regular_degree_bound"]==bound
            assert value["coefficient_field_basis"]==c15["coefficient_field_basis"]
            assert value["target_configuration"]==c15["target_configurations"][target]
            assert value["target_configuration_sha256"]==fingerprint(value["target_configuration"])
            assert len(value["matrix_row_blocks_tau"])==len(value["matrix_row_blocks_sigma"])==17
            self.operators[target]=value
        sigma=c15["sigma_base_variable_derivative"]
        assert sigma["matrix_blocks"]==self.operators["g"]["matrix_row_blocks_sigma"]
        assert sigma["rational_scalar"]==[-1,1]
        assert sigma["identity"]=="M_(delta_sigma t)=-t^3*D*Mg(1/t)*D^-1"
        self.cusp_specs=c20["two_chart_cusp_ideal_indexes"]
        self.cusps={}
        for chart in CHARTS:
            value=self.r820.indexed(self.cusp_specs[chart])
            assert value["chart"]==chart and value["normal_basis_rank"]==FREE
            assert value["normal_basis_degrees"]==EPS
            assert value["actual_diagonal_degrees"]==[0]*271+[20]
            assert value["actual_quotient_dimension_over_Q"]==20
            assert value["complete_polynomial_kernel_certified_by_inclusion_and_equal_colength"] is True
            assert len(value["Hermite_columns_in_original_basis_order"])==FREE
            self.cusps[chart]=value
        self.tag={
            "result":RESULT,"source_sha256":sha(__file__),"python_flint":flint.__version__,"p":41,
            "R825_proof_sha256":PROOF_SHA,"R825_adapter_method_sha256":sha(args.method),
            "framework_sha256":FRAMEWORK_SHA,"derivative_framework_sha256":DERIVATIVE_SHA,
            "actual_normal_input_result":NORMAL_RESULT,
            "actual_R824_source":c9["actual_R824_source"],
            "actual_R824_relation":c9["actual_R824_relation"],
            "actual_R824_free_column":c9["original_R824_free_column"],
            "original_S5_configuration_sha256":fingerprint(self.r809_basis.tag),
            "normal_configuration_sha256":fingerprint(self.r809.tag),
            "external_S5_configuration_preserved":True,
            "producers":{label:producer_identity(p.identity) for label,p in self.inputs.items()},
            "original_R805_free_basis":free,"actual_sigma_integer_n":1,
            "normal_basis_rank":FREE,"normal_basis_degrees":EPS,
            "coefficient_field_basis":FIELD,"original_b_model":c9["original_b_model"],
            "original_R809_S5_index":self.s5_spec,"original_target_normal_vectors":self.target_specs,
            "original_R815_operator_indexes":self.operator_specs,
            "original_R820_cusp_ideal_indexes":self.cusp_specs,
            "requested_targets":list(TARGETS),"original_input_degree":5,
            "derivative_weighted_bound":7,"regular_g_product_weighted_bound":8,
            "original_D0_multiplier":["1","82"],"sigma_base_derivative_scalar":[-1,1],
            "field_component_order":[{"target":target,"field_component":component}
                                     for target in TARGETS for component in range(14)],
            "matrix_row_block_size":16,
            "completed_old_arithmetic_recomputed":False}
        self.ranges=[(first,min(first+16,FREE)) for first in range(0,FREE,16)]
        self.vector_cache={}
        self.cusp_cache={}
        self.derivative_read_cache={}

        self.put("R825-R824-normal-source-audit",{
            "normal_producer":producer_identity(self.r809.identity),
            "original_S5_producer":producer_identity(self.r809_basis.identity),
            "actual_R824_source":c9["actual_R824_source"],
            "actual_R824_relation":c9["actual_R824_relation"],
            "actual_R824_free_column":c9["original_R824_free_column"],
            "normal_vectors":self.target_specs,
            "original_S5_basis_index":self.s5_spec,
            "normal_configuration_sha256":fingerprint(self.r809.tag),
            "original_S5_configuration_sha256":fingerprint(self.r809_basis.tag),
            "original_relation_denominator_or_content_reinserted":False,
            "synthetic_R787_or_C_only_R809_A_B_output_created":False})

    def receipt(self,final):
        save(self.out/"core-receipt.json",{
            "result":RESULT,"complete":True,"source_sha256":sha(__file__),
            "certificate_sha256":sha(final),"completed_scope":SCOPE,
            "original_a_b_normal_derivatives_computed":True,
            "complete_two_chart_transports_verified":True,
            "original_cusp_coordinate_changes_verified":True,
            "P_Q_operator_matrices_computed":False,
            "general_polar_ideal_or_D_computed":False,
            "original_eta_principal_functions_rigidification_or_heights_computed":False})

    def run(self):
        final=self.out/FINAL
        manifest_name="R825-R824-exact-derivative-stages-manifest"
        if final.exists():
            certificate=read(final)
            assert certificate["complete"] is True and certificate["result"]==RESULT
            assert certificate["configuration"]==self.tag and certificate["completed_scope"]==SCOPE
            manifest=self.get(certificate["stage_manifest"])
            names=set()
            for entry in manifest["files"]:
                assert entry["file"] not in names
                names.add(entry["file"])
                assert self.get(entry)["complete"] is True
            actual={path.name for path in self.out.glob("R825-*.json.gz")
                    if path.name!=self.path(manifest_name).name}
            assert names==actual
            for key in ("original_a_b_normal_derivatives_computed",
                        "all_complete_two_chart_transports_verified",
                        "all_original_cusp_coordinate_changes_verified"):
                assert certificate[key] is True
            self.receipt(final)
            return 0
        for target in TARGETS:
            for component in range(14):self.input_component(target,component)
        blocks={chart:[] for chart in CHARTS}
        transitions=[]
        for index in range(17):
            for chart in CHARTS:blocks[chart].append(self.derivative_block(chart,index))
            transitions.append(self.transition(index,blocks["tau"][-1],blocks["sigma"][-1]))
        cusp_components={target:{chart:[] for chart in CHARTS} for target in TARGETS}
        for chart in CHARTS:
            self.cusp_basis(chart)
            for target in TARGETS:
                for component in range(14):
                    cusp_components[target][chart].append(self.cusp_component(chart,target,component,blocks[chart]))
            self.derivative_read_cache={}
        interfaces={target:self.target_interface(target,blocks,transitions,cusp_components[target])
                    for target in TARGETS}
        paths=sorted(path for path in self.out.glob("R825-*.json.gz")
                     if path.name!=self.path(manifest_name).name)
        files=[]
        for path in paths:
            self.budget()
            value=self.cached(path.name)
            assert value is not None
            files.append(spec(path))
        manifest_payload={
            "files":files,"all_listed_stages_complete":True,
            "normal_derivative_row_block_count":34,
            "exact_two_chart_transition_block_count":17,
            "original_cusp_component_coordinate_count":56,
            "old_R809_R815_R820_results_recomputed":False}
        manifest=self.put(manifest_name,manifest_payload)
        save(final,{
            "result":RESULT,"p":41,"complete":True,"configuration":self.tag,"completed_scope":SCOPE,
            "requested_targets":list(TARGETS),"normal_basis_rank":FREE,"normal_basis_degrees":EPS,
            "coefficient_field_basis":FIELD,"original_b_model":self.tag["original_b_model"],
            "actual_normal_input_result":NORMAL_RESULT,
            "actual_R824_source":self.r809.certificate["actual_R824_source"],
            "actual_R824_relation":self.r809.certificate["actual_R824_relation"],
            "actual_R824_free_column":self.r809.certificate["original_R824_free_column"],
            "original_S5_producer":producer_identity(self.r809_basis.identity),
            "original_S5_configuration_preserved":True,
            "original_relation_denominator_or_content_reinserted":False,
            "synthetic_R787_or_C_only_R809_A_B_output_created":False,
            "actual_sigma_integer_n":1,
            "original_input_weight":5,"derivative_weighted_bound":7,"regular_g_product_weighted_bound":8,
            "original_target_derivative_interfaces":interfaces,
            "two_chart_derivative_and_g_product_row_blocks":blocks,
            "complete_two_chart_transition_certificates":transitions,
            "original_cusp_coordinate_interfaces":{chart:self.cusp_basis(chart)[2] for chart in CHARTS},
            "original_cusp_coordinate_components":cusp_components,
            "original_a_b_normal_derivatives_computed":True,
            "all_complete_two_chart_transports_verified":True,
            "all_original_cusp_coordinate_changes_verified":True,
            "all_28_original_field_columns_preserved":True,
            "original_scalar_and_field_normalizations_preserved":True,
            "all_negative_power_transport_terms_cancelled_exactly":True,
            "old_R809_R815_R820_arithmetic_recomputed":False,
            "P_Q_operator_matrices_computed":False,
            "general_polar_ideal_or_D_computed":False,
            "original_eta_principal_functions_rigidification_or_heights_computed":False,
            "stage_manifest":manifest,"seconds":time.monotonic()-self.started})
        self.receipt(final)
        return 0

def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("config","proof","method","retained","output"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args()
    assert args.budget_minutes>0
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json",{
            "result":RESULT,"complete":False,"source_sha256":sha(__file__),
            "completed_scope":SCOPE,"error":type(error).__name__+": "+str(error),
            "completed_source_bound_blocks_preserved":True,
            "P_Q_operator_matrices_computed":False,
            "general_polar_ideal_or_D_computed":False,
            "original_eta_principal_functions_rigidification_or_heights_computed":False})
        if isinstance(error,BudgetStop):
            print(str(error),flush=True)
            return 124
        raise


if __name__=="__main__":
    raise SystemExit(main())
