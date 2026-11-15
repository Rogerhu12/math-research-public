# R201：权零完整 pure 像等于响应像，且正字符不能经 pure 因子化

日期：2026-11-15。**新的精确原式目标已在本公开仓库 GitHub Actions 完成。** 消费器、推导与整理：tail_cost；root 独立全文读取实际输出与原关系。本文对所述结论负责。没有重算完整 H0、混合模式、旧 profile 评价或幂尾。

## 1. 决定性原恒等及结论

沿用 [R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) 的完整真实权零空间 $U_0$、响应 $R_0$、normal 原根 $C_2,C_4,C_6$ 及正字符 $\lambda_+$。设 $\pi$ 表示 universal pure 模式，即完整算子的模式 −4；这是对任意光滑输入的算子投影，不是 $m=8$ 幂尾或某次 profile 采样。

把 R126 的旧块列记为 $R^{(j)}$。本次完整原式结果为

$$
\boxed{
\pi C_2
=-\frac1{48}\pi R^{(0)}
-\frac{11}{64}\pi R^{(2)}
+\frac{13}{96}\pi R^{(3)}.
}
\tag{1}
$$

两边是同一真实右锚、任意 profile 下的准确函数身份。540 项原差经独立 fresh 规范化严格为零。

进一步，

$$
\boxed{
\pi(U_0)=\pi(R_0),\qquad
\dim\pi(U_0)=\dim\pi(R_0)=3.
}
\tag{2}
$$

定义**完整两模式算子**

$$
\boxed{
H=C_2+\frac1{48}R^{(0)}
+\frac{11}{64}R^{(2)}
-\frac{13}{96}R^{(3)}.
}
\tag{3}
$$

则

$$
\boxed{
H\in U_0,\qquad
\pi H=0,\qquad
\lambda_+(H)=1.
}
\tag{4}
$$

所以 $\lambda_+$ 不能通过 universal pure 投影在 $U_0$ 上因子化，当然也不能从任意一组仅 pure 的 profile 查询恢复。

这不撤销 R196 的完整正字符，也没有构造一个实际 pure 零成本字。H 属于真实成本的**线性 span**；式 (3) 的有符号线性组合不能未经证明地当作一个实际有限路径。

## 2. 实际来源与输入范围

公开实际：

- run：43683171512；
- source：8c1ab4bab5763273e1004734a9582e3e9d697f9a；
- job：132718011170；
- lane：character_zero_pure_readout；
- [公开 Actions job](https://github.com/Rogerhu12/math-research-public/actions/runs/43683171512/job/132718011170)；
- [metadata-only 发布回执](../notes/actions-43683171512-1-character_zero_pure_readout/receipt.json)；
- [唯一新源码](../scripts/literature_character_zero_pure_readout.py)；
- [完整来源、算法及 CLI 设计](../notes/character-zero-pure-readout-design-20261115.md)。

源码为 29283 字节，SHA256：

$$
\texttt{8d99414bda0a9bf61925f74e5378bfe80532fc8d9b9d35d6cc73625f8f15f7d1}.
$$

| 对象 | 字节 | SHA256 |
|---|---:|---|
| 公开 metadata-only receipt | 45729 | 0d926d181f6e607af71a59f62cb83cb187e7a9b705508308ffb56adf16472d4f |
| 实际 stdout / runner 临时完整摘要 | 24340 | 1fd475ffeaf62258132ac7d938b4f563f7401f2db0c38e78403f4c9de39b239b |
| 七项新人工 stdout / runner 临时摘要 | 7915 | 15149df0d2811bf72614d40cd96d43ec95a8f4cc928097e2a24555a215bfa154 |
| 仅在内存中的新证明对象 | 7220 | 003bbda2b1ac32d1f99bb22cb7a142db6e4c40f194e52dc9b479c49af0cf0003 |

完整实际摘要已从公开 stdout 读取，尺寸和 SHA 与发布回执准确相符。新人工七项全通过，实际研究 completion=complete。研究耗时 1.273566508 秒，RSS 峰值 88.75390625 MiB；740 次精确整数操作，最大位数 17。

依根 README 的新存储规则，可重算 payload、数据与机器证书不放仓库、Release 或 artifact。表中后三项不被冒称为已保存的仓库文件；复现依据冻结脚本、完整参数、source/run 与 SHA。

本次只消费：

1. R109 已发布的完整静态 L0/W 原导出；
2. R126 已发布的完整 R0 标签、旧原 hash、四条依赖与旧秩证据；
3. R196 已发表的完整头部结论及其 metadata-only receipt。

R126 没有保存 portable 响应 DAG，R196 新运行也只保 metadata。因此只恢复 16 个必要的旧 pure 原根，并逐根核对旧 SHA；没有恢复模式 −2。C2/C4/C6 先由旧静态根和同一八参考 $\Gamma$ 准确线性合并，再只作三个真权零投影。不读取 N0/N2 缓存，不重做 R196 的 11 个新收缩或 38 列完整两模式函数核。

## 3. 式 (1) 中三个旧响应的准确标签

R126 的 R0 全块共有 20 个原标签，已证明真基保留其中 16 个。式 (1) 使用的是**旧原块列号** 0、2、3，不是任意重新排列后的三个响应。

| 旧原块列号 | E8 二阶方向 | W36 索引 | v2 原第三索引 | pure 原 SHA256 |
|---:|---|---:|---:|---|
| 0 | $p_0$ | 7 | 7 | 9e55993789c2c9a5a99a3e4f6e046600e9bc6d553acc85d15b820676f8ba70ec |
| 2 | $p_1$ | 1 | 1 | 7117c05d717abe9925e8dfed1576596d1e1bb3abf2a1e310d14655d2d4842fa4 |
| 3 | $p_1$ | 12 | 12 | 768f415ad01963726d674be8d6d83b9f6d2ab7ce3ba13d73e14c01eb06f977a6 |

所有标签均沿用已冻结 W 的方向和符号，不另改交换子约定。若用完整响应记号，

$$
R^{(0)}=\mathcal B_{p_0}(W_7),\qquad
R^{(2)}=\mathcal B_{p_1}(W_1),\qquad
R^{(3)}=\mathcal B_{p_1}(W_{12}).
$$

其 pure 分量准确使用 R71/R78 的

$$
\pi\mathcal B_A(T)
=\frac18T(A(q,q);q,q)
+\frac14T(q;q,A(q,q))
-\frac14A(q,T(q;q,q)).
\tag{5}
$$

C2 是 R196 的静态 F0 状态键 $(0,2,0,0)$ 原根；其 pure SHA 为

$$
\texttt{ad4cd7fcdcbac89c55309c6906b6cb3a6d869ad37834e4a32fe8cad1b6e33393}.
$$

所以 (1) 的完整归一化，包括 pure 模式系数，全部固定。若换用 R198 的单 isometric quartic $P_B$，其与 canonical pure 原根相差公共因子 16；不能只改变式 (1) 的某一项。

## 4. 新矩阵与原差为何给真实函数结论

新列按顺序为：

$$
\pi R_0\text{ 的16个已知基根},\quad
\pi C_4,\quad\pi C_6,\quad\pi C_2.
\tag{6}
$$

共 19 列、42 个共同 pure word 行。全部列经同一个 R178 固定颜色规范映射，所有余 letter 均满足 R179 的真实单射语法。没有使用非零不完备 NF 来宣告非成员，也没有将各列 history 独立赋值。

实际比较秩与加入目标后的增广秩准确为

$$
\operatorname{rank}(\pi R_0,\pi C_4,\pi C_6)=3,\qquad
\operatorname{rank}(\pi R_0,\pi C_4,\pi C_6,\pi C_2)=3.
\tag{7}
$$

全部 19 列的转换身份 SHA 为

$$
\texttt{4cf2c6100cb4983252d216ac5fa2365832a44d14483437aff20f2b85f4f64443}.
$$

R178 提供每列原表达式到共同表示的准确恒等；R179 保证表示单射，故 (7) 是 pure **真实算子**秩。

算法得到 (1) 后，先核对全部新原列转换身份的精确线性和，再独立组成

$$
\Delta=\pi C_2+\frac1{48}\pi R^{(0)}
+\frac{11}{64}\pi R^{(2)}
-\frac{13}{96}\pi R^{(3)}.
$$

该原差有 540 个 DAG 项，SHA256 为

$$
\texttt{26b40fda855b11499e46e3d1c7c8cc757a35ac50ff385c6a5e242da3099d2036}.
$$

独立 fresh 规范化后项数为零，准确零 SHA 为

$$
\texttt{4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945}.
$$

因此 (1) 有独立的原差身份，不能只被解释为某个消元标签相同。

### 4.1 为何三个旧响应已经给出纯像基

本次消元只把新的独立比较列加入 basis。每个 basis 的 combination 由自身原列及此前已加入的独立原列构成；一个依赖比较列的 combination 从不加入 basis。

对最后的目标作消元时，产生的成员组合因此只能使用已经加入的独立比较列。式 (1) 中旧 0、2、3 三个系数都非零，所以这三个原 pure 列都属于该独立列集合。集合的大小由 (7) 恰为 3，故

$$
\boxed{
\pi R^{(0)},\ \pi R^{(2)},\ \pi R^{(3)}
\text{ 是本次全部比较像的真实基。}
}
\tag{8}
$$

这是对已执行消元不变量和已保存系数的解释，没有重新计算矩阵。另有一个既有独立下界：R126 第 6 节已引用 R116/R125 的 $m=8$ 纯尾响应权零像维数 3；该尾投影经 universal pure 像因子化，也给 $\dim\pi(R_0)\ge3$。本文没有重评这个旧尾。

由 R196 的完整真基

$$
U_0=R_0\oplus\operatorname{span}(C_2,C_4,C_6)
$$

与 (7)–(8)，得到 (2)。C4、C6 的 pure 像也在 $\pi R_0$ 中；这来自完整比较秩，不需要声称本次摘要列出了它们各自的最简组合。

## 5. pure 核的准确维数及 balanced 范围

R196 给 $\dim U_0=19$、$\dim R_0=16$。结合 (2)，

$$
\boxed{
\dim(\ker\pi\cap U_0)=16,\qquad
\dim(\ker\pi\cap R_0)=13.
}
\tag{9}
$$

因而

$$
\dim\frac{\ker\pi\cap U_0}{\ker\pi\cap R_0}=3.
\tag{10}
$$

这准确说明完整权零响应商的三维方向都能选择 pure 零代表。它不意味着三维商为零。

R159 已证明在 pure 核上，balanced 混合投影 $\Xi$ 真实单射。故同一两个核的 balanced 像维数分别为 16 和 13；式 (3) 的 H 给一个明确 balanced 非零方向，因为 $\lambda_+(H)=1$。这些是 (2)、R196 与 R159 的纸面推论，本次没有新增 mixed 原式评价。

## 6. 正字符保留，pure 读出路线被准确排除

R196 的 $\lambda_+$ 在完整 U 上良定义，杀 R，且真实零矩成本满足严格长度恒等。式 (3) 中三项响应都在 R0 内，所以

$$
\lambda_+(H)=\lambda_+(C_2)=1.
$$

与 $\pi H=0$ 一起，这直接否定因子化

$$
\lambda_+=\ell\circ\pi\quad\text{于 }U_0
\tag{11}
$$

对任何 pure 像上的线性泛函 $\ell$ 成立的可能性。即使允许任意多个实或复 profiles、任意多 pure 输出点和导数、或整个 pure 输出函数，H 的全部这些信息仍为零，而 $\lambda_+(H)=1$。

因此本次结果比“$m=8$ 尾看不到该字符”更强：**全部 universal pure 模式已经看不到它。** 原 R133 的单幂尾结论不能提供这个加强；该加强由本次一般 profile 原恒等 (1) 才得到。

也不能由此推出 $\lambda_+$ 假、R196 的正性撤销或完整成本可为零。H 是 R196 完整真实 U 中一个非零 pure 核方向；正字符恰好能够检测这个被 pure 投影丢失的方向。

## 7. 对最右单 g step 和新增 gauge 的准确影响

R198 的最右单 g 阶段在全部右尾满足 f=0，故其 canonical period 是一个单 profile pure isometric quartic；全部允许的二阶 gauge 不能改变该右区间的 period。这个固定 profile 必要门本身仍有效。

本次只证明：不能把 R196 的 $\lambda_+$ 严格正性直接投影到该 pure 必要门。对某个具体真实路径 B，单 g period 仍可能非零，也可能需要其他真实不变量来判断。本文没有评价 R198 的固定 step，没有证明其 period 已消失或已可由 gauge 支付。

R199 所研究的新 faithful 单调 step 若构造完成，可以在**整个所有权 pure(U)** 上检测 universal pure 成本；它同样不能恢复一个已经被 universal pure 投影丢掉的 $\lambda_+$。faithful 于像与恢复投影核是两个不同问题，(4) 保证后者不能由选更好的 step 解决。

下一准确方向应保持完整 mixed 或研究 fixed-circle/gauge 的独立局部 period 不变量；不再试图通过其他 pure profile 重找这个已经被 (4) 排除的 $\lambda_+$ 读出。

## 8. 复现参数与完成边界

实际 CLI 与冻结设计相同：

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

@OUT@ 仅为 runner 临时目录。公开先执行七项新人工，再执行本次单一实际目标。零混合根计算、零新增响应列、零 N 收缩/投影、零旧 profile 评价、零幂尾查询；只恢复必要旧 pure 原根并计算本新投影门。

本文已完成 (1)–(11) 所述原函数身份、维数及不可因子化结论。不宣称实际 universal pure 零成本已经可达，不宣称固定第一圆或新增 gauge 的第四完整 range 已付，也不宣称主课题完成。

