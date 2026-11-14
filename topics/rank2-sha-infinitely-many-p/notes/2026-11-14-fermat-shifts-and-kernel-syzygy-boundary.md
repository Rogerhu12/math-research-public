# 原 Fermat 商移位族的准确范围：没有新增独立核方程

日期：2026-11-14。状态：**已证明的接口说明与排除路线**，不另占结果编号。
依赖 [R530](../results/R530-divided-graded-connection-full-integral-gauge-and-mixed-second-precision.md)。
本记录排除“继续增加移位参数，就自动得到新的独立 Smith 条件”这一用法；
不否定 R530 两端整性、完整进位和固定精度范数结论。

## 1. 所有移位实际生成什么来源操作

固定奇素数 $p$，令
$$
Q_p(z)=\frac{z^p-z}{p},\qquad
\Delta f(z)=f(z+1)-f(z).
$$
对 $0\le r\le p-1$ 置
$$
D_r(z)=\Delta^{p-r}Q_p(z).
$$
因为
$$
\Delta Q_p(z)=\sum_{j=1}^{p-1}\frac1p\binom pj z^j\in\mathbb Z[z],
$$
全部 $D_r$ 属于 $\mathbb Z[z]$，且
$$
\deg D_r=r,\qquad [z^r]D_r=\frac{(p-1)!}{r!}\in\mathbb Z_p^\times.
\tag{1}
$$
有限差分的最高系数公式直接给 (1)；包括
$D_0=(p-1)!$。所以 $(D_0,\ldots,D_E)$ 对每个
$E\le p-1$ 都是 $\mathbb Z_p[z]_{\le E}$ 的一组整基。

在 R530 的同一 canonical 来源中，
$\nabla b_{m,j}=j b_{m,j}$，$0\le j\le e_m\le E_N<p$。
所有平移 $Q_p(\nabla+\alpha)$ 的整线性组合因此包含
每个次数 $\le E_N$ 的 $\nabla$ 多项式，特别包含准确谱投影
$$
\Pi_j=
\prod_{\substack{0\le u\le E_N\\u\ne j}}
\frac{\nabla-u}{j-u}
\quad(0\le j\le E_N).
\tag{2}
$$
所有分母均是 $p$ 单位。它们满足
$$
\Pi_j b_{m,v}=\mathbf1_{j=v}b_{m,v},\quad
\Pi_j\Pi_v=\mathbf1_{j=v}\Pi_j,\quad
\sum_j\Pi_j=1.
\tag{3}
$$
反过来，每个 $Q_p(\nabla+\alpha)$ 已经在这些同一谱空间上对角：
$$
Q_p(\nabla+\alpha)=\sum_{j=0}^{E_N}Q_p(j+\alpha)\Pi_j.
\tag{4}
$$
故移位族的 $\mathbb Z_p$ 线性张成准确就是“按 canonical
$t$ 次数 $j$ 取值”的全部对角来源算子；同一 $j$ 的不同权 $m$
仍被共同作用。这里没有把不同 $m$ 的来源偷偷分离。

式 (2) 可在同一 conductor·$\mathcal B$ 呈示中逐列执行。
如只读模 $p^\nu$，每个系数或谱值都可选
$0,\ldots,p^\nu-1$ 的整数代表，支付实际有限精度范数。
如果需要特征零全局有理范数，则仍须计入 (2) 的分母和组合系数，
不把 $p$ 整性等同于无成本的全局操作。

## 2. 完整左右配对属于原核方程生成的理想

令 $M:V\to W$ 为 R530 声明的同一实际整矩阵；不扩大原来源。
对任意整来源算子 $Q:V\to V$ 和整目标算子 $F:W\to W$，
定义
$$
C=MQ-FM.
\tag{5}
$$
对任意列 $P\in V$、行 $\lambda\in W^*$，准确有
$$
\lambda CP=(\lambda M)QP-\lambda F(MP).
\tag{6}
$$
因此在坐标环中，左边属于 $(\lambda M)$ 的全部坐标与
$(MP)$ 的全部坐标所生成的理想。这是特征零的完整整身份，
不是只在约化后成立。

特别，对同一模 $p^\nu$ 的完整左右核，
$$
MP=0,\quad\lambda M=0\pmod{p^\nu}
\quad\Longrightarrow\quad
\lambda CP=0\pmod{p^\nu}.
\tag{7}
$$
不需要先假定 $Q$ 保右核或 $F$ 保像。相反，(7) 也不证明
这两种稳定性。

在 R530 中，按权将
$$
C_\alpha|_{V_m}=
(\mathscr F_{m,\alpha}-\mathscr F_{*,\alpha})M_m
$$
拼成一个真实全来源矩阵，完整整身份恰是
$$
C_\alpha=M\mathscr Q_\alpha-\mathscr F_{*,\alpha}M.
\tag{8}
$$
全部 $P_{134}/U_0$、Gaussian 双交换子、原两次 wrap 和 conductor
都已经在这些真实矩阵中，不因本记录被截去。
R530 的混权配对就是 (6)–(7) 对 (8) 的使用。

取任意多的 $\alpha$、整线性组合或有限差分，仍留在同一个
核方程理想中。将它们重排成 (2) 的谱投影不会改变这一事实。
因此，仅增加这些等式的个数不能独立降低同一 $M$ 的 Smith 指数，
也不能由来源投影直接推出实际右核逐 $j$ 分裂。

## 3. 后续必须支付的输入

这个范围说明仍允许用完整目标式计算某个候选的实际值。
若一个候选只满足较弱的低行、未完成的提升或部分左核条件，
全式可能排除该候选；那时必须显式使用它尚未满足的原完整方程，
保同一来源、同一修正和全部进位。

若要将 $Q$ 作用成 Bockstein 核上的内在算子，需先证它保持
$\ker\bar M$；若要让 $F$ 作用在真实余核上，需先证它保持
$\operatorname{im}\bar M$。R530 的整性没有自动给这两个输入。
一旦已有完整模 $p^\nu$ 左右提升，(7) 本身不再是独立障碍。

所以后续回到原实际候选、真实 $\alpha/\beta$ 连接、forcing 与
未付补域，不继续把移位族的形式增广当作新的中央约束。
主问题的固定曲线和无穷素数量词均未改变。
