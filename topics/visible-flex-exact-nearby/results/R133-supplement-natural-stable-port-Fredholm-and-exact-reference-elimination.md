# R133 supplement: natural stable-port Fredholm structure and exact common-reference elimination

2026-11-15, newton_source.

**Proved analytic Fredholm structure and conditional exact elimination. No new numerical evaluation.** The actual normalized terminal-Ai high family has an elliptic stable root trace on its natural Sobolev spaces. The proof uses exact root values, the full old-circle inverse on the original reflection spaces, and a complete weighted Fourier estimate. It does not upgrade an old L2 column estimate by changing its input space.

This supplies a precise way to eliminate a second reference basis after the complete incoming relation has been proved invertible. It does not prove that incoming inverse, a finite Schur inverse, or the coupled boundary problem. All supplied head, mean, ordinary-source, jump and exterior ports remain.

## SE1. Fixed objects and existing sources

The circle has period $\pi/2$, normalized measure, physical frequencies $4j$ and Bessel weights $\Lambda_j=(1+16j^2)^{1/2}$. Write $P=1-\Pi$, $I=\partial_\phi^{-1}P$, and let $P_H$ denote the original high projection $|j|\ge97$. On these coordinates $Ne_j=4|j|e_j$. No inverse power of $N$ acts on a mean.

Use the original reflection realization: the first curvature row is odd, the second is even, and $I$ maps even mean-zero functions to odd functions. Both Fourier signs are retained by complexification and then restricted to the conjugation-invariant reflection space. The scalar space $\mathcal H_H^t$ below is this same reflected high coordinate space with its actual $H^t$ norm. It does not replace two independent physical means.

The parameter is an already allowed real $|\delta|\le10^{-8}$ value, at fixed intrinsic $\eta_0$, on the original analytic root piece. Selected-angle changes are used only on their proved selected domain.

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| P, moving root parametrix | 11250cbb5f9921fdaa70791b6095c306e16bc5d7 | 35230 | f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7 |
| I, exact primitive and analytic transport | ddc62b4539d640a950c2005505e08695f80910e7 | 14772 | 38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e |
| O, ordered scalarization and parity | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 12221 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |
| A, genuine common radial columns | 62909c54de321da071a6bbc6e169e87b5888dde6 | 15528 | 0e56cf640b5c5f46c917699396e0ef6e5cce1fd5276cbddfc56ee1ed58d89c49 |
| G, ordered genuine sources | 8fa0d675d454a19451f946ed8f8a8eead7145089 | 22688 | c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e |
| B, selected-family extension of P | e561b822673bbce15c1391ee851fb93d4143d43e | 15703 | f5f980a1fb085103f548d7bbdf6fe0124dda176276fa1b8bac6783b6b22a150c |
| IN, genuine comparison and natural stable factor | f13509b4d0afc691cfc95d86c0f8e5562f919129 | 33894 | d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75 |
| BF, complete finite-factor incoming realization | 921dbfc574e94da86c8d44872a919c201c569060 | 19339 | e8e29c49deb9fabf6be9b9dd9059c26e94afbd1bc274742d7d3fe7527bf4a02e |

P.10 and G.10--20 reconstruct the complete physical rows with the original $J$. A.19--20 fix the normalized genuine Ai column and nonzero root shear. IN.28--30 fix the stable trace of the actually corrected density-normalized high columns. B extends the root construction and positive reference throughout the stated real interval.

## SE2. Complete input-dependent coefficient lemma

Suppose $a_j$ is periodic and holomorphic on one common positive strip $|\Im\phi|<\sigma$, with uniform bound $M$, for every signed high input. For $\alpha\ge0$ define on finite sums
$$
 K_\alpha f=\sum_{|j|\ge97}n_j^{-\alpha}
            a_j(\phi)e^{4ij\phi}\widehat f_j,\qquad n_j=4|j|.
 \tag{SE.1}
$$
For every fixed real $t$,
$$
 K_\alpha:H_H^t\longrightarrow H^{t+\alpha}
 \tag{SE.2}
$$
is bounded. After restricting to a strictly smaller positive strip, the output-$k$, input-$j$ coefficient is bounded by
$M n_j^{-\alpha}e^{-4\sigma|k-j|}$. The inequalities
$\Lambda_k/\Lambda_j\le1+4|k-j|$ and its reverse give
$$
 \Lambda_k^{t+\alpha}\Lambda_j^{-t}n_j^{-\alpha}
 \le(17/16)^{\alpha/2}(1+4|k-j|)^{|t+\alpha|}.
 \tag{SE.3}
$$
The resulting matrix majorant has finite row and column sums bounded by the same complete two-sided exponential sum. Weighted Schur proves (SE.2), including every output and its mean.

The lemma applies to finite sums, actual smooth coefficient products, signed diagonal factors of modulus one, and diagonal scalar sequences bounded by a multiple of $n_j^{-\alpha}$. The original analytic root product supplies the common strip for the finitely many amplitudes and derivatives below. No derivative of an error ball or exchange of a supremum with an unbounded coefficient sum is used. Individual column L2 norms alone would not prove this lemma.

## SE3. The old-circle inverse on every fixed root window

Use exactly O.2 at the root:
$$
 A=\eta_*\partial_\phi+L,\qquad
 L=PM_\ell P-2b_*P M_{v_\phi}I M_uP.
 \tag{SE.4}
$$
Here $\eta_*\ne0$ is independent of $\phi$, the domain is odd and the target is even mean-zero. The actual coefficients are smooth; $L$ is bounded between these parity spaces on each fixed Sobolev window.

The principal inverse $\eta_*^{-1}I$ is an isomorphism from even mean-zero $H^t$ to odd $H^{t+1}$. Exactly,
$$
 A\eta_*^{-1}I=1+L\eta_*^{-1}I
       \quad\text{on even mean-zero }H^t.
 \tag{SE.5}
$$
The second term gains one derivative and is compact on $H^t$: its Fourier output truncations converge in operator norm. Thus (SE.5) is Fredholm of index zero on each fixed $H^t$.

A distributional kernel vector obeys $f=-L\eta_*^{-1}If$. Repetition improves regularity by one each time, so $f$ is smooth. Then $u=\eta_*^{-1}If$ belongs to the original L2 inverse domain and $Au=0$. The already proved full inverse gives $u=f=0$. Index zero gives surjectivity and a bounded inverse on the same $H^t$. The inverses agree on the common smooth core and on overlapping distributional domains.

Consequently the same genuine $J=A^{-1}$ has
$$
 J:H_{\mathrm{even},0}^t\longrightarrow
                  H_{\mathrm{odd}}^{t+1}
       \quad\text{for each fixed real }t.
 \tag{SE.6}
$$
This is qualitative regularity, not a newly evaluated norm. Applying $J$ to (SE.5) gives
$$
 \boxed{
 J-\eta_*^{-1}I=-JL\eta_*^{-1}I:
 H_{\mathrm{even},0}^t\longrightarrow H_{\mathrm{odd}}^{t+2}.}
 \tag{SE.7}
$$
There is no $J\Pi$: the inverse has not been extended to an unpaid constant input. The independent physical mean and all projection terms remain in the original reconstruction.

## SE4. Exact normalization of the genuine root column

Let $\lambda=n^{2/3}$ and use specifically $Y_n=\widehat f_n=f_n/a_n$ from A.19, not the unnormalized terminal column. Its exact root values are
$$
 \begin{split}
 Y_n(0)&=\operatorname{Ai}(0)+\beta_n\operatorname{Bi}(0),\\
 Y_n'(0)&=n^{2/3}
       \{\operatorname{Ai}'(0)+\beta_n\operatorname{Bi}'(0)\},\\
 Y_n''(0)&=-V_n(0)Y_n(0),\qquad
 |\beta_n|\le C_\beta n^{-4/3}.
 \end{split}
 \tag{SE.8}
$$
Ai/Bi primes here are argument derivatives; $Y_n$ primes are $T$ derivatives. A.19--20 give the full shear bound and nonzero normalization. Using $f_n$ without division would require a separate $a_n-1$ term.

Let $w_0=(a_0,b_0)^t$ and
$w_1^V=(a_1^V,b_1^V)^t=w_1+\mathcal B_nK_Tw_0$ be IN.4. P.8--9 and I.21 imply
$$
 a_0(0,X)=1,\qquad b_0=O(T^2),\qquad
 a_1(0,X)=a_1^V(0,X)=0.
 \tag{SE.9}
$$
The last equality follows because the extra first component is $\mathcal B_nTb_0$. All finitely many root coefficients and derivatives below have uniform bounds on a common positive analytic strip by the original amplitude construction, complete common potential and IN.3. Free $w_1$ is not recomputed.

The actual fold identities G.2/P.19 give
$$
 T=0,\quad X=\phi,\quad T_\phi=0,\quad X_\phi=1,\quad
 DT=\lambda_*,\quad DX=0,\qquad D=\partial_r-d\partial_\phi .
 \tag{SE.10}
$$
The positive $\lambda_*$ and $\eta_*$ are radial constants at this circle. In particular $Db_0=0$ at the root.

## SE5. Orders of both complete reconstructed root rows

Before the input density $N_{\mathrm{in}}^{7/6}$, the scalar genuine trial is
$$
 F_j=e^{i\epsilon nX}
 \left[(a_0+n^{-1}a_1^V)Y_n
             +(n^{-1}b_0+n^{-2}b_1^V)Y_n'\right],
 \qquad\epsilon=\operatorname{sgn}j.
 \tag{SE.11}
$$
Its exact physical reconstruction is
$$
 h_2=PF,\qquad h_1=J(D_0-B_{\mathrm{op}})PF.
 \tag{SE.12}
$$
The trial independent mean is zero; its true mean residual remains the separate original P.12/G.20 source row.

At the root,
$$
 F_j(r_*)=e^{4ij\phi}\left[
 \operatorname{Ai}(0)+\beta_n\operatorname{Bi}(0)
 +n^{-4/3}b_1^V(0,\phi)
       \{\operatorname{Ai}'(0)+\beta_n\operatorname{Bi}'(0)\}
 \right].
 \tag{SE.13}
$$
The complete operator therefore obeys
$$
 h_2(r_*)=\operatorname{Ai}(0)\,1+R_2,\qquad
 R_2:H_H^t\longrightarrow H^{t+4/3}.
 \tag{SE.14}
$$
The exact $P$ is included in $R_2$; a low or mean obligation elsewhere is not dropped.

There is no radial carrier contribution $nDX$ at the root. The identities in SE4 give, with every surviving term retained,
$$
 DF_j=e^{4ij\phi}\left[
 (Da_0+n^{-1}Da_1^V)Y_n+\lambda_*Y_n'
 +n^{-2}(Db_1^V)Y_n'
 +n^{-2}b_1^V\lambda_*Y_n''\right]_{T=0}.
 \tag{SE.15}
$$
Because the old mean is at fixed $\phi$,
$D_0PF=P\,DF$ for the actual
$D_0=\partial_r-PM_d\partial_\phi P$.
The entire $B_{\mathrm{op}}$ of O.2 has order zero, including its projected primitive term. Hence
$$
 (D_0-B_{\mathrm{op}})h_2(r_*)
    =\lambda_*\operatorname{Ai}'(0)N_{\mathrm{in}}^{2/3}+R_0,
 \qquad R_0:H_H^t\longrightarrow H_{\mathrm{even},0}^t.
 \tag{SE.16}
$$
For example the shear in $Y_n'$ has input order $2/3-4/3=-2/3$, whereas the first term in (SE.15) has order zero. No radial derivative of an error estimate was taken.

Applying SE3 in the declared parity order yields
$$
 h_1(r_*)=\frac{\lambda_*}{\eta_*}\operatorname{Ai}'(0)
          (i\epsilon)^{-1}N_{\mathrm{in}}^{-1/3}+R_1,
 \qquad R_1:H_H^t\longrightarrow H_{\mathrm{odd}}^{t+1}.
 \tag{SE.17}
$$
Here $JR_0$ gains one derivative and
$(J-\eta_*^{-1}I)N^{2/3}$ gains $4/3$. The worst gain one includes both errors and every projected term.

## SE6. Actual stable trace: diagonal plus a compact gain

The genuine global Riccati root conversion is frequency diagonal. Its proved comparison with the mixed rows
$(N_{\mathrm{out}}^{1/3}h_1,h_2)$ has factor at most nine. Its stable row is therefore a bounded frequency-diagonal map of this pair on every fixed $H^t$. This does not move $N$ through any nonconstant coefficient.

Applying that actual row and the actual output $P_H$ to SE5 gives
$$
 \boxed{
 S_{\mathrm{nat}}=D_c+K,\qquad
 K:\mathcal H_H^t\longrightarrow\mathcal H_H^{t+2/3}
                  \quad\text{for every fixed }t.}
 \tag{SE.18}
$$
The first error is $N_{\mathrm{out}}^{1/3}R_1$, with gain $2/3$, and the second has gain $4/3$. The exact principal diagonal is P.20/IN.30:
$$
 c_n=\frac{\operatorname{Ai}(0)
               -(\lambda_*/\eta_*)\operatorname{Ai}'(0)}
             {\sqrt{1+\widetilde p_n}},
 \quad0<\widetilde p_n<66,\quad c_n>1/25.
 \tag{SE.19}
$$
It is also bounded above on the same root domain. Thus $D_c$ and $D_c^{-1}$ are bounded in every stated window. Both signs use the same genuine normalization and preserve the reflection restriction.

This is the stable trace of the actual PC/IN corrected high Poisson family. IN.28 gives its correction **zero stable root input**, so the stable trace equals the trial trace. The cutoff is one at the root, and the true positive graph still chooses the regular outer boundary.

No removed low output is claimed to vanish in the coupled problem. Its low root trace, physical mean residuals, supplied head and high/low cross equations remain in their original ports.

## SE7. Fredholm index without an evaluated cutoff

The inclusion $\mathcal H_H^{t+2/3}\hookrightarrow\mathcal H_H^t$ is compact by Fourier truncation. Consequently
$$
 S_{\mathrm{nat}}=D_c(1+D_c^{-1}K)
   \quad\text{is Fredholm of index zero on }\mathcal H_H^t.
 \tag{SE.20}
$$
In particular this applies at $t=-7/6$ and $-5/2$. It does not yet assert invertibility at cutoff 97.

Its kernel is smooth: $f=-D_c^{-1}Kf$ repeatedly gains $2/3$ derivatives. This also identifies the kernels in the different fixed windows. The gain norm is finite, but no new numerical value is claimed. P.21's old L2 Hilbert--Schmidt tail alone did not prove this negative-window assertion; SE2--6 are the additional operator argument.

## SE8. Natural weights and the common incoming coordinate

Let $S_{\mathrm{tr}}^Y$ be IN.28's stable trace in the original $Y=N_{\mathrm{out}}^{-1}Z$ frame for the PC density-normalized input. Exactly,
$$
 S_{\mathrm{nat}}=
 N_{\mathrm{out}}S_{\mathrm{tr}}^Y N_{\mathrm{in}}^{-7/6},
 \qquad
 S_{\mathrm{tr}}^Y=
 N_{\mathrm{out}}^{-1}S_{\mathrm{nat}}N_{\mathrm{in}}^{7/6}.
 \tag{SE.21}
$$
The two frequency factors stay on their own sides. They are not commuted with a coefficient, projection or chart.

For a declared common input space $\mathcal X_s$, let
$N_i:\mathcal X_s\to\mathcal H_H^s$ be the actual bounded incoming-coordinate isomorphism. Distinguish the full signed carrier $P_{97}H^s$ from the natural reflected root domain $\mathcal H_H^s$ of SE1. The ordered MS formula is $\Lambda_+^{-1}T_F^{-1}\mathcal S^{-1}$ on the ambient carrier; its natural-root restriction has the domain
$$
 \mathcal X_s=N_i^{-1}\mathcal H_H^s
 =\mathcal S T_F\Lambda_+\mathcal H_H^s
 =\mathcal S D_+\mathcal H_H^s,\qquad
 D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_- .
$$
Here $\Lambda_+=aD_+$ with $a>0$ on the original nonmean high carrier. $D_+$ preserves real Fourier conjugacy and is an isometry, but generally does not preserve even reflection. Thus $\mathcal S\mathcal H_H^s$ alone is not the justified domain. At a selected member $\mathcal S$ is its actual MS chart; a full-family frozen realization is specified separately in [NIF](R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md).

The actual moving reference has $u$ odd and $v$ even, so $F_*=\beta_*u_*v_*/\eta_*$ is odd. Reflection reverses both $M_{F_*}$ and $I$, hence $T_F$ and its same inverse preserve the natural reflected space. The complete degree192, double-high definition also gives $[T_F^{\pm1},D_+]=[T_F^{\pm1},P_{97}]=0$, proving the displayed range equality. The natural-reflection projector is $\mathcal S D_+Q_{\rm nat}D_+^{-1}\mathcal S^{-1}$, with $Q_{\rm nat}=P_{97}(1+\mathscr R)/2$ in the complexified even realization; it is distinct from the ambient $\mathcal S P_{97}\mathcal S^{-1}$. $\Lambda_+$ is a root scalar diagonal, not a Bessel weight. The physical mean extension, original Fourier low complement and every independent rest port remain separate; the opposite-reflection complement is not a finite head. No arbitrary compression product or enlarged old-circle inverse is used.

Define
$$
 C_s=S_{\mathrm{tr}}^Y N_i:
 \mathcal X_s\longrightarrow
        \mathcal Y_s:=\mathcal H_H^{s-1/6}.
 \tag{SE.22}
$$
It is Fredholm of index zero by SE7 and the bounded isomorphisms in (SE.21). The precise two windows are
$$
 \begin{array}{c|c|c}
 s&\text{window for }S_{\mathrm{nat}}&
                       \text{stable }Y\text{ window}\\ \hline
 0&-7/6&-1/6\\
 -4/3&-5/2&-3/2
 \end{array}
 \tag{SE.23}
$$
This is not an unweighted L2 estimate for $S_{\mathrm{tr}}^Y$.

If $C_sx=0$, then $N_{\mathrm{in}}^{7/6}N_ix$ lies in the smooth kernel of $S_{\mathrm{nat}}$. Hence $N_ix$ is smooth. The original smooth Ai and positive-Poisson identities may therefore be applied to this kernel vector without assuming an unproved positive theorem on arbitrary rough stable data.

## SE9. Conditional complete incoming injectivity

Let $\mathcal P_s$ be the stable-input column of the original positive seven-port map, with its specified supplied head and all other inputs zero. Let $\Psi_A$ be the corrected density-normalized terminal-Ai family. On the smooth core IN.28 states
$$
 \Psi_A=\mathcal P_s S_{\mathrm{tr}}^Y.
 \tag{SE.24}
$$
Its incoming and outgoing maps use the **single common input** $N_i$, with every required finite and physical mean row. The outgoing order is precisely MS; its global sign has not been moved through a density chart.

Assume that the complete incoming realization is injective on this Ai family: an input $(x,0)$, with every other independent port zero, vanishes if all actual incoming equations vanish. A bounded inverse of the complete BF incoming realization is sufficient. A high-compression inverse alone is insufficient.

For $C_sx=0$, SE8 makes $N_ix$ smooth. Equation (SE.24) and uniqueness of the original positive given-head graph give $\Psi_A N_ix=0$, including its genuine regular boundary condition. All actual incoming rows vanish, so the stated injectivity gives $x=0$.
Thus $\ker C_s=0$, and its proved index zero yields
$$
 \boxed{C_s:\mathcal X_s\longrightarrow\mathcal Y_s
                    \text{ is a bounded isomorphism}.}
 \tag{SE.25}
$$
No separately evaluated norm of $C_s^{-1}$, growing reference column, or new stable-root cutoff is required for this implication.

It holds in both windows when the complete incoming hypothesis holds there. The inverses are compatible because (SE.21) is one exact map on a common smooth/distributional core.

## SE10. All other ports and exact return cancellation

Denote the remaining independent parameter space by
$\mathcal P_s^{\mathrm{rest}}$, retaining its original function-space and finite-coordinate norms. It may be infinite dimensional. It includes the supplied head functions, independent means, ordinary sources, exterior data, jumps and any other genuinely independent input of the declared realization.

Let $\mathbb I_P,\mathbb O_P$ be incoming/outgoing maps with physical stable coordinate $y$ and remaining data $p$. Let $\mathbb I_A,\mathbb O_A$ be the same complete maps after substituting $y=C_sx$, without changing $p$. Every coupled row remains. On the smooth core,
$$
 \mathbb I_A=\mathbb I_P\mathbb D_C,\qquad
 \mathbb O_A=\mathbb O_P\mathbb D_C,\qquad
 \mathbb D_C=\operatorname{diag}
           (C_s,1_{\mathcal P_s^{\mathrm{rest}}}).
 \tag{SE.26}
$$
After (SE.25), these identities extend on their declared trace spaces. If the physical trace maps were not separately extended to the rough stable space $\mathcal Y_s$, the formulas
$$
 \mathbb I_P=\mathbb I_A\mathbb D_C^{-1},\qquad
 \mathbb O_P=\mathbb O_A\mathbb D_C^{-1}
 \tag{SE.27}
$$
give their unique bounded trace extensions from the smooth positive family. They agree there with the original given-head Poisson maps. This supplies no new bulk state bound or nonlinear theorem on arbitrary rough data.

If the **complete** $\mathbb I_A$ is a bounded isomorphism in the actual square realization, then
$$
 \mathbb I_P^{-1}=\mathbb D_C\mathbb I_A^{-1},\qquad
 \boxed{\mathbb O_P\mathbb I_P^{-1}
              =\mathbb O_A\mathbb I_A^{-1}.}
 \tag{SE.28}
$$
The common factor cancels on its correct side. It is never commuted through a cutoff, $N^{7/6}$, a sign operator, a density map or an original finite row.

An explicit bound for the physical incoming inverse would still require
$$
 \|\mathbb I_P^{-1}\|
 \le\max(\|C_s\|,1)\|\mathbb I_A^{-1}\|.
 \tag{SE.29}
$$
The return equality itself does not require a numerical value of $C_s^{-1}$.

## SE11. Precisely which second reference is eliminated

A genuine radial fundamental matrix has two independent columns. This does not make its growing column a further free coordinate of the same regular positive given-head graph. That graph is parameterized by its high stable input and its explicitly separate ports.

Under the complete incoming hypothesis, SE6--10 show that the normalized terminal-Ai family spans this regular high family on the natural trace spaces. A second basis used solely to represent that same family can be eliminated by the exact common-coordinate relation. It need not be estimated as an additional infinite error and is not called finite rank.

This does not remove a genuinely independent second-column input of a different problem, a nonregular solution, an exterior datum or another supplied positive port. Such an input remains in $\mathcal P_s^{\mathrm{rest}}$, with its actual type and coefficients. Its removal would first require identification with the same graph in (SE.24).

Nor does this theorem make the Maslov sign conjugate, opposite-sign maps, coefficient multipliers or WE placeholders finite rank. MS/ZD retain the global sign terms in their actual order. BF retains only proved finite factorizations in its augmented Schur system.

## SE12. Conclusion and remaining gates

The new result is the complete root gain $2/3$, the index-zero Fredholm property in the two required natural negative windows, and the conditional complete-port cancellation (SE.28). No old successful root, Airy, source, positive graph, propagation, KAM, scalar or finite arithmetic was reevaluated.

The actual complete incoming strong/finite realization, its injectivity or inverse, all retained physical equations, and any requested numerical bound for a rough bulk extension remain separate obligations. The positive seven-port map, a large safe source upper bound or a scalar Cayley gap alone does not supply them.
