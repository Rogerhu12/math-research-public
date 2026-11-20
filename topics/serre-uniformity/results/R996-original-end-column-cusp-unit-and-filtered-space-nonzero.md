# R996 — An actual end-column cusp unit and a nonzero filtered space

Date: 2026-11-20. Author: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved.** For every original allowed prime \(p\ge41\) with \(5\nmid p+1\), the actual primitive/Legendre filtered full-level space \(V_p\) of R992 is nonzero. A specified retained original column has the exact cusp constant \(233/(p-7)!\). The sole possible prime divisor of that numerator is excluded by the original condition modulo nine.

This proves the nonzero-space hypothesis in R992 for this entire subfamily. It does not prove that this column has nonzero CM marked value, that \(V_p\) is preserved by \(\mathcal G\), or that the original same-label product is a unit. A complete cusp formula for all original columns is also supplied, with the Gaussian and canonical-zeta terms retained. No new mathematical execution or finite prime window is used.

## 1. The complete original norm-one cusp source

Use exactly R966/R968, with

\[
\mathscr J(u,v;\tau)
=\frac{e^{-E_2uv/2}}{6\eta^4}
\sum_{\alpha\in\mathbf Z[\zeta]}
\epsilon_{2s}(\alpha)e^{\alpha u+\bar\alpha v}Q^{N\alpha},
\qquad Q=e^{2\pi i\tau/6}.
\tag{996.1}
\]

The algebraic Taylor variables and the positive CM embedding are those of R968. In particular \(\epsilon_{2s}(\epsilon)=\epsilon^{-1}\) for \(\epsilon\in\mu_6\). The only lattice elements of norm one are precisely those six units, and \(\eta^4=Q(1+O(Q^6))\). Since \(E_2\) has constant term one, the exact constant Fourier coefficient, with \(q=Q^6\), is

\[
\boxed{\quad
[q^0]\mathscr J(u,v)
=\frac16e^{-uv/2}
\sum_{\epsilon\in\mu_6}
\epsilon^{-1}e^{\epsilon u+\epsilon^{-1}v}.
\quad}
\tag{996.2}
\]

All six terms are included. The Gaussian has not been dropped, and no single norm-one term is being used in place of its complete unit orbit.

For \(T_{a,l}=[u^a v^l]\mathscr J\), expansion of (996.2) gives

\[
\boxed{\quad
[q^0]T_{a,l}
=\mathbf1_{a-l\equiv1\ (6)}
\sum_{t=0}^{\min(a,l)}
\frac{(-1/2)^t}{t!(a-t)!(l-t)!}.
\quad}
\tag{996.3}
\]

Indeed the unit factor of every summand is \(\epsilon^{a-l-1}\), independently of the Gaussian index \(t\). Its average is exactly the displayed indicator. Formula (996.3) is an exact rational identity in characteristic zero; the integral ranges below permit its stated reductions.

## 2. The specified end column

Let

\[
p=6N+5\ge41,\qquad p\equiv2,5\pmod9,
\qquad i=N-1,\quad j=0.
\tag{996.4}
\]

Then the unchanged R968 indices are

\[
a=6i+4=p-7,\qquad b=6j+1=1.
\]

In R968(968.9), the two zeta correction sums are empty for \(b=1\). Thus the complete actual column is exactly

\[
\boxed{Z_{p-7,1}=12T_{p-7,3}.}
\tag{996.5}
\]

This equality includes the leading Laurent terms of the canonical-zeta operator; their contribution is the coefficient \((1-4)(1-5)=12\). It is not an omission of that operator.

For \(a=p-7\), the congruence \(a-3\equiv1\pmod6\) holds. Multiplying (996.3) by \(a!3!\), one obtains the four-term identity

\[
\begin{aligned}
a!3![q^0]T_{a,3}
&=1-\frac{3a}{2}
+\frac{3a(a-1)}4
-\frac{a(a-1)(a-2)}8\\
&=\frac{8-20a+9a^2-a^3}{8}.
\end{aligned}
\tag{996.6}
\]

Every factorial here is a \(p\)-unit. Substituting \(a\equiv-7\pmod p\) gives

\[
\frac{8-20(-7)+9(-7)^2-(-7)^3}{8}
=\frac{233}{2}.
\]

Multiplication by \(12/3!=2\) in (996.5) therefore proves

\[
\boxed{\quad
[q^0]Z_{p-7,1}
=\frac{233}{(p-7)!}\pmod p.
\quad}
\tag{996.7}
\]

The integer \(233\) is prime: none of the primes \(2,3,5,7,11,13\), which are all the primes at most \(\sqrt{233}\), divides it. Moreover \(233\equiv8\pmod9\), so it is absent from (996.4). Hence (996.7) is a unit for every original prime under consideration. In particular this actual full-level column is globally nonzero for every such prime, without any condition modulo five.

## 3. Both original filters on that same column

The label of the column in §2 is exactly

\[
h=6i+7=p-4.
\tag{996.8}
\]

Its primitive condition is

\[
\gcd(h,p+1)=\gcd(p-4,p+1)=\gcd(5,p+1).
\tag{996.9}
\]

The original Legendre degree is \(h-1=p-5\). The already used finite Legendre reflection gives

\[
P_{p-5}(x)=P_4(x)\quad\text{in }\mathbf F_p[x].
\]

For completeness this instance follows from the finite hypergeometric parameters: \((-(p-5),p-4)\) reduce to \((5,-4)\), the parameters of \(P_4\) in the opposite order. Every later coefficient has the numerator factor \(p\), while its factorial denominator is a unit up to the original degree \(p-5<p\).

At the unchanged point \(x=1/s\), \(s^2=-3\), the value is

\[
\begin{aligned}
P_4(1/s)
&=\frac{35(1/s)^4-30(1/s)^2+3}{8}\\
&=\frac{35/9+10+3}{8}
=\frac{19}{9}.
\end{aligned}
\tag{996.10}
\]

This is a unit for \(p\ge41\). Thus if \(5\nmid p+1\), the original mask on this same column is exactly

\[
w_{N-1}=P_{p-5}(1/s)=19/9\ne0.
\]

Combining (996.7)–(996.10) proves the promised full-family statement:

\[
\boxed{\quad
p\ge41,\quad p\equiv5\pmod6,\quad
p\equiv2,5\pmod9,\quad5\nmid p+1
\quad\Longrightarrow\quad V_p\ne0.
\quad}
\tag{996.11}
\]

The nonzero member is the actual retained column
\(w_{N-1}Z_{p-7,1}\), not a different linear combination with an unverified label. Its cusp constant is

\[
[q^0]\bigl(w_{N-1}Z_{p-7,1}\bigr)
=\frac{19\cdot233}{9(p-7)!}\ne0.
\tag{996.12}
\]

When \(5\mid p+1\), the underlying column is still globally nonzero by (996.7), but its original primitive mask is zero. No conclusion about \(V_p\) is drawn from it in that branch.

## 4. A complete reduced cusp formula for every critical column

This section records a precise formula for studying the remaining branch. It does not assert that its coefficients never vanish.

Let \(a=6i+4\), \(b=6j+1\), \(i+j=N-1\). Then

\[
a+b=p-6,\qquad a\equiv-b-6\pmod p.
\tag{996.13}
\]

For a fixed nonnegative integer \(l<p\), multiply the summand in (996.3) by \(a!\). The falling factorial of \(a\) becomes

\[
(-1)^t a(a-1)\cdots(a-t+1)
\equiv(b+6)(b+7)\cdots(b+5+t)\pmod p.
\tag{996.14}
\]

If \(t>a\), the right side contains the factor \(a+b+6=p\); it is then zero modulo \(p\). Therefore the sum can be extended through \(t=l\), without adding a nonzero term. Define the finite coefficient source

\[
S_b(v)=e^v(1-v/2)^{-b-6},\qquad
\Pi_3S_b=\sum_{l\equiv3\ (6)}[v^l]S_b\,v^l.
\tag{996.15}
\]

All uses of this series below are truncated through degree \(b+2\). Equation (996.3) becomes exactly

\[
\boxed{\quad
a![q^0]T_{a,l}
=\mathbf1_{l\equiv3\ (6)}[v^l]S_b(v)
\pmod p.
\quad}
\tag{996.16}
\]

The canonical cusp zeta function is

\[
\zeta_0(v)=\frac12\coth(v/2)-\frac v{12}
=\frac1v+\sum_{n\ge2}\frac{B_{2n}}{(2n)!}v^{2n-1}.
\tag{996.17}
\]

It is the constant Fourier coefficient of exactly the zeta function used in R968. In particular its linear term is zero. Taking the constant term of the complete finite expression R968(968.9), and using (996.16), proves

\[
\boxed{\quad
a![q^0]Z_{a,b}
=[v^b]\left(\partial_v-6\zeta_0(v)\right)^2
\Pi_3\left(e^v(1-v/2)^{-b-6}\right)
\pmod p.
\quad}
\tag{996.18}
\]

The operator, including its Laurent terms, is applied before the displayed coefficient is taken. In particular (996.18) is not the expression obtained by applying the Gaussian sum alone. Its three sources are fixed: the original unit-orbit projection, the complete Gaussian, and the original canonical-zeta operator.

Every denominator in this reduction is controlled. One has

\[
b+2\le p-8<p,
\qquad 2n\le b+2<p-1
\]

for the weighted Bernoulli coefficients occurring in R968's finite formula. Thus all Taylor factorials and the needed Bernoulli denominators are units at \(p\). No full infinite zeta or exponential series is being reduced outside this finite range.

One may remove the double Bernoulli convolution in (996.18) without changing its source. Put

\[
\wp_0(v)=\frac1{12}+\frac1{4\sinh^2(v/2)}=-\zeta_0'(v).
\]

The elementary identities \(\coth^2-\operatorname{csch}^2=1\) and (996.17) give

\[
\zeta_0^2
=\wp_0+\frac16-\frac{v\zeta_0}{6}-\frac{v^2}{144}.
\tag{996.19}
\]

Consequently the very same squared operator is

\[
\boxed{\quad
(\partial_v-6\zeta_0)^2
=\partial_v^2-12\zeta_0\partial_v
+42\wp_0+6-6v\zeta_0-v^2/4.
\quad}
\tag{996.20}
\]

This is an identity of operators in which the second and later terms have the indicated order. It can be used in (996.18) to give a formula involving only single Bernoulli coefficients. It does not identify (996.18) with the original Legendre factor, and no such identification is assumed.

## 5. Exact consequence and remaining boundary

For the primes in (996.11), the first hypothesis \(V_p\ne0\) in R992's conditional criterion has now been proved in the actual source. Thus on this subfamily, a proof of the still-open invariance

\[
\mathcal G(V_p)\subset V_p
\]

would imply that some one original admissible label has all three original factors nonzero. Invariance itself is not proved here.

The distinction between cusp and CM mark remains essential. At the CM mark the end column is, by R968,

\[
\left[Z_{p-7,1}/E_6^N\right]_{\rm mark}
=-72(-864)^{-N}f_{N-1}g_0
=-72(-864)^{-N}f_{N-1}.
\tag{996.21}
\]

Its cusp constant (996.7) does not prove the last quantity is a unit. Likewise the column does not survive the original primitive mask when \(5\mid p+1\). Formula (996.18) preserves that remaining arithmetic support problem rather than replacing it by an unfiltered assertion.

## Sources and dependencies

- [R966](R966-single-conductor-two-s-CM-kernel-and-original-critical-jet.md): the exact conductor-\((2s)\) finite character, actual unit action, and unchanged original labels.
- [R968](R968-full-level-mixed-CM-jet-and-critical-factor.md): the Gaussian-normalized full-level source, complete canonical-zeta coefficient formula, finite integrality bounds, and exact marked scalar.
- [R971](R971-complete-Wilson-Fourier-source-and-filtered-span-obstruction.md): the full original Fourier source and why a single Gaussian summand cannot stand for the complete column. Here its entire norm-one orbit is taken explicitly in (996.2)–(996.3).
- [R992](R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md): the actual filtered space and the separate nonzero-space and invariance hypotheses.
- [R734](R734-primitive-unit-toric-norm-at-every-prime.md): the previously used finite Legendre identities and the separate original visibility problem. The specific reflection and value needed here are proved directly in §3.

The new conclusion is the specified global cusp unit and the resulting nonzero actual filtered space for \(5\nmid p+1\), together with the complete reduced cusp source for the other columns. The CM marked nonvanishing, the original rational-point exclusion, and the main Serre-uniformity goal remain open.
