# R606：重建 SS_j0_03 的真实 F2 高度并排除整个解析盘

日期：2026-11-14。状态：**本盘全四个坏分量已排除。**

这是旧工作区及未推队列丢失后的必要恢复。旧交接只给出余四十个分歧盘的 R472–511 批次，未保留足以核对 SS_j0_03 原编号的完整映射，所以本次使用新编号 R606，不猜原编号或旧哈希。本篇从已发布原模型、原 atlas、原 based-divisor 输入和冻结引擎实际重建，没有复算已发布 SS_j0_01、SS_j0_02 的数学结果。

## 1. 结论与完整系数

在 \(X_{\rm ns}^+(41)\) 的真正 \(\mathbb Q_{47}\) 盘 SS_j0_03，使用 R228/R231 的原射影单位参数 \(z\)，令

\[
 y=z/47,\qquad Q=47^4=4879681,\qquad F_2=27T_2+4.
\tag{606.1}
\]

同一实际规范给下列按 \(y\) 升次排列的系数：

| 对象 | 模 \(Q\) 系数 |
|---|---|
| 局部规范高度 \(\lambda_{\sigma_{F_2}}\) | `[169106, 4554253, 3077137, 1557345]` |
| 原全局式 \(G_{F_2}\) | `[3143454, 162761, 1145296, 1912994, 2387929]` |
| \(\rho_{F_2}=G_{F_2}-800\lambda_{\sigma_{F_2}}\) | `[4489722, 1882068, 3674601, 355649, 2387929]` |
| \(\rho_{F_2}/47\bmod47\) | `[22, 0, 22, 0, 0]` |

四个坏分量保持原标签 \(0,3,28,32\)，本方向的四个正确靶值都是零。于是任何可能的有理点都必须满足

\[
 22(1+y^2)=0\quad\text{于 }\mathbb F_{47}.
\tag{606.2}
\]

因为 \(47\equiv3\pmod4\)，\(-1\) 不是平方，(606.2) 无解。相同的二次判别式是 \(38\)，Euler 符号为 \(46=-1\)。因此**整个 SS_j0_03 盘在全部四个坏分量上排除**。这是有尾界的解析函数结论，不是只检查有限个实际点的插值结论。

此盘使已发布的非 CM SS 排除数由 \(41\) 增至 \(42\)，剩余 \(63\) 盘尚需恢复其完整 F2 或后续判定。固定 \(p=41\) 的最终汇总及绝对统一性主目标均不能由本条单盘结果冒认完成。

## 2. 实际点、304 位链和完整主函数

先用 `p41_SS_Abel_multiply47.py --prepare-only` 从共同次数 125 除子生成本盘自己的 based 点。该步骤保持同一个 \(f_b\)、\(f_c\)，复用已发布的秩 125 colon 证书，并在当前模型上重新核验全部保存截面的 colon 恒等式、候选空间的维数及秩 74、单点限制、半线性 Frobenius、所有求值点的不交性及实际单位条件。输出摘要为

`d35a001ff8ae9416d63c30238b6772985592acb2ead1438c32812f098f8f85b4`。

随后在未改动的 `p41_SS_Abel_with_transports47.py` 上实际运行本盘完整 304 位链。真实有符号整数仍是

\[
 m=21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072,
 \quad m^{-1}\bmod Q=4074216.
\tag{606.3}
\]

454 次 AddFlip，加初始负点和两个终点提取函数，共保存 457 个真实主函数。每个节点的完整系数、分母、整数指数和 Frobenius 均保留。写 \(C=P-b\)、\(L=\operatorname{div}(f_c)\)，则各实际除子关系和终点运输给

\[
 \Phi_C=f_{\rm final}^{-1}(v_1/f_c)
       (F_{\rm terminal}/G_{\rm terminal}),
 \qquad\operatorname{div}(\Phi_C)=mC-A_1(t).
\tag{606.4}
\]

没有删除 \(v_1/f_c\) 因子。全部 455 个整数除子关系由独立审计重放；展平表达式的最终 \(f_c\) 指数和总线束权严格为零。54 个真实 Abel 值加 54 个原第二类积分全部与独立 SS Hecke 解模 \(47^3\) 一致；另逐项核验主函数 Norm 导数加终点 tiny 积分等于 \(m\int_C\nu\)。

## 3. 完整 Norm、规定参数和中心高度

第二除子始终为原来的

\[
 D_{F_2}(P)=27T_2(P)+81u-27Z_{-8}-54c_7
                 +4P+4b+4K_{g_1}.
\tag{606.5}
\]

本盘实际生成全部三个 2-Hecke 目标和 level 标记，不能以相同粗 \(j\) 代替相同 level 点。三个目标的 1365 条保存 Weierstrass 关系已独立重放。次数 106 的完整典范商代数保留全部因子 \(8,12,26,60\)；460 个保存截面在完整商代数上的 Norm 按确切整数指数重组。固定或碰撞点保留规定局部参数及 distinguished 因子。

Norm、中心连接及多项式三个阶段使用同一个 R435 单位清极 frame。源点的切向值由原 \(dz\) 计算，基点用其原规定参数。得到

\[
 (a_b,a_P)=(433965,1706124),\qquad
 \sigma_{F_2}=(a_b/a_P)^4=733519,
\]
\[
 \log\sigma_{F_2}=2688306,\qquad
 \log\Phi_C[D_{F_2}(P)]=3350724,
\]
\[
 \int_{A_1(t)}\eta_{D_{F_2}(P)}=4632978
 \quad\pmod Q.
\tag{606.6}
\]

所以

\[
 \lambda_{\sigma_{F_2}}(P)
 =2688306+4074216(4632978+3350724)
 =169106\pmod Q.
\tag{606.7}
\]

独审还在真实数据上作 \(z\mapsto2z\)：纤维对数增加 \(4\log2\)，源点主函数 Norm 对数减少 \(4m\log2\)，两项在 (606.7) 中恰相消。中心高度不是一个依赖未记录切向尺度的数字。

## 4. 分歧整组合与本盘必要的分式替换

本盘的粗 \(j\) 剩余分歧指数为三，原射影 \(z\) 仍是单位参数。保持真实模型 \(A,B\)，写

\[
 \Delta=4A^3+27B^2,\qquad K=3BA'-2AB'.
\]

原三个含 \(j'\)、\(j\)、\(j-1728\) 的项按 R435 的函数恒等式合并为

\[
 -4\frac{j''}{j'}+\frac83\frac{j'}j
      +2\frac{j'}{j-1728}
 =\frac{10}{3}\frac{\Delta'}\Delta-4\frac{K'}K.
\tag{606.8}
\]

本盘 \(\Delta(0)=1078631\)、\(K(0)=767511\) 模 \(Q\) 均为单位。所有原 \(W\) 四阶与 \(j\) 四阶系数逐项等于 R435 证书；独审从实际 \(A,B\) jets 重新组装 (606.8)，没有对非单位 \(j'\) 作除法。

本盘还必须对两项固定连接 \(D-20b\)、\(Z_{-8}-20b\) 的分式使用真正的单位分母代表；它们的新分母在中心分别是 \(1537659\)、\(2048792\)。保存的真实截面在原支撑上消失，满足 Frobenius，并与原分式在全部 820 行上有精确交乘恒等式。相关次数界为 \(3L=378\)，低于忠实求值长度，因此这些交乘验证是函数恒等式证书，而非抽样近似。独审以整数运算重新计算了这些交乘及单位 minor。\(\eta_B\) 不需要额外替换。

实际 \(T_2\) 三分支可用源行数为 `[819,819,818]`；在真实维数 451 的 \(V_4\) 中完成单位插值并核验全部三阶系数方程。原移动连接的 Frobenius、对角留数及中心匹配同时成立。

## 5. 从微分到整个解析盘的尾界

所有阶段保持 R472 §5 已完整证明的同一个实际微分公式：

\[
 \frac{d\lambda_{\sigma_{F_2}}}{dz}
 =54T_2\eta_C(P)+8r_z(P)
   +162\eta_{u-b}-27\eta_{Z_{-8}-20b}-54\eta_{c_7-b}
   +\frac{64}{3}\eta_{D-20b}-2\eta_B+\mathcal C,
\tag{606.9}
\]

其中 \(\mathcal C\) 是 (606.8)，各微分取其 \(dz\) 系数。原 54 方向的 \(\nu\)、局部 tiny 坐标、全局二次/线性式及系数 \(-800\) 都未变。

移动 RR 逆矩阵和代数分母为整，唯一非整输入是原正规 \(\nu\) 的一次原函数。因此高度的 \(z^n\) 系数赋值至少为

\[
 -\lfloor\log_{47}n\rfloor-v_{47}(n).
\tag{606.10}
\]

对 \(n\ge4\)，有

\[
 n-\lfloor\log_{47}n\rfloor-v_{47}(n)\ge4.
\]

所以代入 \(z=47y\) 后，全部省略高度项模 \(Q\) 为零。全局形式的线性、二次系数可除性及全部 54 维装配也已核验，保证省略的 Abel 项和次数至少五的全局项不影响所列精度。以真实中心 (606.7) 积分 (606.9)，再组装 \(G-800\lambda\)，得到第 1 节。由此 (606.2) 确实约束整个盘。

## 6. 保存范围与独立审计边界

本条保存本盘 based 点、完整乘法与 Abel 终点、原第二类积分、整数主表达、真实 T2 支撑、全部 T2/典范/固定 Norm、中心、多项式、独审及每阶段检查点。457 个实际主函数加两份 manifest 的 459 文件归档，已在压缩后逐项与原始字节比较；大小 1778086 B，SHA256 为

`1c1464e82008d0287bed45cc676a1b699ae0ba5bdbfaafd7ca76cd364dda9a74`。

核心文件的摘要：

| 文件 | SHA256 |
|---|---|
| `SS_j0_03_actual_canonical_F2_height47.json.gz` | `6b863e239a1c4768b5dfbd4ca751ee2e533077b72c900ed94f17d5009f329180` |
| `SS_j0_03_actual_canonical_F2_polynomial47.json.gz` | `9c06afd88d0ec289cdb7c248a629ca3c5f2b2e47b0ed1202315e060bb28965ee` |
| `SS_j0_03-principal-F2-independent-audit.json` | `35049b25a011476e4c603dfaf1e0385608790340d2778d8a2d9ec12e7e64517e` |

实际审计范围为：全部主函数哈希、整数除子 DAG、1365 条目标 Weierstrass 关系、完整 460 因子 Norm、108 个独立积分、family1 tiny、单位切向抵消、两项固定分式交乘、R435 整组合、原 54 维全局式及剩余根。它没有第二次执行 RR、挠点表或整条长群链；这三项已经由生成引擎在本次必要恢复中实际执行。

## 7. 复现入口

全部数学引擎沿用已发布源码。manifest 保存它们和各旧输入的摘要；本次没有改动或移除任何原数学断言。默认从本次保存的真实主函数归档运行后处理：

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python topics/serre-uniformity/scripts/p41_rebuild_ramified_SS_F2_unit_parameter47.py \
  --script-dir topics/serre-uniformity/scripts \
  --disk-id SS_j0_03 --result-id R606 \
  --canonical topics/serre-uniformity/scripts/data/p41_canonical_SS_robust47_raw.json.gz \
  --canonical-certificate topics/serre-uniformity/scripts/data/p41_canonical_SS_robust47_certificate.json.gz \
  --derivative topics/serre-uniformity/scripts/data/p41_serre_clearing_126_disks47.json.gz \
  --ramified-j-certificate topics/serre-uniformity/scripts/data/p41_ramified_j_regular_height_derivative47.json.gz \
  --ramified-j-audit topics/serre-uniformity/scripts/data/p41_ramified_j_regular_height_derivative47_independent.json \
  --work-dir /absolute/fresh/R606-rebuild
```

加 `--rebuild-chain` 可从保存的 based 点再次执行真实 304 位链。此次恢复实际采用了这个开关；复现命令不另算一次已经执行的验证。

已发布的证明框架见 [R435](R435-integral-ramified-j-height-derivative-and-126-disk-frame.md) 和 [R472](R472-SS_j0_02-ramified-unit-parameter-F2-height-and-disk.md)。此条只补 SS_j0_03，后续仍按开放问题继续。
