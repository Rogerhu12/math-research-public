# R150 Lt0：新增原 P/N 源、同根约化与三参数小行列式

日期：2026-11-27。AI-assisted GPT-6 Astra Pro；会话：Astra-ISP-8542378f-20261127。

**状态：已完成新的原恒等式及 build-only 核验，尚无实际 QQ 单位。** 这是原低次输入之后的实质新增原数据：孤立 B/C 点的完整最高式和第二矩式。不是重开作废的旧均值投影，也不把多变量 gcd=1 当作空集证明。

## 1. 新增完整同一点 P/N，先在同一原根上降幂

原 Frobenius 乘法、Gram、E0/N0 与四原低次式均从头生成，保前稿的所有乘回检查。令 r²=1−Q、eta=theta·Delta；S0 给出

$$
H=\lambda-\tfrac12,\qquad
h=H+\frac{\eta}{2(1-Q)}r,\qquad k=\bar h,
\quad\Delta=(2\lambda-3)^2-4z.
$$

这里共轭只交换同一 r 的两根，eta 同时保留在原配对和范数条件中。令 Jeta=eta²−(1−Q)Delta，源先核

$$
h^2-\left(H^2+\Delta/4+\frac{H\eta}{1-Q}r\right)
=\frac{J_\eta}{4(1-Q)},
$$
$$
h^3-\left(H^3+3H\Delta/4
+\frac{\eta(3H^2+\Delta/4)}{2(1-Q)}r\right)
=\frac{3HJ_\eta}{4(1-Q)}
+\frac{\eta J_\eta}{8(1-Q)^2}r.
$$

这是原**同一根**范数关系下的显式原倍数，不是独立取范数后混合嵌入。源生成

$$
P(K_B)-P_{02}h^3,\qquad N(K_B)-2\lambda P_{02}h^2
$$

在此同根约化后的偶部、奇部；C 点实际为相同共轭，完整保留。没有除 h，h=0 仍在输入中。两个偶部不再含 eta，两个奇部只一次含 eta。

代入原 P1 和 U 矩给出的 z=Znum/(2j²)，其分母 j=ell·k 由 Lt0 的原 P02 非零支付。所有原分母和新清分母实际乘回。四个新必要式的确切次数、项数与 SHA 由自含源逐项输出；原四式 SHA 保持。

本条登记的自含 Cramer 源包含全部上述原 P/N 重建与同根乘回，不依赖额外七变量源的运行。

## 2. 保已付矩阵首项，消去纯 lambda/f 二次单项式

在原可逆坐标 e=u−1、k=Q/e、v=4kbc·t 中，前三个原 mean 对 (lambda²,lambda f,f²) 的系数矩阵 C 满足已逐项核对的

$$
\det C=-512e(e+1)(4e-k-4)k^2(-j)^3D_3^3.
$$

全部因子是物理单位或已完整关闭的半 base 权边界。源码核对九条 C·adj(C)=det(C)I，因此可以用 Cramer 规则把纯 lambda/f 次数至少二的单项式改写为 lambda/f 总次数至多一。

本次不只报告约化结果：每个单项式递归改写同时追踪三个原 mean 的系数。对每个输入 p，源实际回乘

$$
p-\operatorname{NF}(p)=q_1E_1+q_2E_{B,+}+q_3E_{B,-}.
$$

每个有理系数的分母都按 det(C) 的因子实际剥除至常数，共检查 114 个分母；没有加入未知参数曲线的逆。

得到六条对 lambda、f 一次的必要式：原 N1elim、原 NB 偶部、原 PB 偶部、原 U 矩，以及两个原 mean 改写临界对。后两个同样有实际原组合核对，分别来自

$$
fR_{\lambda^2}-\lambda R_{\lambda f},\qquad
fR_{\lambda f}-\lambda R_{f^2}.
$$

它们不是额外假设。六条必要式可写为

$$
L_i=a_i(e,k,v)\lambda+b_i(e,k,v)f+c_i(e,k,v)=0,
\qquad i=1,\ldots,6.
$$

## 3. 二十个三参数小行列式逐个乘回原行

取六行 (ai,bi,ci) 的全部二十个 3×3 行列式。因为第三个坐标恒为 1，每个行列式有直接的多项式原行组合：若选三行 A、B、C，则

$$
\det(A,B,C)
=(b_\lambda c_f-b_fc_\lambda)L_A
-(a_\lambda c_f-a_fc_\lambda)L_B
+(a_\lambda b_f-a_fb_\lambda)L_C.
$$

源码对全部二十条身份逐项核验。因此这些行列式只含 (e,k,v)，且属于原必要理想在已付单位上的局部化。不是仅凭秩的一般位置论证，也没有漏掉某个小行列式首项零面。

每个行列式只除明确已付因子，实际乘回保留。全部余因子仍完整作为输入；即使它们的多变量 gcd=1，也不宣布空集。

## 4. 更小的真实 QQ 门

[独立自含小行列式源](../notes/2026-11-27-unit211-S0-Lt0-original-Cramer-minors-QQ-8542.py) 包含以上全部原 Gram、同根最高/第二矩、Cramer 改写追踪和二十个原行乘回。它使用

```
QQ[invUnit,v,k,e]
```

以及全部二十个必要行列式，加一个原单位饱和。饱和只包含

```
e, k, e+1, j, D3, 4e-k-4, k+4, ek-1, e-1.
```

这些依次来自原 u−1、Q/(u−1)、u、ell、bc、已闭 ell=1/2、原 T0、p≠q、已闭 a=0。没有把 eta 相关单位投影成独立范数。这里省去的其他原约束与单位只会扩大必要零集：若这个扩大系统已产生实际 QQ 单位，原图当然为空；若它未产生单位，则必须继续，不能以 gcd 或 generic 非空结论代替原返回。

此冻结源中保留了原拟用的 QQ `liftstd(...,"modstd")` 入口，但未执行 Singular。另一个七变量输入的真实 smoke 已出现内存和 tasks 错误（见下节）；因此不启动此旧入口。后续须换用官方明确列出的 `"std"` / `"slimgb"`，且小单位和完整 `matrix(I)*cert=[1]` 均实际回乘才可判空。源与 build 的哈希仍按原字节保留。

源 SHA256：

```
b03c51376eb3a972da6bbb05a523b1bacaf6290b81bb06eea094bd98df4f17d0
```

[实际 build-only 回执](../notes/2026-11-27-unit211-S0-Lt0-original-Cramer-minors-QQ-build-execution-8542.json)：exit 0，3.519411 秒，所有原乘回通过；`singularActuallyRun=false, claimExcluded=false`。

运行时生成的 Singular 输入为 1,444,073 字节，只在临时目录重算，不入仓；SHA256：

```
42333165e3802a189823c8616287afeadee2f5c9777a77f84603516b2c6cf74e
```

此前已冻结的七变量门和六变量 eta 返回源没有修改。本文件仅登记新原源、精确降次与下一实际证书输入，不登记未经执行的数学排空。

## 5. 已实际运行的旧七变量门：小证书失败，未判空

[旧低次系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-low-invariant-original-system.md)的 run `45890460154` / job `140151553412` 已收取[完整小回执](../notes/2026-11-27-unit211-S0-Lt0-low-invariant-actual-execution-8542.json)。源 SHA `05e7694122dc8ac6c94ba7a1f1093efa1ac79f00919adab1cd01f136fd27f6ba` 未变；driver 实际 1200.425908 秒、RSS 2665480 KiB、source exit 1。

准确事件顺序是：`liftstd(smoke,smokec,"modstd")` 尚未打印 smoke 通过，就先报 `no more memory`（虚拟地址约 8 GiB）和 `tasks.lib::waitTasks` 类型错误，随后 signal 11 尝试重启，smoke 变量丢失。进程后来打印完整门的 BEGIN 标志，至 1200 秒截止。**没有有效的小单位证书，也没有原系统的单位证书。** 不能将其记作一个已正常启动、只在最后超时的完整 Gröbner 计算；原数学归约不受影响，但此算法入口必须修正。

[官方 liftstd 文档](https://www.singular.uni-kl.de/Manual/latest/sing_294.htm)明确列出 `"std"` 与 `"slimgb"`，并规定变换矩阵的原乘回身份。下一输入已经实质加入原孤立点完整 P/N 和 Cramer 原组合；旧七变量输入不重跑。

## 6. 独立小证书的新执行入口及已闭的两个原零面

[整条 k=4e](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-mean-consistency-line-exclusion.md)和[整个 v=0](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-zero-singleton-pairing-exclusion.md)已各自完成原方程证明，因此新门可合法剥除 4e−k，并把 v 加入单位乘积。原二十个子式的剩余因子全部保留，改写及所有原行乘回仍实际核验。

[新自含安全入口](../notes/2026-11-27-unit211-S0-Lt0-original-Cramer-minors-safe-smoke-slimgb-QQ-8542.py)的 SHA 为 `6cb8a264fd87d7020c868784d76e01c2b6283d655f5c8fec92292870765007c2`。Python 先独立运行 45 秒/8 GiB 限额的 `std` 小单位进程，必须退出0、准确打印回乘通过且没有 Singular 错误诊断；未通过时完整输入文件不会写出，大门不会启动。通过后才运行完整 `slimgb`，1200 秒/8 GiB，仍必须真实 `matrix(I)*cert=[1]` 且退出0。

[实际 build-only 回执](../notes/2026-11-27-unit211-S0-Lt0-original-Cramer-minors-safe-smoke-slimgb-QQ-build-execution-8542.json)为 exit0、3.245212 秒。完整输入 1,425,935 字节、SHA `5d20ee9a067136fdc2db4b4ca634b9e27c7769ee062cbd703102c6b4c7879dd8`，只在临时目录重算。专用 workflow `invariant-subspace-Lt0-original-minors-safe-8542.yml` 固定源提交/Git blob 并复用实际 pull/规则差异驱动；运行回执另记。此时仍未判整个 Lt0 为空。

## 7. 独立 smoke 已通过，原四变量门实际超时；转入新增 Dixon 约束

run `45894728421` / job `140165703666` 的[真实回执](../notes/2026-11-27-unit211-S0-Lt0-original-minors-safe-actual-execution-8542.json)确认：独立 `std` 小进程退出0、32字节准确通过标志、无 Singular 诊断；之后才启动完整 `slimgb`。完整门实际1200秒到时，仅输出 BEGIN 标志，无单位证书。driver 1204.387020秒、峰值RSS 8216876 KiB、source exit1，输入 SHA 与冻结的 `6cb8a264...` 源相符。这次与旧七变量的 smoke 崩溃明确区分；不重跑同一四变量输入。

后续已独立证明[原v首项零面排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-original-v-leading-zero-exclusion.md)，并在其中逐项验证原三 mean 的 Dixon 组合。新门实质增加 D8 必要约束及已闭 Omega、B44 单位；并非只更改时间或变量顺序。

[新增原 Dixon 安全源](../notes/2026-11-27-unit211-S0-Lt0-original-Dixon-paid-leading-safe-slimgb-QQ-8542.py) SHA为 `dc2d1c5bdd4a2ad3558d96f4102f975326a73cb6f249b5814c68b79d13a9c385`。[实际 build 回执](../notes/2026-11-27-unit211-S0-Lt0-original-Dixon-paid-leading-safe-slimgb-QQ-build-execution-8542.json)为exit0、3.998890秒：177个分母、Dixon系数原组合和全部子式/首项分解通过。21条原必要式加一个饱和，生成输入1,476,118字节、SHA `5088e291edcd168e852f93c8d4c7127203bd65c6d25d44a7cb1bf8641cb5fc2e`。继续独立45秒std小证书、1200秒slimgb及真实原乘回；专用 `invariant-subspace-Lt0-Dixon-paid-leading-8542.yml` 固定该新源，实际结论另记。
