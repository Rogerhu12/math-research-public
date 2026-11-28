# R149 ASQ4. The signed CFC matrix as an actual root-coordinate block

**Proved.** There is an invertible transformation of the true constrained
waist equations for which the 96-square physical diagonal block differs
from the complete CFC observation by only a *high-tail* correction.
The bound below retains the actual column error, full high inverse and
signed orientation. It identifies a concrete use of the CFC matrix
without identifying its rectangular observation table with an inverse.

Keep [ASQ2](R149-supplement-actualsquare-selected-far-graph-and-height-span.md)'s
selected exterior and all actual source responses. Begin in the **unextended
physical input** $x$ of WGB.24, with $w=\overline M x$ and
$\Theta w=0$. Write $X=H_{\rm phys}$ for the normalized physical
columns of [CFC.5–11](R149-supplement-complete-normalized-TC-columns-and-finite-physical-interface.md).
The complete constrained equations can be written
$$
 (I+K)w+Xc+gk=f,\qquad \Theta w=0 .             \tag{ASQ4.1}
$$
This follows directly from
[WGB.10–14 and WGB.24](R133-supplement-exact-graph-parameterization-and-physical-finite-border.md):
on the constraint the reference extension equals the physical row.
Here $c$ is the one independent set of prescribed root-even data.
In the coordinate $w$ it is *not* $\Theta w$. To recover WGB's other
implementation use $u=w+\overline M C_Q c$. Then
$\Theta u=c$ and $K\overline M C_Q=0$ since
$\widetilde P C_Q=0$. Thus in either implementation the same 96
physical data occur exactly once. The complete metric column $g$ and
forced row $f$ include effects of the original input chart, left
normalizer, positive solve, actual cap composition, and source signs.

For arbitrary row data the transformation $(y,s)\mapsto(y,\Theta y-s)$
is its own inverse. Apply it to ASQ4.1. Its second equation becomes
$$
 \Theta Kw+(\Theta X)c+(\Theta g)k=\Theta f .    \tag{ASQ4.2}
$$
For original constraint RHS $s$ use $\Theta f-s$ instead.
No angle multiplier has been commuted with a projection. In particular
the exact contribution of the signed physical matrix $\Theta X$ is
**positive** in this row. This equality is not obtained by observing
only the principal or homogeneous part of the waist equation.

Set $P=P_J$, $Q=I-P$, $q=Qw$, $p=Pw$, $H=I_P+PKP$ on the actual
reflected normalized waist target. With $\chi_J$ from WGB.16 and its
strict gate, the high reconstruction is
$$
 p=H^{-1}(Pf-PKq-PXc-Pgk).
$$
It is the complete WGB high action after an exact change of coordinates,
not an omission of the high reference subtraction in WGB.30.
For example starting there gives $PU=PX-P\overline M C_Q$ and
$u=w+\overline M C_Qc$; the equality follows using
$K\overline M C_Q=0$ **before** taking norms.
The effective second row after eliminating $p$ is
$$
\begin{split}
 [\Theta KQ-\Theta KP H^{-1}PKQ]q
 &+[\Theta X-\Theta KP H^{-1}PX]c\\
 &+[\Theta g-\Theta KP H^{-1}Pg]k
   =\Theta f-\Theta KP H^{-1}Pf-s .                \tag{ASQ4.3}
\end{split}
$$
The low waist row remains
$q+QK(q+p)+QXc+Qgk=Qf$. Both receive the *same* signed $p$. The raw phase
and absolute height rows evaluate their actual reconstructed physical
states on $(q+p,c,k)$ including the affine source particular, full direct
and world terms. Translation enters the absolute height with coefficient
one. On the exact conjugacy raw nonmean recovery then follows
[ASQ3](R149-supplement-actualsquare-raw-conjugacy-recovery-at-selected-base.md).
There is no added CFC stored-mean equation; physical mean forcing enters
these formulas via its true response.

Let $D$ be the signed whole CFC matrix center, $e_\Theta$ its joint
operator error for $\Theta X$, $\delta_X$ the whole CFC.10 column error
including any target storage conversion, and $B_\Theta$ the *global*
row bound. For $J>512$, CFC's reflected finite trial is supported below
$J$ (the target reflection acts within each paired frequency). Thus
$\|PX\|\le\delta_X$ even though the true columns have infinite tails.
Since $\|KP\|\le\chi_J$, the physical block in ASQ4.3 satisfies
$$
 \boxed{\quad\|S_{cc}-D\|
 \le e_\Theta + B_\Theta\frac{\chi_J}{1-\chi_J}\delta_X .\quad}       \tag{ASQ4.4}
$$
The same signed orientation gives all other corrections. For the low waist
$c$ block the additional high cost is at most
$\chi_J\delta_X/(1-\chi_J)$ before adding the finite approximation
error of $QX$. For a scalar endpoint functional $L$ on the $w$ variable,
the additional $c$-block cost is at most
$\|LP\|\delta_X/(1-\chi_J)$, but the original fixed-root response of
that scalar must still be included. In particular the physical
phase/height reads supplied by CFC are *direct* $c$ entries at
$w=0$. A common-ratio receiver bounds the corrected combination by
using its actual high dual $\|(L_P-\rho L_H)P\|$ or the sum of two
complete bounds with the same whole $\rho$.

For an explicitly verified left approximate inverse $D_L$ of the
96-square signed center, a sufficient physical pivot gate is
$$
 \|I-D_LD\|+\|D_L\|\bigl(e_\Theta+
 B_\Theta\chi_J\delta_X/(1-\chi_J)\bigr)<1 .
$$
This implies invertibility of precisely $S_{cc}$ by Neumann and
finite dimensionality. It leaves the true $q$ block of size $J-1$,
its signed crosses and its phase/metric rows. A failed sufficient
gate does not imply singularity. No result for a smaller window or
an unexecuted CFC target has been inserted as $D$ or $\delta_X$.

The [matrix-free action and radius](../scripts/fourfold_codazzi_actualsquare_physical_cross.py)
evaluate ASQ4.2 on the reconstructed $p$, with the complete external
source and scalar observables supplied in the original declared units.
The scalar error interface requires a directed positive high gap.
There is no default zero high source. An actual high inverse
implementation, physical $KQ$ action and all requisite bounds remain
necessary to certify the whole selected square; the block enclosure
does not give a bounded full inverse for other PDE or nonlinear rows.
