# 原 E20 第二次终止与三个完整逆检查点

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

本记录只封存实际执行身份和已逐文件核验的完整前缀，不将未完成的 constants 阶段改记为完成。

## 1. 实际执行与终止

本次主源为 `notes/2026-11-16-r150-original-low-commutator-twenty-exact-constants-v2-789f.py`，blob `541c14b36925e3cc94018edd8a17a6a765041f5d`，33539 bytes，SHA256 `d9d98bc379e322e9c212b7ad7721399ec8b1bab9970a2755700338f7053d47da`。仅执行 `--through constants --seconds 180 --memory-mib 1024`。独立 observer 保持冻结源 `f8aea7924d8becc10e50303a1c9b36f34d718014`，外墙时为 240 秒，每 10 秒记录存活、RSS、UTC 和 stdout 字节数。

真实开始时间为 `2026-11-16T16:14:25.840692+00:00`，结束时间为 `2026-11-16T16:14:51.355109+00:00`；observer 所测墙时为 **25.513854554010322 秒**。子进程返回 **−9**，shell 等价退出码 **137**。observer 没有请求终止，180 秒数学预算和 240 秒外墙时均未到达。

最终 `RUSAGE_CHILDREN.ru_maxrss` 为 **153892 KiB**；10 秒采样得到的最大 RSS 为 **75932 KiB**。两者口径不同。没有可读的 cgroup 终止原因记录，因此本记录不把 SIGKILL 解释为 OOM，不把最后事件之后的具体函数认定为原因。

## 2. 已完整封存并重新核验的前缀

相位 manifest 为 3418 bytes，SHA256 `c7b010a2c16e2896782eaaad74f977d00e640af6c8142b623474a015b948bf9b`；语义 binding 为 `672c57bb68079e9a49cff09e4a7fdadd7b89dc017927913ee0d35261a08d2522`。manifest 恰含三份候选逆和三份经过完整两侧乘回的逆。六份压缩字节及逻辑字节的完整 SHA 均已独立重读核对。

| 原矩阵 | 精确数域维数 | 完整两侧 E 产品数 | 忠实有理坐标数 | 同一合法 place 的行列式 |
| --- | ---: | ---: | ---: | ---: |
| 原六个 Bell 主列 | 6 | 72 | 216 | 54 |
| 原五个平方系数块 | 5 | 50 | 150 | 44 |
| 原十一条二次来源 | 11 | 242 | 726 | 44 |

三份经过验证的逆共支付 **364 个 E 产品、1092 个有理坐标**。对应候选文件只保留候选身份，不重复算作另一项数学证书。各逆来源矩阵的哈希、label、维数、同一 place 的逆及两侧乘回标志均保存在实际相位中。

后继最窄入口使用的十一维逆为：

- 文件 `original-inverse-11-abb2c7a819cd.json.gz`，1473718 bytes，SHA256 `ec9d6e2758ae835f027fd0c3d8da26945814cb3599949057f96ac542b78300e6`。
- 逻辑内容 2975996 bytes，SHA256 `31bf451e26193eed026feba6bf00a71a9394a78ecce0a7571aea661380b76c05`。
- 原输入矩阵规范哈希 `028c02fb11bb2acc1717b0c7d221edd91a0e1d6ab2fee34c4fe133d7207e89d5`；label 为 `same original eleven quadratic sources`。
- 维数 11，原两侧 E 产品 242，忠实有理坐标 726，同一 place 的两侧逆产品均真。

原来源方向保持为 $U_{j,g}=[m_j]q_g$，$j$ 按原十五个普通二次单项式中被消去的十一项排序，$g$ 为原 $G_0,\ldots,G_{10}$。存储矩阵是 $U^{-1}$，行是来源 $g$，列是被消去单项式 $j$；它不是转置逆，也不是任意有限域坐标的提升。

## 3. 未完成范围与准确下一步

最后实际 stdout 事件是 `original-all-fifteen-quadratic-source-identities`，相对时间 21.983058697005617 秒，报告全部 225 个原二次正常形来源系数已经核验。随后没有 `original-exact-constants` 完整相位，没有精确二十维求解候选，也没有 Python 最终数学 raw。

因此旧 `constants` 阶段仍为未完成。后继若使用上述十一维逆，必须通过独立源、独立 binding 和独立输出目录，逐一核对原来源字典、父 manifest 和唯一已验证相位的完整物理/逻辑 SHA。原 $C$ 的满秩、$R$ 在核上的单射和 $RX=0$ 只能引用已闭的原 E20 来源定理，不能说成这次新算了 $C$ 或 $CZ$。

计划中的新算术只构造 $20\times50$ 投影 $RZ$，用其选定二十列解真实 E 系统，并完整核验 1000 个 E 产品及 400 个选列单位坐标。只有这些新门实际完成后，才报告新的精确因子化数组。

## 4. 执行身份与保留政策

原子执行身份路径为 `notes/r150-original-parameter-module-execution-789f/local-20261116-original-low20-v2-constants180-terminated137.json`，9215 bytes，SHA256 `5f3325e89d9578f344802ad369a297f318fc5b36b2821a8cadfb25218aa3c700`。其中保存所有六份相位描述符和 observer 的真实终止信息。

原 stdout 为 1860 bytes，SHA256 `93f4135bd7f35827acd22a820e2bfea61856255dfe84c820452c7c7c3d028692`；心跳文件为 1216 bytes，SHA256 `b469b0217e05435c7d42faa70eeb986f7f0a8f3e3ac1f76a6dc878c2b62187df`。所有原文件保持不变；数组、候选、raw 和心跳仅留临时计算目录，仓库只保存来源、参数、证明及执行身份与 SHA。
