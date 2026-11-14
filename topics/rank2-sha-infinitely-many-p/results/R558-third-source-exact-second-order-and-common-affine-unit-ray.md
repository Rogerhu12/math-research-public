# R558 — 原第三来源 Y−W 差的准确二阶与一个共同无限单位 ray

日期：2026-11-14。**状态：已证明。**
本篇继续 R557 的同一个原网格、同一个 R536 七行测试，
把第三来源 $\eta$ 的未归一 $Y-W$ 差从“赋值至少 $2n$”
推进为一个共同无限 ray 上的**准确赋值 $2n$**。
所用系数取自已发表的完整右逆，没有重选测试。

原二阶系数的模 $p$ 值是一个固定的 $\bar\pi_0$ 仿射式。
一个初等的复绝对值与 CRT 引理给出完全固定的附加 ray，
使这条实际仿射式在全部所选普通素数处为单位。
这里新增的是准确的原子域非消失，尚未删除完整中央补域。

## 1. 原同一对象和唯一新有限行

所有 $C,F,D,E,G,\pi_4,\eta,\rho_0,h,\mathcal D_n$ 及
$q_{n,p}^{(0)},\mathfrak q_{n,p}$ 都取 [R557](R557-third-source-common-carry-zero-mass-and-central-rows.md)
的原定义。保
$$
b=17,\quad \beta=-\lambda=\bar\pi_0^{-1},\quad
\kappa=p\lambda^2,\quad d=p-1,\quad
\tau=(1+\lambda)^{-1}.
\tag{1}
$$
特别 $p\ge71$、$p\equiv7\bmod64$；
原 $D_*$ 和全部旧有限坏集均保持。

将原准确多项式写成
$$
P_p(D,E,G)=\sum_{k+j+\ell=6}a_{kj\ell,p}D^kE^jG^\ell,
\quad u_j=(1+\lambda\kappa^j)^{-1}.
$$
原两个自由 $x$ 系数仍为
$$
e_0=(-14-28\omega)/3,\qquad g_0=(32+31\omega)/3.
$$
定义真正的新第三行
$$
\boxed{\mathcal L_{3,p}
=\sum_{j+\ell=3}a_{3j\ell,p}\,u_j e_0^j g_0^\ell.}
\tag{2}
$$
R536 原第七行只是 $\mathcal L_{4,p}=1$，没有预付 (2)。
(2) 的全部 $\lambda,\kappa$ 依赖在这里保留。

## 2. 完整二阶系数

仍用 R557 的未平均真实中央
$$
C^\eta_{L,n}
=\int_{\mathcal D_n}d\log\langle L\rangle\,
q_{n,p}^{(0)}\,d\eta,\qquad L=Y,W.
$$
若用 $\mathfrak q_{n,p}$，下列每个值都除以 $3$。
令 $\mathcal A^\eta_L(T)$ 是 R557 的同一个完整解析函数。

**定理1。** 准确有
$$
\boxed{
[T^2](\mathcal A^\eta_Y-\mathcal A^\eta_W)
=\frac db(1+\lambda\kappa)\,
\frac{2\omega^2(8-3\omega)}{7\bar\gamma^2}\,
\mathcal L_{3,p},
\qquad \bar\gamma=2-\omega.
}
\tag{3}
$$
其固定外因子为
$$
\frac{2\omega^2(8-3\omega)}{7\bar\gamma^2}
=\frac{-96-158\omega}{343},
\qquad
N=\frac{388}{2401}=\frac{4\cdot97}{7^4}.
\tag{4}
$$
在原 $p\equiv7\bmod64$ ray 上它始终为单位。

**证明。** 使用 R539 的真实正交坐标
$$
L=(W-Y)/2=(1+3\omega)c+d_0,\quad
M=c+(2+3\omega)d_0,
$$
$$
Y=A+aL+b_M M,\qquad W=A+(a+2)L+b_M M,\qquad a=-3\omega/8.
\tag{5}
$$
原 $H$ 满足
$$
LH=2(c+d_0),\qquad MH=2\omega(c-d_0).
\tag{6}
$$
因此 $\eta$ 在真实 $L$ 反射下为偶；
其完整 $(L,M)$ 生成函数的末两因子是
$\omega^2\sigma(2l+2\omega m)\sigma(2l-2\omega m)$。
原 $D_f,E_f,G_f$ 及所有 $q$ 多项式只经 $M$ 依赖末两输入，
故在这个反射下保持。

在原 $\mathcal D_n$ 的缩放变量中，$Y,W$ 具有同一自由项
$\bar\gamma x$。两 log 的常数项完全相消，
一次差是 $L$ 的奇函数，所以其与原多项式的任意 $T$ 系数相乘后
积分仍严格为零。二次差的偶部分准确为
$$
-\frac{a^2-(a+2)^2}{2\bar\gamma^2x^2}\,L^2
=\frac{8-3\omega}{4\bar\gamma^2x^2}L^2.
\tag{7}
$$
总型及最小次数使 $T^0$ 的原 $q$ 中只有 $D_f^3$ 项可与 $L^2$
贡献五深输入的次数五；其余 $k$ 的总型不同或次数不足。
该项的自由系数就是 (2)，不是另加的可调系数。

真实五输入系数为
$$
\omega^2[\xi_1\xi_2\xi_3cd_0](D_fH)^3(LH)^2
=-96\omega^2.
$$
乘源的 $-1/84$，得到 $8\omega^2\Omega^5/7$。
自由 $x$ 剩一次幂，原单位矩为
$\Omega(1+\lambda\kappa)$。
再乘 (7)、$d/(b\Omega^6)$，即 (3)。
全过程使用同一 $q$ 和同一原单位域。证毕。

## 3. 原已发表右逆给一个固定仿射式

以下只读取 R536 已发表 JSON 中的矩阵及右逆，不重新求它。
为避免与别处 $A$ 行混同，把这节两个固定常数记为
$\mathsf a_3,\mathsf b_3\in\mathbf Q(\omega)$。

具体计算完全由如下有限式指定。
令 $P_*=-C^6/8$、$P_i=C^{r_i}F^{s_i}G^{t_i}$
为原十个消去单项式；仍代
$C=(E-D)/14$、$F=(E+13D)/14$。
对一个固定 $P$ 定义
$$
\ell_3(P;\tau)=
\sum_{j+\ell=3}[D^3E^jG^\ell]P\,e_0^jg_0^\ell
\begin{cases}\tau&j=0,\\1&j>0.\end{cases}
\tag{8}
$$
取原证书中的 $B_0,B_1,b_0,b_1$，约定
$A(\tau)=A_++\tau A_0$、
$B(\tau)=(B_0+\tau B_1)/(\tau-1)$、
$b(\tau)=b_0+\tau b_1$。准确计算给
$$
\boxed{
\begin{aligned}
&(\tau-1)\ell_3(P_*;\tau)\\
&\quad+\sum_{i=0}^9
\ell_3(P_i;\tau)
\bigl[(B_0+\tau B_1)(b_0+\tau b_1)\bigr]_i
=\mathsf a_3+\mathsf b_3\tau.
\end{aligned}}
\tag{9}
$$
所有次数至少二的系数严格为零。
$\mathsf a_3,\mathsf b_3$ 的完整约分有理 CM 坐标存于附 JSON；
(8)–(9) 也独立指定它们，不依赖样本素数。

原精确解是
$x_p=B(\tau)[A_pB(\tau)]^{-1}b_p$，而
$A_pB(\tau)\equiv I$、$b_p\equiv b(\tau)\bmod p$。
因此同一个实际系数 (2) 满足
$$
\boxed{
\mathcal L_{3,p}
\equiv\frac{\mathsf a_3+\mathsf b_3\tau}{\tau-1}
=-\mathsf a_3+(\mathsf a_3+\mathsf b_3)\bar\pi_0
\pmod p.
}
\tag{10}
$$
$\tau-1=-\lambda/(1+\lambda)$ 为原 ray 的单位。
(10) 只用于单位性；(3) 继续使用完整未约化的 $\mathcal L_{3,p}$。

设 $C_3$ 是 (10) 右侧两常数在基 $1,\delta$ 的四个有理分母的
最小公倍数，并定义原固定代数整数
$$
\boxed{
A_3=-C_3\mathsf a_3,\qquad
B_3=C_3(\mathsf a_3+\mathsf b_3)\in\mathbf Z[\delta].
}
\tag{11}
$$
这里 $B_3$ 只是固定系数名，不是此前的 degree3 theta 来源。
附计算给 $A_3\ne0$，并且
$$
\boxed{\Delta=N(-A_3+B_3)-N(B_3)>0.}
\tag{12}
$$
此外准确有
$$
\frac{16N(A_3)N(B_3)}{\Delta^2}<2,\qquad
\frac{2N(A_3)}{\Delta}<1.
\tag{13}
$$
这些是特征零整数有理不等式，完整整数在附证书中。
它们将在下面将所有大 $p$ 门压到原已有的 $p\ge71$。

## 4. 固定仿射 Frobenius 行的无限单位 ray 引理

**引理2。** 令 $K=\mathbf Q(\omega)$，
$A,B\in\mathcal O_K$，$A\ne0$。
对单位 $\zeta\in\mu_6$，写
$$
q_\zeta=\zeta^{-1}A+\zeta^{-2}B,\qquad
\Delta_\zeta=N(q_\zeta)-N(B).
$$
存在一个 $\zeta$ 使 $\Delta_\zeta>0$。
若固定整数 $M>2(|A|+|B|)$，且 $\pi$ 是范数为有理素数 $p$
的代数整数，满足
$$
\pi\equiv\zeta\pmod{M\mathcal O_K},\qquad
p>\max\left\{
\frac{16N(A)N(B)}{\Delta_\zeta^2},
\frac{2N(A)}{\Delta_\zeta}
\right\},
\tag{14}
$$
则
$$
\boxed{A+B\bar\pi\notin\pi\mathcal O_K.}
\tag{15}
$$

**证明。** 对六个单位取平均，交叉项消掉，故
$\frac16\sum_\zeta N(q_\zeta)=N(A)+N(B)>N(B)$；
于是存在所需 $\zeta$。

反设 $q=(A+B\bar\pi)/\pi\in\mathcal O_K$。
复绝对值和 (14) 给
$$
N(q)\le N(B)+\frac{2|A||B|}{\sqrt p}+\frac{N(A)}p
<N(B)+\Delta_\zeta=N(q_\zeta).
\tag{16}
$$
另一方面由 $\pi\equiv\zeta$、$\bar\pi\equiv\bar\zeta$，
$q\equiv q_\zeta\bmod M\mathcal O_K$。
又有 $|q|\le|A|+|B|$、$|q_\zeta|\le|A|+|B|$，
所以 $|q-q_\zeta|<M$。
非零 $M\mathcal O_K$ 元素的复绝对值至少为 $M$，
故必须 $q=q_\zeta$，与 (16) 矛盾。证毕。

若原已有有限 ray 的模数为 $N_0$，可以选
$M=1+N_0K_0$ 足够大，使 $\gcd(M,N_0)=1$。
原剩余类和 $\pi\equiv\zeta\bmod M$ 由 CRT 相容。
同一个原 principal CM 素理想的 ray 类 Chebotarev 定理，
给无穷多个满足两个条件的 $\pi$；删有限小素数仍无限。
对有限多条这样的固定仿射式，可逐条选择互素新模数，
因而得到一条共同的无限单位 ray。
这不要求逐个扫描 $p$，也没有使用素数取二次多项式值的猜想。

## 5. 本篇完全指定的新 ray

取此前全部已付 ray 的共同模数
$
N_0=\operatorname{lcm}\bigl(
1323133171213029144041201350687525528684869767169429257083200,
29,137,79,103,263,49,1013,31\bigr).
$
第一项是 R487 的全部高 $13/19$ ray；其余保此后的原固定细分。
只取共同模数不更换任何原剩余类。附证书同时给 $N_0,M_3$ 的整数值。
将 (11) 写作
$$
A_3=a_0+a_1\omega,\qquad B_3=b_0+b_1\omega
\quad(a_i,b_i\in\mathbf Z),
$$
定义固定正整数
$$
K_0=2(|a_0|+|a_1|+|b_0|+|b_1|)+1,\qquad
\boxed{M_3=1+37N_0K_0.}
\tag{17}
$$
于是 $M_3>2(|A_3|+|B_3|)$，
且与原 $N_0$ 和 $37$ 都互素。
取原全部条件再加
$$
\boxed{\pi_0\equiv-1\pmod{M_3\mathcal O_K},\qquad p\nmid C_3.}
\tag{18}
$$
系数 $37$ 只保证与实际新交轴所需的独立 $37$ 细分相容；
本篇不借用尚未施用的 $37$ 核。
(17)–(18) 完整指定一个固定模数及剩余类。
$C_3$ 的素因子是固定有限集，不依赖 $p,n$。

用 $\zeta=-1$，(12)–(13) 及原 $p\ge71$ 满足引理全部门。
所以 $A_3+B_3\bar\pi_0$ 在原普通地点是单位。
因 $p\nmid C_3$，(10) 得
$$
\boxed{\mathcal L_{3,p}\in\mathcal O^\times}
\tag{19}
$$
对这个共同无限 ray 的每个素数成立。
原 CM 主生成元的规范由旧模数保留，
没有把任意关联的六个生成元各自当成同一个 $\pi_0$。

## 6. 同一个实际 Y−W 差的准确赋值

R557 已付零阶、一次项为零，原完整尾满足
$$
v_p([T^r](\mathcal A^\eta_Y-\mathcal A^\eta_W))
\ge-\lfloor\log_pr\rfloor.
$$
在 (18) 的同一无限 ray 上，(3)、(4)、(19) 给准确单位二次项。
对任意 $n\ge1,r\ge3$，
$$
rn-\lfloor\log_pr\rfloor>2n.
$$
因此
$$
\boxed{
v_p(C^\eta_{Y,n}-C^\eta_{W,n})=2n
\qquad(n\ge1).
}
\tag{20}
$$
原共同因子 $\beta^{5n}$ 以及平均的 $1/3$ 都是单位。
所以 (20) 对同一个 $\mathfrak q_{n,p}$ 也成立。

(20) 和 R557 的 $h$ 差赋值 $n$、两态零质量一起，
给同一原网格的两个不同而准确的层次。
所有原 $Y,W$ 单位条件在该网格上确实成立，
没有把某个不同的低权测试认成中央。

## 7. 尚须联立的完整补域

新增 ray 没有改变固定目标曲线或扩大完成标准。
(20) 属于原 $\mathcal D_n$ 子域；全 $\pi_4$ 推前仍由 R557 准确控制，
但不能由此删掉原 carry 里的其余输入，或删掉 R556 的 native
$u_1/u_2$ 条带、反射共同支、独有支及四个 Mellin 边界。

下一步是把这条准确二阶与那些同源完整项联立。
仅有固定子域在共同无限 ray 上非零，仍不等于固定曲线的
原完整 $J'_S/J'_T/J'_{\rm new}$ 非零。

## 计算来源

- [R536 原完整 JSON](../scripts/check-r536-exact-fibre-mass-compensation.json)，
  Git blob \`ab452d507aa20c2326312ab059187e0c920c87ec\`；
  本篇直接使用其中的原右逆和固定列。
- [新有限行脚本](../scripts/check-r558-third-source-second-order-and-affine-ray.js)。
- [新有限行及固定 ray 整数证书](../scripts/check-r558-third-source-second-order-and-affine-ray.json)。

脚本只用准确有理和 CM 运算，给 (9)、(11)–(13) 的完整系数。
两阶展开、全部 $n$ 的尾比较以及无限 ray 是正文证明；
不由任何有限素数检查外推。
