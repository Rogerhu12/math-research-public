# R271 附录：四异权任意整数池长的低边统一迹界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
状态：完整证明、全权精确整数证书；池固定 primitive 出生二，不声明整个 primitive 空间。

## 1. 新范围及结论

取
$$
D=\sum_{i=1}^4a_iE_i+\sum_{j=5}^{L+4}E_j,\qquad
a_i>0,\quad L\in\mathbb Z,\quad L\ge4.
$$
只取单位池置换群 $S_L$ 的固定部分，primitive 出生为 $s=2$，
六维固定 primitive 块的总串长为 $h=L$。
设 $H_n$ 是同一个源嵌入下先完整取逆、再压 primitive 的真实 Gram。

**定理 1。** 对全部正头权与全部整数 $L\ge4$，
$$
\boxed{\operatorname{tr}(H_0^{-1}H_1H_2^{-1}H_1)<3,}
\qquad
\boxed{H_1H_2^{-1}H_1\prec3H_0.}
\tag{1.1}
$$
同一固定块的高边也满足
$$
\boxed{H_{L-1}H_L^{-1}H_{L-1}\prec3H_{L-2}.}
\tag{1.2}
$$
迹常数 $3$ 在所有池长上的统一意义下不可再减小；这不表示算子序常数
$3$ 最优。

已证 [四池低边稿](R271-appendix-four-exceptional-weights-four-pool-low-edge-exact-trace-bound.md)
在 $L=4$ 给更小的 $5/2$，该范围和常数保留。
R239 的 $L=2$ 全高度二证书及 q−1 出生的所有端点也不重复登记。
本稿的新内容是 $L\ge4$ 上统一的完整低边费用，不再留下一个未付异常源。
整数池长是定理的准确范围；没有由整数证书宣称一切实参数 $L>3$。

## 2. 全部真实最小逆及参数数目

仍记
$$
f_x(X)=\sum_{i<j}x_{ij}X_iX_j,\qquad
z_i=a_i^2,\quad z_R=\prod_{i\in R}z_i,\quad r=|R|.
$$
按 [R239 一参数稿 §10](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)
的真实嵌入 $\mathcal E$，
$$
H_n=\mathcal E^*
\left(\frac{D^n(D^*)^n}{(n!)^2}\Big|_{\mathcal H_2}\right)^{-1}\mathcal E.
$$
该稿的多重仿射完整 Moore--Penrose 公式在这里给
$$
\begin{aligned}
x^*H_0x&=\sum_{r=2}^4\frac{z_R}{\binom L{r-2}}|f_x(R)|^2,\\
x^*H_1x&=\min_{\beta\in\mathbb C^4}
 \sum_{r=1}^4\frac{z_R}{\binom L{r-1}}
 |f_x(R)+b_R^T\beta|^2,\\
x^*H_2x&=\min_{\beta_0\in\mathbb C,\,\beta\in\mathbb C^4}
 \sum_{r=0}^4\frac{z_R}{\binom Lr}
 |f_x(R)+\beta_0+b_R^T\beta|^2.
\end{aligned}
\tag{2.1}
$$
最后一行中 $\beta\in\mathbb C^4$，$\beta_0\in\mathbb C$；
每行均对所标秩的全部子集求和。

这里两次最小化分别具有四个和五个真正自由参数。
池平均保源且不增范数；完整固定解的维数及穷尽性由所引 §10.2
已付。因此 (2.1) 是完整原 Hilbert 最小逆，而不是选一个方便原像。
源基不假定正交，$H_0$ 始终保留。

## 3. 原整数 Gram 和准确迹比

按边序 $12,13,14,23,24,34$，
$$
v_R=(1_{\{i,j\}\subseteq R})_{i<j},\quad
b_R=(1_{\{i\in R\}})_i,\quad t_R=(v_R,1,b_R).
$$
置
$$
d_0=L(L-1),\quad d_1=d_0(L-2),\quad d_2=d_1(L-3).
$$

原始状态权表为：

| Gram | 秩 $0$ | 秩 $1$ | 秩 $2$ | 秩 $3$ | 秩 $4$ |
|---|---:|---:|---:|---:|---:|
| $A=d_0H_0$ 的 $v_R$ 列 | — | — | $d_0$ | $L-1$ | $2$ |
| 中间 $S,M,C$ 的 $(v_R,b_R)$ 列 | — | $d_1$ | $(L-1)(L-2)$ | $2(L-2)$ | $6$ |
| 下一阶完整 $G$ 的 $t_R$ 列 | $d_2$ | $(L-1)(L-2)(L-3)$ | $2(L-2)(L-3)$ | $6(L-3)$ | $24$ |

每项还须乘原 $z_R$；横线表示不出现的状态。
$S,M,C$ 分别是中间完整 Gram 的源块、交叉块和四维低次块。
定义
$$
\Delta=\det C,\qquad
K=\Delta S-M\,\operatorname{adj}(C)M^T,\qquad
J=(\operatorname{adj}G)_{\rm top},
$$
其中 $J$ 保前六个源坐标。完整块逆给
$$
H_1=\frac{K}{d_1\Delta},\qquad
H_2^{-1}=\frac{d_2J}{\det G}.
\tag{3.1}
$$
$A,C,G$ 严格正定：分别用双点状态、单点状态、以及空集/单点/双点
的布尔评价三角阵即可直接核验。

令
$$
\mathscr N=\operatorname{tr}(\operatorname{adj}(A)KJK),\qquad
\mathscr D=\det A\,\Delta^2\det G.
$$
所有矩阵顺序保留，准确有
$$
\boxed{
\operatorname{tr}(H_0^{-1}H_1H_2^{-1}H_1)
=\frac{L-3}{L-2}\frac{\mathscr N}{\mathscr D}.
}
\tag{3.2}
$$

## 4. 抽去的因子逐项可除，次数界独立于计算

以下把 $L$ 当作形式变量，仅用于有限多项式恒等式。
不对非物理池长定义最小逆。

Cauchy--Binet 的每一列组，状态权都是 §3 表中的多项式。
非零项可逐列组抽去下表因子；伴随和 $K$ 是逐矩阵元素的可除性。

| 对象 | 每个非零列组的共同因子 | 商的 $L$ 次数上界 |
|---|---|---:|
| $\det A$ | $L^2(L-1)^5$ | $5$ |
| $\operatorname{adj}A$ | $L(L-1)^4$ | $5$ |
| $\Delta$ | $(L-2)^3$ | $9$ |
| $K$ | $(L-2)^4$ | $10$ |
| $\det G$ | $(L-3)^{10}(L-2)^6$ | $12$ |
| $J$ | $(L-3)^9(L-2)^5$ | $12$ |

逐项理由如下。

$A$ 的四个三点列及全头列张成维数至多四：
全头列恰是四个三点列之和的一半。
所以非零六列行列式至少使用两个双点列；
非零五列伴随项至少使用一个双点列。
除唯一全头状态外，所有 $A$ 列权又都含 $L-1$。
这给前两行的全部因子。
六列和五列的原次数上界分别为 $12,10$；
减去因子次数 $7,5$，两商均至多五次。

$\Delta$ 采用四列，至多一列是全头状态，其余列权均含 $L-2$，
故至少含 $(L-2)^3$；原次数至多十二。
$K$ 可用完整五列 Schur Cauchy--Binet 式：
若 $u$ 是该组 $4\times5$ 线性评价阵的有符号余子式向量，
其贡献为状态权乘积乘
$(\sum_Ru_Rv_R)(\sum_Ru_Rv_R)^T$。
至多一列是全头状态，故每项含 $(L-2)^4$。
单点状态仅有四个，五列的原最大次数至多 $4\cdot3+2=14$，
故商至多十次。这也说明没有在形式域中倒置 $C$ 来取得可除性。

$\det G$ 用十一列，$J$ 的伴随展开用十列。
秩至少三的状态总共只有五个，秩四状态只有一个；
所以分别至少有六/五列含 $L-2$，
至少有十/九列含 $L-3$。
十一列的原最大次数是 $4+4\cdot3+6\cdot2=28$，
十列则是 $4+4\cdot3+5\cdot2=26$。
减去相应因子次数 $16,14$，两商均至多十二次。

于是存在整数多项式 $\mathscr N_{\rm red},\mathscr D_{\rm red}$，准确满足
$$
\begin{aligned}
\mathscr N&=
 L(L-1)^4(L-2)^{13}(L-3)^9\,\mathscr N_{\rm red},\\
\mathscr D&=
 L^2(L-1)^5(L-2)^{12}(L-3)^{10}\,\mathscr D_{\rm red}.
\end{aligned}
\tag{4.1}
$$
这些因子来自逐项乘积，绝非仅由几个数值代入猜测。
由表中次数，
$$
\deg_L\mathscr N_{\rm red}\le5+10+12+10=37,\qquad
\deg_L\mathscr D_{\rm red}\le5+9+9+12=35.
\tag{4.2}
$$
(3.2) 因而准确化为
$$
\boxed{
\operatorname{tr}(H_0^{-1}H_1H_2^{-1}H_1)
=\frac{\mathscr N_{\rm red}}{L(L-1)\mathscr D_{\rm red}}.
}
\tag{4.3}
$$
对物理 $L\ge4$，分母严格为正。

## 5. 有限 Newton 整数证书覆盖所有池长

定义真正的有限多项式
$$
\mathscr P(L,z)
=3L(L-1)\mathscr D_{\rm red}(L,z)-\mathscr N_{\rm red}(L,z).
$$
由 (4.2)，其每个头权单项式的 $L$ 次数至多 $37$。因此准确有有限恒等式
$$
\mathscr P(L,z)
=\sum_\alpha\sum_{k=0}^{37}
 c_{\alpha,k}\binom{L-4}{k}z^\alpha,
$$
$$
c_{\alpha,k}
=\sum_{j=0}^k(-1)^{k-j}\binom kj
 [z^\alpha]\mathscr P(4+j,z).
\tag{5.1}
$$
该恒等式依赖独立证明的次数界，而非把有限测试外推到无限池长。

完整代码：

[四头任意池长低边 Newton 证书](../notes/2026-11-13-four-exceptional-weights-all-pool-low-edge-newton-certificate-1cf.mjs)

完整源 blob：
$$
\texttt{5398d7934aa7a73ed537f53fc4109ddaeae63dab}.
$$

脚本从十六个实际状态重建 $A,C,K,G$，
对每个 $L=4,\ldots,41$ 作完整 Cauchy--Binet 行列式、伴随和
Schur 展开，再精确抽 (4.1) 的因子。所有整数除法都核余数为零。
这是为了取得 (5.1) 的全部系数，不是以某些正权样本代替全权证明。
另算 $L=42$ 的第 38 阶差分为零，只作冗余一致性检查；
它没有替代 §4 的次数论证。

为减少重复计算，迹的 36 个有序边对按 $S_4$ 分成
对角、相交、相离三轨道，大小为 $6,24,6$。
矩阵对头置换协变，所以选每个轨道的一个元素，再对头权变量置换求和，
正好恢复完整迹。脚本在 $L=4$ 还独立与未经轨道归约的完整矩阵乘积逐项相等核对。
这里没有丢掉非交换乘法中的交叉项。

精确输出为：

- 头权单项式支撑有 $21251$ 个。
- 全部 $c_{\alpha,k}\ge0$，其中严格正系数共 $357050$ 个。
- $k=0$ 的 $21251$ 个系数全部严格为正。
- 全部严格正系数中的最小整数为
  $$
  \boxed{36691771392};
  $$
  它例如出现在 $k=2$、头指数 $(21,17,17,16)$。
- 第 37 阶系数全零；冗余第 38 阶也全零。
- 每次多项式乘法前仍核各变量指数和不超过 $25$，实际最大为 $21$；
  base-$32$ 四槽不会进位，全部符号判断均使用 BigInt。

各阶正系数个数由代码固定断言，依次为
$$
\begin{aligned}
&21251,21251,21251,21171,21031,20815,20506,20086,19536,18836,\\
&17965,16961,15841,14625,13336,12000,10646,9306,8015,6811,\\
&5705,4705,3816,3040,2376,1820,1365,1001,715,495,\\
&330,210,126,69,31,5,1,0 .
\end{aligned}
\tag{5.2}
$$

对任意整数 $L\ge4$，所有 $\binom{L-4}{k}$ 非负；
当 $k>L-4$ 时它准确为零。
由严格正的零阶项，
$$
\mathscr P(L,z)>0\qquad(L\in\mathbb Z,\ L\ge4,\ z_i>0).
$$
代回 (4.3)，得到迹严格小于三。
如四池稿一样，将矩阵以 $H_0^{-1/2}$ 同余后成为正矩阵，
其最大特征值不超过迹，所以得到 (1.1) 的完整算子序。
没有把 scalar log-convexity 直接升级为非交换矩阵比较。

## 6. 高边、整固定块及迹常数的准确范围

[R239 倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)
给 $h=L$ 的完整关系
$$
\Gamma_n(a)=Z^{-1}B_s^*\Gamma_{L-n}(a^{-1})B_s.
$$
$B_se_I=a_I^2e_I$、$Z=\prod_{i=1}^4a_i^2$。
单位池在倒数权下不变；$B_s$ 和其逆与池 $S_L$ 平均交换，
故准确双射这里的六维固定 primitive 块。
对倒数权的低边定理先使用严格正矩阵的 Schur 等价反转两个邻居，
再作该同余，就得到 (1.2)。两边的归一化迹也由相似及迹循环性完全相同，
故高边同样有严格迹界三。

对剩余的每个整数阶 $2\le n\le L-2$，
R239 一参数稿 §10.4 已给
$$
H_nH_{n+1}^{-1}H_n
\preceq
\left(1+\frac3{n-1}\right)
\left(1+\frac3{L-n-1}\right)H_{n-1}
\preceq\frac{4L}{L-3}H_{n-1}.
$$
最后一个最大值在中段的两个端点取得。
新低、高两边的常数三小于 $4L/(L-3)$，因此现在可合法合并成
$$
\boxed{
H_nH_{n+1}^{-1}H_n
\preceq\frac{4L}{L-3}H_{n-1}
\preceq16H_{n-1},
\quad 1\le n<L.
}
\tag{6.1}
$$
这是同一相对出生二固定块的全阶粗界；中段引用旧结论，
新费用仅在两端支付。没有补入其它池表示或其它出生层。

最后，取全部 $a_i=1$。等权 Boolean 链在这里的六维 primitive 块上给
$$
\Gamma_1=L^{-1}I,\qquad
\Gamma_2=\frac2{L(L-1)}I.
$$
所以低边的真实迹恰为
$$
6\frac{L-1}{2L}=3-\frac3L\longrightarrow3.
$$
故统一迹上界三不能严格降低。它不推出最优的相邻算子常数也是三。

所有源坐标仍使用真实 Gram $H_0$。
一般有限异权模型、整个 $K_s$、原连续尾的普遍相邻常数，
以及原缺陷 $N=M$ 均没有由本稿免费完成。
