#!/usr/bin/env node
/* RET84: complete text-only reconstruction of six terminal human-written notes.
   Reads only the six complete <100000-byte historical Markdown inputs through
   git show. It neither runs scientific code nor edits Git refs, requests,
   queues, source files, numerical inputs, checkpoints or reports.
   Optional archival use:
     node reproduce_terminal_run19_24_narratives_ret84.mjs --repository-root CHECKOUT --output-directory NEW_OUTPUT
   The complete old notes remain at the declared immutable commit. Network
   events are historical facts; this tool does not try to reproduce them.
*/
import {readFileSync,writeFileSync,mkdirSync} from "node:fs";
import {dirname,resolve} from "node:path";
import {execFileSync} from "node:child_process";
import {createHash} from "node:crypto";
const CONFIG=[
  {
    "run_label": 19,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md",
      "bytes": 96434,
      "git_blob_sha": "cb7298353531f198ad599445602e495bf51bc612",
      "restore_commit": "a7ee59c79535235b4161da7780b77556e9760940",
      "sha256": "d85678946701c763970a54928e581fc7dd98e9a7a401148c134e8d81ed3e54eb"
    },
    "block_labels": [
      "首次官方 run",
      "首次官方 jobs",
      "第一个必要输入的完整返回",
      "第二个必要输入的完整返回",
      "完整只读进度观察",
      "完整只读进度观察",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "科学自然返回及原 queue/pure 全对象",
      "准确 normal 的完整后继对象",
      "原 pure 的真实完整投影与缺项",
      "原完整索引/分卷身份"
    ],
    "terminal_text": "**已知终态：** run 46076669320/1 的 science 和 pure 都实际自然返回 0，最终工作点接受 4 步，但 reach 与 distance_plus 仍正。随后准确 normal 实际返回 1、未交回 report；内部异常原因仍未知。官方 workflow success 不改这项费用失败。后续完整事实保留于[终态与 normal 失败](2026-11-28-run19-complete-return-normal-fee-failure-and-continuation.md)及[真实失败边界和异常捕获入口](2026-11-28-actual-run19-normal-failure-and-complete-exception-entry.md)，两篇原件本次不改。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md",
      "bytes": 36583,
      "sha256": "36570166e8bfaa3326162b5a686a9437ab009c3e81b77625cb237ec2792f2b6e",
      "git_blob_sha": "b4f9906f360d7ac5ba71e2c3f2dba1217e144a54"
    }
  },
  {
    "run_label": 20,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md",
      "bytes": 93699,
      "git_blob_sha": "6c5f86daae94b925f0f23ba75c4617484f5e3c11",
      "restore_commit": "a7ee59c79535235b4161da7780b77556e9760940",
      "sha256": "118f35c8c0a10d6d0c73298bdb872c1076595973f9535b9ccc263aa1a4cb62d1"
    },
    "block_labels": [
      "首次官方 run/jobs",
      "第一个必要输入的完整返回",
      "原完整索引/分卷身份",
      "第二个必要输入的完整返回",
      "完整只读进度观察",
      "完整数学观察及来源身份",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "真实数学标量及六族",
      "原完整索引/分卷身份",
      "完整只读进度观察",
      "原完整索引/分卷身份",
      "官方取消 run/jobs 全对象",
      "原完整索引/分卷身份"
    ],
    "terminal_text": "**已知终态：** run 46079535427/1 官方在 2026-11-28 04:46:09Z 为 completed/cancelled，原因未知。最后观察的 current 接受数为 3，下一试点只有自身统计，完整科学 report、自然返回和 final/typed 未观察；原 pure 没有因官方终态变成已执行。末节保全部真实边界。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md",
      "bytes": 28230,
      "sha256": "0e283d2edaad4c3d0c7aadfe25acfc0dc515738876de22373f06fb13b14857b9",
      "git_blob_sha": "af46907423b19330db3567adb1233975db0915f0"
    }
  },
  {
    "run_label": 21,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run21-complete-five-eighths-launch-and-continuation.md",
      "bytes": 95194,
      "git_blob_sha": "eaa854edc501e1a0368e55b39cf9d98494844773",
      "restore_commit": "a7ee59c79535235b4161da7780b77556e9760940",
      "sha256": "d7446b6d74168a714b1157caefea22c6d79dcc9b3d352167ea8126febf205578"
    },
    "block_labels": [
      "原完整初始 queue 步骤",
      "首次官方 run 全对象",
      "首次官方 jobs 全对象",
      "原分卷身份",
      "第一个必要输入的完整返回",
      "原分卷身份",
      "第二个必要输入的完整返回",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "试点真实数学返回及缺项",
      "原完整索引/分卷身份",
      "完整只读进度观察",
      "原完整索引/分卷身份"
    ],
    "terminal_text": "**已知终态：** run 46084442413/1 官方在 2026-11-28 05:37:58Z 为 completed/cancelled，原因未知。当前初点接受数仍为 0，科学自然返回、完整 report 和 final/typed 未观察。[独立官方终态与最后完整观察](2026-11-28-run21-official-cancellation-and-last-complete-observation.md)原件本次不改；其固定旧前卷身份继续指向下面保全的 95,194 字节全文。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run21-complete-five-eighths-launch-and-continuation.md",
      "bytes": 26430,
      "sha256": "c13e6fd7399589183b12a6185fdd3a39a82523d005564af5af5b0738617cc3d9",
      "git_blob_sha": "8daa1e1977bbc9c8288503bfa45ed9f2ced1bbda"
    }
  },
  {
    "run_label": 22,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md",
      "bytes": 65324,
      "git_blob_sha": "d7a63157e3614ba573ce6b1fe638b7962306d68f",
      "restore_commit": "a7ee59c79535235b4161da7780b77556e9760940",
      "sha256": "ca64e480a1b6e20c00e600e678b114bc39e0e1132e9b8a49e52c091023ba1d61"
    },
    "block_labels": [
      "完整启动对象身份",
      "首次官方 run",
      "首次官方 jobs",
      "两个必要输入的完整实际记录与原分卷",
      "完整索引身份",
      "完整只读进度观察",
      "完整索引身份",
      "完整只读进度观察",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "试点真实数学标量",
      "原完整索引/分卷身份",
      "完整只读进度观察",
      "原完整索引/分卷身份",
      "第三接受点真实数学标量及六族",
      "原完整索引/分卷身份",
      "下一试点自身的实际观察",
      "原完整索引/分卷身份",
      "官方取消 jobs 全对象",
      "最后完整只读观察",
      "原完整索引/分卷身份"
    ],
    "terminal_text": "**已知终态：** run 46090913581/1 的 job 在 2026-11-28 06:51:08Z 为 completed/cancelled，原因未知。两必要输入确已返回 0，科学没有观察到自然返回；最后 current 接受数为 3，下一 480be 的几何、接受和最终 report/final/typed 未知。末节保留官方对象和最后观察各自的完整历史定位。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md",
      "bytes": 28032,
      "sha256": "bc6ab7f3d118910695e80e4a61b67003fd93c8d05ea566c9ac994efa758b8266",
      "git_blob_sha": "e44c6adc8e21764bd0fd71f3116d20ff163d3eb4"
    }
  },
  {
    "run_label": 23,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run23-complete-restoration-continuation-bhalf-launch-and-continuation.md",
      "bytes": 66558,
      "git_blob_sha": "2da87cf9e52a9c700749b0a8a762416470526131",
      "restore_commit": "a7ee59c79535235b4161da7780b77556e9760940",
      "sha256": "87c194f13156443ccd2be5bd14d0ea908de4faedf9e0f628dc6aced41ceaff1e"
    },
    "block_labels": [
      "首次官方 run/jobs 全对象",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "首接受点及下一试点数学标量",
      "原完整索引/分卷身份",
      "完整只读进度观察",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "491dae 自身数学观察",
      "原完整索引/分卷身份",
      "491dae 拒绝与344a0b自身统计",
      "原完整索引/分卷身份",
      "官方取消 jobs 全对象",
      "最后完整只读观察",
      "原完整索引/分卷身份"
    ],
    "terminal_text": "**已知终态：** run 46094430214/1 的 job 在 2026-11-28 07:32:27Z 为 completed/cancelled，原因未知。两必要输入确已返回 0；最后 current 接受数为 2，491dae 真实被拒，下一 344a0b 仅自身统计已返。科学自然返回、完整 report/final/typed 和该下一点几何/接受仍未知，不能从所选策略预填。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run23-complete-restoration-continuation-bhalf-launch-and-continuation.md",
      "bytes": 30742,
      "sha256": "8f0d9e2d333797be1991f9179b54c9b1eb573f0b4394c646f31d9cb81b5e4db8",
      "git_blob_sha": "5796f3bea62b96914f0d837c806c0e533504e6ee"
    }
  },
  {
    "run_label": 24,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run24-complete-halfwave-five-eighths-launch-and-continuation.md",
      "bytes": 57377,
      "git_blob_sha": "308666a08d7b0b98e58b48354d3d68ae211ef3af",
      "restore_commit": "a7ee59c79535235b4161da7780b77556e9760940",
      "sha256": "eb2e60fa43fdd91084434815327a5a3e40090c35b39a86829b21aa781155ce06"
    },
    "block_labels": [
      "首次官方 run 全对象",
      "首次官方 jobs 全对象",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "第一接受点完整数学标量",
      "原完整索引/分卷身份",
      "完整只读进度观察",
      "原完整索引/分卷身份",
      "原完整索引/分卷身份",
      "f725 拒绝与下一试点的完整数学观察",
      "原完整索引/分卷身份",
      "086003 自身实际观察",
      "原完整索引/分卷身份",
      "第三接受点完整数学标量",
      "原完整索引/分卷身份",
      "官方取消 jobs 全对象",
      "三个不同历史版本的完整索引身份"
    ],
    "terminal_text": "**已知终态：** run 46096380016/1 的 job 在 2026-11-28 07:56:19Z 为 completed/cancelled，原因未知。最后 current 086003 接受数为 3；下一 90c83f 仅自身统计已返，几何、接受和未投影的 alpha 未知。完整 science report、自然返回、final/typed 仍未观察，原 pure 不被改称已运行。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run24-complete-halfwave-five-eighths-launch-and-continuation.md",
      "bytes": 26413,
      "sha256": "b6b8779dcc0b43997e3721d94ccc679e7d920b92aa3da82b109d5d1a78459823",
      "git_blob_sha": "87e1fa6e70b93e5154937c93fae48825f4a6ac4a"
    }
  }
];
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
  const intro="## RET84：终态导读与完整历史记录\n\n"+c.terminal_text+"\n\n本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。"+count+" 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。\n\n**完整旧文件：** "+c.original.bytes+" 字节；SHA256 `"+c.original.sha256+"`；Git blob `"+c.original.git_blob_sha+"`；固定提交 `"+c.original.restore_commit+"`。[完整旧版]("+base+")。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET84 完整交付表](../computations/terminal-run19-24-narrative-retention-84-complete-delivery.json)。\n\n下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。\n\n";
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
process.stdout.write(JSON.stringify({schema:"terminal-human-narratives-ret84-text-reconstruction-v1",scientific_code_executed:false,git_refs_changed:false,files:completed})+"\n");
