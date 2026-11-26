# R150 / S0 / Lt0：原五个二次式把参数压到 F(41,33)

状态：**已证明必要曲线，未排除一般 Lt0。** 剩余原点的参数 $(e,k)$ 必须满足一个新的明确不可约多项式 $F_{41,33}(e,k)=0$，双次数 $(41,33)$，846 项。结论由原五个二次式的多项式组合得到，完整首项零纤维均保留。

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127；2026-11-27（台北）。

## 1. 五个原二次式

在既定 $e=u-1,k=Q/e,j=k+2-2e$ 图上，取

$$q_1=E_1,\quad q_2=E_{B,\mathrm{even}},\quad q_3=E_{B,\mathrm{odd}},\quad q_4=N_1,\quad q_5=Q_a.$$

前四个多项式从原 Frobenius Gram、正确 dual product、原 mean 和 mixed $N_1$ 方程生成。它们对 $(\lambda,f,v)$ 的联合次数至多二。第五个是同 eta 原范数必要式

$$Q_a=U^2D-2(1-ek)B^2.$$

它不要求预先除以 $B$，因为源码在原环中核出

$$D Q_a=M_a(UD+2j\eta B)+2B^2M_n,$$

$$M_a=UD-2j\eta B,\qquad M_n=2j^2\eta^2-(1-ek)D.$$

$D$ 是原两值不同的已付分子。因此 $Q_a$ 本身也有原局部理想来源；它不是另取一嵌入的范数条件。

## 2. 一个完整的原多项式组合

令 $\boldsymbol m$ 为 $(\lambda,f,v)$ 中联合次数至多三的全部 20 个单项式列向量，按源固定的次数逆序排列，最后一项恰为 $1$。对五个 $q_i$ 分别乘

$$\lambda,\quad f,\quad v,\quad1$$

得到 20 行原式，记成

$$M(e,k)\boldsymbol m=\boldsymbol q,$$

其中 $M$ 为 $20\times20$ 矩阵。源逐项重建并检查全部 20 个等式；没有剥除矩阵行内容或只取某个泛型子块。矩阵条目合并 SHA-256 为

`7eb7ed6202c0a79c55a902c94fc8b35a962a59e631253a1366b134e88266896a`。

对 $M$ 做有行交换记录的 fraction-free 消元，每次除法均在 $\mathbf Q[e,k]$ 中精确相除并乘回。随后逆向通过同一批原行操作，**只重构常数坐标需要的一行余子式**。得到真正的多项式行向量 $\boldsymbol c(e,k)$ 和多项式 $D_M(e,k)$，源实际核验全部 20 个条目：

$$\boxed{\boldsymbol c M=(0,\ldots,0,D_M)}.$$

因此

$$\boxed{D_M=\boldsymbol c\boldsymbol q}$$

是原五个二次式的显式多项式组合，右边逐行都是某个 $q_i$ 乘 $\lambda,f,v,1$ 再乘已计算的多项式系数。系数行的合并 SHA-256 为

`c5710af83af7e7bb68f3cb4841a34da0199d9b7a92196643973a1eb84dea109b`。

中间消元 pivot 可在某些原点上为零；本条没有在点上除以这些 pivot。最后身份在整个多项式环中成立，故保留这些纤维。

## 3. 完整因子覆盖

源返回并逐项乘回完整分解

$$\boxed{D_M=65536\,e^4k^{10}j^6(4e-k-4)^2(4e-k)D_3^{10}F_{41,33}(e,k)},$$

其中

$$D_3=4e^3-3e^2k-4e^2+ek^2+4ek+4e-k-4.$$

$D_M$ 的双次数为 $(84,72)$，3013 项，SHA-256 为

`e235b8e13c11576e11a7aafec192d47f075facaef18991359e0c4b1fb9c1470f`。

新因子 $F_{41,33}$ 的双次数为 $(41,33)$，846 项，SHA-256 为

`ca1b9ef43348fdfa70bf1303051d4a5d9315a64a18c7b9b0f98c4ed1e2482144`。

没有省略其他非恒定因子。$e,k,j,D_3$ 为既定原物理单位；$4e-k-4$ 来自已完成的半基点权整支排除；$4e-k$ 来自已完成的原 mean 一致性退化直线排除。因此

$$F_{41,33}(e,k)=0$$

对每个剩余原点都成立，且 $F_{41,33}$ 在这些已付因子局部化后的原必要理想中。此处没有以多变量 gcd 为一判断空集，没有将已付边界重新当作泛型假设，也没有从某个模素数图提升结论。

这个二参数输入可以继续与原 mean 的低次乘法规则及分别的原 $N/P$ 联立。它不代表一般 Lt0 已排空，不代表完整原临界理想的全部生成元已等价返回。

## 4. 实际执行与失败分支

自含源：[2026-11-27-unit211-S0-Lt0-five-quadrics-parameter-curve-original-return-8542.py](../notes/2026-11-27-unit211-S0-Lt0-five-quadrics-parameter-curve-original-return-8542.py)。

- 20,308 字节，SHA-256 `e7fafb7bb9d0ff59cbd54898ba142fe297cb733b9a866f30d930c4bf72718ae1`。
- 无参数；Python 3.12.14、python-flint 0.9.0；150 秒 alarm、4 GiB 地址空间上限。
- 实际退出码 0；外部墙钟 101.464392 秒、源内 101.041965 秒；最大 RSS 58,108 KiB。
- stdout 12,906 字节，SHA-256 `6fc28af8f0b45a9869528c8b45de5518aa31ef607e5fd9ccdab62922a68dbfc2`。
- 回执：`notes/2026-11-27-unit211-S0-Lt0-five-quadrics-parameter-curve-execution-8542.json`。

此前曾把同一组二次式先经过原 mean 余式压成 10 个单项式，再尝试展开整个 $10\times10$ 伴随矩阵；180 秒 alarm 在第 7 步之后终止，未返回行列式或伴随矩阵。这个失败没有用于本结论，也不重跑。负回执：`notes/2026-11-27-unit211-S0-Lt0-ten-matrix-full-adjugate-failure-8542.json`。本条成功的原身份来自另一个明确计算对象：原 $20\times20$ 矩阵的单一常数坐标余子式行。
