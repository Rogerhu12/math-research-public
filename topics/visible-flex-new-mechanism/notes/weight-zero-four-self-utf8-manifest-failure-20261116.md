# 四个权零 self：首次入口清单字节数错误

**分类：实现输入失败，科学尚未开始。**

公开 run43817737164、research job133133535871，
源 `bdd66f8469a9d09b1600329d32074e4612d48e18`，请求
20871 B／SHA `e328bb129fe0f5d2a996bafa68e3f816cc3dba8f3d034d5d4fb70368e2551f83`。
workflow 中完整 `source_sha256` 验证已通过；入口的额外完整
`{path,bytes,sha256}` 清单检查在
`scripts/literature_weight_zero_joint_self_completion.py` 失败。

原文件有一个非 ASCII 字符 α；源码字符串字符数为 50184，
真实 UTF-8 字节数为 **50185**。请求清单手录了字符数，少记一个字节。
原 SHA
`1f5d671598ca6fc4a804c6f22a65d145b5ced3743506a2144d507717ff4789d3`
正确，源码没有改变。修复只把这一条 metadata 的 bytes 改为 50185，
保严格原 SHA、路径、全部旧来源、源码与科学范围。

作者同时追溯同一清单来源：另外八项直接读取源码的长度已按 UTF-8 原文核定；
其余24项来自 R316 原运行 source_hashes 的 bytes，
`read_original_actions_log.py` 的 50679 B 来自 R434/R443 原 source_manifest。
因此没有为通过入口而改旧源或降低核对条件。

原最终报告 `entry_outcome=original_input_or_source_binding_failure`、
`science.started=false`、`completed_record_count=0`。
原日志读取0、旧根恢复0、新 current/self0、旧 rank/dev0。
末 FINAL_CLOCK 记录本入口实际耗时 **0.005253693000000226 秒**；
统一科学钟尚未开始，不能假称它已经做了四个科学收缩。
这次前置失败与其耗时保留；修请求后继续同一个未开始的四目标任务，
180秒科学上限及其全部规模门不增加。

## 本次实际 pull 后已读规则

公开 actual pull 06:35:20.669106 → 06:35:21.220448 UTC，
before=after=`bdd66f8469a9d09b1600329d32074e4612d48e18`、rc0，
根与本题 README diff 为空；blob分别
`21bd547f56590b7f2dd279d0297efb289a9b2783`、
`d0432faff569c8e9af7ed4809847e12880976c11`。
已读这两个 diff，下一实际 pull 最迟 07:35:20 UTC。

私有 actual pull 06:35:24.149406 → 06:35:24.810492 UTC，
before=after=`0bce963fc67dbe510b2fb916dae7d69797b83c0e`；
根 blob `5ba164843b1f5802184178a82d786264404873a3` 未变，
私有本题 README 不存在，QUEUE 本会话唯一进行中；不发表私有内容。

## 原始输出指纹

原生接口解码串按 UTF-8 编码：92382 B／SHA `d9bb7f065da75da3fe2296ae422841a8304da90b189a7c2368ddd736cb7badd7`，来源仅称解码串，不假称服务器下载字节。

- COMPLETE_WEIGHT_ZERO_SELF_REPORT JSON+LF：2634 B／SHA `270d6e15800d7da14386bfed5809c1932537b46ee4d171e799163fed6db09801`。
- FINAL_CLOCK JSON+LF：713 B／SHA `fcf40081f4ed9644518e585c18bf1b7e3db9e6317146483ac36bd39081c33db1`。

不提交原日志/JSONL/数组。后续消费四个完整 self，保 R466 的共同
$\mathfrak h\in\operatorname{span}\{\mathfrak y\}$ 关系；不以两个单独 MEMBER
布尔值替代。主目标未完成，继续。
