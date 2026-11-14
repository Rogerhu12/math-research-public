# R159：准确消元后逐节点、逐格累加正规方程

**状态：已证明；附一次真实有限状态的局部矩阵及受约束方向对照。**

本结果只改变有限最小二乘方向的装配方式，不改变实际场、物理度量、径向网格、角基、任何残差权重或求解器的可行域。它不证明目前保存的场满足几何、Gauss–Codazzi 或本课题强目标。当前 16 末态仍是未收敛的研究输入；本结果也不把节点残差当作格内或连续残差界。

配套说明和全部复现身份见 [实际消费说明](../notes/2026-11-12-fd2d-metric-local-normal-system.md)。主要源为 `scripts/fd2d_gc_local_normal_system.py` 和 `scripts/fd2d_gc_positive_trace_stream_normal.py`；原 `fd2d_gc_positive_trace_bounded_schur.py` 保持不动。

## 1. 有限对象及局部性

固定一次方向计算的当前实际参数与场。设保存网格为

\[
s_0<\cdots<s_{N-1},\qquad y_i\in\mathbb R^q,\qquad p\in\mathbb R^P.
\]

其中每个 `y_i` 保存独立的原始 Fourier 系数，顺序为 `n,m,l`；`p` 的中央、尾和物理 profile 三个切片使用实际 provider 明示的切片。特别地，[R158](R158-exact-angular-nesting-with-fixed-tail-degree.md) 的 `K=31, tail_count=16, profile_count=7` 给出 `P=54`，不能改解码为 `2K+1+7`。

实际完整场不是这些有限系数本身：它还包括原先明确的全角 seed/tail/coast lifting、[R149](R149-frozen-ruling-atlas-with-full-functional-traces.md) 的 atlas、[R153](R153-positive-n-local-Gauss-parameterization.md) 的局部 Gauss-l 商，以及 [R155](R155-positive-II-branch-from-nonnegative-flat-tail.md) 的末端正 trace 映射。这些定义必须完整保留。

**局部性命题。** 对当前真实表示，下列每类有限残差有相应依赖关系：

1. 一个节点的 Gauss、形式曲率及其角补余只依赖 `(y_i,p)`。
2. 一个径向格的完整 endpoint/Gauss2 Codazzi 及其角补余只依赖 `(y_i,y_{i+1},p)`。
3. 一个格内部任意固定求积点的实际 Gauss 或曲率也只依赖 `(y_i,y_{i+1},p)`。
4. 中央 gap 和参数约束只依赖 `p`；原中央/cut 线性边界行只依赖相应端节点及 `p`。

**证明。** 原始 correction 在格内按保存的 P1 函数精确定义，其值与径向导数只用相邻两组系数。Fourier 求值、角微分和角投影只混合同一个径向点上的角系数。已固定的 atlas 在该点求值，所有物理参数在同一个全局 `p` 中；冻结 coast reference 不是额外未知量。[R153](R153-positive-n-local-Gauss-parameterization.md) 与 [R155](R155-positive-II-branch-from-nonnegative-flat-tail.md) 都是在该点对完整场做代数映射，其链式导数不会引入第三个径向节点。[R146](R146-exact-lifting-endpoint-Codazzi-quadrature.md) 的准确端点项和 [R152](R152-hybrid-known-lifting-Codazzi-quadrature.md) 的已知 lifting 细求积只加入同一格端点或该格内部的函数值；已知 lifting 的全部参数列仍属于 `p`。因此四项成立。∎

该命题同样适用于新加入的格内 Gauss/曲率行。不要求它们恰好有某个固定行数，也不要求其残差对 `y` 线性。只需在当前点采用完整的真实 Jacobian。在曲率罚项的分段活跃规则处，本结果保持原代码所选的局部导数规则，不另外声称不可微点存在经典导数。

## 2. 原有准确变量消元

对节点 `i`，设消元后的自由变量为 `v_i∈R^{k_i}`。原方向严格写成

\[
\delta y_i=Q_i v_i+P_i\delta p. \tag{1}
\]

这里 `Q_i,P_i` 完全取自原 `bounded_bump_direction`：

- 在每个准确中央柱节点，全部原始场系数都固定；仅 `n` 的方向为 `C δc`，其中 `C=problem.core_coefficients`。这些列进入 `P_i`，不能直接删除。
- 在准确 cut 节点，全部 correction 方向为零。
- [R153](R153-positive-n-local-Gauss-parameterization.md) 的整个 P1 帽支撑落在 `w=1` 内时，原始 `l` 帽函数在实际场中恒不出现，故对应列删除。跨 rim 的帽函数不删除。
- [R155](R155-positive-II-branch-from-nonnegative-flat-tail.md) 的整个 P1 帽落在末端正 trace 平台时，保留原始 `n` 方向，规定原始 `l` 方向为其相反数。因此局部有效列是 `J_n−J_l`。没有额外乘二；`d=n−l` 对保留变量的导数二已经包含在这一列差中。
- 其余原始字段方向保持单位映射。

这些规则不混合不同径向节点。`Q_i` 的列只在同节点内有 `1` 或 `−1`；`P_i` 非零只发生在准确中央映射的参数列。全局自由字段顺序仍是原始字段编号删去固定列后的升序，和原求解器一致。

设一组原始局部行的线性化为

\[
r+\sum_{i\in I}J_i\delta y_i+J_p\delta p,
\]

其中 `I` 为空、单节点或相邻两节点。代入 (1) 得

\[
r+\sum_{i\in I}A_i v_i+B\delta p,
\quad A_i=J_iQ_i,
\quad B=J_p+\sum_{i\in I}J_iP_i. \tag{2}
\]

**必须先形成 (2)，再平方及计算列范数。** 例如 terminal 的 `J_n` 和 `J_l` 可能相消；分别平方再相加会遗漏交叉项。中央映射中 `J_p` 与 `J_iP_i` 也存在同样的交叉项。配套实现先形成实际局部 `A_i,B`，然后才执行以下累加。

## 3. 正规方程及块三对角结构

将所有实际残差行分为局部组 `b`。目标的线性模型为

\[
\frac12\sum_b\left\|r_b+\sum_{i\in I_b}A_{bi}v_i+B_b\delta p\right\|^2. \tag{3}
\]

令 `v` 为全部自由字段的连接向量。正规矩阵与梯度按下式逐组相加：

\[
\begin{aligned}
D_i&\mathrel{+}=A_{bi}^{T}A_{bi},&
U_i&\mathrel{+}=A_{bi}^{T}A_{b,i+1},\\
(H_{fp})_i&\mathrel{+}=A_{bi}^{T}B_b,&
H_{pp}&\mathrel{+}=B_b^{T}B_b,\\
(g_f)_i&\mathrel{+}=A_{bi}^{T}r_b,&
g_p&\mathrel{+}=B_b^{T}r_b,\\
R_0&\mathrel{+}=r_b^Tr_b.&&
\end{aligned} \tag{4}
\]

`U_i` 仅当同一组确实同时涉及 `i,i+1` 时加入。于是

\[
H_{ff}=\operatorname{blocktridiag}(U_{i-1}^{T},D_i,U_i). \tag{5}
\]

允许 `k_i=0`；准确中央及 cut 的零大小自由块不造成任何数学困难。

**定理 1。** 公式 (4) 与先构造完整消元后 Jacobian `\widehat J=[J_f,J_p]`、再计算 `\widehat J^T\widehat J` 和 `\widehat J^Tr` 完全相同。字段块只可能连接相邻径向节点；全局参数产生的连接全部保留在 `H_fp,H_pp` 中。

**证明。** 将 (3) 展开。每组平方的二次、一次及常数项恰为 (4)。由于一组至多含相邻两节点，非相邻字段变量永远不在同一平方中，因此不存在相应交叉项。中央映射和尾/profile 参数都已进入 `B_b`，故所有全局交叉项均保留。对各组求和便是完整矩阵乘法按行分块的恒等式。∎

该证明不使用 Gauss/Codazzi 残差足够小的假设，也不使用 unknown `n>0` 的全域假设；它只要求当前实际 provider 在各已消费点有定义且返回真实导数。若当前 R153 商离开其定义域，应按原 provider 真实报错，不能由装配器修复或吞掉。

## 4. 列范数、阻尼及原受约束方向

对消元后的各列累计

\[
\nu_{fi}^{,2}=\sum_b\sum_{\text{rows}} (A_{bi})_{\text{row},i}^{,2},
\qquad
\nu_{pj}^{,2}=\sum_b\sum_{\text{rows}} (B_b)_{\text{row},j}^{,2}.
\]

采用原代码同一缩放

\[
S_{jj}=\frac1{\max(\nu_j,10^{-12})}. \tag{6}
\]

先保留 (4) 的未缩放块，再用 (6) 左右相乘。对每个原先选用的正阻尼 `λ`，得到

\[
\mathcal H_{ff}=S_fH_{ff}S_f+\lambda I,
\quad \mathcal H_{fp}=S_fH_{fp}S_p,
\quad \mathcal H_{pp}=S_pH_{pp}S_p+\lambda I,
\]

\[
\mathfrak g_f=S_fg_f,\qquad \mathfrak g_p=S_pg_p. \tag{7}
\]

这是原程序先缩放完整 `J_f,J_p` 再乘积的同一结果。阻尼加在消元、缩放后的变量空间，不提前加到原始字段中。

令

\[
u=\mathcal H_{ff}^{-1}\mathfrak g_f,
\qquad V=\mathcal H_{ff}^{-1}\mathcal H_{fp}.
\]

对称化后的 Schur 目标及梯度为

\[
\mathcal S=\operatorname{sym}(\mathcal H_{pp}-\mathcal H_{fp}^{T}V),
\qquad h=\mathfrak g_p-\mathcal H_{fp}^{T}u. \tag{8}
\]

继续采用原求解器相同的微小特征值保护移位
`max(0,0.1λ−λ_min(\mathcal S))I`。参数缩放后的尾 `[0,1.2]` 盒、profile 盒、中央曲率线性约束、已有 radius 线性约束及真实中央 gap 线性化等式全部保持原式。求得同一参数方向 `z_p` 后，

\[
z_f=-u-Vz_p,\qquad v=S_fz_f,\qquad \delta p=S_pz_p,
\]

最后按 (1) 回填原始变量。

**定理 2。** 在准确算术中，使用 (4)–(8) 与原完整 tall Jacobian 程序给出相同的受约束二次问题。若该二次问题可行并取准确最小点，则所得方向相同。对当前固定的正阻尼及原特征值保护，该有限二次目标严格凸，故可行时最小点唯一。

**证明。** 定理 1 给出未缩放矩阵与梯度相同；(6) 的列范数在两种计算中相同，所以 (7)、(8) 及全部变量变换相同。参数约束仍用同一实际 `p`、同一 `core`、同一切片和同一缩放，因而可行域也相同。正定性及 Schur 补的正定性可直接由对任意非零方向 `z` 有 `z^T(S\widehat J^T\widehat JS+λI)z≥λ||z||²` 得出。后续非负保护移位不会破坏正定性。最后回填的线性映射也相同。∎

这里没有声称两次浮点 SLSQP 迭代的每一位必相同。有限舍入、消去、稀疏乘法和停止判断的顺序可能不同；实际对照应报告方向及 `Jδ` 的差，而不是用理论恒等式替代运行证据。

## 5. 浮点误差及内存范围

先把传入的各局部 Jacobian 数值视为固定实数。若局部消元已经给出数值 `A_b,B_b`，对正常有限数的经典舍入模型 `fl(a\circ b)=(a\circ b)(1+δ), |δ|≤u`，令 `γ_t=tu/(1-tu)`。设总行数为 `M`、局部组数为 `B`，取保守 `t=M+B+2`。逐组 dot 与加法的累计误差可逐元素控制为

\[
|\Delta H_{ff}|\le\gamma_t\sum_b|A_b|^T|A_b|,
\quad |\Delta H_{fp}|\le\gamma_t\sum_b|A_b|^T|B_b|,
\quad |\Delta H_{pp}|\le\gamma_t\sum_b|B_b|^T|B_b|, \tag{9}
\]

以及对应的梯度界 `γ_t Σ|A_b|^T|r_b|`、`γ_t Σ|B_b|^T|r_b|`。完整 tall 乘法自身也有同类舍入界；两者差可由两套误差界相加控制。

若还将局部消元的舍入计入，令准确 `A,B` 与实际局部数值 `\widetilde A,\widetilde B` 的差界为 `Δ_A,Δ_B`。例如字段 Gram 额外项逐元素不超过

\[
|A|^T\Delta_A+\Delta_A^T|A|+\Delta_A^T\Delta_A,
\]

交叉块同样展开即可。`J_n−J_l` 的减法及 `J_iP_i` 的有限乘积给出这些常规 dot/add 界。上述界只是有限装配误差分析，不能包办原场的连续残差。本次实测报告没有把普通浮点比较值伪装成 outward-rounded 区间证书。若发生 overflow、NaN 或 provider 定义域失败，必须失败退出，不能使用 (9) 掩盖。

正规二次式还可计算线性模型残差平方

\[
\|r+\widehat Jv\|^2=R_0+2g^Tv+v^THv. \tag{10}
\]

配套代码显式记录其未截断值和各项绝对值之和。因消去导致严重负数时真实报错；极小的舍入负数只影响显示的平方根，并保留原数值。本次对照另以完整小夹具直接计算 `||r+Jδ||`，验证 (10) 的实际求值差。

存储量为

\[
O\!\left(\sum_i k_i^2+\sum_i k_ik_{i+1}
        +P\sum_i k_i+P^2\right), \tag{11}
\]

加一个节点的完整实际函数/参数包和固定数量格的局部 Jacobian。实际 Fourier 求值需要多少角点并不改变 (11) 的全域累计部分；角网格只影响当前局部包。LU/Schur 仍可使用原稀疏 factorization。并未要求新的高阶全域几何正则性或重新求解物理 BVP。

## 6. 实现及原有限目标的覆盖

`LocalNormalSystem.add(r,Jlocal,nodes=...)` 接受任意局部行，列顺序为列出的原始节点各 `q` 列，然后全部 `P` 参数列。它做 (2)、(4)，并显式拒绝连接非相邻字段节点的假局部块。生产路径不保留完整 tall Jacobian。

当前 `stream_positive_trace_normal` 对每个节点只构造一个点的 no-J 实际字段包，从这个同一包生成原 low Gauss、D2 high Gauss 与形式曲率罚项。cut、R153 恒等平台、R155 恒等平台的行选择与冻结原实现一致。节点参数列完整保留；中央参数映射在累加器中统一加入。

每个最多 `block_cells` 格的块完全复用冻结的 `gauss_cell_positive_trace`，因此 [R152](R152-hybrid-known-lifting-Codazzi-quadrature.md) 的已知 coast lifting 细规则、[R153](R153-positive-n-local-Gauss-parameterization.md) 的非线性增量及 [R155](R155-positive-II-branch-from-nonnegative-flat-tail.md) 的准确 `n` 端点增量都在同一实际 finite consumer 中。程序检查每个格行的非零字段列确实只属于该格两个端点，再逐格累加并释放块。

不同组的执行顺序是行排列；平方范数和正规方程在准确算术中不变。输出始终区别全目标和显式选择的小测试子集。为下一轮增加的格内实际 Gauss/曲率，只需追加对应两个端点局部行，并另行记录新有限目标；不能把新增行说成与旧 16 目标相同。

## 7. 一次实际对照及限度

已闭输入为 `2026-11-12-fd2d-raw-bump-trace16-b0004-accepted-0002.npz`，SHA256
`520a3e333c54bcc18da5071d8534cf91f9e6f0de60a567a5cbb56abb5e697e28`。

选择其原有 **17 个节点、11 个格**，包含准确中央映射、两 coast rim、coast 整帽消元、terminal ramp、末端迹耦合与 cut。没有改变或重新求解场。共有 **2012 行**，包含 70 个活跃曲率行；检查中仅为了独立比较而显式保存这组小行夹具。原冻结 Schur 函数直接消费该夹具，新的累加器也消费同一组实际原始局部行。

真实 `check-02` 子进程 exit 0。内部耗时 3.42725 秒，进程峰 RSS 108784 KiB。归一方式为 `max-absolute difference/max(1,max-absolute of either matrix)`；实际观测为：

| 比较项 | 差的上限或值 |
|---|---:|
| `Hff,Hfp,Hpp,gf,gp` 的上述归一差 | `1.180664e-15` |
| 字段列平方范数的归一差 | `2.759691e-16` |
| 参数列平方范数的归一差 | `9.538058e-17` |
| 残差平方和差 | `0` |
| 实际字段 normal 块带宽 | `1` |
| 原/新 SLSQP（同 `λ=.001`） | 均 success，均 102 次迭代 |
| 方向差 `||δnew−δold||/max(1,||δold||)` | `7.311548e-8` |
| 方向作用差 `||J(δnew−δold)||/max(1,||Jδold||)` | `7.469391e-14` |
| normal 二次式与直接线性残差范数差 | `1.021406e-14` |
| cut、coast 删除方向、terminal 成对方向约束误差 | `0` |
| 中央方向映射误差 | `8.470330e-22` |
| 原输入向量变化 | `0` |

这组小夹具的 tall 存储为 1,775,052 字节；累加器仍为全部原 123 节点分配 normal 块，为 5,489,096 字节。因此**不能从这个局部夹具宣称已测得全主程序峰值下降**。本结果给出完整代数等价性、可直接调用的低内存生产路径和一次实际方向核对；实际全运行的峰值由后续真实运行记录。

首次 `check-01` 的外层日志路径落在同一个 fresh-stem glob 中，触发 `FileExistsError`，真实 exit 1，尚未构造场或矩阵。日志及退出收据保留。`check-02` 只把控制台日志移到独立目录；三份已运行源码完全未改，且结束时逐一检查 source SHA 不变。

R159 无新增物理/几何完成条件，也不替代本课题对实际全图、原 `g`、连续 metric/geometry/reach 及最终展示的要求。
