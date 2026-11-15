# R726 — 低 ell 的固定三 charge 乘子、完整首强迫与同预算单位块之外的指定类

日期：2026-11-15。**状态：已证明。**

本篇将原极端 carry 的指定目标推广到所有 $1\le\ell\le3$ 的实际立方窗。
在同一个因子化基准上，三个固定乘子分别支付一、二、三份 $t$；
它们保全部十九角，而 charge 成本均为三。
选取其中准确的一项后，原第三短块整段消失。
第二块保完整 $V_1$ 高尾及原常数 $\xi_0$，其最低项仍为单位。

在显示的原长度门下，这个**指定的**乘后首强迫不在 R722 的同预算饱和切向单位块中。
这不是整个原像中的非零结论：截源的两条实际剩余列、其余全部 $\mathcal W_D$ 列、
同一个 $R$、两条十三行 carry 和第三精度都继续保留。
特别，以下乘子不被当作整可逆目标变换，也没有给任何乘子来源附加中央零。

## 1. 原对象、实际整基准和符号

完整保 R502、R697、R701 的同一对象：
$$
p=6s-1>101,\qquad
1\le\ell\le r<h,\qquad
k=2h+r-s,\qquad 0\le k<\ell,
\tag{1}
$$
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,\qquad
\overline{P^{\rm fact}}\in\ker\bar J,\qquad
d=1+8t,\quad h_7=7+4t+16t^2.
\tag{2}
$$
这里 $F=\sum_{i=0}^bf_i(t)Y^i$ 是同一个整因子，$b=\deg_YF$，不是固定椭圆曲线参数 $17$；
$Q$ 是同一个多项式余因子，$Q(P)$ 为单位。
因子曲线 $C\subset X$、原光滑点 $P=(0,1)$、
$\kappa=C^2\ge0$、$\chi=-K_XC$ 以及全部十九角格 $\mathcal H_j$ 均不改变。

记
$$
\mathcal E=Y\partial_Y,\quad\delta=t\partial_t,\quad
e=\mathcal EF,\quad a_0=\delta F,\quad
\mathcal V_F=e\delta-a_0\mathcal E .
\tag{3}
$$
沿 $C$ 读 $e,f_2=\mathcal E^2F$ 时省略限制符号；$e(P)$ 是单位。
令 $\widetilde\psi$ 是所选整 $F$ 的实际 Hensel 分支，保持
$$
\eta=\log(g/\widetilde\psi)=t^hu+p\xi,\qquad
u(0)\in\mathcal O^\times,\qquad \xi\in\mathcal O[t]_{<h}.
\tag{4}
$$
特别保原 $\xi_0=-\log\widetilde\psi(0)/p$，
不通过改变 $F$ 免费将它设成零。
令 $a=p\kappa_{\rm Gauss}\in\mathcal O^\times$ 为原 Gaussian 单位，
$$
b_s(t)=\left(\frac{t}{w(t)}\right)^s,\qquad t^s=p\epsilon b_s(t).
\tag{5}
$$
后文所有模 $p$ 的 $a,b_s,u,\xi$ 均读自这些同一实际量。

使用 R697/R701 的固定角最高系数假设：
$f_b$ 在特征零的同一整提升中为 $t,t-1,d,h_7$ 的根处的幂乘单位，
无新增自由零点；并保 $f_D<p$、$b<p$ 及原允许分母。
若在非分歧扩张中拆开 $h_7$，所有构造均保下降。
置
$$
\mathcal P=6(1-t)\delta^2-(1+2t)\delta,\qquad
\mathcal R=\frac{t(154+160t+1792t^2)}{3d^2},
$$
$$
c_F=b^2\{b\mathcal R+\mathcal P\log f_b\},\qquad
K_F^{[3]}=K_F-c_FF^3,
\tag{6}
$$
其中
$$
K_F=e^3\mathcal R+6(1-t)e^2\delta^2F
-12(1-t)e a_0\mathcal E\delta F
+6(1-t)a_0^2\mathcal E^2F-(1+2t)e^2a_0.
\tag{7}
$$
$\mathcal P\log f_b$ 只表示 R701 的准确有理函数，不调用正特征完整 log。

## 2. 三个乘子的五角值和完整返回

为避免与 $d=1+8t$ 混淆，用 $j_0$ 标记新增 $t$ 的份数。对
$$
1\le j_0\le3
$$
定义
$$
\boxed{
\mathfrak m_{(j_0)}
=Y^3t^{j_0}(t-1)^2h_7^3d,\qquad
\mu_{(j_0)}=\mathfrak m_{(j_0)}c_F.
}
\tag{8}
$$
五类原 Gauss 值按 $0,h_7,1,d,\infty$ 排列，
其中 $h_7$ 的两个根分别使用相同一列：

| 因子或相对损失 | $0$ | $h_7$ 的每个根 | $1$ | $d=0$ | $\infty$ |
|---|---:|---:|---:|---:|---:|
| $\mathfrak m_{(j_0)}$ | $4j_0-3$ | $9$ | $3$ | $5$ | $9-2j_0$ |
| $c_F$ 下界 | $0$ | $-8$ | $-3$ | $-4$ | $-2$ |
| $v(K_F)-3v(F)$ 下界 | $0$ | $-8$ | $-3$ | $-4$ | $-2$ |
| 两种完整乘后增益下界 | $4j_0-3$ | $1$ | $0$ | $1$ | $7-2j_0$ |

最后一行对 $j_0=1,2,3$ 全部非负。
这是逐角计算：额外 $t^{j_0-1}$ 只将 $0$ 角提高 $4(j_0-1)$，
将无穷远降低 $2(j_0-1)$，其他有限角不变。
没有以乘子自身的帽替代完整 $K_F$ 的帽。

**定理 1。** 对每个 $N\ge0$，准确整包含
$$
\boxed{\mu_{(j_0)}\mathcal W_N\subset\mathcal W_{N+3}.}
\tag{9}
$$
令
$$
D_0=3b+\deg_YQ,\qquad
h_+=b-\max\{i<b:f_i\ne0\}.
$$
则同一实际来源满足
$$
\boxed{
\begin{aligned}
B_{(j_0)}^{\rm old}
&=d^{-C_D}t^rQ\,\mathfrak m_{(j_0)}K_F
\in\mathcal W_{D_0+3},\\
B_{(j_0)}^{[3]}
&=d^{-C_D}t^rQ\,\mathfrak m_{(j_0)}K_F^{[3]}
\in\mathcal W_{D_0+3-h_+},\\
B_{(j_0)}^{[3]}
&=B_{(j_0)}^{\rm old}-\mu_{(j_0)}P^{\rm fact}.
\end{aligned}}
\tag{10}
$$
因此 $D_0+3-h_+\le D$ 时，第二行是真正同一预算返回。
对一般后续修正 $R$，仍须支付 (9) 的三个 charge；
不能由 (10) 免费宣布 $\mu_{(j_0)}R\in\mathcal W_D$。

**证明。** R701 的双向 Gauss 判据为原六个实际值下界
$(-2,-2,-2,-1,0,-8)$，并加实际 $Y$ 次数上界。
表中非负增益保这些界，允许的 $d$ 分母也由同一 $d$ 角支付。
这等价于原逐 charge 的 $q_n\mathcal O[t]_{\le e_{n+1}}$ 帽，
因而保其全部十九个中间角，不是只进入较大的矩形空间。
$K_F^{[3]}$ 的最高项消去给
$\deg_YK_F^{[3]}\le3b-h_+$；
其各角值由两个已保界的项相减仍成立。
乘回同一个 $Q,d^{-C_D},t^r$，即得 (9)–(10)。证毕。

以下使用准确的原点门
$$
\boxed{c_F(0)\in\mathcal O^\times.}
\tag{11}
$$
若 $a_0^*=\operatorname{ord}_t f_b$，则
$$
c_F(0)=-b^2a_0^*.
\tag{12}
$$
所以 $1\le a_0^*<p$ 已足够。
一个来自原低角的可用充分条件是
$b>\lfloor(4r+2)/3\rfloor$：若 $f_b(0)$ 为单位，
则原 $0$ 角迫 $-b\ge v_0(F)\ge-(4r+2)/3$，矛盾。
原最高 charge 系数的实际次数帽还给
$3\deg f_b\le f_D+C_D-r$；
结合 $f_D<p$、$C_D=\lfloor D/2\rfloor$、$D<2p/9$，
得到 $\deg f_b<p$。故此充分条件确实推出 (11)。
不满足它时应直接核 (11)，不能把 $c_F(0)$ 的零误作单位。

## 3. 准确选择 j0 后，原第三块消失

现在只要求
$$
\boxed{j_0=\ell-k\le3.}
\tag{13}
$$
这覆盖所有 $\ell\le3$，也覆盖较大 $\ell$ 中满足 (13) 的对应 carry。
令
$$
v_{j_0}=\overline{\mu_{(j_0),\rm phys}\,J(P^{\rm fact})/p}.
\tag{14}
$$
这是对同一个 $J(P^{\rm fact})/p$ 施加指定的非单位乘法。
未将 $\mu_{(j_0)}$ 视为整可逆，也未改变同一首次修正 $R$。

R502 的整个原首 Bockstein 为
$$
\begin{aligned}
\beta_J(P^{\rm fact})={}&
\epsilon V_0(b_st^{h+k}u^3+6at^{r+h}u\xi)
+3a\epsilon^2V_0b_st^ku^2\\
&+\epsilon V_1b_st^{2h+k}u^4,
\end{aligned}
\tag{15}
$$
其中
$$
V_0=(d^{-C_D}Q)|_C e^3,\quad
V_1=d^{-C_D}\left((\mathcal EQ)e^3+\frac32Qe^2f_2\right)\Big|_C.
\tag{16}
$$
整个 raw $\bar\Gamma$ 中 $\zeta^3$ 未被删除。

$\mu_{(j_0)}$ 含 $t^{j_0}$，其余因子在原点为单位。
因此 (15) 的原第三块从
$t^{k+j_0}\epsilon^2=t^\ell\epsilon^2$ 起，准确为零。
乘子的一次 Gaussian 项作用在第二块产生的第三块，
最小 $t$ 阶为 $h+k+j_0=h+\ell\ge\ell$，也准确为零。
第一块保持零；第二块最低阶是 $h+\ell>r$。
所以乘后目标的原低行全零，这一步不需要另取低行右逆。

这一消去只在 (15) 的**完整**目标上进行。
不能先减掉旧低行修正，再假定其乘后仍免费返回旧来源。

## 4. 两个原切向规范中的完整高尾

使用 R722 的同一切向返回
$$
\mathcal T_j(H)=d^{-C_D}t^{r+1}Q\,
m_{{\rm tan},j}\,\mathcal V_FH,\qquad j=2,3,
\tag{17}
$$
其中
$$
m_{{\rm tan},2}=Y^2(t-1)^2h_7^2,\qquad
m_{{\rm tan},3}=Y^3(t-1)^2h_7^3d^2.
$$
对相对 $J$ 和完整原 $M$，分别取准确长度
$$
\boxed{
T=T_J=s-r-1=2h-k-1,\quad\text{或}\quad
T=T_M=s-r-14=2h-k-14.
}
\tag{18}
$$
后者按 R543 保完整 $c_*U_0w^{13}$，
没有非整地反演 $w^{13}$，两条十三行及十三自由行不变。

把 $\mu_{(j_0)}=t^{j_0}m_\mu$，则
$$
m_\mu=Y^3(t-1)^2h_7^3d\,c_F.
$$
定义实际两个单位
$$
M_2=m_\mu/m_{{\rm tan},2}=Yh_7d\,c_F,\qquad
M_3=m_\mu/m_{{\rm tan},3}=c_F/d,
$$
$$
\chi_j=M_j|_C,\qquad
\gamma_2=1,\quad\gamma_3=0.
\tag{19}
$$
它们满足 $\mathcal EM_j=\gamma_jM_j$；
$\chi_j(0)$ 由 (11) 为单位。
最后置
$$
\boxed{\nu=h+\ell-r-1.}
\tag{20}
$$
由 (1) 有 $1\le\nu<h$。

**定理 2（完整指定高块）。** 在 (17) 的同一真实前缀规范下，
(14) 的前两块准确为
$$
\boxed{
(v_{j_0})_{\rm tan}
=\epsilon\chi_j\left[
b_se^3u^3t^\nu
+6ae^3u\xi\,t^{h+j_0-1}
+b_su^4\left(\frac32e^2f_2+\gamma_je^3\right)t^{\nu+h}
\right]\pmod{t^T}.
}
\tag{21}
$$
其值块为零。$b_s,\chi_j,e,u,\xi,f_2$ 均保整条所需低窗，
不只保常数项。
特别，$V_1$ 所留下的 $f_2$ 以及实际 normal 单位的 $\gamma_j$ 项，
只有在 $\nu+h\ge T$ 时才能删去。

**证明。** R502 的完整 $Q$ 单位运输给乘前第二高块
$$
\epsilon\left[
b_se^3u^3t^{h+k-r}
+6ae^3u\xi t^h
+\frac32b_se^2f_2u^4t^{2h+k-r}
\right].
\tag{22}
$$
这里的 $(\mathcal EQ)e^3$ 已由同一个 $Q_{\rm phys}^{-1}$ 真实相消；
这是完整 (15) 的结果，不是令 $V_1=0$。

从 (22) 再乘 $t^{j_0-1}M_j(t,\psi e^{\eta_0})$，
其中 $\eta_0=t^hu$。因为 $T\le2h-1$，
$$
M_j(t,\psi e^{\eta_0})=\chi_j(1+\gamma_j\eta_0)\pmod{t^T}.
$$
首项的新增 normal 项准确从 $t^{\nu+h}$ 起。
$\xi$ 项的新增 normal 项从 $t^{2h+j_0-1}$ 起，至少为 $2h$，故消失；
$f_2$ 项的再下一项从 $t^{\nu+2h}$ 起，也消失。
利用 $j_0+k=\ell$ 得到 (21)。
(18) 的 $M$ 情形先保整 carrier 再作相同已知前缀规范，因此同式在其实际较短长度成立。证毕。

由于
$$
h+j_0-1-\nu=r-k\ge1,\qquad \nu+h>\nu,
$$
(21) 可以准确写成
$$
\boxed{
(v_{j_0})_{\rm tan}=\epsilon t^\nu v_*(t),\qquad
v_*(0)=\chi_j(0)b_s(0)e(P)^3u(0)^3\in k^\times.
}
\tag{23}
$$
原 $\xi_0$ 只在更高阶出现，未被人为改动。

例如两种实际长度保留 $V_1$ 的准确可能窗口分别为
$$
r>\ell+k\quad(J),\qquad r>\ell+k+13\quad(M).
\tag{24}
$$
这是 $\nu+h<T$ 的等价式；(24) 之外该项才落在截止之后。
即使 (24) 成立，下面证明也继续使用完整 (21)。

## 5. 指定类退出同一预算的饱和单位块

使用 R722 及其“原同 D 截源”增补，令
$$
\mathcal H_{\rm cut}=\{H\in\mathcal H_2:\deg_YH\le2b-j\},
$$
$$
\mathcal H_{\rm cut}^{00}
=\{H\in\mathcal H_{\rm cut}:
H(\widetilde P)=(\mathcal EH)(\widetilde P)=0\}.
\tag{25}
$$
保同一实际低 charge 截面条件
$b\ge i_0+j$，其中 $i_0=\min\{i:\bar f_i(0)\ne0\}$。
它保证这两个原点条件有原整截面，
而 $\mathcal T_j(\mathcal H_{\rm cut})\subset\mathcal W_{D_0}\subset\mathcal W_D$。
同时保 R537 用于来源核的 $p>8b^2+4bu_{\rm cap}$；
这里 $u_{\rm cap}=\max_i(\deg f_i-4i)$，与 (4) 的接触单位不同。

假设准确长度门
$$
\boxed{\kappa<\nu<T,\qquad T>2\kappa.}
\tag{26}
$$
由 $\nu<h$，这同时给 R722 所需 $h>\kappa$。
于是 (25) 的完整原 $J$ 或 $M$ 像是整饱和单位块。

**定理 3。** 在 (26) 下，指定目标 (14) 不在
$$
\overline{\mathsf M_0\mathcal T_j}
(\overline{\mathcal H}_{\rm cut}^{00}),
\qquad \mathsf M_0=J\ \text{或完整原 }M
\tag{27}
$$
中。这里 $M$ 的目标是 (14) 经完整原 carrier 运输后的目标，
始终使用 (18) 的相应长度。
因此它在此同预算单位块的整商约化中非零。

**证明。** 假设同一个 $H\in\overline{\mathcal H}_{\rm cut}^{00}$
达到 (23)。令 $G=\mathcal V_FH$，$G_i=(\mathcal E^iG)|_C$。
因为 $\eta_0^2=0\bmod t^T$，完整两块条件是
$$
G_0+\eta_0G_1=0,\qquad
a(G_1+\eta_0G_2)=t^\nu v_*(t)\pmod{t^T}.
\tag{28}
$$
置 $H_*=\min(T,h)$。由 (26)、$\nu<h$ 得 $H_*>\nu$；
第二式模 $t^{H_*}$ 迫 $G_1$ 的首项准确在 $\nu$，且首系数非零。
所以第一式给
$$
\operatorname{ord}_P G_0\ge N_*:=\min(T,h+\nu)>2\kappa.
\tag{29}
$$
注意 (29) 不要求 $G_0$ 消到整个 $T$；
当 (24) 成立时，较短的准确界仍已足够。

沿 $C$，
$$
G_0=e\,t\frac d{dt}(H|_C).
$$
因为 $N_*\le T<p$、$H(P)=0$，
得到 $H|_C=0\bmod t^{N_*}$。
该真实限制截面位于次数 $2\kappa$ 的原线束中；
由 $N_*>2\kappa$，必须 $H|_C=0$。
原限制正合列于是给同一个 $H=FH_1$，$H_1\in\overline{\mathcal H}_1$。
再用 $(\mathcal EH)(P)=0$ 和 $e(P)$ 单位，得 $H_1(P)=0$。

$\mathcal V_FF=0$ 继续给
$$
G_1=e^2t\frac d{dt}(H_1|_C).
$$
由 (28) 的第二式模 $t^{H_*}$，
其首项准确在 $\nu$。
$0<\nu<H_*<p$，故所有读到的 Euler 正次数为单位，
于是
$$
\operatorname{ord}_P(H_1|_C)=\nu>\kappa.
$$
而 $H_1|_C$ 是次数 $\kappa$ 的原线束截面，
且所读首系数非零，矛盾。证毕。

这一证明同样适用于未截源的
$\mathcal H_2^{00}/\mathcal OF^2$，
但那时必须另保其实际扩大 $D+2$ 或 $D+3$ 的成本。
(25) 的版本已经在旧预算内。

在原低 $r,\ell$ 满主阶临界范围，
$h=141b^2/32+O(b)$、$\kappa=47b^2/12+O(b)$、
$\nu=h+O(b)$、$T=141b^2/16+O(b)$。
所以 (26) 对充分大 $b$ 严格成立。
这只对已存在且满足全部原因子、角帽和返回条件的实际候选应用；
没有据这些主阶式构造或假定原首核。

## 6. 剩余两列、原首核及同一个 R 的第三精度

R722 同预算增补给原点截面
$$
U=\frac{f_{i_0}(t)Y^{i_0}}
{f_{i_0}(0)\widetilde\psi(0)^{i_0}},
\qquad
H^{(1)}=FU,\quad
H^{(0)}=U^2-\frac{2i_0}{e_0}FU.
\tag{30}
$$
同一个单位块商中仍准确留下
$$
c_i=\pi_{\rm u}\mathsf M_0\mathcal T_j(H^{(i)}),\qquad i=0,1.
\tag{31}
$$
由定理3，指定 $\bar v$ 的商类非零；
整个截源吸收它的条件准确是
$$
\boxed{
[\bar v]\in k\bar c_0+k\bar c_1
\quad\text{于同一个 }\overline{\mathscr Q}_{\rm u}.
}
\tag{32}
$$
没有以两列的数量预判 (32)，也没有把
$\mathscr Q_{\rm u}$ 说成二维目标。

$Z=0$ 时，原来源关系 $1,F$ 使两列整地属于单位块，
因此定理3排除整个这个切向截源。
$Z>0$ 时，截源的来源核已被截掉；
它的任何额外物理核都产生一个实际 $t^{r+1}$ 阶的原首核。
故 R722 增补的准确限制继续为
$$
\dim_k\ker\overline{\mathsf M}_0
\ge1+\dim_k\ker(k^2\xrightarrow{(\bar c_0,\bar c_1)}
\overline{\mathscr Q}_{\rm u}).
\tag{33}
$$
右侧的一来自公共 $t$ 阶恰为 $r$ 的同一个 $\bar P^{\rm fact}$；
不能混同 $J$ 和 $M$ 的核。
若原首核确已证明只有这一个方向，(31) 模 $p$ 满两列秩，
但这本身仍不判断非零目标是否在两列张成中。

最后，原 $\mathcal W_D$ 还有全部其它真实来源。
它们必须同 (31)、指定 (21) 一起进入**同一个**整商。
对 $P_2=P^{\rm fact}+pR$，准确关系仍是
$$
B_{(j_0)}^{[3]}-p\mu_{(j_0)}R
=B_{(j_0)}^{\rm old}-\mu_{(j_0)}P_2.
\tag{34}
$$
三个顶 charge 的实际 cap、非单位 $t^{j_0}$ 成本均保留。
(34) 没有赋予另一个可独立选择的 $R$。

单位块的消元是真正整基变换，故可以保模 $p^3$；
但必须同时运输全目标、(31)、其它原列及 (34) 的同一修正。
原 $P_{134}/U_0$、$U_1/p$、两条十三行 carry、
原低行高尾和 $d_2/G_2$ 的下一位均未删除。
本篇只证明指定类退出明确的同预算单位子像；
全原像的归属、原三条完整中央零与这一类的联立仍待解决。

依赖：[R502](R502-full-low-ell-bockstein-and-actual-geometric-residue.md)；
[R543](R543-actual-tangent-jet-kernel-small-remainders-and-unit-smith-block.md)；
[R697](R697-full-third-normal-top-reduction-and-same-correction-cap.md)；
[R701](R701-sharp-two-charge-clearing-and-complete-same-correction-cap.md)；
[R722](R722-actual-tangent-two-constant-kernel-and-specified-residual-columns.md)；
[R722 同预算增补](../notes/2026-11-15-r722-original-budget-truncated-tangent-unit-block.md)。
