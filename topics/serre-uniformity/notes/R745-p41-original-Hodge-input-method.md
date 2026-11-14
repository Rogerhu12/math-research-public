# R745 — Original p41 Hodge basis and finite period input

**Pre-run method, 2026-11-14.** This file specifies new exact arithmetic
on the public repository Actions. No returned rank or coefficient is
claimed before that execution. R738's completed topology is reused by
hash. This computation does not evaluate the algebraic CM periods or
produce quotient functions, $\beta$, or heights.

## 1. Fixed fields, the original character, and the same source

Put $p=41$, $N=6p=246$, $n=p+1=42$, and fix

$$
\eta=e^{2\pi i/42},\qquad \zeta=\eta^{14},\qquad
s=1+2\zeta=\sqrt{-3},\qquad \alpha=\sqrt[3]4>0,
\qquad F=\mathbf Q(\eta+\eta^{-1}).
\tag{745M.1}
$$

The $p$-adic embedding sends $\eta$ to the original Teichmüller lift of
$\gamma=7+30\zeta\in\mathbf F_{41^2}$; its order is 42 and
$\gamma^{14}=\zeta$. These are the retained R717 labels. Set
$\beta=\eta+\eta^{-1}$ and

$$
\mathcal H=\{1,13,19,25,31,37\}.
\tag{745M.2}
$$

The automorphisms $\sigma_h:\eta\mapsto\eta^h$, $h\in\mathcal H$,
fix $K=\mathbf Q(\zeta)$ and induce all six embeddings of $F$.
For nonzero $y\in\mathbf F_{41^2}$, define

$$
\theta(y)=\eta^{-\log_\gamma(\bar y/y)},\qquad
\theta_h=\sigma_h\theta.
\tag{745M.3}
$$

Thus $\theta(y)=[y]^{-(p-1)}$, $\theta(\zeta)=\zeta^{-1}$, and
$\theta(s)=-1$, in the fixed original convention. The primitive
newform is

$$
f_h(\tau)=\sum_{m\ge1}a_{m,h}e^{2\pi i m\tau},\qquad
a_{m,h}=\sum_{\substack{z\in\mathbf Z[\zeta],\ z\equiv1\ (3)\\
\operatorname N z=m,\ (m,3p)=1}}z\theta_h(z).
\tag{745M.4}
$$

There is exactly one generator $z\equiv1\pmod{3\mathcal O_K}$ of
each ideal prime to three, since the six units map bijectively to
$(\mathcal O_K/3)^\times$. This removes a possible factor of six.
In integer coordinates the condition is $z=a+b\zeta$,
$a\equiv1$, $b\equiv0\pmod3$. It is the original
$\Psi_\theta((z))=z\epsilon_3(z)\theta(z)$, with
$\epsilon_3(z)=1$ on these generators.

The coefficients lie in $F$; conjugating the ideals proves this
directly. The finite calculation checks the fixed normalizations
$a_1=1$, $a_2=0$, $a_4=-2$, the support $m\equiv1\pmod3$,
$a_{pm}=0$, and $a_{4m}=-2a_m$ wherever the requested prefix applies.
The exact newform level is $9p^2$, as in R575.

The source is the original $X_1$ of R738, with
$j=6912a^3(1-a^3)$. We retain its full $Q_8$ graph, original
nonsplit pair, and the exact marked matrix

$$
g_*=\begin{pmatrix}15130&123\\123&1\end{pmatrix}.
\tag{745M.5}
$$

The real $c_1$ is coset 4424 with tame label $C$; its analytic
representative is $g_*\zeta$. Coset zero has $a=\zeta$.
The three cosets $2876,2822,2823$ represent the single coarse $c_0$.
These labels are read from R738's exact retained artifact.

## 2. The actual average, without changing its denominator

Use the left finite model and original form

$$
V=\mathbf Q(\eta)^{\mathbf F_p}/\mathbf Q(\eta)\mathbf1,
\qquad G(e_r,e_t)=p\delta_{rt}-1.
\tag{745M.6}
$$

The upper Borel acts by affine permutations. The Weyl matrix acts as

$$
w e_r=-\frac1p\sum_{y\ne0}\theta(y)
 e_{r\operatorname N(y)+\operatorname{Tr}(y)}.
\tag{745M.7}
$$

The projective original torus consists of the identity and

$$
t_b=\begin{pmatrix}b&-1\\1&b+1\end{pmatrix},\qquad b\in\mathbf F_p.
\tag{745M.8}
$$

Its Bruhat formula gives

$$
\rho(t_b)e_r=-\frac1p\sum_{y\ne0}\theta(y)
 e_{(b^2+b+1)((r+b+1)\operatorname N(y)+\operatorname{Tr}(y))+b}.
\tag{745M.9}
$$

All indices are taken modulo $p$. In particular, the exact vector

$$
u=A_{\mathsf T_\zeta}e_0
  =\frac1{p+1}\left(e_0+\sum_b\rho(t_b)e_0\right)
  =\sum_{r=1}^{40}\frac{c_r(\eta)}{1722}e_r
\tag{745M.10}
$$

has integer polynomial numerators modulo $\Phi_{42}$, with $c_0=0$.
The coefficient convention subtracts the zero-coordinate of the
unsimplified vector, using $\sum e_r=0$. It introduces no scalar
rescaling of the average.

The output keeps all 41 numerators in the power basis
$1,\eta,\ldots,\eta^{11}$. It also computes the original
finite norm $N_1$ directly from the same sums, and verifies

$$
N_1=(p+1)G(u,u),\qquad N_1\equiv-1\pmod p.
\tag{745M.11}
$$

The chosen embedding is used for the congruence. The exact polynomial
for $N_1$ supplies every conjugate $N_h$ by $\sigma_h$; it is not a
claim that every conjugate is a $p$-unit. Invariance of $u$ under a
generator of the actual torus and the original normalizer
$M=\left(\begin{smallmatrix}-1&-1\\0&1\end{smallmatrix}\right)$ is
checked in the same quotient coordinates. Frobenius pairs the
norm/trace fibers, so $c_r\in F$; this is also checked as the exact
identity $c_r(\eta^{-1})=c_r(\eta)$.

This is one new computation of the full original $p41$ vector. The
norm is obtained from that computation and can be reused by R748.
It requires no new CM $L$-value enumeration or Fourier transform.

## 3. The full tame arithmetic descent

Before transporting to $c_1$, put

$$
H_0^\circ(\tau)=f_1(\tau/(6p)),\qquad
H_2^\circ(\tau)=f_1(4\tau/(6p)),\qquad
F_1^\circ=H_0^\circ-4\zeta^2H_2^\circ.
\tag{745M.12}
$$

The original pure two-level right-slash matrices on coefficient columns
in $(H_0^\circ,4H_2^\circ)$ are

$$
S_2=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
T_2=\begin{pmatrix}-1&0\\-1&1\end{pmatrix}.
\tag{745M.13}
$$

These are R592's matrices with the simultaneous three-level translation
factor removed. The latter factor is $\zeta$: the pure three-level
translation is represented by $T^{2p}$ and (745M.4) has support
$m\equiv1\pmod3$. The pure $S_3$ acts trivially because it lies in
the actual $Q_8$ kernel.

Let $v=(1,-\zeta^2)^{\mathsf t}$. Because this is the right-slash
coefficient convention, $C=S_2T_2$ has coefficient matrix $T_2S_2$,
and

$$
(T_2S_2)v=\zeta^2v.
\tag{745M.14}
$$

The geometric graph generator $(C,T_3)$ therefore fixes $v$.
One must also impose the full graph's determinant-minus-one element
$(T_2,D_3)$, where $D_3=\operatorname{diag}(1,-1)$.
Its determinant Galois action fixes $F$ and $\zeta_p$ and sends
$\zeta$ to $\zeta^2$. On this space it acts by

$$
T_2\bar v=-v.
\tag{745M.15}
$$

Since $\bar s=-s$, the full graph fixes $sv$. Thus the arithmetic
canonical Hodge line is $sF_1^\circ$ after the unchanged $p$-projection.
The factor $s$ is explicit; no unspecified algebraic lift or rational
normalization of $v$ has been inserted.

For the $p$-component, the finite left action is inverse to the
classical right action. The determinant action is included: the
Fourier coefficient automorphism $\zeta_p\mapsto\zeta_p^d$ acts by
$e_r\mapsto e_{dr}$, which is the action of
$\operatorname{diag}(1,d)^{-1}$ in the left model. Its coefficients
fix $F(\zeta)$ because the chosen determinant is one at all
prime-to-$p$ coefficient places. Hence the complete arithmetic
Cartan/normalizer invariance follows from (745M.10), not merely from
complex determinant-one invariance. This is the actual convention
proved in R742 §3.

Now apply the positive twist $u=a/\alpha$ of R575. Its cocycle on
the pullback is $\delta_{\kappa_4^{-1}}$, while this Hodge line has
deck character $\zeta$. Therefore multiplying the pulled-back
canonical differential by $\alpha$ gives the actual arithmetic
Hodge line on $X_1$. The full scalar is $\alpha s$.

Finally, (745M.5) is identity at $3,p$ and equals $C$ at 2. Thus

$$
F_1^\circ|_2g_*=\zeta^2F_1^\circ.
\tag{745M.16}
$$

The global forms and period tables below use the untransported functions
on $X_1$. Evaluation at $c_1$ uses $g_*\zeta$, or equivalently slashes
once by $g_*$ and evaluates at $\zeta$. The factor $\zeta^2$ is not
inserted a second time. At the $c_0$ marking the pure two-level
reflection instead gives the vector $(-\zeta^2,1)$ of R586.

## 4. Explicit Fourier functions and a rational Hodge basis

For $r\in\mathbf F_p$, take the unique

$$
0\le k_r<246,\qquad k_r\equiv0\pmod6,\qquad k_r\equiv r\pmod p.
\tag{745M.17}
$$

The actual unipotent realization is
$H_{i,r}^\circ(\tau)=H_i^\circ(\tau-k_r)$.
With $Q=e^{2\pi i\tau/246}$ and $\xi=e^{2\pi i/41}$, its phase is
$\xi^{-mr/6}$, where $6^{-1}$ is taken modulo 41. This fixed
tame-unit factor cannot be suppressed in an absolute Fourier table.
It still gives the same determinant action $r\mapsto dr$.

Let $\mathcal F_h$ be the Cartan average of (745M.12), using
$\sigma_h(c_r)/1722$. Define the six exact differentials

$$
\boxed{
\omega_j=2\pi i\,\alpha s\sum_{h\in\mathcal H}
 \sigma_h(\beta)^j\mathcal F_h(\tau)\,d\tau,
\qquad 0\le j\le5.
}
\tag{745M.18}
$$

By the arithmetic descent in Section 3, this is the $F/\mathbf Q$
trace construction on the original positive factor, so
$\omega_j\in H^0(X_1,\Omega^1)_{\mathbf Q}$.
The local invariant dimensions are one for the full six-level graph
and for the specified nonsplit normalizer, and one at all remaining
spherical places. Global multiplicity one therefore identifies their
span with the six-dimensional Hodge space of the actual primitive
factor of R616. The six distinct Hecke eigenlines are nonzero, by
the nonzero torus average and tame vector. The Vandermonde matrix on
the six distinct $\sigma_h(\beta)$ proves that (745M.18) is a basis.
This identifies a differential space; it does not identify its
integral Néron lattice or silently divide by an isogeny scalar.

For an explicit small coefficient representation, put

$$
U_{j,m,r}=\operatorname{Tr}_{F/\mathbf Q}
 \bigl(\beta^j a_{m,1}c_r(\eta)\bigr)\in\mathbf Z,
\qquad
P_{j,m}(\xi)=\sum_{r=1}^{40}U_{j,m,r}\xi^{-mr/6}.
\tag{745M.19}
$$

The trace is integral, because the polynomial numerators and newform
coefficients are algebraic integers. It can be evaluated as half the
full degree-12 trace, since its argument is real. The inert-2 identity
$a_{4m}=-2a_m$ now gives

$$
\frac{\omega_j}{246\alpha\,dQ/Q}
 =\frac1{1722}\sum_{m\ge1}
 \begin{cases}
 s P_{j,m}(\xi)Q^m,&m\text{ odd},\\
 3 P_{j,m}(\xi)Q^m,&4\mid m,\\
 0,&m\equiv2\pmod4.
 \end{cases}
\tag{745M.20}
$$

In the even case, $1+2\zeta^2=-s$, and the additional $s$ in
(745M.18) turns $-s^2$ into 3. The factor 246 in (745M.20) is the
exact differential change $2\pi i\,d\tau=246\,dQ/Q$.

The program outputs (745M.19) through exponent 800, reduced modulo
$\Phi_{41}(\xi)$. An exact nonzero six-by-six minor is certified by
a specialization at a prime $\ell\equiv1\pmod{123}$ with
$\ell\nmid1722$. The image of $\xi$ has exact order 41 and
$s^2=-3$ is also solved in that residue field. Each stripped row
factor in (745M.20) is nonzero; hence a nonzero minor proves the
rank in characteristic zero. The output records the actual prime,
root, row exponents, matrix and determinant.

The prefix is sufficient for identification on this actual source:
a nonzero holomorphic differential on a genus-400 curve has total
zero degree 798. Vanishing of the Fourier function through exponent
800 would give order at least 800 for the differential at this cusp,
which is impossible. No Sturm bound from a different $\Gamma_1$
curve is being used.

## 5. An independently fixed q-expansion of the source parameter

The cusp phase in the same component can also be fixed explicitly.
Let $\Delta=\eta_{\mathrm{Ded}}^{24}$, so
$E_4^3-E_6^2=1728\Delta$. The selected canonical branch is

$$
u^3=\frac18-\frac{sE_6}{576\eta_{\mathrm{Ded}}^{12}}.
\tag{745M.21}
$$

It satisfies the original Brau–Jones $j$ equation. Since
$\eta_{\mathrm{Ded}}^{12}=q^{1/2}\prod_{m\ge1}(1-q^m)^{12}$,
the exact branch with root constant one is

$$
\boxed{
\frac a\alpha=\frac{s}{12}Q^{-41}
\left(
\frac{E_6(Q^{246})}{\prod_{m\ge1}(1-Q^{246m})^{12}}
       +24sQ^{123}\right)^{1/3}.
}
\tag{745M.22}
$$

To fix its CM phase, follow the vertical boundary
$\tau=-1/2+iy$, $y\ge\sqrt3/2$. The product in
$\eta_{\mathrm{Ded}}^{12}$ is positive real and its leading square
root has phase $-i$. The real value $E_6$ is positive on this ray:
it is positive at infinity and has no zero there, by its ordinary
valence divisor. Thus the right side of (745M.21) is positive.
The cube root in (745M.22) has phase $\zeta$ on this ray, from
its leading term $(s/12)q^{-1/6}$. At $\tau=\zeta$,
$E_6/\eta_{\mathrm{Ded}}^{12}=24s$, so $u^3=1/4$ and
$u=\zeta/\alpha$. Therefore $a=\zeta$ at the reference coset,
and (745M.16) gives $a=1$ at the actual $c_1$. This agrees with
the independent real-structure determination of R738.

The output computes the finite requested expansion of (745M.22)
and checks its cube exactly. It is an actual source-coordinate
expansion, not a change in the original variable $a$.

## 6. Complete finite input for the original CM period kernel

For $r=1,\ldots,40$ define the rational positive-determinant matrices

$$
A_r=\begin{pmatrix}1&-k_r\\0&246\end{pmatrix},\qquad
B_r=\begin{pmatrix}4&-4k_r\\0&246\end{pmatrix}.
\tag{745M.23}
$$

With the usual weight-two determinant slash, the raw functions obey

$$
H_{0,r}^\circ=246(f_h|_2A_r),\qquad
H_{2,r}^\circ=\frac{246}{4}(f_h|_2B_r).
\tag{745M.24}
$$

The associated differential is an actual pullback because
$d(A\tau)=\det(A)(c\tau+d)^{-2}d\tau$. Consequently (745M.18) is
the explicit sum

$$
\boxed{
\omega_j=\frac{\alpha s}{7}
 \sum_{h\in\mathcal H}\sum_{r=1}^{40}
 \sigma_h\bigl(\beta^j c_r(\eta)\bigr)
 \left(A_r^*(2\pi i f_h\,d\tau)
       -\zeta^2B_r^*(2\pi i f_h\,d\tau)\right).
}
\tag{745M.25}
$$

Here $246/1722=1/7$; the original average denominator has been
canceled only against the displayed differential pullback factor.
It has not been normalized away by declaring a quotient differential
to be a unit.

For a retained positive Manin matrix
$g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$,
the four actual endpoints in the order $A_r0,A_r\infty,B_r0,B_r\infty$
are

$$
\frac{b-k_rd}{246d},\quad
\frac{a-k_rc}{246c},\quad
\frac{4(b-k_rd)}{246d},\quad
\frac{4(a-k_rc)}{246c}.
\tag{745M.26}
$$

These are reduced as rational numbers, with the zero denominator
recorded as infinity. The program forms and deduplicates this list
for all 819 retained relative edges and all 40 translate pairs.
The original 800 closed chains from R738 specify the signed sums
without any new topological computation.

If
$\lambda_h(t)=\Omega_0^{-1}\int_\infty^t2\pi i f_h(\tau)d\tau$,
each row contributes

$$
\lambda_h(A_r g\infty)-\lambda_h(A_r g0)
 -\zeta^2\bigl(\lambda_h(B_r g\infty)-\lambda_h(B_r g0)\bigr),
\tag{745M.27}
$$

with the exact coefficient in (745M.25). R732's completed weight-one
CM kernel applies to these exact rational endpoints, including
denominators not coprime to $6p$. Thus every finite translate,
coefficient, endpoint and sign needed for this period matrix is
now specified by the output. The values of (745M.27) themselves
are a remaining computation; this file does not claim otherwise.

## 7. Retained inputs, outputs, and scope

The completed topology comes only from public run `43612108090`,
artifact `serre-global-R738-p41-original-period-input-43612108090-1`:

| Input | SHA-256 |
|---|---|
| `original-cosets-and-markings.json.gz` | `6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161` |
| `integral-compact-Manin-cycles.json.gz` | `d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf` |
| Small final certificate | `a853f36bf5d6f7d238e805a5c2134b2f7b3db17528195d56d980e66c9c769009` |

The character label is also checked against the retained 2472-byte
R717 p41 receipt from run `43597163388`, SHA-256
`fb4d9ffadacda241575ab92a49f66819d8ac077ececa8f5151adf4aea3751fa6`.
Only its exact field label is read; none of its completed enumeration,
DFTs, or integer-trace recovery is repeated.

The new complete coefficient and endpoint tables remain in the new
Actions artifact. Only the small certificate, receipts and hash
manifest are published into Git. The scripts retain full or failed
outputs; the verifier requires a complete rank-six certificate and
the same original CM markings.

R735's original target model is reused, not recomputed. The remaining
substantive steps are the actual CM period values, the resulting
homomorphism lattice, original rational functions and $\beta$
coordinates, followed by their original height normalization. A
computed Hodge basis alone is not a height exclusion or a completion
of Serre uniformity.

## Sources

- R575, R586, R592: the original positive CM character, exact raw
  tame matrices, Fourier normalization, and both markings.
- R616 §4: full $Q_8$ graph, the one-dimensional arithmetic
  local invariant space, and the actual positive factor.
- R742 §3: the complete arithmetic $p$-action, including the
  determinant action and inverse finite left convention.
- R738: the original closed integer chains, rational matrix lifts,
  real structure, deck direction, and $c_0/c_1$ labels.
- R732: the original completed CM period kernel and its precise
  use in rational-function reconstruction.
- P. Mercuri and R. Schoof, *Modular forms invariant under non-split
  Cartan subgroups*, Math. Comp. 89 (2020), §§4–6,
  [author manuscript](https://reneschoof.github.io/mcom3503.pdf):
  finite cuspidal model and the actual Cartan trace realization.
- J. Brau and N. Jones, *Elliptic curves with 2-torsion contained
  in the 3-torsion field*, Proc. AMS 144 (2016), Theorem 1.4,
  [author manuscript](https://homepages.math.uic.edu/~ncjones/2tin3t.pdf):
  the original level-six graph and $j$ model.
