# R640 — 原 Wilson 来源经固定 conductor 返回同一 canonical 格

日期：2026-11-15。**状态：已证明。**

R609 的三个完整 degree-$12$ 来源，乘 $x^2W_{13}$ 后落在
R473/R486 的同一个 $\mathcal B_{19}$。
本篇进一步支付回到原 $G_0\mathcal W_D$ 的全部十九角与次数帽：
不是仅由 Gaussian 权相同认作原列。

具体地，原固定 conductor $\mathfrak c=\Theta^{10980}q_{\mathfrak c}(t)$
满足新的整多项式界
$$
a^{305}d^{229}\mid q_{\mathfrak c},\qquad
\deg q_{\mathfrak c}\le3433.
$$
因此
$$
S^{189}\mathfrak c\,\mathcal B_{19}\subset\mathcal V_{836},
$$
而乘回整个原 $G_0$ 后正是原 canonical 来源。
全部乘子及其固定成本在正文明确保留。

这条包含不增加任何中央零，也不把原 Wilson 单位行自动变成旧
$M$ 的可提升左行或同一个 $R$ 的 forcing。

## 1. 同一个三来源整模型

沿 R473 的共同 $b=1$ 框，固定
$$
R=\mathbf Z[1/(2\cdot3\cdot7\cdot13\cdot17)],
\quad
t=-x^{-3},\quad\Theta=x\sigma^2,
$$
$$
h_7=7+4t+16t^2,\qquad
a=t(t-1)h_7,\qquad d=1+8t,\qquad f=ad/7.
$$
三个实际来源仍是
$$
S=\Theta^{17}f,\qquad
T=\Theta^{36}fV,\qquad
U=\Theta^{68}f_U,\qquad f_U=aH/91.
\tag{1}
$$
$V,H$ 是 R473 的原固定多项式，
$$
\deg V=6,\qquad \deg H=18,\qquad
\deg f=5,\qquad\deg(fV)=11,\qquad\deg f_U=22.
$$
R473 的整结式证书保证 $ad$ 平方自由，
且 $ad$ 与 $H,V$ 互素；所有所列首项在 $R$ 中为单位。
这里的 $U$ 是第三个实际 degree-$136$ 来源。

仍取同一个 monic 最小式
$$
\Phi(S,U;Z)\in R[S,U][Z],\qquad
\deg_Z\Phi=306,\qquad\Phi(S,U;T)=0
$$
和实际 conductor
$$
\boxed{\mathfrak c=\Phi_Z(S,U;T)
=\Theta^{10980}q_{\mathfrak c}(t),\qquad q_{\mathfrak c}\in R[t].}
\tag{2}
$$
它的定义没有更换。
R473 已证明 $\mathfrak c\mathcal B_m\subset R[S,T,U]$，
但这本身没有证明它落在旧 $G_0\mathcal W_D$ 的指定角格中。

## 2. conductor 的全部实际零端与无穷端

以下先在特征零代数闭域上计算；所得多项式整除随后回到 $R[t]$。

在真实曲线 $U=1$ 的正规化上，
$$
\Theta^{68}aH/91=1.
\tag{3}
$$
它是不可约 Kummer 曲线：
在 $a$ 的一个简单零点，右端的赋值为 $-1$，
所以其六十八次根扩张不可约。
$S$ 的全部零点及原局部阶数如下。

| 位置 | 正规化上的点数 | $\operatorname{ord}t_{\rm loc}$ | $\operatorname{ord}\Theta$ | $\operatorname{ord}S$ | $\operatorname{ord}T$ |
|---|---:|---:|---:|---:|---:|
| $a=0$ 的四个简单根 | 每根一处，共四处 | $68$ | $-1$ | $51$ | $32$ |
| $d=0$ | $68$ | $1$ | $0$ | $1$ | $1$ |
| $\infty$ | $2$ | $\operatorname{ord}(1/t)=34$ | $11$ | $17$ | $22$ |

表 1：同一 $U=1$ 正规化上的全部 $S$ 零端。

在第一行，(3) 给 $\Theta$ 的一阶极，
于是 $S$ 的阶为 $68-17=51$，$T$ 为 $68-36=32$。
第二行因 $aH$ 在 $d=0$ 是单位，得到六十八个非分歧点。
第三行来自 $\gcd(68,22)=2$，且
$$
17\cdot11-5\cdot34=17,\qquad
36\cdot11-11\cdot34=22.
$$
$H$ 的其它根只使 $\Theta$ 有极，
那里 $f$ 非零，所以是 $S$ 的极点而非零点。
这证明表中没有遗漏其它 $S=0$ 分支。

因此
$$
\deg(S)=4\cdot51+68+2\cdot17=306.
\tag{5}
$$
而 R473 的实际有理反函数
$t\in k(S^{36}/T^{17},U/S^4)$ 及
$\Theta=S^{17}V^8/(T^8f^9)$，在 (3) 上仍给
$$
k(S,T)=k(t,\Theta).
$$
故 $\Phi(S,1;Z)$ 仍是次数 $306$ 的 monic 最小式。
于是对 (3) 上任何一个分支，(2) 可准确按其余全部 $305$ 个共轭计算：
$$
\boxed{\mathfrak c=\prod_{T'\ne T}(T-T').}
\tag{6}
$$
这里按可分函数域的全部嵌入计数，允许多个共轭在同一几何点附近。
不需要假设不同分支的首项均不相消；相消只会加强以下下界。

### 2.1 四个 a 零点

在表1的一个 $a$ 点，以其局部赋值归一。
$S$ 的阶是 $51$，自己的 $T$ 的阶是 $32$。
其余来自四个 $a$ 点的共轭 $T'$，阶同为 $32$；
来自 $d$ 点的共轭阶为 $51$；
来自无穷点的共轭阶为 $66$。
所以每个差 $T-T'$ 的阶至少为 $32$，从而
$$
\operatorname{ord}\mathfrak c\ge305\cdot32=9760.
$$
若 $v_a(q_{\mathfrak c})$ 为底线上该根的重数，
由 $\operatorname{ord}\Theta=-1$、$\operatorname{ord}(t-t_a)=68$，
$$
68v_a(q_{\mathfrak c})-10980\ge9760.
$$
故四根都满足
$$
\boxed{v_a(q_{\mathfrak c})\ge305.}
\tag{7}
$$

### 2.2 d 零点

在一个 $d$ 点，$S,T$ 都为一阶。
其余 $67$ 个 $d$ 分支，每个差至少为一阶。
来自 $a$ 点的 $204$ 个共轭，按 $S$ 归一的阶是 $32/51<1$，
因此与本支 $T$ 的差准确有该阶。
来自无穷点的 $34$ 个共轭，其阶为 $22/17>1$，
与本支的差准确为一阶。
所以
$$
\operatorname{ord}\mathfrak c
\ge67+204\frac{32}{51}+34=229.
$$
这里 $\Theta$ 是单位，遂有
$$
\boxed{v_d(q_{\mathfrak c})\ge229.}
\tag{8}
$$

### 2.3 无穷处

在一个无穷点，$\operatorname{ord}S=17$、
$\operatorname{ord}T=22$。
$204$ 个 $a$ 共轭相应有阶 $32/3<22$，
$68$ 个 $d$ 共轭有阶 $17<22$，
其余 $33$ 个无穷共轭与本支之差至少为阶 $22$。
于是
$$
\operatorname{ord}_\infty\mathfrak c
\ge204\frac{32}{3}+68\cdot17+33\cdot22=4058.
$$
若 $\deg q_{\mathfrak c}=d_{\mathfrak c}$，
(2)、表1 给
$$
10980\cdot11-34d_{\mathfrak c}\ge4058,
$$
故
$$
\boxed{\deg q_{\mathfrak c}\le3433.}
\tag{9}
$$

结合 (7)–(9)，得到完整整多项式结论。

**定理1。**
$$
\boxed{
q_{\mathfrak c}=a^{305}d^{229}\widetilde q_{\mathfrak c},
\qquad
\widetilde q_{\mathfrak c}\in R[t],\qquad
\deg\widetilde q_{\mathfrak c}\le1984.}
\tag{10}
$$

**整性说明。**
以上先证明特征零中的整除。
$a,d$ 的首项在 $R$ 中都是单位，且互素；
对 $R[t]$ 的普通多项式除法即可把商降回 $R[t]$，
不会引入新分母素数。
次数为
$3433-4\cdot305-229=1984$。
因此 (10) 在每个允许的好特征约化后仍是准确多项式恒等。
本篇只需要这些下界，不称 (7)–(9) 均为锐等号。

## 3. 原 Wilson 三来源准确进入 B19

在 R609 的原 $E_b$ 上，
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6,
$$
$$
\mathcal H_4(f)=fD^4f-4(Df)(D^3f)+3(D^2f)^2,\qquad
\mathcal W(f_4,f_1)=f_4Df_1-(Df_4)f_1.
$$
其完整全函数身份已付：
$$
\mathcal H_4(f_4)=72x(x^3+2b)\sigma^{12},
$$
$$
\mathcal H_4(f_1)=-432b^2x\sigma^{12},\qquad
\mathcal W(f_4,f_1)=-3x^4\sigma^{12}.
\tag{11}
$$
转入 R473 的共同角变量 $t=-b/x_b^3$；
$\Theta=x_b\sigma_b^2$ 在这个同构下不变。
乘 $x_b^2$ 后准确成为
$$
\boxed{
\begin{aligned}
x_b^2\mathcal H_4(f_4)&=72\Theta^6(1-2t),\\
x_b^2\mathcal W(f_4,f_1)&=-3\Theta^6,\\
x_b^2\mathcal H_4(f_1)&=432b\,\Theta^6t.
\end{aligned}}
\tag{12}
$$
这里的 $b$ 为已付原 $b=17$ 或共同 $b=1$，
在系数环中均为单位。
(12) 由 (11) 完整相乘得到，不只是低 Taylor 项。
它也表明乘 $x_b^2$ 后的来源全纯：
可能的 $x_b^2$ 极在全式中已经被原 sigma 零支付。

取 R486 的实际
$$
W_{13}=\Theta^{13}a.
$$
由 (12)，三条完整来源都落在
$$
\boxed{
x_b^2W_{13}
\langle\mathcal H_4(f_4),\mathcal W(f_4,f_1),\mathcal H_4(f_1)\rangle_R
\subset
\mathcal B_{19}
=\Theta^{19}a\,R[t]_{\le2}.}
\tag{13}
$$
实际上它们使用 $\{1,t\}$ 两个基方向。
这是固定来源包含，未涉及任何中央导数的传播。

## 4. 返回原 V836 的完整多项式

原相对径向变量与 canonical 格仍是
$$
\mathscr R=\Theta^{17}d,\qquad
\mathcal V_n=\mathscr R^nq_n(t)R[t]_{\le e_{n+1}},
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
e_{n+1}=\lfloor9n/2\rfloor+4-3A_n-B_n+C_n.
\tag{14}
$$
这里的 $q_n$ 不与 conductor 的 $q_{\mathfrak c}$ 混同。
仍有 $S=\mathscr R a/7$。

对 $\mathcal B_{19}$ 的每个标准列
$B_{19,j}=\Theta^{19}at^j$，$j=0,1,2$，
直接计算
$$
S^{189}\mathfrak c\,B_{19,j}
=
7^{-189}\Theta^{14212}
q_{\mathfrak c}a^{190}d^{189}t^j,
\qquad 14212=17\cdot836.
\tag{15}
$$
而
$$
A_{836}=209,\quad B_{836}=279,\quad C_{836}=418,
$$
$$
f_{836}=3766,\qquad e_{837}=3278.
\tag{16}
$$
所以 (15) 除以同一 $\mathscr R^{836}q_{836}$ 的商准确为
$$
\boxed{
F_j(t)=
\frac{7^{-189}q_{\mathfrak c}a^{190}t^j}
{d^{229}(th_7)^{209}(t-1)^{279}}
=
7^{-189}(th_7)^{286}(t-1)^{216}
\widetilde q_{\mathfrak c}(t)t^j.}
\tag{17}
$$
(10) 支付了第一个表达式的全部分母，
第二个表达式是同一 $R[t]$ 中的真正多项式。

最后
$$
\deg F_j\le
3\cdot286+216+1984+j
=3058+j\le3060<3278=e_{837}.
\tag{18}
$$
(17) 同时保 $t=0$、$h_7=0$、$t=1$、$d=0$ 的角重数；
(18) 支付无穷处帽。
它们正是原 canonical 格的全部显示条件，
所以全部十九角经过原模型保持，而非仅在 $t=0$ 作局部比较。

**定理2（实际固定返回）。**
$$
\boxed{
S^{189}\mathfrak c\,\mathcal B_{19}
\subset\mathcal V_{836}\subset\mathcal W_{836}.}
\tag{19}
$$
更完整地，三条 R609 来源满足
$$
\boxed{
G_0S^{189}\mathfrak c\,x_b^2W_{13}
\langle\mathcal H_4(f_4),\mathcal W(f_4,f_1),\mathcal H_4(f_1)\rangle_R
\subset G_0\mathcal W_{836}.}
\tag{20}
$$
$G_0$ 是整个原固定因子；
它包括原 $P_{134}$、$w^{13}$、$U_0$ 及 Gaussian charge 四十。
(20) 没有用 $G_0$ 的局部常数替代它，也没有在目标中作非整逆。

## 5. 实际成本、目标与不能转移的单位行

返回中所有乘子都固定，且实际用了 $S^{189}$。
这不等于只付一次 conductor 后便免费进入旧格。

各阶段的 $\Theta$ 权依次为
$$
6\ \xrightarrow{\ W_{13}\ }\ 19\
\xrightarrow{\ \mathfrak c\ }\ 10999\
\xrightarrow{\ S^{189}\ }\ 14212\
\xrightarrow{\ G_0\ }\ 14892.
\tag{21}
$$
最后的相对 canonical 指数是 $836$，
原公共四十仍在，所以总 Gaussian charge 为 $876$；
总 sigma degree 是 $2\cdot14892=29784$。
在原要求 $f_D<p$ 的局部连接窗中，
直接使用 (20) 须保 $D\ge836$ 及 $p>3766$，
或对实际所选更大 $D$ 检查原 $f_D<p$。
不把这个固定数误写成零成本。

因 $\mathfrak c\mathcal B_{19}\subset\mathcal A_{10999}$，
(19) 也属于原三生成元齐次权 $14212$，
可由总次数不超过 $836$ 的实际 $S,T,U$ 多项式表示。
分母仍只来自固定环 $R$，没有随 $p$ 或预算增加的新坏素数。
这给真实固定返回，未声称该返回后的物理像饱和。

原 Wilson 行在相乘后会经历整个乘子的 Taylor 卷积、
原 Gaussian 变化及原目标 carry。
故不能保留相乘前的系数下标或单位值不变，
也不能由 (20) 认它杀掉旧 $M$ 的整个像。
尤其不能把 $\mathcal C_p$ 的某条高行搬入
R597 的旧截止内。

原三条算术中央零只属于已识别来源；
本篇没有给 $S^{189}\mathfrak c$、$W_{13}$、
返回列或其乘积赋中央零。
同一个 $R$ 的两条十三行和完整第二 forcing 继续按原定义处理。

## 依赖

- [R473](R473-three-source-function-field-normalization-and-integral-conductor.md)：
  同一 $\Phi$、三个真实来源、全部结式、规范化与 conductor。
- [R486](R486-graded-integral-connection-and-actual-homogeneous-third-kernels.md)：
  $\mathcal B_{19}$ 与真实 $W_{13}$，齐次物理运输的范围。
- [R609](R609-original-wilson-pairing-and-quadratic-defect.md)：
  三个全函数身份 (11) 与原 Wilson 行；本篇未重做其有限证书。
- [R352](R352-whole-canonical-degree-two-derivation-and-original-moving-poles.md)：
  原 $\mathcal V_n$、$G_0$ 与全部相对次数帽。
- [R620](R620-full-original-weighted-hilbert-function-and-thirteen-row-smith-window.md)：
  同一 canonical 基及完整大目标的来源范围。

本篇为固定代数返回的全证明，不增加素数扫描。
