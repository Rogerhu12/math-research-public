# R680 — 全十九角的原两 jet 能量与更强混合 charge 限制

日期：2026-11-15。**状态：本文的原目标素数内必要条件已证明；指定 forcing 的非零及主课题仍未完成。**

R672 将原函数值和相对 Euler 导数的两个长零合并为一个加权根能量。
本篇不再用清分母后的矩形次数估计这个能量，而把每个实际因子的
Euler 三次 forcing 放回原十九角曲面。其准确固定极除子与因子曲线的交数至多为径向次数的八倍。
整个原来源的除子类同时是 nef，因而所有实际接触因子的共同自交由原预算准确控制。

若同一候选的 charge 全在一个模 $q$ 类，这个多项式对称把已有的两个 jet
搬到 $q$ 个互异的未吹起点；不需要新增算术零。结合重复因子的真实轨道，
得到
$$
p\le
\left(\frac{141}{8q}+\frac{12}{q^2}\right)D^2+O(D).
$$
原低 $\ell$ 临界的 $p/D^2\to47/8$ 因此排除所有 $q\ge4$。
一般混合来源取 $q=1$ 也得到比 R672 更强的统一平方根门。
最大公因数为 $1,2,3$ 的实际密支持仍未排除；本文不把这份必要限制
称为同一个修正 $R$ 的第二余类非零。

## 1. 同一实际来源及长 jet 的范围

保持 R672 的原对象
$$
p=6s-1>101,\qquad D\ge3,\qquad
f_D=\lfloor9D/2\rfloor+4<p,\qquad 1\le\ell<s-13,
$$
$$
\mathcal W_D=\bigoplus_{n=0}^{D}
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},\qquad
\mathcal E=Y\partial_Y,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,\quad
e_{n+1}=f_n-3A_n-B_n+C_n.
\tag{1}
$$
这是 canonical $T$ 次数为零的真实来源；不将另含 $T^j$ 的较大格免费并入。

取非零原约化 $\bar P$，置
$$
\widehat P=d^{C_D}\bar P,\qquad
r=\operatorname{ord}_t\widehat P,\qquad
M_D=f_D+C_D=5D+4-(D\bmod2).
$$
全部原角帽给
$$
\deg_Y\widehat P\le D,\qquad
\deg_t\widehat P\le M_D.
\tag{2}
$$
如 R672，令
$$
(\Delta,H)=
\begin{cases}
(0,s),&\bar P\in\ker\bar J,\\
(13,s-13),&\bar P\in\ker\bar M.
\end{cases}
\tag{3}
$$
保原 $P_{134}/U_0$ 和两个十三行带，准确得到
$$
\widehat P(t,g),\quad
(\mathcal E\widehat P)(t,g)\in t^Hk[[t]],
\qquad g\equiv\rho=(1+8t)\Theta^{17}\pmod{t^s}.
\tag{4}
$$
三个原块的常数观察在原允许的 $n=0,1,2$ 上给单位 Vandermonde，
仍迫
$$
1\le r\le M_D.
\tag{5}
$$
真正 primitive 模 $p^2$、模 $p^3$ 核由 R449 必须先在 $\ker\bar J$ 内，
故须用较强的 $\Delta=0$，不是只用 $\Delta=13$。

若 $r\ge H$，已有
$$
p\le6(M_D+\Delta)-1.
\tag{6}
$$
以下保 $r<H$，记 $S=H-r>0$。只用原低轴的模 $t^s$ 数据，
不将原 ODE 延长到其真实共振之后。

## 2. 整个原角线性系是 nef

使用 R495/R555 的同一光滑曲面
$\pi:X\to\mathbb F_4$。负截面 $S_0$ 满足 $S_0^2=-4$，底纤维类为 $F_0$。
在 $0,h_7$ 两根的 $Y=\infty$ 各有四步链，
在 $(1,\infty)$ 有三步链，在 $d=0,Y=0$ 和底无穷远各有两步链。
记每一步的全变换例外类为 $E_{\alpha,j}^*$；它们是交数计算的正交例外基。

置 $c_D=C_D$、$u_D=2c_D+4$。R555 已准确识别
$$
H^0(X,\mathcal O_X(\mathcal B_D))
=d^{c_D}\overline{\mathcal W}_D,\qquad
\mathcal B_D=
D S_0+(u_D+4D)F_0-\sum_{\alpha,j}\mu_{\alpha,j}(D)E_{\alpha,j}^*.
\tag{7}
$$
原十九个重数完整为：

| 链 | $D$ 的余类 | 重数 |
|---|---|---|
| 每条四步链，$D=4a+r$ | $r=0$ | $(a,a,a-1,a-1)$ |
| 同上 | $r=1$ | $(a,a,a,a-1)$ |
| 同上 | $r=2$ | $(a,a,a,a)$ |
| 同上 | $r=3$ | $(a+1,a,a,a)$ |
| 三步链，$D=3a+r$ | $r=0$ | $(a,a,a-1)$ |
| 同上 | $r=1$ | $(a,a,a)$ |
| 同上 | $r=2$ | $(a+1,a,a)$ |
| 每条两步链 | 全部 | $(c_D,c_D)$ |

因此
$$
\boxed{\mathcal B_D^2
=4D^2+2D u_D-\sum_{\alpha,j}\mu_{\alpha,j}(D)^2
=\frac{47}{12}D^2+O(D).}
\tag{8}
$$
有限参数使用左侧准确整数，不先舍掉取整项。

**引理 1。** 对全部 $D\ge3$，$\mathcal B_D$ 为 nef。

**证明。** 先定义固定有理类
$$
B_\infty=S_0+5F_0
-\frac14\sum_{\text{三条四步链}}E_{\alpha,j}^*
-\frac13\sum_{\text{三步链}}E_{1,j}^*
-\frac12\sum_{\text{两条两步链}}E_{\alpha,j}^*.
\tag{9}
$$
有 $B_\infty^2=47/12$。

考虑非垂直、非两截面的几何整曲线 $C$。
其原多项式方程 $F=\sum_{i=0}^b f_i(t)Y^i$ 可取为 primitive，
且 $b\ge1$、$f_0\ne0$；置 $u=\max_i(\deg f_i-4i)$。
R495 的全部角公式给
$$
C\sim bS_0+(u+4b)F_0-\sum\mu_{\alpha,j}(F)E_{\alpha,j}^*.
$$
记原末 Gauss 值为 $v_0,v_{h_1},v_{h_2},v_1,v_d,v_\infty$。
各链总重数分别为
$$
b+v_0,\ b+v_{h_1},\ b+v_{h_2},\ b+v_1,\ v_d,\ 2u+v_\infty.
$$
系数 primitive 给 $v_0,v_{h_1},v_{h_2},v_1\le0$；
非零 $f_0$ 给
$$
v_d+v_\infty
\le2\operatorname{ord}_d f_0-2\deg f_0\le0.
$$
直接相交便得
$$
B_\infty C=
\frac{47}{12}b
-\frac14(v_0+v_{h_1}+v_{h_2})
-\frac13v_1-\frac12(v_d+v_\infty)
\ge\frac{47}{12}b.
\tag{10}
$$

$\mathcal B_D-D B_\infty$ 的纤维部分是 $(u_D-D)F_0$，
其系数为偶数 $D$ 时四、奇数 $D$ 时三。
在上表中，$\mu_{\alpha,j}(D)-D\alpha$ 的正值仅可能是：

- 每条四步链的第一项在 $D\equiv3\pmod4$ 时为 $1/4$；
- 三步链的第一项在 $D\equiv2\pmod3$ 时为 $1/3$。

这里 $\alpha$ 分别为 $1/4,1/3,1/2$。
每个这样的第一中心的曲线重数不超过 $b$，因为至少一个系数是角单位。
故
$$
(\mathcal B_D-D B_\infty)C
\ge(3-3/4-1/3)b=\frac{23}{12}b.
\tag{11}
$$
这处理了全部非边界曲线。

剩余边界曲线逐条读取原表。四步链所在严格纤维的交数为二，
三步链纤维为一，两条两步链纤维为 $D-2c_D\ge0$；
其他纤维的交数为 $D$。
第 $j$ 个非末例外曲线为
$E_{\alpha,j}^*-E_{\alpha,j+1}^*$，交数为
$\mu_{\alpha,j}-\mu_{\alpha,j+1}\ge0$；末例外交数也非负。
严格负截面只穿过两条两步链的第一中心，交数为
$u_D-2c_D=4$。
严格正截面只穿过三个四步链及一个三步链的第一中心，交数为
$$
u_D+4D-3A_D-B_D>0.
$$
式中最后 $B_D=\lfloor(D+1)/3\rfloor$ 是角指数，勿与除子
$\mathcal B_D$ 混同。
所有不可约曲线均已覆盖，所以 $\mathcal B_D$ nef。证毕。

**引理 2。** 每个上述非垂直、非截面的几何整曲线 $C$ 也为 nef。

**证明。** R495 的规范式不要求 $C$ 在 $(0,1)$ 光滑：
$$
-K_XC=2b-(v_0+v_{h_1}+v_{h_2}+v_1+v_d+v_\infty)\ge2b.
$$
整 Cartier 曲线的算术亏格非负，伴随公式给
$$
C^2\ge-K_XC-2\ge2b-2\ge0.
\tag{12}
$$
$C$ 与任何不同的不可约曲线交数非负；连同 (12) 即得 nef。
这里只用交数，不从本引理推断任何物理评价像饱和。证毕。

## 3. Euler 三次 forcing 的准确固定极除子

取上述曲线 $C$ 的 primitive 方程 $F$，$1\le b=\deg_YF<p$。
沿用同一原算子
$$
\delta_t=t\partial_t,\quad e=\mathcal EF,\quad a_0=\delta_tF,
$$
$$
A=6(1-t),\quad B=-(1+2t),\quad
\mathcal R=\frac{t(154+160t+1792t^2)}{3d^2}.
$$
R514 的实际 Euler 三次多项式为
$$
\begin{aligned}
K_F^{E}={}&e^3\mathcal R
+A e^2\delta_t^2F
-2A e a_0\mathcal E\delta_tF\\
&+A a_0^2\mathcal E^2F+B e^2a_0.
\end{aligned}
\tag{13}
$$
它允许显示的 $d^2$ 分母；本节不先乘新增三 charge。

对任一角链置
$$
D_\alpha=\sum_{j=1}^{e_\alpha}E_{\alpha,j}^*.
$$
若用严格例外曲线表示，$D_\alpha$ 在第 $j$ 个严格例外上的系数是 $j$。
令 $F_d,F_\infty$ 为底 $d=0$、底无穷远的纤维，定义
$$
\boxed{
L=\pi^*F_\infty+2\pi^*F_d+2D_{h_1}+2D_{h_2}+D_1.}
\tag{14}
$$

**引理 3（完整十九角极帽）。**
在原多项式平凡化中，准确有
$$
\boxed{K_F^{E}\in H^0(X,\mathcal O_X(3C+L)).}
\tag{15}
$$
并且
$$
\boxed{
L\cdot C=3b+2V^{(h_1)}_4(F)+2V^{(h_2)}_4(F)+V^{(1)}_3(F)
\le8b.}
\tag{16}
$$

**证明。** 在 $\mathbb F_4$ 上，$\mathcal E$、$\delta_t$
在原 $F$ 的线束框内均只加正规零阶项，不增加斜次数。
(13) 的系数仅在 $d=0$ 有至多二重极、在底无穷远有至多一重极。
故 ambient 极帽为 $3C_0+F_\infty+2F_d$，
其中 $C_0$ 是原曲线闭包。

现在逐一检十九个累计条件。有限角取 $z=t-\alpha$，
$x=1/Y$（正截面链）或 $x=Y$（负截面链），第 $j$ 个图为
$z=x^jz_j$。$\mathcal E$ 是对 $x,z_j$ 的对数向量场，
不损累计角阶。若 $\alpha\ne0$，$\delta_t$ 的非正规部分
至多是单位倍 $x^{-j}\partial_{z_j}$，
每次最多损 $j$ 阶；若 $\alpha=0$，它为 $z_j\partial_{z_j}$，
不损角阶。在 $t=1$，二次导数前的 $A$ 具有 $j$ 阶零；
在 $d=0$，$\mathcal R$ 的极和二次导数损失均至多 $2j$。
因此相对 $3C$ 的可能累计损失准确被下表覆盖：

| 原链 | 全部中间 $j$ | 极阶上界 |
|---|---:|---:|
| $0,Y=\infty$ | $1\le j\le4$ | $0$ |
| 两个 $h_7$ 根，$Y=\infty$ | $1\le j\le4$ | $2j$ |
| $1,Y=\infty$ | $1\le j\le3$ | $j$ |
| $d=0,Y=0$ | $1\le j\le2$ | $2j$ |
| 底无穷远 | $1\le j\le2$ | $j$ |

最后一行也须在正确框内计算。
令 $T=1/t,Z=t^4Y$，原方程框为
$T^uF(T^{-1},T^4Z)$。有
$$
\delta_t=-T\partial_T+4Z\partial_Z,\qquad
\mathcal E=Z\partial_Z.
$$
代入 $T=Z^jT_j$ 后仍是对数向量场；
线束框只贡献正规常数项，所以导数本身不损阶。
(13) 的有理系数在 $T=0$ 至多一重极，恰给第 $j$ 例外上的 $j$ 阶。

(14) 在这些严格例外上的系数正好覆盖上表：
$\pi^*F_\alpha$ 在该链第 $j$ 个例外上的系数也是 $j$。
同时 $F_\infty+2F_d$ 覆盖两个严格纤维上的实际极。
其他素除子处没有极。光滑面的线束截面按素除子检正规性，
因此这些相容框计算支付了 (15)，而非只支付最终 Gauss 半空间。

最后，$\pi^*F_\alpha\cdot C=b$，
$D_\alpha\cdot C=\sum_j\mu_{\alpha,j}(F)=V_{e_\alpha}(F)$。
primitive 系数给 $V^{(h_i)}_4=b+v_{h_i}\le b$、
$V^{(1)}_3=b+v_1\le b$，故 (16) 成立。证毕。

(15) 是原 forcing 的几何极帽，不是将它塞进原同预算 $\mathcal W_D$。
若要将 (13) 用作被原真左行杀掉的实际来源，仍须支付 R514 的
三 charge 返回或该篇明确的同 $D$ 缓冲条件；本篇没有删除那些成本。

## 4. 原 ODE、完整判别式及每个接触点的能量

仍用 R467 的原二阶方程
$$
\mathscr D(\psi)=A_0(\psi\psi''-(\psi')^2)
+B_0\psi\psi'-C_0\psi^2,
$$
$$
A_0=6t(1-t)d^2,\quad B_0=(5-8t)d^2,\quad
C_0=(154+160t+1792t^2)/3.
\tag{17}
$$
若 $\zeta\ne0$ 为常数，则
$\mathscr D(\zeta\rho)=\zeta^2\mathscr D(\rho)$；
故同一个低轴方程在每个 $(0,\zeta)$ 仍有效至原长度。

设 $F$ 经过某个 $(0,\zeta)$，并令 $\psi$ 为该点的 tame 单位分支。
它的局部分裂域是 tame，因为 $b<p$ 且其 Galois 群嵌入 $S_b$。
R467 的整数幂投影共振也对任意非零常数项成立：
若 $\mathscr D(\psi)=0$，则 $\psi'/\psi-8/d$ 的正规整数幂部分满足
$$
v_0=34/15,\qquad(6n+5)v_n=(6n+2)v_{n-1},
$$
在 $n=s-1$ 处矛盾。
所以 $\mathscr D(\psi)\ne0$。

记 R467 的隐式多项式为 $K_F^{\rm std}$，
使沿 $C$ 有
$$
K_F^{\rm std}(t,\psi)=F_Y(t,\psi)^3\mathscr D(\psi).
$$
R514 的原 Euler 写法与它有准确关系
$$
\boxed{
K_F^E|_C=-\frac{tY}{d^2}K_F^{\rm std}|_C.}
\tag{18}
$$
确实，若
$\mathcal P=6(1-t)\delta^2-(1+2t)\delta$，则
$$
\mathcal P\log\psi-\mathcal R
=\frac{t}{d^2}\frac{\mathscr D(\psi)}{\psi^2},
\qquad
K_F^E|_C=(YF_Y)^3(\mathcal R-\mathcal P\log\psi).
$$
这证明 (18)，包括其单位和额外一份 $t$。

设该点的完整 Hensel 因子有根 $\psi_j$，置
$$
h_j=\operatorname{ord}_t(\psi_j-\zeta g),\qquad
\bar h_j=\min(h_j,s).
$$
R467 只在原截止内给
$\operatorname{ord}\mathscr D(\psi_j)\ge\bar h_j-1$。
(18) 的一份 $t$ 准确补回这一个损失。
若 $\Delta_{F,\zeta}$ 为整个 Hensel 因子的判别式赋值，则
$$
\boxed{
I_{(0,\zeta)}(C,K_F^E)
\ge\sum_j\bar h_j+3\Delta_{F,\zeta}.}
\tag{19}
$$
这里 $Y,d$ 为单位；全部 $F_Y$ 的总阶就是完整判别式阶。
式 (19) 适用于奇异点、切向 Puiseux 根和任意 $h_j\ge s$；
没有把 $F_Y$ 当单位，也没有将 ODE 延长过 $s$。
$t$ 阶按根的全部 tame 共轭求和，准确等于局部交数。

(18) 及共振还保证 $K_F^E$ 在 $C$ 上不恒零。
因此 (15) 的非零限制具有总零长度
$$
C\cdot(3C+L)=3C^2+L\cdot C.
\tag{20}
$$
对任何若干互异 $(0,\zeta)$，(19) 的左侧可相加，且不超过 (20)。

## 5. 同余支持给 q 个真实 jet；全因子共同交数

假定 $\widehat P$ 的非零 charge 至少有两个。
若它们全同余模 $q$，$1\le q\le D<p$，则
$$
\widehat P(t,\zeta Y)=\zeta^{n_*}\widehat P(t,Y)
\quad(\zeta\in\mu_q),\qquad
n_*=\min\{n:\widehat P_n\ne0\}.
\tag{21}
$$
由同一个 (4)，对所有 $\zeta\in\mu_q$，
函数值及 $\mathcal E$ 值都在轴 $Y=\zeta g(t)$ 上消到 $H$。
$q$ 个点 $(0,\zeta)$ 互异，且全部避开十九个吹起中心。
这是 (21) 的实际多项式恒等式，不是给第二分支或新来源添加中央零。

在代数闭剩余域分解所有经过这些点的不可约因子，置
$$
\mathscr C=\sum_i m_i C_i,\qquad
B_{\rm ct}=\sum_i m_i b_i,\qquad
m_{\max}=\max_i m_i.
\tag{22}
$$
$C_i$ 为严格变换，$b_i=\deg_YF_i\ge1$；
不计垂直因子和 $Y=0$。这些因子在 $\widehat P$ 中的真实重数为 $m_i<p$。
去掉 $t^r$ 和各点处的单位后，两个 jet 均具有长度 $S=H-r$。

在每个 $(0,\zeta)$ 应用 R672 的加权根引理，其同一个量至少为 $4S$。
在每个不可约因子内部，(19) 的
$3\Delta=6\sum_{j<k}\operatorname{ord}(\psi_j-\psi_k)$
准确支付内部根对。不同因子的根对由各点局部交数支付，
而不同点的交数和不超过全局 $C_iC_j$。
给内部项乘 $m_i^2$，交叉项乘 $6m_im_j$，相加便得
$$
\begin{aligned}
4q(H-r)
&\le\sum_i m_i^2(3C_i^2+L C_i)
 +6\sum_{i<j}m_im_j C_iC_j\\
&=\boxed{3\mathscr C^2+\sum_i m_i^2 L C_i}\\
&\le3\mathscr C^2+8m_{\max}B_{\rm ct}.
\end{aligned}
\tag{23}
$$
重复因子保持在 $m_i^2$ 中；未将同一根复制为不同根后丢掉判别式。

每个 $C_i$ 由引理2为 nef，故 $\mathscr C$ nef。
由于 $\widehat P$ 是 (7) 的真实截面，存在有效余除子
$$
\mathcal B_D\sim\mathscr C+\Delta_P,\qquad \Delta_P\ge0.
$$
$\Delta_P$ 包含全部垂直含量、截面、其余因子和十九角余量。
引理1遂给
$$
\boxed{
\mathcal B_D^2-\mathscr C^2
=(\mathcal B_D+\mathscr C)\Delta_P\ge0.}
\tag{24}
$$
这是同一个实际截面的比较；没有根据维数补出任何因子。

还须保 (21) 对真实重复次数的限制。$\mu_q$ 置换所有接触因子，
且同一轨道上的重数相同。若某个因子的轨道长为 $l$，
其稳定子阶为 $h=q/l$。
将该 primitive 因子写为 $F_i$，它有非零常数 $Y$ 系数。
稳定子满足 $F_i(t,\zeta Y)=c_\zeta F_i(t,Y)$；
比较常数系数迫 $c_\zeta=1$。
故它的全部 $Y$ 次数均为 $h$ 的倍数，特别 $b_i\ge h$。
整个轨道的径向次数至少为 $lb_i\ge q$。
因此准确有
$$
\boxed{
B_{\rm ct}\le D-n_*,\qquad
m_{\max}\le\left\lfloor\frac{D-n_*}{q}\right\rfloor.}
\tag{25}
$$
这里使用实际因子轨道，未假设因子无重复或分别位于一个自由矩形。

## 6. 有限参数定理及平方根临界

**定理 4。** 在 (1)–(5) 的原非零核中，若 charge 全同余模 $q$，
且 $r<H$，则
$$
\boxed{
4q(H-r)\le
3\mathscr C^2+\sum_i m_i^2 L C_i
\le3\mathcal B_D^2+8m_{\max}B_{\rm ct}
\le3\mathcal B_D^2+
8(D-n_*)\left\lfloor\frac{D-n_*}{q}\right\rfloor.}
\tag{26}
$$
优先使用已知真实因子的第一个界；最后一个界完全由原预算给出。
若只有一个 charge，则如 R672 必落入 (6)。

利用 $r\le M_D$、$p=6s-1$，(26) 特别给
$$
\boxed{
p\le6(M_D+\Delta)-1+
\frac{9}{2q}\mathcal B_D^2+\frac{12D^2}{q^2}.}
\tag{27}
$$
$r\ge H$ 时 (6) 更强，所以 (27) 也是统一必要上界。
所有取整均可先用 (8)、(26) 的准确整数处理。

由 (8)，对全部 $q\ge1$ 统一有
$$
\boxed{
p\le
\left(\frac{141}{8q}+\frac{12}{q^2}\right)D^2+O(D).}
\tag{28}
$$
特别，任意原非零两长 jet 核的序列必须满足
$$
\boxed{
D\ge\left(\sqrt{\frac8{237}}-o(1)\right)\sqrt p.}
\tag{29}
$$
这加强 R672 的 $\sqrt{2/99}$，仍未达到实际维数临界。

考虑真实低 $\ell$ 序列
$$
2s+\ell=\dim\mathcal W_D+o(D^2),\quad
\ell=o(D^2),\quad
\dim\mathcal W_D=\frac{47}{24}D^2+O(D).
$$
于是 $p/D^2\to47/8$。对 $q\ge4$，
$$
\frac{141}{8q}+\frac{12}{q^2}
\le\frac{141}{32}+\frac{12}{16}
=\frac{165}{32}<\frac{47}{8}=\frac{188}{32}.
\tag{30}
$$

**推论 5。** 在这样的实际非零核序列中，充分大时，
原非零 charge 差的最大公因数只能为 $1,2,3$。
此结论对 $K_1(M)$ 的 $\Delta=13$ 仍成立；
对真正第二、第三提升核须用 $\Delta=0$ 的更强准确条件。

若实际接触因子重数有固定上界，(23) 的第二项仅为 $O(D)$，
其主系数进一步变为 $141/(8q)$。
但 $q=3$ 此时恰等于 $47/8$，仍不能凭主项排除。
一般 $q=3$ 的 (28) 系数是 $47/8+4/3$，
所以本篇没有将最大公因数为三的候选也删掉。

## 7. 保留同一修正和真实未解范围

本篇每一步使用同一个原 $\widehat P$、真实角线性系 (7) 和原低轴。
(21) 的 $q$ 个 jet 仅来自这个多项式的支持对称。
它们不赋新的完整中央条件，不给任意因子或幂新的算术意义。
(15) 的较小几何极帽也没有将 $K_F^E$ 免费作为原被测列；
若后续把它与实际左行相配，R514 的来源返回成本继续保留。

对没有被 (26) 排除的候选，R651/R593/R608 的同一个 $R$、
全部低行右逆的高尾、两个十三行门、$Z^+$、活 $U_1/p$ 和真正 $d_2$
均仍须联立。没有从 $\mathcal B_D$ nef、来源有限自由或因子返回
推出原物理像饱和。$\ker\bar J$ 在这里只是 primitive 第二核的必要条件，
并未被认作充分条件。

新的密支持范围已经缩到 charge 差最大公因数为 $1,2,3$。
这些候选仍可混合多个模十二块；其
$U-1$ 的实际 regular 高尾、原有序前缀和同 $R$ 的第二 forcing
不由 (26) 判定。本文不以有限素数扫描替代该剩余比较。

## 依赖

- [R672](R672-original-two-jet-weighted-root-energy-and-charge-congruence.md)：
  原两 jet、最近根截断、重复因子和正特征导数首项的加权根引理。
- [R467](R467-tame-branch-contact-and-all-factor-degree-barrier.md)：
  同一原 ODE、tame 共振及完整判别式。
- [R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)、
  [R555](R555-whole-original-linear-system-and-nonzero-high-contact-forcing.md)：
  原十九次吹起、全部角重数和全来源线性系。
- [R514](R514-cubic-forcing-return-and-actual-mirror-tail-normal-form.md)：
  同一 Euler 三次 forcing 及不可删除的真实来源返回成本。
- [R449](R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)、
  [R651](R651-original-higher-critical-branch-lift-and-complete-second-forcing.md)：
  primitive 核范围及同一原修正的完整下一精度。

本篇为全参数几何与局部代数证明，不新增目标素数扫描或未运行的证书。
