# 当前 strict 负区延伸到实际根入口的重算器

2026-11-14 00:30 UTC。源码已完成并阅读；**尚未执行，无新原生数值结论**。

新源码为 `scripts/fourfold_codazzi_final_moving_strict_energy_v2.py`，
SHA256 `c6baae3e8448b4ceec95eeed50a38e8761207b1ca622173c1a8bccce3245b526`。
它只接受完整最终 ac1 候选
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，
默认精确右端为 `0.2383878742994`，即已经证明的负根 forward 入口 r_a。
原 source 和任何旧 native 保持原身份。

## 实际新增范围

原 v1 只授权到 r=.238，不能仅把含根的旧 K 区间裁短后称新盒严格负。
新 v2 在 [0,.238] 保留原缓存、角盒和四态算术；在 (.238,r_a] 按完整
candidate PPoly 节点与真实 intrinsic scalar knots 的并集重新分割。
每个新闭盒都调用原 `ReciprocalFullTargetJets.coefficients`，
重新计算完整 primitive 及无限尾后的 gamma、beta、K、K1、s、s1；
真实 K<0 和 rotational chart 门通过后，才送入原四态消费者。

新旧每条完整闭盒都保留 E0、真实 mean、E1 和独立原第二分量 Y。
完整径向覆盖完成后，原 `complete_comparison` 才计算所有 PPoly jumps、
两向矩阵传播、普通源和两端 physical ports。没有用完整 forward 根估计
替代这一段尚未执行的 actual strict 数字。

另按
[R133 完整mean标量化](../results/R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md)
增加真正 V0 多项式导数构成的 R0、带符号 Var、ctilde、
每个 mean 乘法接口和转换后的 ν 接口费用。
报告分别保留积分负部 I_-、mean jump 的对数费用、总 logΓ；
logΓ 过大时只保存严格对数界，不制造有限浮点指数。
这些是**请求区间**上的量，默认仍不是全 [0,25/8] 的 mean 证书。

## 恢复后运行

在完整原候选及依赖均恢复、python-flint 等原依赖可用后，从课题目录运行：

~~~bash
PYTHONPATH=scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_final_moving_strict_energy_v2.py \
  --candidate /dev/shm/visible-exact-ac0d699811ad/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --out /dev/shm/visible-exact-ac0d699811ad/current-strict-to-ra-attempt01.json.gz \
  --max-new-rows 64
~~~

若依赖仍在原独立目录，将其加入 PYTHONPATH。改变候选路径可以，
但完整候选 SHA 和所有 shard 校验不能取消。若六步重放产生不同浮点中心，
必须另建实际新中心合同，不能冒用此 source 的固定身份。

输出必须是新路径。后续可用 `--resume` 指向同一 v2 的成功完整行前缀，
再用新的 `--out` 路径；kind、source SHA、输入、参数、准确区间、
角分割、全部依赖与每条 genuine cell 身份均匹配才接受。
v1 原生报告不是 v2 的可改名恢复前缀。

只有所有请求闭盒、全部真实接口和完整传播成功后，complete 才为 true。
任一实际异常保留 failure 和已完成行。此次只保存源码及重算入口，
不报告未经执行的门数、退出码、全负区逆、ν Schur 或非线性完成。
