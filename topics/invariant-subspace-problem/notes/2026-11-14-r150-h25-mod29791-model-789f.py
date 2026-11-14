#!/usr/bin/env python3
"""Reduce the frozen exact original17 integer model modulo31^3, without a solve."""
import argparse,gzip,hashlib,json,time
from pathlib import Path

EXACT_SHA='fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3'
MODEL_SHA='291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6'

def main():
 p=argparse.ArgumentParser()
 for name in ('exact-json','original-model','out'):p.add_argument('--'+name,type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 data=gzip.decompress(a.exact_json.read_bytes()) if a.exact_json.suffix=='.gz' else a.exact_json.read_bytes()
 if hashlib.sha256(data).hexdigest()!=EXACT_SHA:raise ValueError('exact original primitive integer model checksum')
 exact=json.loads(data)
 if exact['format']!='r150-original-primitive-integer-equations-v1':raise ValueError('exact original model format')
 original=a.original_model.read_bytes()
 if hashlib.sha256(original).hexdigest()!=MODEL_SHA:raise ValueError('same original F31 model required')
 tokens=original.decode().split();offset=1
 if tokens[0]!='R150_NATIVE_NF_V1':raise ValueError('original F31 model header')
 equations=[[[int(c) for c in poly] for poly in row] for row in exact['equations']]
 if len(equations)!=17 or any(len(row)!=77 for row in equations):raise ValueError('full original17 equations')
 modulus=31**3;D=int(exact['denominator']);contents=[int(x) for x in exact['contents']]
 if len(contents)!=17 or any(c%31==0 for c in [D,*contents]):raise ValueError('original row normalization units')
 lines=['R150_ORIGINAL_MOD29791_V1',' '.join(map(str,[D%modulus,*[c%modulus for c in contents]]))]
 checks=0
 def get(poly,k):return poly[k] if k<len(poly) else 0
 for e in range(11):
  row=equations[e];values=[]
  for k in range(66):
   if any(row[k+11][1:]):raise ValueError('original N quadratic part must be constant')
   values.append(get(row[k+11],0)%modulus)
  for v in range(11):
   if any(row[v][11:]):raise ValueError('original N parameter degree bound')
   values.extend(get(row[v],d)%modulus for d in range(11))
  for c in values:
   if c%31!=int(tokens[offset]):raise ValueError('complete original N coefficient residue mismatch')
   offset+=1;checks+=1
  lines.append(' '.join(map(str,values)))
 count=int(tokens[offset]);offset+=1
 if count!=3333:raise ValueError('same complete original prebasis')
 offset+=4*count
 for e in range(11,17):
  row=equations[e]
  if any(any(poly) for poly in row[:11]):raise ValueError('original Gamma is exactly quadratic')
  values=[]
  for k in range(66):
   if any(row[k+11][6:]):raise ValueError('original Gamma parameter degree bound')
   values.extend(get(row[k+11],d)%modulus for d in range(6))
  for c in values:
   if c%31!=int(tokens[offset]):raise ValueError('complete original Gamma coefficient residue mismatch')
   offset+=1;checks+=1
  lines.append(' '.join(map(str,values)))
 h0=[int(c) for c in exact['h0']]
 if len(h0)!=25 or h0[-1]!=3125:raise ValueError('frozen exact h0')
 H=[0]*26
 for k,c in enumerate(h0):H[k]-=2*c;H[k+1]+=c
 lines.append(' '.join(str(c%modulus) for c in H))
 output=a.out/'original-integer-h25-mod29791.txt';payload=('\n'.join(lines)+'\n').encode();output.write_bytes(payload)
 receipt={'format':'r150-h25-mod29791-original-model-v1','status':'exact-original-model-reduced','prime':31,'modulus':modulus,'targetMultiplier':'H0=(s-2)*h0','exactIntegerModelSHA256':EXACT_SHA,'originalF31ModelSHA256':MODEL_SHA,'coefficientResidueChecks':checks,'originalEquations':17,'allOriginalRowContentsAre31Units':True,'targetDegree':25,'sourceSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'output':{'file':str(output),'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest()},'mathematicalSourceSolveExecuted':False,'elapsedSeconds':time.monotonic()-start}
 (a.out/'mod29791-model-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)

if __name__=='__main__':main()
