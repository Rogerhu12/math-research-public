# 平坦带完整物理宽度的圆柱投影嵌入证书

作者：Astra-visible-flex-78718bd0 / root，2026-11-10。

**状态：已给完整条件证明，待未参与此证明者审查。**
本稿接 R71 的真实浸入，给可由入口函数及其一次导数核验的全宽度
全局嵌入条件。没有声称当前数值候选已经满足这些条件，也没有由此
声称闭面或 reach 下界。这里的所有条件都针对完整函数，不是采样点。

## 1. 同一个实际直纹浸入

保 R71 的全部假设和符号，特别是同一个固定
$a(s)=a_0+cs>0$、$0\le s\le S$、正平方根和 $J>0$。
其特征坐标中的位置是
$$
X(s,\xi)=\gamma(\xi)+\ell(s,\xi)e(\xi),
\qquad \ell(0,\xi)=0,\quad \ell_s=a/t\ge1.
\tag{1}
$$
这里 $e=e_0$ 是单位向量，$\gamma=\gamma_0$；物理参数浸入
$F(s,u)=X(s,\Xi(s,u))$ 已由 R71 证明为 $C^2$。
坐标变换是全局微分同胚，因此 $F$ 与 $X$ 的单射性等价。

选一个固定单位向量 $v$ 及其垂直平面中的一个定向正交基。
写 $z=\langle x,v\rangle$，$x_h\in\mathbb R^2$ 为相应水平分量。
额外假设某个常数 $\nu>0$ 满足
$$
e_z(\xi)=\langle e(\xi),v\rangle\ge\nu
\quad\hbox{对全部 }\xi.
\tag{2}
$$
若已知 $0\le\ell\le L_*$，则实际曲面全部高度位于
$$
I=[\min\gamma_z,\ \max\gamma_z+L_*].
\tag{3}
$$
例如 R71 的实域充分门给一个有效选择
$$
L_*={S a_{\max}\sqrt{1+B_0^2}\over h_*}.
\tag{4}
$$
只需一个严格足够大的区间；不要求式(3)的端点是曲面的实际极值。

由入口数据定义真正周期 $C^1$ 函数
$$
q={e_h\over e_z},\qquad A=\gamma_h-\gamma_z q,
\qquad P(z,\xi)=A(\xi)+zq(\xi).
\tag{5}
$$
每条实际直纹在它的高度 $z=\gamma_z+\ell e_z$ 上，水平位置恰为
$P(z,\xi)$。式(5)也在整个 $I\times S^1$ 上定义；某些这样的点不必
属于原有限带，这不妨碍下面的全域充分条件。

## 2. 精确投影判据

假设对全部 $(z,\xi)\in I\times S^1$，
$$
P(z,\xi)\ne0,\qquad
\det(P(z,\xi),P_\xi(z,\xi))>0,
\tag{6}
$$
并且对某个 $z_*\in I$，闭曲线 $P(z_*,\cdot)$ 绕原点的次数为一。
则 $F$ 是**整个给定宽度** $[0,S]\times S^1$ 上的 $C^2$ 嵌入。

**证明。** 式(6)的非零性给沿 $z\in I$ 的无零同伦，故每个高度
的绕数都是一。其角度 lift 满足
$$
\theta_\xi={\det(P,P_\xi)\over |P|^2}>0,
\qquad \theta(\xi+2\pi)=\theta(\xi)+2\pi.
\tag{7}
$$
所以对于每个固定 $z$，$\xi\mapsto\arg P(z,\xi)$ 是圆的保向微分
同胚，特别地 $P(z,\cdot)$ 单射。

若 $X(s,\xi)=X(\widetilde s,\widetilde\xi)$，它们的高度相同。
在该高度用刚证的单射性得到 $\xi=\widetilde\xi$（模 $2\pi$）。
然后由
$$
\partial_s z(s,\xi)=e_z(\xi)\ell_s(s,\xi)\ge\nu>0
\tag{8}
$$
得到 $s=\widetilde s$。因此 $X$，从而 $F$ 全局单射。R71 已付浸入
和 $C^2$ 正则性；紧致域到 Hausdorff 空间的连续单射是到像的同胚，
故这确为带边 $C^2$ 嵌入。证毕。

式(6)的行列式是高度的准确二次多项式：
$$
\det(P,P_\xi)=\det(A,A')+
z\{\det(A,q')+\det(q,A')\}+z^2\det(q,q').
\tag{9}
$$
因此可用完整入口的区间包围和一个有限高度区间验证；(9) 没有把
非线性源或角向尾项截断。若只有有限模近似，仍必须包围全部遗漏误差。

## 3. 无需另算绕数的一个宽裕充分门

设某个 $R>0$ 对全部 $I\times S^1$ 满足
$$
\begin{aligned}
|P(z,\xi)-R(\cos\xi,\sin\xi)|&\le R/4,\\
|P_\xi(z,\xi)-R(-\sin\xi,\cos\xi)|&\le R/4.
\end{aligned}
\tag{10}
$$
则式(6)与绕数条件都成立，而且
$$
{3R\over4}\le |P|\le {5R\over4},\qquad
\det(P,P_\xi)\ge {7R^2\over16},\qquad
\theta_\xi\ge {7\over25}.
\tag{11}
$$

**证明。** 半径界由三角不等式。写 $r=(\cos\xi,\sin\xi)$、
$P=Rr+E$、$P_\xi=Rr'+G$，用 $\det(r,r')=1$ 和
$|\det(x,y)|\le|x||y|$，得
$$
\det(P,P_\xi)\ge R^2-R|E|-R|G|-|E||G|
\ge {7R^2\over16}.
$$
线性同伦 $Rr+\lambda E$（$0\le\lambda\le1$）距原点至少 $3R/4$，
所以对每个 $z$ 绕数都是一。再除以 $|P|^2\le25R^2/16$ 得角导数界。
证毕。

这里 $R$ 只是此投影证书的参考半径，不用它重定义整个曲面直径 $D$。
若所选入口角坐标不适合式(10)，可直接用式(6)–(9)，不改变原度量。

## 4. 全宽度分离的一个有效副结论

在(10)下，定义 $q_*:=\sup_{\xi}|q(\xi)|$，可取
$q_*\le\sqrt{1-\nu^2}/\nu$。设 $d_{S^1}(\xi,\eta)$ 是入口标号圆上
取值于 $[0,\pi]$ 的最短角差。对于同一个高度 $z\in I$，有
$$
|P(z,\xi)-P(z,\eta)|\ge
{21R\over50\pi}\,d_{S^1}(\xi,\eta).
\tag{12}
$$
事实上，两条入口圆弧的角像长度各自至少为其长度的 $7/25$ 倍；
故两个水平向量之间的最短角差至少为 $7d_{S^1}/25$。
用半径下界 $3R/4$ 及 $\sin(x/2)\ge x/\pi$（$0\le x\le\pi$）即得(12)。

对任意两个实际点 $X=X(s,\xi)$、$Y=X(\widetilde s,\eta)$，
其高度记为 $z,\widetilde z$。在虚拟共同高度 $z$ 使用(12)，再用
$P(z,\eta)-P(\widetilde z,\eta)=(z-\widetilde z)q(\eta)$，得到
$$
d_{S^1}(\xi,\eta)\le C_\xi|X-Y|,
\qquad C_\xi={50\pi(1+q_*)\over21R}.
\tag{13}
$$
若还记 $Z_*:=\sup_{s,\xi}|\partial_\xi z(s,\xi)|<\infty$，由(8)和
相同高度的三角不等式可得
$$
|s-\widetilde s|\le\nu^{-1}(1+Z_*C_\xi)|X-Y|.
\tag{14}
$$
其中 $Z_*$ 只用入口一次导数，因为
$z_\xi=\gamma_z'+\ell_\xi e_z+\ell e_z'$，而
$\ell_\xi=k(1-J)$、$e'=(c-b_0'/(1+b_0^2))w_0$ 已由 R71 显式给出。
这些不等式提供不同直纹与大参数间隔的有效分离，不声称其常数最优。

## 5. 连续族与未支付之处

对 R71 的同度量连续族，若同一个 $v,I,\nu,R$ 满足上述统一门，
则每个族参数都给完整宽度的嵌入；$C^2$ 连续性由 R71 保留。
这里无需从有限多个时间样本推全时间性质。

仍须用实际入口及其严格误差界支付(2)、(6)或(10)。现有有限数值曲线
本身不构成精确入口。此证书没有处理相邻非平 ramp 的存在、不同片
之间的分离、带边法向锥或整个闭面的 reach，也不解除原终门或 G5。

依赖：[R71](../results/R71-flat-strip-exact-global-angle-propagation.md)。
本稿为纸面证明，未运行新的数值或 PDE 程序。
