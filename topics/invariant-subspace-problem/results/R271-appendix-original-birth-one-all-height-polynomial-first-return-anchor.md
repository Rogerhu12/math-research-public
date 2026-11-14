# R271 附录：原连续尾出生一的全高度精度夹逼与多项式第一返回锚

日期：2026-11-14 UTC。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 对原连续权 $b_i=(i+1)^{-2}$，本文在整个出生一 primitive 空间、全部高度上给出真幂 MP Gram 的显式多项式条件数；继而支付第一下降伴随的所有旧列。结论对原 $m,q$ 一致，不把任意正权的标量 Newton 提升为非交换矩阵 Newton。最高层 $h=d=2^m$ 没有新增头列，故原出生一的 $D_1^*$ 顶部锚费用至多 $(d+2)^{61/2}\sqrt{S_m}$。

协方差精度和正边权本身已经见于 [任意出生倒数权对偶 §7](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)，出生一首处相邻边已见于 [全任意正权首边定理及原无限尾延拓](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)。本文的新内容是利用原连续权付清**全部高度**的标量夹逼与 $D_1^*$ 旧列比较；不把已有协方差身份重计为新结论。

依赖的实际两带、真 MP 字典和顶锚为 [Boolean 三次权桥与最高正锚](R239-appendix-boolean-cubic-mp-bridge-top-layer-anchor-and-polynomial-top-cost.md)。一般出生 $a\ge2$、$\Gamma^{-1}$ 的跨出生传播及边界 $N=M$ 仍未由本文解决。

## 1. 原空间与结论

固定 $m\ge1$，置
$$
x=m+1,\qquad b_i=(i+1)^{-2}\quad(i\ge m),\qquad
w_i=b_i^2,\qquad S=S_m=\sum_{i\ge m}w_i.
$$
原删除为 $D=\sum_{i\ge m}b_iE_i$，其完整物理范数记为 $\nu=\|D\|\le1/m$。特别
$$
S=\|D:\mathcal H_1\to\mathcal H_0\|^2\le\nu^2,
\qquad S\le\frac1{3m^3}.
\tag{1.1}
$$
在原 $\mathcal H_1=\ell^2(\{i\ge m\})$ 上，记
$$
b=(b_i),\qquad K=K_1=b^\perp,
\qquad
J_t=(D^t:\mathcal H_{t+1}\to\mathcal H_1)^\dagger|_K,
\qquad H_t=J_t^*J_t,\quad H_0=I_K.
\tag{1.2}
$$
以下所有 Gram 都是先取完整层上的真幂逆，再压 $K$。

令 $e_t=e_t(w)$，约定 $e_0=1$、$e_{-1}=0$，并定义正标量
$$
\tau_t=(t!)^2S\,\frac{e_t^2}{e_{t+1}}\quad(t\ge0).
\tag{1.3}
$$
特别 $\tau_0=1$。

**定理 1（全高度精度夹逼）。** 对每个整数 $t\ge0$，
$$
\boxed{\frac{\tau_t}{(t+1)^{17}}I_K
\preceq H_t^{-1}\preceq\tau_tI_K.}
\tag{1.4}
$$
对 $t\ge1$，
$$
\boxed{\frac{S}{(t+1)^2}
\le\frac{\tau_t}{\tau_{t-1}}
\le(t+1)(t+2)^3S.}
\tag{1.5}
$$

**定理 2（正出生一的全部旧列）。** 对整数 $h\ge1$ 及 $1\le\ell\le h$，
$$
\boxed{
H_{h-1}H_h^{-1}H_\ell H_h^{-1}H_{h-1}
\preceq
h^{34}(h+1)^2(h+2)^6(\ell+1)^{19}S\,H_{\ell-1}
\preceq(h+2)^{61}S\,H_{\ell-1}.}
\tag{1.6}
$$
这里所有乘积次序保留，没有交换不同 $H_t$。

若 $y\in W_{h,h}=J_{h-1}K$ 是原出生一、高度 $h$ 的向量，则对任意非负标量列权 $c_0,\ldots,c_{h-1}$，
$$
\boxed{
\sum_{j=0}^{h-1}c_j^2\|D_1^jD_1^*y\|^2
\le(h+2)^{61}S
\sum_{j=0}^{h-1}c_j^2\|D_1^jy\|^2.}
\tag{1.7}
$$
$D_1^*$ 在这里是无限高度出生商的伴随；出生一保留在任何合法 $q\ge0$ 的该商内。

## 2. 完整无限层 Gram 与真实 Schur 精度

固定 $t\ge0$，在 $\mathcal H_1$ 上定义
$$
F_t=\frac{D^t(D^*)^t}{(t!)^2}.
$$
固定孔层的界 $\|D_p\|\le\sqrt{pS}$ 保证它有界。对原物理基直接展开，
$$
(F_t)_{ii}=e_t(w_{\ne i}),\qquad
(F_t)_{ij}=b_ib_j e_{t-1}(w_{\ne i,j})\quad(i\ne j).
\tag{2.1}
$$
对 $t=0$，第二式为零。

这些完整算子均有有界逆。确实，对角差
$e_t(w_{\ne i})-e_t=-w_ie_{t-1}(w_{\ne i})$ 趋零；非对角部分满足
$$
\sum_{i\ne j}|(F_t)_{ij}|^2
\le e_{t-1}^2S^2<\infty\quad(t\ge1).
$$
所以 $F_t=e_tI+\text{紧算子}$。它没有核：若 $(D^*)^tf=0$，则对每个大小 $t+1$ 的有限集合 $I$，
$$
\sum_{i\in I}\frac{f_i}{b_i}=0.
$$
交换两个坐标、保持其余 $t$ 个不同指标，可知所有 $f_i/b_i$ 相同，再代回任意一个集合得它们全零。$t=0$ 直接成立。于是正 Fredholm 算子 $F_t$ 可逆。因此
$$
H_t=(t!)^{-2}P_KF_t^{-1}|_K
\tag{2.2}
$$
确为正且有界可逆的真 MP Gram。

设 $u_i=b_i e_t(w_{\ne i})$。逐集合计数给
$$
F_tb=(t+1)u,\qquad b^*F_tb=(t+1)^2e_{t+1}.
$$
在完整空间按 $\mathbb Cb\oplus K$ 作 Schur 消元，得到
$$
C_t=F_t-\frac{uu^*}{e_{t+1}},\qquad
C_tb=0,\qquad
H_t^{-1}=(t!)^2C_t|_K.
\tag{2.3}
$$
这一步没有把压缩与逆交换。

记 $e_r^{ij}=e_r(w_{\ne i,j})$。代入 (2.1) 并展开 $e_{t+1}$，非对角项准确为
$$
(C_t)_{ij}=-b_ib_j\,\frac{(e_t^{ij})^2-e_{t+1}^{ij}e_{t-1}^{ij}}{e_{t+1}}.
\tag{2.4}
$$
$C_tb=0$ 决定对角项。因此对任意 $f\in\ell^2$，
$$
\boxed{
\langle H_t^{-1}f,f\rangle
=(t!)^2\sum_{i<j}
\frac{(e_t^{ij})^2-e_{t+1}^{ij}e_{t-1}^{ij}}{e_{t+1}}
\,|b_jf_i-b_if_j|^2,\quad f\in K.}
\tag{2.5}
$$
这是已有的准确正网络形式在本文记号下的表达。

所有无限和都有直接的有界二次型意义：分子非负且至多 $e_t^2$，而
$$
\sum_{i<j}|b_jf_i-b_if_j|^2=S\|f\|^2-|\langle f,b\rangle|^2.
\tag{2.6}
$$
故有限对和单调收敛到有界正形式。式 (2.4) 的每一行与 $b$ 的乘积绝对收敛，由 $C_tb=0$ 核对对角项；先对有限支撑 $f$，再按 (2.6) 连续延拓即得 (2.5)。不需要把无限对角 $\operatorname{diag}(b_i)^{-1}$ 当成有界算子，也不需要用截断模型的 MP 逆冒充原逆。

## 3. 删除有限位置后的原权初等比

写
$$
S_y=\sum_{n=y}^{\infty}n^{-4}\quad(y\ge2).
$$
积分比较给
$$
\frac1{3y^3}\le S_y\le\frac1{3(y-1)^3}.
\tag{3.1}
$$

若从原权行删去 $r$ 个任意位置，余行记为 $U$，其初等和记为 $e_t(U)$。对 $t\ge1$，
$$
t e_t(U)=
\sum_{\substack{I\subset U\\|I|=t-1}}
w_I\sum_{j\in U\setminus I}w_j.
$$
集合的并至多删去 $r+t-1$ 个权。由于原权单调，所剩总质量至少是删掉最大的 $r+t-1$ 项后的尾质量。因此
$$
\boxed{
\frac{S_{x+r+t-1}}t
\le\frac{e_t(U)}{e_{t-1}(U)}
\le\frac{S_x}t.}
\tag{3.2}
$$
上界只使用余质量不超过 $S_x$。全部级数非负，故计数与换序合法。

现在只删两位 $i,j$。展开
$$
e_t=e_t^{ij}+(w_i+w_j)e_{t-1}^{ij}+w_iw_je_{t-2}^{ij}.
$$
使用 $w_i,w_j\le x^{-4}$、(3.2) 和 (3.1)，对 $t\ge1$ 得
$$
\frac{e_t}{e_t^{ij}}\le(1+A_t)^2,
\qquad
A_t=\frac{3t(x+t+1)^3}{x^4}.
\tag{3.3}
$$
$t=1$ 的最后一项为零；$t\ge2$ 时
$e_{t-2}^{ij}/e_t^{ij}$ 由相邻两个 (3.2) 相乘支付，且不超过
$[3t(x+t+1)^3]^2$，所以同一式成立。

因 $x\ge2$，
$$
A_t\le\frac{3t(t+3)^3}{16}.
$$
又对整数 $t\ge1$，
$$
16(t+1)^4-\{16+3t(t+3)^3\}
=t(13t^3+37t^2+15t-17)\ge0.
$$
于是
$$
\boxed{1\le \frac{e_t}{e_t^{ij}}\le(t+1)^8.}
\tag{3.4}
$$
$t=0$ 时该式为等式。这个粗而显式的次数只来自原连续权；没有声称任意正权行也满足 (3.4)。

## 4. 由正边权得到整个真 Gram 的条件数

对删去两位的仍为无限正 $\ell^1$ 权行，标量 Newton 给
$$
e_{t+1}^{ij}e_{t-1}^{ij}
\le\frac{t}{t+1}(e_t^{ij})^2.
$$
这是有限截断的标准 Newton 不等式逐阶取极限；只用于标量初等对称和。包括 $t=0$ 的约定后，
$$
\frac{(e_t^{ij})^2}{t+1}
\le(e_t^{ij})^2-e_{t+1}^{ij}e_{t-1}^{ij}
\le e_t^2.
$$
再用 (3.4)，得到
$$
\frac{e_t^2}{(t+1)^{17}}
\le(e_t^{ij})^2-e_{t+1}^{ij}e_{t-1}^{ij}
\le e_t^2.
\tag{4.1}
$$
把 (4.1) 代入真实正形式 (2.5)，对 $f\in K$ 使用 (2.6)，即得
$$
\frac{(t!)^2Se_t^2}{(t+1)^{17}e_{t+1}}\|f\|^2
\le\langle H_t^{-1}f,f\rangle
\le\frac{(t!)^2Se_t^2}{e_{t+1}}\|f\|^2.
$$
这证明 (1.4)。特别，整个出生一空间上的
$\operatorname{cond}(H_t)$ 至多 $(t+1)^{17}$，不依赖 $m$。

为了控制标量尺度的相邻比，令 $r_t=e_t/e_{t-1}$。准确有
$$
\frac{\tau_t}{\tau_{t-1}}=t^2\frac{r_t^2}{r_{t+1}}.
\tag{4.2}
$$
Newton 给 $r_{t+1}\le tr_t/(t+1)$，结合 (3.2) 的未删行，
$$
\frac{\tau_t}{\tau_{t-1}}
\ge t(t+1)r_t\ge(t+1)S_{x+t-1}.
$$
另一方面，
$$
\frac{\tau_t}{\tau_{t-1}}
\le\frac{S_x^2}{r_{t+1}}
\le(t+1)\frac{S_x^2}{S_{x+t}}.
$$
由 (3.1) 和 $x\ge2$，
$$
\frac{S_x}{S_{x+t-1}}\le(t+1)^3,\qquad
\frac{S_x}{S_{x+t}}\le(t+2)^3.
$$
这恰好证明 (1.5)。

## 5. 非交换乘积的直接夹逼与全部旧列

令 $\beta_t=(t+1)^{17}$。由 (1.4)，
$$
\tau_t^{-1}I\preceq H_t\preceq\frac{\beta_t}{\tau_t}I.
$$
保持全部乘法次序，并逐次使用范数界，对任意 $u\in K$，
$$
\begin{aligned}
&\langle H_{h-1}H_h^{-1}H_\ell H_h^{-1}H_{h-1}u,u\rangle\\
&\qquad\le
\beta_{h-1}^2\beta_\ell
\left(\frac{\tau_h}{\tau_{h-1}}\right)^2
\frac{\tau_{\ell-1}}{\tau_\ell}
\,\langle H_{\ell-1}u,u\rangle.
\end{aligned}
\tag{5.1}
$$
这里没有使用不同 $H_t$ 的共同特征向量。由 (1.5)，系数至多
$$
h^{34}(\ell+1)^{17}
(h+1)^2(h+2)^6(\ell+1)^2S,
$$
这就是 (1.6)。由于 $\ell\le h$，
$h^{34}(h+1)^{21}(h+2)^6\le(h+2)^{61}$。

原真 MP 字典给
$$
D_1J_t=J_{t-1},\qquad
D_1^*J_{h-1}=J_hH_h^{-1}H_{h-1}.
\tag{5.2}
$$
第二式是按原物理内积取伴随，不能把其 Gram 比例倒置。若 $y=J_{h-1}u$，则对 $0\le j<h$、$\ell=h-j$，
$$
\|D_1^jD_1^*y\|^2
=\langle H_{h-1}H_h^{-1}H_\ell H_h^{-1}H_{h-1}u,u\rangle,
$$
$$
\|D_1^jy\|^2=\langle H_{\ell-1}u,u\rangle.
$$
逐列应用 (1.6)，乘 $c_j^2$ 并求和，证明 (1.7)。

## 6. 原最高锚及准确剩余范围

原头 $A=VJ_dV^{-1}$，$v_j=V_{jj}$，顶锚为
$$
\Theta_h=\sum_{j<h}v_j^2(D_1^j)^*D_1^j,\qquad
\Theta_{h+1}^{[h]}=\sum_{j<h}v_j^2(D_1^j)^*D_1^j
\quad\hbox{于输出高度 }h+1.
$$
当 $h=d=2^m$ 时，截断头没有新增 $j=d$ 列。定理 2 直接给原整个出生一上的
$$
\boxed{
\|(\Theta_{d+1}^{[d]})^{1/2}D_1^*y\|
\le(d+2)^{61/2}\sqrt{S_m}\,
\|\Theta_d^{1/2}y\|
\le\frac{(d+2)^{61/2}}{\sqrt3\,m^{3/2}}
\|\Theta_d^{1/2}y\|.}
\tag{6.1}
$$
与已有出生零的 $\sqrt d\,\nu$ 界及全部出生的 $D_2^*$ 三次权桥并列，本文补上了原连续尾**出生一的所有高度旧列**及其最高 $D_1^*$ 锚费用。合法出生商的截口不删出生一，因此常数对 $q$ 一致。

若 $h<d$ 而要加入新的头列 $j=h$，必须另付原列权比；(1.7) 并未把它免费加入。准确新列为
$$
D_1^hD_1^*J_{h-1}u=H_h^{-1}H_{h-1}u.
$$
由同一夹逼，可另得
$$
\|D_1^hD_1^*y\|^2
\le h^{34}(h+1)^2(h+2)^6S_m^2
\|D_1^{h-1}y\|^2.
\tag{6.2}
$$
乘新列权时仍须保留 $v_h/v_{h-1}$；本文的顶部应用 (6.1) 不需要这一步。

本稿不证明一般正权的全高度算子 Newton，不处理出生 $a\ge2$ 的相同条件数，也不使 $\Gamma^{-1}$ 保持出生一。实际最高正锚只有无指定速率的趋零，不能再无条件乘 $(d+2)^{61/2}$ 宣布传播消失。因此原同源高返回、固定物理测试双费 Gram 和边界 $N=M$ 仍保留各自准确缺口。
