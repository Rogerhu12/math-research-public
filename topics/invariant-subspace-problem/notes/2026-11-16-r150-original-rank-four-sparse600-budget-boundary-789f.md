# 原 rank-four 稀疏局部输入：完整预核与首个 600 秒预算边界

作者：Astra-ISP-789f / literature_audit，与 /root。AI-assisted GPT-6 Astra Pro。  
日期：2026-11-16。

## 1. 本次实际结论

独立 Actions run `43883188532`、job `133354233895` 真实重建原模型和压缩来源，随后完成原 rank-four chart 14 的全部输入来源核验、Singular 自测与全部 560 个 SSI 坐标回读。首个 600 秒预算没有得到完整候选基，因而没有目标余式和原来源证书。

数学消费者按约定返回 `75 / budget-checkpoint`。包装器检测到完整候选和验证前缀均未增加，准确停止续跑；外层 job 的 failure 来自请求任务未完成。它不表示算术门失败、MemoryError、目标非成员或局部理想非单位。

本条只记录实际已完成的门与预算范围。原 Bell 单位问题和向特征零的提升均未因此关闭。

## 2. 同一原输入与已核来源

系数域仍为同一合法的 $\mathbf F_{127}$、$d\mapsto100$，全部十二个参数 $y,w$ 均保留。本次使用已付十个原模生成元和五十条原来源，不把初始参数子模称为稳定闭包。

字面 chart 14 取六个原 mean 列中的 $[2,3,4,5]$，在四个二次模坐标上构成 $4\times4$ 矩阵 $A$。令

$$
\delta=\det A.
$$

本次逐一重核全部十五个字面四阶子式及其两侧 adjugate 身份。所选 $\delta$ 有 124 项，其规范多项式 SHA-256 为

~~~text
eff3070880440dd84f3b8d6bcfac5fc71461537d55b9f3d2c323a4287cdde0f6
~~~

程序保留原五十列中的四十六列，仅删除四个二次轴上的 Bell 列。每一条删除都通过字面恒等式

$$
\delta(b-1)e_{6+k}
=
\sum_j \operatorname{adj}(A)_{jk}(b-1)Y_j
-
\sum_i(C\operatorname{adj}(A))_{ik}(b-1)e_i
$$

支付原来源；全部四十个模坐标和四条完整十八生成元乘回实际通过。因此原五十列与四十六列在倒置该 $\delta$ 后生成同一初始子模。这里没有删除其它列，也没有将未计算的稳定关系加入输入。

本次实际通过的原门包括：

- 全部五十条完整原十八生成元来源；
- 原十七梯度的完整 Jacobian 运输；
- 全部十五个两侧 adjugate 检查；
- 四条 Bell 删除的四十坐标和四个原十八生成元产品；
- 原 $10\times46$ 稀疏输入与十个 $(\rho\delta-1)e_i$ 局部器组成的完整 $10\times56$ 输入。

原四十六列共有 315860 项。本次没有物化先前较大的 Schur 矩阵。关于输入构造及成功正门的完整定义，见 [稀疏局部来源接口](2026-11-16-r150-original-rank-four-unexpanded-local-source-interface-789f.md)。

## 3. 实际计算边界

本次固定 Python 3.12.14、python-flint 0.9.0，并真实调用已安装的 Singular。它的三个阶段为：

| 实际阶段 | 耗时（秒） | 返回与已完成证据 |
|---|---:|---|
| 独立局部来源自测 | 0.200583017 | exit 0，完整自测标记 |
| 原局部模 SSI 物化与回读 | 0.801134497 | exit 0，全部 560 坐标相等 |
| 局部候选 slimgb | 583.182706065 | 预算 75；仅有 START 标记 |

最后阶段没有返回完整基，没有保存可重用的完整候选，也没有进入目标降约、target-only lift 或清分母原来源验证。程序未把不完整的内部状态当成来源或基。

完整数学消费者耗时 592.145546676 秒，外层墙钟为 592.395772499 秒。实际父进程峰值为 150240 KiB，子进程峰值为 424732 KiB。这两个数是各进程统计的峰值，不能相加后称为同一时刻的总内存。

严格续跑守卫的旧、新完整前缀签名均为 null。因此本次没有执行空的第二轮，也没有把未完成的内部计算当成进度证书。

## 4. 实际身份与独立只读回核

实际数学源为

~~~text
notes/2026-11-16-r150-original-rank-four-unexpanded-local-source127-v2-789f.py
blob 11f6bf80f1ced7e5a2a21ae0f763ffb7225102d6
35070 bytes
SHA256 ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3
binding 8e701750318d6bed82bd5e202266e025a60da1d23397f2c740badae301ad0bff
~~~

本次完整 raw 回执仅在完成 job 日志和临时审计目录中：

~~~text
19983 bytes
SHA256 b77565d9425d3e4a74b8567ec29873a24724802f0d3d779c39cb02c3bb5a390f
manifest: 18075 bytes
SHA256 3910d03bae2dab9d38244f108da038915dbf88abd3f4c1708da5e94581aecf2c
~~~

已实际发布的运行身份是 [43883188532 的局部候选步骤](r150-original-rank-four-local-source-execution-789f/43883188532-original-rank-four-unexpanded-local-positive600.json)；该身份只保存源码、参数、run 和输出 SHA。其实际终端提交为 `71bdd520ca5427e2b619020d94560f6534f5fcfc`。

独立只读脚本 [完整日志审计](2026-11-16-r150-rank-four600-log-audit-789f.py) 已实际运行：从完成 job 日志恢复生产者原始规范 JSON，重得完整 19983 字节及同一 SHA，另用冻结源和已付 prepare manifest 重算语义 binding，逐核全部上述原门、三个真实阶段和 null→null 的续跑停止。它没有调用 Singular，也没有重新消元。

审计源 blob 为 `73131a5feefe7cc19a6eef7b2f8c3c1d1307946d`，SHA-256 为 `04c122fbda0b63e0124b53df25d37cad7b6007b5dca17522bfbdeeed932f0609`。原数组、SSI、完整回执和审计输出均继续只放临时目录或完成 job 日志。

## 5. 后继的精确范围

本次证明了较小原输入可以完整重建并通过实际引擎预核；它没有给出 $\delta^N$ 的原来源，也没有给出任何非成员结论。后继可消费已经完成的有界原来源消元，对指定 $b\delta e_0$ 或六个 $y_i b\delta e_0$ 作完整 RHS 降约。只有真实零余式和原十、十八、十七坐标乘回才支付相应正证；本次预算不能替代这些门。

## 6. 根的独立全日志复核

根独立读取完成 job 的全部 106139 字节日志（SHA-256 `9ec0c6c34dffcb56576e85e2478be593a7d85fdeccb12bfe3acca777ec98bc26`），按生产者原规范重新构造 19983 字节 raw，得到同一 SHA；另从冻结 v2 源与原 prepare manifest 重算语义 binding。完整原门、三个真实阶段、全部 560 SSI 坐标标记及 null→null 停止均一致。该复核没有调用候选引擎，也没有把预算状态改写成成员性结果。
