# 原 Picard--Fuchs 连接的 cusp Cartier 源与首 p 周期修正

日期：2026-11-15。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：本文的 Cartier、连接曲率及有限截断修正式已证明；原临界五次分母源和 primitive / Legendre 同标签非零仍开放。**
本文只用 [PL 原 Schwarz 标架](2026-11-15-sigma-original-Schwarz-frame-and-critical-Lagrange-source.md)
的实际方程与归一。没有执行新的数学计算。

## 1. 原有限多项式与 cusp 值

设
$$
p=6N+5\ge41,\qquad r=(p-2)/3=2N+1,\qquad
D=1-8U^3.
$$
PL 的原算子是
$$
\mathcal L=D\partial_U^2-24U^2\partial_U-8U
          =\partial_U\circ D\partial_U-8U.
\tag{PC1}
$$
所有下式先在 PL 指定的 $p$ 整有限范围形成，再在
$k=\mathbf F_p$ 约化。定义
$$
A(U)=U\sum_{j=0}^{r}a_jU^{3j},\qquad
a_j=8^j\frac{(2/3)_j^2}{(4/3)_j\,j!},
$$
$$
C(U)=\sum_{j=0}^{r}c_jU^{3j},\qquad
c_j=8^j\frac{(1/3)_j^2}{(2/3)_j\,j!}.
\tag{PC2}
$$
本篇的 $A,C$ 只表示这两个有限多项式，不表示完整超几何级数
在模 $p$ 的不存在的普通约化，也不重命名 R812 的 Hasse 归一。

PL 已证明这些分母和各 $a_j,c_j$ 都是单位，
$\deg A=p-1,\deg C=p-2$，$A(0)=0,A'(0)=C(0)=1,C'(0)=0$。
对单项式直接有
$$
\mathcal L(U^n)=n(n-1)U^{n-2}-8(n+1)^2U^{n+1}.
$$
相邻系数按 (PC2) 约去，最后一项分别给
$$
\boxed{\mathcal L A=0,\qquad
       \mathcal L C=-8c_rU^{p-1}.}
\tag{PC3}
$$
特别第二式不是齐次方程。

令
$$
a_*=\sum_{j=0}^{r}\frac{(2/3)_j^2}{(4/3)_j\,j!}.
$$
因 $-r=2/3$ 在 $k$ 中成立，把终止恒等式
$$
\sum_{j=0}^{r}
 \frac{(-r)_j(b)_j}{(c)_j\,j!}
 =\frac{(c-b)_r}{(c)_r}
$$
用于 $b=2/3,c=4/3$，得到
$$
\boxed{a_*=\frac{(2/3)_r}{(4/3)_r}\in k^\times.}
\tag{PC4}
$$
这是有限 Chu--Vandermonde 恒等式；其所有分母都在 (PC2)
的已检查范围内。因此没有在一个含 $p$ 的分母上使用形式终止。

在 $D$ 的任一根 $d$ 上，$d^3=1/8$，准确有
$$
A(d)=d\,a_*\ne0.
\tag{PC5}
$$
另一方面，$A$ 在 $D\ne0$ 处的根全部简单：
若重数 $2\le m\le\deg A<p$，(PC1) 的最低次项为
$D(d)m(m-1)(U-d)^{m-2}$，不能为零。这也说明
$A,A'$ 在有限直线上没有共同零。

## 2. 只由实际 cusp 留数决定的 Cartier

记 $\operatorname{Car}$ 为一变量几何 Cartier，定义在
$k(U)dU$，并按通常的 $p^{-1}$ 半线性扩到 $\overline{k}(U)dU$。
置
$$
\omega=\frac{dU}{D A^2}.
\tag{PC6}
$$
若 $a$ 是 $A$ 的根，则 (PC3) 在 $a$ 给
$$
D(a)A''(a)+D'(a)A'(a)=0.
$$
把 $A=A'(a)(U-a)+A''(a)(U-a)^2/2+\cdots$ 代入 (PC6)，
其双极的留数为
$$
-\frac{D'(a)/D(a)+A''(a)/A'(a)}
        {D(a)A'(a)^2}=0.
\tag{PC7}
$$
因此这些双极不产生 Cartier 极点：$p>2$ 时一个只有双极且
无留数的局部极部是精确微分。

剩余有限极点恰为三个 $D$ 根。由 $D'(d)=-24d^2$、
$d^3=1/8$ 与 (PC5)，
$$
\operatorname{res}_{U=d}\omega
=\frac1{D'(d)A(d)^2}
=-\frac1{3d\,a_*^2}.
\tag{PC8}
$$
它们位于 $k_2=\mathbf F_{p^2}$。因 $d\in\frac12\mu_3$，
$p\equiv2\pmod3$，故
$$
d^p=d^{1/p}=\frac1{4d}.
\tag{PC9}
$$
Cartier 不把局部极点换成另一个点；它在每个固定点把留数
取 $p$ 次根。因此 (PC8) 对应的新留数是
$$
-\frac{4d}{3a_*^2}.
$$
同时 $\omega$ 在无穷远的阶为 $2p-1\ge0$，Cartier 也在那里正则。
$\mathbf P^1$ 没有非零全局正则微分，所以所列留数唯一决定
$\operatorname{Car}(\omega)$。利用
$$
\sum_{d^3=1/8}\frac{d}{U-d}
 =U\frac{D'}D-3=-\frac3D,
$$
准确得到
$$
\boxed{
\operatorname{Car}\left(\frac{dU}{D A^2}\right)
 =\frac{\kappa}{D}\,dU,\qquad
 \kappa=\frac4{a_*^2}\in k^\times.
}
\tag{PC10}
$$
这里所有极点、无穷远和半线性常数都已保留。
这不是把某个 supersingular 点的周期选择为单位后的推论。

## 3. 原连接的完整 p 曲率，包括基的符号

在列向量 $(y,y')^t$ 上定义原 Picard--Fuchs 连接
$$
\nabla_\partial=\partial_U-M,\qquad
M=
\begin{pmatrix}
0&1\\
8U/D&24U^2/D
\end{pmatrix}.
\tag{PC11}
$$
因而 (PC1) 的解列是 $\nabla_\partial$ 的水平列，而不是其对偶。
在函数域上取真正的有理基
$$
v=\binom{A}{A'},\qquad
e=\binom{0}{1/(DA)}.
$$
直接求导给
$$
\nabla_\partial v=0,\qquad
\nabla_\partial e=-h\,v,\qquad h=1/(D A^2).
\tag{PC12}
$$
此基的行列式为 $1/D$。在这个基中连接算子是
$\partial_U-hE_{12}$。

在 $k(U)$ 上 $\partial_U^p=0$：例如对 $k(U^p)$ 的基
$1,U,\ldots,U^{p-1}$ 逐项检查即可。因 $E_{12}^2=0$，
迭代连接算子时含两个 $E_{12}$ 的项为零，其余混合项用
$\binom pj=0$ 约去。因此
$$
(\partial_U-hE_{12})^p
 =-\partial_U^{p-1}(h)E_{12}.
$$
若 $\operatorname{Car}(h\,dU)=H\,dU$，则
$\partial_U^{p-1}h=-H^p$；这是 Laurent 单项式定义中的
$(p-1)!=-1$。故 (PC10) 给该基中的 $p$ 曲率为 $H^pE_{12}$。
返回原列坐标，
$$
(v,e)E_{12}(v,e)^{-1}
  =D\binom{A}{A'}(-A',A).
$$
于是原曲率完整为
$$
\boxed{
\psi_p
=\nabla_\partial^p-\nabla_{\partial^p}
=\kappa D^{1-p}
 \binom{A}{A'}(-A',A).
}
\tag{PC13}
$$
其秩为一，平方为零，并且在每个 $D\ne0$ 的有限点都非零。
特别在原 $U=0$，
$$
\boxed{\psi_p(0)=
\begin{pmatrix}0&0\\-\kappa&0\end{pmatrix}.}
\tag{PC14}
$$
这是 PL 的实际 rank-two Gauss--Manin / Picard--Fuchs 连接，
不是另篇已平凡化的六个 theta heat 截面连接。两者的曲率不应混同。

## 4. 顶项与首个 p 分母的原规范相合

把 $w=(C,C')^t$ 代入同一连接，(PC3) 给
$$
\nabla_\partial w
 =\binom0{-8c_r U^{p-1}/D}.
\tag{PC15}
$$
再作用 $p-1$ 次并在 $U=0$ 评价，只有 $U^{p-1}$ 的纯
$p-1$ 阶导数贡献常数；含连接矩阵或较低阶导数的项均仍有正阶。
故
$$
\psi_p(0)w(0)=\binom0{8c_r}.
$$
而 $w(0)=(1,0)^t$。与 (PC14) 比较，准确得到
$$
\boxed{\kappa=-8c_r.}
\tag{PC16}
$$
这样 (PC10) 的 cusp 留数与 (PC3) 的局部顶项在同一归一下匹配，
没有另选符号或尺度。

也可仅用 Wilson 核对该常数。设
$$
P_0=3^r r!,\quad
P_1=\prod_{j=0}^{r-1}(3j+1),\quad
P_2=\prod_{j=0}^{r-1}(3j+2).
$$
$r$ 为奇数，配对 $u$ 与 $p-u$ 得
$P_2=-P_0$ 及 $\prod_{j=0}^{r-1}(3j+4)=-P_1$。
Wilson 给 $P_0P_1P_2=1$，从而 $P_1P_2^2=-1$。
又 $8^r=2^{p-2}=1/2$，故
$$
a_*=-P_2/P_1,\qquad
c_r=\tfrac12P_1^3,\qquad
4/a_*^2=-8c_r,
$$
与连接推导完全相同。

PL 的完整特征零 $C$ 在 $U^{p+1}$ 首次出现 valuation $-1$，
而上述有限 $C$ 的曲率顶源正是这一不能普通约化的现象。
(PC15) 不是第二个水平列；把其右端置零会与 (PC14) 直接矛盾。

## 5. 有理截断的精确修正与第二个 Cartier 式

定义另一个有限多项式
$$
J(U)=\sum_{j=0}^{r}\frac{a_j}{3j+1}U^{3j+1},
\qquad J'=A/U.
\tag{PC17}
$$
因 $1\le3j+1\le p-1$，这里所有新分母也为单位。
令 $W=A'C-AC'$。由 (PC3)：
$$
(DW)'=8c_r A U^{p-1}=-\kappa U^p J'.
$$
两边积分常数不能在特征 $p$ 中任意删去。
这里 $\deg(DW),\deg(U^pJ)\le2p-1$，所以导数为零的差
只能为 $b_0+b_1U^p$。
但 $DW$ 和 $U^pJ$ 仅有 $0\bmod3$ 的次数，$p\equiv2\bmod3$，
故 $b_1=0$；初值给 $b_0=1$。于是
$$
\boxed{D(A'C-AC')=1-\kappa U^pJ.}
\tag{PC18}
$$
所以有限有理函数 $C/A$ 的微分，准确为
$$
\boxed{
d(C/A)
=-\frac{dU}{DA^2}
 +\kappa U^p\,\frac{J\,dU}{DA^2}.
}
\tag{PC19}
$$
该修正不能因含 $U^p$ 就被 Cartier 忽略：
$J\,dU/(DA^2)$ 在 $0$ 有留数 $1$ 的简单极点，
故修正项从 $U^{p-1}dU$ 开始，恰会贡献首 Cartier 系数。

对 (PC19) 应用 Cartier，左边是有理函数的精确微分，像为零。
由 (PC10) 及 $p^{-1}$ 半线性，
$$
0=-\kappa\,\frac{dU}{D}
   +\kappa U\,
      \operatorname{Car}\left(\frac{J\,dU}{DA^2}\right).
$$
因此还得到
$$
\boxed{
\operatorname{Car}\left(\frac{J\,dU}{DA^2}\right)
=\frac{dU}{UD}.
}
\tag{PC20}
$$
这是同一原截断的准确补偿关系；没有将特征零的完整
$C/A$ 当成特征 $p$ 的有理原函数。

## 6. 与真正临界五次源的距离

PL 的原平方卷积是
$$
S_{p-6}
=-\frac1{4374}[U^{p-1}]
       \frac{\mathsf x^2 A^5}{D C^5}
\pmod p,
$$
其中 $\mathsf x$ 是 XF 的固定 Fermat 支，且只在 PL 已证的
首 $p$ 整范围取系数。等价地，它要求
$(A/C)^5\alpha_0$ 的指定 Cartier 系数，
$\alpha_0=d\mathsf y/(\mathsf y^3-1)$。

(PC10)、(PC13) 和 (PC20) 计算的是原周期连接及其 cusp 源，
并没有将上述 $C^{-5}$ 消去。尤其非零的秩一曲率只给出
(PC15) 的准确顶源，不能推出另一指定截面或其五次商的
Cartier 评价非零。原同 $h$ 目标还须保持 PL(16) 的两个
独立变量及 primitive / Legendre 权，单个未筛 $S_{p-6}$
非零也不会自动满足该目标。

本篇完整说明了 cusp 留数、连接符号、首个 $p$ 分母和有限
有理修正之间的关系。下一步需要真实控制带 $C^{-5}$ 的源
或原双变量筛后的源；不使用一个并不存在的第二水平周期来关闭缺口。
