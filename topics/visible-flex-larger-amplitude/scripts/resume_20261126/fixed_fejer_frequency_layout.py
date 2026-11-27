#!/usr/bin/env python3
"""Complete fixed-reference M160 -> current M320 layout and word inclusion.

Only the declared current trial space changes.  Pure validators import no
scientific package.  Array inclusion is public-Actions-only and never
evaluates a field, a root, a Jacobian, or a scientific integral.
"""
import hashlib
import json
import os
from pathlib import Path

SCHEMA = 'complete-fixed-fejer-M160-to-M320-frequency-inclusion-v1'
BASE_SCHEMA = 'complete-fixed-fejer-frequency-refined-frozen-reference-so3-meridian-v1'
REFERENCE_M = 160
CURRENT_M = 320
RADIAL_J = 923
FIXED_CORE = 3
FULL_ANGLES = 2048


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def sha(path):
    digest=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            digest.update(block)
    return digest.hexdigest()


def digest(value,name):
    if (not isinstance(value,str) or len(value)!=64
            or any(c not in '0123456789abcdef' for c in value)):
        raise ValueError('Keep the complete actual SHA256: '+name)
    return value


def definition(*, reference_M, current_M, J, K, full_N, mesh_sha256):
    if (type(reference_M) is not int or reference_M!=REFERENCE_M
            or type(current_M) is not int or current_M!=CURRENT_M
            or type(J) is not int or J!=RADIAL_J
            or type(K) is not int or K!=FIXED_CORE
            or type(full_N) is not int or full_N!=FULL_ANGLES):
        raise ValueError('Only the complete frozen-M160/current-M320/J923/N2048 inclusion is declared')
    digest(mesh_sha256,'the unchanged complete mesh')
    radial_free=[i for i in range(3*J) if i not in (0,3*(J-1),3*(J-1)+1)]
    old_n,new_n=3*reference_M+2,3*current_M+2
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        reference_M=reference_M,current_M=current_M,J=J,K=K,full_N=full_N,
        mesh_sha256=mesh_sha256,radial_free_slots=radial_free,
        original_rotation_channels=old_n,current_rotation_channels=new_n,
        original_free_core=reference_M-K,current_free_core=current_M-K,
        original_free_size=reference_M-K+len(radial_free)*old_n+1,
        current_free_size=current_M-K+len(radial_free)*new_n+1,
        core_copy=dict(old_start=0,new_start=0,count=reference_M-K),
        omega_blocks=[
            dict(component='x',basis='odd-sine',old_start=0,new_start=0,count=reference_M+1),
            dict(component='y',basis='odd-cosine',old_start=reference_M+1,
                 new_start=current_M+1,count=reference_M+1),
            dict(component='z',basis='even-sine',old_start=2*(reference_M+1),
                 new_start=2*(current_M+1),count=reference_M)],
        height_copy='actual final H word to last current slot',
        all_original_free_words_retained=True,new_current_modes_zero=True,
        fixed_reference_and_material_chart_unchanged=True,
        same_accuracy_of_numerical_field_or_root_claimed=False,
        compatible_implicit_branch_required_for_exact_selected_field_inclusion=True,
        old_metric_geometry_norm_identity_or_damping_inherited=False)


def validate_definition(value):
    if not isinstance(value,dict):
        raise ValueError('Keep the full independent current-frequency definition')
    expected=definition(reference_M=value.get('reference_M'),current_M=value.get('current_M'),
        J=value.get('J'),K=value.get('K'),full_N=value.get('full_N'),
        mesh_sha256=value.get('mesh_sha256'))
    if value!=expected:
        raise ValueError('The complete fixed-reference/current-layout definition changed')
    return canonical(expected)


def validate_base_model(model,*,expected_base_source_sha256=None):
    if not isinstance(model,dict) or model.get('schema')!=BASE_SCHEMA:
        raise ValueError('Use the independently source-bound frequency-refined complete base')
    if expected_base_source_sha256 is not None and model.get('source_sha256')!=expected_base_source_sha256:
        raise ValueError('The actual complete refined base source changed')
    reference=model.get('complete_axisymmetric_reference_model')
    if (not isinstance(reference,dict) or reference.get('M')!=REFERENCE_M
            or reference.get('J')!=RADIAL_J or model.get('M')!=CURRENT_M
            or model.get('reference_M')!=REFERENCE_M or model.get('current_M')!=CURRENT_M
            or model.get('J')!=RADIAL_J):
        raise ValueError('Do not relabel or mutate the complete original M160 reference')
    for key in ('mesh_sha256','fixed_chart_core_sha256','fixed_core_first3',
                'fixed_scalar_metric_identity_sha256','fixed_scalar_profile_definition'):
        if model.get(key)!=reference.get(key):
            raise ValueError('The fixed reference/current base disagree: '+key)
    value=model.get('frequency_layout_definition')
    identity=validate_definition(value)
    if (identity!=model.get('frequency_layout_identity_sha256')
            or model.get('frequency_layout_source_sha256')!=sha(__file__)
            or value['mesh_sha256']!=model.get('mesh_sha256')):
        raise ValueError('The whole refined layout/source identity changed')
    for key in ('all_original_outer_free_variables_retained_and_new_modes_added',
                'frozen_reference_layout_unchanged','current_norm_layout_changed'):
        if model.get(key) is not True:
            raise ValueError('Retain old variables and distinguish the current larger space: '+key)
    return value


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Array inclusion belongs to the public repository Actions')


def array_sha(value):
    import numpy as np
    value=np.ascontiguousarray(value)
    h=hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def embed_outer_words(value,layout):
    """Copy every old free word, inserting zeros only in genuinely new modes."""
    require_actions()
    import numpy as np
    identity=validate_definition(layout)
    x=np.asarray(value)
    if (str(x.dtype)!='float64' or not x.dtype.isnative
            or x.shape!=(layout['original_free_size'],) or not np.isfinite(x).all()):
        raise ValueError('Supply the actual complete finite original native binary64 point')
    old_core=layout['original_free_core'];new_core=layout['current_free_core']
    old_n=layout['original_rotation_channels'];new_n=layout['current_rotation_channels']
    radial=len(layout['radial_free_slots'])
    y=np.zeros(layout['current_free_size'],dtype=np.float64)
    y[:old_core]=x[:old_core]
    old=x[old_core:-1].reshape(radial,old_n)
    new=y[new_core:-1].reshape(radial,new_n)
    records=[]
    for block in layout['omega_blocks']:
        a,b,n=block['old_start'],block['new_start'],block['count']
        new[:,b:b+n]=old[:,a:a+n]
        if new[:,b:b+n].tobytes()!=old[:,a:a+n].tobytes():
            raise ArithmeticError('An original full rotation block was not copied word for word')
        records.append(dict(component=block['component'],old_start=a,new_start=b,count=n,
            original_block_sha256=array_sha(old[:,a:a+n]),
            included_block_sha256=array_sha(new[:,b:b+n]),all_words_identical=True))
    y[-1]=x[-1]
    if y[:old_core].tobytes()!=x[:old_core].tobytes() or y[-1:].tobytes()!=x[-1:].tobytes():
        raise ArithmeticError('The old free core or H words changed')
    marked=np.zeros(new_n,dtype=bool)
    for block in layout['omega_blocks']:
        marked[block['new_start']:block['new_start']+block['count']]=True
    if np.any(y[old_core:new_core]!=0) or np.any(new[:,~marked]!=0):
        raise ArithmeticError('Every genuinely added mode must be zero at inclusion')
    record=dict(schema='actual-complete-free-point-zero-inclusion-v1',
        layout_source_sha256=sha(__file__),layout_identity_sha256=identity,
        original_full_point_sha256=array_sha(x),current_full_point_sha256=array_sha(y),
        original_free_size=int(x.size),current_free_size=int(y.size),
        original_free_core_sha256=array_sha(x[:old_core]),
        included_free_core_sha256=array_sha(y[:old_core]),
        original_height_hex=float(x[-1]).hex(),current_height_hex=float(y[-1]).hex(),
        rotation_blocks=records,all_original_free_words_retained=True,
        added_core_and_rotation_modes_zero=True,
        actual_field_or_root_evaluated_by_inclusion=False,
        original_and_current_point_bytes_equal=False,
        numerical_field_equality_claimed=False,
        old_metric_geometry_or_continuous_certificate_inherited=False)
    return y,record


def validate_inclusion(value,layout):
    identity=validate_definition(layout)
    if (not isinstance(value,dict)
            or value.get('schema')!='actual-complete-free-point-zero-inclusion-v1'
            or value.get('layout_source_sha256')!=sha(__file__)
            or value.get('layout_identity_sha256')!=identity
            or value.get('original_free_size')!=layout['original_free_size']
            or value.get('current_free_size')!=layout['current_free_size']):
        raise ValueError('The full actual coordinate-inclusion record changed')
    for key in ('original_full_point_sha256','current_full_point_sha256',
                'original_free_core_sha256','included_free_core_sha256'):
        digest(value.get(key),key)
    if (value['original_free_core_sha256']!=value['included_free_core_sha256']
            or value.get('original_height_hex')!=value.get('current_height_hex')
            or not isinstance(value.get('rotation_blocks'),list)
            or len(value['rotation_blocks'])!=3):
        raise ValueError('Keep every actual old free block and H')
    for actual,block in zip(value['rotation_blocks'],layout['omega_blocks']):
        for key in ('component','old_start','new_start','count'):
            if actual.get(key)!=block[key]:
                raise ValueError('The three unequal rotation blocks changed')
        digest(actual.get('original_block_sha256'),'original complete rotation block')
        if (actual.get('included_block_sha256')!=actual['original_block_sha256']
                or actual.get('all_words_identical') is not True):
            raise ValueError('Every retained full rotation word is required')
    for key in ('all_original_free_words_retained','added_core_and_rotation_modes_zero'):
        if value.get(key) is not True:
            raise ValueError('Incomplete exact trial-space inclusion')
    for key in ('actual_field_or_root_evaluated_by_inclusion','original_and_current_point_bytes_equal',
                'numerical_field_equality_claimed','old_metric_geometry_or_continuous_certificate_inherited'):
        if value.get(key) is not False:
            raise ValueError('Do not promote a word transfer to a field or geometry certificate')
    return dict(value)


def validate_report(report,*,expected_layout_source_sha256):
    if expected_layout_source_sha256!=sha(__file__):
        raise ValueError('Bind the exact complete independent layout validator')
    model=report['representation']
    if canonical(model)!=report.get('model_identity_sha256'):
        raise ValueError('Keep the actual whole current model')
    base=model['base_complete_model']
    layout=validate_base_model(base)
    identity=canonical(layout)
    if (report.get('reference_M')!=REFERENCE_M or report.get('current_M')!=CURRENT_M
            or report.get('frequency_layout_definition')!=layout
            or report.get('frequency_layout_identity_sha256')!=identity
            or report.get('frequency_layout_source',{}).get('sha256')!=sha(__file__)
            or report.get('original_variables')!=layout['current_free_size']
            or report.get('initial_full_variable_point_sha256') is None):
        raise ValueError('Current complete space, layout source or actual first point differs')
    norm=report['coordinate_norm']
    if canonical({k:v for k,v in norm.items() if k!='norm_identity_sha256'})!=norm.get('norm_identity_sha256'):
        raise ValueError('The current complete norm identity is invalid')
    record=report['frequency_refinement'];mode=record.get('mode')
    if mode=='actual-complete-parent-zero-inclusion':
        inclusion=validate_inclusion(record.get('coordinate_inclusion'),layout)
        if inclusion['current_full_point_sha256']!=report['initial_full_variable_point_sha256']:
            raise ValueError('The inclusion is not the actual first fine point')
    elif mode=='same-source-complete-restart':
        if record.get('current_full_point_sha256')!=report['initial_full_variable_point_sha256']:
            raise ValueError('The actual whole fine restart point differs')
    else:
        raise ValueError('Use an actual complete coarse parent or the same complete fine source')
    for key in ('parent_driver_source_sha256','parent_model_identity_sha256',
                'parent_norm_identity_sha256'):
        digest(record.get(key),key)
    return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=layout,
        definition_identity_sha256=identity,reference_M=REFERENCE_M,current_M=CURRENT_M,
        actual_initial_full_point_sha256=report['initial_full_variable_point_sha256'],
        mode=mode,all_original_free_variables_retained=True,
        computed_old_new_field_equality_claimed=False,old_geometry_or_continuous_certificate_inherited=False)
