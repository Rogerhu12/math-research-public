# 已付m7见证细化：首次人工检查通过，真实入口在评估身份处停止

## 实际来源与结论

首次公开执行为 run43771970034 / job132989648048，源码提交
68f92b9cb16677278dfbc7f8e13bdf7189e41d9c。工作流于2026-11-15
22:56:32 UTC结束，结论是 failure。原始job日志430490B，SHA256
ba23313fae7855266456502ea1b5ac1f6b8d3799d5a833c6adbc749a1b3bd69d。

本次新增的四组、每组四条人工检查全部通过。真实入口随后完成必要原输入准备，
在恢复同一epoch的ordinary evaluation definition时触发精确哈希校验；
未进入一次新的科学solver入口，未调用LP11，未形成新模型或新物理trial。
这不是新LP不可行、原cut模型驻点、.26达成或主课题完成的证据。
原已通过双网十四门的最佳点完整保留。

## 已支付的十六条人工检查

四组均 passed=true：

1. paid_witness_and_same_model_binding：同原模型/四个已付见证接受，
   guard targets变化、原observable指纹变化和final pool绑定变化均拒绝；
   不恢复不存在的旧159维方向。
2. valid_supports_and_original_memory_retention：旧438行和顺序保留，
   bank/config不替换，binary64 unit-ball合法，缺失selected witness仅走原行接口。
3. single_new_call_and_inherited_budget：旧剩余时间耗尽在新call前停止，
   无新支持0LP，唯一新call序号11且留原SOC槽，
   solver异常仍保已经开始的call费用。
4. repaired_candidate_and_original_return_gates：共享限变化拒绝，
   旧标量门不恢复或返回缺失旧方向，非改善修复候选不送几何，
   原bounds门拒绝非法新方向。

人工执行收据：real_LP_calls=0、ordinary_geometry_calls=0、
full_directional_JVP_calls=0、original_developer_suites_executed=0；
new_stub_solver_calls=5。人工检查不证明真实恢复成功，真实恢复另有下面的失败。

十六条已支付成功，后续只读该原收据并核源码身份；不再次执行本组或旧
18/20/19/26/cache等研究。core和development若不变，其成功收据可原样复用。
若新增修复必要的具体校验，只执行尚未付的新校验。

## 真实入口的精确失败和费用

PAID_ATTAINER_COMPLETE.status 为
paid-attainer-audit-error-paid-best-preserved。ValueError：

> same epoch ordinary evaluation definition could not be restored exactly

发生于frame_metric_paid_attainer_resume.py构造器的
self.evaluation_sha256与原epoch哈希047cefae968152d170387cf64a9f7b0f132089685472c10868de9379967d93e9
比较。不能跳过该门、另授新模型身份或把历史initial375改标当前438。
下一工作是逐字段审查原成功构造器及元数据来源，恢复原定义。

new_scientific_solver_entry_calls=0；old_optimizer_calls_this_run=0；
old_LP10_or_old_direction_replays=0。stage.model_count=0，
new_accepted_iterates为空，solver及本次snapshot计数为空。
未产生新完整网值或新J/JVP；必要原输入准备实际发生，不能称本次零计算。

费用必须保留：prepare_elapsed_seconds=14.667315975000065；
从真实恢复开始到报错0.08626015199990889秒；
进程总18.621493514000008秒；peak RSS 296092KiB。
原旧epoch active35.54239845799998秒、初始化264.864081096秒、
value_geometry212.6957086999999秒、共享值14、LP10/12，
均为来源费用，不是本次新执行。
下一入口须将本次恢复0.08626015199990889秒累计进同一120秒预算，
准备费用另列且持续累计；必要对象不能跨runner直接保活，不隐去重建费用。

原最佳物理身份e0ab278d1525c90a2be30db12c78e6faac369a8b8d01f0236f4fe6fd02e79f83，
原eta=.26623355613853394、两网最大曲率57.99982504159888；
原bank438、池4432/4525版本1/2、八个已提交学习事件及原控制器保持。
eta仍是metric epigraph辅助值，并非delta-hold；.26/1e−6/reach均未付。

## 原始载荷身份与不重放范围

以下为原标签JSON加一个LF的身份；只保回执，载荷不入Git/Artifact/Release。

| 标签 | 字节 | SHA256 |
|---|---:|---|
| PAID_ATTAINER_REQUEST | 22686 | e69001f12ed703299ffa4224f29fbf926f6581c06b5eab89c45763159f1ddd77 |
| PAID_ATTAINER_DEVELOPMENT | 17680 | ab0755d597c2c626144e823b92d30f887bae96eac2173973179baaf9b218701c |
| PAID_ATTAINER_PRIOR_WORK_REUSED | 1135 | 46480623a3a683dd1a202c9b1f2f47f7105ca43580c5e64d85aa1546a1944661 |
| PAID_ATTAINER_COMPLETE | 305143 | b2a6f4f62684c3d820cb81a6b0bc5a8311957d47a12749d45fb7657948f24515 |

工作流临时audit.json为485577B/hash
6f8dfeb866b0056c90e12364be5e5b5d688012489caa750fca5823b89d616fee，
audit-summary.json474892B/hash
4557a2b3ed9c40bfc2cbda0b9cc6521e928656551819e95b81e943c7df599d77。
这些仅在原runner临时目录，未提交或上传artifact。
修复沿用原12LP/40value/120active/10秒每LP与一个m7接口，
不重做已完成前六步、旧LP10或旧方向，不借失败重置预算。

## 每次实际拉取与规则

本次公开实际git pull --rebase于22:56:03.158651至22:56:05.567623 UTC，
从源码68f92b9…推进到c3cce53015c7783a36102bfc5961cddaafa9b817。
根README与本题README的diff均为空；根blob
21bd547f56590b7f2dd279d0297efb289a9b2783、题blob
d0432faff569c8e9af7ed4809847e12880976c11。仅另一题更新，不改变本题规则。

私有实际pull于22:56:07.764101至22:56:08.339035 UTC，
before=after=a5da2028a7585abb517d5f84551120d288636cbb；
根README未变、私有本题README不存在，QUEUE唯一行仍为本会话进行中。
root已读这两份回执，HANDOFF记入该SHA；下一实际pull不迟于23:56:03 UTC。
