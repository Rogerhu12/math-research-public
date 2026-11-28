# R149 ASQ11. The original positive $i$ divisor and its primitive fees

Use the actual real reflected bases of [WCS.7–12](R133-supplement-certified-Cayley-gap-on-the-reflected-waist-model.md). One positive index $n$ includes both signs and one real coordinate. Write $k=4n$ and $G_n=1/q_n$ for the original model inverse on $n\ge97$. The quantity after one primitive is $g_n=1/(4n|q_n|)$. WCS gives
$$
 |q_n|=\tfrac12|1-i\nu_i/k|\,|\lambda_n-i|,\qquad
 \lambda_n=e^{2\pi in\rho}(1+i\beta_*/(2n))/(1-i\beta_*/(2n)).
 \tag{ASQ11.1}
$$
The first factor in absolute values is at least one. Only the root $+i$ occurs for positive $n$. The negative-frequency part of the real line is its conjugate. The first 96 ordinary model coordinates stay independent.

For $97\le n\le1023$ the complete original [CYA group](R133-supplement-actual-finite-Cayley-scalar-gap-and-selected-inverse.md) has $n|\lambda_n-i|>.8729744$. All 927 members entered this saved bound with witness $190$. Hence this entire group has $g_n<.573$.

## The meaning of each saved candidate distance

Put $b=\beta_*/(2\pi)$, $N=4n$, $P=4p+1$ for an integer $p$. With
$$
 u=n(P/4-n\rho),\qquad
 n|n\rho+b/n-p-1/4|=|b-u|,                             \tag{ASQ11.2}
$$
the complete original [quadratic-norm run](R133-supplement-actual-first-phase-complete-quadratic-gap.md) computed a directed lower endpoint for $\inf_{b\in\mathcal J}|b-u|$ on the whole actual coefficient interval. The [original source](../scripts/fourfold_codazzi_first_symbol_quadratic_gap.py) forms the full interval for $b$, the ball for $u$ and the lower endpoint of their absolute difference. Its native field is **full_coefficient_distance_lower**. This number already contains the multiplier $n$ on the turn distance. If a printed lower endpoint carries a printed radius, its decimal midpoint minus that full radius is a valid exact rational lower.

For $97\le n<2^{34}$, the [quadratic covering theorem](R133-supplement-quadratic-norm-gap-after-first-scalar-phase.md) and that successful run give $|b-u|\ge1/16$ for every integer pair outside its 1502 saved candidates. All four residue counts are $375,372,382,373$ in their original order. Among the 372 with $P\equiv1\bmod4$, let $d_n$ be the minimum of $1/16$ and the saved lower endpoints over **all** such candidates with this $n$. Take $d_n=1/16$ when there are none. Then
$$
             n\|n\rho+b/n-1/4\|_{\mathbb R/\mathbb Z}\ge d_n.     \tag{ASQ11.3}
$$
This covers each noncandidate and every representative of the same circular turn, using the previously proved cover.

If $n\ge1024$ and $0\le d\le2/15$, the chord corresponding to a circular distance of at least $d/n$ is at least $2\sin(\pi d/n)$. Monotonicity on $[0,1/2]$ and $\sin x\ge x-x^3/6$, with $3.1415<\pi<22/7$, give
$$
          2n\sin(\pi d/n)\ge(157/25)d .
$$
Indeed $2\pi-(22/7)^3(2/15)^2/(3\cdot1024^2)>157/25$. The Cayley-to-exponential difference is at most $|\beta_*|^3/(12n^3)<19^3/(12n^3)$ by [CY.33](R133-supplement-exact-Cayley-principal-ratio-and-conditional-scalar-gap.md). Thus, for a positive denominator,
$$
       g_n\le F(n,d_n),\qquad
       F(n,d)=\{2[(157/25)d-19^3/(12n^2)]\}^{-1}.       \tag{ASQ11.4}
$$
The noncandidate bound $F(1024,1/16)<32/25$ also applies at every larger finite index. For candidates the original common finite lower $>.0007196$ alone implies positivity from $n=1024$ onwards. Their individual saved lower endpoints determine their improved bounds without repeating the old Cayley or candidate computation.

## The whole infinite tail

The original $Q(P,N)=aP^2+BPN+cN^2$ has
$$
 (a,B,c)=(10606109135510195,-5831714953207175,801634672549129).
$$
For $P=4p+1$, $N=4n$ one has $Q\equiv3\bmod4$. Modulo 5, $Q\equiv4N^2$, so $Q\bmod5\in\{0,1,4\}$. In $(99,111)$ the integers satisfying the first congruence are $103,107$; their residues $3,2\bmod5$ violate the second. The old complete interval gives $105<16\sqrt5\,b<106$ and $0<b<3$. Therefore
$$
             |Q(P,4n)-16\sqrt5\,b|>5.                    \tag{ASQ11.5}
$$
[Q.7](R133-supplement-quadratic-norm-gap-after-first-scalar-phase.md) gives the exact identity
$$
              Q(P,4n)=16\sqrt5\,u+16a u^2/n^2 .
$$
If $n\ge2^{34}$ and $|u-b|\le2/15$, then $|u|<16/5$ and $16a(16/5)^2/(2^{34})^2<1/64$ since $a<2^{54}$. The absolute difference in (ASQ11.5) is then at most $16(9/4)(2/15)+1/64<5$, a contradiction. Hence the whole tail has $d=2/15$ in the chord calculation and
$$
                       g_n\le F(2^{34},2/15)<3/5.        \tag{ASQ11.6}
$$
This uses the precise positive-$i$ residue and the complete original coefficient interval.

## Finite exceptions and stronger norms

Retain $1,\ldots,96$ and all $1024\le n<2^{34}$ with $F(n,d_n)>32/25$. Let $P_s$ project onto every other orthonormal model coordinate $n\ge97$. There are at most 372 exceptions before counting distinct candidate indices. Equations (ASQ11.1–6) give simultaneously
$$
 \|I\bar G P_s\|_{2\to2}\le32/25,\qquad
 \|I^2\bar G P_s\|_{2\to2}<.573/388,\qquad
 \|\bar G P_s\|_{2\to\dot H^{-4/3}}^3
 \le\max\{.573^3/388,(32/25)^3/4096,(3/5)^3/(4\cdot2^{34})\}.
 \tag{ASQ11.7}
$$
Here $\dot H^{-4/3}$ has weights $(4n)^{-4/3}$. The weights of the last two maps are $g_n/(4n)$ and $g_n/(4n)^{1/3}$. Taking the cube avoids rounding cube roots. The finite head and all true PDE, phase, height and mean columns are still retained.

The [public reader](../scripts/fourfold_codazzi_actual_positive_i_model_fees.py) consumes the original 198079-byte native from commit **d564ebaa49ae933cc1322f1b2f39e4bcacafd1e5**, SHA256 **db861442f5b895362abe090306c2899b3771282269b7ccc5743d820e79f8bff3**, together with its completed process and publication and the actual CYA result/execution. It groups the original saved distances, evaluates the new rational bounds, and lists all exceptions as well as the complete band and all-integer fees. Its noncandidate bound for each band starting at $n_0$ is $F(n_0,1/16)$; the lower original CYA group uses its own complete bound. These new combinations are evaluated in their first public job. This proof uses the unconditional 372 upper and does not assume the sharper actual count.
