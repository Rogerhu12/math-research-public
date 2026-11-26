# 两套实际完整 v2 尾图的有限 $C^2$ 差界入口

维护：Astra-held10-06bbeb39-20261126，2026-11-26。

可信度：下述有限图比较公式是精确代数推导；新入口已经实际通过 Python 编译、CLI 参数入口与三个小型精确代数检查。**尚未对两套真实 $\lambda=1$ actual-DN 尾场执行；没有新的实际场差界、精化收敛或完整曲面结论。** 不重复已登记旧场证书，也不迁移旧场数值。

源：`scripts/resume_20261126/seam_compare_tail_c2_v2.py`，SHA-256 `efcbcf6694c7327ca7ffe062aa883dd1226b75a884d9a3fb1f7249946ba11d33`。原 v2 导出、证书与接缝修补源不变。

## 1. 实际输入与范围

两侧分别给出真实 actual-DN 的 `run.json` 和完整 v2 全尾 `summary.json`。原 actual 类型及显式 `-refinement-v1` 类型均调用正式 `warm_actual_dn_refine_model.accepted_input`；随后调用其 `require_same_problem`，固定完整 $P$、同一 $g$ 输入、真实 $\lambda=1$、literal mean1168、全部 provider、原 $\lambda=1$ 几何锚等，而不是只比较几个标量。$M$、原角节点数 $N$、RK 分辨率与显式 Fourier 度数允许随实际精化改变。

每侧重新核对最终完整 $H$ 包、目标记录、原 raw / physical SHA、相应 source-port SHA，以及全尾 bundle、manifest、原 native mean chain、全部共同节点、全部 stage 证书与本侧深端 collar。必须覆盖完整 stage 集与深端圆盘；不能输入仅 stage 0、warm 缩放包、缺失数组或仅成功标签。各原连续证书是否满足度量/曲率分配仍分别记录；比较有限图本身不把失败分配改成成功。

比较的是 v2 manifest 所定义的**基准尾图**。可计算实数桥迹所定义的 cut Hermite 修补不在此差界内；完整修补图的精化还需加入两侧修补的差界。双方所有大数组、全 stage 证书与公共区间记录留在执行 runner，不进 Git。

## 2. 同背景消项与真实高度常数

对每侧 $i\in\{L,R\}$，令 $V_i(R,\theta)$ 为所声明的平面 Fourier 扰动，$\mu_i(R,\theta)$ 为包含原始非旋转均值的完整高度扰动，$\mu_{i,c}$ 为该原 mean chain 在 cut 的值。上尾图采用既有定义

$$
F_i(R,\theta)=\left(
R e^{i\theta}+V_i(R,\theta),\
Z_{i,c}+\mu_{i,c}-[h(R)-h(R_c)]-\mu_i(R,\theta)
\right).
$$

入口逐项比较两侧背景定义中的全部 `parameters,cells,checkpoint_sha256,factory_sha256`，并各自通过 R58 完整定义 SHA 与 normalization 复用链。只有它们完全相同时，才符号消去 $h$ 与 $R e^{i\theta}$。

按 $\Delta=R-L$，

$$
F_R-F_L=
\left(
\Delta V,\ 
\Delta Z_c+\Delta\mu_c-\Delta\mu(R,\theta)
\right).
$$

$\Delta\mu_c$ 是两个**原始保存的均值**之差，按各自 binary64 literal 转成精确有理数；不重置、不重新积分，也不把它并入可随意选择的平移。在双方深 collar 以内，扰动均为零，位置差仍为 $(0,0,\Delta Z_c+\Delta\mu_c)$，导数差为零。

$\Delta Z_c$ 来自双方同场完整 `true-cut-height.json`，保持原 $Z_i(0)=0$ 锚。若 $Z_{L,c}\in[\ell_L,u_L]$、$Z_{R,c}\in[\ell_R,u_R]$，则使用

$$
\Delta Z_c\in[\ell_R-u_L,\ u_R-\ell_L].
$$

这里不选区间中点，不对齐高度或刚体。未提供这一对真实证书时，入口仍能完成全部径向/角向导数计算，但 `complete=false`，状态明确为高度常数未付；不输出绝对位置或完整 $C^2$ 范数。

## 3. 精确共同 $R$ 分割和谱并集

每侧有限 stage 的所有 `radiusJS` 结点均按精确 binary 有理数解释；深 collar 的端点使用其已有精确定义

$$
R_{i,\mathrm{in}}=\frac{R_{i,0}+R_{\mathrm{cuff}}}{2},
\qquad
L_i=\frac{R_{i,0}-R_{\mathrm{cuff}}}{2}.
$$

从中心开始顺序流式取双方所有结点及深 collar 端点的并集。每个公共闭区间都严格包含于两侧各自的一段原多项式域，覆盖直到共同 $R_c$；不近似合并相邻半径，也不使用网格中点定义新图。实现同一时间仅保留每侧当前 stage 的数组和多项式。

对某侧原段 $[r_0,r_1]$，令 $t=(R-r_0)/(r_1-r_0)$。其每个 Cartesian Fourier 系数是匹配保存的值、$\partial_R$、$\partial_R^2$ 的唯一五次 Hermite 多项式 $p(t)$。若公共子段为 $[a,b]$，则

$$
t=\alpha+\beta u,\qquad
\alpha=\frac{a-r_0}{r_1-r_0},\quad
\beta=\frac{b-a}{r_1-r_0},\quad
u=\frac{R-a}{b-a}.
$$

若 $p(t)=\sum_{j=0}^d p_jt^j$，$d\le5$，精确重参数化为

$$
p(\alpha+\beta u)
=\sum_{k=0}^d
\left[
\beta^k\sum_{j=k}^d {j\choose k}p_j\alpha^{j-k}
\right]u^k.
$$

所有运算为有理数；先对两图同频率多项式相减，再取界。完整平面模式并集与高度模式并集分别处理，某侧没有的频率系数为零。特别是增加 $M,N,D$ 时，新出现的全部 Fourier 模式都进入差界，不截掉“高模”。高度 $0$ 模在相减后精确加入 $\Delta\mu_c$。

深 collar 使用本侧真实最深共同节点和原右端 Hermite 基函数；高度反号与完整 upper 图一致。内圆盘的扰动系数为零。已有全节点二 jet 链与深 collar 匹配保证原图及差图在所有公共分割点都是 $C^2$。

## 4. 连续 Bernstein 界与 Cartesian $C^2$ 范数

对公共段中任一有理多项式 $q(u)=\sum_{j=0}^n q_j u^j$，它的 Bernstein 系数为

$$
b_k=\sum_{j=0}^k
\frac{{k\choose j}}{{n\choose j}}q_j,\qquad 0\le k\le n.
$$

Bernstein 基函数在 $[0,1]$ 上非负且和为 $1$，故

$$
\sup_{0\le u\le1}|q(u)|\le\max_k |b_k|.
$$

物理径向导数每求导一次均除以公共段长度 $b-a$。平面模式 $p_m e^{im\theta}$ 与高度模式 $h_m\cos(m\theta)$ 的 $b$ 阶角导数范数均由 $|m|^b$ 乘系数界控制。对 $a+b\le2$，定义

$$
B_{ab}
=\sum_{m\in\mathcal P}|m|^b
\left\|\partial_R^a\Delta p_m\right\|_\infty
+\sum_{m\in\mathcal H}|m|^b
\left\|\partial_R^a\widetilde{\Delta h}_m\right\|_\infty.
$$

其中高度 $0$ 模已含 $\Delta\mu_c$；上述表达式暂不含 $\Delta Z_c$。由三角不等式，$B_{ab}$ 控制完整三维向量的相应导数。

在公共段 $R\ge r_*>0$，以 Euclidean disk 的正交极坐标标架 $(e_R,e_\theta)$ 表示。对向量值差图 $U$，

$$
DU(e_R)=U_R,\qquad
DU(e_\theta)=R^{-1}U_\theta,
$$

$$
D^2U(e_R,e_R)=U_{RR},
$$

$$
D^2U(e_R,e_\theta)
=R^{-1}U_{R\theta}-R^{-2}U_\theta,
$$

$$
D^2U(e_\theta,e_\theta)
=R^{-2}U_{\theta\theta}+R^{-1}U_R.
$$

因此有完整 Cartesian Frobenius 控制

$$
\|DU\|_{\mathrm{op}}
\le
\sqrt{B_{10}^2+(B_{01}/r_*)^2},
$$

$$
\|D^2U\|_{\mathrm{bilinear}}
\le
\sqrt{
B_{20}^2+
2(B_{11}/r_*+B_{01}/r_*^2)^2+
(B_{02}/r_*^2+B_{10}/r_*)^2
}.
$$

含中心的第一个公共段位于双方扰动为零的圆盘内，直接使用常向量的零导数，不除以 $R=0$。全图界是所有公共段界的最大值；共享二 jet 保证结点处也受同一界控制。平方根上取界采用精确整数平方根构造有理上界，展示的小数向外舍入。

若全域相对位置界为 $P$，已得到的 $\Delta Z_c$ 区间绝对值上界为 $Z$，一二阶界分别为 $A_1,A_2$，则

$$
\sup|F_R-F_L|\le P+Z,\qquad
\|F_R-F_L\|_{C^2}
\le \max\{P+Z,A_1,A_2\},
$$

其中 $C^2$ 范数明确使用上述共同 Euclidean disk 坐标的三维向量、算子与双线性二阶范数。它只比较两套指定有限图；不自动推出一列图的 Cauchy 性。

## 5. $N,D$ 改变时仍未支付的内容

每侧 v2 的 $N,D$、选择规则、完整频率列表都作为其有限图定义固定。比较器确实比较改变 $N,D$ 后的两个图，包含所有新增系数和原均值差。它没有把这些有限 DFT 系数冒充原连续 source evaluator 的全部精确 Fourier 展开；到未投影连续图的误差、无限精化的可求和控制、固定 $g$ 的完整度量极限以及桥/尾修补族都仍需各自支付。

背景相同才能符号消项；输入的完整 $P$ 相同不能替代这些误差证明。输出始终保留 `Cauchy_sequence_proved=false`、`whole_closed_surface=false`、`exact_cut_seam_corrections_included=false`。

## 6. 已执行检查与调用

实际执行的小型纯代数检查：

- 同一个 $R^2(R-\frac14)^3$ 系数函数，分别放在两个不同的非重合径向网格，并为一侧加入零系数新模式；公共分割准确得到五段，全部 $0$、$1$、$2$ 阶差界精确为零。
- 双方内圆盘扰动都为零时，输入 $\Delta\mu_c=2$，位置差界保留精确 $2$，所有导数界为零。
- $R^3\cos(3\theta)$ 在原段内部公共子段 $[\frac12,\frac34]$ 的物理 $R$ 导数与角权重得到精确
  $B_{00}=27/64$、$B_{10}=27/16$、$B_{01}=81/64$、$B_{20}=9/2$、$B_{11}=81/16$、$B_{02}=243/64$。

这些只验证代数实现，不是构造或假装接受一个数值尾包。初次从过浅 scratch 路径运行 CLI 不符合 repo-relative 布局；移入镜像仓库相对路径后实际 `py_compile`、`--help` 均退出 $0$。数学与输入函数完成检查后，仅调整最终状态投影：没有真实 $\Delta Z_c$ 区间时 `complete=false`。没有调用 BVP、DN 或旧几何证书。

同一 runner 上的最终调用形式：

~~~bash
python topics/visible-flex-held-10pct/scripts/resume_20261126/seam_compare_tail_c2_v2.py \
  --left-source-run /runner/actual-left/run.json \
  --right-source-run /runner/actual-right/run.json \
  --left-tail-certificate /runner/geometry-left/certify-all/summary.json \
  --right-tail-certificate /runner/geometry-right/certify-all/summary.json \
  --left-cut-height /runner/height-left/true-cut-height.json \
  --right-cut-height /runner/height-right/true-cut-height.json \
  --outdir /runner/tail-pair-c2
~~~

上述是参数形式，不是实际运行路径。当前还没有两套满足入口的真实实际场，故没有可登记的新差界数值；父任务继续真实 $\lambda=1$ 与原完整尾接受计算。

