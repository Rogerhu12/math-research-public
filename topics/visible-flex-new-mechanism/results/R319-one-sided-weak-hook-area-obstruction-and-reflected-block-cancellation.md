# R319：单向弱 hook 曲段的更早面积障碍与正反完整块的一门支付

日期：2026-11-15。**完整纸面原式推导。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R317](R317-exact-weak-hook-mixed-correction-and-nonnegative-branch-obstruction.md) 给出了弱 hook 离开导数 rank-one 后的一层准确修正。在检验负分支点能否抵消该修正时，必须先回到原完整面积。其第零外矩已经给出更早的严格门：

> R308 的所有右向 $5/2$ 幂曲段，无论分支点正负，都对同一完整 Gaussian 面积给严格同号贡献。单纯把分支点移到负轴，不能在保持该面积为零的前提下使用一层修正的变号。

这也适用于全部左向曲段的同向族，符号相反。另一方面，正反两个真正完整三阶块可以准确相消此面积的**全部相位第零外矩**。该推论只支付这一门，不支付同一面积的另外两个外矩，更不宣布第四可解。

主要来源：[R250 原完整三槽与三个外矩](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R304 原小共振 Gaussian 必要门](R304-positive-one-history-remainder-excludes-disjoint-real-rank-one-circles.md)、[R306 弱 hook 与一般 mixed 原式](R306-derivative-rank-classification-and-overlapping-profile-Gaussian-obstruction.md)、[R308 真弱核圆与完整三阶](R308-genuine-derivative-rank-two-circles-with-one-hook-and-complete-third-range.md)及 R317。

## 1. 保留实际 weak hook、完整右锚和原系数

几何、右锚和小共振芽与 R317 相同：
$$
M=0,\qquad T=\kappa_H\mathfrak H,\quad\kappa_H\ne0,
$$
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100 .
\tag{1}
$$
$f,g$ 是实际三矩非退化圆，并已按 R308 支付完整三阶。只使用
$$
\mathfrak H(g;f,f)=0;
$$
不施加第二个 hook。令
$$
u=\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u,\qquad
d_0=(f'')^2-(u'')^2.
$$
因此
$$
\mathfrak H(u;D)=0
\tag{2}
$$
是完整相位恒等。

沿原方向记
$$
P=\Phi_{r_0},\quad W_*=a\Phi_{r_1}+b\Phi_{s_0},
\quad B_{-3}=c_PP,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\qquad
b=-\frac{17t^2+4t}{32h_e^2},\qquad
c_P=-\frac{\kappa(41t^2+27)}{216h_e^3}.
\tag{3}
$$
则
$$
a+3b=-\frac{153t^2+26t+8}{64h_e^2}\ne0,\qquad c_P\ne0.
$$

R250 的完整三槽原式为
$$
[W_*,P](u;D)
=\frac13\{(a+3b)J(u''d_0)+a\mathfrak H(u;D)\}.
\tag{4}
$$
用 (2)后只剩真实右原函数 $J(u''d_0)$。不要求这个单独原函数的左常尾为零。

## 2. 第零外矩准确化为一个真实局部配对

记 $r=u''$，$v=u'$，$F=(f'')^2$。令
$$
w=J\{r(F-r^2)\}.
$$
其真实导数是
$$
w'=-r(F-r^2),\qquad
w''=-r'(F-r^2)-r(F-r^2)'.
$$
由于外 profile $u$ 紧支撑，合法全区分部积分给
$$
\begin{aligned}
I_0(u,w)
&=\int r w''\\
&=-\frac12\int(r^2)'(F-r^2)
-\int r^2(F-r^2)'\\
&=-\frac12\int r^2F'
=-\int (u'')^2f''f'''.
\end{aligned}
\tag{5}
$$
$r^2(r^2)'$ 为全导数；边界由真实外 profile 的零 collar 消失。这个推导保留了 $w$ 的原左尾，未把 inner primitive 改成紧函数。

代入 (4)，得到所有相位的准确身份
$$
\boxed{
I_0\{u,[W_*,P](u;D)\}
=-\frac{a+3b}{3}
\int (u'')^2f''f'''.
}
\tag{6}
$$
这是完整 $A_{-2,-3}$ 面积的一个原外矩。若完整第四 ruling 可行，原 Gaussian 词独立性先迫该面积系数为零；原几何配对中三个外矩的系数函数独立，故 (6)也必须为零。不能用另一个 history 或合法 gauge 偶商吸收它。

在真实相位 $\theta=\pi/2$，必要条件尤其是
$$
\boxed{\mathcal M(f,g):=\int (g'')^2f''f'''=0.}
\tag{7}
$$

## 3. 真实曲段、补包、cutoff 的全部贡献

沿 R308 的最终物理位置，把发生 $W=g'f''-f'g''\ne0$ 的曲段记为 $J_\nu$。允许右向或左向：
$$
f(x)=A_\nu\{\varsigma_\nu(x-\beta_\nu)\}^{5/2},
\quad
g(x)=w_\nu(x)\in C_c^\infty(J_\nu),
\quad \varsigma_\nu\in\{+1,-1\},
$$
$$
\varsigma_\nu(x-\beta_\nu)>0
\quad\text{于 }\overline J_\nu.
\tag{8}
$$
所有分支点与实际紧支撑有严格距离，没有在幂分支点拼接非光滑函数。

直接求导得
$$
f''=\frac{15A_\nu}{4}\{\varsigma_\nu(x-\beta_\nu)\}^{1/2},
\qquad
f'''=\frac{15A_\nu\varsigma_\nu}{8}
\{\varsigma_\nu(x-\beta_\nu)\}^{-1/2},
$$
所以
$$
\boxed{f''f'''=\varsigma_\nu\frac{225A_\nu^2}{32}.}
\tag{9}
$$
它与 $\beta_\nu$ 的数值和符号完全无关。

其余区域的贡献也须支付。R308 原 cutoff 过渡区上 $g=0$，故对 (7)无贡献。在每个矩补偿包中，
$$
f=A\eta,\qquad g=B\eta
$$
取同一个真实实紧 bump，因而
$$
\int(g'')^2f''f'''
=A^2B^2\int(\eta'')^3\eta'''
=\frac{A^2B^2}{4}\big[(\eta'')^4\big]_{\rm ends}=0.
\tag{10}
$$
不要求这个补包独立满足原三矩。先得到全局原式 (5)–(7)，再对其真实局部密度分区，才可使用 (10)。

因此整个已配平 profiles 准确有
$$
\boxed{
\mathcal M(f,g)
=\frac{225}{32}\sum_\nu
\varsigma_\nu A_\nu^2\int(w_\nu'')^2.
}
\tag{11}
$$
所有同向曲段都给同号。至少一个 $w_\nu$ 非零；紧支撑非零函数的二阶导数不可能恒零，故该号严格。

八完整副本的幅度 $a_j=(-1)^j\binom7j^{1/3}$ 不能改变这个结论。它同时乘 $f$ 与 $g$，于是 (11)只按 $a_j^4>0$ 加权。原共同正缩放及矩归一化同样只乘正四次因子。

## 4. 对负分支点通道的严格结论

**定理 1。** 在 (1)的同一几何芽上，R308 的任意同向幂曲段族都不能通过完整第四 ruling。尤其所有右向曲段
$$
f=A_\nu(x-\beta_\nu)^{5/2}
$$
无论 $\beta_\nu$ 为正、零或负，均被 (7)排除。

证明：若全部 $\varsigma_\nu=+1$，由 (11)有 $\mathcal M>0$；若全部为 $-1$，则 $\mathcal M<0$。而 (6)前的常数非零，故必要面积第零外矩不为零。证毕。

对右向情形，去掉原 $c_P$ 的 (6)甚至严格为正。保留实际 commutator 规范，
$$
I_0\{g,[W_*,c_PP](g;f\odot f-g\odot g)\}
=
-\frac{\kappa(41t^2+27)(153t^2+26t+8)}
{41472h_e^5}\,\mathcal M(f,g)\ne0.
\tag{12}
$$
这里不需要先设 R317 的三个 directed 行为零，也不需要比较一层正负余量。

因此 R317 中 $9x+5\beta_\nu$ 的变号不能在这批同向 profiles 上独立使用：当仅改变右向分支点为负时，原更早面积已经严格失败。这是联立必要条件的实际否定，不是只观察一个积分的符号。

本定理没有把所有弱 hook 圆排除。特别不同方向的曲段在 (11)中有真正反号，不能从同向证明删掉这些反号。

## 5. 正反完整块可以准确支付该门的全部相位

下面给一个明确的新正向推论，只支付 (6)这一门。

取 R308 的一个完整基本三矩对 $(f_*,g_*)$，使其右向曲段非零。再取同宽反射
$$
(f_*^-,g_*^-)(x)=(f_*,g_*)(d-x).
\tag{13}
$$
反射后的三个复矩按
$$
M_0\longmapsto M_0,\quad
M_1\longmapsto dM_0-M_1,\quad
M_2\longmapsto d^2M_0-2dM_1+M_2
$$
变换，所以仍全零。对弱 hook 不假定任意坐标协变：反射使 $A_f$ 保号、$W$ 反号，因此 $A_fW=0$ 保持；共同右锚恢复仍给 $\mathfrak H(g_*^-;f_*^-,f_*^-)=0$。

先在最终给定的合法区间内安排两个互不交的完整块包络。正向基本对和反向基本对分别使用相同宽度、相同八个有限差分幅度，独立执行 R308 的八副本三阶构造。所有位置、宽度和几何在此时固定。由原二阶局部化、四条 ruling 的次数至多六以及真实弱周期，各自都已完整支付三阶。没有假定把一个已经完成的固定几何 ruling 任意反射后仍自动为零；反射的是基本 profile 对，然后在该最终几何上重新应用准确的八副本恒等。

令两最终块为 $(f_+,g_+)$ 与 $(f_-,g_-)$。对任意实紧 pair，写
$$
\mathcal N(f,g)=\int(f'')^2g''f''',\qquad
\mathcal M(f,g)=\int(g'')^2f''f'''.
$$
由 $\int(f'')^3f'''=0$，完整相位配对为
$$
\int(\phi_\theta'')^2f''f'''
=2\cos\theta\sin\theta\,\mathcal N(f,g)
+\sin^2\theta\,\mathcal M(f,g).
\tag{14}
$$
$\mathcal N,\mathcal M$ 均不含显式 $x$，故平移不改其值。同宽反射只使 $f'''$ 改号，准确给
$$
\mathcal N(f_*^-,g_*^-)=-\mathcal N(f_*,g_*),\qquad
\mathcal M(f_*^-,g_*^-)=-\mathcal M(f_*,g_*).
$$
每个八副本块再乘同一个四次权和
$$
W_4=\sum_{j=0}^7|a_j|^4>0.
$$
因此两完整块的上述二元向量仍准确互为相反数，与两个块的最终不同物理位置无关。

现在以相同实幅度合并
$$
f=f_++f_-,\qquad g=g_++g_- .
\tag{15}
$$
两个完整包络互不交，原三矩按平方相加，弱通量逐区成立，二阶 canonical 场局部化，三阶 forcing 与 ruling 按三次相加。因此 (15)仍是一条非退化、真正导数 rank-two、完整三阶已付的弱 hook 圆。

而 (14)的两个系数准确相消，所以
$$
\boxed{
I_0\{\phi_\theta,[W_*,P](\phi_\theta;D_\theta)\}=0
\qquad\text{对全部 }\theta.
}
\tag{16}
$$
如需原 $I_0(f,f)=I_0(g,g)=1$ 的规范，再作一次共同正幅度归一化，(16)仍为零。

这一推论没有把单个曲段当作独立合法 packet。用于相加的是已经三矩配平、八副本 ruling 与组合周期均已支付的两个完整块；真实第三 history 与其包内尾仍保留。

## 6. 新推论的准确剩余范围

(16)仅支付完整 $A_{-2,-3}$ 面积的第零外矩。含 $x$ 与二次权的另外两个外矩不会仅因反射自动相消；原算子本身也含 $x$，不能把一般平移解释成只搬动一组已付 moments。

R317 的完整 mixed 一层、其余 Gaussian 面积与对称乘积、真实零/一层、第四周期及所有平台门仍须对 (15)这个同一 profiles 和同一实际几何重新判断。本稿没有继承旧 rank-one 模板的任何未证消项。

R308 的完整三阶正向结论保持；新增内容是对全部同向曲段（包括负分支点）的更早严格否定，以及一个通过正反两个真实完整块准确支付 (16)的建设性入口。
