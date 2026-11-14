#!/usr/bin/env python3
"""Read-only two-accepted-tail secant-Hessian warm diagnostic.

No ODE, Node, residual, Newton or acceptance operation occurs. The original
backward graph/forward transport formulas are evaluated with NumPy, then the
first-order prediction is compared with the already archived original seed.
All numerical comparisons are diagnostics, not error certificates.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import struct
import sys
import time
import numpy as np

PREDICTOR_SHA='8d39830939a52fc40f7de06cf5a2a9de9959f94058594051a7989b8b40744459'
HELPER_SHA='fb6ed25102cb91a332e1c2d879cf6218f9c88faaebe6916e801e46e6f8c1551f'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    p=Path(path);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def decode(x):
    tag=x[0]
    if tag=='object':return {k:decode(v) for k,v in x[1]}
    if tag=='array':return [decode(v) for v in x[1]]
    if tag=='f64le':return struct.unpack('<d',bytes.fromhex(x[1]))[0]
    if tag=='null':return None
    if tag in ('string','boolean'):return x[1]
    raise ValueError('Unknown typed identity tag')
def snapshot(path,identities,check,label):
    path=Path(path);d=read(path);identities[str(path)]=sha(path)
    check(label+'_schema',d['schema']=='full-shooting-flow-tangent-storage-v1' and d['complete'] and
          d['helperSha256']==HELPER_SHA and d['allStageFlowJacobiansRetained'] and
          d['allBaseStatesAndHeightsRetained'] and d['convergedBaseResidual']<d['originalSolveTolerance'])
    canonical=d['identityCanonical']
    check(label+'_canonical_sha',hashlib.sha256(canonical.encode()).hexdigest()==d['identitySha256'])
    identity=decode(json.loads(canonical));dims=d['dimensions'];M=dims['modes'];K=dims['stateDimension']
    depth=dims['stages'];nodes=dims['nodes']
    check(label+'_dimensions',K==2*M and nodes==depth+1 and identity['parameters']['modes']==M and
          identity['parameters']['depth']==depth and len(identity['rawNode'])==identity['parameters']['physicalDepth']+1 and
          len(identity['stageLayout'])==depth and len(identity['farGraph'])==M)
    def payload(row):
        p=path.parent/row['file'];raw=p.read_bytes()
        check(label+'_file_'+row['file'],p.name==row['file'] and len(raw)==row['bytes'] and
              hashlib.sha256(raw).hexdigest()==row['sha256'])
        data=gzip.decompress(raw)
        check(label+'_raw_'+row['file'],len(data)==row['rawBytes'] and hashlib.sha256(data).hexdigest()==row['rawSha256'])
        a=np.frombuffer(data,dtype='<f8');check(label+'_finite_'+row['file'],bool(np.isfinite(a).all()))
        identities[str(p)]=row['sha256'];return a
    base=payload(d['base']);at=nodes*K;states=base[:at].reshape(nodes,K).copy()
    height=base[at:at+M].copy();at+=M;far=base[at:at+M].copy();at+=M;radius=float(base[at]);at+=1
    check(label+'_binary_identity',radius==identity['radius'] and np.array_equal(far,identity['farGraph']) and
          np.array_equal(base[at:],identity['rawNode']))
    flows=np.empty((depth,K,K));first=0
    for row in d['chunks']:
        lo=int(row['firstStage']);hi=lo+int(row['stageCount'])
        check(label+'_stage_coverage_'+str(lo),lo==first and lo<hi<=depth)
        flows[lo:hi]=payload(row).reshape(hi-lo,K,K);first=hi
    check(label+'_complete_stage_coverage',first==depth)
    return d,identity,states,height,far,radius,flows

def graph_transport(flows,far):
    depth=len(flows);M=len(far);graphs=np.empty((depth+1,M,M));transports=np.empty((depth,M,M))
    graphs[depth]=np.diag(far);max_condition=0.;worst_backward=0.
    eye=np.eye(M)
    for n in range(depth-1,-1,-1):
        J=flows[n];g=graphs[n+1]
        A=J[:M,:M]+J[:M,M:]@g;C=J[M:,:M]+J[M:,M:]@g
        T=np.linalg.solve(A,eye);transports[n]=T;graphs[n]=C@T
        condition=float(np.linalg.norm(A,np.inf)*np.linalg.norm(T,np.inf));max_condition=max(max_condition,condition)
        backward=float(np.linalg.norm(A@T-eye,np.inf)/(1+np.linalg.norm(A,np.inf)*np.linalg.norm(T,np.inf)))
        worst_backward=max(worst_backward,backward)
    return graphs,transports,max_condition,worst_backward
def direction(graphs,transports,dq):
    M=len(dq);out=np.empty((len(graphs),2*M));dq=dq.copy()
    for n,g in enumerate(graphs):
        out[n,:M]=dq;out[n,M:]=g@dq
        if n<len(transports):dq=transports[n]@dq
    return out
def stats(value,reference):
    err=value-reference;scale=np.maximum(np.max(abs(reference),axis=1,keepdims=True),1e-250)
    relative=abs(err)/scale;M=value.shape[1]//2
    return dict(max_absolute=float(np.max(abs(err))),max_node_relative=float(np.max(relative)),
        rms_node_relative=float(np.sqrt(np.mean(relative*relative))),
        worst_node_relative=list(map(int,np.unravel_index(np.argmax(relative),relative.shape))),
        cut_Q_max_absolute=float(np.max(abs(err[0,:M]))),cut_pi_max_absolute=float(np.max(abs(err[0,M:]))),
        raw_final_node_max_absolute=float(np.max(abs(err[-1]))))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('previous','current','initial-seed','iteration-reference','original-predictor','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    a=ap.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError(a.out)
    checks={};identities={}
    def check(name,value):
        if not value:raise ArithmeticError(name)
        checks[name]=True
    check('original_predictor_source',sha(a.original_predictor)==PREDICTOR_SHA);identities[str(a.original_predictor)]=PREDICTOR_SHA
    previous=snapshot(a.previous,identities,check,'previous');current=snapshot(a.current,identities,check,'current')
    ma,ia,sa,ha,far,radius,fa=previous;mb,ib,sb,hb,farb,radiusb,fb=current
    check('full_tail_identity_unchanged',ma['identityCanonical']==mb['identityCanonical'] and radius==radiusb and
          np.array_equal(far,farb) and sa.shape==sb.shape)
    seed=read(a.initial_seed);ref=read(a.iteration_reference)
    identities[str(a.initial_seed)]=sha(a.initial_seed);identities[str(a.iteration_reference)]=sha(a.iteration_reference)
    cs,cr=seed['checkpoint'],ref['checkpoint'];htarget=np.asarray(cs['cutHeight'],dtype=float)
    seed_states=np.asarray(cs['states'],dtype=float);reference=np.asarray(cr['states'],dtype=float)
    check('same_complete_target_height_and_states',np.array_equal(htarget,np.asarray(cr['cutHeight'])) and
          cs['rawNode']==cr['rawNode']==ib['rawNode'] and seed_states.shape==reference.shape==sb.shape and
          np.isfinite(seed_states).all() and np.isfinite(reference).all())
    io={'traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}
    for name,c in (('seed',cs),('iteration',cr)):
        check(name+'_same_nonIO_parameters',{k:v for k,v in c['parameters'].items() if k not in io}==ib['parameters'])
    dh=hb-ha;dn=htarget-hb;alpha=float(dh@dn/(dh@dh));orthogonal=dn-alpha*dh
    collinearity=float(np.linalg.norm(orthogonal)/np.linalg.norm(dn))
    check('actual_target_direction_near_collinear',collinearity<1e-8)
    ga,ta,cona,bera=graph_transport(fa,far);gb,tb,conb,berb=graph_transport(fb,far)
    r4=radius**4;M=len(far)
    linear=sb+direction(gb,tb,htarget/r4-sb[0,:M]);linear[0,:M]=htarget/r4
    previous_action=direction(ga,ta,dh/r4);current_action=direction(gb,tb,dh/r4)
    correction=.5*alpha*alpha*(current_action-previous_action)
    predicted=seed_states+correction;predicted[0,:M]=htarget/r4
    secant_value=sb-sa
    a2=(previous_action-secant_value)+2*(current_action-secant_value)
    a3=(previous_action-secant_value)+(current_action-secant_value)
    cubic_correction=alpha**2*a2+alpha**3*a3
    cubic=seed_states+cubic_correction;cubic[0,:M]=htarget/r4
    t=1+np.longdouble(alpha);s0=sa.astype(np.longdouble);s1=sb.astype(np.longdouble)
    v0=previous_action.astype(np.longdouble);v1=current_action.astype(np.longdouble)
    direct=((2*t**3-3*t**2+1)*s0+(t**3-2*t**2+t)*v0+
            (-2*t**3+3*t**2)*s1+(t**3-t**2)*v1).astype(np.float64)
    direct[0,:M]=htarget/r4
    agreement=stats(linear,seed_states);seed_error=stats(seed_states,reference);second_error=stats(predicted,reference)
    cubic_error=stats(cubic,reference)
    # A numerical implementation cross-check, explicitly not an exact theorem.
    check('NumPy_original_formula_agreement_is_negligible',agreement['max_absolute']<seed_error['max_absolute']*1e-7 and
          agreement['max_node_relative']<seed_error['max_node_relative']*1e-7)
    check('Dirichlet_height_remains_bit_identical',np.array_equal(predicted[0,:M].view(np.uint64),seed_states[0,:M].view(np.uint64)))
    output=dict(schema='same-tail-two-point-full-flow-secant-offline-diagnostic-v1',scope=__doc__,
        source_sha256=sha(__file__),input_sha256=identities,checks=checks,all_checks=True,
        dimensions=ma['dimensions'],same_complete_tail_identity_sha256=ma['identitySha256'],
        reference_scope='Already recorded accepted Newton trial iteration02 at the q122 initial H; not a final coupled q122 acceptance.',
        iteration_reference=ref['iteration'],previous_base_residual=ma['convergedBaseResidual'],current_base_residual=mb['convergedBaseResidual'],
        target_direction=dict(alpha=alpha,orthogonal_relative_l2=collinearity,
            previous_delta_H_max=float(np.max(abs(dh))),target_delta_H_max=float(np.max(abs(dn)))),
        formula='original linear seed + (alpha^2/2)*(J_current-J_previous)*(H_current-H_previous); target cut Q preserved exactly.',
        original_formula_NumPy_agreement=agreement,original_archived_linear_seed_error=seed_error,
        secant_corrected_seed_error=second_error,
        cubic_Hermite_seed_error=cubic_error,
        cubic_Hermite_formula='At t=1+alpha use the two values and directional tangents; evaluate the correction to the archived linear seed as alpha^2*((v0-d)+2*(v1-d))+alpha^3*((v0-d)+(v1-d)), d=s1-s0.',
        cubic_Hermite_direct_longdouble_agreement=stats(cubic,direct),
        improvements={k:seed_error[k]/second_error[k] for k in ('max_absolute','max_node_relative','rms_node_relative','cut_pi_max_absolute')},
        cubic_Hermite_improvements={k:seed_error[k]/cubic_error[k] for k in ('max_absolute','max_node_relative','rms_node_relative','cut_pi_max_absolute')},
        correction=dict(max_absolute=float(np.max(abs(correction))),
            max_node_relative=float(np.max(abs(correction)/np.maximum(np.max(abs(sb),axis=1,keepdims=True),1e-250)))),
        numerical_graph_checks=dict(previous_max_condition=cona,current_max_condition=conb,
            previous_max_normalized_inverse_residual=bera,current_max_normalized_inverse_residual=berb),
        original_solver_modified=False,ODE_Node_Newton_residual_evaluations=0,new_target_accepted=False,
        rigorous_Hessian_remainder_certified=False,numerical_values_are_diagnostics=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,command=sys.argv)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),checks=len(checks),
        improvement=output['improvements'],cubic_improvement=output['cubic_Hermite_improvements'],first=seed_error,second=second_error,cubic=cubic_error,
        elapsed=output['elapsed_seconds'],peak_rss_kib=output['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
