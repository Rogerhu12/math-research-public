# R310：真实秩零 H3 frame、固定第三类原函数与完整中央转置

日期：2026-11-13。**状态：以下真实有理商、全部二十四个简单极、十八个非挠极、规范第三类原函数、普通一阶 distribution 以及惰性完整移权和统一 Gauss 界均已证明。自然留数加权的椭圆对数行准确为零；原中央导数的跨素数非零仍未证明。**

R307 的 $F=\Theta^{17}$ 方便做有限代数约化，却不是该篇的原秩零 Hecke 来源。本篇改用 R307–308 已完整识别的真实 $H_3$。它的普通中央质量是单位，因此可以在同一原 Mellin 函数上作真正的参考商。以下始终保留 theta 乘子，绝不把 Mellin 商换成函数商的 Mellin。

## 1. 真正的参考商及全部极

固定
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad
dz=\frac{dx}{2y},\quad
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad\sigma=z+\cdots.
$$
写 $X=x^3$，并令
$$
\begin{aligned}
C_3(X)&=X^3-204bX^2-384b^2X+64b^3,\\
P_1(X)&=\frac17(X+b)(X-8b)(7X^2-4bX+16b^2),\\
P_3(X)&=(X-8b)(X+4b)C_3(X),\\
S&=\sigma^{34}x^2P_1(X),\qquad
H=\sigma^{34}x^2P_3(X).
\end{aligned}                                                   \tag{1}
$$
这里 $S$ 是原秩二曲线 $y^2=x^3+17$ 的首项一来源，$H=H_3$ 是 $y^2=x^3+17^3$ 在共同 $b=17$ frame 中的质量一来源：
$$
S=z^6+\cdots,\qquad H=1+\cdots.
$$
R306–308 已付全部局部 Schwartz、真实 Hecke 角色、周期、Euler 因子和 $L(E_{17^3},1)/\Omega_{17^3}=3$；本篇不重新选择一个候选参考。

准确的函数商是
$$
\boxed{
g:=\frac SH
=\frac{(X+b)(7X^2-4bX+16b^2)}
       {7(X+4b)C_3(X)}
=\frac1{28(X+4b)}
 +\frac{27X(X+4b)}{28C_3(X)}.}                              \tag{2}
$$
共同因子 $X-8b$ 已经且只已经在 (2) 中消去。其余分子、分母互素；分母有四个不同非零根，且没有根为 $-b$。因此
$$
\eta=g\,dz                                                   \tag{3}
$$
只有二十四个简单极：$x^3=-4b$ 的六点，以及 $C_3(x^3)=0$ 的十八点。它在 $O$ 正则并从 $z^6\,dz$ 开始，没有原点留数。

前六点是原 $E_b[3]\setminus\{O,(0,\sqrt b),(0,-\sqrt b)\}$，因为三除法多项式为 $3x(x^3+4b)$。后三组没有被当作挠点。

## 2. 十八个额外极确实全部非挠

令
$$
f(u)=u^3-204u^2-384u+64 .
$$
它模 $5$ 不可约，且
$$
\operatorname{disc}f=2^{12}3^9\cdot107.                     \tag{4}
$$
所以对每个根 $u$，$L_0=\mathbb Q(u)$ 是三次域，并在 $107$ 真分歧：多项式判别式在 $107$ 的赋值为一，整指数的平方不可能含有 $107$，故域判别式也含 $107$ 一次。

任取 $P=(a,y_0)$ 满足
$$
a^3=17u,\qquad y_0^2=17(u+1).
$$
其坐标域 $L=\mathbb Q(a,y_0)$ 含 $L_0$，且 $[L:\mathbb Q]\le18$。曲线 $E_{17}$ 在 $\ell=107$ 好超奇异，因为 $107\equiv2\pmod3$。

如果 $P$ 是挠点而阶含 $\ell$，则 $L$ 包含一个非零 $\ell$ 阶点。好超奇异曲线的 $\ell$ 阶点全在形式群中。其原整参数的 $[\ell](t)/t$ Newton 多边形从常数项赋值一到次数 $\ell^2-1$ 的单位项，所有非零 $\ell$ 阶参数都具有赋值 $1/(\ell^2-1)$。因此任一容纳该点的局部域，其分歧指数至少为 $\ell^2-1>18$，与全局次数界矛盾。

如果 $P$ 的阶与 $\ell$ 互素，好约化整模型上的该阶扭点群是有限 étale 的；故其坐标域在 $\ell$ 未分歧。它却含有在 $\ell$ 分歧的 $L_0$，仍矛盾。于是所有这十八个点均非挠。模五不可约性及三次 CM 作用也保证这里没有只排除某一个选定根。

同样的论证同时记录 R307 另一参考的真实边界：
$$
\begin{aligned}
P_5(X)&=(X-8b)
 (X^4+280bX^3+1968b^2X^2+832b^3X-128b^4),\\
f_5(u)&=u^4+280u^3+1968u^2+832u-128,\\
\operatorname{disc}f_5&=2^{24}3^{15}\cdot1427 .
\end{aligned}                                                \tag{5}
$$
$f_5$ 模 $11$ 不可约，$1427\equiv2\pmod3$，相应点的坐标次数至多二十四。因此这二十四个 $H_5$ 零点也全部非挠。后文的实际 frame 仍只用 $H=H_3$。

## 3. 固定第三类原函数及真实 monodromy

记
$$
D(X)=(X+4b)C_3(X),\qquad
N(X)=\frac17(X+b)(7X^2-4bX+16b^2).
$$
对 $D$ 的每个根 $r$，写
$$
A_r=\frac{N(r)}{D'(r)}.
$$
准确有
$$
A_{-4b}=\frac1{28},\qquad
A_r=\frac{27r(r+4b)}{28C_3'(r)}
       \quad(C_3(r)=0).                                    \tag{6}
$$
取 $r$ 的三个立方根 $a$，并对每个 $r$ 固定一个 $y_r$ 满足 $y_r^2=r+b$。令
$$
P_a=(a,y_r),\qquad
\varrho_a=\frac{A_r}{6a^2y_r}.
$$
共十二个这样的 $P_a$，其负点给其余十二个极。普通部分分式准确给
$$
g(x)=\sum_{r}\sum_{a^3=r}\frac{A_r}{3a^2(x-a)},\qquad
\operatorname{res}_{P_a}\eta=\varrho_a,\quad
\operatorname{res}_{-P_a}\eta=-\varrho_a.                    \tag{7}
$$
所有这些留数非零。

令 $\zeta=\sigma'/\sigma$。经典加法恒等式在当前 $x'=2y$ 规范中为
$$
\zeta(z-P)-\zeta(z+P)+2\zeta(P)
             =\frac{2y(P)}{x(z)-x(P)}.                     \tag{8}
$$
也可直接证明 (8)：两边是具有相同简单极、相同留数的椭圆函数，其差是常数；在 $z=0$ 处两边均为零。这里不能漏掉 $2\zeta(P)$。

因此唯一满足 $V(0)=0$、$V'=g$ 的原局部积分为
$$
\boxed{
V(z)=\sum_a\varrho_a
\log\left(
-\frac{\sigma(z-P_a)}{\sigma(z+P_a)}
                  e^{\,2\zeta(P_a)z}\right).}             \tag{9}
$$
每个对数括号在 $z=0$ 为一，按该点的形式对数定义。(8) 使其规范局部 germ 只依赖代数点的 $(x,y)$，不依赖为 $P_a$ 选择的复周期提升；同一形式展开可用于每个 $p$ 进嵌入。尤其 (9) 中的准对数常数和 $\sigma$ 比是一个整体，不能分开保留其中某项作为新的中央常数。

定义
$$
C=HV,\qquad
a=\frac{H'}H
 =34\zeta+\frac{4y}{x}
       +6x^2y\,\frac{P_3'(X)}{P_3(X)},\qquad
\nabla_H=\partial_z-a .
$$
则准确有
$$
\boxed{\nabla_H C=S,\qquad
V=z^7/7+\cdots,\qquad C=z^7/7+\cdots.}                     \tag{10}
$$
其中三项 $a$ 的原点负一次项完全抵消；$a$ 是原点的真实解析 germ。

$C$ 不被声称是全局全纯 theta 截面。在二十四个极附近，$V$ 有非零对数 monodromy；即使 $H$ 在该点有一个简单零，$C$ 的局部形状仍含非零的 $t\log t$，其 monodromy 是 $2\pi i\varrho_a H$，并不为零。若存在全局亚纯截面 $C_{\mathrm{rat}}$ 满足 (10)，则 $C_{\mathrm{rat}}/H$ 是椭圆有理函数，其微分不可能有 (7) 的非零留数。这也直接证明本次真实连接确实需要这个对数扩张。

## 4. 自然固定椭圆对数行准确为零

令 $\omega=(-1+\sqrt{-3})/2$。对固定 $r$，在 (7) 中取
$$
P_j=[\omega]^jP_0,\qquad
x(P_j)=\omega^j x(P_0),\qquad y(P_j)=y(P_0),\quad0\le j\le2.
$$
其真实留数为
$$
\varrho_j=\omega^j\varrho_0.                               \tag{11}
$$
任取一个 $p$ 进嵌入，用原微分 $dz$ 的椭圆对数。它在某个有限扩域上由形式群对数唯一延拓，杀掉挠点，并满足
$$
\log_{E,p}([\omega]P)=\omega\log_{E,p}(P).
$$
所以每个实际三次轨道都有
$$
\sum_{j=0}^2\varrho_j\log_{E,p}(P_j)
 =\varrho_0\log_{E,p}(P_0)\sum_{j=0}^2\omega^{2j}=0.
$$
负点同样成立；六个三挠点自身的对数已经为零。因此
$$
\boxed{\sum_{P\text{ 为 (3) 的极}}
\operatorname{res}_{P}(\eta)\,\log_{E,p}(P)=0.}             \tag{12}
$$
这是由真实留数和真实 CM 标签得到的准确取消，不是说这些非挠点的单个对数为零。

准对数的 CM 权不同。例如复 $\zeta(\omega P)=\omega^{-1}\zeta(P)$，于是同一三点的 $\varrho_j\zeta(P_j)$ 相加为 $3\varrho_0\zeta(P_0)$，没有 (12) 的取消。但它在 (9) 中伴随同一个 $\sigma$ 比；(12) 不允许单独删去剩下的完整对数来源。

## 5. 普通处：规范原函数是一阶 distribution

固定 $p>7$、$p\equiv1\pmod3$。沿 R295、R308 的同一个形式周期 $\Omega_p$ 和原整 Amice frame，写 $\nu_S,\nu_H$ 为原有界整测度。由 $H(0)=1$，其 Amice 级数是整形式单位，因此
$$
g\bigl(\Omega_p\log(1+Z)\bigr)
=\int_{\mathbb Z_p}(1+Z)^x\,d\nu_g(x)                     \tag{13}
$$
也给一个有界整测度。特别 $\nu_g(\mathbb Z_p)=g(0)=0$，且
$$
\boxed{\nu_S=\nu_H*\nu_g.}                                \tag{14}
$$
星号始终表示加法卷积。

不能只把 (9) 的积分称为有界测度。其正确规范是如下连续的一阶 distribution：对每个局部解析函数 $f$，定义
$$
\boxed{\eta_g(f)=\Omega_p
\int_{\mathbb Z_p}\frac{f(x)-f(0)}x\,d\nu_g(x),}            \tag{15}
$$
在 $x=0$ 处商按 $f'(0)$ 解释。该商在每个局部解析 Banach 空间上连续地依赖 $f$；离开零邻域只用有界的 $1/x$，在零邻域用一次差商。因此 (15) 是定义良好的 distribution。

它满足
$$
\eta_g(1)=0,\qquad x\eta_g=\Omega_p\nu_g.                   \tag{16}
$$
对 $(1+Z)^x$ 作测试，(16) 给
$$
(1+Z)\partial_Z\mathcal A_{\eta_g}(Z)
 =\Omega_p\mathcal A_{\nu_g}(Z),\qquad
\mathcal A_{\eta_g}(0)=0 .
$$
这正是 $V'=g,V(0)=0$ 换到原正式参数后的方程。因此
$$
\mathcal A_{\eta_g}(Z)=V(\Omega_p\log(1+Z)),\qquad
\nu_C:=\nu_H*\eta_g                                      \tag{17}
$$
是 (10) 中同一个 $C$ 的实际 distribution。该原函数没有逐层选解，也没有引入一个未记录的原点 Dirac 项。

$a=H'/H$ 的原 Amice 变换也整：$H$ 的整单位级数求 $(1+Z)\partial_Z$、除以同一单位，再乘 $\Omega_p^{-1}$ 即得。记其有界测度为 $\nu_a$。完整乘法规则于是给
$$
\boxed{\nu_S=\Omega_p^{-1}x\nu_C-\nu_a*\nu_C.}             \tag{18}
$$
这条式子是完整 distribution 等式，而非只在正权成立的矩等式。

## 6. 普通原参考商的完整中央转置

置 $d=p-1$，用 R307 的权变量规范
$$
\begin{aligned}
M_T(u)&=\nu_T\bigl(\mathbf1_{\mathbb Z_p^\times}
                               \langle x\rangle^{du}\bigr),\\
M_{C,1}(u)&=\nu_C\bigl(\mathbf1_{\mathbb Z_p^\times}
                    \tau_p(x)\langle x\rangle^{du}\bigr),\\
\mathcal K_{a,C}(u)&=(\nu_a*\nu_C)
                \bigl(\mathbf1_{\mathbb Z_p^\times}
                               \langle x\rangle^{du}\bigr).
\end{aligned}
$$
这些都是局部解析测试函数族，因而对 (15)、(17) 合法，并在 $u\in\mathbb Z_p$ 附近解析。由 (18)，
$$
\boxed{M_S(u)=\Omega_p^{-1}M_{C,1}(u+1/d)
                                      -\mathcal K_{a,C}(u).} \tag{19}
$$
原 tame-one 角色及 $1/d$ 移权都在 (19) 中。卷积项的测试变量是两变量之和，不能换成两个乘法 Mellin 函数的乘积。

R300 的原目标给 $M_S(0)=0$；R308 对真实 $E_{17^3}$ 给
$$
m_H:=M_H(0)=1-\bar\pi_3^{-1}\in\mathcal O^\times,
$$
其中 $\bar\pi_3$ 是参考曲线自己的 Frobenius 单位根。于是
$$
\mathscr Q_p(u)=\frac{M_S(u)}{M_H(u)}
$$
在中心附近解析，且准确有
$$
\boxed{
\mathscr Q_p'(0)=
\frac{\Omega_p^{-1}M_{C,1}'(1/d)-\mathcal K_{a,C}'(0)}
     {1-\bar\pi_3^{-1}}.}                                \tag{20}
$$
参考自身未知的斜率 $M_H'(0)$ 在这里确实消失，理由准确是原分子 $M_S(0)=0$。没有把它事先设成零。

使用 (14)，还得到完全等价的实际公式
$$
\boxed{
\mathscr Q_p'(0)=\frac d{1-\bar\pi_3^{-1}}
\iint_{\mathbb Z_p^2}
\mathbf1_{x+y\in\mathbb Z_p^\times}
 \log_p\langle x+y\rangle\,d\nu_H(x)d\nu_g(y).}             \tag{21}
$$
(21) 包含全部原 $p$ 环带及两单位相加后的消去区域。R308 的原参考周期、扭曲根单位和 Euler 均已通过 $\nu_H$ 与 $m_H$ 保留。式 (2) 是 (21) 中 $\nu_g$ 的准确代数输入；它不是 $\mathscr Q_p$ 本身的 Amice 变换。

## 7. 惰性 primitive 的统一积分分母界

固定 $p\ge11$、$p\equiv5\pmod6$、$p\ne17$，令
$$
d=p+1,\qquad R_E=p^{-1/(p^2-1)},\qquad R=p^{-1/(2p)}.
$$
在原点取 $t=x^{-1/2}=z+\cdots$。R301 的高度二估计经 $b=17$ 的单位缩放给：对每个 $R'<R_E$，$t/z$ 和其逆都实际解析、Gauss 范数一。式 (2) 在该正式参数中准确为
$$
g=
t^6\frac{(1+bt^6)(7-4bt^6+16b^2t^{12})}
 {7(1+4bt^6)(1-204bt^6-384b^2t^{12}+64b^3t^{18})}.         \tag{22}
$$
除 $t^6$ 外是整解析单位。因此若 $g=\sum g_nz^n$，则 $g_n=0$ 除非 $n\ge6$、$6\mid n$，并有
$$
\boxed{v_p(g_n)\ge
\left\lceil\frac{6-n}{p^2-1}\right\rceil.}                 \tag{23}
$$
这是先在全部 $R'<R_E$ 得到 $\|g\|_{R'}\le(R')^6$，再逐系数取极限所得。

现在
$$
\frac{V}{z}=\sum_{\substack{n\ge6\\6\mid n}}
                      \frac{g_n}{n+1}z^n.
$$
我们证明每项在半径 $R$ 的加权赋值至少 $3/p$，从而
$$
\boxed{\|V/z\|_R\le R^6.}                                \tag{24}
$$
不能仅从 $\|g\|_R\le R^6$ 省掉积分分母。

当 $n<p^2-1$，(23) 使 $g_n$ 整。若 $p\nmid n+1$，加权赋值至少 $n/(2p)\ge3/p$。若 $p\mid n+1$，此处只有一个 $p$；由 $n\equiv0\pmod6$、$p\equiv-1\pmod6$ 得 $n+1\ge5p$。故加权赋值至少
$$
\frac{5p-1}{2p}-1>\frac3p.
$$
当 $n\ge p^2-1$，写 $j=\lfloor\log_p(n+1)\rfloor\ge2$。用 $v_p(n+1)\le j$ 及 (23)，加权赋值至少
$$
(p^j-1)\left(\frac1{2p}-\frac1{p^2-1}\right)
             +\frac6{p^2-1}-j.                           \tag{25}
$$
$j=2$ 时为
$$
\frac p2-3-\frac1{2p}+\frac6{p^2-1}>\frac3p
             \qquad(p\ge11).
$$
以后 $j$ 每增加一，(25) 的增加量是
$(p-1)p^j(1/(2p)-1/(p^2-1))-1>0$，且趋于无穷。这同时证明所需收敛和 (24)。

## 8. 惰性原参考商及完整负移权

沿 R301、R308 的同一个原 sigma Gaussian，置
$$
c=[z^d]\log(\sigma/z),\qquad \kappa=34c,\qquad v_p(c)=-1,
$$
$$
\widehat H=e^{-\kappa z^d}H,\quad
U=\frac Cz=H\frac Vz,\quad
\widehat U=e^{-\kappa z^d}U,\quad
\widehat W=z\frac{\widehat H'}{\widehat H}.
$$
这里删去指数首先是形式操作；其实际解析表达使用 R301 的 sigma 余项。由 (1) 的首一多项式、$t/z$ 的单位界及 R301 的指数余项，
$$
\|\widehat H\|_R=\|\widehat H^{-1}\|_R=1,\qquad
\|\widehat U\|_R\le R^6,\qquad \|\widehat W\|_R\le1 .
$$
$\widehat W$ 从六次项开始；$\widehat W\widehat U$ 也满足范数至多 $R^6$。

对这些同 charge $34$ 的真实来源，定义
$$
\mathcal J_T(u)=
\sum_{h\ge0}[z^{dh}](e^{-\kappa z^d}T)\,
                         \kappa^{-h}(u)_h.               \tag{26}
$$
(24) 给 $\mathcal J_U,\mathcal J_{\widehat W U}$ 与 R301 原目标同样的系数界
$$
v_p\left([z^{dh}](e^{-\kappa z^d}T)\kappa^{-h}\right)
\ge \left\lceil\frac{h(p-1)+6}{2p}\right\rceil.
$$
两者在包含 $\mathbb Z_p$ 的同一个圆盘解析，且中心质量为零。R308 另给 $\mathcal J_H(0)=1$ 及实际单位参考。

令 $D_z=z\partial_z$。由 (10)，在未删除原 Gaussian 前准确有
$$
S=(D_z+1-zH'/H)U,\qquad zH'/H=\kappa d z^d+\widehat W.
$$
完整 Newton 转置
$$
\mathcal J_{D_zT}(u)=du\,\mathcal J_T(u),\qquad
\mathcal J_{z^dT}(u)=\kappa^{-1}u\,\mathcal J_T(u-1)
$$
于是给
$$
\boxed{\mathcal J_S(u)
=(du+1)\mathcal J_U(u)
 -du\,\mathcal J_U(u-1)-\mathcal J_{\widehat W U}(u).}       \tag{27}
$$
这些等式可先在非负整数 $u$ 用有限系数卷积证明，再用解析性；也可逐个 Newton 基验证。$\widehat W U$ 始终作为实际完整乘积进入 (26)。

原参考商 $\mathcal J_S/\mathcal J_H$ 的中央斜率因此准确为
$$
\boxed{
\left(\frac{\mathcal J_S}{\mathcal J_H}\right)'(0)
=\mathcal J_S'(0)
=\mathcal J_U'(0)-d\mathcal J_U(-1)
                     -\mathcal J_{\widehat W U}'(0).}      \tag{28}
$$
这里用到了 $\mathcal J_U(0)=0$；负权 $-1$、整个连接乘积和真实 Gaussian 都保留。与普通式 (20) 相同，参考自身的未知导数因原目标质量零而消失。

## 9. 所得到的实际接口

(20)、(21)、(28) 是用真实秩零 $H_3$ 归一后的完整中央等式，已去掉参考自身的未知斜率。其新输入是固定的二十四极第三类微分和唯一规范原函数 (9)、(15)，不是仅有同次数的形式 companion。

这些等式尚不把中央斜率算成固定椭圆对数的非零组合。真实自然留数行恰被 (12) 消掉；准对数项必须与 (9) 的非恒定部分共同运输，普通卷积或惰性负移权仍在。后续若使用 Cartier、Frobenius 或新分布关系，需要作用于 (20)/(28) 中同一带 $H_3$ 乘子的对象。

生产证书为 [check-jzero-rankzero-frame-third-kind-and-mellin.py](../scripts/check-jzero-rankzero-frame-third-kind-and-mellin.py) 及其 JSON，精确记录原多项式、部分分式、全部极、两个非挠证书的不可约性与判别式及 CM 留数权。统一分母界、distribution 连续性和完整解析转置由上文证明，未用有限目标素数枚举替代。

直接依赖：
[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、
[R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R306](R306-jzero-three-sextic-original-local-data-and-full-weight-squares.md)、
[R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)、
[R308](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)。
