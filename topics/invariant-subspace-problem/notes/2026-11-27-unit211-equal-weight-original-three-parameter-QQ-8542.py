#!/usr/bin/env python3
"""New original equal-weight k,w,v QQ system with its actual Dval unit.
No data cache, no modular emptiness lift, no replay of a frozen algorithm input.
"""
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import tempfile
import time

DEPENDENCIES = {
  "2026-11-27-unit211-equal-weight-regular-original-chart-8542.js": "cfaa65b201c64aa7e7f019d955212b038260eb626a0b12a96856d9fd90e73e78",
  "2026-11-27-unit211-equal-weight-three-parameter-original-chart-8542.js": "183a3e4fd4f65d1a9e550fae35b606fb5b24384c7be495fa522e551e24aef9f3",
  "2026-11-27-unit211-equal-weight-three-parameter-original-NP-8542.js": "4bb99f9050bae866c30a5081579d0360e1bae1421d012304f111e0491f9c62fc",
  "2026-11-27-unit211-equal-weight-original-distinct-value-8542.js": "e23c1669cf2e717fc47e80f94e7d9e3517887d6500da2bfa7dea7f6691b03437",
  "2026-11-27-unit211-equal-weight-three-parameter-distinct-value-8542.js": "53d01debe7f7cb18deb1cf1247c0f8e49ad1f0c05ecac28a8a958340474a0576"
}
NAMES = {
  "regular": "2026-11-27-unit211-equal-weight-regular-original-chart-8542.js",
  "three": "2026-11-27-unit211-equal-weight-three-parameter-original-chart-8542.js",
  "np": "2026-11-27-unit211-equal-weight-three-parameter-original-NP-8542.js",
  "dregular": "2026-11-27-unit211-equal-weight-original-distinct-value-8542.js",
  "dthree": "2026-11-27-unit211-equal-weight-three-parameter-distinct-value-8542.js"
}
NODE_SOURCE = "const fs=require(\"fs\");\nconst [depdir,outfile]=process.argv.slice(2);\nconst run=(name,...args)=>(new Function(fs.readFileSync(depdir+\"/\"+name,\"utf8\")))(...args);\nconst names=JSON.parse(process.env.ISP_DEP_NAMES);\nconst regular=run(names.regular),chart=run(names.three,regular),np=run(names.np,regular),dr=run(names.dregular),dc=run(names.dthree,dr);\nconst out={original:true,variables:[\"k\",\"w\",\"v\"],rows:{E1:chart.rows.E1,N1:chart.rows.N1,Ns:np.rows.Ns,Ps:np.rows.Ps,Dval:dc.rows.Dval},sourceSeconds:{regular:regular.seconds,chart:chart.seconds,np:np.seconds,dregular:dr.seconds,dchart:dc.seconds}};\nfs.writeFileSync(outfile,JSON.stringify(out));\nconsole.log(\"ISP_ORIGINAL_INPUT \"+JSON.stringify({variables:out.variables,rows:Object.fromEntries(Object.entries(out.rows).map(([n,r])=>[n,{degrees:r.degrees,terms:r.terms,paid:r.paid,clearing:r.clearing}])),sourceSeconds:out.sourceSeconds}));"
SINGULAR_TEMPLATE = "ring ISP = 0,(v,k,w,s),dp;\noption(redSB);\npoly E = @@E1@@;\npoly N = @@N1@@;\npoly NS = @@Ns@@;\npoly PS = @@Ps@@;\npoly DVAL = @@Dval@@;\npoly A = k+w^2-2*w;\npoly MN = (w-1)*(w-k);\npoly POTHER = (2*MN-A)*v^2-3*k*A;\npoly UNITS = v*k*w*(w-1)*(w-k)*(k-1)*A*(v-1)*(v^2-k)*POTHER*DVAL;\nideal I = E,N,NS,PS,1-s*UNITS;\nprint(\"ISP_QQ_ORIGINAL_IDEAL_READY\");\nmatrix TRANSFORM;\nideal GB = liftstd(I,TRANSFORM);\nmatrix RETURN = matrix(I)*TRANSFORM-matrix(GB);\nif (RETURN != 0) { print(\"ISP_ORIGINAL_LIFT_FAILED\"); quit; }\nprint(\"ISP_ORIGINAL_LIFT_BACK_OK\");\nprint(\"ISP_GB_SIZE:\"+string(size(GB)));\nprint(\"ISP_GB_DIM:\"+string(dim(GB)));\nif (size(GB)==1 && GB[1]==1) { print(\"ISP_ORIGINAL_UNIT_IDENTITY_VERIFIED\"); }\nelse { print(\"ISP_NOT_A_UNIT_BASIS\"); }\nwrite(\"@@BASISFILE@@\",GB);\nwrite(\"@@TRACEFILE@@\",TRANSFORM);\nint j;\nint totalTerms=0;\nfor(j=1;j<=size(GB);j++){totalTerms=totalTerms+size(GB[j]);}\nprint(\"ISP_GB_TOTAL_TERMS:\"+string(totalTerms));\nif (totalTerms<1500) { print(\"ISP_SMALL_GB_BEGIN\"); print(GB); print(\"ISP_SMALL_GB_END\"); }\nquit;\n"
pin = os.environ["ISP_PIN"]
checkout = Path.cwd()
print("ISP_RUNTIME " + json.dumps({
    "node": subprocess.check_output(["node","--version"],text=True).strip(),
    "singular": subprocess.check_output(["Singular","--version"],text=True).splitlines()[0],
    "source_pin":pin,
}),flush=True)
with tempfile.TemporaryDirectory(prefix="isp-equal-original-") as td:
    task_dir=Path(td)
    for name, expected in DEPENDENCIES.items():
        raw=subprocess.check_output(["git","-C",str(checkout),"show",pin+":topics/invariant-subspace-problem/notes/"+name],timeout=120)
        actual=hashlib.sha256(raw).hexdigest()
        if actual!=expected:
            raise RuntimeError("Pinned dependency mismatch: "+name)
        (task_dir/name).write_bytes(raw)
    (task_dir/"build.cjs").write_text(NODE_SOURCE)
    env=os.environ.copy()
    env["ISP_DEP_NAMES"]=json.dumps(NAMES)
    started=time.monotonic()
    subprocess.run(["node",str(task_dir/"build.cjs"),str(task_dir),str(task_dir/"input.json")],env=env,check=True,timeout=120)
    inp=json.loads((task_dir/"input.json").read_text())
    def poly(row):
        terms=[]
        for exponents,coefficient in row["coefficients"]:
            factors=["("+coefficient+")"]
            for var,power in zip(("k","w","v"),exponents):
                if power:
                    factors.append(var+"^"+str(power))
            terms.append("*".join(factors))
        return "+".join(terms) or "0"
    code=SINGULAR_TEMPLATE
    for name,row in inp["rows"].items():
        code=code.replace("@@"+name+"@@",poly(row))
    code=code.replace("@@BASISFILE@@",str(task_dir/"basis.txt"))
    code=code.replace("@@TRACEFILE@@",str(task_dir/"trace.txt"))
    (task_dir/"original.sing").write_text(code)
    print("ISP_INPUT_IDENTITY "+json.dumps({
        "dependency_sha256":DEPENDENCIES,
        "original_input_sha256":hashlib.sha256((task_dir/"input.json").read_bytes()).hexdigest(),
        "singular_source_sha256":hashlib.sha256(code.encode()).hexdigest(),
        "build_seconds":time.monotonic()-started,
        "order":"dp on v,k,w,s","field":"QQ",
        "physical_units":"v*k*w*(w-1)*(w-k)*(k-1)*A*(v-1)*(v^2-k)*POTHER*DVAL",
        "algorithm":"one original liftstd with full transformation return",
        "singular_seconds":600,"singular_memory_bytes":4*1024**3,
    },sort_keys=True),flush=True)
    def limit():
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,)*2)
    started=time.monotonic()
    timed_out=False
    try:
        run=subprocess.run(["Singular","-q",str(task_dir/"original.sing")],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=600,preexec_fn=limit)
        output=run.stdout
        code_return=run.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out=True
        output=exc.stdout or b""
        if isinstance(output,bytes): output=output.decode("utf8","replace")
        code_return=None
    print(output,flush=True)
    receipt={
        "run_id":os.environ.get("GITHUB_RUN_ID"),"source_pin":pin,
        "elapsed_seconds":time.monotonic()-started,
        "source_exit_code":code_return,"timed_out":timed_out,
        "stdout_sha256":hashlib.sha256(output.encode()).hexdigest(),
        "stdout_bytes":len(output.encode()),
        "original_lift_returned":"ISP_ORIGINAL_LIFT_BACK_OK" in output,
        "unit_identity_returned":"ISP_ORIGINAL_UNIT_IDENTITY_VERIFIED" in output,
        "artifacts":{}
    }
    for name in ("basis.txt","trace.txt"):
        path=task_dir/name
        if path.exists():
            content=path.read_bytes()
            receipt["artifacts"][name]={"bytes":len(content),"sha256":hashlib.sha256(content).hexdigest(),"stored":False}
    print("ISP_QQ_EXECUTION_RECEIPT "+json.dumps(receipt,sort_keys=True),flush=True)
    if timed_out or code_return!=0 or not receipt["original_lift_returned"]:
        raise SystemExit(1)
