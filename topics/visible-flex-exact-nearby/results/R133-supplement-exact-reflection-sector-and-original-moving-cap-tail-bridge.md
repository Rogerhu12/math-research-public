# R133 续篇：真实反射子类、原 moving 方程与完整帽—尾桥

2026-11-15，visible-exact-astra-0df9。

**状态：解析结论已证。** 原实际非线性构造的状态为
$u$ 奇、$v$ 偶。这里从完整方程及真实外图证明该子类不变，
并将已经完成的负阶/高阶帽—尾估计限制到它。在这一子类，
moving 角规范漂移及全部同类方向导数准确为零，故已付
$F_{\rm cov}$ 的帽逆就是原 $F$ 的帽逆。

一般全 $4\mathbb Z$ 的相位行保持
[G.17--G.21](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md)
的原形式；本文没有从其一般输入空间删除一列。原两个径向
$\Gamma^*$ 相位方程、强返回、完整主体 high 逆、$\nu$ Schur
和最终几何闭合也不是这里的角规范恒等式。

## 1. 已经规定的实际子类和全部均值

对标量和曲率 pair 定义
$$
 (\mathscr R f)(\phi)=f(-\phi),\qquad
 \mathscr J(u,v)=(-\mathscr R u,\mathscr R v),\qquad
 \mathcal X_+=\ker(\mathscr J-I).
 \tag{R.1}
$$
因此 $\mathcal X_+$ 恰为 $u$ 奇、$v$ 偶；不要求
$\langle v\rangle=0$。这些定义也用于复系数，仅是反射，
**不作复共轭**。$\mathscr J$ 是所有真实对称 Fourier 权、
物理 $H^s$ 和逐系数径向 supremum 后的 $\mathfrak M_s$
上的等距 involution。两个投影 $(I\pm\mathscr J)/2$ 有范数
不超过1，负阶使用同一对偶定义。

[完整 moving 带与 mean/参数行](R133-supplement-complete-moving-band-and-mean-parameter-Schur.md)
§1 已明确原实际构造的这个切空间。并非为本篇另造的候选：
[精确连续修补](R133-supplement-exact-continuous-repair-of-final-centre.md)
V.1--V.4 给原32个 sine $U$、33个 cosine $V$ 和所有同支集修补；
[真实连续方向](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md)
Q.1--Q.3 给96个 sine、97个 cosine 的完整 $Z$。故
$$
 \mathscr J\bar Q=\bar Q,\quad
 \mathscr JZ=Z,\quad
 \mathscr J(\bar Q+\delta Z)=\bar Q+\delta Z .
 \tag{R.2}
$$
此式对复 $\delta$ 也是代数恒等式。它不把该显式族说成 PDE
解，也不转授任何尚未验证的非零 $\delta$ 算子界。

实际背景定义仍为
$440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47$，
真实方向定义仍为
$6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04$。
频率仍是原 $4\mathbb Z$，材料角原点不变。

## 2. 从完整 moving 方程证明不变性

记 $I_\phi=\partial_\phi^{-1}(1-\Pi)$，包括准确的零模排除。
原真实径向参数 $K,\beta,\gamma$ 不依赖角。用
$$
 m=\Pi v,\quad S=u^2+Kv^2,\quad d=-\beta I_\phi S,
$$
$$
 F(Q)=
 \begin{pmatrix}
 d u_\phi+\gamma mK v_\phi-\beta u(1+S)\\
 d v_\phi-\gamma m u_\phi+\beta v(1-S)
 \end{pmatrix}.
 \tag{R.3}
$$
完整 primitive 满足
$\partial_\phi\mathscr R=-\mathscr R\partial_\phi$、
$I_\phi\mathscr R=-\mathscr R I_\phi$。因而
$$
 m(\mathscr JQ)=m(Q),\quad
 S(\mathscr JQ)=\mathscr R S(Q),\quad
 d(\mathscr JQ)=-\mathscr R d(Q),\quad
                  F(\mathscr JQ)=\mathscr JF(Q).
 \tag{R.4}
$$
逐项看，第一行是奇函数，第二行是偶函数。中间的完整卷积、
$\Pi v$、primitive 的零模处理和 $Kv^2$ 均未改变。

在一个 $\mathcal X_+$ 中心，
$$
 DF(Q)\mathscr J=\mathscr JDF(Q),\qquad
 D^kF(Q)[\mathscr Jh_1,\ldots,\mathscr Jh_k]
       =\mathscr JD^kF(Q)[h_1,\ldots,h_k].
 \tag{R.5}
$$
实际残差 $R=Q_r-F(Q)$ 也在 $\mathcal X_+$。
原分片的普通单侧残差跳保持该类；实际连续修补没有值跳 Dirac。
真实 affine 数据若属于该类，不能因解只取此类而被省略。

原参数 $\nu,\eta$、两径向 bump 及其真实系数导数仍是径向。
对 (R.4) 取参数导数，完整参数源在 $\mathcal X_+$。
特别原 normalized $\nu$ 列是
$$
 \alpha^{-1}\{F_\nu+DF(Q)(0,s_\nu)^t-(0,s_\nu')^t\},
 \qquad
 \langle(F_\nu)_2\rangle=-\beta m K_\nu(v^2)_0 .
 \tag{R.6}
$$
$s_\nu,s_\nu'$ 及末式的真实 mean 都保留。这里
$F_\nu$ 指在固定物理 $Q$ 处的完整 intrinsic 导数；不把它
换成有限响应。对 $\Gamma^*$ 的断言也是等变性，不替代其
source norm、移动切口和参考高度的实际收费。

## 3. 角规范、漂移及残差源的准确限制

在 $m\ne0$、$v/m>0$ 的原真实角图内，定义同一零 mean 规范
$$
 \Theta_Q(\phi)=\phi+m^{-1}I_\phi(v-m),\qquad
 \Phi_Q=\Theta_Q^{-1},\qquad
 \Psi(Q)=(u/v,1/v)\circ\Phi_Q .
 \tag{R.7}
$$
若 $Q\in\mathcal X_+$，则 $\Theta_Q,\Phi_Q$ 都为奇的次数1圆
微分同胚，所以物理 $B$ 奇、$C$ 偶。
一般状态也有
$\Theta_{\mathscr JQ}(\phi)=-\Theta_Q(-\phi)$，
故 $\Psi(\mathscr JQ)=\mathscr J\Psi(Q)$。
其微分和逆微分准确交换相应反射。

全图 G.10 的漂移为
$$
 A(Q)=\left\langle {dv\over m}-\gamma u\right\rangle,\qquad
                         F_{\rm cov}=F-AQ_\phi .
 \tag{R.8}
$$
由 (R.4)，$A(\mathscr JQ)=-A(Q)$，故
$$
 A|_{\mathcal X_+}=0,\qquad
 D^k A(Q)[h_1,\ldots,h_k]=0
 \quad(Q,h_1,\ldots,h_k\in\mathcal X_+),\quad k\ge1.
 \tag{R.9}
$$
径向参数的任意混合导数也满足此式，只要所有状态方向仍在
$\mathcal X_+$。也可由 G.21 逐项检查：
$\delta d$ 奇，$dv,\delta d\,v,dh_2,h_1$ 全奇，
而 $m,z_h$ 为完整 scalar，故平均准确为零。

因此在该子类上，不只基值相等，而且
$$
 F_{\rm cov}=F,\qquad
 D^k F_{\rm cov}[h_1,\ldots,h_k]
       =D^kF[h_1,\ldots,h_k].
 \tag{R.10}
$$
固定已经规定的角原点，即 G.17 中 $a(L)=0$。
真实解的 $a'=A$ 和同类 Jacobi 方向的 $a'=DA[h]$ 都给
$a(r)\equiv0$。于是 G.20 的 $aR_\phi$ 项准确为零；
这里并未把非解中心的真实残差 $R$ 设零，也未以“小”代替零。
同一个 $a$ 贯穿所有径向片，两端相位都是0，没有逐片重置角原点。

若取非反射方向、非零独立相位输入或不相容源，则不能使用
(R.9)--(R.10)。例如 $Q_\phi$ 在 $\ker(\mathscr J+I)$ 中，
其位于另一子空间的相位列仍按原 G.17--G.21 处理。
本文也不把一个任意材料角重标记宣称为允许的 ambient 刚体运动。

## 4. 完整 residual Hessian 和源/jump 的同类性

由 $\Psi$ 等变，$Q,R,h\in\mathcal X_+$ 时
$D^2\Psi[R,h]\in\mathcal X_+$。G.22 在这里给原方程的准确桥：
$$
 L_{\rm phys}(D\Psi h)
       =D\Psi(L_{\rm orig}h)+D^2\Psi[R,h].
 \tag{R.11}
$$
在 G.4 的完整 weighted primitive 中，
$Ch_2$ 偶、$I_\theta(Ch_2)$ 奇、$C$ 偶，所以
$m\langle C I_\theta(Ch_2)\rangle=0$。
同样 $e=E_R=I_\theta(CR_2)$ 奇。完整 inverse differential
及 $\langle h_2\rangle,\langle x_C\rangle$ 原样保留。

将已付 Hessian 写成
$H_Rx=\partial_\theta(-ex)+O_Rx$ 时，
$-ex$ 的第一分量偶、第二分量奇，而其角散度和 $O_Rx$
都在 $\mathcal X_+$。因此没有把不正确的散度 source 反射规则
放进物理 Green。

更完整地，同类 ordinary/jump 数据为 $(f_B,f_C)$、
$(j_B,j_C)$ 的奇/偶 pair；一个独立角散度密度
$(g_B,g_C)$ 应为偶/奇 pair，使 $\partial_\theta g$ 属于
奇/偶 pair。端点物理 $B$、$C$ 也按原奇/偶读取。
真正不具这些对称性的独立输入不属于本篇限制空间，
仍由原全方向定理处理。

## 5. 真实 R119 尾方程、径向参数及弱源的反射

这一部分直接读物理方程，不从 KAM 标签的命名推断对称性。
[实际末端全标签延拓](R119-actual-final-connector-all-label-continuation.md)
119.7--119.10 用原高度相对态 $(P,\mathcal K)$：
$$
 P_t=V-(A_{\rm rad}+1)P,\qquad
 \mathcal K_t=
 { -A_{\rm rad}(2\mathcal K+U+\mathcal K^2+\mathcal K U+w^2P^2)
      +E(V-P)^2\over 1+\mathcal K+EU},
 \quad U=P_\theta,\ V=\mathcal K_\theta .
 \tag{R.12}
$$
此处 $A_{\rm rad}=rw_r/w$ 是径向 profile 系数，和 (R.8) 的
角规范漂移 $A(Q)$ 不同。变换
$(P,\mathcal K)\mapsto(-\mathscr RP,\mathscr R\mathcal K)$
使 $U$ 偶、$V$ 奇；原 $E,J,D$ 偶，$(V-P)^2$ 偶。
所以完整分式与反射等变，所有 mean 小根保原方程。

[控制 profile 全标签图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
C.2--C.4 的两 $\Gamma$ bump、坡平移、形状函数和真实 stop
全部只改变径向数据。其 C.29 后明确由完整解唯一性保持偶反射。
原 C.30--C.31 的参数导数也由同一全图产生，故在同一反射
成员及其相容数据上保持反射。这里不要求某一套中间 FIO/KAM
坐标逐项为偶，也不重选实际 $\Gamma^*$ 或五盒参数。

对相同背景上的物理 Jacobi 高度，记 $\mathscr Rh(t,\theta)
=h(t,-\theta)$。真正散度矩阵满足
$$
 G^{tt},G^{\theta\theta}\ {\rm even},\qquad
 G^{t\theta}=G^{\theta t}\ {\rm odd}.
 \tag{R.13}
$$
因此散度算子与 $\mathscr R$ 交换。对
$Lh=f-\partial_tF^t-\partial_\theta F^\theta$，相容数据恰为
$$
 f,\ F^t\ {\rm even},\qquad F^\theta\ {\rm odd}.
 \tag{R.14}
$$
真实 total 径向通量为偶，它的平均仍可非零；高度 mean
也仍是独立量。flat 条件和固定整体高度 gauge 都保持反射。
实际 $C_R$ 数据为偶、$B_R$ 数据为奇，全部 Robin 与独立 mean
方程照旧。给定原通量兼容和相容的完整端口后，
[Z 完整规范逆](R119-supplement-new-closed-mean-compatibility-gauge-and-complete-fixed-CR-inverse.md)
的唯一性给 $h=\mathscr Rh$。

同样，[K 固定径向源定理](R119-supplement-fixed-radial-root-sources-and-complete-ordinary-C2-inverse.md)
只改变每个相同径向截面的角，$\mu,v,\chi$ 偶、$d$ 奇，
其 $\phi(t,\theta)$、$\Phi(t,\phi)$ 奇。
K.5 的 Piola 变换使 $\bar f,\bar F^t$ 偶，
$\bar F^\phi$ 奇。K.7 的 $u$ 偶、$z$ 奇而 $c$ 为完整 scalar；
K.9 保持这个子类。根能量、真实有序源接线及全部物理 $C^2$
界原样适用；没有删掉 K.9 的 $c$ 或 $u_0$ 方程。

上述是域对称和唯一性结论。任何 metric/两 $\Gamma$ 列还须
满足 K/P 原明确的源 norm 和 weak 端迹条件。径向切口导数、
实际尺度、参考高度和 total-to-bare 通量列不会因反射而消失；
它们只是按各自正确 parity 留在相同方程中。

## 6. 真外端 B mean 在该类准确为零，其余 mean 不消失

[完整四重帽—长图](R133-supplement-complete-fourfold-periodic-cap-long-graph-with-true-B-mean.md)
B.8--B.9 的真实公式是
$$
 B=\chi\,{V-P\over\sqrt D},\qquad
 C=-\chi\,{1+\mathcal K+EU\over\sqrt E\sqrt D},\qquad
 b_0=\chi\left\langle(V-P)(D^{-1/2}-1)\right\rangle .
 \tag{R.15}
$$
在同一实际 even 高度成员，$P,V$ 奇，$\mathcal K,U,D$ 偶，
因此 $B$ 奇、$C$ 偶，并且
$$
               b_0=0,\qquad
 D^k b_0[\text{相容反射方向}]=0\quad(k\ge1).
 \tag{R.16}
$$
完整 nonlinear $C_R\mapsto f_*$、长段 Dirichlet 解和帽固定点
都与相应反射交换；它们的已有唯一性将 even 输入识别为这个
实际反射解。B 篇 §5 的最后一段已明确该识别，故未改变已成
symmetric scientific 成员的身份。一般四重数据的 $b_0$ 仍是
B.9 的非零真实 functional，且其全方向导数仍按 B.17--B.18 收费。

在本篇限制的物理 cap 输入中，独立 $B_0$ source 必须为0，
这是“第一分量为奇”的准确条件；任意非零 $B_0$ 输入仍属原
全方向问题。本篇保留原完整 boundary row，再由 (R.16) 验证
其值。$C_0$ 及其参数/ordinary source 不受 (R.16) 影响。

同样，物理守恒量 $(a^2B_0)'=0$ 在无源反射成员上给 $B_0=0$。
它不是完整腰条件 $B(0,\theta)=0$ 的替代：所有奇的非零模
腰条件仍必须解。Darboux total-flux 兼容、其唯一辅助荷、
mean 高度和 holonomy-one 根也仍完整存在。
这里没有把曲率 $B_0$ 直接改名为 Darboux 通量 mean。

## 7. 原 moving 方程的实际帽—尾估计

在修补中心、固定 $\eta_0,\delta=0$ 上，采用
[S 完整 shifted-Sobolev 桥](R133-supplement-shifted-Sobolev-complete-gauge-Hessian-and-cap-tail-Schur.md)
的同一个真 Green、完整 long $B_0$ 闭合及 residual Hessian。
所有源/jump/端口按第4--6节的实际反射规则限制。
物理算子及 boundary map 交换反射；唯一性使完整 inverse
保持这个闭子空间。故限制不会增大任何原算子范数。

由 (R.10)--(R.11)，S.18--S.24 此时适用于**原**
moving forced operator，而不再需要一个额外的未解规范漂移。
准确保留的安全界为
$$
 \left\|(I-GH_R)^{-1}\right\|_{\mathfrak M_s\to\mathfrak M_s}
       <2^{262145},\qquad -3/2\le s\le1024,
$$
$$
 \|\mathcal C_f^{\rm orig,+}\|_{H^{1/2}\to H^{-3/2}}
       <2^{400000},\qquad
 \|\text{同一完整帽--尾反馈}\|<2^{-31000000}.
 \tag{R.17}
$$
这些均是先前已经支付的严格二进制界，没有新增数值求值。
它们包含真 $C_0$、物理 flux auxiliary charge、完整源/跳和高度
gauge，且继续只在 S 的真实源域使用。moving 输出仍按
$L^\infty_rH^s_\phi$ 读取；没有改成未经证明的
moving $\ell^2\sup_r$ 合成范数。

S 的全方向证明已经付过 $B_0$ feedback，因此在反射子类继续
使用它的较宽常数完全合法；无需为了使用 (R.17) 重算旧帽
kernel、Hessian、已成 finite193 或方向 Gram。

这里给的是已经完成的外帽—尾块在实际存在性子类中的原方程
接口，不是尚未完成的全 mixed inner-body inverse。
也不把 (R.2) 的结构恒等式升级为非零 $\delta$ 的统一定量逆。

## 8. 后续闭合中准确删除的只是一个已证恒零行

今后实际反射构造不必再列“原 moving 的角规范 $A,DA$”
作为一个独立未付反馈：在同一材料角原点，它由 (R.9) 恒为0。
若回到任意全 $4\mathbb Z$ 方向或改变相位输入，则立即恢复
原 G 的完整 scalar phase、$aR_\phi$ 和两端数据。

仍要完成的内容不变：完整 inner/body high 与强返回、充分
cutoff、真实 $\nu$ 响应与两 $\Gamma$ 参数 Schur、可用的
非线性状态空间和小球、全部 physical matching，以及在同一
真闭 $C^2$ 家族上核固定握持区、reach、四静态 marker 和
含反射的可见非刚性。原径向返回相位算术与 (R.8) 的角规范
漂移是不同方程；本篇没有消去前者。

最终公共度量仍须先选定再固定。仅有反射对称也不证明
可见振幅或非刚性，purephase 的 Euclidean 商仍按原几何定义
处理。这里是一条完整接口结论，主课题尚未完成。
