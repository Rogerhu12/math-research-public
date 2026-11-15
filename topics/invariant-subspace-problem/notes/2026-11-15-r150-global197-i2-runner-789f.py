#!/usr/bin/env python3
"""2026-11-15. Author: ChatGPT (AI), literature_audit.

Seven complete polynomial batches for the full global I2(A).
Uses only the paid T96 / original 200 input arrays and the original17 model.
Every batch uses the same raw VQ section, all6188 source rows, p^3 original
products, the paid F/B DAG, the entire G quotient and all505/315 observations.
All large files are temporary in the job. No upload or archive is performed.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json, os, shutil, signal, struct, subprocess, sys, time
from pathlib import Path
sys.dont_write_bytecode = True

SOURCE_PINS = {
    "2026-11-15-r150-global197-i2-common-789f.hpp": "a871e1ddb8e06c9580351fad6f3275f9076a639cd7b251c28c50f53a08427519",
    "2026-11-15-r150-global197-i2-image-789f.cpp": "73b23703d5519afa2e6e75fa4f90b06f06d0dc3d1849e1771008f50d59ac24fd",
    "2026-11-15-r150-global197-i2-source-789f.cpp": "281907d42d90ba1666f8df20cc08b3f573f21c710387401cb2ddb7d3d2325f74",
    "2026-11-15-r150-global197-i2-transport-789f.cpp": "c2f195bb866a72923ecb7846b679f8c163a3ca60f29e58e199b003bc708f8aad",
    "2026-11-15-r150-global197-i2-original-789f.cpp": "8be9925cf90da48f8a7e6115d0d6b2d0374ce6de2ac92c1b9665d2b6def81afe",
    "2026-11-15-r150-global197-i2-normal-789f.cpp": "9b0eb1fa130ef556aa7179dcebbcdfb01fa1d260fe63f7051ff021bd6c4eeb89",
    "2026-11-15-r150-global197-i2-closure-789f.py": "9071f4a3b48fdf277a6cc6e7c65f5dc0b5aea213dd6cf0b4affffc1eccb1a471",
    "2026-11-14-r150-f31-bitplane-789f.hpp": "73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec",
    "2026-11-14-r150-torsion-characteristic-789f.py": "8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"
}
INPUT_MANIFEST_SHA = "a5d9cd78042fcbde42a6cc4fb8c740ce30b4064fb2be60f85b48b8c1db66aeac"
PREFIX = "2026-11-15-r150-global197-i2-"
LABELS = list(range(2, 33))
class BudgetStop(Exception):
    pass

def require(ok, message):
    if not ok:
        raise ValueError(message)

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for part in iter(lambda: f.read(1048576), b""):
            h.update(part)
    return h.hexdigest()

def ident(path):
    p = Path(path)
    return {"file": str(p.resolve()), "bytes": p.stat().st_size, "sha256": sha(p)}

def atomic(path, value):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(str(p) + ".tmp")
    tmp.write_bytes(canonical(value) + b"\n")
    os.replace(tmp, p)

def suffix(path, ending):
    return Path(str(path) + ending)

def identity(n, c=1):
    return [[[c] if i == j else [] for j in range(n)] for i in range(n)]

def select(old_count, high_numbers):
    polynomials = [[[] for _ in range(31)] for _ in range(old_count)]
    for j, high in enumerate(high_numbers):
        require(1 <= high <= old_count, "actual high source selection")
        polynomials[high - 1][j] = [1]
    return polynomials

def write_mix(path, labels, bound, families):
    text = ["R150_RHS_MIX_V1", "%d %d %d" % (len(labels), bound, len(families)), " ".join(map(str, labels))]
    for family in families:
        text.append("%s %s %s %s %d" % (family["nf"], family["q"], family["rem"], family["trace"], len(family["labels"])))
        text.append(" ".join(map(str, family["labels"])))
        for row in family["polys"]:
            for poly in row:
                pp = [int(a) % 31 for a in poly]
                while pp and not pp[-1]:
                    pp.pop()
                text.append(" ".join(map(str, [len(pp)] + pp)))
    path.write_text("\n".join(text) + "\n")

def write_original(path, labels, bound, families):
    text = ["R150_ORIGINAL_COMBINATION_V1", "%d %d 961 0 %d" % (len(labels), bound, len(families)), " ".join(map(str, labels))]
    for family in families:
        text.append("%s %d" % (family["file"], len(family["labels"])))
        text.append(" ".join(map(str, family["labels"])))
        for row in family["polys"]:
            for poly in row:
                pp = [int(a) % 29791 for a in poly]
                while pp and not pp[-1]:
                    pp.pop()
                text.append(" ".join(map(str, [len(pp)] + pp)))
    path.write_text("\n".join(text) + "\n")

def old_labels_and_zero_remainders(files):
    with files["oldK"].open("rb") as f:
        header = f.read(24 + 16 * 200)
    require(header[:8] == b"R150KK31" and struct.unpack_from("<4I", header, 8) == (31, 6188, 200, 85),
            "complete original200 source header")
    labels = []
    for i in range(200):
        _, label, cost, source, raw = struct.unpack_from("<IHHII", header, 24 + 16 * i)
        require(cost == (80 if i < 160 else 81 if i < 198 else 85)
                and 1 <= source <= 2195 and 1 <= raw <= 6188, "actual200 original source dictionary")
        labels.append(label)
    raw = files["oldRem"].read_bytes()
    require(raw[:8] == b"R150NF31" and struct.unpack_from("<3I", raw, 8) == (0, 200, 1034),
            "paid original200 remainder header")
    at = 20
    for i in range(200):
        r, label, count = struct.unpack_from("<IHI", raw, at); at += 10
        require(r == 0 and label == labels[i] and (i >= 198 or count == 0),
                "all first198 actual global first remainders zero")
        previous = 0
        for _ in range(count):
            c, length = struct.unpack_from("<HB", raw, at); at += 3
            require(previous < c <= 1034 and length >= 1, "actual old remainder dictionary")
            previous = c
            pp = raw[at:at + length]; at += length
            require(len(pp) == length and pp[-1] and all(v < 31 for v in pp), "actual old remainder field")
    require(at == len(raw) and len(set(labels)) == 200, "complete original200 remainder EOF")
    return labels

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs-root", type=Path, required=True)
    ap.add_argument("--input-manifest", type=Path, required=True)
    ap.add_argument("--sources-root", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seconds", type=float, default=600)
    ap.add_argument("--memory-mib", type=int, default=4096)
    ap.add_argument("--compile-seconds", type=int, default=45)
    ap.add_argument("--through", choices=("prepare", "batches", "final"), default="final")
    ap.add_argument("--max-new-batches", type=int, default=7)
    a = ap.parse_args()
    require(a.seconds > 0 and 1024 <= a.memory_mib <= 8192 and 0 <= a.max_new_batches <= 7,
            "explicit resources and batch limit")
    a.out = a.out.resolve(); a.sources_root = a.sources_root.resolve(); a.inputs_root = a.inputs_root.resolve()
    for path in (a.out, a.out / "inputs", a.out / "bin", a.out / "stages", a.out / "cache"):
        path.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    deadline = start + a.seconds
    rp = a.out / "global197-i2-pipeline-receipt.json"
    receipt = {"format": "r150-global197-original-i2-pipeline-v1", "status": "running",
               "prime": 31, "parameters": {"seconds": a.seconds, "memoryMiB": a.memory_mib,
               "through": a.through, "sourceCostBound": 177, "firstRHSCostBound": 81,
               "batchSize": 31, "activeColumns": 197, "stages": {}, "batches": []}}
    params = receipt["parameters"]
    child = None
    def save():
        receipt["elapsedSeconds"] = time.monotonic() - start
        atomic(rp, receipt)
    def time_left():
        return deadline - time.monotonic()
    def check_time(reserve=15):
        if time_left() <= reserve:
            raise BudgetStop("shared budget")
    def parent_stop(signum, frame):
        nonlocal child
        if child is not None and child.poll() is None:
            child.terminate()
            try:
                child.wait(timeout=12)
            except subprocess.TimeoutExpired:
                child.kill(); child.wait()
        raise BudgetStop("pipeline signal")
    signal.signal(signal.SIGTERM, parent_stop)
    signal.signal(signal.SIGINT, parent_stop)
    try:
        require(sha(a.input_manifest) == INPUT_MANIFEST_SHA, "frozen original input manifest")
        spec = json.loads(a.input_manifest.read_text())
        require(spec["sourceCount"] == 197 and spec["sourceHighKernelNumbersOneBased"] == [2, 198]
                and spec["originalProductModulus"] == 29791 and spec["originalProductDivisor"] == 961,
                "original global197 contract")
        sources = {}
        for name, expected in SOURCE_PINS.items():
            p = a.sources_root / name
            require(p.is_file() and sha(p) == expected, "frozen source: " + name)
            sources[name] = ident(p)
        params["sources"] = sources
        params["runnerSHA256"] = sha(__file__)
        params["inputManifestSHA256"] = INPUT_MANIFEST_SHA
        available = [p for p in a.inputs_root.rglob("*") if p.is_file()]
        files = {}
        all_specs = {**spec["files"], **spec["smallFiles"]}
        for name, expected in all_specs.items():
            check_time()
            aliases = set(expected["aliases"])
            aliases.update(x + ".gz" for x in list(aliases) if not x.endswith(".gz"))
            target = a.out / "inputs" / expected.get("logicalName", name + ".bin")
            if target.is_file() and target.stat().st_size == expected["bytes"] and sha(target) == expected["sha256"]:
                files[name] = target
                continue
            candidates = [p for p in available if p.name in aliases]
            found = None
            for p in candidates:
                if p.stat().st_size == expected["bytes"] and sha(p) == expected["sha256"]:
                    found = p.resolve(); break
                if p.suffix == ".gz":
                    tmp = Path(str(target) + ".tmp")
                    try:
                        with gzip.open(p, "rb") as inp, tmp.open("wb") as out:
                            shutil.copyfileobj(inp, out, 1048576)
                        if tmp.stat().st_size == expected["bytes"] and sha(tmp) == expected["sha256"]:
                            os.replace(tmp, target)
                            found = target; break
                    except (OSError, EOFError):
                        pass
                    finally:
                        if tmp.exists(): tmp.unlink()
            require(found is not None, "missing paid input (no recomputation): " + name)
            files[name] = found
        params["inputs"] = {name: ident(path) for name, path in files.items()}
        oldlabels = old_labels_and_zero_remainders(files)
        params["all198PaidGlobalFirstRemaindersZero"] = True
        semantic = {"format": "global197-i2-content-binding-v1", "runnerSHA256": params["runnerSHA256"],
                    "sources": SOURCE_PINS, "inputs": {k: v["sha256"] for k, v in params["inputs"].items()},
                    "highKernels": list(range(2, 199)), "batchSize": 31, "firstCost": 81, "sourceCost": 177,
                    "modulus": 29791, "divisor": 961, "rawVQ": True}
        binding = hashlib.sha256(canonical(semantic)).hexdigest()
        params["binding"] = binding
        binding_path = a.out / "binding.json"
        if binding_path.exists():
            require(json.loads(binding_path.read_text()) == semantic, "output checkpoint belongs to different original sources")
        else:
            atomic(binding_path, semantic)
        binaries = {}
        compile_info = {}
        for kind in ("image", "source", "transport", "original", "normal"):
            check_time(25)
            name = PREFIX + kind + "-789f.cpp"
            exe = a.out / "bin" / kind
            stamp = a.out / "cache" / ("compile-" + kind + ".json")
            key = {"sourceSHA256": SOURCE_PINS[name], "commonSHA256": SOURCE_PINS[PREFIX + "common-789f.hpp"],
                   "bitplaneSHA256": SOURCE_PINS["2026-11-14-r150-f31-bitplane-789f.hpp"],
                   "flags": ["-O3", "-std=c++17"] + (["-DR150_TARGETS=31"] if kind == "source" else [])}
            old = json.loads(stamp.read_text()) if stamp.exists() else {}
            if exe.is_file() and old.get("inputs") == key and old.get("sha256") == sha(exe):
                compile_info[kind] = {"status": "completed", "reused": True, "sha256": old["sha256"]}
            else:
                command = ["timeout", "--kill-after=5s", str(min(a.compile_seconds, int(time_left()-15)))+"s",
                           "prlimit", "--as="+str(a.memory_mib*1048576), "--core=0", "--",
                           "g++"] + key["flags"] + ["-I", str(a.sources_root), str(a.sources_root/name), "-o", str(exe)]
                t = time.monotonic()
                cp = subprocess.run(command, capture_output=True, text=True)
                (a.out / "stages" / ("compile-"+kind+".log")).write_text(cp.stdout+cp.stderr)
                require(cp.returncode == 0 and exe.is_file(), "bounded compile: "+kind)
                info = {"inputs": key, "sha256": sha(exe)}
                atomic(stamp, info)
                compile_info[kind] = {"status": "completed", "reused": False, "sha256": info["sha256"],
                                      "elapsedSeconds": time.monotonic()-t}
            binaries[kind] = exe
        params["compilations"] = compile_info
        save()
        if a.through == "prepare":
            receipt["status"] = "prepared"
            save()
            return 0

        def stage(name, kind, infile_list, outfiles, logical, command_factory, status, required):
            nonlocal child
            entry_inputs = {str(i): ident(p) for i, p in enumerate(infile_list)}
            key_payload = {"binding": binding, "kind": kind, "logical": logical,
                           "inputs": {k:v["sha256"] for k,v in entry_inputs.items()}}
            key = hashlib.sha256(canonical(key_payload)).hexdigest()
            cache = a.out / "cache" / (name+".json")
            old = json.loads(cache.read_text()) if cache.exists() else {}
            if old.get("inputBinding") == key and all(p.is_file() and old.get("outputs",{}).get(str(p)) == ident(p) for p in outfiles):
                last = old["nativeStatistics"]
                require(last.get("status") == status and all(last.get(k)==v for k,v in required.items()),
                        "completed native gate: " + name)
                params["stages"][name] = {"status":"completed","reused":True,"inputBinding":key,
                                          "nativeStatus":last["status"],"completedCache":ident(cache)}
                save()
                return
            check_time(25)
            remaining = time_left() - 15
            command = ["timeout", "--signal=TERM", "--kill-after=12s", "%.3fs"%remaining,
                       "prlimit", "--as="+str(a.memory_mib*1048576), "--core=0", "--"] + [str(v) for v in command_factory(remaining,key)]
            entry={"status":"running","inputBinding":key,"inputs":entry_inputs,"logical":logical}
            params["stages"][name]=entry; save()
            events=[]; t=time.monotonic()
            logpath=a.out/"stages"/(name+".log")
            with logpath.open("a") as log:
                child=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,
                                       stdin=subprocess.DEVNULL)
                for line in child.stdout:
                    log.write(line);log.flush()
                    try:
                        ev=json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(ev,dict):
                        events.append(ev);events=events[-4:]
                        entry["lastProgress"]=ev
                        print(json.dumps({"stage":name,"native":ev}),flush=True)
                code=child.wait()
            child=None
            last=events[-1] if events else {}
            entry.update(exitCode=code,elapsedSeconds=time.monotonic()-t,nativeStatistics=last)
            if code in (75,124,137,-15,-9):
                entry["status"]="budget-checkpoint";save()
                raise BudgetStop("native stage saved or stopped: "+name)
            require(code==0 and last.get("status")==status and all(last.get(k)==v for k,v in required.items())
                    and all(p.is_file() for p in outfiles),"native complete identity gate: "+name)
            outputs={str(p):ident(p) for p in outfiles}
            atomic(cache,{"inputBinding":key,"outputs":outputs,"nativeStatistics":last})
            params["stages"][name]={"status":"completed","reused":False,"inputBinding":key,
                                   "nativeStatus":last["status"],"elapsedSeconds":time.monotonic()-t,
                                   "completedCache":ident(cache)}
            save()
        def stage_prefix(bi, name):
            d=a.out/"stages"/("batch-%02d"%(bi+1))/name
            d.mkdir(parents=True,exist_ok=True)
            return d/name

        batches=[]; newly_completed=0
        for bi in range(7):
            active=list(range(2+31*bi,min(199,2+31*(bi+1))))
            batch_done=a.out/"cache"/("batch-%02d-completed.json"%(bi+1))
            existed=batch_done.exists()
            if not existed and newly_completed>=a.max_new_batches:
                raise BudgetStop("explicit new-batch limit reached")
            matrix=select(200,active)
            base=a.out/"stages"/("batch-%02d"%(bi+1))
            base.mkdir(parents=True,exist_ok=True)
            mix=base/"first.mix"
            firstfamily={"nf":files["oldNF"],"q":files["oldQ"],"rem":files["oldRem"],
                         "trace":files["oldTrace"],"labels":oldlabels,"polys":matrix}
            write_mix(mix,LABELS,81,[firstfamily])
            im=stage_prefix(bi,"first-image")
            stage("b%02d-first-image"%(bi+1),"image",
                  [files["graph"],files["oldNF"],files["oldQ"],files["oldRem"],mix],
                  [suffix(im,e) for e in ("-normal-forms.bin","-image-quotients.bin","-image-remainders.bin","-image-certificate.json")],
                  {"activeHighKernelNumbers":active,"firstCost":81},
                  lambda rem,key:[binaries["image"],files["graph"],mix,im],
                  "saved-quotient-mixture-complete",{"fullImageQuotientIdentity":True,"completeRHSInImage":True,"targets":31})
            vq=stage_prefix(bi,"raw-VQ")
            stage("b%02d-raw-VQ"%(bi+1),"source",
                  [files["graph"],files["originalNF"]]+[suffix(im,e) for e in ("-normal-forms.bin","-image-quotients.bin","-image-remainders.bin")],
                  [suffix(vq,e) for e in ("-standard-coefficients.bin","-source-certificate.json")],
                  {"sourceMode":"raw","bound":177,"activeHighKernelNumbers":active},
                  lambda rem,key:[binaries["source"],files["graph"],files["originalNF"],suffix(im,"-normal-forms.bin"),
                                  suffix(im,"-image-quotients.bin"),suffix(im,"-image-remainders.bin"),vq,key,"raw"],
                  "packed-image-source-convolution-complete",
                  {"fullNormalFormDecompositionIdentity":True,"rawPaidVQSectionPreserved":True,
                   "standardKernelNormalForm":False,"completeRHSInImage":True})
            tr=stage_prefix(bi,"q1-original")
            stage("b%02d-q1-original"%(bi+1),"transport",
                  [suffix(vq,"-standard-coefficients.bin"),files["model"],files["normalTrace"],files["forward"],files["backward"],
                   files["oldNF"],files["oldQ"],files["oldRem"],files["oldTrace"],mix],
                  [suffix(tr,e) for e in ("-primitive-source-mod31.bin","-original-transport.json")],
                  {"bound":177,"activeHighKernelNumbers":active},
                  lambda rem,key:[binaries["transport"],suffix(vq,"-standard-coefficients.bin"),files["model"],
                                  files["normalTrace"],files["forward"],files["backward"],mix,tr,
                                  tr.parent/"native-checkpoint",params["runnerSHA256"],rem],
                  "original-source-transport-complete",{"phase":5})
            trmeta=json.loads(suffix(tr,"-original-transport.json").read_text())
            require(trmeta.get("fullActualPrebasisTransport") is True and trmeta.get("targetCount")==31
                    and trmeta.get("provedSourceCostBound")==177 and max(trmeta["sourceCosts"])<=177,
                    "all raw q1 original costs")
            original=stage_prefix(bi,"divided-original")
            recipe=base/"second-divided.recipe"
            write_original(recipe,LABELS,177,[{"file":files["oldK"],"labels":oldlabels,"polys":matrix},
                                              {"file":suffix(tr,"-primitive-source-mod31.bin"),
                                               "labels":LABELS,"polys":identity(31,-31)}])
            stage("b%02d-divided-original"%(bi+1),"original",
                  [files["model"],files["integerModel"],files["oldK"],suffix(tr,"-primitive-source-mod31.bin"),recipe],
                  [suffix(original,e) for e in ("-primitive-source-mod29791.bin","-original-seventeen-source-mod29791.bin",
                                                "-divided-original-rhs.bin","-original-product.json")],
                  {"bound":177,"modulus":29791,"divisor":961,"activeHighKernelNumbers":active},
                  lambda rem,key:[binaries["original"],files["model"],files["integerModel"],recipe,original,key],
                  "full-original-combination-complete",{"divisor":961,"allOriginalProductCoefficientsDivisible":True})
            nf=stage_prefix(bi,"paid-normal")
            stage("b%02d-paid-normal"%(bi+1),"normal",
                  [files["model"],suffix(original,"-divided-original-rhs.bin"),files["forward"],files["backward"]],
                  [suffix(nf,e) for e in ("-normal-forms.bin","-reduction.bin","-forward.bin","-backward.bin")],
                  {"bound":177,"paidDAGOnly":True,"activeHighKernelNumbers":active},
                  lambda rem,key:[binaries["normal"],files["model"],suffix(original,"-divided-original-rhs.bin"),
                                  nf,key,files["forward"],files["backward"]],
                  "global197-i2-paid-normal-forms-complete",{"sources":0,"targets":31,"components":1034})
            require(sha(suffix(nf,"-forward.bin"))==spec["files"]["forward"]["sha256"]
                    and sha(suffix(nf,"-backward.bin"))==spec["files"]["backward"]["sha256"],
                    "paid original F/B byte identities after replay")
            finalmix=base/"second-image.mix"
            fresh={"nf":suffix(nf,"-normal-forms.bin"),"q":"-","rem":"-",
                   "trace":suffix(nf,"-reduction.bin"),"labels":LABELS,"polys":identity(31)}
            write_mix(finalmix,LABELS,177,[fresh])
            fim=stage_prefix(bi,"complete-G-image")
            stage("b%02d-complete-G-image"%(bi+1),"image",
                  [files["graph"],suffix(nf,"-normal-forms.bin"),finalmix],
                  [suffix(fim,e) for e in ("-normal-forms.bin","-image-quotients.bin","-image-remainders.bin","-image-certificate.json")],
                  {"bound":177,"allOriginalGComponents":1034,"activeHighKernelNumbers":active},
                  lambda rem,key:[binaries["image"],files["graph"],finalmix,fim],
                  "saved-quotient-mixture-complete",{"fullImageQuotientIdentity":True,"targets":31})
            entry={"batch":bi+1,"activeHighKernelNumbersOneBased":active,"paddedColumnCount":31-len(active),
                   "files":{"originalMetadata":ident(suffix(original,"-original-product.json")),
                            "imageMetadata":ident(suffix(fim,"-image-certificate.json")),
                            "imageRemainders":ident(suffix(fim,"-image-remainders.bin")),
                            "normalForward":ident(suffix(nf,"-forward.bin")),
                            "normalBackward":ident(suffix(nf,"-backward.bin")),
                            "firstMixture":ident(mix),"secondRecipe":ident(recipe)},
                   "binding":binding}
            atomic(batch_done,entry);batches.append(entry)
            if not existed:newly_completed+=1
            params["batches"]=batches;save()
        all_manifest={"format":"r150-global197-i2-complete-batches-v1","status":"completed","binding":binding,
                      "originalHighKernelNumbersOneBased":list(range(2,199)),
                      "paidForwardSHA256":spec["files"]["forward"]["sha256"],
                      "paidBackwardSHA256":spec["files"]["backward"]["sha256"],"batches":batches}
        allpath=a.out/"complete-batches.json";atomic(allpath,all_manifest)
        params["completeBatchManifest"]=ident(allpath)
        if a.through=="batches":
            receipt["status"]="batches-completed";save();return 0
        closure=a.out/"closure";closure.mkdir(exist_ok=True)
        stage("complete-global315-closure","closure",
              [allpath,files["state"],files["selector"],a.sources_root/"2026-11-14-r150-torsion-characteristic-789f.py"],
              [closure/"global197-i2-closure-receipt.json",closure/"complete-global197-i2-source-system.json.gz"],
              {"all197":True,"all505":True,"full315JClosure":True},
              lambda rem,key:[sys.executable,a.sources_root/(PREFIX+"closure-789f.py"),
                              "--batches",allpath,"--state",files["state"],"--selector",files["selector"],
                              "--reader",a.sources_root/"2026-11-14-r150-torsion-characteristic-789f.py",
                              "--out",closure,"--seconds",rem],
              "complete-global197-i2-closure",{})
        final=json.loads((closure/"global197-i2-closure-receipt.json").read_text())
        require(final.get("status")=="completed","actual final full315 closure")
        params["conclusion"]=final["parameters"]
        receipt["status"]="completed";save()
        print(json.dumps({"status":"complete-global197-original-I2",
                          "completeGlobalI2Dimension":final["parameters"]["completeGlobalI2Dimension"],
                          "completeCoefficientPrimeExponentTwoMultiplicity":final["parameters"]["completeCoefficientPrimeExponentTwoMultiplicity"],
                          "elapsedSeconds":time.monotonic()-start}),flush=True)
        return 0
    except BudgetStop as exc:
        receipt.update(status="budget-checkpoint",errorType=type(exc).__name__,error=str(exc))
        save()
        print(json.dumps({"status":"budget-checkpoint","error":str(exc),"elapsedSeconds":time.monotonic()-start}),flush=True)
        return 75
    except Exception as exc:
        receipt.update(status="failed",errorType=type(exc).__name__,error=str(exc))
        save()
        print(json.dumps({"status":"failed","errorType":type(exc).__name__,"error":str(exc)}),flush=True)
        return 1

if __name__=="__main__":
    raise SystemExit(main())
