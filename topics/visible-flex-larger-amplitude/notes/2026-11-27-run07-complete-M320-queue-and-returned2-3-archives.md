# Run07：完整 M320 后继与真实已返 2–3 参数归档

## 1. 真实状态与读取范围

本次只作源码、完整参数和已公开小记录的读取及编辑，不执行 F、J、root、积分或区间算例。运行是公开 Actions `45909290354/1`，请求 `visible-larger-resume-20261126-07`。队列读取快照为 `d9394ebeb6d5067ae8652d487468fe5ab9f0c7fd`；根随后已将全部 M320 v2 源普通发布到 `5feb2207f7c0dcf7832fa10f6f05f7abc22a531a`。

先从 Git tree 读取文件大小，再完整读取 48,412-byte 原队列、3,897-byte 实际 index 和 31,775-byte 第 1 小卷。实际 index 的记录时间为 2026-11-27 03:13:15 UTC，明确已返阶段为 1–3，当前是 `complete-material-envelope-cached-normal-first-20261126-07` / running，子进程尚未退出。不能由等待时间填造第 4 步结果。

实际来源：

- `notes/2026-11-26-public-actions-45909290354-1.md`：3,897 bytes，SHA256 `a2de15588d1d324f475040962d97af933aec9ca6d84e78317ac4d0357661ef2f`，Git blob `faa7e12315e1900b2ded4b4d9b25bece88d109d2`。
- `notes/2026-11-26-public-actions-45909290354-1-part-001.md`：31,775 bytes，SHA256 `8630c9e440a6eaf648e3fcec35eb86e67b03a7d4ddab4db07ca2ba1ef2888749`，Git blob `f79052f10a6adb41c53f39101784ee8b34842fa3`。
- 原队列 `computations/resume-20261126-followups-07.json`：48,412 bytes，SHA256 `58ac96f1648c1d8afcb1ba3a285b11d2eeace0138ae5a0c9f7d95283392a57c5`，Git blob `181f7fb20a6d3d4a51bff08e15ae4a52ba15b049`，完整恢复提交为上述读取快照。

## 2. 只归档真正返回的两个 followup 对象

归档文件 `computations/resume-20261126-followups-07-returned-stages2-3-complete-parameters.json` 保存原两个对象的全部字段：原 step ID、source path、完整 argv、parent bundle、全部 outputs、完整 summary selectors、scope 和 reconstruction_source；没有以缩写 argv 或只存 SHA 代替对象。另保两个原对象各自的 compact-JSON SHA、全部实际 command、source commit/source SHA、实际 output file records，以及指向上述完整实际小卷的身份。

阶段 2 是完整原 `so3_axisymmetric_reference.py` 参考准备，实际 state=completed、returncode=0、source commit `d2fa260c0adde7c89e94a96cafc8be03ced3a091`。实际报告 `78411d9a91633816fd514b927d288ad17922b67eca0f5bd4fd400ec3a06b1821` / 29,792 bytes；实际 reference `e435343954ed3c9fd2617e36185a1e0a71213cc6b432eb94578066954930c5db`；实际 carrier `7c8b3cbffd66a360b01341db8e1179f211da3c264de85812020a5e48ad5637c3`。这些只引用原返回，没有读取数组或重新计算。

阶段 3 是原 `restore_actual_run05_observation_carrier.py` 必要输入重建，实际 state=completed、returncode=0、source commit `40f73dbacdd18bab36cda4cd6b421a1d1b917694`。报告 `926db461a4efce0fa40ab539b9df28143f8664cca25ec96e95ebe1d7aa83dcdf` / 19,691 bytes；旧 carrier 全文确为 `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` / 227,202 bytes；binding `aaa65a5ecac807e97cf771a08dd57d2ac26b48adf6acc9592025c0c706581c8e` / 1,537 bytes。既有全 cells/u/Gauss 原字相等结论照原实际小卷保留；本次不重复重建。

本次不归档 warm 的 controller journal，也不改 controller 已记录的运行历史。移出活动队列的仅是这两个已真实完成 followup；所有原待返对象完整保留。

## 3. 新队列的准确顺序

新 `computations/resume-20261126-followups-07.json` 按下列顺序保六个完整对象：

1. `complete-material-envelope-cached-normal-first-20261126-07`
2. `actual-material-envelope-cached-normal-first-20261126-07`
3. `complete-frequency-M320-from-cc0a-20261127-v2`
4. `actual-frequency-M320-from-cc0a-20261127-v2`
5. `all-actual-material-envelope-seed-batches-complete-mean-profile-fees-first-20261127-07`
6. `complete-material-envelope-reference-node-four-jet-fees-first-20261127-07`

原第 4 步 science、紧随其后的原 pure，以及两个费用步骤，每一个完整 JSON 对象与读取快照中的对应对象精确相等。新插入的两个 M320 对象与已发布 `M320-frequency-refinement-cc0a-v2-ready.json` 的 `steps` 精确相等。没有删减任何 summary、预算、source、参数或 pending 责任；只改变步骤列表位置。

原队列的非 steps 字段也原样保留，包括 `finish_when_done=false`。后继仍可据实际返回继续追加。

## 4. 完整参数和真实父绑定

M320 两步使用已刊完整 v2：

- science driver SHA256 `6a900861c01d0967dc585dd84797cc2428b62bd4a5969d594a68387c7a0175be`；
- launcher SHA256 `dbdf9cce0a2a294e601a6416b0084bdbc66a0257151d50e702a53b1c81514e43`；
- pure reader SHA256 `bc0c2c64d4f512fe4a42711e1b0f91ef4496a03a7b1d969c27febd5476c3f2eb`。

来源、13 个完整运行源、3 个完整再生器、51-role runtime closure、布局、normal 和历史合同详完整 v2 实施说明。所选参数文件 SHA256 为 `150277da610fa7c6aa5b47866ca35f04f38e65b2b193b10433ae8d038b8f86ef` / 72,978 bytes。

科学步的 parent report 明确为 `{work}/reference-centred-c1-material-envelope-normal-lift-first/report.json`，checkpoint 为 `{work}/reference-centred-c1-material-envelope-normal-lift-first/final.npz`；二者与仍在运行的原 cc0a science 实际 outdir 对应。原 cc0a pure 也读同一个 report，且位于 M320 之前。未来实际父报告、model、final SHA 不预填，不把尚未返回的第 4 步宣称为可用场。新 transfer 必须读到完整、来源正确的真实父才会注入；没有完整父时应保持真实 setup/科学失败，不造 checkpoint。

M320 pure 的 controller parent 是已存在的参考 bundle，允许真正首次 fine 场失败时仍读取其失败报告。新布局 M320 / 原冻结 M160、J923/N2048、32 共同阶段、全自由量、三路 omega、同准确 g、原完整 typed E 和几何真筛保持。新规范范数与 μ 为已明确参数，不继承旧统计或证书。

这一版本只登记 cc0a/91c 既有家族；本次实际使用 cc0a。没有静默接受 run08 新 chart/target 或 repaired 5c5c 家族。两个原费用步骤保持它们原来的实际 report 输入，未冒适配到新 M320 报告。

## 5. 队列体积：沿原格式完整保存

原队列本来就是 compact JSON。保持同样的 compact JSON 与末尾换行，新完整队列为 **86,173 bytes**，相对 95,000-byte 准入上限仍余 **8,827 bytes**。

若改为两空格缩进会有 100,207 bytes；那只是展示空白的增加，并非实际当前编码需要。这里沿原 compact 格式，不删除对象或字段，不压缩/编码二进制，不拆数据文件，也不需要另造 pair wrapper 或参数载入器。所有实际值与完整对象已经用文本等号核对。

## 6. 本次完整交付与发布边界

| 完整文件 | bytes | SHA256 | 远端未引用 Git blob |
|---|---:|---|---|
| resume-20261126-followups-07-returned-stages2-3-complete-parameters.json | 21409 | `1e8809cfef81fa48fc1755b8c91743f907e52fda9e833e9dfb64db9d93ac9e7d` | `f111a54cf2ff61be537ce85b55ea569ebf3bbf8c` |
| resume-20261126-followups-07.json | 86173 | `ac39413d179e75079dae0391c99f73cc40970b0d9ef4401afeb18117db985b6d` | `140064a25b7b7172faeea8a9e0e227d9d0493eb5` |

root 发布前应以原 queue whole SHA / 四个 pending 完整对象核对当前分支，保其他同时到来的新步骤；本草案未更新 ref。以上四 pending 已逐对象保持，真实 2/3 全对象已完整归档。源码/参数处理没有运行科学或引入新 fixture，也没有将排队当作已执行、已接受或连续几何完成。
