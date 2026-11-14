#!/usr/bin/env python3
"""Select actual old columns199..202 byte-for-byte; no Bockstein is recomputed."""
import argparse,gzip,hashlib,json,struct,time
from pathlib import Path

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def read(f,n):
 b=f.read(n)
 if len(b)!=n:raise ValueError('truncated actual source file')
 return b
def uint(f,n):return int.from_bytes(read(f,n),'little')
def selected_nf(path,indices):
 b=path.read_bytes()
 if b[:8]!=b'R150NF31':raise ValueError('actual NF magic')
 ns,nt,q=struct.unpack_from('<3I',b,8)
 if ns or q!=1034:raise ValueError('actual RHS NF dimensions')
 o=20;records=[]
 for i in range(nt):
  start=o;raw,label,n=struct.unpack_from('<IHI',b,o);o+=10
  if raw:raise ValueError('actual original RHS record')
  for _ in range(n):_,length=struct.unpack_from('<HB',b,o);o+=3+length
  if i in indices:records.append((label,b[start:o]))
 if o!=len(b) or len(records)!=len(indices):raise ValueError('complete actual NF selection')
 return records
def selected_trace(path,indices):
 records=[]
 with path.open('rb') as f:
  if read(f,8)!=b'R150NR31':raise ValueError('actual trace magic')
  nt=uint(f,4)
  for i in range(nt):
   header=read(f,10);raw,label,n=struct.unpack('<IHI',header)
   if raw:raise ValueError('actual RHS trace raw row')
   if i in indices:records.append((label,header+read(f,4*n)))
   else:f.seek(4*n,1)
  if f.read(1) or len(records)!=len(indices):raise ValueError('complete actual trace selection')
 return records
def main():
 p=argparse.ArgumentParser()
 for k in ('old-recovery','last-two-recovery','out'):p.add_argument('--'+k,type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 paths={}
 for name,root in [('old',a.old_recovery),('last',a.last_two_recovery)]:
  for kind,rel in [('kernels','original/kernel-original-kernels.bin'),('nf','normal/beta-normal-forms.bin'),('trace','normal/beta-reduction.bin'),('q','image/image-image-quotients.bin'),('rem','image/image-image-remainders.bin')]:paths[name+'-'+kind]=root/rel
 bindings={k:{'path':str(v),'bytes':v.stat().st_size,'sha256':sha(v)} for k,v in paths.items()}
 expected={
  'old-kernels':'ec067d86ce7c838697369d1f6a986c823de8564823d85b6684fe7a2926127a88',
  'old-nf':'c1b0e2e79a52e312acb9a9b89a03c031a5d6bbd5afc34c862ff7c2ff35479b2b',
  'old-trace':'85105ff9a84a81c05b88ee09d1f3a8de4bd9a1e7faf5657889c74e95f4f441ae',
  'old-q':'0bd81e4ae045daef1e224922ff0cceabd81436dc1680af29595ba2e169865338',
  'old-rem':'1f33a90bb81566e900dd2fc56d5cba50a853d73e3f927b288c0e19936b29d9de',
  'last-rem':'eef83657cdfb946f85e617d73b441719f8c24fcc3aebb4a6c799344a1fe17199'}
 for k,v in expected.items():
  if bindings[k]['sha256']!=v:raise ValueError('frozen input SHA '+k)
 labels=[2275,2276,2277,2278]
 for kind in ('nf','rem'):
  records=selected_nf(paths['old-'+kind],{198,199})+selected_nf(paths['last-'+kind],{0,1})
  if [r[0] for r in records]!=labels:raise ValueError('actual four NF labels')
  (a.out/('four-beta-'+kind+'.bin')).write_bytes(b'R150NF31'+struct.pack('<3I',0,4,1034)+b''.join(r[1] for r in records))
 records=selected_trace(paths['old-trace'],{198,199})+selected_trace(paths['last-trace'],{0,1})
 if [r[0] for r in records]!=labels:raise ValueError('actual four trace labels')
 (a.out/'four-beta-trace.bin').write_bytes(b'R150NR31'+struct.pack('<I',4)+b''.join(r[1] for r in records))
 with paths['old-q'].open('rb') as old,paths['last-q'].open('rb') as last,(a.out/'four-beta-quotients.bin').open('wb') as out:
  for f,nt,B in [(old,200,85),(last,2,86)]:
   if read(f,8)!=b'R150IQ31' or struct.unpack('<4I',read(f,16))!=(1034,1021,nt,B):raise ValueError('actual complete image Q')
  out.write(b'R150IQ31'+struct.pack('<4I',1034,1021,4,86))
  for _ in range(1021):
   header=read(old,4);rh=read(last,4)
   if header!=rh:raise ValueError('same actual monic G dictionary')
   polys=[]
   for i in range(200):
    n=uint(old,2);b=read(old,n)
    if i>=198:polys.append(struct.pack('<H',n)+b)
   for _ in range(2):n=uint(last,2);polys.append(struct.pack('<H',n)+read(last,n))
   out.write(header+b''.join(polys))
  if old.read(1) or last.read(1):raise ValueError('actual complete Q tail')
 with paths['old-kernels'].open('rb') as old,paths['last-kernels'].open('rb') as last,(a.out/'four-original-kernels.bin').open('wb') as out:
  kernel_labels=[]
  for f,nt,B in [(old,200,85),(last,2,86)]:
   if read(f,8)!=b'R150KK31' or struct.unpack('<4I',read(f,16))!=(31,6188,nt,B):raise ValueError('actual original kernel dimensions')
   for i in range(nt):
    desc=list(struct.unpack('<IHHII',read(f,16)))
    if nt==2 or i>=198:kernel_labels.append(desc)
  if kernel_labels!=[[2192,2275,85,1241,3485],[2193,2276,85,1242,3497],[2194,2277,86,1243,3498],[2195,2278,86,1244,3499]]:raise ValueError('actual four original kernel mapping')
  out.write(b'R150PS31'+struct.pack('<5I',31,31,6188,4,86)+struct.pack('<4H',*labels))
  for r in range(1,6189):
   h=read(old,15)
   if h!=read(last,15) or struct.unpack_from('<I',h)[0]!=r:raise ValueError('same full6188 original row map')
   polys=[]
   for i in range(200):
    n=uint(old,2);v=read(old,n)
    if i>=198:polys.append(v)
   for _ in range(2):n=uint(last,2);polys.append(read(last,n))
   out.write(h)
   for v in polys:
    if any(x>30 for x in v) or (v and not v[-1]):raise ValueError('canonical original kernel polynomial')
    out.write(struct.pack('<H',len(v))+b''.join(struct.pack('<H',x) for x in v))
  if old.read(1) or last.read(1):raise ValueError('complete original kernel tail')
 files={}
 for f in sorted(a.out.glob('*.bin')):
  b=f.read_bytes();z=f.with_suffix(f.suffix+'.gz');z.write_bytes(gzip.compress(b,mtime=0))
  if z.stat().st_size>5_000_000:raise ValueError('selected input requires persistent sharding')
  files[f.name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'gzip':z.name,'gzipBytes':z.stat().st_size,'gzipSHA256':sha(z)};f.unlink()
 receipt={'format':'r150-four-second-bockstein-input-byte-selection-v1','status':'completed','sourceSHA256':sha(Path(__file__)),'inputSources':bindings,'selectedHighKernelNumbers':[199,200,201,202],'actualKernelLabels':kernel_labels,'outputs':files,'originalKernelArithmeticRecomputed':False,'oldBocksteinRecomputed':False,'integerCoefficientValuesChanged':False,'F31KernelBytesWidenedToU16':True,'elapsedSeconds':time.monotonic()-start}
 (a.out/'selection-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
