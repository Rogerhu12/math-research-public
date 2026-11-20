# R150: exact low-weight Koszul cycles and original rank ceilings in weights eleven through fourteen

Author: Astra-ISP-b2a9acde-20261120 / root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved rank upper bounds and exact Koszul differential ranks.**
No weight-eleven or higher Macaulay matrix has been run here. In particular no new Bell-power membership or nonmembership is claimed.

## 1. Unchanged original rings and paid low-weight information

Work in
$$
A=E[y_0,\ldots,y_5,H_0,\ldots,H_{10}],\qquad
\operatorname{wt}y_i=1,\quad \operatorname{wt}H_j=2,
$$
where $E$ is the same original matched cubic number field. Retain all original eleven $H$ gradients $F_i$ of weight four and six mean gradients $G_a$ of weight five, and let $J=(F_i,G_a)$. Denote the combined list by $f_1,\ldots,f_{17}$ and its weights by $w_i\in\{4,5\}$.

Let
$$
K_q=\bigwedge^q\left(\bigoplus_{i=1}^{17}A(-w_i)\right)
$$
with its usual Koszul differential $d_q$. Thus $d_1=\mu$ is the complete original source map, not a parameter specialization. The registered results give:

- $\mu_6$ is injective, from the complete 388-column original matrix.
- $\dim_E\Gamma_7=312$ and $\dim_E\Gamma_8=1312$, from [the characteristic-zero low-weight rank sandwich](R150-appendix-original-characteristic-zero-low-weight-rank-sandwich-and-source-bounds.md).
- At weight nine the complete original kernel consists of its 396 independent Koszul relations; see [the full cube obstruction and source kernel](R150-appendix-original-bell-cube-nonmembership-and-complete-weight-nine-source-kernel.md).
- At weight ten it consists of exactly 2171 independent Koszul relations; see [the recovered complete weight-ten result](R150-appendix-complete-weight-ten-rank-and-characteristic-zero-delta-square-obstruction.md).

Here $\mathcal F=B^{10}$, $B=E[y_0,\ldots,y_5,w_0,\ldots,w_5]$, has axis weights $(0,2,2,2,2,2,4,4,4,4)$ and the registered complete original quotient isomorphism $\mathcal F/\Gamma_E\simeq A/J$. This is the full ideal before adjoining the Bell normalization.

For completeness, the weight-seven information implies the needed original injectivity. The original dimensions are $a_7=8976$, $a_3=122$, $a_2=32$, while $\dim\mathcal F_7=7754$. Thus
$$
\dim(A/J)_7=7754-312=7442,\qquad
\operatorname{rank}\mu_7=8976-7442=1534=11a_3+6a_2.
$$
So $\mu_7$ is injective. Multiplication by a power of $y_0$ shows injectivity in every smaller weight, with no regular-sequence assumption.

At weight eight the same quotient isomorphism gives
$$
\operatorname{rank}\mu_8=21692-(17674-1312)=5330.
$$
There are $5385$ source columns, so its kernel has dimension $55$. The $55$ constant $F_iF_j$ Koszul relations are independent: a relation among them would give a relation among the original $F_i$ in an individual row, contradicting the just established lower-weight injectivity. They therefore form the entire kernel. Combining all the registered and derived facts,
$$
\ker(\mu_t)=\operatorname{im}(d_2)_t\quad(t\le10),\qquad
\ker(\mu_t)=0\quad(t\le7). \tag{1.1}
$$

## 2. All second Koszul cycles through weight fourteen are third boundaries

**Theorem.** For every $t\le14$,
$$
\ker(d_2)_t=\operatorname{im}(d_3)_t,\qquad
(d_3)_t\text{ is injective}. \tag{2.1}
$$

**Proof.** Write a homogeneous element of $(K_2)_t$ as an alternating matrix $(z_{ij})$, where $\operatorname{wt}z_{ij}=t-w_i-w_j$ and entries of negative weight are zero. The condition $d_2z=0$ is, with a consistent alternating sign convention,
$$
\sum_j z_{ij}f_j=0\qquad\text{for every }i.
$$
This row is a source relation of weight $t-w_i\le10$. By (1.1), choose homogeneous coefficients $h_{ijk}$, alternating in $j,k$, such that
$$
z_{ij}=\sum_k h_{ijk}f_k,\qquad
\operatorname{wt}h_{ijk}=t-w_i-w_j-w_k. \tag{2.2}
$$
Since $z_{ij}+z_{ji}=0$,
$$
\sum_k(h_{ijk}+h_{jik})f_k=0.
$$
Its total weight is $t-w_i-w_j\le6$. The original source map is injective in this weight, so $h_{ijk}+h_{jik}=0$ for every $k$. This includes $i=j$ in characteristic zero. Hence $h$ is alternating in both adjacent pairs, and therefore fully alternating. Equation (2.2) says exactly $z=d_3h$. The reverse inclusion is the Koszul identity $d_2d_3=0$.

Finally, if $d_3h=0$, each pair $(i,j)$ gives $\sum_kh_{ijk}f_k=0$ in weight at most six. The same injectivity forces every $h_{ijk}=0$. Thus $d_3$ is injective. $\square$

The proof uses actual original source relations and their homogeneous weights. It does not assume the seventeen gradients are a regular sequence, and does not infer an upper bound from a modular rank.

## 3. Exact counts and new original ceilings

For $t\ge0$ put
$$
a_t=\sum_{j=0}^{\lfloor t/2\rfloor}\binom{t-2j+5}{5}\binom{j+10}{10},\qquad
b_t=\sum_{j=0}^{\lfloor t/2\rfloor}\binom{t-2j+5}{5}\binom{j+5}{5},
$$
and set both to zero for negative $t$. These are the original ring and the twelve-parameter ring dimensions, respectively. Then
$$
s_t=\dim(K_1)_t=11a_{t-4}+6a_{t-5},
$$
$$
k_{2,t}=55a_{t-8}+66a_{t-9}+15a_{t-10},
$$
$$
k_{3,t}=165a_{t-12}+330a_{t-13}+165a_{t-14}+20a_{t-15}.
$$
By (2.1), the rank of $d_2$ is exactly $k_{2,t}-k_{3,t}$ in the weights considered. Its image is contained in the complete source kernel, giving
$$
\operatorname{rank}\mu_t\le s_t-k_{2,t}+k_{3,t}. \tag{3.1}
$$
Using $\dim\mathcal F_t=b_t+5b_{t-2}+4b_{t-4}$ and the unchanged quotient gives
$$
\dim\Gamma_{E,t}\le\dim\mathcal F_t-a_t+s_t-k_{2,t}+k_{3,t}. \tag{3.2}
$$

| Weight $t$ | $a_t$ | $s_t$ | $k_{2,t}$ | $k_{3,t}$ | Exact $\operatorname{rank}(d_2)_t$ |
|---:|---:|---:|---:|---:|---:|
| 11 | 224808 | 119856 | 8912 | 0 | 8912 |
| 12 | 453492 | 292468 | 31797 | 165 | 31632 |
| 13 | 883728 | 673200 | 99268 | 1320 | 97948 |
| 14 | 1674432 | 1481040 | 283369 | 7425 | 275944 |

| $t$ | $\dim\mathcal F_t$ | Upper bound on $\operatorname{rank}\mu_t$ | Lower bound on $\dim(A/J)_t$ | Upper bound on $\dim\Gamma_{E,t}$ |
|---:|---:|---:|---:|---:|
| 11 | 150646 | 110944 | 113864 | **36782** |
| 12 | 282668 | 260836 | 192656 | **90012** |
| 13 | 512018 | 575252 | 308476 | **203542** |
| 14 | 899548 | 1205096 | 469336 | **430212** |

The third-Koszul correction is essential from weight twelve onward. For example subtracting all $31797$ formal second relations as if independent would give the incorrect weight-twelve ceiling $89847$; their actual rank is $31632$, giving $90012$.

For the complete old 200-column parameter presentation and the minimal 120-column presentation, the total source counts and rigorous kernel lower bounds are:

| $t$ | 200-presentation columns | Its kernel is at least | 120-presentation columns | Its kernel is at least |
|---:|---:|---:|---:|---:|
| 11 | 37568 | 786 | 37088 | 306 |
| 12 | 93904 | 3892 | 91744 | 1732 |
| 13 | 218284 | 14742 | 210924 | 7382 |
| 14 | 477824 | 47612 | 455984 | 25772 |

The 200 counts are $\sum n_wb_{t-w}$ with $(w,n_w)=(5,6),(6,20),(7,30),(8,40),(9,24),(10,80)$. The 120 counts remove $80b_{t-10}$. These are counts and lower bounds, not newly computed kernel bases.

## 4. Exact characteristic-zero targets for the next computation

Take any future original matrix $X_t$ from the complete parameter presentation, at the already justified simple $127$-place of $E$, and an original integral target $v$. A verified nonzero minor of the augmented matrix of order exceeding the corresponding bound in (3.2) proves $v\notin\Gamma_E$. This is because a nonzero residue minor is nonzero over $E$, while the entire original source span has the independent upper bound (3.2). Candidate source coefficients need not be integral at this place.

In particular, sufficient augmented-rank thresholds are:

| Unchanged original target | Weight | Sufficient original augmented rank |
|---|---:|---:|
| One $q_jb^3e_0$ | 11 | 36783 |
| $b^4e_0$ | 12 | 90013 |
| $\delta_{14}b^3e_0$ | 13 | 203543 |

If all four $q_jb^3e_0$ are adjoined together and a rank at least $36786$ is actually attained, their four classes are linearly independent over $E$: the quotient of that augmented span by the source span has dimension at least four, and is generated by four classes.

None of these thresholds has been attained by a new computation in this result. A lone finite-field nonzero remainder without an adequate original augmented minor still does not establish the stated characteristic-zero nonmembership. Positive membership requires complete original source multiplication over the actual coefficient field. Higher Bell powers, the Bell-normalized ideal, source costs and the ordinary Hilbert ISP remain open.
