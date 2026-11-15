# R234：权零 mixed −2 一次端层的真实 pure 零响应消去

日期：2026-11-15。此文记录公开 Actions run **43699241372** 的完整新计算及其严格推论。它结束 R230 所提出的本次一次层读出试验；不是完整 period 或 joint ruling 的完成报告。

数学责任范围：下述原式恢复、两个有限有理成员门和 fresh 一次层核验只在本仓库公开 Actions 实际执行；本文只解析既有 stdout 和 provenance，并作有限维线性推论。没有在本地重算研究目标。

## 1. 结论先行

记 $\mathcal U^{(0)}$ 为真仿射权零的完整成本空间，$\mathcal R^{(0)}$ 为该权响应块，$\pi$ 为 universal pure 投影。本文的
$\mathcal R^{(0)}_{\mathrm p0}=\mathcal R^{(0)}\cap\ker\pi$
只指**权零** pure 核，不是 R225 的全权 $\mathcal R\cap\ker\pi$。

令 $\mathfrak T=\mathfrak T^{\uparrow}_{0,-2}$ 是 [R230](R230-first-flat-end-layer-as-an-exact-cubic-tail-operator.md) 第 1、3、8 节定义的特定 universal 一次端层映射：**先限制真仿射权零，取 canonical mixed 模式 $-2$ 的原根，再取首个 $f$ 上升、局部 $g=0$ 的左平端 germ**。在该 germ 只令局部 $q=\bar q=f$，保完整同右锚三次尾函数，把局部一次项全部收齐。右侧两种颜色未合并，三次尾值没有被独立赋值。

这个 $\mathfrak T$ 不是所有端点、所有局部 profile 状态或所有权的联合观测。R230 第 8 节另已说明：对 whole pure 零的成本，完整两混合目标可由 $V_d=-4\operatorname{Re}V_{-2}$、$V_e=4\operatorname{Im}V_{-2}$ 恢复；该事实不把本次固定端口的一次层升级为完整 mixed 函数或全部端点联合层。

沿用 R126 的旧列编号 $R_i$，以及 R196 的静态原系数 $C_2$。新的明确代表为

$$
\boxed{
H_{\mathrm E}
=C_2-\frac18R_0-\frac1{64}R_1
+\frac{13}{32}R_2+\frac1{48}R_3
+\frac5{64}R_4-\frac1{32}R_{10}.
}
\tag{1}
$$

公开实际已付

$$
\boxed{
\pi H_{\mathrm E}=0,\qquad
\lambda_+(H_{\mathrm E})=1,\qquad
\mathfrak T(H_{\mathrm E})=0.
}
\tag{2}
$$

其中 $\lambda_+$ 是 [R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) 的真实正字符，杀整个响应空间。式 (2) 保留该完整正字符，并证明：**即使先限制到 whole pure 零的权零成本，单独的一次端层也不能读出 $\lambda_+$。**

这不是 $H_{\mathrm E}$ 为零。事实上 $\lambda_+(H_{\mathrm E})=1$ 已说明它是非零真实函数。也没有证明 $H_{\mathrm E}$ 的二次及更高端层、内部退化、总通量或平台条件已经满足。

## 2. 六条响应原列和准确比较对象

本次所有 $R_i$ 都是 R126 已发布的完整两模式响应列。恢复时只重建当时未保存 portable DAG 的 $-2$ 原根，逐列核原 SHA，不重原评价、旧 NF 或旧秩。

式 (1) 用到的列为：

| R126 旧下标 | 二次算子 | 完整第三模板 | 本次恢复 $-2$ 原项数 |
|---:|---|---:|---:|
| 0 | $p_0$ | $W_7$ | 800 |
| 1 | $p_0$ | $W_{17}$ | 1060 |
| 2 | $p_1$ | $W_1$ | 1047 |
| 3 | $p_1$ | $W_{12}$ | 549 |
| 4 | $p_1$ | $W_{16}$ | 1216 |
| 10 | $p_2$ | $W_{15}$ | 640 |

完整比较基的 16 个旧下标按

$$
(0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19)
\tag{3}
$$

排列。这是已证真实 $\mathcal R^{(0)}$ 基；没有用“字面不同”替代原函数独立。

$C_2$ 是 R196 的 normal index 2、family $F_0$、state key $(0,2,0,0)$、真权零原根。本次先按同一八矩 $\Gamma$ 组合静态原根，再做真权投影；没有先对分项截断再改变参考减项。其 $-2$ 原 SHA 精确为

~~~text
b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f
~~~

原项数为 1633；仅这一新的 projected static sum 被恢复，未重算其余 196 个静态目标或完整 H0。

[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md) 已给

$$
H=C_2+\frac1{48}R_0+\frac{11}{64}R_2-\frac{13}{96}R_3,\qquad
\pi H=0,\quad\lambda_+(H)=1.
\tag{4}
$$

其本次 $-2$ 原式有 2436 项，SHA 为

~~~text
3be041da7463195066061c4fea47881cedb8c65e69fc65b063748dc7264de325
~~~

原 $H$ 的一次层非零。这一事实仅说明需要补响应；以下新关系确实把它消掉。

## 3. 第一门：对完整权零响应块的成员关系

首次新表含 16 个响应的一次层及 $H$ 的一次层，共 17 列。采用 R230 的原局部次数展开，保持旧 $\mathcal I=\int_r^x$ 的**原正左增量**，再仅对真实三次边界系数使用固定颜色余字母表示。

得到

$$
\boxed{
\mathfrak T(H)
=\mathfrak T\left(
\frac7{48}R_0+\frac1{64}R_1-\frac5{64}R_2+\frac1{32}R_{10}
\right).
}
\tag{5}
$$

响应比较秩和加 $H$ 后的增广秩均为 **4**。式 (5) 的完整原 $-2$ 差有 2666 项：

~~~text
6b0b7dee9845fb8a219ea799495e890773d077513a009a54db675d58294d5768
~~~

程序从这份原差重新提取一次层，重新作三次系数转换，结果准确为零。它没有把“表中标签相等”当成 fresh 原差证明，也没有宣布这 2666 项原函数本身为零。

式 (5) 的响应组合尚未要求 whole pure 零，因此它不是最终需要的比较门。

## 4. 第二门：保 whole pure 零的响应组合

R116 已保存该权的三个 pure 多项式查询：

$$
(c,r)=(0,32),(1,31),(2,30).
\tag{6}
$$

R201 已证这些查询在 $\pi\mathcal R^{(0)}$ 上共同忠实，且该 pure 像恰为三维。本次直接读取旧完整 certificate 中的准确有理数，不重新代入 profile、不重算旧多项式查询、不重做旧消元。

将 (6) 的三行附于同一 16 列一次层表。目标 $H$ 的这三行取**已证**的零，得到新联合比较矩阵秩 **6**，增广后仍为 **6**。准确解为

$$
\boxed{
K_{\mathrm E}
=\frac7{48}R_0+\frac1{64}R_1
-\frac{15}{64}R_2-\frac5{32}R_3
-\frac5{64}R_4+\frac1{32}R_{10}.
}
\tag{7}
$$

三条已存 pure 查询的组合分别准确为 $0,0,0$。由它们在已证 pure 像上的忠实性，

$$
\pi K_{\mathrm E}=0.
\tag{8}
$$

同一新实际还给

$$
\mathfrak T(H-K_{\mathrm E})=0.
\tag{9}
$$

这里 $H-K_{\mathrm E}$ 的完整原 $-2$ 差有 **2694 项**，SHA 为

~~~text
346ea2a14c74e4a6d831b05288533609b08bf7776782c0964dd66ece9eda96b6
~~~

fresh 转换准确归零；零一次层的 SHA 为

~~~text
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
~~~

这次 fresh 验证使用 124 次新三次 primitive 调用、68 次严格下降的固定颜色 IBP，cycle fallback 为 0。转换记录的 SHA 为

~~~text
8cc334e96f795f1b76a68c1f97aba516dc75e342fb3313933272188643a8ff75
~~~

把 (4) 减去 (7) 即得 (1)。式 (8) 与 $\pi H=0$ 给 $\pi H_{\mathrm E}=0$；$\lambda_+$ 杀每个 $R_i$ 给 $\lambda_+(H_{\mathrm E})=1$。这就完整证明 (2)。

两个成员门各自从原差作 fresh 转换。它们的最终三次转换记录相同，是此次实际输出；两份原 $-2$ 差的 SHA 和项数仍分别保存并区分，没有混称同一原目标。

## 5. 有限线性推论及其严格边界

本次新表和旧 pure 查询联合给

$$
\dim\mathfrak T(\mathcal R^{(0)})=4,\qquad
\dim(\mathfrak T,\pi)(\mathcal R^{(0)})=6.
\tag{10}
$$

因为 $\dim\pi\mathcal R^{(0)}=3$，对联合像投影到 pure 像的准确序列给

$$
\dim\mathfrak T(\mathcal R^{(0)}_{\mathrm p0})=6-3=3.
\tag{11}
$$

这里的维数只属于本次明确的 universal 一次端层映射和已证 $\mathcal R^{(0)}$。没有新增完整 $\mathcal U$ 的维数、没有把权零层替代全权 pure 核，也没有从有限表推出某个固定解析圆的 faithful 性。

式 (2) 的因子化结论尤其直接。若存在仅依 $\mathfrak T(V)$ 的线性读出 $\ell$，在 $\mathcal U^{(0)}\cap\ker\pi$ 上满足 $\lambda_+(V)=\ell(\mathfrak T(V))$，代入 $H_{\mathrm E}$ 得 $1=\ell(0)=0$，矛盾。因此本次一次层读出路线到此结束。这个反例只否定经本 $\mathfrak T$ 的读出；它不否定经更完整端点算子或其他权联合观测的读出。

这个结论不取消 $\lambda_+$ 的正性，也不证明完整 period 可解。对真正解析端芽，R230 只把一次项消去后留下

$$
G=P_2+p^2\mathscr A.
\tag{12}
$$

[R226](R226-exact-flat-end-layers-and-remainder-germs-of-the-response-chain.md) 已说明，$p^2$ 层的有限极点仍可能破坏端点解的光滑延拓；R225 的平台、总通量、内部退化及右锚条件也没有由 (12) 自动支付。本文未指定 R225 存在性构造中的正多项式，未求固定圆的真实三次尾值，更未完成全相位 period/ruling 联立。

## 6. 新计算范围与完整实际状态

本次做了 17 个新一次层，完整进度为 17/17；其中实际转换 34 个真实三次系数。原局部映射读取 2574 个 atom、5756 个 monomial，独立尾符号创建数为 0。只把规范化后的**外部** anchor jets 置零，没有删除 word 字母内部的 profile jets。

16 个恢复响应的原 mixed SHA 全匹配 R126。pure 原根恢复数为 0；新 N 收缩数为 0；新 profile 评价数为 0；旧 pure 查询重新评价数为 0；完整 quartic NF、完整 H0 kernel 及旧 full-function 秩均未重复。

本次总新三次 primitive 调用为 415；主表三次 NF 无 cycle fallback。以上是完成状态，不把预算退出写成证明。

| 项目 | 公开实际 |
|---|---:|
| 新一次层列 | 17/17 |
| 新三次系数记录 | 34 |
| 完整权零响应块的一次层秩 | 4 |
| 加三 pure 查询后的联合秩 | 6 |
| exact integer operations | 85870 |
| 最大整数位长 | 50 |
| 研究 elapsed seconds | 11.40945734799999 |
| 研究峰值 RSS | 112.6171875 MiB |
| 新人工条数 | 12，全部通过 |
| 人工 elapsed seconds | 0.009005078999990701 |
| 人工峰值 RSS | 28.40234375 MiB |

新人工覆盖原 $\int_r^x$ 方向、嵌套左积分、外多项式与 derivative 的完整 IBP、真实 coupled cubic shuffle、外 anchor jets、R78 mixed-only 输入恢复以及附加旧 pure 行可以改变成员门。没有重跑旧人工组或真实目标。

## 7. 公开 provenance、源码和复现参数

- Repository：Rogerhu12/math-research-public。
- Run：43699241372，attempt 1。
- Job：132766507930，lane character_zero_endpoint_layer。
- Source commit：ee9e2098c62392ddb709e7db26467bc225642d54。
- 完成状态：complete，phase 为 complete_weight_zero_universal_first_endpoint_layer。
- Metadata receipt：[本次 provenance](../notes/actions-43699241372-1-character_zero_endpoint_layer/receipt.json)。

正文由完整 stdout 读取；从日志重取完整 JSON 行后，逐字节 bytes/SHA 与已发表 receipt 一致。

| 临时输出 | bytes | SHA256 |
|---|---:|---|
| character-zero-endpoint-layer.json | 38943 | 577157ad38ca9744411167bd0fe865838df0360ee2564421b598a82f76fea26b |
| character-zero-endpoint-layer-development.json | 8580 | 5e1f237e6c3ca3fb95149199449a95507682875f123afcbbbd84390637085403 |
| receipt.json | 49168 | ea5c31ce431cff1f1765f04dd00ec14b26e6e624230d516485e7e994ea46a62c |
| 内存完整 certificate | 94085 | bda761d579684cb2e28c0df7644bb244264094543c43e71079275a21f12062f0 |

按根 README 15，recomputable report/certificate 没有保存到仓库、Release 或 artifact。certificate 仅在 runner 内存中形成并取 hash。这里的 SHA 是来源与复现身份，不代替上文原式证明。

两个新源码：

- scripts/literature_endpoint_first_layer.py：11829 B，SHA256 cf14e26c215bd93feb43dc4b56b8ecdcf9f9013084236e772229404eb9401b69。
- scripts/literature_character_zero_endpoint_layer.py：29604 B，SHA256 bb7be8fc3fa6b98f3f69aca96e5145c6df1f3d581ea85d14aa7fb6ccfefe6a94。

完整输入绑定见 [已发表设计](../notes/character-zero-endpoint-first-layer-design-20261115.md)。五份真实旧来源分别是 R109 静态原根、R126 权零响应定义、R196 完整 H0 provenance、R201 pure 身份，以及 R116 已保存 pure 查询；主报告逐一核 source/run/receipt/原 bytes/SHA。

人工入口：

~~~sh
python topics/visible-flex-new-mechanism/scripts/literature_character_zero_endpoint_layer.py \
  --toy-only --output "$OUT/character-zero-endpoint-layer-development.json"
~~~

唯一实际研究入口：

~~~sh
python topics/visible-flex-new-mechanism/scripts/literature_character_zero_endpoint_layer.py \
  --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
  --R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation \
  --head-directory topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero \
  --pure-identity-directory topics/visible-flex-new-mechanism/notes/actions-43683171512-1-character_zero_pure_readout \
  --stored-pure-directory topics/visible-flex-new-mechanism/notes/actions-43646543691-1-full_m8_tail_response_projection \
  --max-seconds 240 --memory-mib 1024 --integer-bits 8192 \
  --max-terms 100000 --max-IBP-calls 300000 --max-cache-entries 250000 \
  --max-summary-bytes 95000 --max-certificate-bytes 8000000 \
  --output "$OUT/character-zero-endpoint-layer.json"
~~~

脚本只允许本公开仓库的 Actions 运行真实研究。原始输出还明确保留 task_complete=false、full_period_or_joint_ruling_paid=false；它完成的是本节的有限新问题，不是本课题总目标。
