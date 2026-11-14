# R133 supplement: complete nonlinear derivative bounds from the relative centre

This result concerns the actual rotational target on
\(I=[9/10,25/8]\), the full affine parameter interval, and all physical
Fourier modes in \(4\mathbb Z\). It supplies a strict derivative bound for
a nonzero-centred cap fixed-point map. It does **not** yet supply that
map's complete residual on this interval, a cap solution, periodic frame
holonomy, body matching, or the true nonlinear regular-tail relation.

The completed zero-centred attempt on the same interval remains false.
Only its successful, complete linear Green operator is consumed here.
The nonzero-centred estimate changes neither the correction norm nor
any source or boundary port.

## 1. The Banach space and the actual reference

Write the real orthonormal second form as

\[
 II=\begin{pmatrix}A&B\\ B&C_{\rm ref}+c\end{pmatrix},\qquad
 Q(B,c)=\frac{B^2+\ell c^2}{C_{\rm ref}+c},\qquad
 A=A_{\rm ref}-\ell c+Q(B,c).
 \tag{D.1}
\]

All coefficients are those of the true rotational metric. In particular,
\(C_{\rm ref}<0\) and \(\ell=A_{\rm ref}/C_{\rm ref}>0\). The
complete native coefficient cover gives uniform numbers

\[
 |C_{\rm ref}|\ge C_*>0,\qquad 0<\ell\le\Lambda,\qquad \Lambda\ge1.
 \tag{D.2}
\]

The scalar space and pair norm are

\[
 X_0=\ell^1\bigl(4\mathbb Z;C(I)\bigr),\qquad
 \|u\|_{X_0}=\sum_{m\in4\mathbb Z}\sup_{r\in I}|u_m(r)|,
 \qquad \|(B,c)\|_{X_0^2}=\|B\|_{X_0}+\|c\|_{X_0}.
 \tag{D.3}
\]

The order in (D.3) is essential: take a radial supremum separately for
each coefficient, then sum. All products below use the complete
convolution algebra inequality on this space. A scalar radial multiplier
has its actual uniform norm. The zero mode is included.

Let \((\widehat B,\widehat c)\) be the complete finite polynomial centre.
Its finite support is a property of the centre alone. Corrections are
arbitrary elements of the full space (D.3). Define

\[
 B_\diamond=\left\|\frac{\widehat B}{C_{\rm ref}}\right\|_{X_0},
 \qquad
 c_\diamond=\left\|\frac{\widehat c}{C_{\rm ref}}\right\|_{X_0}.
 \tag{D.4}
\]

The denominator in each coefficient of (D.4) is the same true radial
\(C_{\rm ref}(r)\). No angular projection, frozen denominator, or ratio
of unrelated global maxima is substituted for this function.

## 2. Full derivative bound in the original absolute correction norm

Suppose \(V=(V_B,V_c)\) satisfies \(\|V\|_{X_0^2}\le\rho\). Put

\[
 b=B_\diamond+\rho/C_*,\qquad
 z=c_\diamond+\rho/C_*,\qquad d=1-z.
 \tag{D.5}
\]

If \(d>0\), the Neumann inverse in the Banach algebra exists and

\[
 \left\|\left(1+\frac{\widehat c+V_c}{C_{\rm ref}}\right)^{-1}
 \right\|_{X_0}\le d^{-1}.
 \tag{D.6}
\]

Set \(x=B/C_{\rm ref}\) and \(y=c/C_{\rm ref}\). Direct
differentiation of (D.1), keeping \(C_{\rm ref},\ell\) fixed, gives

\[
 D_BQ=\frac{2x}{1+y},\qquad
 D_cQ=\frac{2\ell y}{1+y}-\frac{x^2+\ell y^2}{(1+y)^2}.
 \tag{D.7}
\]

These are multiplication operators on the full Fourier algebra. Hence
throughout the complete correction ball,

\[
 \|D_BQ\|\le L_B:=\frac{2b}{d},\qquad
 \|D_cQ\|\le L_c:=\frac{2\Lambda z}{d}
               +\frac{b^2+\Lambda z^2}{d^2}.
 \tag{D.8}
\]

Both derivative columns are paid. The pair norm in (D.3) gives

\[
 \|DQ[V]\|_{X_0}\le\max(L_B,L_c)\|V\|_{X_0^2}.
 \tag{D.9}
\]

The closed ball is convex, so integrating (D.9) along its line segments
gives the same Lipschitz bound for the full nonlinear difference. This
argument does not assume corrections have the centre's finite support.
It also gives the actual pointwise denominator bound

\[
 |C_{\rm ref}+\widehat c+V_c|\ge C_*d.
 \tag{D.10}
\]

Let \(K_G\) be the already certified operator norm of the complete
nonlinear source-to-pair Green map. The map includes the nonzero-mode
\(d=b+q_mc\) and \(c\) source terms and the forced mean equation.
The four independent ports remain

- the entire nonzero \(c(9/10)\) trace;
- the entire nonzero \(d(25/8)\) trace;
- \(B_0(25/8)\);
- \(c_0(25/8)\).

Thus the derivative bound for the fixed-point map is

\[
 L=K_G\max(L_B,L_c).
 \tag{D.11}
\]

If its separately verified full residual at the centre is \(\varepsilon\),
the ordinary sufficient closed-ball condition would be

\[
 L<1,\qquad \varepsilon<\rho(1-L).
 \tag{D.12}
\]

This supplement proves and evaluates the right-hand side of (D.12).
It does not assert the uncomputed residual inequality.

## 3. Complete interval producer and identities

The source is
`scripts/fourfold_codazzi_cap_relative_centre_budget.py`.
It checks the native coefficient and Green-consumer identities, their
declared dependency hashes, and agreement of the object, central affine
parameter, and affine half-width. The interval starts to the right of
the compact metric modification, whose support lies in \((.05,.18)\).
Consequently the same true rotational reference is used throughout
the requested cap; this makes no assertion about the modified body.

There are 949 selected true native boxes. They are intersected with
every exact binary centre polynomial join, giving 994 closed boxes.
For each of the complete 64 positive centre frequencies and their
negative partners, the producer encloses the exact finite polynomial
on each box, divides by the corresponding directed true
\(C_{\rm ref}\) interval, and updates that coefficient's separate
radial supremum. Only after the entire cover is complete are these
suprema summed. The report contains all four arrays for
\(\widehat B,\widehat c,\widehat B/C_{\rm ref},\widehat c/C_{\rm ref}\),
and the complete 994-box cover with original scalar germs.

The reference intervals retain the entire original primitive tail and
the true R74 regular linear-line fee. The latter is positive for the
non-fourth frequencies, however small its printed float is. The centre
has the exact stored binary amplitude corresponding to the diagnostic
number \(.65\), and the stored M64 compact parameter
\(\nu=-.023721707968258524\). No centre approximation is used to
replace the true target coefficients or their whole affine interval.

All directed scalar finishing arithmetic uses 320-bit Arb. The finite
coefficient Horner operations and ratios use the existing directed
`Box` arithmetic. These are continuous closed-box bounds, not angular
or radial sample maxima.

## 4. Actual completed bounds and the failed zero-centred attempt

The complete report gives the following conservative outward decimal
statements:

| Quantity | Strict bound |
| --- | ---: |
| \(K_G\) | \(<15.952407\) |
| \(\Lambda\) | \(<1.693662\) |
| \(C_*\) | \(>.1705338016\) |
| \(\|\widehat B\|_{X_0}\) | \(<.0043518120\) |
| \(\|\widehat c\|_{X_0}\) | \(<.0033681008\) |
| \(B_\diamond\) | \(<.0139840010\) |
| \(c_\diamond\) | \(<.0108230199\) |
| Absolute correction radius \(\rho\) | \(1/2000\) |
| Full \(B\) derivative column \(L_B\) | \(<.0343037903\) |
| Full \(c\) derivative column \(L_c\) | \(<.0478660278\) |
| Full fixed-point derivative \(L\) | \(<.763578348\) |
| Actual denominator throughout the ball | \(>.1681881109\) |
| Available complete-residual budget \(\rho(1-L)\) | \(>.0001182108262\) |

The full relative-centre derivative gate is true. The earlier
zero-centred consumer on these same 949 boxes, with its own radius
\(.006\), reported image bound \(.01786133294\) and Lipschitz bound
\(2.006439811\); that false result remains in its original report.
The successful rows used here are its complete linear Green rows,
whose strict rate gates are independent of that unsuccessful nonlinear
closed-ball estimate.

The new result does not remove any failure by deleting a mean, taking a
finite Fourier inverse for an infinite correction, or declaring the
true nonlinear regular condition homogeneous. It supplies a measured
residual target for the next complete nonzero-centred computation.

## 5. Reproduction and frozen input hashes

From the topic directory, using the already installed python-flint
runtime:

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_cap_relative_centre_budget.py \
  --out /tmp/R133-relative-centre-independent.json.gz
```

The source refuses to overwrite any existing attempt.

| File | SHA-256 |
| --- | --- |
| Relative-centre producer | `be77d36388b6eb84e710753480c280fee97f78a78524a1f9a4e7a0cc298a08d4` |
| `notes/2026-11-13-R133-r09-relative-centre-DQ-native.json.gz` | `608ef3d56265056d544c7504470181e7a0656dc03245585647e1f250e92a02c6` |
| `notes/2026-11-13-R133-A0-r09-linear-kernels-native.json.gz` | `d5364505098d55d84bae39f81d18ca81cf65a7a78fbcfc68f2797174b9f4ded3` |
| Actual rotational positive-cap v2 native | `3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22` |
| Complete M64 centre | `4046eb7ac8da162ab9aad9fcb4991933200abdbc2c22ed6329d49bb13d72b856` |
| Original exact affine object | `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848` |

The affine centre is
\(-7789843107295549/4611686018427387904\), and its complete half-width
is \(10^{-9}\). Every input and helper hash needed by these consumers
is retained in the reports and the companion manifest.
