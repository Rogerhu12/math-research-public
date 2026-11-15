# 原 cosigma 降阶及其闭合的 critical 通道

日期：2026-11-15。状态：**本文恒等式、秩四核和未筛全零的等价已证明；同一本原标签的非零未证明。**

本笔记给出 R784 六截面的一个原半周期 cosigma 表达，并准确检查这是否增加独立的临界支撑条件。
结论是：去掉乘二参数后，所得 degree $3$ 两截面的加法核确实更小，
但 $x^2\sigma^6$ 通道整列为零；总阶 $p-6$ 恰好回到同一个原 $F/G$ 配对。
没有运行数学计算，也没有更换原 $c=0$ sigma 的二次 Gaussian。

## 1. 原参数、半周期与全部常数

始终固定
$$
E_0:y^2=x^3-1,\qquad dz=dx/(2y),\qquad
Dx=2y,\quad Dy=3x^2,
$$
$$
\sigma(z)=z+O(z^7),\qquad (\log\sigma)''=-x.
\tag{CS1}
$$
取 $s^2=-3$，使用 R782 的原 CM 公式
$$
\sigma(sz)=s x(z)\sigma(z)^3.
\tag{CS2}
$$
取非零二挠点 $T=(1,0)$ 及其任一半周期提升，定义规范 cosigma
$$
c_T(z)=e^{-\zeta(T)z}\frac{\sigma(z+T)}{\sigma(T)}.
\tag{CS3}
$$
改变半周期提升时，sigma 的准周期因子与指数中的 zeta 平移相消，故此函数不变。
它为偶函数、常数项为 $1$，sigma 加法公式给
$$
c_T(z)^2=(x(z)-1)\sigma(z)^2.
\tag{CS4}
$$
另外两个非零二挠点记为 $T_2=(e_2,0),T_3=(e_3,0)$，
其中 $e_2,e_3$ 是另外两个三次单位根；$c_{T_i}$ 采用同一规范。

定义三个 degree $3$ 截面
$$
A(z)=x(z+T)c_T(z)^3,\qquad
B(z)=-\frac12 y(z+T)c_T(z)^3,\qquad
C(z)=c_T(z)^3.
\tag{CS5}
$$
它们有同一个平移后 theta 乘子。原点处 $A(0)=C(0)=1$，
$B(z)=-\tfrac32z+O(z^3)$；符号由 $y' (T)=3$ 固定。

半周期加法公式为
$$
x(z+T)=\frac{x+2}{x-1},\qquad
y(z+T)=-\frac{3y}{(x-1)^2}.
\tag{CS6}
$$
从 (CS2) 两次取对数导数，并用
$D^2\log x=2x+4/x^2$，得到
$$
x(sz)=-\frac{x^3-4}{3x^2}.
\tag{CS7}
$$
因此 (CS4)、(CS6)、(CS7) 给
$$
c_T(sz)^2=(x-1)(x+2)^2\sigma^6=A(z)^2.
$$
两边平方根的常数项都是 $1$，故有准确等式
$$
\boxed{A(z)=c_T(sz).}
\tag{CS8}
$$
这也表明 $s$ 的两种选择不改变 $A$，因为 $c_T$ 为偶函数。
同样，由 (CS4) 和原点处的首项，
$$
c_{T_2}c_{T_3}=-\frac{y\sigma^3}{c_T}.
$$
代入 (CS5)--(CS6) 得
$$
\boxed{B(z)=-\frac32\sigma(z)c_{T_2}(z)c_{T_3}(z).}
\tag{CS9}
$$

## 2. 与 R784 六个原截面的直接识别

沿用 R784 的 $S_0,S_1,S_2,T_0,T_1,T_2$；本节出现的 $T_i$ 截面与上节二挠点的角色不同。
为避免在公式中混淆，以下直接列出所用组合。
令 $Q=x^2-2x-2$。原倍点公式与 (CS4) 给
$$
\sigma(2z)=-2y\sigma^4,\qquad
x(2z)=\frac{x^4+8x}{4(x^3-1)},\qquad
c_T(2z)=Q\sigma^4.
\tag{CS10}
$$
最后一式先平方验证
$4(x^3-1)(x(2z)-1)=Q^2$，再由常数项 $1$ 定号。
从 (CS5)、(CS6)、(CS10) 展开，准确得到
$$
\begin{aligned}
a(z):=A(2z)
&=T_0(z)+6T_1(z)-18T_2(z)\\
&=\bigl(x^6+6x^5-18x^4-8x^3-24x^2+16\bigr)\sigma^{12}\\
&=c_T(2sz),
\end{aligned}
\tag{CS11}
$$
$$
\begin{aligned}
b(z):=B(2z)
&=-18S_0(z)-3S_1(z)+S_2(z)\\
&=3y\bigl(x^4+2x^3+6x^2-4x+4\bigr)\sigma^{12}\\
&=-\frac32\sigma(2z)c_{T_2}(2z)c_{T_3}(2z).
\end{aligned}
\tag{CS12}
$$
例如，(CS11) 的多项式也可因式分解为
$$
(x^2-2x-2)(x^4+8x^3+8x-8).
$$
(CS12) 则直接由 $S_0=-x^2y\sigma^{12}$、
$S_1=-2y(x^3+2)\sigma^{12}$、$S_2=3xy(x^3-4)\sigma^{12}$ 展开。
所有首项与 R784 一致：$a=1+6z^2-18z^4+\cdots$，
$b=-3z-6z^3-18z^5+\cdots$。

## 3. 三条双线性式及完整的代数核验

Hirota 差导数采用 R782 的方向
$$
\mathcal D^r U\cdot V
=\sum_{i=0}^r(-1)^{r-i}\binom ri U^{(i)}V^{(r-i)}.
\tag{CS13}
$$
先在未平移的变量中令 $U=x\sigma^3$、$V=y\sigma^3$。
由 (CS1) 直接求导，有以下四个有理恒等式：
$$
\begin{aligned}
\mathcal D x\cdot y&=-x^3-2,\\
\mathcal D^2x\cdot y&=6x^2y,\\
\mathcal D^3x\cdot y&=-18x^4-72x,\\
\mathcal D^4x\cdot y&=144x^3y+144y.
\end{aligned}
\tag{CS14}
$$
公共 sigma 因子的准确展开为
$$
\frac{\sigma(z+t)^3\sigma(z-t)^3}{\sigma(z)^6}
=1-3x(z)t^2+3x(z)^2t^4+O(t^6).
\tag{CS15}
$$
因此，二至四阶 Hirota 式分别是
$$
\mathcal D^2U\cdot V
=\sigma^6\bigl(6x^2y-6x\cdot xy\bigr)=0,
$$
$$
\mathcal D^3U\cdot V
=\sigma^6\bigl((-18x^4-72x)-18x(-x^3-2)\bigr)
=-36x\sigma^6,
$$
$$
\mathcal D^4U\cdot V
=\sigma^6\bigl((144x^3y+144y)-36x(6x^2y)+72x^2(xy)\bigr)
=144y\sigma^6.
\tag{CS16}
$$
共同平移 $z\mapsto z+T$ 后，(CS3) 的公共线性指数
在差导数中相消；再保留 $B=-V/2$ 的因子，就得到
$$
\boxed{
\mathcal D^2A\cdot B=0,\qquad
\mathcal D^3A\cdot B=18AC,\qquad
\mathcal D^4A\cdot B=144BC.
}
\tag{CS17}
$$
为确定低列，还保留一阶式
$$
\mathcal DA\cdot B=2B^2+\frac32 C^2.
\tag{CS18}
$$
它由 $\mathcal DU\cdot V=-(x^3+2)\sigma^6$ 及
$4B^2=(x(z+T)^3-1)C^2$ 直接得到。

## 4. 加法核的秩恰为四；$x^2\sigma^6$ 整列为零

置
$$
K_{A,B}(z,t)=A(z+t)B(z-t).
$$
$A,B$ 是 degree $3$、同一半周期平移的 theta 截面。
乘积在 $z,t$ 两个变量中的线丛均为原 $\mathcal O(6O)$：
共同半周期的二次角色在两因子中相消。
也可直接从准周期公式检查，因此
$$
K_{A,B}\in H^0(6O)\otimes H^0(6O)
\tag{CS19}
$$
并采用公共因子 $\sigma(z)^6\sigma(t)^6$。
$A$ 偶、$B$ 奇，故 $K_{A,B}(t,z)=-K_{A,B}(z,t)$。
原 $H^0(6O)$ 的偶部分维数为 $4$、奇部分维数为 $2$；
核只连接这两个部分，所以秩至多 $4$。

记
$$
F=x\sigma^6,\qquad G=-xy\sigma^6,\qquad
Y=y\sigma^6,\qquad R=(x^3+2)\sigma^6.
\tag{CS20}
$$
由 (CS5)--(CS6)，直接化简 (CS17)--(CS18) 的低列：
$$
\begin{aligned}
[t^0]K_{A,B}&=-\frac32G+3Y,\\
[t^1]K_{A,B}&=\frac32R+9F,\\
[t^2]K_{A,B}&=0,\\
[t^3]K_{A,B}&=3R-9F,\\
[t^4]K_{A,B}&=-9G-9Y.
\end{aligned}
\tag{CS21}
$$
例如 $AC=(x^3-3x+2)\sigma^6$，
$BC=\tfrac32y(x-1)\sigma^6$，给出了第三、第四阶的两行。
两对非零列在 $\langle G,Y\rangle$ 与 $\langle R,F\rangle$ 上的行列式
分别为 $81/2$ 与 $-81/2$；因此核的秩恰为 $4$，像恰为
$\langle R,F,G,Y\rangle$。

此外，完整 $H^0(6O)$ 中只有 $H=x^2\sigma^6$ 的 $t^2$ 系数非零。
所以 (CS17) 的二阶零式意味着 **$H$ 的整列为零**；
由反对称性，其整行也为零。这不是只在一个低阶系数上偶然消去。

用 $U\wedge V=U(z)V(t)-V(z)U(t)$ 记号，(CS21) 唯一确定整个核为
$$
\boxed{
K_{A,B}
=\frac32 R\wedge G-3R\wedge Y+9F\wedge G+9F\wedge Y.
}
\tag{CS22}
$$
证明不需要一个未写出的高阶计算：秩上界与四个独立低列已确定整个像；
再用 $R,F,G,Y$ 的首阶 $0,4,1,3$，四个低列准确确定反对称系数。

## 5. 总阶 $p-6$ 为何没有新增通道

设 $p=6N+5\ge41$，$d=p-6\equiv5\pmod6$。
以 $[\ ]_d$ 表示一个二变量级数的总次数 $d$ 齐次部分。
原 $R,F,G,Y$ 的 CM 权依次为 $0,4,1,3$，所以 (CS22) 给
$$
\boxed{
[K_{A,B}]_d=9[F\wedge G]_d.
}
\tag{CS23}
$$
其它三项的总权分别为 $1,3,1$，不会贡献总次数 $d$。
特别，缺失的 $H/Y$ 总权 $2+3=5$ 通道没有被恢复。

事实上，未筛选的两个全零条件准确等价：
$$
\boxed{
[F(z)G(t)]_d=0
\quad\Longleftrightarrow\quad
[A(z)B(t)]_d=0.
}
\tag{CS24}
$$
证明正向先用可逆线性换元 $(z,t)\mapsto(z+t,z-t)$，
再用 R784 的完整六截面加法式。
在总权 $5$ 中，每个有序 CM 权对只由一个 $S_\nu/T_\nu$ 通道贡献；
故原全零迫每个互补权的截面系数乘积为零。
于是六截面空间中任意两个元素的总次数 $d$ 乘积都为零。
对 (CS11)--(CS12) 应用此结论，并将两个变量同除以 $2$，得到右边。
反向则由 (CS23) 和同一可逆换元得到 $[F\wedge G]_d=0$。
$F(z)G(t)$ 与 $G(z)F(t)$ 的有序权分别为 $(4,1)$ 与 $(1,4)$，
互不重叠，故每一部分分别为零。

这些运算只使用总次数 $d<p$ 的有限系数。
R697/R784 的整性以及 (CS11)--(CS12) 保证它们可以约化；
$2,3,9,81/2$ 对全部允许的 $p$ 都是单位。
没有把高于首整块的普通 Taylor 级数当成完整 $k[[z]]$ 解。

(CS24) 可以把**未筛选**支撑问题换成半周期 cosigma 语言，
但它没有添加独立非零约束。
原真本原条件与 $P_{6a}(1/s)$ 必须仍保留在原 $F/G$ 同一标签上；
上述换元本身不把一个 cosigma 系数非零自动送到可见本原标签。
需要继续寻找独立的几何或算术输入，不能把这次降阶当成已解决原非零问题。

## 来源

- R782，原 sigma 规范、CM 三同源式及 Hirota 方向。
- R784，六截面的完整加法式、CM 权与规范首项。
- R788，首 $p$ 矩形与 primitive 筛选不能省略的范围。
- 本文 (CS14)--(CS24) 给出了所用降阶和闭合障碍的完整纸面推导。
