# 真角上的两行根 Cauchy 迹准确配平

在 GDM 的同一原真实族、$n=4|j|\ge388$ 上，以原自由试探的根两行本身解一个物理角矩阵。记 $w=1/n$，$c=(D_rT)_*$，$u=(D_ra_0)_*$，$a=(D_ra_1)_*=(D_ra_1^V)_*$，$b=b_1|_*$，$b_r=(D_rb_1)_*$。$c$ 为正径向常数。置 $V=\mathcal B(0)$、$V_1=\mathcal B'(0)$、$\gamma=b+V$、$\gamma_r=b_r+c V_1+Vu$、$A=u+wa$。$V,V_1$ 为原频率和有限族的标量，$a$ 随 $\epsilon=\operatorname{sgn}j$ 变号。令
\[
 M_F=\begin{pmatrix}1&w^2 b\\ A&c+w^2 b_r\end{pmatrix},\quad
 M_G=\begin{pmatrix}1&w^2\gamma\\ A-w^2 c V\gamma&c+w^2\gamma_r\end{pmatrix},
 \quad J_0=\det M_F=c+w^2 d_0+w^3 d_1,\quad
 d_0=b_r-bu,\quad d_1=-ba .
 \tag{GRT.1}
\]
此处 $J_0$ 是标量行列式。原变系数角逆仍记 $J_*$。[SE.9–15](R133-supplement-natural-stable-port-Fredholm-and-exact-reference-elimination.md) 的真实根归一给未投影的原高度和 $D_r$ 导迹，分别为 $M_FF_n(0)$ 与 $M_GF_n(0)C_n$，并且 $X_*=\phi,D_rX_*=0$。在下述完整有向差距门成立时，新的真实两列系数为
\[
 {\cal L}_n(\phi)=F_n(0)^{-1}M_F(\phi)^{-1}M_G(\phi)F_n(0)C_n .
 \tag{GRT.2}
\]
在负侧用原自由标量试探的原两列右乘 $\mathcal L_n(X(r,\phi))$，再取 $P$ 和 WUA.40–41 的完整两状态与独立均值。因 $D_r\mathcal L_n(X)|_*=0$，其未投影两行根值等于真正的两行。再取相同 $P$ 和 $J_*(D_0-B_{\rm op})$、两次相同的零均值初值，根两物理状态**精确相等**。GDM.6 应沿用原正侧实际有定义的输入（特别是原自然终端 Ai）；全根差 $\delta h_*=0$，独立 $e^+-P_F h^G$ 保留。完整负侧的普通、跳和腰端必须使用这一个配平试探，不能将新根的零与另一试探的体源相拼。[整件有向替换](R149-supplement-exact-root-matched-right-matrix-and-signed-physical-trial-exchange.md)

## 角变化部分实际比常值右矩阵多三分之四阶

记 $L_n$ 为 GDM.1 的常角矩阵，写
\[
 M_GD(0)-M_F=
 \begin{pmatrix}0&-w^4 S\\-w^2 T_1&-w^3 H+w^4 W\end{pmatrix},\qquad
 S=V_1\gamma,\quad T_1=cV\gamma,\quad H=Va,\quad
 W=cV^2\gamma-V_1\gamma_r .                                \tag{GRT.3}
\]
所有量在同一 $\phi$、同一 $n$ 及原参数上相乘。用
\[
 U=AS+W=-V_1d_0-cV_1^2+cV^2\gamma+w V_1a\gamma,\qquad
 F_*=\operatorname{diag}(1,n^{-2/3})F_n(0)
\]
得到完整精确展开
\[
 n^{8/3}(\mathcal L_n-L_n)=F_*^{-1}
 \begin{pmatrix}
 w^{4/3}bT_1/J_0&
 -w^{2/3}S+w^{5/3}bH/J_0-w^{8/3}bU/J_0\\
 -T_1/J_0&-w^{1/3}H/J_0+w^{4/3}U/J_0
 \end{pmatrix}F_*L_n .                                     \tag{GRT.4}
\]
证明是把 $F_n(0)C_n=D(0)F_n(0)L_n$ 代入 GRT.2，严格照矩阵顺序乘 $M_F^{-1}$。真实 Airy 初值与同一 Wronskian 给 $\|F_*^{-1}\|\|F_*\|\le\pi(m(0)+m_1(0))<5/2$，使用 GIV 的 $m(0)<(18/25)^2$、GDM 的 $m_1(0)<69/250$。连同 $\|L_n\|<6/5$，左右常矩阵的联合费用严格小于 $3$。因此额外角乘子本身为 $O(n^{-8/3})$。对 $r$、物理角或波算子求导时，$\partial_X\mathcal L_n$、$\partial_X^2\mathcal L_n$ 和所有已有有向源仍必须保留。

## 原整文件上的首个数值门

在 $s=1/512$ 取归一 Wiener 导数权 $A_k(p)=\sum_h |p_h|(4|h|)^k e^{4s|h|}/k!$。用原完整背景、原 leading 两条及首修正次数 $0,1$ 的有向 Fourier 系数求 $d_0,d_1$。$D_rb=-\partial_\rho b-d\partial_\phi b$ 含实际漂移；对 $a_0,a_1$ 的角漂移因 SE.9 的根恒等式准确为零。原完整复 $z$ 正方形用一次带全部 $\pm1,\ldots,\pm96$ 的径向三角反演给出 $V,V_1$，分别为 $V(z,0),V_T(z,0)/3$。相同 $V$ 的 $\gamma$ 与 $U$ 的完整有限带号组合先合成再计各阶范数。$N=388$，置 $e_k=N^{-2} A_k(d_0)+N^{-3} A_k(d_1)$。若 $g=\inf c-e_0>0$，则 $b_0^*=1/g$，并可递归取
\[
 b_k^*=\frac1g\sum_{i=1}^k e_i b_{k-i}^*,\qquad 1\le k\le4 .
 \tag{GRT.5}
\]
这是对 $J_0^{-1}$ 于整条物理角和全 \(n\) 的统一逐 Fourier 系数绝对包络的 Wiener 导数界。零阶以 $e_0/c<1$ 的正卷积几何级数证明，再对 $J_0J_0^{-1}=1$ 求归一导。全频带可共用这一同号包络，因 $w^p\le N^{-p}$ 始终在各原输入列上。对于 GRT.4 的四个矩阵位置按同样的正卷积传播各阶，再将四个费用求和，最后只乘一次 $3$。所得结论控制 $\sum_h e^{4s|h|}(4|h|)^k\sup_n\|n^{8/3}(\mathcal L_n-L_n)_h\|/k!$，可在随后对每个物理移频逐一应用，而非只给每个 $n$ 各自分开的 Wiener 范数。

公开入口只读接受的 23 整件和原共同势收据，回报真实 $g$、逆与 GRT.4 的零至四阶完整数值以及修正小于 $1/100$、$1/10$ 两门。若 $g$ 门失败则只返回有向差距，保留原 GDM 的真根两行。全域自由普通源的实际径向传播不含于本次根矩阵预算。
