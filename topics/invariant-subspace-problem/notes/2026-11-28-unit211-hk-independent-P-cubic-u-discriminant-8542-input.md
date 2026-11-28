# 新输入：独立 Delta/Tnum 曲线 P 的 u 三次判别式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

**状态：首次执行前定义；尚不预报因式。** 只用独立正确的 $P(\lambda,u)$ 参数，构造此前未执行的 $u$ 三次判别式。它不是冻结 ad00 的整 K99 联合 u-gcd、同 Q 或八原 z 门的续跑；不重算 M、不重建 F99/F300，不重跑旧投影及旧因式门。

## 1. 唯一既有参数

$P$ 是原 $\Delta(Q),T_{\rm num}(Q)$ 的固定四阶 Q 结式，仅剥旧已付 Q-free 支持后的必要式。原结果：
- 双次数 $(\deg_\lambda,\deg_u)=(28,3)$，115 项；
- 规范 JSON 2496 字节，SHA256 8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c；
- 旧唯一 run46025096446/job140594347573 中名为 original_Delta_Tnum_compatibility 的独立分支。
- 原 $\Delta$ 没有剥多项式因子；$T_{\rm num}$ 只剥 Q/S 已付支持。原四阶结式只剥 A、B、u、u−1、S。
- 原同源中另一条 wrong-R 均值曲线永久隔离，不读取其参数、更不执行其源码。

现 main 小回执：[独立原执行记录](2026-11-27-unit211-equal-singleton-Delta-zero-two-QQ-curves-848-base-cover-receipt-8542.json)。其历史参数仅由 runner 临时读取 ac40c96b0cfb3758fbf8bd380d18ca288a23601f 同路径；只按上述 SHA 选择 P。执行结束不提交参数载荷。

## 2. 新计算及完整返回

由同一 P 精确收集
$$
P=a(\lambda)u^3+b(\lambda)u^2+c(\lambda)u+d(\lambda).
$$
程序先把四个系数重新拼回 P 的全部 115 项，再构造
$$
\operatorname{Disc}_u(P)
=18abcd-4b^3d+b^2c^2-4ac^3-27a^2d^2.
$$
随后做新判别式的完整 QQ 因式分解，全部因子带重数乘回原判别式。仅输出次数、字节数、SHA 和返回状态；不保存展开系数。

如果判别式非零且其所有不可约因子次数都小于 99，则它在既有两个不可约谱域 $K_{99},K_{300}$ 中均为单位，给每个域上的三次 P 可分。若这项次数条件不满足，保留实际所有因子，不宣称该域上可分。

这条新信息可与[约化权基](../results/R150-appendix-unit211-hk-Delta-zero-reduced-base-and-4788-coordinate-Artin-envelope.md)的唯一 u 结构结合，随后考察原固定四阶 Q 结式在该 u 点的一阶赋值。那项原 Q 纤维结论仍须完整纸面证明；本源不执行原 Q-gcd，不产生原八 z 的排空证书。

## 3. 原边界和预算

源自含数学定义，只依赖上述一个已成参数；初始绝对 60 秒、1 GiB，外驱动 75 秒。单线程 Python 3.12.14 / python-flint 0.9.0。实际失败按最后完整标记记录，不增限、续段或复跑。

[可读源码](2026-11-28-unit211-hk-independent-P-cubic-u-discriminant-8542.py)。全部原几何条件、两个谱域的未排空范围、Delta 非零支、独立 U0 尺度以及普通 Hilbert ISP 仍保留。
