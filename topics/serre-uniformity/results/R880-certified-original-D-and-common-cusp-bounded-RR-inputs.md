# R880：原 D 有界代表、共同 cusp 完整空间及主函数输入已认证

## 1. 实际结论

原公开 [run 43840391925](https://github.com/Rogerhu12/math-research-public/actions/runs/43840391925)，
construct job `133207448529`，source
`3c1ddaf3c94d63aee2f9dd0bee32b6dbdeff35b9` 已实际 success。
数学核心用时 **15.559026589 秒**，保存 **28 个完成数学阶段**；
纯 IO verifier 核完 **944 个原来源成员**。

这次实际取得的是原
\[
 E_f=C+P_0+3D,\qquad \deg D=395
\]
的一组完整有界输入：

- 完整 $H^0(3H-(C+252P_0))$，维 418；
- 原残余空间 $H^0(3H-F)$，维 269，其中 $F=\operatorname{div}_{3H}(a)-D$、$\deg F=421$；
- 完整 $H^0(3H-F-123P_0)$，维 146，及其中一个准确第 123 阶为单位的原截面 $v$；
- 完整 $H^0(3H-D^*)$，维 418，其中
  $D^*=\operatorname{div}_{3H}(v)-F-123P_0$ 有效、次数 272，且 $P_0\notin D^*$；
- 原主函数 $Q_f$ 的准确单位求解表达式、除子恒等式与未缩放的原局部首项。

准确对象沿 [R880 证明](../notes/R880-original-D-pencil-reuse-and-common-cusp-RR-inputs.md)
和 [执行契约](../notes/R880-original-D-and-cusp-bounded-RR-input-execution-method.md)
定义为原来源矩阵的单位子式求解、完整关系核及投影。
保存的有限域数组是这些准确对象在指定原素点的像；
本次没有把模数组称为已经有理重构的特征零系数。

## 2. 原 place 与真实锚

本次保持 $L=\mathbb Q(b,\zeta)$ 的原 branch0：

| 字段 | 实际值 |
|---|---:|
| 辅助素数 | 1000000753 |
| 原 integral $B_{\rm fld}$ 根 | 3197390 |
| 原 $b$ 根 | 637573097 |
| 原 $s$ 根 | 99932770 |
| 原 $\zeta$ 根 | 549966761 |
| 原保留自由列 | 1186 |

R845 的原 $a,b$ 两锚在 $P_0$ 的实际模值为
\[
 a(P_0)=620415780,\qquad b(P_0)=947339000.
\]
程序因而选择原 $a$，没有交换两块，没有除以 $a(P_0)$。

新的完整 146 空间内所选 $v$ 满足
\[
 [\rho^{123}](v/\tau^3)=465210523\ne0,
 \qquad \rho=z-z_0.
\]
这个数值由真实 jet 行与完整单位核产生，原截面没有除以它作重新归一化。
完整来源保存在下述 $a$ 选择与 fixed-$v$ 阶段。

## 3. 两个完整 418 空间

### 3.1 共同 cusp 空间

程序保原两图完整 $C$ 的全部 20 个余商坐标，
再保 $\rho$ 阶 $0,\ldots,251$ 的 252 条原条件。
所得完整 $272\times690$ 矩阵实际满行秩 272，
规范自由列恒等的完整核为 418 维：
\[
 W_{D_C}=H^0(3H-D_C),\qquad D_C=C+252P_0.
\]
原 cusp 余商只按其完整 $K[z]$ 模映射消费，未把该线性余项映射假定为环同态。
既成 $C$、原 Hensel jets 与旧正规转换均未重算。

### 3.2 原 D 的有界代表

程序复用 R845 已认证的 1111 秩行列选择及五纤维原产品，
取得完整 269 关系核并投影到真实残余空间。
其 123 条原点 jet 条件给完整 146 空间，所选 $v$ 的精确阶由上一节非零值认证。

第一个整数候选
\[
 w=\sum_{j=0}^{145}U_j
\]
已在原五个完整纤维 $z=0,1,2,3,4$ 上给出
$[vV_3,wV_3]$ 的**实际秩 962**。
这是 $1360\times1380$ 矩阵的实际下界；几何上界同为 962，
因此两锚无额外共同零，像恰为完整 $H^0(6H-F-123P_0)$。

保存的 962 阶选行单位逆有双向乘回；
全部 $1360\times418$ 原关系残差为零；
第二块投影的实际独立秩为 418。
故输出确为
\[
 W_{D^*}=H^0(3H-D^*),
 \qquad D^*=\operatorname{div}_{3H}(v)-F-123P_0.
\]
有限纤维达到完整全局秩上界后才用于完整关系核判定，
没有先假设五个纤维约化或与相关除子不交。
本阶段没有单独报告新的 determinant 数值；实际单位见证是保存的选行/列、准确单位求解定义和双向逆乘回。

## 4. 原 Qf 与首项

继续使用 R872 的原准确 $u_\chi$，记
\[
 D_\chi=\operatorname{div}_{2H}(u_\chi)-272P_0,\qquad
 Q_f=\frac{(a/v)^3}{(u_\chi/\tau^2)^4}.
\]
实际输出保存
\[
 E_f-1206P_0
 =(D_C-H)+3(D^*-H)+4(D_\chi-H)+\operatorname{div}(Q_f).
 \tag{880R.1}
\]
对应可逆分式理想的主因子方向为**正乘 $Q_f$**。
原 $D,E_f$ 没有被替换成只有相同次数的任意除子。

在本次真实局部参数 $\rho=z-z_0$ 下，
\[
 Q_f=L_f\rho^{-1457}(1+O(\rho)),\qquad
 L_f\bmod 1000000753=566605368.
 \tag{880R.2}
\]
准确 $L_f$ 仍是原未缩放节点
\[
 L_f=\frac{a(P_0)^3}{v_{123}^3u_{\chi,272}^4}
\]
的来源表达式；不能将这个模值替代准确常数，也不能把 $\rho$ 自动称作原 $t$。

式 (880R.1) 同时给下一个共同 cusp 翻转消费者真实输入：
将 $D_C$ 再换成避开 $P_0$ 的有界有效代表时，必须保其准确主因子与第 252 阶首项。
该后继不属于本次已完成 28 阶段。

## 5. 准确文件身份

所有表内 SHA 均来自原输出 manifest 与实际小型 IO 读回。
未在 Git 保存原矩阵、模数组或原载体。

| 原文件 | bytes | SHA256 |
|---|---:|---|
| `p41-original-D-and-cusp-bounded-RR-inputs-certificate.json` | 18296 | `a9b24bacd5965ab387d719d70238e83c5a12dfd9b101970649b6a3f889a3c3f8` |
| `R880-exact-stages-manifest.json.gz` | 6322 | `8053fe0b34237d8b9e0ac5fde2fc0186da9317fdf132444b865ec7dc87864327` |
| `R880-common-cusp-and-252P0-constraint-matrix.json.gz` | 986214 | `b382a2ba0b35c6e4b96a70a1af23de3384019aaf93fcd796b245652bd8f1c7ae` |
| `R880-complete-common-cusp-418-kernel.json.gz` | 963130 | `6fe5b5b8f9a0433125eac34eae682f4ddcd39829af1cea1dd8bb2c213af052f7` |
| `R880-original-P0-unit-anchor-selection.json.gz` | 4823 | `ba4e1de2c230ed62e425f2b78da9afe511dc475bbcda95d8beed34e6d6fc0891` |
| `R880-standardizing-146-original-V3-basis.json.gz` | 485663 | `6bde28657c4a304ffde59347d29072d183356149102b130a1897b62c17b95c37` |
| `R880-fixed-v-section.json.gz` | 7386 | `c46a1d37745dfe6fd27d63d549a82daad81da00a4b206b71e554a8eba724dbd5` |
| `R880-trial-000001-five-fiber-rank.json.gz` | 7705 | `2b4e8b2dbed26a3afdac8219aeecaf763a8c76cad1b00926e84c15ddf1c0f8a1` |
| `R880-trial-000001-Dstar-projected-original-V3-basis.json.gz` | 1793292 | `33af46de42dde8fa39f53dadde93a72c2beb3a2304ef538e53d71fa7a0c11adc` |
| `R880-original-D-cusp-chi-principal-inputs.json.gz` | 6588 | `e31404734f964c75b902e756ad19b0f7db493d6f674cf4b84955a5a336328432` |

核心 SHA：
`ca46e8f9a9410be240ad77c0863b193e77ef701b06186a31b3edb20eb3e997a4`；
标准库 wrapper：
`3a888af1b0ff3339743a1369c416be0d85111562c167260637b4b0da1b52b630`；
实际 configuration：
`a45fbf96ab0c58b64609bbf147b2ced7c8edd16f6ac59829d3e870641380b873`。

数学证明 pin：
`5a833046b269b1682f4e6c33c6cc54b6f9d09354f0d40ccf2c47e1455747101e`；
执行方法 pin：
`529443f81c0c1b57d8dfdc80008c9e4ee7c4b6bca5f3c7f00ff64841a7a8aac2`。

原 full manifest 为 50 条、8526 bytes、
`ce5240b0e1385253ea5cce459842888f0f4e374a255f496a6d93bb54869983db`。
原 artifact `14212028755`：
`serre-R880-D-cusp-bounded-RR-inputs-43840391925-1`，
105609871 bytes，平台 ZIP SHA
`5af19f69961afba3a1d7fba8cd71e7bb9ef5d5b0b5d99b390e5aafecc2028bb3`，
到期 `2026-11-17T09:31:44Z`。

## 6. 已执行纯 IO 与准确范围

后继 [IO run 43842697439](https://github.com/Rogerhu12/math-research-public/actions/runs/43842697439)，
job `133215197880`，source `0210f90f1ac7d2c89e948cae0cdc5f64f775dc07`，
已实际 success。它核原 manifest 的 50 项 ZIP 目录身份，
只下载 **16 个所需输出加 manifest/reference**，逐 bytes/SHA 与原来源核验；
15 次 Range、5286142 bytes，没有重算数学，也没有宣称重新哈希整个 105 MB ZIP。

原 28 条完成数学 inventory 已逐项对照原 manifest，所有本次选入 stage 的 result/configuration/complete 与真实 final 一致。
小载体 `R880-intake-selected-original-sources.tar.gz`：
4294307 bytes，
`b0442fa0bb9cb6439e252d024730907a762db206888cf96b71c206dc6d42f24e`。
其 artifact `14213722649` 为 4408749 bytes，
ZIP `4f2a361dae343ad60329f158a8c211b4f0ea86d20d49c8bb22b2db8e0c61abb1`，
到期 `2026-11-17T09:46:31Z`。

本次未完成的字段在实际证书中保持 false：
其余六个 $b$ 分支各自 A/B 的 12 个右端、
五个原 $L_j$ 的 128 维 RR 空间及 144 维补空间、
原 $t$ 框架校准、连接、Poincaré period 与指定高度。
这些边界不影响上文两个完整 418 空间和式 (880R.1) 的真实完成性。
