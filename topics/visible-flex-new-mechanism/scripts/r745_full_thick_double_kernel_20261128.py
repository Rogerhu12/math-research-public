"""Public R745 genuine two-parameter shoot, box proof and signed full-cap response."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import time
import numpy as np
from scipy.special import expit
from r726_closed_spinor_fourier import public
from r728_closed_spinor_continuation_20261128 import PaidPause
from r734_true_dyadic_tail import I,D,sym
from r735_paid_tail_beta_envelope import cap_mode
from r745_three_broad_valleys import H,coordinate
from r745_shooting_and_actual_response import tag,matching,beta_and_cost
from r745_true_valley_enclosure import paired
from r745_true_cap_beta_envelope import tail_bounds
from r745_signed_true_cell_beta import signed_cap
from r745_completed_source_and_paid_units import Journal,actual_sources,higher_modes


def emit(name,**values):print('R745_'+name+' '+json.dumps(values,sort_keys=True,separators=(',',':'),allow_nan=False),flush=True)


def numerical(book,ports,eta,tol,counts,ray=1):
    def evaluate():
        r,J,ratio,state,_=matching(book,ports,eta,ray,tol,counts)
        counts['new_two_valley_terminal_with_complete_2_by_2']+=1
        return dict(residual=r,full_J_logit=J,right_cut_multiplier=ratio,
                    singular_values=np.linalg.svd(J,compute_uv=False),matching_Cauchy={str(k):v for k,v in state.items()})
    return book.once(f'num_{tag(eta)}_{ray}_{float(tol).hex()}'.replace('.','p').replace('+','u'),'read',evaluate)


def check_J(book,ports,eta,tol,count):
    current=numerical(book,ports,eta,tol,count);errors=[]
    for h in (3.e-5,7.e-6):
        columns=[]
        for j in range(2):
            e=np.eye(2)[j]*h
            hi=numerical(book,ports,eta+e,tol,count)['residual'];lo=numerical(book,ports,eta-e,tol,count)['residual']
            columns.append((hi-lo)/(2*h))
        delta=np.asarray(columns).T-current['full_J_logit']
        errors.append(float(np.linalg.norm(delta)/max(1.e-8,np.linalg.norm(current['full_J_logit']))))
    if min(errors)>.002:raise ArithmeticError('Actual two-valley finite differences disagree with all variational columns.')
    return errors


def search(book,ports,opt,count):
    best=None;roots=[]
    for seed,raw in enumerate(opt['starting_physical_valleys']):
        eta=np.array([coordinate(v) for v in raw]);mu=opt['initial_logit_trust']
        for it in range(opt['iterations_per_actual_seed']):
            bank=f'seed{seed}_i{it}'
            if book.has(bank):
                z=book.load(bank)
                best=z['best']
                if z['kind']=='root':roots.append(z['current']);break
                if z['kind']=='exhausted':break
                eta,mu=z['next'],z['trust'];continue
            book.locate(action='whole_true_valley_shoot',seed=seed,iteration=it,parameters=eta.tolist())
            q=numerical(book,ports,eta,opt['work_tolerance'],count)
            r=q['residual'];J=q['full_J_logit'];norm=np.linalg.norm(r)
            if it==0:book.once(f'seed{seed}_two_column_finite_difference','read',lambda:check_J(book,ports,eta,opt['work_tolerance'],count))
            cur=dict(eta=eta.copy(),valley=H*expit(eta),residual=r,full_J_logit=J,singular=q['singular_values'],norm=float(norm))
            if best is None or norm<best['norm']:best=cur
            book.checkpoint_state(bank,action='model_and_pending_actual_steps',seed=seed,iteration=it,eta=eta.tolist(),trust=mu)
            if norm<=opt['root_residual']:
                roots.append(cur);book.save(bank,dict(kind='root',current=cur,best=best));break
            U,S,Vh=np.linalg.svd(J,full_matrices=False)
            accepted=False
            for trial in range(opt['trials_per_model']):
                radius=mu*.55**trial
                # Scale all singular directions together through damped least squares, including zero singular values.
                if S[-1]>0:
                    step=-(Vh.T@((U.T@r)/S))
                else:step=np.full(2,np.inf)
                if np.linalg.norm(step)>radius:
                    low=0.;hi=max(S[0]**2,1.e-15);force=S*(U.T@r)
                    while np.linalg.norm(force/(S*S+hi))>radius:hi*=4
                    for _ in range(54):
                        mid=(low+hi)/2
                        if np.linalg.norm(force/(S*S+mid))>radius:low=mid
                        else:hi=mid
                    step=-(Vh.T@(force/(S*S+hi)))
                candidate=eta+step
                if max(abs(candidate))>opt['maximum_logit']:
                    book.once(bank+'_out_'+str(trial),'metadata',lambda:dict(candidate=candidate,status='declared_physical_valley_domain'));continue
                book.locate(action='actual_valley_trial',seed=seed,iteration=it,trial=trial,parameters=candidate.tolist())
                nxt=numerical(book,ports,candidate,opt['work_tolerance'],count)
                pred=norm**2-np.linalg.norm(r+J@step)**2;real=norm**2-np.linalg.norm(nxt['residual'])**2
                if pred>0 and real>0:
                    ratio=real/pred;mu=min(opt['max_logit_trust'],radius*(1.5 if ratio>.75 else .75 if ratio<.2 else 1.))
                    eta=candidate;accepted=True;count['accepted_two_valley_steps']+=1
                    nc=dict(eta=eta.copy(),valley=H*expit(eta),residual=nxt['residual'],full_J_logit=nxt['full_J_logit'],
                            singular=nxt['singular_values'],norm=float(np.linalg.norm(nxt['residual'])))
                    if nc['norm']<best['norm']:best=nc
                    emit('ACCEPT',seed=seed,iteration=it,valleys=(H*expit(eta)).tolist(),residual=nxt['residual'].tolist(),
                         whole_singular_values=S.tolist(),trust=mu,real_over_model=ratio);break
            if accepted and nc['norm']<=opt['root_residual']:
                roots.append(nc);book.save(bank,dict(kind='root',current=nc,best=best));break
            book.save(bank,dict(kind='accepted' if accepted else 'exhausted',next=eta,trust=mu,current=cur,best=best))
            if not accepted:break
        if roots:break
    return best,roots


def certified_box(book,ports,cur,opt):
    v=cur['valley'];J=cur['full_J_logit']/(v*(1-v/H))[None,:]
    try:pre=np.linalg.inv(J)
    except np.linalg.LinAlgError:return None
    P=[[I(D.from_float(float(t))) for t in row] for row in pre]
    if (P[0][0]*P[1][1]-P[0][1]*P[1][0]).distance_from_zero()==0:return None
    for depth in opt['validated_piece_depths']:
        for width in opt['valley_box_absolute_radii']:
            rad=np.minimum(np.minimum(v,H-v)*.4,width)
            lo=[I(D.from_float(float(x))) for x in v-rad];hi=[I(D.from_float(float(x))) for x in v+rad]
            if any(a.lo<=0 or b.hi>=D('.56') for a,b in zip(lo,hi)):continue
            allfaces=[]
            for i in range(2):
                for sg in (-1,1):
                    prev={};n=1
                    while n<=opt['maximum_face_parts']:
                        success=True;curr={}
                        for k in range(n):
                            if k//2 in prev and prev[k//2] is not None and n>1:
                                curr[k]=prev[k//2];continue
                            box=[None,None];box[i]=lo[i] if sg==-1 else hi[i];j=1-i
                            low=lo[j]+(hi[j]-lo[j])*k/n;high=lo[j]+(hi[j]-lo[j])*(k+1)/n
                            box[j]=I(low.lo,high.hi)
                            book.locate(action='true_Poincare_Miranda_face',axis=i,sign=sg,subdivision=n,index=k,depth=depth)
                            ans=paired(book,ports,box,depth,False)
                            if ans is None:curr[k]=None;success=False;continue
                            z=sg*sum((a*b for a,b in zip(P[i],ans['residual'])),I(0))
                            curr[k]=z.bounds() if z.lo>0 else None
                            if z.lo<=0:success=False
                        if success:break
                        prev=curr;n*=2
                    allfaces.append(dict(axis=i,sign=sg,passed=success,pieces=n if success else n//2,
                                   oriented_images=[q for q in curr.values() if q is not None]))
                    if not success:break
                if not success:break
            if len(allfaces)==4 and all(a['passed'] for a in allfaces):
                return dict(valleys=[[a.bounds()[0],b.bounds()[1]] for a,b in zip(lo,hi)],faces=allfaces,
                         exact_fixed_preconditioner=[[a.bounds() for a in row] for row in P],depth=depth,
                         representative='lexicographically least common true shooting zero in this compact box')
    return None


def main():
    public();ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',required=True,type=float)
    args=ap.parse_args();opt=json.loads(Path(args.geometry).read_bytes());req=json.loads(Path(os.environ['R745_REQUEST']).read_bytes())
    started=time.monotonic();elapsed=lambda:time.monotonic()-started;count=Counter()
    book=Journal(opt,args.max_seconds,elapsed,count,req);history=None;answer={};kind='terminal'
    try:
        orig,thin,old,new,ports,native,history=actual_sources(book,req,opt,count)
        capbound={s:book.once(f'actual_normalized_full_cap_{s}','directed_cell',lambda:tail_bounds(old,new,thin,s,ports)) for s in (-1,1)}
        answer['whole_cap_absolute_without_signed_refinement']={str(s):capbound[s] for s in (-1,1)}
        best,roots=search(book,ports,opt,count)
        def shown(cur):return {k:(v.tolist() if isinstance(v,np.ndarray) else v) for k,v in cur.items()}
        if best is not None:answer['best_actual']=shown(best)
        if roots:
            cur=roots[0];eta=cur['eta']
            answer['root_full_J_check']=book.once('candidate_two_column_finite_difference','read',lambda:check_J(book,ports,eta,opt['independent_tolerance'],count))
            independent={}
            for j in (0,1,2):
                a=numerical(book,ports,eta,opt['independent_tolerance'],count,j)
                independent[str(j)]=dict(residual=a['residual'].tolist(),full_J=a['full_J_logit'].tolist(),
                        multiplier=a['right_cut_multiplier'],singular_values=a['singular_values'].tolist())
            answer['independent_cut_rays']=independent
            answer['full_finite_parts_and_costs']=[book.once('finite_beta_'+str(deg),'read',lambda:
                beta_and_cost(book,ports,native,eta,opt['independent_tolerance'],count,deg)) for deg in opt['beta_quadrature_orders']]
            cert=certified_box(book,ports,cur,opt);answer['true_two_valley_box']=cert
            if cert:
                emit('TRUE_DUAL_BOX',**cert)
                vals=tuple(I(*v) for v in cert['valleys']);d=cert['depth']
                if higher_modes(book,orig,ports,opt['extra_negative_depth']):
                    high=paired(book,ports,vals,d,False,(4,5,6))
                    answer['true_other_second_modes']=None if high is None else [a.bounds() for a in high['residual']]
                bulk=paired(book,ports,vals,d,True)
                if bulk is not None:
                    rr=bulk['ratio'][0]*bulk['ratio'][1];s0,s1=[I(*capbound[s]['complete_normalized_cap_absolute']) for s in (-1,1)]
                    b=bulk['bulk_beta']+sym(s0.hi)+rr*sym(s1.hi)
                    beta=dict(true_bulk=bulk['bulk_beta'].bounds(),actual_right_ratios=[v.bounds() for v in bulk['ratio']],
                            whole_signed_with_absolute_caps=b.bounds(),strict_signed_cap_refinements=[])
                    answer['complete_beta']=beta
                    if b.distance_from_zero()==0:
                        caps={s:{j:cap_mode(j,s,book.records,book) for j in (2,3)} for s in (-1,1)}
                        for lev,N in opt['signed_cap_schedule']:
                            x,y=[signed_cap(s,ports,old,new,caps[s],book,lev,N) for s in (-1,1)]
                            z=bulk['bulk_beta']+I(*x['whole_signed_physical_cut_beta'])+rr*I(*y['whole_signed_physical_cut_beta'])
                            beta['strict_signed_cap_refinements'].append(dict(level=lev,head=N,inner=x,outer=y,whole=z.bounds()))
                            if z.distance_from_zero()>0:break
    except PaidPause:kind='paid_partial'
    except Exception as exc:
        kind='incomplete';answer['reason']=type(exc).__name__+': '+str(exc);raise
    finally:
        book.flush();book.out.close()
        emit('FINAL',kind=kind,actual=answer,source_history=history,counts=dict(count),pending=book.ledger['pending'],
             fingerprint=book.ledger['fingerprint'],last_resume=book.ledger['latest_state'],current_elapsed=elapsed(),
             cumulative_seconds=book.ledger['cumulative_seconds'],finite_amplitude_root=False,README_completion_claim=False)


if __name__=='__main__':main()
