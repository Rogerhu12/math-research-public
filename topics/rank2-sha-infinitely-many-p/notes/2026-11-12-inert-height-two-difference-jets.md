# 惰性高度二与固定差分逆像：半径改善及首个共振系数

日期：2026-11-12。状态：**下述系数与图像大小命题已证明；
尚未证明非目标有限处的大小损失可求和。**

固定 $a=69$ 和 R28 的零线性系数解
$$
q(z)=\log\Phi(\exp_Ez)=\sum_{k\ge3,\ k\text{ 奇}}b_kz^k,
\qquad H_m(z)=\sum_{k\ge3,\ k\text{ 奇}}
\frac{b_kz^k}{(a^k-a)^m},
\qquad F_m(t)=\exp H_m(\log_Et).
\tag{1}
$$
主要关心 $m=3$，但结论对任意固定 $m\ge1$ 成立。
设 $p\equiv3\pmod4$ 为好素数，$p\nmid a$；排除固定有限多个
使 $\Phi$ 在原点没有整单位展开的素数。
在 $K=\mathbb Q(i)$ 的惰性素点 $v$ 处，以 $v_p(p)=1$ 正规化。

## 1. 高度二实际给出的正向系数界

直接核查 Coates–Liang–Sujatha，
*The Tate–Shafarevich group for elliptic curves with complex multiplication II*，
Milan J. Math. 78 (2010)，
[原文](https://arxiv.org/abs/1005.4206)，
Theorem 2.1、式 (29)–(32)、Lemma 2.6。

惰性处的形式群与 $[\pi](w)=\pi w+w^{p^2}$ 的 Lubin–Tate 群
在 $\mathcal O_v$ 上同构。其对数在次数小于 $p^2$ 时只有一次项：
比较 $\nu(\pi w+w^{p^2})=\pi\nu(w)$ 的 $w^n$ 系数，
对 $2\le n<p^2$ 得 $(\pi^n-\pi)\nu_n=0$，故 $\nu_n=0$。
一次项为单位；与整同构复合可知 $\exp_E(z)$ 与 $\log_E(t)$
在次数小于 $p^2$ 的截断中均为整级数，且互为复合逆。
这也是 CLS Lemma 2.6 的低阶 Taylor 系数整性的具体内容。

所以
$$
\varphi(z)=\Phi(\exp_Ez)\pmod{z^{p^2}}
\quad\text{具有整系数}.
\tag{2}
$$
又 $\varphi(0)=1$、$\varphi'(0)=0$，实际上 $\varphi-1$ 从三次开始。
当 $k\le p$ 时，$[z^k]\log\varphi$ 中至多出现
$(\varphi-1)^r/r$，其中 $r\le k/3<p$。
因此
$$
\boxed{\ b_k\in\mathcal O_v\qquad(0\le k\le p).\ }
\tag{3}
$$

对全部奇数 $k\ge3$，R19 的矩公式与 CLS Theorem 2.1 给
$$
v_p(b_k)
\ge \left\lfloor\frac{kp}{p^2-1}\right\rfloor-1-v_p(k!).
\tag{4}
$$
这里 CLS 排除的同余类 $k\equiv p+1\pmod{p^2-1}$ 为偶数类，
故不会出现；$2$ 与 $f^k$ 都是局部单位。
由 $v_p(k!)\le k/(p-1)$ 得较粗但方便的统一界
$$
v_p(b_k)\ge-\frac{k}{p^2-1}-2.
\tag{5}
$$
这准确体现高度二相较高度一的半径改善。

## 2. 差分对数仍有高度二半径；图像大小却另需有限 jet 控制

记
$$
d_p=\operatorname{ord}_{\mathbb F_p^\times}(a),\qquad
c_p=v_p(a^{d_p}-1).
$$
若 $d_p\mid k-1$，则
$v_p(a^k-a)=c_p+v_p((k-1)/d_p)$；否则该赋值为零。
因此对固定 $p$，除以 $(a^k-a)^m$ 只增加 $O_p(\log k)$ 的分母赋值。
式 (5) 遂给 $H_m$ 在 $z$ 坐标中的收敛半径下界
（此处用 $|p|=p^{-1}$）
$$
R_p(H_m)\ge p^{-1/(p^2-1)}.
\tag{6}
$$
其负对数对惰性素数可求和。

但是 (6) 是**对数级数的收敛半径**，不是 $F_m$ 的形式图像大小。
它既不控制低阶小除数，也不能直接穿过乘法指数得到图像大小界。
下面给出对实际 $\Phi$ 可用的精确有限 jet 条件。

## 3. 首个奇共振权的必要整性条件

令
$$
D_p=\operatorname{lcm}(d_p,2),\qquad k_p=D_p+1.
$$
因为 $d_p\mid p-1$，有 $D_p\mid p-1$，所以
$$
3\le k_p\le p.
\tag{7}
$$
$k_p$ 是至少三的奇数权中，首个满足 $p\mid a^k-a$ 的权。
而 $D_p/d_p$ 为一或二，故
$$
v_p(a^{k_p}-a)=c_p.
\tag{8}
$$

**命题。** 若
$$
v_p(b_{k_p})<m c_p,
\tag{9}
$$
则 $F_m(t)$ 的次数小于 $k_p$ 的系数全为整，且
$$
v_p([t^{k_p}]F_m)=v_p(b_{k_p})-m c_p<0.
\tag{10}
$$

**证明。** 对所有奇数 $3\le k<k_p$，式 (3) 给 $b_k$ 整，
而 $a^k-a$ 是单位；偶数系数和一次系数为零。
所以 $H_m$ 在次数小于 $k_p$ 的系数均整，
其第 $k_p$ 个系数的赋值由 (8) 为 $v_p(b_{k_p})-mc_p$。

因为 $H_m$ 从三次开始，$[z^k]\exp H_m$ 中的非线性项只涉及
$H_m^r/r!$，其中 $r\le k/3<p$，只要 $k\le k_p\le p$。
这些阶乘是单位。故次数小于 $k_p$ 的指数系数均整；
在第 $k_p$ 次，所有非线性项只涉及较低次的整系数，
不能抵消唯一的非整线性项 $[z^{k_p}]H_m$。这证明 $z$ 坐标版的 (10)。

最后，第 1 节已证明 $z=\log_E(t)$ 到次数 $p$ 的截断为整，
且一次系数为一。因此复合回 $t$ 坐标，第一个非整系数的赋值不变。
得到 (10)。$\square$

特别地，$F_m\in\mathcal O_v[[t]]$ 必须满足
$$
b_{k_p}\in p^{m c_p}\mathcal O_v.
\tag{11}
$$
这是真正与本题固定 $\Phi$ 有关的额外条件；高度二本身只给式 (3)，
并没有给出 (11)。

## 4. 该系数如何控制 Bost 图像大小

令 $e_p=mc_p-v_p(b_{k_p})>0$，并假设 (9)。
在 $E\times\mathbb A^1$ 的整局部坐标中，把图像的第二坐标由
$F_m-1$ 改成 $F_m-1+t$。这个整坐标变换保持形式曲线大小，
并使第二坐标的一次系数为一；第 $k_p$ 次非整系数仍有赋值 $-e_p$。

Bost–Chambert-Loir，*Analytic curves in algebraic varieties over number fields*，
[arXiv:math/0702593v3](https://arxiv.org/abs/math/0702593v3)，
Proposition 3.5(2)，用第一 Newton 斜率给出
$$
S_v(\widehat{\operatorname{graph}}F_m)
\le |p|_v^{e_p/(k_p-1)}.
\tag{12}
$$
按该文全局乘积公式的正规化，惰性处 $|p|_v=p^{-2}$；
若只用 $\mathbb Q_p$ 正规化 $|p|=p^{-1}$，右边相应为
$p^{-e_p/D_p}$。
因此即使 (6) 的半径损失为 $O(\log p/p^2)$，
首个共振 jet 若未被取消，仍允许图像损失达到 $\log p/p$ 或更大。
本文没有证明 (9) 对无穷多个 $p$ 成立；这里指出并证明需要控制的准确系数。

## 5. 两项不能互相替代的事实

一方面，高度二确实消除了坐标变换在低于 $p^2$ 的截断内的分母。
另一方面，小除数可以早在 $k_p\le p$ 出现。
例如仅为检验这项逻辑，在同一曲线上取另一个固定有理函数
$$
R(t)=\frac{1+t^3}{1-t^3}.
$$
它满足 $R(0)=1$、零线性对数系数和奇对称。
在惰性素数 $p=7$ 处，$69\equiv-1\pmod7$，
$d_p=2$、$k_p=3$、$c_p=1$，且对数的三次系数为 $2$。
相应 $m$ 次差分逆像的三次系数赋值恰为 $-m$。
这是一个点态反例，说明“形式群高度二”本身不推出所需图像大小；
它不是本题的 $\Phi$，也没有否定某个排除有限素数后的估计。

也不能反过来把 $\log\Phi$ 中出现的乘法对数分母自动当作 $F_m$
的分母：$m=0$ 时取指数就回到整函数 $\Phi$，这些分母完全相消。
对 $m>0$，指数中的相消须在差分除法后重新核算；第 3 节正是在
第一个可能非整 jet 上完成了这一核算，没有把对数半径当成图像大小。

## 6. 当前能够用于后续证明的输入

惰性处已经有可求和的 $H_m$ 对数半径下界 (6)。
若要把它用于 Bost 或更弱的 arithmeticity 判据，仍需实际控制
共振系数及指数的整性相消；最先遇到的是 (11)。
R9 的惰性强制因子在 $k_p\le p$ 时没有给出所需的 $mc_p$ 深度。
目前没有得到这些非目标有限处的可求和图像大小界，
因此也尚不能从这项高度二改进推出一个可用的 Herblot $\alpha$-arithmetic 上界。
