"""Optional B32 terminal-layer initializer and declared resolved P1 mesh.

This is a new initialization of the same R181 metric/provider, not an
accepted solution. The full analytic d/m reference obeys Gauss on its
positive-K layer. Angular projection and P1 interpolation do not preserve
that identity and must be measured by the actual finite objective.
"""
from __future__ import annotations
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_raw_lifted_dae import step5
from fd2d_gc_r181_b_round_raw_recovery import (
    R181BRecoveryRoundRawBumpDAE,REPRESENTATION)
from fd2d_gc_r181_b_finite_seed_recovery import finite_nonzero_seed
from fd2d_gc_r181_b_point_objective_recovery import small_gap_parameter_certificate


def create_layer_resolved_problem(*args,terminal_layer_width=.002,**kwargs):
    """Retain every original node; add explicit terminal distances.

    Only the finite P1 partition changes. The candidate, physical profile,
    chart, lifting and all windows remain those of the new B32 provider.
    The floating endpoint is the provider's declared accurate-cut label.
    No equality of that floating length and the accurate length is inferred.
    """
    problem=R181BRecoveryRoundRawBumpDAE(*args,**kwargs)
    width=float(terminal_layer_width)
    final=problem.profile.base.segments[-1]
    if final.get('exact_endpoint_phase')!='-pi/2':
        raise ValueError('This initializer requires the explicit flat-cut brake')
    if not 0<width<float(final['L'])/2:
        raise ValueError('The new layer must lie in the full trace half-brake')
    old=problem.x.copy();end=float(problem.profile.end)
    distances=width*np.asarray([1/64,1/32,1/16,1/8,1/4,1/2,3/4,1.,3/2,2.])
    requested=end-distances
    merged=np.unique(np.r_[old,requested])
    floor=32*np.finfo(float).eps*max(1.,abs(end))
    if np.min(np.diff(merged))<=floor:
        raise ValueError('Requested point would create a near-zero cell; no window was changed')
    view=problem.radial_view(merged)
    where=np.searchsorted(merged,old)
    if not np.array_equal(merged[where],old):
        raise ArithmeticError('All old nodes must remain exactly')
    view.terminal_initialization_mesh=dict(
        schema='fd2d-B32-terminal-initializer-radial-mesh-v1',
        source=identity(__file__),parent_mesh=old.tolist(),
        actual_mesh=merged.tolist(),old_node_to_new_node=where.tolist(),
        added_points=[float(x) for x in merged if not np.any(old==x)],
        terminal_distances_requested=distances.tolist(),
        terminal_layer_width=width,all_old_nodes_retained=True,
        candidate_profile_atlas_lifting_and_windows_unchanged=True,
        finite_objective_new_discretization=True)
    return view


def finite_terminal_layer_seed(problem,*,tail_amplitude=None):
    """Construct a finite nonzero seed, then replace only its inner layer."""
    if problem.representation_kind!=REPRESENTATION:
        raise ValueError('Use the explicit new B32 raw three-field provider')
    mesh=getattr(problem,'terminal_initialization_mesh',None)
    if mesh is None:raise ValueError('Use create_layer_resolved_problem')
    width=float(mesh['terminal_layer_width'])
    z,base_info=finite_nonzero_seed(problem,tail_amplitude=tail_amplitude)
    y,p=problem.unpack(z)
    # The initializer is explicitly on the undeformed new physical profile.
    if np.any(p[problem.profile_slice]!=0.):
        raise ValueError('The reference initializer is defined at new delta=0')
    lift=problem.lifting(p[problem.profile_slice],p[problem.tail_slice])
    ops=problem.operators(p[problem.profile_slice])
    tau=problem.profile.end-problem.x
    mask=(tau>=0)&(tau<=width)
    xi=np.flatnonzero(mask)
    if len(xi)<3:raise ValueError('Declared terminal layer is unresolved')
    full=lift['values'][:,mask]
    n,m,l=(full[...,j] for j in range(3))
    # Round reference is angle-independent but is evaluated from the actual
    # new candidate. Its exact cut value is part of that declared provider.
    packet=problem.reference.jet(problem.x[mask])
    n0=np.asarray(packet['values'])[:,0]
    l0=np.asarray(packet['values'])[:,2]
    q=step5(tau[mask]/width)[0]
    d=(n-l)+(q[None,:]-1)*(n0-l0)[None,:]
    K=ops['jet']['K'][mask]
    radicand=d*d+4*m*m+4*K[None,:]
    if np.min(radicand)<0:
        raise FloatingPointError('Actual layer trace radicand is negative')
    h=np.sqrt(radicand)
    target_n=.5*(h+d);target_l=.5*(h-d)
    add_n=target_n-n;add_l=target_l-l
    pn=(problem.PE@add_n).T;pl=(problem.PE@add_l).T
    # The central taper is exactly zero here. These are complete replacement
    # raw n/l fields, not a second addition on top of the old trace shift.
    y[mask,:problem.e]=pn;y[mask,problem.d:]=pl
    projection_error=max(float(np.max(abs(problem.E@pn.T-add_n))),
                         float(np.max(abs(problem.E@pl.T-add_l))))
    z=problem.impose_linear_boundary_values(z)
    certificate=small_gap_parameter_certificate(problem,z)
    if not certificate['passed']:
        raise ValueError('New finite seed violates its exact parameter domain')
    return z,dict(schema='fd2d-B32-finite-terminal-layer-seed-v1',
        source=identity(__file__),parent_initializer=base_info,
        radial_mesh=mesh,transition_width=width,
        complete_reference='d=q*(n0-l0)+eta*kappa*cos(2u), m=-eta*kappa*sin(u)*cos(u), q=S5((S-s)/width), n,l=(sqrt(d^2+4m^2+4K)+/-d)/2',
        source_coordinate='fixed current atlas; angular projection in its declared xi',
        modified_raw_nodes=xi.tolist(),
        maximum_actual_layer_projection_error=projection_error,
        full_reference_Gauss_zero_before_projection_on_K_positive_layer=True,
        saved_raw_P1_field_not_claimed_Gauss_zero=True,
        exact_boundary_map_reimposed=True,parameter_certificate=certificate,
        BVP_or_continuous_solution_claimed=False)
