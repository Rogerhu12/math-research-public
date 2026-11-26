#!/usr/bin/env python3
"""Publish a root-authored ordered manifest with real Git CLI pulls/rebases.

Only a temporary Actions branch runs this publisher. It performs no science.
MR_TOKEN is used only in process environment Git headers and API requests.
No token file, force push, raw-log upload, arbitrary path edit or shell command
from a manifest is supported. Every scientific/document change is a root-
specified immutable blob or a unique literal HANDOFF replacement.
"""
import ast
import base64
import datetime as dt
import difflib
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
import time
import urllib.request

PUBLIC = "Rogerhu12/math-research-public"
PRIVATE = "Rogerhu12/math-research"
TOPIC = "topics/visible-flex-new-mechanism"
HANDOFF = TOPIC+"/HANDOFF.md"
SELF_PATH = ".github/scripts/visible-flex-remote-cli-publisher-20261126.py"
WORKFLOW_PATH = ".github/workflows/visible-flex-remote-cli-publisher-20261126.yml"
SCHEMA = "visible-source-cli-publication-batch-v1"
PUBLIC_STAMP = re.compile(r"公开已读提交 \*\*[0-9a-f]{40}\*\*（[^）\n]*）")
PRIVATE_STAMP = re.compile(r"最后实际pull及规则同blob读至 \*\*[0-9a-f]{40}\*\*（[^）\n]*）")
MAX_FILE_BYTES = 2_000_000


class PublicationError(RuntimeError):
    pass


class PublicationCheckpoint(RuntimeError):
    pass


def require(ok, message):
    if not ok:
        raise PublicationError(message)


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00","Z")


def minute():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def emit(tag, value):
    value=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False)
    value=value.replace("::","\\u003a\\u003a").replace("##[","\\u0023\\u0023[")
    print("REMOTE_CLI_PUBLICATION_"+tag+" "+value,flush=True)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def path_ok(value):
    require(isinstance(value,str) and "\\" not in value and "\0" not in value,
            "invalid manifest path")
    p=PurePosixPath(value)
    require(not p.is_absolute() and str(p)==value and ".." not in p.parts
            and value not in (SELF_PATH,WORKFLOW_PATH,HANDOFF)
            and (value.startswith(TOPIC+"/") or value.startswith(".github/workflows/")),
            "manifest path outside the authorized topic/workflow scope")
    require(value not in (TOPIC+"/README.md",) and not value.endswith((".log",".zip",".npy",".npz"))
            and "/runlogs/" not in value,"rules/raw/large work products are not publication files")
    return value


def validate(manifest):
    require(manifest.get("schema")==SCHEMA and manifest.get("repository")==PUBLIC,
            "publication manifest schema/repository differs")
    require(manifest.get("queue_session")=="Astra-new-mechanism-0105020f-20261126",
            "publication queue session differs")
    require(set(manifest["expected_readme_blobs"])=={"README.md",TOPIC+"/README.md"},
            "public rules paths differ")
    require(set(manifest["expected_private_readme_blobs"])=={"README.md"},
            "private rules paths differ")
    for field in ("public_rules_read_commit","private_rules_read_commit"):
        require(re.fullmatch(r"[0-9a-f]{40}",manifest[field]) is not None,"invalid prior rule commit")
    for collection in ("expected_readme_blobs","expected_private_readme_blobs"):
        require(all(re.fullmatch(r"[0-9a-f]{40}",v) for v in manifest[collection].values()),
                "invalid expected README blob")
    require(isinstance(manifest["steps"],list) and 0<len(manifest["steps"])<=30,
            "publication batch needs one to thirty ordered steps")
    ids=set()
    for step in manifest["steps"]:
        require(re.fullmatch(r"[A-Za-z0-9_.-]{1,100}",step["id"]) is not None
                and step["id"] not in ids,"invalid or duplicate publication step id")
        ids.add(step["id"])
        require(isinstance(step["message"],str) and step["message"].strip()
                and "\0" not in step["message"] and len(step["message"])<=8000,
                "invalid root-authored commit message")
        require(isinstance(step["files"],list) and 0<len(step["files"])<=50,"invalid step file count")
        paths=set()
        for item in step["files"]:
            path=path_ok(item["path"])
            require(path not in paths,"duplicate file path within one step")
            paths.add(path)
            require(re.fullmatch(r"[0-9a-f]{40}",item["blob_sha"]) is not None,"invalid source blob SHA")
            old=item["expected_old_blob"]
            require(old is None or re.fullmatch(r"[0-9a-f]{40}",old) is not None,"invalid old blob identity")
            if "sha256" in item:
                require(re.fullmatch(r"[0-9a-f]{64}",item["sha256"]) is not None,"invalid optional SHA256")
            require(item.get("mode","100644") in ("100644","100755"),"unsupported file mode")
        require(isinstance(step.get("handoff_replacements"),list),"HANDOFF edits must be explicit")
        for item in step["handoff_replacements"]:
            require(set(item)=={"old","new"} and isinstance(item["old"],str)
                    and isinstance(item["new"],str) and item["old"] and "\0" not in item["old"]+item["new"],
                    "HANDOFF replacements need nonempty unique literal old and literal new")
    return manifest


class Publisher:
    def __init__(self, manifest, manifest_raw, folder, token):
        self.manifest,self.manifest_raw,self.token=manifest,manifest_raw,token
        self.manifest_hash=sha256(manifest_raw)
        self.folder=Path(folder)
        self.public,self.private=self.folder/"public",self.folder/"private"
        self.hooks=self.folder/"empty-hooks";self.hooks.mkdir()
        self.started=time.monotonic()
        self.deadline=self.started+2700
        self.public_record,self.private_record=None,None
        self.completed=[]
        self.current_step=None
        self.last_local_commit=None
        self.env=dict(os.environ)
        for name in list(self.env):
            if name.startswith(("GIT_CONFIG_","GIT_TRACE")) or name in (
                    "MR_TOKEN","GITHUB_TOKEN","GH_TOKEN","GIT_CURL_VERBOSE","GIT_ASKPASS","SSH_ASKPASS"):
                self.env.pop(name,None)
        self.env["GIT_TERMINAL_PROMPT"]="0"
        self.env["GIT_EDITOR"]="true"
        settings=[
            ("credential.helper",""),
            ("http.https://github.com/.extraheader","AUTHORIZATION: Basic "+base64.b64encode(("x-access-token:"+token).encode()).decode()),
            ("gc.auto","0"),("maintenance.auto","false"),("commit.gpgsign","false"),
            ("core.hooksPath",str(self.hooks)),("core.autocrlf","false")]
        self.env["GIT_CONFIG_COUNT"]=str(len(settings))
        for i,(key,value) in enumerate(settings):
            self.env["GIT_CONFIG_KEY_"+str(i)]=key
            self.env["GIT_CONFIG_VALUE_"+str(i)]=value
        name=manifest.get("commit_author_name","Codex research publisher")
        email=manifest.get("commit_author_email","codex-research@users.noreply.github.com")
        require(all(isinstance(x,str) and x and not any(c in x for c in "\r\n\0") for x in (name,email)),
                "invalid publication commit identity")
        self.env.update(GIT_AUTHOR_NAME=name,GIT_COMMITTER_NAME=name,
                        GIT_AUTHOR_EMAIL=email,GIT_COMMITTER_EMAIL=email)

    def check(self):
        if time.monotonic()>=self.deadline:
            raise PublicationCheckpoint("cooperative publisher clock; current manifest remains resumable")

    def git(self, root, *arguments, checked=True):
        self.check()
        result=subprocess.run(["git",*arguments],cwd=root,env=self.env,
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120,check=False)
        if checked and result.returncode:
            raise PublicationError("Git "+arguments[0]+" failed; output SHA256="+sha256(result.stdout+result.stderr))
        return result

    def text(self, root, *arguments):
        return self.git(root,*arguments).stdout.decode().strip()

    def blob_at(self, root, ref, path):
        result=self.git(root,"rev-parse","--verify",ref+":"+path,checked=False)
        if result.returncode:
            return None
        value=result.stdout.decode().strip()
        require(re.fullmatch(r"[0-9a-f]{40}",value) is not None,"invalid actual Git blob identity")
        return value

    def api_blob(self, blob_sha):
        self.check()
        require(re.fullmatch(r"[0-9a-f]{40}",blob_sha) is not None,"invalid API blob identity")
        request=urllib.request.Request("https://api.github.com/repos/"+PUBLIC+"/git/blobs/"+blob_sha,
            headers={"Authorization":"Bearer "+self.token,"Accept":"application/vnd.github+json",
                     "X-GitHub-Api-Version":"2022-11-28","User-Agent":"math-research-cli-publication"})
        with urllib.request.urlopen(request,timeout=90) as response:
            data=json.load(response)
        require(data.get("sha")==blob_sha and data.get("encoding")=="base64","API blob response identity differs")
        raw=base64.b64decode(data["content"],validate=False)
        require(len(raw)==data["size"] and len(raw)<=MAX_FILE_BYTES and git_blob_sha(raw)==blob_sha,
                "blob size or actual Git object hash differs")
        raw.decode("utf-8")
        return raw

    def clone(self):
        all_paths={"README.md",TOPIC+"/README.md",HANDOFF}
        for step in self.manifest["steps"]:
            all_paths.update(item["path"] for item in step["files"])
        self.git(self.folder,"clone","--filter=blob:none","--no-checkout","--branch","main",
                 "https://github.com/"+PUBLIC+".git",str(self.public))
        self.git(self.public,"sparse-checkout","init","--no-cone")
        self.git(self.public,"sparse-checkout","set","--no-cone",*["/"+p for p in sorted(all_paths)])
        self.git(self.public,"checkout","main")
        self.git(self.folder,"clone","--filter=blob:none","--no-checkout","--branch","main",
                 "https://github.com/"+PRIVATE+".git",str(self.private))
        self.git(self.private,"sparse-checkout","init","--no-cone")
        self.git(self.private,"sparse-checkout","set","--no-cone","/README.md","/QUEUE.md")
        self.git(self.private,"checkout","main")
        self.pull_both()

    def rule_check(self, root, old_ref, new_ref, expected, private=False):
        rows={}
        for path,expected_blob in expected.items():
            current=self.blob_at(root,new_ref,path)
            prior=self.blob_at(root,old_ref,path)
            if prior is None:
                self.git(root,"fetch","origin",old_ref)
                prior=self.blob_at(root,old_ref,path)
            old=self.git(root,"show",old_ref+":"+path).stdout
            new=self.git(root,"show",new_ref+":"+path).stdout
            diff="".join(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),
                fromfile=old_ref+":"+path,tofile=new_ref+":"+path))
            row={"expected_blob":expected_blob,"prior_blob":prior,"after_pull_blob":current,
                 "matches":current==expected_blob,"diff_bytes":len(diff.encode()),"diff_sha256":sha256(diff.encode())}
            if not private:
                row["diff"]=diff
            else:
                row["private_difference_not_published"]=True
            rows[path]=row
        emit("PRIVATE_RULES" if private else "PUBLIC_RULES",rows)
        require(all(row["matches"] and row["diff_bytes"]==0 for row in rows.values()),
                "README changed; root must read the exact new rules before further publication")

    def stamp_handoff(self, text):
        require(self.public_record is not None and self.private_record is not None,"real dual pull receipt absent")
        public=("公开已读提交 **"+self.public_record["remote_main_after"]+"**（"+
                self.public_record["minute"]+"；本次实际pull后根/题README空差异）")
        private=("最后实际pull及规则同blob读至 **"+self.private_record["remote_main_after"]+"**（"+
                 self.private_record["minute"]+"；实际pull成功，根README空差异、QUEUE仍本会话）")
        require(len(PUBLIC_STAMP.findall(text))==1 and len(PRIVATE_STAMP.findall(text))==1,
                "HANDOFF actual-pull anchor is not unique")
        text=PUBLIC_STAMP.sub(lambda _:public,text,count=1)
        text=PRIVATE_STAMP.sub(lambda _:private,text,count=1)
        require(len(text.encode())<10000,"HANDOFF exceeds the declared 10000-byte limit")
        return text

    @staticmethod
    def normalize_stamps(text):
        require(len(PUBLIC_STAMP.findall(text))==1 and len(PRIVATE_STAMP.findall(text))==1,
                "conflicting HANDOFF lacks unique read-stamp anchors")
        text=PUBLIC_STAMP.sub("公开已读提交 **"+"0"*40+"**（仅归一化读账）",text)
        return PRIVATE_STAMP.sub("最后实际pull及规则同blob读至 **"+"0"*40+"**（仅归一化读账）",text)

    def resolve_handoff_stamp_conflict(self):
        paths=self.text(self.public,"diff","--name-only","--diff-filter=U").splitlines()
        if paths!=[HANDOFF] or self.private_record is None:
            raise PublicationError("unresolved real rebase conflict paths="+json.dumps(paths))
        stages=[self.git(self.public,"show",":"+str(i)+":"+HANDOFF).stdout.decode() for i in (1,2,3)]
        normalized=[self.normalize_stamps(text) for text in stages]
        # Rebase stage 2 is new upstream, stage 3 is our manifest commit.
        with tempfile.TemporaryDirectory(prefix="handoff-merge-",dir=self.folder) as temp:
            paths3=[Path(temp)/name for name in ("base","upstream","manifest")]
            for path,text in zip(paths3,normalized):
                path.write_text(text)
            result=self.git(self.folder,"merge-file","-p",str(paths3[1]),str(paths3[0]),str(paths3[2]),checked=False)
        require(result.returncode==0,"HANDOFF has a non-read-stamp content conflict; no semantic overwrite attempted")
        merged=self.stamp_handoff(result.stdout.decode())
        (self.public/HANDOFF).write_text(merged)
        self.git(self.public,"add","--",HANDOFF)
        continued=self.git(self.public,"rebase","--continue",checked=False)
        require(continued.returncode==0,"rebase continuation has a further unresolved conflict")
        emit("HANDOFF_READ_STAMP_MERGED",{"only_conflict_path":HANDOFF,
            "non_stamp_text_merged_by_git_without_conflicts":True})

    def pull_public(self):
        before=self.text(self.public,"rev-parse","HEAD")
        prior=(self.public_record or {}).get("remote_main_after",self.manifest["public_rules_read_commit"])
        started=utc()
        result=self.git(self.public,"pull","--rebase","--no-autostash","origin","main",checked=False)
        # FETCH_HEAD is the actually fetched main, not an unpublished local
        # commit that would change its own identity when HANDOFF is amended.
        fetched=self.text(self.public,"rev-parse","FETCH_HEAD")
        self.rule_check(self.public,prior,fetched,self.manifest["expected_readme_blobs"])
        self.public_record={"actual_git_pull":True,"before":before,"remote_main_after":fetched,
            "started_at":started,"completed_at":utc(),"minute":minute(),
            "git_returncode_before_possible_conflict_resolution":result.returncode,
            "git_output_sha256":sha256(result.stdout+result.stderr)}
        if result.returncode:
            conflicts=self.text(self.public,"diff","--name-only","--diff-filter=U").splitlines()
            if conflicts:
                self.resolve_handoff_stamp_conflict()
            else:
                raise PublicationError("public actual pull failed without a resolvable HANDOFF conflict")
        self.public_record["local_head_after"]=self.text(self.public,"rev-parse","HEAD")
        emit("PUBLIC_PULL",self.public_record)

    def pull_private(self):
        before=self.text(self.private,"rev-parse","HEAD")
        prior=(self.private_record or {}).get("remote_main_after",self.manifest["private_rules_read_commit"])
        started=utc()
        self.git(self.private,"pull","--rebase","--no-autostash","origin","main")
        fetched=self.text(self.private,"rev-parse","FETCH_HEAD")
        self.rule_check(self.private,prior,fetched,self.manifest["expected_private_readme_blobs"],private=True)
        rows=[line for line in (self.private/"QUEUE.md").read_text().splitlines()
              if chr(96)+TOPIC+chr(96) in line]
        require(len(rows)==1 and "进行中" in rows[0] and self.manifest["queue_session"] in rows[0],
                "private QUEUE no longer uniquely records this session ongoing")
        self.private_record={"actual_git_pull":True,"before":before,"remote_main_after":fetched,
            "started_at":started,"completed_at":utc(),"minute":minute(),
            "queue_unique_and_ongoing":True,"private_contents_not_published":True}
        emit("PRIVATE_PULL",self.private_record)

    def pull_both(self):
        self.pull_public()
        self.pull_private()

    def published_step(self, step):
        manifest_line="Publication-Manifest: "+self.manifest_hash
        step_line="Publication-Step: "+step["id"]
        records=self.text(self.public,"log","origin/main","--format=%H",
            "--fixed-strings","--all-match","--grep="+manifest_line,"--grep="+step_line).splitlines()
        require(len(records)<=1,"duplicate manifest-step provenance already exists")
        if not records:
            return None
        commit=records[0]
        for item in step["files"]:
            require(self.blob_at(self.public,commit,item["path"])==item["blob_sha"],
                    "already published step has different file blobs")
        return commit


    def static_checks(self, prepared):
        """Parse sources/configuration only; never import or execute science."""
        pending={item["path"]:raw for item,raw in prepared}
        cache={}
        def source_bytes(path):
            p=PurePosixPath(path)
            require(not p.is_absolute() and str(p)==path and ".." not in p.parts
                    and ".git" not in p.parts,"unsafe static dependency path")
            if path in pending:
                return pending[path]
            if path not in cache:
                cache[path]=self.git(self.public,"show","HEAD:"+path).stdout
            return cache[path]
        reports=[]
        for item,raw in prepared:
            path=item["path"]
            if path.endswith(".py"):
                ast.parse(raw,filename=path)
                reports.append({"path":path,"stdlib_AST_parse":True,"module_imported_or_executed":False})
            if not path.endswith(".json"):
                continue
            value=json.loads(raw,parse_constant=lambda x:(_ for _ in ()).throw(ValueError("nonfinite JSON token")))
            record={"path":path,"JSON_parsed":True,"science_executed":False}
            if isinstance(value,dict) and "source_sha256" in value:
                bindings=value["source_sha256"]
                require(isinstance(bindings,dict),"request source_sha256 must be a mapping")
                trees={}
                for dependency,expected in bindings.items():
                    require(re.fullmatch(r"[0-9a-f]{64}",expected) is not None,"invalid request source SHA256")
                    actual_raw=source_bytes(dependency)
                    require(sha256(actual_raw)==expected,"request source binding differs: "+dependency)
                    if dependency.endswith(".py"):
                        trees[dependency]=ast.parse(actual_raw,filename=dependency)
                record["source_sha256_bindings_checked"]=len(bindings)
                if "entry_point" in value:
                    entry=value["entry_point"]
                    require(entry in trees,"request entry point is not a bound parsed Python source")
                    modules={PurePosixPath(p).stem:p for p in trees}
                    reachable=set()
                    def visit(path):
                        if path in reachable:return
                        reachable.add(path)
                        for node in ast.walk(trees[path]):
                            names=([x.name for x in node.names] if isinstance(node,ast.Import)
                                   else [node.module] if isinstance(node,ast.ImportFrom) and node.module else [])
                            for name in names:
                                if name in modules:visit(modules[name])
                    visit(entry)
                    options=set()
                    def argument_value(node,scope):
                        if isinstance(node,ast.Constant):return node.value
                        if isinstance(node,ast.Name) and node.id in scope:return scope[node.id]
                        if isinstance(node,ast.BinOp) and isinstance(node.op,ast.Add):
                            a,b=argument_value(node.left,scope),argument_value(node.right,scope)
                            if isinstance(a,str) and isinstance(b,str):return a+b
                        return None
                    def walk(node,scope):
                        if isinstance(node,ast.For):
                            try:values=ast.literal_eval(node.iter)
                            except (ValueError,TypeError):
                                # Option names can still be literal when a
                                # default value is a nonliteral expression.
                                values=([tuple(argument_value(x,scope) for x in row.elts)
                                         if isinstance(row,(ast.Tuple,ast.List))
                                         else argument_value(row,scope)
                                         for row in node.iter.elts]
                                        if isinstance(node.iter,(ast.Tuple,ast.List)) else None)
                            if isinstance(values,(tuple,list)):
                                names=([node.target.id] if isinstance(node.target,ast.Name)
                                       else [x.id for x in node.target.elts]
                                       if isinstance(node.target,(ast.Tuple,ast.List))
                                       and all(isinstance(x,ast.Name) for x in node.target.elts) else [])
                                for row in values:
                                    row=(row,) if len(names)==1 else row
                                    if names and isinstance(row,(tuple,list)) and len(row)==len(names):
                                        nested=dict(scope);nested.update(zip(names,row))
                                        for child in node.body:walk(child,nested)
                        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and node.func.attr=="add_argument":
                            for arg in node.args:
                                opt=argument_value(arg,scope)
                                if isinstance(opt,str) and opt.startswith("--"):options.add(opt)
                        for child in ast.iter_child_nodes(node):walk(child,scope)
                    for dependency in reachable:walk(trees[dependency],{})
                    require(bool(options),"no declared argparse options found for request entry/import graph")
                    cli={}
                    require(isinstance(value.get("common_parameters",{}),dict)
                            and isinstance(value.get("lanes"),dict),"request CLI mappings differ")
                    for lane,parameters in value["lanes"].items():
                        require(isinstance(parameters,dict),"lane parameters must be a mapping")
                        merged=dict(value.get("common_parameters",{}));merged.update(parameters)
                        flags=[];stdin=None
                        for name,parameter in merged.items():
                            require(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*",name) is not None,"invalid CLI option key")
                            option="--"+name.replace("_","-")
                            if name=="source_state_json":
                                require(isinstance(parameter,str),"source_state_json must be exact text")
                                json.loads(parameter,parse_constant=lambda x:(_ for _ in ()).throw(ValueError("nonfinite source JSON")))
                                flags.extend((option,"--source-state-sha256"))
                                stdin={"bytes":len(parameter.encode()),"sha256":sha256(parameter.encode())}
                            elif isinstance(parameter,bool):
                                if parameter:flags.append(option)
                            else:
                                # Existing entry wrappers serialize declared
                                # list/dict inputs (for example parent_guide)
                                # as one JSON argument; this is not execution.
                                require(isinstance(parameter,(str,int,float,list,dict)),"unsupported CLI parameter type")
                                if isinstance(parameter,(list,dict)):
                                    json.dumps(parameter,separators=(",",":"),allow_nan=False)
                                flags.append(option)
                        require(set(flags)<=options,"request CLI option not found in bound entry/import AST: "+
                                ",".join(sorted(set(flags)-options)))
                        cli[lane]={"options":flags,"source_state_stdin":stdin,"CLI_executed":False}
                    record["declared_CLI_static_check"]=cli
            reports.append(record)
        emit("STATIC_SOURCE_AND_REQUEST_CHECKS",reports)

    def prepare_step(self, step):
        self.current_step=step["id"]
        self.pull_both()
        prior=self.published_step(step)
        if prior:
            emit("STEP_ALREADY_PUBLISHED",{"id":step["id"],"commit":prior})
            self.completed.append({"id":step["id"],"commit":prior,"already_published":True})
            return False
        require(not self.text(self.public,"status","--porcelain"),"fresh publication checkout is not clean")
        prepared=[]
        for item in step["files"]:
            actual=self.blob_at(self.public,"HEAD",item["path"])
            require(actual==item["expected_old_blob"],
                    "expected old blob differs for "+item["path"]+"; actual="+str(actual))
            raw=self.api_blob(item["blob_sha"])
            if "sha256" in item:
                require(sha256(raw)==item["sha256"],"root-provided SHA256 differs: "+item["path"])
            prepared.append((item,raw))
        self.static_checks(prepared)
        text=(self.public/HANDOFF).read_text()
        for replacement in step["handoff_replacements"]:
            require(text.count(replacement["old"])==1,"HANDOFF literal replacement is not unique")
            text=text.replace(replacement["old"],replacement["new"],1)
        text=self.stamp_handoff(text)
        for item,raw in prepared:
            target=self.public/item["path"]
            require(not target.is_symlink() and not any(p.is_symlink() for p in target.parents if p!=self.public.parent),
                    "publication target traverses a symlink")
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(raw)
            target.chmod(int(item.get("mode","100644"),8)&0o777)
        (self.public/HANDOFF).write_text(text)
        paths=[item["path"] for item in step["files"]]+[HANDOFF]
        allowed=set(paths)
        actual=set(self.text(self.public,"diff","--name-only").splitlines())
        untracked=set(self.text(self.public,"ls-files","--others","--exclude-standard").splitlines())
        require((actual|untracked)<=allowed,"publication changed a non-manifest path")
        self.git(self.public,"add","--",*paths)
        message=step["message"].rstrip()+"\n\nPublication-Manifest: "+self.manifest_hash+"\nPublication-Step: "+step["id"]+"\n"
        with tempfile.NamedTemporaryFile(mode="w",prefix="publication-message-",dir=self.folder,delete=False) as handle:
            handle.write(message); message_path=Path(handle.name)
        try:
            self.git(self.public,"commit","--allow-empty","-F",str(message_path))
        finally:
            message_path.unlink()
        self.last_local_commit=self.text(self.public,"rev-parse","HEAD")
        emit("STEP_COMMITTED",{"id":step["id"],"local_unpublished_commit":self.last_local_commit,
            "files":[{"path":i["path"],"blob_sha":i["blob_sha"],"sha256":sha256(b),"bytes":len(b)}
                     for i,b in prepared]})
        return True

    def push_step(self, step):
        attempts=0
        while True:
            self.check()
            # On every non-fast-forward rejection this is the immediate next
            # operation: real pull --rebase, followed by current rule checks.
            self.pull_both()
            prior=self.published_step(step)
            if prior:
                self.completed.append({"id":step["id"],"commit":prior,"already_published_after_resync":True})
                emit("STEP_PUBLISHED",self.completed[-1])
                return
            ahead=int(self.text(self.public,"rev-list","--count","origin/main..HEAD"))
            require(ahead==1,"publication step is not exactly one unpublished commit after rebase")
            text=self.stamp_handoff((self.public/HANDOFF).read_text())
            (self.public/HANDOFF).write_text(text)
            require(set(self.text(self.public,"diff","--name-only").splitlines())<={HANDOFF},
                    "unexpected dirty path before HANDOFF amend")
            self.git(self.public,"add","--",HANDOFF)
            self.git(self.public,"commit","--amend","--no-edit")
            allowed={item["path"] for item in step["files"]}|{HANDOFF}
            require(set(self.text(self.public,"diff","--name-only","origin/main...HEAD").splitlines())<=allowed,
                    "rebased publication includes a non-manifest path")
            for item in step["files"]:
                require(self.blob_at(self.public,"HEAD",item["path"])==item["blob_sha"],
                        "rebase changed a root-specified file: "+item["path"])
            self.last_local_commit=self.text(self.public,"rev-parse","HEAD")
            attempts+=1
            result=self.git(self.public,"push","origin","HEAD:refs/heads/main",checked=False)
            if result.returncode==0:
                record={"id":step["id"],"commit":self.last_local_commit,"attempts":attempts,
                    "public_actual_pull":self.public_record,"private_actual_pull":self.private_record,
                    "handoff_blob":self.blob_at(self.public,"HEAD",HANDOFF),"completed_at":utc()}
                self.completed.append(record)
                emit("STEP_PUBLISHED",record)
                return
            output=(result.stdout+result.stderr).decode(errors="replace").lower()
            non_fast_forward=("non-fast-forward" in output or "fetch first" in output
                              or ("cannot lock ref" in output and "expected" in output)
                              or ("[rejected]" in output and "main" in output))
            emit("PUSH_REJECTED",{"id":step["id"],"attempts":attempts,
                "non_fast_forward":non_fast_forward,"output_sha256":sha256(result.stdout+result.stderr)})
            require(non_fast_forward,"push failed for a reason other than non-fast-forward; no force attempted")
            # No force, stale retry or API ref update: loop immediately pulls.

    def run(self):
        self.clone()
        for step in self.manifest["steps"]:
            if self.prepare_step(step):
                self.push_step(step)
        emit("BATCH_FINISHED",{"manifest_sha256":self.manifest_hash,"completed":self.completed,
            "wall_seconds":time.monotonic()-self.started,"scientific_computation_performed":False,
            "force_push_used":False,"private_repository_modified":False})


def main():
    token=os.environ.get("MR_TOKEN","")
    require(bool(token),"MR_TOKEN is required for the authorized CLI publisher")
    branch=os.environ.get("GITHUB_REF","")
    require(branch.startswith("refs/heads/") and branch!="refs/heads/main",
            "remote publisher must run only on a root-created temporary branch")
    blob=os.environ.get("PUBLISH_MANIFEST_BLOB","")
    expected=os.environ.get("PUBLISH_MANIFEST_SHA256","")
    require(re.fullmatch(r"[0-9a-f]{40}",blob) and re.fullmatch(r"[0-9a-f]{64}",expected),
            "invalid root-supplied immutable manifest identity")
    request=urllib.request.Request("https://api.github.com/repos/"+PUBLIC+"/git/blobs/"+blob,
        headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
                 "X-GitHub-Api-Version":"2022-11-28","User-Agent":"math-research-cli-publication"})
    with urllib.request.urlopen(request,timeout=90) as response:
        body=json.load(response)
    require(body.get("sha")==blob and body.get("encoding")=="base64","manifest blob response differs")
    raw=base64.b64decode(body["content"])
    require(len(raw)<=2_000_000 and sha256(raw)==expected and git_blob_sha(raw)==blob,
            "manifest byte/object identity differs")
    manifest=validate(json.loads(raw))
    if "runner_ref" in manifest:
        require(manifest["runner_ref"]==branch,"temporary runner branch differs from the manifest")
    emit("SOURCE",{"temporary_runner_ref":branch,"temporary_runner_commit":os.environ.get("GITHUB_SHA"),
        "publisher_source_sha256":sha256(Path(__file__).read_bytes()),"manifest_blob":blob,
        "manifest_sha256":expected,"manifest_steps":[step["id"] for step in manifest["steps"]],
        "MR_TOKEN_written_to_file":False,"scientific_execution":False})
    with tempfile.TemporaryDirectory(prefix="visible-cli-publisher-",dir=os.environ.get("RUNNER_TEMP")) as folder:
        publisher=Publisher(manifest,raw,folder,token)
        try:
            publisher.run()
        except Exception as error:
            emit("CHECKPOINT",{"type":type(error).__name__,"message":str(error)
                if isinstance(error,(PublicationError,PublicationCheckpoint)) else "transport/process error; credential-bearing details withheld",
                "manifest_sha256":expected,"completed":publisher.completed,
                "current_step":publisher.current_step,"last_local_unpublished_commit":publisher.last_local_commit,
                "public_actual_pull":publisher.public_record,"private_actual_pull":publisher.private_record,
                "not_a_completed_publication_batch":True})
            raise SystemExit(2) from None


if __name__=="__main__":
    try:
        main()
    except (PublicationError,PublicationCheckpoint) as error:
        emit("ERROR",{"type":type(error).__name__,"message":str(error)})
        raise SystemExit(2) from None
    except Exception as error:
        emit("ERROR",{"type":type(error).__name__,"message":"publisher initialization failed; transport details withheld"})
        raise SystemExit(2) from None
