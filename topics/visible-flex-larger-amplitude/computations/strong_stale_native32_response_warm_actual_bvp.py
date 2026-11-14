#!/usr/bin/env python3
"""Transport all 32 saved old control modes only as an initial guess.

Author: strong_recovery (GPT-6 Astra Pro, AI assisted), 2026-11-13.
Both the old response point and the current complete field are real accepted
M32/N1280 objects. The current original owned acceptance and its fixed-view
identity are checked by the unchanged prior transport adapter. Complete old
vectors stay bound to their own original full nine-control response. They
are never presented as derivatives at a different current point.

All 97 state channels and all 32 core parameter directions are retained.
An old direction may be interpolated to the full current mesh in the common
material coordinate and rescaled through actual physical core units. This
only supplies an initial guess to the original d151 production pipeline;
original new-H, full-J, Newton, RMS, physical BC, domain and audit gates stay.
The coarse-* CLI names mean old-response source, not fewer modes here.
"""
from __future__ import annotations
import ast
import hashlib
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE_NAME = 'strong_stale_coarse_response_warm_actual_bvp.py'
BASE_SHA = 'e21809f94b1b702481ff30181fc936c5ea9e43d9436b4fe69586efadef10bbd0'
SELF_NAME = Path(__file__).stem
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
NATIVE_SCOPE = __doc__


def build():
    path=HERE/BASE_NAME
    if hashlib.sha256(path.read_bytes()).hexdigest()!=BASE_SHA:
        raise ValueError('The frozen accepted-origin stale transport changed')
    spec=importlib.util.spec_from_file_location('_frozen_native32_stale_transport_base',path)
    base=importlib.util.module_from_spec(spec);sys.modules[spec.name]=base;spec.loader.exec_module(base)
    source=base._STALE_SOURCE;original=source;changes=[]
    def edit(before,after,count=1):
        nonlocal source
        if source.count(before)!=count:
            raise ValueError('The original same-mode dimension/source anchor differs: '+repr(before))
        source=source.replace(before,after);changes.append(dict(before=before,after=after,count=count))
    node=ast.parse(source).body[0]
    old_doc=''.join(source.splitlines(keepends=True)[node.lineno-1:node.end_lineno])
    edit(old_doc,repr(NATIVE_SCOPE)+'\n')
    for before,after in [
        ("(int(coarse['modes']), int(current['modes'])) != (28, 32)","(int(coarse['modes']), int(current['modes'])) != (32, 32)"),
        ('This declared initial-guess embedding is exactly M28 to M32','This declared old-point initial guess is exactly M32 to M32'),
        ("(coarse['config']['angular'], current['config']['angular']) != (1024, 1280)","(coarse['config']['angular'], current['config']['angular']) != (1280, 1280)"),
        ('old_scales.shape != (27,)','old_scales.shape != (31,)'),
        ("response['modes'] != 28 or response['angular'] != 1024","response['modes'] != 32 or response['angular'] != 1280"),
        ("combined = np.zeros(old['y'].size+28)","combined = np.zeros(old['y'].size+32)"),
        ('mapping = np.r_[np.arange(29), 33+np.arange(28), 65+np.arange(28)]','mapping = np.arange(97)'),
        ("transported_field.shape != (85, len(now['x']))","transported_field.shape != (97, len(now['x']))"),
        ('parameters[1:28] = old_parameters[1:]*old_scales/current_scales[:27]','parameters[1:32] = old_parameters[1:]*old_scales/current_scales[:31]'),
        ('not np.all(parameters[28:] == 0.)','not np.all(parameters[32:] == 0.)'),
        ('coarse_modes=28, actual_modes=32','coarse_modes=32, actual_modes=32'),
        ('        added_fine_channels_have_zero_increment_only=True,',
         '        added_fine_channels_have_zero_increment_only=True,\n'
         '        all_97_native_state_rows_and_all_32_core_directions_retained=True,\n'
         '        current_point_Jacobian_or_control_response_not_created=True,'),
    ]:edit(before,after)
    edit("    weights = {}\n", """    wanted_fields = ['delta','boost_length','boost_speed','vu',
        'descending_turn_curvature','start_acceleration','initial_speed_frontload',
        'vd','descending_sync_curvature']
    if (response.get('fields') != wanted_fields or response.get('partial_recovery')
            or not response.get('samechart_response_adapter', {}).get('completed')
            or len(response.get('tangent_arrays', [])) != 45):
        raise ValueError('This native transport requires the actually completed full nine-control response')
    weights = {}
""")
    edit('strong_stale_coarse_response_warm_actual_bvp',SELF_NAME,3)
    reverse=source
    for row in reversed(changes):
        if reverse.count(row['after'])!=row['count']:
            raise ValueError('The exact native transport reverse differs')
        reverse=reverse.replace(row['after'],row['before'])
    if reverse!=original:raise ValueError('The native transport changed another original gate')
    ast.parse(source,filename='<native32-complete-old-response-initial-guess>')
    provenance=dict(base._STALE_TRANSPORT_PROVENANCE,
        native32_same_mode_adapter_source_sha256=SELF_SHA,
        native32_base_adapter_source_sha256=BASE_SHA,
        native32_transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        native32_changes=changes,exact_reverse_recovers_original_stale_transport=True,
        original_current_acceptance_verifier_unchanged=True,
        complete_old_nine_response_required=True,
        all_old_and_current_modes=32,no_new_modes_or_directions_fabricated=True,
        original_mathematical_provider_and_solver_sources_unchanged=True)
    return source,provenance,base._verify_current_origin


SOURCE,_STALE_TRANSPORT_PROVENANCE,_verify_current_origin=build()
exec(compile(SOURCE,'<native32-complete-old-response-initial-guess>','exec'),globals())

if __name__=='__main__':main()
