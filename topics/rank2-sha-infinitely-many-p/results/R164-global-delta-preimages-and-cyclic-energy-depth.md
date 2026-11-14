# R164 — 真实全局 delta 原像的循环能量与整深度

**状态：已证明。日期：2026-11-12。**

对原整数范数零点，R128 的有限 p 商给真正的
$Q=\delta^aS$、$S\in A(F)$。同一原 formalizer 令
$z_S=\log_E(D_pS)/p\in I$，因此 $z_Q=\delta^az_S$。
保全部 p 完成，以 R161 的同一核定义对数能量，有
$$
 \mathcal E_1(z_Q)
       =-p\,\operatorname{Tr}_\Gamma((\delta^{a-1}z_S)^2),
                       \qquad a\ge1,
$$
$$
 \mathcal E_2(z_Q)
       =-p\,\operatorname{Tr}_\Gamma((\delta^{a-2}z_S)^2)
        +\frac p6\operatorname{Tr}_\Gamma((\delta^{a-1}z_S)^2),
                       \qquad a\ge2.
$$
这些是实际全局原像的迹，没有把局部加法原像当成椭圆点。

完整群环中 $\delta^{p-1}=N-pV$、$V$ 为整单位。
保留 N 项的精确幂公式给
$$
 v_p\mathcal E_1\ge\left\lceil\frac{2a}{p-1}\right\rceil,\qquad
 v_p\mathcal E_2\ge\left\lceil\frac{2a-2}{p-1}\right\rceil .
$$
奇有理参数使 R161 的 $I_i^{\rm rat}$ 与这些对数能量
相差 $p^2$（E17 为 $p^4$），所以除 p 后的首项正是
上面的真实平方迹。

在已付 $2\le a\le(p-3)/2$ 内，两个自动下界都只有一层 p。
准确 Selmer 长度尚未给实际平方迹额外的 p 整除或单位性。
原高度也仅能通过
$$
 (2\sin(\pi/p))^{2a}\widehat h(S)
          \le\widehat h(Q)\le4^a\widehat h(S)
$$
比较；不能把原小高度免费传给 S。

未证明实际能量无穷次非零。
[完整证明](../notes/2026-11-12-global-delta-preimages-and-cyclic-energy-depth.md)
保留整数原像、全部完成、N 项、精度和实际高度。
