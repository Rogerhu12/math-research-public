# Phi=0 例外 S 四次域：整四次公因子的一阶提升不相容

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**本次新输入已完整返回；没有提高此前严格的 112 个不同有序基点上界。** 实际结果是：原 $F,G$ 在整个常数域中的同一个首一 $\rho$ 四次公因子不能整体提升到模 $\phi^2$ 的首一四次公因子。该不相容不排除部分原核列的更高阶提升，亦不证明原结式的 $\phi$ 重数小于 8。

## 1. 完整原输入及新问题

沿用[整 S 四次域排除与 112 覆盖](../results/R150-appendix-unit211-Phi-zero-exceptional-whole-S-moment-quartic-exclusion-and-112-cover.md)及[新 G-only 精确公因子记录](2026-11-27-unit211-Phi-zero-exceptional-S-quartic-G-only-exact-gcd-no-improved-bound-8542.md)的同一个原输入。令
$$
\phi(\lambda)=\frac{420\lambda^4-1884\lambda^3+3663\lambda^2-3084\lambda+916}{420},
\qquad K=\mathbb Q[\lambda]/(\phi).
$$
此前已经证明 $\phi$ 不可约，原 $F,G$ 的 $\rho$ 次数分别为 26、31，并在 $K[\rho]$ 中有准确的首一公因子 $g$，$\deg_\rho g=4$。完整 $g$ 已精确保存，不重新执行此前 208 维、88 维或 160 维返回。

取每个 $K$ 系数的 $\lambda$ 次数小于 4 的规范代表。令
$$
q_F=\overline F/g,\qquad q_G=\overline G/g.
$$
本次使用完整的原 $\mathbb Q[\lambda,\rho]$ 多项式，而非只用其模 $\phi$ 的值，逐系数精确计算
$$
E_F=\frac{F-gq_F}{\phi}\pmod\phi,\qquad
E_G=\frac{G-gq_G}{\phi}\pmod\phi.
$$
每个 $\phi$ 除法均把商和余式乘回；实际完成 59 次此类原除法。

若整个 $g$ 有首一四次共同提升
$$
\widetilde g=g+\phi h\pmod{\phi^2},\qquad
h\in K[\rho],\quad \deg_\rho h<4,
$$
则必须对同一个 $h$ 有
$$
q_Fh=E_F\pmod g,\qquad q_Gh=E_G\pmod g.
$$
反过来，这两个相容式正是相应两个余商修正存在的条件。因此所求是完整代数 $K[\rho]/(g)$ 上的同一未知量，不能分别选择两份修正，也没有把这个代数假定为域或约化代数。

## 2. 实际有理线性返回

在 $\{1,\lambda,\lambda^2,\lambda^3\}\{1,\rho,\rho^2,\rho^3\}$ 的 16 元基下，上面两式组成 32 条有理线性方程。本次构造并实际约化的增广矩阵尺寸为
$$
32\times17.
$$
完整 $\mathbb Q$ 增广秩为 17。系数矩阵只有 16 列，故两式不相容。这一结果保留全部四个 $\lambda$ 嵌入及完整 $\rho$ 四次代数。

因此，本次没有得到模 $\phi^2$ 的整个首一四次共同因子，后续四条核列同时提到二阶以及新的结式约化未执行。原固定 57 阶 Sylvester 的真实已付下界仍是 $\phi^4$；模 1009 的重数 8 仍只是有理重数的上界。不得把本次不相容改写成 $\phi^8$ 不可能：不同核方向可能具有不同的提升阶数。

## 3. 实际执行及冻结范围

唯一源码：

[2026-11-27-unit211-Phi-zero-exceptional-S-quartic-first-phi-common-divisor-lift-input-8542.py](2026-11-27-unit211-Phi-zero-exceptional-S-quartic-first-phi-common-divisor-lift-input-8542.py)。

- source blob：a2bd84ccb8f16b8f6ee270d363a92ce3d5e161e5。
- source SHA256：59d367f3e01d96b9a1e9cb2ce415a6304b1fbef62dfed9fd6f2842fa0df4dab6。
- run/job：46049433900 / 140676783879。
- source commit：6a249d1f6870908d5feb18dfcdb716f68ff53256。
- 内层耗时：0.152720720 秒；最大 RSS：39952 KiB；退出码：0。
- stdout：732 字节；SHA256：3d30faa9a46dcdeef88b23d2005fc1242588e821f4256c18ba0b203d57cb649c。
- 真正线性输入在 0.088797365 秒形成；完整不相容返回在 0.089610730 秒完成。

本次真实拉取从 6a249d1f6870908d5feb18dfcdb716f68ff53256 到 0526ab6b035556abf0c9051e1a69c11afb6f6566，2026-11-27 18:26:23 UTC 检查两份 README 的 blob 均无变化。资源预算保持 120 秒/1 GiB，没有抬限或重放旧矩阵。

[小回执](2026-11-27-unit211-Phi-zero-exceptional-S-quartic-first-phi-lift-inconsistent-execution-8542.json)保存完整数学阶段及实际执行身份。此处是完整数学分支不相容，既不是资源超时，也不是整个例外原图为空；当前上界仍为 112，普通 ISP 未完成。
