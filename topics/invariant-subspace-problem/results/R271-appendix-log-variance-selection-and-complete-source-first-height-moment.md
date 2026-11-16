# R271 附录：完整 Gram 的对数方差选择与同一原来源的一阶高度矩

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root；AI-assisted，GPT-6 Astra Pro。boundary_core 独立核对完整 inverse 求导及原来源条件。

**状态：已证明。** 对完整头 Gram 的 inverse 直接求对数方差导数，恰好得到实际最小源的一阶高度能量。因而可以先选择一次真实方差，再对所有合法原 cut 使用同一个来源。固定倍数方差窗给一阶高度矩趋零；扩大到 $[S_x,xS_x]$ 则给同一 $u_{m,Q,f}$ 的明确相对预算 $\Delta_{m,Q,f}^2/\log x$。还可选择趋于原物理方差的窗口，而不假定原强收敛具有某个速率。

这里控制的是实际 $a=H^{-1}g$ 的能量。它不把全深 MP 修复的系数自动当作线性函数，也不以一个塔范数下界代替修复上界。

依据为[真实强前缀与远尾方差完整 inverse 定理](R271-appendix-actual-strong-head-gram-comparison-and-true-far-variance-source-limit.md) §§4–5、[放大方差的原物理列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)，以及[原连续尾全相容塔的完整修复平方](R271-appendix-continuous-compatible-vacuum-tower-marginals-and-linear-deep-return-barrier.md) §5。

## 1. 完整空间上的准确求导

先在同一个有限维 Hilbert 头空间上固定 $C$、整数 $J\ge1$ 和向量 $g$。对 $s>0$ 定义
$$
H(s)=\sum_{j=0}^{J}\frac{(C^*)^jC^j}{s^j j!},\qquad
a(s)=H(s)^{-1}g,\qquad q(s)=\langle g,H(s)^{-1}g\rangle,
$$
$$
E_j(s)=\frac{\|C^ja(s)\|^2}{s^j j!}.
\tag{1.1}
$$
全空间上 $H(s)\succeq I$，所以 $H(s)^{-1}$ 存在且 $0\preceq H(s)^{-1}\preceq I$。以下没有先将 $H$ 压到 $g$ 的原支持，也没有要求各项 $(C^*)^jC^j$ 交换。

置 $t=\log s$。有限和逐项可导，且完整 inverse 的导数为
$$
\frac{dH}{dt}=-\sum_{j=1}^{J}\frac{j(C^*)^jC^j}{s^j j!},\qquad
\frac{dH^{-1}}{dt}=-H^{-1}\frac{dH}{dt}H^{-1}.
$$
因此有准确身份
$$
\boxed{\frac{dq}{d\log s}(s)=\sum_{j=1}^{J}jE_j(s).}
\tag{1.2}
$$
右侧非负、连续。特别 $q(s)$ 单调不减，且 $0\le q(s)\le\|g\|^2$。本稿只使用这个一阶导数，不宣称 $q$ 的更高对数导数非负。

对任意 $0<s_-<s_+$，积分得
$$
q(s_+)-q(s_-)
=\int_{\log s_-}^{\log s_+}\sum_{j=1}^{J}jE_j(e^t)\,dt.
\tag{1.3}
$$
令 $s_*$ 是紧区间 $[s_-,s_+]$ 上右侧被积函数的一个最小点。它是真正存在的有限参数选择，且
$$
\boxed{
\sum_{j=1}^{J}jE_j(s_*)
\le\frac{q(s_+)-q(s_-)}{\log(s_+/s_-)}.
}
\tag{1.4}
$$

## 2. 原强前缀、同一物理 forcing 与全部合法 cut

现在使用原定义
$$
d=2^m,\quad x=m+R,\quad C=A_m+D_{[m,x)},\quad
h=d+R,\quad 1\le J<h,
$$
$$
S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
m\ge10,\quad x+1\le d^{4/3}/8.
\tag{2.1}
$$
固定原有限物理 forcing $f$；在充分大的原头中把同一个向量加中间真空记作 $g$，其范数仍为 $\|f\|$。对所有 $s\ge S_x$，取 (1.1) 的完整 inverse 与原物理代表
$$
F_s=\sum_{j=0}^{J}\frac{(-C)^ja(s)\otimes\omega_j}{s^j j!},
\qquad \omega_j=(D_x^*)^j\Omega.
\tag{2.2}
$$
所引真实强前缀定理给，对于每个 $Q\ge R+J$，准确有
$$
P_{V_{m,Q}}F_s=P_{V_{m,Q}}f,\qquad
P_{K_{m,Q}}F_s=P_{K_{m,Q}}f.
\tag{2.3}
$$
故
$$
u_{m,Q,f}=(P_{V_{m,Q}}-P_{K_{m,Q}})f
=(P_{V_{m,Q}}-P_{K_{m,Q}})F_s
$$
在改变 $s$ 时是同一个实际向量。尤其
$$
\|u_{m,Q,f}\|^2\le\|F_s\|^2\le q(s)\le\|f\|^2.
\tag{2.4}
$$
令原缺口
$$
\Delta_{m,Q,f}^2=\|f\|^2-\|u_{m,Q,f}\|^2.
$$
只要 $s_-\ge S_x$，(2.4) 给
$$
0\le q(s_+)-q(s_-)\le\Delta_{m,Q,f}^2.
\tag{2.5}
$$
因此 (1.4) 的同一个 $s_*$ 同时满足所有合法 cut 的预算
$$
\boxed{
\sum_{j=1}^{J}jE_j(s_*)
\le\frac{\Delta_{m,Q,f}^2}{\log(s_+/s_-)},
\qquad Q\ge R+J.
}
\tag{2.6}
$$
选择 $s_*$ 只依赖 $m,R,J,f$ 与两端方差，不依赖 $Q$。这里既没有每个 cut 重选向量，也没有改变内部窗口的 partial、自然域或原 forcing。

## 3. 三个可用的真实方差窗

### 3.1 固定倍数窗的一阶矩趋零

令 $m\to\infty$，允许 $R_m,J_m$ 移动，但满足 (2.1)。取固定 $\lambda>1$ 及
$$
s_-=S_{x_m},\qquad s_+=\lambda S_{x_m}.
$$
因为 $x_m\to\infty$，两端方差都趋零。完整 inverse 强极限定理在两个端点给
$$
q_m(s_-),q_m(s_+)\longrightarrow\|P_Mf\|^2.
$$
用 (1.4) 选择一次 $s_m\in[S_{x_m},\lambda S_{x_m}]$，于是
$$
\boxed{\sum_{j=1}^{J_m}jE_{m,j}(s_m)\longrightarrow0.}
\tag{3.1}
$$
这不需要先给 $\epsilon_m=\sum_{j\ge1}E_{m,j}$ 一个速率。对每个固定 $c>0$，还立即有
$$
x_m\sum_{j\ge c x_m}E_{m,j}(s_m)
\le c^{-1}\sum_jjE_{m,j}(s_m)\longrightarrow0.
\tag{3.2}
$$
所以原连续塔线性下界指出的必要高层能量条件，可以由实际参数选择满足。此处尚未由必要条件推修复充分性。

### 3.2 对数相对预算

取更宽但仍趋零的区间
$$
s_-=S_x,\qquad s_+=xS_x.
$$
因 $S_x\le1/(3x^3)$，有 $xS_x\le1/(3x^2)\to0$，所选 $s_m$ 仍在真实强极限定理范围内。由 (2.6)，
$$
\boxed{
\sum_{j=1}^{J_m}jE_{m,j}(s_m)
\le\frac{\Delta_{m,Q,f}^2}{\log x_m}
\le\frac{\|f\|^2}{\log x_m}\longrightarrow0.
}
\tag{3.3}
$$
该选择仍一次适用于所有 $Q\ge R_m+J_m$，并且实际 $a_m,F_{s_m}$ 仍强趋 $P_Mf$。扩大方差并不免费保持后续任何未证的 MP 系数上界；那些系数必须在实际选中的 $s_m$ 上重核。

### 3.3 方差比趋一，仍不假收敛速率

若 $f=0$，所有结论平凡。若 $f\ne0$，定义真实端点缺口
$$
\delta_m=\frac{q_m(2S_{x_m})-q_m(S_{x_m})}{\|f\|^2}\longrightarrow0.
$$
对充分大 $m$，取
$$
\theta_m=\sqrt{\delta_m+x_m^{-1}}<\log2,
\qquad [s_-,s_+]=[S_{x_m},e^{\theta_m}S_{x_m}].
$$
由单调性与 (1.4)，可选其中一个 $s_m$ 使
$$
1\le\frac{s_m}{S_{x_m}}\le e^{\theta_m}\longrightarrow1,
$$
$$
\boxed{
\sum_j jE_{m,j}(s_m)
\le\frac{\|f\|^2\delta_m}{\theta_m}
\le\|f\|^2\sqrt{\delta_m+x_m^{-1}}
\longrightarrow0.
}
\tag{3.4}
$$
这是由实际完整 Gram 端点值定义的选择。没有声称 $\theta_m x_m\to0$，也没有声称该窗满足先前任何指定幂率的短高度参数。

## 4. 同时固定有限个 forcing

若需要对固定的有限族 $f_1,\ldots,f_n$ 共用一次方差，取任意固定正权 $w_\ell$，把 $q$ 换成
$$
q_{\mathrm{sum}}(s)=\sum_{\ell=1}^n w_\ell q_\ell(s).
$$
其导数恰为 $\sum_\ell w_\ell\sum_j jE_{\ell,j}$。同一个最小点给
$$
\sum_{\ell=1}^n w_\ell\sum_jjE_{\ell,j}(s_*)
\le\frac{\sum_\ell w_\ell(q_\ell(s_+)-q_\ell(s_-))}{\log(s_+/s_-)}.
$$
因此固定倍数窗同时控制每个指定源的一阶矩。这里量词是预先固定的有限族，没有从有限族控制宣称全空间算子范数控制。

## 5. 可以接入的修复费用与仍开的中段

若某个后继已经对同一实际 $a(s_m)$ 证明其正交平方费用为
$$
\mathcal R_m^2\le\sum_{j=1}^{J_m}\alpha_{m,j}E_{m,j}(s_m),
\qquad 0\le\alpha_{m,j}\le K_mj,
$$
则 (3.3) 准确给
$$
\mathcal R_m^2\le\frac{K_m}{\log x_m}\Delta_{m,Q,f}^2.
\tag{5.1}
$$
若 $K_m=o(\log x_m)$，这是同一缺口的趋零系数。固定 $K_m$ 也可与 (3.1) 或 (3.4) 合用。

但 canonical 全深修复的真实系数是
$$
\alpha_{m,j}=\frac{\mathcal M_{m,j}}{y_{m,j}}-2+y_{m,j},
\quad \mathcal M_{m,j}=\sigma_{m,j}^2\|(D_x^\dagger)^j\Omega\|^2,
\quad y_{m,j}=\frac{\sigma_{m,j}^2}{s_m^j j!}.
$$
即使另有 $\mathcal M_{m,j}=O(j)$，也不能删除 $1/y_{m,j}$ 后套用 (5.1)。全部中段系数或源依赖的完整 Schur 最小化仍须支付。原 $R=d$、$h=2d$、$Q\ge R+J$ 以及母 carry 窗保持不变；本稿没有据一阶高度矩证明 $N=M$ 或普通 Hilbert ISP。
