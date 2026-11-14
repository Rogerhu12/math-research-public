# 后续JSON检查点保留native零符号

2026-11-12，numerical_recovery。针对已实际定位的706个负零丢失，新增独立`fd2d-gc-tail-native-checkpoint.mjs`，不改变任何root、ODE、F/J或接受条件。普通states数组照常写JSON，另保存原byte order、完整states和stage-input SHA，以及所有负零坐标索引。读入带身份的检查点时恢复零符号、核对准确SHA，rawStates从已恢复shared states重建；旧无身份JSON仍按原legacy入口消费。

另名worker-v10在初值、迭代、accepted、完整响应和失败恢复包记录上述身份，warm入口恢复它。v9及已完成05来源保持原样；v10尚无真实DN运行。

用05实际payload及经过原缓存逐字节复现的706项mask作唯一存储检查：编码→JSON→解码后原packed-input SHA仍为aea57a9e0dd527663051693eb3ed68dc8741a67370cb04ac3bfcd5b9643e7366。工具24b190真实exit0，未调用任何numerical root或ODE。完整source SHA和结果在native-json-roundtrip-01.json。

这修复可恢复状态的字节身份，未把IEEE符号零差异写成数学障碍，也未对已闭M8结果新增成功门。
