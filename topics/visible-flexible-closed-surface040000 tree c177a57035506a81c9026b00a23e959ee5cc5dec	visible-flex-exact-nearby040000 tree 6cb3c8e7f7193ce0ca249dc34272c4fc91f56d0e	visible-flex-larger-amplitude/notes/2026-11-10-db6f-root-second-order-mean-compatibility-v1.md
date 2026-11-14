# 二阶平均模态的精确消去：径向柱帽线性匹配之后的一个恒等式

**状态：完整作者推导，待未参与者全文独立审查。**  
2026-11-10 UTC；root / Astra-visible-flex-db6f0b0e。

本稿研究已审R58给出的二阶项，不假设已经存在非线性帽族。
结论是：对于同一旋转基态上已经同时满足柱边和正则球心的一阶解，
二阶零角模态的积分兼容条件自动成立。
这消去一个可能的平均障碍；其余角模态、高阶方程和实际非线性存在完全未解决。

所有公式为纸面推导；未运行ODE、PDE、BVP、数值谱、矩阵或几何程序，
没有生成或读取任何候选数组、主flat17数据或网格。

## 1. 固定来源与准确假设

使用已完成全文未参与者独立审查的：

- 作者 notes/2026-11-10-db6f-radial-cylinder-cap-linear-matching-v1.md，
  commit 92236c4b60e5996eb4b17efbfdfd6412e4bc84b0，
  SHA256 a93f8a74f2a23726dd93310d41c85b27499311ed8634c57b37453e48907c9c62；
- 完整独审 notes/2026-11-10-db6f-prefix-review-radial-cap-linear-matching.md，
  commit 63db2491b82e47340a4991cbf5e524a74d473506，
  SHA256 0d101bf56b2e3d47f5b50cc56765cdd763da31c64b0a7bd8ff76160263aff2b8；
- 正式R58，commit 2d3c24c4c2a4426d642ccbd7ae4158a8dd6e790a。

为使新证明可独立核查，下面重列所需方程和全部边界估计。
此前无限模作者稿73963d0b尚待审，本定理不调用它；若它后来成立，
这里只条件应用于其中真实正则的一阶解。

共同材料度量为

$$
g=dr^2+a(r)^2du^2,\qquad 0\le r<T,\quad u\in\mathbb R/(2\pi\mathbb Z).
\tag{1}
$$

基态为实际旋转帽

$$
F_0(r,u)=(a(r)\cos u,a(r)\sin u,Z(r)),\qquad
b(r)=Z_r=\sqrt{1-a_r^2}>0.
\tag{2}
$$

有以下固定假设：

1. 入口有真正开单位圆柱：在某个r=0邻域，a=1、a_r=a_{rr}=0、b=1。
2. 整个去中心区0≤r<T有a>0、b>0，所有材料系数光滑。
3. 中心附近是一个固定半径σ>0的圆球开核心。以ρ=T−r，
   a=σsin(ρ/σ)、b=a/σ，并在真正Cartesian材料图内光滑。
4. 给定一个实、全盘光滑的线性第二形式变化
   δII=ℓ dr²+2m drdu+c du²，满足完整线性Gauss–Codazzi。
5. 柱边m(0,u)=0。其余柱边曲率数据由这个实际正则解决定。

这里“一阶解”是一个固定线性对象，不预设它来自非线性族。
新结论也不要求角向C3或预先指定任何有限模态。

对实周期函数v记
〈v〉=(2π)^{-1}∫_0^{2π}v(u)du。

## 2. 二阶平均兼容条件从何而来

基态M_0=0、C_0=ab、L_0=−a_{rr}/b。
线性Gauss和两个Codazzi给

$$
\ell=\frac{a_{rr}}{ab^2}c,\qquad
x=am,\quad \zeta=\frac ba c,\qquad
x_r=P\zeta_u,\quad \zeta_r=R x_u,
\tag{3}
$$

其中

$$
P=\frac{aa_{rr}}{b^3},\qquad R=\frac b{a^2}.
$$

如将一个候选非线性族按无阶乘的τ²系数展开，

$$
M_\tau=\tau m+\tau^2m_2+o(\tau^2),\quad
C_\tau=ab+\tau c+\tau^2c_2+o(\tau^2),
$$

则Gauss的二阶项为

$$
\ell_2=\frac{a_{rr}}{ab^2}c_2+S,\qquad
S=\frac{m^2}{ab}-\frac{a_{rr}c^2}{a^2b^3}.
\tag{4}
$$

置x_2=am_2、ζ_2=bc_2/a，完整二阶Codazzi是

$$
(x_2)_r=P(\zeta_2)_u+aS_u,\qquad
(\zeta_2)_r=R(x_2)_u+ba_rS.
\tag{5}
$$

这些式子也可只作为给定一阶解之后的非齐次线性方程理解。
取角平均得到

$$
\langle x_2\rangle_r=0,\qquad
\langle\zeta_2\rangle_r=ba_r\langle S\rangle.
\tag{6}
$$

若实际族的柱边仍是同一材料长度2π、共同垂直conormal的平面凸曲线，
则Cτ(0,u)是其曲率，故总转角恒2π。
因此〈c_2(0)〉=0，且Mτ(0,u)=0给〈x_2(0)〉=0。
真实光滑中心还要求ζ_2→0。于是二阶平均必要门为

$$
\boxed{\quad
\int_0^T ba_r\left\langle
\frac{m^2}{ab}-\frac{a_{rr}c^2}{a^2b^3}
\right\rangle dr=0 .
\quad}
\tag{7}
$$

**本稿定理：** 假设1–5下，(7)对每个给定的一阶解自动成立。
它不是新增的二阶障碍；(5)的其他频率仍需另解。

## 3. 轴高坐标、模态方程与缺失的0、±1模

令A(Z)=a(r(Z))，并把Z(0)取为0、Z(T)=H。因为b>0，
这是整个去中心区上的合法坐标变换。有

$$
A_Z=\frac{a_r}{b},\qquad
A_{ZZ}=\frac{a_{rr}}{b^4},\qquad
q=\frac{A_{ZZ}}A.
\tag{8}
$$

对角Fourier系数使用
ζ_n=(2π)^{-1}∫ζe^{-inu}du，实函数满足ζ_{-n}=\overline{ζ_n}。
从(3)得，对n≠0，

$$
x_n=\frac{A^2}{in}(\zeta_n)_Z,\qquad
(A^2(\zeta_n)_Z)_Z+n^2AA_{ZZ}\zeta_n=0 .
\tag{9}
$$

再置y_n=Aζ_n、λ_n=n²−1，则

$$
(y_n)_{ZZ}+\lambda_n q y_n=0 .
\tag{10}
$$

柱边m=0给(ζ_n)_Z(0)=0；A在入口常数，所以(y_n)_Z(0)=0。

全盘光滑张量在真实中心有m=O(a)、c=O(a²)，故x=O(a²)、ζ=O(a²)。
n=0时，(3)直接使x_0、ζ_0都是常数，中心极限使二者为0。
对n=±1，(10)给y_{ZZ}=0，入口y_Z=0使y常数，
而中心y=Aζ→0迫使它为0。故只有|n|≥2可能活动。

在球核心，R58的精确两支为
ζ_n=d_n tan^{|n|}(ρ/(2σ))+e_n cot^{|n|}(ρ/(2σ))。
真实中心正则强迫e_n=0。因此每个活动模态有

$$
\zeta_n=d_n\tan^{|n|}(\rho/(2\sigma)).
\tag{11}
$$

这也直接核清后面的中心边界项，不能只把极坐标形式有界当作正则。

## 4. 每个模态的精确边界通量恒等式

本节用撇号表示d/dZ。固定|n|≥2，暂略n下标，置λ=n²−1。
定义实标量

$$
\mathcal B
=AA'\operatorname{Re}(\overline\zeta\,\zeta')
-\frac12(AA''-(A')^2)|\zeta|^2,
\tag{12}
$$

$$
\mathcal E=|y'|^2+\lambda q|y|^2,\qquad y=A\zeta .
\tag{13}
$$

这里E不是非负能量的断言，q可以变号；只使用其准确导数。

由(A²ζ')'+n²AA''ζ=0，即
ζ''=−2A'ζ'/A−n²A''ζ/A，逐项微分(12)得

$$
\mathcal B'
=AA'|\zeta'|^2-n^2A'A''|\zeta|^2
-\frac12(AA'''-A'A'')|\zeta|^2.
\tag{14}
$$

因q=A''/A，有AA'''−A'A''=A²q'。
另一方面，(10)和q实值给

$$
\mathcal E'
=2\operatorname{Re}(\overline{y'}y'')
+\lambda q'|y|^2
+2\lambda q\operatorname{Re}(\overline y y')
=\lambda q'|y|^2.
\tag{15}
$$

将(14)、(15)组合，得到完整的全段恒等式

$$
\boxed{\quad
A'\left(\frac A{n^2}|\zeta'|^2-A''|\zeta|^2\right)
=
\frac1{n^2}\left(\mathcal B+\frac{\mathcal E}{2(n^2-1)}\right)' .
\quad}
\tag{16}
$$

没有以q为除数，不要求q符号、单调性或转折阶数；
只除以已经排除的n=0、±1的常数。
因此所有负K、正K、平坦区和光滑过渡都包含在同一个公式内。

## 5. 两端边界项都确实为零

入口A'=A''=q=0、y'=0，故B(0)=E(0)=0。

在球心令h=H−Z。实际圆球给

$$
A=O(h^{1/2}),\quad A'=O(h^{-1/2}),\quad
A''=O(h^{-3/2}),\quad q=O(h^{-2}).
$$

并且A与h^{1/2}双向可比。
由(11)，若N=|n|≥2，则

$$
\zeta_n=O(h^{N/2}),\quad
(\zeta_n)'=O(h^{N/2-1}),\quad
y_n=O(h^{(N+1)/2}),\quad
y_n'=O(h^{(N-1)/2}).
$$

代入(12)、(13)的每一项均得O(h^{N-1})，所以B、E都趋0。
这些估计同时支付(16)左侧的可积性。
积分(16)于是得到

$$
\int_0^H A'\left(\frac A{n^2}|(\zeta_n)'|^2-A''|\zeta_n|^2\right)dZ=0
\quad (|n|\ge2).
\tag{17}
$$

特别地，单独看∫q'|y_n|²也为零；
不能只从q'在某一个负曲率窗口的符号就推出二阶阻碍。

## 6. 合并全部真实光滑模态，证明平均门

从(4)、(8)直接变元，而不是把r与Z混同，得到

$$
ba_r\langle S\rangle\,dr
=
A'\left(\frac{\langle x^2\rangle}{A^3}
-A''\langle\zeta^2\rangle\right)dZ.
\tag{18}
$$

Parseval和实值性给〈x²〉=Σ|x_n|²、〈ζ²〉=Σ|ζ_n|²。
再用(9)，第n项就是(17)的被积函数，故每个n的积分为零。

还须支付无限求和与积分的交换。远离中心，全部函数光滑，
Parseval的二次和可积。靠近中心，全盘光滑张量给
x=O(a²)、ζ=O(a²)，其角平均平方均为O(A⁴)。
因A'=O(A^{-1})、A''=O(A^{-3})，

$$
|A'|\left(\frac{\langle x^2\rangle}{A^3}
+|A''|\langle\zeta^2\rangle\right)=O(1).
\tag{19}
$$

这是关于Z可积的统一绝对主控。
任何有限Fourier截断的对应两项平方和都不超过完整平方和；
因此可用支配收敛交换极限、两项积分和。
0、±1模在第3节已为零，于是(18)积分等于(17)之和，证明(7)。

本结论适用于一个真实C∞线性场所带的无限活动模态。
它不从一串分别正则的模态自动推断某个未给收敛控制的形式级数光滑。

## 7. 零模方程实际得到什么

对给定一阶解，定义

$$
\langle x_2\rangle=0,\qquad
\langle\zeta_2(r)\rangle=\int_0^r ba_r\langle S\rangle\,ds .
\tag{20}
$$

式(7)使其同样等于
−∫_r^T ba_r〈S〉ds，故两个端点的零值兼容。
中心m=O(a)、c=O(a²)使S=O(1)，而ba_r=O(ρ)。
所以(20)给〈ζ_2〉=O(ρ²)，〈c_2〉=O(ρ²)，〈ℓ_2〉有界。
这是实际解出了平均一阶径向方程并核必要中心阶数；
不把这些有限阶估计冒称为整个二阶张量的Cartesian光滑性或全函数可解。

还可以在单一实球心模式中核一个完整局部例子。
若ζ=d t^n cos(nu)，t=tan(ρ/(2σ))、n≥2、d实，
则x=−σd t^n sin(nu)、c=σd t^n cos(nu)，并由(4)精确得到

$$
\langle S\rangle
=\frac{\sigma^3d^2t^{2n}}{a^4}
=\frac{d^2}{16\sigma}t^{2n-4}(1+t^2)^4 .
\tag{21}
$$

利用ba_r=−2t(1−t²)/(1+t²)²、dr/dt=−2σ/(1+t²)，
满足中心零值的平均解精确为

$$
\langle\zeta_2\rangle
=\frac{d^2}{4}\left(
\frac{t^{2n-2}}{2n-2}
-\frac{t^{2n+2}}{2n+2}
\right).
\tag{22}
$$

它只含t²的非负整数幂，且首项至少t²。
这里〈c_2〉=σ〈ζ_2〉，〈ℓ_2〉=−〈c_2〉/a²+〈S〉。
在n=2时〈S〉(0)=d²/(16σ)、
〈c_2〉/a²→d²/(32σ)，故径向/角向正交分量在中心相同；
n>2时二者的中心常数皆为0。
两分量之差是t²乘一个t²解析函数，
因此这个单一模式所强迫的平均二阶张量在真实Cartesian中心解析。
这只处理平均部分，尚未解同时生成的±2n部分。

## 8. 新结论的范围与后续问题

本稿支付的是二阶平均兼容条件的一个准确消去：
两个二阶强迫aS_u、ba_rS中，
前者的零模本来就为零；
后者的全段积分由线性ODE和两个真实端条件自动为零。
不能把R58列出的ba_rS逐模源项直接当成新的独立平均阻碍。

没有支付：

- 非零模态的二阶入口—中心边值兼容；
- 同一a上的三阶及所有高阶可积性；
- 稀疏无限谱能否支持在指定开H恒零的曲率数据；
- 一个真实非线性连续等距帽族、与强环带的实际接合或闭曲面；
- 全时reach、目标幅度、原主G5、网格或独立原种子重跑。

本稿作者独立从已审R58的二阶系统推导了(16)与全段消去。
在未参与者完成全文审查前，不放入正式results，也不称本题完成。
