# R824：原全局极点生成元的分层消费者执行契约

日期：2026-11-15。状态：**工程契约与有限算法；本文没有新数学运行结果。**
证明依据为 [R824](../results/R824-original-pole-module-generators-in-weights-five-to-seven.md)
及 [R822](../results/R822-original-polar-lattices-certified-by-global-colength.md)。
以下全部新算术仅在公开仓库自己的 Actions 中执行。

## 1. 实际简化后的 scope

根会话已从旧 R787 完成阶段按原 manifest 逐 SHA 读回一条真实1186阶非零 Schur minor，
所以这里可消费已证明的原实际
$$
r=28,\qquad M\simeq S(-5)^{28}\oplus S(-6)^{244}.
\tag{824M.1}
$$
该结论不要求旧 R787 的一个有理关系已经恢复，更不将它冒称为完整核。

原已核见证为：

- R787 run43683912711，source `eab5e58bbf951c48ccf13a109bbdf0b0289a6f23`；
- 原 full manifest SHA `613f436b2c398cdcd5c9a92c4eb47e72bc81f8d0e8395322eff6455c89c0821c`；
- 素数1000000753，原 branch0 的 $(B_{\rm fld},s)=(3197390,99932770)$；
- 原1186阶 Schur minor 的实际 determinant 为296007862；
- 原1234阶分子 minor 为336446771，原20阶常数 minor 为322380492；
- chart SHA `47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96`；
- selection SHA `a420d94a9a2f56fa449946bac6379f437e7e53120a651d7df95b5f9ef9b07adb`；
- branch00 SHA `c5b75f48b5c5d1cf2d98390e814a245306fa63f10ae43dae194dbfd560d895d7`；
- rational-blocks SHA `fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b`。

这里的 $B_{\rm fld}=\lambda b$ 是原 R781 整系数域生成元，
不是一个新的 CM 模型。源链同时保原 field、14个合法分支、$\kappa$ 和分母单位、
真实主元行列、原核心及来源 receipt；只读了已有见证，没有重新计算该 minor。

初次消费者只处理：

- 原五次空间的28个自由方向；
- 原六次空间模 $\tau M_5+\sigma M_5$ 的244个补方向；
- 272条完整原关系与最后的原纤维非零见证。

**不生成权7关系，不延伸 $R_{143},\ldots,R_{155}$，不重新计算任何 $H^3$。**
原五次 chosen_free_column=1186 的那条关系已经由 R787 正在提升，
本消费者为它保留原来源插槽，不再开始第二份同目标的 Dixon。
其余27条五次方向和244条六次补方向可先执行。

建议工程名字：

- core：`scripts/R824_original_global_polar_generators.py`；
- wrapper：`scripts/R824_public_original_global_polar_generators.py`；
- RESULT：`R824-original-global-polar-generators`；
- FINAL：`p41-original-global-polar-generators-certificate.json`；
- CLI：`--config --proof --method --field-core --retained --output --budget-minutes`；
- Python-flint 0.9.0；数学预算300分钟，外层job350分钟。

`requested_scopes` 与 `requested_generator_ids` 只表示本次实际工作集合。
部分集合已成时，FINAL必须明写 `all_272_generators_exact=false`、
`actual_complete_polar_module_certified=false`；不能因为本次scope完成就宣布极理想已成。

## 2. 真实最小来源闭包

### 2.1 R787：已成五次转换、模块和保留的一个目标

直接读取旧同核数学配置下的：

- 全部1234条 `R787-real-power5-row-NNNN.json.gz`；
- 原 selection、chart、rational-blocks、十四个 completed branch stage；
- 原 full manifest、public input、run/core receipts 与源文件 SHA；
- 若原 reserved target 已真正成功，再按其实际成功来源取 function recipe。

旧 R787 的预算停止不使已成 stage 失效。wrapper可接受这一明确的 partial producer，
但每个消费 stage 都须 `complete=true`、相同原数学配置、相同原输入及已绑定 SHA。
不能把部分 producer 的某个 candidate 文件当作准确关系。

直接复用原1234阶模逆、原常数消元 $Z_5$、
十四个1186阶 Schur 模逆与 `C_J_pivot_columns`。
这些旧块不重新选行、不重新求逆、不重新跑 rank。
此前未保留的其他自由方向右端只按本次实际需要生成；不重新形成全部旧 Schur 矩阵。

原 reserved target 在新的成功 recipe 中可能已同时清分母和除content；
保留其成对 $A,B$ 的真实共同比例，不再把原分母/content乘回。
它的原自由坐标 normalization 与新的目标标签均独立记录。

### 2.2 R781：补齐真正已成的130至142阶段

当前 R787 carrier实际只保 `R781-inverse-free-Laurent-000` 至129，
不能误当作原 R781 的全部已成前缀。

六次消费者从原成功 R781 run43679703344直接补入130至142，
并核0至142完整 `previous_stage_sha256` 链。
必须携带原 real-field input、真实证书、完整 manifest 和来源 receipts。
原0至129若已在当前carrier，逐SHA直接复用，不再次下载或重算。

该源已给 $R_0,\ldots,R_{142}$、$\kappa^0,\ldots,\kappa^{142}$；
本次只需 $N_5=129$、$N_6=142$。不消费新 Laurent 系数，也不新增 $\kappa$ 幂。

### 2.3 R801 与原父级：六次完整142项和七次短见证

读取 R801 的真实 power6 frontier142：
每条原 V6 行的区间拼接为

- 原 R795 `[0,82)`；
- 原 R799 `[82,109)`；
- 原 R801 `[109,142)`。

每段保原 `producer/file/bytes/sha256/first/stop`、
原 row index、recipe、node fingerprint 与前段来源链。
直接读已成 `integer_v_t_coefficients`；不再卷积已成前缀，也不重新做原相位转换。

最终纤维见证只需原 V7 的短坐标行及其已成 recipe；
读 R799 的真实1778维 index、实际短 minor 与所需 selected candidate rows。
不消费 R801 的七次96至175长尾，更不消费八次数据。
原已成 selected exact products优先按原叶子 recipe 做别名查询；
只有不存在别名的有限域新目标才作本次有限域乘法。

原 R786 的 M2第0、1、73行以及必要原 recipe 元数据，
可从已绑定 parent bundle提取。五次真实相位转换已由 R787保存，
本次首选这些完成行，不再对1234条原 q/xi 行做同一转换。

### 2.4 R798：复用已成六次选行

读取原 R798 已成的 `R798-selected-short-rows.json.gz`、
证书、manifest及来源 metadata即可；不重求其1506个行指标，
不复制690个与本次无关的锚点积。

原行集 $I_6$ 位于前82项、1640个坐标中，
实际已认证1506阶 minor mod739为646。
新使用素数下仍须核该固定矩阵为单位；
这只是新算术所需的合法约化检查，不重新声明一条新的原短基结论。

若固定minor在所选新素数不为单位，记录该坏素数后换素数，
不重选原V6基，不把失败当作特征零秩下降。

### 2.5 R805：原实际铅笔

只取真实 $\tau=e_0$、$\sigma=e_1+e_{73}$、
原272基次序与分布 `[1,144,127]`、证书和来源 metadata。
不重算无基点铅笔、291+127补基或690秩。

首scope不依赖 R803、R807、R809、R811 的原函数乘法矩阵，
也不计算完整 normal 换基。
需要后继 normal 坐标时，另接已经完成的 S 基接口。

## 3. 公共身份与可追加目标

不变 `basis_configuration` 至少包含：

- RESULT、core/proof/method/field-core SHA、Python-flint版本；
- 原 p41、原map index4、真实 degree1206；
- 原 $L$ 模数、$\lambda$、$s^2=-3$、实圆分模数与280维坐标说明；
- 原 R787 数学配置及消费的各 completed stage SHA；
- 原V5/V6/V7 basis/index身份、原142项区间闭包、
  R798实际行集、R805实际pencil；
- 已证明 profile `[28,244,0]`、原权总和1604、原epsilon权总和398；
- 固定的公共clear-operator定义及原14坐标基顺序。

传输artifact URL、预算、requested targets不改变数学身份。
旧 R787 成功关系尚未返回时，不在公共tag中伪造一个null成功producer。
该 reserved target单独绑定其最终真实成功recipe与原自由列；
追加时不使已成27+244条失效。

任何新素数有自己实际的 source-bound modular-chart tag；
同一原target若需要换素数，保留旧已成特征零候选和失败原因，
不能把两个不同自由坐标归一的 lift拼在一起。

## 4. 用公共clear-operator消去逐阶重复域乘

令 $N$ 为129或142，并定义
$$
U_N(v)=\sum_{n=0}^{N-1}R_n\kappa^{N-1-n}v^n,
\qquad Q_N=246^3\kappa^N.
\tag{824M.2}
$$
对原 $A,B$，R824的全部条件等价于
$$
Q_N\,vA(v)+U_N(v)B(v)\equiv0\pmod {v^N}.
\tag{824M.3}
$$

**等价证明。** 第 $m$ 个系数是 R824(824.22)乘以非零
$\kappa^{N-m-1}$。$0\le m<N$ 时幂指数非负；
故所有式的零条件相同，没有求一次精确 $\kappa^{-1}$。$\square$

取一个明确正整数 $D_N$ 清除 $U_N$ 和 $Q_N$ 全部280坐标的分母，保存
$$
\widetilde U_N=D_NU_N,\qquad \widetilde Q_N=D_NQ_N.
\tag{824M.4}
$$
它们是固定原整系数基
$B_{\rm fld}^i s^j t^r$ 中的整数数组。
这一步是本次真正新增的公共乘积，不重新计算任何 $R_n$、
$\kappa^n$ 或原基前缀。完成一次后，全部该权目标只读同一数组。

使用 R781 原打包
$$
r+39i+507j,\quad0\le r<20,\ 0\le i<7,\ 0\le j<2,
$$
再以1521为 $v$ 指数间隔。
两因子乘后最高内部指数
$38+39\cdot12+507\cdot2=1520$，
严格小于1521；故不同 $v$ 次数不会发生内部carry。
先作两次截断整数或模整数多项式乘法
$$
\widetilde Q_N\cdot vA+\widetilde U_N\cdot B
\pmod{v^N},
\tag{824M.5}
$$
再逐块以原 $s^2=-3$、原 $B_{\rm fld}$ 模数、
原 $t$ 模数准确约化，即得到全部 $N\cdot280$ 个有理坐标条件。
不能只检查少数点值、少数块或某个代数分支。

在 Dixon 的素数域修正中，使用各原分支的同一个
$\widetilde Q_N^{-1}$ 将残差还原成原未清分母的分子/Schur方程。
必须实际核 $D_N$、$\widetilde Q_N$ 在全部所用分支为单位。
原 $\kappa$ 单位及原R系数分母链提供来源，实际逆仍在素数域中验乘回。
复合模数上仅做环运算；不对复合模数矩阵求逆或求秩。

## 5. 五次完整28方向：复用旧chart

读取原1214个常数消元后的自由变量、1186个Schur主元列。
28个非主元方向按原列序编号。

每个新目标只固定其中一个非主元坐标为1，其余非主元坐标为0；
这是原 $L$ 上的同一个归一，不允许十四个代数分支各选不同的自由列。
原 chosen_free_column=1186保留给原 R787。
其他27个目标只新增其原自由右端、对应提升与完整验证。

初始有限域解复用旧：
$Z_5$、分子模逆、每branch的Schur逆及 `C_J_pivot_columns`。
生成该新自由列所需的卷积像后，解主元坐标，再核全部原129阶模条件。
被旧程序删除的庞大临时全C矩阵不重建；只生成实际所需的新右端。

最终准确recipe保存原V5次序的两组1234×14整数或明确有理坐标，
字段基固定为
$B_{\rm fld}^0,\ldots,B_{\rm fld}^6,
sB_{\rm fld}^0,\ldots,sB_{\rm fld}^6$。
$\lambda^i$ 只在后继确实换到原 $b^i$ 基时乘一次。

## 6. 六次只提升244个商空间补方向

原六次关系的准确核维数为300。
去掉常数20条件及1506个分子变量后，
Schur形状为1314×1486，准确秩1186。
核维数300由R824中的原Riemann--Roch计算给出；R801提供已经完成的原V6前缀。
不从一个退化模秩推定该特征零维数。

先尝试旧 R787 的合法素数1000000753：
保留同一十四个原域分支，核新V6固定分子minor，
真实构造本次所需的常数块及六次Schur块。
全部分支须有同一1186阶非零主元minor，才接受这个chart。
若该素数失败，保存准确失败范围，公平换一个合法素数；
不重选原V6基，也不修改五次已成数学身份。

仅在有限域中恢复六次的300个归一化核向量。
另把五次的28个有限域核向量分别乘 $\tau,\sigma$，
在原V6短坐标中表示，并取该六次chart的300个自由坐标。
乘积属于V6是原截面身份，故前82项的原注入足以求其表示；
不需要为此延伸原V5的129项前缀。

得到300×56矩阵，其真实秩必须为56。
选择在十四个分支都非零的公共56行minor，
其余244个自由坐标的单位向量就是所选补方向。
仅提升这244条；不在特征零恢复全部300条M6核基。

所有实际补方向、分支、主元、自由坐标、输入SHA均进入目标身份。
最终特征零证书不依赖“模补空间看起来正确”：
每条仍完整验证(824M.5)，并执行第8节的真实纤维满秩见证。

## 7. 提升、准确重构与有界断点

每个目标或很小的目标组独立保存current Dixon状态。
公共矩阵与operator只保存一次。
初次可逐目标或两目标一组；只有实际内存和耗时结果支持时才增加组宽，
不能从16GB限制凭空承诺全部271个右端会很快完成。

每次提升：

1. 以(824M.5)求原完整残差 mod $\ell^{k+1}$；
2. 核全部坐标被 $\ell^k$ 整除；
3. 在实际十四个原域分支，以同一主元chart求修正；
4. 核该修正在全部 $N\cdot280$ 条件中准确消去残差；
5. 保存新current、previous SHA和小digit receipt，原子推进。

有理重构使用明确矩形 $2AB<M$，不能只凭近似稳定接受。
候选统一清分母、整content后，重新以整数(824M.5)核全部坐标为零。
正确恢复原比例；只要对同一 $(A,B)$ 成对缩放，生成权及极点身份不变。

单一目标的旧大lift在新current完整落盘后只保name/bytes/SHA/digits历史。
保留未成current与所有已成准确目标，不保存逐位全向量以免重演R787的5GB增长。
若硬中断发生在候选验证中，读取已成operator、候选及完整块检查点，
不重新执行其完成部分。

每次只驻留一个权的原矩阵；源JSON行用有界缓存。
模逆在原始列表读入后转成flint矩阵，释放重复Python大列表。
不把271个大lift或所有版本同时留在内存。

## 8. 最终原纤维证书与输出

从实际准确272对recipe读取 $B_j$，权为28个5及244个6。
以某个实际整数 $z_0$ 形成原V7中的1778列
$$
[(\sigma-z_0\tau)V_6,\quad
(\tau^2B_j)_{a_j=5},\quad(\tau B_j)_{a_j=6}].
\tag{824M.6}
$$
所有列的原整数尺度都是 $82^{14}$。
原 selected recipe别名优先；不存在的乘积只为此次有限域目标计算。
使用原 R799 已成1778个短坐标行，记录一个在真实合法原剩余域上非零的minor。
该有限见证证明特征零满秩；没有把模值直接当作特征零determinant。

这一最终minor必须由已准确验证的最终recipe形成；
不能只沿用提升前的模候选基，也不能把原V7自身的旧minor当作(824M.6)的minor。
坏素数或某个 $z_0$ 恰落在极点像中只继续搜索，不推定候选数学错误。

通过后，R824/R822直接给全部原极点模：
$$
\pi_*\mathcal O_Y(-E)\simeq
\mathcal O(-5)^{28}\oplus\mathcal O(-6)^{244},
\qquad \operatorname{length}=1206.
$$
不需要首轮计算 $M_A,M_B$ 或完整特征零Hermite操作记录。

最终索引逐列保存：

- generator id、真实权、原V5或V6基索引及producer；
- 原 $(A_j,B_j)$ 两份准确坐标与共同归一；
- 完整 $N\cdot280$ 验证stage及公共operator来源；
- 原自由/补方向标签；
- 272列真实纤维minor的参数、原域合法约化及完整源指纹。

FINAL应分别列出：
`exact_weight5_generators:28`、`exact_weight6_generators:244`、
`exact_weight7_generators:0`、`global_generator_count:272`、
`weighted_source_degree:1604`、`ambient_epsilon_degree:398`、
`actual_polar_module_colength:1206`。
这些值只有真实完成全部来源和验证后才可置为最终成功。

同一FINAL仍明确：
`normal_polynomial_ideal_matrices_computed:false`（除非后继已实际完成）、
`radical_or_Jacobian_eta_or_height_computed:false`。
此处的全局截面生成元是完整原极点模的输入，
不是已经计算出的闭点分解、radical、$\eta$或规范高度。

## 9. 续传与不改旧任务

wrapper对每个来源核真实run/source/core、原manifest与逐file SHA。
新bundle仅携带本次实际消费的完成行、源metadata和必要公共块；
保留当前原R781130至142与R799 selected rows，避免下一次为旧artifact过期而重算。

只有真实运行的source和artifact进入active request。
原R787尚未返回的reserved准确recipe保持独立pending；
其他目标可继续，不伪填其结果，也不重启旧R787/R809。

所有raw、完整矩阵、lift和可重算证书仅在一日active artifact中续传。
Git只保存证明、方法、脚本、请求、真实run与SHA摘要。
本地限于源码、AST、schema与IO，既不导入该数学核心，也不运行数学枚举。

