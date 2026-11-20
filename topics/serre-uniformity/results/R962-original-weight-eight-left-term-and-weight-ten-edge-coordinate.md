# R962 — The actual weight-eight left term and the weight-ten Cartier edge coordinate

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: proved.** In the original \(r=8\) row, the nontrivial-deck part of the left term in R956's Bol-cokernel sequence has invertible double-\(T_5\). Its actual zero-primary localization is therefore zero. The original Cartier edge on that localization is an isomorphism onto the single named weight-ten CM line. This also gives a specified two-Fourier-coefficient formula for the remaining scalar. Its nonvanishing is not proved.

The complete left space and its actual Hecke transport are computed here; they are not discarded using the dimension of the right space. No mathematical script or new prime scan has been executed.

## 1. The complete weight-eight space on the original tame curve

Keep R918/R920/R942's original \(H_6\), its single width-six cusp, its three elliptic points of order three, and its once-fixed determinant and deck transports. Write
\[
v=V_4^\dagger,\qquad e_4=E_4,\qquad
L=e_4v,\quad J=v^2,\quad E=e_4^2.
\tag{962.1}
\]
In an expansion these mean the same original \(Q=e^{2\pi i\tau'/6}\) as in R956. They may equivalently be pulled back by \(\tau'=6\tau\), as in R942; no Fourier index is rescaled inside an equation.

We have the full-space identity
\[
\boxed{M_8(H_6)=\langle E,L,J\rangle.}
\tag{962.2}
\]
Here is a divisor proof, valid on every residual fiber of characteristic greater than three. R918 gives the exact divisor of \(v\): it has fine order one at each of the three order-three points and order one at the cusp, and no further zeros. A regular weight-eight form has fine order at least two at each of those elliptic points, since its stabilizer character is the square of the weight-four character. Thus division by \(v^2\) gives a rational function with no finite pole on the coarse \(\mathbf P^1_u\), and with a pole of order at most two at its single cusp. Conversely any such function times \(v^2\) is regular. The unchanged identity
\[
u=\frac{E_4}{4s\,v},\qquad s^2=-3,
\tag{962.3}
\]
identifies that function space with \(\langle1,u,u^2\rangle\). This proves (962.2).

The same proof is integral away from six. Alternatively, on the fine full-six curve the weight-eight line has positive degree and has \(H^1=0\), so integral base change holds; the actual tame invariants use only unit averaging denominators. The coefficient matrix of \(E,L,J\) at \(Q^0,Q^1,Q^2\) is triangular with diagonal one. Hence these sections form the whole integral lattice, not a sublattice of unspecified index.

For the actual transported deck action, \(e_4\) is invariant and \(v\) has character \(\zeta\). Therefore
\[
M_8^{\delta=1}=\kappa E,\qquad
M_8^{\delta=\zeta}=\kappa L,\qquad
M_8^{\delta=\zeta^2}=\kappa J.
\tag{962.4}
\]
The two nontrivial lines are cuspidal, and
\[
S_8(H_6)=\kappa L\oplus\kappa J.
\tag{962.5}
\]
No pre-transport direction of \(u\) is substituted for its actual ratio (962.3).

## 2. Two genuine Hecke arrows and their double-step unit

Use the normalized operator \(T_5\) of R942(942.5–7). Its six cosets carry the original graph subgroup to its coefficient-conjugate graph subgroup, and a second application returns to the original one. The proof of this statement uses the groups and cosets and is independent of the weight; it therefore applies to the whole space (962.2).

Keep an overbar on every form in the conjugate marking, with \(s\mapsto-s\) and \(Q\) fixed. R942's genuine target-character argument gives
\[
T_5L\in\kappa\bar J,\qquad
T_5J\in\kappa\bar L.
\tag{962.6}
\]
It is used after full-space stability has been established, rather than to infer stability from Fourier supports.

Only already established expansions are needed. R942(942.11), retaining the original oldform phase, gives
\[
v=Q+8sQ^4+20Q^7+0Q^{10}+O(Q^{13}),\qquad
e_4=1+240Q^6+O(Q^{12}).
\tag{962.7}
\]
Their products give, by the displayed two terms,
\[
[Q^{10}]L=240\cdot8s=1920s,\qquad
[Q^5]J=2\cdot8s=16s.
\tag{962.8}
\]
The normalized formula is
\[
T_5f=\sum_m\bigl(a_{5m}+5^7a_{m/5}\bigr)Q^m
\quad(f\text{ of weight }8).
\tag{962.9}
\]
Since \([Q^2]\bar J=[Q]\bar L=1\), (962.6–9) prove the exact arrows
\[
\boxed{T_5L=1920s\,\bar J,\qquad T_5J=16s\,\bar L.}
\tag{962.10}
\]
Coefficient conjugation supplies the reverse arrows:
\[
T_5\bar J=-16sL,\qquad T_5\bar L=-1920sJ.
\tag{962.11}
\]
In particular the returning operator \(U_5=T_5^2\) satisfies
\[
\boxed{\left.U_5\right|_{M_8^{\delta\ne1}}
=92160\,I,\qquad 92160=2^{11}3^2\cdot5.}
\tag{962.12}
\]
It is invertible at every prime \(p\ge41\). The invariant Eisenstein line \(\kappa E\) is not asserted to have this eigenvalue; it does not belong to the original two nontrivial deck summands.

## 3. The Hecke action on the left of the actual Bol complex

Now assume the original \(r=8\) row:
\[
p\ge41,\qquad p\equiv5\pmod{12},\qquad k=p-7.
\tag{962.13}
\]
For the Serre application retain \(p\equiv2,5\pmod9\) as before. Let
\[
\mathscr E_{\rm Bol}=\operatorname{Sym}^{7}\mathscr H\otimes F_X^*\omega
\]
be exactly R956's connection, with its compact-support logarithmic extension. The absolute-Frobenius convention in R956 gives the exact sequence
\[
0\longrightarrow H^1(\omega^{-6}(-C))
\longrightarrow\mathcal Q_{\rm Bol}
\xrightarrow{\ \mathscr K_8\ }S_{10}
\longrightarrow0,
\qquad
\mathcal Q_{\rm Bol}
=\bigl(\operatorname{coker}(\mathscr D_8:S_{p-7}\to S_{p+9})\bigr)_{\rm Fr}.
\tag{962.14}
\]
The scalar action on the middle term is \(c[Y]=[c^pY]\). Its left term is Serre-dual to the full \(M_8\), with a Hecke action that must be determined from this connection.

We compute it for any original degree-\(\ell\) prime-to-\(6p\) arrow. At its target use the frame \(\rho'\) with \(\varphi^*\rho'=\rho\). The Hasse coefficients agree, while the Gauss–Manin alternating pairing is multiplied by \(\ell\). The original horizontal vectors therefore satisfy
\[
\varphi^*\sigma_{\rho'}=\ell\sigma_\rho.
\tag{962.15}
\]
For example, this follows by pairing with \(\rho\), using
\(\langle\rho,\sigma_\rho\rangle=A\); equality on the ordinary locus extends globally. Thus the horizontal generator of the Bol bundle has pullback
\[
\varphi^*(\sigma_{\rho'}^{r-1}\otimes\rho'^p)
=\ell^{r-1}\sigma_\rho^{r-1}\otimes\rho^p.
\tag{962.16}
\]
After its coefficient \(p\)th root the factor is still \(\ell^{r-1}\).

Let \(S_\ell\) denote the unnormalized sum of the Hodge-line pullbacks on \(\omega^{2-r}(-C)\), with trace on cohomology and with the actual target marking retained. Consequently the actual left operator is
\[
T_{\ell,\rm left}=\ell^{r-1}S_\ell.
\tag{962.17}
\]
The Serre adjoint of this raw Hodge correspondence is
\[
S_\ell^\vee=\ell^{2-r}T_{\ell,M_r}^{\rm tr}.
\tag{962.18}
\]
Here \({\rm tr}\) records the reverse marked correspondence and transpose under Serre duality. To check the normalization, Kodaira–Spencer gives
\(K_{\rho,\rm source}=\ell K_{\rho',\rm target}\). The reverse isogeny uses the dual frame \(\rho/\ell\); its weight-\(r\) evaluation contributes \(\ell^r\), and the normalized modular \(T_\ell\) includes \(1/\ell\). Combining these factors with the Serre pairing gives exactly \(\ell^{2-r}\) for the raw sum. Equivalently the raw sum is \(\ell T_{2-r}\) and the Serre adjoint of \(T_{2-r}\) is \(\ell^{1-r}T_r^{\rm tr}\).

Equations (962.17–18) prove the actual, weight-independent comparison
\[
\boxed{T_{\ell,\rm left}^\vee=\ell\,T_{\ell,M_r}^{\rm tr}.}
\tag{962.19}
\]
There is an additional check directly on the complex: its bottom Hodge quotient carries \(\ell^rT_\ell\), whereas the top one-form carries the standard \(T_\ell\), since its Kodaira–Spencer factor supplies \(1/\ell\). Hence
\[
T_\ell\mathscr D_r=\ell^r\mathscr D_rT_\ell,
\tag{962.20}
\]
which is exactly the original Bol normalization, not an independently chosen left action.

All calculations are on the actual fine marked correspondence before taking tame invariants. Frobenius changes coefficient characters as in R956; it preserves the distinction between trivial and nontrivial deck characters. Serre duality reverses those two nontrivial characters and preserves their direct sum. For the returning degree-five double arrow, (962.19) gives
\[
(U_{5,\rm left})^\vee
=25\,(U_{5,M_8})^{\rm tr}.
\tag{962.21}
\]
By (962.12), its restriction to the original nontrivial-deck sum is the unit \(25\cdot92160\). No additional eigenvalue or residual extension is hidden in this left term.

## 4. The localized edge is the actual named CM line

Take the direct sum of the two nontrivial deck spaces in (962.14), and then its full generalized zero-primary part for \(U_5\). These operations are exact: the tame idempotents have unit denominators, and primary decomposition of a finite-dimensional linear operator is exact. Equations (962.12) and (962.21) kill precisely the left term on this localization.

R942 proves that the zero-primary part of the complete original \(S_{10}\) is the line \(\kappa V_{10}^\dagger\), with no additional generalized zero vectors. We therefore obtain
\[
\boxed{
\mathscr K_8:
(\mathcal Q_{\rm Bol}^{\delta\ne1})[U_5^\infty=0]
\ \xrightarrow{\ \sim\ }\ \kappa V_{10}^\dagger .
}
\tag{962.22}
\]
This is an isomorphism from the real Bol cokernel, with its scalar action and both marked Hecke arrows. It does not assert that the original interpolating class is nonzero.

For an especially explicit projection, the full nontrivial-deck part of \(S_{10}\) is R942's \(\langle B_1,B_2,W\rangle\). On that space
\[
U_5^2=147456\,U_5.
\]
Hence, at every prime under consideration,
\[
\Pi_{\rm CM}=1-\frac{U_5}{147456}
\tag{962.23}
\]
is the actual projector onto \(\kappa V_{10}^\dagger\). This uses the returning double-mark operator. The invariant line \(Z\) and its \(666^2\) eigenvalue are absent because its deck character is trivial.

## 5. The precise remaining scalar and two original coefficients

Keep the actual interpolation from R956:
\[
Y_F\in S_{p+9},\qquad
Y_F|_\Sigma=8!\,\frac{F^p}{\mathcal B^{p-9}}\Big|_\Sigma,
\qquad F=V_{p-7}^\dagger.
\tag{962.24}
\]
Take its original negative nontrivial deck summand by the exact tame idempotent. Its Cartier edge then has the original positive character. Define \(\alpha_8\) by
\[
\boxed{
\Pi_{\rm CM}\mathscr K_8Y_F=\alpha_8V_{10}^\dagger.
}
\tag{962.25}
\]
This fixes its normalization because \([Q]V_{10}^\dagger=1\).

If \(Y_F=\sum y_nQ^n\), R956 gives
\(\mathscr K_8Y_F=\sum y_{pn}^{1/p}Q^n\). For a weight-ten form \(f=\sum a_nQ^n\), the original normalized Hecke formula gives
\([Q](T_5^2f)=a_{25}+5^9a_1\).
Consequently (962.23–25) yield the exact formula
\[
\boxed{
\alpha_8=
\left(1-\frac{5^9}{147456}\right)y_p^{1/p}
-\frac{1}{147456}y_{25p}^{1/p}.
}
\tag{962.26}
\]
The roots are coefficient roots in the original perfect field. They are not dropped or replaced by a relabeling of the tame marking.

R950's original low-weight functional is supported on this same simple \(U_5\) zero-primary line. R956's source-preserving comparison thus becomes
\[
\boxed{
S=\frac{6^6}{8}\,\alpha_8
\langle z_V,V_{10}^\dagger\rangle_X.
}
\tag{962.27}
\]
Its specified low pairing is nonzero by R950. An allowed change of lift
\(Y_F\mapsto Y_F+\mathcal AU\) does not change \(\alpha_8\): R956(956.34) says that its change is annihilated by \(\langle z_V,-\rangle_X\), and on the projected line this functional is nonzero. This also proves independence directly without presupposing a Hecke eigenvector lift.

The original descended functional, including all original source multipliers, is
\[
\lambda_h(\Phi_k(F)_{\rm full})
=\frac{m_{\rm I}(c_h^{\rm F})^{1/p}}{36\,d_1\,8!}\,
\alpha_8\langle z_V,V_{10}^\dagger\rangle_X.
\tag{962.28}
\]
Thus the original high trace is nonzero exactly when this specified \(\alpha_8\) is nonzero. By R955 this is also the exact condition excluding the actual longer Cartier chain. Neither (962.22) nor the two-coefficient formula proves that condition.

## Scope and dependencies

The previously open left-term issue in R956's \(r=8\) comparison is now closed on the actual original nontrivial-deck CM localization, for every allowed \(p\ge41\). The remaining question is the nonvanishing of the explicitly defined projected interpolation coefficient (962.26). No arbitrary vector of the same Hecke type has been substituted for it.

The proof uses R918/R920's full tame divisor and integral base change, R942's two genuine marked Hecke arrows and full weight-ten zero-primary theorem, R950's specified low-weight pairing, and R956's original connection and residue comparison. It does not infer a same-label sigma derivative, exclude a nonzero Mordell–Weil image, or complete the main Serre problem.
