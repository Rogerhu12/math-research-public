# R133 补充：内窗完整实角局部源预算的实际结果

**实际11门通过；原完整内窗源再次改进。** 负侧完整上界降到 10602457152，正侧降到 3219480409。它们仍不足以据此宣布目标强返回或全ν误差门成立。本条只采用实际公开运算，不把候选源码或解析合同当作数值结果。

## K.A1. 真实 run、范围与原生身份

[公开 run43659519776，attempt1](https://github.com/Rogerhu12/math-research-public/actions/runs/43659519776) child0，complete/proved=true，11项检查全部通过。workflow head 为 47da03f4f0fdd7af4779a3a10ed9b925f8414dd8；实际科学 checkout 为 6d274f96bf9d14917d55751213fea9c190273293。

本次完全沿用 [原内窗实际结果](R133-supplement-actual-fixed-inner-first-Airy-complete-sources.md) 的同一物理 I、真实根区间、固定 η0、|δ|≤10^-8、输入 |j|≥97、n=4|j| 和密度 n^(1/6)。空间仍是

$$
H^{-4/3}\longrightarrow
L_r^2(H^{-2/3}\times H^{-2/3}).
$$

全部输出、独立 even mean、真实 old-circle J 和物理 seams 不变。正侧仍只授 raw source，未付其余 weighted 端口。

完整结果保存在 [本次原生目录](../notes/inner_first_Airy_real_local_sources_ci/run-43659519776-1/)：

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| consumers/inner-first-Airy-real-local-sources.json.gz | 13433 | 97d927393b672b19f60c03ac1c551657ded5c87da1399a26eebf64ec3e5e33f3 |
| consumers/process.json | 13838 | c6ec19e86b6a819776f190a117c2f654a9351b86da24d59b2dc5f02c2a18d764 |
| worker-process.json | 2369 | 799ca9434145026fe5730f61abff759547d70ea6c34a6fd3a4093b9b7bf27832 |
| publication.json | 2109 | 3bf2607a747b9b2a9acf2b20b4b8c7f08c0e635c13aafdd5e71d06d3be4b79b7 |

数学源 SHA-256 2151125d2e8c4bb20d0f470f385e2ca670ed9aaf91dd82f4f52cc192954e277b；71pin manifest 为 883742413736aa50c58a98e9b60642baf9f757bc1b407ba5c110ca51f5ba0b62。原64pin逐项不变。实际 Python3.12.14、flint0.9.0、numpy2.3.5；CI数学调用0.3644608649999981秒，worker数学调用0.5648578189999967秒。

## K.A2. 实际新增与准确复用

按 [K1–K11完整实角合同](R133-supplement-complete-real-angular-jets-for-inner-first-Airy-local-source.md)，只新增2个自然阶段和4行changed-local积分：

| 新阶段 | 完整 payload SHA-256 |
|---|---|
| complete-real-raw-local-angular-jets | b3164341a00bd0c599000723bd053f553aab13371be65e4e5083e4dba8048ac8 |
| complete-real-local-Airy-bounds | b6e47603609d7100b91e598a5d8ac86f46ba834ca932a21d1e0a35df7ef30850 |

旧 target、FFT、Taylor、profile、矩阵转换、全部非local和mean预算均0重算。特别是原两个成功 stage payload 9809a086…、1f46b066…原样复用；原全部四矩阵转换 payload c7faf5bc995cb6667693197573b0a8fec94069da67730c8c37b2ca78c86d7eb4 与原四行 payload 7847a7c53a73a1d176ab7de8d21eb6b3782c67ccb676c052fac026269356490e 均核定。

唯一缺失的 W0,4 用原 width1/512 的完整复带表Cauchy补出。T0、V0、vartheta 的角导来自原 width1/32 复带，d、dρ 的实际已存角导单独使用；所有完整乘积项和 raw μL0w1 保留。新界与旧完整解析界在同一空间取min，没有除以μ后偷换回raw源。

## K.A3. 实际 raw 局部角 jets

下表是完整 N1=μL0w1 两分量的实角普通导数上界，均从process Arb区间向上取整。它们仍是幅度jets，尚不是最终径向源norm。

| 角导次数 | 第一分量 upper | 第二分量 upper |
|---|---:|---:|
| 0 | 440.487683 | 14464126.375114 |
| 1 | 49778.881260 | 138172952.496954 |
| 2 | 12633494.837981 | 34775140534.380358 |

原全部真实乘积项分别保存在native：径向二阶、径向角向混合、drift导数、角向二阶、first transport、标量势、准确QK交叉。该预算包含两种分支的同参数准确奇偶识别，不共轭参数。

经原完整 real Airy profile 的 inverse-phase θ²转换，实际负侧上界为

$$
73188836622.74652339457162272908707426767031071422078481375942289
\quad(\text{Arb半径}<1.59\cdot10^{-54}),
$$

正侧上界为

$$
22224582984.24595599326029815804824313431456128870518112802743661
\quad(\text{Arb半径}<3.25\cdot10^{-54}).
$$

两侧都实际选择了新 real_two_derivative 候选。原解析候选分别约为1.494036256e13、1.493724701e13，仍完整保留；本次没有重复计算这些已成功候选。

## K.A4. 原四行完整 source totals

每一行均先按原非local与新local同分量triangle，再和独立mean平方项合并，乘原真实径向权；最后对原四行求和及平方根。

| 项目 | 负侧 upper | 正侧 upper |
|---|---:|---:|
| 完整第一修正非local | 3209834.581089 | 944684.884028 |
| 新完整第一修正local | 10599247317 | 3218535724 |
| 独立even mean | 43198.334265 | 12709.397856 |
| 新完整合并源 | 10602457152 | 3219480409 |

原非local和mean的完整数值对象逐字复制，没有以另一次更粗重算替代。旧合并源的upper分别2163674680531、2163193978865，作为原候选保留在新native和process。

准确新负合并Arb中心为10602457151.31554709760574702204045163298068530182576233739709859，半径<1.30e-56；正合并中心为3219480408.542483713354808068892458706393123374584173244791871118，半径<4.16e-55。完整局部费用确实改善，但这些值是upper，不能反推真实算子具有相同量级。

## K.A5. 检查、同步和继续项

11门核定全部71输入及原64pin不变、原17门inner与20门Taylor、正确μ/同参数分支、原小域13门及完整系数宽度、两旧stage身份、四矩阵/四行覆盖、全部非local/mean/径向权/zero半侧不变，以及新完整实角界有限并0旧数学重算。没有把这11门命名为强返回小量门。

runner在2026-11-15 00:43:10.905905 UTC及00:43:11.788508 UTC两次真实pull，均到6d274f96bf9d14917d55751213fea9c190273293；两README实际diff均为空。所有新stage与完整源行已保存。

下一项继续收紧高角导中的真实Taylor尾。原高根native已保完整intrinsic0..9；若扩阶，只补缺失10..15及相应有限系数/primitive/mean卷积，不重做原0..9、原domain或旧成功Taylor系数。外段root-value剥离、全非local与seams继续独立接合。最终强返回/充分cutoff、未知无限反馈、真实ν、非线性状态球与物理闭合仍未完成。
