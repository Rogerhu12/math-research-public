# Phi：不降 lambda 的二十二列原矩阵与固定切片保度输入

日期：2026-11-28（Asia/Taipei）。尚未执行；120 秒 / 1 GiB。使用已实际选定的十八个原列，不重新选择或重跑旧满秩门。

## 1. 新原矩阵

沿用[十八原列与非零纯权必要式](../results/R150-appendix-unit211-Phi-zero-eighteen-original-columns-and-nonzero-pure-weight-determinant.md)的九种子及固定十八列顺序。先不对 lambda 作首一六次降次，取十八条真实三坐标关系：
$$
r_0,\ldots,r_8,\quad
\lambda r_0,r_0M_T,r_0M_z,\quad
\lambda r_1,r_1M_T,r_1M_z,\quad
\lambda r_3,r_3M_T,\lambda r_5.
$$
它们仍使用原均值降低 $T,z$，因此与原乘法的差都有原三个均值来源。再添四个已刊全图原关系
$$
C_6,\quad\lambda C_6,\quad TC_6,\quad zC_6.
\tag{1}
$$
先列旧十八个低坐标 $\lambda^j(1,T,z)$，$0\le j<6$；最后列
$$
\lambda^6,\quad \lambda^7,\quad \lambda^6T,\quad\lambda^6z.
\tag{2}
$$
构成固定 $22\times22$ 矩阵 $M$。全部列均在当前旧权环的原 $I_{10}$ 中；不需要 $H_{42}$ 或斜率头 $\Delta_N$ 的逆。

记 $h=[\lambda^6]C_6$，$c_5=[\lambda^5]C_6$。最后四列在 (2) 四行上的块是
$$
\begin{pmatrix}
h&c_5&0&0\\
0&h&0&0\\
0&0&h&0\\
0&0&0&h
\end{pmatrix}.
$$
在 $h\ne0$ 图对它作固定 Schur 消元，恰返回旧十八列的首一 lambda 余式。按所列行列顺序，因而有
$$
\det M=h^4\det L.
\tag{3}
$$
这是普遍有理恒等式，不是额外计算门；未要求展开任一个 determinant，也不会将 $h=0$ 删除。

## 2. 新清分母不引入 H42

每列只有三个实际有理坐标。取三分母的完整多项式 LCM $d_j$，每次除法乘回，并核 $d_j$ 只含旧已付权。乘 $d_j$ 后得到三个 QQ 多项式，全部三坐标逐项乘回。

再以一个非零有理常数 $s_j$ 作 1009 Gauss 归一化，使该列所有系数 1009 整且至少一个系数为单位。这是一个明确常数，没有新增参数倒数。记
$$
B_{22}=M\operatorname{diag}(d_js_j),\qquad P(u,Q)=\det B_{22}.
\tag{4}
$$
于是 $B_{22}\in M_{22}(\mathbb Q[u,Q])$，所有原来源仍只有旧权分母，$P\in I_{10}$。这是实际列的 LCM 清除，避免把旧大公共乘积 $\Gamma^{90}$ 带进新的行列式。

(3) 与已成十八列结果保证新定义的 $P$ 非零。具体后续目标是取得其真实 $u$ 次数与一个完整原切片，供以后的有限整模型使用；本次不尝试排空整权图。

## 3. 严格 QQ 次数上界与真正最高系数

从 (4) 的完整 QQ 条目直接取得每个非零条目的 $u$ 次数 $w_{ij}$。Hungarian 算法选择一个最大权完美匹配，同时输出完整整数对偶 $a_i,b_j$，逐项核
$$
w_{ij}\le a_i+b_j,\qquad
D=\sum_i a_i+\sum_jb_j=\sum_iw_{i,\pi(i)}.
\tag{5}
$$
因此 $\deg_uP\le D$ 严格成立。零条目不参与匹配，不由模次数代替 QQ 次数。

固定 $p=1009,Q=2$，将所有完整 QQ 系数按其真实整模型约化。对每项取 $u^{a_i+b_j}$ 系数，组成 $22\times22$ 最高系数矩阵 $H$。由 determinant 的逐项次数展开，
$$
[u^D]\,P(u,2)\bmod1009=\det H.
\tag{6}
$$
若实际 $\det H\ne0$，立即得到
$$
\deg_uP(u,Q)=\deg_uP(u,2)
 =\deg_u\overline P(u,2)=D,
$$
包括真实最高系数为 1009 单位。若 $\det H=0$，本次只保 (5) 的上界，不能从较小模次数猜测 QQ 精确次数，也不自动换权点。

## 4. 新的固定模多项式 determinant

本源随后对同一固定 $22\times22$ 矩阵的 $Q=2$ 模多项式作一次 Bareiss determinant。每个除法实际完整乘回，临时主元的零点不被删去；输出是固定多项式 determinant 的真实约化。

记录它的次数、首项、SHA、每一步实际次数和除法返回数。如果 (6) 非零，核实际次数等于严格上界且首项相等；否则记录明确差额、保持未付次数接口。另核所得多项式在 $u=3$ 的值等于同一个矩阵的直接标量 determinant，只作同一原多项式返回的末点值身份。

没有 QQ determinant 展开、旧十八列 rank 再选择、旧大投影或原值复审。没有因模满秩、模因子或模物理 $D=0$ 而宣称全图空。整个 $H_{42}=0$、所有未付权曲线与后续原物理条件继续保留。

## 5. 不可变源与依赖

建议文件：
2026-11-28-unit211-Phi-zero-unlowered-twenty-two-original-columns-and-fixed-u-degree-8542.py。

源 blob b6423370556fa3ab664e92f025db2b2abaa8b463；10211 字节；
SHA256 043ffc06d0a48f804111ff35cbfee0922fe9a69c87c414f75099b8413cf4b53e。

新增直接依赖：

- 2026-11-28-unit211-Phi-zero-monic-six-eighteen-original-columns-and-nonzero-weight-determinant-8542.py，环境变量 ISP_PHI_EIGHTEEN_SOURCE。只取其 5956 字节必要九种子定义前缀，SHA256 94105fe17b4e239867c7969ad7e620eca5be074b00c15cb898b2cbdcc02481fb；在原固定模点、旧十八列选择之前停止。
- 该源的四个既有小源码依赖：原 centered NSPS、I10 原值、slope 均值、first-head 规则；环境变量与上次十八列工作流完全相同。

总计五个小源码依赖，无历史 JSON。所有 nested alarm/setitimer 均受同一个最初 120 秒绝对截止约束。只输出定义、原来源列表、小 profile、严格匹配对偶与小回执；不输出或保存可重算系数、矩阵、编码和分片。
