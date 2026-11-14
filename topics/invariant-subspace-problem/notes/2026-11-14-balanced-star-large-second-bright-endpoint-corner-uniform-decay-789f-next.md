# 平衡 star 真端峰的大二阶亮方向：双参数去极点与全源统一衰减

日期：2026-11-14；工作标识：789f。

## 0. 定理与新增范围

固定 \(0<a\le b<\infty\)。组数 \(m\)、正整数 \(q_i\) 任意，令
\[
 Q=\sum_iq_i,\qquad a\le z_i\le b,\qquad
 R=\sum_iq_i(1-z_i)>0,\qquad S=\sum_iq_i(z_i-1)^2.
\]
使用真实平衡 star 的整个低 primitive 源，记
\[
 G=\operatorname{Cov}X,\quad
 H=\mathbb E\frac{1-T}{T}XX^*,\quad
 L=\mathbb E\frac{T}{1-T}(1-X)(1-X)^*,
\]
\[
 y=2\mathbb EX-\mathbf1,\quad J=HG^{-1}L-2G-yy^*,\qquad
 \Phi=H^{-1/2}J^*L^{-1}JH^{-1/2}.
\]
其概率实现是
\[
 F_Q(t)=\prod_i(1-t+z_it)^{q_i},\quad \rho_Q=F_Q/\int_0^1F_Q,
 \quad K_i\mid T=t\sim\operatorname{Bin}(q_i,p_i(t)),
 \quad p_i(t)=\frac{z_it}{1-t+z_it},\quad X_i=K_i/q_i.
\]

存在只依赖 \(a,b\) 的 \(K_*,\delta_*,C<\infty\)，使
\[
 \frac SR\ge K_*,\qquad \frac S{R^2}\le\delta_*
                                                        \tag{0.1}
\]
蕴含
\[
 \boxed{\quad 0\preceq\Phi\preceq
          C\left(\frac S{R^2}\right)^2I.\quad}             \tag{0.2}
\]
所有常数不依赖 \(Q,m,\min q_i\)，允许全部 \(q_i=1\)。进一步缩小
\(\delta_*\)，可使右侧小于任意预先固定的正数。

这是同时 \(S/R\) 很大而 \(S/R^2\) 很小的实际有限模型结论；没有先固定维数再取极限。证明保留完整 \(G^{-1}\)、整个源和两个亮方向。所用常数由有限阶联合导数和紧区间正谱取得；本文没有把它们逐项汇总为数值常数。

原已付的有界 \(S\) 全漂移定理不覆盖这里。本文也不把 (0.2) 自动扩展到
\(S/R\le K_*\)。真端峰的这一互补区域需要另一个对有界二阶亮方向统一的论证；不能只引用有界 \(S\) 稿。权取倒数并交换 \(T,1-T\) 给相同的右端峰结论，使用倒数权自己的 \(R,S\)。

## 1. 准确双参数与完整固定源

置
\[
 \omega_i=q_i/Q,\quad \zeta=\sum_i\omega_i z_i=1-R/Q,\quad
 x_i=z_i/\zeta,\quad \theta^2=\sum_i\omega_i(x_i-1)^2.
\]
在 (0.1) 的阈值足够大时 \(\theta>0\)、\(\zeta\in[1/2,1]\)，
\(x_i\) 位于只依赖 \(a,b\) 的正紧区间。定义
\[
 u^2=\frac R{Q\theta^2},\qquad
 v^2=\frac{Q\theta^2}{R^2},\qquad \epsilon=u^2v^2.
\]
则以下等式全部准确：
\[
 Q=(\theta^2u^4v^2)^{-1},\quad
 \zeta=1-\theta^2u^2,\quad z_i=\zeta x_i,\quad
 R=\epsilon^{-1},                                      \tag{1.1}
\]
\[
 \frac SR=\frac{\zeta^2}{u^2}+\theta^2u^2,\qquad
 \frac S{R^2}=v^2(\zeta^2+\theta^2u^4).                   \tag{1.2}
\]
因此所需区域是 \(u,v\) 同时充分小的角点。

以下固定一个有限的 profile \((\omega,x)\)，仅改变 \(u,v\)。不要求在不同
profile 之间选全局光滑的基。令
\[
 W=\operatorname{diag}(\sqrt{\omega_i}),\quad
 u_0=(\sqrt{\omega_i})_i,\quad u_1=(\sqrt{\omega_i}x_i)_i,
 \quad v_c=(u_1-u_0)/\theta.
\]
取 \(F\) 为 \(u_1^\perp\) 的正交等距基，\(E\) 为
\(\{u_0,u_1\}^\perp\) 的正交等距基。设
\[
 h_0=u_1/(1+\theta^2),\quad
 K_\theta=[h_0,F/\theta],\quad
 f_c=F^*v_c,\quad \|f_c\|^2=(1+\theta^2)^{-1},
\]
\[
 e_0=(1,0)^T,\quad
 k=K_\theta^*u_0=((1+\theta^2)^{-1},-f_c)^T,
\]
\[
 \ell_0=(1,-\theta^2f_c)^T,\quad
 \ell_1=(1,f_c)^T,\quad E_0=(0,F^*E)^T.                   \tag{1.3}
\]
这些列组成的完整基及其逆统一有界，且
\[
 k^*\ell_0=1,\quad k^*\ell_1=0,\quad e_0^*\ell_1=1,
 \quad E_0^*k=E_0^*e_0=0.
\]
共同源合同是 \(K_\theta^*W\)。所有以下 \(H_\theta,G_\theta,L_\theta,y_\theta\)
和 \(J_\theta\) 都在这个同一完整源中；因此
\[
 J_\theta=H_\theta G_\theta^{-1}L_\theta
                    -2G_\theta-y_\theta y_\theta^*.
\]

真实的 \(\theta^{-1}\) 消去是
\[
 \frac{\|F^*(\sqrt{\omega_i}f(x_i))_i\|}{\theta}
 \le C\|f\|_{C^1},
                                                        \tag{1.4}
\]
因为 \(F^*u_1=0\)，可减去 \(f(1)x\)，而
\(\sum\omega_i(x_i-1)^2=\theta^2\)。此外，对每个固定 \(j\ge2\)，
\[
 \sum_i\omega_i|x_i-1|^j\le C^{j-2}\theta^2.              \tag{1.5}
\]
(1.4)–(1.5) 支付所有有限阶导数中的 \(\theta^{-1},\theta^{-2}\)。
不能只估计 \(K_\theta\) 自身的范数。

## 2. 联合光滑的标量密度，含移动端点

令 \(T=\epsilon U\)，并记 \(c_i'=\zeta x_i-1\)。真实未归一密度的指数为
\[
 \psi(u,v,U)=\frac1{\theta^2u^4v^2}
       \sum_i\omega_i\log(1+c_i'\epsilon U),\quad
              0\le U\le\epsilon^{-1}.
\]
其准确线性项为 \(-U\)。用
\[
 \log(1+s)=s-s^2\int_0^1\frac{1-r}{(1+rs)^2}\,dr
\]
得到不含隐蔽负幂的形式
\[
 \psi=-U-\frac{v^2U^2}{\theta^2}
  \sum_i\omega_i(c_i')^2
       \int_0^1\frac{1-r}{(1+r c_i'\epsilon U)^2}\,dr.    \tag{2.1}
\]
只要实际 \(z_i\) 保持在固定正区间，分母在整段 \(T\in[0,1]\) 都统一远离零。
(1.5) 及 \(c_i'=x_i-1-\theta^2u^2x_i\) 表明，(2.1) 的任意所需有限阶
\(u,v\) 导数均由只依赖阶数和权区间的 \(U\) 多项式控制。
同时凹性直接给
\[
                    \psi(u,v,U)\le-U.                 \tag{2.2}
\]
因此所有所需有限阶矩、解析向量函数和对角函数的积分都联合 \(C^N\)，
且导数界与维数、组数、\(\theta\) 无关。可取任意预先固定的有限 \(N\)。

移动上端 \(\epsilon^{-1}\) 的边界项由
\(e^{-\epsilon^{-1}}\) 乘有限负幂控制，在两坐标轴处平坦。
这里没有分别除以 \(1-T\) 后在 \(T=1\) 粗估：以下原 Gram 的这些分母
都在真实条件均值/噪声中先消去。

在 \(u=v=0\) 时 \(U\) 为均值一的指数分布。在 \(u=0,v>0\) 轴，
极限密度准确为
\[
                       e^{-U-v^2U^2/2}\,dU;
\]
在 \(v=0,u>0\) 轴则为 \(e^{-U}\,dU\)。仅分别存在这两个极限并不足够；
上面的联合导数界是后续去极点的必要输入。

## 3. 真实三 Gram 的联合正定归一

定义
\[
 {\cal D}_\theta[f]=\theta^2K_\theta^*
                       \operatorname{diag}(f_i)K_\theta,\quad
 Y(t)=K_\theta^*Wp(t),\quad
 N(t)=K_\theta^*W(1/(1+c_i't))_i.
\]
由 (1.4) 和准确有理式，
\[
 Y(\epsilon U)=\epsilon\zeta U e_0+
                    \epsilon^2U^2{\cal R}(u,v,U),       \tag{3.1}
\]
其中 \({\cal R}\) 的所需有限阶导数以 \(U\) 多项式统一控制。
又
\[
 k-Y(t)=(1-t)N(t),                                      \tag{3.2}
\]
从而
\[
 \ell_1^*N(\epsilon U)=\epsilon{\cal N}_1,\quad
 E_0^*N(\epsilon U)=\epsilon^2{\cal N}_E,\quad
 {\cal N}_1=-\zeta U+O(\epsilon U^2),                    \tag{3.3}
\]
所有余项仍是联合光滑的统一向量。后一式须保留 \(E_0\) 同时杀掉 \(k,e_0\)。

真实条件噪声在共同源中为
\(u^4v^2{\cal D}_\theta[p(1-p)]\)。于是三个完整形式准确分成
\[
 H_\theta=\mathbb E\frac{1-T}{T}YY^*
       +u^4v^2\mathbb E{\cal D}_\theta
          \left[\frac{z_i(1-T)^2}{(1+c_i'T)^2}\right],
\]
\[
 G_\theta=\operatorname{Cov}Y
       +u^6v^4\mathbb E{\cal D}_\theta
          \left[\frac{z_iU(1-\epsilon U)}{(1+c_i'\epsilon U)^2}\right],
\]
\[
 L_\theta=\epsilon\mathbb E[U(1-\epsilon U)NN^*]
       +u^8v^6\mathbb E{\cal D}_\theta
          \left[\frac{z_iU^2}{(1+c_i'\epsilon U)^2}\right]. \tag{3.4}
\]
特别是最后一式没有端点奇异分母。

取完整可逆源矩阵
\[
 C_H=\operatorname{diag}(u^{-1}v^{-1},u^{-2}v^{-1}I),
\]
\[
 C_G=\operatorname{diag}(u^{-2}v^{-2},u^{-3}v^{-2}I),
\]
\[
 C_L=[u^{-1}v^{-1}\ell_0,\
             u^{-3}v^{-3}\ell_1,\
             u^{-4}v^{-3}E_0].                          \tag{3.5}
\]
令 \(\widehat H=C_H^*H_\theta C_H\)、\(\widehat G=C_G^*G_\theta C_G\)、
\(\widehat L=C_L^*L_\theta C_L\)。由 (3.1)–(3.4)，三者均联合 \(C^N\)，
所有导数在算子范数中统一有界。

为把这一点逐项说明：\(C_G^*Y\) 的两块为
\(\zeta U+O(\epsilon U^2)\) 和 \(uv^2U^2{\cal R}_\perp\)；
\(G\) 的归一噪声块所带幂为 \(u^2,u,1\)。
\(H\) 的噪声有相同非负幂，其确定项经过
\(\sqrt{(1-T)/T}\) 后同样只含非负幂。
\(L\) 的确定项由 (3.3) 化为三列
\[
 O(1),\quad {\cal N}_1,\quad uv^2{\cal N}_E,
\]
而其归一噪声六种块分别带
\(u^6v^4,u^4v^2,u^3v^2,u^2,u,1\)。
这些都是完整向量/算子界，不是逐 entry 界再乘维数。

记 \(D_x=\operatorname{diag}(x_i)\)。角点准确为
\[
 \widehat H(0,0)=\widehat G(0,0)
                 =\operatorname{diag}(1,F^*D_xF),
\]
\[
 \widehat L(0,0)=
 \operatorname{diag}\left(
        \begin{pmatrix}1&-2\\-2&6\end{pmatrix},
                          2E^*D_xE\right).              \tag{3.6}
\]
因此存在统一的小矩形 \(0\le u\le u_*,0\le v\le v_*\)，使三者都具有
统一正谱下界和有限上界。完整 \(\widehat G^{-1}\) 的有限阶导数也统一。
这里先证明全矩阵正定再取逆，没有先压到亮源后反演。

## 4. 完整非交换 J 只有有限单项式极点

设
\[
 \widehat J=C_L^*J_\theta C_H,\qquad
                    {\cal A}(u,v)=u^8v^4\widehat J.     \tag{4.1}
\]
下面给出其联合光滑性的一份直接完整式，避免只说“形式 Laurent 展开”。

由 (3.4)，
\[
 \widetilde H=H_\theta/(u^2v^2),\quad
 \widetilde L=L_\theta/(u^2v^2)
\]
联合 \(C^N\) 且统一有界。令
\[
 P_H=u^2v C_H=\operatorname{diag}(u,I),\qquad
 P_L=u^4v^3C_L=[u^3v^2\ell_0,u\ell_1,E_0],
\]
\[
 M_G=u^6v^4G_\theta^{-1}
       =\operatorname{diag}(u,I)\widehat G^{-1}
                          \operatorname{diag}(u,I).
\]
则准确保持原次序的恒等式是
\[
 {\cal A}
 =P_L^*\widetilde H M_G\widetilde L P_H
       -2u^2P_L^*G_\theta P_H
       -u^2P_L^*y_\theta y_\theta^*P_H.                 \tag{4.2}
\]
所有因子已经在 §2–3 得到联合 \(C^N\) 和统一混合导数。
所以 (4.1) 的分子确实具有这些性质，且没有
\(u^2+v^2\) 之类可能产生角点非一致性的未消分母。
取 \(N\ge16\) 足够。

## 5. 仅用真实单轴结果消去全部低阶 jet

这里需要的已付单轴输入准确为：

1. [大总曲率高斯窗口](2026-11-14-balanced-star-large-total-curvature-gaussian-window-contraction-789f-next.md) 的完整源极限，
   或其先前固定 profile 高斯三尺度定理：固定 \(v>0\)，
   \(\nu=1/v\)、\(\tau=u^2v\)，\(u\to0\) 时完整相位有有限极限。
   这里只需每个固定参数的有界性，不借用关于无界 \(\nu\) 的统一误差。
2. [严格端峰完整相位衰减](2026-11-14-balanced-star-strict-endpoint-full-phase-decay-789f-next.md)：
   固定 \(u>0\)、profile 和 \(\theta>0\)，权
   \(z_i=(1-\theta^2u^2)x_i\) 不变，均值严格小于 \(1\)；
   \(v\to0\) 等价 \(Q\to\infty\)，其完整相位为 \(O(Q^{-2})=O(v^4)\)。
   因 (3.6) 附近归一 Gram 有界且可逆，故
   \(\widehat J=O(v^2)\)。

第一条使用上述已入主线的大总曲率稿 §§4–6；该输入是同一真实 \(J\)，不是单独 \(\Gamma\) 比较。

为不把非整数计数免费称为物理源，可以如下取得轴 jet。先令全部
\(\omega_i\) 为有理数。固定 \(v>0\)，沿 \(Q\) 为共同分母整数倍的序列选 \(u\to0\)；
固定 \(u>0\)，同样选 \(v\to0\)。两列模型均是真实正整数 \(q_i\)。
在第一列若 \({\cal A}\) 的任一 \(u\) 次数小于 \(8\) 的首个 jet 非零，
则 \(u^{-8}v^{-4}{\cal A}\) 沿该物理序列发散，与第一条矛盾。
第二列同理：\(\widehat J=O(v^2)\) 迫使
\[
 \partial_u^j{\cal A}(0,v)=0\quad(0\le j<8),\qquad
 \partial_v^j{\cal A}(u,0)=0\quad(0\le j<6).             \tag{5.1}
\]
对任意固定有限 profile，用正有理 \(\omega\) 逼近并把 \(x\) 重新归一到
\(\sum\omega_i x_i=1\)。在该 profile 邻域可选择连续的正交帧；
(4.2) 的有限 jets 连续，故 (5.1) 传到任意正实 \(\omega\)。
所有统一界本来就独立于这些帧和组数。

计算联合导数时采用正实 \(q_i=\omega_iQ\) 的积分延拓：
条件均值仍为 \(p_i\)，条件协方差为
\(\operatorname{diag}(p_i(1-p_i)/q_i)\)，所以三 Gram 仍有准确正实现
（亦可用给定 \(T\) 的独立 Gaussian 实现这两个条件矩）。
此延拓仅用于参数微分；最终定理和上述消 jet 序列都保持真实整数物理模型。

## 6. 双 Taylor 积分给统一有限模型预算

由联合 \(C^{14}\) 及 (5.1)，算子值 Taylor 积分给
\[
 {\cal A}(u,v)=
 \frac{u^8v^6}{7!\,5!}\int_0^1\!\!\int_0^1
   (1-s)^7(1-t)^5
   (\partial_u^8\partial_v^6{\cal A})(su,tv)\,ds\,dt.
                                                               \tag{6.1}
\]
因此
\[
                        \|\widehat J\|\le C_1v^2.       \tag{6.2}
\]
这一步是联合混合导数估计；单独沿两条轴有界不能替代它。

用 §3 的两个真实源度量，
\[
 \|\widehat L^{-1/2}\widehat J\widehat H^{-1/2}\|
                          \le C_2v^2.
\]
任意两个可逆源合同保持原相位的广义奇异值，故
\[
                             \Phi\preceq C_2^2v^4I.    \tag{6.3}
\]

最后将参数送回原 \(R,S\)。记 \(C_z=\max(|a-1|,|b-1|)\)。
\(S\le C_z^2Q\)，所以 \(S/R\) 足够大时 \(\zeta\ge1/2\)，且
\[
 Q\theta^2=\frac{S-R^2/Q}{\zeta^2},\qquad
 u^2\le\frac{2R}{S},\qquad
 v^2\le\frac{4S}{R^2}.
\]
增大 \(K_*\)、缩小 \(\delta_*\)，即保证 \(u\le u_*,v\le v_*\)；
(6.3) 得到 (0.2)。

## 7. 保留的范围

本稿实质支付了此前“大 \(S/R\)、小 \(S/R^2\)”共同端峰角点的整个源，
并给趋零费用，而非只得到新的等价表示。完整逆、均值硬列、两个亮方向和全部
条件二项噪声都保留。

整个正权有界区间的真端峰还需合并 \(S/R\le K_*\) 的统一端峰论证；
固定 \(S\) 或固定 profile 的旧结论单独不能承担这个量词。
本稿也没有将平衡 star 相位界直接当作原无限 graph 的跨出生/未知锚速率预算。

本稿的互补区现已由[二次偏差与漂移比有界的完整端峰定理](2026-11-14-balanced-star-bounded-second-bright-endpoint-uniform-decay-789f.md)支付：S/R≤K0且R充分大时Φ≤C/R²。两稿的统一常数均只依固定正权区间及所取固定分界；全部区域接合另行登记。
