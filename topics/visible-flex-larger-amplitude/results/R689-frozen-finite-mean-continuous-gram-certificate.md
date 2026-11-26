# R689. 固定有限均值目标的公共项抵消与全域连续 Gram 证书

2026-11-26，Astra-larger-e4e2a2bf-20261126 / geometry（AI 辅助）。

**状态：下述新增抵消恒等式、共同分割及误差归一化界已证明；源码只作 AST 静态检查，尚无本入口的公开 Actions 科学返回。** 本文不把求解中的移动均值称为固定目标，不把当前约百分之一的候选重新检查一遍冒作进展。严格上界应接在实际新目标求解已经接近要求的候选后；若真实点下界已经超过要求，后继必须改变候选，而非只增加同一失败候选的证书精度。

本接口接 [R684](R684-rotational-mean-metric-design-and-frozen-target.md) 的最终冻结定义，使用 [R657](R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md)、[R674](R674-reference-tail-continuous-profile-and-same-angle-remainders.md) 的完整 Bernstein、非线性角余项及准确参考尾核。新增内容是两个不同准确场的公共 lift 平方抵消、不同网格的完整共同分割、固定有限目标本身的严格系数求值与双方物理余项进入同一相对矩阵的界；已有角核、相位恒等式和旧实际返回不在本条重新认领。数值固定目标求解与实际 mesh/M/N 精化由独立的 frozen-target wrapper 执行；本文的证书加密不等同于候选精化收敛。

## 1. 一个目标与两个不同的场

选定真实设计候选 $F_*$ 后，固定其完整准确表示、原材料角映射、有限角规则、原标量输入与尾模型、固定帽图，以及全部设计常数。本文第一入口只支持明确的**有限物理角均值**：

$$
\phi_j^*=2\pi j/N_*,\quad w_j=1/N_*,\qquad
E_*(s)=\sum_{j=0}^{N_*-1}w_j |F_{*,s}(s,\phi_j^*)|^2,
$$

$$
C_*(s)=\sum_{j=0}^{N_*-1}w_j
\frac{|F_{*,\phi}(s,\phi_j^*)|^2}{\rho_*(\phi_j^*)^2},
\qquad g_*=E_*(s)ds^2+C_*(s)d\theta^2.
\tag{1}
$$

(1) 在完整连续 $s$ 区间上定义目标。它不是材料 Haar 积分的近似，也没有另一个需要随精化改变的“真正平均”。不得把 $N_*$ 换成当前候选的角网格，不得把当前候选的 $\rho$ 放进冻结均值，不得用旧观察点的均值数组插值来填充新径向点。

当前精化候选 $F$ 有自己的完整 $q$、core、$\rho$ 与 $\Theta$。它可以采用不同的准确径向网格、频率数和观察角数；相对于同一材料角 $\theta$，其实际 Gram 仍为

$$
E=|F_s|^2,\qquad B=F_s\cdot F_\phi/\rho,
\qquad C=|F_\phi|^2/\rho^2.
$$

所需误差矩阵准确为

$$
R=\begin{pmatrix}
(E-E_*)/E_* & B/\sqrt{E_*C_*}\\
B/\sqrt{E_*C_*} & (C-C_*)/C_*
\end{pmatrix}.
\tag{2}
$$

不从当前场中再次减去它自己的均值。当前 $\Theta$ 可以随自由 core 变化；这只改变当前实际 Gram 的坐标表达，不改变 (1)。

### 共同表示的准确条件

本入口使用当前与冻结场共同的准确 $f=f_\lambda(s)$。因此逐一核对：原 scalar-input 身份、原 FullHold $S/R$ 定义、lift 宽度、$\lambda$、$\eta$ 的两个物理仿射端点，以及固定 core 前三系数。两个场分别由冻结 R674 reader 核对其 canonical model、节点报告、profile carrier 与全部源身份。不能把另一场的旧证书装入其中。

当前实现还要求节点报告携带的原 scalar identity 与 $S/R$ 包围盒逐字一致。这是此入口的明确验证条件；R676 类型的真正网格/频率精化可原样携带这些定义。以后若只缩小同一准确标量的证书盒，需要扩展验证器来证明同一标量身份，不能未经说明绕过检查。

$H$ 属于待求实际场，可以不同。$z=h_\lambda H+k_\lambda$ 及其导数在两场中分别保留；下面没有把 $H$ 相关项作公共抵消。

## 2. 先准确消去公共纯 lift 平方

沿各自的旋转 $\phi$ 架写

$$
F=q+f e_r(\delta)+z e_z,\quad
U=q_s,\quad T=q_\phi,\quad c=f_s,\quad d=z_s,
$$

$$
F_s=U+c e_r+d e_z,\qquad F_\phi=T+f\rho e_\theta.
\tag{3}
$$

$T$ 含旋转架连接项，直接消费 R674 的完整 `raw_components`，不是把三个架分量作普通导数后忘掉连接。定义

$$
A=|U|^2+d^2+2dU_z
  +2c(U_R\cos\delta+U_T\sin\delta),
$$

$$
D=\frac{|T|^2}{\rho^2}
  +\frac{2f}{\rho}(T_T\cos\delta-T_R\sin\delta).
\tag{4}
$$

由 $|e_r|=|e_\theta|=1$ 及 $e_r\cdot e_\theta=0$，有准确恒等式

$$E=c^2+A,\qquad C=f^2+D.$$

令 $\langle\cdot\rangle_*$ 为 (1) 的固定有限规则。因 $f,c$ 只依赖 $s$，

$$
E_*=c^2+\langle A_*\rangle_*,\qquad
C_*=f^2+\langle D_*\rangle_*,
$$

$$
E-E_*=A-\langle A_*\rangle_*,\qquad
|F_\phi|^2-\rho^2C_*=\rho^2(D-\langle D_*\rangle_*).
\tag{5}
$$

这消掉共同的 $f_s^2$ 与 $f^2$，没有分别区间化后再相减。尤其在准确旋转尾 $q=0$ 且同一 $H$ 下，不会凭空留下这两个纯 lift 大分量的区间宽度。当前 $d^2+2dU_z$ 与冻结 $d_*^2+2d_*U_{*,z}$ 均原样进入 (4)，所以 $H$ 不同的真实影响仍被计入。

将三个分子写成 R657 的完整形式 $P+C_0\cos\delta+S_0\sin\delta$，当前场的表为：

| 分子 | $P$ | $C_0$ | $S_0$ |
|---|---|---|---|
| $E-E_*$ | $|U|^2+d^2+2dU_z-\langle A_*\rangle_*$ | $2cU_R$ | $2cU_T$ |
| $F_s\cdot F_\phi$ | $U\cdot T+dT_z$ | $cT_R+f\rho U_T$ | $cT_T-f\rho U_R$ |
| $|F_\phi|^2-\rho^2 C_*$ | $|T|^2-\rho^2\langle D_*\rangle_*$ | $2f\rho T_T$ | $-2f\rho T_R$ |

这里的 $C_0$ 是余弦项，不是目标系数 $C_*$。冻结均值在本片上是径向 Bernstein 多项式系数区间；它相对于当前角变量为常数。因此表内有限角部分仍满足原 $4M$ 带宽上界。完整的余弦/正弦复合项并未被宣称为带限，也没有截掉解析 lift。

## 3. 不同网格的完整公共分割

当前与冻结场各自具有准确仿射节点 $s_i=\alpha_iS+\beta_i$。两套节点之外，R674 的 `pieces` 还覆盖原 scalar 解析分界、旧 $\chi$ 分界和两个 $\eta$ 分界。接口先检查两套 partition 各自从 0 连续覆盖到准确 $S$，然后按原 $S$ 盒可证明的顺序取两者的完整公共交。

每个公共闭片再允许作明确 dyadic 径向细分。左右端点保持准确 Fraction 仿射表达，两个 reader 分别用自己的原胞宽计算限制参数；没有用浮点 mesh 显示值来决定片的归属或吞掉短片。若原盒无法严格判定两个不同边界的顺序，入口拒绝这次调用，不把未付部分当成空集。

在一个公共小片上，两场使用同一 scalar Taylor 阶数、同一准确物理中心、同一 scalar/lift 定义。$f$ 的共同 Taylor 多项式因此是同一个准确多项式；即使两份系数包围的数值宽度不同，也可以先在准确恒等式 (5) 中消去其纯平方。两场的 $z$ 多项式和误差分别计算。

旧/新自由变量、原 core、所有 Fourier 模与准确尾都保留。共同分割不是改变场或目标；它只是把两套已有完整表示限制到相同的物理区间。

## 4. 冻结有限均值的严格求值

冻结 reader 的物理角节点保持 $N_*$ 不变。在这些准确角点，完整 $P+C_0\cos\delta_*+S_0\sin\delta_*$ 值由原严格区间变换与三角余项求出。对 $D_*$ 先按 (4) 消去纯 $f^2$，再除以这些节点自己的 $\rho_*^2$。逐节点的 Bernstein 控制点用每一步都向外的成对加法求和，再乘准确 $1/N_*$。

角变换的工作网格可以取 $N_*$ 的二幂倍数以满足严格有限谱折扣；此时只抽取间隔为 `Q_eval/N_*` 的原节点。额外工作节点不进入均值。因此提高目标求值精度不改变 (1) 的角点、权重或准确目标。

冻结目标只需要在其有限规则节点上支付物理场 Taylor 误差，因为有限平均本身就是精确定义。当前候选则仍需覆盖全部连续角点；两者的范围没有混用。

## 5. 双方物理 scalar 余项及真正归一化

设 R674 给出当前小片上的准确 jet 余项

$$
|f-\widehat f|\le e_{f,0},\quad
|f_s-\widehat f_s|\le e_{f,1},\quad
|z_s-\widehat z_s|\le e_{z,1}.
$$

对 $V=F_s$ 与 $W=F_\theta$，准确有

$$
|V-\widehat V|\le v:=\sqrt{e_{f,1}^2+e_{z,1}^2},
\qquad |W-\widehat W|\le w:=e_{f,0}.
\tag{6}
$$

第二式先在准确式中消掉 $\rho$，因为解析尾的 $F_\phi$ 误差为 $\rho\,\delta f\,e_\theta$。不再在小 $\rho$ 处错误地放大这项标量误差。

若 $V_0,W_0$ 是近似场两首 jet 范数上界，则三个真实 Gram 误差分别不超过

$$
d_E=2V_0v+v^2,\quad
d_B=W_0v+V_0w+vw,\quad
d_C=2W_0w+w^2.
\tag{7}
$$

当前场的 $V_0,W_0$ 从完整角盒分子与冻结近似目标恢复：

$$
|\widehat V|^2=\widehat N_E+\widehat E_*,\qquad
|\widehat W|^2=\widehat N_C/\rho^2+\widehat C_*.
$$

冻结场则在全部固定规则节点使用完整径向 Bernstein 凸包。取冻结节点费用的统一上界，正权均值给

$$|E_*-\widehat E_*|\le d_{E,*},\qquad
|C_*-\widehat C_*|\le d_{C,*}.$$

于是先形成实际目标盒

$$\mathcal E_* = \widehat E_*+[-d_{E,*},d_{E,*}],\qquad
\mathcal C_* = \widehat C_*+[-d_{C,*},d_{C,*}].$$

只有这两盒与当前 $\rho$ 的下端均严格正时才除法。(2) 的三项分别由下式包围：

$$
\frac{\widehat N_E}{\mathcal E_*}
 +\left[-\frac{d_E+d_{E,*}}{(\mathcal E_*)_-},
          \frac{d_E+d_{E,*}}{(\mathcal E_*)_-}\right],
$$

$$
\frac{\widehat N_B}{\rho\sqrt{\mathcal E_*\mathcal C_*}}
 +\left[-\frac{d_B}{\sqrt{(\mathcal E_*)_-(\mathcal C_*)_-}},
          \frac{d_B}{\sqrt{(\mathcal E_*)_-(\mathcal C_*)_-}}\right],
$$

$$
\frac{\widehat N_C}{\rho^2\mathcal C_*}
 +\left[-\frac{d_C+d_{C,*}}{(\mathcal C_*)_-},
          \frac{d_C+d_{C,*}}{(\mathcal C_*)_-}\right].
\tag{8}
$$

源码使用逐操作向外算术实现 (6)–(8)。公共纯平方抵消不允许漏掉双方物理余项；(7) 的总费用是保守且完整的，可能保留本可进一步抵消的费用，但不会假造更小上界。这里不存在原 $a(s)$ 的额外目标近似误差，因为新目标已经由 (1) 明确定义；原标量只通过实际解析场和其严格余项进入。

## 6. 全角上界、实际点下界与全相位

完整新分子的有限角部分仍以原严格区间变换处理。其前两阶角导数在完成 (5) 的抵消后形成；复合三角项的四阶 Bell 余项照 R657 全部计入。每个闭半步角盒先包围完整 Bernstein 控制点，再取径向凸包。因此返回覆盖整个公共小片和整圆，而不是只覆盖数值观察点。

对于包围的对称三项 $(e,b,c)$，使用准确公式

$$\|R\|_{\mathrm{op}}=
\frac{|e+c|+\sqrt{(e-c)^2+4b^2}}2.$$

同一次计算在小片准确端点、准确当前角网格点上去掉角半步 padding，但保留双方 scalar 余项，得到真正点态范数下端。其最大值是真实连续 supremum 的下界，不是某个上界公式的下端，不以离散扫描充当连续证明。

冻结目标关于材料角不变，所以 R248 的相位共轭证明照用；当前自由 core 变化不改变这个事实。准确镜像不改变相对 Gram。帽上使用同一个固定 p4 图的自身诱导目标，垂直平移 $\pm H$ 不改变帽内第一基本形式；在准确平领中与 R671 两 jet 接口拼合。故全部活动区都支付后，相对误差结论扩展到整个闭面及所有相位。此处没有因此支付全域嵌入、曲率、reach、握持比例或非全等性。

## 7. 身份、逐小片返回和继续入口

接口消费数值 frozen-target producer 的同一个 `R684-frozen-rotational-mean-metric-v1` manifest。其数学身份包括全部输入与源码内容 SHA256、准确 canonical model、有限角规则、domain、cap recipe 和 mean definition；路径、运行时间与 provenance 不参与数学对象 ID，但所指文件的实际内容仍逐一核对。输入路径不是用来绕过身份校验的替代品。

当前场与冻结场各自的 bundle、node report、scalar input、reference carrier 被分别核验。允许不同 mesh/M/N；既不要求沿用旧几何数值，也不把两个场混成同一 bundle。冻结目标均值的计算读取冻结场；当前场的全部误差和材料分母读取当前场。

一次任务为**一个准确公共小片的一个 dyadic 径向子片与全部角域**。`--budget-seconds 600` 是 admission budget：至少接一个仍未执行的小片，然后时间到后不接新任务，当前小片自然返回后再退出。这样不会因 reader 初始化较慢而反复退出且永不支付任何新片。每条实际返回先写 runner-local 不可覆盖 journal，后继以 `--resume` 消费同一 run、同一 producer、同一输入、同一 target 与精度。异常和未返回片不贡献任何上界。只有某个当前原胞的全部共同小片都有效返回，才能把该胞记入 compact covered range；只有所有原胞完整，才允许给全域上界或 `metric_certified=true`。

对期望已经接近目标的新候选，入口形如：

```sh
python "$SRC/frozen_mean_metric_interval.py" \
  --repo "$GITHUB_WORKSPACE" \
  --bundle "$WORK/fixed-target-refinement/final.npz" \
  --node-report "$WORK/fixed-target-refinement/exact-node-report.json" \
  --scalar-input "$WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --reference-carrier "$WORK/fixed-target-refinement/exact-tail-lift-profiles.npz" \
  --frozen-metric "$WORK/frozen-mean-target/manifest.json" \
  --angles 4096 --radial-subdivisions 1 --scalar-degree 5 --panels 128 \
  --budget-seconds 600 --journal "$WORK/fixed-mean-Gram-journal" \
  --out "$WORK/postprocess/fixed-mean-Gram-batch-01.json"
```

后继保持同 journal 与参数，增加 `--resume` 并换一个输出路径。更高证书精度使用另一明确 journal；当前实现不从跨 run compact 声明虚构原始逐片记录。所有可重算逐片 JSON 和数组只留 runner；公开源、参数、实际 run/输出 hash 与紧凑的完整域声明。

连续证书精度提高只降低包围损失。即便全域误差通过 $10^{-6}$，README 要求的同一固定 $g_*$ 下真实网格、频率及时间精化误差继续下降至机器/原求解容差仍要由实际候选序列支付。本文和源码不自动把一个小有限残差、一个完整上界或一个准备好的入口宣布为课题完成。

## 8. 源码与当前验证范围

完整新入口为 [frozen_mean_metric_interval.py](../scripts/resume_20261126/frozen_mean_metric_interval.py)，本条版本 SHA256：

`4552c2eafebb98b732d5ab7717b1b72665680a839b18a51c34c08f718f69381f`。

它严格消费既有 R674 Gram 核 `fd4cd58045e16a969c8c1be48468ab4c1a7be929ef9b95e2a9a24ca546176b2d` 与 reference interval 核 `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225`，不修改两份已刊源。冻结 manifest 的数学身份公式与数值 frozen-target producer 独立复算一致；实际文件内容、canonical model、准确 domain 和 R661 cap recipe 均有验证。

本次只作 AST 解析、字段/接口及数学式的静态审查，没有本地科学计算，没有先报一个未运行的全域数值。算术前提仍是 R657/R674 的逐操作向外 IEEE binary64 及严格三角/变换核；并不声称源码已获形式化验证。

紧凑 summary 字段表为 [resume-20261126-frozen-mean-gram-summary-fields.json](../computations/resume-20261126-frozen-mean-gram-summary-fields.json)，SHA256 `e17e73719c2581958842fc387b5f552738d3fc5c3fe3ecfc4185bf10453df57b`。它把已覆盖胞范围、这些胞的统一上界、目标已付胞范围、实际点下界及见证地址，与当前/冻结场和固定目标身份同时发表。下界可以来自尚未全付胞中的一个已实际返回点；其含义是整个连续 supremum 的下界，不能错误地限制到另一个上界集合。

几何 K、reach 以及固定目标求解精化的实际返回仍须另外登记；本条不占用留给真正同场全域 reach 的 R666。
