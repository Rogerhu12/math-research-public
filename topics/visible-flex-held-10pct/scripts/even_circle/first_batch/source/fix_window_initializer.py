from pathlib import Path
import hashlib,json
p=Path(__file__).with_name('even_window_prefix.py');s=p.read_text();old=hashlib.sha256(s.encode()).hexdigest()
a="configure(Path(__file__).with_name('consumed_window_profile.py'),source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py')"
b=a+"\n    module('even_window_short_install',source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install()"
assert s.count(a)==1;s=s.replace(a,b)
a="port=json.loads(args.port_file.read_text());_PORT_CUT=port['cut'];parameters=json.loads(args.profile.read_text())"
b=a+"\n    port['cut']['_prefix_bridge']=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.2)"
assert s.count(a)==1;s=s.replace(a,b);p.write_text(s)
Path(__file__).with_name('window_initializer_fix.json').write_text(json.dumps(dict(old_sha256=old,new_sha256=hashlib.sha256(s.encode()).hexdigest(),reason='Base BVP initializer constructed an unused legacy DirectionalBridge and raised before any nonlinear iteration. Install the same actual ShortBridge used by the complete custom metric; no equation or guard change.'),indent=2)+'\n')
