# R887：原共同 cusp 翻转的实际执行契约

本消费者实施 [R887 证明](R887-original-common-cusp-flip-and-P0-unit-bounded-representatives.md)，其准确 SHA256 为
`1ebbc0bff297913a9a2f49a507998d49b173fe96ec6944a0e1ac81cd1295763d`。
R880 已在原公开 [run 43840391925](https://github.com/Rogerhu12/math-research-public/actions/runs/43840391925) 完成，
source `3c1ddaf3c94d63aee2f9dd0bee32b6dbdeff35b9`；
其原核心 `ca46e8f9a9410be240ad77c0863b193e77ef701b06186a31b3edb20eb3e997a4`、
certificate `a9b24bacd5965ab387d719d70238e83c5a12dfd9b101970649b6a3f889a3c3f8`、
configuration `a45fbf96ab0c58b64609bbf147b2ced7c8edd16f6ac59829d3e870641380b873`。
本文件不预先断言新的 R887 素点秩或所选截面。

## 1. 固定入口与首次完整出口

核心为 `scripts/R887_original_common_cusp_flip.py`，数学 RESULT 为
`R887-original-common-cusp-flip-and-bounded-RR-space`，FINAL 为
`p41-original-common-cusp-flip-and-bounded-RR-certificate.json`。

命令行固定为：

```text
--config EXPANDED_JOB.json --out OUTPUT_DIRECTORY --budget-minutes 300
```

所有新数学只在原公开 repository 的 GitHub Actions 执行。预算和有限试次数是运行控制；只有这两个控制、绝对目录和纯运输路线排除于数学 tag。首次试次数为 4，有限失败只表示该充分素点判据未完成。

首次完整出口同时包含：

1. 原 $J_C$ 限制到 $\tau V_2$ 的 $272\times418$ 矩阵及其完整 146 核；
2. 首个真实第 252 阶为单位、未经额外归一化的原截面 $u_C$；
3. 两个 $V_2$ 锚的真实 rank 962 证书、完整关系核及其第二块投影所给 $W_{C^*}$ 的完整 418 空间；
4. 原 $\widetilde Q_f=Q_f(u_C/\tau^2)$、准确首项表达式及原 $\rho$ 阶 $-1205$。

第 1 项不充当第 3 项。预算停止时可以只保已经完成的前缀，但 FINAL 的 `complete` 必须为 false。

## 2. 四组来源与运输闭包

新数学只读取 `R880/R845/R872/R827` 四组原件。R880 的原 tag 和 source audit 保留其历史 944 件完整来源身份；本消费者不重复传输已经被 R880 完整 $J_C$ 证书吸收的 R820、R842、R849 三组载体。

R880 的必要小件包括原 final、meta、完整输出清单/引用、阶段索引、共同约束矩阵、完整共同 cusp 核、source audit、$Q_f$ 原主函数阶段以及 $D^*$ 完整投影阶段。它们按原 producer 的 file/bytes/SHA256 绑定；来源标签不能改成 R887。

其他三组直接从本次 R880 输出原样续存的三个 source carrier 读取：

- R845：旧五个完整纤维的 $V_3$ 评价、$K^{-1}E$、23 个正规转换块及其原索引/来源；
- R872：旧完整 $V_2$ 的 $0,\ldots,272$ jets 矩阵，及原 $D_\chi$ 完整空间来源；
- R827：同原 $\zeta,b$ 素点、五个已成 cyclic 节点、原 $W$ reduction 与 source audit。

载体逐成员 bytes/SHA 核验；新 source inventory 按本次实际原件数量登记。旧 944 数量不改写为新数量。核心不重新生成旧原 Fourier 行、$S_5$ 逆、Krylov 逆、cusp Hermite 或 Hensel jets。

原 place 必须同时匹配：

| 字段 | 固定值 |
|---|---:|
| prime | 1000000753 |
| original branch | 0 |
| integral $B_{\rm fld}$ root | 3197390 |
| original $b$ root | 637573097 |
| $s$ root | 99932770 |
| $\zeta$ root | 549966761 |
| canonical free column | 1186 |

只比较 prime 不足够。各源保持原 configuration 和原 normal 整数尺度；不再次插入任何 $82$ 因子。

核心正常导入冻结 R880 源码，只复用矩阵子块、原子保存、完整单位核及投影方法。它不调用旧 Job 的完整 source guard 或旧 run，不修改模块全局常量，也不把新阶段改成旧 R880 标签。所有新 stage 使用 R887 的 result/configuration/prefix。

## 3. 272 × 418 限制、146 核与原第 252 阶

原正规位置为 $\mathcal P_m=\{(i,k):0\le k\le m-\epsilon_i\}$。
从 R880 的 $272\times690$ 原 $J_C$ 中，选取与 $\mathcal P_2$ 相同的 418 列。前 20 行完整保留原 cusp 余商，后 252 行完整保留 $\rho$ 阶 $0,\ldots,251$。

程序在附加单位矩阵的原行消元中取得一个实际 272 阶子式，保存双向逆乘回。自由列按原列次序，核的自由坐标为单位矩阵；必须核所有 $272\times146$ 残差。
准确对象定义为同一原矩阵的选行单位求解表达式，模数组只表示其本原素点约化。

然后只新增
\[
 [\rho^{252}](U_C/\tau^2)
\]
这一行与完整 146 核的乘积。原第 252 行直接读取 R872 矩阵。选择首个实际非零列，保留其原列和真实系数 $\ell_C$，不将 $\ell_C$ 除成 1。

输出 $u_C$ 的原正规 $V_2$ 坐标、选中列、原 jet 来源和准确单位求解表达式。
其除子定义为
\[
 C^*=\operatorname{div}_{2H}(u_C)-C-252P_0.
\]
次数 272、有效性和 $P_0\notin C^*$ 来自完整空间与实际单位第 252 阶，而不是单个候选的名称。

## 4. 两锚完整恢复 418

固定 $u_C$。对原完整核基 $U_j$，第 $n$ 个候选为
\[
 v_{C,n}=\sum_{j=0}^{145}n^jU_j.
\]
整数权是准确定义，不以其模值改写成另一组整数权。

在旧五纤维 $z=0,\ldots,4$ 上，利用已成 $W_z$ 和 $K_z^{-1}E_z$，只计算新的锚向量乘积
\[
 [v_z,W_zv_z,\ldots,W_z^{271}v_z]\,(K_z^{-1}E_z).
\]
固定 $u_C$ 的五个产品按固定锚身份保存，改变 $n$ 时不重复。每个新 $v_{C,n}$ 仅保存本次真正新增的五产品。所得矩阵为 $1360\times1380$。

几何上界为 962。若实际模秩达到 962，保存原行/列索引、选定单位逆的双向乘回，以及规范自由坐标恒等的 $1380\times418$ 完整核；必须核全部 $1360\times418$ 原产品残差。若秩小于 962，保留实际失败 profile，尝试下一已定义候选。

第二块投影必须实际具有秩 418；所得列先保原 $V_3$ 坐标，再用旧准确正规转换保存 normal $V_3$ 坐标。准确解释仍是原关系
$u_Cr+v_{C,n}s=0$ 的完整单位核与第二块投影。有限纤维只是秩下界证书；其达到完整全局上界后，才推出与全局关系核相同。

## 5. 原主函数、类号与首项

新阶段直接消费原 R880 的正乘 $Q_f$ 节点，不重新选原 $f$、$D$、$D^*$ 或 $D_\chi$。
保存
\[
 \widetilde Q_f=Q_f\,\frac{u_C}{\tau^2}
\]
及准确恒等式
\[
 E_f-1206P_0
 =-(C^*-H)+3(D^*-H)+4(D_\chi-H)
   +\operatorname{div}(\widetilde Q_f).
\]
可逆分式理想的主因子是**正乘 $\widetilde Q_f$**。三个有效次数 272 的代表都避开原 $P_0$。

原 R880 首项 $L_f\rho^{-1457}$ 与 $u_C/\tau^2=\ell_C\rho^{252}(1+O(\rho))$ 给
\[
 \widetilde Q_f=(L_f\ell_C)\rho^{-1205}(1+O(\rho)).
\]
程序保留 $L_f$ 和 $\ell_C$ 的准确原源表达式及两者乘积，不以一个模数值替代准确首项。
若未来真正原 $t$ 框架给 $t=c\rho+O(\rho^2)$，对应 $t$ 首项为 $(L_f\ell_C)c^{1205}$。
本次不计算 $c$，也不把 $\rho$ 改名为原 $t$。

$C^*,q_C$ 在原 $K$ 上，沿 $L/K$ 七次作用固定；这不等于从模数组宣称 $\mathbb Q$ 下降。
Norm 后 $\rho$ 阶为 $-8435$，只保存由准确恒等式推出的表达式；其余六个 $b$ 分支各自 A/B 右端仍是独立新工作。

## 6. 原子阶段、续接与完整性

新输出只在根目录使用 `R887-*.json.gz`，另有原 FINAL 和 core/run/meta。每个完成阶段先原子落盘，再检查下一阶段预算。current 保 `complete=false`，不列入完成阶段清单。

所有阶段完整绑定同一新 tag。续接逐字恢复旧完成 stage 及 current，不修改标签、不把旧 R880 阶段复制成 R887 数学阶段。历史 false FINAL 仅作旧运行回执，不约束后续已推进 current 的旧 SHA。true FINAL 则必须核其完整清单与全部当前引用。

四个独立终点字段为：

- `complete_U_C_146_certified`；
- `original_u_C_order252_certified`；
- `complete_Cstar_418_certified`；
- `original_Qtilde_order_minus1205_certified`。

只有完整 $C^*$ 的 418 空间、原主函数首项和来源链均成，才允许 `complete=true`。完整 source closure 和阶段清单由纯标准库 wrapper 核；wrapper 不导入数学 core/flint，不重复矩阵运算。

五个原 $L_j$ 的 128/144 空间、真实 $t$ 首项校准、Y 连接、Poincaré period、theta 二挠与非 $p$ 项不由本次完成。
