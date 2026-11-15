# R822 — 原 Cartier 单位的曲线留数下降、分歧 Grothendieck 行与真实补偿列

日期：2026-11-15。**状态：已证明。**

本篇接 R813 的同一个原 $R$。
将其首共振 Cartier 单位精确下降为原曲线 $C$ 上的非零留数，
给出一个全局恰当项，降低所有非固定 $t$ 分歧处的极阶，
并把这些分歧处的完整残数写为原 $(F,F_Y)$ 商上的 Grothendieck 留数。
后者实际读取 $\mathcal E^2R$，不能因为极阶降低便删去。

还给出一个来源范围明确的结论：
对原真实列 $qt^rF\mathcal H_2$，这批残数是显示的有限代数迹；
在未固定 jet 条件时它们确可非零。
保持同一个首修正全部行后，只能使用该真实子格中的联合核。
因此本篇没有把分歧补偿当成免费可调项，也没有把 R813 的非零单位提前变成原 $M$ 的矛盾。

## 1. 原数据和辅助覆盖

保持 R813 的全部假设，尤其
$$
p=6s-1>101,\qquad s=2h+r,\qquad
1\le r<h,\qquad k_{\rm carry}=0,\qquad f_D<p,
$$
$$
P^{\rm fact}=t^r\widetilde F^3\widetilde q\in\mathcal W_D,
\qquad e_0q_0u_0a\ne0,\qquad
J(P^{\rm fact}+pR)\in p^2\Gamma_{2s+\ell}.
\tag{1}
$$
若从原 $M$ 出发，仍须使用 R808 的 primitive 第三精度引理。
本篇不把第一次 $M\in p^2$ 改成相对 $J\in p^2$。

写
$$
\mathcal E=Y\partial_Y,\quad
\delta=t\partial_t,\quad e=\mathcal EF=YF_Y,\quad d=1+8t,
$$
$$
R_E=(\mathcal ER)|_C,\qquad C=(F=0),\qquad P=(0,1).
$$
$\delta$ 总指固定 $Y$ 的底 Euler 导数。沿曲线的真正导子为
$$
\boxed{\delta_C=\delta-\frac{\delta F}{e}\mathcal E.}
\tag{2}
$$
它在分歧处可有极，不能把它当作原整来源自映射。

在 R813 的实际覆盖 $\mathscr C\to C$ 上取
$$
E_0:y^2=x^3+1,\quad t=-x^{-3},\quad
u=-x/y,\quad\omega_0=dx/(2y).
$$
准确恒等式为
$$
\boxed{
\omega_0/u=dt/(6t),\qquad
u^6=-t/(1-t)^3,\qquad
Du=\frac{1+2t}{1-t},\qquad Dt=\frac{6t}{u}.
}
\tag{3}
$$
它们直接由 $y^2=x^3+1$ 微分得到，均是函数域恒等式。

定义
$$
\boxed{
A_F=1-\frac3{17}\left(\frac{\delta F}{e}+\frac{8t}{d}\right),
\qquad
L_F=6(1-t)\delta_CA_F-(1+2t)A_F+1.
}
\tag{4}
$$
R813 的代数函数及误差微分于是写为
$$
\boxed{
\zeta_F=A_F/u,\qquad
\omega_F=d\zeta_F+x\omega_0
       =\frac{L_F}{6t(1-t)u}\,dt.
}
\tag{5}
$$
这是对原 $\zeta_F$ 的准确改写，未替换其全部 $e,d,x$ 极。

## 2. 首共振单位准确下降为 C 上的留数

R813 的实际微分为
$$
\Omega_R=t^rR_E\omega_F.
$$
因为 $p+1=6s$，(3) 给
$$
u^{p+1}=(-t)^s(1-t)^{-3s}.
$$
因此
$$
\boxed{
\Xi_R:=\frac{\Omega_R}{u^p}
=\frac{(-1)^s}{6}\,
t^{-2h-1}(1-t)^{3s-1}\,R_E L_F\,dt
}
\tag{6}
$$
是原 $C$ 的有理微分；右端不含辅助 $x,y,u$。

也可核其群作用：
在含 $\mu_6$ 的常量域上，
$\Omega_R$ 的权为 $-1$，而 $u^p$ 的权为
$p\equiv-1\pmod6$，故比值不变。
覆盖在指定点的分歧指数为六；
这个局部六次扩张已占满覆盖的泛次数，
所以过该点的分量具有实际六次作用。
(6) 的显示有理式又把结果直接下降回原 $k$，
不要求原惰性剩余域本来包含 $\mu_6$。

**定理 1。** 原点 $P$ 处 $\Xi_R$ 的极恰为简单极，且
$$
\boxed{
\operatorname{Res}_P\Xi_R
=\frac{\gamma_R}{6}
=-\frac{5h(6h-1)q_0u_0^4}{34\,a\,e_0}
\ne0.
}
\tag{7}
$$

**证明。** R813 在真实参数 $u$ 中证明
$$
\Omega_R=\gamma_Ru^{p-1}du+O(u^p)du,\qquad
\gamma_R=-\frac{5(6h)(6h-1)q_0u_0^4}{34ae_0}.
$$
除 $u^p$ 后的留数为 $\gamma_R$。
覆盖在该点的分歧指数六为单位，
故拉回留数是原曲线留数的六倍，得 (7)。
极恰为一也可由 (6) 中
$\operatorname{ord}R_E=\operatorname{ord}L_F=h$ 直接看出。
原 $q_0,e_0,a$ 与 $t/w$ 的符号均已保在 R813 的 $\gamma_R$ 中。证毕。

若用原物理 $E_b$ 尺度，(6)–(7) 同乘原固定单位 $b^s$；
这与 R813(21) 完全一致。以下用 (3) 的无量纲角规范。

## 3. 精确全局分部积分与较低分歧极

置
$$
B_F=(-1)^s t^{-s}(1-t)^{3s}A_F
     =\zeta_F/u^p.
$$
由于特征为 $p$，$d(u^{-p})=0$。
把 R813 的全局分部积分直接除以 $u^p$，得到
$$
\boxed{
\Xi_R=d\bigl(t^rR_E B_F\bigr)+\Xi_R',
}
\tag{8}
$$
其中
$$
\boxed{
\Xi_R'
=\frac{(-1)^s}{6}\,
t^{-2h-1}(1-t)^{3s-1}
\left\{R_E-6(1-t)A_F
             (rR_E+\delta_CR_E)\right\}dt.
}
\tag{9}
$$
(8) 是原 $C$ 上的全局有理恒等式。
也可直接微分右端核验：
所用唯一模 $p$ 标号是 $6s=1$，
不能在特征零把它当作相同常数。

所以 (6)、(9) 在每个正规化分支有相同留数，
并有同一个非零 (7)。
(9) 不含 $\delta_CA_F$。
展开 $A_F$ 和 $\delta_CR_E$ 后，分母至多有 $e^2$；
与自然的 $dt/e$ 配合，比直接展开 (6) 的 $e^3$ 更低。
但这不是没有极或没有残数的结论。

### 所有非固定分歧支的精确极阶范围

在原完整边界之外取正规化点 $Q$：
$t(Q)=t_0$ 与 $Y(Q)=Y_0$ 均有限非零，
$t_0\ne1,-1/8$，并避开原六个固定底纤维及全部例外／水平边界。
原 $R_E$ 在这些点为真正正则函数。
取正规化参数 $v$，写
$$
t=t_0+\alpha v^m+\cdots,\qquad \alpha\ne0.
$$
因为 $t:C\to\mathbf P^1$ 的度数为
$b=\deg_YF\le D<p$，有 $1\le m\le b<p$。
故这里的 $t$ 分歧全部 tame，
$$
\operatorname{ord}_v(dt/dv)=m-1.
\tag{10}
$$
这包括原 $C$ 在该点可能奇异的分支；没有把正规化忽略。

沿该支，
$$
A_F=1-\frac{24t}{17d}
       +\frac{3t}{17}\frac{Y'(v)}{Y(v)t'(v)}.
\tag{11}
$$
由 (8) 或 (9)，除正则微分外，准确有
$$
\boxed{
\Xi_R'\equiv
-\frac{3(-1)^s}{17}\,
t^{r+1-s}(1-t)^{3s}
\frac{Y'(v)R_E'(v)}{Y(v)t'(v)}\,dv.
}
\tag{12}
$$
推导时 $d(t^rR_E)$ 中含 $dt$ 的那项与 $t'$ 相消，因而正则；
其余项正是 (12)。

因此每个这样的分支有
$$
\boxed{\operatorname{poleord}_Q\Xi_R'\le m-1.}
\tag{13}
$$
若 $m=1$ 则正则。$m\ge2$ 时，其残数的准确有限读取为
$$
\boxed{
\operatorname{Res}_Q\Xi_R
=-\frac{3(-1)^s}{17}\,
t_0^{r+1-s}(1-t_0)^{3s}
[v^{m-2}]
\left\{
\frac{v^{m-1}}{t'(v)}
\frac{Y'(v)}{Y(v)}R_E'(v)
\right\}.
}
\tag{14}
$$
把仅依赖 $t$ 的权换成 $t_0$ 合法，
因为 $t-t_0$ 从 $v^m$ 才开始，而这里只读 $m-2$。
导数首项若因特征 $p$ 消失，只会提高正则阶；
(14) 使用实际导数，不替它填一个不存在的首项。
特别，(13) 本身绝不推出 (14) 为零。

## 4. 完整分歧残数是原 (F,F_Y) 商上的一条行

在上述非固定开集，$F$ 可取原仿射平面中的正则方程。
因为 $Y$ 为单位，$(F,e)$ 与 $(F,F_Y)$ 是同一个局部有限概形。
定义
$$
W_s(t)=t^{r+1-s}(1-t)^{3s}.
$$
对局部零维完全交概形
$$
Z_Q=(F,F_Y)_Q
$$
采用有序方程 $(F,F_Y)$、坐标 $(t,Y)$ 的 Grothendieck 留数。
其在曲线上的写法是
$$
\operatorname{GRes}_Q(H;F,F_Y)
=\sum_{\widetilde Q\mid Q}
\operatorname{Res}_{\widetilde Q}
\frac{H}{F_tF_Y}\,dY.
\tag{15}
$$
这里用的是原 Gorenstein 曲线的对偶化微分
$dY/F_t=-dt/F_Y$；
奇点处必须取全部正规化分支的和，并先作各分支剩余域至 $k(Q)$ 的迹，
不是把每条分支另当一个独立来源行。
若 $F_t(Q)\ne0$，(15) 只是先沿 $F$ 作一次普通留数，
再沿 $F_Y$ 作第二次；一般情形为同一个对偶化层公式。

由 (11)–(12) 以及在曲线上
$dt=-F_YdY/F_t$，得到所有这些点的准确式
$$
\boxed{
\operatorname{Res}_{Q}\Xi_R
=\frac{3(-1)^s}{17}\,
\operatorname{GRes}_Q
\left(
W_s(t)\frac{F_t^2}{Y^2}\,\mathcal E^2R
\,;\,F,F_Y
\right).
}
\tag{16}
$$
左边在奇点仍表示正规化各支留数的和。
分子在本开集正则；(16) 因而只依赖显示分子在原 $Z_Q$ 中的类。
这给真正有限的分歧行，但它读取的是完整来源的
$\mathcal E^2R|_Z$，不只是 $R|_Z$。

为核符号，从 (12) 改用 $Y$ 微分：
除正则项外，它等于
$$
\frac{3(-1)^s}{17}\,
W_s(t)\frac{F_t}{YF_Y}
\,\partial_Y(\mathcal ER)\,dY.
$$
再用 $\partial_Y(\mathcal ER)=\mathcal E^2R/Y$，
正是 (15)–(16)。
因此 (16) 没有在分歧处把 $e^{-2}$ 当成单位。

## 5. 原 F 倍来源的残数是准确有限代数迹

式 (16) 在真正因子倍来源上可进一步完全读取。
先在该开集写 $R=FH$。有
$$
\mathcal E^2(FH)\equiv(\mathcal E^2F)H
\equiv Y^2F_{YY}H\pmod{(F,F_Y)}.
$$
另一方面
$$
J(F,F_Y)=F_tF_{YY}-F_YF_{tY}.
$$
故 (16) 的分子在原商内等于
$$
W_sF_t\,H\cdot J(F,F_Y).
$$
完全交留数的迹恒等式于是给
$$
\boxed{
\operatorname{Tr}_{k(Q)/k}\operatorname{Res}_Q\Xi_{FH}
=\frac{3(-1)^s}{17}\,
\operatorname{Tr}_{\mathcal O_{Z_Q}/k}
\bigl(W_s F_tH\bigr).
}
\tag{17}
$$
若只在剩余域 $k(Q)$ 上写局部残数，
先取该域上的代数迹，再作 $k(Q)/k$ 的域迹。
这里的迹恒等式可由有序参数 $(F,F_Y)$ 的系数留数核验：
Jacobian 乘子把完全交对偶元转成乘法算子的迹；
它包括非约化局部代数，不仅是约化简单点。

例如，若 $Q$ 是原 $C$ 的光滑 $t$ 分歧点、分歧指数为 $m$，
则 $F_t(Q)\ne0$，$Z_Q$ 的局部长度为 $m-1$。
对局部 Artin 代数，乘任一元素的迹是其剩余值乘长度。
因此
$$
\boxed{
\operatorname{Tr}_{k(Q)/k}\operatorname{Res}_Q\Xi_{FH}
=\frac{3(-1)^s}{17}\,(m-1)
\operatorname{Tr}_{k(Q)/k}
\left[
t_0^{r+1-s}(1-t_0)^{3s}F_t(Q)H(Q)
\right].
}
\tag{18}
$$
在原剩余域上不先作域迹时，方括号内乘子为单位。
$m-1<p$，故局部长度也非零。

若 $Q$ 为该开集中的原曲线奇点，则 $F_t(Q)=0$；
局部乘法算子 $W_sF_tH$ 是幂零的，迹为零。
所以在 $F$ 倍子格上，这类奇点的全部分支残数和确实为零。
这个断言不扩到一般 $R$ 的 (16)，也不将各奇异分支单独删掉。

### 真实来源能改变这些残数，但未付保持所有 jet

回到原十九角曲面，令
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\qquad
Z=(F,e).
$$
R495/R550 的全局原截面 $F,e$ 无公共曲线分量，
$Z$ 长度为 $\kappa=C^2$。
原曲面有 $H^1(\mathcal O_X)=H^2(\mathcal O_X)=0$，
且 $H^1(\mathcal O_X(C))=0$。
对这个同一个完全交的 Koszul 序列扭 $2C$：
$$
0\longrightarrow\mathcal O_X
\longrightarrow\mathcal O_X(C)^{\oplus2}
\longrightarrow\mathcal I_Z(2C)\longrightarrow0,
$$
得到 $H^1(\mathcal I_Z(2C))=0$，从而
$$
\boxed{\mathcal H_2\longrightarrow H^0(Z,\mathcal O_Z(2C))
\quad\text{满射}.}
\tag{19}
$$
这是已有原全截面格的结论，不是环境多项式替换。

原 $qt^r\mathcal H_3$ 已完整返回 $\mathcal W_D$，
因此
$$
\Delta R=qt^rFH,\qquad H\in\mathcal H_2
\tag{20}
$$
是真正同预算来源。
在避开 $q=0$ 的光滑非固定分歧点，
将 (17) 中 $H$ 换成 $qt^rH$ 即得其准确残数变化。
由 (19)，可在整个 $Z$ 上指定这些真实截面的值。
若至少有一个这样的点，则其局部残数行以及相应总迹行
在这个未加 jet 条件的真实子格上不是恒零：
可令其它 $Z$ 分量的值为零，
在该点利用有限可分剩余域的非退化迹选择所需值。

但 (19) **不**允许在已经固定 R808 的所有行之后自由改残数。
保持同一个实际第一修正，(20) 还必须满足
$$
\boxed{
\bar J(qt^rFH)=0
}
\tag{21}
$$
以及原下一位所要求的联合条件。
这正是 R550/R790 的真实 mirror／联合核限制。
其在 $Z$ 上的像不是 (19) 中的整个空间，
不能先用 (19) 选值、再另外填回 normal 或 carry。
本篇没有作出这种交换。

## 6. 非零原点留数必须由哪一批实际项补偿

对一般原 $R$，令 $\mathfrak G_F(R)$ 为 (16)
在所有非固定分歧概形上的完整和，
并将原边界上除 $P$ 外的全部正规化分支留数记为
$\mathfrak B_F(R)$。
后者包含六个固定底纤维、两个水平框、十九个例外、
$q$ 或原框产生的真实极点及所有边界奇点；
不只保某一条方便的轴。

(9) 在这些边界和上述分歧支之外正则。
全局留数定理于是给实际恒等式
$$
\boxed{
\frac{\gamma_R}{6}
+\mathfrak G_F(R)+\mathfrak B_F(R)=0.
}
\tag{22}
$$
每项都来自同一个 $R$；
在原 $k$ 上求和时保全部剩余域迹。
由 (7)，后两项之和必须为一个指定非零单位。

式 (16) 给 $\mathfrak G_F$ 的有限完全交矩阵，
(9) 给 $\mathfrak B_F$ 的完整原边界读取。
其中 $t^{-2h-1}$ 和 $(1-t)^{3s-1}$ 是实际的 $p$ 相关权，
不能因边界点个数固定便把所有主部长度说成 $O(b)$，
也不能把它们当作同预算整乘子。
同理，(19) 只支付原完整 $\mathcal H_2$ 的来源评价，
不支付已经受 (21) 限制的像。

当前还没有证明原全 $M$ 及其同 $R$ 的剩余 normal／两条十三行
会迫 $\mathfrak G_F(R)+\mathfrak B_F(R)=0$。
因此 (22) 尚未与实际提升矛盾。
它把 R813 的辅助覆盖上的 Cartier 单位
变成原曲线上明确的指定残数及全补偿问题；
后续必须判同一个联合核中的真实像，
不能以简单极上界、trace 记号或局部非恰当性替代这个判断。

原 $P_{134}/U_0$、低行右逆高尾、同一个
$P^{\rm fact}+pR$ 及下一位的 $p^2T$ 全部保持。
没有新增中央零、免费加入有理微分来源，
也未声明固定曲线的无穷素数目标完成。

依赖：
[R813](R813-original-corrector-weighted-cartier-unit-at-first-resonance.md)；
[R808](R808-original-third-precision-corrector-split-branches-and-near-normal-jet.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R550](R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)；
[R750 全来源增补](../notes/2026-11-15-r750-whole-divisible-source-and-primitive-carry-filter.md)。
本篇为精确有理恒等式、原来源 Koszul 返回及留数计算，
没有新增程序运行或生成数据。
