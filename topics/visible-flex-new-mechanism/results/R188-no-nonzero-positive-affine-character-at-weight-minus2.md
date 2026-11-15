# R188：权 −2 不存在非零正仿射字符

日期：2026-11-15。**纸面已证明。** 主推导由 root 完成，tail_cost 独立核对并整理本稿；本文对所述数学结论负责，不把未执行的新计算计作证据。本文只使用已发表的完整权 −2 函数核、字符参数化及真实 action 定理，不进行新 profile、几何或符号计算。

依据 [R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)、[R164](R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)、[R175](R175-complete-highest-action-sharp-two-by-two-criterion-after-original-relations.md) 和 [R186](R186-complete-weight-minus2-function-kernel-and-five-dimensional-character-head.md)。

**定理。** 若 $\lambda$ 是真实完整成本空间 U 上的权 −2 仿射字符，杀掉 R，并在全部实际 $M=T=0$ 成本上非负，则

$$
\boxed{\lambda=0.}
\tag{1}
$$

这里 U、R、真实成本闭锥和完整 canonical 右锚约定均沿用既有结果。结论只排除**权 −2** 的非零正仿射字符，不据此宣称其他偶权也已排除、整个闭锥已等于 U，或任意负成本已经由实际有限词实现。

## 1. 完整五参数及正性首先迫 m=0

R186 已支付全部同权真实函数关系和完整平移分母，真字符由五个实参数

$$
(\alpha,\beta,a,\delta,m)
$$

唯一决定。最高层 R175 矩阵在该真头部上为

$$
M=m\begin{pmatrix}-5/16&-7/4\\-7/4&-7/4\end{pmatrix},
\qquad \det M=-\frac{161}{64}m^2.
$$

真实正字符必须满足 $M\succeq0$，故 $m=0$。此时完整最高层不再含 $k'$、$k''$；这不是删项，而是已支付原函数关系后的准确结果。

置

$$
r=\log h,\qquad v=r',
$$

并记

$$
B=\frac{15\delta-4\alpha-8\beta-12a}{26},\qquad
C_1=\frac{8\alpha-10\beta-28a-43\delta}{26}.
\tag{2}
$$

R140 的**同一个**八矩乘子由 R164 固定；扣去它以后，对全部真实有限开平端水平路径，完整 action 必须非负。R186 给其准确式

$$
\begin{aligned}
I[h,k]=\int e^{-2r}\bigg\{&a(v'+v^2)^2-\frac{7a+\beta}{3}v^4
+B(k')^2+C_1kvk'\\
&+(-\alpha-\beta+\delta k^2)v^2
+(1+k^2)(\alpha+\beta k^2)\bigg\}\,ds\ge0.
\end{aligned}
\tag{3}
$$

整个式子保留静态、二次、四次层以及同一乘子修正。真实几何满足 $h>0$、$\omega'=k'/(2h)$。式 (3) 已独立于 $\omega$，但下文构造仍实际积分这个约束。

长常态段给 $\alpha,\beta\ge0$；加速度正性给 $a\ge0$。R148 的固定 k=0 锐利最高层门还给 $0\le\beta\le4a/3$。后文将得到更强的 $\beta=a$。

另有必要条件

$$
\boxed{B\ge0.}
\tag{4}
$$

证明取 $h\equiv1$，以及任意非恒定 $\varphi\in C_c^\infty(0,1)$，令 $k(s)=\varphi(s/t)$。其真实 $\omega$ 可取 $\omega_0+k/2$，两端为常值 germs。此时全部最高层为零，而 (3) 等于

$$
t^{-1}B\int_0^1(\varphi')^2
+t\int_0^1(1+\varphi^2)(\alpha+\beta\varphi^2).
$$

若 $B<0$，充分小的有限 $t>0$ 给负 action，矛盾。

## 2. p、y 变量和必须保留的联合缩放

设

$$
p=\frac1h>0,\qquad y=pk,
$$

以及

$$
S=B+\frac{C_1}{2}=-\frac\delta4-\frac\beta2-a,
\qquad T=\frac{C_1}{2}+\delta.
\tag{5}
$$

对平端路径分部积分；对周期路径则按相同周期边界处理。由

$$
\int\frac{p''(p')^2}{p}\,ds
=\frac13\int\frac{(p')^4}{p^2}\,ds
$$

和二次层的交叉项，(3) 准确化为

$$
\begin{aligned}
I[p,y]=\int\bigg\{&a(p'')^2+\frac{a-\beta}{3}\frac{(p')^4}{p^2}
+B(y')^2+S\frac{p''y^2}{p}+T\frac{(p')^2y^2}{p^2}
+\beta\frac{y^4}{p^2}\\
&-(\alpha+\beta)(p')^2+\alpha p^2+(\alpha+\beta)y^2\bigg\}\,ds.
\end{aligned}
\tag{6}
$$

把第一行的六项积分记为 $E[p,y]$。它不是仅按时间缩放就齐次的四阶量；必须同时缩放 k。固定一条有限平端形状 $p>0,y$，对 $t>0$ 定义

$$
h_t(s)=\frac1{p(s/t)},\qquad
k_t(s)=t^{-1}\frac{y(s/t)}{p(s/t)}.
\tag{7}
$$

相应 $y_t=p_tk_t=t^{-1}y(s/t)$，故

$$
I[h_t,k_t]
=t^{-3}E[p,y]
+t^{-1}(\alpha+\beta)\int\bigl(y^2-(p')^2\bigr)
+t\alpha\int p^2.
\tag{8}
$$

每个固定 $t>0$ 都给真实有限光滑路径；$\omega_t$ 按实际约束积分，虽可随 t 变大，但对该有限路径仍有界，随后可选择共同合法 profile 区间。没有假设外加的统一 h、k、长度盒。

因此正性强制

$$
\boxed{E[p,y]\ge0\quad\text{对全部有限平端 }p>0,y.}
\tag{9}
$$

若找到负 E 的周期形状，则先固定它，复制足够多个周期，再接两条固定光滑平端连接，使总 E 为负；再使用 (7)–(8)。所以 (9) 也迫使每个真实可重复周期的 E 非负。连接的完整成本不删除，只用有限重复让固定成本被严格负的周期和压过。

## 3. 周期族 k=K h² 迫使 beta=a

取

$$
h(\tau)=(1+b\cos\tau)^{-1/2},\quad
0<b<1,\quad d=\sqrt{1-b^2},\quad
k=Kh^2.
\tag{10}
$$

此时 $p=\sqrt{1+b\cos\tau}$、$y=K/p$，并且

$$
\omega'=\frac{k'}{2h}=Kh',
$$

所以可取 $\omega=\omega_0+Kh$，整个标量状态准确周期。K 是任意有限实数，不是带符号时间。

对 (6) 第一行积分，使用

$$
\int\frac{p''}{p^3}=3\int\frac{(p')^2}{p^4},
\qquad B+3S+T=-2\beta-4a,
$$

得到

$$
E=I_4-(2\beta+4a)K^2Z+\beta K^4W,
\tag{11}
$$

其中

$$
\boxed{
I_4=\frac{\pi(1-d)\{4a(1+d)-\beta(1-d)\}}{16d},\quad
Z=\frac{\pi(1-d^2)}{4d^3},\quad
W=\frac{\pi(3-d^2)}{d^5}.
}
\tag{12}
$$

### 3.1 三个积分的手推

置 $u=1+b\cos\tau$。标准一周积分由 $\tan(\tau/2)$ 代换或对参数求导得

$$
\int u^{-1}=\frac{2\pi}{d},\qquad
\int u^{-2}=\frac{2\pi}{d^3},\qquad
\int u^{-3}=\frac{\pi(3-d^2)}{d^5}.
$$

并有 $u''=1-u$、$(u')^2=-u^2+2u-d^2$。于是

$$
Z=\frac14\int\frac{(u')^2}{u^3}
=\frac14\left(-\int u^{-1}+2\int u^{-2}-d^2\int u^{-3}\right),
$$

给出 (12) 的 Z，W 即 $\int u^{-3}$。再令

$$
A_*=\int\frac{(u'')^2}{u}=\frac{2\pi(1-d)}d,
\qquad C_*=\int\frac{(u')^4}{u^3}=\frac{3\pi(1-d)^2}d.
$$

后式可直接展开 $(-u^2+2u-d^2)^2/u^3$ 后使用上面三个积分。周期边界给

$$
\int\frac{u''(u')^2}{u^2}=\frac23C_*.
$$

由 $p=\sqrt u$ 展开得到

$$
I_4=a\int(p'')^2+\frac{a-\beta}{3}\int\frac{(p')^4}{p^2}
=\frac a4A_*-\frac{4a+\beta}{48}C_*,
$$

即 (12)。这里没有数值求积。

### 3.2 各分支

若 $\beta>0$，(9) 对所有 $K^2\ge0$ 强制二次式 (11) 的最小值非负。因 $a\ge0$，其极小点在非负半轴，故

$$
4\beta WI_4\ge(2\beta+4a)^2Z^2.
$$

令 $d\downarrow0$，代 (12) 后得

$$
3\beta(4a-\beta)\ge(\beta+2a)^2.
$$

两边之差准确为 $-4(\beta-a)^2$，因此 $\beta=a$。

若 $\beta=0,a>0$，任取一个 $0<b<1$，则 $Z>0$，(11) 随 $K^2$ 具有严格负的线性项；取充分大的有限 K 即有负 E，矛盾。若 $\beta=a=0$ 则无需这一步。综合得到

$$
\boxed{\beta=a.}
\tag{13}
$$

## 4. 一条近零成本长路径迫使最后交叉系数相容

现在设 $\beta=a$。在整条实线上取

$$
p_0(x)=\sqrt{1+x^2},\qquad y_0(x)=\frac1{p_0(x)},
\qquad A_*:=\frac{2a-\delta}{4}.
$$

将其代入 E 的密度，准确得到

$$
\frac{A_*(1-3x^2)}{(1+x^2)^3}
=A_*\frac{d}{dx}\frac{x}{(1+x^2)^2}.
\tag{14}
$$

因两端原函数趋零，整线积分为零。我们不直接把这条无限路径当作允许控制，而用下面的有限正平帽。

取固定 $\chi\in C_c^\infty(\mathbb R)$，$0\le\chi\le1$，在 $[-1,1]$ 为 1，在 $|x|\ge2$ 为 0。对 $R\ge1$，在 **$[-3R,3R]$** 上定义

$$
p_R(x)=\chi(x/R)p_0(x)+(1-\chi(x/R))2R,
\qquad y_R(x)=\frac{\chi(x/R)}{p_R(x)}.
\tag{15}
$$

$p_R>0$，而在两端整段 collar 上 $p_R=2R,y_R=0$，所以对应 h、k 有真实常值 germs。对 $R\le|x|\le2R$，有一致估计

$$
p_R\asymp R,\quad p_R'=O(1),\quad p_R''=O(R^{-1}),\quad
y_R=O(R^{-1}),\quad y_R'=O(R^{-2}).
$$

因此帽区的 E 成本为 $O(R^{-1})$；中心区由 (14)，遗漏尾部也趋零。于是

$$
E[p_R,y_R]\longrightarrow0.
\tag{16}
$$

现取任意固定 $\eta\in C_c^\infty(\mathbb R)$。充分大的 R 使其支撑完全落在 $p_R=p_0,y_R=y_0$ 的中心区。对每个实 t，$p_R,y_R+t\eta$ 仍为合法有限平端形状，故 E 非负。让 $R\to\infty$，再看 t=0 两侧的一阶项，必有

$$
\left.\frac{d}{dt}\right|_{t=0}E[p_0,y_0+t\eta]=0.
$$

第一变分除以 2 的 Euler 表达式为

$$
-B y_0''+
\left(S\frac{p_0''}{p_0}+T\frac{(p_0')^2}{p_0^2}\right)y_0
+2a\frac{y_0^3}{p_0^2}
=C\frac{1-3x^2}{(1+x^2)^{5/2}},
$$

其中

$$
C=B+\frac{2a-\delta}{4}.
\tag{17}
$$

任意紧支撑变分迫使 $C=0$。由 (2)、(13)、(17) 解得

$$
\boxed{\delta=\frac{8\alpha+14a}{17},\qquad
B=\frac{2\alpha-5a}{17}.}
\tag{18}
$$

再用 (4)：

$$
\boxed{\alpha\ge\frac52a.}
\tag{19}
$$

整个推导没有除以 a，因此 a=0 的分支也保留。

## 5. 四次主部的完整平方身份

由 (13)、(17)，有 $S=-B-2a$、$T=2B$。直接比较密度得

$$
E[p,y]=\int\left\{a\left(p''-\frac{y^2}{p}\right)^2
+B\left(y'+\frac{p'y}{p}\right)^2\right\}\,ds.
\tag{20}
$$

(20) 是**积分身份**：原 E 密度减去右侧平方密度恰为

$$
-\frac{d}{ds}\left(B\frac{p'y^2}{p}\right).
$$

在平端路径上该边界项为零；在完整周期上两端相同。不能把它当作无边界说明的逐点平方分解。

于是完整 action 为

$$
\begin{aligned}
I[p,y]=\int\bigg\{&a\left(p''-\frac{y^2}{p}\right)^2
+B\left(y'+\frac{p'y}{p}\right)^2\\
&-(\alpha+a)(p')^2+\alpha p^2+(\alpha+a)y^2\bigg\}\,ds.
\end{aligned}
\tag{21}
$$

前两项非负，并不足以使完整 I 非负；下一节保留的低阶项给出严格反例。

## 6. 光滑近复正弦路径排除所有剩余非零参数

选一个频率 $\Omega>0$，令

$$
z(s)=\cos(\Omega s),\qquad
p_\varepsilon(s)=\sqrt{z(s)^2+\varepsilon^2},\qquad
y_\varepsilon(s)=\frac{\varepsilon z'(s)}{p_\varepsilon(s)},
\qquad \varepsilon>0.
\tag{22}
$$

每个固定 $\varepsilon$ 都给光滑正 p，故 h=1/p、k=y/p 为真实有限有界周期函数。两平方中的准确抵消为

$$
p_\varepsilon''-\frac{y_\varepsilon^2}{p_\varepsilon}
=\frac{zz''}{p_\varepsilon},
\qquad
y_\varepsilon'+\frac{p_\varepsilon'y_\varepsilon}{p_\varepsilon}
=\frac{\varepsilon z''}{p_\varepsilon}.
\tag{23}
$$

取完整周期 $T=2\pi/\Omega$。将 (23) 代入 (21)，得到

$$
I_\varepsilon=\int_0^T\left\{
\frac{az^2+B\varepsilon^2}{z^2+\varepsilon^2}(z'')^2
-(\alpha+a)\frac{z^2-\varepsilon^2}{z^2+\varepsilon^2}(z')^2
+\alpha(z^2+\varepsilon^2)\right\}\,ds.
\tag{24}
$$

所有分式因子在 $0<\varepsilon\le1$ 下有一致界；z 的零点只有有限个。由支配收敛，

$$
\lim_{\varepsilon\downarrow0}I_\varepsilon
=\int_0^T\{a(z'')^2-(\alpha+a)(z')^2+\alpha z^2\}\,ds
=\frac\pi\Omega\{a\Omega^4-(\alpha+a)\Omega^2+\alpha\}.
\tag{25}
$$

### 6.1 a>0

取

$$
\Omega^2=\frac{\alpha+a}{2a}.
$$

(25) 中花括号为

$$
-\frac{(\alpha-a)^2}{4a}<0,
$$

严格不等号由 $\alpha\ge5a/2$ 保证。因而存在一个**固定、有限、正的** $\varepsilon$ 使 $I_\varepsilon<0$；无需把退化的 $\varepsilon=0$ 路径当作实际对象。

### 6.2 a=0、alpha>0

此时 (25) 中花括号为 $\alpha(1-\Omega^2)$。取任意 $\Omega>1$，仍得严格负极限，并可固定有限 $\varepsilon>0$ 使一个周期 action 严格负。此分支不使用含 $1/a$ 的公式。

### 6.3 几何 omega 与有限平端实现

这里 $\Omega$ 是选择的时间频率，不是几何状态 $\omega$。实际几何仍必须积分

$$
\omega'=\frac{k'}{2h}.
$$

(22) 满足 $h(s+T/2)=h(s)$、$k(s+T/2)=-k(s)$，因此 $k'/(2h)$ 在半周期平移后变号，准确有

$$
\int_0^T\frac{k'}{2h}\,ds=0.
\tag{26}
$$

等价地直接积分得到 $-\varepsilon/2$ 乘 $\int_0^T z(z')^2/(z^2+\varepsilon^2)^{3/2}$，其两半周相消。故 h、k、$\omega$ 和全部 jets 在每个完整周期后均复位。

先固定上述给负周期的 $\Omega,\varepsilon$。在其两侧各接一段固定光滑连接，使整条路径具有常值 scalar germs；连接保 h>0，并按同一真实方程积分 $\omega$。其完整 action 是一个固定有限数。重复 N 个准确周期后，作用量为

$$
N I_\varepsilon+I_{\rm caps}.
$$

取一个充分大的**有限**整数 N 即严格负。frame 始终由真实 ODE 演化；R140 的开路径不等式本来允许任意末 frame 和任意总矩阵，这里没有偷偷要求每周期 frame 为 I，也没有删除真实矩阵补偿。R140 已把这些端点成本与同一个乘子全部纳入必要条件。

整条所选路径是有限光滑真实路径，h 有正下界，$\omega$ 有界；随后可取共同物理区间使 $\xi+\omega$ 有正间隙。因此负 action 确实违反 (3)，不是只存在于形式变量或无限路径上的反例。

## 7. 唯一剩余字符为零及适用边界

第 6 节排除了 a>0 和 a=0、$\alpha>0$。因此 $\alpha=a=0$。由 (13)、(18) 及最初的 m=0，得到

$$
\alpha=\beta=a=\delta=m=0.
$$

R186 的五参数是真完整字符头部的坐标，所以这等价于 $\lambda=0$，证明 (1)。

本稿没有把真实函数 span 中的负数乘法冒充实际负成本词，也没有构造任意指定第四成本。完整权 −2 的函数核、字符头部和正性问题至此已结束；其他偶权、固定 profile 的代入核、完整第四 period、ruling、更高阶与闭嵌入等仍按各自真实条件继续。
