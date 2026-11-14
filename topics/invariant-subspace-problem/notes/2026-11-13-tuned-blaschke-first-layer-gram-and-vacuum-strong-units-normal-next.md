# 一次层可调 Gram 的近临界 Blaschke 强单位

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065。

**状态：以下构造与一次层估计完整证明，属于中间结果。** 构造实际 $P\in\{A\}'$，满足 $P$ 为非零收缩、$1\in\operatorname{Ran}P$，且有同一组收缩强主理想单位。与 R267 第二附录的固定参数块不同，本稿的 $G=P^{-1}$ 在完整一次 Walsh 层上无界。更进一步，对一个固定的正常正秩一泛函，其一次矩不属于 $\ell^2$，本稿的 $P$ 却满足全部一次有限列的聚合逆图界。这准确修复一次层障碍，不声称控制全部次数的正常矩。

本稿也不同于 R267 的前向无真空原像附录：这里始终有 $Pg=1$，逆真空源及同组强单位都实际存在。

## 1. 实际模型与纯有限块

使用原模型
$$
H=L^2(\mathbb Z_2),\qquad
V_j=I-2Y_j,\qquad V_B1=\chi_B,\qquad
\|V_j-D_j\|\le8\eta_j,
\quad \eta_j\le e^{-770\,16^j},
\tag{1.1}
$$
其中纯位矩阵在 Walsh 基上为
$$
D_j=\begin{pmatrix}0&-1\\1&2\end{pmatrix}.
$$
实际及纯位算子均有范数小于 $3$：纯位范数为 $1+\sqrt2$，再由 $8\eta_j\le8e^{-770}$ 即得实际界。记 $\mathsf N\chi_B=|B|\chi_B$。

在一个大小为偶数 $q\ge4$ 的纯块上，记 $Q=q+2$，置
$$
T_q=\frac2Q\sum_{j=1}^qE_j,\qquad
R_{q,a}=(aI+T_q)(I+aT_q)^{-1},\qquad
U_{q,a}=R_{q,a}^{-1},
$$
$$
\frac25\le a\le\frac34,\qquad
g_{q,a}=U_{q,a}\Omega.
\tag{1.2}
$$
$\|\sum E_j\|=\max_k\sqrt{(k+1)(q-k)}\le(q+1)/2$，故 $\|T_q\|<1$。恒等式
$$
I-R_{q,a}^*R_{q,a}
=(1-a^2)(I+aT_q^*)^{-1}(I-T_q^*T_q)(I+aT_q)^{-1}\ge0
$$
给 $R_{q,a}$ 收缩。$T_q$ 幂零，$a>0$，所以 $R_{q,a}$ 可逆，$U_{q,a}$ 扩张。

准确的有限维 Laplace 式为
$$
g_{q,a}=a\Omega+(1-a^2)\int_0^\infty e^{-as}v_q(s)\,ds,
$$
$$
v_q(s)=\bigotimes_{j=1}^q
\left[\left(1-\frac sQ\right)\Omega_+
+\frac sQ\chi_j\right].
\tag{1.3}
$$
积分是有限次多项式乘指数，不涉及形式预解式。

## 2. 对整个参数区间一致的低次数估计

置
$$
\alpha_{q,a}=\langle g_{q,a},\Omega\rangle,\qquad
\theta=\frac1{256},\qquad d_q=\lfloor\theta q\rfloor.
$$
以下常数不依赖 $a\in[2/5,3/4]$。

### 2.1 真空均值

准确有
$$
\alpha_{q,a}
=a+(1-a^2)J_{q,a},\qquad
J_{q,a}=\int_0^\infty e^{-as}(1-s/Q)^q\,ds.
$$
令 $b=q/Q$。在 $0\le s\le Q$ 上，对 $q$ 次幂作差给
$$
0\le e^{-bs}-(1-s/Q)^q
\le\frac q2\left(\frac sQ\right)^2
e^{-(q-1)s/Q}.
$$
乘 $e^{-as}$ 积分，右侧至多
$$
\frac{q/Q^2}{(a+(q-1)/Q)^3}\le\frac2q.
$$
在 $s\ge Q$ 上，因 $q$ 偶，
$$
\int_Q^\infty e^{-as}(s/Q-1)^q\,ds
=\frac{e^{-aQ}q!}{Q^qa^{q+1}}
\le\frac52e^{-3q/20}.
$$
这里使用 $q!\le((q+1)/2)^q$、$a\ge2/5$ 及
$\log(5/4)<1/4$。指数比较项在该尾的积分至多 $e^{-q}$。又
$$
\left|a+\frac{1-a^2}{a+b}-1\right|\le\frac2q.
$$
合并并用 $\sup_{t>0}te^{-ct}=1/(ce)$，得到安全的统一界
$$
\boxed{|\alpha_{q,a}-1|\le20/q.}
\tag{2.1}
$$
特别 $q\ge40$ 时
$$
|\alpha_{q,a}^2-1|\le50/q.
\tag{2.2}
$$

### 2.2 低于线性次数的非真空质量

令 $r=1/2$。对 $x=s/Q$，
$$
\|r^{\mathsf N}v_q(s)\|^2
=(1-2x+\tfrac54x^2)^q.
$$
全局初等不等式
$$
1-2x+\tfrac54x^2\le e^{3x/4}\qquad(x\ge0)
\tag{2.3}
$$
可以直接求导验证：差函数的导数最小值为
$$
2+\frac{10}{3}\left(1-\log\frac{40}{9}\right)>0.
$$
例如
$\log(40/9)=\log4+\log(10/9)<7/5+1/9=68/45$
已足够。因此
$$
\|r^{\mathsf N}v_q(s)\|\le e^{3s/8}.
\tag{2.4}
$$

在 $0\le s\le Q/4$ 上，将真空正交分量去掉，平方差给
$$
\|v_q(s)-\langle v_q(s),\Omega\rangle\Omega\|
\le\frac{s}{\sqrt q}e^{-s/4}.
\tag{2.5}
$$
确切地，两平方范数之差是
$(1-2x+2x^2)^q-(1-x)^{2q}$，至多
$q x^2(1-x)^{q-1}$；$q\ge4$ 即给 (2.5)。

令 $\Pi_{\le d_q}$ 为整个该块中次数至多 $d_q$ 的正交投影。在 $s\ge Q/4$，利用 (2.4) 得
$$
\|\Pi_{\le d_q}(v_q(s)-\langle v_q(s),\Omega\rangle\Omega)\|
\le2^{d_q}e^{3s/8}.
$$
将小尾和大尾分别代入 (1.3)，使用 $a\ge2/5$，得到
$$
\boxed{
\|\Pi_{\le d_q}(g_{q,a}-\alpha_{q,a}\Omega)\|
\le\frac3{\sqrt q}+40e^{-3q/1280}.
}
\tag{2.6}
$$
因为小尾积分至多
$q^{-1/2}\int_0^\infty s e^{-13s/20}ds<3/\sqrt q$；
大尾至多
$40\,2^{d_q}e^{-Q/160}\le40e^{-3q/1280}$。

对 $q\ge2^{16}$，
$40e^{-3q/1280}\le q^{-1/2}$，故
$$
\boxed{
\|\Pi_{\le d_q}(g_{q,a}-\alpha_{q,a}\Omega)\|^2\le16/q.
}
\tag{2.7}
$$

## 3. 只用连续性调节逆真空范数

本构造不需要临界参数的精确值或鞍点渐近。

### 3.1 参数 $a=3/4$ 的小范数端

由
$1-2x+2x^2\le e^x$ 得 $\|v_q(s)\|\le e^{s/2}$。这个初等不等式的差函数导数最小值为
$6-4\log4>0$。与 (2.5) 分段积分给
$$
\|g_{q,3/4}-\alpha_{q,3/4}\Omega\|
\le\frac7{16\sqrt q}+\frac74e^{-Q/16}
\le\frac4{\sqrt q}.
$$
和 (2.1) 合并，
$$
1\le\|g_{q,3/4}\|^2\le1+200/q.
\tag{3.1}
$$

### 3.2 参数 $a=2/5$ 的大范数端

取单位向量
$$
w_q=13^{-q/2}(-2\Omega_++3\chi)^{\otimes q}.
$$
$q$ 偶保证
$$
\langle v_q(s),w_q\rangle
=\left(\frac{5s/Q-2}{\sqrt{13}}\right)^q\ge0
$$
对全部 $s\ge0$ 成立，且 $\langle\Omega,w_q\rangle\ge0$。只在 $3Q\le s\le3Q+1$ 积分，得到
$$
\boxed{
\|g_{q,2/5}\|
\ge\frac{21}{25}e^{-14/5}
 \exp\left[q\left(\frac12\log13-\frac65\right)\right].
}
\tag{3.2}
$$
指数严格为正。因此该范数随偶数 $q\to\infty$ 指数增长。

给定 $0<\delta\le\theta^2/32$，若偶数 $q$ 足够大，使
$$
q\ge2^{16},\qquad
q\delta\ge \frac8{\theta^2},
\tag{3.3}
$$
并保证 (3.2) 大于 $\sqrt{1+\delta}$，则 (3.1) 给小端严格低于 $1+\delta$。$a\mapsto\|g_{q,a}\|^2$ 连续，故存在
$$
a(q,\delta)\in[2/5,3/4],\qquad
\boxed{\|g_{q,a(q,\delta)}\|^2=1+\delta.}
\tag{3.4}
$$
无需该函数单调。

以下记这个调好的源为 $g_q$。由 (2.2)、(2.7)，其次数大于 $d_q$ 的质量满足
$$
\boxed{
\|\Pi_{>d_q}g_q\|^2
\ge\delta-\frac{66}{q}\ge\frac\delta2.
}
\tag{3.5}
$$
同时全部非真空质量至多 $\delta+50/q\le2\delta$。

## 4. 去均值的真实一次块 Gram 下界

这里先在纯块完成准确线性代数。记 $C_+$、$C_-$ 为一次 Walsh 生成、消去算子的和，$\mathsf N_q$ 为该块次数算子，则
$$
L_q=\sum_{j=1}^qD_j
=C_+-C_-+2\mathsf N_q.
$$
令 $K=C_+-C_-$，则 $K^*=-K$、
$[\mathsf N_q,K]=C_++C_-$，且
$\|C_++C_-\|=q$。因此
$$
\boxed{
L_q^*L_q
=-K^2+4\mathsf N_q^2+2(C_++C_-)
\ge4\mathsf N_q^2-2qI.
}
\tag{4.1}
$$
这是算子不等式，不是只沿一个测试向量估算。

源 $g_q$ 的系数为实数，因此
$\langle Kg_q,g_q\rangle=0$。又 $g_q$ 对该块所有位排列对称。令
$$
w_q=L_qg_q-
\frac{\langle L_qg_q,g_q\rangle}{\|g_q\|^2}g_q.
\tag{4.2}
$$
则 $w_q\perp g_q$，且仍为对称向量。由 (3.5)，
$$
\|\mathsf N_qg_q\|^2\ge\theta^2q^2\delta/2.
$$
又
$$
0\le\langle L_qg_q,g_q\rangle
=2\langle\mathsf N_qg_q,g_q\rangle
\le4q\delta.
$$
代入 (4.1)—(4.2)，得到
$$
\begin{aligned}
\|w_q\|^2
&\ge2\theta^2q^2\delta-4q-16q^2\delta^2\\
&\ge\boxed{\theta^2q^2\delta}.
\end{aligned}
\tag{4.3}
$$
最后一步准确使用
$\delta\le\theta^2/32$ 和 $q\delta\ge8/\theta^2$。

对任意一次系数 $(u_j)_{j=1}^q$，对称性使
$$
\left\langle\sum_j u_jD_jg_q,w_q\right\rangle
=\frac{\sum_j u_j}{q}\|w_q\|^2.
\tag{4.4}
$$
所以这是一个控制整个块上系数和的 Gram 方向，不仅是归一化全位和的范数下界。

## 5. 同一固定正常态及块序列

取
$$
q_i=2^{4i},\qquad c_i=2^{-i-2},\qquad
0<\delta_*\le\theta^2/64,\qquad
\delta_i=\delta_*2^{-i}.
\tag{5.1}
$$
选 $i_0$，使对所有 $i\ge i_0$，第3节的调节条件均成立。有限个初块不需要正则因子。

选择互不交、依次后移的实际有限位块 $B_i$，$|B_i|=q_i$。块可取连续区间。物理位置足够高，使以下两个预算同时成立：
$$
8\eta_j\,\frac{49}{48}\le c_i^2
\quad(j\in B_i),
\tag{5.2}
$$
以及第6节的实际提升误差不超过 $\varepsilon_i=\delta_i^2$，$i\ge i_0$。这是一个一次选定的块序列，后面不随被检验的 $P$ 改变。

定义固定向量和正常泛函
$$
f=1+\sum_{i\ge1}c_i\chi_{B_i},\qquad
\phi_f(F)=\langle Ff,f\rangle.
\tag{5.3}
$$
级数一致收敛，
$$
3/4\le f\le5/4,\qquad
\lambda=\|f\|^2=49/48,\qquad Cf=f.
$$
对 $j\in B_i$，
$$
\langle D_jf,f\rangle=2c_i^2,
\qquad
|\phi_f(V_j)-2c_i^2|\le8\lambda\eta_j.
\tag{5.4}
$$
第一式来自
$\operatorname{Re}D_j=2P_j$，并用实向量使反对称项为零。故 (5.2) 给
$$
\operatorname{Re}\phi_f(V_j)\ge c_i^2,\qquad
\boxed{\sum_j|\phi_f(V_j)|^2
\ge\sum_iq_ic_i^4=\infty.}
\tag{5.5}
$$

因此，凡 R244 强单位正则器的逆真空源属于
$\mathcal H_{\sqrt3}$，R255 的真实双输入端点便使其逆在一次层有界；(5.5) 阻止该 $P$ 为此同一 $\phi_f$ 满足聚合界。以下构造专门改变这一点。

## 6. 实际有限提升、非零极限与同组收缩强单位

对每个 $i\ge i_0$，将第3节调好的 $g_{q_i}$ 放在 $B_i$ 上。其实际 Walsh 提升为
$$
X_{g_{q_i}}=\sum_{F\subseteq B_i}\widehat g_{q_i}(F)V_F.
$$
相应纯提升准确是 $U_{q_i,a_i}$：纯有限代数的真空列映射为同构，且两者有同一真空列。

设 $r_i=\min B_i$。由 (1.1)、乘积逐因子作差和
$\sum_F|\widehat g(F)|\le2^{q_i/2}\|g\|$，有
$$
\|X_{g_{q_i}}-U_{q_i,a_i}\|
\le16q_i5^{q_i}\eta_{r_i}.
\tag{6.1}
$$
通过远置 $B_i$，令右侧不超过
$\varepsilon_i=\delta_i^2$。实际 $X_{g_{q_i}}$ 可逆：其在 $A=0$ 的标量值为 $1/a_i\ne0$，而 $A$ 拟幂零。其逆仍属于 $\mathcal A$。

置
$$
\widetilde U_i=\frac{X_{g_{q_i}}}{1-\varepsilon_i},
\qquad
\widetilde R_i=\widetilde U_i^{-1}.
\tag{6.2}
$$
由于纯 $U_{q_i,a_i}$ 扩张，(6.1) 使 $\widetilde U_i$ 扩张，$\widetilde R_i$ 收缩。准确真空列为
$$
\widetilde g_i=\frac{g_{q_i}}{1-\varepsilon_i}.
$$
其范数平方为 $(1+\delta_i)/(1-\varepsilon_i)^2$，
均值为 $\alpha_{q_i,a_i}/(1-\varepsilon_i)$。这些范数平方与均值对 $1$ 的偏差可和。

所有实际因子交换。因为各块互不交且 $V_F1=\chi_F$，
$$
g_n=\left(\prod_{i_0\le i\le n}\widetilde U_i\right)1
=\prod_{i_0\le i\le n}\widetilde g_i
\tag{6.3}
$$
是准确的普通 Walsh 块乘积，不是纯近似。各块均值和范数的可和偏差直接给 $g_n$ 在 $H$ 中 Cauchy。例如对 $n>m$，内积准确分解为前块范数平方乘以尾块均值乘积。于是
$$
g_n\longrightarrow g,\qquad
1\le\|g\|\le
\exp\left[\tfrac12\sum_i(\delta_i+4\varepsilon_i)\right]<2.
\tag{6.4}
$$

令
$$
P_n=\prod_{i_0\le i\le n}\widetilde R_i.
$$
它们均为收缩，且 $P_ng_n=1$，所以 $P_ng\to1$。

闭轨道 $M=\overline{\mathcal Ag}$ 被全部 $P_n\in\mathcal A$ 保持，故 $1\in M$；$1$ 循环使 $g$ 循环。在稠密轨道 $Fg$ 上，
$$
P_nFg=FP_ng\longrightarrow F1.
$$
一致收缩性因而给整个 $H$ 上的强极限 $P$，满足
$$
\boxed{P_n\to P\ \mathrm{SOT},\quad \|P\|\le1,\quad Pg=1.}
\tag{6.5}
$$

记 $U^{(m)}=\prod_{i_0\le i\le m}\widetilde U_i$。对 $n\ge m$，
$P_nU^{(m)}$ 是收缩尾积；取强极限得
$\|PU^{(m)}\|\le1$。同时
$$
PU^{(m)}1=Pg_m\longrightarrow Pg=1.
$$
借 $1$ 的循环性及一致范数界，得到
$$
\boxed{PU^{(m)}\to I\ \mathrm{SOT},\qquad
\|PU^{(m)}\|\le1.}
\tag{6.6}
$$
这是同一组实际强单位。R244 聚合附录因此准确适用：
$P$ 单射稠密像、$G=P^{-1}=X_g$，全部有限 Walsh 柱构成其图核心，且
$$
Gu=X_ug.
\tag{6.7}
$$

## 7. 完整一次有限列的实际 Gram 下界

对有限一次柱
$$
u=u_\varnothing1+\sum_j u_j\chi_j,\qquad
s_i(u)=\sum_{j\in B_i}u_j,
$$
定义纯参考向量
$$
G_0u=u_\varnothing g+\sum_j u_jD_jg.
$$
每个纯因子 $U_{q_i,a_i}/(1-\varepsilon_i)$ 扩张，有限纯乘积作用在 $u$ 上的范数至少为 $\|u\|$。以 (6.3) 的真空列取极限，得
$$
\|G_0u\|\ge\|u\|.
\tag{7.1}
$$

对每个 $i$，将 (4.2) 的去均值对称向量同样按
$(1-\varepsilon_i)^{-1}$ 缩放，记为 $\widetilde w_i$。在全空间里，向量
$\widetilde w_i\otimes g_{\mathrm{outside}\ B_i}$ 彼此正交：两个不同的块中，至少一个因子与相应 $\widetilde g_i$ 正交。

对 $G_0u$ 向这些方向作正交投影，使用 (4.3)—(4.4)，以及全部其余块范数至少为 $1$，准确给
$$
\boxed{
\|G_0u\|^2\ge\theta^2\sum_{i\ge i_0}\delta_i|s_i(u)|^2.
}
\tag{7.2}
$$
块内零和系数、常数项及其他块的输入都不会进入这个投影。因此 (7.2) 适用于任意一次系数列。

实际与纯参考之差为
$$
\|(G-G_0)u\|
\le8\|g\|\left(\sum_j\eta_j^2\right)^{1/2}
 \left(\sum_j|u_j|^2\right)^{1/2}.
$$
由 $\|g\|<2$ 及
$\sum_j\eta_j^2<2e^{-1540}$，该系数小于 $1/4$。再用 (7.1)，得到安全的完整下界
$$
\boxed{
\|Gu\|\ge\frac12
\max\left\{\|u\|,\
\theta\left(\sum_{i\ge i_0}
 \delta_i|s_i(u)|^2\right)^{1/2}\right\}.
}
\tag{7.3}
$$
这里没有将逐个单项下界当作整个 Gram 下界；正交去均值投影支付了所有系数之间的干涉。

取 $u=q_i^{-1/2}\sum_{j\in B_i}\chi_j$，则
$$
\|Gu\|\ge\frac\theta2\sqrt{q_i\delta_i}
=\frac{\theta\sqrt{\delta_*}}2\,2^{3i/2}\longrightarrow\infty.
\tag{7.4}
$$
所以逆在完整一次层上无界。由于 $G$ 闭，闭图定理还给出：完整一次闭 Walsh 子空间并不包含在 $\operatorname{Ran}P$ 中。

源本身也准确没有半阶次数矩。由 (3.5)，不同块的非负次数相加，得到
$$
\|\mathsf N^{1/2}g\|^2
\ge\frac\theta2\sum_{i\ge i_0}q_i\delta_i=\infty.
\tag{7.5}
$$
因此不是把仍具有平方根次数矩的旧源换一个名字。

## 8. 同一固定非 $\ell^2$ 正常态的一次聚合界

仍用第5节一次选定的 $f$。写
$$
e_j=\phi_f(V_j)-2c_i^2
\quad(j\in B_i),\qquad
e_j=\phi_f(V_j)\quad(j\notin\cup_iB_i).
$$
由 (5.4)，
$$
|e_j|\le8\lambda\eta_j,\qquad e\in\ell^2.
$$
将有限初块 $i<i_0$ 的纯矩并入一个固定 $\ell^2$ 列 $h$，则对每个有限一次柱，
$$
\phi_f(X_u)
=\lambda u_\varnothing+\sum_jh_ju_j
+2\sum_{i\ge i_0}c_i^2s_i(u).
\tag{8.1}
$$
加权 Cauchy–Schwarz 给
$$
\left|\sum_{i\ge i_0}c_i^2s_i(u)\right|
\le
\left(\sum_{i\ge i_0}\frac{c_i^4}{\delta_i}\right)^{1/2}
\left(\sum_{i\ge i_0}\delta_i|s_i(u)|^2\right)^{1/2},
$$
而准确有
$$
\sum_{i\ge i_0}\frac{c_i^4}{\delta_i}
=\frac1{256\delta_*}\sum_{i\ge i_0}2^{-3i}<\infty.
\tag{8.2}
$$
结合 (7.3)，得到
$$
\boxed{
|\phi_f(X_u)|\le
\left[
2(\lambda+\|h\|_2)+
\frac4\theta
\left(\sum_{i\ge i_0}\frac{c_i^4}{\delta_i}\right)^{1/2}
\right]\|Gu\|
}
\tag{8.3}
$$
对**全部有限一次列（含常数项）**成立。

这个同一个正常正秩一态满足 (5.5)，因而所有
$\mathcal H_{\sqrt3}$ 逆真空源正则器都在一次层失败；本稿实际 $P$ 则通过了该一次层检验。结论来自完整块 Gram 控制，而不是由某个逆方向增益推测配对成功。

## 9. 准确剩余范围

(8.3) 只覆盖次数至多一的全部有限列。R244 的最终条件要求任意有限 Walsh 柱，仍包括跨块、多次数和所有干涉项。本稿没有证明这些更高次数上的统一界，也没有证明 $Pf\in\operatorname{Dom}X_f$。

所用 $f$ 连续非负且 Walsh 系数绝对可和，已被 R235/R237 排为慢主理想湮灭者；本例用于检验正则器的真实能力。一般正常湮灭者的全部方程尚未转化为可实现的全次数 Gram 主控，没有构造 $P=SR$ 的有界因式，没有给 R253 的完整 $q_m$ 非消失下界。普通 Hilbert ISP 仍未完成。

后续同一构造的准确范围：[二次消去附录](../results/R230-appendix-tuned-blaschke-second-degree-cancellation-obstruction.md)已证明全部一次列成功的同时，次数至多二的聚合常数发散；该结论不改变本稿一次层估计。
