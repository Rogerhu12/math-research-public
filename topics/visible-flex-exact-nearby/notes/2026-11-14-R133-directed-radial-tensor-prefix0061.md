# R133：61块径向原生前缀与真实连续张量消费

2026-11-14。实际部分运算，主目标未完成。

证明与精确范围见[径向误差及张量消费者](../results/R133-supplement-directed-radial-ODE-error-and-tensor-native.md)。本次输入全部3903个真实闭格与原61块比特门保留在[径向native](2026-11-14-R133-directed-radial-prefix0061-native.json.gz)；全部逐格连续误差在[tensor native](2026-11-14-R133-continuous-tensor-prefix0061-native.json.gz)。源与原始字节SHA见[身份清单](2026-11-14-R133-directed-radial-tensor-prefix0061-identities.json)。

原径向程序从完整8967行geometry proposal及全部141不可变块开始，尚在继续。它使用原candidate ac1d5b98…、准确α/ν、原target91040c…和原q-vector8f2471…；原geometry报告SHA49870375…与链尾4d87057a…未变，全部原大输入的生成方法保存在[完整geometry记录](2026-11-13-R133-moving-connection-checkpoint-consumer.md)及[共同六阶段重构](2026-11-14-R133-common-six-stage-runner-entry.md)。本次没有重新运行原BVP或浮点geometry。

完整mesh输入为已发表 `2026-11-14-R133-complete-geometry-mesh-hulls-native.json.gz`（SHA5ed344a8…）。完整角输入须按[四片无损清单](2026-11-14-R133-final-complete-angular-defect-parts.json)准确恢复原gzip，其SHA为7a3dd2c1…；不把拼接文件再次gzip。

实际消费者命令（从本课题目录，OUT必须为新路径）：

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 -u scripts/fourfold_codazzi_complete_continuous_tensor_geometry.py \
  --mesh notes/2026-11-14-R133-complete-geometry-mesh-hulls-native.json.gz \
  --radial notes/2026-11-14-R133-directed-radial-prefix0061-native.json.gz \
  --angular /workspace/scratch/ac0d699811ad/geometry-verified-20261114/complete-angular-defect.json.gz \
  --out /workspace/scratch/ac0d699811ad/geometry-verified-20261114/continuous-tensor-replay-new.json.gz
```

实际原过程normal0、5.029729794秒；`complete=false`、3903格。首原生输出在scratch名为continuous-tensor-attempt01.json.gz。原径向attempt01–03域/选片/过粗费用保留，attempt04当前成功前缀继续，并没有将它们重命名为本次成功。每次续tensor前先保新径向不可变快照，使用同一输出加`--resume`只消费新增行；完成全部8966格才授完整模型见证距离。
