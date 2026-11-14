"""Recorded actual finite nonlinear DN on the optimized physical metric.
The complete state is retained for each fresh successful response. The finite
far Robin condition is not an exact round collar or a closed-surface proof.
"""
import gzip,hashlib,json,os,subprocess
from pathlib import Path
import numpy as np
from f6curve_compact_tail_port import CompactTailPort as OriginalPort

class OptimizedTailPort(OriginalPort):
    def __init__(self,config,source_root,record_prefix):
        self.config=str(config);self.calls=0;self.cache_key=self.cache_value=None
        self.record_prefix=Path(record_prefix)
        if any(self.record_prefix.parent.glob(self.record_prefix.name+'_????.json.gz')):
            raise FileExistsError('Recording prefix already used')
        cfg=json.loads(Path(config).read_text());N=int(cfg.get('quadrature',128))
        if N<=0 or N&(N-1):raise ValueError('Quadrature must be a positive power of two')
        worker=Path(__file__).with_suffix('.mjs');env=dict(os.environ,VISIBLE_FLEX_SOURCE_ROOT=str(source_root))
        self.proc=subprocess.Popen(['node',str(worker),str(config)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1,env=env)
        line=self.proc.stdout.readline()
        if not line:raise RuntimeError('Actual optimized tail initialization failed')
        self.ready=json.loads(line);self.cut=self.ready['cut'];self.linearD=np.asarray(self.ready['linearSlope']);self.M=len(self.linearD)
        self.sources={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in [Path(__file__),worker,Path(__file__).with_name('closing_recalibrated_tail.mjs')]}
    def solve(self,height,jacobian=True,audit=False):
        before=self.calls;out=super().solve(height,jacobian=jacobian,audit=audit)
        if self.calls!=before:
            target=self.record_prefix.with_name(self.record_prefix.name+f'_{self.calls:04d}.json.gz')
            record=dict(out,recorded_audit=bool(audit),source_sha256=self.sources,
                scope='Actual finite Fourier/depth nonlinear DN state. Far Robin truncation is not an exact circle. No closed-surface claim.')
            raw=gzip.compress((json.dumps(record,separators=(',',':'))+'\n').encode(),mtime=0)
            if len(raw)>=5_000_000:raise RuntimeError('Repository per-file limit exceeded')
            with target.open('xb') as f:f.write(raw)
        return out
