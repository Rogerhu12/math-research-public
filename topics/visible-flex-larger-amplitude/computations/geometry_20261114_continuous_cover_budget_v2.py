#!/usr/bin/env python3
"""Apply the R37/R241 cover with diagonal paths and prefix normal cones.

The unmarked base family differs only by a rigid axial rotation. This program
checks a covering budget for that static base, then the R24 weak-marker cost.
The original v1 remains unchanged. This version uses sharper paths and a
continuous normal-cone exclusion at actually evaluated prefix centers.
Its K, metric, tail-slope and coordinate-error envelopes are numerical inputs,
not interval certificates. It reports uncovered parameter blocks so the same
calculation can be repeated on a finer fixed-map display grid.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from collections import Counter
import gzip
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.spatial import cKDTree
from exact_20261114_refined_tail_adapter import module, sha

HERE = Path(__file__).resolve().parent


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def load_mesh(path, plan):
    raw = gzip.decompress(path.read_bytes())
    header_end = raw.index(b'end_header\n')+len(b'end_header\n')
    vertex = np.frombuffer(raw, dtype=[('x','<f8'),('y','<f8'),('z','<f8'),('piece','u1')],
                           count=plan['vertices'], offset=header_end)
    return np.stack([vertex[k] for k in ('x','y','z')], axis=1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    for key in ('checkpoint','source-topic','port','out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--curvature-upper', type=float, default=8.35)
    parser.add_argument('--relative-metric-upper', type=float, default=1e-6)
    parser.add_argument('--tail-slope-upper', type=float, default=.4)
    parser.add_argument('--radius-lipschitz-upper', type=float, default=1.)
    parser.add_argument('--position-error', type=float, default=1e-12)
    parser.add_argument('--radial-stride', type=int, default=1)
    parser.add_argument('--angular-stride', type=int, default=1)
    parser.add_argument('--witness-limit', type=int, default=128)
    parser.add_argument('--normal-angle-error', type=float, default=1e-10)
    parser.add_argument('--normal-batch', type=int, default=8)
    parser.add_argument('--disable-normal-cones', action='store_true')
    args = parser.parse_args()
    start = time.monotonic()
    K, eta, w_bound, position_error = (args.curvature_upper, args.relative_metric_upper,
                                      args.tail_slope_upper, args.position_error)
    if min(K, args.radial_stride, args.angular_stride,args.normal_batch) <= 0 or min(eta,w_bound,position_error,args.radius_lipschitz_upper,args.normal_angle_error) < 0:
        raise ValueError('Positive curvature/strides and nonnegative envelopes required')
    if args.out.exists():
        raise FileExistsError('Refusing to overwrite a coverage result')
    plan_path = args.directory/'refined-A-closed-plan.json'
    assembly_path = args.directory/'refined-A-closed-assembly.json'
    mesh_path = args.directory/'refined-A-closed-phase0.ply.gz'
    background_path = args.directory/'background.json'
    if not background_path.exists():
        background_path = args.directory/'refined-A-closed-background.json'
    plan, assembly, background = map(read, (plan_path,assembly_path,background_path))
    if assembly['inputs']['plan']['sha256'] != sha(plan_path):
        raise ValueError('Assembly and plan differ')
    phase0 = next(row for row in assembly['files'] if row['t'] == 0)
    if phase0['sha256'] != sha(mesh_path):
        raise ValueError('Mesh and assembly differ')
    if plan['inputs']['checkpoint']['sha256'] != sha(args.checkpoint):
        raise ValueError('Prefix checkpoint differs from the closed plan')
    pb = module('coverage_prefix_loader', HERE/'geometric-checkpoint-core-pullback.py')
    saved, _ = pb.load_saved(args.checkpoint,args.source_topic,args.port,
                            angular=int(read(args.checkpoint)['config']['angular']))
    N, upper = plan['angular'], plan['upper_rings']
    if N % args.angular_stride:
        raise ValueError('Angular stride must divide the display grid')
    ntheta = N//args.angular_stride
    if ntheta < 8:
        raise ValueError('At least eight angular cells are required')
    cloud = load_mesh(mesh_path, plan)
    R = 2*len(upper)-1
    rings = cloud[:R*N].reshape(R,N,3)
    L, cut, cuff = plan['prefix_end'], plan['cut'], plan['cuff']
    meridian_factor = math.hypot(1,w_bound)
    length_factor = math.sqrt(1+eta)
    u_cuff = L+meridian_factor*(cut-cuff)
    u_pole = u_cuff+cuff
    H = assembly['mean_gauge']['upper_cap_height']
    active = [i for i,row in enumerate(upper) if row['kind'] != 'cap' and not row.get('cuff')]
    selected = sorted(set(active[::args.radial_stride]+[active[0],active[-1]]))
    for kind in ('prefix','tail','collar'):
        which = [i for i in active if upper[i]['kind'] == kind]
        if which:
            selected = sorted(set(selected+[which[0],which[-1]]))
    descriptors = []
    for side in (-1,1):
        for i in selected:
            if side == -1 and i == 0:
                continue
            row = upper[i]
            coordinate = row['coordinate']
            if row['kind'] == 'prefix':
                u, radius = coordinate, float(saved.flow.profile(np.array([coordinate]))[0][0])
            else:
                u, radius = L+meridian_factor*(cut-coordinate), coordinate
            descriptors.append(dict(u=side*u, radius=radius, kind=row['kind'],
                                    coordinate=coordinate, side=side,
                                    source_ring=len(upper)-1+side*i))
    descriptors.sort(key=lambda row:row['u'])
    us = np.array([row['u'] for row in descriptors])
    radii = np.array([row['radius'] for row in descriptors])
    boundaries = np.r_[-u_cuff,(us[:-1]+us[1:])/2,u_cuff]
    radial_half = np.maximum(us-boundaries[:-1],boundaries[1:]-us)
    if np.any(radial_half < 0) or not np.all(np.diff(us) > 0):
        raise ValueError('Nonordered active meridian cells')
    # Supplied reference-profile budget |a'|<=radius_lipschitz_upper.
    # The u coordinate above only stretches tail meridian lengths.
    angular_half = math.pi/ntheta
    h_ring = length_factor*np.hypot(radial_half,(radii+args.radius_lipschitz_upper*radial_half)*angular_half)
    indices = np.array([row['source_ring'] for row in descriptors])
    angles = np.arange(0,N,args.angular_stride)
    points = rings[indices][:,angles].reshape(-1,3)
    intrinsic_h = np.repeat(h_ring,ntheta)
    u = np.repeat(us,ntheta)
    a_radius = np.repeat(radii,ntheta)
    theta = np.tile(2*math.pi*angles/N,len(indices))
    active_count = len(points)
    # Each unmarked cap is covered as one full flat disk, not thousands of
    # tiny near-coincident display triangles. Its center and path radius are
    # exact in the finite plan's mathematical definition.
    points = np.vstack([points,[0,0,-H],[0,0,H]])
    intrinsic_h = np.r_[intrinsic_h,cuff,cuff]
    u = np.r_[u,-u_pole,u_pole]
    a_radius = np.r_[a_radius,0.,0.]
    theta = np.r_[theta,0.,0.]
    enclosure = intrinsic_h+position_error

    # R37's radial extremum proof works cellwise with h_i. Caps have the
    # sharper explicit radius bound; do not charge their full disk radius
    # to the body's small diameter margin.
    body_ball = np.linalg.norm(points[:active_count],axis=1)+position_error+K*intrinsic_h[:active_count]**2/2
    cap_ball = math.hypot(H,cuff)
    base_D_upper = 2*max(float(body_ball.max()),cap_ball)
    markers = plan['fixed_cap']['markers']
    marker_A = max(abs(row['height']) for row in markers)
    marker_G = max(8*abs(row['height'])/row['radius'] for row in markers)
    marker_K = max(8*abs(row['height'])/row['radius']**2 for row in markers)
    support_radius = max(math.hypot(*row['center'])+row['radius'] for row in markers)
    body_radius_lower = float(np.min(np.linalg.norm(points[:active_count,:2],axis=1)-enclosure[:active_count]))
    separation = min(cuff-support_radius,body_radius_lower-support_radius,2*H)
    marked_D_upper = base_D_upper+2*marker_A
    target_tau = .03*marked_D_upper
    inverse_base_budget = ((1-2*marker_A/separation)**2/target_tau
                           -2*marker_G/separation-4*marker_A/separation**2) if separation > 0 else -1.
    base_tau = 1/inverse_base_budget if inverse_base_budget > 0 else 1/K
    curvature_gate = K*base_tau <= 1
    marker_gate = (inverse_base_budget > 0 and separation > 2*marker_A and marker_K <= 1/target_tau)

    normal_vectors = np.zeros_like(points)
    normal_available = np.zeros(len(points),dtype=bool)
    normal_info = dict(enabled=not args.disable_normal_cones, prefix_centers=0,
                       checked_existing_normals=0, maximum_existing_angle_difference=None)
    if not args.disable_normal_cones:
        # Only first jets are needed. Their height derivative uses the SAME
        # full angular mean as the assembly. The mean height antiderivative
        # and its second derivative do not enter a surface normal.
        normal_angles = 2*math.pi*angles/N
        meanN = max(512,16*(3*saved.M+1))
        _, B1, B2 = saved.flow.basis(meanN)
        old = module('coverage_v2_material_jets',HERE/'geometric-closed-assembly.py')
        coordinates = sorted(set(row['coordinate'] for row in descriptors if row['kind']=='prefix'))
        prefix_normals = {}
        inverse_residual = 0.
        for first in range(0,len(coordinates),args.normal_batch):
            ss = np.asarray(coordinates[first:first+args.normal_batch])
            frame, _, _ = saved.flow.velocity_s(ss,saved.sol.sol(ss),saved.sol.sol(ss,1),B1,B2)
            hp = np.mean(frame['V'][:,:,2],axis=1)
            zeros = np.zeros(len(ss))
            jets, inv, _ = old.material_jets(saved,ss,normal_angles,(zeros,hp,zeros))
            inverse_residual = max(inverse_residual,float(inv))
            normals = np.cross(jets['p1'],jets['s1'])
            lengths = np.linalg.norm(normals,axis=2)
            if not np.all(np.isfinite(lengths)) or np.any(lengths<=0):
                raise ValueError('Prefix normal evaluation is not a regular finite immersion')
            normals /= lengths[:,:,None]
            for coordinate,value in zip(ss,normals):
                prefix_normals[float(coordinate)] = value
        for i,row in enumerate(descriptors):
            if row['kind']!='prefix':
                continue
            sl = slice(i*ntheta,(i+1)*ntheta)
            normal_vectors[sl] = prefix_normals[row['coordinate']]
            normal_vectors[sl,2] *= row['side']
            normal_available[sl] = True
        normal_info.update(prefix_centers=int(normal_available.sum()),mean_angular=meanN,
            maximum_chart_inverse_residual=inverse_residual,
            definition='The existing SavedPrefix physical quintic, unchanged material chart and unchanged full angular mean derivative; no new state interpolation or height primitive.')
        # Verify the new normal evaluator against every common stored normal.
        normal_path = args.directory/'refined-A-closed-normal-samples.npz'
        normal_info['packet_sha256'] = sha(normal_path)
        if normal_info['packet_sha256'] != assembly['normal_samples']['sha256']:
            raise ValueError('Normal packet and assembly differ')
        with np.load(normal_path,allow_pickle=False) as packet:
            stored_indices = packet['moving_source_indices']
            stored_normals = packet['moving_normal']
        stored = {int(index):value for index,value in zip(stored_indices,stored_normals)}
        checked = []
        for i,row in enumerate(descriptors):
            if row['kind']!='prefix':
                continue
            for j,angle_index in enumerate(angles):
                source_index = int(row['source_ring']*N+angle_index)
                if source_index not in stored:
                    continue
                value = stored[source_index]
                value = value/np.linalg.norm(value)
                candidate = normal_vectors[i*ntheta+j]
                angle_error = math.atan2(float(np.linalg.norm(np.cross(candidate,value))),
                                         abs(float(np.dot(candidate,value))))
                checked.append(angle_error)
        if not checked:
            raise ValueError('No common stored prefix normals for the independent evaluator check')
        normal_info.update(checked_existing_normals=len(checked),
            maximum_existing_angle_difference=max(checked))
    normal_vectors[-2:] = [[0.,0.,-1.],[0.,0.,1.]]
    normal_available[-2:] = True
    # For p in cell i, the tangent projector differs from the stored-center
    # projector by at most sin(min(pi/2,K*h_i+normal_angle_error)).
    cone_sine = np.sin(np.minimum(math.pi/2,K*intrinsic_h+args.normal_angle_error))
    cone_sine[-2:] = 0. # exact unmarked flat caps
    tree = cKDTree(points)
    near_pairs = unresolved = 0
    short_path_count = distance_count = planar_cap_count = normal_cone_count = 0
    minimum_normal_cone_positive_slack = math.inf
    failures_by_piece = Counter()
    worst = []
    threshold = math.pi/K
    max_enclosure = float(enclosure.max())
    # Within one unmarked planar cap every nonzero chord is tangent to its
    # plane, hence cannot be a double normal. This exact R37 third gate does
    # not require the cap's diameter to fit in the short-path window.
    self_uncovered = np.flatnonzero(2*intrinsic_h[:active_count] >= threshold)
    planar_cap_self_cells = 2
    piece_names = ['prefix','tail','collar','cap']
    piece_codes = np.r_[np.repeat([piece_names.index(row['kind']) for row in descriptors],ntheta),3,3]
    horizontal_lower = np.linalg.norm(points[:active_count,:2],axis=1)-enclosure[:active_count]
    cap_active_uncovered = 0

    def describe(index):
        if index >= active_count:
            return dict(kind='cap',side=-1 if index == active_count else 1)
        ring, angular = divmod(int(index),ntheta)
        return dict(**descriptors[ring], theta=float(theta[index]),
                    source_vertex=int(indices[ring]*N+angles[angular]),
                    intrinsic_cover_radius=float(intrinsic_h[index]))

    for index in self_uncovered:
        kind = piece_names[piece_codes[index]]
        failures_by_piece[kind+'--'+kind] += 1
        worst.append(dict(indices=[int(index),int(index)],
            distance_slack=-float(2*enclosure[index]+2*base_tau),
            path_upper=float(2*intrinsic_h[index]),short_path_threshold=threshold,
            left=describe(int(index)),right=describe(int(index))))
    unresolved = len(self_uncovered)
    worst = sorted(worst,key=lambda row:row['distance_slack'])[:args.witness_limit]

    for first in range(0,len(points),64):
        batch = points[first:first+64]
        neighborhoods = tree.query_ball_point(batch,2*base_tau+enclosure[first:first+len(batch)]+max_enclosure)
        for offset, near in enumerate(neighborhoods):
            i = first+offset
            j = np.array([v for v in near if v > i],dtype=np.int64)
            if not len(j):
                continue
            near_pairs += len(j)
            center_distance = np.linalg.norm(points[j]-points[i],axis=1)
            distance_slack = center_distance-enclosure[i]-enclosure[j]-2*base_tau
            far = distance_slack >= 0
            distance_count += int(far.sum())
            j, distance_slack = j[~far],distance_slack[~far]
            if not len(j):
                continue
            # If the whole active block lies outside the cap cylinder, no
            # chord to the flat cap can be perpendicular to its tangent
            # plane. Only an actually paid position-ball lower bound is used.
            cap_excluded = np.zeros(len(j),dtype=bool)
            if i < active_count and horizontal_lower[i] > cuff:
                cap_excluded = j >= active_count
            planar_cap_count += int(cap_excluded.sum())
            j, distance_slack = j[~cap_excluded],distance_slack[~cap_excluded]
            if not len(j):
                continue
            angle = abs(theta[j]-theta[i])
            angle = np.minimum(angle,2*math.pi-angle)
            du = abs(u[j]-u[i])
            radius_upper = np.minimum(a_radius[j],a_radius[i])+args.radius_lipschitz_upper*du
            l1_path = du+np.minimum(a_radius[j],a_radius[i])*angle
            diagonal_path = np.hypot(du,radius_upper*angle)
            center_path = length_factor*np.minimum(l1_path,diagonal_path)
            via_top = length_factor*(2*u_pole-u[j]-u[i])
            via_bottom = length_factor*(2*u_pole+u[j]+u[i])
            center_path = np.minimum(center_path,np.minimum(via_top,via_bottom))
            path_upper = center_path+intrinsic_h[i]+intrinsic_h[j]
            short = path_upper < threshold
            short_path_count += int(short.sum())
            # A strict nonzero tangent component at either endpoint rules
            # out both an intersection and a double-normal chord. This is
            # R241's continuous normal-cone gate, not a finite-pair sample.
            cone_slack = np.full(len(j),-math.inf)
            pending = np.flatnonzero(~short)
            if len(pending) and not args.disable_normal_cones:
                other = j[pending]
                chord = points[other]-points[i]
                chord_length = np.linalg.norm(chord,axis=1)
                position_budget = enclosure[i]+enclosure[other]
                if normal_available[i]:
                    scalar = chord@normal_vectors[i]
                    tangent = np.sqrt(np.maximum(0.,chord_length**2-scalar**2))
                    cone_slack[pending] = tangent-position_budget-cone_sine[i]*chord_length
                available = normal_available[other]
                if np.any(available):
                    scalar = np.einsum('ij,ij->i',chord[available],normal_vectors[other[available]])
                    tangent = np.sqrt(np.maximum(0.,chord_length[available]**2-scalar**2))
                    second = tangent-position_budget[available]-cone_sine[other[available]]*chord_length[available]
                    pp = pending[available]
                    cone_slack[pp] = np.maximum(cone_slack[pp],second)
            cone_pass = (~short)&(cone_slack>0)
            normal_cone_count += int(cone_pass.sum())
            if np.any(cone_pass):
                minimum_normal_cone_positive_slack = min(minimum_normal_cone_positive_slack,float(cone_slack[cone_pass].min()))
            bad = np.flatnonzero((~short)&(~cone_pass))
            unresolved += len(bad)
            if len(bad):
                cap_active_uncovered += int(np.count_nonzero(j[bad] >= active_count)) if i < active_count else 0
                counts = np.bincount(piece_codes[j[bad]],minlength=4)
                for code,count in enumerate(counts):
                    if count:
                        kinds = sorted([piece_names[piece_codes[i]],piece_names[code]])
                        failures_by_piece['--'.join(kinds)] += int(count)
                for k in bad[np.argsort(distance_slack[bad])[:4]]:
                    worst.append(dict(indices=[i,int(j[k])],
                        distance_slack=float(distance_slack[k]),
                        path_upper=float(path_upper[k]),short_path_threshold=threshold,
                        normal_cone_slack=float(cone_slack[k]) if np.isfinite(cone_slack[k]) else None,
                        left=describe(i),right=describe(int(j[k])),
                        center_points=[points[i].tolist(),points[j[k]].tolist()]))
                worst = sorted(worst,key=lambda row:row['distance_slack'])[:args.witness_limit]
        if first % 2048 == 0:
            print(json.dumps(dict(event='continuous_cover_budget',completed_centers=min(first+64,len(points)),
                centers=len(points),uncovered_pairs=unresolved,seconds=time.monotonic()-start)),flush=True)
    sampled_metric = max(row['metric_relative_operator_max'] for row in assembly['sampled_piece_jets'].values())
    sampled_K = max(row['curvature'] for row in assembly['sampled_piece_jets'].values())
    sampled_w = max(abs(row['w']) for row in background['rows'])
    prefix_coordinates = np.array([row['coordinate'] for row in upper if row['kind'] == 'prefix'])
    sampled_radius_lipschitz = max(1.,float(np.max(abs(saved.flow.profile(prefix_coordinates)[1]))))
    samples_contained = (sampled_K <= K and sampled_metric <= eta and sampled_w <= w_bound+1e-14
                         and sampled_radius_lipschitz <= args.radius_lipschitz_upper
                         and (args.disable_normal_cones or normal_info['maximum_existing_angle_difference'] <= args.normal_angle_error))
    result = dict(schema='R37-R241-actual-closed-spatial-cover-budget-v2',finished=True,
        source_sha256=sha(__file__),
        input_sha256={str(p):sha(p) for p in (plan_path,assembly_path,mesh_path,background_path,args.checkpoint,args.port)},
        supplied_envelopes=dict(curvature=K,relative_metric_operator=eta,tail_abs_slope=w_bound,
            evaluation_position_error=position_error,reference_radius_lipschitz=args.radius_lipschitz_upper,
            evaluation_normal_angle_error=args.normal_angle_error),
        actual_saved_samples=dict(curvature=sampled_K,relative_metric_operator=sampled_metric,tail_abs_slope=sampled_w,
                                  reference_radius_lipschitz=sampled_radius_lipschitz),
        supplied_envelopes_contain_saved_samples=samples_contained,
        grid=dict(radial_stride=args.radial_stride,angular_stride=args.angular_stride,
                  active_rings=len(descriptors),angles=ntheta,cover_centers=len(points),
                  maximum_intrinsic_active_radius=float(intrinsic_h[:active_count].max())),
        conditional_diameter=dict(unmarked_upper=base_D_upper,marked_upper=marked_D_upper,
            largest_body_enclosures=[dict(center=int(i),radius_upper=float(body_ball[i]),
                position_norm=float(np.linalg.norm(points[i])),description=describe(int(i)))
                for i in np.argsort(body_ball)[-8:][::-1]],
            vertex_cloud_diameter=assembly['vertex_cloud_diameter_lower'],
            rule='At a global radius maximum in cell i: R<=|stored_center_i|+position_error+K*h_i^2/2. Caps use sqrt(H^2+r_c^2).'),
        marker_budget=dict(height=marker_A,gradient=marker_G,Hessian=marker_K,
            support_max_horizontal_radius=support_radius,active_horizontal_radius_lower=body_radius_lower,
            support_separation=separation,target_reach=target_tau,required_unmarked_reach=base_tau,
            curvature_times_required_reach=K*base_tau,curvature_gate=curvature_gate,marker_gate=marker_gate),
        coverage=dict(total_center_pairs=len(points)*(len(points)-1)//2,
            near_center_pairs_enumerated=near_pairs,distance_pass_in_enumerated=distance_count,
            short_path_pass=short_path_count,normal_cone_pass=normal_cone_count,
            minimum_normal_cone_positive_slack=(minimum_normal_cone_positive_slack if math.isfinite(minimum_normal_cone_positive_slack) else None),
            self_cells_uncovered=len(self_uncovered),uncovered=unresolved,
            planar_cap_self_cells_excluded=planar_cap_self_cells,
            planar_cap_active_pairs_excluded=planar_cap_count,
            cap_active_uncovered=cap_active_uncovered,
            non_cap_uncovered=unresolved-cap_active_uncovered,
            uncovered_by_piece=dict(failures_by_piece),worst=worst,
            outside_query_ball_rule='Center distance >2*tau+e_i+max(e) implies full patch separation >=2*tau.'),
        normal_evaluation=normal_info,
        numerical_cover_budget_passed=bool(unresolved == 0 and curvature_gate and marker_gate and samples_contained),
        entire_phase_circle_reduced_to_static_base=True,
        complete_pair_gates_imply_embedding_for_regular_closed_C2_immersion=bool(unresolved==0 and samples_contained),
        continuous_reach_interval_certificate=False,task_completed=False,
        limitations=['The supplied envelopes are numerical inputs; this run does not derive interval bounds for them.',
            'Repeat on finer grids of the same map and compare uncovered blocks and margins; a different BVP design is not a refinement.',
            'The static base is the closed finite map with all four marker heights set to zero; R24 pays the fixed marker cost.',
            'Closed C2 regular immersion remains a geometric input. A complete cover by these R241 gates also implies injectivity; a watertight PLY alone does not establish C2 or regularity.',
            'Passing this reach budget does not establish the required amplitude or an exact same-g limit.'],
        seconds=time.monotonic()-start)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),budget_passed=result['numerical_cover_budget_passed'],
                         uncovered=unresolved,K_tau=K*base_tau,seconds=result['seconds'])),flush=True)


if __name__ == '__main__':
    main()
