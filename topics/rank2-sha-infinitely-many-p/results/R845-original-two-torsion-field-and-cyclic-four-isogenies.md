# R845 — 原 genus-four 椭圆商的二挠点域、三个实际二同源与循环四同源

日期：2026-11-16。**状态：下列显式映射、核、次数及原 CM 分支的定义域已证明。**
本篇承接 R843 的同一椭圆商，并在第5节使用 R844 付清的原 CM order。
范围始终是 R841 原有限 Hom 表达的最低亏格四项；
未证明存在一个非零的这种项，也未把下面的四同源自动认成原模曲线的退化对应。

## 1. 同一 $E_+$ 的三个非零二挠点

沿 R843，
$$
E_+:\quad v^2=(u+2)(u^3-3u+\mu),\qquad \mu^2\ne4,
\tag{1}
$$
以 $O=(-2,0)$ 为原点，系数域包含 $K=\mathbf Q(\omega)$。
取 $\rho\ne0$ 满足
$$
\boxed{\mu=-(\rho^3+\rho^{-3}).}
\tag{2}
$$
对 $i\in\mathbf Z/3$，置
$$
u_i=\omega^i\rho+\omega^{-i}\rho^{-1}.
$$
直接展开 $u_i^3-3u_i=\rho^3+\rho^{-3}$，得到
$$
\boxed{P_i=(u_i,0),\qquad E_+[2]=\{O,P_0,P_1,P_2\}.}
\tag{3}
$$
三个根互异，因为三次式的判别式为 $27(4-\mu^2)\ne0$。
它们也都不是 $-2$，否则 $\mu=2$。
曲线对合 $(u,v)\mapsto(u,-v)$ 固定所选原点，
故正是群反演；其四个固定点准确为 (3)，并非任取三个分支点后猜测群结构。

三个根的完整 Fourier 逆为
$$
\boxed{
\rho=\frac13\sum_{i=0}^2\omega^{-i}u_i,\qquad
\rho^{-1}=\frac13\sum_{i=0}^2\omega^i u_i.
}
\tag{4}
$$
所以对任何包含 $K,\mu$ 的系数域 $L$，准确有
$$
\boxed{L(E_+[2])=L(\rho).}
\tag{5}
$$
这是实际二挠点坐标域，不是只由某个邻点的 $j$-不变量猜出的域。

当 $\mu$ 为变量时，(2) 是 degree6 覆盖：
$\rho$ 满足 $\rho^6+\mu\rho^3+1=0$，
而六个不同的自同构由
$$
\rho\mapsto\omega\rho,\qquad \rho\mapsto\rho^{-1}
\tag{6}
$$
生成。它们保持 $\mu$、作用忠实，且构成 $S_3$。
在 (3) 上，第一个作用循环三个点，第二个固定 $P_0$ 并交换 $P_1,P_2$。
在特殊参数处只能使用实际专门化的作用，不预先保留泛型的 $S_3$ 阶数。

R843 的 $X_0(3)$ 参数随之准确为
$$
\boxed{
T=-27\left(\frac{\rho^3-1}{\rho^3+1}\right)^2.
}
\tag{7}
$$
(7) 的基点外范围由 $\mu\ne\pm2$ 保证。
它同时保持 R843 的指定三同源核和这里的三个二挠点；
本篇不通过一个未说明的模块函数换标这两个结构。

## 2. 三个二同源的全部方程和归一

R843(19) 的同一个 Weierstrass 模型是
$$
E_+:\quad y^2=x^3+A x+B,\quad
A=-3(2\mu+5),\quad B=\mu^2+14\mu+22.
\tag{8}
$$
(3) 中三个点的 $x$ 坐标准确为
$$
\boxed{e_i=3+\frac{\mu-2}{u_i+2}.}
\tag{9}
$$
这是 R843 的真实双有理变换，不是另一个二挠点排列。

对给定 $i$，置
$$
X=x-e_i,\qquad
a_i=3e_i,\qquad b_i=3e_i^2+A.
$$
于是
$$
E_+:\quad y^2=X^3+a_iX^2+b_iX,\qquad P_i=(0,0).
\tag{10}
$$
平滑性保证 $b_i(a_i^2-4b_i)\ne0$。
定义
$$
\boxed{
\mathcal E_i:\quad
Y^2=U^3-2a_iU^2+(a_i^2-4b_i)U,
}
\tag{11}
$$
以及同一个实际态射
$$
\boxed{
\varphi_i:E_+\longrightarrow\mathcal E_i,\qquad
U=X+a_i+\frac{b_i}{X},\qquad
Y=y\left(1-\frac{b_i}{X^2}\right).
}
\tag{12}
$$
验证 (12) 只需恒等式
$$
U\big((U-a_i)^2-4b_i\big)
=\left(X+a_i+\frac{b_i}{X}\right)
 \left(X-\frac{b_i}{X}\right)^2.
$$
右侧等于 $y^2(1-b_i/X^2)^2$。
这给有理映射；光滑射影曲线的性质使其延拓为态射，
并将 $O$、$P_i$ 都送到 (11) 的原点。

(12) 的 $U$ 在源上总极除子为 $2(O)+2(P_i)$，
而目标 $U$ 的极除子为两倍原点，故态射次数准确为2。
它保持原点，所以为椭圆同态，因而
$$
\boxed{\ker\varphi_i=C_i=\{O,P_i\},\qquad \deg\varphi_i=2.}
\tag{13}
$$
所取符号还支付微分归一：
$$
\boxed{\varphi_i^*\frac{dU}{2Y}=\frac{dX}{2y}.}
\tag{14}
$$
若把 (12) 的 $Y$ 反号，则同源改为 $-\varphi_i$，
核不变，但 (14) 变号；本篇保持 (12)–(14) 的选择。

目标的 $j$ 也可直接写出：
$$
\boxed{
j(\mathcal E_i)=
\frac{16(a_i^2+12b_i)^3}
     {b_i(a_i^2-4b_i)^2}.
}
\tag{15}
$$
这是由 $y^2=x^3+a'x^2+b'x$ 的
$j=256(a'^2-3b')^3/(b'^2(a'^2-4b'))$
代入 $a'=-2a_i,\ b'=a_i^2-4b_i$ 得到，全部常数已保留。

## 3. 不同邻点之间准确为循环四同源

令 $\widehat\varphi_i:\mathcal E_i\to E_+$ 为 (12) 的极化对偶，
则
$$
\widehat\varphi_i\varphi_i=[2],\qquad
\varphi_i\widehat\varphi_i=[2].
\tag{16}
$$
对每个有序对 $i,j$ 定义
$$
\boxed{\Theta_{ij}=\varphi_j\widehat\varphi_i:
\mathcal E_i\longrightarrow\mathcal E_j.}
\tag{17}
$$
它的次数总为4，但核有必须区分的两种情况：
$$
\boxed{
\begin{array}{c|c|c}
i=j&\Theta_{ii}=[2]&
\ker\Theta_{ii}=\mathcal E_i[2]\simeq(\mathbf Z/2)^2\\
i\ne j&\deg\Theta_{ij}=4&
\ker\Theta_{ij}\simeq\mathbf Z/4 .
\end{array}}
\tag{18}
$$

为证明第二行，先由 (16) 得
$$
\widehat\varphi_i(\mathcal E_i[2])\subset C_i.
$$
对偶同源的核在 $\mathcal E_i[2]$ 中有两个元素，
故像也有两个元素，准确等于 $C_i$。
若 $i\ne j$，$C_i\cap C_j=\{O\}$。
所以
$$
\ker\Theta_{ij}\cap\mathcal E_i[2]
=\ker\widehat\varphi_i
$$
只有两个元素。
一个特征零、阶4的椭圆有限子群若非循环，则整个群都在二挠点中；
这里已经排除，遂得到 (18) 的循环性。
此外
$$
\widehat\Theta_{ij}=\Theta_{ji}.
\tag{19}
$$
这保留两个方向，而不把它们合并成一个无向的未定对应。

(18) 是两个实际二同源复合的核计算。
它为原两端点问题提供了一个真实的非回溯 degree4 几何对象，
但还没有证明它等于 R831 的 $q_0/q_2$ 退化数据。
尤其在 $i=j$ 时必须使用第一行，不能把 $[2]$ 当成循环四同源。

## 4. 与同一个三同源的互素方块

仍用 R843 已构造的
$$
\alpha:E_+\longrightarrow E_-,\qquad\deg\alpha=3.
$$
由于核为阶3，$\alpha$ 在 $E_+[2]$ 上为单射，
因而是到 $E_-[2]$ 的同构。
令
$$
C_i^-=\alpha(C_i),\qquad
\mathcal E_i^-=E_-/C_i^-,\qquad
\varphi_i^-:E_-\to\mathcal E_i^- .
$$
商的泛性质给唯一群同态 $\alpha_i$ 满足
$$
\boxed{
\alpha_i\varphi_i=\varphi_i^-\alpha,\qquad
\alpha_i:\mathcal E_i\to\mathcal E_i^- .
}
\tag{20}
$$
两边次数均为6，所以 $\deg\alpha_i=3$。
这是真正的二、三同源方块，未通过两个 $j$ 相等推定其交换。

在 $E_+$ 上，$C_i$ 与 $\ker\alpha$ 阶数互素，
故其和是一个循环阶6子群。
所以 (20) 的共同复合准确为这个阶6子群的商。
所有 (12)、(17)、(20) 都从同一个 (1) 和 R843 的指定 $\alpha$ 出发。

## 5. 原最低属四项中的实际域与 CM order

本节使用 [R844](R844-original-genus-four-cm-order-seventeen-and-two-neighbors.md)
的完整域论证，不能仅由泛型 (6) 代替它。
记
$$
F_3=K(\sqrt[3]{17}),\qquad H_{17}=K(17^{1/6}),\qquad
H_{34}=H_\eta.
$$
原曲线的下降模型须保留可能的 cubic twist：
$$
D:\quad y^3=d\,x(x^4+a x^2+b),\qquad
a,b,d\in F_3,\quad \beta=\sqrt b\in F_3 .
\tag{21}
$$
R844 已付
$$
\Delta=a^2-4b\in17F_3^{\times2},\qquad
\mu=-2a/\sqrt\Delta,\qquad
K(\mu)=K(j(E_+))=H_{17},
\tag{22}
$$
以及两条正文 $E_\pm$ 的几何 endomorphism order 均恰为
$\mathcal O_{17}=\mathbf Z+17\mathcal O_K$。
这里 $d$ 不能在 $F_3$ 内免费吸收，但不进入 $\mu$。

R843 的两个 $j=0$ Prym 商在 (21) 中可写为
$Y_\pm^2=X_\pm^3+c_\pm$，其中
$$
c_\pm=d^4(-a\pm2\beta),\qquad
r_0=c_+/c_-=\frac{a-2\beta}{a+2\beta}.
$$
R844 证明这一实际 twist 比的 Kummer splitting field 为
$H_{34}/F_3$，次数6；在17的归一赋值与6互素。
现在选择与 (22) 同一个 $\sqrt\Delta$，令
$$
\boxed{\rho^3=\frac{a-2\beta}{\sqrt\Delta}.}
\tag{23}
$$
于是
$$
\rho^6=r_0,\qquad
\rho^3+\rho^{-3}=\frac{2a}{\sqrt\Delta}=-\mu.
$$
因此 (23) 正是第1节已付的二挠点参数，且
$$
F_3(\rho)=H_{34}.
\tag{24}
$$
又 $\mu$ 是 $\rho$ 的有理函数，(22) 使
$F_3\subset H_{17}=K(\mu)\subset K(\rho)$。
所以真正得到
$$
\boxed{
K(\rho)=H_{34},\qquad
H_{17}(E_+[2])=H_{34}.
}
\tag{25}
$$
这里 (5) 的 Fourier 逆支付了二挠点域的等号。
选别的 $\rho$ 根只重排三个点，(25) 不变。

$\operatorname{Gal}(H_{34}/H_{17})$ 为阶3群，
按 $\rho\mapsto\omega^{\pm1}\rho$ 循环 $P_i$、$C_i$ 和三个实际二同源。
因为2在 $K$ 惰性且 $2\nmid17$，R844 的局部 CM 格计算说明
每个 $\mathcal E_i$ 的 order 恰为 $\mathcal O_{34}$，
且三个邻点各不相同。CM 主定理给
$$
\boxed{K(j(\mathcal E_i))=H_{34}\qquad(i=0,1,2).}
\tag{26}
$$
(25) 与 (26) 是两项分别付清的结论，不能以其中一项直接替代另一项。

(21) 的实际 elliptic quotients 在固定扩域后与本篇模型相认。
在 $H_{17}$ 上换一个有相同 $j$ 的 elliptic model 只作 quadratic twist：
order17的单位群为 $\{\pm1\}$，且 $j\ne0,1728$。
这样的 twist 在二挠点上作用平凡，故 (25) 也是该 CM 模点
二级结构的内在定义域，不依赖任意的 Weierstrass 二次扭选择。

## 6. 精确接续到原端点时还需要什么

现已从原最低亏格四项得到：

- 一个 order17 的实际三同源 $(E_+,\ker\alpha)$；
- 原十八阶角色域 $H_{34}$ 上全部三个 order34 二邻点及其明确二同源；
- 任意两个不同邻点间的真正循环四同源，反向为极化对偶；
- 与原三同源交换的全部互素二、三同源方块。

这些是同一个曲线项上的真实几何，保留所有核和次数。
然而本篇没有给这些 elliptic CM 点到原
$X_0(10404)\to X_0(2601)$ 的完整 level 结构。
原3、17处向量、两个退化嵌入及有限 Artin 权重仍须逐项比较。
也没有将 (17) 的图形自动等同于原 modified diagonal 的
$\lambda_\nu$-投影，或等同于 R814 的指定 generalized Heegner cycle。

因此 R831 的 $6^{-2}$、$X_1$ 的 $12^{-2}$ 与遗忘次数
$1632/816$ 均不受本篇2、3、4、6这些内部同源次数的改变。
原 $X\to D$ 次数、Hom polarization 系数及全部固定角色仍保留。
下一问题是这条**指定** cycle 对应，而不是另选一个 CM cycle 证明其非零。

## 7. 依赖与范围

- [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)：
  原 whole-packet Hom 展开、实际最低 genus-four 分支。
- [R843](R843-actual-genus-four-quotient-and-cm-three-isogeny.md)：
  同一个 genus-two 商、完整 Weierstrass 变换、指定 degree3 同源与真实 Prym 分解。
- [R844](R844-original-genus-four-cm-order-seventeen-and-two-neighbors.md)：
  原 Galois 下降、整数 CM order、17惯性和 ring class fields；
  第5节只在该定理的原适用范围内使用。
- 第2–4节的同源恒等式、微分符号和有限核均已自含验证，
  没有用一次数值模块方程或有限素数扫描替代。

本篇没有执行新的数学计算或生成可重算数值输出。
