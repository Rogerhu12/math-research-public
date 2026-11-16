# 固定 Python 后的三步实跑：完整模块自测通过，600 秒候选未返回

作者：Astra-ISP-789f / normal_annihilator；AI-assisted GPT-6 Astra Pro。

## 1. 真实作业和输入身份

run `43878449638`、job `133337613806` 已实际结束。工作流为 `invariant-subspace-r150-original-parameter-module-session.yml`，触发 head 为 `a89838eb1776dd04aa0dc5babd770478cc84178a`。实际 Python 为 `3.12.14 (main, Aug 13 2026, 02:45:55) [GCC 15.2.0]`，python-flint 为 `0.9.0`。

原三项数学源码及输入 pin 均未改变。第一步实际重新得到原父 manifest 的 30466 bytes 与 SHA

~~~text
9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2
~~~

第二步严格通过该原物理文件门，完成原 116→50 压缩。由此，上一 run `43876083196` 的 Python gzip header 差异已由固定运行时后的真实完整重建解决，没有改写旧数据或放宽 SHA。

| 步骤 | 执行源码提交 | exit | wrapper wall 秒 | 完整临时 raw bytes / SHA-256 |
|---|---|---:|---:|---|
| 原十行及 116 种子 | `50eedb65c4edc707e8566e8e5f0bbe936b05b0fd` | 0 | 22.670792453000004 | 30924 / `5f7cd8f2caddb695bcca394cb8a9d582290e978b80d56ff761a43d5f541dd7fe` |
| 原 116→50 压缩 | `466876331d3da924155a9873538eddfd0a4deb85` | 0 | 43.271609384 | 4214 / `5043379c6fe0b4af67d900f7066270854e968ea86cd6faa0a99c820a8d492a32` |
| 五十列候选正门 | `9374e61150db974448d99dcfdfad96949769cd7b` | 75 | 592.3023985030001 | 34846 / `ae429213e7c756aed85b3c1e638174c32a63338f5f0e85a5179a19393fbf8a68` |

三份已实际发布的执行身份位于 `notes/r150-original-parameter-module-execution-789f/` 下：

- `43878449638-original-ten-parameter-model116-180.json`，Git blob `e6dba1c822698d2431ed2359ab4de2f1c7bdeb1e`；
- `43878449638-original-parameter-seed-compression50-180.json`，Git blob `beec7267e2b97915e7a98e965f2c493238e4e649`；
- `43878449638-original-compressed-parameter-module-positive600.json`，Git blob `16279f457dc16636d91109ef2bf9358b87c76d6f`。

本代理已完整读取完成 job 日志，并恢复三份原 raw 的 canonical JSON 类型与源码身份，所得字节数和完整 SHA 分别与该次实际 job 上表三项精确一致。所有 raw 仅保存在临时目录。

## 2. 已实际通过的数学和软件入口

第一步全部 116 原种子、50 原边界、11 原生成元、六均值、34 坐标逆、578 Jacobian 与 17 原梯度运输门均为真。

第二步完成全部 1160 原参数坐标及删除种子的完整原十八生成元乘回。实际保留六均值、二十条权六交换子、十四条权八交换子及十条 Bell 列，共 50 列；同完整有限域参数子模的等价门为真。

第三步先重新核全部五十条完整原十八来源和全部十七梯度运输。实际参数维数仍为十二，模行数为十，向量项数为 315888，来源项数为 65853；没有参数点代入。

实际 Singular 版本首行为：

~~~text
Singular for x86_64-Linux version 4.4.1 (44105, 64 bit) Dec  6 2025 11:10:58
~~~

其可执行文件 bytes 为 18736，SHA 为 `eedadb4f1ad9a6bfbf599a0785cb2b1906445ef7c5133de0215c653d534d923e`。完整版本文本 SHA 为 `06b66f07ff183a8b849ce21145600f1c6a7f76b54de830e0be94abf763ff685c`。

独立模块自测实际通过，耗时 `0.20057688200000712` 秒。它覆盖模块 `slimgb` 的正对照与负对照、完整 SSI 往返、`lift(Original,Target,U,"slimgb")` 的 $U=I$、完整两坐标原乘回以及独立 FLINT 多项式解析和乘回。其完整日志仅有开始与完成标记，未出现错误标记。

随后完整原 $10\times50$ 模块 SSI 写入和读回的全部 500 坐标也实际通过，耗时 `0.8011399570000037` 秒。该 SSI bytes 为 9210907，SHA 为 `e057aba1d876f1018450e73e20ee3a7b7db5cac569f94ed9f5c2fa030e2ded28`。

这些是实际通过的接口与来源门；并非依据文档推测 Singular 支持某项功能。

## 3. 实际停止位置与没有得到的对象

第三步总 elapsed 为 `592.055255068` 秒；原 `slimgb` 阶段实际运行 `584.998632592` 秒后因预算退出。该阶段完整日志为 32 bytes，SHA 为

~~~text
afb8960fe4001df08d76c8606a8e0e5dd267b4fd01886c47b283341aeafa2844
~~~

唯一标记是：

~~~text
@@PARAMETER-MODULE-SLIMGB-START
~~~

没有返回标记，没有完成 candidate SSI，也没有候选来源、目标约化或已解析来源文本。最终 manifest generation 为 3，只保留已完成的 ASCII 原模块、实际引擎、独立自测与原模块 SSI；candidate 字段不存在。最终 manifest 为 17687 bytes，SHA

~~~text
4116161f526db0dad03a8b1dc61d27c68d9df02e77680b3143662da147835fe2
~~~

实际父进程峰值为 148744 KiB，子进程峰值为 350720 KiB。本次是 600 秒预算范围内未返回完整候选，不是 `MemoryError`、语法错误或原乘回错误。

wrapper 在 `13:54:45 UTC` 实际记录 `previousSignature=null`、`actualSignature=null`，按冻结规则停止，不启动预设的 1200/1800 秒尝试。整个 job 因所请求正门尚未完成而标为 failure；数学子步骤的真实状态仍是 exit 75 / `budget-checkpoint`。

因此本次没有得到 $e_0$ 的来源、没有特征零提升、没有 Bell 自然幂正证，也没有非成员或稳定闭包负结论。不存在可以声称已保存并接续的 `slimgb` 内部计算前缀。

## 4. 下一条有实际来源的边界

保留上述真实完成门与失败身份，不对同一五十列从零空续。后继只能采用新的、逐原来源核验的输入或不同的受控局部图。已独立实成的三十条 $N_iY_j$ 来源及完整权七秩 312 是一种新的来源接口；其相对所选前缀的独立性仍不能代替相对整个参数子模的新增性或稳定性证明。

所有多项式数组、SSI、raw 与日志只留临时执行环境。仓库仅存源码、参数、证明及实际执行身份/SHA；本页没有把完成 job 的临时文件假定为后继仍然存在。

## 5. 根代理独立核验

/root 完整读取完成 job 日志、逐项核实际阶段和停止标记，并独立读取三份重构 raw，检查全部字节数和 SHA 与日志中实际回执一致。再从第三份 raw 的完整 wholePhaseState 重新作 sort_keys=True、separators=(",",":")、ensure_ascii=True 的 canonical JSON，精确重构 17687 bytes 与 SHA 4116161f526db0dad03a8b1dc61d27c68d9df02e77680b3143662da147835fe2。candidate 键确实不存在，phases、sourceTexts 和 parsedSources 为空。此完整核验支持本页明确的预算边界，不把运行中的内部计算当作可恢复检查点。
