# R153 后继设计：复用原 42×42 pivot，只评价 D0 与一组旧根的组合

日期：2026-11-15。**源码与最小人工开发已完成；实际研究尚未执行。** 真实原式评价只准在 Rogerhu12/math-research-public 的 Actions 中运行。

本稿接 notes/literature-h-axis-sharp-actual-20261115.md。其 D0 成员正规化余 205 项，仍未决；本次不增加正规化预算、不重构轴系数，也不扫描别的系数。

## 1. 唯一目标与已有完整比较空间

目标是已经公开保存的同一个

$$
\mathcal D_0=\Pi_{-2}[h^{-6}\log(h)^0]
\left(Q-\frac13\partial_h(C-\partial_h\beta)-\mathcal B_{m_2}(N_2)\right)
$$

的完整 $-4,-2$ 两模式，不使用 pure 投影替代它。

已有 R131、R136 原式证书给

$$
\mathcal S=\mathcal R_{8,-2}+\mathbb RN^3G+\mathbb RJ,
\qquad \dim\mathcal S=42.
\tag{1}
$$

同一个实系数向量必须同时作用两个模式。新源只消费已存的 40 个响应、$N^3G$ 与 J；不构造旧响应、不重跑旧原式依赖，也不把代表秩当真实上界。

D0 与派生 K0 的旧 portable export 已包含完整未归约 N2 贡献。本次只解码 D0 两根，不再次形成两条 N2 收缩，也不评价 K0。

## 2. 原回执确切保留了什么

已经只读解压核过 R136 的完整报告，stored/raw 双 SHA 与公开 receipt 完全一致：

~~~text
acceleration-layer-mixed-complete-report.json.gz
43071 B / af242f353bfb3e038615a8bc1f9d28752b75233be58f7f1a8ad8f89713110891
raw 175927 B / a106c8a0162ef7c51ca8ad03546ef2d7607f2dabe34a00169acad97c9ed9c9b4
~~~

它保存全部 96 个评价标签，但数值只保存原 42×42 增广子式，不含其他 54 行的旧列数值。这个增广子式在本次恰成为 42 列比较空间的满秩 pivot A：前 40 列为响应，第 40 列为 $N^3G$，第 41 列为 J。

原矩阵 SHA256：

~~~text
f0965e518249763e99e4d9770831bf147db401be9fc4bfe73c389e6cb7f307e5
~~~

原公开证明的

$$p=2147483647,\qquad \det A\bmod p=602105349\ne0.$$

保存的全局行索引为

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,
22,23,26,27,30,31,34,35,38,39,42,43,46,47,50,51,54,55,58,59,62,63,66
~~~

全部旧查询的排列为 $j=1,\ldots,24$，$t=j/25,\xi=2+t$，然后模式 $-4,-2$，再实部、虚部。这一顺序与完整旧源逐字节绑定。

本次不重新评价旧 42 列来填满一个 96×42 矩阵。只消费已保存的满秩子式。

## 3. 新的最小原式评价

沿用原来同一实有理测试对

$$
f(t)=[t(1-t)]^8,\qquad
g(t)=f(t)(1+2t+3t^2+5t^3),\qquad q=f+ig,
$$

支撑 $2\le\xi\le3$，$t=\xi-2$，所有原积分保持同一真实右锚。原 f、g 模多项式 SHA 与旧完整报告核对，不能另选 profile、重配矩或改锚。

步骤如下：

1. 只评价 D0 两模式的原 DAG，取已有 42 个 pivot 查询值组成 b。
2. 使用旧 $A\bmod p$ 解
   $$
   c=A^{-1}b\pmod p.
   \tag{2}
   $$
   直接核 $Ac=b$，不重跑旧矩阵的分离或秩证明。
3. 从已存原根 $U_0,\ldots,U_{41}$ 形成一次线性组合
   $$
   C_{\mathrm{lift}}=\sum_{j=0}^{41}\widetilde c_jU_j,
   \qquad0\le\widetilde c_j<p.
   $$
   这里只作原表达式的加法和整数数乘，不形成新的二阶×第三阶响应。
4. 只评价这个组合的两个原模式，得到
   $$
   E_p=\mathcal D_0-C_{\mathrm{lift}}\pmod p.
   \tag{3}
   $$
   同时核它在全部保存 pivot 查询上为零，检测原根顺序、标签、颜色或锚的任何不一致。没有逐列评价 42 个旧原式。
5. 若某一模式的某个实/虚分量是非零模多项式，设其实际次数为 d。取 $d+1$ 个
   $$
   t_j=\frac{j}{d+2},\qquad1\le j\le d+1.
   \tag{4}
   $$
   在声明次数上限下 $d+2<p$，这些点在模 p 下互异，且分母可逆。非零次数 d 多项式不可能全部取零，所以必得到一个实际有理查询的非零原余量。只使用同一个 f,g；没有新增 profile。
6. 若两个完整原模式的模多项式均为零，只报未决。它可能是真恒等，也可能只有这个固定测试对或这个模数消去；本次不进一步扩大搜索。

原评价直接递推 jets、乘积和右原积分，不经过 word normal form。

## 4. 为什么模候选系数足以给有理非成员证书

设 $A_{\mathbb Q}$ 为真正有理评价矩阵。旧来源保证其全部分母在 p 可逆，且其行列式为 p 单位。因此

$$
a=A_{\mathbb Q}^{-1}b_{\mathbb Q}\in\mathbb Z_{(p)}^{42},
\qquad a\bmod p=c.
\tag{5}
$$

这里 a 不是实际计算出的模整数列表；报告明确不把 $\widetilde c$ 当作 a。即使最初只假设实数系数的全函数成员关系，原有理可逆 pivot 也迫使唯一系数等于这个有理 a；因此下述分离排除真实实 span，不只排除有理 span。

若 $\mathcal D_0\in\operatorname{span}_{\mathbb Q}\{U_j\}$，全函数系数只能是这个唯一 a。于是每一个查询 $\operatorname{ev}_*$ 必须满足

$$
\operatorname{ev}_*\!\left(
\mathcal D_0-\sum_j\widetilde c_jU_j\right)\equiv0\pmod p.
\tag{6}
$$

因此 (3) 在任何新实际查询上非零严格否定真成员，尽管并未逐列算出这个额外查询的 42 个数值。

等价地，定义真实有理泛函

$$
\Lambda_{\mathbb Q}
=\operatorname{ev}_*
-\operatorname{row}_*(U)\,A_{\mathbb Q}^{-1}
\operatorname{ev}_{\mathrm{pivot}}.
\tag{7}
$$

由定义它准确杀全部 42 原列。式 (3) 的新查询值就是 $\Lambda_{\mathbb Q}(\mathcal D_0)$ 的模 p 约化。其 43 阶增广行列式的约化由准确 Schur 恒等式给出

$$
\det(A_{\mathbb Q})\Lambda_{\mathbb Q}(\mathcal D_0)
\equiv602105349\, E_p(\xi_*)\pmod p.
\tag{8}
$$

这给一个由原矩阵、真实原 DAG 与组合评价组成的证书；不伪称已经保存了未逐列评价的额外整行，也不把模泛函系数当作 Q 系数。

旧分母回执和本次全部新原式/查询分母各自保留。即使旧 pivot 上的负证书已经完成，本次依然核组合在旧行上为零，以绑定新目标和组合顺序。

## 5. 全部输入绑定

| 输入 | 公开 run/source | 用途 |
|---|---|---|
| D0 | 43657526246 / 0d5df1843fd829e7c09b17afdead930ec4395f34 | 两模式原目标 |
| J 及原 pivot | 43654534244 / 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b | 第 42 列及原 42×42 满秩证明 |
| 原响应块 | 43653293263 / 2f0add61f44365d713abf836beaa8b0be2806a3d | 40 个真响应和 $N^3G$ |

每一项都绑定小主报告、publisher receipt、原导出 stored/raw 双 SHA、原 producer 源码 SHA、完整角色标签及原根 hash。新脚本导入冻结的 D0 与 R136 输入 helper，不调用其 study/main。

D0 主报告 17542 B，SHA256

~~~text
e0007757b7d113a34b5c2ec594a607d380855f5652042f67fe3f32c1c81397f0
~~~

其 receipt 36161 B，SHA256

~~~text
1d635cdbe80251339d1157cee579c6838cad8975310a80959ef92b171f2458ea
~~~

D0 original export 14497 B，SHA256

~~~text
ecd9edf2d461f6d4f6b9355e17e210ad435b20c53bc16baeda412258b8b3fabd
~~~

解压 80444 B，SHA256

~~~text
2d0433a628b22f223a0f8700cebad02e70305699ff39a65e075de81dad5ceed0
~~~

完整两个 D0 原根为

~~~text
-4: 1236f94a788454870d655dda499714eacccfee730cba582e22fb2c0b4d892f7f
-2: ce6e1dd221080cd0a4961f2cf81b9a1be1f8a276d587b0cd34e0dd884fd83c5f
~~~

## 6. 输出与判定范围

默认 180 秒、软轮询 1024 MiB、模多项式最高次数 256、20000000 次操作检查。已有相似的完整解码约使用 222 MiB；这里没有无理由把内存预算压至输入无法容纳。

输出：

- D0-pivot-residual.json：小于 90000 B 的完整状态、输入身份、旧 pivot 摘要、新求解、实际余量与非成员/未决门；
- D0-pivot-residual-complete-report.json.gz：原保存 pivot、所有标签/列绑定、新目标值、模坐标、原残差的完整模多项式系数和 (7)–(8) 的可复查证据；
- D0-pivot-residual-original-residual.json.gz：D0、一个旧根线性组合、原残差的两模式原 DAG，明确整数系数只是模坐标的 lifts。

完整报告预算 2 MB，新原式预算 1.5 MB，总预留 3.59 MB。补充原式若超额，会明确记录没有导完，不把已经取得的数学证据改成“数学失败”。其他异常也写出有来源的小报告。

若分离成功，结论限于完整 D0 不在 (1)，并可结合 R130 的真系数 span 身份讨论新增商方向。它不自动给真实有符号成本、lineality、正性泛函或完整 ruling。

使用的测试对本身没有三矩配平；成功首先给普适算子身份的否定。若需要同一个合法光滑圆上的后继范围，应另明确使用既有平滑/左补偿论证，不在本次 raw 矩阵声明中偷加。

## 7. 人工开发和最小公开 CLI

新代码只在本地跑过 **15 项小人工检查**：此前 14 项固定 pivot、模坐标、Schur 身份、原式组合等接口检查，加一项针对本次实际故障的共享标签别名检查。后者明确验证追加 J 后旧发布字典仍保持原 41 列列表，而新比较空间独立扩到 42 列。

没有读取实际原根或报告，没有评价研究 profile/D0，没有重跑旧列。

冻结 source：

~~~text
literature_D0_pivot_residual_probe.py
32755 B
e6a4c15bfe95c587c4cde0cae26b33cf0bf4f54f0ea7b9cfb5c83026c98afbcd
~~~

开发报告：

~~~text
D0-pivot-development.json
6738 B
846cb400b52045f98ffdcec23e461543c98a87f80021560d091519aa591102f2
~~~

人工耗时 0.003270470 秒、RSS 14.875 MiB。此报告不冒公开 actual 回执。

最小 Actions CLI：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_D0_pivot_residual_probe.py --toy-only --output /tmp/D0-pivot-output/D0-pivot-development.json
python topics/visible-flex-new-mechanism/scripts/literature_D0_pivot_residual_probe.py --output /tmp/D0-pivot-output/D0-pivot-residual.json
~~~

三个实际目录、SHA、原 run/source 均有准确默认值；CLI 允许搬移文件路径，不允许悄悄更换其身份。新研究路径还检查 GITHUB_ACTIONS=true 和 GITHUB_REPOSITORY=Rogerhu12/math-research-public。

## 8. 第一次公开回执与唯一接口修复

run43658525976/source38fde5a460ac39c4d0b12b5e88309bceeb3ded22 的小主报告公开保留在 notes/actions-43658525976-1-D0_pivot_residual/。其状态为 implementation_check_failed，耗时 0.429821976 秒，阶段仍是 read_only_completed_D0_and_existing_original_comparison_block；新研究 profile 评价数为零。

错误是追加 J 时沿用了 frozen layer helper 返回的同一个标签 list，而该 list 同时挂在已经绑定的旧 report.response_input 中。原位 append 把它从 41 列改为 42 列，随后与 R136 完整报告的只读身份比较正确地拒绝了这个被改写的元数据。

修复只把 controls 和 labels 各自复制为新列表，再追加 J；旧来源记录保持原样。新增人工例直接复现并检查这一 alias 边界。原目标、原根、原矩阵、所有 SHA 绑定、查询策略和预算均不变，不重做已完成的旧代数或原评价。

第一次回执不是数学阴性或资源退出；不修改它，也不将修复后的人工通过当作后继 actual 已成功。

