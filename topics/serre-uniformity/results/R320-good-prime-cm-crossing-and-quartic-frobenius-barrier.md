# R320：好素数处的两个 CM 特化与四次方 Frobenius 障碍

日期：2026-11-13。状态：**已证明；真正全局同构强制的新增必要条件，主要目标仍 OPEN。**

R317 表明，全部变化坏素数处都能匹配，仍不足以构造全局同构。
本篇使用另一组互素整数的素因子：
$$
F_a=2a^3-1,\qquad \gcd(F_a,1-a^3)=1.
$$
它们给的是好约化素数。
在这些素数处，实际曲线分别变成两个固定 CM 模型；
给定的同一个全局模 $p$ 同构，因而迫这两个模型的整数 Frobenius 迹同余。
当 $p\equiv5\pmod {12}$，两个不同 CM 域在 $p$ 的分裂类型不同，
可把部分模 $p$ 迹同余自动提高到模 $p^2$。

主要结论之一是：
$$
q\equiv1\pmod {12},\quad q\mid(2a^3-1),\quad
p\equiv5\pmod {12}
\quad\Longrightarrow\quad
\boxed{q\ge p^4+8p^2+4.}
$$
没有使用变化导子的小素数假设。

## 1. 同一个实际全局同构与好约化特化

保留 R315、R317 的实际范围：
$$
\begin{gathered}
p>37,\qquad p\equiv2,5\pmod9,\qquad
r=1-a^3=db^3,\qquad a,b\in\mathbb Z,\quad d>0\text{ 立方自由},\\
a\ne0,1,\quad b\ne0,\qquad
H_a:y^2=x^3+3arx-r(2a^3-1),\\
B_a:y^2=x^3-\varepsilon r,\qquad
\varepsilon=-1\ (4\mid a),\quad
\varepsilon=1\ (a\equiv1\pmod {32}),\\
\phi:H_a[p]\xrightarrow{\sim}B_a[p]
\quad\text{为原来实际 }G_{\mathbb Q}\text{-模同构}.
\end{gathered}
\tag{320.1}
$$
由实际 $p$ 惯性条件，$p\mid r$，
所以 $a\equiv1\pmod p$。
定义三个固定椭圆曲线
$$
G:y^2=x^3+3x,\qquad
J_\varepsilon:y^2=x^3-2\varepsilon,\qquad
J_1^0:y^2=x^3+1.
\tag{320.2}
$$
$G$ 的 CM 域为 $\mathbb Q(i)$；
后两者的 CM 域为 $\mathbb Q(\sqrt{-3})$。
它们在 $q\ge5$ 好约化。写各自的整数迹为
$g_q,j_{\varepsilon,q},t_q$。

**引理 320.1。** 若 $q\ge5$ 为素数且
$q\mid F_a=2a^3-1$，则 $q\ne p$，$q\nmid r$，
两条实际曲线在 $q$ 好约化，且有 $\mathbb F_q$ 上的同构
$$
H_a\bmod q\simeq G\bmod q,\qquad
B_a\bmod q\simeq J_\varepsilon\bmod q.
\tag{320.3}
$$
所以原来全局 $\phi$ 强迫
$$
g_q\equiv j_{\varepsilon,q}\pmod p.
\tag{320.4}
$$

**证明。** 恒等式 $2r+F_a=1$ 给互素性；
$F_a\equiv1\pmod p$ 给 $q\ne p$。
两条原短模型的判别式均为 $-432r^2$，故在 $q\ge5$ 好约化。
在 $\mathbb F_q$ 中，$a$ 是单位，
$a^3=1/2$、$r=1/2$。
对两边都作
$$
x=a^2X,\qquad y=a^3Y.
\tag{320.5}
$$
$H_a$ 的线性系数变为
$3ar/a^4=3$，常数项为零；
$B_a$ 的常数项变为
$-\varepsilon r/a^6=-2\varepsilon$。
于是得到 (320.3)。
将给定全局同构限制到这个好素数的分解群，
比较 Frobenius 特征多项式，便得到 (320.4)。$\square$

这一步没有在各处另选一个局部同构来代替 $\phi$。
R317 的比较族未必满足 (320.4)，因为那些族没有这样的全局 $\phi$。

## 2. 两个 CM 迹的整数范数表示

本节列出所需的初等有限域事实，并给出范数式的证明。

**引理 320.2。**

1. 若 $q\equiv3\pmod4$，则 $g_q=0$。
   若 $q\equiv1\pmod4$，存在整数 $x,y$，使
   $$
   g_q=2x,\qquad q=x^2+y^2,\qquad x,y\ne0.
   \tag{320.6}
   $$
2. 对任意 $c\in\mathbb F_q^\times$，
   若 $q\equiv2\pmod3$，曲线 $y^2=x^3+c$ 的迹为零。
   若 $q\equiv1\pmod3$，其迹是某个
   $\pi\in\mathbb Z[\zeta_3]$ 的迹，且 $\pi\bar\pi=q$。
   若该整数迹为偶数，可准确写为
   $$
   a_q=2u,\qquad q=u^2+3v^2,\qquad u,v\in\mathbb Z,\quad u,v\ne0.
   \tag{320.7}
   $$

这些表示中的实坐标由相应曲线的**实际整数迹**确定，
不允许事后选择有利的迹符号。

**证明。** 用 $\psi$ 表示二次特征，非平凡乘法特征在零处延拓为零。
对 $q\equiv3\pmod4$，
$x\mapsto-x$ 将
$\sum_x\psi(x^3+3x)$ 变为其负数，故该和及迹都为零。
对 $q\equiv2\pmod3$，立方映射双射，
$\sum_x\psi(x^3+c)=\sum_z\psi(z+c)=0$。

现设 $q\equiv1\pmod4$，取四次特征 $\chi$。
对 $A\ne0$，把 $t=x^2$ 作为变量，可得
$$
\sum_x\psi(x^3+Ax)
=\psi(A)\left[
\chi(-A)J(\chi,\psi)+
\bar\chi(-A)J(\bar\chi,\psi)
\right],
\tag{320.8}
$$
其中
$J(\alpha,\beta)=\sum_t\alpha(t)\beta(1-t)$。
确实，每个非零 $t$ 的两个平方根所贡献的系数为
$(1+\psi(t))\chi(t)=\chi(t)+\bar\chi(t)$，
再作 $t=-Az$ 即得上式。
$J(\chi,\psi)$ 属于 $\mathbb Z[i]$。
对这里的非平凡特征及其非平凡乘积，Gauss 和恒等式
$$
J(\alpha,\beta)=
\frac{\mathcal G(\alpha)\mathcal G(\beta)}
     {\mathcal G(\alpha\beta)},\qquad
|\mathcal G(\alpha)|^2=q
\tag{320.9}
$$
给 $|J(\alpha,\beta)|^2=q$；
这两个恒等式直接来自有限域加法特征的正交性。
于是取
$\pi=-\psi(A)\chi(-A)J(\chi,\psi)\in\mathbb Z[i]$，
其迹为相应椭圆曲线的迹，范数为 $q$。
令 $A=3$，得到 (320.6)。
若任一坐标为零，会使素数 $q$ 成为整数平方，故两坐标非零。

若 $q\equiv1\pmod3$，改取三次特征 $\chi$。
立方的原像个数为 $1+\chi(t)+\bar\chi(t)$，所以
$$
\sum_x\psi(x^3+c)
=\psi(c)\left[
\chi(-c)J(\chi,\psi)+
\bar\chi(-c)J(\bar\chi,\psi)
\right].
\tag{320.10}
$$
相同 Gauss 和论证给
$\pi=-\psi(c)\chi(-c)J(\chi,\psi)\in\mathbb Z[\zeta_3]$，
其迹为 $a_q$、范数为 $q$。
写
$\pi=(s+t\sqrt{-3})/2$，$s,t\in\mathbb Z$ 且同奇偶。
若迹 $s$ 偶，两个数都偶，便得到 (320.7)。
$v=0$ 会使 $q$ 为平方，$u=0$ 会使 $q=3v^2$；
对 $q\ge5$ 均不可能。$\square$

## 3. 准确的二挠点整除与非零迹差

以下仍设 $q\ge5$、$q\mid F_a$。
注意 $2=(a^{-1})^3$ 在 $\mathbb F_q$ 中是立方。

**引理 320.3。**

$$
\begin{array}{c|c|c|c}
q\bmod12&g_q&j_{\varepsilon,q}&
(g_q-j_{\varepsilon,q})/4\\ \hline
5&4\mathbb Z\setminus\{0\}&0&\text{非零整数}\\
7&0&4\mathbb Z\setminus\{0\}&\text{非零整数}\\
1&2+4\mathbb Z&2+4\mathbb Z&\text{非零整数}\\
11&0&0&0
\end{array}
\tag{320.11}
$$

**证明。** 若 $q\equiv5\pmod {12}$，
$3$ 和 $-3$ 都是模 $q$ 非平方。
$G$ 因此只有一个非零有理二挠点 $(0,0)$。
若它有四阶有理点，则其倍点必须为 $(0,0)$；
由倍点公式
$$
x([2]P)=\frac{(x(P)^2-3)^2}
                  {4x(P)(x(P)^2+3)}
\tag{320.12}
$$
会迫 $x(P)^2=3$，不可能。
故 $\#G(\mathbb F_q)\equiv2\pmod4$。
$q+1\equiv2\pmod4$，所以 $g_q\equiv0\pmod4$；
由 (320.6)，该迹非零。
$J_\varepsilon$ 的迹则因 $q\equiv2\pmod3$ 为零。

若 $q\equiv7\pmod {12}$，$g_q=0$。
$J_\varepsilon$ 的二挠点方程为 $X^3=2\varepsilon$。
这里右边为立方，且 $\mu_3\subset\mathbb F_q$，
所以它的全部二挠点有理，
$4\mid\#J_\varepsilon(\mathbb F_q)$。
$q+1\equiv0\pmod4$，故 $j_{\varepsilon,q}\equiv0\pmod4$，
并由 (320.7) 非零。

若 $q\equiv1\pmod {12}$，
$-3$ 为平方，所以 $G$ 也有全部二挠点有理；
$J_\varepsilon$ 的全部二挠点有理同上。
两条曲线的迹因而均为 $q+1\equiv2\pmod4$。
按引理 320.2 写
$$
q=x^2+y^2=u^2+3v^2,\qquad
g_q=2x,\quad j_{\varepsilon,q}=2u.
\tag{320.13}
$$
此时 $x,u$ 奇，$y,v$ 偶。
若两个迹相等，则 $x=u$，所以 $y^2=3v^2$。
整数中只能 $y=v=0$，与 (320.6)–(320.7) 矛盾。
故迹差确实非零。
最后 $q\equiv11\pmod {12}$ 时两条迹均为零。$\square$

## 4. 好素因子的二次方与四次方下界

**定理 320.4。** 在实际范围 (320.1) 中，
对每个 $q\ge5$、$q\mid F_a$，有
$$
\boxed{
\begin{array}{c|c}
q\bmod12&\text{必要下界或条件}\\ \hline
5&q\ge4p^2+1\\
7&q\ge4p^2+3\\
1&q>p^2\\
1,\ p\equiv5\bmod12&q\ge p^4+8p^2+4\\
11&\text{本比较不给下界}
\end{array}}
\tag{320.14}
$$
前两行还给精确表示
$$
\begin{aligned}
q\equiv5\pmod {12}:&\quad
q=4p^2h^2+y^2,\quad h\ne0,\quad y\text{ 奇且非零},\\
q\equiv7\pmod {12}:&\quad
q=4p^2h^2+3v^2,\quad h\ne0,\quad v\text{ 奇且非零}.
\end{aligned}
\tag{320.15}
$$

**证明。** 在第一行，(320.4) 迫 $p\mid g_q$；
由 (320.11)，可写 $g_q=4ph$，$h\ne0$。
于是 (320.6) 给第一条 (320.15)。
因 $q\equiv1\pmod4$ 且 $2ph$ 偶，另一坐标必须奇，
故下界为 $4p^2+1$。
第二行同理，$j_{\varepsilon,q}=4ph$，
由 Eisenstein 范数给第二条 (320.15)；
$q\equiv3\pmod4$ 迫 $v$ 奇，故下界为 $4p^2+3$。

对 $q\equiv1\pmod {12}$，
(320.11) 的非零迹差是四的倍数，
又被 $p$ 整除，所以其绝对值至少 $4p$。
Hasse 界给差的绝对值至多 $4\sqrt q$，
故 $q\ge p^2$；因 $q$ 为素数且 $q\ne p$，实际严格大于 $p^2$。

现另设 $p\equiv5\pmod {12}$，使用 (320.13)。
由 (320.4)，$x\equiv u\pmod p$，所以
$$
y^2\equiv3v^2\pmod p.
\tag{320.16}
$$
但 $(3/p)=-1$，故 $p\mid y$ 且 $p\mid v$。
由于它们为非零偶数，写
$$
y=2ps,\qquad v=2pt,\qquad s,t\in\mathbb Z\setminus\{0\}.
\tag{320.17}
$$
又因 $q\ne p$，从 $q\equiv x^2\pmod p$ 得 $x\not\equiv0\pmod p$。
$x\equiv u\pmod p$ 遂使 $x+u$ 为 $p$ 进单位。
两个范数相等给
$$
(x-u)(x+u)=4p^2(3t^2-s^2),
$$
因此 $p^2\mid x-u$。
$x,u$ 都奇，且两迹不相等，所以可准确写成
$$
x-u=2p^2h,\qquad h\in\mathbb Z\setminus\{0\},\qquad
z=(x+u)/2\in\mathbb Z.
\tag{320.18}
$$
于是
$$
\boxed{
hz=3t^2-s^2,\qquad
q=z^2+p^4h^2+2p^2s^2+6p^2t^2.
}
\tag{320.19}
$$
$z$ 也非零，否则会有 $s^2=3t^2$。
由 $x=z+p^2h$ 为奇，$z$ 和 $h$ 奇偶相反。
若 $|h|=1$，$z$ 为非零偶数，故 $z^2\ge4$；
再用 $s^2,t^2\ge1$，得到 $q\ge p^4+8p^2+4$。
若 $|h|\ge2$，则
$q\ge4p^4+8p^2+1\ge p^4+8p^2+4$。
最后一条实质下界得证。$\square$

这里的模 $p^2$ 提升是两个固定 CM 范数及同一个好素数
Frobenius 的特殊结果：
$$
p\equiv5\pmod {12},\quad q\equiv1\pmod {12},\quad q\mid F_a
\quad\Longrightarrow\quad
p^2\mid\frac{g_q-j_{\varepsilon,q}}4.
\tag{320.20}
$$
它不声称全局 $H_a[p^2]\simeq B_a[p^2]$，
也不把一次模 $p$ 同构任意提高到高阶。

**推论 320.5。** 对 (320.14) 中 $q\equiv5$ 或 $7\pmod {12}$
的素因子，均有
$$
\left(\frac{-p}{q}\right)=1.
\tag{320.21}
$$
若另有 $p\equiv5\pmod {12}$，
该式对 $q\equiv1\pmod {12}$ 的素因子也成立。

**证明。** 第一种由 $q\equiv y^2\pmod p$，
$q\ne p$，及 $q\equiv1\pmod4$ 的二次互反律立即得到。
第二种由 $q\equiv3v^2\pmod p$，
故 $(q/p)=(3/p)$；由于 $q\equiv3\pmod4$，
$$
(p/q)=(-1/p)(q/p)=(-3/p)=-1.
$$
再乘 $(-1/q)=-1$ 即得 (320.21)。
第三种由 (320.17) 给 $q\equiv x^2\pmod p$，
同第一种使用互反律。$\square$

## 5. 奇分支中整除 a 的另一组好素数

**定理 320.6。** 在实际奇分支
$a\equiv1\pmod {32}$、$B_a=A_{-r}$ 中，
若 $q\equiv7\pmod {12}$ 为 $a$ 的素因子，则
$$
\boxed{
q=4p^2h^2+3v^2\ge4p^2+3,\qquad
h\equiv1\pmod3,\quad v\text{ 奇且非零},
}
\tag{320.22}
$$
并且 $(-p/q)=1$。

**证明。** $q\mid a$ 给 $r\equiv1\pmod q$，
所以 $q\ge5$ 在两曲线都是好素数，且 $q\ne p$。
约化分别为
$$
H_a\bmod q:\ y^2=x^3+1,\qquad
B_a\bmod q:\ y^2=x^3-1.
\tag{320.23}
$$
第二条是第一条的非平凡未分歧二次扭曲，
因为 $q\equiv3\pmod4$。
两整数迹为 $t_q,-t_q$，所以给定全局同构迫 $p\mid t_q$。
$q\equiv1\pmod3$ 使 $J_1^0$ 的全部二挠点有理；
它还具有有理三阶点 $(0,1)$。
故 $12\mid\#J_1^0(\mathbb F_q)$，以及
$$
t_q\equiv q+1\equiv8\pmod {12}.
\tag{320.24}
$$
特别 $t_q=4ph$。
因 $p\equiv2\pmod3$，(320.24) 给 $h\equiv1\pmod3$。
引理 320.2 的范数式和奇偶性给
$q=(2ph)^2+3v^2$，$v$ 非零且奇，
得到 (320.22)。二次互反律同推论 320.5。$\square$

这个限制没有移到偶分支：
当 $4\mid a$，指定参考为 $A_r$，
在 $q\mid a$ 时两条约化都是 $y^2=x^3+1$，
不会出现上述两迹相反的比较。

## 6. 可直接使用的全局整数迹证书

对给定允许的整数 $a$ 和对应符号 $\varepsilon$，
定义
$$
D_\varepsilon(q)=\frac{g_q-j_{\varepsilon,q}}4
\quad
(q\ge5,\ q\mid F_a),
\tag{320.25}
$$
它由 (320.11) 始终为整数，
并且准确在 $q\equiv11\pmod {12}$ 时为零。
再定义
$$
\begin{aligned}
G_1(a)&=\gcd\{|D_\varepsilon(q)|:
                    q\mid F_a,\ q\equiv1\pmod {12}\},\\
G_{57}(a)&=\gcd\{|D_\varepsilon(q)|:
                    q\mid F_a,\ q\equiv5,7\pmod {12}\}.
\end{aligned}
\tag{320.26}
$$
若为奇分支，另定义
$$
G_a(a)=\gcd\{|t_q/4|:q\mid a,\ q\equiv7\pmod {12}\}.
\tag{320.27}
$$
空集合的 gcd 定义为零，仅表示该组没有约束。
非空集合中的各项均非零；以上三个 gcd 可以只用三个固定 CM
曲线的有限域迹计算，不需要先构造实际非 CM 曲线的除法域。

原来全局同构必满足
$$
p\mid G_1(a),\qquad p\mid G_{57}(a),
\qquad p\mid G_a(a)\ \text{（奇分支）}.
\tag{320.28}
$$
当 $p\equiv5\pmod {12}$ 时，还必须
$$
\boxed{p^2\mid G_1(a).}
\tag{320.29}
$$
例如一个非零 $G_1(a)$ 若没有大于三十七的
$5\pmod {12}$ 素数的平方因子，
就严格排除该 $a$ 在整个相应 $p$ 分支中的实际同构。
这是一条精确的可复核整数证书，而不是用有限次扫描证明一般结论。

## 7. 全局意义与尚未闭合的部分

这些素数全部位于原来的好约化支撑上：
$F_a$ 与 $r$ 互素，奇分支额外使用的 $a$ 也与 $r$ 互素。
因此 (320.14)、(320.20)、(320.22) 是 R317 的全部坏处匹配
没有自动给出的新条件。

然而本篇没有证明，对每个实际非 CM 参数，
$F_a$ 必有一个落在禁止大小范围的素因子，
也没有统一控制 (320.26)–(320.27) 的 gcd。
若 $F_a$ 的有关素因子都为 $11\pmod {12}$，
或者其余素因子已经足够大，单独这些条件仍可能无矛盾。
尚需把指定全局表示的所有好素数迹关系、
传输的 Selmer 类或其他整体约束合在一起。
这里不把四次方素因子下界反用成参数或导子的上界。

## 8. 依赖与证明输入

- **R289、R301、R306、R315、R317**：
  同一个实际整数参数、CM 扭曲符号、
  原来的全局模 $p$ 同构和 $a\equiv1\pmod p$。
  本文对奇偶分支分别保留这个符号。
- 好约化处的模 $p$ Frobenius 特征多项式、
  Weil/Hasse 界、有限域乘法与加法特征的正交性，
  以及二次互反律是本篇使用的标准基础事实。
  两个 CM 范数式通过 (320.8)–(320.10) 的 Jacobi 和
  重新推导，未调用未核证的最新 CM 分类。
- 全部新增特化、整除、非零性和二次型不等式均在正文证明；
  纯证明条目，无脚本、数值扫描或外部计算证书依赖。
