# R647：全 Gram–T 与核心速度边界的真实完整准备

本条消费 R647 已证的全局 rho 导数、交叉列矩、可逆 T 及964边界投影。唯一实际准备已退出0；没有执行线性或非线性求解。原1662固定 Hold g、602节点、M160/N2048、580328个未知不变。原325左/157右位置约束保留，另明定全部482个核心速度槽 U0=ez。

## 实际模型及初始化

每个节点和实际共同 cubic 中点保留 p0=V·d/a、p1=|d|²/a²−rho²、p2=|V|²−1 的全部962个二次 Fourier 系数，加原位置482行和U0的482行，算子形状为 **1158250×580328**。原始Y全部逐位保持；原U0数值本就为ez，158个负零改为正零，其余U不变。因此没有靠修改几何降低初始误差。

原Y/U二进制SHA `a810eed2f9931e707d8f4da4d0bae72b8739811f59c84ba76f1f3490cb14ed53`；新初始化SHA `c43acd8b24571ea419c57088f428814dadaa31d3c4fc97a729cca7265a752873`。158处变化均已实际核为U0零槽的符号位变化。

核心C列按每点 ||L+G||²累计，保留所有共享rho交叉项；U/D用新的Gram局部矩，U0再加单位边界行。1203点完整局部矩各计算一次，0复用，90.46984548秒。整个准备96.575718秒，最大RSS394812KiB。

## 原始残差与实核

初始完整Gram SSE `1.4951624510753042e-9`；节点系数最大 `2.98523375039692e-6`，中点 `1.8112358523576386e-6`。原BC最大 `4.163336342344337e-17`，新增U0残差准确0；核心962物理行最大约 `2.145628070e-16`。这是新目标的初值，不能与Pr的SSE混作同一目标降幅。

| 完整检查 | 实际结果 |
|---|---:|
| 列平方和最小/最大 | .00040718382195568096 / 130919915295970.69 |
| 固定尺度S最小/最大 | 8.739712415028356e-8 / 49.556969745616954 |
| 9个完整列的范数相对差最大 | 1.9527593191391913e-16 |
| rho全局G与密网Fourier比较最大绝对/相对差 | 4.46637743456435e-9 / 3.1431564864181225e-14 |
| 全增广Jv与complex-step最大绝对/相对差 | 3.655929725621121e-16 / 5.345441539404456e-14 |
| mask后联合边界Gram归一化条件数 | 25.45780623243155 |
| 投影方向原BC最大 / U0最大 | 7.063589287448672e-23 / 0 |
| 仿射修复原BC最大 / U0最大 | 4.930380657631324e-32 / 0 |
| 投影幂等最大误差 | 3.3881317890172014e-21 |
| 全投影算子伴随绝对/相对误差 | 3.548075432260455e-19 / 1.1256101021201119e-13 |

准确模型中的核心Gram恒等为零不等于浮点数组逐位零；本次只对新增U0采用字面精确mask，未把微小位置BC残差冒称严格代数恒等。非零G绝对比较误差亦原样保留。

## 来源与复现

算法 [parallel_20261117_direct_gram_integrated_preparation.py](../scripts/parallel_20261117_direct_gram_integrated_preparation.py)，14475B，SHA `85c726146641e26e09039cfd56e431b56ab503eb2c7801a7ae29d68ea02a0151`。实际报告 `parallel-root-direct-gram-integrated-preparation.json` SHA `b1c03602bd19049361e5268a3cfa39eb0d23fce30805cab814965e45c7c79ea4`；prepared NPZ SHA `70c6a7cb4f8886d96daba9dacda11d7c82d08342ef4d0283cf3a93c795a58390`。原始数组/报告/1203点缓存只在scratch；Git保存源码和配方。报告内全部依赖SHA完整绑定；这些SHA标识本次实际证据，冷重建带时间/路径字段的新报告须如实取得新身份，不能伪造原SHA。

本次在scratch执行的命令如下；各源码的仓内对应入口见R647来源链，原warm按既有1662配方重建。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-root-direct-gram-integrated-preparation.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source parallel-model-implicit-frenet-newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source parallel-root-implicit-frenet-probe.py \
 --matrix-source parallel-root-implicit-matrix-free.py \
 --gram-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_direct_gram_matrix_free.py \
 --coordinate-source parallel-root-integrated-coordinate-preparation.py \
 --work parallel-root-direct-gram-integrated-moments \
 --out parallel-root-direct-gram-integrated-preparation.json
```

该条仅使完整新算子、尺度和联合边界具备实际可用的身份。没有声称Gram收敛、共同C²、闭合、reach或README完成。后续直接Gram求解是独立新模型，不能替换仍在执行的原Pr预算。
