# R723　保留法向方向的正定流支撑与完整欧氏 reach 下界

2026-11-27。状态：新增的完整几何充分条件及其准确全叶接口已经证明；没有任何当前数值场据此获证。

本条加强 [R650](R650-positive-definite-flow-support-reach.md) 中支撑项的使用方式。原证明在平行面上把真实的 $n^{\mathsf T}An$ 提前换成了 $\lambda_{\max}(A)$。保留这个法向方向量，可以给出更大的有效法管；拓扑、全部平行面之间的注入性、实际欧氏曲率和完整闭面责任均不减少。

本条不改变固定度量 $g$、相位定义、$0.03D$ 目标、全部自由变量或二阶导数的含义。它不降低当前工作场已经实际算出的主曲率，也不把有限屏幕、未返回的完整场或可变进度当作连续证书。当前固定四个 $p^4$ 标记仍采用原参数。

## 1. 定理与完整对象

设 $F:S^2\to\mathbb R^3$ 为 $C^2$ 浸入，$n$ 是其连续全局单位法向；由局部正则性，$n$ 实际为 $C^1$。给定一个对整个参数球面固定的中心 $c\in\mathbb R^3$ 和实对称正定矩阵 $A$。记

$$
s_A(p)=\bigl(A(F(p)-c)\bigr)\cdot n(p),\qquad
a_A(p)=n(p)^{\mathsf T}An(p),
$$

$$
m=\lambda_{\min}(A)>0,\qquad L=\lambda_{\max}(A).
\tag{1}
$$

因为 $n$ 是单位向量，$m\le a_A\le L$。

**定理 723-A（方向支撑法管）。** 若在整个参数球面上

$$
s_A(p)>0,\qquad \max\{|\kappa_1(p)|,|\kappa_2(p)|\}\le K
\tag{2}
$$

成立，其中 $\kappa_i$ 是同一 $F$ 的实际欧氏主曲率，定义

$$
\rho_A=\min_{p\in S^2}\frac{s_A(p)}{a_A(p)}>0,\qquad
r_A=\min\{\rho_A,K^{-1}\},
\tag{3}
$$

并在 $K=0$ 时约定 $K^{-1}=+\infty$。则 $F$ 为嵌入，选定的 $n$ 是其有界内域的外法向，且

$$
\boxed{\operatorname{reach}(F(S^2))\ge r_A.}
\tag{4}
$$

紧性、连续性及 $a_A\ge m>0$ 保证式(3)中的最小值存在并且严格为正。没有预先假设 $F$ 单射。

特别地，对于给定 $\tau>0$，以下完整点态条件已经充分：

$$
\boxed{
s_A(p)\ge\tau\,a_A(p),\qquad
|\kappa_i(p)|\le 1/\tau
\quad(p\in S^2,\ i=1,2).
}
\tag{5}
$$

此时 $\operatorname{reach}\ge\tau$。式(5)允许等号；实际法管证明在 $|u|<\tau$ 内使用严格不等式，不要求端点平行面仍正则。

这里必须是闭参数球面上的同一浸入。仅有上片、未付接缝的分片、几个角度、几个相位或只含固定帽之一的集合，都不能作为式(2)或式(5)的完整输入。

## 2. 流坐标、每张平行面与完整法管的注入性

以下给出全局论证，不能用“每个平行面分别嵌入”替代不同平行面之间的分离。

令

$$
X(x)=A(x-c),\qquad
\Psi(q,t)=c+e^{tA}q,\qquad q\in S^2.
$$

对 $x\ne c$，函数 $t\mapsto |e^{-tA}(x-c)|^2$ 的导数为

$$
-2\,e^{-tA}(x-c)^{\mathsf T}A e^{-tA}(x-c)<0.
$$

它在 $t\to-\infty$ 时趋无穷，在 $t\to+\infty$ 时趋零。因此恰有一个 $t(x)$ 使该范数等于1。隐函数定理给出光滑逆

$$
x\longmapsto\bigl(\pi_A(x),t(x)\bigr),\qquad
\pi_A(x)=e^{-t(x)A}(x-c).
$$

于是 $\Psi$ 是从 $S^2\times\mathbb R$ 到 $\mathbb R^3\setminus\{c\}$ 的全局光滑微分同胚，并且

$$
\ker D\pi_A(x)=\operatorname{span}\{X(x)\}.
\tag{6}
$$

固定 $|u|<r_A$，置

$$
F_u(p)=F(p)+u n(p).
$$

以 $dn=-dF\circ S$ 定义形算子，有

$$
dF_u=dF\circ(I-uS).
$$

因为 $|u|K<1$，$F_u$ 是 $C^1$ 浸入，同一个 $n(p)$ 垂直它的切平面。最关键的准确支撑恒等式为

$$
\begin{aligned}
X(F_u(p))\cdot n(p)
&=s_A(p)+u\,a_A(p)\\
&\ge(\rho_A-|u|)\,a_A(p)>0.
\end{aligned}
\tag{7}
$$

在式(5)版本中直接把 $\rho_A$ 换成 $\tau$ 即可。式(7)是相对 R650 的实质加强；没有把 $a_A$ 换为 $L$。

式(7)首先排除 $F_u(p)=c$。考虑

$$
P_u=\pi_A\circ F_u:S^2\longrightarrow S^2.
$$

若 $dP_u(v)=0$，式(6)给出 $dF_u(v)=bX(F_u)$。与 $n$ 点乘，再用式(7)，得到 $b=0$；由浸入性得到 $v=0$。所以 $P_u$ 是 $C^1$ 局部微分同胚。

紧致定义域使 $P_u$ 的像闭，局部微分同胚使像开；目标球面连通，所以像是全部 $S^2$。紧致局部微分同胚是有限覆盖。由于定义域连通且目标 $S^2$ 单连通，此覆盖只有一层，$P_u$ 因而是全局 $C^1$ 微分同胚。特别地，$P_0$ 单射已经证明原 $F$ 是嵌入。

还必须比较不同的 $u$。定义

$$
p(u,q)=P_u^{-1}(q),\qquad
T(u,q)=t\bigl(F_u(p(u,q))\bigr).
$$

映射 $(p,u)\mapsto(P_u(p),u)$ 的微分中，关于 $p$ 的块处处可逆；各 $u$ 截面已双射。联合反函数定理和逆的唯一性给出 $p,T$ 对 $(u,q)$ 联合 $C^1$。准确有

$$
F_u(p(u,q))=c+e^{T(u,q)A}q.
$$

固定 $q$ 对 $u$ 求导，左侧为 $n+dF_u(\partial_u p)$。与 $n$ 点乘，切向项消失，得到

$$
\boxed{
\partial_uT(u,q)
=\frac{1}{X(F_u(p(u,q)))\cdot n(p(u,q))}>0.
}
\tag{8}
$$

因此沿每条固定流轨道，不同欧氏法向位移 $u$ 按严格相同的次序排列。若

$$
F(p)+u n(p)=F(p')+u'n(p'),\qquad |u|,|u'|<r_A,
$$

两边给同一个 $q$ 和同一个流参数。式(8)先推出 $u=u'$，再由 $P_u$ 单射推出 $p=p'$。故整个欧氏法向映射

$$
\mathcal N:S^2\times(-r_A,r_A)\to\mathbb R^3,\qquad
\mathcal N(p,u)=F(p)+u n(p)
\tag{9}
$$

全局单射。这一步同时排除了任意两片、任意两个帽和活动片与固定帽的混合碰撞；它不是若干局部结论的并列。

由于 $P_0$ 是微分同胚，$F(S^2)$ 在流坐标中是单个图 $t=T(0,q)$。集合 $t<T(0,q)$ 加上中心 $c$ 是包含 $c$ 的有界内域；紧性和正定流保证它含有 $c$ 的一个小球且整体有界。另一侧 $t>T(0,q)$ 通向无穷。式(7)在 $u=0$ 表明 $X$ 与 $n$ 同向穿向后一侧，所以所选 $n$ 的确是外法向，不需要先假设全局外向性再证明嵌入。

最后，任意 $y$ 满足 $\operatorname{dist}(y,F(S^2))<r_A$ 时，紧性给出最近点。无边界极小条件使 $y-F(p)$ 垂直切平面，故 $y=\mathcal N(p,u)$ 且 $|u|=\operatorname{dist}(y,F(S^2))<r_A$。若有第二个最近点，就违反式(9)的单射。距离为零时原 $F$ 的嵌入性处理同一问题。故此开距离邻域内最近点唯一，按 reach 定义即得式(4)。没有声称在 $|u|=r_A$ 上仍然单射。

全部论证只使用 $F\in C^2$、$n\in C^1$ 和平行面的 $C^1$ 微分，不增添 $C^3$ 条件。

## 3. 与原支撑预算的关系及严格改善的意义

若原 R650 的完整预算 $s_A\ge\sigma>0$ 已经成立，则

$$
\frac{s_A(p)}{a_A(p)}\ge\frac{\sigma}{L},
\qquad
r_A\ge\min\{\sigma/L,K^{-1}\}.
\tag{10}
$$

所以数学上的新充分界保留原充分界。把 $A$ 同时乘以任何正数，分子分母同倍改变，$\rho_A$ 不变；不能用矩阵整体缩放制造额外 reach。

这个改善可能严格。以中心为 $c$、半径为 $R$ 的准确球面为例，$F-c=Rn$，所以 $s_A=R a_A$，$\rho_A=R$，实际曲率为 $1/R$。新界给出 $R$；原统一预算只给 $Rm/L$。这只是定理的解析比较，不是用于当前求解的数值样本或前置测试。

区间实现仍需区分数学支配关系和具体盒估计。新的区间乘法可能比旧行更宽，因此应保留原已付分支。一个新的盒不充分，不得撤销另一个仍然有效的旧证书；两个独立有效下界可以取较大值。

本条只改进**支撑**一侧。必要的实际曲率条件仍是 $K\tau\le1$。真实曲面在某点的曲率若已经过准确误差支付而违反该条件，不可能靠本条解除该曲率障碍；尚未付误差的工作浮点值则仍只是工作证据。

## 4. 同一 $A_\beta$ 的完整非单位法向形式

对整个闭面使用一个共同的

$$
A_\beta=\operatorname{diag}(1,1,\beta),\qquad \beta>0,\qquad c=0.
$$

在上片采用当前源的候选定向

$$
N=F_\phi\times F_s,\qquad w=|N|>0.
$$

记

$$
a=F_xN_x+F_yN_y,\qquad b=F_zN_z,\qquad
q_h=N_x^2+N_y^2,\qquad q_v=N_z^2.
$$

准确有

$$
s_\beta=\frac{a+\beta b}{w},\qquad
a_\beta=\frac{q_h+\beta q_v}{w^2}.
$$

故目标式(5)的支撑部分等价于

$$
\boxed{
w(a+\beta b)-\tau(q_h+\beta q_v)\ge0.
}
\tag{11}
$$

也就是

$$
C_0+\beta C_1\ge0,\qquad
C_0=wa-\tau q_h,\quad C_1=wb-\tau q_v.
\tag{12}
$$

这里的 $a,b$ 只是两个支撑分子，不是矩阵 $A$ 或目标度量 $g$ 的系数。对于一般固定中心 $c$，将它们相应改为
$(F_x-c_x)N_x+(F_y-c_y)N_y$ 和 $(F_z-c_z)N_z$，同一推导仍成立。本条当前接口保持原中心0，不另外优化或移动中心。

与原条件 $a+\beta b\ge\tau\max(1,\beta)w$ 相比，式(12)对 $\beta$ 是一个仿射约束，不需因为 $\beta=1$ 分成两种数学公式。但所有叶、上下半面、帽与全部相位必须选择**同一个**正 $\beta$；逐叶各取不同 $\beta$ 不能代入全局流论证。

给一个已付完整叶，对准确 $C_0,C_1$ 分别产生有理下界 $\underline C_0,\underline C_1$。由于 $\beta>0$，

$$
\underline C_0+\beta\underline C_1\ge0
\tag{13}
$$

是该叶的有效充分条件。用精确有理线性不等式处理正、负、零系数及开端点 $\beta>0$，再与所有完整叶和固定帽的约束求交即可。非严格目标边界允许保留；正定性边界 $\beta=0$ 必须排除。

生成 $\underline C_i$ 时必须对同一完整区间作真正的有符号乘法。尤其当 $a$ 或 $b$ 的下界为负时，不能擅用 $w_{\rm lo}a_{\rm lo}$ 或 $w_{\rm lo}b_{\rm lo}$ 当乘积下界。$q_h,q_v$ 必须来自同一法向的完整平方分量；可以用 $q_h+q_v=w^2$ 的准确恒等式作相容交，但不能拼接不同点、不同场或不同快照的最好端点。

也可以在选定 $\beta$ 后，从同一叶直接包围

$$
\frac{w(a+\beta b)}{q_h+\beta q_v}.
\tag{14}
$$

分母由 $w>0,\beta>0$ 严格为正。只有支付了分母正性、分子符号以及相反端点除法，式(14)才给可靠的 $\rho_\beta$ 下界。全部原叶取最小值；漏叶、部分角胞、只有字面角节点或未付根盒时，不输出整面下界。

## 5. 原固定四个 $p^4$ 帽的有理仿射约束

本节只复用 [R661](R661-complete-nonplanar-activity-and-four-fixed-markers.md) 已证明的**组件公式**，不继承其中旧6077的高度、半径、嵌入或场结论。

当前四个标记仍取高度 $h=1/1000$、半径 $1/25,9/200,1/20,11/200$ 和原固定圆心。在一张上帽图上写作

$$
F(x)=(x,H+f(x)),\qquad f\ge0,\qquad
N=(-\nabla f,1).
$$

原组件公式及互不重叠的支撑给出

$$
|\nabla f|\le\frac1{20},\qquad
|x|\le\frac15\text{ 在标记支撑上},\qquad
|\kappa_i|\le5.
\tag{15}
$$

平坦余部的梯度和曲率均为零，不需要对其所有 $x$ 强加 $|x|\le1/5$。实际帽半径必须足以容纳全部原标记及平领；原闭面端口消费者对此仍独立负责。

令

$$
u_*=\frac1{400},\quad G_*=\frac1{100},\quad
d_+=1+\frac{u_*}{2}=\frac{801}{800},\quad
d_-=1+\frac{u_*}{2}-\frac{u_*^2}{8}
=\frac{1281599}{1280000}.
\tag{16}
$$

这些都是预定准确有理数。直接展开可得

$$
d_-^2\le1+u_*,\qquad d_->1,\qquad
d_-d_+\ge1+u_*.
\tag{17}
$$

例如
$d_-^2=1+u_*-u_*^3/8+u_*^4/64$
和
$d_-d_+=1+u_*+u_*^2/8-u_*^3/16$；
由于 $0<u_*<2$，上述方向均严格合法。

取准确共同高度下界 $H_-\le H$，设 $B=\beta H_--G_*$。帽上的方向支撑条件为

$$
\bigl(\beta(H+f)-x\cdot\nabla f\bigr)
\sqrt{1+|\nabla f|^2}
\ge\tau\bigl(\beta+|\nabla f|^2\bigr).
\tag{18}
$$

令 $z=|\nabla f|^2\in[0,u_*]$。左侧第一个因子至少为 $B$。以下**两个**有理仿射条件足以支付整张帽：

$$
\boxed{
(H_--\tau)\beta\ge G_*,
}
\tag{19}
$$

$$
\boxed{
(d_-H_--\tau)\beta\ge d_-G_*+\tau u_*.
}
\tag{20}
$$

证明如下。式(19)给 $B\ge\tau\beta>0$。平方根的凹性和式(17)给

$$
\sqrt{1+z}\ge1+(d_--1)\frac{z}{u_*}.
$$

将这个下界乘以正的 $B$，再减 $\tau(\beta+z)$，所得是 $z$ 的仿射函数。其 $z=0$ 端点由式(19)非负，$z=u_*$ 端点由式(20)非负，故整个区间非负。这就证明式(18)。外向下帽是该图的空间反射，相同推导和同一 $\beta,H_-$ 适用。

这两个帽约束在当前有理预算上也保留旧帽充分条件。旧条件是

$$
B\ge\tau\max(1,\beta)d_+.
\tag{21}
$$

它立即给 $B\ge\tau\beta$。同时，式(17)给

$$
Bd_-\ge\tau\max(1,\beta)(1+u_*)
\ge\tau(\beta+u_*),
$$

所以式(21)推出式(19)–(20)。因此帽组件没有因为选取有理平方根下界而无意丢掉原已付范围。

对于**无标记**的两个平盘，$f=0,\nabla f=0$。方向支撑商准确为 $H$，与 $\beta$ 无关；其支撑条件只需 $H\ge\tau$，曲率为0。不能把有标记的帽与无标记盘当成同一个几何输入。

原标记曲率预算5不能用本条降低：半径最小的标记在中心梯度为零，其实际两主曲率绝对值恰为 $8h/(1/25)^2=5$。新的完整标记面仍需 $\tau\max(K_{\rm activity},5)\le1$。

## 6. 全部相位、上下拼接与混合点对

当前相位的活动像由绕竖直轴旋转和原严格材料角重参数化生成。对于同一 $A_\beta$，任何这种旋转 $R$ 都满足 $R^{\mathsf T}A_\beta R=A_\beta$，故

$$
\begin{aligned}
\bigl(A_\beta R(F-c)\bigr)\cdot Rn
&=s_\beta,\\
(Rn)^{\mathsf T}A_\beta Rn&=a_\beta.
\end{aligned}
\tag{22}
$$

实际欧氏主曲率也保持。竖直反射与 $A_\beta$ 同样交换。这里使用的是完整闭面一致定向所传送的单位法向；若只机械反射参数叉积而忘记换图定向，会多出一个符号，不能拿它代替真实下片外法向。

因此，只有在当前准确源已经支付以下责任后，上片全域加固定帽的界才覆盖全部相位：

- 原核心与上下片、末端与平帽/标记帽的完整二阶端口、$C^2$ 接合和球面拓扑；
- 同一完整场的整面浸入和严格角重参数化，及原强 $C^2$ 参数族；
- 当前参考图与当前自由核心的准确区分，全部当前角模、三通道、全部径向叶和全部32段 normal 分支；
- 固定帽的实际原参数、支撑分离、完整帽半径及相同中心；
- 同一 $\beta$、同一 $\tau$、同一完整欧氏曲率上界在所有上述组成部分同时成立。

完成这些输入后，对每个相位应用定理723-A。全局法向映射(9)一次包含该相位的完整闭面，因而活动片—活动片、活动片—固定帽、上下片、两帽等混合点对均在同一个全局注入性证明内。不能用分别证明各片有 reach，再对它们取最小值来替代这一步。

若 $D^+$ 是 [R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 由同一完整叶三维范数及全部帽产生的真实整像直径上界，保持

$$
\tau=\frac3{100}D^+.
\tag{23}
$$

证明 $\operatorname{reach}\ge\tau$ 就足以给原 $\operatorname{reach}\ge0.03D$。不降低 $D$ 定义，不换固定度量，不删标记，也不把有限半径屏幕当作 $D^+$。若 $D^+$ 本身尚未付，本条不产生实际半径。

## 7. R718 距离与 R716 无标记外管必须分别消费

[R718](R718-positive-definite-flow-distance-and-whole-image-held-witness.md) 使用的是完整目标面上的支撑下界

$$
s_\beta\ge\sigma>0,
$$

以及 $m=\min(1,\beta)$。本条的 $\rho_\beta$ 或 $\tau$ 不是这个 $\sigma$。例如由式(5)只能直接推得 $s_\beta\ge\tau m$；当 $\beta<1$ 时，不能省去 $m$。

因此完整消费者仍应保留原全叶支撑复读和固定帽支撑计算，明确输出同一个**标记目标面**的 $\sigma$。如果选择使用 $\tau m$ 这个下界，必须在证据中明确它由式(5)与 $a_\beta\ge m$ 推出，仍满足 R718 原假设；不能把方向半径字段改名为原支撑字段。原整像盒距离和 R718 距离可继续取最大值，R719/R720 的轴比前提也不改变。

同样，[R716](R716-asymmetric-fixed-caps-and-centred-volume-moment.md) 第6节所需的**无标记**外法管不能从标记后面的 reach 倒推。后继必须再次明确：

1. 对同一活动片和两张真实平盘构造原无标记闭浸入，完整端口与定向已付；
2. 活动片使用同一全叶式(11)，平盘使用本条 $H\ge\tau_0$，而曲率仅取实际活动片上界；
3. 对这一无标记闭面独立应用定理723-A，得到其真实 $r_0>0$；
4. 只有严格 $h_{\rm mark}=1/1000<r_0$ 时，才调用 R716 第6节已有的外管、固定柱体不交及十二原始矩可加性。

无需构造新的工作场或重算任何积分，但辅助无标记几何对象和标记对象的支撑、曲率、reach 证据必须各自明确。主报告若晚失败，原副件仍不能单独当作已付外管证书；本条不改变既有主报告完整状态、同点、同快照和全原路径字节重核合同。

## 8. 当前完整源码能提供什么

本节只定位真正可复用的现有数据与有意不同的证明分支，不声称新的执行入口已经写成或运行。

### 8.1 有限工作屏幕已经使用实际形算子

当前完整有限 geometry 源为

[so3_fixed_fejer_batched_missing_angle_geometry.py](../scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py)，88163 B，SHA256：

~~~text
5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135
~~~

其完整网格由同一六 jet 构造 $I,II$，使用实际 $\operatorname{tr}(I^{-1}II)$ 和 $\det(I^{-1}II)$ 的二次特征公式；逐永久点调用的原完整曲率源也直接求对称广义特征问题。故当前有限 $K_{\max}$ 并非二阶 jet 三角上界。

直接连续形算子和不丢真实阈值的完整二阶判据早已在 [R279](R279-finite-field-direct-continuous-curvature-certificate.md)、[R672](R672-complete-lowmode-sixjet-curvature-with-laurent-remainders.md) 登记。本条不把这些公式再次登记为新结果。后继可以把已登记的判据应用到新准确全叶，和现有有效曲率上界取较小者，但必须保持完整同场六 jet、正浸入以及全部原域；那是既有理论的来源适配。

### 8.2 新方向支持所需完整量已经保存在准确流中

当前准确 geometry 源为

[fixed_fejer_meridian_batched_producer_R722_continuous_gram_curvature_support.py](../scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_continuous_gram_curvature_support.py)，46742 B，SHA256：

~~~text
6c57f78a9c8b80805e8e551a8fba50a089687cea164bd192c8bead845dda29b4
~~~

其每个完整连续叶的持久化条目保有：

| 位置 | 原字段 | 本条用途 |
|---|---|---|
| 整条 | exact_radial_leaf、accurate_phi_interval、ordinal | 原全径向与全圆覆盖，不能换成有限字面角 |
| whole_cell_geometry | same_field_normal | 完整三分量 $N$ |
| whole_cell_geometry | normal_norm | 同一完整 $w$ 区间 |
| whole_cell_geometry | position_hull | 完整三维 $F$ 区间 |
| whole_cell_geometry.support | horizontal_numerator、vertical_numerator | 同场 $a,b$ 的准确区间 |
| whole_cell_geometry | raw_first_form、second_fundamental_form | 原曲率证明输入；本条不改其数学含义 |
| whole_cell_geometry | principal_curvature_absolute_upper | 现有有效全叶上界，不能被方向支持替代 |
| whole_cell_geometry | full_position_norm_upper | 原 R717 同叶整像直径责任 |

当前闭面消费者

[fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py](../scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py)，84576 B，SHA256：

~~~text
002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f
~~~

已经通过 original_leaves 重新读取完整 geometry 流及其原 header/footer、全部顺序、全输入输出字节绑定和同点 normal 分支。它当前的 impose_rows、impose_caps 与 second_pass_support 仍实现旧 $\sigma/\max(1,\beta)$ 路线。本条没有把这些已锁函数的结果改义。

一个必要的独立后继可以沿上述完整读取合同，从每条原持久化 whole_cell_geometry 计算式(12)并求共同 $\beta$；不需新 $F/J$、新根、删角或重算原32段。必须同时保留原完整根包含/唯一性/周期 glue、R722 真实均值存在与角 jet 归因、准确 scalar 与参考、当前完整点数组、137个实际科学来源、全部径向与全圆覆盖。缺任一责任时结果仍为未付。

新的证书应明确命名为“方向流支撑商”分支，并分别记录：
共同 $A_\beta,c$，$\tau,D^+$，全叶式(12)有理下界，固定帽式(19)–(20)，整面实际曲率上界，完整端口/相位来源，以及最后完整原字节重核。
原八角色消费者中关于 $\sigma\ge\tau\max(1,\beta)$ 的旧精确 claim 不能因为本条成立就被填成 true；它与本条是不同的充分条件。原支持字段、原证明来源与旧成功分支保留。

## 9. 本条已经闭合与仍须实际支付的事项

已经闭合的是：保留法向方向后的全闭面 reach 充分条件、完整法管不同偏移面的严格排序、共同 $\beta$ 的仿射叶约束、当前四固定帽的准确有理约束，以及全相位/混合点对/R718/R716的合法衔接。

仍未支付的是：当前任一实际 field 的完整 immutable snapshot、准确全域六 jet 与根/标量/积分/算术费用、完整当前相位和端口前提、共同正 $\beta$ 的实际可行性、曲率目标、原固定度量误差及最终整像幅度比例。没有从有限屏幕的改善、相同初始标量或 prepared input 推出这些事实。

本条是纸面证明和完整既有源接口说明。没有本机科学、数值 fixture、新的优化变体、额外准入步骤或已返回费用结果。
