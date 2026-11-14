# R133 supplement: the actual moving positive root piece, complete Riccati reference, and all-frequency two-port inverse

2026-11-13, phase_inverse. **Proved, with a new exact rational budget:
62 gates passed.** This theorem concerns the current complete moving
centre with manifest SHA256
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\).
It solves the complete linearized **moving equation** on
\[
 I_\eta=[r_*(\eta),r_*(\eta)+h],\qquad h=9/10^6.          \tag{P.1}
\]
The whole original \(|\eta|\le10^{-9}\) interval is retained.

The actual high cutoff is \(|j|\ge97\), physical frequency \(|4j|\ge388\).
It is proved here, rather than inferred from bandwidth. The complete
retained head has 193 real reflection coordinates; its two Cauchy rows,
all allowed means, and all head/high paths are included. The resulting
whole-frequency local inverse has
\[
 \|h_{\rm sol}\|_{L^2_rL^2_\phi}
 <\frac1{8000}\|f\|_{L^2_rH^{1/3}_\phi}
       +\frac3{250}\|g\|,                               \tag{P.2}
\]
and both complete raw moving endpoint states obey
\[
 \|\operatorname{Tr}_{r_*,r_*+h}h_{\rm sol}\|
 <\frac1{25}\|f\|_{L^2_rH^{1/3}_\phi}+\frac{27}{5}\|g\|.
\tag{P.3}
\]
The port vector \(g\) is defined precisely below: both low Cauchy rows
at the true root, one high stable row at the root and one high unstable
row at the right endpoint. This is the correct number of conditions.

The theorem does not attach the negative-side physical fold, the rest
of the positive body, or the exterior regular graph. It does not
solve the global scalar parameter Schur equation or nonlinear BVP.
Those remain separate interfaces. In particular this local threshold
does not claim a whole-body cutoff of 97.

## 1. Actual input and strict domain

The actual joint-germ theorem is
R133-supplement-current-moving-body-physical-complex-germ.md, Git blob
\(\mathtt{bfe73ee59142618bc7e36d5e3fe06929d9fb68cb}\).
It gives the whole rectangle
\[
 \Re r\in[r_*^- -10^{-5},r_*^+ +10^{-5}],\quad
 |\Im r|\le10^{-5},\quad|\Im\phi|\le1/1024,
\]
with
\[
 r_*^-=0.2383968742994,\qquad
 r_*^+=0.2383968743003.
\tag{P.4}
\]
The complete candidate is on actual piece 2549,
\[
 \left[
 \frac{2147184947341121}{9007199254740992},
 \frac{4295308144604611}{18014398509481984}
 \right].
\tag{P.5}
\]
The exact rational gate checks
\(h+(r_*^+-r_*^-)<10^{-5}\), with margin exceeding
\(9\cdot10^{-7}\), and checks the whole joint real interval against
(P.5). Thus the union of (P.1) over every allowed root lies strictly
inside the actual same germ. There is no continuation through a
PPoly or target seam.

Only the intrinsic \(K'\) upper bound is taken from
R133-supplement-actual-physical-fold-and-full-Airy-collar.md,
Git blob \(\mathtt{90daf082281a7dfd6616f62e5c187795bf2324ea}\):
\[
       59.74380437<K'<60.465470.                        \tag{P.6}
\]
Its intrinsic rectangle and whole-\(\eta\) target are the same.
The compact \(\nu\) bump is exactly zero here. No nonradial
amplitude-\(.75\) field or coefficient is reused.

The new-centre germ gives
\[
\begin{gathered}
 -m>1.1197077044,\quad |m|<1.119807069,\quad
 \|v-m\|_{A_{1/1024}}/m_-<0.599103154,\\
 a_{\rm char}=-\gamma v>0.5025436590,\quad
 |a_{\rm char}|<2.004892,\quad
 |\gamma u|<0.705336,\quad
 |\gamma u_\theta|<7.302797 .
\end{gathered}                                                       \tag{P.7}
\]
The first two characteristic bounds are uniform on the physical
circle. The genuine inverse angle covers that circle, so averaging
in the moving angle gives the actual radial coefficient
\(\eta=-\gamma m=\langle a_{\rm char}\rangle_\phi\).
The true rotational gap \(E-(a_{\rm phys}')^2>0\) on this germ also
gives \(|\beta|<\gamma\).

## 2. Complete moving coefficients deduced from those proved bounds

All norms here concern the finite moving fields \(u,v\), rather than
a relabelled physical Fourier expansion. Parseval and the exact
support \(|j|\le32\) give the following outward bounds:
\[
\begin{gathered}
 1/2<\eta<201/100,\qquad 25/56<\gamma<9/5,\qquad|\beta|<9/5,\\
 |u|_\infty<8/5,\quad |u_\phi|_\infty<27,\quad
 \|u\|_{A^0}<13,\quad\|u_\phi\|_{A^0}<216,\\
 \|v\|_{A^0}<9/5,\qquad\|v_\phi\|_{A^0}<86,\qquad
 0\le K<61/100000,\qquad \|S\|_\infty<13/5 .
\end{gathered}                                                       \tag{P.8}
\]
Here \(S=u^2+Kv^2\).

For completeness, \(\gamma>\eta/|m|>(1/2)/(28/25)=25/56\).
Also \(\gamma< (201/100)/1.1197077044<9/5\).
The moving angular Jacobian is \(v/m\), bounded by \(1+0.599103154<8/5\).
Thus \(u_\phi=(v/m)u_\theta\), and (P.7) gives the first two \(u\)
supremum bounds in (P.8). There are exactly 64 possible nonzero
complex coefficients in the real odd \(u\) and its derivative;
Cauchy--Schwarz gives the factor 8 in their \(A^0\) bounds.
The \(v\) bounds follow directly from the complete saved strip sum:
\[
 \|v\|_{A^0}\le m_+(1+\kappa)<9/5,\qquad
 \|v_\phi\|_{A^0}\le128m_+\kappa<86 .
\]
In particular physical supremum bounds have not been called moving
Wiener bounds without a conversion.

Since \(K(r_*)=0\), (P.6) gives the stated \(K\) bound.
Introduce the genuine radial optical coordinate
\[
       s(r)=\int_{r_*}^{r}\eta(t)\,dt,\qquad 0\le s\le L .
\tag{P.9}
\]
Then
\[
          29<K_s<122,\qquad K(0)=0.                    \tag{P.10}
\]
The entire construction below uses this same actual \(m(r)\),
\(\eta(r)\), and \(K(r)\). It is not a constant-coefficient surrogate.

Finally \(d=-\beta I S\) has degree at most 64 and
\(d_\phi=-\beta(S-S_0)\). Since \(0\le S_0\le\|S\|_\infty\),
the complete nonmean degree-64 polynomial satisfies
\[
 a_1:=\|d_\phi\|_{A^0}
 \le|\beta|\sqrt{128}\|S-S_0\|_2<54.                   \tag{P.11}
\]
This is a complete Fourier sum, with no unproved tail.

## 3. Exact positive scalar reference at every frequency

Write \(M=|4j|>0\), and initially allow \(M\) to be any positive real
number. For the radial principal equation, put
\(R=\operatorname{diag}(-1,1)\),
\(S_\sigma=\operatorname{diag}(i\sigma,1)\), \(\sigma=\operatorname{sgn}j\),
and \(x=S_\sigma R h_j\).
Its exact principal system is
\[
       x_s=-M\begin{pmatrix}0&K(s)\\1&0\end{pmatrix}x.
\tag{P.12}
\]
The scalar second component solves \(u_{ss}=M^2K(s)u\).

Construct \(g_M>0\) from the left and \(p_M>0\) from the right by
\[
\begin{split}
 (g_M)_s&=M(K-g_M^2),&g_M(0)&=M^{-1/3},\\
 (p_M)_s&=M(p_M^2-K),&p_M(L)&=M^{-1/3}.
\end{split}
\tag{P.13}
\]
Forward and backward scalar comparison prove strict positivity and
the finite bound
\[
      p_M,g_M\le\max(M^{-1/3},\sqrt{K_{\max}}).
\tag{P.14}
\]
Thus these are well-defined actual scalar reference functions.

Equivalently, \(Mg_M(s)\) is the minimum of
\[
 \int_0^s(|u'|^2+M^2K|u|^2)\,dt
                   +M^{2/3}|u(0)|^2,\qquad u(s)=1,
\tag{P.15}
\]
and \(Mp_M(s)\) is the analogous right minimum with
\(M^{2/3}|u(L)|^2\). These strictly coercive one-dimensional minima
also specify the actual reference independently of a numerical
Riccati integrator. They introduce two positive **reference**
impedances, not the actual exterior regular boundary condition.

Let \(W_M=p_M+g_M\) and
\[
       T_M=W_M^{-1/2}
            \begin{pmatrix}p_M&-g_M\\1&1\end{pmatrix}.
\tag{P.16}
\]
Its determinant is exactly one. Since
\(W_s=M(p-g)W\), direct multiplication gives
\[
 -M\begin{pmatrix}0&K\\1&0\end{pmatrix}T_M-(T_M)_s
       =T_M\operatorname{diag}(-MW_M/2,MW_M/2).
\tag{P.17}
\]
Consequently the actual \(r\)-rates are
\(\mp\kappa_M(r)\), \(\kappa_M=\eta MW_M/2>0\).
Every radial turning derivative, including the apparent \(q'/q\),
has been absorbed **exactly** in this reference. It is not dropped
or bounded by a singular root-distance constant.

## 4. Uniform frequency dependence and the Airy-weighted state

Differentiating the positive variational minimum (P.15) in \(M\)
at its unique minimizer gives
\[
       0\le M E_M'/E_M\le2 .
\]
The derivative term in the form has exponent zero, the potential
has exponent two, and the endpoint term exponent \(2/3\).
Stationarity removes the derivative of the minimizer. Hence
\[
       |M\partial_M\log p_M|,\ 
       |M\partial_M\log g_M|\le1 .                     \tag{P.18}
\]
Endpoint cases follow directly from (P.13).

Writing \(\dot p=M\partial_Mp\), \(\dot g=M\partial_Mg\),
\[
 T_M^{-1}M\partial_MT_M=
 \frac1{2W_M}
 \begin{pmatrix}\dot p-\dot g&-2\dot g\\
                 -2\dot p&\dot g-\dot p\end{pmatrix}.
\tag{P.19}
\]
Its Frobenius norm squared is at most \(3/2\), so its operator norm
is less than \(3/2\).

The complete high state used for the inverse is
\[
       Z_j=M^{1/6}T_M^{-1}S_\sigma R h_j .
\tag{P.20}
\]
Thus \(h_j=RS_\sigma^{-1}\mathcal T_M Z_j\), with
\(\mathcal T_M=M^{-1/6}T_M\). Its logarithmic frequency derivative
has norm less than \(5/3\). For two high frequencies with ratio at
most 2,
\[
\begin{split}
 \|\mathcal T_M^{-1}\mathcal T_N\|&\le2^{5/3}<4,\\
 \|\mathcal T_M^{-1}\mathcal T_N-I\|
       &\le3|M-N|/\min(M,N),\\
 N\|\mathcal T_M^{-1}\mathcal T_N-I\|&\le6|M-N|.
\end{split}
\tag{P.21}
\]
The last two inequalities follow by integrating (P.19);
\((5/3)2^{2/3}<3\) and \((5/3)2^{5/3}<6\).
They control actual neighbouring frequencies, without a bare
pullback smallness assumption.

## 5. Complete frame and source bounds at the zero-curvature end

Put
\(D_M=\operatorname{diag}(W_M^{-1/2},W_M^{1/2})\).
Both \(D_MT_M\) and its inverse have norm less than 2: their
Frobenius norm squared is at most 3.

On the current high block \(N_0=97\), \(M\ge388>6^3\).
By (P.14) and \(K_{\max}<1/1600\),
\[
                     W_M<1/3.                         \tag{P.22}
\]
A uniform lower bound is
\[
                     W_M\ge\tfrac12M^{-1/3}.           \tag{P.23}
\]
To prove it, scale \(z=M^{2/3}s\), \(y=M^{1/3}g_M\).
Then \(y_z\ge29z-y^2\), \(y(0)=1\).
For \(z\le1/2\), the zero-potential comparison gives
\(y\ge1/(1+z)\ge2/3\). For \(z\ge1/2\), the constant lower barrier
\(y=1/2\) has strictly positive inward vector field. This proves
(P.23) for every frequency, including arbitrarily large ones.

These give the exact source convention and reconstruction bounds
\[
 \|M^{1/6}T_M^{-1}S_\sigma R f_M\|_{\ell^2}
       <3\|f\|_{H^{1/3}_\phi},\qquad
 \|h_H\|_2<3\|Z\|_2.                                   \tag{P.24}
\]
For example the first source weight is at most
\(\sqrt2M^{1/3}\), while the second is at most \(M^{1/6}/\sqrt3\).
The reconstruction weights are at most \(\sqrt2\).
There is no \(q^{-1}\), no radial derivative of the source, and no
change to a two-dimensional mixed-coordinate source space.

At the true root an even more specific port comparison holds.
Here \(g_M(0)=M^{-1/3}\). In (P.15)'s right-hand version use the
trial \(u(s)=e^{-4M^{2/3}s}\). Since \(K(s)\le122s\),
\[
 Mp_M(0)\le
 \left(2+\frac{122}{64}+1\right)M^{2/3}
       <5M^{2/3}.
\]
The last \(1\) pays the actual right Robin term, without discarding
it. Therefore
\[
 M^{-1/3}\le W_M(0)<6M^{-1/3}.
\]
The norm (P.20) at the root and the complete two-row simple moving
Airy norm
\[
             \|\operatorname{diag}(M^{1/3},1)h_j\|_{\ell^2}
\tag{P.25}
\]
bound each other by a factor less than 5.

At the right endpoint put
\(\omega_M=(K(L)+M^{-2/3})^{1/2}\).
One has \(\omega_M/9<W_M(L)\le2\omega_M\), and hence (P.20)
and
\(M^{1/6}\operatorname{diag}(\omega_M^{-1/2},\omega_M^{1/2})h_j\)
bound each other by a factor less than 6. The lower estimate follows
from the comparison in the next section and \(p_M(L)=M^{-1/3}\).
These are actual fixed-radial ports of the moving equation.
They are not silently identified with the physical fold's curved
ports or with physical means.

## 6. The grounded matrix structure pays the full reaction and nonlocal terms

A further useful uniform consequence is
\[
                         K/W_M<1.                      \tag{P.26}
\]
Here is a proof valid at every point and frequency.
For \(k=K(s)>0\), use the interval of length \(k/244\) immediately
to its left. It lies inside \([0,s]\), and \(K\ge k/2\) there.
Comparison from a nonnegative initial value gives
\[
 g_M(s)\ge\sqrt{k/2}\,
       \tanh\left(\frac{Mk^{3/2}}{244\sqrt2}\right).
\]
If the argument is at least 1, \(\tanh1>3/4\) gives
\(k/W\le k/g<2\sqrt k<1/20\).
Otherwise \(Mk^{3/2}<366\). Since \(s\le k/29\), the
zero-potential comparison gives
\[
 k/g\le\sqrt k(x+x^3/29),\qquad x=M^{1/3}\sqrt k<8.
\]
This is less than \(21\sqrt k<21/40<1\).
At \(k=0\) (P.26) is immediate.
The positive-series inequality \(e^2>7\) justifies the stated
\(\tanh1\) bound.
At the right endpoint the same alternatives, together with
\(p_M(L)=M^{-1/3}\), give the factor-9 lower bound used above.

After the unit phase \(S_\sigma R\), the moving local matrix is
\[
 B=\begin{pmatrix}a&Kb\\c&e\end{pmatrix},\quad
 a=-\beta(1+3u^2+Kv^2),\quad e=\beta(1-u^2-3Kv^2),\quad
 b=2i\sigma\beta uv,\quad c=-b .                        \tag{P.27}
\]
It is essential that the upper-right entry contains the exact \(K\).
For (P.8),
\[
\begin{array}{c|cccc}
 &a&e&b&c\\ \hline
 L^\infty\text{ bound}&16&3&11&11\\
 A^0\text{ bound}&915&307&85&85 .
\end{array}
\tag{P.28}
\]
These are complete coefficient bounds.

For a fixed output frequency \(M\), expand \(T_M^{-1}BT_M\).
Its entries are linear combinations with multipliers
\(p/W,g/W,K/W,pg/W,p^2/W,g^2/W\).
The first two are at most 1, and the last three at most \(W\).
Thus the operator obtained by putting \(T_M\) on both sides at
that same output frequency is bounded by
\[
 2B_\infty,\qquad
 B_\infty\le16+3+11(1+1/3)<34 .                         \tag{P.29}
\]
This uses multiplication supremum bounds and left Fourier
multipliers, not a supposed common eigenbasis of the coefficients.

The actual input uses \(T_N\). Its difference from the same-output
expression is bounded using (P.21). Since the complete angular band
is 64,
\[
 \|{\rm reaction\ difference}\|
 \le\frac{24M_c}{N_0}B_A,\quad
 M_c=32,\quad
 B_A\le915+307+85(1+1/3)<1336 .                         \tag{P.30}
\]
The letter \(M_c\) is the centre degree; \(M\) in (P.12) remains a
physical frequency. To verify the constant, each same-frequency
matrix has norm at most four times its weighted entry sum, the
relative-frame difference costs \(3|j-n|/N_0\), and
\(|j-n|\le2M_c\).

The scalar transport \(d\partial_\phi\) becomes
\(d\partial_\phi+\tfrac12d_\phi\), which is exactly skew-adjoint,
plus a bounded remainder of norm at most
\[
                      (6+\tfrac12)a_1.                \tag{P.31}
\]
Indeed (P.21) bounds its true Fourier kernel difference by
\(6|4(j-n)||d_{j-n}|\); the additional half derivative costs \(a_1/2\).

The high part of the exact mean-rank term is zero on high input.
The other nonlocal term is kept completely. Its intermediate index
is at least \(N_0-M_c\), so the periodic primitive costs at most
\(1/[4(N_0-M_c)]\). The \(D_M\)-weighted dyad has complete coefficient
sum bounded by
\[
 F_N\le(216+86/3)(13+9/5)<3700.                         \tag{P.32}
\]
The frequency ratio in the two \(D\) factors costs at most \(\sqrt2\);
the additional \(M^{1/6}\) costs \(2^{1/6}\); their product is less
than 2. The two \(T/D\) comparisons cost at most 4. Including the
factor \(2|\beta|\) gives the full same-space remainder
\[
        \|{\rm nonlocal\ high\ part}\|
               \le\frac{4|\beta|F_N}{N_0-M_c}.          \tag{P.33}
\]
No ungrounded \(M^{1/3}\) matrix bound has been used. Every \(K/W\)
and \(W\) factor, the complete intermediate primitive, and the mean
rank column before high compression are accounted for.

## 7. Actual high inverse on the full unbounded frequency set

The exact high equation in the state (P.20) is
\[
 Z_r=\operatorname{diag}(-\kappa_M,\kappa_M)Z+
       P_H(d\partial_\phi+d_\phi/2)P_H Z+\mathcal E Z+F_Z.
\tag{P.34}
\]
The scalar transport does not mix its two branch components.
Its projected operator is still exactly skew-adjoint.
The complete remainder obeys
\[
 E_0<
 \frac{13}{2}54+2(34)
       +\frac{24(32)(1336)}{97}
       +\frac{4(9/5)(3700)}{65}
 =\frac{14383799}{1261}<11408.                         \tag{P.35}
\]
Both frequency signs are included. They cannot directly couple in
this high block because their separation is at least \(2N_0>64\).

The diagonal stable evolution is contractive forward in \(r\);
the diagonal unstable evolution is contractive backward.
This remains true with the exact skew transport in (P.34).
Fourier Galerkin energy, the standard differentiated energy for
smooth dense data, and density construct the full propagators.
The derivative commutators of the finite smooth drift are bounded;
the nonnegative diagonal Fourier multiplier commutes with those
derivatives. Uniqueness follows from the same energy. Thus no
finite inverse is being used as a full inverse.

The complete diagonal two-port Green on \(I_\eta\) satisfies
\[
           \|G_0\|_{L^2_r\to L^2_r}\le h,\qquad
           \|P_0\|\le\sqrt h=3/1000.                   \tag{P.36}
\]
The two columns take values in the two orthogonal branch spaces.
The source-to-complementary-trace norm is at most \(\sqrt h\).
These bounds use the entire interval and every frequency.

The new rational budget proves
\[
     hE_0=\frac{129454191}{1261000000}<\frac18 .          \tag{P.37}
\]
Neumann inversion on this one full Hilbert space gives
\[
 \|Z\|_{L^2}\le\frac87(h\|F_Z\|+\sqrt h\,\|g_H\|).
\tag{P.38}
\]
The two independent high inputs are
\(Z_s(r_*)\) and \(Z_u(r_*+h)\).
The full outgoing high trace has
\[
 \|g_{\rm out}\|
 \le\frac87\|g_H\|+\frac87\sqrt h\,\|F_Z\|.
\]
Combining incoming and outgoing states, and using (P.24), gives
\[
\begin{split}
 \|h_H\|_{L^2}
   &<10^{-4}\|f_H\|_{L^2H^{1/3}}+.011\|g_H\|,\\
 \|\operatorname{Tr}h_H\|
   &<\frac1{32}\|f_H\|_{L^2H^{1/3}}+\frac{24}{5}\|g_H\|.
\end{split}
\tag{P.39}
\]
Here \(f_H\) may also be the complete head-driven high source.
All powers in the frame and source are explicit; there is no
root-distance factor \(\delta^{-1/4}\) in these contracts.

## 8. Pay the complete finite head and its genuine high feedback

Set \(P_L={\bf1}_{|j|\le96}\).
The complete moving operator and exact band are those of
R133-supplement-complete-moving-band-and-mean-parameter-Schur.md.
In raw moving \(L^2\), the following bounds hold on this same interval:
\[
\begin{gathered}
 \|d\|_\infty<2,\quad\|d_\phi\|_\infty<5,\quad
 \|L_0\|<31,\\
 \|-\beta Q_\phi I(2u\,\cdot+2Kv\,\cdot)\|<163,\qquad
 \|\gamma\langle h_2\rangle JQ_\phi\|<49 .
\end{gathered}                                                       \tag{P.40}
\]
For the first, the complete mean-zero primitive on a circle of length
\(\pi/2\) has \(L^\infty\) norm at most \(\pi/8<2/5\);
multiply this by \(\|d_\phi\|_\infty<(9/5)(13/5)\).
For the primitive nonlocal part use its \(L^2\) norm \(1/4\),
\(\|Q_\phi\|_\infty\le27+86\), and
\(\|(u,Kv)\|_\infty\le8/5+(61/100000)(9/5)\).
The true mean rank estimate follows directly from its displayed row.

The radial principal matrix commutes with the head projection.
The mean rank term has no high output and no high-input mean.
Taking an adjoint when needed to put a derivative on the finite
head yields the complete cross bounds
\[
 \|\mathcal A_{HL}\|_{L^2\to L^2}<962,\qquad
 \|\mathcal A_{LH}\|_{L^2\to L^2}<967.                   \tag{P.41}
\]
For example the first is \(4(96)\cdot2+31+163\); the second adds
the full \(d_\phi\) fee 5. No crossing mode is discarded.

The high output of \(\mathcal A_{HL}\) has indices \(97\le|j|\le160\).
Since \(\langle640\rangle^{1/3}<9\),
\[
 \|\mathcal A_{HL}\|_{L^2\to H^{1/3}}<8658.             \tag{P.42}
\]
The complete head generator itself has norm less than
\[
       4(96)(201/100)+4(96)2+31+212<1800.               \tag{P.43}
\]
This includes both unprojected mean rows; in the actual reflection
class the odd mean is the explicit symmetry constraint.

Consequently the complete finite-angle **radial Cauchy** operator has
\[
 G_L\le h(51/50),\qquad P_L^\partial\le\sqrt h(51/50),
\tag{P.44}
\]
because \(e^{1800h}<51/50\).
It is an actual all-radial operator bound, proved by Gronwall, not a
collocation or QR assertion.

Now solve the exact coupled equations
\[
\begin{split}
 h_L&=P_L^\partial g_L+
       G_L(f_L+\mathcal A_{LH}h_H),\\
 h_H&=P_H^\partial g_H+
       G_H(f_H+\mathcal A_{HL}h_L).
\end{split}
\tag{P.45}
\]
Here \(g_L=h_L(r_*)\) specifies both low rows.
The actual complete return has bound
\[
 \rho\le h(51/50)(967)(10^{-4})(8658)
       =\frac{1921439637}{250000000000}<\frac1{100}.
\tag{P.46}
\]
A second Neumann inversion closes the **complete** head/high system.
The \(\nu\) source, all means and the full allowed independent source
columns are in (P.45). The actual centre residual is supported in
the head, but arbitrary ordinary sources are not assumed to be.

For clarity, a sufficient complete response matrix, with input order
\((\|f_L\|,\|f_H\|_{H^{1/3}},\|g_L\|,\|g_H\|)\), is
\[
\begin{array}{c|rrrr}
 \|h_L\|_{L^2}&10^{-5}&10^{-6}&.0031&.0001\\
 \|h_H\|_{L^2}&.0000087&.000102&.00269&.0111 .
\end{array}                                                       \tag{P.47}
\]
Every entry is checked by exact rational arithmetic. The source
column sum and the Euclidean port matrix bound give (P.2).
The actual band implies that only head indices \(33,\ldots,96\)
directly meet high indices, but all paths from those indices back
to the inner core and the mean remain in (P.45).

## 9. Complete endpoint outputs and angular regularity

The low right trace follows from its exact Cauchy equation:
\[
 \|h_L(r_*+h)\|
 <\frac1{250}\|f\|+
       \frac{103}{100}\|g_L\|+\frac{17}{500}\|g_H\|.
\tag{P.48}
\]
Its left trace is exactly \(g_L\). Apply the complete high trace
estimate (P.39) to \(f_H+\mathcal A_{HL}h_L\):
\[
 \|\operatorname{Tr}h_H\|
 <\frac7{200}\|f\|+\frac{21}{25}\|g_L\|
                         +\frac{483}{100}\|g_H\| .
\tag{P.49}
\]
The finite-dimensional Euclidean estimates in the native give (P.3)
from (P.48)–(P.49). Both low means and both high state rows are outputs.

The same high realization has an explicit angular regularity
bootstrap. Replace \(Z_j\) by \(M^sZ_j\), \(s=0,1,2\).
The logarithmic frequency bound becomes \(s+5/3\).
Valid sufficient constants for the drift, relative-frame difference,
and primitive term are respectively
\[
 (6,3,4),\qquad(18,9,8),\qquad(48,24,16).
\]
Thus the exact whole remainder bounds are
\[
 E_s=(c_s+\tfrac12)54+68
       +\frac{8d_s(32)(1336)}{97}
       +\frac{n_s(9/5)(3700)}{65}.                      \tag{P.50}
\]
The executed rational gates give
\[
        hE_0<1/8,\qquad hE_1<1/3,\qquad hE_2<5/6.
\]
Their resolvents are bounded by \(8/7,3/2,6\).
The \(H^s\) source in raw moving units is \(H^{s+1/3}\), exactly as
(P.24) specifies. This is not a free same-index source claim.

After (P.45) is solved at base order, its finite head is angularly
smooth. For supplied high data of the stated regularity, apply the
same high inverse with the complete finite head forcing. For example
\[
 \|\mathcal A_{HL}h_L\|_{H^{s+1/3}}
       \le8658\,641^s\|h_L\|_2,\qquad
 \|h_L\|_{H^s}\le385^s\|h_L\|_2.
\]
Uniqueness of the base solution identifies this higher-regularity
solution with the one already obtained; no second head inversion or
unpaid Fourier-tail hypothesis is needed. The pointwise-radial
version follows from the same two contraction kernels and
Cauchy--Schwarz. Interpolation gives intermediate Sobolev orders.

## 10. Mean, parameter, physical ports, and exact scope

The zero mode never enters \(M^{-1/3}\) or a limiting Airy formula.
It is part of the complete low Cauchy problem (P.43)–(P.45).
In the actual reflection tangent space there is one allowed even
mean; the unrestricted algebra preserves the two mean rows before
that explicit symmetry restriction.

The scalar metric parameter has its complete column, including the
reference derivatives and true mean, as proved in the complete-band
theorem. On this root germ the compact metric bump vanishes.
This does not delete its source in the negative body. Globally the
scalar parameter row and the genuine external regular rows still
belong to the full BVP Schur problem.

The present state is a variation of the moving nonlinear unknown.
Its original physical-angle variation and physical moments use the
already proved full variation map and (B.14)–(B.19) of the
complete-band theorem. The passive physical fold at a nonzero-residual
centre is a different operator unless its residual-sensitive bridge
is paid. This theorem supplies no such free identification.
If a parameter differentiates the moving endpoint \(r_*(\eta)\),
the corresponding endpoint-motion source must likewise be included.

There are no PPoly joins inside (P.1). When attached outside it,
the actual moving affine joins and full physical boundary rows must
still be supplied. The right high unstable port has not been set to
zero by an unproved exterior regular graph. The negative incoming
return, the remaining positive body, global \(\nu\) Schur denominator,
and nonlinear contraction remain outstanding.

## 11. Source and new executed exact report

The standalone source is
scripts/fourfold_codazzi_current_positive_root_Riccati_budget.mjs.
The report is
notes/2026-11-13-R133-current-moving-positive-root-Riccati-native.json.
It contains 62 passed BigInt rational gates, full input text-blob
identities, domain, all coefficient envelopes, high and complete
head/high contraction fractions, source and both trace outputs.

This is a new computation from previously proved outward text
bounds. It does not read or recreate an old binary native report.
The only old-object numbers consumed are the expressly identified
intrinsic \(K'\) bounds of the identical target germ.
The current nonradial bounds all come from the current ac1d centre.

Reproduction needs a standard Node runtime:
\[
 \texttt{node scripts/fourfold_codazzi_current_positive_root_Riccati_budget.mjs
 --out notes/2026-11-13-R133-current-moving-positive-root-Riccati-native.json}.
\]
The same exact arithmetic was executed in the available pure
JavaScript runtime before this result was recorded.
