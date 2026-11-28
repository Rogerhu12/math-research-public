#!/usr/bin/env python3
"""Export the own fixed actual-DN field using the reviewed full-map mesh algebra.

No source is relabelled as a design/chord return. The genuine own-KIND gate,
same complete frozen g, final physical H, entire native mean and every saved
tail Fourier mode are retained. The original ring topology, all-mode position
evaluation, held-frame formula and 5 MB binary-double PLY rule are unchanged.
The phase end and material grip width are explicit rational inputs, checked
against this actual lambda-one core's curvature and protected window.
This output is a visualization; continuous geometry and the C2 limit require
their separate proofs for the same actual field and explicit cut width.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import qr_fixed_actual_cartesian_prefix as reader
import material_circle_phase_contract as phase_api
from qr_fixed_actual_closed_map import load_closed_map
from qr_fixed_actual_prefix_continuous import write

MESH_SHA = '38fcc275e1462a5d145dbd7391af36e7febeabfe8a536936e87f7072e78ed412'
COUPLED_MAP_SHA = 'ee5745c809c635fec21c2b2121daa2fdbcb5133b33896c53228c627dbcb3e764'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-run','geometry-bundle','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--frame',choices=('held','phase'),default='held')
    parser.add_argument('--cylinder-half-length',type=float,choices=(.0025,.005),default=.0025)
    parser.add_argument('--cut-width',type=float,default=.04)
    parser.add_argument('--angular',type=int,default=256)
    parser.add_argument('--prefix-intervals',type=int,default=56)
    parser.add_argument('--tail-intervals',type=int,default=28)
    parser.add_argument('--disk-intervals',type=int,default=8)
    parser.add_argument('--times',nargs='+',default=['0','1/4','1/2','3/4','1'])
    parser.add_argument('--phase-end',type=Q,required=True)
    parser.add_argument('--held-width',type=Q,default=Q(27,50))
    args = parser.parse_args()
    phase_end,held_width = args.phase_end,args.held_width
    if phase_end <= 0 or held_width <= 0:
        raise ValueError('Use positive exact phase-end and held-width')
    out = args.outdir.resolve()
    if out == reader.REPO or reader.REPO in out.parents:
        raise ValueError('Reproducible actual meshes belong outside the source repository')
    if (args.angular < 16 or args.angular % 2 or args.prefix_intervals < 4
            or args.tail_intervals < 4 or args.disk_intervals < 4):
        raise ValueError('Use the original even angular grid and at least four intervals per region')
    times = [Q(value) for value in args.times]
    if not times or len(set(times)) != len(times) or any(not 0 <= t <= 1 for t in times):
        raise ValueError('Use distinct exact rational times in [0,1]')
    # This acceptance selects the correct old geometry provider before the
    # unchanged mesh module imports any of its mathematical helpers.
    record,physical,view,provenance = reader.accepted_fixed(args.source_run)
    del physical
    mesh_path = HERE.parent/'geometry/export_actual_closed_mesh.py'
    if reader.sha(mesh_path) != MESH_SHA:
        raise ValueError('The reviewed original mesh algebra changed')
    mesh = reader.module('_fixed_actual_reviewed_mesh_algebra',mesh_path)
    imported_map = sys.modules['actual_closed_map_coupled_v3']
    if reader.sha(imported_map.__file__) != COUPLED_MAP_SHA:
        raise ValueError('The imported original rotation/circle provider changed')
    out.mkdir(parents=True,exist_ok=False)
    started = time.monotonic()
    value = load_closed_map(args.source_run,args.geometry_bundle,out/'verified-node-index.json',
        cylinder_half_length=args.cylinder_half_length,cut_width=args.cut_width,
        canonical_r67_marker=True)
    report = dict(status='evaluating_own_fixed_actual_complete_map_meshes',source=reader.ref(__file__),
        source_kind=reader.SOURCE_KIND,source_model_kind=reader.model.KIND,
        source_run=reader.ref(args.source_run),geometry_bundle=reader.ref(args.geometry_bundle),
        actual_fixed_provenance=value.actual_fixed_provenance,
        actual_complete_map_definition=value.definition_provenance,
        full_height_binding=view['height_reference'],full_height_packet=view['packet'],
        fixed_problem=record['fixed_problem'],frozen_complete_metric=record['frozen_profile'],
        source_mean_nodes=record['mean_nodes'],source_mean_gauss_order=6,
        current_physical_file=view['physical'],source_homotopy=record['core_settings']['homotopy'],
        source_record_relabelled_or_rewritten=False,raw_candidate_used_as_final_height=False,
        all_saved_modes_evaluated=True,Fourier_field_truncated=False,
        mesh_discretization_is_not_a_continuous_certificate=True,
        metric_certified=False,reach_certified=False,held_set_certified=False,
        euclidean_noncongruence_certified=False,C2_limit_proved=False,completion_criteria_passed=False,
        frame=args.frame,phase_definition=f'alpha(t)=({phase_end})*t, exact real expression',
        cylinder_half_length=args.cylinder_half_length,cut_width=args.cut_width,
        canonical_marker_metadata=value.r67_marker.metadata(),files=[])
    try:
        report.update(explicit_phase_contract=phase_api.describe(value,phase_end,held_width),
            phase_contract_source=reader.ref(Path(phase_api.__file__)))
        H = reader.height_bytes(view['candidate_H'],record['modes'])
        for height in (value.cap.packet['request']['height'],
                       value.cap.packet['response']['checkpoint']['cutHeight']):
            if reader.height_bytes(height,record['modes']) != H:
                raise ValueError('The mesh substituted raw or scaled H for this physical field')
        frame = phase_api.held_frame(value,phase_end,held_width,mesh.circle) if args.frame == 'held' else None
        report['held_frame_definition'] = ('R_(-(1-k)*alpha) G_alpha+O-R_(k*alpha) O; '
            'k is the actual exact core curvature and O its true arc center' if frame else None)
        report['held_frame_evaluation_only'] = (dict(center=frame[0].tolist(),
            literal_core_curvature_exact=str(Q(frame[1]))) if frame else None)
        rings = mesh.ring_parameters(value,args.prefix_intervals,args.tail_intervals,args.disk_intervals)
        faces,topology = mesh.faces_for_rings(len(rings),args.angular)
        report.update(topology=topology,angular_vertices_per_ring=args.angular,
            ring_count=len(rings),ring_parameters=rings,
            visualization_samples_do_not_bound_unresolved_spatial_frequencies=True)
        if 24*topology['vertices']+13*topology['faces']+1024 >= mesh.LIMIT:
            raise ValueError('The visualization grid cannot fit in the original strict 5 MB rule')
        theta = 2*np.pi*np.arange(args.angular)/args.angular
        reference_error = 0.
        for index,t in enumerate(times):
            phase = float(phase_end*t)
            positions = [value.disk_jets(0.,0.,-1)[0][None,:]]
            for kind,coordinate,side in rings:
                points = mesh.ring_positions(value,kind,coordinate,side,theta,phase)
                for j in (0,args.angular//3,args.angular-1):
                    true_reader = (value.prefix_jets(side*coordinate,theta[j],phase)[0]
                        if kind == 'prefix' else value.tail_jets(coordinate,theta[j],side,phase)[0])
                    reference_error = max(reference_error,float(np.max(abs(points[j]-true_reader))))
                positions.append(points)
            positions.append(value.disk_jets(0.,0.,1)[0][None,:])
            vertices = mesh.transform(np.concatenate(positions),phase,frame)
            if not np.all(np.isfinite(vertices)) or reference_error > 2e-12:
                raise ArithmeticError('The original vector adapter differs from the actual fixed map reader')
            normals = np.cross(vertices[faces[:,1]]-vertices[faces[:,0]],
                               vertices[faces[:,2]]-vertices[faces[:,0]])
            area2 = np.linalg.norm(normals,axis=1)
            if not np.all(np.isfinite(area2)) or np.any(area2 == 0):
                raise ArithmeticError('A sampled mesh triangle is nonfinite or has zero area')
            row = mesh.write_ply(out/f'closed-t{index:02d}.ply',vertices,faces,
                f't={t}; alpha=({phase_end})*t; frame={args.frame}; own fixed actual-DN field')
            row.update(t_exact=str(t),phase_exact=str(phase_end*t),
                minimum_double_triangle_area_sampled=float(np.min(area2)))
            report['files'].append(row)
            report.update(maximum_vector_vs_reader_position_difference=reference_error,
                          seconds=time.monotonic()-started)
            write(out/'summary.json',report)
            print(json.dumps(dict(mesh=index,t=str(t),bytes=row['bytes'],seconds=report['seconds'])),flush=True)
        sources = {**reader.reader_sources(),**provenance['actual_geometry_provider_sources']}
        for path in (Path(__file__),HERE/'qr_fixed_actual_closed_map.py',
                     HERE/'qr_fixed_actual_prefix_continuous.py',Path(phase_api.__file__),
                     mesh_path,Path(imported_map.__file__)):
            sources[str(path.resolve())] = reader.sha(path)
        report.update(status='own_fixed_actual_complete_map_meshes_exported',source_hashes=sources,
            full_node_check=reader.ref(out/'verified-node-index.json'),
            every_file_strictly_below_5_million_bytes=True,seconds=time.monotonic()-started,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        write(out/'summary.json',report)
    finally:
        value.close()


if __name__ == '__main__':
    main()
