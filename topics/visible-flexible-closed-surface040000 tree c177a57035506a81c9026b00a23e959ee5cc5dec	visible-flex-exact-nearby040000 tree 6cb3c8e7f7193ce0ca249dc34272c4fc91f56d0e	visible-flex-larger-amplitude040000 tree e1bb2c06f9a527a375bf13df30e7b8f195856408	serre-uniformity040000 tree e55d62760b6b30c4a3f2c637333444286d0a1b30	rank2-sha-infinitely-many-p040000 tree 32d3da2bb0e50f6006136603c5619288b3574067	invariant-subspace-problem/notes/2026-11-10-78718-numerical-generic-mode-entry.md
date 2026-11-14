# 同一 flat17 几何的可选 M 真 DN 联解入口

2026-11-10，numerical_recovery。依据根 README 第13条，后续升频直接使用
这个实际入口；没有冻结、登记、独审、机械核验或独立重跑等启动前置。
这些新文件不修改当时正在运行的 M15 程序。

**同日更新：** 现在还支持 `--tail-modes W` 与 `--tail-only`，真实尾暖启动
已改为保持raw高度/斜率的几何嵌入，附轻量Jac/LU/Newton/尾进度。完整当前
用法见 `2026-11-10-78718-numerical-mode-split-and-geometric-warm.md`。
下文M16准备的源SHA和旧π补零说明保留为初版历史，不冒充改进后的真实DN结果。

## 直接使用

主文件 `scripts/78718-run-prefix-mode.py` 接收 `--modes M` 和实际 prefix CP。
若 CP 已有自己的最终 `tail_seam.tail_record`，程序自动取该末包；若显式
使用其它真实成功的尾初猜，传 `--tail-seed` 并在研究记录中说明。
输出 stem 必须未使用。

例如，当当前 M15 真联解实际成功后，在 repo 根直接运行 M16：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
 --modes 16 \
 --restart topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01.json.gz \
 --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m16-direct-01
```

这条命令**尚未执行**，当前没有M16解。将 `--modes` 改为17、18等并给新
stem，即使用同一程序继续计算，不再复制12份另阶包装。
实际启动后由持有终端 session 的执行者正常观察自然出口；程序不会把
自身报告伪装成工具退出回执。

默认保留 max_nodes8000、每进程 DATA6GiB 和 Node1536MiB，可用
`--max-nodes`、`--data-gib`、`--node-heap` 明确改变数值/资源预算。
默认角数取满足 $N\ge\max(512,8(3M+1))$ 的最小二次幂，所以 M16用N512，
M22自动用N1024；`--angular` 可明确指定更高角数。角数改变的是数值求积，
不改变固定度量。

`--prepare-only` 会真正构造原 saved-mesh restart（包括新M的 inlet 校正），
只输出几个初猜标量和小报告，不启动 DN/BVP。这个选项是调查实际初猜的
工具，不是正常求解必须先经过的门。

## 保持的数学与实际改变

相同阶数分支的原 `db6f-prefix-flat-coupled.py`、`db6f-prefix-coupled.py::main`、
`solve_with_actual_tail`、全部 BC/physicalBC 和 adaptive flat profile 均直接复用。
固定 profile/chart/port 来自现有 flat17 输入；加载时与 CP 的原冻结几何
字段比较，避免研究中误把变度量当加密。同一 gauge amplitude=.1、
warp reference=.1 不变，core自由参数仍由原BVP重新求。

每阶仍使用原 `power2_weights(M)`，原谱坐标 solver 会回到物理坐标重新
计算 RMS 和 BC。径向 tol$2\times10^{-9}$、BC$10^{-8}$、physicalBC
$2\times10^{-11}$ 保持。释放旧LU的 Newton 和直接 canonical CSC 都复用
现成通用函数，不改它们的算式；程序只做进程内选择并在结束时恢复。

第二份新文件 `78718-tail-mode-continuation.py` 只重写控制器的初始化，
使旧 warm 允许明确的 M/N 数值改变。它继承现有物理 H 的 `Coordinator`
及 solve/cache/record/close。初版底层是原 trial worker；当前的另名几何warm
worker只改初猜转换，仍用原真 nonlinear
residual、36轮、原 line search/floor、原 audit/Jacobian。延拓预算仍为
初步1/8、最低1/1024、每外请求最多32次，成功不扩步；没有新线性响应
替代真 DN。

初版原 worker 的 `950f-tail-warm-remesh.mjs` 对状态的两半分别按旧新M索引
复制公共模式，其余模式补0。物理深度、parts及原分段不变时，它直接对应
已有 shooting 节点。外层 prefix 的
`db6f-prefix-preserve-restart.py` 同样复制三个 Fourier 分量的公共模式，
并用原局部 inlet 校正让新的有限初值满足新M的原 core BC。两种操作都
只是初猜；新的响应必须由新的实际请求求得，旧 Jacobian不会当作新M的
Jacobian使用。

新 tail packet 诚实记录实际八份 trial 源及两份控制源，未冒充旧八源或
九源标签。当前旧的按M硬钉 final 归档包装不用于这条新入口；数学检查直接
保留在求解返回后的原 RMS、physicalBC、真正 outer BC、自己最后 audit
包及有限数据检查中。连续整图原 $2\times10^{-9}$ 及 README 各条件仍需
后续实际计算，本程序的有限成功不支付这些条件。

## 已做的实际初猜计算

真实 **a63e07 自然 exit0**，约0.648秒：将公开的旧M15 matched-cut
UNSOLVED warm与其旧N256真首包放到M16/N512，得到：

- 49个状态、16个自由参数、原2633个节点，最大谱权4096；
- 新prefix cut height与按模式补0的旧真tail物理标签的最大差为0.0；
- 原inlet校正由原函数实际执行；0 DN、0 BVP。

具体输入是
`notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz`
及
`notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01_tail_0001.json.gz`。
这只说明通用M入口可构造此明确初猜，未说明它会收敛；也没有使用尚未
完成的当前M15结果。

小报告
`notes/2026-11-10-78718-numerical-generic-m16-initial-prepare-01-mode-run.json`
8,841 B，SHA `a9f1636b37c0903d5c89c8198ff514f3ae97cfda53fb49136ca947ddaf004f7a`。
真实argv/工具回执为
`notes/2026-11-10-78718-numerical-generic-mode-preparation-observed.json`。

上述初版实际准备计算的两源分别为：driver14,205 B / SHA
`d2432718f6465d5b587da07bcf94f941635e501105a904245fc2c04b6e703c19`；
tail adapter5,287 B / SHA
`9a74f018df2069045a49bb313e6aaf2efdcac9ae91a86313e48cf25c17b18e80`。
这些记录帮助复现实际计算，不设额外审批或重新冻结要求。
