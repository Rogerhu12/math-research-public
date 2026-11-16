# R896：原五个 sum-Hom 的低权残余 RR 消费方法

日期：2026-11-16。状态：源码与准确执行契约；本消费者的新两 B 秩、padding 核、962 子式、418 空间和标记主函数尚未运行。原 R893 五个初始 RR 空间已经实际完成。本稿不改变已冻结的 R893 算术，也不将它的初始维数直接当作 R896 的输出。

证明采用 [R896 原两 B 低权核](../results/R896-original-two-denominator-low-weight-residual-RR-kernels.md)，SHA ca0d8891a04683f712c1fe347f1da3e707854aa889163c7c3207ec8656b70341。全部新算术只在原公开仓库 Actions 内执行。

## 1. 准确对象及固定剩余处

保留原 $Y/L$、属127、$H=(\tau)_0$、$\deg H=272$、原 $P_0$ 和 $\rho=z-z(P_0)$。输入是原正号同态 $g_j=(1+T^j)f$ 的完整关系图，$j=1,\ldots,5$。不换同态、相位、曲线、原 $-3$ 下降或正规基。

实际计算素数为 $1000000753$，原整元 $B=\lambda b$、$s=1+2\zeta$ 的原像分别为3197390、99932770，$\zeta$ 原像549966761。正规基权仍为 $(0,1^{144},2^{127})$。$V_m$ 的正常基按 $(i,k)$，$0\le k\le m-\epsilon_i$，先 i 后 k；数组已经表示截面除以原 $\tau^m$ 的函数坐标，不另施82、$\lambda$ 或正常基尺度。

| j | n | $\deg E$ | $\delta$ | 原完整 B 维数 | 原完整纤维数 | 两 B 所需秩 | 残余维数 | padding |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1|12|2970|294|168|23|984|396|250|
|2|8|1674|502|376|15|1192|188|42|
|3|8|1800|376|250|15|1066|314|168|
|4|13|3024|512|386|25|1202|178|32|
|5|14|3339|469|343|27|1159|221|75|

准确空间由原矩阵及实际单位子式定义；新数组只是这些准确 unit-solve 表达式在指定处的约化。有限域零不独自证明任意特征零等式。

## 2. 真正已成来源与最小选择

原 R893 实际 run43861874528 / job133280560534，source fe27ac55e0c5d538ac60473df9f1c33f1f90f3b3，已完成全部五方向。其数学核心是 c199ccbf95de73fb8e1f156a4adaea9ce517cb1c42c427b55c2dcc4901065daa；FINAL 18395B / ad135ab7a624beaad0e1fba76230a63cfe478b3aa667b6b33624f763269cf728；完整 manifest 98261B / 58a66985fc3bcb663ab5e7c4238546d8d33a876a3fd69663e9f4f817fb8eb8b4。原 artifact14224626902 576747513B / cc7cc8e58754205f1472929b4a733e20bf594732aae869a19004d9c32fb01893 为不可变出处。

包装器沿 FINAL 引用逐项选取五方向证书、完整 A/B 核、原单位子式、实际纤维选择、全部已成 B 纤维值和原 A−yB 全行回执。由各 single-denominator 的 source_complete_fibre 再取真实原 Krylov receipt；新节点还取其已成 W/K 矩阵阶段。已成初始 Schur 大块、normal-multiplier、导数块、整个146MB原输入载体不为本 scope 重新下载或计算。B 纤维阶段中同时保存的 yB 数组保原字节，不能删字段后仍称同一来源。

其余实际来源为：

- R880 原 252×690 正常 V3 点矩阵，文件 R880-original-V3-252-point-jet-matrix.json.gz，901788B / 5f40695a800339604c7fba0fcf19e73c677dd54579170f50c46b054b9b903120。字段为 matrix_mod_prime、V3_basis 和 row_orders=0..251。不得以 R845 Fourier V3 评价冒充正常基评价。
- R872 原 point-linearization、固定 $\chi$ 除子与未缩放 u 锚。$\chi=H-272P_0=(D_\chi-H)-\operatorname{div}(u/\tau^2)$，原272阶单位须读取实际 exact_order272_unit。
- R883 原 $t=c\rho+O(\rho^2)$，c的实际约化354813668。只消费已成原帧，不求新的 t jets。
- R848 的实际 c0 五 W/λ³ 非零阶段和原 c0 局部证明。它们给原 $m_0=\operatorname{mult}_{P_0} E=1$；这个准确阶不是由一个模零常数项猜出。
- R890 已完成的七个正常 V3 纤维，run43853462674 / source aa00d76e4a0292f780406c5f75090668a9b66523，配置75267c1ba5c7b60c69d22b6a4359a564c7636706b99be9dff781959523155f8e。每个旧文件同时给 normal_evaluation_mod_prime 与 cyclic_evaluation_mod_prime。包装器可直接取已成小 IO run43860838780 的31MB源包；无须下载3.8GB原八 flip artifact。
- R827 原 W 和八个已成 Krylov 点继续保原 producer 身份。它们可从 R885 已成15件 R827 载体13461744B / 95e2c88502c73b285a37f26df0765abd8bb4830742c231ced6f64a066fafa26b运输；R885在这里仅作不可变载体，不运行其数学。

逻辑来源组固定为 R893、R880、R872、R883、R827、R890、C0。所有来源保完整 manifest、实际 public input、run/core receipt、证书或真实 checkpoint 配置和所选文件字节/SHA。部分旧公共配置的指纹可从已 pin 的真实成功证书读出后写入 expanded job；不补造未知值，也不把 carrier 的标签改成新数学标签。

## 3. 先标记原 A/B 对，保原标量

只读 R893 原完整 A 核，在原 P0 正常点评价上找第一个实际非零列。所选同列 A0、B0 原样保留，不把 A0(P0) 缩成1。若所有 A 值在这一剩余处为零，本次只报告缺少单位列，不否定特征零空间。

原 A0(P0) 非零和准确关系 A0=y_g B0，结合原 m0=1，给
$\operatorname{div}_{nH}B_0=E+F_0$，$P_0\notin F_0$。原 B0 第一系数从既存正常 V3 的 beta 零、一阶按
$$
[\rho](z^k\beta_i)=z_0^k\beta_{i,1}+kz_0^{k-1}\beta_{i,0}
$$
运输；这是新的必要截面评价，未重求任何 Hensel jet。必须实际得到其单位。B0 零阶的准确消失来自原全局关系与原 c0 极点，模零只检查约化一致性。

每个标记阶段保存原核列号、完整 A0/B0 正常向量、未缩放单位、准确源定义及实际 rho 阶。以后取 Galois 共轭须固定这些原列号和整数组合，不能另选基后称同一个共轭。

## 4. 两 B 产品与完整残余核

在同一个原完整 B 基中按正整数 c=1,2,... 取
$B_1(c)=\sum_{i=0}^{r-1}c^i B^{(i)}$。c与幂次定义准确整数；保存的模系数只是其约化，不能反向把任意模系数当作特征零选择。

所有 B0/B1 纤维值都从 R893 的完整272×r值直接选列或取相同组合。其乘 V3 产品用
$$
[B,W B,\ldots,W^{271}B]\,(K^{-1}E_3).
$$
旧0..6的 E3/K⁻¹E3直接来自 R890；其余实际 R893 节点仅新形成缺少的正常 V3 单项式评价。每个 W、Krylov 逆及原整 Artin 纤维都来自已成阶段，不重新取逆、不删剩余域因子或 nilpotent。

固定 B0 产品每节点只保存一次。各 B1 试次不重算固定列。完整矩阵是272N×1380；因 N>n+3，其核就是全局 V_(n+3) 核，未借 V2n 注入。

所需秩为690+δ。先保实际主列、原选行和秩；接受后保存原方块逆、双向乘回、实际非零行列式、规范自由单位块核和全部原行按272行分块的乘回。几何上界与单位子式夹逼给准确特征零秩，故选行解满足全部准确行。只有这些条件全成才投影第二690行，并再保存投影实际单位子式，认证完整 H0(3H−F0)。

失败有限试次保留其真实秩。增加最大试次数只续下一个整数参数，不重旧试次、固定 B0 产品或已成逆。

## 5. 旧 jets 的 padding146 与完整418

把既存252阶点矩阵的前 k 行限制到完整残余空间，实际形状依次为250×396、42×188、168×314、32×178、75×221。每个完整秩 k 子式、规范核和全部行乘回给
$$
U=H^0(3H-F_0-kP_0),\qquad \dim U=146.
$$
完整 U 的正常坐标由两次准确 unit-solve 相乘定义。第 k 阶泛函也从旧点矩阵读取。选择其第一条实际单位列 v，保持原标量；于是
$\operatorname{div}_{3H}v=F_0+kP_0+D_{\rm std}$，Dstd 有效次数272并避开P0。

在同一 U 中按独立正整数调度取 w。使用本方向已接受节点中的前七个完整纤维，形成1904×1380的 [vV3,wV3]。v固定产品保存一次。只有实际秩962、全1904行核乘回和第二690行418秩投影都完成后，才给完整
$$
H^0(3H-D_{\rm std})\subset V_3.
$$
输出690×418正常坐标与准确 unit-solve 定义；不得将前面的146或残余396/188/314/178/221列改名为418。

## 6. 原主函数和 t 帧

逐个保原函数
$$
G=(B_0/\tau^n)/(v/\tau^3)=\tau^{3-n}B_0/v,\qquad
Q=G(u_\chi/\tau^2)^{-(n-2)}.
$$
正常数组已经各除其对应 tau 幂，因此实际 DAG 是两个正常函数相除，权差3−n只解释其同次截面公式，不再乘第二次 tau。

准确除子恒等式为
$$
E-\deg(E)P_0=(D_{\rm std}-H)+(n-2)(D_\chi-H)+\operatorname{div}Q.
$$
令 b1、vk、u272是所选原截面的准确首项；实际读其约化。则
$$
\operatorname{ord}_\rho Q=1-\deg E,\qquad
\operatorname{lead}_\rho Q=(b_1/v_k)u_{272}^{-(n-2)},
$$
$$
\operatorname{lead}_t Q=\operatorname{lead}_\rho Q\,c^{\deg E-1}.
$$
新整数幂是对已成 c 的必要消费，不是新的 t jet。准确首项保源绑定表达式，实际有限域首项单列；不宣称它们已经展开为特征零坐标，更不把辅助处单位说成41处单位。

## 7. 输出、原子续接与真实性

数学核心是 R896_original_five_sum_Hom_low_weight_RR.py；标准库封装是 R896_public_original_five_sum_Hom_low_weight_RR.py。结果名 R896-original-five-sum-Hom-low-weight-residual-RR，FINAL 为 p41-original-five-sum-Hom-low-weight-residual-RR-certificate.json。

核心只写根目录 R896-*.json.gz 原子阶段及 FINAL/core receipt。每个阶段同一新数学配置，包含真实来源身份和所选文件指纹。完整矩阵逆、规范核、逐行回执、投影、固定产品、试次和主函数分别保存。完整阶段 manifest 按文件清单和当前 checkpoint 内容命名，避免预算结束时历史快照与新 current 争用固定文件。

同一核心/方法/来源标签可增预算、方向范围和有限试次上限。这些是运行控制，不改变已经定义的整数调度或准确选择。恢复按实际完整 manifest 的 SHA 保所有已成阶段；旧 false FINAL 不限制随后推进的 current。true FINAL 才要求当前完整 inventory、全部请求方向和全部输出引用一致。外层超时留900秒余量，TERM后短宽限再kill，并保真实退出码124、已成阶段和一日 artifact；没有 core receipt 时只记真实缺失。

包装器只做标准库字节、schema、来源和引用检查，不 import 数学核心。公开 workflow 在真实 pull/rebase 后核两 README 与冻结文本，再执行核心；所有新算术仅在本仓库 Actions。源码、参数、纸面证明与简明运行/SHA登记可入Git；机器回执、矩阵和向量只在一日 active artifact/carrier续传。

本次终点是五个原 E 的有界代表、完整418源和准确标记 Q。原五 Lj128/144、范数 RR、Hecke/Picard 活跃支持、连接、period 和高度均不由此宣布完成。
