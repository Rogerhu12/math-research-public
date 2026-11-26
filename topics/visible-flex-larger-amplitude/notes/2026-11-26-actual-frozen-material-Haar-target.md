# 第 75 阶段：从真实 7ebb 场冻结准确材料 Haar 目标

日期：2026-11-26。状态：**实际目标定义返回；没有优化结果或认证声明**。本条登记公开 Actions 45762076394/1 第 75 阶段，来源是[第 9 卷实际小结](2026-11-26-public-actions-45762076394-1-part-009.md)与[运行](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394)。它使用已刊 R691 公式和已实际返回的第 71 阶段 moment carrier，不重证已有结论。

## 1. 返回了什么

完整 `frozen_material_haar_metric.py` 在真实 7ebb bundle、该场完整报告与完整 moments 上自然返回，returncode=0，阶段耗时 6.227917259999231 秒；`summary_errors=[]`、`missing_outputs=[]`。新文件为 `haar-7ebb-fixed-target/frozen-target.json`，19744 B，SHA `4db6a26e5fa330e00ad5e25976731b5134e39f1d15639c7ca1338e76ee39fc99`。它是固定目标 manifest，**不是方向报告，也不是近等距解**。

| 身份 | 实际值 |
|---|---|
| schema | R691-frozen-true-material-Haar-metric-v1 |
| 新 target identity | e35ce2d39863848238d08d2cc783292ed39929239ec6cae036deab88c9d73123 |
| frozen physical bundle | 7ebb5f42b29e0979f7a84a93fb8decb0b45ae8ec2f8c713bed820a8adb33d37b |
| frozen canonical physical model | 4c8e450615a63136013110568207903624d070aa77b5c0b791a079fcbee54b82 |
| angular identity | 0f21f1e2f6ec76b2df2ef50e2f255d1516cbb0bef404ffeb83b25215a00b213d |
| nodes | 06e56f248db23c20a7f91c32861cd64daf51706ce06bf74aeeb5ee6070ef3734 |
| observations | 71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112 |
| profile carrier | 3d5063c868245c155b6258f47d0ed5059ee48ae98da520f930a7e08153332cc8 |
| 完整 evaluator source | c5a717dbca55311060207672c703293403c16c6e5142b84cc522e660afc67a64 |
| 完整 moment source | 1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010 |
| working moments | 027c36ae6f55a204a9636eabf2eda841609a784b823c76435d74bddce7f0c16f |
| actual source commit | dc7b8bccee2fa89e39879b0083808679becb88ec |

冻结输入报告和 bundle 都来自 `mean-metric-design-amplitude-separated-SOC-v2-first/{report.json,final.npz}`。这是原 λ=1 / R671 物理场的 7ebb 分支；不能把它改标签为 fixed-deep 的 9b937e 场，也不能将两者的 profile、reference、D/L 或 Phi 混合。

## 2. 同一个准确目标的定义与数值载体

按已刊完整源 `mean_definition()`，冻结物理场记为 $F_*(s,\phi)$，材料角满足 $d\theta=\rho_*(\phi)d\phi$。目标定义为

$$
g_* = E_*(s)\,ds^2+C_*(s)\,d\theta^2,
$$

$$
E_*(s)=\frac1{2\pi}\int_0^{2\pi}\rho_*(\phi)\,|F_{*,s}(s,\phi)|^2\,d\phi,
\qquad
C_*(s)=\frac1{2\pi}\int_0^{2\pi}\frac{|F_{*,\phi}(s,\phi)|^2}{\rho_*(\phi)}\,d\phi.
$$

混合项由原完整反射奇偶性为零。冻结的是完整原 shared-quintic q、同一 canonical analytic f/h/k 与准确全圈积分的定义；当前优化变量不再改变此目标。上式是已刊 R691 定义的应用，不是本次 6 秒目标写出步骤重新证明的连续解结论。

返回字段 `frozen=true`、`exact_Haar=true`、`finite_quadrature_is_target=false`、`new_target=true`、`old_Phi_preserved=false`。第 71 阶段实际工作载体使用 M=160、全角 Q=8192、derivative order=12，2049/2049 quarter orbits、完整正 orbit weight=8192。该 moment 结果的 complete=true 与 rho_positive=true 仍保留；但 **accuracy_reached=false**。工作 Q、区间中点和包围精度不成为新目标定义，可以为同一目标更换更精确的有效数值载体。不能把“exact_Haar=true”解释为此刻所有数值 moments 已达到其精度目标。

## 3. 显式未通过、未执行与误差责任

| 实际字段 | 值／解释 |
|---|---|
| target_certified | false |
| metric_certified | false |
| geometry_certified | false |
| refinement | false |
| topic_complete | false |
| 第 71 阶段 accuracy_reached | false |
| 优化方向数 | 本步骤没有求方向 |
| 新 baseline Phi / max | 本步骤没有读优化基线，不用旧 mean Phi 填补 |
| 全域 metric / reach / marked certificate | 本步骤没有给出 |
| 异常与缺项 | returncode=0；summary_errors=[]；missing_outputs=[] |

准确积分目标的数学身份与数值求值精度是不同责任。这里没有把 7ebb 旧报告的移动均值 objective 复制为固定 Haar objective，没有把 old mean 的 accepted/iteration_limit 复制为新分支结果，也没有宣称已完成固定 g 精化。连续目标值区间、scalar carrier 误差、当前场的全域 metric 以及新场的完整几何仍需实际消费和记录。已准备的准确 Haar 连续消费源只提供可执行方法；未运行的源不能升级这些字段。

## 4. 可复现命令与实际后继

以下 {repo} 是阶段记录的 source checkout `dc7b8bccee2fa89e39879b0083808679becb88ec`，{work} 是同 run 的 research scratch；实际绝对 argv 已原样保留于第 9 卷。

```sh
python -u {repo}/topics/visible-flex-larger-amplitude/scripts/resume_20261126/frozen_material_haar_metric.py \
  --repo {repo} \
  --report {work}/mean-metric-design-amplitude-separated-SOC-v2-first/report.json \
  --bundle {work}/mean-metric-design-amplitude-separated-SOC-v2-first/final.npz \
  --moments {work}/haar-7ebb-fixed-target/moments.json \
  --out {work}/haar-7ebb-fixed-target/frozen-target.json
```

后继第 76 阶段才会用完整 b70 driver 对这个固定 Haar 目标读取真实新 baseline、求方向并做完整真筛；第 77 阶段读取它的实际报告。在这些返回前，不填初末 Phi、Pg、μ、线搜索结果或新末场 SHA。当前只保留真实冻结返回与未支付的范围，本条没有另排计算。
