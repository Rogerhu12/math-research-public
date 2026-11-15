# 只消费 R186 已存纯分量的权 −2 完整纯像门

日期：2026-11-15。**新计算设计；尚无本目标实际结论。**

源码：`scripts/literature_pure_minus2_archived_projection.py`。它只导入 Python 标准库。首轮实际目标是 9 个已证响应纯基加 12 个新增真实商基；不重建原 DAG、不调用 normalizer、forcing 或 profile/geometry evaluator。

## 1. 为什么恰好只需这 21 列

记 $\pi$ 为完整 canonical 第四成本的 $-4$ 纯分量。R151 已证明

$$
\dim\pi R_{-2}=9,
$$

其在原 R40 内的基下标为

$$
0,1,2,3,8,9,10,12,19.                                      \tag{1}
$$

对应全 R116 编号是 $0,48,88,112,41,73,81,193,170$。R151 的 31 条完整 pure 原式身份提供上界，R131/R151 中已付的原评价 minor 提供独立下界。本次不重新验证这些原差或独立性；只把九列准备成解新线性问题的精确消元接口。

R186 §2.1 的真正 $U_{-2}$ 基为原 77 列中的

$$
0,\ldots,39;\quad 40,41,42,43,44,45,46,49,51,52,54,58.       \tag{2}
$$

后十二列的原 normal 下标为

$$
0,1,2,4,5,7,8,23,28,30,38,46.                              \tag{3}
$$

R174 的 70 条原式字面关系和 R186 的 25 条共同原函数关系已付完整覆盖，故

$$
\pi U_{-2}=\pi R_{-2}
+\operatorname{span}\{\pi C_j:j\text{ 为 (2) 的后十二列}\}.  \tag{4}
$$

本次只解 (4) 的十二个新方向。原 R40 中另外 31 列、原 77 中另外 25 列均不再次消元。

## 2. 两组准确输入

### R186

目录 `notes/actions-43676765171-1-character_head_word_relations`。

- run：`43676765171`。
- source：`ca4e52869123fa97df4560232a03f9529cf05332`。
- main：`character-head-word-relations.json`，12724 B，SHA256 `68bf26fc88ffea61f5be2e17e11324540f58ff0a4c71f59b87428caef38c1341`。
- receipt：43019 B，SHA256 `1e4faea0f993c36021fc769c9e66c313f6e131f8d2d2add418143d14ed724dfa`。
- certificate：`character-head-word-relations-certificate.json.gz`，773910 B，SHA256 `fec2d558a1241a4e0beaedcd80fd03395f7c87bce028cb65357cb804bf434685`。
- raw：3936105 B，SHA256 `88baa9dd0ff0ed3d992d67846cbcb2553b68b455ed99b24cfca926ca382d7647`。
- 原 producer：79108 B，SHA256 `1ec5fab96ec173c3e1583b40a124c5c98b3249cec9a87be39db3b3066e31b300`。

第 $j$ 列的纯词行正是

```text
completed_original_to_word_conversions[j].projections["-4"]
```

其 `conversions["-4"]` 绑定原完整纯根、投影根、词行 SHA、同一右锚和已验证的 R178 余 letter 语法。原 147 下标和原元数据同时保留。

### R151

目录 `notes/actions-43657785023-1-general_pure_J_membership`。

- run：`43657785023`。
- source：`c606688a842bd811106ff2844e1161a4f34c159e`。
- main：`general-pure-J-membership.json`，45019 B，SHA256 `98442251ed15b708a70e3fcbbdb2ae6cf76c8c1873aa21345354a5a320a9cfac`。
- receipt：35841 B，SHA256 `31d6380160437b0098d33d35e4b722c79cd780d351f614a4e48901100a9d0fa4`。
- certificate：`general-pure-J-membership-certificate.json.gz`，84283 B，SHA256 `af46437f676716a20051bf3bad5a96235398dcf8a45c179d1395bc1f9d84712e`。
- raw：456216 B，SHA256 `9859368ec20e0923cc168199a7ecb82eff0beac5fa191f1b6388e67cfd1aa550`。
- 原 producer：37092 B，SHA256 `1a84590f8b6f0c35a1df5f251a8ffa0e9f4da65ea2cc3bd777e752482ef05bcc`。

此份输入只核已存九基、31 条原身份完成状态、原根跨来源身份，以及 R186 所引用的同一证书；不重算它的 40 词表、31 原差或 J 目标。

输入器逐项核主文件、receipt、packed/raw SHA/bytes、schema、repository/run/source、原 driver、发布输出记录以及证书的完整来源表一致。两个输入目录必须加入新 job 的 sparse checkout；不能只检出新脚本后在运行时尝试恢复研究。

## 3. 原语法与真实结论

共同右锚是

$$
I(F)(\xi)=\int_r^\xi F,
$$

所有颜色在同一右 collar 为零。所选纯表达式只有 $q$ 颜色、总 profile 次数为四、真实仿射权为 $-2$。词行是局部多项式单项式乘有序余 letter 词；输入器不 shuffle 或重做分部积分。

全部 77 列的两个已存分量仅核 hash、原根绑定与完成标志；数学消元只读取 (1)、(2) 的 21 个纯分量。所选 21 份词行另逐项检查余 letter 语法、严格排序、约分有理数、颜色、次数和仿射权。

R178 给每份表与原函数相等，R179 给余词字典在真实 universal smooth profile 函数空间上的单射。因此本次非零余项具有**真实函数非成员**含义。这里与旧不完备 normalizer 的“余项非零仅未决”不同：完整性由已经发表的 R179 提供，程序没有从自己的消元结果猜测完整性。

旧 producer 中 `complete_true_functional_kernel_claimed=false` 等保守字段不构成数学反例；R186 用其完整转换加后来已付的 R179/R159 证明真实核。本消费者依赖这条完整论文链，不把旧 source 的 scope 标签擅改成新的 actual 结果。

## 4. 唯一新有理计算

先把已证九个响应纯基准备为一个精确三角解算器。这是读取新问题的固定比较空间，不重新提出“原 R40 的 rank 是否为 9”这一旧目标。

对每个新列 $X_j$：

1. 仅减去九个固定响应基，得准确余项 $r_j$。
2. 若 $r_j=0$，记录 $\pi X_j$ 的九列准确有理系数，并从**未修改的已存词表**重新相加核零。
3. 若 $r_j\ne0$，R179 给 $\pi X_j\notin\pi R_{-2}$；再只把 $r_j$ 对此前独立新余项归约。
4. 新独立余项保主词、非零主系数、对原 21 列的准确组合；新依赖关系保完整原 21 列系数。所有新关系/新残差表示都由未修改的词表独立相加检查。

令独立新余项数为 $d$。完整十二列处理后严格得到

$$
\begin{aligned}
\dim\pi U_{-2}&=9+d,\\
\dim(\pi U_{-2}/\pi R_{-2})&=d,\\
\dim\ker(\pi|U_{-2})&=43-d,\\
\dim\ker(\pi|R_{-2})&=31,\\
\dim\ker[U_{-2}/R_{-2}\longrightarrow\pi U_{-2}/\pi R_{-2}]&=12-d.
\end{aligned}                                               \tag{5}
$$

若 $d=0$，这是完整纯像等号 $\pi U_{-2}=\pi R_{-2}$。若 $d>0$，这是明确的新 universal pure 商方向，不是一个固定 circle 的不可解证书。程序也不从线性像等号宣称已有真实有限几何使整个纯 period 为零；真实控制词的基准成本、其他权和所有 ruling 仍须另付。

## 5. 输出、预算与失败范围

默认 120 秒、512 MiB RSS 软轮询、每个有理数 16384 bits、200 万次稀疏有理更新。研究规模只有 21 个存量列。正常主报告上限 95000 B；完整新证明内容在内存中形成一个至多 5 MB 的确定 JSON，只输出 bytes/SHA，不保存该证书。

研究 job stdout 输出：

- `MATHEMATICAL_RESULT`：完整 (5) 的实际数值和原基编号。
- 每个 `MATHEMATICAL_COLUMN`：十二个目标的成员状态、新基状态与准确有理关系。
- `CERTIFICATE_METADATA`：内存完整证书 bytes/SHA。
- `REPORT_SHA256`：job 临时主报告的 bytes/SHA。

遵根 README §15：主报告、人工报告和内存证书均不提交、不上传 Release；只发布脚本、参数、run、SHA 和完整数学结论。若小报告异常超限，只从其中省去详细列数据并保数学摘要与完整 report SHA，不伪造新数学失败。预算或接口失败另报已处理十二列的实际前缀，不授完整纯像结论；不会重算旧研究去补接口。

实际入口强制 `GITHUB_ACTIONS=true`、本公开 repository、非空 run/source。`--toy` 完全不读两份研究输入。

## 6. 人工检查与公开 CLI

新增人工包括：非整数准确成员、独立新方向、依赖于先前新方向的旧像非成员、所有新恒等式再相加、输入不变、纯词语法/次数/权、非约分与错误颜色拒绝、错误新关系拒绝、错误已证基输入拒绝、字节/SHA绑定、人工 publication/run绑定。只用小型自造数据。

公开先运行：

```bash
python scripts/literature_pure_minus2_archived_projection.py --toy --output "$RUNNER_TEMP/pure-minus2-archived-development.json"
```

唯一实际：

```bash
python scripts/literature_pure_minus2_archived_projection.py \
  --word-dir notes/actions-43676765171-1-character_head_word_relations \
  --pure-dir notes/actions-43657785023-1-general_pure_J_membership \
  --seconds 120 --memory-mib 512 --rational-bits 16384 \
  --output "$RUNNER_TEMP/pure-minus2-archived-projection.json"
```

当前仅新增人工允许在本地运行；21 列研究尚未本地执行。
