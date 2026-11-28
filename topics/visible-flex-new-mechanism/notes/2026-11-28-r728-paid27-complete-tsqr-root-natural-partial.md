# R728 自然保留态：完整闭纬圈的27次接受与已付TSQR根

**未冻结 E，未达到完成门。** [原 run 46162476275](https://github.com/Rogerhu12/math-research-public/actions/runs/46162476275) / job **141032646065** / head **95bbcc413114726105944fa8ed6d2891f4161580** 于 2026-11-28 16:48:56 UTC 自然 success。科学入口返回 paid_partial，恰停在原第2级、iteration10 的完整 TSQR 根 SVD 之前。时间分配不是研究完成；下单从原下一未付操作续接。

## 实际场和约束

源确为已付 R703 的39163字节原 literal、157原参数和 R687 原材料框，一次真实半频投影与全径向三jet Hermite 拟合已完成。其后空间依次为 24跨/K10 的1014列、24跨/K12 的1198列、48跨/K12 的2446列。已付两次自然嵌套延拓，旧源重建、投影和前两级不再执行。

第0级独立交叉度量峰从 .12039735970761645 到 .029740853320973107，9接受；第1级又8接受，最终交叉 .02967776213406613，因三种全列权模型均无可接受步结束该级。第2级当前10接受，总27，最后接纳 iteration9：

- 工作残差范数 .030832274301850735，独立范数 .031144405540474675。
- 成对物理相对度量最大值 **.025839833448117806**，其中镜相峰标 r=.21708403768134824、φ=3.1632498558422224。
- 实际主曲率绝对峰 **31.14829745481658**，r=.21848958333333335、φ=6.196522767954121。
- 角材料速率样本下界 .928304 一带，连续角向充分下界读数 .9137581042198415；该估计尚不等于严格全域证书。
- 真实内中心 ( .0007343197133077451, 0, −.0036979177481927224 )；当前 trust **.0007326308468874878**，最后 μ **56.34055948595833**。
- 指定 E 的径向积分 **.14836936883560958**，全方向必要长度 margin **−.0013794338605008505**。这是目标度量积分；未等距的实际母线长度不能用它代替。负 margin 明确阻止冻结。
- 两镜相的整壳有限读数通过；样本全 D 上估 .9833984192602818、支撑优势 .156948207925329、条件握持支撑差 .3024。这些条件量不越过未闭度量/长度和全域门。

真端六jet的最大差低于 3.42e−11。离散有限身份三径阶差逐项保存：mean J−target 最高 1.53e−13、mean V闭合最高1.13e−13、插值 Φψ−J 最高8.65e−12、插值 Uψ−V最高4.15e−11。端迹小不表示中央同g已解。actual_frozen_reference=null；continuous_certificate=false。

## 完整原算子与精确下一项

原2446个 float64 参数 packed SHA **6023803db8bf3462b999cf1ff01e2425e0c0596d72d343c2a3f34f8ddf5c1d0c**。paid_partial 原JSON literal **59209 B**、SHA **60bd3e148a75f25ff887d11276928c4db297716ca585aa3bea1485b501c94f39**。科学指纹 **f3a489a6aa5cda2bd1051682d7a3943c9b9701f654ded054667fbac741060df0**。

最新状态键 s02_i010_model_base、stage2、iteration10、accepted27、space[48,12]；当前完整原J和全部叶/合并QR已经支付。下一键 **s02_i010_model__variant0_QR_SVD**，unit=qr，context 为 full_TSQR_root_SVD，原根 **s02_i010_model_tree0_000_050**、variant0。保留583份必要块，7905份旧等价/已接纳前驱工作区已在原账标 retired，不能借此重复科学。归档包含原账、全部保留块和原R703 literal。

本次 elapsed **3085.9459010600003 s**，落账 cumulative **3085.940954607 s**；差为终态输出附近的计时，不盲相加。原失败首run的I/O1.86873602秒和含import进程1.026369秒仍在[原失败账](2026-11-28-r728-original-literal-order-and-first-natural-startup-failure.md)，没有原场/J/试步。当前全部原计数：

| 原计数 | 次数 |
|---|---:|
| TSQR_input_rows_including_merges | 4355240 |
| actual_local_complex_shape_states | 46814 |
| actual_nonzero_support_radii_for_columns | 1261388 |
| actual_physical_trials | 122 |
| all_material_parameter_columns | 46814 |
| complete_Hermite_QR_SVD | 3 |
| complete_TSQR_Householder_blocks | 2211 |
| complete_new_Fourier_physical_J | 29 |
| discrete_projector_radial_twojet_steps | 200064 |
| full_QR_SVD | 32 |
| full_frame_states | 1 |
| full_real_candidate_shape_states | 170 |
| half_frequency_integrated_radial_twojet_coefficients | 11462 |
| new_needed_paid_source_native_reconstructions | 1 |
| new_transported_grids | 1 |
| original_analytic_angle_integrals | 521 |
| original_numeric_anchor_comparisons | 1 |
| paired_complete_physical_reads | 158 |
| source_and_new_native_material_inversions | 152132 |
| true_nested_shape_prolongations | 2 |

[原 artifact 15272306550](https://github.com/Rogerhu12/math-research-public/actions/runs/46162476275/artifacts/15272306550)：visible-r728-paid-checkpoint-46162476275-1，**733240015 B**，ZIP SHA **60af03053fa50f4ba56720e6be9ff0421e9648fe6adf7d1da5f97e106d911f3b**，到期 2026-12-28 16:48:25 UTC。必要非再生付费状态保存于 Actions，不写大数组进git。

## 原身份续接

新增纯行政运输器先核自然完成的 run/job/head、artifact元数据和完整ZIP SHA，再逐项核原ledger指纹、583个原键、每一原块的长度/SHA、全部继承计数、真实最新态和下一操作。只恢复这份完成态；不读运行中日志，不重新下载历史日志，不执行科学导入。运输器单独以请求中的 transport_sha256 绑定，原15个科学 .py 和49b325d24b26b7e1374e611f601d7a56806221fa58b17fbe70c331b956757afc配置字节不改，故保留原科学指纹。原源码自己的 source-from-restored-checkpoint 分支读取保存的R703 literal。

接着仍由既有监督器实际pull双仓、比对规则、清除凭据，再从 full_TSQR_root_SVD 开始。旧完整J、TSQR树、源投影、每次真实试步和物理读数按原键加载；新操作仍即写paid ledger。三网真实同E、全部壳/端/材料/长度门过后，才允许原条件中的同E加2K/倍跨自然精化。R738使用另一真实宏观材料，独立求解，不借本算子或资格。

