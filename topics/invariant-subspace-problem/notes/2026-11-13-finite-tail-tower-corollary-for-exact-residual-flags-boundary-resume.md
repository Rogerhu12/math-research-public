# 有限尾塔法对准确联合旗的直接推论

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：已证明的接口补充；不是新的无权增长界。

本稿是 [R239 闭链与 Riccati](../results/R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md) 有限尾塔证明的直接应用，承接 [R271 实际残量正交旗与准确源 Gram](../results/R271-appendix-orthogonal-residual-flags-and-exact-source-gram.md)。它补证后者 $S_{\rm flag}$ 的固定有限层闭像，并确认受控原始投影准确保留这些旗。

## 1. 向下延长同一个有限尾塔

固定 $m,q$，$d=2^m$，$q\ge d-1$。令最低层
$$
b=q-d+1\ge0,
$$
考虑纯尾层 $H_b,H_{b+1},\ldots,H_{q+d}$。
取覆盖这个有限源层范围及所需阶数的同一个相容族 $R_k$。
令
$$
K_b=H_b,\qquad K_s=\ker(D:H_s\to H_{s-1})
\quad(b<s\le q+d).
$$
如原闭链稿，有限三角映射
$$
V_p:\bigoplus_{s=b}^pK_s\to H_p,\qquad
V_p((h_s))=\sum_{s=b}^pR_{p-s}h_s
\tag{1.1}
$$
是有界同构：从 $D^{p-b}$ 的坐标开始逐个剥离即可。
所有常数只断言对固定 $m,q$ 有限。

若 $p-h\ge b$，相容关系给
$$
D^hV_p((h_s))
=V_{p-h}((h_s)_{s\le p-h}).
$$
因此
$$
\boxed{
V_p^{-1}\ker(D^h|_{H_p})
=\bigoplus_{s>p-h}K_s.
}
\tag{1.2}
$$
这是对实际删除核的精确坐标识别，不是范数比较。
基空间 $K_b=H_b$ 保留任意尾向量；张量原头后也保留任意原头系数。

## 2. 准确联合旗仍化成有限矩阵直和

R271 的联合旗为
$$
\mathscr C_{\rm flag}
=\bigoplus_{t=1}^d
 \bigoplus_{i=0}^{d-t}
 e_i\otimes
 \ker(D^{d-i}|_{H_{q+t}}).
$$
每个删除目标层都在上述塔内，因为
$$
(q+t)-(d-i)=b+(t+i-1)\ge b.
$$
由 (1.2)，在 $I_{\rm head}\otimes\bigoplus_pV_p$ 下，
$\mathscr C_{\rm flag}$ 恰成为一个有限坐标子空间。

旧内部输出 $S_0=A+\mathbb D$ 在每个出生空间 $K_s$ 上仍是有限矩阵
$A+\text{有限后移}$ 张量 $I_{K_s}$。把其定义域限制到刚识别出的坐标子空间，只是选取该有限矩阵的相应列。因此
$$
S_{\rm flag}=S_0|_{\mathscr C_{\rm flag}}
$$
经有界源/目标同构后，是有限个有限矩阵张量恒等算子的直和。
每个这样的像闭，故
$$
\boxed{
\operatorname{Ran}S_{\rm flag}
\text{ 与 }\operatorname{Ran}S_{\rm flag}^*
\text{ 均闭。}
}
\tag{2.1}
$$

特别，R271 §6 的
$$
\inf_z\bigl\|
P_{\mathscr C_{\rm flag}}(D_0^*y-S_0^*z)
\bigr\|^2
$$
可以取到。把 $z$ 限制到 $\ker S_{\rm flag}^*$ 的正交补后，
极小链唯一，且对固定 $m,q$ 有界依赖于 $y$。
本推论没有给出足以直接吸收真实 carry 的统一范数；不能据此删除末端泄漏或宣布完整旗 Gram 已受控。

## 3. 原始投影保留两个准确旗

若一个尾算子 $P$ 保持每个尾孔层并与 $D$ 交换，则
$$
P\ker(D^h|_{H_p})\subseteq\ker(D^h|_{H_p}).
$$
因此它在原头张量恒等后保留 R271 的残量旗
$$
\mathcal R_{m,q}
=\bigoplus_{i=0}^{d-2}e_i\otimes\ker(D^{d-i-1}|_{H_q})
$$
以及上述 $\mathscr C_{\rm flag}$。
若 $P$ 是投影，$I-P$ 同样保留这两个空间。

特别，配对斜投影以及
[指数秩局部原始投影](2026-11-13-high-rank-primitive-removal-and-full-prefix-projection-obstruction-boundary-resume.md)
都满足这两个条件。所以此前的
$r=Pr+(I-P)r$ 无权小修复及最小能量差估计，准确发生在
$G_{\rm flag}$ 对应的同一合法源与全部可行链内；它们没有绕过或放宽 R271 的联合核条件。
