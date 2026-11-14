# 少于平衡长度的主池：全部出生的真实三层特征、硬源回归与完整相位

日期：2026-11-14；工作标识：789f。

## 0. 模型与本稿给出的准确接口

取 \(Q\ge1\) 个外部 Boolean 位，其正权平方为 \(z_1,\ldots,z_Q\)。
取整数 \(0\le d\le Q/2\)，另加一个权为 \(1\)、长度
\[
                         q_0=Q-2d
\]
的真实相等权主池，并限制到主池的对称 reducing 模块。总长度为
\(2s=2(Q-d)\)。在这个模块中，保留整个低 primitive 源
\[
 V=\ker D\cap{\cal H}_{s-1}
\]
和整个硬 primitive 源
\[
 U=\ker D\cap{\cal H}_s.
\]
主池长度可以为 \(0\)；此时就是原来的 \(Q=2d\) 个外部位，没有另加物理位。

本稿把两个完整源及相位的全部 Gram 写成同一乘积 Bernoulli 积分，并准确保留硬源回归。\(d=0\) 恰回已经研究的平衡 star；\(d=1\) 才首次接入外部出生 \(2\)。这里得到的是完整身份，没有声称一般 \(d\) 的统一相位常数已经支付。

令 \({\cal P}_j\) 为外部 \(Q\) 个变量的多线性齐次次数 \(j\) 空间，
\[
 \partial=\sum_{i=1}^Q\partial_{x_i},\qquad
 {\cal K}_j=\ker\partial\cap{\cal P}_j.
\]
定义两个固定系数源
\[
 {\cal E}_d=\ker\partial^3\cap{\cal P}_{d+1},
                    \qquad {\cal U}_d={\cal K}_d.        \tag{0.1}
\]
它们不依赖 \(z\)。以下将证明它们分别与整个物理 \(V,U\) 同构，并给出同构的真实度量；不会把这个代数同构免费当作等距。

使用原始乘积
\[
 F(t)=\prod_{i=1}^Q(1-t+z_it),\qquad
 {\cal Z}=\int_0^1F(t)\,dt,\qquad \rho(t)=F(t)/{\cal Z},
\]
\[
 X_i\mid T=t\quad\hbox{独立 Bernoulli},\qquad
 \mathbb P(X_i=1\mid T=t)=\frac{z_it}{1-t+z_it}.
                                                               \tag{0.2}
\]
对 \(\phi\in{\cal E}_d\)，置
\[
                       \psi_\phi=\partial\phi-2\phi.    \tag{0.3}
\]
在下面准确指定的可积特征上，记正形式
\[
 \langle f,g\rangle_d
       =\mathbb E_\rho\left[
           [T(1-T)]^{-d}\overline{f(X)}g(X)\right].       \tag{0.4}
\]
当 \(d>0\) 时，(0.4) **不是** 一个在所有常数函数上有限的概率内积；只在实际的 \(\psi_\phi\)、硬特征及其线性组合上使用。端点可积性在 §4 证明。

任取 \({\cal E}_d\) 的完整基和 \({\cal U}_d\) 的完整基
\(\chi_\alpha\)，定义矩阵
\[
 H_{\phi,\widetilde\phi}
 =\mathbb E\left[
 [T(1-T)]^{-d}\frac{1-T}{T}
       \overline{\phi(X)}\widetilde\phi(X)\right],
\]
\[
 L_{\phi,\widetilde\phi}
 =\mathbb E\left[
 [T(1-T)]^{-d}\frac{T}{1-T}
       \overline{\phi(\mathbf1-X)}
                  \widetilde\phi(\mathbf1-X)\right],    \tag{0.5}
\]
\[
 B_{\phi,\widetilde\phi}
        =\langle\psi_\phi,\psi_{\widetilde\phi}\rangle_d,
 \quad M_{\alpha\beta}=\langle\chi_\alpha,\chi_\beta\rangle_d,
 \quad C_{\alpha\phi}=\langle\chi_\alpha,\psi_\phi\rangle_d,
\]
\[
                  R=C^*M^{-1}C,\qquad G=(B-R)/4.        \tag{0.6}
\]
Then \(H,L,M,G\) are strictly positive definite and the actual full phase is
\[
                  J=HG^{-1}L-2G-R,\qquad
                  \Phi=H^{-1/2}J^*L^{-1}JH^{-1/2}.      \tag{0.7}
\]
The formulas (0.5)–(0.7) preserve the full inverse on each source. In particular,
\(M^{-1}\) is the inverse on the entire hard primitive space, not a scalar or a selected subspace.

All physical Gram matrices equal the displayed ones multiplied by the same scalar
\[
                         c=\frac{(q_0+1){\cal Z}}
                                      {\prod_i z_i}.    \tag{0.8}
\]
This common scalar cancels from (0.7). The rest of the proof establishes these assertions.

## 1. Exact primitive coordinates and their birth content

Use the polynomial model for the symmetric main pool. Its monomial \(x_0^k\)
has squared norm \(1/\binom{q_0}{k}\), and its deletion operator is
\(\partial_{x_0}\). An external monomial \(x_I\) has squared norm \(1\).
Put \(b_i=\sqrt{z_i}\), \(y_i=x_i/b_i\), \(y_0=x_0\). Thus
\[
 D=\partial_{y_0}+\sum_i\partial_{y_i},\qquad
 \|y_0^k y_I\|^2=\frac{z_I^{-1}}{\binom{q_0}{k}}.        \tag{1.1}
\]
Different monomials are orthogonal in this actual physical metric.

Every homogeneous primitive polynomial of degree \(n\) is uniquely determined
by its value \(f(y)\) at \(y_0=0\):
\[
 P_f(y_0,y)=f(y-y_0\mathbf1)
          =\sum_{k\ge0}\frac{(-y_0)^k}{k!}\partial^k f(y).
                                                               \tag{1.2}
\]
It belongs to the main-pool module exactly when
\[
                              \partial^{q_0+1}f=0.      \tag{1.3}
\]
This follows directly by solving \(\partial_{y_0}P=-\partial P\);
the degree bound in \(y_0\) is precisely (1.3).

For a multilinear homogeneous polynomial \(\phi=\sum_{|I|=p}\phi_Ix_I\),
write its coefficient complement as
\[
                        f_\phi(y)=
                          \sum_{|I|=p}\phi_Iy_{I^c}.     \tag{1.4}
\]
The outside coefficient complement exchanges unweighted deletion
\(\partial\) and creation \(e=\sum_i x_i(1-x_i\partial_{x_i})\).
For \(p=d+1\), (1.3) is therefore
\(e^{Q-2d+1}\phi=0\).

For completeness, the ordinary Boolean \(\mathfrak{sl}_2\) strings show
\[
 \ker e^{Q-2d+1}|_{{\cal P}_{d+1}}
               =\ker\partial^3|_{{\cal P}_{d+1}}.       \tag{1.5}
\]
Indeed, on the string starting at \({\cal K}_j\), degree \(d+1\) has height
\(d+1-j\), and the total string length is \(Q-2j\). The displayed power of \(e\)
vanishes exactly for \(j\ge d-1\), which is also exactly when
\(\partial^3\) vanishes. These are the actual unweighted Boolean strings;
no general Hodge assertion is being applied to a physical norm.

For \(p=d\), the same argument gives
\[
                       \ker e^{Q-2d+1}|_{{\cal P}_{d}}
                                   ={\cal K}_d.         \tag{1.6}
\]
Equations (1.2), (1.4) consequently give the asserted complete isomorphisms
\[
              \phi\in{\cal E}_d\longmapsto P_{f_\phi}\in V,
 \qquad \chi\in{\cal K}_d\longmapsto P_{f_\chi}\in U.     \tag{1.7}
\]

The exterior birth content of \(V\) is exactly \(j=d-1,d,d+1\), omitting
strings absent at the degree in question; \(U\) uses exactly exterior birth
\(d\). These are algebraic string decompositions. At unequal physical
weights their Gram cross terms are retained throughout (0.5)–(0.7);
the decomposition is not asserted to be orthogonal.

With binomial coefficients outside their usual range interpreted as \(0\),
\[
 \dim V=\binom Q{d+1}-\binom Q{d-2},\qquad
 \dim U=\binom Qd-\binom Q{d-1}.                          \tag{1.8}
\]
For \(d=0\), \(V\) has dimension \(Q\) and \(U\) dimension \(1\):
only exterior births \(0,1\) can occur. For \(d=1\), the dimensions are
\(\binom Q2\) and \(Q-1\), and exterior birth \(2\) first appears.
For \(q_0=0\), (1.7) is still valid and describes the full original
even Boolean source rather than an auxiliary extension.

## 2. The complete source Gram by a Beta integral

Let \(p=d+1\) and \(v_\phi=P_{f_\phi}\). If the main-pool degree is \(k\)
and the external occupied set is \(J\), set \(A=J^c\). Then
\[
             |A|=p+k,\qquad
 [y_0^k y_J]v_\phi=(-1)^k\phi(\mathbf1_A).                \tag{2.1}
\]
This is the direct expansion of the product in (1.2). Formula (1.3)
guarantees that coefficients with \(k>q_0\) vanish.

By (1.1),
\[
 \langle v_\phi,v_{\widetilde\phi}\rangle_{\rm phys}
   =\frac1{\prod_i z_i}
       \sum_A
       \frac{z_A\,\overline{\phi(\mathbf1_A)}
                         \widetilde\phi(\mathbf1_A)}
            {\binom{q_0}{|A|-p}},                       \tag{2.2}
\]
where only \(p\le |A|\le p+q_0\) is included. The exact identity
\[
 \binom{q_0}{k}^{-1}
        =(q_0+1)\int_0^1 t^k(1-t)^{q_0-k}\,dt           \tag{2.3}
\]
transforms (2.2) into
\[
 \frac{q_0+1}{\prod_i z_i}
 \int_0^1 F(t)\,
     t^{-p}(1-t)^{q_0+p-Q}
       \mathbb E[\overline{\phi(X)}
                    \widetilde\phi(X)\mid T=t]\,dt.
\]
Here
\[
 t^{-p}(1-t)^{q_0+p-Q}
         =[t(1-t)]^{-d}\frac{1-t}{t}.
\]
This proves the physical source Gram \(h=cH\) with \(c\) from (0.8).
The same argument at central degree \(s\), now \(p=d\), gives the
hard primitive Gram \(m=cM\).

The finite-sum formula (2.2), not a formal singular density, is the starting
point. Thus no divergent endpoint integral is silently subtracted.

## 3. The dual creation column and its full hard projection

Let
\[
                     {\mathfrak e}
       = E_{0,\mathrm{pool}}^*+\sum_i b_i^{-1}E_i^*
\]
be the true reciprocal-weight creation. In the \(y\)-coordinates it is
the ordinary bounded-degree creation
\[
 q_0y_0-y_0^2\partial_{y_0}
       +\sum_i y_i(1-y_i\partial_{y_i}).
\]
For \(v\in V\),
\[
                              D{\mathfrak e}v=2v.       \tag{3.1}
\]

At central degree, let again \(A=J^c\), now \(|A|=d+k\). Direct creation
of (2.1) gives
\[
 [y_0^k y_J]{\mathfrak e}v_\phi
       =(-1)^k\bigl[(\partial\phi)(\mathbf1_A)
                                  -2\phi(\mathbf1_A)\bigr].
                                                               \tag{3.2}
\]
To verify the coefficient \(-2\) explicitly, external creation contributes
\[
 \sum_{i\notin A}\phi(\mathbf1_{A\cup\{i\}})
       =(Q-|A|-p)\phi(\mathbf1_A)
                          +(\partial\phi)(\mathbf1_A).
\]
Main-pool creation contributes
\(-(q_0-k+1)\phi(\mathbf1_A)\). Since
\(|A|=d+k,\ p=d+1,\ q_0=Q-2d\), their scalar sum is \(-2\).

Applying (2.3) at central degree proves the joint physical Gram
\[
       \operatorname{Gram}_{\rm phys}
         \bigl((P_{f_{\chi_\alpha}})_\alpha,
                             ({\mathfrak e}v_\phi)_\phi\bigr)
           =c\begin{pmatrix}M&C\\C^*&B\end{pmatrix}.     \tag{3.3}
\]
Thus projection on the **whole** actual hard space \(U\) gives
\[
 \operatorname{Gram}_{\rm phys}(P_U{\mathfrak e}v_\phi)
                                  =c\,C^*M^{-1}C=cR.   \tag{3.4}
\]

The full map \(D:{\cal H}_s\to{\cal H}_{s-1}\) is onto on this reducing
module. Its kernel is \(U\). Let \({\cal J}_1=D^\dagger|_V\) be its true
minimum-norm preimage. Equation (3.1) implies
\[
                   (I-P_U){\mathfrak e}|_V=2{\cal J}_1.
\]
The full Moore–Penrose Gram is consequently
\[
           \operatorname{Gram}_{\rm phys}({\cal J}_1v_\phi)
                             =\frac c4(B-R)=cG.        \tag{3.5}
\]
The surjectivity is the ordinary Boolean string fact transported by the
invertible positive diagonal deweighting; it does not assert a physical
orthogonal decomposition into those transported strings.

Since \({\cal J}_1\) is injective on \(V\), (3.5) also proves \(G>0\).
No order of a compression and an inverse has been exchanged.

## 4. Endpoint integrability and the exact top Gram

The hard polynomials satisfy
\[
                      \chi(\mathbf1-x)=(-1)^d\chi(x).
\]
For \(\phi\in\ker\partial^3\cap{\cal P}_{d+1}\), the finite Taylor identity
gives
\[
 \phi(\mathbf1-x)=(-1)^{d+1}
            [\phi(x)-\partial\phi(x)+\tfrac12\partial^2\phi(x)],
\]
\[
                       \psi_\phi(\mathbf1-x)
                                   =(-1)^{d+1}\psi_\phi(x).       \tag{4.1}
\]
Hard features have least degree \(d\); \(\psi_\phi\) also has least degree
\(d\). Under independent Bernoulli probabilities of order \(t\), their
squared expectations are \(O(t^d)\). By (4.1) the corresponding estimate
at \(t=1\) is \(O((1-t)^d)\). Thus (0.4) is finite on the joint feature space
used in (3.3).

For \(H\), \(\phi\) has least degree \(d+1\), which pays \(t^{-d-1}\)
at the left endpoint. At the right endpoint, (4.1) has least degree
at least \(\max(d-1,0)\), which pays \((1-t)^{1-d}\).
The same argument by reflection proves integrability of \(L\).
These statements are for each actual finite polynomial; no bound on the
dimension is being inferred from these endpoint orders alone.

Now let \({\cal C}\) be the physical subset complement on all \(2s\) bits,
including the main pool, and let
\[
 {\cal D}|I\rangle=\Bigl(\prod_{i\in I}b_i\Bigr)|I\rangle,
 \qquad P=\prod_{i=1}^Q b_i.
\]
Main-pool weights are \(1\). The exact top normalized preimage is
\[
 {\cal J}_2
    =\left(\frac{D^2}{2}\right)^{-1}\bigg|_V,\qquad
 {\cal J}_2v
       =\frac{(-1)^{s-1}}P\,{\cal C}{\cal D}^2v.         \tag{4.2}
\]
This is an inverse between the complete equal-dimensional layers
\({\cal H}_{s+1}\) and \({\cal H}_{s-1}\), hence the genuine
Moore–Penrose inverse as well.

A direct verification of (4.2) is useful. Deweighting gives
\(D={\cal D}^{-1}d_0{\cal D}\), while
\({\cal D}{\cal C}{\cal D}=P{\cal C}\). For an unweighted primitive
\(v_0\) of degree \(s-1\),
\[
                         \frac{d_0^2}{2}{\cal C}v_0
                                     =(-1)^{s-1}v_0.   \tag{4.3}
\]
Indeed, the coefficient at a set \(J\) of size \(s-1\) is the sum of
coefficients \((v_0)_I\) over \(I\cap J=\varnothing\).
Inclusion–exclusion over subsets of \(J\) kills every proper subset
by \(d_0v_0=0\); only \(I=J\) remains, with sign \((-1)^{s-1}\).
This proves (4.3), and conjugating proves (4.2).
Invertibility on the complete layers follows from the actual unweighted
Boolean strings, and is preserved by deweighting and the symmetric-pool
reducing restriction.

Taking the norm in (4.2) changes the source norm to the reciprocal-weight
source norm, with factor \((\prod_i z_i)^{-1}\).
Applying (2.2)–(2.3) there, then replacing \(T\) by \(1-T\), gives
\[
                 \operatorname{Gram}_{\rm phys}
                       ({\cal J}_2v_\phi)=cL.           \tag{4.4}
\]
In particular the appearance of \(\phi(\mathbf1-X)\) in (0.5) and the
ratio \(T/(1-T)\) are forced by the true top inverse, not chosen to obtain
a convenient positive form.

## 5. The full noncommutative phase and equal-weight calibration

In the inherited physical Hilbert space \(V\), put
\[
 \Gamma_1={\cal J}_1^*{\cal J}_1,\qquad
 \Gamma_2={\cal J}_2^*{\cal J}_2,\qquad
 R_{\rm phys}={\mathfrak e}^*P_U{\mathfrak e}|_V.
\]
The actual even-pool phase operator used in the preceding reductions is
\[
                {\cal H}_0=\Gamma_1^{-1}\Gamma_2
                                      -2\Gamma_1-R_{\rm phys}.   \tag{5.1}
\]
For a nonorthogonal coordinate basis with source Gram \(h\), preimage Grams
\(g,\ell\) and projected Gram \(r\), its quadratic-form matrix is exactly
\[
                           h g^{-1}\ell-2g-r.           \tag{5.2}
\]
For example, the coordinate operator of \(\Gamma_1\) is \(h^{-1}g\);
substitution into (5.1) gives (5.2) in the displayed order.

Equations (2.2), (3.4)–(3.5), (4.4) give
\[
                           h=cH,\quad g=cG,\quad
                           \ell=cL,\quad r=cR.
\]
Thus (5.2) is \(cJ\), with \(J\) as in (0.7), and
\[
 {\cal H}_0^*\Gamma_2^{-1}{\cal H}_0\preceq\kappa I_V
        \quad\Longleftrightarrow\quad
                           J^*L^{-1}J\preceq\kappa H.   \tag{5.3}
\]
This verifies both endpoint metrics and the ordered product \(HG^{-1}L\).

At equal weights \(z_i=1\), reciprocal creation is ordinary physical
creation \(D^*\). On this true spin \(1\) source,
\[
 \Gamma_1=\tfrac12 I_V,\qquad
 \Gamma_2=I_V,\qquad P_UD^*|_V=0.
\]
Therefore, in the same coefficient basis,
\[
                         \boxed{H_0=L_0=2G_0,\qquad R_0=0.}     \tag{5.4}
\]
The subscript here denotes equal weights, not the operator \({\cal H}_0\).
The actual equal-weight phase is the identity. This calibration retains
the full hard spin \(0\) space and its orthogonality to the raised spin \(1\)
space; it is not a scalar approximation.

For \(d=0\), \({\cal E}_0={\cal P}_1\), \({\cal U}_0=\mathbb C\), and
\(\psi_\phi=\partial\phi-2\phi\).
Projection in (3.3) removes its constant mean, so \(G=\operatorname{Cov}X\)
in the linear-feature coordinates and \(R=yy^*\). Thus all formulas reduce
exactly to the previous balanced-star \(H,G,L,J\).

## 6. What a higher-birth estimate must preserve

The new feature system displays the next actual budget without dropping
its nuisance space. For \(d=1\), the hard source is all exterior harmonic
linear functions, of dimension \(Q-1\); its inverse \(M^{-1}\) must remain
inside the same joint Gram with the quadratic \(\psi\)-features.
For general \(d\), the nuisance is the full \({\cal K}_d\), not only a
constant or a few collective columns.

The already proved bounded-positive-weight balanced-star theorem covers
\(d=0\). It does not by itself control (0.7) for \(d\ge1\).
In particular, adding a balanced main pool does not insert arbitrary old
births into its spin \(1\) source: §1 gives the exact restriction.

Conversely, (0.1)–(0.7) are genuine finite product-integral formulas on
coefficient spaces of degrees at most \(d+1\). They make it possible to
attempt a dimension-free fixed-\(d\) comparison of the **entire**
\(({\cal U}_d,\psi)\) Gram, together with the two actual endpoint forms,
and then take its full Schur complement. Any such new comparison must
retain the same \(\psi\), the same hard projection and the same physical
normalization; separate scalar or diagonal estimates do not establish
(5.3).
