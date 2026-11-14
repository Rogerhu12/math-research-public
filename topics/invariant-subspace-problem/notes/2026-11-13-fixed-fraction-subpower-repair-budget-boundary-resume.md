# 固定比例末段的次幂最小修复预算

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。状态：以下固定比例分支的真实次幂能量预算已证明；早期分支及无权 $N=M$ 仍开放。

本稿接[联合核短塔](../results/R239-appendix-short-flag-towers-and-near-linear-nonvacuum-prefix-removal.md)和[完整首个三维块分解](../results/R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)。前者为 $q^{1-o(1)}$ 长度、但相对比例趋零的分支末段给范数趋零修复。本稿处理固定正比例的末段，代价是把趋零结论改为明确的 $q^{o(1)}$ 最小能量增长。两种结论的强度不同。

## 1. 只需一个固定的纯尾满射余量

沿原全整数头长 $m(q),d(q)$，取任意固定
$$
0<\alpha<\alpha_*:=
\frac{2(2^{1/3}-1)}{2\cdot2^{1/3}-1},\qquad
s=\lfloor\alpha q\rfloor,\qquad
n=q-s,\qquad J=m+2n.
\tag{1.1}
$$
写 $D=D_J$、$S_J=\sum_{j\ge J}(j+1)^{-4}$、$S=S_J$。
在恰好 $p$ 孔层，物理系数单调性给准确对角范数
$$
\left\|W_p\right\|
=\left\|\sum_{j\ge J}a_j^2n_j\bigm|_{\mathcal H_p}\right\|
=S_J-S_{J+p}.
$$
因此
$$
D_pD_p^*
=D_{p-1}^*D_{p-1}+S_J I-2W_{p-1}
\ge (2S_{J+p-1}-S_J)I.
\tag{1.2}
$$
对全部 $1\le p\le s+d$，积分比较的尾和渐近一致给
$$
\frac{S_{J+p-1}}{S_J}
=\left(\frac{J}{J+p-1}\right)^3(1+o(1))
\ge
\left(\frac{2(1-\alpha)}{2-\alpha}\right)^3+o(1).
$$
这里用了 $J\sim2(1-\alpha)q$、$s\sim\alpha q$ 和 $d=o(q)$；
各 $p$ 的下界最坏在 $p=s+d$。令
$$
\gamma_\alpha=
\frac12\left[
2\left(\frac{2(1-\alpha)}{2-\alpha}\right)^3-1
\right]>0.
\tag{1.3}
$$
其正性恰由 $\alpha<\alpha_*$ 保证，其中
$\alpha_*=0.3420\ldots$。对充分大的 $q$，所有 $p\le s+d$ 同时有
$$
\boxed{D_pD_p^*\ge\gamma_\alpha S I.}
\tag{1.4}
$$
因此逐层 canonical 右逆的范数不超过
$(\gamma_\alpha S)^{-1/2}$。本稿不要求 (1.4) 与 $S I$ 渐近相等。
这里保留了 $W_p$ 的准确物理尾和；用 $p a_J^2$ 代替它只能得到较窄的
$\alpha<1/4$ 范围。

## 2. 准确受限塔的粗范数，独立于 s

仍取
$$
\mathcal E_t=\ker D^{d+t}\cap\mathcal H_{s+t}
\quad(0\le t\le d).
$$
由短塔稿已证的核阶范数引理，
$$
\|D|_{\mathcal E_t}\|^2\le(d+t-1)S.
\tag{2.1}
$$
$D:\mathcal E_t\to\mathcal E_{t-1}$ 满射，且其最小右逆就是全层 canonical 右逆在受限源上的限制。

这次不使用近等距 Gram 递推，而取简单的标量塔：
$$
\mathfrak E_t=\mathcal E_0
  \oplus\bigoplus_{j=1}^t K_{s+j},
\qquad K_{s+j}=\ker D_{s+j}.
$$
标准降阶 $\mathfrak a_t$ 在旧基底 $\mathcal E_0$ 上为 $\sqrt{tS}$，在出生分量 $K_{s+j}$、$j<t$ 上为 $\sqrt{(t-j)S}$，并杀去新生分量。
这只建源层 $s$ 之上的塔，不声称 $D_s$ 在旧基底上为零。

令 $V_0=I$，按短塔稿相同的精确右逆递归定义 $V_t$，使其在新生分量上恒等，在旧塔上为
$$
V_t=\mathcal R_tV_{t-1}
      (\mathfrak a_t|_{\rm old}).
$$
于是准确有
$$
D V_t=V_{t-1}\mathfrak a_t.
\tag{2.2}
$$
由 (1.4)，
$$
\boxed{\|V_t\|\le\gamma_\alpha^{-t/2}\sqrt{t!}.}
\tag{2.3}
$$

逆的成本同样只取决于 $d,t$。对 $x\in\mathcal E_t$，正交分解为
$x=k+x^\perp$，其中 $k\in\ker D$、$x^\perp\perp\ker D$。
由 canonical 右逆的最小性，
$$
V_t^{-1}x=
k\ \oplus\
(\mathfrak a_t|_{\rm old})^{-1}V_{t-1}^{-1}D x.
$$
旧塔频率的最小值为 $\sqrt S$，且 (2.1) 可用于
$x^\perp\in\mathcal E_t$。因此
$$
\|V_t^{-1}x\|^2
\le\|k\|^2+
 (d+t-1)\|V_{t-1}^{-1}\|^2\|x^\perp\|^2.
$$
从 $V_0=I$ 归纳得到
$$
\boxed{
\|V_t^{-1}\|\le
 \sqrt{\frac{(d+t-1)!}{(d-1)!}}.
}
\tag{2.4}
$$
整个 $0,\ldots,d$ 塔可统一用
$$
\boxed{
K_{d,\alpha}:=
\left(\frac{2d}{\sqrt{\gamma_\alpha}}\right)^d
}
\tag{2.5}
$$
控制 $\sup_t\|V_t\|\sup_t\|V_t^{-1}\|$。对原自适应 $d(q)$，
$$
\log K_{d(q),\alpha}=O_\alpha(d\log d)=o(\log q),
\qquad K_{d(q),\alpha}^2=q^{o(1)}.
\tag{2.6}
$$
这里没有使用 $D^*$ 保核阶，也没有把 $V_t$ 当作酉算子。

## 3. 真实源的完整修复成本

令 $\mathcal P_n$ 是前 $n$ 个相邻配对的原始投影，在之后的尾部恒等。沿用
$$
C_n=\|\mathcal P_n\|\le e^{2/(m+1)},\quad
v=v_{m,q}(w),\quad r=L_mv,\quad w\in M.
$$
短塔稿 §5 的同一个 $q+d$ 原低投影已给全部未来层在
$\mathcal E_t$ 中的近似，其误差直和范数不超过
$C_ne^{-74d^4}\|w\|$。投影真实方程后，误差范数不超过
$$
C_n(26\eta_{m-1}+e^{-74d^4})\|w\|,
\qquad \eta_{m-1}\le e^{-80d^4}.
\tag{3.1}
$$
这些结论不要求塔近等距，仍适用于 (1.1) 的固定比例 $s$。

按 (2.2) 的标量旧基底链，定义原宽 $d$ 内的高尾修复
$$
c_t=(-1)^{t-1}V_t
 \left[\frac{A_m^t v_s^\circ}{\sqrt{t!\,S^t}}\right],
\quad 1\le t<d,\qquad v^\circ=\mathcal P_nv.
\tag{3.2}
$$
前缀单位原始张量按原位置补回。准确有
$$
L_mc=\mathcal P_nr,\qquad
D_m^dc=0,\qquad
c\in\operatorname{Ran}\mathcal P_n
 \cap\mathcal H_{[q+1,q+d-1]}^{(m)}.
\tag{3.3}
$$

标准塔的误差三角矩阵仍满足
$$
\Gamma_d=d6^dS^{-d/2}\le e^{d^4}.
$$
真实未来坐标的抽取及推回只支付 (2.5) 的完整条件数。因
$\log K_{d,\alpha}=o(d^4)$，对充分大的 $q$，
(3.1) 和原顶部误差经过全部变换后仍至多
$C_ne^{-70d^4}\|w\|$。由此得到
$$
\boxed{
\|c\|\le
K_{d,\alpha} C_n
 \|P_{[q+1,q+d-1]}^{(m)}w\|
 +C_ne^{-70d^4}\|w\|.
}
\tag{3.4}
$$
这是完整实际修复，不是只估算某个环境创建方向。

特别，在真正核的单位球上，其受限最小能量一致满足
$$
\boxed{
\min_{\substack{L_mc=\mathcal P_nr,\ D_m^dc=0\\
 c\in\operatorname{Ran}\mathcal P_n\cap
       \mathcal H_{[q+1,q+d]}^{(m)}}}
 \|c\|^2
\le q^{o(1)}\|w\|^2.
}
\tag{3.5}
$$
不从 (3.4) 声称 $\|c\|\to0$：任意 Hilbert 尾不必抵消一个增长的
$q^{o(1)}$ 因子。

## 4. 固定正比例的全部末段分支

在完整首个三维块分解中，
$$
\mathcal P_n=T_\infty+\sum_{i=n+1}^qT_i.
$$
令 $\mu_i^{[h]}(r)$ 是前稿明确在 $\operatorname{Ran}T_i$ 内最小化的分支能量，$h\ge d$。把 (3.3) 的 $c$ 一次施加完整分析界，得到
$$
\boxed{
\mu_\infty^{[h]}(r_q)^2+
 \sum_{i=n(q)+1}^q\mu_i^{[h]}(r_q)^2
\le A_q^2\|c\|^2
\le q^{o(1)}\|w\|^2.
}
\tag{4.1}
$$
此处末段含 $\alpha q+O(1)$ 个分支，仍没有乘分支数或
$\sqrt q$。$A_q=1+O(m(q)^{-1/2})$ 是已证的完整分析常数。
该预算与先前的近一次长度末段范数趋零结论并存，不将两者混同。

## 5. 临界增长必须由早期分支承担

用原宽 $h=d(q)$，定义
$$
\mathcal E_q^{\rm early}(w)=
 \sum_{i=1}^{n(q)}\mu_i^{[d(q)]}(r_q)^2.
$$
完整合成界和 (4.1) 给
$$
\lambda_q(w)^2
\le B_q^2\left[
 \mathcal E_q^{\rm early}(w)+q^{o(1)}\|w\|^2
\right],
\qquad B_q\to1.
\tag{5.1}
$$
因此原全部整数充分增长条件可以完全留给早期分支：
$$
\boxed{
\mathcal E_q^{\rm early}(w)
=O\!\left(q(\log q)^{2/3}\log\log q\right)
\quad\Longrightarrow\quad w\in N.
}
\tag{5.2}
$$
证明是把 (5.1) 代入原最小能量判据；$q^{o(1)}$ 为严格低阶。
等价地，任意非零真正缺陷必须满足
$$
\boxed{
\limsup_{q\to\infty}
\frac{\mathcal E_q^{\rm early}(w)}
 {q(\log q)^{2/3}\log\log q}=\infty.
}
\tag{5.3}
$$
这是一条必要增长约束，尚未排除它。

本稿为一个固定正比例的完整分支族给出了真正源上次幂的能量预算；
它不覆盖剩下的早期分支，不把投影 $T_iw$ 视为仍与 $N$ 正交，
也没有证明整个 $\lambda_q$ 具有该次幂界。普通无权 $N=M$ 和 ISP 继续开放。
