# R150：剩余 h=k、Delta 非零的同点原四参数式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

在[整个碰撞 Delta 零分支已排空](R150-appendix-unit211-equal-singleton-entire-Delta-zero-exclusion.md)之后，本次直接恢复同一个原 f、z=Qt，并将四条紧凑原均值/N1 条件返回为完整 QQ[lambda,u,Q] 多项式。四个核心均已实际完整 QQ 分解并乘回；每个都是不可约多项式的非零有理倍数。

这给出余下整个碰撞图的原值输入，尚不排空它。所有 Q 首项和 lambda 首项的整零面保留，个别 N/P 原条件仍须保留。

## 1. 同一点的原两线恢复

沿用[紧凑原五行](R150-appendix-unit211-equal-singleton-global-compact-original-three-column-cofactors.md)及[原标量恒等式](R150-appendix-unit211-compact-original-scalar-means-and-N1-identities.md)的定义：
$$
P_ff+bc\Phi z+P_c=0,\qquad
N_Ff+bcS\xi z+N_C=0,
$$
$$
\Delta=\Phi N_F-S\xi P_f,\quad
T_{\rm num}=P_fN_C-P_cN_F,\quad
F_{\rm num}=S\xi P_c-\Phi N_C.
$$
原已经支付 Pf、bc、Phi；本次可用 Delta，理由正是整零面独立排空，不能用一般点代替那个证明。

准确恢复
$$
f=F_{\rm num}/\Delta,\qquad
z=T_{\rm num}/(bc\Delta).
$$
源将这两个同点表达式分别完整代回原 P1、NV 两线，均为零。没有给四个原条件分别选择不同的 f 或 z。

## 2. 从真实三列到四个参数多项式

保存的原三列行分别为
$$
R_i(z)=p_{i0}+p_{i1}z+p_{i2}z^2,\quad
i=R,W,O,N1.
$$
它们经此前已付单位和分母对应四个原紧凑式，其中 R/W/O 的同时为零准确恢复三个原均值。原 NV 行为 a0+a1 z，a1 是原单位乘 Delta，故现在非零。

令
$$
E_i=p_{i0}a_1^2-p_{i1}a_0a_1+p_{i2}a_0^2.
$$
源完整核回
$$
E_i=a_1^2R_i(-a_0/a_1).
$$
之后只剥原已付因子与非零有理常数，得到 C_i。所有剥除均有完整乘积；没有除去任何新几何首项。当前域上，四个 C_i 同时为零等价于所述原三均值和 N1 在恢复的同一点同时为零。此等价不把完整个别 N/P 条件省略。

实际返回为：

| 原来源 | 次数 (lambda,u,Q) | 项数 | 总次数 |
|---|---:|---:|---:|
| R | (49,12,5) | 2065 | 60 |
| W | (48,12,6) | 2070 | 60 |
| O | (54,13,6) | 2493 | 67 |
| N1 | (51,13,6) | 2349 | 64 |

四个规范核心 SHA256 依次为：

- 4c0130336d7f9973f9cc369e700dd6e7f67bd6adba0dd05565ff9081717fd2aa；
- 0d107cec119b63088f2cf7daa9d41459ddbf6063b426f23284b4eb5b9431f95c；
- 1eccf7ea51138b45126e31806be36f0416614ebdf52da7eef517f4cfd42406ae；
- 505f84f4ea421c06edc20853ed54a686a85b2103e354273cd319f949986be838。

全部原同点恢复、清分母和四个核心在 2.891 秒前返回；完整 QQ 分解在 3.069 秒前完成。四个核心各只有一个不可约因子，重数均为一。不可约并不意味着它在复参数域非零，也不意味着四式交点为空。

## 3. 原首项全部保留

Q 首项的次数 (lambda,u) 分别为
$$
(49,2),\quad(44,0),\quad(53,1),\quad(50,1).
$$
尤其 W 的 Q 六次首项只依赖 lambda，给出一个可以独立检验的整个 lambda 边界；本结果尚未把该首项作为原单位。

lambda 首项的次数 (u,Q) 分别为
$$
(8,5),\quad(12,5),\quad(13,5),\quad(13,5).
$$
全部首项原系数已返回，所有首项为零的纤维都仍是当前输入的一部分。后续可用固定原次数 Sylvester 投影保留次数下降；不能直接把多变量 gcd 为一解释为空集。

## 4. 唯一实际源、精确后续输入

源：
[2026-11-27-unit211-equal-singleton-Delta-nonzero-same-original-four-polynomials-8542.py](../notes/2026-11-27-unit211-equal-singleton-Delta-nonzero-same-original-four-polynomials-8542.py)。

- blob：1f391530ac96267f1a71ebf5ee1c4ae0ec002103。
- SHA256：6b21d1f741ce34bf9f7fb3b94a998777d079483b272884d7a6173cbab3a19a69。
- run/job：46035514551 / 140629816677。
- source commit：5ef6957e12f9e14f96cf58797eb98ed13ee07169。
- 内层：3.239153137 秒 / 57596 KiB / exit 0。
- stdout：292983 字节，SHA256 25264c67d1097fda1aa453fcb931e5cac77eb05853db2154c0ac2dc06aa680f3。

真实 pull 于 2026-11-27 16:40:11.422435 UTC 读到 ad53b75a50916bd96599d6962bc7e16b166cafbb，根与课题 README 未变。

后续直接使用四个完整原多项式的精确参数载荷，避免重放均值或旧 cofactor 门。压缩前载荷为 310329 字节，SHA256
11046373e5362f4b5606e2940483929954a74382e152e40f211fbe79ec42b292。
其 base64 压缩文本分为两个约 66KB 的参数片段，均有独立 SHA；源逐片、整体解压及全部系数重建后核验。它们是后续精确投影所需的原多项式输入，不包含行列式矩阵或大 Bézout 缓存。

新的固定原 Q 投影只读取上述输入，先完整分解各原 Q 首项，再对 (R,W)、(R,N1) 作固定 11 阶原 Sylvester 结式。完整头零纤维与投影交点均保留；其运行结果另行登记。普通 Hilbert ISP 未完成。
