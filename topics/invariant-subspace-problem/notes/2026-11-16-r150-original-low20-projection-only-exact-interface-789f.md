# 原 E20 仅投影精确消费者：冻结接口

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

状态：主源仅实际 AST 通过；本接口不宣称独立消费者已运行。父 v2 的三个逆已经完整乘回，但其 constants 阶段实际终止，仍未完成。

## 1. 唯一数学输入及原来源方向

数域和合法 place 固定为

$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),
\qquad (p,\bar d)=(127,100).
$$

新消费者只读取父 v2 的 **已验证十一维逆**，不消费未验证 candidate，不重新执行原物理模型和三个逆。父完整 manifest 为 3418 bytes，SHA256 `c7b010a2c16e2896782eaaad74f977d00e640af6c8142b623474a015b948bf9b`，binding 为 `672c57bb68079e9a49cff09e4a7fdadd7b89dc017927913ee0d35261a08d2522`。

唯一相位为 `original-inverse-11-abb2c7a819cd`：压缩 1473718 bytes，SHA256 `ec9d6e2758ae835f027fd0c3d8da26945814cb3599949057f96ac542b78300e6`；逻辑 2975996 bytes，SHA256 `31bf451e26193eed026feba6bf00a71a9394a78ecce0a7571aea661380b76c05`。其 label 必须是 `same original eleven quadratic sources`，输入矩阵哈希必须是 `028c02fb11bb2acc1717b0c7d221edd91a0e1d6ab2fee34c4fe133d7207e89d5`；两侧 242 个 E 产品、726 个忠实有理坐标和 place 逆门必须全部为真。

原十一条二次来源写作 $G_g=q_g+\ell_g+c_g$，$g=0,\ldots,10$。五个 $u$ 变量的普通二次单项式按 `combinations_with_replacement(range(5),2)` 排序；保留四项为

$$
(u_1u_4,\ u_2u_3,\ u_2u_4,\ u_3u_4).
$$

其余十一项的原矩阵是 $U_{j,g}=[m_j]q_g$。父相位储存的 $U^{-1}$ **行是来源 $g$，列是被消去单项式 $j$**。新源分别重建并逐项核对原 monomial、ELIM、五十 low labels、所选二十列和原五十五来源标签，避免转置或坐标换名。

对于普通单项式 $u_i u_k$，

$$
\alpha_{ik}=U^{-1}e_{ik}^{\rm elim}.
$$

若它是四个保留项之一，则右端为零。$i=k$ 时仍用普通单项式字典，不添加额外因子 2。程序核对全部 $15\times11=165$ 个字面来源索引及四个零列。这些是读取后索引检查，不冒称新支付父原二次正常形的 225 个乘积。

## 2. 直接投影，避免大常数重复构造

原三次来源列标签为 $(g,\ell)$，列号 $5g+\ell$；$R$ 恰取原列 35 至 54，即 $g=7,8,9,10$、$\ell=0,\ldots,4$。对全部五十列 $(i,j,k)$，其中 $i<j$，新源直接计算

$$
(Rz_{ij,k})_{g,\ell}
=\delta_{\ell,j}\alpha_{ik,g}-\delta_{\ell,i}\alpha_{jk,g}.
$$

这就是原交换子最高线性来源的投影。原十六个三次 border 来源 $X$ 支撑在列 $0,\ldots,34$，所以 $RX=0$。原 $C$ 的满秩、$Cz=0$、$R|_{\ker C}$ 单射及规范来源唯一性，引用已闭的 `results/R150-appendix-original-characteristic-zero-low-commutators-factor-through-twenty-cubic-sources.md`。本次明确不新算 $C$、$CZ$ 或 55 坐标乘回。

选定二十列是 $i=0$ 的全部 $(0,j,k)$，$j=1,\ldots,4$、$k=0,\ldots,4$；原 seed IDs 为

~~~text
1..5, 11..15, 21..25, 31..35.
~~~

记 $Z=RZ_{50}$，$A=RZ_{20}$。新源完整核实际 $20\times20$ 矩阵的 place 行列式非零，不预填其值。所有计算都在原 E 常数中，不把有限域解的系数冒作 E 解。

## 3. 精确求解与完整新产品门

按 $(1,d,d^2)$ 把 $A$ 写成忠实 $60\times60$ 有理矩阵 $Q_A$，把五十个右端写成 $60\times50$ 矩阵 $Q_Z$。调用 FLINT 的有理 Dixon 求解，得到原 E 的 $20\times50$ 坐标 $\Lambda$。同一 place 的坐标由同一单位矩阵 $\bar A^{-1}\bar Z$ 决定，只用于维护原合法局部运算，不替代精确求解。

完整候选先以独立相位封存，标记 `candidateOnly=true` 和 `exactProductsVerified=false`。最终成功还必须同时满足：

1. $Q_A\operatorname{coord}(\Lambda)=Q_Z$ 的全部 **3000 个有理坐标**，等价于全部 **1000 个原 E 产品**。
2. $\bar A\bar\Lambda=\bar Z$ 的全部 1000 个 place 产品。
3. 所选二十列的全部 **400 个 E 单位坐标**。

两边原五十五维来源均在 $\ker C$ 中；上述精确 $R$ 坐标相同，再用已付单射得到原五十五维恒等。规范来源校正 $a(z)=-U^{-1}\operatorname{elim}(\sum z_g\ell_g)$ 是 E 线性的，故原参数多项式列及其原来源也同时相同。这一步是明确引用已付定理的推论，不声称另外展开并乘回新的参数大数组。

官方 API 依据为 [python-flint 的 fmpq_mat.solve](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html)，其中 `algorithm="dixon"` 是真实有理求解；同页说明矩阵乘法及精确比较。最终完整乘回是本消费者的算术门。

## 4. 独立版本、流式相位和恢复

本源 format 是 `r150-original-low20-projection-only-exact-v1`，输出目录独立。binding 包含主源身份、父源、父 manifest、唯一 verified UI 相位、UI 输入哈希和全部原字典。父 `original-exact-constants` 相位不存在是显式硬门，防止把父失败重标为成功。

新 manifest 只允许三个相位：

| 相位 | 范围 |
| --- | --- |
| `all50-original-low-source-projections` | 全部 $20\times50$ 原投影、原字典、实际二十列单位门 |
| `candidate-exact-original-low20-coordinates` | 完整精确坐标候选；尚无产品结论 |
| `complete-exact-original-low20-products` | 全部最终产品门及前两个相位的完整描述符 |

相位用 JSON `iterencode` 流式写入 `GzipFile(filename="",mtime=0)`，同时累计逻辑 SHA。完整写入、关闭 gzip、`fsync` 和原子改名以后才登记 manifest。最终证明相位引用同一个候选文件，不重复序列化一千个精确 E 系数。中断留下的 `.tmp` 文件不构成完整相位。

恢复时核同一 binding、物理与逻辑全部 SHA。完整候选可以恢复最终乘回；候选自身不能称成功。`--through candidate` 的 `completed-unverified-candidate` 仅表示文件完整，不是数学正证。75 只在有新的完整相位时允许接续；没有全相位的 137 不作空重试。

## 5. 冻结文件

| 文件 | Git blob | bytes | SHA256 |
| --- | --- | ---: | --- |
| `2026-11-16-r150-original-low20-projection-only-exact-789f.py` | `d20db6c713d362d56e8e59ab0c8bcdf846764728` | 21178 | `a77cf71a3e3c4dcbd4b68f3f4d99f98a64bd4f64394f46507c8c42cc5aecf48f` |
| `2026-11-16-r150-original-low20-projection-only-exact-inputs-789f.json` | `03df83d7092e05864843fd75974677aa87749612` | 5266 | `31bfee9a1b7a32d52468f19fdbaa5ed1e5f6dbd11f95134f5566b77fc7fe0a4c` |
| 精确 helper：原 v2 常数源 | `541c14b36925e3cc94018edd8a17a6a765041f5d` | 33539 | `d9d98bc379e322e9c212b7ad7721399ec8b1bab9970a2755700338f7053d47da` |
| 原 observer | `f8aea7924d8becc10e50303a1c9b36f34d718014` | 5855 | `c5d5f777246dbb99d516855eb007845c9b25673cfe736e74cf56f559111a5618` |

父 v2 终止身份为 `notes/r150-original-parameter-module-execution-789f/local-20261116-original-low20-v2-constants180-terminated137.json`，blob `28f8fd36e7d970efa921a58d72e89e3cce83a4fd`，9215 bytes，SHA256 `5f3325e89d9578f344802ad369a297f318fc5b36b2821a8cadfb25218aa3c700`。它明确三个逆完成、完整 constants 未完成和终止原因未证。

## 6. 建议实际 CLI 与资源

固定 Python **3.12.14**、python-flint **0.9.0**，不需 Singular。原 observer 保持逐字相同。第一步建议 `projected` 60 秒 / 512 MiB / outer 120，第二步 `final` 300 秒 / 1024 MiB / outer 360；实际执行由根完整审读后安排。

在共同临时根目录执行第一步：

~~~bash
venv/bin/python 2026-11-16-r150-exact-low20-observed-execution-789f.py \
  --outer-seconds 120 --heartbeat-seconds 10 \
  --stdout original-low20-projection60.log \
  --heartbeats original-low20-projection60-heartbeats.jsonl \
  --identity original-low20-projection60-observed.json -- \
  venv/bin/python 2026-11-16-r150-original-low20-projection-only-exact-789f.py \
  --exact-helper 2026-11-16-r150-original-low-commutator-twenty-exact-constants-v2-789f.py \
  --parent-out original-low-commutator-twenty-exact-constants-v2 \
  --out original-low20-projection-only-exact \
  --through projected --seconds 60 --memory-mib 512
~~~

第二步使用同一数学输出目录，改 `--through final --seconds 300 --memory-mib 1024`，observer 改 outer 360，三个观测文件分别改成 `original-low20-projection-final300.log`、`original-low20-projection-final300-heartbeats.jsonl`、`original-low20-projection-final300-observed.json`。observer 拒绝覆盖已存在的观测文件，后续每次执行仍用新的观测文件名。

## 7. 成功后的范围

若最终门实际完成，则得到原 E 的具体精确低交换子系数及同原来源恒等。它给五十低列由所选二十列生成的实际数组，与原定理合并给 **76 个原 E 种子的同普通 B 模**和至多 **670 列的完整两轮呈示**。

它不删除四十个 high comm，不支付条件性的 quartic 95 门，不声称 E 版本已有有限域的 200/210 压缩，也不证明 Bell=1 原理想为单位理想。全部数组、候选、raw 和 observer 心跳仅留临时目录；Git 只保存本源、参数、证明及真实执行身份与 SHA。
