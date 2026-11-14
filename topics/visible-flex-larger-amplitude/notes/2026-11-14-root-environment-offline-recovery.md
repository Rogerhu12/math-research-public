# 2026-11-14 执行环境离线恢复记录

/root（GPT-6 Astra Pro，AI辅助）。本记录明确区分已推、仅本地落盘/入队与未执行。远端旧 HANDOFF blob `919b29838ab650c85386741a2f6c2f8e428d245c` 保留在 Git 历史，现不再沿用其中“正在运行”的旧状态。

# 状态与证据边界

课题 Rogerhu12/math-research/topics/visible-flex-larger-amplitude 尚未完成。2026-11-14 约 02:06 UTC 起执行环境明确 unavailable；最后一次新进程请求在 CreateProcess 阶段返回 environment_offline 409，随后返回 No usable execution environment is available。本记录最初为会话故障恢复备份；此后按根 README 第8条“只有 GitHub 集成可用时”例外，以小文本方式保存回仓库并同步 HANDOFF。API 操作不冒充实际终端 pull/push，也没有新增数值计算成功。没有把未知退出归为成功、数学失败或 OOM。

# 用户授权与恢复时必须遵守的规矩

继续研究直到课题 README 的全部完成标准真正达到；子问题完成即继续 open.md。至少每小时实际 git pull，普通推送前实际 git pull --rebase；非快进拒绝立即 pull --rebase 后重推至成功。每次 pull 比较根 README 和课题 README，只读新差异并立刻遵守，把读过的提交号写入 HANDOFF。每条完成结论独立提交推送。凭据只允许临时命令行使用；本备份不含凭据。

根写者独占 Git、索引、HANDOFF、results、log、open 和发布队列。子代理只写分配的新源码和证明包。全部任务合计约 9 CPU、10.2 GB 内存，BLAS/OMP/MKL 设为 1；只允许一个大型 strong J/QR 任务。完整证明放 results 并索引；每篇 Markdown 小于 100 KB，HANDOFF 连同发布页脚小于 10000 字节，log 每条最多 5 行；超过 1 MB 的数据压缩、单文件小于 5 MB。廉价大表仅保留可重建的源码、参数、SHA。不能增加独立复核或冻结闸门。不同 exec 会话的 PID 命名空间不同，不能用另一个会话的进程列表推断退出。

# 工作目录

```text
B=/workspace/scratch/d1aa462cfc02
R=B/math-research
T=R/topics/visible-flex-larger-amplitude
RW=B/root-work
EW=B/exact-work
GW=B/geometry-work
SW=B/strong-work
PYTHONPATH=B/exact-work/python-deps
```

# 最后确认的 Git 状态

最后实际 pull：2026-11-14 02:01:00 UTC；README 已读提交 c15b292293319d116558ee1852ebb45c7a36e86b。根 README blob f787a306d90892d8dec765dc59747d60ba39f055；课题 README blob 696eb3ba7d3a90636e51e8fbdd573b2f37cae707，最后确认未变。发布状态计数 committed=339、pushed=338；最后确认已推 SHA 66ec18eda6876a16a508acd91aced9494baf1beb。这些计数是故障前的实际观察，不表示所有队列均已推送。

发布父进程 session 94713 实际退出 1。其最后子日志记录 actual pull 成功，随后 POSTPULL_RESOURCE_REFUSAL，free_bytes=0，minimum_bytes=419430400。父进程在写 publisher-owned-attempts/20261114T020037794361Z-resource.json 时 ENOSPC；该子进程的 wait4 资源记录未持久化，不能补造退出码。父进程没有重新启动。

原同步器 sync_queue.py SHA 37a00c1b2367964d57c3b5ee2d5fb2b3f92a84ab8c87d28bc1859c4ee39f7748；原父控制器 run_publisher_bounded.py SHA d542392b4d126e63594f41940bb5fb42726b646f98b1e0d5933bf4e0fd03acff；sole-publisher-runtime.lock 保持单发布者。恢复后计划新父控制器在磁盘 ENOSPC 时把已完成子进程的资源记录先写到 RAM，再每 5 秒重试原目标；不改变 pull、README 差异检查、资源门或数学行为。尚无此新控制器成功写入的确认。

# 环境断开时未确认的操作

functions cell 257 原本拟迁移 378 个 R221 已完成只读派生表（33491064 字节）至 /dev/shm/vfr221-0204，逐个 SHA 核对、fsync 后以原路径符号链接替换，并写 RW/R221-completed-profile-RAM-relocation-r1.json；还拟生成新的资源记录安全发布父控制器。调用在 CreateProcess 阶段失败，没有执行确认。恢复后先检查路径和回执；既不能假定已经发生，也不能盲目重跑覆盖现场。RAM 路径若丢失，只按对应固定源码、参数、SHA 重建缺失廉价表。

HANDOFF 最新快照文件为 B/handoff_current_snapshot.json，镜像 RW/handoff_next_candidate.json；最后成功记录正文 9637 字节，另预留页脚 350 字节。它已经落后于 r5/r6/r7、metric 终止和 R222/R223 状态，恢复后需压缩更新。只允许删除本任务明确可重建缓存；不要动其他工作区或唯一科研数据。

# 完成标准和真正缺口

必须同时提供闭连通 C² 嵌入曲面族、全参数 C² 连续性、固定有内点的 H 且直径至少 0.2D、固定位置像 Hausdorff 变形至少 0.2D、模全部欧氏等距含反射后仍正的形变、全时刻 reach 至少 0.03D、同一个固定度量 g 上全曲面全时刻相对度量误差至多 1e-6，并在相同 g、参数和时间范围下通过网格/频率/时间精化把误差降至机器或原求解器容差。永久构造缺陷仅靠换层数、缩尺度或换 g 压小，不算完成。还需完整网格与严格存在性差距的诚实说明；达到门槛后继续增大振幅。

接受候选 A 的核心支撑差代理 G=0.2506381129076958，Cartesian 核心轴差约 0.2506381374645977；连续前缀直径下界 3.976755157289288，因此 0.2D 至少 0.7953510314578576。现有 G 远小于这一门槛，且 G 不是已证明的闭曲面 Hausdorff 下界。不存在已完成的大振幅见证，也没有不可能性证明。新半步目标约 0.25463811298 即使收敛仍不足以达到任务标准。

# 根线路完成包与下一次实际计算

R216：18 个子任务、3976 细分叶、46 个偶数低模 2..92、原 3940 传播叶全部实际 0。完整密度响应主证书 SHA 6a3e2773921f1800abe0fd86b812386394246f8c3462f6a9191bbc36f873cd14；整三 cell 低模读数 SHA 4a2f3540deda0a480401cf338953a06bb369ce1cd03edaf6bf58863e002d1e0f。窄条合计 0.015103892811772568<1/64，移动权合计 0.024084466805128657<1/32，仍有未支付的未知高模反馈。完整包 manifest d8a92b27cc75559f5a71c0a901bfa674fa7de3fb996b1962dad2c7f89074dca1，已入队。

R219：新低模盒 B=(6/5)×(R215 基线+R216 完整物理源响应)，因子已完整，禁止再次乘 2。主数据 SHA 55cb6c5b88c0d51b767699d24c31f3cad7a8d33f86c16c3c6b8b6219969b537e，实际 0，36.9646 秒。窄条 0.018124671374127082<1/32，移动权 0.028901538123257055<3/64。manifest b8632e07c4c6b18ec4c444d3c166acc9be593296656b4b4d4dd3246bd9c8142c 已入队；仍只是纯低模条件盒。

R221：全过去源叶至当前原传播叶右端的新旧完整源比 C_m，乘原任意符号源的完整叶响应。v2 源码 3032547f02c561fe07f90e26c5ef23f2d7e12ed44d4bcf4684450f2b1030c2cf；主结果 51a1bcd2757f16d80f5f040e48ffdc4c9ce83b604578618a3c967899b599f9f1，实际 0，60.18156 秒、116856 KiB。cell9 全部分量包含通过；cell8/cell7 共 171261 个比较失败。高频加权循环卷积对低频的上界混叠是主要过宽来源，不能当作真实误差下界。manifest d0b060554c78334b3ba8c749a0949ae1b0fa5be1e12f1229b03b709ef8b293fc 已入队。

R224 源码已写但未运行：computations/root_R224_minimum_source_prefix_response.py，SHA e841009e40f387f69099ec54cfb0b04179e07acec63e8031a35ffdf6976c4914。消费 R222 的逐项 min 源，按源支配复用整个已成功的 R221 cell9，只新增 cell8/7 前缀读数；仍覆盖所有过去源叶和完整当前叶。输出目标 RW/R224-minimum-prefix-r1.json.gz，资源目标 RW/R224-minimum-prefix-r1-resource.json。没有主结果或成功记录。

# R222 最小完整低频源包

R222 已完成：64 个真实资源记录、3976 行、全部实际 0，源计算 812.595 秒、83660 KiB。保留 R220 完整均值和正逆级数尾，仅新增 η=0 有限正卷积；每个物理模式 2..184 的完整源帽取 min(新的完整无扭曲帽, 原相同输入的完整加权帽)，不借用旧 2b 盒。最坏旧低频叶 2520 的 m28 从 log2 约 -101.728 改善至约 -168.459。

完整 manifest：notes/2026-11-14-exact-resume-R222-untwisted-source-manifest.json，SHA c148c946584b06f23ba4355e9cd45b1961cde3c410e38465f64d0c32cde496e1；12 文件、129764 字节。已完成但尚未入队。源码 e270a969a74814699cdbd0cf7869fb687b44c1a53d0a5a887e7096785b3d9b6a；计划 e98808af8e164e300b906aca7f0bd72457e162900221bbd450a608154ed156ca。

根索引目录 RW/R222-owned-source-indices，三 cell 均实际 0。索引源码 SHA 8bee7bcc3c98864cfa63f1a7423d262f1da3b864e21fab15e4206b94e2210a79；共同 case b0c85bc83dd94a2054a08b47cfea7155f851f2e0ae3a88270f813d26dc935700。cell9 索引 7f2b1488b727540d8a0e801889e679f2797b5c1cb324f6649b1833605aaf04a9；cell8 54033cda968cd16a2f71a9021cef626b6e4cc311e1120c2e6e1c7165969c5794；cell7 68ded5765cd4c9049e60d4a181681b2ff11f56c64105e2894c39c15a02957166。含所有原完整源、尾、flags 和别名 SHA 核对。

# R223 固定帽标记的条件性刚性证明

完整证明 results/R223-flat-cap-circle-markers-and-actual-nonplanarity.md，manifest notes/2026-11-14-root-R223-flat-circle-markers-manifest.json，SHA c79d3f6939fdb94ab0177c8ac6e56b9809948f81635481754b19d145cefa5ce6；6 文件、35079 字节，已入队。主证书 SHA 5d6ea74fc8bf8a93d22a4e5da6ff5861bb58d4646587252bd8747ce3d707a9ca，实际 0，28 gates。

用固定上下平帽的极大开放平面部分边界识别四个不同半径的圆，四个圆心仿射独立，故保曲面欧氏等距含反射只能为恒等。证明以闭嵌入、其他身体及尾部无开放平面片、两端像确实不同为前提。实际前缀非平面性和有限内 collar 的非平面性已分别由解析性/π 奇偶性/正分支、精确有理行列式多项式支付。有限 collar 的 P(1)>0 约 7.808684593950796e-25。标记对 g 的改变必须一次固定为 I+db⊗db，不能随精化改标记幅度隐藏永久误差；整体 reach 仍未支付。

# 精确线路高模状态

R220 完整加权源/类尾包当前 manifest b1dfa3eec1171c1b7aa22a2d4ec51e92658308143128d93f655ac51ed3c28e1d，已入队。原 SHA 6592e483 前缀已过时；仅修复两处证明 LaTeX 的 qquad 分隔符，未改科学数据。refined moving tail manifest bba493dd008edb4975ada71ab92a0f6be5538f8ad55399b797f7fd30ba7949be 已入队：全部 ≥226 移动权尾 <2.45e-8，全部 ≥258 的 log2≤-32.1344640655；≥218 仍不够。

98..184 源响应 18/18 子任务实际 0，完整主结果 SHA 前缀 ff07f156，移动权合计 1.37210960977018e-13；尚未形成完整证明包。186..192 三 cell 全部实际 0，最终 SHA 8f87ab7806f0440928882dfcea3f224b4ec1fe81d36c0acb18e00c3fc11ababd；移动权 log2 分别约 -76.47314、-79.51482、-82.08520、-84.74784，尚待归档。原过宽 v1 负面记录保留；v2 用有符号一阶参数差和逐行 PSD 噪声包，不新算 ODE。

194..224 驱动 session 30650 实际退出 1，348.709 秒，ENOSPC；6 个 cell 记录实际 0，恢复仅补缺项。94/96 薄前缀消费者 session 62007 实际退出 1，11.243 秒、60508 KiB，在写 targets-009 时 ENOSPC；它是廉价新旧源比读数，无需重跑传播。后续还须消费 R200 的真实全高模初值为完整移动权逐叶帽，随后支付未知高模反馈，不能把旧窄条高模范数免费升格。

# Strong 线路真实状态

接受 A 输入 SHA 917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf；M32/p35/2590，RMS 9.9224e-8，边界 9.234e-13，真实 H/J 577 格，audit=false。完整均值密网格 metric 6.733e-8，κ≈8.34551434。新半步目标仍未成为接受解。

r5 原精确循环真实退出 -9，2026-11-14 01:43:33，293.976 秒、388784 KiB，原因未知；没有主动暂停。保存 factors=1、updates=2、iteration=2、refresh=false 和第三轮前八个实际拒绝，next_back=8。manifest c098d72538a99015eaf8644d53bf4e74ead48ef419210cc67a855a192faabcb9 已入队。

r6 实际退出 1，2026-11-14 01:51:37，56.66 秒、230108 KiB；初始 Node 全流 worker 在 ready 前返回 -9，尚未进入 J/QR/线搜索。原因未知，cgroup 指标不可读。manifest notes/2026-11-14-strong-half-positive-native-loop-r6-initial-tail-interruption-manifest.json，SHA e8c9e7155e595b495d9444782af9a35d530f1e9a96e7e3a6c6cde88cef50d98e，32 文件、252663 字节，未入队。

r7 没有启动科学 producer。精确同 H 回放只接受原 32 个 H 比特且 audit=false；一 ULP 不同或 audit=true 必须调用原活计算。14 gates、全部 3136 个 J 比特与原记录一致、0 Node，回放检查实际 0；native prepare 也实际 0。原 J1 460075656 字节、QR1 851514112 字节保留。容量预付后磁盘再次被占满，原 656 MiB 余量门拒绝启动。

纯容量 helper 退出 130；原未用全零 hold 实际释放 460070912 字节。释放回执 SW/half-positive-native-r7-unused-capacity-cancellation.json，SHA af2b5d32f0e4e15dc429eb8a659c680096223a40b8c04ab53d9bfde8749a309f。旧 capacity receipt 虽仍有 finished=false 和历史预付数值，但 hold 已释放，不能拿它启动；必须新建 capacity-r2/launcher-plan-r2，真读 hold stat、实际 arena 已分配容量和原 656 MiB 余量门，再从 next_back=8 接原数学循环。

# Geometry 线路真实状态

接受 A 连续前缀的完整 3016 箱、48 批均实际 0；C²、正分支和非退化已证。连续反射前缀直径区间 [3.976755157289288,3.979776359467403]，仍有两个外边界，不能称闭曲面 D。连续曲率上界 8.374728593585317，前缀 κD≤33.32954687370653<100/3；这不是全局 reach。

完整 metric 驱动 session 73667 实际退出 1。nodes batch144-attempt00 在 01:53:21 返回 -9，8.046 秒、90600 KiB，原因未知。前 144 批 /1156 个原父盒实际 0，batch144 的 ellipse 也实际 0，均复用；部分节点日志不等于完整主结果。原共 377 批。恢复可用两个静态区间 [144,260)、[260,377) 独立控制，只补缺少 nodes；新控制器只存在代理会话记录，未落文件、未启动。

完整 metric 原计划 SHA 760de2d85205cb36509ee0ad17a960b2d2d96d75af8d5cf89403b8aea3899bee；driver cb5084d184c50881c1b76ad05e9c7e334c89b79ff1d955bc3405f35130c29802；ellipse worker 7e305b5995d42e033afb42509f7c1f96e7abdf4c3f20d2f7876961837b25038e；nodes v4 7845cfc4191de39a29b01cf4882dadaaa1955cad142f650db19b9b587e7cf786。

实际尾端读数 manifest 76a03235acadaf6a0cf212b6cf71168ed857584610494f158d8bc255d1f36324、外框比较 4b491dba991659603c9d1931ee0ff72ed9afb469a3f207cf16c31352a152b214、有限内 Hermite collar 32d67e31d442465d3332ac5848c9df8bcc0d5ec216756daf5ab1d80322fb6e6f、冻结头背景识别 0e2ef20f54cb9db78b25a48f0bcdb5b41170bce8bb197a964969340f43fc3fb1 均已入队。所有有限差分 2-jet 数据只作为明确的有限定义，不冒充真实连续导数误差界。

冻结实际背景头仅 0..159 层与旧 R26 精确相同，可复用其 C² 与曲率上界 8；n≥160 原 factory 的旧校准不同于 R26 的 65/64，不能免费借其深尾。有限内 collar 的全角/全相位 metric 扰动 ≤4.711295311828805e-12、内端 0/1/2 jet 精确零，永久误差仍不满足固定 g 精化要求。外端修正叠加一般近似尾时，曲率估计必须支付完整协变 Hessian（含切向部分），仅使用旧表面曲率不足。

# 恢复后的优先顺序

1. 确认环境、磁盘、RAM 和所有未确认路径的真实状态；只重建已知缺失廉价表。
2. 保存发布父进程 ENOSPC 原故障，恢复单发布者；实际 pull --rebase 并比较两份 README 后再继续推送。
3. 压缩更新 HANDOFF，写明环境中断、上述真实终态、当前读过 SHA 和振幅硬缺口。
4. 将 R222、strong r6 等已完整包逐个核对入队、独立推送；不把队列当已推。
5. 运行根 R224 两 cell 读数，复用 cell9。Exact 只补 94/96 廉价读数与近高模缺项，归档已完成高模后继续未知高模反馈。
6. Strong 重新真实预付容量，从 r7 原 next_back=8 继续，保持唯一大 J/QR。Geometry 补原 metric 缺项，再处理实际尾部、固定 g 精化和闭曲面 reach。
7. 当前候选距 0.2D 很远，必须继续实质性增大核心振幅并降低身体高度，同时检查真实空间球排除；任何小步数值成功都不能作为本课题完成。

# 机器可读关键检查点

```json
{
  "state": "Environment unavailable; no completion claimed",
  "rootPendingCall": "cell 257 failed at CreateProcess: environment_offline 409; no execution confirmed; inspect migration/new publisher paths after reconnect",
  "publisher": {
    "lastSession": 94713,
    "actualExit": 1,
    "reason": "ENOSPC while writing parent attempt resource",
    "lastPull": "2026-11-14T02:01:00+00:00",
    "readSha": "c15b292293319d116558ee1852ebb45c7a36e86b",
    "committed": 339,
    "pushed": 338,
    "lastPushedSha": "66ec18eda6876a16a508acd91aced9494baf1beb",
    "missingResource": "publisher-owned-attempts/20261114T020037794361Z-resource.json",
    "childLog": "actual pull completed; POSTPULL_RESOURCE_REFUSAL free0/min419430400; child wait4 record unavailable"
  },
  "R224": {
    "source": "computations/root_R224_minimum_source_prefix_response.py",
    "sha": "e841009e40f387f69099ec54cfb0b04179e07acec63e8031a35ffdf6976c4914",
    "run": "NOT STARTED",
    "proof": "R222 pointwise min source, reuse successful R221 cell9 by domination; read only cells8,7 for new prefix ratios."
  },
  "R222": {
    "complete": true,
    "manifest": "notes/2026-11-14-exact-resume-R222-untwisted-source-manifest.json",
    "manifestSha": "c148c946584b06f23ba4355e9cd45b1961cde3c410e38465f64d0c32cde496e1",
    "queued": false,
    "caseSha": "b0c85bc83dd94a2054a08b47cfea7155f851f2e0ae3a88270f813d26dc935700",
    "indexSource": "8bee7bcc3c98864cfa63f1a7423d262f1da3b864e21fab15e4206b94e2210a79",
    "indexDir": "root-work/R222-owned-source-indices",
    "index9": "7f2b1488b727540d8a0e801889e679f2797b5c1cb324f6649b1833605aaf04a9",
    "index8": "54033cda968cd16a2f71a9021cef626b6e4cc311e1120c2e6e1c7165969c5794",
    "index7": "68ded5765cd4c9049e60d4a181681b2ff11f56c64105e2894c39c15a02957166",
    "allIndicesOwned0": true
  },
  "R223": {
    "manifest": "notes/2026-11-14-root-R223-flat-circle-markers-manifest.json",
    "manifestSha": "c79d3f6939fdb94ab0177c8ac6e56b9809948f81635481754b19d145cefa5ce6",
    "primary": "5d6ea74fc8bf8a93d22a4e5da6ff5861bb58d4646587252bd8747ce3d707a9ca",
    "queued": true,
    "fullProof": true
  },
  "strong": {
    "r5": "owned -9, c098d725... queued",
    "r6": "owned1, initial Node returned -9, e8c9e715... NOT queued",
    "r7": "0 producer; exact same-H replay owned0/14gates/noNode; native prepare0; unused capacity helper exited130; explicitly freed460070912B zero hold, old J/QR preserved",
    "releasedReceipt": "strong-work/half-positive-native-r7-unused-capacity-cancellation.json",
    "releasedSha": "af2b5d32f0e4e15dc429eb8a659c680096223a40b8c04ab53d9bfde8749a309f"
  },
  "geometry": {
    "metric": "73667 actual1; nodes batch144 attempt00 actual-9; first144 batches/1156 parents owned0 preserved, ellipse144 owned0 reuse; propose static shards[144,260),[260,377), not launched",
    "latestQueued": "0e2ef20f54cb9db78b25a48f0bcdb5b41170bce8bb197a964969340f43fc3fb1"
  },
  "exact": {
    "high98_184": "18/18 owned0, full ff07f156... moving1.37210960977018e-13; proof not yet written",
    "high186_192": "all3cells owned0, final8f87ab7806f0440928882dfcea3f224b4ec1fe81d36c0acb18e00c3fc11ababd",
    "near194_224": "driver30650 actual1 ENOSPC, six cell records owned0; resume only missing",
    "mode94_96": "prefix62007 actual1 ENOSPC writing targets009; full data reconstructable no new propagation",
    "refinedTail": "bba493dd... queued; >=226 moving<2.45e-8"
  }
}
```

## 本次文本提交的远端基准

GitHub集成读到 main=199937d68805d323d5f7ed330a8495194a8ea8a4；根/题README blob仍为 f787a306d90892d8dec765dc59747d60ba39f055 / 696eb3ba7d3a90636e51e8fbdd573b2f37cae707。此为终端不可用时的小文本提交，未声称执行 git pull；分支更新使用原HEAD租约且 force=false，已有他人提交保留。
