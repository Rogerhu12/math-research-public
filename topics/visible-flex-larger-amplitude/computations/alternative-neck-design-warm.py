#!/usr/bin/env python3
"""Explicit changed-metric warm start for the finite-neck nonlinear BVP.

The old and new physical profiles are recorded separately. Positive C2
maps match every corresponding meridian knot; material angles are inverted
before Fourier projection. The intermediate map retains the old image
before projection. It is NOT isometric to the new target metric. The BVP
subsequently solves the new problem and reconstructs its own height mean.

Extra flags: --design-fields comma,separated,fields (default loop_curvature),
--design-control-map keep_offsets|keep_physical (default keep_offsets), and
--design-latitude-map preserve_image|scale_radius (default preserve_image).
The latter option explicitly rescales latitude xy and mean-free z by the
new/old target radius; that changes the image and its angular metric.
All other flags are those of alternative-neck-bvp.py. This wrapper keeps
q and both prescribed core coefficients fixed during a design step.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import gzip,hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent

def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m)
    return m

def take_option(name,default):
    if name not in sys.argv:return default
    j=sys.argv.index(name)
    if j+1==len(sys.argv):raise ValueError('Missing value for '+name)
    value=sys.argv[j+1];del sys.argv[j:j+2]
    return value

def main():
    fields=set(filter(None,take_option('--design-fields','loop_curvature').split(',')))
    control_map=take_option('--design-control-map','keep_offsets')
    latitude_map=take_option('--design-latitude-map','preserve_image')
    if control_map not in ('keep_offsets','keep_physical'):
        raise ValueError('Unknown design-control map')
    if latitude_map not in ('preserve_image','scale_radius'):
        raise ValueError('Unknown design-latitude map')
    if '--restart' not in sys.argv:
        raise ValueError('A successful saved --restart is required')
    adapter=module('alternative_design_adapter',P/'alternative-neck-bvp.py')
    original_module=adapter.module
    neck_chart=module('alternative_design_neck_chart',P/'root_neck_chart.py')

    def patched_module(name,path):
        loaded=original_module(name,path)
        if Path(path).name!='root_dual_core_bvp.py':return loaded
        original_make=loaded.make_dual
        def make_dual(*args,**kwargs):
            Dual=original_make(*args,**kwargs)
            def restart_from(self,saved,pullback,nodes,scale='linear'):
                from fixed_metric_mode3_bvp import merge_profile_mesh
                old=saved.rec;oldcfg=old['frozen_profile']
                if not old.get('solver_success',False):
                    raise ValueError('Design continuation requires a successful old checkpoint')
                if abs(self.q-saved.q)>2e-14*max(1.,self.q):
                    raise ValueError('Do amplitude continuation separately from this design step')
                if not np.allclose(self.ref_coeff,old['chart_reference_coefficients'],rtol=0.,atol=1e-14):
                    raise ValueError('Prescribed core coefficients changed during design step')
                controlled={'delta',self.second_control}
                changed={k for k in set(oldcfg)|set(self.cfg)
                         if k not in controlled and oldcfg.get(k)!=self.cfg.get(k)}
                if not changed<=fields:
                    raise ValueError('Undeclared metric design change: '+','.join(sorted(changed-fields)))
                if old['physical_tail_parameters']!=self.port['parameters']:
                    raise ValueError('This design step keeps physical tail parameters fixed')
                clean=lambda cut:{k:v for k,v in cut.items() if k!='_prefix_bridge'}
                if clean(old['physical_tail_cut'])!=clean(self.port['cut']):
                    raise ValueError('This design step keeps the physical cut fixed')
                p=np.zeros(self.M)
                previous_base=old.get('base_profile')
                if control_map=='keep_offsets' and previous_base is None:
                    raise ValueError('Old base_profile is needed to keep control offsets')
                for j,key in enumerate(('delta',self.second_control)):
                    p[j]=oldcfg[key]-(previous_base[key] if control_map=='keep_offsets' else self.cfg[key])
                coeff=np.asarray(old['core']['coefficients'])
                for j in range(2,min(self.M,len(coeff))):p[j]=coeff[j]/self.pscale[j-1]
                self.select(p);f=self.flow(p[0])
                if self._neck_knots is None:
                    raise ValueError('Changed-metric design warm start requires all-knots chart')
                kinds=lambda flow:[z['kind']for z in flow._alternative_neck.segments+flow.bridge.segments]
                if kinds(f)!=kinds(saved.flow) or len(f.breaks)!=len(saved.flow.breaks):
                    raise ValueError('Physical segment/knot topology changed')
                t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks)
                s,new_ds=self.chart(t,p[0])
                old_chart=neck_chart.NeckChart(self._neck_knots,saved.flow.breaks)
                old_s,old_ds=old_chart.evaluate(t)
                N=max(512,32*(2*self.M+1));psi=2*np.pi*np.arange(N)/N
                B,B1,B2=pullback.basis_values(self.M,saved.mode,psi)
                height=saved.height_jets(old_s,angular=128)
                y=np.empty((self.n,len(t)));error=0.;angle_error=0.;mean_correction=0.
                old_radius=saved.flow.profile(old_s)[0];new_radius=f.profile(s)[0]
                radius_ratio=new_radius/old_radius;angular_metric_error=0.;initial_margin=1.
                mean_range=[float('inf'),-float('inf')]
                for first in range(0,len(t),24):
                    sl=slice(first,first+24);ng=f.geo(s[sl],N)
                    eta,res,_=saved.inverse(old_s[sl],ng['theta'])
                    old_jets=saved.jets(old_s[sl],eta,tuple(h[sl]for h in height))
                    target=old_jets['pos'].copy()
                    old_angle=saved.angle(old_s[sl],eta)
                    angular_scale=ng['rho']/old_angle['rho']
                    target_p1=old_jets['p1']*angular_scale[:,:,None]
                    if latitude_map=='scale_radius':
                        ratio=radius_ratio[sl,None,None]
                        target[:,:,:2]*=ratio
                        center=height[0][sl,None]
                        target[:,:,2]=center+ratio[:,:,0]*(target[:,:,2]-center)
                        target_p1*=ratio
                    desired=(new_radius[sl,None]*ng['rho'])**2
                    angular_metric_error=max(angular_metric_error,float(np.max(abs(np.sum(target_p1*target_p1,axis=2)/desired-1))))
                    residual=target-ng['pos'];state=pullback.project(residual,B)/self.q
                    mean=np.mean(residual[:,:,2],axis=1);reconstructed=ng['pos']+self.q*pullback.values(state,B)
                    reconstructed[:,:,2]+=mean[:,None]
                    error=max(error,float(np.max(np.linalg.norm(reconstructed-target,axis=-1))))
                    angle_error=max(angle_error,res)
                    mean_correction=max(mean_correction,float(np.max(abs(mean-height[0][sl]))))
                    mean_range=[min(mean_range[0],float(mean.min())),max(mean_range[1],float(mean.max()))]
                    d=ng['p1']+self.q*pullback.values(state,B1)
                    dd=ng['p2']+self.q*pullback.values(state,B2)
                    speed=np.linalg.norm(d,axis=2)
                    kap=np.linalg.norm(np.cross(d,dd),axis=2)/speed**3
                    ap=f.profile(s[sl])[1]
                    margin=1-(ap[:,None]/(new_radius[sl,None]*kap))**2
                    initial_margin=min(initial_margin,float(np.min(margin)))
                    y[:,sl]=state
                correction=self.initial(p)-y[:,0]
                y+=correction[:,None]*np.maximum(0.,1-s/(f.Tu/2))[None,:]**3
                physical={**self.cfg,'delta':self.cfg['delta']+p[0],
                          self.second_control:self.cfg[self.second_control]+p[1]}
                record=dict(scope=__doc__,changed_metric_design=True,
                    declared_fields=sorted(fields),changed_uncontrolled_fields=sorted(changed),
                    control_map=control_map,design_latitude_map=latitude_map,old_physical_profile=oldcfg,
                    old_base_profile=previous_base,new_base_profile=self.cfg,
                    new_initial_physical_profile=physical,
                    old_meridian_length=saved.flow.end,new_initial_meridian_length=f.end,
                    old_physical_breaks=saved.flow.breaks.tolist(),new_initial_physical_breaks=f.breaks.tolist(),
                    common_numerical_knots=self._neck_knots.tolist(),
                    radial_map_derivative_range=[float(np.min(old_ds/new_ds)),float(np.max(old_ds/new_ds))],
                    old_modes=saved.M,new_modes=self.M,gauge=self.q,
                    angular_projection=N,height_angular=128,height_quadrature_order=6,
                    intermediate_image_projection_error=error if latitude_map=='preserve_image' else None,
                    projected_design_position_error=error,angle_inverse_error=angle_error,
                    physical_radius_ratio_range=[float(radius_ratio.min()),float(radius_ratio.max())],
                    preprojection_angular_metric_error=angular_metric_error,
                    initial_projected_Frenet_margin_min=initial_margin,
                    intermediate_mean_height_range=mean_range,mean_height_angular_correction_max=mean_correction,
                    inlet_guess_correction_max=float(np.max(abs(correction))),
                    height_mean_disposition='The intermediate position comparison retains its angle-dependent mean correction. The following new-metric BVP independently reconstructs the solved mean from its velocity; this is a design initial guess, not an image-preserving or isometric new solution.',
                    physical_tail_parameters_unchanged=True,fixed_metric_refinement=False)
                return t,y,p,record
            Dual.restart_from=restart_from
            return Dual
        loaded.make_dual=make_dual
        return loaded
    adapter.module=patched_module
    try:adapter.main()
    finally:
        if '--out-prefix' in sys.argv:
            out=Path(sys.argv[sys.argv.index('--out-prefix')+1])
            provenance=dict(scope=__doc__,source_sha256={name:hashlib.sha256((P/name).read_bytes()).hexdigest()
                for name in ['alternative-neck-design-warm.py','alternative-neck-bvp.py','root_neck_chart.py','geometric-checkpoint-core-pullback.py']})
            for path in [out.with_suffix('.json.gz'),out.with_name(out.name+'-summary.json')]:
                if not path.exists():continue
                raw=gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_bytes()
                data=json.loads(raw);data['alternative_neck_design_warm']=provenance
                raw=(json.dumps(data,indent=2)+'\n').encode()
                if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
                if len(raw)>=5000000:raise RuntimeError('Design metadata exceeds file limit')
                path.write_bytes(raw)

if __name__=='__main__':main()
