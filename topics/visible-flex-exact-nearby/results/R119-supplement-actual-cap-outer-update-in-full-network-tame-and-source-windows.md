# R119 续篇：实际两输入帽外行的全网络高阶一次预算与完整源读出

2026-11-15，visible-exact / tail_connector。

**状态：已证明的解析附篇，声明域内。** 本篇只更新同一个完整网络的有限外行，
不改内部根、真实 negative 分量、公共表示、层权、cutoff、source 单位或设计参数。
目的有二：将实际两输入帽的较大高阶常数真正计入全网；并写清独立源和未受
长段衰减控制的 mean/height 输出费用。局部 DN 小门不直接充当全网估计。

使用以下已发布原件：

* [N：两层 full-network 逆](R119-supplement-two-level-full-network-tame-inverse-and-complete-sources.md)，
  正文 blob 7c0015f8268052ac724a5ea1b996c636a2cd8326；
* [D：两 actual 外行的完整 weighted 传输](R119-supplement-actual-outer-row-to-complete-mixed-weighted-Schur.md)，
  正文 blob aec40417371379ce6371e76c94c0fbe963fa1901；
* [O：实际两输入帽的 long tame 与物理 Poisson](R133-supplement-actual-two-input-cap-long-tame-forms-and-physical-Poisson.md)，
  正文 blob c42aee669ef73e3321c6e3fa04f2fa18ee91b730；
* [M：两输入零宽帽及全部内端输出](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md)；
* [L：原物理半阶端口](R119-supplement-complete-physical-cap-tail-Sobolev-Schur-with-all-mean-charges.md)，L.14--L.23；
* [J：三径 source 与四态恢复](R119-supplement-three-radial-source-jets-four-state-jets-and-1734-loss.md)，
  正文 blob 6df5823e0183dec3158f16865b92a509e618ae5f。

下文所有角空间为同一真实物理角的完整 $4\mathbb Z$ 空间。出现 adjoint 时
指原 Green 配对中的真正 adjoint。ordinary mean、两个 canonical mean、
两个 wave、相反 Fourier 锥和 affine 荷均保留。

## 1. 本次实际输入与固定参考

保持 N.1 的低阶球及高阶有限量：
$$
 q_0=1792,\quad q\le8128,\quad
 \mathscr R_{1856}\le2^{-8192000},\quad
 \mathscr R_{8192}<\infty .
 \tag{HT.1}
$$
外口使用 O.21 的实际域，特别
$n_{1824}+f_{1824}\le2^{1024}\mathscr R_{1856}$、
$\|\gamma/r_\gamma\|_{A_0}\le1/32$、
$g_{1824}\le2^{1048576}$，以及 O.4 的完整低 sum 球。
这些是明确的输入门；不从高范数仅有限推出。

参考行 $\mathcal T_0$ 是 D 第1节明确重新实例化的
$Z^0=f_B^0=0$ 真 fixed-$C_R$ 行，短侧仍是当前实际背景。
它的 finite-length reflection、$D_f\Phi_R(0,0)$ 和
$\mathcal E_{B,0}$ 均保留。特别，它不是远端 Dirichlet comparator。
实际新行记作
$$
 \mathcal T_1=\mathcal N_{B,1}-\mathcal E_{B,1},\qquad
 \Delta\mathcal T=\mathcal T_1-\mathcal T_0 .
 \tag{HT.2}
$$
O.23a--b 给两实际行的准确局部差，D.5 给其完整传输：
$$
 d_{1792}<2^{-6000000},\qquad
 \|(v^\#)^{-1}\Delta S_{\rm rem,out}(v^\#)^{-1}\|_{H^{1792}}
                         <2^{-3000000}.
 \tag{HT.3}
$$
因此 N.2 的两个 low 门均已支付。这里没有把 O 的 comparator
直接改名为旧实际外行。

本篇的高背景因子为
$$
 \mathfrak H_q^{\rm act}
 =1+\mathscr R_{q+64}+
       \mathcal A_{q+16}^{\rm act}
       +\epsilon\mathcal D_{q+16}^{\rm act}.
 \tag{HT.4}
$$
$\mathcal A,\mathcal D$ 正是 O.13，不改变其 radius 单位。
$q+16\le8144$，所以外 state/curvature 最高8176，
physical height 最高8178，仍在8192以内。

## 2. 实际高常数并不放进 low cutoff

O.15 在本次最高调用上给确定数
$$
 C_*:=C_{8144}^{\rm act}=2^{3401728}.
 \tag{HT.5}
$$
从 O.21 未放宽账有
$\mathcal A_{64}^{\rm act}\le\mathcal A_{1824}^{\rm act}<2^{-7142397}$。
参考预算准确为
$\mathcal A_q^{\rm ref}=n_q+n_{64}+\epsilon
 \le\mathcal A_q^{\rm act}$；
旧 K 的同窗常数小于 $C_*$。

故对两实际之差及其真正 adjoint，O.18 给
$$
 \|\Delta\mathcal T u\|_{H^{q-1/2}}
 \le a_*\|u\|_{H^{q+1/2}}
       +8C_*\mathcal A_q^{\rm act}
                       \|u\|_{H^{64+1/2}},\qquad
 a_*:=2^{-3740000}.
 \tag{HT.6}
$$
至多再加两行/两侧的固定因子，未放宽最高项仍小于
$2^{3401728+3-7142397}<a_*$，有666 bits余量。
两actual的 $N_B,E_B$ 四项和其相邻窗口统一由这里的 $8C_*$ 支付；
第4节 high行的固定 $+4$ bits已经包含该因子8，不依赖缩窄 $q$ 的隐含余量。
同式用于原所需的相邻半阶与真正对偶窗；低方向可宽为 $q_0$ 窗。
这不把 (HT.3) 的 $2^{-6000000}$ 当作任意高窗的同阶 norm。
高窗最高未知只使用 (HT.6) 的 $a_*$；高背景另作为 forcing。

所有后续乘积使用 N.11 的准确规则：
$$
 (ST)_0=s_0t_0,\qquad
 (ST)_q\le s_0t_q+s_qt_* .
 \tag{HT.7}
$$
一次高插入以外的因子一律用已经存在的 low 映射。
不得用 $s_qt_q$，也不得将 $C_*$ 替换原内部每个 $B_{\rm hi}$。
新 $C_*$ 只属于这一个真实外口。

## 3. 原物理正端口的二层常数

D.6--D.9 定义同一个旧正区的 $\mathcal P_0,\mathcal C_0,\mathcal K_0$：
真实 root incoming 到物理 $B$ 高度，物理 $B$ 总通量到 root affine，
以及同一个 particular 的 $B$ 高度。它们的类型分别为
$$
 \mathcal P_0:H^q\to H^{q+1/2},\quad
 \mathcal C_0:H^{q-1/2}\to H^{q+1},\quad
 \mathcal K_0:H^{q-1/2}\to H^{q+1/2}.
 \tag{HT.8}
$$
右 $4/3$ 窗与左真实对偶窗仍按 D.7--D.9；这里只消费其中一阶。
mean 用完整 root shear/Poincare，不使用齐次非mean半范数替代。

在 (HT.8) 各自的真实输入/输出空间中，N.11 正区有界型构造、
N.20--N.21 的 complete Poisson/source 一次高插入，以及 L.14--L.18
的物理半阶恢复给
$$
 \|\mathcal A_0u\|_{Y_q}
 \le2^{245760}\|u\|_{X_q}
       +2^{21495808}\mathfrak H_q^{\rm ref}\|u\|_{X_{q_0}},
 \quad
 \|\mathcal A_0u\|_{Y_{q_0}}
       <2^{245760}\|u\|_{X_{q_0}}.
 \tag{HT.9}
$$
$\mathcal A_0$ 表示上述任一 map、所需强窗或真正 adjoint；
$\mathfrak H_q^{\rm ref}\le2\mathfrak H_q^{\rm act}$ 可纳入下节固定因子。

这里的21495808不是新的未展开角费。其逐来源上界为
$$
 20971520+2\cdot229376+15000+32768
       =21478040<21495808 .
 \tag{HT.10}
$$
第一项是 N.20--N.21 已支付的完整 inverse/Poisson/source 高插入，
包括 N.11 的同一零边界正型和真 adjoint；它已大于局部 strong
的12582912，并非再加一份全局解的 high norm。
两个229376允许原 source/trace 各一份低角换算，
15000是 L.14--L.18/D.8 的物理 root/B 与半阶 mean 费用，
32768是 N 第5节已列的 word/两相邻窗/mean 固定组。
最高未知一侧仍只用 D.8 的245760。
(HT.7) 保证这不是上述 high 常数相乘。

## 4. 新正片及 Schur 的 high 构造没有循环

先由 D.10 在 low 窗独立构造
$(I+\mathcal K_0\Delta\mathcal T)^{-1}$
和 $(I+\Delta\mathcal T\mathcal K_0)^{-1}$。
在有限 Fourier/层穷尽上代入 (HT.6)、(HT.9)，
最高项的系数至多 $2^{245760}a_*<1/4$；
high forcing 只乘已得的同一个 low 解。
先吸收最高项，再取原穷尽极限，所得仍是 D 的唯一解。
准确新映射为
$$
 \mathcal P_1=(I+\mathcal K_0\Delta\mathcal T)^{-1}\mathcal P_0,\quad
 \mathcal C_1=\mathcal C_0(I+\Delta\mathcal T\mathcal K_0)^{-1},
$$
$$
 \mathcal K_1=\mathcal K_0(I+\Delta\mathcal T\mathcal K_0)^{-1},
 \qquad
 \Delta R_+=-\mathcal C_1\Delta\mathcal T\mathcal P_0 .
 \tag{HT.11}
$$
不是先假定全网 high inverse 后才构造正片。

接下来依 D.13、D.19、D.24 的真实顺序，
$$
 \Delta\widehat U=H_W^*\Delta R_+S_-H_W,\qquad
 \Delta S_{\rm rem,out}
       =\mathscr L_1\Delta\widehat U\mathscr R_0 .
 \tag{HT.12}
$$
负片与公共表示没有因外行改变而重选。
$\Delta\widehat U=\Pi\Delta\widehat U\Pi$，
$\Pi$ 是129--131层的完整波空间，包含所有角模与mean。
消元后不再假定有限邻接；D 的两 high/deep Poisson 全部保留。

对 (HT.11)--(HT.12) 作 (HT.7) 的一次高插入。
四个固定组各取32768 bits，分别覆盖正片两半阶 resolvent/端口、
high 与 deep 的有序 inverse identity、两侧表示/adjoint 和
完整 mean/source 恢复。每组采用 N 第5节的同一有限计数；
新增的 resolvent low norm 小于2，仅增加固定因子，不增加角组数。
记这些固定费之和为131072。

有限支持处双逆层权继续严格使用 D.25 的2476416 bits。
最高未知新增反馈因此小于
$$
 2^{3000000+131072}a_*
                   =2^{-608928}.
 \tag{HT.13}
$$
此处3000000是 D.5 的十进制整数，不是 $3\cdot2^{20}$。
与 N 原小于 $2^{-300000}$ 的最高反馈相加仍可用同一严格吸收；
保守宽为 $2^{-299999}$ 即足。
原局部 cut、$T^\#$、$v^\#$、$F$、两个 low 锥和
真实 first-cut 逐频分配全不改变。

高 forcing 的三个可能位置如下。表内每一行已经包含其余位置的 low norm，
而非不同 high norm 的乘积：
$$
\begin{array}{c|r}
 \text{一次 high 的位置}&\text{binary exponent 上界}\\ \hline
 \text{旧 }\mathcal P/\mathcal C/\mathcal K\text{ 的 high，
             另一端 low，}\Delta\mathcal T\text{ 取最高系数}
 &21495808+245760+2476416+131072-3740000=20609056\\
 \Delta\mathcal T\text{ 自身的 high，两端取 low}
 &3401728+2(245760)+2476416+131072+4=6500740\\
 \mathscr L,\mathscr R,H_W,S_-\text{ 的 high，
                         中间取已付 low }\Delta\widehat U
 &20971520-5508476+2476416+131072=18070532
\end{array}
 \tag{HT.14}
$$
第三行的 $-5508476$ 正是 D.12--D.14：
$491521+3-6000000=-5508476$。
若 high 落在新的消元映射内，先用其准确 inverse identity：
唯一 high forcing 夹在两个已得 low resolvent之间。
其中由外行产生的项归入前两行，旧项归第三行；没有第四种 high 位置。

表中最大20609056与原 N.20 的17621632、15524380、16706264
一起相加后仍小于 $2^{20971520}$。前者还有362464 bits，
远大于这里有限行数和相邻窗的固定计数；131072已经逐组先付。
无限返回次数通过相同 low resolvent 和
$\sum_{n\ge1}n\varepsilon^{n-1}$ 求和，不按一次返回再付一份 high 常数。
原 $75/256$ 深余量与真实正 profile 不变。

这证明 N.20--N.21 的20971520完整 high forcing 桶在实际外行下仍有效。
不是将较大的 $C_*$ 免费塞进原 $B_{\rm hi}=2^{1048576}$。

## 5. 原 N 的最终常数可以保留

源仍严格按 N.21 的次序：
$$
 k_L=g_L+F_Hg_H,\quad k=k_{\rm rem}+F_Dk_D,\quad
 x_D=E_Dx_{\rm rem}+R_Dk_D,\quad
 x_H=E_H(x_{\rm rem}+x_D)+R_Hg_H .
 \tag{HT.15}
$$
原根内任意源位置到两个 cut/root 的有序 Duhamel、BV 原子、
one-sided trace、真mean及反向窗均未改。
对于已经转换成相同物理 $B$ total flux 的外源，N.4 的范数定义不变。

若从 O/M 所列的原始外数据出发，则先用第6节各自的真实 map
形成 $\mathfrak B_q^{\rm act}$。其规范化形状含完整
$\mathcal D_{q+16}$，不能只留screened部分。
把新外源 map 的 $C_*$ 作为一次实际 source 转换另付，
并给全部 source/读出分组另留确定的524288 bits，完整 high 账为
$$
 20971520+3407872+4500000+3401728+524288
        =32805408<33554432 .
 \tag{HT.16}
$$
前三项是 N.23 的未放宽28879392，不是把其已放宽33554432再作起点。
差额749024足以支付实际有限个原源种类及两个 mean/source 窗。
同一 source map 的 high 与随后 inverse 的 high 按 (HT.7) 分组，
不把最高背景相乘。

所以，对已经按真实外 map 规范化的
$$
 \mathfrak d_q^{\rm act}
       =\mathscr N_{q+2}(g)+\mathfrak B_q^{\rm act}(d_{\rm ext}),
$$
原 projected 第一参数反馈后的体状态估计仍可取
$$
 \boxed{\ 
 \|h\|_{\mathscr Y_s}
 \le2^{8388609}\mathfrak d_{s+1728}^{\rm act}
   +2^{33554433}\mathfrak H_{s+1728}^{\rm act}
                               \mathfrak d_{1792}^{\rm act},
 \quad64\le s\le6400 .
 \ }
 \tag{HT.17}
$$
对单个 raw 外源若不预先纳入其 $C_*$，最高数据项可显写
$2^{12582912}$，因为
$8388609+3401728+131072=11971409<12582912$；
high项仍由 (HT.16) 统一控制。
这两个写法的 source norm 不同，不把其中的 $s_B$、$s_R$ 或
$aw(L)$ 重新解释成数值常数。

N.26 的 D8 low 读出仍从 $\mathscr Y_{64}$ 取得，
普通源1794、背景1802，均在1856低球内。
其 unrounded7907872加本篇极小 low 外行修正只需一个固定factor2，
原 $-7951840$ 反馈余量仍足以保 $2^{-7900000}$。
最终 high 常数的一个factor2仍是 (HT.17) 的33554433。
不把 high 参数范数送回 low Schur；也没有再对 $\mathcal E_N$
作有损 Neumann。

loss1730与背景 $s+1792$ 不变。
按 J 的三次真实 scaled source 径导恢复四态四次 broken 径导时，
读取角阶 $s+4$，仍是 loss1734、背景 $s+1796$、$s\le6396$。
没有暗中调用8193阶背景。

## 6. 独立源、measure、mean 与尺度

以下每行都是一个不同的真实输入，不互相改名。

**总物理 B 通量。**
$\beta\in H^{q-1/2}$ 是 D.6 方程的完整 density source。
原 P 的 weak 源、短侧 $P_{\mu_T}$、affine mean 和真实 Piola
先组成该 $\beta$，再用 $\mathcal C_1,\mathcal K_1$。
同阶 source 消元和相应 adjoint由 (HT.8)、(HT.15) 给出；
裸 $F^t$ 端迹仍只在原 BV/trace域内使用。

**独立帽内非mean曲率。**
O.25 的准确列是
$$
 \mathcal B_\gamma\dot\gamma
  =-\mu_Ls_BD_g\mathcal K\,
                     D_\gamma\Phi_\gamma(f_B)\dot\gamma .
 \tag{HT.18}
$$
它的 $H^{q-1/2}\to H^{q+1/2}$ 预算带
$s_B\epsilon C_q^{\rm act}$ 及完整 $\mathcal D_q$。
这是 long 左端 outward $-\pi_L$ 的列，尚不是 D.6 的右端。
仅考虑此独立列且 $q_T=0$ 时，原 N.24 的准确转换为
$$
 \beta_\gamma=-P_{\mu_T}(r_\mu\mathcal B_\gamma\dot\gamma),
 \qquad
 c_{B,\gamma}=
 \frac{\langle r_\mu\mathcal B_\gamma\dot\gamma\rangle}
      {\langle\mu_T\rangle},
 \qquad r_\mu=\mu_T/\mu_L .
 \tag{HT.18a}
$$
因此 nonmean total-flux 与独立 raw mean斜率都保留，号数不混用。
其余独立 $q_T$、weak荷仍按原完整N.24相加。
尾的 normalized高度读出有 D.27 的 $1/s_B$，
故只在这同一个物理列上准确消去 $s_B^{-1}s_B$，保 $\epsilon$。
$\gamma$ 按定义没有input mean；不能据此删掉该列产生的实际 output mean。

**独立远端高度源。**
$f_*^{\rm src}$ 是 normalized height source，
其 bare列为 $-\mu_Ls_BD_g\mathcal K f_*^{\rm src}$。
它保原 $\dot H^{2,s}$ 或原明确 weak-height 单位，
不能套用曲率 $\dot\gamma$ 的 $H^{q-1/2}$ 输入名。
若给的是 physical $y_R^{\rm src}=s_R f_*^{\rm src}$，
先准确除 $s_R$；$s_B/s_R$ 不设成1。
这里的 bare列同样是 outward；转到D.6时使用 (HT.18a) 的同一负号和mean分解。
该 source 的两种 mean/Robin附加列仍按原 K.20 和 O.24--O.27保留。

**帽/long mean 与 algebraic输出。**
内端 $B(L),C_0(L),B_0(L)$、外端两曲率mean、
$m,\bar u$, Gauss量和phase primitive都使用 M 的完整输出。
它们不乘 $\epsilon$，也不由齐次
$\Delta\mathcal T1=0,\ \langle\Delta\mathcal T u\rangle=0$ 消掉。
normalized phase 读取一阶，$f_*$ 读取两阶；
physical角中的 scalar 和density有各自原真实 measure。

**高度跨度及全局荷。**
准确保留
$$
 \delta[v_0(L)-v_0(0)]
       =\int_0^L aw(t)\,D\kappa(h)\dot h\,dt .
 \tag{HT.19}
$$
其中原纯incoming列的 $aw(L)/165$ 不受screening控制。
这个物理因子原样留在源/读出范数中，不试图以524288覆盖其数值。
同理 $H_p$ 的两个端值使用同一个有向积分；
不同端不再各添一个高度常数。

一般不相容数据仍保 Z 的辅助荷
$\tau=\mathcal L_{\rm act}g/(\mathcal L_{\rm act}\sigma_\circ)$，
及真实非零分母。一个物理常高度 $\lambda$ 是唯一 gauge；
未知曲率mean、raw斜率 $c_B$、height span和frame属于实际匹配行。
(HT.17) 对有荷数据仍只具有 N/G 所定义的 projected-feedback意义；
与 nonlinear $\Gamma_1$ 导数的识别只在原 holonomy-one切向上成立。

## 7. 全部已定义输出行的确定成本，不冒称增广逆

M.20 在最高调用 $q+16=8144$ 给
$$
 C_{8144}^{M}=2^{934144}<C_* .
 \tag{HT.20}
$$
因此直接 inner/outer curvature、两个mean、phase、Gauss和
normalized height输出的完整二层系数均可由 $C_*$ 支配，
输入的 $r_\gamma^{-1},r_B^{-1}$ 按 M.23原样恢复。
O 的 whole-long mean-height 等列也按其 $C_*$ 与准确物理尺度读取。

若把所有已经定义的 affine 行及这些输出并成一个有限 block sum，
以原 M/O normalization读取，不吞掉 $s_B,s_R,aw(L)$，
其 high背景应宽写为
$$
 \widehat{\mathfrak H}_q
       =\mathfrak H_q^{\rm act}+\mathcal D_{q+16}^{\rm act}.
 \tag{HT.21}
$$
特别不能只用 $\epsilon\mathcal D$ 控制未screen的帽mean/height输出。

对 raw 数据先 source转换、再完整尾逆、最后读出，
最坏 high成本可统一宽取
$$
 32805408+3401728+524288+1024+2
       =36732450<41943040 .
 \tag{HT.22}
$$
1024支付 O.21/E 的实际 finite trace 到 normalized B 高度单位，
两个固定factor2含完整mean/Γ的最后读取。
对于 source map和readout各带high背景的情形，(HT.7)仍只保一个high，
并用统一low解估计其余方向；不会产生
$\mathcal D_q\mathfrak H_q$ 的两个最高范数乘积。
highest raw 数据项也严格低于此宽界。

这给所有这些**已有定义的行**一个明确 $2^{41943040}$ tame成本。
它不是这些行联立矩阵的逆范数。
特别，独立 $\gamma$ 是否等于实际主体送来的内C、
内端 $B/C$ mean、两个相对height、waist/材料约束和frame闭合，
仍须用它们真实 residual 作联立，不由一份输出估计自动消去。
原 approximate inverse 的 A.19--A.24、collar seed、Nash初入口
及全部 boundary defects不在本篇被改成0。
本篇新增的是 actual外图的完整 high/source费用，并非最终全局解。

## 8. 不再混淆设计参数与挠曲参数

本篇固定当前设计 metric；$\nu,\eta,\Gamma_1,\Gamma_2$ 的真正参数导数
若作为独立设计列输入，仍保原系数、$H_p$ 和端值。
$\nu$ 是intrinsic设计参数，不称为同metric flex参数。

原 [平盘与五次标记](R133-supplement-waist-normal-offset-and-fifth-power-markers.md)
第5节给另一条明确的几何接续：
一旦取得同一个全闭精确径向metric的 $G$，且有原规定的两同轴真平盘，
先用 $G_\tau=R_\tau G S_{-\tau}$，再在相同材料平盘加固定标记。
所有intrinsic参数可先选定后冻结；不必另构
“固定metric整$\nu$族”IFT。
该接续仍需要原非平凡性、标记唯一峰、全域几何和reach/held门，
也不替本篇尚未求解的单个 $G$ 的全匹配。
