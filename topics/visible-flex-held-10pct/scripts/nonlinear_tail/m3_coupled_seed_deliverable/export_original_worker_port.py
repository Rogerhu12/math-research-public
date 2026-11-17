#!/usr/bin/env python3
"""Read a literal physical m3 port from the original actual worker startup."""
from pathlib import Path
import argparse,hashlib,importlib.util,json

def main():
 p=argparse.ArgumentParser();p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--config',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 source=a.source_topic.resolve();path=source/'scripts/950f-tail-client-v3.py';spec=importlib.util.spec_from_file_location('m3_original_client',path);client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
 cfg=json.loads(a.config.read_text());a.out.parent.mkdir(parents=True,exist_ok=True);tail=client.WeightedTailPort(a.config,source/'repro/source-root',a.out.with_suffix('.unused'),node_heap=2048)
 try:
  keys=['rCut','wCut','width','curvatureBound','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','slopeCap','capTransition','calibrationSteps','warpSteps','cuspAwareQuadrature','quadratureTolerance','capMode','valleyControls','pulseCaps','valleyCaps','maxCachedBetas','warpWeightLevels','spacing']
  parameters={k:cfg[k]for k in keys if k in cfg};cut={k:tail.ready['cut'][k]for k in ['radius','backgroundSlope','backgroundSecond','E','Ep']}
  out=dict(scope=__doc__,parameters=parameters,cut=cut,modes=[cfg['spacing']*(j+1)for j in range(tail.M)],linearSlope=tail.ready['linearSlope'],source=dict(client_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),config_sha256=hashlib.sha256(a.config.read_bytes()).hexdigest(),source_sha256=tail.sources),claim='Actual linear finite port only. No nonlinear or closed-surface conclusion.')
  a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(out=str(a.out),D_first4=out['linearSlope'][:4],cut=cut,sha256=hashlib.sha256(a.out.read_bytes()).hexdigest())),flush=True)
 finally:tail.close()
if __name__=='__main__':main()
