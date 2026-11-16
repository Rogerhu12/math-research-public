# 原清转置首次启动的整数读取边界与单行修复

日期：2026-11-16。状态：**实际启动错误已定位；未产生新 dual 位或 A.1 结论。**

原公开 run43785814509、job133033100469、source9e4b002127f1a727c7e592e5979e5c4358b381d3 的 prepare 已核1481个原输入；
载体331720235 bytes / fe7c4126e9f3e335f5e70020c05a07c045e149aedf5e0f8ea4af821bcc56b2db。
旧 primal current 未下载，旧逆/CM 数学未重跑。

coref5fff4439fb9f5eff522218f6ef8876ae4fd33d1c344982551081aeef257ebc3 在0.929534089秒退出1。
真实 traceback 是 Job.load_original_coefficients → 原 R781 Field.decode → int(numerator)，
读取原 kappa_power 的4311位整数时触发 Python3.11 默认4300位字符串转换上限。
core receipt 的 configuration、actual_new_dual_digits 均为 null；没有已完成数学 stage。
此错误不是有理重构拒绝、方程不相容或原候选 q 被否定。

修复仅在新 core 的 main 公开 Actions 约束之后加入
`sys.set_int_max_str_digits(0)`。原 R781/R787 在自己的 main 已作此设置，
但作为模块导入时不会运行其 main。新 core 为
59197 bytes / 969201b943bf7591baee92c168546b9992e59b94e1b5b1b2304732b85c052407。
wrapper611e8ad8670f7c2622130638d398e366d5855fe00875ed09c57d2247fa397d23、
全部数学公式、来源、strict RR/full35840 及 Δ 接受条件不变；
resume 仍为 null，因为本次尚无新数学断点。修复后的 request 82de2d032433ae29747258b0f7b7f05564823c2e87c8cad7feac9223ba4a518c 重新触发同一公开 workflow。

实际失败材料来自 artifact14189259689，332472336 bytes /
123ffbeeed23222e2382f871e9c2f20676a39b356c1c8684e2fd004b7355efbd，
有效至2026-11-17 01:22:38 UTC。
原 manifest910 bytes / b7c6b519a2321ef730022f39f9d58f525f9d2369c5c113f7a8a8eb0f0fe6a910，
core receipt e1582a7922ece3414bf2731cbeea9297840ca9f81bc8a51dc49b9e74e70bd1fc。
根仅 Range 读取5个小文件、752985 bytes/11请求并逐SHA核定；未在本地运行数学。
