"""Read the actual joined surface, the two axial constraints and rigorously propagate supplied all-cell bounds."""
from types import SimpleNamespace
import re
import numpy as np
from r726_closed_spinor_fourier import public
from r734_true_dyadic_tail import I,D,ZERO,monotone_trans
from r728_full_spinor_geometry import read_curve


def measured(grid,phi,context,E,theta,cx,cz):
    public()
    if grid.r[0]!=.075 or grid.r[-1]!=.22 or np.sin(theta)<.2699999999 or np.sin(theta)>.2700000001:
        raise ValueError('R680 whole-rigid-part observer requires the actual R738/R745 dimensions.')
    F=context['actual_physical_six'];c=F[0].mean(axis=1);c[0]=[cx,0.,cz];c[-1]=0.
    g=SimpleNamespace(r=grid.r,a=.075,b=.22,theta=theta)
    angles=np.broadcast_to(np.asarray(phi)[None,:],F[0].shape[:2])
    physical=read_curve(g,F,(c,),np.asarray(E),angles)
    axes=[]
    for angle in (0.,np.pi):
        match=np.flatnonzero(np.asarray(phi)==angle)
        if len(match)!=1:
            axes=[];break
        i=match[0];axes.append(float(-grid.primitive_from_outer(context['A'][:,i],0.)[0]))
    if axes:
        axial=dict(L_plus=axes[0],L_minus=axes[1],horizontal_sum_defect=sum(axes)-2*(g.b-g.a*np.cos(theta)),
                   actual_center_x_defect=cx-(axes[1]-axes[0])/2)
    else:axial=dict(available=False,reason='Both exact reflection-axis evaluation columns required.')
    absmax=lambda x:float(np.max(abs(x)))
    return dict(actual_closed_shell_sample=physical,real_boundary_two_jets=context['inner_outer_rim_errors'],
          axial_horizontal_lengths=axial,scalar_D_sampled_max=absmax(context['scalar_D']),
          delta_W_direct_vs_curvature_integral=absmax(context['coframe_W']-context['integrated_W']),
          delta_H_direct_vs_W_integral=absmax(context['mixed_displacement']-context['integrated_H']),
          actual_inner_outer_join_displacements=[absmax(context[name]) for name in
                      ('coframe_rotation_mismatch','inner_minus_outer_position','inner_minus_outer_radial','inner_minus_outer_angular')],
          true_sampled_min_A=float(context['A'].min()),true_sampled_min_s=float(context['normal_height'].min()),
          relative_three_Gram_maxima=[[absmax(t) for t in g] for g in context['relative_Gram_three']],
          sampled_only=True,whole_continuous_metric_or_reach_certified=False)


def conditional_bound(edges,cells,boundary,source_proof_sha256):
    """Propagate declared continuous bounds only; does not establish their input certificates."""
    public()
    if not re.fullmatch('[a-f0-9]{64}',source_proof_sha256):raise ValueError('An identified external continuous-bound proof is required.')
    r=[I(*z) for z in edges]
    if len(r)!=len(cells)+1 or any(q.lo<=0 for q in r):raise ValueError('Invalid certified radial grid.')
    pos=lambda d:I(D(d))
    W,H=pos(boundary['W_upper']),pos(boundary['H_upper'])
    if W.lo<0 or H.lo<0:raise ValueError('Invalid signed bound.')
    out=[];worst=ZERO
    for i in reversed(range(len(cells))):
        w=r[i+1]-r[i];c=cells[i]
        a,s,e,d=[pos(c[k]) for k in ('A_upper','normal_s_lower','E_lower','D_absolute_upper')]
        if min(w.lo,a.lo,s.lo,e.lo)<=0 or d.lo<0:raise ValueError('Actual nonnegative continuous bounds and positive chart required.')
        rate=d/(I(r[i].lo)*monotone_trans(e,'sqrt')*s**3)
        H=H+a*w*(W+rate*w/2);W=W+rate*w
        delta=H/I(r[i].lo)
        eta=(1+monotone_trans(I(2),'sqrt'))*delta+delta**2
        er,ep=[pos(c[k]) for k in ('relative_radial_join_error_upper','relative_angular_join_error_upper')]
        if min(er.lo,ep.lo)<0:raise ValueError('Each full-interval join error must be bounded.')
        J=er+ep;after=eta+2*monotone_trans(1+eta,'sqrt')*J+J**2
        out.append(dict(radial_cell=i,inner_W_upper=str(W.hi),inner_H_upper=str(H.hi),
                        full_cell_relative_Gram_upper=str(after.hi)))
        worst=I(max(worst.hi,after.hi))
    return dict(all_cell_Gram_upper=str(worst.hi),from_inner_to_outer=out[::-1],
                conditional_on_real_continuous_cell_bounds=source_proof_sha256,
                establishes_input_proofs_or_whole_reach=False)
