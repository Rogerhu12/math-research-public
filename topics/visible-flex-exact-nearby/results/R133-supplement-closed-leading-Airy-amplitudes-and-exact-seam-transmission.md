# R133 supplement: closed leading Airy amplitudes and exact transmission at original seams

2026-11-14, phase_inverse. **Proved analytic identities.** The complete
leading two-amplitude solution of the actual moving operator is an
explicit function of the paid fold and one radial scalar integral.
It does not require another two-variable leading transport solve.

The formulas hold on the paid complex direction disk $|\delta|\le10^{-8}$
in the current joint root domain. A separate public consumer evaluates
their bounds from completed process records. Its proposed numerical
gates below are not called executed before an actual successful run.

The final section states the true transmission rules for extending to
the original candidate pieces. It grants neither a milliscale joint
holomorphic domain nor removal of any residual jump.

## 1. Both original curvature rows fix the amplitude

Use the definitions of
[the actual principal fold](R133-supplement-actual-moving-analytic-principal-fold.md).
Write
$$
 D_r=\partial_r-d\partial_\phi,\quad q^2=-K,\quad
 \eta=-\gamma m,\quad \mathcal S=u^2+Kv^2,\quad
 d_\phi=-b(\mathcal S-\langle\mathcal S\rangle).        \tag{L.1}
$$
The mean is the normalized old-angle mean at fixed physical $r$.
Here $b$ is the metric coefficient, not an Airy amplitude.

The order-one and local order-zero parts of the complete equation are
$$
 D_rh=\eta\begin{pmatrix}0&q^2\\1&0\end{pmatrix}
                     \partial_\phi h+
 \begin{pmatrix}L_{11}&-q^2\ell\\\ell&L_{22}\end{pmatrix}h
              +\mathcal Nh+\text{mean and source rows},
                                                               \tag{L.2}
$$
$$
 L_{11}=-b(1+3u^2-q^2v^2),\quad
 L_{22}=b(1-u^2+3q^2v^2),\qquad \ell=-2buv .
$$
The entire old primitive in $\mathcal N$ remains of angular order
minus one on the stated nonmean window, with its mean terms separate.
The centre is not asserted to solve the nonlinear PDE.

Put
$$
 \psi_\pm=\tfrac12(h_2\pm h_1/q),\qquad
 h=\begin{pmatrix}q&-q\\1&1\end{pmatrix}
                           \begin{pmatrix}\psi_+\\\psi_-\end{pmatrix}.
$$
Matrix multiplication, including this matrix's radial derivative,
gives the principal speeds $c_\sigma=d+\sigma\eta q$ and the
same diagonal order-zero coefficient:
$$
 \frac{L_{11}+L_{22}}2-\frac{q_r}{2q}
 =2d_\phi-2b\langle\mathcal S\rangle-\frac{q_r}{2q}.
                                                               \tag{L.3}
$$
The other-row terms remain in the first correction and strict
normalizer; they do not alter the leading own-ray amplitude.
There is no $\eta_r/\eta$ contribution in (L.3).

Let $\Theta_\sigma$ be the true root-based characteristic label,
$$
 (\Theta_\sigma)_r=c_\sigma(\Theta_\sigma)_\phi,\qquad
 \Theta_\sigma(r_*,\phi)=\phi .
$$
Then
$(\partial_r-c_\sigma\partial_\phi)(\Theta_\sigma)_\phi
=d_\phi(\Theta_\sigma)_\phi$.
The leading height amplitude is therefore proportional to
$$
 E(r)q(r)^{-1/2}(\Theta_\sigma)_\phi^2,\qquad
 E(r)=\exp\!\left[-2\int_{r_*}^r
             b(t)\langle\mathcal S(t)\rangle\,dt\right].
                                                               \tag{L.4}
$$
This identity retains the actual nonradial square and true mean.

## 2. The exact two leading amplitudes in the actual fold

Use
$$
 \Phi_\pm=X\pm\tfrac23(-T)^{3/2},\qquad
 T=-\rho A^{2/3},\quad q^2=\rho k,\quad \rho=r_*-r .
                                                               \tag{L.5}
$$
The $\Phi_\pm$ are paired with the $\Theta_\sigma$ by their actual
speed; the displayed signs need not equal the wave-row signs.
All powers use the branch fixed by the positive real root data.
For $k_*=k(0)$ and $\eta_*=\eta(0)$ define
$$
 G=(k_*/\eta_*)^{1/6}A^{1/6}k^{-1/4}E
   =(k_*/\eta_*)^{1/6}(-T/q^2)^{1/4}E.                \tag{L.6}
$$
The first expression defines the root value. It is analytic,
nonzero and $G(0,\phi)=1$; no zero-interval division occurs.

For $n=4|j|$ and $\epsilon=\operatorname{sgn}j$, the leading
two-amplitude solution is
$$
 \boxed{\quad a_0=G(X_\phi^2-TT_\phi^2),\qquad
             b_0=-2i\epsilon G X_\phi T_\phi .\quad}  \tag{L.7}
$$
Its convention is exactly
$$
 U_n(a_0,b_0)=e^{i\epsilon nX}
 \{a_0\operatorname{Ai}(n^{2/3}T)
             +b_0n^{-1/3}\operatorname{Ai}'(n^{2/3}T)\}.
                                                               \tag{L.8}
$$
The old $\phi$ derivatives in (L.7) are taken before composition
with the actual inverse $(r,\phi)=(r(T,X),\phi(T,X))$.

On the strict negative side put $t=\sqrt{-T}$. The phase
$e^{i\epsilon n\Phi_\pm}$ has coefficient
$a_0\mp i\epsilon t b_0$ relative to its free Ai coefficient.
Exactly,
$$
 a_0\mp i\epsilon t b_0
       =G(X_\phi\mp tT_\phi)^2
       =G(\Phi_\pm)_\phi^2.                          \tag{L.9}
$$
Multiplying (L.6) by the common Airy height factor $(-T)^{-1/4}$
recovers (L.4), with its fixed common root normalization.
Thus each branch satisfies the actual leading transport.
Away from the root the two branch equations determine $a_0,b_0$;
analytic extension gives (I.19) at the root and on the positive side.
This proof uses the complete original two rows.

Since $T_\phi=O(T^2)$ in the paid fold,
$$
 a_0(0,X)=1,\qquad b_0=O(T^2).                         \tag{L.10}
$$
For real data $a_0$ is real and $b_0$ purely imaginary with the
displayed sign. The reflection symmetries make $a_0$ even and
$b_0$ odd in the old angle. No finite Fourier assumption was used.

## 3. Exact cancellation of the centre's radial derivative in leading transport

The ordered principal-plus-first-derivative operator is
$$
 \mathcal L=D_r^2-\eta^2q^2\partial_\phi^2
        -(\eta_r/\eta+\bar T)D_r,\qquad
 \bar T=-4b\langle\mathcal S\rangle+5d_\phi .
$$
The exact commutator $[D_r,\partial_\phi]=d_\phi\partial_\phi$
and $D_r\Theta_\sigma=\sigma\eta q(\Theta_\sigma)_\phi$ imply
$$
 \mathcal L\Theta_\sigma
 =\left(q_r/q+4b\langle\mathcal S\rangle-4d_\phi\right)
                                        D_r\Theta_\sigma .
                                                               \tag{L.11}
$$
The $\eta_r$ term cancels identically; no even mean or residual is set
to zero.

Let $H=q_r/q+4b\langle\mathcal S\rangle-4d_\phi$ and retain the
actual principal factor $\mu$. In physical $r$ orientation the
first derivative coefficients after the fold are
$$
 l=\frac{H D_rT}{\mu}-\frac1{2T},\qquad
 T^2m=\frac{H D_rX}{\mu}.                             \tag{L.12}
$$
Indeed $Q=(\Phi_+-\Phi_-)/2$ obeys $\mathcal LQ=H D_rQ$ and
$T=f(Q)=-(3Q/2)^{2/3}$. The principal quadratic form of $Q$
is $\mu(-T)$, while $f''(Q)(-T)=-1/(2T)$.
The apparent singularity in (L.12) cancels at the true root,
as also proved by the analytic fold theorem.

The full lower operators, including $R_{-1}D_r$, remain in the
next amplitude equation. Their radial derivatives are not removed
by this cancellation or replaced by a local scalar potential.

## 4. A quantitative contract using completed complex bounds

Take $R=9/10^6$. Use the paid fold constants
$a_+,A_-,A_+,j,T_+,B_T,D_1,D_2,\eta_{\rm inv}$ from
(F.7)--(F.14). Use $\eta_+,B,k_->0$ from the original complete
complex mean, metric and $K_r$ enclosures.
The latter real-part bound applies to $k$ by its convex integral.

Set
$$
 k_+=a_+^2\eta_{\rm inv}^2,\qquad
 U_0=630/1000,\quad V_0=1791/1000,\qquad
 h_E=2RB(U_0^2+Rk_+V_0^2).                            \tag{L.13}
$$
The rational field bounds already passed the full-family root
Cauchy consumer and come from whole complex root-domain Fourier
norms. The mean in (L.4) may use those original bounds without
angular-strip inflation. Thus $|E|,|E^{-1}|\le e^{h_E}$.

Complete complex bounds for $G$ and its inverse are
$$
 G_+=(k_+\eta_{\rm inv})^{1/6}
                         A_+^{1/6}k_-^{-1/4}e^{h_E},
$$
$$
 G_{\rm inv,+}=(\eta_+/k_-)^{1/6}
                         A_-^{-1/6}k_+^{1/4}e^{h_E}.
                                                               \tag{L.14}
$$
These use the nonzero analytic branches already fixed.
The amplitudes then satisfy
$$
 \|a_0\|_\infty
 \le G_+\{(1+j)^2+T_+B_T^2\}=:A_0^+,\qquad
 \|a_0^{-1}\|_\infty
 \le\frac{G_{\rm inv,+}}{1-2j-j^2-T_+B_T^2}.           \tag{L.15}
$$
The denominator is required positive.
The root divisibility has the genuine quantitative bound
$$
 \left\|b_0/T^2\right\|_\infty
 \le\tfrac45G_+(1+j)a_+D_2 A_-^{-5/3}e^{4D_1R}
                                         =:B_2^+.   \tag{L.16}
$$
Use the pointwise (F.14) inequality
$|T_\phi|\le(2/5)a_+D_2 A_-^{-1/3}|\rho|^2e^{4D_1R}$
and $|T|\ge|\rho|A_-^{2/3}$. No uniform error ball is divided
by a number tending to zero.
Each complete branch coefficient in (L.9) has inverse bound
$$
       G_{\rm inv,+}/(1-j-\sqrt{T_+}B_T)^2.            \tag{L.17}
$$
The proposed gates are $A_0^+<51/50$, both inverse bounds
$<51/50$, and $B_2^+<6$. An actual successful public execution
is required to activate these numerical thresholds.

The estimates hold on the actual canonical rectangle
$|T|\le81/4000000$, $|\Im X|\le1/128$ because its inverse image
is inside the paid old product. On
$|T|\le19/10^6$, $|\Im X|\le1/256$, Cauchy gives, for any
specified nonnegative integers $p,q$,
$$
 \|\partial_T^p\partial_X^q a_0\|_\infty
       \le p!q! A_0^+ (800000)^p(256)^q,              \tag{L.18}
$$
and the same formula for $b_0/T^2$ with $B_2^+$.
These are complete derivative bounds; sharper direct bounds may
be needed. They do not certify the numerical strong-return budget.

## 5. Exact seam transmission and the remaining amplitude obligation

At a strict original radial seam the repaired centre values,
their angular derivatives, and the intrinsic values agree exactly.
Hence $A,B,d$ in the ordered scalarization have equal traces.
Where the full inverse $J=A^{-1}$ has been paid on the declared
space, it is continuous there by the resolvent identity.

For the homogeneous reconstruction $h_2=f$, $h_1=J(D_r-B)f$,
exact transmission is
$$
 [h_1]=[h_2]=0\quad\Longleftrightarrow\quad[f]=[f_r]=0 .
                                                               \tag{L.19}
$$
Brackets are right trace minus left trace. For a finite trial,
keep instead the complete formula
$$
 [h_2]=[f],\qquad
 [h_1]=J\{[f_r]-d\partial_\phi[f]-B[f]\}.              \tag{L.20}
$$
Nonzero even mean or second-row source contributes its full terms
in the reconstruction. Formula (L.20) does not remove those ports.

On a larger real radial window with continuous coefficients and
piecewise radial derivatives, the characteristic labels and their
fixed angular derivatives are $C^1$ in $r$.
Across strict seams $q,q_r$ are continuous; (L.4)--(L.7) then make
the leading amplitudes $C^1$ in the original $(r,\phi)$.
Thus (L.8) and its exact full two-row reconstruction have zero
value jumps wherever their full $J$ inverse is available.
This conclusion concerns the leading trial, not a fictitious
joint holomorphic continuation across all pieces.

The next amplitude forcing contains radial derivatives of the
original coefficients and may jump. Its exact (L.20) jump must be
supplied to the true Green or propagation map. A formal jump order
does not certify an operator norm, and the leading-amplitude
bounds do not evaluate $C_E,C_s$.

A larger piecewise construction still needs actual angular domains,
the full inverse and ordinary-source estimates on that window,
every radial interface, the next complete amplitudes and a useful
strong-remainder bound. No cutoff-97 inverse, nonzero-parameter
positive transfer or true nonlinear PDE branch follows here.
