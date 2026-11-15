# R271 附录：真实返回上的逆芽伴随测试与位置加权全旗运输

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文把返回主配对中的 $q_h(-T_0)^*$ 精确提到同一个物理右环境；完整零源投影始终保留。这个额外多项式及真实 Riordan 逆伴随都保持已付的实际测试暗矩。进一步证明：真实返回投影、这个逆芽伴随、Riordan 帽测试及其全部正交核旗，均有位置加权交换预算 $O(\nu Q\|f-u_f\|^2)$，常数不依赖切口、$m$ 或 $h$。$\nu$ 是原窗口的实际重叠数。

本文没有估计完整返回列 $\mathcal R$，也没有把真正正交旗换成顺次 Moore--Penrose 投影。新结论支付的是原主配对中真实测试端的进一步运输。

依赖：

- [完整返回的物理分解及有限驱动系统](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)；
- [强联块 gauge 与准确 divided-difference](R271-appendix-strong-gauge-true-left-feedback-driven-return-and-ordinary-endpoint.md)；
- [相对层 Riordan 完整运输](R271-appendix-relative-hole-riordan-conjugacy-full-bare-source-transport-and-uniform-budget.md)；
- [真实返回投影、逆伴随及全暗矩](R271-appendix-actual-return-projection-inverse-adjoint-test-and-all-dark-moment-transport.md)；
- [同源位置加权交换、全旗与排斥 Hardy](R271-appendix-actual-position-weighted-exchange-full-flags-and-exclusion-hardy.md)。

## 1. 固定来源及同一个返回环境

沿用原 $m,R,Q$，置
$$
C=A_m+D_<,\qquad h=2^m+R,\qquad x=m+R,\qquad
D=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad \delta=\|D\|.
$$
取有限的合法切口集合 $\mathcal I$，所有切口都满足原低输出及右环境条件；若使用强 gauge 主配对，再要求 $n+2h+R<Q$。取固定有限物理测试 $f$，其第 $x$ 位以后为真空。始终使用
$$
v=P_Vf,\qquad k=P_Kf,\qquad u_f=v-k,\qquad e^V=f-v,
$$
其中 $K=K_{m,Q}\subset V=V_{m,Q}$ 是原来的两个物理空间。令
$$
\Delta_f^2=\|e^V\|^2+\|k\|^2=\|f-u_f\|^2,\qquad
\zeta_f=\|e^V\|+\|k\|\le\sqrt2\Delta_f .
\tag{1.1}
$$
最后的等式使用 $e^V\perp k$。

对每个切口，$\mathscr W_n,\mathscr E_n,Z_{f,n},\mathscr E_{0,n}$ 都是完整返回稿的原物理空间：
$$
\mathscr E_n=\mathscr W_n^{\rm hi}\oplus^\perp Z_{b,n}
=\mathscr W_n^{\rm hi}+Z_{f,n},\qquad
\mathscr E_{0,n}=\mathscr E_n\ominus Z_{f,n}.
$$
第二个和是已经证明的闭和。它保证每次有限位平衡时
$\mathscr E_n(t)=S(t)\mathscr E_n(0)$，没有把非正交相似误当正交裸截面的运输。

写
$$
Y_{f,n}=(u_{f,n+1},\ldots,u_{f,n+h}),\qquad
e_{f,n}=P_{\mathscr E_n}Y_{f,n}.
\tag{1.2}
$$
这是原实际返回代表，已知 $e_{f,n}\perp Z_{f,n}$。
令 $\mathcal Y$ 为同时提取所有这些未来段的算子，并置
$$
\nu=\sup_\ell\#\{n\in\mathcal I:n<\ell\le n+h\}\le h.
$$
因此 $\|\mathcal Y\|\le\sqrt\nu$，且 $\mathcal Yf=0$。于是
$$
\|\mathbf Y_f\|^2\le\nu\Delta_f^2,\qquad
\|\mathbf e_f\|^2\le\nu\Delta_f^2.
\tag{1.3}
$$
这里粗体表示所有切口的正交直和。每个实际右栈的远孔均不超过 $Q$；后文只用这个物理支撑上界，不要求 $P_{\mathscr E_n}$ 与孔数交换。

## 2. 返回商上的逆芽伴随就是带原投影的环境多项式

在完整物理右栈上定义环境尾移位
$$
(\mathbb T z)_j=Dz_{j+1},\qquad(\mathbb Tz)_h=0.
$$
这里暂不加头旗或尾旗，准确环境为 $\bigoplus_{j=1}^h(\mathcal H_C\otimes\mathcal H^>_{n+j})$。它有 $\|\mathbb T\|\le\delta$、$\mathbb T^h=0$；限制到 $\mathscr W_n$ 就是原 $\mathcal T$。环境伴随将第 $j$ 行以 $D^*$ 升到第 $j+1$ 行，并在 $j=h$ 截为零。因此 $q_h(-\mathbb T)^*$ 也严格留在这一个环境，每步远孔都不超过 $n+h\le Q$。

原 $\mathscr E_n$ 和 $Z_{f,n}$ 都被 $\mathcal T$ 保持，所以
$$
T_{0,n}=P_{\mathscr E_{0,n}}\mathcal T|_{\mathscr E_{0,n}}
$$
是这个真不变商上的压缩。对任意多项式 $p$ 及 $e\in\mathscr E_{0,n}$，
$$
\boxed{
p(T_{0,n})^*e=P_{\mathscr E_n}p(\mathbb T)^*e .
}
\tag{2.1}
$$
证明：商上的逐幂乘法由不变性成立；对 $z\in Z_{f,n}$，
$\langle p(\mathbb T)^*e,z\rangle=\langle e,p(\mathcal T)z\rangle=0$。
因此右边投到 $\mathscr E_n$ 后已经属于 $\mathscr E_{0,n}$。
环境限制所引入的 $P_{\mathscr W_n}$ 被外层 $P_{\mathscr E_n}$ 吸收。
这不是声称 $\mathscr E_n$ 约化 $\mathbb T$。

保留原有限多项式
$$
q_h(z)=\left[\frac{\psi_m(z)}z\right]_{<h}
=d_0+\sum_{j=1}^{h-1}q_jz^j,\qquad d_0=e^{-20}.
$$
在原允许的远尾半径上，已有绝对系数预算
$$
A_1=\sum_{j=1}^{h-1}|q_j|\delta^j<d_0/2,\quad
A_0=d_0+A_1,\quad
A_{\rm drv}=\sum_{j=1}^{h-1}j|q_j|\delta^j .
\tag{2.2}
$$
这里 $d_0=e^{-20}$ 是原固定数，不随 $m$ 改变：原 $\Lambda_0=100-105+25=20$。故 $A_0<3e^{-20}/2$ 有统一绝对上界；$A_1$ 仍保其更小的原参数值。没有使用头环境 $\|q_h(C)\|$。

定义真正的新测试
$$
\boxed{
e^q_{f,n}=q_h(-T_{0,n})^*e_{f,n}
=P_{\mathscr E_n}q_h(-\mathbb T)^*P_{\mathscr E_n}Y_{f,n}.
}
\tag{2.3}
$$
它属于同一个 $\mathscr E_{0,n}$，且
$$
\|\mathbf e_f^q\|\le A_0\sqrt\nu\Delta_f,\qquad
\|\mathbf e_f^q-d_0\mathbf e_f\|
\le A_1\sqrt\nu\Delta_f .
\tag{2.4}
$$
所有结论也适用于去常数多项式 $q_h-d_0$，此时将 $A_0$ 换成 $A_1$。

对同一实际源 $r_{w,n}$，已付驱动身份现在准确成为
$$
\boxed{
\left|
\langle\mathcal R_nq_h(C_{\rm s})r_{w,n},e_{f,n}\rangle
-\langle\mathcal R_nr_{w,n},e^q_{f,n}\rangle
\right|
\le A_{\rm drv}\alpha(r_{w,n})\|e_{f,n}\|.
}
\tag{2.5}
$$
所以 (2.3) 正是主配对所需的测试，未另选来源。

## 3. 全暗矩和完整 Riordan 帽测试

对有限个互不相交的远尾相邻对，使用原平衡参数
$$
H_i=n_{i+1}-n_i,\qquad
\theta_i=\log\frac{i+2}{i+1},\qquad
S(t)=\exp\!\left(\sum_i t_iH_i\right).
$$
所有参数都在 $0\le t_i\le\theta_i$。在此盒子中尾 $\ell^1$ 范数不增加，故 (2.2) 对环境多项式统一成立。令
$$
B_q(t)=q_h(-\mathbb T(t))^*.
$$
准确协变为
$$
B_q(t)=S(t)^{-1}B_q(0)S(t),\qquad
\|\partial_S B_q(t)\|\le2^{|S|}A_0.
\tag{3.1}
$$
去常数时右边为 $2^{|S|}A_1$。这里求导的是环境多项式；不能把含物理投影的 $T_0(t)$ 自身说成同一相似族。

若使用已付 $\tau_{14}$ 窗口，完整环境 Riordan 算子有
$\|K_{\rm amb}^{\pm1}\|\le\mathcal C_0$，其逆伴随也满足 (3.1) 中同型的导数界。具体地，$K_{\rm amb}^{-1}$ 仍是输出行 $J$ 与 $\mathbb T$ 的有限降行多项式；其伴随反向升行，仍在第 $h$ 行截断。因此它和所有 $P_{\mathscr E_n}$、$P_{\widehat{\mathscr E}_n}$ 及其正交差都保持同一 $n+1,\ldots,n+h$ 物理栈。后面的 $\le Q$ 支撑估计在每个中间因子之后均成立，不要求它们与 $\mathcal N$ 交换。新帽测试准确是
$$
\boxed{
\widehat e^q_{f,n}
=P_{\widehat{\mathscr E}_n}
 K_{\rm amb}^{-*}
 P_{\mathscr E_n}B_qP_{\mathscr E_n}Y_{f,n}.
}
\tag{3.2}
$$
它仍正交于全部 $\widehat Z_{f,n}$：$K^{-1}\widehat Z_{f,n}=Z_{f,n}$，
而 (2.3) 已正交于 $Z_{f,n}$。不能删掉 (3.2) 的任何源投影。

为明确给出已有暗矩的运输，记 $N_\sigma$ 为原互不相交对的暗计数，$\sigma=4$ 指物理反对称行，$\sigma=5$ 指真 pair primitive 行；置
$$
a_x=\sum_i\theta_i^2e^{2\theta_i}
\le e^{2/(x+1)}/x.
$$
原真实投影的混合导数不超过 $4^rr!$，缺陷导数带同一个
$e^{\sum\theta_i}\zeta_f$。对 (2.3)、(3.2) 做 Leibniz 后，环境因子的
$2^r$ 与投影的 $4^rr!$ 卷积分别给 $e^{1/2}$、$e$，故
$$
\sum_n\left\langle {N_\sigma\choose r}e^q_{f,n},e^q_{f,n}\right\rangle
\le
\nu e A_0^2\binom{r+2}{2}^2r!(\sigma^2a_x)^r\zeta_f^2,
\tag{3.3}
$$
$$
\sum_n\left\langle {N_\sigma\choose r}\widehat e^q_{f,n},
\widehat e^q_{f,n}\right\rangle
\le
\nu e^2\mathcal C_0^2A_0^2
\binom{r+3}{3}^2r!(\sigma^2a_x)^r\zeta_f^2 .
\tag{3.4}
$$
具体地，每个待微分的环境因子贡献
$\sum_{j\ge0}(1/2)^j/j!=e^{1/2}$；其余投影／缺陷因子的微分次数分配数给显示的二项式。任一所选对在 $t_i=0$ 时，整个实际输出都严格交换对称；逐参数 FTC 再对互不相交集合求和给 (3.3)--(3.4)。真 primitive 行的额外微分正是原 $\sigma=5$ 预算。有限和先证，再由 Tonelli 推到无限对族。

若再接全部真正正交旗
$$
F_\ell=P_{\ker D^\ell}-P_{\ker D^{\ell-1}},
$$
原三带导数列范数为 $2\sqrt{2r+1}\,4^rr!$。同一证明给
$$
\sum_{n,\ell}\left\langle{N_\sigma\choose r}F_\ell e^q_{f,n},
F_\ell e^q_{f,n}\right\rangle
\le4\nu e A_0^2(2r+1)\binom{r+3}{3}^2
r!(\sigma^2a_x)^r\zeta_f^2,
\tag{3.5}
$$
$$
\sum_{n,\ell}\left\langle{N_\sigma\choose r}F_\ell\widehat e^q_{f,n},
F_\ell\widehat e^q_{f,n}\right\rangle
\le4\nu e^2\mathcal C_0^2A_0^2(2r+1)\binom{r+4}{4}^2
r!(\sigma^2a_x)^r\zeta_f^2.
\tag{3.6}
$$
这些是整个正交分析列的估计，没有逐旗另乘 $h$。

## 4. 一个保局部行的准确投影差引理

以下引理也允许所有相邻对重叠。

设 $H=H^*$、$H^3=H$，$P=P_E$、$P'=P_{e^{sH}E}$，
$|s|\le\theta$。对任意 $z$，
$$
(I-P')Pz=(I-P')(I-e^{sH})Pz,
$$
$$
P'(I-P)z=P'(I-e^{-sH})(I-P)z.
$$
第二式用 $e^{-sH}\operatorname{Ran}P'\subset E$ 及 $e^{-sH}$ 自伴。
两项位于 $P'$ 的两个正交部分，故
$$
\boxed{
\|(P'-P)z\|^2
\le(e^\theta-1)^2
\bigl(\|HPz\|^2+\|H(I-P)z\|^2\bigr).
}
\tag{4.1}
$$
这比对所有位置使用一个环境投影范数界更有用。

若 $B(t)=e^{-tH}B(0)e^{tH}$ 且 $\|B(t)\|\le M$，则在端点
$t=\theta$ 有
$$
\boxed{
\|(B(\theta)-B(0))z\|
\le(e^\theta-1)
\bigl(\|HB(\theta)z\|+e^\theta M\|Hz\|\bigr).
}
\tag{4.2}
$$
它直接来自
$B(\theta)-B(0)=(I-e^{\theta H})B(\theta)
+e^{\theta H}B(\theta)(I-e^{-\theta H})$。

这两个式子保留同一端点的局部 $H$ 行；不会把位置和变成
$\sum_i1$。

## 5. 真实返回投影的位置预算

现在对全部相邻对 $i\ge x$，令
$$
a_i=(i+1)(i+2),\quad
r_x=1+\frac1{x+1},\quad
\mathfrak e_{\rm pos}(z)=\sum_{i\ge x}a_i\|P_i^-z\|^2.
$$
在所有右栈的直和上也使用同一形式。准确有
$$
e^{\theta_i}-1=\frac1{i+1},\qquad
a_i(e^{\theta_i}-1)^2\le r_x,\qquad
\sum_iH_i^2\preceq2\mathcal N.
\tag{5.1}
$$

为每个 $i$ 只平衡该一对，其余权保持原值，记这一平衡面的向量为下标 $0,i$。对原两个投影应用 (4.1)，用 $H_if=0$，得到
$$
\|u_f-u_{f,0,i}\|^2
\le4(e^{\theta_i}-1)^2
\bigl(\|H_ie^V\|^2+\|H_ik\|^2\bigr).
\tag{5.2}
$$
所有右边都在原来的同一端点，而非不同变形处。

写 $\mathbf e=\mathbf P_E\mathbf Y$，则
$$
\mathbf e-\mathbf e_{0,i}
=(\mathbf P_E-\mathbf P_{E,0,i})\mathbf Y
+\mathbf P_{E,0,i}(\mathbf Y-\mathbf Y_{0,i}).
$$
由 (4.1)、(5.2) 及 $\|\mathcal Y\|\le\sqrt\nu$，
$$
\begin{aligned}
\sum_i a_i\|\mathbf e-\mathbf e_{0,i}\|^2
&\le4r_xQ\|\mathbf Y\|^2\\
&\quad+16\nu r_x
\bigl(\langle\mathcal Ne^V,e^V\rangle+
      \langle\mathcal Nk,k\rangle\bigr)\\
&\le20\nu r_xQ\Delta_f^2 .
\end{aligned}
\tag{5.3}
$$
第一行使用 $\mathbf e\perp(\mathbf Y-\mathbf e)$ 及所有右栈孔数
$\le Q$；不要求投影与孔数交换。第二行中的两个缺陷也支撑在原
$\le Q$ 孔空间。

平衡面的 $\mathbf e_{0,i}$ 交换对称，所以
$$
\boxed{
\sum_n\mathfrak e_{\rm pos}(e_{f,n})
\le20\nu r_xQ\Delta_f^2.
}
\tag{5.4}
$$
真 pair primitive 投影 $A_i^-$ 与 $P_i^-$ 的差仅在单占据部分，
且 $\|A_i^--P_i^-\|\le\theta_i\le e^{\theta_i}-1$。因此
$$
\boxed{
\sum_n\mathfrak a_{\rm pos}(e_{f,n})
\le44\nu r_xQ\Delta_f^2 .
}
\tag{5.5}
$$

## 6. 有界逆相似因子和新测试的同源位置预算

给出一个可直接复用的完整规则。假设某个实际右栈族 $\mathbf z(t)$ 满足：各平衡面交换对称；在原端点
$$
\|\mathbf z\|^2\le M_0^2\nu\Delta_f^2,\qquad
\sum_i a_i\|\mathbf z-\mathbf z_{0,i}\|^2
\le C_z\nu Q\Delta_f^2 .
$$
令
$$
\mathbf w(t)=P_{E(t)}B(t)\mathbf z(t),
$$
其中 $E(t)=S(t)E(0)$，$B(t)=S(t)^{-1}B(0)S(t)$，
$\|B(t)\|\le M$，所有向量仍在相同的 $\le Q$ 物理右栈。

三项望远镜、(4.1)--(4.2)、(5.1) 给
$$
\boxed{
\begin{aligned}
\|\mathbf w\|^2&\le M^2M_0^2\nu\Delta_f^2,\\
\sum_i a_i\|\mathbf w-\mathbf w_{0,i}\|^2
&\le
M^2\left[(18+12r_x^2)r_xM_0^2+3C_z\right]
\nu Q\Delta_f^2 .
\end{aligned}
}
\tag{6.1}
$$
常数来源可逐项检查：投影差贡献
$6r_xQM^2\|\mathbf z\|^2$，因子差贡献
$12r_x(1+r_x^2)QM^2\|\mathbf z\|^2$，输入差贡献
$3M^2\sum_i a_i\|\mathbf z-\mathbf z_{0,i}\|^2$。
它们均使用同一端点局部行。

置
$$
c_q=(78+12r_x^2)r_x,\qquad
c_{\widehat q}=(252+48r_x^2)r_x.
$$
对 (5.3) 连用 (6.1)，得到
$$
\boxed{
\sum_n\mathfrak e_{\rm pos}(e^q_{f,n})
\le c_q A_0^2\nu Q\Delta_f^2,
}
\tag{6.2}
$$
$$
\boxed{
\sum_n\mathfrak e_{\rm pos}(\widehat e^q_{f,n})
\le c_{\widehat q}\mathcal C_0^2A_0^2
\nu Q\Delta_f^2 .
}
\tag{6.3}
$$
去掉 $q$ 因子的普通帽测试也有
$c_q\mathcal C_0^2\nu Q\Delta_f^2$ 的界。
若将 $q_h$ 换成 $q_h-d_0$，(6.2)--(6.3) 的 $A_0$ 可准确换成 $A_1$。

对任何 (6.1) 产生的输出，若其差常数为 $C_w$、范数常数为 $M_w$，
同一 primitive 行比较给
$$
\sum_n\mathfrak a_{\rm pos}(w_n)
\le(2C_w+4r_xM_w^2)\nu Q\Delta_f^2 .
\tag{6.4}
$$
因此所有这些位置形式都在自然闭二次型域内；无限位置和由非负项单调极限得到。

## 7. 位置预算通过全部正交旗，仍不乘旗数

对一个固定 $H_i$，真正 $F_\ell(t)$ 为三带。令
$T_\ell=F_{\ell+1}H_iF_\ell$，则
$$
F_\ell'=T_\ell+T_\ell^*-T_{\ell-1}-T_{\ell-1}^*,
$$
$$
\sum_\ell\|F_\ell'z\|^2
\le3\sum_\ell\|H_iF_\ell z\|^2.
\tag{7.1}
$$
当这里的 $z$ 固定不动时，将 $H_iF_\ell(t)z$ 作为整个分析列，
反向 Grönwall 给
$$
\left(\sum_\ell\|(F_\ell(\theta_i)-F_\ell(0))z\|^2\right)^{1/2}
\le(e^{\sqrt3\theta_i}-1)
\left(\sum_\ell\|H_iF_\ell(\theta_i)z\|^2\right)^{1/2}.
\tag{7.2}
$$
这是对完整旗列的估计。

对第 6 节任一输出 $\mathbf w$，分解
$F(\theta_i)\mathbf w-F(0)\mathbf w_{0,i}$ 并使用分析列等距，得到
$$
\boxed{
\sum_{n,\ell}\mathfrak e_{\rm pos}(F_\ell w_n)
\le
\left[2C_w+12r_x^{\,2\sqrt3-1}M_w^2\right]
\nu Q\Delta_f^2 .
}
\tag{7.3}
$$
确实，
$a_i(e^{\sqrt3\theta_i}-1)^2\le3r_x^{2\sqrt3-1}$，
且
$\sum_{i,\ell}\|H_iF_\ell w\|^2
\le2\langle\mathcal Nw,w\rangle$，
因为每个 $F_\ell$ 与孔数交换。再作一次 (6.4) 型比较，真 primitive 形式为
$$
\boxed{
\sum_{n,\ell}\mathfrak a_{\rm pos}(F_\ell w_n)
\le
\left[4C_w+
 (24r_x^{\,2\sqrt3-1}+4r_x)M_w^2\right]
\nu Q\Delta_f^2 .
}
\tag{7.4}
$$
这同时覆盖 $e_f$、$e_f^q$、普通帽测试和 $\widehat e_f^q$。在
$e_f$ 的情形取 $C_w=20r_x,M_w=1$。
全部正交旗一起付费，没有把每个旗的估计再累加一次 $h$。

## 8. 原配对的范围

(2.5) 保原源 $r_{w,n}$。把 (2.3) 放入已付 Riordan 混合配对，还得到
$$
\left|
\langle\mathcal R_nr_{w,n},e^q_{f,n}\rangle
-\langle\widehat{\mathcal R}_n(g(C)r_{w,n}),\widehat e^q_{f,n}\rangle
\right|
\le\mathcal C_0^2\alpha(r_{w,n})\|e^q_{f,n}\|.
\tag{8.1}
$$
新帽测试准确是 (3.2)，而不是任意平滑向量。
(1.3)、原裸费窗口平方和及 Cauchy--Schwarz 支付这些显示的误差，
不涉及 $\|\mathcal R_n\|$。

对原同一 $w\in W$ 和合法母窗口，已付 $P_Uw\to w$ 给
$\limsup\Delta_f\le\|f-w\|$。所以本稿的每个位置形式在除以
$\nu Q$ 后都保一个仅乘固定 $\|f-w\|^2$ 的常数。这个结论没有要求
$\Delta_f$ 的衰减率。

仍未证明的是返回列与这些测试之间的统一混合估计，或顺次 MP 和的
两个端点 partial sum 在位置形式下的相对负部控制。真正
$F_\ell$ 是正交核旗，不能替换为
$D_n^\dagger\cdots D_{n-j+1}^\dagger D^j$。
同样，(7.3)--(7.4) 只控制测试端，不能与一个未付的逆范数相乘后声称
$N=M$ 已闭合。
