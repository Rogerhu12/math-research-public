# 完整几何位置观测及独立25传输

2026-11-28（UTC）；Astra-larger-e4e2a2bf-20261126（AI）。这是完整源码和参数投影的实现记录，不是新场、数值运行或连续几何结论。原执行中的19–24及其controller和queue不改。

## 1. 原返回对象与准确语义

原完整几何scan已经返回worst曲率位置、farthest表面位置与amplitude.worst_by_family的body_diameter/distance_plus/distance_minus位置。原observer只保留数值，故不能从旧进度的K×D值反推热点属于端层或中央。本修改在原_geometry读出中复制这些已经返回的有限标量，保持原Recorder/observe/validate_report_progress API、事件、六物理g、统计、接受标识和完整normal进度捕获。

每个位置仅含原对象已有的cell/u/phi/branch/stage/angle/s。非字典位置保持null；缺字段或非有限数字保持null，不计算s、不解释piece、不生成flex时间、不调用F/J/root。branch是原几何返回的数值分支；若来源没有，则为null。曲率极值是原scan选择的一个最大位置，不枚举并列全部最大点。farthest_surface不是对完整闭面直径达到点的证明。三amplitude族各自的physical_g原字保；不推全像Hausdorff或unmarked E3分离。

当前点与最新trial分别保存实际point/model/source和返回位置，原last_completed_trial仍保存完整前一真实返回。尚未有几何的trial不借当前点的位置。有限screen.complete不成为连续曲率或reach证书，accepted/final只从原完整report得到。

## 2. 完整三个源与精确父

| 源 | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| observer | 42637 | 4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94 | bad0be021443e7fa7a8fbfe4ee473f3e05ccadad |
| followups | 32763 | 444f57b28c695fbcd0fbfc03237b8c7a56dedccc97a64873b7dae083de5dbb12 | 4b72d0565d3f3fd797dd8bf45e48310cad8226d2 |
| controller | 19995 | 4bbac0cd1bb116205b4f94b8bc544e102bd522af9abb697327a8eb9b6f984562 | e792c8368fc4e0a4a50d693f9a836b44ae662f34 |

完整路径、三个完整父的字节/hash与每一项文字变换保在[完整再生器](../scripts/resume_20261126/reproduce_complete_geometry_location_observation.mjs)。原observer为39500B/321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5/8173d3576958dc5c476466dd4c5012c5ed81b0c1；原followups为32762B/046f0d7b8d27df95f5249438fdaf435b00c482b009fa8956f27dbdc662a6b314/d2c8ef87878d57525cfef04cfc401da7a9f30d6d；原controller24为19984B/289fa6ad3d93ac4257509e31a79459ef25608379efb0ac67dcce84d76f8e8796/c1d51b6ad5e86e41c2afa826968581b41c2d485c。所有父源码保留。

新observer仅由十项明列文本变化形成；其中两处own输出上限共同替换，其余单处。完整原捕获MAX_FILE_BYTES=16384保，只将新observer自身进度和immutable completed-trial scalar的界设32768。原normal捕获仍两次完整小文件读取并保真实whole身份。pure读取继续比较原来源对象，并检验新增位置字段等于原实际返回；不添独立审查、fixture或科学前置步骤。

## 3. 64项完整live投影及边界

原48个label→dotted-path配对全部保留，只有输出目录换成25自己的namespace。新增以下16个已有标量；没有把列表或对象编码成字符串越过字段上限。

| 新label | 原实际来源路径 |
|---|---|
| current_K | current_geometry.maximum_absolute_principal_curvature |
| current_D_point_lower | current_geometry.diameter_point_lower |
| current_K_cell | current_geometry.returned_locations.curvature.cell |
| current_K_u | current_geometry.returned_locations.curvature.u |
| current_K_phi | current_geometry.returned_locations.curvature.phi |
| current_K_branch | current_geometry.returned_locations.curvature.branch |
| current_K_s | current_geometry.returned_locations.curvature.s |
| trial_K | latest_trial_geometry.maximum_absolute_principal_curvature |
| trial_K_cell | latest_trial_geometry.returned_locations.curvature.cell |
| trial_K_u | latest_trial_geometry.returned_locations.curvature.u |
| trial_K_phi | latest_trial_geometry.returned_locations.curvature.phi |
| trial_K_branch | latest_trial_geometry.returned_locations.curvature.branch |
| trial_K_s | latest_trial_geometry.returned_locations.curvature.s |
| trial_alpha | latest_trial.alpha |
| trial_phase | latest_trial.phase |
| current_distance_plus_phi | current_geometry.returned_locations.amplitude.distance_plus.location.phi |

K是原maximum_absolute_principal_curvature，D_point_lower是原diameter_point_lower，不能称真实完整D或上界；alpha和phase来自实际trial，缺则未知。distance_plus_phi仅是该原max点的phi，不能由一个角度重建完整位置。

新followups完整源只改三项：全live计数48→64、错误文句、compact public总字节8000→16384。完整原progress文件上限95000、每个字符串512B、两次一致读取、4个文件上限、scalar-only规则、缺字段错误原文和未知状态、轮询、科学child及自然返回处理、原预算/顺序/队列95k限制全部不改。不丢掉原48项，不删原错误或来源身份；超界仍保原失败/未发布事实。

新controller25只有六项变换：自己的四个H槽文字、绑定新followups完整路径、pretty progress上限16000→32768。总索引95000及全MD/topic/H限制、真实pull及两README差异检查、普通NFF重试、原科学控制流全部保。新运行才使用该完整controller；原活槽不可冒25或缩减。

## 4. 复原与实际状态

再生器使用Node标准库读三个完整已知父，做所有明确文字替换、完整输出hash和逐字逆变换，再把三个完整源写入独立目录。其复原不读取科学数组、不执行Python/AST/fixture、不给科学加准入门。命令：

```text
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_complete_geometry_location_observation.mjs --source-root REPOSITORY --output-directory OUTPUT
```

所有新增源<100000B。25正式science仍157 argv、pure7 argv，原458/445 formal投影保；完整参数包另外给全部64 live映射。原五CLI与所有外部peer、来源历史、未知typed/final责任独立保留。所有新raw进度/完整报告/数值数组只在runner/scratch。当前未有25真实run/point/model/K/位置/接受或加速结果，不把源代码准备当科学返回。
