# 共享背景场的完整 cover 与 held 薄入口

状态：源码与接口已保存；只做纯 AST、冻结源码 SHA 及字符串接线后的 AST
静态核对。**没有新 fixture，没有本地科学计算，没有实际父场或几何通过结果。**
数值调用仍限于本公开仓库 GitHub Actions。

本条接续
[共享 B 闭几何 wrapper](2026-11-14-shared-background-closed-wrapper-interface.md)。
两个独立新入口为：

| 入口 | SHA-256 |
|---|---|
| `geometry_20261114_shared_background_continuous_cover.py` | `fc5bbb6762cf589a8ab6096c066bdd1bbad17c516954a43c4a40496445e9a5fb` |
| `geometry_20261114_shared_background_held_hausdorff.py` | `f9c6466c1a9b8eccde3a5cf83159d2f30f2b2a00b0ab51bf49b83c9b1e698b90` |

两者都锁定几何 wrapper SHA
`ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb`。
原 loader、geometry wrapper、R241 空间门、held 距离公式均未编辑。

## 1. Cover 只替换输入/身份接线

新 cover 先调用原 `geometry_20261114_full_state_continuous_cover.build_program`
取得原实际全域 gate 程序，再仅做下列源文本变换：

- 加入 `--source-directory`、`--source-basename`、`--descriptor`；
- 输出 schema 改为
  `R37-R241-complete-shared-background-spatial-cover-budget-v1`；
- 输入 SHA 清单增加 descriptor，结果增加原源体/旧转换程序/新转换程序和
  新几何来源身份；
- 执行 namespace 中的 `load_full_bundle` 明确绑定到
  `geometry_20261114_shared_background_closed_assembly.load_shared_bundle`。

最后一点是实际函数绑定，不是仅改说明文字。没有旧 loader fallback。
该 loader 会重核原完整来源 bundle、真实 accepted 父场与自身 tail、
新 descriptor、wrapper guard、新 plan/background、mesh 和 normal 包。
所有 active centers、法向和 prefix child 点由同一新几何对象直接读出，
包括完整 z0、原 SE2、原 R249 选择和同一共享 (B)。

以下算法保持原源：全部空间块、所有 pair 类别、角子分块、帽盘与 marker
成本、全家族直径、reach (0.03D) 门、曲率门、正则 C² 浸入前提、每项
position/normal/metric/slope/radius/curvature 误差包络及相同的失败记录。
不把标量背景变更当作自动改善这些量的证据。

新场的 metric 参考仍是原独立 source table，而非 (1+B'^2)。所有包络
必须属于这次新几何；程序只是消费它们，默认值和有限 sample consistency
不是严格连续包络证明。没有把旧 A 的通过数值搬过来。

静态源接线后程序 SHA：

- 原 full-state 转换程序：
  `b800b0727c8c1683589fa80df9bb405443b19c3665e2a0b89d538d83b2b20e52`；
- 新共享背景转换程序：
  `d3a71b6a986bb4ec01789c80c5f0fc8bd6f952b4ed7b862389ca8424e8631390`。

这些只是源文本身份，不是科学结果。运行时再次核唯一替换锚与全部冻结源。

## 2. Held 复用整像公式和完整绑定

新 held 直接复用原 full-state `bind` 函数体，只把已知 coverage schema 和
其 producer SHA 两处改成新入口。全部原字段、完整模式身份、原/new
闭包、R249、SE2、绝对 mean、所有 active chunks、两个完整帽盘、marker
支撑、(D) 分母与误差包络的核对均保留。

它还**实际调用** `load_shared_bundle`，把该 loader 返回的整个 binding 与
新 position packet 的 binding 逐项比较。故 held 的额外来源验证会重新
构造同一完整几何及 cut；输出如实记
`new_SavedPrefix_or_tail_evaluation_run=true`。这不是重解 BVP/tail，也不重跑
空间 pair pass，更不产生新接受场。

通过上述身份核对之后，仍由原
`geometry_20261114_held_hausdorff_cover.main()` 读取所有原 SHA 绑定 chunks，
计算 witness 到全部 active balls 和两个完整 cap disks 的距离下界，保留
全家族 marked diameter、witness/rotation/position 误差和原 (0.2) 门。
不将材料点位移当成整像 Hausdorff 距离，不用核心直径替代全曲面 (D)。

reach 数值通过仍不是 held witness 的前置条件；失败的 reach 报告只要
position packet 完整且来源一致，仍可提供该独立幅度诊断。所有连续包络
与正则 C² 前提仍单独支付。held 新 schema 为
`actual-complete-shared-background-held-Hausdorff-cover-witness-v1`。

## 3. 真父场后的命令

令 `$NEW_CLOSED` 是新共享 B renderer 的输出目录，`$ORIGINAL_CLOSED` 是
其原完整来源闭包。两者默认 basename 都是 `surface`，也可显式指定。
使用本次真实新场的包络参数，不填历史 A 的结果来冒充。

```bash
python "$C/geometry_20261114_shared_background_continuous_cover.py" \
  --directory "$NEW_CLOSED" --basename surface \
  --source-directory "$ORIGINAL_CLOSED" --source-basename surface \
  --descriptor "$BACKGROUND_DESCRIPTOR" \
  --checkpoint "$ACTUAL_ACCEPTED" --port "$ORIGINAL_PORT" \
  --config "$ACTUAL_CONFIG" --tail-response "$ACTUAL_FINAL_AUDIT" \
  --complete "$ACTUAL_COMPLETE_READOUT" --source-topic "$PUBLIC_SOURCE_TOPIC" \
  --curvature-upper "$K_UPPER" --relative-metric-upper "$ETA_UPPER" \
  --tail-slope-upper "$SOURCE_W_UPPER" \
  --radius-lipschitz-upper "$SOURCE_RADIUS_LIPSCHITZ" \
  --position-error "$POSITION_ERROR" --normal-angle-error "$NORMAL_ANGLE_ERROR" \
  --radial-stride 1 --angular-stride 1 --prefix-angular-subdivision 2 \
  --out "$OUT/shared-cover.json"
```

原 writer 同时写出 `shared-cover-position-cover.json` 及完整 chunks；不另
引入 `--position-cover-out` 参数。随后消费**这次**对应的两个报告：

```bash
python "$C/geometry_20261114_shared_background_held_hausdorff.py" \
  --directory "$NEW_CLOSED" --basename surface \
  --source-directory "$ORIGINAL_CLOSED" --source-basename surface \
  --descriptor "$BACKGROUND_DESCRIPTOR" \
  --cover "$OUT/shared-cover-position-cover.json" \
  --coverage "$OUT/shared-cover.json" \
  --checkpoint "$ACTUAL_ACCEPTED" --port "$ORIGINAL_PORT" \
  --config "$ACTUAL_CONFIG" --tail-response "$ACTUAL_FINAL_AUDIT" \
  --complete "$ACTUAL_COMPLETE_READOUT" --source-topic "$PUBLIC_SOURCE_TOPIC" \
  --rotation-position-error "$ROTATION_POSITION_ERROR" \
  --out "$OUT/shared-held.json"
```

held 保留原 `--phase` 和 `--witness-source-index` 可选项，不强制另设新数值门。
报告输出必须尚不存在。两个入口当前都没有被执行，不构成完成标准的通过。
