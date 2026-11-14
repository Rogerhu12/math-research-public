# 谱权正对角共轭模块：独立全文审查

审查者 `/root/tail_theory`，2026-11-09。

**结论：代数说明通过；实现以冻结 v2 为有效入口通过全文审查。** v1 的复数转 float 输入漏洞已在另存的 v2 收紧，原 v1 字节保留。本次没有运行真实或解析 BVP，没有读取候选 CP，没有 DN、root、RK 或 flow 调用。新增的实际检查仅为一次合成回调截获、十二类输入拒绝、精确有理运算及源码身份/差分。

## 1. 冻结对象和审查范围

| 对象 | SHA256 |
| --- | --- |
| 原完整代数稿 `root-spectral-collocation-conjugacy.md` | `a413fcdfe3d5fac0bbef4fc0466707fd5ddaf88d87e00924b03ea23c463067fe` |
| 原模块 v1 | `b5422e43c06bde4f988bf5a2d4331ff9fa65ecef5f11722388aa5c6f57d8575c` |
| 有效模块 v2 | `47e1128c8cabb7c77797ebea6534cf77d63964add54f78a2cab827d1f0101854` |
| 安装的 SciPy 1.17.0 `_bvp.py` | `59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2` |

已全文读两版模块、代数稿、作者两版解析检查脚本，并核 SciPy 的 `wrap_functions`、配点残差、Newton 调用、`create_spline`、`estimate_rms_residuals` 和返回对象。另读本题 adaptive-v2、warped、圆柱基底/3-fold 模式来源及原 domain-aware Newton 安装入口。十五个实际来源和完整哈希列在本审 `-sources.json`。

v2 仅增加实数 numeric dtype、参数及坐标输入门和有限严格递增网格检查。从 `weighted_fun` 到模块结尾的整个源码块与 v1 逐字节相同；`power2_weights` 及四个变换回调的 AST 也相同。没有更改方程、容差、返回样条公式或接受门。

## 2. 精确方程与全部 Jacobian

常数正对角 W 可逆；$u=Wy$ 与 $y=W^{-1}u$ 互为映射，所以原有限问题与

$$
u'=Wf(x,W^{-1}u,p),\qquad B(W^{-1}u_a,W^{-1}u_b,p)=0
$$

具有一一对应的精确解。该推论只使用 W 常数且可逆，不要求实际数值迭代路径相同。未知参数 p 不参与缩放，边界残差各行也不另加权。

源码五个导数块逐项正确：

$$
\widetilde f_u=Wf_yW^{-1},\quad \widetilde f_p=Wf_p,
\quad\widetilde B_{u_a}=B_{y_a}W^{-1},\quad
\widetilde B_{u_b}=B_{y_b}W^{-1},\quad
\widetilde B_p=B_p.
$$

RHS Jacobian 的形状为 $(n,n,m)$、参数 Jacobian 为 $(n,k,m)$；左侧 W 乘输出分量轴，右侧 $W^{-1}$ 乘状态输入轴。边界的两个 $(n+k,n)$ 矩阵分别除列权重；$(n+k,k)$ 的参数块原样保留。代码的广播轴与这些公式一致。原 callback 已含的 chart、gauge、物理参数链式项由原 callback 计算，不能在外层再重复缩放。

独立合成检查使用四状态、两参数、三个点，以及非对角稠密 RHS Jacobian、两个非零边界状态块和非零边界参数块。以 dyadic 输入保证比较不依赖舍入容差。检查器在模块将要调用 SciPy 的本地引用处截获，实际执行四个变换回调，与独立 Fraction 构造结果逐项相等；随后立即抛出专用停止异常，没有调用数值求解器。该次异常记录也按模块原协议保存，未伪造成功 BVPResult。

## 3. 权重和 RMS 方向

状态是均值径向分量加三个 M 模块，$n=3M+1$；`PlanarSymmetryFlow` 明确 `even=3*arange(1,M+1)`，继承圆柱基底按 R/T/Z 三块排列。代码用 `bit_length(9*j*j)` 得到

$$
w_j=2^{\lceil\log_2(1+9j^2)\rceil},\qquad
1+9j^2\leq w_j<2(1+9j^2),
$$

首均值权为 1，三个块重复同一权重。它不把 R/T 基向量自身的角导数、材料角图或全部 Cartesian 二阶导数直接化成这个对角范数。

对同一个物理近似函数、同一点及同一原 RHS，残差满足 $\widetilde r_i=w_i r_i$。因为 $w_i\geq1$，

$$
\frac{w_i|r_i|}{1+w_i|f_i|}-\frac{|r_i|}{1+|f_i|}
=\frac{(w_i-1)|r_i|}{(1+w_i|f_i|)(1+|f_i|)}\geq0.
$$

分量平方和及相同非负 Lobatto 权重保持方向。SciPy estimator 的三个非端点权均为正，故所述同图 RMS 不等式成立。它不比较不同求解得到的不同图，也不保证实际浮点指标严格保持形式不等式。尤其 $|f_i|$ 较大时增益可远小于 $w_i$；此权重不是对连续 metric 的直接证书。

独立 Fraction 检查包含 36 个标量符号/零值例，全部满足方向；完整证明是上述恒等式而非这些有限例。安装的原 RHS/Jacobian 已有 64 列分批；计划没有把不存在的“尚未分批”当作内存根因，也没有增添未经比较的第二套分批。

## 4. PPoly 返回轴及物理接受门

`create_spline` 先计算四个三次系数，交给 `PPoly(...,axis=1)`；构造后的内部 c 确为 $(4,m-1,n)$。将最后状态轴逐分量除 W、保留节点和 axis=1，正确给出物理未知量坐标下的同一三次插值。节点 y、节点 yp 也除 W；p 和 x 不缩放。复核 `raw.sol` 类型、axis 和系数形状后才构造返回对象，未猜测其它 SciPy API。

这里“物理 PPoly”是指状态分量已恢复到原 y 坐标。**它没有把独立变量 x 变成物理弧长 s。** 若原 prefix 以数值 t 为自变量，返回三次仍是 t 上的插值；原 `chart` 变换及物理 s 上的 C² 五次 `c2_interpolant` 仍另行执行，不能把返回三次直接写作最终 Cartesian 图。

scale_checked 对初值、返回节点、节点导数和 c 做有限性与乘除往返检查。二次幂的选择减少了正常范围内的额外舍入，但模块不声称所有浮点数据都无损；溢出、下溢异常或不能恢复时拒绝。

物理 RMS 重新用返回 PPoly 的真实导数减原 RHS，在中点及另两个 Lobatto 内点评价；不是直接把 weighted_rms 除某个常数。边界残差用恢复的原节点状态及 p 重新评价。原 `rms_residuals` 字段装入物理 RMS，weighted RMS 另存。只有 raw.success 为真且原物理 RMS/BC 两门都过，才能保持成功；物理门失败时显式改 success=false/status4。原失败即使物理指标较小，也不会被提升为成功。

SciPy 的残差估计使用 Hermite 节点残差为零的精确身份；浮点节点和真实连续区间误差仍没有严格包围。模块已经明确这是有限配点诊断，不是连续 metric/C²/reach 证明。重算中任何非有限值或原域异常向上传播，不以裁剪替代原几何定义。

## 5. v1 输入漏洞与 v2 修复

本审在 v1 找到具体漏洞：complex ndarray 经 `np.asarray(...,float)` 可仅发 ComplexWarning 并丢弃虚部，影响 weights 和 p；原 SciPy 对 x 也有类似 cast。仅加 `np.isrealobj` 仍不足，因为 object array 中的 `np.complex128` 元素会被视为 real-object dtype 后继续静默丢虚部。

纯 NumPy 转换检查 receipts `0ea5ea`、`861703` 均实际 exit0，未 import 本模块或运行 solver。它们证明的是输入门反例，未否定作者全实数解析算例。

v2 在 cast 前限定 dtype.kind 属于 `biuf`，并对 x 检查一维、至少两节点、有限及转换后严格递增。权重仍须有限、至少 1 且为二次幂；y 和缩放返回值同样拒绝 object/string/complex。参数必须非空一维并有限。S、缺失解析 Jacobian 等不支持接口继续明确拒绝。

独立实际检查 receipt `701d6a`、exit0：十二类非法输入均在任何 callback/solver 引用之前拒绝，包括普通 complex 与 object-complex 的 weights/p/x、complex y、S、空参数、缺 Jacobian、非有限和非递增 x。输入拒绝未产生 solver-start record。故最终 PASS 绑定 v2，不能把 v1 仍有的入口漏洞抹掉。

## 6. 解析算例和原 prefix Newton 的边界

作者非几何算例的独立解析公式正确：首分量 $y_0=x^2$ 给 p=2，其余为常系数线性方程的 exponential 解。已读两版 checker 及原报告、v2 observed-replay；v2 report SHA 为 `682e758be6032aae354a6630306963bcb181a24ffdcc4176f91a507c33cfcda2`。根报告实际 receipt `885818`、exit0；本审没有再次运行这两个解析 BVP。

作者算例具有对角 $f_y$、零 $B_p$，右端非零导数所在分量权为 1。故它没有单独数值覆盖非对角状态共轭、非零参数边界块与右端非单位权。第 2 节的独立稠密回调检查正补这些接口项。返回样条值/一导和物理残差的作者实际算例仍只属于接口验证，不能类推真实 M14 误差下降。

还须区分磁盘 SciPy 源与运行中函数身份。原 prefix 会执行已绑定的 `f6curve_domain_newton.install()`，将 `_bvp.solve_newton` 替换为原 domain-aware 版本。`59aff…` 只绑定磁盘布局/estimator 源，不证明运行中 Newton 未被替换。新模块没有覆盖这个 patch，可与它兼容；未来真实入口必须另绑定该模块及安装次序。当前解析算例采用未 patch 的 SciPy，不是原 prefix Newton 全链测试。

## 7. 采用条件与剩余门

可以采用 v2 作为同一有限方程的误差分配接口，前提是未来新 launch 绑定该模块、原 source-root、实际 domain Newton 入口、权重、初值、容差和资源预算。不同权重可改变数值步及自适应网格，不能宣称迭代过程逐位相同。

首先若只求冻结 affine DN 的前缀，它仍是 `actual_nonlinear_tail=false`；配点成功不能改成真实联解。必须再由原实际尾、true outer、原 physical BC 和最终 audit seam 修正。所有完整图、固定 g 的加密轨迹、角向/径向误差及 README/G5 的最终门继续独立支付。本审不构造新候选，也不改变当前 continuation03 或每请求 DN 延拓的算法。

独立检查器 `scripts/db6f-tail-review-spectral-conjugacy.py` 与其机读输出、十五源账本及实际观察记录随闭清单发布；全部无真实 solver 调用。
