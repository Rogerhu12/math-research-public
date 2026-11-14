"""Constructive exact central cylinder within the clean physical-bump field.

Only the numerical field's central nodal freedom is removed. The target g,
the angular chart, exact tail and every original residual row are retained.
The explicit cylinder X(s,u)=gamma_c(u)+s*e_z needs no C3 assumption.
"""
import numpy as np
from fd2d_gc_raw_bump_clean import CleanRawBumpDAE


class CylinderRawBumpDAE(CleanRawBumpDAE):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fixed_central_nodes = np.flatnonzero(self.x <= self.profile.central_end)
        if self.x[self.fixed_central_nodes[-1]] != self.profile.central_end:
            raise ValueError('The exact central-cylinder trace needs its own mesh node')
        self.representation_kind = 'coalesced_mesh_exact_central_cylinder_v1'
        self.central_field_definition = dict(kind='exact_central_cylinder',
            s_start=0., s_end=float(self.profile.central_end),
            n='actual central seed plus sum c_j*(cos(2j*xi)-mu_j)',
            m=0., l=0., fixed_node_indices=self.fixed_central_nodes.tolist(),
            target_metric_changed=False, additional_surface_regularity_assumed=False)

    def impose_linear_boundary_values(self, vector):
        out = super().impose_linear_boundary_values(vector)
        y, p = self.unpack(out)
        y[self.fixed_central_nodes] = 0.
        y[self.fixed_central_nodes, :self.e] = self.core_coefficients@p[self.central_slice]
        return out

    def parameter_layout(self):
        out = super().parameter_layout()
        out['central_field_definition'] = self.central_field_definition.copy()
        out['eliminated_field_node_count'] = len(self.fixed_central_nodes)+1
        return out
