# 完整权零正字符的单一 pure 读出门：19 个已知基根

日期：2026-11-15。状态：新消费器与新人工开发完成；真实研究目标只由本公开仓库 GitHub Actions 执行，本文不预报其成员结论。

源码建议路径：scripts/literature_character_zero_pure_readout.py。当前冻结源 29283 字节，SHA256：

$$
\texttt{8d99414bda0a9bf61925f74e5378bfe80532fc8d9b9d35d6cc73625f8f15f7d1}.
$$

对应源码已放在 root 指定恢复环境的独立 pending_tail 目录，没有修改公共 checkout 中已跟踪的冻结源。

## 1. 只问一个会改变主线判断的问题

[R196](../results/R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) 已完整证明

$$
U_0=R_0\oplus\operatorname{span}(C_2,C_4,C_6),
\qquad \dim R_0=16,
$$

并给真实正字符

$$
\lambda_+|_{R_0}=0,\quad
\lambda_+(C_2)=1,\quad
\lambda_+(C_4)=\lambda_+(C_6)=0.
\tag{1}
$$

R196 还证明闭 frame、真实 $M=0$ 正时长 canonical 成本满足

$$
\lambda_+(V_B)=\int k^2\,ds
=L_B+\int(h_s/h)^2\,ds>0.
$$

但这不意味着 $\lambda_+$ 可以从任意选定第一圆或 pure 输出读出。R198 的最右单 g 阶段提供了一个特别需要区分的纯目标：在该右区间 f 恒零，全部二阶 gauge 对 period 的作用消失，剩余原 period 是同几何单 profile 的纯 isometric quartic。要知道 R196 的正字符是否有可能只从这种 pure 信息取得，第一道准确门就是

$$
\boxed{
C_{2,-4}\stackrel{?}{\in}
\operatorname{span}_{\mathbb Q}
\bigl(R_{0,1,-4},\ldots,R_{0,16,-4},C_{4,-4},C_{6,-4}\bigr).
}
\tag{2}
$$

所有根都是真实 universal profile 原函数，使用同一个右锚；没有选 m=8 或其他幂尾，也没有使用某个固定 profile 的有限采样代替 (2)。

### 1.1 两种完整结论分别意味着什么

若 (2) 为真，给出准确有理系数并定义完整算子

$$
H=C_2-\sum_{i=1}^{16}a_iR_{0,i}-bC_4-cC_6.
$$

由 R196，$H\in U_0$ 且 $\lambda_+(H)=1$，而新的原式恒等给 $H_{-4}=0$。因此 $\lambda_+$ **不能**经 universal pure 投影在 $U_0$ 上因子化。任何只读取 pure 输出的线性泛函都无法等于它。这里 H 是真实成本线性 span 中的元素，不声称它已由一个实际有限正时长字实现，也不声称实际 pure 零成本已构造。

若 (2) 为假，完整的规范 word 单射给一个准确有理对偶行 $\ell$，使

$$
\ell(R_{0,i,-4})=\ell(C_{4,-4})=\ell(C_{6,-4})=0,\qquad
\ell(C_{2,-4})=1.
$$

它在整个 $U_0$ 的 pure 像上恰为 $\lambda_+$，而非只在一个目标上非零。对偶只需至多 19 个规范 word 坐标，全部支持行和有理系数在小摘要中明确输出。

这条对偶首先是 universal 规范 word 系数的线性读出，不是已经实现的固定 profile 点值。它没有自动杀掉其他真权在同一固定 profile 上的评价像。要用于 R198 的一个固定 step，仍须另付跨权与固定输入因子化；本消费器不声称这两个结论。

## 2. 三项输入与逐字节来源

### 2.1 已发布完整静态原式与 W

读取旧目录：

```text
topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient
```

保留原主报告、receipt、完整 static/W 原导出的 packed/raw SHA 与生产者 source 绑定，完全复用冻结 head.bind_input("static",...)。

原生产者是 literature_local_fourth_quotient.py，38857 字节，SHA256

$$
\texttt{9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0}.
$$

完整旧导出 local-fourth-quotient-original-expressions.json.gz：

- packed 657195 字节，SHA256 ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace；
- raw 3518194 字节，SHA256 d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。

它是已有旧文件，后继可以读取；本任务不重做其 producer，也不生成新的同类 payload。

### 2.2 已证明的完整 R0 基标签、原 hash 和真秩

读取旧目录：

```text
topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation
```

完全复用冻结 zero.read_R0_definition 对旧主报告、receipt、完整报告 gzip 的检查。这包括 R126 原 20 列覆盖、16 个保留标签、四条已付原式依赖的 hash，以及旧 16 阶原评价子式。只消费这些已成证据，不重新评价它们。

保留原下标：

$$
0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19.
$$

旧 R126 当时没有保存完整响应 DAG；R196 依新规则也只保 metadata，没有存 318 行共同矩阵。因此本新派生目标需要最小恢复上述 **16 个 pure 根**，每根须准确匹配旧报告的模式 −4 原 SHA。

恢复只调用冻结 R78 的 pure 分量

$$
\frac18T(A(q,q);q,q)
+\frac14T(q;q,A(q,q))
-\frac14A(q,T(q;q,q)).
\tag{3}
$$

不调用完整两模式 full_response；不恢复或评价模式 −2。需要的旧 W 只有索引

$$
1,6,7,11,12,14,15,16,17,27,32,34,35,
$$

共 13 根，均从 2.1 旧导出读取并核原 SHA。

### 2.3 R196 的真实头部与 normal 根身份

读取新 metadata-only 目录：

```text
topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero
```

只读 receipt.json。该回执为 45501 字节，SHA256

$$
\texttt{7919e2406650d394b1128d7014585dbdb830a87adb7979e74f6b2e752e484abf}.
$$

其 run/source 为 43681388902 / 7872857e7750e1b5091560b6362e52dd952bc6fa。绑定的 H0 源是 42361 字节 / 337966b4fb9a417ed62d650cac87ffc4c41bedc9938e11c1520fe1136b53dee4。

回执还绑定已由 root 与作者全文读取的实际 stdout 摘要：25121 字节，SHA256 838266c7b4b86b137482127e7e874d8d3eb014aa5745b9be6fceb2d9d3dc7fa4。该摘要没有作为仓库 payload 保存，本新 consumer 不要求一个实际不存在的主 JSON 文件。

回执身份本身不被当作数学证明；基与 $\lambda_+$ 值来自已经发表的 R196 完整证明。新源码显式保留这个区别。

## 3. 只提取 C2、C4、C6，不重装全部十四族

三个根均来自原静态规范化

$$
F_0(S)=L_0(S)-\sum_{i=1}^8a_i(m_0(S))L_0(S_i^*).
\tag{4}
$$

其中参考态、坐标逆矩阵与 R130/R163/R196 完全相同。三个所需状态键依次为

$$
(0,2,0,0),\quad (0,4,0,0),\quad(1,1,1,0),
$$

顺序为 h、k、$\omega$、$\log h$ 的幂。

为了不重做 R196 的 197 个逐根 weight0 投影，本 consumer 先在几何系数层准确线性合并：若目标键为 j，旧 L0 的键为 a，则系数为

$$
\mathbf1_{a=j}
-\sum_{i=1}^8[a_i(m_0)]_j\,S_i^{*a}.
\tag{5}
$$

先按 (5) 合成三个原 profile 表达式，再各作一次 $\Pi_0$。原式线性与同一精确规范保证这与 R196 的“先逐根投影、再 (4)”相同；原 SHA 还须逐根匹配。含 $\log h$ 的键在 h=1 参考态上的值按原规则为零，不能忘记它们。

| 根 | pure 模式原 SHA256 |
|---|---|
| C2 | ad4cd7fcdcbac89c55309c6906b6cb3a6d869ad37834e4a32fe8cad1b6e33393 |
| C4 | 5d70abb9d4000f457beb9d5d6d0adbf08f19becb953818f362c62b5c04dbb3e9 |
| C6 | c074cfef87ff0f7b9435092bfce4615b7de12d2cbe4a0eabcb1a457d17b01044 |

摘要保存每根的完整旧原根线性组合、投影前后 hash 和参考逆矩阵身份。只 subset 解码需要的旧模式 −4 原根及 W，不解码旧混合原根。

本任务不读取 N0/N2 缓存或完整 3974 因子；不重做 R196 的 11 个新增 E×N 收缩，不重装 Q2/A/H/Q4，不重求完整 38 列两模式核或两维头部。

## 4. 新 19 列精确判门及单原差

新列顺序严格固定为

$$
R_{0,1,-4},\ldots,R_{0,16,-4},\
C_{4,-4},C_{6,-4},C_{2,-4}.
\tag{6}
$$

每列先验证仅有 q 颜色且四次齐次，再经同一个冻结 R178 PriorityWords 转换。全部余 letter 的规范语法逐项检查，R179 的单射因此适用。此处所有新列都使用同一个新映射 $\Phi$；没有混入旧不完备或不同语法的 word 代表。

旧 pure 表示未保存，所以这 19 根的 pure 映射是本单一新投影问题所需的派生计算；不把它描述成已经有一份可直接读取的旧矩阵。相对旧 H0 全函数目标，本次不含 mixed 根、其余 normal 根、完整 D 分母或任何重新解头部的步骤。

先只把前 18 个比较向量加入精确无分母列消元。原 pure 比较列可以有真实依赖；不假定它们仍有维数 18 或 16。最后只对目标 C2 作一次成员判断。

### 4.1 成员证书

若目标消元为零，准确输出 (2) 的有理组合。先用全部已保存新原列的转换身份核对 word 和为零，再独立组成原 profile 差

$$
\Delta=C_{2,-4}-\sum a_iR_{0,i,-4}-bC_{4,-4}-cC_{6,-4},
$$

对这唯一新原差重新作 fresh R178 规范化，并要求准确为零。新 fresh 调用计入同一个总 primitive-call 预算；不通过增加隐含旧预算再算一遍。

输出包含原差 SHA/项数、规范零 SHA、完整系数，以及 $\lambda_+(H)=1$ 的已证头部解释。因为所有列确用同一规范映射，fresh 不零会被记录为本次实现检查失败，不解释为数学非成员。

### 4.2 非成员证书

若目标余向量非零，在比较基与目标的真实原向量上选取 pivot 行，准确解转置有理方阵。得到的对偶支持大小不超过新秩，故不超过 19。

对偶须重新在全部原 19 列逐项相乘，准确得到

$$
(0,\ldots,0,1).
$$

摘要明确输出每个支持行的 local monomial、ordered word、精确有理权及全部 19 个核对值。由 R179，这是真实函数非成员及显式 universal word 读出，不再需要原 profile 点值或有限域非零子式。

## 5. 输出、失败语义与资源

唯一实际 lane 建议为 character_zero_pure_readout。默认预算：

| 项目 | 上限 |
|---|---:|
| 实际 wall time | 120 秒 |
| RSS | 512 MiB |
| 精确整数位数 | 8192 |
| 单式/字典项 | 80000 |
| 新 primitive 调用总数 | 150000 |
| 缓存条目 | 150000 |
| stdout 完整摘要 | 95000 字节 |
| 只在内存构造的证明对象 | 2000000 字节 |

有限预算退出不产生成员或非成员结论。完整原式 gate 只有实际 completion=complete 且单原差或全部对偶值核对通过才完成。摘要超限返回 summary_output_limit，并只保完整摘要尺寸/SHA；不会把被截断的对象冒充可读完整证据。

内存证明只保原根身份、全部新转换身份和单一准确关系/对偶。它不写仓库、Release 或 artifact。允许 --output 写 runner 临时摘要供新版 metadata-only publisher 取 hash；publisher 不保存 payload。

未来复用本结论时，应消费发表的准确小关系或对偶及其 source/run/SHA。需要较大机器数据时依根 README 的当时规则重现，不能偷偷分片或编码归档。

## 6. 新人工开发的实际状态

当前冻结源 8d99414b… 已在恢复终端通过语法检查及以下七项**新增小人工**：

1. 比较列含依赖、目标系数为非整数有理数时，成员关系准确；
2. 非成员时，对偶对全部原列逐项给出零/一；
3. pivot 插入次序不单调时仍取得正确对偶；
4. 零目标给成员而非伪 rank1；
5. 人工静态 $\Gamma$ 组合保留参考常项和 $\log(1)=0$；
6. 人工乘法二/三算子上的 pure R78 系数正确；
7. 一个新人工原差的独立 fresh pure 规范化为零。

人工未读取任何真实原式输入，不运行目标 (2)，不重跑旧 10 项、旧 31/40/70 依赖或旧实际 profile。

完整本地人工回执为 7839 字节，SHA256

$$
\texttt{f9d33da1b16463071c7536ac0e1eb60e1ff9164a017cbdc13f69ece78f44ad08}.
$$

人工 elapsed 为 0.004805596 秒，RSS 20.25 MiB。公共实际派发应先执行同一新 --toy-only，然后本次新 actual；人工回执自身也遵守 metadata-only 规则，不把它作为新机器证书入仓。

## 7. 完整公共 CLI 与 sparse 目录

开发：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_character_zero_pure_readout.py \
  --toy-only \
  --output @OUT@/character-zero-pure-readout-development.json
```

唯一实际：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_character_zero_pure_readout.py \
  --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
  --R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation \
  --head-directory topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero \
  --max-seconds 120 \
  --memory-mib 512 \
  --integer-bits 8192 \
  --max-terms 80000 \
  --max-IBP-calls 150000 \
  --max-cache-entries 150000 \
  --max-summary-bytes 95000 \
  --max-certificate-bytes 2000000 \
  --output @OUT@/character-zero-pure-readout.json
```

只需上面三个 notes 目录和已有 scripts；H0 目录只消费 receipt，没有主摘要 payload 依赖。新源绑定完整已发表 H0 驱动与全部其语义依赖，冻结 H0 源本身不修改。真实研究 gate 要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。

本消费器的完整数学目标就是 (2)。得到一条原关系或一个准确对偶后即停止本次研究，不顺带扫描其他权、重跑幂尾、加入 mixed 或评价新的几何/profile。

