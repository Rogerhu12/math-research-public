# 原共同 Y/K 的有理等距变换、准确 p 级字及 norm11 端点

日期：2026-11-27。状态：本文的有理等距矩阵、原 split p Schwartz 稳定子与至少一个准确导子 p^n 的角色，以及固定 norm11 角端点的完整 sigma 身份均为手证。没有新增数学执行。本文只排除把所显示的单个变换向量未经投影当成固定有限未分歧 canonical 族的步骤；不排除某个另行证明的有限求和消去全部新字。

## 1. 原六维整框架与实际有理对应

使用 [R1040](../results/R1040-new-e3969-whole-companion-frame-and-sixth-degree-carry.md) §10 的原六行：
$$
\begin{aligned}
Y&=(7,4+\omega,3-\omega,3\delta,2\delta,2\delta),\\
H&=(1,-1,-1,0,0,0),\\
K&=(-1,\omega,\omega^2,\delta,0,0),\\
J&=(0,0,0,0,1,-1),\\
A&=(1,-\omega^2,-\omega,0,-\delta,-\delta),\\
N&=(0,-2,2,2,-1,-1).
\end{aligned}
\tag{1}
$$
其 Hermitian Gram 为 $\operatorname{diag}(126,3,6,2,9,14)$，行列式的范数为 $756^2$。因此在任何 $p>1296$ 的原普通分裂处，这六行及逆矩阵都保持原整格；特别 $(Y,K)$ 与其余四轴给真正的整直和坐标，而非只在 $K$ 上的一组抽象基。

原普通射线仍记
$$
\kappa=\pi_0/\bar\pi_0,\qquad
\kappa\bar\kappa=1,\qquad v_{\mathfrak p}(\kappa)=1.
$$
固定非零有理整数 $c$，置
$$
D_c=1+21c^2,\quad
a=\frac{1-21c^2}{D_c},\qquad
b_n=\frac{2c}{D_c}\kappa^n,\qquad n\ge1.
\tag{2}
$$
本节排除 $2cD_c(1-21c^2)$ 的素因子。因此 $a$、$2c/D_c$ 在当前 p 都是单位，且
$$
v_{\mathfrak p}(b_n)=n,\qquad
v_{\mathfrak p}(\bar b_n)=-n.
$$
完全明确的选择是 $c=1$，此时 $a=-10/11$、$b_n=\kappa^n/11$；当前 $p>1296$ 已支付这些单位条件。

在原 $(Y,K)$ 行坐标上取
$$
g_n=
\begin{pmatrix}
a&21b_n\\-\bar b_n&a
\end{pmatrix},
\tag{3}
$$
在其余四行上取恒等。直接计算
$$
a^2+21b_n\bar b_n=1,\qquad
g_n\begin{pmatrix}126&0\\0&6\end{pmatrix}
\bar g_n^{\,t}=
\begin{pmatrix}126&0\\0&6\end{pmatrix},
\qquad \det g_n=1.
\tag{4}
$$
因此这是 $K$ 上真实的 Hermitian 等距对应。它将原观察送到
$$
Y_n=aY+21b_nK,\qquad
a^{-1}Y_n=Y+t_nK,\quad
t_n=\frac{42c}{1-21c^2}\kappa^n\longrightarrow0
\quad(\mathfrak p\text{ 进}).
\tag{5}
$$

矩阵 (3) 一般有固定的 $D_c$ 分母，不能称为处处整的自同构或只含 p 次数的整同源。将固定分母、(1) 的固定逆分母及相应 $\pi_0^n,\bar\pi_0^n$ 分母一起清掉，得到原 $E^6$ 上真正的有限同源对应。其远离 p 的成本仅含一份固定有限集合。

若要在指定原坏处保持原 Schwartz，而不只保持一个固定有限轨道，可先取 c 被所需固定模数充分整除，再将原 ray 细化到对应 $\kappa$ 的单位类；(2) 在这些处趋于恒等，故确可保持其实际开稳定子。新固定分母的来源必须另列。本文的 p 处结论不以这项细化为假设。

## 2. 原 split p Schwartz 的完整稳定子

在好分裂 p，原六 sigma 的有限 Schwartz 是六个原球的张量。由 (1) 的整可逆性，它在所写六坐标中仍为
$\mathbf1_{\mathbf Z_p^6}$。在 split unitary Schrödinger 模型，(3) 的 determinant 为一，故原 Weil 作用就是变量变换，不产生额外绝对值或未付 unit splitting。采用反变规范，记变换向量
$$
\phi_n(x)=\mathbf1_{\mathbf Z_p^6}(g_nx).
\tag{6}
$$
换成正变规范只把 $g_n$ 改成逆，以下准确稳定子不变。

令 $u\in\mathbf Z_p^\times$，原 Y 的紧环面在该块上为
$t_u=\operatorname{diag}(u,1)$，在其余四轴上为一。原好处分量在这些 units 上未分歧，所以不存在一个可改变支撑的附加相位。完整共轭是
$$
g_nt_ug_n^{-1}=
\begin{pmatrix}
a^2u+21b_n\bar b_n&
21ab_n(1-u)\\
a\bar b_n(1-u)&
21b_n\bar b_nu+a^2
\end{pmatrix},
\qquad \det(g_nt_ug_n^{-1})=u .
\tag{7}
$$
两对角项永远整，右上项永远整；左下项的估值准确为
$$
-n+v_p(1-u).
$$
因 determinant 是单位，一个这样的矩阵保持整格当且仅当其全部条目整。这支付了正反两个包含，而非只给一个充分条件。因此
$$
\boxed{\operatorname{Stab}_{\mathbf Z_p^\times}(\phi_n)
=1+p^n\mathbf Z_p.}
\tag{8}
$$

这一步使用的是同一个原好处球和真实 (3)，不是从复范数不变推断的局部不变性。

## 3. 至少一个准确导子 p^n 的新字

由 (8)，$\phi_n$ 的紧环面轨道通过有限群
$$
\mathbf Z_p^\times/(1+p^n\mathbf Z_p)
$$
作用。对其全部角色采用实际有限投影
$$
e_\vartheta\phi_n=
\frac1{\#G_n}\sum_{u\in G_n}
 \vartheta(u)^{-1}t_u\phi_n .
\tag{9}
$$
在特征零中，这些幂等完整分解原向量。

对 $n\ge2$，如果所有导子恰为 $p^n$ 的 (9) 都为零，则每个留下的角色在 $1+p^{n-1}\mathbf Z_p$ 上平凡，于是该群固定 $\phi_n$，与 (8) 矛盾。对 $n=1$，若全部非平凡 tame 投影为零，则整个 $\mathbf Z_p^\times$ 固定 $\phi_1$，同样矛盾。故
$$
\boxed{\text{每个 }n\ge1\text{ 都有至少一条非零 }
e_\vartheta\phi_n\text{ 的导子准确为 }p^n.}
\tag{10}
$$

原固定有限曲线族在充分大的好 p 处，其指定 CM canonical 分量是 p 处未分歧的。原 p-old 向量仍在该未分歧角色的局部表示中；不能把 (10) 中另一个实际紧环面角色改称原未分歧字。因而 (5) 的整个角来源不能仅凭 Hermitian 等距、坏处不变或固定复范数就继承这个固定族的中央零。

(10) 的非零严格发生在所显示的原 Schwartz 向量及紧环面投影层面；尚未断言这些分量经后续 theta 求和、伴随平均或完整中央积分后非零。若这些后继操作消去全部新字，必须给出它们在同一原测试上的实际身份。

可以对 (6) 取未分歧投影，也可以求某个有限 Hecke 组合。但必须重新写其真实测试：被删去的 (9) 与原 unit cut、Mellin 导数和 (5) 的角差同时在场。本文没有证明它们的中央值非零，也没有证明任意有限求和都保留新字；所缺的确切步骤是一个使全部这些新字消失且保留所需角导数的实际恒等式。

## 4. 一个完全固定的角端点及其 CM 质量边界

原 (1) 还给无需 p 变化的准确身份
$$
Y+K=2\delta(-\delta,-\omega,-\omega^2,2,1,1).
\tag{11}
$$
括号内行的范数为11。令 $u=2\delta z$，使用原
$\sigma(\delta u)=\delta x(u)\sigma(u)^3$、
$\sigma(2u)=-2y(u)\sigma(u)^4$ 及
$\sigma(\zeta u)=\zeta\sigma(u)$，逐项相乘得到
$$
\boxed{
\prod_{j=1}^6\sigma((Y+K)_jz)
=2\delta\,x(u)y(u)\sigma(u)^{11}.}
\tag{12}
$$
这包括原全部半特征和绝对符号；若返回原 $\rho=-\nu_\sigma^{\otimes6}/84$，还须保这个 $-1/84$。

标准 odd degree11 的 principal 空间准确为
$$
\operatorname{span}_K\{xy\sigma^{11},\,x^4y\sigma^{11}\}.
\tag{13}
$$
前者从 $-z^6$ 起，后者质量为−1。因此质量核一维，但不能据此把它叫作一个 CM Hecke 本征来源。

以下直接在原 theta 线性化中检验这一点。取
$\gamma=3+\omega$，原完整算子为
$$
\mathcal N_\gamma=\gamma^{-1}[\gamma]_*[\bar\gamma]^*.
$$
其质量是在同一全七点纤维上对 $[\bar\gamma]^*(xy\sigma^{11})$ 作准确 theta trace。O 项为零。其余六个点是一个 $\mu_6$ 轨道。

这里六项相等并非忽略相位：原 geometric CM 作用 $\mathcal C_\zeta$ 与 canonical Weyl lift 满足
$$
\mathcal C_\zeta\mathcal T_U\mathcal C_\zeta^{-1}
=\mathcal T_{\zeta U},
$$
输入 $[\bar\gamma]^*(xy\sigma^{11})$ 的完整 principal 角色是一，原点质量泛函的角色也是一。故同一 trace 中的六项连同其 Gaussian、半周期和 CM 标量确实相等。每项非零：$\bar\gamma$ 在 $\ker\gamma$ 上可逆，其非零像是七挠点，不在二挠、$\ker\delta$ 或 O；原 sigma、x、y 在该点均非零，Weyl 指数也是非零数。于是
$$
\boxed{
m_0(\mathcal N_\gamma(xy\sigma^{11}))\ne0,\qquad
m_0(xy\sigma^{11})=0.}
\tag{14}
$$
所以 (12) 的 norm11 内层本身不是任一 $\mathcal N_\gamma$ 本征线。该固定角端点确为一个真实小来源，却没有因此增加一条已授权的 rank-two canonical 零。

## 依赖与继续使用的范围

- R1040 §10：原六维整框架及全部 theta 规范。
- R290、R316：原全局加性角色、好处分裂球、奇 sigma 和 Weil 规范。
- R816 §8：原 full-fiber pull/trace 及完整 theta carrier；本文沿用同一算子定义，不重算其 degree66 矩阵。
- R1042、R1044：原三 canonical 观察、共同 carry 和尚需保留的完整补域。

本笔记的输出是 (8)–(10) 这一准确投影成本及 (12)–(14) 这个固定来源边界。后继应检验真正的有限 Hecke/角求和是否在保留原中央测试时消掉新字，而非把 (5) 的无限角族逐个赋零。
