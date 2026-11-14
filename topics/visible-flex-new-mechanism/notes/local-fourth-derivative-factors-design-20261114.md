# 完整局部导数权二、四的缺失原式因子：新增导出设计

日期：2026-11-14。状态：代码已静态核读；恢复终端后 py_compile 与八项小人工检查已实际通过，研究实际仍须公开 Actions；不预写研究 passed。

脚本 [literature_local_fourth_derivative_factors.py](../scripts/literature_local_fourth_derivative_factors.py) 独立于所有已成功生产者。该文件只新增原式因子导出，不计算新的 profile 查询、几何路径或成本商。

## 1. 为什么还需要新增原式

R124 已证明真实零矩后，静态 pure $m=8$ 局部成本逐系数落在现有响应投影像内。剩余完整导数成本为

$$
L^{[2]}+\Delta L^{[2]}+L^{[4]}.
$$

已发布 R124 的 $\Delta L^{[2]}$ 只是矩阵规范化诱导补项，不能代替原 $L^{[2]}$。

R109/R112 的原式为

$$
N=N^{[0]}+N^{[2]},\qquad N^{[2]}=P_{\rm acc},
$$

$$
L^{[2]}=v^{[2]}-\mathcal B_{m^{[0]}}(N^{[2]})
-\mathcal B_{m^{[2]}}(N^{[0]}),
$$

$$
L^{[4]}=v^{[4]}-\mathcal B_{m^{[2]}}(N^{[2]}).
$$

旧 full export 只有 $W$ 和静态 $L^{[0]}$ 原式，没有独立保存 $N^{[0]}$、$N^{[2]}$ roots。尤其没有证据证明 $N^{[2]}$ 的系数属于 $W$。因此不能删 $P_{\rm acc}$，也不能通过只读旧静态文件恢复这些缺失因子。

本次新目标准确限定为：

- 完整未模 $W$ 化简的原势 $N^{[0]},N^{[2]}$；
- 完整两模式 $-4,-2$ 的新局部生成元 $v^{[2]},v^{[4]}$；
- 冻结完整点态矩阵 $m^{[0]}+m^{[2]}$ 的原几何系数。

这些数据是上述两个完整 $L$ 表达式的**因子形式原式**，不冒充已完成全部复合或成本商计算。

## 2. 冻结接口与新增范围

依赖冻结的 literature_local_fourth_quotient.py，SHA-256：

- 9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0。

使用其既有 SharedCompiler、ZeroStateCoefficients、local_forcing、GeometryExpansion、endpoint_potential 和原 DAG 序列化接口；不修改旧脚本。

由于缺少原势独立导出，本次必须再次执行原局部第三密度的有限下层公式，以取得 $P_{\rm acc},P_h,R$ 并构成真实端点势。这是新缺失因子的必要前置运算。它不调用 control_templates、pre_reduce_templates，不重建 152 条控制表或 36 维 $W$，不重跑旧 $W$ 查询。

完整原势固定为

$$
N=P_{\rm acc}+P_h+F_*(k,\omega),
$$

$F_*$ 使用既有参考 $h_*=k_*=\omega_*=1$。原局部第三几何重构继续由冻结 raw_decomposition 的准确差式核验。按导数权拆出的 $N^{[2]}$ 必须与完整原 $P_{\rm acc}$ 逐项一致。它不经第三 span 化简，不把任何未证非零端势丢弃。

## 3. 全部真实 s 导数先于累计值置零

新 $v$ 仍使用旧生产者的完整六个 forcing 配对和两模式组合：

$$
v_{-4}=-R_{BB}/16-R_{AU}/4,
$$

$$
v_{-2}=R_{BB}/8+R_{B\bar B}/8+R_{AU}/4+R_{AV}/4
-R_{A\bar V}/4-R_{\bar A U}/4.
$$

第二、第三场来自原下层恢复。先计算全部 cov 导数及 cov-xi 导数，代入真实 history RHS；然后调用

- ZeroStateCoefficients(algebra, static=False)。

它只把累计 history 值置零，不把它们的导数置零，也不删除 $h_s,k_s,h_{ss},k_{ss}$ 等真实几何 jets。

新 adapter 的几何键共有十项：沿用原八项的顺序，再追加 $h_{sss},k_{sss}$。原势和矩阵的旧八键只在末尾补两个零。完整 cov 导数可能暂含三阶 $s$ jets，不能沿用只支持二阶 jets 的旧 GeometryExpansion，也不能假定这些项已经相消。

在展开之前，代码从最终真实 raw coefficient DAG 的可达节点扫描并记录各模式的真实最高 $s$ 导数阶及 jet 清单。新 adapter 保留 $h,k$ 的三阶 jets；若实际仍出现未支持的更高阶，则保留该扫描和已成原势导出，明确报告接口失败，不删项继续。这个阶数门独立于总导数权判断。

完整生成元的几何展开只能有权 $0,2,4$。新导出只选择权二和四。权零可作为完整原式展开中的中间项出现，但不组成旧静态 $L^{[0]}$、不再作旧静态商查询、不与旧目标重复验算。

两模式的全部原系数都保留。$-4$ roots 额外要求颜色次数严格为 $q^4$；每个 $-2$ root 保持原混合颜色。全体均为 profile 四次。没有在本次选择某个具体 $q$ 或 profile 测试对。

## 4. 原始代表与旧静态代表的相容

旧静态生产者对 $N^{[0]}$ 的每个几何系数作过模 $W$ 化简，并给原式重构证书。本次保留 raw $N^{[0]}$。两者的逐系数差属于真实 $W$，故乘 $m^{[0]}$ 或 $m^{[2]}$ 作 $\mathcal B$ 都只改变真实 $\mathcal R_8$ 项。

所以后续在同一响应商中可以将本次 raw 代表的导数密度与 R124 的静态规范化补项组合。但必须记录这个代表变化的来源，不能把两个未匹配的完整原成本在取商之前直接称作完全相同。

## 5. 两阶段完整导出

第一阶段完成原势后，立即写：

- local-fourth-derivative-factors-potential-original-expressions.json.gz；
- content_scope 为 unreduced-N0-N2-only。

它只含完整原势和完整矩阵元数据，不冒充 $v^{[2]},v^{[4]}$ 已完成。

第二阶段完成全部两模式新生成元后，写：

- local-fourth-derivative-factors-original-expressions.json.gz；
- content_scope 为 unreduced-N0-N2-and-complete-two-mode-v2-v4。

两份文件都含：

- source_hashes、真实 github_run_id/source commit；
- geometry_names（原八坐标之后追加 h_sss、k_sss）；
- 每个 potential_record 的几何键、导数权、原 root 名；
- 完整数据中每个 local_generator_record 的模式、导数权、几何键、原 root 名；
- 完整点态矩阵各坐标的原几何系数；
- 原 topological profile DAG、全部 original_root_sha256；
- 完整 $L^{[2]},L^{[4]}$ 的因子组合公式与 phase 约定。

沿用冻结 decode_expressions 可逐 root 恢复并核原 hash。序列化保存原表达式，不用不完备 word 代表替换它们。

后阶段若预算失败，完整原势早期导出仍留给终端 publisher 保存；main 照实 incomplete，仍记录早期文件身份。以后只消费这个已成因子，不需要为失败的下阶段再重算原势。

## 6. 后续 pure consumer 的具体计算

该导出完成后，下一 consumer 将直接读取这些新因子，并使用已经成功的 OriginalTailEvaluator 与 OriginalTailThird：

1. 在共同右锚代 $q=(c-\xi)^8$，原 $I$ 始终执行 $-J$；
2. 只评价新 $v_{-4}^{[2]},v_{-4}^{[4]}$；
3. 按原外槽与内槽顺序评价 $\mathcal B_{E_i}(N^{[0/2]}_\gamma)$，完整 pure 响应公式使用其既定 $1/16$ 约定；
4. 与导出的 $m^{[0/2]}$ 几何系数组成上文完整 $L^{[2]},L^{[4]}$；
5. 加入 R124 已发的 $\Delta L^{[2]}$，再对 R116 已发响应像求准确商。

不重新计算任何已发静态 profile 代入或旧响应列。完整两模式因子同时保留，供后续真正两模式商研究使用；pure 消费结论不会自动推广到 mixed。

## 7. 人工检查、预算与公开命令

建议 lane：local_fourth_derivative_factors。只需 topic/scripts 和正常 README/request/publisher 文件，不需要取旧大原式数据。

从 topic 目录运行：

~~~bash
python3 -m py_compile scripts/literature_local_fourth_derivative_factors.py
python3 scripts/literature_local_fourth_derivative_factors.py \
  --toy-only --out computations/run-local-fourth-derivative-factors/local-fourth-derivative-factors-development.json
python3 scripts/literature_local_fourth_derivative_factors.py \
  --max-seconds 600 --memory-mib 1024 --max-export-bytes 4500000 \
  --out computations/run-local-fourth-derivative-factors/local-fourth-derivative-factors.json
~~~

八项新人工检查只用手造三次/四次 profile 表达式、手造几何矩阵与一个 RHS=7 的人工 history，检查：

- $N^{[0]},N^{[2]}$ 两部分都保留；
- $v^{[2]},v^{[4]}$ 两部分都保留；
- 全部原 DAG hash roundtrip；
- 累计值置零后其真实 RHS 导数仍为七；
- static=False 保留真实几何 jets；
- 新第三 jet adapter 保留人工 $h_s h_{sss}$，准确总权为四；
- 非声明导数权被拒绝；
- 未运行研究目标或实际 $m=8$ 代入。

恢复终端后这八项人工检查已通过（见 local-fourth-derivative-factors-local-development-20261114.json）；未执行研究目标或实际 m=8 代入。人工导出使用人工矩阵覆盖，不调用研究用八矩公式。公开 lane 仍先运行其人工开发阶段。

实际总预算 600 秒、1024 MiB；系数节点 500000、profile atoms 100000、单表达式项数 100000、改写调用 1000000、有理数预算 8192 bits。完整原文上限 40 MB。早期原势 gzip 上限 1.1 MB；两个 gzip 的总计连同紧凑主报告预留后不超过 4.8 MB。全部完整输出由本公开 Actions 终端 Git 发布，不经 API 分片或编码。

## 8. 不授予的结论

原式导出完成只意味着新因子齐备。它尚未证明任何导数成本成员、符号、实际可达维数或零 period，也未计算任何几何路径、ruling 或有限等距族。后续消费必须把 $N^{[2]}$、原 $v^{[2/4]}$ 和 R124 诱导项一起保留，才能对剩余 pure 成本作新的判断。
