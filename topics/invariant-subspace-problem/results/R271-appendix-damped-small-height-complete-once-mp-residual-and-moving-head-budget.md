# R271 附录：小阻尼截断的完整一次 MP 残量与移动真实头的显式预算

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 在原连续无限尾上，给定整个真实有限头 $C$，本稿仍使用同一完整正矩阵 $H_{C,J}(s)$ 的 inverse，而不限制其最小源的孔支持。取 $s$ 略大于真实尾方差、$J$ 为 $o(x)$ 的显式增长截断后，原残量经过完整一阶 Moore--Penrose 逆 $D_x^\dagger$ 仍趋零，最高截断项包含在预算内。

特别，对原移动头 $C=A_m$、$x=m$，该结论不支付任何头相似的条件数，不要求固定 $m$，并精确保持原 $V_Q/K_Q/u_g$。它是一次完整 $D^\dagger$ 的结论，不是 $(C+D)^\dagger$ 或全部顺次返回的界。

依据：

- [原完整相干列的 Bernoulli 原像及全层修复](R271-appendix-continuous-tail-coherent-columns-bernoulli-lifts-and-exact-residuals.md)，尤其 §§1、3、4；
- [放大方差、同源阻尼列和远孔指数矩](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)，尤其 §§3--6；
- [原同一实际测试的 coherent 投影身份](R271-appendix-same-actual-test-minimal-coherent-representative-and-exact-residual.md)，§2。

## 1. 同一个完整源与全部自然定义域

在原无限尾 $i\ge x$ 上令
$$
D=D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad
S=S_x=\sum_{i\ge x}(i+1)^{-4}.
$$
所有 $D^\dagger$ 均指这个同一有界算子的完整 Moore--Penrose inverse。它在全孔直和上可以无界；下面只对至多 $J$ 个输入孔层使用它。每一固定层有已付的全层有界右逆，因此本文的所有有限孔列都在其自然定义域，未使用 primitive 限制逆来代替完整逆。

记
$$
\omega_j=(D^*)^j\Omega,\qquad
\sigma_j^2=\|\omega_j\|^2=(j!)^2 e_j(b^2),\qquad \omega_0=\Omega .
$$
让 $C$ 为整个真实强头上的有界 nilpotent 算子，$C^h=0$；头与尾严格对易。取 $1\le J<h$、$c>1$，令
$$
s=cS,\qquad r=c^{-1},\qquad
H_J(s)=\sum_{j=0}^{J}\frac{(C^*)^jC^j}{s^j j!},
\qquad a=H_J(s)^{-1}g ,
$$
$$
f=\sum_{j=0}^{J}\frac{(-C)^ja\otimes\omega_j}{s^j j!}.
\tag{1.1}
$$
完整正能量为
$$
E_j=\frac{\|C^ja\|^2}{s^j j!},\qquad
\epsilon=\sum_{j=1}^{J}E_j
=\langle g,H_J(s)^{-1}g\rangle-\|H_J(s)^{-1}g\|^2
\le \frac{\|g\|^2}{4}.
\tag{1.2}
$$
没有假设 $g$ 或 $a$ 位于低强孔空间。

## 2. 真完整相干 MP 列与一个精确平方相消

写
$$
v_j=D^\dagger\omega_j,\qquad
\ell_j=\frac{\sigma_j^2}{\sigma_{j+1}},\qquad
a_j=\frac{\|v_j\|}{\ell_j}\ge1 .
$$
已付完整随机池预算给
$$
a_j\le A_{x,j}:=
\frac{S_x}{S_{x+j+1}}
+12\,512^j(x+j+1)^{3/2}\sqrt{(j+1)S_x}
   \exp\!\left[-\frac{S_{x+j}}{(x+1)^{-4}}\right].
\tag{2.1}
$$
令
$$
A_*=\max_{0\le j\le J}A_{x,j},\qquad
\nu_j=\frac{\sigma_{j+1}^2}{(j+1)S\sigma_j^2},
\qquad \nu_*=\frac{S_{x+J}}{S_x}.
$$
真实固定大小计数给
$$
\nu_*\le\nu_j\le1\qquad(0\le j\le J).
\tag{2.2}
$$
确实 $\nu_j S$ 是 $j$ 孔乘积权分布中未占位置的平均总平方权；删去任意 $j$ 个位置之后仍有至少 $S_{x+j}$。

因为 $\omega_{j+1}\in\operatorname{Ran}D^*\subset(\ker D)^\perp$，
$$
D^\dagger D\omega_{j+1}=\omega_{j+1},
\qquad
\langle\omega_{j+1},v_j\rangle=\sigma_j^2.
$$
所以对同一个列，而非两个独立上界，
$$
\begin{aligned}
&\left\|D^\dagger\!\left[D\omega_{j+1}-s(j+1)\omega_j\right]\right\|^2\\
&\quad =
\sigma_{j+1}^2-2s(j+1)\sigma_j^2
+s^2(j+1)^2\|v_j\|^2\\
&\quad =
\boxed{
\frac{\sigma_{j+1}^2}{(r\nu_j)^2}
\left[(1-r\nu_j)^2+(a_j^2-1)\right].
}
\end{aligned}
\tag{2.3}
$$
这个完整 MP 平方恒等式同时保留阻尼误差和真正的非相干 inverse 误差。

## 3. 完整残量含最高 top 的显式界

在远孔层 $j<J$，
$$
[(C+D)f]_j=
\frac{(-C)^{j+1}a}{s^{j+1}(j+1)!}
\otimes\left[D\omega_{j+1}-s(j+1)\omega_j\right].
\tag{3.1}
$$
在最高远孔 $J$ 层，残量是
$$
[(C+D)f]_J=
\frac{C(-C)^Ja}{s^J J!}\otimes\omega_J.
\tag{3.2}
$$
不同输入层经 $D^\dagger$ 后仍落入不同、彼此正交的输出孔层。

设 $\kappa_j=\sigma_j^2/(j!S^j)\le1$。把 (2.3) 代入 (3.1)，第 $j$ 项的准确费用是
$$
\kappa_{j+1}r^{j-1}
\frac{(1-r\nu_j)^2+(a_j^2-1)}{\nu_j^2}\,E_{j+1}.
\tag{3.3}
$$
由于 $r^{j-1}\le r^{-1}=c$，全部低段之和至多
$$
c\,\nu_*^{-2}
\left[(1-r\nu_*)^2+(A_*^2-1)\right]\epsilon.
\tag{3.4}
$$

最高层用的仍是完整 $v_J$。从
$\sigma_{J+1}^2/\sigma_J^2\ge(J+1)S_{x+J}$ 得
$$
\begin{aligned}
\|D^\dagger[(C+D)f]_J\|^2
&\le
\frac{\|C\|^2A_*^2r^J}{(J+1)S_{x+J}}\,E_J .
\end{aligned}
\tag{3.5}
$$
因此有全参数、全源的不等式
$$
\boxed{
\|D^\dagger(C+D)f\|^2
\le \mathfrak R_{x,J,c}(C)\,\epsilon,
}
\tag{3.6}
$$
其中
$$
\boxed{
\mathfrak R_{x,J,c}(C)=
\frac{c}{\nu_*^2}
\left[\left(1-\frac{\nu_*}{c}\right)^2+(A_*^2-1)\right]
+\frac{\|C\|^2A_*^2c^{-J}}{(J+1)S_{x+J}}.
}
\tag{3.7}
$$
没有 $J$ 次 Cauchy 损失，也没有把最高层当成 $C^{J+1}a=0$。

## 4. 显式小阻尼选择：全源一次 MP 的统一增长高度界

令 $x\to\infty$，并取
$$
\tau_x=\left(\frac{\log(x+1)}{x}\right)^{1/3},
\qquad c_x=1+\tau_x,
\qquad
J_x=\left\lceil\frac{8\log(x+1)}{\tau_x}\right\rceil .
\tag{4.1}
$$
只需 $J_x<h$。则
$$
J_x=O\!\left(x^{1/3}\log^{2/3}(x+1)\right)=o(x),
\qquad
\frac{J_x+2}{x}=O(\tau_x^2).
$$
对充分大 $x$，$\log(1+\tau_x)\ge\tau_x/2$，故
$$
c_x^{-J_x}\le(x+1)^{-4}.
\tag{4.2}
$$
由原连续尾积分界
$$
\frac{1}{3(y+1)^3}\le S_y\le\frac1{3y^3}
$$
得到
$$
\nu_*\ge\left(\frac{x}{x+J_x+1}\right)^3
=1-O(\tau_x^2).
\tag{4.3}
$$
(2.1) 的第一项在 $0\le j\le J_x$ 上一致为 $1+O(\tau_x^2)$；第二项的对数一致不大于
$$
J_x\log512+O(\log(x+1))
-\frac{(x+1)^4}{3(x+J_x+1)^3}
=-\frac x3+o(x).
$$
所以
$$
A_*=1+O(\tau_x^2)+e^{-x/3+o(x)},\qquad
A_*^2-1=O(\tau_x^2).
\tag{4.4}
$$
又 $1-\nu_*/c_x=O(\tau_x)$。最高层 (3.5) 的系数至多
$$
O\!\left(\frac{\|C\|^2}{(x+1)(J_x+1)}\right).
$$
因此 (3.7) 给
$$
\boxed{
\mathfrak R_{x,J_x,c_x}(C)
=O\!\left((1+\|C\|^2)
\left[\frac{\log(x+1)}x\right]^{2/3}\right).
}
\tag{4.5}
$$
这里 $O$ 的常数是绝对常数；(3.7) 是不使用渐近符号的明确版本。故对任意整个头源 $g$，
$$
\boxed{
\|D_x^\dagger(C+D_x)f\|
\le
O\!\left((1+\|C\|)
\left[\frac{\log(x+1)}x\right]^{1/3}\right)\|g\|.
}
\tag{4.6}
$$
这是完整一次 MP 的向量范数界。没有先要求 $H_J(s)^{-1}g$ 的低孔定位，也没有乘未知的移动源收敛率。

## 5. 原 moving-m 同一来源与缺陷预算

首先取 $R=0$、$x=m$、$C=A_m$。原有限整数头是 $T$ 的不变子空间，所以
$\|A_m\|\le\|T\|$；充分大 $m$ 时 $J_m<d_m=2^m$。取 (4.1) 的 $s_m=c_mS_m$，则 $s_m\ge S_m$ 且 $s_m\to0$。

前篇方差扩张定理可用于同一完整 $H_{A_m,J_m}(s_m)^{-1}$。对固定有限物理 $g$，
$$
f_m\longrightarrow P_Mg,\qquad
\|D_m^\dagger(A_m+D_m)f_m\|
=O_T\!\left((\log(m+1)/m)^{1/3}\right)\|g\|.
\tag{5.1}
$$
任何原合法 $Q_m\ge J_m$ 都保持
$$
(P_{V_{Q_m}}-P_{K_{Q_m}})f_m
=(P_{V_{Q_m}}-P_{K_{Q_m}})i_0g=u_g .
\tag{5.2}
$$
因此 $Q_m$ 可取原 $m/Q$ 窗口本来已合法的参数；本结论只保持既定
$V_{Q_m}/K_{Q_m}$，没有要求 $e^{c d_m^4}$ 的新 cut，也没有把原真实
$u_g$ 换源。若随后调用任何要求 $R=d_m$、$h=2d_m$ 的扩块或内部 cut
结论，仍须另行满足该结论的全部门槛，不能用这里的 $R=0$ 特例取消它们。

还有一个同实际来源的加强。对一般满足原强头 cut 条件 $Q\ge R+J$ 的情形，
设原缺陷
$$
\Delta_g^2=\|i_0g-u_g\|^2
=\|g\|^2-\|u_g\|^2 .
$$
由 $\|u_g\|^2\le\|f\|^2\le q:=\langle g,H_J(s)^{-1}g\rangle$，以及标量
$\lambda-\lambda^2\le1-\lambda$ 对 $0\le\lambda\le1$，有
$$
\boxed{
\epsilon\le\|g\|^2-q\le\Delta_g^2 .
}
\tag{5.3}
$$
所以真正同源的完整一次 MP 费满足
$$
\boxed{
\|D^\dagger(C+D)f\|^2
\le\mathfrak R_{x,J,c}(C)\,\Delta_g^2.
}
\tag{5.4}
$$
对原同 $w$ 测试族，可以直接保留此前已付的同一 $\Delta_g$，没有把标量行升成范数行，亦未给其添加未经证明的收敛速率。

(3.6)--(4.6) 本身亦可用于其他原强前缀 $C=A_m+D_{[m,x)}$，其源恒等式仍要求 $Q\ge R+J$，且 $\|C\|\le\|T\|+\sum_{i\ge m}b_i$ 一致有界。但若此时取 $s=c_xS_x$，未必有 $s\ge S_m$；故不能据 (4.6) 自动调用前篇 moving-m 的强极限。一次 MP 费和原投影同源仍成立，两种量词分开。

## 6. 一次修复之后仍保留的完整反馈

置
$$
z=f-D^\dagger(C+D)f .
$$
则准确有
$$
Dz=-Cf,\qquad
(C+D)z=-C D^\dagger(C+D)f .
\tag{6.1}
$$
所以 $z-f$ 的物理范数和 (6.1) 的未修复残量均由本稿支付。可是第二次修复的尾源一般含
$D^\dagger\omega_j$，不再只是 $\omega_j$；不能免费把 (2.1) 重新用于它，也不能以 (3.6) 推出 $z\in\ker(C+D)$。

原完整返回、帽投影、中间 Schur 和全部两端 partial 仍须在同一源上继续处理。小的一次 MP 修正没有被乘上一个未经证明的完整逆上界，本稿没有证明 $N=M$。
