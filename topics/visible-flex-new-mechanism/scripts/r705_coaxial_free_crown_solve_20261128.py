"""Joint public solve of the new half-turn annulus, reusing actual paid R688 objects."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.linalg import cho_factor,cho_solve
from scipy.spatial import QhullError

from r688_actual_r664_window_collars import require_public
from r705_equivariant_window_field import Representation, WindowField
from r705_paid_coaxial_geometry import CoaxialAtlas, CoaxialBody, PaidArchive, PARENT, phase_objects, reference, strip_readout

DEST=Path('r705-paid-state')
PHASES=[0.,.3,.65,1.]
INDEPENDENT=[0.,.15,.3,.475,.65,.825,1.]
H=.0002


def emit(tag,data):
    print('R705_'+tag+' '+json.dumps(data,separators=(',',':'),allow_nan=False),flush=True)


def digest_file(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for buf in iter(lambda:f.read(1048576),b''):
            h.update(buf)
    return h.hexdigest()


def archive_arrays(name,**arrays):
    tmp=DEST/(name+'.partial.npz')
    final=DEST/(name+'.npz')
    np.savez_compressed(tmp,**arrays)
    os.replace(tmp,final)
    emit('PAID_OBJECT',dict(file=final.name,bytes=final.stat().st_size,sha256=digest_file(final)))


def build_model(ref,lines,grids,index,rep):
    # Both use new, aligned material rays; the finer grid uses shifted radial/angle knots.
    ntheta,nrings,shift,body_res=((40,5,0.,18),(64,8,.31,26))[index]
    phases=(PHASES,INDEPENDENT)[index]
    A=CoaxialAtlas(ref,lines[0.],ntheta,nrings,H,shift)
    body=CoaxialBody(ref,body_res)
    data=dict(centers={},actual_by_phase={},collar_k=[],shoulder_sine=body.primary_shoulder_min_sine,
              shoulder_k=body.primary_shoulder_max_abs_principal)
    for p in phases:
        line=lines[p]
        pair=grids[p][index]
        source=grids[0.][index]
        A.prepare(line,pair,source)
        data['centers'][p]=line.center
        data[p]=body.cloud(line,pair,H)
        row=strip_readout(pair,source,H)
        vs=np.unique(np.r_[np.linspace(-1.,1.,2001),line.curve.x[:-1]+.0005])
        d,dd=line.cartesian(vs,1),line.cartesian(vs,2)
        speed2=np.sum(d*d,axis=-1)
        speed0=np.sum(lines[0.].cartesian(vs,1)**2,axis=-1)
        k=abs(d[:,0]*dd[:,1]-d[:,1]*dd[:,0])/speed2**1.5
        sym=[]
        for order in range(3):
            delta=line.cartesian(vs,order)-line.old.cartesian(vs,order)
            if not order:
                delta+=line.center[1:]
            sym.append(float(np.linalg.norm(delta,axis=-1).max()))
        data['actual_by_phase'][p]=dict(strips=row,actual_sheet_max_abs_principal=float(k.max()),
                centered_source_minus_old_absolute_derivatives=sym,actual_sheet_min_speed=float(np.sqrt(speed2.min())),
                actual_sheet_relative_gram=float(np.max(abs(speed2/speed0-1))))
        data['collar_k'].extend([float(k.max()),*[s['position_jet_max_abs_k'] for s in row]])
    emit('NEW_ATLAS',dict(independent=index,angles=len(A.theta),radial=len(A.t),
            paired_rays=A.n,actual_corner_ray_indices=A.corner_ray_indices,actual_negative_strips_and_sheets=data['actual_by_phase'],
            original_shoulder_width=.05,coaxial_center='physical symmetric midpoint',
            known_crown_old_cap_clearance_for_travel_le_005='cos(1.02)-.05-.2005 > .272',
            sampled_shoulder_k=body.primary_shoulder_max_abs_principal))
    return WindowField(A,phases,data,2,2,rep)


def qsha(q):
    return hashlib.sha256(np.asarray(q,dtype='<f8').tobytes()).hexdigest()


def run(config,budget):
    require_public()
    started=time.monotonic()
    deadline=started+budget
    DEST.mkdir(exist_ok=True)
    paid=PaidArchive(config['manifest'],config['manifest_sha256'],config['paid_directory'])
    rep=Representation(2,2,PHASES)
    q,excluded=rep.from_parent(paid.record)
    ref=reference(paid)
    lines={}; pairs={}
    for p in INDEPENDENT:
        lines[p],pairs[p]=phase_objects(paid,p,H)
        emit('R709_CONTINUOUS_PHYSICAL_STRIP',dict(phase=p,receipt=lines[p].physical_strip_bounds))
    inherited=dict(parent=PARENT,terminal_sha256=hashlib.sha256(paid.final).hexdigest(),
        parent_status=paid.record['status'],parent_work=paid.record['work'],
        parent_elapsed=paid.record['elapsed'],parent_q_sha256=paid.record['packed_le_float64_sha256'],
        paid_object_receipts=paid.manifest['objects'],consumed_dense=paid.used,
        R709_same_open_dense_strip_records={p:lines[p].physical_strip_bounds for p in INDEPENDENT},
        parent_work_and_independent_report_retained_in_literal=True,
        parent_J_and_normal_qualification_transported=False,unrepresented_old_coefficient_norm=excluded)
    emit('TRANSPORT',dict(inherited=inherited,new_q_sha256=qsha(q),columns_per_block=rep.columns,
        parameter_shape=rep.shape,predictor_only=True))
    work=build_model(ref,lines,pairs,0,rep)
    fine=build_model(ref,lines,pairs,1,rep)
    counters=dict(complete_J=0,FD_columns=0,coarse_all_shells=0,independent_all_shells=0,
                  trials=0,accepted=0,new_ode_solves=0,new_negative_collar_evolutions=0)
    def full(model,value,key):
        result=model.state(value,True)
        counters[key]+=1
        return result
    residual,r0,witness=full(work,q,'coarse_all_shells')
    rf,r1,_=full(fine,q,'independent_all_shells')
    damp=.03
    phase_scan={}
    def snapshot(status):
        rec=dict(status=status,parameters=q.tolist(),parameter_shape=list(q.shape),packed_le_float64_sha256=qsha(q),
            source_and_increment_phase_knots=PHASES,elapsed=time.monotonic()-started,next_damping=damp,
            new_work=dict(counters),old_cost=inherited,coarse=r0,independent=r1,
            new_source_metric_frozen=False,actual_continuum_qualification=False,
            finite_recovery_qualification=False,source_zero_rotation_exact=True,
            damping_and_line_search=phase_scan,README_completion_claim=False)
        tmp=DEST/'current.tmp'
        tmp.write_text(json.dumps(rec,separators=(',',':'),allow_nan=False))
        os.replace(tmp,DEST/'current.json')
        return rec
    emit('BASELINE',snapshot('new coaxial and new free rigid poses independently read'))
    reason='natural time checkpoint'
    while time.monotonic()<deadline-100:
        J=np.empty((residual.size,q.size),order='F')
        base=q.ravel()
        columns=0
        for j in range(q.size):
            if time.monotonic()>=deadline-95:
                break
            probe=base.copy()
            probe[j]+=1.6e-7
            val,_,_=work.state(probe.reshape(q.shape),False,witness)
            J[:,j]=(val-residual)/1.6e-7
            columns+=1
        counters['FD_columns']+=columns
        if columns<q.size:
            archive_arrays('unfinished-J',q=q,J=J[:,:columns],columns=np.arange(columns),
                residual=residual,active_witness_json=json.dumps(witness))
            reason='natural clock within new joint Cartesian Jacobian'
            break
        counters['complete_J']+=1
        normal=J.T@J; grad=J.T@residual
        del J
        scale=np.sqrt(np.maximum(np.diag(normal),1.e-12))
        eq=(normal/scale[:,None])/scale[None,:]
        archive_arrays('last-normal',q=q,normal=normal,gradient=grad,column_scale=scale,
            residual=residual,witness_json=json.dumps(witness))
        changed=False
        old=np.linalg.norm(residual); oldfine=np.linalg.norm(rf)
        for attempt in range(12):
            direction=cho_solve(cho_factor(eq+damp*np.eye(q.size)),-grad/scale)/scale
            direction/=max(1.,float(abs(direction).max())/.12)
            for k,alpha in enumerate((1.,.5,.25,.125,.0625)):
                phase_scan=dict(q_at_normal=qsha(q),damping=damp,next_alpha_index=k,complete_trial=False)
                if time.monotonic()>=deadline-90:
                    break
                trial=q+alpha*direction.reshape(q.shape)
                counters['trials']+=1
                # Every actual trial really reconstructs sigma, both crowns, hulls and all near pairs.
                try:
                    rc,co,wc=full(work,trial,'coarse_all_shells')
                except (ArithmeticError,ValueError,np.linalg.LinAlgError,QhullError) as e:
                    emit('TRIAL_DOMAIN',dict(q_sha256=qsha(trial),phase='coarse',error=str(e)))
                    phase_scan['complete_trial']=True
                    continue
                if np.linalg.norm(rc)>=(1-1e-11)*old:
                    phase_scan['complete_trial']=True
                    continue
                try:
                    ff,fi,_=full(fine,trial,'independent_all_shells')
                except (ArithmeticError,ValueError,np.linalg.LinAlgError,QhullError) as e:
                    emit('TRIAL_DOMAIN',dict(q_sha256=qsha(trial),phase='independent',error=str(e)))
                    phase_scan['complete_trial']=True
                    continue
                phase_scan['complete_trial']=True
                if np.linalg.norm(ff)>=(1-1e-11)*oldfine:
                    continue
                q,residual,r0,witness,rf,r1=trial,rc,co,wc,ff,fi
                counters['accepted']+=1
                damp=max(1e-13,damp/3)
                phase_scan={}
                emit('ACCEPTED_REPAIR',snapshot('two independently reconstructed full-shell recovery decreases'))
                changed=True
                break
            if changed or time.monotonic()>=deadline-90:
                break
            damp*=8
        if not changed:
            reason=('clock during new full direction' if time.monotonic()>=deadline-90
                    else 'twelve new dampings exhausted on this actual input')
            break
    emit('FINAL',snapshot(reason))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--geometry',required=True)
    parser.add_argument('--max-seconds',type=int,required=True)
    args=parser.parse_args()
    run(json.loads(Path(args.geometry).read_text()),args.max_seconds)


if __name__=='__main__':
    main()
