# R756 — 原范数三映射的完整 canonical 返回与真实接触成本

日期：2026-11-15。**状态：以下准确同源映射、全来源格返回和接触运输已证明。**

本篇继续 R729 的原范数三同源，支付它在 R680 的完整 canonical 来源格上的实际代价。径向变量虽为三次，但原十九角条件不随之自动满足。一个显示的公共乘子把全部原列送入同一 canonical 系列，最高 charge 为
$$
3D+\left\lceil\frac{36D+181}{47}\right\rceil.
$$
这是一条统一充分上界，不声称最优，也不声称原 $3D$ 预算已足够。

原低轴接触在同源代入后保持原阶；显示乘子再增加一个 $O(D)$ 的准确阶。它没有把 $h$ 变成 $3h$。对完整高度二 Gaussian 规范，还必须保 R729 的实际有限指数。原中央零没有被赋给本篇新增来源。

## 1. 原变量及准确范数三映射

在原 equianharmonic 曲线上取
$$
E_b:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad\delta^2=-3,
$$
$$
t=-b/x^3,\qquad \Theta=x\sigma^2,\qquad
d(t)=1+8t,\qquad Y=d(t)\Theta^{17}.
\tag{1}
$$
在 R418/R473 的共同 $E_1$ 规范中取 $b=1$；下面的 $t,\Theta$ 变换完全相同。$\sigma$ 是同一个原 sigma，不改 Gaussian 或半特征。

置
$$
v(t)=1-4t,\qquad
A(t)=v(t)^3-216t,\qquad h(t)=7+4t+16t^2,
$$
$$
\boxed{\varphi(t)=-\frac{27t}{v(t)^3},\qquad
B(t)=\frac{A(t)v(t)^{14}}{d(t)^3}.}
\tag{2}
$$

**定理 1。** 原 $[\delta]$ 在完整变量上的准确作用为
$$
\boxed{
t(\delta z)=\varphi(t(z)),\quad
\Theta(\delta z)=v(t(z))\Theta(z)^3,\quad
Y(\delta z)=B(t(z))Y(z)^3.
}
\tag{3}
$$

**证明。** 因 $\delta=\omega-\omega^2$，在
$[\omega]P=(\omega x,y)$ 与 $-[\omega^2]P=(\omega^2x,-y)$
之间用原椭圆曲线加法式，斜率为 $2y/(\delta x)$。故
$$
x(\delta z)
=\frac{4y^2}{\delta^2x^2}-(\omega+\omega^2)x
=-\frac{x^3+4b}{3x^2}
=-\frac{xv(t)}3.
$$
第一式随即成立。R729 已完整支付同一 sigma 的
$\sigma(\delta z)=\delta x(z)\sigma(z)^3$，
包括奇范数半特征和绝对首因子。因此
$$
x(\delta z)\sigma(\delta z)^2
=\left(-\frac{xv}3\right)(-3x^2\sigma^6)=v\Theta^3.
$$
最后 $d(\varphi)=A/v^3$，故
$d(\varphi)v^{17}\Theta^{51}=B(d\Theta^{17})^3$。证毕。

本篇将 (3) 记作有理代入
$$
\Psi^*P=P(\varphi(t),B(t)Y^3).
\tag{4}
$$
它不是原十九角曲面上已经付清的无极自映射。下面直接把它作用于全部原列，支付所有角条件。

## 2. 原完整 canonical 格与三个辅助恒等式

使用 R680 的相同整系数环；可取
$$
R=\mathbf Z[1/(2\cdot3\cdot7\cdot13\cdot17)].
$$
固定 $D\ge3$，对 $0\le n\le D$ 置
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
f_n=\lfloor9n/2\rfloor+4,\quad
e_{n+1}=f_n-3A_n-B_n+C_n,
$$
$$
q_n(t)=(t h(t))^{A_n}(t-1)^{B_n}d(t)^{-C_n}.
$$
全部原来源为
$$
\boxed{\mathcal W_D=
\bigoplus_{n=0}^D Y^nq_n(t)R[t]_{\le e_{n+1}}.}
\tag{5}
$$
这里 $f_n$ 始终是整数帽；列多项式另记作 $F_n(t)$，不混用。

直接由 (2) 有
$$
\boxed{
\varphi-1=\frac{(t-1)d^2}{v^3},\qquad
d(\varphi)=\frac A{v^3},\qquad
\varphi-t=\frac{4t(t-1)h(t)}{v^3}.
}
\tag{6}
$$
定义完整多项式
$$
H(t):=v(t)^6h(\varphi(t))
=7v^6-108tv^3+11664t^2.
\tag{7}
$$
由最后一式 (6)，$h(\varphi)-h(t)$ 被 $h(t)$ 整除于
$R[t,v^{-1}]$。又 $h(1/4)=9$ 在 $R$ 中为单位，所以 $h$ 与 $v$ 在 $R[t]$ 中互素；$h$ 的首系数16也在 $R$ 中为单位。因此
$$
\boxed{H(t)=h(t)H_4(t),\qquad H_4\in R[t],\quad\deg H_4\le4.}
\tag{8}
$$
这没有用模若干素数的观察推断因子。也可代入
$h(X)-h(t)=(X-t)(16(X+t)+4)$
逐项得到该整除；(7) 的次数至多六给最后的次数界。

式 (6) 表示三个原四步链的底点 $0,h_{7,1},h_{7,2}$
以及原三步链底点1在底映射下固定。$d=0$ 和无穷远的实际分歧也保留在 (6)、(7)，没有把新原像当成免费旧角。

## 3. 每条原列的全部分子、分母及新极点

对任意 $F_n\in R[t]_{\le e_{n+1}}$，由 (2)、(6)、(7) 精确有
$$
\begin{aligned}
\Psi^*(Y^nq_nF_n)
={}&(-27)^{A_n}Y^{3n}
 t^{A_n}H^{A_n}(t-1)^{B_n}
 d^{2B_n-3n} A^{n-C_n}\\
&\quad\cdot
v^{14n-9A_n-3B_n+3C_n}
F_n(-27t/v^3).
\end{aligned}
\tag{9}
$$
所有因子均来自同一实际代入。特别 $A$ 的指数
$n-C_n\ge0$；$d(\varphi)=0$ 的新原像不会给一个漏记的分母。

将最后一个多项式齐次化：
$$
\widetilde F_n(t)=v^{3e_{n+1}}F_n(-27t/v^3)\in R[t].
$$
则 (9) 中剩余 $v$ 指数准确为
$$
m_n^{(v)}=14n-3f_n
=\begin{cases}
n/2-12,&n\ {\rm even},\\
(n-21)/2,&n\ {\rm odd}.
\end{cases}
\tag{10}
$$
所以对全部 $n\ge0$，$m_n^{(v)}\ge-12$。
**固定的 $v^{12}$ 已清掉全部新底点 $t=1/4$ 的极点。**
这里的12与 $D$、$p$ 无关；没有将每个 charge 的分母独立放大。

乘 $v^{12}$ 后，(9) 的唯一可能有限极点在原 $d=0$。
由 (8)，它在 $0,h_{7,1},h_{7,2}$ 至少分别有
$A_n$ 阶零，在1至少有 $B_n$ 阶零。
另一方面，在底无穷远
$$
\varphi(t)\sim\frac{27}{64}t^{-2},\qquad B(t)\sim c_Bt^{14},
\quad c_B\ne0.
$$
因此 (9) 的 $Y^{3n}$ 系数的准确统一度界为
$$
\boxed{\deg_\infty\bigl(\Psi^*(q_nF_n)\,B^n\bigr)
\le14n-2A_n.}
\tag{11}
$$
这里仅用 $F_n$ 在0无极；若它在0有零，则度更小。
式 (11) 用有理函数的分子次数减分母次数，因而没有忘记 $d$ 的分母。

## 4. 一个显示的公共乘子和全部原角返回

定义整数
$$
\boxed{
m=\left\lceil\frac{36D+181}{47}\right\rceil,\quad
a=\left\lceil\frac{2D+m}{4}\right\rceil,\quad
b_1=\left\lceil\frac{2D+m}{3}\right\rceil,\quad
c=\max\!\left(0,\left\lceil\frac{5D-3m+11}{6}\right\rceil\right).
}
\tag{12}
$$
下标 $b_1$ 只是乘子指数，不是曲线常数 $b=17$。
令
$$
\boxed{
\Gamma_D(t,Y)=
Y^m v^{12}(t h(t))^a(t-1)^{b_1}d^c.
}
\tag{13}
$$

**定理 2（完整 canonical 返回）。**
$$
\boxed{
\Gamma_D\,\Psi^*(\mathcal W_D)
\subset \mathcal W_{3D+m}.
}
\tag{14}
$$
这个包含在环 $R$ 上逐列成立，因而对所有原允许素数整成立。它保原十九角的所有中间条件，不只保最后一个矩形帽。

**证明。** 对 (9) 的一条原列，乘 (13) 后的新 charge 是
$N=3n+m$。要属于 (5) 的 $N$-块，须且只须：

1. 在 $0,h_{7,1},h_{7,2}$ 的零阶均至少 $A_N$；
2. 在1的零阶至少 $B_N$；
3. 在 $d=0$ 的极阶不超过 $C_N$；
4. 除这些原有限点外无极，且有理系数度至多 $f_N$。

前三项由下列准确整数不等式支付。
对 $n\le D$，
$$
A_N-A_n\le\left\lceil(2n+m)/4\right\rceil\le a,
$$
$$
B_N-B_n\le\left\lceil(2n+m)/3\right\rceil\le b_1.
\tag{15}
$$
而
$$
\begin{aligned}
3n-2B_n-C_N
&\le3n-\frac{2(n-2)}3-\frac{3n+m-1}2\\
&=\frac{5n-3m+11}{6}\le c.
\end{aligned}
\tag{16}
$$
式 (16) 允许右侧非正，此时 (12) 的 $c=0$ 仍足够。
$A^{n-C_n}$ 没有新极；$v^{12}$ 清分母由 (10) 付清。
因此前四项中的有限点条件全部成立。

还需完整无穷远次数。记 (13) 中角多项式的次数
$$
K_D=12+3a+b_1+c.
$$
若 $c>0$，取整式给
$$
K_D\le3D+\frac7{12}m+\frac{211}{12}
\le\frac92m+\frac52,
\tag{17}
$$
最后一步准确等价于 $47m\ge36D+181$。
若 $c=0$，则
$$
K_D\le\frac{13}6D+\frac{13}{12}m+\frac{179}{12}
\le\frac92m+\frac52.
\tag{18}
$$
此处所需 $41m\ge26D+149$ 也由 (12) 推出，因为
$$
41(36D+181)-47(26D+149)=254D+418>0.
$$

对每个整数 $n$，按 $n\bmod4$ 直接有
$2A_n-n/2\ge-1$。所以
$$
f_N-(14n-2A_n)
\ge\frac92m+\frac72-\frac n2+2A_n
\ge\frac92m+\frac52.
\tag{19}
$$
合并 (11)、(17)–(19)，所得系数度不超过 $f_N$。

将该系数除以 $q_N$ 后，有限点条件保证商在 $R[t]$ 中，
度界保证商的次数至多
$f_N-3A_N-B_N+C_N=e_{N+1}$。
所除固定多项式的首系数只含环 $R$ 中的单位，故不引入移动素数分母。
这正是 (5) 的原 $N$-块，证明 (14)。

R491/R555/R680 已证明 (5) 与十九角线性系逐列双向对应；
因此此处直接回到 (5)，同时支付所有十九个实际角条件。
不再需要假设 $\Psi$ 在吹起曲面上处处正则。证毕。

本定理是充分返回，既没有断言给出的 $m$ 最小，也没有证明不存在更便宜的、依赖实际因子的专用返回。特别不能把 (14) 改写为尚未证明的 $\Psi^*\mathcal W_D\subset\mathcal W_{3D}$。

## 5. 系数成本及原共同来源因子

(14) 是同一个环 $R$ 上的实际线性映射。若原 $P$ 的 canonical 系数范数为 $\|P\|$, 可选其返回表达，使
$$
\|\Gamma_D\Psi^*P\|_{\rm can}\le C^{D+1}\|P\|
\tag{20}
$$
对一个只依赖固定多项式的常数 $C$ 成立。

确实，(9)、(13) 中所有指数和所有次数均为 $O(D)$；
固定多项式的幂及齐次代入的系数范数因此至多指数增长。
除去 $q_N$ 的固定角因子时，可使用其在相应局部框中的单位逆，
或按首系数为固定单位的多项式作除法。
最多 $O(D)$ 步，每步系数只由固定多项式及其 $O(D)$ 次幂的二项系数给出；
等价地，其截断逆系数由固定有理函数的幂产生，统一界仍为 $C^{D+1}$。
$t$ 的幂仅移位。有限个 fixed-denominator primes 的分母指数同为 $O(D)$。
故没有新增随 $p$ 变化的分母或超线性对数系数费用。

原完整物理来源还带 R418 的同一个共同因子
$G_0$，其中包括原 charge40 和 $P_{134}/U_0$ 的固定规范。
对它应使用准确身份
$$
\boxed{
G_0(z)\,\Gamma_D(t(z),Y(z))\,\Psi^*P(t(z),Y(z))
=
\Gamma_D(t(z),Y(z))\frac{G_0(z)}{G_0(\delta z)}
\,(G_0P)(\delta z).
}
\tag{21}
$$
右侧按有理函数恒等式理解，零点处由左侧的完整来源延拓。
式 (21) 保全部固定比值，不能把它删成裸同源 pullback。
(14) 说明左侧属于原定义的更高预算来源，不给它附一个新的中央零条件。

## 6. 原低轴、Euler jet 和接触的准确运输

令 $\rho(t)=d(t)\Theta(t)^{17}$ 是原特征零 germ。
(3) 给
$$
B(t)\rho(t)^3=\rho(\varphi(t)).
\tag{22}
$$
因此对任意原多项式或允许的有理来源 $P$，
$$
(\Psi^*P)(t,\rho(t))
=P(\varphi(t),\rho(\varphi(t))).
\tag{23}
$$
因 $\varphi(0)=0$、$\varphi'(0)=-27$，在原允许素数处为单位，
若右端原接触为有限的 $h$，则
$$
\operatorname{ord}_{t=0}(\Psi^*P)(t,\rho(t))=h.
\tag{24}
$$
它不是 $3h$。

设 $\mathcal E=Y\partial_Y$。链式法则准确给
$$
\mathcal E(\Psi^*P)=3\Psi^*(\mathcal EP),
$$
$$
\boxed{
\mathcal E(\Gamma_D\Psi^*P)
=\Gamma_D\Psi^*(mP+3\mathcal EP).
}
\tag{25}
$$
$\Gamma_D(t,\rho(t))$ 在0的准确阶为 $a$，首单位含
$h(0)^a=7^a$ 及 $(t-1)^{b_1}$ 的真实符号。
所以若 $P,\mathcal EP$ 同消到 $H$，返回后两条 jet 均消到
$H+a$；若只问 $P$ 自身且原阶恰为 $h$，返回后的准确阶为
$$
\boxed{h+a.}
\tag{26}
$$
反向读两条 jet 时，(25) 的矩阵
$\left(\begin{smallmatrix}1&0\\m&3\end{smallmatrix}\right)$
在好素数处可逆。故这一运输没有制造一个额外独立 jet。

R680 的实际惰性低轴满足 $g\equiv\rho\bmod t^s$。
于是 (23)–(26) 在原可读截止以内同样适用于 $g$；
若原接触 $h<s$，其准确阶判断合法。
本篇不将该低轴合同延伸到 $s$ 以后的实际共振行。
乘 $t^a$ 后应相应使用原截止的平移，不能宣称新增行已由原 $M$ 读取。

## 7. 高度二 Gaussian 规范中的完整附加项

R729 使用
$$
w=z^6,\quad c_\sigma=[w^s]\log(\sigma/z),\quad
U=(\sigma/z)e^{-c_\sigma w^s},\quad
s=(p+1)/6,
$$
以及实际整数系数
$$
t_3=c_\sigma(3-\delta^{p+1}).
$$
定义同一个去 Gaussian 变量
$$
\Theta_U=xz^2U^2=\Theta e^{-2c_\sigma w^s},
\qquad Y_U=d(t)\Theta_U^{17}.
$$
由 (3) 逐项保指数，准确得到
$$
\boxed{
Y_U(\delta z)=B(t)Y_U(z)^3
                 \exp(34t_3w^s).
}
\tag{27}
$$
在原 $w^L$ 高度二窗，指数必须按 R729 的实际有限式读取：
$$
\exp(34t_3w^s)
\equiv\sum_{j=0}^{p-2}\frac{(34t_3)^jw^{sj}}{j!}
\pmod{w^L},\qquad L=(p^2-1)/6.
\tag{28}
$$
全部这些阶乘在该窗口为单位。

所以对一个含 charge $n$ 的来源，(27) 还产生对应的
$\exp(34n t_3w^s)$；混合 charge 必须逐项保留。
(14) 支付的是显示代入 (4) 的 canonical 来源返回，
没有支付删除 (27) 的真实 Gaussian/Fermat 商。
在低轴 $t^s$ 前，(27) 的附加项为1，正好与第6节相容；
在完整第二位中则不能省略。

## 8. 可使用的结论及尚未完成的环节

本篇新增的全参数接口是：

- 原 $[\delta]$ 的实际 $(t,\Theta,Y)$ 映射及所有有限分子、分母；
- 固定 $v^{12}$ 清掉新点 $1/4$ 的极；
- 公共乘子 (12)、(13) 将全部 canonical 列整地返回
  $\mathcal W_{3D+m}$，含十九角和指数系数成本；
- 原共同因子 $G_0$ 的完整比值、Euler 两 jet 和准确接触
  $h\mapsto h+a$；
- 高度二处不可删除的实际 Gaussian 项 (27)、(28)。

这里的 charge 主系数为 $177/47$，严格大于3。
不能将该统一返回放进 R750 的原 $3C$ 同预算而忽略差额；
依赖真实因子 $F$ 的更便宜返回仍可另行研究。
它也没有把实际 $\xi$ 或原两十三行重新赋值，
没有将中央 $J'_S,J'_T,J'_U$ 的零传播到 $\Gamma_D\Psi^*P$。
后续若使用此来源与原左行配对，必须保持 (14)、(21)、(25)、(27)
的同一预算与同一个实际来源。

依赖：
[R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)；
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R555](R555-whole-original-linear-system-and-nonzero-high-contact-forcing.md)；
[R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)；
[R729](R729-norm-three-seven-cm-and-density-one-full-ah-reconstruction.md)。

所有公式和整数界均为符号推导；本篇没有新增数值运行或可重算输出。
