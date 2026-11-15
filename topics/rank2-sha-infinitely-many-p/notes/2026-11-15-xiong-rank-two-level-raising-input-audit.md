# Audit of the claimed rank-two BSD argument in Wang's February 2026 manuscript

Date: 2026-11-15.

Status: the manuscript does **not** supply an input for O4 or O6. Its starting quadratic field and its stated level-raising primes violate necessary local conditions. Independently, its passage from a nonzero complex central value to a zero Iwasawa $\lambda$-invariant is unsupported by the cited source. This note concerns that argument, not the truth of BSD.

## 1. Sources and exact scope

The audited source is Xiong Wang, *The Birch and Swinnerton-Dyer Conjecture for Analytic Rank Two: A Complete Proof via Definite Anticyclotomic Iwasawa Theory*, February 2026 manuscript, author upload dated 2026-03-01, DOI [10.13140/RG.2.2.14539.86569](https://doi.org/10.13140/RG.2.2.14539.86569). The [author-uploaded full text](https://www.researchgate.net/publication/401385931_The_Birch_and_Swinnerton-Dyer_Conjecture_for_Analytic_Rank_Two_A_Complete_Proof_via_Definite_Anticyclotomic_Iwasawa_Theory) was read at Definitions 6.1 and 6.8, Proposition 6.3, Proposition 10.2, Theorem 11.1, and Theorem 15.10.

Two original references were checked directly:

- K. A. Ribet, [*Raising the Levels of Modular Representations*](https://math.berkeley.edu/~ribet/Articles/dpp.pdf), Theorem 1, p. 3.
- Dac-Nhan-Tam Nguyen, [*On $\lambda$-invariants of congruent modular forms in the anticyclotomic, indefinite setting*](https://arxiv.org/abs/2510.12890), v1, 2025-10-14; [full PDF](https://arxiv.org/pdf/2510.12890).

No numerical experiment or unproved nonvanishing assertion is used below.

## 2. The initial quadratic field cannot satisfy the stated conditions

Wang's Definition 6.1 requires an imaginary quadratic field $K$ with $(D_K,Np)=1$, every prime dividing $N$ split in $K$, and $\epsilon(E/K)=+1$. Proposition 10.2 additionally requires $L(E\otimes\chi_K,1)\ne0$ for an analytic-rank-two curve.

Here is the local calculation, including the archimedean place. At a finite bad prime $\ell$ of $E$, splitting gives two copies of the original local representation; their root numbers multiply to

$$
w_\ell(E/\mathbf Q)^2=1.
$$

At every other finite place the curve has good reduction, which remains good after base change, so its root number is $1$. An imaginary quadratic field has **one complex place**. For the weight-two elliptic-curve representation its local root number is $-1$. Consequently

$$
\epsilon(E/K)=-1. \tag{1}
$$

This calculation works for arbitrary conductor exponents at the split bad primes. It is not a semistability qualification.

Equivalently, the quadratic-twist root-number formula in this coprime situation gives

$$
\epsilon(E\otimes\chi_K)
 =\chi_K(-N)\epsilon(E)
 =-\epsilon(E), \tag{2}
$$

since $\chi_K(\ell)=1$ for every $\ell\mid N$ and $\chi_K(-1)=-1$. Analytic rank two implies $\epsilon(E)=+1$, so the twist has sign $-1$ and

$$
L(E\otimes\chi_K,1)=0. \tag{3}
$$

The source's Proposition 6.3 counts the complex contribution incorrectly. Thus its initial admissible $K$ does not exist. A quadratic-twist nonvanishing theorem cannot produce a field inside this empty set.

For comparison, under the generalized Heegner hypotheses the all-split case belongs to the indefinite, sign-minus situation. One inert bad prime changes the quaternionic parity. It cannot be inserted while preserving all the original all-split hypotheses and the same Selmer module without an explicit comparison.

## 3. The selected auxiliary primes prohibit the asserted level raising

The source's Definition 6.8 and Theorem 11.1 impose the inequality

$$
a_q(E)^2\not\equiv(q+1)^2\pmod p.
$$

Theorem 15.10, Step 0, makes this explicit by selecting $q'\equiv-1\pmod p$ with $p\nmid a_{q'}(E)$.

For $q\nmid Np$, a weight-two, trivial-nebentypus $q$-new form at level $Nq$ is locally an unramified twist of Steinberg. If it is residually congruent to the good-at-$q$ original form, the residual semisimplification at $q$ has eigencharacters $\varepsilon$ and $\varepsilon\chi_{\mathrm{cyc}}$, where $\varepsilon(\operatorname{Frob}_q)\in\{1,-1\}$. Hence the necessary trace condition is

$$
a_q(E)\equiv\varepsilon(\operatorname{Frob}_q)(q+1)\pmod p,
\qquad
a_q(E)^2\equiv(q+1)^2\pmod p. \tag{4}
$$

Ribet's original Theorem 1 uses precisely this equality, in the notation where his level-raising prime and residual characteristic are interchanged relative to ours.

When $q\equiv-1\pmod p$, (4) requires

$$
a_q(E)\equiv0\pmod p. \tag{5}
$$

Thus the primes selected in the manuscript do not merely fail a sufficient hypothesis: they fail the necessary local condition for the asserted residual congruence to a $q$-new form. This is independent of (1).

The source's two auxiliary primes $q,q'$ are two asserted level-raising constructions. Their mere number is not a proof that the original Kolyvagin system has a primitive class at its first two-node level.

## 4. The cited $\lambda$ comparison does not compare these two modules

The arXiv identifier in Wang's bibliography is 2510.12890. Its actual author and title are those listed in Section 1, rather than the bibliographic name/title printed in that manuscript.

Nguyen's Theorem 3.5 assumes the all-split Heegner condition for both levels, ordinarity and residual irreducibility, $\mu=0$, and absence of finite nonzero submodules. Its $\lambda$ is that of the torsion part of a rank-one anticyclotomic module. The elliptic-curve criterion, Theorem 3.8, assumes a nontorsion Heegner point and an exact $p$-primary index/Tamagawa equality. Section 4 contains Example 4.1, not the “Theorem 4.8” cited by Wang. Appendix A explicitly retains local invariant quotients when comparing residual and divisible-coefficient Selmer conditions. These are features of the original theorem, not hypotheses that can be dropped because the residual representations agree.

There is also a direct local reason not to replace a split correction by twice an inert correction. Let $\Gamma\simeq\mathbf Z_p$ be the anticyclotomic Galois group and let $v$ lie over an inert rational prime $q\ne p$. Its Frobenius is fixed by complex conjugation, whereas conjugation acts on $\Gamma$ by inversion. Therefore

$$
\operatorname{Frob}_v=\operatorname{Frob}_v^{-1}.
$$

For odd $p$, $\Gamma$ has no nontrivial element of order two, so $\operatorname{Frob}_v=1$. Inert primes split completely in this extension; they do not have the finite-decomposition behavior used for the split local terms. The proposed automatic factor of two does not establish equality of the original and level-raised Selmer conditions.

This observation does not exclude every possible generalized comparison theorem. It shows that the cited theorem and its local terms do not supply the comparison used here.

## 5. Complex nonvanishing is not a $p$-unit conclusion

Even after repairing the two preceding construction errors, a further independent step remains. Wang's Theorem 15.10, Step 1, replaces a nonzero central value of the auxiliary form by $\lambda_{\mathrm{ac}}=0$.

The following exact Iwasawa-algebra example isolates the missing implication. Put

$$
\Lambda=\mathbf Z_p[[T]],\qquad X=\Lambda/(T+p).
$$

Then $X\simeq\mathbf Z_p$ as a $\mathbf Z_p$-module. It has no nonzero finite $\Lambda$-submodule, its characteristic power series has $\mu=0$ and $\lambda=1$, and

$$
X/TX\simeq\mathbf F_p,\qquad (T+p)|_{T=0}=p\ne0. \tag{6}
$$

Thus finite base-level coinvariants, no finite submodule, and nonzero augmentation of the characteristic power series do not force $\lambda=0$.

In an actual rank-zero main-conjecture application, an appropriate algebraically normalized special value being a $p$-unit, with the genuine Euler, period, and control factors retained, can supply a unit characteristic series. A complex value merely being nonzero does not supply that integrality conclusion. In particular, the statement that all but finitely many primes fail to divide one fixed algebraic number cannot be used when the auxiliary newform and quadratic field themselves depend on $p$.

This is not a counterexample involving an elliptic curve. It is a counterexample to the algebraic inference used to pass from the asserted control data to $\lambda=0$.

## 6. Consequence for the original problem

The audited argument gives neither:

1. a valid first-support or two-node primitivity theorem for the original Kolyvagin system; nor
2. an upper bound of two for the full original $p^\infty$-Selmer corank; nor
3. a new infinite set of primes for which the full $\Sha(E/\mathbf Q)[p^\infty]$ is finite.

For an already known rank-two fixed curve such as the original non-CM candidate, the lower bound on Mordell–Weil rank is not the missing implication. The missing assertion concerns the extra full Selmer directions, or equivalently the required original global divisibility/primitivity condition. Eventual nontriviality of derived classes and a nonzero complex value of a varying auxiliary form do not settle that assertion.

The two local contradictions above already prevent application of the claimed theorem. The $\lambda$ example and the original Nguyen hypotheses record why correcting typography alone would not close O4 or O6. No conclusion about the intended BSD statement is inferred from the failure of this particular proof.
