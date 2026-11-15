# normal4 实际 130 个高自由列的分批精确续接

作者：Astra-ISP-789f / normal_annihilator。  
AI-assisted，GPT-6 Astra Pro。日期：2026-11-15。

## 1. 已成前缀与严格状态

实际 run 为 `43702348535`，步骤为 `selected-natural-second-left-normal-four`，执行源码提交
`49b15114688b66fb31d36bf71dfc6f8e39561bcc`。数学时间为 1.9903180860001157 秒，墙钟为 2.0685019669999747 秒。它完整生成并保存了同一原 $I,J$ 的 $M_4$，核旧 $M'_0$ 及全部旧 36 个右端在 1736 个高行上严格为零。

实际完整 $H_4\in\mathbb Z^{1736\times1485}$ 的模 31 秩为 **1355**，实际所选 $1355$ 阶原单位子式行列式模 31 为 **25**，自由列数为 **130**。旧入口的自设 64 列形状限制因此触发：

`status=completed-prefix`，`outcome=high-nullity-above-bounded-entry`，退出码 75。

没有运行有理高核求解，也没有新第二连接结论。原 $[9,11]$ 秩区间、22 个真头及来源费条件仍沿此前已付结果。

主线实际回执为：

`notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-normal-four.json`。

原临时完整小回执 3442 B，SHA256：
`613c992cef822f11f1f912b4c0eb7c2a12ba2f22ce0e844b14b8faf05305b95f`。

已成原数据身份为：

| 同旧输出目录的相对路径 | 字节数 | SHA256 |
|---|---:|---|
| `high-profile/complete-original-normal-four-block.json.gz` | 910,759 | `c80ca9f374da6ec41410b8dd2a844328176b7c96ca1e0f1364096bb1a51712fa` |
| `high-profile/complete-normal-four-high-unit-profile.json.gz` | 4,852 | `cbeccd17b5bbe1578eb58e0b7b8b990494d85642095c49e1c0277afe9dd9411f` |

共同绑定为 `8b3f9574b5fa816b6f967bc9c9530c6dc991e879f070964d0d409b360ffad781`。

## 2. 新入口准确改变什么

新程序是旧 normal4 完整算法的独立续接版本。它不重构任何 $M_4$ 系数，不重作有限域单位剖面，不重算旧第一 RREF、旧 $HF,T$、旧 36 个精确单位解或旧全原残差。

它锁上述两份完整字节，核原 source labels、1736 行位置、实际秩 1355、实际自由数 130、实际单位行列式 25，然后把相同矩阵数组与原剖面接到新的源码绑定。新的临时 JSON 只增加父绑定/原文件身份并替换运行绑定；所有数学数组保持逐项相同。

本次高自由列形状上限按已经实际观测的 **130** 固定，不使用新的素数或参数扫描。准确选择的 $1355$ 阶单位块记为 $U$，自由列集合记为 $F$。以下五批依次计算：

$$
F[0:32],\quad F[32:64],\quad F[64:96],\quad
F[96:128],\quad F[128:130].
$$

每批仍解原整数单位块对应的有理方程；矩阵和 RHS 同除选中行的共同系数公因子。只要一批 native solve 返回，立即先保存该批完整分子、正分母、原自由列标签、输入身份与 SHA，再开始下一批。时间到可直接读取已完成批次，不重复其右端。native 内部尚未返回的批次不冒称已有可恢复解。

FLINT 的每批 `solve(dixon)` 可能重新形成内部因子；程序不声称共享了未公开的 factorization。这个有限重复是为了保每批实际已返回的解，而不是重算已经完成的 RHS。

## 3. 全部 1736 行仍决定真有理核

原单位剖面只给真实有理可逆块，不决定 $H_4$ 的完整有理秩。完成全部 130 个 RHS 后，对每个自由列形成完整整数图向量 $v_j$，其自由坐标为 $D_j$，主坐标为 $N_j$。再准确计算

$$
S^{\rm high}=H_4[v_1,\ldots,v_{130}]
$$

的全部 1736 行，并核所有原单位行严格为零。取这个**有理**小 Schur 残量的完整核，组合回完整 1485 个 normal4 坐标，逐全部 1736 原行再乘回。

所以如果 $S^{\rm high}$ 的有理秩为 $r_s$，才有

$$
\operatorname{rank}_{\mathbb Q}H_4=1355+r_s,\qquad
k=\dim_{\mathbb Q}\ker H_4=130-r_s.
$$

这里既不预填 $k=2$，也不把 $130$ 个有限域自由方向当作有理核。最终完整原高核、原始单位候选和自由坐标像都只在当前 job 临时目录保存。

## 4. 按实际真高核维数连续接回第二原式

若实际 $k\le64$，本次程序继续原 normal4 后半段：

1. 形成全部 4354 行的 $W=M_4Z_4$，核高行零。
2. 只对实际 $k$ 个新右端使用已经付清的旧 $1546$ 阶 $M'_0$ 单位块。
3. 读取旧 36 个实际有理解和全原残差，追加新列的全 4354 残差。
4. 求精确合并残差核，带所有列分母回原 $x,\eta,t,c$。
5. 核独立 $c$ 投影以及每个候选全部 4354 个原第二产品；保 $E_{\rm old}$、$E_{\rm new}$、$E_4$ 三个真实嵌入。

若 $k=0$，高行迫所有新增 normal4 校正为零，严格继承旧 22 个已经付清的原产品，当前 normal≤4 头空间仍恰为 22。

若实际 $k>64$，本次**先保存完整真有理高核**，然后明确返回

`completed-prefix/actual-high-kernel-needs-wider-next-worker`。

这是下一实际 RHS 形状的边界，不是有理失败或完整第二像的负结论。后继应按这个已算出的真正 $k$ 调整辅助求解入口，不能再重原高块或此前完成的批次。旧辅助 worker 的 64 上限本次不提前扩大。

若后半段完成，仍只有 24 个真实独立头及全部原乘回成功时才可宣布第二连接秩恰为 9；22 或 23 个头仅分别给完整秩区间 $[9,11]$ 或 $[9,10]$，normal5 校正仍可能需要。原条件来源公式和剩余 33/36 维一阶、常核自由度均沿原 normal4 接口保留。

## 5. 源码与准确 CLI

新主程序：

`notes/2026-11-15-r150-selected-natural-second-left-normal-four-continue-789f.py`

- blob：`56780b8c80cf9c522e0b9a873c918a3426385086`；
- 字节数：37,123；
- SHA256：`eabfa9bb969b4e62afbeb21b18f3f662da3606a5bf894790beef55f65c7e278d`。

辅助 worker 不变：

`notes/2026-11-15-r150-selected-left-additional-unit-solve-worker-789f.py`，

blob `1f1aaa60dea2236c001c6439a09248244aae7fd8`，
16,409 B，SHA256
`28928f4298d0689f72ea8d39e530d474c4d15076af1c26aee612a2cb1413982e`。

```text
python -B {scripts}/2026-11-15-r150-selected-natural-second-left-normal-four-continue-789f.py
  --regauged-out {work}/selected-natural-second-left-regauged
  --rebuild-root {work}/selected-natural-u-rebuilt
  --previous-prefix {work}/selected-natural-second-left-normal-four
  --unit-worker {scripts}/2026-11-15-r150-selected-left-additional-unit-solve-worker-789f.py
  --out {work}/selected-natural-second-left-normal-four-continue
  --seconds 300
  --memory-mib 2048
```

新主回执为：

`selected-natural-second-left-normal-four-continue-receipt.json`。

共有 9 个固定主输入：原 normal4 的七个已付输入加本次两份完整原高块/剖面。它们的准确 SHA 全进入新绑定，单位 worker 和新主源码的身份亦入绑定。路径不进入数学绑定；调时不会使已完成批次失效。

## 6. 时限、完整批次和长期保存范围

五批高单位解保存在 `high-kernel/complete-high-unit-batch-000-031.json.gz` 等文件；它们仍是候选，只有随后完整高行乘回才确立对应的高核结论。全部批次完成后，合并候选保存在 `complete-high-unit-rational-candidate.json.gz`，真高核保存在 `complete-original-normal-four-high-kernel.json.gz`。

程序共享 300 秒数学时钟、每进程 2048 MiB；没有新编译、安装或 NumPy 依赖。若有时间限制，回执保最后实际完成批和阶段。时间停止与高核形状停止使用不同 outcome，不能混称。

新程序人工读核已完成；冻结时本地没有做 AST 或数学运行，实际执行面应按原 session 的源码校验流程解析。旧 normal4 源和全部已成文件保持冻结。所有可重算大数组只留本 job 临时，永久提交仅源码、参数、实际 run、SHA 和小回执。
