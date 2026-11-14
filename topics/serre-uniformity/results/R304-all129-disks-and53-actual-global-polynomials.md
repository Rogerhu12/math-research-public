# R304：全部 129 个有理剩余盘的真实 Abel 常数及 53 方向全局项

## 1. 完整结论与范围

本条保存 $X_{\mathrm{ns}}^+(41)$ 在 47 处全部 129 个有理剩余盘的
实际 Abel 中心常数，以及每盘全部 53 个真实 Hecke 方向的全局多项式。
总数为 $129\cdot53=6837$ 个，均在同一模 $47^4$ 规范下计算。

文件 p41_all129_global_functions47_complete.json.gz 的 SHA256 为

~~~text
cf97e7db020cc81373dfd8584336365d23c1ec597ff91130f31882a1a0d48a90
~~~

这完成全局项；它不把全局二次型视为局部 Poincare 高度，也不声称
全部 129 盘的局部 QC 函数或共同根已算完。全部 108 个 de Rham
原常数的最终生产汇总仍由 R244 单独处理。

## 2. 实际输入的覆盖与身份检查

R237 的 113 个已完成盘由 110 个真实 SS 中心及三个普通 CM 中心
ORD_j38、39、40 构成。其中心和局部函数数据原样保留。
其余 16 个盘为

~~~text
ORD_j01, ORD_j05, ORD_j07, ORD_j11, ORD_j12, ORD_j15,
ORD_j19, ORD_j24, ORD_j27, ORD_j28, ORD_j30, ORD_j32,
ORD_j41, ORD_j43, ORD_j45, ORD_j46.
~~~

每个新增普通输入均要求真实整数乘法已完成全部 304 位、454 个操作；
所乘整数与 Abel 输出的整数完全相同。还逐一核对：

- 实际末点 SHA 与形式群对数的输入末点 SHA 相同；
- 完成的乘法证书 SHA 与 Abel 证书记录相同；
- 54 个循环坐标均在 $\mathbf Q_{47}$ 中，且循环基与 Lie 基往返通过；
- tiny 微分输入严格是 R234 的同一个 129 盘文件；
- 原 113 盘、补齐的 16 盘与 tiny 图的 129 个标签恰好一致，无重复无缺口。

ORD_j01 此时使用早先已经完成的纯 Abel 群链。该链的两个完整文件
分别以独立目录 R304_pure_Abel/ 保存，避免与正在保留真实主函数的
j01 重演混淆：

| 输入 | SHA256 |
|---|---|
| ORD_j01_Abel47.json.gz | 08dfbe394560bb140151351317d9905e45df9012fd0e789f973dbbf352d8d841 |
| ORD_j01_multiply47.json.gz | 8ba75b4cc1a43e76b839dd7a6fad52982cdfeaceda87df18c1fcd8de8f0f8dfe |

该选择不需要第二类积分或主函数链已完成：本条只使用已经核准的
全纯 Abel 对数。没有把进行中的群链误标为完成。

## 3. 同一坐标和精确全局装配

每盘都使用 R228/R231 的真正中心化射影参数 $z$，并令 $y=z/47$。
令 $C=P-b=aB_{-4}$，在 R89 八个数域的既定顺序和升幂循环基中写

$$
a(y)=a_0+a_1y+a_2y^2+a_3y^3\pmod{47^3}.
$$

$a_0$ 是上述实际中心常数，后三项来自同一个真实盘的已完成 tiny
积分，不能跨盘或跨标架替换。对每个原 R228 方向 $F_n$，按原
精确全局公式

$$
G_n(a)=\operatorname{Tr}\!\left(
s\{800F_na^2+(80F_nr_{-3}-20\xi_{2F_n})a\}\right)
\pmod{47^4}
$$

逐块求值，保存 $y^0$ 至 $y^4$ 五个系数。程序先求到 $y^6$，并且
逐项断言五、六次系数为零；没有直接舍弃可能非零的高次系数。
全局线性和二次系数均被 47 整除，所以模 $47^3$ 的 Abel 坐标足够
确定模 $47^4$ 的全局值。遗漏的 Abel 尾项以及高次乘积由 R230/R237
已证明的估值界控制。

原 53 个方向标签、八域坐标基及坏分量标签 $[0,3,28,32]$ 整体
复制到输出；各方向的坏分量向量不重新配对。故后续求真正 QC 共同根
时可以直接按同一个分量标签减去真实局部高度。

## 4. 可复现输入快照

输出的 actual_rational_disk_global_polynomials 是 129 行记录。
每行保存 disk_id、54 个中心循环坐标、四项循环坐标级数，以及
global_polynomials 中 53 行 n 与 coefficients_0to4_in_y_mod47four。
两个 complete_all129 标记为真，局部高度和共同根标记保持为假。

R304-global-input-snapshot.json 逐个绑定三项共同输入和 32 个普通
Abel/乘法文件的 SHA。快照重建入口按这个映射恢复输入，因此后续
j01 真实主函数链完成后也不会静默换掉本条已经核准的原输入。

~~~bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python \
  scripts/p41_rebuild_all129_global_functions47.py \
  --script-dir scripts \
  --snapshot scripts/data/R304-global-input-snapshot.json \
  --work-dir /absolute/path/to/rebuild-R304 \
  --output /absolute/path/to/rebuild-R304/global129.json.gz
~~~

本次实际运行了装配器；另外按快照重建并要求整个 gzip 文件的
SHA 与上述最终输出一致。只进行了已有真实数据的线性/二次装配，
没有重复任何原群链或把未计算的局部高度填成全局项。
