# R375：真实 Y 第二 cubic 恒等与十三行联合根支付 ZY2 和 YY2

日期：2026-11-15。**完整有限纸面证明；未运行求积、符号程序、参数扫描、人工测试或研究计算。**

本稿沿 R373 的同一个全偶真实弱圆构造，新增两个完整角函数：
$ZY$ 第2外矩及 $Y^2$ 第2外矩。
它们可以共用原 $F_{Y,2}\equiv0$ 的准确身份；因此本稿无需假设一个新的 $C^2$ 角商已由旧纤维固定。

先把两个完整对称矩化为对真紧 $D$ 的线性读出，保原 $Y(f,f)$ 的真实二次左尾和 $I_2$ 的两个项。
随后两个主行的真实最高位置次数分别为8与10。
原五种 $\chi$、60个实际正幅列的十二点 kernel 正好覆盖次数至多10；
同一有限频率十三行根因此同时保持原十一行并支付这两个新值。
$ZZ_2$ 仍未支付，不由本稿类推。

来源：
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R291](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)、
[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)、
[R368](R368-two-exact-cubic-identities-and-seven-target-control-pay-the-PY-product.md)、
[R369](R369-vanishing-first-cubic-and-eight-target-control-pay-the-ZW-product.md)、
[R372](R372-complete-ZZ-zero-angular-quotient-and-nine-target-finite-frequency-control.md)、
[R373](R373-complete-W-square-angular-quotients-and-eleven-target-control.md)。

## 1. 当前对象、原系数和需要共同保持的目标

仍用
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=dL+eU.
$$
固定 $0<\zeta=\kappa^2<1/100$、$\kappa>0$，原系数为
$$
a=-\frac{51\zeta^2+2\zeta+8}{64h_e^2},\quad
b=-\frac{34\zeta^2+8\zeta}{64h_e^2},\quad
d=\frac{6\kappa\zeta}{h_e},\quad
e=-\frac{\kappa(15\zeta+1)}{4h_e}\ne0.
\tag{1}
$$
本稿不更改这些 Gaussian 方向。

设
$$
\phi=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-\phi\odot\phi.
$$
$f,g$ 是当前同一个全偶实紧圆，保
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0.
\tag{2}
$$
因此 $ZD,YD$ 的三种原左尾全部为零，是真紧函数。
弱单 hook、非零 derivative rank-two 核及完整第二／第三 range 按既有构造保持。

继续使用 normalized 对称外矩
$$
\mathcal Q_{XY,j}
=-I_j(XD,YD)+I_j\{\phi,X(\phi,YD)+Y(\phi,XD)\}.
\tag{3}
$$
$I_2(u,w)=\int(x^2u''w''+2u'w')$，不删第二项。
对 $X=Y$，(3)的 nested 部分有准确因子2。

共同保留的旧条件是全部18个反对称 Gaussian 外矩、
R364 的真实局部 $\mathcal T=0$、$\Psi$、原三条 directed 行、
指定一层／完整第三，以及 R373 已付的完整
$$
P^2,\ PW,\ PZ,\ PY,\ ZW,\ W^2
$$
和 R372 的 $ZZ_0$。
它们不能在新增两个门时分开换到不同最终圆。

## 2. 原 F_Y2 恒等的适用域：真右锚、任意正负支撑

R291、R368 已从原完整 $Y$ 式证明
$$
\boxed{F_{Y,2}(u):=I_2\{u,Y(u,u)\}=0}
\tag{4}
$$
对任意实紧 $u$ 成立，不要求单包三矩为零。

为明确本稿使用的尾和负轴范围，写
$$
v=u',\quad r=u'',\quad C=J(x^2r^2+2v^2),
$$
$$
Y(u,u)=-xu^2+x^2uv-\frac{x^3v^2}{2}-\frac{x^2C}{4},
$$
$$
Y'=-u^2+x^2ur-x^3vr+\frac{x^4r^2}{4}-\frac{xC}{2}.
\tag{5}
$$
$Y(u,u)$ 的左尾一般是 $-I_2(u,u)x^2/4$，并未设成零。
将(5)及原二导代入 $I_2$，完整 primitive 项为
$-\frac12\int(x^2v)'C$。
只由紧 outer 的端值与 $C'=-(x^2r^2+2v^2)$ 积分后，
整个 cubic 收为
$$
-\frac13\int(x^3v^3)'-\frac23\int(u^3)'=0.
$$
这正是(4)的无除 $x$ 证明；即使实际区间跨过零也合法。

对真正紧的 $u,w$，沿紧族 $u+tw$ 微分(4)，得到
$$
\boxed{
2I_2\{u,Y(u,w)\}=-I_2\{w,Y(u,u)\}.
}
\tag{6}
$$
右侧仍保完整 $Y(u,u)$ 的二次左尾。
本稿只在 $w=ZD,YD$ 这样的真紧方向上用(6)，
不沿单包 nonlegal 输出偷用紧变分。

## 3. 两个完整 mixed 原式

记 full area 按 $I$ 规范为
$$
\mathcal A_{ZY,2}=I_2\{\phi,[Z,Y](\phi;D)\}.
$$
原18面积已给 $\mathcal A_{ZY,2}=0$，所有相位成立。
由
$$
I_2\{\phi,Z(\phi,YD)+Y(\phi,ZD)\}
=2I_2\{\phi,Y(\phi,ZD)\}+\mathcal A_{ZY,2},
$$
在(6)取 $u=\phi,w=ZD$，得到
$$
\boxed{
\mathcal Q_{ZY,2}
=-I_2\{Y(f,f),ZD\}+\mathcal A_{ZY,2}.
}
\tag{7}
$$
这里使用 $YD+Y(\phi,\phi)=Y(f,f)$，并保原对称配对的两个项。

再在(6)取 $w=YD$，直接得到
$$
\boxed{
\mathcal Q_{YY,2}=-I_2\{Y(f,f),YD\}.
}
\tag{8}
$$
(8)没有一个需要另付的 $[Y,Y]$ 面积。

式(7)—(8)是整个原 mixed 表达式，不是 pure 值或 principal。
其中 $Y(f,f)$ 的真实二次左尾一般非零；
真紧的是 $ZD,YD$。两者不能混同。
同样没有删去内部 ordered history 或将所有单微包都当成三矩合法。

已付 $\mathcal A_{ZY,2}=0$ 后，右侧准确线性于
$$
D=\sin^2\theta(f^2-g^2)-2\sin\theta\cos\theta\,fg.
$$
原十二完整副本准确清除 $\sin\theta\cos\theta$ 系数，故
$$
\boxed{
\mathcal Q_{ZY,2}(\theta)
=\sin^2\theta\,\mathcal Q_{ZY,2}(\pi/2),\qquad
\mathcal Q_{YY,2}(\theta)
=\sin^2\theta\,\mathcal Q_{YY,2}(\pi/2).
}
\tag{9}
$$
所有实际平移、多副本和正四次权都仍在原十次界中。

按 R294 的额外角商写法，对合法复 $q=f+ig$，
$K_{ZY,2}(q)=S_{ZY,2}(q)/2$、$K_{YY,2}(q)=0$；
这只是(6)—(8)的同一原身份。
因此本稿没有新增一个尚未证明由 $\mathcal F_{\rm new}$ 保持的 $C^2$ 条件。

## 4. 完整 block 的真尾相加

新原式还允许直接核对并置过程。
每个最终完整 block 的 $D_i$ 都有三矩零，故 $ZD_i,YD_i$ 真紧。
另一完整 block 的 $Y(f_j,f_j)$ 在其左侧保真实二次尾
$p(x)=Ax^2+Bx+C$，在右侧真零。

对任意紧 $w$，原完整 $I_2$ 准确满足
$$
I_2(p,w)
=2A\int x^2w''+4A\int xw'+2B\int w'=0,
\tag{10}
$$
因为三项分别为 $4A\int w,-4A\int w,0$。
$2p'w'$ 正是这里不可省略的抵消项。

因此(7)—(8)跨这些完整 blocks 的尾配对准确为零。
各 block 内部的单微包尾和 ordered history 仍留在完整函数中。
这个论证适用于保三矩的实际弱 block，不要求其内部 rank-one；
它不是把 R259 的逐微包公式越界套到弱 rank-two 核。

## 5. 两个新增真实主行

仍只在末端强控制器的 rank-one 微包上扰动。
写
$$
f_i=a_i u_i,\quad g_i=b_i u_i,\quad
\lambda_i=-a_i^2(a_i^2-b_i^2),
\quad v=u_i',\ r=u_i'',\ t=u_i'''.
$$
原主系数为
$$
\alpha_Z=du+(2e-d)xv-3ex^2r,
\qquad
\alpha_Y=x^2u-x^3v+\frac{x^4r}{2}.
$$
R285 完整保尾的分裂给
$$
\mathcal Q_{ZY,2}(\pi/2)
\equiv_2\sum_i\lambda_i\int x^2\alpha_Z\alpha_Y\,t^2,
$$
$$
\mathcal Q_{YY,2}(\pi/2)
\equiv_2\sum_i\lambda_i\int x^2\alpha_Y^2\,t^2.
\tag{11}
$$
$\equiv_2$ 的余项是实际连续 $C^2$ 多项式泛函，
含全部 Green、右历史、copy 低项和 $I_2$ 的 $2X'Y'$。
最后求根时它们全部评价，不只保主项。

对同一个偶母、一个实际偶 $\chi_\alpha$，
把完整复制分支写为 $x=X+d_\nu+y$，保正权 $\omega_\nu$。
令
$$
R_\alpha=\int r_0^2\chi_\alpha^2>0,\qquad
W_c=\sum_\nu\omega_\nu>0.
$$
则(11)的两行是 $X$ 的真实多项式：

- $ZY_2$ 次数8，最高系数准确为
$$
-\frac{3e}{2}\,W_cR_\alpha\ne0;
$$
- $YY_2$ 次数10，最高系数准确为
$$
\frac14\,W_cR_\alpha>0.
$$

这些最高系数分别来自
$x^2(-3ex^2r)(x^4r/2)$ 与
$x^2(x^4r/2)^2$。
所有偏移产生的低次项仍保留，不将实际 copy 换成同心模型。
空间镜像对这两个目标为反射偶，贡献同号实际列。

## 6. 原60列直接给十三维严格正锥

沿用 R373 从起点选出的同一个母及五个 $\chi$：
原有限 $\mathcal F_{\rm new}$ 最大 minor 与五种真实形状的严格点值 minor 同时成立。
原十一行的位置次数全部不超过6，其联合 span 已证明为 $\mathbb R^{11}$。

现在每组仍取十二个原实际交替位置
$$
0,1,33,34,49,50,65,66,81,82,97,98.
$$
对真实递增 $X_i$，
$$
\beta_i=\frac1{\prod_{k\ne i}(X_i-X_k)},\qquad
\frac{\beta_i}{\lambda_i}>0.
$$
十二点准确消去所有次数至多10的位置多项式。
本稿新增最高次数恰为10，没有超出原正 kernel 的准确范围。
故每组原严格正 kernel 同时杀全部十三行。

若一个行 covector 消灭五组全部实际列，每组所得多项式次数至多10，
有十二个不同零点，故恒零。
看十次系数先迫 $YY_2$ 新坐标为零；
看八次系数再迫 $ZY_2$ 新坐标为零，因为 $e\ne0$。
余下原十一行的 covector 再由 R373 的已证满秩迫零。
所以
$$
\boxed{
\operatorname{rank}(\text{60个真实十三行列})=13.
}
\tag{12}
$$
每组严格正 kernel 与联合 span 共同给
$$
\boxed{
\operatorname{cone}_+(\text{60个真实十三行列})=\mathbb R^{13},
\qquad\ker\cap\mathbb R^{60}_{>0}\ne\varnothing.
}
\tag{13}
$$
这一步没有增加形状自由量，也没有把 signed span 当成正幅可实现性。
原十一行证明中的有限 Hermite 正母和同母最大 minor 原样适用。

## 7. 同一个有限 N 的十三行完整根

仍从最后控制器以前的实际入口开始：
弱核及全部旧宏块已固定，全部18面积与 R364 的
$$
\mathcal T=\operatorname{Re}
\{\mathfrak k(f+ig)-\rho_\kappa\mathfrak j(f+ig)\}
$$
为零，并留负 $\Psi$ 供末强块支付。
不在一个已冻结的十一行根上任意更换 profile。

从起点保持同一有限映射
$$
\mathcal F_{\rm new}
=(\mathcal F_\star,\
\text{全部 }\mathfrak j,\mathfrak k
\text{ 的真实平移系数}).
\tag{14}
$$
先选同母最大 minor、五种 $\chi$、全部实际 copy 与最终中心，
再用末强块的静态正幅支付 $\Psi$。
每个选定微包使用
$$
u_{N,z}=u_0+N^{-3}z\chi_\alpha\cos Ny
+\sum_\ell a_\ell(N,z)e_\ell,
\qquad
\mathcal F_{\rm new}(u_{N,z})=\mathcal F_{\rm new}(u_0).
\tag{15}
$$
最大 minor／局部常秩保持整个(14)。
有限正幅盒先固定，纠正及参数一导在 $C^2$ 为 $O(N^{-1})$，
固定光滑纠正方向的三导贡献同阶。

完整十三目标按顺序为
$$
\begin{aligned}
\mathbf G_N={}&(
\mathcal Q_{PP,0},F_0,F_1,F_2,
\mathcal Q_{PZ,2},\mathcal Q_{PY,0},\mathcal Q_{PY,2},
\mathcal Q_{ZW,1},\mathcal Q_{ZZ,0},\\
&\mathcal Q_{WW,0},\mathcal Q_{WW,2},
\mathcal Q_{ZY,2},\mathcal Q_{YY,2})(\pi/2).
\end{aligned}
$$
R285 的原 $C^2$ 分裂、原完整 block 加法及本稿(10)给
$$
\mathbf G_N(\mathbf z)
=\mathbf G_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1)
\tag{16}
$$
在该有限盒上一致成立。
基线含弱 rank-two 核、宽 cutoff、全部补矩、
旧面积和角商模块、所有真实 Green／右历史／内部尾、
完整 copy 权及最终位置；不以微包近似替代它们。

由(13)，把 $-\mathbf G_{\rm base}$ 表为全部严格正的平方幅组合。
选十三个独立列并固定其余正幅，极限 Jacobian $2z_iv_i$ 可逆。
非退化零在小 $C^1$ 扰动下稳定，因此存在一个足够大但实际有限的整数 $N$ 和精确正幅根
$$
\boxed{\mathbf G_N=0.}
\tag{17}
$$
这是同一个最终圆上的十三行共同求根，不是拼接不同最终圆的结论。

(15)保持全部18面积、末强块原72面积数据、R364 的 $\mathcal T$ 与 quartic $C$，
故 $\Psi$、原三条 directed 行、指定一层／完整第三保持。
原十一行及各自准确角商身份恢复完整六个旧乘积与 $ZZ_0$。
本稿(7)—(9)将新两行提升为
$$
\boxed{
\mathcal Q_{ZY,2}(\theta)=
\mathcal Q_{YY,2}(\theta)=0
\qquad\text{全部相位}.
}
\tag{18}
$$

同一证明可把最后两行指定为任意固定有限实数 $(\tau_Z,\tau_Y)$，
前十一行为零；两个完整函数准确为
$\tau_Z\sin^2\theta,\tau_Y\sin^2\theta$。
因此新增的是两个可同点联合调节的真实方向。

## 8. 选择顺序及尚未支付的四个位置

本稿没有增加末控制器以前的面积或角商费用。
先固定弱核、所有原模块、负 $\Psi$ 储备和有限映射(14)；
随后选择同母最大 minor、五个实际 $\chi$、全部 copy、最终中心与静态正幅；
再固定有限正幅盒，最后取同一个有限 $N$ 解(17)。
根后不再平移、换锚或拆开共享副本。

所有有限 profiles 和正负支撑确定后，
按 R354 选新共同物理区间、足够大的 $\omega$ 下界及初始小 $h_e$，
真实安装闭 hook 与共振保护芽。
新 $ZY_2$ 的共同非零 $h_e$ 行因子及 $YY_2$ 的规范不改变零目标；
(1)的 $e\ne0$ 保证最高系数不退化。
不继承另一条几何的 wholeE、Morse 或全 period。

当前仍未支付的反射允许对称位置准确为
$$
\boxed{ZZ:2;\qquad ZY:0;\qquad WY:1;\qquad YY:0.}
$$
这是四个完整角函数位置，不是独立 rank，也不是已知可自由指定的四个 scalar。
尤其 $ZZ_2$ 的真实同权 $C^2$ 角商不能因为本稿主次数增加而被忽略。

原 canonical 第四 period、其余零／一 Gaussian history、
平台／退化通量／端芽、整条闭路径 ruling 及同一 gauge 的 joint 条件仍未付。
本稿严格完成的是同一最终全偶真实弱圆上，
新增 $ZY_2,YY_2$ 全角与全部既有面积、局部角商、六个旧完整对称乘积、
$ZZ_0$、$\Psi$ 和三行的联合有限支付。
