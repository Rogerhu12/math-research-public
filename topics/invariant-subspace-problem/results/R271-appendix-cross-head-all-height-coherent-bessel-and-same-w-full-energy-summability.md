# R271 附录：跨头全高度 coherent Bessel 与原同 W 完整逆能量可和

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文把移动第一、第二远孔行推广到全部 $1\le j<h_m$。
原快速增长的远尾切点使完整 coherent 行满足绝对 Bessel 界，没有再乘高度数。
结合原同 $w$ 的 $V_Q/K_Q$ 低 forcing 恒等式，得到整个 $H_{\rm coh}^{-1}$ 之后
头误差与全部正高度能量的跨 $m$ 平方和。
所有 $s_m\ge S_{x_m}$ 的完整 boson Gram 也由同一量控制；
原 log-variance 选择进一步给带 $\log x_m$ 的第一高度矩可和。

coherent 代表只是向一个显式闭列空间的正交投影，通常不是物理真核。
本文未把这些能量直接送过原 MP、完整物理修复或帽返回逆，也未证明 $N=M$。

内积对第一变量线性。原物理表示始终为 N/Y 的共同 $\ell^2(\mathbb N_0)$。

依据：

- [原同一测试的最小 coherent 代表](R271-appendix-same-actual-test-minimal-coherent-representative-and-exact-residual.md)，§§1–2；
- [完整 forcing 同余及零源](R271-appendix-joined-quotient-coherent-forcing-congruence-and-complete-source-gram.md)；
- [原强尾同一顶部流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)，§2；
- [原相对孔 Riordan 参数](R271-appendix-relative-hole-riordan-conjugacy-full-bare-source-transport-and-uniform-budget.md)，§§5–6；
- [跨头有限前缀比较](R271-appendix-cross-head-finite-prefix-kernel-comparison-and-summable-first-row-gain.md)，§8，仅借用其明确参数检查；本稿的 Bessel 证明不调用其核修复。

## 1. 原切点、完整行与独立的头维数

记头维数为 $d_m=2^m$，本稿不使用原链权的 $d_i$ 记号。
从 $m\ge m_0\ge10$ 起，取原整数切点 $x_m=m+R_m$，
$$
C_m=A_m+D_{[m,x_m)},\qquad h_m=d_m+R_m,\qquad C_m^{h_m}=0.
$$
本稿的 Bessel 结论使用
$$
\boxed{
e^{(25/2)d_m^3}\le x_m\le e^{13d_m^3},\qquad
h_m\le2x_m.
}
\tag{1.1}
$$
原 $\tau_{14}$ 的偶数 $R_m=2\lceil2e^{\tau_{14,m}}\rceil$
满足这些不等式，且仍在已付 Riordan 环境范围内。

对每个 $m$，置
$$
D_m^>=\sum_{i\ge x_m}b_iE_i,\quad b_i=(i+1)^{-2},\quad z_i=b_i^2,\quad
S_m=\sum_{i\ge x_m}z_i,
$$
$$
\omega_{m,j}=(D_m^{>*})^j\Omega,\qquad
\sigma_{m,j}^2=\|\omega_{m,j}\|^2=(j!)^2e_j(z_{i\ge x_m}).
$$
所有 $\sigma_{m,j}>0$；$\sigma_{m,0}=1$。
令 $\mathfrak h_m=\mathcal H_{<x_m}$ 为完整物理强头空间，
并将远真空输出与 $\mathfrak h_m$ 等距识别。定义
$$
\beta_{m,j}=\frac{(D_m^>)^jP_{\{N_{\ge x_m}=j\}}}{\sigma_{m,j}},
\quad
\mathcal B_m f=(\beta_{m,j}f)_{1\le j<h_m},
$$
$$
\mathscr Y_m=\bigoplus_{j=1}^{h_m-1}\mathfrak h_m.
\tag{1.2}
$$
$(D_m^>)^j$ 在恰 $j$ 孔层上正是 $\omega_{m,j}$ 的读行。
因此
$$
\mathcal B_m\mathcal B_m^*=I_{\mathscr Y_m},\qquad
\mathcal B_m^*\xi
=\sum_{j=1}^{h_m-1}\xi_j\otimes\omega_{m,j}/\sigma_{m,j}.
\tag{1.3}
$$
同一个 $m$ 的全部行正交；没有逐行范数后再累加 $h_m$ 次。

## 2. 真跨头算子范数与无限乘积测度

设 $\ell>m$，令 $Q_\ell$ 是“至少一个物理孔位于 $i\ge x_\ell$”的正交投影。
(1.3) 给
$$
\operatorname{Ran}\mathcal B_\ell^*\subseteq\operatorname{Ran}Q_\ell.
$$
因此
$$
\|\mathcal B_m\mathcal B_\ell^*\|^2
\le\|\mathcal B_mQ_\ell\mathcal B_m^*\|.
\tag{2.1}
$$
$Q_\ell$ 保持 $m$ 的总远孔数，所以 (2.1) 右侧按 $j$ 真正块对角。
其第 $j$ 块是强头上的标量恒等：
$$
p_{m,j,\ell} I_{\mathfrak h_m},\qquad
p_{m,j,\ell}
=\Pr_{\mu_{x_m,j}}\{I\cap[x_\ell,\infty)\ne\varnothing\},
$$
其中原概率严格为
$$
\mu_{x,j}(I)=\frac{\prod_{i\in I}z_i}{e_j(z_{i\ge x})},
\qquad |I|=j.
$$
故右侧范数取 $\max_j p_{m,j,\ell}$，不取各 $j$ 的和。

下面的恒等式全部为非负绝对收敛的级数；也可先截有限位再取单调极限：
$$
j e_j
=\sum_{|I|=j-1}z_I\sum_{i\notin I}z_i
\ge S_{x+j-1}e_{j-1}.
\tag{2.2}
$$
原因是任何 $j-1$ 个位置至多删去最强的前 $j-1$ 个平方权。
另一方面，
$$
p_{m,j,\ell}
\le\sum_{i\ge x_\ell}\Pr(i\in I)
\le S_{x_\ell}\frac{e_{j-1}}{e_j}
\le\frac{jS_{x_\ell}}{S_{x_m+j-1}}.
$$
于是
$$
\boxed{
\|\mathcal B_m\mathcal B_\ell^*\|^2
\le\frac{h_mS_{x_\ell}}{S_{x_m+h_m}}.
}
\tag{2.3}
$$
此式已经包含原全高度 $j<h_m$、全部强头来源及每个 tail collision。

原积分比较
$$
\frac1{3(y+1)^3}\le S_y\le\frac1{3y^3}
$$
及 $h_m\le2x_m$ 给
$$
\|\mathcal B_m\mathcal B_\ell^*\|
\le\sqrt{128}\,\frac{x_m^2}{x_\ell^{3/2}}.
$$
若 $k=\ell-m\ge1$，由 (1.1)、$d_\ell^3=8^k d_m^3$，
$$
\log\|\mathcal B_m\mathcal B_\ell^*\|
\le\tfrac12\log128+
\left(26-\tfrac{75}{4}8^k\right)d_m^3
\le-(k+1)\log2.
\tag{2.4}
$$
最后一步可用 $8^k\ge8k$；
其左负系数绝对值至少 $124k\,d_m^3$，充分大于右边所需常数。

有限 block Gram 的标量 Schur 行和因此至多
$1+2\sum_{k\ge1}2^{-(k+1)}=2$。
取有限和后按单调极限，有整个物理 Hilbert 空间上的真行界
$$
\boxed{
\sum_{m\ge m_0}\|\mathcal B_mw\|^2\le2\|w\|^2
\qquad(w\in\mathcal H).
}
\tag{2.5}
$$
它不使用 $w\in W$，也不使用任何头逆或最小源比较。

## 3. 完整 coherent 逆及准确的物理范数身份

现在对同一个实际 $w\in W$，取
$$
g_m=P_{x_m}w\in\mathfrak h_m,\qquad W_0=\|w\|.
$$
这里 $P_{x_m}$ 是远位全真空的原物理投影；
没有改成另一无限张量积中的参考真空。

在整个 $\mathfrak h_m$ 上定义
$$
H_m^{\rm coh}
=\sum_{j=0}^{h_m-1}\frac{(C_m^*)^jC_m^j}{\sigma_{m,j}^2}\ge I,
\quad a_m=(H_m^{\rm coh})^{-1}g_m,
$$
$$
\mathcal R_m^{\rm coh}a
=\sum_{j=0}^{h_m-1}
 \frac{(-C_m)^ja\otimes\omega_{m,j}}{\sigma_{m,j}^2},
\qquad
f_m^{\rm coh}=\mathcal R_m^{\rm coh}a_m.
$$
不同远孔层正交，给
$$
(\mathcal R_m^{\rm coh})^*\mathcal R_m^{\rm coh}=H_m^{\rm coh},
\qquad
(\mathcal R_m^{\rm coh})^*i_{0,m}=I.
$$
所以 $f_m^{\rm coh}$ 是 $i_{0,m}g_m$ 向
$\operatorname{Ran}\mathcal R_m^{\rm coh}$ 的真正交投影。
**不把这个闭列空间声称为 $\ker(C_m+D_m^>)$。**

写
$$
\xi_{m,j}=\frac{(-C_m)^j a_m}{\sigma_{m,j}}\quad(1\le j<h_m),
\qquad
f_m^{\rm coh}=i_{0,m}a_m+\mathcal B_m^*\xi_m,
$$
$$
\Delta_m=\|g_m\|^2-\langle g_m,a_m\rangle\ge0.
$$
准确有
$$
\boxed{
\|i_{0,m}g_m-f_m^{\rm coh}\|^2=\Delta_m
=\|g_m-a_m\|^2+
 \sum_{j=1}^{h_m-1}\frac{\|C_m^ja_m\|^2}{\sigma_{m,j}^2}.
}
\tag{3.1}
$$
特别 $\|\xi_m\|^2\le\Delta_m$。
这里的逆从未限制到 $g_m$ 的低孔或低整数头范围。

## 4. 原同一个 $u_m$ 给出可和缺陷

选原合法母窗口
$$
4d_m\le Q_m\le\exp((1601/64)d_m^3),\qquad
Q_m\ge R_m+h_m-1.
\tag{4.1}
$$
固定同一个 $w$，
$$
u_m=(P_{V_{Q_m}}-P_{K_{Q_m}})w,\qquad
\|u_m-P_{\mathcal N_m\le Q_m}w\|
\le2\eta_mW_0,\quad \eta_m=e^{-6d_m^4}.
\tag{4.2}
$$
$\mathcal N_m$ 是原 $m$ 后总孔数。
(4.2) 是原定理对整个允许 $Q_m$ 窗的一致估计。

父稿 §2 的真实低 forcing 恒等式为
$$
P_{V_{Q_m}}(D_m^{>*})^ji_{0,m}
=(-1)^j(P_{V_{Q_m}}i_{0,m})(C_m^*)^j,
\quad j\le Q_m-R_m.
$$
其证明使用
$(D^*)^j-(-C^*)^j=(C+D)^*
\sum_{\ell<j}(D^*)^{j-1-\ell}(-C^*)^\ell$；
中间向量原总孔数至多 $R_m+j-1<Q_m$。
$K_{Q_m}$ 的恒等式同样成立。
由 (4.1)，覆盖全部 $j<h_m$，所以
$$
(P_{V_{Q_m}}-P_{K_{Q_m}})
(i_{0,m}g_m-f_m^{\rm coh})=0.
\tag{4.3}
$$
完整零源与非零源都保留；没有用“coherent 列是真核”的错误替代。

差向量在原总孔数 $\le R_m+h_m-1\le Q_m$ 上。
对 (4.2) 配对，利用 (4.3) 与 (3.1) 得
$$
\left|\langle w,i_{0,m}g_m-f_m^{\rm coh}\rangle\right|
\le2\eta_mW_0\sqrt{\Delta_m}.
$$
又 $g_m=P_{x_m}w$，所以左边准确为
$$
\left|\Delta_m-\langle\mathcal B_mw,\xi_m\rangle\right|.
$$
因此，无论 $\Delta_m$ 是否为零，
$$
\boxed{
\sqrt{\Delta_m}\le\|\mathcal B_mw\|+2\eta_mW_0.
}
\tag{4.4}
$$
结合完整全高度行 (2.5)，最终得到
$$
\boxed{
\left(\sum_{m\ge m_0}\Delta_m\right)^{1/2}
\le\left(\sqrt2+2\Big(\sum_{m\ge m_0}\eta_m^2\Big)^{1/2}\right)W_0.
}
\tag{4.5}
$$
例如也可取保守平方界
$\sum_m\Delta_m\le(4+8\sum_m\eta_m^2)W_0^2$。

由 (3.1)，这同时支付
$$
\boxed{
\sum_m\left[
\|g_m-a_m\|^2+
\sum_{j=1}^{h_m-1}\frac{\|C_m^ja_m\|^2}{\sigma_{m,j}^2}
\right]\le(4+8\sum_m\eta_m^2)W_0^2.
}
\tag{4.6}
$$
全部高度先共同进入 $\mathcal B_m$；没有把仅逐列强收敛相加。

(1.1) 下可明确取 $Q_m=d_m^2h_m$；
则 $Q_m<e^{14d_m^3}$，(4.1) 与全部原低 forcing 门同时成立。
如后续需要真帽，仍取
$Q_m/2\le n\le Q_m-R_m-2h_m-1$，
其 $h_m/N_m\le3/d_m^2$；
本稿不因此自动支付任何帽后的逆范数。

## 5. 任意完整 boson 方差与整个高度能量

对每个 $m$ 任取 $s_m\ge S_m$，可依同一个 $w$ 与原头选择，
但在使用后续所有 cut 前固定。定义完整头 Gram
$$
H_{C_m}(s)=\sum_{j=0}^{h_m-1}\frac{(C_m^*)^jC_m^j}{j!s^j},
\quad a_{m,s}=H_{C_m}(s)^{-1}g_m,
$$
$$
E_{m,j}(s)=\frac{\|C_m^j a_{m,s}\|^2}{j!s^j},\quad
q_m(s)=\langle g_m,a_{m,s}\rangle,\quad
d_m(s)=\|g_m\|^2-q_m(s).
$$
由原 $e_j\le S_m^j/j!$，
$$
\sigma_{m,j}^2\le j!S_m^j,\qquad
I\preceq H_{C_m}(s)\preceq H_m^{\rm coh}\quad(s\ge S_m).
$$
正逆的 Loewner 序给
$$
0\le d_m(s)\le\Delta_m.
\tag{5.1}
$$
完整正规方程还准确给
$$
\boxed{
d_m(s)=\|g_m-a_{m,s}\|^2+\sum_{j=1}^{h_m-1}E_{m,j}(s).
}
\tag{5.2}
$$
所以任意上述选参族都满足
$$
\boxed{
\sum_m\left[
\|g_m-a_{m,s_m}\|^2+\sum_{j=1}^{h_m-1}E_{m,j}(s_m)
\right]\le\sum_m\Delta_m<\infty.
}
\tag{5.3}
$$
这是整个头逆后的来源，不是逐 primitive 或低头压缩逆。

特别 $P_{x_m}w\to w$ 在原物理表示中强成立，
故这些 $a_{m,s_m}\otimes\Omega\to w$；
新结论实质在 (5.3) 的可和误差，而非重报一个无速率强极限。
这里不把任意大的 $s_m$ 自动解释成小物理核残量。

## 6. log-variance 第一高度矩的带权可和选择

固定 $m$。由于所有头矩阵有限且 $H_{C_m}(s)\ge I$，
对 $\log s$ 的完整非交换逆求导给
$$
\frac{dq_m(s)}{d\log s}
=\sum_{j=1}^{h_m-1}jE_{m,j}(s)
=:F_{1,m}(s)\ge0.
\tag{6.1}
$$
没有假设更高导数保持正性。

对任意预定 $\lambda_m>1$，
$$
\int_{S_m}^{\lambda_mS_m}F_{1,m}(s)\frac{ds}{s}
=q_m(\lambda_mS_m)-q_m(S_m)
\le d_m(S_m)\le\Delta_m.
$$
连续性保证可选同一个
$s_m\in[S_m,\lambda_mS_m]$，使
$$
\boxed{
(\log\lambda_m)F_{1,m}(s_m)\le\Delta_m,\qquad
\sum_m(\log\lambda_m)F_{1,m}(s_m)
\le\sum_m\Delta_m.
}
\tag{6.2}
$$
选参只依同一个 $g_m,C_m$，先于全部 $Q_m$ 内 cut 使用。
例如 $\lambda_m=x_m$ 时，
$s_m\le x_mS_m\le(3x_m^2)^{-1}\to0$，且
$$
\boxed{
\sum_m(\log x_m)\sum_{j=1}^{h_m-1}jE_{m,j}(s_m)<\infty.
}
\tag{6.3}
$$
它加强了同一 log-variance 窗的第一矩预算；
没有免费控制任意更高阶矩或错误的普通公共塔。

## 7. 保留的实际门

(4.6)、(5.3)、(6.3) 是同一个原 $w$、
移动强头 $g_m=P_{x_m}w$、完整来源逆与全部高度的真实可和量。
它们不意味着 $\mathcal R_m^{\rm coh}a_m$ 属于物理真核；
硬核下 $D\omega_{j+1}$ 一般不是 $\omega_j$ 的标量倍数。

若把这些列再送入原物理修复、顺次 MP、零源 Schur 或
$P_{\widehat{\mathscr E}}K_{\rm amb}^{-*}$，
仍必须证明该准确映射的费用与这里的能量相容。
不能把已付可和量乘一个未经控制的增长逆范数，
也不能从 (6.3) 宣称原普通封口或 $N=M$ 已闭合。
