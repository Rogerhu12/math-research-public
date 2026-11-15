# 已观察曲率缺陷 guard 的实现与首次公开执行边界

日期：2026-11-15。状态：五个新源码和首次入口已完成静态审查，**四组18项新增人工及新科学阶段尚未执行**。本稿不预报通过或改进。设计见 [observed-curvature-defect-primary-guard-design-20261115.md](observed-curvature-defect-primary-guard-design-20261115.md)。

## 1. 唯一输入、冻结源与新文件

继续点是 covered-growth run43762868037/job132961344492/source4f1365300b70831550d544df119d738b2531eff5 的实际终态：η=.2662701215525791，fineκ=57.99998346840656；完整有序bank375、coarse4432/fine4451、B=.00025、legacy/covered双streak0。永久reference163及原g/b0/independent159/physical163不变。

原日志5818416B/SHA256 bd49ef570ab38e23af4bdbe47d71d567cca76d9add2d91d4953fe40ed34b5842。新transfer核的语义COMPLETE是**JSON加一个LF**，1223175B/SHA256 e233db56f1466d63edad76e542db4cd4e873e0ecb56cd09efcc68ed6d9276d5f；上轮人类结果note所列无LF的1223174B/hash3e5e…是不同字节约定，不混用。

旧135份Python冻结保留；新5份使实际source闭包为140份Python。前5份workflow不改，加本入口共6份，request准确绑定146项。旧24份原始输入只恢复必要对象；唯一新的历史日志下载为上述covered日志一次，其原20/19/26/cache收据按已付源核对，不执行旧developer或optimizer，不递归复制整个旧PRIOR payload。

| 新文件 | UTF8字节 | SHA256 |
|---|---:|---|
| frame_metric_curvature_defect_guard.py | 35055 | `d04e56fdd55e1fe5b5b323f63fdb9b0d0c70db046cefb528f947839f878cf115` |
| frame_metric_curvature_defect_guard_recovery.py | 48568 | `4a3b6dde704e5e18d3a9d91da7032ac69b67c113cf2ddc9538a1efd3ebeefcb1` |
| frame_metric_curvature_defect_guard_development.py | 29288 | `4be459dee22c71a6bf93075b0963daea11d8fd094c242887f6421ce3ab7e04ad` |
| frame_metric_curvature_defect_guard_transfer.py | 20945 | `7ac5f8721d9d0045156c4fb5b35d1b18168ffd62dabd100e0b3d29489793b240` |
| frame_metric_curvature_defect_guard_audit.py | 31920 | `df8eb6890f6f27fbafdc5898739603e5aa615e97de0cd05898906187c02e9973` |

新workflow .github/workflows/visible-curvature-defect-guard.yml，4305B，SHA256 199af979d66d0d3b7da61593973e9443f32d238cf280cbdf3e15934db589ad06。它先执行公开及私有actual git pull --rebase/双README差异核验，随后回到本次请求source，核全部源码指纹、只编译五个新Python，再执行新人工和一次新算法阶段。所有新运行只在公开仓库Actions；runner临时JSON及语义stdout不入Git、artifact或Release。

## 2. 普通primary唯一数值改动

new core的 guarded_primary 先提交上一模型已完成pending、冻结两桶state，再直接调用原 selected_model。只对原variable domain中已选group8行改变 targets 和 b：
target=max(old_target, original_floor+gamma_grid*B²)，b=base_value−target。gamma只由过去真实同一行actual−prediction的最小差，按实际y−x原共同physical body范数平方归一取得。

不改变原A/c/上下界、values/J/groups/tolerances/state/step_scale、其他行或顺序；不删zero-J。系数为零时target/RHS数值逐位保持。提高target若令LP不可行，走原已计费失败/缩径，没有免费未加guard重求。系数只是原单位经验记忆，不是Hessian上界或跨中心/全域误差证书。

两个原observable factory在guard之后依次建立；随后以同一primary对象、原x、完整row mapping、pool versions及complete binding绑定。旧键 radius_independent_model_sha256 在此新primary内明确包含B、targets、RHS和learning-state；本次不调用旧radius_mapped_witness，也不声称它在半径变化下不变。其他同模型原cache合同保持。

## 3. 原SOC、行学习和控制器的保真边界

新outer从冻结covered outer显式派生；只替换普通primary入口、两factory后的新绑定、原curvature diagnostic后的新样本排队、下一模型/finish提交及独立报告。原 solve_reserved_primary、SOC solver、same-y rebound helper、旧17项same-layout hold、expanded hold、covered/legacy控制器及所有真实验收/learning仍直接调用原实现。

原 build_correction 从原base/J、真实y、groups及cfg floor独立重建SOC RHS，不读取新primary.targets。expanded rebound继续调用未包guard的原selected_model；新ordinary包装不会递归进入SOC。最先完整ordinary alpha1以外的SOC、backtrack、rebound都不训练。

实际新样本先pending，不改当前模型coefficients、targets或incumbent合同；仅下一ordinary factory前提交，退出时把已经发生的样本提交到最终checkpoint，不追改旧LP。初始两样本在第一模型前提交后，其输出receipt已刷新为真实committed状态，避免仍显示旧pending副本。

所有原12次LP、40次共享值、120秒active、每LP最多10秒上限保持。末余一LP仍受no-unpaired规则。所有已启动和失败调用仍计费，完整初验与首J的pre-active成本照原报告单列，不能藏到active以外而称免费。

## 4. 精确375入口和历史样本

新类直接调用原Remembering基础构造并用原restore_checkpoint_bank恢复375条有序记录；不经过冻结covered类的hardcoded59构造，不重放direction events。原context与source cfg未变，因此第一complete model仍须严格核375-entry原bank hash。

历史训练仅原模型2和6的trial0：x取对应原accepted_index，y取原exact binary64 independent159。旧SOC_hold_model_binding必须与旧ordinary_covered_context.final_model_binding相同。旧行池/versions在这个历史样本内部核同；当前只核原坐标、map、width、subspace、cfg和相应固定网格定义，不错误要求本次新池与旧样本池相同。来源log/record/source、精确物理身份、原x数组与原完整诊断均保。

core只对这些已经存在的x/y做新M(y−x)/width范数映射，不重算旧J、geometry、值或LP。两桶初始系数由首次公开执行得到；未在本地估算后硬编码。

## 5. 仅四组18项新人工

| 组 | 项数 | 解决的新接口风险 |
|---|---:|---|
| original_RHS_scope_and_final_factory_binding | 5 | 原wrapper仅改group8 RHS、zero系数、B平方、真实两factory最终绑定 |
| actual_step_and_delayed_defect_learning | 5 | 实际rounded y−x、同一行缺陷最小值、当前冻结/后继提交、忽略SOC/backtrack、zero/nonfinite norm |
| original_SOC_and_infeasible_proposal_scope | 4 | 原SOC数组相同、zero-J不可行见证、原paid helper引用、后继学习不重写已构造LP |
| three_seventy_five_entry_and_paid_sample_linkage | 4 | 新375构造/第一bank门、精确有序原context、旧样本内部binding及初始committed receipt、错误59/错binding拒绝 |

这些是明确标记的人工数组，不是曲面或科学checkpoint。只调用一次旧 artificial_arrays 数据构造器和原纯数组_ArrayOracle类；不调用任何旧developer_check。人工会使用真实163×159映射、原build_primary、两个真实数组observable factory、原curvature_trial_diagnostics和原SOC数组构造，因而有真实计算成本；不调用HiGHS、科学geometry/JVP或优化器。zero-J不可行是原数组不等式见证，并非solver成功/失败模拟。

375构造人工用局部context-manager mock替代基础构造和基础factory，并给旧59构造加禁止哨兵，以隔离新构造入口；退出即恢复，冻结源码不修改。**生产恢复链不monkeypatch任何冻结模块**。人工中的源形状样本有明确artificial标记，不冒实际paid source的验证结果。

根完整静态读五源、outer相对旧源码diff及新四组；tail_cost独立核root transfer的样本/135旧closure、root audit的constructor/stage/140 closure。所有检查的首次通过/失败以随后公开输出为准，静态阅读不冒执行。

## 6. 输出与解释

新标签为CURVATURE_GUARD_REQUEST/PUBLIC_PULL/PRIVATE_PULL/PRIOR_WORK_REUSED/DEVELOPMENT/MODEL/COMPLETE。完整stage键 curvature_defect_guard_stage；学习终态键 curvature_defect_guard_learning_checkpoint。

每模型分开记录guard是否建成、真实started primary LP是否使用、原真实接受/失败/SOC与learning/费用。root audit只有在modified_row_count>0且inner_call_count>0时才记实际guard使用，不能把建模当已使用。最终future checkpoint保完整bank/pools/reference/selected159/163和两个controller streak，另外保完整经验learning状态；后继不得重置本轮实际观察。

不会将一次未触发SOC或一次η下降归因成普遍改进；仍报告原直接κ/14门/完整metric/所有费用。即使本次失败或guard消耗原预算，也保实际结果和最后合格点，不延预算或机械重跑等成功。当前离主题1e−6同g精化、全时嵌入和reach完成门仍远，不以本新算法阶段结束课题。
