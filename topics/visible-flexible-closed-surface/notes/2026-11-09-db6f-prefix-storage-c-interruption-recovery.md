# C 存储整链：执行环境中断后的可核恢复断点

2026-11-09；作者 /root/coupled_prefix。状态：**作者纯源码/旧存储检查已经真实关闭；C 的最终方法、总清单与独立实际重放尚未关闭。** 本文是按父会话明确授权，在执行环境不可用后通过 GitHub 的小文本接口新建的恢复记录，不是补造一次终端执行，也不是 C 的完成证书。

## 1. 中断事实与范围

系统先报告 exec-server transport disconnected / recovery timeout；随后将执行环境标为 unavailable。一次最小 pwd 探针立即返回 No usable execution environment is available。此后停止执行器探针。

这些事实不提供任何主求解器的退出码，不能判定数值成功、失败、OOM 或其它终止原因。作者不据此改变主线状态。本文没有数值数组、二进制、令牌或其它认证内容；没有修改 HANDOFF、LOG、results 或已有冻结文件。

## 2. A、B 已关闭批次

A 作者清单：notes/2026-11-09-db6f-prefix-storage-foundation-publication.json，SHA256
5600ffe2c1407b44bf42ae605fcbaea956baf1014be7bab7e412a52f4b9ee353。

A 的实际纯检查为155f5b/exit0；旧 M12 的原始 logical gzip/NPZ 字节由四个实际磁盘分片恢复，原数组与原数学表示不变。独审实际48adaf/exit0，独审 publication SHA256
5f3c411d38d1fa156334c72d072b28046a09f524b87890cdc236127a9b57a18b。

B 作者清单：notes/2026-11-09-db6f-prefix-storage-consumers-publication.json，SHA256
0f5fcedacc0d3db60a1fb6559871981fca33477ff90e25b68373993c96e63e45。
实际作者纯源码检查c69564/exit0。B 独审包含独立纯重放b0d47b/exit0和来源/AST检查e2ab4b/exit0，独审 publication SHA256
45d9c6b070b2d6eb4ce4be5085c73c5fb28776868ecde8ee4eb1e6b985f2ceee。

A/B 都没有实际构造新 prefix/common-cut 数学对象，没有运行 BVP/DN/RK/新几何 producer 或连续认证后台。独审完整范围见各自已关闭审稿，不将存储检查冒充未来新图证书。

## 3. C 当前实际冻结源

以下路径均相对于本课题 scripts/。其中终门最终拟用 v3；v1/v2 保留历史，不改原字节。

| 文件 | SHA256 |
|---|---|
| db6f-prefix-angular-metric-storage.py | 2f24cdf9b9649a5ecd34bdbbdabaf294f1fb985288578b54217a6143c98e902c |
| db6f-prefix-export-closed-mesh-storage.py | d776e41ef75741be0d5d44a8156d2c71a70ad016ef3678605d718a32ba7684d1 |
| db6f-prefix-review-closed-mesh-storage.py | 698e8b0528ffa7b1bbe1bc84c574079f60261156f1d3a6ddae048af0f9c0c479 |
| db6f-prefix-terminal-error-storage.py | 809cc7ab61903f11847653fda018506f7c2bed38a7501007909200eb0bf69584 |
| db6f-prefix-terminal-error-storage-v2.py | a00f8210d561983e9d137a848cb7b582e33de8450c0b70497e3933080c297aa1 |
| db6f-prefix-terminal-error-storage-v3.py | 8db94c71a9035f2f977daea9c315b669bce4c20800f80e7886b77c66af6f7ed7 |

完整变换账本位于 notes/：

| 文件 | SHA256 |
|---|---|
| 2026-11-09-db6f-prefix-storage-gates-transformations.json | 0417ac80883dda492618f8535a06ce0eaab230decf0eec4751d2b8c41b25dd88 |
| 2026-11-09-db6f-prefix-storage-terminal-v2-transformations.json | 82bbb53a65803c1f2531a6d2544f82d86f820d458acfeb5494f07f3d7b7f3d69 |
| 2026-11-09-db6f-prefix-storage-terminal-v3-transformations.json | 4299872c6189de869d137682ace26eee965fdabc0af01a2c47a25342bab1e336 |

这些哈希是中断前已真实读取的文件身份；本文自身不能替代那些源的完整字节。若恢复时文件缺失，应从真实已保存副本恢复并核哈希，不能据本文猜写原件或宣称原字节仍存在。

## 4. 新来源门与两次明确修订

原终门的 SOURCES 字典保持原键与原值，继续服务原 tail、background 与固定 M12 reference。新 prefix 来源由独立 PREFIX_SOURCES 和 Files.prefix_source 核验。原 reference、transfer、tail_certificate、scalar_gate、main 等14个函数逐字保留；原数值阈值、覆盖条件与 source-to-exact-target 误差转移均未放宽。

v2 补上真实 base/common 的 fullxyz producer、base mirror、两种 prefix metric 的新 interval backend、moment backend，以及 supplier/geometry/moment/budget/metric 报告的实际 storage closure 门。不能只核存储 helper 而忽略实际 producer 身份。

独审随后真实复现：报告记录旧 checkout 的绝对路径失效时，原 Files.file 的 notes fallback 无法找到 scripts 中的 helper/codec。v3 仅修 prefix_storage_ledger：先核 reported 与 actual 的 basename、非 bool 整数字节数、SHA256 和完整多重集，然后沿 defining base/descriptor 已独立验证的实际本地路径读取。没有扩展原 Files 或 tail/source 路径门。

公共 cut 的数组读取始终针对 defining base；旧 M12 的 base M24 与公共 cut M64 不能混作同一数组 shape。新 chain 不降低原表示阶，也不重新计算 saved jets 或 mean increments。

## 5. 作者实际检查：已关闭与失败历史分开

最终纯检查源：

scripts/db6f-prefix-check-storage-gates-v4.py

SHA256：59c250c55cfe731753f0ee1639728dd4d8b67fca0134e480ebd9f7ca1e55426c。

实际输出：

notes/2026-11-09-db6f-prefix-storage-gates-check-v4.json

SHA256：f1daab8418dd20e722bfabf4688b813dc358300eed323dd04189747f973f380c。

真实启动回执e21d05，session68045；真实完成回执**88ff38/exit0**。报告记录：

- 六份完整声明的源码变换从原件按顺序重放，逐字与 AST 核对相同。
- 34个实际输入；原 SOURCES 和14个原终门函数保持原字节。
- 实际旧 M12 base 的 storage-only 正例及其八项报告路径全部迁移的正例。
- 12个错误身份、缺项、重复项、非法类型或错误字节绑定负例全部拒绝。
- fresh python -I 子进程未导入 NumPy/SciPy。
- 数学对象构造、producer、新几何、网格、BVP/DN/RK 和连续 metric/curvature 后台调用均为0。

这里的存储正例把同一真实旧 base metadata 用于 helper 的两个身份位置，仅支付字节/来源接口；没有制造新的公共 cut metadata 或未来 positive candidate。

保留先前失败：checker-v3 的真实回执33f591/exit1停在文字逆替换计数歧义。新插入的来源字典含相同文件名，使全局逆向 replace 不再唯一；它尚未进入实际 storage 读取。v4 改为从原件严格前向重放已声明变换，没有因此修改数学入口。旧 checker 与失败事实不得删改或称为成功。

## 6. 未付事项与恢复顺序

截至中断：

1. C 的完整方法稿、最终 sources ledger、observed 文件和 closed publication **尚未写完**。
2. 独审 /root/tail_review_continued_2 已全文读 C 核心源、v2 和 v3 修订，并独立复现过路径迁移负例68cd2b/exit0；但在读取 checker-v4 时执行器失联，**独立 v4 重放尚未运行**。作者88ff38不能替代该门。
3. 不应把 C 标为独审 PASS 或把本恢复记录当完整 publication。

恢复后先核所有已冻结字节，再补完整方法/来源/真实观察清单，交独审继续 checker-v4 与标准库旧存储入口重放。只读 source/byte 检查通过也不自动允许数学导出。

真正未来 M14 图仍必须有原 true coupled 的实际成功、自己的 final seam/CP、全图新连续证书和最后独立复算。旧 M12 的 metric、curvature、reach、whole D 或 G5 数值没有因为存储等价而转移给未来图。G5与README完成状态均保持未付。
