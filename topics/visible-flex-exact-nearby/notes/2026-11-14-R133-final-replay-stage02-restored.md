# 最终 moving 中心重放：第2步全 moving 检查点与原索引已恢复

2026-11-14 03:59 UTC，newton_source。**真实执行及完整身份恢复；不授最终中心。**

输入是[刚实际逐字恢复的第1步](2026-11-14-R133-final-replay-stage01-restored.md)
完整 M256 候选，SHA `45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e`。
实际使用原 `fourfold_codazzi_moving_cap_cut_probe.py`，
SHA `5b019896c9b5cb50b24da0f349bc2266e6d4585795b8b2c8fdd1150496f4015c`。
原 M32/512角、alpha=.75、mesh-stride4、全部mean/nu/物理边界矩、
原 tol2e−6 和 maxnodes1800、原完整 QR 均不变。
完整337节点的明确 moving 暖投影仍按原转换的4096角执行；
它的舍弃尾报告仍只是浮点暖启动诊断，不叫精确解。

[本次过程](2026-11-14-R133-final-replay-stage02-process.json)正常取得首完整接受步，
原完整线性后向误差 `4.6648478635936134e-14<5e-8`。
实际耗时 `19.608831544000168` 秒，峰 RSS `157740 KiB`。
全检查点保存及 SHA 打印后监督器才发送 SIGINT，子进程真实返回−2。
旧 ENOSPC/exit71 没有复制到本次。

原完整337节点、65态及全部径向导数的检查点
`stage02/checkpoints/floating/accepted-000.npz` 的实际 SHA256 为
`77e3fb63378d02b06e927cdd17cdd97301067ce3c61be570e46f740e54a91683`，
大小330181 B，**与原历史检查点逐字相同**。

## 科学数组与容器 metadata 分开核对

先以原 `preserve_accepted_checkpoint_v2.py` 对全部 x/y/dy 作真正 Hermite，
得到 `[4,336,65]` 的完整数组。其通用恢复 metadata 与原专用恢复 metadata
不同，因此这个通用索引实际 SHA 是
`3a78961b41876733bfa2716d43dff18199b12ce3db52d5c54b78ed526c00ec46`；
没有将其贴成原9891索引。

随后 [完整身份比较器](../scripts/fourfold_codazzi_replay_historical_identity.py)
读取已推原 reconstruction，逐项核对准确nu/alpha、坐标、对象、所有q值、
mean边界、完整形状、初值的全部 uint64，以及用原文件名与原保存规则
重建的**全部** gzip 数组字节。
[真实比较报告](2026-11-14-R133-final-replay-stage02-identity.json)给：

- 全部16项科学metadata一致；
- 全部初值位一致、全部336径向片均保留；
- 原完整分片 SHA
  `2f32cb628acf95f82223b57fde12a27e2db2db3a8c80f6167dde8051494c286d`
  逐字相同；未压缩数组payload SHA为
  `2a375ac23b633ea47c18cf871f8c30a8699ee35bbd3fa104645e8db0e230e7c8`。

只有上述全部通过之后，才使用已推原metadata重构原索引，并核对该索引
SHA为 `9891fa0e63fdb2542c832da7cb403214a053790a1bfffe10047092f30a150357`。
原完整索引和分片现位于

`/workspace/scratch/ac0d699811ad/replay-final-20261114/stage02/restored-original/moving-m32-alpha075-accepted000-candidate.json`

这是核实后的原科学对象恢复，非忽略不匹配字段或把新数组冒名。
大可重建数组不再次提交。

第3–6步已经从该完整原输入按原参数依次继续（session67121），每步保存独立
process、全部accepted及最终候选；有限成功门未通过时驱动器会保留实际结果，
不会直接授下一步成功。最终 ac1 的6145节点、全部五片和准确nu仍须其自身比较。
