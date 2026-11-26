# B030 真工作行交换与 SLSQP 曲率：原终态和源码证据

2026-11-27，会话 `Astra-new-mechanism-1f4a61a4-20261127`。
可信度：原日志观察、官方源码的控制流结论，以及明确的新算法设计；没有新增科学求值。

## 1. 原 33 次调用，实际 32 次交换

直接继承已登记的[完整原终态](2026-11-27-r566-physical-epigraph-original-terminal.md)：
run [45892179085](https://github.com/Rogerhu12/math-research-public/actions/runs/45892179085)，
job `140157246913`，source `1530094182e7409efe4fd040b9daa843389fbe2c`。
完整原 stdout 为 24,320,183 B，SHA-256
`fb0591bef629a409e8e720154ca19a93bc7559c308bbd6f08b79e5566aa5a674`；
原 FINAL 为 575,651 B，SHA-256
`fca44b01c14b3a220f6d9116615e97371c887c2f67082e538f55f6e5bdfd9bb7`。

已有原事件包含 33 条 `WORKING_ROWS_BACKEND_START`、33 条完整
`WORKING_ROWS_JACOBIAN`、32 条 `WORKING_ROWS_OUTER_COMPLETE`。
FINAL 的 `cost.counts.working_jacobian_seconds` 是
**520.4795086719993 秒**，`working_direction_blocks=1548`。
每次原调用恰有一个完整 J；没有原 backend 自然返回。

| 原完成原因 | 次数 |
|---|---:|
| `required_coarse_row_exchange` | 6 |
| `complete_fine_peak_exchange_preserved_after_epigraph_lift` | 16 |
| `complete_fine_actual_peak_exchange` | 9 |
| `complete_geometry_restoration_reached` | 1 |

合计是 **32 次完成的库 / phase 交换**，不能写成 33 次交换。
最后第 33 次在原 1519 个定位 bracket 中完成 391 个后到时；其余 1128 个后来
已由另一个真实续算处理。这里不重放这批队列或已付 Jacobian。
原完整费用 2370.192668793 秒与全部更早成本仍属于原收据，不因本次文本解析再加一次。

## 2. 官方控制流给出的新结论

核读的主来源是 SciPy Developers，*SciPy 1.17.0*，2026，tag `v1.17.0`：

| 官方源 | 字节 | SHA-256 |
|---|---:|---|
| [`_slsqp_py.py`](https://github.com/scipy/scipy/blob/v1.17.0/scipy/optimize/_slsqp_py.py) | 24296 | `c8362e8d36440f3de97b58562aadb86661271ea7f66160505f51a601aff71609` |
| [`__slsqp.c`](https://github.com/scipy/scipy/blob/v1.17.0/scipy/optimize/__slsqp.c) | 33406 | `bc6516a9c65eb4b43d823c13c44c8fa02bc9486af87c17e7ffe1ec21b9dbd25b` |
| [`__slsqp.h`](https://github.com/scipy/scipy/blob/v1.17.0/scipy/optimize/__slsqp.h) | 17294 | `4888eb0a72734e36d09f7bbae3290f3c68451c2b14258da56fc360b0f9b9a3b9` |
| [`__nnls.c`](https://github.com/scipy/scipy/blob/v1.17.0/scipy/optimize/__nnls.c) | 9982 | `bf9228b49a696cae15b26c24275508580d7965726df08efbcd91cf04d8e548a2` |
| [`__nnls.h`](https://github.com/scipy/scipy/blob/v1.17.0/scipy/optimize/__nnls.h) | 654 | `a68f214a640c08fe382cb69e829afe79767f91f6744f043d1da9d08e0d957857` |

这里 C 主源 Git blob 是 `becae58b1abf9da37e184ae003a4650d1e79f363`，
header 是 `752821d88dd3f706a8bbecf94cafe3b69ba0bb15`。
主源说明沿用 Dieter Kraft，*Algorithm 733: TOMP—Fortran Modules for
Optimal Control Calculations*，ACM TOMS 20(3), 1994, pp.262–281，
[DOI](https://doi.org/10.1145/192115.192124)；本控制流结论以实际 C/Python 源为准。

Python `_minimize_slsqp` 在 `state_dict['iter']` 增加时调用 callback。
第一次 C `MODE0` 先把 BFGS 因子置为单位阵，求第一个 QP，形成一次
`mode=1` 的试探点，返回 Python。Python 先计算该试探点的目标 / 约束值，
随后便调用 callback；此时尚未要求新点的 Jacobian。
只有 callback 未中断、原线搜索走到 `mode=-1` 后，Python 才计算新 J，
下一次 C `MODEM1` 才作真正 BFGS 更新。

因此结合原每次仅一个完整 J 的实际事件，**这 33 次调用都在第一次能够形成
新 secant 更新之前被原交换或时钟中断**。原已经保留“无交换时继续同 backend”
的机制，但该原段没有实际走到这种情况。这解释了为什么原段并没有跨交换学习到
非平凡的准 Newton 曲率；不是在未输出时猜测某个内部 H 的数值。

原 stdout 没保存 H、QP 乘子或其完整加权梯度，后继不能从 q 或一条步长反造这些状态。
新算法第一次进入仍必须从 **H=I** 开始。

## 3. 新输入应如何消费真 secant

此处给出随后实现的明确协议，不提前声称它改善实际求解。
变量仍是原 $x=(q,e)\in\mathbb R^{82}$，目标仍是原 $f(x)=e$，
每条工作约束仍按原代码定义为 $c_i(x)\ge0$。完整 coarse、永久 fine、
所有已枚举角峰、nested 和原物理 margin 的接受链不变。

在一个真实 QP 后，从它实际使用的 J、梯度与乘子记录

$$
g_*=\nabla f(x_*)-J_{\mathcal I}(x_*)^T\lambda_*.
$$

这是同一次 QP 在原点 $x_*$ 的量，不能拿 callback 的 raw 试探点替换 $x_*$。
原 C `buffer` 中的 `x0` 与 `v` 在该返回处恰保存这两个量。
所有非零乘子必须连同准确行语义保留；不设省略小乘子的阈值。
box 乘子不进入这条原 C 的加权梯度；其行是线性的，对固定乘子的 secant 差为零。

下一次原流程本来就需要当前点 $x_+$ 的完整新 J。只有模型、参数顺序、目标、
phase、FFT 角网、原物理阈值等语义不变，并且每条旧非零乘子行都仍同义存在时，
才取这个已经付费的新 J 中对应的旧行，形成

$$
s=x_+-x_*,\qquad
y=\bigl(\nabla f(x_+)-J_{\mathcal I}(x_+)^T\lambda_*\bigr)-g_*.
$$

这两端使用同一冻结的 $\lambda_*$ 和同一旧行库的函数。
新增行的乘子在这个更新中是零；新 QP 自身仍包含全部当前工作行，且重新求其真乘子。
旧非零乘子行缺失时跳过更新。目标 / phase / 模型 / 参数顺序或角语义改变时，
重置 H=I 并丢弃 pending secant。单纯改变线性 trust box 的右端不会改变非线性行函数。
若旧字段对应四点 orbit 的 `min` 换了活跃分支，原 J 仍是其实际所选分支导数；
该 secant 只是分段光滑函数的数值近似曲率，不是经典光滑 Hessian 或收敛定理。

对一个正定近似 H，令 $b=Hs$、$h=s^THs$。若 $s=0$、数据非有限或更新不可靠，
跳过并说明实际原因；不另付一轮旧 J 来制造可更新数据。
其余情形使用原 Powell 阻尼形式：若 $s^Ty\ge h/5$，取 $r=y$；否则取

$$
\theta=\frac{4h/5}{h-s^Ty},\quad
r=\theta y+(1-\theta)b,\quad
H_+=H-\frac{bb^T}{h}+\frac{rr^T}{s^Tr}.
$$

在精确运算下 $s^Tr>0$，该 BFGS 更新保持正定。
浮点实现另作明确的正定近似规整和 Cholesky 检查；这些只是新 QP 初值策略，
全部耗时计入新科学时钟，不是几何或等距资格。
一次已消费的 pending secant 立即清除，防止跨终态再次应用同一对数据。

## 4. 最小 native 初始 H 接口

原 C 的 `buffer[0:n(n+1)/2]` 是下三角列主序：对角存 D，严格下三角存单位 L
的元素，实际 QP 曲率为 $H=LDL^T$；不是完整对称矩阵，也不是 Cholesky 自身。
本例 $n=82$，准确为 **3403** 个数。原 `dtpmv` 与随后逐对角乘 D 的代码给出此身份。

随后最小补丁仅在 `MODE0` 原初始化处接受一个有限、对角严格正的 packed LDL
初值；首次 reset 计数仍为 1。没有 seed 时仍按原代码置 I；其后的失败 reset
仍置 I，全部 QP、增广、原线搜索、迭代判断与 wrapper 的原逐坐标 box clamp 都保留。
不通过仿射变量把原 box 换成另一类约束，不改原工作行的缩放或单位。

补丁须完整绑定上述官方源字节，公开记录构建命令、运行时版本、相同 BLAS/LAPACK
动态库身份、补丁 / 扩展哈希及构建费用；不能把新二进制称作原 wheel 的逐位相同程序。
唯一新增科学范围将从当时最新正常续算的真实自然终态接入，不能替换正在运行的
normal56e8 或 normal311。

跨段只允许必要续算输入：3403 项 H、82 项旧点、82 项加权梯度、实际非零乘子与行 key、
语义指纹、是否已消费和全部费用。完整 J、native 大 buffer、逐步轨迹与重算数据不落库。
超过声明的必要输入上限时必须显式放弃那条 pending secant，不能偷偷裁去非零乘子。
首次只有旧正常终态而无这些状态时，明确从 I 开始，随后才产生真可继承数据。

本收据仅做原日志文本 / JSON 解析和源码纸核。没有运行本地优化、ODE、区间或任何新诊断。
