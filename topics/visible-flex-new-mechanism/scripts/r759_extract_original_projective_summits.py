"""Byte-only extraction from the immutable completed R745 journal, no ODE or interval evaluation."""
import hashlib
import json
import re
import zipfile
from pathlib import Path

ZIP_SHA='655bf0f756684dda5f257c4d468105767a8f9401bb23c373deac9c11090c9bdd'
DIRECT_SHA='b36cf17f8af6b3d6ea4affb8ef48c424ff77e382452e963ccae8a791b90a7b84'
LEDGER_SHA='572dad7b08b08849f37a16cb00f9e5ff78ec0e9543a4e6802ca235635fab733b'
FID='1b40bcf507d16497579ef47032968914ce787f6113899a185e60c050b42167cf'

def extract(path):
    path=Path(path)
    with path.open('rb') as f:
        if path.stat().st_size!=136888055 or hashlib.file_digest(f,'sha256').hexdigest()!=ZIP_SHA:raise ValueError('Wrong R745 archive.')
    with zipfile.ZipFile(path) as z:
        ledger=z.read('ledger.json')
        if hashlib.sha256(ledger).hexdigest()!=LEDGER_SHA or json.loads(ledger)['fingerprint']!=FID:raise ValueError('Wrong R745 ledger.')
        last=None;lines=[];selected=[];dig=hashlib.sha256();n=0
        def finish():
            # First chunk per side in the original depth-6 Poincare-Miranda scan.
            # Only the last row of every native material piece is needed downstream.
            if len(selected)>=2 or not any(q[1]==0 and q[2]==63 for q in lines):return
            rs=[dict(piece=p,key=k,cached_value=v) for k,p,i,v in lines if i==63]
            selected.append(dict(label=last,piece_endpoints=rs))
        with z.open('directed.jsonl') as stream:
            for row in stream:
                dig.update(row);n+=1
                if len(selected)>=2:continue
                item=json.loads(row);m=re.fullmatch(r'enc_([0-9a-f]{24})_p(\d+)_z(\d+)',item['key'])
                if not m:continue
                label=m[1]
                if item['fingerprint']!=FID:raise ValueError('Wrong unit origin.')
                if label!=last:
                    finish();lines=[];last=label
                lines.append((item['key'],int(m[2]),int(m[3]),item['value']))
            finish()
        if n!=242732 or dig.hexdigest()!=DIRECT_SHA or len(selected)!=2:raise ValueError('Incomplete original journal or coarse face.')
    return dict(origin=dict(archive_sha256=ZIP_SHA,directed_sha256=DIRECT_SHA,ledger_sha256=LEDGER_SHA,fingerprint=FID,directed_rows=n),original_blocks=selected)

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('zip');p.add_argument('output');q=p.parse_args()
    Path(q.output).write_bytes(json.dumps(extract(q.zip),sort_keys=True,separators=(',',':'),allow_nan=False).encode())
