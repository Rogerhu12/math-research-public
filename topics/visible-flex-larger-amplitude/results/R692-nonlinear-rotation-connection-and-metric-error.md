# R692：固定旋转度量的完整非线性连接与无 1/c 的 Gram 误差界

日期：2026-11-26。状态：以下代数、重建和条件误差界已逐式推导；没有新数值运行，没有非圆解的存在声明，没有课题完成声明。

本条使用 [R669](R669-same-g-axisymmetric-tail-linear-uniqueness-and-endpoint-defect.md)、[R671](R671-exact-reference-tail-affine-lift.md)、[R690](R690-quasimonotone-tail-and-deep-valley-input.md) 已登记的准确参考输入，不重证它们的线性唯一性、有限高度表示判据或 deep 输入积分。新增对象是一个完整非线性尾部连接系统，以及由它的连续残差直接控制真实相对 Gram 的积分界。它允许无限材料角谱，不预先固定自由 core。

## 1. 固定输入、方向和适用正则性

在圆柱 $[s_0,S]\times\mathbb R/(2\pi\mathbb Z)$ 上固定

$$
g=ds^2+a(s)^2d\theta^2,\qquad
a>0,\quad a'=b,\quad b^2+c^2=1,
$$

$$
b'=-\kappa c,\qquad c'=\kappa b.
$$

这正是 R669 的 $b=\sin\alpha,c=\cos\alpha$ 约定，不能互换二者。R690 新 deep 输入是一个允许的固定选择。取参考高度 $z_*'=c$，并令

$$
u=b e_r+c e_z,\quad v=e_\theta,\quad
n=u\times v=-c e_r+b e_z.
$$

这里使用 inward 法向，与 R669 明写的 outward 法向相反。因此参考形算子是 $\operatorname{diag}(\kappa,c/a)$。基本导数为

$$
u_s=\kappa n,\quad v_s=0,\quad n_s=-\kappa u,
$$

$$
u_\theta=bv,\quad v_\theta=-bu+cn,\quad n_\theta=-cv.
\tag{1}
$$

以下先对具有所用经典导数的场理解；例如对势取 $\psi\in C^3$、$A\in C^1$，并使参考和连接具有文中所用的连续导数。完备性结论只限于**诱导连接满足这些经典导数条件的准确等距类**；例如 $F\in C^4$ 足够。单独 $F\in C^2$ 只给 $R\in C^1$ 和连续连接，不能无证明升级成经典二阶 Maurer–Cartan 或 $C^3$ 势。本文不宣称覆盖所有低正则 $C^2$ 等距浸入。

固定帽的端口条件为

$$
b(S)=-1,\quad c(S)=\kappa(S)=0.
\tag{2}
$$

下文的帽处 $C^2$ 接合是端口匹配条件，不替代上述内部经典正则性。分片离散表示若需要跨胞适用，必须另付所需导数的接合和连续残差包围。

## 2. 保持度量的旋转标架与完整兼容方程

设 $R(s,\theta)\in SO(3)$，规定

$$
F_s=Ru,\qquad F_\theta=aRv.
\tag{3}
$$

只要二式可积，度量就准确等于固定的 $g$。反过来，每个有向准确等距浸入都由其两个单位切向量和叉积唯一确定这样的 $R$。

用轴向向量定义

$$
R^{-1}R_s=[\Omega_s]_\times,\qquad
R^{-1}R_\theta=[\Omega_\theta]_\times.
$$

由 (1)，位置可积条件只剩

$$
\Omega_\theta\times u=a\Omega_s\times v.
$$

将两个轴向向量在 $(u,v,n)$ 中展开，逐分量比较得到且仅得到

$$
\Omega_s=p u+q v,\qquad
\Omega_\theta=A u-apv.
\tag{4}
$$

不是假定法向旋转分量为零；它是位置可积强制出的条件。旋转场自身的 Maurer–Cartan 条件是

$$
\partial_s\Omega_\theta-\partial_\theta\Omega_s
+\Omega_s\times\Omega_\theta=0.
$$

代入 (1)、(4)，三个分量准确为

$$
A_s-p_\theta+bq=0,
\tag{5a}
$$

$$
ap_s+q_\theta+2bp=0,
\tag{5b}
$$

$$
A(\kappa-q)-cq-ap^2=0.
\tag{5c}
$$

重建面的形算子在 $(Ru,Rv)$ 中是

$$
\mathcal S=\begin{pmatrix}\kappa-q&p\\p&(A+c)/a\end{pmatrix}.
\tag{6}
$$

(5c) 就是 $\det\mathcal S=\kappa c/a=-a''/a$；(5a,b) 是另外两个完整 Codazzi 方程。这些式子没有除以 $c$、$\kappa$、$K$ 或形算子的某个分量。

## 3. 一个周期势和一个标量非线性方程

若帽处 $p=0$，则 (5b) 的角均值给 $\partial_s(a^2\operatorname{mean}p)=0$，因此全段 $\operatorname{mean}p=0$。可以引入周期势，再用其径向均值吸收 $\operatorname{mean}q$，使

$$
p=\frac{\psi_\theta}{a^2},\qquad q=-\frac{\psi_s}{a}.
\tag{7}
$$

此时 (5b) 恒等成立。归一化 $\psi(S,\theta)=0$ 并设 $A(S,\theta)=0$，则 (5a) 等价于线性 Volterra 算子

$$
A[\psi](s,\theta)=\int_S^s
\left(\frac{\psi_{\theta\theta}(r,\theta)}{a(r)^2}
+\frac{b(r)}{a(r)}\psi_s(r,\theta)\right)dr.
\tag{8}
$$

完整非线性 Gauss 方程缩为

$$
\boxed{\mathcal G(\psi)
=a\kappa A[\psi]+(A[\psi]+c)\psi_s
-\frac{\psi_\theta^2}{a^2}=0.}
\tag{9}
$$

这是全非线性等式，不是线性化，也没有只保某个角模或删除均值。$A+c$ 可能趋零或变号，故不将 (9) 强行解成除以 $A+c$ 的显式 IVP。可以直接求隐式边值问题，或保留 $(\psi,A)$ 为两个未知场。

在第1节限定的经典正则性类中，任何与固定平帽准确 $C^2$ 接合的等距浸入都先唯一给出 $R$，再由位置兼容给 (4)，由 (5b) 的帽条件消去 $p$ 的均值，最后给 (7)、(8)。归一化后 $\psi$ 唯一。因此它对**该经典准确等距类**是完整参数化，不是通过冻结旧 q、core 或 H 人为缩小准确解集。它**不是**全部离散近等距 q 场的双射坐标变换；从现有近场切换表示必然是一次显式新场构造。

## 4. 固定帽、闭圈和位置重建

对满足 (8)、(9) 的周期 $\psi$，附加

$$
\psi(S,\theta)=\psi_s(S,\theta)=0.
\tag{10}
$$

先只解正交矩阵的径向 ODE

$$
R_s=R[\Omega_s]_\times,\qquad R(S,\theta)=I,
\tag{11}
$$

再定义

$$
F(s,\theta)=a(S)e_r(\theta)+H e_z+
\int_S^s R(r,\theta)u(r,\theta)\,dr.
\tag{12}
$$

ODE 的反对称系数保证 $R\in SO(3)$。系数和初值均为周期函数，故 $R,F$ 自动周期；不需要另假定位置闭圈。

为核对未隐藏旋转 holonomy，令 $W=R_\theta-R[\Omega_\theta]_\times$。直接微分给

$$
W_s=W[\Omega_s]_\times
-R[\partial_s\Omega_\theta-\partial_\theta\Omega_s
+\Omega_s\times\Omega_\theta]_\times.
\tag{13}
$$

精确 (5) 使第二项为零；(10)、$A(S)=0$ 给 $W(S)=0$。线性 ODE 唯一性给 $W=0$，所以实际 $R_\theta$ 正是规定的连接。又令 $K=F_\theta-aRv$，则由 (4)

$$
K_s=Wu,\qquad K(S)=0.
\tag{14}
$$

故 $K=0$，即 (3) 两式全部成立。由于 $a>0$，$F$ 是浸入。这是圆柱全域的结论，含其非单连通方向；帽处的恒等标架已支付所有圈的旋转与位置周期。

在 (2)、(10) 下，$p=q=A=0$ 于帽边界，(6) 给零二阶法向 jet。位置、切向及二阶 jet 因而与同半径、同高度的平圆盘准确匹配。这给帽处 $C^2$ 接合。它没有证明全表面嵌入、reach 或握持幅度。

## 5. 完整连续残差的二重积分界

更实用地，允许 $(\psi,A)$ 只近似满足 (5)，但保留周期性及 $\psi(S)=\psi_s(S)=A(S)=0$。仍按 (7)、(4)、(11)、(12) 重建真实 $R,F$。定义两个真实连续残差

$$
\mathcal C=A_s-\psi_{\theta\theta}/a^2-(b/a)\psi_s,
$$

$$
\mathcal G=a\kappa A+(A+c)\psi_s-\psi_\theta^2/a^2.
$$

Maurer–Cartan 缺陷恰为

$$
\mathcal D=\mathcal C\,u+(\mathcal G/a)\,n,
\qquad |\mathcal D|=\sqrt{\mathcal C^2+(\mathcal G/a)^2}.
\tag{15}
$$

(13) 的齐次演化只是右乘正交矩阵，左边的 $R$ 也正交；因此算子范数满足

$$
\|W(s,\theta)\|\le\int_s^S |\mathcal D(v,\theta)|dv.
$$

再由 (14) 得

$$
|K(s,\theta)|\le\int_s^S(v-s)|\mathcal D(v,\theta)|dv.
\tag{16}
$$

记右边除以 $a(s)$ 为 $\eta(s,\theta)$。实际 $F_s=Ru$，所以径向误差**准确为零**。其余相对 Gram 分量满足

$$
|F_s\cdot F_\theta/a|\le\eta,\qquad
\big||F_\theta|^2/a^2-1\big|\le2\eta+\eta^2.
$$

因此完整相对 Gram 矩阵的谱误差有上界

$$
\boxed{\frac{2\eta+\eta^2+
\sqrt{(2\eta+\eta^2)^2+4\eta^2}}2.}
\tag{17}
$$

若 $\eta<1$，则 $|F_s\times F_\theta|\ge a(1-\eta)>0$，重建仍为浸入。若 $A$ 直接取 (8)，则 $\mathcal C=0$，(16) 只含 $|\mathcal G(v)|/a(v)$。这没有 $1/c$ 或条件数指数，也不需要 $B\in L^1$。

连续 (15) 的完整包围才能用于 (17)。有限网格最大值不能冒充全域包围，常规浮点旋转 ODE 的误差也必须另付；此处没有把数值 QR 或采样说成准确 $SO(3)$ 演化。

## 6. 完整一阶、二阶变分

保留两个未知场时，对扰动 $(h,k)$ 有

$$
D\mathcal C[h,k]=k_s-h_{\theta\theta}/a^2-(b/a)h_s,
$$

$$
D\mathcal G[h,k]=(a\kappa+\psi_s)k+(A+c)h_s
-2\psi_\theta h_\theta/a^2.
\tag{18}
$$

唯一的二阶项是

$$
D^2\mathcal G[(h,k),(l,m)]
=k l_s+m h_s-2h_\theta l_\theta/a^2.
\tag{19}
$$

对 $ds\,d\theta$ 配对，形式伴随为

$$
J^*(\lambda,\mu)_\psi
=-\lambda_{\theta\theta}/a^2+
\partial_s((b/a)\lambda)-\partial_s((A+c)\mu)
+\partial_\theta(2\psi_\theta\mu/a^2),
$$

$$
J^*(\lambda,\mu)_A=-\lambda_s+(a\kappa+\psi_s)\mu.
\tag{20}
$$

径向边界协向量是

$$
\left[\lambda k+\big(-(b/a)\lambda+(A+c)\mu\big)h\right]_{s_0}^{S}.
\tag{21}
$$

帽端扰动按 (10) 消失；内端不得为省事删除 (21) 或固定全部 core。若消去 $A$，在 (18) 中用 $k=A[h]$，并按 (8) 的真正积分转置返回协向量，不使用未投影的旧 Jacobian。

几何重建也有完整变分。写 $\delta R=R[\xi]_\times$，则

$$
\xi_s=\xi\times\Omega_s+
(h_\theta/a^2)u-(h_s/a)v,\qquad \xi(S)=0,
$$

$$
\delta F(s,\theta)=\delta H e_z+
\int_S^s R(\xi\times u)dr.
\tag{22}
$$

这给实际 core、握持、直径约束的场导数；$A$ 独立变化只影响兼容残差，固定 $\psi$ 的径向重建不变。不能把它误作已付物理几何约束。

## 7. 内圈接合和非平凡性仍须真实支付

若把 $s_0$ 选在具有 $a'(s_0)=0,c(s_0)=1$ 的中圈，以中平面反射补下半面，则应要求真实重建的

$$
R(s_0,\theta)e_z=e_z,\qquad F_z(s_0,\theta)=0.
\tag{23}
$$

精确满足 (5) 时，第一式使 meridian 竖直、core 切向水平；第二式可由一个实际高度平移 $H$ 处理，因为此时第一式使 $F_z$ 沿圈恒定。再从真实 core 曲线求其法向角、支撑函数、凸性及题目固定的三个系数，其余系数继续作为自由度，不把参考圆偷偷代替原非圆 core。全局闭圈由 (12) 已经保证，但简单性、绕数、凸性和三个固定系数没有自动保证。

精确满足 (5) 且 (23) 成立时，$p(s_0,\theta)=0$ 从其角导数推出，而 $A,q$ 可以依角变化；这不意味着 core 为圆。还须保留当前模型的反射、半周对称和真实幅度约束，最后用实际全场认证 embedding、D/L、reach。

对仍有连续兼容残差的近似场，中圈真正必须检查的完整条件是

$$
F_z(s_0,\theta)=0,\qquad F_s(s_0,\theta)=e_z,\qquad
F_{ss,z}(s_0,\theta)=0.
\tag{24}
$$

不能仅由第一条标架条件推断近似场的 $F_z$ 沿圈恒定，因为此时 $F_\theta=aRv+K$ 的 $K_z$ 未必为零。精确径向重建恒有 $F_{ss}=(\kappa-q)Rn$，故在 $b(s_0)=0,c(s_0)=1$ 和准确 $R(s_0,\theta)e_z=e_z$ 下第三式解析成立；数值重建仍应报告其实际误差。(24) 分别给位置、一次反射 jet 和二次反射 jet 匹配。还必须核周期、core 绕数及简单性、全像握持变化和含反射刚体商，不能用圆柱端口闭圈替代这些条件。

旧 q 近场若通过正交化提取 $R$，再通过 Hodge 或势拟合初始化 $\psi,A$，两步均只形成新的候选；全部新场、完整残差和接合缺陷须在真实 Actions 中重新记录，不能继承旧父 metric 或几何证书。

甚至 $\psi\ne0$ 也不足以证明需要的非平凡性。明确反例是

$$
\psi_s=-2a\kappa,\qquad A=-2c,\qquad\psi_\theta=0.
$$

它满足全部精确方程和帽匹配，却只给参考面关于帽平面的镜反射。因此不得用非零势、非零 core 参数或只去普通刚体运动的商来代替题设含反射的整像差及握持见证。材料角依赖和实际全像量必须分别核实。

若最终获得非轴对称完整闭场，R248 的准确相位机制才能产生连续同 $g$ 族；当前条件化重建本身没有提供这样的非圆解。

## 附：一个等能无穷小核圆不能直接补成连续族

设 $X$ 是二维浸入，尝试

$$
X_t=X+\varepsilon(\cos t\,Y+\sin t\,Z).
$$

若 $Y,Z$ 都为 $X$ 的无穷小等距场，并要求 $dY^T dY=dZ^T dZ$、$\operatorname{sym}(dY^T dZ)=0$，令 $A=dX$、$D=dY+i\,dZ$，则

$$
D^T D=0,\qquad A^T D+D^T A=0.
$$

在 $\mathbb C^3$ 非退化双线性点积下，全 isotropic 子空间至多一维。若 $D\ne0$，写它两列为 $\xi_j z$，$z=x+i y$、$z\cdot z=0$。于是非零实向量 $x,y$ 正交且等长。令 $t_j=A_j\cdot z$。第二个矩阵等式给 $\xi_jt_k+\xi_kt_j=0$；选一个 $\xi_j\ne0$，先取 $k=j$ 再取另一个下标，得到所有 $t_k=0$。所以 $A$ 两列都垂直于 $x,y$，从而 $\operatorname{rank}_{\mathbb R}A\le1$，与浸入矛盾。

故处处 $dY=dZ=0$，连通域上只有平移。这只阻断这个特定单谐波仿射核圆；不阻断退化基、更多 $t$ 谐波、完整非线性校正或 R248 机制。不能把该窄判据当作全部闭曲面连续可弯曲性的否定结论。
