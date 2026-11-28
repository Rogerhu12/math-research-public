# 正确 Phi：原 F 商矩阵的一轮 Q 精除与两个幺模输入的内存边界

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127。

两个预先固定的新输入 F、G 均在原定 1 GiB 内存上限内以 FLINT 分配失败、内层 exit $-6$ 结束。本条准确保留其中已经完整返回的一轮新原身份：
$$
F_*=-Q\det M_1.
\tag{1}
$$
因此
$$
F_Q:=F_*/Q=-\det M_1
$$
是当前原图的非零必要权多项式，并满足
$$
\deg_uF_Q=368,\qquad \deg_QF_Q=205,\qquad \deg F_Q\le408.
\tag{2}
$$
(1) 只支付 $\operatorname{ord}_QF_*\ge1$，没有支付准确阶数。G 没有返回任何完整零行精除轮，不登记它的新 $Q$ 幂。

## 1. 已知输入及本次独立新目标

沿用
[两个原权矩阵的 QQ 精确已付因子提取](R150-appendix-unit211-Phi-zero-corrected-exact-paid-matrix-extraction-and-common-curve-bidegrees-five-fifty-one.md)
的非零支持
$$
F_*=\det M_F,\qquad G_*=\det M_G.
$$
当前正确 Phi、distinct singleton、物理 $D\ne0$ 的旧已付权环中，
$$
F_*\in I_6,\qquad G_*\in I_6+(Vlow).
$$
原矩阵为 $12$ 阶和 $14$ 阶；已有
$$
(\deg_uF_*,\deg_QF_*)=(368,206),\quad\deg F_*\le409,
$$
$$
593\le\deg_uG_*\le594,\quad\deg_QG_*=302,\quad\deg G_*\le633.
\tag{3}
$$
原来未归一的支持还有精确身份
$$
F=Q(u-1)^4(-L)^{15}F_*.
\tag{4}
$$

本次固定同一新源，以两个独立首次工作流分别设置 ISP_Q0_MODEL=F 与 ISP_Q0_MODEL=G，每次均为 120 秒 / 1 GiB、外层 135 秒。它只按前次实际的八组整数行列尺度形成唯一商矩阵定义并核 profile，没有重求旧最小匹配、条目赋值、旧最高矩阵、旧行列式或旧双轴 gcd。

新目标是 $\mathbb Q[u]$ 上的真幺模行运算和完整二元行的 $Q$ 精除。没有新模点、素数或未付 $u$ 主元逆。准确输入及依赖见
[唯一冻结输入说明](../notes/2026-11-28-unit211-Phi-zero-corrected-QQ-Q-primary-unimodular-row-extraction-8542-input.md)。

## 2. 已完成一轮为什么给整个 QQ 多项式身份

在某列的两个 $Q^0$ 条目 $a,b\in\mathbb Q[u]$ 上，源实际返回
$$
g=sa+tb,\qquad a=gA,\qquad b=gB,\qquad sA+tB=1.
$$
因此两个完整二元行之间的矩阵
$$
E=\begin{pmatrix}s&t\\-B&A\end{pmatrix},
\qquad
E^{-1}=\begin{pmatrix}A&-t\\B&s\end{pmatrix}
\tag{5}
$$
具有行列式一。源码对所有 $Q$ 系数、所有列返回这两个逆行身份，而非仅返回选中主元。

F 的原矩阵最大条目 $Q$ 次数为 $25$。实际使用的每行 $12\times26$ 个 $\mathbb Q[u]$ 坐标包含全部原多项式；行运算只用 $u$ 多项式，不增 $Q$ 次数。这个容器不是截断环，也没有忽略高阶尾项。

F 的第零轮完成了 $35$ 个双行 Bézout 块和 $7$ 次换行。全部块的行列式一和 $70$ 个整除商都乘回；两个完整行的逆身份共返回 $21840$ 个坐标。模 $Q$ 阶梯形的真实秩为 $11$，其最后一行的全部 $12$ 个常数条目都为零。该完整二元行的 $312$ 个坐标逐项精除 $Q$ 并乘回。于是
$$
E_0M_F=\operatorname{diag}(I_{11},Q)M_1,
\qquad
E_0\in\operatorname{GL}_{12}(\mathbb Q[u]),\qquad
\det E_0=(-1)^7=-1.
\tag{6}
$$
取行列式即得 (1)。每个非常数 $u$ 主元的零集仍由 (5) 的全多项式逆保留；没有把这些主元当成物理单位。

该轮完整结束于数学时间 $59.760017624$ 秒，已输出
new_complete_unimodular_Q_primary_round_returned。返回的 $M_1$ profile 为：

- 阶数：$12$；
- 全部条目共有 $501507$ 个非零项；
- 条目最大 $u$ 次数 $903$、最大 $Q$ 次数 $25$、最大总次数 $904$；
- 完整系数流 SHA256：e0c9a55b770a10c136b0ceca49b90fcb683bffd297026eba1bf918acb9f0bf84。

这里的高条目次数没有被误作行列式次数；后者由原多项式身份 (1)、(3) 支付。该巨大矩阵没有作为系数载荷保存。

结合 (4)，本次还给完整原支持的定义式
$$
F=Q^2(u-1)^4(-L)^{15}F_Q.
\tag{7}
$$
当前 $Q$ 是旧物理权单位，所以 $F_Q\in I_6$。从非零性及次数可加性得到 (2)，不需要另做行列式或最高系数计算。

## 3. 没有完成的部分

F 的第一轮只返回了 $3$、$6$ 个主元的中间 checkpoint；最后一个时间为 $62.235726223$ 秒，累计双行块数 $41$。这一轮没有返回完整零行或整行除 $Q$，故不能增加 (1) 的指数，也不能据此断言剩余常数矩阵满秩。

G 的唯一第零轮只返回至 $6$ 个主元、$21$ 个双行块，最后 checkpoint 时间为 $21.019311272$ 秒。没有任何
new_complete_unimodular_Q_primary_round_returned 记录，也没有最终满秩记录。因此 G 的新有效提取指数取 $b=0$，支持仍为原 $G_*$；没有结论说它不含 $Q$。

两个输入的失败均是内存分配边界，而非 120 秒计时边界。完整内层日志给出：

| 输入 | run / job | driver 秒 | 峰值 KiB | 内层 exit | FLINT 末错误 |
|---|---|---:|---:|---:|---|
| F | 46161293869 / 141028978873 | 90.638152077 | 1030128 | -6 | Unable to allocate memory (1605632). |
| G | 46161295453 / 141028982297 | 39.604973848 | 1032692 | -6 | Unable to allocate memory (802816). |

外层工作流的失败状态和内层 $-6$ 原样保存，不将已经完成的一轮改写成整门成功。这两个门均冻结：不增加内存或时间、不改主元顺序、不恢复后继轮，也不把同一个饱和目标改写后重跑。

## 4. 当前公共支持界保持 45

由
[公共因子的总次数界及 Q 精除条件式](R150-appendix-unit211-Phi-zero-corrected-common-factor-total-degree-forty-five-and-Q-extraction-refinement.md)，
真实 $a,b$ 下的两个新商的公共 gcd 满足
$$
\deg H_{a,b}\le5+\min(41-a,40-b).
$$
本次唯一有效新指数是 $a=1,b=0$，故
$$
H_{1,0}=\gcd_{\mathbb Q[u,Q]}(F_Q,G_*),\qquad
\deg_uH_{1,0}\le5,\qquad \deg H_{1,0}\le45.
\tag{8}
$$
$Q$ 次数也不超过 $45$；原可能公共纯 $Q$ 内容上界仍为 $40$。本条没有进一步降低这一公共曲线界，也没有求出 QQ 公共因子。

原权点既可能位于公共曲线，也可能是去公共因子后的孤立交点；这些全部保留。没有 QQ 无公共曲线、有限权点、整个 Phi 排空或完整规范点数的新结论。当前原有限生成结果保持其原系数环与几何局部化范围；没有恢复被撤回的错误 Rbar 链。

## 5. 完整实际来源

冻结源：
[Q 主分量幺模原行源码](../notes/2026-11-28-unit211-Phi-zero-corrected-QQ-Q-primary-unimodular-row-extraction-8542.py)。

源码 blob：f6ffe1592022e69abe8746e97e436b86763b354b。

SHA256：5971d0015ea65e5f8f2fc0c0ba6be7bbf5aea15292dc1383cd83c85dee3a877c。

两个输入的源提交及真实 pull 后提交均为 e9083c90000316e09cd6efda8cae908bd5bf0bb3。F 的规则读取时间为 2026-11-28T15:42:57.669933+00:00，G 为 2026-11-28T15:42:58.163053+00:00，两次根、题目 README 均未变化。

F stdout：$3271$ 字节，SHA256 7c9b231e1b46a3ad8bba811b888f993893c591f1a50a325b2e255cf4ae4a9207。

G stdout：$1700$ 字节，SHA256 fd410842d88953afdcc28f5cf101d402f8cad0818c643c4b00da84601d8dd228。

两份完整内层数学记录和末尾 FLINT 错误均已亲读。[合并小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-QQ-Q-primary-unimodular-row-extraction-8542-execution.json)只保存实际身份、完成范围、profile 与资源边界，不含原矩阵系数载荷或可恢复轮状态。
