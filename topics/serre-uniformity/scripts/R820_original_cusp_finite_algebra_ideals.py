#!/usr/bin/env python3
"""R820: exact original two-chart cusp kernels from saved S3 constant terms."""
import argparse
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_poly, fmpq_mat
import R811_original_regular_multipliers as framework
from R811_original_regular_multipliers import (
    Retained, BudgetStop, sha, read, save, spec, plain, fingerprint, producer_identity, same_producer
)

RESULT="R820-original-cusp-finite-algebra-and-ideals"
FINAL="p41-original-cusp-finite-algebra-ideals-certificate.json"
SCOPE="two_original_cusp_finite_algebra_kernels"
EPS=[0]+[1]*144+[2]*127
FRAMEWORK_SHA="849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"


def guard():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("All new mathematical arithmetic belongs to public repository Actions.")


def qp(value):
    value=fmpq(value)
    return [str(value.numer()),str(value.denom())]


def qv(value):
    assert len(value)==2 and int(value[1])>0
    answer=fmpq(int(value[0]),int(value[1]))
    assert qp(answer)==value
    return answer


def encode(values):
    return [qp(value) for value in values]


def decode(values):
    return [qv(value) for value in values]


def field_vector(value):
    assert value.degree()<20
    return [value[i] for i in range(20)]


def row_index(a):
    return 0 if a==0 else 4+3*(a-1) if a<=144 else 436+2*(a-145)


def apply_matrix(matrix,vector):
    return [sum((matrix[i][j]*vector[j] for j in range(20)),fmpq(0)) for i in range(20)]


class Job:
    def __init__(self,args):
        self.args,self.out,self.started=args,args.output,time.monotonic()
        self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["requested_stage"]==SCOPE
        assert self.item["core_sha256"]==sha(__file__)
        assert self.item["R820_proof_sha256"]==sha(args.proof)
        assert self.item["R820_method_sha256"]==sha(args.method)
        assert self.item["framework_sha256"]==sha(framework.__file__)==FRAMEWORK_SHA
        assert flint.__version__=="0.9.0"
        assert set(self.item["retained_artifacts"])=={"R805","R806"}
        self.r805=Retained(args.retained,"R805",self.item["retained_artifacts"]["R805"])
        self.r806=Retained(args.retained,"R806",self.item["retained_artifacts"]["R806"])
        c5,c6=self.r805.certificate,self.r806.certificate
        assert self.r805.identity["core_sha256"]=="730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420"
        assert self.r806.identity["core_sha256"]=="b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d"
        same_producer(self.r806.tag["retained_artifacts"]["R805"],self.r805.identity)
        assert c5["affine_free_module_rank"]==272 and c5["graded_free_basis_degrees"]==[1,144,127]
        assert c5["actual_pencil_n"]==1 and c5["actual_pencil_rank"]==690
        assert c5["degree3_S_basis_dimension"]==690 and c5["degree3_S_prefix_count"]==41
        assert c5["all_S_rows_original_and_real_coordinates_verified"] is True
        assert c5["original_82_scales_preserved"] is True
        for key in ("exact_polynomial_multiplication_computed","all272_columns_verified_in_all820_original_rows",
                    "actual_cyclic_minor_certified","original_function_field_primitive_generator_certified",
                    "normal_integral_basis_preserved"):
            assert c6[key] is True
        assert c6["actual_cyclic_minor"]["rank"]==272
        assert c6["actual_cyclic_minor"]["determinant_mod_prime"]!=0
        self.free_spec=c5["graded_free_basis_stage"]
        self.free=self.r805.indexed(self.free_spec)
        assert self.free["affine_free_module_rank"]==272 and self.free["degree_distribution"]==[1,144,127]
        assert self.free["degree1_original_indices"]==list(range(2,146))
        assert len(self.free["degree2_original_indices"])==127
        assert self.free["characteristic_zero_complement_certified"] is True
        self.index_spec=c5["S_basis_index"]
        self.index=self.r805.indexed(self.index_spec)
        assert self.index["dimension"]==690 and self.index["integer_scale"]==str(82**6)
        assert self.index["graded_free_basis_stage"]==self.free_spec
        assert self.index["qY_count"]==41 and self.index["all_original_and_real_coordinates_verified"] is True
        assert self.index["all_new_S_rows_have_original_generation_witnesses"] is True
        assert len(self.index["basis_rows"])==690
        self.pencil_spec=c5["pencil_stage"]
        self.r805.indexed(self.pencil_spec)
        self.w_spec=c6["polynomial_multiplier"]
        self.w=self.r806.indexed(self.w_spec)
        assert self.w["original_R805_free_basis"]==self.free_spec
        assert self.w["original_R805_S_basis_index"]==self.index_spec
        assert self.w["coefficient_field"]=="Q, certified by exact original rational coordinate equations"
        assert self.w["normal_affine_basis_rank"]==272 and self.w["normal_affine_basis_degrees"]==EPS
        assert self.w["original_function_field_primitive_generator_certified"] is True
        assert self.w["all272_columns_verified_in_all820_original_rows"] is True
        self.tag={
            "result":RESULT,"source_sha256":sha(__file__),"python_flint":flint.__version__,"p":41,
            "R820_proof_sha256":sha(args.proof),"R820_method_sha256":sha(args.method),
            "framework_sha256":sha(framework.__file__),
            "producer_identities":{"R805":producer_identity(self.r805.identity),"R806":producer_identity(self.r806.identity)},
            "original_R805_free_basis":self.free_spec,"original_R805_S3_index":self.index_spec,
            "original_R805_pencil":self.pencil_spec,"original_R806_Q_primitive_multiplier":self.w_spec,
            "normal_basis_degrees":EPS,"normal_basis_rank":272,"actual_pencil_n":1,
            "finite_field_degree":20,"fixed_charts":["tau","sigma"],
            "normal_basis_processing_order":"271,270,...,0",
            "kernel_algorithm":"first dependence in each reverse-ordered original Z-Krylov chain",
            "old_Fourier_or_primitive_arithmetic_recomputed":False,
            "transport_carrier_and_budget_excluded_from_mathematical_identity":True,
        }

    def budget(self):
        if time.monotonic()-self.started>=60*self.args.budget_minutes-20:
            raise BudgetStop("Completed finite-algebra stages and each exact chain step retained.")

    def path(self,name):
        assert Path(name).name==name and name.startswith("R820-")
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cached(self,name,current=False):
        path=self.path(name)
        if not path.exists():
            return None
        data=read(path)
        assert data["configuration"]==self.tag and data["complete"] is (not current)
        return data

    def put(self,name,data,current=False):
        path=self.path(name)
        assert current or not path.exists()
        save(path,dict(data,configuration=self.tag,complete=not current))
        return spec(path)

    def referenced(self,entry,current=False):
        assert spec(self.path(entry["file"]))==entry
        return self.cached(entry["file"],current)

    def source_constants(self):
        name="R820-original-selected-cusp-q0"
        old=self.cached(name)
        if old is not None:
            assert len(old["normal_basis_rows"])==272 and len(old["selected_original_S3_files"])==273
            return old,spec(self.path(name))
        selected={}
        for i in sorted({row_index(a) for a in range(272)}|{1}):
            self.budget()
            entry=self.index["basis_rows"][i]
            assert entry["index"]==i
            row=self.r805.indexed(entry)
            assert row["index"]==i and row["weight"]==6 and row["integer_scale"]==str(82**6)
            assert row["qY_count"]==41 and row["free_basis_stage"]==self.free_spec
            assert row["recipe"]==entry["recipe"]
            assert row["all_original_and_real_coordinates_verified"] is True
            assert row["V3_membership_has_original_product_generation_witness"] is True
            assert len(row["integer_v_t_coefficients"][0])==20
            selected[i]={"source":plain(entry),"recipe":row["recipe"],
                         "constant_integer_real_coordinates":row["integer_v_t_coefficients"][0]}
        normal=[]
        for a in range(272):
            row=selected[row_index(a)]
            if a==0:
                expected={"kind":"degree0_free_generator","tau_power":3,"sigma_power":0}
            elif a<=144:
                expected={"kind":"degree1_free_generator","original_M2_index":a+1,"tau_power":2,"sigma_power":0}
            else:
                expected={"kind":"degree2_free_generator",
                          "original_V2_index":self.free["degree2_original_indices"][a-145],
                          "tau_power":1,"sigma_power":0}
            assert row["recipe"]==expected
            normal.append(dict(row,normal_basis_index=a,S3_row_index=row_index(a),epsilon=EPS[a]))
        assert selected[1]["recipe"]=={"kind":"degree0_free_generator","tau_power":2,"sigma_power":1}
        self.put(name,{
            "original_S3_index":self.index_spec,"original_free_basis":self.free_spec,
            "normal_basis_rows":normal,"z_numerator_row":selected[1],
            "selected_original_S3_files":[selected[i]["source"] for i in sorted(selected)],
            "integer_scale":str(82**6),"common_denominator_section":"original tau^3",
            "old_real_coordinates_reconverted":False,"old_Fourier_coefficients_recomputed":False,
        })
        return self.cached(name),spec(self.path(name))

    def finite_algebra(self):
        source,source_spec=self.source_constants()
        name="R820-original-cusp-finite-field-interface"
        old=self.cached(name)
        if old is not None:
            assert old["source_original_constants"]==source_spec
            return old,spec(self.path(name))
        X=fmpq_poly([0,1])
        C=[fmpq_poly([2]),X]
        for _ in range(2,21):
            C.append(X*C[-1]-C[-2])
        P=fmpq_poly([1])
        for value in C[1:]:
            P+=value
        assert P.degree()==20 and P[20]==1
        basis=[fmpq_poly([0]*i+[1]) for i in range(20)]
        values=[fmpq_poly([int(x) for x in row["constant_integer_real_coordinates"]])
                for row in source["normal_basis_rows"]]
        N0=values[0]
        Nz=fmpq_poly([int(x) for x in source["z_numerator_row"]["constant_integer_real_coordinates"]])
        assert N0 and Nz and N0.degree()<20 and Nz.degree()<20

        def multiplication(value):
            columns=[field_vector((value*power)%P) for power in basis]
            return [[columns[j][i] for j in range(20)] for i in range(20)]

        def inverse(value):
            self.budget()
            matrix=fmpq_mat(multiplication(value))
            column=matrix.solve(fmpq_mat([[int(i==0)] for i in range(20)]))
            answer=fmpq_poly([column[i,0] for i in range(20)])
            assert (value*answer)%P==fmpq_poly([1])
            return answer

        inverse0,inversez=inverse(N0),inverse(Nz)
        alpha=(Nz*inverse0)%P
        alpha_inverse=(N0*inversez)%P
        assert (alpha*alpha_inverse)%P==fmpq_poly([1])
        tau=[(value*inverse0)%P for value in values]
        assert tau[0]==fmpq_poly([1])
        inverse_powers=[fmpq_poly([1]),alpha_inverse,(alpha_inverse*alpha_inverse)%P]
        sigma=[(value*inverse_powers[EPS[a]])%P for a,value in enumerate(tau)]
        for a in range(272):
            assert (sigma[a]*(alpha**EPS[a]))%P==tau[a]
        matrix_tau,matrix_sigma=multiplication(alpha),multiplication(alpha_inverse)
        # These are the same finite algebra and exact original field coordinates.
        for j in range(20):
            assert apply_matrix(matrix_tau,field_vector(basis[j]))==field_vector((alpha*basis[j])%P)
            assert apply_matrix(matrix_sigma,field_vector(basis[j]))==field_vector((alpha_inverse*basis[j])%P)
        self.put(name,{
            "source_original_constants":source_spec,"finite_field_degree":20,
            "fixed_field_generator":"xi_41+xi_41^-1 in the unchanged R805 real coordinate basis",
            "field_modulus_low_to_high":encode([P[i] for i in range(21)]),
            "N0_inverse":encode(field_vector(inverse0)),"Nz_inverse":encode(field_vector(inversez)),
            "both_original_nonzero_denominators_inverted_and_fully_multiplied_back":True,
            "alpha":encode(field_vector(alpha)),"alpha_inverse":encode(field_vector(alpha_inverse)),
            "alpha_inverse_product_verified":True,
            "evaluation_vectors":{"tau":[encode(field_vector(v)) for v in tau],
                                  "sigma":[encode(field_vector(v)) for v in sigma]},
            "base_multiplication_matrices":{"tau":[encode(row) for row in matrix_tau],
                                            "sigma":[encode(row) for row in matrix_sigma]},
            "all_base_multiplication_columns_verified_in_original_field":True,
            "all_272_original_two_chart_evaluation_transitions_verified":True,
            "original_common_82_power_cancels_exactly":6,
            "all_original_frames_and_cusp_conjugates_preserved":True,
            "constant_evaluation_matrix_rank_not_assumed":True,
            "base_value_primitive_not_assumed":True,
        })
        return self.cached(name),spec(self.path(name))

    def chart(self,chart,field,field_spec):
        assert chart in ("tau","sigma")
        name="R820-chart-"+chart+"-cusp-Hermite-index"
        current_name="R820-chart-"+chart+"-current"
        old=self.cached(name)
        if old is not None:
            self.validate_chart(chart,spec(self.path(name)),field_spec)
            self.path(current_name).unlink(missing_ok=True)
            return spec(self.path(name))
        evaluations=[decode(row) for row in field["evaluation_vectors"][chart]]
        matrix=[decode(row) for row in field["base_multiplication_matrices"][chart]]
        current=self.cached(current_name,current=True)
        if current is None:
            state={"chart":chart,"source_field_interface":field_spec,"normal_basis_index":271,
                   "power":0,"current_vector":encode(evaluations[271]),"selected_steps":[],
                   "relation_steps":[],"degrees":[None]*272,"step_count":0,"last_completed_step":None}
            self.put(current_name,state,current=True)
            current=self.cached(current_name,current=True)
        assert current["chart"]==chart and current["source_field_interface"]==field_spec
        while current["normal_basis_index"]>=0:
            self.budget()
            a,k=current["normal_basis_index"],current["power"]
            assert 0<=a<272 and 0<=k<=20
            step_name="R820-chart-"+chart+"-basis-"+str(a).zfill(3)+"-power-"+str(k).zfill(2)+"-step"
            step=self.cached(step_name)
            current_spec=spec(self.path(current_name))
            if step is None:
                basis=[self.referenced(entry) for entry in current["selected_steps"]]
                rank=len(basis)
                assert rank<=20
                candidate=decode(current["current_vector"])
                residual=list(candidate)
                coefficients=[fmpq(0)]*rank
                originals=[decode(data["original_candidate_vector"]) for data in basis]
                pivots=[]
                for j,data in enumerate(basis):
                    assert data["kind"]=="independent" and data["chart"]==chart
                    assert data["selected_position"]==j
                    pivot=data["pivot_row"]
                    assert pivot not in pivots
                    pivots.append(pivot)
                    echelon=decode(data["normalized_echelon_vector"])
                    transform=decode(data["echelon_in_selected_original_vectors"])
                    assert len(transform)==j+1 and echelon[pivot]==1
                    factor=residual[pivot]
                    residual=[residual[i]-factor*echelon[i] for i in range(20)]
                    for b,value in enumerate(transform):
                        coefficients[b]+=factor*value
                assert all(residual[pivot]==0 for pivot in pivots)
                for row in range(20):
                    assert candidate[row]==residual[row]+sum(
                        (coefficients[j]*originals[j][row] for j in range(rank)),fmpq(0))
                binding={
                    "chart":chart,"normal_basis_index":a,"power":k,
                    "source_field_interface":field_spec,"before_current_state":current_spec,
                    "previous_completed_step":current["last_completed_step"],
                    "step_number":current["step_count"],
                    "previous_selected_steps":current["selected_steps"],
                    "original_candidate_vector":encode(candidate),
                    "full_20_coordinate_echelon_multiply_back_verified":True,
                }
                if any(residual):
                    assert rank<20
                    pivot=next(i for i,value in enumerate(residual) if value)
                    assert pivot not in pivots
                    value=residual[pivot]
                    normalized=[x/value for x in residual]
                    transform=[-x/value for x in coefficients]+[fmpq(1)/value]
                    original_extended=originals+[candidate]
                    for row in range(20):
                        assert normalized[row]==sum(
                            (transform[j]*original_extended[j][row] for j in range(rank+1)),fmpq(0))
                    next_vector=apply_matrix(matrix,candidate)
                    self.put(step_name,dict(binding,kind="independent",
                        selected_position=rank,pivot_row=pivot,pivot_value=qp(value),
                        normalized_echelon_vector=encode(normalized),
                        echelon_in_selected_original_vectors=encode(transform),
                        next_candidate_vector=encode(next_vector),
                        actual_independence_certified_by_new_nonzero_pivot=True,
                        next_candidate_is_original_base_value_times_original_candidate=True))
                else:
                    terms=[{"normal_basis_row":a,"power":k,"coefficient":["1","1"]}]
                    for coefficient,data in zip(coefficients,basis):
                        if not coefficient:
                            continue
                        b,power=data["normal_basis_index"],data["power"]
                        assert b>=a
                        assert power<(k if b==a else current["degrees"][b])
                        terms.append({"normal_basis_row":b,"power":power,"coefficient":qp(-coefficient)})
                    terms.sort(key=lambda row:(row["normal_basis_row"],row["power"]))
                    assert len({(row["normal_basis_row"],row["power"]) for row in terms})==len(terms)
                    self.put(step_name,dict(binding,kind="first_dependence",
                        first_dependent_power=k,relation_coefficients_in_selected_vectors=encode(coefficients),
                        complete_relation_evaluation_zero_in_all_20_original_coordinates=True,
                        column_terms=terms,monic_diagonal_degree=k,
                        upper_entries_zero_and_lower_remainders_strict=True,
                        exact_original_normal_basis_column=a))
                step=self.cached(step_name)
            assert step["before_current_state"]==current_spec
            assert step["previous_completed_step"]==current["last_completed_step"]
            assert step["source_field_interface"]==field_spec and step["chart"]==chart
            assert step["normal_basis_index"]==a and step["power"]==k
            assert step["previous_selected_steps"]==current["selected_steps"]
            entry=spec(self.path(step_name))
            next_state=dict(current)
            if step["kind"]=="independent":
                assert step["selected_position"]==len(current["selected_steps"])
                next_state["selected_steps"]=current["selected_steps"]+[entry]
                next_state["power"]=k+1
                next_state["current_vector"]=step["next_candidate_vector"]
            else:
                assert step["kind"]=="first_dependence" and step["first_dependent_power"]==k
                next_state["relation_steps"]=current["relation_steps"]+[entry]
                degrees=list(current["degrees"])
                assert degrees[a] is None
                degrees[a]=k
                next_state["degrees"]=degrees
                next_state["normal_basis_index"]=a-1
                next_state["power"]=0
                next_state["current_vector"]=encode(evaluations[a-1]) if a else None
            next_state["step_count"]=current["step_count"]+1
            next_state["last_completed_step"]=entry
            self.put(current_name,next_state,current=True)
            current=self.cached(current_name,current=True)
        assert len(current["selected_steps"])==20 and len(current["relation_steps"])==272
        assert current["step_count"]==292 and sum(current["degrees"])==20
        selected=[self.referenced(entry) for entry in current["selected_steps"]]
        pivots=[data["pivot_row"] for data in selected]
        assert sorted(pivots)==list(range(20))
        originals=[decode(data["original_candidate_vector"]) for data in selected]
        minor_name="R820-chart-"+chart+"-actual-reachable-minor"
        minor=self.cached(minor_name)
        if minor is None:
            self.budget()
            determinant=fmpq_mat([[originals[j][i] for j in range(20)] for i in range(20)]).det()
            assert determinant
            self.put(minor_name,{
                "chart":chart,"source_field_interface":field_spec,
                "selected_original_chain_vectors":current["selected_steps"],
                "actual_pivot_rows":pivots,"actual_rank":20,"exact_minor_shape":[20,20],
                "actual_nonzero_rational_determinant":qp(determinant),
                "minor_computed_over_Q_in_original_real_cyclotomic_coordinates":True,
                "constant_evaluation_matrix_rank_or_base_primitivity_assumed":False})
            minor=self.cached(minor_name)
        assert minor["selected_original_chain_vectors"]==current["selected_steps"]
        assert minor["actual_rank"]==20 and qv(minor["actual_nonzero_rational_determinant"])
        columns=list(reversed(current["relation_steps"]))
        nonmonic=0
        for a,entry in enumerate(columns):
            relation=self.referenced(entry)
            assert relation["normal_basis_index"]==a
            assert relation["first_dependent_power"]==current["degrees"][a]
            assert relation["complete_relation_evaluation_zero_in_all_20_original_coordinates"] is True
            diagonal=0
            for term in relation["column_terms"]:
                b,k=term["normal_basis_row"],term["power"]
                assert b>=a and qv(term["coefficient"])
                if b==a and k==current["degrees"][a]:
                    assert term["coefficient"]==["1","1"]
                    diagonal+=1
                else:
                    assert k<current["degrees"][b]
                    nonmonic+=1
            assert diagonal==1
        position_bound=sum((a+1)*degree for a,degree in enumerate(current["degrees"]))
        assert nonmonic<=position_bound<=5440
        self.put(name,{
            "chart":chart,"source_field_interface":field_spec,
            "normal_basis_rank":272,"normal_basis_degrees":EPS,
            "original_basis_processing_order":"271,270,...,0",
            "selected_original_chain_vectors":current["selected_steps"],
            "actual_reachable_minor":spec(self.path(minor_name)),
            "actual_reachable_rank":20,"actual_diagonal_degrees":current["degrees"],
            "actual_total_diagonal_degree":20,"actual_step_count":current["step_count"],
            "Hermite_columns_in_original_basis_order":columns,
            "coefficient_convention":"sparse column_terms: output normal_basis_row, base-variable power, [numerator,denominator]",
            "actual_nonmonic_nonzero_coefficient_count":nonmonic,
            "actual_nonmonic_coefficient_position_bound":position_bound,
            "universal_nonmonic_coefficient_position_bound":5440,
            "all_272_original_relations_verified_in_full_finite_algebra":True,
            "canonical_lower_triangular_monic_and_reduced_conditions_verified":True,
            "complete_polynomial_kernel_certified_by_inclusion_and_equal_colength":True,
            "actual_quotient_dimension_over_Q":20,"quotient_is_original_separable_cusp_field":True,
            "reduced_cusp_multiplicity_one_at_all_20_geometric_cusps":True,
            "no_geometric_closed_point_splitting_required":True,
            "latest_completed_step":current["last_completed_step"],
            "general_polar_ideal_eta_or_height_computed":False})
        self.path(current_name).unlink()
        print(json.dumps({"stage":"complete_original_cusp_ideal","chart":chart,"actual_rank":20,
                          "actual_nonmonic_coefficients":nonmonic,
                          "seconds":time.monotonic()-self.started}),flush=True)
        return spec(self.path(name))

    def validate_chart(self,chart,entry,field_spec):
        data=self.referenced(entry)
        assert data["chart"]==chart and data["source_field_interface"]==field_spec
        assert data["normal_basis_rank"]==272 and data["normal_basis_degrees"]==EPS
        assert data["actual_reachable_rank"]==20 and data["actual_total_diagonal_degree"]==20
        assert len(data["actual_diagonal_degrees"])==272 and sum(data["actual_diagonal_degrees"])==20
        assert data["actual_step_count"]==292
        assert data["complete_polynomial_kernel_certified_by_inclusion_and_equal_colength"] is True
        minor=self.referenced(data["actual_reachable_minor"])
        assert minor["actual_rank"]==20 and qv(minor["actual_nonzero_rational_determinant"])
        assert minor["selected_original_chain_vectors"]==data["selected_original_chain_vectors"]
        assert len(data["selected_original_chain_vectors"])==20
        for i,step in enumerate(data["selected_original_chain_vectors"]):
            value=self.referenced(step)
            assert value["kind"]=="independent" and value["selected_position"]==i
            assert value["chart"]==chart and value["source_field_interface"]==field_spec
            assert value["actual_independence_certified_by_new_nonzero_pivot"] is True
        columns=data["Hermite_columns_in_original_basis_order"]
        assert len(columns)==272
        for a,column in enumerate(columns):
            value=self.referenced(column)
            assert value["kind"]=="first_dependence" and value["normal_basis_index"]==a
            assert value["first_dependent_power"]==data["actual_diagonal_degrees"][a]
            assert value["chart"]==chart and value["source_field_interface"]==field_spec
            assert value["complete_relation_evaluation_zero_in_all_20_original_coordinates"] is True
        return data

    def run(self):
        field,field_spec=self.finite_algebra()
        indexes={chart:self.chart(chart,field,field_spec) for chart in ("tau","sigma")}
        for chart,entry in indexes.items():
            self.validate_chart(chart,entry,field_spec)
        assert not list(self.out.glob("R820-*-current.json.gz"))
        files=[spec(path) for path in sorted(self.out.glob("R820-*.json.gz"))
               if not path.name.startswith("R820-stage-manifest-")]
        manifest_name="R820-stage-manifest-"+fingerprint(files)[:24]
        prior=self.cached(manifest_name)
        if prior is None:
            inventory=self.put(manifest_name,{"files":files})
        else:
            assert prior["files"]==files
            inventory=spec(self.path(manifest_name))
        final=self.out/FINAL
        save(final,{
            "result":RESULT,"complete":True,"configuration":self.tag,"p":41,"completed_scope":SCOPE,
            "normal_basis_rank":272,"normal_basis_degrees":EPS,"finite_field_degree":20,
            "selected_original_S3_row_count":273,"original_source_constants":field["source_original_constants"],
            "original_finite_algebra_interface":field_spec,"two_chart_cusp_ideal_indexes":indexes,
            "actual_cusp_colengths":{"tau":20,"sigma":20},
            "actual_input_producers":self.tag["producer_identities"],
            "original_two_chart_cusp_ideals_computed":True,
            "complete_polynomial_kernels_certified":True,
            "same_original_cusp_field_and_two_chart_transitions_verified":True,
            "old_Fourier_or_primitive_results_recomputed":False,
            "original_Gamma_or_general_polar_ideal_computed":False,
            "actual_eta_principal_function_or_height_computed":False,
            "stage_manifest":inventory,"seconds":time.monotonic()-self.started})
        save(self.out/"core-receipt.json",{
            "result":RESULT,"complete":True,"source_sha256":sha(__file__),"certificate_sha256":sha(final),
            "completed_scope":SCOPE,"original_two_chart_cusp_ideals_computed":True,
            "complete_polynomial_kernels_certified":True,
            "original_Gamma_or_general_polar_ideal_computed":False,
            "actual_eta_principal_function_or_height_computed":False})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("config","proof","method","retained","output"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--budget-minutes",type=float,default=60)
    args=parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json",{
            "result":RESULT,"complete":False,"source_sha256":sha(__file__),
            "error":type(error).__name__+": "+str(error),
            "completed_finite_algebra_and_each_exact_chain_step_preserved":True,
            "original_Gamma_or_general_polar_ideal_computed":False,
            "actual_eta_principal_function_or_height_computed":False})
        raise


if __name__=="__main__":
    sys.exit(main())
