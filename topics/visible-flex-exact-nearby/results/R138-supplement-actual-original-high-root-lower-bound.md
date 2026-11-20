# R138 补篇：实际完成原 high97 根压缩的严格正下界

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**已证明（公共有向计算）：** 同一固定 `Qrepair`、真实根、真实 periodic frame 与原 low1..96 / high97..infinity 分解下，原根型的完整 high 压缩具有严格正下界。public run **44750653724/1** 完成全部32768个闭角格、41条新 scalar records；保存的下界约为 `0.722619734714693…`。本篇的严格结论使用完整保存球的下端，展示小数只供阅读。

已成 signed96/97 负方向与全部旧输入原样保留。这个 high 压缩的正性尚不等于完整根型正性、原正区边值逆或 R141 的低193混合算子逆。

## 1. 实际运行和完整文件身份

workflow event commit 为 `50ea0be3b5bdb13607eeb7b535178b374e6f36a8`，实际 scientific checkout 为 `364ce99a7100813bda712ec8f8165b6cc6e4cb4b`。以下为完整文件的 bytes 与 SHA-256：

| 对象 | bytes | SHA-256 |
|---|---:|---|
| [frozen manifest](../notes/2026-11-20-R138-original-high-root-lower-bound-inputs.json) | 13520 | `5a33312d1b738abd3a8d4686244c33298167181b41e926212433a48dc09e783e` |
| [whole scientific result](../notes/original_high_root_lower_bound_ci/run-44750653724-1/original-high-root-lower-bound.json) | 53310 | `f3f97be683009e9c8ae461c25dfd17d782a61ea6feaf9b8b7967b3e28a9e835d` |
| [whole execution](../notes/original_high_root_lower_bound_ci/run-44750653724-1/execution.json) | 15691 | `e753dd0ea848302ccbe41dc90a3cd8ab1a1a211985d7a7d3691d7ab6384a7687` |
| [scientific source](../scripts/fourfold_codazzi_original_high_root_lower_bound.py) | 31180 | `1bd839a44ce1075e4906fddee14b5bc56e737740538e22c4b763c4715821da35` |
| [public worker](../scripts/fourfold_codazzi_original_high_root_lower_bound_public_worker.py) | 31695 | `2cd84dd9529255ab9719906d46868037167db4f83dc0cba03d4f7ecd500d19ad` |
| [complete scientific contract](../notes/2026-11-20-R138-original-high-root-lower-bound-contract.md) | 12692 | `6124234adf7967e2d87e13457dacac03dcd2f4000224c11244d5d45515092785` |

runtime 为 Python3.12.14、NumPy2.3.5、python-flint0.9.0、320bits。单一科学 child 的数学时间为19.66021421000002秒，child wall 为19.754728083999993秒；returncode0、无超时、无failure。scientific 的 `complete/proved` 及 execution 的 `complete/original_scientific_complete` 均为 true。全部32768角格完成，新的完整 high 根目标计数为1。

独立后验 metadata 审读逐份核24个current文件的UTF-8 bytes、SHA与Git blob，4个Python源作AST静态检查；26个科学顶层字段与manifest完全一致。六份原始历史对象的全部恢复spec和 `exact_original_bytes_verified` 记录逐项一致。这里没有本地重新运行科学代码、恢复数组或求值新的算子界。

execution记录5次README检查，并按worker明确策略只保首条与最近3条完整收据。已从实际job `136337349911` 的完整公共日志取得全部5条收据，并独立核对首条加末3条恰等于execution所留4条。所有5条的两个README `actual_diff/diff_from_read_commit` 均为空，reviewed-rules SHA与manifest相同。依原worker的canonical encoding逐条重建完整5条累积链，恰等于execution保存的

`7442cbac7bee25b975d275bbf4a1d5d1c8cdbeb2c3894ccceec045ef99faa4be`。

该次审读使用的5条完整收据metadata为3433B、SHA `68417e48d9d0071683e486caecc5883fd775f1f599964bdd7fadede5d3347970`；本篇不重复发布日志或冗余收据。这里核的是全部5条链，未把保留的4条误认为全部检查。

## 2. 同一个实际对象与原始结论的只读资格

实际对象SHA为 `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`，完整repair-definition SHA为 `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。固定参数为

$$
\eta_0=-7789843107295549/4611686018427387904,\qquad
\nu=-2572625729470897/72057594037927936.
$$

真实根位于原精确区间

$$
[1191984371497/5000000000000,\ 2383968743003/10000000000000].
$$

几何输入仍为同一 `p=(0,0,1/2)`、`X(root,0)=e_z`、`Y(root,0)=e_y`、`n(root,0)=e_x`；使用完整moving-$\phi$圆圈、归一角内积，实际frame满足 $X\times Y=-n$。原scalar odd-fourfold空间、真频率 $4j$、low1..96/high97..infinity 与

$$
S=P_LN+P_HN^{1/3},\qquad N=|D_\phi|,
$$

完全不变。最小high频率为388。这里没有高未知量截断、没有把人工轴误差矩形的各顶点当成真实几何，也没有把固定 `Qrepair` 换成WVC的same-eta hybrid。

实际结果的 `whole_original_references.two_mode` 与旧 signed 原件逐字节对应的完整JSON对象相等；其内部 axis、mean、physical-budget 三个whole对象又与本次各独立输入完全相同。这四个旧科学结论及其四份完整execution均核了run/attempt、0 returncode、complete、failure和whole scientific文件SHA：

| 完整旧结果 | run/attempt | whole scientific SHA-256 |
|---|---|---|
| actual axis | 44730968113/1 | `b300ea209acb2239a93a87aa3f14d6d9c5f0ed3b5b88ea44b415e5078ea0cd92` |
| actual independent mean | 44733403315/1 | `de3a14606aa432fbd1f7707c277a33110f81ce6ca23fdfc6bfdf7e9d497623b4` |
| actual X root defects | 44737045152/1 | `1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec` |
| signed96/97 form | 44745192261/1 | `95c80fdeeb3cf75327f028b1020db5aeda0fa3502aa6c0b3546c17ac6d2258c2` |

旧 `negative_two_mode_direction_proved`、`all_root_data_nonnegative_form_excluded` 与严格负determinant均仍为true；旧的actual BVP singular、positive inverse和final topic flags均仍为false。本次high下界没有覆盖、删除或推翻这些结论。

## 3. 严格结论及保存球的消费方向

沿[HC.1–HC.16合同](../notes/2026-11-20-R138-original-high-root-lower-bound-contract.md)与[完整high principal/signed compact证明](R138-supplement-original-high-principal-and-signed-compact-bound.md)，记原high根型的压缩为 $D_H$。本次保存

$$
D_H\succeq\lambda_HI,\qquad
\lambda_H=a_{\min}-\varepsilon_{\rm pr}
 -\varepsilon_{\rm loc}-\varepsilon_m-\varepsilon_I.
$$

其中实际principal的二阶导由完整frame/position缺陷导数支付；实际mean分母来自完整旧mean，六项signed局部余项、全部mean rank及两个环境primitive均保留。环境primitive的最低非零频率为1；near/far收紧使用194/388两门槛，未借scalar四重的1/4替换环境常数。

`complete_actual_high_lower_bound` 是这个明确算子下界的保存球；不是声称实际最小特征值落在该窄球内。取该记录的严格下端后即有正的统一高频二次型下界。保存的 `high_lower_bound_positive=true` 与完整decimal记录的严格符号相符。

`complete_receiver_coefficients.kappa_upper` 的完整上端严格小于1，`receiver_neumann_gate=true`。该门仅支付[relative receivers证明](R138-supplement-original-high-compression-and-relative-root-receivers.md)中R.7–R.9明确的odd/even两种restriction的 $L^2$ Neumann逆；具体有限接收器 $W_L$、完整 $r_E,r_B$、有限负方向接收及其三门还须另付。

后继应消费所有 `*_upper` 记录的有向上端，以及 `principal_a_minimum_lower`、`complete_actual_high_lower_bound` 的有向下端。41条记录的完整JSON语义均为 `complete_decimal_ball_v1`：整数串 $M,R,e$ 表示

$$
[(M-R)10^e,(M+R)10^e].
$$

下列各表逐字抄录原整数串和指数；没有将它们改成展示中心、浮点数或本地新球。

## 4. 全角系数：17条

| 完整记录字段 | midpoint_integer | radius_integer | decimal_exponent |
|---|---|---:|---:|
| `A_RR_negative_upper` | `9555152952088974416255950927734375000000000000000000000000000000000000000000000` | `1` | `-81` |
| `A_RT_absolute_upper` | `19664593727623862958422624258303462359517887491832798855430908750627133129059758` | `2` | `-80` |
| `A_Rq_absolute_upper` | `26383877114508729238363723788810964010371910763027388488262396820416277406968561` | `2` | `-80` |
| `A_TT_negative_upper` | `8070580300409346818923950195312500000000000000000000000000000000000000000000000` | `1` | `-80` |
| `A_qT_absolute_upper` | `14936950824409870806951734024201831356256973533162847131348468899549877700775256` | `2` | `-82` |
| `A_qq_negative_upper` | `12147115996808971195743004118161122717434394189569288046806947621776887256524208` | `2` | `-78` |
| `G_0_upper` | `13784272431893363265249786395254993038654959268261564626206390803539212563636138` | `2` | `-79` |
| `G_1_upper` | `17518176713629264398378652954639656056715492443876462782338210161081066610303750` | `2` | `-79` |
| `b_0_upper` | `97982073528694968272257205879616215327132522361353039741516113281250000000000000` | `0` | `-80` |
| `b_1_upper` | `10041213735176920270654919047508782141031609946214513537127373576570221687056627` | `2` | `-79` |
| `b_2_upper` | `10290424972243343164326446506649033101816553949789308200692562450643631964426231` | `2` | `-79` |
| `c_0_upper` | `19238341329624366210970775517579631521856209236781867188642787130394256831978823` | `2` | `-80` |
| `c_1_upper` | `43039167760607970726761228860493031526576482981217653267289574553225711100843733` | `2` | `-80` |
| `g_m_0_upper` | `20054106966560056095066517802158249350029002125744061514394302885891385629291873` | `2` | `-79` |
| `k_0_upper` | `20054010158334484062711409639452771277695251097856746318511462196489462737097829` | `2` | `-79` |
| `principal_a_minimum_lower` | `95380143123156621576687579895859912519446558837852569151850349340528733238187284` | `2` | `-80` |
| `principal_a_second_upper` | `10787199794230858425071091669228098557486506596317005049219449275001422018811479` | `2` | `-77` |

## 5. 接收器系数：9条

| 完整记录字段 | midpoint_integer | radius_integer | decimal_exponent |
|---|---|---:|---:|
| `V_0_upper` | `11690512192097375154210973733334913708788319256812763195835156795583519387573407` | `2` | `-79` |
| `V_1_upper` | `26153357216730689991780786009623043711686317584974820818258513570379844726166619` | `2` | `-79` |
| `X_1_upper` | `62421731024083548866918282197549345963731849739323248036282357548200019630504228` | `2` | `-80` |
| `chi_0_upper` | `47949001470514076572726480662822723388671875000000000000000000000000000000000000` | `2` | `-79` |
| `chi_1_upper` | `16169174573616896771128159864566911108707862596674588017643407395323596641057048` | `2` | `-78` |
| `chi_q0_L2_upper` | `14174372627266783996912051660791550946087566654288280943165616587099678764267575` | `2` | `-80` |
| `kappa_upper` | `9013464455406403659882376347858947823639708171954039805787210831543108965605764` | `2` | `-80` |
| `m_absolute_upper` | `11198066337645620065639102966706807770895887870237809141262428951748981438285388` | `2` | `-79` |
| `rho_inverse_upper` | `10206889417022466659545898437500000000000000000000000000000000000000000000000000` | `0` | `-79` |

## 6. 完整high误差项：9条

| 完整记录字段 | midpoint_integer | radius_integer | decimal_exponent |
|---|---|---:|---:|
| `E_H_upper` | `19027582595275141188290590675695485398737144342811230725563122339493458740173781` | `2` | `-81` |
| `I_H_upper` | `79984890061786771433257709453712885619673991998831151980275250359692871048408247` | `2` | `-83` |
| `L_H_upper` | `23757791386519020775663358214982141618157954928745392717806296998589801470923515` | `2` | `-83` |
| `V_H_upper` | `19504023885029612777190658745431519414702144089499477748615427748056794231834462` | `2` | `-81` |
| `Y_H_upper` | `29343895259843969800232633610938486044218112443676680049806963062331807621581571` | `2` | `-80` |
| `complete_primitive_error_upper` | `43266740124358122721114350519722928427053246279879304719052795170979774542412913` | `2` | `-83` |
| `mean_rank_error_upper` | `38542599215147999428453726014431913696844925785607010221395741877095886009113664` | `2` | `-83` |
| `principal_error_upper` | `13370719440800153052654049273487539758681553393889763952288860646161549357561962` | `2` | `-82` |
| `signed_local_error_upper` | `22902653117939804423433886383892583121746953259345322907960377515013070226198073` | `2` | `-80` |

## 7. 实际high下界：1条

| 完整记录字段 | midpoint_integer | radius_integer | decimal_exponent |
|---|---|---:|---:|
| `complete_actual_high_lower_bound` | `72261973471469309500577584942698299157988891872502862289426634682005971857862060` | `2` | `-80` |

## 8. 非齐次源系数：5条

| 完整记录字段 | midpoint_integer | radius_integer | decimal_exponent |
|---|---|---:|---:|
| `C_H_cross_upper` | `37084944312472576732743845167079547240378956634990946161422075683523975862469735` | `2` | `-79` |
| `C_L_upper` | `32654883758779462178440008143698676673306994224110360539381349188373924841765741` | `2` | `-78` |
| `C_omega_H_upper` | `29423880149905756571665891320392198929837786435675511201787238312691500492629981` | `2` | `-80` |
| `C_omega_L_upper` | `25908988238773734745685847288464590269034469010637847040797471773200676617874994` | `2` | `-79` |
| `C_quad_upper` | `18404048763371519615249086907951161636983765207859948354132020235243603531762646` | `2` | `-78` |


## 9. 已完成资格与尚待真正闭合的量

五条非齐次源系数精确对应[原根源消元证明](R138-supplement-root-source-elimination-and-concave-finite-gate.md)的 $C_{\omega,L},C_{\omega,H},C_L,C_{H,\rm cross},C_{\rm quad}$。它们保留实际mean消元和全部环境primitive；不能把它们重新解释为对所有原root数据成立的单一无正负区分能量界。旧signed96/97负方向正是必须显式保留有限负块的理由。

本次新scope明确给出同一 `Qrepair` 的true root、原low96/all-highrows保持、独立mean按实际已存分母消去、完整high压缩下界和正性，以及上述有限restriction的Neumann门。它没有给出完整positive inverse、实际边值奇异性或课题完成。

全部旧axis、mean、X、旧两模矩阵、旧Z/P传播与旧geometry目标调用计数均为0；`published_arrays=false`，无新数组、artifact或Release。原candidate/germ只私有恢复定义，新的geometry只服务这一个新增scalar目标。整个新结果与41条完整保存球现应冻结为后继只读输入。

继续可执行的缺项是同一个真原始算子下有限负root接收器和它的完整非齐次消元，及相关有限三门；R141的实际低193 inverse、完整physical97+96外块、原七高端口和两条WPN右端仍按它们各自的同对象合同支付。不能由此high正性把固定候选、原真线性化、same-eta hybrid或旧finite-trial $F$互相替换。
