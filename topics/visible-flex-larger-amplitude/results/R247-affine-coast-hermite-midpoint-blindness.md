# R247. Exact midpoint cancellation for an affine coast initial guess

## Status and purpose

This is an algebraic result about the original finite Frenet equation and
the cubic Hermite curve used in its collocation/RMS evaluation.  Its proof
is complete below.  It explains a structural difference between a
midpoint **domain** preflight and the two off-midpoint RMS queries.  It
does not prove that a particular candidate leaves the domain, that a
larger Fourier cutoff cures that failure, or that any coupled BVP has
been accepted.

The actual motivating computation is public Actions run `43585737152`
at source `085dcb540a6a2d6ba1f223db37b8df4f9c14d64e`; its input binding,
returned margins, and separate diagnostic probe are recorded in
[`2026-11-14-prefix-controls-RMS-domain-failure-and-circle-probe.md`](../notes/2026-11-14-prefix-controls-RMS-domain-failure-and-circle-probe.md).

## 1. Equation and precise hypotheses

Let `S` be the fixed linear synthesis map from a finite coefficient vector
to a physical curve in `R^3`, with parameter `phi`.  In the implementation
it includes the rotating `(e_r(phi),e_phi(phi),e_z)` basis.  Let `Pi` be
the fixed linear projection of a physical velocity, expressed in that
same basis, back to the coefficient vector.  It may be the actual
uniform-grid projection `Pi_(M,N)`; no exact continuous orthogonality is
needed for the result.  Its modes and quadrature are fixed throughout the
interval under discussion.

For a regular curve `F=S(y)`, use the original Frenet definitions

\[
\lambda=|F_\varphi|,\qquad
T=F_\varphi/\lambda,\qquad
W=F_{\varphi\varphi}-(F_{\varphi\varphi}\cdot T)T,
\]

\[
N=W/|W|,\qquad B=T\times N,\qquad
\kappa=|W|/\lambda^2,
\]

and

\[
\alpha=-\frac{a_s}{a\kappa},\qquad
\beta=+\sqrt{1-\alpha^2},\qquad
V=\alpha N+\beta B,\qquad y_s=\Pi V.
\tag{247.1}
\]

All quantities in (247.1) are required to be in their real regular domain:
`a>0`, `lambda>0`, `|W|>0`, and `1-alpha^2>0` wherever the equation is
evaluated.  For a grid equation these requirements are at all actual
quadrature nodes.  A continuous statement requires them for every
`phi`; a grid check alone is not substituted for that stronger condition.

On an interval `[s_i,s_i+h]`, `h>0`, suppose

\[
a(s)=a_i+b(s-s_i)>0,\qquad b\text{ is constant},
\]

and consider the **initial guess**

\[
y_*(s)=a(s)c+[Z_i+w(s-s_i)]e_0.
\tag{247.2}
\]

Here `c` is one fixed complete finite coefficient vector, `S(e_0)=e_z`
is a constant spatial translation, and `w` is constant.  In the circular
warm under consideration, `c` is the projection of the complete
material circle, its height coefficients vanish, and
`w=+sqrt(1-b^2)` with `|b|<1`.  The constant-velocity argument itself
allows any fixed shape `C=S(c)` with nonzero curvature and any constant
`w`.

The assertion that (247.2) is an initial guess is essential: it is not
assumed to satisfy (247.1).

## 2. Frenet scaling makes the evaluated RHS constant

**Proposition 247-A.** Under the hypotheses of section 1, the right-hand
side of (247.1), evaluated along (247.2), is a constant coefficient vector
`f` on the whole interval.  The derivative of the initial guess is the
constant vector `u=b c+w e_0`, and `f` need not equal `u`.

**Proof.** The translation in (247.2) has no angular derivatives.  Since
`a>0`,

\[
F_{*,\varphi}=aC_\varphi,\quad
F_{*,\varphi\varphi}=aC_{\varphi\varphi},\quad
\lambda_*=a\lambda_C.
\]

Consequently `T_*=T_C`, `W_*=aW_C`, `N_*=N_C`, `B_*=B_C`, and
`kappa_*=kappa_C/a`.  Thus

\[
\alpha_*=-b/\kappa_C,\qquad
\beta_*=+\sqrt{1-b^2/\kappa_C^2},
\]

which are independent of `s`.  The original velocity `V_*`, and therefore
its fixed projection `f=Pi V_*`, are independent of `s` as well.  Direct
differentiation of (247.2) gives `u=b c+w e_0`.  No equation used in this
calculation identifies these two vectors.  This proves the proposition.

In particular, for the projected planar material-circle seed the
admissibility condition reduces to `kappa_C>|b|` on the evaluation set.
This condition concerns the projected physical curve, whose curvature
need not be the curvature of the complete material circle.

## 3. Exact Hermite error and the RMS constants

Let `y_H` be the cubic Hermite curve which has the endpoint **values** of
`y_*` and the endpoint **derivatives supplied by the original ODE**:

\[
y_H(s_i)=y_*(s_i),\quad y_H(s_i+h)=y_*(s_i+h),\quad
(y_H)_s(s_i)=(y_H)_s(s_i+h)=f.
\]

**Proposition 247-B.** For every real `t` in `[0,1]`,

\[
\boxed{
y_H(s_i+th)=y_*(s_i+th)+h\,\psi(t)(f-u),\qquad
\psi(t)=t(1-t)(1-2t).
}
\tag{247.3}
\]

**Proof.** The four cubic Hermite basis functions are

\[
h_{00}=2t^3-3t^2+1,\quad h_{10}=t^3-2t^2+t,
\]

\[
h_{01}=-2t^3+3t^2,\quad h_{11}=t^3-t^2.
\]

Write `y_i=y_*(s_i)` and use `y_*(s_i+h)=y_i+hu`.  Substitution into the
Hermite formula gives

\[
y_H=y_i+h h_{01}u+h(h_{10}+h_{11})f.
\]

Now `h_{10}+h_{11}=psi` and `h_{01}-t=-psi`.  Subtracting
`y_*(s_i+th)=y_i+htu` proves (247.3).

At the midpoint, `psi(1/2)=0`.  Therefore the midpoint field is exactly
the initial-guess field, even when `f-u` is large.  At the RMS fractions

\[
t_\mp=\frac12\mp\frac12\sqrt{\frac37},
\]

one has `t_\mp(1-t_\mp)=1/7`, and hence

\[
\psi(t_-)=+\frac{\sqrt{3/7}}7,\qquad
\psi(t_+)=-\frac{\sqrt{3/7}}7.
\tag{247.4}
\]

Thus the two actual off-midpoint queries contain opposite copies of the
full derivative mismatch with magnitude `h sqrt(3/7)/7`.  This is an
exact algebraic cancellation and amplification pattern, not a numerical
roundoff argument.

If the nonmean height coefficients of the planar seed vanish, their
Hermite coefficients are exactly

\[
(y_H)_{z,m}=h\psi(t)f_{z,m},\qquad m\ge1.
\tag{247.5}
\]

For the implemented `cos(2m phi)` height basis, two angular derivatives
multiply (247.5) by `-(2m)^2`.  A small coefficient-level mismatch can
therefore have a much larger effect on the curvature entering the
Frenet domain.  Neither (247.3) nor (247.5) asserts that a particular
margin must become negative; that requires the actual coefficient data.

## 4. A domain preflight is different from a residual test

Since `y_H` equals `y_*` at the midpoint, the original RHS there is again
`f`.  The midpoint collocation defect is nevertheless

\[
y_*(s_i+h)-y_*(s_i)
-\frac h6(f+4f+f)=h(u-f).
\tag{247.6}
\]

It is generally nonzero.  The proposition concerns the inability of a
**midpoint-only domain check** to detect the off-midpoint displacement;
it does not claim that the collocation equation or its residual is blind
to the same derivative mismatch.  A preparation routine may legitimately
allow a large residual in an initial guess while requiring its evaluation
points to remain in the real equation's domain.  Such a routine must
check the actual RMS points separately if a subsequent RMS evaluation is
to be defined.

For a nonconstant `a_s`, the endpoint velocities need not be equal and
the simple constant-`f` formula is not applicable as stated.  The exact
general Hermite formula still applies; no coast cancellation is assumed
across turn or bridge intervals.

## 5. Complete material circle and finite projection limitations

Suppose a fixed material angle satisfies `Phi_phi=rho>0`.  The complete
physical material circle is

\[
C(\varphi)=(\cos\Phi(\varphi),\sin\Phi(\varphi),0).
\]

Its derivatives are

\[
C_\varphi=\rho e_\theta,\qquad
C_{\varphi\varphi}=\rho_\varphi e_\theta-\rho^2e_r.
\]

Thus `T=e_theta`, `N=-e_r`, `B=e_z`, and `kappa_C=1`.  For
`F_*=aC+Ze_z`, equation (247.1) gives exactly

\[
V_*=bC+\sqrt{1-b^2}\,e_z.
\tag{247.7}
\]

With the stated choice of `w`, this equals the physical derivative of
the complete-circle guess.  No angular mode has been discarded in this
argument.

By contrast, if `C_(M,N)` is synthesized from the finite rotating-frame
projection of `C`, it is a different physical curve.  In general

\[
\Pi_{M,N}V(C_{M,N})
\ne \Pi_{M,N}V(C),
\]

because the Frenet normal, curvature and square root are nonlinear.  A
finite core `c` does not make `cos(Phi_c-phi)` and `sin(Phi_c-phi)` finite
Fourier polynomials.  Therefore (247.7) cannot be transferred to the
finite projected field by dropping the analytic high-mode remainder.

This result also does not authorize replacing the original endpoint RHS
with the derivative of an initial guess.  Any alternative representation
retaining the complete analytic circle must specify its full field,
derive its own equation and Jacobian, preserve the true domain and
acceptance gates, and account for its unprojected residual.  Such a
representation would be a separate finite approximation, not an accepted
solution of the previously recorded one.
