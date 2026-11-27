#!/usr/bin/env python3
"""Apply root rules 4,8,15 by terminal partial-clone git, without rewriting history."""
import os,json,re,hashlib,base64,subprocess,posixpath
from pathlib import Path
from datetime import datetime,timezone
ROOT="topics/invariant-subspace-problem/"
SESSION="Astra-ISP-8542378f-20261127"
RULES={"README.md":"282e86b03385d3b6245ce7100ae2e2af7b103c2d",ROOT+"README.md":"5fbd905291dd044c88d35bd9c07ac0e586ff795a"}
RUN=os.environ.get("GITHUB_RUN_ID","unknown");env=os.environ.copy()
env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+env["MR_TOKEN"]).encode()).decode())
repo=Path(env["RUNNER_TEMP"])/"isp-rule-correction-8542"
def run(args,check=True):
 r=subprocess.run(args,cwd=repo if repo.exists() else None,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if check and r.returncode:raise RuntimeError("command failed: "+args[0]+" "+str(r.returncode)+" "+r.stderr.decode("utf-8","replace")[-1600:])
 return r
def git(*args,check=True):return run(["git",*args],check)
def show(path,ref="HEAD"):return git("show",ref+":"+path).stdout
def head():return git("rev-parse","HEAD").stdout.decode().strip()
def write(path,data):
 p=repo/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data if isinstance(data,bytes) else data.encode());git("add","--sparse","--",path)
def stamp():return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
pulls=[]
def check_rules(before):
 after=head();actual={p:git("rev-parse",after+":"+p).stdout.decode().strip() for p in RULES}
 if actual!=RULES:
  print(json.dumps({"rulesChanged":True,"before":before,"after":after,"diff":git("diff",before,after,"--",*RULES).stdout.decode("utf-8","replace"),"mutationStopped":True}),flush=True)
  raise RuntimeError("Read changed README differences before resuming")
 pulls.append({"before":before,"after":after,"utc":stamp(),"rulesGitBlobs":actual,"rulesUnchanged":True});return after
if not repo.exists():run(["git","clone","--filter=blob:none","--no-checkout","--depth=1","https://github.com/Rogerhu12/math-research-public.git",str(repo)])
git("sparse-checkout","init","--no-cone")
git("sparse-checkout","set","--no-cone","/README.md","/"+ROOT+"README.md","/"+ROOT+"HANDOFF.md","/"+ROOT+"open.md","/"+ROOT+"log.md","/"+ROOT+"results.md")
git("checkout","main");git("config","user.name","Astra ISP 8542");git("config","user.email","astra-isp-8542@users.noreply.github.com")
before=head();git("pull","--rebase","origin","main");archive_commit=check_rules(before)
all_paths=git("ls-tree","-r","--name-only","HEAD","--",ROOT).stdout.decode().splitlines()
def payload(obj):
 if isinstance(obj,dict):
  for k,v in obj.items():
   if isinstance(v,str) and (k=="dataChunk" or (k in {"data","base64","payload"} and len(v)>200 and re.fullmatch(r"[A-Za-z0-9+/=\s]+",v))):return True
   if isinstance(v,(dict,list)) and payload(v):return True
 elif isinstance(obj,list):return any(payload(v) for v in obj if isinstance(v,(dict,list)))
 return False
deleted={}
def without_payload(obj):
 if isinstance(obj,dict):
  out={}
  for k,v in obj.items():
   if isinstance(v,str) and (k=="dataChunk" or (k in {"data","base64","payload"} and len(v)>200 and re.fullmatch(r"[A-Za-z0-9+/=\s]+",v))):
    out[k+"Omitted"]={"characters":len(v),"encodedTextSHA256":hashlib.sha256(v.encode()).hexdigest()}
   else:out[k]=without_payload(v)
  return out
 if isinstance(obj,list):return [without_payload(v) for v in obj]
 return obj
for path in all_paths:
 name=path.rsplit("/",1)[-1]
 if not path.startswith(ROOT+"notes/") or "8542" not in name or not name.endswith(".json"):continue
 raw=show(path)
 try:obj=json.loads(raw)
 except (ValueError,UnicodeDecodeError):continue
 split=bool(re.search(r"\.part[-.]?\d+|exact-part-\d+",name))
 generated=bool(re.search(r"(exact-input|retained-exact-parameters|characteristic-exact-input)",name)) and "manifest" not in name
 encoded=payload(obj)
 if encoded and not split and not generated and ("receipt" in name or "execution" in name):
  cleaned=without_payload(obj)
  cleaned["dataPolicyCorrection"]={"originalRecordSHA256":hashlib.sha256(raw).hexdigest(),"existingExecutionMetadataPreserved":True,"regenerablePayloadRemoved":True}
  data=json.dumps(cleaned,ensure_ascii=False,indent=2).encode()+b"\n"
  assert len(data)<100000;write(path,data);continue
 if not (split or encoded or generated):continue
 deleted[path]={"gitBlob":git("rev-parse",archive_commit+":"+path).stdout.decode().strip(),"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
 git("rm","--cached","--sparse","--",path)
 p=repo/path
 if p.exists():p.unlink()
manifest_path=ROOT+"notes/2026-11-28-historical-input-provenance-8542.json"
manifest={"schema":"isp-historical-input-provenance-v1","session":SESSION,"sourceCommit":archive_commit,
 "policy":"Root rules 8 and 15: no encoded/split cache in main. Existing historical inputs may be read by terminal git only; new work keeps source, definitions, run IDs and hashes.","files":deleted}
data=json.dumps(manifest,ensure_ascii=False,indent=2).encode()+b"\n";assert len(data)<100000;write(manifest_path,data)
format_count=0;link_count=0
def format_math(s):
 out=[];fence=False
 for line in s.splitlines(keepends=True):
  if line.lstrip().startswith(chr(96)*3) or line.lstrip().startswith("~~~"):fence=not fence;out.append(line);continue
  if not fence:line=line.replace("\\[","$$").replace("\\]","$$").replace("\\(","$").replace("\\)","$")
  out.append(line)
 return "".join(out)
for path in all_paths:
 if not path.endswith(".md") or path in RULES or path.endswith("/HANDOFF.md") or path.endswith("/open.md") or path.endswith("/log.md"):continue
 if not (path.startswith(ROOT+"results/") or (path.startswith(ROOT+"notes/") and "8542" in path.rsplit("/",1)[-1])):continue
 if re.search(r"(handoff|open-before|log-before|snapshot|archive)",path.rsplit("/",1)[-1],re.I):continue
 raw=show(path)
 if len(raw)>=100000:continue
 text=raw.decode()
 if SESSION not in text:continue
 revised=format_math(text)
 def relink(m):
  global link_count
  target=m.group(1)
  if "://" in target or target.startswith("#"):return m.group(0)
  full=posixpath.normpath(posixpath.join(posixpath.dirname(path),target))
  if full not in deleted:return m.group(0)
  link_count+=1
  return "](https://github.com/Rogerhu12/math-research-public/blob/"+archive_commit+"/"+full+")"
 revised=re.sub(r"\]\(([^)\s]+)\)",relink,revised)
 if revised!=text:
  if any(posixpath.basename(q) in text for q in deleted):
   notice="数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。\n\n"
   at=revised.find("\n")+1;revised=revised[:at]+"\n"+notice+revised[at:]
  assert len(revised.encode())<100000
  write(path,revised);format_count+=1
hpath=ROOT+"HANDOFF.md";h=show(hpath).decode()
write(ROOT+"notes/2026-11-28-handoff-before-data-policy-correction-8542.md",h)
line="- **数据规矩8/15已纠正：** 本会话可重算编码/分片载荷从main普通删除；只保源/定义/run/SHA及[历史定位](notes/2026-11-28-historical-input-provenance-8542.json)，以后不经工具搬数据。冻结源若需旧输入，用终端按该定位临时取回；不重写历史。"
if line not in h:h=h.replace("## 目标与规矩\n","## 目标与规矩\n\n"+line+"\n",1)
def update_h(text):
 p=pulls[-1]
 replacement="- **最近实际 pull / 已读规则提交：** "+p["after"]+"（"+p["utc"]+"，数据规矩修正run"+RUN+"真实pull --rebase，两README无差异）。记录：notes/root-terminal-pulls-8542/"+RUN+"-policy.json。"
 return re.sub(r"^- \*\*最近实际 pull / 已读规则提交：\*\*.*$",lambda m:replacement,text,flags=re.M)
h=update_h(h);assert len(h.encode())<10000;write(hpath,h)
op=show(ROOT+"open.md").decode()
notice="**数据保存范围纠正（2026-11-28）：** 下列旧时态的“已存参数/分片”只保其原运行历史；可重算载荷已按根规矩8/15从main移除。以后仅源、紧凑定义、run和SHA入库，旧输入的终端临时定位见[历史索引](notes/2026-11-28-historical-input-provenance-8542.json)。这不改变任何已证数学或未付范围。"
op=op.replace("\n","\n\n"+notice+"\n",1);write(ROOT+"open.md",op)
record_path=ROOT+"notes/root-terminal-pulls-8542/"+RUN+"-policy.json"
record={"schema":"isp-data-policy-correction-v1","session":SESSION,"run":RUN,"historicalSourceCommit":archive_commit,
 "deletedCacheFiles":len(deleted),"deletedCacheBytes":sum(r["bytes"] for r in deleted.values()),
 "markdownFilesCorrected":format_count,"historicalLinksCorrected":link_count,"ordinaryISPClaim":False,"rulesReads":pulls}
write(record_path,json.dumps(record,ensure_ascii=False,indent=2)+"\n")
log=show(ROOT+"log.md").decode().rstrip()
date=datetime.now(timezone.utc).timestamp()+8*3600;display=datetime.fromtimestamp(date,timezone.utc).strftime("%Y-%m-%d %H:%M")
log+="\n\n"+display+" Asia/Taipei｜"+SESSION+"\n- 纠正根规矩8/15：终端普通删除本会话"+str(len(deleted))+"份可重算输入缓存（"+str(record["deletedCacheBytes"])+"字节），只留小历史定位/源/定义/run/SHA，不新增编码或分片。\n- 根规矩4：修正本会话"+str(format_count)+"份说明的数学格式及旧数据链接，原数学身份不变；源需要历史输入时只在Actions临时用终端git取得。\n- 公开实际pull --rebase并检查两README；无强推、不改写已发表提交。普通ISP与全部未付分支继续。\n"
assert len(log.encode())<100000;write(ROOT+"log.md",log)
git("commit","-m","ISP: remove regenerable parameter caches and restore repository data rules")
while True:
 pushed=git("push","origin","HEAD:main",check=False)
 if pushed.returncode==0:break
 before=head();rebased=git("pull","--rebase","origin","main",check=False)
 if rebased.returncode:
  print(json.dumps({"rebaseConflict":True,"stderr":rebased.stderr.decode("utf-8","replace")[-1200:],"published":False}),flush=True)
  raise RuntimeError("Resolve recorded rebase conflict; no force push")
 check_rules(before);h=Path(repo/hpath).read_text();h=update_h(h);assert len(h.encode())<10000;write(hpath,h)
 record["rulesReads"]=pulls;write(record_path,json.dumps(record,ensure_ascii=False,indent=2)+"\n")
 git("commit","--amend","--no-edit")
print("ISP_DATA_POLICY_CORRECTION "+json.dumps({"publishedCommit":head(),"deletedCacheFiles":len(deleted),
 "deletedCacheBytes":record["deletedCacheBytes"],"markdownFilesCorrected":format_count,
 "manifest":manifest_path,"sourceCommitForHistoricalInputs":archive_commit,"rulesReads":pulls}),flush=True)
