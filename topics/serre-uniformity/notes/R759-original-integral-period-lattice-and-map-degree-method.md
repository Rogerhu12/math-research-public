# R759 method: the complete original integral-period lattice and map degrees

Date: 2026-11-14. **The lattice, orientation, degree and recovery statements
below are proved. The numerical inputs from R754 have not yet been supplied
to this computation. No rank, map degree, short vector, rational function
or point coordinate is reported as a new computed result here.**

This is the executable successor to R754. It reads the successful original
period certificate and the unchanged R738 compact-chain artifact. It does
not regenerate the target, topology, torus average, period table or Hom
kernel. Its new output is the full integral-period lattice in that actual
Hom space, the exact degree form, and integral differentials for subsequent
rational-function reconstruction on the original curve.

## 1. The fixed original period convention

Use the R735 target and the exact R751 scale:

$$
K=\mathbf Q(\zeta),\quad \zeta^2+\zeta+1=0,
\quad\operatorname{Im}\zeta>0,
\qquad C/L:y^2=x^3+b,
\qquad\omega_C=\frac{dx}{2y},
$$

$$
\Lambda_C=\frac{\Omega_0}{R_C}\mathbf Z[\zeta].
\tag{759M.1}
$$

The order of the two rational coordinates is always **$1,\zeta$**.
The cycle order is the unchanged R738 list
$\gamma_1,\ldots,\gamma_{800}$, and the six rational Hodge forms are the
unchanged R745 $\omega_0,\ldots,\omega_5$. The actual $c_1$ has coset
4424, with the same original $c_0$ and target $b$. No new sixth root,
CM embedding or $c_1$ phase is selected.

Let $h_0,\ldots,h_5$ be the six $K$-basis differentials returned by
R754, written in the original $\omega_j$ basis. For every original
closed chain, its saved exact period has the form

$$
\frac{R_C}{\Omega_0}\int_{\gamma_i}h_\ell
=a_{i\ell}+b_{i\ell}\zeta,
\qquad a_{i\ell},b_{i\ell}\in\mathbf Q.
\tag{759M.2}
$$

R754 supplies the actual values, not merely their existence. The input
must be its completed 800-chain verification file, with SHA equal to
the entry in the successful R754 final certificate. The expected
R754 core SHA is an explicit execution argument and part of every
R759 checkpoint.

## 2. What the R738 polygon matrix actually pairs

The word `intersection_matrix` alone is not sufficient to decide whether
to use a matrix or its inverse in a degree calculation. Here the two
graphs in the original construction determine the answer.

The R738 primal graph is the modular spine: vertices are $R$-orbits,
and an $S$-pair gives an edge between the two neighboring $R$-vertices.
The original Manin edge $\{g0,g\infty\}$ is transverse to this spine
edge. For the identity label, the oriented spine edge goes from
$\zeta$ to $S\zeta=1+\zeta$, from left to right through $i$;
the oriented Manin edge goes from $0$ to $\infty$, upward through $i$.
Their local ordered tangent pair is positive. Every retained $g$ lies
in $\mathrm{SL}_2(\mathbf Z)$ and preserves that sign.

R738 contracts a primal spanning tree and joins cusp faces along the
second, dual spanning tree. Call the surviving oriented spine loops
$\delta_1,\ldots,\delta_{800}$. The compact Manin chain $\gamma_i$
has coefficient one on its own surviving edge, coefficient zero on
all other surviving edges, and uses only dual-tree Manin edges for
its closing path. It uses no primal-tree Manin edge. Consequently

$$
\delta_j\cdot\gamma_i=\delta_{ij}.
\tag{759M.3}
$$

Indeed, representatives of $\delta_j$ use their one surviving spine
edge and primal-tree paths. The latter have zero transverse
intersection with every $\gamma_i$, because no primal-tree Manin
edge occurs there. The closing Manin paths cross only the deleted
dual-tree spine edges. Thus the remaining local intersection is
exactly the one just oriented above.

Let $\alpha_i$ be the cohomology class whose value on $\delta_j$ is
$\delta_{ij}$. Fix the Poincaré-dual convention
$\int_\delta\operatorname{PD}(\gamma)=\gamma\cdot\delta$.
Equation (759M.3) gives

$$
\alpha_i=-\operatorname{PD}(\gamma_i).
\tag{759M.4}
$$

The R738 polygon uses these coordinate cochains on its surviving
**spine** edges. Its accumulated-prefix formula

$$
\frac12\sum_s
\bigl(A_i(s)\alpha_j(s)-A_j(s)\alpha_i(s)\bigr)
=\int_X\alpha_i\wedge\alpha_j
\tag{759M.5}
$$

is obtained by triangulating the oriented polygon. The face direction
is the retained positive cusp loop $T$, as in R738. Using (759M.4),
the two minus signs cancel and the saved matrix is therefore

$$
\boxed{\quad\Omega_{ij}=\gamma_i\cdot\gamma_j.\quad}
\tag{759M.6}
$$

It is a cup matrix for the coordinate cochains of the **spine** basis,
and a homology intersection matrix for the **Manin** basis used in
every actual period. These are dual bases, not the same basis. This
explains why taking the cup interpretation directly in the Manin
period coordinates would be wrong. The completed R738 certificate
already supplies $\det\Omega=1$; R759 reuses that matrix and proof.

## 3. The entire integral-period lattice

Expand an unknown differential in the fixed twelve rational directions:

$$
h(x,y)=\sum_{\ell=0}^5(x_\ell+y_\ell\zeta)h_\ell,
\qquad x_\ell,y_\ell\in\mathbf Q.
\tag{759M.7}
$$

The coefficient-column order is
$(x_0,\ldots,x_5,y_0,\ldots,y_5)^t$.
Since $\zeta(a+b\zeta)=-b+(a-b)\zeta$, the two period rows
corresponding to $\gamma_i$ are exactly

$$
P_{2i,*}=(a_{i,*},-b_{i,*}),\qquad
P_{2i+1,*}=(b_{i,*},a_{i,*}-b_{i,*}).
\tag{759M.8}
$$

Here the row labels are zero based when read by the code. Thus
$P\in\operatorname{Mat}_{1600\times12}(\mathbf Q)$ records both
coordinates for every original closed chain. Let $D>0$ clear all
its rational denominators and set $M=DP\in\operatorname{Mat}_{1600
\times12}(\mathbf Z)$.

Let $H\in\operatorname{Mat}_{12}(\mathbf Z)$ have as its rows the
nonzero row-Hermite basis of the lattice generated by **all** rows
of $M$. Its rank is checked in the computation; it is not inferred
from the requested output size. Write coefficient vectors as columns.
Then

$$
\begin{aligned}
\mathcal S
&=\{c\in\mathbf Q^{12}:Pc\in\mathbf Z^{1600}\}\\
&=\{c: Hc\in D\mathbf Z^{12}\}\\
&=\boxed{D H^{-1}\mathbf Z^{12}}.
\end{aligned}
\tag{759M.9}
$$

No transpose belongs on $H^{-1}$ in (759M.9): $H$ stores row
functionals and $c$ is a coefficient column. Denote the basis matrix
on the right by $B=D H^{-1}$. Its columns, rather than its rows, are
the integral differential directions.

For a bounded certificate of the equality of row lattices, the code
processes 32 original rows at a time. It stacks the previous nonzero
Hermite rows above the next original rows, obtains a full integer
unimodular transform $U$, and checks $U M_{\rm stack}=H_{\rm full}$
and $\det U=\pm1$. It saves every such transform and discards only
zero rows. Induction proves equality of the accumulated row lattice
with that of all processed rows, in both directions. All 1600 rows
are processed. Thus the result is not a twelve-dimensional sublattice
chosen by separate denominator clearing.

The complete integral period matrix is $PB$, and every one of its
entries is checked to be an integer. This is a full $\mathbf Z$-lattice
of rank twelve. Multiplication by $\zeta$ in the initial coefficient
coordinates is

$$
J_0=\begin{pmatrix}0&-I_6\\ I_6&-I_6\end{pmatrix}.
\tag{759M.10}
$$

The code computes and checks

$$
J_{\mathcal S}=B^{-1}J_0B\in\operatorname{Mat}_{12}(\mathbf Z),
\qquad J_{\mathcal S}^2+J_{\mathcal S}+I=0.
\tag{759M.11}
$$

Hence this is the full $\mathcal O_K$-stable lattice, of
$\mathcal O_K$-rank six. One need not mistake a selected twelve
rational directions for a complete integral lattice, nor assume an
integral basis of the target field $L$.

The meaning of completeness is also geometric. Every differential in
$\mathcal S$ has all periods in (759M.1), so integration from the
original $c_0$ gives a map $X_1\to C$ with $c_0\mapsto O$.
As proved in R732, its Jacobian homomorphism is algebraic, and it
descends to $L$ because its derivative and base condition do.
Conversely, every such homomorphism with derivative in the original
positive space has integral periods and hence lies in (759M.9).
The lattice is therefore the full lattice of
$\operatorname{Hom}_L(J_{X_1},C)$ in that positive rational Hom space.
Factoring through the original $q_1$ may still introduce its finite
isogeny denominator. We do not replace this lattice by an unproved
integral saturation statement for $A_{\theta,1}$ itself.

## 4. Exact degree and its sign

Let an integral differential have normalized period coordinates
$a,b\in\mathbf Z^{800}$ in the order $1,\zeta$. Since (759M.6)
is the homology intersection form, the coordinate cup pairing is

$$
\int_X a\wedge b=-a^t\Omega^{-1}b.
\tag{759M.12}
$$

For completeness, change the original cycles to an oriented integral
symplectic basis with intersection matrix
$J=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$.
In that basis the right side is
$a^tJb=\sum_i(a_{A_i}b_{B_i}-a_{B_i}b_{A_i})$, the ordinary
Riemann bilinear expression. Transforming back gives (759M.12).
In particular the sign is fixed by the identity map on the positive
elliptic period basis $(1,\zeta)$: it gives degree $+1$.

For the map $f$ with differential $h$, Riemann bilinearity gives

$$
\frac{i}{2}\int_Xh\wedge\bar h
=\left|\frac{\Omega_0}{R_C}\right|^2
\operatorname{Im}\zeta\,(-a^t\Omega^{-1}b).
\tag{759M.13}
$$

The left side is $\deg(f)$ times the area of the same target
$C$, which is the prefactor on the right. Therefore

$$
\boxed{\quad\deg(f)=-a^t\Omega^{-1}b.\quad}
\tag{759M.14}
$$

Write $A,B_1\in\operatorname{Mat}_{800\times12}(\mathbf Z)$ for
the two row blocks of the saturated period matrix $PB$. The notation
$B_1$ avoids confusing the second period block with the coefficient
basis $B$ in (759M.9). Solve only the new system

$$
\Omega Y=B_1,
\tag{759M.15}
$$

and verify that identity exactly. Unimodularity implies $Y$ is
integral, which is also checked. No symplectic basis, polygon or
full $800\times800$ inverse is regenerated. Put

$$
C_0=-A^tY,\qquad S=C_0+C_0^t.
\tag{759M.16}
$$

The degree of the map given by an integer coefficient column $n$ is

$$
d(n)=\frac12 n^tSn.
\tag{759M.17}
$$

The matrix $S$ is symmetric integral with even diagonal. It is
positive definite: the full period realization has rank twelve, and
the area norm of every nonzero real combination of these holomorphic
forms is positive. The code verifies positivity with an exact
rational $LDL^t$ decomposition and checks
$J_{\mathcal S}^tSJ_{\mathcal S}=S$. A negative sign or a wrong
cycle/cup identification cannot be corrected by taking absolute
values; it would fail these identities.

## 5. Short maps inside the complete integral lattice

For efficiency of the later Riemann–Roch step, the code performs
ordinary LLL on the positive degree Gram matrix, with
$\delta=3/4$ and exact rational Gram–Schmidt coefficients.
Every size reduction and swap is an integer unimodular row operation.
If the resulting row matrix is $U\in\mathrm{GL}_{12}(\mathbf Z)$,
then the new differential coefficient **columns** are

$$
B_{\rm new}=BU^t,
\qquad S_{\rm new}=USU^t.
\tag{759M.18}
$$

The determinant, congruence, all size-reduction bounds and Lovász
inequalities are checked exactly. The finite LLL algorithm uses no
floating-point distance or reconstruction. Its saved state includes
the current integer basis, next index and iteration count; it can
continue without redoing the lattice or degree solve.

All twelve new integral differentials, their full original integer
periods, their degrees $S_{{\rm new},ii}/2$, and the conjugated
integer $\zeta$ action are retained. The chosen map is the least
degree among these twelve basis vectors, with deterministic index
tie-breaking. **This does not assert a global minimum modular degree.**
Any nonzero chosen vector supplies a genuine original map and a
rigorous finite reconstruction bound.

To recover its coefficients in the original six $\omega_j$, the
script applies $BU^t$ to the saved six $L$-differential vectors from
R754. Scalar multiplication uses precisely

$$
(x+y\zeta)(a+b\zeta)=(xa-yb)+(xb+y(a-b))\zeta.
\tag{759M.19}
$$

This keeps the original $L=K(b)$ coordinates, $\alpha s$ descent and
the single original $\zeta^2$ transport. No Fourier first coefficient
is substituted for a Néron or Manin scale.

## 6. A specific effective divisor and the next exact truncation

The source coordinate is the original one:

$$
j=6912a^3(1-a^3).
\tag{759M.20}
$$

R738 gives the original $j$-map degree 4920. The polynomial map from
$a$ to $j$ has degree six, so $\deg(a)=820$. At every original cusp,
$j$ has pole order 246, hence $a$ has pole order 41. Thus
$(a)_0$ is an effective rational divisor of degree 820 whose support
avoids every cusp. This follows from the unchanged original
covering, not a new model or a new cusp marking.

For the actual selected map degree $d$, define

$$
m=\left\lceil\frac{2d+400}{820}\right\rceil,
\qquad D=m(a)_0,
\qquad M_0=820m+2d.
\tag{759M.21}
$$

This supplies the concrete divisor in R732, with
$\deg D\ge2d+g(X_1)$. The integral-period construction first gives
$f_0:X_1\to C$ **over $L$**, based at the original $c_0$.
The expansion cusp $P$ need not be $L$-rational, and its chosen
parameter and Fourier coefficients need not be over $L$ either.
For the retained full-level cusp one may use the fixed working
field $E=L(\alpha,\xi)$, where $\alpha^3=4$ is the original positive
root and $\xi=e^{2\pi i/41}$ is the original R751 root: the
full-level 246 Tate cusp has coefficients in
$\mathbf Q(\zeta_{246})=K(\xi)$, and the R745 $a$ branch uses this
same $\alpha$. More generally, any explicit finite cusp working
field containing these original data is allowed; no minimal
field claim is needed.

Over this fixed field $E$, the map used for the Laurent expansion is
$f_P=f_0-f_0(P)$, so $f_P(P)=O$. Its degree and derivative are still
$d$ and $h$, but it is only asserted to be defined over $E$ at this
stage. Let $q$ be the retained cusp parameter and
$I(q)=\int h$ with $I(P)=0$. The uniformization of the unchanged target has
$x_\infty=I^{-2}-(b/7)I^4+\cdots$. If $e=\operatorname{ord}_q I$,
then $e\le d$.

A basis $r_\nu$ of $\mathcal L(D)$, expanded through
$q^{M_0+2d}$, and $h/dq$ through $q^{M_0+3d}$ suffice for the exact
linear conditions

$$
[q^k](A-Bx_\infty)=0\quad(-2e\le k\le M_0),
\qquad A,B\in\mathcal L(D),\quad B\ne0.
\tag{759M.22}
$$

The proof is R732: $\deg(D-E_x)\ge400$ gives a nonzero denominator;
the difference has total pole degree at most $M_0$ but zero order
at least $M_0+1$, so it is identically zero. Hence
$x=A/B$ and $y=dx/(2h)$ are the actual map. Translation by its
value at the original $c_0$ then fixes the base point, and evaluation
at the original $c_1$ gives the corresponding $\beta_C$.

The linear system and the Riemann--Roch basis may therefore be
computed over $E$. Finite base extension does not change the genus,
divisor degrees, degree $d$, or the zero-versus-pole argument, so
all the displayed truncation bounds are unchanged. After obtaining
$f_P$, form $f_P-f_P(c_0)$. This is the original $f_0$: for every
$\sigma\in G_L$, it and its conjugate have the same original
$L$-defined derivative $h$ and send $c_0$ to $O$, hence differ by
the zero constant. This proves descent to $L$ after the actual base
translation, without imposing an $L$-rational zero value at an
arbitrary cusp.

R759 outputs $m,M_0$ and both explicit expansion bounds for the
**actual computed degree**. It does not claim to have computed that
Riemann–Roch basis, the rational functions or those point values.
Those are the subsequent original algebraic computation.

## 7. Execution and retained output

The core is `R759_integral_period_lattice_and_degrees.py`, requiring
Python-FLINT 0.9.0. Its public Actions guard precedes the disabling
of Python's decimal-integer string length limit, needed by the
original exact coordinates. Source SHA, the successful R754 core
and final certificate SHA, its actual period-file SHA and the fixed
R738 artifact SHA are part of every checkpoint.

Stages are: complete row-HNF with all unimodular certificates;
the full integral-period lattice and its $\zeta$ action; the new
intersection solve and positive degree form; exact LLL; the twelve
original map differentials and the selected bounded reconstruction
input. A successful completed result is reused by exact source and
stage SHA. An interruption preserves every complete stage and the
partial HNF/LLL state. Only small final certificates, receipts and
SHA manifests enter Git; all new exact matrices remain in artifacts.
Completed saturated-lattice and final-map stages are read directly
from the same tagged checkpoint, without repeating their inverse
or full period-table multiplication.

The method needs no local mathematical run. A public request may be
completed only after the true R754 result and artifact manifest are
available. An unexpected rank, nonintegral period, failed solve,
nonpositive degree form or failed $\zeta$ compatibility is a failed
computation, not a reason to alter an original phase.

## Dependencies

- R732, Sections 5–7: original rational Hom identification, integral
  periods, descent, degree and finite Riemann–Roch recovery.
- R738, Sections 4–5 and its retained source: the original two trees,
  actual compact Manin chains, polygon cochains and orientation.
- R735/R745/R751/R754: unchanged target, original Hodge basis,
  absolute period scale and the complete actual period/kernel tables.
- Python-FLINT 0.9.0 primary API documentation:
  [integer matrices](https://python-flint.readthedocs.io/en/latest/fmpz_mat.html)
  (`hnf(transform=True)`, `solve`, exact matrix operations) and
  [rational matrices](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html).
  The LLL loop itself uses the explicitly written exact rational
  algorithm, rather than relying on an undocumented Gram-mode return
  convention.
