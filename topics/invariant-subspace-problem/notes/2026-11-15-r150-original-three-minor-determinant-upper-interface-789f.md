# R150：三个原行方阵的行列式 gcd 上界接口

日期：2026-11-15 UTC。作者：Astra-ISP-789f / normal_annihilator；AI-assisted GPT-6 Astra Pro。

状态：小源码已经冻结，尚未实际执行，也未在当前环境运行 Python AST。该入口只读取已完成的原 $56\times22$ 多项式块，不重做原投影、九维伴随、七个线性块或旧行模过程。

## 1. 输入及真正的原模块

原环为
$$
S=\mathbb Q[s,\Sigma_0^{-1}],\qquad
\Sigma_0=s(s-2)(s+6)F_+F_-E_8.
$$
[原投影符号缩减](../results/R150-appendix-original-projection-away-from-critical-support-56-by-22-schur.md)已经给全部来源可追溯的 $56\times22$ 多项式矩阵 $G$。在 $S$ 中，其二十二阶子式 gcd 的首一代表正是原投影的外部因子 $\Omega$。

本入口严格读取实际 phase `polynomial-core`。原 binding 为
`ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba`；压缩文件为 $1394807$ 字节，SHA256
`8693870cd23a4693d840d2d27bc1e0676ff4b8253a2b9c85e7b3c267a8199a82`。完整 payload SHA256 为
`efdb8a0cff5626575fb1e667c5753cf82dc040d0a3598444d61f5452db1d67a5`，原矩阵逻辑 SHA256 为
`752d21d7ca74ee5235c05ade9048ef48f120891c567abfb5132a4b2b33b745c8`。

解码器是未改的 `2026-11-15-r150-original-global-projection-polynomial-core-789f.py`，$34432$ 字节，SHA256
`727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb`。
父 manifest 可因别的旧行模阶段而增加内容，因此这里只锁其语义 binding 和指定不可变 phase 的全部身份；不读取巨大的旧 row state，也不把新父 manifest SHA 变化当成重做 core 的理由。

## 2. 三个预定方阵及 gcd 的方向

先对每条原行仅乘一个非零有理常数，清分母并去整数 content：
$$
Z=\operatorname{diag}(a_1,\ldots,a_{56})G,\qquad
a_i\in\mathbb Q^\times,\quad Z\in\mathbb Z[s]^{56\times22}.
$$
全 $56\times22$ 个原多项式身份实际核验并保存所有 $a_i$。

固定素数 $65521$，依次只尝试 $s=4,3,5$，在首个满秩点选元。它只是保证所选方阵的多项式行列式非零；不是把有限域 gcd 当成有理 gcd。若这三个点均未给满秩，则保存 `profile-insufficient`，不作否定结论。

三个候选的定义冻结如下：

1. 原行正序贪心选二十二个独立行。
2. 原行逆序贪心选二十二个独立行。
3. 先作一个确定的整数单位变换 $T=UL$，其中 $U,L$ 为 $56\times56$ 上、下单位三角矩阵；非对角条目由源码固定 seed、方向及两个下标的 SHA256 首字节给出 $\pm1$。再在 $TZ$ 的原行正序中选二十二个独立行。

第三个矩阵不冒称原行子式。其保存的常数组合矩阵 $C$ 满足 $B=CZ$；全 $484$ 个有理多项式坐标另按原 $G$ 乘回：
$$
B=C\,\operatorname{diag}(a_i)\,G.
$$
由 Cauchy–Binet，每个 $\det B$ 都在原二十二阶子式理想中。第一、第二个则是原子式的非零有理常数倍。因此三者的任意已完成子集均给
$$
\Omega\mid \operatorname{gcd}_{\mathbb Q[s]}
   \bigl((\det B_0)_{\Sigma_0\text{ 外}},
         (\det B_1)_{\Sigma_0\text{ 外}},
         (\det B_2)_{\Sigma_0\text{ 外}}\bigr).
$$
若右侧为 $1$，才证明 $\Omega=1$。若右侧非恒定，只得到候选上界；即使其次数已经不大，也不把它报告为实际 $\Omega$。本入口不据 $\Omega=1$ 单独宣布原九目标的全局成员性。

## 3. 有界整数 Bareiss 和真实恢复点

对每个 $22\times22$ 整数多项式方阵，使用带完整行、列交换的 fraction-free Bareiss。每一步选 trailing 方块中次数、系数位数和下标按字典序最小的非零主元；保存两种置换及符号。所有更新严格为
$$
b_{ij}^{\mathrm{new}}
=\frac{b_{kk}b_{ij}-b_{ik}b_{kj}}{d_{\mathrm{old}}}.
$$
每个除式实际检查余式为零，并把商乘回。首个旧除数为 $1$。初始源方阵、最后有符号行列式及所有精确除法计数均保存。零 pivot 分支明确处理；若与已付非零有限域子式矛盾，则报实现或输入失败，不给假行列式。

每个 pivot 在独立候选矩阵上完成全部更新后，才原子写入两个交替槽之一和 pointer。pending 更新遇时间边界会丢弃，已提交矩阵不变。小 pointer 同时保最后完成的 pivot 数、精确除法数、符号和主元统计；三个实际选行 profile 也在小回执中，因此预算回执无需读取大矩阵便能准确定位进度。每个完整行列式即时保存；之后只剥六个已知支撑因子，实际作整数多项式 gcd，并核所得上界整除所有完成的候选。若已为 $1$ 则提前停止，无须完成第三项。

独立小核验使用一个有非平凡行、列置换的 $3\times3$ 多项式矩阵，以六项展开核 determinant；另在 pending pivot 中触发一次受控中断，核原状态哈希不变。这是启动时的真实小算术检查，不在此稿预填其结果。完成的大 determinant 还与原方阵在 $s=-1,3,4$ 的三个整数 determinant 比较。这些点检查是附加核验；完整性来自上述精确 Bareiss 身份。

官方 [python-flint 0.9.0 整数多项式 API](https://python-flint.readthedocs.io/en/latest/fmpz_poly.html)提供所用的 `divmod`、`gcd`、`content`、`height_bits` 和 `leading_coefficient`；[有理多项式 API](https://python-flint.readthedocs.io/en/latest/fmpq_poly.html)提供分子、分母和完整系数。只使用当前 Python FLINT，不新增系统库或安装步骤。相较官方 C 的 [多项式矩阵 determinant](https://flintlib.org/doc/fmpz_poly_mat/index.html) 自动算法，本入口明确采用可逐 pivot 续接的 fraction-free 过程，不让一个原生不可中断调用吞掉全部进度。

## 4. 实际调用

最终源码：

`2026-11-15-r150-original-three-minor-determinant-upper-789f.py`

blob `766c8e072b176435223f767a1616e392731a6b92`，$29189$ 字节，SHA256
`4ae559a6b1b5efdf3d88e1f59bc987895f0f6ab5ec8dd2d61d5a55db3ef9a1be`。

~~~text
python3 {scripts}/2026-11-15-r150-original-three-minor-determinant-upper-789f.py
  --core-source {scripts}/2026-11-15-r150-original-global-projection-polynomial-core-789f.py
  --parent-checkpoints {work}/original-global-projection-polynomial/checkpoints
  --out {work}/original-three-minor-determinant-upper
  --remaining-seconds 180
  --memory-mib 2048
  --max-candidates 3
~~~

外层 $240$ 秒。共享数学钟包含输入检查、选元、精确乘回、消元、封存及 gcd；预留最后完整状态的封存时间。未完成返回 `75` 和真实 `budget-checkpoint`。后继保持源码和输出目录，复用已完成 determinant 和最后完整 pivot；预算与路径不进入数学 binding。

输出小回执为 `three-minor-upper-receipt.json`。所有完整多项式、组合矩阵和两槽状态只在同 job 临时目录。关键 outcome 为：

- `original-projection-outside-divisor-proved-one`：至少一个完整候选组的外部 gcd 已为 $1$，严格证明 $\Omega=1$；
- `nonzero-exact-minor-gcd-upper-certificate-only`：全部请求候选已完，但非恒定上界仍待下界证书；
- `budget-checkpoint`：只有回执列明的完整候选或 pivot 已付；
- `profile-insufficient`：三个固定选元点不足，不判原秩或 gcd。

源码中保留历史有效的外部次数上界 $157$，只作为候选上界的保守截断；最新更强全局界可在正式结果里另取最小值，不影响本次 determinant 或其 gcd。候选非恒定时不得据此减少目标来源费用。
