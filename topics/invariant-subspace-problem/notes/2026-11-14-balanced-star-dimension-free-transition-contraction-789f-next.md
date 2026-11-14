# 平衡 star 临界窗口的维数无关完整相位收缩

日期：2026-11-14；工作标识：789f。

状态：完整证明；全部源、统一余项与标量严格缺口均已保留。

## 0. 结论

固定
\[
 0<x_-<x_+<\infty,\qquad \chi_->0,\qquad \Lambda<\infty.
\]
对每个整数 \(Q\)，允许组数 \(m=m_Q\) 变化，组大小
\[
             q_i\in\mathbb N,\quad \sum_{i=1}^{m}q_i=Q
\]
任意，特别允许全部 \(q_i=1\)。置 \(\omega_i=q_i/Q\)。假设
\[
 x_-\le x_i\le x_+,\quad
 \sum_i\omega_i x_i=1,\quad
 \chi=\sum_i\omega_i(x_i-1)^2\ge\chi_-,\quad |\lambda|\le\Lambda,
                                                               \tag{0.1}
\]
并取实际小组权平方
\[
                   z_i=(1-\lambda Q^{-1/2})x_i.          \tag{0.2}
\]
主组长度 \(Q\)、权平方 \(1\)，小组总长度 \(Q\)。使用该真实平衡 star reducing 模块的整个 \(m\) 维低 primitive 源、一维硬源及原相位
\[
 \Phi_Q=H_Q^{-1/2}J_Q^*L_Q^{-1}J_QH_Q^{-1/2},\qquad
 J_Q=H_QG_Q^{-1}L_Q-2G_Q-y_Qy_Q^*.                       \tag{0.3}
\]

存在只依赖 \(x_-,x_+,\chi_-,\Lambda\) 的 \(\gamma>0,Q_0<\infty\)，使得对所有上述参数、所有 \(Q\ge Q_0\)，
\[
                         \boxed{\Phi_Q\preceq(1-\gamma)I.}
                                                               \tag{0.4}
\]
\(Q_0,\gamma\) 不依赖 \(m\)、单个 \(q_i\) 或 \(\min_i\omega_i\)。

这是实际有限 \(Q\) 的完整源收缩，不只是逐点极限。它只处理 (0.1)–(0.2) 所指定的非退化临界窗口，尚未覆盖归一权趋零或无界、\(\chi\to0\)、\(|\lambda|\to\infty\) 等窗口之外参数，也不外推到这个 reducing 模块之外的全部物理源。

等价地，对任意给定的实际正权平方 \(z_i\)，可令
\[
 \zeta=Q^{-1}\sum_iq_i z_i,\quad
 x_i=z_i/\zeta,\quad \lambda=\sqrt Q(1-\zeta).
\]
这样 (0.2) 完全准确，没有更改主组权或偷偷作额外物理缩放。

## 1. 从真实全源形式开始

概率模型及每个完整矩阵沿用
[高斯过渡层完整稿](2026-11-14-balanced-star-gaussian-transition-full-phase-bound-789f-next.md)：
\[
 F_Q(t)=\prod_i(1-t+z_it)^{q_i},\quad
 \rho_Q=F_Q/\int_0^1F_Q,\quad
 K_i\mid T=t\sim\operatorname{Bin}(q_i,p_i(t)),
\]
\[
 p_i(t)=\frac{z_it}{1-t+z_it},\qquad X_i=K_i/q_i,
\]
且给定 \(T\) 后各组独立。写
\[
 G=\operatorname{Cov}X,\quad
 H=\mathbb E\frac{1-T}{T}XX^*,\quad
 L=\mathbb E\frac{T}{1-T}(1-X)(1-X)^*,
 \quad y=2\mathbb EX-\mathbf1.
\]
这里没有对每个二项变量使用中心极限定理；其二阶矩在 \(q_i=1\) 时仍然完全准确。

关键是先对全部源同时作同一个可逆合同
\[
                 W=\operatorname{diag}(\sqrt{\omega_i}).
\]
用 \(\mathscr H=WHW,\mathscr G=WGW,\mathscr L=WLW\) 及
\(\mathscr y=Wy\)。则
\[
 \mathscr J=WJW
     =\mathscr H\mathscr G^{-1}\mathscr L
                         -2\mathscr G-\mathscr y\mathscr y^*.
                                                               \tag{1.1}
\]
因此新的相位与 (0.3) 酉等价。即使 \(W\) 的条件数很大，也不需估计它；以下全部估计都在合同后的真实源内进行。

对任意标量函数 \(f,g\)，有
\[
 W\mathcal D[f]W=\operatorname{diag}(f(x_i)),\qquad
 W\mathcal O[f,g]W=v_fv_g^*,\quad
 v_f=(\sqrt{\omega_i}f(x_i))_i.
\]
所以
\[
 \|W\mathcal D[f]W\|\le\sup_{[x_-,x_+]}|f|,\qquad
 \|v_fv_g^*\|\le\sup|f|\sup|g|.                          \tag{1.2}
\]
所有常数都与维数无关；\(\sum_i\omega_i=1\) 已支付完整外积范数。

## 2. 半线矩展开的统一常数

写 \(\varepsilon=Q^{-1/2}\)。在 (0.1) 上
\[
 \chi\le \chi_+:=\max\{(x_--1)^2,(x_+-1)^2\},
\]
而每个固定次数 \(k_r=\sum_i\omega_i(x_i-1)^r\) 都有统一界。真实对数密度
\[
 Q\sum_i\omega_i\log(1+\varepsilon u(x_i-1-\lambda\varepsilon x_i))
\]
的有限 Taylor 系数就是完整稿 §2 的 \(W_1,V_2,\ldots\)。它们的次数和系数界只依赖本稿四个固定参数。

对充分小 \(\varepsilon\)，实际二阶导数在整个 \(t\in[0,1]\) 上满足
\[
 -\frac{d^2}{dt^2}
    \sum_i\omega_i\log(1-t+z_it)
   =\sum_i\omega_i\frac{(z_i-1)^2}{(1-t+z_it)^2}\ge c>0,
\]
其中 \(c\) 只依赖四个固定参数。因此，换元 \(t=\varepsilon u\) 后的指数有统一上界 \(C-c'u^2\)。Taylor 的余项先在 \(u\) 的增长截断区间上估计，外部用此统一高斯尾；由此得到任意所需有限阶的矩展开，余项常数无维数依赖。

极限分布为
\[
 f_{\lambda,\chi}(u)\propto e^{-\lambda u-\chi u^2/2},
 \quad u>0.
\]
其 \(\mu=\mathbb EU\)、\(v=\operatorname{Var}U\)、\(M_2,M_3\) 以及
\(\mu M_3-M_2^2\) 在
\[
          |\lambda|\le\Lambda,\quad \chi_-\le\chi\le\chi_+
\]
上连续且严格正。因此它们有统一正下界、有限上界。若参数集为空则定理真空成立。

此外归一权 \(\sum\omega_i x_i=1\) 和方差下界给
\[
 \sum_i\omega_i\log x_i\le-c_0<0
\]
一致成立。例如在固定区间上，\(\log x\le x-1-c_1(x-1)^2\)。所以完整端点参数
\(\beta=\prod z_i^{q_i}/\int F_Q\) 指数小，且所有被其乘上的多项式费用统一可控。

## 3. 每个位的噪声及完整逆的统一估计

条件协方差给完全准确的式子
\[
 \mathscr G=
 \varepsilon^2\operatorname{diag}
                   \{\mathbb E[p_i(T)(1-p_i(T))]\}
       +\operatorname{Cov}(Wp(T)).                       \tag{3.1}
\]
由统一半线矩展开，
\[
 \mathbb E[p_i(T)(1-p_i(T))]
       =\varepsilon x_i\mu+O(\varepsilon^2)
\]
逐位一致成立。因此
\[
                   \mathscr G\succeq c_2\varepsilon^3I. \tag{3.2}
\]
这一步明确保留所有 \(q_i=1\) 的真实噪声，并没有用一个只对宏观组成立的近似。

设
\[
 u_0=(\sqrt{\omega_i})_i,\qquad
 u_1=(\sqrt{\omega_i}x_i)_i,\qquad D=\operatorname{diag}(x_i).
\]
则
\[
 \|u_0\|=1,\quad u_0^*u_1=1,\quad
 \|u_1\|^2=1+\chi.                                      \tag{3.3}
\]
合同后的完整协方差展开为
\[
 \mathscr G=\varepsilon^2v\,u_1u_1^*
      +\varepsilon^3\mathscr G_3
      +\varepsilon^4\mathscr G_4
      +\varepsilon^5\mathscr G_5+O(\varepsilon^6)
\]
且每个系数和余项均以维数无关算子范数控制。完整稿的四条对角/外积乘法规则经 (1.2) 仍逐项准确。

具体地，
\[
 \mathscr R_0=\mu^{-1}(D^{-1}-u_0u_0^*),\quad
 \mathscr w_i=\sqrt{\omega_i}
       \left[1+\frac{M_3-\mu M_2}{\mu}(x_i-1-\chi)\right]
\]
都具有统一有界范数，并满足
\[
 \mathscr R_0u_1=0,\quad u_1^*\mathscr w=1,\quad
 \mathscr R_0\mathscr G_3=I-\mathscr w u_1^*.
\]
完整稿 §3 的准确基逆
\[
 (\varepsilon^2v\,u_1u_1^*+\varepsilon^3\mathscr G_3)^{-1}
 =\varepsilon^{-3}\mathscr R_0+
   \frac{\varepsilon^{-2}}
        {v+\varepsilon\mathscr w^*\mathscr G_3\mathscr w}
                       \mathscr w\mathscr w^*
\]
的分母一致远离零。对余下 \(\varepsilon^4\mathscr G_4+\cdots\) 作 resolvent 展开，得到
\[
 \mathscr G^{-1}=
       \varepsilon^{-3}\mathscr R_0+
       \varepsilon^{-2}\mathscr T_1+
       \varepsilon^{-1}\mathscr T_2+O(1),                \tag{3.4}
\]
其中全部系数有统一范数，\(O(1)\) 与 \(m,\min q_i\) 无关。这也可直接由 (3.2) 和有限级数的矩阵余项恒等式验证。反演始终在完整原源上完成。

## 4. 三尺度压缩仍具有维数无关余项

在 (3.3) 的两个特殊方向上，Gram 行列式是 \(\chi\ge\chi_-\)。可统一取
\[
 h_0=u_1/(1+\chi),\qquad l_0=u_0,\qquad
 l_1=(u_1-u_0)/\chi.
\]
它们满足
\[
 u_1^*h_0=1,\quad u_0^*l_0=1,\quad
 u_0^*l_1=0,\quad u_1^*l_1=1,
\]
且范数一致有界。取 \(F\) 为 \(u_1^\perp\) 的任意正交等距基，
\(E\) 为 \(\{u_0,u_1\}^\perp\) 的任意正交等距基，令
\[
 B_H=[\,\varepsilon^{-1/2}h_0,\ \varepsilon^{-1}F\,],\quad
 B_L=[\,\varepsilon^{-1/2}l_0,\
       \varepsilon^{-3/2}l_1,\ \varepsilon^{-2}E\,].
\]
完整稿的三尺度极限，现在在统一算子范数下成为
\[
 \widetilde H=B_H^*\mathscr HB_H=H_\infty+O(\varepsilon^{1/2}),
\]
\[
 \widetilde L=B_L^*\mathscr LB_L=L_\infty+O(\varepsilon^{1/2}),
 \qquad
 \widetilde J=B_L^*\mathscr JB_H=J_\infty+O(\varepsilon^{1/2}), \tag{4.1}
\]
其中
\[
 H_\infty=\operatorname{diag}(\mu,F^*DF),
\]
\[
 L_\infty=\operatorname{diag}
       \left(\begin{pmatrix}\mu&-M_2\\-M_2&M_3\end{pmatrix},
                            M_2E^*DE\right),
\]
\[
 J_\infty=
 \begin{pmatrix}
 j_0&0\\ j_2&0\\ 0&-j_0E^*DF
 \end{pmatrix},\quad
 j_0=(2\mu^2-M_2)/\mu,\quad
 j_2=(\mu^2-v)/(\chi v)-2\mu^2.                          \tag{4.2}
\]
\(H_\infty,L_\infty\) 的最大、最小特征值有统一正界。

说明 (4.1) 的最坏余项来源，可避免因增加维数而漏掉交叉：

| 完整块 | 首个未消余项及缩放后阶数 |
|---|---|
| \(H\) 的亮/补空间交叉 | 原阶 \(\varepsilon^2\)，乘 \(\varepsilon^{-3/2}\)，得 \(O(\varepsilon^{1/2})\) |
| \(L\) 的亮/最深层交叉 | 原阶 \(\varepsilon^3\)，乘 \(\varepsilon^{-5/2}\)，得 \(O(\varepsilon^{1/2})\) |
| \(L\) 的第二层/最深层交叉 | 原阶 \(\varepsilon^4\)，乘 \(\varepsilon^{-7/2}\)，得 \(O(\varepsilon^{1/2})\) |
| \(J\) 的第一输出/源补空间 | \(J_1\) 被源正交性消掉，剩余阶 \(\varepsilon^2\)，得 \(O(\varepsilon^{1/2})\) |
| \(J\) 的第二输出/源补空间 | \(J_1,J_2\) 被准确像/核关系消掉，剩余阶 \(\varepsilon^3\)，得 \(O(\varepsilon^{1/2})\) |
| \(J\) 的最深输出/亮源 | 首个可能项为 \(\varepsilon^3\)，得 \(O(\varepsilon^{1/2})\) |

最深 \(J\) 交叉使用的是完整稿的准确恒等式
\[
 E^*J_3F=-j_0E^*DF;
\]
完整 \(O(\varepsilon^4)\) 余项经最大源尺度乘积
\(\varepsilon^{-2}\varepsilon^{-1}\) 后为 \(O(\varepsilon)\)。
上述表只有固定数目的块，而每个矩阵余项已由 (1.2) 控制为算子范数，所以不随 \(m\) 累积。没有将逐 entry 的误差上界误用为算子界。

特别，对 \(J\) 的推导仍先保
\[
 A=D_a+aR^*/h=O(\varepsilon^2),\qquad
 B=D_b-Sb^*=O(\varepsilon^2)
\]
和完整 (3.4)。其逆余项 \(O(1)\) 只贡献 \(AG^{-1}B\) 的
\(O(\varepsilon^4)\)，未把三个大的非交换项分别估计。

## 5. 从统一极限谱得到实际有限模型的严格收缩

设
\[
 T_Q=\widetilde L^{-1/2}\widetilde J\widetilde H^{-1/2},
 \qquad
 T_\infty=L_\infty^{-1/2}J_\infty H_\infty^{-1/2}.
\]
在统一正谱区间内，逆平方根的算子范数连续性具有统一 Lipschitz 常数。例如可对正算子的 resolvent 积分公式直接估计。因此 (4.1) 给
\[
 \|T_Q-T_\infty\|\le C\varepsilon^{1/2},\qquad
 \|T_Q^*T_Q-T_\infty^*T_\infty\|\le C'\varepsilon^{1/2}.   \tag{5.1}
\]
常数只依赖 \(x_-,x_+,\chi_-,\Lambda\)。\(T_Q^*T_Q\) 与真实 (0.3) 酉等价。

由完整过渡层计算，\(T_\infty^*T_\infty\) 的谱恰为
\[
 \{\Lambda_{\rm b}(\lambda/\sqrt\chi),
       \Lambda_{\rm d}(\lambda/\sqrt\chi)^{[m-2]},0\}.
\]
标量严格收缩引理给所有有限实参数
\[
              \Lambda_{\rm b}<1,\qquad \Lambda_{\rm d}<1.
\]
此处使用[半高斯严格相位收缩及完整矩证书](2026-11-14-half-gaussian-bright-phase-sharp-one-bound-789f-next.md)的自足定理：它通过真实七阶矩的 shifted Hankel 正定性及两条完整正系数恒等式证明两个标量在每个有限参数处严格小于 \(1\)。原过渡稿 §7 的 \(4/3\) 界不承担此严格缺口。
这些标量连续，且
\(\lambda/\sqrt\chi\) 属固定紧区间。因此
\[
 \gamma_*=
 1-\max_{\substack{|\lambda|\le\Lambda\\
                  \chi_-\le\chi\le\chi_+}}
       \max\{\Lambda_{\rm b},\Lambda_{\rm d}\}>0.         \tag{5.2}
\]
取 \(Q_0\) 使 \(C'Q^{-1/4}\le\gamma_*/2\)，便有
\[
 \Phi_Q\preceq(1-\gamma_*/2)I\qquad(Q\ge Q_0),
\]
证明 (0.4)，其中 \(\gamma=\gamma_*/2\)。

这里紧性只作用于已经证明具有严格共同缺口的两个连续标量参数；没有将逐方向有限维正性或方向依赖半径拼成无根据的共同邻域。

## 6. 实际新增范围

本稿去掉了原过渡层初稿的一切“组数固定”和“组比例有正下界”限制。其核心是同源 \(W\) 合同与完整二项噪声，而不是另选一个有限分组族。特别小组全为独立单个位、组数随 \(Q\) 增长的情况，仍有同一个 \(Q_0,\gamma\)。

剩余的全参数缺口是 (0.1) 所排除的退化及窗口外区域。该窗口的相位严格收缩本身尚不足以支付所有正权、所有源出生和原无限 graph 的预算。
