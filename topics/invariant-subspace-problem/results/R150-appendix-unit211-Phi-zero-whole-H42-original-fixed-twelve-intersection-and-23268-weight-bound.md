# Phi：整 H42 原权支的固定十二阶返回与 23268 个不同权点上界

日期：2026-11-28（Asia/Taipei）。

## 1. 全原范围和新结论

本条针对当前 $\Phi=0,D\ne0$ 的整个权图中 $H_{42}=0$，包含第一六次头 $H_{19}=0$ 的所有零纤维。

由两条已经完成的原身份定义一个新的固定十二阶权多项式 $G$，本次实际证明
$$
D G\in I_{10},\qquad
\deg_{u,Q}G\le554,\qquad
\gcd_{\mathbb Q[u,Q]}(H_{42},G)=1.
\tag{1}
$$
因此整个 $H_{42}=0$ 支的不同复权点满足
$$
\boxed{\#\{(u,Q)\text{ 来自本支原物理点}\}\le42\cdot554=23268.}
\tag{2}
$$

(2) 是权点计数。固定这些权点后的 $\lambda,T,z$ 纤维仍须遵守各自已付头范围；没有由有限权点数直接宣称整个原商有限或整个 Phi 已空。

## 2. 固定十二阶原来源，完整保留首项零纤维

[第一头原 D 六次必要式](R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md)支付
$$
P_6D\in I_4.
$$
整第一头已排空，该原表示现覆盖当前整个 Phi 图。这里保留原 $D$ 因子，不误写成未作 $D$ 局部化的 $P_6\in I_4$。

[全 Phi 正则三来源六次式](R150-appendix-unit211-Phi-zero-whole-original-NSPS-sixth-scalar-and-regular-three-source-extension.md)支付
$$
C_6\in I_{10},\qquad I_4\subset I_{10}.
$$
这条身份包含斜率判别式的整零支。两式都只使用既有权单位环，且 $P_6,C_6\in\mathbb Q[u,Q,\lambda]$ 的原 $\lambda$ 次数均为六。

以 $\lambda^jP_6,\lambda^jC_6$，$0\le j<6$，作为十二列，以 $\lambda^0,\ldots,\lambda^{11}$ 为十二行，定义固定矩阵 $S$ 和
$$
G=\det S
=\det\operatorname{Syl}^{6,6}_\lambda(P_6,C_6).
\tag{3}
$$
全部条目都是 QQ$[u,Q]$ 多项式。固定矩阵 adjugate 的常数坐标给完整普遍身份
$$
G=aP_6+bC_6
$$
及
$$
DG=a(P_6D)+bD C_6\in I_{10}.
\tag{4}
$$
因此每个本图原点都满足 $G=0$。式 (3)–(4) 不倒置任一六次头；即使在 $H_{42}=H_{19}=0$、两原式都降次时仍然成立。

本次只按 (3) 定义原 QQ determinant，未展开它的巨大系数。

## 3. 完整 QQ 总次数上界

程序从固定十二阶矩阵的实际 QQ 条目总次数，得到以下行、列对偶：
$$
a=(40,40,40,40,40,39,39,38,38,37,37,36),
$$
$$
b=(0,0,0,0,1,1,14,14,14,15,15,16).
$$
每个非零条目都实际满足 $\deg S_{ij}\le a_i+b_j$，且完整匹配
$$
(6,0,1,2,3,4,5,7,8,9,10,11)
$$
达到对偶和。因此
$$
\deg G\le\sum_i a_i+\sum_jb_j=554.
\tag{5}
$$
这是原 QQ 多项式的严格上界，不是把某个模次数当成 QQ 次数。

## 4. 位于真实 H42 曲线上的唯一模见证

[三头互素结论](R150-appendix-unit211-Phi-zero-whole-three-heads-coprimality-and-798-sixth-head-exceptional-weights.md)已支付 $H_{42}$ 在 QQ$[u,Q]$ 中不可约、总次数 42。其规范 SHA256 为
1988b732b97dfdded9386c97d261774e6cc4d7e8db659f211faa54961c67a8e7。
本次没有重做因式分解。

固定 $p=1009$，完整核对 $P_6,C_6,H_{42}$ 所有 QQ 系数均 $p$ 整；$H_{42}$ 已有至少一个单位系数，实际 Gauss 常数指数为零。

按预定顺序，只检查 $\overline H_{42}=0$、原权单位和 $P_6$ 六次头。首个合格点恰为
$$
(u,Q)=(3,175)\in\mathbb F_{1009}^2.
$$
在选择它之前没有计算 gcd、determinant 或原理想秩，也没有按结果重新选点。此点上
$$
\deg_\lambda\overline P_6=6,\qquad
\deg_\lambda\overline C_6=5.
$$
完整实际 Bézout 返回
$$
s\overline P_6+t\overline C_6=1,
\qquad \deg s=4,\quad\deg t=5,
\tag{6}
$$
两个乘子的规范 SHA256 分别为
d3e4945f339ef2faa90b869116d592073a1772b0e51f3319337496efb0e45334
和
866271859774cf8ad4e435b519dd64f84a2784c1b855daa27cffd17ebb1d198b。

另按 (3) 的原固定十二阶尺寸直接计算，实际
$$
\det\overline S(3,175)=311\ne0.
\tag{7}
$$
虽然 $C_6$ 在该点降为五次，固定尺寸并未改变，(7) 仍是原 $G$ 的真实约化；$P_6$ 保持六次保证这一固定 determinant 与 (6) 相容。

## 5. 从单点非零到整条 QQ 曲线有限交

假设 $H_{42}\mid G$ 于 QQ$[u,Q]$，写 $G=H_{42}J$。$H_{42}$ 的最小系数 1009 赋值为零，$G$ 的系数 1009 整；多元 Gauss 赋值的乘积公式因此迫 $J$ 的系数也 1009 整。

在上述真实 $H_{42}$ 点约化，便有 $\overline G(3,175)=0$，与 (7) 矛盾。所以
$$
H_{42}\nmid G.
$$
结合已付 QQ 不可约性，得到 (1) 中的互素性。由于两个多项式都在 QQ 上，若在 $\mathbb C[u,Q]$ 共享曲线因子，其 Galois 共轭会给非平凡 QQ 公因子；故复数上也没有共同曲线成分。Bézout 与 (5) 给 (2)。

这是原多项式身份、系数整性及 QQ 不可约性共同推出的特征零结论，并未把模因子认成 QQ 分支，也未声称 $H_{42}$ 绝对不可约。

## 6. 固定权后的范围仍须保留

在这些权点中，$H_{19}\ne0$ 的部分已有原六次 $\lambda$ 模型，结合三生成元给有限纤维。$H_{19}=0,C_*\ne0$ 的部分可用已刊最高项模型。$H_{42}=H_{19}=C_*=0$ 的剩余固定权仍只沿用已付三生成元的 $\mathbb C[\lambda]$ 有限模表述，不能仅由本条权点有限性断言其 $\lambda$ 纤维有限。

这些剩余权点包含在既有 $H_{42}=H_{19}=0$ 的有限交中，因此不同复权点至多 798；这个既有权点界不替代每个 $\lambda$ 纤维的原返回。

本条只新增完整的整 $H_{42}$ 权支持有限性，不删任何上述零纤维。

## 7. 唯一实际执行

源：[整 H42 固定十二阶原标量交点输入](../notes/2026-11-28-unit211-Phi-zero-whole-H42-fixed-twelve-original-scalar-intersection-8542.py)，9789 字节，blob
017740aad4f49dc472c714ac507b818fb0a1494b，SHA256
150c6d10552e97914de24d46da398371740963205022cebd92f80586aa917e94。

唯一首次 run 46098494949、job 140835304343；源提交
80d7105eee4f792176e1dee0255fb73369498d98。
实际 $3.403564485$ 秒、最大 RSS $51892$ KiB、内层退出码 $0$。
stdout 2257 字节，SHA256
c6742cc3c85e4375b3685f8e9c66982be895a9ddf23a89041a27aaf88e9a3f2f。

2026-11-28 02:31:53.130119 UTC 真实 pull 至
6a507e579284348430be008489eaf185eb38f73e，两份 README 无变化。旧 P6 参数只在 runner 临时恢复；没有新增系数载荷，没有重算旧 P6 cofactor 或旧三头因式，也没有声称普通 ISP 已完成。
