# R133 supplement: exact leading-matrix factorization of the complete transport source

2026-11-15, visible-exact / phase_inverse.

**Status: analytic identity proved; no new numerical bound is asserted.** This supplement factors the transport amplitude in L.13 before taking any norm. It uses the same leading matrix, genuine radial columns, input frequency, physical angle, root normalization, and one-sided physical pieces. It does not replace a genuine high boundary-value inverse or remove an independent physical mean.

The primary references are:

- [G: ordered genuine-reference sources and whole-domain correlated forcing](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md), G.2--G.7 and G.17--G.23;
- [P: exact first-local-vector reduction through regular transport](R133-supplement-exact-first-local-vector-reduction-through-regular-transport.md), P.7--P.18;
- [L: correlated second local vector and complete transport amplitudes](R133-supplement-correlated-second-local-vector-and-complete-transport-amplitudes.md), L.1--L.18.

All displayed equalities are identities of complete signed amplitudes for one fixed input label. The physical output Fourier mean remains part of every amplitude.

## 1. The actual leading matrix and two elementary factors

Write $s=i\epsilon$, where $\epsilon=\pm1$, and set
$$
 K=\begin{pmatrix}0&T\\1&0\end{pmatrix},\qquad
 E=E_{12},\qquad J_*=\operatorname{diag}(-1,1),\qquad
 U_\pm=xI\pm s yK,\qquad B_+=x^2+Ty^2.
 \tag{F.1}
$$
Here $x=X_\phi$, $y=T_\phi$, $K^2=TI$, and all products act on the left of column amplitudes. The original exact leading amplitude and matrix are
$$
 a_0=G(x^2-Ty^2),\qquad b_0=-2sGxy,\qquad
 w_0=\binom{a_0}{b_0},\qquad
 M=[w_0,Kw_0]=a_0I+b_0K=G U_-^2.
 \tag{F.2}
$$
Consequently
$$
 U_+U_-=B_+I,\qquad
 U_+M=G B_+U_-,\qquad U_+KM=G B_+U_-K.
 \tag{F.3}
$$
This uses $B_+$ for the principal determinant factor. It does not replace the distinct $x^2-Ty^2$ in $a_0$.

The scalar $\eta$ is independent of the angular variable, and the original physical material derivative is $D=\partial_r-d\partial_\phi$. Define
$$
 \mathcal G_0w=Dw+s\partial_\phi(QKw).
 \tag{F.4}
$$
The derivative in (F.4) acts on the complete product. In particular $Q_\phi$ and $K_\phi=yE$ are retained.

## 2. The exact matrix cancellation

Let $\Xi=c_X/T$ denote the regular quotient from P.18. On the common product, L.13 states
$$
 \mathcal G_0(M)=
 -\frac Q2 U_+(c_TI+s\Xi K)M
 +\frac{Qb_0}{2T}U_+KJ_*
 +s(Q_\phi K+QyE)M.
 \tag{F.5}
$$
The exact fold identity is
$$
 Q_\phi=-\frac Q2\frac yT.
 \tag{F.6}
$$
Both sides extend holomorphically through the root on the original paid product: $y/T=(2/3)A_\phi/A$, with its original nonzero $A$ and fixed branch.

The last two terms of (F.5) have zero diagonal after addition. Their off-diagonal entries are, respectively,
$$
 -\frac{sQG B_+ y}{2},\qquad
 \frac{sQG B_+ y}{2T}.
$$
Thus their complete signed sum, before any absolute value, is
$$
 \frac{Qb_0}{2T}U_+KJ_*+
 s(Q_\phi K+QyE)M
       =-\frac{sQG B_+}{2}\frac yT KJ_*.
 \tag{F.7}
$$
For a direct check, the off-diagonal reduction uses
$xb_0+sya_0=-sG yB_+$; the upper and lower products are kept in their displayed order. No Fourier projection occurs in this calculation.

Combining (F.3) and (F.7) gives the full matrix identity
$$
 \boxed{\displaystyle
 \mathcal G_0(M)=
 -\frac{QG B_+}{2}
 \left\{U_-(c_TI+s\Xi K)+s\frac yT KJ_*\right\}.}
 \tag{F.8}
$$
This is an exact replacement for the separate three summands of L.13. It subtracts no upper bounds.

## 3. Application to the same regular correction

Let $Z=(A,B)^t$ be the normalized correction from P and L, and retain
$$
 b_{\rm reg}=\frac{f_b-B}{T},\qquad
 v=\binom{f_a}{b_{\rm reg}},\qquad
 Z_T=\frac12v-sKZ_X.
 \tag{F.9}
$$
The regular root solution has $B(0,X)=f_b(0,X)$, and $b_{\rm reg}$ is the complete regular integral from P. All paths $s_0T$, $0\le s_0\le1$, must stay inside the same canonical product used there.

The exact $Z_X$ cancellation in L.11, followed by (F.3) and (F.8), yields
$$
 \boxed{\displaystyle
 \mathcal G_0(MZ)=\frac{QG B_+}{2}
 \left\{U_-\big[v-(c_TI+s\Xi K)Z\big]
                      -s\frac yT KJ_*Z\right\}.}
 \tag{F.10}
$$
In particular no separate norm of $Z_X$ is required for this transport amplitude. Its dependence through the exact regular $b_{\rm reg}$ is still present.

For componentwise consumption, put $\mathfrak f=QG B_+/2$. Then (F.10) reads
$$
 \begin{split}
 [\mathcal G_0(MZ)]_a
  =\mathfrak f\{&
       xf_a-sTy\,b_{\rm reg}
       -(c_Tx+Ty\Xi)A
       -s(Tx\Xi-Tc_Ty+y)B\},\\
 [\mathcal G_0(MZ)]_b
  =\mathfrak f\{&
       -syf_a+xb_{\rm reg}
       -(c_Tx+Ty\Xi)B
       -s(x\Xi-c_Ty-y/T)A\}.
 \end{split}
 \tag{F.11}
$$
The fixed leading root anchor gives $y/T=O(T)$ and $\Xi=O(T)$. These are genuine analytic zero factors; (F.11) does not claim that a complete scalar mean vanishes.

## 4. Genuine-column rank term and all companion amplitudes

Let $B_V=H_V^{-1}$ on its already verified genuine old-circle domain and define, in the original order,
$$
 \mathcal Q_V=QV\,B_Ve_1(sy,x),\qquad
 B_VH_D^V=-sQK-n^{-2}\mathcal Q_V .
 \tag{F.12}
$$
For the actual trial $w=w_0+n^{-1}MZ$, the full source amplitude remains
$$
 \begin{split}
 g(w)&=\mathcal G_0w+n^{-2}\partial_\phi(\mathcal Q_Vw)\\
 &=\mathcal G_0w_0+n^{-1}\mathcal G_0(MZ)
   +n^{-2}\partial_\phi(\mathcal Q_Vw_0)
   +n^{-3}\partial_\phi(\mathcal Q_VMZ).
 \end{split}
 \tag{F.13}
$$
Formula (F.10) replaces only its displayed complete transport component. It does not remove the genuine rank term or commute $B_V$ past a scalar differential operator. Every $n^{-1}$ in (F.13) remains attached to the same input label.

Writing the original physical even background as $v_{\rm bg}$, the remaining complete amplitudes are
$$
 \begin{split}
 h(w)&=\eta^{-1}(-sQK-n^{-2}\mathcal Q_V)w,\\
 y_{\rm bg}(w)&=v_{\rm bg}(-sQK-n^{-2}\mathcal Q_V)w,\\
 q(w)&=v_{\rm bg}g(w)
       +s(v_{\rm bg})_\phi QKw
       +n^{-2}(v_{\rm bg})_\phi\mathcal Q_Vw .
 \end{split}
 \tag{F.14}
$$
The symbol $y_{\rm bg}$ distinguishes this nonlocal amplitude from the fold derivative $y=T_\phi$.

Angular derivatives for a subsequent operator budget must be taken on the complete products (F.10)--(F.14), on an explicitly common strip. The existing two primitive windows, all nine nonlocal words, the five old-circle mean terms, the independent physical mean terms, the actual radial measure, the one-sided traces, and every physical seam contribution remain unchanged. A later bound may be intersected with an earlier bound for the same complete operator; no difference of numerical upper bounds is a new correlated estimate.

This supplement proves the identities only. It neither enlarges a paid product nor recomputes a successful scalar enclosure, genuine profile, operator word, source row, or radial integral.
