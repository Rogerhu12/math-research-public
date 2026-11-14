# R7：保持度量端 jet 的局部变形与全频尾方向排除

日期：2026-11-10。作者：visible-exact-astra-76e8 / a_posteriori_pde。

**状态：已证明。** 在一段负 Sturm 势帽内，构造保持两端背景及其二阶 jet 的正函数变形 $h_t$。对任意预先给定的真实尾输入直线，存在同一个参数，使全部整数频率 $n\ge2$ 的回传直线与规定的正增长方向保持一个明确、与频率无关的正夹角。证明使用精确变分恒等式及可求和的参数坏集；没有未付的 Diophantine 常数。

本结果给的是**尾方向接线模块**。它不构造原先尚未给出的精确平尾，不支付尾的普通源逆，也不同时恢复 $n=3$ 的核。尤其不能用一次非零腰部度量修正后，自动继承 R4 的全部高频算术谱隙。

## 1. 设定和完整陈述

取 $0<\ell\le1/16$，给定正 $C^2$ 函数 $h$ 于 $[0,\ell]$，令
$$
V=-h''/h,\qquad w=h'/h,
$$
假设整个区间上
$$
-3\le V\le-1,\qquad |w|\le2.
\tag{1.1}
$$
这些是本模块的明确输入，不从有限采样推断。

定义 quintic 函数
$$
S(u)=10u^3-15u^4+6u^5\quad(0\le u\le1)
$$
及 $C^2$ bump
$$
\phi(x)=
\begin{cases}
S(4x/\ell),&0\le x\le\ell/4,\\
1,&\ell/4\le x\le3\ell/4,\\
S(4(\ell-x)/\ell),&3\ell/4\le x\le\ell.
\end{cases}
\tag{1.2}
$$
其两端值及前两阶导数均为零；延零仍是 $C^2$。置
$$
\gamma_0=\frac{\ell^2}{512},\qquad
h_t=h\exp(\gamma_0t\phi),\qquad
V_t=-h_t''/h_t,\qquad 0\le t\le1.
\tag{1.3}
$$

对每个整数 $n\ge2$，任取一条**与 $t$ 无关**的实直线
$\Lambda_n\subset\mathbb R^2$ 作为右端数据。解
$$
y''+n^2V_t y=0,
\qquad (y(\ell),y'(\ell)/n)\in\Lambda_n\setminus\{0\},
\tag{1.4}
$$
并将其左端直线记为 $L_n(t)$。再任给目标直线
$$
G_n=\operatorname{span}(1,b_n),\qquad 1\le b_n\le2,
\tag{1.5}
$$
也要求其与 $t$ 无关。

**定理。** 令
$$
\varepsilon_\ell=\frac{\gamma_0\ell}{4096}
=\frac{\ell^3}{2^{21}}>0.
\tag{1.6}
$$
存在测度至少 $1-19/1024$ 的参数集合 $\mathcal G\subset[0,1]$，使对每个 $t\in\mathcal G$、每个整数 $n\ge2$，
$$
\boxed{\quad
\frac{|\det(v_n,g_n)|}{|v_n|\,|g_n|}
\ge\varepsilon_\ell,
\qquad 0\ne v_n\in L_n(t),\quad0\ne g_n\in G_n.
\quad}
\tag{1.7}
$$
同时 $h_t>0$，其两端 $0,1,2$ jet 与 $h$ 完全相同，且
$$
-4<V_t\le-3/4.
\tag{1.8}
$$

特别，取 $\ell=1/16$ 时，$\gamma_0=2^{-17}$、$\varepsilon_\ell=2^{-33}$。这里所有频率同时成立，不是先选一个有限截断再取依赖截断的参数。

## 2. 背景与二阶接合的常数

直接求导给
$$
0\le\phi\le1,\qquad
|\phi'|\le\frac{15}{2\ell},\qquad
|\phi''|\le\frac{96}{\ell^2}.
\tag{2.1}
$$
第一导数用 $S'=30u^2(1-u)^2\le15/8$。第二导数
$S''=60u(1-u)(1-2u)$ 的最大绝对值为 $10/\sqrt3<6$，因此给出所列界。

令 $\gamma=\gamma_0t$、$w_t=h_t'/h_t=w+\gamma\phi'$。精确展开为
$$
V_t=V-\gamma(\phi''+2w\phi')-\gamma^2(\phi')^2.
\tag{2.2}
$$
由 (1.1)、(2.1)，
$$
|\gamma(\phi''+2w\phi')|
\le\frac{96+30\ell}{512}\le\frac{783}{4096}<\frac14,
$$
$$
\gamma^2(\phi')^2
\le\frac{225\ell^2}{4\cdot512^2}<\frac1{1024}.
$$
这证明 (1.8)。正性来自指数因子；$\phi,\phi',\phi''$ 两端为零，故保持 $h$ 的完整二阶 jet，特别保持 $V$ 的端点值。

通过已证明的几何换算
$$
a=1/h,\qquad \frac{ds}{dx}=\frac{\sqrt{1+h'^2}}{h^2},
\qquad \frac{dz}{dx}=\frac1{h^2},
\tag{2.3}
$$
该变形确实对应另一个旋转度量，并保持与两侧原背景的径向二阶接合。积分后的外侧位置差可用刚体平移吸收；不改变两端的半径和切向方向。这里没有使用 Dirac 势或不连续曲率的薄层近似。

## 3. 保持 $h$ 端数据的精确变分恒等式

先把参数写作 $\gamma$。在给定 $\gamma$ 处，取任一真实解
$y''+n^2V_\gamma y=0$。因为
$$
\partial_\gamma V_\gamma=-\phi''-2w_\gamma\phi',
\qquad w_\gamma'=-V_\gamma-w_\gamma^2,
$$
两次分部积分得到
$$
\boxed{\quad
\int_0^\ell(\partial_\gamma V_\gamma)y^2\,dx
=-2\int_0^\ell\phi\left[(y'-w_\gamma y)^2
 -(n^2-1)V_\gamma y^2\right]dx.
\quad}
\tag{3.1}
$$
详细地，边界项因 $\phi=\phi'=0$ 全部消失；被积式先化为
$$
-2\phi\{y'^2+yy''-w_\gamma'y^2-2w_\gamma yy'\}.
$$
用 $y''=-n^2V_\gamma y$ 和 $w_\gamma'=-V_\gamma-w_\gamma^2$ 后即是 (3.1)。

因为 $n\ge2$、$V_\gamma\le-3/4$、$\phi=1$ 于正长区间，(3.1) 对任一非零解严格为负。
这项同号性不要求 $\partial_\gamma V_\gamma$ 点态同号；它恰好利用了保持几何端 jet 的特殊变形。

## 4. Prüfer 角的全局单调性及坏方向附近的下界

为每个 $n$ 在右端选一个固定非零向量，得到随 $t$ 光滑依赖的实解。写
$$
Y=(y,y'/n),\qquad \theta_n(t,x)=\arg Y(t,x),
$$
在右端取固定实提升 $\theta_n(t,\ell)$，沿 $x$ 连续延拓。ODE 解不可能同时有 $y=y'=0$，故角有定义。

对参数微分，令 $W=y\partial_\gamma y'-y'\partial_\gamma y$。由右端向量固定，$W(\ell)=0$，而
$$
W'=-n^2(\partial_\gamma V_\gamma)y^2.
$$
因此左端角满足
$$
\partial_\gamma\theta_n(\gamma,0)
=\frac{n\int_0^\ell(\partial_\gamma V_\gamma)y^2dx}
 {y(0)^2+(y'(0)/n)^2}<0.
\tag{4.1}
$$
这是真正的全参数单调性；没有从数值斜率推断。

下面只在距目标 $G_n$ 很近的参数上需要定量下界。若两直线的夹角正弦小于某个 $0<\varepsilon\le1/20$，把 $Y(0)$ 归一化并选择符号，使它与
$(1,b_n)/\sqrt{1+b_n^2}$ 的内积为正，则两单位向量的距离小于 $2\varepsilon\le1/10$。由于
$$
\frac1{\sqrt{1+b_n^2}}\ge\frac1{\sqrt5}>\frac49,
\qquad
\frac{b_n}{\sqrt{1+b_n^2}}\ge\frac1{\sqrt2}>\frac7{10},
$$
可得
$$
y(0)>1/3,\qquad y'(0)/n>0.
\tag{4.2}
$$
由 $y''=-n^2V_t y$、$-V_t\ge3/4$，从 (4.2) 出发，$y,y'$ 在整个层上保持正，且 $y(x)\ge y(0)>1/3$。因而
$$
\int_0^\ell\phi y^2dx\ge\ell/18.
$$
将它与 (3.1)、(4.1) 合用，得到在所有上述坏方向参数处
$$
\boxed{\quad
|\partial_t\theta_n(t,0)|
\ge\gamma_0\frac{n(n^2-1)\ell}{12}
\ge\frac{\gamma_0n^3\ell}{16}.
\quad}
\tag{4.3}
$$
最后一步用 $n^2-1\ge3n^2/4$。这里没有固定的指数角带费用：只在需要排除的正增长方向附近，解的正性给出多项式横截性。

另外，由系统 $Y'=n\left(\begin{smallmatrix}0&1\\-V_t&0\end{smallmatrix}\right)Y$，直接有
$$
|\partial_x\theta_n|=
n\frac{|V_t y^2+(y'/n)^2|}{|Y|^2}\le4n.
\tag{4.4}
$$
右端提升固定，所以当 $t$ 遍历 $[0,1]$，左端角的整个值域长度不超过 $8n\ell$。

## 5. 对全部整数频率同时排除

令 $\beta_n=\arctan b_n$，定义开坏集
$$
\mathcal B_n=\{t\in[0,1]:|\sin(\theta_n(t,0)-\beta_n)|<\varepsilon\}.
$$
在实角轴上，坏集由以 $\beta_n+k\pi$ 为中心、宽度
$2\arcsin\varepsilon\le4\varepsilon$ 的区间组成。
因为 $\theta_n(t,0)$ 严格单调、值域长不超过 $8n\ell$，实际遇到的坏区间数至多
$$
\frac{8n\ell}{\pi}+2\le3n\ell+2.
$$
在每个这样的区间中用 (4.3) 换元，得到
$$
|\mathcal B_n|
\le\frac{64\varepsilon}{\gamma_0\ell}
\left(\frac{3\ell}{n^2}+\frac2{n^3}\right).
\tag{5.1}
$$
由 $\sum_{n\ge2}n^{-2}\le1$、$\sum_{n\ge2}n^{-3}\le1/2$，
$$
\left|\bigcup_{n\ge2}\mathcal B_n\right|
\le\frac{64\varepsilon}{\gamma_0\ell}(3\ell+1)
\le\frac{76\varepsilon}{\gamma_0\ell}.
\tag{5.2}
$$
取 (1.6) 的 $\varepsilon=\gamma_0\ell/4096$，右边为 $19/1024$。这个 $\varepsilon$ 远小于 $1/20$，故所有前置界同时有效。
令 $\mathcal G=[0,1]\setminus\bigcup_{n\ge2}\mathcal B_n$，即证明全部整数频率同时满足 (1.7)。这是一个正测度、明确常数的存在性结论，不要求先算出每条尾直线的斜率。

相同参数若控制 $q$ 个互不相交的层，且每层分别满足上述输入并有自己的固定输入/目标直线，则把坏集再作有限并，补集测度至少 $1-19q/1024$。特别两端帽可用同一个参数，仍有正测度可选集。此句不额外声称一个核保持条件也成立。

## 6. 对 R4 势的帽部适用性

取 R4 的
$$
\kappa=\sqrt2,\qquad A=2+\frac{\sqrt2}{3},\qquad
V(x)=A\operatorname{sech}^2x-2.
\tag{6.1}
$$
若 $x\ge2$，由 $e^2>7$、$\cosh2>7/2$、$A<5/2$，
$$
-2\le V(x)<-2+\frac{10}{49}=-\frac{88}{49}< -1.
\tag{6.2}
$$
R4 的正全局解 $h$ 满足 $h''=-Vh\le2h$。对任何在整条实线上为正的 $C^2$ 函数满足 $h''\le\kappa^2h$，有
$$
|h'/h|\le\kappa.
\tag{6.3}
$$
一个直接证明如下：若在 $x_0$ 有 $h'(x_0)<-\kappa h(x_0)$，令 $u$ 解 $u''=\kappa^2u$ 并取相同初值，则 $u$ 在有限正时间首次为零。只要 $h$ 为正，变常数公式与 $h''-\kappa^2h\le0$ 给 $h(x_0+t)\le u(x_0+t)$，在该零点矛盾。另一符号由反向时间相同证明。

所以任意放在 $[T,T+\ell]$、$T\ge2$ 内的层都满足 (1.1)。这种变形由正 $h_t$ 定义，并保持层外的核心、帽和任何已给定尾的背景完全相同，几何端 jet 自动匹配。

## 7. 长帽压低反射误差的有效推论

这一节假设在右层远端已给定一条实际尾允许线 $\Lambda_n$；定理并不为它补造精确平尾。

在未改的 P–T 帽 $[2,T]$ 上，(6.2) 还给
$$
\left(\frac43\right)^2 n^2<-n^2V(x)\le2n^2.
\tag{7.1}
$$
取实际正增长解 $g_n$ 满足 $g_n(2)=1$、$g_n'(2)=\kappa n$。Riccati 比较给
$$
\frac43\le\frac{g_n'}{ng_n}\le\kappa,
\qquad g_n(x)\ge e^{(4/3)n(x-2)}.
\tag{7.2}
$$
因此层左端的增长方向 $G_n=\operatorname{span}(g_n(T),g_n'(T)/n)$ 恰满足 (1.5)。

令 $f_n$ 为 P–T 帽上向 $+\infty$ 衰减的解，并归一化 $f_n(2)=1$。它存在且为正；可在有限远端取正衰减 Robin 线后以 ODE 比较取极限。等价地，可用 $V+2$ 可积的标准 Volterra 积分直接构造。比较还给
$$
\frac43\le-\frac{f_n'}{nf_n}\le\kappa,
\qquad0<f_n(x)\le e^{-(4/3)n(x-2)}.
\tag{7.3}
$$
为说明比较的边界量词：在任一有限 $R>T$ 取 $f_R(R)=1$、$f_R'(R)=-\kappa n$。其反向 Riccati $-f_R'/(nf_R)$ 保持于 $[4/3,\kappa]$；归一化 $f_R(2)=1$ 后在每个紧区间一致有界，导数也由方程一致有界，子列极限给 (7.3)，并因指数衰减而选定唯一衰减方向。

取本定理的一个好参数。实际允许解在 $[2,T]$ 上写成
$$
y_n=c_nf_n+d_ng_n.
$$
由 (1.7)，$c_n\ne0$。用二阶行列式求系数，并用 (7.2)–(7.3)，得到
$$
\boxed{\quad
\left|\frac{d_n}{c_n}\right|
\le\frac2{\varepsilon_\ell}
\exp\left[-\frac83n(T-2)\right].
\quad}
\tag{7.4}
$$
证明中，衰减解的缩放状态 $(f_n,f_n'/n)$ 的范数至多
$\sqrt3 e^{-(4/3)n(T-2)}<2e^{-(4/3)n(T-2)}$，增长解状态范数至少
$e^{(4/3)n(T-2)}$；夹角下界正好给分母 $\varepsilon_\ell$，没有再假设尾 Robin 属于某个未证的符号锥。

若 (7.4) 的右边不超过 $1/2$，则在固定切口 $x=2$ 的实际 logarithmic derivative 与原衰减方向的差满足
$$
\boxed{\quad
\left|\frac{y_n'(2)}{y_n(2)}-\frac{f_n'(2)}{f_n(2)}\right|
\le\frac{12n}{\varepsilon_\ell}
\exp\left[-\frac83n(T-2)\right].
\quad}
\tag{7.5}
$$
确切计算是令 $r=d_n/c_n$、$u=-f_n'(2)/n\in[4/3,\kappa]$，则归一化斜率差为
$n(\kappa+u)r/(1+r)$；其绝对值至多 $4\kappa n|r|<6n|r|$。

左帽在反向坐标中同样成立。式 (7.4)–(7.5) 是对全部整数模的实际指数衰减控制，足以作为后续核心 Schur / Green 计算的输入；尚不能单独替代那项计算，更不能替代完整尾的普通源估计。

## 8. 与低模恢复及本题完成标准的边界

这里使全部尾方向避开帽的正增长方向，保持了核心背景；没有要求某个非零角模的全局边值算子仍恰有核。若另在腰部作固定非零 profile 修正恢复 $n=3$，高频核心相位一般会变动 $O(n\,\delta\mathrm{profile})$；无论该常数多小，不能直接把原 R4 的 $n^{-2}$ 谱隙转授给所有 $n$。

下一步必须把低模兼容与高频方向排除联立。例如，可把补偿参数也放在远帽另一段，先实际建立 $n=3$ 兼容曲线的起点和横截性，再沿该曲线重做 (4.3)–(5.2)。本稿没有假设这样的起点存在，没有假设曲线上高频导数仍同号。

同样，R520 型尾的“稳定线”必须先换成这里的真实 $(y,y'/n)$ 单位；某个其它归一坐标中的负斜率不能代付 (1.7)。本定理允许任意固定实输入直线，正是为了避免这一混用。

完整非线性精确等距族、握持开集、$5\%$ 比例及全程 reach 均仍未由本结果证明。

