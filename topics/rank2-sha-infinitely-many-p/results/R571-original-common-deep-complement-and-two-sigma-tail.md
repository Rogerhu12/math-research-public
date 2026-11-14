# R571 — 原算术补域的全部共同深度、双 sigma 消元与真实首层

日期：2026-11-14。**状态：已证明。**

本篇直接计算 R556 (16)、R567 (34) 中的整个原补项
$\int_{c,d_0\in p}q\ell\,d\rho_0$，并支付任意共同深度 $m$。
原 carry 深度 $n$、$\kappa^{-n}$、完整多项式、两个 Mellin 单位条件
及纯 $C$ 三分支全部保持。结果包括 $m>n$ 的真正尾部；
它没有把 native 残差认成完整算术总行。

两个原 sigma 输入的精确积分使首项降为同一个四 sigma 来源上的
$\partial_D\widehat P_p/A_*$。该积分尚未被赋非零。
末节把它与 R567 的两个完整 strip 和仍保留的整个 $u$ 单位补项合在一起，
给出准确的全算术首层。

## 1. 同一原测试与完整来源

沿用 [R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)、
[R556](R556-native-mixed-carry-odd37-cores-and-complete-residual.md)、
[R567](R567-native-both-strips-and-exact-five-sigma-normal-jets.md)、
[R568](R568-original-positive-strip-full-cores-and-native-transport.md)
的同一普通射线和全部固定坏集，不再细分射线。记
$$
b=17,\quad \omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1.
\tag{1}
$$
以下把最后一个原输入 $d_0$ 简写成 $d$。原输入仍为
$(\xi_1,\xi_2,\xi_3,x,c,d)$，且
$$
\rho_0=-\nu_\sigma^{\otimes6}/84,\qquad
\mu_0=\mathcal P_C\rho_0
=\nu_4\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),\qquad
\nu_4=-\mathcal P_C\nu_\sigma^{\otimes4}/84.
\tag{2}
$$
$\mathcal P_C$ 只操作前四个真实输入。

令 $q_n=\mathfrak q_{n,p}$ 为 R536 的原三分支平均，包含
$1_{\Gamma_{n,j}}$、$\kappa^{-n}$ 及同一个准确六次
$\widehat P_p=\mathcal R_pP_p$。再令
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
          -1_{W\ {\rm unit}}\log\langle W\rangle\},
\qquad a_n=q_n\ell .
\tag{3}
$$
本篇要计算的是全部真实共同深补项
$$
I_{n,m}=\int_{\{c,d\in p^m\}}a_n\,d\rho_0,\qquad n,m\ge1.
\tag{4}
$$
它是整个原六输入域上的积分，不添加 $u$、$L$ 或其他 unit cut。

## 2. 完整三轴与保持的三个伴随

使用原行
$$
\begin{gathered}
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\qquad
C=(\xi_1-\xi_3+x)/\delta,\\
H_1=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x,\qquad
a=2+3\omega,\quad l=1+3\omega,\quad g=3-2\omega,\\
D=D_4+c+ad,\qquad E=D+14C,\qquad G=13H_1+g(D+C),\\
A=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\qquad
Y=A+c+2d,\quad W=A+3\delta c+4d .
\end{gathered}
\tag{5}
$$
在原前四输入内定义
$$
\boxed{
\begin{aligned}
C_*&=C+D_4/6,&H_*&=H_1+gD_4/6,\\
E_*&=14C_*,&G_*&=13H_*+gC_*,\\
A_*&=A-\frac{1+6\omega}{6}D_4 .
\end{aligned}}
\tag{6}
$$
它们均与 $D_4,c,d$ 正交，并完全不含 $c,d$。令
$$
B=c+ad,\quad e=-4D_4/3+B,\quad h_0=(1+6\omega)/6,
$$
$$
y=h_0D_4+c+2d,\qquad w=h_0D_4+3\delta c+4d,\qquad
L=lc+d.
$$
则准确有
$$
\boxed{
E=E_*+e,\quad G=G_*+ge,\quad
Y=A_*+y,\quad W=A_*+w,\quad w-y=2L.
}
\tag{7}
$$
$e,y,w,L$ 都与 $D$ 正交。完整六行框架
$(D_4,c,d,E_*,G_*,A_*)$ 的行列式和范数为
$$
\det=-2821-273\delta,\qquad
N(\det)=8181628=2^2\,7^2\,13^3\,19.
\tag{8}
$$
因此原 $p\ge71$ 处整格可分，没有隐藏的格指数损失。
(8) 不要求把后三个伴随互相认成独立测度。

### 2.1 两套全来源矩形

第一套正是 R568 已付的
$$
X=c-D/14,\quad Z=d+lD/14,\quad
P=\frac{\omega}{2}\{X-(2+\omega)Z\},\quad
Z_*=Z-\frac{8+3\omega}{10}P.
\tag{9}
$$
$D,P,Z_*$ 正交。whole $140/60$ 的两次真实来源作用
$(-\chi\lambda R_1)^2=\lambda^2I$ 给
$$
\mu_0|_{\{D\in p^n,\ P,Z_*\in p^m\}}
=\beta^n\lambda^{2m}
(P_{D,\kappa^n}P_{P,\kappa^m}P_{Z_*,\kappa^m})_*\mu_0 .
\tag{10}
$$
这里使用原两态，没有把该身份延到新的第三态。

第二套是 $D_4,c,d$。它们两两正交，范数为 $6,1,1$。
完整 $C$ 共轭下的三个 $D_4$ 行在前四输入上分别为
$$
(1,\omega^2,-2\omega,0),\quad
(-\omega,\omega^2,1-\omega,\omega^2),\quad
(1-\omega,\omega^2,-\omega,-\omega).
\tag{11}
$$
三个标准半特征均为 even（非零 mod $2$ 系数数目为 $2,4,4$）。
R533 §3、R562 §1 的 **entire even $\mathcal S_6$** 实际核心为
$\beta$，所以它逐伴随系数作用于 (11) 的全部来源。
这不是仅由 R569 的 $D_4$ 边际推出。
又因 $\mathcal P_C$ 固定 $c,d$，原两个 sigma 核保持全部伴随，故
$$
\boxed{
\mu_0|_{\{D_4\in p^n,\ c,d\in p^m\}}
=\beta^{n+2m}
(P_{D_4,\kappa^n}P_{c,\kappa^m}P_{d,\kappa^m})_*\mu_0 .
}
\tag{12}
$$

## 3. 一个固定的双参数全测试

以下 $\widehat P_p$ 的原 $u_j=(1+\lambda\kappa^j)^{-1}$、
全部七行右逆和 $p$ 依赖始终固定。
引入变量 $s,t$ 不会把其中的 $\kappa$ 换成 $s$ 或 $t$。

对 $s\in p\mathcal O,\ t\in\mathcal O$，定义
$$
\boxed{
\begin{aligned}
\mathscr H(s,t)=
\int_{\{E_*,A_*\ {\rm unit}\}}
&\widehat P_p\bigl(D_4+tB,\
 E_*+s(-4D_4/3+tB),\
 G_*+gs(-4D_4/3+tB)\bigr)\\
&\cdot d_p\log
\frac{A_*+s(h_0D_4+t(c+2d))}
     {A_*+s(h_0D_4+t(3\delta c+4d))}
\,d\mu_0 .
\end{aligned}}
\tag{13}
$$
两个 log 参数均为单位；比值属于 $1+p\mathcal O$。
所以 (13) 是原两个单位 log 的准确差，不漏固定尺度 log。
原 $E$ 条件准确成为 $E_*$ unit，两个 Mellin 条件同时准确成为
$A_*$ unit。这些真实条件没有被丢弃。

**定理 1（所有共同深度）。** 对任意 $n,m\ge1$，令
$$
s_{n,m}=\kappa^{\min(n,m)},\qquad
t_{n,m}=\kappa^{(m-n)_+}.
$$
则
$$
\boxed{
I_{n,m}=\frac{\beta^n\lambda^{2m}}{b\Omega^6}\,
          \mathscr H(s_{n,m},t_{n,m}).
}
\tag{14}
$$

**证明。** 纯 $C$ 旋转固定 $\ell,c,d$；三分支平均在该全域上的
积分，准确等于单支在 $\mu_0$ 上的积分。因此 (4) 等于
$$
\frac1{b\Omega^6}
\int_{\{D\in p^n,\ E\ {\rm unit},\ c,d\in p^m\}}
\widehat P_p(D/\kappa^n,E,G)\ell\,d\mu_0 .
\tag{15}
$$
此处 $C,F$ unit 与 $D\in p^n,E$ unit 的等价正是原 carry 身份。

若 $m\le n$，在 $D\in p^n$ 内，
$c,d\in p^m$ 等价于 $X,Z\in p^m$，再等价于 $P,Z_*\in p^m$；
(9) 的二维行列式是 $\omega/2$，为单位。
应用 (10)。$D/\kappa^n$ 回到原 $D=D_4+B$，
而 (7) 中的 $e,y,w$ 同时乘 $\kappa^m$；
$E_*,G_*,A_*$ 固定。这正给 (13) 的 $(s,t)=(\kappa^m,1)$，
且给原显示的两个单位条件。

若 $m\ge n$，在 $c,d\in p^m$ 内，
$D\in p^n$ 等价于 $D_4\in p^n$。应用 (12)：
$$
D/\kappa^n\longmapsto D_4+\kappa^{m-n}B,
$$
$$
E\longmapsto E_*+\kappa^n(-4D_4/3+\kappa^{m-n}B),
$$
$G,Y,W$ 同样逐项成为 (13)。外部
$\beta^{n+2m}=\beta^n\lambda^{2m}$。两种情况在 $m=n$ 完全一致。
这证明 (14)，包括原 carry 深度以后的真正尾部。证毕。

## 4. 两个原 sigma 的精确首项

原 sigma 满足
$$
m_0=0,\quad m_1=\Omega,\quad m_2=\cdots=m_6=0,\qquad
m_7=24b\Omega^7 .
\tag{16}
$$
对任意次数不超过六的多项式 $Q(T)$，逐单项式有
$$
\boxed{
\int L\,Q(D_4+t(c+ad))\,d\nu_\sigma(c)d\nu_\sigma(d)
=-6t\Omega^2 Q'(D_4).
}
\tag{17}
$$
确切地，左侧每个多项式的 $c,d$ 总次数至多七；
两输入的质量为零，所以唯一可能的非零矩是 $(1,1)$。
$L(D_4+tB)^k$ 的 $cd$ 系数为
$$
ktD_4^{k-1}(1+la)=-6ktD_4^{k-1},
\qquad la=(1+3\omega)(2+3\omega)=-7.
$$
因此 (17) 是全部六次多项式上的精确身份。
它没有漏掉第七矩：$(7,1)$ 或 $(1,7)$ 要求总次数八，
从下一阶才可能出现；不能将 (17) 无条件延到更高次数。

定义同一个原四输入积分
$$
\boxed{
K_1=
12d_p\Omega^2
\int_{\{E_*,A_*\ {\rm unit}\}}
\frac{\partial_1\widehat P_p(D_4,E_*,G_*)}{A_*}\,d\nu_4
\ \in\mathcal O .
}
\tag{18}
$$
域完全不含 $c,d$，故可合法使用 (17)。
(13) 的 log 一阶为 $-2d_pstL/A_*$，
而其零阶为零。因此
$$
[s]\mathscr H(s,t)=t^2K_1 .
\tag{19}
$$

**定理 2（统一整尾）。** 对 $s\in p\mathcal O,t\in\mathcal O$，
$$
\boxed{\mathscr H(s,t)=st^2K_1+s^2t^2R(s,t),\qquad R(s,t)\in\mathcal O.}
\tag{20}
$$
这里 $R$ 表示在这些实际取值上的有界整函数；
不声称去掉 $s$ 的收敛权后所有形式 log 系数本来就整。

**证明。** 逐 $s$ 次数展开 (13)，每一系数是有限多项式积分，
log 第 $r$ 项唯一可能的分母为 $r$。
所有 $c,d$ 的出现均带一个 $t$。
两原 sigma 各自零质量，故总 $c,d$ 次数小于二的项全部消失；
所以每一系数均有 $t^2$。
一阶由 (17)–(19) 给出。其余 $r\ge2$ 的项在除去 $s^2t^2$ 后
由 $s^{r-2}/r$ 控制（多项式部分只增加非负 $s$ 次数）。
$p\ge71$ 且 $v_p(s)\ge1$，故这些值整并随次数趋向零。
原来源有界且 $\widehat P_p$ 整，允许逐项积分。证毕。

若把 (18) 沿完整 $D_4$ theta 基再展开，次数五的项因
$\mathcal S_6$ 没有 type $5$ 而整条消失；
剩余实际条件系数仍带 $E_*,A_*$ unit 及 $G_*$。
未加权 $D_4$ 边际为 $f_4$ 不允许删掉这些条件系数。

## 5. 原 carry 前后两种深度及整个环带

置
$$
a_{n,m}=m+(m-n)_+.
$$
由 (14)、(20) 严格得到
$$
\boxed{
I_{n,m}=
\frac{\beta^n\lambda^{2m}}{b\Omega^6}
\left\{\kappa^{a_{n,m}}K_1+p^{2m}\mathcal O\right\},
\qquad v_p(I_{n,m})\ge a_{n,m}.
}
\tag{21}
$$
这里 $p^{2m}\mathcal O$ 是原系数环中的误差理想。
因为
$s^2t^2=\kappa^{2m}$，这个尾界在两种范围内相同：
首项深度在 $m\le n$ 时为 $m$，在 $m\ge n$ 时为 $2m-n$。
如果 $K_1$ 是单位，(21) 的下界就是等号；
本篇不赋 $K_1$ 单位或非零。

整个共同深环带
$\{c,d\in p^m\}\setminus\{c,d\in p^{m+1}\}$ 的积分是
$I_{n,m}-I_{n,m+1}$，准确满足
$$
\boxed{
\frac{\beta^n\lambda^{2m}}{b\Omega^6}
\left\{
\kappa^{a_{n,m}}
(1-\lambda^2\kappa^{a_{n,m+1}-a_{n,m}})K_1
+p^{2m}\mathcal O
\right\}.
}
\tag{22}
$$
差指数在 $m<n$ 时为一，在 $m\ge n$ 时为二，均给一个单位括号。
固定 $n$ 后，(21) 还给 $m\to\infty$ 的真实尾部趋零。
所有这些都是同一个原 $q_n$ 的域分解，没有将不同 $q_n$ 的零值互换。

## 6. 回到完整原算术总行

保 R567 的原记号
$$
\mathcal N_n=\int_{\{u\in p,L\ {\rm unit}\}}
(a_n-a_n\circ R_c)\,d\Delta,\qquad
U_n=\int_{\{u\ {\rm unit}\}}
(a_n-a_n\circ R_c)\,d\Delta .
$$
则整个总行是
$$
\boxed{
3\beta^n(J'_S-6\delta J'_T)=\mathcal N_n+U_n+3I_{n,1}.
}
\tag{23}
$$
由于 (3) 的两个原 log 均在 $p\mathcal O$，有 $U_n\in p\mathcal O$。
由 (14) 的 $m=1$ 特例，完整第三项准确为
$$
\boxed{
3I_{n,1}=\frac{3\beta^n\lambda^2}{b\Omega^6}
                  \mathscr H(\kappa,1).
}
\tag{24}
$$
它没有因原 sigma 零质量消失，而是有 (18) 的实际一阶。

将 R567 原 $C_0\in p\mathcal O,C_1\in\mathcal O$ 代回，有
$$
\boxed{
\frac{3b\Omega^6}{p}(J'_S-6\delta J'_T)
\equiv
\beta\left(\frac{C_0}{p}+\lambda^2C_1\right)
+3\lambda^4K_1
+\frac{b\Omega^6}{p\beta^n}U_n
\pmod p .
}
\tag{25}
$$
这是包含两个完整补域的首层，不是局部残差判据。
其中 $C_0/p$ 的原 log 质量、$K_1$ 的全部条件测试和整个
$U_n$ 都必须保留。

(23)、R567 的完整条带公式和 (24) 还表明
$\beta^{-n}U_n$ 对所有 $n\ge1$ 准确相同。
所以单纯增加 carry 深度 $n$ 不提供一列新的独立算术零式。
要由 (25) 排除两原中央同时为零，仍须计算或控制这个完整单位补项，
或证明原指定负矩的合法非消失；这里没有完成无穷素数主目标。

## 精确证书

- [check-r571-original-common-deep-complement-and-two-sigma-tail.js](../scripts/check-r571-original-common-deep-complement-and-two-sigma-tail.js)
- [check-r571-original-common-deep-complement-and-two-sigma-tail.json](../scripts/check-r571-original-common-deep-complement-and-two-sigma-tail.json)

脚本在 $\mathbf Q(\delta)$ 中用 BigInt 有理运算核定 (5)–(11)
的完整行、正交关系、框架行列式及 (17) 的固定系数。
全部深度的域等价、整尾及完整算术身份由正文支付；
没有以有限素数样本、边际非零或辅助来源替代原全域。
