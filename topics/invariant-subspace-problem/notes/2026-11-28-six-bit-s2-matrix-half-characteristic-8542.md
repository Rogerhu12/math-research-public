# 六位独立正权的原 S2：新完整矩阵 half 特征输入

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**状态：新输入已冻结，尚未执行这一新特征目标。**
它使用此前已实际返回的完整上十五维特征参数构造必要前缀，
随后计算新的五维矩阵预算；不重跑已被反例排除的统一平方迹门。
任意部分特征系数、状态或外层绿色都不证明 S2。

## 1. 实际原来源与新的唯一目标

完全沿用[原 pair companion 输入](2026-11-28-six-bit-birth-two-s2-full-pair-companion-8542.md)：
\[
K_2=\ker d_2,\quad L=\ker d_1,\quad \dim K_2=9,\quad\dim L=5,
\]
\[
G_u=P_{K_2}(d_3d_3^*)^{-1}|_{K_2},\quad C_u=G_u^{-1},\quad
B=d_{b^3}|_{K_2},
\]
\[
L_j=P_LF_{j,1}^{-1}|_L,\quad
A=\frac12(C_uB^*L_2+B^*L_2L_3^{-1}L_2),\quad
\mathsf K=A^*G_uA\succeq0.
\tag{1.1}
\]
所有伴随仍是原物理伴随；全十五维 $F_u=d_3d_3^*$ 的逆先于九维压缩；
完整两来源和两个交叉项全部保留。

新的准确目标是
\[
\boxed{I_L-2\mathsf K>0.}
\tag{1.2}
\]
已刊六位出生一首边 half 在同一 $L$ 上给
$L_1L_2^{-1}L_1<I_L/2$。因此若 (1.2) 全部证明，
则同一原完整 S2
$\mathsf K+L_1L_2^{-1}L_1<I_L$
成立。这仍不支付原六位上出生二 S1，也不单独闭合七位递推或普通 ISP。

[真实一特殊权全谱](../results/R271-appendix-six-site-one-special-weight-full-s2-and-sharp-trace-square-budget.md)
已证明该族 $\mathsf K=0\oplus\kappa I_4$，$\kappa<1/3$，
但 $\operatorname{Tr}(\mathsf K^2)$ 可大于 $1/4$。
因此本次直接检查 (1.2) 的全谱，没有继续追逐那个已假的标量门。

## 2. 已刊十五阶参数的使用范围

原 run **46052984288 / job 140688624777** 已完成完整十五阶
Cayley–Hamilton 和 $F_u$ 逆，真实用时 $24.720906012$ 秒，
其中全逆于 $0.553607569$ 秒返回。
[保留小参数](2026-11-28-six-bit-s2-retained-exact-parameters-8542.json)
含原全部十五个特征系数，blob
$\texttt{2237cf832bbc9d14d73553bd43f657df5f3dc66d}$。

新源嵌入这同一十五项，按
\[
\operatorname{adj}F_u=
F_u^{14}+c_1F_u^{13}+\cdots+c_{14}I,\qquad
\det F_u=-c_{15}
\]
构造必要的原完整逆。这里 $c_j$ 是
$\det(\lambda I-F_u)$ 的原系数。
不重新求这些系数，也不重新设立该已完成逆的通过门。
新的运算目标从 (1.2) 开始。

程序将全正分母的数值 content 与 primitive 因子分开：
\[
\det F_1=4\delta,\quad \det F_2=9\epsilon,\quad
\det F_u=9216\theta,
\]
\[
\begin{aligned}
\delta={}&S^3W-4S^2U+12SV-32X,\\
\epsilon={}&Z^2U^2-4SZUV+12S^2UX+12ZV^2-18ZUX-36SVX+81X^2,\\
\theta={}&S^2WV^2-4SUV^2+12V^3-4S^2ZVX+12S^3X^2.
\end{aligned}
\tag{2.1}
\]
它们都是真实完整正 Gram 的行列式除以正整数，因而在正权域严格为正。
其整数内容均为一，后续连续 Faddeev 因子只能使用这类 primitive 多项式。

## 3. 真空商、物理实谱和严格证书

原低零延拓 $\mathsf K$ 消去常数多项式真空线，
并保持其实际物理正交补 $L$。
设新分母规范给
$\mathsf K=N_{\mathsf K}/D$，$D>0$。
源先验证完整六维 $N_{\mathsf K}$ 的真空列为零，
再形成准确五维商矩阵
\[
J=D I_5-2(N_{\mathsf K})_{\rm quotient}.
\tag{3.1}
\]
这个商与真实 $D(I_L-2\mathsf K)$ 相似，而不是普通转置下的压缩。
所有特征值均为实数。

只将 (3.1) 提出一个明确正标量多项式 $q$，写 $J=qH$，
并计算新的完整
\[
\det(\lambda I_5+H)=
\lambda^5+a_1\lambda^4+a_2\lambda^3+a_3\lambda^2+a_4\lambda+a_5.
\tag{3.2}
\]
若全部 $a_j>0$ 在原正权域得到证明，则 (3.2) 在 $\lambda\ge0$
无根，物理实谱给 $H>0$，从而得到 (1.2)。
任何一个 reduced 参数多项式有负系数，本身都不构成实际负特征值。

companion 求值相似先在互异正 $z_i$ 上使用。
所有实际完整 Gram 逆和 (2.1) 正分母在整个正权域连续，
因此特征系数身份延拓到碰撞权。
若后续全系数正性在碰撞处仍严格，才得到同处严格矩阵正性。
特别，全等权 specialization 的 companion 矩阵本身未必等于标量矩阵，
不能把退化求值基当成可逆相似；程序只对特征系数核全等权值。

## 4. 准确整数递推和原始 checkpoint

连续 Faddeev 矩阵只提出
$S,Z,W,U,V,X,\delta,\epsilon,\theta$
这些 primitive 正因子。若原连续矩阵为 $P\widehat F$，其中 $P$ primitive，
原整数 Faddeev 除法及 Gauss 引理保证
$-\operatorname{Tr}(H\widehat F)/k$ 仍为整数多项式。
因此下一阶没有引入未标记的有理分母。
**连续矩阵绝不提出任意整数 content。**
已完成的单个特征系数和最初整个 $J$ 可以提出正整数 content，
因为那不再改变连续矩阵的除法规范。

新源完整保留：

- (3.1) 的初始正标量 $q$、原 $D$ 因子和准确五维初始矩阵 $H$；
- 每个已形成的原新特征系数，包含所有正因子和完整 reduced 整数系数；
- 当前连续矩阵及其累计 primitive 标量因子；
- 每一份压缩载荷的原始字节数、SHA-256 和编码。

内部载荷使用 lossless 的 JSON、zlib 和 base64。
初始矩阵不会在形成最后标量或最后系数时删除。
它使同一原来源在资源终止后可继续，不需要再求原十五维逆。
输出大小须按首次真实返回记录；目前未声称实际体积。

源固定 **180 秒内层 alarm / 4 GiB RLIMIT_AS**；
不提高此前任何失败门的时限，也不重跑原四阶或平方迹目标。
新源只在全部五阶和新的完整 Cayley–Hamilton 返回后标
EXACT_CHARACTERISTIC_READY（或其 reduced 基本对称系数已直接正时标 CERTIFIED_ELEMENTARY）。
只得到部分 checkpoint 时仍严格标未完成。

## 5. 有限数值选源记录的准确地位

随附[小数值源](2026-11-28-six-bit-s2-shifted-cubic-budget-numeric-screen-8542.mjs)
和[实际记录](2026-11-28-six-bit-s2-shifted-cubic-budget-numeric-screen-8542.json)
只用于本次选择矩阵目标，没有设置额外数值门。
它从完整物理子集矩阵重建同一两来源，
以 seed $28540317$ 检查 $405$ 个点，无 Cholesky 失败，
实际耗时 $1002$ ms。
记录的移位三次量
$\operatorname{Tr}(32\mathsf K(\mathsf K-I/4)^2)$ 最大约 $0.505464$。
这不是一致上界，也不是本次将要求执行的目标；
本次精确源直接处理 (3.2)，不盲目增加迹阶。

运行示例：
\[
\texttt{python <source>.py --output <checkpoint.json> --full-orbits}.
\]
实际路径为
[新完整矩阵 half 源](2026-11-28-six-bit-s2-matrix-half-characteristic-8542.py)。
首次执行后从其真实内层和全部 checkpoint 继续；未执行或部分返回绝不写成一般 S2 已证。
