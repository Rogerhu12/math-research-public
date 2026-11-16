# R507：同一完整 ruling 下的真实非正割标量返回回路

日期：2026-11-16。**新的纸面实际构造；未执行 profile 求积、符号程序、数值秩、开发检查或科学任务。**

本稿在 [R505](R505-complete-same-mother-ruling-and-real-nonsecant-local-paths.md) 的同一个新母库、同一个右锚、同一个第二规范与同一个第三规范上继续。R505 已给完整非正割局部路径，但其选定 $h_s>0$ 的正则分支不能在该邻域内返回高度。本稿支付这个具体限制：保完整能量约束的整个速度椭圆后，可以构造正长度真实路径，使 $h,k,\omega$ 三个终值全部准确回到入口，同时整个区间、全部相位的完整第四 ruling 仍为零，且 $k$ 真正非恒。

返回的是三个 scalar 值，不是整个 frame、位置、矩阵 history 或全部端 germs。后面给这些真实未归零增量的准确范围，尤其一个原矩阵坐标有严格负的首项；不会把这一回路冒称为原 $M=0$ prototype。

## 1. 同一个已付背景与本稿的新目标

完全保留 R505 的字面同形母包、真实八／十二／五块布局及三矩。写
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f^2-\phi_\theta^2,\qquad
\Delta=f^2-g^2.
$$
仍只有一个第二规范
$$
w_\theta=-\mathsf A_gD_\theta
$$
和 R505(38)所定义的一个第三 Gram 向量 $\nu$；$\chi_\theta$ 满足
$$
\mathbf I(\phi_\theta,\chi_\theta)=\sin^2\theta\,\nu.
\tag{1}
$$
本稿不改变它们，也不重新选择 profile、参考高度 $H$ 或任何已固定的积分。

一次固定 $y=x+\omega_0$ 记号，并把几何偏移记为
$\varpi=\omega-\omega_0$。于是
$$
z=y+\varpi,\quad e=hz-k,\quad Q=1+e^2,\qquad
\varpi_s=\frac{k_s}{2h}.
\tag{2}
$$
右锚随这次记号变换固定为 $r_*+\omega_0$，以后不随 $s$ 移动。

R505 的完整身份是
$$
\mathscr K(s,\theta)
=-\sin^2\theta\,
\{\mathscr E(h,k,\varpi,\bar{\mathsf m},\gamma,\upsilon)
+2\mathbf w_g(h,k,\varpi)\cdot\nu\},
\tag{3}
$$
$$
\gamma=h_s,\quad\upsilon=k_s,\quad
\bar{\mathsf m}=\mathsf m-\mathsf m_g,\qquad
\mathbf w_g=
\left(\frac{1+(h\varpi-k)^2}{4h},
\frac{h\varpi-k}{2},\frac h4\right).
$$
$\mathscr E=h^{-1}\int|V_{Z_\Delta}'|^2$ 是完整 second 能量。其原有序尾、third 配对及相位身份已经在 R505 全部支付，不能在这里再用只含 principal 的替代式。

固定 R505(39)–(42)的实际入口
$$
X_*=(h_0,0,0,0),\qquad h_0>H,
\tag{4}
$$
其中状态 $X=(h,k,\varpi,\bar{\mathsf m})$ 有 $3+8$ 个真实坐标。正水平速度为 $(\gamma_0,0)$，$\gamma_0>0$。存在性可取 $\mathsf m_g=0$ 从原零历史开始；一般非零实际入值仍须由原前缀提供。

目标是：对充分小而固定的正长度 $\epsilon$，构造一条真路径
$$
h(\epsilon)=h_0,\qquad k(\epsilon)=0,\qquad
\varpi(\epsilon)=0
\tag{5}
$$
并始终满足(3)为零。$\bar{\mathsf m}(\epsilon)$ 不在(5)中，不能由 scalar 返回推断它为零。

## 2. 完整速度二次型在每个合法状态严格正定

原 [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)(29)(30)给
$$
\eta_\Delta=\gamma a_h[\Delta]+\upsilon a_k[\Delta].
\tag{6}
$$
对一个单包 $u$，记 $p=u',r=u'',t=u'''$。直接求原同锚导数，有
$$
\boxed{
a_h[u^2]'=\frac Q{8h^2}(p-zr)t,\qquad
a_k[u^2]'=\frac Q{16h^2}rt.
}
\tag{7}
$$
这里 $k$ 一般不为零；$e=hz-k$、$Q'=2he$ 的各项与原 $J$ 导数准确抵消。(7)没有用 $A_u=0$、局部根代入或单包三矩零。

令
$$
W_\alpha=\left(\frac{a_\alpha}h,\ 0,\
\frac{ea_\alpha}h\right),\qquad \alpha\in\{h,k\},
$$
并定义真实 $2\times2$ Gram
$$
C_{\alpha\beta}(X)=\frac1h\int W_\alpha'\cdot W_\beta'.
\tag{8}
$$
它只依赖当前几何和固定 $\Delta$，不含第二 history。

**引理1。** 对所有 $h>0,z>0$ 的合法几何，$C(X)$ 严格正定。

**证明。** 若一个实向量 $(\alpha,\beta)$ 的二次型为零，则
$(\alpha W_h+\beta W_k)'=0$。其右 collar 为零，所以整个向量为零，特别
$\alpha a_h'+\beta a_k'=0$。

在最右非零微包上，$\Delta$ 是真实非零系数 $R_i$ 乘 $u^2$，没有更右的局部输入。由(7)，
$$
\{\,\alpha p-(\alpha z-\beta/2)r\,\}\,t=0.
$$
记 $\vartheta=\alpha z-\beta/2$、$\ell=\alpha p-\vartheta r$。
因为 $\vartheta'=\alpha$，
$$
\ell'=-\vartheta t,\qquad
(\ell^2)'=-2\vartheta\ell t=0.
$$
平端给 $\ell=0$。若 $\alpha=0,\beta\ne0$，则 $r=0$，再由右 collar 得 $u=0$，矛盾。若 $\alpha\ne0$，在 $\vartheta\ne0$ 的每个区间，
$(p/\vartheta)'=0$。$\vartheta$ 至多有一个零点，每个分支都连到一个 $p=0$ 的外 collar；故 $p=0$，连续性补上可能的单点，仍得 $u=0$。所以只能 $\alpha=\beta=0$。证毕。

这个证明保留整个右端条件，也不需要除以 $u$、$p$ 或 $t$。因此原两速度在完整 second 能量中没有被一个隐藏 profile 零方向合并。

## 3. 一个角控制给完整允许速度椭圆

固定状态 $X$，真正 $q_\Delta=\Phi_{\bar{\mathsf m}}\Delta$ 不随当前速度独立改变。由(6)，完整能量对 $v=(\gamma,\upsilon)^{\mathsf T}$ 恰是
$$
\mathscr E(X,v)=E_0(X)+2b(X)^{\mathsf T}v+
v^{\mathsf T}C(X)v.
\tag{9}
$$
$E_0$ 含完整 normal 项与 $q_\Delta$ 平方，$b$ 含全部真实交叉；本稿不删除它们。定义
$$
\mathcal T(X)=-2\mathbf w_g(X)\cdot\nu,\qquad
v_c=-C^{-1}b,\qquad
\rho^2=\mathcal T-E_0+b^{\mathsf T}C^{-1}b.
\tag{10}
$$

在入口(4)，$q_\Delta=0$，所以 $b=0$，且 R505(42)严格给
$$
\mathcal T(X_*)-E_0(X_*)=\gamma_0^2C_{hh}(X_*)>0.
\tag{11}
$$
取一个足够小的固定状态邻域 $\mathcal U$，便有
$\mathcal T-E_0>0$。于是完整(3)的允许速度集是光滑椭圆
$$
(v-v_c)^{\mathsf T}C(v-v_c)=\rho^2,
\tag{12}
$$
其内部包含原点。不是仅取 R505 的一个 $h_s>0$ 图片；椭圆同时允许正、负的高度速度。

用严格正定矩阵的唯一正平方根，令
$$
v=v_c+\rho C^{-1/2}n,\qquad |n|=1.
\tag{13}
$$
为保持两端原 regular collar，作一次光滑的状态依赖角归一：在每个 $X\in\mathcal U$，椭圆与正水平半轴有唯一横截交点
$v_+(X)=(\gamma_+(X),0)$。它由(9)的正根给出，$\gamma_+>0$，并在入口等于 $\gamma_0$。

令 $n_+(X)=C^{1/2}(v_+-v_c)/\rho$，取其正向正交旋转矩阵 $R_+(X)$，第一列为 $n_+$。最终使用
$$
\boxed{
\mathcal V(X,n)=v_c(X)+\rho(X)C(X)^{-1/2}R_+(X)n,
\qquad |n|=1 .
}
\tag{14}
$$
当 $n=e_1$ 时，实际 $\upsilon=0$，不是只在冻结状态上的零值。

在入口定义
$$
A=\rho(X_*)C(X_*)^{-1/2}R_+(X_*).
\tag{15}
$$
它可逆、$\det A>0$，且 $Ae_1=(\gamma_0,0)$。因此在冻结入口上，允许速度恰为 $An$，而不是任意另加幅度的两输入控制。

实际 ODE 为
$$
\boxed{
\begin{aligned}
(h_s,k_s)^{\mathsf T}&=\mathcal V(X,n(s)),\\
\varpi_s&=\frac{\mathcal V_2(X,n(s))}{2h},\\
\bar{\mathsf m}_s
&=M_{\rm raw}\bigl(h,k,\varpi,\mathcal V_1,\mathcal V_2\bigr).
\end{aligned}}
\tag{16}
$$
由构造，它逐点严格满足完整(3)。原 frame、位置和全部 Taylor history 继续按原式恢复，未成为可自由指定的附加控制。

## 4. 一个严格光滑、零有向面积的单位速基线

本节只构造一个固定平面控制曲线，不执行轨迹实验或函数秩计算。

从
$$
q_{\rm G}(t)=(\sin2\pi t,\ \sin4\pi t),\qquad 0\le t\le1
\tag{17}
$$
开始。其导数从不为零：若 $\cos2\pi t=0$，则 $\cos4\pi t=-1$。它满足
$q_{\rm G}(1-t)=-q_{\rm G}(t)$，所以闭合且有向面积为零。它经过原点时有不平行的真实切线，因而不在任何圆上。

还可使它在两端完全直线，而不失这些性质。在足够短的左邻域把
$q_{\rm G}(t)$ 改为 $q_{\rm G}'(0)t$，用固定光滑 cutoff 接回；差为 $O(t^3)$，导数差为 $O(t^2)$，故小邻域中仍正则。右端按
$q(1-t)=-q(t)$ 同步定义。两端各阶 germs 匹配，有向面积仍严格为零；中部不平行交叉保留。

旋转使初始切向为 $e_1$，再按总弧长缩放并作弧长参数化，得到一条固定
$$
q:[0,1]\to\mathbb R^2,\qquad
q(0)=q(1)=0,\quad |q'|=1,
$$
$$
q'=e_1\text{ 于两端 collar},\qquad
\int_0^1q_1q_2'\,dt=0,
\tag{18}
$$
且 $q$ 不在任何圆或直线上。弧长参数化保闭合、有向面积和两端直线；缩放后的总长度恰为一。以下记 $n_0=q'$。

这条“8”字只在标量控制平面中使用；它不是对最终曲面自交或嵌入作任何断言。

## 5. 三个真实内支撑角方向有满三行端点导数

取三个待选的实 $C_c^\infty((0,1))$ 函数 $\psi_j$，并置
$$
n_z(t)=\operatorname{Rot}\!\left(\sum_{j=1}^3z_j\psi_j(t)\right)n_0(t).
\tag{19}
$$
始终 $|n_z|=1$，且两端仍准确 $n_z=e_1$。记 $J_2$ 为平面正九十度旋转，则
$\partial_{z_j}n_z|_0=J_2n_0\,\psi_j$。

考虑冻结入口平面速度 $An_z$，其累计为
$$
(H_z(t),K_z(t))^{\mathsf T}=A\int_0^t n_z(\tau)\,d\tau.
$$
在 $z=0$，两终值为零，有向面积也为零。其三个一阶端点函数是
$$
A\int_0^1J_2n_0\,\psi,\qquad
\det A\int_0^1 q\cdot n_0\,\psi.
\tag{20}
$$
最后一项是 $\int H_zK_z'$ 的微分。完整证明是：在闭合基点，
$$
\delta\!\left(\frac12\int\det(q,q')\right)
=\int\det(q,\delta q')
=\int q\cdot n_0\,\psi;
$$
端点项因为 $q(0)=q(1)=0$ 准确为零。乘可逆 $A$ 后，非反对称的端点二次项在此基点也只有零一导，故因子正是 $\det A$。

三条函数
$$
(J_2n_0)_1,\qquad (J_2n_0)_2,\qquad q\cdot n_0
\tag{21}
$$
线性独立。若末函数是前两条的常系数组合，就有一个固定点 $c$ 使
$(q-c)\cdot q'=0$；于是 $|q-c|^2$ 恒定，迫整条曲线在一个圆上，和(18)矛盾。若末项系数为零，则变化的切向不共线直接迫前两系数为零。

所以可以选三个真实内点及小支撑光滑 $\psi_j$，使(20)的 $3\times3$ 矩阵可逆。理由是(21)的点值向量张成 $\mathbb R^3$；在三个张成点附近取归一化紧 bumps，其积分矩阵连续接近该可逆点值矩阵。选定一次充分小的有限支撑后便有严格非零 determinant。这里没有执行点选、数值求积或 rank 程序，也没有把一个未证 generic rank 当成假设。

## 6. 有限正长度 IFT 支付原水平关系的三个真实终值

现在用真实(16)，令
$$
n(s)=n_z(s/\epsilon),\qquad 0\le s\le\epsilon,
\tag{22}
$$
初值固定为 $X_*$。取足够小的 $\epsilon>0$ 和固定小 $z$ 盒，解始终在 $\mathcal U$，故完整 ruling 保持为零。

写真实终点偏差为 $\Delta h,\Delta k,\Delta\varpi$，定义
$$
\mathcal F(\epsilon,z)=
\left(
\frac{\Delta h}{\epsilon},\
\frac{\Delta k}{\epsilon},\
\frac{\Delta\varpi-\Delta k/(2h_0)}{\epsilon^2}
\right).
\tag{23}
$$
该归一并未改原几何条件。原水平式准确给
$$
\Delta\varpi-\frac{\Delta k}{2h_0}
=\int_0^\epsilon
k_s\left(\frac1{2h}-\frac1{2h_0}\right)ds.
\tag{24}
$$
因此最后一个分量真实含两个 $\epsilon$ 因子。

将原时间改写为 $t=s/\epsilon$，(16)成为
$X_t=\epsilon F(X,n_z(t))$。普通光滑 ODE 参数依赖及(24)给 $\mathcal F$ 在 $\epsilon=0$ 的 $C^1$ 延拓，准确为
$$
\boxed{
\mathcal F(0,z)=
\left(
H_z(1),\
K_z(1),\
-\frac1{2h_0^2}\int_0^1H_zK_z'\,dt
\right).
}
\tag{25}
$$
$\bar{\mathsf m}$ 的真实变化、椭圆中心和形状的变化都在这一原 ODE 中保留；它们对(25)的误差为 $O(\epsilon)$，不是被设成零。

由(18)，$\mathcal F(0,0)=0$。由(20)(21)，
$D_z\mathcal F(0,0)$ 可逆。有限维 IFT 遂给一个真实小参数 $z(\epsilon)\to0$，使每一个充分小、正而有限的 $\epsilon$ 上
$$
\mathcal F(\epsilon,z(\epsilon))=0.
$$
这正是原终点条件(5)，没有用首项近似代替准确根。

**定理。** 在 R505 的同一个母库、同一个 $w_\theta,\chi_\theta$ 和正规入口上，存在任意充分短的实际光滑正长度路径，同时满足
$$
\boxed{
h(\epsilon)=h_0,\quad k(\epsilon)=0,\quad\omega(\epsilon)=\omega_0,
\qquad \mathscr K(s,\theta)=0\text{ 对全部 }s,\theta.
}
\tag{26}
$$
其 $k$ 非恒。因为冻结首项为
$(h-h_0,k)=\epsilon A q(t)+O(\epsilon^2)$，而 $Aq$ 的第二分量不恒零；选择其一个非零点，有限小 $\epsilon$ 保此真实非零值。故该路径不是一条正割段或其参数重复。

两端(19)准确为 $n=e_1$，由(14)得真实 $k_s=\omega_s=0$ 的共同 regular collars，且 $h_s=\gamma_+(X)>0$。高度在全段返回而两端高度速度正，故其内部确实经过负高度速度区间。整个构造使用完整速度椭圆；不可能由 R505 的单一 $h_s>0$ 图片独自得到。

## 7. 原历史、frame、位置和两端 germs 的真实账不能省略

定理(26)不是 $M=0$ 返回块。一个具体原坐标已经说明这一点。

在入口 $k=\varpi=0$，原 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(6)(10)给任意实际两速度下
$$
(M_{\rm raw})_{t_1}
=-\frac18\left(1+\frac{\gamma^2}{h_0^2}\right).
\tag{27}
$$
$\upsilon$ 出现在该处的其它坐标中，不改变这个 $y$ 线性系数。沿本稿短路径，状态变化为 $O(\epsilon)$，所以在固定 $y$ 八矩坐标中
$$
\boxed{
(\mathsf m(\epsilon)-\mathsf m_g)_{t_1}
=-\frac{\epsilon}{8}
\left\{1+\frac1{h_0^2}
\int_0^1[(An_0(t))_1]^2dt\right\}
+O(\epsilon^2)<0.
}
\tag{28}
$$
本稿没有执行该积分；正的常数1已足以给严格号。可把它看成这条真实 scalar-return 单元必须交给后继矩阵桥的一个已知非零成本，而非将它当作精确零或可忽略量。

同样，由 $k=O(\epsilon)$，
$$
F(\epsilon)=F(0)\{I+\epsilon\Omega(0)+O(\epsilon^2)\},
\qquad
\alpha(\epsilon)-\alpha(0)
=\epsilon h_0^2T(0)+O(\epsilon^2).
\tag{29}
$$
因此 frame 和位置也没有随(26)自动返回。完整第三、第四原函数按 R56/R73 的实际恢复计算；控制随 $s/\epsilon$ 变化，较高几何导数可以随 $\epsilon$ 缩短而变大。对每个已经选定的正 $\epsilon$ 它们光滑有限，但不能由 $\mathsf m$ 的 $O(\epsilon)$ 推出全部 $T,V$ 小，更不能把这些基准删除。

两端 scalar **值** 相同，两端完整 scalar/history germs 则由各自实际状态决定。虽然两端都在 $k_s=0$ 的同一 regular 分支，终端 $\bar{\mathsf m}$ 已改变，故 $\gamma_+(X_{\rm end})$ 一般不等于入口 $\gamma_0$。把这些端口接入原固定词时，必须匹配各自真实 germs；本稿不声称已经构造了常 scalar collar 或相同全 germ 的闭环。

R505 §10 的有限端点纤维仍可在本稿三个精确终值纤维内使用。具体地，先加入更多有限个内支撑角参数，保第5节三个可逆方向作正常列；同一 IFT 先准确解(26)，余参数仍为真实允许控制。然后才把额外端传递数据纳入同一个有限映射，选择其真实最大秩点。参数数目预先超过该有限终点表的维数，便可得到保已有端数据的非平凡纤维。它不能强迫(28)变成零；不以常秩定理替代未达目标的基线。

## 8. 已获得的正向用途与剩余全词问题

本稿把 R505 的局部正则路径推进为一个真实返回单元：其 $h,k,\omega$ 三个终值精确闭合、曲率非恒、完整第四 ruling 全段全相位为零，并始终使用同一实际母库和同一规范。这个结果不来自原 R70 无 ruling 限制桥，也不是逐点拟合两个加速度。

仍需处理的是这些单元的实际矩阵、frame、位置和完整高阶传递。在当前小邻域，(28)甚至显示原 $t_1$ 坐标的一侧漂移；要形成原 $M=0$、指定第三算子和全周期词，必须有其它真实受约束段提供相应端点控制。对参考正割入口的连接、同一个十三行、全第四 period 和原 Klein 基准，本稿没有给未付的消去。

本稿也没有改变 R505 的 profile 范围：它是从起点选择的字面同形库，不能移植为旧冻结不同母十九／二十目标已经兼容。基几何随真实控制改变，所得仍是理论基带构造；不把它当作已冻结固定度量数值曲面的零成本修正，更不声称主课题的有限等距族、嵌入或厚度门已经完成。

新闭合部分是实际可用的非正割 scalar-return 控制，以及它的完整原历史和端口账。全部公式以上述原式为证，没有新增科学执行。
