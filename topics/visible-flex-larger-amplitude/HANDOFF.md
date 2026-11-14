# HANDOFF — visible-flex-larger-amplitude

/root，visible-larger-public-resume-20261114，GPT-6 Astra Pro（AI辅助）。**未完成，继续大幅完整闭族及同g精化，不等用户阶段确认。** 历史细节见本日migration/legacy/recovery notes及Git历史。

## 授权、规则和现场

本轮用户明确指定公开 Rogerhu12/math-research-public，授权CLI commit/push main与本仓Actions；旧公开发布审批阻塞已解除，普通push多次成功，不重复问。只在公开仓写；PAT只瞬时CLI，不入文件/日志/提交，不强推。根README全部授权/14规则已读。
每push前真实pull --rebase；非快进立即pull/rebase/重推循环；至少每小时pull，每次检查双README新差异，有变只读差异并立刻执行。读SHA记末行。root独占Git/H/open/log/workflow，子线交独立文件冻结。
计算直接用本公开仓Actions（4CPU/16GB/6hr）；本地只读/源码/准备/压缩取回。Rule12完整证明直接results，不加独审或冻结审批门。H<10KB、md<100KB、数据>1MB gzip、单件<5MB；大派生表保存源/argv/hash，不写根LOG。
clone=/workspace/scratch/e959e57ee07f/math-research-public（本轮目录现symlink到/home/agent/vl-e959以避共享overlay满盘，逐文件SHA一致），部分克隆/窄检出，禁gc.auto/autoPackLimit/maintenance.auto。共享磁盘紧张，不删除他人文件，不对大树git ls-tree -l触发全blob下载。exec各自PID命名空间，只管owned-child。
旧B=/workspace/scratch/ffc1334c1988仍可只读，含math-research-public、math-research、root-work/strong-work/exact-work/geometry-work。已恢复旧公开clone43个本地提交，旧末端e4e38a4fab4cadf9039640dc3495add7eb15eb36；R235–237及真RK24/RK48求解不需重复。恢复说明notes/2026-11-14-public-successor-recovery.md。

## 完成标准

按README：同一固定g的连通闭C²嵌入连续族、固定H含内点、diamH与实际像δhold均≥.2D、含反射商δE>0、全t reach≥.03D、全域metric≤1e−6，并同g/参数/t范围精化至机器或原solver容差。D取完整闭F0；H可为两个固定帽之并。交数个<5MB网格并明确严格存在缺口。开放前缀、设计代理、有限样点或小幅A不够收尾。

## 当前最新真实大核接受点

公开followup run43580643038，源码be989410a0149c2d5b24feec5b32ba3f93ad5c70：free3第一段从.984真正接受到 **s=.99**，423节点/M96/N1024，固定核心前3、释放4..96，93条principal normal设计末条件。RMS5.4570433066e−7、BC3.46945e−18；完整实际文件SHA b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff。
结果在notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz（artifact14108132430取回并归档），含原profile/projector/seed/日志、精确core-certificate和material-quintic。两档材料C²读出已真0：1024角/2径向误差5.77368e−7、κ6.30084、G样本.960000980454、Dprefix样本3.5003721203；更密档读同JSON。不是完整尾或闭面。
第二段duration .012 **只在prepare的Taylor2末点principal elliptic门失败**：detII正性/IIφφ条件未通过，未启动Newton；不能说.99接受点失败。新public_free3_adaptive.py从此真.99开始，先核实际入口正分支，仅预测门失败时二分步长，不放宽原门；mainline workflow从.006试起向1.05。若入口真不在principal域则转fullDN，不无限缩步。
首批run43579782197的固定32核 .99恢复真运行321.75s但不接受：5次Jac后回溯失败，连续残差5.93612e−5，需求764节点超过640上限，实际保存423节点。BC3.39e−21不代全域通过；原checkpoint/actual/日志在notes/public-actions-43579782197-1-m96，不能冒新接受解。
旧.984真M96接受文件仍notes/2026-11-14-geometry-resume-scaled-sphere-M96-normal-BVP-r1.json.gz，SHA3ac8c8ef…；R237严格证全96核rho>.16611593994/G≈.959999999997。新free3核心必须使用自己的证书，不移植旧下界。

## 完整尾和同材料度量主线

R236 λ=6/5全32核心G≈.96；照搬旧scalar会遮挡到.869，球控制新prefix保持样本G。现有AngleConnector/coast/finitebridge能把scalar接到真实r=.3尾cut，但新增段的非轴场尚未求出。
geometry_20261114_full_scalar_profile.py包含3个内支scalar控制和FrozenCompleteProfile；full_dn_boundary.py按完整材料θ匹配非均值DN并含core换角导数；full_dn_augmented.py用c'=p'=0把非局部BC变成原QR可解的分离BC。M=T96初设计固定前3、3scalar，增广389维/左293右96。run43582043166真scalar/RHS一致，完整690节点θ圆warm已通过节点/中点域，无补点；准备最大col.00711，尚非解。BC FD粗步5.04965e−5略超门，减半后1.26187e−5且约4倍收缩；三步/Richardson新版保持5e−5和原Newton门，待真算。
**R240已证明**：ρ>0、固定c0=1时 θ=Φc(φ)，g=ds²+a(s)²dθ²与核心c无关。真正同g精化冻结完整a(s;p*)/区间/尾帽g和t范围，释放全部核心，K=0/T=M/k=0，增广386维/左290右96。不得把非线性换角硬延到帽心；用共同θ环带与固定帽图册，实际C²拼接/固定H另付。
**R239已证明条件引理**：同完整材料高度/非均值径向斜率、连续正分支和实际turning number决定均值，单个SE2配准及同非特征Darboux分支决定完整六jet。有限DFT不能自动核销这些假设。exact正接真T96 tail worker已具备，原有限尾g/正性/Newton/J/audit不改，只扩constructor容量限制。
材料谱run43580643038 material真成功并自动push，输入仍旧.984：N4096下T96的高度C²截断误差.00253633，T512仍.00141522，T768约5.92449e−9但仅一档；原96φ模不能当96θ模。该处a'>0，非native上尾cut；只作谱诊断，真正cut重新核全谱。完整pack在notes/public-actions-43580643038-1-material/material-tail/。

## 原A固定g尾与整闭结果

A仍唯一完整旧小幅组装基准：M32/35参数/2590nodes/生产1280角，RMS9.9224e−8、BC9.234e−13；coreG=.2506381129、D≥3.9767551573，幅度不达标。旧13方向full/half失败/被杀/首inner接受记录原样保，不能称新A。
原stored g/全32H/RK12/depth8/576stage；真depth12、RK24及RK48 BVP/J/audit均已完成，不重算。RK24残差8.36178e−11；RK48残差1.67235558e−10、4114.75s。24→48 cut slope/second差3.55e−13/8.29e−12，但旧freq40 J差.0671/1.5655，未机器稳定。
**run43579782197的RK48完整readout step真success**：重建RK24真8、RK48真16+源节点，两独立共同网格、有限collar、完整closed全完成。已取回artifact14108496208，位于notes/public-actions-43579782197-1-rk48/reports/；原旧ENOSPC只属历史，不能继续说当前未读完。真实精化结论已发布：24→48同f8二jet差7.03e−6；48f8→16二jet差.0029138，尚未机器稳定。
新三mesh各解压3745773B，73442顶点/146880面、Euler2、每边两面、零退化。Dcloud3.9774592667、Hdiamcloud3.9695633777；九phase最大点云Hausdorff.2506381375，比例.06301463338，明确低于.2。全phase有限空间三类弦无负例，但连续空间reach仍需覆盖。R234原finitecollar全域metric界约1.002e−18，不能移植给新大核。

## 全t几何和发布故障

geometry run43580643038数值步骤均真success，artifact14108097323已取回notes/public-actions-43580643038-1-geometry。R238条件定理已登：平面局部胚支持4弱标记排除含反射全等；真实2589/2589prefix片非平面与4固定支持圆代数通过，tail/collar连续输入仍未齐，不冒δE已证。
R241 v2在run43582043166真完成：D上界3.980751407764145、Ktau0=.9994116104，曲率与标记门已过；所有prefix-tail/cap/self已付，余33712仅prefix-prefix。原3192共点法向差7.85e−17，锥门付392296对。v3只将失败前缀父块角分2并真评价新角中心，其他已付块保留，待Actions；不改标记/曲面/K。
两首批及free3/geometry的自动publisher失败均为pull--rebase缺committer identity，计算结果/完整artifact未失；material恰无需rebase已推。root已修全过程临时Git身份；每pull同时检查README变化，变化交root读差异后发布。所有首批取回包已普通push，不重跑成功计算。
新exact公开源恢复只取实际需要的78件，逐件对原91清单SHA；12未迁移MD和1变动但未用client明确排除。全部来自公开当前repo、无私仓secret或读写。原源revision86943663…表示字节身份，不假冒公开commit。

R242已证：精确度量+每纬圈角解析下，平面开片强制一段a′为固定非零整数；严格|a′|<1排除，不能套有限metric误差或无解析控制的C²极限。

## 紧接执行

R239–241及首批数值包已公开push。run43582043166/source8fa6b3f已完：free3真接受.996/.9975但material误差4.61e−6/8.09e−6；下一段真Newton失败。T96真zeroH/J/audit成功（805.48s，metric9.99e−16），已取回待归档。v2和690节点prepare已完，fullDN尚未启动。手动workflow_dispatch被PAT权限403拒绝，改用用户授权的本仓既有push触发，显式选择任务，不重复已跑项目。zeroH缓存已对真实包和coupling配置严格预检通过，后续新H/最终audit仍实际求尾。新接受点立即原审计/实际材料谱/核心G与球排除，然后继续真正tail匹配/闭合；定型后固定同材料g精化并核全域全t。任何阶段完成不结束本题。

规则同步记录：2026-11-14T10:02:53.258112+00:00 实际pull --rebase成功；双README自373e59e无变化，已读提交 56ce464594a201e5a3cd50c0239abb5f5e52c330。
