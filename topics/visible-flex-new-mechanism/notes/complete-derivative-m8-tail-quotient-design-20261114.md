# 完整原导数成本的 m=8 pure 消费：L2、L4 与真实矩阵补项一起保留

日期：2026-11-14。状态：新源码已通过本地 py_compile 和五项新人工小例检查；研究实际尚待公开 Actions。完整因子生产者本轮仍需完成后，本消费才能取得准确 run/source/hash 入口。

对应 [literature_derivative_m8_tail_quotient.py](../scripts/literature_derivative_m8_tail_quotient.py)。本消费不调用任何原式编译器，不重算已成静态目标或旧响应公式。

## 1. 完整新目标

R124 已从真实零矩和完整静态成员身份推出

$$
[\Pi_8 V_B]_{\mathcal T}
=
\left[\int_B\Pi_8\{L^{[2]}+\Delta L^{[2]}+L^{[4]}\}\,ds\right]_{\mathcal T}.
$$

本次逐系数评价括号内的整个新密度，保留

$$
L^{[2]}=v^{[2]}-\mathcal B_{m^{[0]}}(N^{[2]})
-\mathcal B_{m^{[2]}}(N^{[0]}),
$$

$$
L^{[4]}=v^{[4]}-\mathcal B_{m^{[2]}}(N^{[2]}),
$$

和已经完整发表的

$$
\Delta L^{[2]}=-\sum_i a_i(m^{[2]})L^{[0]}(S_i^*).
$$

$N^{[2]}$ 不被删除、不被假定在 $W$ 中；原 $v^{[2]},v^{[4]}$ 与矩阵补项都必须在输出里。

## 2. 三组字节与来源绑定输入

### 新完整导数因子

使用 literature_local_fourth_derivative_factors.py 的完成导出，源码固定为：

- 22205 bytes；
- SHA-256 02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf。

必须有完整 main、真实 publication receipt 和完整 factor gzip。实际 source run、commit、main SHA、receipt SHA、export SHA 全部通过 CLI 明确绑定；生产者尚未完成时不填猜测值。消费器同时比对当前完整 source_hashes、main、receipt 的 source_files/outputs 以及 gzip 的原文身份。

content_scope 必须是 unreduced-N0-N2-and-complete-two-mode-v2-v4。早期 N-only 导出不能替代完整数据。全部原 roots 由冻结 decoder 重算原内容 hash，完整 mixed roots 保留在来源数据中；本消费仅选择 pure $-4$ 评价。

### R124 完整矩阵诱导补项

固定 run 43649160345，source c69562728ce9d0f5115ad2710d45bcff15762693，目录 notes/actions-43649160345-1-constrained_static_m8_tail_quotient：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| constrained-static-m8-tail.json | 7892 | 297c6716a7cf23d1c6006a273f251640bc4c0da878da07d68ef981af43ba65b7 |
| receipt.json | 32633 | 8b8e3aff681ccbb15a879040d4a69aad94900b00eadae0130571c36b9b18679e |
| constrained-static-m8-tail-certificate.json.gz | 57845 | 022cd4f767d40b5ad21089e4cf88f7f6d4e6e051b7d730c038e87ab0e0961175 |

完整原文 489034 bytes，SHA-256 ced7357546b2c85610cf200e961c4e568a7a8f53407bf8da033eee8b9cb86ed7。

完整 18 个诱导补项三元记录 $(P,A,R)$ 全部读取并核对。不会只读取其两个独立余项，也不把它代替原 $L^{[2]}$。

### R116 完整响应多项式

固定 run 43646543691、source f0652a013fe546778300f0213e659f63ab96ed07 的主报告、receipt 和 full-m8-tail-response-certificate.json.gz，沿用冻结来源门。

对已发 31 个原基列作仅供新目标分解的一次因式分解。旧响应公式和旧依赖没有重算。另读取全部 288 原列的 third original hash 与 quadratic index，组成复用表：若某个新 N 原 root 恰与一个旧 W 原 root 同 hash，直接消费该旧响应多项式，绝不再次执行其旧公式。

## 3. 十个几何坐标与完整槽序

几何键顺序为

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}).
$$

新原式中的三阶 jets 必须保留。旧 R124 八坐标键仅在末尾补两个零，不重排任何原坐标。导数权为

$$
j_h+j_k+2j_{hh}+2j_{kk}+3j_{hhh}+3j_{kkk}.
$$

源数据对真实 raw DAG 的最高 $s$ 导数阶已有扫描。本消费不按总权猜测最高 jet 已消失，不剪掉末两个坐标。

同一 profile 右锚始终为 $c$。代

$$
q=(c-\xi)^8,\quad r=c-\xi,\quad I_c=-J.
$$

完整原 N 的外槽 a、内槽 b,c 保持原顺序。使用冻结 OriginalTailThird 直接评价原 DAG 的 jets 和嵌套 primitive；没有自由 primitive 常数或独立 history 参数。

对 $\mathcal B_{E_i}(N_\gamma)$，沿用 R116 的完整 pure 响应适配器及其 $1/16$。源 $v_{-4}^{[2/4]}$ 已是完整相位系数，不再除一次 $16$。

## 4. 新计算复用与完整装配

只评价以下三组矩阵/势组合：

- $m^{[0]}$ 与 $N^{[2]}$，贡献 $L^{[2]}$；
- $m^{[2]}$ 与 $N^{[0]}$，贡献 $L^{[2]}$；
- $m^{[2]}$ 与 $N^{[2]}$，贡献 $L^{[4]}$。

同一个原势 root 和 quadratic index 的响应只算一次。不同几何系数共享完全同 hash 的表达式时复用缓存；第三组与第一组重叠的响应同样复用。与 R116 完全同源的旧列直接读取。

先得到完整原 $L^{[2]},L^{[4]}$ 的新多项式，再作准确响应商分解。R124 的诱导项携带已发表的原基系数和余项，作为整个三元记录加到 $L^{[2]}$。加法后的完整差式直接由原 31 个响应多项式核验，不重复旧补项的 profile 代入或商计算。

原势本次使用未模 $W$ 化简代表。旧静态 N0 的代表变化有逐系数真实 W 证书；乘任一真实矩阵坐标只改变 R8 项。因此同一 pure 响应商中可与旧 R124 补项组合。输出明确记录该代表变化，不在取商前宣称两个完整原密度相同。

## 5. 输出四组完整结果

完整 gzip 证书包括：

1. 原 $L^{[2]}$ 的所有几何系数多项式和原响应分解；
2. 加入完整 R124 补项后的 $L^{[2]}+\Delta L^{[2]}$；
3. 原 $L^{[4]}$；
4. 完整剩余导数密度两组几何系数合并后的响应商。

每组都输出未分权系数商秩、先真 profile 权投影后的商秩、偶总次数投影秩、独立几何键和全部新依赖。所有非零余项完整保存，不把它们限制到旧响应的 45 行支撑，也不假定只有旧的两个剩余权。

另外保存每个新 $v$ 系数的 pure 多项式、每个新 N response 的完整多项式、原 root 身份及旧列复用索引，以便后续只消费这些结果做真实几何积分分部或端点势分析，无须重算本轮新目标。

主报告紧凑；完整证书原文上限 40 MB，gzip 上限 4.5 MB，给主报告和人工记录留出总 4.8 MB 预算。大数据由公开 Actions 终端 Git 保存，API 不取 gzip、不分片、不编码。

## 6. 公开运行条件与参数

建议 lane：derivative_m8_tail_quotient。sparse checkout 需要：

- topic/scripts；
- 新因子 producer 实际发布的 notes 目录；
- notes/actions-43649160345-1-constrained_static_m8_tail_quotient；
- notes/actions-43646543691-1-full_m8_tail_response_projection；
- 正常 README/request/publisher 文件。

先执行：

~~~bash
python3 -m py_compile scripts/literature_derivative_m8_tail_quotient.py
python3 scripts/literature_derivative_m8_tail_quotient.py \
  --toy-only --out computations/run-derivative-m8-tail/derivative-m8-tail-development.json
~~~

实际命令必须补入**已发表的**以下八项因子绑定参数：

- --factor-report；
- --factor-report-sha256；
- --factor-publication-receipt；
- --factor-publication-sha256；
- --factor-export；
- --factor-export-sha256；
- --factor-source-run；
- --factor-source-commit。

其余 R124/R116 输入均有精确硬绑定默认路径。实际运行选：

~~~bash
python3 scripts/literature_derivative_m8_tail_quotient.py \
  [已发表因子的八项准确绑定参数] \
  --max-seconds 600 --memory-mib 1024 --max-operations 10000000 \
  --out computations/run-derivative-m8-tail/derivative-m8-tail.json
~~~

五项新人工检查只用手造低次多项式：验证新原密度完整余项、补项相加而非替代、三阶几何 jets 保留、旧八键只补零，以及没有读取研究输入。已在恢复终端真实通过，0.002395115 秒；报告 complete-derivative-m8-artificial-development.json 为 5127 bytes，SHA-256 259dc030c697966493f37be8e9346a68a063dd075660d9e5751ce8b890c615d8。公开实际仍须读取真实完整因子；人工通过不替代它。

## 7. 结论范围

完整新密度加入后，若逐系数商为零，可准确推出相应 pure 幂尾周期商为零；若不为零，则仍需真实几何积分分部、端点势、$M=0$ 及端口条件，不能从非零局部余项直接推符号或不可行。

本消费不做真实几何积分分部，不计算实际路径，不宣布成本锥、完整两模式商或 ruling 已支付。完整 mixed 因子已经保存在 producer 数据中，后续研究可另行消费，不能由本 pure 结果代替。
