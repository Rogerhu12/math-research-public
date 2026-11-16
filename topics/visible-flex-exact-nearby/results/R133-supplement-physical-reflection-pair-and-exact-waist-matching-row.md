# R133 supplement: physical reflection, the paired waist receivers, and the exact waist matching row

This note identifies the physical reflection constraint on the **pair** of complete waist receivers and writes the actual linearized waist condition in those receivers. It also proves a concrete obstruction to restricting the already certified full-circle scalar principal inverses to the same reflected input space as endomorphisms. The obstruction does not invalidate their full-circle inverses.

The input domain is the corrected NIF inverse-image domain. No new numerical enclosure, saved target, Airy calculation, flow, or primitive is evaluated. The physical paired range, the positive regular graph, and the target of a single scalar principal operator are distinguished throughout.

## WPR1. Original objects and three different reflection realizations

All circles have physical period $\pi/2$, normalized measure, frequencies $4j$, and
$$
 I=\partial_\phi^{-1}(1-\Pi),\qquad P=1-\Pi,\qquad
 \Lambda_j=(1+16j^2)^{1/2}.
 \tag{WPR.1}
$$
$\Pi$ is the full mean projection. Its action on a two-component vector is componentwise.

The following immutable texts are the primary identities used here. The original WY and IC bodies are cited for their unchanged receiver and primitive formulas; the later MS common-input order, and the corrected SE8/NIF domain, govern the interpretation.

| Primary and precise use | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| Moving scalarization N.3--7: the actual odd/even physical system and mean | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| Strict density cut N.4, N.8--11: physical state, two means, ordered normalizers | da51581b623d4167ae9278af6892bc9a0591fb3f | 13892 | 4d44bbe7082d4ee967ebf9d02284b3510624624ab98adb087b8d0499eb030376 |
| SF.14--19: the complete first-symbol matrices and fixed-cutoff realization | 0f93e925d354133675b84ffeaa959a0b58d339a0 | 35289 | add091118ef1af71bc8c4be275742d4124a076d6cf2ebaf00d35c66f8348f2b4 |
| Original WY.3--5, WY.11--14: complete primitive-plus-mean receivers | 847a7dd335158482811561c2ed5e1aa7175e8797 | 30764 | ebf8713508a11ef96decc5691056ea6eaa15d967d08b3a8af4b20c4284f6d1b3 |
| MS.2--4, MS.13--19: one incoming normalization and the full outgoing sign factor | 10fdaddc0114e25ad349f1f411e80baf4f98fe26 | 19522 | 44038eaed377863961aad7f0c74caa2bf498d6a689812f05933111777c191161 |
| Original IC.13--17: the exact full-density primitive and both rank terms | bd4ed3ab5d72a10021df281542d080ef2f67fb0e | 17274 | 4164e4a7a10db651654cf63b7ecf7772fc1ba2cb966da4f9347711156301ddee |
| NIF.5--13 and NIF9: fixed phase, true inverse-image domain, and corrected SE8 | d606faa1ffd30c34d3487985a57dbc62a18890bc | 32942 | 8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640 |
| Corrected SE8: typed natural stable factorization | 2f554e31e051a3e27295e514036d1289e9281f75 | 21356 | 93266089706d71dfa9ee6e5fd48be9cd796354a25b5801f0386d225e4fea2572 |
| Physical waist/amplitude A.17--26: actual waist equation and independent parameter/mean rows | 511c9ca83972003796c4c4fa456236f32095e3e3 | 13237 | 825113583ae91127e6b99fc839a7b5fd32bdaa660befcce5c7d5728c253f0538 |
| SEI actual execution, run43773319871/1: certified signs of the two actual principal coefficients | e1532b816ea344ee65e52a503279376a0c449299 | 46192 | b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29 |

The selected real parameter, original fixed intrinsic parameter, and all physical reference data are those in NIF.1. Statements below concerning a parameter family use the original reflected physical realization at each qualified parameter. A selected KAM factorization is invoked only at its already certified selected parameter.

There are three distinct objects:

1. On the raw moving waist circle, $R f(\phi)=f(-\phi)$ is physical reflection. The actual linearized class in N.3 is $h_1,u$ odd and $h_2,v$ even.
2. On the original root circle, $R_*$ defines the natural reflected high input space $\mathcal H_{\rm nat}^s=P_{97}\operatorname{Fix}(R_*)$, with the original real form when required.
3. In the selected angle, the fixed full density map $\mathcal S_*$ and the constant sign phase $D_+$ transport that root space. They do not identify root reflection with raw waist reflection.

Specifically, NIF gives
$$
 D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_-,
 \qquad
 X_s^{\rm fr}=\mathcal S_*D_+\mathcal H_{\rm nat}^s,
 \qquad
 N_{i,\delta}^{\rm fr}=\Lambda_{+,\delta}^{-1}T_{F,\delta}^{-1}
                                      \mathcal S_*^{-1}.
 \tag{WPR.2}
$$
Here $\Lambda_{+,\delta}=a_\delta D_+$ on the nonmean high carrier, with $a_\delta>0$. The natural projector transported by $\mathcal S_*D_+$ is distinct from the transported full signed high projector. The complementary parity class in that carrier is infinite-dimensional. Neither $D_+$ nor $\Lambda_+$ alone preserves the even root class. The root normalizer preserves it by the two reflection sign changes proved in NIF2.

All other physical inputs, including the independent means, low/head columns, radial inputs and any separately declared second reference input, keep their original domains. Formula (WPR.2) does not normalize their means by a nonzero Fourier frequency.

## WPR2. Exact physical reflection in primitive-plus-mean coordinates

At a qualified strict endpoint, including the actual waist, retain the original radial quantities
$$
 q=\sqrt{-K}>0,\qquad n_g=\frac{a_{\rm phys}^2}{m^2}>0,\qquad
 T(q)=\frac1{\sqrt{2q}}
       \begin{pmatrix}1&q\\1&-q\end{pmatrix}.
$$
The complete density coordinates are
$$
 w=n_gT(q)h,\qquad y=Iw,\qquad z=\Pi w.
 \tag{WPR.3}
$$
There is no new integration constant. Both entries of $z$ are stored.

Let
$$
 J_h=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
 \qquad E=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
Direct multiplication and the exact primitive identity $RI=-IR$ give
$$
 T(q)J_hT(q)^{-1}=-E,\qquad
 Rh=J_hh
 \ \Longleftrightarrow\
 Rw=-Ew
 \ \Longleftrightarrow\
 \left\{
 \begin{aligned}
 Ry&=Ey,\\
 z&=-Ez .
 \end{aligned}\right.
 \tag{WPR.4}
$$
The last equivalence uses $w=\partial_\phi y+z$ and $\Pi y=0$. Thus the two stored mean entries satisfy $z_-=-z_+$ on this particular reflection subclass. This is the same explicit relation recorded after N.7 of the strict-cut result. It is not a deletion of either mean slot, or a replacement of the independent physical mean equations in the complete problem.

The original reflected realization is a condition on the physical field $h$. In particular, the genuine homogeneous Ai/positive-graph columns with compatible natural reflected input satisfy it by their original realization. It is not inferred from an inverse of a scalar incoming branch, or from calling an arbitrary full-circle Ai input “physical.”

## WPR3. The actual ordered waist normalizer preserves the paired reflection

Use bold letters for the moving two-by-two coefficients to distinguish them from the selected density chart $\mathcal S_*$. With the original radial $\beta,\eta,q$, put
$$
 r_\sigma=u+\sigma qv,\qquad c_\sigma=d+\sigma\eta q,\qquad
 d=-\beta I(u^2+Kv^2),
$$
$$
 B_\sigma=-\frac{q_r}{2q}-\beta(1+r_\sigma^2),\qquad
 \mathbf S_{\sigma,-\sigma}=-\frac{\sigma B_\sigma}{2\eta q},
 \tag{WPR.5}
$$
and give both matrices zero diagonal. The full second coefficient is
$$
 \begin{aligned}
 O_\sigma={}&-(B_\sigma)_\phi-\beta(r_\sigma)_\phi r_\sigma
       +c_\sigma(\mathbf S_{\sigma,-\sigma})_\phi
       -(\mathbf S_{\sigma,-\sigma})_r
       +\mathbf S_{\sigma,-\sigma}d_\phi,\\
 \mathbf Z_{\sigma,-\sigma}={}&-\frac{\sigma O_\sigma}{2\eta q}.
 \end{aligned}
 \tag{WPR.6}
$$
These are the exact N.8--10/SF coefficients. In particular the radial derivative and the complete physical mean entering $\eta$ have not been removed.

The reference parities imply
$$
 Rr_\sigma=-r_{-\sigma},\quad Rc_\sigma=-c_{-\sigma},
 \quad RB_\sigma=B_{-\sigma},\quad Rd=-d.
$$
Using $R\partial_\phi=-\partial_\phi R$ in every term of (WPR.6) proves
$$
 R\mathbf S R=-E\mathbf S E,\qquad
 RO_\sigma=-O_{-\sigma},\qquad
 R\mathbf ZR=E\mathbf ZE .
 \tag{WPR.7}
$$
Here reflection of a multiplication matrix means reflection of each entry. For example the derivative of the reflected $\mathbf S_\sigma$ has the opposite extra sign from the reflected $\mathbf S_\sigma$ itself; the $c_\sigma\mathbf S_{\sigma,\phi}$ term therefore has exactly the sign in (WPR.7).

Let $P_{J_s}$ be the original strict normalizer projection, with its already selected $J_s=268435456$. This is distinct from the root cutoff 1024 and the input cutoff 97. The ordered realization is
$$
 \mathscr T_{J_s}
   =(1+P_{J_s}M_{\mathbf S}IP_{J_s})
      (1+P_{J_s}M_{\mathbf Z}I^2P_{J_s}).
 \tag{WPR.8}
$$
Reflection and the swap $E$ commute with each $P_{J_s}$. The minus signs in $R\mathbf S R$ and $RIR$ cancel, and $RI^2R=I^2$. Hence
$$
 [\mathscr T_{J_s},ER]=0,\qquad
 [\mathscr T_{J_s}^{-1},ER]=0
 \tag{WPR.9}
$$
where the latter uses the actually proved waist inverse of WTA. There is no interchange of the two factors or of their inverses. Both factors are identity on the full finite head; their high projections also make the nonmean subspace invariant and the mean block exactly the identity. All finite corrections and mean rows of the transformed equation remain present.

## WPR4. The complete physical pair is a graph with a necessary mean rank

Define the actual normalized primitive and its complete encoding by
$$
 \widehat y=\mathscr T_{J_s}^{-1}y,\qquad
 f_\sigma=\widehat y_\sigma+z_\sigma .
 \tag{WPR.10}
$$
This is precisely the WY.5 encoding after the actual waist matrix inverse. It does not identify a primitive with the raw curvature field.

Combining (WPR.4) and (WPR.9), and retaining the two mean entries, gives
$$
 \boxed{\quad f_-=(R-2\Pi)f_+ .\quad}
 \tag{WPR.11}
$$
Indeed $\widehat y_-=R\widehat y_+$, while $z_-=-z_+$. If $K_0=R-2\Pi$, then
$$
 K_0^2=1,\qquad \Pi K_0=-\Pi,\qquad
 \|K_0f\|_{H^s}=\|f\|_{H^s}.
 \tag{WPR.12}
$$
The last identity follows from its action as $-1$ on the mean and as reflection on the nonmean Fourier modes.

There is also an exact state-level converse. Given a complete scalar $g$, set $f=(g,K_0g)$ and reconstruct
$$
 y=\mathscr T_{J_s}P f,\qquad z=\Pi f,\qquad
 w=\partial_\phi y+z,\qquad h=T(q)^{-1}n_g^{-1}w.
 \tag{WPR.13}
$$
The resulting state has $Rh=J_hh$. These statements extend on the bounded distributional windows of the actual coordinate maps.

This converse describes all reflected Cauchy states at this endpoint. It does **not** assert that every such state extends to the original positive regular given-head graph, satisfies the waist boundary condition, or lies in the image of the actual incoming map. Those are additional equations on the state.

At the selected parameter, let $\mathcal A_\sigma$ be the exact raw-angle encoded branch map of MS.2, and use one common input, with its corrected restriction (WPR.2). Thus
$$
 \mathcal I_{\rm com}
       =U_{\mathcal H^{-1}}\mathcal A_+N_i,\qquad
 \mathcal O_{\rm com}
       =U_{\mathcal H^{-1}}\mathcal A_-N_i .
 \tag{WPR.14}
$$
Full density pullbacks are used: $U_\psi f=\psi'(f\circ\psi)$ and $\Pi U_\psi=\Pi$. Formula (WPR.11) therefore becomes, on the qualified physical input,
$$
 \boxed{\quad
 \mathcal O_{\rm com}=K_{\mathcal H}\mathcal I_{\rm com},\qquad
 K_{\mathcal H}=U_{\mathcal H^{-1}}(R-2\Pi)U_{\mathcal H}.
 \quad}
 \tag{WPR.15}
$$
The full mean term is explicitly
$$
 K_{\mathcal H}
   =U_{\mathcal H^{-1}}RU_{\mathcal H}
         -2\,(U_{\mathcal H^{-1}}1)\otimes\Pi .
 \tag{WPR.16}
$$
Thus $K_{\mathcal H}^2=1$ and $\Pi K_{\mathcal H}=-\Pi$. Its bounds may use the already paid factors
$\|U_{\mathcal H^{-1}}\|_{H^s\to H^s}\|U_{\mathcal H}\|_{H^s\to H^s}$.
No new numerical product is formed here. It need not be unitary in the selected measure, and $U_{\mathcal H^{-1}}1$ is not replaced by 1.

In the selected KAM factorization, MS.16 gives the exact same pair as
$$
 \mathcal I_{\rm com}=\mathcal B_+,\qquad
 \mathcal O_{\rm com}=U_{R_\Omega}\mathcal B_-Z^{\mathcal S_*}.
$$
Consequently
$$
 \left.U_{R_\Omega}\mathcal B_-Z^{\mathcal S_*}\right|_{X_s^{\rm fr}}
    =\left.K_{\mathcal H}\mathcal B_+\right|_{X_s^{\rm fr}}.
 \tag{WPR.17}
$$
The rotation, the full infinite-dimensional Maslov sign operator, its true order and its mean extension are retained. This is a relation between the two restrictions, not an identity on the auxiliary full circle. The pair relation (WPR.11) is physical and remains meaningful for the original family; the selected factorization in (WPR.17) is not thereby extended as a KAM family.

## WPR5. The actual waist equation in the complete pair

At the actual waist set
$$
 \kappa_1=\frac{\sqrt{q_0/2}}{n_g(0)},\qquad e^T=(1,1).
$$
The raw reconstruction (WPR.13), for any complete pair $f$, gives
$$
 h_1(0)=\kappa_1 e^T
        \left[\partial_\phi\mathscr T_{J_s}P f+\Pi f\right].
 \tag{WPR.18}
$$
Here $\partial_\phi\mathscr T_{J_s}$ means the derivative of the full output; it includes the angular derivatives of its coefficients. It is not commuted through the normalizer.

The exact equivalent primitive and mean rows are
$$
 \boxed{\quad
 Ih_1(0)=\kappa_1 e^T\mathscr T_{J_s}P f,\qquad
 \Pi h_1(0)=\kappa_1 e^T\Pi f .
 \quad}
 \tag{WPR.19}
$$
In particular $h_1(0)=0$ if and only if both rows vanish. The first row is a meanzero primitive of the raw equation, not the raw value $h_1(0)$. This equivalence is valid for the same raw distributional state window used in WY.3--5.

The actual physical waist condition is $u(0,\phi)=0$, so (WPR.19) is its complete homogeneous linearization. The original physical amplitude row, outer regular relation, mean equations and the metric-parameter scalar of A.17--26 remain separate. On the reflection subclass the mean in (WPR.19) vanishes by $z_-=-z_+$; recording that fact does not discard the independent even physical mean or any original outer/height/amplitude equation.

In common selected-angle coordinates the first row is the actual operator
$$
 \mathscr W_{\rm waist}^{\rm ne}
  =\kappa_1e^T\mathscr T_{J_s}P
       \operatorname{diag}(U_{\mathcal H},U_{\mathcal H})
        \binom{\mathcal I_{\rm com}}{\mathcal O_{\rm com}},
 \tag{WPR.20}
$$
and its companion mean row is obtained by replacing $\mathscr T_{J_s}P$ by $\Pi$. There is no exchange of $P$ with $U_{\mathcal H}$. The physical mean effect of $U_{\mathcal H}1=\mathcal H'$ stays in this formula.

For a reflected actual column one can insert (WPR.15) in the same order:
$$
 \mathscr W_{\rm waist}^{\rm ne}
   =\kappa_1e^T\mathscr T_{J_s}P
      \binom{U_{\mathcal H}}{U_{\mathcal H}K_{\mathcal H}}
            \mathcal I_{\rm com}.
 \tag{WPR.21}
$$
The output is in the original even meanzero primitive waist space, because the raw $h_1$ is odd. The output includes its true low and high Fourier modes. This is a concrete physical boundary map, rather than an endomorphism obtained by naming an unknown incoming image as its target.

Equations (WPR.20)--(WPR.21) provide an exact row in a subsequent complete boundary square. They do not prove that this row, that square, or a single branch is onto. They do not remove any separately prescribed source or rest column.

## WPR6. A nonzero principal mean prevents the proposed same-space restriction

The following lemma concerns a genuine obstruction, not an untested numerical gate.

Let $S=U_\psi$ be an actual full density isomorphism on the two windows used below, let $\chi=\psi^{-1}$, and let
$$
 X=S D_+P_{97}\operatorname{Fix}(R_*).
$$
Assume $c$ is real, has nonzero mean $\nu=\langle c\rangle$, and has the regularity needed for the exact IC.16 rank rows to act from $H^{-4/3}$ to $L^2$. For example the smooth coefficients and lifts in the already qualified selected construction suffice. Let
$$
 A=1+M_cI+E_1,\qquad
 E_1:H^{-4/3}\longrightarrow L^2.
 \tag{WPR.22}
$$
Here $E_1$ must be the complete strong remainder of the particular operator to which the lemma is applied. An unbounded or unpaid retained term cannot be silently included in this hypothesis.

IC.16, with both mean ranks retained, gives
$$
 S^{-1}AS=1+M_bI+F,\qquad b=U_\chi c,\qquad \langle b\rangle=\nu,
$$
$$
 F=b\otimes p_\chi-(bp_\chi)\otimes1+S^{-1}E_1S,
 \qquad p_\chi=\chi-\mathrm{id}-\langle\chi-\mathrm{id}\rangle .
 \tag{WPR.23}
$$
Thus $F:H^{-4/3}\to L^2$ is bounded. The first rank has the full $H^{4/3}$ dual row $p_\chi$; the second has the actual constant row.

Suppose that $A$ preserved $X$. For every integer $n\ge97$ put
$$
 f_n=e^{i4n\phi}+e^{-i4n\phi},\qquad k=4n,\qquad
 A^\natural=D_+^{-1}P_{97}S^{-1}ASD_+ .
$$
Then $A^\natural f_n$ would be even. The high projection does not alter either of its coefficients at $n$ or $-n$. With $\widehat b_j$ denoting the Fourier coefficient at physical frequency $4j$, the two corresponding coefficients of $1+M_bI$ after phase conjugation are
$$
 \begin{aligned}
 n:&\quad 1+\frac{\nu}{ik}-\frac{\widehat b_{2n}}{k},\\
 -n:&\quad 1-\frac{\nu}{ik}-\frac{\widehat b_{-2n}}{k}.
 \end{aligned}
 \tag{WPR.24}
$$
The relative phase $D_{+,-n}/D_{+,n}=i$ is used here; it is not replaced by a common real scalar.

Consequently their difference, including the complete $F$, is
$$
 \Delta_n=\frac{2\nu}{ik}
      +\frac{\widehat b_{-2n}-\widehat b_{2n}}{k}+r_n,
 \qquad |r_n|\le2\|F\|_{H^{-4/3}\to L^2}\Lambda_n^{-4/3}.
 \tag{WPR.25}
$$
The remainder bound follows from
$\|f_n\|_{H^{-4/3}}=\sqrt2\Lambda_n^{-4/3}$ and the norm $\sqrt2$ of the difference of the two Fourier coefficient rows. Since $b\in L^2$, its Fourier coefficients tend to zero. Also $k\Lambda_n^{-4/3}\to0$. Therefore
$$
 k\Delta_n\longrightarrow-2i\nu\ne0 .
 \tag{WPR.26}
$$
For sufficiently large $n$ the output is not even. This contradicts preservation of $X$ and proves
$$
 \boxed{\quad A(X)\not\subset X.\quad}
 \tag{WPR.27}
$$

The proof only uses high test frequencies. Changing only the original finitely many Fourier columns cannot remove the obstruction, nor can an additional finite-rank map in the same complete strong class of (WPR.22). It does not assert that the actual physical target of $A$ is $X$.

For the scalar principal operators $T_i=1+M_{c_i}I$ and $T_o=1+M_{c_o}I$ the hypothesis holds with $E_1=0$. The complete SEI execution listed in WPR1 certifies $c_i>0$ and $c_o<0$ in the selected real chart. In particular their means are nonzero. Thus their existing full-circle inverses cannot be reinterpreted as endomorphism inverses $X_s^{\rm fr}\to X_s^{\rm fr}$. The full-circle inverse estimates and all previous successful scalar receipts remain unchanged.

The same distinction already occurs for the isolated real Cayley factor with $\mu\ne0$:
$$
 C_\mu=(1+\mu I/2)(1-\mu I/2)^{-1}
   =1+\mu I+\frac{\mu^2}{2}I^2(1-\mu I/2)^{-1}.
 \tag{WPR.28}
$$
The last term is strong from $H^{-4/3}$ to $L^2$, and its mean is zero. The factor $(1-\mu I/2)^{-1}$ is bounded on every fixed circle Sobolev window because $\mu$ is real. Applying the lemma proves the same nonpreservation for this factor alone. It is not a statement about an arbitrarily rotated or sign-conjugated complete return operator: those factors must retain their exact order and their actual physical source and target.

## WPR7. Actual range versus an auxiliary endomorphism

If a full-circle operator $A$ is invertible, its restriction is automatically an isomorphism $X\to AX$. That tautology supplies no identification of $AX$ with a separately defined physical boundary target. For instance the transported involution on the full high carrier is
$$
 J_X=S D_+R_*D_+^{-1}S^{-1},
$$
and $A J_X A^{-1}$ characterizes the transported reflection on $AX$ only after the ambient inverse is available. Neither this notation nor a definition of $AX$ proves physical surjectivity.

For the actual waist states, (WPR.11) and (WPR.15) provide a stronger, independent statement: the two receivers obey a reflection graph determined directly by physical state reconstruction. The actual waist condition then supplies (WPR.20), with its own original target. This separates:

| Object | What has been proved here |
|---|---|
| Physical reflected endpoint states | Exact complete pair graph (WPR.11), including the mean rank |
| The actual regular given-head subspace of those states | Its existing Poisson-graph realization is retained; endpoint reflection alone does not fill it |
| Full-circle $T_i^{-1},T_o^{-1}$ and Cayley results | Existing results retained on their original full-circle spaces |
| Same-space restriction to $X_s^{\rm fr}$ | The naive single principal restriction is ruled out by (WPR.27) |
| Actual linearized waist condition | Exact paired primitive and mean rows (WPR.19)--(WPR.21) |
| Complete physical incoming square and finite/mean Schur system | Still require their actual domain/range and full retained rows |

In particular, no count of two sign labels turns an infinite sign operator or an infinite parity complement into a finite border. No mean-identity replacement of a full density map is made. If a later realization uses $U_\psi P+\Pi$ instead, the exact difference $(\psi'-1)\Pi$ remains an additional explicitly typed rank map.

## WPR8. Consequence for the next complete error calculation

A future estimate of the complete physical boundary row must start with (WPR.20), keep the outgoing factor in the MS.16 order, and retain the primitive and mean reconstruction (WPR.19). It may exploit exact correlation between the two physical branches before taking a norm. It may not independently enlarge a Fourier head until a formally small tail appears and call the unchanged complete boundary problem solved.

The already paid partial strong bounds are not a norm of every retained contribution. The common stable right-coordinate factor from R97/RNE/NIF can be cancelled only when both maps are exactly the same given-head Poisson realization with the same independent ports. Its cancellation changes the leading map on that side as well. It does not erase the inhomogeneous trial correction, a true independent radial input, a second prescribed reference datum, or any independent mean row.

The next separate accounting statement must therefore identify that exact common right factor, list the retained maps on the correct $X_s^{\rm fr}$ domain, and form the complete error of the concrete row (WPR.20) before applying any $T_i^{-1}$ high-tail test. This note supplies the actual row and the obstruction that the accounting must respect; it does not assign a new value to the complete incoming error or to a finite inverse.
