#!/usr/bin/env python3
"""Complete planned fixed-reference node packets and outward four-jet fees.

The complete material/integration query plan is retained. Missing actual
means or accurate fees remain pending, never zero. All raw four-jet words,
outward error carriers and immutable proof-input snapshots stay on the
runner. This pays the fixed reference at literal nodes, not continuous
angles, outer normal controls, calibration, physical F or reach.
"""
import argparse
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

SCHEMA = 'complete-material-envelope-reference-node-four-jet-fees-v1'
FEE_SCHEMA = 'immutable-complete-reference-node-four-jet-error-packet-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
INPUT_SOURCE = 'material_envelope_reference_node_inputs.py'
INPUT_SHA = '80744e058f95e4d91192b74c9a01c2ed9018858a15b5c8fd83d3b960069e62eb'
FIELD_KEYS = ('T','Tp','Tpp','Ts')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('All complete node arithmetic requires public repository Actions')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def load_inputs(repo):
    path=Path(repo)/TOPIC/'scripts/resume_20261126'/INPUT_SOURCE
    if sha(path)!=INPUT_SHA:
        raise ValueError('Use the complete declared immutable input producer')
    spec=importlib.util.spec_from_file_location('_complete_envelope_node_inputs',path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    if sha(module.BoundReferenceInputs.__init__.__code__.co_filename)!=INPUT_SHA:
        raise ValueError('The actual complete node input body changed')
    return module


def event(**value):
    print(json.dumps(value,separators=(',',':'),allow_nan=False),flush=True)


def upper_binary64(value):
    """A checked outward carrier; conversion is not assumed correctly rounded."""
    value=F(value)
    if value<0:
        raise ValueError('A norm error bound must be nonnegative')
    carrier=float(value)
    if not math.isfinite(carrier):
        raise OverflowError('The accurate error has no finite binary64 upper carrier')
    while F(carrier)<value:
        carrier=math.nextafter(carrier,math.inf)
        if not math.isfinite(carrier):
            raise OverflowError('The accurate error has no finite binary64 upper carrier')
    return carrier


def capture_snapshot(module,path,directory,expected=None):
    path=Path(path).resolve()
    output_root=Path(directory).resolve().parent
    if path==output_root or output_root in path.parents:
        raise ValueError('The complete output subtree must be disjoint from every accurate-fee input')
    value,record=module.capture(path,expected)
    destination=directory/(record['sha256']+'.json')
    if destination.exists():
        snapshot=module.file_record(destination)
        if snapshot['sha256']!=record['sha256'] or snapshot['bytes']!=record['bytes']:
            raise ValueError('An immutable actual input snapshot was changed')
    else:
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()!=record['sha256'] or len(data)!=record['bytes']:
            raise ValueError('The source changed before its immutable snapshot was saved')
        destination.parent.mkdir(parents=True,exist_ok=True)
        with destination.open('xb') as stream:
            stream.write(data)
        snapshot=module.file_record(destination)
    if module.file_record(path)!=record:
        raise ValueError('The source changed while its immutable input snapshot was saved')
    return value,dict(original_record=record,immutable_snapshot=snapshot)


class MeanFeeInputs:
    """All available original-order accurate batch results; no new mean roots."""
    def __init__(self,inputs,directory,path):
        self.inputs=inputs
        self.module=inputs.modules['schedule']
        self.utility=inputs.modules['accurate']
        self.m=inputs.modules['fees']
        self.by_angle={}
        self.original_records=[]
        self.snapshots=[]
        self.pending_batches=[]
        self.directory=Path(directory)
        helper=sys.modules['_complete_envelope_node_inputs']
        self.helper=helper
        value,snapshot=capture_snapshot(helper,path,self.directory)
        self.original_records.append(snapshot['original_record'])
        self.snapshots.append(snapshot)
        if value.get('source_sha256')!=helper.PINS['schedule'][1] or value.get('schema')!=self.module.SCHEMA:
            raise ValueError('Use the actual complete published mean-fee schedule')
        binding=value['binding']
        if value.get('binding_identity_sha256')!=canonical(binding):
            raise ValueError('The complete accurate mean-fee binding changed')
        for key in ('actual_report','actual_driver_sha256','actual_model_identity_sha256',
                'fixed_scalar_metric_identity_sha256','supported_unit_seed_identity_sha256',
                'complete_seed_model','complete_input_records','actual_all_batch_metadata_sha256',
                'actual_recorded_completed_batches','actual_recorded_literal_angles',
                'complete_ordered_literal_angle_words_sha256','schedule'):
            if binding.get(key)!=inputs.recorded.get(key):
                raise ValueError('The accurate fee schedule names another complete actual input: '+key)
        if len(value['batches'])!=len(inputs.recorded['schedule']):
            raise ValueError('Do not select a subset of actual recorded mean batches')
        for index,row in enumerate(value['batches']):
            if row.get('batch_index')!=index:
                raise ValueError('Keep the original complete actual mean batch order')
            producer=row.get('producer')
            if producer is None or producer.get('complete') is not True or producer.get('fee_request') is None:
                self.pending_batches.append(dict(batch_index=index,reason='complete accurate mean integral cover/request not yet present'))
                continue
            pvalue,psnapshot=capture_snapshot(helper,producer['report']['path'],self.directory,producer['report'])
            self.module.validate_producer(pvalue,binding,index)
            if pvalue.get('complete') is not True:
                raise ValueError('A complete producer record changed its actual completion state')
            request_record=pvalue.get('fee_request')
            if request_record!=producer['fee_request']:
                raise ValueError('The complete current accurate request changed')
            request,rsnapshot=capture_snapshot(helper,request_record['path'],self.directory,request_record)
            self.original_records.extend((psnapshot['original_record'],rsnapshot['original_record']))
            self.snapshots.extend((psnapshot,rsnapshot))
            candidates=[v for v in row.get('consumers',[]) if v.get('fee_request_sha256')==request_record['sha256']]
            if not candidates:
                self.pending_batches.append(dict(batch_index=index,reason='matching complete-source mean/profile consumption not yet present'))
                continue
            saved=candidates[-1]
            consumer,csnapshot=capture_snapshot(helper,saved['report']['path'],self.directory,saved['report'])
            self.original_records.append(csnapshot['original_record']);self.snapshots.append(csnapshot)
            self.module.validate_consumer(consumer,binding,index,request_record['sha256'])
            expected=binding['schedule'][index]['actual_complete_batch_metadata']['literal_angle_hex']
            results=consumer.get('results',[])
            if (consumer.get('complete_seed_model')!=inputs.seed
                    or consumer.get('actual_completed_angles')!=len(results)
                    or [v['literal_phi_hex'] for v in results]!=expected[:len(results)]
                    or len(results)>len(expected)
                    or consumer.get('precision_bits')!=inputs.args.precision_bits
                    or consumer.get('taylor_order')!=inputs.args.taylor_order
                    or consumer.get('profile_series_order')!=inputs.args.profile_series_order):
                raise ValueError('The actual complete/prefix mean result or arithmetic parameters changed')
            if (request.get('schema')!=self.m.REQUEST_SCHEMA
                    or request.get('binding')!=consumer['binding']
                    or request.get('binding')!=pvalue['binding']['actual_batch']
                    or [v['literal_phi_hex'] for v in request['angles']]!=expected
                    or request.get('external_fee_provenance')!=consumer['external_fee_provenance']):
                raise ValueError('Retain the entire accurate mean request and its real external producer')
            external=request['external_fee_provenance']
            if (pvalue.get('binding_identity_sha256')!=canonical(pvalue['binding'])
                    or pvalue['binding']['complete_input_records']!=inputs.recorded['complete_input_records']
                    or pvalue['binding']['complete_seed_model']!=inputs.seed
                    or external.get('source_sha256')!=helper.PINS['accurate'][1]
                    or external.get('report_source_schema')!=self.utility.SCHEMA
                    or external.get('accurate_mean_binding_identity_sha256')!=pvalue['binding_identity_sha256']
                    or external.get('complete_journal_sha256')!=pvalue['journal']['sha256']
                    or external.get('complete_journal_chain_sha256')!=pvalue['journal_chain_sha256']
                    or external.get('complete_reference_identity_sha256')!=inputs.context.identity
                    or external.get('exact_reference_unit_and_nonnegative_vertical_law')!=self.utility.REFERENCE_UNIT_LAW
                    or external.get('exact_all_radial_pieces_and_infinite_tail_retained') is not True
                    or external.get('actual_working_scalar_quadrature_or_libm_errors_assumed_zero') is not False
                    or external.get('current_outer_field_or_geometry_certified') is not False):
                raise ValueError('The accurate input request is not closed to its complete radial producer')
            for item in results:
                word=item['literal_phi_hex']
                recorded=inputs.mean_by_angle[word]
                actual_words=dict(recorded['actual_words'],literal_phi_hex=word)
                if (item.get('complete') is not True or item.get('actual_working_words')!=actual_words
                        or item.get('requested_nodes')!=[]):
                    raise ValueError('Use the actual completed mean/profile result, not a relabelled node result')
                mean=self.decode_mean(item['mean'],word)
                provenance=dict(actual_batch_index=index,literal_phi_hex=word,
                    complete_accurate_producer_snapshot=psnapshot,
                    complete_fee_request_snapshot=rsnapshot,
                    complete_mean_profile_consumer_snapshot=csnapshot,
                    accurate_mean_result_sha256=canonical(item),
                    result_is_an_actual_complete_original_order_prefix=consumer.get('complete') is not True)
                self.by_angle[word]=dict(mean=mean,provenance=provenance)
            if len(results)<len(expected):
                self.pending_batches.append(dict(batch_index=index,reason='accurate mean/profile result incomplete',
                    completed_angles=len(results),required_angles=len(expected)))
        self.record=dict(actual_schedule_snapshot=self.snapshots[0],
            available_accurate_literal_angles=len(self.by_angle),pending_batches=self.pending_batches,
            no_missing_mean_fee_defaulted_to_zero=True,
            complete_actual_mean_batches_retained=True,
            immutable_input_snapshots=self.snapshots)
        self.recheck()

    def decode_mean(self,value,word):
        k=self.m
        if (value['seed_model_identity_sha256']!=self.inputs.seed_identity
                or value['literal_phi_hex']!=word or value['provider_sha256']!=k.PROVIDER_SHA
                or value['precision_bits']!=self.inputs.args.precision_bits
                or value['taylor_order']!=self.inputs.args.taylor_order
                or value['profile_series_order']!=self.inputs.args.profile_series_order
                or value.get('central_profile_moment_errors_certified_by_this_module') is not True
                or value.get('continuous_uniform_field_certificate') is not False):
            raise ValueError('The completed accurate mean jet has a different identity/scope')
        bits=value['precision_bits']
        intervals={key:(k.vector_box(row,bits) if key in k.MEAN_VECTOR_KEYS else k.box(row,bits))
            for key,row in value['intervals'].items()}
        expected=set(k.MEAN_VECTOR_KEYS)|{'lambda','lambda_phi','lambda_phiphi'}
        if set(intervals)!=expected:
            raise ValueError('Keep every accurate mean and amplitude jet')
        length=copy.deepcopy(value['length_bounds'])
        length['relative_central_intervals']=[[F(v) for v in pair] for pair in length['relative_central_intervals']]
        length['profile_delta']=F(length['profile_delta'])
        return dict(seed_model_identity_sha256=value['seed_model_identity_sha256'],literal_phi_hex=word,
            provider_sha256=value['provider_sha256'],intervals=intervals,length_bounds=length,
            accurate_S_interval=k.box(value['accurate_S_interval'],bits),
            accurate_root_vertical_lower=F(value['accurate_root_vertical_lower']),
            precision_bits=bits,taylor_order=value['taylor_order'],profile_series_order=value['profile_series_order'])

    def recheck(self):
        for record in self.original_records:
            if self.helper.file_record(record['path'])!=record:
                raise ValueError('An actual accurate-fee input changed during this invocation')
        for item in self.snapshots:
            if self.helper.file_record(item['immutable_snapshot']['path'])!=item['immutable_snapshot']:
                raise ValueError('An immutable accurate-fee snapshot changed')


class AccurateNodeBounds:
    """Whole exact affine-point law and all possible supported branches."""
    def __init__(self,inputs):
        if inputs.actual is None:
            raise ValueError('No actual completed mean batch supplies this exact reference context')
        self.inputs=inputs;self.actual=inputs.actual;self.k=self.actual.k
        self.source_sha256=sha(__file__)
        self.bits=inputs.args.precision_bits
        self.radial={};self.charts={}
        self.counts=dict(accurate_scalar_point_enclosures=0,accurate_chart_enclosures=0,
            complete_node_bounds=0,possible_supported_branches=0,multiple_branch_nodes=0)

    def radial_input(self,cell,word):
        key=(cell,word)
        if key not in self.radial:
            point=self.inputs.exact_point(cell,word)
            raw,pieces=self.actual.scalar.enclose(point,point)
            boxes=[self.actual.from_deep(v) for v in raw]
            if len(boxes)!=4:
                raise ValueError('The complete accurate scalar law must provide b,c,bs,cs')
            boxes[0]=boxes[0].intersect(-1,1);boxes[1]=boxes[1].intersect(0,1)
            exact_s=self.actual.from_deep(self.actual.scalar.exact_affine_box(point))
            relative=self.actual.relative_box(point,point).intersect(0,1)
            branches=[]
            cursor=F(0)
            for index,((left,right),(ca,cb)) in enumerate(zip(self.actual.support,self.actual.central)):
                candidates=(('outside',None,cursor,left),('boundary_left',index,left,ca),
                    ('central',index,ca,cb),('boundary_right',index,cb,right))
                for kind,which,a,b in candidates:
                    lo,hi=max(relative.lo,a),min(relative.hi,b)
                    if lo<=hi:
                        branches.append(dict(kind=kind,index=which,relative=self.k.Interval(lo,hi,self.bits)))
                cursor=right
            lo,hi=max(relative.lo,cursor),min(relative.hi,F(1))
            if lo<=hi:
                branches.append(dict(kind='outside',index=None,relative=self.k.Interval(lo,hi,self.bits)))
            if not branches:
                raise ValueError('The complete accurate supported partition omitted the exact material point')
            self.radial[key]=dict(exact_affine=[str(v) for v in point],exact_s=exact_s,
                exact_relative=relative,scalar=boxes,scalar_piece_scope=pieces,branches=branches)
            self.counts['accurate_scalar_point_enclosures']+=1
        return self.radial[key]

    def chart(self,word):
        if word not in self.charts:
            self.charts[word]=self.actual.chart(word)
            self.counts['accurate_chart_enclosures']+=1
        return self.charts[word]

    def cutoff(self,relative,kind,index):
        a,b=self.actual.support[index]
        xi=((relative-a)/self.actual.delta if kind=='boundary_left'
            else (b-relative)/self.actual.delta).intersect(0,1)
        def S5(v):return v**3*(10-15*v+6*v*v)
        def derivative(v):return 30*v*v*(1-v)*(1-v)
        chi=self.k.Interval(S5(xi.lo),S5(xi.hi),self.bits).intersect(0,1)
        extrema=[derivative(xi.lo),derivative(xi.hi)]
        if xi.lo<=F(1,2)<=xi.hi:extrema.append(F(15,8))
        chis=self.k.Interval(min(extrema),max(extrema),self.bits)/(self.actual.delta*self.actual.S)
        if kind=='boundary_right':chis=-chis
        return chi,chis

    def bound(self,cell,u,phi,working,mean):
        k=self.k;radial=self.radial_input(cell,u);chart=self.chart(phi)
        if (mean['accurate_S_interval'].lo!=self.actual.S.lo
                or mean['accurate_S_interval'].hi!=self.actual.S.hi):
            raise ValueError('The complete accurate mean and node use different exact S enclosures')
        b,c,bs,cs=radial['scalar'];e,e1,e2=chart['e'];zero=k.Interval(0,0,self.bits)
        original=dict(T=k.vadd(k.vscale(e,b),[zero,zero,c]),Tp=k.vscale(e1,b),
            Tpp=k.vscale(e2,b),Ts=k.vadd(k.vscale(e,bs),[zero,zero,cs]))
        values=[];pieces=[]
        base=dict(same_field_node_binding=dict(supported_unit_seed_identity_sha256=self.inputs.seed_identity,
            literal_phi_hex=phi,provider_sha256=k.PROVIDER_SHA,
            complete_input_binding_identity_sha256=self.inputs.identity),
            address=dict(cell=cell,u_binary64_hex=u,literal_phi_hex=phi,
                exact_affine_S_coefficient_and_constant=radial['exact_affine']),
            actual_working_fields=working)
        for part in radial['branches']:
            node=copy.deepcopy(base);kind=part['kind'];index=part['index'];relative=part['relative']
            if kind=='central':
                a,b1=self.actual.central[index]
                t=((relative-a)/(b1-a)).intersect(0,1)
                node.update(region='central',central_interval_index=index,
                    accurate_normalized_central_coordinate=t.json())
            else:
                node.update(region='outside' if kind=='outside' else 'boundary',
                    accurate_original_reference={name:[v.json() for v in row] for name,row in original.items()})
                if kind!='outside':
                    chi,chis=self.cutoff(relative,kind,index)
                    node.update(accurate_chi=chi.json(),accurate_chi_s=chis.json())
            result=k.bound_reference_node(mean,node)
            values.append(result['intervals'])
            pieces.append(dict(kind=kind,support_index=index,accurate_relative_intersection=relative.json(),
                complete_central_profile_enclosures=k.encode(result['complete_central_profile_enclosures'])))
        hull={name:[k.Interval(min(v[name][j].lo for v in values),max(v[name][j].hi for v in values),self.bits)
            for j in range(3)] for name in FIELD_KEYS}
        errors={name:k.vector_error(hull[name],working[name],self.bits) for name in FIELD_KEYS}
        self.counts['complete_node_bounds']+=1
        self.counts['possible_supported_branches']+=len(pieces)
        self.counts['multiple_branch_nodes']+=int(len(pieces)>1)
        proof=dict(address=base['address'],accurate_S_interval=self.actual.S.json(),
            accurate_s_interval=radial['exact_s'].json(),accurate_relative_point=radial['exact_relative'].json(),
            complete_scalar_piece_scope=radial['scalar_piece_scope'],complete_possible_supported_pieces=pieces,
            working_region_tag_used_to_select_accurate_branch=False,
            complete_original_reference_four_jets_assembled=True,
            all_scalar_chart_cutoff_profile_and_working_carrier_errors_included=True,
            accurate_input_producer_sha256=self.source_sha256,
            fixed_seed_node_scope_only=True)
        return errors,proof


def validate_work_packet(module,inputs,chunk,path):
    value,record=module.capture(path)
    if (value.get('schema')!=module.WORK_SCHEMA or value.get('source_sha256')!=INPUT_SHA
            or value.get('binding_identity_sha256')!=inputs.identity or value.get('chunk')!=chunk
            or value.get('supported_unit_seed_identity_sha256')!=inputs.seed_identity
            or value.get('actual_report')!=inputs.report_record
            or value.get('actual_values_computed_in_this_new_producer') is not True
            or value.get('old_outer_unrecorded_working_words_asserted_identical') is not False):
        raise ValueError('An immutable actual four-jet packet changed its input/query/scope')
    arrays=module.checked_arrays(value['runner_raw_arrays'])
    if {key:module.array_record(v) for key,v in arrays.items()}!=value['array_records']:
        raise ValueError('An immutable actual node array word changed')
    if ([int(v) for v in arrays['cells']]!=[v[0] for v in chunk['radial']]
            or [float(v).hex() for v in arrays['local']]!=[v[1] for v in chunk['radial']]
            or [float(v).hex() for v in arrays['phi']]!=chunk['phi']):
        raise ValueError('An immutable node packet changed literal material addresses')
    return value,record,arrays


def validate_fee_packet(module,inputs,chunk,path,work_record):
    value,record=module.capture(path)
    if (value.get('schema')!=FEE_SCHEMA or value.get('source_sha256')!=sha(__file__)
            or value.get('binding_identity_sha256')!=inputs.identity
            or value.get('chunk_identity_sha256')!=chunk['identity_sha256']
            or value.get('actual_working_packet')!=work_record or value.get('complete') is not True
            or value.get('all_four_reference_jets_paid') is not True
            or value.get('old_outer_working_word_association_paid') is not False
            or value.get('complete_current_field_fees_paid') is not False):
        raise ValueError('An immutable complete node fee packet changed its actual scope')
    arrays=module.checked_arrays(value['runner_raw_arrays'])
    shape=(len(chunk['radial']),len(chunk['phi']),4)
    errors=module.finite_array(arrays['norm_error_upper'],shape=shape)
    if (set(arrays)!={'norm_error_upper'} or module.array_record(errors)!=value['norm_error_upper_array']
            or (errors<0).any()):
        raise ValueError('The complete outward error carriers changed')
    for item in value['complete_accurate_mean_inputs']:
        for key in ('complete_accurate_producer_snapshot','complete_fee_request_snapshot','complete_mean_profile_consumer_snapshot'):
            saved=item[key]['immutable_snapshot']
            if module.file_record(saved['path'])!=saved:
                raise ValueError('An immutable accurate mean proof input changed')
    return value,record


def build_fees(module,inputs,fee_inputs,bounds,chunk,arrays,work_record,packet_path):
    import numpy as np
    errors=np.empty((len(chunk['radial']),len(chunk['phi']),4),dtype=float)
    maxima={name:F(0) for name in FIELD_KEYS}
    proof_digest=hashlib.sha256();ambiguities=[]
    start=time.monotonic();counts0=dict(bounds.counts)
    provenance=[fee_inputs.by_angle[word]['provenance'] for word in chunk['phi']]
    for i,(cell,u) in enumerate(chunk['radial']):
        for j,word in enumerate(chunk['phi']):
            actual={name:[float(v).hex() for v in arrays[name][i,j]] for name in FIELD_KEYS}
            mean=fee_inputs.by_angle[word]['mean']
            upper,proof=bounds.bound(cell,u,word,actual,mean)
            proof=inputs.modules['fees'].encode(proof)
            serialized=json.dumps(proof,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
            proof_digest.update(len(serialized).to_bytes(8,'little'));proof_digest.update(serialized)
            if len(proof['complete_possible_supported_pieces'])>1:
                ambiguities.append(proof)
            for k,name in enumerate(FIELD_KEYS):
                errors[i,j,k]=upper_binary64(upper[name]);maxima[name]=max(maxima[name],upper[name])
    arrays_path=packet_path.with_suffix('.npz')
    array_output=module.save_arrays(arrays_path,{'norm_error_upper':errors})
    value=dict(schema=FEE_SCHEMA,source_sha256=sha(__file__),binding_identity_sha256=inputs.identity,
        chunk_identity_sha256=chunk['identity_sha256'],actual_working_packet=work_record,
        complete=True,complete_nodes=len(chunk['radial'])*len(chunk['phi']),
        field_axis=list(FIELD_KEYS),runner_raw_arrays=array_output,
        norm_error_upper_array=module.array_record(errors),
        maximum_exact_norm_error_upper={key:str(v) for key,v in maxima.items()},
        maximum_outward_binary64_norm_error_upper_hex={key:upper_binary64(v).hex() for key,v in maxima.items()},
        every_binary64_error_carrier_checked_against_its_exact_Fraction=True,
        complete_ordered_node_input_proof_sha256=proof_digest.hexdigest(),
        complete_accurate_mean_inputs=provenance,
        complete_possible_branch_ambiguities=ambiguities,
        accurate_arithmetic_counts={key:bounds.counts[key]-counts0[key] for key in counts0},
        elapsed_seconds=time.monotonic()-start,
        all_four_reference_jets_paid=True,
        exact_scalar_fixed_chart_cutoff_profile_and_all_coordinate_carriers_paid=True,
        complete_source_bound_mean_and_profile_fees_consumed=True,
        point_enclosures_not_whole_cells=True,continuous_phi_cover_paid=False,
        old_outer_working_word_association_paid=False,
        outer_normal_roots_calibration_integrals_and_F_sixjet_fees_paid=False,
        complete_current_field_fees_paid=False,
        full_node_formula_intervals_recomputable_from_all_bound_sources_and_inputs=True)
    inputs.recheck();fee_inputs.recheck()
    module.write_json(packet_path,value,fresh=True)
    return value,module.file_record(packet_path)


def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','report','reference-bundle','carrier','node-report','scalar-input','preparation-report','mean-fee-report','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--seconds',type=float,default=600.)
    p.add_argument('--panels',type=int,default=128)
    p.add_argument('--precision-bits',type=int,default=160)
    p.add_argument('--taylor-order',type=int,default=48)
    p.add_argument('--profile-series-order',type=int,default=48)
    p.add_argument('--radial-block',type=int,default=64)
    p.add_argument('--angle-block',type=int,default=8)
    a=p.parse_args()
    for key in ('repo','report','reference_bundle','carrier','node_report','scalar_input','preparation_report','mean_fee_report','outdir'):
        setattr(a,key,getattr(a,key).resolve())
    if (not math.isfinite(a.seconds) or a.seconds<=0 or a.panels<1 or not 64<=a.precision_bits<=1024
            or a.taylor_order<1 or a.profile_series_order<1 or a.radial_block<1 or a.angle_block<1):
        p.error('Keep positive full arithmetic and natural block/budget parameters')
    if a.outdir==a.repo or a.repo in a.outdir.parents:
        p.error('Scientific raw arrays and full journals remain outside the repository')
    for key in ('report','reference_bundle','carrier','node_report','scalar_input','preparation_report','mean_fee_report'):
        q=getattr(a,key)
        if q==a.outdir or a.outdir in q.parents:
            p.error('The complete fresh output subtree must be disjoint from all inputs')
    return a


def refresh(state):
    rows=state['chunks']
    state['completed_working_chunks']=sum(v.get('working_packet') is not None for v in rows)
    state['completed_fee_chunks']=sum(v.get('fee_packet') is not None for v in rows)
    state['completed_working_nodes']=sum(v['point_count'] for v in rows if v.get('working_packet') is not None)
    state['completed_fee_nodes']=sum(v['point_count'] for v in rows if v.get('fee_packet') is not None)
    state['complete_planned_reference_node_fees']=bool(rows) and all(v.get('fee_packet') is not None for v in rows)
    state['complete']=state['complete_planned_reference_node_fees']
    for name in FIELD_KEYS:
        state['maximum_exact_'+name+'_norm_error_upper']=(None if state['maximum_exact_norm_error_upper'] is None
            else state['maximum_exact_norm_error_upper'][name])
    state['scope']='fixed accurate reference at every declared finite material/integration query; original unrecorded outer words, continuous cover and current physical field fees remain unpaid'
    return state


def main():
    require_actions();args=parse_args();start=time.monotonic()
    module=load_inputs(args.repo)
    inputs=module.BoundReferenceInputs(args)
    args.outdir.mkdir(parents=True,exist_ok=True)
    chunks=list(inputs.chunks(args.radial_block,args.angle_block))
    policy=dict(radial_block=args.radial_block,angle_block=args.angle_block,
        precision_bits=args.precision_bits,taylor_order=args.taylor_order,
        profile_series_order=args.profile_series_order,panels=args.panels,
        all_planned_queries_retained=True,no_subset_fixture=True,
        exact_mean_inputs_may_be_extended_by_new_immutable_schedule_snapshot=True)
    report_path=args.outdir/'report.json'
    if report_path.exists():
        state,_=module.capture(report_path)
        if (state.get('schema')!=SCHEMA or state.get('source_sha256')!=sha(__file__)
                or state.get('binding_identity_sha256')!=inputs.identity or state.get('binding')!=inputs.binding
                or state.get('policy')!=policy or len(state.get('chunks',[]))!=len(chunks)):
            raise ValueError('Resume the same complete source/input/query/arithmetic contract')
    else:
        state=dict(schema=SCHEMA,source_sha256=sha(__file__),binding=inputs.binding,
            binding_identity_sha256=inputs.identity,policy=policy,complete=False,invocations=0,
            chunks=[dict(serial=v['serial'],chunk_identity_sha256=v['identity_sha256'],
                point_count=len(v['radial'])*len(v['phi']),working_packet=None,fee_packet=None,pending=None) for v in chunks],
            mean_fee_input_snapshots=[],complete_planned_reference_node_fees=False,
            actual_values_are_new_provider_reads=True,old_outer_working_word_association_paid=False,
            current_F_J_normal_roots_recomputed=False,continuous_phi_cover_paid=False,
            complete_current_field_fees_paid=False,maximum_exact_norm_error_upper=None,
            last_invocation_elapsed_seconds=None,
            unrecorded_or_missing_nodes_are_not_assumed_zero=True)
    state['invocations']+=1
    fees=MeanFeeInputs(inputs,args.outdir/'immutable-fee-inputs',args.mean_fee_report)
    state['mean_fee_input_snapshots'].append(fees.record)
    bounds=None if inputs.actual is None else AccurateNodeBounds(inputs)
    module.write_json(report_path,refresh(state))
    maxima=None if state['maximum_exact_norm_error_upper'] is None else {k:F(v) for k,v in state['maximum_exact_norm_error_upper'].items()}
    for chunk,row in zip(chunks,state['chunks']):
        if row['serial']!=chunk['serial'] or row['chunk_identity_sha256']!=chunk['identity_sha256']:
            raise ValueError('The immutable complete query order changed')
        directory=args.outdir/('node-'+str(chunk['serial']).zfill(7))
        work_path=directory/'working.json';fee_path=directory/'fees.json'
        if row['working_packet'] is not None:
            actual,record,arrays=validate_work_packet(module,inputs,chunk,work_path)
            if record!=row['working_packet']:
                raise ValueError('A registered immutable working packet changed')
        else:
            arrays=None
        if row['fee_packet'] is not None:
            value,record=validate_fee_packet(module,inputs,chunk,fee_path,row['working_packet'])
            if record!=row['fee_packet']:
                raise ValueError('A registered immutable fee packet changed')
            continue
        if time.monotonic()-start>=args.seconds:
            break
        missing=[word for word in chunk['phi'] if word not in inputs.mean_by_angle]
        if missing or inputs.provider._plan is None:
            row['pending']=dict(reason='actual complete mean or radial-plan input absent',literal_angle_words=missing)
            continue
        try:
            if row['working_packet'] is None:
                directory.mkdir(parents=True,exist_ok=True)
                if work_path.exists() or (directory/'working.npz').exists():
                    raise FileExistsError('An unregistered immutable working packet is not silently overwritten or adopted')
                arrays,actual=inputs.evaluate(chunk)
                actual['runner_raw_arrays']=module.save_arrays(directory/'working.npz',arrays)
                inputs.recheck()
                module.write_json(work_path,actual,fresh=True)
                row['working_packet']=module.file_record(work_path)
                module.write_json(report_path,refresh(state))
            missing_fees=[word for word in chunk['phi'] if word not in fees.by_angle]
            if missing_fees:
                row['pending']=dict(reason='complete accurate mean/profile input not yet available',literal_angle_words=missing_fees)
                continue
            if bounds is None:
                raise ValueError('A complete accurate original reference context is absent')
            if fee_path.exists() or fee_path.with_suffix('.npz').exists():
                raise FileExistsError('An unregistered immutable fee packet is not silently overwritten or adopted')
            value,record=build_fees(module,inputs,fees,bounds,chunk,arrays,row['working_packet'],fee_path)
            row['fee_packet']=record;row['pending']=None
            if maxima is None:maxima={name:F(0) for name in FIELD_KEYS}
            for name in FIELD_KEYS:maxima[name]=max(maxima[name],F(value['maximum_exact_norm_error_upper'][name]))
            state['maximum_exact_norm_error_upper']={key:str(v) for key,v in maxima.items()}
            state['last_invocation_elapsed_seconds']=time.monotonic()-start
            module.write_json(report_path,refresh(state))
            event(event='complete_reference_node_packet_returned',serial=chunk['serial'],nodes=row['point_count'],
                completed_fee_nodes=state['completed_fee_nodes'],planned_nodes=inputs.query_definition['planned_points_with_explicit_group_multiplicity'],
                actual_working_packet_sha256=row['working_packet']['sha256'],actual_fee_packet_sha256=record['sha256'])
        except (ValueError,TypeError,KeyError,ArithmeticError,MemoryError,OSError) as error:
            row['pending']=dict(reason='actual node evaluation or accurate-input consumption failed',error=repr(error))
            state['last_failure']=dict(serial=chunk['serial'],chunk_identity_sha256=chunk['identity_sha256'],error=repr(error),
                missing_or_failed_fee_is_not_geometric_nonexistence=True)
            module.write_json(report_path,refresh(state))
            raise
    inputs.recheck();fees.recheck()
    state['last_invocation_elapsed_seconds']=time.monotonic()-start
    state['actual_provider_counts_this_process']=dict(inputs.provider.counts)
    state['accurate_node_arithmetic_counts_this_process']=None if bounds is None else dict(bounds.counts)
    state['maximum_exact_norm_error_upper']=None if maxima is None else {key:str(v) for key,v in maxima.items()}
    state['natural_budget_return_is_not_whole_field_completion']=True
    module.write_json(report_path,refresh(state))
    event(event='complete_reference_node_fee_schedule_returned',complete=state['complete'],
        completed_working_nodes=state['completed_working_nodes'],completed_fee_nodes=state['completed_fee_nodes'],
        planned_nodes=inputs.query_definition['planned_points_with_explicit_group_multiplicity'],
        all_outer_field_fees_paid=False,report=module.file_record(report_path))


if __name__=='__main__':
    main()
