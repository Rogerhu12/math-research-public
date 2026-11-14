# R133 补篇：由连续 regular 子空间构造完整 193 态 Green 算子

2026-11-14。**已证明：连续有限 head 的后验逆判据。** 本文给全部 ordinary 源、两端原行及所有接口的同一个 Green 构造。另有同 ac1 的实际有限子空间提案在生成；尚未支付下述连续门，故本文不宣称该 193 态逆已经得到，更不把它当作无穷频主体逆。

新源：[fourfold_codazzi_regular_subspace_proposal.py](../scripts/fourfold_codazzi_regular_subspace_proposal.py)。它保留声明的 193 态矩阵的每个元素、真实均值、全部 96 腰奇行及全部 97 外 mean/Robin 行。无穷 high 的反馈不包含在这个有限提案中，必须在后续全块 Schur 中单独保留。

## 1. 正确的物理 Gram 与一般连续问题

令 $h$ 是实际反射类的物理未规范化 moving 系数，排序为 96 个 sine、1 个 even mean、96 个 cosine。其准确 $L^2_\phi$ Gram 为

$$
W=\operatorname{diag}(\tfrac12 I_{96},1,\tfrac12 I_{96}).
$$

先取 $z=W^{1/2}h$。有限 true head 矩阵为 $A=W^{1/2}(P_{96}D_QF P_{96})W^{-1/2}$。本篇不以数值角采样替代此真正压缩；当前浮点 source 只给它的提案，后续目标/舍入误差属于连续门。

也允许进一步使用任意已支付的连续可逆径向矩阵 $R(r)$：将 $z$ 改为 $Rz$ 时，必须同时改用

$$
A_R=RAR^{-1}+R'R^{-1},\qquad f_R=Rf,
$$

并保两端数据转换与每个真实 jump。若 $R$ 连续，$[z_R]_i=R(r_i)[z]_i$；不允许丢掉 $R'R^{-1}$。这给严格负区使用实际对称度量留出接口，而没有在根处除以零。

以下对同一 Euclidean 坐标中的完整问题

$$
z'=A(r)z+f(r),\quad Uz(0)=g_0,\quad Bz(R)=g_R,
\quad [z]_i=j_i
\tag{G.1}
$$

证明。$A$ 可有已列出的有限跳，普通源取 $L^2_r$，$j_i$ 是独立接口源。$U$ 有 96 行，$B$ 有 97 行；$B$ 包含原物理第四 Robin 和全部 mean，不把其任一行作为自由 scalar 删除。

## 2. 任意完整连续投影与准确分解

取连续、分片 $C^1$ 的正交投影 $P(r)$，秩为 96，置 $Q=I-P$。设

$$
U|_{\operatorname{ran}P(0)}\quad\hbox{和}\quad
B|_{\operatorname{ran}Q(R)}
\tag{G.2}
$$

分别是到完整 96/97 维边界数据空间的双射。记其逆为 $L_U,L_R$，并定义

$$
D_0=L_UU|_{\operatorname{ran}Q(0)},\qquad
D_R=L_RB|_{\operatorname{ran}P(R)}.
\tag{G.3}
$$

$D_R$ 衡量提案与真正外端 regular 核的差；它允许非零，故旧浮点 $q$ 或有限物理积分误差不能通过“初始化为核”被隐去。

写 $x=Pz,y=Qz$。定义完整交叉项

$$
C=PAQ+PP'Q,\qquad E=QAP-QP'P.
\tag{G.4}
$$

由 $P^2=P$ 微分得到 $PP'P=QP'Q=0$，直接对 $Pz,Qz$ 求导可得准确系统

$$
\begin{aligned}
x'&=(PAP+P'P)x+Cy+Pf,\\
y'&=(QAQ-P'Q)y+Ex+Qf.
\end{aligned}
\tag{G.5}
$$

两条齐次生成元分别保持相应移动子空间；法向连接 $P'P,-P'Q$ 对子空间内的范数平方导数没有贡献。

有用的消减是

$$
\boxed{C=2P\operatorname{Sym}(A)Q-E^*.}
\tag{G.6}
$$

因为 $QP'P=QAP-E$，转置即 $PP'Q=PA^*Q-E^*$。因此不必把共同反对称 principal 单独按其大范数付两次；完整 mean 及所有实际非对称余项仍在 (G.6) 中。

## 3. 可积标量界与两个真正连续 Volterra 算子

设在每个真实闭盒已支付

$$
\lambda_{\max}(P\operatorname{Sym}A P|_{\operatorname{ran}P})\le\mu,
\quad
\lambda_{\max}(-Q\operatorname{Sym}A Q|_{\operatorname{ran}Q})\le\nu,
\quad \|C\|\le c,\quad\|E\|\le e.
\tag{G.7}
$$

保留 $\mu,\nu$ 的真实符号，不预先取绝对值。令 $\Phi_P(r,t)$ 是第一子空间的前向齐次演化，$\Phi_Q(r,t)$ 是第二子空间的后向演化。由范数微分、逐片接合，有

$$
\|\Phi_P(r,t)\|\le L_P(r,t)=\exp\!\int_t^r\mu,\quad r\ge t;
$$
$$
\|\Phi_Q(r,t)\|\le L_Q(r,t)=\exp\!\int_r^t\nu,\quad r\le t.
\tag{G.8}
$$

没有沿正型区作整个裸 Cauchy 矩阵的巨大前向传播。两端准确是
$x(0)=L_Ug_0-D_0y(0)$、$y(R)=L_Rg_R-D_Rx(R)$。

于是 (G.5) 与

$$
x=x_f+\mathcal S y,\qquad y=y_f+\mathcal T x
\tag{G.9}
$$

等价，其中

$$
\begin{aligned}
(\mathcal S y)(r)&=-\Phi_P(r,0)D_0y(0)
                  +\int_0^r\Phi_P(r,t)C(t)y(t)\,dt,\\
(\mathcal T x)(r)&=-\Phi_Q(r,R)D_Rx(R)
                  -\int_r^R\Phi_Q(r,t)E(t)x(t)\,dt.
\end{aligned}
\tag{G.10}
$$

后向积分和两个边界反馈的负号均保留。普通与接口数据准确为

$$
\begin{aligned}
x_f(r)={}&\Phi_P(r,0)L_Ug_0+
 \int_0^r\Phi_P(r,t)P(t)f(t)\,dt
 +\sum_{r_i\le r}\Phi_P(r,r_i)P(r_i)j_i,\\
y_f(r)={}&\Phi_Q(r,R)L_Rg_R-
 \int_r^R\Phi_Q(r,t)Q(t)f(t)\,dt
 -\sum_{r<r_i}\Phi_Q(r,r_i)Q(r_i)j_i.
\end{aligned}
\tag{G.11}
$$

用各自正确单侧值解释接口点即可。它们产生准确 $[x]_i=P_i j_i$、$[y]_i=Q_i j_i$，故恢复 (G.1) 的全部独立跳。

在 supremum 径向范数中，实际可消费的上界是

$$
s=\sup_r\left[L_P(r,0)\|D_0\|+
               \int_0^rL_P(r,t)c(t)\,dt\right],
$$
$$
t=\sup_r\left[L_Q(r,R)\|D_R\|+
               \int_r^RL_Q(r,t)e(t)\,dt\right].
\tag{G.12}
$$

所有普通 $L^2$ 源列使用 Cauchy–Schwarz 的准确核费
$(\int L_P^2)^{1/2}$ 和 $(\int L_Q^2)^{1/2}$；所有独立跳列使用 (G.11) 的同一完整核，不删除 mean 跳或改成只给端点输入。

**连续 head 逆判据。** 若 (G.2)、(G.7) 已严格支付，并且 $st<1$，则 (G.1) 对所有完整数据有唯一分片绝对连续解。若 $X_f,Y_f$ 分别界住 (G.11) 的 supremum 范数，则

$$
\|x\|_\infty\le\frac{X_f+sY_f}{1-st},\qquad
\|y\|_\infty\le\frac{Y_f+tX_f}{1-st},
$$
$$
\|z\|_\infty\le
\frac{\sqrt{(X_f+sY_f)^2+(Y_f+tX_f)^2}}{1-st}.
\tag{G.13}
$$

证明：$\mathcal S\mathcal T$ 的范数至多 $st<1$，故第一式有 Neumann 逆；代回得到第二式。差的同一估计证明唯一性。投影的正交性给最后一个平方和界。原连续 ODE 和全部边界、接口由 (G.5)、(G.9) 反向恢复。这是同一个连续数据空间的逆，未用离散条件数代替它。

## 4. 从完整 dyadic Hermite frame 支付投影缺陷

实际提案保存 $193\times96$ frame $X$ 的每个端值及原背景单侧导数。数学验证时使用**准确有理 Hermite 基函数**，端点半径和矩阵值都取存储 double 的准确 dyadic 数，不先将 Hermite 系数再浮点舍入。因此相邻端值的原字节相同就给准确 $X$ 连续；导数允许按原背景接缝有不同单侧值。

若在整闭盒严格有 $G=X^*X\ge gI$、$g>0$，则

$$
P=XG^{-1}X^*
\tag{G.14}
$$

是准确正交投影。对任意完整有限矩阵 $T(r)$，置

$$
\mathcal R_X=X'-AX+XT.
$$

由 $P'X=(I-P)X'$ 得

$$
E X=-(I-P)\mathcal R_X,\qquad
\boxed{\|E\|\le\|\mathcal R_X\|/\sqrt g.}
\tag{G.15}
$$

因此可在同一径向多项式中先做完整消减，而不是分别包住两个大项 $AX$ 和 $X'$。$T$ 不必是真 QR 系数；取由 $X^*AX$ 形成的连续 QR 上三角多项式可改善消减，但任何选择都不改变 (G.15) 的严格性。Gram、真正 $A$ 的目标尾、舍入费、全部矩阵系数、所有径向闭盒都必须实际支付。

在非恒定正度量中先使用第1节的准确坐标变换，再用 (G.14)–(G.15)。这不允许把未加权投影误当成变换后的正交投影。

## 5. 提案算法和当前实际状态

新 source 的外初始化对原完整物理模型 $B$ 的 $97\times97$ even 块求解，以所有 96 个 odd 幅度为独立端口，构成完整 kernel frame；随后按真实 $W$ 正交化。它没有丢弃偶 mean，也没有把第四模变成 free scalar。

在每个原背景 germ 内，两 Gauss 节点的第四阶 Magnus 提案为

$$
\Omega=\frac h2(A_1+A_2)-\frac{\sqrt3h^2}{12}[A_1,A_2],
\qquad X_{\rm next}=\operatorname{qr}(e^\Omega X).
\tag{G.16}
$$

每个完整 segment 后保存全部矩阵。QR 的正对角规范对应
$X'=AX-XT$，其中 $T_{ii}=(X^*AX)_{ii}$、
$T_{ij}=(X^*AX)_{ij}+(X^*AX)_{ji}$ 对 $i<j$，下三角为零；这正是保存单侧导数的规范。

**(G.16) 的浮点阶数和采样误差不被当作证明。** 最终验证只消费它给出的准确 dyadic Hermite 函数及 (G.2)、(G.7)、(G.14)–(G.15)。当前实际首8段已正常 exit 0，域为 $[3.1224999999999996,25/8]$，完整外模型 kernel 残差约 $4.95\cdot10^{-17}$、最大浮点 Gram 残差约 $8.89\cdot10^{-16}$，均只是诊断。全域提案以明确内存上限和64完整 segment 检查点继续；没有以首8段授予全域或连续门。

无穷 high、真正外 DN、完整 moving–physical 残差桥、$\nu$ 与腰幅度 scalar 均保持各自接口。即便以后 (G.13) 对整个193态通过，也还须把全部 high→head→high 反馈加入同一个完整 Schur，才能称为主体全频逆。
