# 任意 profile 的 G 纯模态：一条固定原式关系的最小消费设计

日期：2026-11-14。**设计与小人工接口已完成；实际研究结果尚未运行。** 结果编号由 root 预留为 R138。此处不把 $m=8$ 的阳性投影推广为任意 profile 恒等式。

源码：`scripts/literature_general_pure_G_identity.py`，18430 bytes，SHA-256 `a6731a1c0b4940aadc689f97b9d516029518697619986aa7577b79a71ba5bcc7`。旧 G、静态局部导出、36 个第三模板和各冻结消费者均不修改。

## 1. 唯一新问题与完整相位

[R123](../results/R123-static-pure-tail-three-dimensional-graded-quotient-and-G-blindness.md) 已在同右锚 $q=(c-\xi)^8$ 上证明

$$
\Pi_8G_{-4}=\frac1{128}\Pi_8\mathfrak B_{p_2}(W_1)_{-4}.
$$

这只给一条有根据的原式候选。本次只检验

$$
\boxed{\Delta(q)=G_{-4}(q)-\frac1{128}\mathfrak B_{p_2}(W_1)_{-4}(q)=0.}
\tag{1}
$$

这里 $W_1$ 是 R116 的 36 模板表中索引 1，原 v2 retained index 也是 1；二次算子为八矩表索引 2 的 $p_2$。故原列编号恰为 $8\cdot1+2=10$，没有重排或换符号。其真 profile 仿射权为 $0+1=1$。

同一真实三线性算子令 $d_\tau(q)=\tau(q;q,q)$。R71/R80 的完整 pure 响应是

$$
\mathfrak B_A(\tau)_{-4}(q)
=\frac18\bigl(Dd_\tau(q)[A(q,q)]-2A(q,d_\tau(q))\bigr).
\tag{2}
$$

内两槽对称时，(2) 即

$$
\frac18\tau(A(q,q);q,q)
+\frac14\tau(q;q,A(q,q))
-\frac14A(q,\tau(q;q,q)),
$$

与冻结 `blocks.full_response` 的 $-4$ 分量完全一致。新的实际调用仅按 (2) 生成 pure 表达式，**不调用会同时生成 mixed 的 `full_response`**。原 $G_{-4}$ 亦已含完整相位系数，因此不另乘 $1/16$。

所有项使用同一固定右锚

$$
I(F)(\xi)=\int_r^\xi F(\eta)\,d\eta.
$$

输入为普通复 $C^\infty$ profile，在共同右 collar 上为零。变分精确微分实际 jets 和此固定 Volterra 积分；没有把 primitive 当自由独立变量，不改变右锚，也不把左端/period 值置零。只有 pure 分量使用对角第三算子；这不丢掉待检 pure 的外槽贡献，且不对完整 mixed 算子作此替换。

## 2. 已发原式输入及其绑定

来源固定为 run **43645177423**、source **2f1b809c0b0abb7a26303d36940edc203815f872**，目录

`notes/actions-43645177423-1-local_fourth_quotient`。

| 原件 | bytes | SHA-256 |
|---|---:|---|
| `local-fourth-quotient.json` | 3982 | `19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a` |
| `receipt.json` | 31846 | `c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba` |
| `local-fourth-quotient-original-expressions.json.gz` | 657195 | `ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace` |
| 上项解压原文 | 3518194 | `d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1` |
| `local-fourth-quotient-weight-+1.json` | 13499 | `57d8a80b8344f42cd8594e7d117d29098991d1c392d3101264195eeb1a8533c4` |

另使用原 v2 第三模板 receipt：

`notes/actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json`。

其精确 SHA 和所有原源依赖由冻结 `dual.read_receipt` 绑定；36 retained indices 和各第三模板原 hash 全部核对。没有重编原 152 模板，也没有用形式代表代替原模板。

消费入口直接复用 `literature_static_G_rational_dual.load_G_and_bound`。该 helper 源码为 16444 bytes，SHA-256 `0872f0fc8b561a547342d530239e35c6ac9a37a5bddc5c472bf16c0df73ac477`。它依次核主报告、实际终端发布 receipt、run/source、gzip/raw 完整字节、同源 source_hashes、全部 portable roots、36 模板以及原 weight-one 分块身份。

旧主报告的 `completion=output_limit` 原样保留：它是主摘要字节限制，完整原式导出已成功且被真实发布 receipt 绑定。新消费器没有修改状态来通过校验。

原 G 的定义为几何键 $(1,3,0,0,0,0,0,0)$ 的完整静态局部系数，再作真 profile 权 1 投影。其 $-4$ 原根 SHA-256 必须为

`4608912701e99a514cff0dcb93b896200beeb6e3cbead9a70547b78e00d18c7a`。

原 helper 也验证已发 $-2$ 根以保来源完整性，但本轮不创建、求值或归约任何新的 mixed 响应。weight-one 原 8→7 依赖仅读取已发证明，不重跑它。

## 3. 唯一新增研究计算

1. 从已发 DAG 恢复原 $G$ 和 $W_1$，保原 hash。
2. 同时把 $W_1$ 的 $a,b,c$ 三个颜色代为同一 $q$，得到 $d_\tau$；核颜色次数恰 $q^3$。
3. 按 (2) 新建一个 $p_2$ pure 响应，核 $G$、响应和原差全为 $q^4$、真仿射权 1。
4. 先保存完整原 $W_1$、对角、$G_{-4}$、响应和原差五个 roots。即使后续预算结束，已经生成的原差也可直接继续消费。
5. 对**整条原差 (1)** 调用冻结 `ProfileNormalizer` 一次。该 normalizer 包含 sound 同右 collar IBP 与全部深度的 shuffle；所有未消项保留。输出整个 word 表达式，不只输出 hash。

normalizer 的入口源码 SHA-256 为 `0627875fe06950c9e7c360baaf0429451697a460e2cf10aa6b3434c501363bd2`，其 exact/word/formal 依赖继续由既有 `dependency_info` 逐项绑定。没有引入“NF 不同即函数独立”的假设，也没有重跑旧 forcing、旧 288 列、旧 $m=8$ 查询或任意新幂尾。

判定只有两种：

- 整条原差的 sound 代表准确为零：`original_identity_proved`，可得到任意同右 collar profile 的 (1)。随后再用真实仿射协变，把 **G 仿射轨道的 pure 分量** 放入一般 pure 响应像。
- sound 代表非零：`unresolved_nonzero_representative`。只排除了这次归约直接给出关系；不证明候选恒等式为假，不证明 $G_{-4}$ 非成员，也不证明任何实际成本不能消。

即使阳性，也只付一个 G 方向及其仿射轨道的 pure 分量；[R133](../results/R133-complete-m8-pure-cost-range-and-exact-tail-payment.md) 的整个 $m=8$ 结论仍不能据此自动推广为任意 profile 的整个 $\mathcal U_4$。其余完整正规系数、mixed、ruling、高阶收敛及 README 几何完成门均不在本轮结论内。

## 4. 六项小人工检查

本地已实际运行语法检查和 `--toy-only`，没有读取已发研究 DAG 或运行真正目标。

- 人工 $A(f,g)=fg,\ d_\tau=q^3$ 给完整响应 $q^4/8$。
- 人工内槽对称、外槽不同并含真实右 primitive 的三线性式，核 (2) 等于字面的 $(K-L)/16$。
- 核 signed-right IBP 与零右 collar 边界。
- 核 $1/128$ 关系，故意给错系数时保留非零代表。
- 核带积分的三颜色同时对角化，并拒绝 pure 目标中的 $\bar q$ 颜色。
- 核人工完整原 DAG 导出/恢复及内容 hash。

六项全部通过；本地小人工耗时 0.005009319997043349 秒、峰值 RSS 13.875 MiB。开发报告 5498 bytes，SHA-256 `551c45c82f9e1f2e0033bd36d2f7b6bfa9444f682c57527a67f042727575e219`。公开同 lane 可先运行该新小人工再实际，不为任何旧研究添加重复 gate。

## 5. 公开 Actions 入口和数据范围

仅允许 `GITHUB_ACTIONS=true` 且仓库等于 `Rogerhu12/math-research-public` 时运行研究入口；其余环境只允许 `--toy-only`。默认 180 秒、RSS polling 1024 MiB、40 万系数节点、10 万 profile atoms、10 万 terms、25 万 IBP calls；预算退出报告 `resource_limit`，不冒数学否定。

除 scripts 外只须检出两个旧数据目录：

- `topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient`
- `topics/visible-flex-new-mechanism/notes/actions-43633746055-1-full_phase_bridge_exact`

从仓库根目录的完整实际参数为：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_general_pure_G_identity.py \
  --source-report topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient/local-fourth-quotient.json \
  --source-report-sha256 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a \
  --source-run 43645177423 \
  --source-commit 2f1b809c0b0abb7a26303d36940edc203815f872 \
  --publication-receipt topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient/receipt.json \
  --publication-receipt-sha256 c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba \
  --input-export topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient/local-fourth-quotient-original-expressions.json.gz \
  --export-sha256 ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace \
  --third-receipt topics/visible-flex-new-mechanism/notes/actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json \
  --block-receipt topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient/local-fourth-quotient-weight-+1.json \
  --max-seconds 180 --memory-mib 1024 \
  --output general-pure-G-identity.json
```

主报告保全部来源、原差身份与准确结论，限 90000 bytes。完整新 certificate 为 `general-pure-G-identity-certificate.json.gz`，上限 2500000 bytes，包含原根、完整 NF 和语义范围；主报告若超限则完整另存 gzip，限 2000000 bytes，选取的小 main 仍保来源/状态/结论/文件身份。潜在全部输出合计限 4.8 MB；大原式始终只由公开 Actions 终端消费和发布，不经 API 传送或分片。
