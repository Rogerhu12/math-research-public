# 原 Deddens 范数闭包：全部 2-adic 平移的精确距离与平移生成代数的自伴核

日期：2026-11-27（UTC+8）。会话：`Astra-ISP-8542378f-20261127`，分工 `literature_deddens`；AI-assisted，GPT-6 Astra Pro。

**状态：第 2–7 节的结论均已证明。** 结论针对原 Haar 算子，不是抽象替代模型。整个 $\overline{\mathcal D_A}^{\|\cdot\|}$ 的自伴核是否仍为乘法 MASA，**本稿没有解决**。本稿给出全部实际 $2$-adic 加权平移与该闭包的精确距离，并在一个明确的具体 $C^*$ 代数内完整确定自伴核；最后证明该 $C^*$ 代数并不包含整个 $\mathcal D_A$，所以不能删掉这个范围。

## 1. 为什么不能自动取范数闭包

前稿已证 $\mathcal D_A\cap\mathcal D_A^*=\mathcal M$，其中 $\mathcal M$ 是原乘法 MASA。但该证明中的全正幂成本必须固定；若只给普通算子范数逼近，则成本可以无界，不能沿用该证明。

这也不是一个能用通用三角代数定理补上的步骤。J. L. Orr，*On the closure of triangular algebras*，American Journal of Mathematics **112** (1990), 481–497，给出非范数闭的最大三角代数，包括传递例子；本次核对的[作者原始论文摘要页](https://johnorr.uk/research/abstracts.html)明确陈述了这些范围。以下全部结论由本模型额外的有限字符、真实块和权重结构直接证明。

## 2. 原对象与收缩的有限字符提取

仍取
$$
H=L^2(\mathbb Z_2,\mu),\qquad Af(y)=w(y)f(y-1),
$$
$$
w(0)=0,\qquad w(y)=\alpha_{v_2(y)}\ (y\ne0),\qquad
\alpha_j=\exp\left(-\frac{280}{3}16^j+90\,8^j-300\,2^j+\frac{850}{3}\right).
$$
记
$$
\mathcal D=\mathcal D_A,\qquad \mathcal R=\overline{\mathcal D}^{\|\cdot\|},\qquad
\mathcal M=\{M_v:v\in L^\infty(\mathbb Z_2)\},
$$
以及
$$
\beta_n=\|A^n\|,\quad \varepsilon_m=\frac{\alpha_m}{\beta_{2^m-1}}\longrightarrow0.
\tag{2.1}
$$
事实上 $\varepsilon_m\le\exp(-(90/7)16^m)$，且 $2^m\varepsilon_m\to0$。

对每个 $t\in\mathbb Z_2$ 定义真正的保测平移
$$
(U^tf)(y)=f(y-t).
$$
这里 $t$ 不限于普通整数；$U^t$ 是原 $H$ 上的酉算子。若 $t\in\mathbb Z$，这与通常的整数幂一致。

固定 $m$，令 $N=2^m$，$P_{m,r}$ 为余类 $r+N\mathbb Z_2$ 的乘法投影，$0\le r<N$。令
$$
\chi_m(y)=e^{2\pi i(y\bmod N)/N},\qquad V_m=M_{\chi_m}.
$$
对 $a\in\{0,\ldots,N-1\}$ 定义
$$
\mathcal F_{m,a}(X)=\frac1N\sum_{q=0}^{N-1}e^{-2\pi iqa/N}V_m^qX V_m^{-q}.
\tag{2.2}
$$
它是范数至多一的线性映射。有限 Fourier 正交性给准确块公式
$$
\boxed{\mathcal F_{m,a}(X)=
\sum_{s=0}^{N-1}P_{m,(s+a)\bmod N}X P_{m,s}.}
\tag{2.3}
$$
因此它保留低头行列差等于 $a\pmod N$ 的整条循环块对角线。

乘法酉及其逆都有 Deddens 成本 $1$，故每项共轭保持 $\mathcal D$，并且
$$
c_A(\mathcal F_{m,a}(X))\le c_A(X)\quad(X\in\mathcal D).
\tag{2.4}
$$
特别，$\mathcal F_{m,a}$ 也保持范数闭包 $\mathcal R$。

写 $t=a_m+Nb_m$，其中 $0\le a_m<N$。对任意 $v\in L^\infty$，
$$
\boxed{\mathcal F_{m,a_m}(M_vU^t)=M_vU^t.}
\tag{2.5}
$$
这只是字符在平移 $t$ 下的准确相位，不使用对整个 $B(H)$ 存在圆作用的假设。

## 3. 回绕块的费用与距离下界

令
$$
E_m(t)=\{y\in\mathbb Z_2:y\bmod 2^m<a_m\},\qquad a_m=t\bmod 2^m.
\tag{3.1}
$$
在输出头 $r<a_m$ 时，$U^t$ 的输入头为 $s=r-a_m+N>r$；尾平移为 $z\mapsto z-b_m-1$。所以这些正是整条块对角线中发生低头回绕的**上三角块**。

[全 Deddens 最优有限头稿](R12-appendix-full-deddens-algebra-optimal-cost-finite-head-approximation.md) §2 给真实全尾估计
$$
\|X_{rs}\|\le c_A(X)\varepsilon_m\quad(r<s).
\tag{3.2}
$$
在 (2.3) 所选的循环块对角线上，每行、每列至多一个块。因而取回绕部分时，不需三角截断的维数因子：
$$
\boxed{\|M_{\mathbf1_{E_m(t)}}\mathcal F_{m,a_m}(X)\|
\le c_A(X)\varepsilon_m\qquad(X\in\mathcal D).}
\tag{3.3}
$$
结合 (2.5)、提取映射的收缩性和左乘投影的收缩性，对每个固定 $X\in\mathcal D$ 有
$$
\boxed{\|M_vU^t-X\|\ge
\|v\mathbf1_{E_m(t)}\|_\infty-c_A(X)\varepsilon_m.}
\tag{3.4}
$$
先固定这个实际 $X$，再令 $m\to\infty$，得到
$$
\operatorname{dist}(M_vU^t,\mathcal R)
=\operatorname{dist}(M_vU^t,\mathcal D)
\ge\limsup_m\|v\mathbf1_{E_m(t)}\|_\infty.
\tag{3.5}
$$
这一步允许不同逼近算子的成本任意大，因为取 $m$ 的极限发生在对 $X$ 取下确界**之前**；没有假设逼近族有统一费用。

## 4. 全部 2-adic 加权平移的精确距离

把普通非负整数嵌入 $\mathbb Z_2$，记为 $\mathbb N_0$。

**定理 4.1。** 对任意 $t\in\mathbb Z_2$ 和 $v\in L^\infty$：

1. 若 $t\notin\mathbb N_0$，则
   $$
   \boxed{\operatorname{dist}(M_vU^t,\mathcal R)=\|v\|_\infty.}
   \tag{4.1}
   $$
   特别，任何非零负整数或非整数 $2$-adic 加权平移都不属于 $\mathcal R$。

2. 若 $t=n\in\mathbb N_0$，则对 $2^m>n$ 置
   $$
   E_m(n)=\bigcup_{r=0}^{n-1}(r+2^m\mathbb Z_2),
   $$
   空并取空集。有
   $$
   \boxed{\operatorname{dist}(M_vU^n,\mathcal R)
   =\lim_{m\to\infty}\|v\mathbf1_{E_m(n)}\|_\infty.}
   \tag{4.2}
   $$

**证明第一项。** $t\notin\mathbb N_0$ 当且仅当其二进展开有无穷多个 $1$。在任意一个满足第 $j$ 位 $t_j=1$ 的位置，若 $y_j=0$，则
$$
y\bmod2^{j+1}<t\bmod2^{j+1},
$$
不论更低位为何；所以 $\{y:y_j=0\}\subseteq E_{j+1}(t)$。
Haar 位独立且公平，故对每个起点 $J$，无穷多个这种位同时满足 $y_j=1$ 的集合测度为零。于是
$$
\mu\left(\bigcup_{m\ge J}E_m(t)\right)=1\qquad(J\ge1).
\tag{4.3}
$$
若 $0<q<\|v\|_\infty$，集合 $\{|v|>q\}$ 有正测度。由 (4.3)，对每个 $J$ 都有某个 $m\ge J$，使其与 $E_m(t)$ 的交有正测度。因此
$$
\limsup_m\|v\mathbf1_{E_m(t)}\|_\infty\ge q.
$$
令 $q\uparrow\|v\|_\infty$，再用反向显然上界，右侧恰为 $\|v\|_\infty$。式 (3.5) 给距离下界；取 $X=0$ 给相同上界。这也包含 $v=0$。

**证明第二项。** $E_m(n)$ 随充分大的 $m$ 递减，故 (4.2) 右端的极限存在。式 (3.5) 已给下界。
令
$$
W_n(y)=\prod_{j=0}^{n-1}w(y-j),\qquad W_0=1.
$$
这是连续函数，零集恰为 $\{0,1,\ldots,n-1\}$；在紧集 $E_m(n)^c$ 上有严格正的最小值。故
$$
v_m=v\mathbf1_{E_m(n)^c},\qquad v_m/W_n\in L^\infty,
$$
进而
$$
M_{v_m}U^n=M_{v_m/W_n}A^n\in\mathcal D.
$$
其与原目标的距离恰为 $\|v\mathbf1_{E_m(n)}\|_\infty$。令 $m\to\infty$ 即得所需上界。$n=0$ 时目标本来就是乘法算子。证毕。

对于 $n\ge1$，(4.2) 还等价于
$$
M_vU^n\in\mathcal R
\quad\Longleftrightarrow\quad
\lim_{\delta\downarrow0}\|v\mathbf1_{\{W_n<\delta\}}\|_\infty=0.
\tag{4.4}
$$
因为两类集合 $E_m(n)$ 与 $\{W_n<\delta\}$ 是同一有限零集的互相余终邻域。这里要求的是**本质上确界意义的一致消失**，不是仅在有限零集上指定函数值。

这里另有已证明的准确必要成本式：对 $n\ge1$，
$$
M_vU^n\in\mathcal D\quad\Longleftrightarrow\quad v/W_n\in L^\infty,
\qquad c_A(M_vU^n)=\beta_n\|v/W_n\|_\infty.
\tag{4.5}
$$
参见 [Deddens 分类原稿 §3](R12-appendix-deddens-algebra-localizing-and-uniform-cost-obstruction.md)：望远镜恒等式把 $A^k$ 比较的最佳常数写成 $\operatorname*{ess\,sup}_y |v(y)|W_n(y+k)/W_n(y)$，然后用正向 odometer 尾轨道稠密及 $W_n$ 连续得到 $\sup_{k\ge n}W_n(y+k)=\beta_n$；可数上确界与本质上确界可交换，故必要下界也是准确成本。

例子：$M_{\sqrt{W_n}}U^n\in\mathcal R$，但当 $n\ge1$ 时不在 $\mathcal D$，因为 $1/\sqrt{W_n}$ 本质无界，(4.5) 给无穷成本。未加权的 $U^n$ 对每个 $n\ne0$ 都满足到 $\mathcal R$ 的距离为 $1$。

**有限和推论。** 若 $t_1,\ldots,t_k$ 是互异的 $2$-adic 数，则
$$
\sum_{j=1}^kM_{v_j}U^{t_j}\in\mathcal R
$$
当且仅当每个非零项都满足：$t_j\in\mathbb N_0$，且对应的 (4.4) 成立（$t_j=0$ 无额外限制）。
必要性：取足够大的 $m$，所有 $t_j\bmod2^m$ 互异，用一次有限提取 (2.2) 精确分离各项；它保持 $\mathcal R$。充分性由有限和封闭性。特别地，这类有限和中属于 $\mathcal R\cap\mathcal R^*$ 的只有乘法算子。

## 5. 一个具体完整 $C^*$ 范围内的自伴核

定义原表示上的 $C^*$ 代数
$$
\mathcal B=\overline{\operatorname{span}\{M_vU^t:
v\in L^\infty(\mathbb Z_2),\ t\in\mathbb Z_2\}}^{\|\cdot\|}.
\tag{5.1}
$$
乘法及伴随的准确式为
$$
(M_vU^s)(M_zU^t)=M_{v\,z(\cdot-s)}U^{s+t},\qquad
(M_vU^t)^*=M_{\bar v(\cdot+t)}U^{-t},
$$
所以 (5.1) 确实是含单位的具体 $C^*$ 代数。这里包含所有 $L^\infty$ 乘子和所有真正的 $2$-adic 平移，不只包含 UHF 代数。

**定理 5.1。**
$$
\boxed{\mathcal R\cap\mathcal R^*\cap\mathcal B=\mathcal M.}
\tag{5.2}
$$

### 5.1 仅在 $\mathcal B$ 上构造所需连续紧群作用

令 $G$ 为全部有限阶连续字符 $\chi:\mathbb Z_2\to\mathbb T$。将 $G$ 嵌入 $\mathbb T^{\mathbb Z_2}$，令
$$
K=\overline{\{(\chi(t))_{t\in\mathbb Z_2}:\chi\in G\}}.
$$
这是紧阿贝尔群。其元素 $k$ 满足 $k(s+t)=k(s)k(t)$；所有坐标函数 $k\mapsto k(t)$ 都是连续字符，彼此区分 $K$ 中的点。对 $t\ne s$，某个有限字符区分它们，所以坐标字符 $k(t)$ 和 $k(s)$ 也互异。

在有限和上定义
$$
\gamma_k\left(\sum_tM_{v_t}U^t\right)
=\sum_t k(t)M_{v_t}U^t.
\tag{5.3}
$$
有限和表示唯一：对互异的有限个 $t$，选择足够细的 (2.2) 即可逐项分离。若 $k$ 来自原字符 $\chi$，(5.3) 恰为 $M_\chi X M_\chi^*$，故等距。一般 $k$ 可用原字符的网在所用有限个坐标上逼近，有限和因而在范数中收敛，仍保范数。由稠密性，(5.3) 延成 $\mathcal B$ 的等距 $*$-自同构，逆为 $\gamma_{k^{-1}}$；对每个 $X\in\mathcal B$，映射 $k\mapsto\gamma_k(X)$ 范数连续。

这段证明**没有**把该作用延到全部 $B(H)$ 或全部 $\mathcal D$，也没有假定非原字符的 $k$ 在当前表示中由一个已知酉实现。

### 5.2 完整频率系数与唯一性

对 $K$ 的 Haar 概率测度积分，定义收缩映射
$$
\mathcal E_t(X)=\int_K\overline{k(t)}\,\gamma_k(X)\,dk.
\tag{5.4}
$$
字符正交性给有限和的准确第 $t$ 项。通过范数逼近，有
$$
\mathcal E_t(X)=M_{v_t}U^t\quad\text{对某个 }v_t\in L^\infty,
\tag{5.5}
$$
因为 $v\mapsto M_vU^t$ 是等距映射，其像范数闭。

另外，对每个 $X\in\mathcal B$，
$$
\boxed{\mathcal F_{m,t\bmod2^m}(X)\longrightarrow\mathcal E_t(X)
\quad\text{于算子范数}.}
\tag{5.6}
$$
对有限和，当 $m$ 充分大时提取准确等于第 $t$ 项（若无此项，则为零）；两边都是收缩映射，故有限和的范数稠密性证明 (5.6)。由 (2.4) 和 $\mathcal R$ 的范数闭性，
$$
X\in\mathcal R\cap\mathcal B\quad\Longrightarrow\quad
\mathcal E_t(X)\in\mathcal R.
\tag{5.7}
$$

这些系数在 $\mathcal B$ 内唯一决定算子。事实上，若全部 $\mathcal E_t(X)=0$，固定 $f,g\in H$，连续函数
$F(k)=\langle\gamma_k(X)f,g\rangle$
与每个坐标字符 $k(t)$ 正交。坐标字符的线性张成含常数、对乘法和复共轭封闭、并区分 $K$ 的点。Stone–Weierstrass 定理使其在 $C(K)$ 中稠密。因此 $F$ 与自身正交，连续性及 Haar 满支集给 $F=0$。特别在单位元处有 $\langle Xf,g\rangle=0$，故 $X=0$。

### 5.3 自伴核的证明

取 $X\in\mathcal R\cap\mathcal R^*\cap\mathcal B$。由 (5.5)、(5.7) 和定理 4.1，当 $t\notin\mathbb N_0$ 时，$\mathcal E_t(X)=0$。当 $t$ 是正整数时，
$$
\mathcal E_{-t}(X^*)=\mathcal E_t(X)^*=0,
$$
因为 $X^*\in\mathcal R\cap\mathcal B$，且 $-t\notin\mathbb N_0$。所以所有非零频率系数均消失。$\mathcal E_0(X)$ 是乘法算子，而 $X-\mathcal E_0(X)$ 的全部系数为零；§5.2 的唯一性给 $X=\mathcal E_0(X)\in\mathcal M$。反向包含显然，证明 (5.2)。

## 6. 范围不能删除：整个 Deddens 代数确有不属于 $\mathcal B$ 的元素

记原多项式范数闭包为
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$

**定理 6.1。**
$$
\boxed{\{A\}'\cap\mathcal B=\mathcal A.}
\tag{6.1}
$$

**证明。** $\mathcal A\subseteq\{A\}'\cap\mathcal B$ 显然。反向取 $X\in\{A\}'\cap\mathcal B$。因为
$\gamma_k(A)=k(1)A$，每个 $\gamma_k(X)$ 仍与 $A$ 交换，故每个 $\mathcal E_t(X)$ 也交换。交换子属于 $\mathcal D$，成本为其普通范数；所以由定理 4.1，只可能有 $t=n\in\mathbb N_0$ 的非零系数。

若 $M_bU^n$ 与 $A$ 交换，准确相消式为
$$
b(y)w(y-n)=w(y)b(y-1)\quad\text{a.e.}
$$
当 $n\ge1$，$W_n$ 满足同一式且几乎处处为正，所以 $b/W_n$ 是有限可测的平移不变函数。遍历性给 $b/W_n=c_n$ 几乎处处，于是 $M_bU^n=c_nA^n$。这里无需比值有界或可积：对其有界一一可测变换应用遍历性即可。$n=0$ 时直接得到 $b$ 常数。故
$$
\mathcal E_t(X)\in\mathcal A\quad\text{对全部 }t\in\mathbb Z_2.
$$
若 $X\notin\mathcal A$，Hahn–Banach 给一个有界线性泛函 $\ell$，在 $\mathcal A$ 上为零而 $\ell(X)\ne0$。连续函数 $k\mapsto\ell(\gamma_k(X))$ 的所有字符系数都为 $\ell(\mathcal E_t(X))=0$。由 §5.2 的同一 Stone–Weierstrass 论证，它恒为零，特别 $\ell(X)=0$，矛盾。这证明 (6.1)。

[R38 §5](R38-relative-commutant-and-strong-multipliers.md) 已从 R37 的原强乘积极限（可取 $s_j=0,t_j=1/(j+2)$）给出实际有界算子
$$
Y\in\{A\}',\qquad Y\notin\mathcal A.
$$
因此 (6.1) 推出
$$
\boxed{Y\in\mathcal D\setminus\mathcal B.}
\tag{6.2}
$$
本稿只使用 R38 已登记的这一明确存在性，不重做其乘积构造。这证明 §5 的具体范围确实小于整个 Deddens 代数；不存在把所有 $X\in\mathcal D$ 放进 $\mathcal B$ 的自动步骤。

## 7. 全 $B(H)$ 上的系数消失并不保证唯一性

最后给一个实际反例，说明不能从全部移动字符提取趋零推出算子为零。令
$$
P_{\mathbf1}f=\left(\int f\,d\mu\right)\mathbf1.
$$
对每个 $m,a$，(2.2) 给
$$
\mathcal F_{m,a}(P_{\mathbf1})
=\frac1N\sum_{q=0}^{N-1}e^{-2\pi iqa/N}
|\chi_m^q\rangle\langle\chi_m^q|.
$$
这些字符两两正交，故
$$
\boxed{\|\mathcal F_{m,a}(P_{\mathbf1})\|=\frac1{2^m}}
\tag{7.1}
$$
对每个 $a$ 一致成立。因此即便对全部 $t\in\mathbb Z_2$，都使用 $a=t\bmod2^m$，这些提取仍全部按范数趋零，而 $P_{\mathbf1}\ne0$。

这不与 §5.2 矛盾：该秩一投影不属于 $\mathcal B$，否则 (7.1)、(5.6) 与系数唯一性会迫使它为零。原 Deddens 范数闭包不含非零紧算子已在旧稿证明，所以 (7.1) 也没有提供 $\mathcal R\cap\mathcal R^*$ 的反例。

**仍然开放的准确问题。** 是否 $\mathcal R\cap\mathcal R^*=\mathcal M$，需要控制 (6.2) 所展示的、超出 $\mathcal B$ 的真实部分。不能靠只检查普通整数频率、未经证明的全代数圆作用，或把所有字符系数消失当作全 $B(H)$ 唯一性来结束。
