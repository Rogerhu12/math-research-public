# 原全局极理想消费者的 R791 旧 ZIP 格式修复

日期：2026-11-16。状态：**首启动的来源读取断言已定位并修复；本次还没有全局表达式输出。**

首 run43787110788/job133037154308，sourcec0387d67eebf240b1c13f2e2300fb21d79bbaad3，
使用 core995a1298defa007a3f0447a91761a0fc1ad4bfe0ff6efc5a0ac99c76c77db59a、
wrapper5f963b478d2fecb0ec2320fc969fea80c635fb19b584eb56cdb5b829ce981237。
它在来源准备阶段报 AssertionError；没有进入新数学 core，也没有 public-actions-input 或数学 stage。
失败 artifact14190916375，1449 bytes /
614ffa3ce7acf3084ee0d8f71c2b4b11d99d27362e14e9c77740e9c9f520deb9，
一日截止2026-11-17 01:36:01 UTC。

真实纯 IO 诊断按冻结八源逐一调用同一 fetch 路径，
前七组 R787/R781/R786/R806/R809/R840/R845 均通过；
R791 在 fetch_direct 的 ZIP 成员集合断言失败。
原 R791 producer 的 manifest 只有9个输出成员，加 manifest 本身共10件，
从未创建较晚格式的 manifest-reference。
先前2709件缓存闭包已过内容/身份核对，但未触及这个新鲜 ZIP 的错误假设。

修复仅对固定 R791 run43686308194、
sourcef945ef5d5aee4d8222dc791e39a0709b661cebbc、
core11068eb00caa71e9c8ed1ffba0277534a52f5cce3402a59b68c7d5d66a8b7a4d、
manifest4eeb9ba12e203f41d2525325bf1ae207b46baa2b88ad88b31de2c3ac58a317fc
及9成员数量允许该准确旧集合；所有其他来源仍须原双manifest结构。
所有文件、来源、配置、SHA 与2709件 expanded fingerprint a2839071 保持不变。
新 wrapper 36428 bytes /
39bef61981f6c2193e64cd1797331a0ce9340ed468fc93dc785d8994c8d2a541；
只另加异常 traceback 输出。数学 core995a1298 不改。

修复后只对最后这组重复来源读取，实际 R791 七个选中成员指纹
31f2340f364fe1d1e559357b941c3672a8c246e2a53618cd08c864600fd290b5 通过，
实际Range826 bytes/3请求，前七组不重复。无数学导入或执行。
新 request f83a2c46ffb0e85f3ae113016e93a96cde9853c196a9a89c06b86495a239f47a 保 resume null，重新触发原公开workflow。
全局五极理想、标准Jacobian、原刚性化及高度的实际状态仍以随后真实输出为准。
