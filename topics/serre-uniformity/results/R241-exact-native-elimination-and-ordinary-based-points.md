# R241：保持实际群运算的整数消元与全部 19 个普通基点差

日期：2026-11-13。本文给出 R121 群运算引擎的精确整数消元实现，并构造 R231 全部 19 个普通有理中心的真实 Makdisi 点 \(P-b\)。它为余下 16 个普通盘的大 Abel 积分提供已执行的入口；**本条尚不宣称 16 次完整倍乘、对数提取或局部 QC 高度已完成**。

## 1. 环、精确运算与接口

始终使用

\[
 R=(\mathbf Z/47^4\mathbf Z)[i]/(i^2+1).
\]

`p41_native_r2_linear47.py` 的 `install(r, build_dir)` 编译同目录的 `p41_r2_mod47_native.cpp`，仅替换既有模块 `r` 的 `rank_pivots` 与 `inverse_matrix`。矩阵格式、实际单位主子式的原始行列索引、核空间与 Frobenius 规范均保持既有接口。编译后的共享库只放在指定的工作目录；源 C++ 与 Python 文件是复现所需文件。

```python
from p41_projective_jet_frames47 import install_exact_float_mm
from p41_native_r2_linear47 import install

install_exact_float_mm(r)
manifest = install(r, build_directory)
```

前一个函数仍按 R222 的已证明整数界进行精确矩阵乘法：每个非负实矩阵内积的整数值严格小于 \(2^{53}\) 时，分别计算四个 float64 内积，各自转换回整数并取模，最后再复合实虚部；不满足该界时回落到原始有界 int64 算法。本条没有修改乘法逻辑。

新的消元只在 \(\mathbf F_{47}[i]\) 上进行整数运算。因 \(47\equiv3\pmod4\)，一个元素 \(a+bi\) 非零当且仅当其范数 \(a^2+b^2\) 非零，其逆为

\[
 (a-bi)(a^2+b^2)^{-1}.
\]

C++ 代码逐列选择与原始 NumPy 代码相同的第一个可用非零主元，记录同一行置换，并执行同样的初等行运算。每次取模前加入固定的 \(47^2\) 或 \(3\cdot47^2\)，保证整数为正；所有内层计算量都小于 \(4\cdot47^2=8836\)。因此 int32 运算不会溢出，也没有近似数或不同特征的替代秩计算。由消元步骤逐项归纳，返回的单位主子式与原函数相同。

逆矩阵先在 \(\mathbf F_{47}[i]\) 用完整增广矩阵得到，再在原环中执行两次

\[
 C\longmapsto C(2I-AC).
\]

误差 \(I-AC\) 每次平方，故精度从 47 提升到 \(47^2\)，再到 \(47^4\)。每次调用最终仍检查完整矩阵 \(AC=I\)，所有 Makdisi 核空间仍由原函数检查完整矩阵 \(RK=0\)、实际秩和 Frobenius 下降。优化没有取消这些代数验证。

## 2. 已实际执行的整条 AddFlip 比较

以 `ORD_j01` 的真实已存三位倍乘前缀为输入，分别使用原来的 NumPy 消元与新的整数消元完成同一条 AddFlip。该输入保存在 `p41_native_r2_comparison_input47.json.gz`，哈希为

`cc031404cafdfd15efa43b7b2cfc471c34952b416a7dd43ca9947200c4aadda8`。

以下各项均实际逐项相同：

- 199×73 的完整输出点坐标；
- 73×73 的完整 Frobenius 矩阵；
- 完整的 operation witness，包括实际秩、选取次数与输出点哈希；
- 结束时的随机数状态。

输出点哈希均为

`aa7c12369eed6f7fda444832641a00356ad615f28e1d9527d37c168c95dc0681`。

同次比较中，原实现耗时约 5.281 秒，新实现约 0.691 秒。数值仅为该次执行的性能观察，代数正确性来自上节的精确整数算法与全矩阵核验，不依赖某个速度承诺。可复现程序为 `p41_native_r2_comparison47.py`：

```sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python p41_native_r2_comparison47.py \
  --script-dir . \
  --input data/p41_native_r2_comparison_input47.json.gz \
  --build-dir /path/to/work/native-build \
  --output /path/to/work/native_r2_benchmark47.json
```

## 3. 全部 19 个普通中心的共同真实除子

R231 提供 19 个真正的 \(\mathbf Q_{47}\) 中心及其 73 坐标。令 \(L\) 是既有 Makdisi 嵌入线丛，\(\deg L=126\)，\(b=P_{-3}\)。在 \(H^0(L-b)\) 中寻找一个 Frobenius 不变截面 \(f_b\)，要求：

- 它在 \(b\) 的一阶导数为单位，故 \(b\) 是单零点；
- 它在全部 19 个普通中心为单位；
- 它在模型的全部 820 个评估点为单位。

实际第二次选择即满足全部条件。令

\[
 D_b=\operatorname{div}(f_b)-b,\qquad \deg D_b=125.
\]

脚本用实际截面 \(h\in H^0(L-b)\) 的约束

\[
 (h/f_b)s\in H^0(2L)
\]

计算共同 colon。清分母后的关系是 \(3L\) 截面恒等式，其在完整评估模型上的检查是忠实的。实际一个测试截面即给秩 125 的约束，核维数 74，并检查所有完整约束为零。另一方面，

\[
 h^0(2L-D_b)=252-125-54+1=74,
\]

因为该线丛次数 127 大于 \(2g-2=106\)。包含关系和相等的维数遂证明算出的正是完整 \(H^0(2L-D_b)\)，不是仅有正确大小的任意子空间。

对每个实际中心 \(P\)，进一步施加 \(s(P)=0\)。该限制在模 47 为单位秩 1，所以得到真实的 73 维空间

\[
 H^0(2L-E_P),\qquad E_P=D_b+P.
\]

所有 19 个点均完成全矩阵核验证、实际单位秩检查和 Frobenius 下降。由于

\[
 E_P-\operatorname{div}(f_0)
 =P-b+\operatorname{div}(f_b/f_0),
\]

其 Makdisi 类就是 \(C(P)=P-b\)，并且保留了初始主函数 \(f_b/f_0\) 的实际截面坐标，供需要具体纤维规范的后续局部高度算法使用。

`p41_all19_based_points47.json.gz` 保存共同 199×74 colon、全部 19 个 199×73 点坐标、Frobenius 矩阵、\(f_b\) 的 73 个截面系数、在 \(b\) 的导数和在全部普通中心的实际值。

## 4. 正在执行的 16 盘倍乘接口

`p41_ordinary_Abel_multiply47.py` 沿用 R121 的真实群阶

\[
 m=\#J(\mathbf F_{47})
 =21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072.
\]

每个盘的点从 \(C(P)\) 与实际 \(-C(P)\) 出发，按 304 位整数的准确前缀执行 454 条 AddFlip。每完成一位就以原子替换写入独立 checkpoint，保存符号、完整整数前缀、点坐标、Frobenius、输入哈希和随机数状态。恢复时逐项核对这些数据，继续未完成前缀。

只有完整倍乘结束并通过原始完整模 47 零点检验后，执行真正的正式对数提取。对 \(Y=\epsilon mC\) 的代表无关正式坐标 \(F\)，使用

\[
 \log C=\frac{\epsilon}{m}\,
 dF^{-1}\frac{2F(Y)-6F(-Y)+F(-2Y)}6\pmod{47^4}.
\]

这个组合消去二次、三次项；\(Y\in J_1\)，故四次及更高项模 \(47^4\) 消失。\(dF^{-1}\) 使用 R121 已经实际校准的 54 维规范微分变换，随后再使用 R230 的单位 Lie/cyclic 变换取回 \(C=aB\) 的 54 个坐标。程序要求全部坐标满足 Frobenius 关系，转成 cyclic 后虚部为零，并检查再变回 Lie 坐标完全一致。

每盘得到完整对数后才输出 `complete_actual_center_Abel_constant=true`。正在进行的乘法文件保留“未完成/尚未提取”状态，不把前缀或预计耗时登记为已完成结论。

执行示例：

```sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python p41_ordinary_Abel_multiply47.py \
  --script-dir . \
  --ordinary-atlas data/p41_ordinary_rational_atlas47.json.gz \
  --based-points data/p41_all19_based_points47.json.gz \
  --workdir /path/to/work/ordinary-abel \
  --tiny data/p41_all129_tiny_Abel47_complete.json.gz \
  --disk ORD_j01 --disk ORD_j05
```

完整 16 盘作业已实际启动并逐前缀落盘；本条的最终完成标志仅覆盖精确原生消元、实际整条 AddFlip 比较，以及全部 19 个真实初始基点差。后续完整 Abel 常数将另行登记。

## 5. 封存文件

所有准确文件哈希、大小与输入边界见 `R241-handoff-manifest.json`。关键哈希为：

| 文件 | SHA256 |
|---|---|
| `p41_native_r2_linear47.py` | `18a25842e7db48f533b7d8d3304338ba404d9777319e8485dc2dd91a928ed7d8` |
| `p41_r2_mod47_native.cpp` | `14d1cb3b9b286ac6e7c41668d20328428c6f1790443889d7fba431e63ba88b49` |
| `p41_ordinary_Abel_multiply47.py` | `cd424e39bfa3386c6de74bf7320f2ffce1d37dd121e74d82fd730a30827d6545` |
| `p41_all19_based_points47.json.gz` | `19f90754a0f83c163f8cbab8ba15fd2fb745bd819f8ea7bc3d4962d164c7e9a4` |

本条仍是固定素数 \(p=41\) 的实际计算进展，不改变主题 README 的主要完成标准。
