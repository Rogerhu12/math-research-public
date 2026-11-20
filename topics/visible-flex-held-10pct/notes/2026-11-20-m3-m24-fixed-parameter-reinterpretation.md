# m3：M24 实际设计到固定全部物理参数对象的转换

维护会话：Astra-held10-1b6d88ec-20261120。

本条接已通过原 metric 门的
newg-wide-lambda0p002-m24-linear，准备后续固定参数的场细化入口。
没有再解前缀、没有新尾调用，也没有把设计序列叫作固定 g 的收敛。

## 1. 必须解释 p0，不能原样改 fixed 标志

原 portable 设计对象的 p0 是 delta 增量；在本次实际 raw 中为
-9.684017201077914e-6。原 base delta=.06414432506418023，所以
冻结后的 delta=.06413464104697915。

固定对象采用原类的 fixed=True 构造，其 p0 语义是
log(q_actual/q_seed_support_amplitude)。本次两者均为 .06，故新 p0=0。
全部实际 c6,...,c72 仍相同；新旧 pscale 完全相等时直接保留原
p[1:]，避免无意义的乘除舍入。若尺度不等则按物理 c 转换并检查。
原 gauge、warp=.06、角图、profile、尾参数、cut 与 exact-lift 系数 1
均保持相同定义。

新增独立 adapter：

    scripts/resume_m3/frozen_actual_m3_model.py

它复用 actual_m3_metric_model 读取原对象，再用同一完整 Base/Lift 类
构造固定对象，不绕过旧 adapter 对 fixed=True 不同 p0 语义的拒绝。
load_model 接受 source_run、source_run_sha256、mean_nodes，
返回可直接交 FrozenPhysicalField 的固定几何对象；常量向量在
obj.frozen_parameters，完整参数合同在 obj.frozen_geometry_contract。
原 raw 与 physical 数据仍只读，输出不包含可再生场数组。

原图的均值声明是 mean1168 与原 GL6 高度 oracle。此函数没有把它
替换成真积分 primitive，也没有把 literal clip 图升级成 C² 图；
正在另付的无 clip 解析桥、共享 Hermite 与真积分对象必须单独绑定。

## 2. 实际转换检查已执行

~~~bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/frozen_actual_m3_model.py" \
  --source-run "$WORK/newg-wide-lambda0p002-m24-linear/run.json" \
  --outdir "$WORK/newg-m24-fixed-reinterpretation" \
  > "$WORK/newg-m24-fixed-reinterpretation.log" 2>&1
~~~

实际 exit 0。保原 631 个物理节点，新 normalized chart 对物理 s 的
回转误差最大 2.220446049250313e-16；原节点与 physical 导出的节点
完全相同。

在包括 profile breaks 的 42 个 s 断面、1168 个角点上，下列差量
实际全部为 0：

- 完整 exact-lift 参考 pos、p1、p2、s1、s2、sp、spp；
- 完整 rho、rhop、v、vp、vs；
- 同一物理场的非均值六个二阶 jet；
- profile 的值、一阶导数、二阶导数；
- 物理坐标中的原 Frenet RHS；
- mean1168 速度及其原求导值；
- 同一原 GL6 规则的高度 oracle；
- 完整核心入口系数。

这些是明确参数重解释的有限检查，不是连续区间证书。新对象没有
新增参数自由度、额外 forcing 或可调均值。后续 field-only 修正必须
仍用原真实 DN、原物理验收和明确的完整场/均值导出；单个 accepted_step
不是完整物理 pass。

## 3. 来源

| 对象 | SHA256 |
|---|---|
| 新 adapter 源 | e2b423838cf6a1bccbfbc5bf3a87be3f44d6ecddbb1d507f935500eaa5772f44 |
| 原 M24 run.json | c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a |
| 原 M24 raw | 1bb631d68796af48821e71baeb696a9ffa7f66f92d7cdcb3af84e27ebe08076e |
| 原 M24 physical | f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d |
| 实际 identity.json | fb4f796fdb7c8fed75a2b223869527597420086ad7506c2c37415d2d1c53a0ce |
| 实际 model-config.json | 45baf24f3465cec3c8844d65969a056a1be04c39c4b626eed3ea33208de67b14 |

当前原 nonlinear DN 作业独立继续。待它返回后，必须从其最终原 run
重新生成固定合同，不能把本条 linear 场的参数/hash 无条件搬过去。

