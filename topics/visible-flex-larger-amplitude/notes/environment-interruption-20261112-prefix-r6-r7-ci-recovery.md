# strong 分支：r6 明确 ENOSPC 与 r7 环境中断恢复记录

日期：2026-11-12。性质：执行记录；课题未完成。原 r7 的正式终态未知，不据执行器失联、工具会话缺失或跨 exec 的 /proc 观察推断信号、退出、成功或失败。新的 CI 运行必须使用 fresh prefix/运行 ID。

## 已正式成功且已提交的锚点

原接受基准是 q095 的 M24/N768、2004 节点、tol=1e-7 实际非线性尾联解：
`notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1.json.gz`；
其 raw 后缀为 `-raw-collocation.json.gz`，尾包后缀为 `-tail-response_0003.json.gz`。

新 q096 的初始完整尾 H 已由 r11/session88161 正式 exit0、worker0 验收：
`notes/2026-11-12-strong-actual-q096-cached-iteration-tail-audit-heap96-young4-r11-response_0001.json.gz`，
SHA256 `c8420b9b33df6472b05bd31604c69feb2470cf6d41310c8d8ca785942d15efd2`；
对应 ready SHA256 `e2be7cb8c4e136624d804faf3da394d1f859ba73427d17be89680cbbf6b0fde5`。
完整 H 的 float64 字节 SHA256 为
`c486a7cac208969a2c7e4febd7961098a9e075e641ebee2596876c7179d8f4f7`。
r11 residual=1.120173227172859e-9 < 2e-9，576 段完整 Jacobian、全部原 audit、74×24 物理高度 Jacobian 和 predictor 均完成。
这只是拟用 q096 前缀的准确初始尾锚点；不是新 q096 前缀已接受。

## r6：已确认的执行终态

前缀
`notes/2026-11-12-strong-actual-q096-combined-m24-tol7-prefixcache-radial8-heap96-r6`，
session58524 正式 exit1、child exit1，无终止信号。
wall=168.419734651 秒，wait4 peak=249864 KiB，user=161.274886、system=3.451543 秒。
334 个完整 fun_jac 回调及 4173 个回调节点已实际完成；state-J 和全部 27 参数 PJ 都保存。
完整块 Jacobian 202367096 字节已装配。
在 disk_factor_begin 后出现原始 OSError(28, 'No space left on device')：
未完成整次 factor，未得到任何新接受 Newton 步。

该次默认 /tmp 的可用量约 528281600 字节，而 J 与 QR 同时所需
202367096 + 374133760 = 576500856 字节。
这只解释这一明确 ENOSPC；不解释此前未知 signal9。
共享卷可用量多次自行变化，不把空间恢复归因于清理。

原 radial8 cache 完整身份：
`5d412603f4260085eecff2b23c9577a7aae63881680b12339dffd1e609da8647`。
它绑定完整输入 t/y/p 的 float64 字节、shape/layout、全部 state-J/PJ、实际物理 profile/参考图/目标/源 SHA、
Python/NumPy/SciPy/CPU 特征与批量设置。不得在新路径/运行时下重贴此身份使用。

r6 本地 2340 个完整条目曾经全部逐项读回验证；账本：
`notes/2026-11-12-strong-q096-prefix-r6-full-call-cache-verified.json`，
SHA256 `1591c847f55743796d6900d94a1b1d5dd5ae120bb81821b982ce2427491d0eaa`，2493758 字节。
这是哈希/身份账本，不是数组归档；该账本与 r6 数组尚未推送时环境不可用。
需要诚实重做未能恢复的结果，不能从哈希造回数组。

## 自有重复缓存清理

在原334J和2个全场RHS逐项保全后，27037 正式0：
只删除 2164 个已归档的旧 radial16 重复条目及可由原公式重算的小 FD 中间条目，
实际 unlink 57343817 字节。
所有当前334J和2个全场RHS保留，旧13点对照所需RHS也保留。
不触碰未知作业文件、别的代理文件、原接受态、primary 数据或未归档完整Jac。
账本
`notes/2026-11-12-strong-prefix-cache-redundant-storage-release-r1.json`
SHA256 `ccae30b8e7d885c5b663718336451d478b24c1bfa511c0646fd02324f4ff06c0`，
1075671 字节，尚未推送。
因此不能同时声称清理后全部2340条目仍在；剩下的336个当前大条目才是继续首Jac的充分保存。

## r7：正式终态未知

前缀
`notes/2026-11-12-strong-actual-q096-combined-m24-tol7-prefixcache-radial8-workspace-heap96-r7`，
session80885。
运行计划 SHA256
`5a24b89bdfd73d5a2cb6665363c9d7a2966b45fde3f51d2f9ceaf00e9a714d37`。
只把 TMPDIR 改为自有 workspace：
`/workspace/scratch/c0de65fac774/strong-q096-workspace-arenas-r7`。
启动时实际可用 1969246208 字节。
数学源、MJS、所有门和 radial8/cache identity 都未改。
原2004/2003全场 RHS 和随后完整 Jac 批次真实命中；
最后观察约18.69秒仍是 cache hit，尚未观察完整factor或新接受步。
原始 scaled collocation=.00015616055003179834，BC=2.4581922476547945e-9。

已写的 iterate-0001 主包 SHA256
`37257117c842d4e12eada19e21a82dcdc5cc2467b46279d96c521feef043c10b`，
标签仍 newton-entry / solverfalse / physicalfalse；不是接受态。

其后 exec-server transport disconnected；
对原 session80885 的 write_stdin 返回无可用执行环境。
没有 wait4 结果，不补写退出码，不猜 OOM、时间限制或数学不可达。
另 /dev/shm 方案只做过纯文件I/O和 prepared plan，从未执行BVP。

## 新 CI 重做原则及精确命令

保留 q096 目标：
(.09599996014428179, -.006718093057120565, -.0004136733380408847)，
外物理方向 vu=-.0002、descending_turn_curvature=-.0025。
M24/N768/tol1e-7/maxnodes2400、原2004网格、全部24核心未知和三个物理控制、完整H真尾、原outer/fullJac/audit门不变。
旧 r7 继续 unknown，新运行用独立 `OUT`。
原334J若不可取得就原样重新算；新 runner 的cache身份应自然不同。
不要复制旧身份以取得假 hit。
r11包仅通过现有严格完整H/source/config/audit守卫复用。

以下命令从本题目录执行，PYTHON 使用已安装 Python3.12.14，
SOURCE 为按固定 revision/91文件清单恢复的 source topic。
所有 BLAS/OMP/MKL/NUMEXPR 线程设1。
TMPDIR 指向本次 runner 自有磁盘且启动前核够完整576500856字节加存储余量；
不通过新增 --disk-temporary-parent 改编译源。
环境版本原记录为 NumPy2.3.5、SciPy1.17.0、Node24.22.1。

```sh
"$PYTHON" -u computations/strong_foreground_resource_run.py \
  --out "$OUT-resource.json" --heartbeat "$OUT-heartbeat.json" \
  --ownership "$OUT-ownership.json" --task-prefix "$OUT" -- \
  "$PYTHON" -u computations/strong_cached_prefix_actual_bvp.py \
  --actual-reference notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1.json.gz \
  --actual-reference-raw notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1-raw-collocation.json.gz \
  --actual-reference-tail notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1-tail-response_0003.json.gz \
  --target-core .09599996014428179 -.006718093057120565 -.0004136733380408847 \
  --frozen-reference-ready notes/2026-11-12-root-vu032-q085-fixed-actual-m20-staged-audit-ready.json \
  --frozen-calibration-ledger notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --source-topic "$SOURCE" \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --tail-config notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1-config.json \
  --out-prefix "$OUT" \
  --response-data notes/2026-11-12-strong-q095-actual-fixed-control-response.json \
  --max-nodes 2400 --neutral-control-step vu=-0.0002 \
  --neutral-control-step descending_turn_curvature=-0.0025 \
  --initial-audited-tail-packet notes/2026-11-12-strong-actual-q096-cached-iteration-tail-audit-heap96-young4-r11-response_0001.json.gz \
  --initial-audited-tail-ready notes/2026-11-12-strong-actual-q096-cached-iteration-tail-audit-heap96-young4-r11-ready.json \
  --release-tail-worker-between-responses --node-heap 96 --point-cache-limit 2 \
  --radial-batch-size 8 --collocation-batch-size 12 --tol 1e-7 \
  --disk-backward-error-tol 5e-11 --disk-heartbeat-seconds 20 \
  --stage-cache-directory "$STAGE_CACHE" --node-young-semi-space 4 \
  --prefix-cache-directory "$PREFIX_CACHE" --prefix-cache-budget-MiB 256
```

固定源 revision=869436630c99aa5a68afb55bd8877c826034d117，
91文件总866846字节，
source manifest SHA256=7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941。
本题 main 已提交的 r4/r5 完整缓存归档仍可作为历史可复核证据，
不需要为 fresh CI 新身份加载这些旧前缀缓存。
所有 computations/*.mjs 仍冻结。

## 完成此步后的既定工作

只有真实 q096 前缀全部门通过，才做 actual 27→24 fixed-view、真实 pulse 外列和 core-held δ/LB/vp 响应；
以实际完整场 κD/D/RMS 选步，继而固定 g 的 M28/径向加密并继续增幅。
新 pulse/cache 组合入口只做过 source-only prepare，尚无非零 pulse 真解或新 q096 前缀接受态。
