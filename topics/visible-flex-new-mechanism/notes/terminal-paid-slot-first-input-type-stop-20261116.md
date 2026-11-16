# 末槽首次入口：十一新分支已通过，原浮点10秒类型检查在恢复前停止

日期：2026-11-16。**已完整消费唯一公开原日志；这是输入实现失败，不是新模型或物理候选的失败。第64个LP仍未启动。**

## 1. 唯一实际身份

- run 43786841449 / job 133036290253。
- source 60ff5c1171c3c94ac84f7fcb88427c530daf69e8。
- [原公开job](https://github.com/Rogerhu12/math-research-public/actions/runs/43786841449/job/133036290253)，failure，完成于01:32:58 UTC。
- 请求38549B，SHA256 0b571b9cdcd1305c56b79130270883d77a6941e0ba1f994b4f6ef8847fa6e4f1。
- 原stdout136943B，SHA256 0216ddbbdd392d1e23240378b8aa6d61c4e154076db42895e2806004fab416eb。

root已读完整原tag，REQUEST的168绑定与实际请求相同，COMPLETE的158个Python身份亦逐项相同。没有把失败原日志或checkpoint复制进Git。

| 原记录，JSON加一个LF | bytes | SHA256 |
|---|---:|---|
| REQUEST | 27707 | 37a8976234f4966ce643dc993336346949049b92ab654c97bbd68315922cd8ae |
| DEVELOPMENT | 1792 | 6cf5254aaeef45fe6cc68ece4c9b0f5b6359dbe0ac1233d3f53dc02d01de1a06 |
| COMPLETE | 21997 | ef90eadd0fe0314cfe4f388c311cd619748ba8c64b357dcde593e355b54f94da |

## 2. 十一个已付新分支与其准确范围

首次公开执行3组，case数4/3/4，全部通过：

1. 原末分支资格、已有trial拒绝、gap已合拒绝、64已花拒绝。
2. 原重复行完整保留、新行判重、无新行零调用、非有限支持拒绝。
3. 一次63→64且无SOC、同槽二次拒绝、开始后异常保收费、开始前异常不虚收费。

原DEVELOPMENT用时0.000886163秒；入口计时0.000889610秒。三个stub callback已发生；真实LP、ordinary geometry、directionalJVP、旧developer和科学优化均为0。

这些是旧core SHA0042cb95a8f61f53f35e9edeed028fa0ed8f42215c952dd4b19c889fcd9afe40、developer SHA3ea04322743cb45efbb157a4bd6f449ed227552ca5d53faab324491bb7036f45上的真实通过收据。fixture使用整数10秒；它们没有覆盖随后遇到的原浮点10.0输入。后续必须只读复用这11条，不机械重跑，也不冒称它们已在修改后的新core执行。

## 3. 实际失败位置

入口已下载并核原science源日志，在transfer.read_completed调用validate_release时停止。原trace最终为：

ValueError: original direct-task resource limit differs: linear_program_seconds

具体原因是新core的_ledger_guard把四项资源值一并要求为Python int。原长期沿用的单LP值却是10.0：frame_curvature_feasible_steps.py原configuration写linear_program_seconds=10.，DirectReference只要求其数值等于10并原样保留。原完整cfg及其SHA未改变。

因此不能把原cfg改为整数10；那会改原hash。准确修复是保64/160/1800三个整数限制不动，单LP项接受有限且数值恰等于10的原numeric，仍拒布尔、非有限值和其他额度。

本次未进入必要24输入恢复、constructor、普通value、selectedJ、完整模型、LP64、SOC或物理trial。没有新方向JVP、没有新接受点、没有修改bank/池/learning。该结果不证明末槽新支持无效或原模型驻点。

## 4. 必须继承的全部费用

| 账 | 实际值 |
|---|---:|
| 原累计科学秒 | 257.595331213 |
| 本次新增科学秒，含原日志读取 | 2.884255101000008 |
| 本次结束累计同任务科学秒 | 260.479586314 |
| 当前process总秒，含import和新developer | 4.209023590000015 |
| 峰值RSS | 153336 KiB |
| 共享LP累计 | 63 = 62 primary + 1 SOC |
| 真实value累计 | 58 = 29 coarse + 29 fine |
| 本次新LP / value / J / model / trial / accepted | 全0 |

原64LP/160value/1800科学秒、每LP10秒仍不变。源257.595331213已经含两次更早direct入口失败，不再加一次。下一未完成输入路径须从260.479586314开始累计，读取本失败收据和原science输入也收费；不能重新给1800秒或丢掉本次2.884秒。

既有第27接受点仍是唯一物理当前点：physical bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c。其η/曲率/两网14门沿原direct完整实际记录；本次没有独立重评价这些数值。

## 5. 两次实际pull与已读规则

公开actual pull始于01:32:46.498215，结束01:32:46.895014 UTC，before=after60ff5c1171c3c94ac84f7fcb88427c530daf69e8。根blob21bd547f56590b7f2dd279d0297efb289a9b2783、题blobd0432faff569c8e9af7ed4809847e12880976c11均未改，两diff为空，实际返回0。

私有actual pull为01:32:49.393916→01:32:50.697657 UTC，c3994ae5d1ced54daeb8d23676700daff42e001c→a53fa5f4ce67d539be10e5eea3985f1fce6e697f。根blob5ba164843b1f5802184178a82d786264404873a3不变，题README仍无；QUEUE唯一且为本会话进行中，未发布私有正文。

root于01:36:30读完这些原字段；下次实际pull最迟02:32:46 UTC。输入类型修复及已付11收据复用正在继续，不重跑本次已完成分支；尚未消费第64次、未达到README主门。
