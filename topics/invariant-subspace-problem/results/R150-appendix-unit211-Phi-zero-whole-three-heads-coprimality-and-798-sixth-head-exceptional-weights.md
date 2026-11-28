# Phi：真实 H42、H19 互素与至多 798 个六次头例外权对

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 结论与准确范围

在当前整个 $\Phi=0,D\ne0$ 原图，记：

- $H_{42}$：新完整 NS/PS 六次标量 $C_6$ 的真实最高系数，剥原已付单位后的支持；
- $H_{19}$：旧原物理 $D$ 目标必要六次式 $P_6$ 的真实最高支持；
- $C_*$：旧最高 $N(V),F_6,N1$ 原来源的二十一个生成元支持。

本次完整 QQ 返回给出
$$
\gcd_{\mathbb Q[u,Q]}(H_{42},H_{19})=1,\qquad
\gcd_{\mathbb Q[u,Q]}(H_{42},C_*)=1.
\tag{1}
$$
$H_{42}$ 的完整 QQ 因式分解只有一个不可约因子，重数 1。

所以新的六次头共同例外集合
$$
E=\{(u,Q)\in\mathbb C^2:H_{42}(u,Q)=H_{19}(u,Q)=0\}
\tag{2}
$$
至多有 **798 个不同权对**。集合 $E$ 外，每个固定原权对的必要代数长度至多 18；若另有原斜率 $\Delta_N\ne0$，则至多 12。

这不表示全部原权对只有 798 个，也没有排除 (2) 内的任何纤维。二元多项式 gcd 为 1 不等于它们没有共同零点。整 Phi 和 ordinary ISP 均未完成。

## 2. 三个真实全图输入

[完整 NS/PS 全图来源](R150-appendix-unit211-Phi-zero-whole-original-NSPS-sixth-scalar-and-regular-three-source-extension.md)
已经支付 $C_6\in I_6$ 于整个当前 Phi，包括 $\Delta_N=0$；实际第三原乘子分母只有旧单位 $Q$。因此本条采用的 $H_{42}$ 是全原图头，不是将一个斜率补图头外推。

另外两个来源分别为
[原 D 六次式](R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md)
和
[最高原来源二十一生成元](R150-appendix-unit211-Phi-zero-whole-first-head-highest-original-NV-F6-filtered-lift-and-twenty-one-generators.md)。
此前
[两旧支持的 1634 界](R150-appendix-unit211-Phi-zero-coprime-original-highest-supports-and-1634-exceptional-weights.md)
仍保留，但本条没有重新执行它的 gcd。

本次必要定义给出的三个规范对象是：

| 支持 | $(\deg_u,\deg_Q)$ | 总次数 | 项数 | 定义 SHA256 |
|---|---:|---:|---:|---|
| $H_{42}$ | $(39,22)$ | 42 | 540 | `1988b732b97dfdded9386c97d261774e6cc4d7e8db659f211faa54961c67a8e7` |
| $H_{19}$ | $(19,11)$ | 19 | 137 | `24f31b9bac95b9e45fc2f8a5fffc1035dece82238d19f1ec5030c68e026b424d` |
| $C_*$ | $(74,49)$ | 86 | 2403 | `f2fcd6f323adaf47121341fc2e28c8af92dfba0e84dd13ed87e96f1f77081d8a` |

$H_{42}$ 从同一个 $C_6$ 的真实 $\lambda^6$ 系数提取，只剥 $u$ 一次、$u-1$ 两次、$Q$ 一次及 $\ell$ 清分母分子三次。没有使用 $\Delta_N$ 作为本次允许单位。

旧 $P_6$ 只在 runner 临时历史输入中取 $\lambda^6$ 系数，没有重算原 cofactor。旧 $C_*$ 只由已经固定的三行 adjugate 定义恢复，没有执行旧 Gaussian。

## 3. 完整 QQ 返回与有限例外集合

本次对 (1) 两对多项式作精确 QQ gcd，分别把双方除法全部乘回；两次规范 gcd 都是 1。由 (1)，两个多项式在复数域也没有共同曲线分量，故 (2) 是有限仿射集合。对总次数 42 与 19 的两个平面曲线用 Bézout，
$$
\#E\le42\cdot19=798.
$$
该界允许重交点、无穷远交点及在已排除原权面上的交点；它只是不同仿射权对的安全上界，不把模数或 scheme 长度冒充不同点数。

第二对同样给
$$
\#\{H_{42}=C_*=0\}\le42\cdot86=3612.
$$
这是另一个完整交集的界，不是把 798 换成更大的当前界。

本次还仅对新 $H_{42}$ 作完整 QQ 因式分解。实际返回有理单位 $1/28311552$、一个因子、该因子重数 1；规范化后该因子的定义恰为表中 $H_{42}$。完整乘积回到原 $H_{42}$。此处只称 QQ 不可约，不将其当作原权单位，也不额外声称复数上的绝对不可约。

## 4. 例外集合外的原有限性

若 $(u,Q)\notin E$，则 $H_{42},H_{19}$ 中至少一个非零。相应原标量 $C_6$ 或 $P_6$ 可规范为真正首一 $\lambda^6$ 关系。

原第一二次头已全图支付，所以三个均值将必要商作为 $\mathbb C[\lambda]$ 模由 $(1,T,z)$ 生成。因而加入该首一六次式后，十八个
$$
\lambda^j,\quad\lambda^jT,\quad\lambda^jz,\qquad0\le j<6
$$
生成整个必要代数，其长度至多 18。原商不要求自由，后续原值关系或原非零约束只会缩小该代数。

若另有 $\Delta_N\ne0$，已成原 N1 坐标与首一中心二次把基降为 $(1,\mathcal X)$，所以同一论证只需十二个生成元。

在 $E$ 内但 $C_*\ne0$ 的点，旧最高模型仍可给二十一个生成元；本条没有据此控制 $E\cap\{C_*=0\}$ 的完整纤维。没有把 (2) 当作所有原点的必要权条件，也没有从 (1) 宣布原点为空。

## 5. 唯一实际执行

唯一新源：
`notes/2026-11-28-unit211-Phi-zero-whole-NSPS-head-exact-H19-highest-relations-8542.py`。

- 源 blob `5883dd19438ec9ec5e55a81d3fe3a0ab3cb4f912`；
- 6279 字节，SHA256 `1d9078fbecf6f6cf7c82eb90a3a073d5924edba8c9def5926ae353fa7b25824c`；
- run `46092989625`，job `140817949161`；
- 3.881622428 秒，driver 峰值 54244 KiB，内层 exit 0；
- 源与真实 pull 后提交均为 `a526eede24c7428b781fd60f4d290bef040d7a87`；
- pull 时间 `2026-11-28T01:25:13.711675+00:00`，两份 README 无差异；
- stdout 4223 字节，SHA256 `dd21f860761450a2ead78c4ec8db9cb90c68f7415343d2b438df72501478de2c`。

两个新 gcd 分别于 3.774995478、3.827855589 秒返回；新 $H_{42}$ 完整因式与乘积于 3.838412301 秒返回。未执行旧 $H_{19}$ 因式、旧 $C_*/H_{19}$ gcd、旧 P6、Gaussian、大范数或投影。所有系数仅用于运行内计算；保存范围限源、原定义、SHA 和小回执。

附[实际小回执](../notes/2026-11-28-unit211-Phi-zero-whole-NSPS-head-exact-H19-highest-relations-execution-8542.json)。
