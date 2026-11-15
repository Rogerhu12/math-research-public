# One explicit static-positive outer point and a complete rational static oracle

## 1. The new actual target

This is a continuation of the published finite necessary system, not a new computation of the character head or the original Volterra functions. The preceding static/parity actual is run `43668125602`, source `c8a89721ee361074096b202af6aa0841ac1bc445`. Its complete certificate contains 68 exact halfspaces in the unchanged 23-coordinate parametrization of the original 107 normal generators.

The root subsequently identified a better immediate target than repeated static cuts. In the saved point, replace only

$$
y_{12}=-\frac{11}{48}\quad\longmapsto\quad-\frac12.
$$

The free-coordinate list identifies this coordinate with normal generator 73. The stored transform contains this free coordinate only in normal coordinates $0,1,9,10,73$. Reading every stored corrected scalar-family row shows that among all fourteen families these five normal coordinates occur only in the degree-zero and degree-two coefficients of $F_0$.

Consequently, the proposed point has

$$
a(k)=\frac12-\frac32k^2+k^4+k^6,
$$

while its quadratic and highest layers are unchanged. The new public actual checks this statement and **all 68 inherited halfspaces at this one specified rational point**. It does not search for another point, compute roots, add cuts, rebuild an equality system, or run an LP.

The full rational static oracle in Section 7 is implemented in the same independent source as a reusable utility, but the actual entry does not call it. Its only executions in this release are small artificial cases. The known explicit SOS makes a real oracle call for this candidate unnecessary.

## 2. Files and exact provenance

New source:

`scripts/literature_character_minus2_static_positive_candidate.py`

Suggested lane:

`character_minus2_static_positive_candidate`

Suggested actual output:

`character-minus2-static-positive-candidate.json`

The source imports the frozen `literature_character_minus2_static_cut.py` and its already-published exact finite-system engine. The actual never calls their old construction, RREF, LP or integration routines. Source identities are checked before either development or actual execution.

### Current complete system

Directory: `notes/actions-43668125602-1-character_minus2_static_parity`.

| File | Bytes | SHA-256 |
|---|---:|---|
| `character-minus2-static-parity.json` | 6971 | `bb2e66e4ddd6e0e826c8aa78cef96462e23290852f512b84ab0d3fceb800f968` |
| `receipt.json` | 40112 | `947bbcd35c08476233568a67c8f6b4c322bf8991284b8c9382fc65fea2ccd6d2` |
| `character-minus2-static-parity-certificate.json.gz` | 9222 | `2431172cb890ad9d6bc7fa227793fabd9a33e5f254531ff2411b6fbc6870e3af` |
| Certificate raw JSON | 34807 | `f15004c94a2400bf9fed2e9705227ba2cd1ca2dacc38080a25bf703e9f27ef23` |

Its producer is 18508 bytes, SHA-256 `9e7f7d2b9b70b78a3eec17f8c4c2e4cd64caf8d6304247355aaff55c962f41e1`.

### Original coefficient and coordinate interpretation

The current certificate deliberately does not duplicate the entire original 107-to-23 transform and fourteen linear polynomial families. The fourth input is therefore the already-published complete certificate:

`notes/actions-43665971895-1-character_minus2_finite_necessary/character-minus2-finite-necessary-certificate.json.gz`.

It is 31976 packed bytes, SHA-256 `5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634`; its raw JSON is 143028 bytes, SHA-256 `dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7`. The source actual is `05bb659b59997906316ddd2873aedbf4840f62a5`, run `43665971895`.

The consumer verifies the current main and publication receipt, current packed/raw certificate identities, producer bytes, and the embedded binding to this original certificate. It also checks the original equalities, inequalities, RREF, transform, path-integral metadata and reduced-row hashes against the unchanged-data record already stored in the current certificate. These are read-only identity checks; none is reconstructed. The current first 63 row records must be byte-equivalent JSON objects to the original reduced-row prefix. All 68 current records are retained in the new certificate.

## 3. Full support and coordinate checks

Before evaluating the candidate, the consumer reads **every** saved degree of every one of the fourteen scalar families. Each stored normal-coordinate linear form is substituted into the archived exact transform $x=B y$.

For the static family the only permitted nonzero transformed degrees are $0,2,4,6$. Every other stored degree, including an odd degree or a degree greater than six, must give the exactly zero rational row. A nonzero unsupported degree is an implementation/input failure. The program never discards a coefficient because the expected shape is even sextic.

The free-coordinate list must be unchanged, and the corresponding rows of $B$ must remain the coordinate unit rows. The candidate is copied before its one-coordinate replacement. The source checks that only free coordinate 12 changed and that its normal index is 73. Both points are nonzero and lie in the normalization box $|y_j|\le1$.

The complete candidate, all 107 normal values and all fourteen scalar polynomials are saved. For each of the thirteen nonstatic families the new polynomial is compared coefficient by coefficient with the saved parent's polynomial, including explicit zero entries. The current source applies the old layer certificates only if these complete comparisons and the prescribed coefficient comparisons succeed.

## 4. Expected exact scalar result and its meaning

The proposed fourteen polynomials are

| Family | Scalar polynomial |
|---|---|
| $F_0$ | $\tfrac12-\tfrac32k^2+k^4+k^6$ |
| $Q2_0$ | $1+k^2$ |
| $Q2_1$ | $-k-k^3$ |
| $Q2_2$ | $1+k^2+k^4$ |
| $\bar A_{hh}$ | $1+k^2$ |
| $\bar A_{hk}$ | $-k$ |
| $\bar A_{kk}$ | $1$ |
| $H_1$ | $-k$ |
| $H_2$ | $-1$ |
| $Q4_0,Q4_1$ | $0,0$ |
| $Q4_2$ | $1$ |
| $Q4_3$ | $-k$ |
| $Q4_4$ | $1+k^2$ |

The same archived multiplier/cocycle rows must give, in the order $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$,

$$
\mu=(0,1,2,0,0,0,0,4),\qquad
c=0,\qquad d=(0,2,6,0,0,0,0,8).
$$

Writing $x=k^2$,

$$
a(k)=(x+2)\left(x-\frac12\right)^2+\frac{x}{4}\ge\frac1{16}.
$$

Indeed, $x\ge1/4$ gives $x/4\ge1/16$. For $0\le x\le1/4$, the first term is at least $2(1/4)^2=1/8$.

The quadratic layer has the already-proved SOS

$$
(1+k^2)\left(k_s-\frac{k r_s}{2}\right)^2
 +\left(1+\frac34k^2+\frac34k^4\right)r_s^2,
\qquad r=\log h.
$$

R172 supplies the exact highest-layer certificate with its two parameters equal to $-1$ and Gram part

$$
\left(Z_1+\frac12Z_2+\frac12Z_3-Z_4\right)^2
 +\frac{11}{4}\left(Z_2+\frac3{11}Z_3\right)^2
 +\frac6{11}Z_3^2+Z_4^2.
$$

R173 states the resulting strict positive lower bound for the complete scalar action. The new actual does not reproduce these paper identities or solve a Gram problem: it verifies that the newly read complete coefficients are precisely those to which the identities apply.

Even if every check succeeds, this is a nonzero point of the **necessary external coefficient system** with a positive formal scalar action. It has not yet been shown to descend to a linear functional on the actual original-function space. Additional genuine two-mode dependencies may cut it. In particular, the consumer does not claim a true positive character, an obstruction to bending, payment of the full period/ruling, or an original-function membership result. The sibling raw-expression consumer is the separate interface for these missing dependencies.

## 5. Actual work and output boundaries

The actual performs only:

1. The four immutable input and source checks.
2. Read-only substitution of the already stored finite linear forms into the already stored transform.
3. One explicit rational coordinate replacement.
4. Evaluation of all 68 stored halfspaces and all fourteen scalar families at that point.
5. Exact comparison with the prescribed coefficients, unique multiplier and cocycles.

No `rref`, `construct_system`, `path_integrals`, `certify_zero`, `rational_dual_proposal`, `rational_outer_candidate`, profile evaluation, forcing compiler or normal form is called. No old source expressions are decoded.

Main schema: `visible-flex-character-minus2-explicit-static-positive-candidate-v1`. The complete certificate has the same name with `-certificate` appended. It stores all 68 values and row records, all 107 normal values, both points' full scalar polynomials, original static-support verification records and exact provenance. The main contains the fourteen-polynomial table, multiplier/cocycle values, failed-row indices if any, and certificate packed/raw metadata.

`completion=complete` means the one-point verification completed. Its `explicit_outer_point_verified` field distinguishes success from a mathematical failure of one of the candidate checks. `positive_character_excluded` and `true_positive_character_constructed` remain false in either case.

Default limits are 120 seconds, polled RSS 512 MiB, rational coefficient ceiling 16384 bits, main below 95000 bytes, certificate below 4500000 bytes and total below 4800000 bytes. These are explicit abort/report limits, not interval certification. Resource or implementation failures retain a scoped partial report. No successful assertion is retained if output truncation prevents the required complete certificate from being saved.

The actual entry requires both `GITHUB_ACTIONS=true` and `GITHUB_REPOSITORY=Rogerhu12/math-research-public`. Development is artificial-only.

## 6. Deployment command

From `topics/visible-flex-new-mechanism`:

```bash
python scripts/literature_character_minus2_static_positive_candidate.py \
  --toy-only \
  --output notes/current-character-static-positive-development.json
```

Then the unique actual, after R172/R173 are published:

```bash
python scripts/literature_character_minus2_static_positive_candidate.py \
  --source-report notes/actions-43668125602-1-character_minus2_static_parity/character-minus2-static-parity.json \
  --source-publication notes/actions-43668125602-1-character_minus2_static_parity/receipt.json \
  --source-certificate notes/actions-43668125602-1-character_minus2_static_parity/character-minus2-static-parity-certificate.json.gz \
  --original-system-certificate notes/actions-43665971895-1-character_minus2_finite_necessary/character-minus2-finite-necessary-certificate.json.gz \
  --output notes/current-character-static-positive.json
```

The workflow may use its normal staging/output paths; all mathematical source identities and input hashes are fixed inside the consumer.

## 7. Reusable complete rational oracle, not an actual target in this release

After the complete support check, an arbitrary rational candidate gives

$$
p(x)=a x^3+b x^2+c x+d,\qquad x=k^2\ge0.
$$

Trailing zero coefficients are removed exactly. Degree above three is rejected. The oracle either returns a complete nonnegativity certificate on the half-line or a rational $k$ with the directly verified strict inequality $p(k^2)<0$.

### Endpoint, infinity and lower degrees

If $d<0$, take $k=0$. A nonnegative constant is settled immediately. If the nonzero leading coefficient $a_n$ is negative, let

$$
M=\max_{i<n}\left|\frac{a_i}{a_n}\right|,\qquad R=1+M.
$$

For $x\ge R$, the geometric-series estimate gives

$$
\sum_{i<n}|a_i|x^i<|a_n|x^n,
$$

with the $M=0$ case immediate. Choosing the integer $k=\max(1,\lceil R\rceil)$ yields $k^2\ge R$ and hence a strict negative witness. The program verifies its exact value rather than relying only on the bound.

For a positive linear leading coefficient, the minimum is at zero. For $p(x)=a x^2+b x+d$ with $a>0$, a positive vertex occurs exactly when $b<0$; its location is $r=-b/(2a)$ and its sign is the sign of $4ad-b^2$. Otherwise the endpoint suffices. Equality is allowed and gives a genuine double zero.

### Positive cubic leading coefficient

Let

$$
\Delta=b^2-3ac.
$$

If $\Delta\le0$, the derivative is nonnegative. If $\Delta>0$, the local minimum is

$$
r=\frac{-b+\sqrt\Delta}{3a},
$$

and it is positive exactly when $b<0$ or $c<0$. If it is absent from the open half-line, the endpoint suffices. Otherwise set

$$
T=2b^3-9abc+27a^2d.
$$

Direct substitution gives

$$
p(r)=\frac{T-2\Delta\sqrt\Delta}{27a^2}.
$$

Consequently this minimum is nonnegative exactly when

$$
T\ge0,\qquad T^2\ge4\Delta^3.
$$

Every quantity in these sign tests is rational. No approximate square root is used, and repeated-root equality is distinguished from an arbitrarily small strict negative value.

### Strict-negative minimum to a rational $k$

For a rational quadratic minimum, compare $k^2$ directly with $r$. For a cubic minimum compare $z=3a k^2+b$ with $\sqrt\Delta$: $z<0$ is automatically below it, while $z\ge0$ is compared using $z^2-\Delta$.

An initial rational interval $0<\sqrt r<K$ follows from

$$
r\le\frac{|b|+\Delta+1}{3a}
$$

in the cubic case; a corresponding elementary rational bound applies to the quadratic. Repeated dyadic bisection in $k$ maintains this interval. At each midpoint the program first evaluates $p(k^2)$ exactly and returns when it is negative. Because the exact minimum is strictly negative, continuity gives a nonempty negative neighborhood; bisection therefore terminates in finitely many steps absent the declared resource ceiling. A resource ceiling returns an unresolved status, never a false global-nonnegative certificate.

This is a complete classifier for an individual rational polynomial. It does not prove finite termination of any future outer-cone cutting process. No such process is included in the current actual entry.

## 8. Artificial development boundary

New artificial cases cover zero/constant/linear polynomials, negative infinity behavior, quadratic minima, cubic derivative degeneracies, a double zero, strict negative irrational critical values and a tiny rational perturbation below a double zero. Every negative result is checked by direct rational substitution at its returned $k$.

Independent toy coordinate data check that a stored odd/high degree can be retained only when its transformed coefficient is exactly zero; a nonzero such degree is rejected. Other tests check copy-only coordinate replacement, exact detection of positive/zero/negative archived rows and forbidden-call guards for old RREF, system construction, path integration and LP helpers.

These development tests read no published mathematical input and do not evaluate the actual candidate or its oracle. The actual's complete bound input chain is checked only in the public Actions run. No new research calculation has been run locally.
