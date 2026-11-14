# R133 supplement — cached complete scalar derivatives and the compact parameter column

## 1. Completed same-object input and result

The complete 169-germ cache from
`R133-supplement-actual-complete-169-germ-phase-scalar-cover.md` can be
consumed for derivative estimates without recomputing its intrinsic
primitive or angular exponential. This does **not** mean that a uniform
value error can be differentiated. The stored normalized point jets and
the complete whole-cell seventh derivative provide the additional
information used below.

The new consumer has actually processed all 626 accepted cells. It
reconstructs complete derivative-model errors through order three for
all five scalars $\beta,K,s,\gamma,q$. The actual affine parameter remains
$\eta=\eta_0$, with offset $\delta\eta=0$, and the compact parameter is
the exact fixed value of the preceding cache. No whole-$\eta$ enlargement
is inferred.

On the entire true compact support

$$ I_w=[1/20,9/50],                                        \tag{J.1} $$

the same calculation also constructs 220 exact degree-seven models for

$$
 T=\frac{\beta}{2(a\gamma)^2}=\frac{\beta}{2E_\nu},          \tag{J.2}
$$

with all true coefficient errors included. Their integrated complete
value error is

$$
 \sum_{J\subset I_w}|J|\epsilon_{T,J}
 <1.159582\,10^{-17}.                                      \tag{J.3}
$$

Only the original finite scalar polynomial $a$ is additionally read.
There is no reevaluation of the intrinsic angular primitive, no angular
FFT, and no new approximation to $\gamma$ or $\beta$ independent of the
existing cache. All six complete consumption gates passed in the actual
71.93-second run.

These are coefficient and derivative contracts. They do not assert a
true parameter response, true conjugacy, or a body/parameter inverse.

## 2. Differentiating the proved Taylor identity

Let a saved cell be $[a,b]$ with centre $c=(a+b)/2$. For a true scalar
$f$ the native stores enclosures

$$
 p_k\ni\frac{f^{(k)}(c)}{k!}\quad(0\le k\le6),\qquad
 B_7\supset f^{(7)}([a,b]),
$$

and exact dyadic coefficients $c_0,\ldots,c_7$ of

$$ P(r)=\sum_{k=0}^7c_k(r-c)^k.                            \tag{J.4} $$

For any closed subinterval $J=[l,r]\subset[a,b]$, put

$$ h_J=\max(|l-c|,|r-c|). $$

For each $0\le j\le7$, Taylor's integral formula applied to $f^{(j)}$
gives the complete bound

$$
\boxed{\begin{split}
 \|f^{(j)}-P^{(j)}\|_{C(J)}
 &\le\sum_{k=j}^{6}\frac{k!}{(k-j)!}
          |p_k-c_k|\,h_J^{k-j}\\
 &\quad+\frac{h_J^{7-j}}{(7-j)!}
          \sup|B_7-7!c_7|=:\epsilon_{f,j,J}.
\end{split}}                                               \tag{J.5}
$$

For $j=7$ the sum is empty and the last term is exactly the complete
seventh-derivative discrepancy. Formula (J.5) also applies to a point
subinterval. If the original centre is outside the restricted cell, the
distance $h_J$ is still measured to that original centre; no unjustified
recentering is performed.

To prove (J.5), expand $f^{(j)}$ at $c$ through derivative six. The
remainder is $(r-c)^{7-j}/(7-j)!$ times a weighted average of true
seventh derivatives between $c$ and $r$. That average belongs to $B_7$.
Subtract the exact differentiated polynomial (J.4), take absolute values,
and bound each distance by $h_J$. This also handles negative $r-c$,
since its sign is factored outside the weighted average. Every original
point-jet uncertainty and whole-derivative tail is retained.

In particular the routine `restrict_model(row,name,l,r,j)` returns:

- the exact rational coefficients of $P^{(j)}$, still centred at $c$;
- the outward bound (J.5);
- an interval enclosing the complete true derivative on $J$.

These are ordinary derivatives. `normalized_true_jets` divides the
$j$th result by $j!$ only when forming a formal derivative series.

The larger derivative errors near the root are retained. In particular
the $q$ derivative errors are not uniformly small near the final root
stop. A consumer must use the actual derivative order and its real
radial weights; it may not replace them by the much smaller value error.

## 3. Reusing the cache to form the complete parameter coefficient

The intrinsic identity $E_\nu=(a\gamma)^2$ is exact for the installed
target. On each cell in (J.1), the original finite scalar-germ polynomial
provides the normalized derivatives of $a$ at the centre and on the
whole cell. This is the same finite polynomial read by the complete
high-seven provider before its angular exponential step.

At the centre, use the original saved normalized point jets of
$\beta,\gamma$ through order six. On the whole cell use the complete
normalized jets supplied by (J.5) through order seven. Formal truncated
series division applied to

$$ T=\beta/(2a^2\gamma^2)                                  \tag{J.6} $$

then gives point jets of $T$ through order six and a whole enclosure of
$T^{(7)}$. The full positive lower bounds for $a$ and $\gamma$ are checked
before division, and the actual series precisions are checked after it.
Independent interval boxing of the different jets is conservative: it
contains the simultaneously realized true jets at every point.

Choose dyadic centres for the point coefficients of orders zero through
six and for the whole normalized coefficient of order seven. Apply the
same complete Taylor remainder formula to obtain a model $T_7$ and
$\epsilon_T$. The resulting native stores these original point jets,
whole seventh derivative, exact coefficients and error for every one of
the 220 compact-support cells. Thus these new models can themselves be
restricted and differentiated by (J.5), with no extra target evaluation.

The actual compact support is covered exactly once from $1/20$ to
$9/50$. The outer cells, where the compact bump and its first derivative
vanish identically, need no $T$ model for the direct parameter column.

## 4. The actual derivative of the target parameter

Write

$$
 w(r)=4096t^6(1-t)^6,\qquad
 t=\frac{r-1/20}{9/50-1/20}
$$

on (J.1), extended by zero. The target identity gives, at the exact
fixed compact parameter,

$$
 \partial_\nu\gamma=\frac{w\gamma}{2},\qquad
 \partial_\nu K=-wK+Tw'.                                  \tag{J.7}
$$

The plus sign in the first formula is retained. In particular (J.2)
supplies the complete direct metric term in the previously proved
principal variation. It is not an additional reference-$s_\nu$ state
column: the full state variation remains whatever explicitly defined
physical moving direction is being consumed.

For later real parameter intervals the exact identities, before any
Taylor approximation in the parameter, are

$$
 \gamma_{\nu+\delta}=\gamma_\nu e^{\delta w/2},\qquad
 K_{\nu+\delta}=(K_\nu+\delta T_\nu w')e^{-\delta w}.
                                                               \tag{J.8}
$$

Their second derivatives are consequently

$$
 \partial_\nu^2\gamma=\frac{w^2\gamma}{4},\qquad
 \partial_\nu^2K=w^2K-2wTw'.                              \tag{J.9}
$$

Equations (J.7)–(J.9) do not assert that a chosen finite state direction
is a true nonlinear response. They provide its actual target forcing
when the same fixed metric parameter is varied in a centre construction.
The final isometric flex family must use one final fixed value of that
metric parameter.

## 5. Actual derivative budgets and implementation

As examples of the complete reconsumed derivative errors, the integrated
bounds through the first three derivatives are

| Scalar | First derivative error | Second derivative error | Third derivative error |
|---|---:|---:|---:|
| $\beta$ | $1.595962\,10^{-17}$ | $2.138169\,10^{-13}$ | $2.844071\,10^{-9}$ |
| $K$ | $1.192678\,10^{-11}$ | $1.409721\,10^{-7}$ | $0.001536228$ |
| $s$ | $6.590958\,10^{-12}$ | $7.984600\,10^{-8}$ | $0.000884367$ |
| $\gamma$ | $2.869690\,10^{-12}$ | $3.375782\,10^{-8}$ | $0.000362548$ |

The omitted displayed $q$ derivative numbers are present in full in the
native; they are large near the root and are not omitted from any
computation. They are not needed in the direct compact parameter column
outside its strict support, where $w=w'=0$.

Files:

- `scripts/fourfold_codazzi_phase_scalar_cache_jets.py`
- `notes/2026-11-14-R133-complete-scalar-derivative-and-compact-T-cache-native.json.gz`

The native SHA of the complete input cover is
`94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3`.
The consumer checks it, every original scalar-germ SHA, the exact
complete provider SHA, and the same original target SHA. Its output
stores all 220 new $T$ models and the complete derivative-error tables.

Reproduction from the topic directory:

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python -u \
  scripts/fourfold_codazzi_phase_scalar_cache_jets.py --compact-T \
  --out /path/to/new-scalar-derivative-and-T-native.json.gz
```

The original mathematical cache, active transport source, and ongoing
transport checkpoints are unchanged. The whole positive cap, an affine
parameter neighbourhood, a true response error, and the complete
PDE/phase Schur complement remain separate obligations.
