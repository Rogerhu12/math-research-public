from pathlib import Path
r=Path(__file__).resolve().parent;s=(r.parent/'plateau_core_work/plateau_prefix.py').read_text();changes=[]
def change(a,b):
 global s
 n=s.count(a);assert n>0,a;s=s.replace(a,b);changes.append([a,b,n])
change('from plateau_core import PlateauSupportCore','from homotopy_plateau_core import HomotopyPlateauCore as PlateauSupportCore\nfrom even_mode_loader import load as load_even, module as load_module, TRANSFORMS')
change("SOURCE=ROOT.parent/'true_a_work/bundle/topics/visible-flexible-closed-surface'","SOURCE=ROOT.parent/'m3_flat17_work/recovered/bundle/topics/visible-flexible-closed-surface'")
change("ad=module('plateau_adaptive',SOURCE/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');patch=module('plateau_flat',SOURCE/'scripts/db6f-prefix-flat-profile.py');patch.install(ad);ad.old.install_source(SOURCE/'repro/source-root')","ad=load_even(SOURCE,4)\n short=load_module('even_plateau_short',SOURCE.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py');short.install()")
change('base_mode=3','base_mode=4')
change('64,3,warp_q=a.q','64,4,warp_q=a.q')
change("cfg=json.loads((a.profile or ROOT/'flat17-profile.json').read_text());port=json.loads((a.port_file or ROOT/'flat17-port96.json').read_text())","cfg=json.loads((a.profile or ROOT/'vu25-vd30/profile.json').read_text());port=json.loads((a.port_file or ROOT/'mode4_port8.json').read_text());port['cut']['_prefix_bridge']=cfg['prefix_bridge']")
change("brentq(target,.04,.11,xtol=2e-12)","brentq(target,.8*cfg['delta'],1.2*cfg['delta'],xtol=2e-12)")
change("source_topic=str(SOURCE),linear_delta=", "source_topic=str(SOURCE),source_transforms=TRANSFORMS,linear_delta=")
(r/'even_plateau_prefix.py').write_text(s)
s=(r/'plateau_patch_audit.py').read_text().replace('core.sign*8*core.q','core.sign*core.factor*core.q');(r/'plateau_patch_audit.py').write_text(s)
import json
(r/'driver_transform.json').write_text(json.dumps(changes,indent=2)+'\n')
