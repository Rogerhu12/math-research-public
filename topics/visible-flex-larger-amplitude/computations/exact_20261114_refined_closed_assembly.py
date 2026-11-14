#!/usr/bin/env python3
"""Finite closed-family assembly using the measured background-preserving tail.

Retains the saved physical quintic prefix and complete original mean; uses a
fixed .01-wide tail correction, the explicit finite inner collar, and R14
weak fixed markers. All phase formulas are defined continuously. Spatial
reach checks and metric audits here remain finite samples, not certificates.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import json
import math
import time
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
from exact_20261114_refined_tail_adapter import (
    RefinedTail, RefinedAssembly, complete_prefix_heights, module, sha, synth)

HERE = Path(__file__).resolve().parent


def read(path):
    b = Path(path).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2] == b'\x1f\x8b' else b)


def write(path, obj):
    with Path(path).open('x') as f:
        json.dump(obj, f, indent=2, allow_nan=False)
        f.write('\n')


def load(args):
    pb = module('exact_refined_closed_pullback', HERE/'geometric-checkpoint-core-pullback.py')
    meta = read(args.checkpoint)
    saved, loader = pb.load_saved(args.checkpoint, args.source_topic, args.port,
                                  angular=int(meta['config']['angular']))
    if not saved.rec.get('solver_success') or not saved.rec.get('actual_tail') or saved.sol.sol.c.shape[0] != 6:
        raise ValueError('An accepted actual-tail physical quintic is required')
    if loader.source_revision(args.source_topic) != '869436630c99aa5a68afb55bd8877c826034d117':
        raise ValueError('Pinned source revision differs')
    config = read(args.config)
    if config.get('orientation') != 1 or config.get('spacing') != 2 or saved.mode != 2:
        raise ValueError('Current adapter requires the positive-r, spacing-two family')
    tail = RefinedTail(args.complete)
    if sha(args.config) not in tail.meta['input_sha256'].values():
        raise ValueError('Readout config binding differs')
    actual_response = args.checkpoint.parent/Path(saved.rec['actual_tail']['final_response']).name
    if not actual_response.exists() or sha(actual_response) not in tail.meta['input_sha256'].values():
        raise ValueError('Readout must belong to this accepted prefix actual-tail response, not only the same g')
    original_tail = saved.rec['actual_tail']['config']
    for key in ('rCut','wCut','width','curvatureBound','orientation','modes','spacing','depth','quadrature'):
        if config.get(key) != original_tail.get(key):
            raise ValueError('Actual prefix/tail configuration differs at '+key)
    return saved, tail, config


def anchors(values, lo, hi):
    return np.unique(np.r_[lo,np.asarray(values,float),hi])


def plan(args):
    saved, tail, config = load(args)
    old = module('exact_refined_closed_old', HERE/'geometric-closed-assembly.py')
    cut, inner = float(tail.r[-1]), float(tail.r[0])
    cuff = config['rCut']-config['width']
    if not 0 < args.cut_correction_width < cut-inner:
        raise ValueError('Outer correction must fit in the represented finite tail')
    if args.angular < 64 or args.angular % (4*(args.phase_samples-1)):
        raise ValueError('Mesh angular grid must resolve all requested material phase shifts exactly')
    s = old.distinct(np.r_[np.linspace(0,saved.flow.end,args.prefix_intervals+1),saved.flow.breaks],0,saved.flow.end)
    cell_edges = [row['geometry']['r'] for row in tail.meta['rows']
                  if row.get('rawSegment') == 0 and row.get('x') == 0]
    r = anchors(np.r_[np.linspace(inner,cut,args.tail_intervals+1),cell_edges,cut-args.cut_correction_width],inner,cut)
    collar = np.linspace(cuff,inner,args.collar_intervals+1)
    k = args.marker_k
    if k <= 0:
        raise ValueError('Positive weak marker scale required')
    centers = [[cuff/2,0.],[0.,cuff/2],[-cuff/2,0.],[0.,0.]]
    markers = [dict(index=i,upper=i<4,center=centers[i-1],radius=cuff/(8*i),
                    kappa=i*i*k,height=k*cuff*cuff/512) for i in range(1,5)]
    marker_radii = []
    for row in markers:
        center = np.linalg.norm(row['center'])
        marker_radii.extend([center,center+row['radius']/2,center+row['radius']])
        if center:
            marker_radii.extend([center-row['radius']/2,center-row['radius']])
    cap = anchors(np.r_[np.linspace(0,cuff,args.cap_intervals+1),marker_radii],0,cuff)
    upper = [dict(kind='prefix',coordinate=float(v)) for v in s]
    upper[-1]['cut'] = True
    upper += [dict(kind='tail',coordinate=float(v)) for v in r[-2::-1]]
    upper += [dict(kind='collar',coordinate=float(v)) for v in collar[-2::-1]]
    upper[-1]['cuff'] = True
    upper += [dict(kind='cap',coordinate=float(v)) for v in cap[-2:0:-1]]
    rings = 2*len(upper)-1
    vertices, faces = rings*args.angular+2, 2*rings*args.angular
    if 25*vertices+13*faces+4096 >= 5_000_000:
        raise ValueError('One mesh would exceed 5 MB; reduce display sampling counts')
    paths = dict(checkpoint=args.checkpoint,port=args.port,config=args.config,complete=args.complete)
    result = dict(schema='refined-tail-finite-closed-plan-v1',finished=True,
        source_sha256_at_start=args.source_hash,
        adapter_sha256=sha(HERE/'exact_20261114_refined_tail_adapter.py'),
        inputs={key:dict(file=str(path.resolve()),sha256=sha(path)) for key,path in paths.items()},
        source_revision='869436630c99aa5a68afb55bd8877c826034d117',
        profile_fingerprint=tail.meta['original_profile_fingerprint'],
        cut=cut,cuff=cuff,tail_inner=inner,prefix_end=saved.flow.end,
        cut_correction_width=args.cut_correction_width,
        upper_rings=upper,background_radii=sorted(set(map(float,np.r_[r,collar,cut-args.cut_correction_width]))),
        angular=args.angular,phase_samples=args.phase_samples,
        phase_angles=np.linspace(0,math.pi/2,args.phase_samples).tolist(),
        mesh_phase_indices=[0,(args.phase_samples-1)//2,args.phase_samples-1],
        vertices=vertices,faces=faces,uncompressed_mesh_byte_bound=25*vertices+13*faces+4096,
        fixed_cap=dict(theorem='R14-arbitrarily-weak-gaussian-cap-markers',marker_k=k,markers=markers,
            conditional='The exact rotational metric has no isolated strict Gaussian maxima on active latitude circles. This hypothesis is not asserted for the finite approximate field.'),
        piece_labels={'0':'moving prefix, finite tail and nonzero finite collar','1':'fixed caps outside markers and common cuff','2':'fixed weak markers'},
        phase_rule='For all real alpha, moving F_alpha(s,theta)=R_alpha F_0(s,theta-alpha); fixed caps are unchanged. alpha=pi*t/2 on t in [0,1].',
        mean_rule='Original physical Gauss6 mean primitive anchored once at s=0, full angular rule max(512,16*(3*M+1)); no independent mean resets.',
        exact_infinite_nonlinear_tail=False,exact_common_metric_limit=False)
    output = Path(str(args.out_prefix)+'-plan.json')
    write(output,result)
    print(json.dumps(dict(plan=str(output),vertices=vertices,faces=faces,background_radii=len(result['background_radii']))),flush=True)


def finite_static_pairs(x, normal, tau):
    """All finite same-type pairs: distant pairs positive by |d.n|<=|d|."""
    pairs = cKDTree(x).query_pairs(2*tau,output_type='ndarray')
    minimum, worst, negative = math.inf, None, 0
    for start in range(0,len(pairs),100000):
        p = pairs[start:start+100000]
        d = x[p[:,1]]-x[p[:,0]]
        normal_dot = np.maximum(abs(np.sum(d*normal[p[:,0]],axis=1)),abs(np.sum(d*normal[p[:,1]],axis=1)))
        margin = np.sum(d*d,axis=1)-2*tau*normal_dot
        negative += int(np.count_nonzero(margin<0))
        j = int(np.argmin(margin))
        if margin[j] < minimum:
            minimum = float(margin[j])
            worst = dict(indices=p[j].tolist(),margin=minimum,chord=float(np.linalg.norm(d[j])))
    return dict(points=len(x),all_pairs=len(x)*(len(x)-1)//2,near_pairs=len(pairs),
        negative_sample_pairs=negative,worst=worst,
        distant_pair_rule='All chord lengths >=2*tau have nonnegative normal-chord margin for unit normals.',
        scope='Finite spatial pair sample; common rigid rotations preserve these margins exactly.')


def sampled_geometry(old, jets, E0, G0, inward=False):
    out=old.metric_curvature(jets,E0,G0,inward=inward)
    fr,ft=jets['s1'],jets['p1']
    aa=np.sum(fr*fr,axis=-1)/E0[:,None]-1
    bb=np.sum(fr*ft,axis=-1)/np.sqrt(E0[:,None]*G0[:,None])
    dd=np.sum(ft*ft,axis=-1)/G0[:,None]-1
    out['metric_component_max']=out.pop('metric')
    out['metric_relative_operator_max']=float(np.max((abs(aa+dd)+np.sqrt((aa-dd)**2+4*bb*bb))/2))
    return out


def render(args):
    started=time.monotonic()
    saved,tail,config=load(args)
    p,h=read(args.plan),read(args.heights)
    for key,path in [('checkpoint',args.checkpoint),('port',args.port),('config',args.config),('complete',args.complete)]:
        if p['inputs'][key]['sha256']!=sha(path):
            raise ValueError('Plan input changed: '+key)
    if h['inputs']['plan']['sha256']!=sha(args.plan) or h['profile_fingerprint']!=p['profile_fingerprint']:
        raise ValueError('Source background belongs to another plan')
    old=module('exact_refined_closed_mesh',HERE/'geometric-closed-assembly.py')
    prefix_indices=[i for i,row in enumerate(p['upper_rings']) if row['kind']=='prefix']
    prefix_s=np.array([p['upper_rings'][i]['coordinate'] for i in prefix_indices])
    meanN=max(512,16*(3*saved.M+1))
    heights,mean_info=complete_prefix_heights(saved,prefix_s,meanN,batch=args.mean_batch)
    print(json.dumps(dict(event='complete_prefix_mean',cut_mean=float(heights[0][-1]),seconds=time.monotonic()-started)),flush=True)
    A=RefinedAssembly(saved,tail,p,h,tuple(x[-1] for x in heights))
    N=p['angular'];theta=2*np.pi*np.arange(N)/N
    shape=(len(p['upper_rings']),N,3)
    upper=np.empty(shape);lower=np.empty(shape);un=np.empty(shape);ln=np.empty(shape)
    labels=np.zeros(shape[:-1],np.uint8);lower_labels=labels.copy();audits={};inverse=0.
    for kind in ('prefix','tail','collar','cap'):
        indices=[i for i,row in enumerate(p['upper_rings']) if row['kind']==kind]
        values=np.array([p['upper_rings'][i]['coordinate'] for i in indices])
        if kind=='prefix':
            j,res,_=A.prefix_jets(values,theta,heights);inverse=max(inverse,res)
            upper[indices]=j['pos'];r=saved.flow.profile(values)[0]
            audits[kind]=sampled_geometry(old,j,np.ones(len(values)),r*r)
            un[indices]=np.cross(j['p1'],j['s1'])
        elif kind in ('tail','collar'):
            j=A.tail_jets(values,theta);upper[indices]=j['pos']
            w=np.array([A.height[float(r)]['w'] for r in values])
            audits[kind]=sampled_geometry(old,j,1+w*w,values*values,inward=True)
            un[indices]=np.cross(j['s1'],j['p1'])
        else:
            upper[indices],labels[indices]=A.cap(values,theta,True)
            lower[indices],lower_labels[indices]=A.cap(values,theta,False)
            un[indices]=A.cap_normals(upper[indices],True);ln[indices]=A.cap_normals(lower[indices],False)
        if kind!='cap':
            un[indices]/=np.linalg.norm(un[indices],axis=2)[:,:,None]
            lower[indices]=upper[indices];lower[indices,:,2]*=-1
            ln[indices]=un[indices];ln[indices,:,2]*=-1
    for i,row in enumerate(p['upper_rings']):
        if row.get('cuff'):
            labels[i]=1;lower_labels[i]=1;un[i]=[0.,0.,1.];ln[i]=[0.,0.,-1.]
    core,_,_=A.prefix_jets(np.array([0.]),theta,tuple(x[:1] for x in heights))
    mirror=dict(z_at_core=float(abs(core['pos'][0,:,2]).max()),
        horizontal_s_at_core=float(np.linalg.norm(core['s1'][0,:,:2],axis=1).max()),
        z_ss_at_core=float(abs(core['s2'][0,:,2]).max()))
    baseline=np.concatenate([lower[:0:-1],upper]);normals=np.concatenate([ln[:0:-1],un])
    piece=np.concatenate([lower_labels[:0:-1],labels]);R=len(baseline)
    bottom,bottom_label=A.cap(np.array([0.]),np.array([0.]),False)
    top,top_label=A.cap(np.array([0.]),np.array([0.]),True)
    bottom,top=bottom[0,0],top[0,0]
    faces=[]
    for i in range(R-1):
        for j in range(N):
            aa=i*N+j;bb=i*N+(j+1)%N;cc=(i+1)*N+j;dd=(i+1)*N+(j+1)%N
            faces.extend(((aa,bb,cc),(bb,dd,cc)))
    for j in range(N):
        faces.extend(((R*N,(j+1)%N,j),(R*N+1,(R-1)*N+j,(R-1)*N+(j+1)%N)))
    faces=np.asarray(faces,np.int32)
    all_labels=np.r_[piece.ravel(),bottom_label.ravel(),top_label.ravel()].astype(np.uint8)
    cloud=np.vstack([baseline.reshape(-1,3),bottom,top]);tree=cKDTree(cloud)
    ball=2*float(np.linalg.norm(cloud,axis=1).max())
    ii=int(np.argmax(np.linalg.norm(cloud,axis=1)));jj=int(np.argmax(np.linalg.norm(cloud-cloud[ii],axis=1)));kk=int(np.argmax(np.linalg.norm(cloud-cloud[jj],axis=1)))
    diameter_lower=float(np.linalg.norm(cloud[jj]-cloud[kk]))
    files=[];phase=[];fixed=piece>0
    for index,alpha in enumerate(p['phase_angles']):
        shift=int(round(alpha*N/(2*np.pi)))
        cur=np.roll(baseline,shift,axis=1).copy()
        co,si=np.cos(alpha),np.sin(alpha)
        rotation=np.array([[co,-si,0.],[si,co,0.],[0.,0.,1.]])
        cur=cur@rotation.T
        cur[fixed]=baseline[fixed]
        xyz=np.vstack([cur.reshape(-1,3),bottom,top])
        if index in p['mesh_phase_indices']:
            file=Path(str(args.out_prefix)+f'-phase{index}.ply.gz')
            files.append({**old.ply(file,xyz,faces,all_labels),'alpha':alpha,'t':2*alpha/np.pi})
        forward=tree.query(xyz,workers=1)[0];back=cKDTree(xyz).query(cloud,workers=1)[0]
        H=float(max(forward.max(),back.max()))
        phase.append(dict(alpha=alpha,t=2*alpha/np.pi,vertex_cloud_hausdorff=H,
            ratio_to_vertex_ball_diameter_upper=H/ball,
            fixed_vertices_bitwise_equal=bool(np.array_equal(xyz[all_labels>0],cloud[all_labels>0]))))
    normal_cloud=np.vstack([normals.reshape(-1,3),[0.,0.,-1.],[0.,0.,1.]])
    ring_selection=np.unique(np.r_[np.arange(0,R,args.reach_ring_stride),np.flatnonzero(np.any(piece>0,axis=1))])
    angle_selection=np.arange(0,N,args.reach_angle_stride)
    selected=np.r_[(ring_selection[:,None]*N+angle_selection).ravel(),R*N,R*N+1]
    moving=selected[all_labels[selected]==0];fixed_indices=selected[all_labels[selected]>0]
    packet=Path(str(args.out_prefix)+'-normal-samples.npz')
    np.savez_compressed(packet,moving_xyz=cloud[moving],moving_normal=normal_cloud[moving],
        fixed_xyz=cloud[fixed_indices],fixed_normal=normal_cloud[fixed_indices],
        moving_source_indices=moving,fixed_source_indices=fixed_indices,
        tau=np.array(.03*ball),diameter_vertex_ball_upper=np.array(ball))
    if packet.stat().st_size>=5_000_000:
        raise ValueError('Normal packet exceeds per-file delivery bound')
    phase_reach=module('exact_refined_closed_phase_reach',HERE/'root_phase_reach.py')
    reach=dict(tau=.03*ball,diameter_basis='Finite-cloud ball bound, not a continuous diameter certificate',
        moving_fixed=phase_reach.screen(cloud[moving],normal_cloud[moving],cloud[fixed_indices],normal_cloud[fixed_indices],.03*ball,batch=64),
        moving_moving=finite_static_pairs(cloud[moving],normal_cloud[moving],.03*ball),
        fixed_fixed=finite_static_pairs(cloud[fixed_indices],normal_cloud[fixed_indices],.03*ball))
    reach_file=Path(str(args.out_prefix)+'-all-phase-finite-pairs.json');write(reach_file,reach)
    cut_theta=2*np.pi*np.arange(tail.N)/tail.N
    cj,_,_=A.prefix_jets(np.array([A.L]),cut_theta,tuple(x[-1:] for x in heights))
    tj=A.tail_jets(np.array([A.cut]),cut_theta)
    rs,rss=A.cut_radial_jets['r_s'],A.cut_radial_jets['r_ss']
    targets=dict(pos=tj['pos'],s1=rs*tj['s1'],s2=rs*rs*tj['s2']+rss*tj['s1'],
                 p1=tj['p1'],p2=tj['p2'],sp=rs*tj['sp'])
    seam={key:float(np.max(np.linalg.norm(cj[key]-targets[key],axis=-1))) for key in targets}
    collar_zero=A.perturbation(np.array([A.cuff]),cut_theta)
    collar_inner=A.perturbation(np.array([A.inner]),cut_theta)
    inner_norms={key:float(np.max(np.linalg.norm(v,axis=-1))) for key,v in collar_inner.items()}
    centers=[]
    for row in p['fixed_cap']['markers']:
        centers.append(row['center']+[(1 if row['upper'] else -1)*(A.cap_height+row['height'])])
    affine=float(np.linalg.det(np.array(centers)[:3]-np.array(centers)[3]))
    report=dict(schema='refined-tail-finite-closed-assembly-v1',finished=True,
        source_sha256_at_start=args.source_hash,adapter_sha256=sha(HERE/'exact_20261114_refined_tail_adapter.py'),
        inputs={key:dict(file=str(path.resolve()),sha256=sha(path)) for key,path in [('plan',args.plan),('heights',args.heights)]},
        mean_height=mean_info,mean_gauge=dict(prefix_cut_mean=A.prefix_cut_mean,tail_cut_small_mean=A.tail_cut_mean,
            single_upper_offset=A.offset,upper_cap_height=A.cap_height,whole_lower_sheet_reflected=True),
        prefix_physical_polynomial_degree=5,tail_nodes=len(tail.r),verified_loaded_tail_nodes=len(tail.verified_nodes),
        shared_cut=dict(width=A.W,side='tail radius interval',prefix_untouched=True,
            endpoint_definition=A.cut_radial_jets,after=seam,
            delta_coefficient_l1=[float(np.sum(abs(v))) for v in A.cut_difference_coeff]),
        inner_collar=dict(interval=[A.cuff,A.inner],cuff_jet_norms={key:float(np.max(np.linalg.norm(v,axis=-1))) for key,v in collar_zero.items()},
            inner_jet_norms=inner_norms,nonzero_metric_defect=True,
            definition='Original finite endpoint Hermite collar on unchanged source background; not an exact nonlinear tail.'),
        topology=old.topology(faces,cloud),files=files,piece_labels=p['piece_labels'],
        material_inverse_max_residual=inverse,mirror_inlet_samples=mirror,sampled_piece_jets=audits,
        fixed_markers=dict(theorem=p['fixed_cap']['theorem'],centers=centers,affine_determinant=affine,
            maximum_marker_curvature=16*p['fixed_cap']['marker_k'],height=p['fixed_cap']['markers'][0]['height'],
            exact_limit_conditions_unpaid=True,finite_field_has_exactly_four_gaussian_maxima_claimed=False),
        fixed_hold=dict(two_fixed_caps_union=True,selected_fixed_pole_distance=float(np.linalg.norm(top-bottom)),
            ratio_to_vertex_ball_diameter_upper=float(np.linalg.norm(top-bottom))/ball),
        vertex_cloud_diameter_lower=diameter_lower,vertex_cloud_ball_diameter_upper=ball,
        phase_rule=p['phase_rule'],phase_vertex_samples=phase,
        normal_samples=dict(file=str(packet.resolve()),sha256=sha(packet),moving=len(moving),fixed=len(fixed_indices)),
        all_phase_finite_pairs=dict(file=str(reach_file.resolve()),sha256=sha(reach_file),
            negative_pairs_by_type={key:reach[key]['negative_sample_pairs'] for key in ('moving_fixed','moving_moving','fixed_fixed')}),
        exact_common_g_isometry=False,exact_infinite_nonlinear_tail=False,continuous_embedding_certificate=False,
        continuous_spatial_reach_certificate=False,task_completed=False,
        limitations=['Finite metric and normal-chord samples do not certify the continuous surface.',
            'All phase dependence is explicit; R11 eliminates phase for the finite moving/fixed sample pairs only.',
            'The original finite inner collar has nonzero metric defect; fixed-g convergence remains to be demonstrated.',
            'R14 is a conditional exact-limit tool; no assertion of exactly four Gaussian maxima for this finite approximate field.',
            'This baseline A still falls short of the required large amplitude.'],seconds=time.monotonic()-started)
    output=Path(str(args.out_prefix)+'-assembly.json');write(output,report)
    print(json.dumps(dict(output=str(output),topology=report['topology'],seam=seam,
        metrics=audits,cap_height=A.cap_height,negative_pairs=report['all_phase_finite_pairs']['negative_pairs_by_type'],
        seconds=report['seconds'])),flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['plan','render'])
    for key in ('source-topic','checkpoint','port','config','complete','out-prefix'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--plan',type=Path);p.add_argument('--heights',type=Path)
    p.add_argument('--angular',type=int,default=96);p.add_argument('--phase-samples',type=int,default=9)
    p.add_argument('--marker-k',type=float,default=1/160)
    p.add_argument('--cut-correction-width',type=float,default=.01)
    for key,value in [('prefix-intervals',112),('tail-intervals',112),('collar-intervals',24),('cap-intervals',40),('mean-batch',8),('reach-ring-stride',2),('reach-angle-stride',4)]:
        p.add_argument('--'+key,type=int,default=value)
    a=p.parse_args();a.source_hash=sha(__file__)
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if a.action=='plan':
        if a.phase_samples<3 or a.phase_samples%2!=1:
            raise ValueError('Odd phase sample count at least three required')
        plan(a)
    else:
        if not a.plan or not a.heights:
            p.error('render requires --plan and --heights')
        render(a)


if __name__=='__main__':
    main()
