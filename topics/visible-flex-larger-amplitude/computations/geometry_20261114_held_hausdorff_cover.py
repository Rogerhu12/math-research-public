#!/usr/bin/env python3
"""A true whole-surface held Hausdorff witness from a position cover.

The writer is a small API for an existing continuous-cover producer. The CLI
consumes the resulting packet and the same closed bundle. It never substitutes
material-point displacement or a core-only diameter for set Hausdorff distance.
All continuous envelopes remain explicit producer hypotheses.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data=Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if data[:2]==b'\x1f\x8b' else data)


def bundle_paths(directory):
    directory=Path(directory)
    return (directory/'refined-A-closed-plan.json',
            directory/'refined-A-closed-assembly.json',
            directory/'refined-A-closed-phase0.ply.gz')


def write_position_cover(path, *, directory, centers, enclosures,
                         source_vertex_indices, marked_diameter_upper,
                         witness_position_error, supplied_envelopes,
                         supplied_envelopes_contain_saved_samples,
                         producer_source_sha256, rotation_axis_xy=(0.,0.),
                         chunk_size=50000,distance_evaluation_error=None):
    """Export already computed cover data; this does not run pair checks.

    centers/enclosures cover ALL unmarked active parameter blocks. Fixed flat
    disks are handled exactly by the consumer. A producer must not supply only
    the near-pair subset or only the blocks left unresolved by a reach check.
    """
    path=Path(path)
    if path.exists():
        raise FileExistsError('Refusing to overwrite a position-cover packet')
    centers=np.asarray(centers,dtype=np.float64)
    enclosures=np.asarray(enclosures,dtype=np.float64)
    indices=np.asarray(source_vertex_indices,dtype=np.int64)
    if centers.ndim!=2 or centers.shape[1]!=3 or len(centers)==0 or enclosures.shape!=(len(centers),) or indices.shape!=(len(centers),):
        raise ValueError('Full active centers, enclosures and source indices must have matching shapes')
    if not np.all(np.isfinite(centers)) or not np.all(np.isfinite(enclosures)) or np.any(enclosures<0):
        raise ValueError('Finite positions and nonnegative finite enclosures required')
    if marked_diameter_upper<=0 or witness_position_error<0 or chunk_size<1:
        raise ValueError('Invalid diameter, position-error or chunk budget')
    if distance_evaluation_error is None:
        distance_evaluation_error=witness_position_error
    if not math.isfinite(distance_evaluation_error) or distance_evaluation_error<0:
        raise ValueError('Finite nonnegative distance-evaluation error required')
    plan_path,assembly_path,mesh_path=bundle_paths(directory)
    plan,assembly=read(plan_path),read(assembly_path)
    if assembly['inputs']['plan']['sha256']!=sha(plan_path):
        raise ValueError('Closed assembly and plan differ')
    phase0=next(row for row in assembly['files'] if row['t']==0)
    if phase0['sha256']!=sha(mesh_path):
        raise ValueError('Closed phase0 mesh binding differs')
    axis=[float(v) for v in rotation_axis_xy]
    if len(axis)!=2 or not all(math.isfinite(v) for v in axis):
        raise ValueError('Two finite rotation-axis coordinates required')
    # Current canonical bundle puts both caps on horizontal planes about the
    # common rotation axis. The plane center and radius are mathematical
    # parameters, not bounds inferred from a finite cap vertex cloud.
    cap_height=float(assembly['mean_gauge']['upper_cap_height'])
    cuff=float(plan['cuff'])
    if cuff<=0 or cap_height<=0:
        raise ValueError('Two positive-radius caps with separated planes required')
    markers=plan['fixed_cap']['markers']
    cap_rows=[]
    for upper in (False,True):
        selected=[row for row in markers if bool(row['upper'])==upper]
        amplitude=sum(abs(float(row['height'])) for row in selected)
        support_inside=all(math.hypot(*row['center'])+row['radius']<cuff for row in selected)
        cap_rows.append(dict(center=axis+[cap_height if upper else -cap_height],
            normal=[0.,0.,1.],radius=cuff,marker_height_upper=amplitude,
            marker_height_bound_rule='Sum of absolute peak heights; valid even if supports overlap.',
            marker_supports_strictly_inside_circle=support_inside))
    path.parent.mkdir(parents=True,exist_ok=True)
    chunks=[]
    for start in range(0,len(centers),chunk_size):
        stop=min(start+chunk_size,len(centers))
        file=path.with_name(path.stem+f'-centers-{len(chunks):03d}.npz')
        if file.exists():
            raise FileExistsError('Position-cover chunk already exists')
        np.savez_compressed(file,centers=centers[start:stop],enclosures=enclosures[start:stop],
                            source_vertex_indices=indices[start:stop])
        if file.stat().st_size>=5_000_000:
            raise ValueError('Position-cover chunk exceeds per-file delivery bound')
        chunks.append(dict(file=file.name,first=start,count=stop-start,bytes=file.stat().st_size,sha256=sha(file)))
    result=dict(schema='finite-closed-active-position-cover-v1',finished=True,
        writer_source_sha256=sha(__file__),producer_source_sha256=producer_source_sha256,
        closed_bundle_sha256=dict(plan=sha(plan_path),assembly=sha(assembly_path),phase0_mesh=sha(mesh_path)),
        active_parameter_cover_complete=True,
        enclosure_definition='For every actual unmarked active point in block i, |F(p)-stored_center_i| <= enclosures[i], including center-coordinate error.',
        active_centers=len(centers),chunks=chunks,
        marked_diameter_upper=float(marked_diameter_upper),
        diameter_scope='Upper bound for the entire marked closed family for every phase, conditional on the producer envelopes.',
        witness_position_error=float(witness_position_error),
        distance_evaluation_error=float(distance_evaluation_error),
        supplied_envelopes=supplied_envelopes,
        supplied_envelopes_contain_saved_samples=bool(supplied_envelopes_contain_saved_samples),
        family=dict(rule='F_alpha(active)=R_about_axis(alpha)*F_0(active at shifted material angle); fixed cap graphs unchanged',
            rotation_axis_xy=axis,phase_interval=[min(plan['phase_angles']),max(plan['phase_angles'])]),
        unmarked_caps=cap_rows,
        geometric_hypotheses=['The full active parameter cover is the one constructed by the producer, not only a tested subset.',
            'The supplied center enclosures and whole-family diameter bound hold for the actual finite map.',
            'Each fixed cap is the stated closed disk plus a graph displacement of at most its marker_height_upper.',
            'All cap marker supports lie strictly inside their disk and their maps are fixed for the entire phase interval.'],
        numerical_position_cover_only=True,task_completed=False)
    path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    return result


def mesh_vertex(path,count,index):
    raw=gzip.decompress(Path(path).read_bytes())
    header_end=raw.index(b'end_header\n')+len(b'end_header\n')
    if not 0<=index<count:
        raise ValueError('Witness vertex is outside the bound mesh')
    values=np.frombuffer(raw,dtype=[('x','<f8'),('y','<f8'),('z','<f8'),('piece','u1')],
                         count=count,offset=header_end)
    row=values[index]
    return np.array([row['x'],row['y'],row['z']]),int(row['piece'])


def disk_distance(point,center,normal,radius):
    displacement=np.asarray(point)-np.asarray(center)
    normal=np.asarray(normal,dtype=float)
    if not np.all(np.isfinite(normal)) or abs(np.linalg.norm(normal)-1)>1e-14:
        raise ValueError('The declared cap plane normal must be a unit vector')
    signed=float(np.dot(displacement,normal))
    horizontal=float(np.linalg.norm(displacement-signed*normal))
    return math.hypot(signed,max(0.,horizontal-radius))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--cover',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--phase',type=float,default=math.pi/2)
    parser.add_argument('--witness-source-index',type=int,
        help='Default: zero-angle core vertex in the canonical mirrored ring mesh')
    parser.add_argument('--rotation-position-error',type=float,
        help='Additional rotation-evaluation position error; default is the source error except for an exact origin-centered quarter turn')
    args=parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Refusing to overwrite a held Hausdorff report')
    packet=read(args.cover)
    if packet.get('schema')!='finite-closed-active-position-cover-v1' or not packet.get('finished') or not packet.get('active_parameter_cover_complete'):
        raise ValueError('A complete bound active position cover is required')
    plan_path,assembly_path,mesh_path=bundle_paths(args.directory)
    plan,assembly=read(plan_path),read(assembly_path)
    for key,path in [('plan',plan_path),('assembly',assembly_path),('phase0_mesh',mesh_path)]:
        if sha(path)!=packet['closed_bundle_sha256'][key]:
            raise ValueError('Position-cover packet belongs to another closed '+key)
    index=args.witness_source_index
    if index is None:
        if not plan['upper_rings'] or plan['upper_rings'][0]['kind']!='prefix' or plan['upper_rings'][0]['coordinate']!=0:
            raise ValueError('Default witness requires a canonical zero-core first upper ring')
        index=(len(plan['upper_rings'])-1)*plan['angular']
    source,label=mesh_vertex(mesh_path,plan['vertices'],index)
    if label!=0:
        raise ValueError('Witness source must be an actual moving active vertex')
    phase_interval=packet['family']['phase_interval']
    if not phase_interval[0]<=args.phase<=phase_interval[1]:
        raise ValueError('Witness phase is outside the declared family interval')
    axis=np.asarray(packet['family']['rotation_axis_xy'],dtype=float)
    witness=source.copy()
    exact_quarter_turn=(args.phase==math.pi/2 and np.array_equal(axis,np.zeros(2)))
    if exact_quarter_turn:
        witness[:2]=[-source[1],source[0]]
    else:
        co,si=math.cos(args.phase),math.sin(args.phase)
        rotation=np.array([[co,-si],[si,co]])
        witness[:2]=axis+rotation@(source[:2]-axis)
    source_error=float(packet['witness_position_error'])
    rotation_error=(0. if exact_quarter_turn else source_error) if args.rotation_position_error is None else args.rotation_position_error
    error=source_error+rotation_error
    distance_error=float(packet['distance_evaluation_error'])
    if min(source_error,rotation_error)<0 or not math.isfinite(error):
        raise ValueError('Finite nonnegative witness evaluation budgets required')
    if not math.isfinite(distance_error) or distance_error<0:
        raise ValueError('Finite nonnegative distance-evaluation error required')
    active_min=math.inf
    active_worst=None
    counted=0
    for chunk in packet['chunks']:
        path=args.cover.parent/chunk['file']
        if sha(path)!=chunk['sha256'] or chunk['first']!=counted:
            raise ValueError('Position-cover chunk hash/order differs')
        with np.load(path,allow_pickle=False) as data:
            centers=data['centers'];enclosures=data['enclosures'];indices=data['source_vertex_indices']
        if centers.shape!=(chunk['count'],3) or enclosures.shape!=(chunk['count'],) or indices.shape!=(chunk['count'],):
            raise ValueError('Position-cover chunk shape differs')
        if not np.all(np.isfinite(centers)) or not np.all(np.isfinite(enclosures)) or np.any(enclosures<0):
            raise ValueError('Invalid active position or enclosure value')
        lower=np.linalg.norm(centers-witness,axis=1)-enclosures-error-distance_error
        j=int(np.argmin(lower))
        if float(lower[j])<active_min:
            active_min=float(lower[j])
            active_worst=dict(cover_index=counted+j,source_vertex_index=int(indices[j]),
                center=centers[j].tolist(),position_ball_radius=float(enclosures[j]),
                point_to_center_distance=float(np.linalg.norm(centers[j]-witness)))
        counted+=chunk['count']
    if counted!=packet['active_centers']:
        raise ValueError('Position cover lost an active chunk')
    caps=[]
    for cap in packet['unmarked_caps']:
        if cap['radius']<=0 or cap['marker_height_upper']<0 or not all(math.isfinite(v) for v in cap['center']):
            raise ValueError('Invalid complete cap geometry or marker height bound')
        distance=disk_distance(witness,cap['center'],cap['normal'],cap['radius'])
        lower=distance-error-distance_error-cap['marker_height_upper']
        caps.append(dict(**cap,distance_to_unmarked_disk=distance,distance_to_marked_cap_lower=lower))
    lower=max(0.,min([active_min]+[row['distance_to_marked_cap_lower'] for row in caps]))
    diameter=float(packet['marked_diameter_upper'])
    if not math.isfinite(diameter) or diameter<=0:
        raise ValueError('A finite positive entire-family diameter upper bound is required')
    if len(caps)!=2 or any(row['radius']<=0 for row in caps):
        raise ValueError('Two complete positive-radius fixed caps required')
    # The canonical bundle uses equal-radius coaxial horizontal disks. Their
    # matching boundary points are outside all marker supports and are fixed.
    coaxial=(caps[0]['center'][:2]==caps[1]['center'][:2]==axis.tolist()
             and caps[0]['radius']==caps[1]['radius']
             and all(row['normal']==[0.,0.,1.] for row in caps)
             and all(row['marker_supports_strictly_inside_circle'] for row in caps))
    if not coaxial:
        raise ValueError('The fixed-hold witness requires the declared canonical coaxial cap geometry')
    hold_lower=max(0.,abs(caps[1]['center'][2]-caps[0]['center'][2])-distance_error)
    consistent=bool(packet['supplied_envelopes_contain_saved_samples'])
    result=dict(schema='actual-closed-held-Hausdorff-cover-witness-v1',finished=True,
        source_sha256=sha(__file__),position_cover_sha256=sha(args.cover),
        closed_bundle_sha256=packet['closed_bundle_sha256'],
        witness=dict(source_vertex_index=index,source_phase0_position=source.tolist(),
            phase=args.phase,rotated_position=witness.tolist(),position_error=error,
            source_position_error=source_error,rotation_position_error=rotation_error,
            exact_origin_centered_quarter_turn=exact_quarter_turn,
            membership='The true source is an active point of S_0; the exact axial family rule places its rotated image in S_alpha.'),
        active_distance_lower=active_min,limiting_active_block=active_worst,cap_distance_bounds=caps,
        distance_evaluation_error=distance_error,
        delta_hold_lower=lower,whole_marked_family_diameter_upper=diameter,
        delta_hold_over_D_lower=lower/diameter,
        fixed_H_diameter_lower=hold_lower,fixed_H_over_D_lower=hold_lower/diameter,
        held_amplitude_threshold_passed=bool(consistent and lower>=.2*diameter),
        fixed_H_diameter_threshold_passed=bool(consistent and hold_lower>=.2*diameter),
        genuine_image_change_conditionally_established=bool(consistent and lower>0),
        supplied_envelopes_contain_saved_samples=consistent,
        proof='For every active block, dist(x,F(C_i)) >= computed_distance(x_tilde,c_i)-e_i-epsilon_x-epsilon_distance. For each cap, computed disk distance minus marker height, epsilon_x and epsilon_distance bounds the entire marked graph. The minimum covers all of S_0. Since x belongs to S_alpha, d_H(S_alpha,S_0) is at least this minimum.',
        euclidean_registration_distance_certified=False,
        exact_continuous_envelopes_certified_here=False,task_completed=False,
        limitations=['The source point and all comparison blocks belong to the same bound whole closed bundle.',
            'All active parameter blocks and both entire fixed caps are used; a point-cloud nearest-neighbor distance alone is not used.',
            'Whole-family D, position enclosures, fixed-cap geometry and the axial family identity are producer inputs.',
            'A positive held witness proves image change, but delta_E still requires the independent R238 hypotheses.',
            'This report does not assert a new accepted BVP, new tail, closed C2 immersion or exact same-g limit.'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),delta_hold_lower=lower,ratio_lower=lower/diameter,
                         amplitude_passed=result['held_amplitude_threshold_passed'])),flush=True)


if __name__=='__main__':
    main()
