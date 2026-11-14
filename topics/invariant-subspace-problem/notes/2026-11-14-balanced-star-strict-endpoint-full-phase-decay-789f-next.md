# 平衡 star 严格端峰：任意多个宏观小组的完整相位衰减

日期：2026-11-14；工作标识：789f。

## 0. 完整源定理

固定 \(m\geq1\)、正比例 \(\omega_i\)（和为 \(1\)）及正权平方 \(z_i\)。取 \(q_i=Q\omega_i\)，主组长度为 \(Q\)，小组总长度也为 \(Q\)。使用平衡 star reducing 模块的整个 \(m\) 维低 primitive 源及一维硬源。

令
\[
 \ell(t)=\sum_i\omega_i\log(1-t+z_it).
\]
若
\[
 \zeta=\sum_i\omega_i z_i<1,\qquad d=1-\zeta>0,              \tag{0.1}
\]
则 \(\ell\) 严格递减，最大值在 \(t=0\)。在原来的完整源相位
\[
 J_Q=H_QG_Q^{-1}L_Q-2G_Q-y_Qy_Q^*,\qquad
 \Phi_Q=H_Q^{-1/2}J_Q^*L_Q^{-1}J_QH_Q^{-1/2}               \tag{0.2}
\]
上，有
\[
                         \boxed{\|\Phi_Q\|=O(Q^{-2}).}       \tag{0.3}
\]
三个 Gram、硬源项及 \(J_Q\) 的共同物理标量已同时除去；(0.2) 保持正确的 \(L\leftarrow H\) 次序。

若 \(\sum_i\omega_i z_i^{-1}<1\)，则峰在 \(t=1\)，同样有 (0.3)。证明用精确倒数同谱，不重新交换原目标中的两个端点。

常数可以在满足 \(d\geq d_0>0\)、\(\omega_i\geq\omega_0>0\)、\(z_i\) 位于固定正紧区间、组数 \(m\) 固定的 profile 集上一致选取。这里不包括 \(d\to0\) 的过渡层；也不把该定理外推到任意变化组数或任意正权的统一常数。

## 1. 真实模型及端点身份

沿用[内峰完整源稿](2026-11-14-balanced-star-macroscopic-interior-full-phase-projection-limit-789f-next.md)的真实概率模型：
\[
 F_Q(t)=\prod_i(1-t+z_it)^{q_i},\quad
 \rho_Q(t)=F_Q(t)/Z_{F,Q},\quad
 K_i\mid T=t\sim\operatorname{Bin}
      \left(q_i,\frac{z_it}{1-t+z_it}\right),
\]
各组条件独立，\(X_i=K_i/q_i\)。写
\[
 m=\mathbb EX,\ n=\mathbf1-m,\ G=\operatorname{Cov}(X),
\]
\[
 H=\mathbb E\frac{1-T}{T}XX^*,\qquad
 L=\mathbb E\frac{T}{1-T}(\mathbf1-X)(\mathbf1-X)^* .
\]
本稿省略这些有限 \(Q\) 矩阵的下标。令
\[
 Z=\operatorname{diag}(z_i),\quad a=Zn,\quad b=Z^{-1}m,
\]
\[
 D_a=\operatorname{diag}(a_i/q_i),\
 D_b=\operatorname{diag}(b_i/q_i),\
 D_0=\operatorname{diag}(1/q_i).
\]
有准确式
\[
 H=D_a-ZG+am^*,\qquad L=D_b-GZ^{-1}+nb^*,\qquad
 [Z,G]=am^*-ma^*.                                        \tag{1.1}
\]

置
\[
 \alpha=Z_{F,Q}^{-1},\quad
 \beta=\frac{\prod_i z_i^{q_i}}{Z_{F,Q}},\quad
 u_\pm=(Z^{\pm1}-I)q.
\]
由分部积分及完整源导数，
\[
 Gu_+=a-\alpha m,\quad Gu_-=b-\beta n,\quad
 n^*u_+=1-\alpha,\quad m^*u_-=1-\beta,\quad
 u_+^*Gu_-=\alpha\beta-1.                                 \tag{1.2}
\]
这些是同一实际源的关系，没有用抽象双 star 算子去替换加性源。

## 2. 保留端点参数的完全因式分解

对任意标量 \(c>0\)，令
\[
 R=cm-a,\quad S=Z^{-1}R=cb-n,\quad
 h=c-\alpha,\quad k=1-c\beta .
\]
只要 \(h,k\neq0\)，原 \(J\) 有完全准确的恒等式
\[
 \begin{split}
 J={}&nm^*-G-D_0+\frac{c\beta}{k}nn^*
       +\frac{\alpha}{h}mm^*
       +\frac1k nS^*-\frac1h Rm^*\\
   &+\left(D_a+\frac1h aR^*\right)G^{-1}
                       \left(D_b-\frac1k Sb^*\right).       \tag{2.1}
 \end{split}
\]
这保持整个完整逆及非交换次序。

核对方法如下。令 \(\eta=m^*G^{-1}n-1\)。由 (1.2)，
\[
 R^*G^{-1}S=c^2+1-c(\alpha+\beta)-hk\,\eta.
\]
又
\[
 G^{-1}n=(c u_--G^{-1}S)/k,\qquad
 m^*G^{-1}=(u_+^*+R^*G^{-1})/h.
\]
将它们代入由 (1.1) 直接展开的 \(J\)，全部含完整逆的四项恰合成 (2.1) 的最后一个乘积。其余 \(ab^*\) 系数为
\[
 -c/k-1/h+\{c^2+1-c(\alpha+\beta)\}/(hk)=0,
\]
故得到 (2.1)。不需要给 \(\eta\) 或两个大的均值平方各自找界。

本稿取
\[
                   c=\alpha+1,\qquad h=1.
\]
(0.1) 与 Jensen 不等式给 \(\ell(1)<0\)，所以 \(\beta\) 指数小，而 \(\alpha=O(Q)\)。因此 \(k=1+O(e^{-\delta Q})\)。此外
\[
                         R=m-Gu_+,\qquad S=Z^{-1}R          \tag{2.2}
\]
是完全准确的式子。它避免了用一个几乎等于 \(\alpha\) 的参数去除以小量。

于是 (2.1) 可写成
\[
 \begin{split}
 J={}&nm^*-G-D_0+\alpha mm^*+nS^*-Rm^*\\
   &+(D_a+aR^*)G^{-1}(D_b-Sb^*)+O(e^{-\delta'Q}).            \tag{2.3}
 \end{split}
\]
所有被吸收的多项式因子都由下节的真实完整逆估计控制。

## 3. 端峰展开及三个完整矩阵

写 \(\varepsilon=Q^{-1}\)，
\[
 k_2=\sum_i\omega_i(z_i-1)^2,\qquad K=k_2/d,\qquad
 D_z=\operatorname{diag}(z_i/\omega_i).
\]
对 \(T=\varepsilon U\)，有
\[
 Q\ell(\varepsilon U)
   =-dU-\varepsilon k_2U^2/2+O(\varepsilon^2U^3).
\]
端点 Laplace 展开给
\[
 \alpha=d/\varepsilon+K+O(\varepsilon),
\]
\[
 m=\varepsilon\mu+\varepsilon^2\nu+O(\varepsilon^3),\quad
 \mu=z/d,\quad
 \nu_i=-\frac{2z_i(z_i+K-1)}{d^2},                           \tag{3.1}
\]
以及
\[
 G=\varepsilon^2G_0+\varepsilon^3G_1+O(\varepsilon^4),       \tag{3.2}
\]
其中
\[
 H_0=D_z+\frac{zz^*}{d},\qquad G_0=H_0/d>0,\qquad
 G_0^{-1}=d\{\operatorname{diag}(\omega_i/z_i)-\omega\omega^*\},
                                                                  \tag{3.3}
\]
\[
 \begin{split}
 G_1={}&-\frac2{d^2}
          \operatorname{diag}\!\left(
             \frac{z_i(2z_i+K-1)}{\omega_i}\right)\\
       &+\frac1{d^3}\{(8-6K)zz^*
                    -4(z^{\circ2}z^*+z(z^{\circ2})^*)\}.    \tag{3.4}
 \end{split}
\]
例如这些式只需
\[
 \mathbb ET=\frac{\varepsilon}{d}
               -\frac{2k_2\varepsilon^2}{d^3}+O(\varepsilon^3),
\]
\[
 \mathbb ET^2=\frac{2\varepsilon^2}{d^2}
               -\frac{10k_2\varepsilon^3}{d^4}
               +O(\varepsilon^4),\qquad
 \mathbb ET^3=\frac{6\varepsilon^3}{d^3}+O(\varepsilon^4).
\]
在协方差中保留
\(\mathbb E[p_i(T)(1-p_i(T))]/q_i\) 才得到 (3.4) 的对角项；不能丢掉实际组内二项噪声。

所有余项来自对 \(e^{Q\ell}\) 的端点 Taylor 展开。由于 \(\ell'(t)\leq-d<0\)，积分尾由统一指数函数控制；有限阶展开并积分给所写阶数。在本稿声明的紧 profile 集上，导数、尾界及逆矩阵界均一致。

## 4. 相位中的前两阶全部抵消

由 (2.2)，记
\[
 R=\varepsilon R_1+\varepsilon^2R_2+O(\varepsilon^3),\quad
 S_j=Z^{-1}R_j,\quad w_+=(Z-I)\omega ,
\]
则
\[
 R_1=\mu-G_0w_+,\qquad R_2=\nu-G_1w_+.                     \tag{4.1}
\]
(2.3) 和 (3.1)–(3.4) 给出以下完整矩阵结论：
\[
 \boxed{
 J=\varepsilon^2\mathbf1\,v^*+O(\varepsilon^3),\qquad
 v_i=\frac{2z_i(z_i+K-2)}{d^2}.}                            \tag{4.2}
\]
特别 \(Q^{-1}\) 项是整个矩阵零，而 \(Q^{-2}\) 项的左像严格在 \(\mathbb C\mathbf1\) 中。

下面给出 (4.2) 的有限代数证书，避免以选定维数代入代替一般证明。对单变量多项式 \(f\)，记
\[
 \mathcal D[f]=\operatorname{diag}(f(z_i)/\omega_i),\quad
 \langle f\rangle=\sum_i\omega_if(z_i),\quad
 \mathcal O[f,g]=f(z)g(z)^* .
\]
所有所需矩阵都是 \(\mathcal D[f]+\sum\mathcal O[f,g]\)。若定义
\(A\star B=AG_0^{-1}B\)，则
\[
 \mathcal D[f]\star\mathcal D[g]
   =d\mathcal D[fg/z]-d\mathcal O[f,g],
\]
\[
 \mathcal D[f]\star\mathcal O[g,h]
   =d\mathcal O[fg/z,h]-d\langle g\rangle\mathcal O[f,h],
\]
\[
 \mathcal O[f,g]\star\mathcal D[h]
   =d\mathcal O[f,gh/z]-d\langle g\rangle\mathcal O[f,h],
\]
\[
 \mathcal O[f,g]\star\mathcal O[h,k]
   =d(\langle gh/z\rangle-\langle g\rangle\langle h\rangle)
                                                   \mathcal O[f,k].
                                                                  \tag{4.3}
\]
这些只由 (3.3) 相乘得到。

将 (2.3) 的乘积写作
\[
 D_a+aR^*=\varepsilon A_1+\varepsilon^2A_2+O(\varepsilon^3),
\quad
 D_b-Sb^*=\varepsilon^2B_2+\varepsilon^3B_3+O(\varepsilon^4),
\]
其中
\[
 A_1=D_z+zR_1^*,\quad
 A_2=-\mathcal D[z^2/d]+zR_2^*-(Z\mu)R_1^*,
\]
\[
 B_2=\mathcal D[1/d]-S_1\mathbf1^*/d,
\]
\[
 B_3=\mathcal D[-2(z+K-1)/d^2]
       -S_1[-2(z+K-1)/d^2]^*-S_2\mathbf1^*/d.
\]
于是 \(J\) 的 \(\varepsilon\) 系数为
\[
 \mathbf1\mu^*-\mathcal D[1]+d\mu\mu^*
       +\mathbf1S_1^*+A_1\star B_2=0.                     \tag{4.4}
\]
其 \(\varepsilon^2\) 系数为
\[
 \begin{split}
 &\mathbf1\nu^*-\mu\mu^*-G_0
       +d(\mu\nu^*+\nu\mu^*)+K\mu\mu^*
       +\mathbf1S_2^*-\mu S_1^*-R_1\mu^*\\
 &\hspace{8mm}+A_2\star B_2+A_1\star B_3
                        -(A_1\star G_1)\star B_2
       =\mathcal O[1,\,2z(z+K-2)/d^2].                    \tag{4.5}
 \end{split}
\]
(4.3) 逐项展开时，只需
\[
 \langle1\rangle=1,\quad\langle z\rangle=1-d,\quad
 \langle z^2\rangle=dK+1-2d;
\]
\(\langle z^3\rangle\) 可保持任意符号，最后严格消失。因而 (4.4)–(4.5) 是对任意组数、任意真实正 profile 的同一个多项式身份。

相邻生成器
[精确系数证书](2026-11-14-balanced-star-strict-endpoint-phase-coefficient-certificate-789f-next.py)
仅实现 (4.3) 的这四条规则，独立符号化前三个矩并输出 (4.4)–(4.5)。它不枚举固定参数实例，也不作数值抽样。

## 5. \(L\) 的完整退化度量与相位界

\(H\) 没有遗漏的退化方向：
\[
                           QH\longrightarrow H_0>0.        \tag{5.1}
\]
\(L\) 则必须保留不同尺度之间的交叉。取 \(E\) 为 \(\mathbf1^\perp\) 的固定等距列矩阵，取 \(\ell_0\) 满足
\(\mathbf1^*\ell_0=1\)。使用真实两端坐标
\[
 B_H=\sqrt Q\,I,\qquad
 B_L=\sqrt Q[\ell_0,QE].
\]
在极限中，\(\tau=QT\) 服从参数 \(d\) 的指数分布；给定 \(\tau\)，各 \(K_i\) 独立 Poisson，均值 \(\omega_i z_i\tau\)。置 \(Y_i=K_i/\omega_i\)。这是有限条件二项式及端点 Laplace 展开的直接极限。

由 (1.1)，完整 \(L\) 极限是
\[
 \begin{split}
 B_L^*LB_L\longrightarrow\mathcal L_0
 &=\mathbb E\,\tau
       \begin{bmatrix}1\\-E^*Y\end{bmatrix}
       \begin{bmatrix}1\\-E^*Y\end{bmatrix}^*\\
 &=\begin{pmatrix}
 1/d&-2z^*E/d^2\\
 -2E^*z/d^2&
 E^*(2D_z/d^2+6zz^*/d^3)E
 \end{pmatrix}.                                           \tag{5.2}
 \end{split}
\]
特别不能丢掉此式的两个交叉块后再取逆。其首 Schur 恰为
\[
 \frac2{d^2}E^*(D_z+zz^*/d)E
                         =\frac2{d^2}E^*H_0E>0,
\]
故 \(\mathcal L_0>0\)。\(m=1\) 时对比块为空，首块 \(1/d\) 已给正定性。

现在 (4.2) 给
\[
 B_L^*JB_H=O(Q^{-1}).                                     \tag{5.3}
\]
首行使用 \(J=O(Q^{-2})\)；其余行虽有额外的 \(Q\) 因子，但
\(E^*\mathbf1=0\) 消掉 (4.2) 的整项，故仍为 \(O(Q^{-1})\)。
由 (5.1)–(5.2)，两个缩放后的完整 Gram 及其逆均一致有界。因此真实归一化交叉算子范数为 \(O(Q^{-1})\)，其平方正是 (0.2) 的相位，得到 (0.3)。

## 6. 另一个端点与尚未涵盖的过渡

将全部小权平方换成 \(z_i^{-1}\)，并作 \(T\mapsto1-T\)、\(X\mapsto\mathbf1-X\)，准确地有
\[
 H(z^{-1})=L(z),\quad L(z^{-1})=H(z),\quad G(z^{-1})=G(z),
 \quad J(z^{-1})=J(z)^* .
\]
两个归一交叉算子互为伴随，故相位谱相同。于是严格峰在 \(1\) 的情形也满足 (0.3)。

该结论与内峰完整相位投影极限不同：固定严格端峰 profile 的整个相位趋零，而内峰有 \(m-1\) 个极限等号方向。连接两者时，\(1-\sum\omega_i z_i\) 可达到 \(Q^{-1/2}\) 的尺度，端点成为截断 Gaussian 过渡；本稿的常数依赖严格端峰余量，不能据此跨越该层或关闭一般统一常数问题。

