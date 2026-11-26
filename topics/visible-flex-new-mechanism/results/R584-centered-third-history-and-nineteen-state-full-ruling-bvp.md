# R584：完整 ruling 的中心化第三坐标与真正十九态八端边值问题

日期：2026-11-26。**已证明；原式纸证与准确实现接口；未执行新的符号、求积、ODE、优化或秩计算。**

本文承接 R530、R578、R581。新步骤是把完整 ruling 中的实际 $A$ 线性项、$A^2$ 能量和第三历史准确合到一个可逆的第三状态坐标中，使当前 ruling 的读出只需 R581 的 C² 局部项和六个真实累计坐标。这个变换不删除任何记忆，不需要 R480 的 outer 零条件，也不增加第三控制。

随后将 R530 的冗余双边第二累计准确减到一份八维量，得到十九态系统；固定有限 $H,L$ 时，八矩返回等价于一个明确的 22 条边值问题。22 是方程数，**不是端图满秩或有限根存在的结论**。完整历史导数的稳定预收、实际有限根、端 germs、第四 period 和主几何目标仍须继续。

## 1. 固定同一个模型及原完整读出

固定 R521 或 R578 的一份实际完整库、同一个 $y=x+\omega_c$ 坐标、所有副本位置和原右锚。本文不把原 R521 路径与新 R578 库拼接。取 $\phi=g$、$\Delta=f\odot f-g\odot g$，在原八基 $E_\alpha$ 下写第二累计为向量 $A=(A_\alpha)_{\alpha=1}^8$；其固定 profile 为
$$
q_A=\Phi_A\Delta.
\tag{1}
$$
坐标顺序始终是
$$
(p_0,p_1,p_2,t_1,r_1,s_1,s_0,r_0).
\tag{2}
$$
原完整第三算子记为 $T$，其 ruling 真投影为
$$
t_j=I_{j,y}\{g,T(g;\Delta)\},\qquad j=0,1,2.
\tag{3}
$$
这里只用三投影使几何方程闭合。它们不是三个可独立指定的第三 profiles；完整 $T$ 在所得轨道上仍按 R73 原方程恢复。

置
$$
S=(h,k,\eta),\quad v=(\gamma,\upsilon)=(h_s,k_s),\quad
d_g=h\eta-k,
$$
$$
w(S)=\left(\frac{1+d_g^2}{4h},\frac{d_g}2,\frac h4\right),
\qquad w_0(S)>0.
\tag{4}
$$
规范参数 $\nu\in\mathbb R^3$ 在整段固定一次。R482 **未消历史**的 (24)给
$$
\mathscr K=
\mathscr R(S,v,a,b)+\mathscr L(S,v;A)
-w(S)\cdot G[A,A]-4w(S)\cdot t-2w(S)\cdot\nu,
\tag{5}
$$
其中
$$
G_j[A,B]=I_{j,y}(q_A,q_B).
\tag{6}
$$
$G_j$ 是固定的对称八维双线性型；其系数只由同一实际 profiles 与右锚确定。$\mathscr R$ 是 R581 已保完整原 $M_{\rm raw}$ chain 的局部项，准确对 $(a,b)$ 仿射，其系数为 R521 的 $C_h,C_k$。

由 R221 原式 (17)(18)，$\mathscr L$ 对当前八矩一次、对速度一次：
$$
\mathscr L(S,v;A)=\lambda(S,v)\cdot A,\qquad
\lambda(S,v)=\gamma\lambda_h(S)+\upsilon\lambda_k(S).
\tag{7}
$$
$\lambda_h,\lambda_k$ 为固定有限 profile 积分的光滑几何系数。它们不是另取的响应控制。R221 的右尾转置项及 $q_A$ 的真尾全部包含在 (7)中。

## 2. 可逆的第三状态变换

令 $e^{(0)}=(1,0,0)$，定义
$$
r(S,v,A)=\frac14G[A,A]
-e^{(0)}\frac{\mathscr L(S,v;A)}{4w_0(S)}.
\tag{8}
$$
这里 $r$ 是三维真实坐标函数，不是 profile 的空间原函数。

直接计算
$$
4w\cdot r=w\cdot G[A,A]-\mathscr L.
$$
所以在任意合法当前状态上，置 $\tau=t+r$ 后有准确等式
$$
\boxed{\mathscr K=\mathscr R-4w\cdot\tau-2w\cdot\nu.}
\tag{9}
$$
对固定 $(S,v,A)$，$t\mapsto\tau=t+r$ 是平移，逆为 $t=\tau-r$，不存在退化 Jacobian。$w_0=(1+d_g^2)/(4h)$ 在 $h>0$ 恒正；在任何固定合法紧盒上，它及其逆均有界。

(9)没有声称原 $A$ 能量消失，也没有把大历史置零。该能量及线性项现在准确存入第三状态中；在当前 ruling 读出时，无须再以一个独立算出的 $-wG[A,A]$ 与一个独立大第三累计相减。

### 2.1 完整导数及原有序项

定义固定有序张量
$$
B_{j,\alpha\beta}
=I_{j,y}\{g,\Phi_{E_\alpha}(g,\Phi_{E_\beta}\Delta)\}.
\tag{10}
$$
注意 $\alpha,\beta$ 有序，不将 $B$ 先对称化。令
$$
M=M_{\rm raw}(S,v),\qquad
c_j(S,v,a,b)=I_{j,y}\{g,\mathcal C_s(g;\Delta)\}.
\tag{11}
$$
这里 $\mathcal C_s$ 是 R73(16)的完整局部第三密度，保原变化-profile chain，且对真实 $(a,b)$ 至多仿射。原方程为
$$
A_s=M,\qquad t_s=c-B[M,A].
\tag{12}
$$
从 (8)准确微分，得到
$$
\boxed{
\tau_s=
c-B[M,A]+\frac12G[M,A]
-e^{(0)}D_s\!\left(\frac{\lambda\cdot A}{4w_0}\right).}
\tag{13}
$$
其中
$$
D_s\!\left(\frac{\lambda\cdot A}{4w_0}\right)
=\frac{\dot\lambda\cdot A+\lambda\cdot M}{4w_0}
-\frac{(\lambda\cdot A)\dot w_0}{4w_0^2},
\tag{14}
$$
$$
\dot\lambda=
\partial_h\lambda\,\gamma+\partial_k\lambda\,\upsilon
+\partial_\eta\lambda\,\frac{\upsilon}{2h}
+\partial_\gamma\lambda\,a+\partial_\upsilon\lambda\,b,
\tag{15}
$$
$$
\dot w_0=
\frac{d_g(\gamma\eta-\upsilon/2)}{2h}
-\frac{\gamma(1+d_g^2)}{4h^2}.
\tag{16}
$$
(7)说明 (15)至多仿射依赖 $a,b$；没有 $h_{sss},k_{sss}$，也没有 $A_{ss}$。因此将原两加速度方程代入 (13)后，仍是通常的有限维光滑 ODE。

可以把固定有序张量先写为
$$
D_{j,\alpha\beta}=\tfrac12G_{j,\alpha\beta}-B_{j,\alpha\beta},
\tag{17}
$$
但实现应对其原被积式先准确合并后求积，不能只以两个巨大、不充分收敛的已求积张量相减来声称稳定。

## 3. 同一个中心平移与同一个固定第三规范

采用 R530 中心初值
$$
h(0)=H,\quad k(0)=\eta(0)=\gamma(0)=0,\quad
\upsilon(0)=v_0,
$$
$$
A_+(0)=A_-(0)=A_{\rm o}\in E_{\rm o},\qquad
t_+(0)=t_-(0)=0,
\tag{18}
$$
其中
$$
E_{\rm o}=\operatorname{span}(p_0,p_2,r_0,s_1).
$$
正、负侧在中心的**实际**几何与速度都为
$(H,0,0,0,v_0)$；两侧 $A$ 也相同。故
$$
r_{\rm c}=r(H,0,0,0,v_0,A_{\rm o})
\tag{19}
$$
为两侧共用的同一个三向量。

对整份候选路径定义一次
$$
\boxed{\sigma_\pm=\tau_\pm-r_{\rm c},\qquad
\bar\nu=\nu+2r_{\rm c}.}
\tag{20}
$$
$r_{\rm c}$ 随所选候选的中心控制改变，但在该条路径上不随时间改变。因此
$$
\sigma_+(0)=\sigma_-(0)=0,
$$
$$
\boxed{\mathscr K_\pm=\mathscr R_\pm
-4w_\pm\cdot\sigma_\pm-2w_\pm\cdot\bar\nu.}
\tag{21}
$$
两条式子使用同一个 $\bar\nu$。这里不是给正、负两侧各选一条第三规范。

### 3.1 对未知控制的确切可逆性

固定 $H$，原射击参数为
$$
(v_0,A_{\rm o},\nu)\in\mathbb R^{1+4+3}.
$$
(19)只依赖 $H,v_0,A_{\rm o}$，**不依赖 $\nu$**：$G$ 固定，$\lambda$ 只读一阶几何 jet，(8)没有加速度。因此参数替换
$$
(v_0,A_{\rm o},\nu)
\longmapsto(v_0,A_{\rm o},\bar\nu=\nu+2r_{\rm c})
\tag{22}
$$
有全局准确逆
$$
\nu=\bar\nu-2r_{\rm c}(H,v_0,A_{\rm o}).
\tag{23}
$$
其 Jacobian 为分块三角矩阵，对角是 $I_5,I_3$，行列式为1。若 $H$ 也作为参数，把它保在前块，结论不变。

这只证明**坐标变换**可逆，不能由此推八个实际末端响应满秩。两套射击端图由 (22)互相复合，所以它们的真实 rank 完全相同；原来尚未证明的 rank 没有凭空获得。

选定一条候选后，恢复 (23)并采用 R530 的一条固定 $\chi^\nu$。$\bar\nu$ 或 $\nu$ 都不被当作时间函数。搜索不同候选时规范参数可以不同，最终得到的实际段则始终只使用所选的一个规范。

## 4. 第二累计的八维冗余可以准确删除

按 (2)定义固定对角 involution
$$
J=\operatorname{diag}(1,-1,1,-1,-1,1,-1,1).
\tag{24}
$$
正侧几何与速度为
$$
S_+=(h,k,\eta),\quad v_+=(\gamma,\upsilon),
$$
负侧按实际时间 $-s$ 读取
$$
S_-=(h,-k,-\eta),\quad v_-=(-\gamma,\upsilon).
\tag{25}
$$
R530(23)(24)的原八矩奇偶给
$$
M_-=-JM_+.
\tag{26}
$$
负侧以正变量 $s$ 记录，所以 $(A_-)_s=-M_-$。由 (18)，$JA_{\rm o}=A_{\rm o}$，故
$$
\boxed{A_-(s)=JA_+(s)}
\tag{27}
$$
在任何实际存在区间都准确成立。证明只是两边导数相同、初值相同；不涉及 profiles 的空间反射。

不能对 $\sigma_-$ 作类似的未经证明压缩。完整第三投影的两侧仍有各自的 $c_\pm,B[M_\pm,A_\pm]$ 与真实符号，六个坐标全部保留。

## 5. 真正十九态 ODE

取状态
$$
X=(h,k,\eta,\gamma,\upsilon,A,\sigma_+,\sigma_-)
\in\mathbb R^{5+8+3+3},
\qquad A=A_+.
\tag{28}
$$
记
$$
R_+^0=\mathscr R(S_+,v_+,0,0),\qquad
R_-^0=\mathscr R(S_-,v_-,0,0).
$$
R581 给两者的准确 C² 局部表达，保原 $M_{\rm raw}$ chain。实际加速度由
$$
\begin{pmatrix}
C_h(S_+)&C_k(S_+)\\
C_h(S_-)&-C_k(S_-)
\end{pmatrix}
\binom a b
=-\binom{R_+^0-4w_+\cdot\sigma_+-2w_+\cdot\bar\nu}
{R_-^0-4w_-\cdot\sigma_--2w_-\cdot\bar\nu}.
\tag{29}
$$
仍是原 R530 的正行列式，未因状态替换改变两个加速度系数。

令 $\mathcal H(S,v,a,b,A)$ 表示 (13)右侧。完整状态方程为
$$
h_s=\gamma,\quad k_s=\upsilon,\quad
\eta_s=\upsilon/(2h),\quad
\gamma_s=a,\quad\upsilon_s=b,\quad A_s=M_+,
$$
$$
\boxed{
(\sigma_+)_s=\mathcal H(S_+,v_+,a,b,A),\qquad
(\sigma_-)_s=-\mathcal H(S_-,v_-,a,-b,JA).}
\tag{30}
$$
负侧是**整个**原物理导数反号；不是仅给有序 $B$ 项或某个矩阵项改号。

在共同合法紧域
$$
h>0,\quad y\pm\eta>0,\quad h(y\pm\eta)\mp k>0,\quad
h^2(y\pm\eta)^2>1+k^2
\tag{31}
$$
及有限速度、历史盒内，(29)行列式有正下界，$w_0$ 有正下界，所有右侧光滑。故 (28)–(30)给通常的真实局部解并按标准有限状态准则延拓。它不因此保证任意给定的有限长度都留在该盒。

### 完整等价性

由任一原 R530 解，(8)(20)(27)直接给 (28)–(30)。反过来，给 (28)–(30)及中心条件，先按 (19)(23)恢复固定 $\nu$，再定义
$$
t_\pm=\sigma_\pm-r(S_\pm,v_\pm,A_\pm)+r_{\rm c}.
\tag{32}
$$
用 (13)(30)微分，准确恢复两侧 R73 投影方程及 $t_\pm(0)=0$。在同一所得几何上按 R73 恢复完整 $T_\pm$，取真实中心 $T_\pm(0)=0$；其三个投影因同一个 ODE 和初值而就是 (32)。R530 的中心规范与反向累计解释因此原样保留。

(21)(29)给整段全部相位的原完整 ruling 为零。没有在恢复完整 $T$ 后另发现一个未解第三 forcing；但完整第三**端值**与第四 period 仍是输出。

## 6. 固定有限 $H,L$ 的八端边值问题

先固定 $H>0,L>0$ 和一份 (31)共同域。将 $s=Lx$、$0\le x\le1$，方程为 $X_x=L\mathcal F(X;\bar\nu)$。三个未知参数是恒定 $\bar\nu\in\mathbb R^3$。

中心条件为
$$
h(0)=H,\quad k(0)=\eta(0)=\gamma(0)=0
\quad(4\text{ 条}),
$$
$$
\operatorname{pr}_{E_{\rm e}}A(0)=0
\quad(4\text{ 条}),\qquad
\sigma_+(0)=\sigma_-(0)=0
\quad(6\text{ 条}),
\tag{33}
$$
其中 $E_{\rm e}=(p_1,t_1,r_1,s_0)$。末端条件是
$$
\boxed{A(1)=0\quad(8\text{ 条}).}
\tag{34}
$$
总共 $14+8=22=19+3$ 条。中心的 $\upsilon(0)$ 与四个奇累计仍是自由未知；连同 $\bar\nu$，恰对应原八个射击控制。末端八式保留共同奇入值与四偶目标，未只消总矩阵的四个偶坐标。

**等价命题。** 对固定库、$H,L$，任何保持 (31)的光滑 (33)(34)解，经 (23)(32)恢复后是一条原 R530 的实际双边完整 ruling 解，且两个中心累计末值都为零。反之，任何满足这些原中心、末端条件的 R530 解给该 BVP 的解。

证明由第5节等价性及 (27)立即得到。命题没有断言其解集非空。$L>0$ 被事先固定，避免把零长度当成八矩返回。特别 $k\equiv0$ 时原 $M_{t_1}=-(1+(\gamma/h)^2)/8<0$，所以任何真正满足 (34)的正长度解自动不是 $k\equiv0$ 的平凡路径。

若用 collocation 或多重射击求解，必须把完整 (30)、连续共同域和 (34)一起精化；有限节点残差零本身不是这个命题的精确解。端 Jacobian 的 rank 也须由同一实际解另证或实际评价，不能由方程数得到。

## 7. 真实左端重锚及端口读出

若 (34)成立，则 R530 的真实左端第二入值
$$
B=A_-(L)=0.
$$
从真实左端采用零历史，最终第二规范为 $w_\theta=0$，第三规范固定为
$$
\chi_\theta=\chi_\theta^\nu+
2T_-(L)(\phi_\theta;\Delta_\theta).
\tag{35}
$$
R530 已证明它真紧、保两个 seed、相位光滑周期，并使重锚前后的实际字段完全一致。本稿不重新给每个子段选规范。

由于 $A_\pm(L)=0$，(8)在两个末端给 $r_\pm(L)=0$。故
$$
t_\pm(L)=\sigma_\pm(L)+r_{\rm c}.
\tag{36}
$$
完整第三总响应的三个投影准确是
$$
\boxed{
I_j\{g,T_{\rm tot}(g;\Delta)\}
=(\sigma_+(L)-\sigma_-(L))_j.}
\tag{37}
$$
最终 (35)第三规范的三 Gram 参数则是
$$
\boxed{\nu+2t_-(L)=\bar\nu+2\sigma_-(L).}
\tag{38}
$$
这保留未知中心控制产生的 $r_{\rm c}$，并显示它在真正重锚公式中准确抵消。不能由 (37)的三个数为零推完整 $T_{\rm tot}=0$，更不能推第四 period 为零。

## 8. 有限合法盒与整个空间范围

R578 的实际窗口可从起点取 $y\in[4,6]$。一个具体有限盒是
$$
4/5\le h\le3,\qquad |k|\le2,\qquad|\eta|\le1.
\tag{39}
$$
在这个盒上
$$
y\pm\eta\ge3,\qquad
h(y\pm\eta)\mp k\ge2/5,
$$
$$
h^2(y\pm\eta)^2-1-k^2
\ge144/25-5=19/25>0.
\tag{40}
$$
所以它确属 R530 的共同严格域。这里没有把 R528 的另一个 Möbius 无极点条件 $1-ke\ne0$ 混入 (40)。速度和历史仍需独立有限界；没有声称一个未知 BVP 根会自动留在 (39)。

给实际解，另按原方程积分正半 frame 与位置
$$
F_s=F\Omega(k),\qquad \alpha_s=h^2Fe_1,\qquad
F(0)=I,\quad\alpha(0)=0.
\tag{41}
$$
令 $D_B=\operatorname{diag}(-1,-1,1)$、$N=Fe_2$。R530 的准确中心几何对称给整个基底
$$
X_+(s,y)=\alpha(s)+\frac{h(s)}{y+\eta(s)}N(s),
$$
$$
X_-(-s,y)=D_B\left\{\alpha(s)-\frac{h(s)}{y-\eta(s)}N(s)\right\}.
\tag{42}
$$
因此不只读 $\alpha(L)$；必须把全部 $s\in[0,L]$ 的 (42)纳入空间范围。

对球心 $ce_3$，$D_B$ 保球心，且固定 $s$ 的距离平方是 $u=h/(y\pm\eta)$ 的凸二次式。因此全材料窗口的最大距离精确落在四条 $y=4,6$ 边界曲线上。对这四条曲线取全程连续上界即可给基底包围球，不需在 $y$ 方向虚拟稠密点云。

粗略地，(39)给 $|h/(y\pm\eta)|\le1$、$|\alpha(s)|\le9L$，故基底直径不超过 $2(9L+1)$。此界只说明该有限输入允许同时控制整个空间范围；它不是 reach 下界，也没有支付闭合帽、全部 phase、嵌入或握持幅度。

### 可供后续联解的两个实际 pose 条件

令 $n=N(L)$、$v=\alpha(L)$。由 (41)的中心对称，真实段起终轴为
$$
N(-L)=-D_Bn=(n_x,n_y,-n_z),\qquad N(L)=n,
$$
且位置差为 $(I-D_B)v=(2v_x,2v_y,0)$。
R570 的两半周转轴相交且正交条件在此准确写成
$$
\boxed{n_z^2=1/2,\qquad v_xn_y-v_yn_x=0.}
\tag{43}
$$
前式使两轴正交；后式使其共面，从而两条非平行轴相交。这是**已有实际末点**的准确两标量读出，未宣称 BVP 已能达到它。

若把 $H,L$ 也列为两个参数，并把 (41)的12态和其中心12条件加入，(33)去掉固定高度一条，未知数为31态加 $(\bar\nu,L)$ 四参数，边界条件为中心25条加末端八矩与两pose共10条。仍然只是准确的方程计数；端图可达性和 rank 未付。

此外，R530 的中心奇偶不使 $\pm L$ 自动成为反射中心。即便末速度为零，也不能自动援引 R568 的全部 even germs；真实末控制/germ 必须另付。只有那些条件已经满足时，R570 的四段词才可使用 (43)完成 pose；整个第四 period 继续原样保留。

## 9. 完整实现的下一项明确任务

(21)(29)已经把**整个实际 ruling 读出**准确化成 R581 的 C² 局部积分和真实累计状态。接下来必须同时实现 (13)–(17)，不能只实现新的读出而保留一个不准确的第三更新。

固定库后应从原公式预收 $G$、有序 $B$、$\lambda_h,\lambda_k$ 及完整 $c$ 的有限几何系数。所有读出须保持真实整块二尾，四次幅权只提出一次。组合张量 (17)与 (14)应在被积式/形式系数层先合并，再对同一个实际模型作公开求积；原真正高导正平方若未被恒等式消去，不能因它大而删掉。

R581 的局部 C² 身份没有证明原任意 $A$ 能量或整个 $\sigma_s$ 都是 C² 泛函。本稿也不作这种额外断言。它给的是一个准确可逆的完整状态选择，可避免当前 ruling 的独立大项读出相减，并把余下数值稳定责任明确放在真实累计更新上。

有限八根搜索须在同一份已经可准确评价的 (28)–(34)上进行，保所有 incoming 和一个固定最终规范；不回到 R573 已排除定量比例的已登记 $\delta\to0$ 长词，也不以任意运动学高度草图替代本 ODE 的路径。这个接口是继续求根的具体方程，不是主课题完成声明。

### 原来源

- R73：原八矩与有序完整第三密度。
- R221(17)(18)：全部真尾的局部三线性配对及速度线性系数。
- R482 未消历史的 (24)：完整 $\mathscr R+\mathscr L-\mathcal E-4w\cdot t$；不使用其依赖 R480 的 (25)。
- R530：双边实际加速度、共同中心规范、八矩奇偶、真左端重锚及中心 frame 对称。
- R570：实际半周转轴的两条件 pose 接口，只有付清端 germs 后使用。
- R578：六变换六正节点的同一个从起点实际库。
- R581：保原 chain 和真二尾的完整局部 C² 表达。

