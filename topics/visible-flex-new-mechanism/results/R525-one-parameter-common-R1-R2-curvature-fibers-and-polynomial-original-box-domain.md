# R525：一条真实R1射线上的共同R2曲率纤维与原盒多项式域

2026-11-16。本文只作原式、已发表实际摘要和源码的纸面分析，没有执行几何、J、求积、符号程序、开发检查、优化或原实例恢复，没有读取新的研究raw日志。数值事实只引用根已消费并发表的原收据。

**已证明的推进。** 沿已经支付的同一非零R1射线，完整同圈问题不需要任意17维R1二次张量：一个共同标量 $\alpha$、同一17个R2系数 $y$ 已由现存 $V_{17},V_x,Z_x,L_x,H_{xx}$ 完整决定。固定 $\alpha$ 后仍是原盒中的凸曲率纤维；共同选择 $\alpha$ 时，可准确写成次数至多八的有限多项式域。每角的最佳自由对角元是 $A=-C$，原盒则给出一个准确的可达trace区间；这比只检查不可变第二列更强。共同17列能否同时到达所有角区间，由一个连续的标量纤维余量完整描述。

本文没有证明当前58存在合格下降点，也没有把一次后端 status2 提升为射线不可行。最后给一个不同于旧固定幅度LP的新19变量会话合同；源点、原盒和全部实际门保持原身份。

## 1. 新实际证据限定了什么

[反射R1任务的完整实际笔记](../notes/true58-reflected-R1-ray-selected-fiber-infeasible-no-candidate-20261116.md)记录：

- run $\mathtt{43873254906}$，research $\mathtt{133319615177}$，source $\mathtt{0b8bb24ce9d4a9acb3219c6fe01f35328aba4139}$；
- 唯一BVLS成功，nit17，给出同一非零 $x_*\in\mathbb R^{17}$；原向量SHA256为 $\mathtt{49375e447b080d2f41f127a2a213e7b6102f8ab527ff0c57c73797a511af4385}$；
- $\alpha=1/2$ 的环metric约 $.31271618$，违反原58预算；$3/8,1/4,1/8,1/16,1/32,1/64$ 的两网metric、正面积、不变列和剩余R2盒均通过；
- $3/8$ 的细网metric为 $.2471139468080773$，不可变列最大为 $8.706206255002707$，但R1-only完整环曲率达到 $79.96170050758747$；
- 只在 $3/8$ 处解了一次5056行18变量R2问题，返回status2、nit0，没有raw18或对偶乘子；没有全body预测或actual；
- 本任务新增 $19.350847490999968$ 秒、0个full value，结束累计为 $2882.412483226$ 秒、147个full value。当前仍是真实接受58。

因此，metric改善没有自动支付径向二阶曲率；第二列通过也没有支付共同R2与原盒。其余五个合格非零幅度没有被解LP。下一问题不能把它们写成失败，也不能机械重复 $3/8$ 的旧LP。

本次原MODEL已完整保存新向量表，原JSON加LF为13,312,899 B，SHA256：

$\mathtt{ca0aec1d95949c467042eb74b94314a4490d6742e5cf76f040eeba060d1b8f3e}$。

这些新表与先前纯R2的原环二jets共同构成本稿的付费输入。读取身份和新代数处理仍须计入未来明确账户，但不重建旧frame、$\Pi$、BVLS或LP。

## 2. 同一个实际基点、同一原盒与一个共同标量

使用 [R514](R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)、[R516](R516-common-first-radial-jet-quartic-domain-and-original-box-curvature-separation.md) 的原全支撑三jet基：

$$
R_i^{(j)}(\sigma)=\delta_{ij},\qquad \sigma=\text{原radial第141项},\qquad i,j=0,1,2.
\tag{1}
$$

这三条函数是原末三条样条的完整线性组合，不截断其前102列参与的中段。令值层始终为零，只取

$$
x_0=0,\qquad x_1=\alpha x_*,\qquad x_2=y\in\mathbb R^{17}.
\tag{2}
$$

$x_*$ 是上节实际BVLS的原binary64向量。它没有被重新拟合、正交化、缩放到另一范数或替换为准确反射。原新增九个背景坐标、高度坐标、$g,b_0$、永久参考和当前58都不变。

记原独立与物理嵌入为 $\mathsf E_1,\mathsf E_2$ 及 $\mathsf P_1,\mathsf P_2$。理想未舍入状态是

$$
q(\alpha,y)=q_{58}+\alpha\mathsf E_1x_*+\mathsf E_2y,\qquad
c(\alpha,y)=c_{58}+\alpha\mathsf P_1x_*+\mathsf P_2y.
\tag{3}
$$

只改变原51个切向物理系数，其余121个物理坐标逐字保持。原172盒是

$$
\ell-c_{58}\le \alpha\mathsf P_1x_*+\mathsf P_2y\le u-c_{58}.
\tag{4}
$$

若引入 $h$，它表示完整合成物理增量：

$$
h\ge4\|\alpha\mathsf P_1x_*+\mathsf P_2y\|_\infty,\qquad h\ge0.
\tag{5}
$$

不把R1、R2分别算范数后相加，也不先接受或舍入一个中间 $q_1$。本问题不暗加旧 $1/128$。由原有限盒可以给足量 $h_{\max}$，因此引入该足量上界不删掉任何原盒内的点。

因原58在盒内且 $x_*$ 已真实属于 $\mathcal J_1$，凸性保证 $0\le\alpha\le1$ 都在R1投影盒中。不过这只保证至少存在一个R2补偿满足物理盒，并不保证曲率。后文建议的有限会话只取

$$
I=[1/64,1/2],
\tag{6}
$$

避免把原 $\alpha=0$ 闭合实例重新作为目标。这个范围不是整条正射线、负射线或全部R1空间的代称。

## 3. 现有向量表已经给出整条射线的有限恒等

固定一个原角点。记原固定径向尺度为 $a_\sigma>0$，以免与后文曲率分子混淆。原完整归一二jets是

$$
U_0=X_{s,58},\quad T=X_{\theta,58}/a_\sigma,\quad
B_0=X_{ss,58},\quad C_0=X_{s\theta,58}/a_\sigma,\quad
D_0=X_{\theta\theta,58}/a_\sigma^2.
$$

原17列为 $V_j=a_\sigma\Pi Z_j$。沿已付 $x_*$ 只需原记录中的

$$
V=V_{x_*},\qquad Z=Z_{x_*},\qquad L=L_{x_*},\qquad H=H_{x_*x_*}.
$$

同圈完整有限式为

$$
\boxed{
\begin{aligned}
U_\alpha&=U_0+\alpha V, & T_\alpha&=T,\\
Z_{12,\alpha}&=C_0+\alpha Z, & Z_{22,\alpha}&=D_0,\\
Z_{11,\alpha,y}
 &=B_0+\alpha L+\alpha^2H+\sum_{j=1}^{17}V_jy_j.
\end{aligned}}
\tag{7}
$$

式(7)不是Taylor截断。原 $R_1(\sigma)=R_1''(\sigma)=0$、$R_1'(\sigma)=1$，原 $R_2=R_2'=0,R_2''=1$；完整 $T_{ss}$ 的平方只产生 $\alpha^2H$。所有 $\Pi$已在保存的向量中作用于完整原角网；此后只收缩这些表。

不能由(7)冒称任意 $x\in\mathbb R^{17}$ 的完整二次系数已保存。本次支付的是一个 $H_{x_*x_*}$，不是289个 $H_{ij}$。改变射线本身需要另付相应数据。

源码准确来源为：

- [新反射模块](../scripts/frame_metric_current168_reflected_R1_ray.py)的 $\mathtt{\_contract\_R1\_ray}$、$\mathtt{\_r1\_scale\_grid}$、$\mathtt{\_conditional\_grid}$；
- 原MODEL的 $\mathtt{new\_complete\_frame\_and\_vector\_tables}$，包含 $\mathtt{V17,R1\_Vxstar,R1\_Zxstar,R1\_Lxstar,R1\_Hxxstar}$；
- 原纯R2 MODEL的 $\mathtt{position\_two\_jets\_without\_X}$；
- [原ring模块](../scripts/frame_metric_current168_ring17.py)的实际 $G$ 正交化和原172盒。

$V_{x_*}$ 的原完整 $\Pi$ 路径与 $V_{17}x_*$ 的浮点重组差已在原输出单独保存。未来方法须声明自己消费哪条路径；不能把它们当逐位相同，更不能用其微小差异替代严格误差界。

## 4. 原metric域、正面积与一维分段结构

保持原metric定义，设

$$
E(\alpha)=U_\alpha\cdot U_\alpha,\quad
F(\alpha)=U_\alpha\cdot T,\quad
G=T\cdot T>0,
$$

$$
w(\alpha)=U_\alpha\times T=w_0+\alpha w_1,\qquad
Q(\alpha)=w\cdot w=GE-F^2.
\tag{8}
$$

这里 $Q$ 是原法向面积平方。原Schur量是

$$
q_\perp^2=E-F^2/G=Q/G;
\tag{9}
$$

不能把两者同名使用，亦不能因数学单位切向量而把实际binary64 $G$ 写成1。

原预算取当前58的两网最大值

$$
\varepsilon=.26600541463999305.
\tag{10}
$$

这不是把主目标 $.26$ 放宽或改名；它仅是本圈候选域的原58水平。后继全body仍要求实际严格下降。

由R516，准确两metric门为

$$
M_+(\alpha)=\varepsilon(1+\varepsilon-E)-F^2\ge0,\qquad
M_-(\alpha)=\varepsilon(E-1+\varepsilon)-F^2\ge0.
\tag{11}
$$

二者都是至多二次多项式，且与 $y$ 无关。它们等价于原
$\phi=(|E-1|+\sqrt{(E-1)^2+4F^2})/2\le\varepsilon$。

**正面积引理。** 若 $0<\varepsilon<1$ 且 $G\ge\varepsilon$，则(11)给

$$
Q\ge G(1-\varepsilon)+(G/\varepsilon-1)F^2
 \ge G(1-\varepsilon)>0.
\tag{12}
$$

证明只从 $M_-\ge0$ 得 $E\ge1-\varepsilon+F^2/\varepsilon$ 后乘 $G$。因此本域不需要任意另造一个几何面积floor。原实际摘要给两网 $\max|G-1|=6.661338147750939\,10^{-16}$；未来源码仍核并保实际G数组，而不把摘要代替绑定输入。

(12)是准确一致内积中的实数式。浮点 $Q_{\rm cross}=|U\times T|^2$ 与 $G(E-F^2/G)$ 的运算次序可产生差异，必须记录，不能硬设它们相等。原actual面积门也继续独立保留。

加上原投影盒、后文第二列四次门，有限两网的低阶合法 $\alpha$ 集是有限多个闭区间和孤立点的并；若使用正面积条件而无统一正下界，则不应无条件称其闭紧。多项式恒等零、重根和单点区间均允许。七个离散读数不确定这些连续区间的全部端点，更不证明曲率纤维可行性随 $\alpha$ 单调。

## 5. 实际G下的完整形算子分子

定义

$$
p=w\cdot Z_{11,\alpha,y},\qquad
r=w\cdot Z_{12,\alpha},\qquad
c=w\cdot D_0,
$$

$$
a=G^2p-2GFr+F^2c,\qquad b=Gr-Fc.
\tag{13}
$$

由原正交基
$(U-(F/G)T)/\sqrt{E-F^2/G},\,T/\sqrt G$
得到完整对称形算子

$$
\boxed{
S(\alpha,y)=
\begin{pmatrix}A&B\\B&C\end{pmatrix},
\quad
A=\frac{a}{GQ^{3/2}},\quad
B=\frac{b}{GQ},\quad
C=\frac{c}{G\sqrt Q}.}
\tag{14}
$$

这保了原 $a_\sigma$ 在 $Z_{12},Z_{22}$ 中的尺度；不能只用未归一 $X_{s\theta},X_{\theta\theta}$ 填入分子。

次数和最高层依赖非常小：

$$
\deg_\alpha Q\le2,\quad
\deg_\alpha c\le1,\quad
\deg_\alpha b\le2,\quad
a=a_0(\alpha)+G^2\sum_j(w_0+\alpha w_1)\cdot V_j\,y_j,
\tag{15}
$$

其中 $\deg_\alpha a_0\le3$。所以 $B,C$ 与 $y$ 无关，$A$ 对同一17个 $y$ 仿射。

目标 $K=1000/61$ 的不可变列门为

$$
P(\alpha)=K^2G^2Q^2-b^2-c^2Q\ge0.
\tag{16}
$$

它是至多四次式，等价于 $B^2+C^2\le K^2$。本次各合格尺度只支付了这种必要门；R1-only的 $A$ 仍可能把谱范数推到约80。

## 6. 最优自由对角元与真实trace区间

**引理。** 固定任意实数 $B,C$，有

$$
\min_{A\in\mathbb R}
 \left\|\begin{pmatrix}A&B\\B&C\end{pmatrix}\right\|_{\rm op}
 =\sqrt{B^2+C^2},
\tag{17}
$$

并可由 $A=-C$ 取到。

证明：算子作用于第二单位向量给下界 $\sqrt{B^2+C^2}$。当 $A=-C$ 时矩阵平方为 $(B^2+C^2)I$，故取到。这个结论不要求 $B=0$，适用于当前58非轴峰。它只解释逐角的自由对角元，不表示共同17列或原盒能实现 $A=-C$。

令

$$
\tau=A+C,\qquad m=K^2-B^2-C^2.
$$

当 $|C|<K$ 时，完整曲率门准确等价于

$$
m\ge0,\qquad
-\frac{m}{K+C}\le\tau\le\frac{m}{K-C}.
\tag{18}
$$

两端由 $\det(KI\pm S)\ge0$ 得出；此时它们也保证两PSD的trace非负。$\tau=0$ 是区间内一个明确几何目标，但区间一般不以零为算术中心。不能把“最佳自由对角元”误写成对所有可行区间的中点。

退化点必须单独保全：

- $C=K$ 时，第二列门迫 $B=0$；完整要求 $-K\le A\le K$，即 $0\le\tau\le2K$；
- $C=-K$ 时同样 $B=0$，完整要求 $-2K\le\tau\le0$；
- $|C|>K$ 时任意 $y$ 都不可能完成该角点。

在不作任何 $K\pm C$ 除法时，统一保

$$
|\tau|\le2K,\qquad
m+(K+C)\tau\ge0,\qquad
m-(K-C)\tau\ge0.
\tag{19}
$$

这与原两PSD的trace和det完整等价。后文所有分离式均可用(19)，不会删掉退化角点或常数行。

## 7. 无平方根的完整曲率域，而非仅第二列门

令

$$
t=a+cQ,\qquad R=K^2G^2Q^2+ac-b^2=P+ct.
\tag{20}
$$

则 $\operatorname{tr}S=t/(GQ^{3/2})$，
$\det S=(ac-b^2)/(G^2Q^2)$。

对 $K>0,G>0,Q>0$，有完整等价

$$
\boxed{
\|S\|_{\rm op}\le K
\quad\Longleftrightarrow\quad
\begin{cases}
4K^2G^2Q^3-t^2\ge0,\\
R\ge0,\\
R^2-K^2G^2Qt^2\ge0.
\end{cases}}
\tag{21}
$$

**证明。** 实对称二阶矩阵的两个特征值都在 $[-K,K]$，等价于
$KI+S,KI-S$ 同时PSD。二阶PSD各自由非负trace和det刻画，所以先得到

$$
|\operatorname{tr}S|\le2K,\qquad
K^2+\det S\ge K|\operatorname{tr}S|.
$$

全部分母正，第二式成为 $R\ge KG\sqrt Q\,|t|$。它准确等价于
$R\ge0$ 与最后一个平方不等式；第一式给(21)第一行。特别是 $R\ge0$ 不可删，否则平方会加入伪解。此末代数已获另一作者窄核，范围仅限该二阶谱界等价。

三行对 $\alpha$ 的次数分别至多 $6,4,8$，对 $y$ 的次数分别至多 $2,1,2$。不能把完整谱域笼统叫“六次”，也不能把原第二列的四次门当作(21)。对固定 $\alpha$，(21)虽呈二次 $y$，其真实可行集合仍是原四条PSD仿射行的交；凸性由未平方原式保证。

本节清分母的用途是给出完整单参数代数域及可直接求导的函数。数值入口必须回到未平方原PSD和原单位残差判断候选；大正分母、平方和缩放不能替代原容差，也不能把新多项式成功当作原actual通过。

## 8. 原盒给出更强的逐角可达区间

原三条末系数对每个模式 $j$ 满足

$$
l_{\ell j}
 \le W_{\ell1}\alpha x_{*,j}+W_{\ell2}y_j
 \le u_{\ell j},\qquad \ell=1,2,3.
\tag{22}
$$

按 $W_{\ell2}$ 符号正确除与换端点，零系数保原常数不等式，得到

$$
\mathcal Y(\alpha)=\prod_{j=1}^{17}[L_j(\alpha),U_j(\alpha)].
\tag{23}
$$

$L_j$ 是有限仿射函数的最大值，$U_j$ 是有限仿射函数的最小值；两者分段仿射、连续，允许零宽。若任一空区间或常数行失败，则此 $\alpha$ 已被原盒排除，不再假定义其support function。

由(15)、(20)，

$$
t(\alpha,y)=t_0(\alpha)+\sum_j M_j(\alpha)y_j,\qquad
M_j(\alpha)=G^2(w_0+\alpha w_1)\cdot V_j,
\tag{24}
$$

其中 $t_0$ 至多三次，$M_j$ 至多一次。定义准确的原盒trace分子范围

$$
\begin{aligned}
t_{\min}(\alpha)
 &=t_0+\sum_j\{M_j^+L_j+M_j^-U_j\},\\
t_{\max}(\alpha)
 &=t_0+\sum_j\{M_j^+U_j+M_j^-L_j\}.
\end{aligned}
\tag{25}
$$

这里 $M_j^+=\max(M_j,0)$，$M_j^-=\min(M_j,0)$。线性函数在非空紧凸盒上的像恰好为这个完整闭区间，不只给上下界。将盒活动面和 $M_j$ 的零点分段后，(25)为至多三次多项式。

对 $|C|<K$，同角点要求的trace分子区间为

$$
\mathcal I_K(\alpha)=
\left[-\frac{P}{KG\sqrt Q+c},
       \frac{P}{KG\sqrt Q-c}\right].
\tag{26}
$$

这是(18)乘 $GQ^{3/2}$，所有因子和符号均保。退化 $|C|=K$ 用第6节的trace界，不用(26)的零分母。

因此，**某一个角点能够由原盒中的R2完成**，准确等价于其第二列门成立，且

$$
[t_{\min}(\alpha),t_{\max}(\alpha)]\cap\mathcal I_K(\alpha)
 \ne\varnothing.
\tag{27}
$$

如果交集为空，这个 $\alpha$ 的整个R2纤维立即被该角点与原盒联合排除。它比单独 $P\ge0$ 更强，也不要求先求另一个固定幅度LP。

但把(27)对所有角点分别检查仍只是必要条件：各点允许的 $y$ 可能不同。下一节保同一 $y$，准确封住这个缺口。这里没有执行新的(25)查询，也没有据现有status2倒推出哪个角点已满足严格排除。

## 9. 共同纤维余量与一维优化的准确等价

固定非空 $\mathcal Y(\alpha)$。把完整四条未平方PSD行统一写成

$$
\mathsf R(\alpha)y\le d(\alpha),
\tag{28}
$$

其行与R516(31)、原源码的 $\mathtt{plus/minus\_trace}$、
$\mathtt{plus/minus\_determinant}$ 一致；原数值行尺度不能随证明中的任意归一混用。定义

$$
\mathfrak f(\alpha)
 =\min_{y\in\mathcal Y(\alpha)}
       \max_i\big(\mathsf R_i(\alpha)y-d_i(\alpha)\big).
\tag{29}
$$

所有行取明确同一固定正尺度时，下述符号结论不变；尺度本身必须绑定，不能在求解中为掩盖残差自适应改变。

紧性给最小值确实取到。因此

$$
\mathfrak f(\alpha)\le0
\quad\Longleftrightarrow\quad
\text{该}\alpha\text{存在同一原盒R2完成全部有限角网。}
\tag{30}
$$

有限单纯形与紧凸盒上的线性minimax给

$$
\boxed{
\mathfrak f(\alpha)=
\max_{\lambda\ge0,\ \boldsymbol1^{\mathsf T}\lambda=1}
 \left[
 -\lambda^{\mathsf T}d(\alpha)
 -h_{\mathcal Y(\alpha)}
     \big(-\mathsf R(\alpha)^{\mathsf T}\lambda\big)
 \right].}
\tag{31}
$$

不要求Slater条件，不要求盒有内点。零宽坐标照原相等条件处理；空盒先退出。

在任意低阶合法的紧 $\alpha$ 集上，若 $Q$有统一正下界，$\mathsf R,d$连续；(23)的端点也连续。以
$y=L(\alpha)+(U(\alpha)-L(\alpha))z,\ z\in[0,1]^{17}$
统一到固定紧盒，(29)的函数连续且局部一致连续，故 $\mathfrak f$连续。由(21)也可见，有限网时其零水平可行域是半代数集。

于是共同射线问题准确是

$$
\min_{\alpha\in I_{\rm legal}}\mathfrak f(\alpha)\le0?
\tag{32}
$$

这是数学等价，并不授权免费执行每个 $\alpha$ 的LP。若采用内层LP，所有内层调用必须另记优化成本；本稿建议的下一会话直接联合求 $\alpha,y,h$，不调用这些固定幅度内层实例。

两个有用后果是：

1. 一个严格可行 $(\alpha_0,y_0)$ 若同时保原盒的必要相对内部余量，则连续性给一个邻近可行区间；不需要该方向在其余五个已读幅度也可行。
2. 若整个紧域满足 $\mathfrak f>0$，便有一致正余量。每个点可由(31)的一个真实非负乘子严格分离，连续性给邻域，紧性给有限覆盖。要把它写成严格射线排除，必须真正支付这些乘子与覆盖的有向/准确界；一个没有dual的后端status2并未支付任何这类证据。

对连续整角圈，原盒紧性仍给R516所述的有限支撑分离：任一固定 $\alpha$ 的全圈无交有某个有限角子族见证。但仅当前两网的可行点不能授全连续圈；也不能从有限网的局部优化失败推出(32)为正。

## 10. 解析导数只需新收缩现有表

后继19变量模型无需新的几何J。其非平凡导数可以完整写成下表，所有点积仍在同一角点、同一已付向量表上。

$$
\begin{aligned}
E_\alpha&=2U_\alpha\cdot V,&F_\alpha&=V\cdot T,\\
w_\alpha&=V\times T,&Q_\alpha&=2w\cdot w_\alpha,\\
p_\alpha&=w_\alpha\cdot Z_{11}
             +w\cdot(L+2\alpha H),\\
r_\alpha&=w_\alpha\cdot Z_{12}+w\cdot Z,&
c_\alpha&=w_\alpha\cdot D_0,\\
a_\alpha&=G^2p_\alpha-2G(F_\alpha r+Fr_\alpha)
                +2FF_\alpha c+F^2c_\alpha,\\
b_\alpha&=Gr_\alpha-F_\alpha c-Fc_\alpha,\\
t_\alpha&=a_\alpha+c_\alpha Q+cQ_\alpha,\\
R_\alpha&=2K^2G^2QQ_\alpha+a_\alpha c+ac_\alpha-2bb_\alpha.
\end{aligned}
\tag{33}
$$

对每个 $y_j$，

$$
a_{y_j}=t_{y_j}=M_j,\qquad R_{y_j}=cM_j;
\tag{34}
$$

$E,F,Q,b,c$不依赖 $y$。三条(21)残差的导数为

$$
\begin{aligned}
\partial_\alpha(4K^2G^2Q^3-t^2)
 &=12K^2G^2Q^2Q_\alpha-2tt_\alpha,\\
\partial_{y_j}(4K^2G^2Q^3-t^2)&=-2tM_j,\\
\partial_\alpha R&=R_\alpha,\qquad \partial_{y_j}R=cM_j,\\
\partial_\alpha(R^2-K^2G^2Qt^2)
 &=2RR_\alpha-K^2G^2(Q_\alpha t^2+2Qtt_\alpha),\\
\partial_{y_j}(R^2-K^2G^2Qt^2)
 &=2RcM_j-2K^2G^2QtM_j .
\end{aligned}
\tag{35}
$$

原盒与完整物理norm行对 $(\alpha,y,h)$ 是线性的，目标 $h$ 也是线性。式(33)–(35)是新有限模型的解析导数；未来每次实际评价必须计费，不能说“源表已付所以新的优化与导数免费”。它不是新168参数几何J，也不需要重新生成完整角 $\Pi$。

## 11. 精确恒等、源数组有限模型与实际候选分开

应明确区分三层：

- 原连续真实场中的(7)–(35)是准确数学恒等；
- 已付binary64向量表定义一个新的有限预测模型；浮点点积、$Q_{\rm cross}$、原Schur路径与原 $\Pi$ 重组可不同，不声称逐位或有向等价；
- 最后实际binary64候选由原有理嵌入组合后每个被触及坐标一次舍入，须重新经过完整非线性预测和原actual14。

如果未来用严格有理多项式证明，应先把选择的全部存储常数解释为有理数，按同一内积一致构造 $G,Q,a,b,c$，并给这个代数模型独立身份。它仍不是原连续场的误差证书。不能一边使用旧独立舍入的 $G/E/F$，一边把有理 $Q=EG-F^2$ 和 $Q=w^2$当作已经逐字验证的同一值。

数值入口可保原来源的实际G，选定 $Q_{\rm cross}$ 做新多项式预测，并保存它与 $Gq_\perp^2$ 的实际差。合格向量还应沿原未平方正交化/PSD路径读出原单位残差，不以(21)的平方尺度覆盖它。数学上冗余的(12)若用于数值闭域，也须如实标成这一新有限模型中的约束。

物理合成的准确顺序是：

$$
\alpha_{\mathbb Q}=\operatorname{Fraction}(\alpha_{\rm raw}),\quad
y_{\mathbb Q,j}=\operatorname{Fraction}(y_{{\rm raw},j}),\quad
x_{*,\mathbb Q}=\text{原binary64精确有理值},
$$

$$
q_{\rm ideal}
 =q_{58,\mathbb Q}
  +\alpha_{\mathbb Q}\mathsf E_{1,\mathbb Q}x_{*,\mathbb Q}
  +\mathsf E_{2,\mathbb Q}y_{\mathbb Q},
\tag{36}
$$

然后一次round至168坐标。保未舍入增量、理想172系数、实际rounded168/172及舍入差。各系数独立舍入后 $R_0=0$ 等中性身份可能只近似成立，不能把理想圈的门授给实际候选。原172盒按准确有理值判；原height、mirror、ball、regularity、curvature和其余actual门全部保留。

## 12. 唯一新共同会话合同

根已接受以下独立新问题；本稿和源码文本本身不执行它。

| 项目 | 固定范围 |
|---|---|
| 当前基点 | 真正58；原physical、168坐标、固定g/b0、原172盒 |
| 变量 | $\alpha+y_{17}+h$，共19 |
| 射线范围 | $\alpha\in[1/64,1/2]$；原已付 $x_*$ 唯一 |
| 目标 | 最小完整物理步长上界 $h$ |
| 圈条件 | 原metric预算(10)、正面积、实际G、完整谱 $K=1000/61$ |
| 原盒 | (4)，不把 $\mathcal J_1$ 成员冒作完整R2盒 |
| 唯一初点 | $\alpha=1/4$；$y$取该处准确剩余盒各区间中点；$h$取完整物理增量范数 |
| 新优化 | 一次带解析Jac的19变量约束非线性会话；不重启，不对离散幅度补LP |
| 迭代/评价 | maxiter160；至多400次完整值及解析Jac模型评价，同一输入缓存不重复收缩 |
| 科学时钟 | 新600秒，输入/导入/解析/组装/优化/输出都计入 |
| solver子钟 | 目标120秒；回调检查不能抢占一个底层调用，实际超额必须保留 |
| 复用范围 | 原二jets、$V_{17},V_x,Z_x,L_x,H_{xx}$、原精确嵌入和原输出身份 |
| 不发生的旧工作 | 0旧BVLS，0旧固定幅度LP，0新frame/$\Pi$/几何J/输入ordinary |
| 后继预测 | 至多一个真正rounded候选的全body非线性metric+curvature预测 |
| actual | 只有预测原曲率门通过且相对58严格η降至少 $10^{-7}$ 才至多1pair/2值；原actual14 |
| 祖先费用 | $2882.412483226$ 秒、147值，闭账保留；旧剩余时间不转成新额度 |

初点的中点构造只保证原盒，不保证曲率可行。零宽坐标保相等约束；原不动坐标只在其真实常数门成立时消掉数值常数行，不伪造自由度。

一个约束非线性后端返回“成功”不足以接受：先保其真实raw19和全部返回字段，再读原未平方行、原metric及准确原盒，最后才可能进入全body预测。后端失败、时间/评价额度耗尽、非有限返回或无向量都原样记录；不能以一个guard结果覆盖原状态，也不据本局部算法失败宣称(32)在整个区间严格为正。

每个实际进入的完整模型评价只记一次，目标/约束/Jac对同一字面输入可以读同一已付缓存。失败评价也保started与实耗。source恢复失败、模型组装partial、solver异常和stdout失败前已完成的真实数据、费用都要保；最后权威钟晚于大输出。不能用未执行的新16/17/19维开发检查冒作已通过，也不重旧suite。

## 13. 此结果怎样推进下一步

现有结果允许把原“选首个低阶合格幅度，再尝试R2”的顺序选择，改成同一个有限域中共同选择 $\alpha$ 与 $y$。真正新信息不是再支付一个相同LP，而是：

1. 原R1改变法向和 $X_{ss}$ 的完整二次代价已被保进同一模型；
2. 最佳自由曲率完成有明确的trace零目标；
3. 原盒的逐角可达trace区间可以指出不变列之外的具体阻碍；
4. 全部共同角约束由连续纤维余量(29)准确刻画，若需要严格排除也有明确的乘子及区间覆盖义务；
5. 下一有限会话只增加一个非线性标量，没有假称缺失的任意R1二次张量已付。

主课题的全body、连续角精化、全时间等距和非局部reach仍未完成。当前谱目标只针对本圈的曲率；即使新共同问题找到候选，仍须付同一个实际候选的全部原门。

## 来源

- [R514：完整51圈控制与条件17维曲率纤维](R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)。
- [R516：共同17维四次域与原盒分离](R516-common-first-radial-jet-quartic-domain-and-original-box-curvature-separation.md)，特别是原metric、实际G、原盒和support-function判据。
- [R519：反射支、均值及真实径向lift](R519-fixed-ring-reflection-branch-and-mean-compatible-radial-lift.md)，不把原有界LS投影称为准确反射。
- [本次反射射线的已发表实际收据](../notes/true58-reflected-R1-ray-selected-fiber-infeasible-no-candidate-20261116.md)。
- [原ring源码](../scripts/frame_metric_current168_ring17.py)与[本次反射源码](../scripts/frame_metric_current168_reflected_R1_ray.py)，全文只读，未执行。

