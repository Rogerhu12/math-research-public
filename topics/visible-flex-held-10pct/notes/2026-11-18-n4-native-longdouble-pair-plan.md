# n4：同库 long double 状态／完整 Jacobian 探针入口

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 当前只完成源码与元数据

[native double 基线](2026-11-18-n4-native-double-exact-baseline.md) 已真实通过全部 126 个输出和 116608 条事件的字节身份。本条在它之后准备唯一的原生 `long double` 探针；**目前没有执行新的 long double flow 或 Jacobian**。

新增入口为 `scripts/resume_n4_tail/native_extended/probe_native_longdouble_pair.py`，SHA256 为 `4d6b143bfda1c7ba04e1538aeeade874bc5df3d011fc181d7a3ea3b8ed8865dc`。冻结计划为 `n4_work/native-longdouble-pair-v1/plan.json`，SHA256 为 `b30bdac3396a3ba141b72d3ec0aa67c989cab5da2ef0602db82973acbfb3bd5b`。紧凑元数据记录是 `scripts/resume_n4_tail/native_longdouble_pair_entry.json`。

准备过程只做 AST 语法解析、来源哈希核对和读取已有终态；没有导入新探针、加载共享库或调用数学内核。主 C++ `916d0a…`、原 ABI harness `42893f…`、build `6a3bccea…` 和已编译共享库 `d31cd86…` 均不改动，不重新编译。

## 固定的六次调用

计划只处理原 stage 43、38、175，每段依次调用一次 state-only、一次完整 40 列 Jacobian，总计六次。每次都以同一 C ABI 的 scalar mode 1 调用 `vf_run_stage`，传入空 callback 指针；没有额外 traced run、自动重试、精度扫描、全尾 batch 或 DN。

这里的 `long double` 是已确认平台上的 **64 位有效二进制精度**，存储占 16 字节，其中 10 字节为 x87 有效编码；不是 binary128。每个输入仍是胶囊中冻结的原 binary64 state、trig、profile 系数和 RK 横坐标。唯一精度提升发生在 state-dependent 原 formed-moment 根和原普通 RK 的算术中；没有夹带 shifted root、Kahan/Neumaier 或线性项分拆。

每段的两种模式必须同时满足：

- 全部 42 个状态的原生 10 字节编码逐位相同，包含两个 mean；
- 全部 42 个输出 binary64 编码逐位相同；
- 可取得的原根诊断聚合逐位相同，包括根数、更新总数、fallback 数、域最小读数和最大相对停止残差。

这些是明确的同态检查，不用误差容忍替代。任何 native 失败、状态身份不符、输入被改写或环境控制字变化都保存现有结果并终止该轮，不用另一变体补跑。

每次成功调用立即在 scratch 保存独立 checkpoint。完整 Jacobian 模式还保存 **全部 $42\times40=1680$ 个原生编码和 binary64 输出**，包括 mean 行，便于后续独立比较。Git 中只保留源码、协议、来源与标量。

## 根、隐式 Jacobian 与尺度

原根的 30 次上限、20 个减半因子、域 floor、停止和 fallback 常数均由同一个已审 C++ 内核检查。null trace 下保留全部 `VFDiagnostics` 聚合；它不能给出未保存的逐根迭代或减半序列，记录不会把更新总数误写成逐根次数。

完整 Jacobian 使用已审的字面有限根方程导数，独立组装 $B^{exact}$ 并检查真实分解枢轴。没有把原 Newton 矩阵的正定性当作新矩阵的证据，也没有使用 $E=1+w^2$、$pref\,TF=\sigma$ 或另一套 fast-Jac trig 的约简。

它是在近似返回根处评价的隐式方程导数，不是对有限次数 Newton、停止分支或 roundoff 算法作微分。原 stage 输入直接复制原节点坐标；切向量初值前 40 行是单位阵、两个 mean 行为零。原输出 $\pi$ 行的 portRatio 除法留在边界外，不额外对输入列乘 portRatio。

## 真实运行环境与计时

计划在每次调用前后读取 ABI 大小、FE 舍入模式和 x87 控制字，检查 nearest 与 64 位有效精度。也保存该进程实际 `/proc/self/maps`、映射文件的哈希，以及从已加载库句柄解析的 `sqrtl`、`log1pl`、`expm1l` 符号 provider。`dladdr` 这里只查询身份，不调用数学函数；符号解析不能证明某函数的调用次数，也不能排除编译器将某次平方根实现为指令。

计时分为三项：`kernel_seconds` 是无 trace 的 native `e.flow` 墙钟，包含其内部临时分配；FFI 墙钟还包括 Engine 构造和输出编码；Python 的编码解读、哈希及 MP90 比较另计。三段计时不是完整 2304 段实测，不能把原有带 trace 的 double 计时混入比较。

## 对照与未付的门

状态精度将只读既有 MP90 最后 42 个输出，分别比较原生值和一次最终 binary64 转换后的值，覆盖两 mean 和原物理行归一误差。固定 target 的残差也记录，但不以 target 残差更小来选择算法。

[独立变分参照](2026-11-18-n4-saved-mp90-variational-reference-plan.md) 由另一份源沿保存的 MP90 state／L 评价解析偏导和 MP LU，再推进变分 RK；不重新计算非线性 MP 根或流。本探针只保留全部切向量供随后比较，尚不宣称独立 Jacobian 数值验证通过。

long double 的真实六调用终态、同态、对 MP90 的精度、独立全部 40 列变分对照、完整 batch 接口、原 tail norm 与 $2\times10^{-9}$ 门、最终 audit 和 coupled prefix 仍分别待做。本条没有新增 actual-tail 接受、连续流误差界或闭合几何结论。
