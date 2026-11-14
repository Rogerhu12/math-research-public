# 原 continuation02 的 ENOSPC 中断与可恢复范围

会话 Astra-visible-flex-db6f0b0e；root 实际观察 tool session17869 返回 exit1，receipt cf4fa6。运行中断是共享文件系统写满，不能据此判原方程不收敛或不存在解。

02 的 call1–9、11–15 已有完整真成功响应；call15 在 s=31/32 达原容差，residual=6.367950627222893e−10、history7。其闭审8件文件在中断后再次逐字节重哈希一致，并已在 main462ff1d5f15902bea9c9d7d6278310795baa9ed8 发布。这是合法的有限 warm，不是真 s=1 或完整前缀。

call16 请求精确 s=1；最后已记录的基点为 iteration2/norm4366.75959636498/minA.12185332299106727，随后接受 step .0625。2026-11-09T15:36:43.537Z 的 worker trace 明确记录 `Error: ENOSPC: no space left on device, write`。call16 的完整响应不存在，最终 reproduction 不存在；旧 progress 虽仍写 RUNNING，实际进程已经退出，不能把该字段当存活证据。iteration gzip可解析也不使它成为成功响应，本次不使用该中间态续算。

controller 的 finally 中写 progress 再遇 ENOSPC；root wrapper 试写执行记录也失败并留下0字节。空间恢复后，root 仅把这个0字节文件改写成真实观察 exit1 的记录；没有虚构 child/worker 的直接退出值，没有改动旧 progress 或失败 trace。源文件及故障输出绑定见 root-amplitude-resume02-observed-execution.json。

恢复计划使用原已审 controller、同一个原配置/目标/source-root，只把新运行编号设为03，以闭成功 call15 为初态，起始 continuation 步取1/64。原 tail max36、tol2e−9、projectionFloor.05、M15/N256/p8/s32/depth12均不变。缩短边值延拓步是数值初值路径选择，不改物理 g，不把 ENOSPC 当线搜索数学失败。03 必须独立得到精确 s=1、原 Jacobian/source audit、真实工具退出；最终前缀准备器也须显式核对03身份，不能冒充02完成。
