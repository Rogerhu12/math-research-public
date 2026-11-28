# 第29组：原容量异常、完整发布等待修复与真实重启

日期：2026-11-28 UTC。会话：Astra-larger-e4e2a2bf-20261126。原运行 `46110194444/1` 已失败，本次是新的独立公开 runner。数学完成标准仍未达到；本记录不把编排修复当科学结论。

## 1. 已确认的原失败

原 run head `259814e67c1435016353a70bb9e9b7d7b2a8c7e7`，job `140871777584`，官方于 05:08:49Z completed/failure。原 whole job log 53972 B / SHA256 `e6d7253506bdcc37df4b588accad288c5db812fbd7a1c5da0a736312d24931cc`，先由只读公开诊断记录完整大小，再取该小文本全文核同。实际栈是第二输入 `finish_record` 调用 `Publisher.publish` 时抛出题目超过 200000000 B 的 RuntimeError。root 原预留空间不足；不是科学子程序拒绝或输入失败。

两个输入均实际 returncode=0。maker 为 5.783396263s，source `14fa94bbaac9dafaa6b7be3d06a32d940a8c1f04`，报告 65322 B / `7e17ee19a68931d044e2e34c4ea0eade6e485af81a330667028cd0d65670a41e`；reference 为 368.740189417s，source `748f083094eeb026231fa3e084eaa22e8968427f`，报告 84966 B / `01d21ecd3970c77608be9bdb70cd6a8cfe591ade9adbbc5fe7292da1ef4390aa`。第二输入只在原 job log 完整返回，原阶段分卷没有发布它，不补造旧分卷。没有观察到原科学步骤启动、模型、点或报告。

全部原命令、输入/输出身份、metrics、完整 trace 和官方 run/jobs 保在原完整说明的固定版本：

```json
{
  "original_run": "46110194444/1",
  "job_id": "140871777584",
  "official_conclusion": "failure",
  "official_completed_at": "2026-11-28T05:08:49Z",
  "actual_cause": "The topic exceeds the explicit 200 MB repository bound; preserve provenance and retire reproducible old raw before publication",
  "both_necessary_input_steps_returned_zero": true,
  "actual_mathematical_solver_start_or_report_observed": false,
  "complete_original_failure_note": {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run29-complete-r726-spherical-launch-and-continuation.md",
    "bytes": 73361,
    "sha256": "637477bc6a46a87c55344221d9a8a2ed784c10077428ec4da507416cb0a78d20",
    "git_blob_sha": "b1e22efdcf52a623732c7318d62abe90a1521f56",
    "fixed_publication_commit": "1302dbcfb0197b9541ddedd5c08c39bf3592fd5c"
  },
  "complete_original_job_log_metadata": {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run29-original-job-failure-metadata.json",
    "bytes": 8312,
    "sha256": "43c28f36a61564c4fa2c9902f77c154a04303cfffed895ceb8bdbd6c4203191a",
    "git_blob_sha": "ce551b98d1dcf3c80109d79d5d371e562ca74faf",
    "fixed_publication_commit": "7f057637d0a538556e753c816ec0ab2cb9f329b4"
  },
  "original_log_bytes": 53972,
  "original_log_sha256": "e6d7253506bdcc37df4b588accad288c5db812fbd7a1c5da0a736312d24931cc",
  "old_runner_inputs_or_raw_outputs_transferred": false,
  "original_failed_run_or_output_identities_relabelled": false
}
```

只读日志恢复 run `46111548660/1` 成功，其任务只读取原已完成日志。它不是重算或额外科学通过门。19 的 N exit1 和20的取消原因仍未知，不能用这次容量原因替代它们。

## 2. 完整修复及不变的责任

原控制器整个 `write_parallel_handoff` 与 `publish` 连续文本段替换为完整的新文本段。前后段和逐字反向恢复规则存入完整 MJS；段外源逐字不变。原始控制器完整保在 `259814e67c1435016353a70bb9e9b7d7b2a8c7e7`，大小19995 B / SHA256 `0ab835efc215f21291c10d1cec24a29460419d0f9e71e1b9db69e2a05ee3df01` / blob `9b9242db15f40902f37a2843ab7762d3560af5f1`。

新的 `parallel_handoff_text` 保原29槽的完整语义，但先返回文本。新的 `prepare_complete_publication` 每轮先真正 `git pull --rebase origin main`，按原规则只读双 README 的实际差异；完整渲染索引、全部阶段卷和 own slot，按当前整个题目目录字节数加每个完整文件的新旧差计算发布后总数。只有总数≤200000000且 HANDOFF<10000 B 时才写入完整候选文件。

空间暂不足时，每30秒真 pull 后重新计算。完整 pending 文件的路径、字节数、SHA256 和投影容量写入原 job 的事件日志；原 status、journal、科学输出、已完成步骤都保在原 runner。等待不缩卷、不丢 completed record、不发信号给科学 child、不把待发布记录计成已发布，也不改变科学参数或预算。等待时暂不产生新的轮询快照，故不宣称捕获每个瞬时进度；原完整步骤/报告的保留责任不变。原 GitHub 360分钟窗口仍有效，容量等待不是无限延长 job 的保证。

普通 push 非快进后仍立刻原 `sync` 做 rebase，再按合并后的完整树重新预检所有候选文件；有空间才 amend 当前尚未发表的普通提交并再次 push，成功才更新 published snapshot。没有 force push。原 other failure、child signal、源 worktree、followup、render、README 变更处理完全保留。原 60000 B 分卷、95000 B 索引、32768 B pretty progress 和64 selectors都不改。

本次没有新增 Python/AST、fixture、benchmark、数值重跑、审查或录取门。全段唯一替换及反替等式仅是完整文本的来源说明；实际源码按原公开执行入口执行。

## 3. 当前完整文件与原执行参数

| 完整文件 | B | SHA256 | Git blob |
|---|---:|---|---|
| `topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel29_geometry_locations.py` | 21888 | `abf54a1b323aa3b514f1b6b6e3b1310844c717b0f4f2fb064b02dda1280907ad` | `4e0919183ab256c34484e86035de326976262a65` |
| `topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-29.json` | 45534 | `d5e405ecf9e3d16f92e9d0fe1f3c9fdcaa211d0165acc73ce4b20ff43e26e397` | `5a6b187bdba3bc1326e1aaab8dee5714f8f9ae7f` |
| `topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_public_controller29_complete_capacity_wait.mjs` | 13096 | `b66bab9718ce1976ca09a1420999abf633ef341c1aa5fc91cbc9f63eedbd78fe` | `6d5ca68c953dd4b3e1bb3c720a89297bd3a5df8e` |
| `topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-29.json` | 74372 | `e16b8d782febeb5e0b70840b925003fdc6524ee6595f29b3fb1e9807a5dd717a` | `e46753d93f0c1ceb4d60a59e5a73e0cfdf0d32b8` |
| `.github/workflows/visible-larger-20261128-parallel29.yml` | 2207 | `0834dd557492e10730befea2844ae49facfb52967ff83d3d45398f3b5a916ffa` | `1cc478bb737ab2403bc9a08d42526ea4f00c7314` |

本提交替换当前 controller 和完整 request；完整 queue、workflow 不改。请求 `visible-larger-resume-20261128-29-retry1` 有59个完整顶层键，引用原54键的 whole request 和全部原历史。新 request 不是元数据片段；全部157/7 argv、458/445形式/解析参数、64 live selectors、5 CLI peer、15原数学 external及原28外部观察责任仍由原完整 ready/source/binding 固定。

科学源仍为 `7acb89983fe616fbba85cef74811625b357942e4` 的完整R726族，参数为 `18a43b01f1b72fd3b77013d7eab7099232c559f1` 的完整29参数；数学父26、b=1/2、ε=1/8，全部域、误差、预算、接受规则不变。没有把30按需优化或R727准确费用源码混入本次计算。

完整3-step queue为74372 B，三步命令词数6/26/157。science自然返回后再按原完整 ready 接 pure-only 52442 B；science+pure118584 B / 全四126705 B 超过原95000 B队列上限，所以不在活动child期间乱换整队列，也不截参数。公共窗口360min，controller准入21000s原字保持。

原 runner 已终止，其局部数组不可转移。新的独立 runner必须按原两完整输入步骤生成自身输入；不把旧输入 SHA、模型、点或 run ID 回填新运行，不跨 runner以Git/Release/Artifact转存数组。必要的输入生成不重复宣布原数学结论，也不是新增入场检验。

## 4. 全文再生与后续实际记录

完整再生器接受 `SOURCE_REPOSITORY OUTPUT_DIRECTORY`。读取旧完整控制器（原路径若已替换则读取已记录整 Git blob），先核19995 B和全SHA，执行唯一完整文字段替换，再反替逐字还原旧全文，核新完整21888 B和SHA，写入独立输出目录；不执行Python/AST/科学程序、不改ref/队列、不覆盖不同现有输出。

原全request40193 B / `473b5ff5c7af82fa6ef3611c7134b9255bc03f443c518ae76594a0b3830479c2` / `a97d6b2a2c0bb1e017ea5d1ec39046512b80e6f2` 在原259814提交逐字保留。当前全request45534 B单独随本提交发表，每个原历史链接与失败边界仍在whole对象里。本说明的完整交付manifest还保存原/新文件、原失败和队列/参数/来源责任。

本提交只是已授权的修复和新push触发请求。新的 run ID、job ID、实际开始、子进程源、模型、参数点和报告在真实返回前均为null；之后追加实际官方对象和阶段证据。保留原失败说明；本新说明负责新runner历史，不抹旧失败。

容量已通过普通退役可完整复现的历史输出释放；所有原结论、完整源参、失败及固定Git恢复责任保留。当前新增运行记录需要持续预留空间，不能把剩余空间全分配给尚未启动的源码包。
