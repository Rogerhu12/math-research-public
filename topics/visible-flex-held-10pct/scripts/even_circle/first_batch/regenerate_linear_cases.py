#!/usr/bin/env python3
"""Portable path adapter for the frozen original seven-case linear screen."""
from pathlib import Path
import argparse,hashlib,json,sys
p=argparse.ArgumentParser();p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--runtime',type=Path,required=True);a=p.parse_args();here=Path(__file__).resolve().parent;original=here/'source/screen_linear_even.py';source=original.read_text()
expected='86527b39818a6ae45cbc224e4c0c39d2ed89caa75edbd2b30b8e25c68ce3b6fc'
if hashlib.sha256(source.encode()).hexdigest()!=expected:raise RuntimeError('Frozen original linear screen source changed')
old="b=Path('/workspace/scratch/f00f08c94d46');r=b/'even_plateau_work';source=b/'m3_flat17_work/recovered/bundle/topics/visible-flexible-closed-surface';comp=b/'m3_flat17_work/recovered/bundle/topics/visible-flex-larger-amplitude/computations'"
new='r=Path('+repr(str(a.runtime.resolve()))+');source=Path('+repr(str(a.source_topic.resolve()))+");comp=source.parent/'visible-flex-larger-amplitude/computations'"
if source.count(old)!=1:raise RuntimeError('Original path declaration was not found exactly once')
source=source.replace(old,new);a.runtime.mkdir(parents=True,exist_ok=True);sys.path.insert(0,str(here/'source'))
(a.runtime/'linear_portable_source_record.json').write_text(json.dumps(dict(original_source_sha256=expected,adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),only_change='Replace four absolute source/output path bindings; numerical source text otherwise unchanged',executed_transformed_sha256=hashlib.sha256(source.encode()).hexdigest()),indent=2)+'\n')
exec(compile(source,str(original),'exec'),dict(__name__='__main__',__file__=str(original)))
