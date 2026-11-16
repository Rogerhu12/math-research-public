# R860 原半线性函数分式的最小执行契约

日期：2026-11-16。首 scope：`two_original_cofactor_expressions_and_fixed_differential`。
数学证明见 [R860](R860-original-adjugate-semilinear-descent-and-rational-differential.md)。

## 1. 本次输出

- RESULT：`R860-original-semilinear-resolvent-DAG`。
- FINAL：`p41-original-semilinear-resolvent-DAG-certificate.json`。
- core：`scripts/R860_original_semilinear_resolvent_DAG.py`。
- CLI：`--config <expanded-job.json> --out <directory> --budget-minutes <number>`。
- 核心只在本公开仓库 Actions 执行，使用标准库；`sys.set_int_max_str_digits(0)` 在入口设置。

本次实际构造两个有界余子式及其函数分式的完整源 DAG。原 $W$ 的全部有理系数由真实 34 组原坐标文件给出；矩阵条目是原分子除原逐列分母，不再乘 $82^6$。不重算旧 690 块、272 乘法右端、cyclic minor 或 R853 的三个共轭。

本次不展开 $D(z,T)$、$N(z,T)$ 的系数，也不展开 $\beta_{72}$ 的幂基向量。结果把 `exact_original_semilinear_fraction_DAG_constructed` 与 `expanded_bivariate_cofactors_computed`、`expanded_power_basis_coordinates_computed` 分开，后二者保持 false。RR、连接和 period 的实际完成旗标也保持 false。

## 2. 三组真实来源，61 个最小文件

### R806：45 个文件

原 producer `43707290840` / source `75b1d56c821abe34660477ba8b4c7f7b75a4382b`。选择原完整 manifest、public/core/run metadata、成功 certificate、stage manifest、polynomial-multiplier index、accepted candidate、candidate definition、coordinate chart、实际 cyclic witness，以及 index 的全部 34 个 coordinate groups。

每组保真实 complete/configuration，核 column indices 的完整 0..271 覆盖、690 行、各原逐列分母、原 `all820_original_coordinates_verified`、`weighted_polynomial_support_verified` 和 `reduction_equals_successful_modular_multiplier`。用原 index 的 690 条 S 行映射建立条目寻址。实际负次数位置逐项必须为零；不执行新的原 820 行乘回。

每个组的来源检查保存为单独原子 stage。恢复时直接读取已成检查及其同源 SHA，不重新解析该组的大有理数组。所有原数组字节仍完整保留在输入 carrier，不用一张无系数的矩阵描述替代它们。

### R805：7 个文件

原 producer `43705580592` / source `9f960b8e0b2fa825ab1391e86db4e1383ffdd700`。选择 manifest、三 metadata、certificate、accepted pencil、graded-free-basis。

原 free-basis 的真实文件为 11649B / `74311a7a143fafc43a36d1a43f6146e6aa3cb28809a020e3fa1337fdc4e475c9`。核原一次补基 $e_2,\ldots,e_{145}$、次数分布 $(1,144,127)$、实际 $n=1$。只读复用实际选择，不重求 739 的秩。

### R853：9 个文件

原 producer `43801910753` / source `813f9b813fe131dedadd3891bfedfbc2074e3406`。选择 manifest、三 metadata、certificate、source audit、三个准确共轭的 coordinate stage、原 function-field DAG、stage manifest。

三个准确列、全部 560 原坐标乘回旗标、实际 normal 运输和原来源同一性保持。三个旧未执行 Krylov 节点不冒称已成；新输出只替换剩余 $\beta_{72}$ 的表示法，不将源 DAG 改标签。

各来源的 result/run/source/core/manifest/certificate/configuration、全部选件 name/bytes/SHA 都固定。配置中的本地 `directory` 只用于当前读取，绝不进入数学 tag。61 件原字节打入本次一日最小 carrier，后继不依赖旧包是否仍活跃。原 metadata 本身属于源，不改写为新 producer。

全新 Actions runner 的实际运输不用过期的 R805/R806 原 artifact：R806 的45个原件从已结束 R815 run `43777837244` 的53件原输入 carrier 中取得；该 carrier 为109958828B / `051571e117cdaafe31f9851c664c72583f55181444dbe112bbcbb7f2d2fbf1b3`。R815 此次真实预算出口124、无 core receipt，只承担原输入字节续存，不声称其算子已完成。R805 的7个原件从成功 R856 run `43805659598` 的569件输入 carrier 中取得；该 carrier 为13406926B / `fd6329bd17f2d729a3c3834e78fe7b4b626be84b692e77d0e51bbdf205f01e41`。R853 的9个原件仍从其真实成功 artifact 直接选取。

两份 carrier 均逐全部成员核原 bytes/SHA，再仅保选中的原组。活跃运输 producer 的 manifest/public/run/真实可有的 core receipt、成员清单和输入 receipt 原字节另存入新 artifact；新数学 tag 仍只依赖原61件的真实身份。运输路线不改旧函数、坐标或来源标签，也不触发旧数学。

## 3. 有类型的表达式程序

程序的两个变量是原底域坐标 $z$ 和独立多项式变量 $T$；原 primitive 函数是 $w$。原 $W$ 节点明确保留 `row_output_column_input`、272 阶原 normal 基、全部 $\epsilon_i$、完整 S 行映射及 34 组分子/逐列分母的源引用。

构造

$$
A=TI-W,\qquad
D=\det A_{\widehat0,\widehat0},\qquad
N=\det A_{\widehat{72},\widehat0}.
$$

删行、删列均从 0 起；$(-1)^{72}=1$。记录 $D$ 首一 $T^{271}$、总次数至多 271；$N$ 的 $T$ 次数至多 270、总次数至多 272。度数证书来自原逐项 weighted support 和固定矩阵结构，不假称实际展开后次数恰等上界。

两个多项式只在 `evaluate_T_at_original_primitive_w` 节点代入 $T=w$。原 R806 primitive certificate 与 $D$ 的首一 $T^{271}$ 一同给真实非零分母依据。随后构造

$$
r=N(z,w)/D(z,w),\quad
c_Yz=z-2r,\quad c_Yw=w,\quad c_Ys=-s,\quad c_Yr=-r.
$$

程序同时给一个有限的 normal 输入模板：对实际 $v$，用
$-\det\bigl(\begin{smallmatrix}A&v\\e_0^t&0\end{smallmatrix}\bigr)/D$
得到原函数。模板不算一份已经实例化的额外右端；只有当前 $e_{72}$ 真输入是本次函数分式根。

原导子/微分部分绑定 R860 定理 860.2、R802、R813、R853：$c_Y\delta=\delta c_Y$、$c_Y\nu=\nu$，$\nu=82\tau dq_Y/q_Y$。这是证明适用的实际源接口，不读取或生成未成的 $\Gamma$。所有后继对 $f\nu$ 的下降只对 $f$ 执行上述真正函数替换。

非零分母只在函数域意义成立；在指定点可能为零。程序不声称它在整个 affine 图或某个 41-adic 球上可直接取逆。后继局部求值须按原 normal 环消去可去分母或真实选择可用图。

## 4. 原子阶段和续算

所有数学阶段在 output 根目录，文件名 `R860-*.json.gz`。已成阶段含同一个完整 configuration 和 `complete=true`，写临时文件后原子替换。完整阶段不覆盖。每个 coordinate group 的结构/来源检查写完后才进入下一个预算边界。

顺序为：真实小 source identity 审核；34 个原 W 分组检查；完整 coefficient-address index；两个余子式与半线性/微分 DAG；最终 certificate。预算停止保留全部已成阶段及 `R860-current.json.gz`，不补算任何旧数学。current 的 `complete=false`，只登记实际已完成的阶段和停止位置。

stage manifest 只列本次所有 `complete=true` 阶段，排自身与 current；文件名带实际清单 fingerprint，避免旧 false FINAL 锁住后续推进。false FINAL 是那一时刻的历史状态，不用它的旧清单 SHA 约束更新后的 current。true FINAL 必须逐 SHA 绑定全部所引阶段。

## 5. 标准库 wrapper 与真实输出核验

wrapper 正常导入冻结的原 R837 transport helper 与原 Range helper，仅调用标准库 IO 函数，不改全局常量、不导入数学核心。新来源下载逐选件核 bytes/SHA 和原 metadata/schema；如果从新 carrier 恢复，先核 carrier 与全部成员，再重建同一 expanded source identity。

数学 tag 包含真 core/proof/method SHA、原六项证明 SHA、三组源 identity/configuration/selected-file fingerprint、固定原索引、完整策略。预算/恢复 artifact 及本地目录不进入数学 tag。新的运行不伪装成 R806 或 R853。

verify 只核真实 source、stage、类型/索引、依赖及成功旗标，不重做余子式算术或原 W 乘法。所有异常打印完整 traceback。run/core/public-input/full-output manifest 保实际运行身份；所有 raw/coefficient/source 数据仅一日 Actions artifact，Git 仅方法、脚本、request 和 workflow。

成功出口只说明指定原函数分式、共轭生成元及原固定微分的完整源表达式已实际构造。指定 theta 帧、原 RR 选择、Hecke period、非 $p$ 项、height 与全 $p$ 非消失都不由本次替代。
