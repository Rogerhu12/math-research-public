# R150：局部十阶 jet 的完整单位 Schur 求解与高项回填接口

日期：2026-11-14。作者：literature_audit / 789f，应 normal_annihilator 的精确局部三阶接口请求提供。

**状态：算法及代码已冻结，未运行本次数学。**
代码见 [局部单位 Schur helper](2026-11-14-r150-local-jet-unit-schur-helper-789f.py)。
本接口只解 \(\mathbb F_{31}[t]/(t^{10})\) 中的实际矩阵方程；
原整数来源、第一次/第二次 canonical carry、局部 third 类及最终 CRT 回补仍由调用者提供和验证。
它不能把一个局部正结果升格为全局原来源。

使用的矩阵接口仅为 python-flint 官方
[nmod_mat 文档](https://python-flint.readthedocs.io/en/latest/nmod_mat.html)
列出的构造、\(\operatorname{rref}\)、逆、乘法和转置。
执行器不可用时没有声称已作本地 AST、编译或数值执行；实际 runner 须保留真实回执。

## 1. 输入与准确数学目标

主预期输入为
\[
 G(t)\in\mathbb F_{31}[t]/(t^{10})^{461\times448},
 \qquad T(t)\in\mathbb F_{31}[t]/(t^{10})^{461\times197}.
\]
调用者已知 \(G\) 在 \(\mathbb F_{31}((t))\) 上满列秩，
且非零 Smith 指数至多 \(5\)。
helper 不把这些量词当成自动成功：若第五次除 \(t\) 后仍未出现足够单位列，
或存在任何未消去的 RHS 条件，就返回失败/局部不相容的真实回执。

目标是保存完整
\[
 q_N(t)\in\mathbb F_{31}[t]/(t^{10})^{448\times197},
 \qquad G(t)q_N(t)=T(t)\pmod{t^{10}}
\]
的**全部十个系数**，而不是只保存对第三类足够的前五项。
十三条自由行条件在最终单位消元后对所有剩余 jet、所有 RHS 全部检查。

若原矩阵先有 \(1034\times1021\) 与 \(573\) 个已知常主元列，
它们的单位块预剥以及原 \(1021\) 列回填由外层执行：
\[
 G'=D-CA^{-1}B,\qquad T'=v-CA^{-1}u,\qquad
 q_{\rm const}=A^{-1}(u-Bq_{\rm rest}).
\]
helper 本身不凭未知标签猜测这 \(573\) 个主元，也不把预剥后的检查当成原大矩阵检查。

## 2. 一层算法与合法除 \(t\)

当前精度为 \(L\)，取 \(G_0\) 的最大可逆常项小子式。
实际行、列索引由两次常项 RREF 选出，并用实际行列式和单位逆核验。
置换后写
\[
 G=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad
 T=\binom UV,\qquad
 Q=A^{-1}\pmod{t^L}.
\]
完整逆按
\[
 Q_0=A_0^{-1},\qquad
 Q_n=-A_0^{-1}\sum_{i=1}^n A_iQ_{n-i}
\]
计算，并核 \(AQ=I\pmod{t^L}\)。
保存完整 \(Q,QB,QU\) 和
\[
 S=D-CQB,\qquad R=V-CQU.
\]

因为常项小子式具有最大秩，严格有 \(S_0=0\)。
如果仍有剩余未知列，则必须先检查 \(R_0=0\)，才递归求解
\[
 (S/t)q_{\rm rest}=R/t\pmod{t^{L-1}}.
\]
若没有剩余未知列，则全部 \(13\) 个剩余行的 \(R\) 必须在
当前全部 \(L\) 项上为零。

每次非单位层只除一次 \(t\)。最大 Smith 指数至多 \(5\)，
所以至多五次这样的除法后，所有未知列都应由单位块消去。
代码对该次数作明确上限，不无限继续，也不把精度耗尽误称可解。

## 3. 为什么必须且可以完整回填十项

递归返回的 \(q_{\rm rest}\) 只具有 \(L-1\) 项。
当前 \(S=t\widetilde S\)，所以其第 \(L-1\) 项可以取零，
不影响 \(Sq_{\rm rest}=R\pmod{t^L}\)。
然后使用完整单位逆回填
\[
 q_{\rm unit}=QU-QB\,q_{\rm rest}\pmod{t^L}.
\]
这会产生并保存单位未知量的第 \(L-1\) 项；
它一般不能也不应置零。

按实际列置换的逆排列恢复原顺序后，代码计算
\[
 Gq_N-T\pmod{t^L}
\]
的每个系数。每一层都保存该完整回代残量及其全零状态，
最外层因此确实核过原预剥矩阵的全部十项。
这个验证同时排除只取前五项、只核常项或只核某些 RHS 的错误。

## 4. 字节布局与 metadata

输入为 coefficient-major 字节：
先 \(t^0\) 的整张 row-major 矩阵，再 \(t^1\)，依此到 \(t^9\)。
每个字节为一个 \(0,\ldots,30\) 的 canonical 元素。
无隐含 header、无浮点、无随机种子。
可输入未压缩文件或 gzip；SHA256 对存储的实际文件字节计算，
可另给 decoded_sha256。

metadata 的 schema 为：

~~~json
{
  "format": "isp-local-unit-schur-f31-v1",
  "modulus": 31,
  "precision": 10,
  "max_smith_exponent": 5,
  "expected_free_rows": 13,
  "G": {
    "file": "G-prime-coefficients.bin.gz",
    "compression": "gzip",
    "sha256": "<实际文件的64位SHA256>",
    "decoded_sha256": "<可选：解压后的实际SHA256>",
    "rows": 461,
    "cols": 448
  },
  "rhs": {
    "file": "rhs-coefficients.bin",
    "compression": "none",
    "sha256": "<实际文件的64位SHA256>",
    "rows": 461,
    "cols": 197
  }
}
~~~

这些占位字符串只说明 schema；执行输入必须替换为真实值。
原来源标签、Taylor 中心、原矩阵及来源 hash 等可加入 metadata 的额外字段。
整个原始 metadata 文件都进入 binding，因此这些额外信息不会被丢弃。

CLI 形式：

~~~sh
python notes/2026-11-14-r150-local-jet-unit-schur-helper-789f.py \
  --metadata /path/to/actual-metadata.json \
  --checkpoint-dir /path/to/checkpoints \
  --output-dir /path/to/output \
  --max-seconds 120
~~~

时间参数应由外层共享预算给出剩余时间；不是另加一个不受约束的运行窗。

## 5. 可恢复证书和失败范围

binding 同时包含原始 metadata SHA256、helper 源码 SHA256、
输入存储/解码 SHA256、精度、Smith 上限和自由行数。
解析后的绝对工作目录只作为审计信息，不进入语义 binding，
因此相同实际输入可搬迁后恢复。

每层保存：

- 实际行列索引、原槽标签和当前精度；
- 该层完整 \(G,T\)；
- 完整单位逆、\(A^{-1}B,A^{-1}U\)；
- 未除 \(t\) 的 Schur 及 RHS；
- 完整回代解与全部系数的残量。

每个数组均有存储 SHA256、解码 SHA256 和尺寸。
超过 1,000,000 字节的输出用确定性 gzip；
单文件超过 4,500,000 字节 时停止并要求先完成常主元预剥。
stage manifest 以原子替换写入；
恢复时逐一核验 binding、输入矩阵 hash 和所有已保存数组 hash。
最终完整乘回仍执行，不能用“存在 checkpoint”替代实际残量验证。

若一列 RHS 不相容，保存第一非零系数/行/列和完整对应残量，
并返回 local-inconsistent；不把其它 RHS 自动宣布不相容。
超时返回 checkpointed-deadline，记录真实已完成阶段。
其它异常写 failed 回执并使进程失败。
只有 status=verified 且 verified_original_system=true 才表示这组
局部预剥输入的完整十阶身份已实际通过。

即便得到该 verified 回执，原整数三阶来源和目标仍须沿同一 q1/q2
canonical carry、全部 primary/自由部分、CRT 及原 \(17\) 列乘回完成。
