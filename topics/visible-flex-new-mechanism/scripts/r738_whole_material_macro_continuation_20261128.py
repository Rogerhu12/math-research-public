"""All-column finite-angle R738 solver on one prescribed material metric, including phase zero."""
import argparse
from collections import Counter
import json
from pathlib import Path
import time
import numpy as np
from r669_true_finite_tilt_reach_continuation_20261128 import trust_step
from r703_real_material_mass_continuation_20261128 import public,emit
from r726_closed_spinor_fourier import ClosedSpinor
from r728_closed_spinor_continuation_20261128 import PaidPause,weighted_tree
from r728_full_spinor_geometry import state,local_rows,length_rows,actual_read
from r738_macro_spline_space import Layout,Grid
from r738_deep_cap_bounds import omitted_sectors
from r738_paid_true_native_input import SolveBook,source_fields,NativeBook
from r738_real_macro_reference import Base


def strict_gate(v,opt):
    if not v['shell_pass'] or not v['whole_deep_pass']:return False
    if v['eta']>opt['freeze_eta'] or v['target_length_margin']<0:return False
    if v['angular_J_lower_estimate']<=0:return False
    if max(max(q) for rim in v['rim_material_six'].values() for q in rim)>opt['rim_tolerance']:return False
    reads=v['finite_identity_disagreements']
    names=('mean_J_minus_target_0_1_2','mean_V_closure_0_1_2','interpolated_Phi_psi_minus_J_radial_0_1_2',
              'interpolated_U_psi_minus_V_radial_0_1_2')
    return all(all(d*h<t for d,h,t in zip(reads[key],(1.,.145,.145**2),(5.e-11,5.e-10,5.e-8))) for key in names)


def admissible(now,old):
    return (now['shell_pass'] and now['whole_deep_pass'] and now['sampled_J_minimum']>.05 and
        now['target_length_margin']>=0 and now['eta']<old['eta'])

def mixed_envelopes(curve,c,deep,shell):
    """Mixed pairs between either omitted sector, all sampled annulus points, and both true rigid pieces."""
    import math
    F=curve[0];s=.27;co=math.sqrt(1-s*s);d,h=c[0][0,[0,2]]
    ra=max(np.linalg.norm(F[...,:2],axis=-1).max(),*(float(v['max_radius_upper']) for v in deep))
    lo=min(F[...,2].min(),*(float(v['minimum_z_lower']) for v in deep))
    hi=max(F[...,2].max(),*(float(v['maximum_z_upper']) for v in deep))
    pieces=[(ra,lo,hi),(abs(d)+.075+.0336*s,h-.075*s,h+.0336*co+.075*s),
            (abs(d)+.043+.28*s,h-.043*s,h+.28*co+.043*s)]
    radius=max(q[0] for q in pieces);zmin=min(q[1] for q in pieces);zmax=max(q[2] for q in pieces)
    diam=max(shell['sampled_whole_D_upper_estimate'],math.hypot(2*radius,zmax-zmin),
          *(.04501+math.hypot(a+k,max(abs(l-o),abs(u-o))) for a,l,u in pieces for k,o in ((.285,-.045),(.56,-.335))))
    dominance=min(shell['sampled_whole_support_dominance'],*(.335*co-.56*s+.04499-s*float(q['max_radius_upper'])
               +co*float(q['minimum_z_lower']) for q in deep))
    return dict(mixed_diameter_upper_estimate=float(diam),mixed_support_margin_estimate=float(dominance),
             admissible=bool(diam<1 and dominance>0))


def main():
    public()
    ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',type=float,required=True)
    args=ap.parse_args();opt=json.loads(Path(args.geometry).read_bytes())
    started=time.perf_counter();elapsed=lambda:time.perf_counter()-started
    counts=Counter();history=[];accepted=0;last=None;sp=None;x=None;trust=opt['initial_trust'];mu=None
    book=SolveBook(opt,args.max_seconds,elapsed,counts)
    schedule=list(opt['stages']);layouts={};first=schedule[0]
    def layout(n,k,depth,fi=0):
        key=(n,k,depth,fi)
        if key not in layouts:layouts[key]=Layout(n,k,depth,allfields[fi],scales)
        return layouts[key]
    def grid(st,ordr,split,fi):
        g=Grid(st['spans'],ordr,split,st['depth']);g.fi=fi
        return g
    def evaluate(g,k,y,unused,physical):
        ls=layout(sp.spans,sp.K,sp.depth,g.fi)
        ref=common_E.paid(g.r)['reference_E'];z,c,sh=state(ls,k,y,g.r,ref)
        counts['full_real_candidate_shape_states']+=1
        rows,active=local_rows(z,sh,g.guard,opt)
        S=g.w@np.sqrt(ref);C=c[0][0,[0,2]]
        gl,_=length_rows(S,C,opt['work_betas'],opt['length_weight'])
        read=None
        if physical:
            read=actual_read(g,z,c,sh,opt['fine_betas'])
            read['ordinary_fine_eta']=read['eta']
            sectors=omitted_sectors(ls.split(y)[3],scales,cost,c[0][0])
            read['omitted_native_entire_old_caps']=sectors;read['whole_deep_pass']=all(v['available'] for v in sectors)
            read['deep_target_length_truncation_upper']=g.deep_radial_length_error_upper
            if read['whole_deep_pass']:
                read['whole_eta_upper_on_omitted']=max(float(v['normalized_metric_operator_upper']) for v in sectors)
                read['eta']=max(read['eta'],read['whole_eta_upper_on_omitted'])
                read['mixed_across_all_three_parts']=[mixed_envelopes(z,c,sectors,o['shell']) for z,o in zip(sh,read['paired'])]
                read['shell_pass'] &= all(v['admissible'] for v in read['mixed_across_all_three_parts'])
            read['actual_center_for_all_sectors']=c[0][0].tolist()
            read['fixed_reference_vs_base_quadrature_E_difference']=float(np.max(abs(ref-ls.fields.raw(g.r)[2])))
            counts['paired_complete_physical_reads']+=1
        return dict(rows=rows,active=active,global_rows=gl,S=S,C=C,E=ref,read=read,
                    norm=float(np.linalg.norm(np.r_[rows.ravel(),gl])))
    def cached_observation(key,g,k,y,bind,physical=True):
        return book.once(key,'read',lambda:evaluate(g,k,y,bind,physical))
    def gate(v):return strict_gate(v,opt)
    try:
        fields,rays,scales,cost=source_fields(book,opt,counts,emit)
        allfields=fields+rays
        # Every work, independent, endpoint ray, and final solve uses this single finite target evaluator.
        common_E=Base(opt['fixed_reference_order'],NativeBook(book),counts)
        sp=layout(first['spans'],first['K'],first['depth'])
        x=np.zeros(sp.size)
        if book.ledger['latest_state'] is None:
            book.once('genuine_macroscopic_initial_field','metadata',lambda:dict(x=x,space=[sp.spans,sp.K,sp.depth],phase_zero_metric_solved=False))
            book.checkpoint_state('genuine_macroscopic_initial_field',accepted=0,space=[sp.spans,sp.K,sp.depth],trust=trust)
        for stage_no,stage in enumerate(schedule):
            stage_key=f's{stage_no:02d}'
            completed=stage_key+'_complete'
            if book.has(completed):
                done=book.load(completed)
                sp=layout(*done['space']);x=done['x']
                trust,mu,accepted=done['trust'],done['mu'],done['accepted']
                history=done['history'];schedule[:]=done['schedule'];last=done['read']
                continue
            geom=grid(stage,stage['order'],1,0)
            verify=grid(stage,opt['check_order'],opt['check_split'],1)
            cross=grid(stage,opt['cross_order'],opt['cross_split'],1)
            measured=lambda K,want:ClosedSpinor(K,max(want,8*K+5))
            kw=measured(stage['K'],stage['angles']);kf=measured(stage['K'],opt['check_angles']);kc=measured(stage['K'],opt['cross_angles'])
            book.locate(stage=stage_no,action='initial_physical_reads',fixed=True)
            if (sp.spans,sp.K,sp.depth)!=(stage['spans'],stage['K'],stage['depth']):
                old=sp;oldx=x.copy();sp=layout(stage['spans'],stage['K'],stage['depth'])
                def prolong():
                    promoted=sp.prolong(old,oldx)
                    oldjet=old.space.actual_jets(geom.r,old.split(oldx));newjet=sp.space.actual_jets(geom.r,sp.split(promoted))
                    same=[[float(abs(z-w[:,:z.shape[1]]).max()) for z,w in zip(a,b)] for a,b in zip(oldjet,newjet)]
                    tail=[float(abs(z[:,old.nd:]).max()) if z.shape[1]>old.nd else 0. for z in newjet[0]+newjet[1]]
                    counts['true_nested_shape_prolongations']+=1
                    emit('nested_spinor_space',previous=[old.spans,old.K],new=[sp.spans,sp.K,sp.depth],radial_jet_differences=same,
                         new_tail=tail,coefficients=promoted.tolist(),seconds=elapsed())
                    if max(max(z) for z in same)>2.e-6 or max(tail)>2.e-6:
                        raise ArithmeticError('Nested field transfer changed physical radial two-jets.')
                    return promoted
                x=book.once(stage_key+'_prolong','prolong',prolong)
            
            work=cached_observation(stage_key+'_work',geom,kw,x,True)
            ind=cached_observation(stage_key+'_independent',verify,kf,x,True)
            start_eta=ind['read']['eta'];nacc=0;status='iteration_limit'
            supports=sp.masks(geom.r)
            emit('actual_stage',stage=stage_no,space=[sp.spans,sp.K,sp.depth],columns=sp.size,fixed='prescribed_R738_E_sharp',
                 work=work['read'],independent=ind['read'],parameters=x.tolist(),trust=trust,seconds=elapsed())
            for it in range(stage['iterations']):
                tag=stage_key+f'_i{it:03d}'
                finished=tag+'_successor';bank=tag+'_model_'
                if book.has(finished):
                    result=book.load(finished)
                    trust,mu,accepted,nacc,status=(result[k] for k in ('trust','mu','accepted','nacc','status'))
                    if not result['ok']:break
                    x,work,ind=result['x'],result['work'],result['ind']
                    if status=='fixed_numerical_goal':break
                    continue
                rows=work['rows'];active=work['active'];gl=work['global_rows']
                lookup=np.full(active.shape,-1,int);lookup[active]=np.arange(active.sum())
                nlocal=int(active.sum());v=np.r_[rows[active],gl];loss=work['norm']**2
                h=2.e-24;ref=work['E']
                if it==0:
                    d=np.cos(.917*np.arange(1,sp.size+1));d/=np.linalg.norm(d)
                header=bank+'base'
                book.locate(stage=stage_no,iteration=it,action='complete_column_blocks',base=header)
                book.once(header,'metadata',lambda:dict(x=x,space=[sp.spans,sp.K,sp.depth],rows=v,local_mask=active,
                    local_row_count=nlocal,complete_shape=[len(v),sp.size],source_trust=trust,prescribed_metric='prescribed_R738_E_sharp'))
                book.checkpoint_state(header,stage=stage_no,iteration=it,space=[sp.spans,sp.K,sp.depth],accepted=accepted,trust=trust,mu=mu)
                for j0 in range(0,sp.size,opt['column_block']):
                    if book.has(bank+'complete_J'):break
                    j1=min(sp.size,j0+opt['column_block'])
                    def columns():
                        block=np.zeros((len(v),j1-j0))
                        for j in range(j0,j1):
                            ids=supports[j];y=x.astype(complex);y[j]+=1j*h
                            z,c,sh=state(sp,kw,y,geom.r[ids],ref[ids])
                            local,_=local_rows(z,sh,geom.guard[ids],opt);selected=active[ids]
                            block[lookup[ids][selected],j-j0]=local.imag[selected]/h
                            S=work['S']+geom.w[ids]@(np.sqrt(z['E'])-np.sqrt(work['E'][ids]))
                            C=c[0][0,[0,2]] if ids[0]==0 else work['C']
                            gy,_=length_rows(S,C,opt['work_betas'],opt['length_weight'])
                            block[nlocal:,j-j0]=gy.imag/h
                            counts['actual_local_complex_shape_states']+=1
                            counts['all_material_parameter_columns']+=1
                            counts['actual_nonzero_support_radii_for_columns']+=len(ids)
                        paid=np.flatnonzero(np.any(block!=0,axis=1))
                        return dict(first=j0,stop=j1,kept_rows=paid,values=block[paid],height=len(v))
                    chunk=book.once(bank+f'cols_{j0:05d}_{j1:05d}','columns',columns)
                    if chunk['first']!=j0 or chunk['stop']!=j1 or chunk['height']!=len(v):raise ArithmeticError('Wrong paid column block layout.')
                def assembled():
                    counts['complete_new_Fourier_physical_J']+=1
                    return dict(rows=len(v),columns=sp.size,block_size=opt['column_block'])
                book.once(bank+'complete_J','metadata',assembled)
                if it==0:
                    def directional():
                        out=np.zeros(len(v))
                        for j0 in range(0,sp.size,opt['column_block']):
                            j1=min(j0+opt['column_block'],sp.size)
                            part=book.load(bank+f'cols_{j0:05d}_{j1:05d}')
                            out[part['kept_rows']]+=part['values']@d[j0:j1]
                        return out
                    pred=book.once(bank+'full_unweighted_directional_action','fd',directional);err=[]
                    for ei,eps in enumerate((2.e-6,4.e-7)):
                        def actual_fd():
                            hi=evaluate(geom,kw,x+eps*d,True,False);lo=evaluate(geom,kw,x-eps*d,True,False)
                            delta=np.r_[(hi['rows']-lo['rows'])[active],hi['global_rows']-lo['global_rows']]/(2*eps)
                            return float(np.linalg.norm(delta-pred)/max(np.linalg.norm(pred),1.e-15))
                        err.append(book.once(bank+'fd_'+str(ei),'fd',actual_fd))
                    emit('all_column_actual_difference',stage=stage_no,relative=err,columns=sp.size,rows=len(v))
                    if min(err)>2.e-4:raise ArithmeticError('Full local-support derivative differs from actual centered evaluation.')
                ok=False;start_trust=trust
                for variant in range(3):
                    vtag=bank+f'variant{variant}'
                    book.locate(stage=stage_no,iteration=it,variant=variant,action='whole_QR_SVD',base=header)
                    model=weighted_tree(book,bank,sp,variant,v,nlocal,active,supports,opt['column_block'],
                                          stage['order']+1,counts,emit)
                    if variant==0:
                        raw_R=model['R'];raw_rhs=model['weighted_projected_residual']
                    rad=start_trust*(.5**variant)
                    for trial in range(12):
                        ttag=vtag+f'_trial{trial:02d}'
                        book.locate(stage=stage_no,iteration=it,variant=variant,trial=trial,base=header,
                                    factorization=vtag+'_QR_SVD',trust=float(rad),next_proposal=ttag+'_step')
                        def proposal():
                            dx,_,damping=trust_step(model['s'],model['vt'],model['force'],rad,model['least'])
                            image=raw_R@dx
                            return dict(dx=dx,y=x+dx,mu=float(damping),prediction=float(-2*raw_rhs@image-image@image),radius=float(rad))
                        step=book.once(ttag+'_step','proposal',proposal)
                        book.locate(stage=stage_no,iteration=it,variant=variant,trial=trial,base=header,
                                    factorization=vtag+'_QR_SVD',paid_next_real_parameters=ttag+'_step')
                        y=step['y'];pred=step['prediction'];damping=step['mu']
                        def trial_work():
                            counts['actual_physical_trials']+=1
                            try:
                                test=evaluate(geom,kw,y,True,True)
                                if pred>0 and test['norm']<work['norm'] and admissible(test['read'],work['read']):
                                    return dict(ok=True,observation=test)
                                return dict(ok=False,read=test['read'],norm=test['norm'])
                            except FloatingPointError as exc:
                                counts['rejected_physical_domain']+=1
                                return dict(ok=False,reason=str(exc))
                        tw=book.once(ttag+'_work','trial',trial_work)
                        if tw['ok']:
                            def trial_fine():
                                try:
                                    test=evaluate(verify,kf,y,True,True)
                                    if test['norm']<ind['norm'] and admissible(test['read'],ind['read']):
                                        return dict(ok=True,observation=test)
                                    return dict(ok=False,read=test['read'],norm=test['norm'])
                                except FloatingPointError as exc:
                                    counts['rejected_physical_domain']+=1
                                    return dict(ok=False,reason=str(exc))
                            tf=book.once(ttag+'_independent','trial',trial_fine)
                            if tf['ok']:
                                nw,ni=tw['observation'],tf['observation'];ratio=(loss-nw['norm']**2)/pred
                                x=y;work,ind=nw,ni;mu=damping;nacc+=1;accepted+=1;ok=True;trust=rad
                                if ratio>.75:trust=min(opt['max_trust'],trust*1.45)
                                elif ratio<.2:trust*=.65
                                emit('accepted_real_parameters',stage=stage_no,iteration=it,variant=variant,total=accepted,
                                     paired_physical=ind['read'],work_norm=work['norm'],ind_norm=ind['norm'],parameters=x.tolist(),
                                     actual_feasible_shell=work['read']['shell_pass'] and ind['read']['shell_pass'],
                                     trust=trust,mu=mu,counts=dict(counts),seconds=elapsed());break
                        rad*=.43
                        if rad<1.e-12:break
                    if ok:break
                    trust=rad
                if not ok:status='unaccepted_all_three_models'
                elif gate(work['read']) and gate(ind['read']) and ind['norm']<opt['goal']:status='fixed_numerical_goal'
                result=dict(ok=ok,trust=trust,mu=mu,accepted=accepted,nacc=nacc,status=status)
                if ok:result.update(x=x,work=work,ind=ind)
                book.save(finished,result)
                book.checkpoint_state(finished,stage=stage_no,iteration=it,accepted=accepted,space=[sp.spans,sp.K,sp.depth],trust=trust,mu=mu)
                if ok:book.retire_accepted_model(bank)
                if not ok or status=='fixed_numerical_goal':break
            book.locate(stage=stage_no,action='stage_cross',accepted=accepted)
            checked=cached_observation(stage_key+'_cross',cross,kc,x,True);last=checked['read']
            history.append(dict(stage=stage_no,space=[sp.spans,sp.K,sp.depth],columns=sp.size,accepted=nacc,status=status,
                                fixed=True,start_eta=start_eta,end_cross_eta=last['eta'],norm=checked['norm']))
            emit('stage_end',data=history[-1],physical=last,parameters=x.tolist(),counts=dict(counts),seconds=elapsed())
            if stage_no+1<len(schedule):trust=max(trust,opt['retarget_trust'])
            book.save(completed,dict(x=x,space=[sp.spans,sp.K,sp.depth],trust=trust,mu=mu,accepted=accepted,
                       prescribed_metric='prescribed_R738_E_sharp',history=history,schedule=schedule,read=last))
            book.checkpoint_state(completed,stage=stage_no,accepted=accepted,space=[sp.spans,sp.K,sp.depth])
        crossed={}
        for label,order,split,nphi in (('radial_only',opt['final_order'],opt['cross_split'],opt['cross_angles']),
            ('angle_only',opt['cross_order'],opt['cross_split'],opt['final_angles']),
            ('both',opt['final_order'],opt['cross_split'],opt['final_angles'])):
            book.locate(action='final_independent_cross',label=label,accepted=accepted)
            gg=grid(dict(spans=sp.spans,depth=sp.depth),order,split,1);kk=ClosedSpinor(sp.K,max(8*sp.K+5,nphi))
            def cross_read():
                try:return evaluate(gg,kk,x,True,True)['read']
                except FloatingPointError as exc:return dict(continuous_gate_unavailable=str(exc))
            crossed[label]=book.once('final_'+label,'read',cross_read)
        for fi in (2,3):
            alias=grid(dict(spans=sp.spans,depth=sp.depth),opt['cross_order'],opt['cross_split'],fi)
            kk=ClosedSpinor(sp.K,max(8*sp.K+5,opt['final_angles']))
            def endpoint_ray():
                try:return evaluate(alias,kk,x,True,True)['read']
                except FloatingPointError as exc:return dict(unavailable=str(exc))
            crossed['old_input_ray_'+str(fi)]=book.once('endpoint_ray_'+str(fi),'read',endpoint_ray)
        book.ledger['pending']=None;book.checkpoint_state('terminal',accepted=accepted,space=[sp.spans,sp.K,sp.depth])
        emit('terminal',actual_space=[sp.spans,sp.K,sp.depth],all_parameters=x.tolist(),accepted=accepted,stages=history,
             prescribed_metric='prescribed_R738_E_sharp',trust=trust,last_mu=mu,full_independent_cross=crossed,
             counts=dict(counts),elapsed_seconds=elapsed(),cumulative_seconds=book.ledger['cumulative_seconds'],
             fingerprint=book.ledger['fingerprint'],continuous_certificate=False,README_completion_claim=False)
    except PaidPause:
        book.flush()
        emit('paid_partial',next_paid_unit=book.ledger['pending'],latest_resume=book.ledger['latest_state'],
             fingerprint=book.ledger['fingerprint'],files_kept=len(book.ledger['kept']),files_superseded=len(book.ledger['retired']),
             actual_space=None if sp is None else [sp.spans,sp.K,sp.depth],all_parameters=None if x is None else x.tolist(),accepted=accepted,trust=trust,last_mu=mu,
             prescribed_metric='prescribed_R738_E_sharp',counts=dict(counts),elapsed_seconds=elapsed(),
             cumulative_seconds=book.ledger['cumulative_seconds'],continuous_certificate=False,README_completion_claim=False)
    except Exception as exc:
        book.flush()
        emit('incomplete',reason=str(exc),actual_space=None if sp is None else [sp.spans,sp.K,sp.depth],parameters=None if x is None else x.tolist(),
             accepted=accepted,trust=trust,last_mu=mu,prescribed_metric='prescribed_R738_E_sharp',paid_counts=dict(counts),
             pending=book.ledger['pending'],stages=history,last=last,elapsed_seconds=elapsed(),README_completion_claim=False)
        raise


if __name__=='__main__':main()
