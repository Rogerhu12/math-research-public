# M24 真实尾接续：丢失场的必要恢复入口

维护：Astra-held10-06bbeb39-20261126 / actual_tail。日期：2026-11-26 UTC。

**范围：已完成输入与源码再生，直接 M24 场恢复已启动；不是新增的等距闭族结果。**

接手时实际检查了前会话记录的
`/workspace/scratch/1b6d88ecddf3/m3-work/`：目录不存在。因此旧 `.25/.5`
完整尾检查点、M24 `inner-00.npz` 和原 `.75` 进程的终态不可取。此前已登记的
`.25/.5` 成功结论不受影响；不能把旧 session 号说成当前仍在运行，也不由
目录缺失推断它们后续的数学成败。

## 已实际恢复的输入

新工作根为 `/tmp/held10-astra-06bbeb395471-tail`（下称 `W`）。按原
`m3_source_recovery_manifest.json` 恢复 70 个源文件，合计 537048 字节；
每个文件逐个核原 SHA。来源仍是 manifest 的三个历史提交
`34a036028256ad59c702a3fc8088275dad7c2948`、
`46fe93d4bb708fdfb7935e91b8141ea77586f0d2`、
`507d346bf1d13c8baf03ee3a4636ecc2fa6aa1d5`。

随后依次复用原 sparse、multistage profile、shared allocation、periodic
quadrature、bounded-chord-3 和 native 安装器；所有副本使用不同目录。
`W/multistage-source` 是前缀来源，`W/native-tail24` 是尾来源。二者均保持
原方程与残差门，native 只用两个进程。

原 `portable_bootstrap.py` 的未共享 baseline exporter 在本环境中发生
`Weighted stage-tail initialization failed`，没有返回端口。原客户端没有
保存该 Node 子进程退出原因，因此不指定 OOM 或数学失败。改用**已登记的**
shared allocation 副本后，同一 baseline 配置和 M24 配置都实际 export 成功。
该调整没有改变有限端口的数值；实际复现的关键文件如下。

| 文件 | SHA-256 | 与 11 月 20 日记录 |
|---|---|---|
| `inputs/reference/chart.json` | `dc85dda524e03896b4afa552bd1f859b73cf96f88033565ff910e227034f2f93` | 相同 |
| `m24-linear-port.json` | `42369d1571413fd4ecccea43ccfef233f4b97506f71e28b86ed9735c28c2d93b` | 相同 |
| `m24-tail-settings.json` | `37bc9073d2dba1d110b165b5febbb054d1dd1a8ca09ec23b86e2d76c39f08f46` | 相同 |
| `frozen_flow_batch` | `1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94` | 相同 |
| `native-tail24/native-manifest.json` | `af878d1a70fe6934f2db62a2d23b6028d52aae776353e4b5876b4d510ed2873c` | 新绝对路径绑定 |

M24 端口的前四条 DN 为
`[21.398688018893054,44.01273315539301,48.64330690634227,35.31533434331294]`。
这仅是恢复输入，不重记端口研究结论。

## 直接场恢复，没有重走旧 q/λ 设计链

用 `multistage_m24_core_neighborhood.json` 的 23 个原 binary64 控制和
原实际 `delta=.06413464104697915` 构造冷初猜。物理 profile 已包含原
delta 增量，故初始 `p0=0`，不再把它加第二次。原 full exact lift 保留，
q=.06、材料 λ=.002、M24/angular768、原 linear DN、原 tol 和 BC 门不变。

实际启动命令为（`T` 是当前课题目录）：

```bash
env -u LD_LIBRARY_PATH -u LD_PRELOAD \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  PYTHONUNBUFFERED=1 python -u "$T/scripts/resume_m3/portable_prefix_continue.py" \
  --source-topic "$W/multistage-source" \
  --short-bridge "$W/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --profile "$W/m24-recovery-profile.json" \
  --chart "$W/inputs/reference/chart.json" --port "$W/m24-linear-port.json" \
  --control-record "$W/m24-recovery-controls.json" \
  --core-module "$T/scripts/resume_m3/material_support_factory.py" \
  --core-config "$T/scripts/resume_m3/multistage_wide_circle_lambda0p002.json" \
  --amplitude .06 --warp-reference .06 --modes 24 --angular 768 \
  --audit-angular 512 --nodes 801 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$W/m24-direct-recovery"
```

初始 818 节点已实际通过原 Frenet 域，耗时 5.41016035 秒、max RHS
4.6999814719027，随后进入原 Newton。该进程后来真实返回 `exit137 / Killed`，
没有第一网格返回或 raw。检查时整机 `MemAvailable` 约 2.5 GB；没有可读的
cgroup OOM 计数，故只登记 SIGKILL，不把原因断言为 OOM，更不说数学门失败。
旧目录和日志保持不动。保原 M24/angular768、全部方程和门，仅把初始 `--nodes`
改为 `401`（原已登记 M24 入口也用 401），并改用全新
`--outdir "$W/m24-direct-recovery-n401"` 继续。新 raw/physical 和全尾必须
等待真实返回，不能把重新构造的初猜当成丢失的旧场。

新增 `scripts/resume_20261126/tail_recovery_setup.py` 将以上已实际执行的
源/参数/端口/native 准备步骤整理成可搬迁入口。脚本本身已过 `--help`
语法和导入检查，没有为验证包装器而再跑一遍完整准备。它要求全新、仓库外
的 `--work`；不生成 BVP 或尾成功主张。全部可再生输入、检查点和 native
数据留 scratch，继续原 fullH 与前缀联立后再绑定最终固定 g。

## 原 401 入口与首个资源观测的实际终态

401 入口也已真实返回 `exit137`。它完成初域并进入原 Newton，首个 full
trial 的 Frenet margin 为 `-.8102927711606788`，由原线搜正常拒绝；
随后进程被终止，没有首网格/raw。不能把这一次 trial 拒绝等同于 BVP 失败。

第三个新目录 `m24-streamed-recovery` 使用 root 的
`streamed_prefix_driver.py --rhs-block 8` 和本子任务的
`tail_observe_prefix.py`。仅沿径向分批评价原 RHS/Jacobian，保 M24、768
角点、原 BC、原 Newton 和全部门。observer 在每次 Jacobian 入口保存完整
`x,y,p,pscale`，明确是**未接受的初猜**；并记录 Jacobian、sparse LU 的前后
事件与进程实际峰值 RSS，不修改原运算。

该运行真实返回 `returncode=-9`，18.265470712 秒；父进程
`RUSAGE_CHILDREN.ru_maxrss=494444 KiB`。observer 只见 8.152483831 秒的
首 `jacobian_start`，峰 RSS 同为 494444 KiB，没有 `jacobian_return`
或任何 sparse-LU 事件。这定位了该次终止在首 Jacobian 构造中，尚不确定
终止来源。紧凑事件/完整非秘密 argv/快照 SHA 见
`2026-11-26-tail-resource-entry.json`。原 `last-jac-input.npz` 留在
`W/m24-streamed-observer/`，后续可用作 raw-restart，不再丢失本次初猜。

首次观测启动还遇到 `/usr/bin/time` 不存在，exit127、零次数学调用；随即
用 Python 父进程的 subprocess/resource 包装得到上面真实终态。后续将
从快照接省内存的原方程评价，不原样重试已经被终止的入口。
