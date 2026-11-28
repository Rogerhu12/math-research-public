# R150：W 整 b0 零支的原二次／六次与唯一 78 次必要权曲线

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 结论及未闭范围

在当前 W 的原互异两值、$D\ne0$ 图中，令
$$
b_0=2m\{A_*T+uQ\ell(3-2\lambda)\}.
$$
整个 $b_0=0$ 分支都被同一个非零多项式 $F_{78}(e,k)=0$ 覆盖。
此次实际完整 QQ 因式返回显示：
$$
\deg_eF_{78}=43,\qquad \deg_kF_{78}=53,\qquad
\deg F_{78}=78,
$$
且只有一个 QQ 不可约因子，重数 1。

这是整分支的新必要权曲线，**没有排除该曲线，也没有证明它只含有限权点**。
全部原均值和个别 N/P 仍须在同一点返回。
本结果不把 $b_0$ 或 $A_*$ 支付到 W 的互补图，更不外推到原值碰撞 $D=0$。

唯一首次实际执行为
[run46126392724](https://github.com/Rogerhu12/math-research-public/actions/runs/46126392724)，
job140921825207，内层 exit0，1.686397753 秒，48572 KiB。
未重放 native 六规则、此前 122 秒四次两列或旧参数结式。

## 2. 原权和同值定义

取当前已刊 W 原权
$$
u=e+1,\quad Q=ek,\quad \overline V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{k\overline V},
$$
$$
\delta=1-Q,\quad m=u-\ell,\quad
M=\ell(2u-\ell Q)-u^2=\ell^2\delta-m^2=4bc\delta,
$$
$$
J=2u(1-u)+\ell Q,\qquad
A_*=4uQ-J,\qquad C_*=A_*m^2+J\delta\ell^2.
$$
沿[同一点两个原四次](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)，记
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3,
$$
$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQ(3-2\lambda)\ell T+DC_*.
$$
原值条件给
$$
\mathcal C_4=2mD a_\Delta+KM b_0=0,\qquad
\mathcal R_6=MK^2-4m^2D^3=0.                       \tag{1}
$$
这些是同一个 $\lambda,T$ 的原必要方程，未分别选择根。

使用的既有权单位只在当前 W 原图有效。特别 $m$ 来自真正原等权排除，
$\ell$ 来自整 $\ell=0$ 排除，
$2\ell-1$ 来自
[整 Lhalf 原排除](R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)。
前一份仅有 F101 覆盖的定理不能替代这个完整排除来源。
当前源所列 J19、C9 等其他权支持仍仅按其已经发表的整 W 范围使用。

## 3. 整 b0 零面上的合法恢复

若在 $b_0=0$ 上又有 $A_*=0$，则
$$
uQ\ell(3-2\lambda)=0.
$$
当前 $uQ\ell$ 已付，所以 $\lambda=3/2$。
这已被
[整 W 的 $\lambda=3/2$ 原返回](R150-appendix-unit211-W-lambda-three-halves-complete-original-exclusion.md)
独立排除。因此只在这个完整 $b_0=0$ 分支，可以支付 $A_*$ 并唯一恢复
$$
\kappa=\frac{uQ\ell}{A_*},\qquad
T=-\kappa(3-2\lambda).                              \tag{2}
$$
这覆盖该支的全部原点，不是任取一个非零首项开图。

由 (1) 和当前原 $mD\ne0$，
$$
a_\Delta=0.                                        \tag{3}
$$
源确实只在此推论用到原 $D$ 非零，未把它当成系数域中可逆的范数。
设 $n=2\lambda-1$。直接代入 (2) 并完整乘回得到
$$
\frac{2a_\Delta}{\ell}
=2M\ell Q(1-2n)+C_*(n^2+1)
 -8uQ\delta\ell\kappa^2(n-2)^2.                    \tag{4}
$$
故 (3) 是真正的 $\lambda$ 二次；
(1) 中完整 $\mathcal R_6$ 是 $\lambda$ 六次。
源对 $b_0=0$、$\mathcal C_4=2mDa_\Delta$ 及 (4) 均直接返回。

只清已付权分母、剥已付纯权因子并作非零有理数归一后，
记这两条原输入为 $q_2,r_6$。
实际次数分别是 2、6；两者全部 $\lambda$ 首项零纤维保持在内。

| 原输入 | 清除已付支持后 $(\deg_e,\deg_k,\deg_\lambda)$ | 总次数 | 项数 | 定义 SHA256 |
|---|---:|---:|---:|---|
| $q_2$ | $(7,9,2)$ | 15 | 163 | 88bf8a85f29cbe0aa6c11c63d322e08f95777247596dc82858df9047c4d54ed8 |
| $r_6$ | $(13,15,6)$ | 29 | 1141 | 92840a3ef63d3a606929f43dd88e7eb5d02a5f27407ac6fe3dfddaec531e4421 |

对 $q_2$，实际剥除记录为 e 支持 1 层、u 支持 3 层；
对 $r_6$，为 u 支持 5 层、ell 支持 3 层。
这里“层”始终是与该标签原多项式反复取 gcd 后的精确除法次数，
不是声称整个标签因子以该整数为幂。
每次都有除法和最终乘积返回。

## 4. 固定八阶投影与全部首项零

在基 $(1,\lambda,\ldots,\lambda^7)$ 上使用固定八行
$$
q_2,\lambda q_2,\ldots,\lambda^5q_2,\quad
r_6,\lambda r_6.                                   \tag{5}
$$
若某权下存在有限共同 $\lambda$，其 Vandermonde 列非零，
(5) 的八行在该列上全部为零；故固定行列式
$$
R(e,k)=\det\operatorname{Sylv}_{2,6}(q_2,r_6)
$$
必为零。这个论证不要求二次或六次首项非零，也覆盖同时降次。
这里没有把按当点实际次数重算的较小结式替代固定八阶式。

首次 Bareiss 完成全部七步，共 140 次精确商乘回。
中间主元只为构造这个多项式行列式，不作为原参数单位；
每次精除恒等式及最终固定行列式保留所有主元零纤维。
实际
$$
(\deg_eR,\deg_kR,\deg R)=(64,84,124),
$$
4077 项。其定义序列 203451 字节，
SHA256 为
86511dda8479808aa3a17623606f490ef2e7c9b1057a9c784790385f4795c910。

然后只按已付支持反复剥除：
k 为 6 层、Vbar 为 1 层、M 为 2 层、ell 为 2 层、
本整分支才支付的 Astar 为 12 层。
源完整核回
$$
R=c\,U_{\rm paid}\,F_{78},\qquad c\in\mathbb Q^\times. \tag{6}
$$
因此每个当前 $b_0=0$ 原点都在 $F_{78}=0$ 上。

## 5. 完整 QQ 因式与准确保存方式

剩余归一多项式的完整 QQ 因式只有一个非恒定因子，重数 1，
且因子乘积实际回到原多项式。
两种有理数归一的参数定义如下：

| 对象 | 次数 $(e,k;\mathrm{total})$ | 项数 | 定义字节数 | SHA256 |
|---|---:|---:|---:|---|
| 剥除后的归一 $F_{78}$ | $(43,53;78)$ | 1697 | 66020 | cb5eaec8695f8bd013bc5023f6d083c070881799ce57362dac81df0e2844069f |
| QQ 因式器归一的同一不可约因子 | $(43,53;78)$ | 1697 | 63059 | 0ae3e9daca7eda26a7e7e1e33bb5f3457080f98e871f489fcd7dddf1f5295770 |

两行只差非零有理数归一，定义编码均为按指数排序的
$[[\mathrm{exponents},\mathrm{rational\ coefficient}],\ldots]$。
不保存或传送这些可重算系数；源中 (2)–(6) 是完整准确的再生定义。

只有一个 QQ 不可约权曲线并不证明原点不存在，
也不由此得到有限权集合。下一步需要对这条完整曲线使用更多同点原条件，
或与独立原权条件作真正的交集返回。
任何额外内容或首项均未在本篇支付。

## 6. 源、真实回执及更新状态

自含源：
[首次原二次／六次八阶源](../notes/2026-11-28-unit211-W-entire-b0-zero-original-quadratic-six-fixed-eight-8542.py)。

源 blob 7ea83a3e60ecb8a57b1e02470730e63ba56a1b89；
SHA256 a11fa3741692def8a90a04324378be92531c6e55569da596c59321e8b4116677。
[首次输入说明](../notes/2026-11-28-unit211-W-entire-b0-zero-original-quadratic-six-fixed-eight-8542-input.md)
保留派发前状态；本篇和
[实际小回执](../notes/2026-11-28-unit211-W-entire-b0-zero-original-quadratic-six-fixed-eight-receipt-8542.json)
登记完成范围。

源码预算 180 秒、4 GiB；驱动实际内层 exit0，
耗时 1.686397753 秒、最大子进程 RSS 48572 KiB。
原源最后阶段在 1.611638126 秒完成。
全部 223 次精除、140 次 Bareiss 商乘回、83 次已付支持乘回、
1 次完整 QQ 因式乘回均通过。

source/pull commit 为 492ad39544838857deb807bcaeb5520d5e1b18ed。
真实 pull 在 2026-11-28 08:33:54.087736 UTC 完成，
根 README 和课题 README 均无变化；
其 blob 分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、
5fbd905291dd044c88d35bd9c07ac0e586ff795a。
stdout 为 6580 字节，SHA256
612f2a1074ccad398ab76cadbbf8f8aebe3f7e2625ad9187c597ec930ffea4ac。

结论严格止于整个 $b_0=0$ 支的原必要曲线及上述准确恢复；
当前 W 其余原解和普通 ISP 均未因此宣称完成。
