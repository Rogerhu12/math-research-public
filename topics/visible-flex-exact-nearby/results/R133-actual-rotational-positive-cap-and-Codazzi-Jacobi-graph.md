# R133：同一固定目标的真实旋转正帽与完整 Codazzi Jacobi 边界图

2026-11-13，visible-exact-astra-ac0d / newton_source。

**数学合同。** 本篇给同一 $g_0$ 的精确旋转参考、其完整 Fourier Codazzi
Jacobi 方程、R74 真 regular 线到该曲率 frame 的准确转换，以及有向标量
Riccati 比较算法。它的径向入口为 $r_*=239/1000$，外端为原
$R=25/8$；中间使用实际 body 和 R66 的实际 natural graft。

**native 状态：已通过。** v2 以 256-bit Arb 给出整个
$[239/1000,25/8]$ 的 1,334 个闭盒，覆盖完整
$|\eta|\le10^{-9}$、实际角均值与全部 primitive 尾；16 个列出模式
以及所有 $m\in4\mathbb N$ 的独立正性门均通过。第 7 节保留首版
真实失败及修复，给出可重跑输入和外舍入数值。

这是一条真实旋转参考的**线性曲率边界图**。
它不是原非圆腰分支的 nonlinear cap DN，不给缺陷源的完整 contact，
也不把曲率变量的 mean 与 regular 平移高度端口混为一谈。

## 1. 旋转参考与正域图

目标不变：
$$
g_0=E(r)\,dr^2+a(r)^2d\theta^2,
\qquad E=\langle |F_{{\rm original},r}|^2\rangle_\theta.
\tag{133.1}
$$
若 $a,E>0$ 且 $E-a'^2>0$，定义
$$
z_{\rm rot}'=\sqrt{E-a'^2},\qquad
F_{\rm rot}=(a\cos\theta,a\sin\theta,z_{\rm rot}).
\tag{133.2}
$$
积分常数是保留的刚体平移高度。直接微分给
$dF_{\rm rot}^2=g_0$，而非仅一阶或近似相等。
用 R126 同一物理方向
$X=F_r/\sqrt E$、$Y=F_\theta/a$、$n=Y\times X$，其正交曲率为
$$
B_0=0,\qquad
C_0=-\frac{\sqrt{E-a'^2}}{a\sqrt E}<0,\qquad
A_0=\frac K{C_0},
\tag{133.3}
$$
$$
K=-\frac{a''}{aE}+\frac{a'E'}{2aE^2}.
$$
在 $K>0$ 区间，$A_0,C_0$ 都为负。即使中间经过最大圆 $a'=0$，
$C_0$ 仍非零；本曲率图不经过高度图 $n_z=-a'/\sqrt E$ 的分母。

选择 (133.2) 的高度常数使它在 $r=R$ 与 R74 原径向对象高度相同。
graft 终端的非径向相位及其四 jet 为零，故 $a,E$ 的连续低 jet 与
该原尾一致。旋转参考可以接上 R74 选择的同一径向两 bump、connector
和真实 regular 尾；高度常数不会改变其曲率 Jacobi 线。

## 2. 完整 primitive 的稳定系数，而非两个大数相减

在旋转柱坐标基中写原始明确对象
$$
F=a(e_r+P)+Ze_z,
$$
其中 $P$ 是准确单位切向量减圆背景后的完整角原函数，
$\langle P_z\rangle=0$。置
$$
L=\frac{a'}a,\qquad H=\frac{Z'}{a^2},\qquad
u=LP+P_r,\qquad u_r=L'P+LP_r+P_{rr},
$$
$$
e=2L\langle u_x\rangle+\langle u\cdot u\rangle,
\qquad
e_r=2L'\langle u_x\rangle+2L\langle (u_r)_x\rangle
       +2\langle u\cdot u_r\rangle.
\tag{133.4}
$$
精确零 mean 的竖直原函数消掉与 $Z'$ 的交叉项，因此
$$
\overline E:=\frac E{a^2}=L^2+a^2H^2+e,\qquad
\mathscr R:=\frac{E-a'^2}{a^4}=H^2+\frac e{a^2}.
\tag{133.5}
$$
稳定目标曲率恒等式为
$$
K=\frac{H^2(L^2-L')+LHH'
 +(Le_r-2L'e)/(2a^2)}{\overline E^2}.
\tag{133.6}
$$
这是 R69/R111 同一半径消去恒等式。
特别地，深帽只需计算 $\mathscr R$，不从两个约为 $a^2$ 的区间直接
相减来求一个约为 $a^4$ 的量。
所需 Jacobi 系数随后准确为
$$
\gamma=\frac{\sqrt E}a=\sqrt{\overline E},\qquad
\beta=L,\qquad
C_0=-\sqrt{\mathscr R/\overline E},\qquad
\ell:=\frac{A_0}{C_0}=\frac K{C_0^2}
=\frac{K\overline E}{\mathscr R}.
\tag{133.7}
$$

### 2.1 Body 的无限尾费用

body provider 使用同一准确仿射参数 germ 和原 `MetricDefectTarget`。
对每一个真实公共 spline germ，单位原函数的完整尾及 alias 给
每个分量的 $A^0$ 误差 $\epsilon_j$，$j=0,1,2$。
记有限部分的每分量 $A^0$ norm 上界为 $M_u,M_{u_r}$，则
$$
e_u=|L|\epsilon_0+\epsilon_1,\qquad
e_{u_r}=|L'|\epsilon_0+|L|\epsilon_1+\epsilon_2.
$$
三个 Euclidean 分量的完整均值卷积误差满足
$$
\begin{aligned}
\operatorname{err}(e)
&\le2|L|e_u+3(2M_ue_u+e_u^2),\\
\operatorname{err}(e_r)
&\le2|L'|e_u+2|L|e_{u_r}
 +6(M_ue_{u_r}+M_{u_r}e_u+e_ue_{u_r}).
\end{aligned}
\tag{133.8}
$$
脚本逐项支付这些误差后，才使用 (133.5)–(133.7)。
数值有限 Fourier mean 从未被当作真实目标的定义。
误差和 scalar germs 均保留完整 $|\eta|\le10^{-9}$；角平均的计算也
没有将参数改为中点。

### 2.2 真正的 natural graft

$[3,25/8]$ 使用 R66 的准确 $\log a$、$H$ 和物理权
$\beta_j=a^3\chi b_j$、$\gamma_j=a^2\chi g_j$，不是 body spline 外插。
原 `NaturalGraft.majorants` 的完整 Wiener 界给
$|e|\le e_*$、$|e_r|\le e_{r,*}$。将它们作为独立有效余项代入同一
(133.5)–(133.7) 即可。这里不需要有限角网格，也不省略 mean。

全部闭盒必须有 $a,\overline E,\mathscr R,K,\gamma,\ell>0$，
以及 $C_0<0$。对正商 $\ell=K\overline E/\mathscr R$，v2 使用
正端点乘除：下界为 $K_-\overline E_-/\mathscr R_+$，上界为
$K_+\overline E_+/\mathscr R_-$，每一步均有向外舍入。
必须先核严格正性，再比较上界/下界的宽度比；一个穿零区间的
负比值不能通过宽度门。
任何未解决的正性或宽度门都细分原盒；达到深度限制仍失败时保存失败，
不得以邻点符号补齐。最终以准确 Fraction 检查完整无缝径向覆盖。

## 3. 准确 Codazzi Jacobi 系统与 Fourier frame

R126 的完整方程为
$$
B_r=\gamma A_\theta-2\beta B,\qquad
C_r=\gamma B_\theta+\beta(A-C),\qquad
A=\frac{K+B^2}{C}.
$$
围绕 (133.3) 作真实线性化，$\delta A=-\ell\,\delta C$。
取物理频率 $m\in4\mathbb N$、
$\delta B=b_m(r)\sin(m\theta)$、
$\delta C=c_m(r)\cos(m\theta)$，得到
$$
\boxed{
\frac d{dr}\binom{b_m}{c_m}
=\begin{pmatrix}
-2\beta&\gamma m\ell\\
\gamma m&-\beta(\ell+1)
\end{pmatrix}\binom{b_m}{c_m}.
}
\tag{133.9}
$$
此处 $m$ 是物理频率 $4j$，不能把归一化序号 $j$ 直接代入。
另一实反射扇区及负频率由同一复 Fourier 系统和实共轭得到。

设 $z_m=b_m/c_m$，则
$$
(z_m)_r=\gamma m(\ell-z_m^2)+\beta(\ell-1)z_m.
\tag{133.10}
$$
往内回传时用 $t=R-r$、$q_m=-z_m$，方程为
$$
\boxed{
(q_m)_t=m\gamma\ell-\beta(\ell-1)q_m-m\gamma q_m^2.
}
\tag{133.11}
$$
正型区域 $\gamma,\ell>0$ 使 $q=0$ 的向内导数严格为正，
并在大正 $q$ 处给负二次增长。这是可以直接认证的标量比较方程，
不需要对整条指数增长传递矩阵取浮点逆。

## 4. R74 真 regular 线到当前 frame：准确消去

在实际长径向入口处，记半径坐标系数为
$E_a=1+w^2$，$w=a_*/(4\omega)$。
R74 对同一真实两 bump、connector 和无限尾给出
$\lambda_m=y_u(0)/y(0)$，且
$$
|\lambda_m+m\omega|
\le4m\omega\epsilon_*^{-1}e^{-2m\omega B},\qquad
\epsilon_*=2^{-39},\quad B=2^{24}-25/8,
\quad\lambda_4=-4\omega.
\tag{133.12}
$$
这些是完整实际尾的结论；$m=4$ 的等式来自匹配，不是近似。

R74 的实际高度变分为
$\delta Z=4(\omega y-y_u/m^2)$。
令 $h=-\delta Z/(aw)$，并用 R119 的反向高度坐标 $t_u=-\omega$。
这里是在指定的准确长径向入口求值；该入口满足
$y_{uu}=m^2\omega^2y$，且 $\omega$ 为径向常数。
因 $(aw)_u=-2\omega aw$，得到
$$
\frac{2h+h_t}{h}
=-\frac{(\delta Z)_u}{\omega\delta Z}
=\frac{\omega-\lambda_m}{\omega-\lambda_m/m^2}
=:c_m^{\rm ht}.
\tag{133.13}
$$
$\lambda_m<0$ 使此高度分母严格大于 $\omega$。
再用 R119 曲率接口的准确一阶式，
$$
z_m(R)=-\frac{m(c_m^{\rm ht}-1)}
                  {\sqrt{E_a}(m^2-c_m^{\rm ht})}
=\boxed{\frac{\lambda_m}{m\omega\sqrt{E_a}}}.
\tag{133.14}
$$
最后一步是准确代数消去，不需要小半径极限。
因此
$$
q_4(R)=\frac1{\sqrt{E_a}},\qquad
\left|q_m(R)-\frac1{\sqrt{E_a}}\right|
\le4\epsilon_*^{-1}e^{-2m\omega B}/\sqrt{E_a}.
\tag{133.15}
$$
脚本对非第四模宽松保留
$2^{42}e^{-2m\underline\omega B}$ 的真实非零有向 fee，
并另核它小于 $2^{-100}$。浮点显示为0不会改变保存的 Arb 指数界。
这里没有把 R119 的两端 $f_B=0$ 边界替换成已经匹配的真实 regular 条件。

## 5. 每盒准确 Riccati 上下流与全频门

在一闭盒内，给出
$\gamma\in[\gamma_-,\gamma_+]$、
$\ell\in[\ell_-,\ell_+]$，以及
$-\beta(\ell-1)\in[b_-,b_+]$。
对任意 $q\ge0$，(133.11) 的右侧夹在
$$
m\gamma_-\ell_-+b_-q-m\gamma_+q^2
\quad\hbox{与}\quad
m\gamma_+\ell_++b_+q-m\gamma_-q^2
\tag{133.16}
$$
之间。将相应常系数方程从已付的下/上初值解到盒末，标量比较定理
就给完整真实径向盒的末端界。不同系数的相关性只被用于安全放宽，
没有从它们假设不存在的独立参数对象。

常系数方程 $q'=A+Bq-Cq^2$、$A,C,q(0)>0$ 的准确流可写为
$$
\Delta=\sqrt{B^2+4AC},\quad
\alpha=\frac{2A}{\Delta-B}>0,\quad
\nu=-\frac{\Delta-B}{2C}<0,
$$
$$
\rho=\frac{q(0)-\alpha}{q(0)-\nu}e^{-\Delta h},\qquad
q(h)=\frac{\alpha-\rho\nu}{1-\rho}.
\tag{133.17}
$$
若 $q(0)\ge\alpha$，则 $0\le\rho<1$；否则 $\rho<0$。
所以分母始终正，正解没有有限时爆破。
脚本以 Arb 向外计算本式，并独立检查分母及输出正性，再取
lower/upper 作为下一盒的确定有向初值。
逐盒轨迹用 decimal ball 保存，重读时须再取外端点。

该有限模式回传之外，还有**所有** $m\in4\mathbb N$ 的共同门。
令完整正帽上的全局界为
$$
g_\pm=\inf/\sup\gamma,\quad
l_\pm=\inf/\sup\ell,\qquad
b_*\ge\frac14\sup|\beta(\ell-1)|.
$$
设 $q_-$、$q_+$ 分别是下列方程的正根：
$$
g_-l_--b_*q_--g_+q_-^2=0,
\qquad
g_+l_++b_*q_+-g_-q_+^2=0.
\tag{133.18}
$$
因 $m\ge4$，(133.11) 除以 $m$ 后，在 $q_-$ 处导数非负、
在 $q_+$ 处非正。将该区间扩大到包含 (133.15) 的全部初值，
即得所有真实频率的共同严格正有限区间 $[q_{\min},q_{\max}]$。

同时由 (133.9)
$$
(c_m)_r=[-\gamma m q_m-\beta(\ell+1)]c_m.
\tag{133.19}
$$
从任意非零归一化 $c_m(R)$ 出发，该解在紧区间上不为零。
所以所认证的曲率边界图没有隐藏的 Dirichlet 零分母。
在复 Fourier 写法中它是
$\widehat{\delta B}(m)=i\operatorname{sgn}(m)q_{|m|}\widehat{\delta C}(m)$。
对同一任意 Fourier 权，该图和逆图的 norm 分别不超过
$q_{\max}$ 与 $1/q_{\min}$。没有只从列出的16模外推无限高模。

这里每一条 regular 线的初始数据来自 R74 的真实周期 infinitesimal
isometry，包括它在 $r=R$ 的位置和框架变分。将 R126 的径向框架和
位置 ODE 在旋转参考处线性化，并以这些实际数据往内积分，线性化的
角约束误差仍满足齐次径向 ODE，故保持为零。系数和初值的周期性也由
ODE 唯一性保持。因此 (133.9) 所回传的是该真实周期位移的曲率数据，
并非忽略 holonomy 后任取的一条形式 Codazzi 解。刚体位置/框架常数
与非零曲率图分开保留；它们不会改变 (133.14) 的比值。

## 6. mean、位置端口与非线性限制

纯曲率 mean 的形式 Jacobi 方程仍保留：
$$
(b_0)_r=-2\beta b_0,\qquad
(c_0)_r=-\beta(\ell+1)c_0.
\tag{133.20}
$$
它不能取代真实周期框架/位置条件。
对于旋转参考的周期轴对称 infinitesimal isometry，写位移为
$V=Ue_r+Te_\theta+We_z$。固定 $g_{\theta\theta}=a^2$ 的 mean 行给
$U=0$；因 $z'_{\rm rot}>0$，固定径向度量给 $W'=0$；
交叉度量给 $(T/a)'=0$。因此这个完整齐次 mean 扇区是竖直平移和
绕轴刚体转动，其曲率变化为0。
regular mean 高度 $W$ 是独立保留的刚体端口，没有被曲率图吸收。

上述齐次结论不意味着带真实 metric source 时可以删掉 R74/R111 的
mean trace 或 mean flux 行。forced mean contact、两端源 jet 及非线性
mean 小根在本篇没有被求逆或消去。

对于实际非圆腰 Cauchy 分支，本篇的参考图只能作为比较或预条件。
准确非线性差是
$$
A-A_0+\ell(C-C_0)
=\frac{B^2}{C}+\frac{K(C-C_0)^2}{CC_0^2}.
\tag{133.21}
$$
已有有限 Cauchy 候选在 $r=.239$ 上相对旋转参考的
$\sup|C-C_0|/|C_0|$ 约为2.18，(133.21) 的 sampled sup 约为0.819。
这些仅是浮点诊断，足以说明不能把该候选直接当作本参考的小线性扰动。
真正的 nonlinear cap map 及它与原腰分支的闭合仍须完成。

## 7. Native 结果及冻结清单

### 7.1 首版真实失败与非破坏性修复

首版约运行 3,896.79 秒，完成 1,332 个标量闭盒，随后在 Riccati
比较入口处正确拒绝，报告保留
`cap_linear_reference_certified=false` 和
`Jacobi_failure="invalid Riccati comparison initial data"`。
具体地，在实际 graft 盒 $[3,49/16]$，三个原始正量
$K,\overline E,\mathscr R$ 均严格为正，但普通 ball 乘除的派生
$\ell$ 包络下端达到 $-.109308190643787384$。旧宽度门没有先核
$\ell>0$，把负的上/下比误当作小比值；下游正 Riccati 门拒绝了它。
首版从未产生成功的曲率边界图证书。

v2 保留首版源和完整失败报告。它先核原始源、全部依赖、准确仿射
对象和 R74/R126 定理 SHA，再对缓存的所有系数盒重做严格正性与
正端点商。1,331 盒直接通过；上述坏盒的真实 scalar germ 被重新
计算，最终用以下三盒替换：
$$
[3,97/32],\qquad[97/32,195/64],\qquad[195/64,49/16].
$$
这不是删去坏盒或补一个邻点符号。最终以准确 Fraction 核无缝闭覆盖，
总计 1,334 盒。v2 实际运行 27.56 秒，完整系数门和全部 Riccati 门
同时通过；其新报告还保留原失败身份和每次真实细分原因。

### 7.2 完整区间上的有向结论

下面十进制数均向安全方向放宽，作为明确有理数使用。整个正帽满足
$$
\begin{gathered}
6.56331699\times10^{-6}<a<1.11994991,\\
1.11248831<\gamma<5.63913356,\qquad
.92479550<\mathscr R<1.00721464,\\
.02679531<K<3.45006391,\qquad
.03787180<\ell<4.91515570,\\
.17053380<|C_0|<.89601480.
\end{gathered}                                                  \tag{133.22}
$$
真实外端 $a_*\in(6.5637657879557,6.5637657879724)\times10^{-6}$，
$\omega\in(1.4611528630835,1.4611528630923)$。
全频 regular fee 在 Arb 中实际保留为正，约为
$7.5277\times10^{-85170600}$；不能因为普通 double 输出为0就把它
从证明中删除。

对所有 $m\in4\mathbb N$，整个区间均有
$$
\boxed{\quad .03599163<q_m(r)<5.44526455.\quad}                \tag{133.23}
$$
这个门由 (133.18) 的真正全频不变区间取得，不是由下表外推。
在内端 $r=.239$，额外的逐模有向回传给：

| 物理频率 $m$ | $q_m(.239)$ 的严格下界 | 严格上界 |
|---:|---:|---:|
| 4 | 1.04056072 | 1.07181583 |
| 8 | .86117965 | .89165243 |
| 12 | .76911554 | .80159852 |
| 16 | .70602175 | .74039946 |
| 20 | .65964608 | .69563699 |
| 24 | .62405933 | .66139105 |
| 28 | .59576872 | .63421445 |
| 32 | .57262209 | .61199960 |
| 36 | .55324267 | .59340513 |
| 40 | .53671402 | .57754161 |
| 44 | .52240265 | .56379631 |
| 48 | .50985583 | .55173272 |
| 52 | .49874053 | .54103073 |
| 56 | .48880570 | .53144974 |
| 60 | .47985797 | .52280500 |
| 64 | .47174574 | .51495201 |

### 7.3 复跑与身份

两个运行入口如下。脚本拒绝覆盖已有结果，复核时可把 `--out` 指向
一个新的路径；v2 的 `--checkpoint` 默认读取所保存的完整首版报告。

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_rotational_cap_jacobi.py \
  --out notes/2026-11-13-Codazzi-rotational-positive-cap-native.json.gz

PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_rotational_cap_jacobi_v2.py \
  --out notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz
```

主要输入身份如下；完整递归 Python 依赖及定理输入另存于 manifest
和 native 报告。

| 对象 | SHA256 |
|---|---|
| 准确仿射对象 | `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848` |
| 原点数据 | `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b` |
| 仿射方向 | `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab` |
| 首版 producer | `05dda3acc9cd359c8cd15b61e1d573d310289af984d6923261e61161afc50046` |
| v2 producer | `2c0115b9d42e33b8f9db1220b220e0c37ab1c20446109511d1df7930db46b609` |
| 首版完整失败报告 | `582cc5bb7a74d42a9a9548b42370cef9c3e91efac1a5c05104c7e0724565a2bf` |
| v2 完整成功报告 | `3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22` |

本结论给出了同一 $g_0$ 的真实旋转正帽和完整线性 regular 曲率图。
它仍未将有限非圆 Cauchy 候选与该正帽作 nonlinear 匹配，也没有
据此声称完成整个闭曲面的精确可见 flex。
