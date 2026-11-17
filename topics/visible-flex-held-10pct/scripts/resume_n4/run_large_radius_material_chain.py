#!/usr/bin/env python3
"""Use the full material-map predictor at every circle-homotopy step.

The base driver, equations, physical parameters, guards and tolerances are
unchanged.  The literal transform replaces only the cross-step initial
guess.  It uses the preceding accepted checkpoint, including its exact
reference lift, and repairs the new core inlet before Newton iteration.
"""
import hashlib,json,types
from pathlib import Path

SOURCE=Path(__file__).with_name('run_large_radius_circle.py')
OLD='if sol is not None:x,y,par=sol.x,sol.y,sol.p'
NEW='''if sol is not None:
                from bimodal_material_restart import restart
                x,y,par,diagnostic=restart(obj,BVP,[record],settings)
                row['material_restart']=diagnostic
                print(json.dumps(dict(event='homotopy_material_restart',**diagnostic)),flush=True)'''

if __name__=='__main__':
    source=SOURCE.read_text()
    if source.count(OLD)!=1:raise RuntimeError('Base driver literal transform mismatch')
    print(json.dumps(dict(event='material_chain_initialization_transform',base_sha256=hashlib.sha256(source.encode()).hexdigest(),replacement=[OLD,NEW],scope=__doc__)),flush=True)
    mod=types.ModuleType('large_radius_material_chain');mod.__file__=str(SOURCE)
    exec(compile(source.replace(OLD,NEW),str(Path(__file__)), 'exec'),mod.__dict__)
    mod.main()
