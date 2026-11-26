# R271 附录：完整 Gram 列的位置能量与同源二阶物理孔矩

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下完整 $J=\infty$ 原未加权源的物理位置能量运输、辅助一阶能量比较及公共方差二阶孔矩已证明。**
本稿从同一 $f_1=e_1$ 出发。最后的残量是原全 $T_N$ 或 $T_Y$ 的
$T\mathcal H_T(s)^{-1}f_1$，不是 $J=1$ 的残量，
也不是原真 $F_0$ 的 $\xi_0$。
关键是对完整参考 $L_m$ 的正规方程使用一个与删除算子可交换的位置导数；
没有展开成须支付旧头幂范数的 $A_m^k$。

依赖：

- [指数远孔起点的相对全算子 Gram](R271-appendix-exponential-weight-cutoff-relative-global-gram-and-actual-weighted-residual.md)，尤其原 (1.1)、(5.2)--(5.7) 的完整列、闭域和尾截；
- [真实二阶孔矩与公共方差选择](R271-appendix-critical-second-hole-moment-and-common-log-variance-selection.md) §3 的原参数与最高零头母窗。该稿的 $J=1$ 矩结论不会被搬用到本稿。

## 1. 原完整源与一次公共辅助能量

令
$$
\mathcal H_T(s)=\sum_{j=0}^\infty\frac{(T^*)^jT^j}{j!s^j},
\qquad
a_T(s)=\mathcal H_T(s)^{-1}f_1,
$$
$$
k_T(s)=\mathcal R_{T,\infty}(s)a_T(s)
=\sum_{j=0}^\infty\frac{(-T)^ja_T(s)}{\sqrt{j!s^j}}\otimes e_j,
\qquad
\mu_T(s)=\sum_{j=1}^\infty
\frac{j\|T^ja_T(s)\|^2}{j!s^j}.
\tag{1.1}
$$
对每个 $s>0$，所有算子级数连同一次 $s$ 导数均按范数收敛。
因 $\mathcal H_T\ge I$，
$$
\|a_T(s)\|\le1,\qquad
\|k_T(s)\|^2=\langle f_1,a_T(s)\rangle\le1.
\tag{1.2}
$$
所有 inverse 仍是原 Hilbert 度量中的 inverse。

写 $M=\ker T$、$q(s)=\langle f_1,a_T(s)\rangle$。
对原 inverse 求导得到
$$
\boxed{\frac{dq(s)}{d\log s}=\mu_T(s)\ge0.}
\tag{1.3}
$$
由于
$$
I\le\mathcal H_T(s),\qquad
I+T^*T/s\le\mathcal H_T(s),
$$
及正逆的次序，$\mathcal H_T(s)^{-1}f_1\to P_Mf_1$ 强收敛。
具体地，分开 $f_1=P_Mf_1+g$，$g\perp M$；
对第二部分
$$
\|\mathcal H_T(s)^{-1}g\|^2
\le\langle g,\mathcal H_T(s)^{-1}g\rangle
\le\langle g,(I+T^*T/s)^{-1}g\rangle\longrightarrow0.
$$
在 $s\to\infty$ 时 $\mathcal H_T(s)\to I$。
因此
$$
\boxed{
\int_0^\infty \mu_T(s)\,\frac{ds}{s}
=1-\|P_Mf_1\|^2\le1.
}
\tag{1.4}
$$
这是同一个原 $T$ 的能量积分；后面移动 $m,y$ 时不改变 (1.1)。

还准确有
$$
\langle w,a_T(s)\rangle=\langle w,f_1\rangle
\quad(w\in M),
\tag{1.5}
$$
以及原正高度总能量
$$
\sum_{j\ge1}\frac{\|T^ja_T(s)\|^2}{j!s^j}
=q(s)-\|a_T(s)\|^2\longrightarrow0.
\tag{1.6}
$$

## 2. 完整参考列的物理位置能量恒等式

固定原 $m\ge10,d=2^m,y\ge m+d$，令
$$
L=L_m=A_m+D_{\ge m},
\qquad
\mathcal W_{m,y}=\sum_{m\le i<y}(i+1)^3 n_i,
\qquad
D_\omega=\sum_{m\le i<y}a_i(i+1)^3E_i,
\quad a_i=(i+1)^{-2}.
\tag{2.1}
$$
$\mathcal W_{m,y}$ 是有限位置上的有界正算子。
它与原头 $A_m$ 交换。尾删除算子逐位交换，所以准确有
$$
[\mathcal W_{m,y},L]=-D_\omega,
\qquad [D_\omega,L]=0,
\qquad \mathcal W_{m,y}f_1=0.
\tag{2.2}
$$
因此对每个整数 $j\ge1$，
$$
L^j\mathcal W_{m,y}
=\mathcal W_{m,y}L^j+jD_\omega L^{j-1}.
\tag{2.3}
$$
保留整个原 $A_m$；没有要求其按物理孔次数齐次。

逐位 Cauchy--Schwarz 给
$$
\|D_\omega v\|
\le\sigma_{m,y}\|\mathcal W_{m,y}^{1/2}v\|,
\qquad
\sigma_{m,y}^2
=\sum_{m\le i<y}\frac1{i+1}\le1+\log y.
\tag{2.4}
$$
这里使用 $\|E_iv\|^2=\langle n_iv,v\rangle$，不要求不同 $E_iv$ 正交。

先允许任意有限 $0\le J<\infty$，并取原
$$
a_{L,J}=H_{L,J}^{-1}f_1,\qquad
v_j=\frac{L^ja_{L,J}}{\sqrt{j!s^j}},
$$
$$
X_{L,J}^2=\sum_{j=0}^J\|\mathcal W_{m,y}^{1/2}v_j\|^2,
\qquad
\mu_{L,J}=\sum_{j=1}^Jj\|v_j\|^2.
$$
原正规方程 $H_{L,J}a_{L,J}=f_1$ 与 $\mathcal W_{m,y}a_{L,J}$ 配对。
用 (2.2)--(2.3) 并取实部，得到完整恒等式
$$
\boxed{
X_{L,J}^2
=-\frac1{\sqrt s}\operatorname{Re}
\sum_{j=1}^J\sqrt j\,
\langle v_j,D_\omega v_{j-1}\rangle.
}
\tag{2.5}
$$
它没有把辅助次数当物理孔数：左端一直是 $\mathcal W_{m,y}$ 的物理位置能量。
由 (2.4) 和列 Cauchy--Schwarz，
$$
X_{L,J}^2
\le\frac{\sigma_{m,y}}{\sqrt s}
\sqrt{\mu_{L,J}}\,
\left(\sum_{j=1}^J
\|\mathcal W_{m,y}^{1/2}v_{j-1}\|^2\right)^{1/2}
\le\frac{\sigma_{m,y}}{\sqrt s}\sqrt{\mu_{L,J}}X_{L,J}.
$$
故
$$
\boxed{\sqrt s\,X_{L,J}\le\sigma_{m,y}\sqrt{\mu_{L,J}}.}
\tag{2.6}
$$

相同公式对 $J=\infty$ 成立：
$\mathcal W_{m,y},D_\omega,L$ 都有界，factorial 保证全部配对级数绝对收敛；
直接对完整正规方程配对即可。
以下用 $k_L=\mathcal R_{L,\infty}\mathcal H_L^{-1}f_1$、$\mu_L$ 记此完整版本。
每次固定 $m,y,s$ 后 (2.6) 都是原完整最小者的等式后果。

## 3. 原母窗与完整 $T/L$ 列比较

固定 $0<s\le1$，取
$$
K=2^{40},\qquad y=\lceil K/s\rceil,\qquad
m=4\left\lfloor\frac{\log_2y}{8}\right\rfloor,
\qquad d=2^m,\qquad n=d/2,
$$
$$
L_s=1+\log\frac{K+1}{s},
\qquad L_0=1+\log(K+1).
\tag{3.1}
$$
已核的原参数满足
$$
m\in4\mathbb N,\quad m\ge20,\quad
\sqrt y/16<d\le\sqrt y,\quad y\ge m+d,\quad
K/y\le s\le2K/y,
$$
$$
y<e^{12n^3}\le e^{12d^3}.
\tag{3.2}
$$
最高零头的更小母窗也保留。
如需原有限物理支持，取 $r$ 与 $R,x,Q$ 为前稿 §3 的
$$
r\ \text{奇数},\quad r\le3y,\qquad
R=576(m+1)^2y^2,\quad x=m+R,\quad Q=R+r.
$$
则原高度窗成立，$Q<e^{26n^3}/4$，
基头改为 $m-1$ 时也准确支付 $(R+1)+(r-1)=R+r$。
这些只是比较和母支持参数，(1.1) 的原全 $T$ 源不会随它们更换。

现在严格使用
$$
\Gamma_y=32^{\mathcal N_{\ge y}},\qquad
\widehat\Gamma_y=\Gamma_y\otimes I.
$$
相对全 Gram 定理给原完整源的闭域估计
$$
\boxed{
\|\widehat\Gamma_y k_T(s)\|\le8/7,\qquad
\|\widehat\Gamma_y(k_T(s)-k_L(s))\|
\le e^{-3d^4/2}.
}
\tag{3.3}
$$
尤其同一列差也满足未加权界。
此处用的是该定理对任意 $y\ge m+d$ 的相对比较，
不是旧 $y=m+d$ 的绝对 $e^{81/s}$ 预算。

## 4. 辅助 $\sqrt j$ 尾的完整支付

(3.3) 本身只控制列范数，不能直接推出 $\mu_L$ 与 $\mu_T$ 的比较。
取已付的有限整数
$$
J_*=\left\lceil
\max\{d+y-m-1,\ 81e^2/s,\ 4d^4+2\}
\right\rceil.
\tag{4.1}
$$
原母窗给
$$
J_*/s\le e^{25d^3}<\mathscr R_m^2,
\qquad J_*\le e^{25d^3}.
\tag{4.2}
$$
完整 $X=L,T$ 都满足 $\|X\|\le9$、$\|a_X(s)\|\le1$。
所以
$$
\begin{aligned}
\|N_{\rm aux}^{1/2}P_{>J_*}k_X\|^2
&\le\sum_{j>J_*}j\frac{(81/s)^j}{j!}\\
&\le\sum_{j>J_*}je^{-j}
\le(J_*+2)e^{-J_*}.
\end{aligned}
\tag{4.3}
$$
第二步使用 $j!\ge(j/e)^j$ 及 $j\ge81e^2/s$。
第三步是几何级数的一次导数，不删除辅助 $\sqrt j$ 因子。

对前 $J_*$ 行使用 (3.3)，再加两个完整尾，
$$
\begin{aligned}
\|N_{\rm aux}^{1/2}(k_T-k_L)\|
&\le\sqrt{J_*}\,e^{-3d^4/2}
+2\sqrt{J_*+2}\,e^{-J_*/2}\\
&\le3\sqrt{J_*+2}\,e^{-3d^4/2}
\le e^{-d^4}.
\end{aligned}
\tag{4.4}
$$
最后由 (4.2) 和 $d\ge2^{20}$；更小的 $d\ge1024$ 也足够。
从而
$$
\boxed{\sqrt{\mu_L(s)}\le\sqrt{\mu_T(s)}+e^{-d^4}.}
\tag{4.5}
$$
这一步把移动 $L_{m(s)}$ 的辅助能量返回同一个固定 $T$，
之后才能使用 (1.4)。

## 5. 完整列中的物理位置能量运输

由于
$$
\|\mathcal W_{m,y}^{1/2}\|
\le\left(\sum_{i=0}^{y-1}(i+1)^3\right)^{1/2}
=\frac{y(y+1)}2\le y^2,
$$
(2.6)、(3.3)、(4.5) 直接给
$$
\begin{aligned}
\sqrt s\,\|\widehat{\mathcal W}_{m,y}^{1/2}k_T\|
&\le \sigma_{m,y}\sqrt{\mu_L}
+\sqrt s\,y^2e^{-3d^4/2}\\
&\le\sqrt{L_s}\sqrt{\mu_T}
+\sqrt{L_s}e^{-d^4}
+\sqrt s\,y^2e^{-3d^4/2}.
\end{aligned}
\tag{5.1}
$$
这里不需要 $\mathcal W_{m,y}$ 或其孔权保持未知列空间；
使用的是有界的真实物理位置乘子。

现在 $y\le e^{12d^3}$，故
$y^2e^{-3d^4/2}\le e^{-d^4}$。
而 $L_s\le26d^3$、$\log(1/s)\le12d^3$ 给
$\log(L_s/s)\le13d^3<2d^4$，所以
$\sqrt{L_s}e^{-d^4}\le\sqrt s$。
因此
$$
\boxed{
\sqrt s\,\|\widehat{\mathcal W}_{m,y}^{1/2}k_T(s)\|
\le\sqrt{L_s}\sqrt{\mu_T(s)}+2\sqrt s.
}
\tag{5.2}
$$

## 6. 二阶总物理孔矩：完整列同时控制

将总物理孔数分成
$$
\mathcal N=A+B+C,\qquad
A=\mathcal N_{<m},\quad
B=\mathcal N_{[m,y)},\quad
C=\mathcal N_{\ge y}.
$$
对三个真实物理部分分别估计。

首先 $A\le m$，所以 $\|\widehat A^{\,2}k_T\|\le m^2$。
其次，若中间区间有 $b$ 个孔，
$$
\mathcal W_{m,y}\ge\sum_{j=1}^b j^3\ge b^4/4;
$$
因此 $\|\widehat B^{\,2}k_T\|\le2\|\widehat{\mathcal W}_{m,y}^{1/2}k_T\|$。
最后，逐整数 $c\ge1$ 有 $c^2\le32^{c-1}$，故 (3.3) 给
$$
\|\widehat C^{\,2}k_T\|
\le\frac1{32}\|\widehat\Gamma_yk_T\|\le\frac1{28}.
\tag{6.1}
$$
特别，所有无限远孔二阶自然域已付。

记
$$
\mathcal A(s)
:=\sqrt s\,\|\widehat{\mathcal N}^{\,2}k_T(s)\|.
\tag{6.2}
$$
用 $(a+b+c)^2\le3(a^2+b^2+c^2)$ 及 (5.2)，
$$
\mathcal A(s)
\le\left(3m^2+12+\frac3{28}\right)\sqrt s
+6\sqrt{L_s}\sqrt{\mu_T(s)}.
$$
保守写为
$$
\boxed{
\mathcal A(s)
\le4(m(s)+2)^2\sqrt s
+6\sqrt{L_s}\sqrt{\mu_T(s)}.
}
\tag{6.3}
$$
低于 $m$ 的物理孔项 $m^2\sqrt s$ 被明确保留，没有以辅助次数替换。

由于 $m(s)+2\le L_s$，
$$
\boxed{
\mathcal A(s)^2
\le32L_s^4s+72L_s\mu_T(s).
}
\tag{6.4}
$$
从完整列的真实第 $j$ 行可同时读取
$$
\boxed{
\|\mathcal N^2T^ja_T(s)\|
\le\sqrt{j!}\,s^{(j-1)/2}\mathcal A(s)
\quad(j\ge1).
}
\tag{6.5}
$$
特别 $\|\mathcal N^2Ta_T(s)\|\le\mathcal A(s)$。
实际上 (6.2) 付的是全部行的加权平方和，不只是逐个固定 $j$。

## 7. 一次对数方差选择，保全部列

(1.4) 和 (6.4) 给完整积分
$$
\boxed{
\int_0^1\frac{\mathcal A(s)^2}{sL_s}\,ds
\le
32(L_0^3+3L_0^2+6L_0+6)+72.
}
\tag{7.1}
$$
此处用了
$\int_0^1[L_0-\log s]^3\,ds=L_0^3+3L_0^2+6L_0+6$。
所有非负行和与孔截断均可按 Tonelli 和单调收敛交换。

对任意 $L\ge L_0$，记同一个原 $T$ 的
$$
I_L^T=\int_{e^{-2L}}^{e^{-L}}\mu_T(s)\,\frac{ds}{s}.
\tag{7.2}
$$
由 (1.4)，$I_L^T\to0$。
在 $s=e^{-\ell}$、$L\le\ell\le2L$ 上，$L_s\le3L$。
对 (6.4) 的右端作普通 $\ell$ 平均，可选一个
$s_L\in[e^{-2L},e^{-L}]$ 使
$$
\boxed{
\mathcal A(s_L)^2
\le32L_{s_L}^4s_L+72L_{s_L}\mu_T(s_L)
\le2592L^3e^{-L}+216I_L^T
\longrightarrow0.
}
\tag{7.3}
$$
同一选择也使 $L_{s_L}\mu_T(s_L)\to0$。
于是原完整源沿这一次共同方差选择满足
$$
\|\mathcal N^2Ta_T(s_L)\|\longrightarrow0
$$
以及 (6.5) 中全部行共同的归一化二阶物理矩控制。
每个物理前缀的孔数平方均不超过 $\mathcal N^2$，
故无需为不同前缀或不同辅助行重复选择 $s$。
原配对 (1.5) 保持准确。

## 8. 范围及仍需支付的返回

这里完成了 $J=1$ 之外、真正原完整 Gram 源的二阶物理矩公共方差端点。
没有把移动 $m(s)$ 的 $\mu_L$ 当成固定算子的谱能量；
(4.1)--(4.5) 已把它完整返回 $\mu_T$。

(7.3) 仍是沿每个对数窗的一次选择，
不声明 (6.3) 右端对全部 $s\downarrow0$ 自动趋零。
所得物理二阶矩和全 $T$ 幂源关系可用于进一步分析源专属返回，
但这里没有证明一个可支付的真核修正，
没有改写为指数孔权右逆界，
没有宣称原真 $F_0$、实际 $S_x$ 的绝对 $\mathcal Z_\gamma$、
物理 MP 或真帽费用已经闭合。
原同一 $w/u$ 返回仍须按原接口继续；普通 Hilbert ISP 仍未完成。
