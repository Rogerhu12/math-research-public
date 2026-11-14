"""Re-evaluate one saved immutable raw-bump state, with no nonlinear solve."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_clean import CleanRawBumpDAE
from fd2d_gc_raw_bump_cylinder import CylinderRawBumpDAE
from fd2d_gc_codazzi_complement import codazzi_complement
from fd2d_gc_bump_residual_locations import residual_locations


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--representation',choices=('clean','exact-cylinder'),required=True)
    args=ap.parse_args();start=time.monotonic();a=load_npz(args.input)
    cls=CleanRawBumpDAE if args.representation=='clean' else CylinderRawBumpDAE
    problem=cls(args.candidate,modes=int(a['modes']),supports=a['profile_supports'])
    if not np.array_equal(problem.x,a['mesh']) or json.loads(str(a['seed_weight_definition']))!=problem.seed_weight_definition:
        raise ValueError('The declared field representation does not match this saved entity')
    if str(a['candidate_sha256'])!=identity(args.candidate)['sha256']:
        raise ValueError('Candidate identity mismatch')
    vector=np.r_[a['corrections'].ravel(),a['parameters']]
    raw,data=problem.evaluate(vector)
    comp=codazzi_complement(problem,vector,data=data,jacobian=False)
    report=dict(schema='fd2d-closed-raw-bump-state-consumption-v1',source=identity(__file__),
        input=identity(args.input),candidate=identity(args.candidate),
        representation=args.representation,parameter_layout=problem.parameter_layout(),
        seed_weight_definition=problem.seed_weight_definition,
        original_diagnostics=problem.diagnostics(vector,data),
        omitted_codazzi=comp['info'],locations=residual_locations(problem,vector,data,comp),
        nonlinear_solve_performed=False,saved_field_altered=False,continuous_certificate=False)
    arrays=dict(a);arrays.update(full_gauss_nodes=data['full_gauss'],codazzi_cells=data['codazzi_cells'],
        omitted_codazzi_cells=comp['omitted_codazzi_cells'])
    report['field']=save_npz(args.out_prefix.with_name(args.out_prefix.name+'-field.npz'),**arrays)
    definition=problem.profile.definition();metric=args.out_prefix.with_name(args.out_prefix.name+'-physical-metric.json')
    metric.write_text(json.dumps(definition,indent=2)+'\n');report['actual_physical_metric']=identity(metric)
    report['central_definition']=problem.core(a['parameters'][:problem.K])[0].definition()
    report['seconds']=time.monotonic()-start
    args.out_prefix.with_name(args.out_prefix.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(seconds=report['seconds'],raw=float(np.max(abs(raw))),
        full_gauss=report['original_diagnostics']['full_gauss_node_maximum'],
        omitted_codazzi=comp['info']['sampled_omitted_codazzi_maximum'],field=report['field'])),flush=True)


if __name__=='__main__':main()
