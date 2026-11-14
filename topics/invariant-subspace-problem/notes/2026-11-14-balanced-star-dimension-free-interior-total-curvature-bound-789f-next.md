# 平衡 star 内峰区：总曲率控制的维数无关完整相位界

日期：2026-11-14；工作标识：789f。

## 0. 定理

固定 \(0<a\le b<\infty\) 和 \(0<\eta<1/2\)。小组数 \(m\)、正整数组大小 \(q_i\) 任意，\(Q=\sum_iq_i\)，小组权平方满足 \(a\le z_i\le b\)。主组长度 \(Q\)、权平方 \(1\)。

假设真实密度乘积
\[
 F_Q(t)=\prod_i(1-t+z_it)^{q_i}
\]
有唯一内峰 \(t_0\in[\eta,1-\eta]\)。记
\[
 \lambda_i=\frac{z_i-1}{1+t_0(z_i-1)},\qquad
 M=\sum_iq_i\lambda_i^2>0.                              \tag{0.1}
\]
使用平衡 star reducing 模块的整个 \(m\) 维低 primitive 源、一维硬源和原相位
\[
 J=HG^{-1}L-2G-yy^*,\qquad
 \Phi=H^{-1/2}J^*L^{-1}JH^{-1/2}.
\]

存在只依赖 \(a,b,\eta\) 的常数 \(C,M_0<\infty\)，使 \(M\ge M_0\) 时
\[
                         \boxed{\Phi\preceq(1+CM^{-1/2})I.}
                                                               \tag{0.2}
\]
更准确地，在下面给出的完整真实度量中，\(\Phi\) 距一个秩 \(m-1\) 正交投影的算子范数为 \(O(M^{-1/2})\)。故增加 \(M_0\) 后可取实际统一有限界 \(\Phi\preceq2I\)。

常数不依赖 \(m,Q,\min_iq_i\)，也不要求 \(M/Q\) 有正下界。特别允许全部 \(q_i=1\)、组数增长以及权方差趋零。这里 \(m=1\) 的非恒定权没有严格内峰，故定理假设自动排除它。

本稿严格升级
[原完整内峰投影极限](2026-11-14-balanced-star-macroscopic-interior-full-phase-projection-limit-789f-next.md)
的量词；并不把它的固定 profile 余项常数直接当作统一常数。由于极限有等号方向，本稿不声称有限 \(M\) 的最优常数 \(1\)。

## 1. 真实完整源及峰坐标

令 \(T\) 的密度为 \(F_Q/\int_0^1F_Q\)。给定 \(T=t\)，各
\[
 K_i\sim\operatorname{Bin}(q_i,p_i(t)),\qquad
 p_i(t)=\frac{z_it}{1-t+z_it},\qquad X_i=K_i/q_i
\]
独立。完整形式为
\[
 G=\operatorname{Cov}X,\quad
 H=\mathbb E\frac{1-T}{T}XX^*,\quad
 L=\mathbb E\frac{T}{1-T}(1-X)(1-X)^*,\quad
 y=2\mathbb EX-\mathbf1.                                \tag{1.1}
\]
这是已识别的实际平衡 star 物理源概率形式；共同物理正标量同时从全部三式及硬源平方中除去。

以下写
\[
 t=t_0,\quad a_0=t(1-t),\quad c_0=(1-t)/t,\quad
 \omega_i=q_i/Q,\quad \theta^2=\sum_i\omega_i\lambda_i^2=M/Q,
 \quad \tau=M^{-1/2}.
\]
峰条件准确给
\[
 \sum_i\omega_i\lambda_i=0,\qquad
 p_i(t)=t+a_0\lambda_i,\qquad
 n_i(t)=1-t-a_0\lambda_i.                               \tag{1.2}
\]
所有 \(\lambda_i\) 一致有界，且 \(p_i(t),n_i(t)\) 一致远离 \(0\)。这些界只依赖 \(a,b,\eta\)。

相对峰的实际密度有准确乘积式
\[
 \frac{F_Q(t+s)}{F_Q(t)}
               =\prod_i(1+s\lambda_i)^{q_i}.             \tag{1.3}
\]
对每个固定 \(r\ge2\)，
\[
 \sum_i\omega_i|\lambda_i|^r\le C^{r-2}\theta^2.
\]
因此换元 \(s=\tau u\) 后，
\[
 \log\frac{F_Q(t+\tau u)}{F_Q(t)}
 =-\frac{u^2}{2}
   +\sum_{r\ge3}\frac{(-1)^{r+1}}r
       \frac{\sum_i\omega_i\lambda_i^r}{\theta^2}
             \tau^{r-2}u^r.                            \tag{1.4}
\]
所有所需有限阶系数一致有界，即使 \(\theta\to0\)。

在整个实际积分区间上，\((1+s\lambda_i)\) 一致处于正紧区间，所以对数密度的二阶导数在峰尺度上由一个负常数控制。两端距峰至少 \(\eta/\tau\)，故尾积分统一指数小。有限 Taylor–Gaussian 展开因此给任意所需阶的统一矩余项。

此外展开的奇项积分为零：指数的 \(\tau^k\) 系数具有与 \(k\) 相同的 \(u\) 奇偶性，被积函数的 \(\tau^j\) 系数也具有与 \(j\) 相同的奇偶性。故完整归一期望按 \(\tau^2\) 的整数幂展开，端点误差指数小。

## 2. 支付趋零权方差的共同源预条件

置
\[
 W=\operatorname{diag}(\sqrt{\omega_i}),\qquad
 u_0=(\sqrt{\omega_i})_i,\qquad
 v=(\sqrt{\omega_i}\lambda_i/\theta)_i.
\]
则 \(\|u_0\|=\|v\|=1,\ u_0^*v=0\)。取 \(F_0\) 为 \(u_0^\perp\) 的任意正交等距基，令
\[
 K_\theta=[\,u_0,\ F_0/\theta\,],\qquad f=F_0^*v.
                                                               \tag{2.1}
\]
\(\|f\|=1\)。在这个完整共同源内，峰处两个均值准确变成
\[
 P=K_\theta^*Wp(t)=\binom{t}{a_0f},\qquad
 N=K_\theta^*Wn(t)=\binom{1-t}{-a_0f}.                   \tag{2.2}
\]
它们的范数和张成的二维基均一致良态，因为 \(t\in[\eta,1-\eta]\)。

预条件虽然含 \(\theta^{-1}\)，实际函数与噪声没有这个损失。对任何在 \(\lambda_i\) 的固定紧区间内具有统一一阶导数界的函数 \(g\)，
\[
 \frac{\|F_0^*(\sqrt{\omega_i}g(\lambda_i))_i\|}{\theta}
 \le\frac{\|(\sqrt{\omega_i}[g(\lambda_i)-g(0)])_i\|}{\theta}
 \le\|g'\|_\infty.                                     \tag{2.3}
\]
而
\[
 \theta^2K_\theta^*\operatorname{diag}(g_i)K_\theta
 =
 \begin{pmatrix}
 \theta^2u_0^*\operatorname{diag}(g)u_0&
       \theta u_0^*\operatorname{diag}(g)F_0\\
 \theta F_0^*\operatorname{diag}(g)u_0&
       F_0^*\operatorname{diag}(g)F_0
 \end{pmatrix}                                         \tag{2.4}
\]
的算子范数一致有界。

准确的单坐标恒等式
\[
 p_i(t+s)=(t+s)+
          \frac{(t+s)(1-t-s)\lambda_i}{1+s\lambda_i}      \tag{2.5}
\]
说明所有所需有限阶导数在 (2.3) 后都一致有界。条件二项协方差在共同 \(K_\theta^*W\) 源中准确为
\[
 \tau^2\theta^2K_\theta^*
        \operatorname{diag}\{p_i(T)(1-p_i(T))\}K_\theta.
                                                               \tag{2.6}
\]
所以任意 \(q_i=1\) 的噪声仍被完整保留；不存在单组中心极限定理的隐含前提。

下文给矩阵加帽表示同一个合同
\[
                   \widehat A=K_\theta^*WAWK_\theta
\]
及向量变换 \(\widehat a=K_\theta^*Wa\)。整个相位在这种共同坐标变换下酉等价。

## 3. 完整协方差首项与统一逆

令
\[
 d=K_\theta^*Wp'(t),\qquad
 \mathcal C=\theta^2K_\theta^*
               \operatorname{diag}(p_i(t)n_i(t))K_\theta+dd^*.
                                                               \tag{3.1}
\]
由 (1.4)、(2.5) 和完整噪声 (2.6)，
\[
                  \widehat G=\tau^2\mathcal C+O(\tau^4).
                                                               \tag{3.2}
\]
此处全部余项是维数无关算子范数。

\(\mathcal C\) 一致正定。事实上
\[
 p_i'(t)=1+(1-2t)\lambda_i-a_0\lambda_i^2
        =p_i(t)n_i(t)/a_0>0.
\]
所以
\[
 d_0=\sum_i\omega_ip_i'(t)=1-a_0\theta^2
\]
有统一正下界；其余分量由 (2.3) 一致有界。第一项则至少为
\[
                c\,\operatorname{diag}(\theta^2,I_{m-1}).
\]
即使删去其第一对角项，\(dd^*\) 仍支付第一方向：
\[
 |x_0|\le d_0^{-1}\bigl(|d^*x|+\|d_{\perp}\|\|x_\perp\|\bigr)
\]
给 \(\mathcal C\succeq c'I\)。上界由 (2.3)–(2.4) 同样一致。因此
\[
 \widehat G^{-1}
   =\tau^{-2}\mathcal C^{-1}+O(1)                       \tag{3.3}
\]
并有任意需要的更高阶统一展开。逆始终先在完整源上取得。

还保留一个准确的共同正交身份：
\[
                            P^*\mathcal C^{-1}N=0.      \tag{3.4}
\]
为自足核对，原首项
\[
 G_0=\operatorname{diag}(p_in_i/\omega_i)+p'p'^*/\theta^2
\]
由 Sherman 公式满足
\[
 G_0^{-1}=\operatorname{diag}(\omega_i/(p_in_i))
                                     -\omega\omega^*/a_0.
\]
因为 \(\sum\omega_i p_i=t,\sum\omega_i n_i=1-t\)，有
\(p^*G_0^{-1}n=0\)。而
\(\mathcal C=\theta^2K_\theta^*WG_0WK_\theta\)，故得到 (3.4)。
没有对压缩后的矩阵假设交换性。

## 4. 在共同源上保留非交换抵消

记 \(\mathbf m=\mathbb EX,\mathbf n=1-\mathbf m\)，
\(Z=\operatorname{diag}(z_i)\)，
\[
 a_1=Z\mathbf n,\quad b_1=Z^{-1}\mathbf m,\quad
 D_a=\operatorname{diag}((a_1)_i/q_i),\
 D_b=\operatorname{diag}((b_1)_i/q_i),\
 D_0=\operatorname{diag}(1/q_i),
\]
\[
 R=c_0\mathbf m-a_1,\qquad S=Z^{-1}R,\qquad c_0=(1-t)/t.
\]
在峰处 \(Zn=c_0p\)。统一偶次展开因而给
\[
 \widehat{\mathbf m}=P+O(\tau^2),\quad
 \widehat{\mathbf n}=N+O(\tau^2),\quad
 \widehat R,\widehat S=O(\tau^2),\quad
 \widehat D_a,\widehat D_b,\widehat D_0=O(\tau^2).        \tag{4.1}
\]
\(Z,Z^{-1}\) 在这个预条件源中的相似变换也一致有界，唯一可能的
\(\theta^{-1}\) 列由 (2.3) 支付。

真实端点量
\[
 \alpha=(\int F_Q)^{-1},\qquad
 \beta=\prod_i z_i^{q_i}/\int F_Q
\]
均至多为 \(C\tau^{-1}e^{-c\eta^2/\tau^2}\)。由
\[
 Gu_+=a_1-\alpha\mathbf m,\quad
 Gu_-=b_1-\beta\mathbf n,\qquad u_\pm=(Z^{\pm1}-I)q
\]
及它们的准确标量边界式，原共同差可写成
\[
\begin{split}
 J={}&\mathbf n\mathbf m^*-G-D_0+\mathbf nS^*
                         -R\mathbf m^*/c_0\\
 &+(D_a+a_1R^*/c_0)G^{-1}(D_b-Sb_1^*)+
                 O(e^{-c'/\tau^2}).                   \tag{4.2}
\end{split}
\]
(4.2) 是完整稿已证明的端点因式分解；其取得方法是把四个含 \(G^{-1}\) 的项合成同一个乘积，再准确消掉两个大均值平方。这里 (3.3)、(4.1) 证明它的指数余项在新源中也一致，未留下 \(\theta^{-1}\) 费用。

两个乘积因子为 \(O(\tau^2)\)，而完整逆为 \(O(\tau^{-2})\)。因此
\[
            \widehat J=NP^*+\tau^2\mathcal J_2+O(\tau^4)
                                                               \tag{4.3}
\]
具有统一有界系数和余项。没有分别估计
\(\widehat H\widehat G^{-1}\widehat L\) 与大的均值平方。

令 \(E_P,E_N\) 分别是 \(P^\perp,N^\perp\) 的任意正交等距基。全部对比方向的准确系数满足
\[
                      E_N^*\mathcal J_2E_P
                                  =-E_N^*\mathcal CE_P. \tag{4.4}
\]
为说明 (4.4) 不依赖固定方差假设，原完整代数证明使用
\[
 v_i=\frac{\sum_j\omega_j\lambda_j^3/\theta^2-\lambda_i}
                           {a_0\theta^2}
\]
及同一个 \(G_0^{-1}\)，得到
\[
 \mathcal T=-G_0+\alpha_Ppp^*-\alpha_Nnn^*
\]
的准确身份；因此任意左 \(n^\perp\)、右 \(p^\perp\) 测试都只剩 \(-G_0\)。
将这些测试取为 \(WK_\theta E_N,WK_\theta E_P\)，再乘
\(Q^{-1}=\theta^2\tau^2\)，恰得 (4.4)。
其中原 \(v_i\) 的单独大小可以发散；本稿不估计它，而用 (2.3)–(4.3) 先支付完整共同系数及余项。

## 5. 双超平面完整 Gram 与投影极限

由实际条件矩及 (3.2)，
\[
 \widehat H=c_0PP^*+O(\tau^2),\qquad
 \widehat L=c_0^{-1}NN^*+O(\tau^2),
\]
\[
 \tau^{-2}E_P^*\widehat HE_P
            =c_0E_P^*\mathcal CE_P+O(\tau^2),
\]
\[
 \tau^{-2}E_N^*\widehat LE_N
            =c_0^{-1}E_N^*\mathcal CE_N+O(\tau^2).        \tag{5.1}
\]
选 \(h_P=P/\|P\|^2,h_N=N/\|N\|^2\)，作完整两端坐标
\[
 B_H=[h_P,\tau^{-1}E_P],\qquad
 B_L=[h_N,\tau^{-1}E_N].
\]
这些首列范数一致有界。由 (4.3)–(4.4)、(5.1)，有
\[
 B_H^*\widehat HB_H=
  c_0\operatorname{diag}(1,E_P^*\mathcal CE_P)+O(\tau),
\]
\[
 B_L^*\widehat LB_L=
  c_0^{-1}\operatorname{diag}(1,E_N^*\mathcal CE_N)+O(\tau),
\]
\[
 B_L^*\widehat JB_H=
  \operatorname{diag}(1,-E_N^*\mathcal CE_P)+O(\tau).      \tag{5.2}
\]
误差为完整算子范数。最慢项是一个亮方向与一个对比方向的交叉：
原 \(O(\tau^2)\) 乘 \(\tau^{-1}\) 后为 \(O(\tau)\)；对比块
\(O(\tau^4)\) 乘 \(\tau^{-2}\) 后为 \(O(\tau^2)\)。
固定数目的块不会带来维数因子。

(5.2) 两端极限 Gram 有统一正谱区间。归一对比交叉是同一个
\(\mathcal C\) 内积中两个超平面之间的交叉 Gram。由 (3.4)，两法向
\(\mathcal C^{-1}P,\mathcal C^{-1}N\) 正交，所以其奇异值恰为
\(1\)（\(m-2\) 次）及 \(0\)。再加一维亮通道，完整极限相位为秩
\(m-1\) 正交投影。

统一谱区间内的逆平方根算子范数连续性将 (5.2) 变成
\[
                 \|\Phi-U^*\Pi U\|\le C\tau             \tag{5.3}
\]
（某个源酉 \(U\) 与秩 \(m-1\) 投影 \(\Pi\)）。因此得到 (0.2)。
这证明的是完整实际源的有限常数，不将投影极限的等号方向擅自判成有限参数下的正缺陷。

## 6. 与有限中央区的准确接合及尚余范围

若 \(M\) 有界，则
\[
 z_i-1=\frac{\lambda_i}{1-t\lambda_i},\qquad
 \sum_iq_i(z_i-1)
    =t\sum_iq_i\frac{\lambda_i^2}{1-t\lambda_i},
\]
因为 \(\sum_iq_i\lambda_i=0\)。分母在固定正权区间内一致有界且远离零，所以
\[
 \sum_iq_i(z_i-1)^2\le C M,\qquad
 \left|\sum_iq_i(z_i-1)\right|\le C M.                   \tag{6.1}
\]
故同一真实模型若已在“总平方偏差和总漂移均有界”的中央区取得统一有限预算，它与本稿就覆盖所有
\(a\le z_i\le b,\ t_0\in[\eta,1-\eta]\) 的完整平衡 star 源，无须限制
\(Q,m,q_i\) 或归一方差。这一接合只用 (6.1)，没有遗漏低曲率条带。

本稿尚不控制 \(t_0\to0\) 或 \(t_0\to1\) 时与内峰高斯宽度的联合尺度。
尤其端点距离乘 \(\sqrt M\) 趋无穷、但端点距离本身趋零的区间，需要另付统一的源尺度匹配。不能把本稿依赖 \(\eta\) 的常数直接用于那里。
