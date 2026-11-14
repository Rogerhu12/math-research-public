# R754 — Exact original p41 periods and the complete Hom kernel

**Pre-run method, 2026-11-14.** The identities and finite algorithm below
are proved. Actual period coordinates, rank, kernel and integer clearing
factors are numerical conclusions only after the public repository
Actions returns a complete certificate. All arithmetic is exact.

This task reuses the completed original R735 target, R738 topology and
R745 Hodge vector. It does not repeat the old division-polynomial/model
calculation, topology, finite torus average, L5/L7 enumeration or DFT.

## 1. The retained fields and actual markings

Use precisely R751:

$$
p=41,\quad K=\mathbf Q(\zeta),\quad \zeta^2+\zeta+1=0,
\quad A=\mathbf Q(\eta),\quad\eta=e^{2\pi i/42},
\quad\beta=\eta+\eta^{-1}.
\tag{754M.1}
$$

Write $M_0=K(U)$ for the retained degree-280 field, with the exact
R735 monic polynomial $P(U)$; $L=K(b)\subset M_0$ has degree seven.
All $280$-dimensional arithmetic is represented by two rational
polynomials modulo $P$, in the fixed basis $1,\zeta$.

The point for this field realization is

$$
P'=D_u(\Omega_0/p),\quad
u=\sqrt[3]4\,e^{\pi i/6},\quad
U=64/X(P')^3=-4/x(\Omega_0/p)^3.
\tag{754M.2}
$$

Thus it is R751's **negative-real $U$ embedding**, not the real point
of $E_{27}$. The latter is $[2+\zeta]P'=[-\zeta\sqrt{-3}]P'$.
R751 proves that the original $b$ is unchanged, and retains the
resulting $-\zeta$ in the target scaling. No alternative real root,
CM direction or quotient normalization is selected.

Let $S(U)=W(U)(1-3^{20}R_3(U)^2)$ be R735's original function, read
from its completed `wn,wd,rn,rd` products. Put

$$
H(U)=\frac{U^7S(U)}{1+U},\qquad
Z_a=R_C\alpha\sqrt{-3}\,\lambda_1(a/p),\quad1\le a\le40.
\tag{754M.3}
$$

The exact meaning of $R_C$, $\alpha$, $\lambda_1$, and the
once-only $c_1$ phase is R751. In particular
$R_C^6=-b$ and $\Lambda_C=(\Omega_0/R_C)\mathcal O_K$.

The original finite character is unchanged:
$\gamma=7+30\zeta\bmod41$, $\gamma^{14}=\zeta$,
$\theta(y)=\eta^{-\log_\gamma(\bar y/y)}$, so
$\theta(\gamma)=\eta^2$.

## 2. A seven-term nonzero period-line projector

Let $\mathcal M=K(E_{27}[p])$, whose Galois group is
$\mathbf F_{p^2}^{\times}$ by R725. Set
$r=r_0(P_{27}^{\rm real})$. For $c$ in the subgroup fixing $L$,

$$
\sigma_c r=\theta(c)^{-1}r.
\tag{754M.4}
$$

The class of $\gamma$ generates the quotient of order seven. Define

$$
z_* =\frac17\sum_{j=0}^{6}\theta(\gamma)^{-j}
                \frac r{\sigma_\gamma^j r}\ \in L A.
\tag{754M.5}
$$

Each ratio is in $L$: the full Galois group is abelian, and (754M.4)
cancels in numerator and denominator. The seven-term expression is
the full $\theta$ projector on $1/r$, multiplied by $r$; all omitted
cosets contribute the same term. Because
$\sigma_\gamma^7r=\theta(\gamma)^{-7}r$, cyclically shifting the
seven summands is valid, including the last one. It gives, for every
$c\in\mathbf F_{p^2}^{\times}$,

$$
\boxed{\quad\sigma_c z_*=
\theta(c)\frac{\sigma_c r}{r}\,z_* .\quad}
\tag{754M.6}
$$

This identity is independent of the representative modulo $\mu_6$,
since (754M.4) cancels the extra unit character. It therefore applies
to every automorphism of $M_0/K$ in the trace below.

Nonvanishing has a direct original normalization proof. R725's
leading tame ratio is
$\sigma_c r/r\equiv c^{p-1}=\theta(c)^{-1}$ at the specified
$p$-adic embedding. Hence every summand in (754M.5) is congruent
to one, and $z_*\equiv1$ modulo the maximal ideal. In particular
$z_*\ne0$. This does not assume any L-value nonvanishing.

For computation, if $R_c=X([c]P')/X(P')$ and
$U_c=U/R_c^3$, the retained formula $r\propto X(P')U^7S(U)$ gives

$$
\frac{\sigma_c r}{r}=R_c^{-20}\frac{S(U_c)}{S(U)}.
\tag{754M.7}
$$

Only $c=\gamma$ is needed in the large field. Compute its point by
the original $E_{27}$ group law, compute $\sigma_\gamma b=b(U_\gamma)$,
and verify that both (754M.7) and $\sigma_\gamma b$ descend to the
retained basis $1,b,\ldots,b^6$ by substitution in **all** 280
coordinates. After that, the seven ratios are generated entirely
in $L$ by

$$
a_0=1,\qquad a_{j+1}=a_1\sigma_\gamma(a_j),\qquad
a_7=\zeta^2,
\tag{754M.8}
$$

because $\theta(\gamma)^7=\eta^{14}=\zeta$.
The code checks $\sigma_\gamma^7(b)=b$ and the exact covariance
(754M.6) for this generator.

We use the small tower

$$
\nu=\eta^6=\zeta_7,\qquad
A=K(\nu),\quad\Phi_7(\nu)=0,\qquad
\eta=-\zeta^2\nu^6.
\tag{754M.9}
$$

The degree-six cyclotomic polynomial over $K$ stays irreducible
over $L$, since $L/K$ has degree seven. In fact $A$ is ramified at
seven and $\mathcal M$ is unramified there, so $A\cap\mathcal M=K$.
Thus $LA/L$ is exactly degree six. The program inverts $z_*$ in
this $7\times6$ tower by polynomial Euclid and checks the exact
product one. It never constructs a degree-3360 coordinate algebra.

## 3. The complete period sum as forty exact traces

R751 has already proved the full 280-orbit expression with the
original inverse character and positive additive phase. Its exact
equivalent is

$$
\boxed{
Z_a=-\frac{3\zeta}{p}\,z_*
\operatorname{Tr}_{M_0A/A}
       \left(\frac{H(U)\xi^{9a}}{z_*}\right),
\qquad \xi=e^{2\pi i/p}.
}
\tag{754M.10}
$$

Here the trace is the **unnormalized field trace**: there is no
additional $1/280$, $1/40$ or $1/7$.
For completeness, (754M.7) and $U_c=U/R_c^3$ imply

$$
\frac{z_*}{\sigma_c z_*}\,\sigma_c H
=\theta(c)^{-1}U^7S(U)
       \frac{R_c^2}{R_c^3+U}.
\tag{754M.11}
$$

Also $\sigma_c\xi=\xi^{Nc}$ by Weil pairing. Summing (754M.11)
over $\operatorname{Gal}(M_0/K)$ recovers every original weighted
$\mu_6$ orbit of R751.29. The scalar in (754M.10) is precisely
R751.38 after multiplying by $R_C\alpha\sqrt{-3}$.
This proves (754M.10) with the original target phase.

In particular $Z_a\in LA$. This descent is also the period version
of the original $L$-isogeny $A_{\theta,1,L}\sim C^6$ from R725.
For the rational Hodge basis of R745 all the target-normalized
periods are therefore in $L$: expand each original differential
in an $L$-basis of pullbacks from these six elliptic projections;
their normalized periods are in $K$.

Write the already computed inverse as

$$
z_*^{-1}=\sum_{i=0}^{5}\sum_{j=0}^{6}
             c_{ij}b^j\nu^i,\qquad c_{ij}\in K.
\tag{754M.12}
$$

Only the following 280 small trace values are necessary:

$$
T_{j,a}=\operatorname{Tr}_{M_0/K}
              (H b^j\xi^{9a}),\qquad0\le j\le6,
\quad1\le a\le40.
\tag{754M.13}
$$

Then the trace in (754M.10) is
$\sum_i(\sum_jc_{ij}T_{j,a})\nu^i$. This replaces a large
compositum calculation by seven fixed functionals and forty powers.

Each functional uses the exact Lagrange trace formula from R735:

$$
\operatorname{Tr}_{M_0/K}(f)
=[U^{279}](fP'(U)\bmod P(U)).
\tag{754M.14}
$$

For $j=0,\ldots,6$, first compute
$D_j=H b^jP'(U)\bmod P$. The vector
$w_{j,r}=[U^{279}](U^rD_j\bmod P)$, $0\le r\le279$,
is built by repeated multiplication by $U$ and exact reduction.
Since $H,b,P$ have rational coefficients, these seven vectors
are rational. If $\xi^{9a}=A_a(U)+\zeta B_a(U)$, then

$$
T_{j,a}=\sum_rw_{j,r}[U^r]A_a
        +\zeta\sum_rw_{j,r}[U^r]B_a.
\tag{754M.15}
$$

No approximate interpolation, Fourier transform, or rounding enters
these traces. Each completed functional and the forty powers are
saved as separate compatible checkpoints.

## 4. The original Weil-pairing root without a coordinate extension

R751.30–32 fixes the positive root by monic Miller functions and
the sigma/Legendre relation:
$e_p(P',[\zeta]P')=e^{2\pi i/p}$.
For monic $f_P$ with divisor $p(P)-p(O)$,

$$
f_{\zeta P}(R)=\zeta^{-p}f_P(\zeta^2R).
$$

Consequently

$$
\boxed{\xi=-\zeta^{41}
              \frac{f_{P'}(\zeta P')}{f_{P'}(\zeta^2P')}.}
\tag{754M.16}
$$

This is computed directly in $K(U)$. Represent a multiple of $P'$
by $(X R,Y S)$, where $X=X(P'),Y=Y(P')$ and
$D=Y^2/X^3=1+U/4$. Ordinary addition has normalized slope
$m=(S_B-S_A)/(R_B-R_A)$; doubling has
$m=3R_A^2/(2D S_A)$. Its output is

$$
R_{A+B}=Dm^2-R_A-R_B,\qquad
S_{A+B}=-S_A+m(R_A-R_{A+B}).
\tag{754M.17}
$$

At the two evaluation points $(\zeta X,Y)$ and $(\zeta^2X,Y)$,
the common $Y/X$ in each line/vertical quotient cancels. For
$A+B\ne O$ the ratio is

$$
\frac{1-S_A-m(\zeta-R_A)}{\zeta-R_{A+B}}
\left(\frac{1-S_A-m(\zeta^2-R_A)}{\zeta^2-R_{A+B}}\right)^{-1}.
\tag{754M.18}
$$

For $A+B=O$ use the full vertical-line ratio
$(\zeta-R_A)/(\zeta^2-R_A)$. The last step of the binary Miller
chain for 41 is exactly such a step. Both evaluation points are
independent from the rational cyclic subgroup generated by $P'$,
so the indicated values and denominators do not vanish.

Every monic normalization factor is common to the two evaluations
of the **same** $f_{P'}$ and cancels. The factor $-\zeta^{41}$
in (754M.16) remains explicit. The code checks $\xi^{41}=1$,
$\xi\ne1$, and the full cyclotomic relation, while its exact
orientation is the proof of R751, not these order checks alone.
Replacing $P'$ by the real $E_{27}$ point would change the pairing
by the norm-three power and is expressly excluded.

## 5. The same finite vectors and all original edge periods

The only new finite matrix is the Weyl action (R751.5), in the
original character and gauge. It transports the **saved** R745
vector; no torus average or norm is re-enumerated.
The exact Bruhat formula of R751.8 computes

$$
u_g=\rho(g_p^{-1})u
   =\sum_{r=1}^{40}\frac{d_{g,r}}{41\cdot42}e_r.
\tag{754M.19}
$$

The arithmetic checks that the apparent additional Weyl denominator
41 cancels coefficient by coefficient in $\mathbf Z[\eta]$.
For every original positive Manin edge, the actual $g_2,g_3$
give $x_g,y_g,\chi_g$ by the original tame matrices and graph.
With $a_r\equiv-r/6\pmod{41}$, R751.14 becomes

$$
\boxed{
\Pi_{j,g}:=\frac{R_C}{\Omega_0}\int_{g0}^{g\infty}\omega_j
=-\frac{\chi_g}{7}\operatorname{Tr}_{A/K}
\left(\beta^j\sum_{r=1}^{40}d_{g,r}
            (x_gZ_{a_r}+y_gZ_{4a_r})\right)\in L.
}
\tag{754M.20}
$$

The trace here is relative degree six. In the $\nu$ basis its
values are $\operatorname{Tr}(1)=6$ and
$\operatorname{Tr}(\nu^i)=-1$ for $1\le i\le5$.
The global forms are those of R745; no second $\zeta^2$ is inserted
for $c_1$ during a global period calculation.

The 819 original edges and all 800 compact chains are read in their
retained order. Each closed period is the signed sum using precisely
the saved integer chain coefficients. The original intersection
matrix and topology are not regenerated.

## 6. Streamed exact constraints and complete kernel verification

Write an unknown original differential combination as

$$
v_j=\sum_{t=0}^{6}x_{jt}b^t,\quad x_{jt}\in K,
\qquad\sum_{j=0}^{5}v_j\omega_j.
\tag{754M.21}
$$

There are 42 variables. Because every exact $\Pi_{ji}$ is in
$L=K(b)$, the nonconstant coefficients of
$\sum_jv_j\Pi_{ji}$ give **six rows per original closed chain**:

$$
M_{(i,a),(j,t)}=[b^a](b^t\Pi_{ji}\bmod F_{41}(b)),
\quad 1\le a\le6,\quad1\le i\le800.
\tag{754M.22}
$$

This is a $4800\times42$ matrix over $K$. It represents exactly
the same original period condition as R751.44; no constraint is
discarded. It is streamed through an exact reduced row-echelon
basis, saving every independent source row and periodic checkpoints.
After rank 36 is reached, every remaining row still has to reduce
to zero. A computed rank different from 36 is a failed computation,
not a license to change phase or normalize a period.

The six kernel columns are then independently substituted into all
800 saved closed period vectors. The result must have only its
constant $b$ coefficient for every column and every chain. The full
$800\times6$ array of actual periods in $K$ is saved. Thus neither
the proven dimension in R732 nor early attainment of rank is being
reported as an unperformed numerical verification.

Finally, for each kernel vector, take the exact least common multiple
of denominators of its two $K$ coordinates over all 800 periods.
The resulting integer $N$ is saved and all multiplied coordinates
are checked to lie in $\mathbf Z[\zeta]=\mathcal O_K$.
By R732 these give actual integral-period differential inputs for
maps $X_1\to C$, based at the original $c_0$. No $N$ is assumed to
be a 41-unit. Rational functions, $\beta$ coordinates, map degrees
and the original height connection remain subsequent computations.

## 7. Retention, resources and resumability

The fixed inputs are the six files and exact SHA-256 values listed
in the source's `FIXED` dictionary, from R735 run `43608152850`,
R738 run `43612108090`, and R745 run `43616027318`.
The wrapper downloads those existing public artifacts, verifies the
listed hashes and records source, method, request, current README
hashes and all referenced result hashes.

The large arithmetic uses degree 280 only; the small fields use
degrees seven and six. Substitution uses baby-step/giant-step
polynomial evaluation. The largest cached objects are exact
degree-280 coordinates, seven trace vectors, 41 root-of-unity
powers, and the small-coordinate edge/closed period tables.
No floating point precision parameter exists.

The exact source/configuration is bound into every checkpoint.
Miller steps, the large-field gamma descent, the small projector,
each trace functional, additive periods, finite edge vectors,
relative periods, streamed constraints, and the final 800-chain
verification are independently retained. A compatible continuation
reads completed stages. A completed final certificate is reused after
all its stage hashes are checked.

The initial public core budget is 80 minutes. On timeout or any
failed assertion, all completed and partial exact files are uploaded,
and the small run receipt records incomplete status. A subsequent
request can name that public artifact and its manifest SHA to
continue the same source. Time limits are checkpoint boundaries,
not mathematical completion.

Only small receipts, the final small certificate, source/method and
the full file/hash manifest are published into Git. Reproducible
coordinates stay in the Actions artifact. No old target model,
old topology, old torus average or old L-value certificate is rerun.

## Dependencies

- R751: complete positive-period kernel, original inverse character,
  exact Miller orientation, actual target phase, and degree-280 field.
- R725/R735: the actual $r_0,b$, full $p$-torsion Galois group,
  tame leading ratio, retained model products and polynomial.
- R732: exact characterization of the original Hom kernel and the
  role of integral periods in rational-function reconstruction.
- R738/R745: the unchanged original chains, markings, full tame
  descent, rational Hodge basis and finite vector.
- Python-FLINT 0.9.0, rational/integer polynomial API:
  https://python-flint.readthedocs.io/en/latest/fmpq_poly.html and
  https://python-flint.readthedocs.io/en/latest/fmpz_poly.html.
