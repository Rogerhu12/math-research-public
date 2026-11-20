# R138 完整谱体预算的4个新upper与条件性allowance合同

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

公开科学入口建议 `fourfold_codazzi_spectral_body_energy_budget.py`，对应 scratch 源
`r138_spectral_body_budget.py`；建议结果名 `spectral-body-energy-budget.json`。
本合同规定一个新的完整能量比较，不重新计算旧 $C_E$ 或任一旧预算。
本机仅已进行 AST、whole原输入恢复/hash/metadata admission；没有 Arb import、
新科学求值、旧producer或旧目标调用。

## 1. 新目标与原对象

数学依据为
[SG 互补Gram谱体能量](../results/R138-supplement-complementary-Gram-spectral-body-energy.md)、
[RN 根锚定组合必要筛查](../results/R138-supplement-root-anchored-spectral-budget-necessary-screen.md)。
保持同一实际 $Q_{repair}$、固定内禀参数 $\eta_0$、固定 $\nu_0$、完整moving圆周、
真实根与原外端 $R=25/8$。原body drift仍以外端恒等锚定；其完整旧 $\Gamma$仅读。
本预算的后继根读出明确使用RA的独立真根锚定flow，而不是重启已被SE排除的旧根
$\Gamma$整因子路线。

新目标按顺序为：

| 名称 | 数学意义 | 保存方向 |
|---|---|---|
| `C_spectral_upper` | SG.12整个4651片的完整谱upper，并与已保存旧CE upper取min | upper |
| `wE_spectral_upper` | SG.14同原GB体 $H^{1/2}$读出E系数 | upper |
| `aEE_spectral_upper` | SG.15体平方E系数 | upper |
| `aEB_spectral_upper` | SG.15体交叉系数 | upper |
| `root_allowance_spectral_lower` | 仅原body三门通过后，SG.17的半余量allowance | 条件性lower |

前4项必须全部完成。若三门未过，仍保存整个4项成功结果与false门，不制造第5项。
即使所有必要筛查和body三门通过，也不授根有限receiver Gram、实际low96返回、
完整high交叉、真实边界型、正区逆或非线性存在。

## 2. 原完整输入、纯admission与CLI

入口独立，无 W2C context、旧科学 import 或 candidate numpy。CLI有11项：

```
--positive --germ --physical --physical-execution
--composed --composed-execution --body-budget --body-execution
--root-screen --screen-execution --output
```

`admit_inputs(args)` 与 `admit_saved_budgets(args,admitted)` 只作完整原字节、
JSON/参数/分区metadata校验，使用标准库。它们可在不导入Arb的情况下检查
所有whole资格。新数学只在 `run(args)` 内，且要求当前公开Actions仓库身份。
精度固定320bits，不在本机求值。

### 原native，历史恢复只有5件

| 输入 | 完整 SHA256 |
|---|---|
| positive完整4650行native | `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d` |
| 完整true-root germ native | `397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864` |

原positive parts index对应4块：

```
21aeb58604b9b969f815ea23f437e3bcc9e069f5
3656cfd427b93a3fd7e58094aa7f6832d6e0296b
eddff9213f80635df57a35ce11b6751de1cbbda3
c26c0957b9eef2386e87f66a385d7871369eba55
```

完整germ历史blob为 `2b90cfe80a6381badc29f02f7dcb3dce2584851d`。
先按原定义恢复整个native、核压缩字节SHA，再读JSON；没有只取局部几行
当作原完整证书。无需candidate5、angular4、high41 native或任何g0 stdout。

同candidate/object/repair身份分别为

```
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
```

### 当前完整已成科学与execution，共4对

| 对象/run | actual SHA256 | execution SHA256 |
|---|---|---|
| X 44737045152/1 | `1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec` | `999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92` |
| Y 44740320925/1 | `19b489ce0b8b85d4223ea334f7e2397188755d42605bf7613d2023ac69cb2cf3` | `2e4cea611a229dbf894bae1fb2478ebc2219f9c0282a84cae1abd32ceb54f084` |
| GB 44745355257/1 | `5b5f374fb68e66ce25725195a9d574940e5ee7e9b273b6b55da90ada261ec492` | `9bc00f39ab9656ef3e3afbc64f3df20d8340bbe85b92be4bc17141a80f28a18f` |
| RS 44758362539/1 | `e1b27ffa5759b9b55bc785ef17d362a67f1d370d5ae26e68b422922d9a0229d8` | `ba15b1060c40e965b27cc325c7696a35202dbf54c83817dbfb508750acdf8f1c` |

每对都核完整文件SHA、same run/attempt、complete/proved/failure、returncode0、
原child数1及0旧target重算/producer调用，执行receipt必须绑定整个actual SHA。
Y内原X引用与独立读取whole X一致；GB明确绑定同X/Y两对；RS明确绑定同X/GB
及同positive/germ。原success/false比较与scope逐对象原字引用保留。

RS的完成数327/10464、真根/全部高/mean资格以及完整 $T<125$球用于RN前提，
不调用RS源、不求原积分、不读取旧3条signed矩阵为新目标。
RD局部Gamma的actual并非本算法前置；RN只用 $\Gamma_{loc}\ge1$。
这不是省略后继真正容量所需的局部Jacobian，而是本次未消费它。

### 建议当前proof pins

新源/合同/worker/gen/manifest/workflow、原positive parts index、上述8个小输入外，
至少保留公开SG/RN/RA、GB截顶曲率体能量、X/Y完整预算、RS实际单积分结论、
同实际support $\sigma>2/5$、same-Qrepair连续修补及原positive全cover接受证明。
不用旧CE source执行来“验证”其输出，也不加入未完成的finite Gram伪前置。

## 3. 全4651片，不截下端、不丢mean

新完整数学domain是真正 $[r_*,R]$。为上界，第一片使用原germ覆盖
$[r_{lo},r_b]$，其余是原4650行完整覆盖 $[r_b,R]$。
必须核 $[r_{lo},r_b]$同时在原scalar germ与complex rectangle的real domain内，
原真正根interval、2549piece和固定参数全部相同。
本次没有把 $r_{lo}$作为实际根；首germ $K_-=0$只用于实际正侧 $r\ge r_*$。

body的完整4650行与3594interface metadata均按原顺序读取，接口hash与X相同；
每行原moving角、whole primitive、完整mean资格保持。
私有分区 `(left,right,original_row,candidate_piece)` 的新hash/count公开，数组不公开。
整4651片均完成才发布新全域谱upper，不能在中途以旧CE补未算片并声称全新目标成功。

各原闭行 $U,V$为Wiener upper；$m$、$\gamma,K$使用完整signed lower/upper球。
germ的 $U,V$读取Astrip0，支配完整真圆周；$m_+$沿旧X读取其完整modulus_upper。
原inverse-angle gap给 $v_-$。原mean没有以零或一个样本替代。

## 4. SG.12 的完整有向实现

完整pair修补界仍为 $\varepsilon=4\cdot10^{-18}$。
原已付背景只作以下同X的代数改变：

$$
U\gets U+\varepsilon,\quad V\gets V+\varepsilon,\quad
m_-\gets m_- -\varepsilon,\quad m_+\gets m_++\varepsilon,
\quad v_-\gets v_- -\varepsilon.
\tag{SC.1}
$$

新增的upper/lower都按所示方向取；$m_->0,v_->0,\gamma_->0$须整片严格核定。
intrinsic $\gamma,K$不受状态修补而变化。body保原 $K_->0$；germ取 $K_-=0$，
$K_+$均用原完整real球绝对upper。

依次构造私有有向量

$$
t_-=(\gamma_-m_-)_{lo},\quad t_+=(\gamma_+m_+)_{hi},\quad
M_b=(1+U^2+K_+V^2)_{hi},\quad
\kappa_b=(K_-v_-^2)_{lo},
$$
$$
\Delta_b=\sqrt{\max\{0,\operatorname{upper}(M_b^2-4\kappa_b)\}}_{hi}.
\tag{SC.2}
$$

最后分别在两个同一eta端点求

$$
C_i=\max_{t\in\{t_-,t_+\}}
\operatorname{upper}\frac{M_b(t+t^{-1})+\Delta_b|t-t^{-1}|}
                              {2(2/5)v_-}.
\tag{SC.3}
$$

两端点最大来自固定 $A,B$ 的Loewner凸性；$M$增、$\kappa$减的替换只放大谱。
没有分开挑不同eta点构造虚假的相关性。真判别式非负由
$M\ge1+\kappa$保证；(SC.2)的max只解决有向表示，不能删除真实正项。
整个计算不除以 $K$，真根退化域保持。

每64片保存当前max并读回upper继续；最后一片也保存。完整4651片结束后，
才把新max与**只读**旧X `C_E` 的完整upper取min，保存 `C_spectral_upper`。
旧CE已是同谱的合法另一upper，这个min不重算其原4651片，也不授新曲率/A0目标。

## 5. 只读旧量与4条新upper链

源码完整保留的旧scalar records为：

| 来源 | 字段 |
|---|---|
| X | new_scalar_suprema.C_E、C_H、A_Theta；complete_derived_energy_bounds.Gamma、h_B |
| Y | new_scalar_suprema.E_0、E_1；complete_derived_energy_bounds.h_E、r_E、r_B |
| GB | new_records.wB_half_upper、aBB_upper |
| RS | complete_test_integral |

它们原球只读，不重新求值；真正新链为

$$
w_E=\frac52\Gamma\sqrt{A_\Theta}
                (\sqrt{C_{sp}}+\sqrt{C_H}h_E),
$$
$$
a_{EE}=E_0w_E^2+E_1w_Eh_E,\qquad
a_{EB}=2E_0w_Ew_B+E_1(w_Eh_B+w_Bh_E).
\tag{SC.4}
$$

每条先原子写入、准确字节读回、核完整球contains，然后仅以其saved upper
进入下游。没有以新体 $H^{1/2}$值替换旧真正root $H^{2/3}$ trace的 $r_E,r_B$。
$w_B,a_{BB}$与旧算法完全无关于CE，本次不把它们再次输出为新目标。

## 6. body三门与条件性第5个lower

从4条新saved upper与旧 $a_{BB}$ upper构成选定矩阵

$$
M=\begin{pmatrix}a&-c\\-c&d\end{pmatrix},\quad
a=2-a_{EE},\quad d=1-a_{BB},\quad c=a_{EB}/2.
\tag{SC.5}
$$

先用有向 $a_{lo},d_{lo},c_{hi}$形成
$D_{lo}=\operatorname{lower}(a_{lo}d_{lo}-c_{hi}^2)$。
只有 $a_{lo}>0,d_{lo}>0,D_{lo}>0$全部成立，才计算

$$
Q_{hi}=\operatorname{upper}\{2[d_{hi}r_E^2+2c_{hi}r_Er_B+a_{hi}r_B^2]\}>0,
\qquad C_{allow,lo}=\operatorname{lower}(D_{lo}/Q_{hi}).
\tag{SC.6}
$$

分母是upper，里面必须使用 $a_{hi},d_{hi}$，不能误用numerator里的margin lower。
$r_E,r_B$均是完整旧saved upper；中间 $a,d$是同一数值选择的有向表示。
第5条保存为lower后，再取整个读回球的lower供后继。
这是SG.17原半余量推导；它不支付实际根低receiver或source。

三门中任一个false时，条件allowance字段明确 `applicable=false`，只保4条新upper。
完整科学仍成功，并如实保false；不得未算补0、用旧allowance改label或重复启动
同名目标来掩盖本次结果。

## 7. RN必要筛查的独立scope

科学准入直接从旧完整球确认 RN4/RN7 的精确有理前提以及 $T<125$。
完成新4条并读回后，比较

$$
C_{sp}<24,\qquad w_E<45/2,\qquad a_{EE}<102/125.
\tag{SC.7}
$$

每项的严格通过使用整个new saved upper；另外用new saved lower不小于相应阈值
来标记“确证违反该必要条件”。若保存球跨阈值，只是未通过，不能误称确证违反。
即使全部严格通过也只是必要条件；不设根边界正型/全逆true。
本次不读取RD数值、不重新求其Dloc/Gamma，不假定任何尚未支付的新capacity函数。

## 8. 科学JSON的准确27字段

固定kind为 `R138_complete_complementary_Gram_spectral_body_budget_v1`。
顶层准确字段为：

```
identity complete proved failure stage
expected_closed_cells completed_closed_cells current_exact_right spectral_max_prefix
new_records saved_record_count old_scientific_targets_called old_CE_targets_recomputed
old_geometry_ODE_calls old_residual_targets_recomputed
old_Gamma_and_root_trace_targets_recomputed old_wB_aBB_targets_recomputed
old_RS_targets_recomputed new_drift_or_capacity_ODE_calls published_arrays
whole_original_references reused_complete_scalar_records
body_only_sufficient_comparison root_anchor_necessary_screen conditional_root_allowance
scope seconds
```

完成stage为 `complete-spectral-body-energy-budget`，expected/completed=4651。
`saved_record_count`只能4或5，对应完整4upper与真正适用时的条件lower。
`spectral_max_prefix`是该新谱目标的断点/完整中间max，不额外冒充旧target或新数组。
原inputs/outputs/false gates经whole hash与reference保留。
所有旧target、ODE、array计数恒0，future根Gram/全逆/非线性scope均false。

中途异常保留真正prefix/failure，不覆盖已有完整科学或未成记录。
公开worker须先发表科学源/合同/manifest，再运行唯一新child；完整处理当前root README、
课题README、真实同步、容量和推送重试，receipt绑定全部实际输入与最终whole结果。
