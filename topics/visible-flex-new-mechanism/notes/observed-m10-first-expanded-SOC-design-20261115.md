# Observed m10: one first expanded-pool SOC on an existing failed trial

责任：tail_cost 负责这个新入口的源码与纸面接口；root 负责原文审阅、唯一 Git 发布和公开 Actions 调度。本文冻结时只写源码、读既有输出、做文本 SHA；未执行新人工或科学。本文不是新实际结果。

## 1. 唯一科学问题

原 norm-memory run 43741276060 / job 132894771246 的 model 10 已经实际得到完整主步 y，却因新 coarse/fine 行而在 SOC 前返回原已接受点 x。后来 expanded-pool SOC run 43744903357 已完成十个新接口检查及一次正常阶段，但该阶段没有触发扩池重绑定分支。因此下一次不增加主模型数、不重复旧优化来等待触发，而只对这个已确定的 m10 失败 y 首次应用冻结的扩池 SOC。

原来源及可恢复性已见：

- [原 norm-memory 首实际](norm-memory-first-actual-result-20261115.md)；
- [m10 精确可恢复性](observed-m10-failed-trial-exact-recoverability-20261115.md)；
- [expanded-pool SOC 首实际](expanded-pool-SOC-first-actual-result-20261115.md)。

本实验的接受基准只是历史 x。它不是晚于这些数据的当前最好点的后继；即使本次 z 比 x 改善，也不能自动替代后来更好的正式当前点。

## 2. 原数据与不可替代的身份

唯一科学来源：

| 项 | 原值 |
|---|---|
| run / job | 43741276060 / 132894771246 |
| source | c30e7ea00a9ae06356409d5fdae289dfecf2210d |
| 原 job log | 3,443,509 B / 5e3be6e199829aee81de637c9e856a5ca0b91caa2154cefec913461c48c136e8 |
| COMPLETE 原 JSON 加 LF | 868,908 B / f14909e957164ea1bc92363ec228b91cf2adff773270108afe9005d4856d12bf |
| source cfg | b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6 |
| x physical SHA | 10b0a3b208ccb13919227d2b459995bffbe86dd528f0f1f136098d7b75adba1d |
| y physical SHA | 627c9474c4f3d2cb9c28c248f1ae06251274e1c1d50a2097280fc93e57d4d290 |

原 model 9 唯一 accepted_index=7 的完整 trial 与 accepted_iterates 中 x 的三组身份必须相同：physical SHA、159 个 binary64 精确有理字符串、163 个真实物理精确有理字符串。model 10 的 linearized_at_physical_sha256 必须等于该 x；model 10 必须是唯一 alpha=1 主 trial、未被接受、没有任何原 SOC 或 backtrack。

x 的两网最大 eta 为 0.26636800393715654。历史 y 的 coarse/fine eta 为 0.2663651531755449 / 0.2663651530478497，实际最大曲率为 58.00000333192753 / 58.00002409366549。这些是既有观察，不是本次将通过的宣告。新 ordinary 评价必须仍得到原十四 gate 布尔值，且 eta / 曲率与原值的绝对差不超过 5e-10；任何错配均停止，不能借“新策略”放宽原真实门。

冻结 transfer 读取原完整 reference163，再以这个原 reference 构造同一 FiveHeightField。当前 x、y 都用原 159 精确字符串恢复；各自经 coordinates.physical_exact 得到原 163 字符串并核 canonical physical SHA。没有重新选择 height anchor、将九个高度四舍五入、替换 g 或 b0。

原 target metric 的数学 definition hash、b0 definition hash、159 坐标 definition、163 原物理盒、fixed height slots 4/5、全原 F/T/Pi 网格与原 configuration 均由已发 transfer 和本次原模型重放继续绑定。source cfg 不增 policy 字段，也不改变 factorizer configuration SHA。

## 3. 两个完整池的恢复不是猜测

原 m10 起点的 coarse/fine 池大小为 4417 / 4091、版本为 4 / 7；失败 y 后变为 4418 / 4092、版本为 5 / 8。原 m11 没有再添加行，因此最终 COMPLETE 中的两个完整整数 ID 列表就是 m10 扩池后的列表。

原两次 separation 记录同时具有：

1. 所有实际遗漏 hard 行数为 0；
2. metric_minus 遗漏数与 whole_grid violation 数都为 0；
3. metric_plus 遗漏数为 1，whole_grid violation 数为 0；
4. 每个其他组的遗漏数为 0；
5. 原 true eta peak point index 唯一。

按照冻结 separator 的原 slot 规则，唯一新增 ID 为 point_count + eta_peak：

| 网格 | point_count | peak | 唯一新 ID |
|---|---:|---:|---:|
| coarse | 61440 | 11040 | 72480 |
| fine | 122880 | 22080 | 144960 |

从已保存的最终完整有序列表只删去对应的这一个整数 ID，就恢复原 m10 起点的完整列表。源码仍同时验证 source history count/version、m11 无变更、原 final list SHA，以及恢复的 old list SHA：

| 列表 | compact JSON SHA256 |
|---|---|
| old coarse | cbc5100fd624e48ac6515ba0c5c9435f53b0ab09ca4805b2c5d94c22eb4added |
| old fine | 1af3afd7ffa7bc55908f6e6c70759e54f3a89daff83420616faf79288e0be61e |
| new coarse | 88039c5e6c70f3767536ce7016159495f7074dc71654bd634186e41dcc0b2fc6 |
| new fine | c9620badc20d7a2b6924f3e0b1ef759e2aae337ab506b637a96bf3784779bd90 |

新 objective 在安装列表之前显式恢复已发表的 version offset；原 setter 一次安装得到版本 4 / 7。这个操作不宣称那些未保存的早期逐行插入已经执行。新的 ordinary y 评价和冻结 separator 必须实际重新得到同两个 ID，完整列表和版本必须准确变为 5 / 8。恢复说明中的推理不能替代这项新实际核对。

## 4. 原 bank 是完整精确恢复

直接复用冻结 transfer 的只读输入链：祖日志的 19 条真实方向输入，加原 source m8.cut_rounds 的两条实际插入记录。不得从 complete_model 的累计镜像重复计入，也不得重新采样方向。

原 m9、m10、m11 没有方向插入；因此 m10 的 bank 和最终 bank 相同。第一完整 factory 装配完待处理输入后必须核：

- entries 恰为 9；
- 原 context 与 entries 的整体 state SHA 为 07a1f00af0acc950a7db91c698d824b3ce47324921272f45b2e2b1b1eca18f81。

新 source configuration、reference163、factorization definition 均不改。不能豁免 hash 差异，也不把“21 个输入”误称为 21 个 bank entries。

## 5. 历史 binding 与新 binding 的准确分域

历史原 ordinary 大数组和 full J 没有逐项打印为 payload；其准确值已由原模型 SHA 绑定。本次恢复必须证明当前同一 x、同一原 ID、同一 M/width/trust 生成的 scalar 模型确是原模型，不能仅比较维数或 LP 结果。

记当前原 scalar 模型签名为 S，历史 selected observable binding 为 O_old，历史完整 binding 为 C_old。两个冻结 factory 的原定义分别为 D_sel、D_all。源码原样重放：

    S_sel_old = digest({
        inherited_scalar_model_sha256: S,
        affine_spectral_observables_sha256: digest(O_old),
        policy: D_sel
    })

    S_all_old = digest({
        inherited_selected_affine_model_sha256: S_sel_old,
        complete_affine_binding_sha256: digest(C_old),
        policy: D_all
    })

重放的 S_all_old 必须等于历史 SOC_hold_model_binding.radius_independent_model_sha256。S 本身绑定原 full selected J、values、tolerances、boxes 等原模型数组。这样没有把未打印的 J 当作可凭空读出的数组，却仍严格核当前恢复 J 与原原始签名的一致性。

当前 selected observable 与 O_old 的字段集合必须相同。唯一允许不同的是两个 external_current_cache_binding 中的 evaluation_sha256，因为本次显式 expanded policy/evaluation 元数据不同。这两条变化逐字段记录；de/df/e/f SHA、soft 原 tags、selected IDs、原 pool version 和其它所有叶都必须准确相同。

当前完整 oracle binding 必须与历史完整 oracle binding 整个字典相等，包括 state/reference/config/coordinate/whole grids 等。当前 hold binding 除最终 radius_independent_model_sha256 外，所有字段也必须与历史相等。

**新 capture/rebuild 使用当前两 factory 都执行完后的最终 binding。** 历史 binding 仅作为原来源和重放目标保留，不能冒作当前 factory 的绑定。新 policy 不改变真实物理签名域，也不能成为跳过原可比字段的理由。

## 6. 唯一新科学路径

顺序是固定的：

1. 只读恢复原 24 个输入、same reference163、exact x/y、完整 old/new 两池、source cfg、9-entry bank 输入；旧 optimizer 和旧 primary 都是 0 次。
2. 新 ordinary x 两网评价，核原 gate/值、登记 x 为当前唯一已接受点，保存它的两份实际 ordinary cache。
3. **在第一次 old-layout J 恢复前启动 active 120 秒计时。** 原 selected_model 与完整 factory 装配原 m10 old layout，完成上节的严格历史重放、bank gate。没有求主 LP。
4. 新 ordinary y 两网，实际核历史失败和两个唯一新 ID。原真实 d=y-x 按 binary64 原数组相减；冻结 capture 还必须核 subspace.apply(x,d) bitwise 重现 y。原 nominal proposal 仅作为另一来源字段保存，不代替 d。
5. 冻结 rebuild_failed_context 恢复同一个已接受 x，在新 complete IDs 上重新生成整个 base/J/原 selected model，再执行 selected + complete 两 factory。最终 binding 在两 factory 更新后产生；rebound complete model 从 primary registry 分离，oracle 总账保留。
6. 冻结 rebound_budget 在同一 d 上计算新 scalar slack 和完整两网 affine-e/f slack。两项 gain 都必须 finite 且大于原 floor，否则记录准确“未启动 SOC”的结果并复验 x。
7. 仅调用一次冻结 solve_rebound_correction；若得到合格 w，令 z=subspace.apply(y,w)。没有第二个主 LP、没有递归 rebind、没有新 parabolic arc 或 backtrack。
8. z 以原 ordinary 两网与原所有真实 gates 验收。它必须相对历史 x 严格降低 eta，满足原 minimum drop 或原新 target 条件，才成为已接受点。否则保留 x。
9. 原 separator 仍可从 z 学习；原失败 y 的 new_rows=1+1 从不清掉。因此这次历史分支不能伪装成 unchanged-layout SOC hold 证据。原 next_soc_hold_trust 计算一次下一 B/streak，保存但不据此继续下一模型。
10. 对真实最后已接受的 x 或 z 各做一次独立 coarse/fine 复验，严格核原 gates、exact original box、canonical state、same-state eta，输出结果。

## 7. SOC 预算保持原 scalar 定义

令 rho_s,0 是新 selected scalar 模型原初值、rho_s(d) 是该模型在真实 d 上的原最小 slack；rho_all,0 和 rho_all(d) 是完整两网 affine-e/f 模型对应值。两种基准及两种实际 gain 都单独记录。

原 SOC 保留约束仍使用：

    RHS_scalar = rho_s,0 - tau * (rho_s,0 - rho_s(d)),

其中 tau 是原 SOC_predicted_descent_retention_exact。完整两网对应 RHS 只作诊断，不替换 frozen build_correction 的原数学。旧 primary LP 的非最小 auxiliary rho 也不进入本次预算。

所有物理 margin/strip/curvature floors、相对 correction 半径、physical block M/width、原 HiGHS tolerance、可逆 scaling 和返回原单位残差检查都由冻结 helper 保持。solver 启动前先收费；异常或 status/residual 失败不能把该调用隐藏。

本次 gain<=floor、非有限、无原 LP slot、原10秒或120秒预算耗尽都须如实停止，保留已接受 x。不得为了让分支走到 z 而放松任何门。

## 8. 调用与时间账

| 项 | 本次执行 |
|---|---|
| 原 m1..m10 primary / optimizer | 0 |
| 已通过的 expanded 十项接口 | 0；只读原 log/开发 SHA/117 冻结源核一致 |
| 新 extraction/signature 人工 | 七项，仅 synthetic 字典，不调用 geometry/LP |
| 新 primary LP | 0 |
| 历史 LP 已用账 | 11 primary，0 SOC；作为来源继承，不计为本次计算 |
| 新 correction LP | 至多 1；共享原12总限额的最后 slot |
| 单次新 LP | 原10秒上限 |
| 新 active 工作 | 原120秒上限，从 old-layout J 之前开始 |
| 新 ordinary x/y/z | 每点最多两网 |
| 独立末复验 | 两网共2次 |
| 新 ordinary 总上界 | 8，且历史22+新8<=原40 |

为什么 rebuild 的 evaluate(x)+fine_decision(x) 不另产生两个 ordinary？冻结 SOCObjective.physical_geometry 先根据精确 state 恢复 accepted_cache['coarse']，其父函数随即命中同 state；冻结 MetricRecoveryObjective.fine_decision 同样恢复 saved['fine']。pool version 改变只使 selected derivative cache 失效，不删除已接受 x 的 ordinary 全网。初始 x 已经过 accepted_point，失败 y 未被接受，所以这个 saved x 仍真实拥有两网值。

driver 在 rebuild 前后逐项记录 geometry_evaluations、fine_evaluations 以及 coarse/fine accepted-cache-restore 计数的增量。实际若 ordinary 增量不为零，明确以“声明的8值界无法继续”停；不假记 cache hit，不偷偷上调 cap。snapshot 同时保留实际已消耗的全部计数。

source 原 m10 active elapsed 没有被日志完整保存。故本文不虚构“原120秒还剩多少”；这是新的、预先声明的 one-shot 实验 active120 上限，不能宣传为原历史 run 的未中断延续。原输入读取/初始 x ordinary 与新 active/末验的边界分别报告；新所有 J/JVP/full model 扫描与 correction 工作都在 active 内。

## 9. 报告和异常范围

输出包括历史完整证明、新旧签名分域、bank 精确门、原 x/y 两网差异、真实两池列表及版本、实际 d、每个新 model/rebound binding、scalar/affine RHS、原单位 SOC 残差、z 两网/学习/反馈、末验、成本。

primary 和 rebound 的 complete model registry 必须分开。原 attach_complete_model_reports 先处理唯一未求 LP 的已恢复主模型，然后 core.attach_rebound_reports 按 model10/revision1 把 correction 的初值和 binding 改写成真正 rebound 记录。没有让 zip 把 rebound 模型当成下一主模型。

原 attach helper 返回时无条件写 frozen_outer_recovery_function_was_called_without_monkeypatch=True；本入口没有调用整个 outer，所以保留这个继承标签后准确改为 False，只声称使用原 capture/rebuild/correction 数学。报告不能把它误称为又运行了旧 outer。若 attach 自身在异常路径失败，secondary_report_error 单独记录，最初的实际错误仍保留。

完整结果四类都可能出现：新预算门在 SOC 前停止、原 SOC 返回不合格、z 原门失败保 x、z 真正改善并接受。只有最后一种是一次历史点改善。任何 budget/error partial 都不是 complete，也不推断新算法正确或有效。

payload 只在 runner 临时路径与公开 job stdout；仓库与 Release 不保存大数据。公开保脚本、参数、run/source、SHA 与人类结果。新报告的 future_direct_checkpoint 标明这是历史分支，不自动成为当前主线 warm start。

## 10. 新文件、入口和已有检查复用

新增两份源码，旧117依赖不改：

| 文件 | UTF8 bytes | SHA256 |
|---|---:|---|
| scripts/frame_metric_observed_m10_soc_audit.py | 54699 | 5a69407ea22297c0af8558643f45aa8a50588670697143d5ed23c2b63126685e |
| scripts/frame_metric_observed_m10_soc_development.py | 12600 | 918702d5f6a6a25014fe2f0bc8235a60fafa38bc8c87d8c1bb8dbb3d6fdea5ca |

新 developer_check() 只检查：原 JSON 的唯一 m10 与 accepted x、两完整池恢复、重复/已接受 trial 拒绝、唯一新 ID 的充分证据、native x 或历史剩余 LP slot 错配拒绝、仅允许的 metadata leaves、原 scalar/J 两 factory 签名重放、错误 de/IDs/J/oracle 拒绝。这些是七个新分组，不重已有十项 array/SOC 检查。

已完成检查来源为 run43744903357 / job132905938795 / source5fa2424a6316b1daa8453864ce223b128a43d72f。其原 log 为3194767B，SHA14cafc198a1df4e7de2882994b37b9dffcf4284daacc49c670a9f65240926c3d；开发 JSON+LF 为14219B，SHAd5f6caa58189a34d9b059557e37323e173982c9301236acb3076781fbfc94b97。入口只读核原 run/job completed success、开发 passed/all_passed/十项 true 及完整117源码字典相等，然后输出复用证明，原十项执行0次。

CLI：

    python topics/visible-flex-new-mechanism/scripts/frame_metric_observed_m10_soc_audit.py \
      --request topics/visible-flex-new-mechanism/computations/request-observed-m10-soc.json \
      --out "$RUNNER_TEMP/observed-m10-expanded-SOC-audit.json"

新 request 继承原24输入的98个 read-only prepare 参数、原祖 request/hash与source metadata；加入 m10 原 ID/状态 hash、复用开发 proof、新两源，科学及原输入121项 source_sha256；再绑定 root 独有 workflow .github/workflows/visible-observed-m10-soc.yml，合计122项。workflow SHA256 为 a3a290ff0d09bfe0397db28bdf6273ca99b98404ac54095e98ae3e714ad39928。GITHUB_TOKEN 只供原生 GitHub API读取公开 run/log，不能写入源码/请求。workflow 仍先进行真实 public/private pull+规则阅读；规则头若前移由 root 更新接线，不绕过检查。

stdout 标签为 M10_SOC_PRIOR_CHECKS_REUSED、M10_SOC_DEVELOPMENT、M10_SOC_HISTORICAL_CASE、M10_SOC_MODEL、M10_SOC_SUMMARY、M10_SOC_COMPLETE、M10_SOC_REPORT_METADATA。最后一项给完整 JSON payload 字节/hash，不以 workflow success 替代数学结论。

冻结时：新代码未执行；没有新的科学数字、没有已通过的新七项声明、没有新的接受点。
