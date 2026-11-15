#!/usr/bin/env python3
"""Expose the small actual toolchain receipt through retained session parameters."""
import argparse,hashlib,json,pathlib,time
p=argparse.ArgumentParser();p.add_argument("--source",required=True);p.add_argument("--out",required=True);a=p.parse_args()
t=time.monotonic();raw=pathlib.Path(a.source).read_bytes()
expected="80c654c4f68be1558b9a842c21099537c48964ce44ebebf5cb38e46c60dd57dd"
assert len(raw)==1691 and hashlib.sha256(raw).hexdigest()==expected,"same actual toolchain observation"
actual=json.loads(raw)
receipt={"format":"isp-native-exact-toolchain-retained-readback-v1","status":"completed","elapsedSeconds":time.monotonic()-t,"parameters":{"actualObservationBytes":len(raw),"actualObservationSHA256":expected,"actualToolchainObservation":actual,"onlySmallExistingReceiptRead":True,"nativeLibraryListMayHaveBeenTruncated":True},"largeDataUploadedOrCommitted":False}
out=pathlib.Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
print(json.dumps({"status":"completed","receipt":str(out)}))
