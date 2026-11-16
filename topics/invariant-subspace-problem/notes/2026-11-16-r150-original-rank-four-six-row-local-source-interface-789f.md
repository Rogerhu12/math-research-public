# R150: original rank-four Bell charts and a six-row local-source consumer

Author: ChatGPT (AI), literature_audit.  
Date: 2026-11-16 UTC.  
Status: frozen source-preserving interface. The source is prepared for a bounded actual run; no local unit identity or characteristic-zero lift is assumed.

## 1. The exact geometric chart and the smaller positive-search module

Retain the original field $E$, all seventeen variables, the full original gradient ideal, and the global polynomial coordinates from the [matched Bell coordinate theorem](../results/R150-appendix-global-matched-bell-hyperbolic-coordinates-and-normalized-critical-ideal.md). Put
$$
B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad S=B[u_0,\ldots,u_4].
$$
The original eighteen generators are the seventeen transported gradients and $b-1$, where $b=y\cdot w$.

The [complete ten-generator presentation](../results/R150-appendix-complete-original-ten-generator-finite-critical-presentation.md) retains
$$
m=(1,u_0,\ldots,u_4,v_0,v_1,v_2,v_3),
$$
with the original four quadratic monomials $v$. The quadratic-generator part of the six original mean columns is $M(y)^{\mathsf T}$, for the same literal $6\times4$ mean matrix used in the [nineteen-chart Bell cover](../results/R150-appendix-original-mean-quadrics-dual-normalization-and-complete-bell-cover.md).

For each four-subset $R\subset\{0,\ldots,5\}$, let
$$
A_R=M[R,:]^{\mathsf T},\qquad\delta_R=\det A_R.
$$
The fifteen opens $\delta_R\ne0$ cover exactly the rank-four mean branch. They do not cover the rank-three branch. The four additional quadratic opens from the cited cover remain necessary on that branch.

If one applies the following Schur operation to the complete ten-by-fifty-seven presentation, it gives a complete six-by-fifty-three presentation over $S[\delta_R^{-1}]$. This follows from the same two-sided elimination as the [fifty-six seven-generator charts](../results/R150-appendix-complete-original-fifty-six-seven-generator-critical-charts.md), now eliminating all four quadratic generators using four original mean equations.

The present consumer deliberately uses the smaller, already source-certified fifty-column **parameter submodule**. Those columns are the literal original columns retained in the [116-to-50 compression](../results/R150-appendix-original-parameter-seeds-fifty-and-complete-field-module-equivalence.md): six mean, twenty weight-six commutator, fourteen weight-eight commutator, and ten Bell columns. Their equality with the 116 initial columns has been proved over the specified field place, not as an $E$-module equality. Neither this initial submodule nor its localization is claimed to be the full stable critical relation module.

Every one of these fifty columns has an exact original eighteen-generator source. Consequently an actual unit source obtained from any subset of their relations is sufficient for a positive local conclusion. Failure to obtain such a source is not a negative statement about the complete critical ideal.

## 2. Four original columns, all remaining rows, and the source formula

Order the four eliminated generator rows first, and use the selected four literal mean columns first. Write the fifty-column matrix as
$$
V=\begin{pmatrix}A&B_0\\C&D_0\end{pmatrix},
$$
where $A$ is four by four, $B_0$ is four by forty-six, $C$ is six by four, and $D_0$ is six by forty-six. The retained generator vector is
$$
m_K=(1,u_0,\ldots,u_4).
$$
Let $\mathcal G$ be the row of the original eighteen generators, and let $\Sigma_P,\Sigma_R$ be the corresponding original source matrices. The complete parent identities are
$$
m_EA+m_KC=\mathcal G\Sigma_P,\qquad
m_EB_0+m_KD_0=\mathcal G\Sigma_R.
$$
For $\delta=\det A$, the polynomial Schur matrix is
$$
P_\delta=\delta D_0-C\operatorname{adj}(A)B_0.
\tag{2.1}
$$
It satisfies the exact original-source identity
$$
m_KP_\delta
=\mathcal G\bigl(\delta\Sigma_R-\Sigma_P\operatorname{adj}(A)B_0\bigr).
\tag{2.2}
$$
No division is used in (2.1)--(2.2). The six retained rows, all forty-six remaining columns, the four selected source labels, and all eighteen original source coordinates are retained. The inverse chart map uses the same $A^{-1}=\operatorname{adj}(A)/\delta$; no mean coordinate is set equal to one and no second Bell scaling is introduced.

The consumer actually verifies the two adjugate products for each of the fifteen original matrices, all twenty-four entries of $M(y)$ against the actual mean columns, and all 460 coordinates in the original ten-row Schur reconstruction for the selected chart. It verifies each of the fifty original eighteen-generator identities and all seventeen source-Jacobian transports before forming the chart.

## 3. A localizer used only as a search device

At the legal field place $p=127,d=100$, adjoin one variable $\rho$ and form
$$
\mathcal P_\delta=
[P_\delta,(\rho\delta-1)I_6]
\in\mathbb F_{127}[y,w,\rho]^{6\times52}.
\tag{3.1}
$$
All twelve original parameters remain variables. The only specialization is the already verified coefficient-field place.

Singular's module `slimgb` is a candidate finder. If reduction of $e_0$ returns zero, the consumer separately requests a source by `lift(Original,Target,Units,"slimgb")`, requires $Units=I$, and verifies all six polynomial product coordinates independently with FLINT. A saved Gröbner candidate alone is not a positive result.

Suppose the verified source is
$$
P_\delta a+(\rho\delta-1)c=e_0.
$$
Let $N$ be the greatest $\rho$ exponent appearing in the first forty-six coefficients $a$. Substitute $\rho=\delta^{-1}$ and multiply by $\delta^N$:
$$
P_\delta\widetilde a=\delta^N e_0,\qquad
\widetilde a=\delta^N a(y,w,\delta^{-1})\in\mathbb F_{127}[y,w]^{46}.
\tag{3.2}
$$
The program does not accept the formal substitution without checking its six complete polynomial products.

Recover the coefficients of the original fifty columns by
$$
\gamma_R=\delta\widetilde a,\qquad
\gamma_P=-\operatorname{adj}(A)B_0\widetilde a.
\tag{3.3}
$$
All ten original module coordinates must then equal $\delta^N e_0$. The final positive gates are
$$
\delta^N=\sum_{i=1}^{18}\sigma_i\mathcal G_i,
$$
and the independent complete seventeen-physical-gradient plus Bell product after the paid Jacobian source transport. All of these are actual full polynomial multiplications. The final source is therefore a genuine original field identity with no localizer denominator left.

Such a result would close the selected field chart only. It does not prove a characteristic-zero identity. A later $E$ lift must reconstruct the same literal original coefficient model and verify the entire original polynomial identity. The program explicitly records `characteristicZeroLiftVerified=false`.

## 4. Selection, input pins, and continuation

The chart dictionary is the lexicographic list of the fifteen four-subsets of the six original mean indices. `--chart 0` through `--chart 14` fixes a literal chart. `--chart sparsest` selects among nonzero reductions by the lexicographic tuple
$$
(\text{number of minor monomials},
\text{total adjugate monomials},\text{original four-row tuple}).
$$
The entire fifteen-entry statistics table is retained in the temporary receipt. Selection is not evidence of completeness of one chart.

The new source is
`2026-11-16-r150-original-rank-four-six-row-local-source127-789f.py`,
blob `c56cc3ea13be44ef68f1032731a8188de57e9b00`, 33705 bytes, SHA256
~~~text
2e52674af37101cd9c6f12afbb9870fffe723f9ac01d7cb66d3663b9e1af851b
~~~
Its two complete imported source pins are:

| Helper | Bytes | SHA256 |
|---|---:|---|
| `2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py` | 23879 | 4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4 |
| `2026-11-16-r150-original-parameter-seed-compression127-789f.py` | 20434 | b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9 |

The original model binding is
~~~text
7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4
~~~
and its complete 30466-byte manifest SHA256 is
~~~text
9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2
~~~
The complete compression binding is
~~~text
baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca
~~~
Its canonical 620742-byte pure-mathematics identity has SHA256
~~~text
a1d73ea1ce5809c87bdc34724c1eb4407d6a5c0ae78fbf16aa3650563aa089dd
~~~
Every retained original column descriptor is matched with the corresponding parent descriptor. All compressed and decoded parent hashes remain mandatory. The published companion input manifest records the local paths and full base-model hashes.

The current parent byte protocol was produced with Python 3.12.14. A rebuild must preserve that pinned protocol and verify the same bytes; a platform gzip-header change is not silently normalized by this consumer.

Each completed child phase is immutable under its own source binding, with deterministic gzip and a full stored and logical hash. Singular candidates and source matrices are saved only after a complete return and an SSI read-back comparison. A timeout during a basis computation does not produce a reusable partial basis. Resuming after such a timeout must not be described as continuing an internal Gröbner state.

## 5. Bounded actual commands and result scope

Local preparation uses the actual same-source parent directories and a fresh child directory:
~~~sh
/tmp/r150-normal-789f-20261116-1040/venv/bin/python \
  /tmp/literature_bell_rank4_789f/2026-11-16-r150-original-rank-four-six-row-local-source127-789f.py \
  --model-source /tmp/r150-normal-789f-20261116-1040/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py \
  --model-out /tmp/r150-normal-789f-20261116-1040/original-ten-parameter-module127-v2 \
  --compression-source /tmp/r150-normal-789f-20261116-1040/2026-11-16-r150-original-parameter-seed-compression127-789f.py \
  --compression-out /tmp/r150-normal-789f-20261116-1040/original-parameter-seed-compression127 \
  --out /tmp/literature_bell_rank4_789f/sparsest-original-chart \
  --chart sparsest --through prepare --seconds 300 --memory-mib 2048
~~~
With an actually available Singular executable, the same mathematical binding may continue with `--through selftest` and then `--through final`; the initial complete candidate budget is at most 600 seconds and 4096 MiB. Time limits and execution paths do not change the mathematical input. The independently checked localizer selftest precedes the actual chart computation.

Preparation proves only the actual original chart formulas and input identities. A nonzero candidate remainder is diagnostic; it is not a complete negative membership test. A timeout or memory failure leaves the last verified whole phase and makes no local unit claim. A positive field result must pass every gate in Section 3, and still awaits its distinct characteristic-zero source proof.

All matrices, polynomial coefficients, SSI files, and mathematical receipts remain temporary or in completed execution logs. Only source, interfaces, execution parameters and hashes enter the repository. This local branch is separate from the ongoing full twelve-parameter fifty-column search and does not assert that all nineteen geometric charts have been closed.
