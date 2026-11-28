# R763. Releasing the two material rims on the paired-track body

Throughout, the initial nine-chart material surface and fixed tensor are those of R757, and the central motion is the R759 true paired track, with $0\le\theta=\theta_{\max}\sin\phi,\ \theta_{\max}\le.81,\ 0\le\phi\le\pi/2$. R761 provides an independent all-phase thick body on the same initial metric. The [additional physical base](../scripts/resume_20261126/r763_translated_caps_and_shared_rim.py) uses two independently deformable terminal circles. We establish a quantitative defect of the prescribed uncorrected R759 terminal circles, exact compatibility of a different entire cap trace, and uniformly short center-to-corresponding-rim chords in that new base.

## A terminal condition which interior modes cannot change

Let $m_0(s)=1-d_b k_0(s)$. The old cap material rim has speed $m_0$ and its signed geodesic curvature is $k_0/m_0$, up to the consistent choice of boundary orientation. This follows from the planar normal collar and the fact that the R757 graph height has zero two-jet at the rim. These are intrinsic data of the material rim. The argument does not require the cap to be planar in its interior. In the uncorrected R759 parallel roll the new terminal spatial curve $q_\theta-d_b n_\theta$ has material speed $m_\theta=1-d_b k_\theta$. An independent rigid pose or a developable isometry of its *current* cap plane preserves that speed. So does retaining the old transverse height graph in that development, since its differential vanishes on the rim. Any additional field vanishing at the entire rim leaves the tangential derivative unchanged. The three paired starts in the corresponding run-43 basis thus have a true positive residual on that circle for every positive active phase. This is a constraint of those boundary variables.

There is a uniform quantitative witness for their last phase. On a rising cell choose $t=1/6$, where the exact density is one and $k_0<0$. Let $b=1.3/11,\ m=2(1/3-.025)$, and let $e=\sqrt{1+f'^2}<1.00021$. Then
$
 {g_{\theta,ss}\over g_{0,ss}}-1
 =\left[1+{d_b\,\theta\over jbm e(1-d_b k_0)}\right]^2-1 .
$
For all the indicated $\theta\ge .768,\ j\le3$ this is $>.72$, using $d_b\ge .108,\ d_b<.10930,\ |k_0|\le1.6$. Thus merely increasing the interior basis and phase count cannot give a convergent exact solution. If a free angular relabeling equalizes the terminal speed while the rim and its tangent plane remain planar, its planar curvature as a function of material arclength must also match $k_0/m_0$. By integration of the unit tangent direction, equality of both intrinsic data forces the resulting *plane curve* to be congruent to the initial rim. An unrestricted space rim has independent normal curvature and a moving normal frame; this last plane-curve consequence then need not apply.

## A positive full-circle starting trace

Use $D_\theta(x)=\int_0^x(R_\psi-I)(1,f')\,d\xi$ from R759. On each of the two original complete R757 caps make the planar translation $h=-D_\theta(U)/2$, $U=1.30$; on the positive/negative cap use an additional axial translation $\mp c\sin\phi$ with $c\ge.23$ in the stated examples and $c\le.42$. The entire tensor, signed rim geodesic curvature, ordered first and second material derivatives up to this common translation, and all cap pair distances are then exact. On each roll write $Q_0=q_0-dn_0,\ Q_\theta=q_\theta-dn_\theta$, $p=p(v)$, $L=.108\pi/2+.0005+.81$, and put
$
 ((1-S_7(v/L))Q_\theta+S_7(v/L)(Q_0+h),
       \quad \pm [Y+p-c\sin\phi\,S_7(v/L)]) .
$
At zero this is exactly the initial R757 physical embedding; at each central and terminal seam it shares both true material derivatives through order two with the prescribed center or rigid cap. At the terminal seam this uses $d'=1,p'=d''=p''=0$. At the central seam $d'=0,p'=1,d''=p''=0$; the central immersion itself is isometric. In particular *at both boundaries* all three induced tensor entries agree exactly with their initial values. Isometry through the interior of each roll is still required.

On a center/roll seam of either sign and any station $s$, the actual displacement of $q_\theta(s)$ from $q_0(s)+h$ has norm bounded by
$
 {1\over2}\int_0^U |R_\psi-I|\,\sqrt{1+f'^2}\,d\xi
 \le \tfrac12 U(1.00021)(.81)\sin\phi<.527\sin\phi .
$
For either rigid head this follows from $|D_\theta(U)|/2$. On either track subtract the full integral's half from the prefix integral, or reverse signs, and use the triangle inequality on the two complementary pieces. The lateral center-to-corresponding-terminal-rim distance is therefore at most $.10930+.527\sin\phi$ and the axial difference is $p_b-c\sin\phi$. The squared upper bound
$
 (.10930+.527x)^2+(.9185-.23x)^2,\quad x=\sin\phi\in[0,1]
$
is convex with endpoint values $<.95^2$. Here $p_b>.9179>c$. Thus every corresponding chord, on both ends at every phase, is $<.95<L$. This necessary strict margin concerns the actual original meridian length. It neither proves all intrinsic path inequalities nor implies existence of an embedded isometric roll.

One alternate cap start uses the exact unit-speed development of the cap plane along its $X$ coordinate. On $-.83<X<-.63$ set $\beta=\pm a\sin\phi\,\sin^4(\pi(X+.83)/.20)$, zero elsewhere, $0\le a\le.22$. For $T=(\cos\beta,\sin\beta,0),\ N=(-\sin\beta,\cos\beta,0)$ in $xyz$ order, replace the plane embedding by its unit-speed integral in $X$ and retain $Z e_z$; extend the original signed cap height $f$ in the *new unit normal* $N$. The resulting metric differs from the true R757 cap tensor by exactly
$
                     ((1-f\beta')^2-1)dX^2 .
$
The finite R757 cap bump lies outside the hinge support. There $|f|<4.7\,10^{-9}$, and $|\beta'|\le(4\pi/.20)(.22)<13.83$, giving a full relative spectral cap error $<1.31\,10^{-7}$; $|dX|_{g_0}\le1$. Its rim two-jet of $f$ vanishes and the planar development is intrinsically flat, so the material rim tangential length and signed geodesic curvature remain their initial ones. This finite small error alone does not meet the exact-limit refinement requirement. At both joins the source fades this physical displacement onto the rolls with the same endpoint-flat weight. The preceding numerical chord bound was proved for the rigid cap starts.

## Shared free boundary derivatives

Use outward collar variable $r=v-L$ on a roll and $r=w$ on its cap. For each sign independently add the three-vector material fields
$
 \begin{split}
 V_{\rm roll}&=S_7(v/L)\,(A(s)+r B(s)+r^2 C(s)/2),\\
 V_{\rm cap}&=[1-S_7(w/.65)]\,(A(s)+r B(s)+r^2 C(s)/2).
 \end{split}
$
The cap term vanishes in a full neighborhood of its polar center. On each rim these have exactly the same two-jet $A,A_s,B,A_{ss},B_s,C$, in the corresponding derivative order. They vanish to second order at the central seam, where the strong grip and the finite center held witness are untouched. Separate Cauchy data are available on the two different ends. Fourier and section-adapted coefficients can be increased independently of both interior vector fields. Giving these coefficients zero initial values keeps the same continuum tensor and material domain at phase zero. Their induced-metric, curvature, support or ordered-chord, and any folding costs are properties of the corrected entire field. They are charged directly; the R761 tube proof applies to its prescribed field and does not cover these general modifications.
