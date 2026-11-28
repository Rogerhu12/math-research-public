"""All two-equation material, frame and Cartesian physical rows for the same R764 metric."""
import numpy as np
from r703_material_geometry_observer import cones,barrier
from r738_negative_tail_and_macro_source import THETA
from r748_single_height_development import RadialGrid
from r748_nested_true_material_height import grid_edges
from r683_proper_phase_metric_transport_20261128 import shell_ok
from r761_unrestricted_frame_and_solid import cap_fields,shell3,projected_geodesic_rows
from r766_gauss_codazzi_material_frame import Frame,Space
from r766_single_hermite_physical_surface import all_six,compared
from r766_deep_so3_hermite_bounds import both

class Field:
    def __init__(self,book,base,opt,stage,detail,sp):
        t=opt['theta'];self.base,self.book,self.sp,self.detail=base,book,sp,detail
        if t!='arcsin(.27)':raise ValueError('Only the actual R764 endpoint is specified.')
        add=[*sp.knots,.085-.0045,.085,.085+.0045,.21-.0045,.21,.21+.0045,.083,.212,.1475]
        self.grid=RadialGrid(grid_edges(opt,stage,detail,add),opt['radial_orders'][detail]);self.depth=opt['tail_depths'][detail]
        self.phi=np.arange(opt['angles'][detail])*(2*np.pi/opt['angles'][detail]);self.phi[len(self.phi)//2]=np.pi
        self.r=self.grid.r;self.frame=Frame(sp,self.grid,self.phi,base,book)
        self.w=np.zeros(len(self.r));self.width=(np.r_[0.,np.diff(self.r)]+np.r_[np.diff(self.r),0.])/2
        for i,j,h in self.grid.cells:self.w[i+1:j]=h*self.grid.w
        self.halved=None
    def independent(self,sp,x,coarse):
        if self.halved is None:self.halved=Frame(sp,self.grid,self.phi,self.base,self.book,refine=2)
        fine=all_six(self.halved,sp,x)
        e=compared(self.frame,self.halved,coarse,fine)
        # Physical F on the bisected representation includes all between-node points.
        mat=self.halved.original.mat
        deep=both(sp,x,self.halved.r,self.depth)
        class Grid: pass
        grid=Grid();grid.r=self.halved.r
        e['independent_bisected_shell']=physical(grid,self.phi,fine,x,mat,deep);return e
    def evaluate(self,sp,x,opt,physical_read=True):
        st=all_six(self.frame,sp,x);curve=st['actual_six'];g=st['frame'];r=self.r[:,None];m=self.frame.original.mat['m'];E=m*m
        N=len(self.phi);rw=np.sqrt(self.width*self.r*m/np.sum(self.width*self.r*m));w=rw[:,None]/np.sqrt(N)
        rows=[];mask=[]
        def add(q,active=None):
            rows.append(q*w);mask.append(np.ones(q.shape,bool) if active is None else active)
        for q in g['gc']:add(opt['gc_weight']*r*q)
        for q in g['actual_Xphi_errors']:
            for i in range(3):add(opt['connection_weight']*q[...,i])
        a,b,c=st['actual_Gram'];emph=1+(a*a+2*b*b+c*c)/opt['peak_scale']**2
        for z in (a,np.sqrt(2.)*b,c):add(z*emph)
        for i,z in enumerate(cones(curve,THETA)[0]):
            bound=opt['cone_guard'] if i<4 else opt['axis_guard'];add(opt['geometry_weight']*barrier(bound-z,.004),z.real<bound)
        T=st['design_T'];period=T.mean(axis=1);gl=[(rw[:,None]*period).ravel()]
        er,et,_=cap_fields(self.phi,THETA);nn=np.cross(er,et);Rin=np.stack((er,et,nn),axis=-1)
        pose=g['rotation'][0][0]-Rin;gl.append((pose/np.sqrt(N)).ravel())
        S=self.w@m;lg,lm=projected_geodesic_rows(S,x[:3],opt['length_meridians'],opt['length_directions'],opt['length_weight']);gl.append(lg)
        for end in st['inner_and_outer_unadjusted_six']:
            for rho,group in zip((8.,1.2,.08),end):
                for j,q in zip((1.,.4,.08),group):gl.append(rho*j*q.ravel()/np.sqrt(N))
        v=np.column_stack(rows);active=np.column_stack(mask);glob=np.concatenate(gl);read=None
        if physical_read:
            dd=both(sp,x,self.r,self.depth)
            read=physical(self.grid,self.phi,st,x,self.frame.original.mat,dd)
            hi=[int(np.argmin(abs(self.r-u))) for u in (.085,.21)]
            read.update(target_geodesic_bound_margin=lm,target_meridian_integral=float(S),
                actual_center=x[:3].tolist(),developed_center=st['developed_center'].tolist(),
                real_two_Codazzi=[float(abs(r*q).max()) for q in g['gc']],actual_high_circle_k_ranges=[[float(g['k'][i].min()),float(g['k'][i].max())] for i in hi],
                actual_full_radial_two_field_count=2,source_curvature_angle_connection=st['diagnostics'],period_max=float(abs(period).max()),
                actual_high_circle_periods=period[hi].tolist(),raw_rim_max=float(max(abs(z).max() for e in st['inner_and_outer_unadjusted_six'] for group in e for z in group)),
                raw_inner_frame=float(abs(pose).max()),cap_six=st['cap_six'])
            if self.detail==2:read['independent_halfstep_and_actual_ODE_defect']=self.independent(sp,x,st)
        return dict(rows=v,active=active,global_rows=glob,read=read,norm=float(np.linalg.norm(np.r_[v.real.ravel(),glob.real])))

def physical(grid,phi,st,x,mat,deep):
    rc=shell3(grid,phi,st['actual_six'],x[:3],mat['E'],deep,THETA)
    old=rc.pop('pose_margin');rc['unused_R680_rectangle']=old;rc['violation']-=max(0.,-old)
    sh=rc['shell'];mix=rc['mixed'];rc['shell_pass']=bool(rc['deep_pass'] and mix['admissible'] and shell_ok(sh))
    rc['pose_margin']=min(sh['peg_outer_tube_cylinder_margin'],sh['sampled_whole_support_dominance'],sh['sampled_side_margin'],sh['sampled_cylinder_margin'])
    rc['whole_deep_pass']=rc['deep_pass'];rc['whole_deep_sectors']=deep
    rc['eta']=max(rc['eta'],*[float(z.get('normalized_metric_operator_upper',0.)) for z in deep])
    return rc

def admissible(a,b):
    if not a['whole_deep_pass'] or a['target_geodesic_bound_margin']<min(0.,b['target_geodesic_bound_margin']):return False
    if b['shell_pass']:return a['shell_pass'] and a['eta']<b['eta']
    return (a['shell_pass'] and a['eta']<=b['eta']*1.02) or (a['violation']<b['violation'] and a['eta']<b['eta'])

def strict(o,opt):
    return (o['shell_pass'] and o['target_geodesic_bound_margin']>=0 and max(o['eta'],o['raw_rim_max'],o['raw_inner_frame'],o['period_max'],
            *o['real_two_Codazzi'],*o['source_curvature_angle_connection']['complete_frame_angular_connection'])<opt['goal']
            and max(max(a) for a in o['cap_six'])<opt['rim_tolerance'])
