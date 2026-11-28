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



class PaidPause(Exception):
    pass


class PaidBook:
    """Typed JSON and numeric NPZ receipts. Loading never unpickles Python objects."""
    def __init__(self,opt,limit,elapsed,counts):
        import hashlib,os,scipy
        self.hashlib,self.os,self.elapsed,self.counts=hashlib,os,elapsed,counts
        self.limit,self.reserve=limit,opt['reserve_seconds']
        self.root=Path(os.environ['RUNNER_TEMP'])/'r728-paid-checkpoint'
        self.root.mkdir(parents=True,exist_ok=True)
        self.ledger_file=self.root/'ledger.json'
        req=json.loads(Path(os.environ['R728_REQUEST']).read_bytes())
        scientific={k:v for k,v in req['source_sha256'].items() if
               k.endswith('.py') or k in (req['common_parameters']['geometry'],opt['frame'])}
        semantic=dict(schema='r728-paid-v1',sources=scientific,config=opt,
                      runtime=[np.__version__,scipy.__version__],source_final='bd5a52dcc40e31e898d3e02b99e4e5c0d449bfd697ac95faa8a168082c6012b2')
        identity=hashlib.sha256(json.dumps(semantic,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        if self.ledger_file.exists():
            self.ledger=json.loads(self.ledger_file.read_bytes())
            if self.ledger.get('fingerprint')!=identity:raise ValueError('Paid scientific object differs from the bound solver/field/space.')
            counts.update(self.ledger['counts'])
        else:
            self.ledger=dict(schema='r728-paid-v1',fingerprint=identity,semantic=semantic,kept={},retired={},
                counts={},unit_max_seconds={},runs=[],cumulative_seconds=0.,latest_state=None,pending=None,context={})
        self.prior_seconds=self.ledger['cumulative_seconds']
        self.ledger['runs'].append(dict(id=os.environ.get('GITHUB_RUN_ID'),attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
                                   source=os.environ.get('GITHUB_SHA'),opening_paid_seconds=self.prior_seconds))
        literal=(Path(os.environ['RUNNER_TEMP'])/'r728-r703-natural-final.json').read_bytes()
        if hashlib.sha256(literal).hexdigest()!=semantic['source_final']:raise ValueError('Missing protected source final literal.')
        (self.root/'r703-original-final.json').write_bytes(literal)
        self.flush()
    def flush(self):
        self.ledger['counts']=dict(self.counts)
        self.ledger['cumulative_seconds']=self.prior_seconds+self.elapsed()
        tmp=self.ledger_file.with_suffix('.tmp')
        tmp.write_text(json.dumps(self.ledger,sort_keys=True,allow_nan=False,separators=(',',':')))
        self.os.replace(tmp,self.ledger_file)
    def digest(self,path):
        with path.open('rb') as f:
            return self.hashlib.file_digest(f,'sha256').hexdigest()
    def has(self,key):return key in self.ledger['kept']
    def save(self,key,data):
        if not key or any(ch not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-' for ch in key):
            raise ValueError('Invalid internal checkpoint key.')
        arrays={}
        def flatten(v):
            if isinstance(v,np.ndarray):
                if v.dtype.kind not in 'biufc':raise TypeError('Only numerical checkpoint arrays are permitted.')
                name='a'+str(len(arrays));arrays[name]=v
                return {'@array':name}
            if isinstance(v,np.generic):return flatten(v.item())
            if isinstance(v,dict):return {k:flatten(z) for k,z in v.items()}
            if isinstance(v,tuple):return {'@tuple':[flatten(z) for z in v]}
            if isinstance(v,list):return [flatten(z) for z in v]
            if isinstance(v,(str,int,float,bool)) or v is None:return v
            raise TypeError('Unsupported checkpoint type: '+type(v).__name__)
        description=json.dumps(flatten(data),sort_keys=True,allow_nan=False,separators=(',',':')).encode()
        arrays['meta']=np.frombuffer(description,np.uint8)
        final=self.root/(key+'.npz');tmp=final.with_suffix('.tmp')
        with tmp.open('wb') as f:np.savez(f,**arrays)
        self.os.replace(tmp,final)
        self.ledger['kept'][key]=[final.stat().st_size,self.digest(final)]
        self.flush()
    def load(self,key):
        path=self.root/(key+'.npz');size,sha=self.ledger['kept'][key]
        if path.stat().st_size!=size or self.digest(path)!=sha:raise ValueError('Paid receipt corrupt: '+key)
        with np.load(path,allow_pickle=False) as d:
            def recover(v):
                if isinstance(v,list):return [recover(z) for z in v]
                if isinstance(v,dict):
                    if list(v)==['@array']:return d[v['@array']]
                    if list(v)==['@tuple']:return tuple(recover(z) for z in v['@tuple'])
                    return {k:recover(z) for k,z in v.items()}
                return v
            return recover(json.loads(d['meta'].tobytes()))
    def once(self,key,unit,fn):
        if self.has(key):return self.load(key)
        if key in self.ledger['retired']:raise ArithmeticError('Reached an obsolete accepted model instead of its durable successor.')
        reserve={'source':240.,'columns':15.,'qr':65.,'trial':24.,'read':30.,'fd':24.,'prolong':8.,'proposal':4.}.get(unit,2.)
        reserve=max(reserve,1.3*self.ledger['unit_max_seconds'].get(unit,0.))
        self.ledger['pending']=dict(key=key,unit=unit,context=self.ledger['context'])
        self.flush()
        if unit!='metadata' and self.elapsed()+reserve+self.reserve>=self.limit:raise PaidPause(key)
        start=time.perf_counter()
        try:
            data=fn()
        except PaidPause:
            raise
        except Exception as exc:
            self.ledger['pending']=dict(key=key,unit=unit,context=self.ledger['context'],last_error=str(exc))
            self.flush()
            raise
        self.save(key,data)
        duration=time.perf_counter()-start
        self.ledger['unit_max_seconds'][unit]=max(duration,self.ledger['unit_max_seconds'].get(unit,0.))
        self.ledger['pending']=None;self.flush()
        return data
    def retire_accepted_model(self,tag):
        # Only a durable, genuinely accepted successor permits retirement of its predecessor workspace.
        keys=[key for key in self.ledger['kept'] if key.startswith(tag)]
        for key in keys:
            self.ledger['retired'][key]=self.ledger['kept'].pop(key)
        self.flush()
        for key in keys:(self.root/(key+'.npz')).unlink(missing_ok=True)
    def locate(self,**context):
        self.ledger['context']=context
    def checkpoint_state(self,key,**state):
        self.ledger['latest_state']=dict(key=key,**state)
        self.flush()


def main():
    public()
    ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',type=float,required=True)
    args=ap.parse_args();opt=json.loads(Path(args.geometry).read_bytes())
    prior=checked_receipt(opt)
    started=time.perf_counter();elapsed=lambda:time.perf_counter()-started
    counts=Counter();history=[];accepted=0;frozen=None;reference_cache={}
    schedule=list(opt['stages']);first=schedule[0]
    sp=Layout(first['spans'],first['K']);x=None;trust=prior['trust'];mu=None;last=None
    def serialize_reference():
        if frozen is None:return None
        layout,fx,N=frozen
        return dict(space=[layout.spans,layout.K],parameters=fx.tolist(),reference_angles=N)
    def reference(r,binding):
        if binding is None:return None
        ls,v,N=binding
        key=(ls.spans,ls.K,N,v.tobytes(),r.tobytes())
        if key not in reference_cache:
            def fixed():
                k=ClosedSpinor(ls.K,N);za,zb,c=ls.space.actual_jets(r,ls.split(v))
                value=k.state(r,za,zb,c)['E'];counts['immutable_reference_radial_evaluators']+=1
                return value
            uid=book.hashlib.sha256(v.tobytes()+r.tobytes()+str((ls.spans,ls.K,N)).encode()).hexdigest()
            reference_cache[key]=book.once('frozen_E_'+uid,'read',fixed)
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
    book=PaidBook(opt,args.max_seconds,elapsed,counts)
    def unserialize(data):
        if data is None:return None
        return Layout(*data['space']),np.asarray(data['parameters']),data['reference_angles']
    def cached_observation(key,g,k,y,bind,physical=True):
        return book.once(key,'read',lambda:evaluate(g,k,y,bind,physical))
    try:
        book.locate(action='one_R703_transfer',old_repository_run=46151140087)
        x=book.once('converted_actual_seed','source',lambda:transfer(opt,sp,prior,counts,elapsed,book))
        if book.ledger['latest_state'] is None:book.checkpoint_state('converted_actual_seed',space=[sp.spans,sp.K],accepted=0,trust=trust,mu=mu)
        for stage_no,stage in enumerate(schedule):
            stage_key=f's{stage_no:02d}'
            completed=stage_key+'_complete'
            if book.has(completed):
                done=book.load(completed)
                sp=Layout(*done['space']);x=done['x'];frozen=unserialize(done['frozen'])
                trust,mu,accepted=done['trust'],done['mu'],done['accepted']
                history=done['history'];schedule[:]=done['schedule'];last=done['read']
                continue
            geom=Grid(stage['spans'],stage['order'])
            verify=Grid(stage['spans'],opt['check_order'],opt['check_split'])
            cross=Grid(stage['spans'],opt['cross_order'],opt['cross_split'])
            measured=lambda K,want:ClosedSpinor(K,max(want,8*K+5))
            kw=measured(stage['K'],stage['angles']);kf=measured(stage['K'],opt['check_angles']);kc=measured(stage['K'],opt['cross_angles'])
            book.locate(stage=stage_no,action='initial_physical_reads',fixed=frozen is not None)
            if (sp.spans,sp.K)!=(stage['spans'],stage['K']):
                old=sp;oldx=x.copy();sp=Layout(stage['spans'],stage['K'])
                def prolong():
                    promoted=sp.prolong(old,oldx)
                    oldjet=old.space.actual_jets(geom.r,old.split(oldx));newjet=sp.space.actual_jets(geom.r,sp.split(promoted))
                    same=[[float(abs(z-w[:,:z.shape[1]]).max()) for z,w in zip(a,b)] for a,b in zip(oldjet,newjet)]
                    tail=[float(abs(z[:,old.nd:]).max()) if z.shape[1]>old.nd else 0. for z in newjet[0]+newjet[1]]
                    counts['true_nested_shape_prolongations']+=1
                    emit('nested_spinor_space',previous=[old.spans,old.K],new=[sp.spans,sp.K],radial_jet_differences=same,
                         new_tail=tail,coefficients=promoted.tolist(),seconds=elapsed())
                    return promoted
                x=book.once(stage_key+'_prolong','prolong',prolong)
            reference_cache.clear()
            work=cached_observation(stage_key+'_work',geom,kw,x,frozen)
            ind=cached_observation(stage_key+'_independent',verify,kf,x,frozen)
            start_eta=ind['read']['eta'];nacc=0;status='iteration_limit'
            supports=sp.masks(geom.r)
            emit('actual_stage',stage=stage_no,space=[sp.spans,sp.K],columns=sp.size,fixed=serialize_reference(),
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
                mat=np.zeros((len(v),sp.size),order='F');h=2.e-24;ref=work['E'] if frozen is not None else None
                header=bank+'base'
                book.locate(stage=stage_no,iteration=it,action='complete_column_blocks',base=header)
                book.once(header,'metadata',lambda:dict(x=x,space=[sp.spans,sp.K],rows=v,local_mask=active,
                    local_row_count=nlocal,complete_shape=[len(v),sp.size],source_trust=trust,frozen=serialize_reference()))
                book.checkpoint_state(header,stage=stage_no,iteration=it,space=[sp.spans,sp.K],accepted=accepted,trust=trust,mu=mu)
                for j0 in range(0,sp.size,opt['column_block']):
                    j1=min(sp.size,j0+opt['column_block'])
                    def columns():
                        block=np.zeros((len(v),j1-j0))
                        for j in range(j0,j1):
                            ids=supports[j];y=x.astype(complex);y[j]+=1j*h
                            z,c,sh=state(sp,kw,y,geom.r[ids],None if ref is None else ref[ids])
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
                    mat[chunk['kept_rows'],j0:j1]=chunk['values']
                def assembled():
                    counts['complete_new_Fourier_physical_J']+=1
                    return dict(rows=len(v),columns=sp.size,block_size=opt['column_block'])
                book.once(bank+'complete_J','metadata',assembled)
                if it==0:
                    d=np.cos(.917*np.arange(1,sp.size+1));d/=np.linalg.norm(d);pred=mat@d;err=[]
                    for ei,eps in enumerate((2.e-6,4.e-7)):
                        def actual_fd():
                            hi=evaluate(geom,kw,x+eps*d,frozen,False);lo=evaluate(geom,kw,x-eps*d,frozen,False)
                            delta=np.r_[(hi['rows']-lo['rows'])[active],hi['global_rows']-lo['global_rows']]/(2*eps)
                            return float(np.linalg.norm(delta-pred)/max(np.linalg.norm(pred),1.e-15))
                        err.append(book.once(bank+'fd_'+str(ei),'fd',actual_fd))
                    emit('all_column_actual_difference',stage=stage_no,relative=err,columns=sp.size,rows=len(v))
                    if min(err)>2.e-4:raise ArithmeticError('Full local-support derivative differs from actual centered evaluation.')
                ok=False;start_trust=trust
                for variant in range(3):
                    vtag=bank+f'variant{variant}'
                    book.locate(stage=stage_no,iteration=it,variant=variant,action='whole_QR_SVD',base=header)
                    def decomposition():
                        weights=np.ones(len(v))
                        if variant==1:weights[nlocal:]=8.
                        if variant==2:
                            weights[:nlocal]+=8*abs(v[:nlocal])/max(float(abs(v[:nlocal]).max()),1.e-12);weights[nlocal:]=4.
                        Q,R=qr(mat*weights[:,None],mode='economic',check_finite=False,overwrite_a=True)
                        rhs=Q.T@(v*weights);del Q
                        u,s,vt=svd(R,full_matrices=False,check_finite=False)
                        force=-(u.T@rhs);counts['full_QR_SVD']+=1
                        emit('complete_spectrum',stage=stage_no,iteration=it,variant=variant,values=s.tolist())
                        return dict(R=R,weighted_projected_residual=rhs,U=u,s=s,vt=vt,force=force,
                                    raw_row_weights=weights,least=max(1.e-17,float(s[0]**2)*2.e-13))
                    model=book.once(vtag+'_QR_SVD','qr',decomposition);rad=start_trust*(.5**variant)
                    for trial in range(12):
                        ttag=vtag+f'_trial{trial:02d}'
                        book.locate(stage=stage_no,iteration=it,variant=variant,trial=trial,base=header,
                                    factorization=vtag+'_QR_SVD',trust=float(rad),next_proposal=ttag+'_step')
                        def proposal():
                            dx,_,damping=trust_step(model['s'],model['vt'],model['force'],rad,model['least'])
                            image=mat@dx
                            return dict(dx=dx,y=x+dx,mu=float(damping),prediction=float(-2*v@image-image@image),radius=float(rad))
                        step=book.once(ttag+'_step','proposal',proposal)
                        book.locate(stage=stage_no,iteration=it,variant=variant,trial=trial,base=header,
                                    factorization=vtag+'_QR_SVD',paid_next_real_parameters=ttag+'_step')
                        y=step['y'];pred=step['prediction'];damping=step['mu']
                        def trial_work():
                            counts['actual_physical_trials']+=1
                            try:
                                test=evaluate(geom,kw,y,frozen,True)
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
                                    test=evaluate(verify,kf,y,frozen,True)
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
                elif frozen is not None and gate(work['read']) and gate(ind['read']) and ind['norm']<opt['goal']:status='fixed_numerical_goal'
                result=dict(ok=ok,trust=trust,mu=mu,accepted=accepted,nacc=nacc,status=status)
                if ok:result.update(x=x,work=work,ind=ind)
                book.save(finished,result)
                book.checkpoint_state(finished,stage=stage_no,iteration=it,accepted=accepted,space=[sp.spans,sp.K],trust=trust,mu=mu)
                if ok:book.retire_accepted_model(bank)
                if not ok or status=='fixed_numerical_goal':break
            book.locate(stage=stage_no,action='stage_cross',accepted=accepted)
            checked=cached_observation(stage_key+'_cross',cross,kc,x,frozen);last=checked['read']
            history.append(dict(stage=stage_no,space=[sp.spans,sp.K],columns=sp.size,accepted=nacc,status=status,
                                fixed=frozen is not None,start_eta=start_eta,end_cross_eta=last['eta'],norm=checked['norm']))
            emit('stage_end',data=history[-1],physical=last,parameters=x.tolist(),counts=dict(counts),seconds=elapsed())
            if frozen is None and all(gate(a['read']) for a in (work,ind,checked)):
                proposed=(sp,x.copy(),opt['reference_angles'])
                checks=[]
                for j,(g,c) in enumerate(((geom,kw),(verify,kf),(cross,kc))):
                    book.locate(stage=stage_no,action='fixed_reference_three_grid_read',read=j)
                    def fixed_read():
                        try:return dict(ok=True,read=evaluate(g,c,x,proposed,True)['read'])
                        except FloatingPointError as exc:return dict(ok=False,reason=str(exc))
                    checks.append(book.once(stage_key+'_fixed_'+str(j),'read',fixed_read))
                if all(a['ok'] and gate(a['read']) for a in checks):
                    frozen=proposed;del schedule[stage_no+1:]
                    schedule.append(dict(opt['fixed_stage'],K=sp.K+2,spans=sp.spans*2))
                    emit('actual_reference_frozen',reference=serialize_reference(),three_matching_E_reads=checks)
            if stage_no+1<len(schedule):trust=max(trust,opt['retarget_trust'])
            book.save(completed,dict(x=x,space=[sp.spans,sp.K],trust=trust,mu=mu,accepted=accepted,
                       frozen=serialize_reference(),history=history,schedule=schedule,read=last))
            book.checkpoint_state(completed,stage=stage_no,accepted=accepted,space=[sp.spans,sp.K])
        crossed={}
        for label,order,split,nphi in (('radial_only',opt['final_order'],opt['cross_split'],opt['cross_angles']),
            ('angle_only',opt['cross_order'],opt['cross_split'],opt['final_angles']),
            ('both',opt['final_order'],opt['cross_split'],opt['final_angles'])):
            book.locate(action='final_independent_cross',label=label,accepted=accepted)
            gg=Grid(sp.spans,order,split);kk=ClosedSpinor(sp.K,max(8*sp.K+5,nphi))
            def cross_read():
                try:return evaluate(gg,kk,x,frozen,True)['read']
                except FloatingPointError as exc:return dict(continuous_gate_unavailable=str(exc))
            crossed[label]=book.once('final_'+label,'read',cross_read)
        book.ledger['pending']=None;book.checkpoint_state('terminal',accepted=accepted,space=[sp.spans,sp.K])
        emit('terminal',actual_space=[sp.spans,sp.K],all_parameters=x.tolist(),accepted=accepted,stages=history,
             actual_frozen_reference=serialize_reference(),trust=trust,last_mu=mu,full_independent_cross=crossed,
             counts=dict(counts),elapsed_seconds=elapsed(),cumulative_seconds=book.ledger['cumulative_seconds'],
             fingerprint=book.ledger['fingerprint'],continuous_certificate=False,README_completion_claim=False)
    except PaidPause:
        book.flush()
        emit('paid_partial',next_paid_unit=book.ledger['pending'],latest_resume=book.ledger['latest_state'],
             fingerprint=book.ledger['fingerprint'],files_kept=len(book.ledger['kept']),files_superseded=len(book.ledger['retired']),
             actual_space=[sp.spans,sp.K],all_parameters=None if x is None else x.tolist(),accepted=accepted,trust=trust,last_mu=mu,
             actual_frozen_reference=serialize_reference(),counts=dict(counts),elapsed_seconds=elapsed(),
             cumulative_seconds=book.ledger['cumulative_seconds'],continuous_certificate=False,README_completion_claim=False)
    except Exception as exc:
        book.flush()
        emit('incomplete',reason=str(exc),actual_space=[sp.spans,sp.K],parameters=None if x is None else x.tolist(),
             accepted=accepted,trust=trust,last_mu=mu,actual_frozen_reference=serialize_reference(),paid_counts=dict(counts),
             pending=book.ledger['pending'],stages=history,last=last,elapsed_seconds=elapsed(),README_completion_claim=False)
        raise


if __name__=='__main__':main()
