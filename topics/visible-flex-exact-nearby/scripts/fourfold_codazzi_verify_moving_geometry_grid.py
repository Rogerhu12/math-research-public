#!/usr/bin/env python3
"""Validate the actual complete moving geometry's radial integration grid.

The original complete numerical block chain is reproduced and compared
bit for bit. Directed third Taylor polynomials plus complete fourth
derivative bounds control the true model ODE at every exact angle grid
point. A separate continuous-angle and exact-solution comparison is still
required; neither is inferred from this finite-angle certificate.
"""
from __future__ import annotations
import argparse,gzip,importlib,json,math,sys,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_moving_connection_frame_probe import (
    Connection,CompleteBlocks,load_exact_object,RotationalBodyTarget,
    RotationalGraftTarget,MovingRegularEndpoint,load_candidate,array_sha,sha)
from fourfold_codazzi_moving_geometry_directed_jets import (
    model_jets,coefficient_norms,local_taylor_budget,maximum_euclidean,
    Box,DirectedFFT,arb_box,stack)
from fourfold_codazzi_full_body_graft_target_jets import ReciprocalFullTargetJets
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_interval import sincos
from fourfold_phase_metric_defect import record
from fourfold_codazzi_rotational_cap_jacobi import box_from_record

FINAL="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)

def persist(path,doc):
    raw=(json.dumps(doc,indent=2,allow_nan=False)+"\n").encode()
    if str(path).endswith(".gz"):raw=gzip.compress(raw,mtime=0)
    temporary=Path(str(path)+".partial");temporary.write_bytes(raw);temporary.replace(path)

def exact_anchor(fields,target,N):
    phase=stack([arb_box(arb.pi()*k/(2*N)) for k in range(N)])
    phase=phase+fields["inverse_lift_shift"][0]
    sine,cosine=sincos(phase)
    a=arb_box(target["a"]);rad=arb_box(target["beta"]/target["gamma"])
    vertical=arb_box(-target["a"]*target["Cref"])
    zero=Box(np.zeros(N))
    return stack([a*cosine,a*sine,zero,
                  rad*cosine,rad*sine,zero+vertical,
                  -sine,cosine,zero,
                  vertical*cosine,vertical*sine,zero-rad],1)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidate",type=Path,required=True)
    ap.add_argument("--geometry-report",type=Path,required=True)
    ap.add_argument("--geometry-blocks",type=Path,required=True)
    ap.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    ap.add_argument("--q-vector",type=Path,default=Path(
        "notes/2026-11-13-R133-regular-r25over8-q256-floating.json"))
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--max-blocks",type=int,default=4)
    ap.add_argument("--resume",action="store_true")
    args=ap.parse_args();start=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.max_blocks<1:raise ValueError("positive bounded block work is required")
    if args.out.exists()!=args.resume:raise FileExistsError("explicit resume or a new output is required")
    old=load(args.geometry_report);gi=old["identity"]
    if not old["complete"] or old["failure"] is not None:
        raise ValueError("a complete original numerical geometry is required")
    if (sha(args.candidate)!=FINAL or gi["candidate_sha256"]!=FINAL or
        sha(args.object)!=gi["object_sha256"] or sha(args.q_vector)!=gi["q_vector_sha256"]):
        raise ValueError("the complete original geometry object changed")
    if sha(Path(__file__).with_name("fourfold_codazzi_moving_connection_frame_probe.py"))!=old["source_sha256"]:
        raise ValueError("the original geometry producer changed")
    for name,digest in gi["modules"].items():
        module=importlib.import_module(name)
        if sha(module.__file__)!=digest:raise ValueError("an original numerical geometry module changed")
    saved=load_candidate(args.candidate);meta=json.loads(str(saved["metadata"]))
    alpha=Fraction(meta["exact_float_amplitude"]);nu=Fraction(meta["exact_float_nu"])
    N=int(gi["angles"]);nodes=np.asarray(saved["radial_nodes"])
    exact_nodes=[Fraction.from_float(float(x)) for x in nodes]
    geometry,_=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=MovingRegularEndpoint(geometry,32,N,body,graft,
                                q_path=args.q_vector,mean_boundary="outer")
    system.alpha=float(alpha);connection=Connection(system,saved,float(nu))
    radii=np.unique(np.r_[np.linspace(0.,25/8,int(np.ceil((25/8)/gi["max_requested_step"]))+1),
                          nodes,.05,.18,.25,3.])
    if array_sha(radii)!=gi["radial_grid_sha256"] or len(radii)!=8967:
        raise ValueError("complete original radial grid differs")
    store=CompleteBlocks(args.geometry_blocks,gi,True)
    last_state,next_index,_=store.recover(len(radii),N)
    if next_index!=-1 or store.previous!=old["last_complete_block_sha256"]:
        raise ValueError("complete numerical checkpoint chain differs")
    target=ReciprocalFullTargetJets(args.object,Fraction(1,10**9),512)
    fft=DirectedFFT()
    dependencies={name:sha(Path(__file__).with_name(name)) for name in (
        "fourfold_codazzi_moving_geometry_directed_jets.py",
        "fourfold_codazzi_full_body_graft_target_jets.py",
        "fourfold_codazzi_reciprocal_compact_target_jets.py",
        "fourfold_codazzi_cubic_target_jets.py","fourfold_codazzi_high_target_jets.py",
        "fourfold_phase_beta_bulk_box.py","fourfold_phase_root_interval.py",
        "fourfold_phase_beta_bulk_interval.py","fourfold_phase_uniform_tail.py")}
    identity=dict(source_sha256=sha(__file__),dependencies=dependencies,
        geometry_report_sha256=sha(args.geometry_report),
        original_geometry_chain_sha256=store.previous,candidate_sha256=FINAL,
        object_sha256=sha(args.object),q_vector_sha256=sha(args.q_vector),
        radial_grid_sha256=array_sha(radii),angles=N,bits=192,
        integration_norm_scope="operator norms at all exact angle grid points",
        actual_alpha=str(alpha),actual_nu=str(nu),target_half_width="1/1000000000")
    if args.resume:
        doc=load(args.out)
        if doc["identity"]!=identity or doc["complete"] or doc["failure"] is not None:
            raise ValueError("only the same successful partial computation may resume")
        done=doc["complete_blocks"]
        if done<0 or done>=len(store.files):raise ValueError("invalid saved complete block count")
        with np.load(store.files[done-1],allow_pickle=False) as z:
            state=z["last_state"].copy()
        eQ=box_from_record(doc["frame_error_at_exact_angle_grid"]).upper()
        eF=box_from_record(doc["position_error_at_exact_angle_grid"]).upper()
        elapsed=doc["wall_seconds"];doc["resume_history"].append(done)
    else:
        done=0;state=connection.anchor();elapsed=0.
        z,_=target.coefficients(Fraction(25,8),Fraction(25,8),nu)
        fields=model_jets(saved,len(nodes)-2,Fraction(25,8),Fraction(25,8),z,alpha,fft,N)
        anchor=exact_anchor(fields,z,N)
        eQ=maximum_euclidean(Box(state[:,3:12])-anchor[:,3:12])
        eF=maximum_euclidean(Box(state[:,:3])-anchor[:,:3])
        doc=dict(kind="complete_directed_radial_model_geometry_at_exact_angle_grid",
            identity=identity,complete=False,failure=None,complete_blocks=0,
            total_blocks=len(store.files),total_radial_rows=len(radii),
            rows=[],block_checks=[],resume_history=[],wall_seconds=0.,
            exact_angle_definition="phi_k=pi*k/(2*N), k=0,...,N-1",
            whole_closed_radial_intervals=True,whole_original_affine_parameter_interval=True,
            all_connection_modes_retained=True,
            complete_primitive_index=64,complete_connection_index=96,
            model_anchor_frame_error=record(eQ),model_anchor_position_error=record(eF),
            actual_tail_world_anchor_error_not_included=True,
            continuous_angular_geometry_proved=False,
            nonlinear_solution_exists=False,final_geometry_proved=False)
        persist(args.out,doc)
    endpoint_cache={}
    try:
        stop=min(len(store.files),done+args.max_blocks)
        for block in range(done,stop):
            with np.load(store.files[block],allow_pickle=False) as z:
                indices=z["indices"].copy();expected=z["last_state"].copy()
            block_rows=[]
            for index in indices:
                index=int(index)
                if index==len(radii)-1:continue
                outer=Fraction.from_float(float(radii[index+1]))
                inner=Fraction.from_float(float(radii[index]))
                # Near two adjacent binary64 endpoints a floating midpoint
                # can round to the wrong side of a real PPoly interface.
                piece=bisect_right(exact_nodes,(outer+inner)/2)-1
                if piece<0 or piece>=len(nodes)-1:raise ValueError("invalid true candidate piece")
                whole_cuts=[inner]+[c for c in target.cuts if inner<c<outer]+[outer]
                after=connection.step(state,float(outer),float(inner))
                intermediate=state.copy();substeps=[]
                # Third target jets are one-sided. Never apply one Taylor
                # polynomial across a scalar germ or compact-control join.
                for left,right in reversed(list(zip(whole_cuts,whole_cuts[1:]))):
                    values,germ=target.coefficients(left,right,nu)
                    fields=model_jets(saved,piece,left,right,values,alpha,fft,N)
                    an,fn=coefficient_norms(fields,fft,N)
                    # A genuine closed box approaching from the interval's
                    # own side encloses the correct endpoint jets, even at
                    # a target seam; it does not assume matching third jets.
                    epsilon=min((right-left)/2,Fraction(1,2**100))
                    point,_=target.coefficients(right-epsilon,right,nu)
                    at=model_jets(saved,piece,right,right,point,alpha,fft,N)
                    next_state=connection.step(intermediate,float(right),float(left))
                    budget=local_taylor_budget(intermediate,next_state,left-right,at,an,fn)
                    width=exact_arb(right-left)
                    eF=(eF+width*fn[0]*eQ+budget["local_position_error"]).upper()
                    eQ=(eQ+budget["local_frame_error"]).upper()
                    substeps.append(dict(interval=[str(left),str(right)],
                        complete_actual_scalar_germ=list(map(str,germ)),
                        endpoint_jet_box=[str(right-epsilon),str(right)],
                        connection_derivative_norms=[record(x) for x in an],
                        radial_position_derivative_norms=[record(x) for x in fn],
                        budget={k:record(v) for k,v in budget.items()}))
                    intermediate=next_state
                # Keep and check the original full-step numerical chain.
                # Any difference from the auxiliary germ-wise chain is paid.
                joinQ=maximum_euclidean(Box(after[:,3:12])-Box(intermediate[:,3:12]))
                joinF=maximum_euclidean(Box(after[:,:3])-Box(intermediate[:,:3]))
                eQ=(eQ+joinQ).upper();eF=(eF+joinF).upper()
                block_rows.append(dict(radial_index=index,interval=[str(inner),str(outer)],
                    candidate_piece=piece,one_sided_germ_substeps=substeps,
                    original_step_reconnection_frame_error=record(joinQ),
                    original_step_reconnection_position_error=record(joinF),
                    cumulative_frame_error=record(eQ),cumulative_position_error=record(eF)))
                state=after
            if not np.array_equal(state.view(np.uint64),expected.view(np.uint64)):
                raise ValueError("actual original numerical block endpoint did not reproduce bit for bit")
            doc["rows"].extend(block_rows)
            doc["block_checks"].append(dict(block=block,path=store.files[block].name,
                sha256=sha(store.files[block]),complete_endpoint_bits_equal=True))
            doc["complete_blocks"]=block+1
            doc["frame_error_at_exact_angle_grid"]=record(eQ)
            doc["position_error_at_exact_angle_grid"]=record(eF)
            doc["wall_seconds"]=elapsed+time.monotonic()-start
            doc["complete"]=block+1==len(store.files)
            if doc["complete"] and len(doc["rows"])!=len(radii)-1:
                raise ValueError("complete exact radial interval coverage missing")
            persist(args.out,doc)
            print(dict(complete_blocks=block+1,total_blocks=len(store.files),
                complete_steps=len(doc["rows"]),radius=str(inner),
                frame_error=eQ.str(12),position_error=eF.str(12),
                wall_seconds=doc["wall_seconds"]),flush=True)
    except Exception as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
        doc["wall_seconds"]=elapsed+time.monotonic()-start;persist(args.out,doc)
        raise
    print(json.dumps(dict(complete=doc["complete"],failure=doc["failure"],
        complete_blocks=doc["complete_blocks"],out=str(args.out))),flush=True)

if __name__=="__main__":main()
