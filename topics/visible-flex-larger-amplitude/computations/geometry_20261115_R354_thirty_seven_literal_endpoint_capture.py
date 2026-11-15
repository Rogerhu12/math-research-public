#!/usr/bin/env python3
"""Request170: observe one real unchanged37 model, without replacing any gate.

Capture actual returned arrays, the final chosen direction, and original
per-interval A-chunk J/P identities. No RHS, J, model action, trial or FD is
added by this wrapper. All new arithmetic belongs to a separate post-model
consumer after the original actual-warm FD attempt. Scientific code executes
only in this public repository's Actions; this source is an independent
execution observer, never a new mathematical producer or warm checkpoint.
"""
from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import os
from pathlib import Path
import sys
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R354-original37-endpoint-literal-cache-capture-v1"
ENTRY = "geometry_20261115_thirty_seven_query_collocation_observer_warm.py"
ENTRY_SHA = "2f70133e81f235af4439a1d2b173be835532ae5e8521e3be5216ed2750bd8778"
PRODUCER = "geometry_20261115_thirty_seven_query_condensed_warm.py"
PRODUCER_SHA = "293045c6e52ef7760f3e3f275aa6d7ec63f9d38ef070178932dcb9022e717ef4"
DOMAIN = "geometry_20261115_thirty_seven_query_domain_operator.py"
DOMAIN_SHA = "2e189fbf48ddeb5bb2ffba60047ee544bc39b22c6fe5073a91dad6bb2a1074e3"
FFT = "geometry_20261114_fft_frenet.py"
FFT_SHA = "973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401"
ENGINE = "geometry_20261114_full_angle_projection_warm.py"
ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
AUGMENTED = "geometry_20261114_full_dn_augmented.py"
AUGMENTED_SHA = "f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e"
PHYSICAL = "geometry_20261114_r225_free_core_bvp.py"
PHYSICAL_SHA = "a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08"
HERE = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for raw in iter(lambda:f.read(1 << 20), b""):
            h.update(raw)
    return h.hexdigest()


def canonical(value):
    return (json.dumps(value,ensure_ascii=True,sort_keys=True,
        separators=(",",":"),allow_nan=False)+"\n").encode("ascii")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
        os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "Scientific observation belongs only to the original public Actions")
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--resume",type=Path,required=True)
    parser.add_argument("--expected-resume-sha",required=True)
    parser.add_argument("--parent-status",type=Path,required=True)
    parser.add_argument("--expected-parent-status-sha",required=True)
    args,_=parser.parse_known_args()
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(args.out.resolve().is_relative_to(temporary) and args.out.resolve()!=temporary
        and not args.out.is_symlink(),"Observe only this job temporary original output")
    for name,expected in ((ENTRY,ENTRY_SHA),(PRODUCER,PRODUCER_SHA),
            (DOMAIN,DOMAIN_SHA),(FFT,FFT_SHA),(ENGINE,ENGINE_SHA),
            (AUGMENTED,AUGMENTED_SHA),(PHYSICAL,PHYSICAL_SHA)):
        require(file_sha(HERE/name)==expected,"Frozen science source changed: "+name)
    import numpy as np
    import geometry_20261115_thirty_seven_query_collocation_observer_warm as observer
    entry=observer.entry
    domain=entry.domain
    require(Path(entry.__file__).resolve()==HERE/PRODUCER,
        "Use the already bound original37 producer")
    nodes=np.asarray(domain.QUERY_ENDPOINT_NODES,dtype=np.int64)
    mids=np.asarray(domain.MID_INTERVALS,dtype=np.int64)
    specs=[dict(v) for v in domain.QUERY_SPECS]
    root=args.out/"R354-return-capture"
    state=dict(schema=SCHEMA,source_sha256=file_sha(__file__),
        source_commit=os.environ.get("GITHUB_SHA"),run_id=os.environ.get("GITHUB_RUN_ID"),
        original_producer=dict(file=PRODUCER,sha256=PRODUCER_SHA),
        original_observer=dict(file=ENTRY,sha256=ENTRY_SHA),
        original_domain=dict(file=DOMAIN,sha256=DOMAIN_SHA),
        original_FFT=dict(file=FFT,sha256=FFT_SHA),
        original_engine=dict(file=ENGINE,sha256=ENGINE_SHA),
        original_augmented=dict(file=AUGMENTED,sha256=AUGMENTED_SHA),
        original_physical=dict(file=PHYSICAL,sha256=PHYSICAL_SHA),
        source_input_warm=dict(file=args.resume.name,bytes=args.resume.stat().st_size,
            sha256=file_sha(args.resume)),
        source_parent_status=dict(file=args.parent_status.name,
            bytes=args.parent_status.stat().st_size,sha256=file_sha(args.parent_status)),
        query_specs=specs,endpoint_nodes=nodes.tolist(),midpoint_intervals=mids.tolist(),
        evaluations=[],angular_returns=[],selected_query_calls=[],domains=[],
        chosen_directions=[],original_direction_documents=[],errors=[],
        original_model_returned=False,original_model_exit_code=None,
        original_exception=None,observation_complete=False,
        original_scientific_return_objects_not_replaced=True,
        extra_RHS_J_QR_projection_or_trial_calls=0,
        post_model_scientific_diagnostic_not_run_by_this_observer=True,
        original_warm_schema_and_mathematical_source_set_unchanged=True)
    require(state["source_input_warm"]["sha256"]==args.expected_resume_sha and
        state["source_parent_status"]["sha256"]==args.expected_parent_status_sha,
        "Bind this actual complete parent pair")
    phase={"kind":None}
    serial=[0]

    def ensure():
        # The original engine alone establishes its fresh-output guard.
        require(args.out.is_dir(),"Original engine has not created its output directory")
        root.mkdir(exist_ok=True)
        return root

    def receipt(path):
        return dict(file=path.relative_to(root).as_posix(),
            bytes=path.stat().st_size,sha256=file_sha(path))

    def write_json(name,value):
        base=ensure();path=base/name
        raw=canonical(value);tmp=path.with_suffix(path.suffix+".partial")
        tmp.write_bytes(raw);tmp.replace(path)
        return receipt(path)

    def save_arrays(label,**arrays):
        base=ensure();serial[0]+=1
        path=base/(str(serial[0]).zfill(6)+"-"+label+".npz")
        require(not path.exists(),"Never overwrite an original observed array file")
        supplied={key:np.ascontiguousarray(value).copy() for key,value in arrays.items()}
        with path.open("xb") as stream:
            np.savez(stream,**supplied)
        return dict(**receipt(path),arrays={key:dict(dtype=value.dtype.str,
            shape=list(value.shape),order="C",raw_bytes=value.nbytes,
            raw_sha256=sha(value.tobytes(order="C")))
            for key,value in supplied.items()})

    def array_identity(value):
        a=np.ascontiguousarray(value)
        return dict(dtype=a.dtype.str,shape=list(a.shape),order="C",
            raw_bytes=a.nbytes,raw_sha256=sha(a.tobytes(order="C")))

    def scalar_word(value):
        return np.asarray(value,dtype="<f8").tobytes().hex()

    def flush():
        if args.out.is_dir():
            write_json("capture.json",state)

    def safe(label,callback):
        try:
            return callback()
        except Exception as error:
            item=dict(phase=label,error_type=type(error).__name__,error=repr(error),
                traceback=traceback.format_exc(),original_scientific_decision_unchanged=True)
            state["errors"].append(item)
            print(json.dumps(dict(event="request170_capture_error",**item),
                ensure_ascii=True,separators=(",",":")),flush=True)
            try:
                flush()
            except Exception:
                pass
            return None

    old_residual=entry.observed.OriginalCompleteResidual

    class ReturnedResidual(old_residual):
        def evaluate(self,coordinates,require_rms=False):
            result=super().evaluate(coordinates,require_rms=require_rms)
            def record():
                index=len(state["evaluations"])
                arrays={}
                for key in ("y","f"):
                    if key in result:
                        arrays[key]=np.asarray(result[key])[nodes]
                if "middle" in result:
                    arrays["middle"]=np.asarray(result["middle"])[mids]
                pack=save_arrays("evaluate-"+str(index),**arrays)
                item=dict(index=index,original_require_rms=bool(require_rms),
                    coordinates=array_identity(coordinates),
                    returned_array_packet=pack,
                    original_finite=result.get("finite"),
                    original_report_field_names=sorted((result.get("report") or {}).keys()),
                    original_RHS_and_middle_return_values_only=True)
                state["evaluations"].append(item)
                if isinstance(result.get("report"),dict):
                    result["report"]["R354_read_only_capture"]=dict(schema=SCHEMA,
                        evaluation_index=index,coordinates=item["coordinates"],
                        packet=pack,original_state_and_residual_words_unchanged=True)
                flush()
            safe("original-evaluate-return",record)
            return result

    original_angular=domain.angular.angular_values
    original_alias=domain.frozen.angular_values
    require(original_alias is original_angular,
        "Bind both actual aliases of the original angular_values")
    original_selected=domain.selected_actual_angles
    OriginalDomain=domain.ThirtySevenQueryDomainOperator
    original_run=entry._run_engine

    def angular_return(flow,station,query):
        result=original_angular(flow,station,query)
        if phase.get("kind") in ("domain-build","trial-selected"):
            def record():
                if np.iscomplexobj(query):
                    return
                record_index=len(state["angular_returns"])
                packet=save_arrays("angular-"+str(record_index),
                    query=query,first=result["first"],second=result["second"],
                    scalar=result["scalar"],beta=result["beta"],
                    cross_beta=result["cross_beta"])
                row=dict(index=record_index,context=dict(phase),
                    station_float64le=scalar_word(station),
                    query=array_identity(query),packet=packet,
                    original_normal_and_cross_expressions_separate=True)
                state["angular_returns"].append(row)
            safe("original-angular-values-return",record)
        return result

    def selected_return(problem,current):
        previous=dict(phase)
        tag=(current.get("report") or {}).get("R354_read_only_capture") or {}
        index=len(state["selected_query_calls"])
        phase.clear();phase.update(kind="trial-selected",selected_call=index,
            evaluation_index=tag.get("evaluation_index"))
        start=len(state["angular_returns"])
        try:
            result=original_selected(problem,current)
        finally:
            phase.clear();phase.update(previous)
        def record():
            arrays,reports=result
            state["selected_query_calls"].append(dict(index=index,
                evaluation_index=tag.get("evaluation_index"),
                original_reports=reports,
                actual_beta_arrays=save_arrays("selected-"+str(index),
                    beta=np.asarray(arrays,dtype=np.float64)),
                angular_return_indices=list(range(start,len(state["angular_returns"]))),
                original_result_returned_unchanged=True))
            flush()
        safe("original-selected-query-return",record)
        return result

    class ReturnedDomain(OriginalDomain):
        def __init__(self,problem,current,capture,*positional,**keywords):
            previous=dict(phase);index=len(state["domains"])
            phase.clear();phase.update(kind="domain-build",domain_index=index)
            start=len(state["angular_returns"])
            controls=[]
            profile=problem.flow.profile
            had="control_jets" in profile.__dict__
            old_instance=profile.__dict__.get("control_jets")
            original_controls=profile.control_jets

            def control_return(station):
                result=original_controls(station)
                def record():
                    controls.append(dict(observed_call_index=len(controls),
                        station_float64le=scalar_word(station),
                        packet=save_arrays("original-controls",controls=result)))
                safe("original-query-controls-return",record)
                return result

            profile.control_jets=control_return
            try:
                super().__init__(problem,current,capture,*positional,**keywords)
            finally:
                if had:
                    profile.control_jets=old_instance
                else:
                    del profile.control_jets
                phase.clear();phase.update(previous)

            def record():
                flow=self.flow;chart=self.chart
                packet=save_arrays("base-model",mesh=self._mesh,y=self._y,rhs=self._f,
                    scale=self._scale,inlet=chart.inlet,q_frequency=flow.q.freq,
                    endpoint_nodes=nodes,midpoint_intervals=mids)
                tag=(current.get("report") or {}).get("R354_read_only_capture") or {}
                row=dict(index=index,base_evaluation_index=tag.get("evaluation_index"),
                    B_model_sha256=self.model_sha256,base_identity=self.base_identity,
                    capture_description=capture.description(),
                    original_chart_description_copied_later_from_direction_document=True,
                    dimension=flow.dimension,M=flow.M,N=flow.q.N,n=flow.n,k=flow.k,
                    K=chart.K,free=chart.free,m=chart.m,physical_size=chart.physical_size,
                    coordinate_size=chart.size,
                    core_slice=[flow.core_slice.start,flow.core_slice.stop],
                    parameter_slice=[flow.parameter_slice.start,flow.parameter_slice.stop],
                    arrays=packet,controls=controls,queries=[],
                    angular_return_indices=list(range(start,len(state["angular_returns"]))),
                    original_q_jet_file=inspect.getsourcefile(flow.q.jet),
                    original_q_jet_source_sha256=file_sha(inspect.getsourcefile(flow.q.jet)),
                    original_q_unpack_file=inspect.getsourcefile(flow.q.unpack),
                    original_q_unpack_source_sha256=file_sha(inspect.getsourcefile(flow.q.unpack)),
                    original_q_unpack_text=inspect.getsource(flow.q.unpack),
                    same_node_different_A_chunk_words_not_collapsed=True,
                    endpoint_scalar_cache_observations=[])
                # No call to scalar_jets/base_jet/control_jets is made here.
                # Their actual original A-call cache entries already exist.
                # The original station identity includes shape and dtype bytes.
                cache=flow._base_cache
                for call in capture.calls:
                    matches=[]
                    for key,values in cache.items():
                        require(isinstance(key,bytes),"Original station-cache key is bytes")
                        if len(key)!=8*call["station_count"]:
                            continue
                        stations=np.frombuffer(key,dtype="<f8")
                        identity=domain.frozen.array_identity(stations)
                        if identity==call["stations"]:
                            matches.append((stations,values))
                    require(len(matches)==1,
                        "Bind each original A chunk to exactly one literal scalar-cache entry")
                    stations,values=matches[0]
                    baseline,control=values
                    require(np.asarray(baseline).shape==(len(stations),3) and
                        np.asarray(control).shape==(len(stations),3,3),
                        "Preserve all three returned scalar jets and all three controls")
                    require(np.all(np.isfinite(baseline)) and np.all(np.isfinite(control)),
                        "The existing endpoint scalar-cache words are finite")
                    packet0=save_arrays("endpoint-original-scalar-cache",
                        stations=stations,baseline=baseline,controls=control)
                    positions={}
                    for j in call["selected_intervals"]:
                        found=[]
                        for k in range(len(stations)-1):
                            if (stations[k:k+2].tobytes()==self._mesh[j:j+2].tobytes()):
                                found.append(k)
                        require(len(found)==1,
                            "The original A chunk contains one exact selected endpoint pair")
                        positions[str(j)]=dict(left=found[0],right=found[0]+1)
                    row["endpoint_scalar_cache_observations"].append(dict(
                        original_A_call_number=call["call_number"],
                        original_station_identity=call["stations"],
                        original_station_count=call["station_count"],
                        original_selected_intervals=call["selected_intervals"],
                        endpoint_positions=positions,packet=packet0,
                        original_scalar_jets_function_identity=capture.functions["original_scalar_jets"],
                        copied_existing_cache_without_any_new_scientific_call=True,
                        baseline_and_controls_are_literal_words_not_exact_profile_claim=True))
                require(len(row["endpoint_scalar_cache_observations"])==len(capture.calls),
                    "All actually captured A chunks have their literal scalar coefficients")
                for group,spec in enumerate(specs):
                    j=spec["interval"];query=self._queries[group]
                    endpoint=capture.records[j]
                    qp=save_arrays("base-query-"+str(group),query=query["value"],
                        left_J=endpoint["left"]["physical"],right_J=endpoint["right"]["physical"],
                        left_P=endpoint["left"]["parameter"],right_P=endpoint["right"]["parameter"])
                    weights=(list(self.hermite_weights) if spec["kind"]=="left-RMS"
                        else [.5,.125,.5,-.125])
                    identity_field=("scalar_control_jets" if spec["kind"]=="left-RMS"
                        else "original_scalar_control_jets")
                    explicit_identity=self.query_reports[group][identity_field]
                    row["queries"].append(dict(query_index=group,**spec,
                        original_explicit_scalar_control_identity=explicit_identity,
                        original_explicit_scalar_control_identity_field=identity_field,
                        explicit_identity_copied_from_original_B_query_report=True,
                        station_float64le=scalar_word(query["station"]),
                        h_float64le=scalar_word(query["h"]),
                        hermite_weights_float64le=[scalar_word(x) for x in weights],
                        packet=qp,endpoint_original_call_number=endpoint["call_number"],
                        endpoint_scalar_original_call_number=endpoint["call_number"],
                        endpoint_original_identities={side:endpoint[side]["identity"]
                            for side in ("left","right")}))
                row["actual_query_count"]=len(row["queries"])
                row["actual_control_return_count"]=len(controls)
                row["actual_base_angular_return_count"]=len(row["angular_return_indices"])
                row["all_control_return_calls_retained_without_deduplication"]=True
                row["total_control_call_count_not_assumed_equal_query_count"]=True
                state["domains"].append(row)
                flush()
            safe("completed-original-domain",record)

    def run_with_choose_observation():
        chosen=entry.engine.choose_feasible_descent
        previous_write=entry.engine.write

        def chosen_return(*positional,**keywords):
            result=chosen(*positional,**keywords)
            def record():
                current_domain=positional[0]
                z,action,Bz,report,rows=result
                state["chosen_directions"].append(dict(index=len(state["chosen_directions"]),
                    B_model_sha256=current_domain.model_sha256,
                    packet=save_arrays("actual-final-choice",z=z,action=action,Bz=Bz),
                    original_selection_report=report,
                    actual_complete_final_choice_not_LSMR_or_unselected_recovery=True))
                flush()
            safe("complete-final-choose-return",record)
            return result

        def write_return(path,value):
            result=previous_write(path,value)
            if Path(path).name=="direction-00.json.gz":
                def record():
                    state["original_direction_documents"].append(dict(
                        file=Path(path).name,bytes=Path(path).stat().st_size,
                        sha256=file_sha(path),packet=save_arrays("original-direction-words",
                            scaled_direction=np.asarray(value["actual_scaled_direction"],dtype="<f8"),
                            coefficient_direction=np.asarray(value["actual_coefficient_direction"],dtype="<f8")),
                        original_coordinates=value.get("coordinates"),
                        original_resume_sha256=value.get("resume_sha256"),
                        original_damping=value.get("damping"),
                        original_actual_direction_diagnostics=value.get("actual_direction_diagnostics"),
                        words_copied_from_original_engine_document_without_second_scaling=True))
                    flush()
                safe("original-direction-document-written",record)
            return result

        entry.engine.choose_feasible_descent=chosen_return
        entry.engine.write=write_return
        try:
            return original_run()
        finally:
            entry.engine.choose_feasible_descent=chosen
            entry.engine.write=previous_write

    entry.observed.OriginalCompleteResidual=ReturnedResidual
    domain.angular.angular_values=angular_return
    domain.frozen.angular_values=angular_return
    domain.selected_actual_angles=selected_return
    domain.ThirtySevenQueryDomainOperator=ReturnedDomain
    entry._run_engine=run_with_choose_observation
    try:
        result=observer.main()
        state["original_model_returned"]=True
        state["original_model_exit_code"]=result
        return result
    except BaseException as error:
        state["original_exception"]=dict(type=type(error).__name__,message=str(error))
        raise
    finally:
        entry.observed.OriginalCompleteResidual=old_residual
        domain.angular.angular_values=original_angular
        domain.frozen.angular_values=original_alias
        domain.selected_actual_angles=original_selected
        domain.ThirtySevenQueryDomainOperator=OriginalDomain
        entry._run_engine=original_run
        state["original_runtime_aliases_restored"]=True
        state["observation_complete"]=bool(state["original_model_returned"] and not state["errors"])
        safe("capture-final-write",flush)
        print(json.dumps(dict(event="request170_original37_capture_returned",schema=SCHEMA,
            original_model_returned=state["original_model_returned"],
            original_model_exit_code=state["original_model_exit_code"],
            original_exception=state["original_exception"],
            observation_complete=state["observation_complete"],
            evaluations=len(state["evaluations"]),angular_returns=len(state["angular_returns"]),
            domain_count=len(state["domains"]),actual_final_directions=len(state["chosen_directions"]),
            capture_errors=state["errors"],
            new_scientific_gate=False,diagnostic_arithmetic_not_run=True),
            ensure_ascii=True,separators=(",",":")),flush=True)


if __name__=="__main__":
    raise SystemExit(main())
