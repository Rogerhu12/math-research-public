#!/usr/bin/env python3
"""Replay the actually completed but unpublished R106 native extraction/root jobs.
Run from topics/visible-flex-exact-nearby; the output directory must be new.
No geometry formula is changed. Old report SHA/time fields are not fabricated.
"""
from pathlib import Path
import argparse,gzip,hashlib,importlib.util,json,subprocess,sys

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir",type=Path,required=True)
    args=parser.parse_args()
    if args.out_dir.exists():
        raise ValueError("Use a new output directory; preserve earlier successful or partial reports")
    topic=Path.cwd()
    pinned={
      "fourfold_subprincipal_extract_saved_bulk_moduli.py":"5f905b4257e2e968623d87a8315ed035e4b1df37664cef1a407b459e5e0f7f3e",
      "fourfold_subprincipal_root_fields.py":"3a92a7ae5c8d66199ca2599be53590f91d976e89b05a24ec9ddab182367e8ac5",
    }
    for name,digest in pinned.items():
        if sha(topic/"scripts"/name)!=digest:
            raise ValueError("Frozen source changed: "+name)
    args.out_dir.mkdir(parents=True)
    path=topic/"scripts/fourfold_subprincipal_extract_saved_bulk_moduli.py"
    spec=importlib.util.spec_from_file_location("saved_bulk",path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    report=module.extract(topic)
    raw=(json.dumps(report,indent=2)+"\n").encode()
    bulk=args.out_dir/"saved_bulk_moduli.json.gz"
    bulk.write_bytes(gzip.compress(raw,mtime=0))
    summary={k:v for k,v in report.items() if k!="selected_spans"}
    summary["full_report"]={"path":str(bulk),"sha256":sha(bulk)}
    (args.out_dir/"saved_bulk_moduli_summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps({"completed":"saved_bulk","sha256":sha(bulk)}),flush=True)
    for mode,extra in [("point",["--point","1/16"]),("strip",["--strip","1/320","--angle-cells","128"])]:
        out=args.out_dir/("grounded_root_"+mode+(".json.gz" if mode=="strip" else ".json"))
        command=[sys.executable,str(topic/"scripts/fourfold_subprincipal_root_fields.py"),
                 "--mode",mode,*extra,"--out",str(out)]
        subprocess.run(command,check=True)
        print(json.dumps({"completed":mode,"sha256":sha(out)}),flush=True)
    files=[p for p in args.out_dir.iterdir() if p.is_file()]
    inventory={str(p):{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(files)}
    (args.out_dir/"replay_manifest.json").write_text(json.dumps({
      "kind":"actual_native_R106_replay","complete":True,"source_sha256":sha(__file__),
      "frozen_kernels":pinned,"files":inventory,
      "scope":"Complete original mathematical kernels rerun; no binary data reconstructed from summaries."},indent=2)+"\n")

if __name__=="__main__":
    main()
