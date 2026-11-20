# R945 — Original central sigma zeros, second coefficients, and same-label alternatives

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. **Status: proved finite counterexamples to an unqualified source-to-linear-coefficient implication, with exact finite same-label alternatives.** All new arithmetic was performed in the public repository's GitHub Actions. This is not a counterexample to Serre uniformity, and it does not exclude a theorem for all sufficiently large primes.

## 1. Exact statement in the original sources

Keep the original curve, branch, differential, and sigma normalization of R697–698 and R925:
$$
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad
x'=2y,\qquad y\sim-z^{-3},
$$
$$
(\log\sigma)''=-x,\qquad c=0,\qquad \sigma=z+O(z^7),
$$
$$
x\sigma^6=z^4\sum_{i\ge0}f_i z^{6i},\qquad
-xy\sigma^6=z\sum_{j\ge0}g_j z^{6j}.
\tag{945.1}
$$
Let $S$ denote precisely the complete supersingular sum in R932/R936, with the original two CM companions, all fine supersingular points, their actual weights, and the corrected positive Tate/Kodaira–Spencer convention. Let
$$
Q_h(w)=\overline{p^{-a_h}G_h(w)}=\sum_{j=1}^{J}q_{h,j}w^j
\tag{945.2}
$$
be the original calibrated normal function from R924–925, retaining the actual Tate-image index $a_h$.

The following equalities hold in the respective prime fields:

| $p$ | Original central $h$ | $r$ | Critical sigma factors | Complete $S$ | $Q'_h(0)$ |
|---:|---:|---:|---|---:|---:|
| 227 | 115 | 2 | $f_{18}=0$, $g_{18}=136$ | 95 | 0 |
| 857 | 433 | 8 | $f_{71}=176$, $g_{70}=0$ | 568 | 0 |

Both primes satisfy the actual source condition $p\equiv2\pmod9$. Their original central Legendre factors are nonzero, by the already recorded windows of R934 and R943. Therefore the original same-label fifth jet $J_{3,2}$ is zero in both cases because of its sigma factor, not because of its Legendre factor.

For those same original functions,
$$
q_{115,2}\ne0\quad(p=227),\qquad
q_{433,2}\ne0\quad(p=857).
\tag{945.3}
$$
In particular $Q_h$ has a zero of exactly order two at the center. It is not identically zero and is not an inseparable polynomial map. No additive-polynomial assertion is made.

There are also actual alternative labels at each of these two primes:

| $p$ | Alternative primitive $h$ | Same-label sigma product | Same-label Legendre factor | Consequence |
|---:|---:|---|---|---|
| 227 | 151 | $f_{24}g_{12}=166\cdot63=16$ | nonzero, from the previous selected-third window | original $J_{3,2}\ne0$ |
| 857 | 445 | $f_{73}g_{68}=187$ | $P_{444}(1/s)=P_{412}(1/s)=298$ | product $21\ne0$, hence original $J_{3,2}\ne0$ |

Here $s^2=-3$ is the original choice. The first label is one of the already proved legal third labels in commit `543d03f8`; the second is R935's original weight-34 label. At $857$ the fixed bad integer $B_{34}$ is a unit, so R938/R940 also give the actual $Q'_{445}(0)\ne0$. No R925 statement for the central labels is silently extended to $h=151$.

## 2. The first calculation and the independently derived second formula

The first public calculation used the original $z$ parameter. Write $v=z^6$ and
$$
x=z^{-2}X(v),\qquad y=z^{-3}Y(v),\qquad \sigma^6=z^6E(v).
$$
The equations $x''=6x^2$, $x'=2y$, and $(\log\sigma)''=-x$ give
$$
X_0=1,\quad X_1=\frac17,\quad
X_n=\frac{\sum_{j=1}^{n-1}X_jX_{n-j}}{(n-1)(6n+1)}\ (n\ge2),
$$
$$
Y_n=(3n-1)X_n,\qquad
\log E=-\sum_{n\ge1}\frac{X_n}{n(6n-1)}v^n,
\qquad \sum f_nv^n=XE,\quad \sum g_nv^n=-YXE.
\tag{945.4}
$$
The consumer also checks the independent first integral $Y^2=X^3-v$. Its 48-prime window was restricted to the original allowed primes between 109 and 1000, for which the complete trace had already been computed. The only central zeros in that window were the two in §1. This last window statement remains finite evidence only.

The second calculation does not reuse the $X,Y,E$ coefficient arrays. In the original algebraic parameter of R698, set
$$
u=x^{-1/2},\qquad w=u^6,\qquad
C=(1-w)^{-1/2},\qquad z=uZ(w),\qquad \sigma^6=u^6T(w).
$$
Since the original branch has $y=-u^{-3}\sqrt{1-w}$, one has
$$
dz=C(w)\,du,\qquad x\sigma^6=u^4T,\qquad -xy\sigma^6=uT/C.
$$
The exact original series are
$$
c_j=\frac{\binom{2j}{j}}{4^j},\qquad
C=\sum_{j\ge0}c_jw^j,\qquad
Z=\sum_{j\ge0}\frac{c_j}{6j+1}w^j,
$$
$$
h_j=\prod_{a=1}^{j}\frac{6a-4}{6a-1},\qquad
T=\exp\left(\sum_{j\ge1}\frac{h_j}{j}w^j\right).
\tag{945.5}
$$
All truncations used here are integral: the cutoff is $24$ at $p=227$, strictly below R698's $N=37$, and $71$ at $p=857$, strictly below $N=142$. In particular none of $j$, $6j+1$, or $6j-1$ in the required range vanishes modulo $p$.

Apply the residue change of variables to the coefficients in (945.1). For example,
$$
f_i=\operatorname{Res}_{z=0}\frac{x\sigma^6}{z^{6i+5}}\,dz
=\operatorname{Res}_{u=0}u^{-6i-1}T C Z^{-(6i+5)}\,du.
$$
The same calculation for $g_j$ cancels $C$. Thus the second algorithm uses
$$
\boxed{f_i=[w^i]TCZ^{-(6i+5)},\qquad
g_j=[w^j]TZ^{-(6j+2)}.}
\tag{945.6}
$$
No upper-end simplification such as $Z^p=1$ is used for these middle coefficients.

Unit inverses and integer powers are formed in the truncated polynomial ring. In addition to the defining convolutions, the second consumer checks
$$
C^2(1-w)=1,\quad Z+6wZ'=C,\quad H=CW,\quad wT'=T(H-1),
$$
and, separately for every negative power $S_e=Z^e$, the complete identity
$$
Z S_e'=e Z'S_e.
\tag{945.7}
$$
Here $H=1+\sum_{j\ge1}h_jw^j$ and $W$ is R698's integral auxiliary series. These are finite exact checks at the stated cutoffs, not floating-point evaluations.

## 3. Finite zero certificates and their normal-function consequence

In (945.6), take each convolution summand in its canonical representative in $\{0,\ldots,p-1\}$. The public second calculation gives the following integer sums before final reduction:

| $p$ | Coefficient | Sum of canonical finite summands | Reduced value |
|---:|---|---:|---:|
| 227 | $f_{18}$ | $2497=11\cdot227$ | 0 |
| 227 | $g_{18}$ | $1952=8\cdot227+136$ | 136 |
| 857 | $f_{71}$ | $34456=40\cdot857+176$ | 176 |
| 857 | $g_{70}$ | $26567=31\cdot857$ | 0 |

The complete summands are reproducible from the committed consumer and were emitted in the cited public job. They are not committed as regenerable arrays. The respective summand hashes are

```text
227 f18 c9d95c390814dcbdff11b060bd7ddef60c306debf6729a745792bbf9ab255c5b
227 g18 fa9a6f255352b5bb1c407fdf3e216b14964d06fa97030b0cfee970307dc950ad
857 f71 1d7de112803d5ab8560000044709831ce16bc60cc1e488303f6ded9884593d79
857 g70 dc31eb7301db0d6466b80d90a55178d2c3aec504c1be4f8d02b843520794368a
```

R925(925.11–12) identifies vanishing of every original $q_{h,j}$ with vanishing of the corresponding ordered sigma product. All remaining factors in that comparison, including $q_{h,J}$, $(3J)!$, the actual Cartier constant, and $f_*$, are units. At $j=1$, the two products in the table vanish. Hence $Q'_h(0)=0$ in both original central cases.

For $j=2$ the original $m_j=5$ gives
$$
\begin{array}{c|c|c}
(p,h)&\Sigma_2&\text{new exact factors}\\\hline
(227,115)&f_{17}g_{18}=101&f_{17}=176,\ g_{18}=136\\
(857,433)&f_{69}g_{71}=335&f_{69}=319,\ g_{71}=310.
\end{array}
\tag{945.8}
$$
Thus $q_{h,2}\ne0$, proving (945.3) and the exact order-two assertion. This uses the entire original squared coefficient comparison; it does not select unrelated square-root signs or set $a_h=0$.

For clarity, write $p^{-a_h}G_h(w)=wH_h(w)$ over the original complete unramified DVR $R_0$. Equation (945.3) implies
$$
H_h(0)\in pR_0,\qquad H'_h(0)\in R_0^\times.
\tag{945.9}
$$
Hensel's lemma therefore gives a unique root $w_*\in pR_0$ of $H_h$ in the central residue class. It can coincide with $0$ if the characteristic-zero linear coefficient vanishes. If that coefficient is nonzero, then $w_*\ne0$. This is a root of one original scalar coordinate after calibration; it is not a proof of simultaneous vanishing of all Abel coordinates, a rational point on the original modular curve, or a height relation. On the algebraically closed complete open unit disc, the smallest unit index of $p^{-a_h}G_h$ is two, so it has exactly two zeros counted with multiplicity, as in R924's original disc count. No assertion about rational zeros follows.

## 4. The two actual alternative labels

For $p=227$, the previously established third-label pair is $h=79,151$. The existing selected-third Legendre window already proves the $h=151$ factor nonzero; it is not recomputed. Formula (945.6) newly gives
$$
f_{24}=166,\qquad g_{12}=63,\qquad f_{24}g_{12}=16\ne0.
\tag{945.10}
$$
The original all-label critical-jet identity of R889/R898 therefore proves the same-label $J_{3,2}\ne0$. This does not borrow a sigma factor from the central $h=115$ label.

For $p=857$, R935's actual weight-34 label is $h=445$, and the first run had already proved
$$
p\nmid B_{34},\qquad f_{73}=465,\qquad g_{68}=146,\qquad
f_{73}g_{68}=187\ne0.
$$
The new arithmetic here is solely the missing Legendre factor. The original reflection identity gives $P_{444}=P_{412}$ modulo $857$. Since $412$ is even and $(1/s)^2=-1/3$, its direct finite binomial expression is
$$
P_{412}(1/s)=2^{-412}\sum_{j=0}^{206}(-1)^j
\binom{412}{j}\binom{824-2j}{412}
(-1/3)^{206-j}.
\tag{945.11}
$$
The canonical summands have integer sum $81980$, the prefactor is $404$ modulo $857$, and the value is $298$. Hence the actual same-label critical product is
$$
298\cdot187=21\pmod{857},
\tag{945.12}
$$
which is nonzero. R940 supplies the full original weight-34 normal-function comparison with its original source, norm, phase, and $a_h$; its hypotheses hold at this prime. Neither of these two finite alternatives proves that one of a fixed list of labels works for all sufficiently large primes.

## 5. What is ruled out, and what remains open

The complete supersingular values $S=95,568$ are directly reused from the earlier successful trace run, rather than recalculated by either sigma consumer. R936/R939 already prove their exact source, complete point weights, and descent to $\mathbf F_p$. Together with §3, they disprove the unqualified assertion
$$
S\ne0\ \Longrightarrow\ Q'_h(0)\ne0
\tag{945.13}
$$
for the two original central families over all their allowed primes. In particular no everywhere-unit identification of these two scalars can hold on that entire range.

This leaves several mathematically different possibilities open: a comparison with explicit exceptional factors, a statement only for sufficiently large primes, a different coefficient of the original $Q_h$, or an actual same-label choice that varies with $p$. The nonvanishing of the complete trace itself is also still open in general. The two computations neither produce nonsurjective representations at unbounded primes nor prove an absolute Serre constant. They close the false unrestricted scalar implication, and nothing in the source or height gaps is removed by changing the completion standard.

## 6. Reproducible public sources

All paths below are relative to `topics/serre-uniformity/`. Outputs were temporary files and stdout only, with no regenerable arrays in Git or Releases.

1. **Existing complete trace.** Run [`44716895805`](https://github.com/Rogerhu12/math-research-public/actions/runs/44716895805), job `136222480093`, source `7843407c2633ffd5f9041a137bd9fe7174021b65`; the original R939 window with `--minimum 109 --maximum 1000` gives $(p,T,S)=(227,6,95),(857,463,568)$. Output SHA256 `900524ddf9b53e831ec32e9a64a2bc9c394a22a738574877ce6b872d5209d2ab`. Its exact script and the complete receipt are preserved in [the earlier receipt](../notes/2026-11-20-R939-window-and-weight34-sigma-receipt.md).
2. **First, original-$z$ sigma consumer.** Run [`44719847377`](https://github.com/Rogerhu12/math-research-public/actions/runs/44719847377), job `136232493369`, source `1f394d300f92824f3bb1253af1f44ca7c1652501`; `scripts/original_middle_sigma_window.py --minimum 109 --maximum 1000 --output /tmp/original-middle-sigma-window.json`. Script SHA256 `a504e9c107228a209e3687cfcedaf288be10154b9594ab4fc1d6fc26487a77c5`; output 48,285 bytes, SHA256 `32f320938f5e5f43541e7c7e7c93967ad26faab63fab21d22fc4cc6d91a03023`.
3. **Second, algebraic-parameter sigma consumer and the new alternatives.** Run [`44720732478`](https://github.com/Rogerhu12/math-research-public/actions/runs/44720732478), job `136235472207`, source `2ca40e8720ff441fb29b700ca99e5582bb60b1a4`; `scripts/central_sigma_two_zeros_lagrange.py --output /tmp/central-sigma-two-zeros-lagrange.json`. Script SHA256 `95684611f724a866f04a735306336be89b845beaaf138aa32eaaf9ac79472941`; output SHA256 `217d9ff8f89c3270b8af2d0226fabb70662bff5874c526302933feaa66e08aad`. All four original central values agree, all finite identity checks pass, and the computation exits zero.
4. **Previously proved Legendre factors.** R934's run `44711592515` covers the central $p=857$ factor. R943 Appendix A's run `44718206366`, job `136226900472`, source `cfa323577937abf5f80652bacab6bd81971db2d6`, covers the central and selected-third factors at $227$; output SHA256 `f4e7416026c5cf358f6b473185cabf1d105998e8db2e79f2c457cecb7996400a`. Neither window is rerun here.

The second consumer reuses every complete trace, previous Legendre value, and the previous $857/h445$ sigma product. Its only duplicated mathematics is the four newly found central values, checked from the independent residue-change formula; the second coefficients, $227/h151$ sigma product, and $857/h445$ Legendre factor are new targets.
