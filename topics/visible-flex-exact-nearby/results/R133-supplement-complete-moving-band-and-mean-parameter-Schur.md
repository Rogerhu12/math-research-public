# R133 supplement: exact complete moving band, parameter and mean rows, and a compatible positive high block

2026-11-13, phase_inverse. **Proved exact identities and complete support
reduction.** The actual final moving centre has degree \(M=32\), manifest
SHA256 \(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\).
All statements about angular support below hold on every complete saved
radial piece, for the whole intrinsic parameter box. They do not require
that this centre solve the PDE. No radial coefficient samples or a
finite-dimensional inverse are substituted for an infinite-dimensional
inverse.

The new reduction concerns the **moving unknown** in
R133-supplement-exact-moving-curvature-chart-and-mean-energy.md.
This is the same nonlinear equation whose complete residual the current
moving consumers validate. Its positive high block is derived below in
the same Fourier coordinates. The passive physical Dirac theorem has
different projectors after its coordinate transform; its inverse must
not be inserted into the band reduction without a proved bridge.

## 1. Complete equation and index convention

Use physical angular frequencies \(4j\), \(j\in\mathbb Z\), on the
fourfold circle. Write
\[
 u=\alpha U,\qquad v=s_\nu+\alpha V,\qquad
 m=v_0,\qquad S=u^2+Kv^2,\qquad d=-\beta I S,
 \quad I=\partial_\phi^{-1}P_{\ne0}.
\tag{B.1}
\]
The actual finite centre has \(u_j=v_j=0\) for \(|j|>M=32\);
\(s_\nu=1/C_{{\rm ref},\nu}\) is radial. Its dependence on \(r,\eta,\nu\)
is retained exactly. The true metric coefficients \(K,\gamma,\beta\)
are radial, including their complete primitive and parameter errors.

The complete nonlinear right side is
\[
 \mathcal F_1=d u_\phi+\gamma mK v_\phi-\beta u(1+S),
 \qquad
 \mathcal F_2=d v_\phi-\gamma m u_\phi+\beta v(1-S).
\tag{B.2}
\]
Let \(h=(h_1,h_2)\), \(z=\langle h_2\rangle\). Its complete derivative is
\[
 \mathcal A h=(dI+\gamma mJ(K))h_\phi+L_0h
       -\beta Q_\phi I(2u h_1+2Kv h_2)
       +\gamma z J(K)Q_\phi ,
 \quad Q=(u,v)^t,\quad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},
\tag{B.3}
\]
where
\[
 L_0=\begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
 -2\beta uv&\beta(1-u^2-3Kv^2)
 \end{pmatrix}.
\tag{B.4}
\]
In particular the intermediate product before applying \(I\) is not
cut back to \(M\), or to the eventual output head. The only removed
intermediate coefficient is the true zero coefficient, as prescribed
by the complete periodic primitive.

These formulas define the complete two-component operator. For the
actual nonlinear construction the preserved tangent class is
\(h_1\) odd, \(h_2\) even. In that class \(h_{1,0}=0\) by the explicit
reflection condition, while \(h_{2,0}\) remains an independent unknown.
We keep both zero-frequency columns in the unrestricted algebra.
We do not infer a physical non-reflection coordinate theorem from
this algebraic extension.

## 2. Exact infinite matrix entries

Put \(W_1=u\), \(W_2=Kv\), \(Q_1=u\), \(Q_2=v\).
For output component \(a\), input component \(b\), and indices \(j,n\),
the exact complete matrix is
\[
\begin{split}
 \mathcal A_{ab}(j,n)={}&
 i4n\,d_{j-n}\delta_{ab}
 +i4n\,\gamma mJ(K)_{ab}\delta_{jn}
 +(L_0)_{ab,j-n}\\
 &-2\beta\sum_{\substack{k\in\mathbb Z\\k\ne0}}
       \frac{j-k}{k}\,Q_{a,j-k}W_{b,k-n}\\
 &+\gamma\delta_{b2}\delta_{n0}\,
                   i4j\,[J(K)Q]_{a,j}.
\end{split}
\tag{B.5}
\]
The sum is finite for each entry because its two centre factors have
complete support in \([-M,M]\). It has no small divisor from \(k=0\):
that coefficient is exactly excluded by \(I\), while the other mean
and rank-one columns in (B.5) remain.

For example, the fourth term follows by multiplying
\(i4(j-k)Q_{a,j-k}\) by
\(2W_{b,k-n}/(i4k)\). This establishes its sign, order and both
frequency locations directly.

Every entry in (B.5) vanishes when
\[
                  |j-n|>2M=64.                         \tag{B.6}
\]
The last rank-one column has support at most \(M\), and so also
satisfies (B.6). This is the bandwidth of the complete infinite
operator, including its nonlocal term and its true mean column.
It is not a finite truncation assertion.

## 3. The exact second mean row

Periodic integration of the complete nonlinear equation gives
\[
        \langle\mathcal F_2\rangle
               =\beta m(1-S_0).                        \tag{B.7}
\]
Indeed
\(\langle d v_\phi\rangle
 =\beta\langle(S-S_0)v\rangle\), which cancels the cubic term
except for \(-\beta mS_0\). Therefore
\[
 z'=\beta(1-S_0)z
       -2\beta m\langle u h_1+Kv h_2\rangle+f_{2,0}.
\tag{B.8}
\]
Equivalently,
\[
 \mathcal A_{21}(0,n)=-2\beta m\,u_{-n},\qquad
 \mathcal A_{22}(0,n)=
       \beta(1-S_0)\delta_{n0}-2\beta mK\,v_{-n}.
\tag{B.9}
\]

Thus the **direct** input to the complete second mean row vanishes
already for \(|n|>M\). This does not remove an indirect path from a
high mode through the retained head into the mean. Such paths are
exactly kept by the Schur equation below.

The other mean is kept by (B.5). In the actual reflection tangent
class its equation and source have the corresponding odd parity;
this is an explicit symmetry restriction, not an omitted column in
an unrestricted calculation.

## 4. The full metric parameter column, including the normalized reference

For the actual compact metric deformation, \(a\) and \(\beta\) are
fixed, while
\(\gamma_\nu=(h_0/2)\gamma\) and \(K_\nu\) are the genuine radial
derivatives. At fixed physical moving fields \(u,v\), the complete
parameter source is
\[
\begin{split}
 f_\nu={}&-\beta K_\nu Q_\phi I(v^2)
 +\gamma_\nu m J(K)Q_\phi
 +\gamma m(K_\nu v_\phi,0)^t\\
 &-\beta K_\nu(uv^2,v^3)^t .
\end{split}
\tag{B.10}
\]
Its support is at most \(3M=96\). Its exact second mean is
\[
                 (f_\nu)_{2,0}=-\beta mK_\nu(v^2)_0.
\tag{B.11}
\]
The two cubic mean terms cancel exactly as in (B.7);
the mean must not be bounded or dropped separately before this
cancellation.

The solver unknown is \(Y=(U,V)\), with \(u=\alpha U\) and
\(v=s_\nu+\alpha V\), at fixed positive amplitude \(\alpha\).
The normalized radial right side is
\(\alpha^{-1}(\mathcal F-(0,s_\nu')^t)\).
Its state derivative is exactly \(\mathcal A\): the two factors of
\(\alpha\) cancel. Its parameter column is
\[
  f_\nu^{\rm norm}=
  \alpha^{-1}\left[f_\nu+
          \mathcal A(0,s_\nu^{\,\boldsymbol\cdot})^t
          -(0,(s_\nu^{\,\boldsymbol\cdot})')^t\right].
\tag{B.12}
\]
The bold dot denotes the parameter derivative, while a prime denotes
the radial derivative. Thus the parameter dependence of the reference
mean and its radial derivative are both retained.

Writing \(s_{\nu}= \partial_\nu s\), the exact second mean of (B.12) is
\[
 \frac1\alpha\left[
 -\beta mK_\nu(v^2)_0
 +s_\nu\beta(1-S_0-2Km^2)-s_\nu'\right].
\tag{B.13}
\]
Its complete support is still at most \(3M\), since the extra state
column in (B.12) has support at most \(2M\). The actual parameter
support is contained in the already specified compact radial bump;
no new artificial parameter column is introduced outside it.

## 5. Actual physical boundary means and all nonzero moment rows

The finite angular support of the **interior** equation does not make
the physical boundary operator a finite Laurent polynomial. The
exact physical angle is
\[
 \theta=\phi+m^{-1}I(v-m),\qquad \theta_\phi=v/m>0.
\tag{B.14}
\]
For a physical frequency \(k=4j\),
\[
 C_k=m^{-1}\langle e^{-ik\theta}\rangle_\phi,\qquad
 B_k=m^{-1}\langle u e^{-ik\theta}\rangle_\phi.
\tag{B.15}
\]
For a complete moving variation \(h\), put
\[
 z=\langle h_2\rangle,\qquad
 \Theta_h=m^{-1}I(h_2-zv/m).
\tag{B.16}
\]
Then the exact boundary derivative is
\[
\begin{split}
 \delta C_k&=-zC_k/m-(ik/m)
                    \langle e^{-ik\theta}\Theta_h\rangle,\\
 \delta B_k&=-zB_k/m+m^{-1}
            \langle e^{-ik\theta}(h_1-iku\Theta_h)\rangle .
\end{split}
\tag{B.17}
\]
In particular
\[
 \delta C_0=-z/m^2,\qquad
 \delta B_0=\langle h_1\rangle/m-u_0z/m^2.                \tag{B.18}
\]
All allowed means remain. In the actual reflection class the second
expression is zero by its stated oddness, not by deleting an
independent even mean.

For the normalized physical \(C\)-mean
\(c_0=(m^{-1}-C_{\rm ref})/\alpha\), its exact state derivative with
respect to \(V_0\) is \(-m^{-2}\), and its exact parameter derivative
at fixed \(Y\) is
\[
 \partial_\nu c_0
 =\frac{-s_\nu/m^2-\partial_\nu C_{\rm ref}}{\alpha}
 =-\frac{(\partial_\nu C_{\rm ref})V_0(2s+\alpha V_0)}{m^2}.
\tag{B.19}
\]
The equality uses \(C_{\rm ref}=1/s\), \(m=s+\alpha V_0\).
It is the complete true parameter column, including its cancellation.
Any remaining metric, regular-tail or exterior parameter dependence
must of course be differentiated in the exterior boundary operator
itself.

Equations (B.15)–(B.17) retain the infinite physical Fourier tail and
its complete quadrature/analytic error budget. An interior support
argument is not permission to truncate these rows.

## 6. The complete head and the exact coupling shell

Let \(P_L={\bf1}_{|j|<N}\) and \(P_H=I-P_L\), with \(N>2M\).
By (B.6), the two cross operators factor through the finite shell
\[
       N-2M\le |j|<N                                    \tag{B.20}
\]
on their head side, and through
\(N\le |j|\le N+2M-1\) on their high side.
Every head index \(|j|<N-2M\) has exactly zero **direct** coupling to
the high block. These are exact support facts, valid also for the
full intermediate primitive in (B.5).

For the current \(M=32\), the smallest head containing the entire
parameter and centre-residual support is \(N=97\):
\[
\begin{array}{c|c}
 \text{retained head}& |j|\le96\\
 \text{first physical high frequency}&4N=388\\
 \text{head-side coupling shell}&33\le |j|\le96\\
 \text{inner core}&|j|\le32 .
\end{array}
\tag{B.21}
\]
In the actual real reflection class this is a 193-dimensional angular
head: the original 65-dimensional core plus a 128-dimensional shell.
The scalar metric parameter gives a 194th global unknown. This is
only a structural size. It is **not** a proof that the high block is
invertible starting at frequency 388, or that this radial head BVP
is invertible.

The complete centre residual has support at most \(3M\): the radial
derivative of the finite centre has support \(M\), and (B.2) has
support \(3M\). True radial coefficient uncertainty does not enlarge
angular support. Actual interface jumps of the moving centre have
support at most \(M\). Thus they also lie in this head. Ordinary
user/source inputs and the true physical boundary operator need not
have finite support and are still retained.

If a complete high Green \(G_H\) and its two-port Poisson operator
\(P_H^\partial\) are established in these same coordinates and
projections, the exact equation is
\[
\begin{split}
 h_H&=P_H^\partial g_H+
                  G_H(f_H+\mathcal A_{HL}h_L),\\
 [\partial_r-\mathcal A_{LL}
       -\mathcal A_{LH}G_H\mathcal A_{HL}]h_L
 &=f_L+\mathcal A_{LH}G_Hf_H
           +\mathcal A_{LH}P_H^\partial g_H .
\end{split}
\tag{B.22}
\]
The Schur correction acts on the shell rows and columns in (B.20).
It still changes the core and the mean after the **full head inverse**
is taken; no path through the shell is dropped.
The full physical boundary rows (B.17), their high input/output
columns, parameter column, and all true source/jump columns are
substituted into the same reduction. A finite angular head remains
a radial BVP until its radial validation has been supplied.

## 7. A compatible positive Dirac frame with identity interfaces

Here is a positive high-block framework that preserves the exact
band. On \(K>0\), set \(q=\sqrt K\), \(\eta=-\gamma m>0\), and
\[
       w=\operatorname{diag}(-1,q)h,\qquad
       J_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\tag{B.23}
\]
This is a radial Fourier-diagonal transformation, with no angular
coordinate change and no half-density multiplication.
The exact equation is
\[
 w_r=\eta qJ_0w_\phi+
       (d\partial_\phi+d_\phi/2)w+
       V_{\rm mov}w+N_{\rm mov}w+f_w,                   \tag{B.24}
\]
where \(f_w=\operatorname{diag}(-1,q)f\),
\[
 V_{\rm mov}=
 \begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&2\beta quv\\
 2\beta quv&\beta(1-u^2-3Kv^2)+q'/q
 \end{pmatrix}-\frac12d_\phi I,                         \tag{B.25}
\]
and
\[
 N_{\rm mov}w=
 2\beta\binom{-u_\phi}{qv_\phi}\,
                      I(uw_1-qvw_2)
       -\gamma\binom{qv_\phi}{u_\phi}\langle w_2\rangle .
\tag{B.26}
\]
The scalar transport in (B.24) is exactly skew-adjoint and
\(V_{\rm mov}\) is real symmetric. Formula (B.26) has **no factor
\(q^{-1}\)**. Its mean rank-one column is retained.

At an actual PPoly join, moving corrections are defined on the same
\(\phi\) circle. Their homogeneous interface is identity. Since the
intrinsic \(K\) is continuous, the frame (B.23) has identity interface
too. The complete affine centre jump appears as the exact source
\(\operatorname{diag}(-1,q)[h]\). No unitary angle pullback or
unpaid opposite-cone leakage is introduced at these joins.

The fixed physical-angle Jacobi equation and its passive pullback
have different variables. Their separate residual-sensitive bridge
is still required at a turning block proved only for that operator.
Equations (B.23)–(B.26) do not assert that bridge for free.

## 8. Complete high nonlocal gain and exact vanishing of drift cross blocks

Let
\[
 R=\|\sqrt{u^2+q^2v^2}\|_\infty,\qquad
 L=\|\sqrt{u_\phi^2+q^2v_\phi^2}\|_\infty .
\]
For \(N>M\), an input supported in \(|j|\ge N\), multiplied by a centre
coefficient of degree \(M\), has intermediate support
\(|j|\ge N-M\). Therefore the exact primitive has norm at most
\(1/[4(N-M)]\) on that intermediate field. The mean term in
(B.26) vanishes on a high input. Consequently
\[
 \|P_HN_{\rm mov}P_H\|
        \le n_N:=\frac{|\beta|RL}{2(N-M)}.               \tag{B.27}
\]
This is a complete same-space high estimate. No finite primitive
truncation, analytic-width loss or omitted mean term is used.
Low/high columns remain exactly as in (B.22).

Put \(\mathcal C=iJ_0\). Split the high space into the two constant
branches of \(\mathcal C D_\phi\), with stable and unstable signs.
The drift and its half-derivative are scalar and have bandwidth at
most \(2M\). A cross-branch scalar entry would require opposite
frequency signs, hence \(|j-n|\ge2N>2M\). It follows that
\[
 \Pi_s(d\partial_\phi+d_\phi/2)\Pi_u
 =\Pi_u(d\partial_\phi+d_\phi/2)\Pi_s=0.                 \tag{B.28}
\]
This exact zero is stronger than paying a drift derivative norm.
It holds on this finite-centre moving operator, not on an arbitrary
angularly reparametrized operator.

Write \(V_{\rm mov}=aI+T\), \(\operatorname{tr}T=0\).
The scalar part has no cross block, while the real symmetric
traceless part anticommutes with \(\mathcal C\).
The same bandwidth argument shows its two diagonal high branch
compressions vanish. Explicitly
\[
\begin{split}
 a&=\frac{q'}{2q}-\frac{3\beta}{2}S-\frac{\beta}{2}S_0,\\
 T&=\begin{pmatrix}
 -\beta(1+u^2-Kv^2)-q'/(2q)&2\beta quv\\
 2\beta quv&\beta(1+u^2-Kv^2)+q'/(2q)
 \end{pmatrix}.
\end{split}
\tag{B.29}
\]
Let \(a_*=\|a\|_\infty\), \(t_*=\|T\|_\infty\).
A convenient complete bound is
\[
       a_*+t_*\le |q'|/q+|\beta|(1+3\|S\|_\infty).
\tag{B.30}
\]
Indeed \(S\ge0\), \(|S_0|\le\|S\|_\infty\), and
\((1+u^2-Kv^2)^2+4Ku^2v^2=(1+S)^2-4Kv^2\le(1+S)^2\).

## 9. A full positive high Green gate, with all lower blocks retained

On a strictly positive interval, the diagonal branch propagators of
(B.24) have full Hilbert decay rate at least
\[
        \lambda_N=\inf(4N\eta q-a_*-n_N).
\]
The complete off-diagonal coupling is bounded by
\(k_N=\sup(t_*+n_N)\).
Whenever
\[
                         \lambda_N>k_N,                \tag{B.31}
\]
the usual two-direction Green construction on the full high Hilbert
space gives
\[
 \|G_H\|_{L^2_rL^2_\phi\to L^2_rL^2_\phi}
       \le(\lambda_N-k_N)^{-1},\qquad
 \|P_H^\partial\|
       \le\frac{\sqrt{\lambda_N/2}}{\lambda_N-k_N}.
\tag{B.32}
\]
Stable input is at the left, unstable input at the right. Both output
traces and all ordinary source columns follow from the same
exponential kernels, as in the passive Dirac proof. Uniform Fourier
Galerkin energy followed by density constructs these full operators;
a finite inverse is not being promoted to an infinite inverse.

The exact identity interfaces described above allow the same global
energy estimates across every saved radial join. There is no product
of artificial angle-interface factors.

All terms in (B.31) must be evaluated on the current centre. In
particular \(q'/q\) is a real radial turning term; it is not deleted.
If an exact radial Airy/Riccati reference is used to absorb it, that
is a different, explicitly constructed reference contract.
Condition (B.31) is therefore not asserted at the arbitrarily close
turning endpoint, and \(N=97\) from (B.21) is not asserted to satisfy it.

## 10. Exact computation and current scope

The companion standalone source
scripts/fourfold_codazzi_moving_full_band_exact.mjs uses normalized
BigInt rational complex Laurent arithmetic. Its independent dual
derivative of the nonlinear equation checks the complete matrix
action, parameter action, normalized \(s_\nu,s_\nu'\) column, and
mean rows. Its exact degree-32 fixture also detects the change caused
by incorrectly cutting the intermediate primitive at degree 32.
There are 22 exact gates. They passed in the pure JavaScript runtime;
the complete small text report is
notes/2026-11-13-R133-moving-full-band-exact-algebra-native.json.

The fixture is explicitly a rational algebra fixture, **not** the
current candidate coefficients. The universal identities are proved
above; the computation checks their implementation and index
conventions. The report does not claim current numerical high
invertibility or a finite radial inverse.

Reproduction needs only a standard Node runtime:
\[
 \texttt{node scripts/fourfold_codazzi_moving_full_band_exact.mjs
 --out notes/2026-11-13-R133-moving-full-band-exact-algebra-native.json}.
\]
It has no numerical-library dependency and reads no binary native
reports.

The actual remaining task is quantitative: pay a same-centre complete
high inverse, validate the resulting finite radial head and scalar
parameter row, and insert the complete physical boundary operator,
ordinary sources and true joins into the final nonlinear contraction.
This result identifies a concrete finite block structure and its
compatible high operator; it does not replace those remaining gates.
