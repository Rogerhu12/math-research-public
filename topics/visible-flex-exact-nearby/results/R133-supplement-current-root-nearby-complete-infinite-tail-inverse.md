# R133 supplement: the complete positive-root inverse in an actual infinite-tail neighbourhood

2026-11-14, phase_inverse. **Proved; all 43 new exact rational gates
were executed and passed.**

This is a neighbourhood theorem for the actual complete moving centre
\[
 \mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}.
\]
It adds the whole head-to-high and high-to-head operators to the
all-frequency frame theorem. The background may have an arbitrary
unknown Fourier tail. The complete mean, all ordinary source columns,
and both endpoint outputs are retained.

Let \(Q_c=(u_c,v_c)\) be that centre. On the actual root interval
\[
 I_\eta=[r_*(\eta),r_*(\eta)+h],\qquad h=9/10^6,             \tag{N.1}
\]
take any real odd/even background
\[
 Q=Q_c+q,\qquad
 \sup_{r\in I_\eta}\|q(r)\|_{A^3}\le\rho\le10^{-6},
 \quad
 \|q\|_{A^3}=\sum_{k\in4\mathbb Z}(1+|k|)^3
                    (|q_{1,k}|+|q_{2,k}|).              \tag{N.2}
\]
The even mean is included in this norm. The weight in (N.2) is the
same polynomial Wiener weight as in the all-frequency frame theorem;
it has not been replaced by a Bessel weight with the same radius.
Radially measurable bounded coefficients suffice for the linear
construction; continuous backgrounds give the usual continuous
coefficient formulation.

For the exact moving derivative at \(Q\), and the ports specified
in Section 5, the complete local solution satisfies
\[
 \|z\|_{L^2(I_\eta;L^2_\phi)}
 <\frac1{8000}\|f\|_{L^2(I_\eta;H^{1/3}_\phi)}
        +\frac3{250}\|g\|,                              \tag{N.3}
\]
\[
 \|\operatorname{Tr}_{r_*,r_*+h}z\|_{L^2_\phi\oplus L^2_\phi}
 <\frac1{25}\|f\|_{L^2(I_\eta;H^{1/3}_\phi)}
        +\frac{27}{5}\|g\|.                             \tag{N.4}
\]
Every frequency is present. The cutoff is \(|j|\ge97\), \(k=4j\),
and the retained reflection head has 193 coordinates. This is an
actual inverse on the interval (N.1), uniformly for the whole
original \(|\eta|\le10^{-9}\).

A complete once-differentiated estimate is also proved below.
It has source order \(H^{4/3}_\phi\), includes the infinite
head-driven output, and uses the same high resolvent \(15/13\).
A second angular derivative and a same-space nonlinear contraction
are not asserted. The rest of the positive body, the negative
return, physical boundary matching and scalar parameter Schur
remain separate parts of the global BVP.

## 1. Actual inputs and the new radial principal reference

The input results, with text blob identities, are:

* The current actual germ:
  [current moving physical complex germ](R133-supplement-current-moving-body-physical-complex-germ.md),
  blob \(\mathtt{bfe73ee59142618bc7e36d5e3fe06929d9fb68cb}\).
* The complete centre root inverse:
  [positive root, Riccati reference and full head](R133-supplement-current-moving-positive-root-Riccati-and-full-head.md),
  blob \(\mathtt{3edf335784786da9a4a515b28d364d8ad2914e24}\).
* The single reference compatible with the exterior:
  [global positive reference and current collar](R133-supplement-global-positive-reference-and-current-collar.md),
  blob \(\mathtt{5e89a2ec36f36f2852d47738bc46373fdacf67d1}\).
* The complete signed-frequency perturbation estimate:
  [all-frequency frame and infinite-tail neighbourhood](R133-supplement-all-frequency-frame-and-infinite-tail-neighbourhood.md),
  blob \(\mathtt{f07df1671d97116a78050b14dfb717d18b86a407}\).

The root interval is inside the same actual PPoly piece 2549 and
the same target germ for every allowed \(\eta\). Its complete
domain check is the one in P.4–P.6 and G.1–G.4; changing the
background in (N.2) does not change the intrinsic target or move
the interval outside that already proved domain.

Write \(m_c=\langle v_c\rangle\), \(m=\langle v\rangle\).
The actual centre envelopes include
\[
\begin{gathered}
 -m_c>1.1197077044,\quad |m_c|<1.119807069,\\
 0.5025436590<-\gamma m_c<2.004892,\qquad
 |\beta|<9/5,\quad0<\gamma<9/5,\\
 59.74380437<K'<60.465470,\qquad
 0\le K<61/100000 .
\end{gathered}                                                       \tag{N.5}
\]
Consequently the **new actual speed**
\[
                    a_Q=-\gamma m                     \tag{N.6}
\]
still lies in \((1/2,201/100)\). The native checks these two strict
margins using \(|m-m_c|\le10^{-6}\). In particular \(m<0\).
The centre's complete bound
\(\|v_c-m_c\|_\infty<0.599103154(-m_c)\) also gives
\(v<-2/5\), while \(|m|<28/25\). Thus the real moving angular
Jacobian \(v/m\) remains positive. This last fact does not itself
supply a norm for the physical variation map.

For each \(Q\), construct the global positive Riccati reference
using (N.6) on (N.1), an arbitrary positive bounded radial extension
outside it, and the same fixed positive outer reference Robin
datum as in the global-reference theorem. There is no claim that
this extension is the actual speed outside the certified collar.
On the collar, its optical coordinate satisfies \(29<K_s<122\).
The complete scalar functions \(p_M,g_M\), \(M=|k|\ge388\), have
\[
 W_M=p_M+g_M<4,\quad K/W_M<1,\quad
 W_M\ge\tfrac12M^{-1/3},\qquad
 |\partial_{\log M}\log p_M|,\ 
 |\partial_{\log M}\log g_M|\le1 .                       \tag{N.7}
\]
The complete root Airy two-row comparison remains 9.
All these estimates are uniform over the allowed extension.

The principal change
\(\gamma\langle q_2\rangle J(K)\partial_\phi\) is absorbed exactly
into (N.6). It is never estimated as a bounded angular operator.
When estimating coefficient differences, both the centre
coefficients and the new coefficients are put into this one new
reference. The centre coefficient proof was uniform under
(N.7), so its constant remains
\[
                         E_c=18262183/1261.             \tag{N.8}
\]

## 2. Exact derivative and the entire high-to-high part

Here and below
\[
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad
 I=\partial_\phi^{-1}P_{\ne0},\quad
 S=u^2+Kv^2,\quad d=-\beta I S.
\]
The actual moving derivative is
\[
\begin{split}
 {\cal A}_Q z={}&(dI_2+\gamma mJ)z_\phi+L_Qz
       -2\beta Q_\phi I(uz_1+Kvz_2)
       +\gamma\langle z_2\rangle JQ_\phi,\\
 L_Q={}&
 \begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
 -2\beta uv&\beta(1-u^2-3Kv^2)
 \end{pmatrix}.
\end{split}                                                        \tag{N.9}
\]
This identity holds at a background with nonzero residual.
No step assumes that \(Q\) already solves the nonlinear equations.

Let \(P_L={\bf1}_{|j|\le96}\), \(P_H=1-P_L\). At nonzero high
frequencies use the exact state
\[
 Z_k=M^{1/6}T_M^{-1}S_\sigma z_k,\quad
 T_M=W_M^{-1/2}\begin{pmatrix}p_M&-g_M\\1&1\end{pmatrix},
 \quad S_\sigma=\operatorname{diag}(-i\sigma,1).
                                                               \tag{N.10}
\]
The source and reconstruction bounds remain
\[
            \|F_Z\|_2\le3\|f_H\|_{H^{1/3}},\qquad
            \|z_H\|_2\le3\|Z\|_2 .                    \tag{N.11}
\]
They commute with angular derivatives.

The all-frequency input proves, including opposite signs and every
low nonzero intermediate primitive frequency,
\[
 \|\Delta{\cal E}\|\le6174\rho+108\rho^2<6200\rho,        \tag{N.12}
\]
\[
 \|[\partial_\phi,\Delta{\cal E}]\|
       \le796446\rho+108\rho^2<800000\rho.              \tag{N.13}
\]
Adding the differentiated skew-transport lower term increases the
first triangular constant by less than \(810000\rho\).
The exact scalar operator
\(P_H(d\partial_\phi+d_\phi/2)P_H\) stays in the skew part.
There is no bound for a bare composition minus identity, and no
assumption that any intermediate Fourier mode stays high.

The rank-one last term of (N.9) is exactly zero on high input
because that input has zero mean. Its output on low input is
generally infinite and is paid in the next section.
The other terms can have high-to-mean rows in (N.2); none is
deleted.

The executed gates give
\[
 h(E_c+6200\rho)<2/15,\qquad
 h(E_c+6200\rho+5+110\rho)<2/15 .                        \tag{N.14}
\]
The diagonal stable/unstable reference with the exact skew
transport has Green norm at most \(h\) and port norm at most
\(\sqrt h=3/1000\). Thus both the base high equation and the
highest part of its first angular derivative retain resolvent
\(15/13\). In raw units this gives
\[
\begin{split}
 \|z_H\|_{L^2_rL^2_\phi}
    &<10^{-4}\|F_H\|_{L^2_rH^{1/3}_\phi}
                                +.011\|g_H\|,\\
 \|\operatorname{Tr}z_H\|
    &<\tfrac1{32}\|F_H\|_{L^2_rH^{1/3}_\phi}
                                +\tfrac{24}{5}\|g_H\|.
\end{split}                                                        \tag{N.15}
\]
Here \(F_H\) may be the complete head-driven source.

Existence on the infinite high space follows by the same
Galerkin energy and density construction used for the reference
theorem. The new drift has the required real \(C^1\) regularity
by (N.2), its projected symmetric transport is skew, and
(N.12) is a complete bounded operator perturbation.
The first derivative estimate below supplies a dense smooth
uniqueness class. The bounds then extend by density to the
stated ordinary source and port spaces.

## 3. Complete head/high differences with no support restriction

Only the centre has degree 32. For the following estimates use
\[
\begin{gathered}
 \|u_c\|_\infty<1.6,\quad \|v_c\|_\infty<1.8,\quad
 \|u_{c,\phi}\|_\infty<27,\quad\|v_{c,\phi}\|_\infty<86,\\
 \|Q_{c,\phi}\|_\infty<113,\qquad
 \|Q_{c,\phi\phi}\|_\infty<38656 .
\end{gathered}                                                       \tag{N.16}
\]
The final bound is \(128(216+86)\), from the complete centre
Fourier sums. All component derivatives of \(q\) through order
three have supremum at most \(\rho\).

### 3.1 Local multiplication

The sum of the four absolute entry differences in \(L_Q\) is at most
\[
 |\beta|\{4|\Delta u^2|+4K|\Delta v^2|
                      +2(1+K)|\Delta(uv)|\}.
\]
Using
\[
 |\Delta u^2|\le3.2\rho+\rho^2,\quad
 |\Delta v^2|\le3.6\rho+\rho^2,\quad
 |\Delta(uv)|\le3.4\rho+\rho^2
\]
gives
\[
 \|\Delta L\|_\infty<36\rho,\qquad
 \|\partial_\phi\Delta L\|_\infty<840\rho.               \tag{N.17}
\]
For the derivative bound the corresponding three bounds are
\(57.2\rho+2\rho^2\), \(175.6\rho+2\rho^2\), and
\(116.4\rho+2\rho^2\).

Multiplication by a matrix with supremum \(a\) and derivative
supremum \(b\) has \(L^2\) norm at most \(a\) and \(H^1\) norm at
most \(a+b\). Hilbert Sobolev interpolation therefore gives
\[
 \|M_{\Delta L}\|_{H^{1/3}\to H^{1/3}}
 \le(36^2\cdot876)^{1/3}\rho<105\rho.                   \tag{N.18}
\]
The finite head has \(H^{1/3}\) norm at most \(8\) times its
\(L^2\) norm. Hence this contribution to the actual
\(L^2_L\to H^{1/3}_H\) source is \(<840\rho\).

### 3.2 Complete drift

The supremum estimate for \(P_{\ne0}\) pays its full factor 2:
\[
       \|\Delta d_\phi\|_\infty<12\rho.
\]
The periodic primitive on a circle of length \(\pi/2\) has
supremum norm at most \(\pi/8<2/5\), so
\[
       \|\Delta d\|_\infty<5\rho.                     \tag{N.19}
\]
Interpolation of its \(L^2\) and \(H^1\) multiplication norms gives
\[
       \|M_{\Delta d}\|_{H^{1/3}\to H^{1/3}}<8\rho,
 \qquad 5^2\cdot17<8^3 .                              \tag{N.20}
\]
The head derivative has norm at most 384. Thus the low-to-high
\(H^{1/3}\) source difference is \(<24576\rho\).
For high-to-low, take an adjoint and put the derivative on the
finite low test function. This gives
\[
 \|P_L\Delta d\,\partial_\phi P_H\|_{L^2\to L^2}
 <(384\cdot5+12)\rho=1932\rho.                         \tag{N.21}
\]
This argument includes arbitrary high tails and arbitrary signs.

### 3.3 Complete primitive and the new infinite mean column

Put \(W_c=(u_c,Kv_c)\), \(\Delta W=(q_1,Kq_2)\).
The entire primitive difference is
\[
 \Delta{\cal N}=-2\beta\{
       q_\phi I(W_c\cdot\,\cdot)
       +Q_{c,\phi}I(\Delta W\cdot\,\cdot)
       +q_\phi I(\Delta W\cdot\,\cdot)\}.               \tag{N.22}
\]
Here
\(\|W_c\|_\infty<1.602\), \(\|\Delta W\|_\infty\le\rho\).
On the full fourfold circle
\[
 \|I\|_{L^2\to L^2}=1/4,\qquad
 \|I\|_{L^2\to H^1}=\sqrt{17}/4<17/16 .
\]
It follows that
\[
 \|\Delta{\cal N}\|_{L^2\to L^2}<104\rho,\qquad
 \|\Delta{\cal N}\|_{L^2\to H^1}<150000\rho.             \tag{N.23}
\]
For clarity the latter upper bound before rounding is
\[
 \frac{18}{5}\frac{17}{16}
 \bigl(2(1.602)\rho+(113+38656)\rho+2\rho^2\bigr).
\]
Interpolating the output spaces, with the same \(L^2\) input,
gives the complete infinite-output estimate
\[
 \|\Delta{\cal N}\|_{L^2\to H^{1/3}}<1200\rho,\qquad
                    104^2\cdot150000<1200^3.           \tag{N.24}
\]
No cutoff is placed on its output.

The remaining mean column changes by
\(\gamma\langle z_2\rangle Jq_\phi\).
Its \(L^2\to H^{1/3}\) norm is at most \((9/5)\rho<2\rho\),
by (N.2). This is an actual infinite-output column.
It is zero only when the input mean is zero.

Combining (N.18)–(N.24) yields
\[
\begin{split}
 \|\Delta{\cal A}_{HL}\|_{L^2\to H^{1/3}}
       &<26618\rho,\\
 \|\Delta{\cal A}_{LH}\|_{L^2\to L^2}
       &<2072\rho .
\end{split}                                                        \tag{N.25}
\]
The new radial principal coefficient commutes with \(P_L,P_H\).
Consequently it creates no cross term in (N.25).

The old complete centre bounds were \(8658\) and \(967\).
At the actual radius \(10^{-6}\), we therefore have
\[
 \boxed{\quad
 \|{\cal A}_{HL}\|_{L^2\to H^{1/3}}<8659,\qquad
 \|{\cal A}_{LH}\|_{L^2\to L^2}<968 .
 \quad}                                                           \tag{N.26}
\]
This is not a support assertion. In particular a high mode can
now couple directly to the inner head or mean.

## 4. Close the whole head and every high-feedback path

The old padded head generator was
\[
       384(201/100)+384(2)+31+212=1782.84 .
\]
A conservative bound for its change, even also paying the radial
mean change separately, is
\[
 \{384(5)+36+104+2+384(9/5)\}\rho<2754\rho .
\]
Thus the full new head generator is still \(<1800\).
Its actual all-radial Cauchy solution has
\[
 G_L\le h(51/50),\qquad P_L^\partial\le\sqrt h(51/50).   \tag{N.27}
\]
Indeed \(e^{1800h}\le(1-1800h)^{-1}<51/50\).
This is a full finite-angular radial estimate, not a collocation
inverse or a finite QR claim.

Solve the exact equations
\[
\begin{split}
 z_L&=P_L^\partial g_L+
           G_L(f_L+{\cal A}_{LH}z_H),\\
 z_H&=P_H^\partial g_H+
           G_H(f_H+{\cal A}_{HL}z_L).
\end{split}                                                        \tag{N.28}
\]
The full feedback has the actually computed bound
\[
 h\frac{51}{50}\,968\,10^{-4}\,8659
          =\frac{480912201}{62500000000}<\frac1{100}.   \tag{N.29}
\]
This closes every head/high path, including every new mean path.
The two Neumann operations here are a high equation on its full
Hilbert space and then the complete head Schur equation on the
same radial spaces. No finite section is identified with the
infinite inverse.

With input order
\((\|f_L\|,\|f_H\|_{H^{1/3}},\|g_L\|,\|g_H\|)\),
the following complete response matrix is still valid:
\[
\begin{array}{c|rrrr}
 \|z_L\|_{L^2_rL^2_\phi}&10^{-5}&10^{-6}&.0031&.0001\\
 \|z_H\|_{L^2_rL^2_\phi}&.0000087&.000102&.00269&.0111 .
\end{array}                                                       \tag{N.30}
\]
Every entry is checked using the new \(968,8659\) numbers.
The sum of source-column bounds and the Frobenius port bound
give (N.3).

The head right trace, its exact left trace, and the two complete
high endpoint states obey respectively
\[
\begin{split}
 \|z_L(r_*+h)\|&<
 .004\|f\|+1.03\|g_L\|+.034\|g_H\|,\\
 z_L(r_*)&=g_L,\\
 \|\operatorname{Tr}z_H\|&<
 .035\|f\|+.84\|g_L\|+4.83\|g_H\|.
\end{split}                                                       \tag{N.31}
\]
The explicit Euclidean combination of these rows gives (N.4).
In particular both mean outputs remain part of the unrestricted
algebra; odd/even symmetry then restricts the odd mean to zero.

## 5. The precise local ports and source permissions

The low datum is the complete \(P_Lz(r_*)\).
In the reflection class it has 193 real coordinates, including
the even mean. The two high incoming data are
\[
                       g_H=(Z_s(r_*),Z_u(r_*+h)),       \tag{N.32}
\]
in the actual background-dependent reference (N.10).
The stable and unstable labels refer to the two exact radial
Riccati columns. These are independent inputs.

Thus one has the correct number of local boundary conditions.
One has not set both full high Cauchy states to zero at the left
and then imposed a further regular condition at the right.
The high outgoing ports and both raw moving states are outputs
of (N.31).

The radius in (N.2) does not identify the new ports with the old
centre ports by a free small composition or frame difference.
The uniform bounds use the precisely specified new reference.
For matching to other blocks one uses its full state reconstruction
and the raw outputs; a fixed external boundary equation has to
be transformed in that same reference.

The ordinary source in (N.3) is a genuine \(L^2_rH^{1/3}_\phi\)
source for the moving derivative (N.9). It can have arbitrary
Fourier support and arbitrary allowed mean. A metric parameter
column, endpoint-motion column or physical residual source is
included when expressed in this actual source space. The compact
\(\nu\) bump vanishes on the root germ, but this does not remove
its global mean or parameter equation. The local theorem does
not silently convert a physical-angle Jacobi source into (N.9).

There are no PPoly joins within (N.1). All genuine affine joins
outside it remain interface inputs when this block is assembled.
The true exterior nonlinear mean row, including its high-to-low
finite-rank path, is also an external equation; (N.29) does not
delete that row or solve the global scalar Schur.

## 6. A full first angular bootstrap, including the unknown output tail

Let
\[
                  \|a\|_{B_s}=\sum_k(1+|k|)^s|a_k|.
\]
For \(s\ge0\), multiplication has \(H^s\) norm at most \(B_s\),
because
\(\langle k+n\rangle\le(1+|k|)\langle n\rangle\).
This allows direct control of the now infinite low-to-high
output at source order \(H^{4/3}\).

The centre-only support conversions are
\[
 \|u_c\|_{B_{1/3}}<78,\quad
 \|v_c\|_{B_{1/3}}<10.8,\quad
 \|u_c\|_{B_{4/3}}<8580,\quad
 \|v_c\|_{B_{4/3}}<1188,\quad
 \|Q_{c,\phi}\|_{B_{4/3}}<199320.                        \tag{N.33}
\]
Here \(129^{1/3}<6\), \(129^{4/3}<660\).
For the unknown \(q\), (N.2) directly pays all required
\(B_{4/3}\) and \(B_{7/3}\) norms. The arithmetic below uses
the harmless larger bound \(2\rho\), without giving \(q\)
the centre's finite support.

The complete polynomial products and the full primitive give
\[
 \|\Delta d\|_{B_{4/3}}<706\rho,\qquad
 \|\Delta L\|_{B_{4/3}}<320000\rho .                    \tag{N.34}
\]
For the first inequality use
\(\|\Delta S\|_{B_{1/3}}<313\rho\) and
\((1+|k|)/|k|\le5/4\) for nonzero fourfold \(k\).
For the second use the exact local polynomial differences in
Section 3 with (N.33).

The head has \(H^{4/3}\) norm at most \(3000\) times \(L^2\).
Applying the full \(I:H^{4/3}\to H^{4/3}\) norm \(1/4\)
to (N.22) gives a head-to-\(H^{4/3}\) bound
\(<1123000000\rho\) for the primitive difference.
The mean-rank difference contributes \(<4\rho\).
Hence
\[
 \|\Delta{\cal A}_{HL}\|_{L^2\to H^{4/3}}
 <
 \bigl(706(384)(3000)+320000(3000)
                      +1123000000+4\bigr)\rho
 <3\cdot10^9\rho .                                    \tag{N.35}
\]
Every output frequency is included in this estimate.

For the centre alone the old finite output estimate was
\(8658\cdot641\). Consequently
\[
             \|{\cal A}_{HL}\|_{L^2\to H^{4/3}}
                         <5560000 .                   \tag{N.36}
\]
Only the centre term uses 641. Equation (N.35) pays the actual
unknown tail separately.

After solving (N.28) once, put
\[
\begin{gathered}
 L=\|z_L\|_{L^2_rL^2_\phi},\quad
 X_0=\|Z\|_{L^2_r\ell^2},\quad X_1=\|\partial_\phi Z\|_{L^2_r\ell^2},\\
 F_0=\|f_H\|_{L^2_rH^{1/3}},\quad
 F_1=\|f_H\|_{L^2_rH^{4/3}},\\
 G_0=\|g_H\|,\quad G_1=\|\partial_\phi g_H\|.
\end{gathered}
\]
The exact once-differentiated equation has the same resolvent
\(15/13\), by (N.14), and lower-order coefficient
\[
          4538112+810000\rho<4538113 .
\]
Therefore
\[
\begin{split}
 X_0&\le\frac{15}{13}
       \{3h(F_0+8659L)+\sqrt h\,G_0\},\\
 X_1&\le\frac{15}{13}
       \{3h(F_1+5560000L)+\sqrt h\,G_1
                                  +h(4538113)X_0\}.
\end{split}                                                       \tag{N.37}
\]
These are chronological lower-order forcing terms. They are not
new Gronwall exponents and they do not require a second head
inversion.

Raw reconstruction yields the explicit complete estimate
\[
 \|z\|_{L^2_rH^1_\phi}
                  \le385L+3(X_0+X_1).                 \tag{N.38}
\]
The complete angular derivative of the high endpoint output also
obeys
\[
 \|\operatorname{Tr}\partial_\phi z_H\|
 \le\frac1{32}(F_1+5560000L)
       +\frac{24}{5}G_1+\frac{27}{2600}(4538113)X_0 .
                                                               \tag{N.39}
\]
For the low endpoint output multiply its \(L^2\) trace bound
by 385. Together with (N.4), this gives both complete raw
\(H^1\) endpoint states.

One can justify (N.37) first for smooth Fourier approximation
to \(q\) and smooth data, using the uniform \(A^3\) bounds.
Weak compactness and uniqueness of the base inverse identify
the limit with (N.28). This also proves the estimate when
the given \(A^3\) tail has no extra smoothness.
Interpolation supplies the intervening angular orders with
the corresponding source and port orders.

A second commutator would need additional coefficient regularity.
Neither the old finite-band \(H^2\) constants nor an analytic
strip is inferred for the entire ball (N.2).

## 7. Scope, executable source, and the new report

This proves the complete current moving positive-root inverse
in the genuine infinite-tail neighbourhood (N.2). It includes
both signs, all low/high feedback, the full primitive,
the new infinite mean column, all allowed means, ordinary
sources and the complete two-end raw outputs.
The complete once-differentiated source contract is (N.37)–(N.39).

It does not solve the remaining positive interval, the
negative-side return, the full physical regular boundary graph,
the scalar \(\nu\) equation, or a nonlinear iteration. In
particular the moving physical variation map at a nonzero
residual centre still requires its own already identified
residual-sensitive source terms. Uniform local inverses in
these source spaces do not by themselves give a nonlinear
same-space contraction.

The standalone source is
[scripts/fourfold_codazzi_current_root_nearby_infinite_tail.mjs](../scripts/fourfold_codazzi_current_root_nearby_infinite_tail.mjs).
The complete executed report is
[notes/2026-11-14-R133-current-root-nearby-infinite-tail-rational.json](../notes/2026-11-14-R133-current-root-nearby-infinite-tail-rational.json).

The source's complete arithmetic function was run in the
available JavaScript runtime. All 43 normalized BigInt rational
gates passed, including the actual speed margins, the complete
cross blocks, the exact feedback fraction (N.29), all four
output constants (N.3)–(N.4), and the infinite-output
\(H^{4/3}\) source budget. This computation only consumes
identified, previously proved text envelopes. It neither reads
a binary report into the conversation nor recreates a lost
native candidate cache.

Reproduction requires only Node:
\[
 \texttt{node scripts/fourfold_codazzi_current_root_nearby_infinite_tail.mjs
 --out notes/2026-11-14-R133-current-root-nearby-infinite-tail-rational.json}.
\]
