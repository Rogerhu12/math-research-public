# R133 supplement: complete angular model geometry from the moving residual

2026-11-14, visible-exact-astra-ac0d.

This result concerns the complete original moving centre with index
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
Its model frame is integrated radially from its explicitly specified
orthogonal model anchor. The ordinary residual, its angular derivative,
the genuine even source mean and every original candidate value jump are
retained. No nonlinear solution or actual exterior world anchor is
assumed. The separate continuous repair is not substituted silently.

## 1. Exact differentiated defects

Use the full connection, sources and conventions of
[the moving frame theorem](R133-supplement-moving-frame-with-complete-residual-and-mean.md).
In particular, at every open original polynomial piece,

\[
 Q_r=Q\Omega_r,\qquad F_r=Qf_r,\qquad Q^TQ=I,
\]

and

\[
 E=Q_\phi-Q\Omega_\phi,\qquad P=F_\phi-Qf_\phi.
\]

The complete identities already proved there are

\[
 E_r=E\Omega_r-Q\mathcal R,\qquad
 P_r=Ef_r-Q\mathcal T.                                      \tag{A.1}
\]

The centre has finite angular support, so its piecewise radial model
solution is smooth in the angular variable. Differentiate (A.1) at the
same moving angle, without replacing its genuine angle lift by a solution
of a residual-free transport equation:

\[
\begin{split}
 (E_\phi)_r
 &=E_\phi\Omega_r+E\partial_\phi\Omega_r
        -(Q\Omega_\phi+E)\mathcal R-Q\partial_\phi\mathcal R,\\
 (P_\phi)_r
 &=E_\phi f_r+E\partial_\phi f_r
        -(Q\Omega_\phi+E)\mathcal T-Q\partial_\phi\mathcal T.
                                                               \tag{A.2}
\end{split}
\]

Write the following nonnegative uniform bounds on one closed radial box:

| Symbol | Complete quantity bounded |
| --- | --- |
| \(W,W_1\) | \(\|\Omega_\phi\|,\|\partial_\phi\Omega_\phi\|\) |
| \(A_1\) | \(\|\partial_\phi\Omega_r\|\) |
| \(f,f_1\) | \(|f_r|,|\partial_\phi f_r|\) |
| \(b,b_1\) | \(|f_\phi|,|\partial_\phi f_\phi|\) |
| \(R,R_1\) | \(\|\mathcal R\|,\|\partial_\phi\mathcal R\|\) |
| \(T,T_1\) | \(|\mathcal T|,|\partial_\phi\mathcal T|\) |

All matrix norms here are Euclidean operator norms, not sums over sampled
angles. The supremum is over the complete real angular circle. Because
the homogeneous right action in both frame equations is skew, its
propagator is orthogonal. Thus, measuring travel backwards from the right
endpoint, valid nondecreasing majorants \((e,e_1,p,p_1)\) satisfy

\[
\begin{split}
 e'&=R,\\
 e_1'&=(A_1+R)e+WR+R_1,\\
 p'&=fe+T,\\
 p_1'&=fe_1+(f_1+T)e+WT+T_1.                         \tag{A.3}
\end{split}
\]

The system is triangular. There is no homogeneous growth term in the
first equation and no exponential factor hidden in (A.3).

Set \(a_1=A_1+R\), \(b_1^*=WR+R_1\), and let the box width be \(h\).
For the incoming values \((e_0,e_{1,0},p_0,p_{1,0})\), define

\[
 J_e=he_0+\tfrac12 h^2R,\qquad
 J_{e_1}=he_{1,0}+\tfrac12h^2(a_1e_0+b_1^*)
                         +\tfrac16h^3a_1R.                  \tag{A.4}
\]

The outgoing bounds are exactly

\[
\begin{split}
 e&=e_0+hR,\\
 e_1&=e_{1,0}+h(a_1e_0+b_1^*)+\tfrac12h^2a_1R,\\
 p&=p_0+fJ_e+hT,\\
 p_1&=p_{1,0}+fJ_{e_1}+(f_1+T)J_e+h(WT+T_1).
                                                               \tag{A.5}
\end{split}
\]

These are integrations of constant majorants, not a numerical ODE
solver. Directed arithmetic pays all subsequent additions and products.

## 2. Actual coefficient and complete source bounds

Let \(m=\langle v\rangle<0\). The exact connection is

\[
 \tau=dv/m-\gamma u,\qquad
 (p_r,q_r,t_r)=\left(\frac\beta\gamma\tau,
             a(\gamma Kv+du/m),\frac{ad}{m}\right),
\]

\[
 (A,B,C)=\left(\frac{\beta v}{\gamma m},
                    \frac{au}{m},\frac a m\right),\qquad
 f_r=(a\gamma,a\tau,0),\quad f_\phi=(0,av/m,0).         \tag{A.6}
\]

The notation \((p_r,q_r,t_r)\) in (A.6) labels the three radial
connection coefficients; it does not assert they are derivatives of
three additional fields. The script uses the unambiguous connection
matrix directly.

The angular derivative is obtained from

\[
 \tau_\phi=d_\phi v/m+d v_\phi/m-\gamma u_\phi,\qquad
 (\Omega_\phi)_\phi
 =\Omega\left(\frac\beta{\gamma m}v_\phi,
                     \frac a m u_\phi,0\right).               \tag{A.7}
\]

The residual curvature and torsion, with the full mean
\(R_0=\langle R_v\rangle\), are

\[
 \mathcal R=\Omega\left(
 \frac\beta{\gamma m}(R_v-vR_0/m),
 \frac a m(R_u-uR_0/m),-\frac a{m^2}R_0\right),
\]

\[
 \mathcal R_\phi=\Omega\left(
 \frac\beta{\gamma m}(R_{v,\phi}-v_\phi R_0/m),
 \frac a m(R_{u,\phi}-u_\phi R_0/m),0\right),            \tag{A.8}
\]

\[
 \mathcal T=\left(0,\frac a m(R_v-vR_0/m),0\right),\quad
 \mathcal T_\phi=\left(0,\frac a m(R_{v,\phi}-v_\phi R_0/m),0\right).
                                                               \tag{A.9}
\]

In particular, no pointwise \(1/v\) denominator is introduced by this
geometry calculation. The separate candidate curvature and immersion
claims still require their own full pointwise \(v\)-gap.

The original residual reports enclose the normalized \((U,V)\)
equations. Their \(A^0\) and \(A^1\) bounds must be multiplied by the
exact positive physical amplitude \(\alpha\). The inhomogeneous
\(A^1\) bound also bounds the complete first angular derivative. It
includes the full index-96 residual support and all original intrinsic
remainders. None of the unretained residual modes is removed.

The complete positive cover already supplies all required coefficient
norms. The complete negative cover supplies pointwise bounds for
\(u_\phi,v,v_\phi,d_\phi,m,a,\beta,\gamma,K\). The actual odd
fourfold functions \(u,d\) vanish at every multiple of \(\pi/4\), hence

\[
 \|u\|_\infty\le\tfrac\pi8\|u_\phi\|_\infty,\qquad
 \|d\|_\infty\le\tfrac\pi8\|d_\phi\|_\infty.          \tag{A.10}
\]

The short interval between these two covers is evaluated once, on its
actual common scalar germ and its complete original polynomial piece.
The source uses every one of its 65 real coefficients and the valid
complete primitive bound \(\|IS\|_{A^0}\le\|S\|_{A^0}/4\).
There is no extrapolation of a negative curvature box across the root.

## 3. All genuine candidate interfaces

The model \(Q,F\), and their angular derivatives are continuous across
each radial coefficient interface. The connection and source vectors
can jump. With \(\Delta\) denoting right minus left,

\[
 E_- -E_+=Q\Delta\Omega_\phi,\quad
 (E_\phi)_--(E_\phi)_+
       =Q_\phi\Delta\Omega_\phi+Q\Delta\partial_\phi\Omega_\phi,
                                                               \tag{A.11}
\]

\[
 P_- -P_+=Q\Delta f_\phi,\quad
 (P_\phi)_--(P_\phi)_+
       =Q_\phi\Delta f_\phi+Q\Delta\partial_\phi f_\phi.
                                                               \tag{A.12}
\]

Therefore a backward crossing adds

\[
 \left(j_W,\ (W_++e_+)j_W+j_{W,1},\
              j_f,\ (W_++e_+)j_f+j_{f,1}\right)               \tag{A.13}
\]

to the four incoming bounds. The old incoming \(e_+\) is used in both
second-order fees. The one-sided denominator gaps from both pieces are
retained.

For example, if \(m_*\) bounds both absolute means from below and
\(J_v\) bounds the complete physical jump, then

\[
 |\Delta(v/m)|\le J_v/m_*+VJ_v/m_*^2,\qquad
 |\Delta(v_\phi/m)|\le128J_v/m_*+V_1J_v/m_*^2.          \tag{A.14}
\]

The corresponding \(u\) formula retains the same mean term, and
\(|\Delta(1/m)|\le J_v/m_*^2\). The factor 128 is the largest actual
physical frequency of the complete original candidate jump. It is not
an upper cutoff on an unknown variation. The consumer requires all
6,143 interfaces exactly once.

## 4. The actual model anchor

At \(R=25/8\), let \(\theta\) be the original complete candidate lift,
\(b=\beta/\gamma\), and \(z=-aC_{\rm ref}\). The model anchor is

\[
 F=a e_r(\theta),\quad X=b e_r(\theta)+z e_z,
 \quad Y=e_\theta(\theta),\quad N=z e_r(\theta)-b e_z.   \tag{A.15}
\]

The metric identity gives \(b^2+z^2=1\); this frame is exactly
orthogonal, with the same orientation as the original model producer.
Its angular connection is \(\Omega(bv/m,0,-zv/m)\), so

\[
 E(R)=Q(R)\Omega\left(0,-au/m,
                          aC_{\rm ref}(v-s)/m\right),\qquad
 P(R)=P_\phi(R)=0.                                      \tag{A.16}
\]

Here \(s=C_{\rm ref}^{-1}\), including its complete true parameter
dependence. The right-hand state is evaluated exactly from the last
original cubic, including its even mean. Differentiating (A.16) pays
the additional term \(Q_\phi\Delta\Omega\). In particular,

\[
 \|E_\phi(R)\|\le \|\theta_\phi\|_\infty\|E(R)\|
     +\frac a{|m|}\sqrt{\|u_\phi\|_\infty^2
                  +C_{\rm ref}^2\|v_\phi\|_\infty^2}.       \tag{A.17}
\]

No small boundary mismatch is set to zero. The actual nonlinear exterior
world-frame matching is a separate, still necessary input.

## 5. From the exact angle grid to the entire circle

Differentiating the two angular reconstruction identities gives

\[
 \|F_{\phi\phi}\|\le (W+e)b+b_1+p_1,\qquad
 \|Q_{\phi\phi}\|\le W^2+eW+W_1+e_1.                 \tag{A.18}
\]

For a twice differentiable vector or matrix function on a grid interval
of width \(\delta\), its difference from the linear interpolation of
its two exact endpoint values is at most
\(\delta^2\sup\|f''\|/8\). This follows by the Dirichlet Green kernel
for the second derivative, whose absolute integral at position \(t\)
is \(t(\delta-t)/2\le\delta^2/8\); it holds directly in the Euclidean
or operator norm used here.

For the original exact angular grid,

\[
 \delta=\frac\pi{2\cdot512}.                            \tag{A.19}
\]

Fourfold equivariance is an exact consequence of the complete centre and
the anchor, and is preserved by uniqueness of the radial ODE. The final
grid interval therefore uses the actual quarter-turn of the first grid
value. It is not closed by identifying two unrotated world vectors.

Directed radial integration errors at the grid values are added
separately. A position-radius bound, normal support bound, true model
immersion, actual exterior anchor, exact nonlinear correction, marker
conditions and reach are not inferred from (A.18) alone.

## 6. Complete consumer

`scripts/fourfold_codazzi_moving_geometry_angular_defect.py` consumes the
complete merged original residual, complete strict and positive native
covers, and the original verified candidate index. It intersects their
closed partitions exactly, evaluates the one new root gap, integrates
(A.5), and pays every jump using (A.13). Its report keeps the complete
rowwise budgets, every source identity, the model-anchor data and the
full original scope. The numerical report is to be attached only after
all 7,296 original residual boxes are genuinely available; an unfinished
residual checkpoint is rejected.
