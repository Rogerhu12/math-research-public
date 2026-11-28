"""Account for the genuine negative and infinite true-cap parts of the R745 signed beta."""
from r734_true_dyadic_tail import I,B,L0,ONE,ZERO,HIGH,sym
from r735_paid_tail_beta_envelope import as_matrix,mv,magnitude
from r738_negative_tail_and_macro_source import FIRST


def tail_bounds(data,journal,terminal,s,ports):
    rho=I(15)/44 if s==-1 else ONE
    cap=next(v['source_tail_bounds'][str(s)] for v in terminal['actual_results'] if v.get('actual',{}).get('accepted'))
    # R735 source_tail_bounds stores the entire normalized R734 absolute beta integral at the old cut.
    old_abs=I(*cap);lo=FIRST[s];baseamp=[];costs=[]
    for j in (2,3):
        k=j*j;po=ports[s,j];lines=po['negative_cells'];amp=None;cell={}
        for n in range(lo,0):
            L=L0/(I(2)**n)
            v=tuple(I(*v) for v in lines[str(n)]['line'])
            if amp is None:amp=(B/(B-s*L))**k/v[0]
            vp=(tuple(I(*v) for v in lines[str(n+1)]['line']) if n<-1 else
                tuple(I(*v) for v in data[f'side{s}_m{j}_n0_accepted_line']['data']['line']))
            key=f'side{s}_m{j}_n{n}';d=lines[str(n)]['depth'];prefix=f'{key}_depth{d}'
            M=as_matrix(journal[prefix+'_complete']['data'])
            piv=0 if v[0].lo==v[0].hi==1 else 1
            if v[piv].lo!=1 or v[piv].hi!=1:raise ArithmeticError('Negative cell lacks true normalized line.')
            a=mv((M[3],-M[1],-M[2],M[0]),vp)[piv]
            def section(p,lev,i,top):
                raw=journal[f'{key}_p{p}_h{lev}_i{i}']['data']
                if raw is not None:
                    m=as_matrix(raw)
                    norm=max(HIGH.add(m[0].hi,m[1].hi),HIGH.subtract(m[3].hi,m[2].lo))
                    return HIGH.multiply(norm,magnitude(top)),mv(m,top)
                U,mid=section(p,lev+1,2*i+1,top);V,end=section(p,lev+1,2*i,mid)
                return max(U,V),end
            q=magnitude(v);cur=v
            for p in reversed(range(7)):
                for ix in reversed(range(2**d)):
                    upper,_=section(p,d,ix,cur);q=max(q,upper)
                    cur=mv(as_matrix(journal[f'{prefix}_p{p}_i{ix}_outward_prefix']['data']),v)
            cell[n]=I(HIGH.multiply(q,amp.norm()))
            amp=16*amp/a
        v=tuple(I(*v) for v in data[f'side{s}_m{j}_n0_accepted_line']['data']['line'])
        baseamp.append(((B-s*L0)/B)**k*amp*v[0]);costs.append(cell)
    oldabs=I((old_abs*baseamp[0]*baseamp[1]/rho**2).norm());negative=ZERO
    for n in range(lo,0):
        L=L0/(I(2)**n);rlo=B-L;rhi=B+L
        v=[(2+2*j*j+64*rhi/L)*costs[i][n] for i,j in enumerate((2,3))]
        negative=negative+208*v[0]*v[1]/((I(1)/32)*rlo**3*L**4*rho**2)
    return dict(old_cut_actual_amplitudes=[q.bounds() for q in baseamp],old_positive_absolute_beta=oldabs.bounds(),
                new_negative_absolute_beta=negative.bounds(),complete_normalized_cap_absolute=(oldabs+negative).bounds())
