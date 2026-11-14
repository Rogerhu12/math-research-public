# R169：有限 gauge 证书的闭关系复形与双慢方向的两轨道分离

日期：2026-11-12（UTC）。作者：literature。

状态：完整证明。R166 的有限轨道证书给出全部不变子商上、有限放大后的约化 Koszul 正合性及共同分母关系的闭核心；两个独立慢方向另有除有限 gauge 外的共同核零与两向量联合循环结论。多方向单个算子的核仍不因此被排除。

## 1. 两类输入与结论边界

本稿使用两种不同强度的输入，始终分开处理。

### 1.1. 快系数理想证书

设有限个 $T_1,\ldots,T_m,B_1,\ldots,B_m\in\mathcal A$ 满足
$$
\boxed{
D=\sum_{i=1}^mB_iT_i,\qquad
D\in\mathcal G\setminus\{0\}.
}
\tag{1.1}
$$
R151 给
$$
I\in\overline{D\,\mathbb C[A]}^{\rm SOT}.
\tag{1.2}
$$
所以存在多项式强近似
$$
U_\lambda=D p_\lambda(A)\longrightarrow I.
\tag{1.3}
$$
本稿不要求 $p_\lambda(A)$ 的范数一致有界。

R166 已证明：任意有限个加性慢模式的非零实际 $\mathcal G$ 系数多项式演算 $T$，
均可选有限 gauge 族
$$
T_i=\gamma_{\zeta_i}T
$$
及 $\mathcal A$ 系数 $B_i$ 得到 (1.1)。
因此下文 §§2–5 可直接用于这些有限轨道族。

### 1.2. 双慢方向消元证书

若两个独立慢方向上的两个多项式仅在 $K[w_1,w_2]$ 中互素，
其中 $K=\operatorname{Frac}\mathcal G$，
可得到某个非零单变量消元算子
$$
R(S_1)=U(S)T_1+V(S)T_2.
\tag{1.4}
$$
R152 保证左侧在全 $H$ 上单射稠密。
但它未必属于 $\mathcal G$，
也未获得其在任意不变限制上的稠密性。

因此 (1.4) 给全空间共同核零和总值域稠密；
它本身不提供 (1.1) 那种全部子商闭关系正合性。
这个区别是本稿的关键边界。

## 2. 快证书给全部层的约化 Koszul 正合

### 2.1. 复形和有界同伦

先在 $H$ 上证明。
令
$$
\mathscr H_k=H\otimes\bigwedge^k\mathbb C^m,\qquad 0\le k\le m.
$$
外代数使用标准正交基 $e_1,\ldots,e_m$。
记 $\varepsilon_i$ 为左楔乘 $e_i$，$\iota_i=\varepsilon_i^*$ 为内乘。
它们满足
$$
\iota_i\varepsilon_j+\varepsilon_j\iota_i
=\delta_{ij}I.
\tag{2.1}
$$

定义有界微分和升阶映射
$$
\delta=\sum_{i=1}^mT_i\otimes\iota_i,\qquad
h=\sum_{i=1}^mB_i\otimes\varepsilon_i.
\tag{2.2}
$$
全部系数在交换代数 $\mathcal A$ 中。
内乘反对易和 $T_iT_j=T_jT_i$ 给
$$
\delta^2=0.
$$
再由 (2.1) 及 $T_iB_j=B_jT_i$，
$$
\boxed{
\delta h+h\delta=D\otimes I.
}
\tag{2.3}
$$
写成逐层式为
$$
\delta_{k+1}h_k+h_{k-1}\delta_k
=D\otimes I_{\wedge^k},
\tag{2.4}
$$
端点取 $\delta_0=h_m=0$。

这是完整的有界算子恒等式，不涉及无界逆算子或形式分母。

### 2.2. 强正则化只给闭包正合

把 (1.3) 对角作用在每个外代数层，并定义
$$
H_{\lambda,k}
=(p_\lambda(A)\otimes I)h_k.
$$
因为全部系数交换，
$$
\delta_{k+1}H_{\lambda,k}
+H_{\lambda,k-1}\delta_k
=U_\lambda\otimes I.
\tag{2.5}
$$

若 $x\in\ker\delta_k$，则
$$
\delta_{k+1}H_{\lambda,k}x
=(U_\lambda\otimes I)x\longrightarrow x.
$$
反向包含由 $\delta^2=0$ 和 $\ker\delta_k$ 闭得到。
因此
$$
\boxed{
\ker\delta_k
=\overline{\operatorname{Ran}\delta_{k+1}}
\quad(0\le k\le m).
}
\tag{2.6}
$$
这称为约化正合，即把每一层的像取闭包后，所有同调为零。

端点明确给出
$$
\overline{\sum_i\operatorname{Ran}T_i}=H,\qquad
\bigcap_i\ker T_i=\{0\}.
\tag{2.7}
$$

中间层 (2.6) 是比这两个端点更强的实际有限放大结论。
但 $H_{\lambda,k}x$ 的范数可能发散；
本稿没有证明 $\operatorname{Ran}\delta_{k+1}$ 本来就是闭的，
也没有把 (2.6) 改写成普通不取闭包的正合性。

### 2.3. 全部不变子商及有限放大

设 $\mathcal Q=M/N$ 是闭 $A$ 不变子商。
每个 $\mathcal A$ 元素保持 $M,N$，
故 $T_i,B_i,D,p_\lambda(A)$ 都诱导 $\mathcal Q$ 上的有界算子。

(1.1)、(2.3) 作为有限有界恒等式直接下降。
取正交代表 $M\ominus N$，由 $U_\lambda\to I$ 强，
其诱导算子也强趋 $I_{\mathcal Q}$。
因此 §2.2 的每一步在 $\mathcal Q$ 上仍成立。

同理，先对 $A$ 作任意有限对角放大 $A^{(n)}$，
再取它的任意闭不变子商，也得到 (2.6)。
原因是每个 $T_i^{(n)},B_i^{(n)}$ 均在 $A^{(n)}$ 的范数多项式闭包内，
从而保持这些子空间和子商；
(1.3) 也在有限放大上强收敛。

这里没有把“某个全空间算子稠密”直接当成“其所有不变限制稠密”。
使用的是实际强近似单位及其明确下降。

## 3. 共同分母兼容关系有同一参数闭核心

定义闭子空间
$$
\mathscr C(T)
=\left\{(v_1,\ldots,v_m)\in H^m:
T_iv_j=T_jv_i\text{ 对全部 }i,j\right\}.
\tag{3.1}
$$
它是有限多个有界算子方程的共同核。

由于 $T_i$ 交换，
$$
\{(T_1x,\ldots,T_mx):x\in H\}\subseteq\mathscr C(T).
$$
反向取 $v=(v_i)\in\mathscr C(T)$，置
$$
x_0=\sum_iB_iv_i.
$$
兼容式给每个 $j$：
$$
T_jx_0
=\sum_iB_iT_jv_i
=\sum_iB_iT_iv_j
=Dv_j.
\tag{3.2}
$$
再取
$$
x_\lambda=p_\lambda(A)x_0,
$$
则
$$
(T_1x_\lambda,\ldots,T_mx_\lambda)
=(U_\lambda v_1,\ldots,U_\lambda v_m)
\longrightarrow(v_1,\ldots,v_m).
$$
所以
$$
\boxed{
\mathscr C(T)
=
\overline{\{(T_1x,\ldots,T_mx):x\in H\}}.
}
\tag{3.3}
$$

共同参数列映射
$$
x\longmapsto(T_1x,\ldots,T_mx)
$$
由 (2.7) 单射。
但其像未被宣称为闭像；(3.3) 是其精确闭核心结论。

(3.3) 同样对 §2.3 的全部子商及有限放大成立。
它是多分母兼容关系的实际闭图接口，
不需要任何一个 $T_i$ 已知单独单射。

## 4. 所有行关系都是反对称关系的极限

为了把中间正合性写成可直接使用的有限公式，
设
$$
\sum_iT_iv_i=0.
\tag{4.1}
$$
定义
$$
k_{ij}=B_jv_i-B_iv_j,\qquad k_{ji}=-k_{ij}.
$$
则
$$
\begin{split}
\sum_jT_jk_{ij}
&=\sum_jT_jB_jv_i-B_i\sum_jT_jv_j\\
&=Dv_i.
\end{split}
\tag{4.2}
$$
因此对 $k_{ij,\lambda}=p_\lambda(A)k_{ij}$，
$$
\left(\sum_jT_jk_{ij,\lambda}\right)_{i=1}^m
=(U_\lambda v_i)_{i=1}^m
\longrightarrow(v_i)_{i=1}^m.
\tag{4.3}
$$

每个反对称数组产生的向量都满足行关系，因为
$$
\sum_{i,j}T_iT_jk_{ij}=0.
$$
故 (4.3) 给出全体行关系的明确近似，
并使 §2 的中间层不只是抽象的同调记号。

## 5. 两分母情形：最大闭关系等于参数图闭包

本节假设两算子本身已具有快证书
$$
D=B_1T_1+B_2T_2\in\mathcal G\setminus\{0\}.
\tag{5.1}
$$
不能只从更大的有限轨道族有证书，默认任取两项也有 (5.1)。

定义
$$
\mathscr R_{\max}
=\{(x,y)\in H\oplus H:T_2x=T_1y\},
$$
以及
$$
\mathscr R_{\min}
=\overline{\{(T_1h,T_2h):h\in H\}}.
$$
(3.3) 给
$$
\boxed{\mathscr R_{\max}=\mathscr R_{\min}.}
\tag{5.2}
$$

这是闭线性关系的结论。
若 $T_1$ 有核，它未必是单值算子的图。
精确地，
$$
\mathscr R_{\max}(0)=\ker T_1,\qquad
\ker\mathscr R_{\max}=\ker T_2,
\tag{5.3}
$$
并且
$$
\overline{\operatorname{Dom}\mathscr R_{\max}}
=\overline{\operatorname{Ran}T_1}.
\tag{5.4}
$$
(5.4) 的两个包含都来自 (5.2)：参数图的第一坐标是 $\operatorname{Ran}T_1$，
而其闭包图的第一坐标仍落在 $\overline{\operatorname{Ran}T_1}$ 中。

实际 $\mathcal A$ 元素满足 $T_i^*=CT_iC$。
令 $\mathcal C(x,y)=(Cx,Cy)$。
对闭线性关系使用通常伴随定义
$$
(u,v)\in\mathscr R^*
\iff
\langle y,u\rangle=\langle x,v\rangle
\quad((x,y)\in\mathscr R).
$$
由参数图，
$$
\mathscr R_{\min}^*
=\{(u,v):T_2^*u=T_1^*v\}.
$$
结合 (5.2)，得到
$$
\boxed{\mathscr R_{\max}^*=\mathcal C\mathscr R_{\max}.}
\tag{5.5}
$$
所以这是准确的 $C$ 自伴闭关系。

如果另已证明 $T_1$ 单射，
共同 $C$ 对称性同时给其值域稠密；
此时关系成为稠密定义的闭算子
$$
T_1^{-1}T_2,\qquad
\operatorname{Dom}=\{x:T_2x\in\operatorname{Ran}T_1\},
$$
而参数图就是它的图核心。
没有这个额外单射输入时，本稿保留闭关系表述。

## 6. 两变量互素的有限消元

现在转向与 (1.1) 不同的消元输入。

设
$$
S_1,S_2\in\mathcal A,\qquad
\gamma_\zeta S_i-S_i\in\mathcal G,
$$
且 $\sigma_1,\sigma_2$ 在 $L/K$ 中对 $\mathbb C$ 线性无关。
R166 给它们在 $K$ 上代数无关。

取
$$
P,Q\in\mathcal G[w_1,w_2]
$$
在 $K[w_1,w_2]$ 中互素，且二者非零。
置
$$
T=P(S_1,S_2),\qquad U=Q(S_1,S_2).
$$

### 6.1. 不把互素误当成单位理想

把 $P,Q$ 看作 $K(w_1)[w_2]$ 中的多项式。
它们在这个一变量多项式环中仍互素。
否则一个正 $w_2$ 次数的公共不可约因子清除内容后，
由 Gauss 内容引理给 $K[w_1,w_2]$ 中的公共因子，矛盾。
若某个多项式只依赖 $w_1$，它在 $K(w_1)[w_2]$ 中是单位，也没有问题。

这里 Gauss 引理只使用：在唯一分解整环上，两个本原多项式的乘积仍本原。
对每个不可约素因子模掉后，剩余多项式环是整环，
所以素因子不可能整除乘积的全部系数而不整除其中一个因子的全部系数。
这保证公共因子可由分式域提升回本原多项式环。

在欧几里得环 $K(w_1)[w_2]$ 中求 Bézout 式并清除有限个 $w_1$ 有理分母，得到
$$
\boxed{
R_1(w_1)=A_1(w)P(w)+B_1(w)Q(w),
}
\tag{6.1}
$$
其中
$$
0\ne R_1\in K[w_1],\qquad A_1,B_1\in K[w_1,w_2].
$$
交换两个变量，亦有非零 $R_2(w_2)$ 属于同一理想。

这说明商代数
$$
K[w_1,w_2]/(P,Q)
$$
若非零，则是有限维 $K$ 向量空间：
将 $R_1,R_2$ 各自归一成首一多项式，
单项式
$$
w_1^iw_2^j,\quad
i<\deg R_1,\ j<\deg R_2
$$
已张成该商。
若某个 $R_i$ 是非零常数，理想本来就是全环。

但是一般的 $R_1$ 有正次数；
(6.1) 不是 $1\in(P,Q)$ 的断言。
有限维 $K$ 商也不是未经证明的有限自由 Hilbert 模型。

### 6.2. 真正清分母后使用单方向核定理

将 (6.1) 中所有系数的有限个 $K$ 分母用非零 $b\in\mathcal G$ 清除：
$$
\rho_1=bR_1\in\mathcal G[w_1],\qquad
\widetilde A_1=bA_1,\quad\widetilde B_1=bB_1\in\mathcal G[w].
$$
实际求值给
$$
\boxed{
\rho_1(S_1)
=\widetilde A_1(S)\,T+\widetilde B_1(S)\,U.
}
\tag{6.2}
$$
因为 $\sigma_1$ 对 $K$ 超越，非零多项式 $\rho_1$ 的求值非零。
R152 的单方向定理因此保证 $\rho_1(S_1)$ 在全 $H$ 上单射稠密。

若 $Tx=Ux=0$，由 (6.2) 得 $\rho_1(S_1)x=0$，故 $x=0$。
又因全部系数交换，
$$
\operatorname{Ran}\rho_1(S_1)
\subseteq\operatorname{Ran}T+\operatorname{Ran}U.
$$
所以
$$
\boxed{
\ker T\cap\ker U=\{0\},\qquad
\overline{\operatorname{Ran}T+\operatorname{Ran}U}=H.
}
\tag{6.3}
$$

此处只用了单方向消元算子在全空间的单射与稠密性。
在某个不变限制内，$\rho_1(S_1)$ 的像是否稠密仍未知；
在一般不变子商上，它是否仍单射也未由 R152 自动得到。
故 (6.3) 不被升格为 §§2–5 的普遍闭关系正合性。

## 7. 双慢方向中，只有有限 gauge 可能留下共同核

沿用 §6 的两个独立方向，取
$$
0\ne P\in\mathcal G[w_1,w_2],\qquad T=P(S_1,S_2).
$$
使用 R166 的半线性作用
$$
\Lambda_\zeta P(w)=(\alpha_\zeta P)(w+h_\zeta).
$$
其实际求值恰为 $\gamma_\zeta T$。

### 7.1. 不可约因子稳定子有限

先设 $P$ 在 $K[w_1,w_2]$ 中不是单位。
把它的不同不可约因子对应的主素理想记为
$$
\mathfrak p_1,\ldots,\mathfrak p_s.
$$
每个稳定子
$$
H_i=\{\zeta\in\Gamma:\Lambda_\zeta\mathfrak p_i=\mathfrak p_i\}
$$
都是子群。

如果 $H_i=\Gamma$，则 $\mathfrak p_i$ 是非零真稳定理想，
与 R166 附录的稳定理想定理矛盾。
所以 $H_i$ 是 $\Gamma$ 的真子群。

Prüfer $2$ 群的每个真子群有限：
若一个子群含有阶数任意大的元素，
则它包含每个唯一的有限子群 $\mu_{2^n}$，
从而等于整个 $\Gamma$。

因此每个 $H_i$ 都有限。
对固定 $i,j$，碰撞集合
$$
\{\zeta:\Lambda_\zeta\mathfrak p_i=\mathfrak p_j\}
$$
若非空，就是 $H_i$ 的一个陪集，也有限。
有限并仍有限。

于是存在有限集合 $\mathcal F\subseteq\Gamma$，使
$$
\boxed{
\gcd(P,\Lambda_\zeta P)=1
\quad(\zeta\notin\mathcal F).
}
\tag{7.1}
$$
可选一个有限 dyadic 子群 $H_0$ 包含 $\mathcal F$。

如果 $P$ 本来是 $K[w]$ 的单位，它与变量无关；
原 $P\in\mathcal G$ 非零，$T$ 已由 R151 单射稠密，下面结论对全部 gauge 都成立。

### 7.2. 两个核的交与两个像的和

对 $\zeta\notin H_0$，将 §6 用于 $P,\Lambda_\zeta P$，得到
$$
\boxed{
\ker T\cap\ker\gamma_\zeta T=\{0\},\qquad
\overline{\operatorname{Ran}T+\operatorname{Ran}\gamma_\zeta T}=H.
}
\tag{7.2}
$$
若 $\gamma_\zeta T=U_\zeta T U_\zeta^*$，则等价为
$$
\boxed{
\ker T\cap U_\zeta\ker T=\{0\},\qquad
\overline{\operatorname{Ran}T+U_\zeta\operatorname{Ran}T}=H.
}
\tag{7.3}
$$

这是真实的两个 gauge 之间的共同核结论。
没有把两个核的交为零写成每个核为零，
也没有声称两个子空间之间有统一正角或闭和。

### 7.3. 混合依赖模式但独立类维数为二

如果原来有有限多个模式，而 R166 的类空间维数恰为二，
先按其常系数变换和有限清分母，把原非零演算写成
$$
bT=P(T_1,T_2),\qquad
0\ne b\in\mathcal G,\quad
P\in\mathcal G[w_1,w_2]\setminus\{0\},
$$
其中 $T_1,T_2$ 是两个独立方向。

$\ker(bT)=\ker T$，因为 $b$ 单射；
对 gauge 像同样有
$$
\ker\gamma_\zeta(bT)=\ker\gamma_\zeta T.
$$
而 $\operatorname{Ran}(bT)\subseteq\operatorname{Ran}T$，
因 $b,T$ 交换。
因此对 $bT$ 得到的 (7.2) 也传回原来的 $T$。

类维数为零或一时，单个非零演算已分别由 R153 或 R152 处理。
类维数至少三时，两个互素多项式的商通常仍有正维数，
本稿不作 (7.2) 的一般断言。

## 8. 真实有限放大：若干 gauge 核的代数直和

令 $H_0$ 如 §7，选有限个不同 $H_0$ 陪集的代表
$$
\zeta_1,\ldots,\zeta_\ell.
$$
记
$$
T_i=\gamma_{\zeta_i}T,\qquad M_i=\ker T_i.
$$
由 (7.2) 及 gauge 共轭，
$$
M_i\cap M_j=\{0\}\quad(i\ne j).
\tag{8.1}
$$
这里只凭一般子空间的两两交零，还不能推出代数直和；
下面额外使用实际 $T_i$ 的交换性。

假设
$$
x_i\in M_i,\qquad\sum_i x_i=0.
$$
固定 $i$，作用有界算子
$$
\prod_{j\ne i}T_j.
$$
除第 $i$ 项外，每项都被对应的 $T_j$ 杀掉，所以
$$
\left(\prod_{j\ne i}T_j\right)x_i=0.
\tag{8.2}
$$
因为 $T_i,T_j$ 交换，$T_j$ 保持 $M_i$；
又由 (8.1)，$T_j|_{M_i}$ 单射。
因此 (8.2) 中的有限乘积在 $M_i$ 上单射，得 $x_i=0$。

所以
$$
\boxed{
M_1+\cdots+M_\ell
\text{ 是代数直和}.
}
\tag{8.3}
$$
相应和映射
$$
\mathcal J:\bigoplus_{i=1}^\ell M_i\longrightarrow H,
\qquad
\mathcal J(x_1,\ldots,x_\ell)=\sum_i x_i
\tag{8.4}
$$
是有界单射，范数不超过 $\sqrt\ell$，
并交织 $\bigoplus_i A|_{M_i}$ 与 $A$。

本稿没有证明 $\mathcal J$ 有闭值域、下界或有界逆。
(8.3) 也不是正交直和。
这是一个真实有限放大结构，不能据此声称 $\dim M_i$ 有限。

## 9. 两向量联合循环

设 $g$ 是 $A$ 的循环向量，特别可取 $g=1$。
令
$$
f=Tg.
$$
因为 $T\ne0$ 且 $g$ 循环，$f\ne0$。

由 $T$ 有界并与 $A$ 交换，
$$
\overline{\operatorname{span}}\{A^nf:n\ge0\}
=\overline{\operatorname{Ran}T}.
\tag{9.1}
$$
gauge 协变保证 $U_\zeta g$ 仍循环：
$U_\zeta A^n$ 与 $A^nU_\zeta$ 只差非零标量因子。
又
$$
U_\zeta f=(\gamma_\zeta T)U_\zeta g.
$$
因此
$$
\overline{\operatorname{span}}\{A^nU_\zeta f:n\ge0\}
=\overline{\operatorname{Ran}\gamma_\zeta T}.
\tag{9.2}
$$
结合 (7.2)，对全部 $\zeta\notin H_0$，
$$
\boxed{
\overline{\operatorname{span}}
\{A^nf,\ A^nU_\zeta f:n\ge0\}=H.
}
\tag{9.3}
$$

所以双独立慢方向上的任意非零实际多项式乘子，
作用于循环向量后，所得向量和除有限例外外的一个 gauge 像构成联合循环对。
这不等价于其中任意一个向量单独循环。

## 10. 真实慢平方及有限重叠双模式的具体应用

### 10.1. 任意可和第一阶的二次点态式

设
$$
u=a_*+\sum_ja_j\chi_j,\qquad a\in\ell^1,
$$
以及任意复杂平方可和第一阶指数
$$
w=c_*+\sum_jc_j\chi_j,\qquad c\in\ell^2.
$$
R147 已证明 $e^w\in H$ 且循环。

使用 R160 的真实倾斜算子
$$
R_j(c_j)
=(I-e^{-2c_j}N_j)(I+e^{-2c_j}N_j)^{-1}.
\tag{10.1}
$$
对固定 $c\in\ell^2$，$\sup_j\|R_j(c_j)\|<\infty$，
且其代数字符均为 $1$。
有限不同位集合满足
$$
\left(\prod_{j\in J}R_j(c_j)\right)e^w=\chi_J e^w.
\tag{10.2}
$$
不把 (10.2) 改成同一位平方的乘法同态。

定义
$$
S=a_*I+\sum_ja_jR_j(c_j),\qquad
D_u=\sum_ja_j^2(I-R_j(c_j)^2).
\tag{10.3}
$$
前式由 $a\in\ell^1$，后式由 $\sum_j|a_j|^2<\infty$ 按算子范数绝对收敛，
故 $S,D_u\in\mathcal A$。

固定一个 dyadic $\zeta$ 后，所有充分高位 $N_j$ 在 gauge 下不变。
因此 $\gamma_\zeta S-S$ 和 $\gamma_\zeta D_u-D_u$ 都只剩有限低位有理解析函数之和；
这些函数在 $A=0$ 附近是真正解析芽。
所以
$$
\gamma_\zeta S-S\in\mathcal G,\qquad
\gamma_\zeta D_u-D_u\in\mathcal G.
\tag{10.4}
$$

在有限截断中展开 $u^2$，用 (10.2) 处理不同位交叉项，
并用 $\chi_j^2=1$ 保留同位修正，得到
$$
u^2e^w=(S^2+D_u)e^w.
\tag{10.5}
$$
由于 $a\in\ell^1$，点态截断一致收敛，相关算子级数也绝对范数收敛；
乘 $e^w\in L^2$ 后可合法取极限。

于是对任意次数至多二的
$$
q(t)=q_2t^2+q_1t+q_0,
$$
有真实恒等式
$$
\boxed{
q(u)e^w=T e^w,\qquad
T=q(S)+q_2D_u.
}
\tag{10.6}
$$
若左侧非零，则 $T\ne0$。
反之，因 $e^w$ 循环，$T\ne0$ 也保证左侧非零。

$S,D_u$ 只有两个加性慢方向，其在 $L/K$ 中的类维数至多二。
若维数为零或一，R166 的相应归约给 $T$ 单射稠密，左侧已单独循环。
若维数为二，则 §7–9 适用。

因此有如下不要求预先判定两个类是否独立的结论：

**推论10.1。** 若 $q(u)e^w\ne0$，则存在有限 dyadic 子群 $H_0$，使对所有 $\zeta\notin H_0$，
$$
\boxed{
\overline{\operatorname{span}}
\{A^n(q(u)e^w),\
A^nU_\zeta(q(u)e^w):n\ge0\}=H.
}
\tag{10.7}
$$

这包括尚未单独排核的慢平方共振。
尤其不要求 $D_u\in\mathcal G$；
R160 已证明某些慢尾的这种二阶修正确实不属于 $\mathcal G$。
这里把它当作第二个具有 $\mathcal G$ 增量的加性方向，而非快系数。

### 10.2. 两个可和模式的有限重叠双线性式

再设
$$
v=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^1,
$$
且两个非零系数支撑的交集有限。
仍使用同一指数 $w$ 和同一倾斜算子 $R_j(c_j)$。
定义
$$
S_u=a_*I+\sum_ja_jR_j(c_j),\qquad
S_v=b_*I+\sum_jb_jR_j(c_j),
$$
及
$$
D_{uv}=\sum_ja_jb_j(I-R_j(c_j)^2).
$$
由于共同支撑有限，$D_{uv}$ 是真正一元解析函数的有限和，因而属于 $\mathcal G$。
不同位精确式 (10.2) 和同位修正给
$$
uv\,e^w=(S_uS_v+D_{uv})e^w.
\tag{10.8}
$$

所以任何实际非零
$$
f=(\alpha uv+\beta u+\gamma v+\delta)e^w
$$
都等于
$$
[\alpha S_uS_v+\beta S_u+\gamma S_v+\delta I+\alpha D_{uv}]e^w.
$$
这是至多两个加性慢方向上的 $\mathcal G$ 系数多项式。
相同的类维数归约和 §9 给：
除有限 dyadic gauge 例外外，$f$ 与 $U_\zeta f$ 联合循环。

本小节只处理上述双线性形式。
任意二次多模式符号的自平方修正可能引入更多独立慢方向，
不能仅凭“总次数为二”就套用两方向结论。

## 11. 当前未跨越的边界

1. R166 的有限快证书给 (2.6)，其中闭包不能删除；本稿没有构造一致有界的 contracting homotopy。
2. 多分母共同关系 (3.3) 的闭核心，不自动传给任意两个坐标投影；投影后的闭性及最大两分母关系需要单独证明。
3. 两变量互素只给有限维 $K$ 商和单变量消元；它通常不给单位理想，也不直接给非零 $\mathcal G$ 元素属于两生成理想。
4. 消元算子 $R(S_1)$ 的全空间单射稠密，不能替代其在未知不变限制或子商上的同性质。
5. 不同 gauge 核的交零、代数直和及两向量联合循环，都没有把不同目标的跨核配对合并。
6. 类维数至少二时，单个非零实际多项式演算的核仍未由本稿排除。
7. 完整 Hilbert 不变子空间问题与本课题一般闭不变子空间缺口保持开放。

## 12. 依赖与新增内容

- R151：非零 $\mathcal G$ 元素的强主理想单位。
- R152：一个加性慢方向上非零 $\mathcal G$ 系数多项式演算的全空间单射稠密。
- R166：线性类与代数独立、稳定理想定理、混合依赖归约及有限 gauge 快证书。
- R32 及实际共轭：所有有界演算位于交换 $\mathcal A$，并有共同 $C$ 对称性。

本稿的新结论是：有限轨道证书的全部层约化 Koszul 正合与共同参数闭核心；
双慢方向的有限例外两轨道共同核零；
若干 gauge 核的代数直和及相应联合循环对；以及任意可和第一阶二次点态式带平方可和指数权的具体联合循环应用。
所有使用的闭图、子商和有限放大步骤已在正文给出。
