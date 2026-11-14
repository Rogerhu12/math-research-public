# Strong 当前实际检查点（2026-11-14T08:38:57.776683+00:00）

课题尚未完成，尚无新耦合半步 prefix 接受。公开写入因实际自动审批拒绝仍暂停；本地实际求解继续。

## 正在运行

- session：**28520**，实际开始 08:25:33 UTC。
- 完整计划：`/workspace/scratch/ffc1334c1988/strong-work/loop-margin325-half-actual-r4-plan.json`。
- 实际 launch/未来真实退出：`/workspace/scratch/ffc1334c1988/strong-work/loop-margin325-half-actual-r4-launch.json`。
- 日志：`/workspace/scratch/ffc1334c1988/strong-work/loop-margin325-half-actual-r4.log`。
- 输出及完整迭代分块：`/workspace/scratch/ffc1334c1988/strong-work/runtime/topics/visible-flex-larger-amplitude/new/loop-margin325-half-actual-r4-*`。
- 原 supervisor 的停止文件：`/workspace/scratch/ffc1334c1988/strong-work/loop-margin325-half-actual-r4.stop`。不得从另一个 exec 命名空间按旧 PID 发信号。
- 稳定源码在 `/workspace/scratch/ffc1334c1988/strong-work/runtime/topics/visible-flex-larger-amplitude/computations/`；固定源在 `/workspace/scratch/ffc1334c1988/source-dependencies/topics/visible-flexible-closed-surface`。

## 已发生的真实数学步骤

M32/1280角/35参数/2590初节点和全部13方向同一半步、原全部验收门保持。新的初始H已真正完整审计，首次请求逐位匹配；闲置Node不存在。首完整J、QR、线性解都成功。alpha=1、.5、.25的真实trial依次被原Armijo拒绝；alpha=**.125**的首个inner Newton步真正被接受，物理merit由 .0137068173435 降到 .0129302881078，scaled collocation由 .0898436796822 降到 **.0795726991102**，BC由6.5146982e−8降到**5.5572491e−8**。

它只是第一内迭代更新，远未通过最终RMS/完整新H/物理审计。当前正在第二个完整J。新 manifest 为 `new/loop-margin325-half-actual-r4-iterate-0002.json.gz`，SHA256 `ba41dd0765b7c7ff5212295c0a161ba076db8f3b1ef99602b5cf434d8769e63c`。完整7件数据已经另存 `/workspace/scratch/ffc1334c1988/strong-work/r4-first-inner-step-recovery/index.json`，以防原两代保留策略退休旧块。

## 执行选项与恢复

r4只改变执行：radial24/collocation12、2个RHS线程、原字节arena的fdatasync/fadvise选项、独立256MiB complete-input cache。原/advised存储逐位对比已真实通过。cache身份为 `3797019285c88c27b07c468694df638c6938245f089ee4901ea75752631e4951`，目录 `/workspace/scratch/ffc1334c1988/strong-work/loop-margin325-half-actual-r4-prefix-cache/3797019285c88c27b07c468694df638c6938245f089ee4901ea75752631e4951`。所有源、编译函数、runtime、对象和完整输入字节检查保留，不能改比较器强行命中。

进程仍活着时不应重启。如果它结束，先读原wait4结果与最新iterate，再使用新输出前缀和原入口恢复。只有原起始 iterate-0001 的H已知与 `/workspace/scratch/ffc1334c1988/strong-work/runtime/topics/visible-flex-larger-amplitude/new/loop-margin325-half-Haudit-r1-response_0001.json.gz` 和配套ready逐位相同；**最新iterate-0002的H尚无其自身真实非线性尾解/完整审计**。恢复新H时应走原工厂重解、J和audit，不能继续套初始audited-H标签。

r1/r2/r3三次−9都是外部信号事实，不等于数学失败。r3完整23件在 `/workspace/scratch/ffc1334c1988/strong-work/margin325-half-r3-recovery/index.json`，但匿名J/QR字节未保存。已冻结的r3/I/O及大核心scalar连接包由root本地提交；未来真实结果应另建新包，本现场只是时点快照，不是后台完成承诺。
