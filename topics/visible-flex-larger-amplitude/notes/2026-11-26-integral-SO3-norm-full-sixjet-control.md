# 2026-11-26：完整积分范数对原meridian表示六个物理jet的径向网格无关控制

## 1. 本引理的用途和条件

**状态：已证明（完整条件引理）。**

这是一个无编号的完整条件引理，补充积分范数的实际数学作用；它不重登记积分矩阵正定性、白化或带状QR结论，也不将已返回的几何失败归因于某一种范数。

对象是原234ac/7f26采用的同一个连续meridian表示
$$
F(s,\phi)=\Gamma_c(\phi)+I(s,\phi)+h(s)\Delta(\phi),\quad
I(s,\phi)=\int_0^sT(u,\phi)\,du,
$$
$$
T=\exp([\Omega]_\times)T_0,\qquad
\Delta=P_H-\Gamma_c-I(S),\qquad h(s)=S_5(s/S).
$$
这里 $S$、cap 半径 $R$、固定材料图 $\theta_0$ 和固定单位参考 $T_0$ 保持；全部 free core、全部旋转自由量和 $H$ 可以同时变化。本文控制的是精确连续函数，不把工作Gauss积分、浮点Cholesky、工作逆图或近似S/宽度直接称为精确函数。

假设：

1. $S>0$、$\ell>0$，固定有限角带宽；每个旋转分量使用原完整odd/odd/even三角模式及共享五次径向函数。
2. 原结构端值满足 $\Omega(0,\phi)=\Omega(S,\phi)=0$。额外cap slope条件仍保留，但以下估计无需使用它。
3. 固定 $T_0$ 是单位向量，具有下文要求的连续 $T_{0,s}$、$T_{0,\phi}$、$T_{0,\phi\phi}$，其真上界已支付。
4. 当前 core 的 $\rho_x$ 在全角具有严格正真下界 $r_0$；扰动满足下述保正性条件。固定 $\theta_0$ 的 $\rho_0$ 和 $\rho_0^\prime$ 全角上界已支付。
5. 全部积分和范数采用同一个精确 $s$ 域与同一组真实径向宽度。若计算实现采用近似载体，差额另付，见第8节。

**结论：**对固定有限角带宽，完整径向积分范数的小扰动在上述正图域内控制 $F$、$F_s$、$F_\phi$、$F_{ss}$、$F_{s\phi}$、$F_{\phi\phi}$ 的全域上确界差。所有常数都不依赖最小径向胞宽或胞数；条件仍允许全部core/H变量同时变化。这里不使用一般的“H²控制二阶点态导数”错误命题：原表示的 $F_{ss}$ 只需要 $T_s$，而 $T_s$ 只含 $\Omega_s$，不需要 $\Omega_{ss}$ 的点态上界。

## 2. 精确一维Green核

设 $v\in H^2(0,S)$，$v(0)=v(S)=0$。由两次积分和端值消去 $v^\prime(0)$，
$$
v'(s)=
\int_0^s\frac{t}{S}v''(t)\,dt
-\int_s^S\left(1-\frac tS\right)v''(t)\,dt.
$$
故Cauchy–Schwarz给出
$$
|v'(s)|
\le
\sqrt{\frac{s^3+(S-s)^3}{3S^2}}\,\|v''\|_{L^2}
\le\sqrt{\frac S3}\,\|v''\|_{L^2}. \tag{1}
$$

同样，
$$
v(s)=
-\int_0^s\frac{t(S-s)}{S}v''(t)\,dt
-\int_s^S\frac{s(S-t)}{S}v''(t)\,dt.
$$
核的 $L^2$ 范数平方为 $s^2(S-s)^2/(3S)$，从而
$$
|v(s)|
\le\frac{s(S-s)}{\sqrt{3S}}\,\|v''\|_{L^2}
\le\frac{S^{3/2}}{4\sqrt3}\,\|v''\|_{L^2}. \tag{2}
$$
这两个恒等式适用于整个共享五次C²函数；胞间端jet已共享，所以没有额外跳跃分布或未付胞界项。证明中没有使用最小胞宽。

## 3. 有限角模式与完整旋转扰动

记三个通道的频率集合为
$$
\mathcal V_x=\mathcal V_y=\{1,3,\ldots,2M+1\},\qquad
\mathcal V_z=\{2,4,\ldots,2M\}.
$$
令 $\sigma_\nu^2=1+(\nu/\tau)^2$，其中 $\tau>0$ 是原显式角向 transition。定义
$$
K_j=\max_{a\in\{x,y,z\}}
\sum_{\nu\in\mathcal V_a}\frac{\nu^{2j}}{\sigma_\nu^2},
\qquad j=0,1,2.
$$
这些是固定有限带宽下的显式有限常数；不声称它们在 $M$ 趋于无穷时有统一界。

旋转扰动的完整积分能量记为
$$
\varepsilon_\Omega^2=
\sum_{a,\nu}\sigma_\nu^2
\int_0^S
\left(
|\delta\omega_{a,\nu}|^2+
\ell^2|\delta\omega'_{a,\nu}|^2+
\ell^4|\delta\omega''_{a,\nu}|^2
\right)ds.
$$
每个模态的二阶项由该能量支付。对每一通道先在模态上Cauchy–Schwarz，再对三个通道平方求和，并用 $K_j$ 的最大值，(1)–(2)严格给出
$$
d_j:=\|\partial_\phi^j\delta\Omega\|_\infty
\le
\frac{S^{3/2}}{4\sqrt3\ell^2}\sqrt{K_j}\,
\varepsilon_\Omega,
\qquad j=0,1,2, \tag{3}
$$
$$
d_s:=\|\partial_s\delta\Omega\|_\infty
\le
\frac{\sqrt{S/3}}{\ell^2}\sqrt{K_0}\,
\varepsilon_\Omega. \tag{4}
$$
向量上确界均采用Euclidean范数。使用通道最大值的原因是各通道能量相加；不必把三个通道的频率和先相加再冒作准确最优常数。

这正是径向细化时所需要的稳定性差别：固定 $M$、$S$、$\ell$、$\tau$ 时，上式没有 $h_{\min}$ 的负幂。它没有声称 $\Omega_{ss}$ 的 $L^\infty$ 范数受同一能量控制。

## 4. 同时支付全部free core和H

原support写成
$$
p_c(\psi)=1+\sum_\nu c_\nu\cos(\nu\psi),\quad
\rho_c(\psi)=1+\sum_\nu(1-\nu^2)c_\nu\cos(\nu\psi),
$$
$$
\Theta_c(\psi)=\psi+
\sum_\nu\frac{1-\nu^2}{\nu}c_\nu\sin(\nu\psi).
$$
只在原 free 集合 $\mathcal V_f$ 上改变 core；固定前三项仍固定。令
$$
\varepsilon_c^2=\sum_{\nu\in\mathcal V_f}
((1-\nu^2)\delta c_\nu)^2,\quad n=|\mathcal V_f|,
$$
$$
A_\Theta=\left(\sum_{\nu\in\mathcal V_f}\nu^{-2}\right)^{1/2},
\quad
A_\Gamma=\left(\sum_{\nu\in\mathcal V_f}
\frac{1+\nu^2}{(1-\nu^2)^2}\right)^{1/2}.
$$
原 free 频率均非 $1$，所以这些式子有定义。直接Cauchy–Schwarz给出
$$
\|\delta\Theta\|_\infty\le A_\Theta\varepsilon_c,\qquad
\|\delta\rho\|_\infty\le\sqrt n\varepsilon_c. \tag{5}
$$
令 $r=r_0-\sqrt n\,\varepsilon_c$，并要求 $r>0$，则扰动后的整个 $\rho$ 也至少为 $r$，旧 $\rho$ 也至少为 $r$。

令 $\psi_x$、$\psi_y$ 在同一个实 lift 上分别解
$\Theta_x(\psi_x)=\theta_0(\phi)$、$\Theta_y(\psi_y)=\theta_0(\phi)$。
$\Theta$ 严格递增且 $\Theta(\psi+2\pi)=\Theta(\psi)+2\pi$，原正弦表示统一取 $\Theta(0)=0$，因此不存在可任意选择的浮点 wrap。由(5)和真导数下界，
$$
\|\psi_y-\psi_x\|_\infty
\le L_\psi:=A_\Theta\varepsilon_c/r. \tag{6}
$$

记
$$
R_0=\|\rho_x\|_\infty,\quad R_1=\|\rho'_x\|_\infty,\quad
Q_0=\|\rho_0\|_\infty,\quad Q_1=\|\rho'_0\|_\infty.
$$
当前 core 曲线为
$\Gamma_c(\phi)=p_c(\psi_c)e_r(\psi_c)+p_c^\prime(\psi_c)e_t(\psi_c)$。
这里必须使用普通法向架 $e_r(\psi)$、$e_t(\psi)$；$e_r(\Theta_c(\psi))$ 是另一个角度的向量。

完整链式法则中的消去给出
$$
\Gamma_{c,\phi}=\rho_0e_t(\psi_c),\qquad
\Gamma_{c,\phi\phi}
=\rho'_0e_t(\psi_c)
-\frac{\rho_0^2}{\rho_c(\psi_c)}e_r(\psi_c). \tag{7}
$$
于是以下真界足够：
$$
G_0:=\|\delta\Gamma\|_\infty
\le A_\Gamma\varepsilon_c+R_0L_\psi, \tag{8}
$$
$$
G_1:=\|\delta\Gamma_\phi\|_\infty
\le Q_0L_\psi, \tag{9}
$$
$$
G_2:=\|\delta\Gamma_{\phi\phi}\|_\infty
\le
\left(Q_1+\frac{Q_0^2}{r}\right)L_\psi
+\frac{Q_0^2}{r^2}
\left(\sqrt n\varepsilon_c+R_1L_\psi\right). \tag{10}
$$
(8) 中先在同一 $\psi_y$ 比较两个 support，再沿旧曲线移动 $\psi$；旧曲线关于 $\psi$ 的速度是 $\rho_x$。
(10)中使用
$$
|\rho_y(\psi_y)-\rho_x(\psi_x)|
\le\sqrt n\varepsilon_c+R_1L_\psi
$$
及两个正分母均至少为 $r$，所以没有漏付当前free core的逆图链。

cap 点为 $P_H(\phi)=R e_r(\theta_0(\phi))+H e_z$。$R$ 与 $\theta_0$ 固定，故
$$
P_0:=\|\delta P\|_\infty=|\delta H|,\qquad P_1=P_2=0. \tag{11}
$$
完整积分范数满足
$\varepsilon_\Omega^2+\varepsilon_c^2+|\delta H|^2=\varepsilon^2$；因此上面所有扰动块均由完整 $\varepsilon$ 支付，没有冻结任何一个原自由块。

## 5. 旋转与固定参考的完整低阶链

对实反对称矩阵 $A$，$\exp(A)$ 正交。Duhamel 的 $k$ 重有序积分对所有排列求和后，总单纯形体积为 $1$，因此
$$
\|D^k\exp(A)[B_1,\ldots,B_k]\|_{op}
\le\prod_i\|B_i\|_{op},\qquad k=1,2,3. \tag{12}
$$
沿 $\Omega$ 到 $\Omega+\delta\Omega$ 的实反对称线段应用此式，不产生 $\exp(\|\Omega\|)$ 因子。

令 $A_s$、$A_1$、$A_2$ 分别是真实旧 $\Omega_s$、$\Omega_\phi$、$\Omega_{\phi\phi}$ 的全域上界，设
$W_s=A_s+d_s$、$W_1=A_1+d_1$、$W_2=A_2+d_2$。本节记 $\mathcal R=\exp([\Omega]_\times)$，下式的 $B_{R_*}$ 表示该旋转矩阵相应导数的差上界，不是 cap 半径的变化。
完整微分给出可用的上界
$$
B_R=d_0,\quad
B_{R_s}=d_s+W_sd_0,\quad
B_{R_\phi}=d_1+W_1d_0, \tag{13}
$$
$$
B_{R_{\phi\phi}}=
d_2+2W_1d_1+(W_1^2+W_2)d_0. \tag{14}
$$
这些常数来自对整个线段的导数上界；它们不要求小角近似，也不丢掉二阶交叉项。

记固定单位参考真上界
$B_s=\|T_{0,s}\|_\infty$、$B_1=\|T_{0,\phi}\|_\infty$、
$B_2=\|T_{0,\phi\phi}\|_\infty$。由于当前 core 变化不改变固定 $T_0$ 或固定材料角，$T=\mathcal R T_0$ 的全部相关差值由
$$
b_0=d_0,\qquad
b_s=B_{R_s}+d_0B_s, \tag{15}
$$
$$
b_1=B_{R_\phi}+d_0B_1,\qquad
b_2=B_{R_{\phi\phi}}+2B_{R_\phi}B_1+d_0B_2 \tag{16}
$$
支付，分别控制 $\delta T$、$\delta T_s$、$\delta T_\phi$、$\delta T_{\phi\phi}$。
特别是 (15) 只要求 $\Omega_s$；没有引入未受积分范数控制的 $\Omega_{ss}$ 点态项。

## 6. 闭合项Delta的全部变化与六jet最终界

把同一个表示重写为
$$
F=(1-h)\Gamma+hP+I(s)-hI(S). \tag{17}
$$
对于 $j=0,1,2$，$I_j(s)-hI_j(S)$ 的扰动可分成
$$
(1-h)\int_0^s\delta T_j-
h\int_s^S\delta T_j.
$$
由于 $0\le h\le1$，其范数至多
$$
L_h(s)b_j,\qquad
L_h(s)=(1-h)s+h(S-s)\le S. \tag{18}
$$
于是
$$
\|\delta\partial_\phi^jF\|_\infty
\le\max(G_j,P_j)+Sb_j,
\qquad j=0,1,2. \tag{19}
$$
这支付了 $F$、$F_\phi$ 和 $F_{\phi\phi}$；没有冻结 $\Delta$ 或用旧闭合差抵消新闭合差。

对 $S_5$ 精确曲线，
$$
H_1=\|h'\|_\infty=\frac{15}{8S},\qquad
H_2=\|h''\|_\infty=\frac{10}{\sqrt3 S^2}. \tag{20}
$$
$F_s=T+h^\prime\Delta$ 和 $F_{s\phi}=T_\phi+h^\prime\Delta_\phi$ 给出
$$
\|\delta F_s\|_\infty
\le b_0+H_1(P_0+G_0+Sb_0), \tag{21}
$$
$$
\|\delta F_{s\phi}\|_\infty
\le b_1+H_1(P_1+G_1+Sb_1). \tag{22}
$$
最后 $F_{ss}=T_s+h^{\prime\prime}\Delta$，故
$$
\|\delta F_{ss}\|_\infty
\le b_s+H_2(P_0+G_0+Sb_0). \tag{23}
$$
(19)、(21)–(23)完整覆盖六个物理jet。$\Delta$ 的 core、$H$ 和完整终积分变化全部在 $G_j$、$P_j$、$S b_j$ 中支付。

固定 $S$、$\ell$、有限 $M$、完整参考上界和正图余量时，上式右端随 $\varepsilon$ 趋于 $0$ 而趋于 $0$，且各常数不依赖径向网格的胞数或最小宽度。这证明所宣称的完整六jet连续控制；它不是一般 $H^2$ 函数的二阶 $L^\infty$ 嵌入。

## 7. 可推论和不可推论的边界

对同一个已知真正则的父场，若第一基本形式的 $E$、$EG-\mathsf F^2$ 等在整个域具有真正下界，则上述六jet界可进一步代入完整度量、面积和主曲率的连续公式，得到保持严格几何余量的充分扰动条件。必须把那些真下界和相应代数Lipschitz界实际支付，不能只说“连续”就把有限screen变为reach证书。

因此本引理解释了：原meridian特殊积分表示下，完整积分范数能够控制相关物理jet，并且允许全部free core/H同时变化。它没有证明某次 QP 或 SOC 会给出足够小的 $\varepsilon$，没有证明现有连续几何余量，也没有证明 $M$、$N$ 或工作积分精化已经收敛。

固定 $M$ 是必要范围。$K_2$ 和 core 的频率常数随角带宽变化，故本文不自动给出 $J/M/N$ 同时精化时统一不变的常数。新的有限 $M$ 可能采用新的明确常数，或需另证更强角向范数；不能暗换这个条件。

## 8. 数学范数与当前工作实现的区分

本文 $\varepsilon$ 是同精确连续域上实际系数函数的积分范数。浮点带矩阵、Cholesky因子、solve和当前报告的Euclidean coordinate norm只给出一个工作实现；其canonical hash说明输入身份，不证明精确等距白化。

若把本引理用于最终严格消费，须由精确积分/区间包围，或已经支付的因子缺陷、宽度载体及转置误差，给出 $\varepsilon$ 的真上界。固定 $T_0$ 的单位性与三个真导数上界、core 全角 $\rho$ 下界、$\Gamma$ 逆图、$S$、$h$、$h^\prime$、$h^{\prime\prime}$ 的真实域也须采用同一个模型。工作 $\widehat h$ 及真实 $h$ 的差额应由完整 outward 费用支付，不能将 $\widehat h$ 的数值峰值代入 (20) 冒作真实峰值。

这不增加当前优化算法的执行前门；原完整integral入口可以依授权直接运行并真实返回。本文只是未来解释和严格消费该范数时可用的完整条件估计。没有本地科学计算、没有新fixture、没有新成功或完成宣称。

## 9. 来源与核查范围

本引理的连续表示和完整范数对应已刊 [7f26 完整 direct-axisymmetric 算子](../scripts/resume_20261126/so3_axisymmetric_meridian_operator.py)，完整源码 SHA256 为 `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf`；其原物理与范数公式来自 [234ac 完整 normalized-parent 算子](../scripts/resume_20261126/so3_closed_meridian_operator.py)。原代码把核心插值系数命名为 $1-S_5$，本文把端点闭合系数命名为 $h=S_5$，两种写法通过 (17) 完全相同。这里没有把近似参考或工作宽度当成已认证的精确参考。

上述证明已由独立代理完整静态核对 Green 核、原频率权、全部 core 逆图、旋转混合项与六 jet 传播；检查没有运行科学计算，也不为当前 integral 方向新增执行门槛。
