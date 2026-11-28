# R150：正确 Phi 的整 B 曲线中 F34 权纤维由原 I4 排空

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

**已证明。** 在当前修正后的 $\Phi=0,\ D_{\rm val}\ne0$ 原图中，整 $B=0$ 曲线的已刊 $C_{76}$ 覆盖里，完整 34 次因子 $F_{34}$ 没有原点。新证书直接在原 $I_4=(E_1,E_{Be},E_{Bo},N_1)$ 中返回常数 $1$，没有倒置 $\lambda,t,D_{\rm val}$ 或任何几何范数。结合此前完整二次因子的排除，B 曲线只余 $F_{40}$，不同权对至多 40 个；本篇不排除该最后因子。

## 1. 同一个原 B 图及完整常数域

采用 [整 B 的正确原十二行呈示](R150-appendix-unit211-Phi-zero-true-Bzero-whole-original-I6-twelve-by-two.md)。其有理权坐标为

$$
u=\frac{(x+1)^2}{3x},\qquad
Q=\frac{4(x^2-x+1)}3,\qquad
\ell=\frac{(x+1)(5x-1)}{6x^2}.
$$

整图只使用该文逐项支付的权分母，尤其不倒置旧选头 $H_3$。由 [终端原乘子的一次覆盖](R150-appendix-unit211-Phi-zero-true-Bzero-terminal-C76-original-ideal-cover.md)，原点必满足

$$
C_{76}(x)=0.
$$

其中 $F_{34}$ 是既有完整 QQ 因式分解中唯一 34 次因子，其原多项式字典 SHA256 为

`b593d2770a0337dcaf2f4908e51cfc9feb3c5890ce21e5c3c6c1707ff98187ff`。

本篇使用整个

$$
K=\mathbb Q[x]/(F_{34}),
$$

不选某个实根、复嵌入或模因子。原权分母在整个 K 中都已有实际逆乘回；不存在因某个几何首项为零而删除的 K 分量。

原四行在同一个首一二次

$$
q_\omega=\omega^2+q_1(\lambda)\omega+q_0(\lambda),
\qquad \deg q_1\le1,\quad\deg q_0\le2
$$

下分别写成

$$
r_i=a_i(\lambda)+b_i(\lambda)\omega,\qquad 0\le i\le3.
$$

$q_\omega$ 和四个 $r_i$ 保有原 $I_4$ 来源；原四式与这些行的理想关系由整 B 呈示逐项给出。系数的次数依次为 $(4,3),(4,3),(4,3),(3,2)$。

已成原首一 $g_6\in K[\lambda]$ 的 SHA256 是

`f2d41bd0b2b1623745f9e0fd69a0cb488650f07bcd264a3f18b4a63bf8188b0c`。

新源仅按其第一非零原行对 (0,3) 再生这个既定输入：

$$
g_6=\gamma(b_3r_0-b_0r_3),\qquad
\gamma\in K^\times,
$$

并核不可变身份。没有重放旧六对 gcd、旧原 I6 的 408 维矩阵或正目标门。

## 2. 四个固定次数原范数身份

对每条原线性行，定义新的

$$
n_i=a_i^2-q_1a_ib_i+q_0b_i^2.
$$

它满足完整多项式身份

$$
n_i=(a_i-q_1b_i-b_i\omega)r_i+b_i^2q_\omega.
\tag{1}
$$

这是固定次数 $(2,1)$ 的 Sylvester 身份；没有倒置 $b_i$，所以 $b_i=0$ 及进一步降次的全部纤维仍保留。源码实际返回 (1) 的 $\omega^0,\omega^1,\omega^2$ 全三坐标。

此次四个 $n_i$ 的 $\lambda$ 次数准确为

$$
8,\ 8,\ 8,\ 6.
$$

它们除以既有首一 $g_6$ 后余式次数均为 5。该首一短除没有新增参数首项逆。

## 3. 完整 Bézout 合成回原四式

在整个 $K[\lambda]$ 中，对新的理想

$$
(g_6,n_0,n_1,n_2,n_3)
$$

进行精确扩展 Euclid。逐条加入 $n_0,n_1,n_2,n_3$ 后，实际首一 gcd 次数为

$$
1,\ 1,\ 1,\ 0.
$$

每步都保留并乘回

$$
h=\beta_g g_6+\sum_i\beta_i n_i.
$$

若 $n_i=q_i g_6+\bar n_i$，新 Euclid 行 $h'=Ah+B\bar n_i$ 使用准确运输

$$
\beta_g'=A\beta_g-Bq_i.
$$

最终 $h=1$。将上述 $g_6$ 的原 (0,3) 来源和 (1) 全部代入，实际得到

$$
\sum_{i=0}^3
\bigl(M_{i0}(\lambda)+M_{i1}(\lambda)\omega\bigr)r_i
+H(\lambda)q_\omega=1.
\tag{2}
$$

源码直接把 (2) 的三个完整 $\omega$ 坐标乘回为 $(1,0,0)$，而不只读取 gcd 标志。四个 (1) 加最后 (2) 共返回 15 个坐标。因此原 $I_4$ 在整个 K 上包含 1，所有复嵌入、所有 $\lambda,\omega$ 重数和所有线性头零纤维均排尽。

本结论强于原物理单位目标：不需要原 NS/PS，也没有用 $D_{\rm val}^{-1}$。结合 [完整二次因子原排除](R150-appendix-unit211-Phi-zero-true-Bzero-terminal-quadratic-complete-original-exclusion.md)，$C_{76}$ 的剩余支持只可能为 $F_{40}$。

## 4. 唯一新实际执行与冻结边界

源：[固定原范数输入](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-large-fixed-original-norms-8542.py)，环境选择 `ISP_B_FACTOR_DEGREE=34`。源 blob：

`f7aa6e677ca3d4e2a59c146f0c35e7ec4fdc6cc9`。

源 SHA256：

`c6e8acc0e71c119fd76f8213f2934daacc8ec728cb44b5a51f8541413e3a6eef`。

唯一 run **46125571211**，job **140919303032**；源码和真实 pull 提交均为 `85e32a6c96a40c236c915030017a0972b06493ed`。真实 pull 时间 2026-11-28 08:23:27.809249 UTC，两 README 内容未变。

数学末阶段 5.694431214 秒，驱动 5.722861425 秒，最大 RSS 51060 KiB，exit 0。预算为 120 秒/1 GiB、外驱动 135 秒。stdout 4644 字节，SHA256：

`5b34dab63aba321baa4a4a14d397d245904a53342489cdfea3db66212738e07c`。

[本次小回执](../notes/2026-11-28-unit211-Phi-zero-B-F34-fixed-norm-original-execution-8542.json)保完整阶段身份及原返回摘要，不保存系数载荷。

此前大矩阵 run 46124520657 的真实 1 GiB 内存失败保持冻结，本次没有重启、缩写或重新排列那个矩阵。新增输入是未曾计算的四个固定原范数及其完整三坐标 Bézout。整 $F_{40}$、一般 Phi 及普通 ISP 不因本篇自动完成。
