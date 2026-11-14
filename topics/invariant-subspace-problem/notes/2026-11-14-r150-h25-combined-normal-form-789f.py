#!/usr/bin/env python3
"""Form the exact nine normal forms (s-2)*(r1-c1*beta1-c2*beta2).

Only already certified normal forms are combined. No original DAG is rerun.
This is not yet a mod961 original source certificate.
"""
from __future__ import annotations
import argparse,hashlib,json,struct,time
from pathlib import Path

RHS_SHA='5016b8e42f2ef1b36c9107b95616a190a47697b640599cb9eb98b2476be8f317'
BETA_SHA='c1b0e2e79a52e312acb9a9b89a03c031a5d6bbd5afc34c862ff7c2ff35479b2b'
META_SHA='730ee02d91e53cbfc1463fbfb366ee35edaa908775af30f97dedef8cae1749e9'
G_SHA='d5ce008439820c4ed9ff33f58ca33267f4e3badf429ab581311818d1fb5b3a76'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def parse(path,expected,labels,wanted):
    data=path.read_bytes()
    if hashlib.sha256(data).hexdigest()!=expected:raise ValueError('actual source checksum: '+str(path))
    if data[:8]!=b'R150NF31' or struct.unpack_from('<3I',data,8)!=(0,len(labels),1034):raise ValueError('actual complete NF dimensions')
    offset=20;answer={}
    for label in labels:
        raw,target,n=struct.unpack_from('<IHI',data,offset);offset+=10
        if raw or target!=label:raise ValueError('complete actual RHS source dictionary')
        row={};previous=0
        for _ in range(n):
            c,length=struct.unpack_from('<HB',data,offset);offset+=3
            if c<=previous or c>1034 or not 1<=length<=86:raise ValueError('actual NF entry')
            previous=c;poly=data[offset:offset+length];offset+=length
            if len(poly)!=length or not poly[-1] or max(poly)>30:raise ValueError('canonical original field polynomial')
            if label in wanted:row[c]=poly
        if label in wanted:answer[label]=row
    if offset!=len(data) or set(answer)!=set(wanted):raise ValueError('complete normal-form file or selected columns')
    return answer

def main():
    p=argparse.ArgumentParser()
    for k in ('first-normal-form','beta-normal-form','beta-metadata','common-g-result','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
    if sha(a.beta_metadata)!=META_SHA or sha(a.common_g_result)!=G_SHA:raise ValueError('actual original identities and common-g solution required')
    bm=json.loads(a.beta_metadata.read_text());gs=json.loads(a.common_g_result.read_text())
    if not bm['fullOriginalBocksteinDivisionIdentity'] or not bm['allIndividualWeightedBoundsVerified'] or gs['basisDescriptors']!=[[199,2275,0,85],[200,2276,0,85]]:raise ValueError('actual two original kernel sources')
    solution=gs['commonHCorrection']
    if not solution.get('full315OriginalIdentity'):raise ValueError('whole nine-target g identity')
    coefficients=solution['kernelModuleBasisCoefficients']
    if len(coefficients)!=2 or any(len(row)!=9 for row in coefficients):raise ValueError('actual two-by-nine coefficient matrix')
    first=parse(a.first_normal_form,RHS_SHA,list(range(2,11)),set(range(2,11)))
    beta=parse(a.beta_normal_form,BETA_SHA,[L[1] for L in bm['labels']],{2275,2276})
    result=bytearray(b'R150NF31')+struct.pack('<3I',0,9,1034)
    profile=[]
    for j in range(9):
        entries=[];maximum=-1;nonzero=0
        for c in sorted(set(first[j+2])|set(beta[2275])|set(beta[2276])):
            temp=[0]*86
            for k,v in enumerate(first[j+2].get(c,b'')):temp[k]=v
            for acoef,label in zip([coefficients[0][j],coefficients[1][j]],[2275,2276]):
                for k,v in enumerate(beta[label].get(c,b'')):temp[k]=(temp[k]-acoef*v)%31
            out=[0]*87
            for k,v in enumerate(temp):
                out[k]=(out[k]-2*v)%31;out[k+1]=(out[k+1]+v)%31
            while out and not out[-1]:out.pop()
            if out:
                maximum=max(maximum,len(out)-1);nonzero+=sum(v!=0 for v in out);entries.append((c,bytes(out)))
        result.extend(struct.pack('<IHI',0,j+2,len(entries)))
        for c,poly in entries:result.extend(struct.pack('<HB',c,len(poly)));result.extend(poly)
        profile.append({'target':j+2,'nonzeroComponents':len(entries),'nonzeroCoefficients':nonzero,'maximumParameterDegree':maximum})
    out=a.out/'combined-rhs-normal-forms.bin';out.write_bytes(result)
    record={'format':'r150-h25-combined-normal-form-v1','status':'completed','field':31,
      'combination':'(s-2)*(NF(r1_j)-c1_j*NF(beta2275)-c2_j*NF(beta2276))',
      'originalTargetMultiplier':'H0=(s-2)*h0','originalRightHandSideCostBound':86,
      'firstNormalFormSHA256':RHS_SHA,'all200BetaNormalFormSHA256':BETA_SHA,
      'originalBetaMetadataSHA256':META_SHA,'commonGSolutionSHA256':G_SHA,
      'sourceSHA256':sha(__file__),'baseKernelLabels':[bm['labels'][198],bm['labels'][199]],
      'kernelCoefficients':coefficients,'profile':profile,'sourceTransported':False,
      'output':{'file':str(out),'bytes':len(result),'sha256':hashlib.sha256(result).hexdigest()},
      'elapsedSeconds':time.monotonic()-start}
    (a.out/'combined-normal-form-receipt.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'h25-combined-normal-form-complete','actualTargets':9,
      'actualOriginalKernelHeads':[2275,2276],'originalRightHandSideCostBound':86,
      'sourceTransported':False,'elapsedSeconds':record['elapsedSeconds']}),flush=True)

if __name__=='__main__':main()
