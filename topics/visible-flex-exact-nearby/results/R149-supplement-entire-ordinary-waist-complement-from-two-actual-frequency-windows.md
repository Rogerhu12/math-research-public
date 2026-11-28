# R149 ASQ15. All ordinary waist frequencies above the original reference head

Use the actual preconditioned equation [ASQ10.6](R149-supplement-practical-high-cut-with-paid-coordinate-errors.md). Set $L=2^{20}$, $P_M=P_{[97,L]}$, $P_H=P_{[L+1,\infty)}$, $P=P_M+P_H$. For the *same* full physical receiver $E=E_\partial^{\rm fr}+\Delta_\partial$ put
$$
         c=\|P_{97}E:X_{\rm fr}^{-4/3}\to Y_a^0\|,\qquad
         h=\|P_HE:X_{\rm fr}^{-4/3}\to Y_a^0\|.
$$
Write $\mathcal L$ for the complete operator in ASQ10.6. The four true operator norms of the compression of $\mathcal L-Id$, in rows/columns $M,H$, have simultaneous majorant
$$
   \mathcal B=
   \begin{pmatrix}
        .44+.1c & .71+9c\\ .00004+.1h & .02+9h
   \end{pmatrix}.                                           \tag{ASQ15.1}
$$
Every coordinate entry is unconditional. For the physical sources only the displayed two independently qualified output norms remain. The following alternatives each imply an inverse on the **whole** ordinary complement $n\ge97$,
$$
 (c\le3,\ h\le1/32)\qquad\text{or}\qquad(c\le4,\ h\le1/64).   \tag{ASQ15.2}
$$
Thus the original $J=2^{4608}$ split and the entire 65535-mode lower complement require no additional ordinary matrix once a physical gate in (ASQ15.2) is established. Both inequalities concern the actual selected original WPL row, with positive feedback for the coupled problem. They are sufficient tests, not asserted physical estimates. The remaining ordinary head has exactly 96 real coordinates and the unchanged physical border.

## The two right-hand windows

All Fourier signs below use their original unit real reflected basis. For $n\in M$ the complete [ASQ14 readback](R149-supplement-original-WMA-head-on-the-true-signed-waist-inverse.md) gives $g_n=1/(4n|q_n|)<.573$. Consequently
$$
 \|I\bar G P_M\|<.573,\quad
 \|I^2\bar G P_M\|<.573/388,\quad
 \|P_{97}C^{-1}A\bar G P_M\|_{\dot H^{-1}}
    <1.11(.573)(1+1.43/388)<.64.                          \tag{ASQ15.3}
$$
The last estimate is [ASQ12.5](R149-supplement-all-positive-i-safe-modes-in-the-physical-waist-square.md)'s proof with the actual smaller head budget. After the true intervening $P_{97}$ one additional $1/3$ derivative costs at most $388^{-1/3}$. Since $\|S\|_{-4/3}<1.1$, the physical right factor costs $<.1$.

For the entire infinite $H$, WCS.11 and the qualified CYA bound give $g_n\le512<513$. Thus $\|I^2\bar G P_H\|<513/(4L)$ and $\|\bar G P_H\|_{H^{-4/3}}\le512(4L)^{-1/3}$ by WCS.13. ASQ10.12 proved the bound $1.001$ for $A$ on *any input supported at $n\ge65536$* in this window; $C^{-1}$ costs $5/2$. Both genuine projections have norm at most one. Hence the true physical right factor costs
$$
             (1.1)(5/2)(1.001)512(4L)^{-1/3}<9.              \tag{ASQ15.4}
$$

For the four coordinate blocks, write $V_N=\|P_{\ge N}v\|_{A^0}$, $A_N=\|P_{\ge N}\alpha\|_{A^0}$. The true [ASQ10](R149-supplement-practical-high-cut-with-paid-coordinate-errors.md) bounds and $w=v-\alpha$ give
$$
 V_{49}<.008,\quad V_{194}<.00024,\quad V_{L/2}<10^{-11},\qquad
 A_{L/2}\le .023/\sqrt{8(L/2-1)},\quad V_{L/2}+A_{L/2}<.000012 .
$$
We shall use the latter number for either $\alpha$ or $w$ tails at or above $L/2$. All same-sign multiplication bounds follow from the two-sign Wiener norm with the same physical Fourier convention.

## Opposite signs in the four true positions

For output in $M$ the cost of $P_M Q_a T_iD$ on $\dot H^{-1}$ is $<.32$ by ASQ12. For output in $H$, use the already proved $\operatorname{Re}p'>.9$ on $S_{1/256}$. The original opposite-sign kernel satisfies $|D_{j,-n}|\le \exp[-(n+.9j)/64]$. With $\sum n^2e^{-n/32}<66100$, separation gives
$$
 \|P_{\ge N}D\|_{\dot H^{-1}\to0}<6500 e^{-.9 N/64}.
$$
At $N=L/2$ this is $<10^{-15}$. For $P_HQ_aT_iD$ split the $v$ multiplier at $L/2$ as in ASQ12, using $\|ID\|_{\dot H^{-1}\to0}<.08$ for the true low-to-high crossing. Its whole norm is $<10^{-11}$. The right $\dot H^{-1}$ factors are $<.64$ for $M$ and $<1.11(513)(1+1.43/388)<573$ for $H$.

For the remaining $H$ input and $M$ output, use the signed inverse-density identity [ASQ13.1–2](R149-supplement-opposite-density-inverse-on-original-high-frequency-inputs.md), retaining the middle $P_{97}$. Its bound is $12d_H+.00132(513)<.678$.
Indeed $d_H\le4(513)(\sum_{n>L} n^2 e^{-18n/640})^{1/2}<10^{-12}$. For example, $ne^{-9n/1280}<1$ there by monotonicity, so the last sum is at most $\sum_{n>L}e^{-9n/640}<10^{-40}$. This uses the actual inverse lift and its true contour, without a frequency width loss.

## Diagonal coordinate costs

The finite reference correction of ASQ10.6 vanishes on both $M$ and $H$ inputs. Write the remaining nonphysical multiplier terms exactly as in ASQ12, keeping $B-Id$, the sign commutator, $-M_v I\mathcal T_\alpha I\bar G$, $-\nu I\mathcal T_\alpha I\bar G$ and $-\nu\mathcal T_w I^2\bar G$. For input and output $M$ these five and the opposite-sign term sum to less than
$$
 {2.51\over388}+.00024(.573)
 +\left({1.08\over192}+{.008\over4}\right)1.43(.573)
 +{37\over388}1.43(.573)+37(2.51){.573\over388}+.32(.64)<.44.
$$
The reference range, original mean and physical phase are kept in their own rows. Within the two windows both signs in each real coordinate are already present.

For input and output $H$ the corresponding sum is bounded by
$$
 {2.51\over4L}+10^{-11}(513)
 +\left({1.08\over2L}+{10^{-11}\over4}\right)1.43(513)
 +{37\over4L}1.43(513)+37(2.51){513\over4L}+573\,10^{-11}<.02.
$$
The two-sign commutator requires coefficient separation $2(L+1)$; the displayed bound uses the larger $V_{L/2}$. The first $M_v$ term splits its intermediate primitive at $L/2$. These expressions do not rely on cancellation of unrelated upper bounds.

## Crossed coordinate costs

For input $M$, output $H$, split the input primitive in $B-Id$ at $L/2$. Its upper is $2.51/(2L)+.000012/388$. The sign commutator is $<10^{-11}(.573)$. The $M_v$ and $\nu I\mathcal T_\alpha$ terms have respective uppers
$$
 \left({1.08\over2L}+{10^{-11}\over4}\right)1.43(.573),\qquad
 {37\over4L}1.43(.573).
$$
For $\nu\mathcal T_w I^2\bar G$, split its original input at $L/2$. The part above has second-primitive norm at most $.573/(2L)$, while the lower part crosses with the true $w$ tail. Its upper is $37[2.51(.573)/(2L)+.000012(.573)/388]$. Adding the full opposite-sign upper $.64\,10^{-11}$ gives a sum $<.00004$. This direction costs substantially less than its reverse.

For input $H$, output $M$, $B-Id$ is bounded by $2.51/(4L)$ and the sign commutator by $10^{-11}(513)$. In $I\mathcal T_\alpha I\bar G$ first split the intermediate frequency at $L/2$. The high frequency costs $1.43/(2L)$, the low frequency uses an $\alpha$ coefficient beyond $L/2$. After multiplication by $v$, its low primitive costs at most $1/4$. In the $\nu$ term the ultimate output is still at least 97, and its low part costs instead $1/388$. The resulting two terms are bounded by
$$
 1.08(513)\left({1.43\over2L}+{.000012\over4}\right),\qquad
 37(513)\left({1.43\over2L}+{.000012\over388}\right).
$$
The last $w$ term is bounded by $37(2.51)513/(4L)$. With the $<.678$ opposite-sign estimate the whole reverse sum is $<.71$.

## Full complementary inverse and the remaining finite rows

Adding the physical costs (ASQ15.3–4) in their actual output windows proves (ASQ15.1). Set $(a,u;v,b)$ to its four ordered entries. Under either test (ASQ15.2), $a,b<1$ and $uv<(1-a)(1-b)$ by exact rational multiplication. Thus the nonnegative matrix $\mathcal B$ has spectral radius $<1$. The vector of component norms of any power of $P(\mathcal L-Id)P$ is dominated by the corresponding power of $\mathcal B$ on nonnegative columns. Its Neumann series converges on the full Hilbert direct sum. In particular the full complementary inverse $H_c=(P\mathcal L|_{PY})^{-1}$ satisfies the componentwise estimate
$$
 \binom{\|P_M H_c y\|}{\|P_H H_c y\|}
 \le{1\over(1-a)(1-b)-uv}
 \begin{pmatrix}1-b&u\\v&1-a\end{pmatrix}
 \binom{\|P_M y\|}{\|P_H y\|}.
$$

Now $Q=Id-P$ is precisely the original ordinary 96-dimensional reference head. With $q=Qw_0$, the exact recovered vector is
$$
 p=H_c P(Bf+Us-\mathcal L q-BXc_{\rm root}-Bg_{\rm met}k),
 \qquad w_0=q+p .
$$
The low waist row uses $Q\mathcal L(q+p)+QBXc_{\rm root}+QBg_{\rm met}k=Q(Bf+Us)$. The same recovered $w_0$ enters $\Theta w_0=s$, both true physical means, the signed raw phase and the complete same-world height rows. CFC's 96 independent physical root coordinates $c_{\rm root}$ are separate from the 96 ordinary coordinates $q$. All $M$ and $H$ tails of each CFC trial are charged by this two-window reconstruction. An estimate proved only beyond the trial support at 512 is insufficient for $P_M BX$. The actual low signed physical square and its full crossings are still required.
