# R267. Separate evidence and feasible points in a fixed damped model

**Status.** Complete finite-dimensional theorem. The result concerns one
fixed quadratic model and its linear inequalities. It supplies no
nonlinear BVP, native-tail or geometric acceptance claim. The numerical
substitution at the end uses stored request26 diagnostics only; it is not
a newly executed Actions calculation or a verified floating-point bound.

## 267.1. Fixed objects and notation

Let $A\in\mathbb R^{m\times n}$, $b\in\mathbb R^m$,
$B\in\mathbb R^{r\times n}$, $c\in\mathbb R^r$ and $\lambda>0$ be fixed.
Define

$$
 f(u)=\frac12\|Au+b\|_2^2+\frac{\lambda^2}{2}\|u\|_2^2,
 \qquad H=A^TA+\lambda^2I,
 \qquad g(u)=\nabla f(u)=A^T(Au+b)+\lambda^2u.
$$

The feasible set is

$$
 \mathcal C=\{u\in\mathbb R^n:Bu+c\ge0\},
$$

with componentwise inequalities. Assume $\mathcal C$ is nonempty. It is
closed and convex. Since $H\succeq\lambda^2I$, $f$ is coercive and
strictly convex, so it has a unique constrained minimizer $u_*$ and finite
minimum $f_*=f(u_*)$.

For statements about decrease from the zero direction, also assume
$c\ge0$, so $0\in\mathcal C$. The warm algorithms use the stronger
condition $c>0$. Define

$$
 \Delta(u)=f(0)-f(u),\qquad \Delta_*=f(0)-f_*.
$$

An **evidence point** $x$ can be any vector in $\mathbb R^n$; it need not
be feasible or be a physically admissible nonlinear trial. A **final
candidate** $z$ is a separate vector whose linear feasibility must be
established before the candidate bounds below are applied.

All occurrences of $A,b,\lambda,B,c$ refer to these same fixed objects.
In the repository model, this also fixes the original residual weights,
coordinate scaling, base state and Jacobian. A lower bound from a
previous warm model cannot be transferred merely because the field
dimension or the value of $\lambda$ is unchanged.

## 267.2. General lower bound at any evidence point

**Theorem 267-A.** For arbitrary $x\in\mathbb R^n$ and
$\mu\in\mathbb R^r$ with $\mu\ge0$, set

$$
 r(x,\mu)=g(x)-B^T\mu
$$

and

$$
 L(x,\mu)
 =f(x)-\mu^T(Bx+c)
  -\frac{\|r(x,\mu)\|_2^2}{2\lambda^2}.
$$

Then

$$
 f_*\ge L(x,\mu).
$$

There is no feasibility, complementarity, stationarity, rank or
linear-solver convergence assumption on $x$. The multiplier need not be
optimal or approximate a KKT multiplier. Its required sign is
$\mu\ge0$ for the convention $Bu+c\ge0$.

**Proof.** For fixed $\mu$, use the Lagrangian

$$
 \mathcal L_\mu(u)=f(u)-\mu^T(Bu+c).
$$

Its Hessian is the same $H\succeq\lambda^2I$ as that of $f$, and its
gradient at $x$ is $r(x,\mu)$. Thus, for every $v\in\mathbb R^n$,

$$
 \begin{aligned}
 \mathcal L_\mu(v)
 &\ge \mathcal L_\mu(x)
     +r(x,\mu)^T(v-x)+\frac{\lambda^2}{2}\|v-x\|_2^2\\
 &=\mathcal L_\mu(x)-\frac{\|r(x,\mu)\|_2^2}{2\lambda^2}
   +\frac{\lambda^2}{2}
      \left\|v-x+\frac{r(x,\mu)}{\lambda^2}\right\|_2^2\\
 &\ge L(x,\mu).
 \end{aligned}
$$

For a feasible $v$, nonnegativity of $\mu$ gives
$f(v)\ge\mathcal L_\mu(v)$. Consequently $f(v)\ge L(x,\mu)$ for every
$v\in\mathcal C$, and taking the constrained minimum proves the claim.
In particular, $Bx+c$ itself may have negative components: its actual
signed value, rather than its positive part or an assumed zero, belongs
in the formula. $\square$

For this quadratic, exact minimization of the Lagrangian would give the
possibly sharper lower bound

$$
 \inf_u\mathcal L_\mu(u)
 =\mathcal L_\mu(x)-\frac12r(x,\mu)^TH^{-1}r(x,\mu).
$$

Theorem267-A uses the simpler inequality
$H^{-1}\preceq\lambda^{-2}I$, so it does not require an inverse,
factorization or an accurately solved normal equation. It does require
the complete model gradient, not only its projection onto a numerical
subspace or its column-preconditioned norm.

## 267.3. Multiple evidence points and a separate feasible candidate

**Theorem 267-B.** Suppose $(x_i,\mu_i)$, $1\le i\le q$, are any finite
collection of legal evidence pairs for the same fixed model. Define

$$
 L_{\max}=\max_{1\le i\le q}L(x_i,\mu_i).
$$

Every feasible $z$ satisfies

$$
 0\le f(z)-f_*\le f(z)-L_{\max}.
 \tag{267.1}
$$

It also satisfies

$$
 \|z-u_*\|_2
 \le\frac{\sqrt{2\bigl(f(z)-L_{\max}\bigr)}}{\lambda}.
 \tag{267.2}
$$

If $0\in\mathcal C$ and $\Delta(z)>0$, then

$$
 0<\Delta(z)\le\Delta_*\le f(0)-L_{\max}
$$

and therefore

$$
 \frac{\Delta(z)}{\Delta_*}
 \ge\frac{\Delta(z)}{f(0)-L_{\max}}.
 \tag{267.3}
$$

In particular, the evidence points may be infeasible while the final
candidate is feasible. The evidence need not come from the algorithm
that produced the final candidate.

**Proof.** Each lower bound from Theorem267-A is valid, so their maximum
is valid. Combining $L_{\max}\le f_*\le f(z)$ gives (267.1).

For the distance assertion, fix feasible $z$. Convexity of $\mathcal C$
makes the segment $u_*+t(z-u_*)$ feasible for $0\le t\le1$.
Minimality of $u_*$ implies the one-sided derivative condition
$g(u_*)^T(z-u_*)\ge0$. Strong convexity then gives

$$
 f(z)\ge f(u_*)+g(u_*)^T(z-u_*)
             +\frac{\lambda^2}{2}\|z-u_*\|_2^2
 \ge f_*+\frac{\lambda^2}{2}\|z-u_*\|_2^2.
$$

Apply (267.1) and take the nonnegative square root to obtain (267.2).
Finally, subtract the inequalities $L_{\max}\le f_*\le f(z)$ from
$f(0)$, use $\Delta(z)>0$, and divide only by positive denominators to
obtain (267.3). $\square$

No independence or predetermined choice of the evidence pairs is
required: taking the maximum of finitely many valid deterministic lower
bounds preserves validity. Every included pair must nevertheless use the
same model and the correct complete quantities.

## 267.4. Useful special cases and the relation to R263/R265

With $\mu=0$, Theorem267-A becomes

$$
 L(x,0)=f(x)-\frac{\|g(x)\|_2^2}{2\lambda^2}.
$$

Thus an arbitrary, possibly infeasible raw LSMR point $x$ can certify the
following model-quality bound for a separately verified feasible $z$:

$$
 \frac{\Delta(z)}{\Delta_*}
 \ge
 \frac{\Delta(z)}
 {\displaystyle\Delta(x)+\frac{\|g(x)\|_2^2}{2\lambda^2}}.
 \tag{267.4}
$$

Here $\Delta(x)$ need not be positive. Under the theorem's assumptions,
the displayed denominator is at least $\Delta_*\ge\Delta(z)>0$.
The denominator is not formed using the gradient at $z$ unless $x=z$ is
deliberately chosen. A large gradient at a feasible projected candidate
does not invalidate a better lower bound obtained at a different point.

If the evidence point is itself feasible and is chosen equal to $z$,
then

$$
 f(z)-L(z,\mu)
 =\mu^T(Bz+c)+\frac{\|g(z)-B^T\mu\|_2^2}{2\lambda^2},
$$

which is the one-point complementarity-plus-residual estimate of R265.
The zero-multiplier unconstrained case recovers the corresponding damped
model estimate in R263. R267 separates the two roles and permits choosing
the strongest available lower bound.

Multipliers obtained from a different projection metric are not thereby
KKT multipliers of $f$. They can still be **evidence multipliers** in
Theorem267-A if they are nonnegative and all terms in its formula are
actually recomputed with the original $B,c,g$. For a positive row scaling
$D$, a multiplier $\widetilde\mu$ associated with $D(Bu+c)$ corresponds
to $\mu=D\widetilde\mu$ in the original convention. An arbitrary
negative multiplier is inadmissible. Replacing it by its componentwise
positive part is permitted only if the Lagrangian and full residual are
then recomputed for that replacement.

## 267.5. Stored request26 data as a formal substitution

The actual request26 finite model uses lambda270. In its
`full-angle-warm/model-000.json`, the raw unconstrained LSMR point $x$ has

```text
Delta(x)             = 0.5355637512713852
reported ||g(x)||_2  = 345.6423090505119
```

The separately repaired and selected full direction $z$ has program-
checked nonnegative slacks at all10,240 finite rows and

```text
Delta(z) = 0.4990204300440543.
```

Substituting these stored diagnostics into (267.4) gives the expression

$$
 \frac{0.4990204300440543}
 {\displaystyle0.5355637512713852
  +\frac{(345.6423090505119)^2}{2\cdot270^2}}.
 \tag{267.5}
$$

This file does not evaluate that ratio locally or describe it as an
already saved Actions diagnostic. It also does not replace the full
gradient by LSMR's much smaller preconditioned normal residual. The
artifact identities are recorded in
`../notes/2026-11-14-actual-request26-full-angle-projection-warm.md`.

The $z$ in this substitution is the **full selected model direction**.
The real nonlinear trial accepted only $\alpha z$ with
$\alpha=2^{-6}$. Because $0,z\in\mathcal C$ and the constraint set is
convex, $\alpha z$ is also feasible in exact arithmetic for
$0\le\alpha\le1$. To assess that scaled model direction instead, the
numerator must be replaced by

$$
 \Delta(\alpha z)
 =-\alpha b^TAz
   -\frac{\alpha^2}{2}
       \bigl(\|Az\|_2^2+\lambda^2\|z\|_2^2\bigr),
$$

using the same fixed model. It must not be replaced by the observed
nonlinear merit decrease, which is a different quantity and excludes
the damping penalty. No bound in this theorem transfers between the
weights refreshed for request26 and those of request22 or request27.

## 267.6. What a rigorous floating-point use must establish

The theorems above are exact real-arithmetic statements. Ordinary
floating-point signs, dot products, residual norms and printed decimals
are useful diagnostics but are not, by themselves, verified bounds.

For example, suppose the same finite model and evidence point have
certified enclosures providing a lower bound $f_x^-$ for $f(x)$, an
upper bound $m^+$ for the signed product $\mu^T(Bx+c)$, an upper bound
$R_+^2$ for $\|g(x)-B^T\mu\|_2^2$, and a positive lower bound
$\lambda_-\le\lambda$. With outward evaluation,

$$
 L^-=f_x^- -m^+-\frac{R_+^2}{2\lambda_-^2}
$$

is a certified lower bound. Each multiplier's nonnegative sign must also
be established. For several evidence pairs, the maximum of their
certified lower bounds remains a certified lower bound.

For the final candidate, its original finite inequalities must be
verified, rather than inferred from a near-zero rounded slack. If
certified objective bounds give $f_0^-\le f(0)\le f_0^+$ and
$f(z)\le f_z^+$, with $f_0^- -f_z^+>0$, a certified version of (267.3)
is

$$
 \frac{\Delta(z)}{\Delta_*}
 \ge\frac{f_0^- -f_z^+}{f_0^+-L^-},
$$

with its quotient rounded downward. The gap and distance statements
similarly use $f_z^+-L^-$ and $\lambda_-$ with outward rounding.

One may define the finite model by treating its saved binary64 entries
as exact real coefficients. A verified computation then bounds that
literal finite model. Identifying it with an unrounded Jacobian or a
continuous geometric problem requires the additional corresponding
error bounds. Neither equality of source hashes nor a passing derivative
check alone supplies those error bounds.

These requirements concern the interpretation of a **rigorous posterior
bound**. They do not impose new BVP acceptance gates or cancel the
independently recorded actual warm decrease and original domain checks.
