# R271 附录：固定比例实际修复的平方平均衰减与共同子序列

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_rebuild；root 指出固定头窗口中的重叠平方和可支付既有次幂费用。
状态：已证明。此稿把既有固定比例末段的 $q^{o(1)}$ 修复预算，升级为固定头长窗口内的指数小平方平均、密度趋一的好窗口以及同一有限源族上的共同趋零子序列。没有把该结论改写为全部 $q$ 上趋零。

## 1. 完整保留旧实际修复

固定两个实际边界之一，令 $M=\ker T$，并取任意固定
$$
0<\alpha<\alpha_*=
\frac{2(2^{1/3}-1)}{2\cdot2^{1/3}-1}.
$$
沿原全整数头选择
$$
m(q)=\max\left\{5,\left\lceil
\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right\},
\qquad d(q)=2^{m(q)}.
$$
记 $s(q)=\lfloor\alpha q\rfloor$、$n(q)=q-s(q)$，并保留原源
$r_{m,q}(w)=L_m v_{m,q}(w)$ 和原始前缀投影 $\mathcal P_{n(q)}$。

[R239 固定比例预算](R239-appendix-fixed-fraction-subpower-repair-budget.md)
§§1–3 已给
$$
\gamma_\alpha=
\frac12\left[
2\left(\frac{2(1-\alpha)}{2-\alpha}\right)^3-1
\right]>0,
\qquad
K_{d,\alpha}=\left(\frac{2d}{\sqrt{\gamma_\alpha}}\right)^d.
$$
取该稿 (3.2) 的固定线性构造，记其输出为
$c_{m,q}(w)=\mathcal C_{m,q}w$。
所有构造中的纯头、塔及投影在 $m,q$ 固定后都固定，$v_{m,q}$ 对 $w$ 线性，所以 $\mathcal C_{m,q}:M\to H$ 是有界线性算子。
对充分大的合法 $q$，完整身份是
$$
\boxed{
L_mc_{m,q}=\mathcal P_{n(q)}r_{m,q}(w),\quad
D_m^dc_{m,q}=0,\quad
c_{m,q}\in\operatorname{Ran}\mathcal P_{n(q)}
\cap\mathcal H_{[q+1,q+d-1]}^{(m)}.
}
\tag{1.1}
$$
特别，旧稿 (3.4) 给的是真实有限未来窗口，而不只是整个 Hilbert 尾：
$$
\boxed{
\|c_{m,q}(w)\|
\le K_{d,\alpha}C_{n(q)}\beta_{m,q}(w)
 +C_{n(q)}e^{-70d^4}\|w\|,
}
\tag{1.2}
$$
$$
\beta_{m,q}(w)=
\|P_{[q+1,q+d-1]}^{(m)}w\|,
\qquad C_{n(q)}\le C_m:=e^{2/(m+1)}.
$$
本稿使用 (1.1)--(1.2) 的原全部未来旗投影和 carry，不重选源或省掉条件数。

## 2. 在一个真正固定的头长内平均

对整数 $m\ge6$，置 $d=2^m$，并定义
$$
Q_m=\left\lfloor e^{d^3/4}\right\rfloor-2,
\qquad
I_m=\{q\in\mathbb Z:\lceil Q_m/2\rceil\le q\le Q_m\},
\qquad N_m=|I_m|.
\tag{2.1}
$$
对所有充分大的 $m$，
$$
\boxed{m(q)=m\quad\text{对全部 }q\in I_m.}
\tag{2.2}
$$
确实，$q+2\le\lfloor e^{d^3/4}\rfloor$，所以
$\log(q+2)\le d^3/4$；另一方面
$q+2>\tfrac12 e^{d^3/4}$，所以
$$
\log(q+2)>d^3/4-\log2>d^3/32.
$$
这恰落在使原向上取整等于 $m$ 的区间
$$
d^3/32<\log(q+2)\le d^3/4.
$$
也有 $4d\le q<e^{d^3/4}$，故每个参数都是原合法窗口。
此外，
$$
\boxed{N_m\ge\frac14e^{d^3/4}.}
\tag{2.3}
$$

由于这里的头 $m$ 真正固定，全部投影都使用同一尾孔层正交分解。
一个孔层指标至多属于 $d-1$ 个区间 $[q+1,q+d-1]$，所以
$$
\boxed{
\sum_{q\in I_m}\beta_{m,q}(w)^2
\le(d-1)\|w\|^2.
}
\tag{2.4}
$$
没有跨不同 $m$ 混用孔层，也没有对 $w$ 的尾衰减速度作假设。

## 3. 原实际修复算子的指数小平方平均

定义明确常数
$$
\boxed{
a_m=2C_m^2\left[
K_{d,\alpha}^2\frac{d-1}{N_m}
 +e^{-140d^4}
\right].
}
\tag{3.1}
$$
把 (1.2) 平方，使用 $(x+y)^2\le2x^2+2y^2$，再对 $q\in I_m$ 求和，(2.4) 给
$$
\boxed{
\frac1{N_m}\sum_{q\in I_m}
\|\mathcal C_{m,q}w\|^2
\le a_m\|w\|^2
\qquad(w\in M).
}
\tag{3.2}
$$
等价地，在同一个实际 $M$ 上有正算子不等式
$$
\boxed{
\frac1{N_m}\sum_{q\in I_m}
\mathcal C_{m,q}^*\mathcal C_{m,q}
\preceq a_mI_M.
}
\tag{3.3}
$$
这是平均后的原算子费用，不是把某个模型能量代入真实源。

由 (2.3) 及 $\log K_{d,\alpha}=O_\alpha(d\log d)$，
$$
\boxed{
a_m=\exp\!\left[-\frac14d^3+O_\alpha(d\log d)\right]
\longrightarrow0.
}
\tag{3.4}
$$
也即 $a_m=Q_m^{-1+o(1)}$。原 carry 的 $e^{-140d^4}$ 在此更小，所有固定常数已包含在 (3.1) 中。

## 4. 同一源、有限维源族及正密度的共同窗口

对每个固定 $w\in M$，从 (3.2) 可选 $q_m\in I_m$，使
$$
\boxed{
\|c_{m,q_m}(w)\|
\le\sqrt{a_m}\|w\|
=\exp\!\left[-\frac18d^3+O_\alpha(d\log d)\right]\|w\|
\longrightarrow0.
}
\tag{4.1}
$$
这些都是同一固定比例 $s(q_m)=\lfloor\alpha q_m\rfloor$ 的完整实际修复，并保留 (1.1)。

更一般地，令 $E\subset M$ 为任意固定 $k$ 维子空间，取其正交规范基 $w_1,\ldots,w_k$。
把 (3.2) 对这些向量求和，可选同一个 $q_m\in I_m$，使
$$
\sum_{j=1}^k\|\mathcal C_{m,q_m}w_j\|^2\le k a_m.
$$
Hilbert--Schmidt 范数控制算子范数，因而
$$
\boxed{
\|\mathcal C_{m,q_m}|_E\|\le\sqrt{k a_m}\longrightarrow0.
}
\tag{4.2}
$$
所以有限个实际源可以共同选窗，不必逐向量选互不相容的子序列。

若 $\rho$ 是支持在 $M$ 上的正迹类算子，由 (3.3) 取迹，也可选同一窗口满足
$$
\boxed{
\operatorname{Tr}(\mathcal C_{m,q_m}\rho\mathcal C_{m,q_m}^*)
\le a_m\operatorname{Tr}\rho.
}
\tag{4.3}
$$
本式只使用该同一密度的实际修复，不跨不同见证替换状态。

## 5. 好窗口的比例趋于一

对子序列还可给更强的计数结论。
固定 $w\ne0$ 和任意 $0<\eta<1/2$，令
$$
\mathcal B_m(w,\eta)
=\{q\in I_m:
\|\mathcal C_{m,q}w\|>Q_m^{-\eta}\|w\|\}.
$$
由 (3.2) 的 Markov 估计，
$$
\boxed{
\frac{|\mathcal B_m(w,\eta)|}{N_m}
\le a_m Q_m^{2\eta}
=Q_m^{2\eta-1+o(1)}\longrightarrow0.
}
\tag{5.1}
$$
因此在每个固定头长的整个上半合法窗口内，比例趋一的 $q$ 都使同一固定比例实际修复小于 $Q_m^{-\eta}\|w\|$。
对固定 $k$ 维 $E$，用上一节的 Hilbert--Schmidt 平方和，同样有
$$
\frac{|\{q\in I_m:
\|\mathcal C_{m,q}|_E\|>Q_m^{-\eta}\}|}{N_m}
\le k a_mQ_m^{2\eta}\longrightarrow0.
$$
不从这些估计声称存在一个对无限维 $M$ 的整个单位球都有效的共同点态窗口。

## 6. 整个固定比例末段的实际能量

原完整配对分解给
$$
\mathcal P_{n(q)}=T_\infty+\sum_{i=n(q)+1}^qT_i.
$$
其完整分析常数在固定 $m$ 的全部分支数上可统一取
$$
\overline A_m=e^{2/(m+1)}
\left(1+\sqrt{\frac6{m+1}}\right),
$$
见[R239 完整三维分解 §5](R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)。
对任意预先指定的合法修复宽度 $\ell\ge d$，由 (1.1) 和一次完整分析，
$$
\mathcal E_{m,q}^{\rm late}(w)
:=\mu_\infty^{[\ell]}(r_{m,q})^2
 +\sum_{i=n(q)+1}^q\mu_i^{[\ell]}(r_{m,q})^2
\le\overline A_m^2\|c_{m,q}(w)\|^2.
$$
因此
$$
\boxed{
\frac1{N_m}\sum_{q\in I_m}
\mathcal E_{m,q}^{\rm late}(w)
\le\overline A_m^2 a_m\|w\|^2.
}
\tag{6.1}
$$
沿 (4.1) 的子序列，整个 $\alpha q_m+O(1)$ 个末段分支的能量趋零；沿 (4.2) 的窗口，这对同一有限维实际源族一致成立。
没有额外的分支数因子。

对原宽 $d$ 或已定义双宽 $2d$ 的真正最小修复 $F_\ell^\dagger$，同一实际原像还给
$$
\left|
\|F_\ell^\dagger r_{m,q_m}(w)\|
-\|F_\ell^\dagger(I-\mathcal P_{n(q_m)})r_{m,q_m}(w)\|
\right|
\le\|c_{m,q_m}(w)\|\longrightarrow0.
\tag{6.2}
$$
这把真正总修复费沿共同子序列保留在早期源上，而不改变其来源。

## 7. 准确范围和剩余任务

旧固定比例稿没有把次幂常数与任意 Hilbert 尾的无率衰减相乘后宣称趋零；该限制仍正确。
本稿的新增输入是固定同一个 $m$，使用真实有限未来窗口的重叠平方和，再择子序列或平均。没有对 $\tau_q(w)$ 补设速率。

固定比例末段现在有平方平均趋零和共同实际子序列趋零，但仍未覆盖前面 $n(q)=(1-\alpha)q+O(1)$ 个分支。
这些移动前缀不能未经证明改成任意移动窗口，也不能把 $T_iw$ 当作仍属于 $W$。
本稿没有得到全源修复趋零、无权 $N=M$ 或普通 Hilbert ISP 的完整答案。
