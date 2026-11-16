# 直接reference首次九项人工通过与入口配置字段停止

日期：2026-11-16。本稿只消费已结束的公开 Actions 原日志与现有源码；没有重跑开发检查、研究求值或旧优化器。

## 实际来源与结局

- Run：[43777844163](https://github.com/Rogerhu12/math-research-public/actions/runs/43777844163)，job `133008102089`。
- 唯一请求源码提交：`ad3b104606347c345020d229b6fbc1c648dabacc`；请求39202字节，161绑定（152Python、8workflow、祖先人类note）。
- 首次入口 `frame_metric_direct_reference_audit.py` 为27701字节，SHA256 `7bc6910328ce6d6b82fafd0693030416a4736c0e6473a4cd08520e5c9d868ccd`。
- 新三组九项人工检查全部通过。
- 科学入口状态为 `new-direct-reference-task-audit-error`；失败是读取不存在的 `source_cfg["primitive_order"]`，发生在调用新 objective 构造函数的实参求值阶段。
- 新 objective 未构造，`new_scientific_recovery_entries=0`；新 adapter 的研究完整求值、selected J、模型、LP、SOC、trial和接受均未进入。当前没有新两网门收据，也没有实际加速结果。

已完成的是必要源日志验证、24份输入与不可变对象准备，以及新小人工接口。不能把这个 workflow 的 failure 称为新几何失败，更不能把九人工通过写成研究模型或原14门通过。原最佳点仍只是合法祖先输入。

## 九项新人工的准确范围

最大12个径向节点、16个角节点，仅用新小人工对象：

| 分组 | 项数 | 已观察结果 |
|---|---:|---|
| reference_and_Jacobian_branches | 3 | ordinary8、basic J8、full two-jet J16均通过；各24/28/31个数组逐位相同，最大差0，原163/新159映射及结构相同 |
| deleted_calls_cache_and_failure_cost | 3 | 两个被删除的整场路径调用均0；同进程真实缓存hit保当前null更新；预定的单个失败调用准确留在计时中 |
| new_identity_and_selected_binding | 3 | 新ordinary身份不冒旧SHA；原selected J接口绑定本次新普通缓存；frozen copy保同一个原对象与永久reference |

精确执行数量：旧人工输入factory2，原比较geometry3（其中J2），adapter geometry6（成功5、预定失败1，其中J2）；selected factorizer构造1、ordinary bind1、selected J evaluate0。真实LP、optimizer、research geometry、full directional JVP、旧developer suite均0。

九项内部耗时1.5599133969999457秒；整个开发入口1.5606790740000633秒，RSS135064 KiB。人工对象中观察到的fixed-primitive、height-jet及缓存细分只证明这些新小输入；不将其外推为真实研究网格速度。下一修复必须读取这份完整通过收据复用，不重跑这九项或旧18/16/20/19/26套件。

## 全部实际成本与同任务预算

| 成本段 | 秒 |
|---|---:|
| 原guard完整日志读取和收据核验 | 1.2269315170000255 |
| 必要24输入和不可变准备 | 12.425874333000024 |
| 本次全部科学输入与准备 | 13.652855353000064 |
| 构造实参错误前后至异常记录 | 0.0011811779999106875 |
| 全部本次科学时间（从原日志读取前开始） | 13.756976061000046 |
| 科学开始前导入、新开发、源码哈希等 | 3.4872812469999417 |
| 本次总进程 | 17.244257307999987 |

整个科学进程峰值RSS299708 KiB。表内分段存在正常记录开销，不强行把几个小段相加改成总值。

这13.756976061000046秒属于已经发起的独立direct-reference任务的1800秒总科学限额。必要后继修复要把它累计进入同任务时钟，并计入下一次源收据读取和必要prepare；新值/LP累计仍为0。没有以这次入口错误新开一个更大预算，也没有把此前已耗尽的旧120秒m7 epoch并回本任务。

旧closed epoch的active241.3142038439999秒、initialization293.5427817930001秒、LP10、values15及两个失败/恢复准备仍按[旧完整结局](paid-attainer-restoration-budget-first-completed-actual-20261115.md)独立保留。本次没有重启旧LP11，也未复现或重新消费未知旧方向。

## 输出身份与规则实际拉取

原完整日志185504字节，SHA256：
`1890cc27b6f6ca3ff28cf2d821c73e9c4e78b8912822452cd6ec17c52a61b0cf`。

关键日志记录按规范JSON加LF计：

| 记录 | 字节 | SHA256 |
|---|---:|---|
| DIRECT_REFERENCE_REQUEST | 26268 | `948243d9dbf009e2a1634db26ee636fa5a3eb143851f6bf3c004fcf918e6462e` |
| DIRECT_REFERENCE_DEVELOPMENT | 25953 | `717719da39d867b3206c12250ccc1df92e5276245cc48d8d9e4e6ba76b4accae` |
| DIRECT_REFERENCE_PRIOR_WORK_REUSED | 1135 | `46480623a3a683dd1a202c9b1f2f47f7105ca43580c5e64d85aa1546a1944661` |
| DIRECT_REFERENCE_COMPLETE | 52471 | `d7d82f9646ca3e5da536f7622645e81cb7e402062ff3039190edd6c49d42c648` |

Runner临时audit为58831字节/hash `29b699724a7446b05049f20c9b8b1ba1db1243ad97153edfadebeb9d0f056806`；summary59225字节/hash `80ed2d7d5f4bfdff4c96c1314c08898eae4a7ef799539a333f35d268276fcd56`；development30403字节/hash `8b5fed8f83943a27925b220ce56bfb8d10fa17efa9b5b20919184b4e913fe7f1`。这些payload只在本次runner临时目录与原log，没有写入Git、artifact、Release或跨run缓存。

公开实际 `git pull --rebase` 于00:01:00.734491—00:01:00.977543 UTC完成，前后均 `ad3b104606347c345020d229b6fbc1c648dabacc`。根README blob `21bd547f56590b7f2dd279d0297efb289a9b2783`、本题blob `d0432faff569c8e9af7ed4809847e12880976c11` 均空diff。私有actual pull于00:01:03.209253—00:01:03.614773完成，前后均 `44a25d2c60fdc81e98da4ea88eec84a19ec5362d`；根blob未变、题README不存在、QUEUE本会话唯一进行中。root于00:05:03读完这些记录；下次公开actual pull最迟01:01:00 UTC。

## 立即继续的准确工作

对照原成功guard/paid入口，修正primitive order的真实来源；其值、原规则、固定g/b0、14门和几何方法均不因此改变。随后唯一修复请求只复用本次九项完整收据，继承本次科学成本，在同一新任务余量中进入尚未执行的真实ordinary/J/模型/实际步。冷速度、fresh context首模型绑定、两网门与是否取得新下降均待实际返回；主课题保持进行中。
