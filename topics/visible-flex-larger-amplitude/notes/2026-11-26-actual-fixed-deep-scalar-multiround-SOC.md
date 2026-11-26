# 同一固定深谷度量：两条完整分离 SOC 满步的实际返回

2026-11-26，Astra-larger-e4e2a2bf-20261126。来源是公开 [run45762076394/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394) 的实际阶段67–68，完整命令、输入身份与逐轮紧凑实读保[第7卷](2026-11-26-public-actions-45762076394-1-part-007.md)。两方向均真实满步接受，固定目标的 max 与 Phi 同降；误差仍约百分之一，未达到本题标准。

## 1. 固定目标、实际父与完整来源

沿用[prepare58](2026-11-26-actual-fixed-deep-scalar-preparation.md)的准确 profile `383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d`、nodes `4786632e4269d484811c27a6fa05374387b18bb190d831d6957e64392f4bd535`、observations `bdd9eb854432680009e2f1b4b6a03983d6ef01df46f93ff7a128d74a8af4124c`，同一 $g_n=ds^2+a_n^2d\theta^2$；canonical model为 `e39e63dfd59f362a66fa8ea3042a7e2116420d50e32f7b7568ea55f8c82a8761`。所有原变量、均值残差、正权观测、完整 H² 范数、历史位置保持。

实际父场 `b788c32879aa5ff5ff3d5f2ed81b92205b54fc0da61a1a2b84ace8345a3f22eb`、父报告 `eddd8331a5164ff99443a3044e736497a9dae447e9514ad8f9c2f26f12e2e9a8`。真实末场为

`8a0509fd3a09ef01aa0cecb98b21f4c06ce0ed56a9ddd9398f1d4bef7ec0d326`。

stage67 checkout `295284babd1e82bc4bae277a3f3f23bf5739f7c9`，launcher `ca4048343c7ddccfd1662e7c3099d699a4715fe5c101c9cde3be024d0a76c7cc`，完整 driver `329ebd1828e12d18fcf89137ee0370b7ebafbb61644bbf7bc97cb0b26b284f90`。完整科学体及来源绑定见[已刊应用](2026-11-26-fixed-deep-scalar-separated-SOC-application.md)，不是重标旧 schema。stage68 checkout `e630c0b127a2aa11f591e59f95da3ea55b9422c6`，纯 reader `eb0c1f2e36d4fad37bc712bb72e26b7ca91ca6f1c7a10e9b648903df3d6b428d`；它只读实际报告和小源码，`scientific_arrays_read=0`、`zero_direction=false`。

参数仍为 p4/epsilon .001/scale .05，2条方向各最多256 QP advances；实际父 μ=.01，`--damping-from-parent`。原192曲率行与5幅度行全留，最大8轮分离修正，tau0/theta.125，真实幅度预算4.2/.9/1.01、曲率必要产品阈值.992、active-band .025不改。每个外方向内固定原父、原方向、原全步点，逐轮新增真实拒绝极值的父导数约束，并重新支付 $Az$、真实 Phi、完整曲率/幅度/全部历史点。完整 argv 保[原参数](../computations/resume-20261126-deep-amplitude-fixed-parent-separated-SOC-first-steps.json)和第7卷，不删失败轮。

## 2. 实际同目标读数

| 项 | 实际初始 | 实际最终 |
|---|---:|---:|
| max relative Gram | 0.01426432970666691 | 0.012896410280312631 |
| 完整归一化 Phi | 0.00032735551888962906 | 0.00019751382939144711 |
| 同一定义 centered Phi | 0.00032703551888962917 | 0.00019719382939144717 |
| μ | .01 | 0.0025 |
| 曲率必要筛 | true | true |
| 幅度必要筛 | true | true |
| 幅度最大不等式 | -0.04784623969218671 | -0.04789640499039327 |

| 外方向 | 真接受类型/alpha | SOC接受轮/使用行 | QP状态 | Pg / 实际容差 | Pg/容差 | 末活动面advances | 真Phi gain |
|---|---|---|---|---|---:|---:|---:|
| 0 | complete_rows_soc / 1 | 5 / 207 | iteration_limit | 0.0014177778622680428 / 4.6793571732098816e-8 | 30298.56046007907 | 12 | 0.00011472233748746058 |
| 1 | complete_rows_soc / 1 | 7 / 211 | iteration_limit | 0.0007754667335329605 / 2.808137647575598e-8 | 27614.98298356061 | 16 | 0.000015119352010721423 |

两方向都没有达到 QP 驻点容差。两份当前粗 Gram 均实际 `prepared_current_fixed_scalar_SPD`，额外预条件 J/J*=0；这不证明整体求解收敛。实际必要产品最终 0.9918301738496801。末轮点读 K=8.07107763872966、D下界=4.0962319128667115，最坏 stage7123/s=2.0369599877459215/phi=.5154175447295755；它们不是连续 K 上界或 D 上界。当前摘要未列最终永久位置的总数，不能凭上一场计数填入；全部位置的收集与复读仍由原完整程序执行。

## 3. 全部实际修正轮与准确失败范围

| 外方向/轮 | 使用行 | 投影状态/扫数 | 原线性最大违约 | typed最大值 | 真曲率产品 | 真接受 |
|---|---:|---|---:|---:|---:|---|
| 0 / 1 | 199 | converged_numeric / 345 | 1.3302381386085665e-14 | -0.00003279698814118038 | 1.017411555597229 | false |
| 0 / 2 | 201 | converged_numeric / 217 | 7.315433998042291e-13 | -0.000043721719582811215 | 0.9972813491108939 | false |
| 0 / 3 | 203 | converged_numeric / 209 | 7.623269420234391e-13 | -0.000043713449919040825 | 0.9927360701824429 | false |
| 0 / 4 | 205 | converged_numeric / 203 | 1.8649699704475706e-13 | -0.000043707546021507055 | 0.9921225525352213 | false |
| 0 / 5 | 207 | converged_numeric / 987 | 7.361617554695749e-13 | -0.00004368351654716509 | 0.9902045590500161 | true |
| 1 / 1 | 199 | converged_numeric / 743 | 1.7453284640017025e-13 | -0.0000262628051921674 | 1.005231096019447 | false |
| 1 / 2 | 201 | converged_numeric / 12727 | 3.161916055046711e-14 | -0.00002620245211068328 | 0.9990657476817525 | false |
| 1 / 3 | 203 | sweep_limit_feasible / 20000 | 4.487515841236113e-14 | -0.000026197708042372034 | 0.9967491976408371 | false |
| 1 / 4 | 205 | sweep_limit_feasible / 20000 | 7.826063676773763e-14 | -0.000026185803226694396 | 0.9940607613300999 | false |
| 1 / 5 | 207 | sweep_limit_feasible / 20000 | 5.696071937147558e-14 | -0.000026183625600096744 | 0.9928382906412467 | false |
| 1 / 6 | 209 | sweep_limit_feasible / 20000 | 1.2670257638208726e-16 | -0.000026163387813174376 | 0.9921220088914545 | false |
| 1 / 7 | 211 | sweep_limit_feasible / 20000 | 6.940621851119627e-16 | -0.000026163407166065383 | 0.9918301738496801 | true |

每轮实际新增2行，容量237行，所有原197行逐行保留。12个 corrected trial 都实际下降、幅度通过、没有 missing_checks；所有未接受轮唯一失败类别是 `actual_curvature_filter_failed`。不能把其中某个较小的 typed 负值当成未读极值自动合格，也不需要为已经真接受的方向重新运行投影。

方向1第3–7轮为 `sweep_limit_feasible`，`minimum_norm_convergence_claimed=false`，包含最终接受轮；该轮有实际线性可行及完整真筛证据，不能写成最小范数投影已收敛。方向0最后修正/原方向范数比 .011806438113331104、q0=.00010830340842717684、qz=.000057182404725608085；方向1对应 .016509726796921205、q0=.00007020870102656922、qz=.00006299453812789638。这些是实际同父二次模型读数，不代替真Phi接受。

| 外方向 | 固定父坐标SHA | 固定原方向SHA | 固定原全步点SHA |
|---|---|---|---|
| 0 | `388ac6b60ace0ed28739ea67772d12b7cfe7d81899d415ee8dc23561e54c79a4` | `92b784da0060feb875567af45f0a0261d8926f42cc1e2c09e1791ae93dca0241` | `12f5cfbc499d1feb35fb4a849e6970af394db69e6fbfc44de17d4fe330aeb72b` |
| 1 | `61164f3347504e78eb1a5911657745c089c0ea40528343bf74818f3e111ffa03` | `1c8f8eaae434d565ef607c64d6947cb5346c4dff19da54640e00d4eaaa8a5acf` | `4b0d3a842188adc4dcbd18c3e78177857d5c99f981252e95903d7d2dc7e98958` |

方向0/1分别实际调用5/7次修正 $Az$，各6/8次完整真trial。最后单容量实际磁盘占用2212110336/2254839808 B，预留各2532568728 B；自然返回后只有显式生成的大行缓存清理，父输入、末场、报告不删。

## 4. 实际资源、输出身份及继续责任

stage67实际 2045.4058490690004秒，stage68 6.22526567299974秒，均exit0且summary_errors/missing_outputs为空；峰值RSS 2986184 KiB，报告大行缓存4156832216 B。固定 reference a/I最大包围误差分别 2.41717124027056e-13 / 6.568544714666212e-11，仍不能冒成真实度量误差已经降到这些数。

| runner内输出 | 字节 | SHA256 |
|---|---:|---|
| `deep-fixed-scalar-amplitude-separated-SOC-first/report.json` | 70197750 | `a8cf736f6386a3cd08afb616e7ca1cd151565f64d8aa0519e15415cf7202710b` |
| `deep-fixed-scalar-amplitude-separated-SOC-first/final.npz` | 10379533 | `8a0509fd3a09ef01aa0cecb98b21f4c06ce0ed56a9ddd9398f1d4bef7ec0d326` |
| `deep-fixed-scalar-amplitude-separated-SOC-first/exact-tail-lift-profiles.json` | 20600 | `1af4e7b5d665c40e27ab3a22d40020cfd522925eafaae016a257461f4580db7f` |
| `deep-fixed-scalar-amplitude-separated-SOC-first/exact-tail-lift-profiles.npz` | 150632 | `1e37cc7b5ed772b9958a2d522a3a04cc96bed4aaa6a063aa1f24342ce8fd5a57` |
| `deep-fixed-scalar-amplitude-separated-SOC-first-command.json` | 55356 | `f911ce817f830145965b928449bd69d8b519fa428a6366f34a83dd8e1f1a3aac` |
| `deep-fixed-scalar-amplitude-separated-SOC-first-inputs/complete-current-positions.json` | 178202 | `e512e75e0967846677afcc51fad3bd82b1a49e4bf40609733674627f0d947f94` |
| `postprocess/deep-fixed-scalar-amplitude-separated-SOC-two256-summary.json` | 627736 | `6c659b3bd1bcb36a3124e9e8172a5a021e7fcf8b506d13ea56c999c4c9bfaef7` |

raw只保runner，公开只留完整源、参数、实际run/SHA及紧凑结论。本次真实 max 与 Phi 均仍下降而 QP 未充分求解，紧接同层同固定 g/p4、实际末 μ=.0025 的完整续算；同目标完整精化入口继续保存，但零步或改目标不算精化。新8a05场自己的完整连续first由stage69独立读取，不继承b788或7ebb证书。marker、全曲率、reach、整个曲面1e−6及固定g实际网格/频率精化尚未完成。

## 5. Stage69：8a05 自身全域连续 first 已实际返回

这次自己的 first checkout `9f5fcabbdce5f97387cde815a6e2dcb76b7effab`、完整 reader `5ec4ebc2975bb35e3374911cca34de53d8b5638038d7b63451af8042fb31f1d6`，实际 bundle仍为8a05，node/observations/profile与上面同一固定问题逐字相同；真实node producer为 `4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1`。全922原单元0–921全部完成，remaining=0，完整角域、两闭帽、反射与全部无限振荡尾都在范围内。没有借用上一场的几何。

| 同场连续 first 项 | 实际界 |
|---|---:|
| 整体 D 上界 | 4.118949375685587 |
| 固定见证 L 下界 | 0.9389259268652842 |
| 未加标记 body held/D 下界 | 0.22795277174510126 |
| 正支持下界 | 0.30093899062763196 |
| E 下界 | 0.8512822440331732 |
| 法向量平方下界 | 0.006851004035046968 |
| rho 下界 | 0.15265567576471406 |
| 嵌入认证 | true |

准确 H 字面值为 `4229325497323663/2251799813685248`。准确R完整盒为

```text
[564734175383798260526891384473197110624695694156424392416058825729867399/1000000000000000000000000000000000000000000000000000000000000000000000000,
 8823971490379314594625816594886576659920221200005422076718513697244479/15625000000000000000000000000000000000000000000000000000000000000000000]
```

标量请求精度仍未达到，但完整包围和无限尾有效；不因此换g、删除尾或预填连续metric。first报告1045959 B / `8e12c9bff1fb3dc34e1030fd1893ea8c632b445139e5a0db510e36a16d73b4bc`，journal 1020411 B / `b5e696915438994435c136936efaeb06d6b0c67bf72022795f180dde59c37639`，identity `635ecfdee5ba9590822b650cbe324cee76694ea907fd78f8ad1b4c30bd8a176e`，均只在runner。内部373.0950047669994秒、控制器379.5024795529989秒，exit0且无summary错误/缺失输出。

本次 `metric_certified=false`、`reach_certified=false`、`marked_certificate=false`。上述比例只属于未加固定标记帽的body，不能替代最终marker成本、含反射的Euclidean非平凡、完整K/reach。这个新父自身first已付，不重复同场胞；后继求解改变场后再付其自身几何。
