# 平衡 star 的高斯过渡层：完整三尺度相位及统一极限界

日期：2026-11-14；工作标识：789f。

## 0. 定理与量词

固定组数 \(m\ge2\)、正比例 \(\omega_i\)（\(\sum_i\omega_i=1\)）和正数 \(x_i\)，满足
\[
 \sum_i\omega_i x_i=1,\qquad
 \chi=\sum_i\omega_i(x_i-1)^2>0.                         \tag{0.1}
\]
沿 \(q_i=Q\omega_i\) 为整数的序列，令
\[
 \varepsilon=Q^{-1/2},\qquad
 z_i(Q)=(1-\lambda\varepsilon)x_i,                       \tag{0.2}
\]
其中 \(\lambda\in\mathbb R\) 固定；充分大 \(Q\) 时全部权为正。主组长度为 \(Q\)，小组总长度也为 \(Q\)。始终使用这个真实平衡 star reducing 模块的整个 \(m\) 维低 primitive 源和一维硬源。

令 \(H_Q,L_Q,G_Q,J_Q\) 为下节定义的完整物理形式（同时除去共同标量），并保持
\[
 J_Q=H_QG_Q^{-1}L_Q-2G_Q-y_Qy_Q^*,\qquad
 \Phi_Q=H_Q^{-1/2}J_Q^*L_Q^{-1}J_QH_Q^{-1/2}.             \tag{0.3}
\]
则 \(\Phi_Q\) 的全部特征值收敛到
\[
 \boxed{\{\Lambda_{\rm b},\
         \underbrace{\Lambda_{\rm d},\ldots,\Lambda_{\rm d}}_{m-2},
         0\}},                                         \tag{0.4}
\]
其中两个标量只依赖 \(\lambda/\sqrt\chi\)。它们在所有实 \(\lambda\) 上满足
\[
 0\le\Lambda_{\rm d}<1,\qquad
 0\le\Lambda_{\rm b}\le\frac43.                          \tag{0.5}
\]
因此
\[
                         \limsup_{Q\to\infty}\|\Phi_Q\|\le\frac43.
                                                               \tag{0.6}
\]
\(m=2\) 时没有重复的深层特征值，仍是整个二维源的结论。

收敛在以下紧参数集上一致：\(m\) 固定，\(\omega_i\ge\omega_0>0\)，\(x_i\) 位于固定正紧区间，\(\chi\ge\chi_0>0\)，\(|\lambda|\le\Lambda_0<\infty\)。由下文展开可取误差 \(O(Q^{-1/4})\)。故在这样的紧集上，对任意 \(\delta>0\)，充分大 \(Q\) 有
\[
                    \Phi_Q\preceq(4/3+\delta)I.         \tag{0.7}
\]

这不是所有有限 \(Q\)、所有正权、变化组数或 \(\omega_i\to0\) 的统一界。也没有把 \(\lambda\) 无界、\(\chi\to0\) 或多种退化同时发生的情形包含在一致余项中。固定 \(\lambda\) 的极限常数统一，和有限 \(Q\) 的全参数界是不同量词。

本稿接续[严格端点稿](2026-11-14-balanced-star-strict-endpoint-full-phase-decay-789f-next.md)与[内峰完整源稿](2026-11-14-balanced-star-macroscopic-interior-full-phase-projection-limit-789f-next.md)，处理二者之间的 \(Q^{-1/2}\) 临界层。下文同时给出真实完整源矩阵和有限符号恒等式，未将三个源尺度分开粗估。

## 1. 真实概率形式与端点恒等式

令
\[
 F_Q(t)=\prod_i(1-t+z_i(Q)t)^{q_i},\quad
 Z_{F,Q}=\int_0^1F_Q(t)\,dt,\quad \rho_Q=F_Q/Z_{F,Q}.
\]
给定 \(T=t\)，各组独立且
\[
 K_i\mid T=t\sim\operatorname{Bin}
       \left(q_i,\frac{z_i(Q)t}{1-t+z_i(Q)t}\right),
 \qquad X_i=K_i/q_i.
\]
写
\[
 \mathbf m=\mathbb EX,\quad \mathbf n=\mathbf1-\mathbf m,\quad
 G=\operatorname{Cov}X,\quad y=\mathbf m-\mathbf n,
\]
\[
 H=\mathbb E\frac{1-T}{T}XX^*,\qquad
 L=\mathbb E\frac{T}{1-T}(\mathbf1-X)(\mathbf1-X)^* .       \tag{1.1}
\]
端点处的乘积按其条件矩的连续值理解。上述积分均有限；例如 \(T\to0\) 时 \(\mathbb E(XX^*\mid T)=O(T)\)。

设 \(Z=\operatorname{diag}(z_i(Q))\)，
\[
 a=Z\mathbf n,\quad b=Z^{-1}\mathbf m,\quad
 D_a=\operatorname{diag}(a_i/q_i),\
 D_b=\operatorname{diag}(b_i/q_i),\
 D_0=\operatorname{diag}(1/q_i).
\]
条件二项矩和一次分部积分给
\[
 H=D_a-ZG+a\mathbf m^*,\quad
 L=D_b-GZ^{-1}+\mathbf n b^*,\quad
 [Z,G]=a\mathbf m^*-\mathbf m a^*.                       \tag{1.2}
\]
令
\[
 \alpha=Z_{F,Q}^{-1},\quad
 \beta=\frac{\prod_i z_i(Q)^{q_i}}{Z_{F,Q}},\quad
 u_\pm=(Z^{\pm1}-I)q.
\]
完整源上的准确关系为
\[
 Gu_+=a-\alpha\mathbf m,\quad Gu_-=b-\beta\mathbf n,
\]
\[
 \mathbf n^*u_+=1-\alpha,\quad
 \mathbf m^*u_-=1-\beta,\quad
 u_+^*Gu_-=\alpha\beta-1.                                \tag{1.3}
\]

对任意标量 \(c\)，置
\[
 R=c\mathbf m-a,\quad S=Z^{-1}R=c b-\mathbf n,\quad
 h=c-\alpha,\quad k=1-c\beta.
\]
当 \(h,k\ne0\) 时，实际 \(J\) 满足
\[
\begin{split}
 J={}&\mathbf n\mathbf m^*-G-D_0+
       \frac{c\beta}{k}\mathbf n\mathbf n^*
       +\frac{\alpha}{h}\mathbf m\mathbf m^*
       +\frac1k\mathbf nS^*-\frac1hR\mathbf m^*\\
   &+\left(D_a+\frac1h aR^*\right)G^{-1}
                    \left(D_b-\frac1kSb^*\right).        \tag{1.4}
\end{split}
\]
这是完全非交换恒等式。为核对它，可令
\(\eta=\mathbf m^*G^{-1}\mathbf n-1\)，从 (1.3) 得
\[
 R^*G^{-1}S=c^2+1-c(\alpha+\beta)-hk\eta,
\]
\[
 G^{-1}\mathbf n=(cu_--G^{-1}S)/k,\quad
 \mathbf m^*G^{-1}=(u_+^*+R^*G^{-1})/h.
\]
将它们代入由 (1.2) 展开的 \(J\)，四个含 \(G^{-1}\) 的项合成 (1.4) 最后一个乘积；余下 \(ab^*\) 的系数
\(-c/k-1/h+\{c^2+1-c(\alpha+\beta)\}/(hk)\) 正好为零。

本稿选
\[
                       c=(\mathbb ET)^{-1}-1.           \tag{1.5}
\]
这个选择保留小参数 \(\alpha\) 的真实反馈，而不分别估计大的均值项。

## 2. 极限半线分布及矩展开

令 \(U=T/\varepsilon\)。极限密度为
\[
 f_{\lambda,\chi}(u)=
 \frac{\exp(-\lambda u-\chi u^2/2)}
      {\int_0^\infty\exp(-\lambda v-\chi v^2/2)\,dv},
 \qquad u>0.                                           \tag{2.1}
\]
记
\[
 M_j=\mathbb E_fU^j,\quad \mu=M_1>0,\quad
 v=M_2-\mu^2>0,\quad A_0=f_{\lambda,\chi}(0).
\]
分部积分给
\[
 A_0=\lambda+\chi\mu>0,\quad
 \chi M_{j+1}=jM_{j-1}-\lambda M_j\quad(j\ge1).           \tag{2.2}
\]

以下写出实际有限 \(Q\) 矩到足够阶数，防止只匹配极限密度而漏掉退化源的费用。令
\[
 k_r=\sum_i\omega_i(x_i-1)^r,\quad k_2=\chi,
\]
\[
 W_1(u)=\lambda\chi u^2+k_3u^3/3,
\]
\[
 V_2(u)=-\lambda^2(1+\chi)u^2/2
       -\lambda(k_3+\chi)u^3-k_4u^4/4,\qquad
 W_2=V_2+W_1^2/2.
\]
直接展开真实乘积得到
\[
 Q\sum_i\omega_i\log(1+\varepsilon u(x_i-1-\lambda\varepsilon x_i))
 =-\lambda u-\chi u^2/2+\varepsilon W_1(u)
                   +\varepsilon^2V_2(u)+O(\varepsilon^3u^5).
                                                               \tag{2.3}
\]
对 \(j\ge0\)，定义
\[
 \dot M_j=\mathbb E_f(U^jW_1)-M_j\mathbb E_fW_1,
\]
\[
 \ddot M_j=\mathbb E_f(U^jW_2)-M_j\mathbb E_fW_2
                                      -(\mathbb E_fW_1)\dot M_j.
\]
点号表示展开系数，不表示导数或含 \(1/2\) 的 Taylor 系数。于是
\[
 \mathbb E_Q U^j=M_j+\varepsilon\dot M_j
                  +\varepsilon^2\ddot M_j+O(\varepsilon^3),
                                                               \tag{2.4}
\]
\[
 \alpha=\varepsilon^{-1}A_0
   \left[1-\varepsilon\mathbb E_fW_1
       +\varepsilon^2\{(\mathbb E_fW_1)^2-\mathbb E_fW_2\}
       +O(\varepsilon^3)\right].                         \tag{2.5}
\]
由于 \(\sum\omega_i\log x_i<0\)，\(\beta\) 指数小。在所声明紧集上，(2.3) 的实际指数由
\(C-c u^2\) 控制，因此这些展开、有限次矩积分及尾界均一致；没有用形式级数替代所需余项。

## 3. 完整协方差逆：亮方向与其全部补空间

记
\[
 \mathcal D[f]=\operatorname{diag}(f(x_i)/\omega_i),\quad
 \mathcal O[f,g]=f(x)g(x)^*,\quad
 \langle f\rangle=\sum_i\omega_if(x_i),\quad c_x=x-1.
\]
则
\[
 G=\varepsilon^2v\,xx^*
        +\varepsilon^3G_3+\varepsilon^4G_4
        +\varepsilon^5G_5+O(\varepsilon^6).              \tag{3.1}
\]
为给出完整且可复算的逆，定义
\[
 v_1=\dot M_2-2\mu\dot M_1,\quad
 v_2=\ddot M_2-2\mu\ddot M_1-(\dot M_1)^2,
\]
\[
 v_{12}=M_3-\mu M_2,\quad
 \dot v_{12}=\dot M_3-\mu\dot M_2-\dot M_1M_2,
\]
\[
 v_{22}=M_4-M_2^2,\quad
 \dot v_{22}=\dot M_4-2M_2\dot M_2,\quad
 v_{13}=M_4-\mu M_3,\quad v_{23}=M_5-M_2M_3.
\]
写 \(\operatorname{Sym}\mathcal O[f,g]=\mathcal O[f,g]+\mathcal O[g,f]\)。条件二项协方差给
\[
 G_3=\mathcal D[\mu x]+(v_1-2\lambda v)\mathcal O[x,x]
                   -v_{12}\operatorname{Sym}\mathcal O[x,xc_x],
                                                               \tag{3.2}
\]
\[
\begin{split}
 G_4={}&\mathcal D[(\dot M_1-\lambda\mu)x-M_2x(2x-1)]\\
 &+(v_2-2\lambda v_1+\lambda^2v+2\lambda v_{12})\mathcal O[x,x]\\
 &+(-\dot v_{12}+3\lambda v_{12})
                            \operatorname{Sym}\mathcal O[x,xc_x]\\
 &+v_{22}\mathcal O[xc_x,xc_x]
                 +v_{13}\operatorname{Sym}\mathcal O[x,xc_x^2].
                                                               \tag{3.3}
\end{split}
\]
在下式中 \(G_5\) 只出现于 \(R_0G_5R_0\)。因此可以删去左或右有 \(x\) 的外积；其准确剩余代表是
\[
\begin{split}
 \widetilde G_5={}&
 \mathcal D[(\ddot M_1-\lambda\dot M_1)x
     -\dot M_2x(2x-1)+M_3x(3x^2-4x+1)
     +\lambda M_2x(4x-1)]\\
 &+(\dot v_{22}-4\lambda v_{22})\mathcal O[xc_x,xc_x]
       -v_{23}\operatorname{Sym}\mathcal O[xc_x,xc_x^2].
                                                               \tag{3.4}
\end{split}
\]
特别 \(p_i(1-p_i)\) 的三次项是
\(x_i(3x_i^2-4x_i+1)T^3\)；实际二项噪声不能删除。

令
\[
 R_0=\frac1\mu\{\operatorname{diag}(\omega_i/x_i)
                                -\omega\omega^*\},\qquad
 w_i=\omega_i\left[1+\frac{v_{12}}{\mu}(x_i-1-\chi)\right],
 \quad \sigma=w^*G_3w.
\]
则 \(R_0x=0,\ x^*w=1\)，并有
\[
 R_0G_3=I-wx^*,\quad G_3R_0=I-xw^*.
\]
真实完整逆为
\[
 G^{-1}=\varepsilon^{-3}R_0+\varepsilon^{-2}T_1
                             +\varepsilon^{-1}T_2+O(1), \tag{3.5}
\]
\[
 T_1=ww^*/v-R_0G_4R_0,
\]
\[
\begin{split}
 T_2={}&R_0G_4R_0G_4R_0-R_0\widetilde G_5R_0\\
 &-\frac1v(R_0G_4ww^*+ww^*G_4R_0)-\frac{\sigma}{v^2}ww^*.
                                                               \tag{3.6}
\end{split}
\]
证明可先精确反演
\(\varepsilon^2vxx^*+\varepsilon^3G_3\)：
其逆为
\[
 \varepsilon^{-3}R_0+
 \frac{\varepsilon^{-2}}{v+\varepsilon\sigma}ww^*.
\]
再对 \(\varepsilon^4G_4+\varepsilon^5G_5+\cdots\) 作有限 resolvent 展开即得 (3.5)–(3.6)。这是在完整源上先反演；没有先删去亮方向或将压缩逆次序交换。

## 4. 相位的三阶共同抵消

定义
\[
 j_0=\frac{2\chi\mu^2+\lambda\mu-1}{\chi\mu}
      =\frac{2\mu^2-M_2}{\mu},\qquad
 j_2=\frac{\mu^2-v}{\chi v}-2\mu^2.                     \tag{4.1}
\]
完整矩阵展开有
\[
 J=\varepsilon j_0\,\mathbf1 x^*
       +\varepsilon^2J_2+\varepsilon^3J_3
       +O(\varepsilon^4),                               \tag{4.2}
\]
其中 \(J_2\) 的左像位于 \(\operatorname{span}\{\mathbf1,x\}\)，且
\[
 J_2=\mathbf1\,r^*+j_2\,xx^*                            \tag{4.3}
\]
（某个 \(r\)，无须计算其具体大系数）。更关键的是，对任意
\[
 x^*F=0,\qquad \mathbf1^*E=x^*E=0,
\]
有
\[
                       \boxed{E^*J_3F=-j_0E^*\mathcal D[x]F.}
                                                               \tag{4.4}
\]
这是整个深层块的恒等式，不只是某个测试向量。全部 \(k_3,k_4\) 以及未知高阶均值、协方差修正，在 (4.4) 中共同消掉。

下面给出有限代数证明的完整规则。它也由同行生成器
[transition coefficient certificate](2026-11-14-balanced-star-gaussian-transition-coefficient-certificate-789f-next.py)
直接作有理多项式化简。

令 \(A\star B=AR_0B\)。四条乘法规则是
\[
 \mathcal D[f]\star\mathcal D[g]
   =\mu^{-1}\{\mathcal D[fg/x]-\mathcal O[f,g]\},
\]
\[
 \mathcal D[f]\star\mathcal O[g,h]
   =\mu^{-1}\{\mathcal O[fg/x,h]-\langle g\rangle\mathcal O[f,h]\},
\]
\[
 \mathcal O[f,g]\star\mathcal D[h]
   =\mu^{-1}\{\mathcal O[f,gh/x]-\langle g\rangle\mathcal O[f,h]\},
\]
\[
 \mathcal O[f,g]\star\mathcal O[h,k]
   =\mu^{-1}\{\langle gh/x\rangle-\langle g\rangle\langle h\rangle\}
                                                      \mathcal O[f,k].
                                                               \tag{4.5}
\]
只需用 \(\langle1\rangle=\langle x\rangle=1\) 以及
\(\langle(x-1)^r\rangle=k_r\)，不限制组数。

为明确每个输入系数，置
\(\widehat M_j=M_j+\varepsilon\dot M_j+\varepsilon^2\ddot M_j\)，
\(z_\varepsilon=(1-\lambda\varepsilon)x\)，\(c_\varepsilon=z_\varepsilon-1\)。
按所需阶截断，
\[
 \mathbf m=\varepsilon z_\varepsilon\widehat M_1
    -\varepsilon^2z_\varepsilon c_\varepsilon\widehat M_2
    +\varepsilon^3z_\varepsilon c_\varepsilon^2\widehat M_3
    +O(\varepsilon^4),
\]
\[
\begin{split}
 R={}&-\varepsilon z_\varepsilon c_\varepsilon
          (\widehat M_2/\widehat M_1-\widehat M_1)\\
 &+\varepsilon^2z_\varepsilon c_\varepsilon^2
          (\widehat M_3/\widehat M_1-\widehat M_2)\\
 &-\varepsilon^3z_\varepsilon c_\varepsilon^3
          (\widehat M_4/\widehat M_1-\widehat M_3)
          +O(\varepsilon^4).                            \tag{4.6}
\end{split}
\]
其余 \(a,b,S\) 由定义直接相乘，\(h=(\varepsilon\widehat M_1)^{-1}-1-\alpha\)。注意
\[
 h=\varepsilon^{-1}\chi v/\mu+O(1)>0.                   \tag{4.7}
\]
令
\[
 A=D_a+aR^*/h=\varepsilon^2A_2+\varepsilon^3A_3
                              +\varepsilon^4A_4+O(\varepsilon^5),
\]
\[
 B=D_b-Sb^*=\varepsilon^2B_2+\varepsilon^3B_3
                              +\varepsilon^4B_4+O(\varepsilon^5).
\]
以 (2.5)、(4.6) 作有限系数提取就完全确定这六个矩阵。将它们和 (3.5) 代入 (1.4)；因 \(\beta\) 指数小，前三阶只用
\[
 \mathbf n\mathbf m^*-G-D_0+
 \alpha\mathbf m\mathbf m^*/h+\mathbf nS^*
 -R\mathbf m^*/h+A G^{-1}B.                             \tag{4.8}
\]
乘积的三个系数准确为
\[
\begin{array}{c|l}
 \varepsilon & A_2R_0B_2\\
 \varepsilon^2&A_2R_0B_3+A_3R_0B_2+A_2T_1B_2\\
 \varepsilon^3&A_2R_0B_4+A_3R_0B_3+A_4R_0B_2
        +A_2T_1B_3+A_3T_1B_2+A_2T_2B_2 .
\end{array}                                             \tag{4.9}
\]
利用 (4.5) 和递推 (2.2)，(4.8) 的化简表为
\[
\begin{array}{c|c|c}
 \text{阶}&\text{对角多项式}&\text{外积多项式}\\ \hline
 1&0&j_0\,y\\
 2&0&r(y)+j_2xy\\
 3\text{，左杀 }1,x\text{、右杀 }x&-j_0x&0.
\end{array}                                             \tag{4.10}
\]
这里外积多项式 \(f(x)g(y)\) 表示 \(\mathcal O[f,g]\)，\(r\) 为单变量多项式。最后一行删除外积的左次数 \(0,1\) 及右次数 \(1\)，对角项则必须保留。此规则恰对应 \(E^*(\cdot)F\)，因此 (4.10) 证明 (4.2)–(4.4)。生成器保留任意 \(\chi,\mu,\lambda,k_3,k_4\)，并逐项验证这些有理恒等式；它不代入有限维样本或浮点值。

## 5. 三种尺度同时归一

写 \(D_x=\mathcal D[x]>0\)。选固定列
\[
 x^*h_0=1,\quad
 \mathbf1^*l_0=1,\quad
 \mathbf1^*l_1=0,\ x^*l_1=1,
\]
以及 \(F\) 为 \(x^\perp\) 的任意基，\(E\) 为
\(\{\mathbf1,x\}^\perp\) 的任意基。因 \(\chi>0\)，\(\mathbf1,x\) 线性独立。作完整可逆源变换
\[
 B_H=[\,\varepsilon^{-1/2}h_0,\ \varepsilon^{-1}F\,],
\]
\[
 B_L=[\,\varepsilon^{-1/2}l_0,\
          \varepsilon^{-3/2}l_1,\ \varepsilon^{-2}E\,].
                                                               \tag{5.1}
\]
条件二项二阶矩直接给
\[
 B_H^*HB_H\longrightarrow
     \begin{pmatrix}\mu&0\\0&F^*D_xF\end{pmatrix},         \tag{5.2}
\]
\[
 B_L^*LB_L\longrightarrow
 \operatorname{diag}\left(
   \begin{pmatrix}\mu&-M_2\\-M_2&M_3\end{pmatrix},
   M_2E^*D_xE\right).                                  \tag{5.3}
\]
例如 \(L\) 的前两层来自
\(\mathbb E[T(1-T)^{-1}(1-p)(1-p)^*]\)：
其亮项为 \(\varepsilon\mu\,11^*\)，交叉为
\(-\varepsilon^2M_2(1x^*+x1^*)\)，第二层为
\(\varepsilon^3M_3xx^*\)。
在同时垂直于 \(1,x\) 的深层，首个确定项是实际条件二项噪声
\(\varepsilon^4M_2D_x\)。前两层的 \(-M_2\) 交叉不能丢弃。

(4.2)–(4.4) 同时给
\[
 B_L^*JB_H\longrightarrow
 \begin{pmatrix}
 j_0&0\\
 j_2&0\\
 0&-j_0E^*D_xF
 \end{pmatrix}.                                        \tag{5.4}
\]
全部遗漏交叉在这些完整尺度下为 \(O(\varepsilon^{1/2})\)。两端极限 Gram 严格正定：前两层行列式
\(\mu M_3-M_2^2>0\) 是带 \(U\) 的严格 Cauchy–Schwarz；其余来自 \(D_x>0\)。

合同后
\[
 H^{-1/2}J^*L^{-1}JH^{-1/2}
\]
的谱等于使用 \(B_H^*HB_H,B_L^*LB_L,B_L^*JB_H\) 得到的谱，因此 (5.2)–(5.4) 已覆盖全部源，而不是只覆盖一个压缩。

## 6. 完整极限谱的两个标量

定义
\[
 r=M_2/\mu^2,\quad
 q=r-1=v/\mu^2,\quad
 \Delta=M_3/\mu^3-r^2 .
\]
严格方差和带 \(U\) 的严格 Cauchy–Schwarz 给 \(q>0,\Delta>0\)。由 (2.2)，
\[
              \Delta=\frac{2-r}{\chi\mu^2}
                     =\frac{1-q}{\chi\mu^2},            \tag{6.1}
\]
故 \(0<q<1\)。又
\[
 j_0=\mu(1-q),\qquad
 j_2=\mu^2\{\Delta/q-2\}.
\]
(5.2)–(5.4) 的亮列费用为
\[
\begin{split}
 \Lambda_{\rm b}
 &=\mu^{-1}(j_0,j_2)
      \begin{pmatrix}\mu&-M_2\\-M_2&M_3\end{pmatrix}^{-1}
      (j_0,j_2)^T\\
 &=(1-q)^2+
       \frac{\{\Delta/q-(1+q^2)\}^2}{\Delta}.            \tag{6.2}
\end{split}
\]
深层为
\[
                 \Lambda_{\rm d}
                   =j_0^2/M_2=\frac{(1-q)^2}{1+q}.      \tag{6.3}
\]
由于 \(E\) 的列空间包含在 \(F\) 的列空间中，
\[
 E^*D_xF(F^*D_xF)^{-1}F^*D_xE=E^*D_xE.
\]
所以深层交叉是 \(m-2\) 维等距对偶压缩：其所有非零平方奇异值均为 \(1\)，并在 \(m-1\) 维输入补空间中恰余一维核。这就证明 (0.4)，不是仅给最大特征值上界。

特别 \(\lambda=0\) 时 \(\chi\mu^2=2/\pi=:s\)，
\[
 \Lambda_{\rm d}=(2s-1)^2/s,\qquad
 \Lambda_{\rm b}=
 \frac{4s^5-16s^3+26s^2-17s+4}
      {s(s-1)^2(2s-1)}.                                 \tag{6.4}
\]
这是原精确临界面 \(\sum\omega_i z_i=1,\chi>0\) 的整个源极限；并不遗漏 \(m=2\) 的两个不同输出尺度。

## 7. 所有高斯过渡参数的 \(4/3\) 预算

本节为两个标量提供自足矩证明，不要求数值最大化。

由 (2.2)，
\[
 \chi v=1-\mu A_0<1.
\]
结合 (6.1)，得到
\[
                        \Delta\ge q(1-q).              \tag{7.1}
\]
将 \(U/\mu\) 的矩记为 \(a_j=M_j/\mu^j\)。递推 (2.2) 给
\(a_0=a_1=1,a_2=1+q,a_3=(1+q)^2+\Delta\)，并可消掉
\(\chi\mu^2=(1-q)/\Delta\)、\(\lambda\mu
 =1-(1-q^2)/\Delta\)。
对真实正密度，两个 Hankel Gram 均半正定；直接递推展开它们的行列式得
\[
 \det(a_{i+j})_{i,j=0}^2
       =\frac{\Delta\{q(1+q)-\Delta\}}{1-q}\ge0,
\]
\[
 \det(a_{i+j+1})_{i,j=0}^2
       =\frac{\Delta^2\{(3-q)\Delta-q(1+q)^2\}}{(1-q)^2}\ge0.
                                                               \tag{7.2}
\]
因此
\[
 \max\left\{q(1-q),\frac{q(1+q)^2}{3-q}\right\}
       \le\Delta\le q(1+q).                             \tag{7.3}
\]
令右边 (6.2) 为 \(F_q(\Delta)\)。这是关于正变量 \(\Delta\) 的凸函数，所以在 (7.3) 的区间上只须检查两端。

上端给
\[
 F_q(q(1+q))
    =\frac{(1-q)^2(1+2q)}{1+q}\le1.
\]
两个下界在 \(q=1/3\) 交叉。若 \(0<q\le1/3\)，则
\[
 F_q(q(1-q))=\frac{1-2q+5q^2}{1-q},
\]
\[
 \frac43-F_q(q(1-q))
       =\frac{(1-3q)(1+5q)}{3(1-q)}\ge0.
\]
若 \(1/3\le q<1\)，则
\[
 F_q\left(\frac{q(1+q)^2}{3-q}\right)
   =\frac{(1-q)^2(-q^3+10q^2-q+4)}
          {q(3-q)(1+q)^2},
\]
其与 \(4/3\) 的差为
\[
 \frac{(3q-1)(q^4-13q^3+19q^2-3q+12)}
      {3q(3-q)(1+q)^2}\ge0.                             \tag{7.4}
\]
最后多项式在 \(0\le q\le1\) 上至少为 \(9\)，因为
\(-13q^3+19q^2\ge6q^2\)，而 \(12-3q\ge9\)。
这证明 \(\Lambda_{\rm b}\le4/3\)；(6.3) 立即给
\(\Lambda_{\rm d}<1\)。

## 8. 适用边界与后续确切缺口

本定理保留了真实 \(m\) 维源、完整 \(G^{-1}\)、亮方向回归、\(L\) 的两层交叉以及最深二项噪声。它给所有固定 \(\lambda/\sqrt\chi\) 一个与组数及 profile 形状无关的极限常数。

仍未证明的是有限 \(Q\) 的全参数共同预算，尤其 \(|\lambda|\to\infty\) 与 \(Q\) 同时变化、\(\chi\to0\)、某些组比例趋零、组数增长及它们组合的退化。严格端点、内峰和本高斯层分别有正确的完整源归一；不能仅凭三种逐点极限拼出全参数统一常数，更不能据此声称原无限 graph 预算或 ISP 完成。

