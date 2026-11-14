# 平衡 star 的近端内峰：完整光滑角点、双轴消极点及统一有限界

日期：2026-11-14；工作标识：789f。

## 0. 结论与证明所接的两条真实边界

固定 \(0<a\le b<\infty\)。小组数 \(m\)、组大小 \(q_i\in\mathbb N\) 任意，\(Q=\sum_iq_i\)，\(a\le z_i\le b\)。主组长度 \(Q\)、权平方 \(1\)。令真实乘积
\[
 F_Q(T)=\prod_i(1-T+z_iT)^{q_i}
\]
有严格内峰 \(t\in(0,1)\)，定义
\[
 \lambda_i=\frac{z_i-1}{1+t(z_i-1)},\quad
 M=\sum_iq_i\lambda_i^2,\quad
 r=\frac1{t\sqrt M},\quad u=\sqrt t.                     \tag{0.1}
\]
使用平衡 star reducing 模块的整个 \(m\) 维低 primitive 源及一维硬源。

存在只依赖 \(a,b\) 的 \(u_*,r_*,C>0\)，使
\(0<u\le u_*,\,0<r\le r_*\) 时，原完整相位
\[
 J=HG^{-1}L-2G-yy^*,\qquad
 \Phi=H^{-1/2}J^*L^{-1}JH^{-1/2}
\]
满足
\[
                    \boxed{\Phi\preceq[1+C(u+r)]I.}     \tag{0.2}
\]
增加统一阈值后，特别有 \(\Phi\preceq2I\)。常数不依赖
\(m,Q,\min q_i\) 或归一权方差的正下界。

这处理 \(t\to0\) 且 \(t\sqrt M\to\infty\) 的完整联合尺度。倒数权与端点反射给 \(t\to1\) 的对应结论。

证明使用两个已经在同一真实源上证明的单轴结论：

1. [大总曲率高斯窗口](2026-11-14-balanced-star-large-total-curvature-gaussian-window-contraction-789f-next.md)：固定 \(r>0\)，令 \(u\to0\)，归一高斯参数趋 \(-1/r\)，完整相位有界。
2. [总曲率内峰统一界](2026-11-14-balanced-star-dimension-free-interior-total-curvature-bound-789f-next.md)：固定 \(u>0\)，令 \(r\to0\)，完整相位趋一个秩 \(m-1\) 投影。

本稿的新工作是证明所有实际归一 Gram 在整个角点具有维数无关的联合光滑性，然后用双 Taylor 积分除法支付两轴之间的区域。没有将逐点边界收敛直接用紧性换成联合界。

## 1. 正实组大小的连续延拓

为了在 \((u,r)\) 上做微分，必须明确处理通常非整数的 \(q_i\)。以下连续延拓只用于证明，不将它冒称为新的 Boolean 物理模块。

对任意正实 \(q_i\)，保持 \(T\) 的密度 \(F_Q/\int F_Q\)，给定 \(T\) 后取独立标准实 Gaussian \(\xi_i\)，令
\[
 X_i=p_i(T)+
       \sqrt{\frac{p_i(T)(1-p_i(T))}{q_i}}\,\xi_i,\qquad
 p_i(T)=\frac{z_iT}{1-T+z_iT}.                            \tag{1.1}
\]
其均值和全部二阶条件矩与整数 \(q_i\) 的
\(\operatorname{Bin}(q_i,p_i)/q_i\) 完全相同。因此
\[
 G=\operatorname{Cov}X,\quad
 H=\mathbb E\frac{1-T}{T}XX^*,\quad
 L=\mathbb E\frac{T}{1-T}(1-X)(1-X)^*,\quad
 y=2\mathbb EX-\mathbf1                                 \tag{1.2}
\]
在正实 \(q_i\) 上给出同样的矩阵积分公式，并在整数点准确回到实际物理源。

所有此前使用的积分恒等式仍然准确。例如直接对密度及 \(p_j\) 求导给
\[
 \partial_{\log z_i}\mathbb EX_j
  =q_i\operatorname{Cov}(p_i,p_j)
       +\delta_{ij}\mathbb E[p_i(1-p_i)]
  =q_iG_{ji}.                                          \tag{1.3}
\]
于是端点身份、完整非交换因式分解及所有有限有理系数身份均保持。两条单轴证明只用了这些积分、真实对角噪声
\(\operatorname{diag}(\mathbb E p_i(1-p_i)/q_i)\)、全源反演和 Laplace 展开；每一步对 (1.1) 同样成立。其维数无关证明也没有使用 \(q_i\ge1\) 或 \(m\le Q\)。因此本稿使用的两条单轴有界性确已延到全部正实 \(q_i\)，而非只在离散点上假设连续性。

## 2. 固定峰 score 的双参数族与统一积分微分

冻结当前模型的
\[
 \omega_i=q_i/Q,\qquad
 \sum_i\omega_i\lambda_i=0,\qquad
 \theta^2=\sum_i\omega_i\lambda_i^2>0.
\]
连续改变 \(u,r>0\)，令
\[
 t=u^2,\quad
 z_i(t)=\frac{1+(1-t)\lambda_i}{1-t\lambda_i},\qquad
 q_i(u,r)=\frac{\omega_i}{\theta^2t^2r^2}.                \tag{2.1}
\]
当前实际模型恰在此族中，且峰始终在 \(T=t\)。有
\(M=(t^2r^2)^{-1}\)。

若原 \(a\le z_i\le b\) 且 \(t\) 充分小，则所有 score 位于一个只依赖 \(a,b\) 的区间
\[
                    -1+\delta\le\lambda_i\le C,
 \qquad \delta>0.
\]
统一减小 \(u_*\) 后，(2.1) 的全部权都保持在固定正紧区间，且对
\(s\in[-t,1-t]\) 有 \(1+s\lambda_i\ge c>0\)。

令
\[
                      T=t(1+rU).
\]
积分域为
\[
 -1/r\le U\le(1/u^2-1)/r.
\]
真实相对峰指数准确写成
\[
 \log\frac{F_Q(t+trU)}{F_Q(t)}
                         =U^2g(trU),                   \tag{2.2}
\]
其中
\[
 g(s)=
 -\int_0^1(1-v)
       \frac{\sum_i\omega_i\lambda_i^2/(1+vs\lambda_i)^2}
            {\theta^2}\,dv.                            \tag{2.3}
\]
故 \(g(0)=-1/2\)，\(g(s)\le-c<0\)，而每个固定阶的 \(g\) 导数都一致有界。这来自
\(\sum\omega_i|\lambda_i|^{k+2}\le C^k\theta^2\)，没有单独估计
\(\theta^{-2}\)。

因为 \(tr=u^2r\)，(2.2) 的任意固定阶 \(u,r\) 导数都由一个固定次数的 \(U\) 多项式乘统一 Gaussian 尾控制。移动积分域的边界项也全部可控：

- 下端 \(U=-1/r\) 的指数为 \(g(-u^2)/r^2\le-c/r^2\)。所有有限阶 Leibniz 边界项仅多出 \(u,r,U\) 的有限次幂，因而在 \(r=0\) 平坦。
- 上端指数至多为 \(-c(1/u^2-1)^2/r^2\)，在统一小邻域内至多为 \(-c'/(u^4r^2)\)。所有边界导数都在两轴平坦。

因此，只要被积振幅及其有限阶导数具有统一的多项式增长，归一积分就联合延拓为闭角点上的 \(C^N\) 函数，并有统一导数界。归一化分母有统一正下界。以下需要 \(N=18\)，上述论证适用于这个固定有限阶。

## 3. 固定共同源与显式光滑正交基

置
\[
 W=\operatorname{diag}(\sqrt{\omega_i}),\quad
 u_0=(\sqrt{\omega_i})_i,\quad
 v=(\sqrt{\omega_i}\lambda_i/\theta)_i.
\]
取 \(F_0\) 为 \(u_0^\perp\) 的任意固定正交等距基，令
\[
 K_\theta=[\,u_0,F_0/\theta\,],\qquad f=F_0^*v.
\]
\(\|f\|=1\)。这里 \(K_\theta,F_0,f\) 都不随 \(u,r\) 改变。全部矩阵先共同合同到 \(K_\theta^*W\) 源，以下省略帽号。

分母 \(\theta\) 由真实均值零结构支付：对任意固定阶光滑函数 \(h\)，
\[
 \frac{\|F_0^*(\sqrt{\omega_i}h(\lambda_i))_i\|}{\theta}
 \le\|h'\|_\infty.
\]
而 \(\theta^2K_\theta^*\operatorname{diag}(h_i)K_\theta\) 的范数由
\(C\|h\|_\infty\) 控制。所有所需 \(u,r,T\) 导数均保留此性质。

在这个源中，峰均值及其补向量准确为
\[
 P(t)=t\binom{1}{(1-t)f},\qquad
 N(t)=(1-t)\binom{1}{-tf}.                               \tag{3.1}
\]
令 \(e_0=(1,0)\)、\(\widehat f=(0,f)\)，取固定等距列 \(E\) 张成
\(\{e_0,\widehat f\}^{\perp}\)。以下三套完整正交基只在同一个二维平面内显式旋转：
\[
 \mathcal F_H(t)=
 \left[
 \frac{e_0+(1-t)\widehat f}{\sqrt{1+(1-t)^2}},
 \frac{-(1-t)e_0+\widehat f}{\sqrt{1+(1-t)^2}},E
 \right],
\]
\[
 \mathcal F_L(t)=
 \left[
 \frac{e_0-t\widehat f}{\sqrt{1+t^2}},
 \frac{te_0+\widehat f}{\sqrt{1+t^2}},E
 \right],
\]
\[
 \mathcal F_G=
 \left[(e_0+\widehat f)/\sqrt2,\
       (-e_0+\widehat f)/\sqrt2,E\right].                \tag{3.2}
\]
这些基及全部固定阶导数一致有界，不产生维数或 \(\theta^{-1}\) 费用。

定义真实完整尺度
\[
 B_H=\mathcal F_H(t)\operatorname{diag}
                     (u^{-1},u^{-2}r^{-1}I_{m-1}),
\]
\[
 B_L=\mathcal F_L(t)\operatorname{diag}
            (u^{-1},u^{-3}r^{-1},u^{-4}r^{-1}I_{m-2}),
\]
\[
 B_G=\mathcal F_G\operatorname{diag}
                     (u^{-2}r^{-1},u^{-3}r^{-1}I_{m-1}).
                                                               \tag{3.3}
\]
所有坐标在 \(u,r>0\) 时可逆。\(m=2\) 时 \(E\) 及最深块为空。

## 4. 完整归一 Gram 的联合光滑性与角点正定

记 \(Y(T,t)=K_\theta^*Wp(T,t)\)，\(k=K_\theta^*W\mathbf1=e_0\)。准确单坐标公式为
\[
 p_i(T,t)=T\frac{1+(1-t)\lambda_i}{1+(T-t)\lambda_i}.      \tag{4.1}
\]
它给
\[
 Y(tV,t)=tV(e_0+\widehat f)+t^2R(V,t),\qquad V=1+rU,     \tag{4.2}
\]
其中所有所需导数有统一多项式增长。并且
\(p_i(1-p_i)=T(1-T)b_i(T,t)\)，其中 \(b_i\) 是一致正、导数一致有界的函数。

以下消零是逐点准确身份，不靠 Gaussian 奇矩：

- \(H\) 的全部对比源杀 \(Y(t,t)\)，且 \(Y(0,t)=0\)，故该条件均值列含因子 \(T(T-t)\)。
- \(L\) 的特殊对比源杀 \(k-Y(t,t)\)，且 \(k-Y(1,t)=0\)，故含因子 \((1-T)(T-t)\)。
- 最深 \(E\) 列同时杀 \(k,P(t),N(t)\)，故含因子 \(T(1-T)(T-t)\)。

除去这些因子后，所有固定阶导数仍一致有界。可直接由 (4.1) 核对；也可用二阶、三阶的积分型 divided difference，处理 \(0,t\) 在角点重合时的情形。后者只用同样的一致高阶导数界，不产生 \(1/t\)。

条件噪声的准确式为
\[
 t^2r^2\,\theta^2K_\theta^*
       \operatorname{diag}\{T(1-T)b_i(T,t)\}K_\theta.      \tag{4.3}
\]
代入 \(T=tV\)，它带 \(t^3r^2\)。因此 (3.3) 的所有负幂都被 (4.2)、逐点消零和 (4.3) 支付。例如：

- \(H\) 对比均值为 \(t^2rVU\) 乘有界列，乘 \(1/(tr)\) 后再用 \((1-T)/T\)，只余 \(tV(1-tV)U^2\) 乘有界 Gram；其噪声首项没有消失。
- \(L\) 特殊均值为 \(tr(1-tV)U\) 乘有界列，乘 \(t^{-3/2}r^{-1}\) 后，其平方费用为 \(V(1-tV)U^2\) 乘有界 Gram。
- \(L\) 最深均值为 \(t^2rV(1-tV)U\) 乘有界列，乘 \(t^{-2}r^{-1}\) 后，其确定费用带 \(t\)，真实噪声则留下非退化首项。
- \(G\) 的协方差可用两个独立 \(U,U'\) 的差平方表示；(4.2) 的差准确带 \(r(U-U')\)。在 \(\mathcal F_G\) 的对比方向，首个 \(tV(e_0+\widehat f)\) 项被杀，故额外带 \(t\)。

于是
\[
 H_*=B_H^*HB_H,\qquad L_*=B_L^*LB_L,\qquad
 G_*=B_G^*GB_G                                          \tag{4.4}
\]
都联合延拓为闭角点的 \(C^{18}\) 算子函数，且导数界与维数、组大小及 \(\theta\) 下界无关。所有高阶移动边界项由 §2 处理。

角点值可明确计算。令
\[
 \mathcal N=\theta^2K_\theta^*
                       \operatorname{diag}(1+\lambda_i)K_\theta,
 \qquad d_0=e_0+\widehat f.
\]
记 \(\mathcal N_c\) 为在 \(d_0^\perp\) 的 \(\mathcal F_G\) 对比基中的完整压缩，\(\mathcal N_E=E^*\mathcal NE\)。则
\[
 H_*(0,0)=\operatorname{diag}(2,\mathcal N_c),\qquad
 G_*(0,0)=\operatorname{diag}(2,\mathcal N_c),
\]
\[
 L_*(0,0)=\operatorname{diag}(1,1,\mathcal N_E).           \tag{4.5}
\]
这是标准 Gaussian 的 \(\mathbb EU=0,\mathbb EU^2=1\) 和全部真实噪声的结果。

因为 \(1+\lambda_i\ge\delta>0\)，
\(\mathcal N\succeq\delta\operatorname{diag}(\theta^2,I)\)。
若 \(x\perp d_0\)，则 \(|x_0|\le\|x_\perp\|\)，所以
\(\mathcal N_c\succeq(\delta/2)I\)，而
\(\mathcal N_E\succeq\delta I\)。上界也一致。结合统一一阶导数界，统一缩小 \(u_*,r_*\) 后，三个完整 \(H_*,L_*,G_*\) 在整个闭角点均有同一正谱区间。尤其 \(G_*^{-1}\) 的全部固定阶导数一致有界。

## 5. 清除有限单项式极点

令
\[
                         J_*=B_L^*JB_H.
\]
暂时不估计这个共同差。原 \(H,L,G,y\) 在 §3 的共同源中是联合光滑、导数统一有界的矩阵/向量函数；表面上的 \(1/T\)、\(1/(1-T)\) 由 \(Y(0,t)=0\)、\(k-Y(1,t)=0\) 和真实噪声的 \(T(1-T)\) 因子消掉。

由 (3.3)，
\[
 u^2r B_H=\mathcal F_H(t)\operatorname{diag}(ur,I),
\]
\[
 u^4r B_L=\mathcal F_L(t)
                     \operatorname{diag}(u^3r,u,I),
\]
\[
 u^6r^2G^{-1}
 =\mathcal F_G\operatorname{diag}(u,I)\,
       G_*^{-1}\,
          \operatorname{diag}(u,I)\mathcal F_G^*.        \tag{5.1}
\]
因此
\[
                         \mathcal A(u,r)=u^{12}r^4J_*(u,r)
                                                               \tag{5.2}
\]
联合 \(C^{18}\)，并有统一混合导数界。以乘积项为例，它正好等于
\[
 (u^4rB_L)^*\,H\,(u^6r^2G^{-1})\,L\,(u^2rB_H).
\]
另外两个项只多出非负的因子 \(u^6r^2\)，所以同样光滑。这里保持了完整 \(HG^{-1}L-2G-yy^*\)，没有分别把原大项当有界算子。

## 6. 算子值双 Taylor 除法

使用以下基本引理。设某矩阵族
\[
 A(u,r)=u^{-a}r^{-b}F(u,r),\qquad u,r>0,
\]
其中 \(F\) 在闭角点联合 \(C^{a+b+2}\)，所有相应混合导数有统一算子范数界。若对每个固定 \(r>0\)，\(A(u,r)\) 在 \(u\to0\) 时有界；且对每个固定 \(u>0\)，\(A(u,r)\) 在 \(r\to0\) 时有界，则 \(A\) 联合延拓为 \(C^2\)，其范数及至二阶导数有统一界。

证明如下。固定 \(r>0\) 的有界性迫使
\(\partial_u^jF(0,r)=0\)（\(j<a\)）。连续性将这些身份延到 \(r=0\)。Taylor 积分余项给
\[
 F(u,r)=\frac{u^a}{(a-1)!}
       \int_0^1(1-s)^{a-1}\partial_u^aF(su,r)\,ds.
\]
除去 \(u^a\) 后得到具有统一 \(C^{b+2}\) 界的 \(F_1\)。固定 \(u>0\) 的第二种有界性迫使
\(\partial_r^jF_1(u,0)=0\)（\(j<b\)），再由连续性包括 \(u=0\)。第二次 Taylor 积分便除去 \(r^b\)，给所需统一 \(C^2\) 界。整个论证对算子范数积分成立，不产生矩阵维数因子。

将它用于 (5.2)，取 \(a=12,b=4\)。两种轴有界性确实可用：

- 固定 \(r>0\)，\(u\to0\) 时，(2.1) 的
\(S_{\rm tot}\asymp1/(t^2r^2)\to\infty\)，且
\(D_{\rm tot}/\sqrt{S_{\rm tot}}\to1/r\)。因此大总曲率高斯窗口给完整 \(\Phi\) 有界。由 (4.4) 的有界正 Gram，\(J_*\) 也有界。
- 固定 \(u>0\)，\(r\to0\) 时，峰 \(t=u^2\) 固定在内点且 \(M=(t^2r^2)^{-1}\to\infty\)。完整内峰定理给 \(\Phi\) 有界，进而 \(J_*\) 有界。

这些是 §1 已证明正实组大小延拓后的真实矩阵结论；没有只在不相容的离散点上取轴极限。每条轴的常数可以依赖另一固定参数。联合常数来自 (5.2) 的统一混合导数及双 Taylor 公式。

遂得 \(J_*\) 的联合 \(C^2\) 界。因为 \(H_*,L_*\) 具有统一正谱区间，
\[
                        \Phi_*=H_*^{-1/2}J_*^*L_*^{-1}J_*H_*^{-1/2}
\]
也联合 \(C^2\)，并与原完整相位酉等价。

## 7. 角点投影及统一有限界

固定 \(u>0\) 沿 \(r\to0\)，原完整内峰证明给相位极限为秩 \(m-1\) 正交投影。经本稿的两端合法坐标，仍是同一完整源上的投影 \(\Pi(u)\)。联合连续性再令 \(u\to0\)，得到
\[
                      \Phi_*(0,0)=\Pi_0,\qquad
                      \Pi_0^2=\Pi_0=\Pi_0^*,
\]
其秩为 \(m-1\)。每个 profile 的源维数有限，故投影关系和秩在这个连续极限中保持；统一界本身不使用 trace 估计。

由统一一阶导数，
\[
                    \|\Phi_*(u,r)-\Pi_0\|\le C(u+r).
\]
这证明 (0.2)。角点可以由任意相对速度趋近，包含 \(t\) 比 \(r\) 的任何幂甚至比指数更小的情形。证明中没有把两个单轴极限用未经支付的紧性拼合。

本稿闭合了 bounded 正权的近端内峰尺度；与总曲率内峰、有限中央区及大曲率高斯窗口接合时，应继续保留各自实际参数范围。严格端峰的大漂移区以及权区间本身退化仍需相应证明，不能由本稿自动推出整个 ISP。
