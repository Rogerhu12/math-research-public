# R133 补篇：完整物理边界的准确转置、平均伴随与真正 Schur 配对

2026-11-14。本文完成原物理边界与 moving 伴随之间的准确接线，
以及全频 nonlinear regular 余项的实际有理预算。10 个严格有理门已在
可用 V8 中执行并全部通过。全径向 response、adjoint 和补逆尚未运行；
本文不据边界小量宣称真正参数标量非零。

对象始终是最终 full-\(R\) 中心
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\)，
\(R=25/8\)，原完整 \(|\eta|\le10^{-9}\)。
固定准确 \(\alpha,\nu\)，保留真正独立 \(f_B\) 背景的原允许解析类。
本篇的参数 response 取方向 \(\delta f_B=0\)；这不把背景 \(f_B\)
或远端 nonlinear label 方程设零。

## 1. 原物理矩的完整转置

取归一化圆周平均和 \(L^2\) 范数，周期为 \(\pi/2\)。
记 \(I=\partial_\phi^{-1}P_{\ne0}\)，\(I^*=-I\)，以及
\[
 Q=(u,v),\quad m=\langle v\rangle,\quad
 \theta=\phi+\psi,\quad\psi=I(v-m)/m,\quad
 j=\theta_\phi=v/m>0 .
 \tag{P.1}
\]
原物理曲率满足 \(B\circ\theta=u/v,\ C\circ\theta=1/v\)。
对固定真实物理权 \(b(\theta),c(\theta)\)，准确有
\[
 {\cal M}_{b,c}(Q)=\langle b B+c C\rangle_\theta
   =\frac1m\langle u\,b\circ\theta+c\circ\theta\rangle_\phi .
 \tag{P.2}
\]
因而完整物理矩可以直接在 moving 角计算，无须将有限 moving Fourier
冒作有限物理 Fourier，也无须数值反演角图。

写变化 \(h=(h_1,h_2)\)、\(z=\langle h_2\rangle\)。由 (P.1)
\[
 \delta\theta=\frac1m I(h_2-zv/m).
 \tag{P.3}
\]
令 \(B_b=b\circ\theta,\ C_c=c\circ\theta\) 和
\[
 t=u(b_\theta\circ\theta)+(c_\theta\circ\theta).
\]
对 (P.2) 微分，并使用 \(I^*=-I\)，得到准确梯度
\[
 \boxed{\begin{aligned}
 {\cal M}_{b,c}^*(Q)_1&=\frac{B_b}{m},\\
 {\cal M}_{b,c}^*(Q)_2&=
 -\frac{It}{m^2}
 +\frac{\langle vIt\rangle}{m^3}
 -\frac{\langle uB_b+C_c\rangle}{m^2}.
 \end{aligned}}                                      \tag{P.4}
\]
即 \(D{\cal M}_{b,c}[h]=\langle{\cal M}_{b,c}^*,h\rangle_\phi\)。
推导中 \(\langle tI(v-m)\rangle=-\langle vIt\rangle\)，所以
(P.4) 的第二个 mean 项具有正号。
公式只除非零 \(m\)，没有逐点 \(1/v\)；所有 mean 都保留。

两个直接核对是
\[
 {\cal M}_{0,1}^*=(0,-m^{-2}),\qquad
 {\cal M}_{1,0}^*=(m^{-1},-\langle u\rangle/m^2).
\]
反射类中后一式的第二项为零，但前一式的偶 mean 不能删除。
真实腰幅度
\[
 {\cal A}(v)=2\langle C\cos4\theta\rangle_\theta
\]
使用 \(b=0,c=2\cos4\theta\)；它的完整梯度就是 (P.4)，
而其 mean 已由
[腰 mean 列篇](R133-supplement-final-waist-mean-column-for-adjoint-lift.md)
实际证明处于
\[
 (-1.276033052468981,\,-1.276014207147490).
 \tag{P.5}
\]
这里使用原报告的更精确区间；显示端点向外舍入。

(P.4) 首先对有限光滑物理权成立。实际 finite dual 可以逐频用
\(e^{ik(\phi+\psi)}\) 的完整 Taylor/解析尾计算。未知的真实 nonlinear
DN 转置不通过假定其光滑系数截断计算，而由下节已付的完整算子界支付。
对一般 \(L^2\) 物理权，(P.4) 中的导数按分布与已经支付的 trace
连续延拓解释；不能从此式免费断言裸角导数在 \(L^2\) 有界。

## 2. 原始第四模与保留外行必须合成同一个物理权

真实外端 nonlinear 图及其导数是
\[
 J_\theta B+Q_\theta Z=d(Z,f_B),\qquad
 C_0-C_{\rm ref}=c_0(Z,f_B),\qquad Z=C_{\ne0}-C_{{\rm ref},\ne0}.
\]
在当前径向参考下 \(C_{{\rm ref},\ne0}=0\)。
记其固定背景处线性行
\[
 {\cal R}h=J_\theta\delta B+
                (Q_\theta-D_Zd)\delta Z,\qquad
 {\cal C}h=-z/m_R^2-D_Zc_0\,\delta Z .
 \tag{P.6}
\]
\(J_\theta\sin k\theta=\cos k\theta\)、
\(J_\theta\cos k\theta=-\sin k\theta\)，故 \(J_\theta^*=-J_\theta\)。

原暂列输出保持为
\[
 b_4[h]=2\langle\cos4\theta,{\cal R}h\rangle_\theta .
 \tag{P.7}
\]
令 \(\lambda_R(\theta)\) 是保留非mean 外行的 finite 真物理 cosine 权，
其 \(\cos4\theta\) 系数准确为零。定义
\[
                   w_R=2\cos4\theta-\lambda_R.        \tag{P.8}
\]
若有限数据向量按 real cosine 幅度配对，
应使用 \(\lambda_R=2\sum_j\lambda_j\cos4j\theta\)，不能漏掉2。
若原 solver 行除以 \(\alpha\)，物理乘子还须除以同一准确 \(\alpha\)。
体 trial 的 Hilbert 密度也不能直接用未转换的有限矩阵转置向量代替。

对真实物理 mean 乘子 \(\lambda_{\rm mean}\)，准确有
\[
 b_4-\langle\lambda_R,{\cal R}\rangle-\lambda_{\rm mean}{\cal C}
       =D{\cal M}_{b,c},
\]
其中
\[
 b=-J_\theta w_R,\qquad
 c=(Q_\theta-D_Zd^*)w_R
          -\lambda_{\rm mean}
          +\lambda_{\rm mean}(D_Zc_0)^* .
 \tag{P.9}
\]
最后两个转置算子作用于完整物理非mean 空间，其未知高模没有删除。
把 \(Q_\theta\) 换为实际数值 proposal
\[
 q_{\rm num}=\frac{562949953420957}{562949953421312}
\]
仅定义一个显式比较行，不能授它 true regular 的身份。
已发表的完整实际费用为
\[
 L_d=5.898255\,10^{-6},\quad L_0=7.372818\,10^{-7},\quad
 \epsilon_{\rm prop}=9.1496\,10^{-18}+2^{-512},
 \quad
 \|\delta Z\|_{L^2_\theta}<.03\|h_2\|_{L^2_\phi}.
 \tag{P.10}
\]
\(\epsilon_{\rm prop}\) 保留全部真实 regular 指数误差，包括第四模；
不依赖该模恰好零误差的特殊停止选择。
(P.9) 与模型 \({\cal M}_{-Jw_R,q_{\rm num}w_R-\lambda_{\rm mean}}^*\)
之差仅在 moving 第二分量，且其完整 \(L^2\) 范数小于
\[
 .03\{(L_d+\epsilon_{\rm prop})\|w_R\|_2
                                  +L_0|\lambda_{\rm mean}|\}.
 \tag{P.11}
\]
这里用真实全算子的 Hilbert 转置；没有取 finite head 后将外尾清零。

## 3. 实际纯 mean 端列，比通用 \(1/v\) 界更紧

从最终真实端口证书直接消费
\[
 5.8<|m_R|<7,\quad
 \|\psi_R\|_{A^{1/8}}<P=1.480385\,10^{-11},\quad
 \|u_R\|_{A^{1/8}}<U=1.643190\,10^{-9}.
 \tag{P.12}
\]
所有背景及目标身份与 (P.10) 相同。
用 \(e_1=8P,\ e_2=128P\) 得
\(\|\psi_\phi\|_\infty\le e_1,\|\psi_{\phi\phi}\|_\infty\le e_2\)、
\(\|u_\phi\|_\infty\le8U\)。
物理 \(L^2\) 换测度至多付 \(\sqrt{1+e_1}<1+e_1\)。

对纯 mean 变化 \(h=e_2=(0,1)\)，(P.3) 为 \(-\psi/m\)。
保持物理角的真实变化因此准确给
\[
 \delta Z\circ\theta=\frac1{m^2}
  \left[1-\frac1{(1+\psi_\phi)^2}
                  -\frac{\psi\psi_{\phi\phi}}{(1+\psi_\phi)^3}\right],
 \tag{P.13}
\]
\[
 \delta B\circ\theta=\frac1{m^2}
 \left[\frac{u_\phi\psi-u}{(1+\psi_\phi)^2}
            -\frac{u\psi\psi_{\phi\phi}}{(1+\psi_\phi)^3}\right].
 \tag{P.14}
\]
这些式子的物理 mean 已经分别是0和0；它们不是未经比较的 moving mean。

令 \(g=1-e_1\)。完整有理预算实际计算
\[
 Z_m=\frac{1+e_1}{5.8^2}
   \left[\frac{2e_1+e_1^2}{g^2}+\frac{Pe_2}{g^3}\right]
                 <7.05\,10^{-12},
\]
\[
 B_m=\frac{1+e_1}{5.8^2}
   \left[\frac{U(1+8P)}{g^2}+\frac{UPe_2}{g^3}\right]
                 <4.885\,10^{-11}.
 \tag{P.15}
\]
所以完整 true Robin mean 列满足
\[
 \|{\cal R}e_2\|_2
 \le B_m+(1+L_d+\epsilon_{\rm prop})Z_m
                  <5.591\,10^{-11}.                   \tag{P.16}
\]
\(q_{\rm num}<1\)，而真实 \(Q\) 相差最多
\(\epsilon_{\rm prop}\)；因而 (P.16) 没有遗漏 regular multiplier 的尾。

真实外 mean 标量
\[
 \omega_R={\cal C}e_2=-m_R^{-2}-D_Zc_0\,{\cal Z}_z
\]
满足
\[
 m_R^2L_0 Z_m<3\,10^{-16},\qquad
       \omega_R<0,\qquad |\omega_R^{-1}|<50 .          \tag{P.17}
\]
这是整个偶 mean 行的可逆性，不是全补逆或参数横截。

## 4. 两端 mean 对偶行准确满足

使用
[完整 mean 回填消费者](R133-supplement-mean-completed-head-and-adjoint-body-consumer.md)
的 \(\psi_{\rm ad}=\lambda+\mu e_2\)：
\(\lambda\) 是给定 nonmean body trial，
\[
 \mu'=-c_m\mu-\langle a_{\rm int},\lambda\rangle,\qquad
 \mu(0)=\lambda_{\rm amp}D{\cal A}(v_0)[1].
 \tag{P.18}
\]
这是准确 ordinary scalar 解，数值实现必须完整包住它，不能代以未经验证的
近似积分。

在外端置
\[
 c_R=\langle w_R,{\cal R}e_2\rangle_\theta,\qquad
 \boxed{\lambda_{\rm mean}
                    =\frac{c_R-\mu(R)}{\omega_R}.}     \tag{P.19}
\]
于是原物理外 mean 对偶行准确为零。此式与先前
\(\mathcal P\) 预处理后再回填转置的公式相同，明确包含
\(\omega_R^{-1}\)。没有要求能先计算完整 DN 转置的逐模矩阵。

(P.16)–(P.17) 实际给
\[
 |\lambda_{\rm mean}|
 <50|\mu(R)|+2.8\,10^{-9}\|w_R\|_2.                   \tag{P.20}
\]
将它代入 (P.11)，得到完整未知 DN/regular 的外对偶模型费
\[
 \boxed{\
 \|\Delta_{\rm out}\|_{L^2_\phi}
 <1.77\,10^{-7}\|w_R\|_2
                   +1.106\,10^{-6}|\mu(R)|.}
 \tag{P.21}
\]
mean 对偶行已经准确满足，所以只需计算
\[
 P_\perp\{
 {\cal M}_{-Jw_R,q_{\rm num}w_R}^*-\psi_{\rm ad}(R)\}
 \tag{P.22}
\]
并加 (P.21)。
\({\cal M}_{0,-\lambda_{\rm mean}}^*\) 纯属 mean，故在 (P.22)
准确消失；它在 (P.19) 中的真实作用并未删除。

腰端取完整奇 Dirichlet 乘子
\(\lambda_{0,1}=\lambda_1(0)\)，与实际保留的全部 \(u(0)=0\) 行配对。
则腰第一对偶行准确为零。腰第二行是
\[
 P_\perp\{\lambda_2(0)
             -\lambda_{\rm amp}{\cal M}_{0,2\cos4\theta_0}^*{}_2\}.
 \tag{P.23}
\]
其 mean 因 (P.18) 准确满足，nonmean 完整解析尾继续保留。
这不把 response trial 的腰 Dirichlet 或幅度残差设零；
它们在下一节的 corrected scalar 中都存在。

## 5. 全接口及 corrected scalar 的准确符号

令完整 response 是 \(h=w+ze_2\)，其中 mean 用真实 scalar ODE
和真实 homogeneous 外 mean 图回填。令
\[
 R_h={\cal D}h-F_\nu,\quad R_\psi={\cal D}^*\psi_{\rm ad}.
\]
两者的第二 mean 准确为零，但 nonmean 完整输出并非零。
所有 radial joins 取 response、adjoint、background 的真正共同细分；
记 \([h]=h^+-h^-\)，右迹记 \(+\)。

原全数据功能的 jump 权必须取 \(\psi_{\rm ad}(r_i^+)\)。
ordinary mean 解连续，所以
\[
 \langle\psi_{\rm ad}(r_i^+),[h]_i\rangle
               =\langle\lambda(r_i^+),[w]_i\rangle .
 \tag{P.24}
\]
有限 trial 的这些配对可由每个原 double 的准确 dyadic Horner
作有理数计算；sine/cosine 两个非mean部分各带 Parseval 的 \(1/2\)。
不能换成左迹，也不能只报告 jumps 范数后删除其有符号配对。

由原完整 Green 恒等式
\[
 b_4-\Lambda\overline A
 =\langle E_R,h_R\rangle+\langle E_0,h_0\rangle
       -\int\langle R_\psi,h\rangle\,dr
       +\sum_i\langle[\lambda]_i,w_i^-\rangle .
 \tag{P.25}
\]
\(E_R,E_0\) 分别由 (P.22) 加真实费用和 (P.23) 给出。
所有 mean 项准确回填，所有 nonmean jumps 留在 (P.25)。
若 trial 的 adjoint 本身分片不连续，最后一项尤其不可删除。

对于真实参数 response，\(\delta f_B=0\)，参数控制在腰及外端恒零。
令 \(y_R=P_\perp h_2(R)\)。
原 corrected scalar 的显式模型是
\[
\begin{aligned}
 S_{\rm mod}={}&
  \langle{\cal M}_{-Jw_R,q_{\rm num}w_R}^*,h_R\rangle\\
 &-\langle\lambda_1(0),w_1(0)\rangle
       -\lambda_{\rm amp}D{\cal A}(v_0)[h_2(0)]\\
 &-\int_0^R\langle\lambda,R_h\rangle\,dr
       -\sum_i\langle\lambda(r_i^+),[w]_i\rangle .
\end{aligned}                                                   \tag{P.26}
\]
这里 \(z(0),z(R)\) 和 \(\mu(R)\) 使用原真实 mean 回填；
它们虽未知精确数值，完整区间解会包住真实值。
参数 response 的完整 mean residual 准确为零，
所以没有一个被遗忘的 \(\lambda_{\rm mean}{\cal C}h\)。
真实 nonlinear 背景残差仍在另一个完整存在性数据列中，并未因此设零。

(P.26) 与真实 \(S_{\rm corr}=b_4[h]-\Lambda r_\nu\) 的唯一外模型差是
\[
 \langle w_R,(Q-q_{\rm num}-D_Zd)\delta Z_h\rangle.
\]
已有真实 mean 图给
\(|z(R)|<1.084\,10^{-6}\|y_R\|_2\)。用 (P.10) 及
\(\sqrt{1+x}\le1+x/2\)，10门实际预算证明
\[
 \boxed{\ |S_{\rm corr}-S_{\rm mod}|
       <1.77\,10^{-7}\|w_R\|_2\|y_R\|_2.\ }            \tag{P.27}
\]
此费包括全部 true regular 模式和整个 nonlinear cap derivative，
不以末端曲率很小为由将其设零。
独立 \(\delta f_B\)、ordinary mean/source、原候选 nonlinear boundary
残差在其完整 affine 问题中仍须按原图加入；(P.26) 明确只针对当前
齐次外数据的参数 response。

## 6. 原始保留边界范数与最终门

在计算 primal \(r_\nu\) 的外残差范数时，必须去掉**原物理**
\(\cos4\theta\) 输出，而非 moving \(\cos4\phi\)；
该行正在由 Schur 单独关闭。若使用 physical Fourier 矩，应保留全部
其它模式及解析无限尾。若在 moving pullback 中计算，则用实际
\(j=v/m\) 加权的 \(L^2_\phi\) 正交投影：
\[
 P_{\ne4,\theta}f\circ\theta
  =f\circ\theta-
  2\langle(f\circ\theta)\cos4\theta\,j\rangle_\phi\cos4\theta .
 \tag{P.28}
\]
在真实 even nonmean 空间中，这就是原物理缺失行的投影。
不能用未保留第四行的大小去冒称某个 retained residual，更不能直接把它删在
moving 频谱的第四槽里。

(P.21)、(P.23)、(P.25)、(P.27) 与完整 body residual 共同提供原
双残差标量门需要的量：
\[
 \mathscr S_\nu=S_{\rm corr}
 -(b_4-\Lambda\overline A)[\overline A^{-1}r_\nu].
\]
只有在同一完整状态/source/trace/jump 空间实际支付
\(\overline A^{-1}\)，并且该完整误差严格小于
\(|S_{\rm corr}|\) 后，才可宣称真正 \(\nu\) 标量非零。

## 7. 实际执行和范围

- [精确 BigInt 预算源码](../scripts/fourfold_codazzi_physical_boundary_transpose_budget.mjs)；
- [10门有理报告](../notes/2026-11-14-R133-complete-physical-boundary-transpose-rational.json)。

报告由当前可用 V8 实际执行同一完整函数生成；
Node 包装仅提供恢复环境后的可重算入口。
10门涵盖 (P.15)–(P.17)、(P.20)–(P.21) 和 (P.27)，全为严格有理比较。
没有运行原不存在的 response/adjoint trial，
也没有上传伪造的 full candidate native。
完整物理边界消费者、全部 trial 接口配对和真实全补逆仍须实际完成。
