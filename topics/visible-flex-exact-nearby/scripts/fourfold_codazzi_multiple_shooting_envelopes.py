"""Whole signed transfer products, weighted block sup norm and independent cell energies.

Each leaf carries one scalar injection, while its diagonal free transfer is
a complete signed matrix.  Only O(log n) native product matrices survive
between insertions. Every binary interval keeps its directed product norm.
"""
import math


def require(value,message):
    if not value:
        raise ValueError(message)


class OrderedProducts:
    def __init__(self,left_to_right):
        self.reverse_multiplication=left_to_right
        self.n=0
        self.stack=[]
        self.norms={}

    def append(self,matrix):
        start,length=self.n,1
        self.n+=1
        while True:
            self.norms[start,length]=matrix.norm()
            if not self.stack or self.stack[-1][1]!=length:
                self.stack.append((start,length,matrix))
                return
            left,old_length,older=self.stack.pop()
            require(left+old_length==start,"all physical cells in the signed nominal product")
            matrix=matrix.times(older) if self.reverse_multiplication else older.times(matrix)
            start,length=left,length*2

    def seal(self):
        require(sum(n for _,n,_ in self.stack)==self.n,"whole chronological native partition")
        self.stack=[]


def dyadic_cover(lo,hi):
    """The complete half-open interval, as aligned binary blocks in ascending order."""
    blocks=[]
    while lo<hi:
        avail=hi-lo
        k=1<<(avail.bit_length()-1)
        if lo:
            k=min(k,lo&-lo)
        blocks.append((lo,k))
        lo+=k
    return blocks


def all_observations(*,injections,endpoint,products,reverse,quadratic):
    """Every suffix (reverse) or prefix (forward), in O(n log n) nonnegative scalar operations.

    quadratic=True carries squared Hilbert-Schmidt inputs from independent radial
    cells. The returned values are squared bounds, without a spurious cell-count fee.
    """
    n=len(injections)
    require((0,1) in products and n>0,"certified whole products")
    m=lambda x:x*x if quadratic else x
    sums={(i,1):v for i,v in enumerate(injections)}
    width=2
    while width<=n:
        h=width//2
        for i in range(0,n-width+1,width):
            left,right=(i,h),(i+h,h)
            first,second=(left,right) if reverse else (right,left)
            sums[i,width]=sums[first]+m(products[first])*sums[second]
        width*=2
    ans=[]
    for node in range(n+1):
        parts=dyadic_cover(node,n) if reverse else list(reversed(dyadic_cover(0,node)))
        total=endpoint
        for key in reversed(parts):
            total=sums[key]+m(products[key])*total
        ans.append(total)
    return ans


def shooting_defect(*,rows,root,outer,R,S,weight_c,weight_d):
    n=len(rows)
    require(len(weight_c)==len(weight_d)==n+1,"one positive weight per entire 97- or 96-block")
    c,d=[],[]
    for i,(cl,dl) in enumerate(rows):
        # Exact order (c_i,d_{i+1},c_{i+1},d_i).
        v=[weight_c[i],weight_d[i+1],weight_c[i+1],weight_d[i]]
        c.append(sum(x*y for x,y in zip(cl,v)))
        d.append(sum(x*y for x,y in zip(dl,v)))
    c_bound=outer[0]*weight_c[-1]+outer[1]*weight_d[-1]
    d_bound=root[0]*weight_c[0]+root[1]*weight_d[0]
    return (all_observations(injections=c,endpoint=c_bound,products=R,reverse=True,quadratic=False),
            all_observations(injections=d,endpoint=d_bound,products=S,reverse=False,quadratic=False))


def positive_weights(e,rows,root,outer,R,S):
    """Any positive dyadic vector is allowed. The only proof is the subsequent original interval readback."""
    def number(x):
        v=float(x.upper())
        require(math.isfinite(v) and v>=0,"finite rough weight proposal from a full interval")
        return v
    n=len(rows)
    one=[1.]*(n+1)
    wc,wd=one[:],one[:]
    try:
        frows=[([number(x) for x in a],[number(x) for x in b]) for a,b in rows]
        fr,fo=[number(x) for x in root],[number(x) for x in outer]
        fR,fS={k:number(v) for k,v in R.items()},{k:number(v) for k,v in S.items()}
        args=dict(rows=frows,root=fr,outer=fo,R=fR,S=fS)
        candidates=[(one[:],one[:])]
        for i in range(70):
            c,d=shooting_defect(**args,weight_c=wc,weight_d=wd)
            wc,wd=([1+x for x in c],[1+x for x in d])
            limit=max(max(wc),max(wd))
            if not math.isfinite(limit) or limit>1e150:
                break
            if i in (2,8,24,69):
                candidates.append((wc[:],wd[:]))
        def cost(pair):
            a,b=pair
            c,d=shooting_defect(**args,weight_c=a,weight_d=b)
            return max(max(x/y for x,y in zip(c,a)),max(x/y for x,y in zip(d,b)))
        wc,wd=min(candidates,key=cost)
    except (ArithmeticError,ValueError):
        wc,wd=one,one
    return [e.exact_float(x) for x in wc],[e.exact_float(x) for x in wd]


def verify(*,e,rows,root,outer,R,S,weights,report):
    wc,wd=weights
    require(all(v.is_finite() and v.lower()>0 for v in wc+wd),"strict positive complete dyadic weight")
    c,d=shooting_defect(rows=rows,root=root,outer=outer,R=R,S=S,weight_c=wc,weight_d=wd)
    theta=max(max((v/w).upper() for v,w in zip(c,wc)),max((v/w).upper() for v,w in zip(d,wd)))
    gap=(e.api.one-theta).lower()
    report("whole_multiple_shooting_perturbation",dict(maximum_weighted_block_row_upper=theta,strict_margin_lower=gap,
        complete_97_rows=len(c),complete_96_rows=len(d),induced_2_angular_blocks=True))
    require(gap>0,"full multiple-shooting block inverse margin")
    return gap
