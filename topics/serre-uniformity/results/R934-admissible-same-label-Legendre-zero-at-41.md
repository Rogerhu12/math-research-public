# R934: An admissible zero of the original same-label Legendre factor at p = 41

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: proved exact counterexample to the all-prime auxiliary nonvanishing statement.** The counterexample is to the proposed Legendre nonvanishing condition, not to Serre uniformity. The already completed level-41 classification R707 is unchanged. A claim restricted to sufficiently large primes is not disproved by this result.

## 1. Statement and original scope

Take
$$
p=41,\qquad s^2=-3,\qquad x=s^{-1},\qquad
m=(p-1)/2=20,\qquad h=(p+9)/2=25.
$$
Then, in $\mathbf F_{41^2}$,
$$
\boxed{P_{h-1}(x)=P_{24}(x)=0.}
\tag{934.1}
$$
This is the same label as R920/R929, with the same square root and argument. It is within the original residual range: $41\equiv5\pmod{12}$ and $41\equiv5\pmod9$. Also $\gcd(h,p+1)=\gcd(25,42)=1$. There is no replacement by another $h$, a half-period shift, or a different evaluation point.

The unshifted unit from R929 remains nonzero. Thus its ordinarity theorem and (934.1) are compatible.

## 2. Complete finite-coefficient proof

The finite expansion
$$
P_n(1-2T)=\sum_{j=0}^n
\frac{(-n)_j(n+1)_j}{(j!)^2}T^j
$$
implies $P_{24}(X)=P_{16}(X)$ over $\mathbf F_{41}$. Indeed the parameters for $n=24$ reduce to $(17,-16)$ and those for $n=16$ are $(-16,17)$. The terms with $j\le16$ agree; for $17\le j\le24$ the numerator has a zero factor, while every $j!$ is invertible. This proves equality as polynomials.

Since $x^2=-1/3=27$ in $\mathbf F_{41}$, the usual finite coefficient formula gives
$$
2^{16}P_{16}(x)
=\sum_{j=0}^{8}(-1)^j
\frac{(32-2j)!}{j!(16-j)!(16-2j)!}\,27^{8-j}.
\tag{934.2}
$$
All factorials in the denominators have index less than $41$. Reducing the nine displayed summands, in their indicated order, gives
$$
13+24+14+16+38+11+1+10+37
=164=4\cdot41=0.
\tag{934.3}
$$
The factor $2^{16}$ is a unit. Equations (934.2)–(934.3), together with the polynomial equality, prove (934.1). This is a finite arithmetic proof; it does not rely on an inference from a large empty search window.

For comparison with the precise R929 formula, the same recurrence gives
$$
P_{20}(x)=13,\qquad xP'_{20}(x)=4.
$$
Consequently its exact four-step expression is
$$
\frac{169\cdot13+896\cdot4}{105}=0
\quad\text{in }\mathbf F_{41},
$$
since its numerator is $5781=141\cdot41$, whereas $105$ is invertible. The proof of the zero itself already follows from (934.2), independently of these two additional values.

## 3. Fixed-differential consequence

Retain R933's fixed curve and differential
$$
E_*:v^2=w^3+6w+7,\qquad
\omega=\frac{dw}{2v},\qquad
\beta=(224w-283)\omega.
$$
By the fully proved source comparison R933, (934.1) is equivalent to
$$
\mathcal C(\beta\bmod41)=0.
$$
Here $\beta\bmod41=(19w+4)\omega$. In particular the actual fixed second-kind differential has a rational primitive in characteristic $41$, explicitly of R933(LS13)'s form
$$
\frac1{2v^{41}}
\sum_{\substack{0\le k\le61\\k\ne40}}
\frac{[w^k]\big((19w+4)(w^3+6w+7)^{20}\big)}{k+1}\,w^{k+1}.
$$
The omitted coefficient is zero by R933 and (934.1); every other denominator is a unit. This consequence does not assert that $\beta$ is exact in characteristic zero.

## 4. Reproducible public computation and its narrower role

The new open-factor computation was performed in this public repository:

- Script: `topics/serre-uniformity/scripts/same_label_legendre_window.py`.
- Script SHA-256: `5967887973fefb6538028c1d3b9fc9ceae7902be65a66c475d12ed92213bc255`.
- Parameters: `--bound 100000 --stop-after 0 --output /tmp/legendre-shift-window.json`, without `--allowed-mod9`.
- Source commit: `6a9e3137f825248eaed3b9cb24ece7ea96067e8c`.
- Successful [run 44711592515](https://github.com/Rogerhu12/math-research-public/actions/runs/44711592515), 2026-11-20 09:32 UTC.
- Deterministic output SHA-256: `5c670a06f48ce45e7306c9147d28e7e58de4ae0ed4432519bfb13dbd5abb6bca`.
- Ordered row-stream SHA-256: `51bc76595d38358622e27b0bdcb783bd0244e1e34a5a77db3456068535d117e7`.

It tested all 2406 primes $41\le p\le100000$, $p\equiv5\pmod{12}$ (last prime 99989), and found only $p=41$ as a zero. Every prime was checked against the exact shifted expression; a zero was additionally checked with the independent finite coefficient formula. The wider statement about the finite window is computational evidence only. It is not a proof that no further zero exists, and it is not a uniformity theorem. No row dataset, output artifact, or certificate array is committed.

## 5. Consequences for the active research target

The target “the R920 label has nonzero Legendre factor at every allowed prime” is false and is closed in that form. This does **not** close the following possibilities:

1. nonvanishing for all sufficiently large allowed primes;
2. choosing another actual primitive label with the correct CM companion and a nonzero factor;
3. deriving a uniform bound by another source comparison or the actual global height.

In particular R925's product criterion cannot give a nonzero $J_{32}$ at this label, irrespective of $Q'_h(0)$. No conclusion about $Q'_h(0)$ itself follows. R932's complete supersingular pairing is a separate scalar and is not forced to vanish merely by this Legendre zero.

## Dependencies

- [R929](R929-original-Legendre-auxiliary-ordinary-curve-and-central-shift.md): the original label and exact shifted expression.
- [R933](R933-same-label-Legendre-factor-and-fixed-Cartier-differential.md): the fixed-curve Cartier comparison and the explicit primitive criterion.
- [R707](R707-complete-level41-rational-point-classification.md): the previously closed fixed-level classification, not rerun here.
