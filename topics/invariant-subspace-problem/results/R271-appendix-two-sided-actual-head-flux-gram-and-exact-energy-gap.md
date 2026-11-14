# R271 附录：真实窄通量的两侧最小原像及准确 Gram 能量差

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf。
状态：已证明；§§1–8 由 Astra-ISP-1cf8c51d 与 kernel_resume_1cf 全文复核，§9 由 boundary_resume_1cf 与 Astra-ISP-1cf8c51d 核对原完整旗和物理度量。使用原 Hilbert 范数、原合法窗口及实际 $w\in W$；不把窄通量 $\overline f$ 换成旧有效源 $\sigma$ 或返回源。

本文承接[首段先消元稿](R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md) §9.4–9.7 和[左源 Gram 笔记](../notes/2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)。新的对象是原物理空间中具有两侧输入的高输出问题。其最小能量由一个准确 Gram 给出，而真实 $w$ 对有限核的正交直接支付到最小像的距离。原返回费用仍须另估。

## 1. 同一窗口与实际状态坐标

固定 $m\ge5$、$d=2^m$、$4d\le q\le e^{d^3/4}$。原纯模型记为 $L_m=A_m+D_m$，原核与缺陷为 $M=\ker T$、$W=M\ominus N$。所有空间均为既有真实联合旗。

沿首段先消元稿，设
$$
\mathcal U=Z\ominus\mathcal N,\qquad
\mathcal N=\ker\mathsf F,\qquad
\mathsf f=\mathsf F|_{\mathcal U}:\mathcal U\longrightarrow\mathscr R_q,
$$
$$
\mathcal Y_0=\mathcal N\oplus\mathscr X_H,\qquad
\mathcal R_0=(B|_{\mathcal N},S_H):\mathcal Y_0\longrightarrow\mathscr Y_2,
\qquad B_A=B|_{\mathcal U}.
$$
这里 $\mathsf f$ 是固定窗口中的有界同构，$\mathcal R_0$ 满射。记
$$
H^\circ=\mathcal R_0\mathcal R_0^*>0,\qquad
\mathcal T=\mathcal R_0^*(H^\circ)^{-1}B_A,\qquad
\mathscr L=\mathcal T^*\mathcal T\ge0,
$$
$$
\mathcal J_+a=a-\mathcal T a,\qquad
\mathcal P=I+\mathscr L=\mathcal J_+^*\mathcal J_+.
\tag{1.1}
$$
$\mathcal J_+a$ 是源 $\mathsf f a$ 的原完整右最小链。

令
$$
V_{m,q}=\{v\in P_{\le q}^{(m)}H:P_{<q}^{(m)}L_mv=0\},
\qquad E_qv=A_mv_q.
$$
$E_q$ 的真实最小右逆已存在，定义左最小链及其正 Gram
$$
\mathcal J_-=(E_q)^\dagger\mathsf f:\mathcal U\longrightarrow V_{m,q},
\qquad
\mathcal Q=\mathcal J_-^*\mathcal J_->0,\qquad
\mathcal D=I+\mathcal Q.
\tag{1.2}
$$
于是 $\|\mathcal J_-a\|=\mu_q(\mathsf f a)$，且
$\operatorname{supp}\mathcal J_-a\subset[0,q]$。
$\mathcal Q$ 是左源 Gram 的准确状态坐标，$\mathcal P$ 是完整右源的状态度量；不假设它们交换。

## 2. 两侧物理输入域及真正的高源 Gram

在 $\mathcal U\oplus\mathcal Y_0$ 上使用明确的 Hilbert 内积
$$
\|(a,y)\|_{\mathcal D\oplus I}^2
=\langle\mathcal D a,a\rangle+\|y\|^2.
$$
定义原物理空间中的嵌入
$$
\boxed{\mathcal I(a,y)=\mathcal J_-a-a-y.}
\tag{2.1}
$$
左链在 $\le q$ 孔层，右侧 $a+y$ 在 $[q+1,q+d]$；
并且 $a\perp y$。所以
$$
\boxed{
\|\mathcal I(a,y)\|^2
=\|\mathcal J_-a\|^2+\|a\|^2+\|y\|^2
=\|(a,y)\|_{\mathcal D\oplus I}^2.
}
\tag{2.2}
$$
$\mathcal D\ge I$ 有界可逆，故该加权空间完备，$\mathcal I$ 是等距嵌入，其像 $\mathscr E_q$ 为原 Hilbert 空间中的闭子空间。

完整 $L_m$ 方程也准确。左输入只在第 $q$ 孔层产生 $\mathsf f a$；
右输入的首输出为相同的 $\mathsf f a$，因为 $F_qy=0$。
两者相消。低出生内部输出都为零，剩余内部高输出为
$-(B_Aa+\mathcal R_0y)$。最上端 $A_mc_d=0$ 已由联合旗保证。因此
$$
\boxed{
L_m\mathcal I(a,y)
=-\iota_2\mathcal B(a,y),\qquad
\mathcal B(a,y)=B_Aa+\mathcal R_0y,
}
\tag{2.3}
$$
其中 $\iota_2$ 是 $\mathscr Y_2$ 到原孔层空间的正交包含。
输出支撑只在 $[q+2,q+d-1]$，没有遗漏首端或末端方程。

$\mathcal B$ 满射，因为 $\mathcal R_0$ 满射。它相对于 (2.2) 的真实伴随是
$$
\mathcal B^\sharp z
=(\mathcal D^{-1}B_A^*z,\mathcal R_0^*z).
$$
故两侧高源的准确 Gram 为
$$
\boxed{
H^{\rm two}:=\mathcal B\mathcal B^\sharp
=H^\circ+B_A(I+\mathcal Q)^{-1}B_A^*>0.
}
\tag{2.4}
$$
对任意 $f\in\mathscr Y_2$，有
$$
\boxed{
\inf_{\substack{x\in\mathscr E_q\\L_mx=-\iota_2f}}\|x\|^2
=\langle(H^{\rm two})^{-1}f,f\rangle.
}
\tag{2.5}
$$
这是原物理范数中的最小值，不是对既有高块作普通压缩。
旧末块为 $H^{\rm old}=H^\circ+B_AB_A^*$，所以
$$
H^\circ\le H^{\rm two}\le H^{\rm old},
\qquad
(H^{\rm old})^{-1}\le(H^{\rm two})^{-1}\le(H^\circ)^{-1}.
\tag{2.6}
$$

## 3. 完整核的正交图分解

由 $\mathcal R_0\mathcal T=B_A$，
$$
\ker\mathcal B
=\{(b,-\mathcal T b):b\in\mathcal U\}
\mathbin{\oplus^\perp}
\bigl(\{0\}\oplus\ker\mathcal R_0\bigr).
\tag{3.1}
$$
正交在 $\mathcal D\oplus I$ 中成立，因为
$\operatorname{Ran}\mathcal T\subset\operatorname{Ran}\mathcal R_0^*
=(\ker\mathcal R_0)^\perp$。图的准确度量是
$$
\mathcal D+\mathscr L=\mathcal Q+\mathcal P\ge I.
\tag{3.2}
$$
这个逆始终有界；没有对可能有核的 $\mathscr L$ 取逆。

现在取原 $w\in W$，使用首段先消元稿的同一个实际输入
$$
a=\mathcal A_qw,\qquad
g=u+\widehat a,\qquad
\overline u=-a+g,\qquad
S_qg=B_Aa-\overline f.
$$
$g\in\mathcal Y_0$，故最后一式就是
$\mathcal R_0g=B_Aa-\overline f$。定义
$$
\eta=\mathcal J_+^*\overline u=-a-\mathcal T^*g,\qquad
k=P_{\ker\mathcal R_0}g,\qquad
b=\mathcal Q a-\eta.
\tag{3.3}
$$
向量 $z=(a,-g)$ 具有准确源
$$
\mathcal Bz=\overline f,\qquad
\mathcal I z=\mathcal J_-a+\overline u.
\tag{3.4}
$$
它对 (3.1) 第一项的图协向量是
$$
\mathcal D a+\mathcal T^*g=\mathcal Q a-\eta=b.
$$
所以令
$$
t=(\mathcal Q+\mathcal P)^{-1}b,
$$
便有准确的加权核投影
$$
\boxed{
P_{\ker\mathcal B}^{\sharp}z=(t,-\mathcal T t-k),
\qquad
\|P_{\ker\mathcal B}^{\sharp}z\|_{\mathcal D\oplus I}^2
=\langle(\mathcal Q+\mathcal P)^{-1}b,b\rangle+\|k\|^2.
}
\tag{3.5}
$$
上标只提醒使用 (2.2) 的原物理等距度量，不是改变原范数。

结合 (2.5)，Pythagoras 准确给
$$
\boxed{
\begin{aligned}
\mu_q(r)^2+\|\overline u\|^2
={}&\|\overline f\|_{(H^{\rm two})^{-1}}^2\\
&+\langle(\mathcal Q+\mathcal P)^{-1}
(\mathcal Q a-\eta),\mathcal Q a-\eta\rangle
+\|k\|^2,
\end{aligned}
}
\tag{3.6}
$$
其中 $r=\mathsf f a$。所有源和向量均来自同一个原 $w$。

## 4. 原 W 正交直接支付整个平方差

本节不先放大 $\eta-\mathcal Qa$ 的普通范数。
记原已付参数
$$
\delta=e^{-74d^4},\qquad
\delta_r=12e^{-73d^4},\qquad
\epsilon=e^{-75d^4},\qquad
\rho=e^{-72d^4}.
$$
原宽窗输入和同源校正满足
$$
\|u-P_{\mathscr C_q}w\|\le\delta\|w\|,
\qquad
\|\widehat a-a\|\le\delta_r\|w\|.
\tag{4.1}
$$
令 $v=P_{V_{m,q}}w$。左最小链的正交性给
$$
v-\mathcal J_-a\in\ker E_q,\qquad
v-\mathcal J_-a\perp\operatorname{Ran}\mathcal J_-.
\tag{4.2}
$$

置 $x=\mathcal Iz=\mathcal J_-a+\overline u$。
对任意 $x'=\mathcal I(a',y')\in\mathscr E_q$，
左侧配对准确消失：
$$
\langle w-\mathcal J_-a,\mathcal J_-a'\rangle=0.
$$
右侧只读 $\mathscr C_q$，由 (4.1) 及
$\overline u=u+\widehat a-a$，
$$
|\langle w-x,x'\rangle|
\le(\delta+\delta_r)\|w\|\,\|a'+y'\|
\le(\delta+\delta_r)\|w\|\,\|x'\|.
$$
因此
$$
\boxed{
\|P_{\mathscr E_q}w-x\|
\le(\delta+\delta_r)\|w\|.
}
\tag{4.3}
$$
这里没有乘左链 $e^{20d^4}$ 或一般完整右逆的成本。

由 (2.3)，$\mathcal I(\ker\mathcal B)$ 是支持在
$[0,q+d]$ 的完整 $L_m$ 核。原同窗 lift 将每个这样的向量送入
$N$，相对误差至多 $\epsilon$；支持仍满足原
$q+d\le e^{d^3/3}$，没有扩大窗口。
原 $w\perp N$ 因而给
$$
\|P_{\mathcal I(\ker\mathcal B)}w\|\le\epsilon\|w\|.
$$
将 (4.3) 再投到这个核，并使用 $\mathcal I$ 等距，得到
$$
\boxed{
\|P_{\ker\mathcal B}^{\sharp}z\|_{\mathcal D\oplus I}
\le(\delta+\delta_r+\epsilon)\|w\|
\le\rho\|w\|.
}
\tag{4.4}
$$
最后一步对 $d\ge32$ 直接成立。
所以 (3.6) 的整个非负平方差有真正的实际预算
$$
\boxed{
\begin{aligned}
0\le{}&
\mu_q(r)^2+\|\overline u\|^2
-\|\overline f\|_{(H^{\rm two})^{-1}}^2\\
={}&
\|(\mathcal Q+\mathcal P)^{-1/2}(\mathcal Qa-\eta)\|^2+\|k\|^2
\le e^{-144d^4}\|w\|^2.
\end{aligned}
}
\tag{4.5}
$$

## 5. 同一个实际高源在新旧度量中的准确能量差

首段先消元稿 §9.6.D 的原三正交分解给
$$
\|\overline u\|^2
=\lambda_q(r_q^{\rm small})^2
+\|\overline f\|_{(H^{\rm old})^{-1}}^2+\|k\|^2.
\tag{5.1}
$$
将 (5.1) 从 (3.6) 中相消，得到
$$
\boxed{
\begin{aligned}
&\|\overline f\|_{(H^{\rm two})^{-1}}^2
-\|\overline f\|_{(H^{\rm old})^{-1}}^2\\
&\quad=
\mu_q(r)^2+\lambda_q(r_q^{\rm small})^2
-\|(\mathcal Q+\mathcal P)^{-1/2}(\mathcal Qa-\eta)\|^2.
\end{aligned}
}
\tag{5.2}
$$
左侧非负也直接由 (2.6) 验证。
注意 $\|k\|^2$ 在这个准确差中已经相消，不能再额外扣除一次。

若固定 $0\ne w\in W$，沿 $m\to\infty$、任取原合法的 $q=q_m$，
既有低投影及未来带性质给
$$
\mu_q(r)\longrightarrow\|w\|,\qquad
\|\overline u\|,\lambda_q(r_q^{\rm small})
\le\beta_q^\circ(w)\longrightarrow0.
$$
由 (4.5)、(5.1)，因此
$$
\boxed{
\|\overline f\|_{(H^{\rm two})^{-1}}^2\longrightarrow\|w\|^2,
\qquad
\|\overline f\|_{(H^{\rm old})^{-1}}^2\longrightarrow0.
}
\tag{5.3}
$$
这是对假定存在的原非零 $W$ 向量的必要性质，不是其存在性证明。
它明确说明不能把两侧左源费用从新 Gram 中删除。
本文没有给新旧度量在这一实际源上的统一比较，因而 (5.3) 不构成矛盾。

## 6. 准确两侧最优状态及原返回费的可付校正

(3.5) 的最小原像是 $z_{\min}=z-P_{\ker\mathcal B}^{\sharp}z$。
其第一分量
$$
a_{\rm two}=a-t
$$
满足两个准确公式
$$
\boxed{
a_{\rm two}
=(I+\mathcal Q)^{-1}B_A^*(H^{\rm two})^{-1}\overline f
=(\mathcal Q+\mathcal P)^{-1}
B_A^*(H^\circ)^{-1}\overline f.
}
\tag{6.1}
$$
第一式来自 $\mathcal B^\sharp(H^{\rm two})^{-1}\overline f$。
第二式可由
$\eta=-\mathcal P a+B_A^*(H^\circ)^{-1}\overline f$
代入 $b=\mathcal Qa-\eta$ 得到；它也是真正的有界 Woodbury 恒等式。

(4.5) 给
$$
\boxed{
\|a-a_{\rm two}\|_{\mathcal Q+\mathcal P}
\le\rho\|w\|.
}
\tag{6.2}
$$
若 $r_{\rm two}=\mathsf f a_{\rm two}$，
原左右最小链因而都只改变已付小量：
$$
\lambda_q(r-r_{\rm two}),\ \mu_q(r-r_{\rm two})
\le\rho\|w\|.
\tag{6.3}
$$
这里 $\mathcal P$、$\mathcal Q$ 都被 $\mathcal P+\mathcal Q$ 控制，未交换两者。

原返回源在状态上仍是 $\mathsf f\mathscr L a$。
若使用[全部孔数高旗稿](R271-appendix-all-hole-high-birth-right-inverse-and-return-energy.md)
的真实界 $\|\mathscr L\|\le k_m$，则
$$
\boxed{
\lambda_q\!\left(
r_{\rm ret}(r)-r_{\rm ret}(r_{\rm two})
\right)
\le k_m\rho\|w\|.
}
\tag{6.4}
$$
确实，$\mathscr L$ 与 $\mathcal P=I+\mathscr L$ 交换，故
$\|\mathcal P^{1/2}\mathscr L t\|
\le k_m\|\mathcal P^{1/2}t\|$。
用 $k_m\le m^{-2}e^{40d^4}$，(6.4) 至多为
$e^{-32d^4}\|w\|$。在原合法窗口用已有更好常数还可改善此误差。
这只支付换到 (6.1) 的代价；没有给原返回源本身的上界。

## 7. 保原高对偶的同源极小化也有 e^{-72d^4} 费用

令
$$
\mathcal K_0=\ker\mathscr L=\ker B_A.
$$
$\{(e,0):e\in\mathcal K_0\}$ 是 $\ker\mathcal B$ 的闭子空间。
因此 (4.4) 同样控制到该子空间的加权正交投影。
具体地，置
$$
D_0=P_{\mathcal K_0}(I+\mathcal Q)|_{\mathcal K_0}\ge I,\qquad
e=D_0^{-1}P_{\mathcal K_0}(I+\mathcal Q)a,\qquad
a^\sharp=a-e.
$$
则
$$
\boxed{
\|e\|_{I+\mathcal Q}\le\rho\|w\|,\qquad
a^\sharp
=\arg\min_{B_Au=B_Aa}
\left(\|u\|^2+\mu_q(\mathsf f u)^2\right).
}
\tag{7.1}
$$
这是[左源笔记的零返回方向校正](../notes/2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)
在原物理核投影下的更直接预算；只反演 $D_0\ge I$，
不要求 $B_A$ 闭像，也不反演 $\mathscr L$。

因为 $\mathscr L e=B_Ae=0$，替换 $a$ 为 $a^\sharp$ 时，
原 $r_{\rm ret}$、$z_2=(H^\circ)^{-1}B_Aa$、旧有效源
$\sigma=H^{\rm old}z_2$、旧末块能量及窄头通量全部准确保留。
对应左右源改变的最小费用均至多 $\rho\|w\|$。
这给了一个合法且更窄的实际源类，仍没有该类上的返回费用上界。

## 8. 剩余目标

新的 $H^{\rm two}$ 由一个明确的原物理输入空间产生。
(4.5) 支付真实 $\overline f$ 的两侧最小能量损失，
(5.2) 保留原左源费用，(6.1) 与 (7.1) 给两种准确、代价已付的源规范化。

但 $\overline f$ 仍是原真实未来带产生的窄通量。
本文不将其替成旧 $\sigma$，不把新 Gram 当作旧末块，
也不据 (5.3) 的必要增长宣布无权结论。
下一项仍是使用该真实窄来源估计
$\|\overline f\|_{(H^{\rm two})^{-1}}$ 或 (6.1)/(7.1) 上的返回费用；
普通复 Hilbert ISP 及原 $N=M$ 继续开放。

后续已付的具体充分门槛见[实际源二形式比例与同头全部窗口](R271-appendix-actual-source-two-form-ratios-and-legal-window-summation-threshold.md)：只需原源上的〈La,a〉/〈(I+Q)a,a〉在同头窗口满足相应倒数求和条件；均匀 O(e^(d³/4)/d) 的头子序列已足够。这个比较仍未证明。

## 9. 两侧真实 Gram 的完整降孔与原窄通量交织

日期：2026-11-13（UTC）。本节继续 §§1–7 的同一原物理空间；所有相邻窗口共享头 $m$，并要求
$$
4d\le q,\qquad q+1\le e^{d^3/4},\qquad d=2^m,\quad m\ge5.
$$
所用 $C=D_{3,m}$、$X=X_{3,m}$ 满足
$$
\|C\|,\|X\|\le s_3,\qquad
\|X-C\|\le s_3e^{-770d^4},\qquad
X M\subset N,
\qquad s_3=\sum_{j\ge m}(j+1)^{-6}.
\tag{9.1}
$$
这是[首段先消元稿](R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md) §6 的实际 $X$，不是把纯 $Cw$ 当成 $M$ 中向量。

本节的新对象是 §2 的两侧 Gram $H^{\rm two}$ 和实际窄源 $\overline f$。完整最小链已有的“降孔后再取最小原像”原理只作为依赖，不另登记一般投影引理；下面支付左端最小链产生的额外有限核，并核实真实 $\overline f$ 的交织没有未来带主项。

### 9.1 右输入的完整三角块及左端缺陷

对 $a'\in\mathcal U_{q+1}$，沿首段先消元稿 §9.2 写
$$
C_{\mathscr C,q}a'=\mathsf U_qa'+\mathsf J_qa',
\qquad
\mathsf U_qa'\in\mathcal U_q,\quad
\mathsf J_qa'\in\mathcal Y_{0,q}.
$$
这里 $\mathsf J_qa'$ 同时包含低链的 $\mathcal N_q$ 分量和跨入高出生的分量，不能只留其中一项。若 $y'\in\mathcal Y_{0,q+1}$，完整降孔给
$$
C_{\mathscr C,q}y'\in\mathcal Y_{0,q}.
$$
理由是 $C$ 保持高出生输入；对原 $\mathcal N_{q+1}$，它保持零首段边界，且完整 $S$ 交织保证其低输出仍为零。记其限制为 $\mathsf V_q$。于是
$$
C_{\mathscr C,q}
\binom{a'}{y'}
=
\begin{pmatrix}\mathsf U_q&0\\
\mathsf J_q&\mathsf V_q\end{pmatrix}
\binom{a'}{y'}.
\tag{9.2}
$$
所有输入均用原正交分解；不让正交投影与 $C$ 交换。

左输入也可完整读取。若 $v\in V_{m,q+1}$，则 $Cv\in V_{m,q}$，且
$$
E_qCv=C_{\mathscr R,q}E_{q+1}v.
$$
事实上 $C$ 降低一个孔层，且与 $L_m$ 交换。又
$$
\mathsf f_q\mathsf U_q=C_{\mathscr R,q}\mathsf f_{q+1}.
$$
所以
$$
\boxed{
C\mathcal J_{-,q+1}a'
=\mathcal J_{-,q}\mathsf U_qa'+k_-(a'),
\qquad k_-(a')\in\ker E_q.
}
\tag{9.3}
$$
$k_-(a')$ 与 $\operatorname{Ran}\mathcal J_{-,q}$ 正交；它支持在 $[0,q]$，并且 $L_mk_-(a')=0$。因此它还与整个 $\mathscr E_q$ 正交。最后一个判断同时用了左链最小性和左右孔支撑，不能仅由 $L_mk_-=0$ 推出。

### 9.2 加权输入上的真实收缩及两侧逆 Gram

以 $\mathcal D_q=I+\mathcal Q_q$ 定义加权输入输运
$$
\mathsf T_q(a',y')
=(\mathsf U_qa',\,\mathsf J_qa'+\mathsf V_qy').
$$
由 (9.2)、(9.3) 及 §2 的实际等距嵌入，
$$
\boxed{
C\mathcal I_{q+1}(a',y')
=\mathcal I_q\mathsf T_q(a',y')+k_-(a').
}
\tag{9.4}
$$
两项在原 Hilbert 空间中正交。故有完整平方恒等和上界
$$
\boxed{
\begin{aligned}
&\|\mathsf T_q(a',y')\|_{\mathcal D_q\oplus I}^2
+\|k_-(a')\|^2\\
&\quad=\|C\mathcal I_{q+1}(a',y')\|^2
\le s_3^2\|(a',y')\|_{\mathcal D_{q+1}\oplus I}^2.
\end{aligned}
}
\tag{9.5}
$$
这同时支付了左源度量，不能只用原未加权右输入的收缩替代。

$C$ 保持高输出旗，记其限制为 $C_{22,q}$。对 (9.4) 应用 $L_m$，用 (2.3) 及 $L_mk_-=0$，得到
$$
\boxed{
\mathcal B_q\mathsf T_q=C_{22,q}\mathcal B_{q+1}.
}
\tag{9.6}
$$
因此将下一窗的最小原像经 $\mathsf T_q$ 输运，给出
$$
\boxed{
C_{22,q}^*(H_q^{\rm two})^{-1}C_{22,q}
\le s_3^2(H_{q+1}^{\rm two})^{-1}.
}
\tag{9.7}
$$
此式是 $H^{\rm two}$ 的真实最小原像能量比较。它不将 $H^\circ$ 或 $H^{\rm old}$ 的不等式直接换名，也没有交换 $\mathcal Q$ 与任何 Schur 逆。

### 9.3 最小物理原像的正交亏损恰为有限核

对任意 $f\in\mathscr Y_{2,q}$，记
$$
\mathscr K_q f
=\mathcal I_q\mathcal B_q^\sharp(H_q^{\rm two})^{-1}f
\in\mathscr E_q.
$$
于是
$$
L_m\mathscr K_qf=-\iota_2f,\qquad
\|\mathscr K_q f\|=\|f\|_{(H_q^{\rm two})^{-1}}.
$$
取 $f'\in\mathscr Y_{2,q+1}$，并写
$$
z'=\mathcal B_{q+1}^\sharp(H_{q+1}^{\rm two})^{-1}f',
\qquad
z=\mathcal B_q^\sharp(H_q^{\rm two})^{-1}C_{22,q}f'.
$$
由 (9.6)，$\mathsf T_qz'-z\in\ker\mathcal B_q$。又 $z$ 与该核正交，因此
$$
\boxed{
k_q(f')
:=C\mathscr K_{q+1}f'-\mathscr K_qC_{22,q}f'
=\mathcal I_q(\mathsf T_qz'-z)+k_-(a')
\in\ker L_m.
}
\tag{9.8}
$$
它支持在 $[0,q+d]$。式 (9.3) 的左核项与第一项正交，而这两项都与 $\mathscr K_qC_{22,q}f'$ 正交。所以
$$
\boxed{
\begin{aligned}
\|k_q(f')\|^2
&=\|C\mathscr K_{q+1}f'\|^2
-\|C_{22,q}f'\|_{(H_q^{\rm two})^{-1}}^2\\
&\le s_3^2\|f'\|_{(H_{q+1}^{\rm two})^{-1}}^2
-\|C_{22,q}f'\|_{(H_q^{\rm two})^{-1}}^2.
\end{aligned}
}
\tag{9.9}
$$
所有项都是真实正范数。$q+d\le e^{d^3/3}$ 仍在原有限核 lift 窗内，故
$$
\boxed{
\|P_W k_q(f')\|
\le e^{-75d^4}\|k_q(f')\|
\le s_3e^{-75d^4}
\|f'\|_{(H_{q+1}^{\rm two})^{-1}}.
}
\tag{9.10}
$$
这里仅付 $W$ 投影；未把 $k_q$ 的整个范数宣布为进位小量。

### 9.4 实际窄源的交织只有已付 carry

$\overline f_q(\xi)$ 的原构造对全部 $\xi\in M$ 都是线性的，无需先限制到 $W$。明确写作
$$
f_q(\xi)_t
=H_t\bigl(P_{V_{m,q+d}}\xi\bigr)_{q+t},
\qquad
\overline f_q(\xi)
=f_q(\xi)-B_{A,q}
\bigl(\widehat a_q(\xi)-a_q(\xi)\bigr).
\tag{9.11}
$$
$H_t$ 是[联合旗稿 §6](R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)的纯头算子
$$
H_t=P_{W_{d-t}}A_m(I-P_{W_{d-t+1}}),\qquad
\sup_t\|H_t\|\le6.
$$
所以它与尾算子 $C$ 精确交换；没有加入未知的删除核投影。原宽低投影及 (9.1) 给
$$
\|P_{V_{m,q+d}}X\xi
-C P_{V_{m,q+d+1}}\xi\|
\le3s_3e^{-74d^4}\|\xi\|.
\tag{9.12}
$$
此处同头的两次宽投影都满足原 $\log(2+R)\le d^3$ 预算；正是 $q+1$ 合法假设的用途。由直和范数而非逐段相加，
$$
\|f_q(X\xi)-C_{22,q}f_{q+1}(\xi)\|
\le18s_3e^{-74d^4}\|\xi\|.
\tag{9.13}
$$

另一方面，原同源修正给
$$
\|\widehat a_q(\zeta)-a_q(\zeta)\|
\le12e^{-73d^4}\|\zeta\|\qquad(\zeta\in M).
$$
已证 $\|B_{A,q}\|\le\nu_m:=\|D_m\|\le m^{-1}<1$。用 $\|X\xi\|\le s_3\|\xi\|$ 与 $\|C_{22,q}\|\le s_3$，两项修正的差因而至多为
$$
24\nu_m s_3e^{-73d^4}\|\xi\|.
$$
结合 (9.13)，得到普通范数预算
$$
\|\overline f_q(X\xi)
-C_{22,q}\overline f_{q+1}(\xi)\|
\le42s_3e^{-73d^4}\|\xi\|.
\tag{9.14}
$$
原合法窗内 $H_q^{\rm two}\ge H_q^\circ\ge e^{-2d^4}I$，所以
$$
\boxed{
\|\overline f_q(X\xi)
-C_{22,q}\overline f_{q+1}(\xi)\|_{(H_q^{\rm two})^{-1}}
\le s_3e^{-71d^4}\|\xi\|.
}
\tag{9.15}
$$
这条式子没有未来带 $\beta_q$ 主项；它针对同一个真实窄通量的提取。它也没有把 $\overline f_q(X\xi)$ 换成 $\overline f_q(\xi)$。

### 9.5 原核上有界的两侧最小提取与真实 W 投影

定义
$$
\mathfrak K_q:M\longrightarrow H,\qquad
\mathfrak K_q\xi=\mathscr K_q\overline f_q(\xi).
$$
§4.3 的配对证明仅用低投影和左最小性，对任意 $\xi\in M$ 仍给
$$
\|P_{\mathscr E_q}\xi
-\mathcal I_q(a_q(\xi),-g_q(\xi))\|
\le(\delta+\delta_r)\|\xi\|,
\quad
\delta=e^{-74d^4},\quad\delta_r=12e^{-73d^4}.
$$
到最小像只需再投到
$$
\mathscr G_q
=\mathscr E_q\ominus\mathcal I_q(\ker\mathcal B_q).
$$
因此有算子范数结论
$$
\boxed{
\|\mathfrak K_q-P_{\mathscr G_q}|_M\|
\le\delta+\delta_r,
\qquad
\|\mathfrak K_q\|\le1+\delta+\delta_r.
}
\tag{9.16}
$$
这是原 Hilbert 空间中一个正交投影的近似，不依赖某个昂贵全源逆；两侧像能量准确为
$\|\mathfrak K_q\xi\|^2
=\|\overline f_q(\xi)\|_{(H_q^{\rm two})^{-1}}^2$。

将 (9.8) 用于 $f'=\overline f_{q+1}(\xi)$，再用 (9.15)，得到
$$
\mathfrak K_qX\xi-C\mathfrak K_{q+1}\xi
=-k_q(\overline f_{q+1}(\xi))
+\mathscr K_q\bigl(
\overline f_q(X\xi)-C_{22,q}\overline f_{q+1}(\xi)\bigr).
$$
所以 (9.10)、(9.15)、(9.16) 给
$$
\boxed{
\|P_W(\mathfrak K_qX_M
-C\mathfrak K_{q+1})\|_{M\to H}
\le s_3e^{-70d^4}.
}
\tag{9.17}
$$
第一项的 $W$ 投影已由有限核提升支付，第二项则使用真实 $H^{\rm two}$ 逆度量。式中保留了 $P_W$，没有无证交换 $P_M$ 或 $\mathfrak K_q$ 与 $X$。

对于 $w\in W$，§§4–5 仍给 $\mathfrak K_qw$ 的原两侧能量趋于 $\|w\|^2$；(9.17) 没有将 $X_Mw\in N$ 自动变成 $\mathfrak K_qX_Mw\in N$。当前缺口仍是实际源上的两形式比较或窄通量的新度量上界，本节不从这些正确运输式推出未付的原像预算。

