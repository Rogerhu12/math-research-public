# R9：闭空间曲线的准确 rectifying 平度量核

日期：2026-11-14。以下是独立直接计算的准确局部构造。它提供可闭合材料角的嵌入小环带候选，不提供圆端口、握持帽或最终闭曲面。实现准备在 `../scripts/space_star_flat_core.py`；实际 lift/宽度筛选只在本公开仓库 Actions。

## 1. 准确公式与适用条件

设 $\gamma(u)$ 为光滑闭空间曲线，周期 $2\pi$，$|\gamma_u|=a_0>0$。假设处处物理曲率 $\kappa>0$，取右手 Frenet 标架 $(T,N,B)$ 和物理挠率 $\tau$：

\[
T_u=a_0\kappa N,\quad
N_u=-a_0\kappa T+a_0\tau B,\quad
B_u=-a_0\tau N.
\]

定义 $q=\tau/\kappa$。给定材料坐标 $(s,\theta)$，令内部曲线参数 $u$ 解

\[
\theta=u+\frac{s}{a_0}q(u),\qquad
J(s,u)=1+\frac{s}{a_0}q'(u)>0.
\tag{1}
\]

因为 $q$ 周期，右端提升映射满足 $f_s(u+2\pi)=f_s(u)+2\pi$；$J>0$ 保证它是圆的定向微分同胚。于是可准确定义

\[
\boxed{X(s,\theta)=\gamma(u)+s\,[B(u)+q(u)T(u)].}
\tag{2}
\]

一个明确充分宽度条件是

\[
|s|\le w,\quad
w\,\sup\left|\frac{dq}{d\ell}\right|<1,
\qquad d\ell=a_0du.
\tag{3}
\]

构造属于 rectifying developable：直母线方向为 $B+qT$，它的导数没有法向分量。这里使用 (1) 给出了真正平行于中央测地线的材料坐标，不能把母线参数误当成正交材料坐标。

## 2. 第一基本形式完全准确

关键抵消是

\[
\frac d{du}(B+qT)=-a_0\tau N+q'T+a_0q\kappa N=q'T.
\]

由 (1)，$u_\theta=1/J$、$u_s=-q/(a_0J)$。因此

\[
X_s=B+qT+(a_0+sq')Tu_s=B,
\quad
X_\theta=(a_0+sq')Tu_\theta=a_0T.
\tag{4}
\]

立即得到

\[
\boxed{g=ds^2+a_0^2d\theta^2.}
\tag{5}
\]

这不是将第一基本形式残差优化到小数值，而是公式恒等式。曲线和标架的周期性同时给出 $X(s,\theta+2\pi)=X(s,\theta)$。任意 $\theta\mapsto\theta+\alpha$ 都是该固定平度量的准确等距群作用。

若 $\gamma$ 是嵌入闭曲线，$X_s(0)=B$ 与 $X_\theta(0)=a_0T$ 独立；紧性与局部管状邻域给出某个正但尚未量化的小宽度，使 (2) 是嵌入环带。实际指定宽度是否嵌入和具有足够 reach，仍须另外验证；(3) 只保证材料坐标与浸入不退化，不排除远点相交。

## 3. 完整位置二 jet 与曲率

取曲面单位法向 $\nu=X_s\times X_\theta/a_0=B\times T=N$。再次直接求导：

\[
X_{ss}=\frac{\tau^2}{\kappa J}N,\quad
X_{s\theta}=-\frac{a_0\tau}{J}N,\quad
X_{\theta\theta}=\frac{a_0^2\kappa}{J}N.
\tag{6}
\]

所以第二基本形式矩阵为

\[
\mathrm{II}=\frac1J
\begin{pmatrix}
\tau^2/\kappa&-a_0\tau\\
-a_0\tau&a_0^2\kappa
\end{pmatrix},
\]

其行列式为零；两个主曲率为

\[
0,\qquad
\boxed{\lambda=\frac{\kappa+\tau^2/\kappa}{J}.}
\tag{7}
\]

在中央 $s=0$，混合系数 $W=\mathrm{II}_{s\theta}=-a_0\tau$ 通常**非零**。不能把它替换成 R44 鞍核某些对称入口的 $W=0$。同样，中央 $X_{ss}=\tau^2N/\kappa$ 一般非零；封口 BVP 必须使用这里的完整二 jet。

小的非平面 lift 虽可移走平面拐点，但可能同时使 $\kappa$ 小、$\tau$ 大，从而令 $\tau^2/\kappa$ 或 $q'$ 很大。故 lift 越小不代表越有利：必须同时筛选 (3)、(7) 和非局部几何。

## 4. 三瓣空间核心与半转对称

以原极角 $\varphi$ 写空间曲线

\[
c(\varphi)=\bigl(r(\varphi)\cos\varphi,
 r(\varphi)\sin\varphi,h\sin3\varphi\bigr),
\quad r=1+a\cos3\varphi+b\cos6\varphi.
\tag{8}
\]

$r>0$ 保证投影本身就是简单闭星形曲线，所以空间曲线也嵌入。再按准确弧长定义 $u$，$a_0=\operatorname{length}(c)/(2\pi)$。必须核查空间曲率处处非零，不能仅由 $h\ne0$ 就宣布它成立。

取绕 $x$ 轴半转 $A=\operatorname{diag}(1,-1,-1)$。因为 $r$ 偶，

\[
\gamma(-u)=A\gamma(u),\quad
T(-u)=-AT(u),\quad N(-u)=AN(u),\quad B(-u)=-AB(u).
\]

因此 $\kappa,\tau,q$ 均为偶函数。式 (1) 的唯一性给

\[
u(-s,-\theta)=-u(s,\theta),\qquad
\boxed{X(-s,-\theta)=AX(s,\theta).}
\tag{9}
\]

三重转动对称也保留。上述对称性是准确完整位置公式的性质，不只是中央截面的位置对称。

## 5. star 位移见证需要投影 padding

中央投影是 `../notes/star-core-geometry-plan-20261114.md` 的边界。非平面核的 $B$ 通常有水平法向分量，因此双侧带不能被假定完全留在原填充星域 $\Omega$。

不过由 (4)，沿固定材料角的径向线速度恰为 $1$，所以

\[
|X(s,\theta)-X(0,\theta)|\le|s|.
\tag{10}
\]

故 $|s|\le w$ 的准确核，其投影包含在 $\Omega$ 的 $w$ 邻域中；竖直坐标绝对值不超过 $h+w$。若平面证书给旋转尖点到 $\Omega$ 距离下界 $d$、平面直径上界 $D_{xy}$，则对这个核有条件预算

\[
\delta\ge d-w,\quad
D_{\rm core}\le\sqrt{(D_{xy}+2w)^2+[2(h+w)]^2}.
\tag{11}
\]

完整闭面要继承它，所有过渡与帽也必须满足相同的投影 padding、竖直跨度和实际固定握持条件。公式 (11) 不证明这些对象已经存在。

因此本结果解决的是“有星形投影、准确固定平度量、闭材料角和完整二 jet 的非平面局部核”这一具体入口。圆端口匹配、闭曲面构造、固定握持幅度与全局 reach 仍未解决。
