# R599 — 原完整外矩形补偿、相邻深度差与原负五矩的准确返回

日期：2026-11-14。**状态：已证明。**

本篇保持 R594 的同一个五变量来源、同一个新六支测试，以及原
$Y-W$ 两个观察。矩形内的权差与矩形外的整个积分必须一起保留；
它们合成的完整补偿在新旧 $q$ 之间准确不变。

在同一个实际矩形上，未附 carry 权的原中央差有两条完整角级数。
首项涉及 $f_3$ 的负三矩，下一项恰是 R533/R540 原
$f_1$ 的负五矩 $I_1$。相邻两个深度的明确差准确消去首负三行，
给 $I_1$ 的整逼近，误差为 $p^{4n}$，极限准确为 $I_1$。
没有将负矩换成正矩，也没有把新补偿的任一部分置零。

## 1. 同一实际来源、同一原观察

沿用
[R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)、
[R540](R540-original-degree-six-schwartz-full-weight-and-negative-two-katz.md)、
[R553](R553-original-norm2-two-theta-source-and-mixed-unit-domain.md)、
[R572](R572-original-c-splitting-and-simple-pole-unit.md)、
[R590](R590-original-six-carry-branches-and-sole-b-fibre.md)、
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)
的原普通射线、全部原坏集和完整周期。特别
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times .
\tag{1}
$$
当前 $p\ge71$、$p\equiv7\bmod64$，$v_p(\kappa)=1$。

本篇整个来源仍是 R594 的
$$
\boxed{
\nu^\flat=\frac1{42}
\{\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
-\nu_{f_3}(Z)\otimes\nu_\Theta(Q)\}
\otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),
}
\tag{2}
$$
其中
$$
f_1=-x_\wp y_\wp\sigma^6,\qquad f_3=-y_\wp\sigma^6,\qquad
\Sigma=\sigma^2,\quad\Theta=x_\wp\sigma^2.
$$
所有因子采用同一个原 $\Omega$，系数 $1/42$ 原样保持。

为避免原 $q_n$ 与一个固定 CM 系数混名，置
$$
a_Z=\frac{-2+\omega}{2},\qquad a_Q=\frac{4+3\omega}{2}.
$$
实际两观察为
$$
\boxed{
Y=a_ZZ+a_QQ+2\delta r+c+2d,\qquad
W=a_ZZ+a_QQ+2\delta r+3\delta c+4d.
}
\tag{3}
$$
原 carry 行也保持
$$
F=\delta Z/6+(1-2\omega)Q/2+\omega^2r+c+(2+3\omega)d,
$$
$$
H_1=\omega^2Z/2+(\omega-1)Q/2+2r,\qquad G=13H_1+(3-2\omega)F.
\tag{4}
$$
令
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
       -1_{W\ {\rm unit}}\log\langle W\rangle\},\qquad
\mathcal T=J'_S-6\delta J'_T.
\tag{5}
$$
这里 $\nu^\flat(\ell)=\mathcal T$ 是原来源恒等式；
没有给 $\mathcal T$ 新的零假设。

R594 的真实矩形记为
$$
\boxed{
\mathscr R_n=\{Z\ {\rm unit},\ Q,r,c,d\in p^n\},\qquad
R_n=\int_{\mathscr R_n}\ell\,d\nu^\flat,\qquad n\ge1.
}
\tag{6}
$$
$R_n$ 是该同一矩形上的**未附 carry 权**积分；
它不是 R594 已证明赋值为 $n$ 的带权积分。

在 (6) 中，$F\equiv\delta Z/6\bmod p^n$；
原 $F$ 单位条件自动成立。
而 $Y\equiv W\equiv a_Z Z\bmod p^n$，且
$N(a_Z)=7/4$，故原两 Mellin 单位条件也都自动成立。
只在这个真实域内，
$$
\ell=d_p\log(Y/W).
\tag{7}
$$
矩形外继续使用 (5) 的两个分别的单位指示，不能沿用 (7)。

## 2. 四个真实深核心与完整两条角级数

R553 支付整个标准偶 $\mathcal S_2$ 的原核心 $\beta$，
所以 $\Sigma,\Theta$ 均有此核心；三个原 sigma 的核心同为
$\beta$。这些是 (2) 的实际独立张量因子。
因此 (6) 的四个深条件完整给
$$
\boxed{
\nu^\flat|_{\mathscr R_n}
=\beta^{4n}
[1,\kappa^n,\kappa^n,\kappa^n,\kappa^n]_*
(\nu^\flat|_{Z\ {\rm unit}}).
}
\tag{8}
$$
这没有移动 $Z$ 单位条件，也没有用四个因子的质量代替来源。
尤其 $\Theta$ 的质量一必须保持。

定义两个原 theta 函数
$$
\boxed{
\begin{aligned}
\mathcal A_5(t)
 &=\Sigma(a_Qt)\sigma(2\delta t)
       \{\sigma(t)\sigma(2t)-\sigma(3\delta t)\sigma(4t)\},\\
\mathcal B_3(t)
 &=\Theta(a_Qt)\sigma(2\delta t)
       \{\sigma(t)\sigma(2t)-\sigma(3\delta t)\sigma(4t)\}.
\end{aligned}}
\tag{9}
$$
它们是两条实际四输入差，分别来自 (2) 的 $\Sigma$ 与 $\Theta$
支；没有将 $f_1$ 与 $f_3$ 的两个不同伴随认成同一个数。
写
$$
A_m=[t^m]\mathcal A_5(t),\qquad B_m=[t^m]\mathcal B_3(t).
$$
全 $\mu_6$ 型给
$$
\mathcal A_5(t)=\sum_{j\ge0}A_{5+6j}t^{5+6j},\qquad
\mathcal B_3(t)=\sum_{j\ge0}B_{3+6j}t^{3+6j}.
\tag{10}
$$
式 (9) 始终按两个实际输出函数的差使用；不将其两个输出认成
同一单变量 theta degree。四输入来源与全 $\mu_6$ 型保持准确。

对 $k\ge1$ 记原单位负矩
$$
I_{1,k}=\int_{Z\ {\rm unit}}Z^{-k}\,d\nu_{f_1}(Z),\qquad
I_{3,k}=\int_{Z\ {\rm unit}}Z^{-k}\,d\nu_{f_3}(Z).
\tag{11}
$$
特别本篇的
$$
\boxed{I_1=I_{1,5}}
$$
就是 R533/R540 的原负五矩，不是正一矩或正五矩。
中间量 $I_3:=I_{3,3}$ 没有被赋零或新的算术参考身份。

**定理1（同一原矩形的完整负矩展开）。**
$$
\boxed{
\begin{aligned}
R_n=\frac{d_p\beta^{4n}}{42}\Bigg\{
&\sum_{j\ge0}
(4+6j)!\,\Omega^{5+6j}
A_{5+6j}a_Z^{-(5+6j)}
\kappa^{(5+6j)n}I_{1,5+6j}\\
-&\sum_{j\ge0}
(2+6j)!\,\Omega^{3+6j}
B_{3+6j}a_Z^{-(3+6j)}
\kappa^{(3+6j)n}I_{3,3+6j}
\Bigg\}.
\end{aligned}}
\tag{12}
$$
两个级数在每个 $n\ge1$ 一致收敛，所有负幂都在 (11)
显示的原单位域。

**证明。** 在 (8) 右边令
$$
L_Y=a_QQ+2\delta r+c+2d,\qquad
L_W=a_QQ+2\delta r+3\delta c+4d.
$$
同一个 $Z$ 单位域上准确有
$$
\log\frac{a_ZZ+\kappa^nL_Y}{a_ZZ+\kappa^nL_W}
=\sum_{m\ge1}\frac{(-1)^{m+1}\kappa^{mn}}
 {m\,a_Z^mZ^m}(L_Y^m-L_W^m).
\tag{13}
$$
因为 $a_Z$、$Z$ 单位、四输入都在 $\mathcal O$，
这是完整有界来源上可逐项积分的一致收敛级数。

$\Sigma$ 支的实际 $m$ 次矩差是 $m!\Omega^m A_m$，
$\Theta$ 支为 $m!\Omega^m B_m$。
(10) 所有非零次数都为奇数，因此 (13) 的符号都为正；
再保 (2) 第二支的原负号和 $1/42$ 即得 (12)。

实际四输入测度整有界，故
$$
v_p(m!\Omega^m A_m),\
v_p(m!\Omega^m B_m)\ge0.
$$
除去 log 中的 $m$ 后，唯一可损失的赋值为 $v_p(m)$。
所有 (11) 的单位负矩也整有界，所以 (12) 的项统一满足
$mn-v_p(m)$ 的下界，证明一致收敛。证毕。

## 3. 原负五行的固定单位系数

由真实首项
$\sigma(t)=t+O(t^7)$、$\Sigma(t)=t^2+O(t^8)$、
$\Theta(t)=1+O(t^6)$，准确有
$$
\boxed{
B_3=b_3=4\delta(1-6\delta)=76+8\omega,\qquad
A_5=a_Q^2b_3=103+269\omega.
}
\tag{14}
$$
为核对两个不同源的矩常数：
$\Theta$ 支的三次矩为 $6b_3\Omega^3$；
$\Sigma$ 支的五次矩为 $120a_Q^2b_3\Omega^5$，
后者已包含 $\Sigma$ 的真实二次矩 $2\Omega^2$。

置
$$
\boxed{
c_3=-\frac{b_3}{21a_Z^3}
=\frac{10400+11008\omega}{7203},\qquad
c_5=\frac{4a_Q^2b_3}{7a_Z^5}
=\frac{4312960+1031168\omega}{117649}.
}
\tag{15}
$$
因此 (12) 给全部正确标量的两项式
$$
\boxed{
R_n=\beta^{4n}d_p
\{c_3\Omega^3\kappa^{3n}I_3
 +c_5\Omega^5\kappa^{5n}I_1\}
+p^{9n}\mathcal O .
}
\tag{16}
$$
这里 $f_3$ 支的下一次数为九，$f_1$ 支的下一次数为十一。
对所有剩余 $m\ge9$，
$mn-v_p(m)\ge9n$（当前 $p\ge71$），
所以 (16) 的整条尾界包括全部高负矩，无遗漏。

固定系数的范数为
$$
\boxed{
Nc_3=\frac{2^{10}\cdot109}{3\cdot7^5},\qquad
Nc_5=\frac{2^{14}\cdot3\cdot13^2\cdot109}{7^7}.
}
\tag{17}
$$
当前坏集已经排 $2,3,7,13$，而
$109\equiv45\bmod64$，不可能属于原
$p\equiv7\bmod64$ 射线。
所以 $c_3,c_5$ 在每个当前普通处都是单位。
本篇不增加射线，也不增加固定坏集。

(16) 的量词不能改成 $R_n$ 恒非零：$I_3,I_1$ 尚无这里可用的
非零断言。下面准确消去 $I_3$，而不是先猜它等于零。

## 4. 相邻两层准确读取原 I1

定义同一个原观察的相邻深度差
$$
\boxed{\mathfrak D_n=R_{n+1}-\beta^4\kappa^3R_n.}
\tag{18}
$$
这里的 $\mathfrak D_n$ 是同一原矩形积分的相邻深度差。

**定理2（原负五矩的整返回）。** 令
$$
\boxed{
\mathcal I_n=
\frac{\mathfrak D_n}
 {d_pc_5\Omega^5\beta^{4(n+1)}
       \kappa^{5n+3}(\kappa^2-1)}.
}
\tag{19}
$$
则
$$
\boxed{
\mathcal I_n\in\mathcal O,\qquad
\mathcal I_n-I_1\in p^{4n}\mathcal O,\qquad
\lim_{n\to\infty}\mathcal I_n=I_1 .
}
\tag{20}
$$
其中除显示的 $\kappa^{5n+3}$ 外，(19) 分母全部是单位。

**证明。** 在 (12) 中，对一个次数为 $m$ 的真实项，
(18) 产生准确因子
$$
\beta^{4(n+1)}\kappa^{mn}(\kappa^m-\kappa^3).
\tag{21}
$$
$m=3$ 整条为零，包括其全部原周期和 $I_3$。
$m=5$ 给
$$
d_pc_5\Omega^5\beta^{4(n+1)}
\kappa^{5n+3}(\kappa^2-1)I_1 .
\tag{22}
$$
每个剩余 $m\ge9$ 在除去 (19) 分母后，除固定单位外有
$$
\kappa^{(m-5)n}\frac{\kappa^{m-3}-1}{m}
\times\{\text{整的实际正矩与原单位负矩}\}.
$$
其赋值至少 $(m-5)n-v_p(m)\ge4n$，且一致趋于无穷。
这证明 (20)，并证明 $\mathcal I_n$ 的整性。
$\kappa^2-1$ 为单位，其他单位由 (1)、(17) 支付。证毕。

这给真实可比较的两个范围：
若 $I_1=0$，则
$$
\boxed{v_p(\mathfrak D_n)\ge9n+3\quad(n\ge1).}
\tag{23}
$$
若 $I_1\ne0$，则在 $4n>v_p(I_1)$ 时准确有
$$
\boxed{v_p(\mathfrak D_n)=5n+3+v_p(I_1).}
\tag{24}
$$
这里没有声称原指定 $I_1$ 必定非零；(23) 与 (24)
都是同一实际补偿上可以使用的精确条件。

## 5. 保同一个 W 权：整个外矩形与内部权差

现在回到 R594 原新的
$\widetilde{\mathcal W}_n(F,G)$，保其全部七实际余类矩、
全部 $\lambda,\kappa$ 与整右逆系数。
定义两个完整实际积分
$$
\boxed{
\begin{aligned}
O_n&=\int_{\{F\ {\rm unit}\}\setminus\mathscr R_n}
                 \widetilde{\mathcal W}_n\,\ell\,d\nu^\flat,\\
K_n&=\int_{\mathscr R_n}
                 (\widetilde{\mathcal W}_n-\beta^n)\ell\,d\nu^\flat.
\end{aligned}}
\tag{25}
$$
$O_n$ 使用原 (5) 的两个分别的单位条件；
没有用 $Y,W$ 在矩形内均单位的事实扩展到它。
$K_n$ 是显示的整个测试差，不是以总质量代替
$\widetilde{\mathcal W}_n$。

R594 的原完整四输出返回给
$$
\int_{\{F\ {\rm unit}\}}
       \widetilde{\mathcal W}_n\ell\,d\nu^\flat=\beta^n\mathcal T.
$$
因此这两个实际补偿的准确合并为
$$
\boxed{
\mathcal E_n:=\beta^{-n}(O_n+K_n)=\mathcal T-R_n .
}
\tag{26}
$$
式 (26) 保整个矩形外域和矩形内权差，未删任何一个原观察。

还有一个与测试选择有关的完整结论。
若把 (25) 中的新 $\widetilde{\mathcal W}_n$
换回 R590 的旧 $\mathcal W_n$，则由同一个完整四输出返回，
合成后的 $\mathcal E_n$ **准确相同**。
两个 $O_n$ 可以改变，两个 $K_n$ 也可以改变；
只有它们在 (26) 中的完整和不变。
因此 R594 的新局部补偿没有改变本篇返回的原负五矩。

将 (26) 代入 (18)，得到直接使用原全部补偿的身份
$$
\boxed{
\mathfrak D_n=
(1-\beta^4\kappa^3)\mathcal T
-\mathcal E_{n+1}
+\beta^4\kappa^3\mathcal E_n .
}
\tag{27}
$$
结合 (19)–(20)，原 $I_1$ 的完整返回为
$$
\boxed{
I_1=
\lim_{n\to\infty}
\frac{
(1-\beta^4\kappa^3)(J'_S-6\delta J'_T)
-\mathcal E_{n+1}+\beta^4\kappa^3\mathcal E_n}
{d_pc_5\Omega^5\beta^{4(n+1)}
       \kappa^{5n+3}(\kappa^2-1)} .
}
\tag{28}
$$
每个有限 $n$ 的误差准确在 $p^{4n}\mathcal O$。
所有项都在 (2) 的同一个真实来源、同一个原 $Y/W$ 上；
$\mathcal E_n$ 不是独立新负矩或新曲线中央。

## 6. 两个原中央同时为零时的准确补偿要求

只有在作原反证假设 $J'_S=J'_T=0$ 时，
(26) 才可写成
$$
\mathcal E_n=-R_n,
$$
且 (27) 的显示 $\mathcal T$ 项才为零。
于是 (16) 给同一个全补偿的准确展开
$$
\boxed{
\mathcal E_n=
-\beta^{4n}d_p
\{c_3\Omega^3\kappa^{3n}I_3
 +c_5\Omega^5\kappa^{5n}I_1\}
+p^{9n}\mathcal O .
}
\tag{29}
$$

这还可以和 R594 已付的局部值直接比较。
记
$$
Q_n=\int_{\mathscr R_n}
           \widetilde{\mathcal W}_n\ell\,d\nu^\flat.
$$
R594 已证明 $v_p(Q_n)=n$，而 (16) 无条件给
$R_n\in p^{3n}\mathcal O$。
因此
$$
\boxed{K_n=Q_n-\beta^nR_n,\qquad v_p(K_n)=n}
\tag{30}
$$
对每个 $n\ge1$ 成立。
在上述两原中央同时为零的假设下，还准确有
$$
O_n=-Q_n,\qquad v_p(O_n)=n .
\tag{31}
$$
所以这里两个各为 $n$ 阶的实际项的确必须先抵消到至少 $3n$，
再经 (27) 的相邻深度差读到 $5n+3$ 阶的原 $I_1$。
这不许可把其中一项当成零或更高阶；(29) 的全部补偿本身
正是需要支付的条件。

若原 $I_1$ 也为零，则真实必要条件为
$$
-\mathcal E_{n+1}+\beta^4\kappa^3\mathcal E_n
\in p^{9n+3}\mathcal O .
\tag{32}
$$
若 $I_1\ne0$，同一差的准确赋值由 (24) 给出。
这将原指定负矩直接接回了完整算术测试的补偿；
没有把“负矩为零”排除，也没有从 R594 一个矩形非零
推成整个 $\mathcal T$ 非零。主目标仍未完成。

## 7. 精确证书

- [check-r599-original-complement-and-negative-five-return.js](../scripts/check-r599-original-complement-and-negative-five-return.js)
- [check-r599-original-complement-and-negative-five-return.json](../scripts/check-r599-original-complement-and-negative-five-return.json)

脚本用自含 BigInt 的 $\mathbf Q(\omega)$ 算术验证
实际两观察的四个深系数、完整最低三次与五次矩、
(14)–(17) 的全部精确常数和固定单位范数。
全文的来源核心、完整级数、无穷深度差、误差界及
(25)–(32) 的实际补域量词由上述证明支付。
没有重算 R594 已付右逆，也没有增加独立复跑或审查门槛。
