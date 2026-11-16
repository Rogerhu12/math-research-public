# R527：同一加强 R520 母库的有限幅 ruling 路径与完整八矩扰动

日期：2026-11-16。**完整纸面构造；没有执行数值、符号、profile、秩、开发检查或新的科学任务。**

本文给出 [R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md) 局部离开之后的一条真正有限幅正向路径。在同一个从起点加强选择的 R520 型母库、同一个第二规范 $w_\theta=0$ 和一次固定的第三规范 $\chi_\theta$ 下，存在正长度实际路径，完整第四 ruling 在全部 $s,\theta$ 上为零。其曲率实际换号且超过 $1$，其 $\omega$ 振幅严格超过 [R524](R524-same-gauge-constant-return-gates-and-real-matrix-excursion-obstructions.md) 的普适较弱下界 $2/h_{\max}$；没有宣称超过该稿含真实高度能量的更强下界。

这里不把幅度条件当成矩阵返回。实际八矩始终按 $M_{\rm raw}$ 积分，第三入值继承真实常态前缀，末 frame、位置、$M,T,V$ 全部是原恢复的输出。本文没有取得 $M=0$、常态返回 germ、闭 frame、位置闭合或同一完整十三行。

新的选择只发生在母库初选时。本文以三十个明确的有限高阶目标保留原二十行的全部指定数值、R520 的常态平方零与严格非零速度条件，并保其共同 $C^2$ 纤维、四正常、外 cap、宽度、全部实际 copy 和严格开条件。速度导数取本次初选产生的严格正值，不强制为 R520 用于标定的单位值 $1$。它不宣称任意已经冻结的 R520 圆自动具有下文的三矩二次型与统一正则域，更不把 R521 的另一 O(2) 库拼到本圆上。

## 1. 完整同规范方程的二次、线性与余项分解

固定 R520 的实际记号
$$
S=(h,k,\omega),\qquad h>0,\qquad
d=h\omega-k,\qquad e=hx+d,\qquad Q=1+e^2,
$$
$$
\gamma=h_s,\qquad \upsilon=k_s,\qquad
\omega_s=\frac{\upsilon}{2h},\qquad
e_s=\gamma(x+\omega)-\frac{\upsilon}{2}.
\tag{1}
$$
原 profiles、全部积分锚和物理区间 $I=[\ell,r_*]$ 一次固定。

选
$$
S_c=(h_c,0,\omega_c),\qquad
A_c=\Phi_{M_c},\qquad
M_c=M_{\rm raw}(S_c,0,0).
$$
仍有
$$
A_c=-\frac{R_{x+\omega_c}}{8h_c^2}-\frac{T_{x+\omega_c}}8.
\tag{2}
$$
记
$$
y_c=x+\omega_c,\qquad Q_c=1+h_c^2y_c^2,\qquad
L_c=u'-y_cu''.
$$
此处 $T_{x+\omega_c}$ 是原 E8 二次方向，不是第三累计。

R520 的完整 pure self 纤维及全部 $W$ outer 条件使原点态 ruling 在所有允许当前状态上为同一个 $\sin^2\theta$ 倍数，两个加速度的完整系数均为零。以下取其 $\theta=\pi/2$ 标量，但最终结论同时适用于全部相位。

对任意 E8 算子 $A$，定义三个完整实数
$$
q_j(A)=
-I_j(AD,AD)+2I_j\{\phi,A(\phi,AD)\},
\qquad j=0,1,2,
\tag{3}
$$
其中 $\phi=g$、$D=f\odot f-g\odot g$，且
$$
I_0(a,b)=\int a''b'',\quad
I_1(a,b)=\int xa''b'',\quad
I_2(a,b)=\int(x^2a''b''+2a'b').
$$
完整 $AD$ 因原三矩为零而双 collar 紧。第二项的另一输出保原左尾，不能把单包输出当紧函数。

因此整个平方项准确是
$$
q_S(A)=
\frac{(1+d^2)q_0(A)+2hdq_1(A)+h^2q_2(A)}{4h}.
\tag{4}
$$
其对称极化记为
$$
b_S(A,B)=\frac{q_S(A+B)-q_S(A)-q_S(B)}2.
\tag{5}
$$

对固定 $A_c$ 定义完整速度线性式
$$
\ell_S(\gamma,\upsilon)
=\mathcal L_S(A_cD)
=\ell_h(S)\gamma+\ell_k(S)\upsilon.
\tag{6}
$$
$\mathcal L$ 是 R482/R221 的原三槽式，先代入(1)，不把 $\omega_s$ 另作独立速度。

一次固定 R520 的第三 Gram 向量 $\nu$ 后，其完整标量方程可以写成
$$
\boxed{
F(S,m,\gamma,\upsilon)
=\mathcal R_\nu(S,\gamma,\upsilon)
+\mathcal L_S(\Phi_mD)+q_S(\Phi_m).
}
\tag{7}
$$
$\mathcal R_\nu$ 包含 R482 的完整 local 恢复、$v=M_{\rm raw}D$ 的变化-profile chain、当前与真正初端的商势差，以及 $-2\mathbf w(S)\cdot\nu$。它不依赖累计 $m$。没有删掉其速度平方或原左端势；它在任何固定合法紧状态与速度盒内光滑有界。

式(7)正是 R482(25)在 $w=0$、全部 $W$ outer 已付以后按 $m$ 的次数分组。它不是只保 principal 的模型。

## 2. 同一个母库上可用的十个完整高阶坐标

仍按 R520 的实际包序写
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\qquad \lambda_i=-a_i^2R_i.
$$
每个 $u_i$ 的物理平移、宽度和实际振幅规范与原库相同。下式里的 $x$ 始终是共同物理坐标。

定义十个真实 shape 泛函
$$
\begin{aligned}
\mathcal A_j&=\sum_i\lambda_i\int
x^j Q_c(u_i'-y_cu_i'')^2(u_i''')^2,\\
\mathcal B_j&=\sum_i\lambda_i\int
x^j Q_c(u_i'-y_cu_i'')u_i''(u_i''')^2,
\qquad 0\le j\le4.
\end{aligned}
\tag{8}
$$
它们不是被当成 $C^2$ 观察的平方三导，而是下文明确支付的高阶目标。

### 2.1 三个完整平方系数与 $\mathcal A_j$ 的准确关系

令
$$
Q_c=c_0+c_1x+c_2x^2,\quad
c_0=1+h_c^2\omega_c^2,\quad
c_1=2h_c^2\omega_c,\quad c_2=h_c^2.
$$
R520 的完整三导分裂对(3)逐个给
$$
\boxed{
q_j(A_c)=
\frac{c_0\mathcal A_j+c_1\mathcal A_{j+1}
+c_2\mathcal A_{j+2}}{16h_c^4}+e_j,
\qquad j=0,1,2.
}
\tag{9}
$$
$e_j$ 是完整 quartic/$C^2$ 余项，含所有真实左尾、有序项与 $I_2$ 的一导部分。

原系数为
$$
(A_cu^2)''=\alpha_cu'''+C^2,\qquad
\alpha_c=-\frac{Q_cL_c}{4h_c^2}.
$$
因此平方主项是 $x^j\alpha_c^2(u''')^2$，即(9)的系数。单包之间的真实 cross 中，inner 左尾为二次多项式，故至多留下一个 outer 三导；准确 IBP 后属于 $e_j$。真实端项由原 flat jets 支付，不删除原 primitive 常数。

特别，(9)中的 $e_j$ 在一个预先固定的共同 $C^2$ 小邻域内有统一界。这个界不随稍后指定的高阶目标大小增长。

### 2.2 全几何速度式的完整主项

R221(17)在任意 $S$ 上准确为
$$
\mathcal T_S(c;a,b)=\frac1{32h^4}\int
\left[
Q^2c'''\{\gamma(a'b''+a''b')-e_sa''b''\}
-2h\gamma eQc'''a'b'
+F_c\{(\gamma Q-2hee_s)a''b''-2h^2\gamma a'b'\}
\right],
$$
$$
F_c=Qc''-2hec'+2h^2c.
\tag{10}
$$
这里紧 outer 的真实左 jets 已包含在 $F_c$ 的转置中。

设单包 $q=A_c(u,u)$。保真尾并对 $q'''$ 项作一次 IBP，得到
$$
\mathcal T_S(q;u,u)
\equiv_2-\frac1{16h^4}
\int Q^2\alpha_c(\gamma u'-e_su'')(u''')^2,
$$
$$
\mathcal T_S(u;u,q)
\equiv_2\frac1{32h^4}
\int Q^2\alpha_c(\gamma u'-e_su'')(u''')^2.
\tag{11}
$$
第一行的平方来自
$D_x\{2\gamma u'u''-e_s(u'')^2\}$
的 $2(\gamma u'-e_su'')u'''$ 项；第二行来自外三导乘 $q''$。其它项至多线性含三导，使用 R520(20a)的真实局部 primitive 降为 $C^2$。

将原两幅权 $2R_i^2$、$-4b_i^2R_i$ 合并，恰为 $\lambda_i/8$。代入 $\alpha_c$，得到
$$
\boxed{
\ell_S(\gamma,\upsilon)
=-\frac{
\gamma\,\mathcal A[Q^2]
+\{\upsilon/2-\gamma(\omega-\omega_c)\}\mathcal B[Q^2]
}{32h_c^2h^4}
+\mathcal E_S^{\rm low}(\gamma,\upsilon).
}
\tag{12}
$$
若 $P(x)=\sum_{j=0}^4P_jx^j$，记
$\mathcal A[P]=\sum P_j\mathcal A_j$、$\mathcal B[P]=\sum P_j\mathcal B_j$。

$\mathcal E_S^{\rm low}$ 是完整 $C^2$ 余式，关于两速度线性。式(10)的单包非紧 outer 产生的真 Green/左常数，也属于此余式。完整 $A_cD$ 本来紧；先在整圈使用(10)，或先保各包全部边项后求和，得到相同(12)。

在任何预先固定合法紧几何域上，$\mathcal E_S^{\rm low}$ 的系数在上述共同 $C^2$ 邻域内有统一界。这不是把完整 $\ell$ 当成其主项。

## 3. 原二十行与这十行在同一个实际正根中支付

下文实际使用的十行取为
$$
q_0(A_c),q_1(A_c),q_2(A_c),
\mathcal A_3,\mathcal A_4,
\mathcal B_0,\ldots,\mathcal B_4.
\tag{13}
$$
由 $c_0>0$，(9)说明它们的 principal 与(8)的十个 principal 等价。

核独立性时仍用原
$$
W=u'-xu'',\qquad C=u-xu'+x^2u''/2,
$$
旧十九行只含 $x,W,C$，旧第20行为 $2x^4Cu''$。原真实偶配对普遍零核只有常数倍 $uu'$ 与 $u'u''$。

若新增十行的某个组合落入旧二十行与该零核，可写其新增部分为
$$
Q_c\{A(x)(W-\omega_c r)^2+B(x)(W-\omega_c r)r\},
\quad \deg A,\deg B\le4,\quad r=u''.
$$
比较 $Cr$，旧第20行与 $uu'$ 的系数均为零。再比较 $rW,r^2$，必须有某个实常数 $\beta$ 使
$$
Q_c(B-2\omega_cA)=\beta,\qquad
Q_c(\omega_c^2A-\omega_cB)=\beta x.
\tag{14}
$$
$Q_c$ 是非恒二次式，所以第一式迫 $\beta=0$。随后
$B=2\omega_cA$、$-\omega_c^2A=0$，由 $\omega_c\ne0$ 得 $A=B=0$。旧十九行再按原已付独立性全零。

因此原二十行加(13)有三十维真实 principal。新物理位置次数至多八，没有超过原完整十二交替位置可处理的次数十。

从起点选 R520 的同一个 $\mathcal F_{\rm path}$ 限制最大秩图册；如需给(9)(12)逐个余系数另列坐标，只追加有限个已经降阶的 $C^2$ 观察。四正常、新低阶最大 minor 与三十个 principal minor 在同一个有限解析参数族内同时非零。所有见证和纠正都在原允许严格内区，外 cap、根 germs 与原严格开条件保留。

每个主形状仍用原十二个真实交替列；其 $\lambda_i$ 符号与 Vandermonde 核符号相消后给严格正平方幅核。三十行联合满像，所以真实正锥为 $\mathbb R^{30}$。先在一个有限严格正幅盒中匹配完整目标，再取一个足够大但有限的有号集中参数，用原块三角 IFT 得到准确有限根。全部 $C^2$ 纠正留在预定小邻域。

以下目标可以任意大，但先固定为有限数再选择集中参数。这正是 R520/R447 原顺序，不要求一个固定频率同时实现无界目标。所有旧二十行、共同宽度、三矩、八副本、十二翻号 copy、五块及宏复制都在同一实际名单中保留。

## 4. 具体指定同一个零曲面与两条统一速度符号

先取一个固定 $\kappa_0>0$，例如 $\kappa_0=1$，并指定
$$
\boxed{
(q_0,q_1,q_2)(A_c)
=\kappa_0(1,-\omega_c,\omega_c^2-h_c^{-2}),
\qquad
\mathcal A_3=\mathcal A_4=0.
}
\tag{15}
$$
由(4)，准确有
$$
\boxed{
\mathfrak q(S):=q_S(A_c)
=\frac{\kappa_0}{4h}
\{(d-\omega_ch)^2+1-h^2/h_c^2\}.
}
\tag{16}
$$
特别 $\mathfrak q(S_c)=0$，完整保 R520 的常态平方零。

另固定任意一个实际 $x_0\in I$，指定
$$
\boxed{\mathcal B_j=-\Lambda x_0^j,\qquad 0\le j\le4,}
\tag{17}
$$
其中 $\Lambda>0$ 稍后选为一个充分大的有限数。于是
$$
\mathcal B[Q^2]=-\Lambda Q(S,x_0)^2.
\tag{18}
$$
这只是有限 shape 目标；没有给实际 profiles 添加点质量。

由(9)(15)与 $\mathcal A_3=\mathcal A_4=0$，依次从 $j=2,1,0$ 解出 $\mathcal A_2,\mathcal A_1,\mathcal A_0$。其系数主对角均为 $c_0>0$，而三个完整 $e_j$ 在固定 $C^2$ 邻域内有界。因此
$$
|\mathcal A_0|+|\mathcal A_1|+|\mathcal A_2|\le C_A
\tag{19}
$$
可以取为与 $\Lambda$ 无关的常数。不能用 principal 把 $e_j$ 置零；这里只用其真实统一界。

考虑下一节的紧弧 $-1\le\sigma\le1$。沿该弧，(12)(18)给
$$
\ell_k(S)
=\frac{\Lambda Q(S,x_0)^2}{64h_c^2h^4}
+e_k(S),
\tag{20}
$$
并且
$$
\ell_S(h_\sigma,k_\sigma)
=-\frac{h_\sigma\mathcal A[Q^2]
+\Lambda\cosh\sigma\,Q(S,x_0)^2}{32h_c^2h^4}
+e_{\rm tan}(S).
\tag{21}
$$
由(19)、完整 $C^2$ 余项界和紧弧的 $h>0$，$e_k$ 及(21)中非 $\Lambda$ 部分都有与 $\Lambda$ 无关的界；两个显示 $\Lambda$ 系数的正最小值严格大于零。因此先选一个充分大但有限的 $\Lambda$，再执行第3节的有限正根，便同时得到
$$
\boxed{
\ell_k(S)\ge c_k>0,\qquad
\ell_S(h_\sigma,k_\sigma)\le-c_{\rm tan}<0
\quad(-1\le\sigma\le1).
}
\tag{22}
$$

这两条符号来自同一个实际母库，不是任意指定两条连续函数。本稿不再统一缩放实际 $a_i,b_i$；原二十行中包括 $d_f(P)$ 在内的指定非零数值原样保持。R520 的局部 IFT 只需要速度导数非零，不需要它等于 $1$。因此本次从起点选择固定为
$$
\ell_k(S_c)=g_c>0,\qquad \kappa=\kappa_0>0.
\tag{23}
$$
后面的所有正则性与有限扰动只用 $g_c>0$ 和(22)，没有改变已经冻结的规范或 profile。

## 5. 明确的有限幅真实水平参考弧

取
$$
\boxed{
\begin{aligned}
h_0(\sigma)&=h_c\cosh\sigma,\\
\omega_0(\sigma)&=\omega_c-
\frac{\cosh\sigma\,\arctan(\sinh\sigma)}{h_c},\\
k_0(\sigma)&=-\sinh\sigma-
\cosh^2\sigma\,\arctan(\sinh\sigma).
\end{aligned}}
\tag{24}
$$
它通过 $S_c$。直接微分给
$$
d_0-\omega_ch_0=\sinh\sigma,\qquad
\mathfrak q(S_0)=0,
$$
$$
(k_0)_\sigma=-2\cosh\sigma
\{1+\sinh\sigma\,\arctan(\sinh\sigma)\},
$$
$$
(\omega_0)_\sigma
=-\{1+\sinh\sigma\,\arctan(\sinh\sigma)\}/h_c
=\frac{(k_0)_\sigma}{2h_0}.
\tag{25}
$$
因此(24)是原水平分布中的真实几何弧，不只是状态空间中的任意曲线。

沿它令 $\eta_0=\omega_0-\omega_c$，则
$$
\frac{(k_0)_\sigma}{2}-(h_0)_\sigma\eta_0
=-\cosh\sigma,
\tag{26}
$$
这准确给第4节的(21)。

可在母库初选时取
$$
\omega_c>-\ell+5/h_c.
\tag{27}
$$
因为 $\cosh1\,\arctan(\sinh1)<4$，参考弧及一个固定小邻域都满足共同 $x+\omega>0$。所有 profiles 和右锚不随 $\sigma$ 移动。

这条弧已具有实际需要的有限幅度。它在两侧有相反的曲率符号，且
$$
|k_0(1)|=\sinh1+\cosh^21\,\arctan(\sinh1)>1.
$$
又
$$
\operatorname{osc}_{[-1,1]}\omega_0
=\frac{2\cosh1\,\arctan(\sinh1)}{h_c}
>\frac{2}{h_c\cosh1}.
\tag{28}
$$
例如 $\cosh1>3/2$、$\sinh1>1$、
$\arctan(\sinh1)>\pi/4>3/4$ 已严格给出最后不等式。没有靠浮点样点判号。

(24)还不是 ruling 路径。下一节使用完整八矩和长真实前缀，将它提升成同规范的实际有限幅 ruling 路径。

## 6. 一次固定第三规范与真实长前缀

在第4节母库最终冻结以后，按 R520 选择一次 $\nu$ 与双 collar 紧、相位光滑的 $\chi_\theta$：
$$
2\mathbf w(S_c)\cdot\nu=\mathscr R_c(\pi/2),\qquad
\mathbf I(\phi_\theta,\chi_\theta)=\sin^2\theta\,\nu.
\tag{29}
$$
此后不改变 $\nu,\chi$，始终取 $w_\theta=0$。

由 $\mathfrak q(S_c)=0$，原完整常态路径对任意有限长度都满足全相位 ruling，并有真实历史
$$
m(t)=tM_c,\qquad
T(t)=-t^2A_c^2/2.
\tag{30}
$$
选择一个稍后确定的充分大有限前缀长度 $T_0$。后继区间只重写时间坐标 $s=0$，不重置任何历史：
$$
m(0)=T_0M_c,\qquad T(0)=-T_0^2A_c^2/2.
\tag{31}
$$
尤其
$T(0)+\Phi_{m(0)}^2/2=0$，所以 R482 的真实 $\Theta_0$ 与原初端势完全一致。当前第三类仍是
$\Pi(j^1S)-\Pi(S_c,0,0)-\Phi_m^2/2+W$，不是零第三入值。

需要保入口 frame 时，可以在充分大的 $2\pi$ 整数倍中选 $T_0$；原 $k=0$ frame 旋转确为 $2\pi$ 周期。位置仍有其真实正长度漂移，本文不删除它。

## 7. 参考时钟与完整八矩基线

固定任意一个有限区间 $[0,L]$，取光滑参考时钟
$\sigma(s)\in[-1,1]$，在初段 collar 恒为零，并在区间内先后达到 $-1$ 与 $1$。可以另外让其末段返回零，但这不预付实际末 germ。

把(24)按该时钟参数化，记为 $S_0(s)$。定义其**真实原八矩基线**
$$
\boxed{
B_0'(s)=M_{\rm raw}(S_0(s),h_0'(s),k_0'(s)),
\qquad B_0(0)=0.
}
\tag{32}
$$
这里 $B_0$ 是八维矩阵坐标，算子写为 $\Phi_{B_0}$。没有只取静态密度，也没有去掉速度平方或积分端势。

再定义一个完全确定的平滑实函数
$$
\boxed{
z_0(s)=
-\ell_{S_0(s)}(h_0'(s),k_0'(s))
-2b_{S_0(s)}(A_c,\Phi_{B_0(s)}).
}
\tag{33}
$$
所有函数都已在固定有限时间区间内定义；它们及所需有限阶导数有界。此处只是按完整原式定义参考数据，没有执行求积。

在初段 $\sigma=0$ collar 上，$S_0=S_c$、$B_0=sM_c$；由
$b_{S_c}(A_c,A_c)=0$ 得
$$
z_0=0.
\tag{34}
$$
这一点将保证原常态入 germ 精确接合，而不只是误差趋零。

## 8. 保完整 $m$ 的精确坐标与有限扰动方程

置
$$
\epsilon=T_0^{-1}>0,\qquad
q(s)=\epsilon z_0(s),\qquad
v=d-\omega_ch.
\tag{35}
$$
式(16)可精确解出正高度：
$$
\boxed{
h=H(v,q)
=h_c\sqrt{1+v^2+\frac{4h_c^2q^2}{\kappa^2}}
-\frac{2h_c^2q}{\kappa}.
}
\tag{36}
$$
它对全部实 $(v,q)$ 为正，在本文固定紧域中光滑。再置
$$
\eta=\omega-\omega_c,\qquad
k=h\eta-v .
$$
原水平关系与 $q'=\epsilon z_0'$ 给准确速度
$$
\boxed{
\begin{aligned}
\gamma&=H_vv'+H_q\epsilon z_0',\\
\upsilon&=2\{(\eta H_v-1)v'+\eta H_q\epsilon z_0'\},\\
\omega'&=\frac{\upsilon}{2h}.
\end{aligned}}
\tag{37}
$$
这些不是新自由输入；它们是满足原水平关系和所指定小法向坐标的全部实际速度。

始终写
$$
m=T_0M_c+B,\qquad B(0)=0,\qquad
\boxed{B'=M_{\rm raw}(S,\gamma,\upsilon).}
\tag{38}
$$
把(35)–(38)代入完整(7)，只作真实次数展开：
$$
\boxed{
\epsilon F
=z_0+\ell_S(\gamma,\upsilon)
+2b_S(A_c,\Phi_B)
+\epsilon\,\mathcal H_\nu(S,B,\gamma,\upsilon).
}
\tag{39}
$$
其中
$$
\mathcal H_\nu
=\mathcal R_\nu+\mathcal L_S(\Phi_BD)+q_S(\Phi_B)
$$
是完整光滑余项。$T_0^2q_S(A_c)$ 正好变成 $T_0z_0$；真实 cross 为
$2T_0b_S(A_c,\Phi_B)$，没有被忽略。式(39)不把 $B$ 冻结为参考值，也不把参考八矩当成实际累计。

右侧在 $\epsilon=0$ 光滑延拓。参考解为
$$
v_0(s)=\sinh\sigma(s),\qquad
\omega=\omega_0(s),\qquad B=B_0(s),
$$
且由(33)准确满足延拓后的完整方程。

### 8.1 同一个速度雅可比

在 $q=0$ 参考弧上，
$$
H_v=\frac{h_cv}{\sqrt{1+v^2}},\qquad
\ell_v:=\ell_hH_v+2\ell_k(\eta H_v-1)
=\frac{\ell_S(h_\sigma,k_\sigma)}{\cosh\sigma}.
\tag{40}
$$
由(22)，$\ell_v$ 在整条紧弧上严格负且统一离零。

因此(39)对唯一未知 $v'$ 的导数在 $\epsilon=0$ 正是 $\ell_v$，不是一个未核的端口 minor。

也可把它直接写成原两速度的 $2\times2$ 雅可比。第二个方程是
$$
\mathfrak q'=(\mathfrak q_h+\omega\mathfrak q_d)\gamma
-\frac{\mathfrak q_d}{2}\upsilon=\epsilon z_0'.
$$
参考弧上
$$
\mathfrak q_d=\frac{\kappa H_v}{2h_c^2},\qquad
\mathfrak q_h+\omega\mathfrak q_d
=\frac{\kappa}{2h_c^2}(\eta H_v-1).
$$
故(39)与该方程对 $(\gamma,\upsilon)$ 的极限行列式为
$$
\boxed{
\det
\begin{pmatrix}
\ell_h&\ell_k\\
\mathfrak q_h+\omega\mathfrak q_d&-\mathfrak q_d/2
\end{pmatrix}
=-\frac{\kappa}{4h_c^2}\ell_v\ne0.
}
\tag{41}
$$
原两个方程使用同一 $F$、同一当前状态、同一真实 $B$。没有用另外一个冻结历史系统的雅可比替代它。

### 8.2 统一有限隐函数与实际 ODE

由紧参考图上的(40)，统一 IFT 将(39)准确解成
$$
v'=\mathcal G_\epsilon(s,v,\omega,B).
\tag{42}
$$
其支通过参考速度 $v_0'(s)$。用局部唯一性粘合有限个图册，所有图册在同一个固定紧邻域和同一小 $\epsilon$ 区间内有效。

把(42)代入(37)(38)，得到一条普通光滑有限维 ODE，初值为
$$
v(0)=0,\qquad\omega(0)=\omega_c,\qquad B(0)=0.
\tag{43}
$$
$\epsilon=0$ 时其解正是 $(v_0,\omega_0,B_0)$。普通 ODE 的参数连续依赖及固定紧管道上的 Gronwall 估计给：存在由冻结母、固定时钟和完整基线确定的 $C<\infty,\epsilon_0>0$，使每个
$0<\epsilon<\epsilon_0$ 的真解存在于整个 $[0,L]$，并且
$$
\boxed{
\|(v_\epsilon,\omega_\epsilon,B_\epsilon)
-(v_0,\omega_0,B_0)\|_{C^1[0,L]}
\le C\epsilon .
}
\tag{44}
$$
若需要有限更高阶 jets，同一平滑 ODE 给对应有限阶连续依赖；本稿不把该估计用作周期返回方程的逆。

由(34)、原常态解和局部唯一性，实际解在整个初 collar 精确等于
$$
S=S_c,\qquad B=sM_c .
\tag{45}
$$
所以它与真实长度 $T_0$ 前缀的所有 scalar/germ jets 完全相合，第三历史继承(31)，不是只在极限中接合。

这里先固定母与规范，再固定参考时钟和全部真实基线，最后只选一个充分大的**有限** $T_0$。没有不断重选母形或串接无限多个局部近似。

## 9. 原 $k_s$ 反馈保持统一正则，实际幅度确实跨过局部门

由(7)(38)，在实际有限解上
$$
\partial_\upsilon F
=T_0\ell_k(S)+O(1).
\tag{46}
$$
余项来自完整 $\mathcal R_\nu$、$\mathcal L(\Phi_BD)$ 及有限状态速度；由(44)在同一固定紧管道上一致有界。平方项 $q_S(\Phi_m)$ 不含速度。

(22)与连续性因此给，在充分大有限 $T_0$ 下，
$$
\boxed{\partial_\upsilon F\ge \frac12c_kT_0>0
\quad\text{在整个实际非恒区间上}.}
\tag{47}
$$
所以本文构造沿途仍位于 R520 原来的 $k_s$ 隐函数反馈类型中；没有在中途遇到一个未支付的速度折点再换规范。实际 $h_s$ 是(37)给出的同一个允许控制。

选择 $\epsilon$ 更小，(28)(44)的严格间隔使实际路径满足
$$
\max k_\epsilon>1,\qquad \min k_\epsilon<-1,
$$
$$
\boxed{
\operatorname{osc}_{[0,L]}\omega_\epsilon
>\frac{2}{\max_{[0,L]}h_\epsilon}.
}
\tag{48}
$$
路径还保持 $h>0$、共同 $x+\omega>0$ 和原完整 collars。

由(39)(42)，实际 $F$ 字面为零；由同一个 R520 角向纤维，
$$
\boxed{
\mathscr K(s,\theta)=0
\quad\text{对整个真实前缀及有限幅后继区间的全部 }s,\theta.
}
\tag{49}
$$
二、三阶 ruling 与同锚恢复仍用原母库的实际八副本和全部 $W$ outer 身份。原 frame、位置及完整第三、第四数据按 R56/R73 在这条实际路径上同步恢复。

## 10. 已完成的连接及尚未完成的返回

本文实际完成的是：同一个有限初选母库与同一个固定 $\chi$，先走任意足够长的真实常态前缀，再走一条统一正则的、曲率和 $\omega$ 均有明确有限幅度的全相位 ruling 路径。全部八矩在同一 ODE 中演化；前缀的巨大非零第二、第三入值被准确保留，并没有把它们吸收到一个未写出的常数里。

这比仅有 R520 的一个局部邻域多付了一个具体非局部控制域。式(48)说明 R524 的小幅刚性不禁止该种真实延拓。它不说明零矩条件已经满足。

末累计恰为
$$
m_{\rm end}=T_0M_c+B_\epsilon(L),
\tag{50}
$$
而不是零；完整 $T_{\rm end},V_{\rm end}$、末 frame 和位置也全部保其真实输出。参考时钟即便返回 $\sigma=0$，(44)也只给实际 scalar 近返，不给准确常态末 germ；R524 的两条原二次型返回门仍须真实支付。当前构造尤其没有使用 R518 的无内部 ruling 限制桥去关闭这些差。

同一完整十三行、period、所有保护芽和空间闭合尚未由本文给出，主 README 的完整连续等距族、嵌入、reach 与幅度条件亦不在本稿完成范围内。

本稿的新增实质是一个有限、统一、保真 history 的正向过程：三十个实际 profile 目标使一个明确有限幅水平弧上的原速度图册统一正则；一次长常态前缀与一个普通有限 ODE 扰动把该弧提升为实际全相位 ruling 路径。后续返回必须从(50)及同一规范继续，不能再从零历史重新开始。

### 原来源与纸面核读范围

- R56/R73：原水平关系、全部八矩、frame/位置与第三累计；
- R221/R482：完整三槽式、变化-profile chain、真实初端商势与(7)的次数分组；
- R520：一般 pure self 的完整 $C^2$ 纤维、原二十行、正根、常态第三 Gram 与原速度导数；
- R455/R447：同一共同 cap 图册、四正常、有限限制最大 minor、原十二正核和有号集中；
- R524：本文真正跨过的是 $|k|>1$ 与较弱的 $2/h_{\max}$ 振幅门，不是全部能量必要界，更不是已经完成零矩返回。

全部新增数学均为纸面原式证明；没有科学程序、数值积分、rank 或旧观察重算。

