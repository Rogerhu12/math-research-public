"""Re-express an actual exact-cylinder P1 checkpoint on targeted turn nodes."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_turn_mesh import TurnResolvedRawBumpDAE
from fd2d_gc_codazzi_complement import codazzi_complement
from fd2d_gc_bump_residual_locations import residual_locations


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();a=load_npz(args.input)
    p=TurnResolvedRawBumpDAE(args.candidate,modes=int(a['modes']),supports=a['profile_supports'])
    if json.loads(str(a['seed_weight_definition'])) != p.seed_weight_definition:
        raise ValueError('The actual seed lifting must be explicitly identical')
    if 'central_field_definition' not in a:
        raise ValueError('Use an actual exact-cylinder input, not an implicit extra projection')
    if str(a['candidate_sha256']) != identity(args.candidate)['sha256']:
        raise ValueError('The saved state belongs to a different base metric')
    vector,conversion=p.warm_from_actual_P1(a['mesh'],a['corrections'],a['parameters'])
    f,data=p.evaluate(vector);cod=codazzi_complement(p,vector,data=data,jacobian=False)
    y,parameters=p.unpack(vector)
    arrays=dict(mesh=p.x,corrections=y,parameters=parameters,modes=np.array(p.K),
        profile_supports=p.profile.supports,profile_count=np.array(p.J),fixed_base_T=np.array(p.fixed_base_T),
        profile_kind=np.array(p.profile_kind),tail_kind=np.array(p.tail_kind),base_kind=np.array(p.base_kind),
        candidate_sha256=a['candidate_sha256'],blend=np.array(p.blend),
        seed_weight_definition=np.array(json.dumps(p.seed_weight_definition,sort_keys=True)),
        central_field_definition=np.array(json.dumps(p.central_field_definition,sort_keys=True)),
        representation_kind=np.array(p.representation_kind),
        targeted_mesh_definition=np.array(json.dumps(p.targeted_mesh_definition,sort_keys=True)))
    warm=save_npz(args.out_prefix.with_name(args.out_prefix.name+'-warm.npz'),**arrays)
    report=dict(schema='fd2d-targeted-turn-mesh-actual-preparation-v1',source=identity(__file__),
        provider=identity(Path(__file__).parent/'fd2d_gc_raw_bump_turn_mesh.py'),
        candidate=identity(args.candidate),input=identity(args.input),conversion=conversion,
        targeted_mesh_definition=p.targeted_mesh_definition,warm=warm,
        diagnostics=p.diagnostics(vector,data),locations=residual_locations(p,vector,data,cod),
        omitted_codazzi=cod['info'],finite_equations='Existing trapezoidal raw equations re-evaluated on explicit new nodes; no solve',
        seconds=time.monotonic()-start,continuous_certificate=False)
    args.out_prefix.with_name(args.out_prefix.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(seconds=report['seconds'],conversion=conversion,
        raw=float(np.max(abs(f))),full_gauss=report['diagnostics']['full_gauss_node_maximum'],warm=warm)),flush=True)


if __name__=='__main__':main()
