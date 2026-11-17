"""Restore three immutable reference files from the existing partial clone."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--manifest',type=Path,default=Path(__file__).with_name('reference_sources.json'))
    args=p.parse_args();manifest=json.loads(args.manifest.read_text())
    args.out.mkdir(parents=True,exist_ok=True)
    restored=[]
    for item in manifest['sources']:
        data=subprocess.run(['git','-C',str(args.repo),'show',item['commit']+':'+item['path']],check=True,stdout=subprocess.PIPE).stdout
        digest=hashlib.sha256(data).hexdigest()
        if digest!=item['sha256']:raise RuntimeError('Reference source hash mismatch: '+item['path'])
        target=args.out/item['local_name'];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        restored.append(dict(local_name=item['local_name'],sha256=digest))
    print(json.dumps(dict(restored=restored)))


if __name__=='__main__':main()
