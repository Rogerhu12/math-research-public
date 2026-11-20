# R973: certified original balanced Kronecker coefficients at four primes

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: completed finite public computation.** For the actual curve \(E_0:y^2=x^3-1\), differential \(dx/(2y)\), invariants \(g_2=0,g_3=4\), and canonical sigma function with no Gaussian factor, the four new coefficients
\[
c_n=[z^n w^{n-1}]\frac{\sigma(z+w)}{\sigma(z)\sigma(w)}
\]
at \(n=p-r\), \(r=8,2,2,8\) for \(p=41,47,227,857\), respectively, are all \(p\)-adic units. Their residues are \(13,4,171,317\).

The exact rational calculation and a separately reduced calculation using the original first sigma pole agree in every case. This is a four-prime result. It does not prove a general unit theorem, and this receipt does not by itself identify these values with the original supersingular trace or its valuation.

## 1. Exact source and frozen execution

The complete formula, original signs and integrality proof were frozen before execution in the [R973 method](../notes/R973-original-balanced-Kronecker-four-prime-execution-method.md). In particular,
\[
\Theta(z,w)=\frac{\sigma(z+w)}{\sigma(z)\sigma(w)},\qquad
\sigma'(0)=1,\qquad \sigma(z)=z-\frac{z^7}{210}+\cdots.
\]
The normalization check is exactly \(c_3=-1/6\). The coefficient has homogeneous modular weight \(2n\). The distinct high CM source has modular-form weight \(n+1\); these two weights are not equated.

The Eisenstein–Kronecker convention is that of Bannai–Kobayashi, [Theorem 1.17](https://arxiv.org/pdf/math/0610163):
\[
c_n=-\frac{e^*_{n-1,n+1}(0,0)}
              {(n-1)!\,\mathcal A^{n-1}},
\qquad \mathcal A=\operatorname{Area}(\mathbf C/\Lambda)/\pi.
\]
A separate Manin-period and adjoint comparison is required before using this coefficient in the R970 criterion.

The actual public execution is:

- Run: [44740851091](https://github.com/Rogerhu12/math-research-public/actions/runs/44740851091), successful.
- Job: [136303836405](https://github.com/Rogerhu12/math-research-public/actions/runs/44740851091/job/136303836405), all steps successful.
- Source commit: f3f947dab32911ac0a40040ceb24242d4595488d.
- Consumer: [original_balanced_kronecker_four_prime_consumer.py](../scripts/original_balanced_kronecker_four_prime_consumer.py), SHA256 240a7053fb713b2084e84117182b70da92f8c75fb2870a6a7272b186719721df.
- Method SHA256: 32d4c836cacbb0467c668a4a968be62fe759cd188a3365bdfb9da9583d076269.
- Frozen request SHA256: 2342777cb9d414b325f75f67a0c8929185f43a1eb342152324fd45406fde30c9.
- Runtime: public repository Actions, exact python-flint 0.9.0 rational arithmetic and integer binomials; 620-second internal ceiling.

The complete requested work finished in **15.197670298 seconds**, with no error, no nonunit result and no uncompleted tail. The workflow checked both README pins and the consumer hash. No old trace, moment window or same-label sigma product was recomputed.

## 2. Two calculations from the same original normalization

Write
\[
\sigma(z)=z\sum_{j\ge0}s_jz^{6j},\qquad
\frac z{\sigma(z)}=\sum_{j\ge0}b_jz^{6j}.
\]
The actual differential equation \(x''=6x^2\), with \(x'^2=4(x^3-1)\), determines the rational \(x\)-coefficients. Integrating \((\log\sigma)''=-x\) gives the \(s_j\). The \(b_j\) are independently produced by exponentiating the opposite logarithm, and the exact inverse identity is checked through the full needed prefix.

For \(n=6t+3\), the exact source is
\[
c_n=\sum_{u,v=0}^{t}
 b_u b_v s_{2t+1-u-v}
 \binom{6(2t+1-u-v)+1}{n+1-6u}.
\tag{973.1}
\]
One rational prefix through \(j=283\) supplies all four calculations.

The second calculation retains \(s_j,b_j\) only in their first integral block and uses the already proved original pole relation, for \(p=6N+5\),
\[
p\,s_{N+1+j}=-B\,s_j\pmod p,\qquad
B=(-1)^{(p-1)/2-(p-2)/3}
  \binom{(p-1)/2}{(p-2)/3}.
\tag{973.2}
\]
Every high-binomial term has exactly one factor of \(p\), which cancels the only possible sigma pole. The exact integer binomial is divided by \(p\) before reducing. The full argument is in the frozen method; it proves integrality, not nonvanishing. The consumer checks the original pole scale and then compares the resulting residue with the independently formed complete rational value.

## 3. Actual finite results

| \(p\) | row \(r\) | \(n=p-r\) | high CM weight \(n+1\) | coefficient weight \(2n\) | original \(B\bmod p\) | \(c_n\bmod p\) | \(v_p(c_n)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 41 | 8 | 33 | 34 | 66 | 11 | 13 | 0 |
| 47 | 2 | 45 | 46 | 90 | 10 | 4 | 0 |
| 227 | 2 | 225 | 226 | 450 | 179 | 171 | 0 |
| 857 | 8 | 849 | 850 | 1698 | 489 | 317 | 0 |

For every row, the exact value, independent pole reduction, original normalization check and original pole scale agree.

| \(p\) | last sigma index used | integral low summands | single-pole summands | exact-rational SHA256 |
|---:|---:|---:|---:|---|
| 41 | 11 | 21 | 15 | 0f5910539e2011956ef1bc2061daf5a24079958cd3fc93ea9199909823e18af8 |
| 47 | 15 | 28 | 36 | ea897b9576c8cd3dc8bfbf9791b56b1758177388b93661ebf3cab9eb3be0dd0e |
| 227 | 75 | 703 | 741 | fb2ae15beed52a847605c38e39baf8f32ca7266adff24f7f1b2fb9cce59bf9d2 |
| 857 | 283 | 10153 | 10011 | a9cc5ac67d3decb9f3138e440c4ff3c4c5b59f3e058c3a57b3387699ca7ab230 |

The rational hashes use the canonical JSON pair of numerator and denominator strings. The complete rational values remain in public stdout; they are not duplicated in Git. The primes 227 and 857 retain their role as the earlier central-failure labels, but the present coefficient is a new target. Their positive outcome does not reverse or weaken R945.

## 4. Root verification of the actual receipt

The root read the actual job stdout and reconstructed the canonical JSON records by pure text/JSON IO. It independently verified all four rational hashes and the following deterministic hashes:

| object | SHA256 |
|---|---|
| complete four-row list, 9,079 canonical bytes | 3539d7b331460ed69965c2cbaa48ddf45e7539c69e78f04e6a46f3554ee4b584 |
| prefix-ready record | 4aa3136e5baf8898cc16a30931fd49a41e567e011eaa39ab41335310ccb7492d |
| completion summary | 21210cd6d7391b999abc9f69e8c327561282f04fc1a932e9982d5a0e877a2552 |
| actual rational sigma prefix through \(j=283\), reported by the public consumer | 9b7baaa44a22644aa03f6e6c79d19f556df8181d4c7a927a983c184cd2353091 |

The last hash binds the mathematical prefix generated inside Actions; root did not regenerate that prefix locally. Raw logs and regenerable rational data stay out of Git and Releases. No artifact upload was used.

The finite computation is complete and must not be rerun merely to obtain the same four conclusions. The remaining proof tasks are the exact integral-period comparison with the high CM congruence ideal and a unit argument valid for every required prime. Neither the finite data nor the integrality of (973.1) establishes those tasks or the Serre-uniformity goal.

