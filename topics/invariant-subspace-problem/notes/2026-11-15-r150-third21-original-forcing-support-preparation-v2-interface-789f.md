# 21 个完整第三头的原 forcing 支撑与单位输入准备

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。

状态：v2 小源码冻结。v1 已真实停在输入断言，尚未合成新 RHS；本版不声称已完成新计算。复用已经实际完成的第三秩 3 结果，只准备后继显式 $\lambda_3$ 的真实右端。

## 1. 固定数学对象

已有 22 个真第二 cochain $(L_0,L_1,L_2)$、原第三 forcing $R_3$，以及保存的 $22\times21$ 头投影 $Z$。本轮先实际核 $\operatorname{rank}Z=21$ 和
$$
\operatorname{rank}K_{29}^T[H_F,T,R_3Z]=5.
$$
因此这 21 个头恰为完整第三可延头，不是再筛新的假候选。

逐列合成完整原 $4354$ 坐标的 $R_3Z_j$，取其整数 gcd $g_j>0$（零列取 $g_j=1$），保存
$$
q_j=R_3Z_j/g_j.
$$
这个比例同步用于全部三个低层 cochain：
$$
(L_0,L_1,L_2)Z_j/g_j.
$$
即使 $g_j$ 不整除每个低层来源系数，也只是有理来源代表；本轮不声称它们仍是整数来源。后续统一清分母并核全部原式。每个 $g_j$ 和原 22 头坐标均保存，不仅保存约化右端。

## 2. 实际零行门槛

旧 $M_0$ 有 1546 个纠偏列。保存的 oldZeroRowPositions 是旧第一增广矩阵的 1736 个省略行。它不是 regauged $M_0$ 全部空行的定义。代码实际核这 1736 个位置唯一、合法、当前 $M_0$ 对应行全空，并核旧完整 $[H_F,T]$ 在这些行也全零。另完整统计当前 $M_0$ 的所有空行及额外空行，保存 count、首批原来源标签和全部标签 SHA；额外行继续完整保留在后续 4354 行原残差中。

随后实际检查 21 个 $q_j$ 在这些行上的限制。若限制全零，可以立即生成相同旧单位矩阵的 21 右端输入，后续只求新 21 个 $M_0$ 单位解，并复用既有旧 36 解、normal4 的 130 解及 166 列秩 144 残差系统。

若限制非零，代码保存完整实际高右端和其 Q 核，不推断全局不相容，也不擅自删掉高行。它只说明当前右端不能直接以旧 1736 零行分支处理；后继须实际用 H4/H5 支撑纠正。已证这 21 个头的全局第三可延存在性保持有效。

本轮不求任何 $M_0$ 解，不续高块消元，不重旧 Q 核。

## 3. 固定源码和 CLI

源码 notes/2026-11-15-r150-third21-original-forcing-support-preparation-v2-789f.py：

- blob c98d5649af72bec550ecc93e7e26bfbbdcb7b440；
- 14109 B；
- SHA256 a6bb496eeff96c9a7ca69583f372190e2974e89335b677ea29b5e89c74a2df48。

~~~text
python -B {scripts}/2026-11-15-r150-third21-original-forcing-support-preparation-v2-789f.py
  --regauged-out {work}/selected-natural-second-left-regauged
  --third-out {work}/same-source-koszul29-third-pairing
  --out {work}/third21-forcing-support-preparation-v2
  --seconds 30
  --memory-mib 2048
~~~

建议外墙 60 秒；真实共享数学时间 30 秒、每进程 2 GiB。源码中只允许有限正预算且最高 120 秒，续接可在不改源码的范围内调整真实预算。无需软件安装或 native 编译。

## 4. 固定输入

| 对象 | 字节 | SHA256 |
|---|---:|---|
| 旧 regauged 单位输入 | 9008513 | c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe |
| 实际第三主回执 | 11769 | 954f135c5eab26021fab59aaafd8bd998a232dd2ec02ddcd3204866b93e52ab7 |
| 实际 22 forcing 回执 | 22412 | 59f44ff409f56e420db91f0640b8a6f605e6fbcbf88d7b493f21184741ce5245 |
| 原配对核及 21 头投影 | 45993 | c8e25e15ec3f07e887974adaeff2c573a6391335859bed896a3ca2a6b7af5ae6 |
| 完整原 29×58 配对 | 152226 | 912a777573f261446f87fda25b71fe889963f31cb5a7f34dc192b42045a1af47 |

22 个旧 forcing 文件另外按其完整阶段回执逐文件核 bytes/SHA/binding/原 $J$ 坐标。输入目录可迁移，binding 只含实际源码、输入身份及数学尺寸。

## 5. 输出与完成边界

主回执：
third21-original-forcing-support-and-unit-preparation-receipt.json。

完整临时右端：
complete-third21-original-right-hand-sides.json.gz。

高行真实核：
complete-third21-high-forcing-kernel.json.gz。

仅在全部高行零时另产：
third21-left-m0-unit-input.json.gz。

完成 outcome：

- all21-high-rows-zero-old-unit-input-prepared；
- actual-high-forcing-retained-new-correction-required。

两个完成状态都明确 newM0RightHandSidesSolved=0、explicitNewLambda3SourcesConstructed=false。非零高行只改变后继求解支撑，不能被写成原第三头不存在。

所有大数据只留当前 job 临时目录。永久保存本源码、参数、run、SHA 和小回执，不将完整 21 列数组提交 Git 或 Release。

## 6. v1 实际失败与最小语义修正

v1 在 run43702348535、execution source b73a44af1c5c7735664bfd5b3a7d46769dd3f7d8 的输入阶段实际退出；数学 0.152026088000639 秒、墙钟 0.264470815 秒。失败原回执 1255 B，SHA256 027e5950fab304e9db915444f697b16a129952c0101f0fec34a7a47b85488e52，保持不改。当时固定输入 SHA 全部通过，未合成新 RHS。

确切原因是 v1 将保存的旧省略行集合错误地要求为当前 regauged M0 的全部空行。旧 second pipeline blob 4e0a2cebdf45be98c271bf125796d31b35ae2063 中，这个字段来自第一增广矩阵的 omittedOriginalSourceRows；regauged runner blob 2a9d0e7e4a746c9fe0388d0d5de10e14f919e12b 只核这些行在新 M0 中仍为空，并另外计算完整非空行集合。

v2 恢复这项实际子集语义，继续逐行核其真实性；不删高行门槛，不忽略额外低空行。全部合成、精确高核、原比例和单位输入算法保持不变。
