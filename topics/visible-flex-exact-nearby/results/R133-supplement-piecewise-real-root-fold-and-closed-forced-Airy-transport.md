# R133 supplement: piecewise real root folds and a closed forced Airy transport

2026-11-14, phase_inverse. **Proved quantitative construction from
explicit coefficient envelopes.** The radial coordinate in the larger
window is real and piecewise smooth; the old angle remains analytic.
No joint holomorphic continuation across the original cubic seams is
assumed.

This construction uses the same repaired family $Q^\delta=Q^0+\delta Z$,
all 193 direction components and its true mean. The root is the original
intrinsic root at $\eta_0$; the compact metric perturbation is identically
zero on the window considered. Its numerical domain is granted only
when the independent public coefficient consumer actually passes the
displayed inequalities.

## 1. Full coefficients on a real radial window

Write $\rho=r_*-r$, $q^2=-K$, $\eta=-\gamma\langle v\rangle$,
$e=-d$ and
$$
 k(\rho)=-K(r_*-\rho)/\rho,\qquad a(\rho)=\eta(\rho)\sqrt{k(\rho)} .
                                                               \tag{M.1}
$$
At zero $k=K_r(r_*)$. The original root germ fixes the branch.
The scalar $a$ is radial even when the family is nonradial.
For real parameters $a>0$; for a complex parameter disk use the
same analytic branch with a positive real-part gap.

On $|\rho|\le R$, at old angular width $\sigma_0$, suppose
$$
 \Re a\ge a_->0,\quad |a|\le a_+,\quad
 \|e\|\le D_0,\quad
 \|e_\phi\|\le D_1,\quad
 \|e_{\phi\phi}\|\le D_2 .                             \tag{M.2}
$$
Every coefficient bound includes the exact continuous repair and
the full parameter disk. The finite band belongs to the explicit
background, not to the unknown solution.

Let $O_\pm(R)$ be complete bounds for the two real radial integrals
of $|\eta|\sqrt{|K|}$ from the actual root to distance $R$ on either
side. They may be bounded by summing original closed-cell enclosures;
the uncertain root interval is covered completely. Define
$$
 M_R=D_0R+\max(O_-(R),O_+(R)),\qquad
 j=e^{D_1R}-1,\qquad E_1=e^{D_1R}.                    \tag{M.3}
$$
Using the integral is sharper than replacing it by
$(2/3)a_+R^{3/2}$. A larger certified upper bound in (M.3) is allowed,
including a fully covered root uncertainty margin.

Require $M_R<\sigma_0-\sigma_1$.
The true equations
$$
 (\partial_\rho-e\partial_\phi)S_\pm
       =\pm a\sqrt\rho\,\partial_\phi S_\pm,\qquad
 S_\pm(0,\phi)=\phi                                    \tag{M.4}
$$
then have actual characteristic solutions for every real radial
segment, analytic in $\phi$ on width $\sigma_1$.
On the positive side $\sqrt\rho=i\sqrt{|\rho|}$ is used consistently;
the two flows there are complex conjugate for real data.
This is an ODE with piecewise continuous radial derivatives and
continuous radial coefficients, not a radial Taylor extrapolation.

The flow displacement bound follows by integrating its entire
complex angular speed. Its first two angular variations give
$$
 |S_{\pm,\phi}-1|\le j,\qquad
 |S_{\pm,\phi\phi}|\le D_2|\rho|e^{3D_1R}.              \tag{M.5}
$$
All subpaths used below are ordered inside the same real root-to-point
path. A common drift subpath followed by a ray subpath has total
drift length at most $|\rho|$ and optical integral at most the
full $O_\pm(R)$. No extra traversal of the whole window is implicit.

## 2. Actual fold and its complete domain fees

Set, with the root extension supplied by the original analytic germ,
$$
 X=(S_++S_-)/2,\quad
 A=3(S_+-S_-)/(4\rho^{3/2}),\quad T=-\rho A^{2/3}.
                                                               \tag{M.6}
$$
On each open original piece, and by the matching traces,
$$
 DX=\tfrac23a\rho^2A_\phi,\quad
 2\rho DA+3A=3aX_\phi,\quad D=\partial_\rho-e\partial_\phi .
$$
The exact ordered integral is
$$
 A(\rho,\phi)=\frac32\int_0^1\sqrt{s}\,a(s\rho)
 X_\phi(s\rho,\chi_e(s\rho;\rho,\phi))\,ds .             \tag{M.7}
$$
It remains valid for negative real $\rho$ and through strict original
seams. Therefore put
$$
 A_-=a_--a_+j,\quad A_+=a_+E_1,\quad
 B_A=\tfrac35a_+D_2R e^{4D_1R},
$$
$$
 B_T=\tfrac25a_+D_2A_-^{-1/3}R^2e^{4D_1R},\quad
 T_+=RA_+^{2/3},\quad
 d_*=1-2j-j^2-T_+B_T^2 .                              \tag{M.8}
$$
Require $A_->0$ and $d_*>0$. The actual maps satisfy
$|A_\phi|\le B_A$, $|T_\phi|\le B_T$ and
$$
 |X_\phi^2+TT_\phi^2|\ge d_*,
$$
$$
 |\operatorname{Jac}(T,X)|\ge
       a_-A_+^{-1/3}d_*,
 \qquad |\mu|\ge a_-^2A_+^{-2/3}d_* .                  \tag{M.9}
$$
The exact principal identity is the same as the local fold theorem:
$$
 \operatorname{pr}_2(D^2-a^2\rho\partial_\phi^2)
       =\mu(\partial_T^2+T\partial_X^2).
$$
All lower operators and the independent mean/source equations remain.

A useful stronger displacement, obtained by integrating $DX$ along
the common drift, is
$$
 |X-\phi|\le D_0R+\tfrac1{10}a_+^2D_2R^4e^{4D_1R}.
                                                               \tag{M.10}
$$
The leading optical displacement cancels from the average $X$.
Using the larger ray displacement instead would be valid but
needlessly expensive in an old-mean contour argument.

For real parameters and real angles, $X,T,A$ are real, $A>0$ and
$X_\phi>0$ whenever $j<1$. Along a level of $X$, $T$ is strictly
monotone in $\rho$ by the Jacobian. The real image consequently
contains $|T|<RA_-^{2/3}$ at every real $X$.
This real conclusion does not grant a global analytic rectangle
in the canonical variables across curved images of radial seams.
Derivatives are always taken on the actual pieces and their
one-sided traces.

## 3. Complete inverse on the original circles

At any old radial circle use the full operator
$A_{\rm old}=\eta\partial_\phi+L$ and the old mean projection,
as in the complete moving scalarization.
For width $\sigma_J\le\sigma_1$ put
$$
 L_0^+=2|b|U_0V_0+\tfrac{|b|}{2}V_1U_0,\qquad
 c_J=\eta_{\rm inv}L_0^+/4 .
$$
If the complete interval bounds give $c_J<1$, then
$$
 \|J\|\le\frac{\eta_{\rm inv}}{4(1-c_J)},\qquad
 \|\partial_\phi J\|\le\frac{\eta_{\rm inv}}{1-c_J}.
                                                               \tag{M.11}
$$
This is a full inverse on the nonmean parity space; its primitive,
products, true mean row and all high outputs remain.
It is not an inverse on a fixed-$T$ circle.

Higher declared Sobolev windows can be paid by the same complete
angular commutator recursion as the original root budget. In
particular the actual derivatives of $L$, with every product and
projection retained, give positive integer one-gain bounds; applying
the same argument to the adjoint and interpolating gives the
negative windows. These fees have to be listed by the consumer
when they are used. A uniform $L^2$ bound alone does not imply them.

## 4. Leading amplitudes and actual forced transports

The complete leading amplitudes are the already proved
$$
 a_0=G(X_\phi^2-TT_\phi^2),\quad
 b_0=-2i\epsilon G X_\phi T_\phi,\quad
 G=(k_*/\eta_*)^{1/6}A^{1/6}k^{-1/4}
      \exp[-2\int_{r_*}^r b\langle u^2+Kv^2\rangle\,ds].
                                                               \tag{M.12}
$$
They are continuous with continuous first old radial derivatives
at strict original seams. The full $J$ reconstruction thus has
zero leading value jumps.

There is also a closed actual solution for every forced finite
transport equation, without moving the old primitive to new slices.
Write
$$
 \mathcal T_\epsilon(a,b)=(F_b,F_a)
$$
in precisely the convention (I.19) of
[the original primitive and Airy calculus](R133-supplement-original-primitive-on-actual-Airy-amplitudes-and-exact-mean.md).
Let $t=\sqrt{-T}$ and, for $\sigma=\pm1$, define
$$
 \mathscr D_\sigma=\partial_r-(d+\sigma\eta q)\partial_\phi,
 \qquad C_\sigma=aA^{-1/3}(X_\phi-\sigma tT_\phi),
$$
$$
 V_\sigma=a+\sigma i\epsilon t b,\qquad
 V_{\sigma,0}=G(X_\phi+\sigma tT_\phi)^2 .              \tag{M.13}
$$
Here the first $a$ in $C_\sigma$ is the radial coefficient (M.1);
the $a$ in $V_\sigma$ is the transport amplitude.
This naming distinction is essential.

The true branch label for $\mathscr D_\sigma$ is
$\Theta_\sigma=X-\sigma(2/3)(-T)^{3/2}$.
Directly from the fold,
$\mathscr D_\sigma T=C_\sigma$ and
$\mathscr D_\sigma X=-\sigma t C_\sigma$.
Equations (I.20)--(I.21) therefore give the exact identity
$$
 \boxed{\quad
 \mathscr D_\sigma(V_\sigma/V_{\sigma,0})
 =\frac{C_\sigma}{2V_{\sigma,0}}
            (F_a-\sigma i\epsilon F_b/t).
 \quad}                                                   \tag{M.14}
$$
Both signs and the factor $i\epsilon$ are retained.

Let $\chi_\sigma(s;r,\phi)$ be the true old-angle characteristic
of $\mathscr D_\sigma$ with terminal value $\phi$ at $r$.
For a prescribed common root trace $a_*(\phi)$, (M.14) yields
$$
 \frac{V_\sigma(r,\phi)}{V_{\sigma,0}(r,\phi)}
 =a_*(\Theta_\sigma(r,\phi))+
 \int_{r_*}^{r}
 \left[\frac{C_\sigma}{2V_{\sigma,0}}
       (F_a-\sigma i\epsilon F_b/t)\right]
                    (s,\chi_\sigma(s;r,\phi))\,ds .       \tag{M.15}
$$
The root singularity is integrable because $t\asymp\sqrt{|\rho|}$.
Inside the original root germ the existing analytic transport
proof fixes the branch and proves that
$a=(V_++V_-)/2$ and $b=(V_+-V_-)/(2i\epsilon t)$ extend through
the root, with $b(0)=F_b(0)$.
Beyond that germ the ordered integral is taken along real radial
pieces, with analytic old angular dependence. It never asks for
a holomorphic continuation of a cubic across a radial seam.

For the actual next amplitude use the complete forcing
$-(\mathcal L_0v_0)$ from the finite calculus in the
[actual parametrix construction](R133-supplement-actual-moving-root-parametrix-and-scalar-finite-part.md),
including the degree-zero contribution of $R_{-1}D_r$.
Later amplitudes use the full already specified ordered recursion.
Every old mean, finite inverse remainder and non-amplitude source
stays outside this displayed amplitude equation as an actual residual.
Equation (M.15) grants none of their norms automatically.

## 5. Exact nonzero seam source and the available propagation window

At a strict original seam, $t$, $C_\sigma$, $V_{\sigma,0}$ and
their first required traces are continuous. A piecewise bounded
forcing in (M.15) makes $a,b$ continuous, but their radial
derivatives may jump. With brackets meaning right minus left
in physical $r$, (M.14) gives exactly
$$
 [a_r]=\frac{aA^{-1/3}}2
                 \{X_\phi[F_a]+i\epsilon T_\phi[F_b]\},
$$
$$
 [b_r]=\frac{aA^{-1/3}}2
                 \{i\epsilon T_\phi[F_a]+(X_\phi/T)[F_b]\}.
                                                               \tag{M.16}
$$
The root lies strictly inside its original piece. Thus no seam
in (M.16) has $T=0$; its strict distance must be kept in a
quantitative use. If other inputs have prescribed jumps, the
full (M.15) transmission and their resulting terms are retained.

For the finite scalar trial
$F_N=U_n(\sum_{k=0}^N n^{-k}(a_k,b_k))$, with continuous
amplitudes as above, its exact projected two-row reconstruction is
$f_N=PF_N$, $h_1=J(D_r-B)f_N$, $h_2=f_N$.
The complete seam source is
$$
 j_2=0,\qquad
 j_1=JP\sum_{k=1}^N n^{-k}
     U_n([a_{k,r}],[b_{k,r}]).                           \tag{M.17}
$$
No hidden delta distribution is put into a volume $L^2$ norm.
Additional independent mean or second-row source ports give
their full extra reconstruction terms.

On the already paid short negative root interval, the
[negative-one Cauchy and seam theorem](R133-supplement-full-family-negative-one-root-Cauchy-and-seam-sources.md)
takes each actual $j$ in
$H^{-2/3}\times H^{-1}$, gives the complete $H^{-1}$ state and
then an ordinary $L^2$ old primitive. It is the correct way to
retain an angular gain after true propagation.
Its radial interval has not been enlarged by this reference.
Outside that interval the appropriate true strict or positive
propagator has to be paid separately.

The next task is numerical evaluation of the full forced amplitudes,
their ordered old-primitive residuals and (M.17), on a genuinely
certified larger window. Neither formal jump order nor the existence
of the characteristic integral is a numerical $C_E,C_s$ or a useful
strong-return cutoff. All finite head, mean and original exterior
columns remain independent.
