#!/usr/bin/env python3
"""Genuine scaled g/position six jets, inherited core quadrature, new exact flat annulus and dense sphere source."""
import importlib.util
from pathlib import Path
import sys
import numpy as np
from scipy import sparse


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m


here=Path(__file__).parent;elev=load(here/"2ecf-strong-stadium-real-elevated-cuff.py","scaled_core_true_elevated_input")
dense=load(here/"2ecf-strong-stadium-dense-pair-exchange.py","scaled_dense_geometric_pool")
arb=elev.arb;c=arb.c


class ScaleClock:
    def __init__(self,prior,k):self.prior=prior;self.k=k
    def jets(self,x):return tuple(self.k*q for q in self.prior.jets(x))


    def physical_matrices(self,basis,x):
        _,h,hx=self.jets(x);B,Bx,Bxx=basis.matrices(x)
        return B,sparse.diags(1/h)@Bx,sparse.diags(1/h**2)@Bxx-sparse.diags(hx/h**3)@Bx


class Field:
    def __init__(self,a):
        self.base=elev.RaisedField(a);self.a=a;self.scale_spec=arb.rd(a.core_scale);self.k=float.fromhex(self.scale_spec["lambdaHex"])
        if not (self.scale_spec["originalPhysical"]==[c.sha(p) for p in a.extra_state] and self.scale_spec["elevation"]==c.sha(a.elevation)
                and self.scale_spec["oldMetric"]==self.base.ident):raise ValueError("Correct recut physical source required")
        self.ident=c.sha(a.core_scale);self.dclock=ScaleClock(self.base.dclock,self.k);self.true_cuff_z=self.k*self.base.true_cuff_z
        self.newb=self.k*self.base.newb;self.definition=dict(self.base.definition)
        pc=dict(self.base.definition["pointConfig"]);pc.update(true_cuff_height=self.true_cuff_z,central_a=self.k*pc["central_a"])
        self.definition["pointConfig"]=pc
        self.additional=[]
        for path in a.scaled_spatial:
            d=arb.rd(path);previous=c.sha(self.additional[-1][-1]) if self.additional else None
            if d.get("scaledSource")!=self.ident or d.get("previousScaledState")!=previous:raise ValueError("Same scaled state chain required")
            raw=self.base.raw(d["physicalCorrectionBasis"]["sourceChartBasis"]);basis=c.physical_basis(raw,self.dclock,self.ident)
            if basis.definition!=d["physicalCorrectionBasis"]:raise ValueError("Actual post-scale Cartesian basis")
            self.additional.append((basis,np.array(d["coefficients"]).reshape(basis.nb,basis.na),path))
    def __getattr__(self,key):return getattr(self.base,key)
    def jets(self,x,u):
        Y,rad=self.base.jets(x,u);self.scale_jets(Y,rad)
        for basis,z,_ in self.additional:Y+=self.direct(basis,x,z,u)
        return Y,rad
    def scale_jets(self,Y,rad):
        y=self.k;Y*=np.array([y,1,y,1/y,1,y])[None,:,None,None];rad*=np.array([y,1,1/y])
    def append_flat(self,x,u):
        # x is now the physical material distance after the scaled old r=.32 boundary.
        rr=self.k*.32-np.asarray(x);ee=np.column_stack((np.cos(u),np.sin(u),np.zeros(len(u))))
        tv=np.column_stack((-np.sin(u),np.cos(u),np.zeros(len(u))));Y=np.zeros((len(x),6,len(u),3))
        Y[:,0]=rr[:,None,None]*ee;Y[:,0,:,2]+=self.true_cuff_z;Y[:,1]=-ee;Y[:,2]=rr[:,None,None]*tv
        Y[:,4]=-tv;Y[:,5]=-rr[:,None,None]*ee
        return Y,np.column_stack((rr,-np.ones(len(x)),np.zeros(len(x))))


def rows(f,group):
    x,u,Y,rad,w=elev.elevated_rows(f.base,group);f.scale_jets(Y,rad)
    for basis,z,_ in f.additional:
        for i in range(0,len(x),9):
            sl=slice(i,i+9);Y[sl]+=f.direct(basis,x[sl],z,u)
    W={key:(v*f.k if group!="independent" else v) for key,v in w.items()}
    return x,u,Y,rad,W


class Dense(dense.Dense):
    def __init__(self,f,basis,args,count):
        super().__init__(f,basis,args,count)
        # Parent assembled the original developed shape; replace its tail jets explicitly by the true scaled ones.
        xs=self.x[:self.active:count];outside=xs>f.end;J=self.base[outside].copy()
        J[:,0,:,2]-=self.zc-.51
        J[:,0,:,2]+=f.base.true_cuff_z-.51;J[:,0]*=f.k;J[:,2]*=f.k
        self.base[outside]=J
        # The recut merely splits the same scaled filled flat disk into the genuine extra annulus and the retained r=.32 disk.
        self.disk[:,0,:2]*=f.k
        zero=np.zeros((basis.nb,basis.na));self.origin=self.space(zero)[0][:,0]
    def evaluate(self,z,beta,gradient=True):
        val,grad,rec=super().evaluate(z,beta,gradient);rec["staticCentralDiskRadius"]=.32*self.f.k
        rec["trueCuffRecutRadius"]=.32;return val,grad,rec
