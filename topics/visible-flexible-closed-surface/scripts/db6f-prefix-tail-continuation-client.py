"""Persistent actual weighted-tail DN client, with complete recorded responses.

The underlying spatial/temporal discretization is explicit in config. Success
of this finite DN solve is not a certificate for an infinite closed surface.
"""
import gzip, hashlib, json, os, subprocess
from pathlib import Path
import numpy as np

class WeightedTailPort:
    def __init__(self, config, source_root, record_prefix, node_heap=1536):
        self.config=Path(config);self.record_prefix=Path(record_prefix)
        if any(self.record_prefix.parent.glob(self.record_prefix.name+'_????.json.gz')):
            raise FileExistsError('Record prefix already used')
        worker=Path(__file__).with_name('db6f-prefix-tail-trial-worker.mjs')
        source_root=Path(source_root)
        env=dict(os.environ,VISIBLE_FLEX_SOURCE_ROOT=str(source_root),
                 CLOSING_TAIL_CACHE=str(source_root/'topics/large-amplitude-twist-flex/scripts'),
                 NODE_OPTIONS=f'--max-old-space-size={node_heap}')
        self.proc=subprocess.Popen(['node',str(worker),str(self.config)],stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,text=True,bufsize=1,env=env)
        self.calls=0;self.cache_key=None;self.cache_value=None
        line=self.proc.stdout.readline()
        if not line: raise RuntimeError('Weighted stage-tail initialization failed')
        self.ready=json.loads(line);self.cut=self.ready['cut'];self.linearD=np.asarray(self.ready['linearSlope']);self.M=len(self.linearD)
        names=['db6f-prefix-tail-continuation-client.py','db6f-prefix-tail-trial-worker.mjs','db6f-prefix-tail-trial-core.mjs',
               'db6f-prefix-tail-trial-split.mjs','950f-tail-subdivision.mjs','950f-tail-warm-remesh.mjs',
               'closing_weighted_tail.mjs','closing_recalibrated_tail.mjs']
        self.sources={name:hashlib.sha256(worker.with_name(name).read_bytes()).hexdigest() for name in names}
    def solve(self,height,jacobian=True,audit=False):
        h=np.asarray(height,float)
        if h.shape!=(self.M,) or not np.all(np.isfinite(h)):raise ValueError('Physical height vector has wrong shape or nonfinite values')
        if self.cache_key is not None and np.array_equal(h,self.cache_key) and not audit and (not jacobian or self.cache_value.get('heightJetJacobian') is not None):
            return self.cache_value
        self.calls+=1;request=dict(height=h.tolist(),jacobian=bool(jacobian),audit=bool(audit))
        self.proc.stdin.write(json.dumps(request)+'\n');self.proc.stdin.flush()
        line=self.proc.stdout.readline()
        if not line:raise RuntimeError('Weighted tail worker stopped')
        response=json.loads(line)
        record=dict(request=request,response=response,config=json.loads(self.config.read_text()),source_sha256=self.sources)
        data=gzip.compress((json.dumps(record,separators=(',',':'))+'\n').encode(),mtime=0)
        if len(data)>=5_000_000:raise RuntimeError('Record exceeds repository per-file size limit')
        file=self.record_prefix.with_name(self.record_prefix.name+f'_{self.calls:04d}.json.gz')
        # Publish a complete response atomically, without replacing an old one.
        tmp=file.with_name(file.name+'.tmp')
        with tmp.open('xb') as f:
            f.write(data);f.flush();os.fsync(f.fileno())
        try:os.link(tmp,file)
        finally:tmp.unlink()
        if response.get('failed') or not response.get('converged'):
            raise FloatingPointError('Weighted finite DN trial failed '+str({k:response.get(k) for k in ('failed','residual','lastIteration')}))
        self.cache_key=h.copy();self.cache_value=response
        return response
    def close(self):
        if self.proc.poll() is None:
            try:
                self.proc.stdin.write('{"stop":true}\n');self.proc.stdin.flush();self.proc.stdin.close()
                self.proc.wait(timeout=15)
            except Exception:self.proc.terminate()
