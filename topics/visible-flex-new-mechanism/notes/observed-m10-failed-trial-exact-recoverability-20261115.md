# 已观察失败 m10 的精确状态与扩池恢复

作者：tail_cost；2026-11-15。本文仅消费既有公开日志与冻结源码，不运行科学或人工检查。

## 1. 可恢复的目标

本次只选 norm-memory run **43741276060**、job **132894771246**、source **c30e7ea00a9ae06356409d5fdae289dfecf2210d** 的第十个模型及其唯一 alpha=1 primary trial。

其原结果为 new-rows-return-to-last-accepted-before-SOC：两网值已实际计算，未接受，coarse/fine 各新增一条原行，然后返回旧接受点。原运行没有对该 trial 作 SOC。本次新 expanded-pool 运行 43744903357 的 rebound 分支为零次，不能代替这一试验。

**原日志足以精确恢复 m10 的 x、y、扩池前后完整 ID 列表、固定 reference163、configuration 与九条 bank。** 无须重新求解旧 primary LP。普通全网值、Jacobian 和新 SOC 仍是后继公开 Actions 要实际完成的新工作，本文不预报其结果。

## 2. 状态直接来自原数组

m10.linearized_at_accepted_index=7。原 COMPLETE 的 accepted_iterates[7] 与 m10 唯一 trial 均保存：

- exact_binary64_independent_coordinates：完整 159 个有理字符串；
- exact_original_physical_coefficients：完整 163 个有理字符串；
- canonical physical SHA256；
- 原两网直接 η、κ、全部实际门与点位信息。

取前者为 x、后者为 y；不通过 nominal LP 步或舍入后十进制状态猜 y。原 proposed_step 另完整保存，但新 SOC 必须采用实际 binary64 y−x，并由原子空间 apply 核实能逐位回到 y。

| 项目 | 原记录 |
|---|---|
| x 的 accepted index | 7 |
| x canonical physical SHA256 | 10b0a3b208ccb13919227d2b459995bffbe86dd528f0f1f136098d7b75adba1d |
| y canonical physical SHA256 | 627c9474c4f3d2cb9c28c248f1ae06251274e1c1d50a2097280fc93e57d4d290 |
| x159 原有理字符串列表 compact JSON SHA256 | ace52b298af8c62e6c52d50f17cf851c9243ed07b38841a3d9ec2b10f9820578 |
| y159 原有理字符串列表 compact JSON SHA256 | 34aec5782f7cacac8e965c0f9fde2f6548257b95ca3893be88a48e8b378d556f |
| 原 alpha | 1 |
| 原 B | 0.000125；报告保 binary64 精确有理值 |
| x 两网最大 η | 0.26636800393715654 |
| y coarse / fine η | 0.2663651531755449 / 0.2663651530478497 |
| y coarse / fine 最大曲率 | 58.00000333192753 / 58.00002409366549 |
| 原两网真实 η 降幅 | 0.000002850761611661312 |
| 原 trial 结论 | 未接受；两网曲率门失败 |

source configuration SHA256 仍为
b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6。
原 reference163、159→163 定义和物理盒均在 COMPLETE/future_direct_checkpoint 与绑定中；新入口不另选 reference、不改 configuration。

## 3. 扩池后的完整集合就是原末池

原 m10 的 coarse/fine 版本与数量为：

- 扩池前：versions (4,7)，数量 (4417,4091)；
- 本 trial 原学习：各新增 1；
- m11 开始：versions (5,8)，数量 (4418,4092)；
- m11 接受后新增 (0,0)，之后没有其他模型或学习。

原 set_pool / set_fine_pool 是保全部旧 ID 的单调 union，并按原编号排序。故 m10 扩池后集合准确等于原 COMPLETE.future_direct_checkpoint 的完整：

- coarse_pool，4418 个整数；
- fine_pool，4092 个整数。

这不是从数量猜集合；完整最终数组在原日志中，m10 后唯一 m11 的学习记录严格为零。

## 4. 扩池前集合也能唯一恢复

冻结 frame_metric_budget_recovery.py 的 separation()：

1. 对硬行保所有违反原容差的 omitted 行；
2. 对两个 soft group 保其超过已选包络的 omitted 行；
3. 额外保 true-η peak 点的两个 soft slots；
4. 清除已在池内的 ID。

原末 pool history 的 reason 正是 m10 最后一次实际 set_pool。两网均记录：

- soft 两组 whole_grid=0；
- omitted_hard_violating_count=0；
- metric_minus omitted=0；
- metric_plus omitted=1；
- 总 omitted=1；
- coarse true_eta_peak_point_index=11040；
- fine true_eta_peak_point_index=22080。

因此唯一新行必定是原 group_index=1 的 peak slot。原网点数分别为 61440、122880，所以：

- coarse 新 ID = **61440+11040=72480**；
- fine 新 ID = **122880+22080=144960**。

两完整末池中各 ID 恰出现一次。删除该一个 ID 即得 m10 原旧池；不用求值或搜索候选行。

| 原集合 | 数量 | compact JSON SHA256 |
|---|---:|---|
| m10 coarse 扩前 | 4417 | cbc5100fd624e48ac6515ba0c5c9435f53b0ab09ca4805b2c5d94c22eb4added |
| m10 fine 扩前 | 4091 | 1af3afd7ffa7bc55908f6e6c70759e54f3a89daff83420616faf79288e0be61e |
| m10 coarse 扩后 | 4418 | 88039c5e6c70f3767536ce7016159495f7074dc71654bd634186e41dcc0b2fc6 |
| m10 fine 扩后 | 4092 | c9620badc20d7a2b6924f3e0b1ef759e2aae337ab506b637a96bf3784779bd90 |

扩后两 hash 与原 history.row_indices_sha256 一致。表内 hash 的对象是原整数列表 compact JSON，不混用 NumPy raw-array hash 或 selected-soft 子列表 hash。

## 5. bank、原模型与剩余预算

m10 的 LP 记录 initial_rebuilt_memory_rows=9。唯一两条新方向事件在 m8.cut_rounds 的原 per_row 中；m9、m10、m11 没有再插入方向。因此祖输入 19 个事件加 m8 的两个原事件可恢复 m10 时的九条 bank，完整 hash：

07a1f00af0acc950a7db91c698d824b3ce47324921272f45b2e2b1b1eca18f81。

该同一重放已在 run 43744903357 的首模型前准确通过，后继仍应绑定本次原输入而不是硬编码已重算 entries。不把 complete_model 镜像中的事件重复计入。

原 m10 保存 original binding、两层 complete model binding、原 de/df/值的 hash、原旧池 versions 和原物理映射 hash；但没有保存其完整普通几何缓存或 Jacobian 数组。因此后继必须：

- 用同一真实 field/reference/configuration 在固定 x、y 新评价原全网普通值；
- 以原旧池构造旧 model 对象并核原 binding，**不求解旧 primary**；
- 先完成两个 factory 再取 final complete signature；
- 在相同 y 上采用上述准确新池，调用原 capture_failed_trial / rebuild_failed_context；
- 用新池的新 x-J、y 残差、真实 d=y−x 和原 scalar RHS 作一次原 SOC。

原 m1–m10 的 primary 内 LP 次数为
1,1,1,1,1,1,1,2,1,1，共 **11**；SOC 为零。因此 m10 所在历史共享 12 LP 账本尚有一格，恰可容一次 correction。该试验不能再求新 primary、重复 SOC、回退搜索或扩预算。

新的普通值与 J 恢复费用必须公开分账，不能假称是读取缓存。原 40 值/120 active 与 SOC≤10 s 的界可采用原界或更小的预定界；没有保存逐模型精确 active-clock checkpoint，故不能虚构历史 m10 剩余 wall 秒数。新入口应明确自身恢复与新试验计时，并保唯一 LP 的历史 11+1 计数。

原 m10 已学到 coarse/fine 各一条。即使新 SOC 接受，也必须保这两条原学习事实；不能因重新绑定而把它们清零、授原 same-layout radius hold。只有完整实际两网与原所有门通过的新 z 才可接受。

## 6. 原件与未决部分

原 [run 43741276060](https://github.com/Rogerhu12/math-research-public/actions/runs/43741276060)：

- 完整原 job log：3,443,509 B，SHA256
  5e3be6e199829aee81de637c9e856a5ca0b91caa2154cefec913461c48c136e8；
- 原 NORM_MEMORY_COMPLETE JSON+LF：868,908 B，SHA256
  f14909e957164ea1bc92363ec228b91cf2adff773270108afe9005d4856d12bf；
- 原 source：c30e7ea00a9ae06356409d5fdae289dfecf2210d。

本次仅处理 m10，不扩展 m5。精确恢复结论不授新 SOC 的可行性、接受、目标到达或效率改善。所有新普通值、Jacobian、原 SOC 求解与 z 的两网验收都尚未执行，只能由后继公开 Actions 完成。原 payload 不另存仓库、Release 或 artifact。
