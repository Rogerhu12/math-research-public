#!/usr/bin/env python3
"""Read only the pinned 6043-byte full56 failed receipt, never its matrix state.
Author: Astra-ISP-789f / root. AI-assisted: GPT-6 Astra Pro.
"""
import argparse, hashlib, json, os, pathlib, resource, time
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--receipt',type=pathlib.Path,required=True)
    p.add_argument('--out',type=pathlib.Path,required=True)
    a=p.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,)*2)
    start=time.monotonic()
    b=a.receipt.read_bytes()
    digest=hashlib.sha256(b).hexdigest()
    if len(b)!=6043 or digest!='26917bb0ac3058ce08c57b18f91bca119b42ad866c4264e98ad9d4a02a7382cc':
        raise ValueError('Pinned actual failed receipt byte identity')
    v=json.loads(b)
    if v.get('status')!='failed' or not isinstance(v.get('error'),dict):
        raise ValueError('Actual structured failure required')
    if v.get('binding')!='862cca4d82af7c8031de01117b2f18516c0d3622a73b4e794c4f3280a0fe9850':
        raise ValueError('Pinned original full56 binding')
    out={'format':'r150-full56-small-error-inspection-v1','status':'completed',
         'parameters':{'receiptBytes':len(b),'receiptSHA256':digest,
                       'originalBinding':v['binding'],'originalError':v['error'],
                       'originalElapsedSeconds':v['elapsedSeconds'],
                       'lastWholeCheckpoint':v['parameters']['lastWholeCheckpoint'],
                       'largeCandidateStateRead':False,'newMatrixOperations':False},
         'elapsedSeconds':time.monotonic()-start}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    raw=json.dumps(out,sort_keys=True,indent=2).encode()+b'\n'
    tmp=a.out.with_name(a.out.name+'.partial')
    tmp.write_bytes(raw)
    os.replace(tmp,a.out)
    print(json.dumps(out,sort_keys=True),flush=True)
if __name__=='__main__':
    main()
