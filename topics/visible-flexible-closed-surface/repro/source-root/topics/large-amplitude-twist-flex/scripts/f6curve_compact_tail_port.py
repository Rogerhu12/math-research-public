"""Persistent true compact-tail nonlinear DN subprocess, finite M/depth only.
Astra curve_transition, AI-assisted 2026-11-08.
"""
import json,subprocess
from pathlib import Path
import numpy as np

class CompactTailPort:
    def __init__(self,config,linear_port=None):
        self.config=str(config);self.calls=0;self.cache_key=None;self.cache_value=None
        cfg=json.loads(Path(config).read_text());N=int(cfg.get('quadrature',128))
        if N<=0 or N&(N-1):raise ValueError('Compact tail full metric audit requires power-of-two quadrature; choose 256,512,... before solving')
        self.proc=subprocess.Popen(['node',str(Path(__file__).with_suffix('.mjs')),str(config)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
        line=self.proc.stdout.readline()
        if not line:raise RuntimeError('Compact tail initialization failed')
        self.ready=json.loads(line);self.cut=self.ready['cut'];self.linearD=np.asarray(self.ready['linearSlope']);self.M=len(self.linearD)
        if linear_port:
            d=json.loads(Path(linear_port).read_text());p=d['parameters']
            if abs(p['rCut']-self.cut['radius'])>1e-12 or abs(p['wCut']-self.cut['backgroundSlope'])>1e-12:raise ValueError('Linear reference and nonlinear cut geometries differ')
    def solve(self,height,jacobian=True,audit=False):
        h=np.asarray(height,float)
        if self.cache_key is not None and np.array_equal(h,self.cache_key) and not audit and (not jacobian or self.cache_value.get('heightJetJacobian') is not None):return self.cache_value
        self.calls+=1;self.proc.stdin.write(json.dumps(dict(height=h.tolist(),jacobian=jacobian,audit=audit))+'\n');self.proc.stdin.flush();line=self.proc.stdout.readline()
        if not line:raise RuntimeError('Compact tail subprocess stopped')
        out=json.loads(line)
        if out.get('failed') or not out.get('converged'):
            # Domain-aware Newton can reject this numerical tail branch trial.
            # This does not turn failure of one chart into a geometric claim.
            raise FloatingPointError('Compact tail trial failed '+str({k:v for k,v in out.items() if k not in ('heightJetJacobian','jets','audit')}))
        self.cache_key=h.copy();self.cache_value=out;return out
    def close(self):
        if self.proc.poll() is None:
            self.proc.stdin.write('{"stop":true}\n');self.proc.stdin.flush();self.proc.stdin.close()
            try:self.proc.wait(timeout=15)
            except subprocess.TimeoutExpired:self.proc.terminate();self.proc.wait(timeout=5)
