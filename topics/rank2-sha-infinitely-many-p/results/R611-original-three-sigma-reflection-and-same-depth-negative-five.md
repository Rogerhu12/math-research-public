# R611 — 原三 sigma 反射、同深负五返回与全部 carry 转置

日期：2026-11-14。**状态：已证明。**

本篇使用 R599–R605 的同一个五变量来源。
它的首两因子有一个完整三 sigma 乘积表达，给出实际有理反射
$\tau$，在整个来源上准确为负号。这个变换把原矩形送进 R605
保留的三域外补集；其与原矩形和两个核心像的交域全部明确。

原测试 $\ell\circ\tau-c_\tau\ell$ 的全积分仍是原 $S/T$
中央差的固定单位倍数。在同一个深度 $n$，它的负三首行准确相消，
原负五矩 $I_1$ 的系数则是当前整个射线上的固定单位。
因此可以在同深度直接读取原 $I_1$，误差为 $p^{4n}$。
原 carry 必须连同 $F,G$ 和七个余类矩全部转置；本篇逐项保留。

## 1. 同一个五变量来源和原算术测试

沿用
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)、
[R599](R599-original-complement-and-negative-five-return.md)、
[R601](R601-original-q-tensors-complete-y-w-cores-and-fifteen-source-spectrum.md)、
[R605](R605-original-two-core-images-and-complete-complement.md)
的全部原规范：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times .
\tag{1}
$$
当前 $p\ge71$、$p\equiv7\bmod64$，以及此前所有固定坏集均保持。
本篇第 1–6 节不增加射线或稀疏坏集。

物理坐标为 $\mathbf x=(Z,Q,r,c,d)^t$，来源仍是
$$
\nu^\flat=\frac1{42}
(\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
 -\nu_{f_3}(Z)\otimes\nu_\Theta(Q))
\otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),
\tag{2}
$$
其中 $f_1=-x_\wp y_\wp\sigma^6$、$f_3=-y_\wp\sigma^6$、
$\Sigma=\sigma^2$、$\Theta=x_\wp\sigma^2$。
置
$$
a_Z=(-2+\omega)/2,\qquad a_Q=(4+3\omega)/2,
$$
$$
Y=a_ZZ+a_QQ+2\delta r+c+2d,\qquad
W=a_ZZ+a_QQ+2\delta r+3\delta c+4d .
\tag{3}
$$
原两个观察分别带自己的单位条件：
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
          -1_{W\ {\rm unit}}\log\langle W\rangle\},\qquad
\mathcal T=\nu^\flat(\ell)=J'_S-6\delta J'_T .
\tag{4}
$$
原矩形为
$$
\mathscr R_n=\{Z\ {\rm unit},\ Q,r,c,d\in p^n\},\qquad n\ge1.
\tag{5}
$$

## 2. 完整三 sigma 恒等式与真实反射

在生成函数变量 $(z,q)$ 上，原加法式和二倍公式给
$$
\frac{\sigma(z+q)\sigma(z-q)}{\sigma(z)^2\sigma(q)^2}
=x_\wp(q)-x_\wp(z),\qquad
\sigma(2z)=-2y_\wp(z)\sigma(z)^4 .
$$
因此准确有
$$
\boxed{
f_1(z)\Sigma(q)-f_3(z)\Theta(q)
=-\frac12\sigma(2z)\sigma(z+q)\sigma(z-q).
}
\tag{6}
$$
式 (2) 的整个生成函数于是为
$-\sigma(2z)\sigma(z+q)\sigma(z-q)
 \sigma(r)\sigma(c)\sigma(d)/84$。
所有常数和原正负号均保持。

定义实际五变量反射
$$
\boxed{
\tau(Z,Q,r,c,d)
=\left(\frac{Z-3Q}{2},-\frac{Z+Q}{2},r,c,d\right).
}
\tag{7}
$$
它满足 $\tau^2=I$、$\det\tau=-1$，并保持
$G_5=\operatorname{diag}(6,2,1,1,1)$。
其全部分母在当前处为单位。

物理 push 在生成函数中作用为 $\tau^t$。
(6) 的三条实际 sigma 参数行因而准确变为
$$
(2z,\ z+q,\ z-q)
\longmapsto(z-q,\ -z-q,\ 2z).
$$
它们只是原三因子的一个置换和一个负号；没有格平移或未记录的
Gaussian/flat 相位。因此在整个原有界 Amice 来源上
$$
\boxed{\tau_*\nu^\flat=-\nu^\flat.}
\tag{8}
$$
这里使用完整生成函数恒等式，并非只比较质量或几个 jet。

原观察的真实转置恰为
$$
\boxed{
\begin{aligned}
Y_\tau:=Y\circ\tau&=\bar a_ZZ+\bar a_QQ+2\delta r+c+2d,\\
W_\tau:=W\circ\tau&=\bar a_ZZ+\bar a_QQ+2\delta r+3\delta c+4d.
\end{aligned}}
\tag{9}
$$
(9) 只把这两个固定 CM 系数变成共轭。
这是有理物理矩阵 (7) 的结果，没有共轭整个测度、
没有交换 $\pi_0,\bar\pi_0$，$\delta,\Omega$ 及原单位负矩均未改变。

## 3. 实际外矩形及与三个旧域的准确交域

令
$$
\mathscr A_n=\tau\mathscr R_n.
$$
因为 $\tau^{-1}=\tau$，其完整逆域是
$$
\frac{Z-3Q}{2}\ {\rm unit},\quad
-\frac{Z+Q}{2}\in p^n,\quad r,c,d\in p^n .
$$
在当前处等价地
$$
\boxed{
\mathscr A_n=
\{Z,Q\ {\rm unit},\ Z+Q\in p^n,\ r,c,d\in p^n\}.
}
\tag{10}
$$
在这个域上，保原而非转置的观察：
$$
Y\equiv W\equiv-(3+\omega)Z\pmod{p^n}.
$$
原 carry 行
$$
F=\delta Z/6+(1-2\omega)Q/2+\omega^2r+c+(2+3\omega)d
$$
也满足
$$
F\equiv\frac{-1+4\omega}{3}Z\pmod{p^n},\qquad
N\!\left(\frac{-1+4\omega}{3}\right)=7/3.
\tag{11}
$$
所以 $Y,W,F$ 都是单位。

原矩形 (5) 的 $Q$ 深而 (10) 的 $Q$ 单位，故二者不交。
R601 的两个核心像分别满足
$v_p(Y)=1,W$ 单位及 $Y$ 单位、$v_p(W)=4$，
因此它们也都与 (10) 不交。
于是
$$
\boxed{
\mathscr A_n\subset
\mathcal O^5\setminus
(\mathscr R_n\sqcup\mathscr R_n^Y\sqcup\mathscr R_n^W).
}
\tag{12}
$$
这是对 R605 真正余域的一个明确新支；并未删除其余补集。

对任意完整有界测试 $f$，(8) 给
$$
\boxed{
\int_{\mathscr A_n}f\,d\nu^\flat
=-\int_{\mathscr R_n}f(\tau\mathbf x)\,d\nu^\flat .
}
\tag{13}
$$
原 $F,G$、所有 Mellin 单位条件和依赖隐藏变量的测试都按 (7)
一起转置。

## 4. 完整原算术总行与同深负三消去

记
$$
R_n=\int_{\mathscr R_n}\ell\,d\nu^\flat,\qquad
R_n^\tau=\int_{\mathscr R_n}\ell(\tau\mathbf x)\,d\nu^\flat.
$$
由 (9)，在 (5) 中两组观察都为单位；
它们各自可展开为该组原 log 比。
R599 的完整两条负矩级数因此逐项成立，
$R_n^\tau$ 的唯一替换是
$a_Z\mapsto\bar a_Z,\ a_Q\mapsto\bar a_Q$。
其中 $b_3=4\delta(1-6\delta)=76+8\omega$ 和所有原负矩仍不变。

保原
$$
I_3=\int_{Z\ {\rm unit}}Z^{-3}\,d\nu_{f_3},\qquad
I_1=\int_{Z\ {\rm unit}}Z^{-5}\,d\nu_{f_1}.
$$
这里 $I_1$ 正是 R533/R540 的指定负五矩。
其首两行准确为
$$
\begin{aligned}
R_n&=d_p\beta^{4n}
(c_3\Omega^3\kappa^{3n}I_3+c_5\Omega^5\kappa^{5n}I_1)
+p^{9n}\mathcal O,\\
R_n^\tau&=d_p\beta^{4n}
(c_3^\tau\Omega^3\kappa^{3n}I_3+
 c_5^\tau\Omega^5\kappa^{5n}I_1)+p^{9n}\mathcal O,
\end{aligned}
\tag{14}
$$
其中
$$
c_3=-\frac{b_3}{21a_Z^3},\quad
c_5=\frac{4a_Q^2b_3}{7a_Z^5},\quad
c_3^\tau=-\frac{b_3}{21\bar a_Z^3},\quad
c_5^\tau=\frac{4\bar a_Q^2b_3}{7\bar a_Z^5}.
$$
设
$$
\boxed{
c_\tau=(a_Z/\bar a_Z)^3
=\frac{-323-360\omega}{343},\qquad
\epsilon_\tau=c_5^\tau-c_\tau c_5
=\frac{6789120+4239360\omega}{117649}.
}
\tag{15}
$$
则 $c_3^\tau=c_\tau c_3$ 整条准确相消。
全部高项仍是 R599 的真实两条角级数，
$\Theta$ 支下一次为九，$\Sigma$ 支下一次为十一，
其统一界 $mn-v_p(m)\ge9n$ 保全部尾项。

现在定义同一个完整实际测试
$$
\boxed{g=\ell\circ\tau-c_\tau\ell.}
\tag{16}
$$
在 (5) 之外仍保四个分别的单位指示，不把它写成一个无条件
log 比。由 (8)，全算术总行准确是
$$
\boxed{\nu^\flat(g)=-(1+c_\tau)\mathcal T.}
\tag{17}
$$
更强地，对整个原 Mellin 变量，(8) 分别给
$J_{Y_\tau}(u)=-J_S(u)$、$J_{W_\tau}(u)=-6\delta J_T(u)$；
(17) 是其同一个导数行。
这里没有新增未知来源中央。

令 $D_n^\tau=\int_{\mathscr R_n}g\,d\nu^\flat$，则
$$
\boxed{
D_n^\tau=d_p\beta^{4n}\epsilon_\tau\Omega^5
                \kappa^{5n}I_1+p^{9n}\mathcal O .
}
\tag{18}
$$
所有新系数的单位性由固定范数支付：
$$
\boxed{
N(c_\tau)=1,\quad
N(1+c_\tau)=400/343,\quad
N(\epsilon_\tau)=\frac{2^{22}3^2 5^2\cdot109}{7^9}.
}
\tag{19}
$$
$109\equiv45\bmod64$ 不在当前原射线中；
其余分子和分母坏素数早已排除。
所以 (18) 的负五系数与 (17) 的全算术标量在当前整个射线上
都是单位，无需新的密度删除。

## 5. 同一个完整补域的同深负五返回

保真正完整补域积分
$$
B_n^\tau=\int_{\mathcal O^5\setminus\mathscr R_n}
                         g\,d\nu^\flat .
\tag{20}
$$
(16) 的四个单位条件和所有真实观察都保留。
由 (17)，准确有
$$
D_n^\tau=-(1+c_\tau)\mathcal T-B_n^\tau.
$$
因此定义
$$
\boxed{
\mathcal I_n^\tau=
\frac{-(1+c_\tau)(J'_S-6\delta J'_T)-B_n^\tau}
     {d_p\epsilon_\tau\Omega^5\beta^{4n}\kappa^{5n}} .
}
\tag{21}
$$

**定理1。** 对每个当前普通素数和每个 $n\ge1$，
$$
\boxed{
\mathcal I_n^\tau\in\mathcal O,\qquad
\mathcal I_n^\tau-I_1\in p^{4n}\mathcal O,\qquad
\lim_{n\to\infty}\mathcal I_n^\tau=I_1.
}
\tag{22}
$$

这由 (18)、(19) 直接证明。
它使用同一个深度的两个真实观察；负三矩完全消去，
没有先给 $I_3$ 赋零。
若 $I_1=0$，(21) 的整个实际分子属于 $p^{9n}\mathcal O$；
若 $I_1\ne0$，则当 $4n>v_p(I_1)$ 时其准确赋值是
$$
5n+v_p(I_1).
\tag{23}
$$
这并未证明 $I_1\ne0$。
原两中央同时为零时，只能把 (21) 的显示中央项消去，
留下同一个 $B_n^\tau$；不能把 (20) 一并删去。

## 6. 同一个原 carry 的全部转置与两项补偿

令 $w_n(\mathbf x)=\widetilde{\mathcal W}_n(F,G)$，
按 R594 的原定义在 $F$ 非单位处取零。
所有完整 $\lambda,\kappa$、九乘二十整右逆系数和七个实际
$B_C$ 余类矩均保持。

实际转置参数为
$$
\boxed{
\begin{aligned}
F_\tau=F\circ\tau
 &=\frac{-1+4\omega}{6}Z-\frac12Q+\omega^2r+c+(2+3\omega)d,\\
G_\tau=G\circ\tau
 &=\frac{5-17\omega}{6}Z+\frac{23+15\omega}{2}Q
 +(21-3\omega)r+(3-2\omega)c+(12+11\omega)d .
\end{aligned}}
\tag{24}
$$
故 $w_n\circ\tau=\widetilde{\mathcal W}_n(F_\tau,G_\tau)$；
特别每个旧 $b_{n,s}(F)$ 必须变为
$$
b_{n,s}(F_\tau)=
 \int_{C\in F_\tau+p^n}
 \left(\frac{F_\tau-C}{\kappa^n}\right)^s d\nu_{B_C}(C),
\qquad 0\le s\le6.
\tag{25}
$$
在已经支付的 $\nu_{B_C}\otimes\nu^\flat$ 表示中，
(7) 固定 $C$，所以 (25) 是同一个真实隐藏来源的完整转置。
不从 (8) 逆推未投影的原六 sigma 也有相同反射字符。

这项转置不能省。原 $\pi_4=(Y,W,W',G)$ 的共同核含
$$
v=(4-\omega,\ 7\omega,\ -3-\omega,\ 2+3\omega,\ 7)^t,
$$
而
$$
Y_\tau(v)=18+6\omega=6(3+\omega)\ne0.
\tag{26}
$$
所以 $\tau$ 不保持原四输出空间；
只由 R594 的 $\pi_4$ 中性，不能给
$w_n(\ell\circ\tau)$ 免费赋原中央返回。
(26) 的非零值在当前射线上也是单位。

使用真正的完整测试
$$
\boxed{
\widehat g_n=(w_n\ell)\circ\tau-c_\tau w_n\ell .
}
\tag{27}
$$
R594 的同一个四输出返回和 (8) 准确给
$$
\nu^\flat(\widehat g_n)=-(1+c_\tau)\beta^n\mathcal T .
\tag{28}
$$
第一项的支撑为 $F_\tau$ 单位，第二项为 $F$ 单位；
不把二者强改成它们的交集。

定义两个实际完整补偿
$$
O_n^\tau=\int_{\mathscr R_n^c}\widehat g_n\,d\nu^\flat,\qquad
K_n^\tau=\int_{\mathscr R_n}
            (\widehat g_n-\beta^n g)\,d\nu^\flat .
\tag{29}
$$
由 (17)、(28) 立刻得到全来源等式
$$
\boxed{\beta^{-n}(O_n^\tau+K_n^\tau)=B_n^\tau.}
\tag{30}
$$
将 (30) 代入 (21)，即把原 $I_1$ 的同深返回完整写在
同一个原六支 carry 家族中，没有重算或修改 R594 的右逆。

R594 已付的 $\int_{\mathscr R_n}w_n\ell$ 仍具有原赋值 $n$。
但 $\int_{\mathscr R_n}(w_n\ell)\circ\tau$ 使用 (24)–(25) 的
不同实际余类纤维；这里没有把前一个单位首项移给它。
(29) 的两个补偿均完整保留，局部首项非零不被提升为 (28) 非零。

## 7. 直接接回 R605 的完整三域外积分

保 R605 的
$$
\mathcal T=\mathscr C(\lambda,\kappa)R_n+H_n+C_n^{\rm out},
\qquad H_n\in p^{9n}\mathcal O .
\tag{31}
$$
这里 $C_n^{\rm out}$ 是真正三域外的原 $\ell$ 积分，
不是本篇的转置测试 (20)。
由 (12)，可再定义真正四域外积分
$$
C_n^{\rm out,4}=
\int_{\mathcal O^5\setminus
(\mathscr R_n\sqcup\mathscr R_n^Y\sqcup
 \mathscr R_n^W\sqcup\mathscr A_n)}
\ell\,d\nu^\flat .
\tag{32}
$$
(13)、(16) 给
$$
\int_{\mathscr A_n}\ell\,d\nu^\flat
=-R_n^\tau=-c_\tau R_n-D_n^\tau.
$$
因此同一个实际剩余域准确满足
$$
C_n^{\rm out,4}=C_n^{\rm out}+c_\tau R_n+D_n^\tau .
$$
消去原 $R_n$ 得完整身份
$$
\boxed{
\mathscr C\,C_n^{\rm out,4}
-(\mathscr C-c_\tau)C_n^{\rm out}
-c_\tau\mathcal T
=\mathscr C D_n^\tau-c_\tau H_n .
}
\tag{33}
$$

在 R605 已显示的无穷单位子集 $\mathscr C\in\mathcal O^\times$ 上，
(18)、(31)、(33) 给另一条直接同深返回：
$$
\boxed{
\frac{\mathscr C\,C_n^{\rm out,4}
-(\mathscr C-c_\tau)C_n^{\rm out}
-c_\tau(J'_S-6\delta J'_T)}
{\mathscr C\,d_p\epsilon_\tau\Omega^5\beta^{4n}\kappa^{5n}}
=I_1+p^{4n}\mathcal O .
}
\tag{34}
$$
两个外积分都使用原来的 $\ell$、原来的来源，
且四个被剥出的真实域完全不交。
(34) 不将剩余四域外积分赋零；
它说明原补偿中这一新可控支怎样与两个已付核心像准确联立。

第 1–6 节的 (21)–(30) 对当前整个原射线成立，
只在使用 R605 的系数 $\mathscr C^{-1}$ 时才需其显示的稀疏坏集。
不能将这个固定系数的单位计数用于 $I_1$ 本身。

## 8. 精确证书

- [check-r611-original-three-sigma-reflection-and-same-depth-negative-five.js](../scripts/check-r611-original-three-sigma-reflection-and-same-depth-negative-five.js)
- [check-r611-original-three-sigma-reflection-and-same-depth-negative-five.json](../scripts/check-r611-original-three-sigma-reflection-and-same-depth-negative-five.json)

BigInt 的 $\mathbf Q(\omega)$ 证书核定整个五变量反射及 Gram、
三个真实 sigma 参数的置换负号、所有原观察与 $F/G$ 转置、
准确单位范数、同深负三消去和负五系数，以及 (26) 的完整
四输出不变性边界。
全 Amice 来源、真实切集、级数尾界和两项 carry 补偿由正文证明。
原中央非零与主目标仍未由这些接口完成。
