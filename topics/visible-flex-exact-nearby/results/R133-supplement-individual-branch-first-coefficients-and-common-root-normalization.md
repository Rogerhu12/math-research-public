# R133 supplement: individual branch coefficients and the common root input normalization

2026-11-15, newton_source.

**New exact identities and a quantitative input contract; no new numerical execution is asserted.** The two complete terminal functions in SN determine the individual incoming and outgoing first coefficients after a declared common root input change. Their means are respectively $-\mu/2$ and $+\mu/2$. The nonmean parts therefore come from the two individual SN columns, with their true density changes and errors, rather than from the norm of their difference alone.

The common finite root function is removed by an actual invertible input operator. Its complete strong and finite rank costs are retained. The real scalar part of the incoming coefficient then has an exact diagonal inverse with norm at most one. This reduces the input needed by the incoming Neumann test without asserting that its remaining strong error, finite border or full inverse has been paid.

## IC1. Same family, root and directed convention

Use the selected member of the exact repaired family, its original period $\pi/2$, physical frequencies $4j$, normalized measure and
$$
 I=\partial_\phi^{-1}(1-\Pi),\qquad
 \Lambda_j=(1+16j^2)^{1/2}.
 \tag{IC.1}
$$
The two physical mean ports remain independent. A scalar mean used in a Fourier identity below is not silently identified with either physical mean.

The primary inputs are:

| Result | Immutable Git blob | SHA256 |
|---|---|---|
| Original full branch parametrix P | 11250cbb5f9921fdaa70791b6095c306e16bc5d7 | f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7 |
| Pointwise root coefficient PF | e384f8711a44e1ad16dd05804faf65d62bf016c2 | 5856c8cf5fac8c75997a6e3d8c9aba1ad88cb136d1ae184985164d1745aab026 |
| Complete density transport CT | c60256f55e88f985e73ea1881bf5c766c95d3467 | 341a9463f267d95896d38f5500240e875077b6e6afedbdc1c0625ea24ad10a35 |
| Signed terminal contract SN | published same-name source | 6e90617095bfea61a916dcba2a5bd5ad162c696e50b03ee15f7fefd40079679c |
| Lower-order normalizer budgets LN | e0ffc101b096d5216cdf690ee84a624310ded477 | 53a3dd1dd637a61aec843262d51a2686ef9cf13f5478df4c62b93437db1c6da6 |
| Two-window strict normalizers TN | 401edaeaf8d64f32e51af6faef7c34cb0172f35a | 0ffa3261e3bb3fdea2cd05afd489b2e71b5587a2bba9432410c492e2ee64f2aa |

The original radial gauge, nonzero Airy constants, density normalization $n^{7/6}$, sign selectors and Maslov sector are those of P and PF. Remove their leading invertible factors only on their declared sides, retaining their actual norms and any previously exposed finite or opposite-sign maps. The scalar formulas below are on this same declared common branch chart. They do not commute a sign selector through a circle map.

PF.20b proves that the normalized leading root amplitudes are angular constants. After the specified radial and Airy factors have been separated, the two leading waist maps are $U_{X_-}$ for $\sigma=+$ and $U_{X_+}$ for $\sigma=-$, where
$$
 U_\psi f=\psi'(f\circ\psi),\qquad U_\alpha U_\beta=U_{\beta\circ\alpha}.
 \tag{IC.2}
$$
All occurrences of $X_\pm$ refer to the same original fixed-waist convention in PF.27.

## IC2. The common finite function is a real input change

PF.15 and CT.6 identify the common finite root function
$$
 F_*=-\frac{\ell_*}{2\eta_*}
       =\frac{b_*u_*v_*}{\eta_*},\qquad
 \widetilde C_\sigma=C_\sigma-F_*.
 \tag{IC.3}
$$
The exact selected $u_*,v_*$ have angular degree at most96, including the complete mean of $v_*$. Thus $F_*$ has degree at most192. This is a finite known field. No unknown solution is assigned finite Fourier support.

It is not legitimate to replace $C_\sigma$ by $\widetilde C_\sigma$ in an actual branch map without realizing the common input change. The following construction does so without a smallness assumption at cutoff97 or a zero-mean assumption on $F_*$.

Choose a root-coordinate cutoff $J_F\ge97$ and write
$$
 P_F=P_{\{|j|\ge J_F\}},\quad
 A_F=P_FM_{F_*}IP_F,\quad T_F=1+A_F.
 \tag{IC.4}
$$
Let $m_{F,t}$ be a complete multiplication bound for $F_*$ on $H^t$. If
$$
 \chi_{F,t}=\frac{m_{F,t}}{4J_F}<1,\qquad t=0,-4/3,
 \tag{IC.5}
$$
then the same Neumann inverse satisfies
$$
 \|T_F^{-1}\|_{H^t\to H^t}\le K_{F,t}:=(1-\chi_{F,t})^{-1}.
 \tag{IC.6}
$$
Both inverses agree on the common trigonometric domain. A sufficiently large finite $J_F$ exists because $F_*$ is smooth. An actual chosen value must satisfy both strict tests. The root-coordinate $J_F$ is not renamed as a moving-angle or principal-angle cutoff.

This input change acts as the identity below $J_F$ and on the two independently adjoined physical means. Apply $T_F^{-1}$ on the right of both complete branch maps and of every retained finite row. The homogeneous branch relation is unchanged by this common invertible coordinate change. It is never commuted through a projection or a leading circle map.

Define
$$
 F_J=M_{F_*}I-P_FM_{F_*}IP_F.
 \tag{IC.7}
$$
Both the input and output Fourier support of $F_J$ lie in $|j|\le J_F+191$. Indeed
$F_J=(1-P_F)M_{F_*}I+P_FM_{F_*}I(1-P_F)$ and multiplication adds at most192 labels. In particular the output mean is retained.

Suppose the root-reduced complete branch map is
$$
 L_\sigma=1+M_{C_\sigma}I+E_\sigma,\qquad
 E_\sigma:H^{-4/3}\longrightarrow L^2.
 \tag{IC.8}
$$
The original finite rows can either be written explicitly alongside IC.8 or included with their complete dual $H^{4/3}$ fees. This display does not grant an unmeasured norm for $E_\sigma$.

There is an exact ordered identity:
$$
 \boxed{\;
 L_\sigma T_F^{-1}
 =1+M_{\widetilde C_\sigma}I
 +(E_\sigma-M_{\widetilde C_\sigma}IA_F)T_F^{-1}
 +F_JT_F^{-1}.
 \;}
 \tag{IC.9}
$$
It follows by writing
$L_\sigma=T_F+M_{\widetilde C_\sigma}I+F_J+E_\sigma$.
The last summand is retained as a finite rank map. After multiplication by $T_F^{-1}$ its input row is not claimed to have the former finite Fourier support.

Put
$$
 \alpha_J=\frac{\Lambda_{J_F}^{4/3}}{(4J_F)^2},\qquad
 C_I=\frac{\sqrt{17}}4 .
$$
The two genuine primitives give the complete strong estimate
$$
 \|M_{\widetilde C_\sigma}IA_F\|_{H^{-4/3}\to L^2}
 \le\alpha_J\|\widetilde C_\sigma\|_\infty m_{F,-1/3}.
 \tag{IC.10}
$$
To check the intermediate spaces, the rightmost $IP_F$ maps
$H^{-4/3}$ to $H^{-1/3}$ with norm at most
$\Lambda_{J_F}/(4J_F)$. Multiplication uses $m_{F,-1/3}$.
The next $IP_F$ maps $H^{-1/3}$ to $L^2$ with norm at most
$\Lambda_{J_F}^{1/3}/(4J_F)$. Only after these steps is the complete left multiplier bounded on $L^2$. There is no assumption that this multiplier preserves a high output.

Also
$$
 \|F_JT_F^{-1}\|_{H^{-4/3}\to L^2}
 \le
 2C_I\|F_*\|_\infty
       \Lambda_{J_F+191}^{1/3}K_{F,-4/3}.
 \tag{IC.11}
$$
This is a finite rank fee, not a finite inverse. The true rows may instead be retained individually using their $H^{4/3}$ dual norms.

Consequently one permitted complete root strong budget after IC.9 is
$$
 \widehat E_\sigma=
 K_{F,-4/3}\left[
 C_{E_\sigma}
 +\alpha_J\|\widetilde C_\sigma\|_\infty m_{F,-1/3}
 +2C_I\|F_*\|_\infty\Lambda_{J_F+191}^{1/3}\right].
 \tag{IC.12}
$$
If the last term is kept in a separate exact border, it must still be included whenever that border contributes to the particular high compression being tested. A finite rank declaration alone is not a zero bound.

## IC3. Exact density conjugation of the original primitive

Let $\psi$ be a real orientation-preserving degree-one lift, and put
$$
 p_\psi=\psi-\mathrm{id}-\langle\psi-\mathrm{id}\rangle .
 \tag{IC.13}
$$
For every smooth full function, including its mean,
$$
 I U_\psi=C_\psi I-1\otimes\Pi C_\psi I+p_\psi\otimes\Pi.
 \tag{IC.14}
$$
Differentiation of the right side gives $U_\psi f-\langle f\rangle$, and its mean is zero. Thus IC.14 is the exact original primitive, not an expansion.

Normalized change of variables gives
$$
 \langle\psi^{-1}-\mathrm{id}\rangle
       =-\langle\psi-\mathrm{id}\rangle,\qquad
 p_{\psi^{-1}}\circ\psi=-p_\psi.
 \tag{IC.15}
$$
The extra term in the first equality is the integral of
$(\psi-\mathrm{id})(\psi'-1)$ and is zero. Moreover
$\langle C_{\psi^{-1}}If\rangle=-\langle p_\psi f\rangle$.
For $b=U_\psi c$ these identities prove
$$
 \boxed{\;
 U_\psi M_c I U_\psi^{-1}
   =M_b I+b\otimes p_\psi-(bp_\psi)\otimes1 .
 \;}
 \tag{IC.16}
$$
Here $(u\otimes v)f=u\langle vf\rangle$, with the corresponding conjugate in a Hermitian dual notation. Both finite rank terms are present. This same-chart identity has no additional unlisted order-minus-two term.

On the exact strong window,
$$
 \|b\otimes p_\psi-(bp_\psi)\otimes1\|_{H^{-4/3}\to L^2}
 \le \|b\|_2\|p_\psi\|_{H^{4/3}}+\|bp_\psi\|_2.
 \tag{IC.17}
$$
The row window is $H^{4/3}$, and the constant row has norm one.

The full density map $U_\psi$ preserves the integral but sends $1$ to $\psi'$.
If a physical realization instead uses
$U_\psi(1-\Pi)+\Pi$, the difference is $(\psi'-1)\Pi$.
That additional finite rank map must be retained with the two physical mean ports. IC.16 refers to the full density map.

## IC4. The two coefficients in one principal-angle chart

Let the true selected angle satisfy
$\mathcal H\circ P=R_\Omega\circ\mathcal H$ as in CT.20. Set
$$
 \mathcal S=U_{\mathcal H^{-1}}U_{X_-}
          =U_\psi,\qquad \psi=X_-\circ\mathcal H^{-1}.
 \tag{IC.18}
$$
The exact directed order gives
$$
 U_{\mathcal H^{-1}}U_{X_+}=U_{R_\Omega}\mathcal S.
 \tag{IC.19}
$$
Apply the same incoming input chart $\mathcal S^{-1}$ to the two maps in IC.9. After the declared leading constants have been separated, their forms are
$$
 \begin{split}
 B_i&=1+M_{c_i}I+\mathcal E_i,\\
 B_o&=\zeta U_{R_\Omega}
                  (1+M_{c_o}I+\mathcal E_o),\\
 c_i&=\mathcal S\widetilde C_+,\qquad
 c_o=\mathcal S\widetilde C_- .
 \end{split}\tag{IC.20}
$$
Every rank term in IC.16 and every term in IC.9 is in $\mathcal E_\sigma$ or its explicitly retained border. No actual norm is supplied by the notation.

CT.6 and CT.19 imply
$$
 c_i=U_{\mathcal H^{-1}}\widetilde f_+,\qquad
 c_o=U_{R_\Omega^{-1}}U_{\mathcal H^{-1}}\widetilde f_- .
 \tag{IC.21}
$$
The second formula requires the rotation inverse in that position.

SN.20--21 give, at the same selected parameter and true waist,
$$
 \widetilde f_\sigma=q_\sigma-\frac{\sigma\mu}{2}j,
 \qquad j=\mathcal H',\qquad \langle q_\sigma\rangle=0.
 \tag{IC.22}
$$
Since $U_{\mathcal H^{-1}}j=1$, the individual first coefficients are exactly
$$
 \boxed{\quad
 c_i=-\frac{\mu}{2}+v_i,\qquad
 c_o=+\frac{\mu}{2}+v_o,\qquad
 v_i=U_{\mathcal H^{-1}}q_+,\quad
 v_o=U_{R_\Omega^{-1}}U_{\mathcal H^{-1}}q_- .
 \quad}\tag{IC.23}
$$
Thus $\langle v_i\rangle=\langle v_o\rangle=0$ and
$c_o-c_i=\mu+v_o-v_i=c$, exactly the CT/LN coefficient. The functions $q_\sigma$ themselves have not been renamed as $c_i,c_o$. Their actual density Jacobian, common root input change and finite rank costs are explicit.

For example, if the complete root strong constants in IC.12 and the actual coordinate norms are available, IC.16 gives
$$
 C_{\mathcal E_i}\le
 \|\mathcal S\|_{L^2\to L^2}\widehat E_+
 \|\mathcal S^{-1}\|_{H^{-4/3}\to H^{-4/3}}
 +\|c_i\|_2\|p_\psi\|_{H^{4/3}}+\|c_i p_\psi\|_2,
 \tag{IC.24}
$$
and the corresponding formula for $o$ uses $\widehat E_-$ and $c_o$.
Additional physical mean-realization maps and original finite rows are added if they have not already been included. The rotation costs one in these norms. Neither the leading radial gauge nor a nonunit Airy normalization is assigned norm one by convention.

The root multiplier norm in IC.12 can be read from these same complete coefficients:
$$
 \|\widetilde C_\sigma\|_\infty
 \le\frac{|\mu|/2+\|v_\sigma\|_\infty}{\inf\psi'} .
 \tag{IC.25}
$$
The positive denominator and the coordinate norms are those of the same true map.

## IC5. Read the individual complete SN columns

Suppose a successful SN terminal receipt supplies complete bounds
$Q_{\sigma,q}$ for
$\|\partial_\phi^q q_\sigma^G\|_2$, $0\le q\le3$.
These are the saved reference, transport error and full analytic finite-angle-tail sums. Their numerical construction is not repeated.

Read the same true-angle errors $\epsilon_q$ and nonnegative inverse-density matrix $D$ from SN.26--27. Put
$$
 r_{\sigma,q}=Q_{\sigma,q}+\frac{|\mu|}{2}\epsilon_q,\qquad
 d_{\sigma,k}=\sqrt{\sup j}\sum_{q=0}^kD_{kq}r_{\sigma,q}.
 \tag{IC.26}
$$
Then $d_{+,k}$ bounds the complete $k$th derivative of $v_i$ and
$d_{-,k}$ bounds that of $v_o$. The final rotation is isometric.
The actual $G'$ analytic tail was already included in $Q_{\sigma,q}$; it is not charged again. The additional $\epsilon_q$ is the distinct true $\mathcal H'-G'$ error, with a half factor on each branch.

Define
$$
 C_{\sigma,k}=
 \left(\sum_{q=0}^k {k\choose q}d_{\sigma,q}^2\right)^{1/2}.
 \tag{IC.27}
$$
This is the exact physical Bessel convention. Full signed Fourier sums and the exact zero means give, by the same elementary estimates used in LN,
$$
 V_{\sigma,0}:=
 \min\left\{\frac{C_{\sigma,1}}2,
 \frac{C_{\sigma,2}}{\sqrt{96}},
 \frac{C_{\sigma,3}}{32},
 \sqrt{\frac{\pi d_{\sigma,0}d_{\sigma,1}}2}\right\}
 \ \ge\ \|v_\sigma\|_\infty,
 \tag{IC.28}
$$
and, directly by Cauchy--Schwarz on the same nonzero signed spectrum,
$(1+n)^{4/3}\le(27/20)n^{4/3}$ and
$(\sum_{j\ne0}n^{-4/3})^{1/2}<9/8$ give
$\|v_\sigma\|_{W^{4/3}}\le(243/160)C_{\sigma,2}<(26/17)C_{\sigma,2}$.
This estimate is not obtained by reversing a bound for a different function.
Thus
$$
 \|M_{v_\sigma}\|_{H^{-4/3}\to H^{-4/3}}
 \le \|v_\sigma\|_{W^{4/3}}
 \le\frac{26}{17}C_{\sigma,2}.
 \tag{IC.29}
$$
The nonmean sums are over all $j\ne0$, not a finite head. The zero-norm cases are the zero function and require no division. In particular the incoming multiplier test needs only the individual complete derivatives through order2; it need not use a single much larger order3 constant.

The mean contribution can also be retained orthogonally:
$\|c_\sigma\|_2\le(\mu^2/4+d_{\sigma,0}^2)^{1/2}$.
No estimate for one branch is inferred by subtracting upper bounds for their difference.

## IC6. Exact scalar preconditioning of the incoming block

Now let $P=P_{\{|j|\ge J\}}$ be the actual principal-angle projection, with all complementary finite rows retained. This $J$ is distinct from $J_F$ unless their actual coordinate relationship has been separately proved.

On the high space define
$$
 D_\mu=P\left(1-\frac{\mu}{2}I\right)P.
 \tag{IC.30}
$$
For real $\mu$, its nonzero Fourier eigenvalues have modulus
$\sqrt{1+\mu^2/(4(4j)^2)}$. Therefore, on every real Sobolev window,
$$
 \|D_\mu^{-1}\|\le1.
 \tag{IC.31}
$$
This is an exact diagonal inverse. It does not require $|\mu|/(8J)<1$.

Using the complete $\mathcal E_i$ from IC.20, the actual high incoming block factors in the indicated order:
$$
 PB_iP=
 \left[P+\big(PM_{v_i}IP+P\mathcal E_iP\big)D_\mu^{-1}\right]D_\mu.
 \tag{IC.32}
$$
Set
$$
 \begin{split}
 \chi_0(J)&=\frac{V_{+,0}}{4J}
                    +C_{\mathcal E_i}\Lambda_J^{-4/3},\\
 \chi_{-4/3}(J)&=\frac{(26/17)C_{+,2}}{4J}
                    +C_{\mathcal E_i}\Lambda_J^{-4/3}.
 \end{split}\tag{IC.33}
$$
If both are strictly below one, then
$$
 \|(PB_iP)^{-1}\|_{H^t\to H^t}\le(1-\chi_t)^{-1},
 \qquad t=0,-4/3.
 \tag{IC.34}
$$
For $t=0$ the strong-error small factor is on its high input; for
$t=-4/3$ it is on its high output. Both embeddings are necessary.
The inverse is
$D_\mu^{-1}[P+(PM_{v_i}IP+P\mathcal E_iP)D_\mu^{-1}]^{-1}$.
No factor is reversed.

All finite/high, high/finite and mean blocks remain exactly those of the transformed complete relation. Applying IC.34 does not solve the finite Schur equation. A retained finite rank contribution entering $P\mathcal E_iP$ must be charged in $C_{\mathcal E_i}$ before this test.

## IC7. Concrete new inputs and remaining strong-return obligation

The future small scalar consumer has three distinct input groups:

1. The successful SN terminal four columns for each branch, the same complete $\mu$, the true-angle errors and $D$. These provide IC.26--29 without regenerating a source, reference, ray or KAM iterate.
2. The explicit known root field $F_*$ and its finite multiplication norms, plus the actual true-chart norms and periodic displacement. These provide IC.5--17 and IC.24--25. A physical mean realization must use its own declared finite rank corrections.
3. The complete preexisting-branch strong errors, including the first-neglected free Airy/reconstruction term, the genuine root comparison, positive correction, strict propagation, both means and every seam/source/finite-row contribution. Their actual sums are still required for $C_{\mathcal E_i},C_{\mathcal E_o}$.

The new content is the identification and full normalization of the individual coefficients, together with the exact removal of their real scalar incoming part from the Neumann smallness budget. It is not a numerical proof of IC.5 or IC.33.

The ordered return identity of IN still uses the same actual incoming inverse. Its complete strong error and all bordered equations remain. The independent scalar exponential-versus-linear fee in CN/LN is not discarded by IC.31, and an EN logarithmic remainder is not obtained from an old unsigned $R_0$ bound. No full incoming, full return, finite Schur, same-background high inverse or nonlinear core solution is asserted here.
