# 原 full47 的有界有限域 Miller 第三类微分读取

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
状态：**算法的来源、除子恒等式与有限认证规则已证明；本新消费者尚未执行。**

本请求读取 R1103 的实际
$\alpha_{Z,y}=(\bar\omega_{D_{Z,y}}/d(j-j_y))(y)$，
其中 $X=X_{\rm ns}^+(47)$、$q=4513$，
$D_{Z,y}=\operatorname{Fix}Z-2Zy$。
原 R1104 的五级 RR 环、R1090 的95元来源、
已经认证的八个 CM 标签与切向值仅按哈希消费。
不重做完整辅助素点筛、高 CM 对数或全局高度。

程序分为两个独立进程：

- full_p47_Miller_support.py：新短模形式 jets 和原角支撑；
  只加载固定 python-flint，不导入 Sage；
- full_p47_finite_third_kind.py：原有限域 RR/Miller；
  Sage 父进程在前一个独立进程结束后才加载数学生态，
  扩域数据只通过整数 JSON 和实际模多项式传送。

这避免了 Sage 与 wheel 的两份 FLINT 在同一进程内被混用。
数学只在本公开仓库的专用 Actions 请求中执行。

## 1. 同一条原曲线、同一个有限环

令
$$
\mathcal L=\Omega_X^1(C_\infty),\qquad
d=167,\quad g=73,\qquad
V_n=H^0(X_{\mathbf F_q},\mathcal L^n).
$$
R1104 已经认证
$$
(\dim V_1,\ldots,\dim V_5)=(95,262,429,596,763),
$$
以及标准 cusp 参数 $t=q_{\rm Tate}^{1/47}$ 下836项的真实单射展开。
线标架为 $\ell=47\,dt/t$；产品的表示系数就是通常的级数乘积。
对 $n\le5$，$\deg\mathcal L^n\le835$，所以836项相等就等价于
实际全局 section 相等。所有乘法、相除和线性核都发生在这些空间中。

R1104 的原前两 section $s_0,s_1\in V_1$ 无公共零点。
下文保留这个 pencil；另取的基 section $f_0$ 不必等于 $s_0$。

记 $N=\#J(\mathbf F_q)$。
R1089 的 run45941243499/job140315814260 给
$N\bmod4513=551$。本请求直接消费完整十进制整数及其字符串 JSON 的
SHA-256
cd5db67aa8fa60ef764bb773a9a694878698cba5663f6bfe2cfd2f2b3d863e41，
不重新计算 $T_q$ 或点数。

若 $\bar D$ 是定义于 $\mathbf F_q$ 的度零除子，支撑避开 $y$，
对 $\operatorname{div}f=N\bar D$ 有
$$
\boxed{\quad
\alpha_{\bar D,y}
 =N^{-1}\frac{d\log f}{d(j-j_y)}(y).
\quad}
\tag{M.1}
$$
R1103 已把它接到真正的整规范第三类微分；
不是仅由 Cartier 固定猜测补线。常数倍 $f$ 不影响读数。

## 2. 本次两条实际角和完整支撑

采用 R1078 的原对称角 $R_C$，$C\sim-C$，$C\ne\pm1$。
设
$$
Z_A=13R_0+4R_2,\qquad Z_B=2R_4-7R_0.
$$
二者 trace zero，degree 分别为504和$-72$；
不把它们称为 degree zero 对应。完整 fixed-cycle 给
$$
\operatorname{Fix}Z_A
 =\left(\frac{13}{2}R_{20}+2R_5\right)y_4
  +\frac{26}{3}R_4y_3+8C_\infty,
$$
$$
\operatorname{Fix}Z_B
 =-\frac72R_{20}y_4
  +\left(\frac43R_{12}-\frac{14}{3}R_4\right)y_3
  +8C_\infty.
\tag{M.2}
$$
$y_4,y_3$ 均是原 canonical47-Cartan 点。
程序使用实际整数除子 $6D_{Z,y}$：
$$
\begin{aligned}
6D_{Z_A,y}
 &=39R_{20}y_4+12R_5y_4+52R_4y_3+48C_\infty
   -156R_0y-48R_2y,\\
6D_{Z_B,y}
 &=-21R_{20}y_4+8R_{12}y_3-28R_4y_3+48C_\infty
   -24R_4y+84R_0y.
\end{aligned}
\tag{M.3}
$$
每个完整 signed multiset 的 degree 实际核为零；
末尾严格除以6。

R1074/R1086/R1103 已付：
非恒等 raw 角支撑避开全部八个 canonical CM 中心。
所有 conjugates、粗点重数及23cusps 均保留。
不借 principal 角的 degree/cusp-zero 性质删项。

### 2.1 原几何点及 Frobenius 轨道

对八个已认证模型，复用原47挠点标记和 Weil root2。
在 real/imaginary basis 中
$$
I=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$
全 necklace 由
$$
I'=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\quad
a^2+bc=-1,\quad I'\sim-I'
$$
给出，恰1081个。$c\ne0$，因为 $-1$ 在 $\mathbf F_{47}$ 中非平方。
选 $r^2+s^2=c^{-1}$，则
$$
B=\begin{pmatrix}r+as&-s+ar\\cs&cr\end{pmatrix},
\quad \det B=1,\quad I'B=BI.
\tag{M.4}
$$
所以新的真实标记仍有 Weil root2，没有未付相位。

角标签是 $-\operatorname{tr}(II')/2\bmod\{\pm1\}$。
完整原纤维有24项（$C=0$）或48项。
先按真实几何自同构取粗点，保留合并重数；
不把 raw 标签冒称互异粗点。
Gaussian 的有效自同构是 $\mu_2$，cubic 是 $\mu_3$，
其它模型只有恒等有效自同构。所有作用和 Frobenius
都在同一个实际47挠点基上读取。
Frobenius 共轭后分成完整闭轨道；原95元 projective 坐标
再次验证闭点的最小 residue field。

实际 Reynolds section 始终保 R1090 的两相位和
$$
\sum_{x\ne0}\left(
 \zeta^{aN(x)}e_xe_{\rho x}
 +\zeta^{-aN(x)}e_xe_{\bar\rho x}\right).
\tag{M.5}
$$
不合成 cosine 子族，不删一般纯虚 $\rho$。
每个新 target 只重排同一2208点网格，不重新求挠点。

### 2.2 支撑值和八目标导数分别付款

Miller 初始化只需支撑点处的 $\mathcal L$ 纤维值。
若实际有效 stabilizer 为 $e_s=1,2,3$，
取 fine 参数 $u$ 下 section 系数的 $u^{e_s-1}$ 项；
95项再除以一个非零项，得到真正 projective 值。
公共线标架及 Frobenius 合并的自同构尺度同时相消。

$R_0(y_4)$ 的 anti-Cartan 点可能仍被 $i$ 正规化，此时须读 fine 一阶。
若非canonical标记的 stabilizer 平凡，则用其 fine 参数；
不能把分歧的 $j$ 当普通可逆坐标。

只有八个目标需要粗一阶。使用原完整短流
$$
\begin{aligned}
A_2'&=A_2^2/12+4A,& A'&=A_2A/3+6B,&
B'&=A_2B/2-4A^2/3,\\
e'&=A_2e/12-xe-y,\\
x'&=A_2x/6+2ey+2x^2+4A/3,\\
y'&=A_2y/4+3xy+e(3x^2+A).
\end{aligned}
\tag{M.6}
$$
它是 R1090 的同一 completed-zeta/Gauss–Manin 流，
保留 $A_2$ 的全部导数，且 $KS(\partial)=1$。
初值 $A_2=0$；generic、Gaussian、cubic 的 $F_i(u)$
分别读取到1、3、5阶，而 $j(u)$ 只需分别到1、2、3阶。
这里保存普通 Taylor 系数，递推中的 $k+1$ 分母全部为模4513单位；
原低阶回执保存的是导数，两种规范以 $k!$ 严格转换。

令 $e=1,2,3$ 为目标的实际有效 stabilizer，
$z=j-j_y=j_eu^e+O(u^{e+1})$，其中 $j_e\ne0$。
每个 $F_i$ 的 $u^{e-1}$ 以下系数为零。选择首个
$f_{k,e-1}\ne0$ 的来源 $F_k$，直接相除
$$
R_i(u)=
\frac{u^{1-e}F_i(u)}{u^{1-e}F_k(u)}
 =R_i(0)+R_{i,e}u^e+O(u^{e+1}).
$$
比值在原粗曲线上，故 $u,\ldots,u^{e-1}$ 项必须为零。
程序逐项验证这些零、$j(u)$ 的低于 $e$ 阶零和 $j_e\ne0$，然后准确读取
$$
\boxed{\quad
a_{i,0}=\frac{f_{i,e-1}}{e j_e},\qquad
R_i(y)=\frac{a_{i,0}}{a_{k,0}},\qquad
\frac{dR_i}{d(j-j_y)}(y)=\frac{R_{i,e}}{j_e}.
\quad}
\tag{M.7}
$$
只用 $F_i$ 到 $2e-1$ 阶即可完成相除到 $e$ 阶；
无需先计算绝对微分系数的一阶，也不需要 $j_{2e}$。
不把分歧的 $j(u)$ 当普通可逆幂级数。

为了保留全部实际旧来源，新网格在同一初值上核对
$$
e_0,\qquad
e'_0=-x_0e_0-y_0,\qquad
e''_0=-2e_0^2y_0-4x_0^2e_0-2Ae_0-2x_0y_0.
$$
每个目标只消费原 R1105 已计算的低0/1/2阶。
完整2208点低阶网格哈希、95个原热导数哈希和95个粗切向值哈希
均必须逐字等于 run45968484065/job140402824955 的回执；
代码同时比较 (M.7) 与 R1105 的原 KS 闭式，并核归一化
$R_i(y)=a_{i,0}/a_{k,0}$。这复用本次已经重建的网格，
不进行第二次 seed 或挠点计算。
全部新高阶还逐点核 $e(-P)=-e(P)$ 和实际 Frobenius 运输，
并以 $y(u)^2=x(u)^3+A(u)x(u)+B(u)$ 核完整短流。

JSON 字段为 denominator_index、ratio_values、ratio_dz，
并附原 coarse_tangent95_sha256。每个目标另即时输出三个旧哈希、
新比值/导数哈希及精度的紧凑回执；支撑计算即便随后未完成，
已经完成的短 jet 核验也不会被误称为未执行。

## 3. 固定实际基除子和全部函数框架

从无基点 pencil 取 $f_0=s_0+c s_1$，
实际核它避开全部支撑和八目标，记 $D_0=\operatorname{div}f_0$。
每个几何点最多排除一个 $c$，程序在固定有限前缀寻找并验证。

目标处统一用 $f_0^n$ 平凡化 $V_n$。
95个原 projective 值和一阶导数按商法则再除以 $f_0/F_k$，然后按实际产品索引传播。
所以 $f_0$ 的表示恒为1、导数为0，
$d\log(s/f_0^n)=s'/s$ 是原函数的精确读数。
没有漏掉 line-frame connection。

中间主截面都实际挑成在八目标取单位。
只保存八个 $f'/f$，不保存大主函数；
不在零值上作数值除法恢复精度。

## 4. degree167 点代表和 AddFlip

对有效 $\deg E=167$，
$$
W_E=H^0(\mathcal L^2(-E))\subset V_2,\qquad\dim W_E=95.
$$
代表同时保存精确 formal divisor label $D$ 和八点函数读数：
$$
\operatorname{div}F=D-(E-D_0).
\tag{M.8}
$$

对 $E_1,E_2$，读取实际 $W_{E_1}W_{E_2}\subset V_4$。
实际 rank 达到262时，它恰为
$Z=H^0(\mathcal L^4(-E_1-E_2))$。
未达此秩则报告该步未完成，不预设张成。

原 $s_0,s_1$ 无公共零，故
$$
U=\{s\in V_3:ss_0,ss_1\in Z\}
 =H^0(\mathcal L^3(-E_1-E_2)),\quad\dim U=95.
\tag{M.9}
$$
取 $s\in U$ 避八目标，
$\operatorname{div}s=E_1+E_2+E_3$。
若 $u\in U$ 和 $s$ 的 residual gcd 为 $G$，
$$
\{t\in V_2:tu\in sV_2\}
 =H^0(\mathcal L^2(-E_3+G)).
\tag{M.10}
$$
右侧维数准确为 $95+\deg G$，因为其degree为$167+\deg G>144$。
所以实际 colon 维数95严格证明 $G=0$，
给完整 $W_{E_3}$，不用分解中间除子。乘法最高为 $V_5$。

主函数的准确更新为
$$
F_3=(F_1F_2s/f_0^3)^{-1},\qquad
\gamma_3=-\gamma_1-\gamma_2-d\log(s/f_0^3).
\tag{M.11}
$$
代码同步更新完整 divisor label，不只核点类或哈希。

负点取 $s\in W_E$，
$\operatorname{div}s=E+E_-$，同样的 $V_4$ colon 给 $W_{E_-}$，且
$$
F_-=(F s/f_0^2)^{-1}.
\tag{M.12}
$$
有限 section 前缀只接受实际单位和秩都通过的选择；
“通常随机能选到”不是任何结论的假设。

## 5. 闭点初始化，不假设 cusp vanishing sequence

固定标准 cusp $b$。消费者先把原23-cusp矩阵第0行与原836-jet矩阵的常数列转为同一个 $\mathbf F_q^{95}$ 向量，逐项核二者相等，才把 $b$ 记为 cusp_0；因此下面的高阶消失条件确在同一标准 cusp。对其它闭点 $P$，$f=\deg P$，
要表示 $A_P=P-fb$。
不要求 $D_0$ 含 $fb$，不假设某个未付的特殊vanishing sequence。

由真实 projective 值得到 $H^0(\mathcal L^2(-P))$，
完整 residue-field 系数约束实际 rank 必为$f$。
取 $h,g$ 在此空间，$h$ 避 $b$ 和八目标。
若 gcd 是 $P+G$，则
$$
U_0=\{s\in V_3:sg\in hV_3\}
 \simeq H^0(\mathcal L(P+G)),
$$
其维数为 $95+f+\deg G$。
实际值 $95+f$ 精确认证 gcd 恰为 $P$。

在 $U_0$ 加 $b$ 处前$f$个原cusp系数为零，得到
$$
U=H^0(\mathcal L^3(-E_{\rm big})),\quad
E_{\rm big}=\operatorname{div}h-P+fb,\quad \dim U=95.
\tag{M.13}
$$
$h(b)\ne0$ 排除隐藏的 base-cusp 修正。
取 $s\in U$ 避八目标，$E=\operatorname{div}s-E_{\rm big}$。
§4的 residual-gcd colon 给它的准确 degree167 代表。
真正的初始函数是
$$
\boxed{\quad F_P=h f_0/s,\qquad
\operatorname{div}F_P=(P-fb)-(E-D_0).\quad}
\tag{M.14}
$$
初始读数是 $d\log h-d\log s$，不省去它而只保点类。

本次每个 divisor 的degree为零，
写成 $\sum_{P\ne b}m_P(P-\deg(P)b)$ 恰恢复原 $b$ 系数；
消费者逐字核此整数等式。

## 6. signed $N$-Miller 链和终点

初始化完整除子后只做一条 $N$ 链。
当前 coefficient 为 $\epsilon m$，
doubling AddFlip 给 $-\epsilon(2m)$；
下一位为1时，再与 coefficient $-\epsilon$ 的原正／负初始代表
作 AddFlip，给 $\epsilon(2m+1)$。
所以每bit一次 AddFlip，1-bit再一次，不必每步额外转正。
末尾完整 label 验证准确系数 $\epsilon N$。

$N[D]=0$ 迫终点 $[E_N-D_0]=0$。
通过原pencil求
$$
H^0(\mathcal L(-E_N))
 =\{h\in V_1:hs_0,hs_1\in W_{E_N}\},
$$
实际必须为一维。非零 $h_{\rm end}$ 满足
$\operatorname{div}(h_{\rm end}/f_0)=E_N-D_0$。
因此
$$
f=F_N(h_{\rm end}/f_0),\qquad
\operatorname{div}f=\epsilon N D.
\tag{M.15}
$$
终点导数必须**正加**。整个 $E_N$ 已避八目标，
故 $h_{\rm end}$ 自动为单位。

对于 $D=6D_{Z,y}$，答案准确是
$$
\boxed{\quad
\alpha_{Z,y}
 =\frac{\gamma_N(y)+d\log(h_{\rm end}/f_0)(y)}
        {6\epsilon N}.
\quad}
\tag{M.16}
$$
所有分母模4513为单位；未删除6、signed multiplier或终点运输。

## 7. 有限认证、并行和保存范围

所有row space均是实际836-jets的子空间。
$xA\in\operatorname{row}(B)$ 由 $[A;-B]$ 左核投影读取，
程序核乘法像 $B$ 注入和投影无额外核。

每步保产品262、$U$95、residual colon95；
初始化保闭点rank$f$、初始colon$95+f$、cusp修正后95；
终点保一维主函数空间。全部是原有限域精确线性代数。

最多四个 Sage fork worker 处理四个指定case。
原graded输入只读共享；每个case重置其确定section前缀与操作哈希，
结果不依赖调度。已结束的纯flint进程不进入Sage fork。
case列表、section前缀、field预算和总budget/reserve都写入请求。

每个完成case输出实际$\alpha$、
同一个函数在八目标的全部读数、初始化/终点/链哈希。
失败或超时只保已完成case，不宣其它行。
大矩阵、原级数、projective值和中间函数只留runner scratch；
不提交可重算raw、artifact或Release。

## 8. 最终QC接口仍须实际完成

本请求只付款 R1103 的 $\alpha_{Z,y}$。
原 $b_y$、实际角作用 $z_Z$、完整高度 $K=\kappa/a$
和真正的 $d_{Z,y}$ 坐标各有原来源，不互相替代。
其准确首项是
$$
t(B_{Z,y}+A_{Z,y}t),\quad
A_{Z,y}=-\operatorname{Tr}(Kz_Zb_y^2),\quad
B_{Z,y}=\operatorname{Tr}(Kb_yd_{Z,y})-\alpha_{Z,y}.
$$
只有实际完成的行秩连同整尾判据才能排盘。
本稿不提前声称八盘唯一性或Serre主目标已完成。

## 9. 来源和纸面核查

- R1090 原完整Reynolds95、23cusps、尺度和完整短流。
- R1103 coarse参数、(M.1)、非$q$项、QC首jet和整尾。
- R1104 原五级RR、836单射及无基点pencil。
- R1078 全原角、fixed-cycle和粗点/核重数。
- R1089 原 $N=\#J(\mathbf F_{4513})$。
- R151 §2 的一般Miller invariant；本篇对full47的$d=167$、
  五级环、初始化和终点重新证明，不搬level41的任何数值。

o2已独立纸核 §4–6 的除子符号、维数及终点正加；
o1已独立纸核 §2.2 的粗jet公式和cusp留数规范。
程序尚未运行，公开回执前不报告任何新的数值 $\alpha$。
