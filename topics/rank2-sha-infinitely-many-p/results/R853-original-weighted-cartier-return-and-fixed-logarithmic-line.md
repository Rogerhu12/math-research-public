# R853 — 原四首行的加权 Cartier 返回与固定对数直线

日期：2026-11-16。**状态：以下同一原输入的全极控制、三次 Cartier 的固定返回、精确 exact 分解与第四次的原首行读取已证明。没有证明四条原首行不能同时为零，主目标未完成。**

本篇继续[固定 torsion 原注](../notes/2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md)的四个真实输入。
该注 §19 的无权输入经过三次 Cartier 后会失去所需的原点首行。
这里保留同一个原 $\mathcal P_2$ 与四个 $R_\nu$，改为一个明确的、随 $p$ 变化的乘数 $Z^{-p}$；
它把该首行变为留数，因而在后续每次 Cartier 中都被完整保存。
这不是将一个输入乘数从 Cartier 中错误地提出来，也不声称得到原完整中央的非零。

## 1. 同一原模型、输入和有限窗口

在 R821 的共同模型上取
$$
E_0:y^2=x^3+1,\qquad
\omega=\frac{dx}{2y}=dz,\qquad
D=\frac{d}{dz},\qquad p=6s-1>211.
\tag{1}
$$
在一个完美好剩余域 $k$ 中工作；可作固定常数扩张以包含 $\mu_6$。
保原全部固定坏集和系数分母。
以下使用 R636/R647 的原 $M=1$ 模型，而不是重新选择一个水平项：
$$
Z=\mathscr R_p(x)/y^p,\quad DZ=1,\quad
G=\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^i(-x)}{(i+1)!},
$$
$$
r=\frac{x^2}{y},\qquad H=G+r,\qquad
\nabla_2=D-2G,
$$
$$
\mathcal P_2=-\nabla_2^{p-1}(Z^{p+1})
=\sum_{j=0}^{p-1}\frac{(-Z)^j}{j!}\nabla_2^j(Z^2),
\qquad
\nabla_2\mathcal P_2=2H^pZ^{p+1}.
\tag{2}
$$
原 $Z=z+O(z^{5p})$，且 $\mathcal P_2=z^2+\cdots$。
四个来源完整保持为
$$
A_\nu=\sigma^{2n_\nu}R_\nu(x,y)
=\Theta^{n_\nu}f_\nu(t),\qquad
t=-x^{-3},\quad\Theta=x\sigma^2,
$$
$$
(n_S,n_T,n_U,n_V)=(17,36,68,33).
\tag{3}
$$
这里 $f_\nu$ 和 $R_\nu=x^{n_\nu}f_\nu(t)$ 都是 R821 的完整原多项式；
每个 $R_\nu$ 只在 $O$ 有极，极阶 $2n_\nu-6$，每个原来源从 $z^6$ 起始。
不得把它们换成四个自由测试。

记
$$
\widehat A_\nu=\mathcal P_2^{n_\nu}R_\nu,\qquad
f_\nu^{\rm rat}=Z^{-2}\widehat A_\nu,\qquad
\alpha_\nu=[z^{p+1}]\widehat A_\nu\in k.
\tag{4}
$$
原有限整窗口已经证明，(4)正是指定原首行的约化；
Gaussian 的首次修正不进入这一系数。
本篇不把这个模 $p$ 首行与整个 $J_\nu'(0)$ 的零等价。

使用 $M=1$ 只为了使固定极集合缩回三个非零二挠点。
(2)–(4)仍是同一个原首行的合法模型。
此处不使用大 $M$ 才有的有限 theta 平移或 CM13 交织，
也不把它们的 frame 公式移到 $M=1$ 后删掉。

定义实际加权微分
$$
\boxed{\eta_{\nu,p}
=Z^{-p-2}\mathcal P_2^{n_\nu}R_\nu\,\omega
=Z^{-p}f_\nu^{\rm rat}\omega.}
\tag{5}
$$
乘数 $Z^{-p}$ 是本篇明示的一次原输入变化，其全部极成本在下一节支付。

## 2. 全部极点：没有遗漏 $Z$ 的其它零点

令 $\mathcal D_2$ 为三个非零二挠点之和。
固定 torsion 原注 §13 在 $M=1$ 时已给
$$
-\operatorname{ord}_Q Z=p,\qquad
-\operatorname{ord}_QG=p^2-p-1,\qquad
-\operatorname{ord}_Q\mathcal P_2=p^3-p^2+p+1
\quad(Q\in\mathcal D_2).
\tag{6}
$$
$G$ 在 $\mathcal D_2$ 以外仅在 $O$ 有一个简单极，
$\mathcal P_2$ 在 $O$ 正则且阶二。

先检查所有其它 $Z$ 零点。
若 $Q\ne O$ 且 $Z(Q)=0$，则 $Q\notin\mathcal D_2$，$G,H$ 在 $Q$ 正则。
$DZ=1$ 使 $u=Z$ 成为该点的微分参数。
(2) 的有限和逐项在 $Q$ 正则，且每项在 $Z=0$ 都为零，故
$\mathcal P_2(Q)=0$。
在参数 $u$ 中，
$$
(D-2G)\mathcal P_2=2H^p u^{p+1}.
$$
从零常数项依次比较到 $u^{p-2}$，所有 $1,\ldots,p-1$ 为单位，
所以
$$
\operatorname{ord}_Q\mathcal P_2\ge p.
\tag{7}
$$
这是指定(2)的初始资料，不是任意解所共享的自由归一。
因 $R_\nu$ 在 $Q$ 正则，(5)给
$$
\operatorname{ord}_Q\eta_{\nu,p}\ge(n_\nu-1)p-2\ge0.
\tag{8}
$$
因此 $Z^{-p-2}$ 没有引入新的未记极点。

在 $O$，(3)–(4)使 $\widehat A_\nu$ 阶六，故
$$
\operatorname{ord}_O\eta_{\nu,p}=4-p,\qquad
\boxed{\operatorname{Res}_O\eta_{\nu,p}=\alpha_\nu.}
\tag{9}
$$
留数等式使用完整的 $Z$：
$Z/z=1+O(z^{5p-1})$ 的修正乘上 $z^{4-p}$ 后不可能贡献 $z^{-1}$；
并非在全函数域中把 $Z$ 换成 $z$。

在每个 $Q\in\mathcal D_2$，$R_\nu$ 正则，故极阶至多
$$
\begin{aligned}
d_{\nu,p}
&=n_\nu(p^3-p^2+p+1)-p(p+2)\\
&=n_\nu p^3-(n_\nu+1)p^2+(n_\nu-2)p+n_\nu\\
&<n_\nu p^3.
\end{aligned}
\tag{10}
$$
若 $R_\nu(Q)=0$，实际极更低；本篇不把(10)误称为每点的准确极阶。
(8)–(10)已涵盖全部点。

## 3. 三次 Cartier 的固定有限返回

对任意局部参数 $u$，使用标准准确式
$$
\mathcal C\!\left(\sum_j a_j u^j\,du\right)
=\sum_m a_{pm+p-1}^{1/p}u^m\,du.
\tag{11}
$$
因此，极阶至多 $d>0$ 的微分经一次 Cartier 后极阶至多
$\lceil d/p\rceil$，经三次后至多 $\lceil d/p^3\rceil$。
正则微分仍正则，并且
$$
\operatorname{Res}_Q(\mathcal C\zeta)
=(\operatorname{Res}_Q\zeta)^{1/p}.
\tag{12}
$$
这些式子也说明 Cartier 与可分拉回相容。

令
$$
\rho_{\nu,p}=\mathcal C^3(\eta_{\nu,p}).
$$
由(8)–(12)得到真正先于 $p$ 固定的空间
$$
\boxed{
\rho_{\nu,p}\in
H^0\!\left(E_0,\Omega^1_{E_0}(O+n_\nu\mathcal D_2)\right),\qquad
\operatorname{Res}_O\rho_{\nu,p}=\alpha_\nu^{1/p^3}.
}
\tag{13}
$$
空间固定不表示其中的实际截面与 $p$ 无关。
(13)与旧无权 $\mathcal C^3(f_\nu^{\rm rat}\omega)$ 的区别是：
这里指定原首行已经变为留数，后续 Cartier 不再丢失它。

## 4. 原 $\mu_6$ 型与真正的有理底空间

对 $a_\zeta:z\mapsto\zeta z$，原型为
$$
a_\zeta^*Z=\zeta Z,\quad
a_\zeta^*G=\zeta^{-1}G,\quad
a_\zeta^*\omega=\zeta\omega,\quad
a_\zeta^*\mathcal P_2=\zeta^2\mathcal P_2.
\tag{14}
$$
最后一式也直接由(2)得到：每次 $\nabla_2$ 降型一，
输入 $Z^{p+1}$ 的型为 $p+1$，共降 $p-1$。
由 $R_\nu=x^{n_\nu}f_\nu(t)$，$\widehat A_\nu$ 的型为零。
所以
$$
a_\zeta^*\eta_{\nu,p}
=\zeta^{-p-1}\eta_{\nu,p}=\eta_{\nu,p}.
\tag{15}
$$
这里必须使用 $p\equiv-1\pmod6$。
自然性使 $\rho_{\nu,p}$ 也为不变微分。

真实商
$$
t:E_0\longrightarrow\mathbf P^1,\qquad t=-x^{-3}
\tag{16}
$$
次数为六；在 $O$、$\mathcal D_2$、$x=0$ 上的分歧指数分别为
$6,2,3$，对应底点 $0,1,\infty$。
因此存在唯一有理微分 $\bar\rho_{\nu,p}$ 使
$t^*\bar\rho_{\nu,p}=\rho_{\nu,p}$。
若底微分有极阶 $m\ge1$，在分歧指数 $e$ 的点拉回的极阶是
$e(m-1)+1$；这个首系数含 $e$，当前为单位。
于是(13)精确给
$$
\boxed{
\bar\rho_{\nu,p}\in
H^0\!\left(\mathbf P^1,
 \Omega^1_{\mathbf P^1}([0]+L_\nu[1])\right),\qquad
L_\nu=\left\lfloor\frac{n_\nu+1}{2}\right\rfloor.
}
\tag{17}
$$
在 $\infty$ 正则：一个底极即使简单，在分歧三拉回后也仍是极，
不可能由(13)消失。

四个固定空间的维数及极帽为
$$
\begin{array}{c|rrrr}
\nu&S&T&U&V\\ \hline
n_\nu&17&36&68&33\\
L_\nu=\dim H^0(\Omega^1([0]+L_\nu[1]))&9&18&34&17.
\end{array}
\tag{18}
$$
这里没有通过数值样本取得任何一个维数。
(17)的次数是 $L_\nu-1$，故其截面维数为 $L_\nu$。

## 5. 精确的对数项与唯一 exact 部分

因为 $L_\nu\le34<p$，(17)中每个微分有唯一表达
$$
\bar\rho_{\nu,p}
=a_{\nu,p}\frac{dt}{t(1-t)}
 +dH_{\nu,p}(t),
$$
$$
H_{\nu,p}(t)
=\sum_{j=1}^{L_\nu-1}\frac{h_{\nu,j,p}}{(t-1)^j},
\qquad H_{\nu,p}(\infty)=0.
\tag{19}
$$
证明可直接作部分分式：
在 $0$ 只容简单极，在 $1$ 至多 $L_\nu$ 阶，
在 $\infty$ 正则迫两个简单极的留数相加为零；
所有 $(t-1)^{-j}dt$、$2\le j\le L_\nu$，
均可除以非零 $j-1$ 唯一积分成(19)的极部分。
所以这里的 exact 部分及其常数也已固定，而不是任意代表。

由于 $t$ 在 $O$ 的分歧指数是六，留数拉回给
$6a_{\nu,p}=\alpha_\nu^{1/p^3}$。
从而
$$
\boxed{
\bar\rho_{\nu,p}
=\frac{\alpha_\nu^{1/p^3}}6\,
 d\log\frac{t}{1-t}
+dH_{\nu,p}(t).
}
\tag{20}
$$
这把(13)的四个原首行完整放到一个明确的固定对数直线上；
四个较大的固定空间中其余方向全是(19)列出的 exact 方向。
它没有证明对数系数非零。

## 6. 第四次 Cartier 准确保留原首行

Cartier 杀 exact 微分，并满足 $\mathcal C(d\log f)=d\log f$。
前者由(11)直接可见；后者可在各点用 $f=u^m$ 乘单位及(11)验证，
等价于 Cartier 的对数微分恒等式。
再对(20)取一次 Cartier，利用 $6\in\mathbf F_p^\times$，得到
$$
\mathcal C^4\eta_{\nu,p}
=\frac{\alpha_\nu^{1/p^4}}6\,
 t^*\!\left(d\log\frac{t}{1-t}\right).
$$
原坐标中
$$
\frac{t}{1-t}=-\frac1{y^2},\qquad
t^*d\log\frac{t}{1-t}
=-2\,\frac{dy}{y}
=-6\,\frac{x^2}{y}\omega.
\tag{21}
$$
因此符号与全部倍率准确为
$$
\boxed{
\mathcal C^4\!\left(
 Z^{-p-2}\mathcal P_2^{n_\nu}R_\nu\,\omega
\right)
=-\alpha_\nu^{1/p^4}\,\frac{x^2}{y}\omega.
}
\tag{22}
$$
右边的固定微分 $-(x^2/y)\omega$ 在 $O$ 的留数为一，
在三个非零二挠点各为 $-1/3$；总留数为零，与(9)、(12)一致。

于是有准确等价
$$
\boxed{
\alpha_\nu=0
\quad\Longleftrightarrow\quad
\mathcal C^4\eta_{\nu,p}=0
\quad\Longleftrightarrow\quad
\bar\rho_{\nu,p}=dH_{\nu,p}.
}
\tag{23}
$$
对四个来源可同时读取(23)，仍使用同一个 $Z,G,\mathcal P_2$。
没有得到四个不同的非零特征方向；
共同对数载体是一维，未知的是其中四个指定标量。

## 7. 四个来源共用的准确一变量输入

仍在本篇的 $b=1$ 共同模型上，令
$$
u=-\frac{x}{y},\qquad J_p(t)=\frac Zu,\qquad
\Theta_p(t)=x\mathcal P_2.
\tag{24}
$$
$u,Z$ 同型，$x\mathcal P_2$ 型零，故二者确属同一商域 $k(t)$。
这里 $\Theta_p$ 是指定有理解的有理替身，不能与特征零的 $\Theta=x\sigma^2$
作全局相等。

(5)自身已经下降，并且完整公式为
$$
\boxed{
\bar\eta_{\nu,p}
=\frac{(-1)^s}{6}\,
 t^{-s-1}(1-t)^{3s}
 J_p(t)^{-p-2}\Theta_p(t)^{n_\nu}f_\nu(t)\,dt,
\qquad t^*\bar\eta_{\nu,p}=\eta_{\nu,p}.
}
\tag{25}
$$
证明保所有倍率：$dt=3x^{-4}dx$ 给 $\omega=x^4dt/(6y)$，所以
$$
u^{-p-2}\omega
=-\frac16y^{p+1}x^{2-p}dt
=\frac{(-1)^s}{6}\,t^{-s-1}(1-t)^{3s}dt.
$$
此处用 $p+1=6s$、$y^2=x^3+1$；四个来源共有完全相同的
$J_p,\Theta_p$，只有原 $n_\nu,f_\nu$ 改变。

还可将 $J_p$ 写成一个准确的原多项式比值。
令 $m=(p-1)/2=3s-1$。R636 §1(3)指定的函数正是
$$
\mathscr R_p(x)
=\frac12\sum_{j=0}^{m}\binom mj\,\frac{x^{3j+1}}{3j+1}.
\tag{26}
$$
这些分母在当前特征均为单位。对(26)作 $j=m-i$ 的重排，
并使用 $2(3j+1)\equiv-(6i+1)\pmod p$，得到
$$
\boxed{
J_p(t)=\frac{A_m(t)}{(1-t)^m},\qquad
A_m(t)=\sum_{i=0}^{m}
 \frac{(-1)^i\binom mi}{6i+1}t^i.
}
\tag{27}
$$
(27)是原(26)的逐项恒等式；仅知道 $DZ=1$ 并不能排除附加水平项，
所以不能用该微分等式代替(26)的核对。

逐系数以及有限二项式恒等式还给
$$
6tA_m'(t)+A_m(t)=(1-t)^m,\qquad
A_m(0)=1,\qquad
A_m(1)=\frac{m!}{(7/6)_m}\ne0.
\tag{28}
$$
最后的分母因子为 $7,13,\ldots,6m+1=3p-2$，均不为 $p$ 的倍数；
分子 $m!$ 亦为单位。若 $A_m(a)=0$，则 $a\ne0,1$，
(28)使 $A_m'(a)=(1-a)^m/(6a)\ne0$，故全部根简单。
§2 已证明这些根对应的所有非原点 $Z$ 零点在完整(25)中都被
$\mathcal P_2^{n_\nu}$ 抵消，不能只看 $J_p^{-p-2}$ 而额外增加极点。

(25)–(28)固定了后续可用的共同输入，尚未评价其中四个原留数。
一般 $b$ 模型的 $u^6=-t/[b(1-t)^3]$ 会在(25)增添 $b^{-s}$；
本篇始终在 $b=1$ 模型，原算术尺度按 R821 的既定运输恢复，
没有混用两个规范。

## 8. 与旧迭代测试的区别及实际后续门

原固定 torsion 注 §19 的测试差能保持无权输入的两次及三次
Cartier 输出而改变原首行。
它不能同时保持这里的三次加权输出：
若一个合法局部测试差把该首行加一，则
$$
\operatorname{Res}_O\,
\mathcal C^3\!\left(Z^{-p}\Delta f\,\omega\right)=1,
\tag{29}
$$
直接由(9)、(12)得到。
(29)不声称该差保留原四个 $\mathcal P_2^{n_\nu}R_\nu$；
这些指定来源从来没有被自由化。
它只说明旧“无权迭代看不见首行”的检验不能原样用于(20)。

本篇也没有把一个随 $p$ 变化的有理输入冒充固定有限代数来源。
(5)的乘数和原 $\mathcal P_2$ 都依赖 $p$；
固定的是(17)、(19)的目标及(22)的对数直线。
要完成原无穷性，仍须利用四个真实 $R_\nu$ 与同一 $\mathcal P_2$
的约束，证明在无穷多个允许的 $p$ 上，至少一个(22)非零。
四个完整中央若同时为零，原桥给四个首行零，故四个(22)都为零；
本篇不反用这条必要条件断言完整中央为零。

没有新增数学运行、素数扫描或可重算输出。
所有等式均由原指定有限窗口、全极资料、Cartier 局部公式及实际有限商逐项证明。

依赖：
[R636](R636-original-rational-cartier-return-for-two-critical-rows.md)及
[R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)的原模型以
[固定 torsion 原注](../notes/2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md) §§1、5、13–19所记完整来源为准；
[R821](R821-original-four-central-axes-and-complete-four-block-carries.md)
保四个原 $R_\nu$、全中央必要首行及所有原算术尺度。
