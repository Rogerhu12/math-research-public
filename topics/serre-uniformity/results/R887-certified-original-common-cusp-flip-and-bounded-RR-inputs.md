# R887：共同 cusp 翻转、完整 C*418 空间及原主函数 −1205 首项已认证

日期：2026-11-16。会话：serre-public-astra-20261115。

**本项已实际完成。** 原公开
[run 43844745726](https://github.com/Rogerhu12/math-research-public/actions/runs/43844745726)，
construct job **133222108178**，source
**85049ecab0b62dd5e7a3983841844ddee52b3da4**，于
2026-11-16T10:00:20.712476Z 成功结束。核心用时 **12.558248493 秒**，
20个完成数学阶段、388个原来源成员均通过实际 verifier。

本次将原共同部分 \(D_C=C+252P_0\) 翻转为一个次数272且避开原 \(P_0\)
的有效除子 \(C^*\)，取得完整418维 \(H^0(3H-C^*)\)；
同时保存原 \(\widetilde Q_f=Q_f(u_C/\tau^2)\) 的准确来源表达式、
除子恒等式和阶 \(-1205\) 的首项。完整146核、所选截面和完整418空间
各有独立真完成标志。

## 1. 原对象和准确系数语义

本项直接接
[R880 的真实 D*/共同 cusp 空间](R880-certified-original-D-and-common-cusp-bounded-RR-inputs.md)、
[R887 证明](../notes/R887-original-common-cusp-flip-and-P0-unit-bounded-representatives.md)
和 [执行契约](../notes/R887-original-common-cusp-flip-execution-method.md)。
原 \(Y/K\)、\(K=\mathbf Q(\zeta)\)、\(g=127\)、\(\deg H=272\)、
原 \(P_0\) 及完整20次 cusp 除子 \(C\) 均不改变。需要原
\(D,E_f\) 的恒等式时，沿 \(K\hookrightarrow L=K(b)\) 忠实扩张。

准确空间由原来源矩阵的单位选行解、完整关系核与投影定义；
已保存有限域数组是其指定原素点的实际像。本次没有把模 kernel
改称已展开的特征零有理系数。所选单位子式及几何准确维数共同保证
特征零空间完整，全部规范自由列保持原值。

本次仍是辅助素数
\[
 \ell=1000000753,\qquad \zeta=549966761,\qquad s=99932770,
\]
原 \(b\) branch0、\(B_{\rm fld}=3197390\)、free1186。
没有混用另一 \(\zeta\) 嵌入的纤维矩阵。实际参数为
\(\rho=z-z_0\)，来源字段保 `z_minus_z0`。

## 2. 真实146核和未缩放的 uC

原 R880 的 \(272\times690\) 完整矩阵 \(J_C\)，含原 cusp
余商的20个坐标以及 \(P_0\) 的0至251阶条件。
沿原正规位置仅选出 \(\tau V_2\) 的418列，所得准确限制图满足
\[
 U_C=\ker(J_C|_{\tau V_2})
     =H^0(2H-C-252P_0),\qquad \dim U_C=146.
 \tag{887R.1}
\]
本次实际核得满行秩272、完整146核及全部 \(272\times146\) 残差，
没有重算原 cusp 余商或 Hensel jets。

原 R872 的 \(V_2\) jet 矩阵已有0至272阶。
读取第252行作用于新完整核，**第0列**即为首个实际单位列，
取它为 \(u_C\)，其原首项为
\[
 \ell_C=[\rho^{252}](u_C/\tau^2),\qquad
 \ell_C\bmod\ell=\boxed{207667877}.
 \tag{887R.2}
\]
截面没有除以207667877或其准确提升作重新归一化。
其准确身份是指定规范核的第0列；这个非零模值认证该准确截面的
阶恰为252。

定义
\[
 C^*=\operatorname{div}_{2H}(u_C)-C-252P_0,\qquad
 q_C=u_C/\tau^2.
\]
则
\[
 C^*\ge0,\qquad \deg C^*=272,\qquad P_0\notin C^*,
 \qquad
 D_C-H=-(C^*-H)+\operatorname{div}(q_C).
 \tag{887R.3}
\]
原共同 \(252P_0\) 进入 \(q_C\) 的真实零阶，没有被删去。

## 3. 首个两锚试次实际给完整 C*418

令 \(U_0,\ldots,U_{145}\) 为已成规范核基。本次整数参数 \(n=1\)，即
\[
 v_C=\sum_{j=0}^{145}U_j,
\]
已经通过充分判据。原五个完整纤维 \(z=0,1,2,3,4\) 上的新乘积
\([u_CV_3,v_CV_3]\) 构成 \(1360\times1380\) 矩阵，**实际秩962**。

几何上，若两锚有额外共同零 \(Z\)，准确秩为
\(962-\deg Z\)。因此这个实际下界与全局上界夹逼，证明 \(Z=0\)
以及像恰为完整 \(H^0(5H-D_C)\)。
无需先假定五纤维约化或与相关除子不交。

程序保存真实962阶选行/列、单位逆的两侧乘回、
完整 \(1380\times418\) 关系核，并核全部
\(1360\times418\) 原纤维残差。对
\[
 u_Cr+v_Cs=0,\qquad r,s\in V_3
\]
投影到第二块 \(s\)，取得完整
\[
 \boxed{W_{C^*}=H^0(3H-C^*),\quad\dim W_{C^*}=418.}
 \tag{887R.4}
\]
投影的418独立性也已实际核。最终输出保原 \(V_3\) 坐标及原 normal
转换来源；这一步没有用146列冒充418列。

本次 actual profile 不另报告一个新的 determinant 数值。
其单位见证是所存选行/列、双侧逆乘回和完整关系核，
不能从秩962补写未输出的 determinant。

## 4. 原主函数方向与真实首项

原 R880 的 \(Q_f\)、\(D^*\)、原 R872 的 \(D_\chi\) 均继续使用其
准确未缩放来源。令
\[
 \widetilde Q_f=Q_fq_C=Q_f(u_C/\tau^2).
\]
实际原输入保存
\[
 \boxed{
 E_f-1206P_0
 =-(C^*-H)+3(D^*-H)+4(D_\chi-H)
      +\operatorname{div}(\widetilde Q_f).}
 \tag{887R.5}
\]
可逆分式理想中的主因子为**正乘 \(\widetilde Q_f\)**。
三个有效272次代表 \(C^*,D^*,D_\chi\) 都准确避开原 \(P_0\)；
原 \(E_f=C+P_0+3D\) 没有换成任意等次数除子。

R880 已给
\(Q_f=L_f\rho^{-1457}(1+O(\rho))\)。
本次准确首项来源是原 \(L_f\) 节点与 (887R.2) 的乘积：
\[
 \widetilde Q_f=(L_f\ell_C)\rho^{-1205}(1+O(\rho)),
 \qquad
 (L_f\ell_C)\bmod\ell=\boxed{267133051}.
 \tag{887R.6}
\]
实际源保持两个原因子，不用模值代替准确常数。

同一 \(K\) 上构造的 \(C^*,q_C\) 被原 \(L/K\) 七次 Galois 作用固定。
因此准确 norm 除子接口为
\[
 \sum_\sigma E_f^\sigma-8442P_0
 =-7(C^*-H)+3\sum_\sigma(D^{*\sigma}-H)+28(D_\chi-H)
   +\operatorname{div}N_\sigma(\widetilde Q_f),
 \tag{887R.7}
\]
其中原 \(\rho\) 阶为 \(-8435\)。
该恒等式不表示其余六个 \(D^{*\sigma}\) 的矩阵已经求出。

若后继使用已认证的原 \(t=c\rho+O(\rho^2)\)，准确 \(t\) 首项为
\((L_f\ell_C)c^{1205}\)。R887 本 run 的
`original_t_frame_value_computed` 仍为 false；
原 R883 的 \(c\) 是独立成功源，后继须显式绑定它并保这个正乘方向，
不能改写本历史配置或据此假称本次已算该乘积。

## 5. 实际完成文件及来源身份

| 原文件 | bytes | SHA-256 |
|---|---:|---|
| `p41-original-common-cusp-flip-and-bounded-RR-certificate.json` | 9250 | `c5fa30c7eea59b69de723ea82fd41a05e9536120c49d2b144d4fef831cb1b8bf` |
| `R887-original-418-column-restriction.json.gz` | 572833 | `94a290794b16b1e24311e69cf326fc1480bd8c53044bc61e7d42a5fbaa6b7fbb` |
| `R887-complete-U_C-146-kernel.json.gz` | 582779 | `9560f75a80868ad50b101f0a104f846a22abf9d2b9f8bae09a172ef76882930d` |
| `R887-original-order252-functional-and-u_C.json.gz` | 6077 | `2cf2fa29756489aacde22b338a5f51d7e8f18150d3ea30e589424ec0574b53cb` |
| `R887-trial-000001-v_C.json.gz` | 5106 | `af69bf8e3e44f5311efc698d3cf85c95c5bcae7abca2b3c527da9d4d0d2a3df6` |
| `R887-trial-000001-complete-pencil-profile.json.gz` | 6157 | `9d15d1ecbc1392bf122b4c840820c4d11920b801ce48ec7f41e272ba919c81c6` |
| `R887-trial-000001-Cstar-projected-original-V3-basis.json.gz` | 1791675 | `86e007e9becb33296144c0767945adbacbf88c8148e16a67b6883b1b72b84c73` |
| `R887-original-Cstar-and-Qtilde-principal-inputs.json.gz` | 4098 | `e95532c259b62ddacf9ad0de19c099c4eea87a072449638b02384557182acd9f` |
| `R887-original-source-audit.json.gz` | 3370 | `81a4b452e0c090a112c2c1fe13932cd259cdbd5a6849a4d833297b1e30919c19` |
| `R887-exact-stages-manifest.json.gz` | 4380 | `e043bb183f7485e833b2f226379ef052cc1c20116438336e05f0d8e207a99d25` |
| 全输出 manifest，38项 | 6525 | `05d289d0727952a451f421385cc37b1e54933cd6d2a5038caeafbcac02d5c1d2` |

实际配置指纹：
`d325dc06b7328796467d98cce13cde4c52d90aed4fc697fc2d80a422e7d63b6a`。

冻结源码与方法：

- [核心](../scripts/R887_original_common_cusp_flip.py)，28337B，
  `d469ef046e8575eaed34e5670275f80554edf8cdae723ef3fb029b979e07508c`；
- [纯 IO 包装器](../scripts/R887_public_original_common_cusp_flip.py)，38383B，
  `78a00876c4ecc7309df237de6457068745c65e5b6e65e226db0ce1d362f0cf7e`；
- [证明](../notes/R887-original-common-cusp-flip-and-P0-unit-bounded-representatives.md)，
  `1ebbc0bff297913a9a2f49a507998d49b173fe96ec6944a0e1ac81cd1295763d`；
- [执行方法](../notes/R887-original-common-cusp-flip-execution-method.md)，
  `ae992344dc1305012fe69229d201fa807b84ad96456f97d6cd826accaafb128a`。

本次最小来源闭包是 R88018件、原 R84550件、原 R872307件、
原 R82713件，共388件。旧944件完整来源身份保存在原 R880 tag和审计中；
本消费者没有重新运输已经不需要的 R820/R842/R849 三组载体，
也没有更改旧944记录。

## 6. 一日留存及纯 IO 读回

原 artifact **14214842060**，名称
`serre-R887-common-cusp-flip-43844745726-1`，
81369157B，平台 ZIP SHA-256
`1f44a5cadfad375521263f9d2241a7bbf000786f4852a81f48777a0e3526824b`，
到期2026-11-17T10:00:20Z。

随后纯 IO
[run 43846120888](https://github.com/Rogerhu12/math-research-public/actions/runs/43846120888)，
job133226674819，source
`aaddadb00929b355bc93db1ea869642ecbf59a6e`，
读取14个必要原输出及 manifest/reference，共16个原件。
14次 Range 传输3116227B；所有选择原件逐 bytes/SHA 核验，
完整20阶段索引和同一数学配置已核。没有下载或声称重哈希整个81MB ZIP，
没有导入或执行数学核心。

小载体 `R887-intake-selected-original-sources.tar.gz`：
2989109B /
`67a2313e3674a8df215fe74e08482fe5ebf3da3685388284be40387da71b2712`。
该 IO artifact14214599213 为3057098B /
`edd857bf98ec5b73328107b49da96af89e2e52916f6cb0a4a00f5fe7c2d2843d`。
原矩阵、模数组与载体只留一日 artifact，不入 Git。

## 7. 本次关闭的缺口

共同 cusp 块现在已有避开原 \(P_0\) 的完整272次有效代表、完整418空间、
准确单位求解来源和原主函数首项。因重复使用 \(C+252P_0\) 而产生的
固定252阶零已通过正乘 \(q_C\) 明确转入主函数，后继可以直接消费
(887R.4)–(887R.7)。

其余六个同 \(s\) 分支的 A/B normal 输入、各自的 \(D^*\) 与五个原
\(L_j\) 的128/144空间继续按真实来源逐项构造。本结果不把原
Poincaré、theta刚性化、连接或高度标记为完成。
