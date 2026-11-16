# R133 supplement: complete coefficient reflection and the physical paired waist leading row

2026-11-16, newton_source.

**Proved analytic conclusion at the original selected real member.** The two complete root first coefficients satisfy an exact reflected identity. In the actual selected coordinates this gives $c_o=-R_{a+\Omega}c_i$, with all scalar means included. It identifies the principal part of the real paired waist row; it does not make the individual incoming principal an endomorphism of its reflected input space.

The first off-diagonal waist normalizer could in principle change the first coefficient of that row. Here its value is exactly zero. This follows from the original metric's exact radial parity, its actual differentiability at the waist, and the support of the compact metric perturbation. Consequently the complete physical primitive row has leading part $P\Pi_a^+T_i$ on its correct transported reflected input. Its second-order normalizer, output-mean rank, all genuine state errors, and the original finite complement remain.

No scientific arithmetic is executed. No previously saved upper bound is subtracted, recomputed, or reinterpreted as a lower bound. The formulas below specify complete operators and new symbolic norm consequences.

## WPL1. Scope, conventions and original sources

Fix the same selected member $\delta_*$, real repaired coefficient state, true rays, KAM chart $\mathcal H$, original cutoff 97, and homogeneous terminal-Ai column as WRA. The independent source/head/reference ports are set to zero only to specify this column. They remain separate inputs in the complete problem.

Use the circle of period $\pi/2$, normalized angular measure, and physical frequencies $4j$. Put
$$
 P=Id-\Pi,\qquad I=\partial_\phi^{-1}P,\qquad
 Rf(\phi)=f(-\phi),\qquad R_*f(x)=f(-x),
 \qquad R_c f(x)=f(c-x).
 \tag{WPL.1}
$$
The names $R$ and $R_*$ distinguish the raw waist and root circles. Sobolev norms use $\Lambda_j=(1+16j^2)^{1/2}$, and a Wiener norm below means $W_s(f)=\sum_j(1+|4j|)^s|\widehat f_j|$. The metric coefficient is denoted throughout by $\beta_{\rm metric}=a_{\rm phys}'/a_{\rm phys}$. It is unrelated to the phase angle named $\beta$ in the original exact-affine geometry, or to the scalar return parameter.

The existing complete statements used here are pinned individually:

| Original statement and exact role | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| PF.15--27: root gauge, finite function and complete first coefficient | e384f8711a44e1ad16dd05804faf65d62bf016c2 | 20413 | 5856c8cf5fac8c75997a6e3d8c9aba1ad88cb136d1ae184985164d1745aab026 |
| CT.4,6,10--11: individual complete coefficient transport | c60256f55e88f985e73ea1881bf5c766c95d3467 | 17825 | 341a9463f267d95896d38f5500240e875077b6e6afedbdc1c0625ea24ad10a35 |
| IC.16,20,23: whole density conjugation and the original individual first coefficients | bd4ed3ab5d72a10021df281542d080ef2f67fb0e | 17274 | 4164e4a7a10db651654cf63b7ecf7772fc1ba2cb966da4f9347711156301ddee |
| Strict-cut N.8--11: both ordered off-diagonal normalizers | da51581b623d4167ae9278af6892bc9a0591fb3f | 13892 | 4d44bbe7082d4ee967ebf9d02284b3510624624ab98adb087b8d0499eb030376 |
| MS: common incoming normalization and actual outgoing sign order | 10fdaddc0114e25ad349f1f411e80baf4f98fe26 | 19522 | 44038eaed377863961aad7f0c74caa2bf498d6a689812f05933111777c191161 |
| NIF: corrected reflected input and bounded same-order coordinate maps | d606faa1ffd30c34d3487985a57dbc62a18890bc | 32942 | 8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640 |
| RRF: exact target and input reflections, including the full mean rank | cdb4b957f6976c7b72e974fcccc8f2a15afbee74 | 15266 | 803302f2924da51022e2aa16a36c928ee0789fde93277f5ea9fd9c2ae2a3630f |
| WPR: physical pair and primitive/mean waist rows | 226272031762c5fcace679dd7f940a35040401dc | 22571 | 707b8269e454cab738fe70d84097087a0cf5c74026916a2f8bdc151435eca9cb |
| WRA: complete restricted incoming error and same-tuple state defect | ffe98b2256041bdc4a49d85146ddc48afb301e2c | 26647 | 40fb2167aa27c9f9e07bfcaea89c6f5d20059cc724eb7ba4930e02b16dd27889 |
| R77.1--4: exact radial parity of the original metric | ba843df645c734a714ef29a4d341fb0679832900 | 9207 | 0a7276239ea25ceb87ca386e48e7c9901a7503edf52baad1d3ba753b51ae1243 |
| Exact germ matching, sections 1--2: actual $a,E,K$ regularity at every common knot | c042452ab7368515954ef2586a62d81b0f37d775 | 10948 | bb9a14f2d54db722c3505b5d36bb7422995a74465c20ce0888382b4d438b6752 |
| Polynomial Codazzi P, section 3: the current compact metric and its support | 1b73111e5cf90876f1e593274b27cb1074915b85 | 11606 | 43ee65f22d64aed7d4f156647d0043e7626f2669b31c784a16c72169e6af8e35 |

The IC row is its original mathematical body before the later MS scope clarification. This proof uses the corrected MS common-output order, not the earlier unqualified scalar Maslov reading. The original metric references in the last three rows are used only for the exact waist identity in WPL7; no old floating geometry report is used as a certificate.

All selected-coordinate conclusions below concern $\delta_*$. NIF's qualified frozen input family does not extend the old selected $T_i,T_o,\mathcal H$ factorization to every member of that family. The underlying raw coefficient parity and the local waist metric identities apply wherever their original real-family hypotheses hold, but that is a separate assertion.

## WPL2. The complete root first coefficients have opposite reflected signs

For the original angular reflection, the full fields have
$$
 Ru=-u,\quad Rv=v,\quad Rd=-d,\qquad
 r_\sigma=u+\sigma qv,\qquad
 B_\sigma=-\frac{q_r}{2q}
                 -\beta_{\rm metric}(1+r_\sigma^2).
 \tag{WPL.2}
$$
Here $q,\eta,\beta_{\rm metric}$ are radial scalars and
$\eta=-\gamma\Pi v>0$. In particular the entire mean of $v$ is present. The exact identities are
$$
 Rr_\sigma=-r_{-\sigma},\qquad
 R(r_\sigma)_\phi=(r_{-\sigma})_\phi,\qquad
 RB_\sigma=B_{-\sigma}.
 \tag{WPL.3}
$$
PF.20 gives the complete first coefficient of the strict generator:
$$
 a_\sigma=-d_{\phi\phi}
  -\beta_{\rm metric}(r_\sigma)_\phi r_{-\sigma}
  +\frac{\sigma B_+B_-}{2\eta q}.
 \tag{WPL.4}
$$
Each term in (WPL.4) obeys
$$
                         Ra_\sigma=-a_{-\sigma}.
 \tag{WPL.5}
$$
Equivalently, CT.10--11 splits $a_\sigma=a_{\rm e}+\sigma\Xi/2$ with $a_{\rm e}$ odd and $\Xi$ even. This is an identity of the complete functions, not only of their zero Fourier coefficients.

Let $H_\sigma$ be the true root-labelled flow in PF/RRF, and let $J_\sigma=H_\sigma'$. Its actual root initialization and the coefficient parity give
$$
 H_\sigma(\rho,-x)=-H_{-\sigma}(\rho,x),\qquad
 J_\sigma(\rho,-x)=J_{-\sigma}(\rho,x).
 \tag{WPL.6}
$$
The original complete first coefficient satisfies CT.4,
$$
 \partial_\rho C_\sigma=-J_\sigma(a_\sigma\circ H_\sigma).
$$
Equations (WPL.5)--(WPL.6) imply
$$
                    \partial_\rho(C_-+R_*C_+)=0.
 \tag{WPL.7}
$$

The constant function of $\rho$ in (WPL.7) is fixed by the original root normalization. PF.15--23 gives, in every fixed angular Sobolev norm,
$$
 C_\sigma(\rho,x)
 =\frac{\sigma g_0}{3\rho^{3/2}}
   +\frac{\sigma\widehat g_1(x)}{\sqrt\rho}
   +F_*(x)+O_{H^s}(\sqrt\rho),
 \qquad
 F_*=-\frac{\ell_*}{2\eta_*}
        =\frac{\beta_{{\rm metric},*}u_*v_*}{\eta_*}.
 \tag{WPL.8}
$$
The radial $g_0$ is even. The complete subleading function is
$$
 \widehat g_1
 =g_0\left[-\frac{\eta_\rho}{\eta}
      +\frac32\frac{k_\rho}{k}
      -8\beta_{\rm metric}(1+u^2)\right]_*
      +g_0d_{\phi,*},
$$
so it is even. The finite function $F_*$ is odd. Therefore every displayed singular term and the complete finite function cancel in $C_-+R_*C_+$, whose limit is zero. The constant in (WPL.7) is exactly zero:
$$
 \boxed{\quad
 C_-=-R_*C_+,\qquad
 \widetilde C_-=-R_*\widetilde C_+,\qquad
 \widetilde C_\sigma=C_\sigma-F_*.
 \quad}
 \tag{WPL.9}
$$
Subtracting the same odd $F_*$ preserves this identity. No independent root integration constant, reset of the two phases, or deletion of a mean term is used.

At the original seams these are the same complete transported coefficient and root gauge as PF.26. Its continuous first coefficient has no additional order-minus-one jump. Higher normalizer and source jumps remain in the already retained error.

## WPL3. The actual selected principal pair

Write
$$
 \mathcal S=U_{\mathcal H^{-1}}U_{X_-},\qquad
 U_\psi f=\psi'(f\circ\psi),\qquad
 b=a+\Omega,
 \qquad \mathcal S R_*\mathcal S^{-1}=R_b .
 \tag{WPL.10}
$$
The phase $a$ is the actual RRF reflection phase; it is not set to zero. The translation $U_{R_\Omega}$ has unit Jacobian and satisfies $U_{R_\Omega}R_b=R_a$.

IC.20 uses exactly
$c_i=\mathcal S\widetilde C_+$ and
$c_o=\mathcal S\widetilde C_-$.
Thus (WPL.9) proves
$$
 \boxed{\quad c_o=-R_b c_i,\qquad
 T_o=R_bT_iR_b,\qquad
 T_i=Id+M_{c_i}I,\quad T_o=Id+M_{c_o}I.\quad}
 \tag{WPL.11}
$$
The second equality is exact on the full auxiliary circle because $R_bIR_b=-I$, including its zero action on constants. It is not an equality only modulo a primitive rank or strong error. In particular
$$
 \nu_i:=\Pi c_i,\qquad \Pi c_o=-\nu_i,\qquad
 \mu=\Pi(c_o-c_i)=-2\nu_i.
 \tag{WPL.12}
$$
These are the original individual coefficients and original signed return mean.

The physical reflected input is the NIF space
$$
 X_s^{\rm fr}=\mathcal S D_+\mathcal H_{\rm nat}^s,\qquad
 \mathcal H_{\rm nat}^s=P_{97}\operatorname{Fix}(R_*),
 \qquad
 D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_- .
 \tag{WPL.13}
$$
Set $Z=\Pi+i\Pi_+-i\Pi_-$, $\mathcal J=\mathcal S Z\mathcal S^{-1}$. On the full nonmean carrier, RRF gives the involution and the actual input projection
$$
 J_X=-\mathcal J R_b,\qquad
 Q_X=\frac12 P_{97}^{\mathcal S}(Id-\mathcal J R_b),
 \qquad
 P_{97}^{\mathcal S}=\mathcal S P_{97}\mathcal S^{-1}.
 \tag{WPL.14}
$$
Here $\mathcal J^2=-Id$ and $R_b\mathcal J=-\mathcal J R_b$. The factors in $Q_X$ commute as transports of the original commuting root objects. The projection is not replaced by ordinary $P_{97}$ and is not declared orthogonal.

The exact ambient nonmean identity and its restriction are
$$
 \begin{aligned}
 U_{R_\Omega}T_o\mathcal J&=R_aT_iJ_X,\\
 U_{R_\Omega}T_o\mathcal Jx&=R_aT_ix
                       \qquad(x\in X_s^{\rm fr}).
 \end{aligned}
 \tag{WPL.15}
$$
For example $J_Xx=x$ is equivalent to $R_bx=\mathcal Jx$, and then $R_b\mathcal Jx=x$. This proves (WPL.15) in its original order. The outgoing sign operator is not commuted through $T_o$, the rotation, or the input chart.

Equation (WPL.15) identifies the paired principal relation. It does not assert $T_iX_s^{\rm fr}=X_s^{\rm fr}$. WPR's noninvariance result remains valid.

## WPL4. The physical mean rank in the pair is still present

Retain the full positive density
$$
 h=U_{\mathcal H^{-1}}1,\qquad
 \Pi h=1,\qquad R_a h=h,\qquad
 K_{\mathcal H}=R_a-2h\otimes\Pi .
 \tag{WPL.16}
$$
WPR/RRF identifies the actual physically reflected pair on this same homogeneous column:
$\mathcal O_{\rm com}=K_{\mathcal H}\mathcal I_{\rm com}$.
By WRA,
$\mathcal I_{\rm com}=T_i+E_i^{\rm fr}$ on $X^{\rm fr}$, where
$E_i^{\rm fr}:X_{-4/3}^{\rm fr}\to L^2_{\rm full}$ has the complete same-tuple SWA bound. Combining the actual relation with (WPL.15) gives
$$
 \boxed{\quad
 E_{o,{\rm com}}^{\rm fr}
 :=\mathcal O_{\rm com}-U_{R_\Omega}T_o\mathcal J
 =K_{\mathcal H}E_i^{\rm fr}
       -2h\otimes\rho_i,\qquad
 \rho_i=\left.\Pi T_i\right|_{X^{\rm fr}}.
 \quad}
 \tag{WPL.17}
$$
Although $\Pi x=0$ on this input space, $\rho_i(x)$ is generally nonzero. In the original bilinear functional convention,
$$
 \rho_i(x)=\Pi(c_iIx)
          =-\Pi\bigl(I(c_i-\nu_i)x\bigr),\qquad
 \|\rho_i\|_{(X_{-4/3}^{\rm fr})^*}
       \le\|I(c_i-\nu_i)\|_{H^{4/3}}.
 \tag{WPL.18}
$$
In a Hermitian dual notation the corresponding row is conjugated. The norm is the same. A useful complete symbolic majorant is
$\|I(c_i-\nu_i)\|_{H^{4/3}}\le(\sqrt{17}/4)W_{1/3}(c_i-\nu_i)$; it follows from the physical frequencies $4j$, with no restriction on the scalar mean of $c_i$.

For example
$$
 \|K_{\mathcal H}\|_{L^2\to L^2}
       \le1+2\|h-1\|_2,\qquad
 \|E_{o,{\rm com}}^{\rm fr}\|
       \le(1+2\|h-1\|_2)\|E_i^{\rm fr}\|
                +2\|h\|_2\|\rho_i\|.
 \tag{WPL.19}
$$
The first follows by writing
$K_{\mathcal H}=(R_a-2\Pi)-2(h-1)\Pi$, where $R_a-2\Pi$ is unitary. These are unevaluated whole bounds; no new constant is claimed.

One may express the exact paired compatibility without identifying input and target. The corrected principal pair
$$
 \widehat L_{\rm pair}x=
     \binom{T_ix}{K_{\mathcal H}T_iJ_Xx}
$$
intertwines $J_X$ with the actual pair involution
$(f,g)\mapsto(K_{\mathcal H}g,K_{\mathcal H}f)$.
The original common principal pair
$(T_i,U_{R_\Omega}T_o\mathcal J)$
differs from this pair precisely by the second-row rank
$2h\otimes(\Pi T_iJ_X)$.
This rank is retained in the full pair and in every mean or amplitude readout. An auxiliary identity extension of $J_X$ on a scalar mean does not remove the two original physical mean slots.

## WPL5. Exact compression of the ordered waist normalizer

At the actual waist put
$$
 q_w=q(0)>0,\qquad
 \eta_w=\eta(0)=-\gamma(0)\Pi v(0)>0,\qquad
 \kappa=\frac{\sqrt{q_w/2}}{n_g(0)}.
 \tag{WPL.20}
$$
The symbol $\eta_w$ is a physical coefficient, not the fixed intrinsic parameter called $\eta_0$ elsewhere. All of $v$, including its mean, remains in (WPL.20).

Let $J_s=268435456$ be the original selected strict-normalizer cutoff recorded in WRA, and retain its ordered bounded matrix operator at the waist:
$$
 \mathscr T_J=(Id+\mathsf A)(Id+\mathsf B),\qquad
 \mathsf A=P_{J_s}\mathbf S I P_{J_s},\qquad
 \mathsf B=P_{J_s}\mathbf Z I^2 P_{J_s}.
 \tag{WPL.21}
$$
Bold $\mathbf Z$ denotes the second off-diagonal normalizer; it is not the Fourier sign $Z$. Each scalar cutoff acts componentwise. The matrices are the original strict-cut N.10 coefficients, and the original full finite head is preserved.

WPR proves that $\mathscr T_J$ and its already qualified inverse commute with the wave-swap reflection $ER$, preserve nonmeans, and are identity on the two constant components. For $v\in PH^s$, define
$$
 E_Rv=\binom v{Rv},\qquad
 T_{\rm ref}=\operatorname{pr}_+\mathscr T_J E_R,\qquad
 T_{\rm ref}^{-1}=\operatorname{pr}_+\mathscr T_J^{-1}E_R.
 \tag{WPL.22}
$$
The graph $\operatorname{ran}E_R=\operatorname{Fix}(ER)$ is invariant. Hence
$\mathscr T_JE_R=E_RT_{\rm ref}$, and the second expression in (WPL.22) is its actual two-sided inverse. In the ordinary component Hilbert norm,
$\|E_Rv\|=\sqrt2\|v\|$, while the first component of a vector in this graph has norm exactly its full norm divided by $\sqrt2$. Thus
$$
 \|T_{\rm ref}\|_s\le\|\mathscr T_J\|_s,\qquad
 \|T_{\rm ref}^{-1}\|_s\le\|\mathscr T_J^{-1}\|_s .
 \tag{WPL.23}
$$
There is no extra component factor. Extend $T_{\rm ref}$ by the identity on constants. Define
$$
 \mathcal A_J=U_{\mathcal H^{-1}}T_{\rm ref}U_{\mathcal H},
 \qquad P_h=Id-h\Pi .
 \tag{WPL.24}
$$
Then $\Pi\mathcal A_J=\Pi$, $\mathcal A_Jh=h$, and
$PU_{\mathcal H}=U_{\mathcal H}P_h$.
This does not say that $\mathcal A_J$ commutes with $R_a$ or fixes the ordinary constant function.

For a physically paired scalar $f,K_{\mathcal H}f$, put
$v=PU_{\mathcal H}f$. The second nonmean raw component is exactly $Rv$, because
$PU_{\mathcal H}K_{\mathcal H}=RPU_{\mathcal H}$.
With $e^T=(1,1)$, the original physical primitive row is therefore
$$
 \begin{aligned}
 &\kappa U_{\mathcal H^{-1}}e^T\mathscr T_J P
     \operatorname{diag}(U_{\mathcal H},U_{\mathcal H})
                 \binom f{K_{\mathcal H}f}\\
 &\hspace{25mm}
       =2\kappa\Pi_a^+\mathcal A_JP_hf,
       \qquad \Pi_a^+=\frac{Id+R_a}{2}.
 \end{aligned}
 \tag{WPL.25}
$$
This is an equality for the primitive $Ih_1$, expressed in the selected target coordinates. The raw $h_1$ row contains the original derivative. It has not been assigned a free raw $L^2$ bound.

In particular the actual same-column physical primitive row is
$$
 \mathfrak W_\partial
     =2\kappa\Pi_a^+\mathcal A_JP_h(T_i+E_i^{\rm fr})
       :X^{\rm fr}\longrightarrow P\operatorname{Fix}(R_a).
 \tag{WPL.26}
$$
The full target, including all low output modes, is prescribed by the original physical reflection. It is not defined as the image of an unknown incoming map.

The rank distinguishing $K_{\mathcal H}T_i$ from $R_aT_i$ has zero contribution to this primitive row because $PU_{\mathcal H}h=P1=0$. This exact annihilation is limited to this row. The mean/rank statement (WPL.17) and the other physical readouts still apply.

## WPL6. The possible first-order correction and its complete rank terms

Before using any special waist value, write
$s=\mathbf S_{+,-}$ and
$t=-Rs=\mathbf S_{-,+}=B_-/(2\eta q)$.
Both matrices in (WPL.21) are off-diagonal, so
$$
 T_{\rm ref}
  =Id+\mathsf A_{+,-}R+\mathsf B_{+,-}R
                                      +(\mathsf A\mathsf B)_{+,+}.
 \tag{WPL.27}
$$
Only after the actual left even projection one has
$$
 \Pi_R^+\mathsf A_{+,-}R
     =\Pi_R^+P_{J_s}M_t I P_{J_s},
 \qquad \Pi_R^+=(Id+R)/2.
 \tag{WPL.28}
$$
Indeed $RIR=-I$, $R$ commutes with $P_{J_s}$, and $\Pi_R^+R=\Pi_R^+$. This identity does not commute an unprojected $T_{\rm ref}$ with reflection.

Set $\chi=\mathcal H^{-1}$,
$p_\chi=\chi-id-\Pi(\chi-id)$, and $b_t=U_\chi t$. The exact full-circle IC.16 identity is
$$
 U_\chi M_tI U_\chi^{-1}
       =M_{b_t}I+b_t\otimes p_\chi
                          -(b_tp_\chi)\otimes1.
 \tag{WPL.29}
$$
Both ranks are present. Keep the actual finite complement and higher primitive terms as
$$
 \begin{aligned}
 \mathcal F_t&=U_\chi(M_tI-P_{J_s}M_tIP_{J_s})U_{\mathcal H},\\
 \mathcal V_2&=U_\chi\{\mathsf B_{+,-}R
                         +(\mathsf A\mathsf B)_{+,+}\}U_{\mathcal H}.
 \end{aligned}
 \tag{WPL.30}
$$
The old degree-192 first normalizer makes the difference in the first line genuinely finite before conjugation, with both Fourier ends at most $J_s+191$. After the density conjugation it remains finite rank with its actual dual rows; it is not asserted to have the same Fourier support. The second line keeps its two- and three-primitive ordered products.

Equations (WPL.27)--(WPL.30), and $\mathcal A_Jh=h$, give the complete projected identity
$$
 \begin{aligned}
 \Pi_a^+\mathcal A_JP_hT_i
 =\Pi_a^+\bigl\{&
 Id+M_{c_i+b_t}I+M_{b_t}IM_{c_i}I\\
 &+[b_t\otimes p_\chi-(b_tp_\chi)\otimes1]T_i
      -\mathcal F_tT_i+\mathcal V_2T_i
      -h\otimes(\Pi T_i)\bigr\}.
 \end{aligned}
 \tag{WPL.31}
$$
All right factors retain their order. This formula is after $\Pi_a^+$; it is not an unprojected expansion of $\mathcal A_J$.

It follows that the first coefficient of a general such primitive row would be $c_i+b_t$, with mean $\nu_i+\Pi t$, since a full density pullback preserves the integral. Neither a two-window inverse for $T_i$ nor its sign of mean would justify ignoring this contribution. The next section proves its exact value for the actual waist.

## WPL7. Why the actual first waist normalizer is exactly zero

The original exact-affine geometry imposes radial parity by the defining projections $f(r)\mapsto(f(r)\pm f(-r))/2$. R77.1--4 proves for that exact object
$$
 a_{\rm phys}(-r)=a_{\rm phys}(r),\qquad
 E(-r)=E(r),\qquad K_0(-r)=K_0(r).
 \tag{WPL.32}
$$
In particular $E$ is the actual radial average of the metric of the same infinite-primitive graph, and
$K_0=-(a_{\rm phys}\sqrt E)^{-1}
       \partial_r(a_{\rm phys}'/\sqrt E)$.
This conclusion is not inferred from nearly symmetric floating knots or a radial symmetry assumption on the repaired Codazzi state.

The exact germ-matching note, sections 1--2, supplies the necessary regularity at every common knot, including the waist: $a_{\rm phys}$ is $C^4$, $E$ is $C^3$, and $K_0$ is $C^2$ where $a_{\rm phys},E>0$. Thus the even $K_0$ is genuinely differentiable at zero; an even piecewise continuous function would not have sufficed.

The current compact metric is exactly
$E_\nu=E\exp(\nu h_{\rm met})$, with
$\operatorname{supp}h_{\rm met}\subset(.05,.18)$, and $a_{\rm phys}$ is unchanged, by polynomial Codazzi P, section 3. Hence it agrees with the same original metric on a neighbourhood of the waist. The whole real compact family has the same local parity and derivatives there. The metric bump $h_{\rm met}$ is unrelated to the density $h$ in (WPL.16).

With the already qualified positive waist branch $q_w=\sqrt{-K(0)}>0$, these exact facts yield
$$
 \beta_{\rm metric}(0)=\frac{a_{\rm phys}'(0)}{a_{\rm phys}(0)}=0,
 \qquad K_r(0)=0,\qquad
 q_r(0)=-\frac{K_r(0)}{2q_w}=0.
 \tag{WPL.33}
$$
Consequently, as full angular functions,
$$
 B_\sigma(0)=0,\qquad
 \mathbf S(0)=0,\qquad t(0)=0,\qquad b_t=0.
 \tag{WPL.34}
$$
This uses no parity assumption on the radial derivatives of $u,v$. It is independent of the numerical size of an old upper bound for $\mathbf S(0)$. The two primitive ranks and $\mathcal F_t$ in (WPL.31) vanish because their actual coefficient is zero.

The second normalizer is not zero in general. The complete strict formula is
$$
 \begin{aligned}
 \mathbf S_{\sigma,-\sigma}&=-\frac{\sigma B_\sigma}{2\eta q},\\
 O_\sigma&=-(B_\sigma)_\phi
   -\beta_{\rm metric}(r_\sigma)_\phi r_\sigma
   +c_\sigma(\mathbf S_{\sigma,-\sigma})_\phi
   -(\mathbf S_{\sigma,-\sigma})_r
   +\mathbf S_{\sigma,-\sigma}d_\phi,\\
 \mathbf Z_{\sigma,-\sigma}&=-\frac{\sigma O_\sigma}{2\eta q}.
 \end{aligned}
 \tag{WPL.35}
$$
Here $c_\sigma=d+\sigma\eta q$. Since (WPL.34) holds for the entire angular function, its angular derivatives vanish too. Thus $O_\sigma(0)=-(\mathbf S_{\sigma,-\sigma})_r(0)$, and differentiation of the full neighbourhood formula, before taking the waist value, gives
$$
 \boxed{\quad
 \mathbf Z_{\sigma,-\sigma}(0,\phi)
   =-\frac{(B_\sigma)_r(0,\phi)}{4\eta_w^2q_w^2}
   =\frac{q_{rr}(0)}{8\eta_w^2q_w^3}
      +\frac{\beta_{{\rm metric},r}(0)
                     [1+r_\sigma(0,\phi)^2]}
                   {4\eta_w^2q_w^2}.
 \quad}
 \tag{WPL.36}
$$
Indeed
$(B_\sigma)_r(0)=-q_{rr}(0)/(2q_w)
                 -\beta_{{\rm metric},r}(0)(1+r_\sigma(0)^2)$.
All terms involving $\eta_r$, $u_r$, $v_r$, or $q_r$ in this differentiation multiply an exactly zero $B_\sigma,\beta_{\rm metric}$, or $q_r$. No nonzero upper bound is subtracted to obtain (WPL.36). The full value $r_\sigma=u+\sigma q_wv$, including the mean of $v$, remains.

At this single endpoint,
$$
 \mathscr T_J(0)=Id+P_{J_s}\mathbf Z(0)I^2P_{J_s},\qquad
 T_{\rm ref}=Id+P_{J_s}M_{\mathbf Z_{+,-}(0)}I^2P_{J_s}R.
 \tag{WPL.37}
$$
In particular the $\mathbf S_r(0)$ contribution is retained through (WPL.36). These equations do not set $\mathbf S$ to zero on the strict interval, remove its interfaces, or alter any SWA source or jump bound.

## WPL8. The complete physical leading row and its strong difference

Define the exact waist second-order map
$$
 \mathcal V_w=
 U_{\mathcal H^{-1}}
   P_{J_s}M_{\mathbf Z_{+,-}(0)}I^2P_{J_s}R
 U_{\mathcal H},\qquad
 Q_a=P\Pi_a^+ .
 \tag{WPL.38}
$$
It has zero output mean, $\mathcal V_wh=0$, and
$\mathcal A_J=Id+\mathcal V_w$.
The projector $Q_a$ is the actual orthogonal projector onto the prescribed whole target $P\operatorname{Fix}(R_a)$.

Substitution into (WPL.26) proves
$$
 \boxed{\quad
 \frac{\mathfrak W_\partial}{2\kappa}
       =\left.Q_aT_i\right|_{X^{\rm fr}}
                     +\mathcal E_\partial^{\rm fr},
 \quad}
 \tag{WPL.39}
$$
with the complete error
$$
 \boxed{\quad
 \mathcal E_\partial^{\rm fr}
 =Q_a\mathcal V_w T_i
      -(h-1)\otimes\rho_i
      +Q_a(Id+\mathcal V_w)P_hE_i^{\rm fr}.
 \quad}
 \tag{WPL.40}
$$
For verification, expand
$Q_a(Id+\mathcal V_w)(Id-h\Pi)T_i$;
use $\mathcal V_wh=0$ and $Q_ah=h-1$.
This accounts for every term in (WPL.40), including the output-mean rank.

Every term in (WPL.40) maps
$$
 \mathcal E_\partial^{\rm fr}:
        X_{-4/3}^{\rm fr}\longrightarrow
                           P\operatorname{Fix}(R_a)\cap L^2 .
 \tag{WPL.41}
$$
The first term has two primitives, the second has the complete dual row (WPL.18), and the last uses the full WRA strong difference. That difference still contains the original coefficient finite complement, both primitive ranks, waist projection, PC/ST4 correction and every genuine strict source and jump. The zero value of the new endpoint coefficient $t$ does not remove any of those separate terms.

The first-coefficient mean of the actual normalized primitive row is therefore precisely $\nu_i$, and its constant model uses the same $\mu=-2\nu_i$ as (WPL.12). This identification is now justified by the actual endpoint metric. It does not itself prove a spectral gap, invert a reflected square, or replace the transported input projection.

For clarity, a complete symbolic bound can be written without evaluating any old target. Let $K_{H,s}$ and $K_{H^{-1},s}$ bound the true full-density maps in their indicated windows, let $Z_w\ge\|\mathbf Z_{+,-}(0)\|_\infty$, and put
$$
 \begin{aligned}
 \alpha_{J_s}
     &=\sup_{|j|\ge J_s}
              \frac{(1+16j^2)^{2/3}}{16j^2}
       =\frac{(1+16J_s^2)^{2/3}}{16J_s^2},\\
 \delta_w&=K_{H^{-1},0}\,Z_w\,\alpha_{J_s}\,K_{H,-4/3},\\
 K_{i,-}&=1+\tfrac14 W_{4/3}(c_i),\\
 K_{\mathcal A,0}
     &=K_{H^{-1},0}\,
                    \|\mathscr T_J(0)\|_0\,K_{H,0}.
 \end{aligned}
 \tag{WPL.42}
$$
The scalar $\alpha_{J_s}$ is the exact physical-frequency two-primitive norm with the original input cutoff. The multiplier bound for $Z_w$ is an ordinary $L^\infty$ bound after the two primitives, so no unlisted angular derivative of $\mathbf Z$ is required in this expression. The $1/4$ in $K_{i,-}$ is the original full nonmean primitive norm; no high input assumption about $T_ix$ is substituted for it.

Writing $C_i\ge\|E_i^{\rm fr}\|$ and
$R_i\ge\|\rho_i\|$, a whole bound for the normalized row is
$$
 C_\partial
   =\delta_wK_{i,-}
       +\|h-1\|_2R_i
       +K_{\mathcal A,0}(1+\|h\|_2)C_i .
 \tag{WPL.43}
$$
The terms are all positive complete norm majorants. Actual evaluation would require outward bounds for each displayed factor in its stated window. A potentially sharper direct same-row estimate may replace this whole bound only when proved for the same complete operator.

The exact identity (WPL.36) permits a new endpoint bound using $q_{rr}(0)$, $\beta_{{\rm metric},r}(0)$, the positive $\eta_w,q_w$, and the complete $r_+(0)$ value. It does not require new radial derivatives of $u,v$. A complete old bound for the same $\mathbf Z(0)$, if used instead, remains an independent whole candidate. There is no division by an upper bound or cancellation of separate upper bounds.

## WPL9. The next actual defect is a projected physical row

Equations (WPL.39)--(WPL.40) supply a specified source and a prescribed target:
$$
 \left.Q_aT_i\right|_{X^{\rm fr}}:
       X_s^{\rm fr}\longrightarrow
                                  P\operatorname{Fix}(R_a).
 \tag{WPL.44}
$$
The source is not identified with the target. In particular one cannot apply the old same-Fourier-space high compression to this map merely because the full-circle $T_i^{-1}$ exists. Any input intertwiner must carry the entire $P_{97}^{\mathcal S}$ and its finite complement, and any constant-coefficient spectral model must retain the complete change of leading row and the corresponding strong difference.

There is also an exact way to assess the state contribution before multiplying separate coordinate upper bounds. Write the WRA same-tuple state as
$Y_A=Y_{W,J}+E_{*,W}$, with both physical mean slots retained, and let
$$
 Q_{R,y}y=\frac12(y+ERy),\qquad
 Q_R(y,z)=\left(Q_{R,y}y,\frac12(z-Ez)\right).
$$
The actual homogeneous state obeys $Q_RY_A=Y_A$. Let $\pi_y$ select its nonmean density vector. Then
$$
 \begin{aligned}
 \frac{\mathfrak W_\partial}{2\kappa}
   &=\frac12U_{\mathcal H^{-1}}e^TQ_{R,y}
                              \pi_yY_{W,J}N_i
      +\mathcal E_{\partial,{\rm state}},\\
 \mathcal E_{\partial,{\rm state}}
   &=\frac12U_{\mathcal H^{-1}}e^TQ_{R,y}
                                  \pi_yE_{*,W}N_i .
 \end{aligned}
 \tag{WPL.45}
$$
The normalizer and its inverse have cancelled adjacently in this physical readout. They are not removed from the interior differential equation or from the trial defining $E_{*,W}$. A comparison trial need not have been reflected in advance: the exact $Q_R$ in (WPL.45) provides its reflected part.

The complete physical-row defect is (WPL.40), or equivalently the projected trial in (WPL.45) minus the same leading row in (WPL.44), plus the displayed whole state difference. One must not add these two representations and charge the same state twice.

For instance, the complete old state upper bound yields
$$
 \|\mathcal E_{\partial,{\rm state}}\|
 \le \frac{K_{H^{-1},0}}{\sqrt2}
             C_{*,W}\|N_i\|_{X_{-4/3}^{\rm fr}
                                      \to\mathcal H_{\rm nat}^{-4/3}}.
 \tag{WPL.46}
$$
This is only a safe whole upper consequence. The large saved SWA state upper does not become small through this identity. For a useful new estimate, the object to bound is the actual projected row in (WPL.45): the original cut discrepancy, complete ordinary Duhamel source, all 3070 interface impulses, PC/ST4 correction and waist endpoint term must first be assembled with their true signs and common output row, as in WRA.29--31. No source term or radial integral may be removed merely because a coordinate factor cancels. Interface impulses carry no invented radial length.

The input $N_i$ in (WPL.45) is exactly the original same-column ordered common input. If it is removed by changing to the natural stable coordinate, WRA/NIF's complete right identity must be applied to both the entire leading row and the entire error. Keeping $Q_aT_i$ while cancelling that factor only from its error would change the operator.

The physical row is $2\kappa$ times (WPL.39). The separate raw mean equation, even-mean and amplitude conditions, metric-parameter column, independent radial head/source and second reference input keep their original definitions. In the reflected homogeneous subclass the raw $h_1$ mean is automatically zero, but this is not a count of two independent stored means or a solution of the remaining matching system.

All identities are first proved on the original smooth core. The strong differences then have precisely the trace extensions stated above. No rough bulk Poisson regularity is inferred from a boundary coordinate inverse. At a frozen parameter the row and input changes are fixed linear maps; a genuinely parameter-dependent nonlinear chart must retain the triangular parameter column described in RNS.

The new conclusion is the complete coefficient reflection, its true paired range compatibility, the exact zero first waist normalizer, and the fully specified physical row (WPL.39)--(WPL.45). It leaves a concrete row defect and the actual finite/mean matching problem to be bounded and inverted. It does not assert a complete physical incoming inverse, a same-space principal restriction, a numerical smallness test, a finite Schur determinant, or a nonlinear solution.
