# R449. actual202 十词到准确连续十族的独立初猜：支撑、投影与完整双问题合同

- 作者：AI
- 日期：2026-11-16
- 状态：下列源级区别和条件代数已证明；两独立执行源已写成。没有在本地导入科学模块、做数值算术、AST、编译、fixture 或测试，没有新实际运行。
- 入口责任：actual202 只提供十个原参数字符串。新的准确 C、cut、完整标量域、全部112尾数据、完整453及450仍须由公开 Actions 实际支付。

## 1. 可直接用什么，不能转移什么

[R439](R439-actual202-ten-unit-tolerance-complete-final-diagnostics-and-projection-scope.md) 给出了 request202 的真正末十词：run `43784544723`，source `1a757004b7ebff1f43563bd57b5d13961648d681`，compute `133029129971`，report `133029647087`。当前 owner、final、最后接受 candidate 三路径的十词逐字相同，规范紧凑 JSON 数组为553 B，SHA256为 `ba7d7fe3c7fd2599bb7f06863c117b11c6c9f4feb255a160de13023e22129369`。本稿从已刊 R439 的十行原词选择出新参数输入，并核这个文字身份；没有重新下载日志或重算残差。

202 的持久 Decimal50 有限字面模型达到其原 unit 阈值，末 merit 原词为 `6.792856894159490952984073464463952834293497113858E-20`。同一报告也明确：其 binary64 投影的 unit 判据为 false；完整非零 native、真实非零全场和课题 success 均为 false。已做120个FD及投影处的标量域/453圆参考，不等于新准确连续目标的域、Jacobian、非线性解或闭面。

**本稿结论。** 这些字符串能合法地指定一个新的准确连续十族候选，但既不自动指定与旧模型相同的函数，也不自动满足新函数的严格域。当前112/BVP程序以 binary64 参数字词为实际坐标，因此这里明确选择：先在 Actions 投影原十词，再把投影字词的准确 dyadic 值定义为新的准确参数点。原字符串、投影字词及准确差额分别保留。不是把原 Decimal50 点冒称为已被 binary64 BVP 原样消费。

原源码没有修改。现有203的 actual180/正零xi来源合同也没有放松；新增独立 driver 声明自己的候选来源及 schema。

## 2. 两条原来源链

### 2.1 actual202 的有限字面十族

以下来源在公开库逐文本读取；没有构造其对象。

| 角色 | 文件 | SHA256 |
|---|---|---|
| 固定十族 | `geometry_20261115_adjoint_selected_ten_control_family.py` | `09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016` |
| Decimal50十族 | `geometry_20261115_adjoint_selected_ten_decimal_model.py` | `8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7` |
| 前九列 | `geometry_20261115_small_core_nine_control_family.py` | `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629` |
| 原prefix控制窗 | `geometry_20261114_prefix_controls_profile.py` | `f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24` |
| 原零控制基底 | `geometry_20261114_full_scalar_profile.py` | `8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b` |

必须沿真实构造链，而不能只看 `CompleteProfile` 的默认控制窗。`geometry_20261114_lifted_modes_prepare.py::build` 调用没有另给 supports 的 `LiftedModesPrefixProfile`，后者继承 `PrefixControlsProfile`。其三窗是原 binary64 运算形成的

$$
[.05L_0,.30L_0],\quad [.35L_0,.60L_0],\quad [.65L_0,.90L_0],
\tag{449.1}
$$

并保存每个实际 left/right 及 binary64 的 `right-left`。`constrained_trust_warm.setup` 再从原 prepared 的 `control_supports_binary64` 恢复同三个窗，0865及0924沿用这些真实窗。因此 **actual202 的全部十个控制都在旧prefix内**；其xi是第二个prefix窗的power4项。旧基底在prefix外有 AngleConnector、速度 `-.985` 的coast和原有限尾bridge，不能把这些基底段的位置误称为202控制支持。

8cb8保持原699个节点、698个中点、原完整112零H响应J以及原标量表的 binary64 字词，再作准确lift进入 Decimal50 有限运算。它没有从一个新的连续C profile重新积分这些表。其圆半径R满足原离散形式的 `R'=ap*R/a`；独立返回的ap不因此成为 finite-Gauss 半径的真导数。[R298](R298-original-finite-Gauss-clip-seam-and-same-target.md) 已明确该区别和条件接缝障碍。

### 2.2 准确连续十族及完整BVP

| 角色 | 文件 | SHA256 |
|---|---|---|
| 准确十族factory | `geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py` | `72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682` |
| 公开数值compiler | `geometry_20261115_continuous_ten_fixed_power_scalar_numeric_v3.py` | `7dedb7134cd2efc43f136c4a87795f06c6f3824c12a25261b6886c624f6e4ddd` |
| 当前profile/冻结 | `geometry_20261115_continuous_ten_same_metric_profile.py` | `3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6` |
| 真实双问题基线 | `geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py` | `5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592` |
| 原完整joint native driver | `geometry_20261115_current_C_pruefer_joint_full453_physical_dn.py` | `c71d616936cf33e43965906c7cc99face01d06a12433420474b688b8d76b946d` |
| 活现场checkpoint | `geometry_20261115_continuous_ten_frozen450_checkpoint.py` | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |

72c准确函数的几何语义是[R300](R300-continuous-nine-control-scalar-family-and-cut-calibration.md)、[R323](R323-finite-cut-boxes-and-explicit-uniform-dyadic-windows.md)所定义的共享准确core、两个准确cubic速度过渡、准确累计coast和canonical cubic cut collar，再加明确十个多项式控制。这里的core来源仍为原真正accepted96的几何；accepted96本身不是新目标上的完整112场。

准确尾继续是原 f12f 生产者 `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` 的约定C、同原binary cut及完整许可root族；不以一个cut区间中点重定义准确函数。7ded的数值对象则公开选择有限叶中点、有限DAG运算及实际多项式求值。其作用是数值搜索近似，不是准确C全局root的选择证书，也没有自动给连续目标误差界。

## 3. 十个名字相同，不代表十个作用相同

两族顺序都是

$$
(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3,\xi).
$$

记

$$
B_k(x)=64x^3(1-x)^3(2x-1)^k,
\qquad h_{i,k}(s)=w_i^2B_k((s-\ell_i)/w_i),
\tag{449.2}
$$

在 $0<x<1$ 用该多项式，其他位置零延拓。两族控制形式都按power0、1、2对应前三组三项，xi为support1/power4；区别在准确/有限的基底、支持、坐标与所有求值责任。

| 参数组 | 202原有限族的实际支持 | 72c准确连续族的实际支持 |
|---|---|---|
| p1 / theta1 / eta1 | 第一个prefix窗，原实际left和stored width | 所取准确结构配方的first_support，沿原第一窗字词解释 |
| p2 / theta2 / eta2 | 第二个prefix窗 | $[L_0,L_0+\delta_A]$，准确第一速度过渡 |
| p3 / theta3 / eta3 | 第三个prefix窗 | $[S_1,S_1+L_C]$，准确coast |
| xi | 第二个prefix窗，catalogue3的power4 | 准确第一速度过渡的power4 |

R449的准确结构模板是actual180实际小recipe，2136 B/SHA `cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb`。只复制 `core_end/cut_radius/kappa/collar_width/first_transition_width/last_transition_width/first_support/root_choice/collar_mode` 九项，所有旧九系数及其origin、所选域证书都不复制。原模板的来源是结构参数来源；不把新点叫作180的已证点。

这里固定的 $kappa=1/2$、$delta_A=\delta_B=1/1024$、$d=1/524288$ 是该原配方的字面值。[R323](R323-finite-cut-boxes-and-explicit-uniform-dyadic-windows.md)给其有限包围条件；新C现场仍由原factory实际核全部严格构造条件，不因旧配方已存在而预付。

### 3.1 准确自然长度并不是旧有限长度

对同一个准确C cut，设其语义叶为 $E_0,E_1,E_2$，原cut半径为R，准确core末jet为 $(R_A,V_A,B_A)$。72c实际代码规定

$$
v=-E_0^{-1/2},\qquad b=-\frac{E_1}{2E_0^2},\qquad
q=\frac{E_2}{2E_0^{5/2}}-\frac{E_1^2}{E_0^{7/2}},
\tag{449.3}
$$

$$
R_B=R-vd+\frac12bd^2-\frac16qd^3,\quad
V_B=v-bd+\frac12qd^2,\quad B_B=b-qd,
$$

$$
I_A=\frac{\delta_A}{2}(V_A-\kappa)+\frac{\delta_A^2}{12}B_A,
\qquad
I_B=\frac{\delta_B}{2}(-\kappa+V_B)-\frac{\delta_B^2}{12}B_B,
$$

$$
L_C=\frac{R_A-R_B+I_A+I_B}{\kappa},\qquad
S_1=L_0+\delta_A,\qquad L=L_0+\delta_A+L_C+\delta_B+d.
\tag{449.4}
$$

这些量不依赖十个控制系数。控制在其真实端点零2-jet，所以它们不移动准确core起点、各支撑边界或cut两jet。原有限基底的长度由 AngleConnector、到半径 `.35` 的速度 `.985` coast和有限bridge累计而来；不能把该旧L、旧s表或旧699节点坐标直接当作(449.4)。

共同公共区间可以仍记 $u\in[0,1]$，但新的准确目标为

$$
g_P=L^2\,du^2+a(Lu;P)^2\,d\theta^2,
\tag{449.5}
$$

新的数值搜索用 $s_{\rm num}=L_{\rm num}u$。原453 seed可以按u重参数化后重新求全部RHS；这只是一个新初猜，不能保旧残差或把旧RHS除以一个比例就宣称当前方程成立。完整角材料图、闭面construction、共同材料pullback和全t几何还按[R443](R443-common-material-angle-pullback-and-fixed-closed-target.md)等原责任另付。

### 3.2 控制的准确零2-jet

**命题449-A。** 假设 $w_i>0$，则(449.2)对 $k\in\{0,1,2,4\}$ 的零延拓是 $C^2$；其函数、第一、第二导在两个支持端点均为0。对每个内部点，准确三jet为

$$
(h_{i,k},h'_{i,k},h''_{i,k})=(w_i^2B_k(x),w_iB_k'(x),B_k''(x)).
\tag{449.6}
$$

**证明。** $x^3(1-x)^3$ 在两个端点至少三重为零；另一个多项式因子有限，不降低消失阶。两次求导后仍至少一次为零，故左右零延拓的0/1/2迹一致。内部链式法则给(449.6)。□

这只是准确多项式命题。它不把有限采样或独立舍入两侧迹变为同字词，也不消除旧有限Gauss基底的接缝责任。72c正确性还依赖其共享准确基底构造，7ded的数值seam误差仍公开为未证范围。

## 4. 原50位点与新dyadic点

令 $P^D_i=\mathbb Q(\text{原字符串})$，$p^{64}_i$ 是在Actions按7ded相同的 `float(Fraction(word))` 形成的有限值，$P^{64}_i=\mathbb Q.\mathrm{from\_float}(p^{64}_i)$。R449选的是 $P^{64}$，并逐项输出

$$
\Delta_i=P^{64}_i-P^D_i.
\tag{449.7}
$$

**命题449-B。** 这个显式构造使新的72c初始准确点与新的BVP初始实际参数具有相同十个有理值；它不使 $P^D=P^{64}$，不把新数值compiler等同准确profile，也不转移旧残差。

**证明。** 新模型recipe直接写 $P^{64}_i$ 的完整有理词；新BVP写对应 $p^{64}_i$，并绑定全部10个 little-endian64位字词。3bc的 `current_target_identity` 和7ded的 `export_specification` 正以当前有限参数的准确dyadic解释该族点，所以两处初始参数相同。cut中点/表达运算/完整ODE误差不在这个恒等式里。原第一个50位字符串末位为3，作为十进制有限小数约分后仍有分母5因子，故至少该坐标不是dyadic；其准确数不能由任何有限binary64字词完全表示。因此需要公开(449.7)，不能声称原点已经无损继承。□

没有在本地形成 $p^{64}$ 或(449.7)的数值。输入文件只保存原553字节数组及其来源。未来真实投影记录保10行：原字符串/准确有理数、新binary64数值/hex/little-endian词、新准确dyadic、差额和是否相等。即使某一坐标恰可准确表示，也不省略该行。

另一种合法研究选择是直接把 $P^D$ 作为72c准确参数；但若仍用当前3bc binary64 BVP，则实际求解点成为其投影，必须另付两个参数点之间的准确比较。本接口没有把那条不同任务混入当前初猜路径。

## 5. 合法代数候选，不是已知可行点

给定原准确构造条件，72c的全部十参数允许任意有限准确实数；固定它们不会破坏命题449-A或准确cut两jet。不过正半径、严格 $|a_s|<1$、控制后的完整core/transition/coast/collar都仍要在真实点检验。

原 `construction_conditions` 只由core、C cut和结构宽度形成；它的全部严格条件是原factory进入新定义的前提。原 `prove_domain` 分别对零控制基底和全部十控制做完整闭片覆盖，保未访栈、终深未解叶、全部半径/速度原包围和账本身份。`complete=false` 是充分证书未付，单凭它不能宣称域已被否定。该完整域读回也没有被本稿添加为BVP之外的一个新接受门。

### 5.1 一个必须保留的实际自由度限制

在准确coast中令 $t=(s-S_1)/L_C$。因其他支持不进入其内部，

$$
a(t)=R_A+I_A-\kappa L_Ct+
L_C^2[p_3B_0(t)+\theta_3B_1(t)+\eta_3B_2(t)],
$$

$$
a_s(t)=-\kappa+L_C[p_3B_0'(t)+\theta_3B_1'(t)+\eta_3B_2'(t)].
\tag{449.8}
$$

在 $t=1/2$，$B_0'=B_2'=0$，$B_1'=2$，故

$$
a_s(1/2)=-\kappa+2L_C\theta_3.
\tag{449.9}
$$

**命题449-C。** 若真实准确C给 $0<L_-\le L_C\le L_+$，则由(449.9)的两个端点取最小/最大得到整个许可root族的中心速度包围。若该包围整体位于 $[1,\infty)$ 或 $(-\infty,-1]$，则每个该族成员都违反原严格速度域；固定七shape、只改变p1/p2/p3的453问题不能修复这个中心。若包围含合法区间或跨阈值，不据此判失败；若整个中心包围在 $(-1,1)$，也只支付中心而非全coast。

**证明。** 固定 $\theta_3$ 时(449.9)对 $L_C$ 仿射，闭区间极值在端点。三个p、eta3和support1的xi都不出现在(449.9)，所以不能通过这些坐标改变中心值。严格域的边界值 $\pm1$ 同样不合法。□

新adapter在真实factory之后允许直接从原 `derived_endpoint_intervals.coast_length` 做这个小必要读数，输出原盒及准确有理结果；该结果不控制原BVP调用、不选新系数、不改任何原flag。它是下一步判断是否需要释放真正作用于coast的坐标的证据，不是以六候选或rank数代替可行性。**本稿没有代入新实际LC，也没有宣称202新候选已触发或未触发该反证。**

更一般地，[R383](R383-accurate-R323-target-identity-and-coast-control-necessary-band.md)和[R386](R386-accurate-coast-uniform-feasible-scaling-and-C2-bounds.md)的准确coast作用/缩放论证仍适用；若未来另行修系数，必须再声明新的参数点。不能暗中把202的coast项缩成actual180旧点，或把support1的xi当作coast修复。

## 6. 已实现的最小新路径

### 6.1 `prepare`：只准备新的输入

`geometry_20261116_actual202_accurate_ten_candidate.py` 强绑定独立参数输入及553字节数组，读取实际180小recipe作为结构模板，只复制第3节八项，形成完整新十参数recipe。它在原公共Actions内执行显式投影，保存完整10行差额，且返回 `accurate_C_factory_domain_or_BVP_called=false`。任何旧有限结果或actual180域证书均不写为当前已付。

### 6.2 原生产者真实运行

未来同一job仍真实恢复原accepted96和完整699×453种子，并依原C输入/预算生成 f12f C、完整cut两jet及全部112 joint-provider数据。用新recipe实际调用72c，执行原两个全域pass；不能由本adapter拼一个旧factory schema的result。

### 6.3 `bind`：读真实结果后形成新的双问题recipe

`bind`要求实际factory/definition、modelrecipe和C/cut收据一致，来源/run/commit属于当前job；准确point与初始BVP的10词一致；当前joint config明确四个实际来源角色，完整30源及native policy仍由原c71d入口逐项核。factory的base/current域、未解/未访计数、账本身份、中心必要诊断全部分别读回。不存在“只因new point名字合法便标full domain true”的路径。

原179不可变BVP小配方只提供原算法、lambda、来源seed和预算模板。该模板的lambda仍为0.001、高度sign为−1；本稿不从202的unit判据推导或重选lambda。新recipe把全部旧参数和origin换成实际202候选来源、实际新factory/C/cut，并把native源表换成真实197 joint配置。原17档、RMS/BC/FD、8outer、完整native32×10和112/338行保持。

`geometry_20261116_actual202_accurate_ten_full453_frozen450.py` 只从5400独立派生来源/recipe/CLI适配。原对xi正零的actual180输入限制改为完整R449候选字节绑定；这不是删去一个物理方程或科学接受条件。原 `prepare_design`、`PhaseLease`、`prepare_frozen`、`run_phase` 正文不变，新的候选binding进入实际session和闭包。

### 6.4 两个真正问题，不能省第二个

第一阶段固定theta1..3、eta1..3、xi，共七shape，p1..3活动；完整338物理行、112core行和3参数行，总453。lambda仍乘原真实accepted96的前三core目标。旧699×453文件仅按公共u形成新初猜，全部新节点RHS和原节点/中点/RMS域重新求值。

只有原完整453流程真的接受且活现场43f捕获完成，才使用其末十个真实字词冻结新目标。第二阶段K=k=0，保完整450未知和338+112边界，重新形成所有450 RHS和原preflight，重新当前H/FD/native/full338×112响应/final audit。保一个真实raw native owner，两阶段仅释放各自lease，最终仍实际close。没有从453删除三个变量便标为450接受的路径。

当前R449不产生新的完整闭面图、metric、reach或全t结果。即使将来两BVP都接受，还要按实际新checkpoint、材料图和construction完成原课题的几何消费者。

## 7. 生命周期、差异与下一完整入口

本稿交付两执行源、参数输入、完整5400→新driver差异及接口。没有新request、workflow、run或未来success。

源码接线修订：首刊 `c5577584a5a914a420755d613b803455ec374300` 版本尚未执行。继续逐项对照72c的实际 `main` 时发现，它在形成factory输出前直接读取 `recipe["cut_radius"]`；原adapter八字段列表漏了这项。当前仅从同一2136字节 `cc87d932…` 原模板按原准确字面复制 `cut_radius`，结构字段由八项改九项。driver只级联helper pin，方程、十词、域条件、资源与全部接受门不变；没有从数值中点或旧解反造cut。旧cb057 launcher/203 pipeline硬pin原来源；新driver不能借这些旧pin假称被接受。下一完整入口必须显式接新的pipeline、owned tuple、recipe/实际deadline收据及必要reader。

新adapter不启动、修改或重启绝对钟，不产生新科学求解预算。原179模板的采样启动预留是7200秒；这与完整双BVP的7200秒process上限是不同字段。为避免后继bind完再改recipe破坏身份，`bind`必须显式接受 `--sampling-startup-reserve-seconds`，在生成最终recipe及其SHA之前写入实际预留，并同时记录原7200、传入值和不变的完整BVP上限。没有默认值。本源不预选未来实际请求；后继若明确沿203的3600秒采样预留，应在这一步传入3600，不能在已绑定recipe上静默覆写。

未来外壳须保原namespace绝对截止、已明确的C/112采样资源合同、原7200双BVP共享上限、原2700读回/清理余量、quiet/reap和单份90000字节必要输出；一旦预算到达，按真实partial与未访后缀停。科学大表只在当前Actions临时目录。所有基底域/完整现场关闭和清理责任都不由一个SHA替代。

两新源仅做本地文本/JSON/字节/完整差异工作。源未导入、未AST、未编译、未作数值fixture；执行语法和实际计算留在未来公开Actions原流程。根唯一发布并选择未来实际请求。当前204独立运行由其自身R446记录，本稿不借其未终态内容。

## 8. 结论的准确边界

R449已经给出一个可实现的新候选映射和完整两阶段源接点：原202十词→明确新dyadic点→真实准确C/72c profile→真实453→同真实末十词的完整450。参数顺序与多项式power对应，支持、基底、L、cut及数值求值器没有被混同。

尚未支付：新C/cut包围、新全十参数准确域、center必要读数、初始projection实际差额、全部新数值profile、112 provider、非零native/453/450、连续目标误差、共同材料图及闭面全域几何。原202“unit达到”只作为其原有限问题的事实保留，不被升级成这些新结论。
