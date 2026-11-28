"""First joint R681/R684/R686/R690 full Cartesian annular-window recovery on public Actions."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.linalg import cho_factor,cho_solve

from r688_actual_r664_window_collars import Centerline, Collar, active_width, require_public, verify_collars
from r688_closed_shell_observer import KnownBody, normal_and_curvature
from r688_joint_window_field import JointField, whiten_metric, extrema
from r688_true_caps_and_reference_sections import ReferenceSections
from r688_two_port_material_atlas import MaterialAtlas


def emit(tag,data):
    print('R688_'+tag+' '+json.dumps(data,separators=(',',':'),allow_nan=False),flush=True)


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as src:
        for block in iter(lambda:src.read(1048576),b''):
            h.update(block)
    return h.hexdigest()


def save_arrays(name,fields):
    dest=Path('r688-paid-state'); dest.mkdir(exist_ok=True)
    path=dest/(name+'.npz')
    tmp=dest/(name+'.partial.npz')
    np.savez_compressed(tmp,**fields)
    os.replace(tmp,path)
    emit('PAID_OBJECT',dict(file=str(path),bytes=path.stat().st_size,sha256=sha(path)))


def dense(fields,prefix,obj):
    fields[prefix+'_breaks']=obj.ts
    for key in ('y_old','F','Q','t_old','t'):
        if hasattr(obj.interpolants[0],key):
            fields[prefix+'_'+key]=np.asarray([getattr(i,key) for i in obj.interpolants])


def tck(fields,name,spl):
    for i,val in enumerate(spl.tck):
        fields[name+'_'+str(i)]=val


def save_reference(ref):
    fields=dict(section_angle_knots=ref.angle.t,section_angle_c=ref.angle.c,section_angle_degree=ref.angle.k,starts=ref.starts,
                cuts=ref.cuts,xf=ref.xf,height=ref.height,S=ref.S,tube=ref.tube_length,
                sphere_turn=ref.sphere_turn,source_turn=ref.source_turn)
    for i,spl in enumerate(ref.tables+ref.cap_normals):
        tck(fields,'cap_'+str(i),spl)
    for i,obj in enumerate([*ref.turns[1:],ref.crown,ref.sphere_arc,ref.source_arc]):
        dense(fields,'path_'+str(i),obj)
    save_arrays('true-reference',fields)


def strip_physics(coll,source):
    v=np.linspace(-.90,-.62,301)
    if coll.sign<0:
        v=-v
    frac,v=np.meshgrid(np.linspace(0,1,13),v,indexing='ij')
    t=frac*active_width(v,coll.h)
    x,a,b,aa,ab,bb=coll.position_jets(t,v)
    _,k,sine,g=normal_and_curvature(a,b,aa,ab,bb)
    _,a0,b0,rr,rs,ss=source.position_jets(t,v)
    _,_,_,g0=normal_and_curvature(a0,b0,rr,rs,ss)
    return dict(sign=coll.sign,position_jet_max_abs_k=float(k.max()),min_param_sine_squared=float(sine.min()),
                max_relative_reference_gram=float(extrema(whiten_metric(g,g0)).max()),
                actual_strip_samples=int(t.size))


def make_paid(ref,config,phases):
    lines={}; pairs=[{},{}]; receipts=[]
    for phase in phases:
        line=Centerline(phase); lines[phase]=line
        fields=dict(phase=phase,physical_centerline_knots=line.curve.x,physical_centerline_bernstein=line.curve.c)
        dense(fields,'line',line.solution.sol)
        for r,(modes,steps) in enumerate(config['collar_grids']):
            cols=[Collar(line,sign,config['h'],modes,steps) for sign in (1,-1)]
            pairs[r][phase]=cols
            for j,coll in enumerate(cols):
                for k,spl in enumerate(coll.splines):
                    tck(fields,f'grid{r}_pulse{j}_field{k}',spl)
        rec=dict(phase=phase,line_rhs=line.calls,physical_centerline_vs_original_dop_position_velocity_acceleration=line.curve_errors,pulses=verify_collars(pairs[0][phase],pairs[1][phase]))
        save_arrays('actual-line-collars-'+str(phase),fields)
        emit('TRUE_COLLAR',rec); receipts.append(rec)
        if any(max(p['position_spline_five_differential_defects']+p['coarse_position_five_differential_defects'])>.15 or p['frame_gram_max']>1e-6
               for p in rec['pulses']):
            raise ArithmeticError('Actual collar position/frame disagrees with measured Cartesian jets')
    return lines,pairs,receipts


def build_model(ref,config,lines,collars,phases,index):
    grid=config['field_grids'][index]
    source=lines[0.]
    A=MaterialAtlas(ref,source,grid['theta'],grid['rings'],config['h'],grid['shift'])
    body=KnownBody(ref,grid['body'])
    data={'shoulder_k':body.primary_shoulder_max_abs_principal,
          'shoulder_sine':body.primary_shoulder_min_sine,'collar_k':[],'actual_by_phase':{}}
    _,y0,z0=source.fields(np.array([A.vstar]))
    for p in phases:
        A.prepare(lines[p],collars[p],collars[0.])
        _,y,z=lines[p].fields(np.array([A.vstar]))
        delta=np.array([0.,(y-y0).item(),(z-z0).item()])
        data[p]=body.cloud(lines[p],collars[p],config['h'],delta)
        actual=[strip_physics(c,s) for c,s in zip(collars[p],collars[0.])]
        data['collar_k'].extend(row['position_jet_max_abs_k'] for row in actual)
        vs=np.unique(np.r_[np.linspace(-1,1,2001),lines[p].curve.x[:-1]+.0005])
        vp,ap=lines[p].cartesian(vs,1),lines[p].cartesian(vs,2)
        v0=source.cartesian(vs,1)
        g=np.sum(vp*vp,axis=-1); g0=np.sum(v0*v0,axis=-1)
        sheet_k=abs(vp[:,0]*ap[:,1]-vp[:,1]*ap[:,0])/g**1.5
        data['collar_k'].append(float(sheet_k.max()))
        data['actual_by_phase'][p]=dict(strips=actual,actual_sheet_max_abs_principal=float(sheet_k.max()),
            actual_sheet_min_speed=float(np.sqrt(g).min()),actual_sheet_relative_gram=float(np.max(abs(g/g0-1))))
    emit('GRID',dict(independent_grid=index,radial=len(A.t),angle=len(A.theta),phases=phases,
        vstar=A.vstar,paid_nodes=int(A.paid.sum()),wide_shoulder_source_height=ref.height,
        primary_cap_shoulder_maximum_principal=body.primary_shoulder_max_abs_principal,
        physical_strip_and_sheet_per_phase=data['actual_by_phase'],
        actual_primary_crown_and_reflected_clouds=[len(data[p][0]) for p in phases]))
    return JointField(A,phases,data,config['radial_spans'],config['fourier_modes'])


def transport(q,from_phases,to_phases):
    out=np.empty((len(to_phases),)+q.shape[1:])
    out[0]=q[0]
    rotations=q.copy(); rotations[0]=0.
    for i,p in enumerate(to_phases[1:],1):
        j=np.searchsorted(from_phases,p)
        if from_phases[j]==p:
            out[i]=rotations[j]
        else:
            a=(p-from_phases[j-1])/(from_phases[j]-from_phases[j-1])
            out[i]=(1-a)*rotations[j-1]+a*rotations[j]
    return out


def snapshot(q,pt,phases,rules,work,status,report,fine=None):
    rec=dict(status=status,phases=phases,parameters=q.tolist(),parameter_shape=list(q.shape),
             packed_le_float64_sha256=hashlib.sha256(np.asarray(q,dtype='<f8').tobytes()).hexdigest(),
             design_unfrozen=True,source_phase_rotation_exact_identity=True,
             next_damping=pt,work=dict(work),elapsed=time.monotonic()-rules,
             work_report=report,independent_phase_and_grid_report=fine,
             continuous_phase_metric_reach_and_exact_solution_qualification=False,
             README_completion_claim=False)
    dest=Path('r688-paid-state'); dest.mkdir(exist_ok=True)
    tmp=dest/'current.tmp'
    tmp.write_text(json.dumps(rec,allow_nan=False)); os.replace(tmp,dest/'current.json')
    return rec


def solve(config,budget):
    require_public()
    started=time.monotonic(); deadline=started+budget
    phases=config['joint_phases']; check_phases=config['independent_phases']
    ref=ReferenceSections()
    save_reference(ref)
    lines,collars,receipts=make_paid(ref,config,check_phases)
    model=build_model(ref,config,lines,collars[0],phases,0)
    fine=build_model(ref,config,lines,collars[1],check_phases,1)
    q=np.zeros(model.shape); damp=config['initial_damping']
    work=dict(jacobians=0,complete_original_columns=0,trials=0,accepted_repairs=0,fine_reads=0,
              required_collar_pulses=2*len(check_phases),independent_collar_resolutions=2)
    residual,report,active=model.state(q,True)
    rf,fine_report,_=fine.state(transport(q,phases,check_phases),True)
    work['fine_reads']+=1
    def checkpoint(status):
        return snapshot(q,damp,phases,started,work,status,report,fine_report)
    emit('BASELINE',checkpoint('joint-source-and-moving-crown-recovery'))
    reason='natural clock checkpoint'
    while time.monotonic()<deadline-90:
        J=np.empty((residual.size,q.size),order='F')
        base=q.ravel(); h=config['jacobian_step']
        ncols=0
        for j in range(q.size):
            if time.monotonic()>deadline-75:
                break
            plus=base.copy(); plus[j]+=h
            rr,_,_=model.state(plus.reshape(q.shape),False,active)
            J[:,j]=(rr-residual)/h
            ncols+=1
        work['complete_original_columns']+=ncols
        if ncols!=q.size:
            save_arrays('unfinished-current-J',dict(q=q,complete_columns=np.arange(ncols),J=J[:,:ncols],
                       residual=residual,active_witness_json=json.dumps(active),phase=phases))
            reason='clock during full joint Cartesian Jacobian'; break
        work['jacobians']+=1
        normal=J.T@J; grad=J.T@residual; scale=np.maximum(np.diag(normal),1e-12)
        dnorm=float(np.linalg.norm(residual)); fnorm=float(np.linalg.norm(rf))
        emit('JOINT_J',dict(rows=J.shape[0],original_columns=J.shape[1],norm=dnorm,independent_norm=fnorm,
                           gauss_newton_eigenvalues=np.linalg.eigvalsh(normal).tolist()))
        # Save the full sufficient GN state, allowing the same lambda scan to resume
        # without reconstructing a paid Jacobian.
        save_arrays('last-full-Normal',dict(q=q,normal=normal,gradient=grad,scale=scale,residual=residual,
                       active_witness_json=json.dumps(active),phase=phases))
        changed=False
        for _ in range(12):
            if time.monotonic()>=deadline-80:
                break
            sc=np.sqrt(scale)
            equil=(normal/sc[:,None])/sc[None,:]
            dq=cho_solve(cho_factor(equil+damp*np.eye(q.size)), -grad/sc)/sc
            dq/=max(1.,np.max(np.abs(dq))/.12)
            for alpha in (1.,.5,.25,.125,.0625):
                if time.monotonic()>=deadline-80:
                    break
                cand=q+alpha*dq.reshape(q.shape); work['trials']+=1
                tr,_,_=model.state(cand,False,active)
                if np.linalg.norm(tr)>=(1-1e-11)*dnorm:
                    continue
                tr,co,wit=model.state(cand,True)
                if np.linalg.norm(tr)>=(1-1e-11)*dnorm:
                    continue
                tf,fi,_=fine.state(transport(cand,phases,check_phases),True)
                work['fine_reads']+=1
                if np.linalg.norm(tf)>=(1-1e-11)*fnorm:
                    continue
                q,residual,report,active,rf,fine_report=cand,tr,co,wit,tf,fi
                damp=max(1e-13,damp/3)
                work['accepted_repairs']+=1; changed=True
                emit('RESTORATION',checkpoint('joint-repair-all-sampled-physical-rows-recomputed'))
                break
            if changed:
                break
            damp*=8
        if not changed:
            reason=('natural clock checkpoint' if time.monotonic()>=deadline-80 else
                    'full joint direction and twelve dampings exhausted at current resolution')
            break
    emit('FINAL',checkpoint(reason))


def main():
    arg=argparse.ArgumentParser()
    arg.add_argument('--geometry',required=True); arg.add_argument('--max-seconds',type=int,required=True)
    args=arg.parse_args()
    solve(json.loads(Path(args.geometry).read_text()),args.max_seconds)


if __name__=='__main__':
    try:
        main()
    except (ArithmeticError,ValueError,RuntimeError,np.linalg.LinAlgError) as error:
        emit('UNRESOLVED',dict(type=type(error).__name__,message=str(error),
             retained_state_directory='r688-paid-state',qualification=False))
        raise
