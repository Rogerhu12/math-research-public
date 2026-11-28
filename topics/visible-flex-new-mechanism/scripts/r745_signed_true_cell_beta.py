"""Signed R745 beta enclosures in true dyadic cells. Old Peano leaves and prefixes stay paid."""
from r734_true_dyadic_tail import I,D,B,L0,ONE,ZERO,HALF,HIGH,coefficients,profile,pieces,hull,sym,interval_step,positive_power
from r735_paid_tail_beta_envelope import as_matrix,mv
from r738_negative_tail_and_macro_source import FIRST


def exact_cell(s,n,head,amps,lines,base_deps,paid,book):
    L=L0/(I(2)**n);rho=I(15)/44 if s==-1 else ONE;kinds=pieces(L)
    cur={j:tuple(z*amps[j] for z in lines[j]) for j in (2,3)};start=dict(cur)
    total=ZERO;minimum=max(base_deps.values())+head
    def measure(p,d,i,left,right,kind):
        nonlocal cur,total
        native={}
        for j in (2,3):
            k=f'side{s}_m{j}_n{n}_p{p}_h{d}_i{i}'
            if k in paid:m=paid[k]['data']
            else:
                def true_substep():
                    z=interval_step(j,L,left,right,kind,s)
                    return None if z is None else [v.bounds() for v in z]
                m=book.once('r745_new_'+k,'directed_cell',true_substep)
            native[j]=None if m is None else as_matrix(m)
        if any(m is None for m in native.values()):
            if d>=48:raise ArithmeticError('Cannot bound true signed cap substep.')
            mid=(left+right)/2
            measure(p,d+1,2*i+1,mid,right,kind);measure(p,d+1,2*i,left,mid,kind);return
        q=hull(left,right);dt=right-left
        H=ZERO if kind=='low' else ONE if kind=='high' else HALF if kind=='seam' else profile(q,L/B)
        small=L**2*q**2/256
        w=I(1)/32*(L*q)**5/positive_power(small,H)
        r=B-s*L*q
        ray=[]
        for j in (2,3):
            m=native[j];a,b=coefficients(q,L,H,j,s);z=dt**2*I(a.hi)*I(b.hi)
            if z.hi>=D('.2'):raise ArithmeticError('Stored Peano leaf with incorrect positive bounds.')
            odd=z/(6*(1-z/20))
            partial=(m[0],I((dt*I(a.hi)*odd).hi.copy_negate(),m[1].hi),I(m[2].lo,(dt*I(b.hi)*odd).hi),m[3])
            f,zeta=mv(partial,cur[j]);k=j*j
            F=(r/B)**k*f
            # R735 variable v=w(r f'-k f)=r(s)(B/r)^k W L^4 Z.
            v=r*s*(B/r)**k*(I(1)/32)*L**4*zeta
            ray.append((F,v))
            cur[j]=mv(m,cur[j])
            # At an original accepted prefix restore the original global enclosure directly.
            lev=base_deps[j]
            if d>=lev and i%(2**(d-lev))==0:
                bindex=i//(2**(d-lev))
                key=f'side{s}_m{j}_n{n}_depth{lev}_p{p}_i{bindex}_outward_prefix'
                prefix=mv(as_matrix(paid[key]['data']),start[j])
                fresh=[]
                for first,second in zip(cur[j],prefix):
                    lo=max(first.lo,second.lo);hi=min(first.hi,second.hi)
                    if lo>hi:raise ArithmeticError('Independent true cap propagation disagrees with original prefix.')
                    fresh.append(I(lo,hi))
                cur[j]=tuple(fresh)
        (f,v),(g,u)=ray
        total=total-L*dt*(v*u/w**2-24*f*g)/(2*w*r**3*rho**2)
    for p in reversed(range(7)):
        lo,hi,kind=kinds[p]
        for i in reversed(range(2**minimum)):
            left=lo+(hi-lo)*I(i)/(2**minimum);right=lo+(hi-lo)*I(i+1)/(2**minimum)
            def prefix():
                measure(p,minimum,i,left,right,kind)
                return dict(current={str(j):[a.bounds() for a in v] for j,v in cur.items()},beta=total.bounds())
            saved=book.once(f'r745_beta_prefix_{s}_{n}_{head}_{p}_{minimum}_{i}','directed_cell',prefix)
            cur={j:tuple(I(*a) for a in saved['current'][str(j)]) for j in (2,3)}
            total=I(*saved['beta'])
    return total


def signed_cap(s,ports,old,new,original_opt,book,depth,limit):
    # The original R738 negative and R734 positive arrays describe the same mother cells.
    from collections import ChainMap
    paid=ChainMap(new,old);lo=FIRST[s];rho=I(15)/44 if s==-1 else ONE
    def line(j,n):
        z=ports[s,j]['negative_cells'][str(n)] if n<0 else old[f'side{s}_m{j}_n{n}_accepted_line']['data']
        return tuple(I(*v) for v in z['line']),z['depth']
    amps={j:(B/(B-s*L0/(I(2)**lo)))**(j*j)/line(j,lo)[0][0] for j in (2,3)}
    initial={};total=ZERO;ledger=[]
    for n in range(lo,limit):
        if n==0:initial=dict(amps)
        item=book.once(f'r745_signed_cap_{s}_{n}_{depth}','directed_cell',
            lambda:exact_cell(s,n,depth,amps,{j:line(j,n)[0] for j in (2,3)},
                         {j:line(j,n)[1] for j in (2,3)},paid,book).bounds())
        total=total+I(*item);ledger.append(dict(cell=n,beta=item))
        for j in (2,3):
            v,lev=line(j,n);vp=line(j,n+1)[0]
            M=as_matrix(paid[f'side{s}_m{j}_n{n}_depth{lev}_complete']['data'])
            pivot=0 if v[0].lo==v[0].hi==1 else 1
            amps[j]=16*amps[j]/mv((M[3],-M[1],-M[2],M[0]),vp)[pivot]
    amps0={j:((B-s*L0)/B)**(j*j)*initial[j]*line(j,0)[0][0] for j in (2,3)}
    # Ordinary per-cell absolute F/Z receipts in the donor were normalized to f(old cut)=1.
    # The deep unbounded end is covered from N by the original rigorous cone and a geometric sum.
    cap=original_opt
    N=max(cap[j]['N'] for j in (2,3));rl=B-L0;ru=B+L0
    def remainder(n):
        L=L0/(2**n);q=[]
        for j in (2,3):
            item=cap[j];v=item['cell'][n] if n<item['N'] else item['tail']/32**(n-item['N'])
            q.append(I(amps0[j].norm())*(2+2*j*j+64*ru/L)*v)
        return 208*q[0]*q[1]/((I(1)/32)*rl**3*L**4*rho**2)
    rem=sum((remainder(n) for n in range(limit,N)),ZERO)+remainder(N)*16/15
    return dict(signed_finite_cells=ledger,strict_omitted_absolute=rem.bounds(),
                whole_signed_physical_cut_beta=(total+sym(rem.hi)).bounds(),first_positive_uncomputed_cell=limit)
