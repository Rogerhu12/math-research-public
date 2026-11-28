#!/usr/bin/env python3
"""Continuous Gram and own curvature on the new 65-node central-gap physical ramp."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time

import numpy as np


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def module(p, name):
    sp=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def certify_end(raw,C,bits,L,model,gram,cert,terminal):
    trace=model.terminal_trace
    weights=[[L**(p-i)*terminal.hermite_norm(gram.H2[3+p],i) for p in range(3)]
             for i in range(3)]
    delta={(i,j):sum(weights[i][p]*trace[p][j] for p in range(3))
           for i in range(3) for j in range(3)}
    U=gram.angular(C,model.degree)
    mu=[gram.vector_bernstein_l1(U,bits,L,i) for i in range(3)]
    E=Q(raw['Eminus1']['rational'])
    F=Q(raw['F']['rational'])
    G=[Q(x['rational']) for x in raw['GminusTarget']]
    S=cert.I(1+E).sqrt().upper()
    ds=delta[1,0]
    du=[delta[i,1] for i in range(3)]
    E+=2*S*ds+ds**2
    F+=S*du[0]+mu[0]*ds+ds*du[0]
    G=[G[j]+sum(math.comb(j,k)*(mu[k]*du[j-k]+du[k]*mu[j-k]+du[k]*du[j-k])
                for k in range(j+1)) for j in range(3)]
    u=gram.upper
    return dict(Eminus1=u(E),F=u(F),GminusTarget=[u(x) for x in G],
                normalizedF=u(F/model.B),relativeG=u(G[0]/model.B**2),
                spectralRelativeMetric=u(max(E,G[0]/model.B**2)+F/model.B)),delta


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','submaster','master','coast','master-report','endpoint-input','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--stage',choices=('interior','terminal'),required=True)
    ap.add_argument('--terminal-trace',type=Path)
    a=ap.parse_args()
    start=time.monotonic()
    root=a.scripts
    sources={key:root/name for key,name in {
        'gram':'6a65-geometry-ramp-native-gram-certificate.py',
        'curvature':'6a65-geometry-ramp-native-curvature-certificate.py',
        'terminal':'6a65-geometry-final-ramp-cell-certificate.py',
        'cert':'6a65-m12-r137-continuous-domain.py',
        'ellipse':'6a65-geometry-central-gap-held-budget.py'}.items()}
    gram,curvature,terminal,cert,ellipse=(module(p,'refined_raw_'+k) for k,p in sources.items())
    I=cert.I
    info=json.loads(a.master_report.read_text());entry=json.loads(a.endpoint_input.read_text())
    ids={k:sha(p) for k,p in dict(entry=Path(__file__),submaster=a.submaster,coast=a.coast,master=a.master,
                                    masterReport=a.master_report,endpointInput=a.endpoint_input,**sources).items()}
    if (ids['master']!=info['rampSHA256'] or ids['coast']!=info['coastSHA256'] or
        ids['submaster']!=entry['source']['masterSHA256'] or ids['master']!=entry['source']['physicalMasterSHA256']):
        raise ValueError('Actual new physical ramp, its endpoints and coast required')
    old=gram.ActualRamp(a.submaster)
    if a.stage=='terminal':
        if a.terminal_trace is None:raise ValueError('New accurate terminal trace is required')
        tr=json.loads(a.terminal_trace.read_text())
        if (not tr['fullAngularDomainCertified'] or tr['source']['masterSHA256']!=ids['submaster']
            or tr['source']['coastMasterSHA256']!=ids['coast'] or tr['source']['gramReportSHA256']!=ids['endpointInput']):
            raise ValueError('Actual whole-angle terminal trace is required')
        ids['terminalTrace']=sha(a.terminal_trace)
        old.terminal_trace=[[Q(x['rational']) for x in tr['actualCentralAngleCompletePortDerivativeBounds'][k]]
                            for k in ('P','V','A')]
    with np.load(a.master,allow_pickle=False) as z:
        sx=z['sx'].copy(); raw=z['coefficients'].copy()
        assert np.array_equal(z['wave'],old.wave)
        assert all(Q(float(z[k]))==v for k,v in [('centralA',old.A),('centralB',old.B),('v',old.v),
            ('ramp',old.ramp),('centralLength',old.c),('a0',old.a0)])
    assert raw.shape==(65,768,3,3) and np.array_equal(raw[::4],old.raw)
    assert np.array_equal(sx[::4],old.sx) and np.all(np.diff(sx)>0)
    selected=list(range(63)) if a.stage=='interior' else [63]
    scale=max(old.input_bits,max(float(v).as_integer_ratio()[1].bit_length()
                for part in (raw.real,raw.imag) for v in part.flat))
    lo,hi=ellipse.perimeter_over_pi(old.A,old.B,terms=32)
    abox=(lo/2,hi/2)
    arc=[str(q) for q in abox]
    a.out.parent.mkdir(exist_ok=True,parents=True)
    if a.out.exists():
        raise FileExistsError(a.out)
    receipts=a.out.with_suffix(a.out.suffix+'.cells')
    receipts.mkdir(exist_ok=True)
    # All local indexing maps back to the original exact model. Only the very
    # first local cell uses ActualRamp.port(0), the central ellipse override.
    computed=[]
    for j in selected:
        saved=receipts/f'cell-{j:03d}.json'
        if saved.exists():
            row=json.loads(saved.read_text())
            assert row['source']==ids and row['index']==j
            computed.append(row)
            continue
        model=copy.copy(old)
        model.input_bits=scale
        model.port_cache={}
        local=int(j!=0)
        pick=[0,j,j+1] if local else [0,1]
        model.raw=raw[pick]
        model.sx=sx[pick]
        proxy,_=gram.check_cell(model,local,95,abox)
        actual=copy.deepcopy(proxy)
        raw_bounds=actual['completeRawNativeGramBounds']
        delta={}
        if j==63:
            C,bits,L,left=model.cell(local)
            raw_bounds,delta=certify_end(raw_bounds,C,bits,L,model,gram,cert,terminal)
            actual['completeRawNativeGramBounds']=raw_bounds
        # The curvature consumer explicitly indexes its model.cell() and row
        # by the same LOCAL index. The public receipt below keeps physical j.
        report=dict(exactEllipticArcRadiusInterval=arc,rows=[None]*local+[actual])
        whole=curvature.WholeDomain(gram,cert,model,report,95)
        class ActualCell(curvature.Cell):
            def jets(self,index,count,lo,hi):
                result=super().jets(index,count,lo,hi)
                for i,k,name in ((1,0,'S'),(0,1,'U'),(2,0,'SS'),(1,1,'SU'),(0,2,'UU')):
                    if delta:
                        e=delta[i,k]
                        result[name]=[v+I(-e,e) for v in result[name]]
                return result
        cell=ActualCell(whole,local)
        kappa,area,leafcount,splits=Q(0),None,0,0
        def consume(k,n,lo,hi,depth=0):
            nonlocal kappa,area,leafcount,splits
            values=cell.geometry(k,n,lo,hi)
            bound=values['curvature'].upper()
            if bound>Q(10) and depth<8:
                splits+=1
                if depth%2==0:
                    consume(2*k,2*n,lo,hi,depth+1)
                    consume(2*k+1,2*n,lo,hi,depth+1)
                else:
                    mid=(lo+hi)/2
                    consume(k,n,lo,mid,depth+1)
                    consume(k,n,mid,hi,depth+1)
                return
            kappa=max(kappa,bound)
            amin=values['area'].lower()
            area=amin if area is None else min(area,amin)
            leafcount+=1
        for k in range(64):
            consume(k,64,Q(0),Q(1))
        row=dict(source=ids,index=j,localSupplierIndex=local,physicalRelativeInterval=proxy['relativePhysicalDomain'],
                 ownCurvatureUpper=str(kappa),nativeAreaLower=str(area),curvatureClosedBoxes=leafcount,
                 splits=splits,relativeMetricUpper=raw_bounds['spectralRelativeMetric']['rational'],
                 fullRawGramBounds=raw_bounds,accurateTerminalRepair=(j==63),
                 terminalCartesianJetPerturbation={str(ij):str(val) for ij,val in delta.items()})
        tmp=saved.with_suffix('.tmp')
        tmp.write_text(json.dumps(row,indent=2)+'\n')
        tmp.replace(saved)
        print(json.dumps(dict(index=j,metric=float(Q(row['relativeMetricUpper'])),kappa=float(kappa),
                              boxes=leafcount,seconds=time.monotonic()-start)),flush=True)
        computed.append(row)
    worst=max(computed,key=lambda r:Q(r['relativeMetricUpper']))
    kworst=max(computed,key=lambda r:Q(r['ownCurvatureUpper']))
    for j,row in zip(selected,computed):
        assert list(map(Q,row['physicalRelativeInterval']))==[Q(float(sx[j])),Q(float(sx[j+1]))]
    metric=Q(worst['relativeMetricUpper'])
    curvature_upper=Q(kworst['ownCurvatureUpper'])
    result=dict(schema='new-gap-physical-H65-raw-Gram-curvature-continuous-v1',source=ids,
                originalMaterialAngle='u_ellipse = integral_0^theta ell / a_ellipse, independent of s',
                stage=a.stage,nodes=65,selected=selected,completeRamp=False,
                closedNativeRadialDomain=['0',str(old.ramp)],allTheta=True,allOriginalPhasesByIsometry=True,
                centralAndNewAccurateCoastSource=True,
                originalNormalizedR233PositionNotBorrowed=True,
                exactRelativeMetricUpper=str(metric),maximumMetricCell=worst['index'],
                exactOwnCurvatureUpper=str(curvature_upper),maximumCurvatureCell=kworst['index'],
                allBoxes=sum(row['curvatureClosedBoxes'] for row in computed),
                belowOneMicro=metric<Q('1e-6'),belowTwoNano=metric<Q('2e-9'),
                curvatureBelowFocalLimit=curvature_upper<Q(1000,97),
                rawReceiptSHA256=[sha(receipts/f'cell-{j:03d}.json') for j in selected],
                seconds=time.monotonic()-start)
    a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(stage=a.stage,metric=float(metric),kappa=float(curvature_upper),
                          cells=len(selected),seconds=result['seconds'])),flush=True)


if __name__=='__main__':
    main()
