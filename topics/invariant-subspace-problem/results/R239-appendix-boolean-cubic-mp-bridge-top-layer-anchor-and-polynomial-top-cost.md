# R239 附录：原 Boolean 第二下降的三次权桥、最高真实核层正锚与顶部多项式费用

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文保留原物理 Hilbert 范数、真幂 Moore–Penrose 逆和真实出生截口。第二下降的所有高度由同一个三次权删除连接；最高真实核层有实际正锚；第二下降的伴随在该锚中可以用明确的局部真实 carry 支付。最高几层的 carry 是固定低位，故费用仅随头维数多项式增长。另付清出生零的第一下降顶部伴随。

一般正出生的第一下降顶部伴随仍开放；本文没有控制完整 $H_{\rm top}$、$\Gamma$ 传播、一般三 Gram 或边界 $N=M$。依赖：[原首物理头商 Gram](R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)、[Boolean 两带及商边界](R239-appendix-boolean-two-band-quotient-commutator-boundaries-and-gram-contraction.md)、[真实 Jordan 头](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)。

## 1. 原域、两个截口与真 MP 坐标

固定原 $m$、$d=2^m$ 和合法 $q$。令
$$D=\sum_{i\ge m}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad \nu=\|D\|\le1/m.$$
$\mathcal H_p$ 是孔数 $p$ 的原物理空间，记
$$\mathcal E_{h,p}=\ker D^h\cap\mathcal H_p,\qquad
W_{h,p}=\mathcal E_{h,p}\ominus\mathcal E_{h-1,p}.$$
非零 $W_{h,p}$ 的出生为 $a=p-h+1\ge0$。

先取无限 height 的出生商，删去所有 $a\ge q+2$ 的 $D$ 不变子空间，保留 $0\le a\le q+1$、所有 $h\ge1$ 的正交商。由已证两带定理，
$$\delta_\infty=D_1+D_2,$$
$$D_1:(a,h)\longmapsto(a,h-1),\qquad
D_2:(a,h)\longmapsto(a+1,h-2).$$
越过出生截口的块为零。各自的源/像块标签不重叠，所以
$\|D_1\|,\|D_2\|\le\nu$。物理伴随分别升 height 一、二；$D_2^*$ 同时降出生一，在出生零上为零。

有限矩形 $\mathcal F_d$ 再保留 $h\le d$，$\delta=\delta_\infty|_{\mathcal F_d}$。其有限矩形伴随会删去输出 height 超过 $d$ 的项。本文在讨论 $E^*$ 顶边时明确使用无限 height 出生商的伴随，不把两个伴随混同。

令 $K_a=\ker D\cap\mathcal H_a$，定义
$$J_{t,a}=(D^t:\mathcal H_{a+t}\to\mathcal H_a)^\dagger|_{K_a},
\qquad H_{t,a}=J_{t,a}^*J_{t,a},\qquad J_{0,a}=I_{K_a}.$$
固定孔层的原满射性保证 MP 逆有界。$J_{t,a}$ 的像恰为 $W_{t+1,a+t}$：其 $D^t$ 像 primitive，故在 $\ker D^{t+1}$，同时正交 $\ker D^t$；反向也成立。$H_{t,a}$ 在原 $K_a$ 上有界严格正，以下全部逆在该空间取。

## 2. 第一下降的真幂递推

对 $t\ge1$、$u\in K_a$，$DJ_{t,a}u$ 属于 $\mathcal E_{t,a+t-1}$，且
$$D^{t-1}DJ_{t,a}u=u.$$
投影到 $W_{t,a+t-1}$ 只删去 $\ker D^{t-1}$，仍是 $u$ 的原像并正交该核。真 MP 原像唯一性给
$$\boxed{D_1J_{t,a}=J_{t-1,a}.}\tag{2.1}$$
因此
$$D_1^jJ_{t,a}=J_{t-j,a}\quad(0\le j\le t),\qquad
D_1^{t+1}J_{t,a}=0.$$
没有假定 $D_1$ 与 $D$ 交换，也没有以逐次 MP 逆替代真幂 MP 逆。出生保持，故在合法出生商和有限矩形内均保持。

## 3. 同一个三次权删除决定全部第二下降

定义实际有界删除
$$C=\sum_{i\ge m}b_i^3E_i,\qquad
c_m=\|C\|\le\sum_{i\ge m}(i+1)^{-6}\le\frac1{5m^5}.$$
$C$ 与 $D$ 交换，故
$$C_a=C|_{K_{a+1}}:K_{a+1}\to K_a.$$
其 $C_a^*$ 是 primitive 空间间的物理伴随，即
$P_{K_{a+1}}C^*|_{K_a}$。

原 Boolean 身份为
$$\operatorname{ad}_D^2D^*=-2C,\qquad
\operatorname{ad}_D^3D^*=0.$$
取 $t\ge2$、$v\in K_{a+1}$、$y=J_{t-2,a+1}v$。因 $D^{t-1}y=0$，完整交换展开给
$$D^tD^*y=-t(t-1)Cv.$$
$D^*y$ 的最高可能真实核层为 $t+1$。投影到该层后，由同一个 MP 唯一性，
$$\boxed{D_2^*J_{t-2,a+1}=-t(t-1)J_{t,a}C_a.}\tag{3.1}$$
出生桥要求 $0\le a\le q$；在有限矩形中还要求 $t+1\le d$。无限 height 出生商不需该 height 上界。出生零向负出生的形式块取零。

若写
$$D_2J_{t,a}=J_{t-2,a+1}K_{t,a},$$
则原物理伴随精确给
$$\boxed{K_{t,a}=-t(t-1)H_{t-2,a+1}^{-1}C_a^*H_{t,a}.}\tag{3.2}$$
所有高度的桥由同一个实际 $C_a$ 和两真 MP Gram 决定；次序不可交换。

另因 $CJ_{t,a+1}v$ 是 $C_av$ 的 $D^t$ 原像，最小范数性给
$$\boxed{C_a^*H_{t,a}C_a\preceq c_m^2H_{t,a+1}\quad(t\ge0).}\tag{3.3}$$
这不要求 $C$ 保持 MP 正交域。$D_1J_t$ 与 $D_2J_t$ 的输出物理正交，还给
$$H_{t-1,a}+K_{t,a}^*H_{t-2,a+1}K_{t,a}
\preceq\nu^2H_{t,a}\quad(t\ge2).\tag{3.4}$$

## 4. 最高真实核层的同源正锚

原无缩放头 $A=VJ_dV^{-1}$ 满足 $V=1\oplus V_+$，记
$$v_j=V_{jj}=d_0^j/W_j>0.$$
这里 $W_j$ 是原头权积，与尾真核层 $W_{h,p}$ 区分。原全部同源左/裸接合核由
$$\mathcal T f=\sum_{j<d}(Ve_j)(-\delta)^jf$$
参数化。

给联合物理输出赋次数 $b=\text{物理头指标}+\text{真实尾核 height}$。输入 $f_h$ 在 height $h$ 时，$\delta^j$ 的每个有序词若有 $r$ 次 $D_2$，尾 height 降 $j+r$；头条目若为 $V_{j-\ell,j}$，总次数准确降 $\ell+r$。$D_1,D_2$ 一般不交换，不能把有序词改成交换二项式幂。

所以最高块只来自 $r=\ell=0$：
$$P_{b=h}\mathcal T f_h
=\sum_{j<h}(-1)^jv_je_jD_1^jf_h\quad(h\le d).$$
定义实际正锚
$$\boxed{\Theta_h=\sum_{j<h}v_j^2(D_1^j|_{W_h})^*D_1^j|_{W_h}\succeq I.}\tag{4.1}$$
它按出生约化。在出生 $a$ 上，若 $f_h=J_{h-1,a}u$，
$$\|\Theta_h^{1/2}f_h\|^2
=\sum_{j<h}v_j^2\langle H_{h-j-1,a}u,u\rangle.\tag{4.2}$$
没有共同对角化假设。

对一般 $f\in\mathcal F_d$，$P_{b=d}\mathcal T f=P_{b=d}\mathcal T f_d$。因此真实最小对
$\mathcal T f_r=(v,-a_{\rm bare})$ 满足
$$\boxed{\|\Theta_d^{1/2}f_d\|^2
=\|P_{b=d}(v,-a_{\rm bare})\|^2.}\tag{4.3}$$
$P_{b=d}$ 的物理支撑在全局整数 $n\ge d-1$：height 至少二就至少有一尾孔，从而 $n\ge d$；height 一的无尾项只能在头 $d-1$。原实际强极限族因而给
$$\|\Theta_d^{1/2}f_d\|^2
\le\left(\|\mathbf1_{n\ge d-1}w\|+\|v-w\|\right)^2+\alpha^2
\longrightarrow0.\tag{4.4}$$
这是同一个实际裸费和左最小者的锚；不能把无速率的趋零再乘增长费用。

## 5. 第二下降伴随的旧列与两个精确新列

取 $y=J_{h-1,a+1}v$，$h\ge1$，使用无限 height 出生商的 $D_2^*$。由 (2.1)、(3.1)，对 $0\le j\le h-1$，
$$\boxed{D_1^jD_2^*y=
\frac{h(h+1)}{(h-j)(h-j+1)}D_2^*D_1^jy.}\tag{5.1}$$
这是从同一个 $J/C$ 身份逐项得到的比例，不是交换性。额外两列恰为
$$\boxed{D_1^hD_2^*y=-h(h+1)J_{1,a}C_av,\qquad
D_1^{h+1}D_2^*y=-h(h+1)C_av.}\tag{5.2}$$
更高次为零。

对任意非负权 $c_j$，由 $\|D_2^*\|\le\nu$，
$$\sum_{j<h}c_j^2\|D_1^jD_2^*y\|^2
\le\left[\frac{\nu h(h+1)}2\right]^2
\sum_{j<h}c_j^2\|D_1^jy\|^2.\tag{5.3}$$
只取 $j\le J<h$ 时，可将常数锐化为
$\nu h(h+1)/[(h-J)(h-J+1)]$。取 $c_j=v_j$ 并保留新列，若 $h+2\le d$，
$$\begin{aligned}
\|\Theta_{h+2}^{1/2}D_2^*y\|^2
\le{}&[\nu h(h+1)/2]^2\|\Theta_h^{1/2}y\|^2\\
&+h^2(h+1)^2
\{v_h^2\|J_{1,a}C_av\|^2+v_{h+1}^2\|C_av\|^2\}.
\end{aligned}\tag{5.4}$$

## 6. 新列的局部真实 carry 费用与小 height

对 $h\ge2$，分别以 $t=1,0$ 使用 (3.3)，将 (5.4) 的新列付给输入 $\Theta_h$ 的 $j=h-2,h-1$ 两列。令
$$M_h=\max(v_h/v_{h-2},\,v_{h+1}/v_{h-1}).$$
于是
$$\boxed{\|\Theta_{h+2}^{1/2}D_2^*y\|^2
\le h^2(h+1)^2(\nu^2/4+c_m^2M_h^2)
\|\Theta_h^{1/2}y\|^2.}\tag{6.1}$$
常数对 $q$ 一致，头依赖只在两个明确的原权比：
$$v_h/v_{h-2}
=\frac{d_0^2}{\alpha_{v_2(h-1)}\alpha_{v_2(h)}},\qquad
v_{h+1}/v_{h-1}
=\frac{d_0^2}{\alpha_{v_2(h)}\alpha_{v_2(h+1)}}.$$
偶数 $h$ 时两者均为 $d_0/\alpha_{v_2(h)}$；奇数时取邻近两个偶数的较大倒比。不以整个 $V$ 的条件数替代这些量，也不声称它们对全部 $h$ 统一温和。

$h=1$ 不存在输入 $j=h-2$。此时 $\Theta_1=I$、$v_1=1$、$v_2=d_0^2/d_1=e^{1070}$，直接用
$\|D_1\|,\|D_2^*\|\le\nu$ 得
$$\|\Theta_3^{1/2}D_2^*y\|^2
\le(\nu^2+\nu^4+v_2^2\nu^6)\|y\|^2.\tag{6.2}$$
它与 (5.2) 的 $-2J_1C_av,-2C_av$ 一致。$h=2$ 可合法使用 (6.1)：$v_2=v_3=e^{1070}$、$M_2=e^{1070}$，常数恰为
$9\nu^2+36c_m^2e^{2140}$，输入 $\Theta_2$ 正有 $H_1,H_0$ 两项。

## 7. 最高几层第二下降的多项式桥

在无限 height 出生商中保持同一个 $d$ 头对角，定义
$$\Theta_h^{[d]}=
\sum_{0\le j<\min(h,d)}v_j^2(D_1^j)^*D_1^j.$$
$h\le d$ 时等于 $\Theta_h$。$h>d$ 时这里只是明确正锚，不把相应多项式像宣称为原联合核的合法元素。

因为 $d=2^m$，$d-2$ 的 valuation 为一，最高内部桥为
$$\boxed{\|\Theta_d^{1/2}D_2^*y\|
\le(d-2)(d-1)\sqrt{\nu^2/4+c_m^2e^{2140}}\,
\|\Theta_{d-2}^{1/2}y\|.}\tag{7.1}$$
$h=d-1$ 的截断锚只保一个新列 $j=d-1$，相对输入 $j=d-3$ 的比为 $d_0/\alpha_1=e^{1070}$，故
$$\boxed{\|(\Theta_{d+1}^{[d]})^{1/2}D_2^*y\|
\le d(d-1)\sqrt{\nu^2/4+c_m^2e^{2140}}\,
\|\Theta_{d-1}^{1/2}y\|.}\tag{7.2}$$
$h=d$ 时全部保留列都是旧列，故
$$\boxed{\|(\Theta_{d+2}^{[d]})^{1/2}D_2^*y\|
\le\nu d(d+1)/2\,\|\Theta_d^{1/2}y\|.}\tag{7.3}$$
这些费用只含 $d$ 的多项式和固定最低 carry 常数，对 $q$ 一致。一般固定 $r\ge2$ 的 $h=d-r$ 也只见 $v_2(r),v_2(r\pm1)$ 对应的固定低位。

在原块分解 $\delta_\infty=\begin{psmallmatrix}\delta&E\\0&K\end{psmallmatrix}$ 中，
$$E^*f=D_1^*f_d+D_2^*f_{d-1}+D_2^*f_d.\tag{7.4}$$
(7.2)–(7.3) 支付后两个部分。前两项同在输出 height $d+1$，有真实交叉，不能直接把平方范数拆成正交和。

## 8. 出生零的第一下降顶部也可付清

这一节仅在一维 primitive $K_0$ 上使用标量 Newton。令 $e_t=e_t(b_i^2)$ 为原无限正系数的有限阶基本对称和。真实真幂 MP Gram 为
$$H_{t,0}=\frac1{(t!)^2e_t},\qquad
r_t=\frac{H_{t-1,0}}{H_{t,0}}=t^2e_t/e_{t-1}.$$
由有限截断 Newton 再取单调极限，$r_h/r_k\le h/k$ 对 $1\le k\le h$ 成立。又 (2.1) 与 $\|D_1\|\le\nu$ 给 $r_h\le\nu^2$。

若 $y=J_{h-1,0}v$，则原物理伴随准确为
$$D_1^*y=r_hJ_{h,0}v.$$
对每个旧列 $0\le j<h$，其平方范数相对输入列之比是
$$\frac{r_h^2H_{h-j,0}}{H_{h-j-1,0}}
=\frac{r_h^2}{r_{h-j}}\le h\nu^2.$$
若 $h<d$，新增 $j=h$ 列的费用至多
$(v_h/v_{h-1})^2\nu^4$ 倍输入最后一列。特别 $h=d$ 没有新增头列，得
$$\boxed{\|(\Theta_{d+1}^{[d]})^{1/2}D_1^*y\|
\le\sqrt d\,\nu\,\|\Theta_d^{1/2}y\|
\quad\text{在出生零上}.}\tag{8.1}$$
出生零的 $D_2^*=0$，所以该出生的整个 $E^*$ 顶边已由 (8.1) 支付。

## 9. 准确的剩余缺口与核验

一般出生 $a\ge1$ 的 $H_{t,a}$ 是不交换的算子，§8 的标量 Newton 不能直接推广。原 $\Gamma_{CC}^{-1}$ 作用于出生零测试向量后也可扩展出生，故只付清出生零仍不足以控制一般 $D_1^*:\,W_d\to W_{d+1}$。

因此完整 $E^*$、$EE^*$、$H_{\rm top}$ 尚未由本文付清。各正锚也尚未与原 $\Gamma$ 全部跨 height 抵消合并，不能从顶锚趋零或局部多项式桥直接宣布低侧传播消失。

normal_full_columns_1856 独立核验了 (2.1)、(3.1)、(3.3)、(5.1)–(5.2) 的真 MP 唯一性及端点；根代理全文核了正锚、实际 carry、小 height 和出生零 Newton 推论。所有证明只用已列原身份和物理范数，没有用形式 inverse 替代真 inverse，也没有丢掉跨出生或顶部源项。
