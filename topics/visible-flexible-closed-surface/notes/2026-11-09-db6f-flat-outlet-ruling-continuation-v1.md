# 有限平坦出口的实际母线延拓与共同材料坐标回收

**状态：完整作者推导，待独立全文审查。** 2026-11-09，独立几何分工。
本文把已存在的正 C 平坦出口真正积分为一张角向闭合的曲面，
给出共同材料坐标、完整两 jet、焦集和可接范围。
不修改任何冻结稿；不读优化数组，不运行 PDE、BVP、tail、RK 或网格。

结论只延长已有的有边环带。有限正常平坦段中保持非零 II，
仅排除了用这一平坦延拓直接抹平出口的办法，
不构成一般闭曲面或含新非平段的连接不可能性。

## 1. 固定输入及其来源

可取下列已完整独审的实际新族作为输入：

- 正 C 固定 H 作者正文：[ec5093a6d7c368dfaf80855d03c5c0f19ac51afe](https://github.com/Rogerhu12/math-research/blob/ec5093a6d7c368dfaf80855d03c5c0f19ac51afe/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-epicycle-bump-fixed-h-v1.md)；
  blob 34ba5cd303512e203a22501db57b11dd4e844470。
- 实例及单调 Q 组合的完整独审：[ab158761cb5fc844d8e2da18abdca4313aed79e6](https://github.com/Rogerhu12/math-research/blob/ab158761cb5fc844d8e2da18abdca4313aed79e6/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-positive-epicycle-bump-fixed-h-v1.md)；
  本稿不是该报告已经审过的附加结论。
- 光滑角数据的实际有限平坦领：[9daa8aba8a341855811d2f1c164bfb3ca7eab0bc](https://github.com/Rogerhu12/math-research/blob/9daa8aba8a341855811d2f1c164bfb3ca7eab0bc/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-root-monotone-flat-collar-smooth-data-v1.md)，
  全文独审 15b02049c367e344901fb13264a950f8ff5bf933。

在其已存在的开平坦领内取一个固定完整材料圆周，或取已有外边界。
把该圆周的位置记为 gamma_tau(u)，u属于 T_ell。
所有时间共用同一个正数 a_0 和斜率 B>0。
选择旧径向坐标向外的方向，取入口标架 (e_1,e_2,N)，其中
N=e_1×e_2、gamma'=a_0 e_2。
记入口第二基本形式为 L,M,C，C>0。
入口已经是平坦，故 L=M^2/C。

所有输入都是实际周期位置和实际周期标架，
而不只是满足 Gauss–Codazzi 的周期系数。角导数满足

$$
\begin{aligned}
\gamma'&=a_0e_2,\\
e_1'&=B e_2+M N,&
e_2'&=-B e_1+(C/a_0)N,&
N'&=-M e_1-(C/a_0)e_2 .
\end{aligned}
\tag{1}
$$

若原族有材料 C3 对称，则上述输入也有；
参数 tau 在固定紧区间中光滑，C有统一正下界。
不从原图再移动入口，也不另加待定出口高度。
以下为了简洁暂省略 tau 下标；全部公式对每个时间同时成立。

## 2. 实际母线及其全部第一、第二形式

定义

$$
p=\frac{a_0M}{C},\qquad \lambda=\sqrt{1+p^2},\qquad
\omega=B-\frac{p'}{1+p^2},\qquad
k=\frac{C\lambda}{a_0}>0,
$$

$$
V=\frac{e_1-p e_2}{\lambda},\qquad
W=\frac{p e_1+e_2}{\lambda}.
\tag{2}
$$

这里 omega 是函数，不是旧稿的三次对称角 2pi/3。
V,W,N 是同向正交标架。由 (1) 直接求导得

$$
V'=\omega W,\qquad
W'=-\omega V+kN,\qquad N'=-kW,
\qquad
\gamma'=\frac{a_0}{\lambda}(W-pV).
\tag{3}
$$

例如 V' 的法向分量是
(M-pC/a_0)/lambda=0；其 W 分量为
B-p'/(1+p^2)，因此 (3) 没有遗漏 p' 或 lambda'。

现在对真实空间位置作显式定义

$$
G(u,s)=\gamma(u)+sV(u),\qquad
A(u,s)=\frac{a_0}{\lambda(u)}+s\omega(u),\qquad
E(u)=-\frac{a_0p(u)}{\lambda(u)}.
\tag{4}
$$

则

$$
G_s=V,\qquad G_u=E V+A W,
\qquad
I=ds^2+2E\,ds\,du+(E^2+A^2)du^2.
\tag{5}
$$

在 A>0 的入口连通分支中，G_s×G_u=A N，
所以这是一个正则浸入，其真实法向仍为 N(u)。
再由 (3)，

$$
II_{ss}=II_{su}=0,\qquad II_{uu}=A k.
\tag{6}
$$

唯一非零的主曲率因而是

$$
\boxed{\quad \kappa_{\rm par}(u,s)=
\frac{k(u)}{A(u,s)}
=\frac{C(u)\lambda(u)/a_0}
       {a_0/\lambda(u)+s\omega(u)} .\quad}
\tag{7}
$$

(4) 已给实际坐标，不只是形算子或形式解。
但 (5) 的母线坐标依赖时间，不能把它误报为各时间共同的材料坐标；
下一节完整回收共同坐标。

## 3. 内禀展开与整个圆周的坐标回收

记 rho_0=a_0/B。在通用覆盖上定义平面展开

$$
Z(u,s)=e^{iBu}
 \left\{\rho_0+s\,\frac{1-ip(u)}{\lambda(u)}\right\}.
\tag{8}
$$

对平面正交标架作与 (2) 同样的旋转，直接求导可知
(8) 的第一基本形式正是 (5)。
这里不能把 Z 当成闭合平面圆周：
Z(u+ell,s)=e^{iB ell}Z(u,s)，其旋转单值障碍恰是内禀锥角。

对 s>=0，实部 rho_0+s/lambda 严格正，所以可选定一个无歧义的角 lift：

$$
x(u,s)=\sqrt{\rho_0^2+2\rho_0s/\lambda+s^2}-\rho_0,
$$

$$
\widetilde u(u,s)=u-\frac1B
 \arctan\!\left(\frac{s p}{\lambda\rho_0+s}\right).
\tag{9}
$$

(8) 因而在这个 lift 中写为
Z=(rho_0+x)e^{iB tilde u}。
所以共同材料度量应为

$$
g_{\rm flat}=dx^2+(a_0+Bx)^2\,d\widetilde u^2.
\tag{10}
$$

现在证明 (9) 确实覆盖完整固定圆周，而不是只在一点附近可逆。
固定 x>=0，可唯一解出 s：

$$
s_x(u)=
\sqrt{\rho_0^2/\lambda(u)^2+2\rho_0x+x^2}
-\frac{\rho_0}{\lambda(u)}.
\tag{11}
$$

等价的无相消表达式为

$$
s_x(u)=
\frac{2\rho_0x+x^2}
{\sqrt{\rho_0^2/\lambda(u)^2+2\rho_0x+x^2}
 +\rho_0/\lambda(u)} .
\tag{12}
$$

沿每根母线，

$$
x_s=\frac{s+\rho_0/\lambda}{\rho_0+x},
\qquad \lambda^{-1}\le x_s\le1,\qquad
x\le s_x\le\lambda x .
\tag{13}
$$

由有向面积，(5) 与 (10) 给

$$
(a_0+Bx)\,
 \det\frac{\partial(x,\widetilde u)}{\partial(s,u)}
=A .
$$

沿 x 恒定的圆周求导便是

$$
\frac{d}{du}\widetilde u(u,s_x(u))
=\frac{A(u,s_x(u))}{(a_0+Bx)x_s}>0
\quad\text{只要 }A>0.
\tag{14}
$$

而 p、lambda、s_x 全以 ell 为周期，故该角映射满足
tilde u(u+ell)=tilde u(u)+ell。
它是度数1的严格单调圆周映射，因而是完整圆周微分同胚。
这同时证明单值逆 u=u(x,tilde u) 存在，不能只以局部 Jac不零代替全圈步骤。

给一个统一可执行的正宽度门。令整个紧时间族满足
|p|<=P、|omega|<=Omega，并记 Lambda=sqrt(1+P^2)。
只要

$$
0\le x\le h_J:=
\frac{a_0}{2\Lambda^2\max(1,\Omega)},
\tag{15}
$$

由 (13) 就有 A>=a_0/(2Lambda)>0。
所以在整个 [0,h_J]×T_ell 上，完整共同材料表达式为

$$
F^{\rm flat}_\tau(x,\widetilde u)
=
G_\tau\!\left(u_\tau(x,\widetilde u),
 s_{x,\tau}(u_\tau(x,\widetilde u))\right).
\tag{16}
$$

(14) 的统一正下界及光滑隐函数定理给联合光滑的时间依赖。
(16) 对每个时间严格诱导同一个 (10)。
门 (15) 只保证该共同坐标与浸入存在，不声称排除了所有远距离自交；
全图嵌入的正宽度见 §5。

## 4. 周期、C3、两 jet 和与旧图的真实一致

因为 gamma、V 是实际周期场，(4) 满足 G(u+ell,s)=G(u,s)。
(14) 的逆也保持 ell 的 deck 移位，所以 (16) 是真正周期的空间位置；
没有未检查的平移 monodromy。
若输入满足材料 u->u+ell/3 对应空间 R_z(2pi/3)，
则 p、lambda、omega、s_x 以 ell/3 为周期，
(14) 的角映射也保持该移位，故同一 C3 对称性传给 (16)。

在 x=0，s=0、tilde u=u。由 (9) 可得
s_x=lambda、u_x=p/a_0（这里 x 导数保持 tilde u 不变），
于是

$$
F(0,\widetilde u)=\gamma(\widetilde u),\qquad
F_x(0,\widetilde u)=e_1,\qquad
F_{\widetilde u}(0,\widetilde u)=a_0 e_2 .
\tag{17}
$$

把 (6) 变换到共同坐标，在入口有

$$
II_{xx}=C(p/a_0)^2=M^2/C=L,\qquad
II_{x\widetilde u}=Cp/a_0=M,\qquad
II_{\widetilde u\widetilde u}=C .
\tag{18}
$$

第一形式 (10) 也与旧平坦领相同。
由 Gauss 公式，(17)–(18) 恰为相同的全部 Cartesian 两 jet；
特别是实际初始高度由 gamma 给出，不可之后任选。

还有更强的开重叠唯一性，因此接合不是只有 C2。
在任意已有 C-infinity 正则平坦领中，II 秩一且非零。
取它的单位核方向 V，并取横向单位向量 W，使 S(W)=kappa W。
Codazzi 的
((nabla_V S)W)·V=((nabla_W S)V)·V
给 -kappa (nabla_V V)·W=0。
所以 nabla_V V=0，且 II(V,V)=0，空间中的 V 积分线是直线；
沿该线 N也不变。入口 C>0 使 V 的旧径向分量1/lambda>0，
故这些母线在一个完整小开领内横穿入口并形成坐标。
其初始位置、方向恰为 gamma、V，因而原图必等于 (4)，再等于 (16)。

所以 (16) 与旧图在开平坦重叠上完全相同，全部 jet 匹配。
保留旧域之后，原固定 H 的材料点与空间位置继续原样保留。

## 5. 正宽全时间嵌入及可用的 reach 范围

输入是一个固定紧时间区间上的实际光滑嵌入环带，
入口位于其平坦外领；本节证明可把整个图继续成某个统一正宽嵌入。

由 §4，公式 (16) 向 x<0 也在一个小窗内光滑并与旧图相同。
在 x=0 处 F_x、F_u 处处独立，其最小奇异值有统一正下界。
假如没有一个全时间共同的正外宽可保持嵌入，
则存在 h_j->0、时间 tau_j 和不同材料点 p_j,q_j，
其中至少一点在新宽度 h_j 中，而其空间像相同。
由紧性取子列，tau_j->tau、p_j->p、q_j->q，
极限点属于旧域闭包。
极限旧图嵌入，故 p=q，且 p 在入口圆周。

选择在该点把切平面投影到二维的固定线性投影。
其参数 Jac在 p 处可逆，联合 C1 连续性和局部逆函数定理
给时间与材料的共同邻域，其中新旧图的投影均为单射。
当 j足够大，两点都在该邻域，矛盾。
所以存在 h_E>0，使 0<=x<=min(h_J,h_E) 的拼接全图
对所有时间都是嵌入。此证明使用了真实旧图的全局嵌入，
没有把 (15) 的局部正则性偷换成全局嵌入。

这也给整个有边图的某个统一正 reach，但不提供本题3%指标。
确切地，在固定紧材料域和紧时间区间上，
局部导数的统一下界、有限 Hessian 界以及远离对角线点对的紧性，
共同给一个实际全局参数弦长下界 gamma_*>0 和 Hessian 上界 H_*<infinity。
最近点位于材料边界时，通向任一其他点的可行最短角 lift 线段
只要求一侧极小条件。Taylor 余项遂给
reach>=gamma_*^2/H_*>0。
这与此前各稿的有边证明完全同型；常数属于本次完整新域，不能移用 R45。

本稿没有把 h_E、gamma_* 或 H_* 的数值计算出来。
若想沿 (16) 走得更远，必须重新支付实际空间自交与全部时间 reach；
仅保持 A>0 不足以保证这些结论。

## 6. 焦集和有限平坦接合的准确限制

在每根母线上，若 omega不为0，Jac退化位置是

$$
s_{\rm foc}(u)=-\frac{a_0}{\lambda(u)\omega(u)}.
\tag{19}
$$

omega<0 时它在向外的正 s方向，omega>0 时在反方向；
omega=0 时该母线没有有限 Jac退化点。
当 A->0，(7) 的分子严格为正，所以非零主曲率发散。
这个焦集不能以一次参数变换掩盖为同一 C2 延拓的正常接口。

在入口连通的任一有限正常区域 A>0 中，(7) 严格为正。
若取一个有限、紧的出口曲线，入口全时间 C的正下界与分母上界
更给它的非零主曲率一个统一正下界。
因此这一纯平坦延拓不可能在有限正常出口上获得 II=0 的点或开角区。
当 omega>0，只有沿 s->infinity 才可能使 (7) 趋零；
因 |G-gamma|=s，这不是有限空间中的紧接口。
omega=0 时曲率沿该母线恒定。

R43 的指定圆周接口包含 II=0 的开角区；
其三片柱弯区域之间确有保留的平面扇区。
故当前 C>0 出口不能只通过 (16) 的有限正常平坦段
就 C2 接到该完整指定接口。结论仅限这里的实际正 C 输入与纯平坦延拓，
不排除含新非平曲率段、其他输入或不同机制的接合。

另一个独立核对是内禀 holonomy。
(10) 的平行移动绕完整材料圆周产生角 -B ell（模2pi），
即通常的锥角亏损 2pi-B ell；这里固定 (e_1,e_2) 的正向。
当前小领的 0<B ell<32·10^{-6}，不是平面环域的零 holonomy。
在一整个平坦连接环域中，同伦圆周有相同 holonomy，
所以这种小锥角也不能在纯平坦段里改成 R43 的欧氏平面角。

## 7. 由实际出口隔离出的非平桥问题

入口已经完全显式化：给定上一实际 Cauchy 图，
(16) 及其导数固定位置、标架、II和每个时间的材料对应。
它没有任何可再任选的终端平移或高度。

若继续用共同径向度量 dr^2+a(r)^2du^2、u周期ell，
而目标是半径 R的欧氏平面圆周，目标角变量必须取 theta=2pi u/ell。
还必须固定端口方向 epsilon_out=±1：它说明桥的递增 r 对应目标平面
极径增加还是减小。特别是从边界进入圆盘内部时通常是负号，不能默选正号。
因此在同一材料 gauge 中，目标应满足

$$
a_{\rm out}=\frac{2\pi R}{\ell},
\qquad
a'_{\rm out}=\epsilon_{\rm out}\frac{2\pi}{\ell}.
\tag{20}
$$

不能把旧周期2pi下的 a'=1 不经换算抄到球面弧长周期ell。
对连接环域，径向曲率积分给确切预算

$$
\int K\,dA
=-\ell\int a''\,dr
=B\ell-\epsilon_{\rm out}2\pi .
\tag{21}
$$

当 epsilon_out=+1，(21) 要求净负总曲率；当 epsilon_out=-1，
它要求净正总曲率，并且当前 B>0 的径向斜率必须发生转折。
这两个方向由真实接合布局决定，不能为了使用已有存在定理而互换。
无论哪种方向，都不是把已经平坦的出口再作更长的平坦展开。
(21) 只约束这个具有指定径向 gauge 的桥，不是任意机制的障碍定理。

实际桥接还须把 (20) 的内禀数据和 R43 全部 Cartesian 两 jet一起达到：
位置、径向切向、角向切向以及含零角区的完整 II，都由指定目标图计算；
终端不能只满足一个半径或一个曲率标量。
当前正 C 演化图在 C出现零点时还需适当的新局部表示或退化存在论证。
本文既不宣称已经解出这个边值问题，也不把它挪给数值误差。

下一可推进的实际步骤，是从 (16) 的真实平坦初值重新进入 Q=aa''>0。
原单调下降定理不适用于这一方向；角解析 CK 也不能直接接受固定 H 的光滑 bump。
一个另外研究中的方法是减去 Q=0 的标量背景后改用反向加权能量；
它须另稿完整证明和独审，未在本文预支。
即使该负曲率入口成立，也只付初始一段；它不支付 epsilon_out=-1 所需的
后续正曲率及径向转折，更不自动支付最终 C=0 角区。

## 8. 证据身份

本文为显式微分与几何证明，不包含计算数据或程序执行声明。
(3)、(5)–(7)、(9)–(14)、(17)–(18) 可逐项符号复核；
完整圆周坐标回收、实际 monodromy、开重叠和全图嵌入仍须全文审查。
来源输入的旧执行记录不充作本稿运行回执。
完整新稿冻结后保持原样，后续改动另存新版本。
