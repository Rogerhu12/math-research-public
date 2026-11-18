# n4：冻结系数流计算器的普通算术基线逐字节通过

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

可信度：**启发式/数值证据，属于有限实现身份核对**。
本条只完成一个可供高精度读数使用的独立 evaluator 的普通双精度基线；
尚未执行任何多精度档，没有真实尾的新接受结果。
输入仍是失败态 `b4356eabf97014127a364ef34b7951a930f4b184d8c6f4c4db83c161b2cbbb5e`
的既定 stage 43、38、175，使用前两项算术对照已冻结的 fixture。

## 原代码参考与实际判断顺序

`frozen_stage_arithmetic_bridge.mjs` 在 scratch 创建原 point-root 源的独立副本，
唯一加入 trace callback；split RHS 只把 import 指向该副本。
原生产文件完全不改。每一项替换都要求原文字唯一匹配，collector 再从原源和
声明的替换逐字重建两个副本，核其完整身份。

参考重走原普通 RK16 状态计算，并核对三个完整 42 分量输出与已有
`flowStateWithJacobian` 参考逐字节相同。两个附加 mean 分量全部保留。
实际记录包括：每次 RK field 的位置和标签、完整 root 初始 state/target/$L$、
每次 evaluate-$L$ 的输入和最终 moments、逐角度先 $D$ 后 $S$ 后 $A$ 的短路域判断、
Cholesky 对角元正性、每轮原 stop 的 err/scale/阈值、每个实际 halving 的 trial
和接收判断，以及若发生 fallback 时的原操作数。

原 root 规则仍为最多 30 轮、正常停止
$\mathrm{err}\le(8\times10^{-14})\,\mathrm{scale}$；
最多 20 个 $2^{-k}$ 试步，用原有
$\mathrm{er}<\mathrm{err}$ 或同正常阈值接收；全部试步失败后才检查原
$5\times10^{-12}$ fallback。域下限 $.1$、scale 下限 $10^{-300}$ 保持原二进制浮点值。
完整尾门仍为 $2\times10^{-9}$，本条没有调用它来接受新解。

## 固定什么，以及将来高精度重算什么

冻结 fixture 的全部 binary64 输入和目标、原 trig 表、RK 采样位置/步长和每点几何读数。
另外直接由原 Number 运算导出纯静态子表达式：$r^3,r^4$、
$\sqrt2,\sqrt{12}$、$E,w^2$、每模 $p$ 的分子系数及公共分母、target factor、
$\sigma$、flux prefactor、$q_L$ 分子和 mean factor。
它们在多精度档被当作其**原 binary64 精确二进制值**，不重算连续 profile 或 trig。
这明确限定为冻结离散系数的读数，不把原系数舍入误差悄悄算成已修复。

独立 Python evaluator 按原结合顺序重写 finite-$M$ pointroot、split RHS 与普通 RK4。
普通 float 档通过 V8 小桥取原 `sqrt/log1p/expm1` 的结果，避免把跨语言标量函数差
混入这次移植核对。计划中的 MP 档将对 state-dependent 的
$P,P_\theta,L,U,K,T,D,S,A$、非线性 moments 和 Newton 矩阵、Cholesky、
root 更新及判断、split flux 和 RK 状态计算使用 MP 算术。
RHS 读该 MP state，不使用先前 Kahan carry 变体。

MP 档即使规则相同也可能走不同次数或分支；源码将记录真实 root 次数、停止残差
和 fallback。两精度结果稳定也只会是有限数值证据，不是严格误差界。

## 已完成的严格身份比较

| stage | 完整输出 | 对齐的实际 trace 事件 | root 调用 | 每次 Newton 更新轮数 |
|---:|:---|---:|---:|---:|
| 43 | 42 分量逐字节相同 | 44,928 | 64 | 2 |
| 38 | 42 分量逐字节相同 | 44,928 | 64 | 2 |
| 175 | 42 分量逐字节相同 | 26,752 | 64 | 1 |

共 **126 个输出和 116,608 条实际 trace 事件**全部通过。
trace 的每个已记录数字按 binary64 字节比较，布尔判断和顺序也相同；
没有误差容忍放行。三个原归一残差分别复现为
$7.429289420154656\times10^{-9}$、
$6.419545004694028\times10^{-9}$ 和
$9.507411175182884\times10^{-10}$。
全部 192 次 root 都未用 fallback。
这是实际执行分支的身份核对，不声称穷尽全部可能的失败分支。

## 来源与边界

原参考导出句柄 79140 于 `2026-11-18 00:58:10 UTC` 真实 exit 0；
普通 float 比较句柄 90387 于 `2026-11-18 00:58:53 UTC` 真实 exit 0，
observer 分别记录约 2.002 秒和 6.003 秒。
原始 capsule、参考和 float trace 在 `n4_work/parts32-frozen-mp-baseline-v1/`。

冻结执行源：

- `frozen_stage_arithmetic_bridge.mjs`：`ca62c285779a8f1c60749bf208009f47ca887c3316015206fb1e68a1a3fe6205`。
- `probe_frozen_stage_multiprecision.py`：`a4e5297beb66c218b0b716ff27992830f2d5db6a56655ffab76c9a9b7a4af819`。

紧凑记录
[`raw_primaryb016_lam002_m20_parts32_frozen_float_baseline.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_frozen_float_baseline.json)
保留原/新来源、输出和 trace 身份及标量结果；collector 只读文件，不重跑流。
本条没有 60/90 位计算、完整尾重放、DN/Newton、全尾 Jacobian 或 CP 回写。
下一高精度档只有在绑定本源版本与这份精确 float 基线后才可执行。
