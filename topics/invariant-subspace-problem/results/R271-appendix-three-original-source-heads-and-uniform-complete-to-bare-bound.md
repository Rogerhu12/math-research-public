# R271 附录：整个前三原源头旗的完整右费／裸右费一致比较

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 对原真实 $A_m$、完整原尾、全部合法孔窗及全部源尾核阶，整个 $\ker A_m^2$ 和 $\ker A_m^3$ 源旗都有与 $m,q$ 无关的完整右费／裸右费比较。前三头的常数使用原固定首三头块的一个已明确支付的有限逆；它可以很大，但不随 $m,q$ 增长。没有给纯 $S_H^\dagger$ 费用相同上界，也不声称真正裸最小链的高返回为零。

这是整类原源结论，既不限于 primitive 尾源，也不限于前稿的 $D^2(D^*)^2f$ 单 jet 构造。它可进入原真实两费度量的好顶部投影；投影后的约束仍为该度量的正交条件，不是将前三个源坐标置零。普通 ISP、原 $N=M$ 及一般高返回问题仍为 OPEN。

依赖：[原真幂底项及两道桥](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)、[单 jet 首行 Schur](R271-appendix-single-jet-head-schur-and-pure-versus-completed-high-energy.md)、[真实两费好顶部投影](R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md)。与[两物理头的真正两下降度量](R239-appendix-two-physical-heads-and-true-two-descent-metrics.md)不同，下面直接比较同一个原源的两个真正右最小费用，不运输或交换平坦源中的算子。

## 1. 原源旗及主结论

固定原 $m\ge5$、$d=2^m$、合法 $q$，令 $p=q+1$、$A=A_m$、$D=D_m$，
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q},\qquad
E_{h,q}=\ker D^h\cap\mathcal H_q,
$$
$$
\mathscr E_{k,q}
=\mathscr R_q\cap(\ker A^k\otimes\mathcal H_q)
=\bigoplus_{i=0}^{k-1}e_iE_{d-i-1,q}
\quad(1\le k\le3).
\tag{1.1}
$$
原头是 regular 严格降头矩阵，故 $\ker A^k$ 恰为前 $k$ 个物理头。
记 $\alpha(r)$、$\lambda(r)$ 为同一个源的真正裸右、完整右最小费用。

原嵌套头满足 $Ae_1=e_0$，且其首三头块不随 $m\ge2$ 改变。令
$$
J=\left(A|_{\operatorname{span}(e_1,e_2)}:
\operatorname{span}(e_1,e_2)\longrightarrow
\operatorname{span}(e_0,e_1)\right)^{-1},
\qquad \kappa=\|J\|\ge1.
\tag{1.2}
$$
此 $J$ 只作用于显示的二维原头空间，并非整个 $A$ 的逆。
若 $\theta=\langle Ae_2,e_0\rangle$、$\tau=\langle Ae_2,e_1\rangle\ne0$，则
$$
J(z_0e_0+z_1e_1)
=(z_0-\theta\tau^{-1}z_1)e_1+\tau^{-1}z_1e_2.
\tag{1.3}
$$
$\theta,\tau$ 是原固定低头系数，故 $\kappa$ 与 $m,q$ 无关。
本稿不声称当另外改变 $\tau$ 使其趋零时常数仍一致。

令
$$
S_m=\sum_{\ell\ge m}(\ell+1)^{-4}\le\frac1{3m^3}.
$$
主结论是
$$
\boxed{\lambda(r)=\alpha(r)\qquad(r\in\mathscr E_{1,q}),}
\tag{1.4}
$$
$$
\boxed{
\lambda(r)^2
\le\bigl(\|A_m^*e_0\|^2+S_m\bigr)\alpha(r)^2
<37\,\alpha(r)^2
\qquad(r\in\mathscr E_{2,q}),
}
\tag{1.5}
$$
以及
$$
\boxed{
\lambda(r)^2\le
\bigl(\|A_m\|+\sqrt{2S_m}\bigr)^2
\bigl[1+(1+S_m)\kappa^2\bigr]\alpha(r)^2
<169\kappa^2\alpha(r)^2
\quad(r\in\mathscr E_{3,q}).
}
\tag{1.6}
$$
这里用原既有 $\|A_m\|\le6$。因而可统一取
$C_2=7$、$C_3=13\kappa$，得到 $\lambda\le C_k\alpha$。
所有同一旗中的任意线性组合和全部合法尾核阶都包括在内。

## 2. 只需支付前两个真实下降块

沿原桥稿，在 $K_p=\ker D\cap\mathcal H_p$ 上置
$$
J_j=(D^j:\mathcal H_{p+j}\to\mathcal H_p)^\dagger|_{K_p},
\qquad H_j=J_j^*J_j,\quad H_0=I.
$$
最低深度的原等距坐标为
$$
(\mathcal I\xi)_{j+1}=(-1)^jJ_jH_j^{-1/2}\xi_j,
$$
$$
\xi_j\in
\operatorname{span}(e_0,\ldots,e_{d-j-1})\otimes K_p,
\qquad 0\le j<d.
\tag{2.1}
$$
出生一算子准确为
$$
(\mathcal G\xi)_t=A\xi_{t-1}-T_t\xi_t,\qquad
T_t=H_{t-1}^{1/2}H_t^{-1/2},\quad1\le t<d.
\tag{2.2}
$$
这些乘法次序不交换。

原交换子 $[D,D^*]=S_mI-2W_m\preceq S_mI$ 给
$$
\|D|_{\ker D^h}\|^2\le(h-1)S_m.
\tag{2.3}
$$
为完整说明所用的估计，可作直接归纳：$D=0$ 在 $\ker D$ 上。
若 (2.3) 对 $h-1$ 成立，则对 $z\in\ker D^{h-1}$，
$$
\|D^*z\|^2\le\|Dz\|^2+S_m\|z\|^2
\le(h-1)S_m\|z\|^2.
$$
对任意 $x\in\ker D^h$，其 $Dx$ 属于 $\ker D^{h-1}$；
在该输出空间对偶即得 (2.3)。这没有假定 $D^*$ 保短核旗。

$J_jH_j^{-1/2}$ 是 $K_p$ 到真实
$W_{j+1,p+j}=E_{j+1,p+j}\ominus E_{j,p+j}$ 的等距满射。
两者之间的第一下降压缩恰为 $T_t$，所以
$$
\|T_t\|\le\|D|_{\ker D^{t+1}}\|\le\sqrt{tS_m}.
$$
特别
$$
\boxed{\|H_1^{-1/2}\|\le\sqrt{S_m},\qquad
\|H_1^{1/2}H_2^{-1/2}\|\le\sqrt{2S_m}.}
\tag{2.4}
$$
这只是对原真实下降块的范数估计；没有把两个尾 Gram 对角化或视为可交换。

## 3. 一个零返回 lift 如何支付真正完整费用

对同一个 $r\in\mathscr R_q$，原桥稿给
$$
b_{j+1}(r)=(-1)^j
(D^{j+1}:\mathcal H_{q+j+1}\to\mathcal H_q)^\dagger A^jr,
$$
$$
\alpha(r)^2=\|b(r)\|^2+\|\mathcal G^\dagger\zeta(r)\|^2.
\tag{3.1}
$$
$b(r)$ 与整个最低深度空间 $\operatorname{Ran}\mathcal I$ 正交。
它的内部残量只有出生一，准确为 $\mathcal O\zeta(r)$；其高返回为零。
$\mathcal I\xi$ 的出生一和高输出分别为
$\mathcal O\mathcal G\xi$ 与 $\mathcal R\xi$。
第二桥 $\mathcal R$ 只读取 $\xi_j$ 的 $j\ge2$ 部分。

因此，若在原坐标域中找到
$$
\mathcal G\xi^0=\zeta(r),\qquad \mathcal R\xi^0=0,
\tag{3.2}
$$
则
$$
\boxed{c=b(r)-\mathcal I\xi^0}
\tag{3.3}
$$
是一条同源的原完整合法右链。源端不变，因为
$\mathcal I\xi^0$ 的首段 primitive；全部尾核旗、头旗和末段封口都由
(2.1) 及原桥坐标保持。两个内部输出由 (3.2) 完全相消。

正交性给直接可行上界
$$
\boxed{\lambda(r)^2\le\|b(r)\|^2+\|\xi^0\|^2.}
\tag{3.4}
$$
记 $\Pi=\mathcal G^\dagger\mathcal G$，则
$\Pi\xi^0=\mathcal G^\dagger\zeta(r)$。从 (3.1)、(3.4) 还得到
$$
\boxed{
0\le E_H(r):=\lambda(r)^2-\alpha(r)^2
\le\|(I-\Pi)\xi^0\|^2.
}
\tag{3.5}
$$
同样可以从原
$H_2^\circ=S_HS_H^*+\mathcal R(I-\Pi)\mathcal R^*$
的最小原像定义得到 (3.5)，因为
$\mathcal R\mathcal G^\dagger\zeta=-\mathcal R(I-\Pi)\xi^0$。

(3.2) 不要求真正最小 lift 本身零返回；事实上正交投影 $\Pi$
通常会离开 $\xi^0$ 的最低两层支撑。故 (3.5) 不是纯高费用的上界。

## 4. 所有前两头源：只需一个单位原头逆

同源 jet 的准确公式是
$$
\zeta_t(r)=t(t+1)H_{t-1}^{-1/2}A^tC_0^*
P_{K_q}[D^{t+1}(D^*)^{t+1}]^{-1}r,
\tag{4.1}
$$
其中 $C_0=D_3|_{K_{q+1}}$，所有纯尾算子与 $A$ 交换。
因此 $r\in\mathscr E_{k,q}$ 时
$$
\zeta_t(r)=0\ (t\ge k),\qquad
\zeta_t(r)\in\ker A^{k-t}\otimes K_p\ (t<k).
\tag{4.2}
$$
没有独立改变任何 jet 的来源。

若 $k=1$，$\zeta=0$，所以 $b(r)$ 自己就是完整最小链；
(1.4) 随即成立。

若 $k=2$，写 $\zeta_1=e_0z_1$。取
$$
\xi^0_0=e_1z_1,\qquad \xi^0_j=0\quad(j\ge1).
\tag{4.3}
$$
由 $Ae_1=e_0$，这是 (3.2) 的原合法 lift，且
$\|\xi^0\|=\|z_1\|$。

令 $\eta=\mathcal G^\dagger\zeta$。只读取
$(\mathcal G\eta)_1$ 的第零头，得
$$
z_1=(\langle e_0,A\,\cdot\rangle\otimes I)\eta_0
-H_1^{-1/2}(\langle e_0,\,\cdot\rangle\otimes I)\eta_1.
$$
两个输入分量正交，故由 (2.4)，
$$
\|z_1\|^2
\le\bigl(\|A^*e_0\|^2+S_m\bigr)\|\eta\|^2.
\tag{4.4}
$$
因为 $\|A^*e_0\|\ge1$，将 (4.4) 代入 (3.4)、(3.1) 即得 (1.5)。
特别，新高能量还满足
$$
E_H(r)\le
\bigl(\|A^*e_0\|^2+S_m-1\bigr)
\|\mathcal G^\dagger\zeta(r)\|^2.
\tag{4.5}
$$
原首行的全部长跳都保留在 $\|A^*e_0\|$ 内，并未只读某个 carry。

## 5. 所有前三头源：两个最低层足够

现在 $r\in\mathscr E_{3,q}$。由 (4.2)，只有
$$
\zeta_1\in\operatorname{span}(e_0,e_1)\otimes K_p,\qquad
\zeta_2=e_0z_2,\qquad
\zeta_t=0\quad(t\ge3).
$$
用 (1.2) 的原固定二维逆，定义
$$
\boxed{
\xi^0_1=e_1z_2,\qquad
\xi^0_0=J\bigl(\zeta_1+H_1^{-1/2}\xi^0_1\bigr),\qquad
\xi^0_j=0\quad(j\ge2).
}
\tag{5.1}
$$
$\xi^0_0$ 仅用原头 $e_1,e_2$，$\xi^0_1$ 仅用 $e_1$，
故全部逐段头旗合法。逐式代入得到
$$
A\xi^0_0-H_1^{-1/2}\xi^0_1=\zeta_1,\qquad
A\xi^0_1=\zeta_2,
$$
其余行零。又 $\mathcal R$ 只读 $j\ge2$，故 (3.2) 完全成立。

由 (2.4) 和二维 Cauchy--Schwarz，
$$
\begin{aligned}
\|\xi^0\|^2
&\le \kappa^2
\bigl(\|\zeta_1\|+\sqrt{S_m}\|\zeta_2\|\bigr)^2
+\|\zeta_2\|^2\\
&\le[1+(1+S_m)\kappa^2]
(\|\zeta_1\|^2+\|\zeta_2\|^2).
\end{aligned}
\tag{5.2}
$$
仍令 $\eta=\mathcal G^\dagger\zeta$。读取 $\mathcal G$ 前两行，
将头项与真实下降项分开作一次三角不等式：
$$
\begin{aligned}
(\|\zeta_1\|^2+\|\zeta_2\|^2)^{1/2}
&=\|(A\eta_0-T_1\eta_1,\ A\eta_1-T_2\eta_2)\|\\
&\le(\|A\|+\max(\|T_1\|,\|T_2\|))\|\eta\|\\
&\le(\|A\|+\sqrt{2S_m})\|\eta\|.
\end{aligned}
\tag{5.3}
$$
于是 (5.2)、(5.3)、(3.4)、(3.1) 给 (1.6) 第一式；
其系数至少为 $1$，因此也支付 $\|b(r)\|^2$。

为核实最后的数值常数，$m\ge5$ 时
$\|A\|+\sqrt{2S_m}<7$、$S_m<1$、$\kappa\ge1$，从而
$$
(\|A\|+\sqrt{2S_m})^2[1+(1+S_m)\kappa^2]
<49(1+2\kappa^2)\le147\kappa^2<169\kappa^2.
$$
这完整支付了固定低头逆的费用，没有利用尾源的额外结构。

## 6. 原两费度量上的闭旗删除

在同一个原源空间写
$$
L=J_{\rm left}^{-1},\qquad B=J_{\rm bare}^{-1},\qquad
G=J_{\rm right},
$$
$$
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
\lambda(r)^2=\langle G^{-1}r,r\rangle,
$$
$$
\lambda_{\rm flat}(r)^2=\langle GLr,Lr\rangle,\qquad
\Xi(r)^2=\langle M_2r,r\rangle,\quad M_2=B+LGL.
\tag{6.1}
$$
所有算子均为原真实源 Gram；不令它们交换。
同源 Cauchy--Schwarz 精确给
$$
\mu(p)^2\le\lambda(p)\lambda_{\rm flat}(p).
$$
所以在 $\mathscr E_{k,q}$，$k=2,3$，
$$
\boxed{\mu(p)^2\le\frac{C_k}{2}\Xi(p)^2.}
\tag{6.2}
$$

固定任意原闭源约束空间 $\mathscr N_q$，例如已付的真实负源图，
并令
$$
Z=\mathscr E_{k,q}\cap\mathscr N_q,\qquad
p=P_Z^{M_2}r,\qquad r'=r-p.
$$
固定窗口下各源度量有界正定，$Z$ 闭，故投影存在。
原正交投影恒等式给
$$
\boxed{
\Xi(p)^2+\Xi(r')^2=\Xi(r)^2,\qquad
\mu(p)\le\sqrt{C_k/2}\,\Xi(r),\qquad
\lambda(p)\le C_k\Xi(r).
}
\tag{6.3}
$$
若 $r\in\mathscr N_q$，则 $r'\in\mathscr N_q$，而准确余条件为
$$
\langle M_2r',z\rangle=0\qquad(z\in Z).
\tag{6.4}
$$
这不是物理前 $k$ 个头坐标为零，也不声称裸费和平坦费分别对原输入收缩。

特别，在真实两费好顶部稿的同一实际源流中，可选 $K\asymp Q/d$
个不交未来带中的顶部 $b$，使 $\Xi_b(r_b)^2\le2\varepsilon^2/K$。
在该顶部作上述一次投影，就有
$$
\boxed{
\mu_b(p)^2\le\frac{C_k\varepsilon^2}{K},\qquad
\lambda_b(p)\le\frac{\sqrt2\,C_k\varepsilon}{\sqrt K}.
}
\tag{6.5}
$$
按已证好顶部定理，从
$E_b^\dagger(r_b-p)=E_b^\dagger r_b-E_b^\dagger p$
重建所有截断，仍为同一相容源流，并支付全部 primitive 增量及 MP 反馈。
$C_2,C_3$ 固定，故渐近时 $C_k^2\le K$ 自动成立；
不需要假设未知实际尾能量具有额外衰减速率。
这里只在顶部得到 (6.4)，不将所有较低截断也强加同一正交条件。

## 7. 范围与仍未支付的费用

本稿证明的是整 $\mathscr E_{2,q}$、$\mathscr E_{3,q}$ 上同源的
$\lambda/\alpha$ 上界，以及因此得到的原 $M_2$ 闭旗删除。
它比前稿的特殊单 jet 构造包含更多尾源，但没有从中获得
$$
\|S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)\|
\lesssim\alpha(r).
$$
零返回候选与真正裸最小候选不同；允许更改低域后的新 $H_2^\circ$ 能量
和固定裸候选的纯高补全费用仍须分开。

当源进入 $\ker A^4$ 时，(4.2) 可以出现第三个 jet。
它不能再由只有 $\xi_0,\xi_1$ 的 lift 产生。
任何继续到更高固定原头旗的论证，都须真实处理 $\xi_2$ 起的第二桥
及相应高补全；本稿未声称这一步已经廉价。
