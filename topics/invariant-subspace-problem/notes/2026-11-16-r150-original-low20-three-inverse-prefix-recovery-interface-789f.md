# 原 E20 三逆前缀恢复与四阶段 Actions 接口

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

本包因共享 executor 不可用而冻结。恢复源尚无本地 AST、编译或数学执行；只作静态审读。projection-only 源此前 AST 已通过，尚无成功的实际投影运行。启动请求被 exec-server 拒绝，不是数学退出码 75 或 1。

## 1. 准确恢复对象

原 v2 在 25.513854554010322 秒被 SIGKILL，三个逆已封存，完整 constants 未完成。原 manifest 恰为 3418 bytes：

~~~text
SHA256 c7b010a2c16e2896782eaaad74f977d00e640af6c8142b623474a015b948bf9b
binding 672c57bb68079e9a49cff09e4a7fdadd7b89dc017927913ee0d35261a08d2522
~~~

六个完整文件是三份候选和三份实际两侧乘回后的逆。已验证的逆分别为 6、5、11 维，共 364 个 E 产品、1092 个忠实有理坐标。后继真正需要的十一维逆为：

~~~text
phase original-inverse-11-abb2c7a819cd
stored 1473718 bytes
SHA256 ec9d6e2758ae835f027fd0c3d8da26945814cb3599949057f96ac542b78300e6
logical 2975996 bytes
SHA256 31bf451e26193eed026feba6bf00a71a9394a78ecce0a7571aea661380b76c05
inputSha256 028c02fb11bb2acc1717b0c7d221edd91a0e1d6ab2fee34c4fe133d7207e89d5
label same original eleven quadratic sources
~~~

旧执行身份为 notes/r150-original-parameter-module-execution-789f/local-20261116-original-low20-v2-constants180-terminated137.json，blob 28f8fd36e7d970efa921a58d72e89e3cce83a4fd。此次恢复保留其失败范围，不改旧 raw、时间、状态或源。

## 2. 新 runner 的数学范围

新 runner 导入冻结的原 v2 源，逐一核原物理模型与 helper、原 field model 源、完整 116-seed manifest/base 的全部 SHA，以及原 v2 完整源和语义 binding。它调用原 fd.prepare(helper)、EField.invert 和 build_constants，不修改这些函数。

唯一新的控制是已有 progress 回调：当冻结函数真正发出以下事件后，回调抛出专用 StopBeforeCubic：

~~~text
original-all-fifteen-quadratic-source-identities
exactECoefficients = 225
~~~

此事件位于原代码全部 225 个二次来源恒等核验之后、构造 C 的第一行之前。runner 只捕获这个特定停止，不把任意异常或 Budget 当作完成。

因此这是真正重新执行原数域前缀。没有重建 $35\times55$ 的 C，没有调用其余 constants 打包，也没有运行二十维精确求解。

## 3. 逐字恢复与来源记账

原逆函数每次提交 candidate 或 verified data 时，runner 使用原 canonical JSON、原相位 format 和原 binding 编码。先硬核新逻辑内容的长度/SHA，再用固定运行时压缩，硬核新压缩内容的长度/SHA。只有二者都与旧实际描述符相同，才写入恢复目录并登记。

新的执行由新 recovery 源、独立 binding 和新 receipt 记录；旧文件仅表示经 SHA 重现的原历史数学内容。不把新用时冒作旧用时，不把新源身份冒作旧执行，也不改变候选的未验证标志。verified 文件仍须具有原输入矩阵哈希、label、两侧 E 和两侧 place 的完整标志。

最终成功要求：

1. 六个相位逐个读回，stored/logical SHA 全匹配。
2. 三个 verified 逆的产品计数和标志全匹配。
3. 完整恢复 manifest 恰为旧 3418 bytes / 原 SHA。
4. 真正到达原 225 事件。
5. 原 original-exact-constants 相位仍不存在。

全真才输出 completed-prefix-byte-recovery，始终保留 originalConstantsStageComplete=false。

冻结前，独立 V8 仅重构了上述元数据：原 semantic binding 和 3418-byte manifest SHA 完全一致。这是字典与编码布局核对，不是逆矩阵重算或恢复执行。

## 4. 冻结文件

| 文件 | Git blob | bytes | SHA256 |
| --- | --- | ---: | --- |
| 2026-11-16-r150-original-low20-three-inverse-prefix-recovery-789f.py | 99b82a8faa7c88179d7dcc8ce33b28ee8d1ecfd7 | 15715 | b451d296c705bd9c95de7e35bffc6396a006bcb4d3d968f9b986ee4f11aeb071 |
| 2026-11-16-r150-original-low20-three-inverse-prefix-recovery-inputs-789f.json | 7612e8b2f00725e9fd84a067cc94da52b3e64d48 | 10662 | 0670e498be3a33c8da64296188785937ee98c1a5209186998818c515603d4508 |
| 原 v2 exact helper | 541c14b36925e3cc94018edd8a17a6a765041f5d | 33539 | d9d98bc379e322e9c212b7ad7721399ec8b1bab9970a2755700338f7053d47da |
| projection-only 源 | d20db6c713d362d56e8e59ab0c8bcdf846764728 | 21178 | a77cf71a3e3c4dcbd4b68f3f4d99f98a64bd4f64394f46507c8c42cc5aecf48f |
| 原 observer | f8aea7924d8becc10e50303a1c9b36f34d718014 | 5855 | c5d5f777246dbb99d516855eb007845c9b25673cfe736e74cf56f559111a5618 |

其余三个原模型源及完整六个相位描述符都在 inputs 中锁定。文件 basename 必须原样保留，因为它是历史 source binding 的一部分。

## 5. 同一 job 的准确四阶段

固定 Linux、Python 3.12.14、python-flint 0.9.0，不需要 Singular。四阶段共享同一临时工作根，不从其它 job 下载数组。

| 顺序 | 数学任务 | 数学秒数 | MiB | outer 秒数 |
| --- | --- | ---: | ---: | ---: |
| 1 | 原 field model，through seeds 全 116 | 180 | 2048 | 240 |
| 2 | 新三逆恢复，在 225 门停止 | 120 | 768 | 180 |
| 3 | 独立原 20×50 projected | 60 | 512 | 120 |
| 4 | 原 Q60 solve 与全部最终产品 | 300 | 1024 | 360 |

总 outer 为 900 秒，安装与发布另留余量；约 25 分钟 job 可容纳本计划。阶段依赖只接受前一阶段真实 exit0。新数学失败或 137 不改写为预算；75 只有已产生新的完整相位时才考虑同源接续，不空重复求解。

第一阶段不能只 through base：冻结父 read_paid_base 要求完整 manifest 含 116 seeds，并钉住其全部字节。完整重建保留 116 个原来源核验，不临时删门。

输入 JSON 的 stagePlan 保存全部准确 argv。根 wrapper 可逐阶段套原 observer，三个观测文件每次使用新路径，保十秒心跳和真实子进程退出。wrapper 若另有限时，须为本表 observer 的显式墙时及最终收尾留出余量。

## 6. recovery 直接 CLI

{work} 和 {scripts} 分别是同 job 临时工作根和保留原 basename 的冻结脚本目录：

~~~bash
python 2026-11-16-r150-original-low20-three-inverse-prefix-recovery-789f.py \
  --exact-source {scripts}/2026-11-16-r150-original-low-commutator-twenty-exact-constants-v2-789f.py \
  --model-source {scripts}/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py \
  --helper {scripts}/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py \
  --paid-model-source {scripts}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py \
  --paid-model-out {work}/original-ten-parameter-module127-v2 \
  --restored-out {work}/original-low-commutator-twenty-exact-constants-v2 \
  --out {work}/original-low20-three-inverse-prefix-recovery \
  --seconds 120 --memory-mib 768
~~~

输出路径：

~~~text
{work}/original-low-commutator-twenty-exact-constants-v2/
{work}/original-low20-three-inverse-prefix-recovery/prefix-recovery-manifest.json
{work}/original-low20-three-inverse-prefix-recovery/original-low20-prefix-recovery-receipt.json
~~~

第三、四阶段沿用 projection-only 参数，parent-out 指向上述原字节恢复目录；数学输出为 {work}/original-low20-projection-only-exact。原源码将再核父 manifest、唯一 verified UI 的双 SHA/input hash、全部 alpha 字典，并支付真实 Q60/1000E/400selected 门。不为恢复放宽现有 source 或 binding。

## 7. 数学和数据边界

本恢复没有新的 E20 求解结论。只有第四阶段全部门成功，才有实际原 E 的二十列系数；完整 55/参数/source 身份沿已付规范来源定理，仍不冒称本次新算 C 或 CZ。

全套禁止上传数学数组、checkpoint、candidate、raw 或数学工件。仓库只保存来源、参数、证明、真实执行身份和 SHA。恢复文件和求解相位仅在同一 job 的临时目录使用。job 结束不能假定数组仍可访问；后续需要时须在同 job 登记真实消费，或重新通过本冻结入口计算。
