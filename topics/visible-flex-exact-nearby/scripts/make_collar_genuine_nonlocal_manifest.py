"""Generate the once-only GNF public push input inventory and CPU workflow, without numerical imports."""
from argparse import ArgumentParser
import ast
from fractions import Fraction as Q
from hashlib import sha1,sha256
import json
from pathlib import Path

TOPIC='topics/visible-flex-exact-nearby'
OWNER='fourfold_codazzi_collar_genuine_nonlocal_owner.py'
MANIFEST='notes/2026-11-28-physical-root-finite-nonlocal-inputs.json'
PROOF='results/R149-supplement-complete-root-collar-nonlocal-source-with-both-physical-circle-inverses.md'
YAML='.github/workflows/fourfold-codazzi-physical-root-finite-nonlocal.yml'
ORIGINAL='8c7e3995ea38d81af07a664866d9e6fd34735f29e1cb3a04ee5c9b9d59e71763'
SUPPORT=[PROOF,
 'results/R149-supplement-signed-two-circle-residual-for-complete-nonlocal-and-mean-sources.md',
 'results/R149-supplement-uniform-negative-circle-inverse-through-the-true-root.md',
 'notes/2026-11-28-JCR-new-actual-root-circle-rational-comparisons.json',
 'results/R133-supplement-complete-real-interval-angular-inverse-and-physical-mean.md',
 'results/R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md',
 'results/R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md',
 'results/R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md',
 'results/R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md',
 'results/R133-supplement-actual-genuine-common-radial-columns-and-old-circle-inverse.md',
 'results/R149-supplement-signed-Laurent-terminal-column-and-physical-shift-reception.md',
 'results/R149-supplement-signed-free-first-wave-and-correlated-genuine-potential.md',
 'results/R149-supplement-first-genuine-source-through-the-physical-waist-and-common-input.md',
 'results/R133-supplement-seven-positive-ports-and-mixed-root-to-waist-density.md',
 'results/R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md',
 'notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json',
 'notes/paid_waist_strong_error_assembly_ci/run-43769746581-1/actual-scientific-conclusion.json',
 'notes/paid_waist_strong_error_assembly_ci/run-43769746581-1/execution.json',
 'notes/common_radial_potential_budget_ci/run-43685624307-1/execution.json',
 'notes/common_reference_columns_old_circle_ci/run-43688459733-1/execution.json',
 'notes/genuine_signed_local_collar_ci/run-46143574106-1/whole-scientific-conclusion.json',
 'notes/genuine_signed_local_collar_ci/run-46143574106-1/root-whole-admission.json',
]


def check(ok,msg):
    if not ok:raise ValueError(msg)


def canonical(z):return (json.dumps(z,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()


def files(root,overlay):
    chosen={}
    def add(rel):
        source=overlay.get(rel,root/TOPIC/rel);data=source.read_bytes()
        path=TOPIC+'/'+rel
        chosen[path]=dict(path=path,bytes=len(data),sha256=sha256(data).hexdigest(),
                          git_blob_sha=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
        return data
    todo=['scripts/'+OWNER]
    while todo:
        path=todo.pop()
        if TOPIC+'/'+path in chosen:continue
        tree=ast.parse(add(path),filename=path)
        for item in ast.walk(tree):
            names=[]
            if isinstance(item,ast.Import):names=[n.name for n in item.names]
            if isinstance(item,ast.ImportFrom):names=[item.module or '']
            for name in names:
                if name.startswith('fourfold_'):todo.append('scripts/'+name+'.py')
    for path in SUPPORT:add(path)
    sp=json.loads((root/TOPIC/'notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json').read_bytes())
    ss=sp['actual_scientific_receipt'];raw=canonical(ss)
    check(sp['run_id']==ss['run_id']=='43731464771' and sp['run_attempt']==ss['run_attempt']=='1'
          and sp['complete'] and ss['complete'] and sp['actual_returncode']==ss['actual_returncode']==0
          and len(ss['gates'])==20 and all(g['passed'] for g in ss['gates'])
          and dict(file='consumers/process.json',bytes=len(raw),sha256=sha256(raw).hexdigest()) in sp['output_hashes'],
          'authentic full strict propagation underlying the mixed PW point source')
    wp=root/TOPIC/'notes/paid_waist_strong_error_assembly_ci/run-43769746581-1'
    raw=(wp/'actual-scientific-conclusion.json').read_bytes();ws=json.loads(raw);we=json.loads((wp/'execution.json').read_bytes())
    check(we['run_id']==ws['run_id']=='43769746581' and we['run_attempt']==ws['run_attempt']=='1' and we['complete'] and ws['complete']
          and ws['proved'] and we['actual_returncode']==ws['actual_returncode']==0 and we['actual_failure'] is ws['failure'] is None
          and len(ws['gates'])==22 and all(g['passed'] for g in ws['gates']) and we['source_sha256']==ws['source_sha256']
          and we['input_manifest_sha256']==ws['input_manifest_sha256']
          and dict(file='actual-scientific-conclusion.json',bytes=len(raw),sha256=sha256(raw).hexdigest()) in we['output_hashes'],
          'authentic original output and common input receiver used by GSW')
    return [chosen[k] for k in sorted(chosen)]


def manifest(inventory):
    return dict(kind='R149_GNF_finite_nonlocal_original_columns_v1',repository='Rogerhu12/math-research-public',
        files=inventory,old_original_receipts_sha256=ORIGINAL,original_whole_count=112,
        original_private_restore_rule='read the 112 complete original historical inputs, verifying each whole size and SHA before use',
        root_interval=['1191984371497/5000000000000','2383968743003/10000000000000'],physical_cut='76285779072683/320000000000000',
        inputs=[97,2**20],radial_slabs=16,individually_split_through=128,angular_strip='1/512',angular_lags=[-128,128],
        output_windows=['-5/3','-2/3','scalar'],input_signs=[1,-1],reference_columns=['terminal_Ai','genuine_second'],
        full_unprojected_G10_inputs=['Fw','Fh','Fy','Fg','Fq'],local_in_this_target=0,
        old_target_calls=0,scientific_workers_at_most=4,precision_bits=320,maximum_scientific_wall_seconds=19100,
        maximum_job_memory_bytes=14<<30,maximum_raw_private_bytes=240000000,physical_finite_input_new_target_only=True,
        private_carrier_published=False,final_branch_claimed=False)


def workflow(m,raw):
    digest=sha256(raw).hexdigest();paths=['README.md',TOPIC+'/README.md',TOPIC+'/'+MANIFEST]+[s['path'] for s in m['files']]
    select='\n'.join('            /'+p for p in paths)
    return f'''name: Genuine finite root nonlocal and independent physical mean
on:
  push:
    branches: [main]
    paths:
      - {YAML}
permissions:
  contents: read
concurrency:
  group: visible-flex-exact-finite-root-physical-nonlocal-20261128
  cancel-in-progress: false
jobs:
  physical-circle-sources:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-24.04
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    timeout-minutes: 325
    env:
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      PYTHONDONTWRITEBYTECODE: '1'
    steps:
      - name: Install the public read-only repository transport
        run: |
          apt-get update -qq
          apt-get install -y --no-install-recommends git ca-certificates
      - uses: actions/checkout@v4
        with:
          ref: ${{{{ github.sha }}}}
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
{select}
      - name: Check every current whole source before numerical imports
        env:
          FROZEN_MANIFEST: {TOPIC}/{MANIFEST}
          FROZEN_SHA256: {digest}
        run: |
          git config --global --add safe.directory "$GITHUB_WORKSPACE"
          python -B - <<'PYEND'
          import ast,hashlib,json,os
          from pathlib import Path
          b=Path(os.environ['FROZEN_MANIFEST']).read_bytes();h=hashlib.sha256(b).hexdigest()
          assert h==os.environ['FROZEN_SHA256']
          z=json.loads(b);assert len(set(s['path'] for s in z['files']))==len(z['files'])
          for s in z['files']:
              p=Path(s['path']);v=p.read_bytes()
              assert (len(v),hashlib.sha256(v).hexdigest(),hashlib.sha1(b'blob '+str(len(v)).encode()+b'\\0'+v).hexdigest())==(s['bytes'],s['sha256'],s['git_blob_sha'])
              if p.suffix=='.py':ast.parse(v,filename=str(p))
          print('GNF_FROZEN_SOURCES',len(z['files']),h,'original input count',z['original_whole_count'])
          PYEND
          python -m pip install --disable-pip-version-check --only-binary=:all: numpy==2.3.5 scipy==1.17.0 python-flint==0.9.0
      - name: Measure all finite root-collar nonlocal columns and the true physical mean
        env:
          FROZEN_SHA256: {digest}
        run: |
          script_root={TOPIC}/scripts
          python -B "$script_root/fourfold_codazzi_true_ratio_live_rules.py" python -B "$script_root/{OWNER}" --repo "$GITHUB_WORKSPACE" --manifest "{TOPIC}/{MANIFEST}" --manifest-sha "$FROZEN_SHA256" --private "$RUNNER_TEMP/gnf-private" --receipt "$RUNNER_TEMP/gnf-actual.json"
      - name: Print the entire small terminal outcome or its confirmed physical prefix
        if: always()
        run: |
          python -B - <<'PYEND'
          import hashlib,json,os
          from pathlib import Path
          p=Path(os.environ['RUNNER_TEMP'])/'gnf-actual.json'
          if p.is_file():
              b=p.read_bytes();z=json.loads(b)
              assert 0<len(b)<100000 and isinstance(z['complete'],bool)
              print('GNF_FINAL_WHOLE_OR_PREFIX',len(b),hashlib.sha256(b).hexdigest(),b.decode().strip(),flush=True)
          PYEND
'''


def main():
    ap=ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--owner-overlay',type=Path);ap.add_argument('--mean-overlay',type=Path);ap.add_argument('--proof-overlay',type=Path)
    args=ap.parse_args();overlay={}
    if args.owner_overlay:overlay['scripts/'+OWNER]=args.owner_overlay
    if args.mean_overlay:overlay['scripts/fourfold_codazzi_genuine_physical_mean_adjoint.py']=args.mean_overlay
    if args.proof_overlay:overlay[PROOF]=args.proof_overlay
    m=manifest(files(args.repo,overlay));raw=canonical(m);text=workflow(m,raw)
    args.out.mkdir(parents=True,exist_ok=True)
    for fname,data in ((Path(MANIFEST).name,raw),(Path(YAML).name,text.encode())):
        path=args.out/fname;path.write_bytes(data);check(path.read_bytes()==data,'whole generated entry')
        print(path,len(data),sha256(data).hexdigest())
    print('frozen files',len(m['files']),'old or new numerical calls',0)


if __name__=='__main__':main()
