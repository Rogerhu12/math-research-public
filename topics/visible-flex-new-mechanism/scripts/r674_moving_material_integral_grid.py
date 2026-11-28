"""Material-seam Gauss integration with all original fixed readout positions.

Differentiate the positions, prefix upper limit, panel width and the values
at every moving node. Endpoint interpolation keeps partial integrals C1
when a fixed readout crosses a quadrature-panel edge.
"""
from functools import lru_cache
from types import SimpleNamespace
import time

import numpy as np
import r632_true_hermite_kinetic_chart as shapes

LD, Jet = shapes.LD, shapes.Jet


@lru_cache(None)
def rule(order):
    gauss, weight = np.polynomial.legendre.leggauss(order)
    nodes = np.r_[-1., gauss, 1.]
    inverse = np.linalg.inv(np.polynomial.legendre.legvander(nodes, order+1))
    return (nodes+1)/2, np.r_[0., weight/2, 0.], inverse


def partial_rule(y, order):
    _, whole, inverse = rule(order)
    z = 2*y-1
    leg = np.polynomial.legendre.legvander(z, order+2)
    prim = np.empty((len(y), order+2))
    prim[:, 0] = z+1
    for k in range(1, order+2):
        prim[:, k] = (leg[:, k+1]-leg[:, k-1])/(2*k+1)
    partial = (prim @ inverse)/2
    partial[y==0] = 0
    partial[y==1] = whole
    return partial, leg[:, :order+2] @ inverse


def fixed_readout(panels, order):
    # Reproduce the original float arithmetic and all its exact observation knots.
    local = rule(order)[0][1:-1]
    return np.unique(np.r_[np.concatenate([(j+local)/panels for j in range(panels)]),
                            np.linspace(0., 1., 2*panels+1)])


class MaterialGrid:
    def __init__(self, starts, durations, subdivisions, order, readout, clock):
        self.order, self.clock = order, clock
        self.panels = sum(subdivisions)
        self.control_chain = None
        local, self.whole, _ = rule(order)
        nlocal = len(local)
        length = starts[-1]
        starts_normal = [s/length for s in starts]
        starts_normal[0] = Jet(0,np.zeros_like(length.derivative))
        starts_normal[-1] = Jet(1,np.zeros_like(length.derivative))
        labels, panels, self.layouts = [], [], []
        for j, (duration, count) in enumerate(zip(durations, subdivisions)):
            piece_width = duration/length
            for k in range(count):
                a = starts_normal[j]+piece_width*(LD(k)/count)
                b = piece_width/count
                panel_id = len(panels)
                panels.append((a,b))
                for i, y in enumerate(local):
                    t = (LD(k)+LD(y))/count
                    x = (a+b*LD(y)).value
                    dx = (a+b*LD(y)).derivative
                    if (k==0 and i==0) or (k+1==count and i==nlocal-1):
                        endpoint = starts_normal[j+int(i!=0)]
                        x, dx = endpoint.value, endpoint.derivative
                    labels.append((x, panel_id, i, j, t, dx[-4:], y, -1))
        cuts = np.asarray([p[0].value for p in panels], dtype=LD)
        for i, x in enumerate(readout):
            p = max(0, int(np.searchsorted(cuts, LD(x), side="right"))-1)
            a,b = panels[p]
            y = LD(0) if x==0 else LD(1) if x==1 else (LD(x)-a.value)/b.value
            labels.append((LD(x),p,-1,-1,None,np.zeros_like(a.derivative[-4:]),float(y),i))
        labels.sort(key=lambda s: (s[0],s[7]>=0))
        self.x = np.asarray([row[0] for row in labels],dtype=LD)
        self.tags = [(r[3],r[4],r[5]) for r in labels]
        self.fixed_indices = np.empty(len(readout), int)
        self.readout = SimpleNamespace(x=readout,order=order,panels=self.panels)
        self.nodes = np.empty((self.panels,nlocal),int)
        members=[[] for _ in panels]
        for i, (_,p,which,_,_,_,y,fixed) in enumerate(labels):
            members[p].append((i,y,fixed>=0))
            if which>=0:
                self.nodes[p,which]=i
            if fixed>=0:
                self.fixed_indices[fixed]=i
        for (a,b),rows in zip(panels,members):
            ix=np.asarray([i for i,_,_ in rows])
            y=np.asarray([v for _,v,_ in rows])
            fixed=np.asarray([v for _,_,v in rows])
            W,N=partial_rule(y,order)
            da,db=a.derivative[-4:],b.derivative[-4:]
            byprime=-(da[None,:]+y[:,None]*db[None,:])*fixed[:,None]
            self.layouts.append((ix, W, N, b.value, db, byprime))

    def integrate(self, rows):
        self.clock.check("before_material_aligned_prefix")
        t0=time.monotonic()
        try:
            n,w,d=len(rows),len(rows[0]),len(rows[0][0].derivative)
            values=np.asarray([[v.value for v in row] for row in rows],dtype=LD)
            result=np.empty((n,w),dtype=LD)
            chain=np.empty((n,w,d),float)
            if d:
                derivative=np.asarray([[v.derivative for v in row] for row in rows],float)
            val0=np.zeros(w,dtype=LD)
            jac0=np.zeros((w,d),float)
            for nodes, (ix,W,N,b,db,byprime) in zip(self.nodes,self.layouts):
                self.clock.check("aligned_panel_all_value_and_derivative_columns")
                f=values[nodes]
                partial=W.astype(LD)@f
                average=self.whole.astype(LD)@f
                result[ix]=val0+b*partial
                val0+=b*average
                if d:
                    df=derivative[nodes].reshape(len(nodes),w*d)
                    group=(float(b)*(W@df)).reshape(len(ix),w,d)+jac0
                    correction=np.asarray(partial,float)[:,:,None]*db[None,None,:]
                    correction+=(N@np.asarray(f,float))[:,:,None]*byprime[:,None,:]
                    end_correction=np.asarray(average,float)[:,None]*db[None,:]
                    end_jac=(float(b)*(self.whole@df)).reshape(w,d)
                    if self.control_chain is not None:
                        group+=correction@self.control_chain
                        end_jac+=end_correction@self.control_chain
                    else:
                        group[:,:,-4:]+=correction
                        end_jac[:,-4:]+=end_correction
                    chain[ix]=group
                    jac0+=end_jac
            shapes.COUNTS["complete_prefix_calls"]+=1
            shapes.COUNTS["complete_prefix_value_entries"]+=n*w
            shapes.COUNTS["complete_prefix_derivative_entries"]+=n*w*d
            return [[Jet(result[i,j],chain[i,j]) for j in range(w)] for i in range(n)]
        finally:
            shapes.COUNTS["complete_prefix_seconds"]+=time.monotonic()-t0


class OriginalReadout:
    def __init__(self, full):
        self.full=full

    def __getattr__(self,name):
        return getattr(self.full,name)

    def evaluate(self,curve):
        data=self.full.evaluate(curve)
        grid=curve["grid"]
        idx=grid.fixed_indices
        projected=dict(curve,grid=grid.readout)
        for key in ("geometry","acceleration","history"):
            projected[key]=[curve[key][i] for i in idx]
        # The true near-active height normal is taken at a FIXED normalized x.
        # Its value and all implicit columns use the exact same physical fields.
        data["curve"]=projected
        for key in ("rho","outputs"):
            data[key]=[data[key][i] for i in idx]
        for key in ("base_ruling","design"):
            data[key]=[data[key][2*i+s] for i in idx for s in (0,1)]
        return data
