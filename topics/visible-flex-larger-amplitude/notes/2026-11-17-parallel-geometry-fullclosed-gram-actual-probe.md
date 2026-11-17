# 真正全闭共享 C² 初猜上的完整角值 Gram 雅可比与伴随

2026-11-17，geometry_amplification。**一次真实输入的算子准备试验，未执行非线性求解。** 新共享 `(Y,U,A)`＋解析材料圆端口模型的全部角值行已完成一次 complex-step 方向及一次完整伴随核验；该初猜自身的度量误差很大，不能称为接受场或新的父场。

## 对象与唯一实际计算

消费 model 交付的 `parallel-model-fullclosed-hold-warm.npz`，SHA
`401255b7328ba2e4cdfe5af94d0a0896859960f1b474961d30aff33d8248f02a`；其来源／标量／截频／节点定义报告 SHA
`0c499334cebe74f0c417ccb89b5ee4dcf86cb07dfbab1f0d46c0b805f4a71b80`。
真实规模为 M160、N2048、923 节点、1845 个节点及**真实共同 quintic 中点**、1,332,245 个自由变量、11,335,680 条原角值残差。没有把这个含解析 lift 的目标冒作旧 962 项完整有限谱。

节点剩余场 q 的全部三 jet、Hcap 及固定标量样点直接读入，未另造初猜。`pack(require_affine=True)` 逐项确认输入已经满足准确仿射条件，三组 jet 改动均为零。core 的 Z、U−ez、Az，以及末端 q 的全部三 jet 均字面为零；support core 的 T 也字面使用 `−νc`。完整未截断解析 lift 在端点的径向三 jet 为 `(R,−1,0)`。

浮点载体为 `S=2.3712998717298257`、`R=.5647341753868043`、`Hcap=1.9479520470229232`。初猜报告已逐项给同一个精确 Hold 标量的 oracle 及时间／a 载体误差；本次只消费这些载体，**不把数值读数升级为整个场的精确标量／舍入区间证书**。原 pulse 前缀在 `.995` 后的 g 与 Hold 不同，且原 M320→M160 截频二 jet 系数遗漏 l1 最大为 `.8681159817010814`；本次不继承原 R648 的 Gram 或曲率证书。

完整残差为目标正交标架中的
`(|Fs|²−1, Fs·Fφ/(aρ), |Fφ|²/(a²ρ²)−1)`。位置与六 jet 都来自保存三 jet 定义的共同 quintic 加完整 χ-lift。所有 core→ρ、core→Θ、core→lift 项、普通 core 支撑关系链及 Hcap 都进入 Jv/Jᵀ；模型不调用旧 Pr-CU 逆来定义 A。

## 全部行的实际核验

唯一方向 seed=20261117，complex-step 为 `1e−30`；core、A0、内部 Y/U/A 和 H 块全部非零。方向尺度仅用于平衡这一次导数检查，不是新增 LM 预条件器。其精确配方在源码和报告中保留。

| 核验量 | 实际值 |
|---|---:|
| 完整 Jv 与 complex-step 的相对 l2 差 | `7.634512808900217e−15` |
| 完整 Jv 与 complex-step 的绝对最大差 | `3.019522409886122e−10` |
| Jv 的 l2 范数 | `535859.5517304487` |
| 方向的 l2 范数 | `25181475.060441446` |
| `<w,Jv>` | `37.199146711781566` |
| `<Jᵀw,v>` | `37.19914671178003` |
| 伴随绝对／相对差 | `1.5347723092418164e−12 / 4.125826651705775e−14` |

该结果支持当前完整有限评价算子的实现。它不是全非线性模型可解、满秩、收敛或连续几何通过的证据。一次普通残差、Jv、complex-step、伴随分别耗时约 2.027、4.417、8.835、3.373 秒；整次含数据归档约 20.359 秒，时间仅为当次环境观测。

## 同次残差已经揭示初猜不满足度量门

没有额外扫描；直接消费上述唯一普通残差数组：

| 同一候选的有限读数 | 实际值 |
|---|---:|
| 节点最大相对 Gram 算子范数 | `147.40629026335586` |
| 真实 quintic 中点最大值 | `147.28100241396425` |
| 三分量绝对最大值 ss / sφ / φφ | `1.248555782649316 / 9.997518719350957 / 146.90242962577042` |
| 采样 core ρ 最小／最大 | `.16601843096428737 / 4.613852013401925` |
| 采样相对 Gram 行列式最小值 | `.2096437812129679` |

Gram 峰在节点 `s=1.5788140083860203, φ=.1932815792735908`；角向项主导。行列式最小点为中点 `s=2.090527238528373, φ=5.534602682691394`。这些是指定点集上的普通 binary64 读数，正的点值行列式不等于连续浸入证书。该初猜显然未通过原 `1e−6` 度量数值门；本次没有进行修补、规范化或新非线性迭代。

## 冻结来源、复现与复用

| 文件 | SHA256 |
|---|---|
| `parallel-geometry-fullclosed-gram-operator.py` | `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d` |
| 实际入口 `parallel-geometry-fullclosed-gram-actual-probe.py` | `803f6c5e121a4f167984cc33371856d9978a3d13177f2315e7321f37ea533483` |
| 完整实际报告 `parallel-geometry-fullclosed-gram-actual-probe.json` | `f09148db310f0229170207538ecc4d41c723d74130da6897c10bc06fd68e15c4` |
| 仅仓库外的原数组 `parallel-geometry-fullclosed-gram-actual-dense-arrays.npz` | `4da17687a6856901d09d92f02ad0c7bd0cdf012475403fbf2f8488579cc0a05e` |

入口是在原 f949 准备代码中加入已计算数组的流式归档，再仅适配实际 NPZ 输入；两份未运行准备代码身份也留在报告中。无新增数学评价。304,031,712B 数组只存原 `residual,x,direction,Jv,weights,Jᵀw`，不入库；后续 FFT 等价实现只消费这一份结果作对照，不重新支付 dense 试验。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-geometry-fullclosed-gram-actual-probe.py \
  --operator parallel-geometry-fullclosed-gram-operator.py \
  --bundle parallel-model-fullclosed-hold-warm.npz \
  --bundle-sha 401255b7328ba2e4cdfe5af94d0a0896859960f1b474961d30aff33d8248f02a \
  --out parallel-geometry-fullclosed-gram-actual-probe.json \
  --arrays parallel-geometry-fullclosed-gram-actual-dense-arrays.npz
```

需在新的输出位置复现；入口拒绝覆盖已有报告／归档，防止把重复试验混入一次计划。本文未改变任何正在运行的短 Pr／Gram LM 门或预算。全闭模型的真实 warm 如何改进、同 g 精化、完整连续 Gram／嵌入／reach、固定帽、held 和非全等仍须由后继同一候选支付。
