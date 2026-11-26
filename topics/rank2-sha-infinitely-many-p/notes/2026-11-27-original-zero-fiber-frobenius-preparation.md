# 原完整零纤维 Frobenius 的生产适配准备

2026-11-27 / `Astra-rank2-Sha-0b097461-20261127`。

**状态：源码已准备，只做本地 AST/字节摘要检查；未运行数学，未接正在运行的 v8，未启动另一份重作业。** 这是把既有原零纤维算法接到实际生产调用点的准备，不登记为新的几何 PASS 或新的数学定理。

## 1. 当前实际调用点

唯一原几何 v8 是 run `45882239615` / job `140124138541`，source
`3b0fe32226b1f91ec37ef68a8d53ff865e9d9b26`。原七式的完整 maps、
`v=ys²−1` 的 degree612 和首 cusp 商长/HNF 已返回。
最后实际看到的 Frobenius 进度为 2026-11-26 20:29:58 UTC 的121/306；
后续收到同一旧日志快照时不重标为新进度。21:51 UTC jobs API 仍为 in_progress。

`original_ys_closed_point_tools.py` 的默认 `certify_frobenius` 为每个完整残余基向量
构造一个原全局乘法矩阵，再专门化并作全部 p−1 次乘法。
同一文件已经具有 `prime_specialization_source` 分支，其接受门并未删除任何原乘积：
它逐一核对46971个对称基乘积的两个次序、全部单位乘积、原坐标和原常数域。
旧 `produce-original-ys-closed-local-check.py` 已有完整来源构造
`exact_zero_prime_specialization`；该旧入口没有取得全部 PASS，其运行状态不作为本适配的前提。

## 2. 来源选择是原表的准确专门化

原 complete affine context 给全部306个基元、权重 $w_i$ 以及每个实际乘积

$$
b_i b_j=\sum_{k,e}c_{ij;k,e}\xi^e b_k,
\qquad c_{ij;k,e}\in\mathbf F_r.
$$

所有项、全部原零界及两张完整图已经是同一 context 的组成部分。
有限图在 $\xi=0$ 时准确选择 $e=0$。
无穷图取 $s=1/\xi$、$b_k^\infty=s^{w_k}b_k$，从而

$$
b_i^\infty b_j^\infty
 =\sum_{k,e}c_{ij;k,e}s^{w_i+w_j-w_k-e}b_k^\infty.
$$

在 $s=0$ 时准确选择 $e=w_i+w_j-w_k$。不存在对应 recipe 时该系数为零；
代码使用明确附加的零列，而非省去某个基向量。
每一原对称来源行同时放入 $M_i$ 的第 $j$ 行和 $M_j$ 的第 $i$ 行。
全部表行的占用与原位置索引逐行相同，46971个来源行全部消费。

因此所得306个素域矩阵是原零纤维的完整乘法表；没有另构函数域、另做平面正规化、
挑选约化子代数，或预先假设闭点分裂。

## 3. 只在原完整零纤维上选择既有分支

新 helper `scripts/original_zero_fiber_frobenius.py` 的工厂
`make_original_zero_fiber_residual_class(affine)` 接受本次运行刚重建的原 context，
返回一个 residual class 和完整运行报告函数。工厂本身不改任何模块绑定。

只有同时满足以下既有结构条件时才选择素域分支：

- 原素因子恰为当前图的坐标 `R.gen()`，而非只具相同次数的另一因子；
- 残余维数恰为原306，完整自由基仍为0到305，原理想模该素因子的关系像为零；
- 相对底扩张次数为一，实际常数域绝对次数为一或二；
- 本次 chart 与来源 context 的原完整乘法签名相同。

随后仍调用**未修改的**基类 `certify_frobenius`。
它重新读原 complete affine tables，核对全部46971个乘积的两个次序和全部单位行，
在素域计算全部306个 $p$ 次幂，再沿实际常数域嵌入运输。
后续仍为原半线性 Frobenius 合成、完整 nilradical/约化投影、所有闭点的原始坐标运输、
全部厚理想与厚 Norm。使用的投影仍是原像上的逆构造，不把 $F_q^2$ 自称为幂等投影。

任何其它纤维准确回到基类的原完整路径。
同一图的素域表可在同次运行复用；报告只在该纤维实际完成后记录成功回执。
这里不读取历史生成矩阵或旧数学结果文件。

## 4. 固定源码及启用条件

| 源码 | 字节数 | SHA256 |
|---|---:|---|
| `original_zero_fiber_frobenius.py` | 8202 | `2a505fa616c639947063cd5c3e69a55856daa379b6c6ffd784af069e3c23287d` |
| `original_ys_closed_point_tools.py` | 47931 | `7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb` |
| 旧构造所在 `produce-original-ys-closed-local-check.py` | 18748 | `bff04b4d8c421a035d8798541b58521c536921a363873b9c78946557b727932f` |

新工厂 pin 住完整基类源码；本次提交不改变生产入口、request 或 workflow。
当前 v8 的原源和所有接受门因此保持。
若其实际终点表明需要这个后继，须在下一唯一生产入口中显式绑定返回的 class，
把 helper 列入完整源 manifest，并保留原参数、全部厚度、两张图、四交和18×9 shadow。
届时消费的是新运行自己的全部回执；本篇没有预先宣称速度改善或原几何成功。


## 5. 当前原 v8 已越过该阶段，保持运行

2026-11-26 22:02 UTC 取得并亲读新的原 job 日志快照：6305095字节，
SHA256 `d8cfb9092465de0c83eb97fba5f0cef98ba486c4d99f8fb24d63febf7bc4e2e1`。
这是同一个 run/job/source，不是另发作业。

- 20:56:17 UTC：原306/306个 Frobenius 基行完成。
- 21:03:09 UTC：首个 `all original cusps:positive` 商的4成分中，第一成分完整认证，闭点度1、重数2、全长2。
- 21:10:29 UTC：第二成分完整认证，闭点度8、重数2、全长16。原 R974 的实际常数嵌入/原生残余域因而已在这枚真实 degree8 闭点通过；它仍不等于全部原几何终点。
- 21:14:16 UTC：第三成分完整认证，闭点度1、重数578、全长578。
- 21:20:54 UTC：第四成分（内部 `factor 3`）完整局部原像的 Hermite 为71/306，determinant degree16。

四交、全部 thick Norm/Tate迹和18×9 shadow尚无终点回执。
本篇 helper继续保持备用；不因曾经的 Frobenius 慢点而重启已越过该阶段的原运行。
