# 固定颜色 word 消费器：准确开发分版记录

日期：2026-11-15。本记录只涉及新增小人工和源码检查。**没有本地真实 head、profile、原式消元、几何或路径积分运行。** GitHub Actions 的最终新增人工与真实消费者尚待公开执行；下表不把局部早期回执冒作最终公开通过。

## 1. 已实际执行的四组新增人工

| 组 | 执行时源码 | bytes / SHA256 | 新人工数 | 实际结果 |
|---|---|---|---:|---|
| 固定色规则初版 | literature_color_priority_words.py | 17408 / 150bbc31f96386c4bd493735cc9669d0f1b8e0d119b621566455f3401ace266b | 10 | 全过，0.007902705 s |
| 停止与恢复增量 | literature_color_priority_words.py | 21212 / 2817e312505894ed41d7f7442fc3aa6e6fcad821c46efc6d0406204f06a28b78 | 3 | 全过，0.002830397 s；未重前10项 |
| 77列接口首版 | literature_character_head_word_relations.py | 71097 / d92af90ff99f3bc09e39702b93b932e1aee5b91e8994bb7dc280a6d83c6aefa4 | 6 | 全过，0.022854805 s；未读研究数据 |
| 输出与新进度边界 | literature_character_head_word_relations.py | 72712 / 53a8c52359577fb47ef9a587422804ef7f94e38af246cb1ae847262e5b27881d | 1 | 全过，0.005731232 s；未重6/10/3项 |

初版10项覆盖新的固定颜色选择、同右锚 local/word IBP、全部shuffle重数、最高颜色零阶终止、缓存顺序、人工 pure 行只读接口和显式预算退出。

停止恢复的3项准确核查：

1. 单轮调用上限为2时中断，恢复仍用单轮上限2，继续尚未完成的原语；累计统计从2到4，未把累计上限抬高伪装续算。
2. 全局 cache 超限撤回本次插入；保存状态能按相同全局 cache 上限读回。
3. snapshot expression pool 在构造时受独立字节上限限制。

77列接口的6项使用两条**人工构造**的原函数相同、字面多项式不同的列，验证完整原差和两根转换和、准确原行/B/单点值、伪转换拒绝、完整与紧凑的中途映射/中途证明续算、源绑定拒绝，以及固定颜色余letter语法。

最后1项只构造空进度的小人工输出，检查 certificate/state/main 预留的合计上限，并改变内存进度确认“最新准确进度已保存”会相应转为false。未重新做前述关系测试。

## 2. 原回执文件身份

| 文件 | bytes | SHA256 |
|---|---:|---|
| color-priority-words-local-development.json | 942 | 8868493d0f3534dad780f377fc4f12a0138e1071736fdbfce61732923ddca37b |
| color-priority-words-resume-local-development.json | 549 | 908a6c00fe758b78e125225356a166019c6e9f26a9bb07bcb2c69e19d001be03 |
| character-head-word-relations-local-development.json | 2021 | 8b60fbc4bbeb68861c5f06c1358ea01916b47d10a662bf879caef1375bc2fc02 |
| character-head-word-relations-storage-local-development.json | 1596 | 4be020e44e5f7cfef0077839c5fd87b360284950c7fa68cf24a746934171bc83 |

这些回执本身保留各次执行源的身份，不能通过改名让它们变成其他版本的执行结果。

## 3. 最终提交版本做过什么

最终源：

- literature_color_priority_words.py：21642 B，SHA256 ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9。
- literature_character_head_word_relations.py：72953 B，SHA256 8fd67984ef66bc43da2055b68f6d8b062dde260035668c4f565f9f105e344f13。

两个最终文件的 py_compile 已实际通过。

映射模块在3项增量后仅增加固定余letter语法查询，并把调用统计标签明确改为“已启动，可能包含被中断的调用”。消费者在最后1项边界检查后仅修正紧凑缓存中的本轮统计复制，并明确小main预算范围和最终实际长度检查。根代理与另一代理分别静态读过完整新逻辑；这是源审读，不是研究目标运行或最终完整人工回执。

最终公开 job 的 toy 入口安排 **6项新消费者人工 + 3项新增续算人工**。它不重复已成研究原值、pure40、31条pure依赖、70条字面依赖或86行。该公开 job 是否实际通过，须由本次公开 run 的 development.json 和 receipt 单独报告。

## 4. 真研究门

真实消费者必须运行在 Rogerhu12/math-research-public 自身公开 GitHub Actions。它只消费已发六个目录；没有本地设置 GitHub 环境变量绕过入口，也没有本地预跑候选。最终实际中若触发预算、存储失败、来源不符或未完成，都必须据真实回执保留对应状态，不把小人工成功改写成研究结论。
