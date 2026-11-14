"""Finite geometry only: radial room before attempting a new cut's T root."""
import argparse
import copy
import importlib.util
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("room_family", HERE / "fd2d-wider-cut-prefix-screen.py")
wide = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wide)
fm = wide.fm


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--cut", type=float, required=True)
    p.add_argument("--wcut", type=float, required=True)
    p.add_argument("--pdeep", type=float, required=True)
    p.add_argument("--early-turn-curvature", type=float, default=3.4)
    p.add_argument("--vmid", type=float, nargs="+", required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    if a.output.exists():
        raise FileExistsError(a.output)
    source = json.loads(a.source.read_text())
    rows = []
    for vmid in a.vmid:
        bundle = wide.provisional_bundle(source, vmid, a.cut, a.wcut, 4/a.cut, a.pdeep)
        bundle["segments"][0]["L"] = .001
        turn = next(q for q in bundle["segments"] if q.get("label") == "early_shallow_return")
        turn.update(K=a.early_turn_curvature,
                    L=abs(turn["p1"]-turn["p0"])/(.92*a.early_turn_curvature))
        coast = next(q for q in bundle["segments"] if q.get("label") == "partial_return_matching_coast")
        coast["L"] = 0.
        deep = next(j for j,q in enumerate(bundle["segments"]) if q.get("label") == "final_deep_coast")
        brake = bundle["segments"][deep+1]
        short = copy.deepcopy(bundle)
        short["segments"] = short["segments"][:deep]
        prefix = fm.Candidate(short)
        radius_before_deep = prefix.segments[-1]["a_end"]
        brake_drop = fm.phase_integral(brake, 1.)
        available = radius_before_deep+brake_drop
        room = available-a.cut
        rows.append(dict(vmid=vmid,early_turn_curvature=a.early_turn_curvature,
                         radius_before_deep=radius_before_deep,
                         brake_length=brake["L"],brake_radial_change=brake_drop,
                         maximum_cut_at_zero_matching_coast=available,
                         radial_room=room,
                         maximum_positive_matching_coast=room/math.sin(.1),
                         feasible_radial_room=room>=0))
    out = dict(schema="fd2d-prefix-radial-room-v1",source_sha256=fm.digest(__file__),
               original_candidate_sha256=fm.digest(a.source),cut=a.cut,wcut=a.wcut,pdeep=a.pdeep,
               scope="Actual finite radial geometry from shared candidate formulas; no linear root, nonlinear solve or continuous interval certificate.",rows=rows)
    a.output.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out))


if __name__ == "__main__":
    main()
