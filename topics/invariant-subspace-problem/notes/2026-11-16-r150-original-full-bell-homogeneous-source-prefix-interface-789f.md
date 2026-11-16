# 完整原 Bell 非零临界理想：有来源的齐次次数前缀入口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

本入口开始处理原完整临界理想的 Bell 非零部分。全部六个 $y$ 和十一个 Hankel 坐标 $H$ 均保留为不定元；没有选择参数点、删除临界方程或只取 pencil 的泛部。本次仅冻结源码，因共享执行环境离线，尚未实际 AST、调用 Singular 或运行数学。首次独立 Actions 任务必须先执行下述非平凡小来源自测。

## 1. 唯一原模型与系数域

使用已发表的 [完整原 Bell 系数及自然平方来源](../results/R150-appendix-complete-matched-bell-coefficient-charts-and-natural-square-nonmembership.md) 中未改动的物理模型生成器。固定
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),
$$
以及同一 matched direction
$$
r=(A,A+d,0,0,0,1),\qquad
A=-\frac{521d^2-46784d+271360}{160(5d-704)}.
$$
从完整 $K,J_3$ 直接重建 $R_3(y,H)$、十一条 $H$ 导数、六条 $y$ 导数和原 Bell 多项式 $b_r$。重建时实际核 $J_3$ 的全部 512 个双逆乘积、十七条独立 $N/\Gamma$ 身份，以及原加权 Euler 身份。所有零项和系数运输均由完整多项式比较决定。

原目标理想为
$$
\mathfrak a=(\partial_{H_0}R_3,\ldots,\partial_{H_{10}}R_3,
\partial_{y_0}R_3,\ldots,\partial_{y_5}R_3,\ b_r-1)
\subset E[y,H].
$$
原 $Z$ 的合法 Schur 消去、原 17 梯度和全 33 梯度之间的双向来源范围沿用已发表的原模型证明；本入口不引入新的参数分母。

本阶段只约化系数域到合法 place $127,d=100$。实际核定义多项式在该点为零、导数非零、首系数为单位，且所有使用的有理系数分母均为 127 单位。这里的 $100$ 是固定三次域生成元的像，不是对 $y,H$ 的取值。

## 2. 对 Bell 非零归一的完整齐次处理

引入一个新变量 $\tau$，权为 1。保留原权
$$
\mathrm{wt}(y_i)=1,\qquad \mathrm{wt}(H_j)=2.
$$
在全十八变量环中使用齐次理想
$$
\mathfrak a_h=(\nabla_HR_3,\nabla_yR_3,\ b_r-\tau^3).
$$
十八条原生成元的权依次是 $4^{11},5^6,3$。Singular 的次数边界只施加于此真正齐次模型，绝不把 degree bound 直接套在非齐次的 $b_r-1$ 上。

若实际得到
$$
\tau^n=\sum_{i=1}^{17}A_i(y,H,\tau)F_i+
A_{18}(y,H,\tau)(b_r-\tau^3),
$$
则代入 $\tau=1$ 严格给出
$$
1=\sum_{i=1}^{17}A_i(y,H,1)F_i+
A_{18}(y,H,1)(b_r-1).
$$
实际有限域来源由 Python/FLINT 再对全部十七个原变量独立乘回。这里只支付有限域恒等式；需要后续原 $E$ 上逐系数完整乘回才能宣布特征零判空。

反之，若原归一理想有 $1$ 来源，把其有限来源同时加权齐次化到足够高的同一权，就得到某个 $\tau^n$ 来源。因此此齐次入口保留整个 Bell 非零问题，而非一个局部参数图。

## 3. 每个完整次数的证书

首级权为 5，随后逐权增加。每一级读取上一已成的完整基 $G$ 及其原十八生成元来源矩阵 $S$；不恢复原大 normal-form 数组。计算
$$
G_{\rm new}=G\,T,\qquad S_{\rm new}=S\,T.
$$
只有下列门全部通过，才保存该级：

1. 每个新列满足完整原多项式身份 $G_{{\rm new},j}=\sum_iF_i(S_{\rm new})_{ij}$；
2. 原十八生成元逐条以新列约化为零，保留反包含；
3. 新列及每个原来源系数的所有单项式具有准确齐次权；
4. 枚举全部新基列对。领先单项式互素的对用标准乘积准则；其余每一个 lcm 权不超过本级的 S 对都实际约化为零。高权对只记录数量，留待更高级；
5. 全部结构化输出完整解析、无重复 monomial、无漏列，并绑定压缩和逻辑双 SHA。

这给出该权内的完整齐次标准基前缀，且每列都来自原十八生成元。没有把一份未经检查的 engine 标志当作完备性。Singular 的官方命令语义可参照 [官方教程](https://www.singular.uni-kl.de/ftp/pub/Math/Singular/doc/tutor.pdf) 及其 liftstd、reduce、degBound 文档；实际接口仍以程序的独立自测和完整恒等式门为准。

采用权反字典序且 $\tau$ 最后。每一已成基列均扫描是否为单独的非零 $\tau^n$。若出现，取该列的原来源并除以实际非零常数；代入 $\tau=1$ 后合并重复 monomial，独立乘回 $1$。若未出现，只报告已经核到的权数和当前基/来源规模；不宣称全理想非成员，更不宣称特征零不存在。

## 4. 非平凡接口自测

首次使用实际 Singular 二进制，先在 $\mathbb F_{127}[x,\tau]$ 对
$$
(x^2-\tau^2,\ x\tau)
$$
先计算完整二阶前缀，必须没有任何纯 $\tau$ 幂列；再把同一前缀连同原两来源作为输入，续至三阶，必须实际产生 $\tau^3$ 列及原两来源。恒等式
$$
\tau^3=x(x\tau)-\tau(x^2-\tau^2)
$$
保证此双级自测同时覆盖次数边界实际生效、前缀增级续接、非零纠偏、来源矩阵方向、系数规范、指数输出和原来源独立乘回。程序还用 FLINT 对自测中所有基列重新乘回，而非只检查最后标签。

版本探测保存实际 Singular 二进制 SHA 和 --version 输出。源码不自行安装软件；工作流安装受控依赖后调用。若接口或语法失败，原日志和错误完整保留，不能称为数学负结论。

## 5. 最小 inputs、CLI 和预算

没有历史大数据输入，historicalInputs=[]。仅取两份小源码：

| 项 | 完整 blob | 字节 | SHA256 |
|---|---|---:|---|
| 新 driver | c5e81e3e97d0123df214a994667c5b046171ec82 | 31156 | da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d |
| 原完整 Bell helper | 7e5244c7c9177d483bb2dbe2a1dc7a2dc86904a3 | 16964 | 31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10 |
| 本次 inputs | 2b5b2df1c20f7bbd0aec421d4100b2185d5f38b5 | 3319 | 09f5076b6645c1ab12efce611110d1889d3235e464c922afdc154c6dba1d4a25 |

依赖 Python 3、python-flint 0.9.0 和实际 Singular 命令。首轮建议 300 秒、4 GiB，外墙 360 秒。

~~~
python {scripts}/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py \
  --helper {scripts}/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py \
  --out {work}/original-full-bell-homogeneous-source-prefix \
  --singular Singular --through field --through-degree 9 \
  --seconds 300 --memory-mib 4096
~~~

若只需要先审实际原模型，可用同源 --through prepared。下一轮预算可变、through-degree 可增加，语义 binding 不变；源码或原模型 helper 改动必须使用新 out。

## 6. 续接边界与完整失败状态

每个已成级的全部基列和十八行来源矩阵保存为临时 gzip，mtime=0，manifest 只追加已完成级。续接读取最后一个完整级及来源，继续更高权。这里没有序列化 Singular 内部的未完成临界对队列；某一级途中停止时，该未完成级可重做，所有此前已付基和来源照旧复用。不得把这点表述为逐 S 对恢复。

记录每阶段脚本 SHA、原日志 SHA、实际秒数、父/子进程最大 RSS、基列数、来源非零槽/总项数和临界对计数。timeout/SIGTERM 为 exit75 budget-checkpoint；MemoryError、engine 语法或身份失败为 exit1，错误 type/message 同时写 parameters.error。两种情况均不产生任何数学否定。

若得到正列，额外保存完整
complete-original-affine-field-source-for-one.json.gz，包含十八条原 source 标签、逐项有限域来源、实际总支撑，以及明确的 characteristicZeroOriginalIdentityVerified=false。此物才是后继原 $E$ 有理来源求解的输入。

持久仓库只保存源码、参数、接口、执行身份与输出 SHA。全部原模型、基、来源矩阵和日志留在临时 job，服从现行根规则15。

## 7. 后继特征零提升的硬边界

有限域 $1$ 来源只用于挑选有限的真实原 source monomial 支撑。后继应从本次保存的原有理十七式和三次域 Bell 的完整系数重建 $E$ 线性系统，保留所有原单项式行，包括有限域约化后恰零的行。

固定 place 的单位只选择实际 $E$ 非零单位子式；解完后必须把候选的十八项原多项式乘回并严格得到 $1$。这一步才允许关闭原 Bell 非零临界理想。若当前选出的来源截面不升起，只说明这一截面失败；同一支撑中的其他截面或更大支撑仍可能成功。不得从一次有限域正证或提升失败推断原理想的正/负结论。
