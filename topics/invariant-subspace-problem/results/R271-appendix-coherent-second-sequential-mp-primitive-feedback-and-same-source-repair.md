# R271 附录：相干列的真实二次顺次 MP、primitive 回馈与同源第二次修复

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿进一步支付前稿真正剩下的第二次 $D^\dagger$。关键是把 $(D^\dagger)^2$ 与 $(D^2)^\dagger$ 的差保留为一个准确的 primitive 回馈列，再仅对这个已识别为 primitive 的源使用原多项式逆预算。两种逆从未互换。

结果给原小阻尼同源代表 $f$ 的前两次实际修复
$q_1=D^\dagger(C+D)f$、$q_2=CD^\dagger q_1$ 的显式统一小量，包含全部最高截断项。$f-q_1+q_2$ 仍可能有残量 $Cq_2$，所以本文不声称关闭完整返回或 $N=M$。

依据：

- [原完整相干列的 Bernoulli 原像](R271-appendix-continuous-tail-coherent-columns-bernoulli-lifts-and-exact-residuals.md)，§§4、6；
- [原 primitive 一阶逆预算](R239-appendix-two-descents-third-tail-and-paid-jet-anchor.md)，§5；
- [小阻尼截断的完整一次 MP](R271-appendix-damped-small-height-complete-once-mp-residual-and-moving-head-budget.md)；
- [完整方差 Gram 和同实际来源](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)。

## 1. 完整层与真实二次相干原像

沿用原连续尾
$$
D=D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\quad
z_{\max}=(x+1)^{-4},\quad S=S_x,
\quad \omega_j=(D^*)^j\Omega,\quad
\sigma_j^2=\|\omega_j\|^2.
$$
所有孔层都使用原 Hilbert 内积。每个固定层的全层右逆已付；本文中 $D^\dagger$、$(D^2)^\dagger$ 和 $(D^\dagger)^2$ 都在其完整自然域上使用。

置
$$
Y_j=(D^2)^\dagger\omega_j,\qquad
\ell_{j,2}=\frac{\sigma_j^2}{\sigma_{j+2}},\qquad
Y_j^0=\frac{\sigma_j^2}{\sigma_{j+2}^2}\omega_{j+2}.
$$
任意完整原像 $D^2Y=\omega_j$ 均满足
$\langle Y,\omega_{j+2}\rangle=\sigma_j^2$，故 $\|Y\|\ge\ell_{j,2}$。

原同池二步 Bernoulli 候选满足
$$
D^2q_{j,2}=\omega_j-r_{j,2},\qquad
\frac{\|q_{j,2}\|}{\ell_{j,2}}
\le\left(\frac{S_x}{S_{x+j+2}}\right)^2.
$$
在原少位事件的 Chernoff 界中取参数 $\log2$，得到
$$
\|r_{j,2}\|\le
2\exp\!\left[-\frac{S_{x+j}}{2z_{\max}}\right]\sigma_j .
$$
依次使用两个已付的**完整层**右逆，其范数乘积至多
$144\,512^{2j+1}(x+j+2)^3$；这给真 $D^2$ 原像，而非宣称它是顺次 MP。又
$$
\frac{\sigma_{j+2}}{\sigma_j}
\le S_x\sqrt{(j+1)(j+2)} .
$$
因此
$$
1\le\frac{\|Y_j\|}{\ell_{j,2}}\le B_{x,j},
\tag{1.1}
$$
其中明确取
$$
\begin{aligned}
B_{x,j}={}&
\left(\frac{S_x}{S_{x+j+2}}\right)^2\\
&+288\,512^{2j+1}(x+j+2)^3S_x\sqrt{(j+1)(j+2)}
\exp\!\left[-\frac{S_{x+j}}{2z_{\max}}\right].
\end{aligned}
\tag{1.2}
$$
由于 $Y_j-Y_j^0\perp\omega_{j+2}$，
$$
\|Y_j-Y_j^0\|^2
=\|Y_j\|^2-\ell_{j,2}^2
\le(B_{x,j}^2-1)\ell_{j,2}^2 .
\tag{1.3}
$$

## 2. 顺次二次 inverse 的准确 primitive 回馈

令 $\Pi_{j+1}$ 为原 $\mathcal H_{j+1}$ 中 $\ker D$ 的正交投影，并定义
$$
z_j=\Pi_{j+1}DY_j\in\ker D,\qquad
v_j=D^\dagger\omega_j,\qquad
w_j=(D^\dagger)^2\omega_j.
$$
因为 $D(DY_j)=\omega_j$，完整最小预像条件给
$DY_j=v_j+z_j$。又 $Y_j\perp\ker D^2$，特别 $Y_j\perp\ker D$，故
$$
\boxed{w_j=Y_j-D^\dagger z_j.}
\tag{2.1}
$$
$D^\dagger z_j\in\ker D^2$，所以它与 $Y_j$ 正交；也与
$Y_j^0\in\operatorname{Ran}(D^*)^2$ 正交。因此有准确平方分解
$$
\boxed{
\|w_j-Y_j^0\|^2
=\|Y_j-Y_j^0\|^2+\|D^\dagger z_j\|^2,
\qquad
\|w_j\|^2=\ell_{j,2}^2+\|w_j-Y_j^0\|^2.
}
\tag{2.2}
$$
这一步没有以 $D^\dagger$ 与 $D$ 交换来删掉中间核。

下面只对这个明确的 $z_j\in\ker D|_{\mathcal H_{j+1}}$ 用原 primitive 界。按引用文献的输入孔数 $p-1=j+1$，即 $p=j+2$，可取
$$
\Lambda_{x,j}=512\sqrt{j+4}\,(x+j+4)^{3/2},
\qquad
\|D^\dagger z_j\|\le\Lambda_{x,j}\|z_j\|.
\tag{2.3}
$$
特别索引中的 $j+4$ 保留原右逆输出层，未错用一般全层的多项式逆。

对任意 $u\in\mathcal H_n$，逐坐标 Cauchy 给
$\|Du\|^2\le nS_x\|u\|^2$。另一方面，若
$\mathcal W=\sum_{i\ge x}b_i^2n_i$，则
$$
D\omega_{j+2}=(j+2)(S_x-\mathcal W)\omega_{j+1},
\qquad \Pi_{j+1}\omega_{j+1}=0,
$$
且 $\|\mathcal W|_{\mathcal H_{j+1}}\|\le(j+1)z_{\max}$。所以
$$
\begin{aligned}
\|z_j\|^2\le 2\ell_{j,2}^2\bigg[
&(j+2)S_x(B_{x,j}^2-1)\\
&+\frac{(j+2)(j+1)^2z_{\max}^2}{S_{x+j+1}}
\bigg].
\end{aligned}
\tag{2.4}
$$
第二项用
$\sigma_{j+2}^2/\sigma_{j+1}^2\ge(j+2)S_{x+j+1}$。

定义明确非负数
$$
\begin{aligned}
U_{x,j}:={}&B_{x,j}^2-1\\
&+2\Lambda_{x,j}^2\left[
(j+2)S_x(B_{x,j}^2-1)
+\frac{(j+2)(j+1)^2z_{\max}^2}{S_{x+j+1}}
\right].
\end{aligned}
\tag{2.5}
$$
合并后得到
$$
\boxed{
\|w_j-Y_j^0\|^2\le U_{x,j}\ell_{j,2}^2,\qquad
\|w_j\|^2\le(1+U_{x,j})\ell_{j,2}^2.
}
\tag{2.6}
$$

当 $0\le j\le J=o(x)$ 时，(1.2) 的指数修复一致为
$e^{-x/6+o(x)}$，而 $B_{x,j}-1=O((j+2)/x)+e^{-x/6+o(x)}$。
由 (2.5) 可直接读出
$$
\boxed{
\max_{j\le J}U_{x,j}
=O\!\left(\frac{(J+3)^3}{x}+\frac{(J+3)^4}{x^2}\right)
+e^{-x/6+o(x)}.
}
\tag{2.7}
$$
所以 $J=o(x^{1/3})$ 时，真实顺次二次 MP 在这些相干列上也渐近达到标量下界。此结论仍不是整个 $\mathcal H_j$ 上的 inverse 范数界。

## 3. 同一个阻尼源的第二次修复

取任意真实有界头 $C^h=0$，$2\le J<h$、$c>1$、$s=cS_x$。仍用
$$
a=H_J(s)^{-1}g,\quad
f=\sum_{j=0}^{J}\frac{(-C)^ja\otimes\omega_j}{s^j j!},
\quad
E_j=\frac{\|C^ja\|^2}{s^j j!},
\quad
\epsilon=\sum_{j=1}^{J}E_j.
$$
记 $B=C+D$（本节的 $B$ 仅为实际方程算子，不表示原 weighted shift），并定义真实修复
$$
q_1=D^\dagger Bf,\qquad
q_2=CD^\dagger q_1=C(D^\dagger)^2Bf.
\tag{3.1}
$$
它们都只有有限个远孔层，完整 MP 的自然域逐层成立；$C$ 作用独立头，因而在这些域上确实与 $D^\dagger$ 对易。

令
$$
S_-=S_{x+J+2},\quad \eta=S_-/S_x,\quad
A_*=\max_{0\le j\le J+1}A_{x,j},\quad
U_*=\max_{0\le j\le J}U_{x,j},\quad M_C=\|C\|.
$$
其中 $A_{x,j}$ 是一次稿中的完整相干 MP 明确上界。

在输出远孔层 $j+2$、$0\le j\le J-2$，$q_2$ 的尾列为
$$
v_{j+1}-s(j+1)w_j
$$
乘以 $C(-C)^{j+1}a/[s^{j+1}(j+1)!]$。这个式子来自
$(D^\dagger)^2D\omega_{j+1}=D^\dagger\omega_{j+1}$，
只在该具体 $\omega_{j+1}\in\operatorname{Ran}D^*$ 上使用。

写
$$
v_{j+1}=\frac{\sigma_{j+1}^2}{\sigma_{j+2}^2}\omega_{j+2}+\delta_{j+1},
\qquad
w_j=\frac{\sigma_j^2}{\sigma_{j+2}^2}\omega_{j+2}+\zeta_j.
$$
两误差都与 $\omega_{j+2}$ 正交；其平方费用分别至多
$(A_*^2-1)\ell_{j+1,1}^2$ 和 $U_*\ell_{j,2}^2$。
保留相干部分相消，再只对两误差使用一次二项 Cauchy，得到全部低段费用不超过
$$
\boxed{
\left(\frac c\eta\right)^2
\left[
(1-\eta/c)^2+2(A_*^2-1)+2U_*
\right]\epsilon .
}
\tag{3.2}
$$
这里使用
$$
\frac{\|C^{j+2}a\|^2}{s^{2j+2}((j+1)!)^2}
s^2(j+1)^2\ell_{j,2}^2
\le(c/\eta)^2c^{-j}E_{j+2}.
$$
因此没有额外的 $J$ 因子。

## 4. 两个最高层均保留

$Bf$ 在远孔 $J-1$ 层与 $J$ 层产生的第二次修复，分别落在远孔 $J+1$、$J+2$；这些输出与第 3 节全部低段正交。

对 $j=J-1$ 使用
$\|C^{J+1}a\|\le M_C\|C^Ja\|$，
以及
$\sigma_{J+1}^2/\sigma_J^2\ge(J+1)S_-$，费用至多
$$
\frac{2M_C^2c^{-J}}{(J+1)S_-}
\left[A_*^2+(c/\eta)^2(1+U_*)\right]E_J .
\tag{4.1}
$$
真正最高残量含 $C^{J+1}a\otimes\omega_J$，再乘一次 $C$ 后使用
$\|C^{J+2}a\|\le M_C^2\|C^Ja\|$，费用至多
$$
\frac{M_C^4(1+U_*)c^{-J}}
{(J+1)(J+2)S_-^2}\,E_J .
\tag{4.2}
$$
于是精确可重建的上界为
$$
\boxed{
\|q_2\|^2\le \mathfrak R^{(2)}_{x,J,c}(C)\,\epsilon,
}
\tag{4.3}
$$
其中 $\mathfrak R^{(2)}$ 是 (3.2)、(4.1)、(4.2) 三个 $\epsilon/E_J$ 前系数之和。没有假设 $C^{J+1}a=0$，也没有把 top 移出 natural domain 后省略。

## 5. 新参数及同 actual defect 的显式小量

取
$$
\tau_x=\left(\frac{\log^3(x+1)}x\right)^{1/5},
\quad c_x=1+\tau_x,\quad
J_x=\left\lceil\frac{16\log(x+1)}{\tau_x}\right\rceil .
\tag{5.1}
$$
则 $J_x=O(x^{1/5}\log^{2/5}(x+1))=o(x^{1/3})$，且充分大 $x$ 时
$$
c_x^{-J_x}\le(x+1)^{-8}.
$$
于是
$$
A_*^2-1=O(J_x/x)=O(\tau_x^2),\quad
1-\eta/c_x=O(\tau_x),\quad U_*=O(\tau_x^2).
$$
前稿一次界与本稿 (4.3) 同时给
$$
\boxed{
\|q_1\|^2+\|q_2\|^2
\le
O\!\left((1+\|C\|^4)
\left[\frac{\log^3(x+1)}x\right]^{2/5}\right)\epsilon.
}
\tag{5.2}
$$
常数是绝对常数；全部非渐近系数已在 (1.2)、(2.5)、一次稿 (3.7) 及 (3.2)、(4.1)、(4.2) 给出。

若 $C=A_m+D_{[m,x)}$ 且原 $Q\ge R+J$，$f$ 精确保持同一个
$u_g=(P_{V_Q}-P_{K_Q})i_0g$。前稿已付
$$
\epsilon\le\Delta_g^2,\qquad
\Delta_g^2=\|i_0g-u_g\|^2.
$$
所以 (5.2) 的 $\epsilon$ 可以直接换成同一原测试的 $\Delta_g^2$。

尤其 $R=0,x=m,C=A_m$ 时 $\|C\|\le\|T\|$，$J_m<2^m$，并且 $s_m=c_mS_m\ge S_m$、$s_m\to0$。因此同源代表仍强趋原 $P_Mg$；两次修复均有不含头相似 condition 的显式小量。这里只保原 $V_Q/K_Q$ 的既定 cut；如调用额外的强位并头或母提升定理，仍须分别满足其全部原门槛。

最后定义
$$
z_2=f-q_1+q_2.
$$
由完整层的 $DD^\dagger=I$ 逐项相消，得到准确式
$$
\boxed{
(C+D)z_2=Cq_2.
}
\tag{5.3}
$$
故 $z_2-f$ 和剩余残量都由 (5.2) 控制。不过第三次修复将面对更深的完整核旗；本稿没有把第二次的 primitive 回馈分解无条件复制到所有高度。$z_2$ 尚未被称作原真核向量，原完整中间 Schur、帽返回、carry 与同 $w$ 条件继续保留。
