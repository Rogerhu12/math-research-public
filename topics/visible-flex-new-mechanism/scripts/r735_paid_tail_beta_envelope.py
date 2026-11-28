"""Read actual R734 nested enclosures and bound the normalized complete cap integral."""
from r734_true_dyadic_tail import I,D,HIGH,B,L0,ONE,ZERO,integral_power,HALF,MID,matrix_norm


def recovered(source,key):
    return source[key]['data']


def as_matrix(x):return tuple(I(*v) for v in x)


def mv(m,v):return m[0]*v[0]+m[1]*v[1],m[2]*v[0]+m[3]*v[1]


def magnitude(v):return max(a.norm() for a in v)


def cap_mode(j,sign,source,book):
    start=recovered(source,f'm{j}_tail_cone');N=start['cone_index']
    if I(*start['eigenbasis_error']).hi>D(1)/128:raise ValueError('R734 terminal cone does not meet the proved threshold.')
    def line(n):
        vals=start['asymptotic_line'] if n==N else recovered(source,f'side{sign}_m{j}_n{n}_accepted_line')['line']
        return tuple(I(*v) for v in vals)
    v=line(0);r=B-sign*L0
    if v[0].distance_from_zero()==0:raise ArithmeticError('The paid cut has no certified f=1 normalization.')
    amp=(B/r)**(j*j)/v[0];out=[]
    for n in range(N):
        key=f'absolute_cap_side{sign}_j{j}_n{n}'
        def next_cell():
            v=line(n);vp=line(n+1)
            paid=f'side{sign}_m{j}_n{n}'
            depth=recovered(source,paid+'_accepted_line')['depth']
            local=f'{paid}_depth{depth}'
            mat=as_matrix(recovered(source,local+'_complete'))
            # M v_n=(16/pivot) v_{n+1}. Using the inverse avoids outward cancellation of the stable line.
            adj=(mat[3],-mat[1],-mat[2],mat[0]);inward=mv(adj,vp)
            pivot=0 if v[0].lo==v[0].hi==1 else 1
            if v[pivot].lo!=1 or v[pivot].hi!=1:raise ArithmeticError('Missing normalized projective pivot.')
            if inward[pivot].distance_from_zero()==0:raise ArithmeticError('Insufficient paid amplitude enclosure at '+paid)
            after=16*amp/inward[pivot]
            best=magnitude(v)
            def segment(p,d,i,v0):
                raw=recovered(source,f'{paid}_p{p}_h{d}_i{i}')
                if raw is not None:
                    m=as_matrix(raw)
                    # First-order off-diagonal integrals are nonnegative. Their full-step upper
                    # endpoints plus Peano remainders also bound each unfinished substep.
                    k=max(HIGH.add(m[0].hi,m[1].hi),HIGH.subtract(m[3].hi,m[2].lo))
                    return HIGH.multiply(k,magnitude(v0)),mv(m,v0)
                c,half=segment(p,d+1,2*i+1,v0)
                e,end=segment(p,d+1,2*i,half)
                return max(c,e),end
            current=v
            for p in reversed(range(7)):
                for i in reversed(range(2**depth)):
                    mval,_=segment(p,depth,i,current);best=max(best,mval)
                    prefix=as_matrix(recovered(source,f'{local}_p{p}_i{i}_outward_prefix'))
                    current=mv(prefix,v)
            return dict(absolute_FZ=HIGH.multiply(amp.norm(),best).to_eng_string(),following_amplitude=after.bounds(),
                        true_cell=n,accepted_R734_depth=depth)
        q=book.once(key,next_cell)
        amp=I(*q['following_amplitude']);out.append(I(q['absolute_FZ']))
    k=j*j;integral_a=integral_power(HALF,MID,-5)
    integral_b=I(256*k*(k-1))/B**2*integral_power(MID,ONE,3)
    K=(1+integral_a)*(1+integral_b)
    ls=I(*start['lam_stable']);lu=I(*start['lam_unstable'])
    p=(integral_a/(ls-1+integral_a*integral_b),ONE,ONE,(16-ls)/integral_a)
    if not (ls.norm()<D(1)/256 and lu.distance_from_zero()>512):raise ArithmeticError('Sharper stable decay not established.')
    # Actual R734 inequality used K^2 C delta < .1; each partial U has norm <2K.
    asym=2*K*I(matrix_norm(p))*I(amp.norm())
    return dict(N=N,cell=out,tail=asym)


def cap_integral(sign,W,source,book):
    ca=cap_mode(2,sign,source,book);cb=cap_mode(3,sign,source,book)
    N=max(ca['N'],cb['N']);rl=B-L0;ru=B+L0
    def majorant(n):
        L=L0/(2**n)
        def val(j,c):
            full=c['cell'][n] if n<c['N'] else c['tail']/(32**(n-c['N']))
            return (2+2*j*j+64*ru/L)*full
        return 208*val(2,ca)*val(3,cb)/(W*rl**3*L**4)
    total=ZERO
    for n in range(N):total=total+majorant(n)
    # Successive remaining estimates have ratio at most 2^6/32^2.
    total=total+majorant(N)*16/15
    return dict(normalized_base_absolute_beta_upper=I(total.hi).bounds(),actual_cell_count=N,
                outer_convergent_tail_start=N,reuses_original_R734_line_journal=True)
