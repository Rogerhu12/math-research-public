# The actual good pullback, the bad source, and its unflat limit

Date: 2026-11-27. Session: Astra-rank2-Sha-0b097461-20261127.

This note pays the bounded-source gate left in section 2 of the original
bad-CM $b=2$ note. It keeps the actual full tame level, the same
coefficient source, and the complete Maass operator. It proves neither
a usual-depletion identity nor a nonzero flat value.

## 1. The fixed source and the two actual maps

Use the original full $2$/full $9$ transported tame level. Let $w_0$
be the fixed weight-three algebraic modular source, and set
$$
 F_0=w_0/\omega_{\rm can}^{\otimes3}
     =y_{\rm dR}^3 f_0,\qquad f_0=w_0/s^{\otimes3}.
 \tag{1}
$$
The ratio $f_0$ is an actual completed structure-sheaf germ on the
locus where the fake Hasse invariant $s$ trivializes the Hodge line.
It is not asserted to be a modular eigenvector of a new $p$-operator.

At the original inert CM point $y$, take the chosen basis of book
Proposition 7.7 and put
$$
 g_1=\operatorname{diag}(p,1),\quad
 g_2=\operatorname{diag}(1,p),\quad y'=yg_1,\quad
 Q_b=\exp((z_{\rm dR}-\theta z_{\rm dR})/p^b).
 \tag{2}
$$
The period and differential transformations used here are the original
ones of the bad-$b=2$ note:
$$
\begin{array}{c|cccc}
 &z_{\rm dR}&\hat z&\omega_{\rm can}&dz_{\rm dR}\\ \hline
 g_1^*&p^{-1}z_{\rm dR}&p^{-1}\hat z&\omega_{\rm can}&p^{-1}dz_{\rm dR}\\
 g_2^*&pz_{\rm dR}&p\hat z&p\omega_{\rm can}&p\,dz_{\rm dR}\\
 (pI)^*&z_{\rm dR}&\hat z&p\omega_{\rm can}&dz_{\rm dR}
\end{array}
 \tag{3}
$$
In particular $g_1^*Q_1=Q_2$. The formula
$y_{\rm dR}^{-1}=1-z_{\rm dR}/\hat z$ gives
$g_2^*y_{\rm dR}=y_{\rm dR}$, with the same coefficient transport.

The complete original tame central character is
$\langle p\rangle=-1$. The source and line factors are separately
$$
 (pI)^*w_0=-p^3w_0,\qquad
 (pI)^*\omega_{\rm can}^{\otimes3}=p^3\omega_{\rm can}^{\otimes3},
 \qquad (pI)^*F_0=-F_0.
 \tag{4}
$$
This is the full-level central action paid in the original inert
$p^2$-norm note, section 2, and the actual psi4 graph note, section 4.
Neither the full $9$ character nor the Hodge-line factor is suppressed.

## 2. The good source really has a bounded expansion

Define the actual good source
$$
 F_{\rm good}=g_2^*F_0
     =y_{\rm dR}^3(g_2^*f_0)
 \quad\hbox{at }y'.
 \tag{5}
$$
The action $g_2^*$ preserves the completed structure sheaf and the
period sheaf on this diagonal-stable locus. Thus $g_2^*f_0$ is a
completed structure-sheaf germ, bounded after multiplication by a
fixed power of $p$, and (5) belongs to the actual period sheaf
$\mathcal O_\Delta$. These facts use the original pullback, not an
identification with an arbitrary prime-to-$p$ eigenform.

Book Lemma 6.16 applies to $y_{\rm dR}^k f$ for an arbitrary such
completed structure-sheaf germ $f$ with $y_{\rm dR}^kf$ in
$\mathcal O_\Delta$. It does not require that $f$ be the coefficient
of the original tame newvector. Its point hypotheses at $y'$ are
precisely the ones paid by Corollary 7.8. Since $p>2$, odd $k=3$
is allowed. Consequently, for some finite $M$,
$$
 F_{\rm good}(Q_1)\in
 p^{-M}\mathcal O_{\mathbf C_p}[[Q_1-1]].
 \tag{6}
$$
Here and below evaluation of the actual coefficients at the geometric
point is part of the notation. No value of $M$ or period-unit claim is
inferred from the lemma.

Pull back the entire expansion, its coefficients, and its domain by
$g_1$. Equations (3)--(4) give
$$
 A(Q_2):=g_1^*F_{\rm good}(Q_2)=-F_0(Q_2),\qquad
 A\in p^{-M}\mathcal O_{\mathbf C_p}[[Q_2-1]].
 \tag{7}
$$
The coefficient embedding is isometric, so the coefficient norm in
(7) is the same as the norm in (6). If the pulled weight-three
section rather than its normalized coefficient is used, its
coefficient is $p^3F_{\rm good}$, and every coefficient valuation
increases by exactly $3$.

With the chosen CM basis,
$|\theta y_{\rm dR}(y)|=|\hat z(y)|=1$,
$|\hat z(y')|=p$, and $|\theta y_{\rm dR}(y')|=1$.
The good and bad connection constants therefore match:
$$
 g_1^*\left(-p\,\frac{\theta y_{\rm dR}}{\hat z}\right)_{y'}
 =-p^2\,\frac{\theta y_{\rm dR}}{\hat z}\bigg|_y=:C,
 \qquad v_p(C)=2 .
 \tag{8}
$$
This is not the assertion that the CM period $\Omega_p$ is a unit.

## 3. Full raising, and the precise factor $p^{2n}$

Write $\delta_k$ for the original scalar Maass operator and
$\delta_3^n=\delta_{3+2n-2}\cdots\delta_3$. In the actual horizontal
coordinates it is $\partial_z+k/(z-\bar z)$, with both periods
transported. Equation (3) gives, at every weight,
$$
 g_1^*\delta_k=p\,\delta_k g_1^*,\qquad
 \delta_k g_2^*=p\,g_2^*\delta_k,\qquad
 (pI)^*\delta_k=\delta_k(pI)^* .
 \tag{9}
$$
Thus the complete all-$n$ source identity is
$$
 \boxed{\;
 g_1^*\!\left[(p\delta_3)^n(g_2^*F_0)\right]
   =(p^2\delta_3)^n((pI)^*F_0)
   =-p^{2n}\delta_3^nF_0 .
 \;}
 \tag{10}
$$
The center contributes only the minus sign on normalized
coefficients. The factor $p^{2n}$ comes from the scaled good raising
operator and its transport, not from multiplying a second central
raised-weight factor.

One must also distinguish raising a pulled coefficient from pulling
a previously raised tensor. With
$\widehat F=p^3g_2^*F_0$, the former is
$$
 (p\delta_3)^n\widehat F
      =p^{3+2n}g_2^*(\delta_3^nF_0).
 \tag{11}
$$
The raise-before-pull expression of the form used in book
Definition 7.19 is
$$
 F_n'=p^3g_2^*(p^n\delta_3^nF_0)
      =p^{3+n}g_2^*(\delta_3^nF_0).
 \tag{12}
$$
Consequently (11) equals $p^nF_n'$. This comparison is made on the
true $\omega_{\rm can}^{\otimes3}\otimes(dz_{\rm dR})^{\otimes n}$
basis. It does not replace that basis by
$\omega_{\rm can}^{\otimes(3+2n)}$ without its determinant factor,
and it does not assert that a usual-depleted version of (12) equals
the flat reader.

For later coefficient use, define the exact unflat value
$r_n(y)=\theta(\delta_3^nF_0)(y)$. The actual input to the finite
Newton reader is therefore
$$
 R_n=\theta((p^2\delta_3)^n A)(y)=-p^{2n}r_n(y).
 \tag{13}
$$
All CM periods, the original Gaussian and finite source weights
remain inside $r_n$.

## 4. Exact scope and continuation

All root rotations and all coefficients transport, so
$g_1^*(\flat_1 F_{\rm good})=\flat_2A=-\flat_2F_0$.
This is the actual analytic $Q$ average; no CM-isogeny or usual
depletion interpretation is used.

The input (13), together with all original finite weights, can now
be passed to the proved flat Amice/Newton reader. It does not
promise a nonzero reader. [R1052](../results/R1052-original-unmodified-b2-toric-flat-vanishing.md)
proves the complete unflat-to-flat limit directly, fixes the book's
actual period convention $\omega_{\rm can}\Omega_p=\omega_0$,
and combines the full original theta coefficient bounds with (13).
For the original unmodified degree102/34 toric source its conclusion
is that this $b=2$ branch and its slope are identically zero.
That conclusion concerns the complete toric sum, not individual
point measures, and gives no new zero condition on the canonical
Newton derivative.

The actual connection primitive uses the book/R997 positive
Kodaira--Spencer and Tate pairing conventions, as now stated in
section 4 of the [flat reader note](2026-11-27-original-flat-amice-critical-slope-and-bol-primitive.md).
The 2018 opposite pairing and primitive must be changed together.

## Sources

- D. J. Kriz, AMS212 (2021), Lemma 6.16 (6.54), Proposition 7.7,
  Corollary 7.8, (7.13), and Definition 7.19.
  The proof above does not use Proposition 7.20.
  [Book text](https://dokumen.pub/supersingular-p-adic-l-functions-maass-shimura-operators-and-waldspurger-formulas-ams-212-9780691225739.html).
- [Original bad-CM source and boundary](2026-11-27-original-bad-cm-b2-source-and-p-square-boundary.md),
  sections 1--4.
- [Original inert full norm](2026-11-27-original-inert-p-square-full-norm-and-endpoint-zero.md),
  section 2, and [original psi4 full graphs](2026-11-27-original-psi4-full-graphs-artin-and-geometric-newton-cross.md),
  section 4, for the complete central character.
- [Actual flat moments and Newton reader](2026-11-27-original-flat-amice-critical-slope-and-bol-primitive.md).

Only paper proofs are used; no new mathematical execution was made.
