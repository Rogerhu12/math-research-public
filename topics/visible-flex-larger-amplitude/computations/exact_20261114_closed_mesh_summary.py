#!/usr/bin/env python3
"""Read actual finite meshes and summarize diameter, hold and phase margins.

Point-cloud distances remain spatial samples. The fixed-cap diameter bracket
uses the explicit cap geometry; no continuous whole-surface diameter or reach
certificate is inferred from the mesh or its Euler characteristic.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.spatial.distance import cdist


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();start=time.monotonic();source_hash=sha(__file__)
    b=a.directory;assembly_path=b/'refined-A-closed-assembly.json';plan_path=b/'refined-A-closed-plan.json'
    pair_path=b/'refined-A-closed-all-phase-finite-pairs.json';mesh_path=b/'refined-A-closed-phase0.ply.gz'
    assembly=json.loads(assembly_path.read_text());plan=json.loads(plan_path.read_text());pairs=json.loads(pair_path.read_text())
    raw=gzip.decompress(mesh_path.read_bytes());offset=raw.index(b'end_header\n')+len(b'end_header\n')
    V,F=plan['vertices'],plan['faces']
    vertices=np.frombuffer(raw,dtype=[('x','<f8'),('y','<f8'),('z','<f8'),('piece','u1')],count=V,offset=offset)
    x=np.stack([vertices[k] for k in ('x','y','z')],axis=1)
    faces=np.frombuffer(raw,dtype=[('count','u1'),('indices','<i4',(3,))],count=F,offset=offset+25*V)['indices']
    fixed_indices=np.flatnonzero(vertices['piece']>0);fixed=x[fixed_indices]
    diameter=0.;witness=None
    for first in range(0,len(fixed),128):
        d=cdist(fixed[first:first+128],fixed)
        ii,jj=np.unravel_index(np.argmax(d),d.shape)
        if d[ii,jj]>diameter:
            diameter=float(d[ii,jj]);witness=[int(fixed_indices[first+ii]),int(fixed_indices[jj])]
    areas=np.linalg.norm(np.cross(x[faces[:,1]]-x[faces[:,0]],x[faces[:,2]]-x[faces[:,0]]),axis=1)/2
    H=assembly['mean_gauge']['upper_cap_height'];cuff=plan['cuff'];A=plan['fixed_cap']['markers'][0]['height']
    D=assembly['vertex_cloud_ball_diameter_upper']
    phase=max(assembly['phase_vertex_samples'],key=lambda z:z['vertex_cloud_hausdorff'])
    result=dict(schema='actual-refined-closed-mesh-summary-v1',finished=True,
        source_sha256_at_start=source_hash,inputs={str(p):sha(p) for p in (assembly_path,plan_path,pair_path,mesh_path)},
        topology=assembly['topology'],minimum_triangle_area=float(areas.min()),
        all_three_mesh_files_below_5MB=all(row['bytes']<5_000_000 and row['uncompressed_bytes']<5_000_000 for row in assembly['files']),
        files=[dict(file=Path(row['file']).name,compressed_bytes=row['bytes'],uncompressed_bytes=row['uncompressed_bytes'],sha256=row['sha256'],t=row['t']) for row in assembly['files']],
        global_vertex_cloud_diameter=dict(lower=assembly['vertex_cloud_diameter_lower'],ball_upper=D,
            continuous_surface_certificate=False),
        fixed_hold=dict(fixed_vertices=len(fixed),vertex_cloud_diameter=diameter,
            witness_vertex_indices=witness,witness_coordinates=x[witness].tolist(),
            diameter_ratio_to_vertex_ball_D=diameter/D,
            continuous_cap_geometry_numeric_bracket=[2*math.hypot(cuff,H),2*math.hypot(cuff,H+A)],
            cap_bracket_reason='Opposite points on the fixed cuff circles give the lower value; all fixed caps lie in radius r_c and |z|<=H+A for the upper. Displayed square roots are numerical evaluations.',
            entire_caps_fixed_at_every_phase=True),
        phase_hold_samples=dict(maximum_vertex_cloud_hausdorff=phase['vertex_cloud_hausdorff'],t=phase['t'],
            ratio_to_vertex_ball_D=phase['ratio_to_vertex_ball_diameter_upper'],required_point_two_D=.2*D,
            all=assembly['phase_vertex_samples'],continuous_Hausdorff_or_delta_hold_bound=False),
        reach_threshold=pairs['tau'],reach_threshold_divided_by_vertex_ball_D=pairs['tau']/D,
        all_phase_normal_chord_samples={key:dict(pair_count=pairs[key].get('pair_count',pairs[key].get('all_pairs')),
            negative_pairs=pairs[key]['negative_sample_pairs'],minimum_margin=pairs[key]['worst']['margin'],
            worst=pairs[key]['worst']) for key in ('moving_fixed','moving_moving','fixed_fixed')},
        sampled_geometry=assembly['sampled_piece_jets'],full_mean=assembly['mean_height'],mean_gauge=assembly['mean_gauge'],
        shared_cut_after=assembly['shared_cut']['after'],fixed_markers=assembly['fixed_markers'],
        task_completed=False,continuous_embedding_or_reach_certified=False,
        limitations=['All spatial normal-chord checks are finite samples, although moving/fixed phase is minimized continuously.',
            'Point-cloud Hausdorff values do not by themselves certify continuous delta_hold.',
            'The display samples do not replace denser prior prefix/tail curvature and metric readouts.',
            'A still has amplitude about0.063D in this sample, far below the0.2D requirement.'],seconds=time.monotonic()-start)
    with a.out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(output=str(a.out),D=result['global_vertex_cloud_diameter'],Hdiam=diameter,
        Hdiam_over_D=diameter/D,phase_ratio=result['phase_hold_samples']['ratio_to_vertex_ball_D'],
        area_min=result['minimum_triangle_area'],margins={k:v['minimum_margin'] for k,v in result['all_phase_normal_chord_samples'].items()},seconds=result['seconds'])),flush=True)


if __name__=='__main__':main()
