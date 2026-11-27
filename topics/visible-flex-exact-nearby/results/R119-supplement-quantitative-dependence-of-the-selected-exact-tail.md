# R119 SLIP: quantitative dependence of the actual selected exact tail

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved.** On the original S/T parameter domain, the same selected
nonmean tail is quantitatively Lipschitz from the displayed
$H^{1795}$ parameter distance into the common $E_{20}^+$ graph.
The same normalized B-height output has a correspondingly small
$H^{23}$ Lipschitz constant. A further finite output window is
proved with the actual loss1734 and its complete low-source term.

The comparison includes the changing seed-selected second parameter,
its radial first compensation, the full first-principal feedback,
the actual nonlinear far graph and all ordinary source units.
It uses no derivative of the selected solution, no arbitrary
rough-source inverse and no new seed or PDE computation.

## SL1. One physical coordinate for the two actual solutions

Keep exactly the domain, profiles, stop, exterior parameter, radial
bumps and deterministic selection of
[T](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md),
[SREG](R119-supplement-higher-regularity-of-selected-tail-and-local-uniqueness.md)
and
[GF](R144-supplement-complete-parameter-forcing-for-the-selected-exact-tail-family.md).
In particular
$$
 \|\gamma/r_\gamma\|_{A^0}\le1/128,\qquad
 \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576},\qquad
 r_\gamma=10^{-9}.                                      \tag{SL.1}
$$
The same holds for $\widetilde\gamma$.
For the parameter distance write
$$
 d_j=r_\gamma^{-1}
       \|\widetilde\gamma-\gamma\|_{H^j}.                 \tag{SL.2}
$$
The lower norm in an estimate does not enlarge the value domain
(SL.1) to an open $H^j$ ball.

Let
$$
 w=w_\infty(\gamma),\qquad
 \widetilde w=w_\infty(\widetilde\gamma),\qquad
 h=\widetilde w-w.
$$
These are the same physical nonmean coordinates in T.C14's common
reference $\mathfrak q=0$. Their fixed linear condition is the same
$B_0w=B_0\widetilde w=0$: the compact metric bumps change neither
the B section, $s_B$, nor that boundary condition.

Write $\|\cdot\|_s$ for the actual graph norm at gamma and
$\|\cdot\|_{s,c}$ for the declared common norm. The equivalence
constant between an actual seed reference and the common reference
is below2. SREG's actual and common bounds give, simultaneously
through order2960,
$$
 \|w\|_s<r,\qquad \|\widetilde w\|_s<r,\qquad
 \|h\|_s<2r,\qquad r=2^{-49000000}.                       \tag{SL.3}
$$
Indeed the other selected solution has common norm
$<2^{-49999998}$; converting it to the gamma reference costs
less than2, and $2^{-49999997}<r$.
Thus the entire straight segment in $w$ stays in the original
low domain. Both heights belong to $E_{2960,0}^+$.

Define the complete actual mismatch
$$
 \Delta=\mathcal F_\gamma(\widetilde w)
                   -\mathcal F_{\widetilde\gamma}(\widetilde w)
         =\mathcal F_\gamma(\widetilde w),\qquad
 D_j=\|\Delta\|_{Z_j^{[3]}}.                              \tag{SL.4}
$$
Only the second equality uses the already proved exact selected
equation. The first residual uses the actual seed
$\mathfrak q(\gamma)$ and actual $\mathcal U_\gamma$ even though
its height is $\widetilde w$.

The source norms in (SL.4) are GF's original ordinary source
units, with all three broken radial derivatives. T.C11 is retained
when forming this source; it is not a rescaling of a false
fixed-reference PDE. Ordinary Fourier mean, holonomy mean,
independent charges and the one rigid height constant keep their
original meanings.

## SL2. Quantitative comparison with the complete mismatch

Put
$$
 A=2^{16777216},\qquad B=2^{71303172},\qquad
 K=2^{25165824},\qquad \rho=5Kr.                          \tag{SL.5}
$$
SREG.10 at the actual exact solution $w$ gives
$$
 \|h\|_{20}\le A\|D\mathcal F_\gamma(w)h\|_{Z_{1794}^{[3]}}.
                                                               \tag{SL.6}
$$
This estimate is applied to the actual $E_{2960}^+$ difference.
It does not assert an inverse on every source.

Taylor's exact identity at fixed gamma is
$$
 D\mathcal F_\gamma(w)h=\Delta-\mathcal R(h).              \tag{SL.7}
$$
For every $20\le j\le2898$, the complete S.27 remainder and
(SL.3) give
$$
 \begin{split}
 |\mathcal R(h)|_j
 &\le K\{\|h\|_{20}\|h\|_j
                   +(1+\|w\|_j)\|h\|_{20}^2\}\\
 &<5Kr\|h\|_{20}=\rho\|h\|_{20}.                         \tag{SL.8}
 \end{split}
$$
The affine and nonradial linear terms cancel in this remainder
at one fixed gamma, exactly as in S.25--S.27.
They are still present in the parameter mismatch (SL.4).

The finite-high remainder passes to these inputs by the same
strong lower-order cutoff argument as SREG.6. In particular
$j\le2898<2960$ leaves a strict margin; no Fourier density in
a highest uniform radial norm is being assumed.

The complete low absorption factor satisfies
$$
 A\rho=5\,2^{16777216+25165824-49000000}
                         <2^{-7056957}<1/2.
$$
Consequently
$$
                  \boxed{\ \|h\|_{20}\le2A D_{1794}.\ }  \tag{SL.9}
$$

For every integer $64\le s\le1164$, SREG.13 applied to
(SL.7) gives
$$
 \|h\|_s
 \le A D_{s+1734}+B D_{1794}+(A+B)\rho\|h\|_{20}.
$$
Here $s+1734\le2898$, so (SL.8) applies to both remainder
terms. Use (SL.9), $A<B$ and $4A\rho<1$:
$$
 (A+B)\rho\|h\|_{20}
 \le2A(A+B)\rho D_{1794}
 <4AB\rho D_{1794}<B D_{1794}.
$$
This proves the full finite-window comparison
$$
 \boxed{\ 
 \|h\|_s\le A D_{s+1734}+2B D_{1794},
                  \qquad64\le s\le1164 .
 \ }                                                     \tag{SL.10}
$$
In particular the large low-source coefficient has not been
discarded just because the high source has a higher index.

## SL3. Insert the actual gamma forcing

GF.31--GF.32 hold along the complete parameter segment at the
fixed physical height $\widetilde w$. Its common $E_{2960}^+$
norm is below1, so the same bound applies at every source order
needed here:
$$
        D_j<2^{-44000000}d_{j+1},\qquad20\le j\le2898.
                                                               \tag{SL.11}
$$
This is the already proved derivative of the true endpoint graph
and the true seed/metric maps integrated along the segment.
It is not a fixed-metric Poisson column.

Combining (SL.9) with (SL.11), and then paying the single factor2
from the actual to the common output norm, gives
$$
 \boxed{\ 
 \|w_\infty(\widetilde\gamma)-w_\infty(\gamma)\|_{E_{20,c}^+}
                  <2^{-27222782}d_{1795}.
 \ }                                                     \tag{SL.12}
$$
Thus the original selected map has a genuine quantitative
lower-order Lipschitz estimate on its entire original value domain.

Likewise (SL.10) gives
$$
 \boxed{\begin{split}
 \|w_\infty(\widetilde\gamma)-w_\infty(\gamma)\|_{E_{s,c}^+}
 <{}&2^{-27222783}d_{s+1735}\\
    &+2^{27303174}d_{1795},
                    \qquad64\le s\le1164 .
 \end{split}}                                             \tag{SL.13}
$$
The largest parameter order here is2899, below the actual8193
value-domain order. Both terms are essential to the stated bound.
The high output coefficient is not claimed to be a contraction.

The source and graph units do not change with the intrinsic
metric comparison. In particular no power of the radial
normalizer or a mean-height integration is inserted for free.

## SL4. Actual nonmean height and the normalized B-height output

The physical nonmean height is
$$
 u_\infty(\gamma)=\mathcal U_\gamma w_\infty(\gamma).
$$
Its difference is decomposed exactly as
$$
 \begin{split}
 u_\infty(\widetilde\gamma)-u_\infty(\gamma)
 ={}&\mathcal U_\gamma(\widetilde w)-\mathcal U_\gamma(w)\\
    &+\mathcal U_{\widetilde\gamma}(\widetilde w)
                         -\mathcal U_\gamma(\widetilde w).
 \end{split}                                              \tag{SL.14}
$$
S.16's actual first-difference bound is below2 on the
small order20 segment (SL.3). Converting its input and output
through the common reference gives the safe bound
$8\|h\|_{20,c}$ for the first line.
For the second line, integrate the actual GF.9--GF.10 at
fixed $\widetilde w$. With
$K_\partial=2^{6291456}$ and
$\epsilon_L<2^{-57000000}$ it is bounded by
$3K_\partial\epsilon_L d_{21}$ in the common graph.
All boundary mean and source terms in that lift have already
been paid in GF; $F_B\mathcal L_\partial=0$ is an exact identity.

The second term is much smaller than the first low budget.
Since $d_{21}\le d_{1795}$,
$$
 \boxed{\ 
 \|u_\infty(\widetilde\gamma)-u_\infty(\gamma)\|_{E_{20,c}^+}
                   <2^{-27222778}d_{1795}.
 \ }                                                     \tag{SL.15}
$$
This is a bound for the physical nonmean height. Its ordinary
nonmean coordinate is not confused with the separately reconstructed
holonomy mean or the global rigid height constant.

The actual normalized B-height output is the same linear readout
$$
       f_B(\gamma)=F_Bw_\infty(\gamma)
                  =F_Bu_\infty(\gamma).
$$
The graph explicitly includes
$2^{440}\|F_Bh\|_{H^{23}}$, and its physical scale $s_B$
is common to these references. Directly from (SL.12),
$$
 \boxed{\ 
 \|f_B(\widetilde\gamma)-f_B(\gamma)\|_{H^{23}}
                   <2^{-27223222}d_{1795}.
 \ }                                                     \tag{SL.16}
$$
This pays the trace with its actual graph term rather than
using a radial $L^2$ trace theorem. It is the output used by
the original cap/long interface, with its existing normalization.

## SL5. What has been completed

The estimates compare the two actual deterministic selected
solutions, with their possibly different seed-selected second
parameters. Full first-principal feedback, radial first compensation,
reference source, actual far graph and holonomy reconstruction
were retained before taking the norms.

The lower input norms in (SL.12)--(SL.16) are operator costs
on the original domain. No selection on an arbitrary open
$H^{1795}$ or $A^0$ ball has been constructed here.
No selected parameter derivative is asserted by this paper:
its construction requires an additional genuine difference-quotient
argument and joint continuity of the complete parameter forcing.

The whole core inverse, two physical means, true nu/phase Schur,
all B/C/Cmean matching, one world frame and the final fixed-metric
closed embedded family remain separate obligations.
A parameter which changes the selected intrinsic metric is not
renamed as the final isometric-flex parameter.

The companion reader only evaluates the new exponent arithmetic
in (SL.3),(SL.9)--(SL.16). It executes no old scientific target
and restores no carrier, seed or network inverse.
