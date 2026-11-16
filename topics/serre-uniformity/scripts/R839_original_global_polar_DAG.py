#!/usr/bin/env python3
"""Assemble exact original global function and polar-ideal expression DAGs.

This consumer does not expand the old unit solves, reconstruct coefficients,
compute a new Fourier coefficient, or execute a polynomial ideal HNF.
Every composite operation below has finite exact semantics in the pinned proof.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import time
import traceback

RESULT = 'R839-original-global-addition-polar-ideal-DAGs'
FINAL = 'p41-original-global-addition-polar-ideal-DAG-certificate.json'
PREFIX = 'R839-global-polar-'
INVENTORY = PREFIX+'stage-manifest.json.gz'
EPS = [0]+[1]*144+[2]*127
LABELS = ['R787','R781','R786','R806','R809','R840','R845','R791']
BASE_KEYS = ['result','run_id','source_commit','core_sha256','manifest_sha256','configuration_sha256']
OLD_TAG = '71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d'
OLD_CORE = '93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04'
OLD_METHOD = '1d91bfc7bdf61c40c4deda19833a5f50491630a61a7a25feb7a3a1e0b451204b'
OLD_PROOF = 'c46008726fb18f52a5430b72c4994ce76164f11bea51044f1677278294f7011d'
FIELD_BASIS = 'b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b'
RATIOS = [('31','67'),('-41','67'),('-34','67'),('34','67'),('103','134')]
PQ = [(165,67),(93,67),(100,67),(168,67),(371,134)]
ORIGINAL_DEGREES = [2970,1674,1800,3024,3339]
SCOPE = {
    'p':41,'original_map_index':4,'original_map_degree':'1206',
    'canonical_free_column':1186,'original_unit_chart_shape':[2420,2420],
    'original_relation_condition_shape':[129,20,14],
    'normal_basis_rank':272,'normal_basis_degrees':EPS,
    'original_power5_dimension':1234,'S5_short_shape':[1380,1234],
    'original_Galois_order_over_K':7,'original_addition_exponents':[1,2,3,4,5],
    'global_base_pole_generator_count':8,'projective_minor_functions_per_map':3,
    'derivative_mode':'one_original_global_dz_y_and_Galois_conjugates',
    'derivative_backend':'source_bound_characteristic_polynomial_and_on_demand_cyclic_solve',
    'ideal_convention':'I_E=O(-E) embedded in the original function field',
    'old_numeric_arithmetic_recomputed':False,
    'no_modular_vector_used_as_characteristic_zero_coefficients':True,
    'no_CM_response_used_as_global_function':True,
    'no_arbitrary_cube_root_or_unknown_elliptic_division':True,
    'true_Galois_norm_preserves_all_original_field_constants':True,
    'output_representation':'finite_exact_source_bound_expression_DAG',
    'budget_and_absolute_directories_excluded_from_mathematical_identity':True,
}
H64 = re.compile(r'[0-9a-f]{64}')
INTEGER = re.compile(r'-?(0|[1-9][0-9]*)')
POSITIVE = re.compile(r'[1-9][0-9]*')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b''): h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def read(path):
    path=Path(path)
    with (gzip.open if path.suffix=='.gz' else open)(path,'rt',encoding='utf-8') as stream:
        return json.load(stream)


def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.tmp')
    raw=(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':
        with temporary.open('wb') as stream:
            with gzip.GzipFile(filename='',mode='wb',fileobj=stream,mtime=0) as zipped:
                zipped.write(raw)
    else: temporary.write_bytes(raw)
    temporary.replace(path)


def plain(entry):
    value={key:entry[key] for key in ('file','bytes','sha256')}
    assert isinstance(value['file'],str) and Path(value['file']).name==value['file']
    assert value['file'] not in ('.','..') and '\\' not in value['file']
    assert isinstance(value['bytes'],int) and value['bytes']>=0 and H64.fullmatch(value['sha256'])
    return value


def spec(path):
    path=Path(path)
    return {'file':path.name,'bytes':path.stat().st_size,'sha256':sha(path)}


def identity(item):
    return {key:item[key] for key in BASE_KEYS}


def same_origin(left,right):
    for key in ('result','run_id','source_commit','core_sha256','manifest_sha256'):
        assert str(left[key])==str(right[key]),('Producer mismatch',key)


class BudgetStop(Exception):
    pass


class Source:
    def __init__(self,label,item):
        self.label,self.item,self.directory=label,item,Path(item['directory'])
        self.identity=identity(item)
        self.files={name:plain(entry) for name,entry in item['files'].items()}
        assert all(name==entry['file'] for name,entry in self.files.items())
        selected=[self.files[n] for n in sorted(self.files)]
        assert fingerprint(selected)==item['selected_files_sha256']
        assert len(selected)==item['selected_file_count']
        self.verified=set()
        manifest=self.get('full-outputs-manifest.json',stage=False)
        assert self.files['full-outputs-manifest.json']['sha256']==item['manifest_sha256']
        assert manifest['result']==item['result']
        self.inventory={entry['file']:plain(entry) for entry in manifest['files']}
        assert len(self.inventory)==len(manifest['files'])
        for name,entry in self.files.items():
            if name not in ('full-outputs-manifest.json','full-outputs-manifest-reference.json'):
                assert self.inventory[name]==entry
            self.bound(name)
        certname=item.get('certificate_name')
        self.certificate=self.get(certname,stage=False) if certname else None
        if self.certificate is not None:
            assert self.certificate['result']==item['result'] and self.certificate['complete'] is True
            self.tag=self.certificate['configuration']
        else:
            self.tag=self.get(item['configuration_stage'],stage=False)['configuration']
        assert fingerprint(self.tag)==item['configuration_sha256']
        assert self.tag['result']==item['result'] and self.tag['source_sha256']==item['core_sha256']
        if 'run-receipt.json' in self.files:
            run=self.get('run-receipt.json',stage=False)
            assert str(run['workflow_run_id'])==str(item['run_id'])
            assert run['source_commit']==item['source_commit']
        if 'public-actions-input.json' in self.files:
            public=self.get('public-actions-input.json',stage=False)
            assert public['source_commit']==item['source_commit']
            assert public['job']['core_sha256']==item['core_sha256']
            if label!='R791':assert public['core_sha256']==item['core_sha256']
        if 'core-receipt.json' in self.files:
            core=self.get('core-receipt.json',stage=False)
            assert core['source_sha256']==item['core_sha256']

    def bound(self,name):
        entry=self.files[name];path=self.directory/name
        if name not in self.verified:
            assert spec(path)==entry,('Changed original file',self.label,name)
            self.verified.add(name)
        return path

    def get(self,name,stage=True):
        value=read(self.bound(name))
        if stage:
            assert value['complete'] is True and value['configuration']==self.tag
        return value

    def indexed(self,entry,stage=True):
        entry=plain(entry);assert self.files[entry['file']]==entry
        return self.get(entry['file'],stage)

    def ref(self,name):
        return dict(self.files[name],producer=self.label)

    def ref_indexed(self,entry):
        entry=plain(entry);assert self.files[entry['file']]==entry
        return dict(entry,producer=self.label)


class Graph:
    """Typed finite expression graph; no coefficient expansion is performed."""
    def __init__(self):
        self.nodes=[];self.by_id={};self.obligations={};self.galois_definition=None

    def node(self,operation,domain,inputs=(),**data):
        inputs=list(inputs)
        assert all(value in self.by_id for value in inputs)
        body={'operation':operation,'domain':domain,'inputs':inputs,'data':data}
        key='n'+fingerprint(body)
        if key not in self.by_id:
            item=dict(body,id=key,ordinal=len(self.nodes))
            self.nodes.append(item);self.by_id[key]=item
        return key

    def proof(self,name,statement,reason,sources=(),**data):
        value={'statement':statement,'reason':reason,'sources':list(sources),**data}
        assert name not in self.obligations or self.obligations[name]==value
        self.obligations[name]=value
        return name

    def field(self,value):
        assert INTEGER.fullmatch(str(value))
        return self.node('original_rational_integer','F',decimal=str(value))

    def add(self,*args):
        assert args and all(self.by_id[x]['domain']=='F' for x in args)
        return self.node('field_add','F',args)

    def mul(self,*args):
        assert args and all(self.by_id[x]['domain']=='F' for x in args)
        return self.node('field_multiply','F',args)

    def neg(self,value):
        return self.mul(self.field(-1),value)

    def sub(self,left,right):
        return self.add(left,self.neg(right))

    def power(self,value,n):
        assert self.by_id[value]['domain']=='F' and isinstance(n,int) and n>=0
        return self.node('field_nonnegative_power','F',[value],exponent=n)

    def divide(self,left,right,reason):
        assert self.by_id[left]['domain']==self.by_id[right]['domain']=='F'
        assert reason in self.obligations
        return self.node('field_divide','F',[left,right],denominator_nonzero_proof=reason)

    def gal(self,value,j):
        assert isinstance(j,int) and 0<=j<7
        assert self.galois_definition in self.by_id
        return self.node('original_Galois_conjugate_over_K',self.by_id[value]['domain'],[value],
            exponent=j,acts_on_whole_expression=True,fixes_original_K_curve_and_normal_basis=True,
            Galois_definition_node=self.galois_definition,
            no_T_as_curve_automorphism=True)

    def ipower(self,value,n):
        assert self.by_id[value]['domain'] in ('I_tau','I_sigma') and n>=0
        return self.node('invertible_fractional_ideal_nonnegative_power',self.by_id[value]['domain'],[value],exponent=n)

    def imul(self,*args):
        domain=self.by_id[args[0]]['domain']
        assert domain in ('I_tau','I_sigma') and all(self.by_id[x]['domain']==domain for x in args)
        return self.node('invertible_fractional_ideal_product',domain,args)

    def ispan(self,chart,values,nonzero_reason):
        assert all(self.by_id[x]['domain']=='F' for x in values)
        assert nonzero_reason in self.obligations
        return self.node('sum_of_principal_fractional_ideals','I_'+chart,values,
            all_generators_not_simultaneously_zero_proof=nonzero_reason,
            individual_zero_generator_allowed=True)

    def inorm(self,value):
        return self.imul(*(self.gal(value,j) for j in range(7)))

    def fnorm(self,value):
        return self.mul(*(self.gal(value,j) for j in range(7)))

    def check(self):
        seen=set()
        for i,node in enumerate(self.nodes):
            assert node['ordinal']==i and all(x in seen for x in node['inputs'])
            body={k:node[k] for k in ('operation','domain','inputs','data')}
            assert node['id']=='n'+fingerprint(body)
            seen.add(node['id'])
        assert seen==set(self.by_id)
        for node in self.nodes:
            for key in ('denominator_nonzero_proof','all_generators_not_simultaneously_zero_proof'):
                if key in node['data']: assert node['data'][key] in self.obligations
            if 'Galois_definition_node' in node['data']:
                reference=node['data']['Galois_definition_node']
                assert reference in self.by_id and self.by_id[reference]['ordinal']<node['ordinal']
        for value in self.obligations.values():
            assert all(reference in self.obligations for reference in value.get('proof_ids',[]))


class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic();self.out=Path(args.out);self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item['result']==RESULT and self.item['p']==41
        assert self.item['producer_inputs_pending'] is False and sha(__file__)==self.item['core_sha256']
        assert sha(self.item['proof_absolute_path'])==self.item['proof_sha256']
        assert sha(self.item['method_absolute_path'])==self.item['method_sha256']
        assert set(self.item['sources'])==set(LABELS)
        self.sources={label:Source(label,self.item['sources'][label]) for label in LABELS}
        self.tag={'result':RESULT,'source_sha256':sha(__file__),
            'proof_sha256':self.item['proof_sha256'],'method_sha256':self.item['method_sha256'],
            'source_identities':{label:dict(source.identity,
                selected_files_sha256=source.item['selected_files_sha256'],
                selected_file_count=source.item['selected_file_count']) for label,source in self.sources.items()},
            'arithmetic':'symbolic exact original expression composition; no old numerical arithmetic executed',**SCOPE}
        self.prepare()

    def budget(self):
        if time.monotonic()-self.started>self.args.budget_minutes*60:
            raise BudgetStop('Complete original source and DAG stages retained.')

    def path(self,name):
        assert name.startswith(PREFIX) and Path(name).name==name
        return self.out/(name if name.endswith('.json.gz') else name+'.json.gz')

    def cached(self,name):
        path=self.path(name)
        if not path.exists(): return None
        value=read(path);assert value['configuration']==self.tag and value['complete'] is True
        return value

    def store(self,name,value):
        prior=self.cached(name)
        if prior is not None:return prior
        self.budget();value=dict(value,result=RESULT,configuration=self.tag,complete=True)
        save(self.path(name),value)
        print(json.dumps({'stage':name,'seconds':round(time.monotonic()-self.started,3)}),flush=True)
        return value

    def ref(self,name):return spec(self.path(name))

    def prepare(self):
        r787,r781,r786,r806,r809,r840,r845,r791=(self.sources[x] for x in LABELS)
        assert fingerprint(r787.tag)==OLD_TAG and r787.tag['source_sha256']==OLD_CORE
        assert r787.tag['R787_method_sha256']==OLD_METHOD and r787.tag['R786_proof_sha256']==OLD_PROOF
        assert r787.tag['basis_dimension']==1234 and r787.tag['basis_integer_scale']=='13744803133596058624'
        self.field=r787.tag['field'];assert self.field['original_b_replaced_by_another_twist'] is False
        # This unchanged R781 descriptor is M^+=L(t_xi), of degree 280.
        # The relation unknowns are in L=Q(B,s), of degree 14; each
        # original Laurent coefficient has 20 real cyclotomic coordinates.
        assert self.field['dimension_over_Q']==280
        same_origin(r787.tag['retained_artifacts']['R781'],r781.item)
        same_origin(r787.tag['retained_artifacts']['R786'],r786.item)
        self.chart=r787.get('R787-prime-1000000753-chart.json.gz')
        self.blocks=r787.get('R787-prime-1000000753-rational-blocks.json.gz')
        self.selection=r787.get('R787-prime-1000000753-selection.json.gz')
        assert self.chart['chosen_free_column']==1186 and self.chart['actual_modular_rank']==1186
        assert self.chart['other_free_columns_set_to_zero'] is True
        # The persisted initial chart predates the all-branch verification.
        # The bound R840 unit-chart expression below certifies the full
        # original relation; this historical source flag remains unchanged.
        assert self.chart['all_14_branches_already_verified'] is False
        assert self.blocks['exact_E0_Z_zero_verified'] is True
        assert self.blocks['A_inverse_over_Q_computed'] is False
        self.pivots=self.chart['pivot_columns'];assert len(set(self.pivots))==1186
        self.free=[i for i in range(1214) if i not in set(self.pivots)]
        assert len(self.free)==28 and 1186 in self.free
        self.J=self.blocks['A_pivot_rows'];self.R=self.blocks['A_remaining_rows']
        assert len(self.J)==1234 and len(self.R)==1326 and sorted(self.J+self.R)==list(range(2560))
        self.rows=self.J+[self.R[i] for i in self.chart['pivot_rows']]
        assert len(self.rows)==2420 and len(set(self.rows))==2420
        assert POSITIVE.fullmatch(str(self.blocks['Z_free_diagonal']))
        assert len(self.blocks['B_constant_pivot_columns'])==20
        assert len(self.blocks['B_constant_free_columns'])==1214
        for key in ('prime_proved','all_14_L_branches_distinct','all_kappa_reductions_invertible','all_rational_denominators_units'):
            assert self.selection[key] is True
        self.original_F=[]
        basis=r786.indexed(r786.certificate['basis_index'])
        assert basis['dimension']==1234 and basis['integer_scale']=='13744803133596058624'
        for i in range(1234):
            name='R787-real-power5-row-'+str(i).zfill(4)+'.json.gz'
            row=r787.get(name)
            assert row['index']==i and row['R786_row_sha256']==basis['basis_rows'][i]['sha256']
            assert len(row['integer_t_coefficients'])==129
            assert all(len(x)==20 for x in row['integer_t_coefficients'])
            assert row['all_original_phase_involutions_verified'] is True and row['averaging_used'] is False
            self.original_F.append(r787.ref(name))
        self.laurent=[r781.ref('R781-inverse-free-Laurent-'+str(m).zfill(3)+'.json.gz') for m in range(130)]
        previous=None
        for m,entry in enumerate(self.laurent):
            value=r781.get(entry['file'])
            assert value['order']==m and value['exact_differential_identity_at_this_order'] is True
            if previous is not None: assert value['previous_stage_sha256']==previous['sha256']
            else:
                assert value['input_stage_sha256']==r781.files['R781-original-real-field-input.json.gz']['sha256']
                self.kappa_spec=entry
            previous=entry
        self.field_source=r781.ref('R781-original-real-field-input.json.gz')
        assert r781.get(self.field_source['file'])['field']==self.field
        self.expression_spec=r840.certificate['implicit_expression']
        self.expression=r840.indexed(self.expression_spec)
        assert self.expression['original_relation_exactly_defined_by_unit_chart'] is True
        assert self.expression['original_field']==self.field
        original=[plain(x) for x in self.expression['operator_recipe']['original_F_rows']]
        assert original==[plain(x) for x in self.original_F]
        for key,name in [('original_chart','R787-prime-1000000753-chart.json.gz'),
                         ('original_Z_and_A_row_selection','R787-prime-1000000753-rational-blocks.json.gz')]:
            assert plain(self.expression['unit_chart_solve'][key])==r787.files[name]
        assert self.expression['unit_chart_solve']['row_order']==self.rows
        assert self.expression['unit_chart_solve']['free_column']==1186
        assert self.expression['unit_chart_solve']['second_block_columns']['pivot_columns']==self.pivots
        c806=r806.certificate
        for key in ('exact_polynomial_multiplication_computed','all272_columns_verified_in_all820_original_rows',
                    'actual_cyclic_minor_certified','original_function_field_primitive_generator_certified','normal_integral_basis_preserved'):
            assert c806[key] is True
        self.wspec=c806['polynomial_multiplier'];self.wdata=r806.indexed(self.wspec)
        assert self.wdata['coordinate_groups']==c806['exact_coordinate_groups']
        assert self.wdata['normal_affine_basis_rank']==272 and self.wdata['normal_affine_basis_degrees']==EPS
        assert self.wdata['matrix_convention']=='M_ba(z) is output row b, input column a'
        assert c806['actual_w0_original_M2_integer_coordinates']==['0','0','1']+['0']*143
        self.wgroups=[];columns=[]
        for entry in self.wdata['coordinate_groups']:
            group=r806.indexed(entry);columns+=group['column_indices']
            assert group['integer_scale']=='304006671424'
            for key in ('all820_original_coordinates_verified','weighted_polynomial_support_verified','reduction_equals_successful_modular_multiplier'):
                assert group[key] is True
            assert len(group['coordinate_numerators'])==690
            assert all(len(row)==len(group['column_indices']) for row in group['coordinate_numerators'])
            assert all(POSITIVE.fullmatch(str(x)) for x in group['column_denominators'])
            self.wgroups.append(r806.ref_indexed(entry))
        assert columns==list(range(272)) and len(self.wgroups)==34
        self.cyclic_spec=self.wdata['actual_cyclic_witness'];cyclic=r806.indexed(self.cyclic_spec)
        assert cyclic['actual_cyclic_rank']==272 and cyclic['actual_determinant_mod_prime']!=0
        self.s5spec=r809.certificate['S5_basis_index'];self.s5=r809.indexed(self.s5spec)
        assert self.s5['dimension']==1234 and self.s5['qY_count']==69
        assert r809.certificate['normal_basis_rank']==272 and r809.certificate['normal_basis_degrees']==EPS
        assert r809.certificate['coefficient_field_basis']==FIELD_BASIS
        assert r809.certificate['original_scalar_and_field_normalizations_preserved'] is True
        assert r809.certificate['original_b_model']==self.field['original_b_minimal_polynomial']
        same_origin(r806.tag['retained_artifacts']['R805'],r809.tag['basis_producers']['R805'])
        assert self.wdata['original_R805_free_basis']==r809.tag['original_graded_free_basis']
        self.s5rows=[]
        for i,row in enumerate(self.s5['basis_rows']):
            assert row['index']==i
            data=r809.indexed(row['source'])
            assert data['index']==i and data['integer_scale']=='13744803133596058624'
            assert data['qY_count']==69 and data['real_coordinate_count']==20
            assert len(data['integer_v_t_coefficients'])==69
            assert all(len(coefficients)==20 for coefficients in data['integer_v_t_coefficients'])
            assert data['all_original_term_phases_and_scales_verified'] is True
            self.s5rows.append(r809.ref_indexed(row['source']))
        self.minor_spec=r809.certificate['minor_stage'];self.minor=r809.indexed(self.minor_spec)
        assert self.minor['actual_rank']==1234 and self.minor['actual_determinant_mod_prime']!=0
        assert self.minor['column_indices']==list(range(1234))
        assert len(set(self.minor['row_indices']))==1234
        self.C={}
        assert set(r809.certificate['completed_target_groups'])=={'C'+str(j) for j in range(6)}
        for j in range(6):
            key='C'+str(j);entry=r809.certificate['normal_vectors'][key]
            index=r809.indexed(entry)
            assert index['target']==key and index['normal_basis_rank']==272
            assert index['regular_degree_bound']==4 and len(index['coordinate_groups'])==2
            assert index['normal_function']=='theta*U_'+str(j)+'/tau^4'
            assert index['normal_vector_actually_nonzero'] is True
            assert index['literal_tau_factor_highest_S5_coefficients_zero'] is True
            assert index['target_configuration']['original_b_model']==self.field['original_b_minimal_polynomial']
            groups=[];columns=[]
            for group_entry in index['coordinate_groups']:
                group=r809.indexed(group_entry)
                assert group['target']==key and group['all1380_original_coordinates_verified'] is True
                assert group['original_field_and_scalar_normalizations_preserved'] is True
                assert group['coefficient_field_basis']==FIELD_BASIS
                assert group['S5_basis_index']==self.s5spec
                assert group['target_configuration']==index['target_configuration']
                assert len(group['coordinate_numerators'])==1234
                assert all(len(x)==7 for x in group['coordinate_numerators'])
                columns+=group['column_indices'];groups.append(r809.ref_indexed(group_entry))
            assert columns==list(range(14))
            self.C[key]={'index':r809.ref_indexed(entry),'groups':groups,
                'target_configuration_sha256':index['target_configuration_sha256']}
        self.pole_spec=r845.certificate['pole_ideal_DAG'];self.pole=r845.indexed(self.pole_spec)
        assert r845.certificate['actual_pencil_rank']==1111
        for key in ('complete_original_D_pencil_certified','complete_original_Ey_ideal_certified'):
            assert r845.certificate[key] is True
        for key in ('complete_original_D_ideal_certified','complete_original_Ey_ideal_certified',
                    'eight_source_bound_generators_supplied','both_original_affine_chart_trivializations_preserved',
                    'canonical_ideal_embedding_not_only_Picard_class'):
            assert self.pole[key] is True
        assert self.pole['original_Ey_degree']==1206
        assert self.pole['existing_followup_identity']=='I_EyR=(original_y^2-original_b)*I_Ey^3; requires the original global y DAG'
        self.hom_name='R791-original-Hom-Galois-matrices.json.gz'
        self.eta_name='R791-original-real-descent-and-eta-basis-inputs.json.gz'
        self.hom=r791.get(self.hom_name);self.eta=r791.get(self.eta_name)
        assert self.hom['all_84_coordinates_verified'] is True
        assert len(self.hom['rho_iterates_zero_through_seven'])==8
        assert self.hom['gamma_order']==21 and self.hom['remaining_elliptic_factor_included'] is False
        assert self.eta['all_original_F0_directions_covered'] is True
        assert self.eta['original_F0_dimension']==5
        assert self.eta['unknown_original_kappa_set_to_one'] is False
        assert self.eta['original_vdagger_v_replaced_by_scalar'] is False
        assert self.eta['original_q_alpha_or_c1_changed'] is False
        for j,row in enumerate(self.eta['degree_zero_basis'],1):
            assert row['j']==j and row['degree_zero_coefficient_dj_over_d0']==list(RATIOS[j-1])
        self.store(PREFIX+'source-audit',{
            'original_field':self.field,'original_global_unit_expression':r840.ref_indexed(self.expression_spec),
            'all_1234_original_real_rows_present':True,'all130_original_Laurent_stages_present':True,
            'global_W_complete_coordinate_group_count':34,'six_C_complete_coordinate_group_count':12,
            'global_matrices_not_replaced_by_five_fiber_values':True,
            'source_original_W':r806.ref_indexed(self.wspec),'source_original_cyclic_witness':r806.ref_indexed(self.cyclic_spec),
            'source_original_S5':r809.ref_indexed(self.s5spec),'source_original_pole_DAG':r845.ref_indexed(self.pole_spec),
            'source_Galois_and_Hom':r791.ref(self.hom_name),'source_original_eta_basis':r791.ref(self.eta_name),
            'original_2420_or_1186_solve_expanded':False,'new_old_numerical_arithmetic_executed':False})

    def graph(self):
        name=PREFIX+'exact-global-function-and-five-polar-expression-DAG'
        prior=self.cached(name)
        if prior is not None:return prior
        g=Graph();r787,r781,r786,r806,r809,r840,r845,r791=(self.sources[x] for x in LABELS)
        pr=g.proof('original_unit_chart','det(M)!=0 and selected kernel equals complete kernel',
            'Original U.1: same 28-dimensional kernel, fixed unit chart; not CM evaluation',
            [r840.ref_indexed(self.expression_spec),r787.ref('R787-prime-1000000753-chart.json.gz')])
        b_nonzero=g.proof('original_B_nonzero','B!=0',
            'Z is injective and original free coordinate1186 is1; U.1',[r787.ref('R787-prime-1000000753-rational-blocks.json.gz')])
        s_nonzero=g.proof('original_y_nonconstant','u and each true conjugate are nonconstant; u^2-b!=0',
            'Original nonzero Hom f4 has degree1206; no arbitrary translation',[r840.ref_indexed(self.expression_spec)])
        h_nonzero=g.proof('original_Hodge_C0_nonzero','C0=theta*H_f^3/tau^4!=0',
            'Original nonzero global Hom differential and completed nonzero theta',[self.C['C0']['index']])
        k_nonzero=g.proof('original_cyclic_K','det(K(z))!=0',
            'Actual R806 characteristic-zero-compatible cyclic minor', [r806.ref_indexed(self.cyclic_spec)])
        separable=g.proof('original_primitive_separability','chi_T(z,w)!=0',
            'Original field degree272 and characteristic0; chi is the minimal polynomial',
            [r806.ref_indexed(self.wspec),r806.ref_indexed(self.cyclic_spec)])
        deriv_nonzero=g.proof('global_y_derivative','dz(u)!=0 and all sigma-conjugates are nonzero',
            'Nonconstant map in original characteristic-zero function field; z defined over K',
            [r840.ref_indexed(self.expression_spec),r806.ref_indexed(self.wspec)])
        s5_unit=g.proof('original_S5_unit','det(S5[I5])!=0',
            'Completed original rational S5 basis and actual selected minor',[r809.ref_indexed(self.minor_spec)])
        fmatrix=g.node('original_power5_real_coefficient_matrix','Mat_Z_2580_1234',
            sources=self.original_F,source_coordinate_order='v^n*t^r,n0..128,r0..19',
            source_coefficient_key='integer_t_coefficients',
            original_phase='v=xi^(-10)*qY',original_integer_scale='13744803133596058624')
        zmat=g.node('original_sparse_constant_kernel_Z','Mat_Z_1234_1214',
            source=r787.ref('R787-prime-1000000753-rational-blocks.json.gz'),
            formula='Z[P,:]=stored Z_pivot_integer_rows; Z[Q,:]=Z_free_diagonal*I',
            no_second_minus_sign=True)
        ylaurent=g.node('original_finite_Laurent_operator_Y','L_t_v_0_128',
            original_field_source=self.field_source,sources=self.laurent,
            formula='Y_m=-(1/246^3)*R_m*kappa^(-m-1),m0..128',
            R_coefficient_key='coefficients.R',kappa_source=self.kappa_spec,kappa_coefficient_key='kappa',
            t_modulus=self.field['real_cyclotomic_minimal_polynomial'],
            original_field=self.field,nonzero_kappa_source=r787.ref('R787-prime-1000000753-selection.json.gz'))
        cmatrix=g.node('original_uncleared_C_convolution_matrix','Mat_L_2560_1214',[fmatrix,zmat,ylaurent],
            formula='C*c=coefficients(v^1..v^128) of Y*(F*Z*c);20 original t coordinates',
            no_individual_cleared_row_substitution=True)
        mmatrix=g.node('original_selected_relation_matrix','Mat_L_2420_2420',[fmatrix,cmatrix],
            rows=self.rows,A_rows_range=[0,2560],A_columns=list(range(1234)),
            C_columns=self.pivots,C_block_sign=-1,coefficient_field='Q(B_fld,s),s^2=-3')
        rhs=g.node('original_selected_free_right_hand_side','Vec_L_2420',[cmatrix],
            rows=self.rows,column=1186,sign=1)
        xi=g.node('unit_matrix_solve','Vec_L_2420',[mmatrix,rhs],
            nonzero_determinant_proof=pr,exact_semantics='adj(M)*r/det(M)',expanded=False)
        avec=g.node('vector_slice','Vec_L_1234',[xi],first=0,stop=1234)
        cvec=g.node('fill_original_free_and_pivot_coordinates','Vec_L_1214',[xi],
            pivot_columns=self.pivots,pivot_solution_slice=[1234,2420],
            free_columns=self.free,free_values={str(i):int(i==1186) for i in self.free})
        bvec=g.node('matrix_vector_product','Vec_L_1234',[zmat,cvec])
        f5=g.node('original_short_prefix_matrix','Mat_Q_1380_1234',[fmatrix],
            first_rows=1380,exactly_the_existing_first69_blocks=True)
        s5=g.node('original_S5_coefficient_matrix','Mat_Q_1380_1234',sources=self.s5rows,
            index=r809.ref_indexed(self.s5spec),all_original_rows_preserved=True,
            source_coefficient_key='integer_v_t_coefficients',
            source_coordinate_order='v^n*t^r,n0..68,r0..19',
            original_integer_scale='13744803133596058624')
        unit_s5=g.node('original_S5_selected_matrix','Mat_Q_1234_1234',[s5],
            minor_source=r809.ref_indexed(self.minor_spec),row_indices_from_source=True)
        normal=[]
        for vector,label in [(avec,'A'),(bvec,'B')]:
            target=g.node('matrix_vector_product','Vec_L_1380',[f5,vector])
            targeti=g.node('same_original_S5_row_selection','Vec_L_1234',[target],
                minor_source=r809.ref_indexed(self.minor_spec))
            q=g.node('unit_matrix_solve','Vec_L_1234',[unit_s5,targeti],
                nonzero_determinant_proof=s5_unit,expanded=False,
                exact_membership_reason='original '+label+' is in original V5 and S5 is a complete basis')
            normal.append(g.node('original_S5_normal_polynomial_vector','Vec_Lz_272',[q],
                source_row_mapping=r809.ref_indexed(self.s5spec),
                coefficient_embedding='B_fld=lambda*b;s=1+2*zeta; apply exactly once',
                original_lambda=self.field['lambda'],section_denominator='tau^5',extra_content_or_scale_reinserted=False))
        w=g.node('original_exact_polynomial_multiplier_W','Mat_Qz_272_272',
            interface=r806.ref_indexed(self.wspec),coordinate_groups=self.wgroups,
            decode='coordinate_numerators[S_row,local]/column_denominators[local]; use original S_row_to_polynomial_coefficient',
            original_basis_mapping=self.wdata['S_row_to_polynomial_coefficient'],
            convention='output row,input column',integer_S3_scale_consumed_exactly_once=True)
        krylov=g.node('original_cyclic_matrix','Mat_Qz_272_272',[w],
            columns='e0,W*e0,...,W^271*e0',global_matrix_inverse_expanded=False)
        characteristic=g.node('characteristic_polynomial','Q_z_T',[w],
            formula='det(T*I-W(z))',degree_T=272,determinant_expanded=False)
        a_b_in_field=[]
        for vec in normal:
            cv=g.node('unit_matrix_solve','Vec_Lz_fraction_272',[krylov,vec],
                nonzero_determinant_proof=k_nonzero,only_this_required_right_hand_side=True,
                global_matrix_inverse_expanded=False)
            a_b_in_field.append(g.node('original_primitive_power_basis_element','F',[cv,characteristic],
                primitive_element='w=e2/tau',T_maps_to_original_w=True))
        global_y=g.divide(a_b_in_field[0],a_b_in_field[1],b_nonzero)
        dy=g.node('separable_original_function_field_derivative','F',[global_y,characteristic],
            formula='partial_z F=F_z-F_T*chi_z/chi_T',
            denominator_nonzero_proof=separable,constant_field='original L',
            no_expanded_R815_Gamma_assumed=True)
        original_b=g.node('original_field_generator_b','F',field=self.field,
            original_b_model_preserved=True)
        ss=g.sub(g.power(global_y,2),original_b)
        hodge={}
        for j in range(6):
            key='C'+str(j)
            nv=g.node('original_completed_Hodge_normal_vector','Vec_Lz_272',
                sources=self.C[key],S5_index=r809.ref_indexed(self.s5spec),
                source_field_basis=FIELD_BASIS,
                decode='for each original field column: numerator/group_denominator * original_target_rational_scale; then original S5 row_mapping',
                all14_components_and_original_rational_scale_preserved=True,
                theta_not_inverted_or_rescaled=True)
            pv=g.node('unit_matrix_solve','Vec_Lz_fraction_272',[krylov,nv],
                nonzero_determinant_proof=k_nonzero,only_this_required_right_hand_side=True,
                global_matrix_inverse_expanded=False)
            hodge[key]=g.node('original_primitive_power_basis_element','F',[pv,characteristic],
                primitive_element='w=e2/tau',T_maps_to_original_w=True)
        bases={}
        for chart in ('tau','sigma'):
            bases[chart]=g.node('external_certified_eight_generator_fractional_ideal','I_'+chart,
                source=r845.ref_indexed(self.pole_spec),chart=chart,
                source_exact_section_nodes=self.pole['sections'],
                source_homogeneous_generators=self.pole['Ey_homogeneous_generators'],
                denominator_power=11,modular_kernel_coordinates_are_not_characteristic_zero_coefficients=True,
                exact_section_semantics='preserve source original unit-kernel solves and original anchor scales')
        galois_source=r791.ref(self.hom_name)
        g.galois_definition=g.node('original_Galois_automorphism_definition','Aut_L_over_K',
            source=galois_source,original_field=self.field,
            image_of_original_b=self.hom['field_sigma_b'],fixes_zeta=True,order=7,
            source_encoding='two rational b-polynomials a(b)+zeta*bpoly(b)',
            canonical_encoding='b^0..b^6,s*b^0..s*b^6; s=1+2*zeta',
            exact_encoding_conversion='zeta=(s-1)/2; no change of b root or curve frame',
            fixes_original_z_w_and_normal_basis=True)
        base_norm_function=g.fnorm(ss)
        base_norm_ideals={chart:g.inorm(value) for chart,value in bases.items()}
        outputs={};comparisons={};relative={};proofs=[]
        for j,(p,q) in enumerate(PQ,1):
            self.budget()
            rho=g.node('original_R791_rho_iterate','F',source=galois_source,
                original_index=j,encoding='a(b)+zeta*bpoly(b), original QKField encode',
                source_value=self.hom['rho_iterates_zero_through_seven'][j])
            rho_nz=g.proof('rho_'+str(j),'rho_j!=0',
                'Original target isomorphism; rho_j^6=sigma^j(b)/b', [galois_source])
            v=g.divide(g.gal(global_y,j),g.power(rho,3),rho_nz)
            dv=g.divide(g.gal(dy,j),g.power(rho,3),rho_nz)
            uj=g.divide(hodge['C'+str(j)],hodge['C0'],h_nonzero)
            ratio=g.mul(uj,g.divide(g.sub(g.power(v,2),original_b),ss,s_nonzero),
                        g.divide(dy,dv,deriv_nonzero))
            hom_nz=g.proof('nonzero_original_sum_'+str(j),'f+T^j f!=0',
                '1+T^j is nonzero in original Q[T]/Phi21; original Hom is its rank1 module; c0 translations fixed',
                [galois_source],j=j)
            difference=g.proof('original_x_difference_'+str(j),'r_j^x-1!=0',
                'Otherwise T^j f=+f or -f; excluded in original Phi21 field for j1..5',
                [galois_source],j=j)
            first=g.mul(ss,g.power(g.sub(g.field(1),ratio),3))
            second=g.power(g.add(global_y,v),3)
            third=g.mul(ss,g.power(g.add(v,g.mul(ratio,global_y)),3))
            ideals={}
            for chart in ('tau','sigma'):
                ideal=g.imul(g.ipower(bases[chart],3),g.ipower(g.gal(bases[chart],j),3),
                    g.ispan(chart,[first,second,third],hom_nz))
                ideals[chart]=ideal
            rminus=g.sub(ratio,g.field(1));vdiff=g.sub(v,global_y)
            ysum=g.sub(g.add(g.neg(global_y),
                g.divide(g.mul(vdiff,g.add(g.field(2),ratio)),rminus,difference)),
                g.divide(g.power(vdiff,3),g.mul(g.power(rminus,3),ss),
                    g.proof('secant_denominator_'+str(j),'(r_j^x-1)^3*(u^2-b)!=0',
                        'Product of original proven nonzero functions',proof_ids=[difference,s_nonzero])))
            rg=g.sub(g.power(ysum,2),original_b)
            nonconstant_sum=g.proof('sum_y_nonconstant_'+str(j),'y_(f+T^j f)^2-b!=0',
                'Nonzero original Hom sum is a nonconstant map', [galois_source],j=j)
            fnorm=g.fnorm(rg)
            principal=g.divide(g.power(fnorm,q),g.power(base_norm_function,p),
                g.proof('base_norm_nonzero_'+str(j),'N(u^2-b)^p!=0',
                    'Product and positive power of conjugates of a nonzero field element',proof_ids=[s_nonzero]))
            comparison_nonzero=g.proof('comparison_function_nonzero_'+str(j),'R_j!=0',
                'Quotient of positive powers of true field norms of nonzero functions',
                proof_ids=[s_nonzero,nonconstant_sum])
            eta_ideals={};real_ideals={};real_poles={}
            for chart in ('tau','sigma'):
                normsum=g.inorm(ideals[chart])
                invbase=g.node('invertible_fractional_ideal_inverse','I_'+chart,[base_norm_ideals[chart]],
                    semantics='(R:I) in the fraction field, without intersection truncation')
                eta_ideals[chart]=g.imul(g.ipower(normsum,q),g.ipower(invbase,p))
                real_ideals[chart]=g.imul(g.ispan(chart,[principal],comparison_nonzero),g.ipower(eta_ideals[chart],3))
                real_poles[chart]=g.imul(g.ispan(chart,[rg],nonconstant_sum),g.ipower(ideals[chart],3))
            relative[str(j)]={'rho':rho,'y_Tj_f':v,'h_Tj_f_over_h_f':uj,
                'x_Tj_f_over_x_f':ratio,'three_projective_minor_cubes':[first,second,third]}
            outputs[str(j)]={'original_Hom_word':'1+T^'+str(j),'original_map_degree':ORIGINAL_DEGREES[j-1],
                'global_pole_ideals':ideals,'real_descent_pole_ideals':real_poles,
                'source_eta_basis':r791.ref(self.eta_name),'source_original_hj_index':j,
                'p':p,'q':q,'eta_degree_zero_fractional_ideal':eta_ideals,
                'eta_Picard_class':{'sign':-1,'rational_denominator':q,
                    'ideal_nodes':eta_ideals,'original_kappa_polarization_and_hj_preserved':True},
                'real_descent_degree_zero_fractional_ideal':real_ideals}
            comparisons[str(j)]={'original_global_y_gj':ysum,'original_comparison_function':principal,
                'uses_true_Galois_norm':True,'original_target_b_transformed_under_norm':True,
                'same_target_product_used':False,'no_original_nonzero_field_constant_discarded':True,
                'fractional_ideal_identity':'I_ZjR=R_j*I_Zj^3',
                'original_alpha3':'1-zeta^2','original_y_descent_denominator':'3*s*(y^2-b)',
                'original_c0_rigidification_evaluation_computed':False}
        g.check()
        value={'expression_language_version':1,'source_audit':self.ref(PREFIX+'source-audit'),
            'original_field':self.field,'normal_basis_source':r809.tag['original_graded_free_basis'],
            'field_model':'F=L(z)[T]/det(TI-W), T is the original w=e2/tau',
            'graph_nodes':g.nodes,'nonzero_proof_obligations':g.obligations,
            'global_unit_chart_nodes':{'F':fmatrix,'Z':zmat,'Y':ylaurent,'C':cmatrix,'M':mmatrix,'rhs':rhs,'solution':xi,
                'A_coefficients':avec,'C_coefficients':cvec,'B_coefficients':bvec},
            'global_function_nodes':{'A_over_tau5':a_b_in_field[0],'B_over_tau5':a_b_in_field[1],
                'original_y':global_y,'original_y_z_derivative':dy,'original_b':original_b,'original_y_squared_minus_b':ss},
            'original_global_derivative_nodes':{'W':w,'Krylov':krylov,'chi':characteristic},
            'original_Galois_automorphism_node':g.galois_definition,
            'relative_original_functions':relative,'original_base_pole_ideals':bases,
            'five_original_polar_and_eta_outputs':outputs,'original_principal_comparisons':comparisons,
            'all_three_minor_formulas_are_exact_DVR_ideal_equalities':True,
            'cube_of_ideal_equals_ideal_of_cubes_used_only_on_smooth_curve_DVRs':True,
            'finite_flat_mu3_descent_and_all_ramification_multiplicities_preserved':True,
            'both_original_affine_charts_share_same_field_functions':True,
            'base_chart_transition':self.pole['Ey_chart_transition'],
            'all_nonzero_conditions_use_original_proof_or_source_unit_witness':True,
            'global_y_exact_unit_expression_defined':True,
            'five_original_addition_pole_ideals_as_fractional_DAGs_certified':True,
            'original_eta_Picard_input_DAGs_defined':True,
            'original_comparison_function_DAGs_defined':True,
            'expanded_global_function_coordinates_computed':False,
            'normal_polynomial_ideal_lattices_materialized':False,
            'Jacobian_standard_representatives_computed':False,
            'original_rigidification_and_height_computed':False,
            'original_eta_classes_proved_zero':False,
            'old_1186_lift_global_W_or_six_C_coordinates_recomputed':False,
            'actual_graph_node_count':len(g.nodes),'actual_nonzero_proof_obligation_count':len(g.obligations)}
        return self.store(name,value)

    def inventory(self):
        rows=[]
        for path in sorted(self.out.glob(PREFIX+'*.json.gz')):
            if path.name==INVENTORY:continue
            value=read(path)
            assert value['configuration']==self.tag and value['complete'] is True
            rows.append(spec(path))
        save(self.out/INVENTORY,{'result':RESULT,'configuration':self.tag,'complete':True,'files':rows})
        return spec(self.out/INVENTORY)

    def finish(self,complete,error=None):
        graph=self.cached(PREFIX+'exact-global-function-and-five-polar-expression-DAG')
        assert complete==(graph is not None)
        value={'result':RESULT,'configuration':self.tag,'complete':complete,'p':41,
            'completed_scope':'original_global_function_and_five_polar_expression_DAGs' if complete else 'partial_source_expression_assembly',
            'global_y_exact_unit_expression_defined':complete,
            'five_original_addition_pole_ideals_as_fractional_DAGs_certified':complete,
            'original_eta_Picard_input_DAGs_defined':complete,
            'original_comparison_function_DAGs_defined':complete,
            'expanded_global_function_coordinates_computed':False,
            'normal_polynomial_ideal_lattices_materialized':False,
            'Jacobian_standard_representatives_computed':False,
            'original_rigidification_and_height_computed':False,
            'original_eta_classes_proved_zero':False,
            'old_mathematical_computations_repeated':False,
            'source_audit':self.ref(PREFIX+'source-audit'),
            'exact_expression_DAG':self.ref(PREFIX+'exact-global-function-and-five-polar-expression-DAG') if complete else None,
            'actual_graph_node_count':graph['actual_graph_node_count'] if complete else None,
            'stage_manifest':self.inventory(),'error':error,'seconds':time.monotonic()-self.started}
        save(self.out/FINAL,value);return value

    def run(self):
        prior=self.out/FINAL
        if prior.exists():
            value=read(prior);assert value['configuration']==self.tag
            if value['complete'] is True:
                assert self.cached(PREFIX+'exact-global-function-and-five-polar-expression-DAG') is not None
                return self.finish(True)
        self.graph();return self.finish(True)


def main():
    assert os.environ.get('GITHUB_ACTIONS') == 'true', 'New mathematics runs only in public GitHub Actions.'
    assert os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'
    parser=argparse.ArgumentParser();parser.add_argument('--config',required=True)
    parser.add_argument('--out',required=True);parser.add_argument('--budget-minutes',type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();job=None;code=1;error=None;final=None
    try:
        job=Job(args);final=job.run();code=0
    except BudgetStop as exc:
        error={'type':type(exc).__name__,'message':str(exc)};code=124
        if job is not None:final=job.finish(False,error)
    except BaseException as exc:
        error={'type':type(exc).__name__,'message':str(exc)}
        traceback.print_exc()
    receipt={'result':RESULT,'source_sha256':sha(__file__),'configuration':job.tag if job else None,
        'process_exit_code':code,'complete':bool(final and final['complete']),
        'certificate_sha256':sha(out/FINAL) if final is not None else None,
        'error':error,'seconds':time.monotonic()-started,
        'old_mathematical_computations_repeated':False,
        'original_rigidification_and_height_computed':False}
    save(out/'core-receipt.json',receipt)
    print(json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)


if __name__=='__main__':main()
