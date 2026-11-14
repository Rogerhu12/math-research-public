#!/usr/bin/env python3
"""Losslessly select the two already-computed cost85 source columns/traces.

This changes storage only: no Bockstein, NF or source mathematics is repeated.
The whole original files are SHA-bound and every raw-row mapping is retained.
"""
import argparse,gzip,hashlib,json,struct,time
from pathlib import Path

KERNEL_SHA='ec067d86ce7c838697369d1f6a986c823de8564823d85b6684fe7a2926127a88'
TRACE_SHA='85105ff9a84a81c05b88ee09d1f3a8de4bd9a1e7faf5657889c74e95f4f441ae'
LABELS=[[2192,2275,85,1241,3485],[2193,2276,85,1242,3497]]

def main():
 p=argparse.ArgumentParser()
 for k in ('kernels','trace','out'):p.add_argument('--'+k,type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 data=a.kernels.read_bytes()
 if hashlib.sha256(data).hexdigest()!=KERNEL_SHA:raise ValueError('complete original200 kernel checksum')
 if data[:8]!=b'R150KK31' or struct.unpack_from('<4I',data,8)!=(31,6188,200,85):raise ValueError('original kernel dimensions')
 labels=[list(struct.unpack_from('<IHHII',data,24+16*i)) for i in range(200)]
 if labels[-2:]!=LABELS:raise ValueError('actual original cost85 labels')
 out=bytearray(b'R150KK31')+struct.pack('<4I',31,6188,2,85)+data[24+198*16:24+200*16]
 offset=24+200*16
 for raw in range(1,6189):
  if struct.unpack_from('<I',data,offset)[0]!=raw:raise ValueError('complete original raw row dictionary')
  out.extend(data[offset:offset+15]);offset+=15
  for i in range(200):
   length=struct.unpack_from('<H',data,offset)[0];finish=offset+2+length
   if finish>len(data):raise ValueError('truncated actual source polynomial')
   if i>=198:out.extend(data[offset:finish])
   offset=finish
 if offset!=len(data):raise ValueError('trailing complete original kernel file')
 files=[]
 def save(name,plain):
  f=a.out/(name+'.gz');f.write_bytes(gzip.compress(plain,mtime=0))
  files.append({'file':f.name,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'uncompressedBytes':len(plain),'uncompressedSHA256':hashlib.sha256(plain).hexdigest()})
 save('cost85-selected-original-kernels.bin',out)
 del data,out
 data=a.trace.read_bytes()
 if hashlib.sha256(data).hexdigest()!=TRACE_SHA:raise ValueError('whole original200 normal trace checksum')
 if data[:8]!=b'R150NR31' or struct.unpack_from('<I',data,8)[0]!=200:raise ValueError('original200 trace dimensions')
 out=bytearray(b'R150NR31')+struct.pack('<I',2);offset=12;selected_steps=[]
 for i in range(200):
  raw,target,n=struct.unpack_from('<IHI',data,offset);finish=offset+10+4*n
  if raw or target!=labels[i][1] or finish>len(data):raise ValueError('actual original trace source dictionary')
  if i>=198:out.extend(data[offset:finish]);selected_steps.append(n)
  offset=finish
 if offset!=len(data):raise ValueError('trailing original200 trace file')
 save('cost85-selected-normal-reduction.bin',out)
 receipt={'format':'r150-h25-lossless-selected-inputs-v1','status':'completed-storage-selection-only','sourceSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'originalKernelSHA256':KERNEL_SHA,'originalNormalTraceSHA256':TRACE_SHA,'originalColumns':200,'selectedColumns':2,'selectedLabels':LABELS,'allOriginalRawRowsRetained':6188,'selectedTraceStepCounts':selected_steps,'mathematicalNFOrBocksteinRecomputed':False,'files':files,'elapsedSeconds':time.monotonic()-start}
 (a.out/'selected-inputs-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps(receipt),flush=True)

if __name__=='__main__':main()
