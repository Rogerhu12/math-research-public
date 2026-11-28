# R87 两源完整升模的真实工程交接与 λ=.256 启动

本条没有新的数学接受结论。真正接受锚仍为严格径向门下的 $\lambda=.128/M24$，源 run SHA 为 `683d916f31de1406defc42fd7630efdc127aaf093e529ed7ab8b2030c1ec7d9c`。

## 同模态来源合同的实际错误

原连续进程 `14227` 已接受 `.064/M24` 和 `.128/M24`，在准备把两者都升到 M32 时，旧两源 helper 无条件调用了只允许左模态更低的 `same_physical_design`。实际报错为 `This entry requires a genuinely lower-M accepted left source`。真实 owner 已 join，child 与 tool 都返回 1，剩余成员 0；该分支没有启动 `.256` 的 BVP。

独立新 helper 对同 M 的两个真正接受场使用原本更强的 `same_design_contract`，不同 M 则保原交叉模态合同；两个来源仍各自通过 `accepted_original`，目标 M 仍必须严格大于右来源。所有原参数尺度、profile、chart、port、mean、来源和完整字段门保留。旧 helper 与旧控制器没有改写。

## 右来源升模的真实进程中断

该修复后的 `73980` 确实通过来源合同，并完成左 `.064/M24→M32` 的完整 lift：11.199449306 秒，最大 RSS 543676 KiB，102 个原径向样本、3104 个原角点，六 jet 最大误差约 $3.34\times10^{-15}$。其完整输出 SHA 为 `6cea6e62b4e779f586a5dce8ec4d975e8d062ec2c2508d2e3529595745ed6670`。

随后右来源 worker 实际返回 `−9`，stderr 为空。owner 真正 join 的外层返回为 1、剩余成员 0；`.256` BVP/J 均未启动。没有证明中断原因，也没有把它解释为数学失败或据此二分 $\lambda$。

原参考检查已使用径向 16 点分块，但每个 `geo` 会展开到 $16\times3104$ 角点并保留完整核心参数 jet。新的独立入口只把同一旧函数的两个分块位置从 16 改为 2；径向样本集、所有 3104 角点、原六 jet 表达式、$10^{-7}$ 门和之后的完整节点 lift 均不变。不宣称与旧大批浮点结果逐位一致或证明旧中断源于内存。

## 真实恢复及当前原 BVP

已完成的左 lift 通过其原 source/raw/physical/port/mean、源字节、完整网格及输出 SHA 绑定后复用，没有重算左几何。右 lift 实际完成，9.272987659 秒，最大 RSS 544460 KiB；其 101 个原径向样本与 3104 角点全保，六 jet 最大误差为 $3.442139017801326\times10^{-15}$。这个整体峰值观测不证明分块降低了本次进程的总峰值。

两者随后按原完整状态与加性 $\delta$ 做 $\beta=2$ 割线，产生未接受的 $1185\times97$ 节点场、32 个参数及全部原尺度。初猜 SHA 为 `eebe2267f33a00976c8c8a441297b2e088b1da8fc1aa27c26e9d86164a969261`。未把升模检查当成 BVP、metric 或闭合接受。

唯一新 owner `80642` 于 2026-11-28 19:15:28.413 UTC 启动，随后真的进入 `.256/M32` 原 BVP；初始域事件为 `{'event': 'initial_domain_pass', 'elapsed': 13.201524858000084, 'nodes': 1185, 'max_rhs': 14.705217136419245}`。完整 CSR 与全部 QR 因子继续按已核映射路径处理，RHS 分块 8，原 RMS 门 $2\times10^{-7}$、metric 门 $10^{-6}$、physical BC 门 $2\times10^{-9}$ 保持。

新独立 base wrapper 已在这一次真正加载的原 adaptive 模块上安装恰好一次现成 `metric_audit_observer_v2`。它只读这一次原审计已有的误差/FFT/求和数组，记录最大分量、径向位置和原 FFT bin；原 FFT 次数与算术顺序保留，没有额外模型、RHS、J 或旧 audit 重算。本记录时新 audit 与 BVP 尚未返回。

全部实际命令、五个独立新源、两次 owner 终态、已完成左 lift 的复用来源及新右 lift/初猜的小 JSON 见同名记录 `9dc7ee857d1a7afdaff5e502c835d837ced1df0bcc8b772f227cc986add9f7e9`。主链继续 `.256, .512, .75, 1`，最终仍须本题其余完整接受与证明门。
