# R71：开平曲率段的真实全角非线性 Cauchy 传播

作者：Astra-visible-flex-78718bd0 / geometric_closure，2026-11-10。

v2 订正第 6 节的参数解释：保实际冻结二进参数，不把代码浮点值替换为另一个精确有理度量；v1 原文保留。

**状态：已证明，完整未参与者独审通过。** root 独立重推了特征式、
归一化直纹框架及第一基本形式，但不充当未参与作者的独审。
本文给 $a''=0$ 段的真实二维解及明确的全宽度条件，不是有限阶形式解。
未证明当前数值图的入口数据已满足这些条件，未穿过所有非平 ramp，
未得到新的精确闭面或全时 reach 证书，不改变主任务固定的度量。

## 1. 实际问题与边界数据

固定 $a_0>0$、$c\in\mathbb R$、$S>0$，令
$$
a(s)=a_0+cs>0\quad(0\le s\le S),\qquad
g=ds^2+a(s)^2du^2,\quad u\in\mathbb R/(2\pi\mathbb Z).
\tag{1}
$$
此段的内蕴 Gaussian 曲率精确为 $K=-a''/a=0$。
它包含圆柱型 $c=0$ 与锥型 $c\ne0$，不要求它是平面的一个子集。

给定闭曲线 $\gamma_0(u)$ 和周期正交标架 $(d_0,T_0,N_0)$，满足
$$
\gamma_0'=a_0T_0,\qquad N_0=d_0\times T_0,
$$
$$
\begin{aligned}
d_0'&=cT_0+M_0N_0,\\
T_0'&=-cd_0+(C_0/a_0)N_0,\\
N_0'&=-M_0d_0-(C_0/a_0)T_0.
\end{aligned}
\tag{2}
$$
这里 $C_0$ 是坐标第二基本形式 $II(\partial_u,\partial_u)$ 的入口值，
$M_0$ 是 $II(\partial_s,\partial_u)$ 的入口值；不是正交标架中的
$C_0/a_0^2,M_0/a_0$。
假定
$$
C_0(u)\ne0,\qquad b_0(u)=\frac{a_0M_0(u)}{C_0(u)}\in C^1(S^1).
\tag{3}
$$
最低构造正则性可取 $\gamma_0\in C^2$、标架 $C^1$，并另给 (3)。
由 (2)，$C_0,M_0$ 连续。以下输出为 $C^2$。
光滑或实解析输入当然也允许；这只是本模块的输入范围，
不把 $C^3$ 或更高正则性加入整个课题的完成标准。

若这些数据来自一个已有等距浸入的切口，则 (2) 中的切向项只由
(1) 的 Levi-Civita 连接决定。边界 Gauss 方程在 $K=0$ 处迫使
$L_0=M_0^2/C_0$，所以无需另自由指定一个不相容的 $L_0$。

## 2. 明确公式及全宽度门

令 $\xi$ 为入口圆的参数，定义
$$
\begin{aligned}
&S_0=1+b_0^2,\qquad t_0=\frac{a_0}{\sqrt{S_0}},
\qquad k=\frac{a_0b_0}{\sqrt{S_0}},\\
&e_0=\frac{d_0-b_0T_0}{\sqrt{S_0}},\qquad
w_0=\frac{b_0d_0+T_0}{\sqrt{S_0}},\\
&t(s,\xi)=\sqrt{a(s)^2-k(\xi)^2},\qquad b(s,\xi)=\frac{k(\xi)}{t(s,\xi)}.
\end{aligned}
\tag{4}
$$
平方根总取正实支。第一道实际门是
$$
\inf_{[0,S]\times S^1}(a^2-k^2)>0.
\tag{5}
$$
若 $c\ne0$，定义
$$
\ell=\frac{t-t_0}{c},\qquad
\Psi(s,\xi)=\xi+
\frac{\arctan b(s,\xi)-\arctan b_0(\xi)}{c},
$$
$$
J(s,\xi)=\partial_\xi\Psi
=1+\frac{k'}c\left(\frac1t-\frac1{t_0}\right).
\tag{6}
$$
若 $c=0$，用准确的极限式
$$
t=t_0,\quad b=b_0,\quad
\ell=s\sqrt{S_0},\quad
\Psi(s,\xi)=\xi-\frac{s b_0(\xi)}{a_0},\quad
J=1-\frac{s b_0'}{a_0}.
\tag{7}
$$
第二道实际门是
$$
\inf_{[0,S]\times S^1}J>0.
\tag{8}
$$
于是每个 $\Psi_s$ 都是圆上的 $C^1$ 保向微分同胚：它的 lift 满足
$\Psi(s,\xi+2\pi)=\Psi(s,\xi)+2\pi$，且导数严格正。
写 $\xi=\Xi(s,u)=\Psi_s^{-1}(u)$。
完整位置由
$$
X(s,\xi)=\gamma_0(\xi)+\ell(s,\xi)e_0(\xi),\qquad
F(s,u)=X(s,\Xi(s,u))
\tag{9}
$$
给出。这不是对有限 Fourier 模的投影。

**结论。** 在 (1)–(8) 下，$F$ 是整个 $[0,S]\times S^1$ 上的周期
$C^2$ 浸入，精确满足
$$
F^*e_{\mathbb R^3}=ds^2+a(s)^2du^2,
\quad F(0,u)=\gamma_0(u),\quad F_s(0,u)=d_0(u).
\tag{10}
$$
它的法向正是 $N_0(\Xi(s,u))$。以右边全部函数在
$(s,\Xi(s,u))$ 取值为约定，其第二基本形式为
$$
C=C_0\frac{t}{t_0J},\qquad
M=\frac{k}{a t}C=\frac{C_0k}{a t_0J},\qquad
L=\frac{k^2}{a^2t^2}C.
\tag{11}
$$
因此 $C$ 不过零，$LC-M^2=0$。
两个主曲率为
$$
0,\qquad \kappa=\frac{C_0}{t_0tJ}.
\tag{12}
$$
(5)–(8) 支付域坐标和浸入，不独自支付大宽度上的全局嵌入或 reach。

## 3. 从 Gauss–Codazzi 到真正特征

在本约定下，坐标形式的 Gauss–Codazzi 是
$$
M_s=L_u-\frac ca M,\qquad
C_s=M_u+\frac ca C+acL,\qquad LC-M^2=0.
\tag{13}
$$
在 $C\ne0$ 的解中置 $b=aM/C$，消去 $L=M^2/C$。
直接按商求导得到
$$
b_s-\frac ba b_u=-\frac ca b(1+b^2),
$$
$$
C_s-\frac ba C_u=\frac{b_u+c(1+b^2)}a C.
\tag{14}
$$
对第一式，沿 $u_s=-b/a$ 的特征，
$$
\frac d{ds}\left(\frac{ab}{\sqrt{1+b^2}}\right)=0.
$$
该不变量就是 (4) 中的 $k(\xi)$。
故 $b=k/\sqrt{a^2-k^2}$，积分 $u_s=-b/a$ 正好给 (6) 或 (7)。
其特征 Jacobian 满足
$$
J_s=-\frac{b_u}{a}J.
$$
又
$$
\frac d{ds}\log\frac{a}{\sqrt{1+b^2}}=
\frac ca(1+b^2).
$$
沿特征积分 (14) 的第二式，得
$$
CJ=C_0\frac{a\sqrt{1+b_0^2}}{a_0\sqrt{1+b^2}}
   =C_0\frac t{t_0},
$$
正是 (11)。

这一段还表明：在具有 $C^1$ 第二基本形式、$C\ne0$ 且特征未交叠的
解类中，(11) 是相同入口数据的唯一传播。
并未据此声称所有一般 $C^2$ 浸入具有同样的唯一性定理。
下一节直接构造位置，所以本模块的 $C^2$ 存在性不依赖这个额外唯一性范围。

## 4. 位置、全角周期性与最低正则性的完整核验

由 (2)–(4)，有
$$
\gamma_0'=-ke_0+t_0w_0,\qquad e_0\times w_0=N_0,
$$
$$
e_0'=\left(c-\frac{b_0'}{S_0}\right)w_0,
\qquad
w_0'=-\left(c-\frac{b_0'}{S_0}\right)e_0+\frac{C_0}{t_0}N_0,
\qquad
N_0'=-\frac{C_0}{t_0}w_0.
\tag{15}
$$
例如 $e_0'$ 的法向分量为
$(M_0-b_0C_0/a_0)/\sqrt{S_0}=0$，
切向归一化后系数就是 $c-b_0'/S_0$，没有额外的 $\sqrt{S_0}$。
又 $k'=t_0 b_0'/S_0$。

由 (6)–(7) 可直接验证
$$
\ell_s=\frac at,\qquad
\Psi_s=-\frac{k}{at},\qquad
\ell_\xi=k(1-J),\qquad
t_0+\ell\left(c-\frac{b_0'}{S_0}\right)=tJ.
\tag{16}
$$
这里 $c=0$ 用 (7) 得到同样恒等式。
将 (15)–(16) 代入 (9)，得到
$$
X_s=\frac at e_0,\qquad
X_\xi=-kJ e_0+tJw_0.
\tag{17}
$$
因而 $X_s\times X_\xi=aJ N_0\ne0$。
同时
$$
du=-\frac{k}{at}\,ds+J\,d\xi,
$$
而
$$
|dX|^2=\frac{a^2}{t^2}ds^2
       -\frac{2akJ}{t}ds\,d\xi+a^2J^2d\xi^2
       =ds^2+a^2du^2.
\tag{18}
$$
这证明了整个二维域上的共同度量，不是只核了入口或一条特征。

为了避免最低正则性下不合法地对 $b_0$ 求二次导，进一步写真正物理
坐标中的两个一阶导数：
$$
d:=F_s=\frac ta e_0+\frac ka w_0,
\qquad
T:=\frac1aF_u=-\frac ka e_0+\frac ta w_0.
\tag{19}
$$
右端在 $(s,\Xi(s,u))$ 取值。$\Xi$ 是 $C^1$，(19) 中的所有函数
均为 $C^1$，故 $F_s,F_u$ 均为 $C^1$，实际 $F\in C^2$。
这一步只用了 $b_0\in C^1$，没有假设 $b_0\in C^2$。

由 (15)、$\Xi_u=1/J$、$\Xi_s=k/(atJ)$，对
$N=N_0(\Xi)$ 求导，和
$N_s=-Ld-(M/a)T$、$N_u=-Md-(C/a)T$ 比较，得 (11)。
其秩为 1，迹为 $L+C/a^2=C_0/(t_0tJ)$，得 (12)。
在 $s=0$，$t=t_0,J=1,\ell=0,\Xi=u$，(19) 恢复原 $d_0,T_0$，
从而 (10) 的全部入口数据成立。

所有入口对象均为真正周期函数，$\Psi_s$ 的 lift 次数为 1，
故 (9) 在 $u$ 整圈严格单值。这一步不是只凭局部 Gauss–Codazzi
假定欧氏 monodromy 消失。

## 5. 一个无需解 PDE 的统一实域证书

设已认证
$$
|b_0|\le B_0,\qquad |b_0'|\le B_1.
$$
令
$$
a_{\min}=\min(a_0,a_0+cS),\quad
a_{\max}=\max(a_0,a_0+cS),
$$
$$
h_*^2=a_{\min}^2-
          \max(a_0^2-a_{\min}^2,0)B_0^2.
\tag{20}
$$
若
$$
h_*^2>0,\qquad
\eta_*:=\frac{S a_{\max}B_1}{h_*^2}<1,
\tag{21}
$$
则 (5)–(8) 在全部 $0\le s\le S$ 成立，且
$$
a^2-k^2\ge\frac{h_*^2}{1+B_0^2},\qquad J\ge1-\eta_*.
\tag{22}
$$

**证明。** 写 $H=\sqrt{S_0}\,t$，则
$$
H^2=a^2+(a^2-a_0^2)b_0^2\ge h_*^2.
$$
令 $\rho=\ell/\sqrt{S_0}$。由 (16)，
$\rho_s=a/H$，故 $0\le\rho\le Sa_{\max}/h_*$。
由 (6) 或 (7) 的等价恒等式
$$
J=1-\frac{\rho b_0'}H
\tag{23}
$$
得 $J\ge1-Sa_{\max}B_1/h_*^2$。同时
$t^2=H^2/S_0\ge h_*^2/(1+B_0^2)$。证毕。

因此还可直接认证局部主曲率界
$$
|\kappa|\le
\frac{\|C_0\|_\infty(1+B_0^2)}
     {a_0h_*(1-\eta_*)}.
\tag{24}
$$
(24) 不控制跨不同特征的自接近，故不能单独称为 reach 下界。

## 6. flat17 两个中段的实际宽度与尚待验证的入口门

这里保当前代码冻结的实际二进参数，不把它们另换成精确有理数。
记 $\varepsilon,v_u,v_d,\delta$ 为代码中 `.4`、`.17`、`.18`、
`.07254443456654512` 的冻结实值，取一个 outward cycle。
以下宽裕有理包含足以给全部结论：
$$
\frac{399}{1000}<\varepsilon<\frac{401}{1000},\quad
v_u>\frac{169}{1000},\quad v_d>\frac{179}{1000},\quad
0<\delta<\frac3{40}.
\tag{25}
$$

在 `950f-prefix-flat-accel-screen.py` 的 `ramp` 中，
归一化经线变量 $z\in[\varepsilon,1-\varepsilon]$ 有 $w=1,w'=0$。
这里 $w$ 是该源文件的 ramp 函数，不是 Darboux 高度的径向斜率。
配合 `db6f-prefix-flat-profile.py` 和原
`fixed_metric_mode3_flow.py` 中
$T_u=\delta/[v_u(1-\varepsilon)]$、
$T_d=\delta/[v_d(1-\varepsilon)]$，令
$$
q_\varepsilon=\frac{\varepsilon}{2(1-\varepsilon)},\qquad
 a_- =1+\delta q_\varepsilon,\qquad
 a_+ =1+\delta(1-q_\varepsilon).
\tag{26}
$$
得到两个实际 $K=0$ 区间：

| 段 | 本段入口 $a_0$ | 本段斜率 $c$ | 本段宽度 $S$ | 出口半径 |
| --- | --- | --- | --- | --- |
| 上升中段 | $a_-$ | $v_u$ | $(1-2\varepsilon)\delta/[v_u(1-\varepsilon)]$ | $a_+$ |
| 下降中段 | $a_+$ | $-v_d$ | $(1-2\varepsilon)\delta/[v_d(1-\varepsilon)]$ | $a_-$ |

这些是以冻结二进参数作为实数定义的同一数学 profile。
单次浮点求值的舍入误差仍由数值链自身的包围负责；本文不把它清零。

对任一段，**若实际完整入口数据**满足
$$
C_0\ne0,\qquad |b_0|\le1,\qquad |b_0'|\le1,
\tag{27}
$$
则本模块在上表的整个实际宽度可用，且 $J>4/5$。

证明如下。由 (25)，
$$
\frac{33}{100}<q_\varepsilon<\frac{34}{100},\qquad
1<a_-<a_+<\frac{53}{50}.
$$
两个宽度都满足
$$
S<\frac{202}{601}\frac{3/40}{169/1000}<\frac3{20}.
\tag{28}
$$
上升段 $h_*^2=a_-^2>1$。下降段利用 (20) 得
$$
\begin{aligned}
h_*^2&=2a_-^2-a_+^2\\
&>2(1+\tfrac{33}{100}\delta)^2
  -(1+\tfrac{67}{100}\delta)^2\\
&=1-\frac{\delta}{50}-\frac{2311\delta^2}{10000}\\
&>1-\frac3{2000}-\frac{20799}{16000000}>\frac{99}{100}.
\end{aligned}
\tag{29}
$$
因此两个段统一有
$$
\eta_*<\frac{(3/20)(53/50)}{99/100}
       =\frac{53}{330}<\frac15,
$$
由 (22) 得 $J>4/5$。这是全宽度有理估计，不是“足够窄”的未量化声明。

**(27) 尚未对当前全 PDE 入口得到验证。** 现存有限模输出不能自动
提供它对应的精确曲线和精确二阶数据。即使对数值曲线作连续包围，
还需和真正解的修正界连接。故本节不声称已经为当前候选跨过任一段。
它只给一个明确、相当宽裕、可由后续真实入口证书检验的完整模块门。

## 7. 正则性、接合、连续族和保留的缺口

若入口数据实解析，则 (4)–(9) 在 (5)–(8) 的严格范围内实解析，
由解析逆函数定理得到真正的解析二维解。
固定闭实域上的严格余量保证可在某个共同复杂角带延拓；
若要有效的角带宽、log 权值或 ordinary-source Green 界，
仍须另提供入口的复域范数和相应算子表，本文不从实域余量虚构这些数值。

若一族入口数据在 $\gamma_0$ 的 $C^2$、框架的 $C^1$、$b_0$ 的 $C^1$
拓扑连续，并共同满足严格门及 $a_0,c,S$ 固定，则 (9)、(19)
和其一次导数在紧域上一致连续依赖这些数据。
故所得族在 $C^2$ 拓扑连续，且每个参数使用同一 (1)。

若邻接已存在片的完整两 jet 满足 (2) 及 $K=0,C_0\ne0$，
Gauss 方程给相同 $L_0=M_0^2/C_0$。
两个浸入有相同位置、一阶框架、第二基本形式和度量连接，
所以全二阶坐标导数相同，形成真实 $C^2$ 接合。
这不预先断言邻接非平 ramp 已存在。

若 $\gamma_0$ 本身嵌入，初边界的 $d_0$ 与 $\gamma_0'$ 正交且单位，
则局部逆函数定理加紧性和远离对角的曲线分离，给某个正薄宽度的
全局嵌入。要取得第 6 节的**完整物理宽度**，必须另核不同特征之间
的全局分离；(5)、(8)、(24) 不代替它，也不代替闭面其它片之间的距离。

本构造没有涵盖非零曲率 ramp、有限阶转型根的完整高频图、
普通非齐次源的真逆、无限尾匹配或闭合。
它的作用是把实际 flat17 的开放 parabolic 段从未构造的头部 provider 中
明确分离出来，并为这些段提供真正全角、全宽度可检验的非线性传播公式。


## 8. 正式采纳与完整独立审查

本结果逐字保留冻结 v2 的全部数学主体，仅更换标题和审查状态并加本节。
[v2 原稿](../notes/2026-11-10-78718-geometry-flat-strip-provider-v2.md)
12,558 B，SHA256 cc26cf6685ec4a26f4c8b612c64d1af598cc4f8e223d6cd2c1b0a87e99af23d4。
[完整独审](../notes/2026-11-10-78718-audit-flat-strip-provider-v2.md)
14,168 B，SHA256 e91ae79faf2f2d9a04c74dd9049753cc40a083de31b4ea8d66cb0b389394aa14。
审者 independent_audit 未参与构造；其逐式推导并直接核原解析 Target 的
exact-binary Fraction 参数和 Tu/Td，确认不是另一张度量。root 全文读稿46e8bf、
全文读独审8cc9e9后正式采纳。

冻结 [有限参数检查源](../scripts/78718-geometry-flat-strip-binary-gates.py)
SHA256 904a48bab818343dd288ace9607542659a2788d999f24923bbd38397031ed50e；
作者实际360ae9、独立者实际b7808a均自然exit0。
[独立报告](../notes/2026-11-10-78718-audit-flat-strip-binary-gates-01.json)
771 B，SHA256 67776fc8235e18e011aad462624f80fcb0a94336636a0cd65a6926bc2af9cf33，
仅10项二进/有理门、0 PDE。真正二维存在性由全文位置公式证明，不靠有限检查替代。

本结果仍是条件条带模块：真实当前入口条件、完整宽度的全局嵌入与 reach、
非平 ramp、闭面及主 README 的全部完成条件没有因此得到支付。
