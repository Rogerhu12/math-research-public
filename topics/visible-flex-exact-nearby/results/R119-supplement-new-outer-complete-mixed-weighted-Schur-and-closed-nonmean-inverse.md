# R119 续篇：新外真实同表示差、全部加权两外消元与闭合非mean块

2026-11-14，visible-exact / tail_connector。

**状态：解析结论；完整同表示差、源窗和真实消元已核。** 本篇使用新 simple-root 对象、
新外 F/J/C 三篇的同一个公共参数点。外侧的未知高度列从头固定
独立物理 $C_R$，其准确径向边界为 C.13a；完整帽内的 $C_R$
响应不在这里被设置为零。证明把新增有限两行真正接入原 mixed
高外和无限 deep-low 消元，得到同一个表示、同一逐层权下的实际
非mean inverse。两个物理 mean、两条曲率 mean、$\nu$、两
$\Gamma^*$ 和全部外源继续留在明确的联立式。

记
$$
 \mathcal X\le2^{-8388608},\quad
 \epsilon_L=e^{-7L/4}<2^{-33554432},\quad
 v_j^+=2^{-464800}J^{-4165}\delta_j^{1073/32},\qquad J=j+5 .
 \tag{Y.1}
$$
实际和径向的完整 remaining 算子在同一个根波空间满足
$$
 \boxed{\quad
 \|(v^+)^{-1}(S_{{\rm rem},a}-S_{{\rm rem},\circ})(v^+)^{-1}\|
                                  <\eta:=2^{-5800000}.
 \quad}
 \tag{Y.2}
$$
此式包括 canonical mean 的行列。令 $P_N$ 是 remaining 中的
canonical 非zero Fourier 投影，则
$$
 \boxed{\quad
 R_{N,a}=[P_N(I-S_{{\rm rem},a})P_N]^{-1},\qquad
 \|v^+R_{N,a}v^+\|<(1-\eta)^{-1}<2 .
 \quad}
 \tag{Y.3}
$$
这是实际闭合、固定 $C_R$ 的整个非mean块，不是开放内部压缩。
完整算子的物理常高度核和通量兼容条件在第8节保留；
(Y.3) 没有将它们称为已反演。

## 1. 两个径向正端参照不能混同

C 篇所选的真实固定外线，在长段的实际变量
$v=awh$ 中是
$$
 v_{m,t}(L)=M^2v_m(L)\quad(M=|m|\ge4),\qquad v_{0,t}(L)=0 .
 \tag{Y.4}
$$
它来自原完整曲率公式
$(\delta C_R)_m=-\chi_R\sqrt{E_R}[(2h+h_t)_m-M^2h_m]$
及 $(aw)_t=2aw$；mean 来自原径向 holonomy 小根的一阶值为零。
这里固定的是独立物理 $C_R$。它不等于帽内 regular 图被解掉，
也不由只在共同偶反射类证明的帽定理获得任意背景的 all-$4\mathbb Z$ 图。

把 (Y.4) 的完整径向正返回记为 $\mathcal R_\circ$。
N 篇另一个较简单的 comparator $\mathcal R_0$ 使用
$\mathcal N_{B,0}=\mu_0|D|\coth(L|D|)\Pi_\perp$，即远端
非mean高度为零的线。两者确实不同。
在 N.1 取 $a=0,Z=0,F=0$，仍保留真实
$D_f\Phi_R$ 的有限长反射，给
$$
 \max_{q\le4}\|\operatorname{ad}_{D_\phi}^{\,q}
            (\mathcal R_\circ-\mathcal R_0)\|_{H^s\to H^s}
 <2^{160}\epsilon_L,\qquad |s|\le2 .
 \tag{Y.5}
$$
实际 $Z$ 固定在 N 已付物理球中。三角不等式及 $F\le n_0$ 给
$$
 \max_{q\le4}\|\operatorname{ad}_{D_\phi}^{\,q}
          (\mathcal R_{a,Z}-\mathcal R_\circ)\|_{H^s\to H^s}
 <2^{162}(n_0+\epsilon_L),\qquad |s|\le2 .
 \tag{Y.6}
$$
两个 mean 阻抗及未匹配界面项仍全部属于这同一个算子。

径向 (Y.4) 是固定实 Robin 线，所以 $\mathcal R_\circ$ 是
Fourier 对角酉算子。实际固定 $Z$ 的 $\mathcal R_{a,Z}$
一般不自伴；以下只用 P/N 已付的 norm 小于2和两个强余项窗。
不把保通量或近酉的说法当作它正定 $L^2$ 酉性的证明。

## 2. 旧逐行参数小量在新增联合行后仍然保留

原真实六项邻胞数记为 $\mathcal N_j$，只求和实际存在的胞元。
除了新增有限元件外，J.11 重实例化的是旧 controlled N.9、
N.11 的每一行，而不仅是它们的总和。这一点可直接从新固定点核实。

对任一旧行，完整首相位误差在整个允许 $q$ 球上满足原局部门；
真实第一 KAM 改动仍为
$2^{39}(j+4)\sqrt j\,\delta^{-3/4}\mathcal N_j\mathcal X$。
径向归一化首相位的第一参数导数在原 $2^{-64}$ 系数盘中可用
$2^{36}$ 宽放。再用 $|\varphi_i'|<2^{10}$、
$|\partial_q\chi_i|<2$，逐行代入
$q_i=\varphi_i(-E_i)$，仍给原完整物理 Q7 篇 D.5：
$$
 |\Gamma_i^*-\bar\Gamma_i|
 <2^{200}J^4\delta_j^{-6}\mathcal N_j\mathcal X .
 \tag{Y.7}
$$
例如首相位的原 $2^{144}J^3\delta^{-5}\mathcal N_j\mathcal X$
和第一 KAM 项乘 $2^{36}$，再乘 $2^{10}$ 和两个 inverse 因子，
都严格小于显示右边。新增外行只改变共同固定点的位置；
这些逐行门对球中任意其它坐标统一，故没有把其总 $\ell^\infty$
误差均匀灌入所有深层。

因此旧 V.1 在所有未改变的实际行、列仍准确成立：
$$
 \epsilon_j^{\rm old}
   =2^{35000}J^{40}\delta_j^{-47}\mathcal N_j\mathcal X .
 \tag{Y.8}
$$
所有 controlled 根图、完整 mean 和两 $\Gamma$ 的值已包含在内。
真正变分方向中的 $D\Gamma^*$ 仍是源列，未由 (Y.7) 删除。

## 3. 新有限 strict 片的一阶物理差

外 F.11--F.16 使用的完整物理系统与原 Q7 篇 D.6 相同：
$$
 (y_\sigma)_t+\partial_\theta(g_\sigma y_\sigma)
     =-\sigma\kappa w/2,\quad
 w_t=d(y_++y_-)+qv(y_+-y_-),\quad
 w=a+\partial_\theta^{-1}(y_++y_-).
 \tag{Y.9}
$$
$a=\langle w\rangle$ 和另一独立 mean
$\langle y_+-y_-\rangle$ 均保留。
在其完整半阶空间 $\mathcal E_{\pm1/2}$ 中比较 generator。

F.13 已给同一 $\Gamma$ 的
$\int\|\kappa-\kappa_0\|_{\mathcal A_1}<2^{937}n$，
$|I_*|<2$、$\int q<512$ 及真实流差 $<2^{64}n$。
传输项仍含一次角导；mean 行由 (Y.9) 准确取平均。
完整乘法、半阶平衡及两个 mean 计入后可用
$2^{1200}n$ 的一阶 generator 差。

比较 $\Gamma^*$ 与 $\bar\Gamma$ 时只对系数作 Cauchy。
原两 bump 支集及其半径 $2^{-64}$ 复盘保持，盘内
$Q$ 的相对改变小于 $2^{-32}$，同一平方根支满足
$$
 |Q|<2^{221},\quad |Q_t|<2^{426},\quad
 |Q_{tt}|<2^{641},\quad |\sqrt Q|>1/32 .
$$
径向
$\kappa_0=Q_t/(2q)-(1+Q)^2/(4q)+5Q_t^2/(16q^5)-Q_{tt}/(4q^3)$。
最大项的 bits 为 $2\cdot426+5\cdot5=877$；
乘真实长度、有限和后
$\int(1+|q|+|\kappa_0|)<2^{1000}$。
系数 Cauchy 的64 bits、两个参数及完整 half-order 乘法均可放在
$2^{1200}$ 内。不对复参数的无限高频 propagator 断言 $L^2$ 有界。
故
$$
 \int\|\mathsf A_a-\mathsf A_{\bar\Gamma}\|
             _{\mathcal E_{1/2}\to\mathcal E_{-1/2}}
 <2^{1400}(n+|\Gamma_o^*-\bar\Gamma_o|).
 \tag{Y.10}
$$

原物理角与 F 的完整固定标签空间也要重新计 mean lift。
真实流 Jacobian 及逆在 $[1/2,2]$，所需角导由
F.13--F.14 的 $C^8$ 门控制；实平移本身 norm1。
唯一比旧短片大的有限项是
$|S_+-S_-|<2^{11}$。
把它保在 $c,\alpha$ 两行，角 primitive 的非mean norm 不超过
$1/4$，两个真实 lift 及逆在半阶空间各小于 $2^{36}$。
F.16 的 $2^{1536}$ 因而给任意 strict 子段
$$
 \|U_{\rm ph}(t,s)^{\pm1}\|_{\mathcal E_{\pm1/2}}<2^{4096}.
 \tag{Y.11}
$$
这里没有对小位移 pullback 使用假的同阶小差。

用原准确 Duhamel，一侧只在 $\mathcal E_{-1/2}$，另一侧只在
$\mathcal E_{1/2}$ 收费。J.14 及第一 inverse 共同给有限外参数的
安全界 $|\Gamma_o^*-\bar\Gamma_o|<2^{160128}\mathcal X$。
两次 (Y.11) 与 (Y.10) 遂给
$$
 \|U_{{\rm st},a}-U_{{\rm st},\circ}:
              \mathcal E_{1/2}\to\mathcal E_{-1/2}\|
 <2^{171000}\mathcal X .
 \tag{Y.12}
$$
正反向同样；没有第三次 Cauchy 条件数。

## 4. 真根、graph、全部 mean 到有限原位差

根 germ 不含两个下降 bump。左根使用原 Q7 D.18--D.20，
右 simple 根使用新 A.15--A.25 和 F.21 的已付替代输入：
$b_0<2^{29}$、$|V|<17$、$|V_\xi|<129$、
$n_{e,0}=2^{64}n_0$，完整根能量常数 $2^{2184}$。
因此相同 exact-root、normal shear 和 graph 公式给
$$
 \|L_e^{\pm1}\|<2^{2300}\sqrt{b_e},\quad
 \|\Delta L_e:H^1\to\mathcal E_{-1/2}\|<2^{6700}b_e^{3/2}n_e,
$$
$$
 \|\Delta L_e^{-1}:\mathcal E_{1/2}\to L^2\|
                       <2^{11400}b_e^{5/2}n_e .
 \tag{Y.13}
$$
此处是 balanced root 到实际 fixed strict cut；不使用旧已勘误
的低非mean free-frame $b^{1/2}$ 断言。
改为 F 使用的自由 Airy 两列时，再按完整 free-frame 证明及
根处真实 $c,c/\pi$ 两个 mean 付其原准确转换。
$b_X<2^{336}$，右根更小；这些 root/graph 差可统一放宽为
$2^{16600}\mathcal X$。

F.25 的任一完整有序子乘积和 inverse 小于 $2^{32768}$。
在少于32项的真正 telescoping 中插入 (Y.12)、(Y.13)，
并保 strict 端的两个 $2^{36}$ 转换，得到完整两根 Cauchy 差
小于 $2^{240000}\mathcal X$。
每项只乘左右两个完整子乘积，未逐个重新乘所有粗界。
径向 incoming 所恢复的端状态 norm 不超过 $\sqrt2$；
transfer 差作为实际 particular 进入，准确 scattering 源消元
norm 小于2。因此
$$
 \|\Delta S_o:H^1\to L^2\|,\quad
 \|\Delta S_o^*:H^1\to L^2\|<2^{241000}\mathcal X .
 \tag{Y.14}
$$
第二式使用真实 $S_o,S_{o,\circ}$ 酉和径向 $H^1$ norm1，
$\Delta S_o^*=-S_o^*\Delta S_o S_{o,\circ}^*$。
这保留完整两端、所有角模及两条 mean 行。

原相邻正片和新外正片按真实 $U_a=R_{+,a}S_{-,a}$ 接合。
forward 差用 $R_{+,a}\Delta S_-+\Delta R_+S_{-,\circ}$；
adjoint 差用
$\Delta S_-^*R_{+,\circ}^*+S_{-,a}^*\Delta R_+^*$。
实际 $R_{+,a}$ 只收 norm2，右侧的 $H^1$ 因素都是径向的。
结合 (Y.6)，有限受影响行列在原 Airy 单位的双一阶差
小于 $2^{242000}(\mathcal X+\epsilon_L)$。
完整源也沿同一个次序，不能只保孤立 $S_o$ 的源。

## 5. 同一 unitary 表示与原频率权

采用高外 H.6--H.9 的**共同** unitary $H_a$，
而不是 J.22 的非酉行操作。$H_a$ 在 canonical mean 上是恒等；
径向 $H_\circ$ Fourier 对角，并在每个 $H^s$ 上 norm1。
J.19--J.21 及原 V.16 的有序比较给有限新行
$$
 \|H_a-H_\circ:H^1\to L^2\|,
 \quad\|H_a^*-H_\circ^*:H^1\to L^2\|<2^{50000}\mathcal X .
$$
这里 $15000+\log_2\Lambda_o+\log_2(\epsilon_o^c/\mathcal X)
=49816$，相邻旧行也在显示宽界内。

令 $\widehat U_a=H_a^*U_aH_a$、
$\widehat U_\circ=H_\circ^*U_\circ H_\circ$。
使用 V.17 的三个准确有序项，其右侧分别只要求径向
$H_\circ$、差 $H_a-H_\circ$、径向 $U_\circ H_\circ$。
adjoint 用对应三个项和上述两窗，不用实际 $U_a$ 酉性。
得到有限新行列的明确界
$$
 \|\Delta\widehat U:H^1\to L^2\|,
 \quad\|\Delta\widehat U^*:H^1\to L^2\|
                         <2^{262144}(\mathcal X+\epsilon_L).
 \tag{Y.15}
$$
真实新因素只出现在 $\{(129,1),(129,2)\}$；其相邻输入仍全部保留。
为以下行列计数，可把有关有限支持统一放进层 $129\le j\le131$。
其它行、列继续用 (Y.8)。这说的是未消元 $\Delta\widehat U$
的真实有限邻接，不声称 Schur 之后仍有限邻接。

高投影必须采用 C.13 的同一浅平台：
$$
 T_j^+=\max(2^{65664}J^2\delta_j^{-9},\,2^{131072}),\quad
 P_{H,j}=\mathbf1_{\{|m|\ge T_j^+\}},\quad
 \Omega_j(m)=\max(1,\langle m\rangle/(1+T_j^+)).
 \tag{Y.16}
$$
仅有限浅层改变，深于8192的阈值未变。
准确有 $T_j^+/T_j<2^{65536}$、相邻阈值比 $<2^{10}$，
两邻块的 $\Omega$ 比 $<2^{20}$。不只提高两个外行而破坏这个比。

由原 F/P 两窗及 J 的 scalar normal form，直接重复 H.4--H.9
的 unitary 共轭，得到 $\widehat U_a=U_d+\mathcal R_a$：
旧行强余项仍为 $2^{12000}\lambda_j^{4/3}$，
有限新行、列可取 $2^{24000}$。
为核后者，不反演 J 的非酉行矩阵：直接将 F.2 的 $2^{12000}$、
P 的两个 $R_++I$ 强窗、每个 $H^{\pm1}$ 的 $2^{66}$、
J.21 的 $2^{4500}\Lambda_o^{4/3}$ 和最多8个相邻块有序相加，
均严格小于 $2^{24000}$。真实低输入及 mean 包含在这两窗中。

## 6. 全 high 与无限 deep-low：两个真实 Poisson

原任一相邻块比不超过 $2^{256}$ 的权仍合法。
尤其 $w=1,v^+,(v^+)^{-1}$，以及 $wF^{\pm1},wF^{\pm2}$，
$F_j=2^{4096}J^4\delta_j^{-5}$，在距离至多2的块上比值
小于 $2^{184}$；径向再乘 $\Omega$ 后仍小于 $2^{204}$。
这检查包含整个浅前缀，不只深层。

有限行的完整高一阶除法与 $4/3$ 增益给
$$
 2^{24000+12+256+32}(T_\bullet)^{-1/3}<2^{-19000}.
$$
旧行的 H.13 仍小于 $2^{-9500}$，提高阈值只改善。
因此 H.16--H.21 的准确 Neumann 和其 adjoint 全部成立：
$$
 \|wR_Hg_H\|_{H^s}<2^{14}\|wg_H\|_{H^{s+1}},
 \quad -4/3\le s\le0,
$$
$$
 \|wE_Hw^{-1}\|,\ \|wF_Hw^{-1}\|<2^{-9000},\qquad
 \|\Omega_H wE_{H,\circ}P_Lw^{-1}\|<2^{-9000}.
 \tag{Y.17}
$$
最后一式只用于已覆盖内部低输入。现在每个负窗都已完整覆盖；
$C_R$ 等独立源仍不是取得 $|m|<T_j^+$ 权限的未知端口。

这里只使用 H.13--H.21 的双强窗和代数。
H.22 依赖完整实际酉性的“Schur 满射酉”结论**不在本篇使用**。
高 inverse 仍索取一阶源窗，未变成任意 $L^2$ 全源 inverse。

按真正 deep-low 投影
$P_D=\mathbf1_{\{j\ge8193,\ 0<|m|\le A_j\}}$，
$A_j=2^{-40}\delta_j^{-1/8}$。
径向频率对角和真实相邻阈值给
$$
 E_{H,\circ}P_D=0,\qquad P_DF_{H,\circ}=0 .
 \tag{Y.18}
$$
提高浅阈值不会破坏该准确零式。
原完整 deep-low L.5--L.17 的锥、真实两行根架及 Green 核没有改变；
无限尾始终用真正强允许线，未截成一个有限终点。

high Schur 的两种有序差分别是
$$
 \Delta S_HP_D=[I,F_{H,a}]\Delta\widehat U P_D,\qquad
 P_D\Delta S_H=P_D\Delta\widehat U[I;E_{H,a}] .
 \tag{Y.19}
$$
有限 (Y.15) 的支持在这里准确不出现。
(Y.19) 仍把低端的一次角导付成 $2A_j$，并用 (Y.17) 控制
全部长程高反馈。原 L.21--L.22 的 Neumann 于是给同样的
$$
 \|wF^{-1}R_{D,a}F^{-1}w^{-1}\|<2^{66},\qquad
 \|wF^{-1}E_{D,a}w^{-1}\|,
 \ \|wF_{D,a}F^{-1}w^{-1}\|<2^{130}.
 \tag{Y.20}
$$
源域及状态域仍分别是 $\|wFg_D\|$ 和 $\|wF^{-1}x_D\|$。
没有把实际 mixed low 块先对角化，也没有假定近核在低包。

## 7. 新权上的完整 remaining 差与真正非mean inverse

先按准确 high Schur 恒等式
$$
 \Delta S_H=[I,F_{H,a}]\,\Delta\widehat U\,[I;E_{H,\circ}]
 \tag{Y.21}
$$
收费。右径向 Poisson 及 $\langle m\rangle<2T_j^+\Omega_j$
支付唯一角导；左 Poisson 用相应逆层权。
对有限支持，$j\le131$ 给
$(v_j^+)^{-1}<2^{503000}$，且有关输入的 $T_j^+=2^{131072}$。
全部真实行列计数和两个增广 Poisson 可再付 $2^{20}$，故其贡献
严格小于
$$
 2^{2\cdot503000+262144+131073+20}
                   (\mathcal X+\epsilon_L)
 <2^{1450000}(\mathcal X+\epsilon_L).
 \tag{Y.22}
$$
这里没有把任意 $C_R$ 源列的角导付成内部 cutoff。

旧 V 篇用的是 $v_j=2^{-432000}J^{-4165}\delta^{1073/32}$。
准确有 $v^+=2^{-32800}v$，所以对同一个 block 两侧重权的费用为
$2^{65600}$，浅平台付一次导数至多另乘 $2^{65536}$。
因此旧 V.20--V.22 的完整行列和只需再付 $2^{131136}$，
原 $2^{-6000000}$ 门仍严格小于 $2^{-5868864}$。
这只是对已付原算子的换权，不把它用来制造新增外行的小量；
后者已经由 (Y.22) 单独证明。

再按真正 deep-low Schur
$$
 \Delta S_{\rm rem}=[I,F_{D,a}]\,\Delta S_H\,[I;E_{D,\circ}]
 \tag{Y.23}
$$
展开四项。无 $E_D,F_D$ 的项使用刚才的完整 high 差。
其余三项用 (Y.19)，因此中间有限新行仍不出现，
一次角导仍是 $A_j$，不是 $T_j^+$。
旧 L.24--L.27 的逐层预算仅增加 $2^{65600}$：
$$
 2^{1265600}J^{8400}\delta^{-1987/16}\mathcal N_j\mathcal X .
 \tag{Y.24}
$$
真实剩余幂仍是
$31867/256-1987/16=75/256$；
到65536层前保有限整段多项式上界，之后才用几何比
$2^{-11/256}$。原三项总费 $<2^{-6000100}$ 变成
$<2^{-5934500}$。
与 (Y.22) 及完整直接项相加，严格得到 (Y.2)。
尤其没有以“高消元后的差仍只邻接”来略去其外响应。

径向方面，(Y.18) 使 high 和 deep-low 两种真实消元的次序一致。
消去有限高空隙及无限真实允许尾，所得非zero remaining 网络
就是 C.14--C.22 的 fixed-$C_R$ 径向网络：
其外线正是 (Y.4)，根波单位正是同一个 $H_\circ$。
后者按层/Fourier 对角酉，并与逐窗标量权交换。
阈值相等若在 C 中多保一个有限行，可按 (Y.17) 再消去；
新的 inverse 是原 C.22 inverse 的相应压缩，权门不增加。
因而
$$
 \|v^+ R_{N,\circ}v^+\|\le1 .
 \tag{Y.25}
$$
这里没有把 Q7 裸 middle 或原 open 内部矩阵冒作这个算子。

在 $\|(v^+)^{-1}k_N\|<\infty$ 的源域上，准确 Neumann 级数
$$
 R_{N,a}=
 [I-R_{N,\circ}P_N\Delta S_{\rm rem}P_N]^{-1}R_{N,\circ}
 \tag{Y.26}
$$
给 (Y.3)。先对有限模、有限根源构造，再以已付 weighted 门
取极限。径向逐频唯一性来自真实 C.22，
high/low 的定义域唯一性来自 (Y.17),(Y.20)。
任何属于声明状态域的齐次解都满足
$\|v^+x_N\|\le\eta\|v^+x_N\|$，因此为零。

## 8. 两个 mean 与原 source 的完整联立式

记 $P_Z=I-P_N$ 于 remaining。它是 canonical mean 投影，
不是任意非径向物理解的平均投影。置
$A_a=I-S_{{\rm rem},a}$。真正方程仍为
$$
 \begin{split}
 x_N&=R_{N,a}(k_N-A_{NZ,a}x_Z),\\
 [A_{ZZ,a}-A_{ZN,a}R_{N,a}A_{NZ,a}]x_Z
       &=k_Z-A_{ZN,a}R_{N,a}k_N .
 \end{split}
 \tag{Y.27}
$$
由于径向交叉块准确为零，(Y.2)--(Y.3) 给两个交叉的源门，
且 mean Schur 相对 $A_{ZZ,\circ}$ 的双逆权差至多
$\eta+2\eta^2<2\eta$。
这没有把 $x_Z$ 设为零，也没有要求它预先具有更强状态权。

平端真实域仍必须规定 total mean flux 趋0、平均高度有有限极限。
原 mean 篇 M.22--M.25 在未改深尾继续有效；
由 $v^+=2^{-32800}v$ 及旧 $\nu/v$ 有有限 supremum，
其实际/径向根迹差仍趋0。
原两个根初值用
$D_{\sigma,M}(0)\asymp(M/b)^{-1/3}$、
$D_{\sigma,M}'(0)\asymp(M/b)^{1/3}$，mean 用
$c,i\sigma c/\pi$。不以远场 $M^{-1/6}$ 代替这些初值。
新增有限根不影响该平端域的同一性。

闭合 (Y.4) 后，径向 mean 的自然通量条件在两端均为零；
整体物理常高度成为真实一维核。实际系数仍保持常高度解，
但其根波有非zero canonical 分量，因为
$u=\sqrt\alpha\,h_{\rm const}$。
所以原开放 M.19 的 mean inverse 不能不经修改用于 (Y.27)。
必须在同一个源域上付完整通量兼容与一个物理高度 gauge；
这个有限 rank 步骤是本篇后继的明确 mean 门。

所有 source 先沿完整 Piola、root、graph、strict 和正 DN 接线
变为 $\widehat g=H_a^*g$。设 $k_L=g_L+F_Hg_H$，分为
remaining 与 deep-low 后，
$$
 k=k_{\rm rem}+F_Dk_D,\qquad
 x_D=E_D(x_N+x_Z)+R_Dk_D,\qquad
 x_H=E_H(x_N+x_Z+x_D)+R_Hg_H .
 \tag{Y.28}
$$
高 source 必须给 (Y.17) 的一阶窗，deep source 必须给
$\|wFk_D\|$，remaining source 给 $\|(v^+)^{-1}k\|$。
(Y.28) 逐列应用全部 ordinary、两 weak、真实 BV/原子、
独立 $C_R$、$\nu$、两 $D\Gamma^*$ 和材料参数列。
$F^t$ 的裸端荷不能由体 $L^2$ 自动取得。

特别 $C_R$ 的 nonmean 列按 N.23a 的
$2^{48}a_Bw_B\epsilon_L:H^{-1/2}\to H^{1/2}$
和 P 的后续源转换进入；其它 $f_*^{\rm src}$ 保原真实范数。
$B_R$ mean、$C_R$ mean 及 N.23b 的非mean Robin 残差仍独立。
N.25 的 mean 高度跨度仍付 $aw(L)/165$，没有给它指数屏蔽。
参数微分还保 $\dot H_a^*g$、状态坐标导数、真实
$\delta(a_Bw_B),\delta\mu_0,\delta\Phi_R$ 和 J.16--J.17 两行。

本篇已把旧的有限浅前缀和新外负片都接入同一个实际 closed
非mean块，并支付全部高/深 mixed 反馈。
仍须完成 (Y.27) 的物理 mean 商及兼容、原强 source/label
两向连续映射和帽内真实 $C_R$ 响应的联立。
这里不以 fixed-$C_R$ inverse 宣称全 PDE、$\nu$ Schur 或课题完成。
