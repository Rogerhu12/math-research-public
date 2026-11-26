# 192 角直接缓存暴露的 polar 反参循环及独立稳定消费器

状态：**实际执行记录与数值证据**。未得到完整两网格基线，优化接受仍为 0。原成功、原失败和修正后的输入身份分别保留。

## 原完整组与真实失败

原实际背景适配器 `6a65-geometry-nonfold-polar-background.py` 的 SHA 为
`39adb88c1d7b9aa6c43b8851e20d7d7ff2c48734fca14e68178532a636601cdb`；
准备入口 `6a65-geometry-nonfold-cartesian-prepare.py` 的 SHA 为
`497f7e7220003ec0b80ecb97e170b7e68009dcbab63ec06cefedcaf41e15588a`。
背景是已登记的正高度重分配场，目标度量仍独立取原 zero-parameter/window 定义，没有换成该 polar 场的周长。

- $97\times128$ 组确实完成：缓存子进程和外层进程都自然退出 0，190.906005255 秒，峰值 RSS 205392 KiB。封存组 SHA 为 `a3563170041760c4f065e002da61db2f2d5269023c5344a1bda100facf73da5a`。
- $97\times192$ 组自然退出 **1**，176.153509047 秒，峰值 RSS 205464 KiB。实际只写完前 67 个径向点，下一点失败；没有生成完整组封存，没有 assemble，也没有新完整 baseline。
- 失败位置 $s=.7839285554918939$，左端极角反参。最坏角索引 161，材料角 $u=5.268712679457882$，目标极角 $\theta=5.34631057837065$。原 Newton 第 5 步后已到 $3.9\cdot10^{-13}$，随后在 $u\approx5.008888520089132$ 与 $5.008888520088933$ 之间形成二周期，残差约为 $\pm3.36\cdot10^{-13}$，超过原 $5\cdot10^{-14}$ 门槛。
- 该批实际导数最小约 .454466，未观察到宏观支路跳转。底层 `fd2d_k0_ruling_coast.at_material` 默认以 $2\cdot10^{-13}$ 停止；它比外层门槛粗。这解释了应检查的数值层次，但本次没有把这个解释写成已证明的全域浮点误差界。

完整 15 次迭代诊断实际执行并自然退出 0；诊断文件
`nonfold-inverse-failure-diagnostic01.json` 的 SHA 为
`bb7c6fa67e652e50dad48e58ea6e629aa6d4785667db7fbc9008f18a59109f36`。
原失败日志 SHA 为
`e23ad23932adcec0fd973d0aefedaed2f0f9beda618c304ebb773748fdbc2bb6`。

## 独立稳定反参及完整导数链

`6a65-geometry-nonfold-polar-stable-inverse.py` 对同一端口的周期升支使用
$[\theta-\pi,\theta+\pi]$ 括区，实际核端点残差异号和每次所取导数正性；
Newton 候选离开括区时用二分，并单独保留已达到门槛的角度结果。
原 $5\cdot10^{-14}$ 门槛没有放宽。输出仍由原完整端口和原
`polar_profiles` 隐函数公式产生，位置、一阶及二阶 jets 没有独立投影或拟合。
算法在最多 64 次后仍不达门槛时明确失败，不以一个小括区假装残差通过。
这是有限点消费器，不宣称已经支付全角连续导数正下界。

原失败点的全部 192 角现在实际通过：左端 12 次，最大残差
$4.707345624410664\cdot10^{-14}$；右端 4 次，最大残差
$7.105427357601002\cdot10^{-15}$。实际局部计算 10.898810842 秒，进程自然退出 0。
输出 SHA：
`a37f0eedeef4f9f6ca6e6eaa6bbb4a3bb3b6c1041ebb507227786811001536fa`。

完整两端及方向核对另一次自然退出 0，内部耗时 7.112766179 秒：

| 检查 | 实际结果 |
|---|---:|
| 左端全部六 jets 的最大范数差 | $2.870\cdot10^{-13}$ |
| 右端全部六 jets 的最大范数差 | $2.026\cdot10^{-15}$ |
| $h=10^{-5}$ 的一阶中心差分最大差 | $3.824\cdot10^{-10}$ |
| 同一 $h$ 的二阶中心差分最大差 | $5.668\cdot10^{-9}$ |
| cross 平方恒等式差 | $4.441\cdot10^{-16}$ |

$10^{-4},3\cdot10^{-5},10^{-5}$ 的三档实际差分显示二阶收敛。
这些差值是字面数值消费器的差值；没有把非零端口差说成浮点精确拼接。
数学上的同一准确隐函数/端口定义不变，完整归一化、极角反参的浮点误差证书仍须独立区分。
完整检查输出 SHA：
`6a3802295b03644a35777e9afa0edfa9cb288d0469809f8b6085e2f35a82f655`。

为不让所有原已成功点承担昂贵括区，独立
`6a65-geometry-nonfold-polar-compatible-inverse.py` 先执行最多 8 次原 Newton；
成功时保留原运算与返回值，未达门槛才调用上述稳定路径。
它在同一失败点也已实际自然退出 0，19.860397136 秒，一次原快速路径、
一次括区路径，最大残差仍为 $4.707345624410664\cdot10^{-14}$，全部六 jets 有限。
输出 SHA：
`46e4f00ec81edd8227f0833f7a273b5a47cd41885439a2061cb33bd86a640d52`。

## 新来源身份与继续接口

新 v2 背景和准备入口采用独立 source kind/prepared schema。
原 v1 的成功组和不完整失败组未被改标为 v2。新两组必须真实生成并各自自然退出，
随后才可 assemble 和计算新完整 13+q2 基线。完成本说明时新 v2 的第一组已启动；
本说明不预支其结果。

| 完整源码 | SHA-256 |
|---|---|
| `6a65-geometry-nonfold-polar-stable-inverse.py` | `3ef814b4079fd7a0dd7474d2a10f4e3aebddd81751fb11d00253ad19b5de0e88` |
| `6a65-geometry-nonfold-polar-compatible-inverse.py` | `51bc2153d27f62edb6adfe3a47de0e50e1f6a20a2c583d3be6712c2d8f94b028` |
| `6a65-geometry-nonfold-polar-background-v2.py` | `58e7080d51c0c0a7d584e688c9ec1b995fdffb72c0c0a21eec9a8f23f178c3fd` |
| `6a65-geometry-nonfold-cartesian-prepare-v2.py` | `4e6aaee2178c621e1207f6d5b06d58d075aea1c0566f84c8b506cfd588db0ddd` |

可复生直接缓存命令为
`python PREPARE cache --scripts SCRIPTS --background BACKGROUND --candidate CANDIDATE --target-definition ZERO_DEFINITION --ramp-master RAMP --coast-master COAST --prefix FRESH --group training`，
再另进程用 `--group observer`。v1/v2 用各自对应源码。
zero-definition 文件 SHA 为
`dacede8a21b610d25fae4d0a5c3ffed6896b1693e9fbe7f7538234f970d7689f`，
由已公开 `6a65-geometry-nonfold-target-zero-definition.cjs` 与原公开 candidate/recipe 生成。
ramp/coast 仍分别严格绑定
`0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7` /
`f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d`。
不能把其他机器不同 SHA 的重生 master 自动冒成 R233 原输入。

本次均为本地实际进程，没有借 Actions run 号、旧 Cartesian 计数或旧目标下降。
按根 README 第 15 条只提交源码及本 Markdown 摘要；所有完整报告、数组、失败缓存留临时区。
