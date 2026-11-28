# 正确 h=k 的 ell=1/2：八原行、五个固定 Q 目标与完整六次 u 覆盖

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-28（UTC）。

**结果：首次实际完整返回，尚未排空整个 ell=1/2 支。** 在整二次常数域
$$
K=\mathbb Q[\lambda]/(3\lambda^2-2\lambda+1)
$$
上，八条同点原 Gram/值条件给五个固定 $Q$ 常数目标。只剥原已付权支持后，其完整 $K[u]$ gcd 是首一十二次 $g(u)$，并已完整回到八个原来源。正范数精确为
$$
{\rm Nm}_{K/\mathbb Q}g(u)=cF_6(u)^4,\qquad c\in\mathbb Q^\times,
\tag{1}
$$
其中 $F_6$ 是一个完整 QQ 不可约六次因子。因此所有本图物理解必须落在六个复 $u$ 值上；全部同 $Q$ 纤维、首项下降和原重数继续保留。

没有 $Q$ 有限性、整支空性或新的 $2\ell-1$ 单位付款。

## 1. 原范围与再生定义

本次只处理正确原 singleton 值碰撞 $h=k$、$\ell=1/2$、$\Delta\ne0$ 图。整个当前正确 $\Delta=0$ 已由独立终证关闭，可合并理解为当前 ell-half 的必要覆盖；不使用 W 或 Phi 的 distinct-singleton ell-half 排除，也不倒物理 $D$。

完整第一次输入：
[输入说明](../notes/2026-11-28-unit211-hk-entire-ell-half-constant-field-scaled-original-Q-cofactors-8542-input.md)。

准确自含再生源：
[scaled-original-Q-cofactors](../notes/2026-11-28-unit211-hk-entire-ell-half-constant-field-scaled-original-Q-cofactors-8542.py)，blob 53d57ae6baf7a9fdf3867a95952833a570317797，21885 B，SHA256
44b7c44c5e4ba5408a8662e6f2579be23c6bf9effd0d9d2a59993eb827ca79cb。

独立前置：
[正确整 Delta0 原排除](R150-appendix-unit211-hk-corrected-entire-Delta-zero-finite-DVR-original-exclusion.md)，以及
[Pf 真原来源审计](../notes/2026-11-28-unit211-h-equals-k-Pf-true-original-static-audit-8542.md)。
本次源自含，没有重跑前置源、两谱 DVR、旧固定 17 阶覆盖或旧 frozen Loww 门。

原值参数满足
$$
2A^3-B^2=(2\lambda-1)^2(3\lambda^2-2\lambda+1),
$$
其中 $A=2\lambda^2-2\lambda+1$、$B=4\lambda^3-6\lambda^2+3\lambda-1$。原 $2\lambda-1$ 已付，故整个 ell-half 落入上述二次域；判别式 $-8$，两嵌入均保。

实际源逐项返回
$$
\ell=\tfrac12,\quad \xi=1-\lambda,\quad
T=(1-\lambda)/2,\quad h=k=2-\lambda,\quad
w=\tfrac32(\lambda-1),
$$
$$
M=u-u^2-Q/4,\quad T_0=J-Q=2M,\quad P_f=4M^2,\quad
P_{02}=-2M(u-2).
\tag{2}
$$
因此 $u-2$ 由原 $M,P_{02}$ 自动支付。没有新 $\Phi$、$u-\ell$ 或消元头逆。

## 2. 统一原缩放与完整八行

使用完整原线
$$
P_ff+bc\,\Phi z+P_c=0,\qquad
N_Ff+bc\,S\xi z+N_C=0,\qquad z=Qt.
$$
定义
$$
\Delta=\Phi N_F-S\xi P_f,\quad
T_{\rm num}=P_fN_C-P_cN_F,\quad
F_{\rm num}=S\xi P_c-\Phi N_C.
$$
两 Cramer 身份均已逐项返回。令原单位
$$
H=M Q\Delta.
$$
整个真 dual Gram 的所有几何坐标统一乘 $H$ 后再构造原式，而非倒置 $\Delta$ 的范数。最初八行依次为
$$
E_1,\ E_{B,e},\ E_{B,o},\ N_1,\
N_{B,e},\ N_{B,o},\ P_{B,e},\ P_{B,o}.
\tag{3}
$$
前三行是 $H^2$ 倍原均值，后五行是 $H^3$ 倍原值条件。源还完整返回原 $E_0,N_0,P_{\rm jet}$、整个 $N_4(1,w,h,h)$，并核 C 行为相应原 B 行的共轭。头两坐标始终用
$(d^2)_1=2d_0d_1$，未承继错误 compact。

所有八行仅清原 $\delta=1-Q$ 分母，并精除已付
$$
u,\ u-1,\ u-2,\ Q,\delta,M,\Delta
$$
的完整因子。各原缩放都完整乘回。此次实际最后八行的 $\delta$ 分母指数均为零；只是实际简化结果，不是事前偷加条件。

实际保留行的次数如下。总次与双次只计 $(u,Q)$，常数域基是 $1,\lambda$。

| 原行 | $(\deg_u,\deg_Q)$ | 总次 | 项数 |
|---|---:|---:|---:|
| $E_1$ | $(8,3)$ | 8 | 45 |
| $E_{B,e}$ | $(9,4)$ | 9 | 61 |
| $E_{B,o}$ | $(9,4)$ | 9 | 53 |
| $N_1$ | $(9,4)$ | 9 | 53 |
| $N_{B,e}$ | $(15,7)$ | 15 | 131 |
| $N_{B,o}$ | $(14,6)$ | 14 | 113 |
| $P_{B,e}$ | $(15,7)$ | 15 | 131 |
| $P_{B,o}$ | $(14,6)$ | 14 | 113 |

所有八行与原 $H$ 缩放在数学 0.171340443 秒时已全部返回。

## 3. 固定 Q 常数目标跨全部头零

对于每一固定原行对 $F,G$，源取整个 $K[u]$ 上的 $Q$ 次数 $m,n$，以
$$
F,QF,\ldots,Q^{n-1}F,\quad
G,QG,\ldots,Q^{m-1}G
$$
构造固定 $m+n$ 阶 Sylvester 行矩阵。分数自由前消元及精确回代，每个整除乘回，最终返回所有列
$$
\mu S=C(u)e_0^{\,t}
$$
及完整二元原式
$$
\mu_F(Q)F+\mu_G(Q)G=C(u).
\tag{4}
$$
所以临时主元零面、原 $Q$ 首项下降面全部保留。没有只凭函数域 determinant 的非零性排空纤维。

五个事前固定目标均实际完成：

| 原行对 | 固定容量 | 阶数 | 原 $u$ 次数 | 仅剥原 $u,u-1$ | 保留次数 | 累积 gcd 次数 |
|---|---:|---:|---:|---:|---:|---:|
| $E_1,E_{B,e}$ | $(3,4)$ | 7 | 38 | $u^3(u-1)^6$ | 29 | 29 |
| $E_1,E_{B,o}$ | $(3,4)$ | 7 | 35 | $u^3(u-1)^6$ | 26 | 12 |
| $E_1,N_1$ | $(3,4)$ | 7 | 35 | $u^3(u-1)^8$ | 24 | 12 |
| $E_{B,e},N_{B,o}$ | $(4,6)$ | 10 | 68 | $u^8(u-1)^9$ | 51 | 12 |
| $E_{B,o},P_{B,o}$ | $(4,6)$ | 10 | 62 | $u^7(u-1)^8$ | 47 | 12 |

各次数还可伴非零常数域倍数，不改变原单位范围。此次没有剥到 $u-2$；它虽合法已付，实际记录仍如表所示。

整个 $K[u]$ 的除法和 Bézout 均实际乘回；没有把两个 $\lambda$ 嵌入分开选根。

## 4. 十二次原 gcd 与六次 QQ 支持

最终首一 $g(u)\in K[u]$ 的准确再生定义是第 3 节五个规范原常数目标的完整首一 gcd。其 canonical 两坐标编码为：

- $u$ 次数 12；
- 两个 $\lambda$ 基坐标合计 25 项；
- canonical 字节数 688；
- SHA256：3714806312a65901fa4cee34d459124cc7ef1cf4d5c10d72faee853fd7f375e7。

源随后清除实际 scalar 与八行缩放中记录的旧权因子，用其最大指数共同倍数 $E,R$，并真正返回
$$
\sum_{i=1}^{8}\Omega_i H^{d_i}\mathcal E_i=R E\,g(u),
\qquad d_i=2,2,2,3,3,3,3,3.
\tag{5}
$$
$R,E,H$ 都是原单位乘积；(5) 是完整八原来源，不是只有投影方程的无证来源陈述。实际返回时点为数学 6.021577552 秒。八乘子 profile 元数据共 1477 B，SHA256
bc72232d93a530e4a483251973f779d5e0d71d0543272f9bae55a83513a43b4e；
这只是 profile 元数据哈希，不冒充大系数证书载荷。

由 (5)，$g$ 属于当前局部化原理想。正乘其常数域共轭，得必要 QQ 范数
$$
N_{24}(u)=\overline{g(u)}g(u).
$$
此处只作正乘，没有范数逆。完整 QQ 因式乘回实际给 (1)。准确参数身份：

| 参数 | 次数／重数 | canonical 字节数 | SHA256 |
|---|---|---:|---|
| $N_{24}$ | 24 | 603 | 54d20463dcf1ba9e1dca6f4f36a4b2cc0a586722f4270067c256c891e814841e |
| $F_6$ | QQ 不可约次数 6，重数 4 | 54 | 0f8be1fab30e5fc1be7583839d9ce4161bbcd071fb7e4a4b750936713626ba7d |

$F_6$ 由固定源最后一次完整 QQ factor 的唯一六次因子定义；未猜系数、未用次数猜旧单位，也未另存可重算系数缓存。

$F_6^4$ 而非只 $F_6$ 已由原理想身份保留。集合意义下全部物理 $u$ 位于 $F_6=0$；但不能直接把一次 $F_6$ 宣为原理想元素。

在引入自由 $Q$ 或几何局部化之前，
$$
B_0=K[u]/(g)
$$
是秩 12 的自由 $K$ 环境，QQ 维数 24。这只是必要 $(\lambda,u)$ 基环境，绝不表示完整原图有长度 24。不同 $u$ 至多六个、连同两个谱根粗界至多十二个 $(\lambda,u)$ 对；完整 $Q$ 与原几何纤维仍待新返回。

没有执行 $g$ 在 $K[u]$ 内的平方自由分解；也没有证明它就是某个三次的四次幂。该更小常数域若后续采用，必须用新准确参数身份核定，而不能从范数形状猜测。

## 5. 唯一实际回执

[实际 job 日志](https://github.com/Rogerhu12/math-research-public/actions/runs/46154286626/job/141007395347)已亲自完整读取，包含 28 条数学记录和 driver receipt。

- run：46154286626；job：141007395347；第一次 attempt。
- 源提交：59bdc540c392b6985a042294bf68cfc18aa3dc3f。
- 真 pull 后：7c4de3d03ba5a1d59754aa5c8af6f24faf82d4a7。
- 真规则读取：2026-11-28 14:22:17.045618 UTC；两 README 无变化。
- driver：6.111232795 秒，44384 KiB，源 exit 0。
- 源最后数学时点：6.024191213 秒；源自身峰值 RSS 43792 KiB。
- stdout：16797 B，SHA256 d6ef60886ed03c5d4c1092d18dbfd213ff5dd6bcde55f50ee32424d1cde8bfe3。
- 253 次常数域逆乘回，923 次系数精除返回，996 次固定 Bareiss 乘积；
  5 个完整固定 cofactor、25 次一元除法/Bézout 返回；
  18 个原 Gram 与 8 个原矩检查；
  最终完整八源返回 1 次。

源最终准确记录 entireHalfWeightChartExcluded=false。计算本身完整成功，不是数学排空；所有未闭分支仍保留。

小回执：
[execution](../notes/2026-11-28-unit211-hk-entire-ell-half-constant-field-scaled-original-Q-cofactors-8542-execution.json)。
不保存矩阵、大系数、编码片或可重算缓存。

## 6. 后续边界

下一项可以在真正核定的整个常数代数上专门化原八行，做原 $Q$ gcd、按 $Q,\delta,M,\Delta$ 等旧单位去除完整不物理分量，或对真实 Cramer 基点作新的原返回。不得重算本次五个已成 cofactor 或以换序、换素数方式重放。

在新返回之前，整个 $F_6$ 原纤维仍开放；尤其不能把范数零面自动付款，也不能宣布整 $\ell=1/2$ 排空。独立全权首一 $t^3$ 纸证不改变本次实际十二次 gcd 与六次必要支持的身份或未闭范围。
