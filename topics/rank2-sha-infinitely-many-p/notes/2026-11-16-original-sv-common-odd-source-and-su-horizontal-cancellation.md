# 原 S/V 的同一五输入奇来源与 S/U 的准确水平抵消

日期：2026-11-16。**本注证明原 S/V 的完整单输入 [3] 替换、同一个固定 degree30 水平函数对两条指定除 p 行的全卷积表达，以及原 U−S(2z)/64 在同一 degree136 水平空间中恰六阶为零。它没有证明两条或四条首必要行不能同时为零。**

全部来源仍是 [R855](../results/R855-original-full-heat-connection-and-canonical-divided-jet.md)、[R856](../results/R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md) 及 [R812](../results/R812-original-same-charge-cancellation-and-complete-source-budget.md) 的原来源。水平规范取[固定代数水平格](2026-11-16-algebraic-horizontal-theta-frame-and-original-divided-rows.md)，半长 Bol 的一般恒等式取[原半长 Bol 与 CM 留数](2026-11-16-original-half-bol-and-cm-divided-residue.md)。下文显示 R812 的完整多项式来源，不依赖删去的数值文件。

## 1. 同一五因子与真正的单输入 [3]

保持
$$
y^2=x^3+b,\quad D_zx=2y,\quad
X=x^3,\quad \delta^2=-3,\quad \gamma=3+\omega,\quad N\gamma=7.
$$
原精确恒等式
$$
\sigma(\delta z)=\delta x\sigma^3,\qquad
\sigma(2z)=-2y\sigma^4,\qquad
\frac{\sigma(\gamma z)\sigma(\bar\gamma z)}{\sigma^{14}}
=7X^2-4bX+16b^2
\tag{1}
$$
给出一个固定奇来源
$$
\boxed{
C_{30}(z)=
-\frac{\sigma(\gamma z)\sigma(\bar\gamma z)
\sigma(z)\sigma(\delta z)\sigma(2\delta z)}{42}
=-\frac{\sigma^{30}x^2y(X-8b)(7X^2-4bX+16b^2)}7.
}
\tag{2}
$$
右端是原 whole $\mathscr V_{30}$ 的实际多项式，极阶 $25$。
因此
$$
C_{30}(z)=z^5+O(z^{11}),\qquad
C_{30}(\zeta z)=\zeta^5C_{30}(z)\quad(\zeta\in\mu_6).
\tag{3}
$$
(2)的第二式可直接用
$\sigma(2\delta z)=-2\delta xy(X-8b)\sigma^{12}$
验证，因而五因子的绝对倍率也已付清。

原 $S,V$ 准确是
$$
\boxed{
S=C_{30}(z)\frac{\sigma(2z)}2,\qquad
V=C_{30}(z)\frac{\sigma(6z)}6.
}
\tag{4}
$$
证明第二式无需认任何新 Hecke 行。由(1)，
$$
\Theta(z)\Theta(\delta z)=\frac{\sigma(3z)}{3\sigma(z)},
$$
而 R855 的原伙伴身份是
$V=S\Theta(2z)\Theta(2\delta z)$，故
$$
\boxed{V=S\,\frac{\sigma(6z)}{3\sigma(2z)}.}
\tag{5}
$$
这里是原最后一个 sigma 输入的整数 $[3]$ 替换，degree 为 $9$；
它等于 $-[\delta]^2$，不是一次 norm3 的 $\delta$ 返回。
其余五个实际输入逐个不动。原中央条件并没有因此自动传到任意别的输入倍率。

作为首阶核对，$\sigma(z)/z=1+bz^6/210+\cdots$ 给
$$
V-S=\frac{3328}{15}b\,z^{12}+O(z^{18}).
\tag{6}
$$
这只是两原来源的真实差，不把不同 theta degree 的差误当成单一 whole degree66 来源。

## 2. 同一个固定代数奇函数

在原参数点
$$
P:(g_2,g_3)=(0,-4b)
$$
取(2)的唯一水平延拓 $C_{30}^\flat$；必要时把 degree30 的已付水平基一次性加入固定参数覆盖。定义
$$
\boxed{g=D_zC_{30}^\flat(0).}
\tag{7}
$$
即 $g=j_{30,1}(C_{30}^\flat)$。它是固定代数函数，先于 $p$ 定义。
以下参数导子仍记 $L=L_2$，不得与物理 $D_z$ 混用。

从原热方程定义完整奇 jet 标量算子
$$
\mathscr U_0=1,\qquad \mathscr U_{-1}=0,\qquad
\boxed{
\mathscr U_{r+1}
=L\mathscr U_r-\frac{r(2r+1)}{24}g_2\mathscr U_{r-1}.
}
\tag{8}
$$
对任一水平 degree $d$ 奇截面 $F$，逐阶有
$$
j_{d,2r+1}(F)=(2d)^r\mathscr U_rj_{d,1}(F).
\tag{9}
$$
这是 R855(18)在奇指标上的准确归纳，不是删去 $g_2$ 的冻结矩阵。
例如
$$
\mathscr U_1=L,\qquad
\mathscr U_2=L^2-g_2/8,\qquad
\mathscr U_3=L^3-\frac{13g_2}{24}L-\frac{3g_3}{4}.
\tag{10}
$$
sigma 本身满足原 $Q_1\sigma=0$、$\sigma'(0)=1$，故同时有
$$
\boxed{
j_{2r+1}(C_{30})=60^r(\mathscr U_rg)(P),\qquad
j_{2r+1}(\sigma)=2^r(\mathscr U_r1)(P).
}
\tag{11}
$$
(11)的第一式保(2)的整个原纤维；第二式保原 sigma 的整个规范与 Frobenius 初始资料。没有把 sigma 系数换成任意形式解。

由(3)和(8)–(11)，
$$
\boxed{g(P)=Lg(P)=0,\qquad L^2g(P)=\frac{120}{60^2}=\frac1{30}.}
\tag{12}
$$
因此 $g$ 在固定参数覆盖的该点恰二阶为零。
角型还准确给
$$
(\mathscr U_rg)(P)=0\quad(r\not\equiv2\bmod3),\qquad
(\mathscr U_r1)(P)=0\quad(r\not\equiv0\bmod3).
\tag{13}
$$
这里的零是同一原 CM 纤维上的物理 jet 零；不能将(13)作为全参数零式求导。

## 3. whole 奇部分的第 p 阶 canonical 行

固定原惰性 $p=6s-1>211$ 及原坏集，置
$$
n=(p-1)/2=3s-1.
$$
R856 的完整 whole 恒等式在 $k=0$ 给
$$
j_{d,p}(R)\equiv H(P)j_{d,1}(R)=0\pmod p
\tag{14}
$$
对任意固定正偶数 $d$、$p\nmid6d$ 的原整格成立。因此
$$
\boxed{
\mathfrak O_{d,p}(\bar R)=j_{d,p}(R)/p\pmod p
}
\tag{15}
$$
在同一 CM 模型的整个 $\mathscr V_d/p\mathscr V_d$ 上与提升无关。
若换 $R$ 为 $R+pQ$，差正是 $j_{d,p}(Q)\equiv0$。
偶截面的此行恒为零；本注只把它用于(2)的真实奇截面。
这与 R855 第 $p+1$ 行必须限制到准确中心零格的范围不同。

对本来源，
$$
\boxed{
\mathfrak O_{30,p}
=60^n\,\frac{(\mathscr U_ng)(P)}p\pmod p.
}
\tag{16}
$$
其点上整性来自(14)，不从“$g$ 二阶为零”泛化给任意函数。

## 4. S/V 两条原 B 行的同一完整有限多项式

对本节仅用的两个固定整数 $c=2,6$，写
$$
A_c(z)=C_{30}(z)\frac{\sigma(cz)}c;
\qquad A_2=S,\ A_6=V.
$$
整 Leibniz 式是
$$
j_{p+1}(A_c)=
\sum_{r=0}^{n}\binom{p+1}{2r+1}
60^r(2c^2)^{\,n-r}
(\mathscr U_rg)(P)(\mathscr U_{n-r}1)(P).
\tag{17}
$$
$r=0$ 项因 $g(P)=0$ 准确为零；
$r=n$ 项为 $(p+1)j_p(C_{30})$，由(14)被 $p$ 整除。
其余 binomial 系数均被 $p$ 整除，且
$$
\frac1p\binom{p+1}{2r+1}
\equiv-\frac1{2r(2r+1)}\pmod p.
\tag{18}
$$
所以(17)也独立验证两个原偶来源的除 $p$ 整性，且完整保留其共同高阶项。

定义下列**实际有限多项式**，不是自由选择的系数池：
$$
\boxed{
\mathcal P_p(X)=
\sum_{k=1}^{s-1}
\frac{
(\mathscr U_{n-3k}g)(P)
(\mathscr U_{3k}1)(P)
}{6k(6k+1)}X^k\in k[X].
}
\tag{19}
$$
由(13)，(17)所有中间非零项恰对应 $r=n-3k$；
此时
$2r(2r+1)\equiv6k(6k+1)$。因而原两行准确为
$$
\boxed{
\begin{aligned}
\mathfrak B_S&=\mathfrak O_{30,p}
-60^n\,\mathcal P_p\!\left((2/15)^3\right),\\
\mathfrak B_V&=\mathfrak O_{30,p}
-60^n\,\mathcal P_p\!\left((6/5)^3\right).
\end{aligned}
}
\tag{20}
$$
$60^n=(60/p)$ 是单位，且 $(6/5)^3=729(2/15)^3$。特别
$$
\boxed{
\mathfrak B_V-\mathfrak B_S
=-\left(\frac{60}{p}\right)
\left\{\mathcal P_p(729X_0)-\mathcal P_p(X_0)\right\},
\qquad X_0=(2/15)^3.
}
\tag{21}
$$
式(21)消去的是两条**实际同源行**中同一个
$\mathfrak O_{30,p}$，没有消去(19)的任何低卷积。
由原 $S,V$ 中央零得到的首必要条件因此准确包括
$$
\mathcal P_p(729X_0)=\mathcal P_p(X_0),\qquad
\mathfrak O_{30,p}=\left(\frac{60}{p}\right)\mathcal P_p(X_0).
\tag{22}
$$
现在仍未证明第一等式不可能。不能仅用(12)、多项式非恒零、
或整数 $[3]$ 可逆性作此结论。

## 5. 原 g 所在的半短 Bol 与同一留数

这里只将已付一般 Bol 证明代入实际奇来源，不另添连接。
令
$$
a=g_2/12,\quad H=\operatorname{Ha}_p,\quad C=LH,\quad
\mathcal R_p=(L^2H+aH)/p,\quad
a_H=a-p\mathcal R_p/H,\quad \delta_H=H^2L,
$$
$$
r_0=(p-3)/2=n-1.
$$
因
$r(r_0-r+1)\equiv-r(2r+1)/2\pmod p$，准确有
$$
\mathscr U_n
\equiv H^{-r_0-2}\delta_H^{\,n}H^{-r_0}\pmod p.
\tag{23}
$$
whole 奇 jet 的 $j_p\equiv Hj_1$ 又给
$$
(\mathscr U_n-\epsilon_{30}H)g=0,\qquad
\epsilon_{30}=(60/p),
\tag{24}
$$
在原分式函数域中成立。令 $h=H^{-r_0}g$，
(24)等价于
$$
\boxed{(\delta_H^{\,n}-\epsilon_{30}H^p)h=0.}
\tag{25}
$$
这里没有偶质量式中的额外 $\delta_H$ 因子，也没有公共常数分量。
式(25)只是在 characteristic $p$ 的真实谱位置，
不把 $H(P)=0$ 处的除 $p$ 行删去。

在特征零置
$$
G^{\rm odd}_0=1,\quad G^{\rm odd}_{-1}=0,\qquad
G^{\rm odd}_{j+1}
=LG^{\rm odd}_j+j(r_0-j+1)a_HG^{\rm odd}_{j-1}.
$$
它的全阶项是
$G^{\rm odd}_n=H^{-r_0-2}\delta_H^nH^{-r_0}$。
令 $V_j^{\rm odd}=(G_j^{\rm odd}-\mathscr U_j)/p$，则整差递推为
$$
\begin{aligned}
V_{j+1}^{\rm odd}={}&LV_j^{\rm odd}
-\frac{j(2j+1)}2aV_{j-1}^{\rm odd}\\
&+\left(\frac{ja}{2}
-j(r_0-j+1)\frac{\mathcal R_p}{H}\right)G_{j-1}^{\rm odd}.
\end{aligned}
\tag{26}
$$
原 CM 点处 $H=0,L^2H=0,C$ 为单位，且
$\mathcal R_p/H$ 正则。已付一般 residue 公式给
$$
\boxed{
\mathfrak O_{30,p}
=60^n\left[
n!C(P)^{n+1}
\frac{\operatorname{Res}_{P}(g\,\omega_{\rm par}/H^{n+1})}{p}
-(V_n^{\rm odd}g)(P)
\right]\pmod p.
}
\tag{27}
$$
式(27)保同一个 $\mathcal R_p$、全部 $\mathcal R_p/H$ 伴随及真实初始条件。
residue 的除 $p$ 整性是(14)、(26)对这个原 $g$ 的结论；
不是任意双零函数的性质。

## 6. 同 degree136 的真正六阶零

定义原
$$
A^{[2]}(z)=S(2z)/64,\qquad B^{[2]}=U-A^{[2]}.
$$
R812 已付完整源
$$
B^{[2]}=\Theta^{68}\frac{a(t)tK_{17}(t)}{91b},\qquad
K_{17}(t)=\frac{H_{18}(t)-13d(t)^2H_{16}(t)}t,
$$
$$
K_{17}(0)=-24570,\qquad
B^{[2]}(z)=1890b\,z^{12}+O(z^{18}).
\tag{28}
$$
这里 $t=-b/x^3$、$a(t)=t(t-1)(7+4t+16t^2)$；R812 原显示式在 $b=1$，恢复一般固定 $b$ 时的 $b^{-1}$ 正是原首 $z^6$ 系数归一。因为 $a(t)tK_{17}(t)=171990b^2z^{12}+\cdots$，(28)的首项确为 $1890b z^{12}$。这是同 degree136 的完整多项式差，不是把原 $U$ 认成倍点 $S$。

对热算子直接用链式法则：
$$
Q_{4m}\{F(2z)\}=(Q_mF)(2z).
\tag{29}
$$
所以整数 $[2]$ 拉回确实与水平连接交换。
绝对 theta 标签式也准确为
$$
\boxed{
F_{m,a}(\tau,2z)
=F_{4m,2a}(\tau,z)+F_{4m,2a+2m}(\tau,z).
}
\tag{30}
$$
两边都只有同一个 $c_\lambda$，没有额外周期倍率。
因此原固定水平质量满足
$$
\boxed{f_{B^{[2]}}^\flat=f_U^\flat-f_S^\flat/64.}
\tag{31}
$$
由(28)的整个原纤维及热 jet 的三角关系，
$$
\boxed{
L^r f_{B^{[2]}}^\flat(P)=0\ (0\le r<6),\qquad
L^6 f_{B^{[2]}}^\flat(P)
=\frac{12!\,1890b}{272^6}\ne0.
}
\tag{32}
$$
故其零阶恰为六。对原 $p>211$，右端在既有坏集外为单位。
两条源的首行同样精确运输：
$$
\boxed{
\mathfrak B_{136,p}(B^{[2]})
=\mathfrak B_U-\frac{2^{p+1}}{64}\mathfrak B_S
\equiv\mathfrak B_U-\frac1{16}\mathfrak B_S\pmod p.
}
\tag{33}
$$
这里 $j_{p+1}(S)$ 本来含 $p$，因此约化 $2^{p+1}/64$ 不丢额外 Fermat-quotient 项。
原 $S,U$ 两个首必要零条件等价于原 $S,B^{[2]}$ 两个首必要零条件。
这只是同一条件的准确换基，没有增加一个独立中央零。

## 7. 四个固定参数函数的常系数独立性

还有一个不需数值读取的限定结论。
把四个 $f_\nu^\flat$ 乘以同一个 $\eta/\Delta_0^{1/24}$，
得到各 degree $m_\nu$ 的 unary theta 常系数线性组合。
其正 $q$ 指数为 $r^2/(2m_\nu)$。
两个 degree 的正指数能重合，必要且充分是它们比为有理平方。
本题恰有三个平方类：
$$
\{34,136\},\qquad\{72\},\qquad\{66\}.
\tag{34}
$$
对固定 degree，原偶来源的 theta 质量的不同标签只按 $a\sim-a$ 重合；
一个这样的非零组合不能只有常数项，因为每个剩余类也有非零整数代表。
因此任何四函数常系数关系，先迫 $T,V$ 的系数各为零。
剩下 $S,U$ 若有关系，则由(31)–(32)及 $f_S^\flat$ 恰三阶为零，
其两个系数也都为零。故
$$
\boxed{
f_S^\flat,f_T^\flat,f_U^\flat,f_V^\flat
\text{ 在 }\overline{\mathbf Q}\text{ 上线性独立。}
}
\tag{35}
$$
这只是固定常系数函数空间的维数 $4$；
不声称它们在 Frobenius 常数域上自动独立，
也不声称一个指定行不能同时杀此四维空间。

本注的实际新接口是(20)–(22)的同一奇来源约束及(31)–(33)的真实六阶零。
四条原首行的共同非消失仍须由这些**完整**有限卷积、
真实 Bol 余项或原全部中央条件继续推出。
