# 新环境逐字恢复与第一次实际 direct-CSC 主运行

日期：2026-11-10。会话：Astra-visible-flex-78718bd0 / numerical_recovery。
状态：**主运行已由 root 实际启动；尚无最终成功或 G5 结论。**

## 已实际完成

1. 当前 Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0；六份冻结 SciPy 源 SHA 与已审 foundation-v2 全部一致。没有修改环境包、原算法、容差或物理参数。
2. root 在新 checkout 路径实际执行 pure checker（chunk dff588，exit 0）和15例字节/别名测试（chunk c817a1，exit 0）。委派记录绑定 root 所给真实回执；冻结 preparer 的 `--check-current-gate` 实际返回 ready=true（chunk ebd70e，exit 0），0 factory/solver。
3. 原 reference 包固定 SHA `e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83`。`scripts/78718-restore-frozen-m14-layout.py` 从当前部分 checkout 逐字恢复134文件、6,919,663字节，原97绑定均检查。报告 `2026-11-10-78718-numerical-restored-layout.json` SHA `3305bd58d129cffe139ceaf3022e4e90ce3b7141df8daf81c3fddff8264b4fe0`。全部目标先核无冲突，未覆盖未知文件。恢复前该绝对目录不存在。
4. 恢复目录为 `/workspace/scratch/db6f0b0e7462/math-research`；它现在是**本次新环境创建的来源副本**，不是前会话的进程或现场恢复。旧 LU02 的退出仍未知。保留这个绝对路径是为运行原逐字来源门，原 reference/CP/tail/source 不重写。
5. 因为 factory 证据绑定真实路径，root 在恢复目录重新实际运行两项检查：pure chunk 68029c（exit 0，0.228秒），byte chunk d4e4ec（exit 0，0.445秒）。输出 `2026-11-10-78718-numerical-restored-csc-*` 四件已与当前 checkout 同名文件逐字同步。它们只支付实际源码/整数与15个小矩阵/别名门，不支付曲面。
6. 冻结 pure preparer 实际 exit 0（chunk 31504f），141绑定/27回调，0候选初始化、0 BVP/DN。新 launch SHA `a05d22affb9a4dc5c06f1095527b1ae0ba66af423b3ade00bf8e65c846da7487`，保存为 `2026-11-10-78718-numerical-m14-direct-csc-01-launch.json`。

## 当前主运行

root 实际启动回执 chunk **667592**、session **67354**；已观察 `effective DATA = [6442450944,6442450944]` 与 `event=started`。主 stem 是恢复目录 notes 下的 `2026-11-10-78718-numerical-m14-direct-csc-01`。

新资源 wrapper `scripts/78718-run-m14-csc-resource-6g.py` 仅设置每进程 DATA 6 GiB 后调用原磁盘 guard。它是新文件，未沿旧绑定名安装不同来源。Node 原 heap1536 MiB；磁盘暂停512 MiB、恢复768 MiB。149项完整 guard 绑定 SHA `fcaf2122799032d32d93fb6dc358f4ba2df6d55ebfd58393b13374a8011df0dc`。启动前可用内存约8.6 GiB、磁盘49 GiB；这些不是峰值或成功保证。

实际 solver argv、cwd、全部文件身份、固定数学参数见 guard-launch 与 launch。求解本身保持 M14/N512、W14、depth12、P8×S32、原 floor .05、原8轮 outer、原 tol 2e-9、BC 1e-8、physical BC 2e-11、max6500；来源就是原已审 direct-CSC/release-LU 入口。

原种子有2633节点，旧 RMS约1.9978998187e-9，但旧物理 metric 采样约7.946154957e-8；本次不是把这个旧 solver_success 字段当作整图收敛。只有本次真正 s1、末次自有 Jac/audit/seam、完整自然退出及新整图连续证书都付清，才能讨论终门。

## 分工与下一步

root 持有真实长会话并记录退出；numerical_recovery 只读监测、首包审计及生产链准备，不另启动主 solver。未参与优化的 independent_audit 保留从前置原种子到最终新网格的独跑身份。

新候选成功后，必须从本次 CP 的 `tail_seam.tail_record` 提取自己的真实末尾包，不复用旧尾证。独立复算、完整 G5/新网格仍开。最新根规矩第12条已读；每次 pull 的 README 差异检查及已读提交由 root 统一维护。

## run01 实际失败及 run02 的来源修复

root 已观察 run01 自然 exit2（chunk 5e28f1，session67354；guard 2.002243470999929秒）。失败在 Node worker 初始化：缺历史 `general_root_smooth_tail_cells.cjs`；0 BVP、无首DN完成包。原97绑定清单没有该动态CommonJS来源。run01 的完整失败log/reproduction/summary/guard退出和 root观察均保留，没有改称成功。

`closing_tail_dependency_blobs.json` 原已冻结该源的 Git blob `3b98e488e05b2cce59ff8d9d03b4ad78302d8efa`；实际补源6319字节，SHA256 `d074799099e27401456449343c8f490ec60cdec7eb0d02758f024f541d409575`。新补源脚本按原9文件 blob 表逐字核同，并检查20个literal依赖存在。它不改变数学且不声称覆盖任意动态路径。

run02 以全新stem重新纯准备，实际exit0（chunk bc35a6），141内部绑定/27回调、0solver；其外部guard新增补源及闭包身份，原reference与runner等全部不改。run02 launch SHA `b935a5863a88e6c4541357a558c6b3874ed3ba89174b65032b0494425681c671`。新主运行须由root持有真实会话。

run02 root实际启动：chunk `00aa17`，session `44394`；DATA6GiB已应用且 event started。尚未取得最终退出，不以运行记录推定成功。

run02 的首真实 DN 已由冻结新版 auditor 独立只读检查：chunk `a83a78` 自然exit0，`PASS_FIRST_ACTUAL_M14_DN_ONLY`，残差 `5.397833270174952e-10`；616项Jac、17jet、865×28阶段状态及13×28原始状态完整。本次首请求按原流程 audit=false，不能称末端源审计。first-binding 由真实运行在完成Newton/CSC身份选择后写出，未由恢复脚本生成。三份闭文件已逐字同步到当前checkout；主BVP/最终退出仍待root观察。

## 2026-11-10：同一背景输入与首 DN 参数预检

主 run02 持续运行期间，终端按实际 manifest / packet 头文件取回了原
M8/int2 的 8 个 raw 分片、tight / lowmetric 两份 NPZ 及六项背景定义。
8 个 raw 分片的原 SHA256 全部相符，压缩总量为 10,494,261 字节，
每件小于 5,000,000 字节。没有取回约 80 MB 的旧 M12 有限图作中间基底。

以 run02 自己已闭的 `tail_0001` 为 `--new-checkpoint`，实际执行原
`db6f-tail-transfer-background-v3.py --check-parameters-only` 两次：
tight 的工具回执 `eb7b41`、lowmetric 的回执 `863c2c` 均自然退出 0。
两次都复核六项原背景定义、包及 NPZ 散列，11 个实际差异键均属于原数值
白名单；它们没有改变冻结物理背景。原始预检输出为
`2026-11-10-78718-numerical-first-dn-tight-background-preflight.json` 和
`2026-11-10-78718-numerical-first-dn-lowmetric-background-preflight.json`。
汇总、实际回执及 raw 分片身份存于
`2026-11-10-78718-numerical-m8-background-inputs.json`，SHA256
`c50af6d6c1f6f34d56335259e891dda9f3b664300193b89b031395d70802f335`。

这只是原来源和首请求参数检查；0 次新增求解，不调用转移网格或新有限图
构造，不支付新图的连续 metric / 曲率界。最终仍须使用本次实际成功 CP
自己的最后尾响应、完整新 manifest，再运行正式背景转移。

随后按原 terminal gate 的常量表核对9个固定 REFERENCE，原 SHA 全部
相符；取回的 height 和 positive-alpha 也正好等于该终门的固定 SHA。
原 `db6f-audit-closed-budget-transfer-v3.py --check-transfer-policy-only`
对上述 tight/lowmetric 两预检分别实际自然退出0（工具066add、8c6a95），
核清六定义与 height/alpha/bookkeeping 的连接。汇总
`2026-11-10-78718-numerical-fixed-proof-preflight.json`，SHA256
`c048343c9cf3fbd6661c01c6ce3ac2d6878e2457e970d65ca4659ee3c9b23fab`。
原输出状态中的 independent 指 producer/consumer 分开核查，不表示作者
执行了未参与优化者的端到端独跑；仍0新求解、0新图、0正式转包。

本次条件式全链接线另存
`2026-11-10-78718-numerical-post-csc-chain.md`。原末门仍要求读取旧 M12
24 raw 分片（合80,730,280字节）和自己的旧尾CP/点包；仅将其下载推迟
到新图实际有望进入末门时，不删除或放宽该检查。M8背景直接转移与此
旧点下界的最终来源门是不同用途。
