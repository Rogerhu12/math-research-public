#!/usr/bin/env python3
"""R787 material paths on all seven true charts with both regular cap poles identified."""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import dijkstra
import r787_preloaded_two_complete_caps_and_four_returning_meridians as geom

class MaterialGraph:
    def __init__(self,idx,order):
        self.order=order;self.n=(40,64,96)[idx];self.degree=(4,6,8)[idx]
        k=(5,8,12)[idx];n=self.n
        self.P=2*geom.old.old.material(order,True)[-1]
        self.s=np.arange(n)*self.P/n
        r=np.unique(np.r_[np.linspace(0,1,2*k+1),1-geom.wall.RESIDUAL_NORMAL,1-.001])
        v=np.unique(np.r_[np.linspace(0,geom.L,k+1),geom.OLD_L,geom.m.END_E,geom.OLD_L-geom.m.END_E])
        pre=np.unique(np.r_[np.linspace(0,geom.E,k+1),geom.FIRST,geom.EDGE,geom.FIRST-geom.EDGE,
                            geom.FIRST+geom.EDGE,geom.E-geom.EDGE,.10])
        cy=np.linspace(-geom.B,geom.B,2*k+1)
        self.blocks=(("cap-",r),("round-",v[::-1]),("preband-",pre[::-1]),("cylinder",cy),
                     ("preband+",pre),("round+",v),("cap+",r[::-1]))
        self.layers=[("cap-",0.)]
        for ch,vs in self.blocks:self.layers.extend((ch,float(x)) for x in vs[1:])
        self.count=2+(len(self.layers)-2)*n
        def ids(lane):
            if lane==0:return np.zeros(n,dtype=int)
            if lane==len(self.layers)-1:return np.full(n,self.count-1,dtype=int)
            return np.arange(n)+(lane-1)*n+1
        self.ids=ids
        edges={};t,w=geom.m.old.disk.rule(self.degree)
        def segment(ch,s0,v0,s1,v1,i0,i1):
            dx,dv=np.broadcast_arrays(s1-s0,np.asarray(v1-v0))
            dx,dv=np.broadcast_to(dx,(n,)),np.broadcast_to(dv,(n,))
            s=np.broadcast_to(s0,(n,))[:,None]+dx[:,None]*t
            z=np.broadcast_to(v0,(n,))[:,None]+dv[:,None]*t
            g=geom.chart_jet(ch,s,z,0.,order)
            vel=dx[:,None,None]*g[...,1,:]+dv[:,None,None]*g[...,2,:]
            l=np.linalg.norm(vel,axis=2)@w
            for a,b,vv in zip(i0,i1,l):
                if a!=b:
                    key=tuple(sorted((int(a),int(b))))
                    edges[key]=min(float(vv),edges.get(key,np.inf))
        lane=0
        for ch,vs in self.blocks:
            for a,b in zip(vs[:-1],vs[1:]):
                ii,jj=ids(lane),ids(lane+1)
                segment(ch,self.s,a,self.s,b,ii,jj)
                segment(ch,self.s,a,self.s+self.P/n,b,ii,np.roll(jj,-1))
                segment(ch,self.s,a,self.s-self.P/n,b,ii,np.roll(jj,1))
                if lane:
                    segment(ch,self.s,a,self.s+self.P/n,a,ii,np.roll(ii,-1))
                lane+=1
        aa,bb=np.asarray(list(edges)).T
        graph=coo_matrix((list(edges.values()),(aa,bb)),shape=(self.count,self.count)).tocsr()
        self.edges=len(edges)
        targets=[0,self.count-1];angular=np.arange(n)*self.P/n
        extra=geom.m.flat_material_s(np.array([-1.,-.96,-.5,-.10,.30]),order=order)
        extra=np.r_[extra,self.P-extra,0.,self.P/2]
        az=np.unique(np.r_[np.arange(0,n,max(1,n//12)),
                            [int(np.argmin(np.abs(np.mod(angular-x+self.P/2,self.P)-self.P/2))) for x in extra]])
        for j,(ch,vv) in enumerate(self.layers[1:-1],1):
            if j%max(1,len(self.layers)//18)==0 or any(abs(vv-x)<1e-12 for x in
                    (-geom.B,geom.B,0.,geom.E,geom.L,1.)):
                targets.extend(ids(j)[az].tolist())
        self.targets=np.unique(targets);self.dist=dijkstra(graph,directed=False,indices=self.targets)
    def labels(self,i):
        if i==0:return ["cap-",0.,0.]
        if i==self.count-1:return ["cap+",0.,0.]
        j,a=divmod(i-1,self.n);ch,v=self.layers[j+1]
        return [ch,float(self.s[a]),v]
    def audit(self,field):
        points=[]
        for j,(ch,v) in enumerate(self.layers):
            a=self.s[:1] if j in (0,len(self.layers)-1) else self.s
            points.extend(field(ch,a,np.full_like(a,v))[:,0])
        p=np.asarray(points)
        worst=(-np.inf,None,None)
        for i,s in enumerate(self.targets):
            gap=np.linalg.norm(p-p[s],axis=1)-self.dist[i]
            gap[s]=-np.inf;k=int(np.argmax(gap))
            if gap[k]>worst[0]:worst=(float(gap[k]),int(s),k)
        gap,i,k=worst
        return {"graph_vertices":self.count,"edges":self.edges,"sources":len(self.targets),"edge_gauss":self.degree,
                "max_chord_minus_material_graph_distance":gap,"source":self.labels(i),"target":self.labels(k),
                "euclidean_distance":float(np.linalg.norm(p[i]-p[k])),
                "initial_graph_distance":float(self.dist[np.searchsorted(self.targets,i),k])}
