# R134 五族完整混合加速度层：原式消费器设计与冻结输入

日期：2026-11-14。此文件是新消费者的设计与开发回执，**不是实际目标已经计算完成的报告**。研究运行仅在 Rogerhu12/math-research-public 的 GitHub Actions。

## 1. 新问题与不重建的输入

[R134](../results/R134-acceleration-layer-from-complete-local-v4.md) 已证明，R129 的五个正规族

$$
\bar A_{hh},\quad\bar A_{hk},\quad\bar A_{kk},\quad H_1,\quad H_2
$$

只依赖完整 $v_4$ 的加速度与三阶几何导数项。由于 $m_2,N_2$ 均为速度二次，$B_{m_2}N_2$ 只影响速度四次层。本消费者不构造 N 响应，不把 N₂ 从整个第四成本中删掉。

新 [literature_acceleration_layer_mixed.py](../scripts/literature_acceleration_layer_mixed.py) 直接读取两份已经公开的原式导出：

1. 完整变量几何因子中的 $v_4$ 原根；
2. R131 的全部 50 个权负二响应、N³G 两模式原根及已完成证书。

没有运行旧 forcing、W36、常态目标、变量局部第四生成器或旧响应块的构造器。对新五族只取真权 −2，消费已证完整空间

$$
R_{8,-2}+\mathbb R N^3G
$$

的 41 个原列。其维数 41 来自 R131 的原式关系与有理子式，不来自本消费者假定正规形完备。

所有新五族的未分权原式同时保存，便于以后直接消费其他权；本次不研究那些权。

## 2. 几何算子及五族提取

几何十坐标与原导出一致：

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}).
$$

记 $u=h_s,w=k_s,a=h_{ss},b=k_{ss},j=h_{sss},\ell=k_{sss}$，状态算子为

$$
X=\partial_h,\qquad Y=\partial_k+\frac1{2h}\partial_\omega,\qquad
D_0=uX+wY.
$$

程序以原 profile 表达式为系数，对 $(h,k,\omega,\log h)$ 的 Laurent/多项式精确求 X、Y；$\log h$ 的链式项与 Y 的真实 $\omega_s$ 项均保留。

将原 $v_4$ 写为

$$
B_hj+B_k\ell+A_{hh}a^2+A_{hk}ab+A_{kk}b^2+C_ha+C_kb+Q_4,
$$

其中

$$
B_h=\beta_{hh}u+\beta_{hk}w,\qquad
B_k=\beta_{kh}u+\beta_{kk}w.
$$

只消费 13 种加速度/三阶导数单项：四个速度乘三阶导数、三个加速度二次、六个速度二次乘加速度。原速度四次项显式计数后跳过，不假装已付。

准确正规化为

$$
\bar A_{hh}=A_{hh}-\beta_{hh},\quad
\bar A_{hk}=A_{hk}-\beta_{hk}-\beta_{kh},\quad
\bar A_{kk}=A_{kk}-\beta_{kk},
$$

$$
\bar C_h=C_h-D_0B_h,\qquad \bar C_k=C_k-D_0B_k.
$$

若

$$
\bar C_h=\alpha u^2+\beta uw+\gamma w^2,\qquad
\bar C_k=\delta u^2+\varepsilon uw+\zeta w^2,
$$

则

$$
H_1=(2\delta-\beta)/3,\qquad H_2=(\varepsilon-2\gamma)/3.
$$

从原 1236 个 $v_4$ 系数每模式筛选，检查十坐标、导数权与完整原根哈希；未知导数形状明确报错。原 N₂/m₂ 记录的速度二次形状也检查，但不形成其 response。

由 R130 的真实 span 等式及 R134，每个独立状态单项系数属于实际 U₄。再由有限真实仿射作用取真权投影；所以本次新系数不是未经支付的形式“独立几何方向”。

## 3. 完整原因子绑定

固定来源：

- run：43651096112；
- source：2259b57065cfad67682f4c4319885fd5334c4f76；
- lane：local_fourth_derivative_factors；
- 生产器 literature_local_fourth_derivative_factors.py：22205 B，SHA256 02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf。

默认目录为 notes/actions-43651096112-1-local_fourth_derivative_factors：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| local-fourth-derivative-factors.json | 5477 | 42289590f4e8319d2bd4b138497702b701a11c4bcf39ba4c7ed0c2616f3aa927 |
| receipt.json | 33580 | 6857ea6edb3b8132147e3c0c698f79aa6f29e3b59272850267875f45a07fe95e |
| local-fourth-derivative-factors-original-expressions.json.gz | 2132064 | 9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a |
| 上行解压原始 JSON | 11864540 | 58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3 |

消费者同时核完整主报告、生产器及依赖身份、终端 git 发布回执、压缩/原始字节和 SHA，随后用旧原式 codec 还原 selected roots。不是依据文件名或摘要自行重建相近表达式。

## 4. 权负二响应绑定

固定来源：

- run：43653293263；
- source：2f0add61f44365d713abf836beaa8b0be2806a3d；
- lane：g_translation_successor，order 3；
- 原生产器 literature_G_translation_successor.py：39670 B，SHA256 a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406。

默认目录为 notes/actions-43653293263-1-g_translation_successor：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| G-third-translation.json | 25014 | b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3 |
| receipt.json | 34619 | a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523 |
| G-third-translation-original-expressions.json.gz | 157782 | 226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e |
| 上行解压原始 JSON | 889438 | eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7 |

入口检查全部 E8×W36 权负二的 50 列顺序与标签、所有 102 个两模式原根、已证明的 40 列上界及十条原式依赖摘要。取 R131 的保留原列并加 N³G；没有重新推导这些响应、重验旧子式或以 pure 投影替代完整两模式。

本次运行必须显式传主报告与 receipt SHA；默认路径/run/source/order 已指向上述实际。若修改来源或阶数，须明确重新绑定，不能默认另一个新块身份。

## 5. 新成员判断与一个原式对偶目标

按五族与状态单项确定性排序，对新的真权 −2 两模式系数去除**原式哈希完全相同**的重复项。先消费 41 个控制的有声 word 代表并拟合每个新目标：

- 代表余项为零时，重新用同一有理系数组成两模式原表达式之差，证明原式真零；
- 代表余项非零只记录为 unresolved，不作为函数非成员；
- 若有未决项，只选排序中的第一个，直接用同一真实有理 profile 对和原式右积分作一次 41/42 原矩阵检验；不自动遍历剩余项或增加预算。

原式评价仍用共同右锚、同一实 $f,g$、两模式实/虚和同一系数。消费者检查实际最大输入 jet 与固定测试 profile 正则性。分母/素数门和完整控制秩门全部保留。

若完整 41 控制列满秩且增广 42 子式非零，则证该真实 U₄ 系数不属于 $R_{8,-2}+\mathbb RN^3G$。由真分权，这给完整 $U_4/(R_8+\operatorname{span}\operatorname{Orb}(G))$ 的新方向。它只证明实际 span 的增量；没有据此授予该方向的有限有符号成本、闭锥 lineality 或完整联合支付。

若本轮所有目标都有原式成员关系，只支付五族的真权 −2；速度四次、L₂、其他 profile 权、P₀ 与 ruling 全部继续保留。

## 6. 可携输出、部分完成与预算

主文件默认为：

~~~text
acceleration-layer-mixed.json
acceleration-layer-mixed-complete-report.json.gz
acceleration-layer-mixed-original-expressions.json.gz
~~~

主 schema 为 visible-flex-complete-acceleration-layer-mixed-v1。补充原式 schema 为同名加 -original-expressions，scope 为 five-complete-two-mode-normal-acceleration-families。

原式导出在成员判断之前完成，包含五族全部未分权状态系数、两模式原根、选定权目标及别名、输入/生产器/当前 source 绑定，不重复复制旧响应根。保存成功后后续预算退出也保留它。补充导出超过预算会明确记录未完整导出，不用该额外输出失败替换已经成立的数学身份。

预算默认：

| 项目 | 上限 |
|---|---:|
| 本轮时间 | 240 秒，软检查 |
| RSS | 1024 MiB，轮询 |
| 原式评价次数/运算 | 24 个点；10000000 运算 |
| 原式多项式次数 | 256 |
| 主 JSON | 90000 B |
| 完整数学报告 gzip | 2500000 B |
| 新原式导出 gzip | 2000000 B |
| 三项预留总量 | 4590000 B |

大矩阵留在完整 gzip，主 JSON 保存维数/哈希/小元数据。每个完成的新成员证明立即进入 outcomes；异常回执保已完成证明及原式导出。研究部分要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY 恰为本公开仓库。

## 7. 最小公开 Actions CLI

从仓库根运行人工接口：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_acceleration_layer_mixed.py \
  --toy-only \
  --output "$OUT/acceleration-layer-mixed-development.json"
~~~

随后运行唯一实际新目标：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_acceleration_layer_mixed.py \
  --response-report-sha256 b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3 \
  --response-publication-sha256 a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523 \
  --output "$OUT/acceleration-layer-mixed.json"
~~~

输入大 gzip 只由 Actions 的仓库工作树读取，不经 API 分片读取。无需重跑任何已完成的 G³、原因子或 pure 尾研究。

## 8. 已做的人工开发检查与冻结字节

源文件 47656 B，SHA256：

~~~text
271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c
~~~

本地仅 py_compile 与 13 项人为表达式/输入接口检查，耗时 0.002658619 秒、RSS 15.875 MiB；没有读取实际因子或响应导出，没有编译/评价研究目标。

检查包含 X 对 Laurent/log 的导数、Y 的真实 ω 链式、完整三阶势消去、速度三次势的面积项为零、两独立 H 系数、13 种导数形状、纯速度四次不消费、未知高阶 jet 拒绝、q/qbar 原式保持、公开来源绑定与篡改拒绝。

[开发主回执](acceleration-layer-mixed-development.json)为 8411 B，SHA256 d78908002afbb162114ecb5910d3a4def19f381d5f07e44205d8605f62d4f288。其完整 gzip 为 2331 B、SHA256 2bca06f3d24355773ae6a8274c27a73062666317fa84ed460a1df2d31784e1cb；原始 JSON 为 8016 B、SHA256 cbd8a7b3aeba0f9009ab74a584b82593d817bcef7aa83ae823c7bb51243df66a。

这些人工回执只证明上述接口检查实际执行。真实新五族的数量、成员关系、是否有新商方向及实际资源用量，必须以随后公开 Actions 原始报告为准。
