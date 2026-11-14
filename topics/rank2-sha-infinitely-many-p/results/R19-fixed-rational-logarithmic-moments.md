# R19. 固定有理函数的精确对数矩及椭圆单位比较

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes。

本结果将 R6 的 CLS 特值矩与 R16 的有限层椭圆单位，都连接到同一个固定有理函数 $\Phi$。两种测试仍是不同的特化：本结果没有将有限层单位深度直接等同于一个高阶导数的赋值。

## 1. 固定函数及其对数矩

沿用 [R18](R18-rational-layer-and-fixed-fermat-quotient.md) 的固定域 $M/K$ 及 $\alpha=v/u$，定义
$$
\Phi(t)=
\frac{\operatorname N_{M/K}(1+\alpha t)}
{\operatorname N_{M/K}(1-\alpha t)}\in K(t).
\tag{1}
$$
将其与 $t=-x/y$ 复合，亦记所得 $E$ 上的有理函数为 $\Phi$。它满足
$$
\Phi(O)=1,\qquad \Phi(-P)=\Phi(P)^{-1}.
\tag{2}
$$
R18 的有理化公式直接给出
$$
\frac{d}{dt}\log\Phi(t)
=\operatorname{Tr}_{M/K}\left(
\frac{\alpha}{1+\alpha t}+\frac{\alpha}{1-\alpha t}
\right)=2R(t).
\tag{3}
$$
记 $\delta=d/dz=s(t)d/dt$，其中 $dz=dt/s(t)$，并沿用 R17 的 $S(x)$。由于 $sR=S(x)$，
$$
\delta\log\Phi=2S(x),
\qquad
\delta^2\log\Phi=2g_o.
\tag{4}
$$
在 $O$ 附近取常数项为零的形式对数；则对所有 $n\ge0$，
$$
\boxed{\quad
\delta^{2n+3}\log\Phi(O)=4a_n.
\quad}
\tag{5}
$$
证明只需在式 (4) 上再微分 $2n+1$ 次，并用 R13 的 $g_o^{(2n+1)}(0)=2a_n$。此外 $S(\infty)=0$，所以 $\delta\log\Phi(O)=0$；式 (2) 表明所有偶阶对数导数为零。

对目标的 good split $p$，按 corrected CLS 公式
$$
c_p^+(E)=-\frac{2a_{(p-3)/2}}{f^p(p-1)!},
\qquad f=34(1+i),
$$
因此
$$
\boxed{\quad
\delta^p\log\Phi(O)
=-2f^p(p-1)!\,c_p^+(E).
\quad}
\tag{6}
$$
这保留了全部阶乘、$2$ 倍与 $f^p$ 缩放；没有未定常数。

## 2. $\Phi$ 的零极点

令
$$
D_+=\sum_{\sigma\in\operatorname{Gal}(F/K)}[P_f^\sigma],
\qquad
D_-=\sum_{\sigma\in\operatorname{Gal}(F/K)}[-P_f^\sigma].
$$
R13 证明这两个点集互不相交。对每个 $\alpha$ 的共轭，其对应的 $t$ 值 $-1/\alpha$ 的两个逆像正好是 $P_f^\sigma$ 及 $\tau P_f^\sigma$，其中 $\tau P=T-P$，$T=(0,0)$。这些逆像不是 $t:E\to\mathbb P^1$ 的分歧点：分歧条件为 $T-P=P$，亦即 $2P=T$，而本处 $P$ 有非平凡的 $17$-初级 torsion 部分。

因此每个 $1+\alpha t$ 给出上述两个简单零点；$1-\alpha t$ 同样在它们的负点给出两个简单零点。在 $t$ 的极点处，分子和分母的次数相同、首项非零，商没有零极点。故
$$
\boxed{\quad \operatorname{div}\Phi=D_+-D_-.\quad}
\tag{7}
$$

## 3. 与 Rubin 固定 $\Lambda_{(7)}$ 的确切函数恒等式

取与 R16 相同的辅助理想 $\mathfrak a=(7)$，故
$$
N\mathfrak a=49,\qquad \lambda=\psi(\mathfrak a)=-7.
$$
取 $S=P_f=\xi(\Omega_\infty/f)$，并使用 Rubin 的
$$
\Lambda(P)=\prod_{\sigma\in\operatorname{Gal}(F/K)}
\Theta_{E,\mathfrak a}(P+P_f^\sigma).
$$
所用外部输入是 Rubin 讲义 *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer* 的 Lemma 7.5：
$$
\operatorname{div}\Theta_{E,\mathfrak a}
=12N\mathfrak a[O]-12\sum_{Q\in E[\mathfrak a]}[Q].
\tag{8}
$$
其 $\Lambda$ 定义见 §7.3、Proposition 7.8；[原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。这里的 $F=K(E_f)$ 正是所用 ray class field，R16 已核对这个识别。

CM reciprocity 表明 $[\lambda]=[-7]$ 置换 $P_f$ 的 Galois orbit。因此，平移式 (8) 后求和得
$$
\operatorname{div}\Lambda
=12\cdot49D_- -12[\lambda]^*D_-.
\tag{9}
$$
具体地，$[\lambda]$ 在点 $-P_f^\sigma$ 上方的逆像就是 $-P_f^{\sigma'}+E[\mathfrak a]$，而 $\sigma'$ 也遍历整个 orbit，这说明式 (9) 的 pullback 未漏乘重数或单位数。

将式 (9) 与其 $[-1]$-pullback 相减，利用式 (7)，得到
$$
\begin{aligned}
\operatorname{div}\frac{\Lambda(P)}{\Lambda(-P)}
&=12\left([\lambda]^*(D_+-D_-)-49(D_+-D_-)\right)\\
&=\operatorname{div}\left(
\frac{\Phi([\lambda]P)}{\Phi(P)^{49}}
\right)^{12}.
\end{aligned}
$$
两边的商是 $E$ 上的常数。$P=O$ 时两边都为 $1$：$\Phi(O)=1$，而 $\Lambda(O)$ 有限非零，因为所有 $P_f^\sigma$ 都不在 $E[\mathfrak a]$ 中。故常数恰为 $1$，即
$$
\boxed{\quad
\frac{\Lambda(P)}{\Lambda(-P)}
=\left(\frac{\Phi([-7]P)}{\Phi(P)^{49}}\right)^{12}.
\quad}
\tag{10}
$$
这是有理函数恒等式。证明不依赖高阶特值的预期比较，也不把函数相差的常数忽略为“不重要的单位”。

## 4. 对数矩再次核对 $f$ 的正规化

对式 (10) 在 $O$ 取形式对数并微分。对奇数 $m\ge1$，左侧为 $2\delta^m\log\Lambda(O)$，而 $[-7]$ 对不变微分的缩放是 $-7$。所以
$$
\boxed{\quad
\delta^m\log\Lambda(O)
=-6\bigl(49-(-7)^m\bigr)\delta^m\log\Phi(O).
\quad}
\tag{11}
$$
对 $m\ge3$ 为奇数，结合式 (5) 和 corrected CLS trace 公式，得到
$$
\delta^m\log\Lambda(O)
=12(m-1)!\,f^m\bigl(49-(-7)^m\bigr)
\Omega_\infty^{-m}L_{\mathfrak f}(\overline\psi^{m},m).
\tag{12}
$$
这与 Rubin Theorem 7.13 在固定平移 $S=\xi(\Omega_\infty/f)$ 上求和后的公式一致：一般符号为 $12(-1)^{m-1}$，对奇 $m$ 即为正号。$f^m$ 来自原始平移点 $\Omega_\infty/f$，不能删去。

在 $m=1$ 时，R18 已证明 $L(E,1)=0$ 及 $\operatorname{Tr}_{M/K}\alpha=0$，所以式 (11) 两边都为零。这只核对低阶项，并未假设任何秩 $2$ leading term 已非零。

## 5. 有限局部单位深度完全相同

取 R16 的 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，以及
$$
L_p=K(E[\mathfrak p]),\quad P_\pi\in E[\mathfrak p]\setminus\{O\},
\quad F_p=(L_p)_{\mathfrak P},\quad\rho=t(P_\pi).
$$
令 $\chi$ 为 $G_p=\operatorname{Gal}(L_p/K)$ 在 $E[\mathfrak p]$ 上的字符，$\widetilde\chi$ 为其 Teichmüller 提升，$e_\chi$ 为 R16 使用的幂等元。用加法记号表示局部 pro-$p$ 单位模。

R18 已证明 $\alpha$ 在所有 $p\nmid34$ 的上方素位都是单位，而 $v_{F_p}(\rho)>0$。因而 $1\pm\alpha\rho$ 为单位，取固定有限范数后
$$
\varepsilon_p:=\Phi(P_\pi)\in1+\rho\mathcal O_{F_p}.
\tag{13}
$$
这里仅需局部单位性；不预先声称 $\Phi(P_\pi)$ 为全局单位。

记 $\eta_p=\Lambda(P_\pi)$。由于 $\Phi$ 定义在 $K$ 上，$\Phi([-7]P_\pi)$ 等于 $\sigma_7\varepsilon_p$，其中 $\sigma_7$ 在 $E[\mathfrak p]$ 上作用为 $-7$。类似地，$\Lambda(-P_\pi)=\sigma_{-1}\eta_p$。式 (10) 因此给出
$$
(1-\sigma_{-1})\eta_p
=12(\sigma_7-49)\varepsilon_p.
$$
作用 $e_\chi$，注意 $\widetilde\chi(\sigma_{-1})=-1$，得到
$$
\boxed{\quad
e_\chi\eta_p
=6\bigl(\widetilde\chi(\sigma_7)-49\bigr)e_\chi\varepsilon_p.
\quad}
\tag{14}
$$
这个系数模 $p$ 为
$$
6(-7-49)=-336.
$$
对上述素数它是 $\mathbb Z_p$-单位。因此若以 R16 的同一个生成元
$$
u_p=e_\chi(1+\rho)
$$
衡量深度，$e_\chi\Lambda(P_\pi)$ 与 $e_\chi\Phi(P_\pi)$ 的深度完全相同，包括两者为零时的无穷深度情形。

特别地，R16 的判据现在可原样改写为：若
$$
e_\chi\Phi(P_\pi)\notin p^4\mathscr U_p,
$$
则 $\Sha(E/\mathbb Q)[p^\infty]=0$；而已证秩 $2$ 强制该投影属于 $p^2\mathscr U_p$。

### 5.1 同一个值事实上也是全局单位

上面的局部论证之后，可以无额外局部计算地证明 $\varepsilon_p=\Phi(P_\pi)$ 是全局单位。它非零且有限，因为 $P_\pi$ 不在式 (7) 的零极点中。令 $J=(\varepsilon_p)$ 为 $L_p$ 的主分式理想。式 (10) 的左边是两个全局单位之比，因此在无挠的分式理想群中有
$$
12(\sigma_7-49)J=0,\qquad \sigma_7J=49J
$$
（这里理想群采用加法记号）。若 $d$ 为 $\sigma_7$ 的有限阶，反复作用给出 $J=49^dJ$，无挠性遂迫使 $J=0$，即 $(\varepsilon_p)=\mathcal O_{L_p}$。

故式 (14) 也成立于全局单位的 $\chi$ 格。其系数是 $p$-进单位，所以 $e_\chi\Phi(P_\pi)$ 与 $e_\chi\Lambda(P_\pi)$ 的全局深度 $m_p$ 同样相等；局部深度 $\nu_p$ 的相等已在上一节证明。这个推论不提供任何跨素数的深度上界。

## 6. 此次比较已经做到了哪一步

固定函数 $\Phi$ 的第 $p$ 个不变对数矩，由式 (6) 准确给出 CLS 特值；同一个函数在 $\mathfrak p$-division 点的 $\chi$ 投影，由式 (14) 准确给出有限层椭圆单位的局部深度。这两个比较均无未定非零常数，且有限层系数是明确的单位。

不过，$e_\chi\Phi(P_\pi)$ 的展开原则上包含整个相应字符类的项。不能仅凭形式相似，就把其深度认作 $\delta^p\log\Phi(O)$ 的赋值，或未经误差估计只保留一个项。跨 $p$ 的最后任务仍是证明这两种适用的非消失 / 深度条件之一，对无穷多个 $p$ 成立。
