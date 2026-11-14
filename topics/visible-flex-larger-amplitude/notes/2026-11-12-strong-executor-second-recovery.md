# 第二次执行器丢失后的强分支恢复

## 范围与状态

本记录仅恢复源文本、已观察到的退出状态和可重做配方。它不重建丢失的
数值数组。新工作树从 main `95189144e667089085b8603b78822f88b92166c6`
接续；根和课题 README 的核读/发布由 root 统一管理。本文不改变课题完成门。

原 session98619 已观察到初始完整 H 的已审计响应复用，并且没有启动 Node。
随后因与 exact90734 的独占窗口交接，向自有98619发出 Ctrl-C；工具返回
执行器传输恢复超时。没有观察到 Ctrl-C 送达、正式退出码或已接受的 prefix
Newton 步。故98619终态仍未知，不能写成正常调度中止、成功或数学失败。
当前环境中旧工作目录及其未推结果不可访问。

## 已精确恢复的文本

四个独立脚本由会话保全的完整原文恢复；先做内存 SHA256，再在新文件系统
逐件计算 SHA256，结果与旧记录完全相同。Python AST 全部通过。

| 文件 | bytes | SHA256 |
|---|---:|---|
| computations/strong_actual_same_height_tail.py | 11041 | ef8ffa1ceaa813d3a04f3551c3b44111d0e0af2d60953a750e7ec25e46a72ea3 |
| computations/strong_actual_recorded_tail_port.py | 14744 | 7fc687bd4608f5656140dc19abebccfb66074684c46651513efe68818ec311f0 |
| computations/strong_actual_recorded_tail_check.py | 9534 | e009628fe6a94f8537a6513c6a017e18948c4f9024b94c8dfe7660b627548f5d |
| computations/strong_actual_prefix_geometry.py | 7231 | 530a786d65cae809fb38c07f13203b51f7ca36f6e94897c967225e19934e628d |

生产入口 `computations/strong_actual_three_control_bvp.py` 从已发布的87bb版本
重放8处严格唯一的文本替换，得到40199 bytes、SHA256
`a84c8587c8ed605fdc0627c1183d79ff0afaa26d21f2b78e00c7091fa5ba6da4`。
旧基底保存在 `2026-11-12-strong-actual-q105-r2-entry-source.py.gz`，
解压SHA为 `87bb5063e3b0580701cfa2589d1b6eb495fc7a83fb226944e6df3f1c2ce685da`。
完整替换表和统一diff另存，实际逐件重放核对已通过。第一次文本恢复脚本只在
完成所有写入后的打印语句上遇到str/bytes类型错误；后续只读重放核实确认文件
完整。这不是数值计算失败。

## 丢失结果与可用暖点

- session30348正式exit1。首尾已接受试步norm=5.560497277748043e-11，随后
  最终完整Jac复查前worker=-9，原因未知；没有prefix Newton。其完整577×48
  状态、9个raw节点、全部24H已推送。
- session51033正式exit1，原条件同H恢复仍在首完整Jac前worker=-9，原因未知。
- session66750是独立入口的确定实现检查失败：把M20校准ready的modes与实际M24
  比较。worker正常exit0，没有求解请求。现行ef8版本改为从接受的实际M24包
  取完整参数身份；旧M20 ready仍只供原冻结校准/物理指纹核对。
- session29674独立同H完整Jac及audit正式exit0、worker0，真实残差
  3.2267755969289545e-10，wall456.5526793003082s、peak436104KiB。
  原成功packet SHA为7a4c1c2c5390dd997fcef71c58c3e483f31cecd06ce240863c44d929ad1951de，
  ready SHA为3ab4396baa55cbafdb50064a30affbc7ad9913e20725305db95f7087db62a9fa。
  **这两个数值文件未推且已丢失，必须真实重做。** 仅保存摘要和原哈希不能
  当作可复用响应。
- session7181的无Node协议核对正式exit0、10项通过；wall4.926039934158325s、
  peak36428KiB。原输出也丢失；新真尾响应完成后重新核对。

可直接读取的已推暖点：
`2026-11-12-strong-actual-q105-freeq4-m24-tol7-r1-tail-iteration.json.gz`，
SHA256 `9bfe41493d962208f9ede593f95b64a3393dc8c39afb76616640e877b92b7346`。
它是iteration-recovery-only，旧小残差没有绕过完整Jac/audit。重载时依旧执行
原Q/L几何重网格与ratio=1暖变换，状态本身不承诺逐位不变；完整请求H及数学
配置要求严格相同。

## 资源模式不改变数学验收

恢复入口默认不启用新行为。显式传入已审计packet/ready时，只有完整H、源
SHA、全部方程配置、Jacobian与audit身份通过才能复用。任一H分量改变（含1 ULP）
都调用原live求解。响应存盘后可显式关闭worker，再把控制交回prefix全Jac；
下一真实请求以已记录完整响应暖启动。每个真实新H均做完整audit，最终同H
审计可以复用该包，记录 `reused_already_audited_packet` 与
`source_packet_sha`，不称重新计算的独立audit。

三控制目标仍为实际c2=.105、c4=-.006655700963004517、
c6=-.0004116733380408847；表示gauge=.09。M24/N768、tol1e-7、max2400，
原真实尾M24/N512/depth8/steps12/parts8/tol2e-9与physicalBC1e-10保持。
释放worker仅改变资源生存期和I/O暖启动，不改变原方程或收敛门。

## 重做顺序

精确独立命令见同前缀的 `-rerun-plan.json`。先验证标准库prepare与已推暖点
SHA，在固定91源全部恢复之后运行fresh sameH fullJac/audit。然后用旧q095
与新q105-H两个真实已审计包重做无Node协议核对，再运行fresh q105实际三控制
BVP并保存每个接受内层恢复点。成功后做完整物理几何审计；当前尚无q105
新前缀解，更没有完整闭面、reach或大幅完成声明。
