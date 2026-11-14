# 真实矩阵约束下的静态 m=8 纯尾商与导数补项：第二阶段消费设计

日期：2026-11-14。状态：新代码已静态核读，尚待公开 Actions 的 py_compile、六项新人工检查和研究实际。本稿不预写未运行的检查为 passed。

对应独立脚本 [literature_constrained_static_m8_tail.py](../scripts/literature_constrained_static_m8_tail.py)。R123 原消费器及其全部输入保持冻结。

## 1. 需要支付的具体边界

R123 已完整评价全部 197 个静态 $-4$ 几何系数，在逐真权投影后模 R116 响应空间的商维数为三：权 $-1$ 一维，权 $0$ 二维。该结论尚未施加真实 $M=0$，不能把几何系数积分视为自由变量。

R73 的实际矩阵密度只有几何导数权零和二：

$$
m=m^{[0]}+m^{[2]}.
$$

R114 的八个基准常态给固定线性坐标 $a_i$，满足 $m=\sum_i a_i(m)m(S_i^*)$。沿常值端芽的真实零矩路径，

$$
\int a_i(m^{[0]}+m^{[2]})\,ds=0.
$$

因此若 $F_i=L^{[0]}(S_i^*)$，准确规范化应同时保留

$$
\widetilde L^{[0]}=L^{[0]}-\sum_i a_i(m^{[0]})F_i,
$$

以及导数权二的已知诱导补项

$$
\Delta L^{[2]}=-\sum_i a_i(m^{[2]})F_i.
$$

原始的 $L^{[2]}$ 和 $L^{[4]}$ 尚未评价。新代码不把 $\Delta L^{[2]}$ 冒充整个导数权二密度，也不把 $\int m^{[0]}=0$ 当作已知。

## 2. 本次只消费已发完整多项式

输入一为 run 43648433010、source df535c0c42d76040903b1e89c6d08d13ea360ad2：

- notes/actions-43648433010-1-static_m8_tail_quotient/static-m8-tail-quotient.json：10305 bytes，SHA-256 f48539fb8e38fda987aa97bbdf22b940ebe5525261b989e4afedcba628e96dcc；
- 同目录 receipt.json：32674 bytes，SHA-256 c21fc44371341f514e685842c2addee903ebb9fe338e3669e195cdd4b0c66bdd；
- 同目录 static-m8-tail-quotient-certificate.json.gz：47339 bytes，SHA-256 28e4e42ab2ee7c53b26b2df43d18c3622e2798424958656fbb9ecab647089305。

证书原文为 318551 bytes，SHA-256 8e9722de44643fe8d12ce18ce1637341b2df31e4318fadbf76280865d97a8f53。它保存全部 197 个完整 pure 多项式及 254 个真权分量的完整原响应系数和余项。

输入二仍是 run 43646543691 的 R116 完整响应证书及小 main、真实 receipt，全部沿用冻结第一阶段消费器的精确字节/hash/run/source 门。

这次无需重新读取 3.5 MB 的局部原式 DAG、无需重新代入任何 profile、无需编译原 forcing 或 $W$、无需重算一个旧响应。也不重新分解旧 31 个基列；只读取其已发完整原多项式，用于验证新线性组合的准确差式。

## 3. 同时携带完整多项式、原基系数和余项

每个原几何系数恢复为三元记录

$$
\mathsf P=(P,A,R),\qquad
P=\sum_{j\in J}A_j P_j+R.
$$

这里 $P_j$ 是原 R116 的 31 个独立响应列。R123 已给每个真权分量的完整 $(A,R)$；本次按原 target_index 将其加回整个几何系数，不重复旧 profile 计算。

所有几何线性操作同时作用在 $P,A,R$ 上。新结果逐项直接检查完整差式

$$
P-\sum_jA_jP_j-R=0.
$$

原余项在全部旧主元行上为零；新线性操作保持这一性质。所以非零新余项仍是准确投影商中的非成员，不是因为某次改写失败才留下的代表。

同时输出两种维数，避免把它们混称：

1. 未分权完整几何系数余项的真实多项式 span 秩；
2. 先逐真权投影后的系数 span 商秩。

R123 原静态未分权的商秩此前没有计算，本次直接用已发表余多项式相加得到，不重跑其旧分权秩。对新规范化静态部分和新诱导导数二补项，两种秩都完整输出，并另记录其偶总次数投影秩。

## 4. 八个真实矩阵坐标与完整导数二账

冻结几何接口：

- scripts/literature_constrained_static_fourth.py，24202 bytes，SHA-256 814e1338679914b32542f8b360978281002ee02a2c4e8c03912aa40c876786f4；
- reference_coordinates() 返回 $a_i(m^{[0]})$ 和真实八列矩阵的逆；
- BASIS_STATES 为 $h=1$、$d=0,1,-1,2$、$k=0,1$ 的八个常态，$\omega=d+k$；
- 完整 pointwise_matrix() 来自冻结原局部生产者。

代码不把 reference_coordinates() 返回的静态系数冒作完整 $a_i(m)$。它用同一个准确逆矩阵另乘完整 pointwise_matrix() 的导数权二部分，得到 $a_i(m^{[2]})$。随后在全部八个矩阵坐标上分别检验权零和权二的完整重构身份。

八个 $F_i$ 使用已发表完整多项式的几何 Laurent 系数评价取得。$h=1$ 时全部正次 $\log h$ 准确为零；不作近似。新 $\widetilde L^{[0]}$ 在八个基准态上的完整三元记录均必须准确为零。代码另外检验“规范化结果加回完整静态减项”等于原完整静态目标。

这只是在真实矩阵恒等式下规范化局部成本，不创建一条新的几何路径，也不把任意正负几何占用系数宣称可实现。

## 5. 输出和未付条件

完整新证书保存：

- 两份输入的来源与字节身份；
- 八个基准态、真实矩阵和逆矩阵、全部 $a_i(m^{[0]})$、$a_i(m^{[2]})$；
- 八个完整 $F_i$ 三元记录；
- 新静态规范化和诱导导数二补项的每个几何系数、所有真权分量；
- 原响应系数、完整余多项式、准确差式和新 quotient 依赖；
- 原未分权静态商、新两组未分权及分权商的准确秩。

主报告保紧凑，完整证书以 gzip 由本公开 Actions 的终端 Git 发布。API 不读取、分片或编码大数据。

仍未评价原始 $L^{[2]},L^{[4]}$，真实几何参数路径、全周期成本、mixed $-2$、ruling 或完整成本锥。新规范化后的非零系数也不能自动当成某条真实零矩路径的非零周期。

## 6. 公开运行入口

建议 lane：constrained_static_m8_tail_quotient。只需 sparse checkout：

- topic/scripts；
- notes/actions-43648433010-1-static_m8_tail_quotient；
- notes/actions-43646543691-1-full_m8_tail_response_projection；
- 正常 README/request/publisher 所需文件。

从 topic 目录执行：

~~~bash
python3 -m py_compile scripts/literature_constrained_static_m8_tail.py
python3 scripts/literature_constrained_static_m8_tail.py \
  --toy-only --out computations/run-constrained-static-m8-tail/constrained-static-m8-tail-development.json
python3 scripts/literature_constrained_static_m8_tail.py \
  --source-report notes/actions-43648433010-1-static_m8_tail_quotient/static-m8-tail-quotient.json \
  --source-publication-receipt notes/actions-43648433010-1-static_m8_tail_quotient/receipt.json \
  --source-certificate notes/actions-43648433010-1-static_m8_tail_quotient/static-m8-tail-quotient-certificate.json.gz \
  --response-report notes/actions-43646543691-1-full_m8_tail_response_projection/full-m8-tail-response.json \
  --response-publication-receipt notes/actions-43646543691-1-full_m8_tail_response_projection/receipt.json \
  --response-certificate notes/actions-43646543691-1-full_m8_tail_response_projection/full-m8-tail-response-certificate.json.gz \
  --max-seconds 240 --memory-mib 1024 --max-operations 10000000 \
  --out computations/run-constrained-static-m8-tail/constrained-static-m8-tail.json
~~~

所有输入路径均有同样的硬绑定默认，可省略上述路径参数；路径改变不授权内容改变。

六项新人工检查只用手造低次多项式和两个手造插值状态，检查三元记录线性身份、真权拆分、规范化零值、诱导项负号和错误差式拒绝。它们不调用真实八态矩阵，不读取研究输入，也不评价实际 $m=8$。

预算：240 秒、1024 MiB，准确多项式与消元操作各 10000000。完整输出原文不超过 40 MB、gzip 不超过 4.8 MB，主报告不超过 95 KB；失败照实保留完整回执，不以缩小目标冒成功。
