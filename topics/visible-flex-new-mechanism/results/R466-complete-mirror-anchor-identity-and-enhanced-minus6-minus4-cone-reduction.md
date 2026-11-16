# R466：完整换锚镜像身份与增强负六、负四字符的消去

日期：2026-11-16。**完整原式纸面证明及原已付列的只读消费。没有执行符号程序、原根恢复、profile 求积或新的数值／秩计算。**

[R465](R465-complete-zero-weight-affine-head-and-two-mirror-self-membership-gates.md) 已把同一增强映射的零权 lift 门化为两个完整 self 成员问题，并支付最低偶权 $-8$。它保留的另一实质问题是：加入全部真实内部 partial 后，旧 $J_0$ 的负六、负四排正字符证明是否仍成立。

本文在**同一个** $J_{\rm aff}$ 上支付这两层。关键不是再计算旧自然像，而是保真实左右锚，先证明完整 self 镜像关系；再用原已付、真正同权的响应列覆盖所需的全部镜对多项式。结果为
$$
\boxed{
U_{-6}\cap\ker J_0
\subseteq \mathcal R_{-6}+\ker J_{\rm aff},
}
\tag{1}
$$
$$
\boxed{
U_{-4}\cap\ker J_0
\subseteq N(U_{-3}\cap\ker J_0)+\mathcal R_{-4}
+\ker J_{\rm aff}.
}
\tag{2}
$$
第二式有真实 $N$ 项，不能改称负四的垂直响应满覆盖。这两式使任何经 $J_{\rm aff}$ 下降、杀响应和平移的相应正字符都回到旧 $J_0$，从而由 R433 排除。

结合 R465 的两个 self 商类 $\mathfrak h,\mathfrak y$，还得到更精确的末判据：
$$
\boxed{
\overline{\operatorname{cone}J_{\rm aff}(\mathcal S)}
=J_{\rm aff}(U)
\quad\Longleftrightarrow\quad
\mathfrak h\in\operatorname{span}\{\mathfrak y\}.
}
\tag{3}
$$
原双参数 actual 构造的充分接口仍是更强的
$\mathfrak h=\mathfrak y=0$。本文不预报这两个新 self 目标的成员结果，不把闭锥等式直接当作有限正时长实现。

## 1. 同一增强、同一母库与完整规范

保留 R455/R459 从起点选择的共同物理宽度、全部实际角色和副本、真实 suffix、原右锚及共同合法窗口。参考母 $u$ 为偶函数，两实际 Af 镜点为 $\pm b$，记
$$
u(\pm b)=u_*,\qquad
u'(-b)=p_*,\quad u'(b)=-p_*,\qquad
u''(\pm b)=r_*,
\quad p_*r_*\ne0.
\tag{4}
$$
共同物理宽度已收入 $u$；不得把无宽度母的 jets 直接代入(4)。设
$$
s_*=\frac{p_*}{r_*},\qquad h_*=\frac{u_*}{r_*}.
$$
$h_*$ 是本节的 jet 比值，不是路径的几何函数 $h(s)$。最终基本包沿 R407/R459 的真实同三矩、固定内区路径连到该参考母；不假定任意同矩纤维都连通。

沿 R465 置
$$
J_0=(E,\mathcal A,\mathcal O_{\rm all}),\qquad
E=(\pi,\mathcal Q),
$$
$$
F_{\rm aff}
=\operatorname{span}\{FN^j\Pi_\sigma:
-9\le\sigma\le3,\ 0\le j\le\sigma+9\},
\qquad
J_{\rm aff}=(J_0,F_{\rm aff}).
\tag{5}
$$
$F$ 是全部实际角色的两通道、两内部点查询；其在 $U$ 上的线性延拓按 R463 原相位极化固定。$\mathcal A$ 是同库有限仿射自然查询，包含参考母及实际包所需的整包值，不是 universal self 自然函数。

本稿继承 R465 中 $J_0$ 的全部母库前提，包括旧共同自然链和正字符排除所用的条件；不单凭偶性重新授予旧定理。以下全部核和响应空间按(5)使用。$\ker J_0$、$\ker J_{\rm aff}$、$\mathcal R$ 对真缩放生成元 $D$、平移生成元 $N$ 稳定。有限真权谱为 $[-9,3]$。形式 current $\mathscr C$ 仍取 R433/R454 的**完整三尾矩、39坐标**，采用 $\mathcal K/4$ 规范。self partial 本文直接取原积分，不除以4。

写
$$
p=u',\quad r=u'',\quad t=u''',\qquad A_u=6pt-2r^2,
$$
$$
\Sigma_V(u)=V(u^2,0),\qquad
h_\pm(V;u)=\int_{\ell}^{\pm b}p\,\Sigma_V(u)''.
\tag{6}
$$
$\ell$ 位于原左零 collar。积分允许 $\Sigma$ 有真实左尾；平端 jets 才使通常的两次分部积分边项为零。

直接来源为 R56、R73、R145、R292、R356、R407、R432、R433、R443、R448、R454、R457、R459、R462—R465。下文每个新步骤注明它实际使用的完整范围。

## 2. 二阶场的两个锚：必须先保真左尾

先沿一个原同端口、闭 frame、$M=0$ 的 canonical 成本路径证明，再对这些原成本的有限实组合线性延拓到 $U$。这与 [R407 §1](R407-connected-moment-fibers-fix-self-caps-and-retain-the-actual-total-fluxes.md) 的完整 self 入口相同。记
$$
\mathscr K^{R/L}(A,B)=\mathscr P^{R/L}H(A,B),
\qquad Z_u^R=\operatorname{Range}^R H(Y_u,Y_u).
$$
上标只区分 profile 原函数的右、左归一；路径上的同一个 $s$ 起点、所有 history 和周期积分均保留。

原完整 fourth forcing 在 $\phi=0,D=u^2$ 时给
$$
\boxed{\Sigma_V(u)=-\mathscr K^R(Z_u^R,Z_u^R).}
\tag{7}
$$
此式不需要先假设 $\pi V=0$。这里 $Y_\phi=0$ 是实际代入，所以原 $YW$ forcing 的确为零；不是因某个平台局部为零便删其右累计。

记完整三矩为
$$
\mu(u)=
\left(\int r^2,\ \int xr^2,\
\int(x^2r^2+2p^2)\right).
\tag{8}
$$
R73 与 [R292 §3](R292-zero-platform-periods-and-ordered-second-history-matrix.md) 给原二阶左尾：
$$
Z_\mu(s,x)=x\,\mathbf U_\mu(s)+\mathbf V_\mu(s).
\tag{9}
$$
这里是完整场分子的仿射性。其标量 $W_\mu$ 可以是二次多项式；三系数来自同一个真实 $m(s)=\int_{s_0}^sM$，不能独立指定。

对二阶 forcing，设 $T_x$ 为原两个 $x$ 导数的分子配对。完整右、左原函数分别为
$$
P_R(x)=\frac1{2h}\int_x^{r_0}T_x(y)\,dy,\qquad
P_L(x)=-\frac1{2h}\int_{\ell}^{x}T_x(y)\,dy.
$$
所以 $P_L=P_R-P_{\rm total}$，其中 $P_{\rm total}$ 恰为原真实左常数。局部 $B$ 不变；$W,A$ 的差按同一个 $s_0$ 积分恢复。因此整个二阶场准确满足
$$
\boxed{Z_u^L=Z_u^R-Z_{\mu(u)}.}
\tag{10}
$$
$Z_{\mu(u)}$ 是(9)的全 $x$ 仿射延拓。式(10)没有把 $Z_u^R$ 说成左紧，也没有为每个分项重新选积分常数。

## 3. 曲率反号加坐标反射：完整 self 的换锚身份

令 $\iota u(x)=u(-x)$；先在对称 collar 坐标中核原式。所需恒等式是有限原模板的坐标身份，可连同锚与全部系数作合法的共同坐标输运。它不要求原物理区间以0为中心，也不把下面的空间反射单独当作新的允许控制。

[R145](R145-true-curvature-reflection-and-even-positive-characters.md) 的真实曲率反号为
$$
(h,k,\omega)\longmapsto(h,-k,-\omega),
\qquad \mathbf E=\operatorname{diag}(-1,1,1).
$$
其成本是原正缩放有限 Laurent 表示的谱反号
$\mathsf S=\mathsf P^{\rm alg}_{-1,0}$。特别
$\mathsf S V=(-1)^\sigma V$ 对 $V\in U_\sigma$ 成立。这不是物理负 $h$，也不是保持曲率而仅镜像 profile。

现把该曲率反号与 $x'=-x$ 同时用于 R56 原分子式。以
$$
z=x+\omega,\quad e=hz-k,\quad
K_g=kz^2-\frac{k^2+1}{h}z,\quad
\lambda_g=\frac{h_s z-h\omega_s}{h^2}
$$
记几何系数，则 $z,e,K_g,\lambda_g$ 全部反号。R145 的原 frame 共轭同时保证 $\nabla_s^\sharp(\mathbf E Z)=\mathbf E\nabla_s Z$；因此配对 $J,T_s,T_x$ 不变，而 $T_{sx}$ 反号。原右锚在坐标反射后成为左锚，故
$$
P_R^\sharp(-x)=-P_L(x),\qquad B^\sharp(-x)=B(x).
$$
逐项代入
$$
\mathcal R_H=
\frac{T_s}{2h^2}+K_gP-\lambda_gP_s
+\frac{K_g}{z}B-\frac{h_s}{h^2}B_s
\tag{11}
$$
得到 $\mathcal R_H^\sharp(-x)=\mathcal R_H^L(x)$。同一原 $\eta_0$ 式给
$\eta_0^\sharp(-x)=-\eta_0^L(x)$；因此 $W^\sharp(-x)=W^L(x)$、
$A^\sharp(-x)=-A^L(x)$，最终
$$
\boxed{
Z_{\iota u}^{R,\sharp}(s,-x)
=\mathbf E Z_u^L(s,x).
}
\tag{12}
$$
这是第二阶完整场身份，包含真实左 history。第四平方 forcing 继续使用同一配对，故
$$
\Sigma_{\mathsf S V}(\iota u)(-x)
=-\mathscr K^L(Z_u^L,Z_u^L)(x).
\tag{13}
$$

定义原有序 $2+2$ self 交叉输出
$$
\mathcal U_V(u;n)
=[a^2b^2]\Sigma_V(au+bv),\qquad
u<v,\quad \mu(v)=n,
\tag{14}
$$
此处先用原 self 极化定义，随后在 $\pi V=0$ 上才与 R389/R433 两 mixed 所用的 $\mathcal U=4Q$ 识别。先在真实右包矩上取值，再按其三矩线性性延拓。三个不同右包的矩基足够定义所有 $n$。特别代 $n=\mu(u)$ 时，不声称存在一个右包恰有与 $u$ 相同的三个矩。

在整个左包上，原右包二阶场就是 $Z_n$，而 $Z_u^R$ 在包右方准确为零。因此
$$
\mathcal U_V(u;n)=-2\mathscr K^R(Z_u^R,Z_n)
\tag{15}
$$
是保原锚的身份。将(10)代入(13)，得到
$$
\boxed{
\Sigma_{\mathsf S V}(\iota u)(-x)
=\Sigma_V(u)(x)-\mathcal U_V(u;\mu(u))(x)+P_2(x),
\quad\deg P_2\le2.
}
\tag{16}
$$

次数界需要两个准确事实：

1. 对同一 forcing，左右输出的 $P$ 只差真实 $x$ 常数。式(11)的差为 $K_g\Delta P-\lambda_g(\Delta P)_s$，故其完整周期输出至多二次。
2. $\mathscr K^R(Z_\mu,Z_\mu)$ 对真实仿射场(9)也至多二次。这里不能只看 $K_gP$：R292(8)—(10)中，仿射 $P$ 的三次项与 $K_gB/z$ 的三次项准确相消，全部 $h_s$ 项仍保留。

$P_2$ 包含这两类真实差值。本文没有把它当作任意可选 gauge，也没有删除原 $\Gamma$ 或某个 normal family 的端项。式(7)—(16)先对完整 canonical 成本成立，其两侧及交叉极化均对成本线性，因此延拓到完整 $U$ 后依然包含所有原正规化项。不能把它仅理解为一个 acceleration raw 分支的对称性。

## 4. whole self 只消 P2 的二导；total 与 ordered 项还需分别支付

若 $\mathcal QV=0$，缩放协变也给 $\mathcal Q(\mathsf S V)=0$。在 $u$ 的原右 collar，(16)中 $\Sigma_V$ 和 $\mathcal U_V$ 都准确为零；其左边则是 $\mathsf S V$ 的真实左尾经坐标反射。于是 $P_2$ 的二次系数为零：
$$
P_2''=0.
\tag{17}
$$
$P_2$ 的仿射部分可以非零，仍不删除它。二导后才得到
$$
\left[\Sigma_{\mathsf S V}(\iota u)(-x)\right]''
=\Sigma_V(u)''(x)-\mathcal U_V(u;\mu(u))''(x).
\tag{18}
$$

现在 $u$ 偶、$V\in U_\sigma$。将该偶母的两外 collar 在同一坐标证明中取成镜像，记原整包值
$
\Omega_u(V)=\int_\ell^{r_0}p\,\Sigma_V(u)''
=\int_\ell^{r_0}u'''\Sigma_V(u).
$$
换变量 $x\mapsto-x$，而不是把左积分常数设为零，给
$$
\boxed{
h_+(V;u)
=\Omega_u(V)+(-1)^\sigma
\left\{
h_-(V;u)
-\int_\ell^{-b}p\,\mathcal U_V(u;\mu(u))''
\right\}.
}
\tag{19}
$$
式(19)是尚未消任何 total/current 的准确 mirror 关系。

若再有
$$
V\in\ker J_0,\qquad \mathscr C V=0,
\tag{20}
$$
则 $\pi V=0$ 把 $\Omega_u$ 与原自然 $\Lambda_u$ 识别，当前 $\mathcal A$ 使它为零。这里仅使用当前库规定的自然查询，不外推为 $\Lambda_{\rm all}V=0$。

另一方面，whole $E$ 和 $\mathcal O_{\rm all}=0$ 使 R433 的原 ordered 积分成为真实局部 current；其在 Af 点的值恰为 $4\mathscr C V$。所以(19)的最后积分也为零。于是
$$
\boxed{h_+(V;u)=(-1)^\sigma h_-(V;u).}
\tag{21}
$$
这个式子同时使用(17)、真实 total 和完整三尾 current，不能由偶母和同点 jets 单独猜出。

令 $u_c(x)=u(x-c)$，记 $h_\pm(c;V)$ 为其两内部点的原左起 partial。准确平移协变给
$$
h_\pm(c;V)=h_\pm(0;e^{cN}V).
\tag{22}
$$
(20)的核对 $N$ 稳定，$N^jV$ 的真权是 $\sigma-j$。逐项用(21)得到
$$
h_+(c;V)=(-1)^\sigma h_-(-c;V).
\tag{23}
$$
以实际根坐标定义
$$
P_V^-(x)=r_*^{-5}h_-(x+b;V),\qquad
P_V^+(x)=r_*^{-5}h_+(x-b;V),
$$
便有
$$
\boxed{P_V^+(x)=(-1)^\sigma P_V^-(-x).}
\tag{24}
$$
第五次齐次性负责实际幅度的第五幂；(24)没有丢掉该因子。

R356 已给 $\Sigma(U_{-9})=0$。因此 $N^{\sigma+9}V$ 的完整 self 为零，(22)推出
$$
\deg P_V^\pm\le\sigma+8.
\tag{25}
$$
所以在当前完整核上，负六的镜对只需一个 $\operatorname{Pol}_2$，负四只需一个 $\operatorname{Pol}_4$；右多项式由(24)完全确定。

## 5. 为什么这确实覆盖同库全部实际包和 Faff

最终包本身可以非偶。它们通过 R407/R459 的实际同三矩、固定内区路径连到共同偶参考母。R407(10)—(15)证明：whole $\mathcal Q=0$ 使 self 的二阶导数在两侧外 cap 沿该路径准确不变；并未断言 self 仿射尾不变。

左 partial 因此直接等于参考母的左 cap。右 partial 再使用当前 $\mathcal A$ 已规定的真实整包 $\Lambda=0$，才可用相应右 cap。ordered 部分由完整 $\mathscr C=0$ 对任意真实 suffix 为零。于是同一成本若使(24)的两个完整多项式为零，就使每个实际角色的原两通道为零。所有 $a_i^3,R_i,T_i$、各包自身的幅度第五幂、原顺序和 suffix 都仍取实际值；没有逐包自由选择控制。

以上对一个完整平移多项式成立，所以同时杀所有 $FN^j$。若目标和所选响应都是真正同一权 $\sigma$，正缩放只共同乘 $H^\sigma$，也保持此身份。因此它支付(5)的整个 $F_{\rm aff}$。

这里不把一个混权、只在单宽拟合的响应事后投影成同权；下面先选真正同权成本，再证明其两个完整镜多项式同时覆盖。

## 6. 负六的三个真实同权列覆盖整个 Pol2

令 $P=\Phi_{r_0}$，即 $q_P(u)=J(r^2)$。沿 [R432](R432-complete-zero-order-kernel-and-all-degenerate-point-response-matrices.md) 记
$$
\varsigma=\frac12\left[64(\chi_{34}-3\chi_{32})-\frac12\mathfrak J_0\right],
$$
$$
\tau_2=\frac1{20}(H_2+5120\chi_{32}+16J_0).
\tag{26}
$$
它们的完整自伴系数满足 $c=0$，且
$$
a_\varsigma=p^2,\qquad
a_{\tau_2}=x^2A_u+4xpr-4p^2.
$$
$P$ 真权为 $-3$，$\varsigma,\tau_2$ 也各为 $-3$，所以两响应
$\mathcal B_P\varsigma,\mathcal B_P\tau_2$ 确在 $\mathcal R_{-6}$。

原同锚式为
$$
\int_\ell^x p\,(\mathcal B_E\tau(u^2,0))''
=2a_\tau\{p q_E''-r q_E'\}.
\tag{27}
$$
在 $A_u=0$ 点，$pt=r^2/3$，而
$$
p q_P''-r q_P'
=-2prt+r^3=\frac13r^3.
$$
故两个完整 self 值为
$$
\frac23p^2r^3,\qquad
\frac83(xpr^4-p^2r^3).
\tag{28}
$$
$P$ 对任意右 suffix 的真实左尾是常数 $n_0$。$c=0$ 的完整 $K_u$ 杀常数，所以这两列的整个三尾 current 均零；这比仅检查当前一个 suffix 更强。whole $E$ 及完整 natural 零也由原响应恒等保留。

再取原 K 链的真权 $-6$ 成本 $K_2$。其完整生成式由 R435/R443 已付：
$$
w=1-zx,\quad A_z=w^2r+2zwp+2z^2u,
$$
$$
F_{K_n}
=n![z^n]\frac{A_z^3}{15}
\left(4A_z^2-10z^2uA_z-\frac{20}{3}w^4r^2\right).
\tag{29}
$$
它也在 whole-$E$/完整 current/natural 的共同核中。
原最高项为
$$
[x^n](r_*^{-5}F_{K_n})
=-\frac8{45}(-1)^n n!\binom{10}{n}.
\tag{30}
$$
特别 $K_2$ 的二次系数为 $-16$。

在左镜点，用 $p=s_*r_*$ 归一后，(28)的两个多项式是
$$
\frac23s_*^2,\qquad
\frac83(s_*x-s_*^2).
$$
它们的次数依次为0、1，非零最高系数只需 $s_*\ne0$。加(30)的 $K_2$，从最高次向下逐项消去即可得到任意 $\operatorname{Pol}_2$。右侧自动同时由(24)匹配。

因此
$$
\boxed{
S_{-6}(\mathcal R_{-6}\cap\ker E\cap\ker\mathscr C)
\supseteq\{(P(x),P(-x)):P\in\operatorname{Pol}_2\}.
}
\tag{31}
$$
这是三个准确原列的三角证明，未重新计算旧响应秩。

## 7. 负四：消费已付七个完整列，再加 K4

用 R443 原 self-column 标签
$$
i=17,22,23,25,26,28,33.
\tag{32}
$$
这不是 R448 重新编号的 basis slot。R462 按原完整标签和 E8/Z 真权核得这七个成本都属于 $\mathcal R_{-4}$；它们已由 R443 证明为独立完整 self 列，且全部保持 whole $E$、完整三尾 current 和 natural。

为明确使用的是整列而非 pivot，按共同单项顺序
$$
(p^4r,\ up^2r^2,\ xp^3r^2,\ xupr^3,\
x^2p^2r^3,\ x^2ur^4,\ x^3pr^4)
\tag{33}
$$
原 complete-Af 输出的完整有理行是：

| 原列 | 七个完整系数，按(33) | 原 source / complete-current 记录 |
|---:|---|---:|
| 17 | $(-1/16,\ 1/16,\ 5/48,\ -1/24,\ -1/16,\ 0,\ 1/96)$ | 21 / 74 |
| 22 | $(-7855/25216,\ 5561/25216,\ 136435/226944,\ -8465/75648,\ -86767/226944,\ -4525/453888,\ 1339/25216)$ | 26 / 79 |
| 23 | $(-669/3152,\ 783/6304,\ 2815/6304,\ -115/2364,\ -4237/12608,\ -73/6304,\ 2719/37824)$ | 27 / 80 |
| 25 | $(463/788,\ -97/197,\ -3775/3546,\ 171/788,\ 20087/28368,\ 829/28368,\ -481/3152)$ | 29 / 82 |
| 26 | $(0,\ 0,\ -1/16,\ 0,\ 11/96,\ 0,\ -1/32)$ | 30 / 83 |
| 28 | $(967/6304,\ -1555/18912,\ -16951/56736,\ 697/18912,\ 9889/56736,\ 697/113472,\ -347/18912)$ | 32 / 85 |
| 33 | $(-205/197,\ 222/197,\ 1639/1182,\ -325/591,\ -667/1182,\ 23/1182,\ -1/591)$ | 37 / 90 |

R443 的七个已付独立列全落在(33)的七维多项式空间，故它们准确张成(33)。这里只使用原独立性证书与完整列的支持；没有另算一个新 rank，也没有从 pivot 名称猜整列支持。

因此同一七成本空间内可以分别取出
$$
p^4r,\qquad xp^3r^2,\qquad x^2p^2r^3,\qquad x^3pr^4.
\tag{34}
$$
在左镜点除以 $r_*^5$ 后，它们为
$s_*^4,s_*^3x,s_*^2x^2,s_*x^3$，恰给整个 $\operatorname{Pol}_3$。这一步不要求某个泛性的 $h_*$，只用实际 $s_*\ne0$。

真权 $-4$ 的 $K_4$ 在(30)中具有非零四次项 $-896x^4$；它的剩余低次项可用(34)消去。于是
$$
\boxed{
S_{-4}(\mathcal R_{-4}\cap\ker E\cap\ker\mathscr C)
\supseteq\{(P(x),P(-x)):P\in\operatorname{Pol}_4\}.
}
\tag{35}
$$
全部成本从起点都是真同权，不是将旧同宽十九行右逆在事后做谱投影。

本节唯一原执行来源为
[R443](R443-complete-self-image-of-the-paid-joint-kernel-and-forty-nine-formal-directions.md) 的 [run 43801705436](https://github.com/Rogerhu12/math-research-public/actions/runs/43801705436)，job 133083261189，source
9c796878a2f7f1b910ebcebadd0b2d05dc0d42ac。
原 stdout 为421834字节，SHA256
d4a266bb80006a56918f21600ecce75ade0b7522ddbfc45459f89958f5b2c1e8；
249个 JSONL 记录为299732字节，SHA256
1ea691a9cb902e6be7bdbf09b892c3f39d665dbd45174a309be7445686611ca8。
表中完整行由机制作者从其已存原记录只读抄取；没有再次下载、生成或运行它们。R443 §4/5 的独立性与 union 证书仍是本节引用的唯一原秩证据。

## 8. 先清完整 current，再清两个 self：证明(1)和(2)

[R454](R454-complete-response-self-principal-trace-and-seven-ordered-current-invariants.md) 对整个原响应空间给出
$$
\boxed{\mathscr C(\mathcal R\cap\ker E)=\ker D_{\rm cur}.}
\tag{36}
$$
$D_{\rm cur}$ 是七项对角多项式读出，不是缩放生成元。对 whole $E$ 和 ordered 零成本，它等于 R457 的自然多项式 $\mathfrak d$。准确协变为
$$
\mathfrak d(\mathsf P_{H,c}V)(x)
=H^{-5}\mathfrak d(V)(Hx+c),\qquad
\mathfrak d(NV)=\mathfrak d(V)'.
\tag{37}
$$
因此真权 $\sigma$ 的值只能是 $c x^{\sigma+5}$，且指数必须在 $0,\ldots,6$。

式(36)给的响应起初可能混权。$\mathcal R\cap\ker E$ 与 current 映射均按真作用稳定，所以用原有限近一正 $H$ 的有号谱投影，可取与目标真正同权的响应。响应完整 natural 恒零，故该响应同时保持 $J_0$ 的另外两部分。这里是成本线性空间中的合法 lift，不声称谱投影系数是正时间。

### 8.1 负六的垂直覆盖

取 $V\in U_{-6}\cap\ker J_0$。由(37)，其 $\mathfrak d$ 必为零，因为允许的多项式没有 $x^{-1}$ 项。故(36)给
$$
R_C\in\mathcal R_{-6}\cap\ker E,\qquad
\mathscr C R_C=\mathscr C V .
$$
$W=V-R_C$ 仍在 $\ker J_0$，且完整 current 零。由(24)(25)，其 self 镜对落在(31)的整个 $\operatorname{Pol}_2$ 图像内。取同权响应 $R_S$ 同时匹配两侧，便有
$$
V-R_C-R_S\in\ker J_{\rm aff}.
$$
第5节保证这里是全部角色和整个有限仿射闭包，不只一个参考点。这证明(1)。

### 8.2 负四的 N 加响应覆盖

取 $V\in U_{-4}\cap\ker J_0$。写
$$
\mathfrak d(V)=c x.
$$
原正特征代表 $H_*$ 在当前加强母库上满足
$$
H_*\in U_0\cap\ker J_0,\qquad
\mathfrak d(H_*)=-\frac3{128}x^5.
\tag{38}
$$
此处 $J_0H_*=0$ 依靠同一初选母的完整 affine $n_2=0$ 及 locality；并非 universal 自然零。

令
$$
\boxed{
Z=-\frac{16c}{45}N^3H_*
\in U_{-3}\cap\ker J_0 .
}
\tag{39}
$$
由(37)，
$$
\mathfrak d(N^4H_*)=-\frac{45}{16}x,\qquad
\mathfrak d(NZ)=cx .
$$
所以 $V-NZ$ 的完整 current 落在(36)的核内。取同权 $R_C$ 匹配它，再用(35)取同权 $R_S$ 匹配剩下的完整 self 镜对，得到
$$
V-NZ-R_C-R_S\in\ker J_{\rm aff},
$$
即(2)。

这里使用的是已经真实处于 $\ker J_0$ 的 $N^3H_*$，不是一个只在 $\mathfrak d$ 像里存在的 $x^6$ 前像。式(39)保留全部 $n_2$ 原端项；消掉它的原因是当前库所规定的整条 affine 查询，不是只看偶性或 principal 项。

## 9. 两个增强负权正字符因此全部排除

设 $\lambda$ 是经同一个 $J_{\rm aff}$ 下降的正仿射字符，真权为 $-6$ 或 $-4$。原响应 lineality 与平移字符条件给
$$
\lambda(\mathcal R)=0,\qquad \lambda N=0.
\tag{40}
$$
若其权为 $-6$，(1)使它杀 $U_{-6}\cap\ker J_0$。若其权为 $-4$，(2)再用(40)，得到相同结论。

由于 $\ker J_0$ 真权稳定，单权 $\lambda$ 因而杀整个 $\ker J_0$；它可下降为旧 $J_0(U)$ 上的同权正仿射字符。原成本锥未变，故正性仍是对同一真实成本的正性。[R433 §4](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md) 已在同一母库排除了这两权。于是
$$
\boxed{
\lambda\text{ 经 }J_{\rm aff}\text{ 下降且权为 }-6,-4
\quad\Longrightarrow\quad\lambda=0 .
}
\tag{41}
$$

本文不重算 R433 的十四正规族、static/速度/加速度 action 或同一个八矩乘子。新支付的是它们原本不能免费越过的 partial 接口：通过(1)(2)把任何新增强字符严格送回旧共同商。没有用旧自然投影一致直接删除新行。

## 10. 满闭锥的准确末条件是两个 self 类的联合关系

令
$$
\mathcal W_0=U_0\cap\ker E\cap\ker\mathscr C,\qquad
\mathcal K_0=\mathcal R_0\cap\ker E\cap\ker\mathscr C.
$$
R465 给 $\dim\mathcal W_0=7,\dim\mathcal K_0=5$，并固定完整原代表
$$
V_H\equiv H_*+J_4,\qquad
V_Y\equiv J_4-J_6
\pmod{\mathcal R_0\cap\ker E},
$$
以同一真实响应清其完整 current。令 $S$ 为两个完整 self partial 的平移多项式映射，置
$$
\mathfrak h=[S(V_H)],\qquad
\mathfrak y=[S(V_Y)]
\quad\text{于 }S(\mathcal W_0)/S(\mathcal K_0).
\tag{42}
$$
它们是准确的两类，不以单独最高项替代整个 self。

原 R127/R145 的字符提取在(5)上合法。可能的偶权为
$-8,-6,-4,-2,0,2$：

- $-8$ 已由 R465(49)在同一个增强上支付；
- $-6,-4$ 由(41)支付；
- $-2$ 用原 R188 的整个 $U$ 正字符排除；
- $2$ 用 R190 的完整 $U_2=\mathcal R_2$；
- 真权0的正字符按 R196 只能是 $\lambda_+$ 的正倍数。

这一使用保持真实锥的端口无关证明：桥成本通过正整数重复后的闭锥极限处理，不作为有限实际成本删去。闭锥与实际半群仍是不同对象。

R465 的完整零权同构给
$$
Q_0/NQ_1
\simeq S(\mathcal W_0)/S(\mathcal K_0),\qquad
Q=J_{\rm aff}(U)/J_{\rm aff}(\mathcal R),
\tag{43}
$$
且 $\lambda_+(V_H)=1,\lambda_+(V_Y)=0$。因此
$$
\begin{aligned}
\lambda_+\text{ 不经 }J_{\rm aff}\text{ 下降}
&\Longleftrightarrow
\exists\,a\ne0,b:\ a\mathfrak h+b\mathfrak y=0\\
&\Longleftrightarrow
\mathfrak h\in\operatorname{span}\{\mathfrak y\}.
\end{aligned}
\tag{44}
$$
第一步使用完整 $J_{\rm aff}$ 核：R465 已证明其零权部分在 $\mathcal W_0$ 中恰为 $\ker S$，不是仅用某个 signed 列有 $\lambda_+=1$。

若(44)成立，全部候选正字符都被排除，有限维稳定闭锥只能是整个像。若不成立，$\lambda_+$ 确实下降为一个非零正泛函，闭锥不满。因此得到(3)。

这还区分两个实际有意义的情况：

- $\mathfrak h\notin\operatorname{span}\{\mathfrak y\}$：原 canonical 正时长、同端口、$M=0$ 成本满足
  $\lambda_+=L+\int(h_s/h)^2ds>0$。它不能同时使整个 $J_{\rm aff}$ 为零。这是同一增强下的真实正性障碍。
- $\mathfrak h\in\operatorname{span}\{\mathfrak y\}$，但至少一类非零：闭锥已经满，不过(43)仍可有非零余商。原 $DQ+NQ$ 的现成双参数截面不能直接调用；这不证明其它 actual 构造不可能。

因此后继四个新 self 目标的消费必须保**两目标的共同商关系**。两个分别的 MEMBER 布尔值不足以区分“都非成员但彼此成比例”与“正字符仍下降”。本文没有预报哪种结果发生。

## 11. 两成员都过时，原双参数 actual 构造在同一 Jaff 上闭合

若同一加强母库的新完整比较给
$$
\mathfrak h=\mathfrak y=0,
\tag{45}
$$
则(43)给 $Q_0=NQ_1$。非零真权上 $D$ 可逆，所以
$$
DQ+NQ=Q.
\tag{46}
$$
同时(3)给同一 $J_{\rm aff}$ 的满闭锥。

这恰是 [R463](R463-real-partial-quotients-translation-defect-and-finite-affine-control-interface.md) 双参数引理的两个独立前提。使用的是同一有限商上的真实
$\mathsf P_{e^{t_i},c_i}$ 原型族，不能先在较小商取缩放截面，再加一个独立 partial 截面。

全部 finite actual 步骤继续按原式：

1. 选同一增强商的有限正配平原型；真桥与真倒行给
   $2V_{A_i(t_i,c_i)}+n_i\mathsf P_{e^{t_i},c_i}V_{B_i}$。
   桥项是实际 $O(1)$，保其全部新旧目标。
2. 以一个固定有限重复数得到第一个完整商 $C^1$ 截面，并先清全部响应原型的**完整**商基准。
3. 共享原型、真倒行与第二次完整商校正保留共同 $E_0$、各原型成本及第二校正的全部响应分量。
4. 最后在响应坐标作原有限重复收缩；Klein 背景仍为
   $V_{\rm base}+4V_{\mathscr D}$，目标准确取
   $-J_{\rm aff}(V_{\rm base})/4$。

所有真实词、紧参数盒、辅助 profile、原锚和保护芽从起点纳入同一共同合法窗口。若 R467 再加 $M_3\ne0$、外八行或最高 $d$ 的非零条件，必须对**同一**初选母库完成(45)，不能搬用另一个库的成员收据。本文不改变原固定 hook、incoming history、Morse、metric、九/十三行 gauge 或端 germ 的独立要求。

## 12. 已完成与唯一剩余的新比较

本文已完整付清：

- 换锚 self 身份(16)，包含真实二阶仿射尾、输出二次差与所有正规化项；
- 消去 whole-$\mathcal Q$ 后仍保 total/ordered 项的镜像式(19)；
- 在准确共同核内的整个平移 mirror graph(24)，及负六/负四次数界；
- 真同权响应对 $\operatorname{Pol}_2$、$\operatorname{Pol}_4$ 的完整覆盖；
- 同一 $J_{\rm aff}$ 上的(1)(2)与两个新增强负权正字符排除；
- 闭锥充满的准确联合条件(3)，以及两成员都过时可用的 actual 双参数接口。

仍未付的是 R465 指定的两个完整零权 self 类在同一个五维响应像中的实际关系。机制作者正在准备的四目标消费应保持完整原成本、same current 补偿、完整镜对和共同有理关系；它不能只重做旧 rank，也不能从形式 current 零反造 self。

本稿不以编号或阶段结束代替研究结论。下一决定点已经变为这两个明确完整类的共同关系；没有必要再次评价已付自然负权族或重跑 R443 的全秩。
