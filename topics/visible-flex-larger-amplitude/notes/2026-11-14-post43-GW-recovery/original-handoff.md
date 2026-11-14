# exact_closure 当前恢复入口

更新：2026-11-14 09:56 UTC。父代理 `/root` 管 Git、题 HANDOFF/open/log；此文件只记录本子线。公开 push 曾被实际自动审批拒绝，父代理已请求用户直接公开授权；未收到新许可，全部外部写暂停，无绕过。

## 真实终态：本子线已无活计算

- 会话 **68641** 已实际退出 0：`closed-local-r1/GW-RK48-full-r1/terminal.json` 于 09:50:07.625172 UTC 完成，六个子命令全部 exit0，总计1394.1391秒。全部9244区间、157148径向×1024角的 GW rr 六 jet 已完整结束。
- 状态镜像 **87678** 也已实际退出0。`current-checkpoint.json` 已改为真完成，不能再读旧进度作为当前阻塞。
- 新完整结果包 `notes/2026-11-14-exact-resume-RK48-GW-sixjet-complete-r1/`（7件59294B），同名`.md`。未patch metric细层1.2594438379026109e−9，位置差7.3084357702e−14、径向一阶6.4817876484e−9、rr差.0017739032174；不声称C²收敛。
- successor的公开CI run43579782197仅与本地原默认rr全链重合。其默认rr数据与本线相同；新GW有限重构规则及结果不同。只读已核 `/workspace/scratch/e959e57ee07f/math-research-public/topics/visible-flex-larger-amplitude/HANDOFF.md` 和 `notes/2026-11-14-public-RK48-common-grid-completion.md`。本子线未进行任何外部写。

稳定原运行目录：`closed-local-r1/repo/topics/visible-flex-larger-amplitude`；稳定原 source：`closed-local-r1/source/topics/visible-flexible-closed-surface`。这些都是普通副本，原求解/读出已冻结。新发表目录是 `../math-research-public/topics/visible-flex-larger-amplitude`。

## 已完整完成

1. 原 A 同 g/H32、深度 8 的 RK48 Newton/J/audit：会话 87946 实际退出 0，残差 `1.6723555785869715e-10` < 原 `2e-9`。输入/响应在 `closed-local-r1/A-RK48-solve-r1`，已交父代理独立本地归档。
2. RK48 真 9217 规则节点，分别补齐 f8/f16 所需原断点得到 4639/9245 节点，所有 producer 真实退出 0。`closed-local-r1/A-RK48-cusp-resolved-r4`。
3. 原默认规则同 g RK24→48、共同 f8+source knots 的完整六 jet 比较，实际退出 0。未 patch metric `2.1581028853128337e-8 → 2.1590718325551535e-8`，逐点变化仅 `4.789259689785136e-11`；积分加密不解释当前插值误差。
4. 原默认 RK48 f8→f16 完整六 jet/整闭链：会话 87254 实际退出 0。未 patch metric `2.1614936936934382e-8 → 2.076083576699108e-9`，patch 原平台 `4.770331735019531e-8`。全 mean/三个 mesh/九相位/全部相位有限空间弦/finite collar 均真正结束。
5. GW rr 规则 f8→f16 完整区域 metric：会话 45177 实际退出 0，未 patch `1.1835925527203742e-8 → 1.2594438379066541e-9`，全部节点 nz≥`.9284733772597014`，cardinal 与独立 point Ftheta 差≤`8.0571e-18`。主数据 `closed-local-r1/GW-RK48-regional-r1`。
6. 新 GW f16 完整闭组装分支：五个子命令均 exit0，最后 summary 于 09:28:58 UTC 结束。新整闭输出已冻结归档，完整 six-jet 分支也已于09:50实际结束；见上述新完成包。
7. 新独立 M96 容量适配、非零点 RHS/J：会话 84460 实际退出 0；194 状态、194×192 J，全部 96 height 系数非零，fast/Fourier 相对差约 4.33e-17 / 6.48e-17。只点值，没有完整 M96 尾求解或 full provider ready 启动。

## 本轮新冻结结论文件

均在新 T 的 `notes/`，每个 `-r1/` 都有 `files.json`：

- `2026-11-14-exact-resume-RK48-actual-radial16-source-knots.md` 和 `-r1/`（15件，5,550,425B）。
- `2026-11-14-exact-resume-M96-tail-interface-limit.md`。
- `2026-11-14-exact-resume-RK24to48-complete-field.md` 和 `-r1/`（5件，33,769B）。
- `2026-11-14-exact-resume-M96-capacity-point.md` 和 `-r1/`（7件，735,862B）。
- `2026-11-14-exact-resume-RK48-GW-regional-metric.md` 和 `-r1/`（6件，20,818B）。
- `2026-11-14-exact-resume-RK48-radial8to16-closed.md` 和 `-r1/`（17件，3,920,062B）。
- `2026-11-14-exact-resume-RK48-GW-closed.md` 和 `-r1/`（14件，3,862,637B）。
- `2026-11-14-exact-resume-RK48-GW-sixjet-complete.md` 和 `-r1/`（7件，59,294B）。

上述结论均已发父代理；父代理先前结束主 turn 以请求直接公开授权，本次新件不应假设已经本地 commit。子代理没有操作 Git。

## 新源码

新 T `computations/` 中已冻结且实际消费的文件，前缀均为 `exact_20261114_`：

- `target_metric_regional.py`（完整 metric 筛查）。
- `target_metric_common_grid.py`、`target_metric_closed_assembly.py`、`target_metric_collar.py`、`target_metric_finish.py`（整链六个子命令全部成功）。
- `m96_capacity_source.py`、`m96_tail_worker.mjs`、`m96_capacity_point.mjs`（容量窄适配）。

其余 helper 是已交父代理的原 common grid / source-knot / resolved assembly 链，没有改旧文件。

## M96 交接给 geometry

独立派生源树：`m96-capacity-r1/source/topics/visible-flexible-closed-surface`。

身份：`da448038580593e27b11d301730f191a435627e940be38020970ce5027b7519a`。

相对/原 root/Fourier root 三处最大模数 64→96；原严格 `N>4*M*spacing` 保留，M96 点用 N1024。原依赖 Git-blob 检查保持，只有两份派生引擎的 blob 明确更新；source-origin 写明上游 base+显式派生身份。不要再改这棵树，geometry 可直接只读消费；不动公共 source、strong RT 或本线活 source。

new worker 给每个 ready/response 添加 capacityProvider 新身份；它本身仅语法检查过。geometry 负责新的 96core+3profile 增广 BVP、真实 theta(phi;c) 转换和新的完整96H。旧 .984 场直接换角图的二 jet 截谱缺陷约 .0224，不能以此容量包冒称已完成新全场。

同 576 段时 M96 一套流 J 为 162MiB，是 M32 的 9 倍；原代码还可能保留 Array.from 副本。首次真正 full-tail 启动须按当时资源协调，点值 RSS 不保证 512MiB 足够。

## 失败保存与磁盘

旧 v3 会话13425在真实16读出时 ENOSPC、实际退出1；`A-RK48-cusp-resolved-r3` 中4713有效部分节点全部保留。新r4完成后，逐压缩SHA匹配后把这4713旧路径硬链接到完整新节点，旧路径/字节不丢，释放123,242,580B。收据 `space-recovery-20261114-RK48-complete-hardlinks.json.gz`。没有清他题数据。

旧 v1/v2等待脚本退出130后已保字节移到 `history/RK48-source-partition-pipelines/`，manifest在内，v3不import它们。

## 整体未完成及接续接口

68641及其完整GW结论已冻结，毋须再跑。优先由有新公开授权的successor接走本线 post-43-commit 新文件；转移清单见 `successor-exact-transfer-20261114.json`。不要再为压原 prefix cut 的约4.77e-8平台无限提高RK；原prefix tol1e-7，尾tol2e-9。

所有A整闭样本仍 D≈3.97745926668、Hdiam≈3.96956337766、delta/D≈.0630146334；不满足.2D。未支付的主项包括新full-DN prefix重解、频率精化、严格无限尾、连续空间 reach。旧/新GW finite collar都有约1.0014e-18的非零界，不是无限尾存在证明。新候选必须用自己的完整H/prefix/tail，不能移植A数值。

## 本轮磁盘保存

09:48将四份不活跃背景JSON逐SHA无损gzip，净省60,894,923B，收据`space-recovery-20261114-lossless-backgrounds-r2.json`，列出原/压缩路径与恢复步骤。09:52归档目录mkdir实遇ENOSPC（计算已正常完成，文件无损）；随后19份冻结scratch副本与已归档同字节文件硬链接去重，全部原路径保留，省13,392,128B，收据`space-recovery-20261114-archive-hardlinks-r3.json`。强线同时主动结束自身R6并释放其J/QR，恢复大部分磁盘空间；不把该1.3GB算为本线释放。本线不删除原求解/raw节点或他人文件，归档重试成功。
