# R150：原整数 Koszul 外支撑的精确有理求解接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

状态：源码已冻结；本接口不预报尚未执行的有理解或新增真核。先前的原整数稀疏准备已真实完成：run 43679903558，step koszul-exact-sparse-preparation，执行源 5151739a08307a8d3305a5e6060362f386d5b15b，数学 0.412781492 秒。没有可用的一、二支撑行；完整核心仍有 1632 个变量、1808 个非零行、44362 个非零项，最大整数系数 132 bit。26 个原外支撑行恒零；原 1834 行仍完整保存并在后续核验。

## 1. 真实输入和预算

唯一输入是上一阶段实际生成的原整数模型与核心，加原 17 式模型和已付完整乘回辅助程序。既有原正常形和 p768 来源不重算。

准备目录包含：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| exact-original-koszul-outside-model.json.gz | 814572 | 0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d |
| exact-koszul-sparse-core-and-dag.json.gz | 292828 | d9645a8cda617528a6c4a047291e56df6530cb81631e9579f4552a8f8dd3285c |

准备 binding 为 504e56f3cdd71d9527fbf7db4d0b37eff12c55e57b20a7292171c7d1c40806e0。新程序验证准备回执的全部字节身份、同一 binding、原点模型和辅助程序 SHA。恢复绑定不含临时目录路径。

一次共享数学预算 300 秒，每进程 2048 MiB；原核心、模 31 选元、精确求解、全来源核验均计入同一时钟。精确求解在受父进程墙钟约束的独立子进程中进行。它返回后先保存完整有理结果，随后才做全部残差和原式核验。不存在把求解器返回等同数学完成的快捷门槛。

命令为：

~~~sh
python -B 2026-11-15-r150-koszul-exact-rational-support-solve-789f.py \
  --helper PAID_SOURCE_HELPER \
  --point-model ORIGINAL_POINT \
  --prepared-dir ACTUAL_PREPARATION_DIRECTORY \
  --out FRESH_OUTPUT_DIRECTORY \
  --seconds 300 --memory-mib 2048
~~~

同一输出目录接续时显式加 --resume。已经完整保存的选元、精确求解、来源系数核以及逐列原乘回证书均按真实绑定复用。未完成的 native 求解内部迭代没有声称可续；其完成之前只有真实输入与选元保留。

## 2. 为什么模 31 选元合法

写准备后的精确有理等价核心为 $M$。取 $\bar M$ 的全部 $r$ 个主元列，再从这些列选取 $r$ 个独立原行，得到原整数方块 $B$，其模 31 行列式非零，所以 $B$ 在 $\mathbb Q$ 上可逆。

令其余变量为 $x_F$、主元变量为 $x_P$。所选行准确为
$$
B x_P+E x_F=0.
$$
求解器只求原整数矩阵的有理解
$$
X=B^{-1}E,\qquad x_P=-Xx_F.
$$
没有把模 31 RREF 系数当成有理系数。本题当前预期 $r=1603$、$|F|=29$，程序实际重新记录核心选元所得数值。

取这个有理图空间的完整基，逆代所有已保存稀疏消元，得到原 1632 个 Koszul 系数中的列矩阵 $Y$。本次 DAG 为空；通用代码仍保持其原变量编号和精确有理比例。

先核所选原整数行的全部 $B(-X)+E=0$。再计算原完整外支撑矩阵的
$$
R=O Y\in\mathbb Q^{1834\times|F|}.
$$
因此真实来源系数核准确为
$$
\ker_{\mathbb Q}O=Y\,\ker_{\mathbb Q}R.
$$
每一环均是双向参数化：所选行给图空间，全部未选行给完整残量核。若 $R$ 非零，程序不会丢弃这些新约束；它在全部待定列上精确求核。因此所得维数可以小于 29。

## 3. 原来源和原输出的最终门槛

将每一条真实有理核清分母并约成整数列 $c\in\mathbb Z^{1632}$，形成原来源
$$
v=\Phi c\in\mathbb Z^{6188}.
$$
每一列均逐项验证：

1. 6188 个原来源都使用原方程、原单项式及原行号；
2. 1834 个未选来源系数全部为零；
3. 以真实原 17 式整数系数乘回，全部 4367 个输出严格为零；
4. 记录完整 36 个自由来源坐标，最后在 $\mathbb Q$ 上核其秩及与已付 23 个规范自由轴的联合秩。

设最后联合秩为 $u$。只有完整核验完成后才可得
$$
\operatorname{rank}_{\mathbb Q}C_0\le4354-u.
$$
新独立真方向数为 $u-23$，不是求解器返回的列数，也不是模 31 新生方向数。

如果新真 Koszul 自由像本身维数 $d$，且联合秩仍为 $d$，则已付 23 个自由轴都包含其中。由于原非自由 4318 列有模 31 非零子式，其在 $\mathbb Q$ 上独立，所选真核由自由坐标唯一决定；在该条件下才能进一步推出旧 23 条真核都属于新精确 Koszul 空间。程序只记录精确包含关系，正式推论由实际完成数据给出。

## 4. 完成与恢复范围

主小回执为 koszul-exact-rational-support-receipt.json。

成功 status=completed 必须同时有：

- completeKernelDimensionCertifiedOverQ=true；
- all1834OutsideSourceCoefficientsZero=true；
- allOriginal4367IntegerProductsZero=true；
- complete36FreeImageRankOverQ 等于真实完整 Koszul 核维数。

budget-exhausted 只表示本次共享时钟结束；已保存完整阶段可以复用。failed 保留具体错误和真实完成点。没有完成的候选不登记为核。

完整有理解、原来源和证书仅在当前运行临时目录保存。按根 README 第 15 条，长期只保存源码、参数、运行号、小回执及哈希，不将可重算大数据放入 Git、Release 或长期工件。

## 5. 使用的精确算术接口

FLINT 的有理矩阵接口使用 [python-flint 官方 fmpq_mat 文档](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html) 中的 solve(algorithm="dixon") 和 rref。有限域 RREF 仅用于挑选原整数单位子块。原整数完整乘回与所有来源约束由程序逐项核验，故不依赖浮点近似或概率性的残差检查。
