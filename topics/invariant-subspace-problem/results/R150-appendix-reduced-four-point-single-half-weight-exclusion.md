# R150 附录：四个不同支点的单点半权分割全部排除

日期：2026-11-13（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明。** 对原非割线均值、第三矩本质三维、外均值且四个物理支撑点互异的完整临界点，任何一个中央权都不能等于 $1/2$。结合此前已经证明的降秩与有基点排除，剩余四点类只能有唯一的 $2+2$ 半权分割。本稿不把这个最后类型判为存在或不存在。

## 1. 当前原截面与中央节点

由[全部外均值降秩排除](R150-appendix-no-secant-cuspidal-companion-and-outer-mean-rank-drop-exclusion.md)，本稿假设下 $H$ 必秩四。再由[四不同支点有基点整类排除](R150-appendix-reduced-four-point-basepoint-critical-section-is-empty.md)，原四维物理投影无基点。令
$$
E=\operatorname{span}\{u_0,u_1,u_2,u_3\}=W\oplus\mathbb Cy,
$$
其中各 $u_i$ 是不同的物理曲线代表。原 $\lambda|_W=0,\lambda(y)=1$ 在所有 $u_i$ 上均非零；按同一 $\lambda$ 归一，可令
$$
\lambda(u_i)=1,\quad
y=\sum_{i=0}^3w_i u_i,\quad
H=\frac14\sum_iw_i u_i^2,\quad
V=\frac18\sum_iw_i u_i^3,
\quad w_i\ne0,\quad\sum_iw_i=1.
\tag{1.1}
$$
所有权都是复数，归一化仅改变各物理代表的非零比例。第三普通矩是
$$
T_3(x)=\frac12\sum_iw_i(x_i-\mu)^3,\qquad
\mu=\sum_iw_i x_i,
\tag{1.2}
$$
定义在 $E^*/\mathbb C\lambda$ 上。

已经支付的原几何是：四维像是无基点的非退化五次曲线；原二阶梯度给非零二次关系 $N$，其秩至少三；$[\lambda]$ 是该二次曲面的光滑点；从该点投向三维本质空间后，得到双有理不可约普通节点三次曲线。三个投影五次式的共同因子准确为二次式 $G$。这些结论保留同一原 $K,H,V,\lambda$，并非另选一个二次曲面。

假设某个权等于 $1/2$，重编号使 $w_0=1/2$。令
$$
\varepsilon=(1,-1,-1,-1)\in E^*.
$$
于是 $\sum_iw_i\varepsilon_i=0$、$\varepsilon_i^2=1$。中央三次的节点正是 $[\varepsilon]$ 在 $E^*/\mathbb C\lambda$ 中的像；直接从 (1.1) 可核
$$
T_3(\varepsilon,\varepsilon,\cdot)=0,\qquad
T_2(\varepsilon,\varepsilon)=-1/2.
\tag{1.3}
$$
本稿研究通过中心与这个节点方向的直线
$$
\ell=\mathbb P\operatorname{span}\{\lambda,\varepsilon\}\subset\mathbb P(E^*).
$$

## 2. 一般引理：节点纤维直线不能包含在原二次曲面中

**引理。** 设 $\Phi:\mathbb P^1\to\mathbb P^3$ 由四个无共同因子的独立二元五次式给出，像落在秩至少三的二次曲面 $Q$ 上。设 $\lambda\in Q$ 光滑，从 $\lambda$ 投影后的三个五次式有准确二次公因子 $G$，除去后给不可约普通节点三次曲线的双有理参数化。则由 $\lambda$ 和该节点方向确定的纤维直线 $\ell$ 不包含于 $Q$。

**证明。** 取平面中两个独立线性式，使它们的共同零点就是节点。它们在三次参数化上的共同因子准确为节点的两个不同原像，各一次；这是普通节点的两条光滑局部分支。乘回 $G$ 后，两个拉回的五次式具有准确四次公因子 $J$。所以任意一组 $\ell$ 的线性定义方程，其拉回可经可逆组合写为
$$
J a,\qquad J b,
\tag{2.1}
$$
其中 $a,b$ 是两个独立一次式。允许 $G$ 与节点原像除子相交；(2.1) 已保留全部重数。

反设 $\ell\subset Q$。若 $Q$ 秩四，可用线性坐标写成
$$
Q:x_0x_3-x_1x_2=0,\qquad \ell:x_2=x_3=0.
$$
由 (2.1)，$\Phi$ 的后两坐标为 $Ja,Jb$。代入二次式并消去非零 $J$ 得 $x_0b=x_1a$。因 $a,b$ 互素，
$$
\Phi=[af:bf:aJ:bJ]
\tag{2.2}
$$
对某个四次式 $f$ 成立。原无基点性迫 $f,J$ 互素。任何 $\lambda\in\ell$ 的原像于是由 $(a:b)$ 唯一决定；在该原像上 $f\ne0$。一个消失于 $\lambda$ 的线性式
$b_0x_0-a_0x_1$ 的拉回是 $f(b_0a-a_0b)$，准确一阶消失。因此从 $\lambda$ 投影的公共基除子只能长一，违背 $\deg G=2$。

若 $Q$ 秩三，它是二次锥；任一所含直线经过锥顶。取
$$
Q:x_0x_2-x_1^2=0,\qquad \ell:x_1=x_2=0,
$$
锥顶为 $[0:0:0:1]$。由中心光滑，$\lambda$ 的 $x_0$ 坐标非零。将 $x_1=Ja,x_2=Jb$ 代入，得到 $x_0b=Ja^2$；互素性迫 $J=bh$，其中 $h$ 三次，故
$$
\Phi=[ha^2:hab:hb^2:f_5].
\tag{2.3}
$$
要映到光滑点 $\lambda\in\ell$，必须 $b=0$ 且 $ha\ne0$。这个原像唯一，而消失于 $\lambda$ 的坐标 $x_1$ 拉回为 $hab$，准确一阶消失，再次与公共二次因子冲突。两种情形都矛盾。$\square$

该引理仅使用本稿已经支付的五次、二次公共因子、普通节点及光滑中心；没有假设四维曲线自身预先光滑或其节点位置已知。

## 3. 原低梯度将第二个交点固定为一个坐标点

仍用原低梯度的记号
$$
F=\tfrac12y^{\mathsf T}Ky,\quad p=Ky,\quad
M=H-\tfrac14yy^{\mathsf T},\qquad
N=T_{3,p}-FT_2+4HKH.
\tag{3.1}
$$
已付原身份给 $N\lambda=Mp$、$N(\lambda,\lambda)=0$。置
$$
y_+=\tfrac12u_0,\qquad y_-=\sum_{i=1}^3w_i u_i,\qquad
u=y_+-y_-.
$$
于是 $y=y_++y_-$、$H\varepsilon=u/4$。由 (1.3)，
$$
\begin{aligned}
N(\lambda,\varepsilon)
 &=\varepsilon^{\mathsf T}Mp
 =\frac14 u^{\mathsf T}Ky,\\
N(\varepsilon,\varepsilon)
 &=\frac F2+\frac14u^{\mathsf T}Ku
 =\frac14(y^{\mathsf T}Ky+u^{\mathsf T}Ku).
\end{aligned}
\tag{3.2}
$$
因为 $u_0$ 是物理点，$y_+^{\mathsf T}Ky_+=0$。令
$$
\eta=N(\lambda,\varepsilon)=-\frac14y_-^{\mathsf T}Ky_-.
$$
(3.2) 准确成为 $N(\varepsilon,\varepsilon)=-2\eta$。故原二次关系限制在节点纤维直线上为
$$
\boxed{N(c\lambda+d\varepsilon,c\lambda+d\varepsilon)
=2\eta\,d(c-d).}
\tag{3.3}
$$

若 $\eta=0$，整条 $\ell$ 包含于该二次曲面，违背 §2 引理。因此 $\eta\ne0$。除中心 $[\lambda]$ 之外，该直线与二次曲面的唯一交点是
$$
[\lambda+\varepsilon]=[1:0:0:0]\quad\text{在归一物理坐标中}.
\tag{3.4}
$$

设节点的两个不同归一化原像为 $a,b\in\mathbb P^1$。它们在四维曲线上的像必须都是 (3.4)。这里不能把其中一个原像留在投影中心：若四维像为 $\lambda$，节点方向意味着曲线在该原像的首个非零切向属于 $\ell$。但是 (3.3) 在 $\lambda$ 处沿 $\ell$ 的一阶导数非零，说明该方向不属于二次曲面的切平面；而曲线的首个非零切向必须在切平面内。这矛盾。等价地，$\ell$ 在 $\lambda$ 处与二次曲面横截，所以该方向不可能是从中心消去基因子后留下的投影值。

因此若记归一极线 $p_i(z)=u_i^{\mathsf T}Kv(z)$，有
$$
\boxed{p_1(a)=p_2(a)=p_3(a)=p_1(b)=p_2(b)=p_3(b)=0,\qquad a\ne b.}
\tag{3.5}
$$

## 4. 原物理极线使节点产生三个原像，矛盾

令三个对应的原支点为 $s_1,s_2,s_3$。由核的对称性，(3.5) 说明两个物理极线 $k(a,z),k(b,z)$ 都在 $s_1,s_2,s_3$ 为零。

先证明 $k(a,b)=0$。若不为零，则 $a,b$ 都不在这两个极线的公共零集中；由
$$
k(a,z)=-\Delta_a(z)^2q(a,z),\qquad
k(b,z)=-\Delta_b(z)^2q(b,z),
$$
两个二元三次式 $q(a,\cdot),q(b,\cdot)$ 必共享三个不同根 $s_1,s_2,s_3$，从而成比例。可是原 $q$ 的系数配对矩阵为
$$
C_q=
\begin{pmatrix}
0&0&-5&1\\
0&22&-3&1\\
-5&-3&-3&0\\
1&1&0&0
\end{pmatrix},\qquad \det C_q=70.
$$
它把三次 Veronese 曲线作可逆线性变换，所以不同 $a,b$ 给出的两个三次极线不能成比例。这一论证齐次成立，也包括无穷远。

现在 $k(a,b)=0$，因此 $a,b$ 本身也都是这两条物理极线的公共根。原[单基点定理](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md)已经证明：两个不同物理极线不可能有四次公共因子。故五点集合
$$
\{a,b,s_1,s_2,s_3\}
$$
至多有三个不同元素。因为后三点互异，必有 $a,b\in\{s_1,s_2,s_3\}$。重新编号使 $a=s_1,b=s_2$。由 (3.5)，三个物理支点两两 $K$ 正交；也就是它们张成全等向三空间。

因此对每个 $j=1,2,3$，
$$
p_1(s_j)=p_2(s_j)=p_3(s_j)=0.
$$
四维物理投影无基点，故 $p_0(s_j)\ne0$。三个不同参数点 $s_1,s_2,s_3$ 全都映到四维坐标点 $[1:0:0:0]$，从而在三维投影后全都映到同一个节点 $[\varepsilon]$。

这与不可约普通节点三次的双有理参数化矛盾：普通节点的归一化恰有两个不同原像，不可能有三个。因此 $w_0=1/2$ 的假设不成立。

## 5. 完整结论与剩余四点类型

四个指标对称，得到
$$
\boxed{w_i\ne\frac12\quad(0\le i\le3)}
\tag{5.1}
$$
对本文全部原完整临界点成立。已知中央三次必须具有唯一半权分割，按一个子集与其补集视为同一分割；(5.1) 排除了所有 $1+3$ 分割。

所以四个不同、无基点的满秩外均值余类，现在只能有
$$
\boxed{w_i+w_j=w_k+w_l=\frac12}
$$
这一唯一的 $2+2$ 半权分割，且任何单个权均不为 $1/2$。其原二次曲面、光滑中心、二次中心除子与完整低梯度仍必须同时满足。本稿没有把单点半权情形的坐标点结论套到 $2+2$ 分割，也没有由此完成整个外均值类或全局 Bell 自然幂问题。
