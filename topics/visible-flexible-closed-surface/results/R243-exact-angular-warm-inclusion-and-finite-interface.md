# R243：同一固定几何的角频暖启动、精确嵌入与实际有限接口核

**本条完成的是零误差的有限空间嵌入证明、可执行消费者和一次真实非零接口核。尚未执行原 M12 的 M48 暖续，未新增其非线性接受，未据此支付 README 第 5 条。**

## 1. 同一场的精确嵌入

保持原 M12 的材料图、固定 $g$、整个中央到真平 cuff 的物理范围、径向节点和 Gauss 规则。原校正场写成

$$
W(z,\theta)=\left(\operatorname{Re}\sum_{i,m}B_i(z)c_{im}e^{im\theta},\ \operatorname{Im}\sum_{i,m}B_i(z)c_{im}e^{im\theta},\ \sum_{i,n}B_i(z)h_{in}\cos(n\theta)\right),
$$

其中 $m=3k+1$，$-M\le k\le M$；$n=3j$，$0\le j\le M$；全部系数为实数。径向 quintic 基省去两端各三个控制列，因此两端的完整位置、一阶和二阶迹为零。

从 $M$ 增到 $M'>M$，保留每个旧模式的相同 binary64 系数，将新增模式的系数置为精确零，且径向 knots 逐字不变。两式的每个非零项于是完全一致，所以新旧 $W$ 作为连续函数严格相同；高阶原生偏导在其存在处相同，特别是全域完整两 jet 相同。固定材料坐标变换保持不变，故物理 $s$、材料 $u$ 的完整六 jet 误差同样严格为零。这一步没有有理数转浮点的舍入，因为它只复制已经给定的 binary64 数。

同样由模式集合直接得到 $W_{xy}(z,\theta+2\pi/3)=e^{2\pi i/3}W_{xy}(z,\theta)$，高度不变；实系数给出 $x,z$ 对 $\theta\mapsto-\theta$ 偶、$y$ 奇。三重旋转、环境反射和端部两 jet 因而原样保留。此结论只说明暖初场与旧场相同，未替代后继新场的连续几何验证。

`frequency-only-grid-prepare.py` 实际核旧/新角网格的包含关系，逐字复制旧精确径向 query recipe，保留全部祖先观察点和同一径向网格。`frequency-only-warm-transfer.py` 核验旧 result/field/grid 的 SHA、完整模式和系数维数，再执行上述零填充。原源本身的材料角变换并非有限 Fourier 多项式，所以增到 M48 不宣称已完整表示原源的全部角频。

## 2. 暖续保持原目标

新 `entire-half-cartesian-warm-refinement.py` 从实际转移出的完整系数开始，不重置为零。完整三行 Gram 残差、全部列与跨角通道耦合、所有内部自由接口、中央与真 cuff 的完整端迹沿用原 whole-half 供应器；没有加入 $\lambda$ 正则。每个试步仍须同时满足完整加权能量严格下降和训练峰值不超过前态的 1.05 倍。

设原 H1 预条件器为 $T=L_S^{-T}$，物理线性化为 $J$。LSMR 实际解 $\min_y\|JT y+r\|^2$。新诊断先直接计算

$$
q=T^TJ^T(r+JT y),\qquad J^T(r+JT y)=L_Sq.
$$

后一个等式由 $T^T=L_S^{-1}$ 直接得到。代码从保存的真实 lower band 相乘恢复物理梯度，记录其绝对范数以及相对初始 $\|J^Tr\|$ 的比值；同时保留 LSMR stop code、normA、normAr 和实际 slope。达到迭代上限不会被改写成收敛。

独立加密观察分别计算零参考、实际暖初场和新场，并保存暖初场的真实观察收据，允许后继微窗和祖先观察器消费同一初场。所有新场的 R226、全时间几何、R236 和三相位 STL 仍须在同一实际 job 中重新执行；本条没有预支它们。

## 3. 冻结源码

| 文件（位于 scripts/） | 字节 | SHA-256 |
|---|---:|---|
| `6a65-m12-frequency-only-grid-prepare.py` | 4182 | `53fc97c81e3fd4e4e9a7133fee62560016e34cd3af7a81a801464c1e44ca02e0` |
| `6a65-m12-frequency-only-warm-transfer.py` | 6026 | `0467d7f4f29266fcbfaf077c23928c6d91114e24fb6de847fc1320900d96fb00` |
| `6a65-m12-entire-half-cartesian-warm-refinement.py` | 25118 | `e58d4f3c036a1ec4b78a3c7022ac6e6677e9b7bac4c3be8eea43ed8665a2ae81` |
| `6a65-m12-frequency-warm-finite-fixture.py` | 8762 | `6008812ae985de806a9f030bac158896ae2fcd5e591156136c7409f511850ef6` |

原 whole-half 源 `6a65-m12-entire-half-cartesian-bvp.py` 的 SHA-256 仍为 `7214054f65bfbd1055122dddf235074bc812c88cdf5d418b630877bf8b21880b`。新暖续是另一个明示的源码身份，没有覆盖该旧源。

## 4. 本次实际执行

环境为 Python 3.12、NumPy 2.3.5、SciPy 1.17.0。上表四份数学源码的编译检查实际 exit 0。有限核复现命令为

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/6a65-m12-frequency-warm-finite-fixture.py --scripts scripts --out /tmp/m12-frequency-interface-check.json
```

实际执行使用 `/tmp/visible-flex-6a65e705/exact-work/angular-warm/scripts/` 下的同名字节，输出 `frequency-interface-finite-check.json`。输入是 seed `202611261421` 产生的 66 个非零系数，6 个自由径向基、11 个旧角通道，M3→M5 后为 17 个角通道。它是明确的合成接口核，不是原 M12 场。

| 实际核查量 | 返回 |
|---|---:|
| 旧系数字节完全保留；新增通道精确为零 | true / true |
| 独立 SciPy 径向基加直接三角求值的全部六 jet 最大差 | 全部 0 |
| 两端位置、一阶、二阶迹误差 | 全部 0 |
| 独立 dense 三角解与生产物理梯度恢复的相对差 | 1.0909641775140654e-16 |
| 两个真实 grid/transfer CLI | exit 0 / exit 0 |
| 完整 warm reader、精确 query 字节及祖先角/径观察点 | 全部通过 |
| 修后有限核内部时间 / 实际进程返回 | 0.3616792270040605 秒 / exit 0 |

首轮有限核实际 exit 1，原因是 NumPy 2.3.5 的 `count_nonzero(...)==0` 返回 NumPy bool，报告 JSON 序列化拒绝该对象。已经显式转换为 Python bool，随后在上表新 fixture SHA 下完整重跑成功；没有把首次失败伪记为成功。其余三个数学源 SHA 未变。

本次真实临时标量回执文件为 `frequency-interface-finite-check.json`，不提交其可重算 JSON；它有 1532 字节，SHA-256 `499de16b7ecea7bc8a81540c5579154a95b3f9fa0b912aef10ade1c50a9f383d`。回执含计时，重跑应登记自己的真实 SHA。

后继原 M12 运行的预定变化仅为在 h487 同一径向空间、G6、同一精确 query 上从 M32/N384 增到 M48/N768，独立角观察为 1536。后继不假设能够访问先前 runner 的 raw，而是必须同 job 先重生 h487，再消费该 job 的实际场。重生本身不计新的数学下降；能否消除当前剩余完整残差，只能由后继真实输出判断。
