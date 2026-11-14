# R106 supplement: true parameter derivatives of the seven moving-root fields

## 1. Actual uniform conclusion

For the unchanged exact step5 family

\[
 p_5=-7789843107295549/4611686018427387904,\qquad |p-p_5|\le10^{-9},
\]

use the actual positive root \(t(p)\), inward coordinate
\(\rho=t(p)-r\), and physical angle \(\theta\).
On the whole bidisk

\[
 |\rho|\le7/25000,\qquad |\Im\theta|\le1/400,
\]

the actual original-height fields have the following uniform derivative
bounds, where differentiation holds \(\rho,\theta\) fixed:

| True field \(f\) | Complete bound for \(|\partial_p f|_{\rho,\theta}\) |
| --- | ---: |
| \(G\) | \(0.000314\) |
| \(q\) | \(0.007897\) |
| \(k_*\) | \(0.264585\) |
| \(S_{\rm reg}\) | \(0.000285\) |
| \(L_\theta\) | \(0.009159\) |
| \(U_0\) | \(0.002027\) |
| \(U_1\) | \(0.824305\) |

These are actual whole-parameter, whole-bidisk estimates. In particular,

\[
 \sup_{\rho,\theta}|G(\rho,\theta,p)-G(\rho,\theta,p_5)|
       <3.14\,10^{-13}.                                     \tag{1}
\]

This is a bound for the complete nonmean function. It does not transport
an angular mean or a finite truncation. The same mean-value argument applies
to all seven fields.

The proof and native run are in
[the moving-root parameter producer](../scripts/fourfold_subprincipal_root_parameter_bidisk.py)
and

    notes/2026-11-13-R106-seven-field-moving-parameter-bidisk.json.gz

The report SHA256 is

    1b0c96c08ea72e16fddeabf91b74d81f539c4819a50af44ab97ec74f338778f8

## 2. Differentiating the shared actual parameter

The original and direction scalar spline germs are exact polynomials on the
same selected common span. They are differentiated before applying the shared
affine parameter. The existing true derivative target computes the exact
parameter derivative of every trigonometric tangent and of its linear
Fourier primitive:

\[
 F_p=a_p\,\mathcal P(T)+a\,\mathcal P(T_p)+Z_p e_z .
\]

Here \(\mathcal P\) is the unchanged original primitive and the tangent
derivative is evaluated analytically. Independent complete primitive bounds
are paid for \(F\) and \(F_p\); a parameter derivative of a floating reference
is not substituted.

For the physical-r derivative \(X=F_r\), the averaged target metric satisfies

\[
 E=\langle X\cdot X\rangle,\qquad E_p=2\langle X\cdot X_p\rangle.
\]

The existing target formula uses

\[
 C=a_r E_r-2a_{rr}E,\qquad K_0=\frac{C}{2aE^2},
\]

so the true fixed-r derivatives are

\[
\begin{aligned}
 C_p&=(a_p)_rE_r+a_r(E_p)_r
            -2(a_p)_{rr}E-2a_{rr}E_p,\\
 (K_0)_p&=\frac{C_p}{2aE^2}
       -K_0\left(\frac{a_p}{a}+2\frac{E_p}{E}\right).
\end{aligned}
\]

All finite Fourier terms, all independent primitive errors, and the complete
errors in \(E,E_p\) enter these formulas before division.

The same actual simple-root certificate and interval Newton refinement give
the full root interval. At this root, transversality is checked and the two
exact implicit derivative formulas are intersected:

\[
 t'(p)=-\frac{C_p}{C_r}=-\frac{(K_0)_p}{(K_0)_r}.
\]

The actual executed enclosure gives

\[
 0.0000611079949779<t'(p)<0.0000611079950021 .
\]

For every physical jet \(F_{r^a\theta^b}\), the correct moving-root derivative
is then

\[
 \left.\partial_p F_{r^a\theta^b}(t(p)-\rho,\theta,p)
 \right|_{\rho,\theta}
 =F_{r^a\theta^b p}+t'(p)F_{r^{a+1}\theta^b}.                 \tag{2}
\]

Thus the base geometry includes the required third physical radial jets,
and the parameter geometry includes all six fixed-r derivative jets.
Treating the certified root interval as a constant in (2) would miss a
necessary contribution; the producer does not do that.

## 3. Deflated curvature and its derivative without division by rho

The exact root identity gives the genuine analytic field

\[
 Q(\rho,p)=-K_0(t(p)-\rho,p)/\rho
          =\int_0^1(K_0)_r(t(p)-u\rho,p)\,du .
\]

Differentiating at fixed \(\rho\) yields

\[
\begin{aligned}
 Q_p&=\int_0^1\big((K_0)_{rp}+t'(p)(K_0)_{rr}\big)
                  (t(p)-u\rho,p)\,du,\\
 Q_\rho&=-\int_0^1u(K_0)_{rr}(t(p)-u\rho,p)\,du,\\
 (Q_\rho)_p&=-\int_0^1u\big((K_0)_{rrp}+t'(p)(K_0)_{rrr}\big)
                  (t(p)-u\rho,p)\,du .
\end{aligned}                                                \tag{3}
\]

The entire integration segments stay in the same paid complex rho disk.
Complete disk enclosures for the physical curvature jets therefore enclose
these averages. No division by a rho box containing zero occurs.

The disk curvature algebra uses the complete physical jets of \(E,E_p\)
through order four and of \(a,a_p\) through order five. The scalar radial
polynomials are exact; all omitted finite-series tails and true primitive
errors are bounded by the existing analytic Cauchy formulas. The radius and
\(E\) denominators have positive real part before the curvature is formed.
In the saved Taylor-jet notation,
\(K[2]=K_{rr}/2\) and \(K[3]=K_{rrr}/6\), so the enclosures in (3) are
implemented as

\[
 Q\in K[1],\quad Q_p\in K_p[1]+2t'K[2],\quad
 Q_\rho\in-K[2],\quad (Q_\rho)_p\in-K_p[2]-3t'K[3].
\]

The actual run gives \(\Re Q>54.55\). Consequently the principal square root
\(\kappa=\sqrt Q\) is holomorphic, and
\(\kappa_p=Q_p/(2\kappa)\) is its actual derivative.

## 4. Complete angular/radial geometry cover

The finite primitive is evaluated on every closed angular cell of
\(\Im\theta=+1/400\), with its exact Fourier multiplier
\(e^{-4j/400}\) applied before the inverse DFT. Real cell motion is bounded by
the full finite Fourier coefficient sum times its true frequency.
The infinite angular errors and finite radial Taylor tails are added
independently for every physical derivative. There are \(1024\) closed cells,
using \(512\) primitive nodes and radial precision \(48\).

For each field in (2), the enclosure is the fixed-r parameter enclosure plus
the actual \(t'\) enclosure times the extra base-radial derivative. These
are true parameter jets, represented by a pair \((v,d)\) satisfying

\[
 (vw)'=v'w+vw',\qquad
 (1/v)'=-v'/v^2 .
\]

The implementation first encloses the reciprocal and then squares it in
the reciprocal derivative, preserving separation from zero.
All seven original-height formulas are then evaluated on these dual jets.

On all boundary cells and the full rho disk, the actual positive-real
denominator minima satisfy

| Denominator | Strict lower bound |
| --- | ---: |
| area square | \(1.81218\) |
| \(F\cdot F\) | \(1.18533\) |
| support numerator | \(1.21302\) |
| \(F_z\) | \(0.26819\) |
| \(a_0\) | \(0.39426\) |

Schwarz conjugation gives the lower angular boundary for the entire rho
disk. The first geometric denominators are entire in the angle. Their
positive-real boundary bounds extend through the periodic strip by the
harmonic minimum principle; their reciprocals are therefore holomorphic.
The same argument then applies to \(a_0\). The theta-independent \(Q\)
branch has already been separated on the whole rho disk.
All seven fields and their actual parameter derivatives are thus holomorphic
in the angle, and their boundary modulus bounds extend to the whole strip.

For the regularized density, the exact decomposition
\(G=A+\rho B+\rho^2 C_2\) is used. Its derivative is bounded by

\[
 |G_p|\le |A_p|+R|B_p|+R^2|C_{2,p}|.
\]

The leading constant is not multiplied by a square enclosure for rho.
Every cell passes before the uniform table in Section 1 is reported.

## 5. Why this avoids the previous parameter wrapping loss

For a finite center approximation \(\widehat f\), suppose its complete
center error is \(e_{f,0}\) on the same bidisk. The real parameter interval
and the actual root function are connected, so the fundamental theorem of
calculus gives

\[
 f(\rho,\theta,p)-f(\rho,\theta,p_5)
 =\int_{p_5}^{p}\partial_\lambda f(\rho,\theta,\lambda)\,d\lambda.
\]

Thus the actual full-family approximation error is

\[
 \boxed{\ \|f(\cdot,p)-\widehat f\|
           \le e_{f,0}+10^{-9}M_{f,p}.\ }                    \tag{4}
\]

The parameter fee in (4) is paid for the complete function on the entire
complex bidisk, after using its shared analytic parameter. It does not pass
independent interval copies of that parameter through a weighted DFT.
All center aliases and unretained angular/radial modes remain in
\(e_{f,0}\). This proposition does not assert that the separate center
coefficient run has completed; its actual report must be supplied.

## 6. Reproduction

Run from the topic directory:

~~~bash
python3 scripts/fourfold_subprincipal_root_parameter_bidisk.py \
  --out notes/2026-11-13-R106-seven-field-moving-parameter-bidisk.json.gz
~~~

The actual run used python-flint \(0.9.0\), \(256\)-bit Arb arithmetic and
took about \(70.4\) seconds. The report retains all \(1024\) cell moduli,
positive-real gates, complete primitive/Cauchy fees, root derivative,
curvature-derivative enclosures, domain and source/input hashes. Its family
is the full original interval; no smaller parameter box is substituted.
