#!/usr/bin/env python3
"""Exact compatible length brackets for all literal closed polar tensors' residual infinite sheets."""
import argparse,json
from fractions import Fraction as F
from pathlib import Path
p=argparse.ArgumentParser()
for k in ('meridian','buffer','tail','state','out'):p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args();mer,buf,tail,state=(json.loads(getattr(a,k).read_bytes()) for k in ('meridian','buffer','tail','state'));m=mer['selected'][state['index']];b=buf['choices'][0];ws=list(map(F,b['levels']));widths=list(map(F,b['lengths']));seam=F(tail['exactInnerSeam']);rc=F(buf['outerRadius']);cuff=F(8,25);mult=(rc-seam)/sum(widths);S=sum(map(F,m['lengths']))+sum(map(F,state['correctedCoasts']));buff=mult*sum(L*(1+max(v,w)**2/2) for L,v,w in zip(widths,ws,ws[1:]));deep=(seam-cuff)*(1+F(float(.02))**2/2);low=S+rc-cuff;high=S+buff+deep;assert F(1489,1000)<low<high<F(1492,1000)<F(3,2)
d=dict(schema='R295-exact-common-infinite-material-length',prefix=str(S),bufferUpper=str(buff),terminalUpper=str(deep),Tlower=str(low),Tupper=str(high))
with a.out.open('x') as o:json.dump(d,o,indent=2);o.write('\n')
print(float(low),float(high))
