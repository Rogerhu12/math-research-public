"""Public all-column fixed-R738-metric solve with one material height and both real cap centers."""
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
from r748_completed_height_source import Book,prepare
from r748_nested_true_material_height import HeightSpace
from r748_paid_material_height_projection import QuinticHeight
from r748_all_material_rows import Cells,admissible,strict


def emit(event,**data):
    def encode(v):
        if isinstance(v,np.ndarray):return v.tolist()
        if isinstance(v,np.generic):return v.item()
        raise TypeError(type(v).__name__)
    print('R748_'+event.upper(),json.dumps(data,allow_nan=False,default=encode,separators=(',',':')),flush=True)


def solve(opt,req,book,count):
    seed,base,center,base_z,source=prepare(req,opt,book,count)
    emit('projection',**source)
    def scale_seed(factor):
        return QuinticHeight(seed.knots,seed.cosine*factor,seed.sine*factor,True)
    def select_seed():
        # Preserve the full raw transfer. Only repair an invalid true chart or singular actual immersion.
        st=opt['stages'][0];grids=[Cells(opt,st,seed,n) for n in range(3)]
        trials=[]
        for index,factor in enumerate(opt['initial_seed_amplitudes']):
            space=HeightSpace(st,scale_seed(factor),base,center);space.base_inner_height=base_z
            par=np.zeros(space.size);par[:2]=center;passing=True
            for i,g in enumerate(grids):
                def attempt():
                    try:
                        count['initial_real_chart_trials']+=1
                        obs=g.evaluate(space,par,opt,True)
                        return dict(ok=bool(obs['read']['true_sampled_min_s']>opt['s_floor']),observation=obs)
                    except FloatingPointError as exc:return dict(ok=False,reason=str(exc))
                item=book.once(f'chart_{index:02d}_{i}','read',attempt)
                trials.append(dict(scale=factor,grid=i,ok=item['ok'],reason=item.get('reason')))
                if not item['ok']:passing=False;break
            if passing:return dict(scale=factor,index=index,trials=trials,
                   rescaling_error_bounds_at_donor_knots=np.max(abs((1-factor)*seed.cosine),axis=(1,2)))
        return dict(scale=None,trials=trials)
    launch=book.once('selected_actual_height_and_cap_pose','metadata',select_seed)
    if launch['scale'] is None:return dict(kind='no_admissible_positive_projected_seed',launch=launch,genuine_source=source)
    seed=scale_seed(launch['scale'])
    emit('genuine_launch',**launch)
    x=None;previous=None;history=[];accepted=0;mu=None;trust=opt['initial_trust'];xs=None
    for st,stage in enumerate(opt['stages']):
        label=f's{st:02d}';sp=HeightSpace(stage,seed,base,center);sp.base_inner_height=base_z
        if book.has(label+'_complete'):
            last=book.load(label+'_complete');x=last['x'];accepted=last['accepted'];mu=last['mu'];trust=last['trust']
            history=last['history'];xs=last['cross'];previous=sp
            continue
        grids=[Cells(opt,stage,seed,n) for n in range(3)]
        for g in grids:
            # The new whole-domain quadrature basis and E are stage constants.
            sp.prepare(g.grid)
        if previous is None:
            x=np.zeros(sp.size);x[:2]=center
        else:
            def prolong():
                y=sp.prolong(previous,x)
                err=[]
                for g in grids[:2]:
                    old=previous.fields(g.grid,x)[0];new=sp.fields(g.grid,y)[0];K=old.shape[-1]
                    err.append([float(np.max(abs(a-b[:,:K]))) for a,b in zip(old,new)])
                    if new.shape[-1]>K:err.append([float(abs(b[:,K:]).max()) for b in new])
                if max(max(p) for p in err)>opt['prolong_gate']:raise ArithmeticError('Height 0/1/2 jets changed on true nested lift.')
                count['actual_nested_lifts']+=1
                return dict(x=y,full_jet_difference=err)
            x=book.once(label+'_nested','prolong',prolong)['x']
            trust=max(trust,opt['retarget_trust'])
        previous=sp
        def observe(grid,y,full=True):
            count['actual_full_material_surface_states']+=1
            return grid.evaluate(sp,y,opt,full)
        def paid_obs(key,i,y):return book.once(key,'read',lambda:observe(grids[i],y))
        if not book.has(label+'_initial_state'):
            book.save(label+'_initial_state',dict(x=x,trust=trust,mu=mu,accepted=accepted))
            book.checkpoint_state(label+'_initial_state',stage=st,iteration=0,accepted=accepted,trust=trust)
        if st==0:
            work,fine=[book.load(f"chart_{launch['index']:02d}_{i}")['observation'] for i in (0,1)]
        else:
            work=paid_obs(label+'_work',0,x);fine=paid_obs(label+'_fine',1,x)
        emit('stage',stage=st,spans=sp.spans,K=sp.K,cols=sp.size,parameters=x,work=work['read'],fine=fine['read'])
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
                                      accepted=accepted,stage=st,iteration=it,metric='R738_Esharp_Base64'))
            book.checkpoint_state(header,accepted=accepted,stage=st,iteration=it,trust=trust,mu=mu)
            def residual(y):
                z=observe(grids[0],y,False)
                return np.r_[z['rows'][active],z['global_rows']]
            for j0 in range(0,sp.size,step):
                if book.has(bank+'complete_J'):break
                j1=min(j0+step,sp.size)
                book.locate(action='all_nonlocal_column_block',stage=st,iteration=it,first=j0,stop=j1)
                def full_columns():
                    jmat=np.empty((len(v),j1-j0));h=2e-24
                    for j in range(j0,j1):
                        y=x.astype(complex);y[j]+=1j*h;jmat[:,j-j0]=residual(y).imag/h
                        count['full_nonlocal_material_columns']+=1
                    ix=np.flatnonzero(np.any(jmat!=0,axis=1))
                    return dict(kept_rows=ix,values=jmat[ix],height=len(v),first=j0,stop=j1)
                book.once(bank+f'cols_{j0:05d}_{j1:05d}','columns',full_columns)
            def completed():
                count['complete_new_all_height_and_pose_J']+=1
                return dict(shape=shape,column_step=step,all_two_centers=True)
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
                                passed=prop['pred']>0 and z['norm']<parent['norm'] and admissible(z['read'],parent['read'],opt)
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
        cross=(book.load(f"chart_{launch['index']:02d}_2")['observation'] if st==0 and not nacc else
               paid_obs(label+'_cross',2,x))
        xs=cross['read']
        history.append(dict(stage=st,space=[sp.spans,sp.K],size=sp.size,status=status,accepted=nacc,
             norms=[work['norm'],fine['norm'],cross['norm']],etas=[s['read']['eta'] for s in (work,fine,cross)],
             strict_three_discrete_gates=all(strict(z['read'],opt) and z['norm']<opt['goal'] for z in (work,fine,cross))))
        book.save(label+'_complete',dict(x=x,accepted=accepted,trust=trust,mu=mu,history=history,cross=xs))
        book.checkpoint_state(label+'_complete',stage=st,accepted=accepted,trust=trust,mu=mu)
        emit('stage_end',stage=history[-1],physical=xs,parameters=x)
    return dict(kind='terminal',accepted=accepted,parameters=x,trust=trust,mu=mu,history=history,new_final_cross=xs,
                genuine_source=source,selected_input=launch,exact_same_metric_solution_or_time_path_established=False)


def main():
    public();parser=argparse.ArgumentParser();parser.add_argument('--geometry',required=True)
    parser.add_argument('--max-seconds',type=float,required=True);args=parser.parse_args()
    start=time.perf_counter();elapsed=lambda:time.perf_counter()-start
    req=json.loads(Path(os.environ['R748_REQUEST']).read_bytes());opt=json.loads(Path(args.geometry).read_bytes())
    count=Counter();book=Book(req,opt,args.max_seconds,elapsed,count)
    try:final=solve(opt,req,book,count)
    except PaidPause as exc:final=dict(kind='paid_partial',next=str(exc),latest_state=book.ledger['latest_state'],pending=book.ledger['pending'])
    except FloatingPointError as exc:
        final=dict(kind='actual_source_or_current_state_outside_chart',reason=str(exc),latest_state=book.ledger['latest_state'],pending=book.ledger['pending'])
    book.flush();final.update(current_seconds=elapsed(),cumulative_seconds=book.ledger['cumulative_seconds'],
                        counts=dict(count),fingerprint=book.ledger['fingerprint'],global_continuous_certificate=False)
    emit('final',**final)


if __name__=='__main__':main()

