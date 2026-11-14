# R472 — SS_j0_02 的原单位参数、真实 F2 高度与整盘判定

## 1. 实际结论

在 $X_{ns}^{+}(41)$ 的真正 $\mathbf Q_{47}$ 圆盘 **SS_j0_02**，保持 R228 原射影参数 $z$，令 $y=z/47$、$Q=47^4=4879681$。本条重新执行该盘自己的完整 304 位主函数链，再完成 $F_2=27T_2+4$ 的全部 Norm、规范纤维、中心连接、移动 RR 与整盘积分。按 $y$ 升次序，实际得到

| 对象 | 模 $Q$ 系数 |
|---|---|
| $\lambda_{\sigma_{F_2}}$ | `[2165008, 1850531, 24299, 2284106]` |
| $G_{F_2}$ | `[2644878, 1969347, 3026048, 229736, 1453522]` |
| $\rho_{F_2}=G_{F_2}-800\lambda_{\sigma_{F_2}}$ | `[2925233, 87890, 3105572, 2825311, 1453522]` |
| $\rho_{F_2}/47\bmod47$ | `[11, 37, 41, 0, 0]` |

对全部 47 个剩余值求值均非零，故整个盘在四个坏分量上全部排除。 其二次判别式为 35，Euler 符号为 46。

这里四个正确坏分量标签仍为 $0,3,28,32$，它们的 F2 靶值均为零。上表来自整个解析盘的系数与尾界，非有限点插值。这里只结算本盘；其他盘及绝对 Serre 一致性主目标仍开放。

## 2. 真实中心与分歧参数

源点参考纤维为 0，原行号 471、Hecke 顶点 1（均零基）。其实际物理模型 $(A,B)$ 为 `[[4821260, 0], [2203622, 0]]`，$j=1038230$。原 atlas 的全部 73 坐标在四位精度逐项匹配，并满足半线性 Frobenius。物理单位参数 `A-A_reference` 的实际值为 `[0, 0]`；源射影坐标方程的前四项为 `[[0, 0], [4539485, 0], [3139726, 0], [1572089, 0]]`，一阶项是单位。

粗 $j$ 映射在本盘的剩余分歧指数为 3。本盘不是具有非平凡稳定子的 CM3/CM4 粗局部图；原射影 $z$ 仍是单位参数。$j$ 的实际前五项为 `[1038230, 1829052, 3286616, 502065, 4586513]`。我们不对非单位 $j'$ 作整环除法。

在上述真实模型上重新提升全部 2 挠核、执行 Vélu，并用完整 1681 点表重算原始 41 层运输。每一分支保存全部 73 个四位坐标，146 个射影剩余坐标与原 Hecke 图一致；目标为：

| 分支 | 参考纤维 | 项链标签（一基） | 图顶点（零基） |
|---:|---:|---:|---:|
| 0 | 44 | 736 | 2762 |
| 1 | 44 | 502 | 2761 |
| 2 | 44 | 644 | 3029 |

Frobenius 置换为 `[1, 0, 2]`。三个实际 level 目标均与源点分离；微分迹保留 $1/2$ 尺度。相同粗 $j$ 并未被当成相同 level 点。

## 3. 全部实际主函数与完整 Norm

令 $C=P-b$、$L=\operatorname{div}(f_c)$，$\deg L=126$，$V_1,V_2,V_3$ 的维数为 $73,199,325$。原始 based divisor 的秩 125 colon、维数 74 候选空间、一点条件和完整 Frobenius 均实际求得；$f_b(P)$、$f_c(P)$ 为单位，且初始代表与原 820 求值纤维不交。

实际有符号整数为

$$m=21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072,\qquad m\equiv9\pmod{47}.$$

全部 454 次 AddFlip 到达 304 位终点，共保存 457 个实际主函数：初始负点、454 个群运算和两个终点提取函数。所有截面的完整系数、分母 $f_c^d$、实际节点及整数指数均保留。若 $D_T=E_T-L$，每一步满足

$$\operatorname{div}(F/f_c^3)=D_P+D_Q+D_R,\qquad
f_R=(F/f_c^3)/(f_Pf_Q).$$

秩 145 的终点运输以及全部 $820\times73$ 条理想等式给原 family1 的实际微小除子 $A_1(t)$，$t\in47R_2^{54}$。保持真实 $v_1/f_c$ 因子后，

$$\Phi_C=f_{\mathrm{final}}^{-1}(v_1/f_c)(F_{\mathrm{terminal}}/G_{\mathrm{terminal}}),\qquad
\operatorname{div}(\Phi_C)=mC-A_1(t).$$

独立整数审计重放全部 455 个非形式除子关系；展平表达式的最终 $f_c$ 指数和总线束权严格为零。全部 54 个 Abel 值和 54 个原第二类积分均与独立 SS Hecke 解模 $47^3$ 相等，且逐项核验真实主函数 Norm 导数加 tiny 等于 $m\int_C\nu$。

第二除子为

$$D_{F_2}(P)=27T_2(P)+81u-27Z_{-8}-54c_7+4P+4b+4K_{g_1},$$

其次数为零。三个 T2 目标实际执行全部 $3\cdot455=1365$ 条 Weierstrass 除法及四个完整 $73$ 维理想关系，得到 Norm `1543023`、对数 `3404304`。candidate18 的完整次数 106 典范代数因子次数为 $8,12,26,60$，所有 460 个保存截面均在完整商代数上为单位；实际 canonical Norm 为 `3139195`，对数 `4385946`。

24 个固定或碰撞点采用明确规定的局部参数：源点 $P$ 用原 $z$，基点 $b$ 用已处理 CM3 粗图的 $j-j(b)$，其他固定点保留原有效参数。所有四个完整理想在这 24 点实际核验，碰撞处保留 distinguished 因子及首项。加权固定对数为 `2836121`，因此

$$\log\Phi_C[D_{F_2}(P)]
=27(3404304)+4(4385946)+2836121
=63450\pmod Q.$$

独审重新组合完整 106 Norm 的 460 个因子和准确整数指数，并核算固定对数的加权和；它没有声称另一次重放所有 24 点的几何矩阵。原引擎则已实际验证这些矩阵和 Weierstrass 条件。

## 4. 同一单位参数中的规范纤维和中心

在 $P$ 的原 R228 frame 与坐标中，令

$$a_P=\frac{W(P)g_1}{H_c(P)}=\frac{g_1}{dz}(P),\qquad
 a_b=\frac{g_1}{dj}(b).$$

此处 $H_c(P)$ 为单位，所以 $a_P$ 的计算不需要 $j'^{-1}$。Norm 与中心连接两个引擎均明确绑定同一原 frame、同一坐标及同一参数，实际得到

$$(a_b,a_P)=[433965, 615825],\quad
 \sigma_{F_2}=(a_b/a_P)^4=1227090,\quad
 \log\sigma_{F_2}=4121900.$$

第三类连接由原 $\nu$ 梯度、全部有限极留数和完整尖点域条件求出；原 54 个 family2 条件实际核验。固定超奇异支撑仅对完整 Frobenius 稳定集合使用已有的实部总和。沿该盘自己保存的 54 个 family1 参数积分，得到

$$\int_{A_1(t)}\eta_{D_{F_2}(P)}=2322599.$$

这些校准点的 $j$ 参数和全部分母仍为单位；源点使用 $z$ 不会改变校准路径上的真实连接。于是

$$\lambda_{\sigma_{F_2}}(P)
=4121900+m^{-1}(2322599+63450)
=2165008\pmod Q.$$

若在源点再取任意单位线性换参 $t=cz$，则 $a_{P,t}=a_{P,z}/c$，纤维对数增加 $4\log c$；主函数在源点的阶为 $m$，第二除子的源点重数为 $4$，故完整 Norm 对数减少 $4m\log c$。两者在高度中严格抵消。本条独审对真实数据取 $c=2$，重新计算两项并核验总高度完全相同。

## 5. 分歧 $j$ 项的整相消与整盘公式

所有阶段显式使用 R435 的共同单位清极截面，在 126 个非稳定子有理盘及全部 820 原求值点为单位；其真实 21 极条件、59860 导数值及新旧 frame 交乘已有独立证书。该辅助清极截面不替换原 R228 的局部参数。

对原参数的导数记撇号，设

$$\Delta=4A^3+27B^2,\qquad K=3BA'-2AB'.$$

在本盘，$\Delta,K$ 都是单位。R435 的有理函数恒等式为

$$j=\frac{6912A^3}{\Delta},\quad
j-1728=-\frac{46656B^2}{\Delta},\quad
j'=\frac{186624A^2BK}{\Delta^2},$$

因而三个分歧项必须合并为

$$\mathcal C=-4\frac{j''}{j'}+\frac83\frac{j'}j+2\frac{j'}{j-1728}
=\frac{10}{3}\frac{\Delta'}\Delta-4\frac{K'}K.$$

右边只逆单位。本次独立从实际 $A,B$ jets 重算 $\Delta,K$ 与 $\mathcal C$，其前三项模 $47^3$ 为 `[22154, 6963, 98663]`；全部原 $W$ 四阶与 $j$ 四阶系数也逐项等于 R435 证书。独审重新计算这两个单位对数导数，而非只读取成功标记。

真实移动两极点连接取 $g_C(z)=g_C(0)+\int_0^z\nu$；colon 秩 124，820 个忠实源行、2868 条三阶参数方程全部成立。实际 T2 三阶迹在 820 个公共源点通过，各分支可用数为 `[820, 820, 820]`，在真实维数 451 的 $V_4$ 中重建。保持相容连接的完整公式：

$$\frac{d\lambda_{\sigma_{F_2}}}{dz}
=54T_2\eta_C(P)+8r_z(P)
+162\eta_{u-b}-27\eta_{Z_{-8}-20b}-54\eta_{c_7-b}
+\frac{64}{3}\eta_{D-20b}-2\eta_B+\mathcal C.$$

各微分在式中以其 $dz$ 系数表示。右端的 $8r_z+\mathcal C$ 是原正规项与三项 $j$ 换参的准确总和。原含 $j$ 分母的等式在稠密开集成立，而合并后两边均为整解析微分，故延拓到本盘全部点。没有独立去除任何极项。

本盘所有固定连接及 $\eta_B$ 的原分母实际已为单位，无须另换分式。移动 RR 逆矩阵和其余代数分母为整；唯一非整输入是原正规 $\nu$ 的一次原函数。因此 $z^n$ 高度系数的赋值至少

$$-\lfloor\log_{47}n\rfloor-v_{47}(n).$$

对每个 $n\ge4$，有 $n-\lfloor\log_{47}n\rfloor-v_{47}(n)\ge4$，故代入 $z=47y$ 后所省全部高度项模 $Q$ 为零。完整 54 维全局二次/线性形式的可除性亦独立核验，保证 Abel 的省略项及次数至少 5 的项不影响本精度。按实际中心积分右端、重新装配 $G-800\lambda$，即得第 1 节。

## 6. 保存内容与复现

本条 459 文件主函数归档与每个原始文件逐字比较；压缩大小 1772587 字节。完整源码、真实支撑、所有 Norm、第二类与中心连接、整盘系数、实际独审和每条旧输入均由 manifest 的大小及 SHA256 绑定。

| 文件 | SHA256 |
|---|---|
| `SS_j0_02_actual_canonical_F2_height47.json.gz` | `7594ed7c4afe05297635776f777c5dd598c62e087561b8ed1fd6dad82b4430c9` |
| `SS_j0_02_actual_canonical_F2_polynomial47.json.gz` | `8f1283b79e62d441c08f7a7a164eb265114068bd759b9e72681ce75ca5fa81b8` |
| `SS_j0_02-principal-F2-independent-audit.json` | `30489ccd3d3464b063396a7e259a6e8822d000356271d43ea260f9ec8f38aa8b` |
| `p41_SS_j0_02_principal_transports47.tar.gz` | `71aede6c5b0db8b2c1b9f06a834a221126184a04a065e77010edddec393911d8` |

七个后处理阶段和完整长链均已实际执行。独审范围包括主函数哈希、整数除子 DAG、1365 条目标 Weierstrass 关系、完整 460 因子 Norm、108 个独立积分、tiny、两处单位换参抵消、R435 整组合、54 维全局式及全部根；不声称第二次运行 RR、挠点表或长群链。

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python topics/serre-uniformity/scripts/p41_rebuild_ramified_SS_F2_unit_parameter47.py \
  --script-dir topics/serre-uniformity/scripts \
  --disk-id SS_j0_02 --result-id R472 \
  --canonical topics/serre-uniformity/scripts/data/p41_canonical_SS_robust47_raw.json.gz \
  --canonical-certificate topics/serre-uniformity/scripts/data/p41_canonical_SS_robust47_certificate.json.gz \
  --derivative topics/serre-uniformity/scripts/data/p41_serre_clearing_126_disks47.json.gz \
  --ramified-j-certificate topics/serre-uniformity/scripts/data/p41_ramified_j_regular_height_derivative47.json.gz \
  --ramified-j-audit topics/serre-uniformity/scripts/data/p41_ramified_j_regular_height_derivative47_independent.json \
  --work-dir /absolute/fresh/R472-rebuild
```

默认复用真实主函数归档并运行全部后处理；加 `--rebuild-chain` 重新执行 304 位链。这个便携入口已核语法和各阶段路径，未声称它又重复执行了整条已完成长链。
