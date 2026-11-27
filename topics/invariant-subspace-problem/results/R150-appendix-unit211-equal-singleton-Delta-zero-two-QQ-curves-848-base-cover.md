# R150 unit211：整个 h=k、Delta=0 的两条原 QQ 曲线与至多848个基点

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro）。

## 1. 原范围及严格结论

在当前 h=k、Delta=0 的完整原物理图上，不同的原基点 (lambda,u) 至多 **848** 个。所有 Q 首项为零、u 首项为零及原曲线交点都包括在内。

这是投影基点的有限性；尚未返回同一基点上的完整原 Q、自由 Gram 和个别谱条件，不能写成完整原点排空。本篇不把多变量 gcd=1 当作没有共同零点。

输入来自[整个h=k的紧凑原五行和三列](R150-appendix-unit211-equal-singleton-global-compact-original-three-column-cofactors.md)。不倒置 Delta 或新增几何首项，不调用旧 D非零值图的结论。

## 2. 原 Delta零相容的固定 Q 投影

原 P1 已由真实单位 Pf 解出，原 NV 的完整身份为

$$
 P_fE_{NV}=T_n-bc\Delta z,\qquad z=Qt.
$$

故本图上的每个原点必满足 Delta=Tn=0。将两式的已付分母清除并只剥原单位，得到 Q 次数恰为2、2的原必要多项式 D2、N2：

| 原式 | 次数 (lambda,u,Q) | 项数 |
|---|---|---:|
| D2 | (12,4,2) | 98 |
| N2 | (19,5,2) | 180 |

N2 实际移除的非恒定原因子来源只有 Q 与 S，完整商乘回。原有理 Delta 的 Q² 系数另外准确核出

$$
 [Q^2]\Delta=2(\ell-1)(\lambda^2+\lambda-1).
$$

这里没有把此首项设为单位；整个零面仍由固定2、2次数的4阶 Sylvester 矩阵覆盖。

完整 QQ 返回

$$
 P_{\rm raw}(\lambda,u)=\operatorname{Res}_Q(D_2,N_2).
$$

其双次数为 (55,10)、503项。只剥与 Q 无关且此前已付的 A、B、u、u−1、S 因子后，得到必要曲线

$$
 P(\lambda,u)=0,\qquad \deg_{\lambda,u}P=(28,3).
$$

全 QQ 因式分解及乘积均实际返回：一个lambda一次因子、一个lambda二次因子、一个双次数 (25,3) 因子，各重数1，非零常数比例1/663552。三个因子及全部交点都保留；完整小系数载荷在回执。

## 3. 原全部均值的第二条固定 Q 投影

前篇原 (R,W,O) 三行给全 Delta 同点必要多项式 C，次数 (62,17,9)。本次只再生 C 作为精确输入，核冻结摘要；不重放旧三列 cofactor 证书或大哈希门。

用固定 Q 次数2、9的11阶原 Sylvester 矩阵计算

$$
 M_{\rm raw}(\lambda,u)=\operatorname{Res}_Q(D_2,C).
$$

完整 QQ 返回双次数 (218,40)、7522项。只去 Q 无关且已付的 A、B、lambda、u、u−1、S 因子，得到

$$
 M(\lambda,u)=0,\qquad \deg_{\lambda,u}M=(124,17).
$$

其全 QQ 因子为双次数 (116,17) 因子的一次与lambda四次因子的二次，完整乘积实际返回。没有删除这个四次因子的任何lambda纤维。

两个必要曲线的规范摘要为

- P：8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c；
- M：9be04b29c603db94642b6f3df66647427601e79714a1a989a80ba066a7e1cb82。

## 4. 为什么给出完整848基点界

实际精确 QQ 计算得到

$$
 \gcd_{\mathbb Q[\lambda,u]}(P,M)=1.
$$

因此二者在代数闭包没有共同曲线分量。特别不可能在某个 lambda0 上同时恒为关于 u 的零多项式；否则其共同垂直线会给公共因子。

按原固定 u 次数3、17定义20阶 Sylvester 矩阵，其行列式

$$
 R(\lambda)=\operatorname{Res}_u(P,M)
$$

非零。每个属于 P 的17行的lambda次数至多28，每个属于 M 的3行至多124，故

$$
 \deg_\lambda R\le17\cdot28+3\cdot124=848.
$$

不需要为这个上界重新展开大 QQ 结式。

还须按不同 u 根计数，而非只数lambda。固定lambda0处若有 r 个不同公共有限 u 根，它们在固定20列中给 r 个独立评价列 (1,u,...,u^19)^t。因至少一个专化多项式非零，其次数至多17，故 r≤17，Vandermonde独立性适用。于是原矩阵在lambda0处核维数至少r，行列式在那里消失阶至少r。后者也可由常数可逆行列变换将至少r行的常数项置零、再逐行提取lambda−lambda0直接得到。

对所有lambda0求和，得

$$
 \#\{(\lambda,u):P=M=0\}
 \le \sum_{\lambda_0}\operatorname{ord}_{\lambda_0}R
 \le848.
$$

任何原解均投到这个集合中。P的u首项退化、P整条lambda纤维为零或M首项退化都已包括，不使用一般点假设。这同时解释了“QQ互素”在本稿中的正确作用：支付有限基点及非零原投影，绝不是直接排空公共零点。

## 5. 实际执行与下一原输入

[新整个Delta零固定Q投影源](../notes/2026-11-27-unit211-equal-singleton-Delta-zero-compact-original-QQ-projections-8542.py)：

- blob5653204b92d52007d121e2c99eb24f733eecd062，7202字节；
- SHA256 a0e1efb16ec1939e50befbf4844e6cecb1603e17defcfa1b0fa1ae8fcd0abd0b；
- 实际run46025096446 / job140594347573；
- 源1.359859096秒，驱动1.413385340秒，峰值75212KiB，内层0；
- stdout10398字节，SHA256 bc1b16f8270636f7221c4de44ab88916e0fcd21a8d357d8deb05a7bfb9602061；
- 实际pull为2026-11-27 15:27:54.023597 UTC，提交8a15c7fb3e2bc6c4df46b5e7682b05af0954a25a，两README无差异；
- Python3.12.14、python-flint0.9.0，单线程180秒/4GiB。

[完整原返回和小因子载荷](../notes/2026-11-27-unit211-equal-singleton-Delta-zero-two-QQ-curves-848-base-cover-receipt-8542.json)。

接下来计算真正的一元 QQ lambda覆盖，并以独立原 N1 cofactor 的固定投影作真实整性/Gauss 返回；仍保全部原 Q 和自由 Gram 纤维，不以本页848上界作为终点。
