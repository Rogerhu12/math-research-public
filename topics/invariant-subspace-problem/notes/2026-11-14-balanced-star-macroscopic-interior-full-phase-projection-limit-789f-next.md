# 任意多个宏观小组的平衡 star：内峰极限的完整相位投影

日期：2026-11-14；工作标识：789f。

## 0. 已证明的范围

固定小组数 \(m\geq2\)、正比例 \(\omega_i>0\)、\(\sum_i\omega_i=1\)，以及固定正权平方 \(z_i>0\)。取整数 \(Q\to\infty\) 使 \(q_i=Q\omega_i\) 为整数；主组长度为 \(Q\)，小组长度为 \(q_1,\ldots,q_m\)，主组权归一为 \(1\)。以下处理既有平衡 star 稿中的整个 \(m\) 维低 primitive 源，硬源为一维。它是相应群对称 reducing 模块的完整源，不把它冒称为未作分组的全部物理层。

定义
\[
 L_i(t)=1-t+z_it,\qquad
 \ell(t)=\sum_i\omega_i\log L_i(t).
\]
假设 \(\ell\) 的最大值在唯一内点 \(t_0\in(0,1)\) 取得，且
\[
 \chi=-\ell''(t_0)>0.                                      \tag{0.1}
\]
等价的端点条件是
\[
 \sum_i\omega_i z_i>1,\qquad
 \sum_i\omega_i z_i^{-1}>1;
\]
这时严格凹性给唯一内峰。令 \(H_Q,G_Q,L_Q\) 为真实完整源概率 Gram，令
\[
 J_Q=H_QG_Q^{-1}L_Q-2G_Q-y_Qy_Q^*,\qquad
 y_Q=2m_Q-\mathbf1,
\]
\[
 \Phi_Q=H_Q^{-1/2}J_Q^*L_Q^{-1}J_QH_Q^{-1/2}.               \tag{0.2}
\]

**定理。** 在上述整个 \(m\) 维源上，
\[
 \operatorname{spec}(\Phi_Q)
 \longrightarrow \{\underbrace{1,\ldots,1}_{m-1},0\}.        \tag{0.3}
\]
更准确地，下面给出保持两端真实度量的坐标，使相位的归一化交叉算子收敛到一个秩 \(m-1\) 的部分等距算子。故任给 \(\varepsilon>0\)，对该固定 profile 的充分大 \(Q\)，有
\[
                         \Phi_Q\leq(1+\varepsilon)I.        \tag{0.4}
\]
在满足 (0.1) 且远离退化的任意紧 profile 集上，阈值可共同选取，且
\[
                 \|\Phi_Q\|\leq1+C Q^{-1/2}.               \tag{0.5}
\]

这里没有断言任意有限 \(Q\) 的最优常数 \(1\)，也没有给全部 profile、全部组数或全部原始 Boolean 行的统一常数。极限出现 \(m-1\) 个等号方向，因此仅有此极限不能决定有限 \(Q\) 缺陷的正负号。

## 1. 保持完整源的真实概率模型

令
\[
 F_Q(t)=\prod_iL_i(t)^{q_i}=e^{Q\ell(t)},\qquad
 Z_{F,Q}=\int_0^1F_Q(t)\,dt.
\]
\(T\) 的密度为 \(F_Q/Z_{F,Q}\)。给定 \(T=t\)，各
\[
 K_i\sim\operatorname{Bin}(q_i,p_i(t)),\qquad
 p_i(t)=\frac{z_it}{L_i(t)}
\]
独立，置 \(X_i=K_i/q_i\)。使用
\[
 m_Q=\mathbb EX,\quad n_Q=\mathbf1-m_Q,\quad
 G_Q=\operatorname{Cov}(X),
\]
\[
 H_Q=\mathbb E\frac{1-T}{T}XX^*,\qquad
 L_Q=\mathbb E\frac{T}{1-T}(\mathbf1-X)(\mathbf1-X)^*.        \tag{1.1}
\]
端点处的整列乘积按条件二项式定义，故没有人为添加无限项。

这些正是已识别的平衡 star 全源形式。实际物理 \(h,g,\ell\) 是 (1.1) 的同一个正标量倍，与它们同时出现的硬源平方也是该标量乘 \(y_Qy_Q^*\)；因此 \(J_Q\) 也按同一标量缩放，(0.2) 的相位及矩阵不等式不受它影响。全文没有将完整逆换成先压缩后的错误逆。

以下令 \(Z=\operatorname{diag}(z_i)\)，
\[
 a_Q=Zn_Q,\quad b_Q=Z^{-1}m_Q,\quad
 D_{a,Q}=\operatorname{diag}(a_{Q,i}/q_i),\quad
 D_{b,Q}=\operatorname{diag}(b_{Q,i}/q_i),\quad
 D_{0,Q}=\operatorname{diag}(1/q_i).
\]
真实条件二项式身份给
\[
 H_Q=D_{a,Q}-ZG_Q+a_Qm_Q^*,\qquad
 L_Q=D_{b,Q}-G_QZ^{-1}+n_Qb_Q^*,                            \tag{1.2}
\]
\[
                 [Z,G_Q]=a_Qm_Q^*-m_Qa_Q^*.                \tag{1.3}
\]
这些式对组内噪声完整保留 \(1/q_i\) 因子。

## 2. 精确端点关系；不得单独估计大均值项

定义
\[
 \alpha_Q=Z_{F,Q}^{-1},\qquad
 \beta_Q=\frac{\prod_i z_i^{q_i}}{Z_{F,Q}},\qquad
 u_+=(Z-I)q,\quad u_-=(Z^{-1}-I)q,
\]
其中 \(q=(q_i)\)。积分分部给
\[
 n_Q^*u_+=1-\alpha_Q,\qquad
 m_Q^*u_-=1-\beta_Q.                                      \tag{2.1}
\]
例如第一式是对 \((1-t)F_Q(t)\) 的边界计算。再对各 \(\log z_i\) 求导，使用
\(\partial_{\log z_i}m_{Q,j}=q_i(G_Q)_{ji}\)，得到
\[
 G_Qu_+=a_Q-\alpha_Qm_Q,\qquad
 G_Qu_-=b_Q-\beta_Qn_Q,                                    \tag{2.2}
\]
\[
                       u_+^*G_Qu_-=\alpha_Q\beta_Q-1.       \tag{2.3}
\]

固定任意 \(c>0\)，定义
\[
 R_Q=c\,m_Q-a_Q,\qquad S_Q=Z^{-1}R_Q=c\,b_Q-n_Q,\qquad
 \eta_Q=m_Q^*G_Q^{-1}n_Q-1.
\]
(2.1)–(2.3) 精确给出
\[
 R_Q^*G_Q^{-1}S_Q
 =c^2+1-c(\alpha_Q+\beta_Q)
       -(c-\alpha_Q)(1-c\beta_Q)\eta_Q.                     \tag{2.4}
\]
证明可直接代入
\[
 R_Q=(c-\alpha_Q)m_Q-G_Qu_+,\qquad
 S_Q=(c\beta_Q-1)n_Q+cG_Qu_-.
\]
这里 \(R_Q^*G_Q^{-1}Z^{-1}R_Q\) 是实际混合能量；没有声称它对任意 \(c\) 非负。

在本稿内峰条件下，
\[
 \ell(t_0)>\max\{\ell(0),\ell(1)\}.
\]
因此 \(\alpha_Q,\beta_Q\) 指数趋零。下面的完整因式分解会把它们仅作为指数小余项保留；没有分别估计 \(\eta_Qa_Qb_Q^*\) 和大的均值平方。

## 3. 一个消去未知高阶逆项的共同因式分解

由 (1.2)–(1.3) 直接展开，有完全准确的式子
\[
 \begin{split}
 J_Q={}&D_{a,Q}G_Q^{-1}D_{b,Q}-D_{0,Q}-G_Q
       -m_Qm_Q^*-n_Qn_Q^*+n_Qm_Q^*\\
 &+D_{a,Q}G_Q^{-1}n_Qb_Q^*
       +a_Qm_Q^*G_Q^{-1}D_{b,Q}
       +\eta_Qa_Qb_Q^*.                                   \tag{3.1}
 \end{split}
\]
非交换乘法次序在此固定。

只要 \(G_Q^{-1}=O(Q)\) 且 \(R_Q=O(Q^{-1})\)，端点式 (2.2)–(2.4) 将 (3.1) 化为
\[
 \begin{split}
 J_Q={}&n_Qm_Q^*-G_Q-D_{0,Q}
          +n_QS_Q^*-\frac1cR_Qm_Q^*\\
 &+\left(D_{a,Q}+\frac1c a_QR_Q^*\right)G_Q^{-1}
       \left(D_{b,Q}-S_Qb_Q^*\right)
       +O(e^{-\delta Q}) .                                \tag{3.2}
 \end{split}
\]
其中某个 \(\delta>0\) 依赖固定内峰 profile。任意由 \(Q\) 引入的多项式因子可吸收到较小的 \(\delta\) 中。

为核对 (3.2)，先由端点式写
\[
 G_Q^{-1}n_Q=c\,u_--G_Q^{-1}S_Q+O(e^{-\delta Q}),
\]
\[
 m_Q^*G_Q^{-1}=\frac1c(u_+^*+R_Q^*G_Q^{-1})
                                      +O(e^{-\delta Q}),
\]
\[
 \eta_Q=c+c^{-1}-c^{-1}R_Q^*G_Q^{-1}S_Q
                                      +O(e^{-\delta Q}).
\]
四个含完整逆的项正好并成 (3.2) 的一个乘积。剩余项使用
\[
 D_{a,Q}u_-=n_Q-a_Q,\qquad u_+^*D_{b,Q}=(m_Q-b_Q)^*
\]
及 \(c b_Q=n_Q+S_Q,\ a_Q/c=m_Q-R_Q/c\)，逐项消掉两个大的均值平方。这是同一个完整源上的消元，不是把两个大项各自做粗范数估计。

## 4. 内峰展开与完整源的首项

以下所有未标下标的量在 \(t_0\) 处取值。写
\[
 t=t_0,\quad a=t(1-t),\quad c=(1-t)/t,
\]
\[
 p_i=\frac{z_it}{L_i(t)},\qquad n_i=1-p_i,\qquad
 \lambda_i=\frac{z_i-1}{L_i(t)},\qquad
 \chi=\sum_i\omega_i\lambda_i^2,\qquad
 \tau=\frac{\sum_i\omega_i\lambda_i^3}{\chi}.                 \tag{4.1}
\]
峰条件给
\[
 \sum_i\omega_i\lambda_i=0,\quad
 p_i=t+a\lambda_i,\quad
 \sum_i\omega_i p_i=t.                                    \tag{4.2}
\]

标准内峰 Taylor–Gaussian 展开在这里直接给
\[
 m_Q=p+Q^{-1}m^{(1)}+O(Q^{-2}),                             \tag{4.3}
\]
\[
 m_i^{(1)}
   =\frac{p_i''(t)}{2\chi}
      +\frac{p_i'(t)\ell'''(t)}{2\chi^2}
   =\frac{p_i'(t)}{\chi}(\tau-\lambda_i),                   \tag{4.4}
\]
因为 \(p_i''=-2\lambda_i p_i'\)、\(\ell'''=2\sum\omega_i\lambda_i^3\)。

为明确余项依据，将 \(t-t_0=x/\sqrt Q\)，在固定小邻域展开 \(Q\ell(t)\) 及被积函数；奇 Gaussian 矩为零，二次矩为 \(\chi^{-1}\)，三阶指数项与一次被积函数项给 (4.4) 的第二项。补集积分因严格峰隙指数小。此处所有函数解析，继续展开两阶即得所写 \(O(Q^{-2})\)。在远离退化的紧 profile 集上，同一邻域、峰隙及有限阶导数界均可共同选取。

条件二项式噪声完整给
\[
 G_Q=Q^{-1}G_0+O(Q^{-2}),\qquad
 G_0=\operatorname{diag}(p_in_i/\omega_i)
                       +\frac{p'(t)p'(t)^*}{\chi}>0.        \tag{4.5}
\]
由 \(p_i'=p_in_i/a\) 与 (4.2)，Sherman 公式恰化为
\[
 \boxed{
 G_0^{-1}=\operatorname{diag}\!\left(\frac{\omega_i}{p_in_i}\right)
                     -\frac{\omega\omega^*}{a}.}
                                                                  \tag{4.6}
\]
特别
\[
                            p^*G_0^{-1}n=0.                \tag{4.7}
\]
(4.5) 已证明第 3 节需要的 \(G_Q^{-1}=O(Q)\)。又
\(Zn=cp\)，故 \(R_Q=O(Q^{-1})\)，此前所有指数余项均合法。

定义
\[
 v_i=\frac{\tau-\lambda_i}{a\chi}.
\]
则 (4.3)–(4.4) 还给
\[
 R_Q=Q^{-1}R_1+O(Q^{-2}),\quad
 S_Q=Q^{-1}S_1+O(Q^{-2}),
\]
\[
                    R_1/c=p\circ v,\qquad S_1=n\circ v.    \tag{4.8}
\]
\(\circ\) 表示逐坐标乘积。

由 (2.4)，完整均值逆费用因而满足
\[
                       \eta_Q\longrightarrow c+c^{-1}.    \tag{4.9}
\]
将 (3.2) 用在首项，得到
\[
                              J_Q=n p^*+O(Q^{-1}).          \tag{4.10}
\]
其方向是 \(L\) 源在左、\(H\) 源在右；不能写成 \(p n^*\)。

## 5. 全部退化对比方向的 \(Q^{-1}\) 项

取固定等距列矩阵 \(E_p,E_n\)，像分别为欧氏超平面
\(p^\perp,n^\perp\)。令
\[
 D_p=\operatorname{diag}(p_i/\omega_i),\quad
 D_n=\operatorname{diag}(n_i/\omega_i),\quad
 D_\omega=\operatorname{diag}(1/\omega_i).
\]
(3.2) 在左压 \(E_n^*\)、右乘 \(E_p\) 后，所有单独线性均值余项至少为 \(O(Q^{-2})\)，故
\[
 Q E_n^*J_QE_p=E_n^*\mathcal T E_p+O(Q^{-1}),                \tag{5.1}
\]
其中
\[
 \mathcal T=
 [D_p+p(p\circ v)^*]G_0^{-1}
 [D_n-(n\circ v)n^*]-D_\omega-G_0.                         \tag{5.2}
\]
因此这一个完整退化块不需要未计算的 \(m^{(2)}\)、\(G_1\) 或更高完整逆项。

由 (4.6)，
\[
 D_pG_0^{-1}D_n=D_\omega-\frac{pn^*}{a}.
\]
记 \(c_p=\sum_i\omega_i p_iv_i,\ c_n=\sum_i\omega_i n_iv_i\)。从 (4.2) 得
\[
 c_p=t\frac{\tau}{a\chi}-1,\qquad
 c_n=(1-t)\frac{\tau}{a\chi}+1,\qquad
 \operatorname{Var}_\omega(v)=\frac1{a^2\chi}.
\]
逐项展开 (5.2) 因而准确给
\[
 \mathcal T=-G_0+pv^*-vn^*-\frac{pn^*}{a^2\chi}.            \tag{5.3}
\]
另一方面，\(v\) 本身属于 \(\operatorname{span}\{p,n\}\)：
\[
 v=\theta_p p+\theta_n n,\qquad
 \theta_p=\frac{a\tau-(1-t)}{a^2\chi},\quad
 \theta_n=\frac{a\tau+t}{a^2\chi},\quad
 \theta_n-\theta_p=\frac1{a^2\chi}.
\]
于是
\[
 \mathcal T=-G_0+\theta_p pp^*-\theta_n nn^*.
\]
两端超平面恰好消掉后两个真实平方，最终得到
\[
 \boxed{
       Q E_n^*J_QE_p\longrightarrow-\,E_n^*G_0E_p.}          \tag{5.4}
\]
这是全部 \(m-1\) 个退化源方向的联合块，不是选择一个向量的能量极限。

## 6. 真度量缩放、完整极限及奇异值

由 (1.1)，
\[
 H_Q=c\,pp^*+O(Q^{-1}),\qquad
 L_Q=c^{-1}nn^*+O(Q^{-1}),
\]
且对比方向保留真实条件噪声后为
\[
 Q E_p^*H_QE_p\to c E_p^*G_0E_p,\qquad
 Q E_n^*L_QE_n\to c^{-1}E_n^*G_0E_n.                        \tag{6.1}
\]
选 \(h_0,l_0\) 使 \(p^*h_0=n^*l_0=1\)，并作两个合法的源坐标
\[
 B_H(Q)=[h_0,\sqrt Q E_p],\qquad
 B_L(Q)=[l_0,\sqrt Q E_n].
\]
它们分别处理 \(H\) 输入与 \(L\) 输出，不交换原目标的端点度量。由 (4.10)、(5.4)、(6.1)，有完整联合极限
\[
 B_H^*H_QB_H\to
 \begin{pmatrix}c&0\\0&cE_p^*G_0E_p\end{pmatrix},
\]
\[
 B_L^*L_QB_L\to
 \begin{pmatrix}c^{-1}&0\\0&c^{-1}E_n^*G_0E_n\end{pmatrix},
\]
\[
 B_L^*J_QB_H\to
 \begin{pmatrix}1&0\\0&-E_n^*G_0E_p\end{pmatrix}.             \tag{6.2}
\]
上右、下左余项为 \(O(Q^{-1/2})\)；其它所写收敛也至少具有此统一阶。

对比块归一化后是同一 \(G_0\) 内积中两个超平面之间的交叉 Gram：
\[
 -\,(E_n^*G_0E_n)^{-1/2}E_n^*G_0E_p
                      (E_p^*G_0E_p)^{-1/2}.                \tag{6.3}
\]
\(p^\perp\) 的 \(G_0\)-法向为 \(G_0^{-1}p\)，\(n^\perp\) 的为 \(G_0^{-1}n\)；(4.7) 说明两法向正交。故两个超平面的共同部分维数为 \(m-2\)，其余一个主角为 \(\pi/2\)。因此 (6.3) 的奇异值恰为
\[
                       1\ (m-2\text{ 次}),\quad0.
\]
再加 (6.2) 的一维明亮通道奇异值 \(1\)，即证明 (0.3)。当 \(m=2\) 时，两个对比超平面均为一维且相互 \(G_0\)-正交，所以对比奇异值就是 \(0\)，完整相位极限为 \(\{1,0\}\)。当 \(m=1\) 时，非恒定的 \(\ell(t)=\log(1-t+z_1t)\) 无内峰，而 \(z_1=1\) 时 \(\chi=0\)；故该情形不满足本定理假设，应使用既有的两权/单小组完整定理，不能代入本稿的 \(1/\chi\) 公式。

(6.2) 的极限两端 Gram 都严格正定，所以归一化连续；上述误差给 (0.5)，从而给 (0.4)。整个过程保留全部 \(m\) 维源及其两端度量。

## 7. 量词、可用范围及仍未支付之处

- 本定理排除了固定组数、固定正比例、固定严格内峰权型在 \(Q\to\infty\) 时发生相位范数发散的可能；整个源的极限确为投影型，而不是仅一条均值线有界。
- 紧 profile 集须保持 \(\omega_i\) 正下界、权平方的正上下界、内峰远离端点及 \(\chi\) 的正下界。不能把依赖这些参数的阈值换成任意 profile 的共同阈值。
- 可让 \(q_i/Q\) 及正权随 \(Q\) 在这样的紧集内变化：以每个当前 profile 的内峰和基作同一展开，误差仍一致；收敛 profile 得到同一极限结论。这也移除了固定比例必须有共同整数倍的表述限制。
- 未涵盖峰退化、向端点移动、组比例趋零、权比无界或组数增长的联合尺度。它们仍可能承载一般统一常数问题的困难。
- \(m-1\) 个极限相位等号方向意味着有限 \(Q\) 的下一阶缺陷必须继续共同分析；本稿没有由连续性断言 \(\Phi_Q\le I\)，也没有据此关闭 ISP。

