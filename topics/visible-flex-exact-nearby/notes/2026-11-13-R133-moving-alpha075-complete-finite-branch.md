# R133：moving .75的完整有限成功与原ENOSPC恢复

**有限浮点证据，非连续精确解。** 同一原目标的紧支度量族，使用全部M32 moving角状态、512角内部/物理矩边界、完整mean与ν列，完整QR及原独立FFT相对残差门5e−8、非线性tol2e−6不变。

第一次从原.75 M256所有物理系数换角，显式投影只作warm start；337个径向点上所丢的样本normalized尾最大U2.546e−5/V4.801e−5，原完整源没有当成32模精确解。新系统实际第一Newton步全幅接受，原完整线性残差4.665e−14；新collocation2.944e−11/边界1.311e−14均过。随后自适应加密准备下一因子时真实OSError ENOSPC、exit71，原报告与log保，不改成成功。

原accepted000的337个完整节点、全部状态及全部径向导数已从SHA77e3fb63378d02b06e927cdd17cdd97301067ce3c61be570e46f740e54a91683恢复同一Hermite完整三次中心。恢复本身不授有限成功。

后续78381使用数学相同的完整QR memory存储，输入这个恢复中心；所有原方程/门/参数列不变。实际在459、605、617节点各全幅接受一次，正常exit0，最终finite_BVP_success=true：

| 项目 | 实际浮点值 |
|---|---:|
| α | 3/4 |
| ν的准确binary64有理值 | −19089087034901/562949953421312 |
| 完整径向节点 | 617 |
| 原RMS径向门 | 1.9821679565660413e−6 < 2e−6 |
| 完整有限边界最大残差 | 4.440892098500626e−16 |
| 全U/V Fourier l1采样残差 | 1.131997378665248e−5 / 5.571365778374452e−6 |
| 原物理B/C采样残差 | 8.88022810563366e−6 / 1.6137814848882354e−5 |
| 独立固定physical角残差恒等式差 | 3.10082515897871e−14 |
| 腰真实mean相对−1/a(0)差 | −9.651723864578798e−12 |
| 帽未保留physical样本Robin尾（仅至128） | 2.0741655117540007e−14 |
| 512/1024网保留physical矩差 | 1.5435408306026758e−15 |

全部2465个节点/四分点上的完整3M内部频率都进入诊断。原物理残差通过完整逆坐标微分恢复，另独立固定θ求导比对；没有把φ导数当θ导数。边界只到第128物理模式的样本尾、角梯形差及有限圆网都不是无穷尾/连续舍入证明。帽真非线性B/mean余项仍须消，完整BVP逆和最终闭面几何未完成。

源：`fourfold_codazzi_moving_cap_cut_probe.py`、`fourfold_codazzi_moving_candidate_tools.py`。原initial-process/log、accepted000-reconstruction、memory-resume的process/floating/log/reconstruction均随本文保存。重建清单含所有原完整index/shardhash及输入链；大中间数组不重复入Git。

恢复后的完整finite候选SHA为a6b691234dd671e5d2365007c528f34e428c633c04347d40f10a8a5cec4d0672，当前位于/dev/shm/visible-exact-ac0d699811ad/moving-m32-alpha075-memory-resume-candidate.json。立即从该完整状态向α=.765继续，目标是补足可见性余量；不以本有限成功为收尾。
