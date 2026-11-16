# R271 附录：相邻创建来源的完整返回配对与真实帽测试运输

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 对同一个原实际 $u_{w,Q}$，一族相邻实际投影向量经真实创建行合成后，仍正交于整个 $K_Q$。这个全核正交性使其完整返回配对可以直接用左最小列和裸列估计，不需要普通右最小逆的范数。随后保留真正的 $P_{\mathscr E}$、Riordan 环境逆伴随以及 $P_{\widehat{\mathscr E}}$，证明同一创建家族准确运输。原方差一位 Schur 的 $\sigma_i$、$\alpha_i$ 恢复来源实际满足本稿的平方和输入条件。

本稿不把原主测试 $e_{f,n}$ 或其帽版本认作这一家族。另用同一完整配对支付其 $V^\perp$ 缺陷，留下准确的真核投影 $P_{K_Q}f$ 返回。该核测试的进一步表示及其主返回仍未付；普通 $N=M$ 未证。

依据：

- [同一顶部强尾源流和完整两费](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)；
- [完整返回的正交分解、驱动系统及唯一提升](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)；
- [实际返回投影、逆伴随测试和全部切口](R271-appendix-actual-return-projection-inverse-adjoint-test-and-all-dark-moment-transport.md)；
- [相对孔 Riordan 的完整／裸运输](R271-appendix-relative-hole-riordan-conjugacy-full-bare-source-transport-and-uniform-budget.md)；
- [原方差一位恢复和整个加权返回包](R271-appendix-native-variance-one-bit-restoration-and-auxiliary-clearing-pairing.md)。

## 1. 原实际向量、两个孔数与完整右环境

固定原 N/Y 模型，仍写
$$
C=A_m+D_{[m,x)},\qquad x=m+R,\qquad d=2^m,\qquad h=d+R,\qquad C^h=0,
$$
$$
D=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad
z_i=b_i^2,\qquad S=\sum_{i\ge x}z_i .
\tag{1.1}
$$
$E_i$ 是实际物理位删除，$E_i^*$ 是创建。以 $\mathcal N$ 记从第 $m$ 位起的原总尾孔数，以 $\mathcal N_>$ 记从第 $x$ 位起的远孔数。因此
$$
\mathcal N_>\le\mathcal N\le\mathcal N_>+R.
$$

取原同一个合法母窗口 $Q$、原 $w\in W$ 以及
$$
u=u_{w,Q}=(P_{V_Q}-P_{K_Q})w,\qquad \|u\|\le\|w\|.
$$
本稿没有换成另一个便宜来源，也没有用 $w$ 替代 $u$。对一个合法切口
$$
n\ge0,\qquad n+h+R<Q,
\tag{1.2}
$$
置
$$
r_n=C u_n,\qquad
Y_nu=(u_{n+1},\ldots,u_{n+h}),
$$
其中下标表示远孔层。旧真实左最小性给
$$
U_nr_n=P_{\mathcal N_>\le n}u,\qquad
\mu_n(r_n)^2=\|P_{\mathcal N_>\le n}u\|^2.
\tag{1.3}
$$

沿上述父稿，记完整和裸右最小列为 $J_{f,n},J_{b,n}$，完整返回为
$$
\mathcal R_n=J_{f,n}-J_{b,n},\qquad
\alpha_n(r)^2=\|J_{b,n}r\|^2.
$$
完整右环境及其高空间为
$$
\mathscr W_n=\bigoplus_{j=1}^h
\ker C^{h-j+1}\otimes
\bigl(\ker D^h\cap\mathcal H_{n+j}^{>}\bigr),
$$
$$
\mathscr W_n^{\rm hi}=\bigoplus_{j=1}^h
\ker C^{h-j+1}\otimes
\bigl(\ker D^{j-1}\cap\mathcal H_{n+j}^{>}\bigr).
$$
若 $Z_{f,n}$ 为完整零源核，真实返回空间为闭和
$$
\mathscr E_n=\mathscr W_n^{\rm hi}+Z_{f,n},\qquad
\mathscr E_{0,n}=\mathscr E_n\ominus Z_{f,n}.
\tag{1.4}
$$
已付的正交关系是
$$
\mathcal R_nr_n\in\mathscr E_{0,n},\qquad
J_{b,n}r_n\perp\mathscr E_n,\qquad
\alpha_n(r_n)^2\le\|Y_nu\|^2.
\tag{1.5}
$$
特别，左右物理孔层互相正交，故
$$
\boxed{\mu_n(r_n)^2+\alpha_n(r_n)^2\le\|u\|^2\le\|w\|^2.}
\tag{1.6}
$$

## 2. 全核正交测试的完整配对引理

令 $\eta$ 为原物理向量，满足
$$
P_{\mathcal N\le Q}\eta=\eta,\qquad \eta\perp K_Q .
\tag{2.1}
$$
它不必属于 $V_Q$ 或 $U_Q$。定义原完整返回测试
$$
z_n=P_{\mathscr E_n}Y_n\eta.
\tag{2.2}
$$
每个 $Z_{f,n}$ 向量放回物理层后，都是真 $(C+D)$ 核，支撑于远孔 $n+1,\ldots,n+h$，因而总孔不超过 $n+h+R<Q$。由 (2.1)，
$$
Y_n\eta\perp Z_{f,n},\qquad z_n\in\mathscr E_{0,n}.
\tag{2.3}
$$

还必须使用全部 $h$ 个右段。把
$$
k_n=(U_nr_n,-J_{f,n}r_n)
\tag{2.4}
$$
分别放在远孔 $\le n$ 和 $n+1,\ldots,n+h$。原同源条件与末端方程给
$$
(C+D)k_n=0,\qquad
P_{\mathcal N\le n+h+R}k_n=k_n,
$$
所以 $k_n\in K_Q$。这是原完整物理核，不是裸商核。由
$\langle k_n,\eta\rangle=0$，准确有
$$
\langle J_{f,n}r_n,Y_n\eta\rangle
=\langle U_nr_n,P_{\mathcal N_>\le n}\eta\rangle.
$$
因此
$$
\boxed{
\langle\mathcal R_nr_n,z_n\rangle
=
\langle U_nr_n,P_{\mathcal N_>\le n}\eta\rangle
-\langle J_{b,n}r_n,Y_n\eta\rangle .
}
\tag{2.5}
$$
投影 $P_{\mathscr E_n}$ 在左边因
$\mathcal R_nr_n\in\mathscr E_n$ 被准确吸收；不是把它与删除或 MP 交换。

对右边两个正交物理部分同时使用 Cauchy，(1.6) 给
$$
\boxed{
|\langle\mathcal R_nr_n,z_n\rangle|
\le
\sqrt{\mu_n(r_n)^2+\alpha_n(r_n)^2}\,
\|P_{\mathcal N_>\le n+h}\eta\|
\le\|w\|\,\|\eta\|.
}
\tag{2.6}
$$
(2.5) 保留了完整裸末端项。若只保 $j\le r<h$ 的右段，剩余
$j>r$ 与 (2.4) 的配对仍须保留，不能直接对该单独部分套 (2.6)。

对任意合法有限切口集 $\mathcal I$，同一个 $\eta$ 同时满足
$$
\boxed{
\sum_{n\in\mathcal I}
|\langle\mathcal R_nr_n,P_{\mathscr E_n}Y_n\eta\rangle|
\le \#\mathcal I\,\|w\|\,\|\eta\|.
}
\tag{2.7}
$$
这里没有为不同切口重选 $u$ 或 $\eta$。这估计的是完整配对，不是
$\mathcal R_n$ 的环境算子范数。

## 3. 相邻实际投影的真实创建来源

取任意一族实际相邻投影向量
$$
u_i=(P_{V_{Q-1}}-P_{K_{Q-1}})i_0g_i,\qquad i\ge x,
$$
并假设唯一的平方和输入条件
$$
\mathfrak A=\sum_{i\ge x}\|u_i\|^2<\infty.
\tag{3.1}
$$
各 $g_i$ 可以不同；不假定未经度量白化的 $\sum\|g_i\|^2$ 小。
对任意 $|c_i|\le1$，在原物理空间定义
$$
\eta=\sum_{i\ge x}b_ic_iE_i^*u_i.
\tag{3.2}
$$

首先，实际创建行满足完整算子恒等式
$$
\bigl(b_iE_i^*\bigr)_i\bigl(b_iE_i^*\bigr)_i^*
=\sum_i z_iE_i^*E_i
=\sum_i z_i n_i\preceq SI.
$$
故 (3.2) 由 $\ell^2$ 行域收敛，且
$$
\boxed{\|\eta\|^2\le S\mathfrak A.}
\tag{3.3}
$$
这是带原权 $b_i$ 的明确创建合成，不是未付的无权占据范数行。

其次，原远位删除与 $L_m=C+D$ 交换，且把原总孔支撑降一层，因此
$$
E_iK_Q\subset K_{Q-1}.
$$
对 $k\in K_Q$，
$$
\langle k,E_i^*u_i\rangle=\langle E_ik,u_i\rangle=0.
$$
同时 $u_i$ 支撑于原总孔 $\le Q-1$，创建后支撑 $\le Q$。有限和及闭极限遂证明 (2.1)。于是
$$
\boxed{
|\langle\mathcal R_nr_n,P_{\mathscr E_n}Y_n\eta\rangle|
\le\sqrt S\,\|w\|\,\mathfrak A^{1/2}.
}
\tag{3.4}
$$

若 $n\ge1$ 且满足 (1.2)，每个 $u_i$ 的相邻切口 $n-1$ 也合法，因为
$(n-1)+h+R<Q-1$。令
$$
e_{i,n-1}=P_{\mathscr E_{n-1}}Y_{n-1}u_i
\in\mathscr E_{0,n-1}.
\tag{3.5}
$$
在右栈上，$E_i$ 保持全部头旗，与 $D$ 对易，并同时把绝对远孔降一层。
因此
$$
E_i\mathscr W_n^{\rm hi}\subset\mathscr W_{n-1}^{\rm hi},
\qquad E_iZ_{f,n}\subset Z_{f,n-1},
\qquad E_i\mathscr E_n\subset\mathscr E_{n-1}.
\tag{3.6}
$$
取伴随得到
$$
P_{\mathscr E_n}E_i^*(I-P_{\mathscr E_{n-1}})=0.
\tag{3.7}
$$
又真实孔切口给 $Y_nE_i^*=E_i^*Y_{n-1}$。故 (2.2) 的测试准确是
$$
\boxed{
z_n=
P_{\mathscr E_n}
\sum_{i\ge x}b_ic_iE_i^* e_{i,n-1}.
}
\tag{3.8}
$$
特别，内侧 $P_{\mathscr E_{n-1}}$ 没有被未经证明地删除；
(3.6)--(3.7) 正是吸收它所需的原包含关系。
每个创建列还正交于 $Z_{f,n}$，因为删除把 $Z_{f,n}$ 送入
$Z_{f,n-1}$。

## 4. 真正逆伴随和帽返回投影的两次运输

本节只在已付相对孔 Riordan 参数中使用。沿父稿取
$$
\widehat C=\psi_m(C)/d_0,\qquad
g(C_{\rm s})=\psi_m(C_{\rm s})/(d_0C_{\rm s}),
$$
以及完整环境映射 $K_{n,\rm amb}$。它只使用相对行数
$j=1,\ldots,h$ 与真实删除幂 $D^k$。原已付常数是
$$
\|K_{n,\rm amb}\|,\ \|K_{n,\rm amb}^{-1}\|
\le\mathcal C_0,\qquad
\mathcal C_0=\exp[32(1+e^{1070})].
\tag{4.1}
$$
原合法母窗口、强位尺度及全部头旗不变；帽版保守地再要求 $n+2h+R<Q$，以保留父稿使用的同一内部窗口。本节不将该界用于未满足父稿参数的任意 $R$。

Riordan 正反映射保高空间，并准确将完整零源核送到帽零源核。因此闭和 (1.4) 给
$$
K_{n,\rm amb}\mathscr E_n=\widehat{\mathscr E}_n.
$$
这给第一项准确投影吸收：
$$
\boxed{
P_{\widehat{\mathscr E}_n}K_{n,\rm amb}^{-*}P_{\mathscr E_n}
=P_{\widehat{\mathscr E}_n}K_{n,\rm amb}^{-*}.
}
\tag{4.2}
$$
证明是对任意 $\widehat v\in\widehat{\mathscr E}_n$，
$K_{n,\rm amb}^{-1}\widehat v\in\mathscr E_n$，再取伴随。
没有宣称逆伴随单独保持原高旗。

因为系数只依相对行数，且 $E_iD=DE_i$，原全部环境上有
$$
E_iK_{n,\rm amb}=K_{n-1,\rm amb}E_i,\qquad
K_{n,\rm amb}^{-*}E_i^*=E_i^*K_{n-1,\rm amb}^{-*}.
\tag{4.3}
$$
帽空间也满足 (3.6)，故
$$
P_{\widehat{\mathscr E}_n}E_i^*
(I-P_{\widehat{\mathscr E}_{n-1}})=0.
\tag{4.4}
$$
把 (4.2)--(4.4) 按实际次序用于 (3.8)，得到
$$
\boxed{
\begin{aligned}
\widehat z_n
&:=P_{\widehat{\mathscr E}_n}K_{n,\rm amb}^{-*}
       P_{\mathscr E_n}Y_n\eta\\
&=P_{\widehat{\mathscr E}_n}
  \sum_i b_ic_iE_i^*\widehat e_{i,n-1},\\
\widehat e_{i,n-1}
&=P_{\widehat{\mathscr E}_{n-1}}K_{n-1,\rm amb}^{-*}
       P_{\mathscr E_{n-1}}Y_{n-1}u_i .
\end{aligned}}
\tag{4.5}
$$
所以这里确是相邻实际返回测试的原逆伴随／帽投影，
不是用环境创建列替换帽测试。所有输入仍正交于相应完整零源核。

还保留完整最小化差。因
$K_nJ_{f,n}r-J_{\widehat f,n}(gr)\in\widehat Z_{f,n}$，
且原／帽裸最小列分别正交于原／帽 $\mathscr E$，直接得
$$
\boxed{
\langle\widehat{\mathcal R}_n(gr_n),\widehat z_n\rangle
-\langle\mathcal R_nr_n,z_n\rangle
=\langle K_nJ_{b,n}r_n,\widehat z_n\rangle .
}
\tag{4.6}
$$
右端是保留下来的裸端误差，绝对值至多
$\mathcal C_0^2\alpha_n(r_n)\|z_n\|$，没有把它写成零。
结合 $\|z_n\|\le\|Y_n\eta\|$ 与 (2.5)，得到
$$
\boxed{
|\langle\widehat{\mathcal R}_n(gr_n),\widehat z_n\rangle|
\le (1+\mathcal C_0^2)\|w\|\,\|\eta\|
\le(1+\mathcal C_0^2)\sqrt S\,\|w\|\mathfrak A^{1/2}.
}
\tag{4.7}
$$
对任意合法有限切口集可对绝对值求和，右端只再乘其切口数；
没有重选相邻来源，也没有丢掉最左或最右部分段。

## 5. 原方差一位完整恢复来源实际满足输入门

在原方差稿参数
$$
x\ge64,\qquad h\le2x,\qquad Q\ge R+h+2
\tag{5.1}
$$
中，固定同一个头 forcing $g$，置
$$
H=H_C(S),\quad a=H^{-1}g,\quad
\mathfrak F_1=\sum_{j\ge1}
j\,\frac{\|C^ja\|^2}{S^jj!},\qquad
\Delta=\|i_0g-u_{g,Q}\|.
$$
每个真删位 Gram 是 $H_i=H_C(S-z_i)$，其完整最小新源为
$(a_{0,i},a_{1,i})$。准确两反馈为
$$
\sigma_i=\frac{b_i}{S-z_i}H_iCa_{1,i},\qquad
\alpha_i=\frac{b_i}{S-z_i}C^*H_i a_{1,i}.
\tag{5.2}
$$
不能交换其中 $C,H_i$ 的次序。上一层同源 Gram 比较
$G_{U,Q-1}\preceq H^{-1}\preceq e^8H_i^{-1}$ 给
$$
\sum_i\|Z_{U,Q-1}\sigma_i\|^2\le8e^{16}\mathfrak F_1,\qquad
\sum_i\|Z_{U,Q-1}\alpha_i\|^2\le8e^{16}\mathfrak F_1 .
\tag{5.3}
$$
$Q$ 多出的这一层正是保证上一层低 forcing 门所需的条件。
而
$$
S\le\frac1{3x^3},\qquad \mathfrak F_1\le2x\Delta^2.
$$
因此分别取 $g_i=\sigma_i$ 或 $g_i=\alpha_i$，
同一个相位族、相邻投影和完整测试满足
$$
\boxed{
|\langle\mathcal R_nr_n,z_n\rangle|
\le3e^8\,\frac{\|w\|\Delta}{x},
}
\tag{5.4}
$$
$$
\boxed{
|\langle\widehat{\mathcal R}_n(gr_n),\widehat z_n\rangle|
\le3e^8(1+\mathcal C_0^2)\frac{\|w\|\Delta}{x}.
}
\tag{5.5}
$$
(5.5) 还需 §4 的真实 Riordan 参数。
这些是作用于指定完整原恢复来源的真实右配对界；
不需要把未经压缩的 $\sigma$ 列放进单个 $D^*$ 的像中。

## 6. 相邻外投影交换差的全核证书

对 $\sigma$ 家族，还可准确保外侧投影交换差。令
$$
\xi_\sigma=
\sum_i b_ic_iP_{U_Q}E_i^*i_0\sigma_i,\qquad
\eta_\sigma=
\sum_i b_ic_iE_i^*Z_{U,Q-1}\sigma_i,\qquad
\delta_\sigma=\xi_\sigma-\eta_\sigma .
\tag{6.1}
$$
第一和按原恢复身份
$$
P_{U_Q}E_iF_i=Z_{U,Q}r_i+P_{U_Q}E_i^*i_0\sigma_i
$$
及完整平方和预算收敛，并有
$$
\|\xi_\sigma\|\le2e^8\sqrt{S\mathfrak F_1}.
$$
第二和由 (3.3)、(5.3) 给
$\|\eta_\sigma\|\le\sqrt8e^8\sqrt{S\mathfrak F_1}$。故
$$
\boxed{
\|\delta_\sigma\|
\le(2+\sqrt8)e^8\sqrt{S\mathfrak F_1}
\le4e^8\Delta/x .
}
\tag{6.2}
$$
$\xi_\sigma\in U_Q\subset K_Q^\perp$，而 §3 已证明
$\eta_\sigma\perp K_Q$；二者总孔支撑均 $\le Q$。因此
$\delta_\sigma$ 满足 (2.1)，**不要求它在 $V_Q$ 中**。
将 $\eta$ 换成 $\delta_\sigma$ 后，(2.5)--(2.7) 和 (4.6)--(4.7)
全部成立，特别其完整右交换差配对不超过
$4e^8\|w\|\Delta/x$，帽版再乘 $1+\mathcal C_0^2$。

线性和 (3.7) 还准确给
$$
\begin{aligned}
P_{\mathscr E_n}Y_n\xi_\sigma
-
P_{\mathscr E_n}\sum_i b_ic_iE_i^* e_{\sigma_i,n-1}
=P_{\mathscr E_n}Y_n\delta_\sigma .
\end{aligned}
\tag{6.3}
$$
所以这里同时保了外侧相邻 $P_U$ 交换差和内侧真实 $P_{\mathscr E}$；
它们没有因范数小而被自动删除。帽版本按 (4.2)--(4.5) 保完全相同的次序。

## 7. 原主测试中 $V^\perp$ 缺陷的完整支付

这一节重新保原同一个固定低 forcing $f=i_0g$、同一 $Q$，记
$$
v_f=P_{V_Q}f,\qquad k_f=P_{K_Q}f,\qquad
e_f^V=f-v_f,\qquad u_f=v_f-k_f=f-e_f^V-k_f.
\tag{7.1}
$$
$f$ 在所有远位为真空，因而对 $n\ge0$ 有 $Y_nf=0$。
又 $K_Q\subset V_Q$，所以
$$
e_f^V\perp K_Q,\qquad
P_{\mathcal N\le Q}e_f^V=e_f^V.
$$
这正是 §2 所需条件，不要求先把 $e_f^V$ 写成创建行。

令
$$
e_{f,n}=P_{\mathscr E_n}Y_nu_f,\quad
e^V_{n}=P_{\mathscr E_n}Y_ne_f^V,\quad
e^K_{n}=P_{\mathscr E_n}Y_nk_f.
$$
它们严格满足
$$
\boxed{e_{f,n}=-e^V_n-e^K_n.}
\tag{7.2}
$$
其中 $e^V_n\in\mathscr E_{0,n}$ 由 §2 保证。
对 $z\in Z_{f,n}$，其物理嵌入属于 $K_Q$ 且只有严格正远孔，
所以
$$
\langle k_f,z\rangle=\langle P_{K_Q}f,z\rangle
=\langle f,z\rangle=0.
$$
因此 $Y_nk_f\perp Z_{f,n}$，也有 $e^K_n\in\mathscr E_{0,n}$。
没有从“小核投影范数”推出任何返回算子界。

对 (7.2) 的 $V^\perp$ 项直接应用 (2.6)，得到
$$
\boxed{
\left|
\langle\mathcal R_nr_n,e_{f,n}\rangle+
\langle\mathcal R_nr_n,e^K_n\rangle
\right|
\le\|w\|\,\|e_f^V\|.
}
\tag{7.3}
$$
帽测试始终按
$P_{\widehat{\mathscr E}_n}K_{n,\rm amb}^{-*}$
作用于这三个真实返回向量。其线性性、(2.3) 和 §4 给
$$
\boxed{
\left|
\langle\widehat{\mathcal R}_n(gr_n),\widehat e_{f,n}\rangle+
\langle\widehat{\mathcal R}_n(gr_n),\widehat e^K_n\rangle
\right|
\le(1+\mathcal C_0^2)\|w\|\,\|e_f^V\|.
}
\tag{7.4}
$$
全部合法切口可以先对绝对值求和再取平均，右端不增加切口数因子。
原母窗口若要令右端小，仍使用真正 $P_{V_Q}$ 的逼近；
这里没有为不同切口重取 forcing，也没有给 $w$ 的尾设定速率。

留下的唯一核测试正是
$$
\boxed{
e^K_n=P_{\mathscr E_n}Y_n(P_{K_Q}f),\qquad
\widehat e^K_n=P_{\widehat{\mathscr E}_n}
K_{n,\rm amb}^{-*}P_{\mathscr E_n}Y_n(P_{K_Q}f).
}
\tag{7.5}
$$
它来自同一个真实全核投影。即使
$\|k_f\|\le\|f-u_f\|$ 很小，也不能据此估计
$\langle\mathcal R_nr_n,e^K_n\rangle$；
$k_f$ 本身一般不满足 §2 的全核正交条件。
其未来带只给已经合法的 Bessel 范数界
$$
\sum_{n\in\mathcal I}\|e^K_n\|^2
\le\nu\|k_f\|^2,\qquad
\sum_{n\in\mathcal I}\|\widehat e^K_n\|^2
\le\mathcal C_0^2\nu\|k_f\|^2,\qquad \nu\le h,
$$
不把该范数界乘上一个未知的返回 inverse。

## 8. 自然域、原误差及剩余主项

所有 $D,E_i,E_i^*$ 在原连续尾有界模型中按实际物理空间作用。
每个固定 $m,R,n$ 只调用父稿有限多个孔层上的完整最小列，
不使用全孔有界的 $D^\dagger$。各层 $\ker D^a$、完整／裸链、
$Z_f$ 和闭和 $\mathscr E$ 均不改变。无穷位置和先取有限部分和，
再以 (3.1)--(3.3)、(5.3) 及原恢复行的尾界取强极限；
全部闭正交性和配对随之保留。

本稿从头使用真正的 $u_{w,Q}$。原母窗口的 carry 误差若要将它与
$P_{\mathcal N\le Q}w$ 比较，仍使用父稿原式；本稿没有将该误差扩到
未经支付的窗口，也没有用尾的无速率收敛乘上一个普通右 inverse。
帽版唯一额外误差正是 (4.6) 的裸端项，已与 (2.5) 一起支付。

新增可用范围是：原指定恢复创建来源及其相邻外投影交换差，能够保完整
$h$ 段、全部原零源和真正帽运输进入同一 $w$ 的右配对。原主
$e_{f,n}=P_{\mathscr E_n}Y_nu_f$ 一般尚未证明可分解成 (3.8) 的家族加
同样有界的全核正交余项；额外 $q_h(-T_0)^*$ 或其它全返回操作也未因
本稿自动获得这样的表示。因此 (5.4)--(6.3) 不等于完整普通右费上界，
亦不关闭原主负式或 $N=M$。
