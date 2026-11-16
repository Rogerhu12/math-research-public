# R864：从原尖点评价直接构造全部正则微分

日期：2026-11-16。状态：本文给出新的有限准确消费者及其完整性证明；在公开运行成功前，不声称已经取得下述实际秩和 127 个坐标列。

原输入是 [R805](../results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md) 的已认证分次自由基和 [R820](../results/R820-certified-original-cusp-finite-algebra-and-ideals.md) 的真实两图尖点有限代数。微分规范沿 [R814](../results/R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md)；真实半线性作用沿 [R860](R860-original-adjugate-semilinear-descent-and-rational-differential.md)。本篇不改变原曲线、参数、刚性化、Picard 类或高度。

## 1. 一个仅有 20 行的新准确线性问题

记原曲线为 $Y/K$，$K=\mathbb Q(\zeta)$，属为 $127$，约化二十尖点除子为 $C$。原线丛是
$$
\mathcal H=\Omega_Y^1(C),\qquad \deg\mathcal H=272.
\tag{864.1}
$$
令 $H_\tau=\operatorname{div}(\tau)$ 为原无基点铅笔的一员，并保留
$$
z=\sigma/\tau,\quad v=z^{-1},\quad
\beta_i=d_i/\tau^{\epsilon_i},\quad
\gamma_i=d_i/\sigma^{\epsilon_i}=v^{\epsilon_i}\beta_i,
\quad \epsilon=(0,1^{144},2^{127}).
\tag{864.2}
$$
R805 已证明两图所用的是完整正规环，且 $1,\ldots,\beta_{271}$ 是分次整基。它也给出 $H^0(Y,\mathcal H)$ 的下列完整、有序基：
$$
\tau,\ \sigma,\ d_1,\ldots,d_{144},
\qquad \tau=e_0,\quad \sigma=e_1+e_{73},\quad d_i=e_{i+1}.
\tag{864.3}
$$
此处 $e_0,\ldots,e_{145}$ 就是原 $V_1$ 的次序。除以 $\tau$ 后，得到 $L(H_\tau)$ 的基
$$
\mathcal B_1=(1,z,\beta_1,\ldots,\beta_{144}).
\tag{864.4}
$$
它共有 146 项。原 R805 的度一自由补基只有 144 项，不能将那个旧结果称为本篇的 127 维正则微分核。

R814 的同一微分为
$$
\nu=82\tau\,\frac{dq_Y}{q_Y},\qquad
\operatorname{div}(\nu)=H_\tau-C.
\tag{864.5}
$$
所以乘以 $\nu$ 给一个准确同构
$$
L(H_\tau-C)\ \xrightarrow{\ \sim\ }\ H^0(Y,\Omega_Y^1),\qquad f\longmapsto f\nu.
\tag{864.6}
$$
R820 已实际证明 $\tau,\sigma$ 在全部 20 个几何尖点非零，并用同一个可分有限代数
$$
F_{20}=\mathbb Q(\xi_{41}+\xi_{41}^{-1})
\tag{864.7}
$$
编码原尖点轨道；在 $K$ 上取 $F_{20}\otimes_{\mathbb Q}K$。不需要拆分任何闭点。

令 $E_i$、$E_i^\sigma$ 分别为 R820 原件中 $\beta_i$、$\gamma_i$ 的 20 个有理坐标，并令 $\alpha$ 为其已认证的 $z$ 值。定义两个原次序矩阵
$$
M_\tau=[E_0\ \alpha\ E_1\ \cdots\ E_{144}],\qquad
M_\sigma=[\alpha^{-1}\ E_0\ E_1^\sigma\ \cdots\ E_{144}^\sigma].
\tag{864.8}
$$
每个矩阵都是 $20\times146$。所有列均直接读已认证字段，没有新的 cusp Fourier 展开或域逆运算。

**定理864.1。** 对任意 $a=(a_0,a_1,b_1,\ldots,b_{144})^t\in K^{146}$，令
$$
f_a=a_0+a_1z+\sum_{i=1}^{144}b_i\beta_i.
\tag{864.9}
$$
则下列条件等价：

1. $f_a\nu$ 是原 $Y$ 上的全局正则微分；
2. $M_\tau a=0$；
3. $M_\sigma a=0$。

两个矩阵在 $\mathbb Q$ 和 $K$ 上的秩均为 19；其共同核在 $K$ 上维数 127。

**证明。** 由 (864.4)，$f_a$ 已有全局极界 $H_\tau$。由 (864.5)，$f_a\nu$ 正则恰当且仅当 $f_a$ 在 $C$ 的每个几何点至少消失一次。R820 的可分有限代数评价是整个约化尖点商，故此条件正是 $M_\tau a=0$，不是只检一个几何嵌入。R820 原两图运输给
$$
M_\sigma=Z_{\alpha^{-1}}M_\tau,
\tag{864.10}
$$
其中 $Z_{\alpha^{-1}}$ 是原有限代数中乘 $\alpha^{-1}$ 的可逆矩阵。第二张图检的是 $vf_a$ 的尖点值；因 $v$ 在全部尖点为单位，其零条件相同。最后，(864.6) 给核维数 $g(Y)=127$，所以秩为 $146-127=19$。所有输入矩阵是有理矩阵，秩在忠实域扩张 $\mathbb Q\to K$ 下不变。$\square$

## 2. 两图正则性和原 V1 坐标的具体输出

对一个核列 $a$，$\tau$ 图上的函数系数为
$$
f_a=(a_0+a_1z)\beta_0+\sum_{i=1}^{144}b_i\beta_i.
\tag{864.11}
$$
在 $\sigma$ 图，使用正规整基 $\gamma_i$，有
$$
vf_a=(a_0v+a_1)\gamma_0+\sum_{i=1}^{144}b_i\gamma_i.
\tag{864.12}
$$
令 $\nu_\sigma=82\sigma\,dq_Y/q_Y=v^{-1}\nu$。它在 $U_\sigma$ 上仅在 $C$ 有简单极点，而且 $f_a\nu=(vf_a)\nu_\sigma$；故正确的模条件是
$$
f_a\in\mathcal C_\tau,\qquad vf_a\in\mathcal C_\sigma.
\tag{864.13}
$$
不能把第二个条件误写成 $f_a\in\mathcal C_\sigma$。由 (864.11)–(864.12) 的原整基多项式界，加上两图完整尖点评价为零，(864.13) 已检查所有点，包括 $\tau=0$ 和分歧点。

对应原截面 $s_a=\tau f_a$ 的原 $V_1$ 坐标是
$$
(s_a)_0=a_0,\qquad (s_a)_1=a_1,\qquad
(s_a)_j=b_{j-1}+\mathbf1_{j=73}a_1\quad(2\le j\le145).
\tag{864.14}
$$
因此实际输出同时给出
$$
\omega_a=f_a\nu=82s_a\,dq_Y/q_Y.
\tag{864.15}
$$
这里的 $82$ 只来自原微分规范 (864.5)。R820 在同权比值中已准确消去的 $82^6$，以及原输入截面的 $82^2$，均不重新插入坐标。

## 3. 完整准确证书，不先假定实际秩

执行程序构造 (864.8) 的完整两矩阵，并只对 $M_\tau$ 作一次准确有理消元。按照从左到右列次序和从上到下非零枢轴次序，保存每个已经完成的消元阶段。实际秩必须等于 19，否则该运行不得宣称本任务成功。

记实际主元列为 $J$，非主元列为 $F$。程序输出 $146\times127$ 矩阵 $N$，其 $F$ 行是单位矩阵，主元行由实际 RREF 决定；同时保留所选 19 行和 19 列的原矩阵以及准确非零行列式。然后对所有列检查
$$
M_\tau N=0,\qquad M_\sigma N=0.
\tag{864.16}
$$
两项各含完整 $20\times127$ 个有理数等式。单位自由行证明 127 列独立，非零 19 阶子式和 (864.16) 一起证明它们就是完整核。不存在模数约化、数值零判、未知的中间 lift 或未经乘回的有理重构。

程序还逐列实施 (864.11)–(864.14)，保存原 $V_1$ 坐标及两图正规基多项式坐标，检查原截面换基的双向公式。其输出是有原来源的 127 个真实正则微分，并非只给一个维数。

## 4. 定义域与原半线性下降的边界

矩阵和所选核列的系数是有理数，只说明在原整基坐标中使用有理数系数。它不说明每个输出微分已是原曲线的 $\mathbb Q$ 定义微分。原 $c_Y$ 并不逐项固定原整基：R853/R860 给
$$
c_Yz=z-2\beta_{72},\qquad c_Yw=w,\qquad c_Y\nu=\nu.
\tag{864.17}
$$
所以真实下降是 $c_Y(f_a)\nu$ 的系数运输问题。本次不展开全部 146 个共轭，也不把 R805 辅助有理正规环的坐标有理性替代 (864.17)。输出清楚标记：完整 $K$ 上正则微分基已经认证，原 $\mathbb Q$ 半线性固定基尚未计算。

这个 127 维核可直接作为 [FM](2026-11-16-original-Y-finite-RR-matrices-and-source-leaves.md) 与原 YP 构造中正则微分部分的输入。它没有完成 YP 的 128 维函数空间、634 维允许极点微分空间、507 条主部约束、所选 $a_j$、第三类微分、Hecke 周期行或原高度。原 $\eta$、$\beta$、theta 二挠及非 $p$ 项全保留。

## 5. 最小真实来源与恢复契约

源码名为 `R864_original_canonical_cusp_kernel.py`，结果名为 `R864-original-canonical-cusp-kernel`。命令行是 `--config <expanded-job.json> --out <directory> --budget-minutes <minutes>`。只有公开 Actions 运行新有理运算。

首个输入闭包共 16 个原件：R820 的原 manifest、三份元数据、成功 certificate、有限代数 interface、两图 Hermite index 和 stage manifest，共 9 件；R805 的原 manifest、三份元数据、成功 certificate、原 pencil 和 graded-free-basis，共 7 件。源身份、完整原 configuration、每件 bytes/SHA、所有实际规范及跨源自由基身份均核验。

原生产包到期不改变数学来源。全新 runner 从真实 R856 成功 artifact 的同一载体取两组原件：先逐原 inventory 核全部 569 成员的 bytes/SHA，再只保上述 16 个原字节文件。运输身份和原 R820/R805 数学身份分别保存。不能把 R856 伪标成 R820，也不能因只选 9 个文件而声称重新审核 R820 的全部数学输出。未来续算载体只需这 16 件。

所有数学阶段为根目录 `R864-*.json.gz`，内容原子提交、带同一个完整数学 tag。消元按实际主元阶段断点；两图全乘回按连续核列小块断点。已成同 tag 阶段只读复用。预算停止保留完整 current 和已成阶段，并输出 `complete=false`；恢复不拿旧 false FINAL 的历史 inventory 约束后续已推进阶段。成功 FINAL 引用实际完整 stage manifest、127 列基及两图全核。

数学 tag 固定新 core、本文、原 R805/R814/R820/R860/FM 证明 SHA、16 个原来源规格及固定矩阵/基次序。预算、下载位置和纯运输路线不改变数学身份。公开 wrapper 只用标准库作来源和输出核验，不重复任何消元或微分运算。
