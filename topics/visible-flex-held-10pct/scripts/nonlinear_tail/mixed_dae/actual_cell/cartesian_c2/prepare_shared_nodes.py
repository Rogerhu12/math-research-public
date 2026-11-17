"""Pack a completed actual-cell solution for independent original-engine jets."""
import argparse, gzip, hashlib, json
from pathlib import Path
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--solution', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    data = json.loads(gzip.decompress(a.input.read_bytes()))
    report = json.loads(a.solution.read_text())
    if not report['success'] or report['input']['sha256'] != sha(a.input):
        raise ValueError('A successful solution on this exact input is required')
    state = a.solution.with_suffix('.npz')
    z = np.load(state)
    if not np.array_equal(z['x'], np.array([n['x'] for n in data['nodes']])):
        raise ValueError('Solution and physical nodes differ')
    nodes = []
    for n, Y in zip(data['nodes'], z['Y']):
        nodes.append({k:n[k] for k in ('x','r','w','wr','local_parameter','stage','raw_segment')})
        nodes[-1]['Y'] = Y.tolist()
    out = dict(scope='Finite mixed solution nodes; no geometry claim.',
               parameters=data['parameters'], checkpoint_path=data['input'],
               checkpoint_sha256=data['checkpoint_sha256'],
               inputs={str(v):sha(v) for v in (a.input,a.solution,state)}, nodes=nodes)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0))
    print(json.dumps(dict(output=str(a.output),sha256=sha(a.output),nodes=len(nodes))))


if __name__ == '__main__':
    main()
