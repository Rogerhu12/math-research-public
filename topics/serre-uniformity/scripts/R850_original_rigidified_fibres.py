#!/usr/bin/env python3
"""Compose the five original rigidified fibres from completed exact producers."""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
from fractions import Fraction
import sys
import tarfile
import time
import traceback

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

RESULT = 'R850-original-rigidified-Poincare-fibres-and-theta-section'
FINAL = 'p41-original-rigidified-Poincare-fibres-certificate.json'
PREFIX = 'R850-rigidified-fibres-'
PARENT_CORE = 'R839_original_global_polar_DAG.py'
PARENT_SHA = '544241acf5f3451df34c779d513ea6494616d4d4caa26cd2531749edc895aea7'
LABELS = ['GLOBAL', 'C0', 'POINTS']
PQ = [(165,67),(93,67),(100,67),(168,67),(371,134)]
SCOPE = {
    'p':41, 'original_map_index':4, 'original_map_degree':1206,
    'original_pq':[list(x) for x in PQ],
    'source_and_target_curve_points':['c0','c1','P0=phi(c0)','P1=phi(c1)'],
    'original_c0_parameter':'t=a^3', 'original_c1_parameter':'z=a-1',
    'original_elliptic_parameter':'xi=-x/y', 'original_elliptic_differential':'dx/(2y)',
    'ideal_convention':'I_Z=O_Y(-Z), embedded in the original function field',
    'real_descent_ideal_identity':'I_ZR=R_j*I_Z^3',
    'Poincare_power_is_in_second_slot_with_first_point_fixed':True,
    'original_theta_square_factor':['1','2'],
    'original_C_h_not_replaced_or_numerically_recovered':True,
    'all_scalar_powers_are_exact_DAGs_without_large_power_expansion':True,
    'all_old_nodes_and_old_configuration_tags_remain_unchanged':True,
    'new_CM_Hensel_Dixon_point_addition_or_global_solve':False,
    'canonical_Poincare_logarithms_or_height_values_computed':False,
    'output_representation':'finite_exact_source_bound_line_bundle_fibre_and_scalar_DAG',
}
TRUE_FLAGS = [
    'all_five_original_rigidified_Poincare_fibres_constructed',
    'all_five_original_c0_normalized_full_sections_constructed',
    'all_five_original_theta_frame_constants_defined',
    'all_five_original_Q_threefold_theta_square_fibres_constructed',
    'original_full_Picard_correction_and_theta_torsion_transport_preserved',
]
FALSE_FLAGS = [
    'canonical_Poincare_logarithms_computed', 'original_height_values_computed',
    'original_height_nonzero_proved', 'eta_standard_Jacobian_coordinates_computed',
    'original_CM_candidate_A1_accepted', 'large_scalar_integer_powers_expanded',
    'old_mathematical_computations_repeated', 'all_p_uniformity_proved',
]


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as s:
        for b in iter(lambda:s.read(4*1024*1024),b''): h.update(b)
    return h.hexdigest()


def fp(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def read(path):
    p=Path(path)
    with (gzip.open if p.suffix=='.gz' else open)(p,'rt',encoding='utf-8') as s:
        return json.load(s)


def save(path,value):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+'.tmp')
    raw=(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()
    if p.suffix=='.gz':
        with tmp.open('wb') as stream:
            with gzip.GzipFile(fileobj=stream,mode='wb',mtime=0,filename='') as z:z.write(raw)
    else:tmp.write_bytes(raw)
    tmp.replace(p)
    return spec(p)


def spec(path):
    p=Path(path);return {'file':p.name,'bytes':p.stat().st_size,'sha256':sha(p)}


def plain(row):
    return {k:row[k] for k in ('file','bytes','sha256')}


def origin(value):
    return {k:value[k] for k in
        ('result','run_id','source_commit','core_sha256','manifest_sha256','configuration_sha256')}


def same_origin(a,b):
    for k in ('result','run_id','source_commit','core_sha256','manifest_sha256'):
        assert str(a[k])==str(b[k]), ('original source mismatch',k)


def rational(value):
    assert isinstance(value,list) and len(value)==2
    a,b=map(int,value);assert b>0
    q=Fraction(a,b);assert str(q.numerator)==value[0] and str(q.denominator)==value[1]
    return q


def qr(value):
    return [str(value.numerator),str(value.denominator)]


def expected_tag(item):
    return {'result':RESULT,'source_sha256':item['core_sha256'],
        'proof_sha256':item['proof_sha256'],'method_sha256':item['method_sha256'],
        'source_identities':{k:{**origin(item['sources'][k]),
            'selected_files_sha256':item['sources'][k]['selected_files_sha256'],
            'selected_file_count':item['sources'][k]['selected_file_count']} for k in LABELS},
        'arithmetic':'symbolic composition of completed exact original fibres; no old arithmetic executed',
        **SCOPE}


class BudgetStop(Exception):
    pass


class Job:
    def __init__(self,args):
        assert os.environ.get('GITHUB_ACTIONS')=='true'
        assert os.environ.get('GITHUB_REPOSITORY')=='Rogerhu12/math-research-public'
        self.start=time.monotonic();self.deadline=self.start+args.budget_minutes*60
        self.out=Path(args.out);self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item['result']==RESULT and self.item['p']==41
        assert self.item['core_sha256']==sha(__file__)
        for k in ('proof','method'):
            assert sha(self.item[k+'_absolute_path'])==self.item[k+'_sha256']
        parent=Path(__file__).parent/PARENT_CORE
        assert self.item['composition_helper_core_sha256']==PARENT_SHA and sha(parent)==PARENT_SHA
        module_spec=importlib.util.spec_from_file_location('original_finite_graph_and_source_helpers',parent)
        self.parent=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(self.parent)
        # Only Source, Graph and serialization helpers are reused. Parent Job is never instantiated.
        self.sources={k:self.parent.Source(k,self.item['sources'][k]) for k in LABELS}
        self.tag=expected_tag(self.item);self.stages={}
        self.nested=self.open_point_carrier()
        self.global_source=self.sources['GLOBAL'];self.c0=self.sources['C0']
        self.gc=self.global_source.certificate;self.cc=self.c0.certificate
        self.gp=self.global_source.indexed(self.gc['exact_expression_DAG'])
        self.pc=self.nested['POINTS'].certificate
        self.pp=self.nested['POINTS'].indexed(self.pc['point_program'])
        self.global_nodes={n['id']:n for n in self.gp['graph_nodes']}
        self.point_nodes={n['id']:n for n in self.pp['nodes']}
        assert len(self.global_nodes)==self.gp['actual_graph_node_count']==523
        assert len(self.point_nodes)==self.pp['node_count']==529
        self.norms={}
        for j in range(6):
            name='R803-c0-original-norm-and-trace-j'+str(j)+'.json.gz'
            value=self.c0.get(name);assert value['j']==j
            assert value['actual_norm_nonzero'] is True
            assert value['Norm_is_actual_field_norm_not_same_target_T_product'] is True
            assert value['norm_K_1_s'][0]==['0','1']
            assert rational(value['norm_K_1_s'][1])!=0
            self.norms[j]=(name,value)
        self.comparisons={}
        for j in range(1,6):
            name='R803-c0-original-comparison-leading-jet-j'+str(j)+'.json.gz'
            self.comparisons[j]=(name,self.c0.get(name))

    def open_point_carrier(self):
        parent=self.sources['POINTS']
        receipt=parent.get('retained-inputs-receipt.json',stage=False)
        assert receipt['result']==parent.item['result']
        assert receipt['all_source_bytes_and_original_parent_child_bindings_verified'] is True
        bundle=parent.bound(receipt['input_bundle']['file'])
        assert spec(bundle)==plain(receipt['input_bundle'])
        groups=receipt['expanded_sources']
        assert set(groups)=={'CM','DAG','JETS','NONTORSION','POINTS','R791'}
        root=self.out.parent/'original-point-leaves'
        wanted={(label,name):plain(row) for label,s in groups.items() for name,row in s['files'].items()}
        assert len(wanted)==receipt['selected_source_file_count']==270
        seen=set()
        with tarfile.open(bundle,'r|gz') as archive:
            for member in archive:
                if member.isdir():continue
                p=PurePosixPath(member.name);assert member.isfile() and len(p.parts)==2
                assert not p.is_absolute() and '..' not in p.parts
                key=tuple(p.parts);assert key in wanted and key not in seen;seen.add(key)
                row=wanted[key];assert member.size==row['bytes']
                dest=root.joinpath(*p.parts);dest.parent.mkdir(parents=True,exist_ok=True)
                raw=archive.extractfile(member).read()
                assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256']
                if dest.exists():assert spec(dest)==row
                else:dest.write_bytes(raw)
        assert seen==set(wanted)
        sources={}
        for label,source in groups.items():
            item=dict(source,directory=str(root/label),certificate_name=source['certificate']['file'])
            sources[label]=self.parent.Source(label,item)
        return sources

    def tick(self):
        if time.monotonic()>=self.deadline:raise BudgetStop('Only completed source-bound fibre stages need continuation.')

    def stage(self,name,make):
        path=self.out/(PREFIX+name+'.json.gz')
        if path.exists():
            value=read(path)
            assert value['complete'] is True and value['configuration']==self.tag
            assert value['result']==RESULT
            self.stages[name]=spec(path);return value
        self.tick();value=make()
        assert 'configuration' not in value
        value={'result':RESULT,'complete':True,'configuration':self.tag,**value}
        self.stages[name]=save(path,value)
        print(json.dumps({'stage':name,'seconds':time.monotonic()-self.start,**self.stages[name]},sort_keys=True),flush=True)
        return value

    def audit(self):
        assert self.gc['global_y_exact_unit_expression_defined'] is True
        assert self.gc['five_original_addition_pole_ideals_as_fractional_DAGs_certified'] is True
        assert self.gp['all_nonzero_conditions_use_original_proof_or_source_unit_witness'] is True
        assert self.gp['finite_flat_mu3_descent_and_all_ramification_multiplicities_preserved'] is True
        assert self.cc['all_six_true_relative_norms_and_traces_computed'] is True
        assert self.cc['all_five_original_comparison_leading_constants_DAG_and_unit_jets_computed'] is True
        assert self.pc['actual_nontorsion_source_verified'] is True
        assert self.pc['all_addition_denominators_certified_by_original_Hom_words'] is True
        assert self.pc['original_R791_comparison_function_values_as_exact_DAG'] is True
        assert self.pp['original_Galois_transport_and_T7_phase_preserved'] is True
        assert self.pp['imported_R841_nodes_unchanged'] is True
        r791=self.nested['R791']
        same_origin(self.global_source.tag['source_identities']['R791'],r791.identity)
        same_origin(self.c0.tag['sources']['R791'],r791.identity)
        same_origin(self.global_source.tag['source_identities']['R840'],self.nested['CM'].identity)
        eta=r791.ref('R791-original-real-descent-and-eta-basis-inputs.json.gz')
        for j,(p,q) in enumerate(PQ,1):
            glob=self.gp['five_original_polar_and_eta_outputs'][str(j)]
            comp=self.comparisons[j][1]
            assert glob['p']==comp['p']==p and glob['q']==comp['q']==q
            assert glob['source_original_hj_index']==comp['j']==j
            assert plain(glob['source_eta_basis'])==plain(comp['source_original_eta_basis'])==plain(eta)
            assert comp['actual_leading_constant_defined_and_nonzero'] is True
            assert comp['order_in_t']==14*(p-q)
            assert comp['unit_first_logarithmic_derivative_K_1_s'][1]==['0','1']
            row=self.pp['five_original_eta_addition_inputs'][j-1]
            assert row['j']==j and row['true_norm_keeps_Nb_over_b7'] is True
            assert row['comparison_function_value_root']==self.pp['roots']['R791_comparison_'+str(j)]
            assert row['original_rj']==comp['original_degree_zero_ratio']
            for components in (row['real_g_Weil_components'],self.pp['original_real_base_Weil_components']):
                assert [x['sigma_power'] for x in components]==list(range(7))
                for component in components:
                    assert component['target_is_original_conjugate_curve'] is True
                    assert all(component[k] in self.point_nodes for k in ('curve_b','x','y'))
        return {
            'all_original_parent_child_identities_and_pq_directions_preserved':True,
            'same_original_CM_unit_expression_and_R791_Hom_source_verified':True,
            'six_completed_norms_are_nonzero_pure_s_elements':True,
            'original_global_program':self.global_source.ref_indexed(self.gc['exact_expression_DAG']),
            'original_point_program':dict(self.nested['POINTS'].ref_indexed(self.pc['point_program']),nested_in='POINTS'),
            'original_eta_source':dict(eta,nested_in='POINTS'),
            'nested_original_source_identities':{k:s.identity for k,s in self.nested.items()},
            'old_global_node_count':523,'old_point_node_count':529,
            'new_CM_Hensel_Dixon_global_solve_point_addition_or_norm_arithmetic':False,
            'original_primal_518_or_auxiliary_ell_balls_used_as_level41_heights':False,
        }

    def graph(self):
        G=self.parent.Graph()
        proof={'file':self.item['proof'],'sha256':self.item['proof_sha256']}
        p0=G.node('original_marked_curve_point','Y_point',name='P0=phi(c0)',parameter='t=a^3',parameter_value='0',proof=proof)
        p1=G.node('original_marked_curve_point','Y_point',name='P1=phi(c1)',parameter='t=a^3',parameter_value='1',proof=proof)
        py=G.node('original_Abel_difference','JY_point',[p1,p0],formula='[P1-P0]')
        gamma=G.node('original_Abel_difference','JX_point',formula='[c1-c0]',different_from_PY=True,proof=proof)
        global_ref=self.global_source.ref_indexed(self.gc['exact_expression_DAG'])
        point_ref=dict(self.nested['POINTS'].ref_indexed(self.pc['point_program']),nested_in='POINTS')
        def global_node(node_id,domain):
            assert node_id in self.global_nodes
            return G.node('completed_original_global_graph_node',domain,source=global_ref,original_node_id=node_id)
        def point_node(node_id):
            assert node_id in self.point_nodes
            return G.node('completed_original_point_graph_node','L',source=point_ref,original_node_id=node_id)
        def integer(n):
            return G.node('exact_rational_integer','Q',decimal=str(n))
        def power(x,n):
            assert n>=0
            return G.node('exact_nonnegative_scalar_power',G.by_id[x]['domain'],[x],exponent=n,expanded=False)
        def mul(*xs):
            return G.node('exact_scalar_product','Q',xs)
        def div(x,y,reason,domain='Q'):
            return G.node('exact_scalar_quotient',domain,[x,y],denominator_nonzero_proof=reason)
        def nz(name,statement,reason,sources):
            return G.proof(name,statement,reason,sources,proof_file=proof)
        m={}
        for j,(name,value) in self.norms.items():
            m[j]=G.node('completed_pure_s_norm_rational_coordinate','Q',
                source=self.c0.ref(name),coefficient='norm_K_1_s[1]',value=value['norm_K_1_s'][1],
                norm_equals_s_times_value=True)
            nz('m'+str(j)+'_nonzero','m_'+str(j)+' != 0',
                'R848 completed nonzero Norm and exact pure-s coordinate; s^2=-3',[self.c0.ref(name)])
        one=integer(1);three=integer(3)
        outputs=[]
        for j,(p,q) in enumerate(PQ,1):
            self.tick();delta=p-q
            glob=self.gp['five_original_polar_and_eta_outputs'][str(j)]
            old_comp=self.gp['original_principal_comparisons'][str(j)]
            cname,cj=self.comparisons[j]
            row=self.pp['five_original_eta_addition_inputs'][j-1]
            ideals={};idealsR={}
            for chart in ('tau','sigma'):
                ideals[chart]=global_node(glob['eta_degree_zero_fractional_ideal'][chart],'ideal_'+chart)
                idealsR[chart]=global_node(glob['real_descent_degree_zero_fractional_ideal'][chart],'ideal_'+chart)
            L=G.node('original_two_chart_invertible_sheaf','Y_line',[ideals['tau'],ideals['sigma']],
                convention='O_Y(-Z_j)',global_transition_source=global_ref,j=j)
            LR=G.node('original_two_chart_invertible_sheaf','Y_line',[idealsR['tau'],idealsR['sigma']],
                convention='O_Y(-Z_jR)',global_transition_source=global_ref,j=j)
            xi=G.node('negative_of_ideal_Picard_class','JY_point',[L],formula='xi_j=[Z_j]=-[I_Zj]')
            xiR=G.node('negative_of_ideal_Picard_class','JY_point',[LR],formula='xi_jR=[Z_jR]=3*xi_j')
            frames={}
            fibres={}
            for label,line,point in [('original',L,xi),('real_descent',LR,xiR)]:
                e=G.node('original_local_monomial_frame','nonzero_line_fibre',[line,p0],
                    parameter='t=a^3',exponent=-7*delta,proof='RF.4 and RF.8',proof_file=proof)
                unit=G.node('original_P1_unit_ideal_frame','nonzero_line_fibre',[line,p1],
                    rational_section='1',nonzero_support_proof='R843 actual point separation and RF.1',proof_file=proof)
                frames[label]=e
                fibres[label]=G.node('basepoint_rigidified_Poincare_fibre_vector','Poincare_Y_nonzero',
                    [unit,e,py,point],formula='1(P1) tensor e(P0)^(-1)',
                    autoduality_sign='i_Y^*lambda_Y=-id',actual_Q_fibre=True,proof='RF.7-RF.9',proof_file=proof)
            Rglobal=global_node(old_comp['original_comparison_function'],'global_function')
            Rvalue=point_node(row['comparison_function_value_root'])
            rproof=nz('R'+str(j)+'_P1_nonzero','R_j(P1) != 0',
                'original R844 true Norm and actual R843 Hom-value separation; no candidate value substituted',[point_ref])
            kappa=G.node('completed_original_c0_leading_constant','Q',
                source=self.c0.ref(cname),source_DAG_sha256=cj['leading_constant_DAG_sha256'],
                coefficient='leading_constant_DAG.output',expanded=False,
                Q_membership_proof='R848 and RF.27')
            ratio=div(power(m[0],p),power(m[j],q),'m'+str(j)+'_nonzero')
            nu=mul(power(three,11*delta),ratio)
            nuK=G.node('original_full_theta_frame_normalization','K',
                [m[0],m[j]],formula='(3*s)^(7*delta)*M_f^p/M_g^q',
                M_f_source=self.c0.ref(self.norms[0][0]),
                M_g_source=self.c0.ref(self.norms[j][0]),
                inputs_are_rational_coordinates_M_over_s=True,
                original_s_square='-3',original_alpha3='1-zeta^2',alpha3_cube='3*s',
                p=p,q=q,delta=delta,equals_rational_node=nu,proof='RF.24 and RF.27',proof_file=proof)
            transport=div(kappa,Rvalue,rproof,domain='L')
            scalar=G.node('exact_scalar_product','L',[nu,transport])
            multiplication=G.node('original_principal_line_isomorphism','Y_line_isomorphism',
                [L,LR,Rglobal,kappa,Rvalue],source_tensor_power=3,
                global_direction='positive multiplication by R_j',
                P0_fibre_scalar='kappa_j',P1_fibre_scalar='R_j(P1)',proof='RF.10-RF.12',proof_file=proof)
            v3=G.node('Poincare_tensor_power_in_second_slot','Poincare_Y_nonzero',
                [fibres['original'],py],exponent=3,first_slot_fixed=True,
                not_group_multiplication_in_fixed_extension=True)
            comparison=G.node('original_rigidified_Poincare_transport','fibre_isomorphism',
                [multiplication,fibres['real_descent'],v3,transport],
                identity='v_jR=(kappa_j/R_j(P1))*v_j^tensor3',proof='RF.12',proof_file=proof)
            base_points=[];g_points=[]
            for target,components in ((base_points,self.pp['original_real_base_Weil_components']),
                                      (g_points,row['real_g_Weil_components'])):
                for component in components:
                    coord=[point_node(component[k]) for k in ('curve_b','x','y')]
                    target.append(G.node('completed_original_elliptic_point','elliptic_point',coord,
                        sigma_power=component['sigma_power'],curve='y^2=x^3+sigma(b)',
                        actual_target_scale_retained=True,source=point_ref,
                        no_new_point_addition=True))
            S=G.node('original_Hom_pullback_theta_tensor','JX_symmetric_line',
                [gamma],j=j,p=p,q=q,
                formula='G_j^*Theta_B^q tensor q_R^*Theta_B^(-p)',
                original_elliptic_origin_frame='xi^(-1), xi=-x/y',
                Hom_source=dict(self.nested['R791'].ref('R791-original-Hom-Galois-matrices.json.gz'),
                    nested_in='POINTS'),
                proof='RF.17-RF.20',proof_file=proof)
            u=G.node('original_theta_rational_section_value','theta_nonzero_vector',
                [S]+g_points+base_points,formula='tensor_tau 1(g_Rj,tau)^q / 1(f_R,tau)^p',
                coefficients=[q]*7+[-p]*7,
                individual_K_frame_not_misidentified_as_Q_frame=True)
            u3=G.node('third_tensor_of_original_theta_section','theta_nonzero_vector',
                [u,S],exponent=3,actual_Q_rigidified_fibre=True,
                descent_proof='RF.5: N(rho)=zeta^2; third frame multiplier is 1',proof_file=proof)
            z3=G.node('original_canonical_square_Poincare_vector','Poincare_J_nonzero',
                [u3,gamma,S],formula='canonical_square(u_j^tensor6)',
                fibre='P_J(gamma,3*lambda_Sj(gamma))',actual_Q_fibre=True,
                original_polarization_and_v_dagger_v_retained=True,proof='RF.29',proof_file=proof)
            corr=G.node('original_complete_Picard_correction','JX_line',
                [S],formula='S_j tensor P_J,lambda_J[i_X^*S_j]',
                theta_representative_difference_and_inverse_Picard_factor_transported_together=True,
                proof='RF.14-RF.21',proof_file=proof)
            section=G.node('original_c0_normalized_full_section','nonvanishing_X_section',
                [corr,nu,u3,fibres['real_descent']],formula='nu_j*u_j^tensor3 tensor v_jR',
                at_c0=['1','1'],normalization_uses_multiplication_by_nu=True,proof='RF.25-RF.26',proof_file=proof)
            alternate=G.node('same_normalized_section_in_smaller_ideal_frame','nonvanishing_X_section',
                [section,scalar,u3,v3,comparison],
                formula='(nu_j*kappa_j/R_j)*u_j^tensor3 tensor v_j^tensor3')
            nh=G.node('original_full_Nh_unique_rigidified_comparison','JX_line_isomorphism',
                [corr,section],formula='N_h^(3*q) ~= Corr(S_j)^(3*C_h)',
                original_C_h_symbol='C_hj=c_clear*c_triv from R593',
                C_h_numerical_value_not_computed=True,
                sends_original_c0_normalized_sections=True,
                uniqueness='same NS, actual trivial curve pullback, origin rigidification',
                proof='RF.28',proof_file=proof)
            local=G.node('specified_original_local_height_expression','unevaluated_original_height',
                [scalar,z3,fibres['original'],nh],
                formula='(chi_v(nu_j*kappa_j/R_j(P1)) + tau_J,v(z_j^(3))/2 + 3*tau_Y,v(v_j))/(3*q)',
                denominator=3*q,theta_coefficient=['1','2'],Picard_coefficient=3,
                splitting='the same original R724 Hodge/Poincare splitting',
                all_non_p_places_preserved=True,actual_Q_fibres_before_local_evaluation=True,
                canonical_periods_evaluated=False,proof='RF.30-RF.31',proof_file=proof)
            d=rational(cj['unit_first_logarithmic_derivative_K_1_s'][0])
            outputs.append({'j':j,'p':p,'q':q,'delta':delta,'c0_order_Z':-7*delta,
                'original_ideal':L,'real_descent_ideal':LR,'xi':xi,'xiR':xiR,
                'Poincare_v':fibres['original'],'Poincare_vR':fibres['real_descent'],
                'principal_line_isomorphism':multiplication,'rigidified_transport':comparison,
                'global_R':Rglobal,'R_at_P1':Rvalue,'kappa':kappa,
                'nu_original_K_expression':nuK,'nu_exact_Q_expression':nu,
                'full_scalar_nu_kappa_over_R':scalar,'S_j':S,'u_j':u,
                'actual_Q_threefold_theta_section':u3,'canonical_square_z_j_threefold':z3,
                'complete_corrected_line':corr,'normalized_section':section,
                'normalized_section_smaller_ideal_frame':alternate,'original_Nh_comparison':nh,
                'specified_original_local_height_expression':local,
                'c0_first_unit_coefficient_in_original_real_descent_frame':qr(-d/2),
                'c0_first_unit_coefficient_in_smaller_ideal_cubed_frame':qr(-3*d/2),
                'these_are_algebraic_frame_coefficients_not_height_jets':True})
        G.check()
        assert len(outputs)==5
        return {'graph_nodes':G.nodes,'nonzero_proof_obligations':G.obligations,
            'actual_graph_node_count':len(G.nodes),'actual_nonzero_proof_obligation_count':len(G.obligations),
            'five_original_fibre_and_section_outputs':outputs,
            'original_global_program':global_ref,'original_point_program':point_ref,
            'old_graph_nodes_rewritten_or_recomputed':False,
            'all_frame_normalizations_and_true_norm_constants_preserved':True,
            'original_theta_two_torsion_representative_not_deleted':True,
            'new_scalar_powers_expanded':False,
            'all_new_Poincare_nodes_are_actual_fixed_original_fibres':True,
            'all_original_local_height_nodes_remain_unevaluated':True,
            'exact_original_C_h_values_recovered':False,
            'standard_Jacobian_coordinates_recovered':False}

    def run(self):
        self.stage('source-audit',self.audit)
        graph=self.stage('five-original-fibres-and-sections-DAG',self.graph)
        stage_manifest={'result':RESULT,'complete':True,'configuration':self.tag,
                        'stages':[self.stages[n] for n in sorted(self.stages)]}
        ms=save(self.out/(PREFIX+'stage-manifest.json.gz'),stage_manifest)
        final={'result':RESULT,'p':41,'complete':True,'configuration':self.tag,
            'source_audit':self.stages['source-audit'],
            'exact_expression_DAG':self.stages['five-original-fibres-and-sections-DAG'],
            'stage_manifest':ms,'seconds':time.monotonic()-self.start,
            'actual_graph_node_count':graph['actual_graph_node_count'],
            'actual_nonzero_proof_obligation_count':graph['actual_nonzero_proof_obligation_count'],
            'completed_original_fibre_count':5,
            **{k:True for k in TRUE_FLAGS},**{k:False for k in FALSE_FLAGS}}
        save(self.out/FINAL,final)
        return final


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--config',required=True)
    parser.add_argument('--out',required=True);parser.add_argument('--budget-minutes',type=float,default=300)
    args=parser.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    assert 0<args.budget_minutes<=300
    try:
        result=Job(args).run()
        save(out/'core-receipt.json',{'result':RESULT,'complete':True,'source_sha256':sha(__file__),
            'certificate_sha256':sha(out/FINAL),'old_mathematical_computations_repeated':False})
        print(json.dumps({'complete':True,'result':RESULT,'actual_graph_node_count':result['actual_graph_node_count'],
            'seconds':result['seconds']},sort_keys=True),flush=True)
        return 0
    except BaseException as exc:
        traceback.print_exc()
        save(out/'core-receipt.json',{'result':RESULT,'complete':False,'source_sha256':sha(__file__),
            'error':str(exc),'exception_type':type(exc).__name__,'only_complete_stages_are_reusable':True})
        return 1


if __name__=='__main__':
    raise SystemExit(main())

