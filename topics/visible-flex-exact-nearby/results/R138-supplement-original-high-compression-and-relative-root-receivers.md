# R138：保原 low96/high97 的高压缩与相对根迹接收器

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

实际两模 run `44745192261/1` 已证明原齐次根型有负方向。因此本篇不再要求全部根数据上的非负性。下面给出另一条完整充分门：只对原全部 high 压缩支付正性，把剩余负型压在原 low96，再由真实根迹的有限接收器估计相对于体能量吸收。原 low/high 分界、独立 mean、非齐次角缺陷与无限 high 尾全都保留。

本篇的新解析结论是根接收器的准确对偶式、只需一次同一 `L2` 逆的导数界、完整高压缩的有限逆乘子公式及最终二变量吸收门。尚未评估的高压缩常数和接收器费用不写成已过门。所有角积分用归一平均，记
\(E=\mathcal E/(2\pi)\)、\(B=\mathcal B/(2\pi)\)。所有旧 X/Y/GB 常数在型与范数同除 \(2\pi\) 后不变。

## 1. 同一真实根的准确对偶恒等式

沿用 [U 篇](R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md)的真实 moving 角、全圈周期 frame 和原齐次根域。记
\[
 P_L=P_{1\le j\le96},\quad P_H=P_{j\ge97},\quad
 S=P_LN+P_HN^{1/3},\quad f=Sz,
\]
\[
 w_*(\phi)=\omega_{\rm phys}(r_*,\Theta(r_*,\phi)),\qquad
 h=\mathsf H,\quad \rho=a/m,\quad
 Q_H=P_HN^{-2/3},\quad q_0=-I(v-m)/m,\quad
 \chi=u'/v,\quad V_0=Y+uX.
 \tag{R.1}
\]
这里 \(w_*\) 始终是同一 physical 旋转场按自己的真实 \(\Theta\) 拉回后的 moving 根函数；本节所有撇号都是对 \(\phi\) 求导，不再对 \(w_*\) 作第二次角 composition。\(Q_H\) 保留原全部 high，\(m<0\)、\(a>0\)，并保留实际根源 \(h\)。
U.4 的准确式是
\[
 w_*'-h=\rho\{fY+(t'+\mu/m)(X-uY)-tu'Y\},
 \qquad t=(Q_Hf+\mu q_0)/v.
 \tag{R.2}
\]
先与 \(X\) 作内积，再取完整周期平均，得到
\[
 \boxed{\quad
 \mu=-\frac m\rho\{\langle X'\cdot w_*\rangle
                       +\langle X\cdot h\rangle\}.
 \quad}
 \tag{R.3}
\]
这用的是 \(\langle t'\rangle=0\)；没有把 mean 置零，也没有改变 U.9 的原周期相容式。
再将 (R.2) 与 \(V_0=Y+uX\) 作内积，令
\(A=1-M_\chi Q_H\)，可得
\[
\begin{split}
 Af=\rho^{-1}\{&V_0\cdot w_*'
 -m\chi q_0\langle X'\cdot w_*\rangle\\
 &-V_0\cdot h-m\chi q_0\langle X\cdot h\rangle\}.
\end{split}
 \tag{R.4}
\]

令 \(W\) 为从原 scalar odd-fourfold \(z\) 到某个有限欧氏空间的任意固定接收器。对输出向量 \(c\)，定义
\[
 \psi_c=S^{-1}W^*c,\quad
 \eta_c=(A^*)^{-1}\psi_c,
 \quad A^*=1-Q_HM_\chi,
\]
\[
 d_c=\langle\eta_c\chi q_0\rangle,
 \qquad P_c=\eta_c V_0+m d_c X.
 \tag{R.5}
\]
只要显示的 \(A^*\) 逆已经支付，配对 (R.4) 并分部积分给准确有限接收器公式
\[
 \boxed{\quad
 c\cdot Wz=-\rho^{-1}
       \{\langle P_c'\cdot w_*\rangle
                      +\langle P_c\cdot h\rangle\}.
 \quad}
 \tag{R.6}
\]
\(P_c'\) 的环境向量平均严格为零，理由只是完整周期导数的积分为零。\(P_c\) 本身的平均仍在 (R.6) 的第二项保留。因此可以对第一项使用 mean-zero 根迹接收器，而不能对第二项删除零频。

(R.6) 不使用齐次根型非负性、不使用待求正区逆，也不要求 \(h=0\)。mean 分母 \(\mathcal D\) 没有在此被近似；(R.3) 是同一方向的另一个准确读出。根型的均值消元及下面的 \(g_m\) 仍使用已付实际 \(\mathcal D>17/20\)。

上述恒等式先对同域光滑方向证明。实际弱齐次核沿 [V 篇第 9 节](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md)已由同一个原 full-real-delta 高图的 base-order 解辨认；原 stable 输入为零时，[G.13](R133-supplement-global-positive-reference-and-current-collar.md) 的完整根矩阵给 \(N^{1/3}f_H\in\ell^2\)，因而 \(z_H=N^{-1/3}f_H\in L^2\)。V 的真实根缺陷迹及下文有界对偶使恒等式由同域稠密逼近延拓；没有从 WVC hybrid 借用这些实际图的资格。

## 2. 一个显式且非循环的接收器合同

记 \(n_H=388\)，并从同一真实根全圈支付
\[
 \chi_0\ge\|\chi\|_\infty,\qquad
 \chi_1\ge\|\chi'\|_\infty,\qquad
 \kappa=n_H^{-2/3}\chi_0<1.
 \tag{R.7}
\]
将同一个物理 cutoff `388` 的 Fourier 乘子 \(Q_H\) 自然延拓到完整 fourfold `L2`，同时包含 odd 和 even 两种 parity（零模乘子为零）。\(\chi\) 是 even-fourfold，故 \(A^*=1-Q_H\chi\) 保持这两个子空间。\(Q_H\) 自伴且 \(\|Q_H\|_{2\to2}=n_H^{-2/3}\)，同一个 \(\kappa\) 给两种 restriction 的 `L2` Neumann 逆，因此
\[
 \eta_0\le\frac{\Psi_0}{1-\kappa},\qquad
 \eta_1\le\frac{\Psi_1+n_H^{-2/3}\chi_1\eta_0}{1-\kappa},
 \tag{R.8}
\]
其中
\[
 \Psi_0=\|S^{-1}W^*\|_{\mathbb R^d\to L^2},\qquad
 \Psi_1=\|\partial_\phi S^{-1}W^*\|_{\mathbb R^d\to L^2}.
\]
证明第二式时，对 \((1-Q_H\chi)\eta=\psi\) 求导，得到
\((1-Q_H\chi)\eta'=\psi'+Q_H(\chi'\eta)\)。\(\eta\) 是 odd，而 \(\eta'\) 与右侧是 even；此处使用的是刚明确的 even restriction 的同一个 `L2` 逆，不能把 odd restriction 直接作用于 even 函数。故不用另加一个 `H1` 收缩条件。
对纯 low 接收器，准确有 \(\Psi_0=\|N_L^{-1}W^*\|\)、\(\Psi_1=\|W^*\|\)。不得无故将前者换成 \(\|W\|/4\)，以免抹掉 96 附近负方向的实际频率。

设同一根全圈
\[
 v_j\ge\|\partial_\phi^jV_0\|_\infty\ (j=0,1),\quad
 X_1\ge\|X'\|_\infty,\quad
 c_0\ge\|\chi q_0\|_{L^2},\quad m_0\ge|m|.
\]
则可直接取
\[
 P_0=(v_0+m_0c_0)\eta_0,\qquad
 P_1=v_0\eta_1+(v_1+m_0c_0X_1)\eta_0
 \tag{R.9}
\]
作为 \(c\mapsto P_c\) 与 \(c\mapsto P_c'\) 的完整算子范数上界。小写 \(v_0,v_1\) 是此处新定义的向量范数界，不是曲率坐标 \(v\) 的导数。

更紧的完整有限 Gram 接收器可以直接替换 (R.9)，但必须包住全部 \(Q_H\) 的逆尾；仅有限截断 \(A^*\) 的逆不够。保守式 (R.8)--(R.9) 不需物化任何无限 Fourier 数组。

## 3. 无外值费用的 mean-zero 真根读出

本节消费 [RT 的完整自由根迹与接收器合同](R138-supplement-capped-curvature-root-trace-and-finite-receivers.md)。

令 \(x=r-r_*\)、\(L=R-r_*\)、\(\delta=1/1840\)、\(d=L-\delta\)，并用已付
\[
 K\ge k_{\rm cap}(x)=\min(46x,1/40),\qquad
 14/5<L<29/10.
\]
取 \(d_-=14/5-1/1840<d\)。对非零环境频率 \(k\)，将势进一步降低成 \([0,\delta]\) 上零、\([\delta,L]\) 上 \(1/40\)。固定根值而让外值自由的最小能量是相应外 Neumann 辅助解的能量；它给准确容量
\[
 |z_k(0)|^2\le c_k\int_0^L
          (|z_k'|^2+k_{\rm cap}|k|^2|z_k|^2),
\]
\[
 c_k=\delta+\frac{\sqrt{40}}{|k|}
       \coth\!\left(\frac{|k|d}{\sqrt{40}}\right)
 \le\delta+\frac{\sqrt{40}}{|k|}
                     +\frac{40}{d_-k^2}.
 \tag{R.10}
\]
\(\coth t\le1+1/t\) 对 \(t>0\) 由 \(e^{2t}-1\ge2t\) 立即得到。外 Neumann 仅是变分极小器的辅助条件；未知实际方向没有被加此边界条件。零频不能用 (R.10)，但 (R.6) 的第一行系数 \(P_c'\) 本来就有严格零平均。

令 \(w(r,\phi)=\omega_{\rm phys}(r,\Theta(r,\phi))\)，\(v_*=w\circ\psi\)，所以 \(w(r_*,\phi)=w_*(\phi)\) 正是 (R.1)--(R.6) 的同一个函数；其中 \(\psi\) 是 V.13 的同一个 drift，\(\Gamma^{-1}\le\psi_\xi\le\Gamma\)。moving mean-zero 接收行 \(a\) 的准确拉回是 density
\(T_\psi a=(a\circ\psi)\psi_\xi\)，仍平均为零。它在 \(L^2\)、\(\dot H^{-1}\) 的范数均至多 \(\sqrt\Gamma\)：后者由
\(I T_\psi a=(Ia)\circ\psi-\langle(Ia)\circ\psi\rangle\) 和 composition 的 `L2` 换元证明。Hilbert 插值给 \(\dot H^{-1/2}\) 的同一界。

因此对 \(a=P_c'\)，(R.10) 与准确 Minkowski 能量界给
\[
 |\langle P_c'\cdot w_*\rangle|
 \le\Gamma\,\mathcal N_W
 \{(\sqrt{C_E}+\sqrt{C_H}h_E)\sqrt E
                         +\sqrt{C_H}h_B\sqrt B\},
 \tag{R.11}
\]
其中一个可直接用 (R.9) 的完整界为
\[
 \mathcal N_W^2
 =\delta P_1^2+\sqrt{40}\,P_0P_1
                         +(40/d_-)P_0^2.
 \tag{R.12}
\]
这里使用
\(\|P_c'\|_{\dot H^{-1}}\le P_0|c|\) 和
\(\|P_c'\|_{\dot H^{-1/2}}^2\le P_0P_1|c|^2\)。可以改用完整 Gram 的这三项加权和后再取算子范数，避免分别取最坏方向。

旧 Y 的完整根缺陷迹仍为
\[
 \|h\|_{H^{-1/3}_\phi}\le
 R_E\sqrt E+R_B\sqrt B,
 \qquad R_E=\sqrt{A_\Theta}r_E,
 \quad R_B=\sqrt{A_\Theta}r_B.
 \tag{R.13}
\]
本篇不以新 `H1/2` 体门替换这里的旧 `H2/3` 来源。\(h\) 的 mean 保留。由完整非齐次 Sobolev 插值
\[
 P_{1/3}=P_0^{2/3}(P_0^2+P_1^2)^{1/6},
\]
若 \(\rho_-^{-1}\ge1/|\rho|\)，(R.6) 最终给
\[
 \boxed{\quad \|Wz\|\le\alpha_E(W)\sqrt E+\alpha_B(W)\sqrt B,\quad}
 \tag{R.14}
\]
\[
\begin{split}
 \alpha_E(W)&=\rho_-^{-1}
  [\Gamma\mathcal N_W(\sqrt{C_E}+\sqrt{C_H}h_E)+P_{1/3}R_E],\\
 \alpha_B(W)&=\rho_-^{-1}
  [\Gamma\mathcal N_W\sqrt{C_H}h_B+P_{1/3}R_B].
\end{split}
 \tag{R.15}
\]
(R.11) 不含 \(A_\Theta\)，因为接收器与 \(w\) 都在同一 moving 角；唯一的 \(A_\Theta\) 在真实根源的密度拉回 (R.13)，不能漏掉或再重复付。

## 4. 只支付原全部 high 压缩的正性

令 \(K\) 为准确有界自伴算子
\[
 \langle Kz,z\rangle=\mathfrak b_*(Sz)/(2\pi),
 \qquad
 K=\begin{pmatrix}A_L&C^*\\ C&D_H\end{pmatrix}
 \quad\hbox{于 }P_L\oplus P_H.
 \tag{R.16}
\]
不再要求 \(K\ge0\)。新合同只要求证明
\[
 D_H\succeq\lambda_H I,\qquad\lambda_H>0.
 \tag{R.17}
\]
U 篇的正 principal 给 \(D_H=P_HM_aP_H+R_H\)。这里的 \(a\) 沿用 F.9a 的准确 scalar even-fourfold 投影；对真实位置 \(a=a_0>0\)。全部 actual mean rank 与两个非局部 primitive 都在 \(R_H\) 中。一个首选充分界是
\(\lambda_H=a_{\min}-\|R_H\|>0\)，其中 `high-only` 余项表从原 `j>=97` 开始，故 `R` 滤子范数是 \(388^{-2/3}\)，而非全空间低频上界 \(1\)。

若上述全范数界不分离，则令 \(P=P_{97\le j<J}\)、\(Q=P_{j\ge J}\)，仍不改变真实分界。原 high principal 的压缩逆是
\[
 (P_HM_aP_H)^{-1}
 =P_HM_{1/a}P_H
 -P_HM_{1/a}P_L(P_LM_{1/a}P_L)^{-1}P_LM_{1/a}P_H.
 \tag{R.18}
\]
这是正乘子完整二块逆的 Schur 恒等式。因此定义有限矩阵
\[
 B_0=P_LM_{1/a}P_L,\quad C_0=PM_{1/a}P_L,\quad E_0=PM_{1/a}P,
\]
\[
 \mathcal A_H=E_0-C_0B_0^{-1}C_0^*,\qquad
 R_F=PKP-PM_aP.
 \tag{R.19}
\]
特别，不能把 \(\mathcal A_H\) 写成单独的 \(PM_{1/a}P\)：那会错误忽略被保留的原 low96 对逆乘子的影响。

若同一固定 \(0<\tau\le1\) 的完整 directed 门给
\[
 (1-\tau)\mathcal A_H^{-1}+R_F\succeq0,
 \qquad \|R_HQ\|\le\varepsilon_H,
 \tag{R.20}
\]
则 F 篇同一有限秩吸收证明在 Hilbert 空间 \(P_HL^2\) 中给
\[
 \lambda_H=a_{\min}\tau-2\varepsilon_H>0.
 \tag{R.21}
\]
(R.18)--(R.20) 只需完整有限 `1/a` Gram、有限根型与已证明的一侧 infinite-tail 界。所有参数矩形顶点上必须实际支付 \(a>0\)；\(\mathcal A_H^{-1}\) 仍是 shorted affine 正乘子的变分下确界，故 F 篇的完整轴矩形凹性同样适用。任何数值有限矩阵都不能替代 \(\varepsilon_H\)。

## 5. 把所有剩余负型留给原 low96

固定 \(0<\theta<1\)。由 (R.17) 和完成平方，
\[
 \langle Kz,z\rangle
 \ge(1-\theta)\lambda_H\|z_H\|^2
   +\left\langle
    [A_L-(\theta\lambda_H)^{-1}C^*C]z_L,z_L\right\rangle.
 \tag{R.22}
\]
因此只需一个完整有限矩阵 \(W_L\) 满足
\[
 W_L^*W_L\succeq(\theta\lambda_H)^{-1}C^*C-A_L.
 \tag{R.23}
\]
\(W_L\) 有原 `96` 列，可以是非满秩或带权接收器。它可保留 96/97 邻接负方向的精确结构，避免用低频一律最坏的 scalar 下界。若使用完整轴矩形，选同一个固定 \(W_L\) 在全部顶点支付 (R.23) 即足够：\(C\) 与 \(A_L\) 对坐标仿射，而 \(C^*C\) 是矩阵凸的。这里 \(\lambda_H\) 取该完整矩形的统一下界；不能分别挑不相容的顶点接收器后免费移到实际点。

(R.23) 中 \(C=P_HKP_L\) 是全 high 输出。若计算至 \(j<J\)，则输出正交性给准确
\[
 C^*C=C_F^*C_F+C_T^*C_T.
 \tag{R.24}
\]
必须另给 \(C_T^*C_T\preceq T_L\) 的全尾正矩阵上界；有限 \(C_F^*C_F\) 本身不够。最简单是 \(T_L=\varepsilon_C^2I\)。更适合本接收器的可执行选择是先证明
\(\|C_TN_L^{-1}\|\le\varepsilon_C\)，再取
\(T_L=\varepsilon_C^2N_L^2\)，保留原低频权。所用尾式包含完整 principal 跨块、全部 compact 局部项、mean rank 和两个 primitive 项。

## 6. 完整非齐次根源与两个 low 接收器

用 [F.2--F.7](R138-supplement-root-source-elimination-and-concave-finite-gate.md) 的同一实际 \(G,g_m,\mathcal D\) 定义
\[
 L_h=G_1C_{V,0}+2d_DG_0g_0,\quad d_D=20/17,
\]
\[
 C_q=M_{G,1/3}C_{V,1/3}+d_DG_0g_0C_{V,0}.
 \tag{R.25}
\]
分别支付
\[
 \|I\mathcal RSP_L\|\le C_{\omega,L},\qquad
 \|I\mathcal RSP_H\|\le C_{\omega,H},
 \quad C_L=L_h C_{\omega,L},\quad C_H^\times=L_h C_{\omega,H}.
 \tag{R.26}
\]
这是完整根映射的两列范数，不是新的边界条件。它们可由已有无导数展开
\(\omega_0=y+Iv\) 取界：high 的滤子范数为
\(Q=388^{-1/3},R=388^{-2/3},T=388^{-4/3}\)；low 则 \(q=T=0\)、\(R\) 范数为 \(1\)。mean rank 始终保留。

将 (R.22)--(R.23) 代入准确 F.2，并只对 high/source 交叉完成平方，得到
\[
 \widetilde{\mathcal B}_L/(2\pi)
 \ge-\|W_Lz_L\|^2-C_L\|z_L\|\,\|h\|_{H^{-1/3}}
                        -Q_h\|h\|_{H^{-1/3}}^2,
\]
\[
 Q_h=C_q+\frac{(C_H^\times)^2}{4(1-\theta)\lambda_H}.
 \tag{R.27}
\]
无需断言 \(\widetilde{\mathcal B}_L\ge-C_*\|h\|^2\) 对所有根数据成立；实际负两模恰说明这种单独全根充分路线不能免费成立。

对接收器 \(W_LP_L\) 与 \(P_L\) 分别应用 (R.14)，记
\[
 \|W_Lz_L\|\le\alpha_E\sqrt E+\alpha_B\sqrt B,
 \quad \|z_L\|\le\beta_E\sqrt E+\beta_B\sqrt B.
\]
连同原完整 (R.13)，有
\[
 \widetilde{\mathcal B}_L/(2\pi)
 \ge-b_{EE}E-b_{EB}\sqrt{EB}-b_{BB}B,
 \tag{R.28}
\]
\[
\begin{split}
 b_{EE}&=\alpha_E^2+C_L\beta_E R_E+Q_hR_E^2,\\
 b_{EB}&=2\alpha_E\alpha_B
       +C_L(\beta_ER_B+\beta_BR_E)+2Q_hR_ER_B,\\
 b_{BB}&=\alpha_B^2+C_L\beta_BR_B+Q_hR_B^2.
\end{split}
 \tag{R.29}
\]
完整 mean 在 \(P_c\)、\(g_m\)、\(C_q\) 及 \(h\) 的非齐次范数中保留，未被两次消去或删去。

## 7. 与实际已成 GB 体门的最终接法

读取 GB run `44745355257/1` 的完整新 \(a_{EE},a_{EB},a_{BB}\)，以及旧 X/Y 的完整 \(C_E,C_H,\Gamma,A_\Theta,h_E,h_B,r_E,r_B\)。不要重新运行这些旧目标。
令
\[
 A_E=a_{EE}+b_{EE},\qquad A_B=a_{BB}+b_{BB},\qquad
 A_{EB}=a_{EB}+b_{EB}.
\]
则充分且完全明确的三个新门为
\[
 \boxed{\quad A_E<2,\qquad A_B<1,\qquad
 A_{EB}^2<4(2-A_E)(1-A_B).\quad}
 \tag{R.30}
\]
它们接同一真实残差能量恒等式，迫使原齐次核的 \(E=B=0\)。没有改变外端图、mean 或任何接口，也不把 WVC hybrid 当成 \(DF(Q^{\rm repair})\)。从 injectivity 到完整定量 inverse 的原 closed-range / 图接入仍按原合同支付。

一个新公共消费者的完整合同可以只发表：实际高下界 \(\lambda_H\)、(R.7) 的 margin、两个有限接收器的完整 scalar 范数、\(C_L,Q_h\)、(R.29) 三数和 (R.30) 三门。有限矩阵、Gram、角数组与原候选定义只作 CI 私有中间量，不发表可重建数组。原 96/97 两模的三个有符号矩阵项已由 run `44745192261/1` 完成；任何新有限矩阵必须直接嵌入该 actual 的三份完整保存球，并在新求积中跳过这些旧项。其余新 cross、逆乘子 Gram 和尾目标可消费同一私有定义，但不能重算这三个已成科学目标。所有依赖球先完整保存并读回，严格门只用读回后的方向正确端点。false 比较只说明这一充分预算尚未分离，不能写成原 BVP 奇异。
