#!/usr/bin/env node
/* RET85: complete text-only reconstruction of nine terminal human-written notes.
   Reads only the nine complete <100000-byte historical Markdown inputs through
   git show. It neither runs scientific code nor edits Git refs, requests,
   queues, source files, numerical inputs, checkpoints or reports.
   Optional archival use:
     node reproduce_terminal_run15_18_narratives_ret85.mjs --repository-root CHECKOUT --output-directory NEW_OUTPUT
   The complete old notes remain at the declared immutable commit. Network
   events are historical facts; this tool does not try to reproduce them.
*/
import {readFileSync,writeFileSync,mkdirSync} from "node:fs";
import {dirname,resolve} from "node:path";
import {execFileSync} from "node:child_process";
import {createHash} from "node:crypto";
const CONFIG=[
  {
    "note_id": 0,
    "run_label": 18,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-producer-binding-repair-and-continuation.md",
      "bytes": 95805,
      "git_blob_sha": "06f5eb05935f91a7bb8972ca899d3a8047a1118c",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "62bcb336308a6e5220827052f76f9a13bed4246e05a3ebfcee178cbb58891098"
    },
    "block_labels": [
      "第三次入口失败的完整实际诊断返回",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整历史索引身份",
      "完整同点数学观察",
      "完整历史索引身份",
      "完整同点数学观察",
      "完整历史索引身份",
      "完整同点数学观察",
      "完整历史索引身份",
      "完整同点数学观察",
      "完整历史索引身份",
      "最后完整同点数学观察",
      "官方取消 run 全对象",
      "官方取消 jobs 全对象"
    ],
    "terminal_text": "**已知终态：** run 46062343475/1 最后官方状态为 completed/cancelled，run 的 updated_at 为 2026-11-28 02:05:35Z，取消原因未知。原三次入口失败及各自完整诊断照原时序保留；最终 producer-bound 族确曾进入完整科学。最后 current 接受数为 3、g 仍正；后续试点只有自身统计，完整科学自然返回、report/final/typed 及其几何/接受未知。末节的官方对象与观察各自保完整历史定位。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-producer-binding-repair-and-continuation.md",
      "bytes": 28004,
      "sha256": "16f9f6fd60baf7a47fd15d146ff033d4271b80290bd1898b4ddaca51f5557a61",
      "git_blob_sha": "d76ebb12ec24bda2f54788c48877fd5762f1dcb2"
    }
  },
  {
    "note_id": 1,
    "run_label": 17,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run17-wide-seed-actual-mathematics.md",
      "bytes": 81523,
      "git_blob_sha": "d3858027922738a6df247eb109ccfd9d45850b80",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "2bdbea9519316f03bd8680d99a381d691810a3f880106f868bfbcc5277b415fc"
    },
    "block_labels": [
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整实际数学与来源记录",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整历史索引身份",
      "完整同点数学观察",
      "完整历史索引身份",
      "完整同点数学观察",
      "官方终态与末索引的完整身份",
      "官方取消 run 全对象",
      "官方取消 jobs 全对象",
      "最后完整同点数学观察"
    ],
    "terminal_text": "**已知终态：** run 46053911348/1 最后官方状态为 completed/cancelled，run 的 updated_at 为 2026-11-28 00:53:34Z，取消原因未知。最后 current 接受数为 3、g 仍正，下一试点只见开始；完整科学自然返回、最终 report/final/typed 与下一点统计/几何/接受未知。此旧观测源没有实际六族 g 细目，不能借 run18 补入。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run17-wide-seed-actual-mathematics.md",
      "bytes": 22994,
      "sha256": "47d4602e47a3aa434b66a38fa57a17c843b790e2d54eb37bdf0f09e4f408c3c9",
      "git_blob_sha": "c34f3ca6509679696296863766f9c0f78afca52e"
    }
  },
  {
    "note_id": 2,
    "run_label": 16,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run16-initial-mathematics-and-point-bound-progress.md",
      "bytes": 67090,
      "git_blob_sha": "9ee3ab293f60a8a5db2ce4975e534686240f8966",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "0ea51fd23ef97f5e2767d44d348be4c586f688e34fac7172d1facba2c4ab522b"
    },
    "block_labels": [
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察",
      "完整同点数学观察"
    ],
    "terminal_text": "**已知终态：** run 46037017666/1 后来官方为 completed/cancelled，run 的 updated_at 为 2026-11-27 22:41:11Z；该时间不冒作精确 job 完成时间，取消原因未知。完整[官方终态与未返回边界](2026-11-27-run16-official-terminal-and-unreturned-observed-solve.md)保留。这里所有逐点统计仍按原观察时刻解释；最后所见 current 接受数为 0，试点不能冒接受点，科学完整自然返回、report/final/typed 未知。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run16-initial-mathematics-and-point-bound-progress.md",
      "bytes": 23744,
      "sha256": "9672dcf5116c03963dd579d14d563b2202b1d9c1293f6adfc3ff68127005ab08",
      "git_blob_sha": "b3764585030f52c1068d9426709212ee998b1bcd"
    }
  },
  {
    "note_id": 3,
    "run_label": 16,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run16-official-terminal-and-unreturned-observed-solve.md",
      "bytes": 56911,
      "git_blob_sha": "d578b6d0d555786d966f82311a740008a3fa8238",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "1bbd076534f038a753440deb67d13edb41c41c655411ca3c3880445528820a42"
    },
    "block_labels": [
      "官方 run 终态投影",
      "官方 jobs 全对象",
      "原完整科学与 pure 参数对象",
      "完整原索引/分卷/queue 身份",
      "maker 完整实际返回",
      "reference 完整实际返回",
      "最后完整同点进度观察",
      "原完整启动 request"
    ],
    "terminal_text": "**已知终态：** run 46037017666/1 官方为 completed/cancelled；2026-11-27 22:46:25Z 查询得到 run.updated_at=22:41:11Z，未把它当精确 job 完成时间。两个输入确已返回 0，科学没有观察到自然返回，pure/final/typed 没有被官方终态补成已完成。取消原因未知；原点、计数、所有试点和缺项按下文原时序保留。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run16-official-terminal-and-unreturned-observed-solve.md",
      "bytes": 17033,
      "sha256": "01927e4b9aa91c0cedc411cad40e8c0bcb2bc73cc893cb57a1fe9c68300859d7",
      "git_blob_sha": "2e8068f4873aeaf4a911751cc9532bc7dec081e2"
    }
  },
  {
    "note_id": 4,
    "run_label": 18,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-meridian-batched-independent-launch.md",
      "bytes": 53587,
      "git_blob_sha": "2bf31c348caf5808d6d801e41164d9e85c82bc2a",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "d5377d11be582ceecbdc7b1fa72d0a36f7dd744639346c7d7c1219e241abccd1"
    },
    "block_labels": [
      "完整启动对象身份",
      "原完整启动 request",
      "首次官方 run/jobs 观察",
      "首次科学入口失败完整返回",
      "首次真实异常完整诊断"
    ],
    "terminal_text": "**已知后继终态：** 本文原始 41b4/d3f1 入口实际失败，完整 frame/_meridian_data 异常和 traceback 原文保留。随后同一 run 46062343475/1 又经过两次不同的真实入口失败，再由 producer-bound 族进入科学，最终官方 cancelled；取消原因及完整最终场仍未知。完整后继记录见[producer 修复与终态](2026-11-27-run18-complete-producer-binding-repair-and-continuation.md)。后继进展不把本文失败源码改称成功。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-meridian-batched-independent-launch.md",
      "bytes": 16414,
      "sha256": "9e667a48526df02ca55466d5054844565b3bee29bc3c1f74fe9d0d0fdea005cc",
      "git_blob_sha": "b9a8840116785755cc9d8c5f3bd50ba1f7ee8b7f"
    }
  },
  {
    "note_id": 5,
    "run_label": 15,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run15-official-terminal-and-unreturned-radial-solve.md",
      "bytes": 45817,
      "git_blob_sha": "fc451c74235b3ef99b0c93a6f2934668ffaad213",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "abcfe72c86f71e5ab365234583b03cb742d163ba2b445ac01eeb9e581ec07530"
    },
    "block_labels": [
      "官方 run 终态投影",
      "官方 jobs 全对象",
      "原完整科学与 pure 参数对象",
      "最后完整同点进度观察",
      "原完整启动 request",
      "maker 完整实际返回",
      "reference 完整实际返回"
    ],
    "terminal_text": "**已知终态：** run 46031953783/1 官方为 completed/cancelled；2026-11-27 22:08:40Z 查询得到 run.updated_at=22:05:13Z，未把它当精确 job 完成时间，取消原因未知。两个输入确已返回 0，J1845 科学没有观察到自然返回。原 live 字段未给接受数/完整 metric/g，不以 normal 计数推这些值；report/final/typed/pure 仍未返回。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run15-official-terminal-and-unreturned-radial-solve.md",
      "bytes": 14089,
      "sha256": "81aaf3955f8a2d13b7ee538fa54863e004a9fa9abae592760a86be421ec78a1a",
      "git_blob_sha": "591ef6d98ae78481daeb1c57a71fa04fa7d4287b"
    }
  },
  {
    "note_id": 6,
    "run_label": 18,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-method-binding-repair-and-continuation.md",
      "bytes": 39152,
      "git_blob_sha": "0e1482a282f66891586301d24f9ea1499cba3dfb",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "f66194c1ef3791bff0a529e5453600f94cbad10ade90981466bb135d372c824c"
    },
    "block_labels": [
      "method-bound 科学入口失败完整返回",
      "第二次真实异常完整诊断"
    ],
    "terminal_text": "**已知后继终态：** 本文 method-bound 入口确实越过前一个 frame 错误，又实际以静态函数无 __func__ 的异常失败；两项真实错误和完整 traceback 均保原字。后续 callable 与 producer 修复各有独立真实身份，最终 run 46062343475/1 官方 cancelled，完整最终场未返回。见[producer 修复与终态](2026-11-27-run18-complete-producer-binding-repair-and-continuation.md)，不把后继事实倒填本文旧状态。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-method-binding-repair-and-continuation.md",
      "bytes": 20587,
      "sha256": "7a57e981826cae69fe717d4636850b5de6f30101a05cb78e02be91ee1e4e13c7",
      "git_blob_sha": "5a32c6774a88110e41ff66214fbad1ad78a6e0e3"
    }
  },
  {
    "note_id": 7,
    "run_label": 17,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run17-same-target-broader-supported-seed-launch.md",
      "bytes": 34073,
      "git_blob_sha": "13154a9a3e363d213aac6fa16b0af0496f661274",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "d394bbc6d4d960366a38f46fc85089106605880a335e12796b5bcd635006228d"
    },
    "block_labels": [
      "两个必要输入的完整实际返回"
    ],
    "terminal_text": "**已知后继终态：** 本文完整启动和两个真实输入返回属于 run 46053911348/1。其后科学有三次已观察接受，但仍有正 g，官方最终 cancelled；run.updated_at 为 2026-11-28 00:53:34Z，取消原因未知。完整实际数学、逐点来源与最终未知保在[同 run 的实际数学记录](2026-11-27-run17-wide-seed-actual-mathematics.md)。本文最初准备的 null 仍仅表达当时状态。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run17-same-target-broader-supported-seed-launch.md",
      "bytes": 21042,
      "sha256": "1fe349dc4d56a329bdcafcbdcdb6469144cafe75f28f98cc4efb75e21f35dfba",
      "git_blob_sha": "f80f08aafffe59aa8016a36935b35f105aa4be95"
    }
  },
  {
    "note_id": 8,
    "run_label": 18,
    "original": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-callable-binding-repair-and-continuation.md",
      "bytes": 21289,
      "git_blob_sha": "80d5855da4d011733cea0c59d6a1d638d6ecebba",
      "restore_commit": "1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4",
      "sha256": "618d0de64a57ba32c879c3bf5c041d214b79fe1a402d26e7c60e2d593547be2a"
    },
    "block_labels": [
      "callable-bound 科学入口失败完整返回"
    ],
    "terminal_text": "**已知后继终态：** 本文 callable-bound 源实际越过静态函数错误，却在 geometry 的 query-independent producer 守卫失败；下一记录明确实际原因是 geometry 仍钉旧 helper，未删守卫。完整[producer 修复与终态](2026-11-27-run18-complete-producer-binding-repair-and-continuation.md)保后续真实进展。最终 run 46062343475/1 官方 cancelled、完整最终场未返，本文旧错误未知段仍按当时知识保留。",
    "expected_output": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-callable-binding-repair-and-continuation.md",
      "bytes": 14062,
      "sha256": "c71de4a5e556e9ed225d4504c3563a4057b0d48acedd92d92b5a221a81624ada",
      "git_blob_sha": "408e87fcc729e9cf5afdf451ed0bd9de34f259da"
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
  const intro="## RET85：终态导读与完整历史记录\n\n"+c.terminal_text+"\n\n本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。"+count+" 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。\n\n**完整旧文件：** "+c.original.bytes+" 字节；SHA256 `"+c.original.sha256+"`；Git blob `"+c.original.git_blob_sha+"`；固定提交 `"+c.original.restore_commit+"`。[完整旧版]("+base+")。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET85 完整交付表](../computations/terminal-run15-18-narrative-retention-85-complete-delivery.json)。\n\n下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。\n\n";
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
process.stdout.write(JSON.stringify({schema:"terminal-human-narratives-ret85-text-reconstruction-v1",scientific_code_executed:false,git_refs_changed:false,files:completed})+"\n");
