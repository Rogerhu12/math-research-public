# R150：碰撞图整个 u=2 的四原 Q 纤维排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 结论与准确范围

在当前原 $h_U=k_U$、$\Delta\ne0$ 碰撞图，整个
$$
\boxed{u=2}
$$
原纤维为空。因此此图现在可以使用 $u-2$ 为单位。

结论由四条同点原值多项式直接返回，包含全部复 $\lambda,Q$、全部实际 Q 首项下降以及由原两线唯一恢复的 $f,z$。没有从紧化边界、某个模素数或一般点得出排除。一般 $u$ 的碰撞纤维和完整个别 N/P 条件继续开放；既有五坐标有限界 235170 没有被本篇冒称为零。

原输入与坐标来自[四条完整同点原式](R150-appendix-unit211-equal-singleton-Delta-nonzero-four-complete-original-polynomials.md)。既有[整 Q 首项排除与有限五坐标环境](R150-appendix-unit211-collision-complete-Q-head-exclusion-and-finite-original-five-coordinates.md)和[两 E 原 u 首项整纤维排除](R150-appendix-unit211-collision-E-entire-u-heads-finite-free-exclusion.md)保持原范围；本次不重算这两项。

## 2. u=2 时准确的原非零物理乘积

记
$$
A=2\lambda^2-2\lambda+1,\qquad
B=4\lambda^3-6\lambda^2+3\lambda-1,\qquad
X=A^3,\quad Y=B^2.
$$
同一原图有 $\ell=X/Y$、$\xi=B/A$。置
$$
\eta_*=B+(3-2\lambda)A,\qquad
S_*=2B+(3-2\lambda)A.
$$
于是 $S=S_*/A$。在 $u=2$，以下为原量的清分母分子：
$$
T_*=-4Y-XQ,\qquad
J_*=-4Y+(X-Y)Q,
$$
$$
\Phi_*=Q(Y-X),\qquad P_{f,*}=T_*J_*,
$$
$$
N_{F,*}=(3-4\lambda)QYA^2+(-4Y+XQ)B\eta_*,
$$
$$
\Delta_*=\Phi_*N_{F,*}-BS_*P_{f,*}.
\tag{2.1}
$$
准确分母身份为
$$
T_0=T_*/Y,\quad J-Q=J_*/Y,\quad
\Phi=\Phi_*/Y,\quad P_f=P_{f,*}/Y^2,
$$
$$
N_F=N_{F,*}/(YA^2),\qquad
\Delta=\Delta_*/(Y^2A^2).
\tag{2.2}
$$
另置
$$
M_*=4XY-X^2Q-4Y^2,\qquad
P_{02,*}=2Q(2X-Y).
$$
原 $M=2\ell u-\ell^2Q-u^2$、$P_{02}$ 满足
$$
M=M_*/Y^2,\qquad
bc=M/[4(1-Q)],\qquad
P_{02}=P_{02,*}/Y.
\tag{2.3}
$$
最后沿用已排除整零纤维的
$$
J_2=3\lambda^2-2\lambda+1,\quad
G_2=\lambda^2+\lambda-1,\quad
C_4=8\lambda^4-24\lambda^3+24\lambda^2-12\lambda+3.
$$

本次固定的物理多项式是
$$
\mathcal P=
\Delta_*Q(1-Q)M_*P_{02,*}\Phi_*P_{f,*}
\lambda AB S_*J_2G_2C_4(2Y-X).
\tag{2.4}
$$
它在当前原图的每一点严格非零。各因子分别是原已付 $\Delta,Q,1-Q,bc,P_{02},\Phi,P_f,\lambda,A,B,S,J_2,G_2,C_4,u-\ell$ 的分子，所有相应分母仅用已付 $A,B$。这里的 $\Phi,P_f$ 已在四原式的同一点来源中支付，并非把其它物理 $D\ne0$ 图的结论搬入碰撞图。

$\mathcal P$ 的 $(\lambda,Q)$ 次数为 $(75,9)$，503 项。它的 Q 系数内容
$$
c_{\rm phys}(\lambda)=
\operatorname{monic}\gcd_j[Q^j]\mathcal P
\tag{2.5}
$$
次数为 39。因为它整除 $\mathcal P$，其在任何允许原点的 $\lambda$ 处也非零。

## 3. 只作合法原饱和

令 $C_R,C_W,C_O,C_{N1}$ 为原四个核心，直接代 $u=2$。每行只反复除去与 (2.4) 的完整多项式 gcd；每次实际核回商乘因子等于此前原行，并核因子整除 $\mathcal P$。剥完后作非零有理常数规范化，得到 $\widetilde C_i$。

| 原行 | 代 u=2 后次数 $(\lambda,Q)$ | 允许饱和后的次数 | 非常数 gcd 除法次数 |
|---|---:|---:|---:|
| R | $(46,5)$ | $(45,5)$ | 1 |
| W | $(45,6)$ | $(45,6)$ | 0 |
| O | $(51,6)$ | $(51,6)$ | 0 |
| N1 | $(48,6)$ | $(47,5)$ | 1 |

在 $\mathcal P\ne0$ 上，$C_i=0$ 与 $\widetilde C_i=0$ 等价。没有除去一个新首项、一个未付权多项式或一个只在一般点非零的因子。全部四条规范行及原乘积已经实际返回。

## 4. 完整原 Q 投影与唯一整 23 次域

对四行的六个固定配对分别计算真正的 Q 多项式结式。任一同点共同 Q 根都使其为零；固定次数的 Sylvester 恒等式保持每个 $\lambda$ 首项下降纤维。

| 配对 | 固定 Q 次数 | 原结式 $\lambda$ 次数 | 累计必要覆盖次数 |
|---|---:|---:|---:|
| R,W | $5,6$ | 485 | 260 |
| R,O | $5,6$ | 515 | 92 |
| R,N1 | $5,5$ | 450 | 92 |
| W,O | $6,6$ | 560 | 92 |
| W,N1 | $6,5$ | 490 | 92 |
| O,N1 | $6,5$ | 522 | 92 |

累计覆盖取已返回的非零原结式 gcd，并只反复剥其与 (2.5) 的公因子。各除法都完整乘回。最后首一 92 次多项式的平方自由部分是一个完整 QQ 不可约的 23 次多项式，记为
$$
F_{23}(\lambda).
\tag{4.1}
$$
等价地，最后首一覆盖为 $F_{23}^4$。这给 (4.1) 的紧凑、无歧义定义，不保存其可重算系数。实际平方自由除法及 QQ 分解的所有乘积均返回。

$F_{23}$ 的规范有理系数定义为 308 字节，SHA256：
4796bc316b5efb75f8c0590d7b4968032a9da4d6f8d33bd29727efe92da4e99c。

每个允许原点必须落在整个
$$
K=\mathbb Q[\lambda]/(F_{23})
$$
上。以下同时覆盖它的全部复嵌入，没有数值选根。

## 5. 原 Q 公因式与物理乘积平方为零

在 $K[Q]$ 中，四条 $\widetilde C_i$ 的实际 Q 次数依次为 $5,6,6,5$。使用完整扩展 Euclid，逐行返回同一个原组合
$$
g(Q)=
a_R(Q)\widetilde C_R+
a_W(Q)\widetilde C_W+
a_O(Q)\widetilde C_O+
a_{N1}(Q)\widetilde C_{N1}.
\tag{5.1}
$$
每一步都核回全部组合；常数域中每个实际逆都由 QQ 多项式 Bézout 返回并乘回。四次累计 gcd 次数分别为 $5,2,2,2$。最终 $g$ 是首一二次，且确实是四个原多项式的共同 gcd。

直接在同一商 $K[Q]/(g)$ 中约化 (2.4)，实际得到
$$
\boxed{\mathcal P^2=0\pmod g.}
\tag{5.2}
$$
源码先完整核回 $\mathcal P$ 除以 $g$ 的商与余式，再将余式平方逐步除以同一个 $g$，核每个乘积与最终零余式。共完成 9 个非平凡整域逆和 13 次 Q 多项式除法。

每个四原式共同点由 (5.1) 满足 $g(Q)=0$，再由 (5.2) 得 $\mathcal P=0$，与 (2.4) 的原非零条件矛盾。因此 (4.1) 的全部 $\lambda$ 及全部原 Q 纤维排空。这里保留二次商的幂零结构；无需假定它约化，也无需把 gcd 强行变成常数一。

完整原组合、二次 gcd、物理余式及幂次的规范证书为 91547 字节，SHA256：
7846aadad741f7ed2a54e1161f918c98cd4a14e0ad9c5ef4eba87fbed68dd884。
证书仅在运行中构造和乘回，不另存系数载荷。

## 6. 唯一实际执行

源：[2026-11-28-unit211-collision-u2-four-original-Q-full-fibres-8542.py](../notes/2026-11-28-unit211-collision-u2-four-original-Q-full-fibres-8542.py)。

- Git blob：8dfda3ad290c99253130f33fc2fd2f9cd4d7e697。
- 源 SHA256：3e52b76560070f677914e87c84692f94d67b79621fff3bffea11ba58674aa37a。
- [run 46065699605](https://github.com/Rogerhu12/math-research-public/actions/runs/46065699605)，job 140730374090。
- 固定源提交：0058b14e7cc10fd1b9d8547d6f0000678c0f6eed。
- 驱动实测：0.892456749 秒，峰值 46424 KiB，exit 0；数学终标 0.826033513 秒。
- stdout：9008 字节，SHA256 8ed70a59dde18eb6dd619c595dcd75d0c9218922c4b1f1f60610916e04ebcafb。
- 限额始终为 180 秒、4 GiB；没有模素数、提升或数值抽样。

真实 pull 于 2026-11-27T20:45:03.446838+00:00 完成，前后均为固定源提交。根 README 和课题 README 未变，blob 分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、5fbd905291dd044c88d35bd9c07ac0e586ff795a。

[小回执](../notes/2026-11-28-unit211-collision-u2-entire-original-exclusion-execution-8542.json)保实际步骤、源身份和资源记录。历史四原多项式仅在终端临时读取；本次输出与仓库只保源、紧凑参数定义、run、SHA 及小回执。

整条仿射 u=2 的排除不删除既有紧化边界上的 u=2 无穷点，也不把两个 E 的双无穷角判空。下一接口仍是一般 u 的同点四原 Q 与个别 N/P 条件。
