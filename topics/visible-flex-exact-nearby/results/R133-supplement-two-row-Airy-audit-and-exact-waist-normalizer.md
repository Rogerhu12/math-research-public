# R133 supplement: the two-row Airy audit and exact waist normalizer

2026-11-14, visible-exact-astra-0df / phase_inverse.

This proves three facts needed to attach the current strict first
symbol to the actual root. The free Airy model agrees with that symbol
after **both curvature rows** are transformed. The current waist
order-minus-one cross normalizer is exactly zero, by the actual
intrinsic spline construction. At the current nonradial root the cross
normalizer also has a finite symmetric off-diagonal term; it is not a
series of half-odd powers alone.

The Airy calculation is an exact model audit, and the waist statement
applies to the current object. The current moving-to-physical residual
bridge, full root reflection and positive regular graph are not proved
by replacing them with this model. In particular this note does not
identify the current finite-part integral with the complete returned
coefficient.

## 1. Both rows of the free model

Let \(\rho=r_*-r>0\), \(q=\sqrt\rho\), \(\eta=1\), and
\(b=d=0\). For one positive physical frequency \(k=4j\), the two
original curvature rows are

\[
 (h_1)_r=ik\rho h_2,\qquad (h_2)_r=ik h_1.
 \tag{A.1}
\]

Putting \(f=h_2\) gives, exactly,

\[
 f_{\rho\rho}+k^2\rho f=0,\qquad
 h_1=\frac{i}{k}f_\rho,\qquad
 w_\pm=\frac{ik^{-1}f_\rho\pm\sqrt\rho f}
                         {\sqrt{2\sqrt\rho}}.
 \tag{A.2}
\]

All remainders below are two-row remainders at a fixed strict cut
\(\rho=H>0\). Their existence and differentiability follow from
the complete two-row Airy expansion used in
[the full radial root calculation](R119-supplement-actual-complete-radial-return-first-phase.md),
§3. No coefficient-dependent constant from that other object is used.
With

\[
 \vartheta=\frac23k\rho^{3/2}+\frac\pi4,
 \qquad t=\frac1{k\rho^{3/2}},
 \tag{A.3}
\]

the outgoing complex height column is, up to a constant multiplier,

\[
 f_+=\rho^{-1/4}e^{i\vartheta}
             \left(1-\frac{5i}{48}t+O_H(k^{-2})\right).
 \tag{A.4}
\]

This is the usual \(\mathrm{Bi}+i\mathrm{Ai}\) column, with its
complete derivative row. Differentiating its prefactor contributes
\(-f_+/(4\rho)\). Substitution into **both** rows of (A.2) gives

\[
 \begin{pmatrix}w_+\\w_-\end{pmatrix}
 =\sqrt2 e^{i\vartheta}
 \left\{
 \begin{pmatrix}-it/8\\-1-it/48\end{pmatrix}
                     +O_H(k^{-2})\right\}.
 \tag{A.5}
\]

The constant multiplier suppressed in (A.4) is also suppressed in
(A.5). For the opposite height column, retaining the same
\(h_1=ik^{-1}f_\rho\), the corresponding vector is

\[
 \sqrt2 e^{-i\vartheta}
 \left\{\begin{pmatrix}1-it/48\\-it/8\end{pmatrix}
                     +O_H(k^{-2})\right\}.
 \tag{A.6}
\]

Thus the height coefficient \(-5/48\) alone is not the coefficient
in the curvature wave row. The shear contributes \(+1/8\) in the
dominant outgoing row, leaving \(+1/48\).

Here the strict formulas give

\[
 B=\frac1{4\rho},\quad
 S=\begin{pmatrix}0&-1/(8\rho^{3/2})\\
                       1/(8\rho^{3/2})&0\end{pmatrix},\quad
 T=\mathrm{Id}+\frac{S}{ik}.
 \tag{A.7}
\]

Applying \(T^{-1}\) to (A.5)--(A.6) removes their order-minus-one
cross columns. The remaining diagonal phases are
\(\vartheta+t/48\) and its negative. In the outgoing branch

\[
 a_-=-\frac1{32\rho^{5/2}},\qquad
 \frac{a_-}{ik}=\frac{i}{32k\rho^{5/2}}
       =\partial_r\!\left(\frac{i}{48k\rho^{3/2}}\right).
 \tag{A.8}
\]

This is precisely the first coefficient of the complete strict
symbol, including its sign. The signed difference and its finite part
from a cut \(H\) to the root are

\[
 \Xi=\frac1{16\rho^{5/2}},\qquad
 \operatorname{FP}\int_0^{r_*-0}\Xi\,dr
                         =-\frac1{24H^{3/2}},
 \tag{A.9}
\]

where the left endpoint in (A.9) means \(\rho=H\). No additional
root constant occurs in this model. The two-row transformation, not
an unexplained change of finite-part convention, reconciles (A.9)
with the height expansion.

## 2. A nonzero waist normalizer would change the answer

The same model with a raw waist condition \(h_1(H)=0\) has
\(w_++w_-=0\). If \(w=Tz\), its complete first row is

\[
 (1-it/8)z_+ +(1+it/8)z_-=O_H(k^{-2})z.
 \tag{A.10}
\]

Consequently the normalized waist reflection contains

\[
 z_+=-\exp(it/4)z_-+O_H(k^{-2})z_-.
 \tag{A.11}
\]

Dropping this endpoint factor would give the wrong returned phase.
For the real decaying Airy column one obtains directly

\[
 f_\rho=\text{amplitude}\,
       \left[\cos\vartheta-\frac7{48}t\sin\vartheta
                                      +O_H(k^{-2})\right].
 \tag{A.12}
\]

Combining the two strict branch phases \(t/24\) with the waist
factor \(t/4\) in (A.11) yields \(7t/24\), the doubled phase of
(A.12). Thus both possible endpoint mistakes are detectable in this
single exact model.

There is also a useful exact identity beyond this free example.
For any radial local two-row system

\[
 h_{1,r}=ik\eta q^2h_2+L_1h_1,\qquad
 h_{2,r}=ik\eta h_1+L_2h_2,
 \tag{A.13}
\]

put \(a=\eta q\), \(p=\eta'/\eta+L_1+L_2\), and

\[
 \begin{split}
 V&=(\eta'/\eta+L_1)L_2-L_2'+p'/2-p^2/4,\\
 W&=V/a^2+3(a')^2/(4a^4)-a''/(2a^3),\\
 B&=-q'/(2q)+(L_1-L_2)/2.
 \end{split}
 \tag{A.14}
\]

Eliminating \(h_1\), then using the exact Liouville coordinate
\(ds=a\,dr\) and its half-power amplitude, gives
\(z_{ss}+(k^2+W)z=0\). Direct differentiation proves

\[
 \boxed{\quad
 \frac{B^2}{a}=\partial_r(B/a)-Wa.
 \quad}
 \tag{A.15}
\]

The endpoint \(B/a\) is therefore the exact difference between
the two strict first-density conventions. At an analytic simple
root in this radial model, \(B/a\) has only half-odd powers and
no constant term. At an ordinary endpoint its actual value remains.
Formula (A.15) is a radial identity; it does not omit the current
nonradial primitive or declare the current equation radial.

## 3. The actual current waist has exactly zero cross normalizer

The current intrinsic target is the exact symmetric affine object

```
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848
```

Its original spline input is
`data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz`,
SHA256

```
0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b
```

The exact original arrays have degree five for `base`, `shift`,
`mean0`, `mean1`, `mean2` and all four height-slope splines. Zero
is a simple interior knot in these arrays. The phase spline also
has degree five, and zero lies strictly between its knots
\(-0.0022629790359221533\) and \(+0.0022629790359221533\).
These decimal strings identify saved binary data, not rounded
replacement knots.

A degree-five B-spline with a simple interior knot is \(C^4\)
there. Thus the radius construction is at least \(C^4\) at zero.
The actual `BulkTarget.scalars` implementation forms every radius
contribution as \((f(r)+f(-r))/2\), every height contribution as
\((g(r)-g(-r))/2\), and the two angular phases with respectively
even and odd radial symmetry. The affine update changes coefficients
before these operations and preserves their exact symmetry.
The complete, untruncated angular primitive consequently has its
first two spatial components even in \(r\), and its third component
odd. The mean radial energy \(E=\langle|F_r|^2\rangle\) is even
and differentiable. It follows exactly that

\[
 a'(0)=a'''(0)=E'(0)=0.
 \tag{A.16}
\]

The relevant source identities are fixed by the following SHA256s:

| Source | SHA256 |
|---|---|
| `fourfold_phase_beta_bulk_interval.py` | `4b9d6bf8d4b0d0c962eb32df9051b3b58fa1e25d7612e2bcef259572a9b15a76` |
| `fourfold_phase_beta_interval.py` | `ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f` |
| `fourfold_phase_beta_affine.py` | `b82724a2af026b9b9ee935f3df0eb95e7feb36ac5f65db9694085b5a4ad25991` |

The compact metric parameter is identically zero as a perturbation
on a neighborhood of the waist. Using the exact intrinsic identity

\[
 K=-\frac{a''}{aE}+\frac{a'E'}{2aE^2}
 \tag{A.17}
\]

and the proved positive denominators, (A.16) gives
\(K'(0)=0\), hence \(q_r(0)=0\). Since \(b=a'/a\), the
**complete current**, potentially nonradial, coefficient satisfies

\[
 B_\sigma(0,\phi)
 =-q_r(0)/(2q(0))-b(0)(1+r_\sigma(0,\phi)^2)=0,
 \qquad S(0,\phi)=0.
 \tag{A.18}
\]

This conclusion is independent of the angular size of the centre
and holds for every explicit response member whose intrinsic target
has the same compact parameter support. It is not inferred from
a floating value numerically close to zero. The first primitive,
the common radial gauge and the common half-density multiplier do
not change the raw condition \(h_1(0,\phi)=0\). Therefore the
order-minus-one cross transformation introduces no additional waist
phase in the current problem. Higher-order endpoint maps and the
independent mean rows remain in the strong remainder and head.

## 4. The current root also has a finite symmetric cross term

The actual nonradial first-symbol formula must be decomposed before
making a Puiseux assertion. Define

\[
 B_0=-q_r/(2q)-b(1+u^2+q^2v^2),\qquad
 B_\pm=B_0\mp2bq uv.
 \tag{A.19}
\]

Its full normalizer is exactly

\[
 S=\frac{B_0}{2\eta q}
       \begin{pmatrix}0&-1\\1&0\end{pmatrix}
   +\frac{buv}{\eta}
       \begin{pmatrix}0&1\\1&0\end{pmatrix}.
 \tag{A.20}
\]

On the true current analytic root piece, \(q=\sqrt\rho\sqrt{k(\rho)}\).
The first term of (A.20) has half-odd powers beginning with
\(\rho^{-3/2}\); the second has ordinary integer powers and in
general has the nonzero constant
\((buv/\eta)|_{r_*}\). Thus claiming that the **entire** matrix
has no \(\rho^0\) term would be false.

In the current reflection class \(u\) is angular odd and \(v\)
is angular even, while \(b,\eta\) are radial. The angular mean
of that finite coefficient is therefore exactly zero. This gives
an exact scalar fact, not permission to erase the off-diagonal
operator in the two-row root matching. The complete nonmean matrix,
its coordinate change and both reflected columns have to be retained.

## 5. Scope of the executable audit

`scripts/fourfold_codazzi_Airy_first_symbol_boundary_identity.py`
checks the rational Airy coefficients, both wave columns, the waist
reflection, the general radial identity (A.15), the decomposition
(A.20), and the original spline degrees/knot multiplicities. It
records all fixed input hashes and preserves its complete output.
Its actual public execution, when available, is separate evidence;
this text does not invent an execution record.

The remaining current-root obligation is the complete moving
operator's regular two-row reduction, including its nonlocal and
mean columns and the residual-sensitive physical bridge if that
bridge is used. The same full positive regular graph must be
expressed in that corrected frame. Only this calculation can
identify the directed returned row and pay a quantitative strong
remainder. The free model and the exact vanishing waist term are
checks within that calculation, not substitutes for it.
