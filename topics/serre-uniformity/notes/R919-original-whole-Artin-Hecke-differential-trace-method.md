# R919 — Original whole-Artin Hecke differential trace: execution method

This method consumes the completed R885 fibre at the original source value $z=0$. It adds only the evaluations of nine original derivatives $\delta P_i$, the resulting $A_0$-linear Euler row of length eight, and that row applied to the 272 already completed target normal coordinates. It uses the original curve, level $82$, $-3$ descent, coefficient embedding, and two finite projections. It does not evaluate the seven R905 connection numerators or perform any endpoint or non-$p$ calibration.

The exact identity used here is R915, *Original Hecke differential trace and Euler coefficient functional*, SHA256 `b8ea2f3b8b11b0923e9192122d40dbd46224a5e54e4047c534748e9fabf1dc92`. R919 is its first finite whole-fibre consumer, not a replacement of the R915 function-field theorem.

## 1. Actual inputs and their separate mathematical identities

The numerical place is
$$
 \ell=1000000753,\qquad
 \zeta=549966761,\quad s=99932770,\quad B=3197390.
$$
It is the already used auxiliary place of the original $p=41$ problem; it is not the $41$-adic period place.

The five original source groups are as follows.

| Group | Completed source | Data actually consumed |
|---|---|---|
| R885 | run $43848870181$, source `a22acdb019714f55bf182feb958425f8954da2ca` | Entire $A_0$ and rank-eight correspondence, original 146 and 2058 function values, saved $\theta_0^{-1},a_8^{-1},P'(U)^{-1}$, all 272 target normal coordinates and their full original equations |
| R827 | run $43734420663$, source `400edecfeab313d1858cdb72bf18f8452ab9566a` | Completed original $g,\Gamma$ reduction, the original place audit, original $K_0^{-1}$, and full polynomial operator identity |
| R882 | run $43839076365$, source `cb2385cca1fd2c336c7da0e3070bde77129e8e17` | True same-place $2058\times17$ coefficient matrix and its complete $2200\times17$ verification |
| R873 | run $43832703159$, source `2ee14751d7b2cb4403931886b587ca6f64138c73` | Exact original 2058-function DAG, coefficient unit-solve definition and canonical dual-$7$ transport |
| R807 | run $43707939269$, source `2c44d02595d57c22b5ea2c10defa93f63252061d` | Exact $\theta$ linear combination and the already completed $N_{692}=\theta\widehat E_6$ weight-four coordinates |

Each selected file is bound by its original plain filename, bytes, SHA256, producer manifest, source commit, mathematical core, and configuration. The R807 and R827 historical stages store their result in `configuration.result`, with no top-level `result`; that actual schema is checked explicitly. Newer stages retain both fields. No old stage is rewritten under the R919 tag.

The completed R827 producer ended at a later budget boundary; its selected complete operators remain actual certified stages of that original producer. No success certificate is invented for that whole run. Its configuration is obtained from the original completed W/g/h reduction stage and checked against the original metadata.

R807 and R827 can be transported through their completed, independently pinned small intake archives. The original bytes and mathematical source identities are unchanged. The R885, R882 and R873 small selected outputs are read by ZIP Range. No old large Fourier carrier, $2058$-square inverse, polynomial-adjugate computation or characteristic-polynomial interpolation is required.

## 2. Derive first in the original function field

Let
$$
 F=K(Y),\qquad \nu=\frac{dz}{g},\qquad \delta=\nu^{-1}d=g\partial_z.
$$
Here $\partial_z$ is the derivation of the original separable function field, with its actual normal-basis relation. It is not a derivative that holds the primitive element $w$ constant.

In the original normal basis $\beta_0,\ldots,\beta_{271}$, the already certified operator $\Gamma(z)$ gives the columns of $\delta\beta_i$. The 146 original weight-two function leaves are
$$
 e_0/\tau=1,\quad e_1/\tau=z-\beta_{72},\quad
 e_i/\tau=\beta_{i-1}\quad(2\leq i\leq145).
$$
Consequently their derivatives are
$$
 0,\quad g-\delta\beta_{72},\quad
 \delta\beta_1,\ldots,\delta\beta_{144}.                 \tag{919.1}
$$
The original $e_i=82^2T_{(1,i)}$ already have their scale. No further $82^2$, $82^6$ or $82^8$ factor is inserted.

At the completed source fibre,
$$
 A_0=\mathbf F_\ell[X]/(\chi_0(X)),\qquad \dim A_0=272,
$$
the saved $K_0^{-1}$ changes normal coordinates into the original $1,w,\ldots,w^{271}$ coordinates. R919 uses it once on the original values of $g$ and the needed $\Gamma(0)$ columns. The $\Gamma$ input is exactly 17 consecutive blocks of 16 rows, ending with rows $256,\ldots,271$; the original polynomial has five coefficient matrices per block. Evaluating at $z=0$ uses their constant matrices, without interpolating or solving for $\Gamma$.

This evaluates the functions in (919.1) after differentiation. In particular,
$$
 \delta z=g
$$
need not vanish in the fibre. R919 does **not** assert that $\delta$ descends to a derivation of $A_0$. It never differentiates an arbitrary reduced representative modulo $\chi_0$, nor replaces $\delta$ by formal differentiation in $X$.

## 3. Original clearing and all 2058 derivative values

Write
$$
 \theta_0=\theta/\tau,\qquad
 n=N_{692}/\tau^4,\qquad
 E=\widehat E_6/\tau^3=n/\theta_0 .
$$
The exact coefficients of $\theta_0$ in the original 146 leaves and of $n$ in the original weight-four monomials come from R807. Its complete common rational denominator is retained. The completed R885 $E$-value and whole-$A_0$ inverse of $\theta_0$ are reused. Thus
$$
 \delta E=\theta_0^{-1}(\delta n-E\,\delta\theta_0),
 \qquad
 \delta(E^2)=2E\,\delta E.                              \tag{919.2}
$$
There is no new inversion of $\theta_0$, no repeated clearing solve and no discarded zero factor.

For an original monomial $m_1\cdots m_r$, its derivative uses the full product rule, with prefixes and derivatives cached. No inverse of any $m_i$ is used. Zero-valued leaves therefore cause no special exception. The 2050 original $V_8/\tau^8$ basis monomials have eight factors. The eight added functions have the form
$$
 E^2\,m_a m_b.
$$
Their derivatives are
$$
 \delta(E^2)m_am_b+E^2\bigl(\delta m_a\,m_b+m_a\,\delta m_b\bigr). \tag{919.3}
$$
The old completed $E^2$-value is already the first added basis value, index $2050$, whose original $V_2$ recipe is $(0,0)$. It is read directly. The old 2058 completed function values are not reconstructed.

R919 saves the new derivatives in immutable blocks of 64 rows, including the final shorter block. Each block records its exact original recipe source, source leaf-derivative stage and original index interval. The completed index lists every row $0,\ldots,2057$ once.

The exact characteristic-zero coefficient columns are defined by the original R873 unit solve. They are constants for $\delta$. Their actual $\ell$-integral reductions are the completed R882 matrix $C$. Therefore
$$
 \bigl(\delta P_0,\ldots,\delta P_8\bigr)
  =\bigl(\delta f_0,\ldots,\delta f_{2057}\bigr)
       C_{\{0,\ldots,8\}}.                             \tag{919.4}
$$
Only these nine columns are newly evaluated. R919 neither reconstructs the 17 coefficients nor computes $\delta K$. The original R882 full $2200\times17$ source certificate remains the certificate for the input coefficient matrix.

## 4. Complete Euler row and its exact whole-algebra certificate

Put
$$
 P(U)=\sum_{i=0}^8P_iU^i,\qquad p(U)=P(U)/a_8,\quad a_8=P_8,
 \qquad E_0=A_0[U]/(p).
$$
The original $a_8$ is a unit on the **entire** source algebra, and $P'(U)$ is a unit on the **entire** rank-eight algebra; R885 has already computed and certified both inverses. R919 reads them unchanged.

For $h\in E_0$, R915 gives
$$
 \mathcal L(h)
   =-a_8^{-1}[U^7]\bigl(h\,\delta P\bmod p\bigr).       \tag{919.5}
$$
For a general coefficient $h\in E_0$, its input differential is $h\,dU$, and its output frame is $\nu_s$:
$$
 \operatorname{Tr}_{\pi_s}(h\,dU)
      =\mathcal L(h)\nu_s.                             \tag{919.6}
$$
Only when $h=\pi_t^*A$ is this written as $\operatorname{Tr}_{\pi_s}\pi_t^*(A\,dz_t)$. The target $g_t$ is not inverted in this convention. A future input given as $h\nu_t$ must supply the true $h/g_t$; R919 does not silently convert that frame.

The row
$$
 \bigl(\mathcal L(1),\mathcal L(U),\ldots,\mathcal L(U^7)\bigr)
       \in A_0^{\,8}                                  \tag{919.7}
$$
is computed by monic reduction of the nine $\delta P_i$ and seven successive multiplications by $U$. Each entry retains all 272 source coordinates.

The monic Euler identity holds over any commutative base ring:
$$
 \operatorname{Tr}_{E_0/A_0}(x)=[U^7]\bigl(p'(U)x\bmod p\bigr).
$$
Since $p'=P'/a_8$, it gives
$$
 \mathcal L(h)
  =-\operatorname{Tr}_{E_0/A_0}\bigl(h\,\delta P/P'(U)\bigr). \tag{919.8}
$$
R919 certifies (919.8) on all eight $A_0$-basis elements. For each one it builds the eight diagonal entries of the genuine multiplication operator on $1,U,\ldots,U^7$, sums them in $A_0$, and compares all 272 coordinates with (919.7). The previously completed $P'$-inverse is only read and multiplied; it is not solved again. Intermediate basis certificates carry the next multiplication input, so an interruption need not redo the preceding completed basis case.

This is the full $A_0$-linear map certificate. It is not a check at scalar roots, at one reduced point, or on a semisimple quotient. No factor, repeated factor or nilpotent direction is removed.

## 5. Direct application to the completed target normal basis

R885 already supplies every target value
$$
 \beta_i^{(t)}\in E_0,\qquad 0\leq i<272,
$$
in 17 consecutive blocks. Its actual complete certificate checked all 272 target normal equations in all 2176 scalar coordinates, with $\beta_0^{(t)}=1$.

R919 reads those values, writes
$$
 \beta_i^{(t)}=\sum_{k=0}^7b_{ik}U^k,\qquad b_{ik}\in A_0,
$$
and evaluates
$$
 \mathcal L(\beta_i^{(t)})=\sum_{k=0}^7b_{ik}\mathcal L(U^k). \tag{919.9}
$$
The output consists of 272 rows of length 272, in the original normal order, with both differential frames written explicitly. There is no repeated adjugate, target normalization, target equation solve, characteristic-polynomial interpolation or new Krylov inverse.

This table is the ready finite input for a later trace of a connection numerator expanded in that target normal basis. R919 deliberately does not expand or evaluate the seven R905 $A_D$ numerators; the previous 543-row solves and principal-part maps remain untouched.

## 6. Exact expression and actual numerical boundary

The new exact expression DAG contains:

1. The original R873 2058-function recipes and exact coefficient unit-solve column references.
2. The original rational derivation $\delta=\nu^{-1}d$, applied before specialization.
3. Nine derivative nodes and the coefficient functional (919.5).
4. The original $\pi_s,\pi_t$ orientation, canonical dual-$7$ involution, scalar-$7$ diamond, original $-3$ descent, true $c_Y$, and both rigidified determinant frames.

It defines characteristic-zero rational expressions. It does not claim that characteristic-zero $\Gamma$, derivative coordinates or the Hecke trace matrix have been numerically expanded. The actual new arrays are only the stated, source-certified $\ell$-specialization.

In particular the direct direction in (919.6) is not silently substituted for the frozen target norm direction. The original canonical dual-$7$ transport from R873/R915 must be used, with its actual differential pullback and both frames. R919 does not evaluate the $\kappa/\nu$ endpoint factors or claim a completed calibrated Hecke correspondence.

The final certificate keeps false the claims of an original active Hecke projector, endpoint calibration, non-$p$ terms, Poincaré period, and height. Auxiliary values do not substitute for an original $41$-adic ball.

## 7. Immutable stages, continuation and public execution

The new core is `R919_original_whole_Artin_Hecke_differential_trace.py`. It imports only the hash-bound completed helper `R885_whole_Artin_algebra.py`; it does not instantiate the old R885 Job or run old producers. The independent R919 wrapper is the actual driver and is recorded as such.

All new mathematics is guarded by the public repository Actions environment. Local work is limited to source IO, hashes, schema reading and AST parsing.

The stage sequence is:

| New stage family | Saved object |
|---|---|
| source audit | Five original identities, selected bytes, actual fibre and frame |
| original leaf derivatives | 146 derivatives, $\delta z,\delta\theta_0,\delta n,\delta E,\delta(E^2)$ |
| basis derivative blocks/index | All 2058 rows in original order |
| nine original $\delta P$ coefficients | $9\times272$ array |
| complete Euler row | $8\times272$ row and eight complete remainders |
| eight basis identities | Full multiplication traces and coordinate equalities |
| target differential blocks/index | All $272\times272$ values |
| exact expression DAG | Source-bound characteristic-zero operations and retained transport |

Every complete stage is atomic, immutable and bound to the new core, helper, method, proofs, source identities, exact selected file maps and inputs. Budget is excluded from the mathematical tag. A false endpoint is historical; it does not overwrite a newer complete stage inventory. The current pointer is explicitly incomplete and kept separate from the complete stage list.

The wrapper has the usual outer timeout of budget plus 900 seconds, then termination and a short grace period, leaving completed outputs for a one-day artifact. If no core receipt exists after an outer timeout, only an actual unsuccessful run with a null core-receipt SHA can use that boundary. It never manufactures a receipt or successful certificate.

Git contains source code, parameter requests, paper proof and concise run/SHA registration. Machine vectors, receipts, matrices and every saved arithmetic stage remain in the one-day active artifact and its minimal source carrier.

