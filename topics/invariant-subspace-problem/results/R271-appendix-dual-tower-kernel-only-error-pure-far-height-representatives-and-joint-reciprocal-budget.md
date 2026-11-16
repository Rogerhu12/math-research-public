# R271 附录：双塔误差只作用真核列的单远孔代表与整高度倒数门

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：下述单层代表、完整原源误差和整高度必要条件均已证明。** 对每个允许高度 $r$，先在同一个完整强头 $C$ 的截断 boson 核中做真正投影，再通过已付 canonical 创建塔 $W$ 和双塔 $V=W^{-*}$ 回到原平方自由尾。由此得到只支撑于第 $r$ 个远孔层的 coherent 代表。需要估计的双塔差只作用于范数不超过 $1$ 的核投影，不作用于可能很大的 Green 列或其伴随原像。

每个高度仍保整个强头 MP。将不同高度同时纳入原全高度 Bessel，得到非零首头锚所强制的双重倒数可和条件。尚未证明这些真实费用的有效上界，未证明 $N=M$。

内积对第一变量线性。所有原物理空间、权及模型均与下列父稿相同：

- [完整 canonical 创建塔与双 Fock 塔](R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md)，§§1–4；
- [完整低旗来源与核 Gram](R271-appendix-complete-low-flag-return-source-and-cross-head-schur-energy-summability.md)，§§1–4；
- [跨头全高度 coherent Bessel](R271-appendix-cross-head-all-height-coherent-bessel-and-same-w-full-energy-summability.md)，§§1–4；
- [原强尾同一顶部流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)，§2；
- [核旗适配代表和无包络吸收](R271-appendix-true-kernel-flag-adapted-positive-far-representatives-and-envelope-free-reciprocal-budget.md)，§§4–5。

## 1. 原 C、每一个有限高度与完整 Galerkin 源

固定 $m\ge10$，令
$$
d=2^m,\quad R\ge d\ \text{为偶数},\quad
x=m+R,\quad h=d+R,\quad
C=A_m+D_{[m,x)},\quad C^h=0,
$$
$$
D=D_x=\sum_{i\ge x}b_iE_i,\quad b_i=(i+1)^{-2},\quad
S=\sum_{i\ge x}b_i^2,\quad L=C+D,\quad
\mathcal F_j=\ker C^j .
\tag{1.1}
$$
强头是整个原有限维物理空间，不按 forcing 所在低头截断。
令 $f_1=e_1\otimes\Omega$，$Ce_1=e_0$、$Ce_0=0$、
$\|e_1\|=\|e_0\|=1$。

取 $1\le r<h$，置 $p=r-1$。在同一个强头上定义
$$
H_p=\sum_{j=0}^{p}\frac{(C^*)^jC^j}{j!S^j}\succeq I,
$$
$$
a_p=\big(P_{\mathcal F_r}H_p|_{\mathcal F_r}\big)^{-1}
P_{\mathcal F_r}e_1,\qquad
\xi_p=e_1-H_pa_p.
\tag{1.2}
$$
压缩矩阵至少为恒等，逆存在。式 (1.2) 的正规方程准确给
$$
\xi_p\perp\mathcal F_r
=\ker C^r,\qquad
\xi_p\in\operatorname{Ran}(C^*)^r.
\tag{1.3}
$$
定义完整最小列
$$
q_r=\big((C^*)^r\big)^\dagger\xi_p
\in\operatorname{Ran}C^r,\qquad
(C^*)^r q_r=\xi_p.
\tag{1.4}
$$
这里的 MP 在整个强头空间中取值；不将它改成低旗压缩的逆。
$p=0$ 时 $a_0=P_{\ker C}e_1$，上述式子仍准确。

以下写
$$
\omega_j=(D^*)^j\Omega,\qquad
\sigma_j^2=\|\omega_j\|^2
=(j!)^2e_j\big((b_i^2)_{i\ge x}\big)>0 .
\tag{1.5}
$$

## 2. 截断 boson 核中真正的投影与低伴随恒等式

先在单一 boson 出生零塔中工作。令 $e_j^{\rm b}$ 是正交单位基，
$$
\mathfrak a e_j^{\rm b}=\sqrt{jS}\,e_{j-1}^{\rm b},
\qquad
\omega_j^{\rm b}=(\mathfrak a^*)^j\Omega
=\sqrt{j!S^j}\,e_j^{\rm b}.
$$
对 $\mathcal L_{\rm b}=C+\mathfrak a$，
至多 $p$ 层的真核列恰为
$$
R_p^{\rm b}a
=\sum_{j=0}^{p}\frac{(-C)^j a}{j!S^j}\otimes\omega_j^{\rm b},
\qquad a\in\mathcal F_{p+1}.
\tag{2.1}
$$
顶方程是 $C^{p+1}a=0$，没有省掉。
其源 Gram 为 $P_{\mathcal F_{p+1}}H_p|_{\mathcal F_{p+1}}$，因此
$$
k_{\rm b}=R_p^{\rm b}a_p
=P_{\ker(\mathcal L_{\rm b}|_{\le p})}f_1,\qquad
\|k_{\rm b}\|^2=\langle P_{\mathcal F_r}e_1,a_p\rangle\le1.
\tag{2.2}
$$
若将全部外部出生纳入，$C+\mathfrak a$ 及其截断伴随都约化出生直和；
$f_1$ 仅在出生零塔，所以 (2.2) 同时就是完整外部空间的核投影。
这不是任意候选列的范数上界。

对任意头列 $q$ 和整数 $j\ge1$，直接 telescoping 给
$$
(C^*)^j q\otimes\Omega-(-1)^j q\otimes\omega_j^{\rm b}
=\mathcal L_{\rm b}^*
 \sum_{k=0}^{j-1}(-1)^k(C^*)^{j-1-k}q\otimes\omega_k^{\rm b}.
\tag{2.3}
$$
将 $q=C^j a_p/(j!S^j)$ 代入并对 $1\le j\le p$ 求和，得到
$$
H_pa_p\otimes\Omega-k_{\rm b}
=\mathcal L_{\rm b}^*\Upsilon_p
\tag{2.4}
$$
的显式有限列，$\Upsilon_p$ 至多 $p-1$ 层。
再将 (1.4) 代入 (2.3)，得到
$$
\xi_p\otimes\Omega-(-1)^r q_r\otimes\omega_r^{\rm b}
=\mathcal L_{\rm b}^*\Theta_r,
\tag{2.5}
$$
其中 $\Theta_r$ 至多 $r-1=p$ 层。故
$$
\boxed{
f_1-(-1)^r q_r\otimes\omega_r^{\rm b}
=k_{\rm b}+\mathcal L_{\rm b}^*\Psi_r^{\rm b},
\qquad \Psi_r^{\rm b}=\Upsilon_p+\Theta_r .
}
\tag{2.6}
$$
这一步保留整个 $\xi_p$ 和 (1.4)，没有从其正交性推断解也在低旗。

## 3. 完整 W/V 运输：误差只乘核投影

设
$$
\delta_x=\frac{\max_{i\ge x}b_i^2}{S},\qquad
\epsilon_p=\frac43\delta_x p^2<1.
\tag{3.1}
$$
$p=0$ 按 $\epsilon_0=0$ 处理。
父稿在全部不同出生的完整外部直和上给
$$
D V_{\le p}=V_{\le p}\mathfrak a,\qquad
D^*W_j=W_{j+1}\mathfrak a^*,\qquad
V_j=(W_j^*)^{-1},
$$
$$
(1-\epsilon_p)I\preceq W_{\le p}^*W_{\le p}\preceq I.
\tag{3.2}
$$
第二个式子是创建列的逐层准确恒等式，也适用于从 $p$ 到 $p+1$ 的最末一行；
这个最末式不需要 $V_{p+1}$ 的逆界。
$C$、$C^*$ 只作用强头，与这些完整尾映射对易。
此外 $V,W$ 都在零远孔层等于恒等。

令 $G_W=W_{\le p}^*W_{\le p}$。由于
$W_{\le p}^*V_{\le p}=V_{\le p}^*W_{\le p}=I$，
$$
\begin{aligned}
(W_{\le p}-V_{\le p})^*(W_{\le p}-V_{\le p})
 &=G_W-2I+G_W^{-1}\\
 &=(I-G_W)^2G_W^{-1}.
\end{aligned}
$$
因此准确有
$$
\boxed{
\|W_{\le p}-V_{\le p}\|
\le\frac{\epsilon_p}{\sqrt{1-\epsilon_p}}.
}
\tag{3.3}
$$
这比对两塔分别用三角不等式更强，也没有额外出生数。

完整物理截断核准确为
$$
\mathscr K_{p}^{\rm phys}
=\ker L\cap\{N_{\ge x}\le p\}
=V_{\le p}\ker(\mathcal L_{\rm b}|_{\le p}).
\tag{3.4}
$$
等号使用全部出生和真正有界逆 $V_{\le p}^{-1}$，不只使用出生零的候选。
置
$$
k_r=P_{\mathscr K_p^{\rm phys}}f_1 .
$$
对任意 $z\in\ker(\mathcal L_{\rm b}|_{\le p})$，
$W^*V=I$、$V^*f_1=f_1$ 及 $k_{\rm b}=P_{\ker\mathcal L_{\rm b}}f_1$ 给
$$
\langle Wk_{\rm b},Vz\rangle
=\langle k_{\rm b},z\rangle
=\langle f_1,z\rangle
=\langle f_1,Vz\rangle .
$$
所以
$$
\boxed{P_{\mathscr K_p^{\rm phys}}Wk_{\rm b}=k_r.}
\tag{3.5}
$$
由于 $Vk_{\rm b}\in\mathscr K_p^{\rm phys}$，
$$
e_r:=Wk_{\rm b}-k_r
=P_{(\mathscr K_p^{\rm phys})^\perp}(W-V)k_{\rm b}.
$$
于是
$$
\boxed{
\|k_r\|\le1,\qquad e_r\perp\mathscr K_p^{\rm phys},\qquad
\|e_r\|\le
\vartheta_p:=\frac{\epsilon_p}{\sqrt{1-\epsilon_p}}.
}
\tag{3.6}
$$
核项现在就是原物理的完整最小投影，不是未经最小化的 $Vk_{\rm b}$。

将 (2.6) 逐层施加 $W$。创建交织一直保留最末 $p+1$ 行，
结合 (3.5)，得到原物理恒等式
$$
\boxed{
f_1-F_r=k_r+L^*\Psi_r+e_r,\qquad
F_r=(-1)^r q_r\otimes\omega_r,\qquad
\Psi_r=W_{\le p}\Psi_r^{\rm b}.
}
\tag{3.7}
$$
昂贵的 $q_r$ 和 $\Psi_r^{\rm b}$ 都没有出现在 (3.6) 右侧。
没有声称 $\Psi_r^{\rm b}$ 本身有统一范数。

$k_r,e_r,\Psi_r$ 的远孔均至多 $p$；
$F_r$ 恰在第 $r=p+1$ 远孔。每列都是有限层 Hilbert 向量。
原 $D$ 和 $L$ 有界；(3.7) 没有无界形式列或 MP 域捷径。

代表的准确原物理费用为
$$
\boxed{
\kappa_{m,r}^2:=\|F_r\|^2
=\sigma_r^2\left\|\big((C^*)^r\big)^\dagger\xi_{r-1}\right\|^2.
}
\tag{3.8}
$$
等价地，它是整个 $\mathcal F_r^\perp$ 上
$(C^*)^rC^r$ 的正逆在 $\xi_{r-1}$ 上的二次型，再乘 $\sigma_r^2$。

## 4. 原同 Q、同 w 与近平方根的整段高度

采用原同一 $\tau_{14}$ 强段序列和
$$
Q_m=d_m^2h_m,\qquad
e^{(25/2)d_m^3}\le x_m\le e^{13d_m^3},\quad h_m\le2x_m,
\quad \eta_m=e^{-6d_m^4}.
\tag{4.1}
$$
取
$$
P_m=\left\lfloor\frac{\sqrt{x_m+1}}{8(m+1)}\right\rfloor,
\qquad 1\le r\le P_m+1.
\tag{4.2}
$$
原连续权满足 $\delta_x\le3/(x+1)$，故
$$
\epsilon_{r-1}\le\frac1{16(m+1)^2},\qquad
\vartheta_{r-1}\le\frac1{8(m+1)^2}=:\vartheta_m .
\tag{4.3}
$$
同时 $P_m+1<h_m$，且 $Q_m\ge R_m+P_m+1$。
因此 (3.7) 中 $k_r\in K_{Q_m}$，
$\Psi_r$ 的原总孔至多 $R_m+r-1<Q_m$。
原低行身份给
$$
\boxed{
P_{\mathscr U_{Q_m}}(f_1-F_r)
=P_{\mathscr U_{Q_m}}e_r,\qquad
P_{\mathscr U_Q}=P_{V_Q}-P_{K_Q}.
}
\tag{4.4}
$$
这一步使用真实物理 $V_Q/K_Q$；没有将 boson 投影直接当原核投影。

固定同一个原 $w\in W$，记 $W_0=\|w\|$、
$\alpha=\langle w,f_1\rangle$ 和
$u_m=P_{\mathscr U_{Q_m}}w$。
原整窗 carry 结论为
$$
\|u_m-P_{\mathcal N_m\le Q_m}w\|
\le2\eta_m W_0 .
\tag{4.5}
$$
$F_r$ 与 $f_1$ 的原支撑都在 $Q_m$ 内，且远孔正交。
由 (4.4)–(4.5) 得到统一于 (4.2) 的准确锚误差
$$
\boxed{
|\langle w,F_r\rangle-\alpha|
\le W_0\vartheta_m+
2\eta_mW_0\sqrt{1+\kappa_{m,r}^2}.
}
\tag{4.6}
$$
$\vartheta_m$ 不乘 Green 范数。每个 $r$ 的强头来源均先按 (1.2)–(1.4)
选定，再进入同一实际 $Q_m$；不是按每个 cut 重新选择测试。

若还需 matched left 来源，对任意 $n\ge r$ 有
$$
U_n^*(f_1-F_r)=U_n^*e_r.
\tag{4.7}
$$
与精确旗代表不同，这里保留了误差的真实 $U_n^*e_r$；
不把它送过 $(L_n+H_n)^{-1}$ 或帽 inverse 后仍当作无权小量。
原全部 right 继续使用 $h_m$ 段，帽门仍是
$n+2h_m+R_m<Q_m$。

## 5. 全 m、全 r 的 Bessel 与无包络吸收

各 $F_r$ 只占一个 far 层，所以当 $\kappa_{m,r}>0$，
$$
a_{m,r}:=\frac{|\langle w,F_r\rangle|}{\kappa_{m,r}}
\le\|\beta_{m,r}w\|,\qquad
\beta_{m,r}=\frac{D_{x_m}^{\,r}P_{N_{\ge x_m}=r}}{\sigma_{m,r}} .
$$
已付整个高度块的 Bessel 界直接给
$$
\boxed{
\sum_m\sum_{\substack{1\le r\le P_m+1\\\kappa_{m,r}>0}}
a_{m,r}^2\le2W_0^2 .
}
\tag{5.1}
$$
没有按高度再乘 $P_m+1$。

假设 $\alpha\ne0$。由 (4.3)–(4.5)，可统一选取 $m_1$ 使
$$
W_0\vartheta_m+2\eta_mW_0\le|\alpha|/2
\qquad(m\ge m_1).
$$
于是这些 $m$ 的全部 $\kappa_{m,r}$ 都非零；否则 (4.6) 直接矛盾。
令 $\varepsilon_m=2\eta_mW_0$、$z_{m,r}=\kappa_{m,r}^{-1}$。
将 (4.6) 除以 $\kappa_{m,r}$，用
$\sqrt{1+z^2}\le1+z$ 得
$$
|\alpha|z_{m,r}
\le a_{m,r}+\varepsilon_m
 +(W_0\vartheta_m+\varepsilon_m)z_{m,r}.
$$
吸收最后一项，再平方求和：
$$
\boxed{
\sum_{m\ge m_1}\sum_{r=1}^{P_m+1}\kappa_{m,r}^{-2}
\le\frac8{|\alpha|^2}
 \left(2W_0^2+\sum_{m\ge m_1}(P_m+1)\varepsilon_m^2\right)
<\infty .
}
\tag{5.2}
$$
最后一个和的有限性有原参数的明确余量：
$$
(P_m+1)\eta_m^2\le h_m e^{-12d_m^4}
\le2\exp(-12d_m^4+13d_m^3),
$$
对 $m\ge10$ 可和。双塔误差 $\vartheta_m$ 只用于左侧吸收，
没有被错误地重复求和成 $(P_m+1)\vartheta_m^2$。

因此若以后能在这些真正来源上证明
$$
\kappa_{m,r}^2\le c_{m,r},\qquad
\sum_m\sum_{r\in\mathcal R_m}\frac1{c_{m,r}}=\infty
\quad
(\mathcal R_m\subset\{1,\ldots,P_m+1\}),
\tag{5.3}
$$
便可推出 $\langle w,f_1\rangle=0$。
该条件允许同时利用许多高度，且无需任何事先的
$\eta_m\kappa_{m,r}$ 包络。

## 6. 没有省略的剩余来源

(1.2) 是完整有限 Galerkin 正规方程，(1.4) 则是全强头 MP。
即使 $\xi_p\perp\ker C^{p+1}$，其最小原像仍可能经过所有更高核旗。
本稿没有把它改成 $\mathcal F_{p+1}$ 上的逆。

当 $r=2$ 时，$\xi_1$ 就是此前完整二远孔的返回源，
(3.8) 退回无罚两孔费用。较大的 $r$ 保留相应的完整 Galerkin 残量，
不靠重复同一个二孔上界来替代。
现已支付的是：所有这些来源可以同时进入原同 $w$ 锚，
双塔误差不乘昂贵 MP，且整段高度提供 (5.2) 的实际必要条件。

仍需证明 (3.8) 的有效费用，或在真实来源上满足 (5.3)。
(4.7) 的误差也未免费通过原 matched/hatted inverse。
因此这不是 ordinary 右费或 $N=M$ 的完成证明。
