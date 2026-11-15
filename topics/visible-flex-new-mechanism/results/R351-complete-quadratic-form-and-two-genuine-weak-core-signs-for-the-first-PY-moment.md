# R351：P–Y 第一外矩的完整二次式与两个真实弱核心符号

日期：2026-11-15。**完整纸面恒等式及有限光滑构造。** 未执行求积、符号程序、人工测试、profile 扫描或研究计算。

[R347](R347-exact-coupled-moments-and-cheap-one-sided-positive-negative-Gaussian-correction.md) 已给保持旧矩的低成本负向 P–Y 第一矩模块，也证明现有强两坡正锥不能无条件产生相反方向。因此下一问题必须回到原弱 rank-two 输入，而不是增加相同强列。

本稿把**任意真实紧 f、g** 的原 P–Y 第一矩准确化成一个关于 g 的一维二次式，加上明确的 quartic 自项。所有系数来自原完整 Pf、Yf；原左尾、right anchor 与实际积分常数均保留。随后在原 $A_f=0$ 幂段中构造两个真正光滑、导数 rank-two 的弱核心，使这个原矩分别为正、负。

**这两个核心尚未完成三矩圆配平，也未同时支付 R349 的十二旧外矩。** 本稿不把局部符号当作当前全弱圆残差的符号，更不把它登记成已完成的全门正纠正器。新增的是可直接接入完整配平问题的准确原式与真实正号入口。

来源：[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、[R308](R308-genuine-derivative-rank-two-circles-with-one-hook-and-complete-third-range.md)、[R344](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md)、[R348](R348-true-translation-and-Green-self-terms-pay-the-first-positive-minus-one-Gaussian-moment.md)及 R347。

## 1. 原对象与不预设合法三矩的标量

固定真实右锚
$$
J(F)(x)=\int_x^{r_*}F(t)\,dt.
$$
原两个对称二次场为
$$
P(u,v)=J(u''v''),
$$
$$
Y(u,v)=-xuv+\frac{x^2}{2}(uv'+u'v)
-\frac{x^3}{2}u'v'
-\frac{x^2}{4}J(x^2u''v''+2u'v').
\tag{1}
$$
设 $f,g\in C_c^\infty(I;\mathbb R)$，不要求两者此时已经三矩匹配。定义
$$
a=P(f,f),\qquad b=Y(f,f),\qquad
d_1(f,g)=I_1\{g,[P,Y](g;f^2-g^2)\},
\tag{2}
$$
其中
$$
[P,Y](g;D)=P(g,YD)-Y(g,PD),\qquad
I_1(v,w)=\int x v''w''.
$$
$a$ 的左尾一般是常数，$b$ 的左尾一般是二次多项式；下面不将它们当紧函数。

写
$$
\mu_0(g)=\int(g'')^2,\qquad
\mu_2(g)=\int(x^2(g'')^2+2(g')^2).
$$
R271 已保 local 变分及真实 Green 项证明
$$
2I_1\{g,[P,Y](g;g^2)\}=-\frac12\mu_0(g)\mu_2(g).
\tag{3}
$$
因此
$$
d_1(f,g)=I_1\{g,P(g,b)\}-I_1\{g,Y(g,a)\}
+\frac14\mu_0(g)\mu_2(g).
\tag{4}
$$
这一分解不需要 $f^2-g^2$ 的矩为零；它完全保留原自项。

若后来确实组成合法三矩圆，并用原十二副本清掉 odd，相应整个第一外矩才等于 $d_1\sin^2\theta$。不能提前对本节的任意 pair 作这个全相位声明。

## 2. P 槽的完整二次式

对任意原右零 $b$，
$$
P(g,b)''=-g'''b''-g''b'''.
$$
仅对紧 outer $g$ 分部积分，得
$$
\begin{aligned}
I_1(g,P(g,b))
&=\int\{(g'')^2+xg''g'''\}b''\\
&=\frac12\int(b''-xb''')(g'')^2.
\end{aligned}
\tag{5}
$$
全部边项含 $g''$ 或其导数，在真实 collar 为零。这里没有要求 $b,b',b''$ 的左值为零。

## 3. Y 槽的完整二次式

对任意具有所需光滑性的真实原函数 $a$，定义
$$
\boxed{
V_2[a]=\frac{2x^2a-2x^3a'+x^4a''+x^5a'''}8,
}
$$
$$
\boxed{
V_1[a]=\frac{2a-2xa'+x^2a''+5x^3a'''+x^4a^{(4)}}4,
}
$$
$$
\boxed{
V_0[a]=\frac{16xa'''+9x^2a^{(4)}+x^3a^{(5)}}4.
}
\tag{6}
$$
则准确有
$$
\boxed{
I_1\{g,Y(g,a)\}
=\int\{V_2[a](g'')^2+V_1[a](g')^2+V_0[a]g^2\}.
}
\tag{7}
$$

给出完整 IBP 接口。令 $u=g,v=g',r=g'',s=g'''$。从(1)直接求两次导数，唯一的原函数项为
$$
-\frac12J(x^2ra''+2va').
$$
乘原外权 $xr$ 后，使用
$$
(xv-u)'=xr
$$
将它准确变为
$$
-\frac12\int(xv-u)(x^2ra''+2va').
\tag{8}
$$
这一边项只有紧 $xv-u$，没有删除 $a$ 的左尾。

把所有 $rs$ 项先积分后，$r^2$ 的系数已经是 $V_2[a]$。剩余 $ur$、$vr$、$v^2$、$uv$ 项准确为
$$
D\,ur+E\,vr-xa'v^2+a'uv,
$$
$$
D=-xa'+\frac32x^2a''+\frac12x^3a''',
\qquad
E=-xa+x^2a'-\frac32x^3a''-\frac12x^4a'''.
\tag{9}
$$
利用 $ur=(uv)'-v^2$、$vr=(v^2)'/2$、$uv=(u^2)'/2$，其余两个系数是
$$
-D-\frac12E'-xa'=V_1[a],\qquad
\frac12D''-\frac12a''=V_0[a].
$$
这证明(7)，没有假设任何 primitive 常数为零。

尤其当 $a=Ax^2+Bx+C$ 时，(6)准确降为
$$
V_2[a]=Cx^2/4,\qquad V_1[a]=C/2,\qquad V_0[a]=0.
\tag{10}
$$
它与 R344 原多项式输入身份 $Y(g,a)=\frac C2D_+g$ 相符，其中 $D_+g=x^2g'-2xg$。线性、二次项准确不贡献，不是近似小量。

## 4. 任意真实弱输入的完整标量公式

合并(4)、(5)、(7)，得到
$$
\boxed{
d_1(f,g)=\mathcal Q_f(g)+\frac14\mu_0(g)\mu_2(g),
}
\tag{11}
$$
$$
\boxed{
\mathcal Q_f(g)=
\int\left[
\left\{\frac{b''-xb'''}2-V_2[a]\right\}(g'')^2
-V_1[a](g')^2-V_0[a]g^2
\right],
\quad a=Pf,\ b=Yf.
}
\tag{12}
$$
$a,b$ 仍是同一完整 $f$ 的实际右锚原函数。左侧补矩包、右侧恢复段与真实有序位置，凡能影响这些原函数，都必须照原式进入；它们不是新自由参数。

式(11)还给准确幅度依赖：
$$
d_1(f,\varepsilon g)=\varepsilon^2\mathcal Q_f(g)
+\frac{\varepsilon^4}{4}\mu_0(g)\mu_2(g).
\tag{13}
$$
这可以判断一个实际未配平核心的符号。将 $\varepsilon$ 改变以后，三矩合法性若曾成立通常会改变；不能用(13)在已有合法全圆上无条件调幅。

## 5. 朝右幂段：真实二次主系数严格为负

在某个固定紧内区间上，令
$$
f(x)=A(x-\beta)^{5/2},\qquad A\ne0,\qquad y=x-\beta>0.
\tag{14}
$$
外面以任意真实光滑紧延拓固定 $f$。这是 R308 的 $A_f=0$ 真弱段。所有 $g$ 都支持在这个内区间，故原弱 hook 保持。

在该段，
$$
f''{}^2=K y,\qquad K=\frac{225A^2}{16},
\qquad a'=-Ky,\quad a''=-K,\quad a'''=0.
$$
所以 $a$ 在核心上是一个实际二次多项式，$V_0[a]=0$，$V_1[a]$ 为实际有限常数。

记原
$$
C_f=J(x^2f''{}^2+2f'{}^2).
$$
由 R348/R349 的完整 $Yf$ 导数，(12)中 $g''{}^2$ 的系数准确为
$$
\boxed{
W_f=
-\frac{A^2}{16}
\{40y^4-110xy^3+195x^2y^2-120x^3y+75x^4\}
-\frac{C_f+x^2a}{4}.
}
\tag{15}
$$
这里 $a\ge0,C_f\ge0$ 是真实右侧积分，不能重锚成零。

大括号具有准确平方分解
$$
\begin{aligned}
&40y^4-110xy^3+195x^2y^2-120x^3y+75x^4\\
&\quad=
40(y^2-\tfrac{11}8xy)^2
+\frac{955}{8}x^2(y-\tfrac{96}{191}x)^2
+\frac{8565}{191}x^4.
\end{aligned}
\tag{16}
$$
当 $y>0$ 时严格为正，包括 $x=0$ 的情形。因此 $W_f<0$ 在整个固定核心上成立，不依赖真实右恢复尾的具体形状。

取一个非零光滑紧 $\zeta$，支持在此核心内部，并令 $g_N=\zeta\cos Nx$。完整导数展开与普通振荡积分给
$$
N^{-4}\int W_f(g_N'')^2
\longrightarrow \frac12\int W_f\zeta^2<0,
\qquad
N^{-4}\int V_1[a](g_N')^2\longrightarrow0.
$$
所以某个**有限** $N$ 已有 $\mathcal Q_f(g_N)<0$。固定这个真实 profile 后，再取有限正 $\varepsilon$ 足够小，(13)给
$$
\boxed{d_1(f,\varepsilon g_N)<0.}
\tag{17}
$$
没有执行积分或搜索 $N$；证明是严格负极限与连续有限选择，不把 $N=\infty$ 当 profile。

## 6. 朝左幂段：保右端迹后仍有真实正方向

现在固定 $\beta>0$ 和一个紧区间 $J_0\Subset(0,\beta)$。先用右侧模型
$$
f_*(x)=A(\beta-x)^{5/2},\qquad x<\beta,
$$
并在 $x\ge\beta$ 置零；在 $J_0$ 左方可任意紧截断。这个临时右端模型只有 $C^2$，仅用于计算核心上的真实积分极限，随后明确变成 $C^\infty$。

在 $J_0$ 右方直到 $\beta$，令 $y=\beta-x$。真实原函数是
$$
a_*(x)=\frac K2(\beta-x)^2,\qquad K=\frac{225A^2}{16},
\tag{18}
$$
$$
C_*(x)=K\int_x^\beta
\left[t^2(\beta-t)+\frac89(\beta-t)^3\right]dt.
$$
故(10)给
$$
V_1[a_*]=\frac{225A^2\beta^2}{64},\qquad
V_2[a_*]=\frac{225A^2\beta^2x^2}{128},\qquad V_0[a_*]=0.
\tag{19}
$$

令 $b_*=Yf_*$。核心上的完整导数为
$$
b_*'''=-\frac{15A^2}{32}x(9x^2+10\beta x+16\beta^2).
\tag{20}
$$
这里必须保右端的真实迹：
$$
\boxed{b_*''(\beta-)=-\frac{225A^2\beta^4}{64},}
\tag{21}
$$
因为 $f_*''f_*'''\to-225A^2/32$。即使 $f_*$ 自身在右端 $C^2$ 归零，也不能把 $b_*''(\beta-)$ 当作零；它不是一个已平滑的二次场 collar。

将(20)从这个真实迹积分，再代(19)，得到
$$
\boxed{
W_*:=\frac{b_*''-xb_*'''}2-V_2[a_*]
=\frac{15A^2}{64}
\left(
\frac{73}{12}\beta^4+\frac{27}{4}x^4
+\frac{20}{3}\beta x^3+\frac12\beta^2x^2
\right)>0
}
\tag{22}
$$
对 $0<x<\beta$ 成立。常数是 $73/12$，来自(21)的非零端迹；错误删除该迹会得到不同常数。

### 6.1. 真正光滑紧输入保留正号

取固定光滑 cutoff，使 $f_\epsilon=f_*$ 于 $y\ge\epsilon$，在 $y\le\epsilon/2$ 恒零；在 $J_0$ 左方用固定光滑截断。对足够小有限 $\epsilon>0$，$f_\epsilon\in C_c^\infty$，并在整个 $J_0$ 仍准确等于原朝左幂段。

右端修补区的 $f_\epsilon''$ 量级为 $O(\epsilon^{1/2})$，宽度 $O(\epsilon)$。所以该区给 $a_\epsilon-a_*$、$C_\epsilon-C_*$ 的实际尾积分均为 $O(\epsilon^2)$。在整个固定核心上，这两个差都是常数，因局部 $f$ 没有改变。

因而
$$
W_{f_\epsilon}-W_*
=-\frac{C_\epsilon-C_*}{4}
-\frac{x^2(a_\epsilon-a_*)}{4},
\qquad
V_1[a_\epsilon]-V_1[a_*]=\frac{a_\epsilon-a_*}{2}.
\tag{23}
$$
$V_0=0$ 仍准确。由核心紧性，某个有限正 $\epsilon$ 已使 $W_{f_\epsilon}>0$ 在整个 $J_0$ 一致成立。这里没有把理想 $C^2$ 端本身当作最终输入，也没有对其三阶导数作不存在的一致收敛宣称；只使用了(23)中实际所需的两个尾积分。

固定这个真实 $f_\epsilon$。再取非零紧 $\zeta\subset J_0$，用同样的有限频率论证，某个有限 $N$ 使
$$
\mathcal Q_{f_\epsilon}(\zeta\cos Nx)>0.
$$
由(13)的 quartic 自项非负，对任意有限非零实幅 $\eta$，都有
$$
\boxed{
d_1(f_\epsilon,\eta\zeta\cos Nx)>0.
}
\tag{24}
$$
全部函数现在真实光滑、紧支撑，原锚与原 $P,Y$ 都未改变。

## 7. 两个核心是真弱 rank-two，尚不是完成三矩的圆

在两种构造中，$g$ 的支撑都在原 $A_f=0$ 段内；外面 $g$ 和所有导数为零。因此 R306/R308 的弱 hook $A_fW=0$ 原式成立。

同时 $W=g'f''-f'g''$ 不可能恒零：在核心 $f'\ne0$，若 $W=0$，则 $(g'/f')'=0$；由 $g$ 在核心两端附近恒零，常数只能为零，于是 $g=0$，与选择矛盾。故这里是实际导数 rank-two 输入，未退回 R304/R306 已排除的强 rank-one 类。

不过，上面没有把 $I_j(f,f)=I_j(g,g)$、$I_j(f,g)=0$ 同时强加给这些核心。为了形成原合法三矩圆，仍须执行真实补矩与完整复制。那些步骤的贡献由 R263 的原完整拼接式控制：
$$
T(A\star B)=T(A)+T(B)
+\Gamma\{O_{M_A},D_{M_B}\}.
$$
在 partial blocks 上，不能假设最后一项为零。特别 P–Y 第一核是
$$
\Gamma_{P,Y,1}(m,n)=-\frac12(m_0n_2+m_2n_0).
\tag{25}
$$
补偿包的原矩、左右次序和 local self 必须共同入账。

因此(24)是一个真实正号核心来源，**不是已完成的正号完整模块**。R347 的已付负纠正器已经合法并保持旧门，二者证据层次不同；不能以本稿的正核直接抵消它。

## 8. 当前接入任务与准确边界

当前 R349 弱圆已付四个 pair 的十二外矩。P–Y 第一矩只剩一个共同 even 标量，但其当前值必须由整个最终 $f,g$ 按(11)—(12)读取，包含全部弱核心、宽恢复、补偿包、强控制及实际中心。

下一步有两个具体入口：

1. 在原 R331/R339/R341 的实际补矩、三最终中心与负 $\Psi$ 结构中，利用(11)计算完整残差并证明它能保持正号，随后用 R347 型合法负模块准确清除；
2. 以(24)的朝左真实核心为起点，完整支付(25)的有序代价、三矩和全部十二旧外矩，形成真正可接入的正纠正器。

若使用 R349 的新十目标正核，R347 的同权半平面论证也逐列适用：新四列仍来自同一有限大间距母族，所以该核给一个保持十二旧矩的严格负 P–Y 第一矩模块，伸缩成本仍为 $H^{-3}$。这并不补上正方向的合法性。

本文完成的是通用准确二次式、保右端迹的真实光滑正/负弱核心，以及它们与完整配平任务之间的明确接口。没有把 P–Y 的任何新全外矩标为已付，没有宣称剩余 Gaussian、完整第四 period、同一个 gauge 或最终等距曲面已完成。
