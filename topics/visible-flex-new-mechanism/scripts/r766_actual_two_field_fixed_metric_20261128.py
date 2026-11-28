"""Public R766 full azimuthal curvature and twist Gauss--Codazzi system on the R764 metric."""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import time
import numpy as np
from r703_real_material_mass_continuation_20261128 import public
from r669_true_finite_tilt_reach_continuation_20261128 import trust_step
from r728_closed_spinor_continuation_20261128 import PaidPause,weighted_tree
from r766_paid_positive_metric_source import Book,actual_source
from r766_codazzi_physical_rows import Field,Space,admissible,strict
from r766_single_hermite_physical_surface import all_six
from r738_negative_tail_and_macro_source import THETA


def emit(event,**data):
    def encode(v):
        if isinstance(v,np.ndarray):return v.tolist()
        if isinstance(v,np.generic):return v.item()
        raise TypeError(type(v).__name__)
    print('R766_'+event.upper(),json.dumps(data,allow_nan=False,default=encode,separators=(',',':')),flush=True)


def solve(opt,req,book,count):
    first=Space(opt['stages'][0]);base,launch=actual_source(opt,book,count,first)
    source=launch['source_reference_and_actual_six'];emit('actual_positive_source_projection',**launch)
    accepted=0;mu=None;trust=opt['initial_trust'];previous=None;history=[];xs=None;comparison=None
    x=launch['x']
    for st,stage in enumerate(opt['stages']):
        label=f's{st:02d}';sp=Space(stage)
        if book.has(label+'_complete'):
            last=book.load(label+'_complete');x=last['x'];accepted=last['accepted'];mu=last['mu'];trust=last['trust']
            history=last['history'];xs=last['cross'];previous=sp
            continue
        grids=[Field(book,base,opt,stage,k,sp) for k in range(3)]
        def observe(grid,y,full=True):
            count['actual_full_material_surface_states']+=1
            return grid.evaluate(sp,y,opt,full)
        def paid_obs(key,i,y):return book.once(key,'read',lambda:observe(grids[i],y))
        if previous is not None:
            def prolong():
                y=sp.prolong(previous,x);out=[]
                for detail,gr in enumerate(grids[:2]):
                    from r766_gauss_codazzi_material_frame import Frame
                    oldframe=Frame(previous,gr.grid,gr.phi,base,book)
                    old=all_six(oldframe,previous,x);new=all_six(gr.frame,sp,y)
                    out.append([float(abs(a-b).max()) for a,b in zip(old['actual_six']+(old['design_n'],old['normal_scalar']),
                         new['actual_six']+(new['design_n'],new['normal_scalar']))])
                if max(max(t) for t in out)>opt['prolong_gate']:raise ArithmeticError('True body changed on nested lift.')
                count['new_nested_all_coeff_lifts']+=1
                return dict(x=y,full_six_plus_n_and_c=out)
            x=book.once(label+'_nested','prolong',prolong)['x']
            trust=max(trust,opt['retarget_trust'])
        if st==0:
            def signed_start():
                options=[]
                for index,amplitude in enumerate(opt['actual_projection_amplitudes']):
                    y=x.copy();y[3:]*=amplitude
                    seen=[]
                    for i in range(3):
                        def observe_signed():
                            try:return dict(observation=observe(grids[i],y))
                            except FloatingPointError as exc:return dict(invalid=str(exc))
                        item=book.once(f'signed_{index}_{i}','read',observe_signed)
                        if 'invalid' in item:break
                        seen.append(item['observation'])
                    if len(seen)!=3:continue
                    hard=all(o['read']['whole_deep_pass'] for o in seen)
                    if hard:options.append((index,y,seen))
                if not options:raise FloatingPointError('No physical positive-metric seed passes even the native deep and pose guards.')
                # Select by real shell feasibility first, then violation and residual on BOTH independent grids.
                index,y,seen=min(options,key=lambda t:(not all(o['read']['shell_pass'] for o in t[2]),
                        max(o['read']['violation'] for o in t[2]),max(o['norm'] for o in t[2])))
                return dict(index=index,x=y,actual_seed_count=len(options))
            chosen=book.once('selected_actual_projection_amplitude','metadata',signed_start)
            x=chosen['x'];work,fine=[book.load(f"signed_{chosen['index']}_{i}")['observation'] for i in (0,1)]
        else:
            work=paid_obs(label+'_work',0,x);fine=paid_obs(label+'_fine',1,x)
        previous=sp
        if not book.has(label+'_initial_state'):
            book.save(label+'_initial_state',dict(x=x,trust=trust,mu=mu,accepted=accepted))
            book.checkpoint_state(label+'_initial_state',stage=st,iteration=0,accepted=accepted,trust=trust)
        emit('stage',stage=st,K=sp.K,columns=sp.size,parameters=x,work=work['read'],fine=fine['read'])
        status='iteration_limit';nacc=0
        for it in range(stage['iterations']):
            tag=label+f'_i{it:03d}_';bank=tag+'model_';done=tag+'successor'
            if book.has(done):
                result=book.load(done)
                x,trust,mu,accepted,nacc,status=[result[k] for k in ('x','trust','mu','accepted','nacc','status')]
                if result['ok']:work,fine=result['work'],result['fine']
                if not result['ok'] or status=='fixed_grid_goal':break
                continue
            active=work['active'];nlocal=int(active.sum());v=np.r_[work['rows'][active],work['global_rows']]
            header=bank+'base';shape=(len(v),sp.size);step=opt['column_block']
            book.once(header,'metadata',lambda:dict(x=x,rows=v,active=active,nlocal=nlocal,shape=shape,trust=trust,mu=mu,
                                      accepted=accepted,stage=st,iteration=it,metric='R764_positive_slope_squared_fixed_E'))
            book.checkpoint_state(header,accepted=accepted,stage=st,iteration=it,trust=trust,mu=mu)
            def residual(y):
                z=observe(grids[0],y,False)
                return np.r_[z['rows'][active],z['global_rows']]
            for j0 in range(0,sp.size,step):
                if book.has(bank+'complete_J'):break
                j1=min(j0+step,sp.size)
                book.locate(action='all_Gauss_Codazzi_nonlocal_column_block',stage=st,iteration=it,first=j0,stop=j1)
                def full_columns():
                    jmat=np.empty((len(v),j1-j0));h=2e-24
                    for j in range(j0,j1):
                        y=x.astype(complex);y[j]+=1j*h;jmat[:,j-j0]=residual(y).imag/h
                        count['full_nonlocal_material_columns']+=1
                    ix=np.flatnonzero(np.any(jmat!=0,axis=1))
                    return dict(kept_rows=ix,values=jmat[ix],height=len(v),first=j0,stop=j1)
                book.once(bank+f'cols_{j0:05d}_{j1:05d}','columns',full_columns)
            def completed():
                count['complete_new_all_material_generator_and_pose_J']+=1
                return dict(shape=shape,column_step=step,all_three_centers=True,all_u_v_columns=True)
            book.once(bank+'complete_J','metadata',completed)
            if it==0:
                d=np.cos(.901*np.arange(1,sp.size+1));d/=np.linalg.norm(d)
                def action():
                    val=np.zeros(len(v))
                    for j0 in range(0,sp.size,step):
                        j1=min(j0+step,sp.size);p=book.load(bank+f'cols_{j0:05d}_{j1:05d}')
                        val[p['kept_rows']]+=p['values']@d[j0:j1]
                    return val
                image=book.once(bank+'unweighted_Jd','fd',action);errs=[]
                for i,e in enumerate((2e-6,4e-7)):
                    def difference():
                        q=(residual(x+e*d)-residual(x-e*d))/(2*e)
                        return float(np.linalg.norm(q-image)/max(1e-15,np.linalg.norm(image)))
                    errs.append(book.once(bank+'centered'+str(i),'fd',difference))
                emit('all_columns_finite_difference',relative=errs,shape=shape)
                if min(errs)>opt['fd_tolerance']:raise ArithmeticError('Actual centered full-column derivative failed.')
            supports=[np.arange(len(active))]*sp.size
            ok=False;start=trust
            for variant in range(3):
                book.locate(action='complete_TSQR',stage=st,iteration=it,variant=variant)
                model=weighted_tree(book,bank,sp,variant,v,nlocal,active,supports,step,opt['tsqr_radial_block'],count,emit)
                if variant==0:R=model['R'];rhs=model['weighted_projected_residual']
                rad=start*.5**variant
                for j in range(opt['trials']):
                    key=bank+f'v{variant}_t{j:02d}'
                    book.locate(action='trial_proposal',stage=st,iteration=it,variant=variant,trial=j,radius=rad)
                    def proposal():
                        dx,_,damping=trust_step(model['s'],model['vt'],model['force'],rad,model['least'])
                        delta=R@dx
                        return dict(x=x+dx,dx=dx,damping=damping,pred=float(-2*rhs@delta-delta@delta),radius=rad)
                    prop=book.once(key+'_proposal','proposal',proposal);y=prop['x']
                    book.locate(action='actual_trial',stage=st,iteration=it,variant=variant,trial=j,paid_proposal=key+'_proposal')
                    trial=[]
                    for i,parent in enumerate((work,fine)):
                        def check():
                            try:
                                z=observe(grids[i],y);count['actual_material_trials']+=1
                                passed=prop['pred']>0 and z['norm']<parent['norm'] and admissible(z['read'],parent['read'])
                                return dict(ok=bool(passed),observation=z if passed else dict(norm=z['norm'],read=z['read']))
                            except FloatingPointError as exc:
                                count['invalid_chart_or_immersion_trials']+=1
                                return dict(ok=False,reason=str(exc))
                        t=book.once(key+f'_real{i}','trial',check)
                        if not t['ok']:break
                        trial.append(t['observation'])
                    if len(trial)==2:
                        ratio=(work['norm']**2-trial[0]['norm']**2)/prop['pred']
                        work,fine=trial;x=y;accepted+=1;nacc+=1;mu=prop['damping']
                        trust=min(opt['max_trust'],rad*(1.45 if ratio>.75 else .65 if ratio<.2 else 1.))
                        ok=True;emit('accepted',stage=st,iteration=it,total=accepted,parameters=x,trust=trust,
                             work=work['read'],fine=fine['read'],counts=dict(count),seconds=book.elapsed())
                        break
                    rad*=.43
                if ok:break
                trust=rad
            if not ok:status='all_three_models_unaccepted'
            elif all(strict(p['read'],opt) and p['norm']<opt['goal'] for p in (work,fine)):status='fixed_grid_goal'
            result=dict(x=x,accepted=accepted,nacc=nacc,mu=mu,trust=trust,ok=ok,status=status)
            if ok:result.update(work=work,fine=fine)
            book.save(done,result);book.checkpoint_state(done,stage=st,iteration=it,accepted=accepted,trust=trust,mu=mu)
            if ok:book.retire_accepted_model(bank)
            if not ok or status=='fixed_grid_goal':break
        cross=(book.load(f"signed_{chosen['index']}_2")['observation'] if st==0 and not nacc else
               paid_obs(label+'_cross',2,x))
        xs=cross['read']
        comparison=xs['independent_halfstep_and_actual_ODE_defect']
        comparison_ok=(comparison['independent_bisected_shell']['shell_pass'] and
            max(comparison['independent_common_F_and_five'])<opt['integration_goal'] and
            comparison['sampled_true_Hermite_frame_ODE_defect']<opt['integration_goal'])
        history.append(dict(stage=st,space=[stage['spans'],sp.K],size=sp.size,status=status,accepted=nacc,
             norms=[work['norm'],fine['norm'],cross['norm']],etas=[s['read']['eta'] for s in (work,fine,cross)],
             strict_three_discrete_gates=comparison_ok and all(strict(z['read'],opt) and z['norm']<opt['goal'] for z in (work,fine,cross))))
        book.save(label+'_complete',dict(x=x,accepted=accepted,trust=trust,mu=mu,history=history,cross=xs))
        book.checkpoint_state(label+'_complete',stage=st,accepted=accepted,trust=trust,mu=mu)
        emit('stage_end',stage=history[-1],physical=xs,parameters=x)
    return dict(kind='terminal',accepted=accepted,parameters=x,trust=trust,mu=mu,history=history,new_final_cross=xs,
                genuine_source=source,selected_input=launch,exact_same_metric_solution_or_time_path_established=False)


def main():
    public();parser=argparse.ArgumentParser();parser.add_argument('--geometry',required=True)
    parser.add_argument('--max-seconds',type=float,required=True);args=parser.parse_args()
    start=time.perf_counter();elapsed=lambda:time.perf_counter()-start
    req=json.loads(Path(os.environ['R766_REQUEST']).read_bytes());opt=json.loads(Path(args.geometry).read_bytes())
    count=Counter();book=Book(req,opt,args.max_seconds,elapsed,count)
    try:final=solve(opt,req,book,count)
    except PaidPause as exc:final=dict(kind='paid_partial',next=str(exc),latest_state=book.ledger['latest_state'],pending=book.ledger['pending'])
    except FloatingPointError as exc:
        final=dict(kind='actual_source_or_current_state_outside_positive_curvature_chart',reason=str(exc),latest_state=book.ledger['latest_state'],pending=book.ledger['pending'])
    book.flush();final.update(current_seconds=elapsed(),cumulative_seconds=book.ledger['cumulative_seconds'],
                        counts=dict(count),fingerprint=book.ledger['fingerprint'],global_continuous_certificate=False)
    emit('final',**final)


if __name__=='__main__':main()
