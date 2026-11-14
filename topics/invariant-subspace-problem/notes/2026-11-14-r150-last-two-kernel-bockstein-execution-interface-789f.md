# R150：仅补两条成本86核的60秒完整 polynomial Bockstein 入口

**状态：新三份 C++ 已实际编译成功，两份 Python 已通过 AST；尚未运行数学阶段。**
旧200列不重算。原式恢复只选择完整 T96 图中唯二成本86的真实零输出行，
以2列、一个32位 word打包；联合检验读取已经完成任务43605503242的小证书。

## 1. 唯一入口

```text
python3 topics/invariant-subspace-problem/notes/2026-11-14-r150-last-two-kernel-bockstein-runner-789f.py \
  --recovery-root RECOVERY \
  --known-results KNOWN200_RESULTS \
  --out OUTPUT \
  --seconds 60 --memory-mib 512 --compile-seconds 30
```

RECOVERY 仍是 run43597823809 / artifact14114364261 的原图和正常形来源。
KNOWN200_RESULTS 是 run43605503242 已完成小结果目录，只需其中两个已有二进制：

- `all200-torsion-columns.bin.gz`；未压缩SHA
  `9d5e8398f8bd586a1c91eaa5ab93868c9ec1d813c40c7131152d866c287d2b95`。
- `complete-infinite-quotient-system.bin.gz`；未压缩SHA
  `b46b9f338f961c33d528651c515fec1335943417574f8b83dd942407b87e7ef2`。

不需要下载旧200核的大恢复 artifact。

原模型文件在旧 artifact 中缺失时，仍可从已落库 `native-normal-form-input.txt`
补入 RECOVERY 的单独子目录；runner 按内容SHA查找，不以文件名冒认输入。

可选 `--notes-root NOTES` 指向既有 notes 依赖；默认即新runner所在目录。
这一参数仅便于在独立 incoming 目录编译，正常入库后可省略。
`--prepare-only` 只验输入并编译，明确不执行数学阶段。

## 2. 固定输入及共享时钟

原六项 artifact SHA 均不改变：

| 文件 | SHA256 |
|---|---|
| `reweighted-basis.bin` | `bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce` |
| 原 `normal-form-input.txt` | `291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6` |
| `nf-normal-forms.bin` | `eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840` |
| `nf-reduction.bin` | `e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b` |
| `nf-forward.bin` | `66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e` |
| `nf-backward.bin` | `cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f` |

原 integer mod961 模型、完整状态与旧首轮余仍从 notes 读取并核此前固定SHA。
依赖 `2026-11-14-r150-f31-bitplane-789f.hpp`、
`2026-11-14-r150-torsion-characteristic-789f.py` 和 python-flint。

输入验证与三个分别≤30秒/512MiB的编译先完成，然后才启动唯一60秒数学 deadline。
原两核恢复、两列正常形、完整G像、最后联合315判据全部共享这个 deadline；
每个子进程只得到当前剩余时长，TERM后强制结束宽限10秒。
阶段间输出哈希计入数学时钟；最终清单/保存只做文件工作，不追加数学计算。

## 3. 两列的真实原身份

新源码由已经实际完成的全200源码独立派生；准确替换及源SHA保在
`2026-11-14-r150-last-two-kernel-bockstein-source-derivation-789f.json`。
旧源码没有修改。变化限于：

- 只选完整图中 cost=86 的两条源核；完整图1021/1174行、次数和716/60050仍核验。
- 每列为成本86，原来源最高系数界76，打包 word 数从7变1。
- 原加权输出由 B85 的219032个坐标升为 B86 的223399个坐标。
- 新正常形使用 m最高层参数界46，低层按原10次差传播。
- 完整像核验参数界86、两列原 head 标签；没有把它们叫目标2/3。

原6188行重放、全部 primitive 整数系数 mod961、完整31整除、原来源成本、
完整 \(GQ+\rho=RHS\) 核验和 forward/backward 原SHA不变。

二进制仍使用 `R150KK31`、`R150BK31`、`R150NF31`、`R150IQ31`，其明确头部现在
分别含 nt=2、B=86、原输出223399。不能将新文件误接旧nt=200/B=85 reader。

## 4. 最后联合的是完整多项式核像

新的两列首先在实际完整820状态中核505条观测全部为零，并由315维K基逐坐标重构；
若不通过，任务失败，绝不丢弃 free 部分继续。

随后合并旧199/200两列非零像和新两列；其余旧198像已实际为零。
对四个完整向量取全部316次 J-Krylov 列，总1264列，作真正的 J 不变闭包。
每条源保原 head、成本和原行编号。最终检查全部九个真实首轮余是否在该像中，
相容时保存全315坐标解，不相容时给明确正常形坐标对偶。

覆盖范围依据已有精确结构稿：660个 N–N 原核及972个低混合核均有精确
\(\mathbb Z_{(31)}[s]\) 提升，β为零；再加旧200、新2，恰覆盖全部
1834个原 polynomial 核方向。J闭包包含它们的任意多项式倍。

基列按实际成本排序后贪心选独立列，故相容目标还给出其**仿射 β 类**所需的
最小初始核来源成本。此数值不包含后续原来源修正的成本，不能用来代替有限
cokernel 检验。成功或失败均保持 `finite_budget_verified=false`。

## 5. 成功字段与输出

总文件仍是 `OUTPUT/results/bockstein-pipeline-receipt.json`。
数学成功必须为 status=completed，且四个实际阶段标记依次为：

```text
last-two-original-kernel-bockstein-complete
last-two-original-bockstein-normal-forms-complete
last-two-bockstein-image-certificate-complete
last-two-complete-polynomial-bockstein-test-complete
```

原阶段须有 highKernelColumns=2、完整原核身份、完整31整除、各自成本界均true；
最后须有 allNewBocksteinsInTorsion=true、
allOriginalPolynomialKernelRowsAccountedFor=1834。
任务完整完成不等于九目标相容；相容性按实际 `targetCompatibility` 九个值判断。

小输出：

- 原式/像的实际metadata、四阶段日志、编译日志与总回执。
- `complete-polynomial-bockstein-image-result.json`：四列最小多项式、完整像维数、
  增广秩、九目标相容性、完整解或对偶、最小核成本的准确范围。
- `complete-polynomial-bockstein-image.bin.gz`：四列原来源字典、所选J幂、
  全315坐标像基、九右端、来源系数及限制J矩阵。

`OUTPUT/recovery/` 保存两条完整原核、原整数Bockstein右端、正常形、
原来源trace、完整G商与新余。无论超时或完成，全部实际已有文件都应放进同次
recovery artifact；不得只保hash而丢来源。

## 6. 新文件与当前状态

独立新源码为前缀 `2026-11-14-r150-last-two-kernel-bockstein-` 的
`original-789f.cpp`、`normal-form-789f.cpp`、`image-789f.cpp`、
`torsion-789f.py`、`runner-789f.py`。
另有准确派生记录、实际编译/AST准备回执及本接口稿。

三个C++已经分别在30秒/512MiB限制下退出0；两个Python已经通过AST解析。
数学阶段尚未执行。先前200列、共同g及H0存在性结论不因本次准备而改写。
