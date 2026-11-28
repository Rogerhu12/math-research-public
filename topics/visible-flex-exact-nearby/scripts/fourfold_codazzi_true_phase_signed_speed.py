"""True signed speed on every original piece using 193 old direction bounds.

Only the 65-coordinate finite centre is differentiated in r. The full change
of speed from the repaired centre and selected direction is evaluated as a
value on the whole cell. It is never differentiated in r.
"""
from bisect import bisect_right
from fractions import Fraction
from math import comb, factorial
import gzip
import io
import numpy as np
from flint import arb, acb
from fourfold_codazzi_signed_density_transport_arithmetic import LP, Jet, ball, exact, hull
from fourfold_codazzi_true_phase_original_inputs import ALPHA, CONTROL, CUT, DELTA, check


def symmetric(u):
    return arb(0,abs(u).upper())


def coordinate_polys(v):
    n=(len(v)-1)//2
    U=[acb(0)]*(2*n+1);V=[acb(0)]*(2*n+1)
    V[n]=acb(v[n])
    for k in range(1,n+1):
        U[n+k]=acb(0,-v[k-1]/2);U[n-k]=U[n+k].conjugate()
        V[n+k]=V[n-k]=acb(v[n+k]/2)
    return LP(U,-n),LP(V,-n)


def scalar_model(record):
    p=list(map(Fraction,record["exact_centered_polynomial"]))
    nodes=[ball(x) for x in record["point_jets"]]
    check(len(p)==8 and len(nodes)==7,"entire original degree-seven identity")
    # Native point_jets[k] is the factorial-normalized Taylor coefficient.
    return [exact(v) for v in p],nodes,ball(record["whole_final_derivative"])


def restricted(model,x,order):
    """True normalized r derivative on a closed cell, with all signed terms."""
    p,nodes,whole=model
    v=arb(0)
    for k in range(7,order-1,-1):
        v=v*x+comb(k,order)*p[k]
    # The Taylor expansion of the jth derivative has its own qualified tail.
    for k in range(order,7):
        v+=comb(k,order)*(nodes[k]-p[k])*x**(k-order)
    v+=comb(7,order)*(whole/factorial(7)-p[7])*x**(7-order)
    return v


class Inputs:
    def __init__(self,index,parts,repair,direction,rows,compact):
        nodes=[];cubics=[];cursor=0
        for k,blob in enumerate(parts):
            with np.load(io.BytesIO(gzip.decompress(blob)),allow_pickle=False) as z:
                r=z["radial_nodes"];a=z["piece_coefficients"]
            if k: check(nodes[-1]==Fraction(float(r[0])),"adjacent original dyadic nodes agree")
            spec=index["parts"][k]
            check(a.dtype==r.dtype==np.dtype("float64") and
                  a.shape==(4,spec["last_interval_exclusive"]-cursor,65)
                  and len(r)==a.shape[1]+1 and spec["first_interval"]==cursor
                  and np.isfinite(a).all() and np.isfinite(r).all() and (np.diff(r)>0).all(),
                  "whole original physical cubics")
            nodes.extend(Fraction(float(t)) for t in r[int(bool(k)):]);cubics.append(a)
            cursor=spec["last_interval_exclusive"]
        self.cubics=np.concatenate(cubics,axis=1);self.nodes=nodes
        check(self.cubics.shape==(4,2692,65) and nodes[0]==0 and nodes[2549]<CUT<nodes[2550],
              "two original piecesets cover the entire actual strict ray")
        dr=list(map(lambda z:symmetric(exact(Fraction(z))),repair["exact_cumulative_coefficient_suprema"]))
        dz=[symmetric(exact(DELTA)*abs(ball(z)).upper())
            for z in direction["complete_negative_interval_direction_coefficient_suprema"]]
        ru,rv=coordinate_polys(dr);zu,zv=coordinate_polys(dz)
        self.du=ru+zu;self.dv=rv+zv
        self.rows=[];self.bounds=[]
        for (left,right),digest,row in rows:
            centre=Fraction(row["center"])
            data={k:scalar_model(row["models"][k]) for k in ("q","gamma","beta","s")}
            if (left,right) in compact:
                t=compact[left,right]
                check(Fraction(t["center"])==centre,"same compact Taylor origin")
                data["T"]=scalar_model(t["models"]["T"])
            self.rows.append((centre,data));self.bounds.append((left,right))
        self.rights=[b for a,b in self.bounds]
        self.cached_piece=None
        cutset={Fraction(0),CUT,*CONTROL}
        cutset.update(r for r in nodes if 0<r<CUT)
        cutset.update(r for pair in self.bounds for r in pair if 0<r<CUT)
        cuts=sorted(cutset);self.plan=[]
        for l,r in reversed(list(zip(cuts,cuts[1:]))):
            k=bisect_right(nodes,l)-1;i=bisect_right(self.rights,l)
            check(self.bounds[i][0]<=l<r<=self.bounds[i][1] and nodes[k]<=l<r<=nodes[k+1],
                  "all original real seams retained")
            self.plan.append((l,r,k,i))
        check(self.plan[0][1]==CUT and self.plan[-1][0]==0 and len(self.plan)<=4000,"whole strict cover")

    def piece(self,k):
        if k!=self.cached_piece:
            self.poly=[coordinate_polys([exact(ALPHA)*arb(float(z)) for z in self.cubics[j,k]])
                       for j in (3,2,1,0)]
            self.cached_piece=k
        return self.poly

    def nominal(self,cell,p,whole):
        l,r,k,i=cell;h=exact(r-l)
        centre,models=self.rows[i]
        xr=hull(l-centre,r-centre) if whole else exact(r-centre)
        xc=hull(l-self.nodes[k],r-self.nodes[k]) if whole else exact(r-self.nodes[k])
        pol=self.piece(k)
        def scalar(n):
            return Jet([(-h)**j*restricted(models[n],xr,j) for j in range(p+1)])
        beta,gamma,q,s=[scalar(n) for n in ("beta","gamma","q","s")]
        def cubic(side):
            terms=[]
            for j in range(p+1):
                v=LP()
                for a in range(3,j-1,-1):
                    v=v*xc+pol[a][side]*comb(a,j)
                terms.append(v*((-h)**j))
            return Jet(terms)
        u=cubic(0);v=cubic(1)+s
        d=-(beta*(u*u-q*q*v*v).primitive())
        b=-(gamma*q*v.mean())
        return d,b,(u.c[0],v.c[0],beta.c[0].scalar(),gamma.c[0].scalar(),q.c[0].scalar())

    def delta_speed(self,cell,raw):
        l,r,_,i=cell;u,v,beta,gamma,q=raw
        check(q.lower()>0,"true negative nominal q on the entire physical cell")
        if r<=CONTROL[0] or l>=CONTROL[1]:
            dk2=arb(0);wt=arb(0);wq=q
        else:
            a,b=CONTROL;check(a<=l<r<=b,"compact metric control stays on one cell")
            centre,models=self.rows[i]
            T=restricted(models["T"],hull(l-centre,r-centre),0)
            t=hull((l-a)/(b-a),(r-a)/(b-a))
            w=4096*(t*(1-t))**6
            wp=exact(Fraction(24576)/(b-a))*(t*(1-t))**5*(1-2*t)
            z=arb(0,exact(DELTA));wt=-z*T*wp
            rad=q*q+wt;check(rad.lower()>0,"whole real selected square-root gap")
            wq=rad.sqrt()
            y=-z*w
            # exp(y)-1=y int_0^1 exp(sy) ds, directed about zero even for tiny y.
            dk2=q*q*y*(arb(0).union(y)).exp()+wt*y.exp()
        du,dv=self.du,self.dv
        dv2=2*v*dv+dv*dv
        diff=2*u*du+du*du-dv2*(q*q)-(v*v+dv2)*dk2
        dd=diff.primitive()*(-beta)
        db=-gamma*(dv.mean()*wq+v.mean()*wt/(wq+q))
        return dd,db

    def speeds(self,cell,p=4):
        """Four signed Taylor coefficients at entry plus the true whole fourth.

        The last coefficient is a variable remainder, valid for each mode.
        The additional per-mode change has no radial derivative assigned.
        All returned speeds are for dimensionless inward time, including h.
        """
        l,r,_,_=cell;h=exact(r-l)
        d0,b0,_=self.nominal(cell,p-1,False)
        dw,bw,raw=self.nominal(cell,p,True)
        dd,db=self.delta_speed(cell,raw)
        return ([v*h for v in (*d0.c,dw.c[p])],
                [v*h for v in (*b0.c,bw.c[p])],dd*h,db*h,(dw.c[0]+dd)*h)
