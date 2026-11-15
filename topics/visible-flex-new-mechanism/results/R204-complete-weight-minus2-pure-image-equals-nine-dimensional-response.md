# R204：权 −2 的完整 pure 像等于既有九维响应像

日期：2026-11-15。**公开 Actions 实际已完成，准确原函数成员结论。** 本稿不把已证基重算成一个新发现；唯一新增问题是 R186 的十二个真实商基的 pure 投影是否仍在旧九维响应中。

## 1. 完整结论

记 U 为同端口/frame I、M=T0 的完整 canonical 第四成本真实 span，R 为已可调响应空间，π为整个 universal pure −4 相位算子投影。沿用同一右锚和全部真实历史。实际结果是

$$
\boxed{\pi(U_{-2})=\pi(R_{-2}),\qquad
\dim\pi(U_{-2})=\dim\pi(R_{-2})=9.}
\tag{1}
$$

这里下标 −2 是**真仿射权**，不是 pure 所取的 Fourier 模式 −4。式 (1) 是整个单 profile 原函数算子像的等号，不是某个 profile、幂尾、有限点查询或必要 normal form 的近似关系。

已证完整维数为 $\dim U_{-2}=52$、$\dim R_{-2}=40$。因此

$$
\boxed{
\dim\ker(\pi|_{U_{-2}})=43,
\qquad \dim\ker(\pi|_{R_{-2}})=31.
}
\tag{2}
$$

诱导映射

$$
U_{-2}/R_{-2}\longrightarrow
\pi(U_{-2})/\pi(R_{-2})
$$

为零映射，故其整个十二维定义域都在核内。完整十二维商没有消失；它在 pure 投影后不再产生新商方向。

## 2. 只需十二个新成员身份的原因

[既有 R151](R151-general-pure-J-identity-nine-dimensional-range-and-kernel.md) 已证明原响应 R40 的 pure 像为九维，原 R40 中可取基的位置为

$$
0,1,2,3,8,9,10,12,19.
\tag{3}
$$

它的三十一条已完成原式身份给上界，已付的真实评价 minor 给下界。本轮没有重算原 R40 秩，也没有重做那三十一条原差。

[R186](R186-complete-weight-minus2-function-kernel-and-five-dimensional-character-head.md) 已给完整 $U_{-2}$ 真基：原77列中的前四十列 R，加上

$$
40,41,42,43,44,45,46,49,51,52,54,58.
\tag{4}
$$

其原 normal 下标依次为

$$
0,1,2,4,5,7,8,23,28,30,38,46.
$$

R174 的七十条字面关系与 R186 的二十五条完整共同 word 身份已经覆盖其余原列。对这个已证完整基应用线性 π，便知只需判断 (4) 的十二个新 pure 向量。无需重做旧52维联合矩阵或另外消元其余25列。

## 3. 唯一新实际及观察来源

公开运行：[43684612905](https://github.com/Rogerhu12/math-research-public/actions/runs/43684612905)。

- 源提交：`df8522fc261de1dbb09975a594f0fda93f0867b0`。
- 科学 job：`132722373952`，最终 success。
- 脚本：[literature_pure_minus2_archived_projection.py](../scripts/literature_pure_minus2_archived_projection.py)，27076 B，SHA256 `debb22d741b40b952c64cbaefc988c5e6cc2acb5882a5c1c667201afad6ab8e7`。
- [计算设计](../notes/pure-minus2-archived-projection-design-20261115.md) 与 [本次参数](../computations/request-continuation.json) 在该源提交中完整保留；后续请求文件可以继续更新，应据源提交读取本轮参数。
- [metadata receipt](../notes/actions-43684612905-1-pure_minus2_archived_projection/receipt.json)，46353 B，SHA256 `9d205d7fbd72d0f62e99031ebbddd17bca16fd1d5abbafee4d0b9c16539ffaa5`。

十二个实际入口参数元素为：两个已存输入目录 `actions-43676765171-1-character_head_word_relations`、`actions-43657785023-1-general_pure_J_membership`，以及 `--seconds 120 --memory-mib 512 --rational-bits 16384 --output @OUT@/pure-minus2-archived-projection.json`。目录相对 `topics/visible-flex-new-mechanism/notes`；完整文件/SHA/bytes、producer/run/source 绑定写在脚本的 WORD/PURE 常量和设计中。

新入口首先运行同源 `--toy`。公开日志直接显示 `toy_passed`、`artificial_development.all_passed: true`、`synthetic_only: true`；同源共有17项新增小人工断言，没有研究输入访问。随后唯一实际入口完成全部十二个目标。

root 直接读取了该 job stdout 的一条完整 `MATHEMATICAL_RESULT`、十二条 `MATHEMATICAL_COLUMN`、开发通过信息和输出 hash，并与 receipt 核对。本次脚本没有把完整临时主报告打印到 stdout；本稿不声称读到了其中未输出的精确 elapsed/RSS/有理操作计数，也不为这些非必要统计重跑研究。

## 4. 十二个原函数成员的完整证明

消费者只读取两份已经发布的完整呈示。R186 每个所选列的已存 −4 分量是同右锚 R178 余 letter 字典行，并绑定其原完整 pure 根的 SHA；R151 同一原根与九基编号跨来源相同。新入口检查这些原来源、全部77列完成覆盖、原147/normal映射、转换完成标志和字典行身份。

对 (3) 的已证九基只准备准确三角解算器；随后只把 (4) 的十二列减去该基。结果逐列为

| 新原77位置 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 49 | 51 | 52 | 54 | 58 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 旧九维像中的成员 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 |
| 新商余项项数 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

每个新关系还从**未修改的已存原代表词表**独立重新相加，全部准确为零；不是只检查归约过程最后的缓存变量。公开 stdout 逐条给了各自准确有理系数和新原代表总和为零的结果。完整再生证书不保存。

例如最短的一条是原位置52（原 normal 30）：

$$
\boxed{
\pi C_{52}
=-\frac3{32}\pi R_0-\frac3{64}\pi R_2
+\frac18\pi R_8-\frac9{64}\pi R_9
+\frac3{64}\pi R_{10}.}
\tag{5}
$$

这里的下标0、2、8、9、10均是原 R40 位置，不是仿射权。式 (5) 只是解释一种新数学身份的记号；其余十一条的全部具体系数由冻结脚本和同轮 stdout 定位，不复制机器字典或证书到本稿。

R178 的原函数 soundness 已保证这些共同词行相等可升为真实 universal 函数相等。结合 R186 的完整基覆盖，十二条关系给

$$
\pi U_{-2}\subseteq\pi R_{-2}.
$$

反包含来自 $R_{-2}\subset U_{-2}$；既有九维下界不变，故得到 (1)。本次所有新余项均为零，不需为非成员另调用 R179 独立性或产生额外对偶。R179 仍是该公共消费者在其他可能输出下的完整性依据。

## 5. 输出身份与根规则15

本次只保存源码、参数、run 编号、hash 和本文数学结论；没有提交或上传再生输出 payload。

| 临时对象 | bytes | SHA256 |
|---|---:|---|
| 开发报告 | 3334 | `eaafec6c42c8de63bbe41fda3e3a7c9f15cf64b057c4e55613cb6e9da670826e` |
| 主报告 | 18007 | `9666aaf9ae2313e3e6d65f904aaea86e6de00ffa5157379cccdb819d399bc488` |
| 内存完整新证书 | 34362 | `e095e042d0188b526d789393eb074e0cda75d8c546e1f9ebb5c632e2571eacd6` |

开发与主报告只在 runner 临时目录产生；完整证书只在内存中形成。receipt 明确 `output_payloads_committed_or_uploaded=false`、`release_assets_created=false`、`machine_certificates_saved=false`。研究前及发布前实际 pull 均记录所读源提交 `df8522fc261de1dbb09975a594f0fda93f0867b0`，两 README 未变。

运算预算为120秒、512MiB软轮询、16384有理位、200万次稀疏更新；预算是上限，不是观察到的实际耗用。源代码没有导入旧 compiler/normalizer/forcing/profile/geometry 库，且实际入口只允许本公开 Actions。

## 6. 与已付结果相接的准确意义

[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md) 给 $\pi U_0=\pi R_0$、维3。不同真权的像为直和，R 本身真权分解不变，因此本稿与 R201 合并给

$$
\boxed{
\operatorname{im}\big[(\Pi_0\pi,\Pi_{-2}\pi):U\to P_0\oplus P_{-2}\big]
=
\operatorname{im}\big[(\Pi_0\pi,\Pi_{-2}\pi):R\to P_0\oplus P_{-2}\big],
\quad\dim=12.}
\tag{6}
$$

这是十二维**完整算子分量**的线性像结论，不是只在十二个点满足等式。R102 的真实有限复制/Brouwer 方法能否在同一几何设计中同时支付它们，须依其真实原响应生成器、所有自成本、共同包络、闭位置及已付低阶条件逐项接好；不能仅从 (6) 直接忽略这些义务。

另由 [R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md) 在 pure 核上的 balanced 单射，(2) 对应的 balanced 像维数为43及31。这没有把这些纯核向量宣布为实际有限可达成本。

[R188](R188-no-nonzero-positive-affine-character-at-weight-minus2.md) 的“该权无非零正字符”此前已经完整结束。本稿是新的原函数纯像成员定理，没有重做它的 action 或路径正性。完整 $U_{-2}/R_{-2}$ 的十二个方向仍存在，其可见性由其他相位分量承担。

剩余真权的 pure 像、整个 pure 周期的实际有限匹配、全部 mixed/零相位与同一二阶 gauge 的 ruling、高阶收敛、固定 g 的连续嵌入和全时间 reach 仍须继续；主课题尚未完成。
