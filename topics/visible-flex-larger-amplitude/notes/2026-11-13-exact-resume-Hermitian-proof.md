# Same-leaf Hermitian comparison for the physical middle source

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

Status: the comparison theorem below is proved. The associated actual numerical run has a separate result/resource packet; neither this theorem nor two represented modes closes the full outer problem.

## Exact comparison

In the real sine/cosine coordinates of R104, on one true source leaf let
$$
z=(P,K/b)^T,\qquad
z_x=A_bz+(0,f/b)^T,
$$
where $b>0$ is an exact constant on that leaf and
$$
A_b=\begin{pmatrix}-s-\ell&-msb\\-m\ell/b&-2\ell\end{pmatrix},
\quad s=r_x/r>0,\quad \ell=w_x/w.
$$
For complex coefficients use the same matrix over $\mathbb C$; its Euclidean norm has the same Hermitian energy estimate. The maximum eigenvalue of the real symmetric part is exactly
$$
\lambda_b(x)=-\frac{s+3\ell}{2}
 +\sqrt{\left(\frac{\ell-s}{2}\right)^2
       +\left(\frac m2(sb+\ell/b)\right)^2}.
$$
The upper right derivative of $q=|z|_2$ obeys
$$
D^+q\le\lambda_b q+|f|/b.
$$
For $q>0$ this follows by differentiating $q^2$ and using the Hermitian Rayleigh quotient. At a zero, the upper right derivative of the norm is at most the forcing norm; alternatively apply the same estimate to $(|z|^2+\varepsilon^2)^{1/2}$ and pass to $\varepsilon\downarrow0$.

The previously prepared scalar estimate used
$$
\alpha_b=\max(-s-\ell,-2\ell)+\frac m2|sb+\ell/b|.
$$
Because $\sqrt{a^2+c^2}\le |a|+|c|$,
$\lambda_b\le\alpha_b$ pointwise. With interval input boxes one takes the minimum of the independently valid outward upper endpoints, so the new certified bound is never worse merely because one interval evaluation loses correlation.

An Arb ball representing a square can have a tiny negative lower endpoint. For the radicand $D=a^2+c^2\ge0$, the implementation therefore uses $\sqrt{\sup D}$ as an upper bound; it does not take a square root of a ball crossing zero. This is a strictly valid outward bound and changes no source, phase, frame or numerical tolerance.

## Full leaf and frame interfaces

Let $\Lambda$ be a fixed upper bound for $\lambda_b$ on a leaf of actual width $\Delta$, and let $d$ bound $|f|/b$ there. The comparison solution with incoming bound $q_0$ has endpoint
$$
q_1=e^{\Lambda\Delta}q_0+d\Delta\psi(\Lambda\Delta),\qquad
\psi(z)=\int_0^1e^{tz}\,dt.
$$
This formula also applies to $\Lambda=0$ and negative $\Lambda$. Its derivative has fixed sign on the leaf, since it equals $e^{\Lambda t}(\Lambda q_0+d)$. Thus its whole-leaf maximum is $\max(q_0,q_1)$.

At an exact frame change from $b_-$ to $b_+$, physical $(P,K)$ is unchanged and
$$
q_+\le\max(1,b_-/b_+)q_-.
$$
The propagated norm gives separate component estimates $|P|\le q$, $|K|\le bq$. The two radial suprema are taken separately before summation, and the original output weight $1+m$ is included once. No target $V$ divisor is introduced.

For the source-only diagonal contribution, $q_0=0$ at its original source-segment boundary. The existing three candidates (R68 leaf frames, one segment constant, and one phase constant) remain in the computation. Each receives a second independently evaluated candidate using $\lambda_b$. All $10793$ original leaves, $18$ original source segments, modes $94,96$, materials $c_{\rm bg}V^p$ for $p=2,1,0$, exact positive frames and every interface cost remain present.

A componentwise minimum of valid estimates is valid. The new diagonal estimates may replace only the corresponding original R104 diagonal rows. All off-diagonal source positions and both genuine initial columns remain in the complete nonlinear budget.

## Scope

This theorem supplies actual linear source comparisons when the indicated input packet and arithmetic are consumed successfully. It does not discard the complete mean, the inverse denominator, the source strip conversion, or unknown-mode coupling. It cannot establish the full low/middle/high solution, the 46 cut equations, the missing outer cells, a closed surface, or reach by itself.
