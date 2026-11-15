#!/usr/bin/env python3
"""Actions-only exact four-row attribution of actual83 state formation.

Reads the complete pinned actual83 artifact and one pinned original73 J chunk.
No RHS/J/ODE/QR/solve/trial is called. All 224 incoming contributions and the
outgoing -I contribution are retained, then matched to the actual83 exact row.
Adjacent binary64 words are diagnostics, not altered trial states or gates.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import resource
import shutil
import struct
import sys
import time
import traceback

REPOSITORY = 'Rogerhu12/math-research-public'
SCHEMA = 'actual83-four-original-rows-exact-state-formation-and-word-spacing-v1'
FETCH_NAME = 'exact_20261115_fetch_actual83_four_row_inputs.py'
FETCH_SHA = 'e3dae97ae649dadd46cf77508e84b8573daaff30a77c14cc6f7c0a77a3bc6c92'
KERNEL_SHA = '51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859'
PIN83 = dict(run_id=43668743706, artifact_id=14143009723,
    artifact_name='visible-mainline-modelresponse-43668743706-1', expected_size=48375172,
    expected_sha256='9eadec9633a1260597268a760b5870bf59bd18ef808e8c5eb6ac5e006df5634c')
PIN73 = dict(run_id=43657001633, artifact_id=14141540502,
    artifact_name='visible-mainline-nojprimalnative-43657001633-1', expected_size=1752742419,
    expected_sha256='3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9')
SOURCE83 = '8d199eda5c1f1df162ded244e8dfd012e0c8d127'
SOURCE73 = '9515d5aaf7c68f8efd366438d6bd81ce73c3486f'
EXACT_RESULT_SHA = '60feb7732547dcd04ef2469c5a1adf7cef5fd93f714107ac41cdb8f71282ff61'
PROBE_RESULT_SHA = '7be2d7f0a98445e5efcd0ba146b7f8257483fa7593a54a6b389e8279f7fcf6ea'
EXACT_SOURCE_SHA = '3570aa9f6bb3b24eb28678a57f88b145a8725a3a7bda05fe14a0860e136c917d'
PROBE_SOURCE_SHA = '305f5db2c6bc0fef85bd3115045531b1b366334b33300852634692a537f7d9cb'
PROBE_HOOK_SHA = 'c03f59e4c3b6555a7a47187f1905a70f1e5a92dafacc222c327f4913c3ccdce0'
ORIGINAL_MATRIX_SHA = '6ea4b16fa7e41ae1099a3e792b67c19cf6c9d4ae41f5c3209fa84d43c5f8fbd8'
ORIGINAL_J_SHA = '1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4'
CHUNK_SHA = 'fd117e2d3cfdd26ddfa584e5c75e521209f12ca16f098596ec61cab3e47f8677'
CHUNK_RELATIVE = 'native-noj-primal-current576-damped/iteration-002/snapshot/large-arrays/stage-jacobians-0002.f64le'
ROUNDING_SOURCE_NAME = 'exact_20261114_saved_stage_full_rational_reference.py'
ROUNDING_SOURCE_SHA = '119864f3dffd764500e3f15b9bfe8c7e27367384486eaaa11a5db885422b8f12'
ROWS = ((10,187,2539),(10,184,2536),(11,186,2762),(9,0,2128))
NAMES = ('stored_base_residual','saved_direction_endpoint','ideal_affine_residual',
         'realized_affine_residual','stored_trial_residual','state_addition_term',
         'remaining_flow_tangent_model_term','total_trial_minus_ideal')
SHAPES = {'base-states':[577,224],'native-delta':[577,224],'trial-states':[577,224],
    'original-scales':[1,577],'cut-target':[1,112],'physical-height':[1,112],
    'original-far-graph':[1,112],'saved-stage-residuals':[576,224],
    'saved-cut-residual':[1,112],'saved-end-residual':[1,112],
    'trial-stage-out':[576,224],'trial-stage-residuals':[576,224],
    'trial-cut-residual':[1,112],'trial-end-residual':[1,112],
    'trial-mean-height-increments':[1,576]}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def require_actions():
    require(os.environ.get('GITHUB_ACTIONS')=='true' and
            os.environ.get('GITHUB_REPOSITORY')==REPOSITORY,
            'All new scientific arithmetic runs only in this public repository Actions')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def digest(path):
    h=hashlib.sha256();size=0
    with path.open('rb') as stream:
        for chunk in iter(lambda:stream.read(1024*1024),b''):
            h.update(chunk);size+=len(chunk)
    return dict(bytes=size,sha256=h.hexdigest())


def relative_path(base, name):
    p=PurePosixPath(name)
    require(isinstance(name,str) and not p.is_absolute() and p.parts and
            '..' not in p.parts and str(p)==name and '\\' not in name,'Safe relative file descriptor')
    q=base.joinpath(*p.parts)
    require(q.is_file() and not q.is_symlink(),'Required regular original file '+name)
    return q


def json_data(raw):
    if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
    return json.loads(raw)


def receipt(path, root):
    return dict(file=path.relative_to(root).as_posix(),**digest(path))


def write_json(out, name, value):
    path=out/name;path.parent.mkdir(parents=True,exist_ok=True)
    raw=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()+b'\n'
    if name.endswith('.gz'):raw=gzip.compress(raw,mtime=0)
    path.write_bytes(raw)
    return receipt(path,out)


def original_file(base, descriptor, records):
    path=relative_path(base,descriptor['file'])
    actual=digest(path)
    require(actual['bytes']==descriptor['bytes'] and actual['sha256']==descriptor['sha256'],
            'Complete original file identity: '+descriptor['file'])
    records.append(dict(file=descriptor['file'],**actual))
    return path


def preserve(path, out, relative):
    destination=out/'large-arrays'/'original-inputs'/relative
    destination.parent.mkdir(parents=True,exist_ok=True)
    require(not destination.exists(),'Independent preserved original path')
    shutil.copyfile(path,destination)
    return receipt(destination,out)


def exact_pair(encoded):
    require(isinstance(encoded,list) and len(encoded)==2 and
            isinstance(encoded[0],str) and re.fullmatch(r'-?0x[0-9a-f]+',encoded[0]) and
            type(encoded[1]) is int,'Complete original dyadic pair')
    n=int(encoded[0],16);power=encoded[1]
    return Fraction(n<<power,1) if power>=0 else Fraction(n,1<<(-power))


def rational(value):
    value=Fraction(value)
    with localcontext() as context:
        context.prec=64;context.Emax=999999;context.Emin=-999999
        display='0' if value==0 else format(Decimal(value.numerator)/Decimal(value.denominator),'.63E')
    return dict(numerator=str(value.numerator),denominator=str(value.denominator),
        decimal_display_64_significant_digits=display,
        display_is_not_an_interval_enclosure=True,display_never_used_for_comparison=True)


def from_rational_record(value):
    return Fraction(int(value['numerator']),int(value['denominator']))


def summary_view(value):
    """Bounded display view; every exact numerator/denominator remains in result.gz."""
    if isinstance(value,dict):
        if {'numerator','denominator','decimal_display_64_significant_digits'} <= set(value):
            return dict(decimal_display_64_significant_digits=value['decimal_display_64_significant_digits'],
                exact_numerator_and_denominator_in_full_result=True,
                display_is_not_an_interval_enclosure=True)
        return {key:summary_view(item) for key,item in value.items()}
    if isinstance(value,list):return [summary_view(item) for item in value]
    return value


def word_fraction(word):
    exponent=(word>>52)&2047;mantissa=word&((1<<52)-1)
    require(exponent!=2047,'Finite original word for exact arithmetic')
    if exponent:
        mantissa|=1<<52;power=exponent-1075
    else:power=-1074
    if word>>63:mantissa=-mantissa
    return Fraction(mantissa<<power,1) if power>=0 else Fraction(mantissa,1<<(-power))


def word_at(raw, index):
    return struct.unpack_from('<Q',raw,index*8)[0]


def word_record(word):
    exponent=(word>>52)&2047;mantissa=word&((1<<52)-1)
    if exponent==2047:
        classification='NaN' if mantissa else ('-infinity' if word>>63 else '+infinity')
        value=None
    else:
        value=struct.unpack('<d',struct.pack('<Q',word))[0]
        classification=('negative-zero' if word>>63 else 'positive-zero') if exponent==0 and mantissa==0 else 'finite'
    return dict(float64le_hex=struct.pack('<Q',word).hex(),value=value,classification=classification)


def adjacent_words(word):
    require(((word>>52)&2047)!=2047,'Finite centre for adjacent-word diagnostic')
    if (word&((1<<63)-1))==0:return (1<<63)|1,1
    return (word+1,word-1) if word>>63 else (word-1,word+1)


def neighbour_record(word, scale, tolerance, scale_scope):
    value=word_fraction(word);lower,upper=adjacent_words(word)
    result=dict(original=word_record(word),scale_scope=scale_scope,
        original_positive_scale=rational(scale),original_binary64_tolerance=rational(tolerance),
        diagnostics_only_no_state_replacement=True,down={},up={})
    gaps={}
    for key,other in (('down',lower),('up',upper)):
        row=dict(adjacent=word_record(other))
        if ((other>>52)&2047)==2047:
            row.update(finite_spacing=False,exact_gap=None)
            gaps[key]=None
        else:
            other_value=word_fraction(other)
            gap=value-other_value if key=='down' else other_value-value
            require(gap>0,'Strict neighboring finite spacing')
            row.update(finite_spacing=True,exact_gap=rational(gap),
                gap_over_scale=rational(gap/scale),
                gap_over_scale_over_original_tolerance=rational(gap/scale/tolerance))
            gaps[key]=gap
        result[key]=row
    return result,gaps


def nearest_even_integer(numerator, denominator):
    quotient, remainder = divmod(numerator, denominator)
    doubled = remainder << 1
    tie = doubled == denominator
    increment = doubled > denominator or (tie and quotient & 1)
    return quotient + int(bool(increment)), tie

def rational_to_binary64_word(value):
    """Exact round-to-nearest, ties-to-even, by integer quotient/remainder.

    No float conversion, Decimal approximation, or longdouble cast participates.
    Exact zero is +0; a nonzero negative input rounded to zero yields -0.
    """
    if value == 0:
        return 0, dict(classification="positive-zero", exact_zero=True,
                       tie=False, unit_power=-1074)
    sign = (1 << 63) if value < 0 else 0
    numerator, denominator = abs(value.numerator), value.denominator
    exponent = numerator.bit_length() - denominator.bit_length()
    if exponent >= 0:
        if numerator < (denominator << exponent):
            exponent -= 1
    elif (numerator << -exponent) < denominator:
        exponent -= 1
    if exponent > 1023:
        return sign | (2047 << 52), dict(
            classification="infinity", exact_zero=False, tie=False,
            unit_power=exponent - 52, overflow=True)
    if exponent < -1022:
        mantissa, tie = nearest_even_integer(numerator << 1074, denominator)
        if mantissa > (1 << 52):
            raise ArithmeticError("Subnormal quantization exceeded its possible carry")
        if mantissa == (1 << 52):
            word = sign | (1 << 52)
            classification = "normal"
        else:
            word = sign | mantissa
            classification = ("negative-zero" if sign else "positive-zero") if mantissa == 0 else "subnormal"
        return word, dict(classification=classification, exact_zero=False,
                          tie=tie, unit_power=-1074, overflow=False)
    unit_power = exponent - 52
    if unit_power <= 0:
        mantissa, tie = nearest_even_integer(numerator << -unit_power, denominator)
    else:
        mantissa, tie = nearest_even_integer(numerator, denominator << unit_power)
    if not ((1 << 52) <= mantissa <= (1 << 53)):
        raise ArithmeticError("Normal quantization produced an impossible significand")
    if mantissa == (1 << 53):
        mantissa >>= 1
        exponent += 1
    if exponent > 1023:
        return sign | (2047 << 52), dict(
            classification="infinity", exact_zero=False, tie=tie,
            unit_power=unit_power, overflow=True)
    word = sign | ((exponent + 1023) << 52) | (mantissa - (1 << 52))
    return word, dict(classification="normal", exact_zero=False, tie=tie,
                      unit_power=unit_power, overflow=False)


def checked_transport(directory, pin, source, kind, records):
    path=relative_path(directory,'_pinned_public_artifact_receipt.json')
    item=json_data(path.read_bytes())
    require(item['repository']==REPOSITORY and item['success'] is True and
            item['pinned_input']==pin and item['zip_verified_before_extraction'] is True,
            'Complete actual artifact transport receipt: '+kind)
    require(item['download']['actual_sha256']==pin['expected_sha256'] and
            item['download']['actual_size']==pin['expected_size'],'Complete original ZIP byte pin')
    require(item['public_artifact_metadata']['workflow_run']['head_sha']==source,'Original artifact source commit')
    adapter=item['public_artifact_metadata']['local_request91_input_transport']
    require(adapter['input_kind']==kind and adapter['source_sha256']==FETCH_SHA and
            adapter['kernel_source_sha256']==KERNEL_SHA,'Frozen independent transport adapter')
    require(item['source_sha256']==KERNEL_SHA,'Frozen standard-library network/publication kernel')
    records.append(dict(kind=kind,receipt=dict(file=path.name,**digest(path)),
        actual_pin=pin,source_commit=source,metadata=item['public_artifact_metadata'],
        download=item['download'],extraction_scope=item['extraction'].get('per_file_verification_scope',
          'Complete original artifact extraction by the unchanged transport kernel')))
    return item,path


def selected_ledger(base, descriptor, wanted_indices, out, name, original_receipts):
    path=original_file(base,descriptor,original_receipts)
    selected={};raw_lines=[];uncompressed=hashlib.sha256();raw_count=0;records=0
    with gzip.open(path,'rb') as stream:
        for index,line in enumerate(stream):
            uncompressed.update(line);raw_count+=len(line);records+=1
            if index in wanted_indices:
                selected[index]=json.loads(line);raw_lines.append(line)
    require(records==descriptor['records'] and raw_count==descriptor['raw_bytes'] and
            uncompressed.hexdigest()==descriptor['raw_sha256'],'Complete original ledger bytes/order count')
    require(set(selected)==set(wanted_indices),'Every requested original ledger record exists')
    destination=out/'large-arrays'/name
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_bytes(gzip.compress(b''.join(raw_lines),mtime=0))
    preserved=receipt(destination,out)
    preserved.update(scope='Complete original JSONL lines at explicitly selected zero-based record indices',
        original_file_descriptor=descriptor,original_record_indices=sorted(wanted_indices),
        extracted_raw_sha256=sha(b''.join(raw_lines)),extracted_records=len(raw_lines))
    return selected,preserved


def bind_inputs(args, out, report):
    records=[];transport=[];preserved=[]
    report['original_inputs']=records
    report['transport']=transport
    report['preserved_original_inputs']=preserved
    for directory,pin,source,kind in ((args.actual83_directory,PIN83,SOURCE83,'actual83'),
            (args.original73_chunk_directory,PIN73,SOURCE73,'original73-j-chunk')):
        _,path=checked_transport(directory,pin,source,kind,transport)
        preserved.append(preserve(path,out,kind+'/'+path.name))
    report['transport']=transport
    exact_dir=args.actual83_directory/'actual73-exact-realized-step'
    probe_dir=args.actual83_directory/'actual73-realized-trial'
    summary_path=relative_path(exact_dir,'summary.json')
    summary=json_data(summary_path.read_bytes())
    require(summary['full_result']['sha256']==EXACT_RESULT_SHA,'Fixed actual83 complete exact result')
    full_path=original_file(exact_dir,summary['full_result'],records)
    full=json_data(full_path.read_bytes())
    require(full['source_sha256']==EXACT_SOURCE_SHA and full['diagnostic_completed'] is True and
            full['complete_componentwise_decomposition_verified'] is True,'Actual83 completed exact source scope')
    require(full['alpha_exact']==dict(numerator='1',denominator='512') or
            full['alpha_exact']==dict(numerator=1,denominator=512),'Original exact alpha1/512')
    require(str(full['original_run_id'])=='43657001633' and full['original_nonlinear_iteration']==2 and
            full['original_source_commit']==SOURCE73,'Actual73 final iteration scope')
    binding_path=original_file(exact_dir,full['binding'],records)
    binding=json_data(binding_path.read_bytes())
    current=binding['original_current_matrix_binding']
    require(current['new_matrix_identity_sha256']==ORIGINAL_MATRIX_SHA and
            current['full_current_J_raw_sha256']==ORIGINAL_J_SHA,'Complete original fixed matrix identity')
    require(current['node_count']==577 and current['shape_dimension']==224 and current['modes']==112,
            'Complete original node/shape dimensions')
    tolerance=current['numerical_configuration']['solveTolerance']
    tol_word=struct.unpack('<Q',struct.pack('<d',tolerance))[0]
    require(math.isfinite(tolerance) and tolerance==2e-9,'Unchanged original binary64 solveTolerance')
    report['original_tolerance']=word_record(tol_word)
    report['original_matrix_identity']=ORIGINAL_MATRIX_SHA
    probe_result_path=relative_path(probe_dir,'result.json')
    require(digest(probe_result_path)['sha256']==PROBE_RESULT_SHA and
            full['probe_result']['sha256']==PROBE_RESULT_SHA,'Actual83 probe result exact byte identity')
    probe=json_data(probe_result_path.read_bytes())
    require(probe['source_sha256']==PROBE_SOURCE_SHA and probe['hook_sha256']==PROBE_HOOK_SHA and
            probe['completed'] is True and probe['original_noJ_evaluate_calls']==1,'Exactly the actual83 probe')
    manifest_path=original_file(probe_dir,probe['array_manifest'],records)
    manifest=json_data(manifest_path.read_bytes())
    require(manifest==binding['probe_array_manifest'],'Whole actual83 raw manifest equality')
    entries={item['name']:item for item in manifest['arrays']}
    require(set(entries)==set(SHAPES) and len(manifest['arrays'])==15,'Complete original fifteen-array inventory')
    raw={}
    for name,shape in SHAPES.items():
        item=entries[name]
        require(item['dtype']=='<f8' and item['order']=='C' and item['shape']==shape,'Original raw array descriptor '+name)
        path=original_file(probe_dir,item,records)
        raw[name]=path.read_bytes()
        preserved.append(preserve(path,out,'actual83-realized-trial/'+item['file']))
    psummary_path=original_file(probe_dir,probe['summary'],records)
    psummary=json_data(psummary_path.read_bytes())
    require(psummary==full['probe_original_summary'],'Complete original noJ summary copied into exact result')
    probe_binding_path=original_file(probe_dir,probe['input_binding'],records)
    pbind=json_data(probe_binding_path.read_bytes())
    require(pbind==binding['probe_input_binding'],'Whole original probe binding equality')
    j=pbind['original_J_descriptor_only']
    require(j['shape']==[576,224,224] and j['dtype']=='<f8' and j['order']=='C' and
            j['raw_sha256']==ORIGINAL_J_SHA and j['total_bytes']==231211008,'Original complete J descriptor')
    chunk=j['chunks'][2]
    require((chunk['chunk_index'],chunk['row_start'],chunk['row_stop'],chunk['bytes'],chunk['sha256'],chunk['raw_sha256'])==
            (2,8,12,1605632,CHUNK_SHA,CHUNK_SHA),'Exact original stage8..11 chunk descriptor')
    require(chunk['file']=='large-arrays/stage-jacobians-0002.f64le','Original chunk relative path')
    chunk_path=original_file(args.original73_chunk_directory,
        dict(file=CHUNK_RELATIVE,bytes=1605632,sha256=CHUNK_SHA),records)
    jraw=chunk_path.read_bytes()
    preserved.append(preserve(chunk_path,out,'original73-J-chunk/'+CHUNK_RELATIVE))
    for source,root,name in ((full_path,exact_dir,'actual83-exact'),(summary_path,exact_dir,'actual83-exact'),
            (binding_path,exact_dir,'actual83-exact'),(probe_result_path,probe_dir,'actual83-realized-trial'),
            (manifest_path,probe_dir,'actual83-realized-trial'),(psummary_path,probe_dir,'actual83-realized-trial'),
            (probe_binding_path,probe_dir,'actual83-realized-trial')):
        preserved.append(preserve(source,out,name+'/'+source.relative_to(root).as_posix()))
    nodes,nreceipt=selected_ledger(exact_dir,full['complete_exact_state_increment_ledger'],
        {9,10,11,12},out,'selected-original-node-increments.jsonl.gz',records)
    block_descriptor=full['complete_or_partial_decomposition_status']['row_decomposition_ledger']
    blocks,breceipt=selected_ledger(exact_dir,block_descriptor,{10,11,12},out,
        'selected-original-row-blocks.jsonl.gz',records)
    for node,item in nodes.items():
        require(item['node']==node and item['first_state_coordinate']==node*224,'Original full node record identity')
        for key in ('exact_h','ideal_alpha_delta','exact_h_minus_ideal_increment'):
            require(len(item[key])==224,'All 224 original coordinate increments retained')
        start=node*224*8;end=start+224*8
        for name,key in (('base-states','base_node_raw_sha256'),('trial-states','trial_node_raw_sha256'),('native-delta','delta_node_raw_sha256')):
            require(sha(raw[name][start:end])==item[key],'Original node payload and increment identity')
    for index,block in blocks.items():
        require(block['kind']=='stage' and block['node']==index-1 and block['count']==224 and
                block['first_global_equation_row']==112+(index-1)*224,'Original stage row order')
        require(set(block['exact_vectors'])==set(NAMES) and
                all(len(v)==224 for v in block['exact_vectors'].values()),'All original eight row vectors retained')
    report['preserved_original_inputs']=preserved
    report['selected_original_increment_records']=nreceipt
    report['selected_original_row_records']=breceipt
    report['original_inputs']=records
    report['input_binding']=write_json(out,'large-arrays/input-binding.json.gz',dict(
        schema='actual83-four-row-double-artifact-input-binding-v1',transport=transport,
        original_exact_result=summary['full_result'],original_exact_source_sha256=EXACT_SOURCE_SHA,
        original_probe_result=dict(file='result.json',**digest(probe_result_path)),
        original_probe_source_sha256=PROBE_SOURCE_SHA,original_probe_hook_sha256=PROBE_HOOK_SHA,
        original_matrix_binding=current,original_complete_J_descriptor=j,selected_original_J_chunk=chunk,
        original_probe_array_manifest=manifest,requested_rows=[dict(stage=n,row=i,global_row=g) for n,i,g in ROWS],
        original_tolerance=word_record(tol_word),original_alpha=probe['alpha'],
        original_inputs=records,preserved_original_inputs=preserved,
        selected_node_ledger=nreceipt,selected_row_ledger=breceipt,
        original_source_text_not_reimported_or_executed=True))
    return dict(full=full,raw=raw,jraw=jraw,nodes=nodes,blocks=blocks,tol_word=tol_word,probe_summary=psummary)


def node_data(bound, out, report):
    raw=bound['raw'];alpha=Fraction(1,512);computed={};records=[]
    for node,original in sorted(bound['nodes'].items()):
        scale=word_fraction(word_at(raw['original-scales'],node));require(scale>0,'Original positive node sigma')
        vectors=[];public=[]
        for col in range(224):
            index=node*224+col
            bw=word_at(raw['base-states'],index);tw=word_at(raw['trial-states'],index);dw=word_at(raw['native-delta'],index)
            b,t,d=word_fraction(bw),word_fraction(tw),word_fraction(dw)
            h=t-b;ideal=alpha*d;error=h-ideal
            require(h==exact_pair(original['exact_h'][col]) and
                    ideal==exact_pair(original['ideal_alpha_delta'][col]) and
                    error==exact_pair(original['exact_h_minus_ideal_increment'][col]),
                    'Exact original h/ideal/error identity at node '+str(node)+' column '+str(col))
            spacing,gaps=neighbour_record(bw,scale,bound['tol'],'state coordinate own original sigma[node]')
            if h==0 and ideal!=0:category='zero-realized-nonzero-ideal'
            elif h!=0:category='nonzero-realized'
            else:category='zero-realized-zero-ideal'
            vectors.append(dict(base_word=bw,trial_word=tw,delta_word=dw,h=h,ideal=ideal,error=error,gaps=gaps,category=category))
            public.append(dict(node=node,column=col,component='Q' if col<112 else 'Pi',mode=col+1 if col<112 else col-111,
                base=word_record(bw),trial=word_record(tw),delta=word_record(dw),
                original_base_and_trial_words_equal=bw==tw,category=category,
                exact_h=rational(h),exact_ideal_alpha_delta=rational(ideal),exact_h_minus_ideal=rational(error),
                original_dyadic_encodings={key:original[key][col] for key in
                    ('exact_h','ideal_alpha_delta','exact_h_minus_ideal_increment')},base_word_spacing=spacing))
        computed[node]=vectors
        records.append(dict(node=node,original_sigma=rational(scale),coordinates=public,
            all_224_actual_h_and_original_ledger_values_equal=True))
    report['complete_four_node_coordinate_diagnostics']=write_json(out,
        'large-arrays/four-complete-node-word-spacing-and-exact-increments.json.gz',dict(
            schema='actual83-four-complete-original-node-increment-word-spacing-v1',
            original_nodes=[9,10,11,12],nodes=records,coordinate_count=896,
            neighboring_words_are_diagnostics_not_actual_trial_states=True,
            no_multiply_vs_add_rounding_cause_separately_inferred=True))
    return computed


def process_row(bound, node_vectors, stage, row, global_row, out):
    require(global_row==112+stage*224+row,'Original global row map')
    raw=bound['raw'];old=bound['blocks'][stage+1]
    sigma_word=word_at(raw['original-scales'],stage);sigma=word_fraction(sigma_word)
    require(sigma>0 and struct.pack('<Q',sigma_word).hex()==old['original_sigma_float64le_hex'],'Original row sigma raw identity')
    original={name:exact_pair(old['exact_vectors'][name][row]) for name in NAMES}
    rword=word_at(raw['saved-stage-residuals'],stage*224+row)
    tword=word_at(raw['trial-stage-residuals'],stage*224+row)
    require(word_fraction(rword)==original['stored_base_residual'] and word_fraction(tword)==original['stored_trial_residual'],
            'Original row residual words and exact ledger equal')
    offset=((stage-8)*224*224+row*224)*8
    rowbytes=bound['jraw'][offset:offset+224*8]
    require(len(rowbytes)==1792,'Complete 224 coefficient J row')
    jrow_path=out/'large-arrays'/('original-J-row-'+str(global_row)+'.f64le')
    jrow_path.write_bytes(rowbytes)
    contributions=[];sum_state=Fraction(0);sum_h=Fraction(0);sum_ideal=Fraction(0)
    groups={name:dict(count=0,signed=Fraction(0),absolute_sum=Fraction(0)) for name in
        ('zero-realized-nonzero-ideal','nonzero-realized','zero-realized-zero-ideal')}
    all_products=[]
    for col in range(224):
        jw=word_at(rowbytes,col);coefficient=word_fraction(jw);entry=node_vectors[stage+1][col]
        state_part=coefficient*entry['error'];hpart=coefficient*entry['h'];idealpart=coefficient*entry['ideal']
        sum_state+=state_part;sum_h+=hpart;sum_ideal+=idealpart;all_products.append(state_part)
        group=groups[entry['category']];group['count']+=1;group['signed']+=state_part;group['absolute_sum']+=abs(state_part)
        amplified={}
        for direction,gap in entry['gaps'].items():
            amplified[direction]=None if gap is None else dict(
                absolute_J_times_adjacent_state_gap_over_row_sigma=rational(abs(coefficient)*gap/sigma),
                same_quantity_over_original_tolerance=rational(abs(coefficient)*gap/sigma/bound['tol']))
        contributions.append(dict(incoming_node=stage+1,incoming_column=col,
            component='Q' if col<112 else 'Pi',mode=col+1 if col<112 else col-111,
            original_J_coefficient=word_record(jw),category=entry['category'],
            base_state_word=word_record(entry['base_word']),trial_state_word=word_record(entry['trial_word']),
            exact_h=rational(entry['h']),exact_ideal_alpha_delta=rational(entry['ideal']),
            exact_h_minus_ideal=rational(entry['error']),
            state_formation_contribution=rational(state_part),state_formation_contribution_over_sigma=rational(state_part/sigma),
            realized_action_contribution=rational(hpart),ideal_action_contribution=rational(idealpart),
            adjacent_input_word_linearized_effect=amplified,
            adjacent_input_effect_is_not_an_actual_nonlinear_trial_or_error_bound=True))
    outgoing=node_vectors[stage][row]
    direct=-outgoing['error'];direct_h=-outgoing['h'];direct_ideal=-outgoing['ideal']
    total=sum_state+direct
    require(total==original['state_addition_term'],'Complete 224 incoming plus outgoing -I equals original83 state term')
    require(original['stored_base_residual']+sum_h+direct_h==original['realized_affine_residual'],
            'Same original row realized affine response')
    require(original['stored_base_residual']+sum_ideal+direct_ideal==original['ideal_affine_residual'],
            'Same original row ideal affine response')
    require(original['stored_trial_residual']-original['realized_affine_residual']==original['remaining_flow_tangent_model_term'],
            'Same original residual remaining term')
    require(original['state_addition_term']+original['remaining_flow_tangent_model_term']==original['total_trial_minus_ideal'],
            'Same original total componentwise decomposition')
    targetword=outgoing['trial_word'];flowword=word_at(raw['trial-stage-out'],stage*224+row)
    target_spacing,_=neighbour_record(targetword,sigma,bound['tol'],'actual trial target coordinate / original equation sigma[stage]')
    flow_spacing,_=neighbour_record(flowword,sigma,bound['tol'],'actual original noJ flow output / original equation sigma[stage]')
    difference=word_fraction(flowword)-word_fraction(targetword)
    difference_word,difference_rounding=rational_to_binary64_word(difference)
    t=word_fraction(tword)
    largest=max(range(224),key=lambda col:abs(all_products[col]))
    group_public={key:dict(count=value['count'],signed_sum=rational(value['signed']),
        signed_sum_over_sigma=rational(value['signed']/sigma),
        sum_of_absolute_contributions_over_sigma=rational(value['absolute_sum']/sigma))
        for key,value in groups.items()}
    body=dict(schema='actual83-complete224-input-plus-output-original-row-attribution-v1',
        original_stage=stage,original_row=row,original_global_equation_row=global_row,
        component='Q' if row<112 else 'Pi',mode=row+1 if row<112 else row-111,
        propagation_orientation=dict(incoming_node=stage+1,outgoing_node=stage,
            equation='r[stage] + J[stage]*increment[stage+1] - increment[stage]'),
        original_sigma=word_record(sigma_word),original_sigma_exact=rational(sigma),
        original_J_row=receipt(jrow_path,out),all_224_incoming_contributions=contributions,
        outgoing_negative_identity_contribution=dict(node=stage,column=row,
            original_base=word_record(outgoing['base_word']),actual_trial=word_record(targetword),
            exact_h=rational(outgoing['h']),exact_ideal_alpha_delta=rational(outgoing['ideal']),
            exact_h_minus_ideal=rational(outgoing['error']),signed_contribution=rational(direct),
            signed_contribution_over_sigma=rational(direct/sigma)),
        groups=group_public,incoming_total_over_sigma=rational(sum_state/sigma),
        complete_state_formation_sum_over_sigma=rational(total/sigma),
        original_eight_row_values={name:dict(original_dyadic=old['exact_vectors'][name][row],
            exact=rational(value),exact_over_original_sigma=rational(value/sigma)) for name,value in original.items()},
        largest_absolute_incoming_contribution=dict(column=largest,first_tie_rule='smallest original input column',
            signed_over_sigma=rational(all_products[largest]/sigma)),
        actual_output_and_target=dict(target=word_record(targetword),original_noJ_flow_output=word_record(flowword),
            stored_trial_residual=word_record(tword),exact_flow_minus_target=rational(difference),
            exact_flow_minus_target_minus_stored_r=rational(difference-t),
            exact_flow_minus_target_minus_stored_r_over_sigma=rational((difference-t)/sigma),
            correctly_rounded_exact_difference=word_record(difference_word),rounding=difference_rounding,
            exact_zero_rounding_sign_convention='Exact mathematical zero rounds to +0; this does not reconstruct a signed-zero subtraction rule',
            correctly_rounded_difference_equals_saved_residual_word=difference_word==tword,
            target_spacing=target_spacing,flow_output_spacing=flow_spacing,
            original_base_flow_output_not_exported_by_actual83_and_not_reconstructed=True),
        all_original83_row_equalities_verified=True,
        no_coordinate_or_contribution_dropped=True,
        no_positive_universal_residual_lower_bound_claimed=True)
    descriptor=write_json(out,'large-arrays/row-'+str(global_row)+'-complete-attribution.json.gz',body)
    return dict(original_stage=stage,original_row=row,original_global_equation_row=global_row,
        component=body['component'],mode=body['mode'],incoming_node=stage+1,outgoing_node=stage,
        full_row=descriptor,original_J_row=body['original_J_row'],groups=group_public,
        outgoing_negative_identity_contribution_over_sigma=rational(direct/sigma),
        complete_state_formation_sum_over_sigma=rational(total/sigma),
        original_remaining_flow_tangent_model_term_over_sigma=rational(original['remaining_flow_tangent_model_term']/sigma),
        largest_absolute_incoming_contribution=body['largest_absolute_incoming_contribution'],
        output_and_target_spacing=body['actual_output_and_target'],all_original83_row_equalities_verified=True)


def norm_word_diagnostics(bound):
    full=bound['full'];record=full['norm_readback']['original_baseline']
    original_word=int.from_bytes(bytes.fromhex(record['float64le_hex']),'little')
    original=word_fraction(original_word)
    spacing,_=neighbour_record(original_word,Fraction(1),bound['tol'],
        'dimensionless original norm; sigma division already occurred, no second sigma division')
    result=dict(original_native_base_and_actual_trial_norm=record,
        original_scalar_comparison=full['norm_readback']['actual_probe_scalar_comparison'],
        original_dimensionless_norm_spacing=spacing,exact_original_global_norms={},
        global_norms_copied_from_actual83_not_recomputed_from_any_matrix=True,
        rounding_here_is_new_diagnostic_arithmetic_not_a_relabelled_actual83_result=True)
    for name in ('stored_base_residual','ideal_affine_residual','realized_affine_residual','stored_trial_residual'):
        maximum=full['exact_original_sigma_maxima'][name]
        value=from_rational_record(maximum['exact_absolute_scaled_value'])
        word,meta=rational_to_binary64_word(value)
        result['exact_original_global_norms'][name]=dict(
            original_exact_maximum=maximum['exact_absolute_scaled_value'],
            original_max_coordinate={key:maximum[key] for key in ('kind','node','row','global_equation_row','component','mode')},
            correctly_rounded_binary64=word_record(word),rounding=meta,
            rounded_word_equals_actual_original_native_baseline=word==original_word,
            exact_value_minus_original_native_float=rational(value-original),
            exact_value_minus_its_correctly_rounded_float=rational(value-word_fraction(word)))
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--actual83-directory',type=Path,required=True)
    parser.add_argument('--original73-chunk-directory',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    require_actions()
    require(not args.out.exists(),'Use an independent fresh output directory')
    args.out.mkdir(parents=True)
    started=time.monotonic()
    report=dict(schema=SCHEMA,completed=False,scientific_arithmetic_started=False,
        scientific_arithmetic_performed=False,byte_only=False,
        source_file=Path(__file__).name,source_sha256=sha(Path(__file__).read_bytes()),
        original_actual83_pin=PIN83,additional_original73_pin=PIN73,
        original_rows=[dict(stage=n,row=i,global_row=g) for n,i,g in ROWS],
        new_RHS_calls=0,new_J_calls=0,new_ODE_steps=0,new_QR_calls=0,new_solve_calls=0,new_trial_calls=0,
        changed_alpha_direction_tolerance_or_acceptance=False,used_as_any_scientific_acceptance_gate=False,
        rounding_function_text_origin=dict(file=ROUNDING_SOURCE_NAME,sha256=ROUNDING_SOURCE_SHA,
            functions=['nearest_even_integer','rational_to_binary64_word'],
            original_source_module_not_imported=True),rows=[],errors=[])
    try:
        bound=bind_inputs(args,args.out,report)
        report['scientific_arithmetic_started']=True
        report['scientific_arithmetic_performed']=True
        bound['tol']=word_fraction(bound['tol_word'])
        require(bound['tol']>0,'Positive original binary64 solveTolerance')
        nodes=node_data(bound,args.out,report)
        for stage,row,global_row in ROWS:
            report['rows'].append(process_row(bound,nodes,stage,row,global_row,args.out))
            write_json(args.out,'progress.json',dict(schema=SCHEMA,completed_rows=len(report['rows']),
                completed_global_rows=[r['original_global_equation_row'] for r in report['rows']],
                elapsed_seconds=time.monotonic()-started))
        report['dimensionless_native_norm_word_diagnostics']=norm_word_diagnostics(bound)
        report.update(completed=True,complete_original_row_count=4,
            complete_incoming_contribution_count=896,complete_outgoing_contribution_count=4,
            original_J_words_used_in_scientific_arithmetic=896,
            complete_original_J_chunk_bytes_verified=1605632,
            original_full_J_payload_reloaded=False,complete_original_four_node_coordinate_count=896,
            all_original83_row_equalities_verified=True,
            source_scope_limits=[
                'Each exact row reads incoming node n+1 and outgoing node n; no node reversal.',
                'All 224 incoming contributions and the outgoing negative-identity term are retained.',
                'The original83 global norm ratios are reused; their nearest binary64 words are newly computed here.',
                'State, actual flow-output and dimensionless norm spacings are separate quantities.',
                'An adjacent-word residual spacing is not a positive universal residual lower bound; output may equal target.',
                'Remaining actual flow/tangent-model discrepancy is not assigned to a unique nonlinear/root/J cause.',
                'This one alpha and one original current state do not diagnose all ten original trials.',
                'No new weighting, eta, direction, trial, acceptance, tolerance or geometry is selected.',
                'Decimal displays are not interval enclosures and are never used for exact comparisons.'])
    except Exception as exc:
        report['errors'].append(dict(type=type(exc).__name__,message=str(exc)))
        (args.out/'diagnostic-error.log').write_text(traceback.format_exc())
    finally:
        report['elapsed_seconds']=time.monotonic()-started
        report['maximum_RSS_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        full=write_json(args.out,'large-arrays/result.json.gz',report)
        summary={key:report[key] for key in ('schema','completed','scientific_arithmetic_started','scientific_arithmetic_performed',
            'byte_only','source_file','source_sha256','original_actual83_pin','additional_original73_pin','original_rows',
            'new_RHS_calls','new_J_calls','new_ODE_steps','new_QR_calls','new_solve_calls','new_trial_calls',
            'changed_alpha_direction_tolerance_or_acceptance','used_as_any_scientific_acceptance_gate',
            'errors','elapsed_seconds','maximum_RSS_kib')}
        summary.update(full_result=full,rows=report['rows'],
            dimensionless_native_norm_word_diagnostics=report.get('dimensionless_native_norm_word_diagnostics'),
            complete_four_node_coordinate_diagnostics=report.get('complete_four_node_coordinate_diagnostics'),
            preserved_original_inputs=report.get('preserved_original_inputs'),input_binding=report.get('input_binding'),
            source_scope_limits=report.get('source_scope_limits'))
        summary=summary_view(summary)
        summary['complete_exact_ratios_and_all_coordinates_retained_in_full_result_and_row_files']=True
        write_json(args.out,'summary.json',summary)
        print(json.dumps(dict(schema=SCHEMA,completed=report['completed'],
            completed_row_count=len(report['rows']),full_result=full,errors=report['errors']),allow_nan=False))
    return 0 if report['completed'] else 2


if __name__=='__main__':
    raise SystemExit(main())
