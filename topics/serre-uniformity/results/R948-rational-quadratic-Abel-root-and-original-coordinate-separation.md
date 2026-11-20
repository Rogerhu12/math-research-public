# R948 — Rational quadratic Abel root and separation by another original coordinate

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved.** At the two original central labels in R945, its unique Hensel parameter actually belongs to $p\mathbf Z_p$, although the chosen good formal coordinate was originally written over $R_0$. The characteristic-zero linear jet determines whether this parameter is zero and, when nonzero, determines its exact valuation. The alternative original coordinates already proved nonzero in R945 exclude this second scalar root from the common Abel zero locus. These are finite-prime statements and do not exclude the original positive-rank rational-point candidates.

No new arithmetic is performed here. The only finite inputs are precisely R945's already computed central first and second coefficients and its same-label alternatives. All references to zero loci use the original centered increment $\gamma(P)=q([P-c_1])$, the original coarse parameter $a$, and
$$
w=\frac{a-1}{p^3}.
\tag{948.1}
$$

## 1. Statement

Use one of
$$
(p,h)=(227,115),\qquad (p,h)=(857,433).
\tag{948.2}
$$
Let $w_*$ be the unique root supplied by R945 §3 after dividing the original calibrated component by $w$. Then
$$
\boxed{w_*\in p\mathbf Z_p.}
\tag{948.3}
$$
Write $M_{m,h}$ for the actual original flat Hodge jets of R727/R925, and put $\nu_h=v_p(N_h)$ for the unchanged finite norm. The following alternatives are exact:

- If $M_{2,h}=0$ in characteristic zero, then $w_*=0$ and the original scalar Abel component has a double zero at the center.
- If $M_{2,h}\ne0$, then $w_*\ne0$, both scalar zeros are simple, and
  $$
  \boxed{
  v_p(w_*)=2+v_p(M_{2,h})-\nu_h/2\ge1.
  }
  \tag{948.4}
  $$

The only zeros of this scalar component in the algebraically closed complete open disc $v_p(w)>0$ are $0$ and $w_*$, counted with multiplicity. At the two primes (948.2), the original central Legendre factor is a unit, so $\nu_h=0$. In particular the new second-coefficient information gives
$$
v_p(M_{5,h})=-5,\qquad
M_{2,h}=0\ \text{or}\ v_p(M_{2,h})\ge-1.
\tag{948.5}
$$
If $w_*\ne0$, its original coarse parameter satisfies
$$
a_*=1+p^3w_*\in1+p^4\mathbf Z_p,
\qquad
v_p(a_*-1)=5+v_p(M_{2,h}).
\tag{948.6}
$$

Now choose the *other original* label
$$
h'=151\quad(p=227),\qquad h'=445\quad(p=857).
\tag{948.7}
$$
Its original scalar Abel component has only the center as a zero on $v_p(a-1)>3$. Therefore, if the central component has $w_*\ne0$, the component at $h'$ is nonzero there. In fact the common zero locus of these two original scalar components, and hence the zero locus of the full original Abel increment in this original open disc, is exactly the center:
$$
\boxed{
\gamma(P)=0,\quad v_p(a(P)-1)>3
\quad\Longrightarrow\quad P=c_1
}
\tag{948.8}
$$
within the original parametrized branch. The converse holds by centering.

The statement $w_*\in\mathbf Q_p$ is about the calibrated parameter. It neither supplies a $\mathbf Q$-rational point of the original curve nor asserts that the central scalar root kills all other coordinates. Also, the original rational-point candidates are not known to satisfy $\gamma(P)=0$: they may have a nonzero image on the retained Mordell–Weil line. Thus (948.8) is not their exclusion.

## 2. A rational normalization retaining the absolute period and the Tate index

We give the descent argument rather than assuming that the coefficients of the chosen good coordinate $Y_h$ lie in $\mathbf Q_p$.

Keep the notation of R925:
$$
E_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!},
\qquad
J=\deg Q_h,
\qquad E_{J,h}\ne0.
\tag{948.9}
$$
The original flat/coarse change is
$$
V=\frac{z_{\rm f}^3}{p^3}=\Psi(w),
\qquad
\Psi\in w\mathbf Z_p\langle w\rangle,
\qquad \Psi(w)\equiv\frac38w\pmod p,
\tag{948.10}
$$
with its integral analytic inverse. It is independent of the coefficient embedding $h$.

R857 §2 and R925 §3 prove that the actual component differential is defined over $\mathbf Q_p$, with one common comparison scalar for all of its flat jets. Indeed the real Hecke field is contained in $\mathbf Q(\zeta_{p+1})^+$ and is split at $p$, because $p\equiv-1\pmod{p+1}$. The same original comparison and rational flat/coarse inverse give
$$
\frac{M_{3j-1,h}}{M_{3J-1,h}}\in\mathbf Q_p
\qquad(j\ge1).
\tag{948.11}
$$
No value is assigned to the absolute period or to its common comparison scalar. Taking the ratio cancels the *same* scalar at every index, rather than choosing independent phases for the sigma square roots.

Let $c_h^{\rm cal}$ be exactly R925's scalar, so the original calibrated logarithm is
$$
\Lambda_h(w)
=c_h^{\rm cal}\sum_{j\ge1}E_{j,h}\Psi(w)^j.
\tag{948.12}
$$
R925(925.27), including its infinite tail, proves that
$$
\frac{c_h^{\rm cal}}{p^{a_h}}\sum_{j\ge1}E_{j,h}V^j
\in VR_0\langle V\rangle,
\qquad
u_h:=\frac{c_h^{\rm cal}E_{J,h}}{p^{a_h}}\in R_0^\times.
\tag{948.13}
$$
The original index $a_h$ remains in this formula. In particular neither $c_h^{\rm cal}$ nor $E_{J,h}$ is being declared a unit or an element of $\mathbf Q_p$.

By (948.11), every $E_{j,h}/E_{J,h}$ lies in $\mathbf Q_p$. By (948.13), it is integral in $R_0$ and tends to zero as $j\to\infty$. The intersection $R_0\cap\mathbf Q_p=\mathbf Z_p$ therefore gives
$$
\Phi_h(w):=\sum_{j\ge1}\frac{E_{j,h}}{E_{J,h}}\Psi(w)^j
\in w\mathbf Z_p\langle w\rangle.
\tag{948.14}
$$
Moreover,
$$
p^{-a_h}\Lambda_h=u_h\Phi_h,
\qquad Q_h=\bar u_h\,\bar\Phi_h.
\tag{948.15}
$$
These are identities using the original normalization. The first scalar is nonzero and the displayed $u_h$ is a proved integral unit, so passage to $\Phi_h$ changes neither the characteristic-zero scalar zero locus nor its multiplicities.

## 3. Exact quadratic Hensel analysis

R945 proves $q_{h,1}=0$ and $q_{h,2}\ne0$ for (948.2). Equation (948.15) consequently gives
$$
\Phi_h(w)=w\bigl(c_1+c_2w+c_3w^2+\cdots\bigr),
\quad c_1\in p\mathbf Z_p,
\quad c_2\in\mathbf Z_p^\times,
\quad c_j\in\mathbf Z_p,
\tag{948.16}
$$
where the coefficients tend to zero. Put $H(w)=\Phi_h(w)/w$. Hensel's lemma over $\mathbf Z_p$ gives a root $w_*\in p\mathbf Z_p$ because $H(0)\in p\mathbf Z_p$ and $H'(0)=c_2$ is a unit.

This is also the only root of $H$ in the entire open unit disc over $\mathbf C_p$. If $v_p(x)>0$ and $v_p(y)>0$, then
$$
H(x)-H(y)=(x-y)\left(c_2+
\sum_{n\ge2}c_{n+1}\sum_{i=0}^{n-1}x^iy^{n-1-i}\right).
\tag{948.17}
$$
The bracket is a unit: every term after $c_2$ has positive valuation, and the series converges. Thus two roots in that disc must coincide. Also $H'(w_*)$ is a unit, so that root is simple.

If $c_1=0$, then $w_*=0$ and the extra factor $w$ in (948.16) makes the scalar zero double. If $c_1\ne0$, then $w_*\ne0$; the center and $w_*$ are both simple scalar zeros. The equation $H(w_*)=0$ and the unit $c_2$ give
$$
v_p(w_*)=v_p(c_1),
\tag{948.18}
$$
since the terms of degree at least two have valuation strictly greater than $v_p(w_*)$.

It remains to identify $c_1$ without replacing the original jet by a residue-field surrogate. From (948.10) and (948.14),
$$
c_1=\Psi'(0)\frac{E_{1,h}}{E_{J,h}},
\qquad \Psi'(0)\in\mathbf Z_p^\times.
\tag{948.19}
$$
R925(925.37) gives
$$
v_p(E_{J,h})=1+\nu_h/2,
\qquad E_{1,h}=p^3M_{2,h}/6.
$$
Thus $c_1=0$ if and only if the actual characteristic-zero $M_{2,h}=0$, and otherwise
$$
v_p(c_1)=2+v_p(M_{2,h})-\nu_h/2.
\tag{948.20}
$$
This proves (948.3–4). The residue values $f_i g_j=0$ alone do not decide whether $M_{2,h}$ is zero in characteristic zero.

The second coefficient of (948.14) is
$$
c_2=\frac{E_{1,h}}{E_{J,h}}[w^2]\Psi
    +\frac{E_{2,h}}{E_{J,h}}\Psi'(0)^2.
$$
Its first term is divisible by $p$, and its second multiplier is a unit. Hence $E_{2,h}/E_{J,h}$ is a unit, and
$$
v_p(M_{5,h})=-5+\nu_h/2.
\tag{948.21}
$$
At (948.2), R945's central Legendre units and R727(727.3) give $\nu_h=0$. Equations (948.20–21) prove (948.5–6).

Finally these are zeros of the original coordinate, not only of an unrelated primitive. R925 proves
$$
L_h^{\rm cal}(W)=W+pW^2V_h(W),\qquad V_h\in R_0\langle W\rangle.
$$
On the calibrated disc the original $G_h$ is integral, so
$$
\Lambda_h=L_h^{\rm cal}(G_h)
=G_h\bigl(1+pG_hV_h(G_h)\bigr)
$$
has precisely the same zeros and multiplicities as $G_h$: the factor in parentheses is a unit. The uniqueness just proved also identifies our $w_*\in p\mathbf Z_p$ with R945's root initially obtained over $R_0$.

## 4. The alternative original coordinate separates the scalar root

This step uses the exact criterion already proved in R727, rather than asserting a new lattice theorem or extending the central normal-function calculation to another label.

For the two labels (948.7), R945 proves all of the following at the **same** $h'$:

1. The label satisfies the original primitive conditions $7\le h'\le p-4$, $h'\equiv1\pmod6$, and $(h',p+1)=1$.
2. The original $P_{h'-1}(1/s)$ is a unit, hence $N_{h'}$ is a unit by R727(727.3).
3. The two original complementary sigma factors are units. Their exact R697/R683 square formulas have unit factorial and scalar multipliers in this range, so $C_{h'-2}$ and $C_{p-h'-2}$ are units.

For $p=227$ these are R945's factors $f_{24}$ and $g_{12}$ at $h'=151$; for $p=857$ they are $f_{73}$ and $g_{68}$ at $h'=445$. They are not borrowed from the central label.

R727(727.6–8) therefore gives
$$
v_p(M_{2,h'})=-2
\quad\text{and}\quad
\text{the original $h'$ scalar Abel primitive has only its central zero on }
v_p(a-1)>3.
\tag{948.22}
$$
That theorem already includes the original common phase, the one-$p$ bound for every Hodge jet, all factorial-divisible tail indices, and the exact flat/coarse change. Equivalently its rationally normalized restricted series has a unit linear coefficient, and after factoring $w$ the remaining series is a unit whenever $v_p(w)>0$.

Thus a nonzero $w_*$ from §3 cannot kill this second original coordinate. More generally any zero of the full original increment $\gamma(P)$ kills the scalar primitive obtained from every actual quotient differential, including the one at $h'$. Equation (948.22) then forces the center. This proves (948.8), without an assumption that $a_h$ or $a_{h'}$ vanishes.

## 5. Exact boundary for the main problem

There is no conflict between the two scalar descriptions. The central reduction is ramified to order two and may have a nearby characteristic-zero scalar zero. Another embedding of the same actual positive factor has a unit first scalar coefficient and separates that zero.

This settles the common Abel **zero** locus on the indicated open branch for these two finite primes. It says nothing about solutions of
$\gamma(P)\in\mathbf Z\cdot P_0$ with a nonzero Mordell–Weil image, which remain among the original positive-rank possibilities. It also supplies neither an absolute prime bound nor the original height comparison. The field descent (948.3) cannot substitute for any of those assertions.

## Dependencies and arithmetic provenance

- [R945](R945-original-central-sigma-zeros-and-same-label-alternatives.md), especially (945.3), (945.8), and §4: the two exact second coefficients and the two actual same-label alternatives. Its public run `44720732478`, job `136235472207`, source `2ca40e8720ff441fb29b700ca99e5582bb60b1a4` supplies the new finite inputs; output SHA256 `217d9ff8f89c3270b8af2d0226fabb70662bff5874c526302933feaa66e08aad`. No arrays or arithmetic are rerun here.
- [R925](R925-original-low-normal-coefficients-and-same-label-critical-jet.md), (925.20–28), (925.37), and (925.51): the actual calibrated logarithm, integral whole series, nonzero top reference, common phase, exact finite-norm valuation, and retained Tate index.
- [R857](R857-original-higher-unit-Abel-phase-and-deep-disc-root-count.md), §2: rationality of the ratios of every original Hodge jet to any nonzero reference; this is used with R925's reference, not with a different label.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md), (727.1), (727.3), and (727.6–8): the actual primitive embeddings, finite norm, first-jet criterion, and complete original open-disc zero theorem.

This proof involves no new numerical computation and does not choose an absolute period normalization or independent signs for the coefficient square identities.
