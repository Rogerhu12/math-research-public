# 平衡 star：二次偏差与端点漂移比有界时的全维相位衰减

日期：2026-11-14；工作标识789f。

## 0. 定理与原来源

固定 \(0<a\le b<\infty\) 和 \(K_0<\infty\)。在真实平衡 star 中，任意组数、正整数 \(q_i\)、\(Q=\sum q_i\)，权平方 \(a\le z_i\le b\)，保留整个低 primitive 源和原硬源，记
\[
 G=\operatorname{Cov}X,\quad
 H=\mathbb E\frac{1-T}{T}XX^*,\quad
 L=\mathbb E\frac{T}{1-T}(1-X)(1-X)^*,\quad
 y=2\mathbb EX-\mathbf1,\quad J=HG^{-1}L-2G-yy^*.
\]
这里 \(T\) 的密度正比于 \(\prod_i(1-t+z_it)^{q_i}\)，条件 \(X_i=K_i/q_i\)、\(K_i\sim\mathrm{Bin}(q_i,z_it/(1-t+z_it))\) 独立。

设实际右端漂移及二次偏差为
\[
 R=\sum_iq_i(1-z_i^{-1})>0,\qquad
 S_+=\sum_iq_i(1-z_i^{-1})^2,\qquad S_+/R\le K_0.
\]
则存在仅依赖 \(a,b,K_0\) 的 \(R_0,C<\infty\)，使 \(R\ge R_0\) 时
\[
                         \boxed{J^*L^{-1}J\preceq C R^{-2}H.}       \tag{0.1}
\]
常数不依赖 \(Q,m,\min q_i\)，也不要求平均漂移 \(R/Q\) 或权方差有正下界。

取倒数权及 \(T\mapsto1-T,\ X\mapsto1-X\)，则 \(H,L\) 交换、\(J\mapsto J^*\)，真实相位范数保持。因此同样得到左端结论：若
\[
 R_-=-\sum_iq_i(z_i-1)>0,\qquad
 S=\sum_iq_i(z_i-1)^2,\qquad S/R_-\le K_0,
\]
则 \(\Phi\preceq C/R_-^2\)。这支付累计二次偏差可以增长、但第二亮方向的相对强度有界的整个端峰区。

## 1. 将所有可能的大维数因子准确吸收

先证明右端。记
\[
 x=1-T,\quad \alpha_i=z_i^{-1},\quad d_i=1-\alpha_i,\quad
 \omega_i=q_i/Q,\quad d=\sum_i\omega_i d_i>0,
\]
\[
 \varepsilon=R^{-1},\qquad
 Q=(\varepsilon d)^{-1},\qquad
 \kappa=\frac{\sum_i\omega_i d_i^2}{d}=\frac{S_+}{R}\le K_0.
\]
由正权界，
\[
 \ell:=1/b\le\alpha_i\le u:=1/a,\qquad
 0<d<1,\qquad
 \sum_i\omega_i d_i^2=\kappa d.
\]
若右端范围为空，定理无须另作处理。

令 \(W=\operatorname{diag}\sqrt{\omega_i}\)、\(e=(\sqrt{\omega_i})_i\)，取 \(F\) 为 \(e^\perp\) 的正交等距基，\(O=[e,F]\)。把每个完整 Gram 共同合同成
\[
                     A^{\mathrm c}=QO^*WAWO.
\]
这个可逆的共同合同保持原相位；它也是将二值源按真实组内置换约化后得到的原度量，没有删除组噪声。

定义
\[
 A_0=F^*\operatorname{diag}(\alpha_i)F,\qquad
 b_1=\frac{F^*(\sqrt{\omega_i}d_i)_i}{\sqrt d},\qquad
 a_0=1-d=\sum_i\omega_i\alpha_i.
\]
于是
\[
 \ell I\preceq A_0\preceq uI,\qquad
 \|b_1\|^2=\kappa-d\le K_0.                              \tag{1.1}
\]
对任意固定 \(j\ge1\)，
\[
 \frac{\|F^*(\sqrt{\omega_i}d_i^j)_i\|}{\sqrt d}
       \le D^{j-1}\sqrt{K_0},
 \qquad D=\max_i|d_i|.                                  \tag{1.2}
\]
对 \(j\ge2\)，还准确有
\[
 \left|\frac{\sum_i\omega_i d_i^j}{d}\right|
       \le D^{j-2}K_0.                                  \tag{1.3}
\]
这里 \(D\) 只由 \(a,b\) 控制。所有后续看似含 \(d^{-1/2}\) 或 \(d^{-1}\) 的系数都分别由 (1.2)、(1.3) 支付。

## 2. 端点积分的统一光滑性

令 \(U=x/\varepsilon\)，真实密度在 \(0<U<1/\varepsilon\) 正比于
\[
 \exp\{-U-\varepsilon U^2 h(\varepsilon U)\},             \tag{2.1}
\]
其中准确的二阶积分余项给
\[
 h(s)=\int_0^1(1-v)
       \frac{\sum_i\omega_i d_i^2/(1-vs d_i)^2}{d}\,dv.
                                                               \tag{2.2}
\]
因为 \(1-vs d_i\ge\min(1,\ell)>0\) 对 \(0\le s,v\le1\) 成立，所有固定阶 \(h^{(j)}\) 一致有界，且 \(h\ge0\)。密度和它对 \(\varepsilon\) 的任意固定阶导数，均被一个统一多项式乘 \(e^{-U}\) 控制。移动上端 \(1/\varepsilon\) 的全部边界项由 \(e^{-1/\varepsilon}\) 支付；任意有限次导数后仍在 \(\varepsilon=0\) 平坦。

归一化分母在统一小区间 \(0\le\varepsilon\le\varepsilon_0\) 内有正下界。因此对任意预定有限阶，全部归一矩、以及下节的算子值积分，都在 \(\varepsilon=0\) 有一致的右侧 \(C^N\) 延拓。特别 \(U\) 在 \(\varepsilon=0\) 的密度为 \(e^{-U}\)，
\[
 \mathbb EU=1,\quad \mathbb EU^2=2,\quad
 \mathbb EU^3=6,\quad \operatorname{Var}U=1.
\]
例如
\[
 \mathbb E x^k=k!\varepsilon^k
    \{1-\tfrac12k(k+3)\kappa\varepsilon+O(\varepsilon^2)\};
\]
本证明不需要逐项计算高阶系数。

为精确说明算子范数的一致性，置
\[
 v_i(s)=(1-d_i s)^{-1},\quad
 V_0(s)=\sum_i\omega_i v_i(s),\quad
 B(s)=\frac{F^*(\sqrt{\omega_i}d_i v_i(s))_i}{\sqrt d},
\]
\[
 A_{00}(s)=\sum_i\omega_i\alpha_i v_i(s).
\]
所有这些函数和所需有限阶导数一致有界，且
\[
 F^*Wv(s)=\sqrt d\,s B(s),\qquad
 F^*W(\alpha_i v_i(s))_i=\sqrt d\,(s-1)B(s).             \tag{2.3}
\]
对角矩阵的算子范数由最大单坐标控制，外积由这些向量范数控制；没有乘上组数的估计。

## 3. 三个真实 Gram 的整个统一极限

在同一 \(e/F\) 坐标中定义
\[
 B_H=\operatorname{diag}(\sqrt d,\varepsilon^{-1}I),\quad
 B_L=\operatorname{diag}(\sqrt d,I),\quad
 B_G=\varepsilon^{-1/2}B_L,
\]
\[
 \widehat H=B_HH^{\mathrm c}B_H,\quad
 \widehat L=B_LL^{\mathrm c}B_L,\quad
 \widehat G=B_GG^{\mathrm c}B_G.                          \tag{3.1}
\]
每个有限原模型都使用可逆合同。

给定 \(x\)，缺位概率是 \(\pi_i=\alpha_i x v_i(x)\)。三个原矩的完整条件表达为
\[
 H=\mathbb E x(1-x)v v^*
             +\operatorname{diag}\mathbb E[\alpha_i x^2v_i^2]/q_i,
\]
\[
 L=\mathbb E x(1-x)(\alpha v)(\alpha v)^*
             +\operatorname{diag}\mathbb E[\alpha_i(1-x)^2v_i^2]/q_i,
\]
\[
 G=\operatorname{Cov}(x\alpha v)
             +\operatorname{diag}\mathbb E[\alpha_i x(1-x)v_i^2]/q_i.
                                                               \tag{3.2}
\]
故全部原二项噪声都保留。

(2.3) 使 (3.1) 中每个负幂在积分前被准确消去。例如 \(\widehat H\) 的均值项是
\[
 \mathbb E\,U(1-\varepsilon U)
       \binom{V_0(\varepsilon U)}{U B(\varepsilon U)}
       \binom{V_0(\varepsilon U)}{U B(\varepsilon U)}^*.
\]
其噪声项为
\[
 \operatorname{diag}(\sqrt d\,\varepsilon,I)\,
 O^*\operatorname{diag}\mathbb E[
             \alpha_i U^2v_i(\varepsilon U)^2]O\,
 \operatorname{diag}(\sqrt d\,\varepsilon,I).
\]
\(\widehat G\) 的均值协方差项准确为
\[
 \operatorname{Cov}
       \binom{U A_{00}(\varepsilon U)}
             {-U(1-\varepsilon U)B(\varepsilon U)};
\]
其噪声项为
\[
 \operatorname{diag}(\sqrt d,I)\,
 O^*\operatorname{diag}\mathbb E[
       \alpha_i U(1-\varepsilon U)v_i(\varepsilon U)^2]O\,
 \operatorname{diag}(\sqrt d,I).
\]
\(\widehat L\) 的均值项同样是
\[
 \mathbb E\,U(1-\varepsilon U)
       \binom{A_{00}(\varepsilon U)}
             {-(1-\varepsilon U)B(\varepsilon U)}
       \binom{A_{00}(\varepsilon U)}
             {-(1-\varepsilon U)B(\varepsilon U)}^*,
\]
噪声为上式对角形式中的 \(U(1-\varepsilon U)\) 换成
\((1-\varepsilon U)^2\)。

这些准确积分证明三个完整矩阵有统一 \(C^N\) 延拓。取 \(\varepsilon=0\)，得到
\[
 H_*=\begin{pmatrix}
 1&2b_1^*\\2b_1&2A_0+6b_1b_1^*
 \end{pmatrix},\qquad
 G_*=L_*=\begin{pmatrix}
 a_0&-b_1^*\\-b_1&A_0+b_1b_1^*
 \end{pmatrix}.                                        \tag{3.3}
\]
\(\widehat H-H_*,\widehat G-G_*,\widehat L-L_*=O(\varepsilon)\)
及其所需有限阶导数均一致。

全部首项有只依 \(a,b,K_0\) 的正谱区间。\(H_*\) 的首Schur为
\(2A_0+2b_1b_1^*\succeq2\ell I\)。设 \(s=b_1^*A_0^{-1}b_1\le K_0/\ell\)；由真实对角正矩阵的同一压缩，
\[
 O^*\operatorname{diag}(\alpha_i)O
   =\begin{pmatrix}a_0&-\sqrt d\,b_1^*\\
                  -\sqrt d\,b_1&A_0\end{pmatrix}
   \succeq\ell I,
\]
所以 \(a_0-ds\ge\ell\)。于是 \(G_*=L_*\) 的下块Schur是
\[
                   a_0-\frac{s}{1+s}
                     =\frac{a_0-ds}{1+s}
                     \ge\frac{\ell}{1+K_0/\ell}>0.        \tag{3.4}
\]
上界同样直接。\(m=1\) 时对比块为空，公式仍成立。由统一扰动，三个真实矩阵及其逆在同一充分小 \(\varepsilon_0\) 上一致有界。

## 4. 有序共同差只可能有一个可去极点

令
\[
 R_\varepsilon=\operatorname{diag}(1,\varepsilon I),
 \qquad {\cal T}=\widehat G^{-1}\widehat L.
\]
由于 \(G_*=L_*\)，有 \({\cal T}(0)=I\)。因此
\[
 {\cal C}=R_\varepsilon{\cal T}R_\varepsilon^{-1}
\]
仍有统一的 \(C^{N-1}\) 延拓：唯一表面负幂是
\({\cal T}_{01}/\varepsilon\)，而
\[
 \frac{{\cal T}_{01}(\varepsilon)}{\varepsilon}
       =\int_0^1 {\cal T}'_{01}(v\varepsilon)\,dv.
\]
没有假设这些矩阵交换。

记共同变换后的硬源为 \(y^{\mathrm c}=\sqrt Q\,O^*Wy\)。由 (2.3) 准确得到
\[
 B_Ly^{\mathrm c}=\varepsilon^{-1/2}R_\varepsilon\widetilde y,
 \qquad B_Hy^{\mathrm c}=\varepsilon^{-1/2}\widetilde y,
\]
其中
\[
 \widetilde y=
 \binom{1-2\varepsilon\mathbb E[U A_{00}(\varepsilon U)]}
       {2\mathbb E[U(1-\varepsilon U)B(\varepsilon U)]}.
\]
这个向量也有统一 \(C^N\) 界。

令 \(\widehat J=B_LJ^{\mathrm c}B_H\)。保持原乘法次序，严格有
\[
 \boxed{
 {\cal F}(\varepsilon):=\varepsilon\widehat J
   =R_\varepsilon\widehat H{\cal C}
      -R_\varepsilon\widetilde y\widetilde y^*
      -2\varepsilon^2\widehat G R_\varepsilon^{-1}.}       \tag{4.1}
\]
最后一项中的表面负幂只留下一个正的 \(\varepsilon\)。取上文 \(N\ge5\)，则 \({\cal F}\) 至少有统一 \(C^2\) 延拓，尤其
\[
                         \sup_{\varepsilon\le\varepsilon_0}
                                   \|{\cal F}''(\varepsilon)\|\le C.       \tag{4.2}
\]
这一界已经独立于旧固定profile定理，且对任意维数和 \(d\to0\) 一致。

## 5. 用已成真实单轴身份识别零jet

固定一个有限 \(m\)、正有理比例 \(\omega_i\) 和允许正权profile。取 \(Q\) 为其公共分母的整数倍，便得到实际正整数 \(q_i\) 且 \(\varepsilon=1/(Qd)\to0\)。

[已成完整严格端峰定理](2026-11-14-balanced-star-strict-endpoint-full-phase-decay-789f-next.md)对每个这样的固定profile证明原相位为 \(O(Q^{-2})\)。结合第3节真实正定Gram，这给
\[
                  \widehat J=O(Q^{-1})=O(\varepsilon),
                  \qquad {\cal F}=O(\varepsilon^2)
\]
沿该真实整数序列成立。既然 \({\cal F}\) 已有二阶右Taylor展开，严格迫使
\[
                         {\cal F}(0)={\cal F}'(0)=0.       \tag{5.1}
\]
此处只用旧定理的每个固定profile结论来识别两个**准确零系数**；没有把旧定理依赖profile的余项常数当作统一常数。

对一般正实比例，在固定有限维的局部连续正交帧中用正有理比例逼近，(5.1) 的矩阵系数连续，故仍为零。用于微分的正实 \(q_i\) 扩展仅由 (3.2) 的正积分定义；不将非整数 \(q_i\) 冒称原Boolean组，也不需要在非整数参数上另假旧定理。

最后由 (4.2)、(5.1) 的积分Taylor公式，
\[
 {\cal F}(\varepsilon)
       =\varepsilon^2\int_0^1(1-v){\cal F}''(v\varepsilon)\,dv,
 \qquad \|\widehat J\|\le C\varepsilon.
\]
第3节的两个真实端度量一致正定，因此
\[
 \widehat J^*\widehat L^{-1}\widehat J
                  \preceq C\varepsilon^2\widehat H.
\]
通过同一可逆源合同返回原模型，得到 (0.1)。

本稿补的是 \(S/R\le K_0\) 的整个端峰区，允许该 \(S\) 本身趋于无穷。与另一大第二亮方向的角点证明接合时，只取固定 \(K_0\) 分界；仍须分别处理端点高斯窗口及内峰，并保有界正权这一适用前提。
