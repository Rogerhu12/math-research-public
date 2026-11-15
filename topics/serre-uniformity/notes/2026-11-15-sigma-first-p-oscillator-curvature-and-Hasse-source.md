# 首 p oscillator 连接的准确 p 曲率与原 Hasse 边界源

日期：2026-11-15。状态：**以下 Hasse 微分式、Cartier 等式、p 曲率与带源方程已证明；原 critical/primitive 共同非零未证明。**

本篇接续 notes/2026-11-15-sigma-modular-heat-connection-and-odd-tame-trivialization.md（以下称 MH）。
奇部分有限连接的零 p 曲率不能消掉 oscillator。这里在同一个首 p 多项式空间中计算后者的完整 p 曲率。全部为纸面恒等式；没有运行本地数学或扩大有限素数窗口。

## 1. 同一辅助曲线、微分与 Hasse 多项式

固定 p=6N+5>=41，k 为特征 p 的代数闭包，并取
$$
E_{27}:Y^2=X^3+16,\qquad
\omega=\frac{dX}{2Y},\qquad DX=2Y,\quad DY=3X^2.
\tag{OP1}
$$
D 是 MH 中沿 Delta=-432 的同一个模参数导数，原 CM 点为
P_0=(0,4)。MH 的 CM 向量场论证给 D^p=0。
原椭圆变量仍记 z；D 与 partial_z 不混用。

令 m=(p-1)/2=3N+2，并定义
$$
f(T)=T^3-\frac{3X}{4}T-\frac Y4,\qquad
A=[T^{p-1}]f(T)^m.
\tag{OP2}
$$
这是原 Hasse 多项式 A_p(a,b) 在 a=3X,b=Y 上的限制。
保留原 B=(-1)^{N+1} binom(3N+2,2N+1)，MH 已证
$$
A(P_0)=0,\qquad (DA)(P_0)=B\ne0.
\tag{OP3}
$$

## 2. 原 Hasse 的二阶方程：直接系数证明

有
$$
\boxed{D^2A=-\frac X4 A.}
\tag{OP4}
$$
为核对所有常数，不将一般 Picard--Fuchs 规范直接套入。
令
$$
R(T)=-\frac X2T^4-\frac{3X^2}{8}T^2-\frac{XY}{4}T-6.
$$
把 T 看成 D 常数，则
$$
Df=-\frac32YT-\frac34X^2,\qquad
D^2f=-\frac92X^2T-3XY.
$$
利用 Y^2=X^3+16，逐项有多项式恒等式
$$
\frac34(Df)^2-\frac12fD^2f+\frac X4f^2
=f R'-\frac32f'R,
\tag{OP5}
$$
其中撇号只指对 T 的导数。
由于 m=-1/2、m-1=-3/2 于 k，(OP5) 给
$$
D^2A+\frac X4A
=[T^{p-1}]\frac d{dT}\bigl(Rf^{m-1}\bigr)=0.
$$
最后一个系数等于 p[T^p](Rf^{m-1})。m>=2 保证这里始终是多项式，
没有负次数或非法除 p。

## 3. 非零的全局 Cartier 配对

本节证明一个准确的全局等式：
$$
\boxed{\mathcal C(A^{-2}\omega)=\omega.}
\tag{OP6}
$$
其中 C 为原 Cartier 算子。

首先，A 在辅助曲线的 O 点恰有 m 阶极点。
取与 omega 相容的原局部首项 X=s^{-2}+...,Y=-s^{-3}+...，
其首系数是
$$
\mathscr A_p(3,-1)=A(1,-1)=[T^{p-1}]
 (T^3-\tfrac34T+\tfrac14)^m
=[T^{p-1}](T-\tfrac12)^{p-1}(T+1)^m
=(3/2)^m\ne0.
\tag{OP7}
$$
最后一步用模 p 的二项式系数，或展开
(T-1/2)^{p-1} 后逐项相加。
故 A 的有限零除子总次数是 m<p。

其次，所有有限零都简单。若 A 与 DA 在有限点同时为零，
(OP4) 的正则二阶方程在该点使 A 的所有阶数小于 p 的
Taylor 系数为零：逐步递推时只除严格小于 p 的非零整数。
于是该点零阶至少 p，与其总零次数 m<p 矛盾。

在一个有限零点，令 F=DA。由 (OP4)，
dF/dA=-(X/4)A/F，所以 F=F_0+O(A^2)，F_0≠0。
因此
$$
A^{-2}\omega=\frac{dA}{A^2F}
=\frac1{F_0}\frac{dA}{A^2}+O(1)dA
$$
只有二阶极点而无留数。Cartier 后没有极点。
在其他有限点也正则，O 点则原来就正则。
所以 C(A^{-2}omega) 是全局正则微分，必为 c omega。

为核 c，原 supersingular 曲线满足 C(omega)=0；
这也可直接从三次 CM 权与 p≡2 mod3 得到。
因而在 O 的形式邻域可选 s 使 ds=omega，
且 X=s^{-2}+...、Y=-s^{-3}+...。
(OP7) 给
$$
A^{-2}\omega=(3/2)^{-2m}s^{p-1}ds+O(s^p)ds
=s^{p-1}ds+O(s^p)ds.
$$
Cartier 的常数项于是为 1，故 c=1，证明 (OP6)。

D^p=0 的函数域中可以选一个 p-basis 坐标 xi 满足 Dxi=1，
omega=d xi。按 1,xi,...,xi^{p-1} 展开任意函数，立即得到
$$
\mathcal C(h\omega)=\bigl(-D^{p-1}h\bigr)^{1/p}\omega.
$$
这个 p-basis 的存在不需循环假设。先取 Dq≠0，令 n 是该 q 满足
D^nq≠0 的最大指标；由 D^p=0，有 1≤n≤p−1。
置 xi=D^{n-1}q/D^nq，则 Dxi=1。它不属于函数域的 p 次幂子域，
故给出 1,xi,...,xi^{p-1} 的 p-basis。
特别 D^{p-1}(xi^{p-1})=(p−1)!=−1，亦直接给出最高阶非零的元素。
因此 (OP6) 等价于
$$
\boxed{D^{p-1}(A^{-2})=-1.}
\tag{OP8}
$$

## 4. 在真实首 p 多项式空间中的完整 p 曲率

置
$$
\mathscr P=k(E_{27})[z]/(z^p),\qquad
\mathcal O=\frac1{12}\partial_z^2+\frac{3X}{4}z^2,\qquad
\nabla=D-\mathcal O.
\tag{OP9}
$$
这里 partial_z 在该商环上有良好定义，partial_z^p=0。
这些是有限多项式算子；没有假设原完整普通 sigma 级数可以模 p 约化。

准确答案为
$$
\boxed{
\nabla^p=\frac1{12}\bigl(A\partial_z+6(DA)z\bigr)^2.
}
\tag{OP10}
$$
右侧平方作为 z 微分算子合成，A、DA 只作系数；
平方中的交叉项必须保留。

证明。先在 A≠0 的函数域中置 q=DA/A，
由 (OP4) 得 Dq=-X/4-q^2。仍令 m=(p-1)/2，故 m=-1/2 于 k。
定义可逆线性换元
$$
(\mathcal T\psi)(z)
=A^m\exp(-3qz^2)\,\psi(z/A).
\tag{OP11}
$$
指数仅在 z^p=0 中取有限和，其所有阶乘指标小于 p。
由于 z^2 的幂零指数小于 p，通常的一阶及二阶微分公式
在该商环中成立；边界项的整数因子是 p，正好为零。

令 w=z/A。直接微分 (OP11)，z partial_z 的交叉项、
纯标量项和 z^2 项依次由 m=-1/2、Dq=-X/4-q^2 消去，给
$$
\mathcal T^{-1}\nabla\mathcal T
=D-\frac{A^{-2}}{12}\partial_w^2.
\tag{OP12}
$$
partial_w^2 与 D、所有函数系数的乘法均交换。
Jacobson 的一维公式及 (OP8) 因而给
$$
\left(D-\frac{A^{-2}}{12}\partial_w^2\right)^p
=D^p-\frac1{12}D^{p-1}(A^{-2})\partial_w^2
-\left(\frac{A^{-2}}{12}\right)^p\partial_w^{2p}
=\frac1{12}\partial_w^2.
\tag{OP13}
$$
这里 D^p=0、partial_w^{2p}=0，且 12^p=12。

最后
$$
\mathcal T\partial_w\mathcal T^{-1}
=A\partial_z+6(DA)z,
$$
所以 (OP13) 正是 (OP10)。右侧系数在 A 的零点也正则；
因此函数域中证明的等式可在 P_0 代值，不允许把有极点的
(OP11) 本身直接在 P_0 代值。由 (OP3)，
$$
\boxed{\left.\nabla^p\right|_{P_0}=3B^2z^2.}
\tag{OP14}
$$
它在整个 p 维 P 上秩 p-2，核为 span(z^{p-2},z^{p-1})。
在奇子空间中核仅为 span(z^{p-2})，秩 (p-3)/2。

## 5. 与原首 p 奇 theta 种子的精确带源关系

保留 MH 的原 Phi_<p=(J_<p,G_<p)^t，
M=[[0,1/2],[5X/8,0]]，DU=MU，det U=2c 为单位，
V=U^{-1}(0,1)^t，以及 Psi_<p=U^{-1}Phi_<p。
MH 已用普通导数、Hurwitz Leibniz 和 Hasse q-expansion 证明
$$
\nabla\Psi_{<p}=\frac A{12}z^{p-2}V.
\tag{OP15}
$$
U 的可分覆盖上 D^p 仍为零，故 (OP10) 依旧有效。
对 (OP15) 再施行 nabla^{p-1}，得到
$$
\boxed{
\bigl(A\partial_z+6(DA)z\bigr)^2\Psi_{<p}
=\nabla^{p-1}\bigl(Az^{p-2}V\bigr).
}
\tag{OP16}
$$
于是原 CM 点上有
$$
\boxed{
36B^2z^2\,\Psi_{<p}(P_0)
=\left.\nabla^{p-1}\bigl(Az^{p-2}V\bigr)\right|_{P_0}
\quad\bmod z^p.
}
\tag{OP17}
$$
右边的全部辅助 D 导数必须在代 P_0 之前完成。
虽然 A(P_0)=0，其 D 导数 B 为单位；
先把 A 置零会错误地删去整个右边，且与原 G=z+... 的首项矛盾。
这里的 V 是明确的代数向量 (-u_2,u_1)^t/(2c)，其 P_0 两分量为单位。

## 6. 实际推进与尚缺事项

本篇把一个全局 Cartier 配对 (OP6) 与 MH 的真实首 p 边界源
接入同一有限 z 多项式空间，得到 (OP16)--(OP17)。
有限奇连接的零 p 曲率，与剩余 oscillator 的非零 p 曲率
是两个不同的结论，必须同时保留。

但 (OP17) 右侧仍含辅助参数方向的完整导数；
这里尚未将其特定系数改写为仅由原
f_i g_{N-1-i} 构成的单位组合。
原 F 属于 MH 的偶部分；奇部可分平凡化本身也不自动运输 F。

因此未筛 critical 全零仍未排除。
原真正目标还须同一个 (6i+7,p+1)=1 标签，
以及 P_{6i+6}(1/sqrt(-3)) 非零；
本篇没有把不同标签的单位拼接，也没有取消这些筛选。
这是一个实际可继续分析的原连接方程，不是主问题完成声明。

## 依赖

- notes/2026-11-15-sigma-modular-heat-connection-and-odd-tame-trivialization.md：
  原 family、矩阵方向、显式可分 U、首 p Hasse 边界源与 DA(P_0)=B。
- R574、R765：原 Cartier 规范 B；本篇 (OP3) 保持该规范。
- R770：原同 primitive/Legendre 标签的 f/g 目标。

