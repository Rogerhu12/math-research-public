# unit211 紧凑原均值的对偶二重点平方错误：精确更正与依赖隔离

- 日期：2026-11-28（Asia/Taipei）。
- 会话：Astra-ISP-8542378f-20261127。
- 状态：原定义错误已确认；本稿修正恒等式并撤回依赖错误恒等式的原题推论。未证明普通不变子空间问题完成。
- 新证书：`2026-11-28-unit211-corrected-dual-germ-compact-original-identities-8542.js`，SHA256 `a7f1db4305a58c2e733c573158f746d5b4adc312090472de25e472c96ddfeaae`，7228 字节；实际回执见同 basename 的 `-execution.json`。

## 1. 错误在原代数乘法，不在后续精确矩阵运算

原 $2+1+1$ 代数的乘法是
$$
\operatorname{vm}(v,w)
=(v_0w_0,\ v_0w_1+v_1w_0,\ v_Bw_B,\ v_Cw_C).
$$
特别地
$$
\operatorname{vm}(d,d)_1=2d_0d_1.
$$
记原四行 Gram 为 $g_j$，$d=DK(1)$，$F_2=\tau(d)$，则真实四个均值为
$$
E_j=e_j-2(DK(d))_j-2\operatorname{vm}(d,d)_j+2F_2d_j,
$$
其中 $e_1=2\tau(\operatorname{vm}(g_0,g_1))$，其余三个 $e_j=\tau(\operatorname{vm}(g_j,g_j))$。

两份旧紧凑 JavaScript 源错误地对全部 $j$ 使用了 `-2*sq(dv[j])`。这在二重点的一阶坐标 $j=1$ 将 $-4d_0d_1$ 换成了 $-2d_1^2$。在同一原 Gram 中
$$
d_0=u,\qquad d_1=2f-V-(1-\ell)u,
$$
故确切差式是
$$
\boxed{E_{1,\mathrm{bad}}-E_{1,\mathrm{true}}
=4ud_1-2d_1^2=2d_1(2u-d_1).}
$$
这不是可忽略的非零尺度，也不能由旧均值理想自动删去。

## 2. 最早来源和已确认的直接消费者

以下时间是 GitHub 返回的发布提交 `commit.committer.date`（UTC）。

| 身份 | 文件与哈希 | 最早已核提交 |
|---|---|---|
| 两均值错误源 | `2026-11-27-unit211-compact-two-means-original-integer-identities-8542.js`；blob `85a0057e9dafd13433e9e8908c0710bebe8c21aa`；SHA256 `b770f2f4f74af468f5348363a7a245534bb78c6329a645f4f81fb8cbd87bc3a5` | `968dae1ec89a5d5526a3ed6ebfac88bf18e09b00`，2026-11-27 15:13:10 |
| 四均值与 N1 错误源 | `2026-11-27-unit211-compact-all-means-N1-original-integer-identities-8542.js`；blob `94b2be74c729ee76e239491d8e967dc9c41044b0`；SHA256 `9ab0270fe53a0a6f169755f92f731e6cf636f1d9b7a9e12364ef487a01cdea6e` | `155846f67d9fff97adba79dfb57ddb1cf16ade78`，2026-11-27 15:16:43 |

第一次提交同时加入 `2026-11-27-unit211-Phi-zero-general-compact-scalar-means-original-input-8542.py`，这是已经核到的最早直接 Phi 消费者。该提交同时发表的 R271 Haar 结果不使用这个代数恒等式；不得因同一提交日期把它一并撤回。

第二次提交同时加入 [旧紧凑恒等式结果](../results/R150-appendix-unit211-compact-original-scalar-means-and-N1-identities.md)，以及 `2026-11-27-unit211-equal-singleton-global-compact-original-three-column-cofactors-8542.py`。后者是根会话碰撞图的直接消费者；其沿错误均值产生的后续原题结论也必须按依赖隔离，不能仅隔离 Phi 文件。

已全文确认的主要 Phi 输入为 `2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，blob `e6d789552dd958e63269ecb6e1f01e3605ff2eff`，SHA256 `100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf`。它直接写入错误 $\overline R$，再据此生成二次头、三条规则和真实乘法的旧宣称。因此该来源之后的原必要性不能继续使用。

上述是确证的直接链，尚未穷尽每个历史结果的单位依赖。尚未分类的结果须逐条按来源检查，不按文件日期笼统判定有效或无效。

## 3. 同一原 Gram 中的修正恒等式

保留旧变量
$$
\ell=b+c,\quad a=1-\ell,\quad p=1+\rho,\quad q=1-\rho,
\quad Q=1-\rho^2,\quad u=bp+cq,
$$
$$
V=bX+cY,\quad T_0=bp^2+cq^2-2u^2,\quad
v_n=QV,\quad z=Qt,
$$
$$
n_n=Q(T_0+4uf)-2v_n,\qquad
j_n=2Qf-v_n-a uQ=Qd_1.
$$
原 Gram 由
$$
A_1=2f-2bX-2cY+2bc\,t,\quad
r=X-ap-ct,\quad s=Y-aq-bt
$$
及四行
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0)
$$
定义。所有以下整数恒等式都直接在这同一七变量 $(b,c,\rho,f,X,Y,t)$ 的原代数中建立。

记 $E_W=bE_B+cE_C$。真正紧凑多项式是
$$
R_{2,\mathrm{true}}
=2\rho\left[
4Q(f-u)(v_n-Qf)+bc\,z^2
+z(4bc\,uQ-\ell v_n)\right]
+(b-c)z n_n.
$$
它满足完整原组合
$$
\boxed{
R_{2,\mathrm{true}}
+\rho Q^2(E_{1,\mathrm{true}}-E_W)
-Q^2((b-c)t-a\rho)E_0=0.
}
$$
同时
$$
R_{2,\mathrm{true}}-R_{2,\mathrm{bad}}
=\rho Q^2(4ud_1-2d_1^2).
$$
在 $\rho\ne0$ 的原图上，$\overline R=R_2/(2\rho)$ 的更正可写为
$$
\overline R_{\mathrm{true}}
=\overline R_{\mathrm{bad}}+2uQj_n-j_n^2
$$
$$
=\boxed{
4Q(f-u)(v_n-Qf)+bc\,z^2
+z(4bc\,uQ-\ell v_n)
+\frac{u-\ell}{2\rho^2}\,z n_n.
}
$$
最后一个有理形式只用于其分母已支付的图；前面的七变量整数恒等式不要求该分母可逆。

## 4. 已实际完成的更正证书

新源直接定义真正的 `vm`、$\tau$、$DK$ 和全部四个 $E_j$，在整数多项式环完整展开每一差式。实际执行环境为纯 V8 BigInt；20 ms，673 次多项式乘法，共 11 条完整零差返回：

1. 原 $F_2=2f$ 与原 $E_0$；
2. 同一 Gram 的 $d_0=u$、$d_1=2f-V-a u$；
3. 错误与真实 $E_1$ 的确切差式，以及 $j_n=Qd_1$；
4. 新旧 $R_2$ 差式和新 $R_2$ 的完整原均值组合；
5. 旧 $W_4$ 的完整原 $E_W/E_0$ 组合；
6. 旧 $N_{\mathrm{compact}}$ 与真实 $N_4$ 极化 $N_v$ 的恒等式；
7. 旧 $O_{\mathrm{compact}}$ 与真实 $E_B-E_C$ 的恒等式。

新 $R_2$ 展开为 132 项；$W_4$、$N_v$、$O$ 对应完整返回的项数分别为 486、286、120。回执只保存计数、来源和零差状态，没有存放可重算系数载荷。本执行不使用 Phi 特化、不使用未付范数逆、不提出新的排除定理。

## 5. 立即撤回与保留的准确边界

所有以错误 $R_2$ 或 $\overline R$ 为原必要关系的后续结论，原必要性、原点计数、有限性和排除结论均暂撤。特别包括由该式生成的旧第一头、旧三生成元规则，以及沿这些规则建立的 whole-H1 排除、H42、最高项和 $C_5^*$、有限权模型与 583 模型等原题解释。不得借这些旧结论支付新正确模型的头或权单位。

已经实跑的行列式、局部赋值、矩阵恒等式和资源失败仍然是各自**明确写定的旧多项式矩阵**的准确记录；例如已得次数或因子不能被改写成未执行。它们与原 Gram 问题的桥梁现在缺失，因此不再提供原题必要性。后续若需恢复，必须给真实更正原式的全新桥梁，不能用数值巧合或旧矩阵内部自洽替代。

下列内容不被这个错误直接否定：

- 用正确 `vm(d,d)` 定义的原 Gram 和独立原矩恒等式；
- $E_0,E_B,E_C$，以及本次完整重新返回的 $W_4,O_{\mathrm{compact}},N_{\mathrm{compact}}$；
- 原先直接从正确原 Gram 得到且没有再依赖错误紧凑式或其派生单位的结论；
- 独立 Haar、R271 和普通不变子空间研究的其他算子论证明。

例如 `2026-11-27-unit211-general-Phi-zero-monic-six-actual-value-return-8542.py`，blob `ad01958e99ca84b00d03159dc2664fb4eddc88e1`，SHA256 `1218c370659ea487450279925224b57b2c729453d623fd6f086a962d3281963e`，其均值确实用 `-2*vm(d,d)[j]`。这只确认其原定义正确，不自动豁免后续与错误紧凑式合并的推论。

已进一步逐源确认：W native→原 G D→F101 全返回链及十三个实际支付原子的来源均采用正确原乘法，详[W 原链](2026-11-28-unit211-W-native-Lhalf-correct-jet-mean-source-chain-8542.md)与[十三原子来源](2026-11-28-unit211-W-native-thirteen-paid-atoms-correct-mean-provenance-8542.md)。因此整 Lhalf 的原排除不因这处具体错误撤回。

L0 完整覆盖源 blob `64fbf4c19e5d20377e46bc52c023a915f36e5c24` 与 S0/Lt0 低不变量源 blob `1363e56ca7367ea990fadffbaff5f27f7c497f4a` 已静态读到正确 `vm(d,d)`；这确认原输入定义，不替尚未追完的全部后继来源背书。其它 Phi、等单值紧凑三列及全部派生单位继续按确切依赖分类，未确认独立来源之前不得沿用受影响的闭合标签。

下一步从上节真正的 $\overline R_{\mathrm{true}}$ 和完整原 Gram 重建小头与原关系。旧 first-head 单位、旧三生成元、583/H42/$C_5^*$ 不得作为该新来源的假设。该更正本身没有完成 ISP，也没有完成 unit211 的排空。

## 6. h=k、Delta=0 的续查补正

继续追踪原消费者，明确补正以下三页：

- [R150-appendix-unit211-equal-singleton-Delta-zero-two-QQ-curves-848-base-cover](../results/R150-appendix-unit211-equal-singleton-Delta-zero-two-QQ-curves-848-base-cover.md)：本页第二条曲线 M 使用错误 compact R2 的 RWO cofactor，原必要性和 848 基点界撤回。独立 Delta/Tnum 相容及其投影只能按自身原范围保留；不能用旧 M 支付有限性。
- [R150-appendix-unit211-equal-singleton-Delta-zero-seven-lambda-complete-QQ-cover](../results/R150-appendix-unit211-equal-singleton-Delta-zero-seven-lambda-complete-QQ-cover.md)：本页 578 次/80 界/七个 lambda 的完整覆盖使用错误 compact R2 的 RWO、RWN1 cofactor，原覆盖与计数撤回。定义矩阵、准确运行和因式记录保留，不再支持整个原 Delta=0 的候选表。
- [R150-appendix-unit211-equal-singleton-entire-Delta-zero-exclusion](../results/R150-appendix-unit211-equal-singleton-entire-Delta-zero-exclusion.md)：本页整个 Delta=0 排除依赖已撤回的 578 次/七个 lambda 覆盖，因此全支排除撤回。固定 C1、C2、C4 条件下直接来自正确 Gram 的返回只按各自条件保留；不能合成全 Delta=0 排空。

这条依赖确为旧 compact RWO/RWN1，不能因最后固定常数域使用了正确 vm 就补回缺失的全参数覆盖。当前 h=k 的整个 Delta=0 仍保留；直接原 Delta/Tnum 与已经逐个完成的条件纤维不重做。新[正确五原行和三物理条件](../results/R150-appendix-unit211-h-equals-k-corrected-five-original-rows-and-three-physical-cofactor-conditions.md)没有倒 Delta，可继续作为新输入。

已独立重读前会话 S0 等值 lambda-half 的正文与 blob 0f6fbabe15135c7408a8649fad551eab9b80039a，原 vm 和第五列物理秩证明正确，故这一物理点排除直接保留。它不提供裸多项式单位证书。
