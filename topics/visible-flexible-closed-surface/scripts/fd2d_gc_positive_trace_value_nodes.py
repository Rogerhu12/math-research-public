"""Same complete actual node values with no whole parameter-jet packet.

The frozen R153/R155 provider is evaluated one radial node at a time.
Only fields and Gauss values are retained. This removes unused all-node
lifting/parameter-jet allocations from a value-only objective. No function,
quadrature, row normalization, or finite boundary equation is changed.
"""
import numpy as np
from fd2d_gc_positive_trace_stream_normal import radial_view


def value_node_packet(problem,vector,*,progress=None):
    y,p=problem.unpack(vector)
    _,axes=problem.core(p[:problem.K])
    fields=np.empty((problem.work,problem.N,3))
    gauss=np.empty((problem.work,problem.N))
    active_n=[];active_h=[]
    for j in range(problem.N):
        view=radial_view(problem,[j])
        _,data=view.evaluate(np.r_[y[j],p])
        fields[:,j]=data['fields'][:,0]
        gauss[:,j]=data['full_gauss'][:,0]
        v=data['gauss_l_delta']['sampled_minimum_active_n']
        if v is not None:active_n.append(float(v))
        v=data['positive_trace_delta']['minimum_active_h']
        if v is not None:active_h.append(float(v))
        del data,view
        if progress is not None:progress(j)
    # This jet is small: only physical profile scalars and seven profile
    # derivatives, never an angular-by-node-by-field-by-all-p array.
    problem.profile.set_parameters(p[problem.profile_parameter_slice])
    jet=problem.profile.jet(problem.x)
    selected=np.asarray(problem.retained_actual_gauss_nodes,int)
    projected=(problem.PE@gauss[:,selected]).T
    central=y[0,:problem.d].copy()
    central[:problem.e]-=problem.core_coefficients@p[:problem.K]
    bottom=np.r_[projected.ravel(),y[-1,problem.d:],central,y[-1,:problem.d],
                 (float(axes['gap'])-problem.gap)/problem.gap]
    data=dict(fields=fields,full_gauss=gauss,projected_gauss=projected,
        axes=axes,parameters=p,physical_profile_parameters=p[problem.profile_parameter_slice].copy(),
        profile_jet=jet,
        gauss_l_delta=dict(sampled_minimum_active_n=min(active_n) if active_n else None),
        positive_trace_delta=dict(minimum_active_h=min(active_h) if active_h else None),
        affine_node_gauss_rows_removed=np.flatnonzero(problem.window()[:-1]==1).tolist(),
        removed_actual_positive_trace_gauss_nodes=np.flatnonzero(problem.x[:-1]>=problem.trace_ramp_stop).tolist(),
        value_only_node_assembly=dict(one_radial_packet_at_a_time=True,
            whole_parameter_packet_retained=False,full_field_definition_unchanged=True,
            finite_rows_unchanged=True,legacy_trapezoid_diagnostic_not_assembled=True))
    return bottom,data
