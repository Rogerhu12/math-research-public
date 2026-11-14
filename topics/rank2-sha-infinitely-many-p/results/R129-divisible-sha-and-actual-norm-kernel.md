# R129：可除基 Sha 的实际范数核与第二层配对

日期：2026-11-12。状态：已证明。

使用 R126 的实际 $L/F$ 与固定 MW 点所给的两个非零局部像。
它们使 $E(F)$ 向唯一分歧位的二维局部范数商满射；这比仅有
Selmer 局部满射更强。设 $V$ 为处处局部范数的 $F$-有理点群，
$A=\ker N\operatorname{Res}_{L/F}E$、$S=\Sha(A/F)[p^\infty]$。
真实的全局、局部长正合列给
$$
 0\to V/N E(L)\to S\to
 \ker(N:\Sha(E/L)[p^\infty]\to\Sha(E/F)[p^\infty])\to0.
$$
R119 已知 $S$ 有限。若 $D_F,D_L$ 为两基域上的最大可除
$p$ 初级 Sha，则实际限制映射为满射 isogeny，且
$N\operatorname{res}=p$，从而
$$
 \ker(N|D_L)=\operatorname{res}(D_F[p]).
$$
该来源的 $S$-预像 $S_D$ 满足
$$
 0\to V/N E(L)\to S_D\to\operatorname{res}(D_F[p])\to0,
 \qquad S_D\subset S[\delta].
$$
最后一个包含由限制极化
$j^\vee j=\lambda_A=\iota\delta$ 及“可除群到有限群的映射为零”
直接推出。它不把 $D_F[p^n]$ 虚构为同一范数核中的更高层。

R122 的第二层配对还有准确的实际比较：
$$
 \beta_2(z,z')
   =\langle j_*z,j_*z'\rangle_{{\rm CT},E/L}
       \qquad(z,z'\in S[\delta^2]).
$$
即使 $\delta z,\delta z'$ 来自可除基 Sha，$j_*z,j_*z'$ 本身
仍可能在 $\Sha(E/L)/D_L$ 中非零。这说明下一层需要控制的
是这个指定有限商的真实配对，而不能仅借可除部分是 CT radical
就把第二层配对判零。

完整证明：
[工作证明](../notes/2026-11-12-divisible-base-sha-and-actual-norm-socle.md)。
本结果没有证明 Heegner 点的最终 $\delta$ 原始性，也没有把
$v_p(\ell+1)=1$ 的 tame 方向视作未构造的 $\mathbf Z_p$ 塔。
