# R152：只细化已知 lifting 的 Codazzi 混合求积

**状态：已证明。** 本结论把 R146 的端点型 cell 方程分成保存 P1 correction
与完整已知 lifting 两部分。只提高已知函数的径向求积，保留原 correction
Gauss2、全部未知数及其 state Jacobian。它给一个新的有限积分方程；
不改变实际场、物理度量、角图或原 Gauss/边界方程，也不把有限求积比较
当作连续误差证书。

动机是已闭 atlas12 的实际出口单元：whole Gauss2 与分片 Gauss8 的
Codazzi 差约 `(0.495,0.445)`，而 correction 部分只约
`(0.000685,0.001089)`。数据与退出状态见
[实际局部分解](../notes/2026-11-12-fd2d-metric-atlas12-local-residual.md)。
以下恒等式不依赖这些数值大小。

## 1. 固定参数下的线性全函数算子

取固定物理径向区间 `[a,b]`，`h=b-a>0`，材料度量
`ds^2+A_p(s)^2 du^2`，其中 `A_p>0`。为避免将半径函数与单元左端混淆，
本结果把半径写成 `A_p`。采用 R149 的准确角图 `u=U(s,xi)`，
`U_xi>0`；图册与计算网格均不随本次参数 `p` 改变，真实径向接口允许
按 R141/R149 取单侧值。令

\[
c_p=A_p'/A_p,\quad b_p=(A_pU_\xi)^{-1},\quad
v=U_s/U_\xi.
\]

对完整三场 `f=(n,m,l)` 定义两分量物理 PDE 右端

\[
\mathcal A_p f=
\begin{pmatrix}
b_p m_\xi+c_p(l-n)+v n_\xi\\
b_p l_\xi-2c_p m+v m_\xi
\end{pmatrix}. \tag{1}
\]

对每个固定 `p`，这是关于全部三场及其角导数的线性算子。它保留
`U_s/U_xi` 漂移；独立 `l` 不通过未知 `n` 消元。移动图中的准确
Codazzi 方程是 `(n,m)_s|xi=mathcal A_p f`。

令 `C_y(s,xi)` 为保存网格上实际 P1 correction，角函数保留其全部有限
Fourier 项。完整已知 lifting 记为 `L_p(s,xi)`；它包括实际 seed 权重、
尾函数、冻结 coast 参考及各完整角复合。于是

\[
f_{y,p}=C_y+L_p. \tag{2}
\]

这里 `L_p` 不依赖 raw state 系数 `y`；`p` 可改变物理半径和 tail
参数。定义完整两场端点算子

\[
\mathcal E f=\frac{(n,m)(b,\cdot)-(n,m)(a,\cdot)}h.
\]

对任一固定节点、固定权的线性 cell 平均规则 `Q`，R146 方程为

\[
R_Q(y,p)=\mathcal E(C_y+L_p)-Q\mathcal A_p(C_y+L_p). \tag{3}
\]

式 (3) 的已知径向导数已经准确积分为端点差，不再对 `L_s` 求积。
它是本结果的起点；不能与早先把整个 correction RHS 作 Gauss 平均的
有限规则混为一谈。

## 2. 混合恒等式与不变的 state Jacobian

取原两点 Gauss 平均 `Q_2` 和分片高阶规则 `Q_f`，定义

\[
R_H(y,p)=R_{Q_2}(y,p)+R_{Q_f}(0,p)-R_{Q_2}(0,p). \tag{4}
\]

由 (1) 的线性及 `C_0=0`，两份零 correction 的完整已知端点差准确
相消。因此

\[
\boxed{R_H(y,p)=\mathcal E(C_y+L_p)
-Q_2\mathcal A_p C_y-Q_f\mathcal A_p L_p.} \tag{5}
\]

实现只需在原 R146 结果上加

\[
\Delta(p)=(Q_2-Q_f)\mathcal A_pL_p. \tag{6}
\]

整个附加量与 `y` 无关，所以

\[
\boxed{D_yR_H=D_yR_{Q_2}},\qquad
D_pR_H=D_pR_{Q_2}+D_p\Delta. \tag{7}
\]

这不是“小 correction”近似：对任意实际 `y`、任意处于定义域的 `p`
都是恒等式。已知 lifting 积分差可以很大，仍不改变 state 列。

**不能把零 correction helper 的 state Jacobian 加进来。**
即使在 `y=0` 求值，`D_yR_Q(0,p)` 通常仍是非零算子；函数值为零不
等于 state 导数为零。若直接组装 `J_fine(0)-J_2(0)` 并加入全部列，
就会错误地把 correction 方程也改成高阶求积。正确做法是只取式 (6)
的参数导数，或显式仅选两份零场 helper 的参数列差。当前实现采用前者，
不构造 fine 的任何 state 矩阵。

若调用者另以中央参数消去固定边界系数 `y=y(z,p)`，则最后仍作通常的
链式法则 `D_yR_H D_py+D_pR_H`。式 (7) 保留了这部分所需的原 state
Jacobian，不会遗漏准确中央边界的参数作用。

## 3. 完整参数导数

所有规则的分片端点、节点和权重均固定在计算坐标中，不依赖 `p`。
令点号表示参数方向导数，角图仍固定。则

\[
\dot b_p=-\frac{\dot A_p}{A_p^2U_\xi},\qquad
\dot c_p=\frac{\dot A_p'-c_p\dot A_p}{A_p}.
\]

记 `L=(L_n,L_m,L_l)`、`dot L` 为完整 lifting 参数导数。由乘积法则，

\[
\begin{aligned}
\partial_p(\mathcal A_pL)_n={}&
\dot b_p(L_m)_\xi+b_p(\dot L_m)_\xi
+\dot c_p(L_l-L_n)+c_p(\dot L_l-\dot L_n)
+v(\dot L_n)_\xi,\\
\partial_p(\mathcal A_pL)_m={}&
\dot b_p(L_l)_\xi+b_p(\dot L_l)_\xi
-2\dot c_pL_m-2c_p\dot L_m+v(\dot L_m)_\xi.
\end{aligned} \tag{8}
\]

所以 `D_p Delta=(Q_2-Q_f)` 作用于 (8)。式中包含实际 target profile
变化、尾函数值变化及尾角导数的全部链式项；不能仅对尾参数的线性值
求导而漏掉 `A_p`、`c_p` 的变化。

当前原生模型在独立 raw state 坐标下，已知 seed/reference 不依赖
中央控制，已知 lifting 只有显式 tail 与物理 bump 参数列；对应中央
附加列为零。此结论是该准确参数布局的事实，不是任意将来 lifting 都
可采用的假设。若换成 R150 的中央参数已包含于 lifting 的定义，就须
提供它的完整中央列，不能继续沿用这个特定零列。

## 4. 低模、高模与稀疏存储

固定计算标签上的保留投影、余投影以及 R142 的 D2 等距行压缩都是
与 `y,p` 无关的线性映射。因此可以对 (4)–(8) 的完整函数先相消，再
投影，或分别投影后相加，数学结果相同。

当前消费者保留原 R146 的 low rows、high rows、所有 state 列顺序。
已知附加量先按完整角函数累计，再取 low 与 high-D2 行。参数附加块
只放到原 shared-parameter 列区间；原 state 子矩阵逐列复制回去。
故 R142 的有限角目标与行归一不变。全部真实 high 最大值仍从完整点值
输出，不能把压缩行的大小冒称为全角界。

consumer 的 `point_gauss` 与 `quadrature_points` 仍是原实际场的
Gauss2 样本，保证现有 chunk 拼接约定不变。已知高阶求积的点与权重另
在 metadata 中逐 cell 保存；它们不替代 actual-field Gauss 样本。
原节点 Gauss、端点两场、独立 `l`、gap 等方程均由原 caller 保留。

## 5. 本实现的实际分片与低正则性含义

`fd2d_gc_hybrid_lifting_codazzi_d2.py` 只绑定已闭 R149 affine
`RulingAtlasRawBumpDAE`。common 径向 split 包括：

* 物理 profile 的真实段界、bump 支撑界；turn 内 `.08,.92` 的片界；
* 显式 seed 窗界与实现中被代数替换的 legacy seed 界；
* tail 径向 lifting 窗 `.42*end,end`；
* coast `e,e+rim,f-rim,f`；
* 原角图 blend 界与自然母线 atlas 的实际接口。

所有这些量在当前固定物理 `s` 模型中独立于 `p`。每个真子片通常采用
Gauss8。若物理段界与已合并计算节点相差只有几个 binary64 ulp，不能
表示全部内部 Gauss 点，则保留该子片完整的正权重，用明确记录的单点
规则；有可表示内点时取内点，否则取实际左端点。没有删除该物理子片，
也没有把这种情况宣称为八阶规则。后验若用到它，应支付该记录规则的
实际误差及必要单侧跳项。

tail 的 `kappa(A_p(s) sin U)` 活动界一般随角度与 `p` 改变，不是
共同的固定径向 knot。实现保留其原分段光滑函数在每个固定求积点的值
与全部解析参数导数，不把这些活动界伪造为参数无关 split，也不遗漏
其链式导数。Gauss8/Gauss12 的实际比较只是有限诊断，尚非严格余项。

混合与准确平均之间的恒等式为

\[
R_H-R_{\rm exact}=(I-Q_2)\mathcal A_p C_y
                  +(I-Q_f)\mathcal A_p L_p. \tag{9}
\]

因此后来可以分别支付 correction 与已知函数的积分余项。R143 的
分片 W1/W2 规则可直接用于相应部分，不需要凭 Gauss8 的名字引入
`C16`，更不需要给最终位置图新增 `C3` 条件。若导数在真实片界不匹配，
就分片或计入该跳项。

更粗但通用的说明是：对子片 `[a_j,b_j]`，将记录节点写成
`a_j+h_j*t_k`、局部权为 `w_k`。对该片 Lipschitz 常数 `M_1` 的函数
`F`，即使浮点记录权之和不是数学上的精确 1，也有

\[
\left|I_jF-\sum_kw_kF(t_k)\right|
\le h_jM_1\sum_k|w_k|\int_0^1|t-t_k|\,dt
+\left|1-\sum_kw_k\right|\sup|F|. \tag{10}
\]

它由把每个点值与同一准确平均相减直接得到。乘以 `h_j/h` 再求和
可得 composite 规则的界。此式只解释如何为实际记录规则支付余项；
本结果没有替未求出的主场提供缺失的连续常数。

## 6. 不自动覆盖新的非线性 Gauss-l 窗

R153 后续表示拟将
`l=l_raw+w((K+m^2)/n-l_raw)`，只在明确正 `n` 的活动窗内使用。
这个额外未知非线性项不是本文件的完整已知 `L_p`。
当前代码故意只接受原 affine provider，防止把原 endpoint Gauss2
矩阵错当为新实际场的矩阵。

可以把本结果用于该新表示的原 affine background，再为实际新增
`Delta l` 的 PDE 项 `c Delta l` 与
`(Delta l)_xi/(A_p U_xi)` 分别追加一致的真实求积、state 列与参数列。
但那是明确的新组合，不能以 (7) 为由忽略未知非线性修正的导数。
同样，若将来角图或分片节点依赖参数，就必须另付其参数导数。

## 7. 实际消费者与检查对象

入口为

```python
gauss_cell_codazzi_hybrid_d2(
    problem, vector, order=2, high_weight=1., jacobian=True,
    known_order=8, point_batch=8,
)
```

它遵守现有 chunk consumer 的返回结构。已知函数求值每次至多
`point_batch` 个径向点，不构造高阶 state Jacobian。当前独立小检查
只绑定已闭 atlas12 首批接受态的实际 cell 71，比较原 G2、hybrid G8、
hybrid G12，检查零 correction 恒等式、原 state 全列完全相同和非零
tail/profile 参数方向。真实运行结果、原始输入身份及失败/成功退出
由配套闭存 manifest 单独记录，不以本证明代替实际执行记录。

## 8. 已实际运行的一个小见证

`fd2d-metric-hybrid-lifting-cell-check.py` 已对上述不可变 b1 接受态的
cell 71 真正执行：unified-exec session `34047`、completion chunk
`d54522`、exit `0`；耗时 `14.132371968` 秒、峰 RSS `86980 KiB`。
只装配两节点局部视图，未构造全域 BVP 矩阵。

报告为
`notes/2026-11-12-fd2d-metric-hybrid-lifting-cell71-01-report.json`，
SHA256 `97ea6fb00509ac8cd5452a929e64d9d4adb54d46a47212c3b7dcd597659dd8a3`。
全部实际检查通过：

* 原 state Jacobian 的完整列区间与 G2 逐值完全相同；
* 用冻结 endpoint consumer 在真子片分别计算零 correction，再按片长
  加权，核对式 (4) 的 low/high/full 恒等式；
* 原 local provider 的 F、三场、向量、mesh、chart 及原实际 G2 点上的
  Gauss 值均无变化；
* tail 与物理 profile 两组参数方向的完整 JVP 及新增 known-lifting
  JVP 均非零，分别与同一实际方程的中心差分核对。

tail 方向的完整 JVP 相对 L2 差约 `6.19e-8`，新增部分约 `3.63e-8`；
profile 方向分别约 `5.68e-10`、`3.78e-10`。方向、解析值及差分值
保存在 witness NPZ 中，未用一个零列冒称非零参数检验。

本单元所有真子片均能表示完整内部 Gauss 点，未触发窄片 fallback。
known Gauss8/Gauss12 的完整角函数最大差为 `8.74637496e-9`，
low/high 压缩行差约为 `2.73e-10`。原 G2 的 full 峰约 `2.60300591`，
hybrid G8 与 G12 分别约 `3.07804528914`、`3.07804528914`。
这是对已确认漏积分的一致修正，不是声称残差已经变小或解已收敛；
该阶数比较也不是严格连续误差界。
