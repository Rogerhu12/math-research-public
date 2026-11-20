# R995 — The original mixed source for the first coarse CM normal jet

Date: 2026-11-20. Author: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved source identities; the filtered propagation is not proved.** This computes the first coarse normal jet of the actual R968 columns at the original CM mark. R992 detects that jet by the third Serre derivative. The complete original mixed heat equation gives an exact three-branch expression for that derivative: the first-variable functions are \(G'''\), \(uF'\), and \(F\). All Gaussian and canonical-zeta corrections are retained. The \(G'''\) branch comes from the original \(G\otimes H\) summand of R966, which the un-differentiated projection removes.

This is not a proof of invariance of the primitive/Legendre filtered span. In particular the new partner of \(G'''\) is displayed as its actual sigma expression; it is not replaced by one of the old \(f_i\) or \(g_j\). There is no new arithmetic execution or finite window.

## 1. The unchanged sources and the algebraic frame

Let \(X=E_4\), \(Y=E_6\), and use the graded Serre derivation

\[
D=-\frac Y3\partial_X-\frac{X^2}{2}\partial_Y.
\tag{995.1}
\]

It acts on each actual homogeneous coefficient with its own weight. Let \(\mathscr J(u,v)\) be exactly the Gaussian-normalized full-level source of R968(968.2), and let \(\zeta_{\rm alg}(v)\) be the canonical zero-parameter zeta function in R968(968.7). Write

\[
\nabla=\partial_v-6\zeta_{\rm alg}(v),\qquad
\Pi_4=\frac16\sum_{\epsilon\in\mu_6}\epsilon^{-4}\,[u\mapsto\epsilon u].
\]

The actual columns are

\[
Z_{a,b}=[u^a v^b]\Pi_4\nabla^2\mathscr J.
\tag{995.2}
\]

Use the original \(E_-\) algebraic frame

\[
(X,Y)=(0,-864),\qquad
E_-:\ c^2=q^3-1,\qquad
q'=2c,\quad c'=3q^2,
\tag{995.3}
\]

where the prime denotes differentiation in the ordinary original elliptic coordinate. Thus \(q=\wp\), \(c=\wp'/2\), \(\zeta'=-q\), and the sigma function satisfies \(\sigma'/\sigma=\zeta\). The letter \(c\) in this result denotes the curve coordinate \(\wp'/2\), not the complex period ratio of R968. All named sections below use the original \(c=0\) sigma normalization, where this latter zero is the quadratic sigma parameter.

Put

\[
S=\sigma^6,\qquad
F=qS,\quad G=-qcS,\quad Y_s=cS,\quad H=(q^3+2)S.
\tag{995.4}
\]

The subscript in \(Y_s\) distinguishes this section from the modular form \(Y=E_6\). R966/R968 give the exact specialized source

\[
\boxed{\quad
\mathscr J(u,v)\big|_{(0,-864)}
=\mathscr K(u,v)
=G(u)H(v)+6F(u)Y_s(v).
\quad}
\tag{995.5}
\]

This algebraic frame is obtained from R968's actual period scaling: division of a weight-\(w\) value by that period ratio to the power \(w\) sends \(E_6\) to \(-864\) and sends its full mixed source to \(\mathscr K\). It does not choose a new theta phase.

The unit characters of \(G(u)\) and \(F(u)\) are respectively \(1\) and \(4\) modulo six. Also

\[
\nabla(f\sigma^6)=f'\sigma^6,
\qquad
\nabla^2Y_s=-12G.
\tag{995.6}
\]

## 2. Three complete Serre derivatives of the mixed source

For this section keep \(X,Y\) as the modular variables and set

\[
\mathcal A=\partial_u\partial_v,
\qquad \mathcal B=uv/4,
\qquad \mathcal L=\mathcal A+X\mathcal B.
\]

Here \(\mathcal B\) is a multiplication operator. The exact R968 heat identity is

\[
6D\mathscr J=\mathcal L\mathscr J.
\tag{995.7}
\]

Since \(D\) commutes with the Taylor derivatives and \(D\mathcal L=(DX)\mathcal B\), two further applications give

\[
D^2\mathscr J
=\frac{\mathcal L^2}{36}\mathscr J
+\frac{DX}{6}\mathcal B\mathscr J,
\]

\[
D^3\mathscr J
=\frac{\mathcal L^3
+6(DX)(2\mathcal B\mathcal L+\mathcal L\mathcal B)
+36(D^2X)\mathcal B}{216}\mathscr J.
\tag{995.8}
\]

The operator order in (995.8) is part of the formula. In particular one cannot replace the middle term by three copies of either product. At \(X=0\), \(DX=-Y/3\) and \(D^2X=X^2/6=0\). Moreover

\[
\mathcal A\mathcal B
=\mathcal B\mathcal A
+\frac14(u\partial_u+v\partial_v+1).
\]

Thus the exact specialization is

\[
\boxed{\quad
216D^3\mathscr J\big|_{X=0}
=\left\{\partial_u^3\partial_v^3
-\frac Y2\left(3uv\partial_u\partial_v
+u\partial_u+v\partial_v+1\right)\right\}
\mathscr J\big|_{X=0}.
\quad}
\tag{995.9}
\]

The lower jets have a useful character property. In the original frame,

\[
D\mathscr J=\mathcal A\mathscr K/6,
\qquad
D^2\mathscr J
=\mathcal A^2\mathscr K/36+12uv\mathscr K.
\tag{995.10}
\]

The first of these has first-variable characters \(0,3\). The two terms of the second have characters \(5,2\) and \(2,5\), respectively. Consequently

\[
\boxed{\quad
\Pi_4D\mathscr J\big|_{(0,-864)}
=\Pi_4D^2\mathscr J\big|_{(0,-864)}=0.
\quad}
\tag{995.11}
\]

These are identities of the complete specialized two-variable series. They do not say that the same projected derivatives vanish away from the CM point.

Applying (995.9) to (995.5), with \(Y=-864\), gives

\[
\begin{aligned}
\Pi_4D^3\mathscr J\big|_{(0,-864)}
={}&\frac1{216}G'''(u)H'''(v)\\
&+12uF'(u)\bigl(3vY_s'(v)+Y_s(v)\bigr)\\
&+12F(u)\bigl(vY_s'(v)+Y_s(v)\bigr).
\end{aligned}
\tag{995.12}
\]

The \(G'''\otimes H'''\) term is the third mixed derivative of the original first tensor in (995.5). Its first-variable character is \(1-3\equiv4\), so it now survives the unchanged projection. The other two branches come from the complete lower-order part of (995.9).

## 3. All canonical-zeta corrections

The original canonical sigma heat identity, with the same graded Serre convention, is

\[
D\sigma_{\rm alg}
=\frac12\sigma_{\rm alg}''
+\frac{Xv^2}{288}\sigma_{\rm alg}.
\tag{995.13}
\]

It follows by applying the usual theta heat equation to
\(\sigma_{\rm alg}=e^{-E_2v^2/24}\theta(v)/\theta'(0)\), in the algebraic theta variable. The normalization of the derivative at zero contributes \(\Theta\log\theta'(0)=E_2/8\); combining it with the Gaussian gives exactly (995.13). Its logarithmic derivative is

\[
D\zeta_{\rm alg}
=\frac12\zeta_{\rm alg}''
+\zeta_{\rm alg}\zeta_{\rm alg}'
+\frac{Xv}{144}.
\tag{995.14}
\]

There is no extra linear term in the canonical zeta function. Let

\[
P_j(v)=\left.D^j\zeta_{\rm alg}(v)\right|_{(0,-864)},
\qquad j=1,2,3.
\]

These are specified Serre jets of the same source. They can be written entirely in the original elliptic functions:

\[
\boxed{\begin{aligned}
P_1={}&-c-\zeta q,\\
P_2={}&-2qc-4\zeta q^2-2\zeta^2c+2v,\\
P_3={}&-6q^2c-18\zeta q^3-18\zeta^2qc-6\zeta^3q^2
+14\zeta-2vq.
\end{aligned}}
\tag{995.15}
\]

One direct derivation keeps the unspecialized relations

\[
\begin{aligned}
D\zeta&=-c-\zeta q+Xv/144,\\
Dq&=2q^2+2\zeta c-X/36,\\
Dc&=3qc+\zeta(3q^2-X/48),\\
DX&=-Y/3,\qquad DY=-X^2/2.
\end{aligned}
\tag{995.16}
\]

For example, before specialization the second zeta derivative is

\[
D^2\zeta
=-2qc-4\zeta q^2-2\zeta^2c
+7X\zeta/144-Xvq/144-Yv/432.
\tag{995.17}
\]

Differentiating this complete expression and only then setting \(X=0,Y=-864\) proves the last line of (995.15). Dropping the displayed \(X\)-terms before differentiating would lose part of the third jet.

Since
\(\nabla^2=\partial_v^2-12\zeta_{\rm alg}\partial_v+36\zeta_{\rm alg}^2-6\zeta_{\rm alg}'\), its third Serre derivative is the actual differential operator

\[
\boxed{\quad
\left.D^3(\nabla^2)\right|_{(0,-864)}
=-12P_3\nabla+216P_1P_2-6P_3'.
\quad}
\tag{995.18}
\]

Here \(D^3(\nabla^2)\) differentiates the coefficients of the operator. The factor \(216\) is the third Leibniz derivative of \(36\zeta^2\), not a suppressed scalar normalization.

## 4. The exact three-branch normal source

Define three genuine one-variable expressions in the original frame:

\[
\begin{aligned}
\mathsf A(v)&=\nabla^2 H'''(v),\\
\mathsf M(v)&=\nabla^2\bigl(vY_s'(v)\bigr),\\
\mathsf R(v)&=\bigl(-12P_3\nabla+216P_1P_2-6P_3'\bigr)Y_s(v).
\end{aligned}
\tag{995.19}
\]

These definitions retain every zeta term. In particular \(\mathsf A\) is not assumed proportional to \(G\), and \(\mathsf R\) is not discarded.

The full third derivative has four Leibniz blocks:

\[
D^3(\nabla^2\mathscr J)
=\nabla^2D^3\mathscr J
+3D(\nabla^2)D^2\mathscr J
+3D^2(\nabla^2)D\mathscr J
+D^3(\nabla^2)\mathscr J.
\]

All derivatives of \(\nabla^2\) involve only the second variable, so commute with \(\Pi_4\). Equation (995.11) therefore kills the two middle blocks after specialization, rather than merely omitting them. Equations (995.6), (995.12), and (995.18) now give

\[
\boxed{\begin{aligned}
\Pi_4D^3(\nabla^2\mathscr J)\big|_{(0,-864)}
={}&\frac1{216}G'''(u)\mathsf A(v)\\
&+12uF'(u)\bigl(3\mathsf M(v)-12G(v)\bigr)\\
&+F(u)\bigl(12\mathsf M(v)-144G(v)+6\mathsf R(v)\bigr).
\end{aligned}}
\tag{995.20}
\]

This is an exact expression using three first-variable functions. No claim about the minimal tensor rank is needed. The new \(G'''\) branch is unaffected by the zeta-variation corrections, which multiply only the \(F\) branch. This records the genuine coupling to the first original tensor without replacing its partner by a different source.

## 5. The unchanged critical indices and every integral bound

Let \(p=6N+5\ge41\), \(i+j=N-1\), and retain \(p\equiv2,5\pmod9\) in the original application. The source identities themselves hold in both classes modulo twelve. Keep

\[
a=6i+4,\qquad b=6j+1,\qquad h=6i+7.
\tag{995.21}
\]

Write the original divided coefficients as

\[
F(u)=\sum_{i\ge0}f_i u^{6i+4},\qquad
G(u)=\sum_{i\ge0}g_i u^{6i+1},
\]

and set

\[
\mathsf A_j=[v^{6j+1}]\mathsf A(v),\quad
\mathsf M_j=[v^{6j+1}]\mathsf M(v),\quad
\mathsf R_j=[v^{6j+1}]\mathsf R(v).
\]

All coefficients needed in (995.20) are in finite integral ranges. One can check this directly in R968's finite formula (968.9), then apply its exact heat recursion three times. The largest mixed coefficient required is \(T_{a+3,b+5}\), and

\[
a+3\le p-4<p,\qquad b+5\le p-5<p.
\tag{995.22}
\]

Thus each separate Taylor factorial is a unit. Each Gaussian factorial is bounded by the smaller of those indices. If the differentiated zeta factors are instead expanded using their heat identities, the largest possible weighted Eisenstein index is

\[
2n\le b+8\le p-2<p-1.
\tag{995.23}
\]

The weighted forms \(B_{2n}E_{2n}\) in this range are \(p\)-integral, and their factorials are units, exactly as in R968. The Serre operation itself uses only the denominators \(2,3\). Consequently the complete source derivatives and the finite coefficients in (995.20) reduce legitimately modulo \(p\). This argument does not infer nonintegrality merely because a total mixed degree has passed \(p\); the denominators use the two separate indices.

In the original sigma expression, \(G'''\) uses \(g_{i+1}\) at degree \(a+3\le p-4\), and \(\mathsf A_j\) uses \(H\) only through degree \(b+5\le p-5\). These are also within the corresponding first integral blocks. No infinite nonintegral sigma series is reduced modulo \(p\).

Define the actual marked third derivative

\[
\Psi_{i,j}=(D^3Z_{a,b})(0,-864).
\]

Taking the specified coefficient of (995.20) proves

\[
\boxed{\begin{aligned}
\Psi_{i,j}
={}&\frac{(a+1)(a+2)(a+3)}{216}\,g_{i+1}\mathsf A_j\\
&+12(3a+1)f_i\mathsf M_j
-144(a+1)f_i g_j
+6f_i\mathsf R_j.
\end{aligned}}
\tag{995.24}
\]

All four numerical factors in the first term are units for the range (995.21); no unknown factor has been divided out. The identity remains meaningful whether any of the displayed source coefficients vanishes.

## 6. Exact comparison with R992, retaining both original filters

R968 gives

\[
Z_{a,b}(0,-864)=-72f_i g_j.
\tag{995.25}
\]

R992(992.32), specialized to this \(E_-\) frame, gives

\[
\boxed{\quad
\mathcal G(Z_{a,b})(0,-864)
=\frac{25Z_{a,b}(0,-864)+\Psi_{i,j}}{144}.
\quad}
\tag{995.26}
\]

The sign before \(\Psi\) is positive because \(Y=-864\). Using the \(E_+\) formula from R992(992.34) without changing this frame would give the wrong sign.

Retain the unchanged original mask

\[
w_i=\mathbf1_{\gcd(6i+7,p+1)=1}P_{6i+6}(1/s),\qquad s^2=-3.
\tag{995.27}
\]

Then the exact normalized marked action on each actual retained generator is

\[
\boxed{\quad
\operatorname{ev}_0\bigl(\mathcal G(w_i Z_{a,b})\bigr)
=\frac{w_i(-864)^{-N}}{144}
\left(\Psi_{i,j}-1800f_i g_j\right).
\quad}
\tag{995.28}
\]

Together with (995.24), this is a complete original-source formula for the first coarse normal marked jet. It does not commute the primitive filter through a change in the label. For example, if \(f_i=0\), the exact remaining value is

\[
\mathcal G(Z_{a,b})(0,-864)
=\frac{(a+1)(a+2)(a+3)}{31104}\,g_{i+1}\mathsf A_j.
\tag{995.29}
\]

The first factor now uses \(i+1\), whereas the original allowed label in (995.27) is still \(h=6i+7\). Also \(\mathsf A_j\) is the displayed \(\nabla^2H'''\) coefficient, not \(g_j\). Thus (995.29) is a normal-jet identity, not a same-label replacement for the vanished original product.

## 7. The remaining propagation question

R992 proves that any nonzero \(\mathcal G\)-invariant subspace of the actual full-level space has a nonzero original marked functional. The new identities specify exactly what the first action of \(\mathcal G\) looks like on the actual mixed source. They do not prove that the right side of (995.28) is the marked value of a combination of the same retained critical columns.

In particular a hypothesis that every original retained \(f_i g_{N-1-i}\) vanishes does not, merely by deleting its occurrences from (995.24), also delete the new \(g_{i+1}\mathsf A_j\), \(f_i\mathsf M_j\), or \(f_i\mathsf R_j\) terms. A genuine relation among these precise sources, with the original primitive and Legendre mask, is still needed for a propagation proof. Conversely their explicit appearance leaves a specified finite source on which such a relation can be tested or proved.

The new result is the exact normal-source decomposition and coefficient identity. It supplies neither an all-prime nonvanishing theorem nor the original rational-point exclusion.

## References and dependencies

- [R966](R966-single-conductor-two-s-CM-kernel-and-original-critical-jet.md): the actual conductor-\((2s)\) source, original positive CM choice, rank-two specialization, unchanged \(F,G,Y_s,H\), and the two label filters.
- [R968](R968-full-level-mixed-CM-jet-and-critical-factor.md): the complete Gaussian-normalized source, canonical zeta normalization, graded heat identity, finite coefficient formula, period scale, and original marked product.
- [R992](R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md): the actual full-level Jacobi operator and its exact third-Serre-derivative marked interface. Its conditional nonzero-space and invariance hypotheses remain intact.
- [R975](R975-original-balanced-Kronecker-integral-heat-recurrence.md): the canonical sigma/heat convention and graded Serre derivation; the exact identities needed here are also derived in (995.13)–(995.18).
- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md) and [R702](R702-first-pole-block-and-uniform-shifted-units.md): the original first integral blocks and the distinction from the later pole blocks. No shifted-unit claim is used as a lower-weight nonvanishing assertion.

Every new calculation above is a paper derivation in the actual sources. No new prime, coefficient array, numerical matrix, or trace is evaluated.
