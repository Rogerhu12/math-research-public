# Prime-field descent of the complete R936 supersingular trace

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved algebraic descent of the complete trace to $\mathbf F_p$.** This is an increment to R936. It does not prove that the trace is nonzero, identify it with $Q'_h(0)$, or change the original CM source constant.

## 1. Fixed conventions and statement

Keep all of R936, including
$$
p=6N+5,\qquad k=\mathbf F_p(s),\quad s^2=-3,
\quad \zeta=(-1+s)/2,
$$
the original oldform phase $\zeta^2$, $w=k_-=p+1-r=6J+4$, $D(t)=1-4t$, and
$$
F=V_w^\dagger=F_w(Q)-2^w\zeta^2F_w(Q^4).
\tag{PD1}
$$
Write the proved unit-triangular expansion as
$$
F=\sum_{j=0}^Jc_jV_4^\dagger E_6^{J-j}\eta^{12j},
\qquad P_J(X)=\sum_{j=0}^Jc_jX^{J-j}.
\tag{PD2}
$$
Let a bar denote the coefficient-field involution $s\mapsto-s$, with $Q$ and $X$ held fixed. It is the nontrivial automorphism of $k/\mathbf F_p$. The assertion is
$$
\overline{c_j}=(-1)^jc_j,\qquad C(t)\in s\mathbf F_p[t],
\tag{PD3}
$$
$$
R\in\mathbf F_p[t]/(tH_N),\qquad
\operatorname{Tr}_{L/k}((3-2e_0)R)\in\mathbf F_p,
\qquad S^p,S\in\mathbf F_p.
\tag{PD4}
$$
Here $C,R,e_0,L,S$ are exactly R936's objects, without additional scaling.

## 2. The original inert-two parity identity

The rational CM theta coefficients $a_n=[Q^n]F_w$ satisfy $a_{2m}=0$ for $m$ odd and
$$
a_{4m}=-2^{w-1}a_m.
\tag{PD5}
$$
This follows directly at the level of the original ideals, without a Hecke multiplicity assumption. The prime two is inert in $\mathbf Q(\sqrt{-3})$. Every ideal of even norm is divisible by the principal ideal $(2)$, whose norm is four. The original character evaluates on $(2)$ as
$2^{w-1}\epsilon_3(2)=-2^{w-1}$. Removing that factor bijects the ideals of norm $4m$ with those of norm $m$. The same identity includes the zero coefficients at multiples of three.

It follows coefficient by coefficient that
$$
F_w(-Q)=-F_w(Q)-2^wF_w(Q^4).
\tag{PD6}
$$
Using $1+\zeta^2=-\zeta$ and $\overline{\zeta^2}=\zeta$ gives
$$
\begin{aligned}
V_w^\dagger(-Q)
&=-F_w(Q)-2^w(1+\zeta^2)F_w(Q^4)\\
&=-F_w(Q)+2^w\zeta F_w(Q^4)
=-\overline{V_w^\dagger(Q)}.
\end{aligned}
\tag{PD7}
$$
The weight-four case gives the same identity for $V_4^\dagger$. No replacement of the oldform coefficient by a conjugate or an unmarked eigenvector has occurred.

## 3. Coefficients in the full original basis

The exact series $E_6(Q^6)$ is even in $Q$, and
$\eta^{12}(Q^6)=Q^3\prod_{n\ge1}(1-Q^{6n})^{12}$ is odd. For
$$
B_j(Q)=V_4^\dagger(Q)E_6(Q^6)^{J-j}\eta^{12}(Q^6)^j
$$
we consequently have
$$
\overline{B_j(Q)}=(-1)^{j+1}B_j(-Q).
\tag{PD8}
$$
Conjugating (PD2) and comparing with (PD7) yields
$$
\sum_j(-1)^{j+1}\overline{c_j}B_j(-Q)
=-\sum_jc_jB_j(-Q).
$$
The $B_j(-Q)$ remain linearly independent, because the $B_j$ form the full unit-triangular basis proved in R936. Hence
$\overline{c_j}=(-1)^jc_j$. Since $\bar s=-s$, this is equivalent to
$$
c_j=s^jd_j,\qquad d_j\in\mathbf F_p.
\tag{PD9}
$$
No semisimplicity or dimension-one Hecke assertion is used.

## 4. The fixed evaluation polynomial and full trace

Substitute (PD9) into R936's fixed finite polynomial
$$
C(t)=12s(6s)^JP_J(24s(1-8t)).
$$
After the Tate-frame sign correction, the actual modular evaluation is
$F(E_u,\omega)=(-1)^JD^{J+1}C(t)$ and
$\mathcal B(E_u,\omega)=-D^{N+1}b(t)$ on the SS algebra. The even exponents in $F^{p+1}/\mathcal B^w$ leave R936's $R(t)$ unchanged. This note concerns those retained finite polynomials and that exact trace.
Each summand contains $s^{1+J+j+J-j}=s^{2J+1}$. Therefore
$$
C(t)=sU(t),\qquad U(t)\in\mathbf F_p[t].
\tag{PD10}
$$
Since $s^p=-s$ and $s^{p+1}=3$,
$$
C(t)^{p+1}=3U(t)^{p+1}\in\mathbf F_p[t].
\tag{PD11}
$$
The polynomials $D,H_N,b,e_0$ and the inverse of $b$ modulo $tH_N$ are all defined over $\mathbf F_p$. For the inverse, uniqueness gives descent: conjugating $bb^{-1}=1$ fixes $b$ and the modulus, so it fixes $b^{-1}$. Thus $R$ belongs to
$$
L_0=\mathbf F_p[t]/(tH_N).
$$
The algebra $L$ is $L_0\otimes_{\mathbf F_p}k$. Multiplication by $(3-2e_0)R$ has a matrix over $\mathbf F_p$, and its trace is unchanged by scalar extension. This proves the trace assertion even when individual supersingular roots are not $\mathbf F_p$-rational. R936's exact formula
$$
S^p=12[-6^{r-1}(r-1)!]^2
\operatorname{Tr}_{L/k}((3-2e_0)R)
\tag{PD12}
$$
then puts $S^p$ in $\mathbf F_p$. Frobenius has a unique inverse in a perfect field, and is the identity on $\mathbf F_p$, so $S$ itself is the same $\mathbf F_p$ element.

## 5. Branch and source audit

All identities above start with the original fixed $\zeta^2$ phase. The bar is used only as an algebraic coefficient involution to prove relations. It is not an assertion that the conjugate Fourier form belongs to the same marked $H_6$ module, nor an identification of its geometric source with the original one.

More explicitly, (PD3) gives
$$
\overline{P_J}(-X)=(-1)^JP_J(X).
\tag{PD13}
$$
If one consistently changes the chosen square root to $-s$ and hence $\zeta$ to $\zeta^2$, the displayed evaluation polynomial changes to
$$
12(-s)(6(-s))^J\overline{P_J}(24(-s)(1-8t))=-C(t).
\tag{PD14}
$$
Its $(p+1)$st power is unchanged. Changing the cube-root representative of $u$ in R936 leaves $t=u^3$ and the already proved weight-zero function $F^{p+1}/\mathcal B^w$ unchanged. Thus this descent contains neither an untracked square-root sign nor an extra deck scalar.

The actual functional still has precisely the factor
$$
\frac{m_{\rm I}(c_h^{\rm F})^{1/p}}{d_1\,6^r(r-1)!}
$$
multiplying $S$. That factor is not computed or claimed to lie in $\mathbf F_p$. The statement concerns the complete fine sum and its trace, not a normalization of the original functional.

## 6. Scope and reported finite values

This proof does not rule out cancellation inside $\mathbf F_p$. A finite-field norm or an $\mathbf F_p$-valued sum has no positivity property that would force nonvanishing. It also does not compare the trace with the separate higher normal residue defining $Q'_h(0)$.

The reported public run [44713602498](https://github.com/Rogerhu12/math-research-public/actions/runs/44713602498), job 136211233497, has the following trace and $S^p$ values:

| $p$ | Trace | $S^p$ | Original allowed class |
|---:|---:|---:|:---|
| 41 | 3 | 39 | yes |
| 47 | 9 | 34 | yes |
| 59 | 35 | 16 | yes |
| 71 | 59 | 70 | auxiliary |
| 83 | 35 | 14 | yes |
| 107 | 6 | 24 | auxiliary |

All second coordinates are zero, as the proof requires. Primes 71 and 107 are auxiliary because $p\bmod9=8$. These finite values are consistency evidence, not an input to the proof or an all-prime theorem. The reported output has 106489 bytes and SHA256 `e3241fb803c302caa2a3676d4079f528a2954c4a40d73d7654524d8888546c42`; no recomputable output is included here.

## Sources

- [R913](../results/R913-original-Igusa-Cartier-functional-and-two-CM-companions.md), §§5–7: original CM character, rational theta coefficients, and fixed oldform phase.
- [R936](../results/R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md), §§3–6: complete integral triangular basis, evaluation polynomial, full supersingular trace, and exact source scale.

No mathematical computation was performed locally.
