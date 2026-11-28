"""Use the original runtime with one read-only download of each completed source."""
import hashlib
import json
import run_r625_paid_gauge_continuation_20261127 as launcher


original_preload=launcher.preload_paid_log


def single_event(raw,tag):
    marker=(" "+tag+" ").encode()
    rows=[line.split(marker,1)[1] for line in raw.splitlines() if marker in line]
    if len(rows)!=1:
        raise ValueError("Expected one paid event "+tag)
    return rows[0]


def both_logs(request):
    accepted_raw,receipt=original_preload(request)
    spec=request["paid_suffix_source"]
    startup_raw,startup_receipt=original_preload({"paid_source":spec})
    source=json.loads(single_event(startup_raw,"INVERSE_ACTIONS_SOURCE"))
    literal=single_event(startup_raw,spec["suffix_tag"])
    finished=json.loads(single_event(startup_raw,"INVERSE_ACTIONS_FINISHED"))
    if (source["source_commit"]!=spec["source_commit"] or str(source["run_id"])!=str(spec["run_id"])
            or source["request_bytes"]!=spec["request_bytes"] or source["request_sha256"]!=spec["request_sha256"]
            or source["request_path"]!=spec["request_path"] or len(literal)!=spec["suffix_json_bytes"]
            or hashlib.sha256(literal).hexdigest()!=spec["suffix_json_sha256"]
            or finished["returncode"]!=1):
        raise ValueError("Completed R674 startup, request, suffix or exit differs")
    receipt["prior_startup_preload"]=startup_receipt
    receipt["bound_previous_startup_suffix"]=json.loads(literal)
    receipt["prior_startup_child"]=finished
    return accepted_raw,receipt


if __name__=="__main__":
    # Delegate pinned pulls, source binding, environment and credential removal
    # to the established launcher. Only the pre-science receipt has two inputs.
    launcher.preload_paid_log=both_logs
    raise SystemExit(launcher.main())
