from pathlib import Path
import shutil,hashlib,json
r=Path(__file__).resolve().parent;base=r.parent/'plateau_core_work';n4=r.parent/'n4_meridian_work'
for f in ['consumed_window_profile.py']:
 shutil.copy2(base/f,r/f)
shutil.copy2(n4/'consumed_short_profile.py',r/'consumed_short_profile.py')
s=(base/'consumed_window_loop.py').read_text().replace('m=3*np.arange(1,modes+1)','m=4*np.arange(1,modes+1)');(r/'four_mode_linear.py').write_text(s)
s=(base/'window_prefix.py').read_text();changes=[]
def change(a,b):
 global s
 n=s.count(a);assert n>0,a;s=s.replace(a,b);changes.append([a,b,n])
change('from consumed_window_loop import ConsumedWindowLoop,linear_residual,sampled_geometry','from four_mode_linear import linear_residual,sampled_geometry\nfrom consumed_short_profile import ConsumedShortLoop,configure\nfrom even_mode_loader import load as load_even,TRANSFORMS\n_PORT_CUT={}\ndef ConsumedWindowLoop(**parameters):return ConsumedShortLoop(_PORT_CUT,**parameters)')
change('def main():','def main():\n    global _PORT_CUT')
change('default=math.pi/3','default=0.')
change("ad=module('window_adaptive',source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py')\n    ad.old.install_source(source/'repro/source-root')","ad=load_even(source,4)\n    configure(Path(__file__).with_name('consumed_window_profile.py'),source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py')")
change("port=json.loads(args.port_file.read_text());parameters=json.loads(args.profile.read_text())","port=json.loads(args.port_file.read_text());_PORT_CUT=port['cut'];parameters=json.loads(args.profile.read_text())")
change("cfg=dict(delta=.07255,vu=.17,vd=.18,ramp=.4,cycles=1,direction='outward',window_parameters=parameters)","cfg=dict(delta=parameters['delta'],vu=parameters['vu'],vd=parameters['return_speed'],ramp=parameters['epsilon'],cycles=1,direction='outward',window_parameters=parameters)")
change('self.pscale,3,**settings','self.pscale,4,**settings')
change('base_mode=3','base_mode=4')
change("script_sha256=hashlib.sha256", "source_transforms=TRANSFORMS,script_sha256=hashlib.sha256")
(r/'even_window_prefix.py').write_text(s);(r/'window_driver_transform.json').write_text(json.dumps(changes,indent=2)+'\n')
