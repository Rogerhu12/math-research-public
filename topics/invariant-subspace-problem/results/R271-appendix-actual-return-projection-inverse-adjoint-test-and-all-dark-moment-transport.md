# R271 附录：实际返回投影、Riordan 逆伴随测试与完整低暗矩运输

日期：2026-11-15（UTC）。

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文把真实固定测试的全部暗对矩送过原返回投影，并进一步送过已经付费的 Riordan 逆伴随和帽系统返回投影。保留的是原同一个 $u_f=(P_V-P_K)f$ 产生的 $e_{Y,n}$ 和 $\widehat e_{Y,n}$；没有另选测试，没有把返回投影与孔数、尾 MP 或暗投影交换。

关键是完整返回空间有一个不涉及裸正交代表的准确表示
$$
\mathscr E_n=\mathscr W_n^{\mathrm{hi}}+Z_{f,n}.
$$
该和闭，并在每个真实有限对配平变形下准确运输。这使返回投影本身的导数有统一界。整个切口族只付实际未来窗口的重叠数 $\nu\le h$，不乘切口数或 $Q$。

最后给同一个原 $w$ 与固定 $f$ 的完整返回双线性式。未知的主项仍是返回列与这里已支付低暗矩的测试之配对；本文不估计完整 Green/MP 作用于该测试的范数，不宣布普通 $N=M$。

依赖：

- [同一顶部强尾源流和完整自然域](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)；
- [完整返回的正交分解与唯一提升](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)；
- [强 gauge 稿第6节的实际返回代表](R271-appendix-strong-gauge-true-left-feedback-driven-return-and-ordinary-endpoint.md)；
- [真实投影缺陷和全暗矩](R271-appendix-actual-projection-defect-two-sided-generator-and-all-dark-moments.md)；
- [相对孔 Riordan 的完整与裸域运输](R271-appendix-relative-hole-riordan-conjugacy-full-bare-source-transport-and-uniform-budget.md)；
- [Riordan 的实际返回混合配对](R271-appendix-riordan-actual-return-mixed-pair-transport-and-window-error.md)。

## 1. 固定原源、返回环境及切口重叠数

固定原 $N/Y$ 模型和
$$
C=A_m+D_<,\qquad h=2^m+R,\qquad C^h=0,\qquad
D=D_>=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad x=m+R.
$$
取原同一总尾窗口 $Q$，记
$$
V=V_{m,Q},\qquad K=K_{m,Q}\subset V,\qquad
P_U=P_V-P_K.
$$
本稿使用任意固定有限物理 $f$，且 $f$ 在第 $x$ 位及以后为真空。置
$$
v_f=P_Vf,\qquad k_f=P_Kf,\qquad
u_f=v_f-k_f,\qquad e_f^V=f-v_f,
$$
$$
\zeta_f=\|e_f^V\|+\|k_f\|.
\tag{1.1}
$$
两项 $e_f^V,k_f$ 正交，所以
$$
\zeta_f\le\sqrt2\,\|f-u_f\|.
\tag{1.2}
$$
对每个合法切口
$$
n\ge0,\qquad n+h+R<Q,
\tag{1.3}
$$
保同一真实来源
$$
r_{f,n}=C(u_f)_n,\qquad
Y_{f,n}=((u_f)_{n+1},\ldots,(u_f)_{n+h}),
\tag{1.4}
$$
其中下标是远孔数。原低输出递推、左最小性、全部右头旗和零源正交均仍成立；这些事实仅用 $u_f\in V\ominus K$，不要求 $f\in W$。

固定非空合法切口集合 $\mathcal I$，定义
$$
\nu=\sup_{\ell\ge0}\#\{n\in\mathcal I:n<\ell\le n+h\}.
\tag{1.5}
$$
必有 $\nu\le h$；若切口间距至少 $h$，则 $\nu\le1$。把物理向量送到全部未来窗口的算子记为
$$
\mathcal W_{\mathcal I}z=( (z_{n+1},\ldots,z_{n+h}) )_{n\in\mathcal I}.
$$
由正交孔层准确计数，
$$
\|\mathcal W_{\mathcal I}z\|^2
=\sum_\ell \#\{n:n<\ell\le n+h\}\|z_\ell\|^2
\le\nu\|P_{\mathcal I_+}z\|^2,
\tag{1.6}
$$
其中 $\mathcal I_+=\bigcup_{n\in\mathcal I}\{n+1,\ldots,n+h\}$。
$\mathcal W_{\mathcal I}f=0$。

以下所有返回对象都在前稿的完整固定层自然域中：只取有限多个孔层的真满射和有界最小逆；不使用全孔直和上的有界 $D^\dagger$。

## 2. 原返回空间的准确闭和与实际投影

对每个 $n$，沿完整返回稿置
$$
\mathscr W_n=
\bigoplus_{j=1}^h
 \ker C^{h-j+1}\otimes\ker D^h|_{\mathcal H_{n+j}},
$$
$$
\mathscr W_n^{\mathrm{hi}}=
\bigoplus_{j=1}^h
 \ker C^{h-j+1}\otimes\ker D^{j-1}|_{\mathcal H_{n+j}},
\qquad
P_n^{\mathrm{lo}}=I-P_{\mathscr W_n^{\mathrm{hi}}}
\quad\hbox{on }\mathscr W_n .
$$
令 $\mathcal Y_{f,n},\mathcal Y_{b,n}$ 为完整右链和原裸链，$Z_{f,n},Z_{b,n}$ 为其完整零源核。此处下标 $f$ 表示 full，勿与输入向量 $f$ 混淆。

既有真实满射
$$
P_n^{\mathrm{lo}}\mathcal Y_{f,n}=\mathcal Y_{b,n}
$$
保源，因此限制到零源后准确给
$$
P_n^{\mathrm{lo}}Z_{f,n}=Z_{b,n}.
\tag{2.1}
$$
确实，每个裸零源的完整提升仍具有相同的零首源；反向包含显然。

于是
$$
\boxed{
\mathscr E_n
:=\mathscr W_n^{\mathrm{hi}}\oplus^\perp Z_{b,n}
=\mathscr W_n^{\mathrm{hi}}+Z_{f,n}.
}
\tag{2.2}
$$
该和闭，因为左边是两个闭正交空间的和。定义
$$
\mathscr E_{0,n}=\mathscr E_n\ominus Z_{f,n}.
$$
(2.2) 没有将裸规范误认成代数不变的正交截面；它恰把这个截面消去，留下两个真正按核方程定义的空间。

沿前稿记同源最小列 $J_{b,n},J_{f,n}$、返回列
$$
\mathcal R_n=J_{f,n}-J_{b,n},\qquad
\mathcal R_n^*\mathcal R_n=H_n-B_n .
$$
对 (1.4) 的同一来源，已付完整物理身份为
$$
e_{f,n}:=P_{\mathscr W_n}Y_{f,n}+J_{b,n}r_{f,n}
\in\mathscr E_{0,n},
$$
$$
\|e_{f,n}\|^2+\|J_{b,n}r_{f,n}\|^2
=\|P_{\mathscr W_n}Y_{f,n}\|^2
\le\|Y_{f,n}\|^2.
\tag{2.3}
$$
因为 $J_{b,n}r_{f,n}\perp\mathscr E_n$、$\mathscr E_n\subset\mathscr W_n$，得到更便于本稿使用的准确投影式
$$
\boxed{
e_{f,n}=P_{\mathscr E_n}Y_{f,n}
=P_{\mathscr E_{0,n}}Y_{f,n}.
}
\tag{2.4}
$$
第二个等号使用原实际 $Y_{f,n}\perp Z_{f,n}$。这不是对任意外部输入删除零源的恒等式。

特别
$$
J_{b,n}r_{f,n}
=-(P_{\mathscr W_n}-P_{\mathscr E_n})Y_{f,n}.
\tag{2.5}
$$
(2.4) 保原整个返回投影；它不表示该投影保持单个远孔层或暗对次数。

## 3. 有限对变形与返回投影导数

选任意有限个互不相交的相邻对 $S\subset\{i:i\ge x\}$，令
$$
H_i=n_{i+1}-n_i,\qquad
\theta_i=\log\frac{i+2}{i+1},\qquad
\mathsf S(t)=\exp\!\left(\sum_{i\in S}t_iH_i\right),
\quad0\le t_i\le\theta_i .
$$
只将这些对写为
$$
b_i(t)=a_ie^{t_i},\qquad b_{i+1}(t)=a_ie^{-t_i},
\qquad a_i=\sqrt{b_ib_{i+1}},
$$
其余原权不变。端点 $t=\theta$ 是原模型。精确有
$$
D(t)\mathsf S(t)=\mathsf S(t)D(0).
\tag{3.1}
$$
$H_i$ 自伴且范数 $1$；$\mathsf S$ 与全部物理孔截断、独立强头 $C$ 及其头旗交换。

所以 $V(t)=\mathsf S(t)V(0)$、$K(t)=\mathsf S(t)K(0)$，并在每个完整右环境中有
$$
\mathscr W_n^{\mathrm{hi}}(t)=\mathsf S(t)\mathscr W_n^{\mathrm{hi}}(0),
\qquad Z_{f,n}(t)=\mathsf S(t)Z_{f,n}(0).
$$
由 (2.2)，
$$
\boxed{\mathscr E_n(t)=\mathsf S(t)\mathscr E_n(0).}
\tag{3.2}
$$
所有像均闭：这里每次只变有限个位，$\mathsf S(t)$ 在整个物理 Hilbert 空间有界可逆。固定层满射也由该真实相似保留。

若 $P(t)$ 是任一上述像的物理正交投影，则
$$
\partial_iP=H_iP+PH_i-2PH_iP.
$$
对 $r$ 个不同变量的混合导数，已有实参数归纳给
$$
\|\partial_SP(t)\|\le4^r r!.
\tag{3.3}
$$
这对切口直和 $\bigoplus_{n\in\mathcal I}P_{\mathscr E_n(t)}$ 同样成立，不产生切口数因子。

令 $z(t)$ 为 $P_{K(t)}f$ 或 $(I-P_{V(t)})f$。因为 $H_if=0$，有准确的反射微分方程
$$
\partial_i z=(I-2P(t))H_i z.
$$
所以
$$
\|\partial_Sz(t)\|\le4^r r!\,\|z(t)\|,
\qquad
\|z(t)\|\le e^{\sum_{i\in S}\theta_i}\|z(\theta)\|.
\tag{3.4}
$$
这些是同一点的实际缺陷归一，不含 $z$ 的除法；零向量情形亦成立。

用 $\mathcal W_{\mathcal I}f=0$，(2.4) 给整个切口列
$$
\mathbf e(t):=(e_{f,n}(t))_{n\in\mathcal I}
=-\left(\bigoplus_nP_{\mathscr E_n(t)}\right)
 \mathcal W_{\mathcal I}\bigl[(I-P_{V(t)})f+P_{K(t)}f\bigr].
\tag{3.5}
$$
Leibniz、(1.6)、(3.3)–(3.4) 遂给
$$
\boxed{
\|\partial_S\mathbf e(t)\|
\le\sqrt\nu\,(r+1)4^r r!\,
 e^{\sum_{i\in S}\theta_i}\zeta_f.
}
\tag{3.6}
$$
这里的 $(r+1)$ 来自把 $r$ 个导数分到投影和实际缺陷的两种位置；完整返回投影没有省略。

## 4. 原实际返回测试的所有暗矩

令 $U_i$ 为物理交换对 $(i,i+1)$ 的酉反射，
$$
P_i^-=(I-U_i)/2.
$$
另令 $A_i^-(t_i)$ 为真实单孔 primitive 行
$$
\frac{b_{i+1}(t_i)e_i-b_i(t_i)e_{i+1}}
{\sqrt{b_i(t_i)^2+b_{i+1}(t_i)^2}}
$$
张成的一维正交投影，扩为该对真空/双占据上的零，并在其余位为恒等张量。
有 $\|(A_i^-)'(t_i)\|\le1$，且 $A_i^-(0)=P_i^-$。

在任何一个坐标面 $t_i=0$，原 $u_f(t)$、$\mathscr E_n(t)$ 均被 $U_i$ 约化，输入 $f$ 被 $U_i$ 固定；故 $e_{f,n}(t)$ 也对称。这给混合 FTC 所需的全部坐标面消失，不是仅在全零点消失。

固定任意互不相交的无限或有限相邻对族 $\mathcal D$，在所有右段及切口上使用同一个计数
$$
N_4=\sum_{i\in\mathcal D}P_i^-,
\qquad N_5=\sum_{i\in\mathcal D}A_i^-(\theta_i).
$$
两族各自在不同对之间对易。置
$$
a_x=\sum_{i\in\mathcal D}\theta_i^2e^{2\theta_i}
\le \frac{e^{2/(x+1)}}x.
\tag{4.1}
$$
对物理暗投影直接应用 (3.6) 和混合 FTC；对真实 primitive 暗投影同时微分 $A_i^-(t_i)$。后者的 Leibniz 和满足
$$
\sum_{a=0}^r\binom ra(a+1)4^a a!
\le(r+1)5^r r!.
$$
因此对 $\sigma=4,5$，每个选定的 $r$ 对有
$$
\left\|\prod_{i\in S}P_{\sigma,i}\,\mathbf e(\theta)\right\|
\le\sqrt\nu\,(r+1)\sigma^r r!
 \left(\prod_{i\in S}\theta_i e^{\theta_i}\right)\zeta_f .
$$
对所有 $|S|=r$ 求平方和，使用非负 Tonelli 和
$\sum_{|S|=r}\prod a_i\le(\sum_i a_i)^r/r!$，得到
$$
\boxed{
\sum_{n\in\mathcal I}
\left\langle\binom{N_\sigma}{r}e_{f,n},e_{f,n}\right\rangle
\le
\nu(r+1)^2r!\,(\sigma^2a_x)^r\zeta_f^2,
\qquad r\ge1.
}
\tag{4.2}
$$
这里作用在 $e_{f,n}$ 上的是原返回投影之后的计数；不将其移过 $P_{\mathscr E_n}$。

特别，对整数 $k\ge r\ge1$，
$$
\sum_n\|\mathbf1_{\{N_\sigma\ge k\}}e_{f,n}\|^2
\le
\nu(r+1)^2\frac{r!}{\binom kr}
 (\sigma^2a_x)^r\zeta_f^2.
\tag{4.3}
$$
可以沿前稿按合法 $r\le k$ 优化得到平方根指数尾。本文保留 (4.3) 的全部整数范围，不把大 $k$ 的最优选取用于不满足条件的小 $k$。

## 5. 穿过真正的 Riordan 逆伴随和帽返回投影

本节只在已付相对孔 Riordan 参数中使用：取原 $\tau_{14}$、
$R=\lceil4e^{\tau_{14}}\rceil$、$h=d+R$，并保合法母窗口及 (1.3)。
帽头为
$$
\widehat C=\psi_m(C)/d_0,
$$
保全部强位混合。旧证明给明确统一常数
$$
\mathcal C_0=\exp[32(1+e^{1070})]
$$
以及真实右映射 $K_n$、裸商映射和它们的逆的范数上界 $\mathcal C_0$。

为了在固定 Hilbert 空间微分，把同一个有限 Riordan 多项式延到全右段
$$
\mathscr A_n=\bigoplus_{j=1}^h
 \mathcal H_{\mathrm{head}}^C\otimes\mathcal H_{n+j}^{>},
$$
暂不加头/尾旗，记为 $K_{n,\mathrm{amb}}(t)$。其公式只用相对层 $J=1,\ldots,h$ 和真实尾行移位；旧绝对系数预算同样给该全段算子及逆的范数 $\le\mathcal C_0$。

这个界对 (3.1) 的整个参数盒仍成立。确实，每个被变形对满足
$$
b_i(t)+b_{i+1}(t)=2a_i\cosh t_i
\le2a_i\cosh\theta_i=b_i+b_{i+1}.
$$
故 $\|D(t)\|\le\sum b_i(t)\le1/x$，可在同一个旧 Riordan majorant 中使用完全相同的尾上界；没有把有限维相似的全条件数加进来。

由于相对层数与 $\mathsf S(t)$ 交换，
$$
K_{n,\mathrm{amb}}(t)
=\mathsf S(t)K_{n,\mathrm{amb}}(0)\mathsf S(t)^{-1}.
$$
其逆伴随 $\mathcal B_n(t)=K_{n,\mathrm{amb}}(t)^{-*}$ 因而满足
$$
\partial_i\mathcal B_n=\mathcal B_nH_i-H_i\mathcal B_n,
\qquad
\boxed{\|\partial_S\mathcal B_n(t)\|\le2^r\mathcal C_0.}
\tag{5.1}
$$
此式保了逆伴随的方向。

帽空间也满足
$\widehat{\mathscr E}_n(t)=\mathsf S(t)\widehat{\mathscr E}_n(0)$，由与 (2.2) 相同的完整零源闭和证明得到。原实际被运输测试准确为
$$
\boxed{
\widehat e_{f,n}(t)
=P_{\widehat{\mathscr E}_n(t)}
 \mathcal B_n(t)P_{\mathscr E_n(t)}Y_{f,n}(t).
}
\tag{5.2}
$$
这是既有混合配对中的原测试，不是新选列。需要说明全段扩张与原受限逆伴随的关系：在移动 $\mathscr W_n(t)$ 上，
$K_n^{-*}=P_{\mathscr W_n(t)}K_{n,\mathrm{amb}}^{-*}|_{\mathscr W_n(t)}$。
外侧 $\widehat{\mathscr E}_n(t)\subseteq\mathscr W_n(t)$ 正交投影准确吸收这个 $P_{\mathscr W_n(t)}$，才得到 (5.2)。没有假设 $K_n^{-*}$ 自身在全段公式下保持原旗。

又 $K_nZ_{f,n}=\widehat Z_{f,n}$，故
$\widehat e_{f,n}\perp\widehat Z_{f,n}$，即
$\widehat e_{f,n}\in\widehat{\mathscr E}_{0,n}$。

对 (5.2) 的两个投影、一个逆伴随和实际缺陷应用 Leibniz。
若 $b$ 个导数落在逆伴随，余下 $r-b$ 个分到三个其余因子，则
$$
\begin{aligned}
\|\partial_S\widehat{\mathbf e}(t)\|
&\le\sqrt\nu\,\mathcal C_0\,4^r r!
 e^{\sum\theta_i}\zeta_f
 \sum_{b=0}^r\frac{2^{-b}}{b!}\binom{r-b+2}{2}\\
&\le\sqrt\nu\,e^{1/2}\mathcal C_0
 \binom{r+2}{2}4^r r!
 e^{\sum\theta_i}\zeta_f .
\end{aligned}
\tag{5.3}
$$
每个参数面 $t_i=0$ 上，所有投影和 Riordan 多项式及其伴随都与 $U_i$ 交换，故 (5.2) 的输出同样对称。重复混合 FTC；真实 primitive 暗投影的导数用 $\sigma=5$ 吸收，得到
$$
\boxed{
\sum_{n\in\mathcal I}
\left\langle\binom{N_\sigma}{r}\widehat e_{f,n},
                        \widehat e_{f,n}\right\rangle
\le
\nu\,e\,\mathcal C_0^2
 \binom{r+2}{2}^{\!2}r!(\sigma^2a_x)^r\zeta_f^2,
\quad \sigma=4,5,\ r\ge1.
}
\tag{5.4}
$$
同样可除以 $\binom kr$ 得完整高暗谱尾。$\mathcal C_0$ 虽很大，但与 $m,n,Q,h$ 无关。窗口重叠数仍是 $\nu$，不是切口数。

本节没有顺便处理额外的 $q_h(-T_0)^*$ 乘子，也没有宣称任意后续 Green、真幂逆或顺次 MP 保持这些矩。其真实运输若要使用，仍须逐一证明。

## 5a. 返回投影之后再保整个真实正交旗

若下一步要先把返回测试分解成真正的尾核旗，不能假设 $P_{\mathscr E_n}$ 或 $P_{\widehat{\mathscr E}_n}$ 保持该旗。本节直接把这个投影后的操作保在同一参数族中。

在每个右段上定义
$$
\Pi_\ell(t)=P_{\ker D(t)^\ell},\qquad
F_\ell(t)=\Pi_\ell(t)-\Pi_{\ell-1}(t),\qquad \Pi_0=0,
$$
并按右段/切口直和。已付全旗导数论证只用
$\operatorname{ad}_{D(t)}^2H_i=0$ 与 $H_i$ 自伴：
$H_i$ 在这些 $F_\ell$ 中严格三带；$r$ 阶混合
$\partial_SF_\ell$ 两侧均支撑于
$\sum_{|a-\ell|\le r}F_a$。
于是完整分析列满足
$$
\left\|z\longmapsto\bigl((\partial_SF_\ell)z\bigr)_\ell\right\|
\le2\sqrt{2r+1}\,4^r r!.
\tag{5a.1}
$$
直和所有切口及右段不改变这个范数；每个当前正交旗输入只计 $2r+1$ 次，不计 $h$ 次。

对 $F_\ell(t)\mathbf e(t)$ 应用三个因子的 Leibniz；对
$F_\ell(t)\widehat{\mathbf e}(t)$ 则保 §5 的逆伴随及其 $2^r\mathcal C_0$ 导数。与 (5.3) 相同的有限组合计数分别给
$$
\|\partial_S(F_\ell\mathbf e)_\ell\|
\le2\sqrt{\nu(2r+1)}\binom{r+2}{2}4^r r!
e^{\sum\theta_i}\zeta_f,
$$
$$
\|\partial_S(F_\ell\widehat{\mathbf e})_\ell\|
\le2e^{1/2}\mathcal C_0\sqrt{\nu(2r+1)}
\binom{r+3}{3}4^r r!e^{\sum\theta_i}\zeta_f .
\tag{5a.2}
$$
在每个平衡参数面，真 $F_\ell(t)$ 与该对的物理交换也对易，故暗面仍消失。混合 FTC、primitive 暗投影的 Leibniz 及 Tonelli 因而给
$$
\boxed{
\sum_{n\in\mathcal I}\sum_\ell
\left\langle\binom{N_\sigma}{r}F_\ell e_{f,n},
                                      F_\ell e_{f,n}\right\rangle
\le
4\nu(2r+1)\binom{r+2}{2}^{\!2}
r!(\sigma^2a_x)^r\zeta_f^2,
}
\tag{5a.3}
$$
以及
$$
\boxed{
\sum_{n\in\mathcal I}\sum_\ell
\left\langle\binom{N_\sigma}{r}F_\ell\widehat e_{f,n},
                                      F_\ell\widehat e_{f,n}\right\rangle
\le
4e\mathcal C_0^2\nu(2r+1)\binom{r+3}{3}^{\!2}
r!(\sigma^2a_x)^r\zeta_f^2 .
}
\tag{5a.4}
$$
这里 $\sigma=4,5$、$r\ge1$。整个旗均保留，除了真实未来的重叠数 $\nu$ 之外没有新增 $h$ 因子。

单独某个 $\Pi_\ell e_{f,n}$ 或 $\Pi_\ell\widehat e_{f,n}$ 也可在同一 Leibniz 证明中用
$\|\partial_S\Pi_\ell\|\le4^r r!$ 直接估计，其常数与 $\ell$ 无关；不能通过把暗计数移过 $\Pi_\ell$ 来声称该结论。
(5a.3)–(5a.4) 的所有旗都是真正正交核旗，仍不是顺次 $Q^jD^j$。

## 6. 与原 $w$ 的同源双线性主项

取原同一个 $w$，令 $u_w=P_Uw$、$r_{w,n}=C(u_w)_n$，同时保上文固定的 $f$。由实际 flat 配对与同源裸最小化，
$$
\mathcal R_n^*e_{f,n}=(L_n+B_n)r_{f,n}.
$$
所以
$$
\boxed{
\operatorname{Re}\langle\mathcal R_nr_{w,n},e_{f,n}\rangle
=
\operatorname{Re}\langle U_nr_{w,n},U_nr_{f,n}\rangle
+
\operatorname{Re}\langle J_{b,n}r_{w,n},J_{b,n}r_{f,n}\rangle .
}
\tag{6.1}
$$
这里 $U_n$ 是同源真实左最小映射，仍有
$U_nr_{z,n}=P_{\mathrm{far}\le n}u_z$，$z=w,f$。没有把输入 $f$ 认作 $W$ 中的向量。

若不作 Riordan 变换，(6.1) 已把原左双线性锚准确变成返回主项，额外裸交叉的总绝对值至多
$$
\nu\,\|P_{\mathcal I_+}u_w\|\,
      \|P_{\mathcal I_+}u_f\|.
\tag{6.2}
$$

在 §5 的参数中，令 $g(C_{\rm s})=\psi_m(C_{\rm s})/(d_0C_{\rm s})$，零点取常项 $1$。既有完整最小化运输给
$$
\left|
\langle\widehat{\mathcal R}_n(g r_{w,n}),\widehat e_{f,n}\rangle
-\langle\mathcal R_nr_{w,n},e_{f,n}\rangle
\right|
\le\mathcal C_0^2\alpha_n(r_{w,n})\|e_{f,n}\|.
\tag{6.3}
$$
这仍保原 $r_{w,n}$ 和原测试端 $f$，未估计返回列的环境范数。

由 (2.3) 的共同平方，
$$
\alpha_n(r_{f,n})^2+\|e_{f,n}\|^2\le\|Y_{f,n}\|^2.
$$
因此对 (6.1)、(6.3) 的两类误差一起用两次 Cauchy，严格得
$$
\boxed{
\begin{aligned}
\left|
\sum_{n\in\mathcal I}\operatorname{Re}
 \langle U_nr_{w,n},U_nr_{f,n}\rangle
-\sum_{n\in\mathcal I}\operatorname{Re}
 \langle\widehat{\mathcal R}_n(g r_{w,n}),\widehat e_{f,n}\rangle
\right|\\
\le
\nu\sqrt{1+\mathcal C_0^4}\,
\|P_{\mathcal I_+}u_w\|\,
\|P_{\mathcal I_+}u_f\|.
\end{aligned}
}
\tag{6.4}
$$
若 $\#\mathcal I\asymp Q$、$h/Q\to0$，归一平均误差趋零，只用
$\|u_w\|\le\|w\|$、$\|u_f\|\le\|f\|$。
也可保真实未来范数；不需要给 $w$ 的尾指定速率。

原合法母窗口中的实际左前缀逼近给：一次取固定
$\|f-w\|\le\|w\|/8$，对充分大 $m$ 以及原同一晚切口集合，(6.1) 的左锚每项实部至少 $7\|w\|^2/16$。因此 (6.4) 的帽返回主项仍保一个非零的线性窗口锚，而其测试端准确满足 (5.4)。这两件事作用在同一个原来源上。

## 7. 精确新增范围

本文新增支付的是：

- 原返回空间的闭和表示 (2.2) 及真实同源测试 $e_{Y,n}=P_{\mathscr E_n}Y_n$；
- 全部切口一起的返回投影后暗矩 (4.2)，仅花重叠数 $\nu$；
- 原实际 Riordan 逆伴随再经 $P_{\widehat{\mathscr E}_n}$ 后的暗矩 (5.4)，含真正缺陷 $\zeta_f$；
- 返回投影之后完整真旗分析列的 (5a.3)–(5a.4)，不增加旗高度因子；
- 同原 $w$ 的完整双线性返回运输 (6.4)。

它们解决的是低暗约束穿过这些实际投影和逆伴随的问题。它们没有证明 $\widehat{\mathcal R}_n^*$、完整 Green 或顺次 MP 在这些低暗测试上的统一费用，也没有把帽系统的全部强位混合删掉。当前剩余问题可准确保留为 (6.4) 的主配对，而不能用“测试范数小”或暗矩小单独取代它。普通 $N=M$ 仍为 OPEN。
