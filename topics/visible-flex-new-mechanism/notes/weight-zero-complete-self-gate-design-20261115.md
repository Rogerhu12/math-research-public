# R316 设计：完整权零 pure 核上的十四个 full-self 目标

日期：2026-11-15。**设计与源码静态完成；十二项新人工和全部真实目标均尚未执行。** 新运行只由 root 在本公开仓库 Actions 调度。本稿不是新实际结果，也不预报秩、成员或非成员。

建议 lane：`weight_zero_complete_self`。

新主程序：`scripts/literature_weight_zero_complete_self.py`。
新坐标模块：`scripts/literature_full_self_euler_coordinates.py`。

## 1. 唯一新问题与完整比较范围

使用已发表 R196、R201 的真实权零空间，写成 $U^{(0)},R^{(0)}$，避免与 R225 的全权 pure 核记号混淆：
\[
\dim U^{(0)}=19,\qquad \dim R^{(0)}=16,\qquad
\dim\pi R^{(0)}=3.
\]
已知 $\pi R^{(0)}$ 的一组真基为旧 R126 列
\[
\pi R^{(0)},\quad \pi R^{(2)},\quad \pi R^{(3)}.
\]
上式上标括号在旧列标签中指 R126 原下标；下文用 “old” 明确区分。

R201 已给完整原身份
\[
H=C_2+\frac1{48}R_{\mathrm{old}\,0}
+\frac{11}{64}R_{\mathrm{old}\,2}
-\frac{13}{96}R_{\mathrm{old}\,3},\qquad
\pi H=0,\quad\lambda_+(H)=1.
\tag{1}
\]
本次只判
\[
\boxed{\mathcal Q(H)\ \stackrel{?}{\in}\
\mathcal Q(R^{(0)}\cap\ker\pi),}
\tag{2}
\]
其中
\[
\mathcal Q(V):u\longmapsto
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u^2,0).
\tag{3}
\]

比较空间是**全部**权零响应 pure 核，维数13。没有仅取 $Z18\times E8$，所以 R247 另外的完整 pure 核分支在此权块中也已覆盖。没有重新计算 R126/R196 的16维原函数秩。

本次不计算整个 $U^{(0)}$ 的 self 像，不恢复 $C_4,C_6$ 尚未保存的 pure 坐标，不假设全部权块的 self 可独立处理，也不评价一个固定圆。目标是一个闭合、可决定的完整函数问题，而不是 principal 条件、单个母函数或必要采样。

## 2. 十三个 pure 核基只需已保存的三行

R116 已保存三个真实 pure 查询行
\[
(c,r)=(0,32),(1,31),(2,30).
\]
冻结 R234 读取器把它们与 R126 原第三根 SHA、quadratic 名称和原索引逐列绑定。R201 已证明 pure 像恰为3维，这三行在该像上忠实。因此这里只读取原 Fraction 数值，不再评价任何 profile，也不再规范化旧 pure 根。

令 $v_j\in\mathbb Q^3$ 为旧16列的三行值，以已知三基列组成 $3\times3$ 矩阵 $M$。只恢复这个已知基的逆坐标。对其余13个旧列，
\[
K_j=R_j-\sum_{\ell\in\{0,2,3\}}
(M^{-1}v_j)_\ell R_\ell .
\tag{4}
\]
源码逐列重新乘回三行并核精确为零。

每个 $K_j$ 在自身非基原列上的系数为1，在其他非基原列上为0；旧16列已经是真基，所以这13列线性独立。三行的满像维数为3，故它们恰为 $R^{(0)}\cap\ker\pi$ 的完整基。此证明不用再次做旧16列的函数秩消元。

新 full-self 目标因此恰为
\[
K_1,\ldots,K_{13},H .
\tag{5}
\]

## 3. 从完整 mode −2 原根得到 full self 的准确因子

R105 的 canonical 成本只含偶相位，且 $\theta=0$ 时完整第二、第三场和第四 forcing 都为零。对 $f=u,g=0$，
\[
V_\theta=A+B\cos^2\theta+C\cos^4\theta,\qquad A+B+C=0.
\]
按原 Fourier 规范，负2模式为
\[
M_{-2}(u,u)=\frac{B+C}{4}=-\frac A4.
\]
因此
\[
\boxed{\mathfrak q_u(V)=-[x^2]_{\rm left}M_{-2}(u,u).}
\tag{6}
\]
这是完整成本，不只是一个高阶 symbol。

首先在**全部原 DAG 内部**同时把 $q,\bar q$ 都代为同一个真实 u；不能只改最外局部因子。随后用既有同右锚 sound word 转换处理所有原积分、shuffle 和分部积分，最后才把最外 u-jets 置零并读取显式 $x^2$ 系数。字母内部的 profile jets 始终保留。

该顺序等价于先对真实原式作两次 $x$ 微分、再外零并乘 $-1/2$；不能先把所有积分节点当成常数。新人工使用
\[
M=I\bigl(xI(u^4)\bigr),\qquad I=\int_{r_*}^{x},
\]
检查嵌套增量确给 $\mathfrak q=\frac12\int u^4$，也直接对照原 $D^2M$。若先冻结外层 primitive，就会错误得到0。

完整左尾应为至多二次多项式。新模块保留全部次数并核这一界；有更高次数时如实报告接口失败，绝不先删去。

## 4. R314 的有限忠实坐标如何由原式取得

原 primitive 使用 $I=\int_{r_*}^{x}$。在共同左零 collar，
\[
I(a)=-\int a,\qquad
I(aI(b))=\int_{x<y}a(x)b(y)\,dx\,dy .
\tag{7}
\]
所以规范单字母词的系数 c 对应局部密度 $-c a$；规范二字母词的系数保正号。

对 (5) 的每一个 pure-zero 成本，R314 已证明
\[
\mathfrak q_u(V)=\mathcal N_{\mathbf T(V)}(u)+\int L_V(u),
\quad
\mathcal N_A(u)=\int_{x<y}j_u(x)^TAj_u(y),
\tag{8}
\]
\[
j_u=(r^2,xr^2,x^2r^2+2v^2)^T,\quad v=u',r=u''.
\]

新模块按以下确定顺序处理：

1. 所有原积分转换成固定颜色余型 words；这一 sound IBP 保留三角积分对角产生的局部项。
2. 左 $x^2$ 系数中的一字母词给完整 $L_V$。
3. 二字母词必须准确为九个 $\mathcal N_{ij}$ 的展开。每个 $j_i$ 的 $x^ir^2$ 字母是唯一主字母，所以 $(i,j)$ 矩阵项直接由 $(x^ir^2,x^jr^2)$ 词的系数读取；随后把全部九项连同 $j_2$ 中的 $2v^2$ 展开，逐字重构整个二字母部分。
4. 任意额外长词、非二次二阶双字母、未能重构的双核、或超过 R314 局部 jet 界的项都保留为失败原因，不能称非成员或近似零。
5. 从 $L_V(x,u_0,u_1,u_2,u_3)$ 形成完整 Euler 多项式
\[
\mathcal E(L)=L_{u_0}-D L_{u_1}+D^2L_{u_2}-D^3L_{u_3}.
\tag{9}
\]
不只记录三阶平方项；所有 $C^2$ 余项和它们的 Euler 系数一起保留。

坐标为
\[
\boxed{\bigl(\mathbf T(V),\operatorname{coeff}\mathcal E(L_V)\bigr).}
\tag{10}
\]
R314 已证明它忠实：两个坐标同时为零，当且仅当完整 self 对全部真实紧 u 为零。非成员结论来自这个定理和准确有理对偶，不依赖“非零 NF 必非零函数”的捷径。

相应的 exact word 重构还逐列核
\[
\mathcal Q_{\rm word}
=\mathcal N_{\mathbf T,\rm word}
-\sum_{\text{local monomials }m}[m]L\ I(m).
\]
因此不会只凭抽象 locality 删除实际项。

## 5. 真权检查保完整项，不作先验裁剪

原完整 mixed 根真权为0。左二次输出系数的 self 权为 $-2$。一个含 k 个字母的 self word，其权为各字母 $x$ 次数减 jet 阶总和、再加 k。

每个非零原 self word都逐项核权 $-2$。$L$ 的普通密度权为 $-3$，Euler 系数也满足对应准确齐次关系。九矩中
\[
\mathcal N_{ij}\ \text{的权为}\ i+j-6,
\]
所以该权块若出现非零矩阵项，其指标必须满足 $i+j=4$。源码依然生成全部九项，然后核真权；没有预先只留下 $(2,2)$。

## 6. 输入、保存状态和必要恢复的准确范围

全部输入目录沿用已完成 R234，只有五个：

| 用途 | 目录 |
|---|---|
| 完整静态原根与 W | `notes/actions-43645177423-1-local_fourth_quotient` |
| R126 原16响应标签与原 SHA | `notes/actions-43649525432-1-g_first_translation` |
| 已完成 H0 身份 | `notes/actions-43681388902-1-character_head_zero` |
| R201 pure 身份与维数 | `notes/actions-43683171512-1-character_zero_pure_readout` |
| 三个已保存 pure 查询行 | `notes/actions-43646543691-1-full_m8_tail_response_projection` |

R234 冻结读取器的文件、main、receipt、packed/raw SHA、run、source、schema 和 publication 输出绑定全部继续使用。旧数据不改写。

必要恢复只有：

- 按同一八参考状态 $\Gamma$ 原组合提取 C2 mixed 根，核已发 SHA `b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f`；
- 恢复16个未持久化的旧 mixed 响应输入，并逐个核 R126 原 SHA；
- 组合 H 并核 R234 已发 mixed SHA `3be041da7463195066061c4fea47881cedb8c65e69fc65b063748dc7264de325`；
- 读取48个已存 Fraction pure 值，恢复13个核坐标。

这些是必要原输入恢复。新的数学运算是14个完整 self、九矩/全部 Euler 坐标及一次成员/非成员消元。没有恢复旧 pure 根，没有重复旧三查询，没有重复 R196 的38列/318行全 H0，没有调用 R234 的17个一次端层，也没有重新编译3974个 forcing 或新增 N 响应。

原16列顺序仍为
\[
0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19.
\]

## 7. 完整成员与非成员证书

对 (10) 的全部字面有理坐标做消元，前13列是比较空间，第14列是 H。

### 成员

输出完整13个核列的有理系数，并回代到原16个 R126 列。三个已存 pure 查询的组合重新核为0。然后从
\[
H-\sum b_jR_j
\]
的**原始 mixed DAG**形成全差，另建一个无原 NF 缓存的新 word mapper，重新全局同色、完整同锚归约及 self 取出。要求新全部矩阵/Euler坐标准确为零，并重新核完整 word 等于所输出的 N_T+L。非零 sound word 中的局部 total derivative 不能单独作为失败门：完整 self 为零由 R314 的 Euler 忠实性支付。fresh word 的实际项数及字面零标记只作观察字段，不作为额外成员前提。

这给一个明确的新代表
\[
H_{\rm self}\in U^{(0)},\quad
\pi H_{\rm self}=0,\quad
\mathcal Q(H_{\rm self})=0,\quad
\lambda_+(H_{\rm self})=1.
\tag{11}
\]
因此仅完整 universal self 也不能读出该正字符。式 (11) 仍为真实线性空间结论，不是有符号实际成本、完整 period 或 ruling 解。

### 非成员

输出支持于有限 T/Euler 行的准确有理对偶，并重新乘回全部14列，结果必须为
\[
(0,\ldots,0,1).
\]
由 (10) 忠实性，这是真实完整 self 商非零，范围恰为 (2)。没有据此断言 $\lambda_+$ 在全 U 或固定圆上因子化，也没有排除其他真权的响应或未计算的 $C_4,C_6$。

### 资源或结构失败

不足14列、任何预算退出、坐标形状不合、fresh 原差不零或输出超限都不能报告一个完整数学决定。状态中保留真实阶段、已完成列数及异常，不把 partial 当作零，也不声称存在未保存的恢复 cursor。

## 8. 十二项仅新接口人工

公开开发入口 `--toy-only` 只执行以下新人工，无旧 profile 或数据读入：

1. 完整 Euler 杀一个明确四次 total derivative；
2. 三阶平方密度的 $u_6$ 主系数准确为 $-2(u_2)^2$，不删其余 Euler 项；
3. 九个有序矩阵项全部回构，尤其两槽不强制对称；
4. 第三真实密度 $x^2r^2+2v^2$ 在两槽的 $1,2,2,4$ 系数；
5. qbar 位于原积分内部时仍全局代为 q；
6. $I(xI(u^4))$ 的原两次微分、嵌套增量与 Fourier 规范号；
7. 三角边界准确留下 $\int u u'(u'')^2$；
8. 不属于九矩空间的双核拒绝完成；
9. 额外四字母词拒绝截断；
10. 真成本权0到 self 权−2及错误权标签拒绝；
11. 小发明三坐标基到核的完整回代；
12. 独立新 mapper 对原复合差核完整 self 零。

截至本稿，这十二项没有执行，因此没有 “passed” 回执。开发失败只修其准确新问题，不触旧科学与冻结目标。

## 9. 预算、费用和输出

建议 actual：
240秒；1024MiB RSS轮询上限；有理8192bit；
单表达式/局部多项式100000项；
总新 word primitive 调用300000；
共享缓存250000项；
主摘要95000B；
完整内存证书8000000B。

新预算覆盖14列及最后fresh原差的总 primitive 调用。原 DAG 操作另由冻结 exact limits 的节点、原子、项、rational bit及时间/RSS轮询约束。`literal_monitor_operations` 和 `literal_monitor_maximum_integer_bits` 只描述被该监视器检查的操作，不冒全部 DAG 总算术或全局最大位数。完整实际 elapsed/RSS另报。

`MATHEMATICAL_RESULT` 打印最终原式决定/全部关系或对偶。
14条 `SELF_COLUMN` 打印每列完整九矩、局部密度、Euler系数、原根和转换hash。
`COMPLETE_REPORT` 打印有界完整摘要。
stdout中的完整坐标支持人读消费；不能只把它们放在随后删除的临时证书里。

certificate 包括全部新 self words、L、Euler、原组合和证书，始终只在内存；临时 summary 仅写 runner `@OUT@`。按规则15不提交 payload，不上传 artifact/Release，不切块。公开保留脚本、参数、run、SHA和人类结果。超95KB的主摘要不静默丢数学结果，而返回输出限状态。

## 10. 推荐参数与接线

开发：

```text
python scripts/literature_weight_zero_complete_self.py \
  --toy-only --max-seconds 30 --memory-mib 256 \
  --output @OUT@/weight-zero-complete-self-development.json
```


实际：

```text
python scripts/literature_weight_zero_complete_self.py \
  --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
  --R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation \
  --head-directory topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero \
  --pure-identity-directory topics/visible-flex-new-mechanism/notes/actions-43683171512-1-character_zero_pure_readout \
  --stored-pure-directory topics/visible-flex-new-mechanism/notes/actions-43646543691-1-full_m8_tail_response_projection \
  --max-seconds 240 --memory-mib 1024 --integer-bits 8192 \
  --max-terms 100000 --max-IBP-calls 300000 --max-cache-entries 250000 \
  --max-summary-bytes 95000 --max-certificate-bytes 8000000 \
  --output @OUT@/weight-zero-complete-self.json
```


新增接线仅该 lane、开发 flag、两个新源码和临时输出名。五旧目录保持稀疏检出。冻结 R234 科学依赖按同原hash保留；另两能量 lane 与旧当前科学请求不由本代理修改。root 独占 workflow/publisher/request/ref/Actions。

## 11. 冻结来源

新 helper：
`literature_full_self_euler_coordinates.py`，
10966B，
SHA256 `95ec818ce1fdf815b0390aaf2ad4f976a0dfc7bd0b5218899acd4f4bc271f9ba`，
UTF8 blob `a23d47c17144dd03e05dcee62c8bf9acf01bd82c`。

新 driver：
`literature_weight_zero_complete_self.py`，
27626B，
SHA256 `9347caeb4ff7ed54cc88f6c38183d4773d8e12125a5a9631412674550d42b78f`，
UTF8 blob `9fa2381120fd76ee9101dafa7afebb2fa9ce00de`。

最直接的冻结读取器：
`literature_character_zero_endpoint_layer.py`，
29604B，
SHA256 `bb7be8fc3fa6b98f3f69aca96e5145c6df1f3d581ea85d14aa7fb6ccfefe6a94`。
只消费其 source/input binding、C2/16mixed恢复与三个旧pure值函数，绝不调用其旧端层目标。

论文依据：
R105、R126、R196、R201、R234、R247及
[已发表 R314](../results/R314-ordered-matrix-defect-localization-and-faithful-Euler-self-coordinates.md)。

本稿只交付一个最小但完整的真函数门。尚无运行结果，尚未支付完整 period、共同固定 circle 的全部条件或真实成本的任意符号控制。
