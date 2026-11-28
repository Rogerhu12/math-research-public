# R150 附录：Phi 全第一头图的两个原权支持互素与至多 1634 个有限性例外权点

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）  
范围：一般 unit211 的当前 $\Phi=0,D\ne0$ 原图；整第一二次头已经关闭。  
状态：完整特征零精确返回；没有声称整个 Phi 原图为空，也没有把所有原权点计为有限集。

## 1. 结论

在当前原图上，令 $H(u,Q)$ 为已刊完整 $P_6$ 的 $\lambda^6$ 首项除已付权单位后的多项式；令 $C_*(u,Q)$ 为完整原最高 NV/F6 提升的最终权分母除已付权单位后的多项式。两个定义均固定在下文的完整原来源，分别满足
$$
\deg_{u,Q}H=(19,11),\qquad \deg_{\rm tot}H=19,
$$
$$
\deg_{u,Q}C_*=(74,49),\qquad \deg_{\rm tot}C_*=86.
$$
本次完整 QQ 运算证明
$$
\gcd_{\mathbb Q[u,Q]}(C_*,H)=1.
\tag{1.1}
$$
因此
$$
B=\{(u,Q)\in\mathbb C^2:C_*(u,Q)=H(u,Q)=0\}
$$
是有限集，且
$$
\# B\le86\cdot19=1634.
\tag{1.2}
$$
所有原单位零点也被这个上界计入，所以限制到当前原图只会减小例外集。

对任意不在 $B$ 的当前原权点：

- 若 $H(u,Q)\ne0$，已有完整原 $P_6$ 成为首一 $\lambda^6$，结合真实三生成元给 $(\lambda,T,z)$ 的必要原环境长度至多 18。
- 若 $C_*(u,Q)\ne0$，已有完整最高项提升给同一原环境至多 21 个生成元，故其长度和不同点数至多 21。

这给出整个当前权图除至多 1634 个权点外的有限纤维覆盖。两个条件的并集是覆盖，不要求同时非零。在 $B$ 上没有使用任一尚未支付的 $\lambda$ 首项，也没有给其纤维大小偷加界。

$B$ 仅是这两个现有有限环境同时失效的权点集。这里没有证明所有原权点都落在 $B$，没有把原权参数空间称为有限，也没有声称整个 Phi 或普通不变子空间问题已经完成。

## 2. 两个原输入的准确来源

[整 H1 原排除](R150-appendix-unit211-Phi-zero-whole-H1-complete-original-exclusion.md) 已关闭整个第一二次头零支。因而在本范围，三个真实原均值可以用完整恒等式化为 $T^2,Tz,z^2$ 的规则，原环境在权环加 $\lambda$ 上由 $1,T,z$ 生成。这里没有假定该原商自由。

第一个输入来自
[原 D 的六次必要式](R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md)。
它的完整 $P_6$ 双权及 $\lambda$ 次数为 $(39,20,6)$。本次只从原保存定义提取 $\lambda^6$ 系数，不重算原 cofactor。该完整首项的双权次数为 $(34,19)$、387 项；依次只剥已有原单位 $u,(u-1),Q,1-Q,\ell$ 的实际公因子，逐项乘回，得到上述 $H$，共 137 项。具体剥除记录为 $u$ 一轮、$u-1$ 两轮、$Q$ 一轮、$1-Q$ 一轮、$\ell$ 六轮。原 $H$ 的不可约性已有记录，本结论不以再次因式分解作为门。

第二个输入来自
[完整最高原 NV/F6 提升及 21 生成元](R150-appendix-unit211-Phi-zero-whole-first-head-highest-original-NV-F6-filtered-lift-and-twenty-one-generators.md)。
取其三个完整原最高行，按顺序组成
$$
A=
\begin{pmatrix}
\widehat r_{\rm NV}\\
\widehat r_{F6}\\
\widehat r_{N1}
\end{pmatrix}.
$$
这三个原行对应的原次数为 $7,6,2$。已成常数目标的系数唯一，故也由
$$
\alpha=e_0\operatorname{adj}(A)/\det A
\tag{2.1}
$$
定义。设 $C$ 为三个约分后 $\alpha_i$ 的权分母最小公倍式。原证明已经给出
$$
C\lambda^7=a_0+a_1T+a_2z
\quad\bmod I_{\rm original},
\qquad
\deg_\lambda(a_0,a_1,a_2)\le(6,5,5).
\tag{2.2}
$$
它产生首项 $C^3\lambda^{21}$ 的真实原行列式关系；直接按基权 $(0,1,1)$ 递降还给出 21 生成元界。

本次为新的相交目标仅取上述行的必要定义，以 (2.1) 重新识别同一 $C$；没有执行旧五行 Gaussian。实际 $C$ 为 $(78,52)$、2611 项；只剥已付的 $Q$ 一轮及 $\ell$ 两轮，得到同一 $C_*$。源码还允许在当前 Phi 图剥已有的 $2\ell-3$ 整支，但实际额外整除次数为零。

这些剥除都有完整乘回。$\ell$ 使用其在 $\Phi=0$ 上的原有理定义
$$
\ell=1-\frac{2(u-1)(u-2)}Q,
$$
因此程序中的纯权分子与原已付 $Q$ 分母必须一起解释，不能把它误认成新单位。

## 3. 特征零互素与全部纤维

新的唯一相交目标是直接在 $\mathbb Q[u,Q]$ 算
$$
G=\gcd(C_*,H).
$$
实际返回 $G=1$。源码完整乘回 $C_*=G(C_*/G)$、$H=G(H/G)$，并核剩余商互素。本结论没有使用模素数空性、随机权特化或数值结果。

互素性在扩张到 $\mathbb C$ 后仍排除公共曲线分量。将两条平面曲线射影闭包后，Bézout 交数至多为总次数乘积 $86\cdot19$；仿射不同交点数不超过总交数。这同时涵盖任何坐标投影的首项下降、竖直纤维或位于无穷远的交数，不需额外倒置投影首项。

固定一个当前原权点。若 $H\ne0$，将完整 $P_6$ 除其实际首项可得首一 $\lambda^6$；再用三个原均值规则，必要商由
$$
\lambda^j,\ \lambda^jT,\ \lambda^jz,\qquad 0\le j<6
$$
生成，故长度至多 18。若 $C_*\ne0$，所有剥掉的因子已经是当前原单位，故 $C\ne0$，(2.2) 的既有加权递降给长度至多 21。取其商以加入其余完整原值式只会减小这个长度。

在两个首项同时为零的全部 $B$ 上，本证明不进行上述除法。特别是，(1.2) 不构成 $B$ 内原值空性证据。

## 4. 实际执行身份

唯一新源：

[2026-11-28-unit211-Phi-zero-whole-highest-support-and-P6-head-exact-intersection-8542.py](../notes/2026-11-28-unit211-Phi-zero-whole-highest-support-and-P6-head-exact-intersection-8542.py)

源 blob `47aaafc94caf3880e330c2570fb2b8d8e8f76616`，SHA256

`a8d3f03e401a7a7c356da40e1f353ab5d3e879b9455a09a2f73d526c7df1af47`。

实际运行：

- run `46088133539`，job `140802466730`；
- 源提交 `9a9868c5e67083a3bd07563d0d8d2853a8bff52a`；
- 2026-11-28 00:29:34.380989 UTC 真正 pull 后源提交相同，根和课题 README 都无变更；
- 1.218746428 秒，峰值 49176 KiB，内层退出码 0；
- stdout 2929 字节，SHA256 `76e30c754f13e57d7aff051335703985d10604c640b9dcb16477d9a4c286f6f8`。

小回执：
[2026-11-28-unit211-Phi-zero-whole-highest-support-and-P6-head-exact-intersection-8542-execution.json](../notes/2026-11-28-unit211-Phi-zero-whole-highest-support-and-P6-head-exact-intersection-8542-execution.json)。

原多项式的精确定义仍在源码和已有原来源中。$C_*$ 的 2403 项 profile SHA256 为
`f2fcd6f323adaf47121341fc2e28c8af92dfba0e84dd13ed87e96f1f77081d8a`；
$H$ 的 137 项 profile SHA256 为
`24f31b9bac95b9e45fc2f8a5fffc1035dece82238d19f1ec5030c68e026b424d`。
没有新增可重算系数文件、编码或分片，也没有重放旧 cofactor、旧大投影、旧弱 Popov 或旧范数门。
