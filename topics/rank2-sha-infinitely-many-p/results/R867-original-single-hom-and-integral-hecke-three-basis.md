# R867 — 单条原 Hom 重建、整 Hecke 三基与固定 57 清分母

日期：2026-11-16。

**状态：下述整 Hecke 三基、同原 b-基的精确矩阵、固定57清分母、
完整8/64邻点迹以及实际映射次数上界已证明。
仍须重建并认证一条原 $\Xi_0$；尚未证明它已为整数同态，
也未计算一个非零原 shadow。**

本篇不把某个仅在 $\operatorname{End}^0_K(A)$ 中的 CM 元
自动认成原整 Hecke quotient 上的整数 endomorphism。
全部整操作直接在原 Jacobian 与明确的目标椭圆曲线上定义。

## 1. 原源、目标与整算子

固定
$$
C=X_0(2601),\qquad J=J_0(2601),\qquad
K=\mathbf Q(\omega),\quad\delta=1+2\omega,
$$
以及 R862/R864/R866 的
$$
C_v:Y^2+vY=X^3,\qquad \omega_v=\frac{dX}{2Y+v}.
$$
R866 中的三个规范准同态均视作原 $J$ 上的准同态：
$$
\Xi_i\in\operatorname{Hom}_L^0(J,C_v),\qquad
\Xi_i=\Xi_0\circ\iota(b)^i,\qquad
\Xi_i^*\omega_v=H_i(q)\frac{dq}{q}.
\tag{1}
$$
右边的 $\iota(b)$ 只在原三维新 Hecke 因子的 isogeny 范畴中使用。
左边则保留实际 $J\to A$ 的原投影；其它 Hecke 因子被 $\Xi_0$ 杀掉。

$T_7\in\operatorname{End}(J)$ 是真正的整 Hecke correspondence。
目标上有实际整 CM endomorphism
$$
[\omega](X,Y)=(\omega X,Y),\qquad [\omega]^*\omega_v=\omega\omega_v.
\tag{2}
$$
因而每个 $\mathcal O_K$ 系数都可由目标上的加法与 (2) 实现。
本篇的整性只使用这两种操作。

也可在源上核同一个 $\omega$：
$R:z\mapsto z+1/3$ 是原 level2601 的三阶 normalizer，
原 $H_i$ 的全部非零指数均为 $1\bmod3$，故
$$
\Xi_i\circ R_*=[\omega]\Xi_i.
\tag{3}
$$
这是原 $J$ 上准同态的等式，由完整微分和基点得到。
(3) 不要求先选择一个令 $\iota(\mathcal O_K)$ 整的 isogenous 因子。

## 2. 原7系数与两个准确分母公式

R862 固定
$$
\alpha=-1+2\omega,\qquad
b=\beta_{10}((\alpha)),\qquad
b^3=c=-1-19\omega .
\tag{4}
$$
原三个新形式的 nebentypus 为1，所以其7系数为
$$
t=b+\frac7b,\qquad
\bar c=-1-19\omega^2,\qquad
c+\bar c=17,\quad c\bar c=343,\quad
\bar c-c=19\delta.
\tag{5}
$$
此处的横线固定为原复共轭；$7/b$ 是同一个原形式的另一7理想值。
由 (5)，
$$
\boxed{t^3-21t-17=0.}
\tag{6}
$$
它是原实三次 Hecke 系数域的最小多项式；
$t$ 的三份共轭对应原三个 $g_j$。
因此 $\iota(t)$ 在原 packet 上恰为 $T_7$。

从
$$
t=b+(7/c)b^2,\qquad t^2-14=(49/c)b+b^2
$$
直接消元，得到
$$
\boxed{
b=\frac{7t^2-ct-98}{19\delta},\qquad
b^2=\frac{-ct^2+49t+14c}{19\delta}.
}
\tag{7}
$$
第二式不是简单平方后再付一个分母：
利用 $t^3=21t+17$ 后，两式的共同分母都只有 $19\delta$。

定义原三条 Hecke 准同态
$$
Q_0=\Xi_0,\qquad Q_1=\Xi_0\circ T_7,\qquad
Q_2=\Xi_0\circ T_7^2.
\tag{8}
$$
由 (7)，完整换基为
$$
\boxed{
\begin{pmatrix}\Xi_0\\ \Xi_1\\ \Xi_2\end{pmatrix}
=
\begin{pmatrix}
1&0&0\\
-98/(19\delta)&-c/(19\delta)&7/(19\delta)\\
14c/(19\delta)&49/(19\delta)&-c/(19\delta)
\end{pmatrix}
\begin{pmatrix}Q_0\\ Q_1\\ Q_2\end{pmatrix}.
}
\tag{9}
$$
其逆准确为
$$
\boxed{
\begin{pmatrix}Q_0\\ Q_1\\ Q_2\end{pmatrix}
=
\begin{pmatrix}
1&0&0\\
0&1&7/c\\
14&49/c&1
\end{pmatrix}
\begin{pmatrix}\Xi_0\\ \Xi_1\\ \Xi_2\end{pmatrix}.
}
\tag{10}
$$
两个行列式分别为 $-c/(19\delta)$ 和 $-19\delta/c$，互为倒数。
因此 (8) 是完整原 $K$-Hom 空间的三基，而不只张成其一个边际。

证明也可直接从 $1,t,t^2$ 为三次域基看出：
若一个 $K$-线性组合在复合 $\Xi_0$ 后为0，
对应非零域元在原因子上可逆，与 $\Xi_0\ne0$ 矛盾。
没有把三条独立微分误作新的算术中央零。

## 3. 一条实际映射足以恢复全部原 Hom

设 $n>0$ 已经通过 R866 的证书认证，使
$$
P_0=n\Xi_0:J_L\longrightarrow C_v
$$
是实际整数同态。定义
$$
P_1=P_0\circ T_7,\qquad
P_2=P_0\circ T_7^2 .
\tag{11}
$$
它们自动为同一个原 Jacobian 上的整数同态。
由 (2)、(9)，
$$
[19\delta]\,(n\Xi_1)=[7]P_2-[c]P_1-[98]P_0,
$$
$$
[19\delta]\,(n\Xi_2)=-[c]P_2+[49]P_1+[14c]P_0.
\tag{12}
$$
右侧全是整数同态。
因为 $(-\delta)(19\delta)=57$，再在目标后复合 $[-\delta]$，得到
$$
\boxed{57n\Xi_i\in\operatorname{Hom}_L(J,C_v)
       \qquad(i=0,1,2).}
\tag{13}
$$
这里57清的是显示的换基成本；未知的最小清分母仍只留在
**一条** $\Xi_0$ 中。不需对 $\Xi_1,\Xi_2$ 分别作无界重建。

回到原 $E_0$，R866 的
$$
\kappa:C_v\to E_0,\qquad
\kappa^*\omega_0=(h/2^{11})\omega_v
$$
给原 R862 基
$$
\mathcal A_i=2^{11}\kappa\Xi_i.
\tag{14}
$$
因此 $57n\mathcal A_i$ 也都是 $H_9$ 上的真实同态。
原 $\Gamma_j$ 的 Artin/Hecke 系数仍按 R862(39) 线性展开，
不会因 (14) 重新归一原循环。

额外的57只涉及3和19。
对任意原良好惰性有理素数 $r>3$，$r\ne19$ 自动成立，
因为 $19\equiv1\bmod3$；所以这一步没有新增惰性坏素数。
原 $n$、其它 $D$ 因子及 $\ell$-adic 检测处的换格仍完整保留。

## 4. 真正的8项和64项模曲线迹

将 (11) 与基点 $\infty$ 的 Abel 映射复合，仍记为
$P_i:C_L\to C_v$。
对一般点 $x$，令 $\mathcal N_7(x)$ 为带同一原 cyclic2601结构的
8个7-isogenous 邻点，按整个 Hecke correspondence 计。
由于 $T_7(\infty)=8\infty$ 且 $P_0(\infty)=O$，
$$
\boxed{
P_1(x)=\sum_{y\in\mathcal N_7(x)}P_0(y),\qquad
P_2(x)=\sum_{y\in\mathcal N_7(x)}
          \sum_{z\in\mathcal N_7(y)}P_0(z).
}
\tag{15}
$$
这分别是完整8项和64项椭圆群加法，不是逐 q 系数替换。

第二个式子的8条回溯路径准确返回 $x$；
其余56条给 cyclic49 isogenies。
所以也可写成
$$
P_2(x)=[8]P_0(x)
 +\sum_{\substack{x\to z\\\text{cyclic49}}}P_0(z).
\tag{16}
$$
(16) 不把经典 $T_{49}$ 与56条纯 cyclic49 路径混同；
经典关系是 $T_7^2=T_{49}+[7]$，其中 $T_{49}$ 本身还含一次
$[7]$-核对应的对角分支。

在非一般点、有限域以及所有原 cusp 上，(15) 的定义是
正规化 Hecke correspondence 的拉回、推前和闭点迹。
需要保留局部重数。有限域中无需选择8个点都为有理；
其 Galois 轨道的椭圆点和正是同一映射的值。
这为认证一个 $P_0$ 之后的实际 shadow 计算给出完整 finite source。

原 $q_0/q_2$ 仍为 R831 的不同退化映射。
将 (15) 用于 $a\circ q_0$ 或 $b\circ q_2$ 时，先在其各自的原
level2601点上取这份完整迹；不把两端退化图或其权重交换。

## 5. 541项输入无需扩大到 49×541

R866 已给全部 $H_0,H_1,H_2$。
由 (10)，(8) 的完整微分是
$$
\boxed{
\begin{aligned}
Q_0^*\omega_v&=H_0\,dq/q,\\
Q_1^*\omega_v&=(H_1+(7/c)H_2)\,dq/q,\\
Q_2^*\omega_v&=(14H_0+(49/c)H_1+H_2)\,dq/q.
\end{aligned}}
\tag{17}
$$
因此已有三个 $H_i$ 的541项就给 (17) 的全部认证输入。
无需为计算 $T_7^2 H_0$ 先额外生成 $49\cdot541$ 项。

(17) 中的 $7/c$ 或 $49/c$ 是特征零换基；
三条 $nQ_i$ 的整性来自 (11) 的实际 Hecke 操作，
而不是声称此矩阵在每个素数的任意系数格上为整矩阵。

## 6. 认证后两条派生映射的实际次数界

设 $d_0=\deg(P_0:C\to C_v)$。
固定任意复嵌入，用同一个目标微分 $\omega_v$。
对非恒态射 $f:C\to C_v$，有
$$
\int_C i f^*\omega_v\wedge\overline{f^*\omega_v}
=\deg(f)\int_{C_v}i\omega_v\wedge\overline{\omega_v}.
\tag{18}
$$
原三个 CM 新形式在 $T_7$ 下的特征值为
$t_j=b_j+7/b_j$，各 $|b_j|=\sqrt7$，故
$|t_j|\le2\sqrt7$。
Hecke 在原新空间的 Petersson 内积下自伴；
不同原特征线正交。
所以 (18) 给
$$
\boxed{\deg P_1\le28d_0,\qquad \deg P_2\le784d_0.}
\tag{19}
$$
两条映射都非恒，因为 (6) 的常数项非零，$t$ 在系数域可逆。
若 R866 的成功坐标 total-degree 证书为 $d$，
该篇 $d_0\le408d$ 可直接代入 (19)。

这是同一实际映射的 degree 上界；
它不从一个未经认证的形式 germ 推断映射存在，
也不预报最小 $d_0$ 或最小 $n$。

## 7. 对原 shadow 的用途与尚未完成的步骤

R859 的原读数保持
$$
\operatorname{Alb}(b\circ q_2)_*
       (a\circ q_0-\varphi_r\circ F)^*[O].
\tag{20}
$$
本篇允许先认证一条 $P_0$，再用 (12)、(15) 和原全部外部系数
构造 (20) 中所有第三因子 packet 的映射。
原第一 $F$、原 $q/q^4$、Artin 投影、整数 $D$ 与全交点迹仍须保留。

目前尚未找到这个 $P_0$ 的成功有理坐标；
并无一个原非零 shadow 已由本篇算出。
(9)–(13) 的新作用是把原三条 Hom 的实际重建缩为一条，
以完全显示的57承担换基成本，而非重新命名三个未知映射。

## 8. 原来源与所用标准恒等

- [R862](R862-original-seventeen-torsion-product-and-complete-cubic-hom-matrix.md)：
  固定 $b,c$、原 packet、全部 Hom 和 CM 微分。
- [R864](R864-original-seventeen-torsion-exact-field-and-cocycle.md)、
  [R866](R866-original-modular-function-certificate-and-level-nine-model.md)：
  小三次域、$C_v$、$\Xi_i$、认证界和原完整系数。
- [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)：
  原三阶 normalizer 的实际定义域及完整源作用。
- G. Ligozat, *Courbes modulaires de genre 1*, §2.1，
  Hecke 对应、内积和 Euler 关系；上文 (15)–(16) 另按实际
  cyclic 子群逐项计数。
  <https://www.numdam.org/article/MSMF_1975__43__5_0.pdf>。
- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)、
  [R859](R859-original-supersingular-shadow-and-integral-aj-detection.md)：
  不同原端点和完整整 shadow 规范。

本篇没有新增数值计算或扫描。所有等式由固定原角色、真实 Hecke
correspondence、完整微分和显示的有限代数消元得到。
