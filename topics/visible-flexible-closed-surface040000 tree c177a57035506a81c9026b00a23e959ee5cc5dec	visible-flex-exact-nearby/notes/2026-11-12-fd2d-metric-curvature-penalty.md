# Optional finite curvature merit for the raw three-field search

## Status

This helper supplies additional finite merit rows to select a branch.
It does not change the original Gauss--Codazzi equations, and it is not
a certificate for the actual ODE-defined immersion. A final result still
uses the original residual and the actual geometric posterior.

The recovered implementation is
scripts/fd2d_gc_curvature_penalty.py, Git blob
777179d3eeb6eefcaa86f86e36648505a6ac1893.
The recovered directional-check program is
scripts/fd2d-metric-curvature-penalty-check.py, Git blob
0360b84e4bb1cb666393f5c421206277f59a78d7.
The old local write/run request was interrupted by loss of the executor
before a process exit or check report was observed. Thus no implementation
pass is claimed here. A genuine run of the recovered checker must record
its new source identities and actual exit.

## 1. The finite merit

At each selected raw node and solver angular point, the independent
formal second-form matrix in the target orthonormal basis is
\[
 S=\begin{pmatrix}n&m\\m&l\end{pmatrix}.
\]
Changing the diagonal order to \((l,n)\) leaves its eigenvalues unchanged.
The reader's component order remains \((n,m,l)\).

For \(C>0\), nonnegative weight \(w\), and
\[
 d=\sqrt{(n-l)^2+4m^2},\qquad
 \lambda_\pm=\frac{n+l\pm d}{2},
\]
the two optional rows are
\[
 r_+=w\max(\lambda_+-C,0),\qquad
 r_-=w\max(-\lambda_--C,0).
\]
Only strictly active rows are returned. Their count may change from one
trial to the next. A zero weight returns no rows.

These rows concern formal sampled eigenvalues. If the raw field is
incompatible, its independent \(S\) is not automatically the actual
shape operator of the reconstructed map. The R124 actual two-jets and
the appropriate posterior remain responsible for actual curvature.
A useful search penalty is not an additional final acceptance condition.

## 2. Derivatives without division by n

Write \(b=+1\) for the upper row and \(b=-1\) for the negative-lower row.
On a strict active set with \(d>0\),
\[
 r_b=w\left(\frac{b(n+l)+d}{2}-C\right),
\]
so its gradient in \((n,m,l)\) is
\[
 \nabla r_b
 =w\left(\frac{b+(n-l)/d}{2},
          \frac{2m}{d},
          \frac{b-(n-l)/d}{2}\right).
\]
This follows by differentiating \(d^2=(n-l)^2+4m^2\).
No division by \(n\) is used. In particular an unbent arc with
\(l=m=n=0\) is inactive for every positive cap.

The condition \(d=0\) alone does not imply inactivity. For instance
\(n=l=10,m=0\) has a repeated eigenvalue above a cap smaller than 10.
At a strictly active repeated eigenvalue the largest-eigenvalue function
is not differentiable. The helper returns the specified symmetric
spectral subgradient
\[
 w(b/2,0,b/2)
\]
and flags the row as a repeated eigenvalue. It does not label this choice
an ordinary derivative.

To prove this is a valid subgradient, use the Rayleigh quotient:
\(\lambda_{\max}(S)=\sup_{\|v\|=1}v^TSv\).
At \(S=tI\), every unit vector is a maximizing vector. The average of
the two coordinate rank-one projectors is \(I/2\), which is in the
convex subdifferential. The same argument applied to \(-S\) gives
\(-I/2\) for \(-\lambda_{\min}(S)\). Multiplying by \(w\) yields the
displayed component gradient.

At a hinge equality the row is omitted, corresponding to the valid
zero subgradient of the positive-part function. A caller must evaluate
the actual merit on a trial rather than assume that a fixed active set
or a subgradient gives an exact global linear model.

## 3. Sparse columns for the actual raw representation

Let \(K\) be the angular order, \(q=3K+2\), and let the node state be
ordered as
\[
 [n_0,\ldots,n_{2K};m_2,\ldots,m_{2K};
   l_0,\ldots,l_{2K}].
\]
At angular sample \(i\), denote the even and odd basis rows by
\(E_i,O_i\). For an active row at radial node \(j\), with field gradient
\((g_n,g_m,g_l)\), the only node-state block is
\[
 [g_nE_i,\;g_mO_i,\;g_lE_i]
\]
in columns \(jq,\ldots,(j+1)q-1\).

The raw provider supplies the derivative of the complete exact lifting
with respect to all tail controls. Its array has axes
\[
 (\text{angle},\text{node},(n,m,l),\text{tail parameter}).
\]
Contracting this array with the same field gradient gives the tail
parameter columns. This includes every analytic lifting mode; it does
not substitute a Fourier projection of the tail.

When the raw node values are treated as independent variables, the
central curvature coefficients have no direct columns in the sampled
field penalty. They enter through the central boundary equations.
If a solver explicitly eliminates or projects these linear boundary
conditions, it must compose this Jacobian with that linear map.
Equivalently it may pass directions tangent to the imposed identities.
The helper does not silently alter the user's saved boundary values.

The physical coast parameter \(T\) changes the lifting at fixed stored
node coefficients. As in the raw provider, the implemented column uses
\[
 \frac{{\cal L}(T+\varepsilon)-{\cal L}(T-\varepsilon)}
      {2\varepsilon},\qquad
 \varepsilon=\min(10^{-6}(1+|T|),.2T,.2(T_{\max}-T)).
\]
This is explicitly a finite-difference column, not an analytic derivative
claim. The actual profile parameter is restored afterward. A caller that
already computed the same field derivative may pass it as field_T.
No redundant lifting evaluation is then required.

## 4. Optional finite convexity at fixed T

For each fixed \(T\), the full sampled fields are affine in the raw node
state and tail controls. The Rayleigh formula proves that
\(\lambda_{\max}\) and \(-\lambda_{\min}\) are convex functions of the
symmetric matrix. Taking their positive part above a fixed cap preserves
convexity. Squaring a nonnegative convex function also preserves convexity,
because \(t\mapsto t^2\) is convex and nondecreasing for \(t\ge0\).
Therefore the sum of squared penalty rows is a convex function of these
affine variables at fixed \(T\).

This observation does not make the original Gauss--Codazzi system convex,
nor does it prove an admissible branch exists. It explains why the
penalty can guide a finite branch search toward smaller formal curvature
without modifying the compatibility equations.

## 5. Interface and intended check

From the topic directory:

~~~
from fd2d_gc_curvature_penalty import curvature_penalty

extra = curvature_penalty(
    problem, vector, cap=C, weight=w, data=raw_data,
    jacobian=True, field_T=already_computed_field_T_or_None)
~~~

The return value contains the separate residual vector, CSC sparse
Jacobian, angle/node labels, branch signs, repeated-eigenvalue flags,
and scope/derivative metadata. It never appends rows to or replaces
the original residual automatically.

The recovered check can consume a real saved initializer:

~~~
python scripts/fd2d-metric-curvature-penalty-check.py \
  --arrays <actual-initializer.npz> \
  --out notes/2026-11-12-fd2d-metric-curvature-penalty-check-recovery01.json
~~~

Its radial mesh step must match the saved input (default .04); the
profile_kind and tail_kind are explicitly positive_clock and
positive_bernstein. It checks independent node-field, tail, \(T\), and
central-parameter directions before boundary composition; repeated
positive and negative scalar matrices; inactivity of the zero matrix;
and zero weight. It also evaluates the original raw residual before
and after the helper to check that the helper changed no equations or
field values.

These are implementation checks of a finite optional merit. Their
successful completion would not certify the input BVP, its seam, or
its actual surface curvature.
