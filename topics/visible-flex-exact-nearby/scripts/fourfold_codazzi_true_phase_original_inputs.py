"""Whole historical inputs for true root-to-waist phase validation.

All admission is metadata-only. The two original candidate shards stay intact.
The 193 complete repaired direction value bounds refer to the same negative
domain and parameter. No old solver, scalar fit or native producer is called.
"""
from fractions import Fraction
import gzip
import hashlib
import json

TOPIC = "topics/visible-flex-exact-nearby/"
MANIFEST = TOPIC + "notes/2026-11-15-R133-signed-nonmean-density-H3-CI-inputs.json"
MANIFEST_SHA = "f6e5f9fe938d897c2b57d3d34e42391455fc6cea9804576d4dcc90b2021a8351"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
ORIGINAL = "5e14fd1de48f7c51dbe465cebef048c3d948fc76"
REPAIR_COMMIT = "46f127c7153f5393dcd2a00f42d4c1d3662c294d"
CUT = Fraction(76285779072683,320000000000000)
DELTA = Fraction(9368259853002,10**23)
CONTROL = (Fraction(1,20),Fraction(9,50))
ALPHA = Fraction(6890507429876859,9007199254740992)


def check(value, message):
    if not value:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def admit(raw_manifest, read):
    check(len(raw_manifest)==97309 and sha(raw_manifest)==MANIFEST_SHA,"original SN parent manifest")
    manifest=json.loads(raw_manifest)
    paths=manifest["input_paths"]
    receipts={r["path"]:r for r in manifest["file_receipts"]}
    consumed=[]
    def get(path, binary=False):
        commit=manifest["historical_input_overrides"].get(path,manifest["historical_input_commit"])
        check(commit in (ORIGINAL,REPAIR_COMMIT) and path.startswith(TOPIC) and ".." not in path,
              "original immutable source location")
        s=receipts[path];raw=read(commit,path)
        check(len(raw)==s["bytes"] and sha(raw)==s["sha256"]==manifest["files"][path],
              "whole original bytes: "+path)
        consumed.append(dict(**s,commit=commit))
        return raw if binary else json.loads(gzip.decompress(raw) if path.endswith(".gz") else raw)
    cover,cache,direction,repair,index=[get(paths[r]) for r in
                                        ("scalar_cover","t_cache","direction","repair","candidate")]
    check(all(d["complete"] and d["actual_affine_parameter"]=="eta_0" and
              Fraction(d["exact_affine_offset"])==0 for d in (cover,cache,direction)),
          "same original physical intrinsic parameter")
    check(repair["complete"] and repair["corrected_value_and_all_angular_derivatives_continuous"]
          and repair["derived_definition_sha256"]==CENTRE and repair["candidate_sha256"]==CANDIDATE
          and receipts[paths["candidate"]]["sha256"]==CANDIDATE
          and direction["background_definition_sha256"]==CENTRE
          and direction["original_trial_sha256"]=="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
          and direction["derived_direction_definition_sha256"]==DIRECTION
          and direction["repair_input_sha256"]==receipts[paths["repair"]]["sha256"]
          and direction["scalar_cover_sha256"]==cache["cover_sha256"]==receipts[paths["scalar_cover"]]["sha256"]
          and Fraction(direction["exact_alpha"])==ALPHA and Fraction(index["metadata"]["exact_float_amplitude"])==ALPHA,
          "full repaired centre and all original physical response coordinates")
    check(cover["exact_complete_interval"]==direction["exact_phase_interval"]
          and list(map(Fraction,cover["exact_complete_interval"]))[0]==0
          and Fraction(cover["exact_complete_interval"][1])>=CUT
          and len(repair["exact_cumulative_coefficient_suprema"])==65
          and len(direction["complete_negative_interval_direction_coefficient_suprema"])==193
          and index["metadata"]["physical_frequency_factor"]==4
          and index["metadata"]["finite_state_angle"]=="moving phi",
          "whole qualified negative direction, scalar and candidate domains")
    parts=[]
    for i in (0,1):
        p=paths["candidate_part"+str(i)];b=get(p,True);s=index["parts"][i]
        check(s["bytes"]==len(b) and s["sha256"]==sha(b),"original candidate double identity")
        parts.append(b)
    rows=[]
    for g in cover["germs"]:
        q=g["path"];path=q if q.startswith(TOPIC) else TOPIC+q
        doc=get(path)
        check(receipts[path]["sha256"]==g["sha256"] and doc["complete"] and
              doc["configuration"]==cover["configuration"] and len(doc["rows"])==g["accepted_rows"],
              "complete accepted scalar germ and its original domain")
        rows.extend((tuple(map(Fraction,v["interval"])),g["sha256"],v) for v in doc["rows"])
    rows.sort(key=lambda item:item[0])
    check(len(cover["germs"])==169 and len(rows)==cover["accepted_cell_count"]==626
          and rows[0][0][0]==0 and rows[-1][0][1]>=CUT
          and all(a[0][1]==b[0][0] and a[0][0]<a[0][1] for a,b in zip(rows,rows[1:]))
          and rows[-1][0][0]<rows[-1][0][1],"gap-free original signed high-order scalar models")
    compact={tuple(map(Fraction,c["interval"])):c for c in cache["compact_T_models"]}
    check(cache["compact_T_complete"] and len(compact)==len(cache["compact_T_models"])==220
          and all(interval in compact and compact[interval]["scalar_native_sha256"]==digest
                  for interval,digest,_ in rows
                  if interval[0]<CONTROL[1] and interval[1]>CONTROL[0]),"same-piece compact T")
    check(len(consumed)==176 and len({s["path"] for s in consumed})==176,"all natural input receipts")
    return index,parts,repair,direction,rows,compact,consumed
