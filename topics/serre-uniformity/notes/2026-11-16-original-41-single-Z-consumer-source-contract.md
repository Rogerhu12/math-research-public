# 原 41 处四响应、单个 Z 值与五椭圆一阶行的消费契约

日期：2026-11-16。状态：**真实来源与可续执行接口；尚未运行新的 41 进算术。** 本文接已冻结的 [41 域、好模型和倍率稿](2026-11-16-original-41-adic-field-good-model-and-sigma-input.md)（下称 41S）以及 SP。它不更改 R850、529 节点点程序、733 节点一阶程序或原辅助素数计算。

最小数值目标是原 $f=f_4$ 的一个
$\mathcal Z_b(f(c_1))\in L_{41}$ 有保证精度的球。七个共轭由真实 $\sigma$ 运输；五个椭圆一阶组合只需要这个球、原切向、$\rho$ 和准确斜率。原 $Y$-Picard 项、全局 $\ell_h$ 与原高度保持独立。

## 1. 原点来源的实际前沿

本次纯 IO 已读真实 R844 和 R846 程序。R844 有 $529$ 个节点；R846 逐字继承这 $529$ 个节点，总数为 $733$。它们共用同一个 $2420\times2420$ unit_chart_solve 和四个 linear_response。不存在第二个隐藏的待解线性系统。

| 精确对象 | 实际字段／来源 | 41 处状态 |
|---|---|---|
| $b,\zeta$ | 两个 original_field_generator；$\zeta^2+\zeta+1=0$ | 精确定义已成；新模精度表示尚未算 |
| 原单位图 | free column $1186$、其他 free 坐标 $0$、原行序和带符号 $Z$ | 精确定义及可逆性已成；41 处数值求解尚未算 |
| $A_0,A_1$ | 原 $(e_0,0)$、$(e_1,0)$ 泛函 | 尚无实际 41 球 |
| $B_0,B_1$ | 原 $(e_iZ)[1186]+(0,(e_iZ)_{\rm piv})$ 泛函 | 尚无实际 41 球 |
| $h_i$ | R791 actual_L_coefficients_h_i_over_ds_at_c1，共十二条 | 准确原 $L$ 坐标已成 |
| $\rho_j$ | R791 rho_iterates_zero_through_seven，本程序直接使用五条 | 准确原 $L$ 坐标已成 |
| $\sigma$ | R791 field_sigma_b，固定原 $\zeta$，作用于整个准确表达式 | 准确原域自同构已成 |
| 非零分母 | R841 原 $B_0,N$ 证明；R843 同一点非挠；R844 Hom 字 | 准确结论已成；实际 41 赋值尚未知 |

旧键名 over_ds 中的局部参数仍是原 $z=a-1$，不是 CM 常数 $s=1+2\zeta$。733 程序共有 $17$ 个 source_field_element 叶：十二条切向与五条 $\rho$。这些是准确有理数域系数，不是待猜的数值。

四个响应的实际节点 ID 为：

- $A_0$：df6f79bf61aa7e45aa64e7c8c41d71931149981dc98e2c15c85f2d84bc61a003；
- $A_1$：36654715fce2f382459a02034ad56a2ae3f02f7cb560476722b414ae5e69bd7b；
- $B_0$：34111de3daeff665213d65dbee07fd2595797fbbaff1d57db1cc58faf3bd3c7e；
- $B_1$：992e92890e48c629ed973846db3d5255e9021dff9a3ab38bb848dcb206c98bcf。

它们引用同一原 solve 节点
1fd48e17a8801b2125bb57c1ce0811d4736c7bcd5aabd07dd4a7d83d103d9d98。
实际 four-response 的辅助 $518$ 位球、短有理重构候选、原非挠证书使用的辅助球，均不能填入本表的 41 数值栏。

### 1.1 两条现有 carrier 路径

R850 的封装保留：

1. GLOBAL 原 R839-global-polar-retained-original-inputs.tar.gz，$395061658$ bytes，SHA256 $6a0a5d8cc918f1802662865dfaf254987f33086191ce01e9169ec789b5456703$；其原 source inventory 记录 $2709$ 个成员。
2. POINTS 原 R792-log-jet-padic-retained-inputs.tar.gz，$2078830$ bytes，SHA256 $a7ccfe9b61d59233e622505afd0a664e18be8d1384a093b446b8b02bf7b9ddb1$；原 receipt 绑定 $270$ 个成员。

第一条给原 R781 Laurent/字段、R787 的 $1234$ 条真实行、chart、带符号 $Z$ 等 U.1 闭包；第二条给 CM 的准确 $e_i/e_iZ$、原点、切向、非挠与 Hom 程序。后继既可沿已成功的 R850 carrier 取这些原字节，也可沿原 GLOBAL/POINTS 成功来源取同一成员。必须核实际 parent receipt→child identity→member SHA，不能只用一个 DAG 内的未核路径字符串。

R850 已成功：run `43796696213`、source `57b2899f61cb23b73bc7b8532f3ee78d28206`、artifact `14194427829`，archive SHA256 `b466d4c1cb6e0b495e3ca1ba892406d9e51c771b75769505dfec2a8bd49a11c3`；原输入 carrier SHA256 `a4c38c0efd02433b501f62fc2e93b83dacd01299a8f8d5843cc0fadbfef92bc8`。准确登记见 [R850](../results/R850-certified-original-rigidified-Poincare-fibres-and-sections.md)。也可直接按 R850 冻结 request 的原成功来源取同 SHA 成员；运输路线不改原成员数学身份，不授权重标旧 configuration。

## 2. 数值留在原十四坐标域，公共 E 只负责证明

令 $\pi=B=\lambda b$，$\lambda=2^6 3^{180}$。使用
$$
L_{41}=\mathbf Q_{41}[B,s]/(F_B(B),s^2+3),\qquad
v_L=7v_{41},\qquad v_L(\pi)=1.
\tag{41C.1}
$$
$F_B$ 就是原 R781 的 integral_B_minimal_polynomial。$\lambda$ 为单位，故 $F_B$ 仍 Eisenstein；$\mathcal O_L=\mathbf Z_{41}[s,\pi]$。按
$$
1,B,\ldots,B^6,\quad s,sB,\ldots,sB^6
\tag{41C.2}
$$
保存原十四坐标。

41S 的公共域仍为 $E=\mathbf Q_{41}(s,r)$，$e=42,f=2$、$b=16r^6$。但 $P,[42]P\in C_b(L_{41})$，而 41S 已证明原参数满足 $v_{41}(\xi)\ge0$、$v_{41}(\xi^2x-1)>0$。因此直接在原 $C_b$ 上求 SP 的 $u,w,H,F,\mathcal Z_b$，所有数值运算可以留在 $L_{41}$，不必材料化 $84$ 坐标的点值。

这不丢原帧常数：直接使用原 $b,\xi_b,\psi_{b,42}$ 就是在原帧计算。若实现改走好模型，必须执行 41S 的
$\mathcal L_b=\mathcal L_{16}-\log r$、
$\mathcal Z_b=r\mathcal Z_{16}$；
两种路线不能混合一半。初版固定为原模型十四坐标路线。

球以整数绝对精度 $N=v_L$ 记为 $x+\pi^N\mathcal O_L$。其第 $i$ 个 $B$ 次幂的两个未分歧坐标，分别至少保至
$41^{\lceil(N-i)/7\rceil}$；负指数按实际分母保存。输出必须同时给这个整数 $N$ 与 $N/7$ 的 $v_{41}$ 意义，不能把 $N$ 称为 $N$ 位 41 精度。

加法取精度下界的最小值。若 $v_L(x)=m<N$ 已实际确定，逆的绝对精度为 $N-2m$。乘法按两个输入的实际赋值下界传播。若剩余表示全零，只给 valuation_lower_bound，不能把它写作准确零或准确赋值。域自同构 $\sigma$ 保持唯一完成处，是等距作用；完整元素球的误差下界运输不损失。

数值环可用十四个整系数、$F_B$ 和 $s^2=-3$ 的准确约化实现；只有真实单位才作 Newton 逆，非单位先记录 $\pi$ 次数。不能调用仅假定素数模数的矩阵 inverse API 去求模 $41^N$ 的一般逆。python-flint 0.9 的 [nmod_mat](https://python-flint.readthedocs.io/en/latest/nmod_mat.html) 与 [fmpz_mod_mat](https://python-flint.readthedocs.io/en/latest/fmpz_mod_mat.html) 的相关假设应按官方接口保留。

## 3. 四响应的真正有限精度接受

令原 U.1 系统为
$$
M u=r,\qquad
u\in L^{2420}.
\tag{41C.3}
$$
$M,r$ 的具体符号、行序和清分母都从原表达式读；不得用相同数字行号替换成另一套行清分母系统。四响应为
$\ell_i(u)+c_i$，其中 B 响应含真实 free-column 常数项。

$M$ 准确可逆和 $B_0$ 准确非零已证明，但辅助 $\ell$ 单位性不提供 41 单位性。一个实现只有在保存实际逆范数界后，才能把小残差称为准确球。

**一个确定的接受界。** 选准确公共尺度，使 $\widetilde M,\widetilde r$ 整。若实际有限精度 determinant 计算已确定
$v_L(\det\widetilde M)=d<\infty$，则 adjugate 的各项整，故
$$
v_L((\widetilde M^{-1})_{ij})\ge-d.
\tag{41C.4}
$$
若候选 $\widetilde u$ 的原完整残差每项赋值至少 $R$，则
$$
u-\widetilde u\in
\pi^{R-d}\mathcal O_L^{2420}.
\tag{41C.5}
$$
响应再按各准确 $\ell_i$ 的系数赋值下界传播。原尺度必须同时施于 $M,r$，响应本身保持原规范。

也可使用更小的实际 LDU 界：在 DVR 上每步选择当前子块赋值最小的非零 pivot，全部消元比值整，得到两侧整可逆三角因子与对角 pivot。若最大 pivot 赋值为 $\gamma$，其准确逆范数界是 $-\gamma$。有限精度实现必须证明该完整分解或相应可收缩误差界；不得只记录 pivot 数字便推此结论。

以上两种途径都不要求材料化特征零有理逆。原模 $1000000753$ 的逆仅作为旧来源保留，不能冒充 41 处求解算子。最初若尚无 41 factorization，就明确执行一次新的目标地方求解；其实际时间和损失不能预报成已完成。

每个完整精度层须保存：

- 原矩阵来源及全局 U.1 身份、此次准确清分母；
- 实际 pivot/分解或 determinant 非零证书及逆范数界；
- 完整原残差下界；
- 四响应各自的原泛函、常数项和所得绝对精度；
- 已成旧精度层的来源与新层对其降精度相容性。

提高精度只续原系统，不改 free $1186$ 或替换原图。成功的四响应球与“已展开的准确有理坐标”是两种输出；前者足够本次 41 解析求值，不声称 A.1 已通过。后继若真有 A.1，可用一个独立、实际认证的等值输入适配器，无须重跑已足精度的节点。

## 4. 一个 Z 与七个原共轭

给定四响应的真实 41 球，读取原节点
$$
y=\frac{A_0}{B_0},\qquad
y'=\frac{A_1B_0-A_0B_1}{B_0^2},\qquad
x=\frac{3h(y^2-b)}{y'}.
\tag{41C.6}
$$
这是 R841 对 R791 原公式的消费，不是新坐标猜测。只在 ball 已识别所需非零分母的有限赋值后求逆。原纸证给最终可识别性；不足精度返回精度需求，不能改分支。

原 $\sigma$ 节点要求对整个 unit-chart 和全部常数作共轭。数值上先得到同一原十四坐标的响应，然后施加已认证 $\sigma$ 的连续域作用，正是该 whole-expression 共轭。无须七次独立求解。缓存键必须记录原节点 ID、$\sigma$ 次数、原域身份及数值精度；不能只改 $b$ 而沿用未共轭的响应。

记 $P=f(c_1)$。SP 的 Z 公式只含原有理函数、整数系数收敛级数及准确分母，故
$$
Z:=\mathcal Z_b(P)\in L_{41},\qquad
\mathcal Z_{\sigma^kb}(\sigma^kP)=\sigma^k Z.
\tag{41C.7}
$$
证明：$[42]$、原 $\xi$、规范 $\psi_{42}$ 和 $D_\omega\log\psi_{42}$ 全部与域自同构相容，SP 级数有理系数；$\sigma$ 连续且等距，可与收敛和交换。该论证没有把真 $\rho$ 运输换成相位为一。

所以新解析运算只需求 **一个** $Z$，其余七分量由原 $\sigma$ 作用取得。其误差也按等距作用保留。原 Galois 曲线 $C_{\sigma^kb}$ 的点与已输送回同靶的 $T^kf$ 仍是两种标签，不可互换而省略 $\rho_k$。

对这些原 $L_{41}$ 值，公共 $E$ 上的规范化 trace 限制正是原 $L_{41}$ 的规范化 trace：$[E:L_{41}]=6$，故 $84^{-1}\operatorname{Tr}_{E/\mathbf Q_{41}}=14^{-1}\operatorname{Tr}_{L_{41}/\mathbf Q_{41}}$。原角色尺度仍按 SP 保留；这个等式没有额外六倍或七倍的自由归一。

## 5. [42]、规范 psi 和有限尾

首次固定 41S 链
$$
1,\ 2,\ 4,\ 5,\ 10,\ 20,\ 21,\ 42.
\tag{41C.8}
$$
每个 point multiplication 节点以原点身份、整数倍、输入精度为键原子保存。旧 R843 非挠性和 Hom 字给每个加法/doubling 分母准确非零；若本层未识别其赋值，先增加四响应精度，不创建虚假的完成节点。

规范 $\psi_{42}$ 及其 $D_{\omega_b}\log$ 采用 SP 的 $\psi_2=-2y$。可在原 $(x,y)$ 上以双数
$$
D_{\omega_b}x=2y,\qquad D_{\omega_b}y=3x^2,\qquad D_{\omega_b}b=0
\tag{41C.9}
$$
作记忆化除法函数递推。它是有限有理函数值，不需求椭圆积分，也不展开整个高次多项式。各递推节点同样保已完成值；原辅助素数的任何球不参与 41 运算。

在 $P_{42}=[42]P$ 上，核实际球所能读出的
$\xi=-x_{42}/y_{42}$ 和 $u=\xi^2x_{42}$；41S 已证明终将满足
$v_{41}(\xi)\ge0$、$v_{41}(u-1)>0$。据目标精度选择 SP/41S 的完整余尾界。只在此后生成所需新 universal 系数：

- $u(v)^2(1-u(v))=v,\ u(0)=1$；
- $w=(3u-2)^{-1}$；
- $H=b\xi^4(9u+4)/(u^2(3u-2))$；
- 原 $\mathcal Z_b([42]P)=(3u-2)/\xi+\int_0^\xi H$。

通用整系数按已成前缀续算，实际求和按项块保存。积分中的 $6n-1$ 可能被 $41$ 整除，必须按真实分母损失计入，不能用“整 H”替代“整积分”。Rational 项 $(3u-2)/\xi$ 单独精确追踪球精度。

最终
$$
Z=\frac{\mathcal Z_b(P_{42})}{42}
-\frac{D_{\omega_b}\log\psi_{b,42}(P)}{42^2}.
\tag{41C.10}
$$
两个整数分母均为 41 单位。初 scope 求的是 Z 与可选的 log-sigma 原函数 $F$；**不直接对 $F$ 作 p-adic exp**。SP 的 line-log 用 $\log\xi+F$，并不需要在未证 exp 收敛的范围生成数值 $\sigma$。

若后来确需 line-log 值，须另绑定原 $\log_{41}(41)$ 分支和原角色。按原 $L$ 均匀化元把非零数分成 $\pi^m$ 与单位，单位可用其有限剩余群幂进入 $1+\mathfrak m_L$ 后求 log。该额外步骤不属于无对数分支的 Z 核心，且不得删原帧或 RF 常数。

## 6. 五个椭圆一阶行的下游接口

原 $\alpha=1-\zeta^2$ 三同源法则和 RF/SP 的比较已经由 [ZA](2026-11-16-original-three-isogeny-sigma-and-one-Z-period-contraction.md) 证明，正式文件 SHA256 `268fa3fbb9647d7f6f3f781534d9425e09c45ad7945e9aea9a9abd2082834d97`。其 (ZA.29)–(ZA.32) 保留规范 trace、外因子7及原 $Y$/Hecke/非41校准项。按该缩小，五行只需原
$a=h_f$、$Z$、$\rho_j$ 及
$$
c_j=\frac{y(T^jf)-y(f)}{x(T^jf)-x(f)}.
$$
所有斜率分母由 R843/R844 原 Hom 字证明非零，点和切向读取原 529/733 节点，不重建另一组同态。

设实际原比例为 $p_j/q_j$。与该正式公式一致的源对象是
$$
\beta_j=3\left[(2-p_j/q_j)a+
\rho_j\sigma^j(a)+
\sigma^{-j}(\rho_j^{-1}a)\right],
\qquad
d_j=3c_j\left[a+\rho_j\sigma^j(a)\right].
\tag{41C.11}
$$
原 $41$ 唯一完成处保证 normalized trace 在 $\sigma$ 下不变，故一个 $L_{41}$ 球 $Z$ 足够组合相应五行
$7\operatorname{tr}_{\chi,L}(\beta_j Z+d_j)$。此阶段必须 pin 该正式三同源/trace 缩小证明；证明文件尚未列入实际 config 时，运行目标停在 Z，不能假装已完成五行。

$\rho_j$ 是原 R791 值，$T^7=\zeta^2$ 保留；它不是一个无相位周期比。即使五个椭圆一阶行都得到准确有限精度球，原 $Y$ 项和 $\ell_h$ 仍未计算，final 的 actual_height_computed 必须为 false。

## 7. 可续 Actions 的接口分层

拟新 RESULT 为 original-p41-CM-sigma-base-Z-input，独立 core/source/tag；不冒用 R847 或 R850 核。标准 CLI 为 --config、--retained、--output、--budget-minutes。数学 tag 固定原 p41、原模型/字段、原 DAG/来源、U.1 图、SP/41S/本契约证明、固定倍率和 sigma 规范；预算及 requested precision 排除在数学身份之外。

推荐阶段如下：

| 阶段 | 完成条件 | 续算粒度 |
|---|---|---|
| source audit | parent/child/全部选取成员 SHA；529/733原节点一致 | 一次，不重下载 |
| field model | 原 $F_B,\lambda,s$、完整标签和球编码 | 一次；不另找 b 根 |
| original operator | 同 U.1 行与清分母来源 | 原系数块 |
| response layer | 真逆范数界＋完整残差＋四响应球 | 精度层／消元块 |
| base-point layer | 原 R841 分母已识别及 $(x,y,h)$ 球 | DAG 节点与精度层 |
| multiplication 42 | 固定七步均已成、输入标签一致 | 每个倍点 |
| psi42 dual | 原规范值与 Dlog 球均有保证精度 | 每个递推节点 |
| sigma coefficients | 只需的整系数前缀 | 固定项块 |
| base Z | 全尾证书＋有理项＋(41C.10) | 每个精度层 |
| sigma orbit | 原七共轭与等距精度 | 同一已成 Z 的运输 |
| optional five rows | 正式新证明已 pin、原精确系数/斜率、真 trace | 每个目标行 |

每个已成阶段列完整 file/bytes/SHA、source configuration、absolute precision 与父阶段；阶段工作状态 complete=false 单独保存。原子写临时文件后 rename，再推进指针。外层 timeout 必须保已成阶段、真实退出码和完整输出 manifest，不能因没有 FINAL 或 core receipt 伪造成功。续算只恢复同 tag 的完整节点和真实 current；旧来源保持原字节与原 tag。

首次配置不能预填任何新 41 ball。可选外部 response41 来源只有在它已实际完成且满足 §3 的同图/误差契约时才可导入。不存在时由本 run 的 response scope 生成；若预算结束，诚实停在已成精度层，sigma scope 不以空输入启动。以后实际 A.1 是另一显式输入适配，不改旧值身份。

最终至少分开以下状态：

- exact_original_point_expression_source_verified；
- actual_41_responses_computed 和 response_precision；
- actual_original_41_base_Z_computed 和 certified_absolute_precision；
- original_seven_conjugates_transport_verified；
- actual_elliptic_first_derivative_rows_computed；
- exact_expanded_rational_point_coordinates_certified（当前路径为 false）；
- actual_Y_Picard_period_computed=false；
- actual_height_computed=false。

“complete”仅指此次已请求的 scope 完成，不将尚未请求或尚未得到的高精度、Y period、原高度填为成功。

## 8. 已核小源 pin

本契约按已有 R850 carrier 检查这些具体叶：

- R844 program：$68403$ bytes，SHA256 $97a8fb3f185660468e6637358c9c29b34bfe8630599f36fa7e7f58ef6acb582b$。
- R846 program：$93533$ bytes，SHA256 $555e3c6c877ef2b3fb64f0dfe17f463f49fd6ca83bb1a1faedc2db562724547b$。
- 原 CM implicit expression：$72708$ bytes，SHA256 $21cc66ed9a40a856edea495080ef2e375aefea6c6f17d6c26741b85e2f174342$。
- 原 power5 exact-jets index：$10694$ bytes，SHA256 $455eaf217279f7cda39f57cfb0774f72caa1e24d36ad369f964d9eceaef389a5$。
- 原 exact-eZ index：$3981$ bytes，SHA256 $acd7adb6ba2972829b3be41e128356031b55c0457f0db9e3b270015c60392e5e$。
- 原十二切向：$20760$ bytes，SHA256 $32be372f46560ce7cfc0af40666cdc32b39170bfc7b6ec32b92ea747a0629e7e$。
- 原 Hom/Galois：$15617$ bytes，SHA256 $f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183$。
- 同一点非挠 certificate：$6446$ bytes，SHA256 $e4f926d374b5225c45036b363f4cc8a0e4918f54a711e2c3e824f803f3a8e506$。

具体大源以这些 index、GLOBAL inventory 和原 manifest 动态展开，不把数千条 SHA 或机器回执写进本证明。所有新算术只能在本公开仓库的 Actions 内执行；本篇没有执行其中任何数值阶段。
