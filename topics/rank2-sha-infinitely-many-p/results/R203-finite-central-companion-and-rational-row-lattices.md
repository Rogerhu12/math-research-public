# R203. 有限中央伴随格、全部归一方向的有理化与第四层原输入

日期：2026-11-12。**状态：有限中央整格、半带内全部方向的准确整
行等价，以及第四层矩阵展开均已证明。** 尚未得到第四整化格的
一般核，也未证明跨素数的中央非零。

## 1. 同一原中央数据

取 $p=4r-1\ge7$，排除 $11$，置
$$
 R=r(p-1),\qquad q_p=(p-1)/2,\qquad
 a=17pu_0\in\mathbb Z_p^\times,\qquad b=17u_0=a/p.
 \tag{1}
$$
本篇的 $a,b$ 是这两个标量。原函数仍是 $A=A_2$、$C=B-A$，
共同整轴为 $f,c$。记
$$
 v_s=([y^{rs}]f,[y^{rs}]c)\in\mathbb Z_p^2,\qquad
 R_s=([w^{rs}]A,[w^{rs}]C)\in\mathbb Q^2.
 \tag{2}
$$
R185 的实际完整 Stokes 权满足
$$
 \omega_1=1,\qquad
 \omega_s=(-1)^{s-1}(s-1)!b^{1-s}(1+p^{q_p}\mathbb Z_p)
                                  \quad(s\ge2).
 \tag{3}
$$
所有 $\omega_s$ 都是原泛函所定义的确定数，本文不选择这些单位。
置
$$
 Q_h=\sum_{s=1}^h\omega_s v_s,\qquad
 L_h=\sum_{s=1}^h(-1)^{s-1}(s-1)!b^{1-s}v_s.
 \tag{4}
$$
当两个原完整中央导数均为零时，R185 给
$Q_h\in p^{h+v_p(h!)}\mathbb Z_p^2$。

以下始终取
$$
                       1\le N\le q_p+1=(p+1)/2<p.            \tag{5}
$$
由 (3)，$Q_h-L_h\in p^{q_p+1}\mathbb Z_p^2$，故双完整零
在此范围内给 $L_h\in p^h\mathbb Z_p^2$。

## 2. 有限中央条件的准确整伴随格

对任意给定的整向量 $v_1,\ldots,v_N$，在 $\mathbb Q_p^2$ 中
定义
$$
 t_h=\frac{(-b)^{h-1}}{p\,h!}L_h,\qquad t_0=0.
 \tag{6}
$$
直接相减相邻的 (4)，得到准确递推
$$
 \boxed{\qquad v_h=p h\,t_h+a\,t_{h-1},
                        \qquad1\le h\le N.\qquad}            \tag{7}
$$

**定理 1。** 在 (5) 中，下列条件等价：
$$
 L_N\in p^N\mathbb Z_p^2;\qquad
 L_h\in p^h\mathbb Z_p^2\ (h\le N);\qquad
 t_h\in\mathbb Z_p^2\ (h\le N).
 \tag{8}
$$
等价条件也可写成：原向量列 $(v_h)$ 属于整双对角矩阵
$$
 B_N=
 \begin{pmatrix}
 p&0&\cdots&0\\
 a&2p&\cdots&0\\
 0&a&\ddots&\vdots\\
 \vdots&\ddots&\ddots&Np
 \end{pmatrix}
 \tag{9}
$$
在两个坐标上分别作用的像。其非零 Smith 指数准确为
$$
                    \boxed{0^{\times(N-1)},\ N.}             \tag{10}
$$

**证明。** $L_N-L_h$ 的每个 summand 的赋值至少 $h$，因为
$s\ge h+1$ 且 $v_p(b^{1-s})=s-1$；此处所有阶乘均为单位。
故第一个条件推出全部较短条件。式 (6) 给
$v_p(t_h)=v_p(L_h)-h$，证明其余等价，(7) 则给 (9)。

矩阵 (9) 的行列式为 $p^N N!$，赋值为 $N$。取第
$2,\ldots,N$ 行与第 $1,\ldots,N-1$ 列，所得 minor 为
$a^{N-1}$，是单位。故前 $N-1$ 个 Smith 指数均为零，
最后一个为 $N$。$N=1$ 直接成立。$\square$

因 $Q_N-L_N\in p^{q_p+1}\mathbb Z_p^2$，(8) 的第一个条件
在 (5) 内也等价于原 $Q_N\in p^N\mathbb Z_p^2$。
这是一份有限中央数据的准确整格描述，不把这些数据当成原
$E_D$ 中独立可选的多项式列。

令 $Y=y^r$，则 (7) 还给
$$
 \sum_{s=1}^N v_sY^s
   =p(Y\partial_Y+bY)\sum_{s=1}^N t_sY^s
                              \pmod{Y^{N+1}}.                \tag{11}
$$
这与 R62 的中央 Euler 原函数递推相容；新付出的内容是整格
(8)–(10)，以及下节对真实完整权的整行等价。

## 3. 原完整归一方向与 t 行的 GL_N 整等价

不再以有限精度同余代替目标格。令
$$
 \mathsf U_N=
 \begin{pmatrix}p^{-1}Q_1\\p^{-2}Q_2\\\vdots\\p^{-N}Q_N\end{pmatrix},
 \qquad
 \mathsf T_N=
 \begin{pmatrix}t_1\\t_2\\\vdots\\t_N\end{pmatrix}.             \tag{12}
$$

**定理 2。** 对实际确定的全部权 (3)，有准确恒等式
$$
       \boxed{\qquad \mathsf U_N=M_N\mathsf T_N,\qquad
                            M_N\in\operatorname{GL}_N(\mathbb Z_p).
                    \qquad}                                 \tag{13}
$$
因此两者生成同一个 $\mathbb Z_p$ 行格；当它们整时，所有非零
Smith 指数相同，而不只是某个行列式赋值相同。

**证明。** 将 (7) 代入 (4)。矩阵 $M_N$ 下三角，其对角为
$$
 d_h=\frac{h\omega_h}{p^{h-1}}\in\mathbb Z_p^\times,             \tag{14}
$$
$j<h$ 的条目为
$$
 e_{h,j}=\frac{p j\omega_j+a\omega_{j+1}}{p^h}.                 \tag{15}
$$
置
$\omega_j^0=(-1)^{j-1}(j-1)!b^{1-j}$。因 $a=pb$，准确有
$p j\omega_j^0+a\omega_{j+1}^0=0$。用 (3) 的相对误差，
并取 $\omega_1/\omega_1^0=1$，得到
$$
              v_p(e_{h,j})\ge q_p+j-h\ge0                    \tag{16}
$$
（最后一步用 $h\le q_p+1,j\ge1$）。
故 $M_N$ 整且对角均为单位，证明 (13)。$\square$

式 (16) 也是本篇范围的原因：超过半带后，首列不再由现有权
精度保证整。这里没有将该范围无证延长。

## 4. t_h 只由原有理 w 系数构成

因为 $Nr\le R$，R199 的准确第一带给
$$
 \sum_{s=1}^N R_sY^s
   =e^{bY}\sum_{s=1}^N v_sY^s\pmod{Y^{N+1}}.
 \tag{17}
$$
把 (11) 代入，并保留零初值，得
$$
 \sum_{s=1}^N R_sY^s
     =pY\partial_Y\left(e^{bY}\sum_{s=1}^N t_sY^s\right)
                                                 \pmod{Y^{N+1}}.
$$
逐项积分因此给出完全显式的原有理行
$$
 \boxed{\qquad
 t_h=\frac1p\sum_{j=1}^h
                \frac{(-b)^{h-j}}{j(h-j)!}\,R_j,
                           \qquad 1\le h\le N.               \qquad} \tag{18}
$$
$u_0$ 本来就是 R174 的原有理 $r$ 阶系数，故 $b$ 及 (18)
均为有理数。没有输入未知 $p$ 进周期、调节子或 Stokes 单位。
式 (13) 则证明这些有理行准确保留原归一目标格。

特别
$$
 t_1=\frac{R_1}{p},\qquad
 t_2=\frac{R_2-2bR_1}{2p},\qquad
              \det(t_1,t_2)=\frac{\det(R_1,R_2)}{2p^2}.
 \tag{19}
$$
R195 已证明这个行列式非零。用原 Hurwitz 两阶的阶乘赋值
$1,2$，得到
$$
                     v_p\det(t_1,t_2)=v_p(\Delta_p)-5.        \tag{20}
$$
$C=B-A$ 是整行列式一的列变换，因此这里的 $\Delta_p$ 正是
R195/R197 的同一个原 $A,B$ 双权行列式。

若双完整零成立，$\mathsf T_N$ 整；当 $N\ge2$，其行秩为二。
记 Smith 指数为 $\kappa_{1,N}\le\kappa_{2,N}$。由 (13)，
R189 对全部归一中央方向的源 Hasse 恢复损失可准确用
$$
                     \kappa_{2,N}+\lfloor\log_pD\rfloor      \tag{21}
$$
表示。增大 $N$ 只扩大同一个整行格，所以
$\kappa_{2,N}$ 不增。所需原加权 core 的读取精度和窗口仍须按
R189 支付；(21) 不把它们变成已观测的曲线前缀。
即使 $\kappa_{2,N}=0$，也不能从中单独推出完整中央导数非零。

## 5. 前三中央项删除后的真实第四层输入

本节设 $3\le N\le(p+1)/2$，并假设两个完整中央导数均为零，
从而所有 $t_s$ 都整。定义一个明确的辅助轴
$$
 (f^{[N]},c^{[N]})=(f,c)-\sum_{s=1}^N v_s y^{rs}.
 \tag{22}
$$
使用同一个标量 $b$、同一个原有限次数空间 $E_D$、同一归一
目标行。将 (22) 代入 R199 的准确公式定义 $J^{[N]}$。
它只是同源比较矩阵，不被当成另一条已知全局椭圆曲线。

对整方向 $t_s$ 记 $D_{t_s}$ 为原 $A,C$ 方向导数。若 $h\ge s$，
定义整线性行
$$
 \mathcal T^s_{h,l}(P)=
 \frac{a^{h-s}}{(h-s)!}[y^l]D_{t_s}
 \left\{s\mathcal E^{h-s}+(h-s)\mathcal E^{h-s-1}\right\}
                P(f^{[N]},c^{[N]}).
 \tag{23}
$$
$h<s$ 时置零；当 $h=s$，花括号中第二项置零，不读取
$\mathcal E^{-1}$。以下 $h\le p-2$，故所有阶乘为单位。
方向导数与 $\mathcal E$ 的顺序如 (23)，不擅自交换。

**定理 3。** 对原第一带行 $rh+l$、$0\le l<r$，有准确同余
$$
 \boxed{\quad
 (J-J^{[N]})_{rh+l}(P)\equiv
 p^2\mathcal T^1_{h,l}(P)
 +p^3\left\{\mathcal T^1_{h-1,l+r}(P)
                         +\mathcal T^2_{h,l}(P)\right\}
                                      \pmod{p^4\mathbb Z_p}.
 \quad}                                                       \tag{24}
$$
这对任意 $D$ 和同一个原 $P\in E_D$ 成立。

**证明。** 由 (7)，中央轴扰动中的 $t_s$ 成对出现为
$$
                 t_s\{p s\,y^{rs}+a\,y^{r(s+1)}\}.             \tag{25}
$$
末端 $t_N$ 的第二项是否删除只在 $N+1$ 带产生影响，此处
$N\ge3$，因而不进入模 $p^4$ 的计算。

对原多项式使用整 Hasse Taylor 展开。将 (25) 的一次项代入
R199 公式，在额外角向进位 $j\ge0$ 处，得到
$$
                p^{s+1+j}\mathcal T^s_{h-j,l+rj}(P).          \tag{26}
$$
其第二个 Euler 项来自相邻的 $s+1$ 带；这正解释 (23) 的
两个项及其系数。

所有二次及以上 Hasse 项都从 $p^4$ 开始。最浅的三种二次
选择分别为：两个 $y^r$ 项自身各含一个 $p$，加上两次带移位；
$y^r$ 与 $y^{2r}$ 自身含一个 $p$，加上三次带移位；
两个 $y^{2r}$ 有四次带移位。更高选择只增加深度。
这不涉及除以 $D!$。故 (26) 中只有
$(s,j)=(1,0),(1,1),(2,0)$ 留在模 $p^4$ 中，得到 (24)。
$\square$

这里 $J^{[N]}$ 删除了至少前三中央项。若仅删除前两项，
则 (24) 的 $\mathcal T^2$ 只保留
$2a^{h-2}D_{t_2}\mathcal E^{h-2}/(h-2)!$，不能保留来自
删除第三项的另一个 Euler 项。两种辅助矩阵的第四层不同。

## 6. 第四层仍保留原源的下一位

设 $p\ge19$，$k=rq+s$，$\lceil r/2\rceil\le q\le p-2$，
$2\le s\le r-2$，并保持本篇的完整中央消失假设。
R201 在这些中间角向前缀证明了
$\Lambda_3(J)=\Lambda_3(J^{[2]})$。又
$J^{[N]}-J^{[2]}\in p^3\operatorname{Hom}(E_D,\mathbb Z_p^k)$，
所以相同前缀上也有 $\Lambda_3(J)=\Lambda_3(J^{[N]})$。

对这个共同格中的 $x$，置 $P=p^3x\in E_D$。式 (24) 除以
$p^3$ 给第四层的真实输入
$$
 (J-J^{[N]})(x)\equiv
 p^{-1}\mathcal T^1(P)
       +\mathcal T^1_{\mathrm{shift}}(P)+\mathcal T^2(P)
                                                   \pmod p,
 \tag{27}
$$
其中 shift 准确为 (24) 的 $(h-1,l+r)$。
共同第三格使 $\mathcal T^1(P)\in p\mathbb Z_p$，因此第一项
确实整。但其除后值仍需要 $P\bmod p^2$ 及该行本身的
$p^2$ 精度，不能仅由 $\overline P$ 计算。
本篇没有把第三层的未来两行消去直接搬到第四层，也未证明
(27) 的新核或其净范数收益。

依赖：

- [R62 的原 Euler–Stokes 规范](R62-actual-euler-primitive-stokes-constants.md)。
- [R185 的实际完整权及误差](R185-integral-axis-stokes-functional-and-complete-central-tests.md)，(20)、(28)–(31)。
- [R189 的联合 Hasse 整格](R189-complete-central-hasse-families-and-weighted-core.md)。
- [R195 的首次两行独立性](R195-fixed-five-adic-moments-and-first-two-central-rows.md)。
- [R199 的准确第一带及全原源公式](R199-exact-first-band-exponential-and-complete-divided-image.md)。
- [R201 的真实第三层 Schur](R201-double-central-perturbation-and-third-layer-schur.md)。

本篇的有理化完全保留实际目标格。无穷素数非零与严格全次数
预算仍然开放。
