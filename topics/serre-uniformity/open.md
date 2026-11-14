# 未解决的问题

**R575现行更正。** 实际六层的正CM角色为Ψθκ4，根号−1、中心值零；R348把相反扭向Ψθκ4^-1识别为实际商的论断撤回。后文及历史归档中的该出现性、实际秩零与有理点零像应用均以[R575](results/R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)为准。固定家族的L值与局部代数计算仅按各自假设保留。

## O1：主要目标（OPEN）

证明绝对常数C，使所有无CM的E/Q、所有p>C的模p表示满射；或构造p→∞的完整反例族。等价的主要剩余情形是完整非分裂Cartan正规化子，不再以已由Furio–Lombardo排除的指数3子群为主目标。单p、有限层、条件结果与导子下界均不满足完成标准。

2026-11-13压缩前的完整开放问题、已关闭支路、全部公式和文献边界逐字归档于 [前版open](notes/2026-11-13-open-before-first-canonical-disk.md)。以下保留当前可执行缺口；归档不撤销任何已证结论或限制。

## O2：完整正规化子的高度与有理点

R4排除通常Runge捷径：所有含−I子群覆盖及继续扩域，最小提升域的尖点轨道数恰等无穷位数。须有新的全局信息。R101/R109独立完成p41/47/59/83的全部尖点约化/实分支及169候选，四层有理整j仅CM；一般层与非整j仍开。不能调用有gap的BBM全p≤97分类；公开代码审计不能冒认原gap原因。

## O3：实际Frobenius的统一小素数

真正所缺：为实际异常族找到q<p²/4、商二次特征ε(q)=−1且a_q(E)≠0。R2/3/6/7说明任意固定有限窗口仍可由满像曲线实现；R41/52的正密度依赖导子，不能代替首素数上界。R15/20/119给商域互反及分歧q≡1mod4时q≥p²+4，仍无判别式上界。历史见notes/2026-11-12-open-local-frobenius-history.md。

## O4：二次自扭曲、真实三次角色与共同导子

R5商域虚二次、p惰性，统一排除非平凡二次自扭曲间p挠点同构等价主目标；Frey–Mazur不是已证输入。平方惯性分支R58/61–67给有效类关系及D必要下界，仍无D上界。严格小惯性I_p=C³、p≡2,5mod9；R66的实际三次环类导子M=Dc²不可自由更换。

R69/72的非零中心值给实际秩零商及整性；R80/81、R83/86/87给明确非消失范围。R90–93已排hK=3,c=1；R113/115/118证明h3/6/9/12全部实际周期非零，四小层这些分支已排尽，不重开。一般共同中心零及h≥15仍可能。

R137/142/150/153/156给同一尖点和实际谱下分母D的Norm整除、D²/D³乃至满jet条件下D⁶整除；仍不控制分子、变化M或共同中心零。唯一非零谱为有理形式的分支只有Mh(O)下界。有限三点/三阶张量与Gauss和单位性不能代替指定两个Fourier投影的共同非零；已有q=5^203、ell811实际共同零边界，必须用素数性或实际ell>p。

R166/169/172–177建立实际尖点型商、整交格、非零中心值到有限像及原始两行接口。R181/182补全r>4和阶四类型；合数m仍不能用坏方块自动可逆捷径。R214共同p外导子a=bc、(b,c)=1、(bc)_D|36，但b奇部可随III/III*增长。

R236/238修正二次扭曲正投影；R249经CM Hilbert诱导、明确辅助惯性本征值1/(1+ell)及Nekovar B(c)闭合CM中心值有限商接口。全部分支的统一有效条件为

$$p\ge C_\epsilon(M^*)^{1+\epsilon}/h(bc)\Longrightarrow j(E)\in\mathbb Z,\qquad M^*=D(bc)^2.$$

有效系数2592；Siegel平方根化简一般无效。非整M*≳p^(2−δ)，R229/232/233/245的c、bc和新支撑下界均不能反用成上界。八个hK1且K≠−3的bc指数1.5969787214；K=−3非平凡σ给b≳p^(2√e)。当前推进整j真实判别式三次角色的联合检测及K=−3、σ=1的有理六次CM参考、相同实际小挠点商域。须继续变化D,b,c的上方控制或统一排除。

## O5：固定层41已完整分类；一般层仍开放

[R707](results/R707-complete-level41-rational-point-classification.md)已从现存完整原证明和公开R709结果重建全部129盘：19普通=16排除+3CM，110超奇异=105排除+5CM。$X_{\mathrm{ns}}^+(41)(\mathbb Q)$恰为八个CM点，判别式−3、−7、−11、−12、−19、−27、−28、−67，无有理尖点。每个保留点的精确j、真实level盘、坏标签、简单根唯一性均完整连接；不依赖遗失R583摘要。

此固定p41子问题关闭；[129行来源账本](notes/R707-all129-disk-ledger.json)和[105盘执行表](notes/p41-SS-disk-progress.md)保存全部索引，原长链/Norm/连接/全尾无需重跑。一般层仍须真实秩受控商、实际全局高度和统一排除，不能从一个有限层外推绝对一致性。此前完整执行状态保全于[分类前open](notes/2026-11-14-open-before-R707-classification.md)。

## O6：固定CM参考及真实高阶障碍

固定A:y²=x³−x，R16/19把非CM同余完整化为三族原始整数解X³−27W²=cZ^p及全部互素/奇偶条件。p≡1mod4已排，余p≡3mod4。R114/128最大奇同余层m|pg；R127/129已完整关闭九次幂支，R130排49|g并给固定m≥7的有限B_m。当前仍是g=1、g=3及变化大3mod4因子，立方不自动升九级。

R139全部奇层尖点仍单轨道；R143所有实际惰性Weil扭曲正维商中心L值为零，不能找秩零商捷径。R146/149：s=0时实际曲线解析秩0与Sha有限；s>0只知v_ell(Lalg)≥n而非sn。R152幺幂整余核最小挠长度n不能靠换格消掉；所核Jochnowitz和p-converse不满足本题局部条件。

R37/40–46/51给真正三次类群/射线类群覆盖、原始指标Thue–Mahler、Selmer与MW交空间、恢复R19整数谓词。类群非零及局部可解不是矛盾，须控制变化支撑的交空间、真实分母和幂条件。387bit旧R53实例已由R88/95完全排，不能再列开放。R32/34仅给依赖支撑的原始点深度界；已有高秩反例说明不能省略完整分母支持。

变化CM参考由R21/24规范化，R25/29/31/36/38完整二三进惯性、辛符号已相容；不得把固定A论证套变化扭曲。R44的惰性参数约束有真实内容，但整j时Hasse元素Norm已自动，不添独立类群矛盾。所有先前精确公式保留在前版open及相应results。

R157/158实际反循环角色迫支撑R超多项式增长，仍是下界。R161/163严格Selmer为零、Robert单位统一生成唯一对偶线，但局部S_q可为零且多支撑可相消；必须连接实际曲线额外关系或上界。

R171固定p43、776bitq的真实自局部λq=16已算，但该q早被Gaussian5排。R176/180的条件flat塔仍需实际晶体迹t=0与有理整数迹。R191/196/198/200/201补真实射线Norm域、参考抵消和S-unit存在性，准确Ω₂=ε(10−L)，R202仅留实际L。R204真实参考Frob和R207严格43次整模型已完成，不重跑CRT。

R219真实忠实普通U及H90接口，原像X须生成上域实子域（次数1892）；真K子域乘积/43次幂不能产生。R239给V7/V42等明确小目标；R243以完全饱和单位求元素Norm核三维，仍非上域普通单位Norm。R250精确射线Γ作用与长度2结构已证，ρ/长度/L仍未实测。普通非单位见证外支撑正Artin修正不可省。继续忠实Norm或等价后阶可积性；小11次特征结果不能代替χ±1。

## 当前执行与精确缺口（R742、R741、R738、R736）

压缩前全部公式、来源及路线边界保存于[完整检查点](notes/2026-11-14-open-checkpoint-through-R721.md)；
以下以最新已证接口继续，已完成计算不重跑。

### 原变化导子与指定本原非消失

原 R317 剩余为 $p>37$、$p\equiv2,5\bmod9$、$a^3+db^3=1$、$p\mid b$；
$D,b,c$ 无统一上界，R604 的 even 支撑下界不能倒用。
R575 的原正商是 $\Psi_\theta\kappa_4$、根号负；
R597 的 $X_1/c_1$ 与 $X_d/c_0$ 不可自由互换。

[R616](results/R616-original-CM-point-difference-and-explicit-height-basis.md)
给原 $\beta=q[c_1-c_0]$ 非挠当且仅当指定
$L'(g_{\theta,+},1)L(g_{\theta,-},1)\ne0$，成立即
$A(\mathbb Q)\otimes\mathbb Q=F\beta$ 且对数同构。
[R714](results/R714-global-visible-count-and-sublogarithmic-divisor-primitive-region.md)
在保留 $\kappa_p^m$ 和全部 signed-ray 后给明确充分区域，
含固定 $\omega((p+1)/3)$ 的充分大素数及其所述次对数 $J$ 区域；
该估计自身不覆盖全部 $p$，现由下述 R726 补上充分大范围。

[R726](results/R726-uniform-original-primitive-nonvanishing.md)
现去掉因子形状限制：对全部充分大的 $p\equiv2,5\pmod9$，
原本原 signed-ray 误差的 Gaussian 权和 $\mathcal B_p\to0$。
固定阶的小高度点用乘法独立性、模 $p$ 注入和分裂素理想赋值计数；
大阶用 Rankin 乘积，所有无穷尾完整保留。
原 $E_1$ 核逐点有 Gaussian 比较，故两误差分别 $o(1)$、$o(\log p)$，
接同一原轨道/Gross–Zagier 接口，得指定 $\beta$ 非挠、
$A(\mathbb Q)\otimes\mathbb Q=F\beta$ 和原 log 同构。
不存在关于 $\omega((p+1)/3)$、radical 或素数密度的前提。
有效阈值以下的有限层仍需原较锐证书；
此结论不提供高度矩阵或实际共同无根，主目标仍 OPEN。

[R719](results/R719-p137147-original-primitive-visible-enumeration-certificate.md)
已闭合实际137147此前提：公开 run43597653737 的945171点、
132178范数行、2769点独立全核与完整无穷尾给
$B<106516214032/10^{12}<1/2$。
证书 SHA256 为2d97169250b80abf8d4bf9d72ee7a65c5ff9ac609afdd9c9b3ffc1d65639ca3f。
完成枚举不重跑；复非消失不等于模 $p$ 单位或原高度排零。
[新核文献范围](notes/2026-11-14-primitive-nonvanishing-literature-scope.md)
明确固定素数反圆分、固定参数化横向 Heegner 与 Dirichlet 素数幂结果
尚缺原变化 $p$、六水平及指定本原投影的接口。

### 原 sigma 临界系数与完整 Abel 函数

截至R741的完整原式保留于[本次归档](notes/2026-11-14-open-before-R742.md)。
[R742](results/R742-unramified-original-first-jets-and-depth-seven-Abel-isometry.md)
以原Serre导数构造weight0函数：$M_{2,h}=-864\mathfrak J_h(\zeta)$。
完整算术GL2 determinant、支持于p的idele与原CM torus使全部允许flat jets
同处一个p未分歧有限CM域，包括非本原正标签与M2可能为零的情形。
保原R588标度、tame向量和原c1的运输；不把额外$\zeta^2$相位乘两次。
原本原M2非零时$\eta_h=v_p(M_{2,h})\in\mathbf Z$且$\eta_h\ge-2$。
结合R740，原$P_h=S_{2,h}S_{3,h}/C_0^2$非零时赋值为偶数。

R729对全部充分大允许p给原M2非零，R726同时给原秩/log接口；
R682遂有原共同Abel阶m1，仅得真实高度被$s^2$整除，未得首项单位。
R730完整Hodge界$v(M_m/m!)\ge-1-mp/(p+1)$和原jet比值在$\mathbf Q_p$
控制全部阶乘及无限尾。R737的原均方平均给
$$
\frac1g\sum_h2\eta_h<3+\delta_p,\qquad
\delta_p=\frac{134\log2+\log(1+\log p)+2\log(2+\log_2p)}{\log p}.
$$
R742整数rounding得$p\ge2^{160}$某实际本原$\eta_h\le1$；
$p\ge2^{512}$时这类标签超过$g/16$。对这样的同一原组件，完整Tate恒等式为
$$
\frac{16I_h(p^7u)}{p^7M_{2,h}}=u+pH_h(u),\qquad H_h\in u^2\mathbf Z_p\langle u\rangle.
$$
其在每个完整值域上均为等距自同构；真实KS标量$\gamma_h$只保非零，未设单位。
尚未覆盖全部候选$p^4$盘或深度4–6；更不将正秩有理点条件替成Abel回零。

R740用真实循环整格Gram商及T不变线证明$v_p(N_h)$非负偶数，
R741据R733几何均值给原单位标签占比$U/g>(1-\epsilon_p)/2$，
$\epsilon_p=\log(5(2+\log_2p))/\log p\to0$，无M2非零前提。
R734还对每个$p\ge41$、$p\equiv5\bmod6$给某$h>1$真本原N单位。
两个比例界未强迫N单位集与低Abel赋值集相交。

R727保同一原向量/torus及全部Fourier尾：同一真本原h的
$N_h,C_{h-2},C_{p-h-2}$三单位给$\eta_h=-2$、整个$v_p(a-1)>3$仅中心、
$p^4$闭盘等距。两个Cartier系数同h非零仍缺；固定有限h>1可被CRT全部排成本原。
[参数边界](notes/critical-sigma-jet-parameter-boundary.md)说明超奇异/移位数据不能代原固定CM参数。

R739公开run43610788824只复用原五SHA输入：p47/h7原N赋值4、首单位38，
同h两C单位故M2单位；p41/h37原P赋值−2、首单位23、N≡33，故M2赋值−1。
准确圆分Norm决定9/21位精度，零纤维/格点/DFT重算。
R706的5992素数完整窗口仅137147的Cp−3为零；R722已闭合其原M2单位，
两非中心scalar根深度7/2非Qp，完整p4等距；仍非高度排除。

### R717/R722 原精确范数：137147 目标完成

[R717](results/R717-exact-original-CM-norm-from-certified-complex-traces.md)
给原 $P=S_2S_3/C_0^2$ 的实圆分域、分母 $D=2^{37}3^{26}p^5$、
完整周期、原标签、全解析尾和整数 trace 重建。
p41 校准 run43597163388 的42整数 trace、原1274/24已完成，勿重跑。

137147 原 run43597802237 的四片8113行、14925440项全部有效。
其旧 recover 失败由诊断 run43602040433 定位为递推 chirp 包络膨胀。
新 run43602664971 仅独立重算同一精确相位和三个 DFT，复用全部四片，
固定 source/参数/生产前缀一致，无格点重算；全部137148 trace唯一，
最大实半径 $597851749\cdot2^{-82}$。
失败历史和完整修复证明见 R717 §10 与
[相位说明](notes/R717-independent-chirp-recovery.md)。

[R722](results/R722-actual-M2-unit-at-137147-and-deep-Abel-isometry.md)
以精确 $p^6$ 分子赋值5和完整原 norm 标量给
$P\equiv105522$、$v_p(M_2)=0$、
$M_2^2/\zeta^2\equiv53970\pmod{137147}$。
core receipt SHA41940fcf1fde383e723c1b5c0265f23b04ed441cb86d8f1e946223ec721b1c2c；
小凭据在
computations/R717-original-CM-norm-p137147-direct-chirps/43602664971-1/。
实际完整 $M_2$ 单位这个缺口已关闭，不能重新列为待算。
大中间量保留 artifact、脚本、参数和 SHA，不经工具分块传送。

### 真正高度：规范输入可构造，实际数据与排根仍须完成

R593/R596 的原 $\eta_h,\chi$、刚性化、完整 $\mu_3$ tensor、
清分母及截面保持；R690/R694/R696 给实际坏靶 $\Omega_{\rm actual}=\{0\}$。
R634 消去 $A$ 的高度矩阵，但保留 $Y$ 线性项、Picard 修正和局部常数。
R703/R716 的有限代数 jet 提取及完整相对尾已证，
后者免预求 $\gamma$；零数上界不能代共同无根。

[R724](results/R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md)
补上真正规范求值：$Y$ splitting 在原 $\Lambda$ 中含因子2及常数精确抵消；
完整 adelic Hecke/GL$_2$-type 使原 $\eta_h$ 有限轨道给所需 MW 基。
以实际对数矩阵 $L$、高度矩阵 $H$ 得
$\ell_h(v)=y_h^tL^{-t}HL^{-1}e_\eta v$，不假设 $H$ 可逆。
代数 universal-extension 提升先作
$\Delta=\log_I Z-r(\log Q)$ 校正，再在原 Poincaré 纤维做群对数求值。
第二类周期、截面常数、非 $p$ 局部项及完整形式群尾全部保留。

[R725](results/R725-original-CM-elliptic-model-and-splitting-field.md)
给原正 CM 椭圆分量的实际模型：在固定
$E_{27}:Y^2=X^3+16$ 上令
$w(P)=\prod_{a\in\mathbb F_p^\times}t([a]P)$、
$r_0=(w(P)-w([\sqrt{-3}]P))/2$、$b=r_0^6$。
则 $L=K(b)$ 次数 $(p+1)/6$，
$C:y^2=x^3+b$ 是原正 $\kappa_4$ 的分量，
$v_L(b)=1$、类型 II 最小模型；全部系数有核多项式 resultant 公式，
并给具体同源 cocycle。完整正角色、三同源和微分方向均保留。
这只补椭圆分量与分裂域，原 $J_X\to A\to C$ 同态、
$\beta$ 坐标、实际 NS/Picard/刚性化运输及 KS 尺度仍需生成。


[R728](results/R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md)
已将此分量提升为实际有理模型
$B=\operatorname{Res}_{L^+/\mathbb Q}(y^2=x^3+b)$，
其 $m$ 条余式方程、全部原正标签诱导分解和有限阶移位 $T$ 已显式给出。
$T^m=[\eta]$、$cTc=T^{-1}$，故
$e_n=n^{-1}\sum_jc_n(j)T^j$ 精确切出原本原因子，分解同源次数素于 $p$。
在 trace 识别下真实 Néron 余切格为
$F_p'(b)^{-1}\mathbb Z_p[b]\omega_C$，本原格由 $e_n^*$ 取直接和，
而非任意省略逆 different。实际极化和 NS 线丛也已给出。
原 $q/\beta$ 现在准确降为 $(X_1)_{L^+}\to C$ 的有理函数及其原 Hodge 比较；
这些函数仍未生成，原 KS/Manin 指数、Picard 修正和刚性化常数仍保留。


[R732](results/R732-original-CM-period-kernel-and-bounded-rational-function-recovery.md)
已闭合原函数构造中的周期/Manin 规范和有限终止界：
原闭周期除以同一 $\Omega_0$ 是带标签 torsion completed-zeta 的有限代数和，
$E(P)=-D^2\psi_M(P)/(2M^2D\psi_M(P))$ 保留完成化常数。
有限 $K$-线性核 $R\sum_jv_jw_{ji}\in K$ 恰给原
$\operatorname{Hom}_L(A,C)\otimes\mathbb Q$；清分母整数必须记录。
整数辛周期精确给映射次数 $d$；
Riemann–Roch 线性系统截断超过 $\deg D+2d$ 后，
极点度界严格恢复 $x=A/B$、$y=dx/(2h)$，再在原 $c_0,c_1$ 求值。
这是准确有限算法及证明；尚未执行原函数表、$\beta$ 坐标或比较矩阵，
不能把算法存在登记为原高度数值已得。

须继续生成同一原曲线/对应/线丛模型、有限关系矩阵和规范高度前缀，
并实际验证 R724 (724.33) 的有限 Bézout 不等式及全部尾。
137147 的真实高度 jet 尚未生成，排根证书尚未通过；
亦未证明该证书对全部 $p$ 存在。
任意第三类微分、任意曲率原函数、未知高度非退化均不能替代实际输入。

### 原普通 Norm、首矩与类作用参数

[R731](results/R731-complete-ordinary-Gamma-norms-and-marked-q-principalizations.md)
现给全部原层的完整普通 $\Gamma$-Norm：
$N_\Gamma E_{M_n}=(p,s-1,N_{T_n})E_{B_n}$，
商为 $k[T_n]/(N_{T_n})$。
原 $q$ 类 $44N_{S_n}c$ 非零且填满 ambiguous socle，
故 strongly ambiguous 等于 ambiguous；
完整普通除子/Hilbert90 序列遂消去“单位中的域 Norm”与“普通单位 Norm”的差别。
原 residue Norm 精确恒等和 $A_n'(1)=-13i$ 给整核，未漏 $q$ 或额外乘 $p^n$。
进一步可在原 $M_n$ 全局选取
$\operatorname{div}Z_n=N_{T_n}P_+Q_n$、$N_\Gamma Z_n=A_\alpha$，
全部解为普通 $\ker N_\Gamma$ torsor。
这是准确原标记的主化及 Norm 校正存在定理；$Z_n$ 坐标、实际 $J/b$ 尚未求出。



固定 $p=43$ 的776bit $q$ 已被 Gaussian5 排除，并非实际曲线或 Serre 反例。
R715 确定原 $m=43$、普通 scalar Norm 满射、$N_PE=(p,\pi)E_L$；
R718 给所有层 $m_n=42n+1$、$d=\infty$、普通类 Norm 逆极限
$R_\Gamma$ 和真正相容普通单位 Norm 像。

[R720](results/R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md)
用同时整提升、真实 $N_\Gamma X$ 自由像和两次原链比较给
$C=9ib=-34ib$，故 $L=31+26b$、$r_y=25+9b$、
$\Omega_2=\varepsilon(22+17b)$。
最后障碍零恰 $b=24$，但实际 $b$ 未知；
禁止代 pure-$p$ 参考24、一次10或辅助 $C_t=9$。

[首矩重建](notes/2026-11-14-r599-first-moment-normalization-reconstruction.md)
保留原 $t,P_0,P_+$ 和完整普通div/Norm，
定义选择无关 $J_\ell\in\mathbb F_{43}$、$J_r=-2J_\ell$。
全部见证恰 $X+(t-1)E$，完整余数改变量全像 $I^2$，
所以 $J_\ell$ 是唯一剩余坐标。
允许Norm改普通基单位以杀全余数时，系数
$c\equiv-J_\ell/(13i)$。
R185 同一原 Robert 规范给有限 flat Norm 目标
$A_{\alpha,\mathrm{fl}}=A_\alpha-(8i/1848)u$，
故 $J_{\mathrm{fl}}=J_\ell-18$；系数只在模43时写成 $+8i$。
同笔记§8进一步给真实受支撑 primitive
$e_p(d_q)|_q=(J_\ell/2)K_0$、
$e_p(d_q-8d_0)|_q=((J_\ell-18)/2)K_0$，两者奇异项均零，
与原 $w_q$ 配对为 $\varepsilon(J_\ell-18)$。
原障碍却含 $e_q(d_0)$，仍须带完整规范的
$\kappa_p$–$d_q$ / $\kappa_q$–$d_0$ 交换链。
实际 $J_\ell$、$J_{\mathrm{fl}}$ 与原 $b$ 的准确比较及真正主化坐标仍缺。
R704 原43嵌入矩阵及R708局部Norm歧义已处理；
仅局部条件不能替全局普通输入。


**R736（已证明）**：同原p43/q标记，NS kerΓE_M=(π,N_T)kerΓE_N等于全部原q直接相位核。原Fr=s32给s在μp²上指数1+2p及rμ(ct)=ell(ut)，R207实一致化元保含极点双Norm相位零。故存在原divY=D_Tq、NΓY=NSY=D_TXt；Z=Xt−(t−1)Y同时NΓ/NS/NT=Aα，原直接相位rμ((s−1)Y)=−4J，flat=−4(J−18)。完整普通校正已证，真正与R720原b的T/Γ链及J/b数值仍缺。详[R736](results/R736-original-three-norm-exchange-and-minus-four-moment-phase.md)。


**R735（已完成原模型输入）**：公开run43608152850首次生成原p41同一b=r0⁶的完整七次F41，在原280维除法商代数完整核F41(b)=0、七个低阶系数v41=1、disc41=6和F41'逆。原b是唯一实正根，目标Néron格b^j/F41'(b)ω已具体，本原仍投e42；完整小cert SHA752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574。原q函数/β/Manin尺度/高度仍待继续，原4920coset/800闭周期输入已由R738完成，继续原Hodge/adelic矩阵，勿重算模型。详[R735](results/R735-exact-original-p41-CM-model-and-Neron-input.md)。


**R738（原带标记闭周期输入已完成）**：公开run43612108090在原六层Q8图式和同一p项链上生成4920陪集及每条整SL2Z代表；g400、20个宽246尖点、819整数相对基、800整数闭基与交配det1。原c1唯一实标签C为4424，deck[4424,0,1258]对应[1,ζ,ζ²]；c0三轨道是同一个粗点。两完整大表只artifact，cert SHAa853f36bf5d6f7d238e805a5c2134b2f7b3db17528195d56d980e66c9c769009。真正待继续的是原正CM因子的Hodge/完整adelic表及周期求值；原q函数/β/高度未出。详[R738](results/R738-certified-original-p41-period-input.md)。
