#!/usr/bin/env python3
"""Test one paid common denominator on the actual p184 original source.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only exact original integer products can certify additional rational kernels.
"""
import argparse,gzip,hashlib,itertools,json,math,pathlib,resource,struct,sys,time,traceback
sys.dont_write_bytecode=True
def sha(x):return hashlib.sha256(x).hexdigest()
def checked(p,n,h):
 b=p.read_bytes()
 if len(b)!=n or sha(b)!=h:raise ValueError("bytes/hash mismatch "+str(p))
 return b
def jsave(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--dixon-dir",required=True,type=pathlib.Path)
 ap.add_argument("--point-model",required=True,type=pathlib.Path);ap.add_argument("--out",required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=512)
 args=ap.parse_args()
 if not(0<args.seconds<=30 and 0<args.memory_mib<=512):raise ValueError("authorized30s/512MiB bound")
 resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024*1024,)*2)
 out=args.out.resolve()
 if out.exists() and any(out.iterdir()):raise ValueError("new result directory required")
 out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 receipt={"format":"isp-selected-infinity-known-denominator-reconstruction-v1","status":"running",
   "secondsLimit":args.seconds,"memoryMiB":args.memory_mib,"actualSourceExponent":184,"newDixonDigitsComputed":0,"attempts":[]}
 certs=[];rp=out/"known-denominator-exact-kernels-receipt.json"
 try:
  def left():
   if time.monotonic()-start>args.seconds:raise TimeoutError("shared30 second mathematics")
  cb=checked(args.dixon_dir/"exact-rational-kernel-certificates.json.gz",690600,"fbd6089ccf043af574e5c6c58c654e259732782c4a36d40af0ba8a7352078758")
  cr=gzip.decompress(cb)
  if len(cr)!=2367435 or sha(cr)!="2b2b14d844ed6fb6ef1edaea1a84509ef717e93cdd94d51fe4db1b15d911c1a0":raise ValueError("paid13 exact certificate")
  paid=json.loads(cr)
  if paid["kernelCount"]!=13 or not paid["allFreeSourceCoordinatesIdentity"]:raise ValueError("paid13 shape")
  known={c["slot"]:c for c in paid["certificates"]};certs=list(paid["certificates"])
  if len(known)!=13 or any(not c["all4354SelectedExactIntegerProductsZero"] or not c["all4367ExactIntegerProductsZero"] for c in certs):
   raise ValueError("paid13 exact original product scope")
  parts=[("stage-p256/actual-p184-exact-source36.bin.gz.part000",4500000,"943560fdc543450450a51fccbda30a02bf5396e8635ae143e98fcb47bbcf3078"),
      ("stage-p256/actual-p184-exact-source36.bin.gz.part001",4223275,"2cd61573a08d40a66f7228ce17bd23e64f90ac89e7f9e21f409c8eca5f4e0b17")]
  packed=b"".join(checked(args.dixon_dir/n,s,h) for n,s,h in parts)
  if sha(packed)!="fdb0390d2b59f516d75a61f66599c0dc3b60eecbb2f80f556043e9e5c6f846e7":raise ValueError("whole paid p184 gzip")
  raw=gzip.decompress(packed)
  if len(raw)!=9234336 or sha(raw)!="9a000acba358eb042289eb1a63145f205e4049e1d2120100d27416e459030b48":raise ValueError("whole paid p184 original source")
  if raw[:8]!=b"R150BK31" or struct.unpack_from("<IIII",raw,8)!=(31,184,6188,36):raise ValueError("source shape")
  sourcebinding=raw[24:88].decode();pos=88;vals=[]
  for i in range(6188*36):
   sign=raw[pos];n=int.from_bytes(raw[pos+1:pos+3],"little");pos+=3
   if sign>1 or n>4096 or pos+n>len(raw) or (n and not raw[pos+n-1]) or (not n and sign):raise ValueError("source integer")
   a=int.from_bytes(raw[pos:pos+n],"little");pos+=n;vals.append(-a if sign else a)
  if pos!=len(raw):raise ValueError("source tail")
  pb=checked(args.point_model,87459,"97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074")
  point=json.loads(pb);equations=[list(map(int,row)) for row in point["primitivePointCoefficients"]]
  if len(equations)!=17 or any(len(row)!=77 for row in equations) or not point["characteristicZeroSameOriginal17Verified"]:
   raise ValueError("same original primitive17 infinity model")
  D=math.lcm(*(int(c["commonDenominator"]) for c in certs));M=31**184
  if D.bit_length()!=438 or math.gcd(D,31)!=1 or D>=M//2:raise ValueError("actual paid common denominator")
  free=paid["normalizedFreeOriginalSourceRows"];chosen=set(paid["all4354SelectedOutputIndicesZeroBased"])
  if len(free)!=36 or len(chosen)!=4354:raise ValueError("same selected dictionaries")
  for slot,c in known.items():
   den=int(c["commonDenominator"])
   if D%den or len(c["originalIntegerSourceNumerators"])!=6188:raise ValueError("paid denominator/source")
   for r,n in enumerate(c["originalIntegerSourceNumerators"]):
    if (int(n)-vals[r*36+slot]*den)%M:raise ValueError("paid exact kernel does not match same p184 source")
  receipt.update({"commonDenominator":str(D),"commonDenominatorBits":438,"sourceBinding":sourcebinding,
      "paid13ActualSourceResiduesVerified":True,"allChosenOutputIndicesZeroBased":sorted(chosen),"normalizedFreeOriginalSourceRows":free,
      "sourceRawSHA256":sha(raw),"sourceRawBytes":len(raw),"sourceSHA256":sha(pathlib.Path(__file__).read_bytes())})
  var=[8**i for i in range(11)]
  keys=[sum(var[i] for i in ix) for d in range(5,0,-1) for ix in itertools.combinations_with_replacement(range(11),d)]
  index={k:i for i,k in enumerate(keys)}
  multipliers=[sum(var[i] for i in ix) for d in range(4) for ix in itertools.combinations_with_replacement(range(11),d)]
  terms=var+[var[i]+var[j] for i in range(11) for j in range(i,11)]
  rowterms=[[(index[mul+terms[j]],v) for j,v in enumerate(equations[e]) if v] for mul in multipliers for e in range(17)]
  for slot in range(36):
   if slot in known:continue
   left();nums=[]
   for r in range(6188):
    x=(D*vals[r*36+slot])%M
    if x>M//2:x-=M
    nums.append(x)
   if any(nums[r-1]!=(D if j==slot else 0) for j,r in enumerate(free)):raise ValueError("candidate free coordinates")
   product=[0]*4367
   for r,a in enumerate(nums):
    if a:
     for c,v in rowterms[r]:product[c]+=a*v
    if r%500==0:left()
   bad_selected=[c for c in sorted(chosen) if product[c]]
   nonzero=[c for c,v in enumerate(product) if v]
   a={"slot":slot,"freeOriginalSource":free[slot],"selectedOriginalExactProductZero":not bad_selected,
       "full4367OriginalExactProductZero":not nonzero,"nonzeroSelectedOutputCount":len(bad_selected),"nonzeroFullOutputCount":len(nonzero),
       "maximumNumeratorBits":max(abs(v).bit_length() for v in nums)}
   if nonzero:a["firstExactResidual"]={"originalOutputIndexZeroBased":nonzero[0],"value":str(product[nonzero[0]])}
   if bad_selected:a["firstSelectedExactResidual"]={"originalOutputIndexZeroBased":bad_selected[0],"value":str(product[bad_selected[0]])}
   receipt["attempts"].append(a)
   if not bad_selected:
    cert={"slot":slot,"firstSuccessfulExponent":184,"method":"paid-common-denominator-centered-source",
       "freeOriginalSource":free[slot],"commonDenominator":str(D),"originalIntegerSourceNumerators":list(map(str,nums)),
       "all4354SelectedExactIntegerProductsZero":True,"all4367ExactIntegerProductsZero":not nonzero,
       "outsideSelected13ExactProducts":[{"originalOutputIndexZeroBased":c,"value":str(product[c])} for c in nonzero]}
    certs.append(cert)
  total=len(certs);full=sum(c["all4367ExactIntegerProductsZero"] for c in certs)
  receipt.update({"status":"completed","newExactKernelCount":total-13,"totalExactKernelCount":total,"totalFull4367ExactKernelCount":full,
    "characteristicZeroSelectedRankBounds":[4318,min(4340,4354-total)],
    "characteristicZeroSelectedColumnsFull4367RankBounds":[4318,min(4340,4354-full)],
    "all36TrueRationalKernelsVerified":total==36,"all36Full4367TrueRationalKernelsVerified":full==36,
    "mathematicalElapsedSeconds":time.monotonic()-start})
 except Exception as e:
  receipt["status"]="failed-or-incomplete";receipt["error"]=str(e);receipt["mathematicalElapsedSeconds"]=time.monotonic()-start
  (out/"exception.log").write_text(traceback.format_exc())
 finally:
  if certs:
   jsave(out/"combined-exact-rational-kernels.json",{"format":"isp-selected-infinity-exact-rational-kernel36-v1",
       "kernelCount":len(certs),"allFreeSourceCoordinatesIdentity":True,"normalizedFreeOriginalSourceRows":paid["normalizedFreeOriginalSourceRows"],
       "all4354SelectedOutputIndicesZeroBased":paid["all4354SelectedOutputIndicesZeroBased"],"certificates":certs})
  files=[]
  for p in sorted(out.iterdir()):
   if not p.is_file() or p==rp:continue
   b=p.read_bytes();e={"file":p.name,"bytes":len(b),"sha256":sha(b)}
   if len(b)>1_000_000:
    g=gzip.compress(b,compresslevel=1,mtime=0);parts=[]
    for j,startp in enumerate(range(0,len(g),4_500_000)):
     z=g[startp:startp+4_500_000];q=p.with_name(p.name+(".gz" if len(g)<=4_500_000 else ".gz.part%03d"%j));q.write_bytes(z)
     parts.append({"file":q.name,"bytes":len(z),"sha256":sha(z)})
    e.update({"gzipBytes":len(g),"gzipSHA256":sha(g),"parts":parts});p.unlink()
   else:e["storedFile"]=p.name
   files.append(e)
  receipt["files"]=files;jsave(rp,receipt)
 print(json.dumps({k:receipt.get(k) for k in ["status","newExactKernelCount","totalExactKernelCount","totalFull4367ExactKernelCount",
     "characteristicZeroSelectedRankBounds","mathematicalElapsedSeconds"]}),flush=True)
 return 0 if receipt["status"]=="completed" else 1
if __name__=="__main__":sys.exit(main())
