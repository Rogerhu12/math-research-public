#!/usr/bin/env python3
"""Pure source interface for the R613 actual-position height objective.

No optimizer, request, retained state, new run or numerical probe is supplied
here. A later declared scientific scope must bind its actual incoming state,
complete acceptance/readout contract and costs before using this operator.
The original compact1130q field remains unchanged; only the output map is
replaced by real position-defect Fourier coordinates.
"""
from collections import defaultdict
import hashlib
import importlib.util
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
COMPACT_FILE="r606_compact_response_height_20261127.py"
COMPACT_SHA="1e54d50f73dc88f2be2c755e1242fedcb1bacb12fe08da65180cd476d5720dac"
POSITION_FILE="r613_position_defect_linearization_20261127.py"
POSITION_SHA="4327ab847dd2a38a0b4098bd0712d7e2980bcc7c750dc2413b7881f9ed190a31"
POSITION_ODD_MODES=np.arange(1,64,2,dtype=int)
NEW=defaultdict(int)


def bound_import(name,filename,digest):
    path=HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        raise RuntimeError("source-bound position operator changed: "+filename)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


compact=bound_import("r613_original_compact_height",COMPACT_FILE,COMPACT_SHA)
position=bound_import("r613_same_position_linearization",POSITION_FILE,POSITION_SHA)
MODES,CORE_MODES=compact.MODES,compact.CORE_MODES
OLD_NQ=compact.OLD_NQ
check=compact.check


class ActualPositionHeight(compact.CompactResponseHeight):
    def prepare(self,r,ntheta):
        data=super().prepare(r,ntheta)
        if "position_projection" not in data:
            data["position_projection"]=position.projection(data["theta"],POSITION_ODD_MODES)
            data["position_radial_units"]=data["weak_row_units"][:,0].copy()
        return data

    def evaluate(self,q,amplitude,data):
        state=super().evaluate(q,amplitude,data)
        state["original_At_M_positive_residual"]=state["residual"]
        cache=position.prepare(state,data)
        state["position_cache"]=cache
        state["residual"]=position.residual(cache,data["position_projection"],
            data["position_radial_units"],amplitude)
        NEW["same_field_actual_position_evaluations"]+=1
        return state

    def jacobian(self,q,amplitude,data,state):
        check(self.deadline)
        NEW["analytic_jacobians"]+=1
        nr,nt=len(data["r"]),len(data["theta"])
        J=np.empty((nr*2*len(POSITION_ODD_MODES),self.nq))
        r=data["r"][:,None,None]
        g=state["g"]
        p,b,N,u,E,e=[g[k][:,:,None] for k in ("p","b","N","u","E","e")]
        w,wr,fr,frr,ft,ftt,B,M,At=[state[k][:,:,None] for k in
            ("w","wr","fr","frr","ft","ftt","B","M","At")]
        denominator=np.mean(N/u**3,axis=1,keepdims=True)
        position_cache=state["position_cache"]
        for first in range(0,self.nq,16):
            check(self.deadline)
            indices=np.arange(first,min(self.nq,first+16));nc=len(indices)
            jets=[np.zeros((nr,nt,nc)) for _ in range(6)]
            dw,dwr=np.zeros((nr,1,nc)),np.zeros((nr,1,nc))
            dpc,dpr_bulk=np.zeros((self.nm,nc)),np.zeros((self.nm,nc))
            for local,index in enumerate(indices):
                if index==0:
                    dw[:,0,local],dwr[:,0,local]=data["gain_w"],data["gain_wr"]
                    continue
                col=index-1
                fields=amplitude*data["new_columns"][:,col,:]
                c,s,j=data["column_cos"][col],data["column_sin"][col],self.column_modes[col]
                values=(fields[:,0,None]*c,fields[:,1,None]*c,fields[:,2,None]*c,
                    -j*fields[:,0,None]*s,-j*j*fields[:,0,None]*c,-j*fields[:,1,None]*s)
                for target,value in zip(jets,values):
                    target[:,:,local]=value
                if index<self.nm:
                    dpc[index,local]=-(MODES[index]**2-1)/self.par.R*amplitude
                elif index<OLD_NQ:
                    mode,bsindex=divmod(index-self.nm,self.nb)
                    dpr_bulk[mode,local]=amplitude*self.core_k*(self.par.alpha+2)/self.bulk_scale*self.core_B[bsindex]
            dcc=self.correction_derivative(q,amplitude,dpc,dpr_bulk)
            dC=data["core_all_cos"].T@dcc
            dCt=-data["core_all_sin"].T@(CORE_MODES[:,None]*dcc)
            dCtt=-data["core_all_cos"].T@(CORE_MODES[:,None]**2*dcc)
            v,vr,vrr=data["core_radial"].T
            extras=(v[:,None,None]*dC,vr[:,None,None]*dC,vrr[:,None,None]*dC,
                v[:,None,None]*dCt,v[:,None,None]*dCtt,vr[:,None,None]*dCt)
            for target,value in zip(jets,extras):
                target+=value
            _,dfr,dfrr,dft,dftt,dfrt=jets
            dp=-dw+dfr
            dN=(r*ft*dft/b**3+r*r*(ftt*dp+p*dftt)/b**3
                +3*r*r*p*ftt*ft*dft/b**5)
            dshift=(-2*dw*fr-2*w*dfr+2*fr*dfr
                +2*p*dp*ft*ft/b**2+2*p*p*ft*dft/b**2+2*p*p*ft**3*dft/b**4)
            de=(2*np.mean(dN/u,axis=1,keepdims=True)
                +np.mean(N*dshift/u**3,axis=1,keepdims=True))/denominator
            dE=2*w*dw+de
            dM=ftt*dp+p*dftt-2*ft*dft/r
            dB=dfrt-dft/r
            dAt=(-r*(dw*frr+w*dfrr)-r*(dwr*fr+wr*dfr)
                -de*wr*ftt-e*dwr*ftt-e*wr*dftt
                +dE*frr*ftt+E*dfrr*ftt+E*frr*dftt
                -(dw*wr+w*dwr)*fr*ftt-w*wr*dfr*ftt-w*wr*fr*dftt
                -dE*B*B-2*E*B*dB+r*(dfr*frr+fr*dfrr)
                +(dw*wr+w*dwr)*ft*ft/r+2*w*wr*ft*dft/r)
            dG=dAt/M-At*dM/M**2
            du=(de-dshift)/(2*u)
            db=-ft*dft/b
            dS=position.derivative(position_cache,dN,du,dE,db,dG)
            J[:,indices]=position.projected_derivative(dS,data["position_projection"],
                data["position_radial_units"],amplitude)
            NEW["analytic_columns"]+=nc
        if not np.all(np.isfinite(J)):
            raise ArithmeticError("nonfinite complete actual-position Jacobian")
        return J
