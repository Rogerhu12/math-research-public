#!/usr/bin/env python3
"""Padded physical cap proposal, retaining the original moving centre.

The original 96-moving-mode factory is used only to load the same complete
32-mode centre, exact target and repair.  This cap has its own physical
Dirichlet inputs and all regular output rows.  No waist amplitude row is
used.  Padding never changes the background, metric, or true exterior
problem; its continuous residual remains an independent obligation.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from fourfold_codazzi_physical_cap_head_model import PhysicalCapHead
from fourfold_codazzi_final_head_trial_model import reflection_weights,sha


class PaddedPhysicalCapHead(PhysicalCapHead):
    def __init__(self,candidate,object_path,q_vector,waist_row,*,physical_modes=128,
                 **kwargs):
        super().__init__(candidate,object_path,q_vector,waist_row,**kwargs)
        old_modes=self.m
        self.m=int(physical_modes);self.n=2*self.m+1
        if self.m not in (112,128) or self.angles<=6*self.m:
            raise ValueError('an explicit fully resolved physical padding is required')
        q=json.loads(Path(q_vector).read_bytes())
        vector=np.asarray(q['q_values'][:self.m],dtype=float)
        if vector.shape!=(self.m,) or not np.all(np.isfinite(vector)):
            raise ValueError('every retained actual outer proposal row is required')
        # controlled() depends only on the target, not on the old factory
        # state dimension.  Its q_vector is used only by the physical
        # boundary_problem inherited below.
        self.system.q_vector=vector
        self.weights=reflection_weights(self.m)
        self.frequency=4*np.arange(1,self.m+1)
        self.sines=np.sin(self.theta[:,None]*self.frequency[None,:])
        self.cosines=np.column_stack((np.ones(self.angles),
                           np.cos(self.theta[:,None]*self.frequency[None,:])))
        self.basis_b=np.column_stack((self.sines,np.zeros((self.angles,self.m+1))))
        self.basis_c=np.column_stack((np.zeros((self.angles,self.m)),self.cosines))
        self.basis_bp=np.column_stack((self.cosines[:,1:]*self.frequency,
                                      np.zeros((self.angles,self.m+1))))
        self.basis_cp=np.column_stack((np.zeros((self.angles,self.m+1)),
                                      -self.sines*self.frequency))
        self.identity.update(modes=self.m,
            physical_state_dimension=self.n,
            original_moving_factory_modes=old_modes,
            physical_input_columns=self.m,
            padded_model_source_sha256=sha(__file__),
            inherited_physical_model_source_sha256=sha(Path(__file__).with_name(
                'fourfold_codazzi_physical_cap_head_model.py')),
            inherited_waist_amplitude_row_not_used_by_physical_cap=True,
            physical_padding_is_not_a_moving_head_identification=True)
