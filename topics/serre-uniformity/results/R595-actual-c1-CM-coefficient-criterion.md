# R595 — Actual c1 CM coefficient criterion and the verified prime 269

> Recovery record, 2026-11-14. The previous executor scratch and functions.store were lost together. This document reconstructs the complete already reviewed mathematical argument from the surviving detailed conversation. It is not claimed to have the old proof SHA 454b4fdac0eb3eb41054ec0e3028692c70288e3e9d4ad8b203ceaf1da1808e3f. No old torsion orbit, prime grid, or previously completed 269 calculation was rerun for this recovery. The original 23,077-byte Node wrapper was not recoverable verbatim; the separate receipt records this boundary.

## 1. Actual family, normalization, and theorem

Let \(p\ge41\) be prime, \(p\equiv5\pmod6\), and put \(q=p^2\), \(e=q-1\). Work with
\[
E_0:y^2=x^3-1,\qquad \omega=\frac{dx}{2y},\qquad D=\frac d{dz},
\]
and choose the \(p\)-adic embedding of \(\alpha^3=4\) for which \(\alpha\bmod p\) is the unique root in \(\mathbf F_p\). Set \(C_0=72\sqrt3/\alpha\). The actual c1 tame character is
\(\chi_6(\varepsilon\zeta^i\bmod3,\zeta^j\bmod2)=\varepsilon\zeta^{j-i}\).
Its finite kernel is
\[
H_0=C_0R_-,\qquad
R_-=\frac{x^2(x^6+34x^3-8)}{x^9-228x^6+48x^3-64}.
\tag{595.1}
\]
This is not R589's c0 kernel
\[
R_0=u^4\frac{7+4u^6+16u^{12}}{1-228u^6+48u^{12}-64u^{18}},
\quad u=x^{-1/2}.
\]
The degree congruences differ: \(R_-\) starts with \(u^2\), whereas \(R_0\) starts with \(u^4\).

Let \(Y\) be an integral \(\mu_e\)-equivariant CM formal coordinate with linear coefficient one, as in Sections 3 and 6. Write \(H_2(Y)=\sum a_nY^n\), and define
\[
\begin{aligned}
K_p&=\frac1{C_0}\left(a_{p-1}+p\,a_{p-1+e}
+p^2a_{p-1+2e}\right)\pmod p,\\
r_{3,p}&=[z^{(p-1)(p-3)}]R_-\pmod p.
\end{aligned}
\tag{595.2}
\]
All three terms defining \(K_p\) are integral. Put
\[
B=(-1)^{(p-1)/2-(p-2)/3}
\binom{(p-1)/2}{(p-2)/3}\pmod p.
\tag{595.3}
\]
It is a unit. In the actual R588 normalization,
\[
\boxed{
(pM_2)^2\equiv
-20736\zeta^2B^3\alpha^{-2}K_pr_{3,p}\pmod p.
}
\tag{595.4}
\]
In particular
\[
v_p(M_2)\ge-1,\qquad
v_p(M_2)=-1\ \Longleftrightarrow\
K_pr_{3,p}\ne0\pmod p.
\tag{595.5}
\]
If the residue is zero, the conclusion justified by this congruence is
\(v_p(M_2)\ge-\tfrac12\); no unproved unramified-value-field assertion is used.

The exact calculations already performed gave
\[
K_{269}=66,\qquad r_{3,269}=160,\qquad B_{269}=49,\qquad
\alpha_{269}=231.
\tag{595.6}
\]
Thus \(v_{269}(M_2)=-1\). This is a local c1 statement. Since \(269\equiv8\pmod9\), it is not an exclusion of a prime in R317's remaining classes \(2,5\pmod9\).

## 2. The exact finite kernels

For the completed zeta variable \(E\), the translated Kronecker coefficients used in R580 are
\[
\begin{aligned}
T_0&=E,\\
T_1&=-(Ex+y),\\
T_2&=-\frac12(E^2y+2Ex^2+xy),\\
T_3&=-\frac16(E^3x^2+3E^2xy+3Ex^3-2E+x^2y).
\end{aligned}
\tag{595.7}
\]
For example, with \(S_n=(D+E)^n1\), these are
\(T_m=D^mS_{m+1}/(m!(m+1)!)\); this fixes the factorials. At each of the eighteen actual six-torsion points \(Q\), translate using the elliptic addition formulas and the exact completed-zeta value
\[
E(Q)=\frac{y_Qx_Q^2(-19x_Q^6+4328x_Q^3-16)}{5184}.
\]
The tame sum is \(H_m(P)=\sum_Q\chi_6(Q)^{-1}T_m(P+Q)\), in the same character direction as (595.1). The exact R580 kernel input has SHA256
7df27842692876834a223c8d83f407594edb67756f132d31df410719d13034e5.

Let \(\Delta=x^9-228x^6+48x^3-64\). The complete \(H_2\) kernel, reconstructed by exact rational trace and checked against the original actual finite kernel, is
\[
\frac{H_2}{C_0}=
\frac{A_0+EyA_1+E^2A_2}{2\Delta^3},
\tag{595.8}
\]
where
\[
\begin{aligned}
A_0={}&x^{28}+5579x^{25}+394964x^{22}+1306400x^{19}
-3004864x^{16}-3765760x^{13}\\
&+7734272x^{10}-2621440x^7-114688x^4+65536x,\\
A_1={}&2x^{26}+12188x^{23}+949808x^{20}+3062336x^{17}
-8815360x^{14}-30714880x^{11}\\
&+27398144x^8-212992x^5-1245184x^2,\\
A_2={}&x^{27}+6648x^{24}+561408x^{21}+1300224x^{18}
-8685696x^{15}-38088192x^{12}\\
&+58945536x^9-4177920x^6-5210112x^3+131072.
\end{aligned}
\tag{595.9}
\]
All denominators are units at the primes under consideration.

The coefficient of \(E^2\) in \(H_2\) is exactly \(D^2H_0/4\). If
\(N=x^2(x^6+34x^3-8)\) and \(V=N'\Delta-N\Delta'\), the equality was checked by the full integer identity
\[
4(x^3-1)(V'\Delta-2V\Delta')+6x^2V\Delta=2A_2.
\tag{595.10}
\]
The preserved historical record reports twenty-eight zero coefficients. The recovered display originally mistranscribed its last factor as Delta-prime; the published formula above uses Delta. The new complete integer polynomial check verifies the corrected formula and detects that the mistranscribed one is false. No truncation is used; the exact lost historical checker line is not claimed. See [the recovery erratum](../notes/R595-recovery-erratum-595-10.md).

The original finite kernel also gives the following local forms in the actual integral coordinate. For \(Z=E-Y^{-1}\),
\[
H_2=B_0+ZB_1+Z^2B_2,\quad
B_0\in Y^4\mathcal O[[Y]],\quad
B_1\in Y^5\mathcal O[[Y]],\quad
B_2=D^2H_0/4\in\mathcal O[[Y]]^\times.
\tag{595.11}
\]
For \(H_3=\sum_{a=0}^3E^aC_a\), the coefficients are integral and
\[
C_a\in Y^{2+a}\mathcal O[[Y]],\qquad
C_3=D^3H_0/36.
\tag{595.12}
\]
These statements refer to the full actual finite kernels, not solely their highest powers of \(E\).

## 3. The actual completed zeta and integral CM coordinate

The completed zeta at a \(p\)-torsion point is the actual algebraic value, not an arbitrarily chosen primitive. R589 proves this by the division-polynomial identity
\[
D\log\psi_p=pE([p]Y)-p^2E(Y),
\]
whose constant term at a root \(P\) gives
\[
E(P)=-\frac{D^2\psi_p(P)}{2p^2D\psi_p(P)}.
\tag{595.13}
\]
The oddness condition fixes the additive constant.

The integral CM coordinate has
\[
Y=z+O(z^q),\qquad
\omega=(1+O(Y^e))\,dY,\qquad
[p](Y)\equiv-Y^q\pmod p.
\tag{595.14}
\]
The last identity is the complete reduced formal multiplication law in the CM coordinate. If \(\varpi=Y(P)\) for a nonzero \(p\)-torsion point, then
\[
v_p(\varpi)=1/e,\qquad
\varpi^e/p\equiv1\pmod p.
\tag{595.15}
\]
The \(\mu_e\)-equivariance is retained, so all other nonzero torsion coordinates are \([a]\varpi\).

The completed primitive has the form
\[
E(Y)=Y^{-1}+\sum_{\substack{k\ge1\\k\equiv5\ (6)}}e_kY^k,
\qquad v_p(e_k)\ge-v_p(k).
\tag{595.16}
\]
Cartier on \(x\omega\) gives, in the positive-degree range used below,
\[
pE\equiv-BY^p\pmod p.
\tag{595.17}
\]
An allowed exponent divisible by \(p^2\) must be at least \(5p^2\), because \(p^2\equiv1\pmod6\) and the exponents in (595.16) are \(5\pmod6\). This observation controls the first four tails without incorrectly assigning two powers of \(p\) loss to each primitive.

## 4. Both complete Fourier tails

Use the actual character \(\theta=\theta_{-1}\) and the R580 convention
\[
S_2=-\sum_{a\in(\mathcal O_K/p)^\times}\theta(a)H_2(P_a),\qquad
S_3=-\sum_a\theta(a)^{-1}H_3(P_a).
\]
The complete \(\mu_e\)-sum selects respectively the exponents
\[
p-1+je,\qquad N+je,\qquad N=p(p-1),\qquad j\ge0.
\tag{595.18}
\]

For \(S_2\), the coefficient at \(p-1\) is integral. At \(p-1+e\), multiplication by \(p^2\) leaves only the \(Z^2B_2\) term modulo \(p\); its coefficient is
\[
\frac{B^2}{4}N(N-1)[Y^N]H_0=0\pmod p.
\]
Thus this coefficient has valuation at least \(-1\). The coefficient at \(p-1+2e\) has valuation at least \(-2\). These are exactly the three blocks in (595.2).

For \(j=3,4\), every positive primitive index contributing to (595.11) is at most \(p-1+je-5<5p^2\), so each primitive loses at most one \(p\), and the coefficient loses at most two. For \(j\ge5\), the cruder bound is
\[
v_p(a_{p-1+je})\ge-4-2\lfloor\log_p(j+1)\rfloor.
\]
The extra factor \((\varpi^e)^j\) makes the discarded tail gain at least one full power of \(p\), because
\(j-4-2\lfloor\log_p(j+1)\rfloor\ge1\) for \(p\ge41,j\ge5\). Equation (595.15) also makes replacing the first three powers of \(\varpi^e\) by \(p^j\) accurate modulo one additional \(p\). Therefore
\[
S_2=-eC_0K_p\varpi^{p-1}
+\text{an error of valuation at least }1+\frac1{p+1}.
\tag{595.19}
\]

For \(S_3\), multiplication of the first selected coefficient by \(p^3\) retains only \(E^3D^3H_0/36\). Put
\(n_3=N-3p+3=(p-1)(p-3)\). Then \(n_3\equiv3\pmod p\), so
\[
p^3[Y^N]H_3
\equiv-\frac{B^3C_0}{6}r_{3,p}\pmod p.
\tag{595.20}
\]
For \(j=1,\ldots,4\), the largest primitive exponent is below \(5p^2\), so the coefficient loses at most three powers of \(p\). For \(j\ge5\), its valuation is bounded below by
\(-6-3\lfloor\log_p(j+1)\rfloor\). The tail is again smaller by at least one full \(p\), using
\(j-3-3\lfloor\log_p(j+1)\rfloor\ge1\).
Consequently
\[
S_3=\frac{eB^3C_0}{6p^3}r_{3,p}\varpi^N
+\text{an error one full }p\text{ above the stated lower bound}.
\tag{595.21}
\]
Equations (595.19) and (595.21) are lower-bound statements even when one of the displayed residues vanishes. They do not silently assume either leading coefficient is a unit.

Since \(N+p-1=e\), (595.15) and \(C_0^2=15552/\alpha^2\) yield
\[
\boxed{p^2S_2S_3\equiv-2592B^3\alpha^{-2}K_pr_{3,p}\pmod p.}
\tag{595.22}
\]
All omitted terms have valuation at least one after multiplying the product by \(p^2\).

R588 gives the actual toric norm and actual anti-linear identification
\[
M_2\overline{M_2}=\frac{8N_\theta}{(p+1)^2}S_2S_3,\qquad
\overline{M_2}=-\zeta M_2,\qquad N_\theta\equiv-1\pmod p.
\tag{595.23}
\]
These are not replaced by an assumption that complex conjugation fixes the chosen \(p\)-adic place. Their exact combination gives (595.4) and (595.5).

## 5. Strict-coordinate invariance of the residue

For two strict integral \(\mu_e\)-equivariant coordinates,
\(Y'=Y(1+c_1Y^e+c_2Y^{2e}+\cdots)\).
At \(p\)-torsion, (595.15) gives \(Y'/Y=1+O(p)\). The actual finite sum \(S_2\) is independent of that coordinate. Comparing (595.19) in the two coordinates proves that \(K_p\bmod p\) is unchanged. This justifies a computationally convenient strict coordinate, not an arbitrary nonintegral reparameterization.

## 6. A finite coefficient algorithm retaining the CM correction

Put \(u=x^{-1/2}\), \(w=u^6\),
\[
z=uZ(w),\quad
Z(w)=\sum_{k\ge0}\frac{C_k}{6k+1}w^k,\quad
C_k=\binom{2k}{k}/4^k.
\]
Let \(L=(q-1)/6\). In the coefficient range needed for all three blocks, the only nonintegral coefficient of \(Z\) is the one at \(L\):
\[
Z=Z_0+(c_p/p)w^L,\qquad Z_0\in\mathbf Z_p[[w]],\quad
(Z_0)_L=0,\quad c_p\equiv-1\pmod p.
\tag{595.24}
\]
The assertion follows from the exact valuation of the central binomial coefficient: for a denominator divisible by \(p\), the low base-\(p\) digit is \((5p-1)/6>p/2\), causing the cancelling carry. At \(6L+1=q\), the denominator has two powers of \(p\) and only one carry.

The actual averaged CM coordinate has first coefficients
\[
Y_{\rm av}=z+v_qz^q+v_2z^{2q-1}+\cdots,\qquad
v_q=I-c_p/p,
\]
where
\[
I=-L^{-1}[w^{L-1}]Z_0^{-q}Z_0'/Z_0\in\mathbf Z_p.
\tag{595.25}
\]
The second coefficient is
\[
v_2=\frac{[w^{2L}]Z_0^{-(2q-1)}}{2q-1}
-\frac{c_p}{p}[w^L]Z_0^{-2q}+c_p^2.
\tag{595.26}
\]
It is integral: the middle coefficient is divisible by \(q\), as follows by differentiation and the fact that \(L\) is a \(p\)-unit.

The actual strict integral change
\[
Y^*=Y_{\rm av}-IY_{\rm av}^{q}
+(-v_2+Iqv_q)Y_{\rm av}^{2q-1}
\]
has
\[
Y^*=z-(c_p/p)z^q+0\cdot z^{2q-1}+\cdots.
\tag{595.27}
\]
Every coefficient of the change in \(Y_{\rm av}\) is integral. Its expression in flat \(z\) need not be integral, and is not treated as such.

For direct use of (595.8), write \(U=uE\) and
\[
d(w)=1-228w+48w^2-64w^3,\quad
U=1-\sum_{k\ge1}\frac{C_k}{6k-1}w^k.
\]
Reversing the coefficients of \(A_0,A_1,A_2\) gives \(F_0,F_1,F_2\), and
\[
H_2/C_0=
u^{-2}\frac{F_0-U\sqrt{1-w}F_1+U^2F_2}{2d^3}.
\tag{595.28}
\]
The leading \(1-2+1\) cancellation must be kept before coefficient division.

Let \(m=(p+1)/6\), \(M_1=L+m-1\), and \(n_1=q+p-2\). Put
\(J_T=(4+6w\partial_w)(p^2H_2/(C_0u^4))\), using the complete series modulo \(p^2\) where required. The exact \(K_1\) computation is
\[
K_1=\frac1p\,\frac1{n_1}[w^{M_1}]J_T Z_0^{-n_1}\pmod p.
\tag{595.29}
\]
The numerator is divisible by \(p\). The potential strict-coordinate correction contains
\(pw^{L+1}\), while \(J_T\bmod p\) has order at least \(2m-1\), so its product starts beyond \(M_1\). The coefficient can be computed with the full binary negative power, or by the equivalent Frobenius simplification
\[
Z_0^{-n_1}=Z_0^2Z_0^{-p}
(1-p\log Z_0(w^p))\pmod{p^2}
\]
in the stated truncated range.

For \(K_2\), put \(n^*=2q-p-1\), \(M^*=(n^*-2)/6=2L-m\), and \(P=Y^*/u\). Then
\[
K_2=\frac{B^2}{4}(n^*-1)
[w^{M^*}](2A+6wA')P(w)P(w^p)\pmod p,
\tag{595.30}
\]
where \(A=(1+34w-8w^2)/d(w)\) and
\[
P\equiv Z_0+w^L\log Z_0(w^p)\pmod p.
\]
This is the third block actually evaluated in the original computation. It was not assumed to vanish.

Finally, with \(n_3=(p-1)(p-3)=2+6M_3\),
\[
r_{3,p}=\frac1{n_3}
[w^{M_3}](2A+6wA')Z(w)^{-3}Z(w^p)^4\pmod p.
\tag{595.31}
\]
All logarithm coefficients needed in this expression are integral. This is a finite exact coefficient prescription for the actual R595 residue.

## 7. Executed arithmetic and genuinely independent 269 path

The historical actual execution records are:

| p | B | alpha | K0,K1,K2 | r3 | p²S2S3 mod p | (pM2)²/zeta² mod p |
|---:|---:|---:|---:|---:|---:|---:|
| 41 | 11 | 25 | 0,12,0 | 26 | 3 | 24 |
| 47 | 10 | 18 | 0,2,0 | 20 | 23 | 43 |
| 269 | 49 | 231 | 0,66,0 | 160 | 150 | 124 |

For p41, the complete original average-coordinate calculation gave the scaled coefficients
[0,66051,63509] modulo \(41^3\), yielding [0,12,0]. The previously completed R580 torsion-orbit product was 1274 modulo \(41^2\), whose residue is 3. That orbit was not rerun.

For p269, root independently used the explicit complete rational H2 kernel, a full binary evaluation of \(Z_0^{-72628}\bmod72361\), and the true averaged CM coordinate
\[
I=37,\qquad P_{\rm av}=P^*+37w^{12060}.
\]
It found middle numerator 17754, K1=66, K0=K2=0, B=49 and \(c_p=268\). This path did not use the other implementation's Frobenius shortcut, and it retained the actual coordinate correction. Root reported PASS after independent arithmetic and all coordinate/tail review.

The r3_269 calculation used a direct BigInt central binomial coefficient, three successive quotient equations \(QZ=F\), and the final sparse \(Z(w^{269})^4\) convolution. It had
\[
n_3=71288,\qquad M_3=11881,\qquad
n_3\bmod269=3,
\]
and raw sum 211, hence r3=160. Its forty-five summands are preserved verbatim in the recovered certificate. The largest accumulated integer dot product was 853412768, below \(2^{53}\); all modular products were therefore exact. The recovered historical identity certificate preserves twenty-eight zero differences. These are a historical record, while the corrected published (595.10) is established by the separately saved new complete polynomial check; the lost checker source is not identified with the erroneous recovered display.

The source function that constructs the exact rational H2 kernel survives in the conversation and has been restored separately. The original long Node orchestration wrapper was lost; the recovery does not falsely call the reconstructed short source that old wrapper, nor claim it has the old wrapper SHA. The mathematics and historical certificates are preserved independently of that packaging loss.

## 8. Precise global boundary

The p269 statement is **the actual c1 minimum valuation \(v_{269}(M_2)=-1\)**. It is not a complete classification at p269. Its c0 nonunit phenomenon belongs to R594, and \(269\equiv8\pmod9\) is outside R317's remaining classes.

Geometrically, on \(j=6912a^3(1-a^3)\), c0 is \(a=0\) and one c1 is \(a=1\). The full-level \(S_6\) marking action is not by itself an over-j automorphism transporting candidates between these coarse points. R578/R592 alone give
\[
U=z_{\rm flat}^3/p^3,\quad w_1=(a-1)/p^3,\quad
U\equiv3w_1/8\pmod{p^2},
\]
and when \(v_p(M_2)=-1\),
\[
p^{-3}L_1(pV)=V\bigl(pM_2/6+VH(V)\bigr),
\]
with the coefficients of \(H\) in the maximal ideal. This establishes the unique zero of the corresponding actual primitive in the deep disc \(v_p(a-1)\ge4\), subject to that precise map. It does not establish a global zero image, a full quadratic-Chabauty leading term, general candidate transport, or the topic's completion criterion.

The later separately proved R601 universally removes K0 and K2. That later result is not needed to justify the historical R595 computations, which evaluated all three blocks.
