#!/usr/bin/env python3
"""Consume R272's existing ordered-ray certificate and bound the new R272 global normal tube."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def get(p):return json.loads(Path(p).read_text())
def ceil(x):return -(-x.numerator//x.denominator)
def upper(x):return F(float(np.nextafter(float(x),np.inf)))
def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','field','potential','composite','edge-defects','new-edge','output'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();com=get(a.composite);d=get(a.edge_defects);new=get(a.new_edge);po=get(a.potential)
    assert com['inputs']['field']==sha(a.field)==d['fieldSHA256']==po['fieldSHA256']
    assert sha(a.potential)==com['inputs']['potential'] and com['completeActualKernelAndGraftEmbedding']
    assert sha(a.edge_defects)=='a75b6d8f84e5f01cf271047b140d3eae997334ba8cc75bc4295217de96c0083c'
    K=load(a.scripts/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py','full_norm_k')
    edges=load(a.scripts/'2ecf-strong-hf-edge-continuous-projection.py','full_norm_edges')
    inside=load(a.scripts/'2ecf-strong-hf-interior-continuous-projection.py','full_norm_middle')
    I=K.I;a.with_proxy_edges=False;mid,M=inside.makepieces(K,a);ext,_=edges.makepieces(K,a)
    sp=[(l,r,x,None,None) for l,r,x in mid]+ext;assert len(sp)==108
    with np.load(a.field) as data:proxy=data['endpointProxy']
    wave=np.arange(M+1)
    upperJet={}
    for sd,ud in ((1,0),(0,1),(2,0),(1,1),(0,2)):
        worst=F(0)
        for l,r,start,side,k in sp:
            h=I(r-l);ctrl=start
            for j in range(sd):ctrl=(5-j)*(ctrl[1:]-ctrl[:-1])/h
            # Convex hull in radius, absolute Fourier sum in angle. Euclidean <= Cartesian l1.
            norm=(I(ctrl.abs_upper())*I((wave**ud)[None,:,None,None])).sum(-1).sum(1).sum(-1)
            bound=upper(np.max(norm.hi))
            if side:
                wid=k[1]-k[0];et=F(0)
                for j,tag in enumerate(('P','V','A')):
                    if ud<2:
                        names=[('P','V','A'),('U','SU','AU')][ud]
                        defect=sum(F(float(v)) for v in d['bounds'][side][names[j]])
                    else:
                        index=0 if side=='left' else 1
                        coeff=proxy[index,j]
                        boundProxy=sum(F(float(abs(x.real))) *int(m)**2+F(float(abs(x.imag)))*int(m)**2 for m,row in enumerate(coeff) for x in row)
                        defect=sum(F(v) for v in new[side][j])+boundProxy
                    c=[[F(1),F(1),F(1),F(0),F(0),F(0)],[0,wid/5,2*wid/5,0,0,0],[0,0,wid**2/20,0,0,0]][j]
                    for count in range(sd):c=[(5-count)*(y-x)/wid for x,y in zip(c,c[1:])]
                    et+=max(map(abs,c))*defect
                bound+=et
            worst=max(worst,bound)
        upperJet[f'{sd}{ud}']=ceil(worst)
    M1=max(10,upperJet['10'],upperJet['01']);M2=max(upperJet['20'],upperJet['11'],upperJet['02'])
    # On full upper core and straight ambient chords, |x|,|y|<=2, |grad x|<=4.5 and |grad y|=4.
    H=max(sum(abs(F(v))*(F(9,2)*i+4*j)*2**(i+j-1) for v,(i,j) in zip(row,po['monomials'])) for row in po['coefficients'])
    H=ceil(H);area=F('.12')/(F('1.5')*H)
    curvature=max(10,ceil(8*M2*M1**2/area**2))
    angular=80*(6*M1+1);ray=max(500,25*M1**2)
    near=angular+ray*H*(1+angular)
    # 2*rho <= 2/(KC)<pi/(KC) and rho<=1/K, handling both long and close chords.
    reach=min(F(1,1000),F(1,curvature*near))
    out=dict(schema='first-explicit-R272-complete-grafted-closed-surface-rolling-radius-v1',
       sourceSHA256=sha(__file__),compositeSHA256=sha(a.composite),fieldSHA256=sha(a.field),potentialSHA256=sha(a.potential),
       edgeDefectsSHA256=sha(a.edge_defects),newEdgeSHA256=sha(a.new_edge),commonPhysicalIntervals=len(sp),
       existingOrderBoxes=com['completeUpperDiskPotentialBoxes'],completeHFJetNormUppers=upperJet,wholeChartFirstBound=M1,
       potentialGradientBound=H,HFJacobianAreaLower=str(area),wholeKernelCurvatureUpper=curvature,
       angularLegOverChord=angular,fixedRayLengthOverPotential=ray,completeNearPathOverChord=near,
       completeAllPhaseGraftedReachLower=str(reach),completeNormalizedReachLower=str(reach/F(com['graftedDiameterUpper'])))
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(upperJet,M1,M2,H,curvature,near,float(reach),float(reach/F(com['graftedDiameterUpper'])))
if __name__=='__main__':main()
