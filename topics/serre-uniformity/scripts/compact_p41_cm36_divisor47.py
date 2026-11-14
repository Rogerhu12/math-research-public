#!/usr/bin/env python3
"""Retain final T3B and its actual functions; hash the reconstructible intermediate ideals."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,default=Path('/tmp/p41_cm36_divisor47_checkpoint.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_cm36_divisor47_compact.json.gz'))
    args=p.parse_args();raw=args.input.read_bytes();d=json.loads(gzip.decompress(raw))
    assert d['status'].startswith('actual40 CM36 points')
    for record in d['branches']:
        record.pop('point_coordinates');record.pop('point_frobenius')
    d.pop('negative_total_point_coordinates');d.pop('negative_total_point_frobenius')
    d['complete_reconstructible_checkpoint_sha256']=hashlib.sha256(raw).hexdigest()
    d['complete_reconstructible_checkpoint_bytes']=len(raw)
    d['compactor_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    d['storage_scope']='complete T3B point, both actual cubic numerators, fixed f0 and all input/check hashes; intermediate93-to73 kernels and negative total point are reconstructed by the generator'
    packed=gzip.compress((json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
    args.output.write_bytes(packed)
    print('ACTUAL T3B COMPACT SAVED',len(packed),hashlib.sha256(packed).hexdigest())


if __name__=='__main__':main()
