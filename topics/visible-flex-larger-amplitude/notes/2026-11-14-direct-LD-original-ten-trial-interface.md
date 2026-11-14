# 新 direct-LD1372 方向接回原十档非线性试步

类型：计算流程与源码接口，54运输修复后待实际运行；作者：root；日期：2026-11-14。

本入口直接衔接 [868块形成](2026-11-14-rawcell0-direct-longdouble-capture-interface.md) 与 [完整1372系统](2026-11-14-direct-LD-complete1372-system-interface.md)。唯一方向来源是52新矩阵的一致重解，不使用旧41或43方向冒充。全部科学运行仅在公开仓库 Actions。

| 新源 | SHA256 |
| --- | --- |
| `geometry_20261114_native_direct_ld_trial_replay.py` | `99204fcd615affc393a04800f62f80d05dce5225a90ece6c27b4b00e4c241160` |
| `geometry_20261114_native_direct_ld_trial_replay_hook.mjs` | `373c82c75152a800246e84618fb2ba72fc0b3960e3b3e4eff9b7590724bad4ce` |

两个文件薄改原 rawcell0-step replay。Python增加新的capture目录、实际result SHA、source与独立矩阵身份；Node只改绑定和schema。原核心的十个alpha、无J `evaluate`、全部guard和严格 `test.norm < ev.norm` 接受分支保持原表达式；源码插入继续逐字反向恢复到原核心，未加入线性残差门、删模或改变原容差。

## 来源与完整限制

原28 baseline 明确取原 `result.json.gz`，SHA `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`；它是已存 with-J 基态，不称新计算。原41结果仍为 `6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf`。新adapter完整核两原件及868新块，保原非J数组和全部节点映射；新capture四源及所消费metadata按size/SHA绑定。

方向读取新消费者 `result.json.gz`、`input-binding.json.gz`、完整1373节点checkpoint及限制577节点checkpoint。两个checkpoint中的完整binding必须与同一新adapter逐字段相同；每行全部224坐标及negative-zero sidecar恢复后核完整raw字节，限制方向严格等于完整方向按原 `old_to_new` 抽取的577行。原41矩阵仅作来源身份，结果明确不声称解了它。

新capture的逐stage evidence在 `large-arrays/`，Python允许经过边界检查的相对路径，拒绝绝对路径或逃离目录。它们和全部新数组保留在完整artifact，不为发布方便丢行。

## 运行与输出

workflow先取得28/41完整固定artifact，再由公开仓库恢复78个原source。完成868块后才计算实际capture result SHA；完整均衡与三轮预算精确修正完成后才计算实际direction result SHA，随后进入本试步入口。不从未知未来结果猜hash，不在本地运行RHS、RK、J、范数或求解。

该入口除原history/source/capture CLI外接 `--step-directory`、`--step-result-sha256`、`--direct-directory`、`--direct-result-sha256`、`--direction-directory`、`--direction-result-sha256`；默认新producer文件及SHA固定为本次消费者，不能换成旧producer。输出独立于全部输入。

spec/schema前缀为 `original-native-direct-LD1372-trial-replay`，环境键 `VISIBLE_FLEX_NATIVE_DIRECT_LD_TRIAL_REPLAY_SPEC`，进程符号 `visible-flex.native-direct-LD1372-trial-replay.v1`。第一次真实接受后保完整selected状态及字节身份，按计划停止这一次line search；若十步全拒，完整失败/guard/原读数仍保留且进程非零返回。Actions无论成功失败均先上传完整artifact，再发布有界报告。

一次试步接受仍不是原native容差接受，更不是课题完成。后续必须由真实选中状态继续原方程、最终原native门和fresh audit；再完成本课题README要求的闭合、同g全族、operator、reach、固定区及整面幅度。

## 静态完成范围

root已读新source及相对原replay的完整差异。仅做AST、Node语法、workflow YAML、13个bash片段与4个内嵌Python语法检查；没有本地科学计算。job显式使用150分钟资源预算，capture45分钟、完整solve45分钟、原trial30分钟。预算不是科学接受标准；超时或失败保原件并继续处理真实原因。

54版本只跟随capture完整gzip修复更新new adapter与solver pins；原十trial数学、selected-state存储和原接受规则均为同一表达式。52尚未启动native，其原trace见[实际52记录](2026-11-14-actual-request52-direct-LD-spec-transport-failure.md)。
