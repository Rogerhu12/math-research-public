# RET78：三个已终态 Fejér Actions 的完整控制器输出保全

日期：2026-11-28 UTC。状态：来源、参数、实际返回与恢复关系已完整形成；本文件和台账只请求 root 删除七个精确旧输出路径，不写 ref、队列或科学源。

固定恢复提交：`c81a76206aa5627989fd1763cc7ff3639e457fe4`。该提交的本题完整树为 `15a4082193c7706797e32ce566a34f6271e8dbd9`。本批毛退 **264,570 字节**；新增文件的最终字节及净额由完整 delivery 给出。

## 1. 范围与保全方式

根 README 第 15 节允许在保留完整脚本、输入、参数、实际 run/SHA 与结果归属后退役可再生成的旧输出。本批只有 run19、20、21 的三个控制器索引和四个阶段分卷。它们都是已刊控制器从 runner 的 status/journal 生成的紧凑 Markdown；不是源、参数、原始场、数组、checkpoint、唯一输入或新的证明。

[完整台账](../computations/terminal-fejer-actions-retention-78-complete-provenance.json) 在 `deletion_files` 中给出七个文件的原路径、完整字节数、SHA-256、Git blob 和恢复提交。它还保存九个实际返回阶段的全部命令、输入和输出文件身份、真实退出码、耗时、全部 summary_errors、missing_outputs 及原 cleanup 元数据。每个完整 metrics 对象用原 whole-file 身份、JSON fence 序号和 member 定位，保留整个未经筛选的标量映射；不是只留本文挑出的数值。

现有的三份完整 launch/continuation 说明、两份终态说明、run19 normal 实际失败的 JSON 与说明全部保留在当前树。源、请求、所有 whole ready 和原参数构造器也保留。较早的三次 2026-11-20 Actions 需要另一个历史源/队列归属包，本批不纳入。活动 run22 及其后继完全不动。

## 2. 实际结果必须按层级区分

| 运行 | 官方终态 | 已公开自然返回的阶段 | 未付或未知 |
|---|---|---|---|
| 19：46076669320/1 | completed / success；官方更新 2026-11-28 04:00:47Z | 两个输入均 0；完整 science 为 0；pure 为 0；准确 normal 费用为 1 | normal 声明报告缺失；原 Python 异常尚未返回，原因仍 null；没有准确几何或 reach 证书 |
| 20：46079535427/1 | completed / cancelled；官方更新 04:46:09Z | 两个输入均 0 | science 自然退出码、最终 report/final 和完整 typed/accepted 历史未返回；取消原因未知 |
| 21：46084442413/1 | completed / cancelled；官方更新 05:37:58Z | 两个输入均 0 | science 自然退出码、最终 report/final 和完整 typed/accepted 历史未返回；取消原因未知 |

这些官方更新时间不是推断的子进程终止时刻。原完整官方 run/jobs 对象分别保留在下列 whole notes：

- [run19 完整启动和自然返回](2026-11-27-run19-complete-bhalf-launch-and-continuation.md)，96,434 B，blob `cb7298353531f198ad599445602e495bf51bc612`。
- [run19 费用失败及官方终态](2026-11-28-run19-complete-return-normal-fee-failure-and-continuation.md)，29,783 B，blob `1a632b70dd3e8ee13d594017132825e87f6ac6be`。
- [run20 完整启动、观测与官方取消](2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md)，93,699 B，blob `6c5f86daae94b925f0f23ba75c4617484f5e3c11`。
- [run21 完整启动与观测](2026-11-27-run21-complete-five-eighths-launch-and-continuation.md)，95,194 B，blob `eaa854edc501e1a0368e55b39cf9d98494844773`。
- [run21 官方取消与完整末次观测](2026-11-28-run21-official-cancellation-and-last-complete-observation.md)，27,474 B，blob `845d425d774fb2785be68f83337c33b6462a711e`。

run19 的 63,722,853 B 完整 report 的原 SHA-256 是 `ed1ea5db4d0b8961a954ccdd31d1f4662477537a64457db3d7c9eb8875ae3856`；本批没有读取该大报告。其 pure 实返把当前点绑定为 `20d617114ba603edf83e02f342ae26946054cc69a6f99d5f7a9bc474981af45f`，模型为 `0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add`。四次 restoration 接受后，Phi 为 3824.990529790781，最大相对 Gram 读数为 0.6460480621212836；仍不是合格解。六个带符号的 current g 依次为：

| 家族 | 实际值 |
|---|---:|
| reach | 0.9662472339877322 |
| body diameter | -0.03813557730789774 |
| distance plus | 0.005865730451148687 |
| distance minus | -3.0936337267194034 |
| cap diameter | -0.06715136488669782 |
| height floor | -1.0411715338774452 |

原 stop 是 `declared_restoration_budget; actual_violation_remains_and_is_not_accepted`，`final_geometry_passed=false`。四次已接受 restoration 不等于整个约束系统可行。science 原 19 个 summary 错误和 pure 原 22 个 summary 错误均逐项保在台账；它们不会被空列表替代。

其随后 normal 费用真实用时 324.00838658499924 秒、退出 1、没有声明的 report.json。保留的 [实际失败及报告入口证据](../computations/actual-run19-accurate-normal-failure-and-capture-entry-evidence.json) 明确 `actual_error_trace_returned=false`、原因 null。源级发现“初始读取与规划在原报告写入之前”等可能路径，不是本次已查明原因。本批不把这个失败改称 mean 根、曲率或积分失败，也不把官方 job 的 success 改成所有子阶段成功。

run20 的末次完整小进度对象另外原样保在本台账中。run21 的末次完整对象与上述终态 note 第三个 JSON fence 全对象相等，直接 whole 引用。两者都没有被升级为完整最终场、接受历史、typed 清单或费用输入。未公开的历史仍是未知，不是空历史。

## 3. 完整源、参数与实际输入

三次运行使用同一明确 source family：driver `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f`，launcher `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506`，reader `8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49`。完整 137 角色和 18 个 runtime 身份由 [完整 source delivery](../computations/fixed-fejer-meridian-producer-binding-repair-complete-delivery.json) 保留；包含全部原 120 对来源。其整文件为 52,830 B / SHA-256 `970b8f8bbb141fc7f1c4e5e42d6048497f0de58731e65918f3c4e4cf6aff008a` / blob `45f14a52f824ca947a59bacf73ad123f17fddab9`。

| 参数 | run19 | run20 | run21 |
|---|---|---|---|
| seed boundary total length 字面 | 1/2 | 1/2 | 5/8 |
| seed profile delta 字面 | 1/32 | 1/32 | 1/32 |
| restoration damping 字面 | .01 | .001 | .01 |
| metric damping 字面 | .01 | .01 | .01 |
| science argv / formal / live 数 | 157 / 458 / 48 | 157 / 458 / 48 | 157 / 458 / 48 |
| 预定 pure argv / formal 数 | 7 / 445 | 7 / 445 | 7 / 445 |

这是实际 whole ready 和原命令的对应关系，不覆盖原请求里完整保留的祖先元数据。部分继承说明包含旧 seed/source 字样；完整请求原字保留，当前实际 argv、source SHA 与字段归属在台账单列，不用旧祖先说明冒当前执行体。

每次均从两个完整必要输入构造开始：maker 的原 6 argv/14 selectors，以及 reference 的原 26 argv/62 selectors。maker 源为 `89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60`，reference 为 `e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb`。完整 Fejér RN-even binary64 配方、160 个核心词、923 节点、全 R690 标量、2218 counted-tail 叶、7377 carrier、原 8-Gauss 和全部初始化方法原样保留。accuracy_reached=false 不被改写为误差已付。

唯一历史标量参数投影来自固定提交 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 下完整 accepted .99 的 `stage-00/actual.json.gz`，2,614,352 B / SHA-256 `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` / blob `6a9dfda743c464af6ae1190208e7157fa66df30f`。原 maker 只按完整接口消费 analytic_extension_origin 和 fixed_scalar_profile.geometry。该历史文件不在删除清单，本次只沿已刊完整 metadata 记录身份，没有读取 gzip。本次也没有从旧 warm 抽取核心词、按耗时选 chart，或导入旧已接受场。

run19 的完整初始队列 72,837 B、后续 pure-only 队列 52,138 B 以及 pure+normal 队列 58,432 B 都有独立 whole Git/SHA 身份。前两版用各自固定历史提交恢复；当前同路径的后一版不能冒前一版。完整 science/pure ready、N 的 49,322 B whole ready 仍保留。N 的全 38 argv、36 selectors、900 秒、完整角度、径向、精度、百万叶与 32-stage 责任没有在此变动。

## 4. 真正 writer / reader 边界

完整 `public_actions_controller_parallel19/20/21_compact_metadata.py` 均为 19,984 B；三者只有四处 parallel HANDOFF slot/name 字面不同。已读 `Publisher.render` 从 runner 的 returned records 生成索引与分卷，并附完整原 request；`Publisher.publish` 写这些路径，再检查原 200 MB 目录界限。`main` 实际读取 source/request，建立 detached worktree、取回固定历史提交，并以 `followups_only` 从空 completed 列表开始必要输入。

完整 `public_actions_followups_with_active_progress.py` 为 32,762 B / SHA-256 `046f0d7b8d27df95f5249438fdaf435b00c482b009fa8956f27dbdc662a6b314`。其 `poll/begin` 读真实 full queue、pin 当次 worktree，再构造完整命令。`run_step/finish_record/save` 在自然返回后记录实际输出、每个所选标量或明确错误，然后写 status/journal，最后出版。它不读取这里的七个 Markdown 文件来决定 F/J/root、队列 admission 或 scientific input。

原 `poll_active_progress` 的双有界读取与 48 selectors 是只读观测，不是 final。原 `public_cleanup_metadata` 仅压缩公开 copy；其原 record_count/byte_count/metadata SHA 全保，不能声称原 runner cleanup 细节仍在当前目录。

本批没有声称这些文件没有其他历史消费者：现有 launch notes、数学记录和人工比较可能链接或引用它们。凡读取原完整 note 的消费者，必须按下面精确恢复路径读回完整旧文件；不可把本文或某一组选出的标量当原 whole report。原 scientific pure/fees 消费的是各自真实 runner report、输入和 immutable packet；旧公开索引不能替代那些文件。

完整三个 workflow 也保在台账：ubuntu-latest、Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、CPU Torch 2.5.1、四个单线程环境变量、350 分钟 workflow timeout、20,000 秒 controller admission budget 全保。耗时及官方取消不能据预算数字倒推出原因。

## 5. 恢复与未声称事项

每个 `deletion_files` 成员给出完整路径与完整 blob。需要旧字节时，从固定提交恢复整文件：

```sh
git show c81a76206aa5627989fd1763cc7ff3639e457fe4:topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46076669320-1-part-002.md > recovered-run19-part-002.md
```

对其余六项使用台账中的确切 path。完整字节数、SHA-256 和 Git blob 一一给定；不能换成近似名、局部行、重排 scalar 或新的截图。要求旧原路径的历史消费者在独立历史 checkout 中先放回该整文件。

科学重算由完整已刊 recipe、源、原队列与参数构成；实际新浮点结果、时间、路径及 run 身份必须另报，本文不许诺跨硬件科学重算与原数字逐字相同。**原公开输出的逐字恢复依靠固定 Git 对象。** 这一区别也适用于官方 success 与科学未完成、原 scalar 包围未达 tolerance 以及未返回的 20/21 历史。

本批没有运行科学、AST、编译、fixture、benchmark 或重放；没有新增准入门，没有读大报告或任何 binary。所有 proof/source/parameters/当前结果说明、accepted099、parent91、现存 canonical、ports、Nelder 与活动输入不动。发布时 root 只对这七个精确 path/blob/size 做 fresh 比较；任何不同都留树，不扩展删除范围。
