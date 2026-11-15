#!/usr/bin/env python3
"""Normalize only the six newly paid exact Koszul axes and compare all6188 p768 residues.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
All large outputs are temporary, with only small receipts/hashes retained.
"""
import argparse,gzip,hashlib,importlib.util,json,math,os,pathlib,resource,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
H_SHA="9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"
P_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
SOURCE_SHA="0ea5c472aa4013242357ae671b42226b217f61948ee741334eb8a1df0e5dbd07"
U_SHA="79ca0d75d213175b28ce10827cfcf90fef3bea29ef1a6f9c97692c679c569f77"
QBIND="10890e55000e9e0554b2488f333b899dbf224421e5bf091adc24d396348cc6a4"
SLOTS=[17,18,19,26,27,28]
def need(b,s):
 if not b:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   z=f.read(1048576)
   if not z:break
   n+=len(z);h.update(z)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open()) as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp")
 with (gzip.open(q,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else q.open("w")) as f:json.dump(x,f,separators=(",",":"))
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def vecsha(v):
 h=hashlib.sha256()
 for x in v:h.update((str(x)+"\n").encode())
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["helper","source","source-receipt","point-model","prepared-dir","exact-dir","normalizer","out"]:ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args();need(0<a.seconds<=60 and 0<a.memory_mib<=1024,"one60s <=1024MiB budget")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-2;out=a.out.resolve()
 need(not out.exists() or not any(out.iterdir()),"fresh directory");out.mkdir(parents=True,exist_ok=True)
 r={"format":"isp-six-new-exact-koszul-normalized-source-p768-v1","status":"running","parameters":{},"largeDataUploadedOrCommitted":False,"newDixonDigitsComputed":0,"oldNormalFormsRecomputed":False,"completedSlots":[]}
 files=[];records=[];code=1
 def check():
  if time.monotonic()>=deadline:raise TimeoutError("shared60-second budget")
 def checkpoint():
  r["parameters"]["temporaryFiles"]=files;r["parameters"]["normalizedColumns"]=records
  r["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"six-normalized-koszul-p768-receipt.json",r)
 try:
  need(sha(a.helper)["sha256"]==H_SHA and sha(a.point_model)["sha256"]==P_SHA,"paid helper and original point")
  need(sha(a.normalizer)=={"bytes":70882,"sha256":U_SHA},"paid exact normalizer bytes")
  sp=importlib.util.spec_from_file_location("paid_helper",a.helper);H=importlib.util.module_from_spec(sp);sp.loader.exec_module(H)
  point=read(a.point_model);u=read(a.normalizer)
  need(u["binding"]==QBIND and (u["rows"],u["columns"])==(29,29),"actual29 normalizer")
  qr=read(a.exact_dir/"koszul-exact-rational-support-receipt.json")
  need(qr["status"]=="completed" and qr["allOriginal4367IntegerProductsZero"] is True and qr["parameters"]["binding"]==QBIND,"all29 paid products")
  pm=a.prepared_dir/"exact-original-koszul-outside-model.json.gz"
  need(sha(pm)==qr["parameters"]["inputIdentity"]["original"],"same original dictionary file")
  model=read(pm);free=list(map(int,model["freeRows"]));selected=set(map(int,model["selectedRows"]));outside=list(map(int,model["outsideRows"]))
  need(len(free)==36 and len(selected)==4354 and len(outside)==1834,"complete dictionaries")
  declared={x["file"]:x for x in qr["parameters"]["temporaryFiles"]}
  weights=[];denoms=[]
  for slot in SLOTS:
   cc=[tuple(map(int,u["rationalPairsByRows"][i][slot])) for i in range(29)];D=1
   for n,d in cc:need(d>0 and d%31!=0,"normalizer31 unit denominator");D=math.lcm(D,d)
   weights.append([n*(D//d) for n,d in cc]);denoms.append(D)
  accum=[[0]*6188 for _ in SLOTS]
  for i in range(29):
   check();p=a.exact_dir/("exact-selected-koszul-kernel-%03d.json.gz"%i)
   ident=sha(p);expected=declared[p.name];need(ident["bytes"]==expected["bytes"] and ident["sha256"]==expected["sha256"],"actual full kernel bytes")
   cert=read(p);need(cert["binding"]==QBIND and cert["all1834OutsideSourceCoefficientsZero"] and cert["all4367ExactIntegerProductsZero"],"paid full source kernel")
   nums=[int(x) for x in cert["original6188IntegerCoefficients"]];need(len(nums)==6188,"all original source entries")
   for j in range(6):
    w=weights[j][i]
    if w:
     for row,x in enumerate(nums):
      if x:accum[j][row]+=w*x
  # Save all six exact source arrays before complete p768/original-product checks.
  for j,slot in enumerate(SLOTS):
   g=denoms[j]
   for x in accum[j]:g=math.gcd(g,abs(x))
   denoms[j]//=g;accum[j]=[x//g for x in accum[j]]
   need(denoms[j]>0 and denoms[j]%31!=0,"primitive31-unit rational denominator")
   files.append(save(out/("normalized-six-slot%02d-unverified.json.gz"%slot),{"binding":QBIND,"slot":slot,"denominator":str(denoms[j]),"original6188Numerators":[str(x) for x in accum[j]],"verificationPending":True}))
  checkpoint();check()
  native=read(a.source_receipt)
  exponent,binding,values=H.read_source(a.source,36433748,SOURCE_SHA,native,check)
  need(exponent==768,"same actual p768 source")
  modulus=31**768;balanced=math.isqrt(modulus//2);terms=H.original_row_terms(point)
  r["parameters"].update({"codeSHA256":sha(__file__)["sha256"],"normalizerSHA256":U_SHA,"paidKernelBinding":QBIND,
      "sourceSHA256":SOURCE_SHA,"sourceBytes":36433748,"nativeSourceBinding":binding,
      "slots":SLOTS,"residueCoordinateCountPerSlot":6188,"modulusExponent":768})
  for j,slot in enumerate(SLOTS):
   check();nums=accum[j];D=denoms[j]
   need(all(nums[raw-1]==(D if k==slot else 0) for k,raw in enumerate(free)),"all36 exact free normalized coordinates")
   need(all(nums[raw-1]==0 for raw in outside),"complete1834 support")
   for row,x in enumerate(nums):
    need((x-D*values[row*36+slot])%modulus==0,"all6188 p768 source residue identity")
    if row%256==0:check()
   product=H.exact_product(nums,terms,check);need(all(x==0 for x in product),"all4367 fresh exact integer products")
   nmax=max(map(abs,nums));maxbits=nmax.bit_length()
   cert={"format":"isp-new-six-normalized-koszul-actual-source-v1","slot":slot,"binding":QBIND,
       "denominator":str(D),"original6188Numerators":[str(x) for x in nums],
       "all36FreeNormalizedCoordinatesVerified":True,"all1834OutsideCoordinatesZero":True,
       "all4367FreshExactIntegerProductsZero":True,"all6188ActualP768ResiduesVerified":True,
       "numeratorsSHA256":vecsha(nums),"zeroOriginalProductSHA256":vecsha(product)}
   cr=save(out/("normalized-six-slot%02d-verified.json.gz"%slot),cert);files.append(cr)
   records.append({"slot":slot,"denominatorBits":D.bit_length(),"maximumNumeratorBits":maxbits,
       "denominatorDecimal":str(D),"numeratorsSHA256":vecsha(nums),"nonzeroSourceRows":sum(x!=0 for x in nums),
       "bothHeightsWithinBalancedP768Bound":D<=balanced and nmax<=balanced,
       "twoTimesNumeratorDenominatorBelowP768":2*nmax*D<modulus,
       "all4367FreshExactIntegerProductsZero":True,"all6188ActualP768ResiduesVerified":True,"certificate":cr})
   r["completedSlots"].append(slot);checkpoint()
  r.update({"status":"completed","allSixNormalizedPureFreeAxesVerified":True,
      "allSixFullOriginalIntegerProductsZero":True,"allSixCompleteP768SourceResiduesVerified":True,
      "newOriginalKernelDimensionsAddedByThisStep":0})
  code=0
 except TimeoutError as e:r.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:r.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:checkpoint()
 need((out/"six-normalized-koszul-p768-receipt.json").stat().st_size<100000,"small receipt bound")
 print(json.dumps(r),flush=True);return code
if __name__=="__main__":sys.exit(main())
