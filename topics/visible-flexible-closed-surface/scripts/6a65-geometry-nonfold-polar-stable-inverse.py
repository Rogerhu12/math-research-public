#!/usr/bin/env python3
"""Independent safeguarded endpoint polar inverse, preserving full jet chains."""
from __future__ import annotations
import hashlib,importlib.util,sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE/"6a65-geometry-nonfold-height-allocation.py"
EXPECTED_BASE="9918079d1e4356104c0e0c8c6df10714643b052de33f4eca1593fa77f3a42ea6"
if hashlib.sha256(BASE.read_bytes()).hexdigest()!=EXPECTED_BASE:
    raise ValueError("Frozen positive-height field changed")
spec=importlib.util.spec_from_file_location("nonfold_fixed_weighted_formula",BASE)
weighted=importlib.util.module_from_spec(spec);sys.modules[spec.name]=weighted
spec.loader.exec_module(weighted)
geometry_statistics=weighted.geometry_statistics
check=weighted.check

class NonfoldPolarConnector(weighted.NonfoldPolarConnector):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.inverse_receipts=[]
        self.identities.update(weightedPolarSourceSHA256=EXPECTED_BASE,
            sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            endpointInverse=dict(kind="unwrapped periodic lift; bracketed Newton/bisection",
                angleResidualTolerance=5e-14,maxIterations=64,perAngleCompletedValuesFrozen=True,
                originalImplicitSixJetFormulasUnchanged=True))
    def inverse(self,side,theta):
        theta=np.asarray(theta,float).reshape(-1)
        lo=theta-np.pi;hi=theta+np.pi
        def evaluate(values,targets):
            port=self.providers[side](values)
            clock=weighted.base.endpoint_clock(port,values)
            error=clock["phi"][0]-targets
            if np.any(clock["phi"][1]<=0):raise ArithmeticError("Actual polar orientation failed")
            return clock,error
        left,fl=evaluate(lo,theta);right,fr=evaluate(hi,theta)
        if np.any(fl>=0) or np.any(fr<=0):raise ArithmeticError("Actual unwrapped periodic bracket failed")
        del left,right
        u=theta.copy();active=np.ones(len(theta),dtype=bool)
        result={key:np.empty((3,3,len(theta))) for key in ("logrho","rho","z")}
        residual=np.full(len(theta),np.inf)
        worst_iterations=0;smallest_derivative=np.inf
        for iteration in range(64):
            index=np.flatnonzero(active)
            if not len(index):break
            clock,error=evaluate(u[index],theta[index])
            derivative=clock["phi"][1]
            smallest_derivative=min(smallest_derivative,float(np.min(derivative)))
            done=np.abs(error)<5e-14
            if np.any(done):
                profile=weighted.base.polar_profiles(clock)
                finished=index[done]
                for key in result:result[key][:,:,finished]=profile[key][:,:,done]
                residual[finished]=np.abs(error[done]);active[finished]=False
            todo=~done
            if np.any(todo):
                index=index[todo];error=error[todo];derivative=derivative[todo]
                positive=error>0
                hi[index[positive]]=u[index[positive]]
                lo[index[~positive]]=u[index[~positive]]
                candidate=u[index]-error/derivative
                width=hi[index]-lo[index]
                unsafe=(candidate<=lo[index])|(candidate>=hi[index])|(~np.isfinite(candidate))
                candidate[unsafe]=(lo[index[unsafe]]+hi[index[unsafe]])/2
                u[index]=candidate
            worst_iterations=iteration+1
        if np.any(active):
            index=np.flatnonzero(active);clock,error=evaluate(u[index],theta[index])
            raise ArithmeticError("Safeguarded literal inverse unresolved: "+
                repr(dict(side=side,indices=index.tolist(),maximumResidual=float(np.max(abs(error))),
                    maximumBracketWidth=float(np.max(hi[index]-lo[index])))))
        self.inverse_receipts.append(dict(side=side,count=len(theta),iterations=worst_iterations,
            maximumResidual=float(np.max(residual)),minimumSampledDerivative=smallest_derivative,
            branchBracketPaidAtEveryPoint=True,wholeAngleDerivativeLowerCertified=False))
        return result,float(np.max(residual))
