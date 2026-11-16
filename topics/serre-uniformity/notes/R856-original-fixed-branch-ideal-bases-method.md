# R856 执行契约：原 cusp 加 P0 的完整两图理想基

日期：2026-11-16。状态：**工程契约与真实输入闭包；新的有理域/多项式运算尚未执行。**

数学证明为 [R856 固定支撑及三标量入口](R856-original-fixed-branch-ideal-and-three-scalar-pole-source.md)，正式 SHA256 `e2f61908c8e17d8c16113c5c85eccabe71b4c0b7fd057b01daee9081d391b4e2`。其中后半段明确沿 $K\to L$ 扩张；本次实际 scope 只运行前半段的 $K=\mathbf Q(\zeta)$ 固定 21 点块，不运行原 $B$、$D$ 或五个 $\eta$ 的生成矩阵。

## 1. 首次实际目标

脚本 `scripts/R856_original_fixed_branch_ideal_bases.py` 的数学 RESULT 为 `R856-original-fixed-branch-ideal-bases`，FINAL 为 `p41-original-fixed-branch-ideal-bases-certificate.json`。CLI 为

```text
--config <expanded-job.json> --out <output-directory> --budget-minutes 300
```

`requested_stage` 固定为 `complete_two_chart_point_and_fixed_branch_ideal_bases`。所有新数学只在原公开仓库 Actions 执行；入口检查 `GITHUB_ACTIONS=true` 与原仓库身份。本地只做源码、schema、字节/SHA 和 AST 检查。

实际输出为每张图的两个完整 $K[x]$ 基：原点理想 $\mathfrak m_{P_0}$ 与原 $\mathscr C\mathfrak m_{P_0}$。不新增 cusp 评价秩、Fourier、primitive、一般导子或大乘法表。R856 的完整性是 R856 证明中的准确行核等式，而不是一个新模子式的概率判断。

## 2. 真实最小来源闭包

实际纯 IO 已取得 569 个原文件：

| 原 producer | 文件数 | 本次实际需要 |
|---|---:|---|
| R820 run43721747750 / source7890fde180ffabee056de2ce8dd241b189a893a2 | 554 | 两个完整 cusp index、544 条原准确列、有限代数接口、原 certificate/stage manifest/metadata 及 carrier 接续回执 |
| R805 run43705580592 / source9f960b8e0b2fa825ab1391e86db4e1383ffdd700 | 7 | 实际 free-basis、原 pencil、certificate/full manifest/run/core/public input |
| R837 run43770995901 / sourcefa17c77fe36fddd9df06677569984d1ea71a6b41 | 8 | 原146个P0值、原418个V2值及必要 metadata/stage manifest |

原 R805 free-basis 是11,649字节、SHA256 `74311a7a143fafc43a36d1a43f6146e6aa3cb28809a020e3fa1337fdc4e475c9`。它从 R820 实际输入载体取得，289个旧 carrier 成员逐一字节/SHA 验证后，仅保所需七个 R805 文件。原 R805 身份仍是真 producer，R820 只作 transport。

R820 源 artifact14164872449，19,737,373字节、ZIP平台 SHA256 `d09c6d70facec7870121cba30b13371bb672fbfd83cd9914e29ee1cfb1e9d11c`；full manifest SHA256 `2877dd3dbe604f07a58c8774897085d1de90a6faa38a6d2ed78a5bb9d7f79a8f`。此次 Range 只对选中原件逐 SHA，不称重新哈希整个 ZIP。

R837 P0 值21,063字节、SHA256 `2e41a7ec7a73401fd2f5d770c5ef6c4d8d722c38312026a5c6a0f906aedf58c7`。V2值按原 manifest 的实际 spec 绑定。每个 degree2 原 free-generator 的 `producer=R786`、file/bytes/SHA 必须与 R837 完整 V2 source_rows 的同一行吻合；不是只比较下标或维数。

expanded job 的 `sources[label]` 保存原 BASE 身份、certificate spec、原 configuration SHA、全部所选 file/bytes/SHA 及 `directory`。源目录只在本次 expanded job 出现，不进入数学身份。源码先逐 SHA 核全选择闭包，再核原 run/core/certificate/source tag，不导入旧数学核心。

## 3. 原正规基 P0 值

原 R805 实际铅笔是 $\tau=e_0$、$\sigma=e_1+e_{73}$。degree1 基是原 $e_2,\ldots,e_{145}$；127个 degree2 下标必须读取原 free-basis，不预填。

按照证明 FB.4 只作原值比：

$$
\beta_0(P_0)=1,\quad
\beta_i(P_0)=e_{i+1}(P_0)/\tau(P_0),\quad
\beta_{145+j}(P_0)=V_{2,d_j}(P_0)/\tau(P_0)^2.
$$

原 `integer_scale_already_in_source` 为字符串 `6724`，V2原值的尺度字符串为 `45212176`；准确读取这些实际字段，不额外缩放。原系数字段保持 `['1','zeta=(-1+sqrt(-3))/2']`。

消费者准确检查 $\tau(P_0),\sigma(P_0)$ 均非零，逐比值乘回，$z_0v_0=1$，以及全部272个 $\gamma_i(P_0)=v_0^{\epsilon_i}\beta_i(P_0)$ 的正反运输。所有域运算使用规范有理对及 $\zeta^2=-1-\zeta$；非零元素的逆必须两向乘回。

完成阶段 `R856-original-P0-normal-values.json.gz` 保存两图全部272个原值、两个基变量值、原框架/scale/source refs。这是新的准确评价，不能在本地先运行。

## 4. 两图完整基构造和输出

每图先读取 R820 已成272列，原对角次数必须是 $0^{271},20$。其 monic 下三角稀疏形由原 stage 及实际系数共同检查。新评价行

$$
r_j=\sum_{i,n}(C_j)_{i,n}\,x_0^n\beta_i(P_0)
$$

在当前图准确求得。选择实际最小 $r_k\ne0$，核逆和全部 $r_j/r_k$ 的乘回。该阶段不预填某个 pivot，不重新生成原 C 列。

点理想用 FB.6；固定21点理想用

$$
H_k=(x-x_0)C_k,\qquad H_j=C_j-(r_j/r_k)C_k\quad(j\ne k).
$$

每16列形成一个独立原子阶段，完整272列共17组。每列保存原 C 列 spec、原 pivot spec、最多两项的精确 change-of-basis 系数、完整稀疏原正规坐标列。全部新列的 P0 评价为零；原列乘回通过后才标 `complete=true`。pivot列另用完整逐系数线性因子递推验证，不只检查字符串或单点。

列稀疏格式为

```text
{normal_basis_row, power, coefficient_K_1_zeta:[[num,den],[num,den]]}
```

保持原列序0到271，不随 pivot 重新排列。每个 chart index 保存17个组、原 C index、评价行阶段、完整点理想基、实际 pivot，以及准确 determinant

$$
\det H=(x-x_0)P_{20}(x).
$$

该行列式由原已成 C 的 monic 下三角结构和实际两项变换认证，不重算272阶 determinant。点理想 colength 为1，固定21点理想 colength 为21。完整性依原多项式除法证明；不以这些预期数值单独代替完整列和证明。

两图粘合使用原 R820 的同一全局 cusp 理想，以及本次准确运输的同一 P0 评价。没有声称两图的基列在重叠上逐列相同，也没有新增不必要的272阶 Laurent/Hermite 消元。

## 5. 不可变身份与恢复

新数学 tag 包含本核心 SHA、R856证明/执行方法、FM、R820/R837证明的各 SHA；三组真实 producer/configuration/选择清单指纹；原 K 基、正规基次数、free-basis spec、两图、列序、pivot规则与16列块策略。预算、工作目录和载体封装不进入 tag。

所有数学工作文件均为输出根目录 `R856-*.json.gz`，以临时文件写全后原子替换；每个完成阶段含 `result/configuration/complete=true`。复用必须原 tag 和 source refs 完全相同。没有把旧 R820/R837 阶段改成 R856 身份。

运行预算可在已成组之间停止，已成 normal values、评价行、点理想和各列块均保留。预算 FINAL 的 `complete=false` 只记录历史进度；恢复不能据它旧的 manifest 快照拒绝更晚完成的阶段。真正 success FINAL 才要求全部阶段和引用完整。

`R856-stage-manifest.json.gz` 每次按当前实际完成阶段生成，排除自身。成功 FINAL 明列两点理想、两固定理想 index、全部真实 colength、原来源 audit 和 normal 值。主要真旗标是

```text
complete_two_chart_point_ideals_certified
complete_two_chart_fixed_branch_ideals_certified
same_original_global_fixed_branch_ideal_on_both_charts
```

而 `new_B_or_D_normal_coordinates_computed`、`new_Gamma_or_multiplication_table_computed`、`actual_eta_or_height_computed` 始终为 false。

## 6. 后继的实际输入边界

本次新块直接用于 FM 点理想幂、完整生成矩阵和有限余模 membership。后继 FB.16–19 可从同一个 canonical $B$ 与两阶导数取得原 $D/E_y$ 理想；那部分沿原 $L$ 扩张，准确源仍是原 U.1 solve DAG 和原 R813/806 叶，不能用原模列冒充特征零。

此次不展开任何大 $B$、不重复原 R842 短核、不计算全部乘法表、不改变五个原 $\eta$、$\beta$、非 $p$ 项、theta二挠或规定 splitting。公开 Actions 完成后才登记实际 pivot、运行时间、输出SHA与完整基成功结论。
