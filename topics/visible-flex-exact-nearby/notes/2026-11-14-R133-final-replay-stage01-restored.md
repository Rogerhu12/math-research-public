# 最终 moving 中心重放：第1步原 M256 全检查点与 Hermite 索引已逐字恢复

2026-11-14 03:57 UTC，newton_source。**真实执行完成；不是最终中心或精确曲面证书。**

恢复后的同版本运行环境为 Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0，
python-flint 0.9.0 位于 `/workspace/scratch/ac0d699811ad/runtime-deps`。
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1`。
本次不改原数学方程、全部 M256 角模、2048角网、1379初始径向节点、
参数列、mean、物理非线性边界、QR 的任何元素或原容差。

## 1. 输入和真实执行

按[六步链](2026-11-13-R133-final-moving-replay-chain.json)的第1步，实际运行原
`scripts/fourfold_codazzi_reciprocal_branch_refine_probe.py`，SHA256
`331b68f1c11fe625c267620e983786cb5f0f388731b8782e64cd372ee17d1232`。
已推 M128 起点索引 SHA256
`e19344f7f1fecb96f6871315de7e22fee1ad9ca58f34953b4672f05f5a3326ed`，
五个 gzip 的全部 SHA 与原链逐个一致。
准确对象及 origin/direction 三份输入亦按加载器核对原 SHA。

本次只改变输出、QR 缓存、检查点路径及执行资源：AS 上限4096 MiB，
这个限额是地址空间，不是 RSS。完整原命令及观察见
[本次过程记录](2026-11-14-R133-final-replay-stage01-process.json)。
独立监督器 [source](../scripts/fourfold_codazzi_final_replay_first_accept.py)
等待原 producer 已保存全部 `radial_nodes/state/radial_derivative/metadata`，
并打印完整检查点的 SHA 后才发送 SIGINT。没有在未写完的数据中间取快照。

实际两次原完整 FFT 后向误差为

- `1.6868307088282434e-12`；
- `2.929938852328282e-11`。

两者均通过原 `5e-8` 门。全部1378个 QR 块和全部参数/边界列均保留。
原接受门实际接受完整1步，步长1。过程实际耗时 `742.2506468939998` 秒，
观察到的子进程峰值 RSS 为 `1212876 KiB`。
在成功保存后，监督器发送 SIGINT；子进程本次真实返回码为 **−2**。
监督器自身正常结束。没有复制历史 exit137，也没有把有意停止写成数学失败。

## 2. 完整原检查点及真正 Hermite

完整检查点实际路径：

`/workspace/scratch/ac0d699811ad/replay-final-20261114/stage01/checkpoints/floating/accepted-000.npz`

大小 `10916086 B`，1379个径向节点、513维全状态及全部径向导数。
其实际 SHA256 是
`af0a3f5fabd4d8d1194f30ff942130040e62975c0963f127c9ae864f7bd9521a`，
**与原历史完整检查点逐字相同**。

随后实际执行原
`scripts/fourfold_codazzi_preserve_accepted_checkpoint_v2.py`
（SHA `e7d7e33ea74457baab55e7620aa4a52353fd7941edd11f79a238729e530b90c2`），
使用完整 SciPy `create_spline(y,dy,x,np.diff(x))`，没有截节点、只取首向量、
重设mean或外推。见[本次 Hermite 记录](2026-11-14-R133-final-replay-stage01-Hermite.json)。
全部三次系数形状 `[4,1378,513]`，其完整九片索引位于

`/workspace/scratch/ac0d699811ad/replay-final-20261114/stage01/reciprocal-m256-alpha075-accepted000-candidate.json`

实际索引 SHA256
`45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e`，
**也与原完整 M256 候选逐字相同**。这比“浮点库版本相同”或“数值近似”强，
核对的是原全科学数组及其容器字节。

这些大数组可由已推起点、原源、完整参数和本记录重建，依根规矩11只保留于
上述本地独立路径，不再次提交。原历史进程记录和错误未更改。

## 3. 接续范围

第2步已用这个真正完整输入启动为 session63273，独立路径
`/workspace/scratch/ac0d699811ad/replay-final-20261114/stage02`。
本文不凭第1步授最终 ac1 中心、后验界或有限 BVP 收敛。
第2步之后必须继续原链的 moving 转换、.75全解、.765延续、收紧和 fullR。
它们的实际身份另行记录，不能从本检查点推断。
