# 平衡 star 的大总曲率高斯窗口：允许权方差趋零的完整统一收缩

日期：2026-11-14；工作标识：789f。

## 0. 实际有限模型定理

固定 \(0<a\le b<\infty\) 和 \(\Lambda<\infty\)。小组个数 \(m\)、正整数组大小 \(q_i\) 任意，令
\[
 Q=\sum_iq_i,\qquad a\le z_i\le b,
\]
\[
 D_{\mathrm{tot}}=\sum_iq_i(z_i-1),\qquad
 S_{\mathrm{tot}}=\sum_iq_i(z_i-1)^2.                    \tag{0.1}
\]
主组长度为 \(Q\)、权平方为 \(1\)，小组总长度为 \(Q\)。使用这个真实平衡 star reducing 模块的整个 \(m\) 维低 primitive 源和一维硬源。

存在只依赖 \(a,b,\Lambda\) 的 \(S_*<\infty,\gamma>0\)，使得
\[
 S_{\mathrm{tot}}\ge S_*,\qquad
 |D_{\mathrm{tot}}|\le\Lambda\sqrt{S_{\mathrm{tot}}}       \tag{0.2}
\]
蕴含原完整相位
\[
 J=HG^{-1}L-2G-yy^*,\qquad
 \Phi=H^{-1/2}J^*L^{-1}JH^{-1/2}
\]
满足
\[
                         \boxed{\Phi\preceq(1-\gamma)I.} \tag{0.3}
\]
常数不依赖 \(Q,m,\min_iq_i\)，也不要求
\(Q^{-1}S_{\mathrm{tot}}\) 或归一权方差有正下界。允许全部 \(q_i=1\)，允许任意多的小组，同时允许权方差趋零。

本稿在
[维数无关临界窗口稿](2026-11-14-balanced-star-dimension-free-transition-contraction-789f-next.md)
的基础上进一步去掉方差下界。关键是新的共同源预条件，不能直接让旧稿的 \(\chi_-\) 趋零而保留旧余项常数。

结论只针对 (0.2) 的漂移窗口及本 reducing 模块；没有据此声称所有正权、全部出生或原无限 graph 已闭合。

## 1. 实际参数到归一高斯参数的准确转换

置
\[
 \omega_i=q_i/Q,\qquad
 \zeta=\sum_i\omega_i z_i=1+D_{\mathrm{tot}}/Q,\qquad
 x_i=z_i/\zeta,
\]
\[
 \theta^2=\chi=\sum_i\omega_i(x_i-1)^2,\qquad
 \tau=(Q\chi)^{-1/2},\qquad
 \nu=-D_{\mathrm{tot}}\tau.                              \tag{1.1}
\]
于是
\[
 \sum_i\omega_i x_i=1,\qquad
 z_i=(1-\nu\theta^2\tau)x_i,\qquad
 Q=\frac1{\theta^2\tau^2}.                              \tag{1.2}
\]
这只是实际参数的改写，没有改变主组权或原相位。

令 \(C_\delta=\max\{|a-1|,|b-1|\}\)。若 \(C_\delta=0\)，大曲率条件不可能发生，定理真空成立。否则
\[
 S_{\mathrm{tot}}\le C_\delta^2Q,\qquad
 |\zeta-1|\le\frac{\Lambda C_\delta^2}{\sqrt{S_{\mathrm{tot}}}}.
\]
故充分大 \(S_{\mathrm{tot}}\) 时 \(\frac12\le\zeta\le\frac32\)，并有
\[
 2a/3\le x_i\le2b,\qquad
 Q\chi=\frac{S_{\mathrm{tot}}-D_{\mathrm{tot}}^2/Q}{\zeta^2}.
                                                               \tag{1.3}
\]
又
\(D_{\mathrm{tot}}^2/Q\le\Lambda^2C_\delta^2\)，所以进一步增加阈值后，
\[
 \frac29 S_{\mathrm{tot}}\le Q\chi\le4S_{\mathrm{tot}},
 \qquad |\nu|\le(3/\sqrt2)\Lambda,\qquad
 0<\theta\le2C_\delta.                                  \tag{1.4}
\]
因此只须证明：\(x_i\) 在固定正紧区间、\(\nu\) 在固定紧区间、\(\theta\) 有固定上界但没有正下界时，充分小 \(\tau\) 有统一完整相位收缩。

## 2. 半线密度的统一展开

真实密度和条件计数为
\[
 F_Q(t)=\prod_i(1-t+z_it)^{q_i},\quad
 \rho_Q=F_Q/\int_0^1F_Q,\quad
 K_i\mid T=t\sim\operatorname{Bin}(q_i,p_i(t)),
\]
\[
 p_i(t)=\frac{z_it}{1-t+z_it},\qquad X_i=K_i/q_i .
\]
给定 \(T\) 后各组独立。完整形式是
\[
 G=\operatorname{Cov}X,\quad
 H=\mathbb E\frac{1-T}{T}XX^*,\quad
 L=\mathbb E\frac{T}{1-T}(1-X)(1-X)^*,\quad
 y=2\mathbb EX-\mathbf1.                                \tag{2.1}
\]

写 \(c_i=x_i-1\)。对每个固定 \(r\ge2\)，
\[
 \sum_i\omega_i|c_i|^r
       \le C^{r-2}\theta^2,                             \tag{2.2}
\]
其中 \(C\) 只依赖归一权区间。令 \(T=\tau U\)，则
\[
 \log F_Q(\tau U)
 =\frac1{\theta^2\tau^2}
       \sum_i\omega_i\log(1+\tau U(c_i-\nu\theta^2\tau x_i)).
\]
首两项准确为
\[
                        -\nu U-U^2/2.                  \tag{2.3}
\]
由于 (2.2)，每个后续固定阶的 \(\tau\) 系数均一致有界。例如三次修正为
\[
 \tau\left\{\nu\theta^2U^2+
         \frac{\sum_i\omega_ic_i^3}{3\theta^2}U^3\right\}.
\]
没有把 \(\theta^{-2}\) 单独粗估；每个这样的分母都由真实加权矩 (2.2) 支付。

在整个 \(t\in[0,1]\) 上，实际 \(z_i\) 一致位于正紧区间，且
\[
 \frac1{\theta^2}\sum_i\omega_i(z_i-1)^2
       =(1-\nu\theta^2\tau)^2+\nu^2\theta^2\tau^2
\]
一致远离零。因此换元后的指数二阶导数有统一负上界，积分尾由 \(C_1-c_1U^2\) 控制。有限 Taylor 展开加统一尾界给任意所需有限阶矩展开，其余项在算子应用中同样一致。

极限分布为
\[
 d\nu_0(U)=Z_\nu^{-1}e^{-\nu U-U^2/2}\,dU,\qquad U>0.    \tag{2.4}
\]
记
\[
 M_j=\mathbb E_{\nu_0}U^j,\quad \mu=M_1,\quad
 v=M_2-\mu^2.
\]
\(\nu\) 保持在固定紧区间，故 \(\mu,v,M_2,M_3\) 及
\(\mu M_3-M_2^2\) 都有统一正下界及有限上界。

两个实际端点参数
\[
 \alpha=(\int_0^1F_Q)^{-1},\qquad
 \beta=\prod_i z_i^{q_i}/\int_0^1F_Q
\]
满足
\[
 \alpha=\tau^{-1}Z_\nu^{-1}(1+O(\tau)),\qquad
 |\beta|\le C\tau^{-1}\exp(-c/\tau^2+C/\tau).             \tag{2.5}
\]
为证第二式，在固定正区间上取
\(\log x\le x-1-c_2(x-1)^2\)，用 (1.2) 得
\(Q\sum\omega_i\log x_i\le-c_2/\tau^2\)；
\(Q\log(1-\nu\theta^2\tau)=-\nu/\tau+O(1)\)。
这些界即使 \(\theta\) 趋零极快也一致。

## 3. 新共同源预条件

先作同源合同 \(W=\operatorname{diag}(\sqrt{\omega_i})\)。设
\[
 u_0=(\sqrt{\omega_i})_i,\qquad
 u_1=(\sqrt{\omega_i}x_i)_i,\qquad
 v_c=(u_1-u_0)/\theta.
\]
则
\[
 \|u_0\|=\|v_c\|=1,\quad u_0^*v_c=0,\quad
 u_1=u_0+\theta v_c.
\]
取 \(F\) 为 \(u_1^\perp\) 的任意正交等距基，置
\[
 h_0=u_1/(1+\theta^2),\qquad
 K_\theta=[\,h_0,\ F/\theta\,].                          \tag{3.1}
\]
这是真正可逆的完整源变换，逆为
\[
                  K_\theta^{-1}
                     =\begin{pmatrix}u_1^*\\\theta F^*\end{pmatrix}.
\]
虽然 \(\|K_\theta\|\) 可发散，以下所有实际对象在此共同坐标下都有统一界，不能只估计 \(K_\theta\) 的范数。

对向量函数 \(v_f=(\sqrt{\omega_i}f(x_i))_i\)，因为 \(F^*u_1=0\)，
\[
 \frac{\|F^*v_f\|}{\theta}
 \le \frac{\|v_{f-f(1)x}\|}{\theta}
 \le C\|f\|_{C^1([x_-,x_+])}.                           \tag{3.2}
\]
这里 \(f(x)-f(1)x\) 在 \(x=1\) 为零，故 (2.2) 的二阶式支付了全部 \(\theta^{-1}\)。这对所有所需有限阶解析系数统一成立。

令
\[
 Y_\theta(t)=K_\theta^*Wp(t),\qquad
 k_\theta=K_\theta^*u_0,\qquad
 \mathcal D_\theta[f]=\theta^2K_\theta^*
                       \operatorname{diag}(f_i)K_\theta.
\]
写 \(f_c=F^*v_c\)，则
\[
 k_\theta=\binom{(1+\theta^2)^{-1}}{-f_c},
 \qquad \|f_c\|^2=(1+\theta^2)^{-1}.                     \tag{3.3}
\]
此外
\[
 \mathcal D_\theta[f]=
 \begin{pmatrix}
  \theta^2h_0^*\operatorname{diag}(f)h_0&
       \theta h_0^*\operatorname{diag}(f)F\\
  \theta F^*\operatorname{diag}(f)h_0&
       F^*\operatorname{diag}(f)F
 \end{pmatrix},                                         \tag{3.4}
\]
所以 \(\|\mathcal D_\theta[f]\|\le C\max_i|f_i|\)，无维数或 \(\theta^{-1}\) 损失。

由
\[
 p_i(t)=\zeta x_it-
       \frac{\zeta x_i(\zeta x_i-1)t^2}
            {1+(\zeta x_i-1)t},\qquad
 \zeta=1-\nu\theta^2\tau,
\]
及 (3.2)，得到
\[
 Y_\theta(t)=\zeta t\,e_0+t^2R_\theta(t,\tau),            \tag{3.5}
\]
其中 \(e_0=(1,0,\ldots,0)^T\)，向量 \(R_\theta\) 及所有所需有限阶导数一致有界。

给定 \(T=t\)，原全部二项噪声在新源中准确为
\[
 \operatorname{Cov}(K_\theta^*WX\mid T=t)
       =\tau^2\mathcal D_\theta[p(t)(1-p(t))].            \tag{3.6}
\]
(3.6) 来自 \(1/Q=\theta^2\tau^2\)，没有使用单组中心极限定理，所以包括每个 \(q_i=1\)。

## 4. 三个完整 Gram 与完整逆的统一性

写
\[
 H_\theta=K_\theta^*WHWK_\theta,\quad
 G_\theta=K_\theta^*WGWK_\theta,\quad
 L_\theta=K_\theta^*WLWK_\theta.
\]
它们有以下真实同源表示：
\[
 G_\theta=\operatorname{Cov}(Y_\theta(T))
          +\tau^2\mathbb E\mathcal D_\theta[p(T)(1-p(T))],
\]
\[
 H_\theta=\mathbb E\frac{1-T}{T}
       \{Y_\theta(T)Y_\theta(T)^*
          +\tau^2\mathcal D_\theta[p(T)(1-p(T))]\},
\]
\[
 L_\theta=\mathbb E\frac{T}{1-T}
       \{(k_\theta-Y_\theta(T))(k_\theta-Y_\theta(T))^*
          +\tau^2\mathcal D_\theta[p(T)(1-p(T))]\}.       \tag{4.1}
\]
这些表示和 §2–3 给任意所需有限阶的算子范数展开；外积向量范数和对角算子范数已经一致控制，不能改成逐 entry 估计后乘维数。

令 \(D_x=\operatorname{diag}(x_i)\)。按 \(e_0\oplus e_0^\perp\) 分块，
\[
 G_\theta=
 \begin{pmatrix}
   \tau^2(v+O(\tau))&\tau^3O(1)\\
   \tau^3O(1)&\tau^3(\mu F^*D_xF+O(\tau))
 \end{pmatrix}.                                         \tag{4.2}
\]
所有 \(O(\cdot)\) 是与 \(m,\theta\) 无关的算子界。尤其在
\(\operatorname{diag}(\tau^{-1},\tau^{-3/2}I)\) 合同后，完整矩阵趋向
\[
                    \operatorname{diag}(v,\mu F^*D_xF)>0
\]
且余项 \(O(\tau^{1/2})\)。因此
\[
                         \|G_\theta^{-1}\|\le C\tau^{-3}. \tag{4.3}
\]
用完整两块 Schur 反演 (4.2)，得到具有统一有界系数的有限 Laurent 展开。其整数幂从 \(\tau^{-3}\) 开始；任意固定阶余项也一致。这一步保留了亮源与全部 nuisance，未将压缩与反演换序。

为了随后对 \(J\) 保共同抵消，而不是粗估三项，仍使用
[完整高斯过渡稿](2026-11-14-balanced-star-gaussian-transition-full-phase-bound-789f-next.md)
的准确端点因式分解。令原坐标
\[
 Z=\operatorname{diag}(z_i),\quad
 \mathbf m=\mathbb EX,\quad \mathbf n=1-\mathbf m,\quad
 a_0=Z\mathbf n,\quad b_0=Z^{-1}\mathbf m,
\]
\[
 c_0=(\mathbb ET)^{-1}-1,\quad
 R=c_0\mathbf m-a_0,\quad S=Z^{-1}R,\quad
 h=c_0-\alpha,\quad k=1-c_0\beta.
\]
在共同 \(K_\theta^*W\) 坐标中，
\[
 \mathbf m_\theta=\tau\mu e_0+O(\tau^2),\quad
 (a_0)_\theta=e_0+O(\tau),\quad
 (b_0)_\theta=\tau\mu k_\theta+O(\tau^2),
\]
\[
 R_\theta=O(\tau),\quad S_\theta=O(\tau),\quad
 h=\tau^{-1}v/\mu+O(1),\quad k=1+O(e^{-c/\tau^2}).        \tag{4.4}
\]
例如 \(R_\theta\) 的常数项由 \(c_0\mathbf m_\theta\) 与 \((a_0)_\theta\) 准确抵消。\(Z\) 和 \(Z^{-1}\) 在这个完整预条件源中的相似变换也一致有界：其唯一可能带 \(\theta^{-1}\) 的列由 (3.2) 支付。

两个完整乘积因子满足
\[
 A_\theta=(D_a+a_0R^*/h)_\theta=O(\tau^2),\qquad
 B_\theta=(D_b-Sb_0^*/k)_\theta=O(\tau^2).                \tag{4.5}
\]
这里 \(D_a=\operatorname{diag}((a_0)_i/q_i)\)，
\(D_b=\operatorname{diag}((b_0)_i/q_i)\)；其合同分别为
\(\tau^2\mathcal D_\theta[a_0]\)、
\(\tau^2\mathcal D_\theta[b_0]\)。

准确因式分解是
\[
\begin{split}
 J={}&\mathbf n\mathbf m^*-G-D_0
    +\frac{c_0\beta}{k}\mathbf n\mathbf n^*
    +\frac\alpha h\mathbf m\mathbf m^*
    +\frac1k\mathbf nS^*-\frac1hR\mathbf m^*\\
   &+(D_a+a_0R^*/h)G^{-1}(D_b-Sb_0^*/k).                \tag{4.6}
\end{split}
\]
(4.3)–(4.5) 表明 \(J_\theta=K_\theta^*WJWK_\theta\) 从 \(O(\tau)\) 开始，且可在完整源上展开到
\[
 J_\theta=\tau J_{\theta,1}+\tau^2J_{\theta,2}
                         +\tau^3J_{\theta,3}+O(\tau^4), \tag{4.7}
\]
所有系数和余项的算子范数一致有界。若需更高阶余项，只须在 §2 的真实矩和 (4.2) 的完整 Schur 中多取有限项。由于 (4.4)–(4.5) 的所有对象已统一，\(\beta\) 项中也不残留可能随 \(\theta^{-1}\) 发散的因子。

## 5. 既有三阶身份在新完整坐标中的准确形式

取 \(E\) 为 \(\{u_0,u_1\}^\perp\) 的正交等距基，令
\[
 E_0=\binom{0}{F^*E},\qquad P_c=\binom{0}{I_{m-1}},
\]
\[
 \ell_0=\binom{1}{-\theta^2 f_c},\qquad
 \ell_1=\binom{1}{f_c}.                                  \tag{5.1}
\]
这些向量/等距列和它们形成的完整基均一致良态，因为
\(\|f_c\|^2=(1+\theta^2)^{-1}\) 一致远离零。它们满足
\[
 k_\theta^*\ell_0=1,\quad k_\theta^*\ell_1=0,\quad
 e_0^*\ell_1=1,\quad E_0^*k_\theta=E_0^*e_0=0.           \tag{5.2}
\]

令半线分布 (2.4) 的
\[
 j_0=(2\mu^2-M_2)/\mu,\qquad
 j_2=(\mu^2-v)/v-2\mu^2.
\]
完整过渡稿的精确三阶恒等式，作
\[
 \varepsilon=\theta\tau,\quad
 \chi=\theta^2,\quad\lambda_{\mathrm{old}}=\nu\theta
\]
并合同到 \(K_\theta\) 后，成为
\[
 J_{\theta,1}=j_0 k_\theta e_0^*,\qquad
 J_{\theta,2}=k_\theta r_\theta^*+j_2 e_0e_0^*,          \tag{5.3}
\]
\[
                    E_0^*J_{\theta,3}P_c
                              =-j_0E^*D_xF.             \tag{5.4}
\]
某个 \(r_\theta\) 的具体表达无须保留；由 (4.7) 它一致有界。

为核对 (5.4) 的源因子，注意
\(K_\theta E_0=E/\theta\)、\(K_\theta P_c=F/\theta\)。
原三阶项带 \(\varepsilon^3=\theta^3\tau^3\)，原 \(j_0\) 带
\(\theta^{-1}\)，左右源各带 \(\theta^{-1}\)，恰好全部抵消。二阶 \(j_2\) 同理由 \(\theta^{-2}\) 与 \(\varepsilon^2\) 抵消。

(5.3)–(5.4) 是已证明的有限有理恒等式，对每个 \(\theta>0\) 准确成立。这里新付的是其整个余项在 \(\theta\to0\) 时仍一致，来自 §3–4；不是把固定 \(\theta\) 的渐近结论直接外推。

## 6. 完整三尺度 Gram 与严格缺口

在 \(K_\theta\) 源坐标内，取
\[
 C_H=\operatorname{diag}(\tau^{-1/2},\tau^{-1}I_{m-1}),
\]
\[
 C_L=[\,\tau^{-1/2}\ell_0,\
           \tau^{-3/2}\ell_1,\ \tau^{-2}E_0\,].          \tag{6.1}
\]
由 (4.1)、(5.2) 和真实条件噪声，
\[
 C_H^*H_\theta C_H=
 \operatorname{diag}(\mu,F^*D_xF)+O(\tau^{1/2}),          \tag{6.2}
\]
\[
 C_L^*L_\theta C_L=
 \operatorname{diag}
  \left(\begin{pmatrix}\mu&-M_2\\-M_2&M_3\end{pmatrix},
                         M_2E^*D_xE\right)
                  +O(\tau^{1/2}).                      \tag{6.3}
\]
例如 \(\ell_1\) 杀 \(k_\theta\) 而在 \(e_0\) 上取值 \(1\)，所以
\(L\) 的第二尺度来自 \(M_3\)；\(E_0\) 同时杀两个向量，因此最深层首项必须保留真实噪声
\(\tau^4M_2E^*D_xE\)。这也说明 \(q_i=1\) 的噪声没有消失。

(4.7)、(5.3)–(5.4) 同时给
\[
 C_L^*J_\theta C_H=
 \begin{pmatrix}
 j_0&0\\ j_2&0\\ 0&-j_0E^*D_xF
 \end{pmatrix}+O(\tau^{1/2}).                            \tag{6.4}
\]
完整 \(O(\tau^4)\) 余项乘最大尺度 \(\tau^{-2}\tau^{-1}\)
后仍为 \(O(\tau)\)；其余混合块最慢为 \(O(\tau^{1/2})\)。
所有估计都为维数无关算子范数。

三式右端的两个 Gram 具有统一正谱区间。因此，取逆平方根并组合相位后，原完整 \(\Phi\) 酉等价于极限相位加
\(O(\tau^{1/2})\)。极限相位的全部谱仍准确为
\[
 \{\Lambda_{\rm b}(\nu),\
     \Lambda_{\rm d}(\nu)^{[m-2]},0\}.                   \tag{6.5}
\]
其中
\[
 q=\frac v{\mu^2},\qquad
 \Delta=\frac{M_3}{\mu^3}-\left(\frac{M_2}{\mu^2}\right)^2,
\]
\[
 \Lambda_{\rm b}=(1-q)^2+
     \frac{[\Delta/q-(1+q^2)]^2}{\Delta},\qquad
 \Lambda_{\rm d}=\frac{(1-q)^2}{1+q}.
\]
[半高斯严格常数一及完整矩证书](2026-11-14-half-gaussian-bright-phase-sharp-one-bound-789f-next.md)
已自足证明每个有限 \(\nu\) 上两者严格小于 \(1\)。
由于 \(\nu\) 位于 (1.4) 给出的固定紧区间，有共同严格缺口
\[
       \gamma_*=1-\max_{|\nu|\le(3/\sqrt2)\Lambda}
                      \max\{\Lambda_{\rm b}(\nu),
                             \Lambda_{\rm d}(\nu)\}>0.
\]
选 \(\tau_0\) 使统一误差不超过 \(\gamma_*/2\)，再由 (1.4) 选
\(S_*\)，即得 (0.3)，可取 \(\gamma=\gamma_*/2\)。

## 7. 新增范围与剩余缺口

本稿第一次把高斯窗口的实际有限源收缩阈值改为“总曲率足够大”，不要求单个位的方差或任何组比例远离零。证明中两次共同合同可以很大，但所有真实均值、每个位的条件噪声、完整逆及非交换共同差都在合同后先得到一致预算。

若另有同一真实模型在 \(S_{\mathrm{tot}}\) 和
\(|D_{\mathrm{tot}}|\) 同时有界区域的统一有限预算，则它与本稿可直接拼合成整个
\(|D_{\mathrm{tot}}|\le\Lambda\sqrt{S_{\mathrm{tot}}}\)
区域的统一有限常数：小曲率时漂移自动有界，大曲率时由 (0.3) 支付。此拼合仍是对明确区域的定理，不覆盖
\(|D_{\mathrm{tot}}|/\sqrt{S_{\mathrm{tot}}}\to\infty\)
或权区间退化。
