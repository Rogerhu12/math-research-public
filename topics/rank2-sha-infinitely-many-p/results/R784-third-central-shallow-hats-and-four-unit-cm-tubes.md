# R784 — 第三中央在 E 浅共同帽与实际四单位 CM 管族中的完整联立

日期：2026-11-15。**状态：下列完整来源恒等式、真实切集、单轴返回和全部补域已证明。**

本篇接 R780 的更正：共同帽附 W 深条件时处于物理 E-unit，不能从第三中央的 E 深行相减。这里使用同一原 U136 的完整 CM 投影，把 E 浅来源中的整个 Xi 参考和外谱准确消去。所得是一条含 216 个真实分支的第三中央关系。

在共同帽上，恒等分支是原 B 第一态的 W 近相消部分；其余分支在删去显示的固定有限坏素数后，落在原 P、t、W、Vt 四个单位条件内。各分支的 canonical CM 来源、归一逆 Y 观察和补域全部保留。它们不是 216 个独立中央零，也不把这些来源改成 R777 的裸 B0。R785 新的 Z0 偶深核允许只返回这一条帽轴，保持原 q 和其它伙伴。

## 1. 同一来源、原测试与 E 浅的纯 U 投影

保 R734 的最终 $q=q_N^*$、$N\in4\mathbf Z_{>0}$、原 $b=17$ 和周期 $\Omega$。记
$$
\lambda=-\bar\pi_0^{-1},\qquad\beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad d_p=p-1,\qquad
c_B=1-\omega^2.
\tag{1}
$$
R780 的两态是
$$
B_0=\frac{e_0-\omega(e_1+e_2)}{c_B},\qquad
B_1=K_WB_0.
\tag{2}
$$
原 C 六角平均在全部来源中统一保留。本文的 U 是 R780(1)—(3) 所固定的 U136/E2312 来源，物理 first-Y 的实际尺度为 $[1/2]_*\nu_U$。

用 R785 的原正交坐标
$$
Y,\quad Z_0=P-b_YY,\quad t,\qquad
b_Y=\frac{20+3\omega}{17},\qquad a=1+3\omega,
$$
$$
P=b_YY+Z_0,\qquad W=P-at,\qquad
V_t=\bar aP+29t,\qquad \alpha_W=17-3\omega.
\tag{3}
$$
三条真实伙伴 C、H1、J 均垂直于 Y、Z0、t；原 q 只依这三条伙伴。
物理 E 准确为
$$
E=e_ZZ_0+h_0t+e_JJ,\qquad
e_Z=-\frac{17(25+48\omega)}{144},\quad
h_0=17+3\omega,\quad e_J=-\frac{1841}{72}.
\tag{4}
$$
因此 E 同时正交于 Y 和 W，但并不正交于 Z0 或 t。
令
$$
\mathcal E_N=\{E\in p^N\},\qquad
f_w(y)=1_{y\in\mathcal O^\times}\langle y\rangle^{d_pw}.
$$

以 $\mathcal P_U$ 表示 R483/R695 的原第一 $2Y$ 算术投影。R780 的完整 E 深表和未附 E 门的原 $\pi_4$ 返回，分别给
$$
Y_*\mathcal P_U(1_{\mathcal E_N}qB_1)
 =\frac{\lambda^{2N}}{c_B}[1/2]_*\nu_U,\qquad
Y_*\mathcal P_U(qB_1)
 =\frac{52\beta^N}{3c_B}[1/2]_*\nu_U.
\tag{5}
$$
这里 $\mathcal P_U B_0=0$；原 h 部分在该投影中整条为零。
由于 q 和 E 独立于第一 Y 轴，乘这些完整伙伴测试与该投影相容。
准确相减得到
$$
\boxed{
Y_*\mathcal P_U(1_{\mathcal E_N^c}qB_1)
 =c_N[1/2]_*\nu_U,\qquad
c_N=\frac{(52/3)\beta^N-\lambda^{2N}}{c_B}.}
\tag{6}
$$
这一步消去的是原 Xi 中实际不属于 U 的全部谱；没有把它们各自赋零。
$N\in4\mathbf Z$ 时，$\beta^N=\lambda^N$。在任一复嵌入下
$|\lambda^N|=p^{-N/2}<1$，故 $52/3-\lambda^N\ne0$，所以
$$
c_N\ne0
\quad\text{对全部当前 }p,\ N\in4\mathbf Z_{>0}.
\tag{7}
$$
这里不要求 $c_N$ 为 p-adic 单位。

(6) 的完整单位 Mellin 行为
$$
\int_{\mathcal E_N^c}f_w(Y)q\,d\mathcal P_U B_1
=c_N\langle2\rangle^{-d_pw}J_U(w).
\tag{8}
$$
$J_U(0)=0$ 是原来源的已付单位质量，故 (8) 的中央导数等于
$c_NJ_U'(0)$。若采用另一个尺度，必须重加相应的质量项。

## 2. 完整 canonical 分支及其 W 共轭

下列分支始终用 R695 的 raw 平移规范，不把其 $s$ 改成只保生成变量的 $\zeta/\alpha$。置
$$
\alpha_{j,k}=(4+\omega)^j(5+2\omega)^k,\qquad
0\le j\le17,\quad k\in\{0,1\},\quad\zeta\in\mu_6,
$$
$$
s=s_{j,k,\zeta}=\zeta\frac{\bar\alpha_{j,k}}{\alpha_{j,k}},
\qquad
a_{j,k,\zeta}=\frac{\omega^{2j}(-\omega)^k}{216}.
\tag{9}
$$
保原第一 $2Y$、degree136 的 canonical lift，定义
$$
\mathcal Q_\alpha F
=\sum_{\tau\in E[\alpha]}
  \mathsf T^{136}_{\bar\alpha\tau,\,2Y}F,
\qquad
D_s:(Y,Y^\perp)\longmapsto(sY,Y^\perp),
$$
$$
\sigma_{s,i}
=\alpha^{-1}(D_s)_*\nu_{\mathcal Q_\alpha B_i}.
\tag{10}
$$
在 (10) 中 $\alpha$ 由 s 唯一确定。所有 torsion 纤维、canonical 中心、半相位和因子 $1/\alpha$ 均保留。于是
$$
\mathcal P_U B_i=\sum_s a_s\sigma_{s,i}.
\tag{11}
$$
216 个 s 在 K 中互异，唯一的 $s=1$ 是 $j=k=0,\zeta=1$。
其来源为 $\sigma_{1,i}=B_i$，系数为 $1/216$。

R487/R695 原固定高 13、19 条件已支付这些完整平移来源与 W 核的相容性。对整数 $m\ge0$ 置
$$
M_{s,m}=D_sP_{W,\kappa^m}D_s^{-1},\qquad
W_s=W\circ D_s^{-1}=b_Ys^{-1}Y+Z_0-at.
\tag{12}
$$
原 q 和 E 均被 $M_{s,m}$ 固定。完整来源返回是
$$
\boxed{
(q\sigma_{s,0})|_{\{W_s\in p^m\}}
=\lambda^m(M_{s,m})_*(q\sigma_{s,m\bmod2}).}
\tag{13}
$$
实际 inverse-Y 观察为
$$
\boxed{
Y_{s}^{[-m]}=Y\circ M_{s,m}^{-1}
 =Y+\frac{s\alpha_W}{36}(\kappa^{-m}-1)W_s.}
\tag{14}
$$
它只在 $W_s\in p^m$ 的整像上使用，因而是整观察；其 unit 条件仍须完整保留。

以下固定 m 为正奇数。将 (13) 带上 E 浅门，按 (11) 完整求和，(8) 给
$$
\boxed{
\begin{aligned}
\mathscr U_{N,m}(w)
&=\sum_s a_s\!
  \int_{\mathcal E_N^c,\ W_s\in p^m}
       f_w(Y_s^{[-m]})q\,d\sigma_{s,0}\\
&=\lambda^m c_N\langle2\rangle^{-d_pw}J_U(w).
\end{aligned}}
\tag{15}
$$
这是投影之前每个真实域都已运输的等式。它没有把 $\mathcal P_U$ 穿过原未改变的 W 深条件。
偶 m 的同一完整和为零，因为返回态为 B0 且 $\mathcal P_U B_0=0$；本文不从这个整和给任何单项添零。

## 3. 同一帽上的所有分支均属 E-unit

保 R773/R783/R785 的实际共同帽：
$$
\mathcal H_{N,n}
=\{Y\ {\rm unit},\ J,Z_0\in p^N,\
                         U_{\rm f}=u_JJ+u_ZZ_0\notin p^n\},
$$
$$
u_J=\frac{7(4+9\omega)}{72},\qquad
u_Z=-\frac{68+33\omega}{144},\qquad n>N.
\tag{16}
$$
它与 $\{\hat s,\hat d\in p^N,\ \hat s/2-3\hat d\notin p^n\}$ 是同一个整域。
R773 的选择 $n=N+300$ 包含在本篇中。
它只给 E 的 Y/t 正交部分深 N，不给物理 E 深。

对每个 s 及 $m\ge1$，在 $\mathcal H_{N,n}\cap\{W_s\in p^m\}$ 上，
$$
P\equiv b_YY,\qquad
t\equiv \frac{b_Ys^{-1}}aY\pmod p.
\tag{17}
$$
所以 P、t 都为单位；由 (4) 和 $J,Z_0\in p^N$，
$$
E\equiv h_0t\pmod p
$$
也为单位。因而全部 216 个帽管都准确位于 (15) 所用 E 浅域。

更精确地，
$$
W\equiv b_Y(1-s^{-1})Y,\qquad
V_t\equiv\frac{b_Y}{a}(7+29s^{-1})Y\pmod p.
\tag{18}
$$
沿 R695 已删的固定 s 差坏集，有 $s\ne1\Rightarrow s-1$ 为单位。
再删去所有固定非零代数数 $7s+29$ 分子范数的素因子。
它们确实非零：$|s|=1$，而 $|-29/7|>1$。
这是只依固定 CM 投影的有限坏集，独立于 p、N、n、m 的变动，不添加新 CRT 条件。

于是
$$
\boxed{
\begin{array}{ll}
s=1:&
\mathcal H_{N,n}\cap\{W\in p^m\}
 \subset\{E,P,t,V_t\ {\rm unit},\,W\in p^m\},\\[1mm]
s\ne1:&
\mathcal H_{N,n}\cap\{W_s\in p^m\}
 \subset\{E,P,t,W,V_t\ {\rm unit}\}.
\end{array}}
\tag{19}
$$
第二行正落在 R777 的原 P/t 四-unit域
$\mathcal G_{Pt}=\{P,t,W,V_t\ {\rm unit}\}$。
第一行是 R780 更正后的原 W 近相消帽支，仍与 $\mathcal E_N$ 不交。

不同 s 的帽管两两不交，因为在 Y-unit 上
$$
W_s-W_{s'}=b_Y(s^{-1}-s'^{-1})Y
$$
为单位。这个集合事实不意味着其积分不能相消：
各项有不同的完整来源 $\sigma_{s,0}$，系数也不是正权。

## 4. 第三中央的同帽—四单位—补域完整关系

定义
$$
\begin{aligned}
A_{s,m}(w)
 &=\int_{\mathcal H_{N,n},\,W_s\in p^m}
             f_w(Y_s^{[-m]})q\,d\sigma_{s,0},\\
C_{s,m}(w)
 &=\int_{(\mathcal E_N^c\cap\{W_s\in p^m\})
                       \setminus\mathcal H_{N,n}}
             f_w(Y_s^{[-m]})q\,d\sigma_{s,0}.
\end{aligned}
\tag{20}
$$
(19) 支付了这个相减真正使用的包含关系。
由 (15)，得到完整有限恒等式
$$
\boxed{
\frac1{216}A_{1,m}(w)
+\sum_{s\ne1}a_sA_{s,m}(w)
+\sum_s a_sC_{s,m}(w)
=\lambda^m c_N\langle2\rangle^{-d_pw}J_U(w).}
\tag{21}
$$
$A_{1,m}$ 是同 q、同 B0、同原帽的 R780(30) 裸行。
其余帽项具有 (19) 第二行的真实四-unit位置；所有补域均明列在最后一和。
没有把它们改成未附帽的 R777 W-Mellin 行。

特别原第三中央失败 $J_U'(0)=0$ 准确给
$$
\boxed{
\frac1{216}A_{1,m}'(0)
+\sum_{s\ne1}a_sA_{s,m}'(0)
+\sum_s a_sC_{s,m}'(0)=0.}
\tag{22}
$$
这个纯 U 关系不需要另假定参考或 Xi 的其它谱导数为零。
它也不单独令任何帽项、四-unit项或补域为零。
由于 $J_U(0)=0$，(21) 的整个左侧质量和为零；
这不是每一个局部质量为零的断言。

为把全部返回条件写出，对
$z=\kappa^m$ 有
$$
\begin{aligned}
Y\circ M_{s,m}
 &=Y+\frac{s\alpha_W}{36}(z-1)W_s,\\
Z_0\circ M_{s,m}
 &=Z_0+\frac4{17}(z-1)W_s,\\
t\circ M_{s,m}
 &=t-\frac{\bar a}{36}(z-1)W_s,\qquad
J\circ M_{s,m}=J .
\end{aligned}
\tag{23}
$$
其中 $\langle Z_0,W\rangle/N(W)=4/17$；
代入 (4) 可逐项看到 E 严格不动。
因此 $A_{s,m}$ 另一准确表示是
$$
A_{s,m}(w)
=\lambda^m
 \int_{\mathcal H_{N,n}\circ M_{s,m}}
       f_w(Y)q\,d\sigma_{s,1}.
\tag{24}
$$
右域须保 (23) 第一行 unit、J 深 N、(23) 第二行深 N，
以及
$$
u_JJ+u_Z\!\left(Z_0+\frac4{17}(z-1)W_s\right)\notin p^n.
$$
它位于 E-unit，但并不等于原帽。特别 (23) 第一行的 unit 与
$f_w(Y)$ 本身的 Y-unit 是两个条件，不能互相替换。

## 5. 只返回 Z0 的准确同源式

R785(17)、(22) 已付整个原三态的 Z0 偶深核。
它也适用于 (10) 的全部来源：第一 Y 方向的 canonical 平移与 Z0 正交，
在同一个完整正交覆盖上中心交叉项为零，因此与 Z0 ordinary 核交换。
$D_s$ 与 $P_{Z_0,\kappa^N}$ 也严格交换。
这一步没有把一个单态恒等式当成整个高次数空间的 scalar；
只是把已付来源身份沿相互正交的第一 Y 平移运输。

于是，因 N 为偶数，
$$
(q\sigma_{s,0})|_{\{Z_0\in p^N\}}
=\lambda^N(P_{Z_0,\kappa^N})_*(q\sigma_{s,0}).
\tag{25}
$$
这里原 q、Y、J、t 全部逐点不动。置
$$
\begin{aligned}
W_{s,N}&=b_Ys^{-1}Y+\kappa^NZ_0-at,\\
U_N&=u_JJ+u_Z\kappa^NZ_0,\\
Y_{s,N}^{[-m]}
 &=Y+\frac{s\alpha_W}{36}(\kappa^{-m}-1)W_{s,N}.
\end{aligned}
\tag{26}
$$
则每条帽项都准确返回为
$$
\boxed{
A_{s,m}(w)=\lambda^N
 \int_{\substack{Y\ {\rm unit},\ J\in p^N\\
                 U_N\notin p^n,\ W_{s,N}\in p^m}}
 f_w(Y_{s,N}^{[-m]})q\,d\sigma_{s,0}.}
\tag{27}
$$
右侧不附裸 Z0 深或 Z0 单位条件。实际失败门仍是 $U_N$，
而不是删掉 J 或把它改成原 $U_{\rm f}$。

若需要在这个返回坐标中读 (19)，所用原物理行必须相应写成
$$
P_N=b_YY+\kappa^NZ_0,\quad
W_N=P_N-at,\quad
V_{t,N}=\bar aP_N+29t,
$$
$$
E_N=e_Z\kappa^NZ_0+h_0t+e_JJ.
\tag{28}
$$
它们正是 $P,W,V_t,E$ 与 $P_{Z_0,\kappa^N}$ 的复合。
在 (27) 的域上 $E_N$ 为单位；s≠1时 $P_N,t,W_N,V_{t,N}$ 为单位。
不能在返回后仍使用未缩放的 P、W 或 Vt 来宣布同一个四-unit域。

## 6. 原相位、质量与两种表示的界限

把 (10) 的 $D_s$ 完整拉回，因帽、q、E 的伙伴部分均不动，
(20) 的帽项还可等价写成
$$
\boxed{
A_{s,m}(w)
=\alpha^{-1}\langle s\rangle^{d_pw}
 \int_{\mathcal H_{N,n},\,W\in p^m}
       f_w(Y^{[-m]})q\,d\nu_{\mathcal Q_\alpha B_0}.}
\tag{29}
$$
这里 $Y^{[-m]}$ 是 R780(18) 的原 W 逆观察。
所以同一 $\alpha$ 的六个角分支在这个完整主 Mellin 观察中可合并，
但 $\mathcal Q_\alpha$ 的全部原纤维不能删掉。
物理四-unit域的断言 (19) 是在 (10) 的实际推前来源上作出的；
拉回 (29) 后它成为所示近相消域，不再是裸 B0 的原四-unit积分。

若把 (29) 中的 raw 积分记为 $\widehat A_{\alpha,m}(w)$，
准确导数为
$$
A_{s,m}'(0)
=\alpha^{-1}\left(
 \widehat A_{\alpha,m}'(0)
 +d_p\log\langle s\rangle\widehat A_{\alpha,m}(0)\right).
\tag{30}
$$
原 canonical 平移、$1/\alpha$ 和
$\log\langle s\rangle=\log\langle\bar\alpha/\alpha\rangle$
全部保留。完整质量只在 (21) 求和以后为零；
(30) 的各项不能因此省略。

本篇的新接口是同一个第三中央的真实式 (21)：
原 W 近相消帽项、非恒等 CM 的四-unit帽项与全部 E 浅补域共同组成纯 U。
它修复了把物理 E 深与共同帽相认的路径，且不再遗留未投影 Xi 的参考项；
代价是保留显示的真实 CM 来源和移动观察。式 (27) 又允许在这条同一关系中
只返回 Z0，而不改变原 q 或删除 J/失败门。

尚未得到 (22) 与原 S/T 中央返回之间的不相容。
特别，(19) 的物理位置不把相应来源变成 R777 的裸 B0，
也不把 $Y_s^{[-m]}$ 改为 W。下一比较必须在这些显示对象上进行。
主目标仍未完成。

## 依赖及复现范围

- [R483](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)：全十八/三十六项 CM 投影和 U 的完整五伙伴来源。
- [R695](R695-original-cm-word-domains-and-a-z-carries.md)：固定奇覆盖、canonical 原纤维、全部中心及 raw CM 共轭词域。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：原最终 q 和所有完整适配条件。
- [R777](R777-original-b-sector-p-t-core-and-complete-central-renewal.md)、[R778](R778-original-degree174-full-characters-and-unramified-seventeen-point-fields.md)：原 B 态、P/t 与 W/Vt 关系及绝对核。
- [更正后的 R780](R780-original-third-central-b-state-and-true-w-deep-return.md)：原 U136 规范、E 深及 E 浅完整来源。
- [R783](R783-native-hat-images-and-nonzero-cd-exterior-central-row.md)、[R785](R785-original-three-state-even-frames-and-exact-e-gate.md)：真实帽、J/Z0 坐标、失败门和 Z0 偶深核。

所有新显示式由已付完整来源、原正交 Gram 和有限集合恒等式直接推得。
本篇没有执行新的数值实验、素数扫描或生成证书；不新增可重算数据文件。
