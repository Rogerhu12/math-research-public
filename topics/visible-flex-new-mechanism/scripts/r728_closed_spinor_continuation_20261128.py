"""Continue the one R703 endpoint on complete closed-spinor equations and physical shells."""
import argparse
from collections import Counter
import json
from pathlib import Path
import time
import numpy as np
from scipy.linalg import qr,svd
from r669_true_finite_tilt_reach_continuation_20261128 import trust_step
from r703_real_material_mass_continuation_20261128 import public,emit
from r726_closed_spinor_fourier import ClosedSpinor
from r728_paid_spinor_input import checked_receipt,transfer
from r728_full_spinor_geometry import Grid,Layout,state,local_rows,length_rows,actual_read


def main():
    public()
    ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',type=float,required=True)
    args=ap.parse_args();opt=json.loads(Path(args.geometry).read_bytes())
    prior=checked_receipt(opt)
    started=time.perf_counter();elapsed=lambda:time.perf_counter()-started
    counts=Counter();history=[];accepted=0;frozen=None;reference_cache={}
    schedule=list(opt['stages']);first=schedule[0]
    sp=Layout(first['spans'],first['K']);x=None;trust=prior['trust'];mu=prior['last_accepted_mu'];last=None
    def serialize_reference():
        if frozen is None:return None
        layout,fx,N=frozen
        return dict(space=[layout.spans,layout.K],parameters=fx.tolist(),reference_angles=N)
    def reference(r,binding):
        if binding is None:return None
        ls,v,N=binding
        key=(ls.spans,ls.K,N,v.tobytes(),r.tobytes())
        if key not in reference_cache:
            k=ClosedSpinor(ls.K,N)
            za,zb,c=ls.space.actual_jets(r,ls.split(v))
            reference_cache[key]=k.state(r,za,zb,c)['E']
            counts['immutable_reference_radial_evaluators']+=1
        return reference_cache[key]
    def evaluate(g,k,y,bind,physical):
        ref=reference(g.r,bind)
        counts['full_real_candidate_shape_states']+=1
        z,c,sh=state(sp,k,y,g.r,ref)
        rows,active=local_rows(z,sh,g.guard,opt)
        S=g.w@np.sqrt(z['E']);C=c[0][0,[0,2]]
        nonlocal_rows,_=length_rows(S,C,opt['work_betas'],opt['length_weight'])
        val=np.r_[rows.ravel(),nonlocal_rows]
        read=actual_read(g,z,c,sh,opt['fine_betas']) if physical else None
        if physical:counts['paired_complete_physical_reads']+=1
        return dict(rows=rows,active=active,global_rows=nonlocal_rows,S=S,C=C,E=z['E'],read=read,
                    norm=float(np.linalg.norm(val)))
    def gate(v):
        reads=v['finite_identity_disagreements']
        powers=(1.,.145,.145**2)
        fine_identity=all(all(a*h<tol for a,h,tol in zip(reads[key],powers,(5.e-11,5.e-10,5.e-8))) for key in
           ('mean_J_minus_target_0_1_2','mean_V_closure_0_1_2','interpolated_Phi_psi_minus_J_radial_0_1_2','interpolated_U_psi_minus_V_radial_0_1_2'))
        return (fine_identity and v['shell_pass'] and v['eta']<=opt['freeze_eta'] and v['target_length_margin']>=0 and
                v['angular_J_lower_estimate']>0 and all(max(row)<opt['rim_tolerance'] for pair in v['rim_material_six'].values() for row in pair))
    def admissible(now,old):
        if old['shell_pass']:
            if not now['shell_pass'] or now['eta']>=old['eta']:return False
        elif not now['shell_pass'] and now['shell_violation']>=old['shell_violation']:return False
        if old['target_length_margin']>=0 and now['target_length_margin']<0:return False
        return now['sampled_J_minimum']>.05
    try:
        x=transfer(opt,sp,prior,counts,elapsed)
        for stage_no,stage in enumerate(schedule):
            if elapsed()>args.max_seconds-opt['reserve_seconds']:break
            geom=Grid(stage['spans'],stage['order'])
            verify=Grid(stage['spans'],opt['check_order'],opt['check_split'])
            cross=Grid(stage['spans'],opt['cross_order'],opt['cross_split'])
            measured=lambda K,want:ClosedSpinor(K,max(want,8*K+5))
            kw=measured(stage['K'],stage['angles']);kf=measured(stage['K'],opt['check_angles']);kc=measured(stage['K'],opt['cross_angles'])
            if (sp.spans,sp.K)!=(stage['spans'],stage['K']):
                old=sp;oldx=x.copy();sp=Layout(stage['spans'],stage['K']);x=sp.prolong(old,oldx)
                oldjet=old.space.actual_jets(geom.r,old.split(oldx));newjet=sp.space.actual_jets(geom.r,sp.split(x))
                same=[]
                for a,b in zip(oldjet,newjet):
                    same.append([float(abs(z-w[:,:z.shape[1]]).max()) for z,w in zip(a,b)])
                new_tail=[float(abs(z[:,old.nd:]).max()) if z.shape[1]>old.nd else 0. for z in newjet[0]+newjet[1]]
                counts['true_nested_shape_prolongations']+=1
                emit('nested_spinor_space',previous=[old.spans,old.K],new=[sp.spans,sp.K],radial_jet_differences=same,
                     new_tail=new_tail,coefficients=x.tolist(),seconds=elapsed())
            reference_cache.clear()
            work=evaluate(geom,kw,x,frozen,True);ind=evaluate(verify,kf,x,frozen,True)
            start_eta=ind['read']['eta'];nacc=0;status='iteration_limit'
            supports=sp.masks(geom.r)
            emit('actual_stage',stage=stage_no,space=[sp.spans,sp.K],columns=sp.size,fixed=serialize_reference(),
                 work=work['read'],independent=ind['read'],parameters=x.tolist(),trust=trust,seconds=elapsed())
            for it in range(stage['iterations']):
                if elapsed()>args.max_seconds-opt['reserve_seconds']:status='scientific_budget';break
                rows=work['rows'];active=work['active'];gl=work['global_rows']
                lookup=np.full(active.shape,-1,int);lookup[active]=np.arange(active.sum())
                nlocal=int(active.sum());v=np.r_[rows[active],gl];loss=work['norm']**2
                mat=np.zeros((len(v),sp.size),order='F');h=2.e-24;ref=reference(geom.r,frozen)
                for j,ids in enumerate(supports):
                    y=x.astype(complex);y[j]+=1j*h
                    z,c,sh=state(sp,kw,y,geom.r[ids],None if ref is None else ref[ids])
                    local,_=local_rows(z,sh,geom.guard[ids],opt)
                    selected=active[ids]
                    mat[lookup[ids][selected],j]=local.imag[selected]/h
                    S=work['S']+geom.w[ids]@(np.sqrt(z['E'])-np.sqrt(work['E'][ids]))
                    C=c[0][0,[0,2]] if ids[0]==0 else work['C']
                    global_y,_=length_rows(S,C,opt['work_betas'],opt['length_weight'])
                    mat[nlocal:,j]=global_y.imag/h
                    counts['actual_local_complex_shape_states']+=1
                    counts['all_material_parameter_columns']+=1
                    counts['actual_nonzero_support_radii_for_columns']+=len(ids)
                counts['complete_new_Fourier_physical_J']+=1
                if it==0:
                    d=np.cos(.917*np.arange(1,sp.size+1));d/=np.linalg.norm(d);pred=mat@d;err=[]
                    for eps in (2.e-6,4.e-7):
                        hi=evaluate(geom,kw,x+eps*d,frozen,False);lo=evaluate(geom,kw,x-eps*d,frozen,False)
                        delta=np.r_[(hi['rows']-lo['rows'])[active],hi['global_rows']-lo['global_rows']]/(2*eps)
                        err.append(float(np.linalg.norm(delta-pred)/max(np.linalg.norm(pred),1.e-15)))
                    emit('all_column_actual_difference',stage=stage_no,relative=err,columns=sp.size,rows=len(v))
                    if min(err)>2.e-4:raise ArithmeticError('Full local-support physical derivative differs from actual centered evaluation.')
                ok=False;start_trust=trust
                for variant in range(3):
                    weights=np.ones(len(v))
                    if variant:
                        if variant==1:
                            weights[nlocal:]=8.
                        else:
                            scale=max(float(abs(v[:nlocal]).max()),1.e-12)
                            weights[:nlocal]+=8*abs(v[:nlocal])/scale
                            weights[nlocal:]=4.
                    Q,R=qr(mat*weights[:,None],mode='economic',check_finite=False,overwrite_a=True)
                    rhs=Q.T@(v*weights);del Q
                    u,s,vt=svd(R,full_matrices=False,check_finite=False)
                    force=-(u.T@rhs);counts['full_QR_SVD']+=1
                    emit('complete_spectrum',stage=stage_no,iteration=it,variant=variant,values=s.tolist())
                    rad=start_trust*(.5**variant);least=max(1.e-17,s[0]**2*2.e-13)
                    for trial in range(12):
                        dx,_,damping=trust_step(s,vt,force,rad,least);image=mat@dx
                        pred=float(-2*v@image-image@image);y=x+dx
                        counts['actual_physical_trials']+=1
                        try:
                            nw=evaluate(geom,kw,y,frozen,True)
                            if pred>0 and nw['norm']<work['norm'] and admissible(nw['read'],work['read']):
                                ni=evaluate(verify,kf,y,frozen,True)
                                if ni['norm']<ind['norm'] and admissible(ni['read'],ind['read']):
                                    ratio=(loss-nw['norm']**2)/pred
                                    x=y;work,ind=nw,ni;mu=float(damping);nacc+=1;accepted+=1;ok=True;trust=rad
                                    if ratio>.75:trust=min(opt['max_trust'],trust*1.45)
                                    elif ratio<.2:trust*=.65
                                    emit('accepted_real_parameters',stage=stage_no,iteration=it,variant=variant,total=accepted,
                                         paired_physical=ni['read'],work_norm=nw['norm'],ind_norm=ni['norm'],parameters=x.tolist(),
                                         actual_feasible_shell=nw['read']['shell_pass'] and ni['read']['shell_pass'],
                                         trust=trust,mu=mu,counts=dict(counts),seconds=elapsed());break
                        except FloatingPointError as exc:
                            counts['rejected_physical_domain']+=1
                            emit('rejected_domain',stage=stage_no,iteration=it,variant=variant,trial=trial,reason=str(exc))
                        rad*=.43
                        if rad<1.e-12:break
                    if ok:break
                    trust=rad
                if not ok:status='unaccepted_all_three_models';break
                if frozen is not None and gate(work['read']) and gate(ind['read']) and ind['norm']<opt['goal']:
                    status='fixed_numerical_goal';break
            checked=evaluate(cross,kc,x,frozen,True);last=checked['read']
            history.append(dict(stage=stage_no,space=[sp.spans,sp.K],columns=sp.size,accepted=nacc,status=status,
                                fixed=frozen is not None,start_eta=start_eta,end_cross_eta=last['eta'],norm=checked['norm']))
            emit('stage_end',data=history[-1],physical=last,parameters=x.tolist(),counts=dict(counts),seconds=elapsed())
            if frozen is None and all(gate(a['read']) for a in (work,ind,checked)):
                proposal=(sp,x.copy(),opt['reference_angles'])
                try:
                    checks=[evaluate(g,c,x,proposal,True)['read'] for g,c in ((geom,kw),(verify,kf),(cross,kc))]
                    if all(gate(a) for a in checks):
                        frozen=proposal;del schedule[stage_no+1:]
                        schedule.append(dict(opt['fixed_stage'],K=sp.K+2,spans=sp.spans*2))
                        emit('actual_reference_frozen',reference=serialize_reference(),three_matching_E_reads=checks)
                except FloatingPointError as exc:emit('unfrozen_reference',reason=str(exc))
            if stage_no+1<len(schedule):trust=max(trust,opt['retarget_trust'])
            if status=='scientific_budget':break
        crossed={}
        for label,order,split,nphi in (('radial_only',opt['final_order'],opt['cross_split'],opt['cross_angles']),
            ('angle_only',opt['cross_order'],opt['cross_split'],opt['final_angles']),
            ('both',opt['final_order'],opt['cross_split'],opt['final_angles'])):
            gg=Grid(sp.spans,order,split);kk=ClosedSpinor(sp.K,max(8*sp.K+5,nphi))
            try:crossed[label]=evaluate(gg,kk,x,frozen,True)['read']
            except FloatingPointError as exc:crossed[label]=dict(continuous_gate_unavailable=str(exc))
        emit('terminal',actual_space=[sp.spans,sp.K],all_parameters=x.tolist(),accepted=accepted,stages=history,
             actual_frozen_reference=serialize_reference(),trust=trust,last_mu=mu,full_independent_cross=crossed,
             counts=dict(counts),elapsed_seconds=elapsed(),continuous_certificate=False,README_completion_claim=False)
    except Exception as exc:
        emit('incomplete',reason=str(exc),actual_space=[sp.spans,sp.K],parameters=None if x is None else x.tolist(),
             accepted=accepted,trust=trust,last_mu=mu,actual_frozen_reference=serialize_reference(),paid_counts=dict(counts),
             stages=history,last=last,elapsed_seconds=elapsed(),README_completion_claim=False)
        raise


if __name__=='__main__':main()
