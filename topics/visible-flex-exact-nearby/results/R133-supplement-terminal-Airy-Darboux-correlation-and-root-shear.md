# R133 supplement: terminal-Airy Darboux correlation and the complete first-column root shear

2026-11-15, visible-exact / newton_source.

**A new analytic consequence of completed reference and potential bounds.** The actual terminal-Ai column and its first Darboux approximation have a correlated root shear of order $n^{-8/3}$. The formula includes the exact terminal mismatch; it does not replace the nonzero genuine shear by zero. A common, invertible input multiplier changes only the first decaying column and preserves the first symbol. The second reference column, both physical means, positive boundary rows and finite equations remain.

This text performs no new numerical run and calls no successful producer. The new result is the signed Wronskian identity, its complete analytic bound, and its ordered use in the first-column comparison. A full physical strong-remainder or incoming-inverse estimate still has its other terms.

## 1. Exact objects and already completed domains

Use the same original root piece, fixed intrinsic parameter and full complex parameter boxes of [the actual common potential](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md). For physical Fourier labels,
$$
 n=4|j|\ge388,\qquad z=j^{-2},\qquad
 \lambda=n^{2/3},\qquad L=\frac1{2000}.
 \tag{AD.1}
$$
Both signs of $j$ remain. The analytic value $z=0$ is not the independent physical mean.

The completed largest potential case gives the common complex coordinate image
$$
 D(0,R_*),\qquad R_*>0.000742956050168040>L,
$$
and, throughout this image and the original parameter boxes,
$$
 |V|<276,\qquad |V_T|<26431,\qquad |V_{TT}|<3830956.
 \tag{AD.2}
$$
These are the actual canonical $T$ derivatives: the original potential producer first formed the complete $r$ expressions and divided by the same nonzero coordinate derivative. They are not derivatives inferred from the modulus of $V$.

The exact original actual proof is Git blob
b4dc5f5f21394c5163dacd40edc22d6cdb82b333, SHA256
6b6db11ba57bb1273bc84d352fc2318cc69bb982a5a4803e662903932a41cbf1.
Its run 43685624307/1 passed sixteen gates. Its saved execution is
notes/common_radial_potential_budget_ci/run-43685624307-1/execution.json,
27645 bytes, SHA256
d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9.
No part of that computation is repeated.

Write $A(t)=\operatorname{Ai}(t)$ and $B(t)=\operatorname{Bi}(t)$, and
$$
 A_n(T)=A(\lambda T),\quad B_n(T)=B(\lambda T),\quad
 F_n(T)=
 \begin{pmatrix}
 A_n(T)&B_n(T)\\
 A_n'(T)&B_n'(T)
 \end{pmatrix},\qquad \det F_n=\frac{\lambda}{\pi}.
 \tag{AD.3}
$$
Primes on $A,B$ mean argument derivatives; primes on $A_n,B_n,V,\mathcal B$ mean canonical $T$ derivatives.

Use exactly the [genuine reference columns A.11--A.21](R133-supplement-genuine-common-radial-reference-columns-and-two-source-ports.md). In particular,
$$
 (\partial_T^2-n^2T+V)f_n=0,\qquad
 (f_n,f_n')(L)=(A_n,A_n')(L),
$$
$$
 (f_n,f_n')(0)=F_n(0)(a_n,b_n)^t,\qquad
 \widehat f_n=f_n/a_n,\qquad \beta_n=b_n/a_n.
 \tag{AD.4}
$$
The second genuine column $g_n$ has root state $F_n(0)e_2$. Thus
$$
 \Psi_n=(\widehat f_n,g_n),\qquad
 \Psi_n(0)=F_n(0)
 \begin{pmatrix}1&0\\\beta_n&1\end{pmatrix}.
 \tag{AD.5}
$$
Here and below a solution used as a matrix column denotes its complete two-state column.

The proved A estimates, for real $0\le T\le L$ even with complex potential parameters, are
$$
 |f_n(T)|\le e^{\tau_n}A_n(T),\quad
 \tau_n=\frac{8\cdot276\,L}{\lambda}<\frac1{40},\quad
 e^{\tau_n}<\frac{40}{39},\quad |a_n|>\frac{77}{78}.
 \tag{AD.6}
$$
Also $A(0),B(0),B'(0)<1$, $|A'(0)|<1/3$, and
$$
 A(t)>0,\quad A'(t)<0,\quad
 \frac14<-\frac{A'(t)}{A(t)}<\sqrt{1+t},\quad
 A'(t)^2-tA(t)^2=\int_t^\infty A(s)^2\,ds.
 \tag{AD.7}
$$
The original A proof is blob
62909c54de321da071a6bbc6e169e87b5888dde6, SHA256
0e56cf640b5c5f46c917699396e0ef6e5cce1fd5276cbddfc56ee1ed58d89c49.
All estimates below inherit its real-$T$ qualification. Holomorphic existence does not turn these into bounds on an arbitrary complex old-angle image.

## 2. The regular Darboux coefficient and a nonzero first root coordinate

Let $\mathcal B$ be the exact regular solution already used in IN:
$$
 \mathcal B+2T\mathcal B'=V,\qquad
 \mathcal B^{(p)}(T)
 =\frac12\int_0^1s^{p-1/2}V^{(p)}(sT)\,ds.
 \tag{AD.8}
$$
Every segment $sT$ lies in the same completed disk. Consequently (AD.2), with no new potential evaluation, gives throughout $[-L,L]$
$$
 |\mathcal B|<276,\qquad |\mathcal B'|<9000,\qquad
 |\mathcal B''|<800000,\qquad
 |H|<H_*:=2^{20},\quad H=\mathcal B''+V\mathcal B.
 \tag{AD.9}
$$
For the last inequality use $800000+276^2=876176<2^{20}$. The divisions by $3$ and $5$ in the first two derivative bounds are the exact integrals in (AD.8); no derivative of an upper-bound function is taken.

Define
$$
 Y_{d,n}=A_n-\frac{\mathcal B}{n^2}A_n',\qquad
 F_n(0)^{-1}(Y_{d,n},Y_{d,n}')(0)=(a_{d,n},b_{d,n})^t.
 \tag{AD.10}
$$
The complete Darboux residual is
$$
 (\partial_T^2-n^2T+V)Y_{d,n}
       =-\frac{H}{n^2}A_n'.
 \tag{AD.11}
$$
This is the exact IN.6 identity, including its derivative term.

Put $A_0=A(0)$, $A_0'=A'(0)$, and similarly for $B$. Taking the exact inverse of $F_n(0)$ yields
$$
 \begin{split}
 a_{d,n}
 &=1-\pi\mathcal B(0)B_0'A_0'n^{-4/3}
       +\pi\mathcal B'(0)B_0A_0'n^{-2},\\
 b_{d,n}
 &=\pi\mathcal B(0)(A_0')^2n^{-4/3}
       -\pi\mathcal B'(0)A_0A_0'n^{-2}.
 \end{split}\tag{AD.12}
$$
In particular, using $n^{2/3}>52$ for $n\ge388$,
$$
 \begin{split}
 |a_{d,n}-1|
 &<\frac43\{276n^{-4/3}+9000n^{-2}\}\\
 &<\frac43\left(\frac19+\frac1{16}\right)
   =\frac{25}{108}<\frac14.
 \end{split}\tag{AD.13}
$$
Indeed $9\cdot276<52^2$ and $16\cdot9000<388^2$.
Thus
$$
 |a_{d,n}|>\frac34,\qquad |a_{d,n}|<\frac54,\qquad
 |a_{d,n}^{-1}|<\frac43,\qquad
 \beta_{d,n}:=b_{d,n}/a_{d,n}
 \tag{AD.14}
$$
are all well-defined on the original $|j|\ge97$ domain. There is no new smaller-frequency extrapolation or determinant inversion of the full Darboux matrix.

## 3. Exact correlation of the two root shears

Form the signed Wronskian
$$
 \mathcal W_n(T)=f_n(T)Y_{d,n}'(T)-f_n'(T)Y_{d,n}(T).
$$
Equations (AD.4) and (AD.11) give
$$
 \mathcal W_n'(T)
       =-\frac{H(T)}{n^2}f_n(T)A_n'(T),
$$
whereas the root states give
$$
 \mathcal W_n(0)
 =\frac{\lambda}{\pi}
      \{a_nb_{d,n}-b_na_{d,n}\}
 =\frac{\lambda}{\pi}a_na_{d,n}
      (\beta_{d,n}-\beta_n).
 \tag{AD.15}
$$
At the actual terminal point, the exact equality $f_n=A_n$, $f_n'=A_n'$ gives
$$
 \mathcal W_n(L)
 =\frac{\mathcal B(L)}{n^2}
       \{A_n'(L)^2-n^2L A_n(L)^2\}
   -\frac{\mathcal B'(L)}{n^2}A_n(L)A_n'(L).
 \tag{AD.16}
$$
The complete signed identity is therefore
$$
 \boxed{
 \beta_{d,n}-\beta_n
  =\frac{\pi}{\lambda a_na_{d,n}}
       \left[
        \mathcal W_n(L)
        +\frac1{n^2}\int_0^L H(T)f_n(T)A_n'(T)\,dT
       \right].
 }\tag{AD.17}
$$
No independent upper bounds for $\beta_n$ and $\beta_{d,n}$ have been subtracted. Their common order-$n^{-4/3}$ contribution cancels inside this exact identity. The terminal term remains even when it is exponentially small.

The integral has the additional full factor $\lambda^{-1}$ after root normalization:
$$
 \begin{split}
 \int_0^L |f_n(T)A_n'(T)|\,dT
 &\le e^{\tau_n}\int_0^{\lambda L} A(t)|A'(t)|\,dt\\
 &\le e^{\tau_n}\frac{A_0^2}{2}.
 \end{split}\tag{AD.18}
$$
The last inequality is the integral of $-(A^2)'/2$, not an asymptotic truncation. Its contribution to (AD.17) is at most
$$
 \frac{\pi A_0^2}{|a_na_{d,n}|}
       \frac{e^{\tau_n}H_*}{2}n^{-8/3}.
 \tag{AD.19}
$$

## 4. The terminal terms and a uniform complete order

Let $t_n=\lambda L$ and $e_n=\exp[-(4/3)t_n^{3/2}]$.
Equation (AD.7) implies
$$
 A(t)\le A_0e^{-2t^{3/2}/3},\qquad
 \int_t^\infty A(s)^2\,ds<2A(t)^2,\qquad
 |A(t)A'(t)|\le A_0^2\sqrt{1+t}\,e^{-4t^{3/2}/3}.
 \tag{AD.20}
$$
For the first estimate use $-A'/A\ge\sqrt t$, a consequence of the positive Airy energy. For the second, use $-A'/A>1/4$ and monotonicity of that logarithmic derivative.

Writing $B_*=276$ and $B_{1,*}=9000$, (AD.16)--(AD.20) prove the complete bound
$$
 \begin{split}
 |\beta_{d,n}-\beta_n|
 \le\frac{\pi A_0^2}{|a_na_{d,n}|}
 \bigg[
 &\frac{e^{\tau_n}H_*}{2}n^{-8/3}
 +2B_*n^{-4/3}e_n\\
 &+B_{1,*}n^{-2}\sqrt{1+t_n}\,e_n
 \bigg].
 \end{split}\tag{AD.21}
$$
This retains the two distinct terminal terms and the full potential residual.

A useful explicit all-frequency consequence is
$$
 |\beta_{d,n}-\beta_n|
 \le C_{\rm Ai}\,n^{-8/3},\qquad
 C_{\rm Ai}
 =\frac{416}{77}
     \left\{\frac{20H_*}{39}
                  +\frac{2B_*}{L^2}
                  +\frac{2B_{1,*}}L\right\}
 <2^{34}.
 \tag{AD.22}
$$
Here $|a_na_{d,n}|^{-1}<104/77$, $\pi<4$, $A_0^2<1$, and $e^{\tau_n}<40/39$.
For the two terminal terms use
$$
 t^2e^{-4t^{3/2}/3}\le1,\qquad
 t\sqrt{1+t}\,e^{-4t^{3/2}/3}\le2
 \quad(t\ge0).
$$
For example $t\sqrt{1+t}\le t+t^{3/2}$, and each of these two powers times the exponential has maximum below one. These are exact real-variable inequalities. The last coarse rational rounding in (AD.22) is an analytic consequence of the displayed integers, not a newly reported public scalar result.

For a declared root-input threshold $N=4K\ge388$ one may retain the sharper expression
$$
 \mathcal C(N)=\frac{416}{77}
 \left[
  \frac{20H_*}{39}
  +2B_*N^{4/3}e^{-(4/3)NL^{3/2}}
  +B_{1,*}N^{2/3}\sqrt{1+N^{2/3}L}\,
                 e^{-(4/3)NL^{3/2}}
 \right].
 \tag{AD.23}
$$
If $N^2L^3\ge1$, both terminal functions inside the square brackets decrease for all $n\ge N$. In the variable $t=n^{2/3}L\ge1$, their logarithmic derivatives are respectively $2/t-2\sqrt t$ and $1/t+1/[2(1+t)]-2\sqrt t$. Thus
$|\beta_{d,n}-\beta_n|\le\mathcal C(N)n^{-8/3}$ throughout that root-input tail. This is a new optional scalar evaluation, separate from all old reference calculations.

## 5. The complete first-column state identity

Define
$$
 \Delta_n=a_{d,n}\widehat f_n-Y_{d,n},\qquad
 d_n=a_{d,n}\beta_n-b_{d,n}
       =a_{d,n}(\beta_n-\beta_{d,n}).
$$
Its exact root state is
$$
 (\Delta_n,\Delta_n')(0)=F_n(0)(0,d_n)^t
                         =\Psi_n(0)(0,d_n)^t .
 \tag{AD.24}
$$
There is no mixing by an estimated inverse root matrix in this particular first column: the second column of $C_n$ is exactly $e_2$.

For every $T$ in the same reference interval, with oriented integration,
$$
 \boxed{
 \binom{\Delta_n}{\Delta_n'}(T)
  =d_n\binom{g_n}{g_n'}(T)
   +\frac1{n^2}\int_0^T
       \Psi_n(T)\Psi_n(s)^{-1}e_2\,H(s)A_n'(s)\,ds .
 }\tag{AD.25}
$$
The positive forcing sign follows because $Y_{d,n}$ has the negative residual (AD.11). On $T<0$ the integral still runs from $0$ to $T$; its orientation is not changed by the positive-axis estimate used to bound $d_n$.

The first term has
$$
 |d_n|\le\frac54 C_{\rm Ai}n^{-8/3}.
 \tag{AD.26}
$$
The second term is the same complete Darboux inhomogeneous comparison, now for the exact free Ai column. Both state rows are present. The independent ordinary source slots and the extra physical reconstruction terms of IN.23--IN.27 remain; they are not removed by recognizing the scalar equation in (AD.25).

The homogeneous term involves the genuine $g_n$ column. Its physical output is not bounded by replacing its growing-column receiver with the decaying-column receiver. Any subsequent norm must retain the correctly typed column and its actual ordered Liouville/Piola, primitive, mean and phase changes.

## 6. Root-input strong multiplier and a common reparametrization

On the original scalar root-input Fourier labels $|j|\ge97$, let $D_d$ be the multiplier $d_n$ for both signs. Extend this high-input comparison multiplier by zero on $|j|<97$; the actual finite comparison and the independent physical mean remain separate equations. If $P_K^{\rm root}$ is the original root-input Fourier projection $|j|\ge K\ge97$, then with $\Lambda_j=(1+16j^2)^{1/2}$,
$$
 \begin{split}
 \|D_dP_K^{\rm root}:H^{-4/3}\to L^2\|
 &=\sup_{|j|\ge K}\Lambda_j^{4/3}|d_{4|j|}|\\
 &\le \frac54\left(\frac{17}{16}\right)^{2/3}
       C_{\rm Ai}(4K)^{-4/3}.
 \end{split}\tag{AD.27}
$$
Under the extra condition in (AD.23), replace $C_{\rm Ai}$ by $\mathcal C(4K)$.
This is a diagonal-input estimate. It does not assume an unproved Hilbert--Schmidt bound for the old order-$n^{-4/3}$ full matrix.

The threshold in (AD.27) belongs to the original input reference label. It is not the TN moving-output cutoff, the transported projection of TC, or a new phase Fourier cutoff. Changing any of these coordinates requires its full conjugation and finite blocks. The finite root labels $97\le|j|<K$, all low labels and the physical mean remain explicit.

Let $A_d$ be the input multiplier $a_{d,n}$ on the first terminal-Ai column for $|j|\ge97$. On $|j|<97$, including the physical mean, and on every other independently retained coordinate, define $A_d$ to be the identity. No low-frequency value of (AD.12) is used. Equations (AD.13)--(AD.14) give
$$
 \|A_d\|_{H^s\to H^s}<\frac54,\qquad
 \|A_d^{-1}\|_{H^s\to H^s}<\frac43
 \tag{AD.28}
$$
for every common Fourier weight $s$. Moreover $A_d-1$ is a complete input-diagonal operator of order $-4/3$, so it changes no order-$-1$ first coefficient.

Use $A_d$ on the right of the complete corrected trial, including its stable root trace, both incoming/outgoing maps, cutoff terms, physical positive endpoint, finite head and means. Linearity permits this common input reparametrization. Wherever the complete incoming map is genuinely invertible, the exact quotient obeys
$$
 (\mathcal B_oA_d)(\mathcal B_iA_d)^{-1}
       =\mathcal B_o\mathcal B_i^{-1}.
 \tag{AD.29}
$$
There is no assertion of that invertibility here. Compression may be factored through $A_d$ only on the declared root projection, where it commutes, or through the exact transformed operator; a phase or physical projector is not moved past it for free.

At the scalar-profile level, the exact IN.8 identity now yields
$$
 \begin{split}
 a_{d,n}\,\mathcal S_n[\widehat f_n,w^V]
 =&\ \mathcal S_n[A_n,w_0+n^{-1}w_1]
   -n^{-2}\mathcal S_n[A_n,R_2]
   -n^{-3}\mathcal S_n[A_n,R_3]\\
 &+d_n\,\mathcal S_n[g_n,w^V]
   +\mathcal S_n[Z_n,w^V],
 \end{split}\tag{AD.30}
$$
where
$\mathcal S_n[Y,w]=n^{1/6}e^{i\epsilon nX}(Y,Y_T/n)w$,
$Z_n$ is the scalar component of the integral in (AD.25), and its second component is $Z_n'$.
The exact amplitudes are
$w^V=w_0+n^{-1}w_1^V$,
$R_2=\mathcal B K_Tw_1^V+\mathcal B'E_{22}w_0$ and
$R_3=\mathcal B'E_{22}w_1^V$.
The physical completion of (AD.30) uses the same full IN reconstruction, including the inhomogeneous extra rows. It is not inferred by discarding the source of $Z_n$.

Only the first decaying reference column has the correlation (AD.17). The original complete two-by-two root estimate continues to cover the auxiliary growing column and any unrestricted two-column use. No statement here removes $g_n$, $\beta_n$, the true positive boundary row, original seam sources or the finite bordered system.

## 7. What a new scalar consumer may read

A minimal new consumer needs only the already successful complete potential value/derivative/image fields, the A normalization qualifications, and a declared original root-input threshold. Its new arithmetic can evaluate (AD.21)--(AD.23), (AD.27) and the common multiplier bounds. It must not rerun the potential, Airy reference, genuine amplitudes, old source or old phase producers.

To turn this multiplier into a physical incoming remainder, it must then compose with a complete $g_n$-column receiver in the correct domain and retain the inhomogeneous integral, free $R_2,R_3$, the free first-neglected reconstruction, positive correction, true coordinate changes, stable normalization and finite rows. The same physical mean, both signs and selected parameter must be present throughout.

Thus the new improvement is precise: the complete correlated first-column root shear has order $-8/3$, and its strong root-input tail tends to zero with the explicit fee (AD.27). No actual complete $E_i,E_o$, no full $R_0$, and no incoming or finite inverse is claimed by this analytic step.
