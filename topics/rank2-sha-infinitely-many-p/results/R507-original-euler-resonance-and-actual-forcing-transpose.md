# R507 — 完整原 Γ 上的唯一 Euler 共振与实际 forcing 转置

日期：2026-11-14。**状态：已证明。** 原 $t$ 角 ODE 乘回同一个椭圆对数单位后，在整个原三块整目标上准确成为
$\mathsf N(6\mathsf N-1)$。其唯一非零非单位对角元位于原 $\epsilon$ 行，恰为 $sp$。由此，regularization 移走的首共振在下一精度的原目标中准确恢复为 $p a s\,\epsilon$，不是可删的形式尾。

同一身份把 R505 的实际 $\xi$ 配对转成原因子曲线的指定代数 forcing 除 $p$，并给保持原极帽的显式有限转置。这里的 Smith 结论属于这个真实目标微分算子；未冒称它是原 $J$ 或 $M$ 的 Smith，也未假定实际来源像对该算子稳定。R502 的活 $V_1$、原低行高尾及 $P_{134}/U_0$ 的全部运输继续保留。

## 1. 原椭圆参数、准确尺度及整窗口

保 R467、R498、R502、R505 的
$$
p=6s-1>83,\qquad 1\le\ell<s-13,\qquad L=2s+\ell,
$$
$$
\Gamma_\ell=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2).
\tag{1}
$$
$\mathcal O$ 是原有限非分歧整环，$k=\mathcal O/p$。实际 $Y=\mathscr R$ 及 Gaussian 常数仍为
$$
\rho(t)=d(t)\Theta(t)^{17},\quad d=1+8t,\qquad
g(w)=\rho(t(w))\exp(-a w^s/p),\quad a\in\mathcal O^\times,
$$
$$
Y_{\rm phys}=g(w)e_2(a\epsilon).
\tag{2}
$$

为同时保原 $b=17$ 与已经声明的齐次 $b=1$ frame，本篇不将 $t/w$ 的首单位抹掉。用 R305 的原
$$
u=x^{-1/2},\qquad t=-bu^6,\qquad w=z^6,\qquad
\mathsf h(t)=z/u,
$$
$$
\mathsf h(t)=\sum_{n\ge0}\frac{(1/2)_n}{n!(6n+1)}t^n,\qquad
\mathsf h+6t\mathsf h'=(1-t)^{-1/2}.
\tag{3}
$$
于是
$$
w=-\frac{t}{b}\mathsf h(t)^6.
\tag{4}
$$
若在先前 $t=-w+\cdots$ 的已换标 frame 中工作，只是 (4) 的首单位变成 $-1$。以下算子及原 $\epsilon$ 行身份不依赖这个单位的写法。

在所需长度 $L+13<3s<p$ 中，(3) 的全部分母为 $p$ 单位：$n!$ 的范围小于 $p$，而 $6n+1$ 的第一个正 $p$ 倍数出现于 $n=5s-1$，在窗口之外。因此 $\mathsf h(t(w))$ 及其逆是同一原目标的整单位。$t/w$、$dt/dw$ 也都是整单位。这是目标单位的实际整性，不是在来源中免费加入角函数。

## 2. 原角 ODE 与 w-Euler 算子的特征零恒等

记
$$
\delta=t\partial_t,\qquad
\mathcal P=6(1-t)\delta^2-(1+2t)\delta,
$$
$$
\mathsf C(t)=\frac{154+160t+1792t^2}{3},\qquad
\mathcal R(t)=\frac{t\mathsf C(t)}{d(t)^2}.
\tag{5}
$$
R467 的原方程准确等价于
$$
\mathcal P\log\rho=\mathcal R.
\tag{6}
$$
令 $\mathsf N=w\partial_w$，以及实际单位
$$
\nu=\delta\log w=\frac{t}{w\,dt/dw}
=\frac{1}{\mathsf h(t)\sqrt{1-t}},\qquad
\mathsf B=(1-t)\nu^2=\mathsf h(t)^{-2}.
\tag{7}
$$
所以 $\delta=\nu\mathsf N$。

**定理 1。** 在原正式函数上，准确有算子恒等
$$
\boxed{\mathcal P=\mathsf B\,\mathsf N(6\mathsf N-1).}
\tag{8}
$$

**证明。** 原椭圆对数满足
$$
6t(1-t)z''+(5-8t)z'=0,
$$
可直接对 (3) 中 $z=u\mathsf h$ 求导得到。换成 $\delta$ 即 $\mathcal Pz=0$。又 $z=w^{1/6}$，故
$$
6(1-t)\delta\nu+(1-t)\nu^2-(1+2t)\nu=0.
\tag{9}
$$
展开 $\delta^2=\nu^2\mathsf N^2+(\delta\nu)\mathsf N$，并用 (9)，得到
$$
\mathcal P
=6(1-t)\nu^2\mathsf N^2
+\{6(1-t)\delta\nu-(1+2t)\nu\}\mathsf N
=\mathsf B(6\mathsf N^2-\mathsf N).
$$
这也直接核定 (8) 中的因子六及符号。$\square$

## 3. 完整 Γ 中的合法导子、基与准确 Smith

在 (1) 上定义
$$
\mathsf N(w)=w,\qquad
\mathsf N(\epsilon)=s\epsilon.
\tag{10}
$$
它确为整导子，因为三个定义关系分别被送到
$$
s(w^s-p\epsilon),\qquad
3s\epsilon^3,\qquad
(\ell+2s)w^\ell\epsilon^2.
$$
所以 $\delta=\nu\mathsf N$ 也保同一理想，(8) 在整个 $\Gamma_\ell$ 中成立。没有仅在第一块定义微分后忽略两次 carry。

$\Gamma_\ell$ 的准确有限自由基为
$$
w^j\quad(0\le j<s),\qquad
w^j\epsilon\quad(0\le j<s),\qquad
w^j\epsilon^2\quad(0\le j<\ell).
\tag{11}
$$
按 $n=j+is$ 标号，(11) 恰为 $n=0,\ldots,L-1$ 的连续 $L$ 个基向量，并且
$$
\mathsf N(w^j\epsilon^i)=(j+is)w^j\epsilon^i.
$$
令
$$
\mathcal L_\Gamma=\mathsf B^{-1}\mathcal P
=\mathsf N(6\mathsf N-1).
$$
其整矩阵已是对角矩阵
$$
\boxed{\lambda_n=n(6n-1),\qquad 0\le n<L.}
\tag{12}
$$

**定理 2。** 在 (11) 的完整长度中，$\mathcal P$ 和 $\mathcal L_\Gamma$ 的整 Smith 因子准确是
$$
\boxed{L-2\text{ 个单位},\quad 1\text{ 个 }p,\quad 1\text{ 个零}.}
\tag{13}
$$
零因子位于常量，唯一 $p$ 因子位于 $n=s$，即原 $\epsilon$ 行，且该对角元准确为 $sp$。

**证明。** $0<n<L<3s<p$，所以 $n$ 是单位。$6n-1$ 在此窗口为 $p$ 倍数，当且仅当 $n=s$：若 $6n-1=mp$，因 $p\equiv-1\pmod6$，必须 $m\equiv1\pmod6$；继 $m=1$ 后的 $m=7$ 已超出窗口。$n=s$ 时 $\lambda_s=sp$，其 $p$ 赋值恰为一。$\mathsf B$ 是第1节证明的完整整单位，左乘它不改变 Smith。$\square$

同样的证明适用于保原 $m_{13}$ 后的目标 $\Gamma_{\ell+13}$，其长度为 $L+13<3s$；相应单位数为 $L+11$，仍仅一个 $p$ 和一个零。这里两个算子的长度均已明确，并非从一个截断任意延长。

例如对任意实际目标 $f$，方程 $\mathcal PZ=f$ 在 $\Gamma_\ell$ 整可解，当且仅当 $\mathsf B^{-1}f$ 的常量为零，且其 $\epsilon$ 系数属于 $p\mathcal O$。其余各系数由 (12) 的单位唯一解出；$Z$ 的常量自由，$\epsilon$ 系数由除以 $sp$ 得到。这是目标算子的可解性，尚未要求 $Z$ 来自任何实际来源列。

## 4. regularization 的完整 forcing 恰在下一精度恢复

对每个整数 $n\ge0$，(8) 给
$$
\mathcal P(w^n)=n(6n-1)\mathsf B w^n.
$$
特别
$$
\boxed{\mathcal P(w^s)=sp\,\mathsf B w^s,\qquad
\mathcal P(\epsilon)=sp\,\mathsf B\epsilon.}
\tag{14}
$$
将 (2) 代入 (6)，得到原 regularized 轴的特征零身份
$$
\boxed{\mathcal P\log g
=\mathcal R-a s\,\mathsf B w^s.}
\tag{15}
$$
在同一原 $\Gamma_\ell$ 中，这准确成为
$$
\boxed{\mathcal P\log g
=\mathcal R-p a s\,\mathsf B\epsilon.}
\tag{16}
$$
这解释了为何该缺项在第一约化不可见，却在下一精度是一条明确的实际共振行。它不是任意选择的错误项，系数 $a s$ 为单位。

在普通 $t$ 系数中，令 $c_0=(w/t)(0)$，则 (15) 的首缺项为
$$
[t^s](\mathcal P\log g-\mathcal R)
=-a s\,c_0^s\in\mathcal O^\times.
\tag{17}
$$
已换标的 $b=1$ frame 给 $c_0=-1$；原 $b=17$ 给 $c_0=-1/17$。使用原 $w^s=p\epsilon$ 后，这同一个系数必须按 (16) 读取，不能仍当成模 $p$ 的免费目标单位。

现在保 R505 的真实因子整提升及正规分支 $\widetilde\psi$。在完整原目标中取
$$
\zeta=\log(Y_{\rm phys}/\widetilde\psi)
=\log(g/\widetilde\psi)+a\epsilon,
$$
$$
\mathcal F_{\widetilde F}
=\mathcal R-\mathcal P\log\widetilde\psi.
\tag{18}
$$
从 (14)、(16) 精确相消得
$$
\boxed{\mathcal P\zeta=\mathcal F_{\widetilde F}.}
\tag{19}
$$

这里 (19) 使用的是完整原 $\zeta$，不是在 $3C$ 中截到二次的坐标。至少在 R502 所需的模 $p^2$ 精度，有限 log 完全合法：该文范围
$1\le\ell\le r<h$、$s=2h+r-k$、$0\le k<\ell$ 给 $s<3h$，在 $\Gamma_\ell/p^2$ 中
$(p,w^h,\epsilon)^6=0$。每个总次数六的单项式，若含 $p^2$ 已零；若至多含一个 $p$，则由 $w^s=p\epsilon$ 或 $w^\ell\epsilon^2=0$ 归零。因此仅需阶数至五的 log/exp，分母均为单位。导子 (10) 保这个理想，故有限展开与 (19) 相容。

这个理由没有令 $\zeta^3$ 为零。原 $\bar\Gamma$ 中仍有 R502 的
$\zeta^3=3a(t^hu)^2\epsilon$ 活项；相应 $V_1$ 项也仍在。

若将 $\widetilde\psi(0)$ 归一为一，则 $\log(g/\widetilde\psi)$ 是原整普通级数。由 (19) 与 (12)，完整 forcing 的原共振坐标为
$$
\boxed{
[\epsilon]\bigl(\mathsf B^{-1}\mathcal F_{\widetilde F}\bigr)
\equiv p s a\pmod{p^2}.
}
\tag{20}
$$
因为 $\zeta$ 的 $\epsilon$ 系数模 $p$ 准确为 $a$，普通整级数在此行已有一个 $p$ 因子。(20) 对每个这样的实际因子成立，且保原 Gaussian 常数。它不将这个目标单位冒称原中央导数非零。

## 5. 原因子的常量归一由真实来源支付

保 R505 的有限自由格
$\mathcal H_1$、曲线 $C$、$\chi=-K_XC\ge2$ 及同预算包含
$$
\iota(H)=d^{-C_D}t^r\widetilde Q\,\widetilde F^2H\in\mathcal W_D.
$$
R505 在长度一的负度结论给 $\mathcal H_1\to k$ 的点值满射。故可取
$H_0\in\mathcal H_1$，使 $H_0(0,1)\in\mathcal O^\times$。于是
$$
\widetilde F_*=
\widetilde F-\frac{\widetilde F(0,1)}{H_0(0,1)}H_0
\tag{21}
$$
仍在同一格，约化仍为 $F$，并且 $\widetilde F_*(0,1)=0$。因为
$\widetilde F(0,1)\in p\mathcal O$，实际立方来源在模 $p^2$ 的改变由
$$
-3p\,
\frac{\widetilde F(0,1)}{pH_0(0,1)}
\,d^{-C_D}t^r\widetilde Q\,\widetilde F^2H_0
\tag{22}
$$
支付。这是原来源中的真实首次修正，不是免费移动曲线或删常数项。
其 mod $p$ carry 数据不变；若继续第三精度，(22) 必须带入同一原修正。

以下使用 (21) 的合法归一并仍记为 $\widetilde F$，故
$\widetilde\psi(0)=1$。R505 的接触 Bockstein 类及原全余核类不因这个实际提升选择而改变。

## 6. ξ 的前 q 项由同一代数 forcing 唯一计算

沿用 R505 的
$$
q=h-k,\qquad
\log(g/\widetilde\psi)=t^hu+p\xi\pmod{p^2},
\qquad \xi(0)=0.
\tag{23}
$$
(18) 的 forcing 完全来自原因子曲线，而不需要新的 theta 高系数。确切地，令
$$
\mathfrak u_{\widetilde F}
=-\left.\frac{t\widetilde F_t}{Y\widetilde F_Y}\right|_{\widetilde C}
=\delta\log\widetilde\psi.
$$
则
$$
\boxed{
\mathcal F_{\widetilde F}
=\mathcal R-
\{6(1-t)\delta-(1+2t)\}\mathfrak u_{\widetilde F}.
}
\tag{24}
$$
在曲线上 $\delta$ 由 $t\partial_t-t(\widetilde F_t/\widetilde F_Y)\partial_Y$ 作用；分母在 $P$ 是单位。这是同一实际提升的代数有理式，不是任取的局部 forcing。

$q\le h<s$，所以 (15) 的 Gaussian 缺项在此普通截断不出现，且 $\mathcal P(t^hu)$ 从 $t^h$ 起。因此
$$
[\mathcal F_{\widetilde F}]_{<q}\in p\mathcal O[t]/t^q.
$$
定义真实整商
$$
\Omega_{\widetilde F}
=\overline{\frac{[\mathcal F_{\widetilde F}]_{<q}}p}
\in t\,k[t]/t^q.
\tag{25}
$$

**定理 3。** 原 $\xi$ 在该窗口准确满足
$$
\boxed{\mathcal P\xi=\Omega_{\widetilde F}\pmod{t^q}.}
\tag{26}
$$
若 $\xi=\sum\xi_nt^n$、$\Omega=\sum\Omega_nt^n$，其唯一解为 $\xi_0=0$ 及
$$
\boxed{
\xi_n=
\frac{\Omega_n+2(n-1)(3n-2)\xi_{n-1}}
{n(6n-1)}
\quad(1\le n<q).
}
\tag{27}
$$

**证明。** (26) 来自 (15)、(23)、(25) 的同一实际除 $p$。直接计算
$$
[t^n]\mathcal P\xi
=n(6n-1)\xi_n-2(n-1)(3n-2)\xi_{n-1}.
$$
$n<q\le h<s$ 保证所有显示分母是单位，故可逐项唯一求解。$\square$

改变合法因子提升 $\widetilde F\mapsto\widetilde F+pH$ 时，根的真实一阶改变给
$$
\log\widetilde\psi_{\rm new}
=\log\widetilde\psi-pH/e\pmod{p^2},
\qquad e=(\mathcal EF)|_C.
$$
因此在同一截断中
$$
\Omega_{\widetilde F_{\rm new}}
=\Omega_{\widetilde F}+\mathcal P(H/e).
\tag{28}
$$
若同时保持常量归一则 $H(P)=0$。这与 R505 的
$\mu_F=e\xi$、$\mu_F\mapsto\mu_F+\bar E_q(H)$ 完全一致；没有将 forcing 作为新的自由参数。

## 7. 保原极帽的实际 Lagrange 转置

取 R498/R505 通过全部原列测试的真行
$$
\Phi=(A+B_1\zeta+C_2\zeta^2)\frac{dt\wedge d\zeta}{\zeta^3},
\qquad A-2t^huB_1\text{ 正则}.
$$
其 $A$ 层给 R505 的真实接触对偶，且 $\operatorname{pole}_P A\le q$。写
$$
\operatorname{pp}_P(Ae^3)
=\sum_{n=0}^{q-1}\alpha_n t^{-n-1}.
\tag{29}
$$
由于 $\xi_0=0$，$\alpha_0t^{-1}$ 不参与本次 $\xi$ 配对。

对 $\operatorname{Res}(\cdot)\,dt$，有 $\delta^*=-\delta-1$，所以准确的有限伴随为
$$
\boxed{
\mathcal P^*
=6(1-t)\delta^2+(13-22t)\delta+7-20t.
}
\tag{30}
$$
它在由 $t^{-2},\ldots,t^{-q}$ 张成的主部空间上为单位三角矩阵。具体地，置 $b_q=0$，按 $n=q-1,\ldots,1$ 定义
$$
\boxed{
b_n=
\frac{\alpha_n+2n(3n+1)b_{n+1}}{n(6n-1)},
\qquad
\Xi_A=\sum_{n=1}^{q-1}b_n t^{-n-1}.
}
\tag{31}
$$
于是
$$
\operatorname{pp}\mathcal P^*\Xi_A
=\operatorname{pp}(Ae^3)-\alpha_0t^{-1}.
$$
这可直接由
$$
\mathcal P^*t^{-n-1}
=n(6n-1)t^{-n-1}-2(n-1)(3n-2)t^{-n}
$$
逐项核定。尤其没有升高极帽，也没有引入新的 $p$ 分母。

因此 R502/R505 的整个 $\xi$ 配对可准确改写为
$$
\boxed{
3\operatorname{Res}Ae^3\xi\,dt
=
3\operatorname{Res}\Xi_A\,\Omega_{\widetilde F}\,dt.
}
\tag{32}
$$
左侧仍是原真行在完整 $\xi$ 向量上的值；右侧只读 (24) 的实际代数 forcing 整商及显示的有限三角逆。

若在 (28) 中换用另一合法归一，右侧变化为
$$
3\operatorname{Res}\Xi_A\mathcal P(H/e)\,dt
=3\operatorname{Res}Ae^2H\,dt=0,
$$
最后一步正是 R505 付过的真实接触对偶条件。所以 (32) 是提升选择无关的配对，不是挑某个 $\xi$ 后才成立的公式。

例如 R502 的固定实际因子
$\widetilde F=Y-\psi_{<15}(t)$ 在 $p=239$ 时有
$\psi_1=74$，原 $\rho_1=154/15$。因此
$$
[t]\mathcal F_{\widetilde F}
=154/3-5\cdot74=-4p/3,\qquad
\Omega_1=-4/3,\qquad
\xi_1=-4/15\equiv175\pmod{239}.
$$
这从同一个整因子直接恢复了已执行 R502 证书的非零实际 $\xi_1$。它没有说明接触余核类非零；该固定例的完整 $\xi$ 仍可在实际来源中被吸收。

## 8. 完整原 carrier 的算子运输

(8)–(13) 是目标算子的事实。对原
$$
M=c_*U_0m_{13}J
$$
不能省掉 $m_{13}$ 或将 $U_0$ 的导数设零。令 $\mathsf N_+$ 是长度 $L+13$ 的算子，$\mathsf N_-$ 是长度 $L$ 的算子。准确有
$$
\mathsf N_+m_{13}=m_{13}(\mathsf N_-+13).
\tag{33}
$$
把完整原单位的对数导数限制到所需相对目标，记
$$
\mathfrak u_0=\mathsf N_+\log U_0.
$$
由乘法法则，作为作用在同一个 $J(P)$ 上的算子身份，
$$
\boxed{
\mathsf N_+(6\mathsf N_+-1)M(P)
=
c_*U_0m_{13}
\Bigl[
(\mathsf N_-+13+\mathfrak u_0)
\bigl(6(\mathsf N_-+13+\mathfrak u_0)-1\bigr)
\Bigr]J(P).
}
\tag{34}
$$
方括号中是有次序的算子乘积，包含 $\mathsf N_-(\mathfrak u_0)$；不能将它当常系数二次式。$U_0$ 中来自 $P_{134}$ 的实际 Gaussian charge 与全部低、高项均在 $\mathfrak u_0$ 中。

$U_0$ 在较短目标中的限制与 (34) 相容，因为被短目标删去的项再乘 $w^{13}$ 后，也被长目标删去；这没有对 $m_{13}$ 作非整逆。原十三自由行和两条十三行 carry 因而原样保留。

## 9. 已恢复的共振与仍未支付的来源条件

(20) 已在原下一精度付出了明确的非零共振坐标；(32) 把 R505 的接触部分转成同一原因子的实际 forcing。但 R502 完整配对仍是
$$
\text{第一 carry 配对}
+\text{活 }f_2/C_2\text{ 配对}
-\Lambda_{\rm low}
+3\operatorname{Res}\Xi_A\Omega_{\widetilde F}\,dt.
\tag{35}
$$
其中 $\Lambda_{\rm low}$ 是原低行右逆的全部真实高尾。任何一项都没有由 (13) 自动落入或逃出原首像。

准确的剩余界限是：
$$
q=h-k\le (s-1)/2,\qquad \operatorname{pole}\Xi_A\le q.
$$
所以本篇有限转置本身仍不读取普通 $t^s$ 的首共振；它并未将低阶等号延长成全方程。完整目标中的共振 (20) 与原真行的接触读法 (32) 是两份已经付清的接口，尚须在**同一实际来源像**之间连接。

尤其没有证明
$\mathcal P(\operatorname{im}J)\subset\operatorname{im}J$，没有证明
$\mathsf B^{\pm1}$ 可作免费的来源乘子，也没有证明三条完整中央零传播到任意连接来源。若使用 R485/R486 的实际连接返回，必须继续支付其角条件、charge、真实零阶项及全部 carry。原
$K_2^{\rm red}(M)=\ker(\pi\beta_J)$、$G_2=C_2(J)/\overline H$ 和 R481 的同一修正第三精度均保留。

本篇不新增素数扫描。目标对角化、forcing 与有限转置均为上述全参数证明；固定 $p=239$ 的一阶数值只与已发布的 R502 实际来源核对，不被用于跨 $p$ 非零。
