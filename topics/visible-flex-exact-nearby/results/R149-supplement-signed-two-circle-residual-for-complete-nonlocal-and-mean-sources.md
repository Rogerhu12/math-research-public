# R149 GNJ. Signed two-circle residual for the entire nonlocal source and its independent physical mean

This is an exact a posteriori identity on the original old-angle circle, followed by a typed operator estimate. It replaces the separate positive bounds on the two occurrences of $R_QJ$ in [G.12–13](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md) with one signed residual. It does not give an actual numerical bound until the complete new residual operators have been received. The original $J$, physical means, reflection class, radial variable and both genuine reference columns are unchanged.

## GNJ.1. Combine the same inverse before any norm

Use $A=\eta\partial_\phi+L$, $J=A^{-1}$ and all projected operators from [U.1–11](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md). Denote the physical background field by $v_{\rm bg}$ to distinguish it from the new inverse trial. Thus $c_B=-2\beta K$, $R_Q=T_{r_Q}+S_Q$ and
\[
 S_V=S_V^0+R_QJB_{\rm op},\qquad
 S_V^0=-R_{t_Q,b_0}-R_{b_0,d_\phi}+T_{t_Q}N_B
       -(N_B)_r+c_B\mathcal C((v_{\rm bg})_\phi,v_{\rm bg})-KS_{AC}.
 \tag{GNJ.1}
\]
The derivative $(N_B)_r$ includes all three terms of U.4. All multiplications retain their original intervening projections.

For either genuine amplitude $w_j$, define $h_j,y_j,g_j,q_j$ by G.10. Include its actual input power in the map $F_w$: it is $n^{7/6}\mathcal U_j^V(w_0)$ for the leading amplitude and $n^{1/6}\mathcal U_j^V(w_1^V)$ for the correction, with $n=4|j|$. Form the corresponding maps $F_h,F_y,F_g,F_q$ with exactly the same power. Write
\[
 f=PF_w,\quad h=PF_h,\quad g=PF_g,\quad
 e=g-Lh-B_{\rm op}f,\qquad v=Je.
 \tag{GNJ.2}
\]
These are operators on the same original input, so the equations also hold after adding the two density orders. In particular one can add them with signs before measuring any residual. G.11 gives the full reconstructed first row $h_1=h+v$ and $h_2=f$.

Define the following complete known operator, which contains no $J$:
\[
\begin{split}
 K_w={}&S_V^0 f-S_Qh-c_BT_{(v_{\rm bg})_\phi}IPF_q
       +P(r_Q)\Pi F_h+c_BP((v_{\rm bg})_\phi)\Pi F_y\\
 &+\{c_BT_{(v_{\rm bg})_\phi}I(Pv_{\rm bg})+P(T_0)\}\Pi F_g
       -P(V_0)\Pi F_w.
\end{split} \tag{GNJ.3}
\]
Every displayed scalar mean is the physical old-angle mean. The vector $T_{(v_{\rm bg})_\phi}I(Pv_{\rm bg})$ multiplies the mean. The equality $\Pi F_W=\Pi F_g$ used here is precisely G.14, including its full amplitude derivative, rather than an assumed vanishing mean. Expanding G.12–13 and collecting its two inverse terms now gives the exact complete nonlocal source
\[
             \mathcal N^V(w)=K_w-R_Qv.                 \tag{GNJ.4}
\]
Indeed those two terms are $R_QJB_{\rm op}f-R_QJ(g-Lh)=-R_QJe$. This cancellation uses the same physical inverse and the same input column. It would be lost if the two terms were replaced by separate scalar upper bounds first.

## GNJ.2. Two finite trials, with every error left in its true space

Choose any finite real operator trial $v^\circ$ in the domain of $A$ with the required nonmean parity. Let
\[
       q=Av^\circ-e.
 \tag{GNJ.5}
\]
There is no invertibility claim about the finite method that selects the trial. The exact inverse implies $v=v^\circ-Jq$. Let $\ell$ be the **entire** local scalar source G.9 for the combined amplitude. Define
\[
 k=\ell+K_w-R_Qv^\circ.
\]
Choose a second finite nonmean trial $t^\circ$ in the appropriate domain of $A$, and form its complete residual $p=At^\circ-k$. The true first physical source row then satisfies
\[
       g_1=t^\circ-Jp+JR_QJq .                         \tag{GNJ.6}
\]
Both $q$ and $p$ are signed sums before taking norms. They include all finite Fourier coefficients and the infinite angular and input tails of their own operators. A retained finite projection alone does not certify either residual.

Let $\mathscr H$ be the original normalized real input space, keeping both signs and the two independent reference coefficients. On the same actual radial circle let
\[
 J:H^{-8/3}\longrightarrow H^{-5/3}\text{ have norm }j_0,
 \quad J:H^{-5/3}\longrightarrow H^{-2/3}\text{ have norm }j_1,
 \quad R_Q:H^{-5/3}\longrightarrow H^{-5/3}\text{ have norm }r_1.
\]
These are the original one-gain windows of U.25 and G.18; a bound on $J:L^2\to L^2$ is not substituted. Suppose the complete new operator bounds are
\[
 Q\ge\|q:\mathscr H\to H^{-8/3}\|,\quad
 P_1\ge\|p:\mathscr H\to H^{-5/3}\|,\quad
 T_1\ge\|t^\circ:\mathscr H\to H^{-2/3}\|.
\]
Then (GNJ.6) gives
\[
       \|g_1:\mathscr H\to H^{-2/3}\|
       \le T_1+j_1P_1+j_1r_1j_0Q .                    \tag{GNJ.7}
\]
The multiplier $r_1$ is charged only to the actual first inverse residual, not to the norm of a large independent leading particular. The complete old coefficients may still make $r_1$ large. This theorem supplies no smallness without an actual sufficiently small $Q$.

The actual independent even-mean source is
\[
 g_2=2\beta m\,\Pi\{u(h+v)+K(v_{\rm bg}-m)f\}.
\]
Form its signed trial
\[
 g_2^\circ=2\beta m\,\Pi\{u(h+v^\circ)+K(v_{\rm bg}-m)f\}.
\]
Because $Jq$ is nonmean, its exact difference is $-2\beta m\Pi(uJq)$. Duality on the normalized circle yields
\[
 \|g_2-g_2^\circ:\mathscr H\to\mathbb R\|
 \le 2|\beta m|\,\|Pu\|_{H^{5/3}}j_0Q .             \tag{GNJ.8}
\]
The constant output carries the same Bessel norm in the two relevant windows. This pays the physical mean of the chosen reconstructed trial; it does not remove an independent supplied mean source, root port or boundary row.

## GNJ.3. Physical reception and an implementable residual order

All quantities above are formed at one original physical $r$ before radial integration. On a closed radial slab suppose complete uniform bounds for the right sides of (GNJ.7) and (GNJ.8), including $\|g_2^\circ\|$, are $b_{1i},b_{2i}$. The two physical output rows are orthogonal, so their ordinary $L^2(dr)$ source norm is at most
\[
       \left(\sum_i |I_i|(b_{1i}^2+b_{2i}^2)\right)^{1/2}.
\]
An already proved pointwise source-to-waist map may instead be integrated directly in $L^1(dr)$, with its actual row units and original common input normalizer. Every cell must lie in that map's certified physical window. Different interfaces and endpoints remain separate distributional inputs.

For finite genuine input bands the signed Laurent construction of [GLW](R149-supplement-signed-Laurent-terminal-column-and-physical-shift-reception.md) supplies a suitable representation. The physical output label of coefficient $h$ is still $k=\epsilon j+h$. Every primitive is division by $4ik$ only for $k\ne0$; its zero coefficient is removed by the actual $P$ and any requested mean is taken before that removal. A band crossing an exceptional $k=0$ must be split or its exceptional labels handled explicitly. All coefficient products are noncircular convolutions. The two residuals in (GNJ.5–6), with these physical frequency labels and the original right normalization, can be received without postulating that a truncated matrix inverse equals $J$. The true $J$ appears only through the proved correction identities and their typed bounds.

This proves the complete residual reduction, including all five old means and the independent physical mean. Its numerical consumers, the whole finite and infinite input bounds, the remaining negative-domain bulk, positive feedback, all independent ports and the full closed-family acceptance remain unpaid.
