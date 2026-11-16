# R870：原有理 Picard 挠点与 Hecke 支持输入的整数消费者

日期：2026-11-16。状态：可执行契约；原 T₇ 的矩阵、谱及 CRT 投影已经由 R865 完成，本次新的整数和八十条原 Picard 判定输入尚待公开 Actions 实际输出。

数学证明为 [R870](../results/R870-original-rational-Picard-torsion-and-T7-support-certificates.md)。原算子来自 [R865 的对应证明](../results/R865-original-Hecke-T7-from-certified-level82-Fourier-rows.md) 及其 [实际成功结果](../results/R865-certified-original-Y-Hecke-T7-and-squarefree-spectrum.md)。本方法只新增原最小多项式在8处的整数恒等式、各谱因子的挠点消去整数、已有整数投影的共同分母，以及绑定原五个 Picard 输入的有限判定计划。

## 1. 三个真实来源与四十二个原文件

逻辑来源为 R865、GLOBAL、FIBRES，分别保各自的原 result、run、source、core、configuration、成功证书与完整 manifest 身份。R865 采用成功 run43817070047；GLOBAL 是 R849 所登记的原全局五极理想 DAG，来自 run43790410670；FIBRES 是 R850 原刚性化纤维 DAG，来自 run43796696213。所有参数从真实成功文件读回，不由本程序预测谱或填写计算结果。

最小选择为 R865 的26件、GLOBAL 的8件和 FIBRES 的8件，共42件。每组保完整原 manifest、原 public/run/core 三件、成功证书、source audit、stage manifest；两种 DAG 各保其原完整小程序。R865 另保真实八双陪集说明、特征与最小多项式、谱投影索引及16个原 CRT 投影阶段。

本次不消费旧127维矩阵、不重建 Fourier 行，不下载或宣称重新核过约395 MB的原全局输入载体。原 GLOBAL/FIBRES 证书证明此前已经完成的表达式组装；所选小 DAG 本身及其引用身份仍完整保留。后继确要执行 norm–RR 或展开极理想时，必须另行取得当时仍活跃的真实必要叶，不能将本次小选择冒充整个旧大载体。

包装器以冻结 R824 标准库 Range 工具读取不可变 artifact。平台 ZIP digest 作为 API 返回的原身份，所选成员逐 bytes/SHA 核验；局部 Range 读取不称为重新计算整个 ZIP digest。所有42件原字节装入本次一日最小载体。数学核心只读此载体的已展开目录。

原 GLOBAL/FIBRES 的 public 输入使用 driver_sha256，R865 使用 wrapper_sha256；包装器按这两个已存在字段读取真实旧驱动身份。FIBRES 的旧 core receipt 没有 process_exit_code/error，故成功退出码和错误状态按原 run receipt 核，core 只核其真实 complete、source 和 certificate SHA。其 stage manifest 的原清单键是 stages，另外两组为 files；只对 FIBRES 使用这个已核分支。不得给旧文件补字段或改写旧 tag。

## 2. 原对象与符号

原曲线是 Y=W₄₁，原 T₇ 是循环7同源对应的 pull-push。原 level82 标量 diamond7 为恒等，原 −3 twist 在7处的字符为 +1；本次保留原 R865 的 σ₆、σ₇方向和共同尺度，并不引入第二个 Hecke 算子。

原五个输入必须取 GLOBAL 中的

    five_original_polar_and_eta_outputs[j].eta_degree_zero_fractional_ideal

及 FIBRES 的 original_ideal、xi、Poincare_v 节点。原线丛为 I_Z=O_Y(−Z_j)，原整数 Picard 点为 ξ_j=−[I_Z]，η_j=ξ_j/q_j。real_descent_degree_zero_fractional_ideal 对应另一条三次比较线，不能替换 I_Z。

完整七共轭极除子的 Q 下降、原 t=a³ 的 c₀帧与 c₁单位帧沿 R870 §1、RF §5及已成 FIBRES 程序。包装器只核真实源身份，核心保原节点、p_j/q_j 和 c₀阶数；不从一个未下降的单独 Hom 除子推断有理性。

## 3. 新整数算术

读原 R865 的 χ₇、m₇、不可约因子 f_i 与全部已有 E_i、d_i、P_i=d_iE_i。旧因式分解、旧 CRT Bézout 和原127维矩阵均不重算。

首先形成
$$
m_7(X)=(X-8)Q_0(X)+N_0,\qquad
N_0=m_7(8)>0,\qquad N_{\rm full}=\chi_7(8)>0.
\tag{870M.1}
$$
整数除法后逐系数乘回。R870 证明给出 N_full=#J_Y(F₇)，N₀ 消去原 J_Y(Q) 的全部挠点，包括7主部分；这不是仅消去某个未指定扩域中的挠点。

对每个真实因子保存
$$
f_i(X)=(X-8)Q_i(X)+n_i,\qquad n_i=f_i(8)>0.
\tag{870M.2}
$$
程序读取原 P_i 后，只新增 f_iP_i=m₇R_i 的完整整数多项式乘回和
$$
A_i(X)=(X-8)P_i(X).
\tag{870M.3}
$$
A_i 不对 m₇约化。约化虽然不改变 Jacobian 上的作用，却可能改变有限对应及帧比较的实际代表；本任务必须保原对应表达式。

各 n_i 的乘积与 N₀核对，各 n_i 按原重数的乘积与 N_full 核对。随后形成
$$
d_*=\operatorname{lcm}_i d_i,\qquad d_*E_i=(d_*/d_i)P_i\in\mathbb Z[X].
\tag{870M.4}
$$
此 d_* 是实际已有投影分母的一个统一整数，不声称最小。它不同于 R862 的 A 投影分母，也不在尚未判定 η 活跃支持时冒称原 YP 已选 d。

每个因子、共同整数与最终计划各为完整原子阶段。对实际16个因子，本轮应有20个完整数学阶段：source audit、一个普遍整数阶段、16个因子阶段、共同分母阶段和五点判定计划阶段。

## 4. 真正完成与仍待执行的 Picard 判定

实际 R865 的16个因子重数均为1。核心从已有原字段读取该事实，结合 R870 §7的原 GL₂ 型等型论证，只在所有重数确为1时声明这些谱块已相互分离。该结论不决定其中哪些块承载原 η_j。

对每个 i,j 保存原等价式
$$
E_i(T_7)\eta_j=0\text{ in }J_Y(\mathbb Q)\otimes\mathbb Q
\iff A_i(T_7)\xi_j=0
\iff[n_i]P_i(T_7)\xi_j=0.
\tag{870M.5}
$$
得到16×5共80条 source-bound 原 Picard 等式输入。每条保其原 I_Z 两图节点及原刚性化节点，并给真正循环7对应的
$$
\mathcal H(L)=\operatorname{Nm}_{\rm target}({\rm source}^*L)
$$
迭代 tensor recipe。所构造的零度线丛 Picard 类是 −A_i(T₇)ξ_j；完整 RR 维数只能是0或1，维数1才接受该投影为零。

本轮不执行这80个 norm、RR 或 principal-function 计算。actual_complete_RR_dimension、actual_principal_generator、active_factor_indices 均保 null。exact equation plan 的完成不是原 η 支持已经求出。

若未来真实计算得到 A⊗B⁻¹=hO，沿原 c₀刚性化的 A→B 映射必须为乘 c₀/h，其中
$$
c_\nu=\left(h/(e_{A,\nu}/e_{B,\nu})\right)(P_\nu).
$$
c₁纤维比例为 c₀/c₁，原 RF 实例正是 κ_j/R_j(P₁)。本轮只保这个准确方向和原帧输入，不造 h 或 cν。

## 5. 身份、恢复与成功出口

RESULT 固定为 R870-original-Y-rational-torsion-and-Hecke-support-inputs；最终证书固定为 p41-original-Y-rational-torsion-and-Hecke-support-inputs-certificate.json。核心 CLI 是 --config --output --budget-minutes，仅在原公开仓库的 GitHub Actions 内允许新数学。

数学 tag 包含真实核心 SHA、R870/R865/RF/YP 四篇证明 SHA、本文 SHA、三组原数学身份与完整所选文件 fingerprint，以及固定策略。目录、下载方式、预算和真实 rules-pull receipt 不改变数学身份。所有所选原文件字节保持原 tag，新的整数与计划只使用新 R870 tag。

新阶段位于根目录 R870-*.json.gz。写入先临时文件后原子替换；完整阶段一经存在即读取并校验，不重新算。实际 stage manifest 以文件列表 hash 命名；R870-current.json.gz 是 complete=false 的运行指针。失败 FINAL 是历史端点，恢复时不让其旧 manifest SHA 约束后来完成的新阶段；成功 FINAL 则完整引用必须逐 SHA 成立。

标准库 wrapper 从原结束 artifact 恢复同核心、同 wrapper、同数学 tag 的阶段。它不 import 核心，不执行整数多项式运算。外层 timeout 是预算加900秒，随后 SIGTERM/短宽限/kill，保已完成原子阶段、真实退出收据和 full manifest。没有 core receipt 的外层终止诚实标为 incomplete，不能补造成功。

complete=true 只指本次全部整数与80条输入计划完成。原 η 活跃支持、原 e_η、特定 d、主函数、非 p 地方高度、原高度数值和高度非零标志均 false。N₀与 d_* 可作为后继准确输入；不得从本次成功直接删掉 YP 的任何 Picard 或非 p 校正项。

## 6. 存储与发布

新请求已填三个实际成功 producer；没有未知的数学输出或 future artifact。首请求 resume=null。workflow 只在本专属请求变更时触发，权限 contents/actions read，partial checkout 与真实 rules-pull 比较原两个 README 后才执行。源码只 AST 解析，包装器完成来源与输出纯 IO；不另加独立数学测试任务。

所有 raw 输入、数学阶段、机器回执与向量只进入一日 active artifact/carrier。Git 只保存源码、参数、纸面证明及简明 run/SHA 登记。后继若消费完整 norm–RR 原叶，再从真实活跃来源取得必要载体，不在本轮提前延长未使用的大 raw。
