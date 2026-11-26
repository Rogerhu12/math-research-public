# R147 supplement: the complete high parameter forcing with its exact mean leakage

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**New proved reduction.** The strict true parameter particular from [NP](R147-supplement-independent-strict-nu-particular-and-signed-waist-column.md) has a full Fourier waist trace. Its high incoming and outgoing forcing can nevertheless be bounded from the complete saved NP output and the already completed W/JC bounds, without another PDE solve, Fourier carrier, pairing, or high row evaluation. The main improvement is an exact mean-preserving density identity: the nonconstant output of a constant input is controlled by the deviation of the true Jacobian from one. A second improvement subtracts a proved low-mode energy lower bound from a complete nonmean energy upper bound.

These are estimates of the actual right-hand side before the full high incoming inverse. They do not prove that inverse, perform target normalization, or establish the parameter Schur condition. No new numerical value is asserted before the complete new scalar output is saved by a public run.

## NH1. The same true density map, not a composition map

Keep the exact selected member, physical angle, period \(\ell=\pi/2\), normalized measure and true lift \(\mathcal H\) used in NP, [RW](R149-supplement-reflected-finite-waist-rows-from-complete-conjugacy.md), [JC](R149-supplement-joint-compound-waist-row-error.md) and [PN](R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md). Write

\[
 (\mathcal U f)(x)
   =\frac{f(\mathcal H^{-1}(x))}{\mathcal H'(\mathcal H^{-1}(x))},
 \qquad \mathcal U=U_{\mathcal H^{-1}}.
 \tag{NH.1}
\]

This is the original density pushforward: its adjoint is the pullback
\(g\mapsto g\circ\mathcal H\). Thus

\[
 \Pi\mathcal U f=\Pi f,\qquad
 \|\mathcal U f\|_2^2
   =\int_{\mathbb T}\frac{|f(\phi)|^2}{\mathcal H'(\phi)}\,
                         \frac{d\phi}{\ell}.
 \tag{NH.2}
\]

Let \(B_H\) be the original whole saved WX inverse-density upper and
\(K_W\) the original fixed \(J_s=268435456\) two-window inverse upper.
Set \(\Gamma=B_HK_W\). The paired PN.16 receiver has norm at most
\(\Gamma\), with no additional square root of two.

From the **complete original W native**, read
`selected.physical_true_conjugacy_derivative_Astrip_upper` as a whole
saved upper \(H_1\). This bounds the full Wiener sum
\(\|\mathcal H'\|_{\mathcal A_{1/128}}\), not only a real supremum.
The degree-one identity gives its exact zero Fourier coefficient one,
so

\[
 \|\mathcal H'-1\|_\infty
 \le\|\mathcal H'-1\|_{\mathcal A_{1/128}}
 =\|\mathcal H'\|_{\mathcal A_{1/128}}-1
 \le\eta:=H_1-1.
 \tag{NH.3}
\]

Let \(m>0\) be the lower endpoint of JC's whole
`complete_interpolation_derivative_lower`. JC.4--8 prove this lower
for **every** lift \((1-t)G_o+t\psi\), including
\(\psi=\mathcal H-\mathcal H(0)\) at \(t=1\). Therefore
\(\mathcal H'=\psi'\ge m\). This endpoint qualification is necessary;
a bound for the finite compound alone would not suffice.

## NH2. Exact constant-to-nonmean leakage

Put \(P=1-\Pi\). Since \(\Pi\mathcal U1=1\), (NH.2) gives

\[
 \begin{aligned}
 \|P\mathcal U1\|_2^2
 &=\int\frac{1}{\mathcal H'}-1\\
 &=\int\frac{(\mathcal H'-1)^2}{\mathcal H'}
 \le\frac{\eta^2}{m}.
 \end{aligned}
 \tag{NH.4}
\]

All integrals use the same normalized measure. The middle equality
follows from
\(1/t-(2-t)=(t-1)^2/t\) and \(\int\mathcal H'=1\).
It does not subtract unrelated operator upper bounds. Define

\[
 \kappa=\eta/\sqrt m.
 \tag{NH.5}
\]

For two ordinary scalar encodings
\(f_\pm=y_\pm+\mu_\pm\), \(\Pi y_\pm=0\), apply (NH.2) to the
nonmean part and (NH.4) to the same constants. The Euclidean pair norm
then satisfies

\[
 \bigl\|(P\mathcal U f_+,P\mathcal U f_-)\bigr\|_{2\oplus2}
 \le B_H\|(y_+,y_-)\|_{2\oplus2}
          +\kappa|(\mu_+,\mu_-)|.
 \tag{NH.6}
\]

The two physical means are retained. They contribute through their
joint Euclidean norm, and their two original matching observations
remain separate. Formula (NH.6) only estimates their nonconstant image.

## NH3. Recover the trial mean and primitive bounds from complete output

Use the same unknown exact selected particular density \(Y\), exact
finite NP trial density \(Y^a=(y_+^a,y_-^a;\mu_+^a,\mu_-^a)\), whole
saved error \(D\) and trial norm upper \(H\):

\[
 \|Y-Y^a\|_{\mathcal Y_0}\le D,\qquad
 \|Y^a\|_{\mathcal Y_0}\le H.
 \tag{NH.7}
\]

The two complete NP true mean balls contain the two coordinates of
\(\mu=(\mu_+,\mu_-)\). For a real interval \(I\), let
\(\operatorname{absmin}(I)=\inf_{x\in I}|x|\) and
\(\operatorname{absmax}(I)=\sup_{x\in I}|x|\). From both entire balls set

\[
 L_\mu^2=\sum_\pm\operatorname{absmin}(I_\pm)^2,
 \qquad U_\mu^2=\sum_\pm\operatorname{absmax}(I_\pm)^2.
 \tag{NH.8}
\]

Projection onto the complete two-mean block is a contraction. Hence

\[
 M_-=(L_\mu-D)_+\le|\mu^a|,
 \qquad
 |\mu^a|\le M_+:=\min\{H,U_\mu+D\}.
 \tag{NH.9}
\]

The trial mean and primitive coordinates are orthogonal in the
original \(\mathcal Y_0\). Thus

\[
 P_a:=\sqrt{H^2-M_-^2}\ge\|(y_+^a,y_-^a)\|,
 \qquad
 U_a:=B_HP_a+\kappa M_+
 \ge\bigl\|(P\mathcal U f_+^a,P\mathcal U f_-^a)\bigr\|.
 \tag{NH.10}
\]

Every subtraction in (NH.10) removes a **lower** for an actual
orthogonal energy from an **upper** for the whole energy. A negative
directed upper radicand is an admission failure, not a reason to
silently replace it by zero. No midpoint of an inflated true ball is
treated as an exact mean or exact trial value.

## NH4. Paired cosine observations from the same signed trial values

Let \(g_j(x)=\sqrt2\cos(4j(x-a/2))\), with the original
\(a=2\mathcal H(0)\), and let \(p_j\) be RW's full saved finite row.
The complete uninflated NP observations are

\[
 t_j^+=\langle p_j,y_+^a\rangle+(\Pi p_j)\mu_+^a,
 \qquad
 s_j=\tfrac12\langle p_j,y_+^a+y_-^a\rangle.
 \tag{NH.11}
\]

NP's exact trial uses an odd first raw component and an even second
component. Its physical characteristic means consequently obey the
specific exact identity
\(\mu_+^a+\mu_-^a=0\), because their sum is the same radial scalar
times the mean of the odd raw first component. This does not set either
mean to zero. Therefore the corresponding **unrotated** minus pairing
is exactly

\[
 t_j^-:=\langle p_j,y_-^a\rangle+(\Pi p_j)\mu_-^a
          =2s_j-t_j^+.
 \tag{NH.12}
\]

In particular its paired energy is

\[
 \sum_{j=1}^{96}\bigl((t_j^+)^2+(t_j^-)^2\bigr)
 =2\sum_{j=1}^{96}\bigl(s_j^2+(t_j^+-s_j)^2\bigr).
 \tag{NH.13}
\]

The new scalar consumer uses the entire192 raw signed balls from NP,
including their finite evaluation uncertainty, to obtain a lower
\(L_t\) for the square root of (NH.13). It does not use the194
already inflated true solution balls as trial centers.

The same complete JC scalar row-error operator acts on each component.
Its direct sum has the same norm \(E\), not \(\sqrt2E\). Since the
encodings \(y_\pm+\mu_\pm\) are jointly isometric and NP's entire
trial lies below \(J_s\), the paired96 error is at most \(EH\).
Consequently

\[
 L_a=(L_t-EH)_+
 \le\left(\sum_{j=1}^{96}\bigl|
       \langle g_j,\mathcal U f_+^a\rangle\bigr|^2
       +\bigl|\langle g_j,\mathcal U f_-^a\rangle\bigr|^2
                      \right)^{1/2}.
 \tag{NH.14}
\]

The \(g_j\) are orthonormal in the true target angle, even for an
input not in the reflection subspace. These observations are a subset
of the whole low96 Fourier space. The low sine observations are not
available here and are not subtracted.

## NH5. All high modes, followed by the full infinite-dimensional error

Let \(Q_{97}\) project onto every target Fourier mode \(|j|\ge97\),
in both components. Orthogonality, (NH.10) and (NH.14) imply

\[
 \left\|Q_{97}(\mathcal U f_+^a,\mathcal U f_-^a)\right\|
       \le\sqrt{U_a^2-L_a^2}=:H_a.
 \tag{NH.15}
\]

This removes only the paid cosine head. All unobserved low sines and
all high modes remain on the upper side, so it is valid without a
Fourier approximation of \(\mathcal U f_\pm^a\).

For the exact NP particular use the complete ordered PN receiver
\[
 \mathscr RY=
 \left(\mathcal U\mathscr J_+\widehat T_0^{-1}Y,
 U_{R_\Omega^{-1}}\mathcal U\mathscr J_-\widehat T_0^{-1}Y\right).
\]
On the finite trial, \(\widehat T_0^{-1}Y^a=Y^a\). On the full PDE
error it is retained. Rotation commutes with the complete Fourier
projection \(Q_{97}\) and is isometric; this permits a **norm**
estimate from the unrotated minus observations, without claiming any
actual rotated signed matrix entry. Thus

\[
 \boxed{\quad
 \|Q_{97}\mathscr RY\|_{L^2\oplus L^2}
 \le H_a+B_HK_WD.
 \quad}
 \tag{NH.16}
\]

For reference the whole paired bound is
\(\|\mathscr RY\|\le B_HK_W(H+D)\). A completed consumer may select
the smaller of these two **entire** valid high uppers. It may not mix
partial pieces of different estimates.

The same NP raw pairings also admit the joint96 errors
\[
 \Xi_{\rm in}=B_HK_WD+EH,\qquad
 \Xi_\partial=(B_HD+EH)/\sqrt2,
 \tag{NH.17}
\]
directly by JC/JF, with no row-count factor. These refer to the original
declared incoming and physical observations, before any new target
factor or high elimination.

## NH6. Actual entry and retained obligations

The pure module
[fourfold_codazzi_strict_nu_high_forcing_math.py](../scripts/fourfold_codazzi_strict_nu_high_forcing_math.py)
implements (NH.5), (NH.8)--(NH.17). It receives only whole admitted
NP/W/JC records. It saves each directed intermediate bound before
using its correct saved endpoint. It performs no IO, numerical import,
PDE trial, carrier restoration, DFT, old row error or old pairing.

The concrete public scalar owner must require NP's complete two-target
result, all194 true observations, all192 raw signed trial observations,
the original fixed normalizer and selected family, and the whole
completed JC/W objects. Before NP completes it has no admissible
numerical input and emits no actual conclusion. Failure or a wide
bound remains a failure or a wide bound.

The complete high incoming inverse, all transported-head and target
factors, the independent second function input, both mean matching
equations, physical height/phase data, and the final true parameter
Schur still require their original full obligations. In particular
this estimate is not an assertion that the actual high source is zero.
