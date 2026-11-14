# R133 检查点参数说明的继承错误与 v8 修正

状态：已完成的实现审计与描述修复；原浮点计算的数学适用范围不变。

## 实际错误

`fourfold_codazzi_compact_metric_branch_refine_v7_probe.py` 在接受一个 Newton 步后保存完整径向节点、状态和径向导数。其 `checkpoint()` 以 warm-start 的 metadata 为底稿，并准确更新当前双精度 `nu`、`amplitude` 和 producer SHA。然而，它继承了旧的 `exact_float_nu` 字符串，没有把该字符串改成当前 `nu` 的二进制有理数。

本次逐一读取三个已归档的完整 M128 检查点，三个均存在该描述不一致。逐文件的原 SHA、解压后 payload SHA、真实双精度参数、正确有理数和原继承字符串保存在 [实际审计](2026-11-13-R133-m128-v7-checkpoint-description-audit.json)。原检查点及其原 SHA 不作任何改写。

该错误不改变这三次计算或恢复过程：v7 在加载候选/检查点后，唯一使用的参数字段是 `float(meta["nu"])`。继承的 `exact_float_nu` 未进入方程、Jacobian、线搜索、容差、后处理或恢复初值。最终 v7 candidate 和 report 在求解之后均重新执行 `Fraction(float(result.p[0]))`，并非继承检查点字符串。审计已核对已完成 M128 最终 candidate index 和 report，两者的双精度参数与精确有理数逐项相符。

## 修复的精确范围

新的 [v8 producer](../scripts/fourfold_codazzi_compact_metric_branch_refine_v8_probe.py) 在每个 accepted checkpoint 中明确写入当前的 `exact_float_nu`、`exact_float_amplitude` 和实际 `args.mean_boundary`；最终诊断 kind 改为 v8。旧 v7 和任何已完成文件均不修改。

[可复跑审计程序](../scripts/fourfold_codazzi_checkpoint_metadata_audit.py) 把这四项 metadata 改动从 v8 的抽象语法树中反向消除，随后比较 v7 与恢复后的整棵树。结果完全一致。因此 v8 除所列描述字段与诊断 kind 以外，没有改动实际求解代码。三个完整检查点的节点、状态及径向导数尺寸和有限性亦全部通过。

复跑：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_checkpoint_metadata_audit.py \
  --out /tmp/R133-checkpoint-description-independent.json
```

这是一处检查点描述修复，不把浮点有限 BVP 升格为全频、连续径向、全参数或真实 nonlinear regular 帽证书。后续恢复应使用审计明确的当前 `nu`；v8 新检查点同时给出与其一致的精确有理数。
