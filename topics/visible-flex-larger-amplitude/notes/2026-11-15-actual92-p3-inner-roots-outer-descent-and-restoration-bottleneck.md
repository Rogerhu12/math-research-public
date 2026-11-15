# Actual92：近似 p3 内层根、两次完整三方程下降与末轮恢复阻塞

类型：公开 Actions 实际数值证据的完整原件读回；不是新的根存在证明、原 BVP 接受或非零尾端解。

作者：ChatGPT / exact_refinement。日期：2026-11-15（UTC）。

## 1. 实际完成了什么

Actual92 的科学、原件保存与发布步骤全部成功，生产者报告 `diagnostic_completed=true`；同时 `success=false`，低三根没有解出。它从 actual90 的真实末参数出发，首先取得一个通过原完整三方程 merit 与 .2 Armijo 检查的 p3 投影，随后两次接受外层更新。第三次外层迭代用尽 20 档回溯，每一档都因内层第三方程没有满足所声明的 `1e-8` 条件而未进入外层 merit 接受分支。

最后接受的参数是：

```text
p = [0.6929598480979777, 0.1236195236907518, 0.5225323995570981]
unit d = [-233.46281549983243, 126623.86001929421, -7.863297485366516e-09]
full original three-equation merit = 8016828215.536017
```

这不是“完整三方程没有任何下降”：初始 merit 为 `11213045978.398226`，两次外层更新确实被原完整三方程判断接受。也不能把末轮写成“所有试探点都使完整 merit 上升”：末轮的 20 个内层末点保存了更低的完整三方程 merit，但都没有成为这个算法允许检验的 usable 内层候选。正文下面完整保留这 20 个数值与失败原因。

本地工作只读取原 JSON/gzip、逐字面比对、binary64 打包及 SHA256。没有重算方程、RHS、Jacobian、SVD、Schur 补、范数、merit、比例、参数更新或区间包络。全 39 份内层报告及 1,425 条原事件分别完整保存在[内层原记录](2026-11-15-actual92-original-inner-reports.json.gz)和[原求值事件账](2026-11-15-actual92-original-evaluation-ledger.jsonl.gz)；[完整 status 的无损压缩副本](2026-11-15-actual92-original-complete-status.json.gz)解压后就是原 498765 B 文件。[逐字面读数](2026-11-15-actual92-literal-readout.json.gz)仅组织这些已存字段，没有新增科学量。

## 2. 真实运行、父件与原模型身份

| 项目 | 原件身份 |
| --- | --- |
| 运行 | [43672921972](https://github.com/Rogerhu12/math-research-public/actions/runs/43672921972)，job `132686715503`，全部 success |
| 触发源码 | `1755a4f414a77d41d85eae9a0e1625f55a74be90` |
| Artifact | `14144239294`，`visible-mainline-smallcoreresonance-43672921972-1`，676336 B |
| 原 ZIP SHA256 | `f10832bad2ebf3b48a4da501bc0a50b7556e7a839eb86ddd532cab497338d74a` |
| 新入口 | `geometry_20261115_small_core_p3_inner_root_search.py`，43598 B，`3b48efd71eb696fef66acbe7fbd163bb8dc8ca63287bfa8c4e873a2600fbf9d9` |
| 原完整 status | `small-core-p3-inner-root/p3-inner-root-status.json`，498765 B，`e822be884ac07e2b2c46ac7aba7f589ba5233e86cdbb33ad9c95108cc8dca01e` |
| 原事件账 | `large-arrays/original-model-evaluations.jsonl`，2039245 B，`e1b087a4c9581c46226292a9bede43af1e93466457e6477a19222516f94bd0f1` |
| 原运行时间 | `16.914463108000007` s |
| 环境 | Python 3.12.14；NumPy 2.3.5；SciPy 1.17.0；python-flint 0.9.0；BLAS 单线程 |

根代理已完成原 ZIP 的官方元数据、大小、SHA、CRC 和完整下载核验。本审计不再次下载，不把解包文件哈希冒作另一遍完整 ZIP 核验。

父件是 actual90 完整 `damped-resume-status.json`，60951 B，SHA256 `5a4d157aa0bcada3cdd1d319adb419f23b94f52bfc1c945a3c6afe1207cb2f5a`。包中的两份父 status 与真实公开 Git 原件逐字节相同。只使用了父 `final.parameters`：

```text
[0.04241436079648833, 0.02766947731512731, -0.10800335072481342]
```

父 η=0.01 与本轮新二维 η=0.1 属于不同算法，不能描述为固定同一方向模型的单参数对照。父保存的 Jacobian、merit、状态和 FD 均未被重贴成当前值。当前 initial 的一次原 evaluate、完整原 Jacobian 和 FD 由本次调用重新产生，事件账的 `fresh-parent-state` 与 `fresh-parent-original-description-FD` 给出了直接绑定。

四个原数学输入完整 bytes/SHA 在本地只读核过；没有重新执行它们：

| 输入 | 原 SHA256 |
| --- | --- |
| accepted | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| true T112 zero anchor | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail config | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

本轮 71 个 request source pin 的完整源文件逐 SHA 核对。实际生产者登记的 12 源全部属于这 71 件，名单如下；完整 SHA 列表在字节审计和 literal 中保留：

| 完整源文件名 | SHA256 |
| --- | --- |
| `geometry_20261114_constrained_collocation.py` | `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8` |
| `geometry_20261114_constrained_trust_warm.py` | `5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2` |
| `geometry_20261114_direct_operator_cell.py` | `1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce` |
| `geometry_20261114_full_dn_augmented.py` | `f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e` |
| `geometry_20261114_full_dn_boundary.py` | `4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2` |
| `geometry_20261114_full_prefix_operator.py` | `a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703` |
| `geometry_20261114_lifted_modes_profile.py` | `13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5` |
| `geometry_20261114_physical_test_boundary.py` | `3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681` |
| `geometry_20261114_small_core_resonance.py` | `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` |
| `geometry_20261115_small_core_damped_resume.py` | `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a` |
| `geometry_20261115_small_core_damped_search.py` | `1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728` |
| `geometry_20261115_small_core_p3_inner_root_search.py` | `3b48efd71eb696fef66acbe7fbd163bb8dc8ca63287bfa8c4e873a2600fbf9d9` |

其中 `small_core_damped_resume.py` 和 `small_core_damped_search.py` 是父件的不可变来源身份，本次没有执行它们的方向搜索。真正执行的是原 `3b9c45ab…` 的方程、参数 Jacobian、description/FD、Arb 和圆形参考函数，加新 `3b48efd7…` 的内层/外层流程。恢复原 78 个公开数值源的完整运行收据，与冻结 `source-dependencies.json` 的 78 项逐项一致；这 78 件没有在本审计中重新恢复 payload，不能把它们混同于已另核完整源字节的 71 件。

## 3. 实际算法与原接受责任

本轮保留 699 个原网格节点、112 个场/尾端模式和完整保存的 112×112 零态真实斜率 Jacobian。所有条目都已读取；其 off-diagonal 原词全部精确为零，没有阈值化或 ready graph 替代。这允许本轮使用低三 unit 方程；它并不支付当前参数下高 109 自由核的 Schur 消去或非共振证明。

原方程记为 $r=(d_1,d_2,d_3)^T$，完整参数 Jacobian 为 $J$。内层固定 $(p_1,p_2)$，每次仅更新 $p_3$；每个 Newton/验证点重新取得该点的完整 3×3 原 J。内层一条更新只在实际原域返回且 $|d_3|$ 严格减少时采用，最多 12 次 Newton 更新、每次 20 档 $\alpha=2^{-k}$。usable 的声明还要求实际 $|d_3|\le10^{-8}$、完整 J 有限且 $J_{33}\ne0$。

内层记录的 `accepted_outer_state=false` 恒真：其更新是求根探针，并不自行接受外层状态。达到 usable 条件后，当前点保留实际非零 $d_3$，不覆盖为零。外层使用：

$$t=-J_{3,1:2}/J_{33},\qquad K=J_{1:2,1:2}+J_{1:2,3}\,t,$$

$$\min_z\;\left\|\begin{pmatrix}KD^{-1}\\0.1I_2\end{pmatrix}z-
\begin{pmatrix}-r_{1:2}\\0\end{pmatrix}\right\|_2,\qquad
v_{1:2}=D^{-1}z,\quad v_3=t\,v_{1:2}.$$

这里 D 是该实际 K 的原列尺度；计算采用 4×2 增广最小二乘，没有形成正规矩阵。完整原斜率仍读为 $r^T Jv$，原非线性 merit 为 $\frac12\|r\|_2^2$，阻尼罚项没有加进真实 merit。每个外层试探先取预测 seed，再重新做 p3 内层恢复；只有 usable 末点才进入原完整三方程 `.2 Armijo` 判定。外层最多 8 轮、每轮 20 档，本轮第三轮便停止。

这只是近似内根处的切向算法模型；原记录明确没有证明精确 IFT 分支。尤其实际内层恢复后的参数位移通常不等于 `alpha*v`。本稿把 $r^TJv$ 称为保存原线性模型的方向斜率，不把它冒作已证明的精确非线性恢复曲线导数。相关条件与尺度区分见 [R278](../results/R278-finite-resonance-projective-normalization-and-local-elimination.md)。

## 4. 初始 p3 投影：真实原三方程接受

本次 fresh parent 的原残差是：

```text
[229.78524027424547, -149015.7614289278, 14843.921358477846]
```

初始内层 call 1 的三次实际更新均采用 α=1，随后第四次完整 J 调用用于根处验证：

| 内层当前索引 | 原 p3 | 原 d3 | 保存的 p3 Newton 方向 |
| --- | --- | --- | --- |
| 0 | -0.10800335072481342 | 14843.921358477846 | 0.00020616520654615918 |
| 1 | -0.10779718551826725 | 11.841992891936725 | 1.6473464292256488e-07 |
| 2 | -0.10779702078362433 | 7.570770414569837e-06 | 1.0531755627434699e-13 |
| 3 | -0.10779702078351901 | 7.66934330559616e-09 | 验证点，无新方向 |

投影实际总位移为 `[0.0,0.0,0.00020632994129440863]`，并单独接受完整三方程责任：原 merit `11213045978.398226`，fresh-parent J 对该实际总位移的原斜率 `-219614749.28446636`，原 Armijo bound `11169123028.541332`，投影后原 merit `11103779210.306698`。因此 `adopted_as_outer_baseline=true`。

投影后的完整 unit 残差是 `[229.80698277716525,-149021.82930485072,7.66934330559616e-09]`。这里只把第三分量压到了声明阈值，没有宣称另外两分量同时改善或根已经存在。

## 5. 三个外层完整模型与真实接受

| 外层 | 保存的起点 merit | 原完整 $r^TJv$ | 实际外层 trial 数 | 接受 α | 接受后 merit |
| --- | --- | --- | --- | --- | --- |
| 0 | 11103779210.306698 | -22096861360.409607 | 12 | 0.00048828125 | 11097889913.755127 |
| 1 | 11097889913.755127 | -22085295041.22349 | 6 | 0.03125 | 8016828215.536017 |
| 2 | 8016828215.536017 | -15953879456.811777 | 20 | 无 | 保留原起点 |

外层 0 的 usable 内层候选分别出现在 trial 7、8、10、11。前两点实际 merit 上升；trial 10 的实际 merit `11101759888.159971` 虽比该轮起点低，却没有达到原 bound `11099463417.072243`。trial 11 的 `11097889913.755127` 通过原 bound `11101621313.68947`，所以接受。没有把“mere decrease”替换掉原 Armijo。

外层 1 的前五个预测 seed 均触发原 node/mid scalar domain failure；trial 5 的内层 call 19 得到 usable 点，实际 merit `8016828215.536017` 通过原 bound `10959856819.74748`，成为最后接受点。其预测 seed 的 p3 是 `0.05175645831378087`，内层实际末 p3 是 `0.5225323995570981`。call 19 完整记录了这个较大的恢复变化、九次完整 J 和所有原域拒绝；不能把它描述成已证明局部唯一 IFT 分支上的小投影。

三次保存的 lifted 原参数方向分别是：

```text
outer0: [-16.0556592689652, 2.8730898407384204, -3.353109602252214]
outer1: [21.068325269725243, 3.0255094552584456, 5.149240105274236]
outer2: [-0.09361803547736551, -0.4794508453238373, 0.03459895985808484]
```

原 full-J action 的第三分量依次为 `2.8909455408288403e-08`、`-5.772922553027825e-08`、`-8.86965075933326e-09`。这些是本次浮点原动作读数，没有被强行改写为理论切向式中的零。

### 5.1 同模型二维谱并未成为新门

本轮另外保存了三个实际尺度 Schur 矩阵的直接二维 SVD；这是新原二维模型自己的谱，不是 actual88 的旧三维谱：

| 外层 | 尺度 K 的两个奇异值 | 原前两残差在两个左奇异方向上的投影 | η=.1 保存的移除因子 |
| --- | --- | --- | --- |
| 0 | [1.4142134356196223, 0.0005987595043142697] | [149021.29270460573, -461.2388336053506] | [0.9950248747345041, 3.585000913143535e-05] |
| 1 | [1.4142127536635807, 0.0015124071122288123] | [-148982.28629386632, 241.2429537106605] | [0.9950248699602042, 0.00022868521842063513] |
| 2 | [1.4142134041266974, 0.0006690204617095923] | [126624.04539268109, -86.94517980843463] | [0.9950248745140257, 4.475683455471249e-05] |

完整 K、列尺度、增广矩阵/RHS、z、v、Jv、左右奇异向量与过滤后坐标都在 literal 中。它显示此二维模型仍有一个弱方向，但不单独解释本轮全部非线性回溯，也不使末轮已失败的 inner usable 判据自动消失。

## 6. 全 39 个内层结果

下表 d3、merit 均直接取每份 `last_probe`；“seed 域失败”没有成功末点，不填造数字。“可用”仅指该内层报告的 usable 标志，不等于外层接受。总计：6 个 usable、9 个 seed 原域失败、1 个 12 次更新预算用尽、23 个最后内层回溯未能严格减小。

| inner call | 原上下文 | usable | 原最后 d3 | 原最后完整 merit | 原停止类别 |
| --- | --- | --- | --- | --- | --- |
| 1 | `initial-p3-projection` | true | 7.66934330559616e-09 | 11103779210.306698 | 达到阈值及有限非零 J33 |
| 2 | `outer-0/trial-0` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 3 | `outer-0/trial-1` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 4 | `outer-0/trial-2` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 5 | `outer-0/trial-3` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 6 | `outer-0/trial-4` | false | 2.4911659375695394e-06 | 1267728367593.8555 | 12 次更新预算用尽 |
| 7 | `outer-0/trial-5` | false | -3.387120706323937e-07 | 1827926942.3487906 | 20 档内层回溯未严格减小 |
| 8 | `outer-0/trial-6` | false | -6.152512115466073e-08 | 9893251365.454515 | 20 档内层回溯未严格减小 |
| 9 | `outer-0/trial-7` | true | 7.282183562217458e-09 | 12729624067.192156 | 达到阈值及有限非零 J33 |
| 10 | `outer-0/trial-8` | true | 2.4118168646714054e-09 | 11354831568.56619 | 达到阈值及有限非零 J33 |
| 11 | `outer-0/trial-9` | false | -1.2526601617061516e-08 | 11139454010.57229 | 20 档内层回溯未严格减小 |
| 12 | `outer-0/trial-10` | true | 7.056618096633197e-09 | 11101759888.159971 | 达到阈值及有限非零 J33 |
| 13 | `outer-0/trial-11` | true | -3.3766514158871906e-10 | 11097889913.755127 | 达到阈值及有限非零 J33 |
| 14 | `outer-1/trial-0` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 15 | `outer-1/trial-1` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 16 | `outer-1/trial-2` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 17 | `outer-1/trial-3` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 18 | `outer-1/trial-4` | false | 无末点 | 无末点 | 原 seed scalar 域失败 |
| 19 | `outer-1/trial-5` | true | -7.863297485366516e-09 | 8016828215.536017 | 达到阈值及有限非零 J33 |
| 20 | `outer-2/trial-0` | false | 6.186601208667958e-08 | 3483426293.632159 | 20 档内层回溯未严格减小 |
| 21 | `outer-2/trial-1` | false | -1.4999553547574013e-08 | 3363859873.8268824 | 20 档内层回溯未严格减小 |
| 22 | `outer-2/trial-2` | false | -1.124915613211902e-07 | 4920474824.949216 | 20 档内层回溯未严格减小 |
| 23 | `outer-2/trial-3` | false | -1.3014961171634032e-07 | 6252478201.688606 | 20 档内层回溯未严格减小 |
| 24 | `outer-2/trial-4` | false | 2.228434184637848e-07 | 7077898908.677434 | 20 档内层回溯未严格减小 |
| 25 | `outer-2/trial-5` | false | 1.4647801434633512e-07 | 7532894238.799508 | 20 档内层回溯未严格减小 |
| 26 | `outer-2/trial-6` | false | 2.5019127420592563e-07 | 7771213905.447669 | 20 档内层回溯未严格减小 |
| 27 | `outer-2/trial-7` | false | 2.4002876394813022e-08 | 7893105848.53024 | 20 档内层回溯未严格减小 |
| 28 | `outer-2/trial-8` | false | 2.2667065392289326e-07 | 7954737830.845463 | 20 档内层回溯未严格减小 |
| 29 | `outer-2/trial-9` | false | -7.336020784853153e-08 | 7985725674.707881 | 20 档内层回溯未严格减小 |
| 30 | `outer-2/trial-10` | false | -5.109569565977384e-08 | 8001262602.084073 | 20 档内层回溯未严格减小 |
| 31 | `outer-2/trial-11` | false | -1.800587807066628e-08 | 8009041822.322072 | 20 档内层回溯未严格减小 |
| 32 | `outer-2/trial-12` | false | -1.3096087690851743e-08 | 8012934122.193339 | 20 档内层回溯未严格减小 |
| 33 | `outer-2/trial-13` | false | 1.1702114451235535e-07 | 8014880944.680111 | 20 档内层回溯未严格减小 |
| 34 | `outer-2/trial-14` | false | -5.723657916026359e-08 | 8015854524.067162 | 20 档内层回溯未严格减小 |
| 35 | `outer-2/trial-15` | false | 1.961018517042043e-07 | 8016341355.782302 | 20 档内层回溯未严格减小 |
| 36 | `outer-2/trial-16` | false | -2.876202839542652e-07 | 8016584782.156981 | 20 档内层回溯未严格减小 |
| 37 | `outer-2/trial-17` | false | -6.747179638957879e-08 | 8016706497.975718 | 20 档内层回溯未严格减小 |
| 38 | `outer-2/trial-18` | false | 1.9698801306290703e-08 | 8016767356.535457 | 20 档内层回溯未严格减小 |
| 39 | `outer-2/trial-19` | false | -3.3492956272133945e-08 | 8016797785.963466 | 20 档内层回溯未严格减小 |

全 39 份原报告包含 161 个内层完整 J 记录、698 条内层 trial 和 132 个采用的内层更新。额外的 fresh initial 与 final description 各提供一次完整 J，因此原事件总计 163 次 J 返回；没有 J 例外。原 evaluate 共 1262 次：773 次实参数、489 次复数步探针，1213 次返回、49 次原 scalar domain 例外。49 个例外均有原类型、参数与上下文，不被抹去或改成外层接受。

### 6.1 最后外层为什么停

最后外层的 20 个内层调用是 20–39。它们的所有实际 evaluate 都正常返回原域；各自最后失败的是严格 `abs(d3)` 减小条件，没有任何 usable 返回。因此生产者不填写这些 outer item 的 `actual_merit/actual_projected_point` 接受字段，而把末点只保存在原 `inner.last_probe` 中。表中的 merit 是这份探针记录，不是新接受点。

例如 call 20 的末点 d3 为 `6.186601208667958e-08`，merit `3483426293.632159`；call 21 的末点 d3 为 `-1.4999553547574013e-08`，merit `3363859873.8268824`。两者都有更低的完整三方程原 merit，却被当前算法的前置 usable 条件挡在外层判断之前。不能将它们偷换为本轮已接受状态；也不能将此次阻塞写成“没有可产生下降的有限点”。

### 6.2 有直接字节证据的具体停滞

对 call 21 最后内层步，已保存 p3 是 `0.5397924553658555`，方向是 `1.9392127102440378e-17`。其全部 20 条已保存 trial parameters 与当前三个参数逐 binary64 词相同，每次原 d3 都是 `-1.4999553547574013e-08`。call 39 最后内层步也有相同现象：p3 `0.5225324655493556`，保存方向 `1.7951562530441356e-17`，20 档参数词完全不变，d3 恒为 `-3.3492956272133945e-08`。

call 20 的保存方向是 `-1.1638712272146006e-16`。前两档返回另一个已保存参数词 `0.574063864304236`，d3 为 `-6.407261444671408e-08`；余下 18 档返回当前词 `0.5740638643042361`，d3 恒为 `6.186601208667958e-08`。这些字面及 word equality 在 literal 的 `final_inner_stored_word_equalities` 中完整保留。

这些事实足以解释这些具体末步为何没有严格减少 $|d_3|$；本地没有计算 ULP、舍入误差界或相邻词的科学比率。它们不证明一个普遍精度下界，不排除其他参数点、其他可表示的更新或不同算法求得原根。原根停止阈值、完整 112 行候选标志与最终 BVP 门均不因此放宽。

## 7. 最后原检查及其准确范围

最终原完整 112 行右端的前三个数为：

```text
[-107.83819029459062, -7558.74958985967, -1.236901147098294e-10]
```

其后 109 项是保存的有符号零，`high_right_leak_max=0.0`。这只报告此低三候选在真实对角零态 J 下的完整右端；`high_free_core_Schur_elimination_computed=false`、`high_mode_nonresonance_proved=false` 仍保留。前面实际 unit 与完整右端不能混用同一阈值：`original_unit_stopping_tolerance_met=false`，`low_mode_candidate_has_small_full_recorded_right_residual=false`。

final description 在最终接受参数处重新调用了原 J，完整值是：

```text
[[-1107.9006322728314, -114.81514473164688, -375.0129361140701],
 [701367.4128892582, 196645.73358820114, 981203.2544866957],
 [54018763.03371744, 124091399.49520981, 1865745592.4775739]]
```

该 J 与此前最终 usable 根处的完整 J 逐词相同，同时有独立 final event；它不来自 actual90 父报告。原数值奇异值为 `[1870648107.4858866,685087.0896455426,121.78831668458724]`，条件读数 `15359832.194171578`。原三档参数实差分检查的最大相对读数依次为 `3.5830851633286135e-09`、`9.848101438942133e-10`、`9.062838304550438e-10`。这些是普通浮点数值检查，不是外包的导数误差或横截性证明。

最终完整标量域 Arb 报告：160 bits、最大深度 14、957 个 leaf、514 个 split、unresolved 0，覆盖 `[0,5113846463878377/2251799813685248]`，`complete_declared_real_expression_domain_certified=true`。每片原区间端点、半径/返回 ap 包络和布尔标志完整保留。它包围的是声明的精确实表达式，明确没有包围 literal binary64 evaluator roundoff，没有证明 `returned ap` 就是有限 Gauss a 的导数，也没有支付 C² 接口或整个圆形 Frenet 场的连续域。

最后 `complete_reference_check` 重新计算的是**零核圆形参考**：它按原冻结源码把三个固定 core target 设为 `[0.0,0.0,0.0]`，并明确 `original_large_core_targets_retained=false`。本稿没有将该 reference 冒作原非零目标解。参考的原 node/mid/RMS 域失败均为零，4096 角 rho guard true，原 boundary/left/constant 残差读数为零，physical collocation max 为 `4.2809722780590143e-16`。九个原 full-FFT tangent 检查覆盖节点 0、349、698 的低三单位模态，末节点三项相对读数为 `2.8117524939110443e-16`、`1.224124164929413e-15`、`7.144396619629591e-15`；均比较了全部 physical rows。

完整参考导出了 699×453 的 states 与 RHS、699×3×2 的**低三**单位模态及其 RHS，而不是 112 个单位模态。其原 compressed SHA 为 `cfdc0e76d8c8bc47ba15ba0eb931c3ba75152af6c72799d4d3282d865b2c1359`。原 `full_native_tail_at_nonzero_height_computed=false`、`new_coupled_finite_acceptance=false`、`complete_closed_surface=false` 全部保留。

## 8. 字节审计、完整保存及下一算法含义

[纯字节审计](2026-11-15-actual92-byte-audit.json.gz)的 10278 项检查全部通过。范围是完整 51 个 artifact 成员及一件本地运输 marker、71 个 source payload、生产者实际 12 源、四个数学输入 payload、两份完整 actual90 父件、39 个内层原报告、全部 1425 个事件及其当前点关联。78 个恢复来源是完整原收据/冻结 manifest 核对，未在这里再次恢复所有原文件。

额外按实际 shape 打包并哈希了 200 个数值数组身份，包括全部 163 个实际参数 J、三次原二维 direction model 的已存数组、原完整 112×112 零态 J、两端完整 112 向量以及圆形参考的全 states/RHS/低三模态。所有 float 比对区分正零和负零。没有用重新求解去验证报告，更没有增加候选接受门。

| 本附记文件 | 字节数 | SHA256 |
| --- | --- | --- |
| [2026-11-15-actual92-byte-audit.json.gz](2026-11-15-actual92-byte-audit.json.gz) | 65135 | `dca47829ec3202809cb96e615d0909796d0fa4bbc4471cdd944bdf2a79f31409` |
| [2026-11-15-actual92-literal-readout.json.gz](2026-11-15-actual92-literal-readout.json.gz) | 147957 | `1682edcc631e7dde0728852807d194d2f2307ac9d9f97fe5112a53b241253a4c` |
| [2026-11-15-actual92-original-complete-status.json.gz](2026-11-15-actual92-original-complete-status.json.gz) | 33660 | `a2a8d60da59d332dcc833f696f7b7c16169142ca56a88c4fa4e093bce365a90f` |
| [2026-11-15-actual92-original-evaluation-ledger.jsonl.gz](2026-11-15-actual92-original-evaluation-ledger.jsonl.gz) | 106191 | `e9013c86fc64c51fa7efce3abdfe07edf52fa67f0b4fc2012d6e928b0bc374e5` |
| [2026-11-15-actual92-original-inner-reports.json.gz](2026-11-15-actual92-original-inner-reports.json.gz) | 129472 | `4885698c1582054dc0082ba813b2df95b729ae2a3783f0e10e253bb18fec7f5d` |
| [2026-11-15-actual92-byte-audit-summary.json](2026-11-15-actual92-byte-audit-summary.json) | 4249 | `8a33bd80100236bcfeb3f6a9bd2fa71928dda482715ed40b400a861da4b456a7` |

Actual92 支持一个具体后继算法选择：把最后实际有限内层点和该点 fresh 完整 J 作为可检验候选，并把非零实际 d3 保留在完整线性模型中，而不因未达到近似内根阈值就完全放弃外层原 merit 判断。这不是宣布这些点已经接受，也不改变最终原 unit/full112 阈值。若下一方法采用含 normal restoration 的完整线性消去，必须将实际 d3 的 normal offset 写进原模型，并继续由原 full3 merit、真实 gdot、域和原回溯裁定。

项目化三残差可作为另一独立算法表示，但其归一化导数、真实 Robin 行及端点 pair、零分母例外和原阈值恢复都需要明确；不能只按这一轮的谱或 inner 停滞把它称为必然有效的缩放。本次结论到此为止：已经取得真实下降，近似内层根判据在末轮挡住了尚未被外层检验的有限点，原低三求根问题和后续完整 BVP 仍未解决。
