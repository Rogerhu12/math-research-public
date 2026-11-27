#!/usr/bin/env python3
"""Complete N-only dyadic material observation carrier, R679/R691.

The fixed reference problem remains N=2048.  Only the finite observer has
N=4096. Every old literal angle is copied to its even column; all 1025
quarter orbits have their full positive multiplicity. No radial node, scalar
target, material chart, free coordinate or normal-chain stage is changed.
Array construction and metric attribution are public-Actions-only. Pure
validators do not import a numerical library or evaluate a physical field.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import struct

SCHEMA = 'complete-fixed-reference-dyadic-angular-observation-v1'
REFERENCE_FULL_N = 2048
CURRENT_FULL_N = 4096
REFERENCE_SOURCE = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual observation construction requires public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def array_words_sha(words):
    h = hashlib.sha256(b'float64')
    h.update(json.dumps([len(words)]).encode())
    for word in words:
        value = float.fromhex(word)
        if not math.isfinite(value) or value.hex() != word:
            raise ValueError('Use every canonical finite binary64 word')
        h.update(struct.pack('<d',value))
    return h.hexdigest()


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        reference_source_sha256=REFERENCE_SOURCE,
        reference_full_N=REFERENCE_FULL_N,current_full_N=CURRENT_FULL_N,
        reference_quarter_count=513,current_quarter_count=1025,
        old_angles_at_even_columns=True,old_literal_angles_copied_without_recalculation=True,
        old_angle_formula='binary64 pi*j/1024; j=0,...,512',
        new_odd_angle_formula='binary64 pi*j/2048; j=1,3,...,1023',
        current_multiplicity='2 at indices 0 and 1024; 4 at every interior index',
        normalized_even_weight_relative_to_parent='1/2',
        normalized_even_total_mass='1/2',normalized_odd_total_mass='1/2',
        fixed_reference_N_unchanged=True,fixed_material_chart_unchanged=True,
        fixed_scalar_target_unchanged=True,radial_mesh_and_observations_unchanged=True,
        radial_outer_integration_unchanged=True,normal_partition_unchanged=True,
        original_free_coordinate_layout_unchanged=True,
        finite_angular_objective_changes=True,original_parent_Phi_inherited=False,
        nonpolynomial_SO3_field_bandlimit_claimed=False,
        continuous_metric_or_geometry_certificate=False)


def validate_carrier(value):
    if not isinstance(value,dict) or value.get('definition') != definition():
        raise ValueError('Bind the complete unchanged N-only observation definition')
    if value.get('definition_identity_sha256') != canonical(definition()):
        raise ValueError('Observation definition identity differs')
    old = value.get('reference_literal_phi_hex')
    new = value.get('current_literal_phi_hex')
    weights = value.get('current_multiplicity_integer')
    if (not isinstance(old,list) or len(old)!=513 or not isinstance(new,list) or len(new)!=1025
            or old != [(math.pi*j/1024).hex() for j in range(513)]
            or new[::2] != old
            or new[1::2] != [(math.pi*j/2048).hex() for j in range(1,1024,2)]
            or weights != [2]+[4]*1023+[2]):
        raise ValueError('All literal old/even, new/odd and positive orbit weights are required')
    if (value.get('reference_phi_sha256') != array_words_sha(old)
            or value.get('current_phi_sha256') != array_words_sha(new)
            or value.get('current_multiplicity_sha256') != array_words_sha([float(v).hex() for v in weights])
            or value.get('reference_full_N')!=2048 or value.get('current_full_N')!=4096
            or value.get('all_old_angle_words_preserved') is not True
            or value.get('old_grid_indices_reinterpreted') is not False):
        raise ValueError('Complete same-word observation carrier binding differs')
    return json.loads(json.dumps(value,allow_nan=False))


def build(reference_problem):
    require_actions()
    import numpy as np
    p = reference_problem
    context = p.axisymmetric_reference_context
    if (context.model.get('source_sha256') != REFERENCE_SOURCE
            or p.full_N!=2048 or p.N!=513 or p.J!=923 or p.M!=160 or p.P!=7377):
        raise ValueError('The complete original reference remains M160/J923/N2048')
    old = np.array(p.phi,dtype=np.float64,copy=True)
    fine = np.empty(1025,dtype=np.float64)
    fine[::2] = old
    fine[1::2] = np.pi*np.arange(1,1024,2,dtype=np.float64)/2048
    multiplicity = np.full(1025,4.,dtype=np.float64)
    multiplicity[[0,-1]]=2.
    if (old.shape!=(513,) or not np.isfinite(fine).all() or np.any(np.diff(fine)<=0)
            or fine[::2].tobytes()!=old.tobytes()
            or np.asarray(p.multiplicity,dtype=np.float64).tolist()!=[2.]+[4.]*511+[2.]):
        raise ValueError('Preserve every actual original orbit and its literal angle')
    record = dict(definition=definition(),definition_identity_sha256=canonical(definition()),
        reference_full_N=2048,current_full_N=4096,
        reference_literal_phi_hex=[float(v).hex() for v in old],
        current_literal_phi_hex=[float(v).hex() for v in fine],
        current_multiplicity_integer=[int(v) for v in multiplicity],
        reference_phi_sha256=array_words_sha([float(v).hex() for v in old]),
        current_phi_sha256=array_words_sha([float(v).hex() for v in fine]),
        current_multiplicity_sha256=array_words_sha([float(v).hex() for v in multiplicity]),
        all_old_angle_words_preserved=True,old_grid_indices_reinterpreted=False)
    validate_carrier(record)
    for a in (old,fine,multiplicity):
        a.flags.writeable=False
    return fine,multiplicity,record


def validate_base_model(model):
    carrier = validate_carrier(model.get('angular_observation_refinement'))
    if (model.get('reference_full_N')!=2048 or model.get('current_full_N')!=4096
            or model.get('M')!=160 or model.get('J')!=923
            or model.get('complete_axisymmetric_reference_model',{}).get('source_sha256')!=REFERENCE_SOURCE):
        raise ValueError('Only the observer changes; retain the full original fixed reference')
    return carrier


def attribute(raw,stage_weights,multiplicity,parameters,*,spectral,centered,stage_block):
    """Read old-even/odd/all from the very same current raw three-Gram buffer."""
    require_actions()
    import numpy as np
    raw=np.asarray(raw)
    if raw.ndim!=3 or raw.shape[1:]!=(1025,3) or not np.isfinite(raw).all():
        raise ValueError('All current radial rows, angles and three Gram entries are required')
    result={}
    for name,index in (('all',slice(None)),('old_even',slice(None,None,2)),('new_odd',slice(1,None,2))):
        values=raw[:,index,:]
        weights=np.asarray(multiplicity)[index]
        stat=spectral.statistics(values,stage_weights,weights,parameters)
        stat=centered.augment_statistics(values,stage_weights,weights,parameters,stat,stage_block=stage_block)
        e,f,d=values[...,0],values[...,1],values[...,2]
        result[name]=dict(spectral=stat,
            max_relative_gram=float(np.max((np.abs(e+d)+np.hypot(e-d,2*f))/2)),
            actual_angle_count=int(values.shape[1]),actual_multiplicity_sum=float(weights.sum()))
    return dict(schema='same-current-buffer-dyadic-observation-attribution-v1',
        source_sha256=sha(__file__),groups=result,
        old_parent_saved_statistics_used=False,additional_field_evaluations=0,
        finite_Phi_halfsum_is_exact_arithmetic_identity=True,
        actual_floating_reduction_error_enclosed=False,
        no_intermediate_angle_or_continuous_certificate=True)


def validate_report(value,model):
    carrier=validate_base_model(model['base_complete_model'])
    if value != carrier:
        raise ValueError('The report must preserve its actual full observer carrier')
    return dict(definition_identity_sha256=carrier['definition_identity_sha256'],
        reference_full_N=2048,current_full_N=4096,reference_quarter_count=513,current_quarter_count=1025,
        reference_phi_sha256=carrier['reference_phi_sha256'],current_phi_sha256=carrier['current_phi_sha256'],
        all_old_angle_words_preserved=True,old_grid_indices_reinterpreted=False,
        current_objective_has_all_positive_orbit_weights=True,
        radial_refinement_performed=False,free_coordinate_count_changed=False)


def validate_attribution(value):
    if (not isinstance(value,dict) or value.get('schema')!='same-current-buffer-dyadic-observation-attribution-v1'
            or value.get('source_sha256')!=sha(__file__)
            or value.get('old_parent_saved_statistics_used') is not False
            or value.get('additional_field_evaluations')!=0
            or value.get('actual_floating_reduction_error_enclosed') is not False
            or value.get('no_intermediate_angle_or_continuous_certificate') is not True):
        raise ValueError('Attribute only the complete same current raw Gram buffer')
    groups=value.get('groups',{})
    if set(groups)!={'all','old_even','new_odd'}:
        raise ValueError('Retain all three complete positive angular measures')
    result={}
    parameters=None
    for name,count,mass in (('all',1025,4096),('old_even',513,2048),('new_odd',512,2048)):
        item=groups[name]
        spectrum=item.get('spectral',{})
        if (item.get('actual_angle_count')!=count or item.get('actual_multiplicity_sum')!=mass
                or not isinstance(item.get('max_relative_gram'),(float,int))
                or not math.isfinite(item['max_relative_gram']) or item['max_relative_gram']<0):
            raise ValueError('Every same-buffer angular partition must retain its entire grid and mass')
        now={key:spectrum[key] for key in ('p','epsilon','scale')}
        if parameters is None: parameters=now
        if parameters!=now:
            raise ValueError('All/even/odd use one identical scalar loss definition')
        number=spectrum.get('centered_phi_normalized')
        if isinstance(number,bool) or not isinstance(number,(float,int)) or not math.isfinite(number):
            raise ValueError('Do not fabricate a missing angular-measure scalar')
        result[name]=dict(max_relative_gram=item['max_relative_gram'],Phi=number,
            angle_count=count,multiplicity_sum=mass)
    return dict(groups=result,parameters=parameters,old_parent_saved_Phi_used=False,
        computed_same_buffer_half_sum_gap=result['all']['Phi']-(result['old_even']['Phi']+result['new_odd']['Phi'])/2,
        floating_reduction_error_enclosed=False,continuous_certificate=False)
