# R809：同一 S5 块的准确正规坐标消费者执行契约

日期：2026-11-15。状态：**脚本/输入契约；无新运行结果。** 数学依据为 [R809 证明](../results/R809-original-normal-vectors-for-function-and-Hodge-inputs.md)。先执行真实 R803/R807 的六组清极 Hodge 目标；原 R787 成功后追加 A、B。以下全部新算术只能在公开仓库自己的 Actions 中执行。

## 1. 固定任务与输出含义

核心：
- 路径：scripts/R809_original_S5_normal_coordinates.py。
- RESULT：R809-original-S5-normal-coordinates。
- FINAL：p41-original-S5-normal-coordinate-certificate.json。
- CLI：--config、--proof（R809）、--method（本文件）、--retained、--output、--budget-minutes。
- python-flint 固定0.9.0，核心预算300分钟，外层保留整理/归档时间，job350分钟。

固定原空间：Y亏格127；V5维1234；原69阶、每阶20个实圆分坐标，共1380行；整基272项，次数0、144个1、127个2。整数基尺度82^10，实际 sigma=e1+n e73 的 n 只从真实 R805 读取。

允许目标名为 C0,C1,C2,C3,C4,C5,A,B。初次 requested_target_groups 只含六个 C；不放假的 R787 null producer，不将其未返回视为任务停止理由。完整八组是112个有理右端，初次六组是84个。每组输出始终保留原14列
b^0,…,b^6,s b^0,…,s b^6，s=1+2ζ。
这里的完整 scope 指本次实际请求集合；FINAL同时列出所有已成目标，以及 A/B/全部112列各自的真实布尔状态。

## 2. 原输入与最小来源链

### R805：原铅笔、graded free 基和已成单项式

消费实际成功 run/source/artifact/完整 manifest 与小证书，并读取：
- stage manifest、accepted pencil、graded free basis、degree3 S basis index、原 alias index；
- 原 degree2 补基索引与 S3 所使用的实际新二/三次 monomial stages；
- 真实 source-bound retained bundle 中所需 R786 原文件。

不重求 R805 铅笔、原146秩、291+127补基或690 S3秩。原 S3数据只作为生成公式及已成短前缀，不将其 minor 冒充 S5 的短 minor。

### R786：原 degree1至5 行与 recipes

原五次 short-basis producer 的完整 manifest、certificate、exact stages manifest及相关 basis indexes保留。准确行文件为 R786-exact-power-r-row-NNNN.json.gz，r=1,…,5，共146、418、690、962、1234行；每行129项、40个原 xi 坐标，原尺度82^(2r)。

先逐recipe建立叶子别名；扫描可以读取已成JSON，但不重算任何数学。只在实际生成时读取所需前69项。源行同时保持原 finite-coefficient验证标志和完整SHA。缓存有界，避免把3450行129项的多个Python副本永久留在内存。

### R803：原六组694坐标与四补行

必需真实成功证书、stage manifest、六个 exact-original-M6-coordinates-jN stage、四个 new-original-M6-short-row-690…693 stage、原 M6 basis index及 ratio interface；从实际mixed scalar元数据保留原b模型。

只消费 coefficients_in_integer_scaled_original_M6_basis，694×14个准确有理数；不用 unscaled 字段替代。四补行已成42阶照原数据读取。后续42至68只按原 E4/E6/eta12和原 M2 行补足，不重算56张量、H³或任一旧 Hom/period。

### R807：原 theta 与完整 membership 证据

必需真实成功证书、stage manifest、nonzero-pole-clearing-theta stage、four-M6-pole-clearing-coordinate-index、四个完整 member coordinate stages，以及实际新增过的 pair-tail stages。后者若在相关单项式依赖中使用，属于公共基的已成前缀输入。

核真实 lambda五项与146坐标的一致性、first-nonzero归一、源M2索引0至4、四个完整1100行回代标志、原M6四行身份及原R805/R786一致性。R807的五E6投影、138×5残差核和原秩全部只读，不重新执行。

### R787：仅实际成功后按需追加

只接受 complete=true、原129阶完整关系验证成功的 source-bound recipe。核原V5顺序、尺度82^10、A/B两组1234×14整数、B非零和原field.lambda。失败producer的候选不能进入目标。

它的 B_fld=lambda*b 系数必须按i列乘lambda^i，两个s块相同。可以把这个因子放在每个Q右端的准确 rational_scale，最终恢复。recipe记录已清的共同分母/content不再乘回。

## 3. 不变身份与可增目标

公共 basis_configuration 固定：
result、source_sha256、python_flint、R809_proof_sha256、R809_method_sha256、p、qY_count=69、real_coordinate_count=20、S_basis_dimension=1234、normal_basis_rank=272、degree列表、原82^10尺度，以及已存在的R805/R786/R807真实producer身份和所消费公共stageSHA。

producer身份由 result/run_id/source_commit/core_sha256/manifest_sha256/certificate_name及certificate SHA组成。输入files列表可按需扩充，但不能改变同一producer的任何既有字段或文件SHA。数学tag不绑定artifact传输URL、预算、requested_target_groups、尚未存在的R787。

每个目标另有 target_configuration：
- Cj：公共basis指纹、目标名、实际R803第j组坐标SHA、原b模型、真实R807theta和四成员完整证明SHA、M6补行及原R786相关源；
- A/B：公共basis指纹、真实R787 recipe SHA、原field.lambda、原R786basis身份。

任何已成目标若源身份不同必须拒绝，不能以同名覆盖。新增A/B只新增其目标身份与stage，不使原六组失效。顶层run配置记录本次目标集合；它可以改变，不能因此重算已成矩阵。

旧FINAL只证明旧实际scope完成。续算仍应核查新的目标请求并继续，最后生成包含全部实际已成组的新FINAL。原FINAL的SHA由wrapper放续算receipt；不把旧FINAL存在作为退出条件。

## 4. 公共 S5 构造与69阶准确矩阵

按a外层、j内层生成 tau^(5-eps_a-j)sigma^j d_a；展开sigma二项式。优先查询原R786 degree5叶子别名。没有别名时，实际检查一个由R805已成三次monomial与锚点二次monomial构成的分解；不复制已有原截面的已成算术。

对缺少长尾的R805二/三次行，逐段复用原[0,41)，若原R807有实际[41,55)则接上，再只卷积剩余尾段。二/三次尾的sum-band按输出次数切分，不调用完整低阶卷积后丢弃旧前缀。生成新的五次单项式时，其全部69项此前未存在，才允许完整新乘法。

新增单项式仍在原q/xi和v/t两套整数表示中独立相乘并一致核验；S5的二项式线性组合用已认证的v/t行。每条实际S5行保存公式、每个真实因子source、n、尺度和69×20准确行。完整矩阵1380×1234不另写一份重复大JSON；由已成1234条S5行重建。

选择新模素数，计算原短矩阵的真实rank/minor。每个失败素数只登记实际模秩，不能声称特征零失败。实际满秩后固定1234个行指标I，保存原matrix/indexSHA与minor/determinant。所有后续目标共用同一个I和模逆。旧minor绝不替代本次真实证书。

## 5. 六个实际 C 右端的形成

读取lambda并由原V2[0..4]形成准确tau*theta，不再卷积五个已成积。将其整数系数content/denominator提成一个准确 rational_scale；此尺度最终必须恢复。

读取原694条M6的69阶实坐标。前690直接读原R786 V3；后四行按第2节复用/补足。把每个R803坐标列清分母、去content，记录准确比例，再作原整数矩阵乘法形成Uj的14列准确前缀。Uj向量可以逐组保存，避免中断后重新执行已成合成。

对每组14列分别乘同一个tau*theta，得到Cj完整1380行；只做目标实际需要的84个序列积。每个primitive整数列与准确rational_scale共同表示真实目标。原符号、82尺度、4/1722^3与lambda归一都在真实输入及比例中保持，不按浮点大小或近似content改变。

不先计算theta倒数，不先计算Uj/tau³。最终目标即Cj/tau⁵=theta*Uj/tau⁴。原ratio_interface只输出v_Cj/v_C0及两边source，不声称已经完成域除法。

## 6. 准确求解与完整回代

同一1234阶整数minor对每组14个Q右端作Dixon。模逆仅在素数域，误差更新使用原整数残差。可按固定小列组处理以控内存；每个子组有自己的目标来源和完整列索引，不发生14个代数分支分别归一化的问题。

每次有理重构使用固定矩形2AB<M；默认对称界floor(sqrt((M-1)/2))。候选一律在原1380行完整乘回之后才标complete，再恢复目标rational_scale。六C组另外检查每个a的最高S5系数为零。零Q列是合法真实输出，不得强行改成非零；C0本身非零由theta、U0原输入和域性质给出，代码也核实际向量非零。

完整子组一经原子保存就成为可复用阶段。只保每个未成子组最新大Dixon向量，旧位次留小receipt与previous SHA。若完整坐标已存而旧current尚未来得及删除，续算先核成功源/minor一致再删旧current，不重求数学。

## 7. 输出 stage 与 FINAL 草案

核心只写 R809-*.json.gz 及 FINAL。所有stage都有 complete 与对应configuration；target stages另含 target_configuration及fingerprint。

公共阶段包括：
- 原recipe/alias索引、实际复用来源；
- 真正新增monomial尾段与五次monomial；
- S5-row-NNNN、S5-basis-index；
- 短minor、modular-inverse及完整源binding。

目标阶段包括：
- 六U的真实原M6合成前缀；
- Cj或A/B的primitive整数完整1380行与rational_scales；
- 每个子组的当前lift、小digit receipts、最终exact-coordinates；
- 每个目标的normal-vector，明示14列基与272个多项式系数。

stage_manifest列所有完整阶段的file/bytes/SHA。FINAL列p、S5_dimension、qY_count、full_real_coordinates、normal_basis_rank、实际n、完整basis/minor、requested_target_groups、completed_target_groups、每组坐标和normal-vector来源、真实完成的Q右端数、全部完整1380回代和六C最高系数为零的标志。
明确 flags：
actual_original_y_normal_vectors_computed 仅A/B均实际完成才true；
all_112_rational_targets_computed 仅八组全完成才true；
actual_polar_ideal_or_eta_or_height_computed=false；
original_scalar_and_field_normalizations_preserved=true。

## 8. 后继乘法与暂不执行的部分

R809证明的bounded commutant引理给后继R811：
对r5的A/B用8个好点插值，对r4的六清极向量用7个；只做模素数数值Krylov逆，最终按weighted support、Mf e0=vf与[Mf,Mw]=0准确认证。若以特征零点检commutator，分别需要9或8个点和严格次数界。

本核心只生成实际需要的normal vectors，不构造全特征零Krylov逆、全部乘法表、trace pairing、极理想或五加法DAG。R811的实际两图整数格消费者独立接续；这些未完成对象不能写成已有高度输入。

## 9. 保存、续传与核验范围

大输出只保一日active artifact；不入Git或Release。source-bound retained bundle携带本次真实消费的原文件，原producer artifact过期后仍可沿完整SHA链续传，不重跑已成数学。只提交脚本、参数、证明/方法、小run/receipt/manifest摘要与SHA；完整可重算证书和矩阵留临时产物。

本地只做源码、AST、schema、传输及SHA检查；所有新秩、乘法、展开、坐标与Dixon均由公开Actions执行。实际运行之后，独立verify检查原配置、逐stage源身份、完整1380回代标志、实际目标集合与最终normal-vector结构；不把计划的秩、候选theta或预期完成时间登记成计算结果。
