# R46 supplement: the complete actual strict operator and its full strong remainder

This note proves and executes the complete consumer for the old fixed-type R37 operator on

\[
 I=[-r_c,r_c],\qquad r_c=268136140016943/1125899906842624,
 \qquad p_5=-7789843107295549/4611686018427387904,
 \qquad |p-p_5|\le10^{-9}.
\]

It concerns this operator's actual material coefficients, potential, momentum
and characteristic flows. It does not transfer the separate nonlinear
Codazzi/Cauchy branch into these coefficients. The output theorem is the
R46 decomposition

\[
 \mathcal C_I=\mathcal W_0+R_2,
 \qquad R_2:E_s\longrightarrow E_{s+2},\quad |s|\le8,
                                                               \tag{S.1}
\]

with the actual four WKB branches, complete amplitude frame, mean and all
cross-frequency outputs. The completed native calculation covers 215 closed
positive radial cells, reflected exactly to the negative half. The complete
directed consumer proves

\[
 \boxed{\|R_2:E_s\to E_{s+2}\|<6.177244\,10^{502},\quad |s|\le8.}
\]

The true Cauchy bound over the required full shifted window is below
\(1.139199\,10^{251}\); the complete ordinary physical source-to-amplitude
gain is below \(5.598468\,10^{339}\). These are very large finite constants.
They close the stated whole strict-interval strong estimate, but are not an
effective final high inverse or a numerical claim that the actual evolution
has comparable size. The consumer refuses partial covers, changed sources or
different parameter families.

## 1. Same actual coefficients and complete native fields

Use the physical angle \(\theta\) of period \(\pi/2\), its full frequency
lattice \(4\mathbb Z\), and

\[
 Pu=\partial_r(au_r+bu_\theta)+\partial_\theta(bu_r+cu_\theta)+du,
 \qquad p=au_r+bu_\theta,
\]

\[
 \alpha=1/a,\quad v=b/a,\quad
 \mu=\sqrt{b^2-ac},\quad\gamma=\mu^2/a,\quad\nu=\mu/a,
 \quad m=\mu^{-1/2},\quad L=\log\mu.
\]

Here the target curvature is the exact synchronous \(K_0(p,r)\). The modified
coefficient is the actual \(c=(b^2-\mu^2)/a\), and
\(d=\tau+\sigma_\theta\) is the full zero-order coefficient of that same
fixed-type modification. The waist factor uses the true analytic quotient
\(F_z/r\). The field producer does not differentiate a quotient after
interval division by a radial box containing zero.

The native source `fourfold_strict_actual_wkb_fields.py` differentiates the
exact scalar spline germs and the complete degree-40 primitive before
interval evaluation. It retains full primitive, radial Taylor, infinite
angular and closed angular-cell errors through radial order five and angular
order five. The exact rotating-frame position identity

\[
 F_\theta=Y-J_{\rm rot}F
\]

supplies all angular jets from the same position jet. It avoids taking high
angular derivatives of a common nodal interval error as though that error
were a real high-frequency signal.

The WKB fields are paid on the full physical strip \(|\Im\theta|\le1/640\),
for each closed real radial cell and the whole real parameter interval.
Every geometric denominator and square-root branch is checked before use.
The exact potential and auxiliary fields are

\[
 \mathcal F=d-\tfrac12\operatorname{div}(A\nabla L)
                 +\tfrac14(\nabla L)^tA\nabla L,
 \quad T=(aL_r+bL_\theta)/2,
 \quad B_r=a_r+b_\theta-aL_r-bL_\theta.                       \tag{S.2}
\]

The same jet evaluation supplies \(\mathcal F_r,\mathcal F_\theta\) and the
first derivatives of both characteristic speeds. These are the ordinary R46
fields, not the reduced R106 scalar density.

For the high derivative energy, a separate wider normalized angular strip
\(1/16\), equivalently physical width \(1/64\), pays the complete coefficient
moments through order 11. At every retained Fourier mode the source takes
the minimum of two independently valid bounds: the complete directed DFT
coefficient enclosure, and the true analytic Cauchy coefficient bound.
Every omitted mode is then summed by the positive rational power-tail formula
proved in the preceding triangular-energy supplement. It never infers a
high derivative from a saved \(A_0,A_1,A_2\) error alone.

All native radial patches are restricted to their actual common scalar knot
span. The artificial R106 waist integration cut is merged into the same
analytic waist germ; no true scalar knot is crossed by that merge.

## 2. Global radial regularity and exact joining

The consumer independently rereads the exact origin and direction snapshots.
The base, raw phase, direction phase, shift and all three mean-radius splines
have degree five and interior knot multiplicity one. The four integrated
height-slope splines have degree six and interior multiplicity one. Thus the
former are globally \(C^4\), the latter globally \(C^5\), including all true
knots of \(I\). The coefficients are exact stored dyadics; this is a
multiplicity calculation, not a numerical endpoint comparison.

The infinite angular primitive therefore has globally \(C^4\) radial
regularity, with the paid angular derivatives. The synchronous curvature and
fixed-type coefficients have the \(C^2\), piecewise \(W^{3,\infty}\)
regularity required in R46 section 10. The full \(\mathcal F\) is continuous
and piecewise Lipschitz. Its first radial derivative is interpreted almost
everywhere. The actual WKB height and conormal are continuous across every
knot, so their residual contains no uncharged knot delta source.

For integer \(j\ge0\), use the actual constraint energy

\[
 e_j^2=\int\bigl(\lambda|\partial_\theta^j u|^2
       +\gamma|\partial_\theta^{j+1}u|^2
       +\alpha|\partial_\theta^jp|^2\bigr),\qquad\lambda=-K_0>0.
                                                               \tag{S.3}
\]

The preceding triangular-energy supplement gives the exact top matrix
\(H_j=H_0+2j\,\operatorname{diag}(0,[-v_\theta,\nu_\theta;
\nu_\theta,-v_\theta])\). Its diagonal scalar comparison is

\[
 C^{\pm}_{jj}=\max(0,g_\pm/2+j\chi_\pm).
\]

Every lower derivative uses the complete Frobenius coefficient matrix of that
supplement, so only first characteristic derivatives enter the exponential
diagonal. For cell \(i\), set \(M_i^\pm=\exp(L_i C_i^\pm)\), with all entries
bounded outwards. Every such matrix is entrywise at least the identity.

On the positive half, in chronological order,

\[
 P=M_{n-1}^+\cdots M_0^+,\qquad
 B=M_0^-\cdots M_{n-1}^-.
\]

The exact radial reflection exchanges forward and backward orientation and
preserves (S.3). Hence \(PB\) bounds the whole interval in both directions.
It also bounds every subinterval: removing factors that are entrywise at
least the identity can only decrease an entrywise nonnegative product.
No commutativity is required in this observation.

Let \(W_k=\operatorname{diag}_{0\le j\le k}\sqrt{\binom kj}\), and take the
minimum and maximum energy weights over the entire cover:

\[
 h_- =\inf\min(\lambda,\gamma,\alpha)>0,
 \qquad h_+=\sup\max(\lambda,\gamma,\alpha).
\]

The full Cauchy bound on the half-integer level is

\[
 E_{k+1/2}=\sqrt{h_+/h_-}\,
       \|W_k(PB)_{\le k}W_k^{-1}\|_2,
 \quad k=0,\ldots,10.                                      \tag{S.4}
\]

The source computes a directed operator-norm bound for these finite positive
comparison matrices. This matrix is a proof device for the full PDE, not a
Galerkin approximation. Only one endpoint norm comparison appears in (S.4).
Green-flux duality pays negative levels, and Hilbert interpolation pays the
whole interval \([-10.5,10.5]\). Set \(E=\max_k E_{k+1/2}\).
Duhamel then gives the complete ordinary source
\(L^1_rH^{s-1/2}\to\mathcal P_s\) with gain at most \(E\), including the mean.

## 3. The true all-time relative characteristics

The consumer reads the completed R106 all-time ray refinement, containing all
550 actual time segments. Its label has period \(2\pi\); the initial
physical angle is label divided by four. Let the report's complete analytic
bounds be

\[
 |\Theta_\eta|\le J,\quad\Re\Theta_\eta\ge j_*>0,
 \quad|\Theta_{\eta\eta}|\le J_2,
 \quad |\Im\eta|\le S_0=1/1024.
\]

The true relative physical map between any two radial times is
\(\Theta_{r_1}\circ\Theta_{r_0}^{-1}\). The initial factor four cancels in
its derivative; it is not omitted from a map between different periods.
The positive real derivative gives a complex inverse image strip by the
same vertical integration and univalence argument used in the root chart.
Consequently both relative maps and inverses are analytic on the full
physical strip

\[
 \delta_\theta=j_*S_0/4,
 \quad |H'|\le C_J=J/j_*,\quad H'\ge C_J^{-1}
 \text{ on the real circle}.                               \tag{S.5}
\]

All intermediate characteristic images lie in the ray report's paid image
strip, which is checked to lie strictly inside the WKB field strip. The other
characteristic branch is its exact angular reflection. No mean flow is
substituted for either actual branch.

For the inverse relative label \(S\), the chain rule gives

\[
 |\partial_\theta\log S_\theta|\le2J_2/j_*^2.                \tag{S.6}
\]

The full phase of R46 satisfies \(D_\sigma h_\sigma=g_\sigma\), where

\[
 g_\sigma=\frac{\mathcal F}{2\mu S_{\sigma,\theta}}.
\]

Writing \(M_{F,i},\mu_{-,i}\) for the complete field bounds on positive
cell \(i\), a uniform complete modulus for both \(h_\sigma\) and their
input-angle versions is

\[
 H=C_J\sum_i L_i M_{F,i}/\mu_{-,i}.                          \tag{S.7}
\]

The factor two from the reflected radial half cancels the phase's factor
one half. The same bound covers every shorter interval. It holds on the
full strip (S.5), since its proof integrates along the actual complex
characteristics, including their Jacobians.

## 4. The reduced ordinary residual is paid before composition

The exact cancellation in the preceding supplement is

\[
 P(mh_\sigma)=m\,[\mathcal Fh_\sigma
         +aD_\sigma g_\sigma
         +2\sigma\mu\partial_\theta g_\sigma+B_rg_\sigma].  \tag{S.8}
\]

No \(h_{\theta\theta}\) estimate is required. On a cell write
\(V_\sigma=|v|+|\nu|\),
\(V_{\sigma,\theta}=|v_\theta|+|\nu_\theta|\). The full complete moduli give

\[
 \begin{split}
 G_i&=C_JM_{F,i}/(2\mu_{-,i}),\\
 D_i&=\frac{C_J}{2\mu_{-,i}}\{
   M_{F_r,i}+V_\sigma M_{F_\theta,i}
   +M_{F,i}(M_{L_r,i}+V_\sigma M_{L_\theta,i}
                          +V_{\sigma,\theta})\},\\
 T_i&=\frac{C_J}{2\mu_{-,i}}
       \{M_{F_\theta,i}+M_{F,i}(M_{L_\theta,i}+2J_2/j_*^2)\},\\
 P_i&=M_{m,i}\,[M_{F,i}H+M_{a,i}D_i
                         +2M_{\mu,i}T_i+M_{B_r,i}G_i].
 \end{split}                                                  \tag{S.9}
\]

The derivative of \(1/S_\theta\) along a characteristic uses the exact
\(D_\sigma S_\theta=-v_{\sigma,\theta}S_\theta\). This explains the final
term in the second line. All quantities concern the full actual operator.
Then \(\int_I|P(mh_\sigma)|\le 2\sum_iL_iP_i\), on the complete strip
(S.5), for each of the four amplitude/frequency branch choices.

## 5. Full multiplication, composition, cross-cone and mean constants

For a scalar field of modulus \(M\) on a full physical strip of width \(a\),
put \(n=\lceil p\rceil\) and use the complete physical \(4\mathbb Z\) bound

\[
 \mathcal A_p(M,a)=
 4^p M n!\left[\frac{2}{(1-e^{-4a})^{n+1}}-1\right],
 \quad
 \mathcal M_p(M,a)=2^{p/2}\mathcal A_p(M,a).                 \tag{S.10}
\]

It includes the mean. The elementary inequality
\(\langle4k\rangle^p\le4^p(k+1)^n\le4^pn!\binom{k+n}{n}\)
proves this expression. The same bound applies to an integrated modulus by
Tonelli; a common error is not interpreted as independent uncontrolled modes.

The complete composition constants use the Bell-polynomial recurrence from
R46. Analyticity of both maps in (S.5), with a half-strip reserve, pays

\[
 \|H^{(j)}\|_\infty\le (j-1)!C_J/(\delta_\theta/2)^{j-1}.
\]

Their real derivatives are bounded below by \(C_J^{-1}\). The Bell recurrence
pays positive integer levels 0 through 11. Negative levels use the exact
adjoint composition and its true inverse-Jacobian multiplier; interpolation
pays all intermediate real indices. Let \(N_{\rm src}\) bound composition on
\([-6.5,9.5]\), and \(N_{\rm ord}\) on \([-5.5,10.5]\).

For the cross-frequency terms, the consumer constructs the complete Taylor
majorant of
\(1/(tH'+1-t)\), uniformly for \(0\le t\le1\). Its denominator is at least
\(C_J^{-1}\). The exact recursion
\(v_{r+1}=-\partial_\theta[v_r/(tH'+1-t)]\) is performed 24 times, with
starting amplitudes one and \(h_\sigma\). The latter's derivatives use (S.7)
and the same reserved strip. R46's Schur formula then gives

\[
 X_1=2^{20}B_{24}(1)(1+1/4),\quad
 X_h=2^{21}B_{24}(h)(1+1/3),\quad
 X=2^{1/4}X_1+2^{3/4}X_h.                                  \tag{S.11}
\]

The exponents follow from the exact maximal shifted indices \(8.5\) and
\(9.5\); 24 is greater than the required Schur summation thresholds.
All bad-sign outputs, including output zero, are included. Mean input has its
separate full Cauchy estimate below; no nonzero-mode proof is applied to it.

## 6. The exact full frame and the complete R46 budget

The frame is exactly R46's

\[
 \mathscr F(z_+,z_-)=2^{-1/2}
 \binom{m\Lambda^{-1/2}(z_++z_-)}
 {-T m\Lambda^{-1/2}(z_++z_-)
        +i\sqrt\mu\Lambda^{1/2}(z_+-z_-)}.
\]

The source pays all its multiplier bounds and its exact inverse uniformly
through the required shifted index 10.5. Call the resulting constants
\(F_*,I_*\). In particular the real conormal shear \(T\) is kept; no
principal half-density substitution is made.

With \(M_m,M_\mu,M_T\) denoting the corresponding complete multiplier
bounds, sufficient constants are

\[
 u=2^{1/4}M_m,\qquad
 F_*=[u^2+(M_Tu+M_\mu)^2]^{1/2},
 \qquad
 I_*=[M_\mu^2+\sqrt2M_m^2(1+M_T^2)]^{1/2}.                 \tag{S.12}
\]

The actual initial momentum defect is bounded by

\[
 d_*=2^{3/4}\mathcal M_{9.5}
      \left(M_mM_FM_a/(2\mu_-),1/640\right)
\]

at the reflected true initial endpoint. The complete ordinary residual budget
is

\[
 \begin{aligned}
 Q_*&=4\,2^{1/4}N_{\rm src}
       \mathcal M_{9.5}\left(2\sum_iL_iP_i,\delta_\theta\right).
 \\
 a_*&=I_*E(d_*+Q_*+F_*)+1.
 \end{aligned}                                             \tag{S.13}
\]

The factor four counts all amplitude/frequency branch choices. The \(F_*\)
and final one pay the actual infinite outputs from the two mean input columns.
The initial defect and residual are ordinary sources exactly as in R46;
no weak divergence load has been relabeled as an ordinary source.

At the final endpoint, the remaining momentum term and ordering fee satisfy

\[
 L_*=2\mathcal M_{9.5}
      \left(C_JM_FM_a/(2\mu_-^2),\delta_\theta\right)N_{\rm src},
 \qquad K_*=2^6\mathcal A_{11}(H,\delta_\theta).
\]

Therefore the complete computable strong bound is

\[
 \boxed{R_*^{\rm strict}=a_*+
    4\,[2X+L_*+2^{1/4}N_{\rm ord}K_*].}                    \tag{S.14}
\]

This is precisely R46 (6.8) with the whole actual supplied inputs. In
particular it is a full operator estimate, derived from composition and
Schur bounds, rather than a bound inferred from finitely many WKB columns.
The full ordinary physical source in amplitude coordinates has gain
\(I_*E\) from \(L^1_rH^{s-1/2}\) to \(E_s\).

## 7. Reproducibility and remaining interfaces

The native producer is `scripts/fourfold_strict_actual_wkb_fields.py`; the
consumer is `scripts/fourfold_strict_complete_R46_budget.py`.
Their completed reports are

- `notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz`;
- `notes/2026-11-13-R46-complete-actual-strict-operator.json`.

The exact all-time flow input is
`notes/2026-11-13-R106-integrated-source-ray-refinement.json`.
The final native report has SHA256

    8a97d6780955b94f3f96ab7cd8c8d4e518f291cd04e0903505c03e2abe176788

and the full strict-operator report has SHA256

    770fbb61134db79eb3ecb48710b5d65f72e1ff79b2eb3fc1015609a5da040b42

The native calculation took 4503.07 seconds; all 215 accepted cells and all
original scalar spans were covered, with an empty failure list. Its gzip
report contains the final field bounds needed by the consumer, rather than
large primitive or FFT intermediates. The full consumer took 7.38 seconds.
It retained the two half-interval comparison products, their whole-interval
product, every half-integer energy bound, every source row, and all remaining
frame/composition budgets. Selected complete values are:

| Quantity | Complete bound |
|---|---:|
| \(C_J\) | \(<36.730914\) |
| True relative-flow physical strip | \(6.98821875\,10^{-6}\) |
| \(H\), uniform complete strict phase modulus | \(<2078931.088\) |
| \(\int_I |P(mh)|\) on the full strip | \(<1.136648\,10^{13}\) |
| \(F_*\) and \(I_*\) | \(<4.914392\,10^{88}\) |
| \(E\) on \([-10.5,10.5]\) | \(<1.139199\,10^{251}\) |
| Full strict \(E_s\to E_{s+2}\) remainder | \(<6.177244\,10^{502}\) |
| Full physical ordinary-source gain | \(<5.598468\,10^{339}\) |

The scalar phase bound is the modulus needed in this complete WKB consumer.
It does not replace the more accurate signed finite-part phase calculations;
it contains the unregularized strict endpoint contribution.

Run from the topic directory, with fresh output paths if the files exist:

~~~bash
python3 scripts/fourfold_strict_actual_wkb_fields.py \
  --max-depth 12 \
  --out notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz
python3 scripts/fourfold_strict_complete_R46_budget.py \
  --out notes/2026-11-13-R46-complete-actual-strict-operator.json
~~~

The consumer checks every exact adjacent radial endpoint, the full final cut,
all whole-domain flags, source and dependency hashes, actual object identity,
the ray's whole 550-segment interval and its actual image strip. A partial
native checkpoint cannot produce (S.1).

This result covers only the displayed closed strict interval. The physical
cuts are not silently identified with a constant-\(\xi\) section of either
negative canonical root chart. The actual graph/trace gluing, both root
connections, positive Ai/contact network, returned \(b-\beta\), complete
returned \(R_*\), and final finite Schur block must be paid separately.
The potentially large complete constants are recorded as such and are not
advertised as a practical high-frequency cutoff or nonlinear completion.
