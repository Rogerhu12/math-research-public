# 同一 Hold 度量的六点 Gauss 补采样：四个实际父的内部曲率

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**状态：实现已付，读出为数值证据。** [R655](../results/R655-node-midpoint-blind-space-and-Gauss-control.md) 已证明原节点／中点目标的 920 维纯竖直盲空间。本次把同一候选、同一全部自由变量、同一准确 Hold 标量扩展到每胞六个 Gauss 点，保留全部旧行。没有求解或更改四个候选，也未重跑旧 dense 大比较或已登记的连续审计。

## 1. 实际结果与影响

所有候选均为 J923/M160、原角数 2048、带准确重数的 513 个角。保留原 1845 个径向行块，再追加 922×6=5532 个点，共 7377 个径向行块／3784401 个实际角点／15108096 个完整角轨道点。原精确 lift 起点为符号网格节点 894，故本次没有穿界胞需要额外分片。

| 实际候选 | 旧点最大相对 Gram | 新 Gauss 点最大相对 Gram | 旧点最大绝对主曲率 | 新 Gauss 点最大绝对主曲率 |
|---|---:|---:|---:|---:|
| physical v1 六步，af89a441 | 0.5864263699217938 | 0.5866364329932279 | 7.211250722623774 | 7.211809155813935 |
| H² reach-screen 首步，e8b2ca40 | 0.33329462549082134 | 0.33426098300234397 | 7.958664294054651 | 7.966176659104062 |
| curvature QP 六步，0c535377 | 0.1801261226964055 | 0.17983931829794297 | 7.982277645632978 | 8.20029854656145 |
| curvature QP memory 十二步，c71db2bc | 0.07324989313371955 | 0.07270386385936001 | 7.972797448014856 | 8.220342313508384 |

最后两项的全点最大 Gram 仍发生在旧点，但内部曲率更大。六步 QP 的新曲率峰位于原胞 836、局部 u=0.8306046932331322、s=1.1740710114274446、φ=1.2670681307935396；memory 十二步的峰位于同一 s/u，φ=1.217980745581199。旧节点／中点的数值曲率筛选没有覆盖这两个点。

复用各自既有点对给出的直径下界，六步 QP 的 $D_{\rm point}=4.082530716916818$，memory 十二步的 $D_{\rm point}=4.091351989787761$。使用新曲率点读数，$0.03K_{\rm point}D_{\rm point}$ 分别为 **1.0043391211267636**、**1.0089694164332714**。故这两个候选不能继续标为通过当前数值必要曲率筛选；这不是严格舍入包围后的不可解证明，也不是 reach 证书。H² 首步的新曲率仍小于其原适用数值上限 8.03596581723495。四个候选在本次全部有限点上均未发现零面积，但这不证明连续浸入或嵌入。

原行前缀实际重新评价，读数与原各自结果相符。原三父报告内 `old_diagnostics_repeated=false` 的范围是“没有重跑旧 dense／CS 等诊断脚本”，并非“没有读取旧行”；本次明确读取旧前缀用于同点对照。后继复用入口把此范围写成 `old_dense_probes_repeated=false, retained_old_rows_read=true`。

## 2. 相同 g 的载体生成

原标量输入 `pulse-a5-complete-base.json.gz` 的 SHA-256 为 `826106b40f06ddece0500bd5ac7ea1a14ad4edbb9fab0664e3de46a76a76f196`；原 `fullclosed-hold-warm.json` 的 SHA-256 为 `fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692`。本次读取其中 `true_scalar_nodes`，不重新拟合标量或参考曲线。

每个新增观测的数值局部参数 u 按其准确 binary 有理值声明。对原准确节点 $s_i=\alpha_iS+\beta_i$，新点准确为

$$
s(u)=((1-u)\alpha_i+u\alpha_{i+1})S+
      (1-u)\beta_i+u\beta_{i+1}.
$$

由原 `FullHold.affine_time` 形成时间盒，再调用同一个 `FullHold.at_box`；取 a 盒中点作数值载体，用准确有理差的向上浮点载体记录绝对误差。旧 1845 个 a/time 载体及其误差字面保留，端点 1/R 保持，不对旧 a 做插值。

全部 a 载体绝对误差上界为 `2.4815220763730974e-13`；新增点最大为 `2.478933570171891e-13`；全部观测时间载体误差上界为 `1.1226466240975015e-14`。这些只包围固定标量和时间的载体，不是整个曲面的浮点误差证书。普通 double Gauss 节点近似理想代数根，准确积分恒等式的适用边界见 R655 第 5 节。

实际载体存于 scratch `work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz`，SHA-256 `71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`。该可重生数组不入库。

## 3. 完整实现接口

- [gauss_observed_closed_gram.py](../scripts/resume_20261120/gauss_observed_closed_gram.py)：SHA-256 `26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d`。
- [read_gauss_closed_gram.py](../scripts/resume_20261120/read_gauss_closed_gram.py)：SHA-256 `124bfa173faaa836ba0294cb79d0b82ffa004f61b9fd1bbc2d1ae646d3a588fc`。
- [read_gauss_candidate_with_carrier.py](../scripts/resume_20261120/read_gauss_candidate_with_carrier.py)：SHA-256 `95e55c8436e94c1d2520556b65e800af67bd58430d2c4d8f9fc761a9e9bf7b18`，复用载体只读新候选，不重新查询 scalar。
- [check_gauss_observation_maps.py](../scripts/resume_20261120/check_gauss_observation_maps.py)：SHA-256 `9b51a06315ce8c1d82f54e715a714f60edf029110acd9c5c6424c8395bd78d59`。

原 dense 源 SHA-256 `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d`；原 batch 源 `02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a`，未修改它们的字节。FullHold／integer oracle／Hold 三源依次为 `a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670`、`babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0`、`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。

创建方式：

```python
data = np.load(carrier_path, allow_pickle=False)
plan = module.ObservationPlan.from_arrays(data)
op = module.create(dense_source, mesh, a_old, radius, fixed_core,
    batch_source=batch_source, observation_plan=plan,
    a_observations=data['a_observations'],
    M=160, N=2048, width=.05, quarter=True, stage_block=64)
```

`observation_cells` 形状为 `(P,)`；`observation_weights` 为 `(P,3,6)`，六槽顺序是左 Y/U/A、右 Y/U/A，三行分别给值、一导、二导。`_stage_triplet(jets,start,stop)` 返回三个 `(B,n)` 数组；`stage_jets` 给单点完整 `(3,n)`。全部三 jet 余向量的散射为 `weights.T @ cotangent`，前后三行分别加回原两节点；多个观测共享同胞时须正确累加，不能覆盖。新 batch 两 jet 伴随使用 `np.add.at` 保留所有重复贡献。

原 affine 空间、全部 1332245 个原自由变量、非线性 core 链、ρ/Θ、完整解析 lift、角值与重数均继承原算子。`physical_jet_batch` 一次给 Fs/Fφ/Fss/Fsφ/Fφφ，用完整第一／第二基本形式计算实际点主曲率。

`residual/jvp/vjp` 仍只隐含原角轨道平方根权，径向权保持外部。`stage_quadrature_weights` 在旧点为零、新点为片长乘 Gauss 权；`stage_legacy_simpson_weights` 给原节点／中点的 composite Simpson 权。`mixed_stage_weights(t)` 明确返回两种权的正混合，返回的是平方行权，使用时取平方根并一致作用于残差、Jv、Jᵀ。本次读出同时给原旧行和、追加行和及 Gauss 积分型和，未把不同行数的 SSE 相减或称为优化进展。

## 4. 一次必要的新实现检查

在 J6/M3/N32 小模型中，原 lift 起点实际位于胞内；新增 map 包含该分片、重复胞索引、全部自由 core 与 H 的方向。一次检查结果：旧行残差相对差 0，complex-step 相对差 `2.0778056587432853e-16`，伴随内积差 `1.1185154919402138e-16`；新 batch 五种物理导数对原单点读出相对差均小于 `8.7e-17`，完整 quintic 三 jet 求值相对差 `5.434994194146246e-15`。实际检查通过，报告 SHA-256 `a0cbf5ae7ac5761f2d6b6ee9d757b4d46d470fdd8dbde4488d9178c76eb334ef`。该小检查针对新 Hermite 映射、散射与二导批量化风险；没有再使用旧大 warm 对照作为等待门。

## 5. 实际输入、运行和恢复参数

四个输入 bundle 的完整 SHA-256：

| 文件名 | SHA-256 |
|---|---|
| physical-fit-six-step.npz | `af89a4414fb0cee35d75dba5530e9b45b62abd248ddf7509cca92c2a9696a505` |
| integrated-h2-reach-screen-first/final.npz | `e8b2ca40e184157abba15c3c85ebdd651e38cbb4035edb2cfd652c8b57ad0637` |
| curvature-qp-six-step.npz | `0c53537771085266634794d82a0f133e2d1f149d1af7e0248e136d9ceee6812d` |
| curvature-qp-memory-twelve-step.npz | `c71db2bcf628d0126fe178037bf9f04cb22a3baeb593a196daf5ddec5a92dbca` |

第一轮本地 session10939 自然返回 0：一次 scalar 准备后依次读前三个父，各实际读出约 1.3 秒。参数 `--order 6 --angles 2048 --stage-block 64`，其余完整 CLI 在工作根 `/workspace/scratch/24b2ab87057a` 为：

```bash
python -u work/recover_evidence/read_gauss_closed_gram.py \
  --repo math-research-public \
  --batch-source work/recover_evidence/batched_closed_gram.py \
  --bundle work/geometry_path/physical-fit-six-step.npz \
  --bundle work/fullclosed_solver/integrated-h2-reach-screen-first/final.npz \
  --bundle work/geometry_path/curvature-qp-six-step.npz \
  --node-report work/fullclosed_solver/data/fullclosed-hold-warm.json \
  --scalar-input work/fullclosed_solver/data/pulse-a5-complete-base.json.gz \
  --outdir work/recover_evidence/gauss6-current-three
```

该报告 SHA-256 为 `4ab1e37ce4c9a2710bd2ff8213531a9e604f506f437a0bdb10a4dbd05f978e34`。source 在 scratch 的副本与第 3 节公开 source 同字节。

第二轮本地 session60567 自然返回 0，只追加读取新 memory 父，没有重读前三父或重新查询标量：

```bash
python -u work/recover_evidence/read_gauss_candidate_with_carrier.py \
  --repo math-research-public \
  --batch-source work/recover_evidence/batched_closed_gram.py \
  --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
  --bundle work/geometry_path/curvature-qp-memory-twelve-step.npz \
  --out work/recover_evidence/gauss6-memory-parent.json
```

该报告 SHA-256 为 `49cda756108f72ceaaf7accb38ab72876c8aa330ef6b46ce3e4a061227c97da7`。从零恢复时使用已刊原父生成链及其参数，读出只保存本文、完整小源码和身份，不把可重算数组／报告入库。

后续科学动作是把实际曲率扫描、活动约束和原 Gram 求解都接到这些完整观测点，保相同 g；本次没有给当前候选添加连续证书，也没有将更稀旧点的通过标签继续沿用到未检查的新范围。
