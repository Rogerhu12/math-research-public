# R119 续篇：低阶小球、高阶有限背景上的完整网络 tame 逆

2026-11-15，visible-exact / tail_connector。

**状态：下述完整 proxy 与 projected 第一参数反馈的两层 tame 逆已证明。** 本篇保持同一个 fixed-stop
simple-root 对象、$\zeta_j$、第二参数、公共五盒点、全部真实切口和
原 source 单位。第一参数使用 L 已构造的同一个真实值图。
新的结论只把已付 I/T 的背景量词分成两层：1856阶背景小，
更高背景仅有限。它不让 cutoff 随高范数变大，不把不同 Airy 图
写成共同解析 lag，也不把有1730阶损失的逆称作 Picard 收缩。

主要结论是完整几何 proxy 与已定义 projected 第一参数反馈的
tame 逆。真实 reduced Jacobi 导数另有准确 $\mathcal E_N$；
该项在末节保为有源高低乘积，不用这个有损逆对它作泛 Neumann。
一般 charged 数据的解仍只具有原 G 明示的 projected-feedback
识别；不能由此给 $\chi\ne0$ 的非线性第一参数值图。

## 1. 定义、两层背景及外口

使用已发布的：

* [I：附近全尾 proxy 逆](R119-supplement-nearby-finite-Sobolev-full-tail-proxy-inverse-and-complete-sources.md)；
* [T：4384角窗与1730损失](R119-supplement-4384-angular-window-1730-loss-and-finite-tame-budgets.md)；
* [L：低范数第一参数与高阶 tame 共轭](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md)；
* [C：受控 residual 径向 jets](R119-supplement-off-shell-controlled-radial-jets-and-exact-holonomy-retraction.md)；
* [R：canonical 强径向域](R119-supplement-canonical-strong-radial-finite-Sobolev-domain-and-quadratic-sources.md)；
* [G：低方向第一参数与 projected Schur](R119-supplement-low-direction-first-Gamma-projected-metric-source-and-linear-Schur.md)；
* [K：两层 true long DN/Poisson](R133-supplement-two-level-finite-Sobolev-true-long-DN-and-Poisson-tame.md)。

K 使用最终包含 K.21a 的版本：其 normalized 输出为
$W_R=(P,U,K,V,B_R/\chi_R,C_R/\chi_R)$，physical $\chi_R$、
独立 $f_*^{\rm src}$ 和原 Robin source 列仍分别保留。

在实际实背景上明确置
$\mathscr R_a=\max\{\mathscr D_a,\mathscr B_a,
\mathscr N_a^{[3]},\mathscr R_{o,a}\}$。
这里直接使用四态角阶 $a$ 与前三阶 scaled residual 的角阶 $a$，
不借 C 中另含 $+4$ 的同名字母定义再暗加四阶。
$\mathscr D_a$ 是 L 的真实四态范数；
有限 connector 仍按 $2^{-440}$ 方向单位，不能代内部 $c_j$。
这些是当前实际背景的大小，不把已知成员换成新的径向模型。
holonomy-one mean、真实 height、分片四阶径向正则和真根 germ
均按 C/M 重建。令
$$
 q_0=1792,\qquad q_{\max}=8128,\qquad
 \mathscr R_{1856}\le R_0:=2^{-8192000},\qquad
 \mathscr R_a<\infty\quad(1856\le a\le8192).
 \tag{N.1}
$$
高阶量不要求小。L 的值图只用 $\mathscr D_{20}$，故 (N.1)
已经定义同一个 $\gamma_1^*(W)$；不能因高阶方向改变而重新选参。

### 第二参数间隙实际只消费低阶输入

这里须把
[B：有限径向首相位](R119-supplement-finite-radial-Sobolev-first-phase-and-fixed-second-parameter-gap.md)
的两个用途分开。B.2 原来的8196阶小球是一个充分的共同输入，
不是其标量有限部或根处四阶图真正使用的最少阶数。
现在不直接套用那个整球定理，而将其下列有限计算在 (N.1) 重做。

先在角阶192重做 C.9--C.13 的准确递推。
其四态补充角导至多用到196，源只到三次径向导数及196角阶；
C.9a 的完整逆幂级数只需
$2^{200}\|J-1\|_{H^{196}}<1/4$。
(N.1)、原六邻胞 $C^\#$ 及 C.9a 的原上界即给此门，
不使用 $H^{8196}$ 小量。原 profile 的
$\ell_j^{a+1}Q^{(a)}$、C.7 的完整源和有限 connector 的
$\ell_o$ 同样给四次 scaled 径向递推。
把 M 的 holonomy 小根、当前/参考四态的径向乘子
$e^{\pm\psi}$、两个原根和新增根分别保留，
这些低阶真 jets 可统一按半径
$$
 R_\beta:=2^{196608}\mathscr R_{1856}
          \le2^{-7995392}<2^{-2097152}
 \tag{N.1a}
$$
收费。131072 bits来自 C.9 的有限代数递推；
归一换回参考四态、完整 mean 小根及固定 connector
另用至多32768 bits，余下32768覆盖两次角嵌入和有限计数。
没有把 connector 的 source 转换系数换成内部 $c_j$。

B.6--B.8 的 scalar 有限部只使用两个径向 jet 和
$H^4_\theta\hookrightarrow C^2_\theta$；
B.10--B.13 的真 root 图使用四个径向 jet 与 $C^8_\theta$。
B.20 的 $|s|\le64$ 首相位识别用至多160角导，
其 $V,V_\xi$ 从上述192阶四态 jet 直接读出，
原 polynomial $B_0$ 的四阶导数按 B.4 后的独立原件保留。
所以这三个结论的全部输入由 (N.1a) 支付。
任意更高窗的全层余项并不在这里转授，
而是由下文 N.5--N.22 的 one-high 预算另付。

B.15--B.19 的一、二次有限部差于是仍使用原16384/32768 bits
和原三个 profile。在第一参数上，L 的同一低值图
及其物理 $2^{8960}J_j^2\delta_j^{-1}C_j^\#$
导数界更小于 B.25 原来所付的预算。
因此 B.25--B.29 的标量结论适用于当前 $R_\beta$ 球，
并与原固定的已知成员 $u^\flat$ 比较；后者仍用自己已经证明的
$R_*=2^{-2097152}$，不声称其8196阶 norm 变成 $R_\beta$。
准确沿 B.27 的全层求和有
$$
 128\sup_iN_i|\beta_i(W)-\beta_i^0|
 \le2^{1211008-4194304}<2^{-2980000}.
 \tag{N.1b}
$$
第一 principal 相位由 L 保持相同值，
故原 $1/(256N_i|n|)$ 的非零频算术间隙不变。
两个 physical mean 使用独立真行，绝不除以 $n$。
本段只保持第二参数的真实 scalar gap；
任意变化外图的正 form 与 source 仍须下面 (N.2) 的独立接口。


外口先取 I 已付的同一个完整真实线性 long/$C_R$ 行。
若更新为 K 的实际非解析 long 背景，另要求它的真相对型、
伴随型、闭合 mean、Poisson 和真实源接口，并明确要求
$$
 \mathcal A_{1824}\le2^{-2097152},\qquad
 \|(v^\#)^{-1}\Delta S_{{\rm rem},{\rm out}}(v^\#)^{-1}
       :H^{q_0}\to H^{q_0}\|<2^{-400000}.
 \tag{N.2}
$$
这是两个独立外门：前者给局部有界型，后者给经过全部真实有限
connector/Poisson 后的全网端口；不能从前者自动推出后者。
两者均不由 $\mathcal A_{64}$ 小推出。
K 的定义使 (N.2) 涉及外 state 的1856阶和 physical height
的1858阶；不能将后者改称 state 的1856阶。
固定原真实外行时，直接沿用 I 已有的对应门和已知系数界，
不另声称它是任意附近帽的 nonlinear inverse。

在角阶 $q$ 上，下文只调用 K 到 $q+16$：
两侧 $4/3$、半阶平衡、adjoint 和整数 ceiling 用至 $q+4$；
其余12阶是 rank/Poisson/固定坐标转换的余量。
K 自己的输入已经含 $+32$、physical height 含 $+34$。
所以最高调用是 $\mathcal A_{8144},\mathcal D_{8144}$，
state8176、height8178，均小于8192。
尤其没有调用 K.8160 后悄然使用 height8194。

置
$$
 \mathfrak H_q
 =1+\mathscr R_{q+64}
       +\mathcal A_{q+16}+\epsilon_L\mathcal D_{q+16},
       \qquad q_0\le q\le8128 .
 \tag{N.3}
$$
固定外行的对应数值视为已知有限系数。
常数1使固定 radial、浅前缀和原 affine 图的已知费用也包含在内。
它从不进入下文 small gate。

$\mathfrak B_q(d_{\rm ext})$ 始终指 I 的完整外源范数，
另按 K 的真正 source 映射读入：
screened curvature 列保 $s_B\epsilon_L\mathcal D_{q+16}$；
cap 的两个 mean、physical mean-height $a w(L)/165$、
独立 $f_*^{\rm src}$ 和 Robin source 列保
$\mathcal D_{q+16}$，不乘 $\epsilon_L$。
所有实角、scalar/density 的两种 Piola、good/raw transport
均按已证各自合同支付。这一定义不授权把未知 cap high 列删掉。

设
$$
 \mathfrak d_q(g,d_{\rm ext})
 =\mathscr N_{q+2}(g)+\mathfrak B_q(d_{\rm ext}).
 \tag{N.4}
$$
$\mathscr N$ 是原 fixed-$t$ ordinary 物理源，含真实 mean；
不是 mixed 图中逐曲线取值的未知函数。下文原子/切口荷沿
$\mathfrak B$ 的单侧 trace、BV 合同，不从 $L^2_r$ 猜 trace。

## 2. 最高未知系数与高背景必须分开

取物理频率 $m,n,\ell\in4\mathbb Z$，$\Lambda_m=(1+m^2)^{1/2}$。
对整数 $q>0$、$m=n+\ell$，近带
$|\ell|\le\Lambda_n/(2q)$ 给
$$
 (\Lambda_m/\Lambda_n)^q
 \le \exp(q|\ell|/\Lambda_n)<2.
$$
远带给 $\Lambda_n<2q|\ell|$、
$\Lambda_m<(2q+1)|\ell|$。完整 signed Young 卷积于是给
$$
 \|a u\|_{H^q}
 \le2\|a\|_{\mathcal A_0}\|u\|_{H^q}
 +2(2q+2)^q\|a\|_{H^q}\|u\|_{\mathcal A_0}.
 \tag{N.5}
$$
同样，近带均值定理给
$|\Lambda_m^q-\Lambda_n^q||n|
 \le4q|\ell|\Lambda_n^q$；远带将全部高权转给 $\ell$，得
$$
 \|[\Lambda^q,M_a]\partial_\theta u\|_2
 \le4q\|a_\theta\|_{\mathcal A_0}\|u\|_{H^q}
 +4(2q+2)^{q+1}\|a\|_{H^{q+1}}\|u\|_{H^2}.
 \tag{N.6}
$$
$q=0$ 使用原 Young 界，commutator 准确为0。
$\partial_\theta$ 的输入 mean 准确为0，不意味着乘法输出 mean
或独立 mean 行为0。半阶窗用两相邻整数的同一 Hilbert 插值；
负窗用真正 adjoint，不能用非自伴图的假酉性。

(N.5)–(N.6) 的关键是第一项只含低系数。
例如真实 transport $u_t=a u_\theta+a_\theta u/2+f$ 的高阶能量中，
最高未知的积分系数可取
$8(q+1)\|a_\theta\|_{\mathcal A_0}$；
高系数只乘 $\|u\|_{H^2}$。低阶流早已存在后，对其有限 Fourier
regularization 作该能量估计、再取极限即可构造同一个高阶解；
不先假设高阶 evolution 有界。

uniform layer 的次序也要明确。若有正 profile $p_j$ 且
$\sup_j\|a_j/p_j\|_{H^{q+2}}\le A$，则逐系数
$$
 \sum_{\ell\in4\mathbb Z}\Lambda_\ell^q
              \sup_j\frac{|a_{j,\ell}|}{p_j}
 \le A\sum_{\ell\in4\mathbb Z}\Lambda_\ell^{-2}<2A.
 \tag{N.7}
$$
这是明确消费两角阶；不是将
$\sum_\ell\sup_j$ 免费换成 $\sup_j\sum_\ell$。
全部 C.44 型 envelope 和原层权的正 Schur 求和都先用 (N.7)。
以下 $+64$ 背景余量包含这两阶。

## 3. 同一个真实图的 tame 费用

L.18–L.22 的 GN/Hölder 证明给 $k\le8192$ 的完整 one-high
composition/inverse 估计。每个 Faà 项的正导数总阶为 $k-1$，
Hölder 倒数和为 $1/2$，插值指数和为1；Young 后恰有一个高因子。
因此 reciprocal、密度、平方根、真实图和逆图的高范数依赖
当前高背景是线性的，而不是高范数的 $k$ 次幂。

对实际 root、strict、principal 及其反向图，先去径向平移。
低阶真实图在 (N.1) 下给 Jacobian、其逆与密度正因子在
$[1/2,2]$，所有路径均是旧证明同一个真实路径。
(N.6) 使其高阶 transport 的最高未知系数只收
$8(q+1)\int\|a_\theta\|_{\mathcal A_0}$。
原低 profile 和 (N.1) 使该数小于 $1/8$，包括 $q=8128$。
这一步不要求高范数小；同一个流、其逆及 adjoint 都得到
$$
 \|\mathcal C_Wu\|_{H^q}
 \le2\|u\|_{H^q}
   +C_q p_j\mathscr R_{q+40}\|u\|_{H^{q_0}} .
 \tag{N.8}
$$
这里 $p_j$ 是原相应图的 $J,\delta,C^\#$ profile，
不是一个新径向权。需要 primitive 的 composition 差继续是
原 S.20–22 的 $L_HB_HR_H$，其中
$R_H:H^q\to H^{q+1}$。这个真实一角增益支付差图微分的一角损失；
不能将裸 $C_F-C_G$ 当同阶小算子。

跨符号部分另用原有限非驻相式：
$$
 |(\mathcal C_F)_{mn}|
 \le4^r(r!)^2|n|\varepsilon_r(|m|+|n|)^{-r-1},
 \qquad mn\le0,\quad(m,n)\ne(0,0).
 \tag{N.9}
$$
不能直接把 (N.9) 的 $C^r$ 小量替成一个任意大高范数。
这里用一个更明确的 integral 版本。内部各真实图先去径向平移后，
I/L 的低门给 $\|\eta'\|_{\mathcal A_0}<2^{-32768}$。
外帽已知实角不冒用这个门，它已由 K 的完整 kernel 合同单独收费。
在跨符号区 $|n-m|=Q_{mn}$，故
$g=g_0(1+t\eta')^{-1}$，$g_0=\pm1$、$|t|=|n|/Q_{mn}\le1$。
完整 Fourier 幂卷积给
$\|z^k\|_{H^r}\le k^r\|z\|_{\mathcal A_0}^{k-1}\|z\|_{H^r}$。
由 $k\le2^{k-1}$ 和 $r\le8192$，完整 Neumann 和给
$\|g-g_0\|_{H^r}\le2|t|\|\eta'\|_{H^r}$；没有第二个未付阶乘。

非驻相多项式各项有 $r$ 个 $g$ 因子，总导数 $r$，
非负系数和准确为 $r!$。零导因子用 $|g|\le2$，
正导因子用 L.18 对 $g-g_0$ 的 GN/Hölder，正导总数仍为 $r$。
插值指数之和为1，其余低范数因子不超过1。
因此完整积分的 one-high 常数可取
$2^{33r+2}r!(r+1)^{2r}|t|\|\eta'\|_{H^r}Q_{mn}^{-r}$。
这一步保留了 GN 的全部费用，而非将它藏入旧 $C^r$ 门。
非径向 amplitude 的 Leibniz 也按同一个总导数和分配，
radial amplitude 单独保留；所有新增有限计数下节明确收费。
取 $r=q+24$，真实远行、远列和给
$H^{q_0}\to H^{q+20}$ 的高背景项；
对低窗使用原 $r=q_0+24$ 的小量。
没有从 (N.9) 声称完整多图余核具有 exponential lag。
$n=0$、$m=0$ 的准确有限边与两个独立 mean 依原式保留。

若 polar defect 或零边界型的低窗 Neumann 小于 $\varepsilon$，
高窗 estimate 的形式为
$$
 \|Eu\|_q\le\varepsilon'\|u\|_q+B_q\|u\|_{q_0},
 \qquad \varepsilon'<1/2 .
$$
先用低窗真逆得到 $u_{q_0}$，再对有限级数逐项求和：
$$
 \|(I-E)^{-1}f\|_q
 \le2\|f\|_q+
 \frac{2B_q}{1-\varepsilon}\|(I-E)^{-1}f\|_{q_0}.
 \tag{N.10}
$$
同一 argument 适用于 inverse square root 的绝对级数。
没有在高窗假设 $\|E\|_{q\to q}<1$；大 $B_q$ 不是反馈系数。

## 4. 有序乘积只准一次高背景

为记录计数，称一个实际 map 有二层界，如果
$$
 \|Tu\|_q\le t_0\|u\|_q+t_q\|u\|_{q_0},
 \qquad \|Tu\|_{q_0}\le t_*\|u\|_{q_0}.
$$
准确乘积满足
$$
 (ST)_0=s_0t_0,\qquad
 (ST)_q\le s_0t_q+s_qt_* .
 \tag{N.11}
$$
第二项不用 $s_qt_q$。有限 word 的高费用是逐位置插入一个高因子，
其余全取低 norm；有序 Volterra 级数同样在每项选择一个位置，
$n$ 项计数由 $n\varepsilon^{n-1}$ 求和。
这就是下文所用 tame 组合，不以“光滑依赖”替代量化证明。

原 strict 的 order-one drift 先由真实 density flow 准确消去。
然后用完整 primitive、径向 Fourier-diagonal propagator 及
原 interaction-picture Picard 方程。低 norm 保原
$G_i^2\int\|\Delta A_i\|<1/64$；高式用 (N.5)、(N.8)、(N.11)，
唯一高系数乘已得到的低解。根内先用原 radial Airy kernel 与
完整零阶势差的 Volterra 方程，次序完全相同。
因此先有原 W.26 的完整 Cauchy 子乘积
$2^{8192}\lambda_i^{12}$，之后才用 anti-$J$ 四个 block 恒等式
构造 scattering；绝不先借待证的高阶 scattering norm。

正区使用同一个真实零边界型、Piola、Robin mean 和独立源列。
其系数最高项按 (N.5) 分配；低能量 Neumann 由真实相对型提供。
高项是有界型中唯一高系数乘低解，按 (N.10) 求和。
对真正 adjoint 另作同样构造。
原 complete contact 恒等式和
$R_{\rm adj}=R_a^{-*}$ 不变，不能用实际 $R_a$ 的酉性替代它。

高输入 trial 仍为真实 normal-trace 归一
$c\kappa^{-1/3}\operatorname{Ai}(\kappa^{2/3}y)$。
$y^3\kappa^2u$ 的完整平方积分给 $L^2_y$ 的
$\kappa^{-2/3}$，后续 $H^{-2/3}$ 给 $4/3$；
所有 Airy/Airy'/Airy'' 平方矩、两 cut 和 mean 源均保。
(N.11) 只分其系数与解的角阶，未改变任一径向积分或其 $b$ 次数。
低 trial 为0时，高输入恒等式两边仍右乘 $P_H$；
低输入保真正的 $(R_a+I)P_L$。

## 5. 确定的有限角常数

低窗 $q\le q_0$ 最多使用 $q+64\le1856$。
原 I 的 $B_{\rm fin}=2^{229376}$ 足够；原 proof 写2144是上限，
实际展开只到 $q+32$，不是必须使用2144阶背景。
正区外门用 (N.2) 或原固定外行的已付同一窗。
因此原 low Cauchy、gap、mean 商及全部谱选择不变。

高窗取 $r\le8192$。AM–GM 给
$$
 r!\le((r+1)/2)^r\le2^{12r}(1+1/8192)^{8192}
                       <2^{12r+2}.
$$
旧非跨符号组的三个阶乘、finite 分拆与四倍角可取
$2^{40r+8198}$。跨符号 one-high GN 必须另付：
$(r+1)^{2r}<2^{26r+3}$，所以上节的完整积分常数小于
$2^{71r+7}$。amplitude 的 Leibniz、density 恒等式、
有限 mean 边、signed 双 Schur、包络两阶与固定计数
可共同宽取 $2^{80r+16384}$，支配前一种组。
C 的三径 residual 及四态 Nemytskii 改用 L 的
one-high 级数，而非 C.9a 的高范数小门；其实际分母的低下界相同，
高系数费可宽取 $2^{262144}$。
故内部单个 finite 角组不超过
$$
 2^{262144+80\cdot8192+16384}=2^{933888}<2^{1048576}.
$$
K 在所需窗的 $C_q=2^{96q+16384}$、其真 adjoint 和 rank
已经包含各自完整有限角组合，不再乘一次上述 Bell 费用。
将内外最大值、真实 source 坐标和固定端因子统一取
$$
                         B_{\rm hi}=2^{1048576}.
 \tag{N.12}
$$

第一参数及首同调的高费用另列。
L 给同一个 principal conjugacy 的高系数
$2^{1310720}\kappa_i^{-1}J C_i^\#\mathscr R_a$。
inverse、其 density、协变 scalar 首系数、两侧已知真实图之间的
有序转换至多八次 L.19 的 composition/inverse；
它们用 (N.11)，不是八个高背景相乘。
每次 $q+32\le8160$，可收
$2^{90(8192+4)}$。加高系数262144、primitive/同调和角归一
32768，有
$$
 1310720+8\cdot90(8192+4)+262144+32768
       =7506752<8388608 .
$$
因此原 I.10 的高系数位置可以统一使用
$$
 \epsilon_{i,\rm hi}^c
 =2^{8388608}J^{16}\delta^{-16}C_i^\#
                      \mathscr R_{q+64},
 \qquad
 \epsilon_{o,\rm hi}^c=2^{8388608}\mathscr R_{q+64}.
 \tag{N.13}
$$
$\kappa^{-2}$、真实 finite outer $\kappa_o^{-2}$ 和
$\beta_{\rm rad}$ 的层次数仍在 $J^{16}\delta^{-16}$ 中；
它们不因角阶增加变成新的 $\delta$ 次数。

(N.12)–(N.13) 是高强迫的常数，不能放进 low Neumann 门。
最高未知一侧使用 (N.5)–(N.8) 的低系数；
局部双 buffer/Picard 的额外固定因子小于 $2^{64}$，
完整 word、正逆/伴随、有限端口和 signed Schur 合起来
可统一宽放 $2^{32768}$。
这包括32个原 seam/word 位置、每处最多64个常数2因子、
两次相邻窗恢复及 mean/rank 端项；径向 Fourier multipliers
准确交换，不额外乘一个 $B_{\rm hi}$。

## 6. 原 cutoff 保持不变

继续使用 I 的局部 root cut
$L_i^\flat=2^{376832}\lambda_i$。
最高未知的双 buffer feedback 是
$$
 2^{2217+229376-(2/3)376832+64}<2^{-19500}.
 \tag{N.14}
$$
完整一次与二次 Volterra 的高背景只在其真实 forcing 中出现。
没有取 $L^\flat$ 为 $\mathscr R_{8192}$ 的函数。

其后保持原全网
$$
 T_j^\#=\max(2^{2097280}J_j^2\delta_j^{-9},2^{2105344}),
 \quad v_j^\#=2^{-1200000}J_j^{-4165}\delta_j^{1073/32},
 \quad F_j=2^{4096}J_j^4\delta_j^{-5}.
 \tag{N.15}
$$
真实 $\beta$ 与第二冻结参数的 high gap 来自低球，不变。
完整强余项的 tame 形式为
$$
 \|\mathcal R_i u\|_{q+4/3}
 \le 2^{557056}\lambda_i^{4/3}\|u\|_q
 +2^{12582912}\lambda_i^{4/3}\mathfrak h_{i,q}
                                      \|u\|_{q_0},
 \tag{N.16}
$$
真正 adjoint 及另一源窗同式。
$\mathfrak h_{i,q}$ 是 (N.3) 对应的本地 profile/high 因子。
第一常数是 $524288+32768$；
第二常数涵盖两个 finite 角组、(N.13)、完整 word 和 source
恢复，按 (N.11) 每项仅一次 high。
mean 与低入高出均在式中；不能把 (N.16) 缩成高高压缩。

最高未知 high feedback 从原 $2^{-174000}$ 最多增加32768 bits，
仍小于 $2^{-140000}$。因此同一个 high inverse、两侧 Poisson、
adjoint 和所有相邻权比不超过 $2^{256}$ 的权继续存在。
高背景的 Poisson 系数由准确 inverse identity 与 (N.11) 得到，
只乘已知 low solution；它不改变上述反馈门。

## 7. 有限 middle 与真正无限 deep

三项有序 finite 角组从 low 到 high 的增加为
$$
 \Delta_{\rm hi}
 =3(1048576-229376)+(8388608-950272)
 =9895936 .
 \tag{N.17}
$$
所以原完整一角差的高系数可收
$2^{11634872}J^{40}\delta^{-47}C_j^\#\mathscr R_{q+64}$。
这里比较仍是同一个 unitary 表示；真实 primitive 消一导后，
准确完整 Cauchy word 有序插入，沿旧 I.17 的三个位置分组。
高背景不会让 scalar diagonal 或实际 profile 消失。

deep 投影仍是
$P_D=\mathbf1_{\{j\ge8193,\ 0<|m|\le2^{-40}\delta_j^{-1/8}\}}$。
必须先用原准确式
$$
 \Delta S_HP_D=[I,F_{H,W}]\Delta\widehat U P_D,\qquad
 P_D\Delta S_H=P_D\Delta\widehat U[I;E_{H,W}].
 \tag{N.18}
$$
因此这里只收 $A_j=2^{-40}\delta_j^{-1/8}$，不是 $T_j^\#$。
high 消元后 long-range 部分由两侧 Poisson 支付；
不能说消元后仍是有限邻接。

剩余完整 Schur 差还是
$$
 \Delta S_H=[I,F_{H,W}]\Delta\widehat U[I;E_{H,\circ}],
 \qquad
 \Delta S_{\rm rem}=[I,F_{D,W}]\Delta S_H[I;E_{D,\circ}].
 \tag{N.19}
$$
低最高未知收费原 I 的三段和再加32768 bits，故总小于
$2^{-300000}$。高强迫沿同一正 profile 求和：
$$
 \begin{array}{c|r}
 \text{去掉 }R_0\text{ 后的 high coefficient}&
                 \text{binary exponent}\\ \hline
 \text{direct remaining}&7725696+9895936=17621632\\
 \text{三个 deep 项}&5628444+9895936=15524380\\
 \text{有限真实 outer}&6810328+9895936=16706264 .
 \end{array}
 \tag{N.20}
$$
真正深余量仍为 $75/256$；首端、缺失邻项、三段 profile 和
65536层后的真实几何比沿原逐行求和。
(N.7) 先建立完整 angular envelope，所以这里不是逐角 norm
supremum 代替完整 signed 双 Schur。

全部 high inverse/Poisson 的一次高插入、两层 source 和固定端
再统一收进 $2^{20971520}$。这一数比表中最大项多3349888 bits；
除局部 strong (N.16) 的12582912外，后续只用已经小于2的
最高未知 inverse 和原不超过 $2^{130}$ 的 deep Green/Poisson，
以及32768 bits的固定有限变换。因此该余量不依赖层数。
无限 word 用原有限穷尽、共同正 profile majorant 和 low
唯一性取极限，不把“有限窗口2n”当无限谱流计数。

## 8. 完整 mean、源列和二层逆

先在 low 窗定义真实解。保原径向 generalized inverse、
物理常高度核 $c_\circ$、独立 source $\sigma_\circ$、真实 height
functional 与 closed mean 商。remaining 的同一个径向比较 inverse
满足 $\|v^\#R_\circ v^\#\|\le1$；(N.19) 的 low 小门给准确解。

在高窗，对同一个有限穷尽解用 (N.10)；最高项由
$2^{-300000}$ 吸收，高项只乘 low 解。
由共同 bound、弱紧性及 low 唯一性，所有穷尽得到同一个解。
反向也是同一真实源域与同一 height gauge，不只是注入性。

source 的顺序逐字保持：
$$
 k_L=g_L+F_Hg_H,\quad
 k=k_{\rm rem}+F_Dk_D,\quad
 x_D=E_Dx_{\rm rem}+R_Dk_D,\quad
 x_H=E_H(x_{\rm rem}+x_D)+R_Hg_H .
 \tag{N.21}
$$
每个 block 用 (N.11)。weak 外源不能借内部 $P_{L,\rm int}$
的 $\Omega_H=1$；$s_B\epsilon_L$ 与 unscreened mean/height
列继续使用第1节原单位。

原 ordinary fixed-$t$ source 的最高项费用可以统一宽放为
$2^{3407872}$，weak graph/source 读出为 $2^{2359296}$。
前者相对 $2^{3145732}$ 有262140 bits，后者相对
$2^{2097156}$ 同有262140 bits，足收本篇最多四个32768组及
所有两窗/完整 mean/source 固定因子。
source 的高背景项沿同样一次高插入收进 $2^{20971520}$。
root 的所有真实源位置到两 cut/root 端的有序 Duhamel、mean
和反向窗仍是 Kfixed-t 原合同；不将一个单向耗散界当完整两端源列。

## 9. canonical 强径向读出

令
$$
 q=s+1728,\qquad64\le s\le6400.
 \tag{N.22}
$$
原 weak 读出是 $H^{q-12}$。为了恢复四态 $H^s$，high 部分
只需 $H^{s+6}$，故余量1710。
其实际层幂
$$
 1710/8-80-131=11/4>0
$$
不变。首切口 $\delta^{-211}$ 只收 $M^{1688}$；
从 $H^{q-12}$ 到 $H^{s+5}$ 仍余23阶。
每个 Fourier 模的真实 first cut 唯一，所以原 $\ell^2$ 首迹估计
保持，不增加一个额外层数或 $\sup_m$。

低锥的两真线、移动基 determinant 比望远镜与
$r_4=512/1023$ 都由低系数保证；
其高角微分再次只在准确向前/向后 recurrence 中一次高插入。
两个解相减的弱唯一性仍使用 $\delta^{100}$，不能先假 strong。
ordinary mean 的 Volterra/height 重建保完整
$\chi_t=12\mu_jr^{-4}\langle A_0g\rangle$；
body channel 的 flat-end $\chi=0$ 不清零外部 affine flux 荷。

有限129–8192前缀仍用原
$\mu_j/\varepsilon_s\ge\delta_j^6$、$C_j\ge\delta_j^4$、
$2^{16}\delta_j^{-92}$。实际 weak first-cut bits 为
$2359296+211\cdot8197=4088863<4300000$；
加 mean、有限前缀、真两行和四态读出统一取 $2^{4500000}$。

高阶 canonical 系数的所有 one-high 项仍乘已经取得的 low 解；
同一个 $75/256$、$11/4$、23阶及 $\delta^{100}$ majorant 逐项可和。
它们不以高背景改变真锥、gap 或 first-cut 定义。
因此得到确定的完整 tame 估计
$$
 \boxed{\ 
 \|h\|_{\mathscr Y_s}
 \le2^{8388608}\mathfrak d_{s+1728}(g,d_{\rm ext})
 +2^{33554432}\mathfrak H_{s+1728}
                   \mathfrak d_{1792}(g,d_{\rm ext}),
 \quad64\le s\le6400 .
 \ }
 \tag{N.23}
$$
第一数包含 $3407872+4500000=7907872<8388608$；
第二数包含
$20971520+3407872+4500000=28879392<33554432$，
其余两次有限插入和 mean/readout 被差额4675040 bits覆盖。
原 low 解另满足同一背景小门下的统一
$\mathscr Y_{64}\le2^{8388608}\mathfrak d_{1792}$；
不能把 (N.23) 中的大 high 项拿回去做 low 门。

$s<64$ 用这一已付 low 解及嵌入，不提高 low source 要求。
(N.23) 的 source 损失是1730，背景最高为 $s+1792$。
没有给一般 St 源新径向衰减，没有把有限角输出转成 analytic224。

## 10. 第一参数反馈的同一个低阶 Schur

G 的真实 D8 functional 由 L 的低值图导数识别，仍有
$2^{8960}\mathscr R_{20}$ 的低方向系数。
只在真正 holonomy-one tangent 上作这个 nonlinear 识别；
一般有荷数据保 G 的 projected-feedback 定义和其独立 affine
principal-charge 列。

原完整 metric 列是
$$
 B_pv=\Pi_{A_0}\{c e_{\psi,\rm rem}
                         +c(F_K-2Q)\ell-\psi N\}.
 \tag{N.24}
$$
它的 $c\ell_t$ 与 $2cQ\ell$ 是径向常数，准确被 $\Pi_{A_0}$ 消去；
这不删除真实 ordinary mean、height 或外端两迹。
G 的六邻胞、$\psi_t$、physical $\gamma$ 单位与三个 profile
全部原样保留。

对 (N.24) 重做一次 N.5 与 L 的 one-high Moser，
原 G 的 profile sum 仍是86000/165000/200000 bits，
不改变三个 $\delta$ 次数。高系数262144加原 functional、行单位、
两个乘法的 $(2q+2)^q$ 和有限项，宽取
$$
 \mathscr N_q(B_pv)
 \le2^{1048576}\mathscr R_{1856}
        (1+\mathscr R_{q+8})\|v\|_{\mathscr D_8},
 \qquad q\le8130 .
 \tag{N.25}
$$
更低窗继续使用原 G 的二次小量
$2^{524288}\mathscr R_{1856}^2\|v\|_{\mathscr D_8}$。
这里不是把旧 G 的2114窗直接改名；高窗使用的是显示的
one-high 乘积和同一已付 profile sum。

形成 low Schur 时明确从已经证明的 $\mathscr Y_{64}$ 读取
D8 functional，而不调用一个未另证的 $s=8$ 尖窗。
由 (N.4)、(N.23)，所需 ordinary source 是1794阶；
(N.25) 该阶的背景为1802阶，两者都落在1856内。
原 low D8 读出和二次小量给反馈小于
$2^{-7900000}$，其真 inverse 小于2。
这里 D8 读出在 (N.23) 粗化前可取 $2^{7907872}$，
故实际 exponent 为
$7907872+524288-2\cdot8192000=-7951840<-7900000$。
高 equation 使用同一个已解的 low 参数值；
将 (N.25) 作为明确 source 列代入 (N.23)，再按一次高插入求和。
因此在最高常数 $2^{33554432}$ 再增加一个确定 factor2 即可：
完整 projected 第一参数 feedback 的 (N.23) 第二常数统一改为
$$
                              2^{33554433}.
 \tag{N.26}
$$
第一常数也统一取 $2^{8388609}$。
没有把高参数范数放进 low Schur，也没有再对 $\mathcal E_N$
作 derivative-losing Neumann。

参考 metric 的真实 lift $H_p$ 及两个高度迹依 G.28–29 独立恢复；
它不强塞 fixed-metric $\mathscr Y$ 中。所有 body/outer source、
$\nu$ 独立列及两 $\Gamma$ 的原身份不因该 lift 改变。
第二参数仍固定已知值；本篇不是最终 $\nu$ 或第二相位 Schur。

## 11. 高低非线性余项及尚须完成的接口

$\Pi_{A_0}$ 的输出修正是一个**常数函数**，
所以其任意 $H^s$ norm 只用低 scalar functional norm；
不能在此制造高 $A_0$ 导数费。
由原 O 的
$\alpha=J^{-1}+3q(1+K)/D$、
$\beta=(1+q)/J$、$\gamma=3q(1+K)d/D$，
没有 $Q$、$1/c$ 或 $1/\mu_j$，得到
$$
 \begin{split}
 \mathscr N_s(\Pi_{A_0}\mathcal E_Nh)
 \le2^{1048576}\{&
 \mathscr N_{s+1}(N)\|h\|_{\mathscr Y_8}
 +\mathscr N_9(N)\|h\|_{\mathscr Y_s}\\
 &+(1+\mathscr R_{s+8})
       \mathscr N_9(N)\|h\|_{\mathscr Y_8}\}.
 \end{split}
 \tag{N.27}
$$
原真实 $C_j^\#\le2^{256}C_j$、全层 $\sup C_j<2^{-12}$、
浅外 connector 与 T.27 的无 $Q$ 恒等式全部保留。
(N.27) 最高输入 $s+1$ 的真实角损失没有删除。

同样，真正 mean retraction 后的 quadratic 源具有
$$
 \mathscr N_s(g_{\rm quad})
 \le2^{1048576}\{
   \|h\|_{\mathscr Y_8}\|h\|_{\mathscr Y_s}
  +(1+\mathscr R_{s+8})\|h\|_{\mathscr Y_8}^2\},
 \quad s+8\le8192 .
 \tag{N.28}
$$
这是完整物理源，含 mean：先 $P_\perp$ 消去 radial
$\Delta\kappa_2'$，再用准确 $\Pi_{A_0}$ 恢复其 ordinary mean。
原 R.33 的二次 profile 和深净 $103-10/256$ 保持，不将
pure mean 从未投影的 $c_j$ 中粗估。

(N.27)–(N.28) 仍不构成一个已经完成的 Nash 迭代。
必须另外给：真实 reduced derivative 的
$-\mathcal E_N$ 接线或合格 approximate inverse，
每步 mean/height/第一参数的重建，三径 source jets 的闭包，
以及实际初残差与所选平滑序列的数值余量。
本篇只提供已经闭合的 full-network 二层逆，而不把这些剩余门
写成“自动 tame”。

为防最高背景阶数被后续径向恢复偷加，预先固定下一项的允许范围：
若四态要四次 scaled 径向导数，ordinary 源须三次真实径向导数；
从本篇在角阶 $s+4$ 读取，source 为 $s+1734$，
背景为 $s+1796$，因此只能取
$$
                                s\le6396 .
 \tag{N.29}
$$
本篇尚未据一句 PDE 代回授予这些径向范数。
必须按真实第一阶两行、完整 scalar mean、$c_j$ 的前三导、
所有 source 跳及 metric lift 逐项写出；未知 fixed-$t$ 源不能
无偿拉到 tilted Airy 图。