#!/usr/bin/env python3
"""One bounded local JVP fixture for the saved K31/tail16/129-node field.

The actual v21 warm is restored without interpolation. Only selected node
Gauss, actual interior Gauss, and complete R152/R153/R155 endpoint-cell
Codazzi packets are evaluated. This is not a whole Jacobian or a BVP run.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import hashlib
import json
import resource
import time
import traceback
from pathlib import Path
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem
from fd2d_gc_local_normal_system import EliminatedFieldMap
from fd2d_gc_positive_trace_stream_normal import radial_view
from fd2d_gc_positive_trace_interior_merit import actual_point_packet
from fd2d_gc_raw_bump_positive_trace import actual_state_columns
from fd2d_gc_gauss_cell_positive_trace import gauss_cell_positive_trace


def maximum(a):
    return float(np.max(abs(np.asarray(a)), initial=0.))


def digest(a):
    v=np.ascontiguousarray(a)
    return hashlib.sha256(v.tobytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--run-report', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args=ap.parse_args()
    stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh immutable fixture stem')
    start=time.monotonic()
    here=Path(__file__).resolve().parent
    source_names=[Path(__file__).name,'fd2d_gc_midpoint_refined_positive_trace_v3.py',
        'fd2d_gc_midpoint_refined_positive_trace.py','fd2d_gc_nested_angular_positive_trace.py',
        'fd2d_gc_local_normal_system.py','fd2d_gc_positive_trace_stream_normal.py',
        'fd2d_gc_positive_trace_interior_merit.py','fd2d_gc_gauss_cell_positive_trace.py',
        'fd2d_gc_raw_bump_positive_trace.py','fd2d_gc_positive_trace_branch.py',
        'fd2d_gc_positive_gauss_coast_hybrid.py','fd2d_gc_positive_gauss_hybrid.py',
        'fd2d_gc_hybrid_lifting_codazzi_d2.py','fd2d_gc_gauss_cell_positive_gauss.py',
        'fd2d_gc_positive_gauss_l.py','fd2d_gc_gauss_cell_codazzi_endpoint_d2.py',
        'fd2d_gc_gauss_cell_codazzi.py','fd2d_gc_d2_complements.py']
    sources={name:identity(here/name) for name in source_names}
    report=dict(schema='fd2d-actual-refined-independent-tail-local-JVP-v1',
        status='running',passed=False,input_field=identity(args.field),
        input_run_report=identity(args.run_report),sources=sources,
        no_whole_Jacobian=True,no_BVP=True,no_body=True,
        no_continuous_certificate=True,
        input_scope='Immutable v21 central-restored warm; the stopped main solve accepted no new state')
    try:
        if report['input_field']['sha256']!='eac2a27ebecd31424bc5880a3870749cb10b8a130b2a61430d94fa83cf604d73':
            raise ValueError('This one-off fixture is bound to the declared actual v21 warm')
        a=load_npz(args.field)
        run=json.loads(args.run_report.read_text());s=run['settings']
        candidate=Path(s['candidate']);radius=Path(s['radius_packet'])
        proof=json.loads(radius.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=identity(candidate)['sha256']:
            raise ValueError('Base radius proof does not bind the actual candidate')
        witness=dict(**identity(radius),candidate_sha256=proof['candidate_sha256'])
        problem=create_midpoint_refined_problem(candidate,saved_field=a,split_cells=(),
            modes=int(a['modes']),max_step=s['mesh_step'],gap=s['gap'],
            reference_inlet=Path(s['reference_inlet']),reference_cache=Path(s['reference_cache']),
            reference_rim_fraction=s['reference_rim_fraction'],minimum_active_n=s['minimum_active_n'],
            mesh_relative_tolerance=s['mesh_relative_tolerance'],
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=s['radius_floor'])
        if (problem.K,problem.N,problem.q,problem.parameter_count)!=(31,129,95,54):
            raise ValueError('Unexpected actual independent-tail/refined dimensions')
        if (problem.tail_parameter_slice.start,problem.tail_parameter_slice.stop,
            problem.profile_parameter_slice.start,problem.profile_parameter_slice.stop)!=(31,47,47,54):
            raise ValueError('Explicit independent-tail parameter slices changed')
        if not np.array_equal(a['mesh'],problem.x):
            raise ValueError('The saved 129-node partition was not restored exactly')
        z=np.r_[a['corrections'].ravel(),a['parameters']]
        original_digest=digest(z)
        restore,restore_definition=problem.inject_saved_field()
        if not np.array_equal(restore,z):
            raise ValueError('Empty-split restore changed defining coefficients')
        mapping=EliminatedFieldMap(problem)
        y,p=problem.unpack(z)
        central_cell=int(mapping.central_nodes[-1])
        # Old cell63 was explicitly bisected. The lower child tests the
        # nonlinear R153 rim rather than only an exactly Gauss plateau.
        refinement=json.loads(str(a['radial_refinement_definition']))
        parent={row['old_cell']:row['new_cells'] for row in refinement['old_cell_to_new_cells']}
        coast_cell=int(parent[63][0])
        terminal_cell=int(parent[118][0])
        gauge_node=int(problem.inactive_trace_nodes[0])
        gauge_cell=gauge_node
        cells=np.array([central_cell,coast_cell,terminal_cell,gauge_cell],int)
        if len(np.unique(cells))!=len(cells):
            raise ValueError('Selected four local mechanisms unexpectedly coincide')
        node_ids=np.array([central_cell,coast_cell+1,terminal_cell+1,gauge_node],int)
        total=problem.N*problem.q
        where={int(k):j for j,k in enumerate(mapping.free)}
        directions=[]
        def add_direction(name,raw=(),parameter=()):
            vf=np.zeros(mapping.count);vp=np.zeros(problem.parameter_count)
            for node,column,value in raw:
                absolute=int(node)*problem.q+int(column)
                if absolute not in where:
                    raise ValueError('Requested nonzero field direction is eliminated')
                vf[where[absolute]]=value
            for column,value in parameter:vp[column]=value
            full=mapping.expand(vf,vp)
            directions.append(dict(name=name,free=vf,parameter=vp,full=full))
        add_direction('new_high_raw_modes_with_terminal_gauge',raw=[
            (coast_cell+1,31,.6),(coast_cell+1,problem.e+30,-.4),
            (terminal_cell+1,30,-.5),(terminal_cell+1,problem.d+31,.35),
            (terminal_cell+1,problem.e+30,.2),(gauge_node,31,.45)])
        add_direction('last_central_parameter_30',parameter=[(30,1.)])
        # Use nonzero interior tail controls, so both signs of these small
        # finite differences stay inside the original nonnegative family.
        add_direction('independent_tail_31_to_46',parameter=[
            (31,.4),(35,-.3),(38,.2),(42,-.1),(46,.5)])
        add_direction('all_seven_physical_parameters_47_to_53',parameter=list(zip(
            range(47,54),[.35,-.27,.18,.24,-.29,.2,-.16])))
        vf=sum(w*d['free'] for w,d in zip([.3,.2,.4,.1],directions))
        vp=sum(w*d['parameter'] for w,d in zip([.3,.2,.4,.1],directions))
        directions.append(dict(name='combined_new_raw_central_tail_profile',free=vf,parameter=vp,full=mapping.expand(vf,vp)))
        constraint_checks=[]
        for d in directions:
            full=d['full'];vp=d['parameter']
            constraint_checks.append(dict(name=d['name'],
                central=max(maximum(full[j*problem.q:(j+1)*problem.q]-mapping.parameter_maps[j]@vp) for j in mapping.central_nodes),
                cut=maximum(full[total-problem.q:total]),
                deleted_coast_l=maximum(full[np.array([j*problem.q+r for j in problem.inactive_l_raw_nodes for r in range(problem.d,problem.q)],int)]),
                trace_pair_sum=maximum(full[mapping.pairs[:,0]]+full[mapping.pairs[:,1]]),
                full_direction_l2=float(np.linalg.norm(full)),parameter_nonzero_indices=np.flatnonzero(vp).tolist()))
        selected=dict(cells=[dict(index=int(j),left=float(problem.x[j]),right=float(problem.x[j+1])) for j in cells],
            nodes=[dict(index=int(j),s=float(problem.x[j])) for j in node_ids],
            roles=dict(central_transition_cell=central_cell,refined_coast_rim_cell=coast_cell,
                refined_terminal_ramp_cell=terminal_cell,terminal_gauge_cell=gauge_cell),
            terminal_gauge_node=gauge_node,coast_deleted_nodes=problem.inactive_l_raw_nodes.tolist(),
            trace_gauge_nodes=problem.inactive_trace_nodes.tolist())
        report.update(dimensions=dict(raw_modes=problem.K,central=problem.K,tail=problem.tail_parameter_count,
            profile=problem.J,parameters=problem.parameter_count,nodes=problem.N,q=problem.q,work=problem.work),
            layout=problem.parameter_layout(),selection=selected,exact_elimination_direction_errors=constraint_checks,
            restore_is_byte_identical=True,restore_definition=restore_definition)
        print(json.dumps(dict(event='local_fixture_start',selection=selected,dimensions=report['dimensions'])),flush=True)

        def node_block(node,v,jacobian):
            view=radial_view(problem,[node])
            yy,pp=problem.unpack(v);local=np.r_[yy[node],pp]
            _,data=view.evaluate(local)
            G=data['full_gauss'][:,0]
            J=None
            if jacobian:
                dn,dm,dl=actual_state_columns(view,data,0)
                n,m,l=data['fields'][:,0].T
                state=l[:,None]*dn+n[:,None]*dl-2*m[:,None]*dm
                fp=data['fields_parameters'][:,0]
                par=l[:,None]*fp[:,0]+n[:,None]*fp[:,2]-2*m[:,None]*fp[:,1]
                par[:,view.profile_parameter_slice]-=data['profile_jet']['K_parameters'][0]
                J=np.hstack((state,par))
            return G.copy(),J

        # Each helper view owns at most one cell. It is reused only for the
        # same two original nodes; all global parameter slices are explicit.
        cell_views={int(j):radial_view(problem,[j,j+1]) for j in cells}
        def cell_blocks(cell,v,jacobian):
            view=cell_views[int(cell)];yy,pp=problem.unpack(v)
            local=np.r_[yy[cell:cell+2].ravel(),pp]
            cod=gauss_cell_positive_trace(view,local,order=2,high_weight=s['high_codazzi_weight'],jacobian=jacobian)
            rc=np.r_[cod['retained_residual'],cod['high_residual']]
            jc=sparse.vstack((cod['retained_jacobian'],cod['high_jacobian']),format='csc') if jacobian else None
            layout,_,data=actual_point_packet(view,local,cells=(0,),jacobian=jacobian)
            qv=layout['view'];G=data['full_gauss'];jg=[]
            if jacobian:
                for j,t in enumerate(layout['fractions']):
                    n,m,l=data['fields'][:,j].T
                    dn,dm,dl=actual_state_columns(qv,data,j)
                    state=l[:,None]*dn+n[:,None]*dl-2*m[:,None]*dm
                    fp=data['fields_parameters'][:,j]
                    par=l[:,None]*fp[:,0]+n[:,None]*fp[:,2]-2*m[:,None]*fp[:,1]
                    par[:,qv.profile_parameter_slice]-=data['profile_jet']['K_parameters'][j]
                    jg.append(np.hstack(((1-t)*state,t*state,par)))
            info=dict(full_average_codazzi_maximum=maximum(cod['full_codazzi_cells']),
                actual_internal_Gauss_maximum=maximum(G),known_lifting_change=cod['info']['known_lifting_full_change_maximum'])
            return (rc,jc),(G.T.ravel().copy(),np.vstack(jg) if jacobian else None),info

        blocks=[]
        for node in node_ids:
            r,J=node_block(int(node),z,True)
            blocks.append(dict(label='actual_node_G_'+str(node),nodes=(int(node),),kind='node',index=int(node),r=r,J=J))
        for cell in cells:
            cod,G,info=cell_blocks(int(cell),z,True)
            blocks.append(dict(label='complete_endpoint_C_'+str(cell),nodes=(int(cell),int(cell)+1),kind='cell_C',index=int(cell),r=cod[0],J=cod[1],info=info))
            blocks.append(dict(label='actual_interior_G_'+str(cell),nodes=(int(cell),int(cell)+1),kind='cell_G',index=int(cell),r=G[0],J=G[1],info=info))
        for b in blocks:
            b['columns']=np.r_[np.concatenate([j*problem.q+np.arange(problem.q) for j in b['nodes']]),total+np.arange(problem.parameter_count)]
            A,B=mapping.transform(b['nodes'],b['J'])
            b['transformed']=(A,B)
        steps=[1e-6,5e-7]
        rows=[];witness_arrays={}
        for di,d in enumerate(directions):
            derivatives={}
            for b in blocks:
                action=np.asarray(b['J']@d['full'][b['columns']]).ravel()
                A,B=b['transformed'];mapped=B@d['parameter']
                for node,aa in zip(b['nodes'],A):
                    mapped+=aa@d['free'][mapping.offsets[node]:mapping.offsets[node+1]]
                derivatives[b['label']]=action
                witness_arrays['d%d_%s_analytic'%(di,b['label'])]=action
                b.setdefault('mapping_action_errors',[]).append(maximum(action-mapped)/max(1.,maximum(action)))
            direction_rows=[]
            for h in steps:
                plus=z+h*d['full'];minus=z-h*d['full']
                residuals_plus={};residuals_minus={}
                for node in node_ids:
                    label='actual_node_G_'+str(node)
                    residuals_plus[label]=node_block(int(node),plus,False)[0]
                    residuals_minus[label]=node_block(int(node),minus,False)[0]
                for cell in cells:
                    for vv,dd in ((plus,residuals_plus),(minus,residuals_minus)):
                        cc,gg,_=cell_blocks(int(cell),vv,False)
                        dd['complete_endpoint_C_'+str(cell)]=cc[0]
                        dd['actual_interior_G_'+str(cell)]=gg[0]
                for b in blocks:
                    key=b['label'];fd=(residuals_plus[key]-residuals_minus[key])/(2*h)
                    an=derivatives[key];err=fd-an
                    row=dict(direction=d['name'],step=h,block=key,nodes=list(b['nodes']),
                        rows=len(fd),analytic_l2=float(np.linalg.norm(an)),finite_difference_l2=float(np.linalg.norm(fd)),
                        error_maximum=maximum(err),relative_l2=float(np.linalg.norm(err)/max(1.,np.linalg.norm(an))),
                        relative_maximum=maximum(err)/max(1.,maximum(an)))
                    direction_rows.append(row)
                    witness_arrays['d%d_h%s_%s_fd'%(di,str(h).replace('-','m'),key)]=fd
            rows.extend(direction_rows)
            print(json.dumps(dict(event='direction_complete',direction=d['name'],
                largest_action_l2=max(row['analytic_l2'] for row in direction_rows),
                maximum_relative_l2=max(row['relative_l2'] for row in direction_rows))),flush=True)
        # One final local residual evaluation checks no source/input mutation
        # or cache contamination; it does not assemble or inspect a whole F.
        unchanged=[]
        for node in node_ids:
            label='actual_node_G_'+str(node);b=next(b for b in blocks if b['label']==label)
            unchanged.append(maximum(node_block(int(node),z,False)[0]-b['r']))
        for cell in cells:
            cc,gg,_=cell_blocks(int(cell),z,False)
            for tag,r in (('complete_endpoint_C_',cc[0]),('actual_interior_G_',gg[0])):
                b=next(b for b in blocks if b['label']==tag+str(cell));unchanged.append(maximum(r-b['r']))
        mapping_error=max(max(b['mapping_action_errors']) for b in blocks)
        nonzero={d['name']:max(row['analytic_l2'] for row in rows if row['direction']==d['name']) for d in directions}
        blocks_summary=[dict(label=b['label'],nodes=list(b['nodes']),rows=len(b['r']),
            local_columns=b['J'].shape[1],residual_maximum=maximum(b['r']),
            local_J_nnz=int(b['J'].nnz) if sparse.issparse(b['J']) else int(np.count_nonzero(b['J'])),
            mapping_action_error=max(b['mapping_action_errors']),info=b.get('info')) for b in blocks]
        report.update(status='completed',JVP_rows=rows,selected_blocks=blocks_summary,
            finite_difference_steps=steps,all_direction_action_l2_maxima=nonzero,
            maximum_relative_l2=max(row['relative_l2'] for row in rows),
            maximum_relative_maximum=max(row['relative_maximum'] for row in rows),
            reduced_map_action_relative_maximum=mapping_error,
            repeated_original_local_residual_change= max(unchanged),
            vector_bytes_unchanged=digest(z)==original_digest,
            no_whole_original_F_evaluated=True,
            local_fixture_only_not_full_finite_convergence=True)
        report['passed']=bool(report['maximum_relative_l2']<3e-5
            and report['maximum_relative_maximum']<3e-5 and mapping_error<2e-12
            and max(unchanged)<2e-12 and digest(z)==original_digest
            and min(nonzero.values())>1e-6
            and max(max(row[k] for k in ('central','cut','deleted_coast_l','trace_pair_sum')) for row in constraint_checks)<1e-13)
        witness_arrays.update(selected_cells=cells,selected_nodes=node_ids,
            full_directions=np.stack([d['full'] for d in directions]),parameter_directions=np.stack([d['parameter'] for d in directions]),
            mesh=problem.x,actual_parameters=p)
        wp=stem.with_name(stem.name+'-witnesses.npz');np.savez_compressed(wp,**witness_arrays)
        report['witnesses']=identity(wp)
    except BaseException as exc:
        report.update(status='failed',exception_type=type(exc).__name__,exception=str(exc),traceback=traceback.format_exc())
        print(report['traceback'],flush=True)
    report['seconds']=time.monotonic()-start
    report['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['sources_unchanged']=all(identity(here/name)['sha256']==value['sha256'] for name,value in sources.items())
    if not report['sources_unchanged']:report['passed']=False
    dst=stem.with_name(stem.name+'-report.json')
    dst.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='fixture_complete',status=report['status'],passed=report['passed'],
        seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'],report=str(dst))),flush=True)
    return 0 if report['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
