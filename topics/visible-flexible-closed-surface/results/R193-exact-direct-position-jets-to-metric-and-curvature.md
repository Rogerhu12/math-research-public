# R193：准确直接位置两 jet 到归一度量、Gram 与真实曲率的误差转移

**状态：已证明。** 本文给 [R187](R187-closed-unit-angular-tangents-and-direct-position-metric.md)–[R190](R190-positive-radius-design-and-exact-fixing-of-the-metric.md) 直接位置表示的完整条件后验。它消费已证明的同一物理盒上的 jet/误差包；没有证明当前主状态满足这些小误差条件，也不将采样矩阵当连续证书。

## 1. 准确对象和四类输入身份

固定全部设计参数。准确物理坐标为 $s,u$，准确正半径为 $a(s)>0$。令

$$
T=(-\sin\Theta\cos\Phi,\ \cos\Theta\cos\Phi,\ \sin\Phi),\qquad |T|=1,
$$

$Y$ 为 R187/R188 定义的完整零均值周期原函数，$Y_u=T$，并设

$$
X=aY+Ze_z,\qquad g=ds^2+a^2du^2.
$$

准确 $a$ 是准确 B32 基础半径加 R190 全部实际样条；$Z$ 包含准确基础高度及完整高度参数。参数固定后才是同一目标度量。

本证明在一个共同连续物理盒成立，也可限制到一个物理点。数据须绑定以下对象：

1. **准确 B32 基础曲线。** 包括真实 phase 积分、准确中央周长、$c=13/128$ 和准确 cut 长度 $S$。不能把有限 dense interpolation 的导数默认等同于准确 phase 公式的导数。
2. **准确中央曲线与完整角函数。** 包括中央椭圆及其材料角反解、$\Theta,\Phi$ 的完整函数、真实导数、参数和准确径向/角网格。有限 ellipse 求积或 inverse-angle 的误差在这一入口支付。
3. **准确样条网格与实际系数。** 所有 $\rho$ 作为保存 binary64 的准确 dyadic；$h=(S-c)/(J+3)$ 由准确 $S$ 定义。R190 interval 层给准确样条及保存浮点网格的连续敏感界，不把浮点中心另固化成几何定义。
4. **参考求值与误差证据。** 有限程序给出的近似、其真实输入身份，以及上述准确对象相对于这些参考函数的统一误差。R188 primitive 的均值、first moment、完整非线性尾和参数列不能省掉。

这些误差入口可能相关。使用方应按实际分解合并，避免重复计算同一误差，也不能因来源不同遗漏一项。一个有限节点/有限角读数不能自动填成连续盒上界。

## 2. 参考函数与准确误差假设

下标 $0$ 表示同一物理坐标下明确的参考函数或参考 jet。定义

$$
V_0=a_{0,s}Y_0+a_0Y_{0,s}+Z_{0,s}e_z,
$$

$$
A_0=a_{0,ss}Y_0+2a_{0,s}Y_{0,s}
+a_0Y_{0,ss}+Z_{0,ss}e_z.
$$

这里只要求这些量及误差在查询盒上被包围。参考 primitive 与参考 $T_0$ 可以分别是准确函数的不同近似；不假定有限求积 primitive 的导数恰好等于 $T_0$。

设准确误差满足

$$
|a-a_0|\le e_a,\quad |a_s-a_{0,s}|\le e_{a_s},\quad
|a_{ss}-a_{0,ss}|\le e_{a_{ss}},
$$

$$
|Z_s-Z_{0,s}|\le e_{Z_s},\quad
|Z_{ss}-Z_{0,ss}|\le e_{Z_{ss}},
$$

以及向量欧氏范数误差

$$
|Y-Y_0|\le e_Y,\quad |Y_s-Y_{0,s}|\le e_{Y_s},\quad
|Y_{ss}-Y_{0,ss}|\le e_{Y_{ss}},
$$

$$
|T-T_0|\le e_T,\quad |T_s-T_{0,s}|\le e_{T_s},\quad
|T_u-T_{0,u}|\le e_{T_u}.
$$

记 $a_*,a_{0,*}>0$ 为准确和参考半径的下界；$A_a,A_{a_s},A_{a_{ss}}$ 分别包围 $|a_0|,|a_{0,s}|,|a_{0,ss}|$。记 $N_Y,N_{Y_s},N_{Y_{ss}},N_A,N_{T_s},N_{T_u}$ 为对应参考向量的范数上界，其中 **$N_A$ 优先直接包围真实参考组合 $A_0$**，无需再将这个已经相消的组合分拆成大三角界。

参考归一 Gram 矩阵定义为

$$
H_0=\begin{pmatrix}|V_0|^2&V_0\cdot T_0\\
V_0\cdot T_0&|T_0|^2\end{pmatrix}
=\begin{pmatrix}1+r_{E,0}&r_{F,0}\\r_{F,0}&1+r_{G,0}\end{pmatrix}.
$$

输入区间 $I_{E,0},I_{F,0},I_{G,0}$ 必须包含这些**真实二次表达式**。若入口是浮点 residual 数值，其点积舍入必须已经进入区间；不能仅将显示小数作为准确二次式。

## 3. 真实位置一、二 jet 的完整误差

准确位置满足

$$
V=X_s=a_sY+aY_s+Z_se_z,
$$

$$
A=X_{ss}=a_{ss}Y+2a_sY_s+aY_{ss}+Z_{ss}e_z,
$$

$$
X_u=aT,\quad X_{su}=a_sT+aT_s,\quad X_{uu}=aT_u.
$$

准确加减参考量可得

$$
e_V=e_{a_s}N_Y+(A_{a_s}+e_{a_s})e_Y
+e_aN_{Y_s}+(A_a+e_a)e_{Y_s}+e_{Z_s},
\tag{1}
$$

$$
\begin{aligned}
e_A={}&e_{a_{ss}}N_Y+(A_{a_{ss}}+e_{a_{ss}})e_Y\\
&+2e_{a_s}N_{Y_s}+2(A_{a_s}+e_{a_s})e_{Y_s}\\
&+e_aN_{Y_{ss}}+(A_a+e_a)e_{Y_{ss}}+e_{Z_{ss}}.
\end{aligned}
\tag{2}
$$

于是 $|V-V_0|\le e_V$、$|A-A_0|\le e_A$。例如第一乘积准确写成
$(a_s-a_{0,s})Y_0+a_s(Y-Y_0)$，因此其界为式(1)对应两项；其余逐项相同。没有丢掉系数与函数误差的乘积。

这里的二阶导数都固定物理 $s,u$。准确 grid 与浮点 grid 的坐标误差若改变函数输入，其影响必须已进入这些 jet 误差，不能把一个不同 $s$ 点的参考数直接比较。

## 4. 保持准确角向相消的度量与 Gram 界

准确目标正交标架为 $(\partial_s,a^{-1}\partial_u)$。由于完整 $|T|=1$，

$$
H=\begin{pmatrix}|V|^2&V\cdot T\\V\cdot T&1\end{pmatrix},
\quad
r_E=|V|^2-1,\quad r_F=V\cdot T,\quad r_G=0.
\tag{3}
$$

令 $N_V=\sqrt{1+\sup I_{E,0}}$ 的严格上界。无需由各乘积单独估计 $V_0$；其已知真实 residual 直接给出这个界。

准确展开

$$
|V|^2-|V_0|^2=2V_0\cdot(V-V_0)+|V-V_0|^2
$$

及

$$
V\cdot T-V_0\cdot T_0=(V-V_0)\cdot T+V_0\cdot(T-T_0)
$$

得到

$$
d_E=2N_Ve_V+e_V^2,\qquad
d_F=e_V+N_Ve_T.
\tag{4}
$$

第二式使用准确 $|T|=1$，所以不必另加 $e_Ve_T$。因此

$$
I_E=I_{E,0}+[-d_E,d_E],\qquad
I_F=I_{F,0}+[-d_F,d_F]
\tag{5}
$$

包含准确 residual。记 $E_*=\max|I_E|$、$F_*=\max|I_F|$，则准确相对度量算子范数满足

$$
\|g^{-1/2}(X^*e-g)g^{-1/2}\|
\le U:=\frac{E_*}{2}
+\sqrt{\frac{E_*^2}{4}+F_*^2}.
\tag{6}
$$

这是矩阵 $H-I$ 的完整两个特征值公式，不把 $r_E,r_F$ 的符号抵消替换成不相关的几何界。

令 $E_-=\inf I_E$。有

$$
D_*:=1+E_--F_*^2\le\det H,
\tag{7}
$$

$$
\lambda_*:=
1+\frac{E_-}{2}-\sqrt{\frac{E_-^2}{4}+F_*^2}
\le\lambda_{\min}(H).
\tag{8}
$$

式(8)中最小特征值关于 $E$ 单调不减、关于 $|F|$ 单调不增，直接对公式微分或对称矩阵半正定顺序即可证明。因此这些下界在整个查询盒成立。若下界不足以证明正性，消费者如实返回未决，不作不存在结论。

## 5. 真实法向误差：使用 Gram 行列式

设

$$
C=V\times T,\qquad C_0=V_0\times T_0.
$$

由式(4)的同样展开，

$$
|C-C_0|\le e_C:=e_V+N_Ve_T=d_F.
\tag{9}
$$

准确 $\det H=|C|^2$；参考 $\det H_0=|C_0|^2$。从 $I_{E,0},I_{F,0},I_{G,0}$ 得严格参考下界

$$
D_{0,*}=(1+\inf I_{E,0})(1+\inf I_{G,0})
-\bigl(\max|I_{F,0}|\bigr)^2
\tag{10}
$$

时，还必须确认两个对角下界均正。若 $D_*,D_{0,*}>0$，令
$c_*=\sqrt{D_*}$、$c_{0,*}=\sqrt{D_{0,*}}$ 的严格下界。

对任何非零向量 $x,y$，

$$
\left|\frac{x}{|x|}-\frac{y}{|y|}\right|
\le\frac{2|x-y|}{|x|+|y|}.
\tag{11}
$$

证明：写 $a=|x|,b=|y|$ 和两单位向量之差 $d$，则
$|x-y|^2=(a-b)^2+ab\,d^2$，且 $d\le2$。式(11)平方等价于
$(a-b)^2d^2\le4(a-b)^2$，所以成立。

准确定向法向为 $N=C/|C|$。允许参考法向 $N_0$ 是有限 normalization 的近似，若已有严格 $e_{N,0}$ 证明

$$
\left|N_0-\frac{C_0}{|C_0|}\right|\le e_{N,0},
$$

则

$$
|N-N_0|\le e_N:=
\min\left(2,\frac{2e_C}{c_*+c_{0,*}}\right)+e_{N,0}.
\tag{12}
$$

这明确保留有限法向求值的误差；未把其 binary64 单位长度默认成准确 1。法向符号固定为同一 cross-product 约定，不能在比较中私自翻转。

## 6. 第二基本形式：先作准确混合项相消

在准确目标正交标架中的实际第二基本形式为

$$
Q=
\begin{pmatrix}
N\cdot A&
N\cdot(a_sT/a+T_s)\\
N\cdot(a_sT/a+T_s)&
N\cdot(T_u/a)
\end{pmatrix}.
$$

因为 $N\perp T$，完整恒等式化为

$$
Q=
\begin{pmatrix}
N\cdot A&N\cdot T_s\\
N\cdot T_s&N\cdot(T_u/a)
\end{pmatrix}.
\tag{13}
$$

所以无需先分别包围可能较大的 $a_sT/a$ 和 $T_s$ 再求和。此相消作用于准确对象，不依赖采样法向是否机器精度正交。

定义参考矩阵

$$
Q_0=
\begin{pmatrix}
N_0\cdot A_0&N_0\cdot T_{0,s}\\
N_0\cdot T_{0,s}&N_0\cdot(T_{0,u}/a_0)
\end{pmatrix}.
\tag{14}
$$

这是本文使用的准确参考表达式。其输入证书必须包围式(14)，包括浮点点积/normalization 的必要误差。若其他程序以未相消的近似 mixed jet 或舍入矩阵输出，必须先支付它与式(14)的差，不能直接换一个名称当作同矩阵。

由准确加减，

$$
\left|\frac{T_u}{a}-\frac{T_{0,u}}{a_0}\right|
\le e_W:=\frac{e_{T_u}}{a_*}
+\frac{N_{T_u}e_a}{a_*a_{0,*}}.
\tag{15}
$$

于是 $Q-Q_0$ 的三个独立分量分别满足

$$
e_L=e_A+e_NN_A,\qquad
e_M=e_{T_s}+e_NN_{T_s},
$$

$$
e_P=e_W+\frac{e_NN_{T_u}}{a_{0,*}}.
\tag{16}
$$

这些式子用 $|N|=1$ 乘向量误差，将法向误差只乘**实际参考组合**，不会无故重复拆开 $A_0$。

对对称矩阵的分量绝对界 $(x,y,z)\ge0$，其算子范数由

$$
\mathcal B(x,y,z)=\frac{x+z}{2}
+\sqrt{\frac{(x-z)^2}{4}+y^2}
\tag{17}
$$

控制。证明：逐分量绝对值被非负对称矩阵
$\begin{pmatrix}x&y\\y&z\end{pmatrix}$ 支配，其最大特征值就是式(17)，且因迹非负，最大特征值同时控制负特征值的绝对值。对任意向量先取逐分量绝对值即可完成比较。

令

$$
\varepsilon_Q=\mathcal B(e_L,e_M,e_P),\qquad
\varepsilon_H=\mathcal B(d_E,d_F,\max|I_{G,0}|).
\tag{18}
$$

则 $\|Q-Q_0\|\le\varepsilon_Q$、$\|H-H_0\|\le\varepsilon_H$。最后一个 Gram 分量直接是准确 $1-|T_0|^2=-r_{G,0}$，不是额外的未支付角向 metric 缺陷。

## 7. 从真实参考矩阵到准确曲率

假设已经在同一盒上证明

$$
-\kappa_0 H_0\preceq Q_0\preceq\kappa_0H_0,\qquad \kappa_0\ge0.
\tag{19}
$$

这是参考矩阵对的 generalized-Rayleigh 上界。它可以由严格 $2\times2$ 主子式/半正定证书支付；不能把旧 GC 的 formal $l,m,n$ 或少数点的主曲率读数直接充作式(19)。

若式(8)给 $\lambda_*>0$，则准确实际曲面的两主曲率均满足

$$
|\kappa_i(X)|
\le \kappa_0+
\frac{\kappa_0\varepsilon_H+\varepsilon_Q}{\lambda_*}.
\tag{20}
$$

证明：对任意实向量 $v$，

$$
|v^TQv|
\le\kappa_0v^TH_0v+\varepsilon_Q|v|^2
\le\kappa_0v^THv+
(\kappa_0\varepsilon_H+\varepsilon_Q)|v|^2.
$$

再用 $v^THv\ge\lambda_*|v|^2$，除以 $v^THv$，得到式(20)。准确曲率是 $(Q,H)$ 的广义特征值，所以这确实控制实际位置图的主曲率，未用 $l=(m^2+K)/n$ 等退化消元。

若已有更紧的逐分量 $Q_0$ 区间，也可各自加 $[-e_L,e_L]$、$[-e_M,e_M]$、$[-e_P,e_P]$，连同式(5)的准确 $H=[1+r_E,r_F,1]$ 交给下游直接 form/PSD 消费者；这可省去一个较粗的统一 $\kappa_0$ 转移。两条路线消费同一准确对象，不要求重复求解。

所有曲率结论只用实际位置二 jet、准确 immersion 和统一误差。跨径向 C² 片界可按共享两 jet 延伸；不引入 C³ 完成门。在 cut 的第二基本形式为零或某主值为零时，论证也不除它们。真正 caps 的两 jet 接缝仍由其独立构造支付，不由本预算代替。

## 8. 可执行薄消费者与真实小核

源 [fd2d_R193_direct_position_error_budget.cjs](../scripts/fd2d_R193_direct_position_error_budget.cjs)，SHA256 fce702f79dcb66267ff4db1cbc204cc388904a2bb444a9fd423016314c91ea80，提供

r193DirectPositionBudget(packet)

和独立 runR193BudgetFixture()。输入 schema 为 fd2d-R193-direct-position-box-budget-input-v1；只接受明确“certified common continuous physical box”或“certified single physical point”，并要求上述全部 accurate/reference/error 身份。它不验证 caller 的基础数学证书，因此输入本身必须由对应消费者真实支付。

所有数由 BigInt 有理运算计算；Number 输入被准确解码为 binary64。平方根用 $2^{-96}$ 的 dyadic 格向外夹取：对非负 $p/q$，先对准确整数比例作 floor/ceil，再用整数平方根，最终得到严格上下界。此处 96 位是输出包围算法的默认精度，不是新的求解完成条件。

实际 functions JavaScript isolate 已运行一次非零条件 fixture，耗时显示 .002 秒：

- 非零误差与参考 residual 全部保留，得相对 metric 上界显示 $5.605724281776416\cdot10^{-10}$；
- 实际 Gram 最小特征值下界显示 $.9999999994394276$；
- 参考 $\kappa_0=7$ 转移后准确上界显示 $7.0000000000002185$；
- 全误差置零时，metric/form 误差准确为零，曲率转移准确保持 $7$；
- 故意不给足 immersion 下界的输入如实返回未决，没有生成曲率证书。

完整严格有理输出见 notes/2026-11-12-fd2d-metric-R193-direct-position-budget-01-report.json，SHA256 d9995f302d11222cae0142b1c7a25f1e561b164487c865b2d180f45ef4f8470b。

该例子是预算函数的真实算术执行，其误差输入是明确条件例子，不是当前主线 B32 状态的测值或已证误差。没有 Node/OS 子进程、wholebody、F/J 或新 BVP，也没有给它们补造 exit。后续应把准确 B32、中央椭圆、R188 全函数 primitive、R190 准确网格与实际有限求值的真正误差包接入同一接口。
