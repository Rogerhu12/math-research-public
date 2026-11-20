# R958: the original r=2 Cartier matrices and a single-moment trace criterion

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved symbolic formulas for every original r=2 prime.** This gives the two complete opposite-deck Cartier maps by finite polynomial algebra. The actual Cartier-preimage question of R955 becomes one explicitly normalized moment, and that moment is compared to the original full trace by a proved nonzero, explicit scalar. It does not prove the moment nonzero.

The scalar Serre rule and the original companion's degree-$N$ differential equation were already proved in R939 and are reused as such. The new content is the complete opposite-deck operator, both full Cartier matrices, the one-moment preimage test, and its exact comparison with the original trace. There is no new numerical scan or local mathematical execution.

## 1. Keep the original phase, including the corrected minus sign

Throughout assume
$$
p\ge41,\qquad p\equiv11\pmod{12},\qquad
p=6N+5,
\tag{958.1}
$$
and retain $p\equiv2,5\pmod9$ for the original Serre application. Thus $r=2$, $w=p-1=6N+4$, and $N$ is odd. Work over $k=\mathbf F_{p^2}$ containing the original $s^2=-3$ and $\zeta=(-1+s)/2$; the same arguments hold after perfect scalar extension.

Use the original R936/R939 polynomial data
$$
t=u^3,\quad D=1-4t,\quad
\mathcal A=uD^{N+1}H(t),\quad
\beta=-(1-8t)H-3tDH'.
\tag{958.2}
$$
The degree of $H$ is $N$, it is squarefree, and $H(0),H(1/4)\ne0$. The finite algebras below are therefore étale:
$$
L_1=k[t]/(tH),\qquad L_0=k[t]/H.
\tag{958.3}
$$
The images of $D$ and $\beta$ are units in both, and $t$ is a unit in $L_0$. R939 proves, in the whole $L_1$,
$$
\beta^{p-1}=1.
\tag{958.4}
$$

Every scalar evaluation is in the corrected original family and Hodge frame
$$
E_u:y^2=x_E^3+3uD x_E+D(1/2-4t),\qquad \rho=dx_E/(2y).
$$
In particular R939 gives
$$
E_4=-144uD,\quad V_4^\dagger=12sD,\quad
\eta^{12}=-6sD,\quad
\mathcal B=-D^{N+1}\beta,\quad
\operatorname{KS}(\rho^2)=du/D.
\tag{958.5}
$$
Let $C$ be **the unchanged polynomial named $C$ in R936/R939**. Since $J=N$ is odd, the actual high-weight form is
$$
\boxed{F=V_{p-1}^\dagger,\qquad F(E_u,\rho)=-D^{N+1}C(t).}
\tag{958.6}
$$
The minus sign in (958.6) is retained below. It is not a new phase convention.

## 2. The complete two deck spaces as polynomial spaces

R918/R920 prove that $v=V_4^\dagger$ has exactly the minimal cusp and elliptic zeros forced on a cusp form of weight congruent to four modulo six. The same divisor argument used in R920(920.14) therefore gives, for every $N\ge0$,
$$
S_{6N+4}(H_6)=v\,M_{6N}(H_6).
\tag{958.7}
$$
Indeed division removes the one cusp zero and the forced fine zero at each order-three point, and $v$ has no other zero. Conversely multiplication by $v$ produces the required cusp form. These statements hold on the full residual lattice because the tame stabilizer orders are units and the divisor calculation is the original integral one.

The weight-$6N$ line descends to the coarse $\mathbf P^1_u$. The form $(\eta^{12})^N$ is nonzero away from the cusp and has order $3N$ there, so
$$
M_{6N}(H_6)=(\eta^{12})^N k[u]_{\le3N}.
\tag{958.8}
$$
Its degree is $3N$, as already seen for $N=1$ in R920(920.16). Since $v(\eta^{12})^N$ evaluates to the nonzero constant $12s(-6s)^N$ times $D^{N+1}$, the complete scalar-evaluated space is
$$
S_{p-1}(H_6)(E_u,\rho)=D^{N+1}k[u]_{\le3N}.
\tag{958.9}
$$

The deck labels are fixed geometrically after the original determinant correction. Use R939's actual identity
$u=E_4/(4sV_4^\dagger)$. Since $E_4$ is fixed and $v$ has actual character $\zeta$, this transported ratio has character $\zeta^2$. This states the direction of the transported ratio, not an identification with the pre-transport direction of $u$ in another marking. Both have the same fixed $u^3$. Also $\eta^{12}$ is deck invariant by R920(920.17–18). Consequently the two nontrivial deck spaces in (958.9) are exactly
$$
\begin{aligned}
S_w^+&=\{f_P:f_P(E_u,\rho)=D^{N+1}P(t),\ \deg P\le N\},\\
S_w^-&=\{h_K:h_K(E_u,\rho)=u^2D^{N+1}K(t),\ \deg K\le N-1\}.
\end{aligned}
\tag{958.10}
$$
They have dimensions $N+1$ and $N$. Here $+$ and $-$ mean the actual characters $\zeta$ and $\zeta^2$ under R913's once-fixed transport. In particular $F=f_{-C}$. The remaining deck-invariant summand is $uD^{N+1}k[t]_{\le N-1}$ and is not inserted into the original two-character source.

## 3. The two differential operators

R939(939.4) already proves the scalar rule
$$
\partial_k f=D\frac{df}{du}+2ku^2f.
\tag{958.11}
$$
For $w=p-1$, R946's order-two operator is
$\mathscr D_2=\partial_{w+2}\partial_w+E_4/144$. In the residue field $w=-1$, $w+2=1$, and $N+1=1/6$. Substitution in (958.11) gives
$$
\begin{aligned}
(\mathscr D_2 f_P)(E_u,\rho)
&=uD^{N+2}\,\mathcal L_+P,\\
(\mathscr D_2 h_K)(E_u,\rho)
&=D^{N+2}\,\mathcal L_-K,
\end{aligned}
\tag{958.12}
$$
where
$$
\mathcal L_+
=9tD\frac{d^2}{dt^2}
+6(1-12t)\frac d{dt}-9,
\tag{958.13}
$$
$$
\boxed{\quad
\mathcal L_-
=9t^2D\frac{d^2}{dt^2}
+6t(3-20t)\frac d{dt}+(2-49t).
\quad}
\tag{958.14}
$$
For clarity, here is a direct derivation of the new second formula, without appealing to a Fourier residue class. Put
$R=(2-12t)K+3tDK'$. The first Serre derivative of $u^2D^{N+1}K$ is $uD^{N+1}R$. The second, of weight $p+1$, is $D^{N+2}(R+3tR')$. The additional term $(E_4/144)u^2D^{N+1}K$ is $-tD^{N+2}K$. Hence its bracket is $R+3tR'-tK$, which expands to (958.14). All factors refer to the original $\tau'$ derivative; the Katz factor six has not been absorbed into it.

The first formula and the original $C$ equation are already R939 §6, with its factor three restored here:
$$
\mathcal L_+C=-(s/3)H.
\tag{958.15}
$$
The diagonal of $\mathcal L_+$ on $k[t]_{\le N}$ is $-9(2j+1)^2$ for $0\le j\le N$, so it is invertible on that space. This is exactly the uniqueness argument already registered in R939, and is not presented as a second new companion construction.

The new opposite-deck formula has the particularly simple columns
$$
\boxed{\quad
\mathcal L_-(t^j)
=(3j+1)(3j+2)t^j-(6j+7)^2t^{j+1}
\quad(0\le j<N).
\quad}
\tag{958.16}
$$
Its leading coefficient is nonzero: $6j+7\le6N+1=p-4$. Thus
$$
\mathcal L_-:k[t]_{\le N-1}\longrightarrow k[t]_{\le N}
\tag{958.17}
$$
is injective with cokernel of dimension one.

## 4. The complete Cartier matrices in finite étale algebras

Let $\operatorname{Fr}_p$ denote absolute $p$th power on either algebra $L_i$. It is additive, coefficient-Frobenius semilinear, and bijective because the finite algebras are étale over a perfect field. A notation $\operatorname{Fr}_p^{-1}$ below means its unique inverse. No unchanged-coefficient substitution $t\mapsto t^p$ is made in place of this map.

Put
$$
a=2D^{2N+1}\beta^2\in L_1^\times,
\qquad
c=t^{4N+3}a\in L_0^\times.
\tag{958.18}
$$
The two complete $p^{-1}$-semilinear Cartier maps, in the exact R952 notation $\mathscr U$, are
$$
\boxed{\begin{aligned}
\mathscr U(f_P)&=h_K,&
K&=\operatorname{Fr}_p^{-1}\!\left(c^{-1}\mathcal L_+P\bmod H\right),\\
\mathscr U(h_K)&=f_P,&
P&=\operatorname{Fr}_p^{-1}\!\left(a^{-1}\mathcal L_-K\bmod tH\right).
\end{aligned}}
\tag{958.19}
$$
On the first line the output is represented by its unique polynomial of degree at most $N-1$; on the second by degree at most $N$. Both are maps in the one fixed complete $H_6$ space of (958.10), with the actual geometric character change. The global root construction and marking return are R952's, not an extra copy of a conjugate marked space.

### Proof of the matrix formulas

For $r=2$, the pointwise formula R952(952.10) is
$$
(\mathscr D_2H)|_\Sigma
=\left.2\frac{(\mathscr U H)^p}{\mathcal B^{p-3}}\right|_\Sigma.
\tag{958.20}
$$
Since $p-3$ is even, (958.4–5) turn its right side, for an output $f_P$, into
$2D^{3N+3}\beta^2P^p$. Divide by the $D^{N+2}$ of the second line in (958.12), which is a unit at $tH=0$. This gives
$\mathcal L_-K=aP^p$ in $L_1$, proving the second formula.

For an output $h_K$, the corresponding right side is
$2u^{2p}D^{3N+3}\beta^2K^p$. Away from $u=0$, divide by $uD^{N+2}$ in the first line of (958.12). The exponent
$2p-1=3(4N+3)$ gives
$\mathcal L_+P=cK^p$ in $L_0$, proving the first formula. At $u=0$ the prospective target $h_K$ already vanishes and there is no missing interpolation condition. The $N$ distinct $H$ roots uniquely determine a polynomial of degree less than $N$.

The three $D=0$ elliptic points are still part of the full supersingular locus. Every form in (958.10), including every Cartier output, has its forced fine zero there. Formula (958.20) therefore vanishes there automatically. Equivalently (958.12) has the forced elliptic vanishing in its target weight. Omitting these points from the interpolation algebras does not omit a condition with a nonzero right side.

These arguments compute the actual globally existing root forms of R952. They do not deduce modularity from arbitrarily assigned supersingular values.

In particular, (958.19) supplies actual finite matrices without expanding the original CM theta series to precision of order $p^2$. In the monomial bases their columns are respectively
$$
\operatorname{Fr}_p^{-1}(c^{-1}\mathcal L_+t^j\bmod H),\quad 0\le j\le N,
$$
and
$$
\operatorname{Fr}_p^{-1}(a^{-1}\mathcal L_-t^j\bmod tH),\quad 0\le j<N.
\tag{958.21}
$$
These are formulas, not stored arrays or numerical output. Absolute Frobenius inverse in a finite étale algebra can equivalently be computed by its invertible semilinear matrix. Any execution of these formulas remains subject to the repository's public Actions rule.

The first arrow in (958.19) is surjective with kernel $kF$, by the invertibility of $\mathcal L_+$ and (958.15). The second arrow is injective, by (958.16). Thus the entire two-deck high-weight space, before Hecke localization, has Cartier kernel exactly $kF$ in this $r=2$ row.

## 5. A single normalized moment decides the actual preimage question

Define a $k$-linear functional $\ell_N$ on $k[t]_{\le N}$ by
$$
\ell_N(1)=1,\qquad
\frac{\ell_N(t^{j+1})}{\ell_N(t^j)}
=\frac{(3j+1)(3j+2)}{(6j+7)^2}
\quad(0\le j<N).
\tag{958.22}
$$
Every numerator and denominator here is a unit modulo $p$. In rising-factorial notation the same moments are
$$
\ell_N(t^j)=\frac{(1/3)_j(2/3)_j}{4^j(7/6)_j^2}.
\tag{958.23}
$$
This notation is only a rewriting of the displayed finite product. By (958.16) the functional annihilates the image of $\mathcal L_-$. Since both have codimension one,
$$
\operatorname{im}\mathcal L_-=\ker\ell_N.
\tag{958.24}
$$

Let $R_F$ be the degree-at-most-$N$ representative in $L_1$ of
$$
\boxed{R_F=-2D^{2N+1}\beta^2C^p\bmod tH.}
\tag{958.25}
$$
The sign is from the actual $F=f_{-C}$ in (958.6). The first power $C^p$ is absolute Frobenius in the same finite algebra, including all original coefficients.

The second Cartier arrow in (958.19) gives
$$
\mathscr U(h_K)=F
\iff \mathcal L_-K=R_F.
\tag{958.26}
$$
Congruence modulo $tH$ here is equality of the degree-at-most-$N$ representatives. Consequently
$$
\boxed{\quad
\text{the actual opposite-deck Cartier preimage exists}
\iff\ell_N(R_F)=0.
\quad}
\tag{958.27}
$$
If it exists it is unique in the entire opposite-deck space, by injectivity of $\mathcal L_-$. This is a full-space statement, so it does not require discovering a generalized CM eigenvector first. By R955 the preimage, when it exists, lies in the actual CM nilpotent chain and is precisely the first step of a chain of length at least three.

Over $k=\mathbf F_{p^2}$ one can also compose the two matrices in (958.21). If they are written $M_+,M_-$ with the coefficient action $x\mapsto x^{1/p}$ separate, then Cartier squared on $S_w^-$ has the actual $k$-linear matrix
$$
M_+\,\overline{M_-}.
\tag{958.28}
$$
It is singular exactly when (958.27) holds: $M_-$ is injective and the kernel of the next arrow is precisely $kF$. No assertion about its numerical determinant is made.

## 6. Exact comparison with the original whole trace

Keep
$$
e_0=H/H(0)\in L_1,
\qquad
T=\operatorname{Tr}_{L_1/k}\!\left((3-2e_0)D^{2N+2}C^{p+1}\right),
\tag{958.29}
$$
the unchanged $r=2$ trace of R939(939.19–20). Define another fully explicit linear functional on $L_1$ by
$$
M(R)=\operatorname{Tr}_{L_1/k}\!\left(
(3-2e_0)\frac{DC}{\beta^2}R\right),
\qquad c_{\rm mom}=M(1).
\tag{958.30}
$$
We claim
$$
\boxed{\quad M=c_{\rm mom}\ell_N,\qquad c_{\rm mom}\ne0.\quad}
\tag{958.31}
$$
The argument keeps all supersingular multiplicities. Apply R951's symmetric $r=2$ pairing to $h_K$ and the original $F$. Since $\mathscr D_2F=\mathcal A V_4^\dagger/36$, it vanishes along $\Sigma$, and R951 gives
$$
\sum_{P\in\Sigma}
\frac{(\mathscr D_2h_K)_P F_P}{b_P^2}=0.
\tag{958.32}
$$
By (958.5–6) and (958.12), the invariant scalar inside this sum, on the coarse $u$ curve away from $D=0$, is exactly
$$
-\frac{DC}{\beta^2}\,\mathcal L_-K.
$$
At the $D=0$ elliptic points both modular factors have their forced fine zeros, while the actual Hasse derivative is a unit in a regular frame; their contribution is zero. At every other coarse supersingular point R936's actual fine-cover degree is twelve. Above $t=0$ there is one coarse point; above every $H$ root there are three. Therefore the left side of (958.32) is exactly
$$
-12\operatorname{Tr}_{L_1/k}\!\left((3-2e_0)
\frac{DC}{\beta^2}\mathcal L_-K\right)=-12M(\mathcal L_-K).
\tag{958.33}
$$
The factor twelve is the already proved fine-cover degree in this invariant function calculation. It is not substituted for the distinct source degree $d_1$ in R932's original functional.

Since twelve is a unit, (958.33) proves that $M$ annihilates $\operatorname{im}\mathcal L_-$. Equation (958.24) makes $M$ a scalar multiple of $\ell_N$. This multiple is nonzero. Indeed the algebra $L_1$ is étale, so its trace pairing is perfect. The element
$(3-2e_0)DC/\beta^2$ is nonzero in $L_1$: the factors $3-2e_0,D,\beta$ are units, and the nonzero original $C$ has degree at most $N<\deg(tH)$. Thus $M$ is a nonzero functional. Finally $\ell_N(1)=1$, so its nonzero multiple is exactly $c_{\rm mom}=M(1)$. This proves (958.31). It proves a **linear** companion trace is nonzero, without using positivity or assuming the high-weight diagonal nonzero.

Substitute (958.25) in (958.30). All denominator and source signs cancel explicitly except the retained minus two:
$$
M(R_F)=-2T.
$$
Consequently
$$
\boxed{\quad
\ell_N(R_F)=-\frac{2}{c_{\rm mom}}T,
\qquad
c_{\rm mom}=
\operatorname{Tr}_{L_1/k}\!\left((3-2e_0)\frac{DC}{\beta^2}\right)\ne0.
\quad}
\tag{958.34}
$$
This is an exact, explicitly calibrated comparison. No unknown original source scalar has been absorbed into $c_{\rm mom}$: it is defined solely by the unchanged $H,C,\beta$ and actual full-point weights.

R939 gives $S^p=12(-6)^2T=432T$ in this row. Thus equivalently
$$
S^p=-216\,c_{\rm mom}\ell_N(R_F).
\tag{958.35}
$$
The original functional itself still includes R932's $m_{\mathrm I}$, $d_1$, and nonzero $c_h^{\mathrm F}$ exactly as written there. Formula (958.35) changes none of them.

## 7. What the formulas do and do not settle

The Cartier-preimage question is now a fully explicit finite polynomial question: form the unchanged $H,C,\beta$, reduce the **actual** $-2D^{2N+1}\beta^2C^p$ modulo $tH$, and evaluate the fixed moments (958.22). The two complete Cartier arrows are also explicit in (958.19), so higher nilpotent-chain questions can be addressed in the original spaces without guessing a Hecke packet or dropping coefficient Frobenius.

The proved nonzero number in (958.31) is $c_{\rm mom}$, not $\ell_N(R_F)$. Nothing in the unit values of the individual moments prevents their linear combination on $R_F$ from vanishing. Proving $\ell_N(R_F)\ne0$ for all allowed primes would exclude the actual longer Cartier chain in this row and prove the original high-weight trace nonzero. It remains to be done.

This result treats only $r=2$. It supplies no order-two formula for $r=8$, does not identify either high-weight trace with the original $Q'_h(0)$, and does not bypass R945's central zeros or the original rational-point problem.

## Dependencies

- R918/R920: the original full $H_6$ divisor, coarse line degree, residual base change and geometric deck labels.
- R936/R939: the corrected actual family, original $C$ and its sign, Hasse polynomial, Baker identity, scalar derivative and complete supersingular counts.
- R939 §6: the already proved fixed equation and uniqueness for the original $r=2$ companion.
- R951/R952: the complete obstruction pairing and its symmetry, and the exact complete-space Cartier formula with inverse coefficient Frobenius.
- R955: the actual opposite-deck preimage criterion and the single odd Cartier chain.

All new formulas are proved by the displayed symbolic algebra and actual residue pairings. No new mathematical computation or finite-prime scan has been executed.
