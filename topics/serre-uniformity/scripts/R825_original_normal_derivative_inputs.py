#!/usr/bin/env python3
"""R825: original a,b normal derivatives, both charts, and exact cusp coordinates."""
import argparse
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpz_mat
import R811_original_regular_multipliers as framework
from R811_original_regular_multipliers import (
    Retained, BudgetStop, sha, read, save, spec, plain, fingerprint, producer_identity, same_producer
)

RESULT="R825-original-normal-derivative-inputs"
FINAL="p41-original-normal-derivative-inputs-certificate.json"
SCOPE="original_a_b_normal_derivatives_in_two_charts"
FREE,S5,COMPONENTS=272,1234,28
EPS=[0]+[1]*144+[2]*127
TARGETS=("A","B")
CHARTS=("tau","sigma")
FIELD="b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
FRAMEWORK_SHA="849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
PROOF_SHA="73f9f293f0a0526a2f1eed8b62aea562b659090b546d1e122c0e12dbd1f90930"


def guard():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("All new original derivative arithmetic belongs to the public repository Actions.")


def pair(value):
    value=fmpq(value)
    return [str(value.numer()),str(value.denom())]


def rational(value):
    assert len(value)==2 and int(value[1])>0
    answer=fmpq(int(value[0]),int(value[1]))
    assert pair(answer)==value
    return answer


def trim(values):
    values=list(values)
    while values and not values[-1]:
        values.pop()
    return values


def poly_add(left,right):
    answer=[fmpq(0)]*max(len(left),len(right))
    for i,value in enumerate(left):answer[i]+=value
    for i,value in enumerate(right):answer[i]+=value
    return trim(answer)


def poly_mul(left,right):
    if not left or not right:return []
    answer=[fmpq(0)]*(len(left)+len(right)-1)
    for i,x in enumerate(left):
        for j,y in enumerate(right):
            answer[i+j]+=x*y
    return trim(answer)


def monic_divide(numerator,denominator):
    """Exact small Q-polynomial division with the original monic P20."""
    numerator,denominator=trim(numerator),trim(denominator)
    assert len(denominator)==21 and denominator[-1]==1
    remainder=list(numerator)
    quotient=[fmpq(0)]*max(0,len(remainder)-20)
    while len(remainder)>=len(denominator):
        shift=len(remainder)-len(denominator)
        factor=remainder[-1]
        quotient[shift]=factor
        for j,value in enumerate(denominator):
            remainder[shift+j]-=factor*value
        remainder=trim(remainder)
    assert poly_add(poly_mul(quotient,denominator),remainder)==numerator
    return trim(quotient),remainder


class Job:
    def __init__(self,args):
        self.args,self.out,self.started=args,args.output,time.monotonic()
        self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["requested_stage"]==SCOPE and self.item["producer_inputs_pending"] is False
        assert self.item["requested_targets"]==list(TARGETS) and self.item["matrix_row_block_size"]==16
        assert sha(__file__)==self.item["core_sha256"]
        assert sha(args.proof)==self.item["R825_proof_sha256"]==PROOF_SHA
        assert sha(args.method)==self.item["R825_adapter_method_sha256"]
        assert sha(framework.__file__)==self.item["framework_sha256"]==FRAMEWORK_SHA
        assert flint.__version__=="0.9.0"
        assert set(self.item["retained_artifacts"])=={"R809","R815","R820"}
        self.inputs={label:Retained(args.retained,label,self.item["retained_artifacts"][label])
                     for label in ("R809","R815","R820")}
        self.r809,self.r815,self.r820=(self.inputs[label] for label in ("R809","R815","R820"))
        c9,c15,c20=(p.certificate for p in (self.r809,self.r815,self.r820))
        assert self.r809.identity["result"]=="R809-original-S5-normal-coordinates"
        assert self.r815.identity["result"]=="R815-original-normal-derivation-operators"
        assert self.r820.identity["result"]=="R820-original-cusp-finite-algebra-and-ideals"
        assert c9["actual_original_y_normal_vectors_computed"] is True
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
        free=self.r809.tag["original_graded_free_basis"]
        assert self.r815.tag["original_R805_free_basis"]==free
        assert self.r820.tag["original_R805_free_basis"]==free
        same_producer(self.r809.tag["basis_producers"]["R805"],
                      self.r820.tag["producer_identities"]["R805"])
        same_producer(self.r815.tag["R806_producer"],
                      self.r820.tag["producer_identities"]["R806"])
        assert c15["actual_sigma_integer_n"]==self.r809.tag["actual_sigma_integer_n"]==1
        assert self.r820.tag["actual_pencil_n"]==1
        self.s5_spec=c9["S5_basis_index"]
        self.s5=self.r809.indexed(self.s5_spec)
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
            "framework_sha256":FRAMEWORK_SHA,
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

    def budget(self):
        if time.monotonic()-self.started>=self.args.budget_minutes*60-20:
            raise BudgetStop("Completed source-bound derivative blocks retained; no completed block is repeated.")

    def path(self,name):
        assert Path(name).name==name and name.startswith("R825-")
        return self.out/(name if name.endswith(".json.gz") else name+".json.gz")

    def cached(self,name):
        path=self.path(name)
        if not path.exists():return None
        value=read(path)
        assert value["complete"] is True and value["configuration"]==self.tag
        return value

    def put(self,name,payload):
        path=self.path(name)
        value=dict(payload,complete=True,configuration=self.tag)
        if path.exists():
            assert read(path)==value
        else:save(path,value)
        return spec(path)

    def get(self,entry):
        assert spec(self.path(entry["file"]))==entry
        return self.cached(entry["file"])


    def input_component(self,target,component):
        assert target in TARGETS and 0<=component<14
        original=self.targets[target]
        groups=original["coordinate_groups"]
        assert len(groups)==2
        source=groups[component//7]
        group=self.r809.indexed(source)
        indices=list(range((component//7)*7,(component//7+1)*7))
        assert group["target"]==target and group["column_indices"]==indices
        assert group["normal_basis_rank"]==FREE and group["basis_dimension"]==S5
        assert group["full_coordinate_rows"]==1380 and group["regular_degree_bound"]==5
        assert group["S5_basis_index"]==self.s5_spec
        assert group["coefficient_field_basis"]==FIELD
        assert group["target_configuration"]==original["target_configuration"]
        assert group["target_configuration_sha256"]==original["target_configuration_sha256"]
        assert group["all1380_original_coordinates_verified"] is True
        assert group["original_field_and_scalar_normalizations_preserved"] is True
        assert len(group["coordinate_numerators"])==S5
        assert all(len(row)==7 for row in group["coordinate_numerators"])
        assert len(group["column_denominators"])==len(group["original_target_rational_scales"])==7
        local=component%7
        group_denominator=int(group["column_denominators"][local])
        scale=group["original_target_rational_scales"][local]
        scale_num,scale_den=int(scale[0]),int(scale[1])
        assert group_denominator>0 and scale_den>0
        name="R825-input-"+target+"-component-"+str(component).zfill(2)
        binding={
            "target":target,"field_component":component,"regular_degree_bound":5,
            "normal_basis_rank":FREE,"normal_basis_degrees":EPS,
            "source_normal_vector":self.target_specs[target],
            "source_exact_coordinate_group":source,"original_S5_index":self.s5_spec,
            "source_target_configuration":original["target_configuration"],
            "original_target_rational_scale":scale,
            "original_group_column_denominator":str(group_denominator),
            "original_scalar_applied_exactly_once":True,
            "coefficient_field_basis":FIELD}
        old=self.cached(name)
        if old is None:
            self.budget()
            denominator=group_denominator*scale_den
            values=[[0]*FREE for _ in range(6)]
            for row,(output,power) in enumerate(self.mapping):
                values[power][output]=int(group["coordinate_numerators"][row][local])*scale_num
            content=denominator
            for row in values:
                for value in row:content=math.gcd(content,value)
            assert content>0
            denominator//=content
            values=[[value//content for value in row] for row in values]
            self.put(name,dict(binding,common_positive_denominator=str(denominator),
                coefficient_numerators=[[str(value) for value in row] for row in values],
                normalization_content=str(content),
                coefficient_order="power=0..5, normal_basis_row=0..271",
                actual_zero_component=not any(value for row in values for value in row),
                weighted_polynomial_support_verified=True))
            old=self.cached(name)
        for key,value in binding.items():assert old[key]==value
        denominator=int(old["common_positive_denominator"])
        values=[[int(value) for value in row] for row in old["coefficient_numerators"]]
        assert denominator>0 and len(values)==6 and all(len(row)==FREE for row in values)
        for power,row in enumerate(values):
            for output,value in enumerate(row):
                if power>5-EPS[output]:assert value==0
        assert old["weighted_polynomial_support_verified"] is True
        assert old["actual_zero_component"] is (not any(value for row in values for value in row))
        return values,denominator,spec(self.path(name))

    def input_vectors(self,chart):
        assert chart in CHARTS
        if chart in self.vector_cache:return self.vector_cache[chart]
        entries=[self.input_component(target,component) for target in TARGETS for component in range(14)]
        denominators=[entry[1] for entry in entries]
        sources=[entry[2] for entry in entries]
        matrices=[fmpz_mat(FREE,COMPONENTS) for _ in range(6)]
        for column,(values,_,_) in enumerate(entries):
            for output in range(FREE):
                bound=5-EPS[output]
                for power in range(bound+1):
                    destination=power if chart=="tau" else bound-power
                    matrices[destination][output,column]=values[power][output]
        self.vector_cache[chart]=(matrices,denominators,sources)
        return self.vector_cache[chart]

    def operator_block(self,target,chart,index):
        assert target in ("g","Gamma") and chart in CHARTS and 0<=index<17
        interface=self.operators[target]
        source=interface["matrix_row_blocks_"+chart][index]
        data=self.r815.indexed(source)
        first,stop=self.ranges[index]
        degree=3 if target=="g" else 2
        assert data["target"]==target and data["field_component"]==0
        assert data["operator_kind"]==interface["operator_kind"]
        assert data["target_configuration"]==interface["target_configuration"]
        assert data["target_configuration_sha256"]==interface["target_configuration_sha256"]
        assert (data["row_first"],data["row_stop"],data["regular_degree_bound"])==(first,stop,degree)
        if chart=="sigma":
            assert data["source_tau_matrix_row_block"]==interface["matrix_row_blocks_tau"][index]
        denominator=int(data["common_positive_denominator"])
        assert denominator>0
        matrices=[fmpz_mat(stop-first,FREE) for _ in range(degree+3)]
        raw,offset=data["coefficient_numerators"],0
        for output in range(first,stop):
            for column in range(FREE):
                bound=degree+EPS[column]-EPS[output]
                assert bound>=0
                for power in range(bound+1):
                    matrices[power][output-first,column]=int(raw[offset])
                    offset+=1
        assert offset==len(raw)
        return matrices,denominator,source

    def derivative_block(self,chart,index):
        first,stop=self.ranges[index]
        name="R825-"+chart+"-derivative-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
        source_inputs=[spec(self.path("R825-input-"+target+"-component-"+str(component).zfill(2)))
                       for target in TARGETS for component in range(14)]
        gamma_source=self.operators["Gamma"]["matrix_row_blocks_"+chart][index]
        g_source=self.operators["g"]["matrix_row_blocks_"+chart][index]
        binding={
            "chart":chart,"row_first":first,"row_stop":stop,
            "normal_basis_rank":FREE,"normal_basis_degrees":EPS,
            "field_component_order":self.tag["field_component_order"],
            "source_original_input_components":source_inputs,
            "source_Gamma_matrix_row_block":gamma_source,
            "source_regular_g_matrix_row_block":g_source,
            "source_R815_certificate_sha256":self.tag["producers"]["R815"]["certificate_sha256"],
            "sigma_input_transport":None if chart=="tau" else "v_sigma[i](t)=t^(5-eps_i)*v_tau[i](1/t)",
            "base_derivative_scalar":1 if chart=="tau" else -1,
            "derivative_weighted_bound":7,"regular_g_product_weighted_bound":8,
            "coefficient_field_basis":FIELD,
            "original_scales_applied_exactly_once":True,
            "one_original_g_matrix_product_shared_by_product_and_derivative":True}
        old=self.cached(name)
        if old is None:
            self.budget()
            vectors,input_denominators,vector_sources=self.input_vectors(chart)
            assert vector_sources==source_inputs
            gamma,gamma_denominator,actual_gamma=self.operator_block("Gamma",chart,index)
            gm,g_denominator,actual_g=self.operator_block("g",chart,index)
            assert actual_gamma==gamma_source and actual_g==g_source
            common=math.lcm(gamma_denominator,g_denominator)
            gamma_factor,g_factor=common//gamma_denominator,common//g_denominator
            width=stop-first
            derivative=[fmpz_mat(width,COMPONENTS) for _ in range(10)]
            product=[fmpz_mat(width,COMPONENTS) for _ in range(11)]
            for power,matrix in enumerate(gamma):
                for degree,vector in enumerate(vectors):
                    self.budget()
                    derivative[power+degree]+=matrix*vector*gamma_factor
            sign=binding["base_derivative_scalar"]
            for power,matrix in enumerate(gm):
                for degree,vector in enumerate(vectors):
                    self.budget()
                    actual=matrix*vector*g_factor
                    product[power+degree]+=actual
                    if degree:derivative[power+degree-1]+=actual*(sign*degree)
            for local,output in enumerate(range(first,stop)):
                for power,matrix in enumerate(derivative):
                    if power>7-EPS[output]:
                        assert all(matrix[local,column]==0 for column in range(COMPONENTS))
                for power,matrix in enumerate(product):
                    if power>8-EPS[output]:
                        assert all(matrix[local,column]==0 for column in range(COMPONENTS))
            denominators,contents=[],[]
            for column in range(COMPONENTS):
                denominator=common*input_denominators[column]
                content=denominator
                for family in (derivative,product):
                    for matrix in family:
                        for local in range(width):content=math.gcd(content,int(matrix[local,column]))
                assert content>0
                denominators.append(str(denominator//content))
                contents.append(content)
            def encoded(family,count):
                return [[[str(int(family[power][local,column])//contents[column])
                          for column in range(COMPONENTS)] for local in range(width)]
                        for power in range(count)]
            self.put(name,dict(binding,
                operator_common_positive_denominator=str(common),
                original_input_column_denominators=[str(value) for value in input_denominators],
                column_denominators=denominators,
                joint_column_normalization_contents=[str(value) for value in contents],
                derivative_coefficient_numerators=encoded(derivative,8),
                regular_g_product_coefficient_numerators=encoded(product,9),
                coefficient_order="power, output row minus row_first, original target/field column",
                full_weighted_support_verified=True,
                all_original_Q_rational_coefficients_computed=True))
            print(json.dumps({"stage":"original_normal_derivative_block","chart":chart,
                "row_first":first,"row_stop":stop,"seconds":time.monotonic()-self.started}),flush=True)
            old=self.cached(name)
        for key,value in binding.items():assert old[key]==value
        denominators=[int(value) for value in old["column_denominators"]]
        assert len(denominators)==COMPONENTS and all(value>0 for value in denominators)
        assert old["full_weighted_support_verified"] is True
        assert old["all_original_Q_rational_coefficients_computed"] is True
        for key,length,bound in (("derivative_coefficient_numerators",8,7),
                                 ("regular_g_product_coefficient_numerators",9,8)):
            coefficients=old[key]
            assert len(coefficients)==length
            assert all(len(rows)==stop-first and all(len(row)==COMPONENTS for row in rows)
                       for rows in coefficients)
            for power,rows in enumerate(coefficients):
                for local,row in enumerate(rows):
                    if power>bound-EPS[first+local]:assert all(int(value)==0 for value in row)
        return spec(self.path(name))

    def transition(self,index,tau_spec,sigma_spec):
        first,stop=self.ranges[index]
        name="R825-two-chart-derivative-transition-rows-"+str(first).zfill(3)+"-"+str(stop).zfill(3)
        binding={"row_first":first,"row_stop":stop,
            "source_tau_derivative_row_block":tau_spec,"source_sigma_derivative_row_block":sigma_spec,
            "normal_basis_degrees":EPS,"field_component_order":self.tag["field_component_order"],
            "derivative_transport":"d_sigma=t^6*D*d_tau(1/t)-5*t^7*D*u_tau(1/t)",
            "regular_g_product_transport":"u_sigma=t^8*D*u_tau(1/t)",
            "D":"diag(t^-eps_i)","original_input_weight":5}
        old=self.cached(name)
        if old is None:
            self.budget()
            tau,sigma=self.get(tau_spec),self.get(sigma_spec)
            for local,output in enumerate(range(first,stop)):
                for column in range(COMPONENTS):
                    dt=int(tau["column_denominators"][column])
                    ds=int(sigma["column_denominators"][column])
                    laurent={}
                    for power in range(8):
                        exponent=6-EPS[output]-power
                        value=fmpq(int(tau["derivative_coefficient_numerators"][power][local][column]),dt)
                        laurent[exponent]=laurent.get(exponent,fmpq(0))+value
                    for power in range(9):
                        exponent=7-EPS[output]-power
                        value=fmpq(-5*int(tau["regular_g_product_coefficient_numerators"][power][local][column]),dt)
                        laurent[exponent]=laurent.get(exponent,fmpq(0))+value
                    for exponent,value in laurent.items():
                        if exponent<0 or exponent>=8:assert value==0
                    for power in range(8):
                        expected=fmpq(int(sigma["derivative_coefficient_numerators"][power][local][column]),ds)
                        assert laurent.get(power,fmpq(0))==expected
                    reversed_product={}
                    for power in range(9):
                        exponent=8-EPS[output]-power
                        value=fmpq(int(tau["regular_g_product_coefficient_numerators"][power][local][column]),dt)
                        reversed_product[exponent]=reversed_product.get(exponent,fmpq(0))+value
                    for exponent,value in reversed_product.items():
                        if exponent<0 or exponent>=9:assert value==0
                    for power in range(9):
                        expected=fmpq(int(sigma["regular_g_product_coefficient_numerators"][power][local][column]),ds)
                        assert reversed_product.get(power,fmpq(0))==expected
            self.put(name,dict(binding,
                all_28_original_field_columns_verified=True,
                full_rational_polynomial_identities_verified=True,
                both_separate_negative_power_terms_retained_and_cancelled=True,
                no_field_conjugation_or_new_mu3_choice=True))
            old=self.cached(name)
        for key,value in binding.items():assert old[key]==value
        assert old["full_rational_polynomial_identities_verified"] is True
        assert old["both_separate_negative_power_terms_retained_and_cancelled"] is True
        return spec(self.path(name))

    def cusp_basis(self,chart):
        if chart in self.cusp_cache:return self.cusp_cache[chart]
        interface=self.cusps[chart]
        sources=interface["Hermite_columns_in_original_basis_order"]
        name="R825-"+chart+"-original-cusp-coordinate-interface"
        binding={"chart":chart,"source_R820_cusp_index":self.cusp_specs[chart],
            "source_original_Hermite_columns":sources,
            "source_field_interface":interface["source_field_interface"],
            "normal_basis_rank":FREE,"actual_diagonal_degrees":[0]*271+[20],
            "coordinate_change_only_not_ideal_quotient":True}
        old=self.cached(name)
        qs=[]
        modulus=None
        for a,source in enumerate(sources):
            if a%16==0:self.budget()
            data=self.r820.indexed(source)
            assert data["chart"]==chart and data["normal_basis_index"]==a
            assert data["kind"]=="first_dependence"
            expected_degree=20 if a==271 else 0
            assert data["first_dependent_power"]==data["monic_diagonal_degree"]==expected_degree
            assert data["exact_original_normal_basis_column"]==a
            assert data["source_field_interface"]==interface["source_field_interface"]
            assert data["complete_relation_evaluation_zero_in_all_20_original_coordinates"] is True
            terms={}
            for term in data["column_terms"]:
                key=(term["normal_basis_row"],term["power"])
                assert key not in terms
                value=rational(term["coefficient"])
                assert value!=0 and 0<=key[0]<FREE and key[1]>=0
                terms[key]=value
            assert terms.get((a,expected_degree))==1
            if a<271:
                assert all((row==a and power==0) or (row==271 and power<20)
                           for row,power in terms)
                qs.append(trim([-terms.get((271,power),fmpq(0)) for power in range(20)]))
            else:
                assert all(row==271 and power<=20 for row,power in terms)
                modulus=trim([terms.get((271,power),fmpq(0)) for power in range(21)])
                assert len(modulus)==21 and modulus[-1]==1
        assert len(qs)==271 and modulus is not None
        if old is None:
            self.put(name,dict(binding,
                coordinate_identity="v_j=w_j for j<271; v_271=P20*w_271-sum(q_j*w_j)",
                exact_existing_sparse_shape_verified=True,
                original_monic_modulus_degree=20,
                new_cusp_kernel_or_field_computed=False))
            old=self.cached(name)
        for key,value in binding.items():assert old[key]==value
        assert old["exact_existing_sparse_shape_verified"] is True
        answer=(qs,modulus,spec(self.path(name)))
        self.cusp_cache[chart]=answer
        return answer

    def derivative_chart_data(self,chart,blocks):
        key=(chart,fingerprint(blocks))
        if self.derivative_read_cache.get("key")!=key:
            values=[self.get(entry) for entry in blocks]
            assert len(values)==17
            for index,value in enumerate(values):
                assert value["chart"]==chart
                assert (value["row_first"],value["row_stop"])==self.ranges[index]
            self.derivative_read_cache={"key":key,"values":values}
        return self.derivative_read_cache["values"]

    def cusp_component(self,chart,target,component,blocks):
        assert target in TARGETS and 0<=component<14
        column=TARGETS.index(target)*14+component
        qs,modulus,cusp_interface=self.cusp_basis(chart)
        name="R825-"+chart+"-"+target+"-component-"+str(component).zfill(2)+"-cusp-coordinates"
        binding={
            "chart":chart,"target":target,"field_component":component,"joint_column_index":column,
            "source_derivative_row_blocks":blocks,"source_cusp_coordinate_interface":cusp_interface,
            "source_R820_cusp_index":self.cusp_specs[chart],
            "source_original_input_component":spec(self.path("R825-input-"+target+"-component-"+str(component).zfill(2))),
            "normal_basis_rank":FREE,"coefficient_field_basis":FIELD,
            "normal_and_cusp_basis_coordinates_are_distinct":True,
            "coordinate_change_only_not_ideal_quotient":True}
        old=self.cached(name)
        if old is None:
            self.budget()
            source=self.derivative_chart_data(chart,blocks)
            vectors=[]
            for block in source:
                denominator=int(block["column_denominators"][column])
                for local in range(block["row_stop"]-block["row_first"]):
                    vectors.append(trim([fmpq(int(block["derivative_coefficient_numerators"][power][local][column]),
                                              denominator) for power in range(8)]))
            assert len(vectors)==FREE
            numerator=list(vectors[271])
            for row,q in enumerate(qs):
                if row%16==0:self.budget()
                numerator=poly_add(numerator,poly_mul(q,vectors[row]))
            quotient,remainder=monic_divide(numerator,modulus)
            assert not remainder and len(quotient)<=7
            assert poly_mul(quotient,modulus)==trim(numerator)
            self.put(name,dict(binding,
                cusp_coordinate_last_row=271,
                cusp_coordinate_last_row_polynomial=[pair(value) for value in quotient],
                coefficient_order="low-to-high powers of z on tau or t on sigma",
                remaining_cusp_coordinate_rows_equal_source_normal_rows=list(range(271)),
                numerator_identity="d_271+sum(q_j*d_j)",
                exact_original_P20_division_remainder_zero=True,
                full_rational_polynomial_product_verified=True,
                actual_derivative_vector_belongs_original_cusp_ideal=True,
                actual_zero_derivative_component=not any(vectors),
                general_ideal_quotient_computed=False))
            old=self.cached(name)
        for key,value in binding.items():assert old[key]==value
        assert old["remaining_cusp_coordinate_rows_equal_source_normal_rows"]==list(range(271))
        assert old["exact_original_P20_division_remainder_zero"] is True
        assert old["full_rational_polynomial_product_verified"] is True
        assert old["actual_derivative_vector_belongs_original_cusp_ideal"] is True
        coefficients=[rational(value) for value in old["cusp_coordinate_last_row_polynomial"]]
        assert trim(coefficients)==coefficients and len(coefficients)<=7
        return spec(self.path(name))

    def target_interface(self,target,blocks,transitions,cusp_components):
        first=TARGETS.index(target)*14
        name="R825-target-"+target+"-two-chart-normal-derivative"
        payload={
            "target":target,"source_original_normal_vector":self.target_specs[target],
            "source_original_input_components":[spec(self.path("R825-input-"+target+"-component-"+str(k).zfill(2)))
                                                for k in range(14)],
            "original_function":"A/tau^5" if target=="A" else "B/tau^5",
            "normal_basis_rank":FREE,"normal_basis_degrees":EPS,"coefficient_field_basis":FIELD,
            "original_b_model":self.tag["original_b_model"],
            "joint_field_column_indices":list(range(first,first+14)),
            "derivative_vector_weighted_bound_on_each_chart":7,
            "regular_g_product_vector_weighted_bound_on_each_chart":8,
            "two_chart_derivative_and_g_product_row_blocks":blocks,
            "complete_two_chart_transition_certificates":transitions,
            "two_chart_original_cusp_coordinate_components":cusp_components,
            "coefficient_reconstruction":"row-block numerator / row-block column_denominator; original target rational_scale already applied once",
            "derivative_transition_is_not_weight7_homogeneous":True,
            "original_sigma_extra_term_minus_5_t7_gv_retained":True,
            "all14_original_field_columns_retained":True,
            "all_normal_weighted_supports_verified":True,
            "all_derivatives_in_original_two_chart_cusp_ideals_verified":True,
            "all_two_chart_rational_polynomial_identities_verified":True,
            "original_field_and_scalar_normalizations_preserved":True,
            "derivative_multiplication_matrix_computed":False,
            "general_polar_ideal_or_D_computed":False,
            "original_eta_principal_functions_rigidification_or_heights_computed":False}
        old=self.cached(name)
        if old is None:self.put(name,payload)
        else:
            for key,value in payload.items():assert old[key]==value
        return spec(self.path(name))

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
        manifest_name="R825-exact-derivative-stages-manifest"
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
