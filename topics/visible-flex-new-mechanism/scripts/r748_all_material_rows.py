"""All material angular rows of the two-cap development and of its actual joined immersion."""
import numpy as np
from r703_material_geometry_observer import cones,barrier
from r728_full_spinor_geometry import length_rows
from r738_negative_tail_and_macro_source import THETA
from r738_whole_material_macro_continuation_20261128 import mixed_envelopes
from r748_single_height_development import surface,RadialGrid
from r748_height_bounds_and_shell import measured
from r748_nested_true_material_height import grid_edges
from r748_deep_height_sector import one_side


class Cells:
    def __init__(self,opt,stage,seed,detail):
        self.detail=detail;self.depth=opt['tail_depths'][detail]
        self.grid=RadialGrid(grid_edges(opt,stage,detail,seed.knots),opt['radial_orders'][detail])
        self.r=self.grid.r;n=opt['angles'][detail]
        if n%2 or n<=2*stage['K']+2:raise ValueError('Require both exact material axes and all input modes.')
        self.phi=np.arange(n)*(2*np.pi/n);self.phi[n//2]=np.pi
        self.weight=np.zeros(len(self.r))
        for a,b,h in self.grid.cells:self.weight[a+1:b]=h*self.grid.w
        self.width=np.r_[np.diff(self.r),0.]/2+np.r_[0.,np.diff(self.r)]/2
    def evaluate(self,sp,x,opt,full):
        g=self.grid;r=self.r[:,None];phi=self.phi;N=len(phi);span=r[-1,0]-r[0,0]
        jet,E,Ep=sp.jets(g,phi,x)
        a=surface(g,phi,jet,E,Ep,THETA,x[0],x[1],(.105,.175))
        m=np.sqrt(E)[:,None];s=a['normal_height']
        area=self.width[:,None]*r*m
        weight=np.sqrt(area/(N*np.sum(area)));rows=[];masks=[]
        def put(z,mask=None):
            if z.shape!=(len(r),N):raise ValueError('Every material row must cover the whole physical circle.')
            rows.append(weight*z);masks.append(np.ones(z.shape,bool) if mask is None else mask)
        gram=a['relative_Gram_three'][-1]
        h=1+sum(z*z for z in gram)/opt['peak_scale']**2
        for z in (gram[0],np.sqrt(2.)*gram[1],gram[2]):put(h*z)
        put(opt['darboux_weight']*span*a['scalar_D']/(r*m*s**3))
        put(opt['rotation_weight']*a['coframe_W'])
        for k in range(2):put(opt['curl_weight']*a['mixed_displacement'][...,k]/r)
        vals,_=cones(a['actual_physical_six'],THETA)
        for i,y in enumerate(vals):
            target=opt['cone_guard'] if i<4 else opt['axis_guard']
            put(opt['geometry_weight']*barrier(target-y,opt['barrier_scale']),y.real<target)
        # Positive graph and actual chart guard have their own rows as well as a hard domain.
        put(opt['geometry_weight']*barrier(opt['s_guard']-s,opt['barrier_scale']),s.real<opt['s_guard'])
        target_S=self.weight@np.sqrt(E);C=x[:2]
        length,margin=length_rows(target_S,C,opt['length_angles'],opt['length_weight'])
        ax=self.weight@a['A'][:,[0,N//2]]
        width=r[-1,0]-r[0,0]*np.cos(THETA)
        axis=np.array([ax[0]-width+x[0],ax[1]-width-x[0]])
        # Both components of the horizontal displacement and both components of the material angle rotation.
        endpoint=np.r_[a['coframe_rotation_mismatch'].ravel(),
                       (a['inner_minus_outer_position'][0]/span).ravel()]/np.sqrt(N)
        global_rows=np.r_[length,opt['axis_weight']*axis/span,opt['endpoint_weight']*endpoint]
        rr=np.column_stack(rows);active=np.column_stack(masks)
        read=None
        if full:
            if np.iscomplexobj(x):raise ValueError('Physical reports use real candidates only.')
            read=measured(g,phi,a,E,THETA,x[0],x[1])
            shell=read['actual_closed_shell_sample']
            coeff=sp.fields(g,x)[0];freq=np.arange(sp.K+1)
            power=(coeff[0]**2)@((freq**2-1)*freq**2)/(2*self.r**2)
            Kg=Ep/(2*self.r*E**2);pos=np.flatnonzero(Kg>0)
            if len(pos):
                sigma=vals[4].min(axis=1)
                need=sigma*np.maximum(E*self.r*Kg*.03,(E-1+E*power)*.03/self.r)
                err=need-abs(coeff[1,:,0]);worst=pos[np.argmax(err[pos])]
                read['positive_K_outer_height_budget']=dict(r=float(self.r[worst]),height_power_lower=float(power[worst]),
                     actual_mean_radial_height=float(coeff[1,worst,0]),sampled_normal_floor=float(sigma[worst]),
                     proposed_cap_M=1/.03,positive_curvature=float(Kg[worst]),sampled_unsigned_deficit=float(err[worst]),
                     exact_isometry_required=True,sampled_diagnostic_only=True)
            sectors=[one_side(side,c,rate,self.depth,x[:2]) for side,(c,rate) in zip((-1,1),sp.edge_coeff(g,x))]
            deep_ok=all(z['available'] for z in sectors);mixed=None
            if deep_ok:mixed=mixed_envelopes(a['actual_physical_six'],(np.array([[x[0],0.,x[1]]]),),sectors,shell['shell'])
            pose_margin=min(.0115-abs(x[0]),.0426-abs(x[1]))
            eta=max(shell['eta'],*(float(z.get('normalized_metric_operator_upper','0')) for z in sectors))
            read.update(whole_deep_sectors=sectors,mixed_shell_envelopes=mixed,eta=eta,
                    whole_deep_pass=deep_ok,shell_pass=bool(shell['shell_pass'] and deep_ok and mixed['admissible'] and pose_margin>0),
                    target_metric_meridian_integral=float(target_S),target_directional_meridian_margin=float(margin),
                    actual_axis_position_residuals=axis.tolist(),center_xz=x[:2].tolist(),pose_rectangle_margin=pose_margin,
                    curvature=shell['curvature'],shape_violation=shell['violation']+max(0.,-pose_margin),
                    selected_deep_depth=self.depth,query_grid=[len(r),N],entire_body_or_trajectory_certified=False)
        return dict(rows=rr,active=active,global_rows=global_rows,read=read,
                    norm=float(np.linalg.norm(np.r_[rr.real.ravel(),global_rows.real])))


def admissible(now,old,opt):
    if not now['whole_deep_pass'] or now['pose_rectangle_margin']<=0 or now['true_sampled_min_s']<=opt['s_floor']:
        return False
    if now['target_directional_meridian_margin']<min(0.,old['target_directional_meridian_margin']):return False
    if old['shell_pass']:return now['shell_pass'] and now['eta']<old['eta']
    # Genuine shell recovery is separately named. Once feasible, stay feasible.
    return ((now['shell_pass'] and now['eta']<=old['eta']*1.02) or
            (now['shape_violation']<old['shape_violation'] and now['eta']<old['eta']))


def strict(read,opt):
    return (read['shell_pass'] and read['eta']<opt['goal'] and read['target_directional_meridian_margin']>=0 and
        read['true_sampled_min_s']>opt['s_floor'] and max(abs(v) for v in read['actual_axis_position_residuals'])<opt['goal']*.145 and
        max(max(v) for v in read['real_boundary_two_jets'])<opt['rim_tolerance'] and
        max(read['actual_inner_outer_join_displacements'])<opt['goal'] and
        max(read['delta_W_direct_vs_curvature_integral'],read['delta_H_direct_vs_W_integral'])<opt['integration_gate'])

