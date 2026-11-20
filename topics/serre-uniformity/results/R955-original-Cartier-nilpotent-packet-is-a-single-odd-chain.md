# R955: the original Cartier nilpotent packet is a single odd chain

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved structure for the actual original spaces.** The part of the original CM packet which is nilpotent for Cartier has a single chain, and its length is odd. The desired original supersingular pairing is nonzero exactly when this length is one. Thus a failure would require a chain of length at least three. This is not a proof that the length is one, and it does not assert that the whole CM packet has been saturated or that its Hecke algebra is reduced.

No finite arithmetic is performed. The proof uses the complete low-weight spaces already proved in R918/R942 and the complete-space Cartier identification of R952. It does not infer a full-packet assertion from one eigenvector or from an abstract Gorenstein property.

## 1. The actual two-character source and the two Fitting decompositions

Retain the original labels of R932, with
$$
(r,w,V,F)=
\begin{cases}
(2,p-1,V_4^\dagger,V_{p-1}^\dagger),&p\equiv11\pmod{12},\\
(8,p-7,V_{10}^\dagger,V_{p-7}^\dagger),&p\equiv5\pmod{12},
\end{cases}
\tag{955.1}
$$
and all the original assumptions $p\ge41$, $p\equiv2,5\pmod9$. Put $\omega_F=\Phi_w(F)$, with its original full norm extension on the Igusa component union. It is nonzero, satisfies $T_5^{\rm orig}\omega_F=0$ by the original inert-prime CM equation of R913, and satisfies $\mathcal C\omega_F=0$ by R947(947.2), or by the original coefficient criterion in R952.

Work over a perfect field $k$ containing all markings and the two cube-root characters. An algebraically closed extension is harmless for the argument; the dimensions and zero/nonzero statements descend. Let
$$
W=W_h^+\oplus W_h^-,
\qquad
W_h^\pm=(\omega_{B_{\mathrm I}})_{\chi_-,\,\delta=\zeta^{\pm1}},
\qquad \chi_-=\operatorname N^{h-1},
\tag{955.2}
$$
exactly as in R913(913.9). Both geometric deck characters are present. The character $\chi_-$ takes values in $\mathbf F_p$ and includes the actual transport interchanging the two Igusa parts when there are two. No replacement of that full norm extension by a scalar-character restriction is made.

Cartier is an additive $p^{-1}$-semilinear endomorphism of $W$, exchanging its two summands:
$$
\mathcal C(W_h^+)\subset W_h^-,\qquad
\mathcal C(W_h^-)\subset W_h^+.
\tag{955.3}
$$
The actual raw inert-five Hecke correspondence also exchanges the required deck summands, so its square is a genuine endomorphism. Write
$$
\mathcal U_5=(T_5^{\rm orig})^2,
\qquad
M_5=\ker(\mathcal U_5^a:W\to W)
\tag{955.4}
$$
for any sufficiently large $a$ at which the kernel stabilizes. This is the complete generalized zero-primary part. Its complementary Fitting summand is $I_5=\operatorname{im}\mathcal U_5^a$, on which $\mathcal U_5$ is invertible.

Cartier commutes with prime-to-$p$ pullback and trace, and hence with these actual Hecke correspondences. Therefore it preserves $M_5$ and $I_5$. The deck operator preserves $M_5$ because $\mathcal U_5$ preserves the deck characters.

Now take the Cartier Fitting decomposition of $M_5$:
$$
M_5=N\oplus I_{\mathcal C},
\qquad
N=\ker(\mathcal C^b|_{M_5}),\quad
I_{\mathcal C}=\operatorname{im}(\mathcal C^b|_{M_5}),
\tag{955.5}
$$
for sufficiently large $b$. On $N$ Cartier is nilpotent; on $I_{\mathcal C}$ it is bijective and semilinear. This decomposition is valid for semilinear maps over a perfect field: images and kernels are $k$-subspaces, their dimensions stabilize, and the usual kernel/image argument then gives a direct sum. Both summands are preserved by the deck action. In particular $\omega_F\in N$.

The theorem determines the possible shape of this actual $N$. It does not assume $I_{\mathcal C}=0$.

## 2. The Cartier kernel of the complete zero-primary space is exactly the original line

Take any $H\in M_5$ with $\mathcal CH=0$, and identify it with its weight-$w$ modular form by R913/R952's exact Igusa correspondence. R952 proves the entire-space equivalence
$$
\mathcal CH=0
\iff
\mathcal T^rH\in\mathcal A^{r+1}S_{r+2}.
\tag{955.6}
$$
Here and below the modular notation for $H$ is used only after the stated identification. Thus the map
$$
\vartheta_r(H)=\frac{\mathcal T^rH}{\mathcal A^{r+1}}
\tag{955.7}
$$
is defined on this entire Cartier kernel and lands in the complete original low-weight space. It is injective by the actual below-$p$ theta injectivity proved in the supporting note to R946: $0<w<p$, and the original quotient pullback and full norm restriction are injective.

The Hecke normalization is the one already checked in R913 and R946. In modular normalization the theta iterate has factor $5^r$ for $T_5$, and the actual raw high/low powers of five compensate it. In particular (955.7) carries a generalized zero-primary vector for the genuine double correspondence into the generalized zero-primary low-weight space. This remains true with the conjugate intermediate marking retained; it does not use a single $T_5$ endomorphism of one marked modular space.

Both geometric deck characters in (955.2) pass through the **same once-fixed** exotic/Frobenius and determinant-$-1$ transport of R913 §§3 and 5 into one complete $H_6$ low-weight space. This can be checked geometrically, without an inference from Fourier exponent classes. In R920's model the deck action fixes $u^3$, which the determinant-$-1$ correction also preserves; no pre-transport direction of $u$ is identified with its post-transport direction here. The underlying-level forms $E_4,E_6$ are fixed, and R920(920.17–18) proves the same for $\eta^{12}$. The transported $v=V_4^\dagger$ has the actual character $\zeta$ by R913(913.32–33) and its determinant correction. Thus R942's complete weight-ten basis has the actual decomposition
$$
S_{10}(H_6)
=\underbrace{\langle B_1,B_2\rangle}_{\delta=\zeta}
\oplus\underbrace{\langle W\rangle}_{\delta=\zeta^2}
\oplus\underbrace{\langle Z\rangle}_{\delta=1},
\qquad
W=E_4^2\eta^{12}/v,\quad Z=E_4\eta^{12}.
$$
The theta operator and its Hasse denominator preserve this geometrically fixed deck action. The generalized zero-primary space on the sum of the first two summands is therefore still only $kV_{10}^\dagger$, by the complete R942 calculation. For weight four the complete space is already only $kV_4^\dagger$.

There is likewise no extra conjugate $H_6$ copy introduced by Cartier. Its inverse coefficient Frobenius and the actual return to the fixed marking are part of the transported operator in R913(913.43) and R952(952.2), (952.13). At fine level the root construction in R952 gives a direct check: if $L=G^p$ is $H_6$ invariant, uniqueness of the root gives $g^*G=G$ for every $g\in H_6$, since $(g^*G)^p=g^*L=L$. Thus the root stays in the same invariant space while conjugating its deck character. Taking coefficients at indices divisible by $p$ without inverse Frobenius would instead require the conjugate moduli problem, and is not the Cartier map being used. R942's $\overline{\mathcal S}$ is the intermediate target of the ordinary single $T_5$ arrow; it is not a second low-weight kernel added to this source.

For $r=2$, R918's complete low-weight space is $kV_4^\dagger$. For $r=8$, R942 proves on the complete four-dimensional original marked space that the generalized zero-primary part of the genuine double Hecke correspondence is precisely $kV_{10}^\dagger$. Therefore the injective map (955.7) has image of dimension at most one. The named form satisfies $\vartheta_r(F)=V$, so the dimension is exactly one. In actual differential notation,
$$
\boxed{\quad
\ker(\mathcal C|_{M_5})=k\omega_F.
\quad}
\tag{955.8}
$$
This uses all vectors in the indicated Cartier kernel, not just genuine Hecke eigenvectors. It is why the complete low-weight calculation is sufficient for (955.8), even though it does not establish whole-packet Cartier vanishing.

Since Cartier is bijective on $I_{\mathcal C}$, (955.8) is also
$$
\ker(\mathcal C|_N)=k\omega_F.
\tag{955.9}
$$

## 3. The original functional survives on this exact nilpotent part

Let $\lambda_h$ be the actual nonzero functional of R913/R932, extended by zero to the other deck summand of $W$. It has the three already proved properties
$$
\lambda_h\ne0,\qquad
\lambda_h\circ T_5^{\rm orig}=0,\qquad
\lambda_h(\mathcal CW)=0,
\tag{955.10}
$$
and is supported on $W_h^+$.

First $\lambda_h$ annihilates $I_5$. Indeed every vector in $I_5$ is in the image of $\mathcal U_5$, while $\lambda_h\mathcal U_5=0$. Therefore its restriction to $M_5$ is nonzero. Second, it annihilates $I_{\mathcal C}$ because every vector in that summand is a Cartier image of another vector of that summand. Consequently
$$
\boxed{\lambda_h|_N\ne0.}
\tag{955.11}
$$
It still annihilates $\mathcal CN$ and is still supported on the actual $\delta=\zeta$ summand. No scalar comparison between two unspecified eigenfunctionals has been used.

By rank-nullity for the semilinear map over a perfect field and (955.9),
$$
\dim_k(N/\mathcal CN)=1.
\tag{955.12}
$$
Thus $\lambda_h|_N$ spans the dual of this actual one-dimensional cokernel. In particular the cokernel is supported on $\delta=\zeta$: a one-dimensional $\zeta^2$ cokernel would be annihilated by a functional supported on $W_h^+$, contradicting (955.11).

## 4. A single chain and its forced odd length

Let $L$ be the nilpotence index of $\mathcal C|_N$. The following elementary argument works for semilinear maps and supplies an actual chain, rather than assuming a linear Jordan form. The map induced by $\mathcal C$ embeds
$$
\ker\mathcal C^{j+1}/\ker\mathcal C^j
\longrightarrow
\ker\mathcal C^j/\ker\mathcal C^{j-1}.
$$
These are semilinear injections. Starting from the one-dimensional kernel, every successive dimension increment is at most one. Since the nilpotence index is $L$, every increment up to $L$ is nonzero; otherwise injectivity makes every later increment zero too. Hence
$$
\dim\ker\mathcal C^j=j\quad(0\le j\le L),\qquad \dim N=L.
\tag{955.13}
$$
Also $\operatorname{im}\mathcal C=\ker\mathcal C^{L-1}$, since the former is contained in the latter and both have dimension $L-1$.

The deck group has order three, prime to $p$, so choose a lift $v\in N\cap W_h^+$ of the generator of the cokernel in (955.12). It is outside $\operatorname{im}\mathcal C$, and therefore $\mathcal C^{L-1}v\ne0$. The vectors
$$
v,\mathcal Cv,\ldots,\mathcal C^{L-1}v
\tag{955.14}
$$
are linearly independent: in any nontrivial linear relation, applying the largest suitable power of $\mathcal C$ isolates the first nonzero coefficient, and its inverse Frobenius power is still nonzero. They consequently form a basis of $N$.

If $\delta v=\zeta v$, naturality and semilinearity give
$$
\delta\mathcal C^jv=\zeta^{p^{-j}}\mathcal C^jv.
\tag{955.15}
$$
Since $p\equiv-1\pmod3$, these characters alternate between $\zeta$ and $\zeta^2$. The bottom of the chain spans $k\omega_F$, whose actual deck character is again $\zeta$. Thus $L-1$ is even. There is an integer $m\ge0$ such that
$$
\boxed{\quad
L=2m+1,\qquad
\dim(N\cap W_h^+)=m+1,\qquad
\dim(N\cap W_h^-)=m.
\quad}
\tag{955.16}
$$
The basis (955.14) is a single Cartier chain with all scalar Frobenius operations understood. In particular a length-two chain cannot be the actual failure mechanism in these original two-character spaces. If a longer chain exists, the first possible length is three.

## 5. Identification with the CM nilpotent packet and the exact trace criterion

Let $M_{\rm CM}$ be the full generalized packet for the original raw prime-to-$6p$ CM Hecke system, in $W$. The system has values in $\mathbf F_p$ by R913 §7. All these Hecke correspondences commute with Cartier and with $\mathcal U_5$, so they preserve $N$.

For completeness, decompose $N$ into primary modules for the finite commutative image of this Hecke algebra after a field extension splitting its residue characters. Cartier may send such a primary module to its coefficient-Frobenius conjugate, but therefore preserves the sum over every Frobenius orbit of characters. Every nonzero such sum has a nonzero Cartier kernel, because Cartier is nilpotent on $N$. Equation (955.9) says that this entire kernel is the single original CM line. Thus the only character orbit which can occur is the one containing the original CM system. That orbit is a singleton, since its eigenvalues are in $\mathbf F_p$.

It follows that $N\subset M_{\rm CM}$. Conversely $M_{\rm CM}\subset M_5$, because its inert-five eigenvalue is zero, so its Cartier nilpotent Fitting part is contained in $N$. Hence
$$
\boxed{\quad
N=\text{the Cartier nilpotent Fitting part of }M_{\rm CM}.
\quad}
\tag{955.17}
$$
No assertion that the complementary Cartier-bijective part of $M_{\rm CM}$ is absent is required or made.

The bottom vector $\omega_F$ survives in the cokernel $N/\mathcal CN$ if and only if $L=1$. If $L>1$, it is the Cartier image of the preceding chain vector. Since the nonzero original functional spans the dual of that cokernel, one obtains the exact alternatives
$$
\boxed{\quad
\lambda_h(\omega_F)\ne0\iff L=1\iff m=0,
\qquad
\lambda_h(\omega_F)=0\iff L\ge3\iff m\ge1.
\quad}
\tag{955.18}
$$
The full R932/R936 trace has the same zero/nonzero value by R932(932.37a), whose outside factors are all nonzero and remain unchanged. In particular the actual $d_1$, the number of original Igusa parts, and the nonzero source scalar $c_h^{\mathrm F}$ are not set equal to one in using (955.18).

There is an equivalent concrete preimage formulation on the original whole source:
$$
\boxed{\quad
\lambda_h(\omega_F)=0
\iff
\text{there is }\omega\in W_h^-\text{ with }\mathcal C\omega=\omega_F.
\quad}
\tag{955.19}
$$
If the right side holds, the functional kills $\omega_F$ by (955.10). Conversely a zero value forces $L\ge3$, and the preceding vector in the actual chain can be scaled to have Cartier image exactly $\omega_F$; its character is $\zeta^2$. It lies in $N\cap W_h^-$. This proves the reverse implication without supposing that a generalized Hecke eigenclass has an eigenvector lift.

In modular notation, R952 identifies the preimage equation in (955.19), with its inverse coefficient Frobenius retained, as
$$
\mathscr U H=F,
\qquad
\left.\mathscr O_r(H)\right|_\Sigma
=\left.r!\frac{F^p}{\mathcal B^{p-r}}\right|_\Sigma.
\tag{955.20}
$$
These two equations are equivalent, not just one-way implications: the second and R952 force $\mathscr U H-F$ to vanish on $\Sigma$, and restriction is injective on cusp forms of weight $w\le p-1$. Every source character, marking, and full norm extension in (955.20) is the one transported from $W_h^-$.

As a consistency check independent of choosing a chain basis, R952 and R951 give, for such a preimage,
$$
\mathscr B_r(H,F)
=r!\sum_{P\in\Sigma}\frac{F_P^{p+1}}{b_P^w}
=\mathscr B_r(F,H)=0,
\tag{955.21}
$$
because $r=2,8$ is even and $\mathscr O_r(F)=0$. This is the same vanishing of the correctly weighted high-source supersingular diagonal. It does not replace that high diagonal by R950's low-weight diagonal.

## 6. What is still required

The exact remaining issue in this route is to exclude the actual preimage (955.19), or equivalently to prove $m=0$ in (955.16). The argument gives no exclusion of $m\ge1$. In particular the original nonzero additive line fixes the top cokernel character and hence the odd parity of the chain, but does not split the chain or make its bottom survive in that cokernel.

The low-weight complete space is already fully used in proving (955.8). Its simple zero-primary line cannot be applied a second time to all of $N$, because only its Cartier kernel is known to descend holomorphically under (955.7). A vector preceding $F$ has the explicit nonzero supersingular obstruction in (955.20), so its theta quotient has the remaining Hasse poles. Those poles, or the original ramified geometric source governing them, must be treated by a further argument.

Finally, even a proof of $m=0$ would concern the R932/R936 high-weight functional. It would not restore the unit-source comparison to the central $Q'_h(0)$ already disproved by R945. No rational-point exclusion or uniform absolute prime bound is asserted here.

## Dependencies

- R913(913.9–12), (913.40–43): the actual two deck summands, full norm character, nonzero Cartier-cokernel functional, inert-five equation, coefficient field, and Cartier/Hecke transports.
- R932(932.14–19), (932.37a): the original named forms, exact theta companion, and complete trace with its nonzero source scales.
- R918 and R942: the complete low-weight space and complete double-Hecke zero-primary line, respectively.
- R946 and its supporting saturation note: injectivity of the actual theta iterate below weight $p$ and the already fixed high/low Hecke factors.
- R952: the complete-space exact Cartier obstruction formula and its pointwise kernel criterion.
- R951: the actual composed-pairing symmetry used in (955.21).

All new chain, parity, and preimage statements are proved above in the actual original spaces. No new mathematical computation or finite-prime scan was executed.
