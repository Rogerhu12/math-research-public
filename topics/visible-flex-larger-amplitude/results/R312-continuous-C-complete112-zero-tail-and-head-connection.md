# R312 原连续 C 根族的完整 112 模态零响应尾图与有限头连接

- 作者：AI，GPT-6 Astra Pro，geometry
- 日期：2026-11-15
- 状态：下述有限模态无限尾定理及误差界已证明。没有运行新的科学计算，没有实际新的 C 零响应、cut Jacobian、非零 BVP 或闭曲面证书。

本文固定 [R286](R286-original-stored-continuous-integral-and-metric-bridge.md) 的连续约定 $\mathcal C$，保留其原冻结量、原真实根类别及其选择责任。对于原表示中的全部 $112$ 个频率 $m=2,4,\ldots,224$，给出一个共同、明确的深端起点和完整半线构造。结果包括真实深尾线性图、可计算的截尾误差、有限头传递和完整物理 Robin 行。

无限尾图成立不意味着有限头 cut 的高度投影非零。本文把这个分母责任单列；一个有限浮点 pivot 或完整传递矩阵可逆，都不能替它作证。结果也不将另一个有理深源、旧 finite evaluator 或旧零 Jacobian 改称新 C 的输出。

## 312.1 对象、来源与编号

### 312.1.1 同一连续对象

保持 R286 的原冻结数据及实解释，特别是

$$
0<d_0\le\frac1{10},\qquad 0<c_0\le\frac1{16},\qquad
r_c>0,\quad \epsilon_{\rm phys}>0,
$$
$$
a=\frac{11}{4},\qquad
\delta_n=d_0\,2^{-n},\qquad
c_n=c_0\,2^{-n/2},\qquad
\eta_n=c_n\delta_n,\qquad
\mu_n=\epsilon_{\rm phys}\delta_n^a.
\tag{312.1}
$$

在全部 $n\ge160$ 上，使用未经有限头 cap、valley、flat 或 warp 修改的原九段深源。它的六个短段各长 $\eta_n$，三个平台各长 $\delta_n$；对数层值按原 quintic
$S(x)=10x^3-15x^4+6x^5$ 连接

$$
1,\qquad \frac{64}{\delta_n},\qquad
\frac{\delta_n}{\alpha_n},\qquad
\frac1{\delta_n},\qquad 2^a.
\tag{312.2}
$$

记这个完整正函数为 $p_n(s)$。深域取

$$
r=r_o(s)=r_c e^{s/\sqrt{12}},\qquad
w(s)=\frac{\mu_n p_n(s)}{r_o(s)^7}.
\tag{312.3}
$$

**同一层的 $\alpha_n$ 只选一次，并供所有模态共用。** 它是原 mode2 准确胞元下左传递元为零的一个根，且属于 $[1/2,2]$。本文不将它设为 $65/64$，也不为每个频率重新选根。R286 已证明每层有这样的根，并给出对所有根同时成立的界

$$
\left|\alpha_n-\alpha_0\right|
 \le\frac{B_n}{64},\qquad \alpha_0=\frac{65}{64},
$$
$$
B_n=792e^{384c_n}(384c_n+36\delta_n^2).
\tag{312.4}
$$

若选择规则尚未登记，本文的对象是所有这种固定根序列组成的背景族；所有结论对这个族统一成立。唯一的零响应数值对象还需要一个唯一根规则。可采用 R286 §286.8 的固定有理点枚举与严格异号嵌套规则；这不是声称旧 ready 已经自动选定它。

有限头 $n<160$ 的全部原保存常数、六 primitive、$\lambda$、cap/flat/valley/weight 与原保护端责任均沿 R286。本文不重新选择这些常数，不把名义 cut 强制等于真实 $R_{\rm out}$。

### 312.1.2 确切源级切点

原九段公式源为：

- general_root_smooth_tail_cells.cjs，6319 字节；
- SHA256：d074799099e27401456449343c8f490ec60cdec7eb0d02758f024f541d409575；
- 本次读取的 Git blob：3b98e488e05b2cce59ff8d9d03b4ad78302d8efa；
- 公开路径：topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_smooth_tail_cells.cjs。

其 cellSegments 依次给 port、transition、plateau、transition、plateau、transition、plateau、transition、port；smoothCellTransfer 的实数生成元是下面的 (312.6)。原函数本身使用有限 RK 和浮点 calibration；本文使用其准确实公式，不把该有限算法称为准确积分或根证书。

[R269](R269-native-zero-reference-height-slope-gauge.md) 已从原零形状局部块证明 $u=r^4Q$、$k=u_r$ 的可逆变换。这里复用该代数而使用新的连续 $r,w$；不复用旧 literal tables 的实际数值或 [R283](R283-finite-root-trace-differentiation-with-literal-tables.md) 的有限 root/RK 导数身份。

[R15](R15-rational-deep-tail-and-46-parameter-trace.md) 的三个 shear 和 Green 思路是相关结构。该文另取 $\alpha_n=65/64$ 且采用增长的角解析宽度；本文两者都没有照搬。本文只有固定的完整 $112$ 模态，使用实际根族和不增长的有限维权范数，所以这里的 $112$ 个尾方向不与 R15 的全频权空间中 $46$ 个自由参数相矛盾。

### 312.1.3 端口与传播方向

令 $U_n=(Q_n,\Pi_n)$ 位于 source cell $n$ 的**内端**。胞元 $n$ 从内向外传播后接到 $U_{n-1}$，因此

$$
U_{n-1}=T_nU_n.
\tag{312.5}
$$

这就是 R18 已明确的编号：数学端口 $F$ 对应程序的 **physical node $F+1$**。例如 $F=159$ 位于全部深胞元 $n\ge160$ 的外边界，也是有限头 cell159 的内端。

同一 cell 内的 $\mu_n$ 固定。到外端后，$\mu_{n-1}=2^a\mu_n$；保持 R269 的物理高度与斜率要求 $Q$ 不变、$\Pi$ 乘 $d=2^{-a}$。这个端口因子不能删去或在两个方向重复施加。

## 312.2 原 canonical 块与完整平衡

取

$$
m=2j,\quad 1\le j\le112,\qquad
\nu=\frac{m^2(m^2-1)}{12}
   =\frac{j^2(4j^2-1)}3\ge1,
$$
$$
\beta=\frac{m^2-4}{\sqrt{12}},\qquad
\kappa^2=\frac{7m^2-16}{12}>0.
$$

orientation 为原 C 的 $+1$。由 (312.3) 和 R269，cell 内原变量满足

$$
\frac{d}{ds}\binom Q\Pi
 =
 \begin{pmatrix}
 \beta&1/p\\
 -\nu p&-\beta
 \end{pmatrix}
 \binom Q\Pi.
\tag{312.6}
$$

定义固定、可逆的模态平衡

$$
V=S_\nu U,\qquad
S_\nu=\operatorname{diag}(1,\nu^{-1}).
$$

它没有丢弃 $\Pi$，只把第二坐标写为 $\Pi/\nu$。此时

$$
V_s=B(p)V,\qquad
B(p)=
\begin{pmatrix}\beta&\nu/p\\-p&-\beta\end{pmatrix},
\qquad B(p)^2=-\kappa^2 I.
\tag{312.7}
$$

本文以下的矩阵范数为诱导列和范数 $\|\cdot\|_1$。记九段准确基本矩阵乘积为 $\Phi_{m,n}$，平衡后完整含端口的传递为

$$
\widehat T_{m,n}=
\begin{pmatrix}1&0\\0&d\end{pmatrix}\Phi_{m,n},
\qquad d=2^{-11/4}.
\tag{312.8}
$$

$S_\nu$ 与端口对角矩阵可交换。原未平衡传递为
$S_\nu^{-1}\widehat T_{m,n}S_\nu$。cell 内迹为零，故
$\det\Phi_{m,n}=1$、$\det\widehat T_{m,n}=d>0$。

三个平台在 $\delta\to0$ 时的完整 shear 分别是

$$
N_1=\begin{pmatrix}1&0\\-64&1\end{pmatrix},\qquad
N_2(\alpha)=\begin{pmatrix}1&\alpha\nu\\0&1\end{pmatrix},\qquad
N_3=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\tag{312.9}
$$

按原传播次序相乘，再只在参考矩阵中取 $\alpha_0=65/64$，得到

$$
T_{m,0}
 =
\begin{pmatrix}
1-65\nu&(65/64)\nu\\
65d(\nu-1)&d(1-(65/64)\nu)
\end{pmatrix}.
\tag{312.10}
$$

(312.10) 是用于比较的理想矩阵。实际 $\widehat T_{m,n}$ 仍保留所有短段、实际平台指数和实际 $\alpha_n$；下面逐项支付它们的差。

## 312.3 所有实际根、所有 112 模态的一致误差

**命题312.1。** 对每个 $m=2,\ldots,224$（偶数）、每个 $n\ge160$ 以及每个允许的同层根 $\alpha_n$，有

$$
\|\widehat T_{m,n}-T_{m,0}\|_1
 <2^{72}c_n+2^{57}\delta_n.
\tag{312.11}
$$

**证明。**

首先，在这个完整有限模态范围内，

$$
\nu<2^{28},\qquad 0\le\beta<2^{14},\qquad
\kappa^2<2^{16}.
\tag{312.12}
$$

这些是整数上界，不来自谱采样。例如
$224^4/12<2^{28}$ 等价于 $7^4<12\cdot2^8$；对 $\beta$ 使用
$\sqrt{12}>49/16$ 即可。因为 $\alpha\in[1/2,2]$，原 quintic 对数插值在整个九段保持

$$
\delta/2\le p\le64/\delta.
$$

连同 (312.12)，对每个短段有

$$
\|B(p)\|_1<\frac{2^{30}}{\delta}.
$$

六个短段的总积分范数因此小于

$$
\mathcal L=2^{33}c.
\tag{312.13}
$$

对于三个平台，准确指数是

$$
\exp(\delta B_i)
  =\cos(\kappa\delta)I+
       \operatorname{sinc}(\kappa\delta)\,\delta B_i.
$$

写 $\delta B_i=(N_i-I)+D_i$。保留两个非零非理想项，可直接得到

$$
\|D_i\|_1\le\beta\delta+2\nu\delta^2<2^{15}\delta,
\qquad n\ge160.
$$

令 $s_i=\|N_i\|_1$。则
$s_1=65$、$s_2=1+\alpha\nu\le3\nu$、$s_3=2$，所以

$$
s_1s_2s_3\le390\nu<2^{37}.
\tag{312.14}
$$

用准确实不等式
$|\cos x-1|\le x^2/2$、
$|\operatorname{sinc}x-1|\le x^2/6$、
$|\operatorname{sinc}x|\le1$，得到

$$
\frac{\|\exp(\delta B_i)-N_i\|_1}{s_i}
 \le \frac23\kappa^2\delta^2+2^{15}\delta
 <e:=2^{16}\delta.
\tag{312.15}
$$

没有交换任何矩阵的次序。对原九因子的有序乘积逐因子作差，短段分别用
$\|\Phi\|\le e^\ell$、$\|\Phi-I\|\le e^\ell-1$，平台用 (312.15)，可得

$$
\|\Phi_{m,n}-N_3N_2(\alpha_n)N_1\|_1
 \le s_1s_2s_3\{e^{\mathcal L}(1+e)^3-1\}.
\tag{312.16}
$$

$n\ge160$ 给
$c_n\le2^{-84}$、$\delta_n<2^{-163}$。
于是
$v=\mathcal L+3e<2^{33}c+2^{18}\delta<1/2$。
使用 $(1+e)^3\le e^{3e}$ 和 $e^v-1\le2v$，(312.14)–(312.16) 给

$$
\|\Phi_{m,n}-N_3N_2(\alpha_n)N_1\|_1
 <2^{71}c_n+2^{56}\delta_n.
\tag{312.17}
$$

现在支付真实根与参考值的区别，而不是将其删除。由 (312.4) 及 $e^{384c}<2$，

$$
B_n<2^{20}c_n+2^{17}\delta_n^2,\qquad
|\alpha_n-\alpha_0|
 <2^{14}c_n+2^{11}\delta_n^2.
\tag{312.18}
$$

又有

$$
\|N_3[N_2(\alpha_n)-N_2(\alpha_0)]N_1\|_1
 \le130\nu|\alpha_n-\alpha_0|
 <2^{50}c_n+2^{47}\delta_n^2.
\tag{312.19}
$$

最后端口矩阵范数等于1。合并 (312.17)、(312.19) 并用 $\delta_n<1$，即得 (312.11)。全部界对同一层允许的每个根及全部频率同时成立。证毕。

### 归一后真正小的误差

取 $b=11/2$，令

$$
X_n=(-1)^n\delta_n^{-b}S_\nu U_n.
$$

由于 $\delta_n/\delta_{n-1}=1/2$，原准确关系等价于

$$
X_{n-1}=A_{m,n}X_n,\qquad
A_{m,n}=-2^{-b}\widehat T_{m,n}
       =A_{m,0}+E_{m,n},
$$
$$
A_{m,0}=-2^{-b}T_{m,0}.
\tag{312.20}
$$

统一的负号来自相邻 $(-1)^n$，不是从一次实际求解猜测的符号。由 (312.11)，

$$
\|E_{m,n}\|_1
 <2^{67}c_n+2^{52}\delta_n
 <2^{-16}\,2^{-(n-160)/2}.
\tag{312.21}
$$

对端口 $F\ge159$ 定义明确的有理界

$$
\varepsilon_F
 :=2^{-16-\lfloor(F-159)/2\rfloor}.
\tag{312.22}
$$

则全部 $n\ge F+1$ 满足 $\|E_{m,n}\|_1<\varepsilon_F\le2^{-16}$。
这里 $F=159$ 已有效；没有遗漏 $n=160$，也没有把程序 node159 当成该端口。

## 312.4 参考谱、方向与全模态 Green 算子

记 $T_{m,0}$ 的两个特征值为 $-L_m,-S_m$，其中 $L_m>S_m>0$。令

$$
H=65\nu(1+d/64)-1-d.
$$

直接乘开 (312.10) 得

$$
\det T_{m,0}=d,\qquad
\operatorname{tr}T_{m,0}=-H,\qquad
L_m+S_m=H,\quad L_mS_m=d.
\tag{312.23}
$$

多项式 $f(x)=x^2-Hx+d$ 在 $64\nu$ 处的准确值为

$$
f(64\nu)
 =-(\nu-1)\{64\nu+d(65\nu+1)\}\le0.
$$

因此

$$
L_m\ge64\nu,\qquad L_m<66\nu,\qquad
0<S_m\le\frac d{64\nu}<\frac1{64\nu}.
\tag{312.24}
$$

$\nu=1$ 时准确为 $L_2=64$、$S_2=d/64$；其余频率第一不等式严格。

$d<1/4$ 给 $\|T_{m,0}\|_1<82\nu$。谱间隔大于 $63\nu$，所以完整两个谱投影

$$
P_u=\frac{T_{m,0}+S_m I}{S_m-L_m},\qquad
P_s=I-P_u
\tag{312.25}
$$

满足

$$
\|P_u\|_1<2,\qquad \|P_s\|_1<3.
\tag{312.26}
$$

这些投影不被替成坐标轴。对 $A_{m,0}$ 的相应正特征值，

$$
\lambda_u=2^{-b}L_m\ge\sqrt2>7/5,\qquad
0<\lambda_s=2^{-b}S_m<2^{-11}.
\tag{312.27}
$$

我们称 $P_u$ 为**向外不稳定、向内衰减**方向。对于写成
$X_{n-1}=A_{m,0}X_n$ 的关系，大特征值使 $n$ 增大时解衰减；
不能因一般“稳定”一词而把两个方向反用。

可取这个方向的高度归一向量

$$
v_m=\binom{1}{s_m},\qquad
s_m=\frac{65\nu-1-L_m}{(65/64)\nu}.
\tag{312.28}
$$

由 $L_m+S_m=H$，

$$
s_m=-d+\frac{d+S_m}{(65/64)\nu},\qquad
-d<s_m\le0,\qquad \|v_m\|_1<5/4.
\tag{312.29}
$$

$\nu=1$ 时 $s_2=0$。

### 半线边界与 Green 公式

在 $n\ge F$ 的有界序列空间，指定且只指定

$$
P_uX_F=v_m z.
\tag{312.30}
$$

对于强迫关系 $X_{n-1}=A_{m,0}X_n+f_n$，完整解是

$$
P_uX_n
 =\lambda_u^{-(n-F)}v_mz
  -\sum_{k=F+1}^{n}\lambda_u^{-(n-k+1)}P_u f_k,
$$
$$
P_sX_n
 =\sum_{k=n+1}^{\infty}\lambda_s^{k-n-1}P_s f_k.
\tag{312.31}
$$

第一式的和在 $n=F$ 为空。第二式来自向深处的有界条件；任何额外的
$\lambda_s^{-(n-F)}$ 齐次项都会无界。两式代回逐项恢复原关系，
并给出唯一性。

由两个几何级数，

$$
\|\mathcal G\|_{\ell^\infty\to\ell^\infty}
 \le\frac2{\lambda_u-1}+\frac3{1-\lambda_s}<9.
\tag{312.32}
$$

把112个模态作直和，每个节点用各个二元 $\ell^1$ 范数之和，
再对节点取上确界，同一个上界仍成立。这个空间没有逐层增加的角解析权；
它是一项明确的有限模态结论。

## 312.5 真实无限尾图及 cuff 端衰减

**定理312.2。** 对每个允许的固定 C 根序列、每个 $F\ge159$、
每个完整 $112$ 维边界向量 $\mathbf z$，存在唯一有界的归一序列
$X=(X_n)_{n\ge F}$，满足所有真实关系 (312.20) 和所有边界条件 (312.30)。
每个模态在 $F$ 的真实解空间是一条一维直线，并且是高度图。

**证明。** 写 $f_n=E_{m,n}X_n$，则完整方程为

$$
X=\mathcal H\mathbf z+\mathcal G(EX).
\tag{312.33}
$$

由 (312.22)、(312.32)，收缩常数小于
$9\varepsilon_F\le9\cdot2^{-16}<1/2$。
Banach 不动点定理在整个线性有界序列空间给出存在、唯一性和线性依赖，
没有另用一个未经验证的数值近似解。并有

$$
\|X\|_\infty
 \le\frac{\|\mathcal H\mathbf z\|_\infty}{1-9\varepsilon_F}
 \le2\|\mathcal H\mathbf z\|_\infty.
\tag{312.34}
$$

单模态 $z=1$ 时，$F$ 点偏差完全属于 $P_s$；(312.31) 给

$$
\|X_F-v_m\|_1
 <\frac3{1-\lambda_s}\varepsilon_F
     \frac{\|v_m\|_1}{1-9\varepsilon_F}
 <10\varepsilon_F.
\tag{312.35}
$$

因此 $X_{F,1}>1-10\varepsilon_F>1/2$，深端高度投影确实非零。
定义真实平衡尾斜率

$$
\mathfrak g_{m,F}=\frac{X_{F,2}}{X_{F,1}}.
$$

利用 $|s_m|<1/4<1$ 和 (312.35)，得到

$$
\boxed{\quad
|\mathfrak g_{m,F}-s_m|<20\varepsilon_F,\qquad
\Pi_F=\nu\,\mathfrak g_{m,F}Q_F .
\quad}
\tag{312.36}
$$

这同时给出完整112条原坐标 far Robin 行

$$
\Pi_m-\nu_m\mathfrak g_{m,F}Q_m=0,\qquad m=2,4,\ldots,224.
\tag{312.37}
$$

它们属于本次 C 的真实深尾图，不是旧 readylineargraph。
图中每条直线的高度投影结论来自 (312.35)，不是从投影方向名或浮点 pivot 得到。
证毕。

### mode2 的准确特殊性

对 $m=2$，每个实际 $\alpha_n$ 都满足准确校准下左元为零，
所以真实平衡传递是上三角矩阵。令 $\Pi=0$ 的第一列逐层传播；
大对角元素由上述扰动界保持归一后的模长大于1，故这个解向深处衰减，
属于定理312.2的有界类。唯一性因而给

$$
\mathfrak g_{2,F}=0.
\tag{312.38}
$$

这是对**准确根**的结论。若实现只用了有限 RK/Newton 近似根，
其下左残差必须另被包围，不能给 (312.38) 同样的准确标签。
浅160层的 frozen binary $\alpha_n$ 也没有因此被变成准确校准根。

### 物理高度在 cuff 的两 jet

该定理的 bounded 类是
$\sup_{n\ge F}\delta_n^{-11/2}\|S_\nu U_n\|<\infty$。
它不是所有可能 $C^2$ 尾解的分类声明。

对固定有限模态范围，九段内的任意部分传播范数有一个与 $n$ 无关的有限上界：
短段用 (312.13)，平台用
$|\cos|\le1$、$|\operatorname{sinc}|\le1$ 和完整 $\delta B_i$。
因此 cell 内同样有

$$
|Q|+|\Pi/\nu|=O(\delta_n^{11/2}).
$$

原对数 quintic 给
$|(\log p)_s|=O((1+|\log\delta_n|)/\eta_n)$，
且 $\eta_n=(c_0/\sqrt{d_0})\delta_n^{3/2}$。
由 (312.7) 得

$$
\|B\|=O(\delta_n^{-1}),\qquad
\|B_s\|=O((1+|\log\delta_n|)\delta_n^{-5/2}).
$$

所以

$$
Q_s=O(\delta_n^{9/2}),\qquad
Q_{ss}=O((1+|\log\delta_n|)\delta_n^3)
 \longrightarrow0.
\tag{312.39}
$$

端口处 $Q$ 及其真实导数按原 $p$、$\mu$ 的关系相接；
$\Pi$ 的坐标重标度不造成物理高度跳跃。
由于 $r_s=r/\sqrt{12}$ 且 $r\to r_c>0$，
$u=r^4Q$、$u_r$、$u_{rr}$ 均趋零。
有限角和的全部二阶以内混合角导数也趋零，故这些**线性高度分量**
可在 cuff 侧以零作 $C^2$ 延拓。

这里没有从高度两 jet 自动推出完整非线性重构、mean、两帽、嵌入或 reach。
这些责任仍分别沿 R286/R294 及原闭场链。尤其本文没有把任意112模态线性数据
宣称为一个已经完成的非零尾族。

## 312.6 可计算截尾，不以“未付为零”假定存在

定理312.2已经在数学上给出真实半线解，不是用某个预算输出的
unresolved==0 假定其存在。本节说明怎样得到可任意精化的有限计算。

取 $N\ge F$。保留实际 $E_n$ 的全部 $F+1\le n\le N$，在更深处暂令
$E_n^{[N]}=0$。这是有明确误差的**辅助截尾系统**；
它不修改真实 C 的深源。辅助深端 $N$ 的线恰为
$\operatorname{span}v_m$，可以经完整有限乘积传播到 $F$。

两个不动点使用同一 $P_uX_F=v_m$。由 (312.33)，

$$
\|X-X^{[N]}\|_\infty
 \le
 \frac{9\varepsilon_N}{(1-9\varepsilon_F)^2}\,\|v_m\|_1
 <45\varepsilon_N.
\tag{312.40}
$$

真实和辅助 $F$ 点的第一坐标均大于 $1/2$，辅助斜率模小于 $1/2$。
对两个商直接作差，得到简单共同界

$$
\boxed{\quad
|\mathfrak g_{m,F}-\mathfrak g^{[N]}_{m,F}|
 <128\varepsilon_N .
\quad}
\tag{312.41}
$$

常数128保留了商分母，不是只比较未归一向量。

如果实际有限计算给出近似归一矩阵 $\widetilde A_{m,n}$，并已严格证明

$$
\max_{F<n\le N}
\|\widetilde A_{m,n}-A_{m,n}\|_1\le\eta,\qquad
0\le\eta\le\varepsilon_F,
\tag{312.42}
$$

则辅助系统的扰动仍小于 $2\varepsilon_F$。其 $F$ 点相对 $v_m$ 的
偏差小于 $20\varepsilon_F$，故第一坐标仍大于 $1/2$、斜率模仍小于 $1/2$。
两个强迫系统的差满足
$\|X-\widetilde X\|_\infty<45(\varepsilon_N+\eta)$；这里对真实系统
使用 $1/(1-9\varepsilon_F)<2$，对辅助解使用
$1/(1-18\varepsilon_F)<2$。再作同一商估计给

$$
|\mathfrak g_{m,F}-\widetilde{\mathfrak g}^{[N]}_{m,F}|
 <128(\varepsilon_N+\eta).
\tag{312.43}
$$

$\widetilde{\mathfrak g}^{[N]}$ 在此指这个近似矩阵系统的**准确**商；
实际计算该商的舍入或区间包围误差还须加入。
也可以直接用严格区间传播包含 $\mathfrak g^{[N]}$，然后扩张
$128\varepsilon_N$，不把它与单一近似矩阵混用。

要使误差任意小，按已固定的精度请求选择 $N$，
再对有限层的准确根及准确线性 ODE 给收敛严格包围。
原正 log profile 在每个闭有限层上有明确解析表达；
R286 的准确根选择器使用严格 ODE 包围而非浮点符号。
有限层多、条件数大或区间 wrapping 可能增加计算成本，
不改变其有限且可精化的数学责任。

**根族与唯一计算必须分开。**

- (312.36) 是根族统一包络；直接输出它不需要挑一个根。
- 固定 R286 的有效选择规则后，有限 $\alpha_n$ 可任意精化，
  连同 (312.41) 给一个唯一 $\mathfrak g_{m,F}$ 的可计算实数名称。
- 若仅有允许根的粗盒，可以保守传播全族；不能声称其宽度一定缩到零，
  也不能以某个浮点 root 替这个全族指定唯一成员。
- 计算资源截止可以保留已付层、完整剩余层及 (312.41) 的尾界；
  不能删掉未访问层或把非收敛执行当成几何失败。

端口上的非零投影允许选择受证的 projective 归一以控制中间幅度；
一个实际实现仍须把所用分母严格与零分离。
不能因为数学精确图存在就把任意舍入矩阵的 pivot 宣布有效。

## 312.7 有限头使用同一连续 $r,w$ 的完整方程

现在才把无限尾接到有限头。设真实输入已付 R286 §286.7 的保护端兼容性，
并且所求 cut 确在连续对象的实际定义域内：

$$
r_c<r_{\rm cut}\le R_{\rm out}.
\tag{312.44}
$$

若 cut 在 source piece 内部，应包围准确单调方程
$R_*(s_{\rm cut})=r_{\rm cut}$ 的根；不得直接把旧48步 selector 或旧网格点
改称它。若名义 cut 超出已证的自然 $R_{\rm out}$，
本节在该 cut 没有结论，也不作 flat 延拓。

R269 的真实物理变量给

$$
u=r^4Q,\qquad
k=u_r=r^3\left(m^2Q+\frac{\sqrt{12}\mu}{r^7w}\Pi\right).
\tag{312.45}
$$

以物理 $r$ 为自变量，

$$
\frac{d}{dr}\binom uk
 =
\begin{pmatrix}
0&1\\
m^2 w_r/(rw)&-w_r/w
\end{pmatrix}\binom uk.
\tag{312.46}
$$

以 R286 的共同 source $s$ 为自变量，记 $q=w_s$、
$D=(R_*)_s=A+\lambda B>0$，则完全等价为

$$
\frac{d}{ds}\binom uk
 =
\begin{pmatrix}
0&D\\
m^2q/(R_*w)&-q/w
\end{pmatrix}\binom uk.
\tag{312.47}
$$

这明确包括 cap、flat、valley、cut-preserving 和 cusp。
辅助 $R_*$ 在某些 cusp 可能只有 $C^1$，但 (312.47) 的系数连续；
$q$ 的零点不造成除法奇点。$w>0$ 在每个有限闭头区间有正下界。
R286 的真实累计积分负责 $R_*$，而非有限 Gauss point.r 的独立返回。

令 $\Psi_m(r_1,r_0)$ 为 (312.46) 的准确基本矩阵。Liouville 公式给

$$
\det\Psi_m(r_1,r_0)=\frac{w(r_0)}{w(r_1)}>0.
\tag{312.48}
$$

因此完整状态传递可逆。这个式子没有断言任何指定高度分量在终点非零。

在端口 $F$ 的 raw 深侧，$p=1$ 且
$w_F=\mu_F/r_F^7$。用 $Q_F=1$ 归一，真实尾线的物理代表为

$$
v_{m,F}^{\rm phys}
 =
\binom{r_F^4}
 {r_F^3(m^2+\sqrt{12}\nu_m\mathfrak g_{m,F})}.
\tag{312.49}
$$

若从 $F>159$ 起接，应完整保留 $F,F-1,\ldots,160$ 的真实根胞元，
再接160层有限头；不能把这些额外实际胞元删去。
$F=159$ 则直接从深侧接有限头保护端。

定义准确 cut 列

$$
\binom{h_m}{\ell_m}
 =
\Psi_m(r_{\rm cut},r_F)\,
v_{m,F}^{\rm phys}.
\tag{312.50}
$$

因 (312.48) 和初列非零，$(h_m,\ell_m)\ne(0,0)$。
它给出无需除法的完整 Robin 行

$$
\boxed{\quad h_m\,k_m-\ell_m\,u_m=0.\quad}
\tag{312.51}
$$

这已经是一个可用于完整两端线性系统的真实行，
包括 $h_m=0$ 的可能情况；不能为方便输出斜率而丢掉它。
[R277](R277-complete-two-end-chain-determinant-and-high-core-elimination.md)
的完整两端消元结构可以使用这些新 C 行，
但必须重新形成其实际系数和来源，不能复用旧 finite 零响应的数值。

## 312.8 cut 高度 DN 图、全部112行与不能取消的分母

**推论312.3。** 若并且仅若每个请求模态都有 $h_m\ne0$，
该线性尾关系在 cut 处可写成高度到径向斜率图

$$
k_m=\mathcal J_m u_m,\qquad
\mathcal J_m=\frac{\ell_m}{h_m}.
\tag{312.52}
$$

因此新 C 零形状参考的完整112维线性 DN 矩阵是

$$
\mathcal J_{\mathcal C}(0)
 =\operatorname{diag}(\mathcal J_2,\mathcal J_4,\ldots,\mathcal J_{224}).
\tag{312.53}
$$

**证明。** 若 $h_m\ne0$，(312.51) 可直接除以它。
若 $h_m=0$，由于列非零必有 $\ell_m\ne0$，(312.51) 变成 $u_m=0$，
不允许任意给定该高度，所以不是这个高度变量上的 DN 图。
各模态在准确零参考解耦，故全部图存在时矩阵是 (312.53)。证毕。

这里的记号是这个完整线性问题的 DN 矩阵；没有仅凭线性图证明非线性
DN 在零点邻域存在或可微。若同一 C 分支的真实非线性 DN 及其微分已另行
建立，其导数必须满足上述线性化和同一边界类。

在原 $Q,\Pi$ 坐标中，若 cut 处 $Q\ne0$、同一局部 $\mu$ 已明确，
等价公式为

$$
\mathcal J_m
 =\frac1{r_{\rm cut}}\left(
 m^2+\frac{\sqrt{12}\mu}{r_{\rm cut}^7w_{\rm cut}}
       \frac{\Pi}{Q}\right).
\tag{312.54}
$$

不能在已发生端口转换后仍用前一 cell 的 $\mu$。
(312.52) 的 $k$ 是物理 $dH/dr$，正好是现有
geometry_20261114_full_dn_boundary.py 的 tail_map 所要求的量；
原公共材料角 pullback、完整链式 Jacobian、
height_sign*radial_sign/sqrt(E_cut) 仍由原边界消费者承担，
不能重复乘该因子或只保低三个模态。

### 精确误差责任

实际实现应同时保留：

1. 同一连续 C 模型及其实际原冻结输入/根规则；
2. 全112个深端 Robin 包络，含 (312.41) 或 (312.43) 的截尾误差；
3. 所有有限头系数、真实 $R_*$ 累计、cut 逆像与保护端两jet责任；
4. 每个 cut 列的联合包含，以及每个要除的 $h_m$ 的严格非零范围；
5. 真实完整物理行和原单位，而非只打印一组有限近似 slope。

区间包围 $h_m$ 含零可能只是过宽，需要细化；
它也可能反映实际共振。未付时输出 Robin 行包络和确切未付模态，
不声称“DN不存在”，也不声称“DN已经完整”。

先固定 $\mathcal C$ 后，有限头参数没有为了清除分母而暗中改变。
若搜索阶段决定改一个新 $g$ 族，那是另一个显式模型选择；
不是本定理自动修改同一个目标。

## 312.9 可执行实现切点与输出范围

本证明给出的下一最薄实现顺序是：

- **深端生产器**：只读原 C 参数/来源，检查本证明的明确适用范围，
  对全部112模态直接产生 (312.36) 的真实根族包络；
  或在已登记有效根规则下，计算有限准确胞元并加 (312.41)。
  数学存在性已经由本证明支付，数值预算不作存在性定义。
- **有限头连接**：复用 R286/R306 的同一完整函数表达和六 primitive，
  新形成 (312.47) 的全112准确线性传递或严格包围。
  现有 E-cover 的一份粗结果并不自动包含这些矩阵；
  一次正常 schema 也不表示其 cut 或保护端已经有效。
- **两种诚实输出**：始终可以保留完整的非零 Robin 列/行及未付范围；
  只有实际所有分母都受证时才另输出完整 DN 斜率矩阵。
  不能把旧 e788... 或 readylineargraph 的字段重标成 C。
- **后续真正求解**：新连续九标量 profile 可以使用这个新 C 边界作明确的
  线性起始/搜索模型；真实非零尾、完整非线性边界导数、
  原 fullDN/BC/RMS/最终 audit 仍须实际执行。
  一个零参考线性图不是 actual_nonlinear_solve=True。

这里只新增能直接支撑真实计算的解析结论，不增加旧 BVP 的接受门。
现时未给未来 accepted field、$\tau$、误差阈值或未来 run 填值，
也未从一个完整112模态结论冒推全角无限频率问题。

## 312.10 与既有结论的确切差异

R286 付的是连续目标、真实根族、六 primitive 和 cuff/自然外端的几何语义；
它没有给出该根族的112模态尾 DN。
R269 付的是准确零参考的坐标变换；
它没有给出无限尾边界或 cut 无共振。
R15/R18 处理另一个固定有理深源与增长角宽的全频构造；
本文既不借它们的数值证书，也不把其46维结果改成112维。

本文新增支付的是：**在原 C 实际根族上，全部112个请求模态的共同误差阈值、
完整半线规范和唯一有界尾线、深端高度投影、可计算截尾误差、
以及连接有限头后完整 Robin 行与 DN 分母责任的准确分离。**

因此它可直接进入结果索引；不需要先做一个新的合成 fixture。
它仍没有完成本题的非零 BVP、同场连续 metric、两帽、全相位 embedding/reach
或最终闭曲面目标。
