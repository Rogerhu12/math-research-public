# R854 实施补节：几何整化与逐行残差界

日期：2026-11-16。本文细化 [R854 的 41 地方行饱和算法](R854-original-41-cleared-row-saturation-and-four-responses.md) 的初始整化，不改原 $2420$ 未知、原 free $1186$、$2560$ 个 cleared 行、任何 CM 泛函或行饱和算法。尚未运行新的 41 算术；以下 $a,c$ 都必须从实际原 R781 系数算出并保存，不能预填。

## 1. 避免全局整化制造无关零位

R854 (854.5) 的第 $m$ 行块是

$$
246^3K_{m+1}F_{m-1}A+
\sum_{j=0}^{m}R_{m-j}K_jG_jC=0.
\tag{854G.1}
$$

原 R781 已准确给每个 $R_n,K_n$ 的整数 primitive vector 及一次有理尺度，且 $R_0=K_0=1$。从这些真实有理尺度选择一个整数 $a\ge0$，使

$$
41^{an}R_n,\quad 41^{an}K_n\in
\mathbf Z_{41}[B,s,t]/(F_B,s^2+3,g)
\tag{854G.2}
$$

对全部已需 $n$ 成立。具体可取所有非零尺度 $u_n/v_n$ 的
$\max(0,\lceil(v_{41}(v_n)-v_{41}(u_n))/n\rceil)$ 之最大值，$n\ge1$；零向量跳过，$n=0$ 的单位来源另核。整数 primitive vector 不需要再做原域算术。该规则安全，但不声称得到元素实际赋值最优的 $a$。

置

$$
c=\max(0,a-3),\qquad
\widetilde R_n=41^{an+c}R_n,\qquad
\widetilde K_n=41^{an}K_n.
\tag{854G.3}
$$

因为 $246=6\cdot41$，

$$
\mu=246^3\,41^{c-a}=6^3\,41^{c+3-a}\in\mathbf Z_{41}.
\tag{854G.4}
$$

用已整化的两条序列做同一次原卷积，则第 $m$ 块恰为

$$
\mu\widetilde K_{m+1}F_{m-1}A+
\sum_{j=0}^{m}\widetilde R_{m-j}\widetilde K_jG_jC
=41^{am+c}\left(
246^3K_{m+1}F_{m-1}A+\sum_jR_{m-j}K_jG_jC\right).
\tag{854G.5}
$$

所以它严格等于把原块左乘明确非零标量
$S_m=41^{am+c}$，而非改变原 $Y$、$B$ 或 Laurent 相位。两块和 free-column 右端用同一尺度。实际代码只生成整向量及整数 $\mu$，不用先形成有 $41$ 分母的矩阵，也不用把所有块乘同一个可能很大的公共尺度后再剥离。

## 2. 明确针对哪一个矩阵给逆范数界

令 $S$ 是按原 $m=1,\ldots,128$、每块二十行重复 $S_m$ 的对角矩阵，

$$
M_0=S\mathcal M,\qquad b_0=Sr.
\tag{854G.6}
$$

R854 的行饱和直接作用于这个整矩阵 $M_0$。账本初值为 $T_0=I$、全部 $w_i=0$，始终有 $M_h=T_hM_0$。它并没有声称 $T_h\mathcal M=M_h$。实际 $2420$ 个单位行 $I_*$ 给

$$
L_0=U^{-1}(T_h)_{I_*},\quad L_0M_0=I,\quad
v_L((L_0)_{ij})\ge w_*.
\tag{854G.7}
$$

对原规范候选 $\widetilde u$，记全部原 cleared 残差为
$e_j=(\mathcal M\widetilde u-r)_j$。按实际原行号所属块 $m(j)$，完整逐行检查给

$$
u-\widetilde u\in B^{R_*+w_*}\mathcal O_L^{2420},
\quad
R_*\le\min_j\{v_L(e_j)+7(am(j)+c)\}.
\tag{854G.8}
$$

这是对明确整化系统的真实残差界，不是把整化增益冒称原残差精度。输出同时记录每个块的 $7(am+c)$、整化残差各行下界、扣回后的原残差各行下界以及 (854G.8) 所用的加权最小值。若只想报告原统一残差下界，可另取扣回后全部行的最小值，但不必用这个较弱数字丢失已经证明的逐行信息。

若候选以 $B^{-\delta}u_{\rm num}$ 表示，核验整数分子

$$
M_0u_{\rm num}-B^\delta b_0.
\tag{854G.9}
$$

每行先减 $\delta$ 得整化残差下界，再减 $7(am+c)$ 得原残差下界。(854G.8) 中原尺度随后准确加回，最终恰是分子下界的最小值减 $\delta$ 再加 $w_*$。不能省略这个解释而直接把分子精度标为原坐标精度。

## 3. 不变的成功出口和来源边界

全部原行仍检查，$m=0$ 仍由原准确 $G_0=0$ 和当前求值共同核为零。行饱和的剩余域、实际 unit minor、停止性证明、只续下一 Dixon 位、原四泛函和 free-column 常数全部不变。新的 source tag 显式写 `geometric-original-row-scaling`、实际规则以及 `inverse_bound_applies_to=geometrically_scaled_original_tall_matrix`；实际 $a,c$ 是已算阶段字段，不是请求猜值。

此补节只减少人工精度负担，不预报原矩阵在 $41$ 处的真实退化程度。若实际剩余元仍为零或单位图尚未出现，须保断点增加真实精度。辅助 $\ell$ 逆、旧 $518$ 球与未获 A.1 的短坐标均不进入此过程；准确有理坐标、$Z$、原高度仍不因本补节而已计算。
