# R133 补篇：完整 moving 标架、均值残差与几何误差

## 1. 对象、坐标及准确方程

取本文已使用的径向度量
\(g=a^2(\gamma^2dr^2+d\theta^2)\)，
\(\beta=a'/a\)，因此
\[
 \beta'=\beta\gamma'/\gamma-a^2\gamma^2K.                 \tag{1}
\]
本篇不改变目标度量、moving 状态、真实均值或任何边界条件。
令 \(q=(u,v)\)，\(m=\langle v\rangle_\phi<0\)，
\(v<0\)，\(S=u^2+Kv^2\)，\(\bar S=\langle S\rangle\)，
\(d=-\beta I S\)。\(I\) 为四重周期的零均值 primitive。
奇偶类为 \(u,d\) 奇、\(v\) 偶；故 primitive 的零均值规范也在
\(\phi=0\) 给零值。使用全部方程残差
\[
\begin{split}
 u_r&=d u_\phi+\gamma mK v_\phi-\beta u(1+S)+R_u,\\
 v_r&=d v_\phi-\gamma m u_\phi+\beta v(1-S)+R_v,
 \qquad R_0=\langle R_v\rangle .                       \tag{2}
\end{split}
\]
分部积分，保留均值后，准确得到
\[
 m_r=\beta m(1-\bar S)+R_0.                             \tag{3}
\]

真实坐标 lift 为
\(\theta=\phi+I(v-m)/m\)，\(\theta_\phi=v/m>0\)。定义
\[
 \tau=dv/m-\gamma u.
\]
由 (2)–(3) 和奇偶规范，
\[
 \theta_r=\tau+\frac1m I\left(R_v-\frac v mR_0\right). \tag{4}
\]
只有残差为零时才可写 \(\theta_r=\tau\)。未解中心的实际逆图仍必须
使用 (4)，不能以 \(\tau\) 偷换真实材料坐标导数。

## 2. 没有点态 \(1/v\) 分母的连接

在 \((r,\theta)\) 正交标架中取 meridian 单位向量 \(X\)、角向单位向量
\(Y\) 及外法向 \(N\)，使用原本文的 Gauss–Weingarten 符号。
对精确解变换到 \((r,\phi)\) 后：
\[
\begin{array}{ll}
 F_r=a\gamma X+a\tau Y,&F_\phi=avY/m,\\
 X_r=pY+qN,&X_\phi=AY+BN,\\
 Y_r=-pX+tN,&Y_\phi=-AX+CN,\\
 N_r=-qX-tY,&N_\phi=-BX-CY,
\end{array}                                                   \tag{5}
\]
其中完整系数是
\[
\begin{split}
 p&=\beta\tau/\gamma,&q&=a(\gamma Kv+du/m),&t&=ad/m,\\
 A&=\beta v/(\gamma m),&B&=au/m,&C&=a/m.             \tag{6}
\end{split}
\]
特别地，原 \(A_{II}=Kv+u^2/v\)、\(B_{II}=u/v\)、\(C_{II}=1/v\)
并未删去；下面两项是在换坐标后准确抵消：
\[
 \gamma A_{II}+\tau B_{II}=\gamma Kv+du/m,
 \qquad \gamma B_{II}+\tau C_{II}=d/m.                 \tag{7}
\]
因此 (6) 只须真实均值 \(m\) 离零，而不含点态 \(1/v\) 的腰部尖峰。
曲率本身仍须支付真实 \(v\) 离零，不能从这次连接化简省去 reach 条件。

定义
\[
 \Omega(x,y,z)=
 \begin{pmatrix}0&-x&-y\\x&0&-z\\y&z&0\end{pmatrix},
 \quad \Omega_r=\Omega(p,q,t),\quad\Omega_\phi=\Omega(A,B,C).
\]
即使 (2) 的残差非零，仍按 (6) 定义一个完整的 skew 连接。直接求导，
只代 (1)–(3)、\(d_\phi=-\beta(S-\bar S)\)，得到
\[
\begin{split}
 \mathcal R
 &=\partial_r\Omega_\phi-\partial_\phi\Omega_r+
                 [\Omega_r,\Omega_\phi]\\
 &=\Omega\left(
 \frac\beta{\gamma m}\left(R_v-\frac v mR_0\right),
 \frac a m\left(R_u-\frac u mR_0\right),
 -\frac a{m^2}R_0\right).                             \tag{8}
\end{split}
\]
这里完整普通源 \(R_u,R_v\) 和均值源 \(R_0\) 都存在，且无需对源求导。
令 \(f_r=(a\gamma,a\tau,0)^T\)、\(f_\phi=(0,av/m,0)^T\)，位置 torsion 为
\[
 \Omega_r f_\phi+\partial_r f_\phi-
 \Omega_\phi f_r-\partial_\phi f_r
 =\left(0,\frac a m\left(R_v-\frac v mR_0\right),0\right)^T. \tag{9}
\]
(8) 的三个分量可分别由 \(\|R_u\|_{A^0}\)、\(\|R_v\|_{A^0}\)、
真实 \(|m|\) 下界及全部 \(u,v\) 范数控制；\(|R_0|\le\|R_v\|_{A^0}\)。
不用把 \(R_v\) 粗转成 \(C_r\) 的 \(1/v^2\) 放大再估计位置误差。

## 3. 普通源的正交传播与真实接缝

固定 \(\phi\)，以真实端框架积分 \(Q_r=Q\Omega_r\)。若端框架正交，
\(Q\) 全程正交。定义角连接缺陷
\(E=Q_\phi-Q\Omega_\phi\)。则
\[
 E_r=E\Omega_r-Q\mathcal R.                            \tag{10}
\]
右端齐次传播和 \(Q\) 都正交，因此任一子区间的算子范数满足
\[
 \|E(r)\|\le \|E(R)\|+\int_r^R\|\mathcal R(s)\|\,ds
                   +\sum\|\Delta\Omega_\phi\|.       \tag{11}
\]
这是普通 \(L^1_r C^0_\phi\) 源合同，没有指数 Gronwall 因子。
同样积分 \(F_r=Qf_r\)，置 \(P=F_\phi-Qf_\phi\)，得到
\[
 P_r=Ef_r-Q\mathcal T,
\quad
 \|P(r)\|\le\|P(R)\|+
 \int_r^R(\|E\|\,|f_r|+|\mathcal T|)\,ds+
 \sum|\Delta f_\phi|,                                 \tag{12}
\]
其中 \(\mathcal T\) 是 (9)。浮点 RK 的径向积分误差另按正交 Duhamel
估计，不能把浮点轨迹直接当作 (10) 的精确积分。

候选三次片的真实端值跳跃必须进入 (11)–(12)。在同一个目标径向点，
记 \(\delta u,\delta v,\delta m\) 为两侧的完整跳跃，\(a,\beta,\gamma\)
连续。准确恒等式为
\[
\begin{split}
 \Delta(v/m)&=\frac{\delta v-\delta m}{m_+}
       -\frac{(v_--m_-)\delta m}{m_-m_+},\\
 \Delta(u/m)&=\frac{\delta u}{m_+}
       -\frac{u_-\delta m}{m_-m_+},\\
 \Delta(1/m)&=-\frac{\delta m}{m_-m_+}.                 \tag{13}
\end{split}
\]
\(\Delta\Omega_\phi\) 的三个系数依次是
\((\beta/\gamma)\Delta(v/m),a\Delta(u/m),a\Delta(1/m)\)，
\(\Delta f_\phi=(0,a\Delta(v/m),0)\)。完整 mean 跳和 nonmean 跳都保留。
这不是把中心小跳当成零接口。若改用此前 physical Jacobi 未知量，
仍须使用其已证 \(T_+PT_-^{-1}\) 接口，本文没有将它免费换成恒等。

## 4. 真正精确解的两基本型及用途

当 (2) 真正为零、完整端框架/位置匹配、所有周期/接缝条件已解时，
(5) 的第一基本型为
\[
 I=a^2\begin{pmatrix}\gamma^2+\tau^2&\tau v/m\\
                         \tau v/m&v^2/m^2\end{pmatrix},
\]
由 (4) 正是原度量的准确坐标 pullback。第二基本型为
\[
 II=a^2v\begin{pmatrix}\gamma^2K+d^2/m^2&d/m^2\\
                                    d/m^2&1/m^2\end{pmatrix}. \tag{14}
\]
于是 \(\det I=a^4\gamma^2v^2/m^2>0\)、\(\det II/\det I=K\)，
形算子的迹准确为 \(Kv+(1+u^2)/v\)。因此原候选全圆 \(v\)-gap 与
校正界仍可用于最大主曲率；(11)–(12) 给位置/法向的另外一套完整预算。

精确有理函数 producer
`scripts/fourfold_codazzi_moving_flat_frame_identity.py`
逐项展开 (8) 的九格、(9) 的三格、两次分母抵消及 (14) 的 determinant/trace；
原生记录为 `notes/2026-11-13-R133-moving-flat-frame-exact-identities.json`。
它是恒等式记录，不是抽样，不替代本文推导。

这组公式可直接用于当前 SHA ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413
的新 moving 中心。实际连续残差全片消费、全频 BVP 逆、非线性收敛、帽/tail
闭合、固定 marker、held 和 reach 仍须完成；本篇没有提前宣称精确闭面。
