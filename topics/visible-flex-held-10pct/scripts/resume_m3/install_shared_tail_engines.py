#!/usr/bin/env python3
"""Share same-mu engines in an owned copy of the current sparse tail solver.

Only allocation and process diagnostics change.  Engine options other than
mu are fixed within each DN construction; its local cache never crosses a
DN, physical design, mode count, or quadrature.  Split replacement preserves
the engine object captured by cutJets.  No ODE, floating summation, sparse
linear system, root guard, shooting residual, or acceptance gate is edited.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil


def sha(text):return hashlib.sha256(text.encode()).hexdigest()


def replace(text,before,after):
    if text.count(before)!=1:raise ValueError('Unexpected source marker/count: '+before)
    return text.replace(before,after)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('copy-from','source-topic','manifest','export-modules'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();source=a.copy_from.resolve();dest=a.source_topic.resolve()
    if source==dest or dest.exists():raise ValueError('Use a fresh independent source copy')
    names=['950f-tail-stage-core.mjs','950f-tail-stage-split.mjs','950f-tail-client-v3.py']
    original={name:(source/'scripts'/name).read_text() for name in names}
    if 'function sparseGlobalSolve(payload)' not in original[names[0]]:
        raise ValueError('The current sparse solver is required; do not install a historical dense core')
    derived={}
    before=" const graphs=wholeGraph.graphs,gains=wholeGraph.gains,cells=stages.cells.map(c=>{const e=engineFactory({modes:M,spacing,quadrature,mu:c.mu,orientation,projectionFloor});return {...c,engine:cuspAwareFlow?withCuspAwareRK(e):e};});"
    after=""" // Same-mu allocation cache is local to this one fixed-options DN.
 const engineCache=new Map();
 const graphs=wholeGraph.graphs,gains=wholeGraph.gains,cells=stages.cells.map(c=>{
  if(!engineCache.has(c.mu)){
   const e=engineFactory({modes:M,spacing,quadrature,mu:c.mu,orientation,projectionFloor});
   engineCache.set(c.mu,cuspAwareFlow?withCuspAwareRK(e):e);
  }
  return {...c,engine:engineCache.get(c.mu)};
 });"""
    core_before,core_after=before,after
    derived[names[0]]=replace(original[names[0]],core_before,core_after)
    before='  for(const cell of dn.tail.cells){\n    let engine='
    after='  const replaced=new Set();\n  for(const cell of dn.tail.cells){\n    if(replaced.has(cell.engine))continue;\n    replaced.add(cell.engine);\n    let engine='
    derived[names[1]]=replace(original[names[1]],before,after)
    s=original[names[2]]
    s=replace(s,'import gzip, hashlib, json, os, subprocess','import gzip, hashlib, json, os, subprocess, time')
    s=replace(s,"        self.proc=subprocess.Popen(['node',str(worker),str(self.config)],stdin=subprocess.PIPE,",
      "        self.stderr_path=self.record_prefix.with_name(self.record_prefix.name+'_worker_stderr.log')\n"
      "        self.exit_path=self.record_prefix.with_name(self.record_prefix.name+'_worker_exit.json')\n"
      "        self.stderr_file=self.stderr_path.open('x');self.exit_events=[]\n"
      "        self.proc=subprocess.Popen(['node',str(worker),str(self.config)],stdin=subprocess.PIPE,")
    s=replace(s,'stdout=subprocess.PIPE,text=True,bufsize=1,env=env)',
                'stdout=subprocess.PIPE,stderr=self.stderr_file,text=True,bufsize=1,env=env)')
    s=replace(s,"        if not line: raise RuntimeError('Weighted stage-tail initialization failed')",
      "        if not line:\n            self._record_exit('initialization-eof')\n            raise RuntimeError('Weighted stage-tail initialization failed')")
    s=replace(s,"        if not line:raise RuntimeError('Weighted tail worker stopped')",
      "        if not line:\n            self._record_exit('response-eof')\n            raise RuntimeError('Weighted tail worker stopped')")
    s=replace(s,'    def close(self):',"""    def _record_exit(self,reason):
        code=self.proc.poll()
        if code is None:
            try:code=self.proc.wait(timeout=1)
            except subprocess.TimeoutExpired:pass
        self.stderr_file.flush()
        self.exit_events.append(dict(reason=reason,returncode=code,calls=self.calls,
            unix_time=time.time(),stderr_path=str(self.stderr_path),stderr_bytes=self.stderr_path.stat().st_size))
        self.exit_path.write_text(json.dumps(dict(events=self.exit_events),indent=2)+'\\n')
    def close(self):""")
    s=replace(s,'            except Exception:self.proc.terminate()',
      "            except Exception:self.proc.terminate()\n        self._record_exit('close')\n        self.stderr_file.close()")
    compile(s,str(dest/'scripts'/names[2]),'exec');derived[names[2]]=s
    # Numerical source outside these exact allocation lines stays byte-identical.
    stripped=replace(derived[names[0]],core_after,core_before)
    if stripped!=original[names[0]]:raise AssertionError('Unexpected numerical core change')
    shutil.copytree(source,dest,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    a.export_modules.mkdir(parents=True,exist_ok=True)
    for name,text in derived.items():
        (dest/'scripts'/name).write_text(text);(a.export_modules/name).write_text(text)
    if any((source/'scripts'/name).read_text()!=text for name,text in original.items()):
        raise AssertionError('Input source changed')
    record=dict(scope=__doc__,copy_from=str(source),source_topic=str(dest),
      original_sha256={k:sha(v) for k,v in original.items()},derived_sha256={k:sha(v) for k,v in derived.items()},
      canonical_unchanged=True,sparse_global_solve_unchanged=True,
      installer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    a.manifest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))


if __name__=='__main__':main()
