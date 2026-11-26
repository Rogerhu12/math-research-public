# 双 bubble 端点映射的折叠与新增径向形状：完整六控制 KKT 接口

日期：2026-11-26。类型：完整解析构造、条件命题与后继接口；没有本地科学运行，没有新 root、候选场、F/J 或连续证书。原双 bubble 的一般 IFT 已在 [R695](../results/R695-so3-zero-closure-bubble-uniform-IFT.md) 登记，本文不重证该结果。本次新增责任是明确有限控制像的轴端结构、哪些变化真正增加控制能力，以及保原三控制而新增独立径向形状后的完整 KKT/角 jet/转置。

## 1. 当前实际证据允许的判断

[轴端平面同族证明](2026-11-26-zero-endpoint-axis-planar-control-equivalence.md) 已逐字使用固定十八字输入，证明旧端轴 Q 与 moment-Q 在 phi=0 的反射平面分支是同一两独立 Ry bubble 族，只改变参数坐标及有限球。把原两 bubble 各放成三个 world 轴，在原反射协变下仍只留下两个平面 Ry 控制。

[实际阶段15](2026-11-26-public-actions-45820592817-1-part-004.md) 的失败角索引为5，不是 phi=0。它的最后真正回溯候选仍在半径0.75球内，残差没有下降；当前 Cz 的最小数值奇异值为0.0003935073141565039，没有严格误差界。[阶段19](2026-11-26-public-actions-45820592817-1-part-005.md) 换成固定 moment-Q 后又在索引5以同方程回溯不下降结束。它没有返回新的完整六 jet 场，不能从批最大修正量推造该角所有未记录数据。

同一第5卷的阶段23已让原 H 通过全角、全支撑补集的单位速必要条件，且报告明确不能据此证明有限 bubble 族有根。阶段21工作 Istar 与原 reference H 的末字差异也不能解释这些根失败。以下不据这些事实声称已发生严格 fold、已证无根或必须降低 H。

## 2. 平面端点像是两条完整曲线的和

沿用上条证明的 phi=0、零 omega、同 core/chart、准确单位基底

$$
T_0=(b,0,c),\qquad b^2+c^2=1.
$$

把 xz 平面向量写为 q(s)=(b(s),c(s))，定义

$$
\mathsf J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad \mathsf R(t)=\exp(t\mathsf J).
$$

两个 bubble 的支撑 I0、I1 内部互不相交。记 U=I0∪I1，

$$
V_{\rm out}=\int_{[0,S]\setminus U}q(s)\,ds,
\qquad V_i(t)=\int_{I_i}\mathsf R(\beta_i(s)t)q(s)\,ds.
$$

准确端点映射及目标为

$$
V(t_0,t_1)=V_{\rm out}+V_0(t_0)+V_1(t_1),
\qquad d=(R-p(0),H).
\tag{1}
$$

闭合就是 V=d。两条一维参数曲线的和并不自动等于由单位速必要条件允许的整个圆盘；通过支撑长度条件没有支付这个有限函数族的覆盖。

直接求导得到

$$
V_i'(t)=\mathsf J M_i(t),\qquad
M_i(t)=\int_{I_i}\beta_i(s)\mathsf R(\beta_i(s)t)q(s)\,ds,
\tag{2}
$$

$$
V_i''(t)=-\int_{I_i}\beta_i(s)^2
                 \mathsf R(\beta_i(s)t)q(s)\,ds.
\tag{3}
$$

所以平面 Jacobian 奇异的准确条件是

$$
\det\bigl(M_0(t_0),M_1(t_1)\bigr)=0.
\tag{4}
$$

它说明两个**已经修正过的加权切向矩**变为平行。初点用某个 Q 把 Jacobian 预条件到接近单位阵，并不能使 (4) 在有限控制上永远不发生。任何固定可逆二乘二重参数化只右乘该 Jacobian，零行列式集合所对应的物理控制函数不变。

### 条件 fold 判据

若在某 t*，DV 的秩恰为1，k=(k0,k1) 生成其核，n 是非零目标法向，满足 nᵀDV=0，则核方向的二阶法向量为

$$
q_{\rm fold}=n\cdot
       \bigl(k_0^2V_0''(t_0^*)+k_1^2V_1''(t_1^*)\bigr).
\tag{5}
$$

若 q_fold≠0，先用唯一的非零切向导数消去切向目标坐标，剩余法向分量在核参数 eta 上具有 q_fold·eta²/2 加高阶项。这给出通常的局部折叠：同一侧局部有两支、另一侧无该邻域内的根。这个证明只是 Taylor 展开和一维隐式消元，不把某个工作 SVD 的小值升级为其前提。

现有公开实际15/19没有提供当前严格秩、准确 n、(5) 的符号或整个有限像，因此还不能填写当前输入位于哪一侧，也不能排除远处其它根。现有同方程残差 continuation 改变的是找根路径，值得实际尝试；它本身不增加 (1) 的可达像。

## 3. 高度变化应有怎样的具体理由

H 只把目标 d 沿竖直方向平移。靠近上述条件 fold，在消去切向坐标后的法向目标位移一阶含 n_z·delta H。降低 H 是否把目标送回可达一侧，必须结合 n_z、q_fold 以及目标当前的有号法向差；符号不能从“根回溯失败”或“初点 Cz 小”推出。若 n_z=0，H 对该局部法向障碍连一阶修正都没有。

此外，H 是整个帽的一个共同自由参数。不能在每个角单独选 H(phi) 来闭合，再把它冒称为原常高帽；选择一个新初始 H 要同时满足全角的实际根/几何责任。阶段23的必要高度区间并不是有限泡泡可闭合高度区间。

当前没有准确 fold 法向或有限像边界的返回，原 H 又已通过完整支撑必要条件。故本分析不给无根据的新高度数值，保原 H；后继若改 H，应明确这是新的物理初点和它要解决的已读目标差，不引用不存在的长度障碍。

## 4. 真正严格包含旧控制函数族的新输入

保留原 W=beta0 Q0+beta1 Q1 及其全部十八个固定字。新增一个 C² quintic bump gamma，完整支撑仍在原 U 内。例如可明确选择精确相对三节点

$$
(1/16,1/8,3/16),
\tag{6}
$$

用 R695 的同一 S5 升/降公式定义，外部为零。这个支撑严格位于原第一支撑 (1/32,15/32) 内。gamma 与 beta0 重叠是有意的新定义，不能继承只对两不交支撑得到的某些积分常数。gamma 的 value、slope、second jet 在支撑外端都为零。

gamma 不在 span(beta0,beta1) 中：第二支撑上 gamma=beta0=0、beta1非零，迫使 beta1 的系数为零；第一支撑内但 gamma 支撑外的开区间上 beta0非零，又迫使 beta0 系数为零，而 gamma 本身非零。这是准确函数恒等判断，不用对节点矩阵数值判秩。

引入独立 world 轴向控制 v∈R³，定义

$$
w(s,\phi)=W(s,\phi)z(\phi)+\gamma(s)v(\phi),
\qquad \widehat T=\exp([w]_\times)T_y.
\tag{7}
$$

v=0 准确恢复原全部三控制修正函数，故新**容许控制函数族**严格包含旧族；不是重算 moment、换 Q 的三维基或重命名变量。新增三轴不依赖当前自由点改变 gamma 或 Q，避免遗漏这种适应性输入的导数。

这里的严格包含不等于后面“最小范数选支后的单值场映射”逐点包含旧选支。一个旧可行控制 (z,0) 未必满足新 v 方向的驻点式；新最小范数根可能选择不同控制。两者须分别记录，不能借容许集合包含就继承旧场的实际数值或几何。

### 轴端为什么这次增加了一个真实形状

保持原反射协变：z 是 polar，v 是 axial。phi=0 时必有

$$
z_y=0,\qquad v_x=v_z=0.
$$

于是

$$
w(s,0)=
\bigl(\beta_0t_0+\beta_1t_1+\gamma v_y\bigr)e_y.
\tag{8}
$$

这给三个独立标量径向形状对两个平面端点式；旧释放两 bubble 六轴仍只有两个形状。准确零控制时，三个平面切向场方向分别为 beta0·ey×T0、beta1·ey×T0、gamma·ey×T0。因 |ey×T0|=1，它们的函数线性独立等价于三形状独立，故真实 meridian 的线性扰动空间也严格增加。

### 可具体修复一个平面 fold 的条件

在旧平面控制处，新 gamma 方向的端点列为

$$
j_\gamma=\mathsf J\int_U\gamma(s)\widehat q(s)\,ds,
\quad \widehat q=\mathsf R(\beta_0t_0+\beta_1t_1)q.
\tag{9}
$$

如果旧 DV 秩1且 n·j_gamma≠0，新三列的平面端点 Jacobian 就有秩2。相较同一旧 fold 的一侧局部像，新控制可在该端点附近给出完整二维局部覆盖。这是新增形状的明确作用条件，不是“多变量总会更好”的判断。

还有一个可控选择命题：若 h(s)=n·J·qhat(s) 在 U 内不恒零，则其连续性给一个 h 同号且严格离零的开区间；在其中选有理相对端点的正 S5 bump gamma，必有 n·j_gamma=∫gamma h≠0。可以同时使它不在原两形状的 span 中。若已经得到严格该条件的实际分支，这给新形状的构造依据。

(6) 是一个完整明确但尚未科学评价的候选输入，尚未证明它对当前未认证的转折满足 (9)。不得把存在某个可选局部 bump 的条件证明，换成所列固定 bump 已成功的数值宣称。新有限像、全角分支与其余 Gram 方程仍未解决。

## 5. 六控制与三乘子的完整、无量纲 KKT

为了不把不同控制的旧半径0.75混为同域，明确使用

$$
u=(\zeta,v)\in\mathbb R^6,\qquad z=S\zeta,
\qquad B(s,\phi)=[S W(s,\phi),\gamma(s)I_3].
$$

S 是同一固定准确 scalar 的长度，不是待求参数。定义无量纲端点式和选支目标

$$
f(y,u,\phi)=\frac1S\left\{
\Gamma_y-P_y+\int_0^S\exp([Bu]_\times)T_y\,ds\right\},
\qquad E(u)=\tfrac12|u|^2.
\tag{10}
$$

其目标等价于原变量中的 (|z/S|²+|v|²)/2。这是明确新的根选支范数，与外层完整 H²/阻尼、旧三维搜索球均有独立身份。没有往闭合方程中加惩罚项；最终仍须 f=0，不能以小松弛或小正则化残差代替它。

令 A=f_u，乘子 ell∈R³，完整九维 KKT 残差为

$$
\mathcal R(y,Y,\phi)=
\begin{pmatrix}u+A^T\ell\\f\end{pmatrix}=0,
\qquad Y=(u,\ell)\in\mathbb R^9.
\tag{11}
$$

其准确 Jacobian 为

$$
K=\mathcal R_Y=
\begin{pmatrix}
L&A^T\\ A&0
\end{pmatrix},\qquad
L=I_6+\sum_{j=1}^3\ell_j f_{j,uu}.
\tag{12}
$$

没有丢掉 multiplier 乘约束 Hessian 的项，也不把 (12) 改成只含单位矩阵的近似后仍称准确隐式 Jacobian。

**充分非奇异条件：** A 满行秩3，且 hᵀLh>0 对所有非零 h∈ker A 成立。若 K(h,k)=0，则 Ah=0，左乘 hᵀ得 hᵀLh=0，故 h=0；随后 Aᵀk=0，满行秩给 k=0。K 因而可逆。这同时是所选约束极小点的严格二阶充分条件，不证明其它分支或全局唯一最小点。

六控制可能在旧三维 f_z 奇异时仍使 A 满行秩，(9) 给出了轴端一个明确条件；但新 L 在约束切空间的正性、全角可逆性和实际根都不能省略。普通数值 KKT 成功也不直接成为向外区间证书。

完整一、二控制导数可由同一原方程给出。记 X=[Bu]_cross，则

$$
A h=\frac1S\int D\exp(X)[[Bh]_\times]T_y\,ds,
\tag{13}
$$

$$
f_{uu}[h,k]=\frac1S\int
D^2\exp(X)[[Bh]_\times,[Bk]_\times]T_y\,ds.
\tag{14}
$$

固定 Q、gamma、S、theta0 与全部积分域均不随当前 y 改变。公式不以有限 Newton 迭代图代替准确 (11)。

## 6. 周期、反射、端口及轴端方程维数

对空间反射 Sref，z 随 polar 规则变换，v 随 axial 规则变换，故 u 的正交作用为 diag(Sref,det(Sref)Sref)。端点 f 与乘子 ell 均随 polar 规则变换。|u|² 不变，旧 W 的已证协变与径向 gamma 使 (11) 完整等变。要由唯一性推出对称，须把分支声明在这些正交作用保持的域中，并保证其中根唯一；仅每个分散数值根各有自己的局部 IFT 邻域还不够。

另一条充分的选支合同是：从后文对称的 t=0 种子出发，按同一 t 路径在全角持续跟随 K 可逆的同一分支，不跳到另一个根。对称像与原解在起点相同，每一局部延续邻域的 IFT 唯一性便使二者逐段保持相同。周期也须由同一分支绕圈返回，或以该同路径从周期种子延续来保证；实际只算 quarter 时，还须支付反射固定轴处的相容端口。逐角任意选择 KKT 根没有这些保证。

在 phi=0，偶控制为 (z_x,z_z,v_y) 三个，奇控制为 (z_y,v_x,v_z) 三个；偶乘子为 (ell_x,ell_z)，奇乘子为 ell_y。若在该轴直接施加对称子空间，应解三控制与两个独立平面端点式的五维 KKT。若保完整九维系统，须核完整 K 可逆，并使该解及其反射位于上述同一唯一性域，或由对称种子沿同支得到，才能推出这些奇分量为零；不能把平面恒零的 f_y 当作额外独立约束。

所有 beta/gamma 在 core、cap 邻域恒零，故修正保持真实 T_y、T_y,s 的端口。准确 f=0 时取

$$
\widehat F=P_y+\int_S^s\widehat T\,dv.
\tag{15}
$$

core 恰为当前 Gamma_y，cap 恰为同一 R er(theta0)+H ez，且准确径向 Gram 等于1。原反射 C² 接合由同端口继承；没有 hDelta，也没有未闭合时把 hDelta 删掉。交叉与角向这另外两个 Gram 分量、幅度、嵌入与 reach 均仍须实际求解/验证；径向分量已恒1，不应误用其它表示的分量命名。

新 gamma 的准确分片点须进入后续连续积分共同分割。若数值入口保持原 Gauss 工作节点，也必须如实报告新 gamma 求值及其完整积分误差尚未包围；不能因支撑仍在 U 就把新 shape 的所有连续费用继承为已付。

## 7. 全变量、完整角二 jet 与真实 J/J*

原 free core、完整 omega、H 均在 y 中。对固定 Y 的原参数方向 h，

$$
f_y[h]=\frac1S\left(D\Gamma_y[h]-DH[h]e_z
 +\int\exp(X)DT_y[h]\,ds\right),
\tag{16}
$$

$$
\mathcal R_y[h]=
\begin{pmatrix}(f_{uy}[h])^T\ell\\ f_y[h]\end{pmatrix}.
\tag{17}
$$

DΓ 包含完整当前 core 逆角的隐式链；H 的 cap 导数未删除，DT_y 保全部原 omega 方向。在准确选支上

$$
DY[h]=-K^{-1}\mathcal R_y[h].
\tag{18}
$$

令所有 phi 偏导在固定 Y 下取。完整角 jet 为

$$
Y_1=-K^{-1}\mathcal R_\phi,
\qquad
Y_2=-K^{-1}\left(\mathcal R_{\phi\phi}
 +2\mathcal R_{\phi Y}Y_1
 +\mathcal R_{YY}[Y_1,Y_1]\right).
\tag{19}
$$

W 的 theta0、rho0 及全部角导数必须在这些偏导中，不能只对 Ty 求导。实际字段只消费 u、u1、u2，但 ell、ell1、ell2 仍在隐式系统里，不能丢掉它们的反作用。

### 完整六物理 jet 的具体消费式

令 u_j 是 Y_j 的前六个控制分量，u_0=u。用固定输入矩阵 B 的真实导数，

$$
\begin{aligned}
w&=Bu,& w_s&=B_su,\\
w_\phi&=B_\phi u+Bu_1,&
w_{\phi\phi}&=B_{\phi\phi}u+2B_\phi u_1+Bu_2.
\end{aligned}
$$

定义 R=exp([w]_cross)。R_s、R_phi 分别是 Dexp 对 w_s、w_phi 的完整作用，R_phiphi 是 D²exp 对两个 w_phi 的作用加 Dexp 对 w_phiphi 的作用。于是

$$
\begin{aligned}
\widehat T&=RT_y,\\
\widehat T_s&=R_sT_y+RT_{y,s},\\
\widehat T_\phi&=R_\phi T_y+RT_{y,\phi},\\
\widehat T_{\phi\phi}&=R_{\phi\phi}T_y
                      +2R_\phi T_{y,\phi}+RT_{y,\phi\phi}.
\end{aligned}
$$

完整返回必须是

$$
\begin{aligned}
F&=P_y+\int_S^s\widehat T,&F_s&=\widehat T,\\
F_\phi&=P_{y,\phi}+\int_S^s\widehat T_\phi,&F_{ss}&=\widehat T_s,\\
F_{s\phi}&=\widehat T_\phi,&
F_{\phi\phi}&=P_{y,\phi\phi}+\int_S^s\widehat T_{\phi\phi}.
\end{aligned}
$$

u 不随查询 s 改变，它由整条 meridian 的端点 KKT 确定；不能在每个径向点独立找一个控制，也不能把 partial 积分的根误当 full 端点根。新增 gamma_s 进入 B_s，固定 Q 的全部角导数进入 B_phi/B_phiphi。

对全部六物理 jet 及其原参数 J/J*，应构造三个九维式

$$
\begin{aligned}
R_0&=\mathcal R,\\
R_1&=\mathcal R_\phi+K Y_1,\\
R_2&=\mathcal R_{\phi\phi}
  +2\mathcal R_{\phi Y}Y_1
  +\mathcal R_{YY}[Y_1,Y_1]+K Y_2.
\end{aligned}
\tag{20}
$$

变量为 Z=(Y,Y1,Y2)，共27维。其 Jacobian 为

$$
R_Z=
\begin{pmatrix}K&0&0\\B_1&K&0\\B_2&2B_1&K\end{pmatrix},
\tag{21}
$$

$$
B_1h=\mathcal R_{\phi Y}h+\mathcal R_{YY}[h,Y_1],
$$

$$
B_2h=\mathcal R_{\phi\phi Y}h
 +2\mathcal R_{\phi YY}[h,Y_1]
 +\mathcal R_{YYY}[h,Y_1,Y_1]
 +\mathcal R_{YY}[h,Y_2].
$$

因此可以用同一 K 依次解三块，不必稠密形成27×27；转置按相反顺序解。对实际残差/观察算子 L(y,Z)，完整 reduced Jacobian 与转置为

$$
J=L_y-L_Z R_Z^{-1}R_y,
\qquad R_Z^T\eta=L_Z^*r,
\qquad J^*r=L_y^*r-R_y^*\eta.
\tag{22}
$$

旧三控制 root 的9×9角 jet 源不能仅换名字就承担这里的27维合同。KKT stationarity 已含 f_u，其角二 jet 含 f_uφφ；再对原参数作一次完整 J/J* 会需要 f 的混合四阶导数，Dexp 的最高相关阶也增至4。有限 Fourier/quintic 当前候选及正 rho 逆角可在所需方向提供这些导数，但实际实现、复杂度与向外误差必须另付，不能套用旧只到三阶的界宣称完整。

一个完整实现的数组合同可以明确为：每角最终 Y 有9个分量，Yjets 形状为 (angle,3,9)，物理旋转只消费其中 (angle,3,6)；固定 B/B_s/B_phi/B_phiphi 的形状为 (radial,angle,3,6)，校正后 T/T_s/T_phi/T_phiphi 仍为 (radial,angle,3)。最终隐式 pullback 使用全部27分量及原全部 y，不能把末三乘子丢弃后调用旧3root的转置。缓存必须绑定当前完整 y、实际角地址、新控制输入和最终 KKT 分支；这只是明确的后继接口，尚无已运行的实现。

## 8. 明确的 continuation 起点与未完成责任

这不是改写当前已排的旧同方程 continuation 源。以下 §6/§8 的 t 只用于辅助求根，不是 README 要求的物理弯曲参数；实现应使用独立的 continuation_parameter 名称。若未来实现本新增形状，可用该辅助 t∈[0,1] 定义

$$
f^{(t)}(y,u)=f(y,u)-(1-t)f(y,0).
\tag{23}
$$

在 t=0，u=0、ell=0 是明确 KKT 解；若 A(y,0) 满行秩，其 K 为 (I,Aᵀ;A,0)，由前述证明非奇异，故局部路径可从真实零控制出发。这只提供局部起点，不保证能到 t=1。

### 当前零 omega 起点的全角旋转关系

若仍是本分析的零 omega 轴对称基底，令 O(phi)=Rz(theta0(phi))，则 Ty(s,phi)=O Ty(s,0)，W(s,phi)=O W(s,0)Oᵀ。按本无量纲 u=(z/S,v) 定义，直接把 O 移出端点导数积分得到

$$
A(\phi)=O(\phi)A(0)
             \operatorname{diag}(O(\phi)^T,O(\phi)^T).
\tag{24}
$$

其新增 v 块在零点明确是

$$
A_v(0)=-\frac1S\left[\int_0^S\gamma(s)T_0(s,0)\,ds\right]_\times.
\tag{25}
$$

u=ell=0 使 L=I，故以 D=diag(O,O,O) 有 K(phi)=D K(0)Dᵀ。起点的全角秩/奇异值责任因此可准确归结为同一3×6矩阵，而不是每个角不同的未知控制条件。这里的矩是真实连续积分；已冻结的工作 Q 字不因此成为它的准确右逆。非零 u、ell 的后继路径也不能继承这个仅起点的等谱简化。

每一 t 仍使用完整新 KKT 方程、真实 Hessian 与同全径向积分；lambda 一词不再兼指 continuation 参数，以免漏掉乘子链。仅 t=1 的实际闭合根才可交完整物理场和外层求解，不能把中间 f^(t)=0 的人为端点目标冒称原 C=0。

数值搜索域应显式给出无量纲 (u,ell) 的开域/步长/残差容限，或者明确给控制和乘子的分别界限，并纳入新模型/算法身份。旧 z 的0.75球不等于新六控制球；新算法没有继承旧球的 IFT 常数。普通数值迭代若失败就如实保失败，不能把未通过的根替成零或只报 stationarity 而漏闭合残差。

完整可执行后继至少要新绑定：原准确 scalar/profile/reference、全部固定 Q 字、gamma 精确三节点及 S5定义、选支成本与尺度、当前完整 y、所选分支规则、工作 quadrature、最终三组 KKT jet 残差、27维隐式 J/J* 与原全部物理/幅度/永久位置筛。本文没有执行这些科学责任，也没有把这份数学接口当作它们的返回。

现有同方程 continuation 与原 integral 全方向可以先实际推进。新增 gamma 的具体价值，是一个能够在轴端增加独立径向形状、并在条件 (9) 下移除旧平面控制秩缺陷的不同构造机制；它不是换三维坐标后重复同一失败，也不保证当前问题的根或最终等距完成。
