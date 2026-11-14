# 完整 .05 连续残差覆盖及 C0 加密入口

2026-11-13。完整相关 Taylor producer 已实际完成同一原始目标
[0,1/20] 的 150 个连续闭盒，wholeη ±10^-9、完整角圆、原512点primitive
及其全部无限尾。有限候选仍是已保存的准确dyadic函数，不作投影PDE假设。
物理闭角格4096、准确候选存储网1024；所有非线性乘除在实际区间jets中进行，
未以小网作截断Fourier乘法。完成时间590.76178286秒。

完整覆盖不等于误差屏障通过。真实R131 v2在第112盒的1/16管门失败；
见同日R131-C0-only-failed-branch-repair.md及原生失败报告。
现有证据不能以该误差比较授整个.05的精确分支，也不证明不存在。

新 fourfold_codazzi_residual_C0_taylor.py 保留同一完整二维二阶Taylor余项，
只删延拓不再需要的残差角导数和候选D2输出。所需候选归一化导数矩形为
r≤3、θ≤3；闭角格场值另付至θ≤5，残差矩形为r≤2、θ≤2。
只消费j=0 Taylor式，所有低阶系数与原完整Jet公式相同。
初始真实误差/mean/所有全参数及无限尾均仍保留。

正在运行的下一入口（此源码保存时该完整报告尚未完成）为：
```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_codazzi_residual_C0_taylor.py \
  --right 1/20 --subdivide 4 \
  --out notes/2026-11-13-Codazzi-C0-Taylor-r005-v1-native.json.gz
```
当前不授其完整残差覆盖或C0屏障，实际结果须另保存消费。

## 固定输入

- `scripts/fourfold_codazzi_residual_taylor_compact.py`：`51e454ad8aa1209d3199169d52cf8cf3df49d8728da8914db251ebddc363f6d0`。
- `notes/2026-11-13-Codazzi-joint-Taylor-r005-compact-native.json.gz`：`d69d826e957f4a3532fdd5e892d916080de8ae325dfb89d78a7ca0b84a82162a`。
- `scripts/fourfold_codazzi_residual_C0_taylor.py`：`03b9615e0421549e76fd929deca3ee972086c744ee4b045da6da90decf4db27d`。
