# R133 supplement: genuine common-radial reference columns and complete two-source ports

2026-11-15, visible-exact / phase_inverse.

**Proved analytic consequence of the actual common-potential enclosure.**
This constructs two independent solutions of the complete radial reference,
including its finite-frequency potential. The construction supplies an exact
Wronskian, a root change of basis with a complete $n^{-4/3}$ bound, uniform
negative-side relative Cauchy bounds, and both positive-side weighted columns.
The physical positive boundary row is retained as an independent row.

The numerical input is
[the actual complete common-radial potential and root-piece image](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md),
from public Actions run **43685624307/1**. Its original mathematical process
returned zero and passed all sixteen gates. In particular the largest successful
case gives $|V|<276$ on a common complex $T$ disk whose radius exceeds
$0.000742956050168040$. No original target, FFT, intrinsic derivative, or accepted
Taylor coefficient is recomputed in this proof. A separate scalar consumer may
check the rational instantiation below; this text does not report such a new run.

## 1. Object, domain, and the exact equation

Keep fixed intrinsic $\eta_0$, the complete repaired 65-mode background,
the complete repaired 193-mode direction, and the original complex parameter
square $|\Re\delta|,|\Im\delta|\le10^{-8}$. For $|j|\ge97$ set
$$
 n=4|j|,\qquad \epsilon=\operatorname{sgn}j,\qquad
 z=j^{-2},\qquad \lambda=n^{2/3}.
 \tag{A.1}
$$
The potential is exactly $V(z,T)$ of (C.11)--(C.14) in
[the common radial Langer reference](R133-supplement-common-radial-Langer-reference-and-complete-source-ports.md),
with the cancellation-preserving formula and actual modulus gaps already paid.
It is not an arbitrary replacement of the original local coefficient.

Take
$$
 L=\frac1{2000},\qquad M=276,\qquad I=[-L,L].
 \tag{A.2}
$$
The actual common-coordinate image contains the closed complex disk $|T|\le L$.
Thus the same $V$ is holomorphic there, and $|V|\le M$ throughout that disk,
uniformly in the already certified parameter and rational-frequency boxes.
The bounds proved below are for **real $T\in I$**, while $V$ and the parameter
may still be complex. Holomorphic existence does not, by itself, extend the
displayed real-axis column bounds to an old complex angular strip.

The reference equation and its two-state matrix are
$$
 Y_{TT}=(n^2T-V(z,T))Y,\qquad
 \frac d{dT}\binom YP
 =
 \left[
 \begin{pmatrix}0&1\\n^2T&0\end{pmatrix}
 +\begin{pmatrix}0&0\\-V&0\end{pmatrix}
 \right]\binom YP.
 \tag{A.3}
$$
Here $P=Y_T$ only for a homogeneous column. In the presence of the first
ordinary source, the state $P$ remains an independent component.

The auxiliary radial extension agrees with the physical coefficients only on
the original physical piece 2549. Its complete physical piece is contained
in the paid old-radius image of the largest potential case. This does not
identify the neighboring physical cubics with that auxiliary extension.

## 2. Elementary free Airy inequalities with explicit constants

Write
$$
 A(t)=\operatorname{Ai}(t),\qquad B(t)=\operatorname{Bi}(t).
$$
We use the exact Airy equation, initial values, and Wronskian in
[DLMF 9.2.1, 9.2.3--9.2.6, and 9.2.7](https://dlmf.nist.gov/9.2),
and only their standard positive-axis decay and growth from
[DLMF 9.7.5--9.7.8](https://dlmf.nist.gov/9.7).
The numerical inequalities used here are derived below; no truncated
asymptotic series is used as an error bound.

The gamma integral and $1-t\le e^{-t}\le1-t+t^2/2$ for $0\le t\le1$ give
$$
 \frac9{10}<\Gamma(2/3)<\frac{117}{80},\qquad
 \frac94<\Gamma(1/3)<\frac72.
 \tag{A.4}
$$
For the upper bounds, the tails from one to infinity are at most $e^{-1}$;
use $e^{-1}<3/8$ for $\Gamma(2/3)$ and $e^{-1}<1/2$ for
$\Gamma(1/3)$. The first integral for $\Gamma(2/3)$ is at most $87/80$.
Consequently, for
$$
 q_0=-A'(0)/A(0)=3^{1/3}\Gamma(2/3)/\Gamma(1/3)
$$
one has
$$
 \frac14<q_0<\frac{39}{40},\qquad
 0<A(0),B(0),-A'(0),B'(0)<1,\qquad
 |A'(0)|<\frac13.
 \tag{A.5}
$$
For example $3^{1/6}>10/9$ and $\Gamma(2/3)>9/10$ prove $B(0)<1$;
$3^{1/3}>4/3$ proves the last inequality.

On $t\ge0$, $A>0$, $A'<0$, $B>0$, and $B'>0$. Set
$q=-A'/A$ and $p=B'/B$. The exact energy identity is
$$
 A'(t)^2-tA(t)^2=\int_t^\infty A(s)^2\,ds.
 \tag{A.6}
$$
It follows that $q'=q^2-t>0$. Since
$A(t+u)/A(t)\le e^{-q(t)u}$, (A.6) also gives
$q^2-t\le1/(2q)$. If $q\ge1/2$, this is at most one;
if $q<1/2$, then $q^2<1/4<1+t$. Hence $q<\sqrt{1+t}$.
The equation $p'=t-p^2$, the initial value $p(0)=q_0<1$, and the
strict upper barrier $\sqrt{1+t}$ give the same upper bound for $p$.
Together with the Wronskian this proves
$$
 \frac14<q(t)<\sqrt{1+t},\qquad
 0<p(t)<\sqrt{1+t},\qquad
 A(t)B(t)=\frac1{\pi(p(t)+q(t))}<\frac4\pi.
 \tag{A.7}
$$
In particular $B/A$ is strictly increasing.

For the negative axis put $y(s)=A(-s)$ or $B(-s)$, so
$y''+sy=0$. On $[0,1]$, $E=y^2+y'^2$ satisfies
$E'\le(1-s)E$, and $E(0)<2$. Thus $E(s)<2e^{1/2}<4$.
For $s\ge1$, $H=y'^2+sy^2$ satisfies
$(H/s)'=-y'^2/s^2\le0$. Therefore
$$
 |A(-s)|,\ |B(-s)|<2,\qquad
 |A'(-s)|,\ |B'(-s)|<2\max(1,\sqrt s)
 \quad(s\ge0).
 \tag{A.8}
$$
Finally (A.6) at zero yields
$$
 \int_0^\infty A(t)^2\,dt=A'(0)^2<\frac19.
 \tag{A.9}
$$

## 3. Two genuinely independent positive-side columns

Let
$$
 F_n(T)=
 \begin{pmatrix}
 A(\lambda T)&B(\lambda T)\\
 \lambda A'(\lambda T)&\lambda B'(\lambda T)
 \end{pmatrix},
 \qquad \det F_n=\frac{\lambda}{\pi}.
 \tag{A.10}
$$
Define $f_n$ by the exact equation (A.3) and the exact terminal data
$$
 \binom{f_n}{(f_n)_T}(L)
       =\binom{A(\lambda L)}{\lambda A'(\lambda L)}.
$$
Define $g_n$ by the same exact equation and the root data
$$
 \binom{g_n}{(g_n)_T}(0)
       =\binom{B(0)}{\lambda B'(0)}.
 \tag{A.11}
$$
These are definitions of a reference basis. The physical positive boundary
condition is not being imposed by (A.11), nor identified with its Ai terminal row.

For
$$
 K_n(T,S)=\frac{\pi}{\lambda}
 \{A(\lambda T)B(\lambda S)-B(\lambda T)A(\lambda S)\},
$$
variation of constants gives the signed equations
$$
 \begin{split}
 f_n(T)&=A(\lambda T)-\int_T^L K_n(T,S)V(z,S)f_n(S)\,dS,\\
 g_n(T)&=B(\lambda T)+\int_0^T K_n(T,S)V(z,S)g_n(S)\,dS.
 \end{split}
 \tag{A.12}
$$
For $0\le T\le S$, (A.7) and monotonicity of $B/A$ give
$$
 |K_n(T,S)|\,\frac{A(\lambda S)}{A(\lambda T)}
          \le\frac8\lambda,
 \qquad
 |\partial_TK_n(T,S)|\,
 \frac{A(\lambda S)}
      {\lambda\sqrt{1+\lambda T}\,A(\lambda T)}
          \le\frac8\lambda.
 \tag{A.13}
$$
The first estimate even holds with four in place of eight. For the derivative,
use separately $|A'|/A$ and $B'/B$ from (A.7).
For $0\le S\le T$, the corresponding two estimates hold with $B$ in place of
$A$. The constants do not depend on $\lambda L$, which can be arbitrarily
large as $j$ increases.

With
$$
 \tau_+=\frac{8ML}{\lambda},
$$
the ordered Volterra series and its differentiated integral give
$$
 \begin{split}
 |f_n(T)|&\le e^{\tau_+}A(\lambda T),&
 |(f_n)_T(T)|&\le e^{\tau_+}
          \lambda\sqrt{1+\lambda T}\,A(\lambda T),\\
 |g_n(T)|&\le e^{\tau_+}B(\lambda T),&
 |(g_n)_T(T)|&\le e^{\tau_+}
          \lambda\sqrt{1+\lambda T}\,B(\lambda T).
 \end{split}
 \tag{A.14}
$$
For instance the derivative error in the first line is at most
$e^{8M(L-T)/\lambda}-1$ in its displayed normalized weight, while the
free derivative is at most one. This proves (A.14) without differentiating $V$.

## 4. Exact root normalization and the complete shear

Express the two-state value of $f_n$ at zero as
$$
 \binom{f_n}{(f_n)_T}(0)=F_n(0)\binom{a_n}{b_n}.
$$
The exact interaction matrix is
$$
 F_n^{-1}
 \begin{pmatrix}0&0\\-V&0\end{pmatrix}F_n
 =
 \frac{\pi V}{\lambda}
 \begin{pmatrix}AB&B^2\\-A^2&-AB\end{pmatrix},
 \tag{A.15}
$$
where the Airy arguments are $\lambda T$. Since the coefficient vector at
$L$ is $(1,0)^t$, integration backwards gives
$$
 a_n=1-\frac{\pi}{\lambda}\int_0^L V(z,S)B(\lambda S)f_n(S)\,dS,
 \qquad
 b_n=\frac{\pi}{\lambda}\int_0^L V(z,S)A(\lambda S)f_n(S)\,dS.
 \tag{A.16}
$$
Therefore
$$
 |a_n-1|\le\frac{4ML}{\lambda}e^{\tau_+},\qquad
 |b_n|\le\frac{\pi M}{9\lambda^2}e^{\tau_+}.
 \tag{A.17}
$$
The second inequality uses the whole integral (A.9), not an assumption that
the Airy argument is small.

The rational instantiation uses
$52^3<388^2$, hence $\lambda>52$, and $\pi<4$:
$$
 \tau_+<\frac{69}{3250}<\frac1{40},\qquad
 e^{\tau_+}<\frac{40}{39},\qquad
 |a_n-1|<\frac1{78},\qquad |a_n|>\frac{77}{78}.
 \tag{A.18}
$$
The exponential inequality follows from $e^t\le(1-t)^{-1}$ for $0\le t<1$.

Define the normalized column $\widehat f_n=f_n/a_n$ and
$\beta_n=b_n/a_n$. Then
$$
 \Psi_n(T)=
 \begin{pmatrix}
 \widehat f_n(T)&g_n(T)\\
 (\widehat f_n)_T(T)&(g_n)_T(T)
 \end{pmatrix},
 \quad
 \det\Psi_n(T)=\frac{\lambda}{\pi},
 \quad
 F_n(0)^{-1}\Psi_n(0)=
 C_n:=\begin{pmatrix}1&0\\\beta_n&1\end{pmatrix}.
 \tag{A.19}
$$
In particular both columns are independent throughout the common domain.
Moreover
$$
 |\beta_n|
 <\frac{320}{693}M n^{-4/3}
 <\frac M2 n^{-4/3}
 <\frac1{19},\qquad
 \|C_n\|_2,\ \|C_n^{-1}\|_2<\frac{20}{19}.
 \tag{A.20}
$$
The final inequality follows from $138\cdot19<52^2$.
This is a complete reference change of basis with the displayed angular gain,
including both input signs. It is not an estimate of the physical nonradial
root reflection or of the full return remainder.

The positive columns now satisfy
$$
 \begin{split}
 |\widehat f_n(T)|&<\frac{21}{20}A(\lambda T),&
 |(\widehat f_n)_T(T)|&<
       \frac{21}{20}\lambda\sqrt{1+\lambda T}\,A(\lambda T),\\
 |g_n(T)|&<\frac{21}{20}B(\lambda T),&
 |(g_n)_T(T)|&<
       \frac{21}{20}\lambda\sqrt{1+\lambda T}\,B(\lambda T).
 \end{split}
 \tag{A.21}
$$
Indeed the first factor is at most $(78/77)(40/39)=80/77<21/20$;
the second is at most $40/39<21/20$.
Both the decaying and the growing column are present.

## 5. Negative-side ordered propagation in the full free frame

Continue the same columns, without changing their root data, onto $[-L,0]$.
Set $Z_n(T)=F_n(T)^{-1}\Psi_n(T)$. Then
$$
 (Z_n)_T=\mathcal K_n(T)Z_n,\qquad
 \mathcal K_n=
 \frac{\pi V}{\lambda}
 \binom{B}{-A}\begin{pmatrix}A&B\end{pmatrix},
 \quad Z_n(0)=C_n .
 \tag{A.22}
$$
For real negative $T$, the free Airy functions are real. Their two height
bounds (A.8) show
$$
 \|\mathcal K_n(T)\|_2
 \le\frac{\pi M}{\lambda}\{A(\lambda T)^2+B(\lambda T)^2\}
 <\frac{8\pi M}{\lambda}.
$$
No derivative row is discarded in this identity: the exact inverse of the
two-row matrix $F_n$ has already been taken before estimating the rank-one
interaction matrix.

Let $\mathcal U_n(T,S)$ be the complete ordered propagator for $\mathcal K_n$.
With
$$
 \tau_-=\frac{8\pi ML}{\lambda}<4\tau_+<\frac1{10}
$$
its forward and reverse ordered series give
$$
 \|\mathcal U_n(T,S)\|_2,\ \|\mathcal U_n(T,S)^{-1}\|_2
 \le e^{\tau_-}<\frac{10}{9}
 \quad(-L\le T,S\le0).
 \tag{A.23}
$$
Combining this with (A.20) proves
$$
 \|F_n(T)^{-1}\Psi_n(T)\|_2,\
 \|\Psi_n(T)^{-1}F_n(T)\|_2
 <\frac{200}{171}<\frac65.
 \tag{A.24}
$$
For the genuine potential propagator
$\Phi_n(T,S)=\Psi_n(T)\Psi_n(S)^{-1}$, one may use the direct stronger bound
$\|F_n(T)^{-1}\Phi_n(T,S)F_n(S)\|_2<10/9$ from (A.23),
or the product bound $36/25$ from (A.24).
The relative-frame matrices are diagonal in the physical Fourier label,
so these bounds hold on the full direct sum of all $|j|\ge97$ with any
common Sobolev weight on the two coefficient components.
They are not same-order bounds on the unweighted physical state:
the Airy frame and the Liouville/Piola matrices retain their actual powers
of $n$.

The two signed oscillatory Airy combinations are obtained by the fixed unitary
right matrix
$2^{-1/2}\begin{pmatrix}1&1\\i&-i\end{pmatrix}$.
Applying that same matrix to $F_n$ and $\Psi_n$ preserves (A.24).
For complex parameters this is a two-column algebraic change of basis,
not a replacement of one sign by complex conjugation.

## 6. Full sources, root ports, and the independent positive boundary row

For the complete two-source reference of (C.14), put
$$
 \widetilde g_j(T)=
 \binom{g_{2,j}/(\kappa G)}
       {(A_jg_{1,j}+c\,g_{2,j})/(\kappa^2G)}.
$$
The exact solution with initial state $u_j(S)$ is
$$
 u_j(T)=\Psi_n(T)\Psi_n(S)^{-1}u_j(S)
       +\int_S^T
          \Psi_n(T)\Psi_n(s)^{-1}\widetilde g_j(s)\,ds .
 \tag{A.25}
$$
Both source rows are present. In particular (A.25) never differentiates
$g_{2,j}$. The factors $A_j=i\epsilon n a$ and
$dT=\kappa\,dr$ must be included when using physical ordinary $L^2_r$
source norms.

At the root the actual physical mixed trace is exactly
$$
 \binom{U_j}{n^{-2/3}P_j}_{r_*}
 =
 \begin{pmatrix}
 0&1\\
 i\epsilon a(z,r_*)/\kappa_*&
       n^{-2/3}c(z,r_*)/\kappa_*
 \end{pmatrix}
 \binom{n^{1/3}h_{1,j}}{h_{2,j}}_{r_*}.
 \tag{A.26}
$$
Equations (A.19) and (A.26) together specify the genuine root matching,
including the full finite-frequency coefficients and the nonzero shear.
The independent physical $j=0$ equation is retained separately; the analytic
parameter value $z=0$ represents the large-frequency limit and is not that mean.

If the actual positive endpoint supplies a row or a coupled full-frequency
map $\mathcal B$, substitute (A.25) into that row:
$$
 \mathcal B\,\Psi\,c+
 \mathcal B\int\Phi\,\widetilde g=g_B.
 \tag{A.27}
$$
Here $\mathcal B$ acts in its original physical/output order after the inverse
Liouville/Piola change. No entry of this row is set to zero by the definition
of $f_n$ or $g_n$. A coupled map also retains its low/head/mean inputs.
A denominator or Schur gate for (A.27) must still be proved with that actual map.
In particular (A.21) is a two-weight column bound, not a uniform unweighted
positive-side Cauchy bound.

Original physical trace jumps are transformed by (C.12)--(C.13) using their
true one-sided coefficients. Inside one original analytic piece, the reference
and its first derivative are a single solution, so an artificial internal cut
creates no jump. Crossing a true physical seam requires its complete original
two-state matching and all source jumps. It cannot be justified by the
auxiliary continuation alone.

## 7. Old-circle and strong-return scope

The columns just constructed are the real reference solutions required by
(I.1)--(I.14) of
[the complete old-circle primitive and mean interface](R133-supplement-common-radial-reference-old-circle-primitive-and-mean-interface.md).
Their analytic continuation exists on the common potential disk. To use a
complex old angle, their composition with the actual fold must additionally
be bounded on that complex image; (A.21)--(A.24) only supply the real-axis bounds.

The matrix
$H_j^V=H-(T_\phi V_j/n^2)E_{12}$ still needs its own complete gap and derivative
bounds on the declared old-circle domain. The original $P,I,J$, the full
nonmean/mean source terms, actual seams, and both frequency signs remain in
their original order. The finite recursion for $I$ is not an infinite inverse.

Finally, absorbing the complete radial potential changes the reference and
the known trial. Previously certified free-Airy source upper bounds cannot
be reassigned to the new trial without a true complete comparison or a new
consumer. The remaining nonradial principal flow, source remainder, physical
positive matching, and low/high feedback are not closed by this reference
lemma. No actual return arithmetic, nonlinear parameter realization, or
cutoff-97 full inverse is claimed here.
