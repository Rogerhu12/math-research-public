# R252：另外两个完整 Gaussian 面积槽排除现有偶微包圆的全部例外端芽

日期：2026-11-15。**已证明，纯纸面结论。** 没有执行新的 profile 求积、符号目标、参数扫描、函数秩或几何计算。

[R251](R251-nonresonant-Gaussian-area-obstruction-and-two-exceptional-curves.md) 的 $A_{-2,-3}$ 槽留下两条准确退化曲线。本稿使用另外两个完整面积槽 $A_{-1,-3}$、$A_{-1,-2}$，证明 R239 所构造的偶微包双 block 圆在整个 $b=0$ 例外端芽族、所有 $\varepsilon>0$ 上仍不能完成第四 ruling。

这不是对所有圆或所有 germ 的否定。新的第二个面积门还用到该具体构造的中心偶性与正坐标放置；一般三矩圆的普通复四次矩仍可能相消。

来源：[R73 原八矩及真实第三 history](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R224 偶部 gauge 商](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)、[R239 偶微包不可分离圆](R239-nonseparable-third-order-circles-paying-four-exceptional-energy-gates.md)、[R245 完整 Gaussian history](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)、[R248 第四谐波](R248-complete-fourth-harmonics-and-complementary-block-reduction.md)、[R249 真实词独立性及完整面积系数](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)和 R251。

## 1. 固定数据与完整结论

固定共同物理区间 $I=[\ell,r]$、原右锚、左右零 collar，以及真实例外端芽

$$
\kappa\ne0,\qquad h_e>0,\qquad \varepsilon>0,\qquad
H=e^{\varepsilon\sigma^2},
$$

$$
h=h_eH,\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=\frac{\kappa}{h}.
\tag{1}
$$

这里不要求共振 $\varepsilon=\kappa^2/4$。实际物理支条件照常保留；本稿也不重新主张任意大参数都能在某个预给全局几何内安装。

令 $q=f+ig$，其中 $(f,g)$ 是合法三矩圆。因此同一全区间上的普通复矩满足

$$
\int_I(q'')^2=0,\qquad
\int_Ix(q'')^2=0,\qquad
\int_I\{x^2(q'')^2+2(q')^2\}=0.
\tag{2}
$$

记三个局部四次积分

$$
M_4(q)=\int_I(q'')^4,\qquad
M_1(q)=\int_Ix(q'')^4,\qquad
N_1(q)=\int_Iq'(q'')^3.
\tag{3}
$$

它们都不是 Hermitian 量。

**定理。** 若 (2) 成立，并且

$$
M_4(q)\ne0,\qquad N_1(q)=0,\qquad M_1(q)\ne0,
\tag{4}
$$

则对任意具有 (1) 的真实几何，完整第四谐波的偶部不能同时落入允许的三矩 gauge 空间。因而不能由允许的二、三阶 homogeneous gauge 完成第四 ruling。

R239 在所取偶 bump、正坐标微包及两互补旋转角的范围内满足 (4)。所以其已付三矩、完整第三槽及六能量零的双 block 圆，在 (1) 的全部正 $\varepsilon$ 上仍有严格完整 ruling 障碍。

## 2. 两个新的面积槽及其唯一完整来源

沿用 R249 的同中心原函数

$$
E_s(\sigma)=\int_0^\sigma H(t)^s\,dt,\qquad
K_{st}(\sigma)=\int_0^\sigma H(t)^sE_t(t)\,dt,
\qquad A_{st}=K_{st}-K_{ts},
$$

其中字母 $s,t\in\{1,-1,-2,-3\}$。所有负 Gaussian 原函数的真实常数尾保留；没有以无穷远极限重锚。

在 $\mathbb F=\mathbb R(\sigma,H)$ 上，R249 已证明这些同锚二重词的真实独立性。证明只需要 $\varepsilon\ne0$。R245 的完整恢复给

$$
\Phi_m=Q_\sigma+\sum_sE_sB_s,
$$

其中 $Q_\sigma$ 是奇 Laurent 局部项。令

$$
\mathfrak P_\sigma(q)
=-\mathfrak b_\sigma(Z(q,q),Z(q,q))
-4\mathfrak b_\sigma(Y_q,C(q;q,q)).
\tag{5}
$$

R248 的完整第四 $e^{-4i\theta}$ 系数是 $\mathfrak P_\sigma(q)/16$。原第三 history 的二重部分准确为

$$
(W_C)_{\mathrm{two}}
=-\sum_{s,t}K_{st}B_s(q,B_t(q,q)).
$$

所以整个 (5) 的 $A_{st}$ 系数为

$$
\boxed{-2\mathcal E_\sigma\bigl(q,[B_s,B_t]_\Delta(q)\bigr).}
\tag{6}
$$

这里

$$
[X,Y]_\Delta(q)=X(q,Y(q,q))-Y(q,X(q,q))
$$

是双线性 profile 算子的对角三次交换子，并非八矩矩阵的矩阵交换子。

式 (6) 是完整系数：$Z^2$ 只给对称二重乘积；第三局部分子和 chain 只给至多一重 history；奇 Laurent 的交叉原函数由 R245 归约到同一低层。真实中心入值也不能增添一个新的反对称二重槽。因此下面没有只抽取某个未经其余项核对的候选项。

对任何可能带左尾的第三 profile $\tau$，原第一场能量仍准确为

$$
\mathcal E_\sigma(q,\tau)
=\frac{1+j^2}{4h}m_0(q,\tau)
+\frac j2m_1(q,\tau)
+\frac h4m_2^*(q,\tau),
\qquad j=2\varepsilon\kappa\sigma^2,
\tag{7}
$$

$$
m_0=\int_Iq''\tau'',\qquad
m_1=\int_Ixq''\tau'',\qquad
m_2^*=\int_I\{x^2q''\tau''+2q'\tau'\}.
$$

这保留了全部三个真实矩。因 $H$ 对 $\mathbb R(\sigma)$ 超越，(7) 恒为零必有

$$
m_0(q,\tau)=0.
\tag{8}
$$

没有把未知的另两个矩置零来得到 (8)。

## 3. $E_{-1}$ 的两个准确八矩坐标

记 $u=\kappa^2>0$，并沿用 R251 的系数

$$
B_{-2}=a\Phi_{r_1}+b\Phi_{s_0},\qquad B_{-3}=c\Phi_{r_0},
$$

$$
a=\frac{\varepsilon(16-36u)-93u^2-8u-16}{128h_e^2},
\qquad
b=-\frac{u(9u+4+32\varepsilon)}{32h_e^2},
\tag{9}
$$

$$
c=\frac{\kappa\{\varepsilon(36-84u)-20u^2-9u-27\}}
{216h_e^3}.
\tag{10}
$$

新的 $E_{-1}$ 系数只落在 $\Phi_{p_0},\Phi_{s_1}$：

$$
\boxed{
B_{-1}=d_-\Phi_{p_0}+e_-\Phi_{s_1},\qquad
d_-=\frac{6\kappa^3}{h_e},\qquad
e_-=-\frac{\kappa(14u+1+4\varepsilon)}{4h_e}.
}
\tag{11}
$$

这里 $d_-,e_-$ 是固定算子系数，不与 R73 的几何量 $d,e$ 混用。

直接来源如下。R73 的 raw 密度在 (1) 上给

$$
M_{p_0}=\frac{-\kappa+j-\kappa j^2+j^3}{2h_e}H^{-1},
$$

$$
M_{s_1}=\frac{(u-1-4\varepsilon)j-j^3}{4h_e}H^{-1}.
\tag{12}
$$

第二式保留了 $\gamma d_s/h^2$ 项；它使用
$d_s=4\varepsilon\kappa\sigma$，不是常态外推。其他六坐标没有 $H^{-1}$ 指数。

R251 的准确 Gaussian 分部积分规则在指数 $-1$ 时，把 $1,j,j^2,j^3$ 的原函数余系数分别送为

$$
1,\quad\kappa,\quad3\kappa^2,\quad15\kappa^3.
$$

代入 (12) 即得 (11)。特别

$$
\boxed{d_-+7e_-=-\frac{\kappa(74u+7+28\varepsilon)}{4h_e}\ne0.}
\tag{13}
$$

## 4. 六个交叉矩：从原算子到同锚分部积分

暂记

$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad T=\Phi_{s_1},
$$

并令 $r_q=q''$、$v_q=q'$、$t_q=q'''$、$A=J(r_q^2)$，其中 $J=\int_x^r$ 为原正右积分。

R73 的完整算子给

$$
P(q,q)=A,\quad
R(q,q)=v_q^2+xA,\quad
S(q,q)=J(xr_q^2),
$$

$$
L(q,q)=qv_q-\frac x2v_q^2-\frac{x^2}4A
+\frac14J(x^2r_q^2+2v_q^2),
$$

$$
T(q,q)=xv_q^2+xJ(xr_q^2)
+\frac12J(x^2r_q^2+2v_q^2).
\tag{14}
$$

其二阶导数准确为

$$
\begin{aligned}
(P(q,q))''&=-2r_qt_q,\\
(R(q,q))''&=2(v_q-xr_q)t_q,\\
(S(q,q))''&=-r_q^2-2xr_qt_q,\\
(L(q,q))''&=(q-xv_q)t_q-\frac12(xr_q^2+A),\\
(T(q,q))''&=(2xv_q-3x^2r_q)t_q+2v_qr_q-2xr_q^2.
\end{aligned}
\tag{15}
$$

式 (2) 确保 (14) 中五个二次输出都在左 collar 也为零，故它们确为紧 profile。后面的变分沿这些方向进行是合法的。这里使用的是完整三矩条件，不是仅凭第一个矩便假定所有二次输出紧支撑。

定义三个 cubic 泛函

$$
R_3=\int_Ir_q^3,\qquad
N_3=\int_Iv_qr_q^2,\qquad
X_3=\int_Ixr_q^3,
$$

以及 $\mathcal F_X(q)=m_0(q,X(q,q))$。由 (15) 同锚分部积分，

$$
\mathcal F_P=0,\qquad
\mathcal F_R=\mathcal F_S=-\frac13R_3,\qquad
\mathcal F_L=-\frac12N_3,\qquad
\mathcal F_T=N_3-X_3.
\tag{16}
$$

这些 cubic 身份本身对紧 $q$ 成立。对紧方向 $Y(q,q)$ 求变分，利用 $m_0$ 的对称性，得到

$$
2m_0(q,[X,Y]_\Delta(q))
=D\mathcal F_X(q)[Y(q,q)]
-D\mathcal F_Y(q)[X(q,q)].
\tag{17}
$$

为明确每次分部积分，所需变分表为：

| 方向 | $DN_3$ | $DX_3$ | $DR_3$ |
|---|---:|---:|---:|
| $P(q,q)$ | $M_4/3$ | $3M_4/2$ | 不需要 |
| $R(q,q)$ | $-2N_1/3+M_1/3$ | $-2N_1+M_1$ | 不需要 |
| $S(q,q)$ | $-2N_1/3+M_1/3$ | $0$ | 不需要 |
| $L(q,q)$ | 不需要 | 不需要 | $-M_1/2$ |
| $T(q,q)$ | 不需要 | 不需要 | $4N_1-7M_1/2$ |

例如，未删除的 primitive 项先给

$$
\int_I A r_q^2
=\frac12\left(\int_Ir_q^2\right)^2=0.
\tag{18}
$$

在 $DN_3[R(q,q)]$ 中它的系数是 $+1$；在
$DR_3[L(q,q)]$ 中是 $-3/2$。式 (18) 是先准确求出左尾、再用合法矩置零。其余项只需

$$
\int_Iv_qr_q^2t_q=-\frac13\int_Ir_q^4,\qquad
\int_Ixv_qr_q^2t_q=-\frac13(N_1+M_1),
$$

$$
\int_Ix^2r_q^3t_q=-\frac12M_1,
\qquad
\int_Iv_q^2r_qt_q=-N_1.
\tag{19}
$$

所以 (16)—(19) 给以下全部六个所需矩：

$$
\boxed{
\begin{aligned}
m_0(q,[P,L]_\Delta)&=\frac1{12}M_4,\\
m_0(q,[P,T]_\Delta)&=\frac7{12}M_4,\\
m_0(q,[L,R]_\Delta)&=\frac16(N_1-M_1),\\
m_0(q,[L,S]_\Delta)&=\frac16(N_1-M_1),\\
m_0(q,[T,R]_\Delta)&=\frac43N_1-\frac{11}{12}M_1,\\
m_0(q,[T,S]_\Delta)&=\frac13N_1-\frac5{12}M_1.
\end{aligned}
}
\tag{20}
$$

内层二次输出紧支撑不意味着最后的三次交换子也没有左尾。本稿不作这个推断；三次输出的全部尾仍由 (7) 保留。

## 5. $A_{-1,-3}$：只要 $c\ne0$，就必须有 $M_4=0$

由 (11)、(20)，

$$
m_0(q,[B_{-1},B_{-3}]_\Delta)
=-\frac{c(d_-+7e_-)}{12}M_4(q).
\tag{21}
$$

由 (13)，$d_-+7e_-$ 对全部正 $\varepsilon$ 都不为零。因此真实面积独立性、完整系数 (6) 和 (8) 给

$$
\boxed{c\ne0\quad\Longrightarrow\quad
\text{完整第四 ruling 必须满足 }M_4(q)=0.}
\tag{22}
$$

这已经包括 R251 的 $a+3b=0$ 曲线上所有 $c\ne0$ 的点。不必继续把第二条曲线当作当前证据的例外。

## 6. $A_{-1,-2}$：$c=0$ 曲线上的准确非零系数

剩下的正参数只可能为

$$
0<u<\frac37,\qquad
\varepsilon=\varepsilon_c(u)
=\frac{20u^2+9u+27}{36-84u}.
\tag{23}
$$

由 (20)，

$$
\begin{aligned}
12m_0(q,[B_{-1},B_{-2}]_\Delta)
={}&\{2d_-(a+b)+4e_-(4a+b)\}N_1\\
&-\{2d_-(a+b)+e_-(11a+5b)\}M_1.
\end{aligned}
\tag{24}
$$

令

$$
\mathscr D=2d_-(a+b)+e_-(11a+5b).
\tag{25}
$$

我们现在在整条 (23) 上准确证明 $\mathscr D\ne0$，不依赖数值求根或曲线采样。

写

$$
d_-=\kappa d_0,\qquad e_-=-\kappa e_0,\qquad
d_0=\frac{6u}{h_e}>0,\qquad
e_0=\frac{14u+1+4\varepsilon}{4h_e}.
$$

首先 $e_0>d_0$，因为在 (23) 上

$$
1+4\varepsilon_c-10u
=\frac{8(115u^2-51u+18)}{36-84u}>0.
\tag{26}
$$

分母为正；分子二次式首项正、判别式
$51^2-4\cdot115\cdot18<0$。

其次，由 (9)，$b<0$。并且

$$
3a+b=
\frac{\varepsilon(48-236u)-315u^2-40u-48}{128h_e^2}<0.
\tag{27}
$$

若 $u\ge12/59$，(27) 的严格负号直接成立。若
$0<u<12/59$，将 $\varepsilon=\varepsilon_c(u)$ 代入，其分子乘以正数 $36-84u$ 后准确是

$$
21740u^3-9144u^2-3348u-432.
\tag{28}
$$

此时 $21740u<21740\cdot12/59<9144$，所以 (28) 仍严格为负。这样没有留下内部参数子区间未判。

最后，

$$
\begin{aligned}
\frac{\mathscr D}{\kappa}
&=2d_0(a+b)-e_0(11a+5b)\\
&=d_0(-9a-3b)+(e_0-d_0)(-11a-5b)>0,
\end{aligned}
\tag{29}
$$

因为

$$
-9a-3b=-3(3a+b)>0,
$$

$$
-11a-5b=-\frac{11}{3}(3a+b)-\frac43b>0.
$$

因此 $\mathscr D\ne0$。在 $N_1(q)=0$ 的范围内，(24) 和完整面积独立性给

$$
\boxed{
c=0,\ N_1(q)=0
\quad\Longrightarrow\quad
\text{完整第四 ruling 必须满足 }M_1(q)=0.
}
\tag{30}
$$

式 (22)、(30) 合起来证明 §1 的定理。一般 $N_1\ne0$ 的圆只能得到 (24) 的完整线性条件，不能擅自把它改成 $M_1=0$。

## 7. R239 的偶微包与最终不可分离双 block 严格违反两门

对 R239 的一个未旋转完整 block，写

$$
q_0=f_0+ig_0=\sum_i(1+i s_i)a_i u_i,\qquad s_i\in\{-1,1\},
$$

其中 $a_i$ 是实幅度，$u_i$ 是互不交的实紧微包，每个 $u_i$ 关于某个 $x_i>0$ 偶，且至少一个非零。这正包括 R239 的偶 $\chi$、有限差分幅度及合法正伸缩、平移。

由于 $(1+i s_i)^4=-4$，三个局部积分逐包给

$$
M_4(q_0)=-4\sum_i a_i^4\int_I(u_i'')^4<0,
\tag{31}
$$

$$
N_1(q_0)=-4\sum_i a_i^4\int_Iu_i'(u_i'')^3=0,
\tag{32}
$$

$$
M_1(q_0)=-4\sum_i a_i^4x_i\int_I(u_i'')^4<0.
\tag{33}
$$

式 (32) 的每项关于微包中心为奇函数；(33) 使用中心偶性及 $x_i>0$。非零紧函数不可能有 $u_i''\equiv0$，所以严格性完整。

这里只对局部四次积分作不交支撑求和。单个微包不一定有三矩零，也没有被当作独立局域的 Volterra block。§4 的算子计算始终先对满足 (2) 的完整 q 进行，所有跨微包 history 原先已包含在完整面积系数 (6) 内。

R239 最后取两个不交的完整 block，作互补旋转
$\alpha$、$\beta=\pi/2-\alpha$，并乘非零实幅度 $A_1,A_2$。其参数范围由 R248 已付

$$
\cos4\alpha>\frac12.
$$

对 $M=M_4$ 或 $M=M_1$，

$$
M(q)=A_1^4e^{-4i\alpha}M(q_{0,1})
+A_2^4e^{4i\alpha}M(q_{0,2}),
$$

故

$$
\operatorname{Re}M_4(q)<0,\qquad
N_1(q)=0,\qquad
\operatorname{Re}M_1(q)<0.
\tag{34}
$$

最终共同正归一化只乘正四次因子，不改变 (34)。

于是当前同一不可分离圆在 $c\ne0$ 时违反 (22)，在 $c=0$ 时违反 (30)。完整 pure 偶函数不属于 $\mathcal W_e\otimes\mathbb C$；按 R248 的 Fourier 规范，至少一个真实第四谐波的偶部不属于允许的 gauge 空间。真实入 history 与二、三阶 gauge 的偶部改变量均由 R224/R231 控制在同一 $\mathcal W_e$ 内，因此它们不能修复此非成员。

## 8. 已排范围与仍未排的范围

本稿关闭的是 R251 对现有 R239 偶微包构造留下的两条例外曲线。所用证据是两个完整解析面积系数，既没有重算六条已付能量，也没有把低阶渐近误差当作非成员。

结论保留以下范围：

- 端芽仍准确为 (1)，$\kappa\ne0$，没有覆盖任意非偶 germ、任意平移参数或 $\kappa=0$；
- 该具体圆的 $N_1=0$ 与 $M_1\ne0$ 已由中心偶性和正放置证明；一般圆不能直接继承；
- (24) 给的是必要关系，不是一般圆的矛盾；普通复矩可能由别的 profile 结构准确相消；
- 不把一段解析端芽的障碍改述为改变 profile 或几何后仍保持原目标度量，也不授任何全局大参数安装；
- 整个第四 ruling 失败当然阻止当前 joint 完成，但本稿不否定主课题的其他圆和其他真实几何路线。

后续若继续使用这类端芽，应改变能使相应完整矩条件成立的 profile 结构，而不能只在 R251 两条参数曲线上移动同一个 (34) 圆。
