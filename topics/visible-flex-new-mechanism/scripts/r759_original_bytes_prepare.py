"""Pure byte preparation of three immutable already-paid inputs, before science."""
import base64, hashlib, json, os, time
from pathlib import Path

def main():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public':
        raise RuntimeError('Public Actions only.')
    st=time.monotonic();topic=Path('topics/visible-flex-new-mechanism')
    out=Path(os.environ['RUNNER_TEMP'])/'r759-sources';out.mkdir(exist_ok=True)
    paid=Path(os.environ['RUNNER_TEMP'])/'r759-paid';paid.mkdir(exist_ok=True)
    port=json.loads((topic/'computations/r759-r738-actual-complete-cut-npz.json').read_bytes())
    objects=[('r745-final.json',(topic/'computations/r745-original-natural-terminal-20261128.json').read_bytes(),30183,'e9ec284cc041db1649576ad6ef8e0fe97247ac2717bc8b1a857658b54bb5b21b'),
       ('r745-depth6.json',(topic/'computations/r759-original-first-depth6-blocks.json').read_bytes(),93744,'d07dc6fc1972061c4cabe75a2da679b7b26d6f86d8bf65f8d39e02a2352292b9'),
       ('r738-complete.npz',base64.b64decode(port['base64'],validate=True),13093,'cc1826cc43e71c7575ba6a042dcfd06d0df7f1b40e2e17f7696d96f79e9bda20')]
    rows=[]
    for name,raw,length,digest in objects:
        if len(raw)!=length or hashlib.sha256(raw).hexdigest()!=digest:raise ValueError('Original paid bytes differ: '+name)
        path=out/name
        if path.exists() and path.read_bytes()!=raw:raise ValueError('Existing original input differs.')
        path.write_bytes(raw);rows.append(dict(name=name,bytes=length,sha256=digest))
    report=dict(original_inputs=rows,administrative_seconds=time.monotonic()-st,new_scientific_evaluations=0,old_log_requests=0)
    raw=json.dumps(report,sort_keys=True,separators=(',',':')).encode()
    (paid/'original-byte-transport.json').write_bytes(raw)
    print('R759_ORIGINAL_BYTES '+raw.decode(),flush=True)

if __name__=='__main__':main()
