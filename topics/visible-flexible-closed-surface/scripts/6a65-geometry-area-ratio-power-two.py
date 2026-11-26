#!/usr/bin/env python3
"""New fixed-g inverse-square-area row and exact-form J/JT.

This module leaves the original thirteen rows intact. Sigma is the actual
area ratio |Xs cross Xu|/a, not its square eta. The added residual is
sqrt(weight) * max(0, (target/sigma)**2-1); all actual points require sigma>0.
This is a distinct objective, not a continuation identity of the power-one row.
"""
from __future__ import annotations
import copy
import math
import numpy as np
from scipy.sparse.linalg import LinearOperator


class AreaPacket:
    def __init__(self, jets, radius, weights, target):
        jets=np.asarray(jets,float)
        radius=np.asarray(radius,float)
        weights=np.asarray(weights,float)
        if jets.ndim!=4 or jets.shape[1]!=6 or jets.shape[-1]!=3:
            raise ValueError("Area row requires the actual complete physical six-jet packet")
        shape=(jets.shape[0],jets.shape[2])
        radius=np.broadcast_to(radius,shape)
        weights=np.broadcast_to(weights,shape)
        if (not np.all(np.isfinite(jets)) or not np.all(np.isfinite(radius)) or
            np.any(radius<=0) or np.any(weights<0) or not np.all(np.isfinite(weights)) or
            not np.isfinite(target) or not 0<target<=1):
            raise ValueError("Finite complete jets, fixed positive metric radius and explicit target required")
        xs,xu=jets[:,1],jets[:,2]
        cross=np.cross(xs,xu)
        norm=np.sqrt(np.sum(cross*cross,axis=-1))
        if np.any(norm<=0) or not np.all(np.isfinite(norm)):
            raise ArithmeticError("Actual area-barrier trial is outside the positive-area point domain")
        self.sigma=norm/radius
        normal=cross/norm[...,None]
        # At sigma=target the selected generalized hinge derivative is 0.
        # The squared objective is C1 there; every value uses the same hinge.
        active=self.sigma<target
        root=np.sqrt(weights)
        self.residual=root*np.maximum(0,(target/self.sigma)**2-1)
        multiplier=np.where(active,-2*root*target*target/self.sigma**3,0.)/radius
        self.gs=np.cross(xu,normal)*multiplier[...,None]
        self.gu=np.cross(normal,xs)*multiplier[...,None]
        if not all(np.all(np.isfinite(x)) for x in (self.residual,self.gs,self.gu)):
            raise FloatingPointError("Actual reciprocal-area residual/J is not finite")
        self.stats=dict(squaredNorm=float(np.sum(self.residual*self.residual)),
            minAreaRatio=float(np.min(self.sigma)),target=float(target),
            pointCount=int(self.sigma.size),activePoints=int(np.count_nonzero(active)),
            positiveWeightActivePoints=int(np.count_nonzero(active&(weights>0))),
            maxReciprocalViolation=float(np.max(np.maximum(0,(target/self.sigma)**2-1))),
            reciprocalPower=2,
            belowTenthPoints=int(np.count_nonzero(self.sigma<.1)),
            belowQuarterPoints=int(np.count_nonzero(self.sigma<.25)),
            weightBelowTenth=float(np.sum(weights*(self.sigma<.1))),
            weightBelowQuarter=float(np.sum(weights*(self.sigma<.25))),
            costBelowTenth=float(np.sum(self.residual**2*(self.sigma<.1))),
            costBelowQuarter=float(np.sum(self.residual**2*(self.sigma<.25))),
            fullActualPointDomainPositive=True,continuousAreaLowerBoundCertified=False)

    def jvp(self, dxs, dxu):
        dxs,dxu=np.asarray(dxs,float),np.asarray(dxu,float)
        if dxs.shape!=self.gs.shape or dxu.shape!=self.gu.shape:
            raise ValueError("Complete physical Xs/Xu direction required")
        return np.sum(self.gs*dxs+self.gu*dxu,axis=-1)

    def vjp(self,cotangent):
        cotangent=np.asarray(cotangent,float)
        if cotangent.shape!=self.residual.shape:
            raise ValueError("Complete area-row cotangent required")
        return self.gs*cotangent[...,None],self.gu*cotangent[...,None]


def merge(total,part):
    if total is None:
        return copy.deepcopy(part)
    for key in ("squaredNorm","pointCount","activePoints","positiveWeightActivePoints",
                "belowTenthPoints","belowQuarterPoints","weightBelowTenth","weightBelowQuarter",
                "costBelowTenth","costBelowQuarter"):
        total[key]+=part[key]
    if part["minAreaRatio"]<total["minAreaRatio"]:
        total["minAreaRatio"]=part["minAreaRatio"]
        if "minimumPoint" in part:total["minimumPoint"]=copy.deepcopy(part["minimumPoint"])
    total["maxReciprocalViolation"]=max(total["maxReciprocalViolation"],part["maxReciprocalViolation"])
    return total


class AreaGroup:
    def __init__(self,basis,cache,weights,coefficient,target,strength,block=12):
        if not np.isfinite(strength) or strength<=0:
            raise ValueError("A fixed positive area-row strength is required")
        self.basis,self.cache,self.N=basis,cache,len(cache.u)
        self.matrices=basis.matrices(cache.nodes)
        self.slices=[];self.packets=[];self.stats=None
        residual=np.empty((len(cache.nodes),self.N))
        for first in range(0,len(cache.nodes),block):
            sl=slice(first,min(first+block,len(cache.nodes)))
            matrices=tuple(b[sl] for b in self.matrices)
            background,radius=cache(cache.nodes[sl],self.N)
            jets=background+basis.packet(matrices,coefficient,self.N)
            value=AreaPacket(jets,radius,strength*np.asarray(weights)[sl,None]/self.N,target)
            ri,ui=np.unravel_index(int(np.argmin(value.sigma)),value.sigma.shape)
            aa=float(radius[ri,ui]);xs=jets[ri,1,ui];xu=jets[ri,2,ui]
            E=float(xs@xs);F=float(xs@xu)/aa;G=float(xu@xu)/(aa*aa)
            discriminant=math.hypot((E-G)/2,F)
            sigma=float(value.sigma[ri,ui])
            value.stats["minimumPoint"]=dict(s=float(cache.nodes[first+ri]),
                u=float(cache.u[ui]),sigma=sigma,eta=sigma*sigma,E=E,F_over_a=F,G_over_a2=G,
                normalizedGramEigenMinimum=(E+G)/2-discriminant,
                normalizedGramEigenMaximum=(E+G)/2+discriminant,
                meridionalSpeed=math.sqrt(E),angularSpeedRatio=math.sqrt(G),
                meridionalTransverseSpeed=sigma/math.sqrt(G),
                meridionalTangentialSpeed=F/math.sqrt(G),
                tangentCosine=F/math.sqrt(E*G),
                sourceMeridionalSpeed=float(np.linalg.norm(background[ri,1,ui])),
                correctionMeridionalSpeed=float(np.linalg.norm(xs-background[ri,1,ui])),
                x=float(jets[ri,0,ui,0]),y=float(jets[ri,0,ui,1]),z=float(jets[ri,0,ui,2]))
            residual[sl]=value.residual
            self.slices.append(sl);self.packets.append(value)
            self.stats=merge(self.stats,value.stats)
        self.residual=residual.ravel()

    def jvp_coefficients(self,direction):
        out=np.empty((len(self.cache.nodes),self.N))
        for sl,packet in zip(self.slices,self.packets):
            dxs=self.basis.angular(self.matrices[1][sl]@direction,self.N)
            dxu=self.basis.angular(self.matrices[0][sl]@direction,self.N,1)
            out[sl]=packet.jvp(dxs,dxu)
        return out.ravel()

    def vjp_coefficients(self,vector):
        vector=np.asarray(vector,float).reshape(len(self.cache.nodes),self.N)
        out=np.zeros((self.basis.nb,self.basis.na))
        for sl,packet in zip(self.slices,self.packets):
            vs,vu=packet.vjp(vector[sl])
            out+=self.matrices[1][sl].T@self.basis.angular_adjoint(vs)
            out+=self.matrices[0][sl].T@self.basis.angular_adjoint(vu,1)
        return out


def augment(original,area):
    out=copy.deepcopy(original)
    out["schema"]="6a65-complete-original13-plus-reciprocal-area-power-two-row-v1"
    out["originalThirteenRowStatistics"]=copy.deepcopy(original)
    out["areaBarrierStatistics"]=copy.deepcopy(area)
    out["squaredNorm"]+=area["squaredNorm"]
    out["groupSquaredNorm"]["area"]=area["squaredNorm"]
    out["rowCount"]+=area["pointCount"]
    out["allOriginalThirteenRowsRetained"]=True
    return out


class CompleteAreaTwoGrid:
    def __init__(self,joint,stream,basis,caches,weights,coefficient,config,recipe,area):
        self.parent=joint.TwoGrid(stream,basis,caches,weights,coefficient,config,recipe)
        self.preconditioner=self.parent.preconditioner
        self.basis=basis
        self.names=self.parent.names
        self.groups={key:AreaGroup(basis,caches[key],weights[key]["metric"],coefficient,
            area["targetAreaRatio"],area["strength"],recipe["radialBlock"]) for key in self.names}
        self.boundaries=np.cumsum([0,self.parent.shape[0]]+[len(self.groups[k].residual) for k in self.names])
        self.residual=np.concatenate([self.parent.residual]+[self.groups[k].residual for k in self.names])
        self.shape=(len(self.residual),basis.dimension)
        self.operator=LinearOperator(self.shape,matvec=self.matvec,rmatvec=self.rmatvec,dtype=np.float64)
        total=None
        for key in self.names:
            self.groups[key].stats["minimumPoint"]["grid"]=key
            total=merge(total,self.groups[key].stats)
        self.statistics=augment(self.parent.statistics,total)
        self.group_values={key:augment(self.parent.group_values[key],self.groups[key].stats) for key in self.names}

    def unpack(self,x):
        return self.preconditioner.unpack(x)

    def matvec(self,x):
        coefficient=self.unpack(x)
        return np.concatenate([self.parent.matvec(x)]+[self.groups[k].jvp_coefficients(coefficient) for k in self.names])

    def rmatvec(self,x):
        x=np.asarray(x,float)
        if x.shape!=(self.shape[0],):
            raise ValueError("All original and area residual cotangents required")
        base=self.parent.rmatvec(x[:self.parent.shape[0]])
        coefficient=np.zeros((self.basis.nb,self.basis.na))
        for j,key in enumerate(self.names):
            coefficient+=self.groups[key].vjp_coefficients(x[self.boundaries[j+1]:self.boundaries[j+2]])
        return base+self.preconditioner.transpose(coefficient)


def observe(joint,stream,basis,caches,weights,z,config,recipe,area):
    original,original_groups=joint.observe(stream,basis,caches,weights,z,config,recipe)
    total=None;groups={}
    for key in caches:
        value=AreaGroup(basis,caches[key],weights[key]["metric"],z,
            area["targetAreaRatio"],area["strength"],recipe["radialBlock"]).stats
        value["minimumPoint"]["grid"]=key
        total=merge(total,value)
        groups[key]=augment(original_groups[key],value)
    return augment(original,total),groups


def residual(stream,basis,caches,weights,z,config,recipe,area):
    """Full nonlinear residual in the exact same original13/area block order."""
    originals=[];additions=[]
    for key in ("training","observer"):
        cache=caches[key];N=len(cache.u)
        matrices=basis.matrices(cache.nodes)
        r=np.empty((len(cache.nodes),N,13))
        for first in range(0,len(cache.nodes),recipe["radialBlock"]):
            sl=slice(first,min(first+recipe["radialBlock"],len(cache.nodes)))
            packet=stream._point_block(basis,tuple(b[sl] for b in matrices),cache.nodes[sl],
                {name:value[sl] for name,value in weights[key].items()},cache,z,N,config)
            r[sl]=packet.residual
        originals.append(r.ravel())
        additions.append(AreaGroup(basis,cache,weights[key]["metric"],z,
            area["targetAreaRatio"],area["strength"],recipe["radialBlock"]).residual)
    return np.concatenate(originals+additions)
