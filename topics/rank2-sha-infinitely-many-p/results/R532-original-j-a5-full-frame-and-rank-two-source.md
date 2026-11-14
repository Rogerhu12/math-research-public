# R532 — 原 J/A5 的完整六轴核与恰二秩 sigma 张量

日期：2026-11-14。**状态：已证明。** 在 R529 的同一个原六 sigma 来源中，$A_5$ 的 whole odd 核确为已有符号 $\chi_{65}\lambda$，两个实际伴随也可逐轴定标。由此得到整个六输入的正交 scalar 框架。

忘去其中四个明确伴随时，原 $S$ 的两个真实输出有一个恰为二秩的整 theta 张量。四个因子均显示为原 sigma 和 R522 的同一个 $B_3$ 的卷积，所有常数、半特征、完整中心都保留。原五深事件则仍含 $J+K$ 的真实近相消条件；二维张量不替代这个受限联合。主目标尚未完成。

## 1. 原四个 T 固定输出中的新正交框架

沿用 R529 的物理顺序、普通周期及符号
$$
\xi=(\xi_1,\xi_2,\xi_3,x,c,d_0),\quad
\rho_0=-\nu_\sigma^{\otimes6}/84,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,
$$
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
a=2+\omega=-\omega\delta,\quad b=17.
\tag{1}
$$
保 R529 的真实 $J,K,E$，其中
$$
2J=(1,0,\omega^2,-a,-1,0),\quad
2K=(1,0,\omega^2,a,-1,0),\quad
3E=(a,0,\omega-1,0,1-\omega,0).
\tag{2}
$$
定义新的原整行
$$
Q_3=(1,0,1,0,-\omega^2,0),\qquad N(Q_3)=3,
$$
以及
$$
\boxed{
s_0=\frac a3Q_3,\quad
A_5=s_0+\delta\xi_2+d_0,\quad
B_2=s_0-d_0,\quad
C_{30}=3s_0-2\delta\xi_2+3d_0.
}
\tag{3}
$$
所有符号均表示作用于原 $\xi$ 的实际输出，不是另引独立随机输入。

精确 Gram 为
$$
\boxed{
\operatorname{Gram}(J,A_5,K,E,B_2,C_{30})
=\operatorname{diag}\left(\frac32,5,\frac32,1,2,30\right).
}
\tag{4}
$$
完整行列式及其范数是
$$
\boxed{
\det=-\frac{45}{2}+\frac{15}{2}\delta,\qquad
N(\det)=675=3^3\,5^2 .
}
\tag{5}
$$
当前普通处的完整逆因此整。附证书给全部原行、逆及 Gram。

原三阶几何在这个六输入框架中的真实作用恰为
$$
\boxed{
\mathcal T:\ (J,A_5,K,E,B_2,C_{30})
\longmapsto(J,A_5,\omega^2K,\omega^2E,B_2,C_{30}).
}
\tag{6}
$$
这没有将旧四维投影误认成完整原几何；(6) 是从原六乘六矩阵直接相乘所得。

原算术输出准确为
$$
\boxed{
Y=\frac{2(-1+4\omega)}3J+2A_5.
}
\tag{7}
$$
特别 $J\perp A_5$，且两项对 $N(Y)=34$ 的贡献分别是 $14,20$。

## 2. 全部半特征、完整中心和 A5 的绝对核心

按 (4) 的顺序清分母，可用整行
$$
2J,\quad3A_5,\quad2K,\quad3E,\quad3B_2,\quad C_{30},
$$
其完整度数分别是
$$
\boxed{6,\ 45,\ 6,\ 9,\ 18,\ 30.}
\tag{8}
$$
例如新三行的原系数是
$$
\begin{aligned}
3A_5&=(a,3\delta,a,0,\delta,3),\\
3B_2&=(a,0,a,0,\delta,-3),\\
C_{30}&=(a,-2\delta,a,0,\delta,3).
\end{aligned}
\tag{9}
$$
第一行有五个 odd 系数，后两行各有四个；故分别是标准
odd45、even18、even30。任一第一轴与另外五个输出的 Hermitian
交叉全零，所以这些标准半特征不随伴随变量扭曲。

R496 的 $g_\pi\equiv91+72\omega\bmod576$，连同原
$\pi_0\equiv2\bmod5$，给完整共同同余
$$
\boxed{g_\pi\equiv91\pmod{180}.}
\tag{10}
$$
于 (8) 各个 $2N$ 的准确值是
$$
\begin{array}{c|rrrrrr}
N&6&45&6&9&18&30\\ \hline
g_\pi\bmod2N&7&1&7&1&19&31 .
\end{array}
\tag{11}
$$
even 行均是 $1+N$，odd 行是 $1$；故相应 canonical
Heisenberg 交织在整个标准空间为 scalar。这里保 $2N$ 的中心，
未以模 $N$ 的作用代替完整相位。

R529 已定 $J,K,E$ 的实际核心为 $\beta$。
R513 已通过非零固定拉回
$[\gamma_{13}]^*\mathcal S_5^{\rm odd}\subset\mathcal S_{65}^{\rm odd}$
支付
$$
K_5=\chi I,\qquad \chi=\chi_{65},\qquad\chi^2=1.
$$
现在用保持标准 odd 半特征的非零拉回
$$
[3]^*\mathcal S_5^{\rm odd}\subset\mathcal S_{45}^{\rm odd}.
$$
它与真实普通核交换，因此 (11) 中整个 odd45 的绝对标量严格为
$\chi$，不是重新猜一个符号。于是
$$
\boxed{A_5\text{ 的实际单层核心为 }\chi\lambda.}
\tag{12}
$$
另外整个 even18 由真实非零 $\Theta(3z)$ 锚定为 $-I$，所以
$$
\boxed{B_2\text{ 的实际单层核心为 }\beta.}
\tag{13}
$$

## 3. C30 的 whole 标量由同一三输入定标

$Q_3$ 是标准 odd degree3，真实 $\sigma(\delta z)$ 锚给其核心
$\beta$。原 $\xi_2,d_0$ 各自仍为独立 sigma，核心也为 $\beta$。
这三轴与 $J,K,E$ 正交。

由 (3)，完整变换是
$$
\begin{pmatrix}3A_5\\3B_2\\C_{30}\end{pmatrix}
=
\begin{pmatrix}
a&3\delta&3\\
a&0&-3\\
a&-2\delta&3
\end{pmatrix}
\begin{pmatrix}Q_3\\\xi_2\\d_0\end{pmatrix},
\qquad
\boxed{\det=-90\omega.}
\tag{14}
$$
因此两侧的共同深度事件完全相同，全部三层之外的原输入也保留。
它们的同时物理缩放是同一个三维正交投影上的 $\kappa$ 倍。

由 (11)，整个 $\mathcal S_{30}$ 的核心是某个 scalar $c$。
在同一个非零完整来源上，(14) 的左侧同时深系数为
$(\chi\lambda)\beta(c\lambda)=-\chi c\lambda^3$，
右侧为 $\beta^3=-\lambda^3$。消去实际非零推前测度后，严格得到
$$
\boxed{K_{30}=\chi I,\qquad C_{30}\text{ 核为 }\chi\lambda.}
\tag{15}
$$
本定标不需要找一个不存在的范数十五 CM 乘子，也不以中央或质量代替来源。

综合得整个六轴的真实单层核心表
$$
\boxed{
\begin{array}{c|rrrrrr}
\text{轴}&J&A_5&K&E&B_2&C_{30}\\ \hline
\text{核心}&\beta&\chi\lambda&\beta&\beta&\beta&\chi\lambda .
\end{array}}
\tag{16}
$$
它对 $\rho_0$ 成立；由 (6) 和
$h=\omega^2\mathcal T_*\rho_0$，也对 $h$ 成立。本篇没有把这些原
whole 空间自动套到未经处理的任意 quarter 来源。

对于六个非负深度 $(r,s,k,e,\ell,m)$，记
$P_{\boldsymbol n}$ 为在 (4) 中逐轴乘相应 $\kappa$ 幂的完整物理矩阵。
正交性使这些实际核交换，准确有
$$
\boxed{
\nu_\mu|_{\substack{J\in p^r,\ A_5\in p^s,\ K\in p^k\\
 E\in p^e,\ B_2\in p^\ell,\ C_{30}\in p^m}}
=
\beta^{r+k+e+\ell}(\chi\lambda)^{s+m}
(P_{\boldsymbol n})_*\nu_\mu,\quad \mu=\rho_0,h.
}
\tag{17}
$$
(17) 保整个六维测度及任意真实移权，不只是六条边际。

## 4. 原两个输出的显式六 sigma 来源

取整输出
$$
\boxed{U=2J,\qquad V=3A_5,\qquad N(U)=6,\quad N(V)=45,\quad U\perp V.}
\tag{18}
$$
其真正二维推前的生成函数记为 $\Phi(s,t)$。
由 (2)、(9) 逐个原输入代入，
$$
\begin{aligned}
\Phi(s,t)=-\frac1{84}\,
&\sigma(s+at)\sigma(3\delta t)
 \sigma(\omega^2s+at)\\
&\cdot\sigma(-as)\sigma(-s+\delta t)\sigma(3t).
\end{aligned}
\tag{19}
$$
所有六个 sigma 都来自原输入，未增加一个未支付的独立来源。

使用 $\sigma(\omega z)=\omega\sigma(z)$、
$\omega a=\omega-1$、$\omega^2a=-\delta$，两个奇负号抵消，准确为
$$
\boxed{
\Phi(s,t)=
-\frac{\omega^2}{84}\sigma(as)\sigma(3\delta t)\sigma(3t)
 \prod_{j=0}^2\sigma(s+\omega^jat).
}
\tag{20}
$$
它是整个 $\mathcal S_6\otimes\mathcal S_{45}$ 的真实来源。
从原完整框架到这两个输出的忘去操作，以及前面的单位缩放，
均已由 (5)、(18) 明确固定。

## 5. 三 sigma 全局恒等式与同一个 B3

设 $x_\wp,y_\wp=x_\wp'/2$ 满足 $y_\wp^2=x_\wp^3+b$。
原等谐 sigma 的完整规范给
$$
\boxed{\sigma(az)=a\,x_\wp(z)\sigma(z)^3.}
\tag{21}
$$
证明可直接比较全除子：$[a]$ 的核与 $[\delta]$ 的核相同，
$O$ 与两个 $x_\wp=0$ 的点是右侧的全部零；两者具有同一个
degree3 canonical 周期因子。商为常数，以首项 $az$ 定为 $a$。
因此没有另漏一个二次指数因子。

对一般 $t$，按 $s$ 变量的全除子、周期因子及 $s=0$ 的首项，
$$
\boxed{
\prod_{j=0}^2\sigma(s+\omega^jat)
=-\sigma(s)^3\sigma(at)^3
 \bigl(y_\wp(s)+y_\wp(at)\bigr).
}
\tag{22}
$$
三个零正是 $-at,-\omega at,-\omega^2at$，因为
$y_\wp(\omega z)=y_\wp(z)$。$y_\wp(s)=-s^{-3}+\cdots$
确定式中的负号；解析延拓付所有退化 $t$。
这给全函数身份，而非有限 Taylor 项检查。

用 R522 的同一个整卷积单位
$$
B_3(z)=-y_\wp(z)\sigma(z)^3
=\frac{\sigma(2z)}{2\sigma(z)},\qquad B_3(0)=1,
$$
则 (22) 也准确是
$$
\sigma(s)^3B_3(at)+B_3(s)\sigma(at)^3.
\tag{23}
$$
因此
$$
\boxed{
\Phi(s,t)=
-\frac{\omega^2}{84}\sigma(as)\sigma(3\delta t)\sigma(3t)
\left\{\sigma(s)^3B_3(at)+B_3(s)\sigma(at)^3\right\}.
}
\tag{24}
$$
共同的三个 sigma 因子原样保留。它们的质量并非单位，本篇没有
用 (24) 对未知中央作反卷积。

## 6. 四个归一整因子与恰二秩

定义
$$
\boxed{
\begin{aligned}
f_1(z)&=-x_\wp(z)y_\wp(z)\sigma(z)^6
       =\frac{\sigma(az)B_3(z)}a,\\
f_4(z)&=x_\wp(z)\sigma(z)^6
       =\frac{\sigma(az)\sigma(z)^3}a,\\
g_2(z)&=\frac{\sigma(3\delta z)\sigma(3z)B_3(az)}{9\delta},\\
g_5(z)&=-\frac{\sigma(3\delta z)\sigma(3z)\sigma(az)^3}{81}.
\end{aligned}}
\tag{25}
$$
它们分别始于 $z,z^4,z^2,z^5$，首系数全为 $1$。
每项是原 sigma 与整 $B_3$ 的实际卷积，所除固定常数在当前处
全为单位，故四条来源整。$f_1,f_4\in\mathcal S_6$，
$g_2,g_5\in\mathcal S_{45}^{\rm odd}$；相应核心是 (16) 的
$\beta$ 与 $\chi\lambda$。

由 $a^3=3\delta$ 及 $\omega^2a=-\delta$，(20)–(22) 得到完整恒等式
$$
\boxed{
\Phi(s,t)=
-\frac9{28}f_4(s)g_2(t)
-\frac{27\delta}{28}f_1(s)g_5(t).
}
\tag{26}
$$
两对因子的首阶不同，故张量秩严格为 $2$。
这里的二秩是这个实际二维来源的张量秩，不给新的曲线另作秩声明。

为保完全有理的原 theta 表达，令 $X=x_\wp^3$，
$$
P_9(X)=X^3-96bX^2+48b^2X+64b^3.
$$
经典原三倍加法可由曲线方程直接核为
$$
\sigma(3z)=3x_\wp(X+4b)\sigma(z)^9,\quad
x_\wp(3z)=\frac{P_9(X)}{9x_\wp^2(X+4b)^2},
$$
$$
y_\wp(az)=\frac{(X-8b)y_\wp(z)}{3\delta X}.
$$
代入 (25) 给
$$
\boxed{
\begin{aligned}
g_5&=\sigma^{45}x_\wp^5(X+4b)^2P_9(X),\\
g_2&=-\sigma^{45}x_\wp^2y_\wp(X-8b)(X+4b)^2P_9(X).
\end{aligned}}
\tag{27}
$$
所有潜在有理极点都已在全函数 (25) 中消去；(27) 是同一来源的
多项式表达，不是另选一个极点未付的函数。

四个因子的质量全为零，所以两个单轴边际全函数为零。
二维来源仍非零，且有两个明确的完整混合矩
$$
\boxed{
\int U^4V^2\,d\rho_0=-\frac{108}{7}\Omega^6,\qquad
\int UV^5\,d\rho_0=-\frac{810\delta}{7}\Omega^6.
}
\tag{28}
$$
它们由归一首项的 $4!2!$、$1!5!$ 直接得出。
相应单轴正矩还完整提取另一因子，例如
$$
(V)_*\left\{\frac{U}{\Omega}\,d\rho_0\right\}
=-\frac{27\delta}{28}\nu_{g_5},\qquad
(V)_*\left\{\frac{U^4}{24\Omega^4}\,d\rho_0\right\}
=-\frac9{28}\nu_{g_2}.
\tag{29}
$$
(29) 只忘去显示的输入；若另外限制原隐藏变量，须保其真实条件。

## 7. 原 S 行、K 单位逆及独立深度返回

由 (7)、(18)，原 $S$ 是这个同一来源的真实线性输出
$$
\boxed{
Y=\frac{-1+4\omega}{3}U+\frac23V.
}
\tag{30}
$$
所以把 (26) 限于
$s=(-1+4\omega)z/3,\ t=2z/3$，准确得到原 $S(z)$。
在普通测度端也相应得到同一个 $J_S(u)$，不是仅质量或首项匹配。

R529 的
$$
\widehat P_K(E,K)=\frac1{216b\Omega^6}
\sum_{j=0}^6\binom6j
 \frac{\eta^jE^{6-j}K^j}{1+\lambda\kappa^j},
\qquad\eta=\frac{2(1-\omega)}3
$$
保整个 $(J,A_5,B_2,C_{30})$ 推前：
$$
\boxed{
(J,A_5,B_2,C_{30})_*
 \{{\bf1}_{K\ {\rm unit}}\widehat P_K\,d\rho_0\}
=(J,A_5,B_2,C_{30})_*\rho_0.
}
\tag{31}
$$
再忘去 $B_2,C_{30}$ 后，确实就是 (26) 的二维来源。

更一般，固定非负 $(r,s,e,\ell,m)$，取真实域
$$
\mathcal R=
\{J\in p^r,\ A_5\in p^s,\ E\in p^e,\ 
  B_2\in p^\ell,\ C_{30}\in p^m,\ K\ {\rm unit}\}.
$$
在其真实像内使用
$$
J_r=J/\kappa^r,\quad A_s=A_5/\kappa^s,\quad
\widehat P_K(E/\kappa^e,K).
$$
由 (17)、(31)，完整 $(J_r,A_s)$ 推前为
$$
\boxed{
\beta^{r+e+\ell}(\chi\lambda)^{s+m}
 \,(J,A_5)_*\rho_0.
}
\tag{32}
$$
因此用整个
$$
Y_{r,s}=\frac{2(-1+4\omega)}3\,J/\kappa^r+2A_5/\kappa^s
$$
的单位 Mellin 权，准确返回
$\beta^{r+e+\ell}(\chi\lambda)^{s+m}J_S(u)$。
所有逆尺度都只用于其显示的实际深域。对 $h$ 同式另乘
$\omega^2$，因为 (6) 固定这两个输出。

## 8. 原五深事件、旧 W 和完整边界

令 $R_3=J+K=\xi_1+\omega^2\xi_3-c$。
$(R_3,Q_3,E)$ 在原 $(\xi_1,\xi_3,c)$ 上的行列式范数为 $9$；
(14) 的变换也在当前处可逆。因此原五深一单位事件严格为
$$
\boxed{
\mathcal D_n
=\{A_5,B_2,C_{30},E\in p^n,\ K\ {\rm unit},\
                                      J+K\in p^n\}.
}
\tag{33}
$$
原 $x=(K-J)/a$ 的单位条件由 (33) 自动恢复。
这里同时保四个伴随和第五条近相消关系。

其 R529 的 $J$ 深像准确是
$$
\boxed{
\mathcal D_{n,r}
=\{A_5,B_2,C_{30},E\in p^n,\ K\ {\rm unit},\
                         J/\kappa^r+K\in p^n\},
}
\tag{34}
$$
其中 $J\in p^r$ 且 $J/\kappa^r$ 为单位。
(34) 使用原未经丢弃的输入。R529 已付的非零局部积分仍用
$\widehat P_K(E,K)$ 与 $Y_{r,0}$，准确有赋值 $5n$。

若把 (32) 用于包含该域的整个深度矩形，测试却必须改成
$\widehat P_K(E/\kappa^n,K)$，第一权也必须用 $Y_{r,n}$。
这两个实际移动不能省略。因此不能从 (32) 直接给
R529 的受限非零积分赋零。

旧 $W$ 在同一完整框架中准确为
$$
\boxed{
\begin{aligned}
W={}&\frac{-5+\delta}{3}J
+\left(3+\frac\delta{15}\right)A_5
+\left(\frac13-\delta\right)K
+\left(-2+\frac{4\delta}{3}\right)E\\
&+\left(\frac12+\frac\delta6\right)B_2
+\left(\frac12+\frac\delta{30}\right)C_{30}.
\end{aligned}}
\tag{35}
$$
四个被忘去方向的系数均非零，所以 (26) 不能冒充保原 $T$
观察的二维联合。要与 $W$ 的原中央相比较，必须继续使用
(35) 及 R529 的完整两项补偿。

本篇付清的接口是同一六输入的 (16)–(17)、原两个输出的全局
sigma 恒等式 (24)–(27)、原 $S$ 的准确连接 (30) 和真实受限域
(33)–(35)。这些来源和条件已经可以共同使用；其补域仍须按实际
输出运输，尚不能删去。

## 精确证书与依赖

- [完整六轴、所有中心与恰二秩相位证书](../scripts/check-r532-original-j-a5-frame-and-rank-two-source.mjs)；
  [全部矩阵、逆、Gram、原输入条件与归一系数](../scripts/check-r532-original-j-a5-frame-and-rank-two-source.json)。
  同一 BigInt/CM 主体已在 V8 实际执行。检查包括全六维正交性、
  完整逆、(14) 的全部三输入、原 $\mathcal T$、两输出六 sigma 的
  完整首六阶相位及两个显示混合矩。全函数身份由 §5 的全除子、
  canonical 周期和首项证明，不以有限展开替代。
- [R529：原 J/K 小核与完整 carry](R529-original-low-j-k-core-and-complete-st-carry.md)。
- [R522：同一个 B3 与完整正六次身份](R522-common-degree3-even-factor-and-same-st-positive-test.md)。
- [R513：whole odd5 与 chi65 的真实识别](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)。
- [R504：原 odd65 的绝对平方](R504-original-two-axis65-core-and-complete-rectangles.md)。
- [R496：完整当前中心](R496-original-new-axis-even-core-and-four-source-group.md)。
