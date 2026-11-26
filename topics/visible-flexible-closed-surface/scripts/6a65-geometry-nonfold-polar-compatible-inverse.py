#!/usr/bin/env python3
"""Preserve the old successful polar inverse path; safeguard stalled angles.

The former 2e-13 inner R137 stopping tolerance can make the outer old
5e-14 Newton threshold cycle. Eight old iterations are tried unchanged;
a bracketed, per-angle inverse resolves the remaining branch without
loosening the outer residual tolerance or altering any implicit jet.
"""
from __future__ import annotations
import hashlib,importlib.util,sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
PARENT=HERE/"6a65-geometry-nonfold-polar-stable-inverse.py"
EXPECTED_PARENT="3ef814b4079fd7a0dd7474d2a10f4e3aebddd81751fb11d00253ad19b5de0e88"
if hashlib.sha256(PARENT.read_bytes()).hexdigest()!=EXPECTED_PARENT:
    raise ValueError("Frozen safeguarded polar inverse changed")
spec=importlib.util.spec_from_file_location("nonfold_periodic_bracket_parent",PARENT)
parent=importlib.util.module_from_spec(spec);sys.modules[spec.name]=parent;spec.loader.exec_module(parent)
geometry_statistics=parent.geometry_statistics
check=parent.check

class NonfoldPolarConnector(parent.NonfoldPolarConnector):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.identities.update(stableInverseSourceSHA256=EXPECTED_PARENT,
            sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            endpointInverse=dict(kind="eight original Newton steps; periodic bracketed fallback",
                angleResidualTolerance=5e-14,oldSuccessfulFastPathUnchanged=True,
                fallbackMaxIterations=64,originalImplicitSixJetFormulasUnchanged=True))
        self.fast_inverse_calls=0;self.safeguarded_inverse_calls=0
    def inverse(self,side,theta):
        theta=np.asarray(theta,float).reshape(-1);u=theta.copy()
        for iteration in range(8):
            clock=parent.weighted.base.endpoint_clock(self.providers[side](u),u)
            error=np.arctan2(np.sin(clock["phi"][0]-theta),np.cos(clock["phi"][0]-theta))
            if np.any(clock["phi"][1]<=0):raise ArithmeticError("Polar inverse orientation failed")
            if np.max(abs(error))<5e-14:
                self.fast_inverse_calls+=1
                residual=float(np.max(abs(error)))
                self.inverse_receipts.append(dict(side=side,count=len(theta),iterations=iteration+1,
                    maximumResidual=residual,originalFastPath=True))
                return parent.weighted.base.polar_profiles(clock),residual
            u-=error/clock["phi"][1]
        self.safeguarded_inverse_calls+=1
        return super().inverse(side,theta)
