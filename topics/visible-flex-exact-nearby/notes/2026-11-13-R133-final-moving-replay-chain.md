# 最终 moving 主体的完整重放链与实际可用性

2026-11-13 23:23 UTC。**这是已核清的恢复入口；本次环境失效后尚未执行新的重放。**
每个原命令、源SHA、完整候选身份和已推M128五片清单保存于
[机器可读清单](2026-11-13-R133-final-moving-replay-chain.json)。

## 1. 先分清已保存的对象

最终ac1d5b98…的
[重构manifest](2026-11-13-R133-moving-m32-alpha0765-fullR-v2-tol2e9-reconstruction.json)
含完整索引、6145节点/M32的元数据、五片原SHA、参数与原过程入口。
它**不含五片数组字节**。已核对f63e7809749f2804e99667464dbb2114d6353acf的提交文件清单：
这些大分片依根规矩11只留在原本地，是可重建中间，未随提交上传。
原候选位于
`/dev/shm/visible-exact-ac0d699811ad/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json`。
先尝试在实际恢复的同一环境找回它和所有五片；只恢复索引不足以运行消费者。

可从仓库取回的完整数组起点是
`notes/2026-11-13-R133-reciprocal-m128-alpha075-full-QR-candidate.json`
及它指向的五个gzip分片。它保留全1379节点和257维状态；原有限求解到达最大节点数，
故是完整候选而非已收敛BVP。既有后续暖启动允许使用该真实全候选。
二进制由正常Git/实际运行环境取回，不能经当前仅小文本的API输送或编码分块。

## 2. 必须保持的六步实际链

|步|原过程（共同前缀 `notes/2026-11-13-R133-`）|必须保留的对象|
|---|---|---|
|1|`reciprocal-m256-alpha075-checkpointed-QR-process.json`|原M128全状态→M256，取首个完整accepted-000及全部径向导数|
|2|`moving-m32-alpha075-initial-process.json`|从完整M256作明确moving暖投影；M32/512角/mesh-stride4，取首个完整accepted-000|
|3|`moving-m32-alpha075-memory-resume-process.json`|从完整moving .75 accepted节点Hermite继续，tol2e−6，maxnodes1800，memory QR|
|4|`moving-m32-alpha0765-memory-process.json`|完整.75→.765，tol2e−6，maxnodes2000，memory QR|
|5|`moving-m32-alpha0765-tol2e9-process.json`|同.765收紧至tol2e−9，maxnodes6500，file QR；真实cut1.5完整主体|
|6|`moving-m32-alpha0765-fullR-v2-tol2e9-process.json`|明确稳定帽暖延伸后重解整个[0,25/8]，tol2e−9，maxnodes9000；不外推原PPoly|

机器清单逐字保留每步 `producer_arguments`，不要凭此表重拼遗漏参数的命令。
最后一步使用真正的
`scripts/fourfold_codazzi_moving_regular_endpoint_probe.py`，
其原SHA为
`3c170b9c9d2b34655107dba54b189c6a940d9f62901a61d0a3ccc5a5b398e996`；
不得切回旧cut1.5 producer代替fullR。

首步原accepted SHA为
`af0a3f5fabd4d8d1194f30ff942130040e62975c0963f127c9ae864f7bd9521a`，
完整M256 Hermite候选SHA为
`45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e`。
第二步原accepted SHA为
`77e3fb63378d02b06e927cdd17cdd97301067ce3c61be570e46f740e54a91683`，
完整moving accepted候选SHA为
`9891fa0e63fdb2542c832da7cb403214a053790a1bfffe10047092f30a150357`。
其全部元数据在
`notes/2026-11-13-R133-moving-m32-alpha075-accepted000-reconstruction.json`，
不得只复制第一个状态向量、截径向节点或重设mean。

准确节点插值是原SciPy BVP的
`create_spline(y,dy,x,np.diff(x))`，必须用**全部**已接受状态和导数。
`scripts/fourfold_codazzi_preserve_accepted_checkpoint_v2.py`实现全状态保存；
它的报告元数据与原特定恢复器可能不同，因此科学数组一致、容器字节一致
和旧native可直接消费是三个要分别核对的条件。
原源版本由过程SHA及Git历史定位；若当前源码已变，应在隔离路径使用原源，
不得把main回滚或更改原记录。

## 3. 新尝试的可核验记录

原第一步进程82459有真实exit137而原因未知；第二步曾有真实ENOSPC/exit71。
这些是历史观察，**不得复制给新尝试**。新的暂停、退出或失败按实际工具返回记载。
若只需要accepted-000，可在完整原子检查点出现后正常保存并停止后续无用迭代；
这是新的资源执行策略，不冒称重现原退出事件。

为新尝试使用独立输出、checkpoint、QR临时路径。仅替换路径或明确停止点；
数学方程、输入全部系数、角模、网格策略、收敛阈值、完整FFT/Jacobi门不改。
原资源只分配RLIMIT_AS并不说明RSS或失败原因；在恢复环境选择足够资源并记录真实用量。

每步核对原完整meta、候选索引和所有分片SHA。尤其最终必须核对真实
`[0,25/8]`、M32、α的准确有理数
`6890507429876859/9007199254740992`、ν的准确有理数
`-2572625729470897/72057594037927936`、全部6145节点及全部PPoly系数。
浮点库版本或重放舍入若使任一科学数组不同，它就是**新中心**；
不能强行贴ac1d身份，不能把旧原生后验直接迁移。应保存新身份并重新完成
该中心全部连续残差、端口、根块、能量和几何消费者。

## 4. 未推原生结果及接续顺序

最终actualR源已准确恢复，原正常运行39823/12.349s是真的，原native未上传；
按它的原CLI在完整同中心重新运行。新27门fold/Airy consumer只需已推的
`2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz`
和
`2026-11-13-R133-universal-two-port-Airy-v2-native.json.gz`；
不需要先恢复大候选，实际环境恢复后可先重算这一小消费者。

7296闭单元的唯一远程完整前缀是first8；原912行只在失联本地。
找回本地行先按源SHA/候选SHA/分片/位宽/参数/节点身份验证再续，不重复已成行。
找不到则从原producer真实重算余行。最终合并还必须覆盖全部真实PPoly jumps，
且半宽0的η=0报告不能改写成整个η区间。

2026-11-13恢复workflow的run43522044960/job132218484789在runner前失败，
无steps或日志，**没有执行27门或任何重放**。原因未知。
当前继续完成完整逆与几何消费者证明，等实际执行环境恢复后即接上述工作；
本清单不把待执行工作记为已完成。
