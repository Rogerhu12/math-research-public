# R867 — 单条原 Hom 重建、整 Hecke 三基与固定清分母

日期：2026-11-16。

**状态：下述整 Hecke 三基、同原 b-基的精确矩阵、固定57清分母、
完整8/64邻点迹以及实际映射次数上界已证明。附录 A 加入原 $T_{13}$ 后，
把共同清分母严格改进为 $3n$，并给同原 Hom 格上的整单位及其逆。
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


## 附录 A：加入原 $T_{13}$ 后的整单位与共同 $3$ 清分母

本附录不改前面仅用 $T_7$ 的57证书。它给出更强的实际整返回：一旦同一个 $P_0=n\Xi_0$ 已认证，所有 $3n\Xi_i$ 已为真整同态。所有新增操作仍在原 $J_0(2601)$ 与 $C_v$ 上定义。

### A.1 原13系数的完整相位

令
$$
\zeta=b/\alpha,\qquad \zeta^3=\omega^2,\qquad
\vartheta=\zeta+\zeta^{-1}.
\tag{A1}
$$

于是
$$
\vartheta^3-3\vartheta+1=0.
\tag{A2}
$$

这里 $\zeta$ 是 R862 的同一个九次单位根，并未按复近似重新选根。

为核13处相位，取 $\gamma=4+\omega$、$\mathrm N\gamma=13$。
原 $\beta_{10}$ 在素于 $17\delta$ 的主理想上为
$$
\beta_{10}((a))
=\epsilon_\delta(a)\,a\,
 \operatorname{Teich}(a\bmod17)^{32}.
\tag{A3}
$$

这是 R862 中二处 cubic 因子已经准确抵消后的完整公式；它在
$(2)$ 上仍给 $-2$。以 $\alpha$ 为 $\mathbf F_{289}^{\times}$ 生成元，
$\operatorname{Teich}(\alpha)^{32}=\zeta$。

在 $\mathbf F_{289}$ 中置 $g_0=2+4\delta=6+8\omega$。
逐次平方给
$$
\alpha^{16}=8+6\omega=g_0^5,\qquad
\gamma^4=6+8\omega=g_0,\qquad g_0^{18}=1.
\tag{A4}
$$

因此
$$
\gamma^{32}=g_0^8=(\alpha^{32})^8.
$$

又 $\epsilon_\delta(\gamma)=-1$，故(A3)的真实13值是
$$
\boxed{
\beta_{10}((\gamma))=-\gamma\zeta^8=-\gamma\zeta^{-1}.
}
\tag{A5}
$$

其共轭理想值是 $-\bar\gamma\zeta$，没有省略首负号。

令 $t=a_7$、$s=a_{13}$，则
$$
\boxed{
t=2\vartheta^2-\vartheta-4,\qquad
s=\vartheta^2-3\vartheta-2.
}
\tag{A6}
$$

证明直接代入
$t=\alpha\zeta+\bar\alpha\zeta^{-1}$、
$s=-\gamma\zeta^{-1}-\bar\gamma\zeta$，
并使用 $\omega=\zeta^6$、(A2)。
因此
$$
5\vartheta=t-2s,\qquad
19\vartheta=28-3t-2t^2.
$$

两式用 $4\cdot5-19=1$ 合成
$$
\boxed{\vartheta=2t^2+7t-8s-28.}
\tag{A7}
$$

(A5)–(A7)在原三个共轭新形式上同时成立，保持其原 Hecke/Artin 标号。

### A.2 原 Jacobian 上的整数算子和真逆

定义
$$
\boxed{
\mathscr R=2T_7^2+7T_7-8T_{13}-[28]
\in\operatorname{End}(J).
}
\tag{A8}
$$

它在原 packet 上恰为 $\iota(\vartheta)$。从(A2)有
$$
\vartheta^{-1}=3-\vartheta^2.
\tag{A9}
$$

所以 $\mathscr R$ 与 $3-\mathscr R^2$ 都是原 $J$ 的整数 endomorphism，
并在这个 packet 的实际 Hom 格上互逆。准确的意思是：对任意杀掉其它
Hecke 因子的原整数同态 $P:J_L\to C_v$，
$$
P\circ\mathscr R\circ(3-\mathscr R^2)=P.
\tag{A10}
$$

这由(A2)在 packet 上为零及 Hom 微分注入得到。没有宣称
$\mathscr R$ 是整个 $J$ 的全局 automorphism，也没有把
$\operatorname{End}^0(A)$ 的任意整数代数元自动放入原整数 endomorphism ring。

因此，完整的正负整数幂都保持同一个原 Hom 格。该单位操作可用来选择
同格中的实际映射；它本身不保证某一个选择有最小次数。

### A.3 三条原基的共同分母只需3

由 $\zeta^2-\vartheta\zeta+1=0$ 和 $\zeta^3=\omega^2$，
准确得到
$$
\boxed{
\delta\zeta=\vartheta^2-\omega^2\vartheta-2,\qquad
\delta\zeta^2=-\omega^2\vartheta^2+\vartheta+2\omega^2.
}
\tag{A11}
$$

例如第一式也可直接写成
$(\zeta+\zeta^{-1})^2-\omega^2(\zeta+\zeta^{-1})-2
=\zeta^7-\zeta^4=(\omega-\omega^2)\zeta$。
第二式由第一式乘 $\vartheta$、再减 $\delta$ 得到；故两个号均固定。

现设原 $P_0=n\Xi_0$ 已经认证，记
$$
P_{\mathscr R}=P_0\circ\mathscr R,\qquad
P_{\mathscr R^2}=P_0\circ\mathscr R^2.
$$

这些都是真整同态。因为 $b=\alpha\zeta$，(A11)给
$$
\boxed{
[\delta](n\Xi_1)
=[\alpha]\bigl(
 P_{\mathscr R^2}-[\omega^2]P_{\mathscr R}-[2]P_0
\bigr),
}
\tag{A12}
$$
$$
\boxed{
[\delta](n\Xi_2)
=[\alpha^2]\bigl(
 -[\omega^2]P_{\mathscr R^2}
 +P_{\mathscr R}+[2\omega^2]P_0
\bigr).
}
\tag{A13}
$$

右边只用原整数 Hecke 操作、目标的整 $\mathcal O_K$ 作用和群加法。
再后复合 $[-\delta]$，利用 $-\delta^2=3$，得到
$$
\boxed{
3n\Xi_i\in\operatorname{Hom}_L(J,C_v)
\qquad(i=0,1,2).
}
\tag{A14}
$$

原 R862 基 $\mathcal A_i=2^{11}\kappa\Xi_i$ 同样满足
$3n\mathcal A_i$ 为 $H_9$ 上真整同态。因而正文的57可在这些完整
$T_7/T_{13}$ 操作下统一改进为3；未知的原 $n$ 仍保持，不声称该3为最优。

### A.4 原有限来源和计算范围

$T_{13}$ 是同 level2601 上完整14个13邻点的对应；所有复合按正规化、
闭点迹和交重实现。没有把它换成选择一个13邻点，更没有将原
$q_0,q_2$ 两端相认。(A8)若直接用于点值，其两次7步、一次7步、
一次13步和恒等项都以显示整数系数保留。

本附录不需要扩大已有三个 $H_i$ 的输入：在原三维 packet 中，
(A6)–(A7)和正文(9)–(10)准确给各新算子的全部微分。
它也不认一个形式 germ 为全球映射；(A12)–(A14)的前提仍是
同一个 $n\Xi_0$ 已经获得完整坐标证书。

本附录没有执行新的有限域扫描或计算。所用有限域等式(A4)是显示的
固定原角色的逐次代数运算；全部结论由它、原13主理想公式和整 Hecke
correspondence 自含推出。


## 附录 B：两条整单位、三维乘法表与原低权重建的真实运输

本附录给可直接复用的同格坐标。它不改变未知整数 $n$：单位操作只改变
同一原 Hom 的表达与次数，不能把一个本来非整的 $n\Xi_0$ 变成整映射。

### B.1 两个单位及全部逆

沿附录 A，置
$$
\varepsilon_1=\vartheta,\qquad
\varepsilon_2=\vartheta^2-2.
\tag{B1}
$$

其三个实共轭分别为
$\vartheta,\vartheta^2-2,2-\vartheta-\vartheta^2$，均满足(A2)，
且
$$
\boxed{
\varepsilon_1^{-1}=1-\varepsilon_2,\qquad
\varepsilon_2^{-1}=1+\varepsilon_1+\varepsilon_2.
}
\tag{B2}
$$

定义原整数算子
$$
U_1=\mathscr R,\qquad U_2=\mathscr R^2-[2].
\tag{B3}
$$

在原 packet 的 Hom 格上，其逆由原整数算子
$1-U_2$、$1+U_1+U_2$ 实现。下面的任意负幂都指这些明确的整数多项式，
不指在整个 $J$ 上反演一个未证可逆的 endomorphism。

基 $(1,\varepsilon_1,\varepsilon_2)$ 中完整乘法为
$$
\varepsilon_1^2=2+\varepsilon_2,\quad
\varepsilon_1\varepsilon_2=-1+\varepsilon_1,\quad
\varepsilon_2^2=2-\varepsilon_1-\varepsilon_2.
\tag{B4}
$$

采用“输入坐标列向量”的约定，乘法矩阵准确为
$$
\boxed{
M_1=
\begin{pmatrix}
0&2&-1\\
1&0&1\\
0&1&0
\end{pmatrix},\qquad
M_2=
\begin{pmatrix}
0&-1&2\\
0&1&-1\\
1&0&-1
\end{pmatrix}.
}
\tag{B5}
$$

它们交换，行列式均为 $-1$，并有
$$
M_1^{-1}=I-M_2,\qquad M_2^{-1}=I+M_1+M_2.
\tag{B6}
$$

所以对所有 $a,b\in\mathbf Z$，
$$
\begin{pmatrix}e_0\\e_1\\e_2\end{pmatrix}
=M_1^aM_2^b\begin{pmatrix}1\\0\\0\end{pmatrix}
\in\mathbf Z^3
\tag{B7}
$$
精确表示 $\varepsilon_1^a\varepsilon_2^b$。

### B.2 同一个 $K[b]/(b^3-c)$ 中的明确小式

为和原理想 producer 直接对接，另写
$$
\boxed{
\varepsilon_1=\frac b\alpha+\frac{\alpha}{c}b^2,\qquad
\varepsilon_2=\frac{\alpha^2}{c}b+\frac1{\alpha^2}b^2.
}
\tag{B8}
$$

这分别是 $\zeta+\zeta^{-1}$ 和 $\zeta^2+\zeta^{-2}$。
原 $b$ 基中，乘以 $u=A+Bb+Cb^2$ 的矩阵为
$$
\boxed{
M_b(u)=
\begin{pmatrix}
A&cC&cB\\
B&A&cC\\
C&B&A
\end{pmatrix}.
}
\tag{B9}
$$

尤其
$$
M_b(\varepsilon_1)=
\begin{pmatrix}
0&\alpha&c/\alpha\\
1/\alpha&0&\alpha\\
\alpha/c&1/\alpha&0
\end{pmatrix},
\quad
M_b(\varepsilon_2)=
\begin{pmatrix}
0&c/\alpha^2&\alpha^2\\
\alpha^2/c&0&c/\alpha^2\\
1/\alpha^2&\alpha^2/c&0
\end{pmatrix}.
\tag{B10}
$$

令 $\lambda_1=\tau^2\ell$、$\lambda_2=c/\ell$；
这两个记号只是本附录对 R862 原 $u_1,u_2$ 的改名，避免和单位混淆。
若原新形式某个系数为 $f_0+f_1b+f_2b^2$，
相应单位来源的系数准确为
$$
\boxed{
(1,\lambda_1,\lambda_2)\,
M_b(\varepsilon_1)^a M_b(\varepsilon_2)^b
\begin{pmatrix}f_0\\f_1\\f_2\end{pmatrix}.
}
\tag{B11}
$$

此处指数 $b$ 与基元 $b$ 只在(B11)共用字母；实施时可将整数指数另命名。
负幂用(B2)求值。无需为 $T_{13}$ 再生成13倍长度的 Fourier 前缀。

等价地，先固定三条全来源
$$
\boxed{
\mathcal H_0=H_0,\qquad
\mathcal H_1=\alpha^{-1}H_1+(\alpha/c)H_2,\qquad
\mathcal H_2=(\alpha^2/c)H_1+\alpha^{-2}H_2.
}
\tag{B12}
$$

则原单位来源仅为
$$
H_{a,b}=e_0\mathcal H_0+e_1\mathcal H_1+e_2\mathcal H_2.
\tag{B13}
$$

虽然(B8)–(B12)在 $K$ 基中显示分母，其实际整性来自(A8)、(B3)；
不从这些换基矩阵单独宣称局部整格性质。

### B.3 真实下降和首系数

原 R869 使 $\Xi_0$ 与 $H_0$ 下降到 $F=\mathbf Q(v)$。
$T_7,T_{13}$ 以及(B3)的整数多项式均在 $\mathbf Q$ 上，
因此 $\Xi_0U_1^aU_2^b$ 和 $H_{a,b}$ 也全部下降到同一个 $F$。

这是所有系数的全局下降，不是只核有限前缀为实。
实施时可用(B11)在 $K(v)$ 中计算，再准确核其 $\omega$ 坐标消失，
以此确认使用了原同一嵌入。

三条(B12)的首系数为
$$
c_0=1,\qquad
c_1=\lambda_1/\alpha+\alpha\lambda_2/c,\qquad
c_2=\alpha^2\lambda_1/c+\lambda_2/\alpha^2.
\tag{B14}
$$

故
$$
c_{a,b}=e_0+e_1c_1+e_2c_2\in F^\times.
\tag{B15}
$$

非零由 R862 的实际首系数注入得到：
$\varepsilon_1^a\varepsilon_2^b$ 为单位，所以这个 Hom 非零；
其首系数不可能为零。

原每条 CM 新形式的 $q^4$ 系数均为 $-2$ 倍首系数，
因此
$$
H_{a,b}(q)=c_{a,b}q\,f_{a,b}(Q),\qquad
f_{a,b}(0)=1,\quad[Q]f_{a,b}=-2.
\tag{B16}
$$

这里除以 $c_{a,b}$ 只用于把形式递推的 $f_{a,b}$ 写成常数项1。
**实际微分仍为 $nH_{a,b}\,dq/q$，不能把它改成 $nH_{a,b}/c_{a,b}$。**

### B.4 原低权证书的完整运输与倒回

对一个待测正整数 $n$，在 R870 的递推中令
$$
d_{a,b}=n c_{a,b},\qquad t_{a,b}=d_{a,b}^3v.
$$

准确 germ 为
$$
E+3QE'=f_{a,b}(Q)\sqrt{1-4t_{a,b}QE^3},
$$
$$
Y_{\rm form}
=-\frac{1+\sqrt{1-4t_{a,b}QE^3}}{2d_{a,b}^3QE^3}
=-d_{a,b}^{-3}Q^{-1}
-\frac{v+3d_{a,b}^{-3}}2+O(Q).
\tag{B17}
$$

同一个 $M_k(867)$ 基完全可以复用。令候选 $Y=A/B$，
$C_{A,B}=(D_QA)B-A(D_QB)$。必须核的完整式是
$$
\boxed{
C_{A,B}^3
=n^3 H_{a,b}(q)^3 A^2(A+vB)^2B^2.
}
\tag{B18}
$$

右边没有把 $H_{a,b}$ 归一为首系数1。
严格权和末端仍为 $6k+6$、$612(k+1)$，恢复式仍准确是
$$
X=nH_{a,b}(q)\frac{Y(Y+v)}{D_QY}.
\tag{B19}
$$

若该证书成功，它认证的实际映射是
$$
P_{a,b}=n\Xi_0U_1^aU_2^b.
$$

用(B2)指定的整数算子 $U_1^{-a}U_2^{-b}$ 复合，得到
$$
\boxed{
P_{a,b}U_1^{-a}U_2^{-b}=n\Xi_0.
}
\tag{B20}
$$

因此
$$
n\Xi_0U_1^aU_2^b\text{ 整}
\quad\Longleftrightarrow\quad
n\Xi_0\text{ 整}.
\tag{B21}
$$

整数 $n$ 的可积性集合完全不变；单位搜索可以降低函数表示或映射次数，
但不能挽救一个错误的整数倍。成功后仍用附录 A 的共同 $3n$、
原 $\kappa$、$2^{11}$ 和完整 Artin 组合返回原三基。

### B.5 为什么两单位确能平衡三个原分量

这一段只说明实际选择空间，不预报当前一个低权候选成功。
在固定复嵌入下，原三个 Hecke 特征分量的正范数权记为 $a_j>0$，
包括 $H_0$ 的完整 $G_j/3$ 系数及同一个目标 $\omega_v$ 面积。
则对于已整的 $n\Xi_0U_1^aU_2^b$，
$$
\deg(n\Xi_0U_1^aU_2^b)
=n^2\sum_{j=0}^2 a_j
|\varepsilon_{1,j}|^{2a}|\varepsilon_{2,j}|^{2b}.
\tag{B22}
$$

$G_j\ne0$ 由 R862 已付，因此三个权都严格正。
这只是正文(18)与不同 Hecke 线正交的完整应用。

两个向量
$$
v_j=\log|\varepsilon_{1,j}|,\qquad
w_j=\log|\varepsilon_{2,j}|
$$
均在实平面 $\sum x_j=0$，且 $w$ 是 $v$ 的一个三循环。
$v\ne0$；三循环在这个实二维平面没有实特征直线，故 $v,w$ 独立。
这也证明两单位乘法独立。

令 $g=(a_0a_1a_2)^{1/3}$。
先在实数中解
$2a_*v+2b_*w=-(\log(a_j/g))_j$，再分别取最近整数 $a,b$。
得到
$$
g/M_j\le
a_j|\varepsilon_{1,j}|^{2a}|\varepsilon_{2,j}|^{2b}
\le gM_j,
$$
$$
M_j=
\max(|\varepsilon_{1,j}|,|\varepsilon_{1,j}|^{-1})
\max(|\varepsilon_{2,j}|,|\varepsilon_{2,j}|^{-1}).
\tag{B23}
$$

所以某个真整单位平移满足
$$
3n^2g\le\deg(n\Xi_0U_1^aU_2^b)
\le n^2g\sum_j M_j.
\tag{B24}
$$

所有 $M_j$ 只依固定多项式(A2)。本式没有把数值选出的单位当作新的
数学证书；实际坐标仍必须通过(B18)。若不计算范数权，也可按有限窗口
枚举整数 $(a,b)$，每次复用相同的全局模形式基与原三条输入。
任何有限窗口失败都不排除窗口外或更高权的原映射。



## 附录 C：实际有理3同源、较小准 Hom 与同一低权证书

本附录给一个不同于附录 B 单位操作的候选。它保留原
$\Xi_0$、$H_0$、$v$ 及全部 Hecke/Artin 归一化，却先把目标换为明确的
3-isogenous 曲线。较小准 Hom 的整数性尚未证明；不能因此预报低权
重建成功，也不能将它与(B21)的整性等价混同。

### C.1 两条明确的3同源及微分

记
$$
E=C_v:\quad Y^2+vY=X^3,\qquad
E':\quad Y'^2+vY'=X'^3-7v^2,
$$
$$
\omega=\frac{dX}{2Y+v},\qquad
\omega'=\frac{dX'}{2Y'+v}.
\tag{C1}
$$

两曲线和下列全部映射都定义在原 $F=\mathbf Q(v)$ 上。令
$$
\boxed{
\varphi:E\longrightarrow E',\qquad
X'=X+\frac{v^2}{X^2},\quad
Y'=Y-\frac{v^2(2Y+v)}{X^3}.
}
\tag{C2}
$$

把(C2)代入(C1)即得目标方程。它把
$O,(0,0),(0,-v)$ 送到 $O$，且这些点构成原有理三阶子群。
此外，$X'$ 作为 $X$ 的有理函数次数为3；与两曲线的二次 $X$ 映射比较，
说明 $\deg\varphi=3$。原点处延拓后它是真椭圆同源。

微分的两个共同因子准确为
$$
dX'=\left(1-\frac{2v^2}{X^3}\right)dX,\qquad
2Y'+v=(2Y+v)\left(1-\frac{2v^2}{X^3}\right).
$$
故
$$
\boxed{\varphi^*\omega'=\omega.}
\tag{C3}
$$

对偶同源的完整坐标是
$$
\boxed{
\widehat\varphi:E'\longrightarrow E,\qquad
X=\frac{X'^3-27v^2}{9X'^2},\quad
Y=\frac{Y'-13v}{27}
  +\frac{v^2(2Y'+v)}{X'^3}.
}
\tag{C4}
$$

可以把两边先平移为
$\widetilde Y=Y+v/2$、$\widetilde Y'=Y'+v/2$：
(C2)是从 $\widetilde Y^2=X^3+v^2/4$ 到
$\widetilde Y'^2=X'^3-27v^2/4$ 的规范3同源；
对后者再作同一个规范公式，随后按 $X/9,\widetilde Y/27$ 缩放，
恰得(C4)。因而(C4)的次数也是3。直接微分还给
$$
dX=\frac19\left(1+\frac{54v^2}{X'^3}\right)dX',
$$
$$
2Y+v=\frac1{27}(2Y'+v)
          \left(1+\frac{54v^2}{X'^3}\right),
$$
于是
$$
\boxed{
\widehat\varphi^*\omega=3\omega',\qquad
\widehat\varphi\varphi=[3]_E,\qquad
\varphi\widehat\varphi=[3]_{E'}.
}
\tag{C5}
$$

最后两式也可由原点归一和特征零的 Hom 微分注入推出。
这里所有 $3,9,27$ 和正号都由同一套坐标固定。

### C.2 较小准 Hom 与真实整数性的两种可能

在原 $J_0(2601)$ 上定义
$$
\boxed{
\Psi=\frac13\,\varphi\Xi_0
\in\operatorname{Hom}_F^0(J_0(2601),E').
}
\tag{C6}
$$

这是准同态群中的有理倍数，不是宣称目标点已可作唯一的全球三除。
由(C3)、(C5)，
$$
\Psi^*\omega'=\frac13 H_0(q)\frac{dq}{q},
\qquad
\widehat\varphi\Psi=\Xi_0.
\tag{C7}
$$

将曲线映射次数按平方齐次延拓到非零准 Hom，准确有
$$
\boxed{\deg\Psi=\frac13\deg\Xi_0.}
\tag{C8}
$$

设 $n_0,n_\Psi$ 分别是使 $n_0\Xi_0,n_\Psi\Psi$ 为真整 Hom 的最小正整数。
它们存在，因为两个对象已经是实际 Hom 空间中的准同态。
(C5)–(C7)给
$$
\boxed{n_0\mid n_\Psi\mid3n_0.}
\tag{C9}
$$

确切地，$n\Psi$ 整会经(C4)推出 $n\Xi_0$ 整；
而 $n\Xi_0$ 整只自动推出 $3n\Psi=\varphi(n\Xi_0)$ 整。
所以 $n_\Psi=n_0$ 或 $3n_0$。
第一种情况有真正三倍次数节省；第二种情况下最小整候选的次数反而是
原最小整映射的三倍。当前没有排除任何一种。

这个分叉正是它与整单位操作的区别。若再前复合(B3)的任意单位，
$\Psi U_1^aU_2^b$ 与 $\Psi$ 的清分母集合相同，但它们与 $\Xi_0$
之间仍只有(C9)，不自动有(B21)那样的等价。

### C.3 不生成新 CM 前缀的准确 germ

给定待测整数 $n\ge1$，令
$$
\lambda=n/3.
$$

先在原 $E$ 上使用 R870 的同一形式对数递推，只把其有理输入 $n$
换成 $\lambda$：
$$
u=\lambda qE(Q),\qquad Q=q^3,\qquad
E+3QE'=f(Q)\sqrt{1-4\lambda^3vQE^3},
$$
$$
T(Q)=-\frac{1+\sqrt{1-4\lambda^3vQE^3}}
               {2\lambda^3QE^3}.
\tag{C10}
$$

这里 $H_0=qf(Q)$ 仍是未经改动的原来源。
这个 $T$ 只是形式上 $(n/3)\Xi_0$ 的 $Y$ 坐标，不假设该准 Hom 整。

再施(C2)。由于原 $X^3=T(T+v)$，目标 germ 可只用一个有理函数得到：
$$
\boxed{
Y'_{\rm form}
=T-\frac{v^2(2T+v)}{T(T+v)}.
}
\tag{C11}
$$

这样既不需重新计算 CM 理想和，也不需为 $E'$ 编写新的形式群反演。
(C2)在原点的微分为1，故(C11)的实际微分是
$\lambda H_0\,dq/q$，正是 $n\Psi$。特别
$$
Y'_{\rm form}
=-\lambda^{-3}Q^{-1}
-\frac{v+3\lambda^{-3}}2+O(Q).
\tag{C12}
$$

(C11)相对于 $T$ 的修正从 $Q^1$ 开始，不改变这两个首项。

### C.4 同一个 $M_k(867)$ 基上的完整认证式

仍取 R870 的同一全局模形式基，写
$$
Y'=A/B,\qquad A,B\in M_k(\Gamma_0(867)),\quad B\ne0,
$$
$$
C_{A,B}=(D_QA)B-A(D_QB),\qquad D_Q=Q\,d/dQ.
$$

先按(C11)作同样的低线性重建，再必须严格检查
$$
\boxed{
C_{A,B}^{\,3}
=\left(\frac n3\right)^3
 H_0(q)^3
 \bigl(A^2+vAB+7v^2B^2\bigr)^2B^2.
}
\tag{C13}
$$

两边的权仍是 $6k+6$。检查至
$Q^{612(k+1)}$（包含末端）即为全局恒等式证书。
低重建长度 $204k+1$、允许共同 cusp 零、高维核唯一比值以及同一基
扩精度的要求完全保持。

若(C13)与(C12)的主项成立，准确恢复
$$
\boxed{
X'=\frac n3 H_0(q)
   \frac{Y'^2+vY'+7v^2}{D_QY'}.
}
\tag{C14}
$$

证明与 R870 相同，但须保新常数：
(C13)给 $X'^3=Y'^2+vY'+7v^2$ 和
$X'^2=D_QY'/(\lambda H_0)$；
由 $D_q=3D_Q$ 得
$dX'/(2Y'+v)=\lambda H_0\,dq/q$。
原点的主项确保 $\infty\mapsto O$，Hom 微分注入遂认出这个真态射
恰为原 $n\Psi$。

最后把(C14)、$Y'$ 代入(C4)，便得到
$$
\boxed{
\widehat\varphi\circ(n\Psi)=n\Xi_0
}
\tag{C15}
$$
的真实有理坐标。其微分为 $nH_0\,dq/q$，首部为
$X\sim n^{-2}q^{-2}$、$Y\sim-n^{-3}Q^{-1}$。
这里不再乘一个额外3；该3已在(C5)与$\lambda=n/3$中抵消。

因此一个成功的(C13)证书足以回到附录 A 的共同 $3n$、
原 $\kappa$、$2^{11}$ 和全 Artin 组合。该证书尚未执行成功；
它是保原目标的一个可执行备选，不是已找到的新坐标或非零 shadow。

对附录 B 的来源 $H_{a,b}$，把(C10)中的首尺度改为
$(n/3)c_{a,b}$，并在(C13)–(C14)中完整替换 $H_0$ 为 $H_{a,b}$ 即可。
首系数依旧不能除去。

### C.5 Petersson 选单位时的指数与面积规范

这一步只给候选选择的准确归一，不以数值范数认证一个全球 Hom。
在原 $C=X_0(2601)$ 上，
$$
\mu_C=[\operatorname{SL}_2(\mathbf Z):\Gamma_0(2601)]
=3672.
$$

设原三个首项1的新形式为 $F_j$，且
$H_0=\sum_j(G_j/3)F_j$，沿 R862 的同一复嵌入。
令
$$
N_j=\frac1{\mu_C}
 \int_{\Gamma_0(2601)\backslash\mathfrak H}
 |F_j(z)|^2\,dx\,dy,\qquad
\mathcal A_v=\int_{C_v(\mathbf C)}
 i\omega_v\wedge\overline{\omega_v}.
$$

因 $dq/q=2\pi i\,dz$，(B22)的正权准确为
$$
\boxed{
a_j=\frac{8\pi^2\mu_C}{\mathcal A_v}
       \left|\frac{G_j}{3}\right|^2N_j.
}
\tag{C16}
$$

不能把原源指数3672换成三阶商的1224，也不能把
$\mathcal A_v$ 换成未经 $\kappa^*\omega_0=(h/2^{11})\omega_v$
缩放的 $E_0$ 面积。若用同一正向周期基 $\Omega_1,\Omega_2$，
$\mathcal A_v=2\operatorname{Im}(\overline{\Omega_1}\Omega_2)$。

不过(B23)只用三个权的比，因此选择平衡单位时可以只用
$|G_j|^2N_j$，不计算共同面积。其结果只是整数指数候选；
是否真整、能否在给定权表示，仍由(B18)或(C13)完整决定。

PARI 官方 `mfpetersson(mfsymbol(...))` 明确采用上述
$1/\mu_C$ 归一，并在系数域次数大于1时返回全部复嵌入的矩阵。
三个不同 Hecke 本征线的非对角项数学上为零；数值实施仍必须将返回
嵌入按原 $b_j,G_j$ 和 $\varepsilon_{1,j},\varepsilon_{2,j}$
配对，不能只按矩阵出现次序猜原 Artin 标号。
参考：
<https://pari.math.u-bordeaux.fr/dochtml/html/Modular_forms.html#mfpetersson>。

本附录没有执行新的数学数值检查。当前公开低权重建可继续原计划；
备用同源与单位选择不要求取消或改动正在运行的原候选。
