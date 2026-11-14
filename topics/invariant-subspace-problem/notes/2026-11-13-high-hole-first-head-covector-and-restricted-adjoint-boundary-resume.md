# 高孔规范源的首头加权协向量与受限伴随

日期：2026-11-13（UTC）。作者：boundary_resume；AI-assisted，GPT-6 Astra Pro。
状态：以下首头字典及实际 carry 预算已证明，root 与 central_review 已独立全文核验原联合旗、受限最小逆和规范来源；尚未从它重建原高孔左质量。

本笔记承接
[最低头精确分块](2026-11-13-boundary-variation-checkpoint-0c.md) §7、
[左源 Gram](2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)及
[两侧真实源](../results/R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md) §7。
它把[回文四头有限稿](../results/R271-appendix-palindromic-four-head-actual-minimal-sources-and-two-form-nonuniformity.md) §9 的普通单孔测试改写为原高孔层上仍然成立的准确加权形式；不搬用该单孔 gap。

## 1. 首头的原最小逆及全部定义域

固定原 $m\ge5,d=2^m$ 及
$$
4d\le q\le e^{d^3/4}.
$$
令
$$
D_q=D_m|_{\mathcal H_{q+1}}:\mathcal H_{q+1}\longrightarrow\mathcal H_q,
\qquad
E=\ker D_m^{d-1}\cap\mathcal H_q,\qquad
E^+=\ker D_m^d\cap\mathcal H_{q+1}.
$$
[原相容固定层右逆](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md) §§1–3（原权作整数重标）保证 $D_q$ 满射，故其全空间 Moore–Penrose 逆
$$
R_q=D_q^\dagger:\mathcal H_q\longrightarrow\mathcal H_{q+1}
$$
有界。这个有界常数允许依赖 $m,q$，没有先给统一估计。

对 $h\in E$，准确有
$$
D_m^d R_qh=D_m^{d-1}h=0.
$$
所以全空间最小原像已经属于 $E^+$。令
$$
\mathsf D_E=D_q|_{E^+}:E^+\longrightarrow E.
$$
它满射，并且它在原范数中的最小右逆就是 $R_q|_E$。定义
$$
\boxed{
G_D=(R_q|_E)^*(R_q|_E)
=P_E R_q^*R_q|_E
=(\mathsf D_E\mathsf D_E^*)^{-1}>0.
}
\tag{1.1}
$$
这里先在完整孔层取 $R_q$，然后才压到 $E$。最后一个等式用的是已证明的相同最小原像，不是任意交换压缩与逆。

令 $\nu_m=\|D_m\|\le m^{-1}$。因为 $D_qR_qh=h$，
$$
G_D\ge\nu_m^{-2}I_E,\qquad
\|G_D^{-1/2}\|\le\nu_m.
\tag{1.2}
$$
固定参数下 $G_D$ 也有有限上界，所以它及其正平方根在 $E$ 上都是有界可逆的。

它的逆有准确的受限伴随表达：
$$
\mathsf D_E^*h=P_{E^+}D_m^*h,\qquad
\boxed{
\|G_D^{-1/2}h\|
=\|P_{E^+}D_m^*h\|\quad(h\in E).
}
\tag{1.3}
$$
右侧不是不带投影的全环境 $\|D_m^*h\|$。

## 2. 同返回源核中的首头子空间

采用上述两侧真实源稿的原联合旗和正交出生分解。
对输入链 $c=(c_1,\ldots,c_d)$，首源为 $Fc=D_mc_1$，
内部输出为 $(Sc)_t=A_mc_t+D_mc_{t+1}$。
令 $X_{\rm lo}$ 是出生不超过 $1$ 的输入子空间，
$S_{\rm lo}$ 是内部输出到低出生的正交压缩，置
$$
Z=\ker(S_{\rm lo}|_{X_{\rm lo}}),\qquad
\mathcal N=Z\cap\ker F,\qquad
\mathcal U=Z\ominus\mathcal N,\qquad
\mathsf f=F|_{\mathcal U},\qquad
B_A=P_{\rm hi}S|_{\mathcal U}.
$$
这里 $\mathsf f:\mathcal U\to\mathscr R_q$ 是原裸最小链的有界同构；
$B_Aa$ 是该链送入高出生的返回源。

对 $h\in E$，令 $k_h$ 为仅首段非零的链
$$
(k_h)_1=e_0R_qh,\qquad (k_h)_t=0\quad(t\ge2).
\tag{2.1}
$$
由 (1.1) 的核阶，$k_h$ 属于原联合输入旗，并有
$$
Fk_h=e_0h,\qquad Sk_h=0.
$$
任何相同首源的链，其首段第零头分量都必须是 $h$ 的删除原像；因此其范数至少为 $\|R_qh\|$。(2.1) 达到该下界，所以它同时是真正的裸最小链和完整最小链。
特别
$$
k_h\in\mathcal U,\qquad B_Ak_h=0,\qquad
\|k_h\|^2=\langle G_Dh,h\rangle.
\tag{2.2}
$$

取任意真裸最小状态 $a\in\mathcal U$，其首源为 $r=\mathsf f a$。
记首头坐标为
$$
r_0=P_{e_0}r\in E.
$$
因为 $D_q(a_1)_0=r_0$，
$$
(a_1)_0-R_qr_0\in\ker D_q,
\qquad R_qh\perp\ker D_q.
$$
于是对于每个 $h\in E$，
$$
\boxed{
\langle a,k_h\rangle
=\langle R_qr_0,R_qh\rangle
=\langle G_Dr_0,h\rangle.
}
\tag{2.3}
$$
这里没有其他头源造成的首段 primitive 分量：它们与 $R_qh$ 正交。尤其
$$
\|G_D^{1/2}r_0\|=\|R_qr_0\|\le\|a\|.
\tag{2.4}
$$

## 3. 左源 Gram 与准确规范等式

令原左边界映射为
$$
E_q:V_{m,q}\longrightarrow\mathscr R_q,
\qquad E_qv=A_mv_q,
$$
并置
$$
J_{\rm left}=E_qE_q^*>0,\qquad
v=E_q^\dagger r,\qquad y=J_{\rm left}^{-1}r.
$$
首头左协向量为
$$
y_0=P_{e_0}y\in E.
\tag{3.1}
$$
$P_{e_0}$ 是源直和中到首头的正交坐标读取；它不是在左输入中读某一个物理头分量。

按原状态坐标，
$$
\mathcal Q=(E_q^\dagger\mathsf f)^*E_q^\dagger\mathsf f,\qquad
\mathcal D=I+\mathcal Q.
$$
对 $h\in E$，
$$
\langle v,E_q^\dagger(e_0h)\rangle
=\langle y_0,h\rangle.
$$
结合 (2.3)，得到
$$
\boxed{
\langle a,k_h\rangle_{\mathcal D}
=\langle y_0+G_Dr_0,h\rangle.
}
\tag{3.2}
$$
这里及前面内积约定均为第一变量线性。

若 $a$ 满足同返回源的精确规范
$$
a\perp_{\mathcal D}\ker B_A,
$$
则由 $k_h\in\ker B_A$，准确有
$$
\boxed{
y_0=-G_Dr_0,\qquad
\|G_D^{-1/2}y_0\|
=\|G_D^{1/2}r_0\|\le\|a\|.
}
\tag{3.3}
$$
等价地，
$$
\boxed{\|P_{E^+}D_m^*y_0\|\le\|a\|.}
\tag{3.4}
$$
只须对 (2.1) 的首头子空间正交，已经足以得到这些结论；不需要识别整个 $\ker B_A$。

## 4. 原实际状态的规范缺陷也可支付

现在 $a=a_{m,q}(w)$ 来自原 $w\in W=M\ominus N$。
两侧真实源稿 §7 给同源规范状态 $a^\sharp$，满足
$$
e=a-a^\sharp\in\ker B_A,\qquad
\|e\|_{\mathcal D}\le\rho_m\|w\|,
\qquad \rho_m=e^{-72d^4}.
\tag{4.1}
$$
定义
$$
J_{00}=P_{e_0}J_{\rm left}^{-1}|_{e_0E},\qquad
\zeta_0=y_0+G_Dr_0.
$$
$J_{00}$ 按首头坐标视为 $E$ 上的正算子。
映射 $h\mapsto k_h$ 相对于 $\mathcal D$ 的真实 Gram 为
$$
G_D+J_{00}.
$$
由 (3.2) 及 $a^\sharp$ 的规范正交，$\zeta_0$ 恰为这个映射对 $e$ 的协向量。因此极分解的收缩性给
$$
\boxed{
\|(G_D+J_{00})^{-1/2}\zeta_0\|
\le\|e\|_{\mathcal D}
\le\rho_m\|w\|.
}
\tag{4.2}
$$
这个形式不使用任何孔数无关删除逆。

若希望回到 (3.3) 的 $G_D$ 度量，原左塔的已付界
$\|E_q^\dagger\|\le e^{20d^4}$ 给 $J_{00}\le e^{40d^4}I$。
由 (1.2)，
$$
\|G_D^{-1/2}(G_D+J_{00})^{1/2}\|^2
\le1+\nu_m^2e^{40d^4}.
$$
故 (4.2) 及 (2.4) 给
$$
\boxed{
\|G_D^{-1/2}y_0\|
=\|P_{E^+}D_m^*y_0\|
\le\|a\|+2e^{-52d^4}\|w\|.
}
\tag{4.3}
$$
只在最后一步支付一次左塔的成本；没有将高孔的 $R_q$ 普通范数乘到 carry 上。

## 5. 原高孔不存在单孔稿所用的统一 gap

[原权 Vandermonde 构造](../results/R239-appendix-vandermonde-coprimitive-short-kernel-counterexamples.md)给：对任意 $q\ge1$，在前 $2q$ 个真实尾位上有单位向量 $h_q\in\mathcal H_q$，使
$$
D_m^2h_q=0,\qquad
\|D_m^*h_q\|^2=S_{m+2q},
\qquad S_J=\sum_{j\ge J}(j+1)^{-4}.
$$
$d\ge3$ 时 $h_q\in E$，所以相应首头零返回链合法。配对 $D_qR_qh_q=h_q$ 与 $h_q$ 给
$$
\boxed{
\|k_{h_q}\|=\|R_qh_q\|
\ge\frac1{\|D_m^*h_q\|}
=S_{m+2q}^{-1/2}
\ge\sqrt3(m+2q)^{3/2}.
}
\tag{5.1}
$$
最后使用 $S_J\le1/(3J^3)$，原范围 $J\ge1$。

因此不能把回文四头有限稿 §9 中 $D_2D_2^*\ge I$ 的单孔结论搬到这里，也不能由 (4.3) 免费推出 $\|y_0\|\lesssim\|a\|$。

当前已付的新接口是原实际源的 (3.2)、(4.2)、(4.3)。要像有限单孔稿那样重建 $\mu_q(r)$，还须保留这个受限伴随度量、原左核及其余头坐标；本笔记没有完成该左质量重建。
