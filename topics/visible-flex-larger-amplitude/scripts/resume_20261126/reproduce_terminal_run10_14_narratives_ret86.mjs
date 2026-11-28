#!/usr/bin/env node
/* RET86: complete text-only reconstruction of four terminal human-written notes.
   Reads only the four complete <100000-byte historical Markdown inputs through
   git show. It neither runs scientific code nor edits Git refs, requests,
   queues, source files, numerical inputs, checkpoints or reports.
   Optional archival use:
     node reproduce_terminal_run10_14_narratives_ret86.mjs --repository-root CHECKOUT --output-directory NEW_OUTPUT
   The complete old notes remain at the declared immutable commit. Network
   events are historical facts; this tool does not try to reproduce them.
*/
import {readFileSync,writeFileSync,mkdirSync} from "node:fs";
import {dirname,resolve} from "node:path";
import {execFileSync} from "node:child_process";
import {createHash} from "node:crypto";
const CONFIG=[{"note_id":0,"run_label":"10","original":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md","bytes":28909,"git_blob_sha":"546838f35b556015b6aed38a65c80800b23308d9","restore_commit":"0ff96dc0001b35cac2301f942e55292fe0f808ed","sha256":"1e9f274b14d10689f5d93f9f96b51f15e3526abfb0f0dc14960d425f1e31e9b5"},"block_labels":["官方 run 终态字段投影","官方 jobs 完整对象","原四个必要步骤的完整实际返回","最后完整同点进度观察","原三后继完整参数与未返回边界"],"terminal_text":"**已知终态：** 原 run10 已为 completed/cancelled，原因未知；只见四个必要步骤返回 0，完整科学、pure、最终 13 成员和 typed 未返回。新 Fejér 分支不补成原 run10 完成。本文完整终态、全部原源/参数/进度和未付责任保原文。","expected_output":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md","bytes":11054,"sha256":"a28df14293719d11cf5c8d018dddb6356fce3fb09119add856f22e8a646415d0","git_blob_sha":"58cdf85882382d23f7fe821ac21bcc417b94870d"}},{"note_id":1,"run_label":"12","original":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run12-actual-cancelled-without-scientific-return.md","bytes":22062,"git_blob_sha":"54b339f3c1ff338aac2378c84f48d7371617cc8c","restore_commit":"0ff96dc0001b35cac2301f942e55292fe0f808ed","sha256":"ef9e35d7a5280c8ace4680530952a58374db9745caa4657492c3e739f4d376d2"},"block_labels":["官方终态投影与完整 jobs","原索引和完整返回分卷身份","两个必要输入的完整实际记录","最后完整同点进度观察"],"terminal_text":"**已知终态：** run12 官方 completed/cancelled，原因未知。两必要输入实际返回 0；完整科学没有观察到自然返回，report/final/typed/pure 均不能据取消补成已完成。下文全部 48 原观察字段保其固定完整记录。","expected_output":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run12-actual-cancelled-without-scientific-return.md","bytes":9576,"sha256":"0b819f30fb426ce28769b4171d361bd5b7a7ef79d42f635f1dd736e19cb335d0","git_blob_sha":"1b6a398f3297f296a0f6f52241ab429b63f0c6eb"}},{"note_id":2,"run_label":"13","original":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-actual-normal-constructor-source-guard.md","bytes":24676,"git_blob_sha":"9c580305162154d2430fe1e06840ea26a5820d36","restore_commit":"0ff96dc0001b35cac2301f942e55292fe0f808ed","sha256":"558d14fcee888ab7e94dff462e551cdf873b3e61e1783d6e6f8c55cec194ea97"},"block_labels":["两个实际异常读取器的完整返回"],"terminal_text":"**已知后继终态：** 本文准确定位原 N4096 driver 的旧 schema 字面失配，保完整实际 traceback、pure 缺报告和最小修复边界。修后科学曾运行但未自然返回，run13/14 后来均官方 cancelled；原因未知。[两 run 独立终态](2026-11-27-runs13-14-actual-cancelled-without-complete-science.md)本次保持原字。","expected_output":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-actual-normal-constructor-source-guard.md","bytes":7269,"sha256":"c78f45a23ce0199359bd32db62a2f0a0e22bcdf2c83c3044a3f320c8ef051ef8","git_blob_sha":"cd742dc7f9c9463fdd08e8e78a1e0da2e2a84bc5"}},{"note_id":3,"run_label":"13/14","original":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-entry-failure-and-run14-actual-reference.md","bytes":21639,"git_blob_sha":"152fc29e9359502e3415688503606f3968594dbe","restore_commit":"0ff96dc0001b35cac2301f942e55292fe0f808ed","sha256":"1f2ae23384116cdc6e7c5acbabb0aba9b636c8196275705d2d8b7991325f37cb"},"block_labels":["两 run 的完整 maker/reference 实际记录","run13 science/pure 两次真实失败"],"terminal_text":"**已知后继终态：** 本文原 run13 science/pure 两次失败及 run14 输入成功均保其原真实来源和当时未知。随后实际异常在[normal 构造记录](2026-11-27-run13-actual-normal-constructor-source-guard.md)明确，两 run 后来官方 cancelled，未返回完整修后场；[独立终态记录](2026-11-27-runs13-14-actual-cancelled-without-complete-science.md)原字保留。","expected_output":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-entry-failure-and-run14-actual-reference.md","bytes":6378,"sha256":"3bca0f175dbc76fdf3e815a02188746a1bf936e2e6209d5b0ab4a249bb7d43e8","git_blob_sha":"ece8db426c0f5393397e0373d761b6ccb7559fe4"}}];
const bytes=s=>Buffer.byteLength(s,"utf8");
const sha256=s=>createHash("sha256").update(s,"utf8").digest("hex");
const gitblob=s=>createHash("sha1").update("blob "+bytes(s)+"\0","utf8").update(s,"utf8").digest("hex");
const build=function(original, c, sha256, bytes) {
  const re=/^```json[ \t]*\r?\n([\s\S]*?)^```[ \t]*(?:\r?\n|$)/gm;
  const base="https://github.com/Rogerhu12/math-research-public/blob/"+c.original.restore_commit+"/"+c.original.path;
  let count=0; const blocks=[], pieces=[]; let at=0;
  for (const m of original.matchAll(re)) {
    count++; if(!c.block_labels[count-1])throw Error("missing block label");
    const first=original.slice(0,m.index).split("\n").length;
    const last=first+m[0].split("\n").length-1-(m[0].endsWith("\n")?1:0);
    const replacement="> **原 JSON "+String(count).padStart(2,"0")+"："+c.block_labels[count-1]+"。** [固定旧版完整记录，第 "+first+"–"+last+" 行]("+base+"#L"+first+"-L"+last+")。\n\n";
    pieces.push(original.slice(at,m.index),replacement);at=m.index+m[0].length;
    blocks.push({ordinal:count,label:c.block_labels[count-1],first_line:first,last_line:last,fenced_bytes:bytes(m[0]),fenced_sha256:sha256(m[0]),json_bytes:bytes(m[1]),json_sha256:sha256(m[1]),replacement});
  }
  if(count!==c.block_labels.length)throw Error("block count");
  pieces.push(original.slice(at));
  let body=pieces.join("");
  const split=body.indexOf("\n\n");if(split<0)throw Error("title separator");
  const intro="## RET86：终态导读与完整历史记录\n\n"+c.terminal_text+"\n\n本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。"+count+" 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。\n\n**完整旧文件：** "+c.original.bytes+" 字节；SHA256 `"+c.original.sha256+"`；Git blob `"+c.original.git_blob_sha+"`；固定提交 `"+c.original.restore_commit+"`。[完整旧版]("+base+")。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET86 完整交付表](../computations/terminal-run10-14-narrative-retention-86-complete-delivery.json)。\n\n下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。\n\n";
  body=body.slice(0,split+2)+intro+body.slice(split+2);
  let restored=body.slice(0,split+2)+body.slice(split+2+intro.length);
  const ms=[...original.matchAll(re)];
  for(let i=0;i<blocks.length;i++){
    if(restored.split(blocks[i].replacement).length!==2)throw Error("replacement ambiguity");
    restored=restored.replace(blocks[i].replacement,ms[i][0]);
  }
  if(restored!==original)throw Error("narrative changed");
  return {text:body,blocks,intro};
};
function argumentsOf(argv){
  const keys=new Set(["--repository-root","--output-directory"]),out={};
  if(argv.length!==4)throw new Error("Use exactly --repository-root CHECKOUT --output-directory NEW_OUTPUT");
  for(let i=0;i<argv.length;i+=2){
    if(!keys.has(argv[i])||!argv[i+1]||Object.hasOwn(out,argv[i]))throw new Error("invalid argument");
    out[argv[i]]=argv[i+1];
  }
  if(Object.keys(out).length!==2)throw new Error("missing argument");
  return out;
}
const args=argumentsOf(process.argv.slice(2));
const repo=resolve(args["--repository-root"]),destination=resolve(args["--output-directory"]);
const completed=[];
for(const c of CONFIG){
  const r=c.original;
  if(r.bytes>=100000||!/^topics\/visible-flex-larger-amplitude\/notes\/[a-zA-Z0-9_.-]+\.md$/.test(r.path))throw new Error("not an authorized small note");
  const old=execFileSync("git",["show",r.restore_commit+":"+r.path],{cwd:repo,encoding:"utf8",maxBuffer:100000});
  if(bytes(old)!==r.bytes||sha256(old)!==r.sha256||gitblob(old)!==r.git_blob_sha)throw new Error("complete historical note mismatch: "+r.path);
  const output=build(old,c,sha256,bytes);
  const e=c.expected_output;
  if(bytes(output.text)!==e.bytes||sha256(output.text)!==e.sha256||gitblob(output.text)!==e.git_blob_sha)throw new Error("complete transformed note mismatch: "+r.path);
  const target=resolve(destination,r.path);
  if(!target.startsWith(destination+"/"))throw new Error("output escaped destination");
  mkdirSync(dirname(target),{recursive:true});
  writeFileSync(target,output.text,{encoding:"utf8",flag:"wx"});
  completed.push({path:e.path,bytes:e.bytes,sha256:e.sha256,git_blob_sha:e.git_blob_sha,complete_json_block_count:output.blocks.length});
}
process.stdout.write(JSON.stringify({schema:"terminal-human-narratives-ret86-text-reconstruction-v1",scientific_code_executed:false,git_refs_changed:false,files:completed})+"\n");
