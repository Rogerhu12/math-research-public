# R616：同一真实候选的严格扩盒函数图与完整空间 jets

2026-11-27。**已证明：任一 R609/R614 已接受的原函数候选都可成为下述新函数图的准确零点输入；变换保留原中心、末端 germs，扩大人工值域，并给出初始形状方向的连续下界。**
本稿不执行科学计算，不重新拟合已付四偶端，不声称三端图、两 ruling 的根或满秩，亦不改变原 R598 物理盒。

关联纯接口为
[`scripts/r616_same_candidate_expanded_box_agent.py`](../scripts/r616_same_candidate_expanded_box_agent.py)。
这里先给出可以被真实后继消费的函数图；具体后继必须以原 R614 run45885627093 的自然终态为依据另定范围，不能把本稿当作已经启动的计算。

## 1. 固定的真实输入与未被改变的原问题

令 $x=s/L\in[0,1]$。固定一组实际已接受的 R609/R614 系数
$\bar a,\bar b$、物理长度 $\bar L$ 和两个物理常规范。
旧函数本身为

$$
\bar h(x)=\frac{19}{10}+\tanh\!\left(\sum_{j=0}^{m_0-1}\bar a_j\cos(j\pi x)\right),
\qquad
\bar k(x)=\frac{39}{20}\tanh\!\left(\sum_{j=0}^{m_0-1}\bar b_j
\sin\frac{(2j+1)\pi x}{2}\right).
\tag{1}
$$

因此处处有 $9/10<\bar h<29/10$、$|\bar k|<39/20$。
这些是旧函数族的人为值域；原 R598 物理值域仍为

$$
\frac45<h<3,\qquad |k|<2.
\tag{2}
$$

首个真实函数 run45881816067 的接受末态已贴近 (1) 的人工边缘，见
[原终态收据](../notes/2026-11-27-r609-true-integral-function-natural-final-agent.md)。
这提供改善后继函数图的实际动机，但不证明某个原方程根必须越过人工边缘。
本图可固定任意实际接受的 (1)；不能悄悄用未接受试步替代它。

原 R598 母、完整两侧系数、正势系数 1、十八整块、576 微包、
$\varepsilon=1/12000$、原 collars、同一个 $\chi$、真积分历史以及所有原尺度都不变。
固定输入中的常规范也不因这个形状变换而重选单位。

## 2. 一个保持基函数的有理变换

对任意 $c\in\mathbb R,r>0$、$u\in(c-r,c+r)$ 和有限实数 $A$，定义

$$
t=\frac{u-c}{r},\qquad T=\tanh A,
$$
$$
\boxed{\quad
\mathcal C_{c,r}(u,A)
 =u+r\frac{(1-t^2)T}{1+tT}
 =c+r\frac{t+T}{1+tT}.
\quad}
\tag{3}
$$

因 $|t|,|T|<1$，有 $1+tT>0$，且

$$
1-\left(\frac{t+T}{1+tT}\right)^2
=\frac{(1-t^2)(1-T^2)}{(1+tT)^2}>0.
\tag{4}
$$

故 (3) 始终在 $(c-r,c+r)$ 中。对固定 $u$，
$A\mapsto\mathcal C_{c,r}(u,A)$ 严格单调，极限为两个端值，
因而是 $\mathbb R$ 到该开区间的光滑双射。
证明可以用 $\tanh(\operatorname{atanh}t+A)$ 解释，
但实现只用 (3) 的**旧值加增量**，不作 `atanh` 与 `tanh` 的往返重构。

取新的有限函数

$$
A(x)=\sum_{j=0}^{m-1}a_j\cos(j\pi x),\qquad
B(x)=\sum_{j=0}^{m-1}b_j\sin\frac{(2j+1)\pi x}{2},
\tag{5}
$$

并定义

$$
\boxed{\begin{aligned}
h(x)&=\mathcal C_{19/10,\,11/10}(\bar h(x),A(x)),\\
k(x)&=\mathcal C_{0,\,199/100}(\bar k(x),B(x)).
\end{aligned}}
\tag{6}
$$

由 (4)，任意有限新系数都满足

$$
\frac45<h<3,\qquad |k|<\frac{199}{100}<2.
\tag{7}
$$

这里 $k$ 保留 $1/100$ 的外盒余量；没有把原 $|k|<2$ 约束扩大。
它也没有自动支付 $|\eta|<1$、物理速度盒、长度盒或三个真实端积分。
这些约束仍须对 (6) 的实际曲线检查或求解。

旧基函数给出全区间、全新系数的分母界

$$
\begin{aligned}
\left|\frac{\bar h-19/10}{11/10}\right|&<\frac{10}{11},
&1+t_h\tanh A&>\frac1{11},\\
\left|\frac{\bar k}{199/100}\right|&<\frac{195}{199},
&1+t_k\tanh B&>\frac4{199}.
\end{aligned}
\tag{8}
$$

所以本图没有沿旧候选产生接近零的分母，也不需要依赖某个 sampled 最小值来说明可定义。
浮点评价若因饱和舍入真正落到 $h=4/5$ 或 $h=3$，实现必须拒绝该点；
连续严格区间结论不能替代数值域检查。

## 3. 同候选入口与完整空间二阶链

当全部新系数为零时，$A=B=0$，有

$$
h\equiv\bar h,\qquad k\equiv\bar k.
\tag{9}
$$

这不是重新拟合旧曲线。尤其在固定 $L=\bar L$ 和旧两个物理规范时，
它给出同一物理路径、同一连续 $\eta$、全部八个 $A$、六个 $\rho$、
依赖中心及完整两 ruling。
同一离散规则、同一字段的重用也没有新增科学信息；后继不得把这种同值入口计作数值改善。

下面明确空间 jets，以免只保函数值却改掉速度或加速度。
用 $J_2 f=(f,f_x,f_{xx})$，其加法逐项进行，乘法、倒数为

$$
J_2(fg)=
(fg,\ f_xg+fg_x,\ f_{xx}g+2f_xg_x+fg_{xx}),
\tag{10}
$$
$$
J_2(q^{-1})=
\left(q^{-1},-q_xq^{-2},2q_x^2q^{-3}-q_{xx}q^{-2}\right).
\tag{11}
$$

若 $T=\tanh A$，则

$$
J_2T=
\left(T,(1-T^2)A_x,
(1-T^2)(A_{xx}-2TA_x^2)\right).
\tag{12}
$$

以 (10)—(12) 逐项构造

$$
J_2\mathcal C_{c,r}(u,A)
=J_2u+r\,J_2(1-t^2)\,J_2T\,J_2(1+tT)^{-1}.
\tag{13}
$$

其中每一分量本身还携带所有新参数的自动微分 Jet。
故空间微分与参数微分的混合项全保，包含 $T_x,T_{xx}$、
分母的一阶和二阶空间变化，不能只对 (3) 的数值分量求参数导数。

当新系数为零时，$A=A_x=A_{xx}=0$，从而
$T=T_x=T_{xx}=0$；(13) 的整个增量三元组为零。
所以 (9) 连同 $h_x,k_x,h_{xx},k_{xx}$ 同时成立。
源码以旧字段加零增量实现该入口，避免 `atanh` 重构的额外往返误差。
这不是对不同算术、不同求积器或旧物理 readout 实现之间逐 bit 一致性的宣称。

## 4. 原中心和末端 germs 自动保留

原 $\bar h$ 与 $A$ 关于 $x=0$ 偶，$\bar k$ 与 $B$ 关于 $x=0$ 奇。
高度变换中 $t_h,T_h$ 均为偶函数；曲率变换中 $t_k,T_k$ 均为奇函数，
分子 $t_k+T_k$ 为奇、分母 $1+t_kT_k$ 为偶。因此

$$
h(-x)=h(x),\qquad k(-x)=-k(x).
\tag{14}
$$

每个余弦和每个奇半波正弦又都关于 $x=1$ 偶，
故两个新函数也关于 $x=1$ 偶。于是准确有

$$
k(0)=h_x(0)=k_{xx}(0)=0,\qquad
h_x(1)=k_x(1)=0.
\tag{15}
$$

经 $s=Lx$ 换算后，这就是 R609 原条件
$k(0)=\gamma(0)=b(0)=0$、$\gamma(L)=\upsilon(L)=0$。
所有相应更高奇偶 germs 也保留，因为有限基函数和 (3) 在 (8) 下光滑。
中心高度 $H$、$a(0)$、$\upsilon(0)$ 仍可变化，没有加回 prepared 数值。

$k_x/(2h)$ 关于中心偶，所以从零积分的真实 $\eta$ 关于中心奇。
这与原全反射符号和 R609 的真实历史重建相容。
它没有令八矩末端自动为零；四个偶端条件仍是实际积分条件。

## 5. 初始形状方向的连续下界及其范围

对固定 $u$，由 (3) 有

$$
\frac{\partial\mathcal C_{c,r}}{\partial A}
=r\frac{(1-t^2)(1-T^2)}{(1+tT)^2}>0.
\tag{16}
$$

在零新系数处，令 $w=r(1-t^2)$，则

$$
\delta u_{\rm new}=w\,\delta A,
\quad
\delta(u_{\rm new})_x=w_x\delta A+w\delta A_x,
\quad
\delta(u_{\rm new})_{xx}=w_{xx}\delta A+2w_x\delta A_x+w\delta A_{xx},
\tag{17}
$$

其中

$$
w_x=-2t\bar u_x,\qquad
w_{xx}=-2\left(\frac{\bar u_x^2}{r}+t\bar u_{xx}\right).
\tag{18}
$$

由旧人工值域，而非某个离散最小值，准确得到

$$
\boxed{\quad w_h>\frac{21}{110},\qquad
w_k>\frac{394}{4975}.\quad}
\tag{19}
$$

例如 $w_h>(11/10)(1-100/121)=21/110$；
$w_k>(199/100)(1-195^2/199^2)=394/4975$。
因此旧 `tanh` 潜变量接近人工饱和值时，也不会在新图的零点把相应值方向压成零。

更具体，由连续三角基正交性，对任意系数方向有

$$
\int_0^1(\delta h)^2dx
\ge\left(\frac{21}{110}\right)^2
\left((\delta a_0)^2+\frac12\sum_{j=1}^{m-1}(\delta a_j)^2\right),
\tag{20}
$$
$$
\int_0^1(\delta k)^2dx
\ge\frac12\left(\frac{394}{4975}\right)^2
\sum_{j=0}^{m-1}(\delta b_j)^2.
\tag{21}
$$

这是**新参数到两个形状值函数**的连续注入界。
它不证明三端约束雅可比的满秩，不证明完整 ruling 算子的可逆性，
也不保证采用某个 sampled 规则后仍有同一离散奇异值界。
离开零点后 (16) 仍为正，但大修正也会产生新的 `tanh` 饱和；
(19) 的统一下界只用于本图的同候选入口，不能推广为任意系数的全局下界。

有限 $m$ 下，这是一族以同一候选为入口的新函数，
不声称它与原固定有限维 `tanh` 族逐参数等价或包含原族全部成员。
改变有限函数族必须在后继请求里明确登记。

## 6. 与 R612 长度、R614 两规范和真历史的接口

零修正、固定 $\bar L$ 是准确同候选入口。
如果后继采用 [R612](R612-exact-physical-length-elimination-and-three-true-end-integrals.md)
长度图，则新的实际形状还须满足 $K>1,U>0$，并取

$$
L=\sqrt{\frac{U}{K-1}},\qquad
K=\int k^2,\quad U=\int(h_x/h)^2.
\tag{22}
$$

这里的 $h,k,h_x$ 都是 (6)(13) 的新字段。
全部 $\delta L$ 链按 R612 保留；长度盒 $[2.1,7.9]$、
原速度盒和 $\eta$ 盒继续施加。
换求积规则后从 (22) 重选长度不再是固定物理曲线；固定精化必须保留末实际 $L$。

八矩、六个 $\rho$ 和依赖中心全部由同一新曲线重积分。
四偶原行仍完整输出；余三行的恢复不能通过独立历史节点吸收误差。
[R614](R614-complete-two-ruling-global-gauge-projection.md)
的两全局规范投影继续使用原冻结单位和完整离根导数，
正势与所有交叉项保持。新图没有改变 $\zeta_0$ 的依赖定义。

纯接口提供单独的物理几何 adapter，保证 frame、位置和 collar 读数也消费 (6)，
不能误把修正系数喂给只认识 (1) 的旧 `PhysicalCurve`。
本稿未新增数值任务、未支付端根、ruling、period/pose、全时 reach 或主 README 完成门。

