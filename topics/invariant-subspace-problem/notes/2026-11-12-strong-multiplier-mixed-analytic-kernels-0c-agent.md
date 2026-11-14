# 有序强交换子的全部混合解析芽：二阶整轨道排除四阶核衰减

日期：2026-11-12（UTC）。子任务：literature。**状态：已证明。**

设 $A$ 是本课题的实际超快径向 dyadic odometer，$Y$ 是 R37 对任意实有序参数
$$
0\le s_j\le t_j,\qquad \sum_jt_j^2<\infty,\qquad
\sum_j(t_j-s_j)=\infty
$$
构造的有界强乘积交换子。本条证明
$$
\boxed{\quad 0\ne F\in\mathbb C\{z,w\}
\quad\Longrightarrow\quad
F(A,Y)\text{ 单射且值域稠密。}\quad}
$$
特别，全部混合铅笔 $Y-\lambda A$ 都单射且值域稠密。这里没有把 R73 边界商的忠实性用到核投影；证明来自实际 Haar 表示中的半群轨道。

核心机制如下：R37 的 $Y$ 等于一个属于 $\mathcal A=\overline{\mathbb C[I,A]}$ 的可逆算子乘以 R20 半群的时间一算子。该半群作用在常向量上的轨道有二阶增长的向量值整延拓，因此任何非零向量的正时间轨道都不能一致按 $\exp(-ct^p)$、$p>2$ 衰减。另一方面，混合解析关系经 Weierstrass 预备后迫出四阶衰减；这给出矛盾。

依赖的已证基础：R9/R12 的 dyadic 幂；R11 的 $1$ 对 $A$ 循环；R20 的强连续半群；R24 的固定共轭对称；R28 的精确局部替换；R37 的 $Y$；R39 的指数与有理替换因子。本条完整补证所需的整延拓、全局增长界、实轴衰减障碍及混合核结论。

## 1. 实际 dyadic 幂的统一整预解式估计

记
$$
d_j=\|A^{2^j}\|=e^{-\Lambda_j},\qquad
N_j=A^{2^j}/d_j.
$$
模型的精确参数给出
$$
\Lambda_0=20,\qquad \Lambda_{j+1}\ge16\Lambda_j,\qquad
N_j^2=\eta_jN_{j+1},\quad \|N_j\|=1,\quad
\eta_j\le e^{-770\,16^j}. \tag{1.1}
$$
这里所有估计针对真实 $N_j$，不是把它们替换成独立的 $E_j$。

**引理 1.1。** 对所有 $j\ge0$、整数 $n\ge2$，
$$
\|N_j^n\|\le e^{-n^4}. \tag{1.2}
$$

**证明。** 取 $k\ge1$ 使 $2^k\le n<2^{k+1}$。由 $\|N_j\|=1$，
$$
\|N_j^n\|\le \|N_j^{2^k}\|
=\exp(-\Lambda_{j+k}+2^k\Lambda_j)
\le \exp[-(16^k-2^k)\Lambda_j].
$$
又 $16^k-2^k\ge(7/8)16^k$、$\Lambda_j\ge20$，以及 $16^k>n^4/16$，故最后一个指数的绝对值至少为 $(35/32)n^4>n^4$。证毕。

于是对任意复数 $v$，逆级数绝对范数收敛，并且一致于 $j$：
$$
\begin{aligned}
\|(I+vN_j)^{-1}\|
&\le 1+|v|+\sum_{n\ge2}|v|^n e^{-n^4}\\
&\le C_0\exp\!\left(C_0[\log(2+|v|)]^{4/3}\right).
\end{aligned} \tag{1.3}
$$
最后一步可自含使用 Young 不等式：若 $a=\log^+|v|$，则
$$
na-n^4\le C a^{4/3}-\tfrac12n^4;
$$
再对 $n$ 求和。常数 $C_0$ 与 $j,v$ 无关。这个估计同时说明 $(I+vN_j)^{-1}$ 是整个 $v$ 平面上的算子值整函数。

此外，对每个整数 $n\ge1$，
$$
\boxed{\|A^n\|\le \exp(-\tfrac54 n^4).} \tag{1.4}
$$
事实上，若 $2^k\le n<2^{k+1}$，则 $\|A\|<1$ 给
$\|A^n\|\le d_k\le e^{-20\,16^k}\le e^{-(5/4)n^4}$。

## 2. R20 半群的常向量轨道有二阶整延拓

给定 $u_j\ge0$、$u\in\ell^2$，令 R20 的半群为
$$
S(t)=\operatorname*{s-lim}_{N\to\infty}
S_N(t),\qquad
S_N(t)=\prod_{j<N}e^{-tu_j}e^{2tu_jN_j},
\qquad t\ge0. \tag{2.1}
$$
R20 已证明该强极限、半群律、与 $A$ 交换及强连续性；特别，
$$
\sup_{0\le t\le T}\|S(t)\|<\infty
\quad\text{对每个有限 }T. \tag{2.2}
$$

下面只为向量 $S(t)1$ 作整个复平面的延拓。**不声称复时间对应一个有界算子 $S(z)$。**

**定理 2.1。** 存在 $H$ 值整函数 $\mathfrak s(z)$，满足
$$
\mathfrak s(t)=S(t)1\quad(t\ge0),\qquad \mathfrak s(0)=1,
$$
以及某个有限常数 $C_u$ 的全局估计
$$
\boxed{\|\mathfrak s(z)\|\le
\exp[C_u(1+|z|^2)]\quad(z\in\mathbb C).} \tag{2.3}
$$

### 2.1 精确乘积向量

令
$$
P_j(z)=e^{-zu_j}
[I+(1+2zu_j)N_j](I+N_j)^{-1}, \tag{2.4}
$$
以及
$$
R_j(z)=e^{2zu_jN_j}(I+N_j)
[I+(1+2zu_j)N_j]^{-1}. \tag{2.5}
$$
这些是整个 $z$ 平面上可逆的算子值整函数，且彼此交换，因为都是 $A$ 的整函数或拟幂零预解式。它们满足精确恒等式
$$
e^{-zu_j}e^{2zu_jN_j}=R_j(z)P_j(z). \tag{2.6}
$$

R28 的精确一位替换说明
$$
\left(\prod_{j<N}P_j(z)\right)1
=\bigotimes_{j<N}v_j(z)\otimes1_{\ge N}, \tag{2.7}
$$
其中，按两点公平概率测度的函数坐标，
$$
v_j(z)=e^{-zu_j}(1,1+2zu_j).
$$
该恒等式对复 $z$ 同样成立；它来自
$N_j(e_0\otimes h)=e_1\otimes h$，且其余所有位的 $h$ 可以任意。

对 $q=zu_j$，
$$
\|e^{-q}(1,1+2q)\|^2
=e^{-2\operatorname{Re}q}
[1+2\operatorname{Re}q+2|q|^2]
\le e^{2|q|^2}. \tag{2.8}
$$
这里括号内严格为正，且对 $v>-1$ 使用 $\log(1+v)\le v$，取
$v=2\operatorname{Re}q+2|q|^2\ge-1/2$ 即得。

在每个紧的 $z$ 集合上，
$$
\langle v_j(z),1\rangle=e^{-zu_j}(1+zu_j)=1+O(u_j^2),
\qquad \|v_j(z)\|^2=1+O(u_j^2), \tag{2.9}
$$
误差常数一致。由于 $\sum u_j^2<\infty$，有限张量乘积在 $H$ 中局部一致收敛。具体地，对任意尾区间 $m\le j<n$，
$$
\left\|\bigotimes_{j=m}^{n-1}v_j(z)-1\right\|^2
=\prod_{j=m}^{n-1}\|v_j(z)\|^2+1
-2\operatorname{Re}\prod_{j=m}^{n-1}\langle v_j(z),1\rangle
\longrightarrow0
$$
局部一致于 $z$ 及 $n\ge m\to\infty$；有限前缀的范数由 (2.8) 一致控制。故极限
$$
\mathfrak v(z)=\bigotimes_{j\ge0}v_j(z)
$$
是 $H$ 值整函数，并满足
$$
\|\mathfrak v(z)\|\le
\exp\!\left(|z|^2\sum_j u_j^2\right). \tag{2.10}
$$

### 2.2 实际进位修正的局部一致整乘积

写 $r=|zu_j|$。从 (2.5) 的分子减去其分母，常数项及 $N_j$ 一次项都抵消，因此由 $\|N_j^n\|\le\eta_j$（$n\ge2$）可得
$$
\begin{aligned}
&\|e^{2zu_jN_j}(I+N_j)-[I+(1+2zu_j)N_j]\|\\
&\hspace{25mm}\le
\eta_j[(e^{2r}-1-2r)+(e^{2r}-1)]
\le2\eta_je^{2r}. 
\end{aligned} \tag{2.11}
$$
与 (1.3) 结合，对每个固定紧的 $z$ 集合有
$$
\|R_j(z)-I\|\le C_{\rm compact}\eta_j. \tag{2.12}
$$
于是
$$
R(z)=\prod_{j\ge0}R_j(z) \tag{2.13}
$$
按算子范数局部一致收敛，是算子值整函数。对每个固定 $z$，其尾因子与 $I$ 的差绝对可和；尾部逆的差也可和，有限前缀可逆。所以 $R(z)$ 可逆。这里无需从一个强极限推断可逆性。

### 2.3 进位修正的全局增长

通过重标度 $z$，可先假设 $\sup_j u_j\le1$；一般有界 $u$ 只改变最终常数。若 $u=0$，结论显然。以下令 $r=|z|\ge2$。

取最小整数 $k\ge0$ 使
$$
770\,16^k\ge8r.
$$
于是 $k=O(\log(2+r))$，且
$$
\sum_{j\ge k}\eta_j\le2e^{-8r}. \tag{2.14}
$$
对 $j\ge k$，令 $b_j=1+2zu_j$，则
$|b_j|\le1+2r$、$|b_j|^2\eta_j\le1/2$。利用精确恒等式
$$
(I+b_jN_j)^{-1}
=(I-b_jN_j)(I-b_j^2\eta_jN_{j+1})^{-1},
$$
得到
$$
\|(I+b_jN_j)^{-1}\|\le4(1+r).
$$
故由 (2.11)
$$
\sum_{j\ge k}\|R_j(z)-I\|
\le8(1+r)e^{2r}\sum_{j\ge k}\eta_j
\le16(1+r)e^{-6r}\le1. \tag{2.15}
$$
尾乘积范数因而至多为 $e$。

对 $j<k$，(1.3) 给
$$
\log\|R_j(z)\|
\le 2ru_j+C+
C[\log(3+2r)]^{4/3}.
$$
因此
$$
\begin{aligned}
\log\left\|\prod_{j<k}R_j(z)\right\|
&\le2r\sum_{j<k}u_j+Ck[1+(\log(3+2r))^{4/3}]\\
&\le2r\|u\|_2\sqrt k+
Ck[1+(\log(3+2r))^{4/3}]\\
&\le C_u\{1+r\sqrt{\log(2+r)}+[\log(2+r)]^{7/3}\}\\
&\le C'_u(1+r^2).
\end{aligned} \tag{2.16}
$$
结合 (2.15)，并把有界圆盘 $|z|\le2$ 上的局部界吸收入常数，得
$$
\|R(z)\|\le \exp[C_u''(1+|z|^2)]. \tag{2.17}
$$

### 2.4 与真实半群轨道的识别

由 (2.6)—(2.7)，
$$
S_N(z)1=\left(\prod_{j<N}R_j(z)\right)
\left(\bigotimes_{j<N}v_j(z)\otimes1_{\ge N}\right).
$$
右边在 $H$ 中局部一致趋于
$$
\mathfrak s(z):=R(z)\mathfrak v(z). \tag{2.18}
$$
故其为整函数；(2.10)、(2.17) 给 (2.3)。在实 $t\ge0$ 上，R20 的强极限定义给
$\mathfrak s(t)=S(t)1$。在零处，各因子均为恒等，故
$\mathfrak s(0)=1$。定理 2.1 得证。

## 3. 二阶整函数不能沿整个正实轴四阶衰减

下面给一个自含的标量引理，避免引用最小模定理。

**引理 3.1。** 设整函数 $f$ 满足
$$
|f(z)|\le C e^{C|z|^2}\quad(z\in\mathbb C). \tag{3.1}
$$
若存在 $p>2$、$c>0$、$C'>0$ 使
$$
|f(t)|\le C'e^{-ct^p}\quad(t\ge0), \tag{3.2}
$$
则 $f\equiv0$。

**证明。** 若 $f\not\equiv0$，可取 $y>0$ 使 $f(iy)\ne0$，因为非零整函数的零点不能在正虚轴上有聚点。令
$$
D_R=\{z:\operatorname{Im}z>0,\ |z|<R\},\qquad R>2y.
$$
在 $iy$ 看向直径 $(-R,R)$ 的调和测度密度为
$$
k_R(x)=\frac{y}{\pi}
\left[\frac1{x^2+y^2}
-\frac{R^2}{R^4+y^2x^2}\right]. \tag{3.3}
$$
为核对该公式，可从圆盘 Green 函数
$$
G_{\mathbb D_R}(z,\zeta)
=\log\left|\frac{R^2-z\overline\zeta}{R(z-\zeta)}\right|
$$
减去其关于实轴反射的 Green 函数，得到半圆盘 Green 函数，再在直径上取内法向导数并除以 $2\pi$。对 $z=iy$ 直接求导即为 (3.3)。该密度非负。

其直径总质量可直接积分：
$$
\begin{aligned}
\int_{-R}^{R}k_R(x)\,dx
&=\frac2\pi\left[\arctan(R/y)-\arctan(y/R)\right]\\
&=1-\frac4\pi\arctan(y/R).
\end{aligned}
$$
所以圆弧的调和测度质量至多为
$$
\omega_R(\text{圆弧})=\frac4\pi\arctan(y/R)
\le\frac{4y}{\pi R}. \tag{3.4}
$$

令 $v(z)=\log|f(z)|$。次调和均值不等式给
$$
v(iy)\le\int_{-R}^{R}v(x)k_R(x)\,dx
+\int_{\text{圆弧}}v(z)\,d\omega_R(z). \tag{3.5}
$$
若边界有零点，可先对次调和函数
$\max(v,-M)$ 应用此式，再让 $M\to\infty$；以一个共同上界减去后使用单调收敛，故 (3.5) 在可能取 $-\infty$ 的积分意义下仍成立。

由 (3.1)、(3.4)，圆弧贡献至多 $O(R)$。在负半直径上，
$$
v(x)\le C_1(1+x^2),\qquad
k_R(x)\le \frac{y}{\pi(x^2+y^2)},
$$
故该部分贡献也至多 $O(R)$。

由 (3.2)，可固定 $T\ge1$，使 $v(x)\le-(c/2)x^p\le0$ 对 $x\ge T$ 成立。对 $T\le x\le R/2$，因为 $R>2y$，
$$
x^2+y^2\le R^2/2,\qquad
k_R(x)\ge\frac{y}{2\pi(x^2+y^2)}.
$$
因此正半直径在 $[T,R/2]$ 上的贡献至多
$$
-\frac{cy}{4\pi}
\int_T^{R/2}\frac{x^p}{x^2+y^2}\,dx
\le -c_yR^{p-1}+O(1). \tag{3.6}
$$
区间 $[R/2,R]$ 的贡献非正，可舍去；$[0,T]$ 的上界贡献为 $O(1)$。代回 (3.5) 得
$$
\log|f(iy)|\le -c_yR^{p-1}+O(R)\longrightarrow-\infty
$$
因为 $p>2$，与 $f(iy)\ne0$ 矛盾。证毕。

## 4. 任何非零半群轨道都不能超二阶衰减

固定课题中的共轭等距反线性算子
$$
Cf(y)=\overline{f(-1-y)},\qquad
B(x,h)=\langle x,Ch\rangle.
$$
$B$ 是连续非退化的复双线性型，$A$ 对它对称。R20 的 $S(t)$ 由 $A$ 的函数强极限得到，所以对实 $t\ge0$，
$$
B(S(t)x,h)=B(x,S(t)h). \tag{4.1}
$$

**定理 4.1。** 若 $x\in H$，且存在 $p>2$、$c,C>0$ 使
$$
\|S(t)x\|\le Ce^{-ct^p}\quad(t\ge0), \tag{4.2}
$$
则 $x=0$。

**证明。** 对每个一变量多项式 $P$，定义标量整函数
$$
f_P(z)=B(x,P(A)\mathfrak s(z)).
$$
由定理 2.1，它满足引理 3.1 的二阶增长界。在实 $t\ge0$ 上，$P(A)$ 与 $S(t)$ 交换，结合 (4.1) 给
$$
f_P(t)=B(S(t)x,P(A)1),
$$
因此 (4.2) 使 $f_P$ 满足引理 3.1 的超二阶衰减条件，故 $f_P\equiv0$。特别
$$
0=f_P(0)=B(x,P(A)1)
$$
对所有 $P$ 成立。R11 的 $1$ 对 $A$ 循环性及 $B$ 非退化性于是给 $x=0$。证毕。

此处的结论针对每一个向量，而不仅针对某个不变子空间上的算子范数。它也不要求对任意 $x$ 构造复时间的向量 $S(z)x$；所用整延拓只有已完全证明的参考轨道 $\mathfrak s(z)$。

## 5. 把 R37 的 $Y$ 分解为可逆范数因子与半群

沿用 R37 的实有序参数，置
$$
\rho_u=\frac{1-u}{1+u},\qquad
\alpha_j=\frac{(1+s_j)/\sqrt{1+s_j^2}}
{(1+t_j)/\sqrt{1+t_j^2}},
$$
$$
\kappa_j=\rho_{s_j}-\rho_{t_j}
=\frac{2(t_j-s_j)}{(1+s_j)(1+t_j)},\qquad
u_j=\frac{\kappa_j}{2}. \tag{5.1}
$$
则
$$
0\le u_j<1,\qquad u\in\ell^2,\qquad\sum_j u_j=\infty.
$$
最后一项由 $s_j,t_j\to0$ 及 $\sum(t_j-s_j)=\infty$ 得到。R37 的有限局部因子为
$$
W_j=\alpha_j(I+\rho_{s_j}N_j)(I+\rho_{t_j}N_j)^{-1}. \tag{5.2}
$$

定义
$$
D_j=(I+\rho_{s_j}N_j)(I+\rho_{t_j}N_j)^{-1}
e^{-2u_jN_j},\qquad
\beta_j=\alpha_je^{u_j}. \tag{5.3}
$$
于是有精确恒等式
$$
W_j=\beta_jD_j\,e^{-u_j}e^{2u_jN_j}. \tag{5.4}
$$

### 5.1 $\prod D_j$ 是可逆范数乘积

因 $|\rho_{s_j}|,|\rho_{t_j}|\le1$，(1.1) 的二次递归给统一的预解式界
$$
\|(I+\rho_{t_j}N_j)^{-1}\|
\le \frac2{1-\eta_0}.
$$
又
$$
\begin{aligned}
&(I+\rho_{s_j}N_j)(I+\rho_{t_j}N_j)^{-1}
-(I+\kappa_jN_j)\\
&\qquad=-\kappa_j\rho_{t_j}N_j^2
(I+\rho_{t_j}N_j)^{-1}.
\end{aligned}
$$
故其范数不超过 $C\kappa_j\eta_j$。另一方面，
$e^{-\kappa_jN_j}(I+\kappa_jN_j)-I$ 的常数项和一次项都消失；因为 $0\le\kappa_j<2$，其范数不超过 $C\kappa_j^2\eta_j$。组合后得
$$
\|D_j-I\|\le C\kappa_j\eta_j. \tag{5.5}
$$
右边可和。每个 $D_j$ 都可逆，且属于 $\mathcal A$。尾部逆的差也可和，所以
$$
D=\prod_{j\ge0}D_j
$$
及其逆均按范数收敛，且 $D,D^{-1}\in\mathcal A$。

### 5.2 标量乘积不退化

记
$$
\ell(u)=\log(1+u)-\tfrac12\log(1+u^2).
$$
则
$$
\log\beta_j=\ell(s_j)-\ell(t_j)+u_j.
$$
对充分小的非负参数，$\ell(u)=u+O(u^2)$，而
$$
u_j=(t_j-s_j)+O(t_j^2+s_j^2).
$$
因此
$$
|\log\beta_j|\le C(t_j^2+s_j^2)\le2Ct_j^2
$$
对所有充分大 $j$ 成立。有限前缀各项都严格正，故
$$
\beta=\prod_{j\ge0}\beta_j\in(0,\infty). \tag{5.6}
$$

令
$$
\mathcal R=\beta D\in\mathcal A,\qquad
\mathcal R^{-1}\in\mathcal A.
$$
将 (5.4) 相乘，有限范数因子趋于 $\mathcal R$，半群有限乘积按 R20 强趋于 $S(1)$，而 R37 的左边强趋于 $Y$。因此
$$
\boxed{Y=\mathcal R S(1)=S(1)\mathcal R,\qquad
\mathcal R,\mathcal R^{-1}\in\mathcal A.} \tag{5.7}
$$
这里 $\mathcal R$ 是一个明确可逆的范数乘积；不要求它等于某个普通收敛一变量解析芽在 $A$ 上的值。

## 6. 全部非零混合解析芽单射且值域稠密

首先说明演算合法。$A,Y$ 交换且均拟幂零；对于每个 $\varepsilon>0$，分别存在有限常数，使
$$
\|A^m\|\le C_\varepsilon\varepsilon^m,\qquad
\|Y^n\|\le C'_\varepsilon\varepsilon^n.
$$
所以对每个收敛芽 $F(z,w)=\sum f_{mn}z^mw^n$，选足够小的 $\varepsilon$ 后，
$\sum |f_{mn}|\|A^m\|\|Y^n\|$ 有限。其算子值演算绝对范数收敛，乘法由绝对收敛合法交换求和；每个标量常数非零的芽单位 $U$ 在算子上可逆，其逆为 $(1/U)(A,Y)$。

**定理 6.1。** 对任意非零 $F\in\mathbb C\{z,w\}$，
$F(A,Y)$ 单射且值域稠密。

**证明。** 从 $F$ 中提取最大的 $z$ 公因子：
$$
F(z,w)=z^\nu F_0(z,w),\qquad F_0(0,w)\not\equiv0.
$$
由于 $A$ 单射，$F(A,Y)$ 与 $F_0(A,Y)$ 有相同的核。若
$F_0(0,0)\ne0$，则 $F_0(A,Y)$ 可逆，结论立即成立。

否则，对 $F_0$ 关于 $w$ 应用 Weierstrass 预备（所需自含版本见 R62），得
$$
F_0(z,w)=U(z,w)\left[
w^d+\sum_{k=0}^{d-1}a_k(z)w^k\right], \tag{6.1}
$$
其中 $d\ge1$、$U(0,0)\ne0$，各 $a_k(0)=0$。写
$a_k(z)=zb_k(z)$，并定义有界交换子
$$
Q=-\sum_{k=0}^{d-1}b_k(A)Y^k. \tag{6.2}
$$

若 $F(A,Y)x=0$，因上述单位可逆，有
$$
Y^dx=AQx.
$$
$A,Y,Q$ 全部交换，故可逐次迭代：
$$
Y^{dn}x=A^nQ^nx\quad(n\ge0). \tag{6.3}
$$
从 (5.7)，得到
$$
S(dn)x=\mathcal R^{-dn}A^nQ^nx,
$$
因此由 (1.4)
$$
\|S(dn)x\|
\le \|x\|\,
\|\mathcal R^{-1}\|^{dn}\|Q\|^n
\exp(-\tfrac54 n^4). \tag{6.4}
$$
对一般实 $t\ge0$，写 $t=dn+r$，$0\le r<d$。半群律及 (2.2) 的 $[0,d]$ 一致界把 (6.4) 变成
$$
\|S(t)x\|\le C_xe^{-c_dt^4}\quad(t\ge0), \tag{6.5}
$$
其中 $c_d>0$，有限常数 $C_x$ 吸收小 $t$ 区间。若 $Q=0$，(6.4) 从 $n\ge1$ 已为零，同样满足 (6.5)。由定理 4.1，$x=0$。这证明单射性。

最后，$A,Y$ 对同一个 $B$ 对称且交换，绝对范数收敛的解析演算保留该对称性。因此
$$
F(A,Y)^*=C\,F(A,Y)\,C.
$$
单射性于是给 $\ker F(A,Y)^*=\{0\}$，即
$\overline{\operatorname{Ran}F(A,Y)}=H$。证毕。

### 6.1 若干直接推论

1. 对每个 $\lambda\in\mathbb C$、正整数 $r,m$，
   $Y^r-\lambda A^m$ 均单射且值域稠密；其非零性也由定理本身得到。
2. 非零混合解析芽的演算忠实：若 $F(A,Y)=0$，则定理 6.1 的单射性与 $H\ne\{0\}$ 矛盾。
3. 若 $h$ 对 $A$ 循环，则对每个非零 $F$，
   $F(A,Y)h$ 非零并且对 $A$ 循环。事实上，$F(A,Y)$ 的值域稠密，而 $F(A,Y)p(A)h=p(A)F(A,Y)h$。
4. 任意有限、由不同参数对 $(\alpha_j,\beta_j)$ 构成的非零标量组合
   $F(z,w)=\sum_j c_j e^{\alpha_j z+\beta_j w}$ 都满足本条结论。这些指数芽的线性独立可沿避开有限条退化方向的直线归结为一变量不同指数的 Vandermonde 行列式。
5. 更一般地，只要交换子方程在某个向量 $x$ 上给出
   $Y^dx=AQx$，其中有界 $Q$ 与 $A,Y,\mathcal R$ 交换，同一个迭代证明就迫使 $x=0$。解析芽只是完整保证这种关系的一类来源。

## 7. 结论的准确范围

本条覆盖 R37 **全部实有序平方可和参数**；未要求尾参数具有正则幂次渐近，也未要求 $\sum(t_j-s_j)$ 收敛。证明真正使用了相对差不可和所产生的 $Y$ 及其既有拟幂零性，但整轨道工具本身对任意非负 $\ell^2$ 半群参数成立。

本条没有把结果自动扩到 R37 第 10 节的同虚部复参数：那需要额外验证相应半群时间方向及整轨道增长，本文没有做该步骤。也未证明范数闭代数
$\overline{\mathcal A[Y]}$ 的每个非零元素都单射，未覆盖任意非解析交换子，更未证明 $A$ 的每个非零向量都循环。

新证明排除的是明确的混合解析核。原 Hilbert 不变子空间问题及本候选算子的全部向量循环性仍未完成。

