# R149 ASQ10. All coordinate errors at ordinary cutoff 65536

**Proved for the original selected graph.** At $J=65536$, the
complete high compression after an invertible row operation has norm
distance from identity less than
$$
                 1/8+23\,C_{\rm phys}(J),\qquad
 C_{\rm phys}(J)=
 \|P_J(E_\partial^{\rm fr}+\Delta_\partial):
                 X_{\rm fr}^{-4/3}\longrightarrow Y_a^0\|.
 \tag{ASQ10.1}
$$
In particular all nonphysical coordinate terms together cost less than
$1/8$. The same statement omits $\Delta_\partial$ for the WDH
homogeneous row. The physical quantity in (ASQ10.1) still needs its
own signed estimate; it is the **high output** of the actual complete
WPL error, including the positive feedback in the coupled case.
If it is at most $1/32$ the high block is invertible, and if it is at
most $1/64$ its distance from identity is less than $1/2$.
This gives an explicit practical-cut target for the actual Airy, strict,
positive, jump, mean and endpoint suppliers. No smallness of the
ordinary finite block or this physical error is assumed as a conclusion.

## The actual scalar and lift bounds

Write $v=v_i$, $\nu=\nu_i$, $c_i=\nu+v$, $\alpha=v-w$, and
$A=I_d-\mathcal T_\alpha I$, $B=I_d+\mathcal T_wI$, with
$I=\partial^{-1}P_{\ne0}$. Here $I_d$ denotes identity, $\nu_i$
is the symbol mean, and $\mathcal T$ is the original same-sign
Toeplitz multiplier. Both real Fourier signs are present.
[NWA2](R133-supplement-actual-cohomological-normalizer-windows-and-global-sign-correction.md)
and its defining NW.5 give
$$
 |\nu|<37,\quad \|v'\|_2<2.374,\quad \|v'''\|_2<12044,\qquad
 \|v\|_{A^0}\le (\pi/\sqrt{48})\,2.374<1.08 .
 \tag{ASQ10.2}
$$
This uses the two-sign Cauchy--Schwarz sum and the true zero mean of
$v$. NWA's incoming order-zero number is an $L^2$ bound.

We also need a genuine small estimate for $\alpha$ on the full circle.
The complete
[UACT actual](../notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/actual-unit-disk-operator-Theta-low-square.json)
contains the copied whole trial Wiener upper $<.491$.
UACT3 record 4 is
$<.930$. Its precise nonnegative construction matters:
the [owner](../scripts/fourfold_codazzi_unit_disk_operator_Theta_low_square_owner.py)
takes $J_G$ from its saved Schur budget $>2$ (the alternative saved
HS budget is $>9$), weights every complete coefficient error by
$2J_G$, and in its first candidate adds $J_GT_\infty$ after all
2048 modes. This is [UDR.9,14](R149-supplement-unit-disk-phase-errors-in-original-Theta-rows.md)
on the fixed original trial. AS.13–14's bound $T_\infty$ is proved by
summing absolute analytic coefficients and Cauchy--Schwarz on the
remaining **two-sign coefficient sum**. Thus it controls the Wiener
tail itself. Every weight for this full positive sum dominates the
same term with algorithm weight one. Applying that pointwise
domination, with the saved trial, gives
$$
 \|\alpha\|_{A^0}<1.421<1.43,\qquad
 \|w\|_\infty<2.51 .
 \tag{ASQ10.3}
$$
No lower bound for the *operator* $GY$ is used. An arbitrary upper
for $\|\mathcal T_{\alpha-\widehat\alpha}GY\|$ would not imply
(ASQ10.3). The [whole WMA record 10](R149-supplement-actual-complete-weighted-model-Theta-receiver.md)
and its WMT.13 give
$\|P_{>2048}\alpha'\|_2<.023$. On $|j|\le2048$ the derivative has
Wiener norm $<8192(1.43)<12288$, by the true coefficient sum.

Write $L=J/2$. Cauchy--Schwarz on the original two Fourier signs yields
$$
 \|P_{\ge L}v\|_{A^0}
 \le12044\sqrt{\frac{2}{5\cdot4^6(L-1)^5}}<2^{-30}.
 \tag{ASQ10.4}
$$
For the last comparison $L-1>(15/16)2^{15}$ and
$(16/15)^{5/2}<5/4$. Similarly
$\|P_{\ge L}\alpha\|_{A^0}\le .023/\sqrt{8(L-1)}$.

Prior [SDI.1,4](R149-supplement-actual-small-density-inverse-constants-and-Theta-errors.md)
gives $\|C^{-1}\|_{-4/3}<5/2$, and for the true inverse lift
$p=\psi^{-1}$, $p'>.9749$, $|p'|<1.0251$, $|p''|<1/6$.
For $S=U_\psi$ its $L^2$ adjoint on the full circle is ordinary
composition by $p$. On $H^1$ this composition costs
$m^{-1/2}\max(1,\|p'\|_\infty)<21/20$, with $m=.9749$.
On $H^2$ use the binomial derivative norm, the diagonal change of
variables and the additional $f'\circ p\,p''$ term:
the cost is at most
$m^{-1/2}(1.0251^2+1/(6\sqrt2))<6/5$.
Interpolating these Fourier Hilbert spaces and dualizing gives
$$
                 \|S\|_{-4/3}
 <[(21/20)^2(6/5)]^{1/3}<11/10 .                         \tag{ASQ10.5}
$$
Projection of a test onto its nonmean part is contractive. No
positive-order smoothness of an unknown rough input is used.

## A row operation preserving the constrained physical equations

Use $w_0$ for the waist unknown to distinguish it from the target
coefficient $w$. On the actual input chart
$\Theta w_0=s$, $\Theta=V_Q\bar G$ and
$\widetilde P\bar G w_0=\bar G w_0-C_Qs$ by WGB.4–5.
Keep $C=WS$, $D=S-C$, and $P_{97}$ from
[DG.8–10](R149-supplement-complete-graph-remainder-through-same-sign-density-compression.md).
Multiply the entire normalized waist row of ASQ4 by $B$ and add
$U(\Theta w_0-s)$ to that row, where
$$
          U=[B(M_\nu-\bar M)+Q_a R_{\rm ss}]C_Q.
$$
This change together with the constraint is bounded and invertible
on the stated windows: the added map has finite-dimensional input,
the $C_Q$ columns are genuine graph vectors and $B$ has WBP's
proved inverse. The transformed RHS is $Bf+Us$ after moving $s$
to the right. The waist operator on $w_0$ is exactly
$$
 \begin{aligned}
 B+B(M_\nu-\bar M)\bar G+Q_aR_{\rm ss}\bar G
 &+Q_a T_i D P_{97} C^{-1}A\bar G\\
 &+(E_\partial^{\rm fr}+\Delta_\partial)S P_{97} C^{-1}A\bar G.
 \end{aligned}                                            \tag{ASQ10.6}
$$
The physical columns are $BX$ and $Bg_{\rm met}$. The true projection
$P_{97}$ before $S$ still produces the qualified physical domain.
The finite reference term in (ASQ10.6) has zero **high input** because
$(M_\nu-\bar M)\bar G P_J=0$ by ordinary reference support. Its
low inputs and its output after $B$ remain.

The $\Theta$ constraint can either be kept literally or transformed to
ASQ4.2 using the *original* waist row. These are invertible row
operations; the $\Theta X$ sign, both physical means and the
nonlinear normalizer derivatives retain their original meanings.

## The true same-sign coefficient error on the high block

Below every high input is $P_J$, every high output $P_J$, in the
ordinary model basis. $Q_a$ commutes with these cutoffs. WCS.13
gives
$$
 \|I\bar G P_J\|_{2\to2}<513,\qquad
 \|I^2\bar G P_J\|_{2\to2}<513/(4J).
 \tag{ASQ10.7}
$$
Indeed $\Lambda_n/(4n)<513/512$ for $n\ge J$. The same input feeding
$I^2\bar G$ has $L^\infty$ output $<1$:
Cauchy--Schwarz on $I(I\bar G P_J)$ costs at most
$513/\sqrt{8(J-1)}<1$. This holds for either Fourier sign using
the corresponding input-sign norm, so same-sign products below incur
no extra count.

The complete WDH.15 commutator term
$\frac12 Z[M_v I,Z_{\rm full}]$ costs $<513\,2^{-30}$ on this
high block: only opposite signs survive, requiring a coefficient
separation at least $2J$. The input is nonmean and the auxiliary
constant output vanishes under the left high projection.
Before estimating the other two terms, collect them exactly:
$$
 -M_{c_i}I\mathcal T_\alpha I-\nu\mathcal T_w I^2
 =-M_v I\mathcal T_\alpha I-\nu\mathcal T_v I^2
       +\nu I\mathcal T_{\alpha'} I^2 .                  \tag{ASQ10.8}
$$
On each nonzero sign $[I,\mathcal T_\alpha]=-I\mathcal T_{\alpha'}I$
by the Fourier entries, and $\alpha+w=v$. This cancellation uses the
same selected real coefficient in both parts.
The three costs in (ASQ10.8), from left to right, are less than
$$
 \begin{aligned}
 &[1.08/(4L)+2^{-30}/4](1.43)(513)<.007,\\
 &37(1.08)513/(4J)<.079,\\
 &\frac{37}{4J}[12288\cdot513/(4J)+.023]<.004 .
 \end{aligned}                                            \tag{ASQ10.9}
$$
The first bound splits $I$ at $L$ immediately before multiplication
by $v$, using (ASQ10.4) for a low-to-high crossing. The last splits
$\alpha'$ at 2048 and uses (ASQ10.7)'s $L^\infty$ control for its
$L^2$ tail. All inequalities extend from finite sums by density.
Also $\|P_J(B-I_d)P_J\|<2.51/(4J)<.00001$.

## Opposite signs and the original right factors

For any $j,n\ge1$, the opposite-sign matrix entry of $D=S-C$ equals
that of $S$. Changing variables by its actual inverse lift gives
$$
                 D_{j,-n}=\int e^{-4i(ny+jp(y))}\,dy/(\pi/2).
$$
The integral is over one period. [DG.4](R149-supplement-complete-graph-remainder-through-same-sign-density-compression.md)
gives $|p'|<11/10$ on $S_{1/256}$. On $|\operatorname{Im}y|\le
u=1/1024$, Cauchy's bound for $p''$ and the real lower in SDI give
$\operatorname{Re}p'>.9749-(11/10)/3>3/5$.
Shift the contour down by $u$ to get
$|D_{j,-n}|\le e^{-4u(n+3j/5)}$; the other sign is its conjugate.
The density Jacobian has been exactly absorbed by the change of
variable. Consequently
$$
 \|P_L D\|_{H^{-4/3}\to L^2}<2^{-70},\qquad
 \|I D\|_{H^{-4/3}\to L^2}<2^{20}.                     \tag{ASQ10.10}
$$
For details, $\Lambda_n^{4/3}\le16 n^{4/3}$ and
$n^{4/3}e^{-2un}\le u^{-4/3}$. Thus the weighted input $\ell^2$
sum in the separated kernel, after square root, is at most
$8u^{-11/6}$. On high output the other factor is
$e^{-12uL/5}(1-e^{-24u/5})^{-1/2}<16 e^{-76.8}$, by
$1-e^{-x}\ge x/(1+x)$. On output after $I$ its factor is at most
$\pi/\sqrt{96}<1/3$. Since $8u^{-11/6}/3<2^{20}$ and
$e^{76.8}>2^{100}$, these are (ASQ10.10). The two conjugate
off-diagonal blocks form an orthogonal direct sum.
Here $D$ is the off-sign density operator, distinct from the CFC
signed finite matrix.

Splitting the output of $D$ at $L$ and retaining all low-output
crossings by $v$ now gives
$$
 \|P_J Q_a T_iD\|_{H^{-4/3}\to L^2}
 \le [1+37/(4J)+1.08/(4L)]2^{-70}+2^{-30}2^{20}<1/1000 .
 \tag{ASQ10.11}
$$

For the original $A$ before $C^{-1}$, no unrestricted high gain
is taken after $C^{-1}$. On a single sign its primitive part,
conjugated into $H^{-4/3}$ Fourier units, has absolute entries
$\Lambda_j^{-4/3}|\alpha_{j-n}|\Lambda_n^{4/3}/(4n)$ for
$n\ge J$. For $j\ge n/2$ their norm is bounded by Young by
$2^{4/3}(1.43)/(4J)$. For $j<n/2$, $h=n-j>n/2$, and
$\Lambda_n^{4/3}/(4n)\le2(4h)^{1/3}
\le2(4h)(2J)^{-2/3}$. Its Hilbert--Schmidt norm is thus at most
$2(2J)^{-2/3}.023(\sum_{j\ge1}\Lambda_j^{-8/3})^{1/2}$
by summing $|4h\alpha_h|^2$ in each row. The last series is less
than one by integral comparison. The two bounds sum to less than
$1/1000$. Since $\bar G P_J$ preserves its input frequencies, WCS
and SDI give
$$
 \|P_{97} C^{-1}A\bar G P_J\|_{2\to H^{-4/3}}
 <(5/2)(1.001)512(4J)^{-1/3}<20.1 .                     \tag{ASQ10.12}
$$
Thus the $T_iD$ term costs $<.0201$. By (ASQ10.5) the remaining
physical term costs at most $23C_{\rm phys}(J)$. The entire
coordinate sum in (ASQ10.6–12) is $<1/8$, proving (ASQ10.1).
In particular only a single material receiver before the known
ordered source factors remains in that high estimate.

## Finite and physical recovery in the new rows

The intact low waist row uses the full transformed operator in
(ASQ10.6), including $B(M_\nu-\bar M)\bar GQ_J$. The high sources
are $P_J(Bf+Us)$, $P_JBXc$, $P_JBg_{\rm met}k$ and the negative
of the whole high-on-low block applied to $q$. The same reconstructed
$p$ enters $\Theta$, the weighted raw phase, world placement and the
actual physical mean rows, with the same affine exterior data.
Even a finite trial for $X$ acquires a tail after $B$. If the CFC
trial $X_0$ has support at most 512 and $\|X-X_0\|\le\delta_X$,
then
$$
 \|P_JBX\|\le1.63\delta_X+\|X_0\|/80000 .
$$
Indeed $\|B\|\le1+2.51/4<1.63$, and the separated multiplication
uses $\|P_{\ge L}w\|_{A^0}\le2^{-30}+.023/\sqrt{8(L-1)}<1/20000$
and $\|I\|_{2\to2}=1/4$. The corresponding signed row should use
the true $BX_0$, with the complete tail fee if it is approximated.

The physical quantity in (ASQ10.1) is the whole high output of the
correct WPL interface. For a new strict forcing supplier the $8.22$
bound of NRO.1 applies to ordinary $L^2$ input on its exact strict
body with the original radial measure. It gives no estimate for
previously projected-out mean sources, the root Cauchy trace, or a
fourth endpoint by itself. Nonstationary oscillatory bands must keep
their actual phases and all jumps before any WPL recombination.
Neither NRO's known metric-source particular nor a bound on label
$H^1$ alone establishes the required physical operator norm.
The 65535 ordinary retained modes and their physical border still
require certification once this high gate is actually met.
