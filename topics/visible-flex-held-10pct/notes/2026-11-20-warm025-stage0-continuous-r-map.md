# 实际 warm .25 尾切口首段的共享 R 图与连续度量界

维护：Astra-held10-1b6d88ec-20261120 / geometry_advance。2026-11-20 UTC。

## 已证明的结论

对已接受的 M24、depth 8、warm `.25 H` 尾记录，沿用 stage 127 的**同一新物理半径共享 Hermite 图合同**，取 stage 0 的实际保存 Cartesian Fourier 两阶数据。在全部 16 个物理 $R$ 片和整个角圆上，相对于当前 [R58](../results/R58-q060-valley-background-height-and-curvature.md) 真实背景的同一个度量，实际执行得到

$$
\boxed{
\|g^{-1/2}(F^*\langle\cdot,\cdot\rangle-g)g^{-1/2}\|_{\rm op}
\le6.587612426404962\,10^{-9}<10^{-6},\qquad
|\kappa_i|\le8.039225762263028<8.04.
}
$$

若背景 cut 高度 $z_b\in[.1,1.28]$，同段还满足

$$|F|\le1.3398944230361383<1.34,\qquad F\cdot n\ge.08889530337433385>.08889.$$

该结论是**连续且严格的范围证明**，不是角采样、两次 quadrature 的差或原 finite audit 的小误差。所有 Fourier 模式都保留在图中；低模划分只用于计算二次 Gram 项，其余二次项有明确余项上界。

这里认证新共享 R 图的这一段，不声称旧 shooting 图已是 C²、full H 真尾已经求出、全尾已覆盖或前缀与尾的 Cartesian 接缝已完成。planar 有限差分 `rr` 只作为新图的字面两阶结点参数，未被称为原 PDE 场位置的真实二阶导数。

## 1. 同一次保存数据，均值和公共结点均不重置

checkpoint 与深端圆领、stage 127 使用同一份
`newg-wide-lambda0p002-m24-actual/tail_0001.json.gz`，SHA-256：

`302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de`。

原 native record 为
`newg-native-m24/runs/actual-lambda0p002/0009-jac-record.json`，SHA-256：

`a15afe15bdea350f03ea282c475deece4179f59c72f227b0bac9b5ec00980e7a`。

原 extract 工具已对全部 1152 个 stage 的 native 输入前 48 个分量与 checkpoint 逐字核对。此次只重放已有 stage 0 的原 IVP，没有 Newton 或新 shooting。stage 0 是 raw cell 0、segment 8、源坐标 $x\in[15/16,1]$。

导出的 17 个结点中，物理半径区间为

$$
\left[\frac{168884058786037}{562949953421312},
      \frac{5404319552844595}{18014398509481984}\right].
$$

外端恰是当前真背景的 exact binary `.3`，**没有 cut 半径重新选点或半径修补**。内端非旋转 mean 为 exact binary `3.681589766154052e-7`，外端为 exact binary `3.681650775547157e-7`；其差来自原 native 保存增量。所有内部结点保留原重放的 mean 值及两阶数据。

原 height 数据仍是 $r_{\rm JS}^4u$，不以真背景半径代换 $r_{\rm JS}$ 后重新解释。背景 primitive 单独加入，`meanBackground` 不再进入非旋转 mean。对上侧图，反射整个背景高度和全部 height Fourier 项，不能只翻转一方。

每个结点将原二进制数理解成精确有理数。相邻结点之间的每个 Fourier 系数，是匹配其共同值、一阶和二阶导数的唯一物理 $R$ quintic。这与已付 stage 127 及深圆领是同一表示；源实际验证了 $16\times153\times3\times2=14688$ 条精确端点等式。

stage 0 的内端就是后继 stage 1 外端应采用的 canonical 数据。后继全尾表示需**直接共用这份结点**，不可将另一侧重复浮点评价的小差当作字面两阶相等。本条的首段自身没有改动该公共结点。

## 2. 真背景覆盖与同一目标 g

使用冻结的 [q060_true_background_oracle.py](../scripts/resume_n4/q060_true_background_oracle.py)，其归一系数仍由 R58 真实积分唯一确定，未在区间内任选一个中点。此次只计算首段需要的局部真积分，没有重跑完整背景。

源证明物理区间包含在同一源片

$$x\in[937499/1000000,1]$$

内：左端真实半径的严格上界小于当前最小字面 $R$ 结点，外端是相同的精确 $R_c$，且真实 $R_x>0$。同片还证明 $w_x<0$，因此用端点包围整个真实 $w(R)$：

$$.08\le w(R)\le.08000303119483511.$$

固定辅助有理数

$$w_0=\frac{2882358366668837}{36028797018963968},\qquad
|w(R)-w_0|\le d_w:=\frac{109210303439}{72057594037927936}.$$

$w_0$ 只用于精确展开加有界余项；实际目标一直是

$$g=(1+w(R)^2)\,dR^2+R^2\,d\theta^2,$$

没有换成 $w_0$ 的常系数度量，也没有选取浮点归一系数。

## 3. 全角 Gram 的线性、二次共同抵消

在整体高度反射前，记水平扰动
$W=\sum_m a_m(R)e^{im\theta}$，竖直扰动
$H=\sum_m c_m(R)\cos(m\theta)$。相对参考 $(Re^{i\theta},h(R))$，三个未归一 Gram 缺陷是

$$
A=2\operatorname{Re}(e^{-i\theta}W_R)+2wH_R+|W_R|^2+H_R^2,
$$

$$
B=\operatorname{Re}(e^{i\theta}\overline{W_\theta}
 +iRe^{i\theta}\overline{W_R})+wH_\theta
 +\operatorname{Re}(W_R\overline{W_\theta})+H_RH_\theta,
$$

$$C=2\operatorname{Re}(iRe^{i\theta}\overline{W_\theta})+|W_\theta|^2+H_\theta^2.$$

上侧同时反射背景与扰动，三个内积不变。

计算对全部模式保留线性项。对 $|m|\le12$ 的水平项和 $m\le12$ 的高度项，二次项也精确卷积，随后和线性项按相同 cosine/sine 频率合并；所有系数都是有理 $R$ 多项式。原图 153 个模式没有被截断：只有二次运算被拆成 13 个低项与 140 个高项。

设在一个物理 $R$ 片上，低、高部分的向量一阶上界分别为

$$|V_{R,L}|\le r_L,\quad |V_{R,H}|\le r_H,\quad
|V_{\theta,L}|\le t_L,\quad |V_{\theta,H}|\le t_H.$$

未精确展开的三个二次余项分别由

$$2r_Lr_H+r_H^2,\qquad r_Lt_H+r_Ht_L+r_Ht_H,\qquad2t_Lt_H+t_H^2$$

包围。另将 $w-w_0$ 对 $A,B$ 的贡献分别以 $2d_w|H_R|$、$d_w|H_\theta|$ 支付。

合并之后才取各频率多项式的 Bernstein 系数绝对上界并求和。因此保留了实际场的同频抵消，而不是先对每个位置/导数项分别取绝对值。所有 polynomial、卷积、Hermite 和 Bernstein 运算均为 Fraction 精确运算。

最后利用 $E=1+w^2\ge1$ 及每片 $R\ge R_-$，对归一矩阵的 $A/E,B/(R\sqrt E),C/R^2$ 分别得到 $\mathcal A,\mathcal B,\mathcal C$。对称矩阵的 operator 范数不超过

$$\max(\mathcal A,\mathcal C)+\mathcal B.$$

16 片中的最大值就是结论中的 $6.587612426404962\,10^{-9}$。此处用到的 $w$ 范围是真实全片范围；没有只在结点或中点代入原 JS 背景。

## 4. 曲率与几何窗口

令 $v_R,v_\theta,v_{RR},v_{R\theta},v_{\theta\theta}$ 是全模式 Fourier–Bernstein 界，取

$$\eta^2=v_R^2+(v_\theta/R_-)^2.$$

实际全片最大严格上界为 $\eta\le.0010405175208580144<1$，故图浸入。相对于参考度量的协变 Hessian 三个正交分量为

$$
\frac{V_{RR}}E-\frac{ww_R}{E^2}V_R,\qquad
\frac{V_{R\theta}-V_\theta/R}{R\sqrt E},\qquad
\frac{V_{\theta\theta}}{R^2}+\frac{V_R}{RE}.
$$

R58 的 $|w|\le41/100$、$|w_R|/E^{3/2}\le8$ 给其范数上界

$$
b_{11}=v_{RR}+\frac{82}{25}v_R,\quad
b_{12}=(v_{R\theta}+v_\theta/R_-)/R_-,\quad
b_{22}=v_{\theta\theta}/R_-^2+v_R/R_-.
$$

令 $\beta^2=b_{11}^2+2b_{12}^2+b_{22}^2$。参考图的协变 Hessian 纯法向，且参考形算子 operator 范数至多 8；所以新图有

$$|\kappa_i|\le\frac{8+\beta}{(1-\eta)^2}\le8.039225762263028.$$

这个公式对真实 $R$ 背景使用协变 Hessian，不把辅助 $x$ 坐标中的二阶导数误作物理位置导数，也不需假设整个辅助 $x$ 图是 C²。

若 $z_b\in[.1,1.28]$，R58 的同一 $h_* =7446320975220351/288230376151711744$ 给背景

$$R_*:=\sqrt{(.3)^2+(1.28+h_*)^2},\qquad \Xi\cdot n_0>1/11.$$

全片 Fourier–Bernstein 的位置界 $v_0$、同向法线差 $\sqrt2\eta$ 给

$$|F|\le R_*+v_0<1.34,\qquad F\cdot n\ge1/11-R_*\sqrt2\eta-v_0>.08889.$$

这些仍是同一个中心、同一个高度窗；未单独平移此段来改善比值。全闭面 reach 与其他组件相交检查仍需完整组合后支付。

## 5. 执行与复现

源为 [certify_q060_stage0_r_quintic.py](../scripts/resume_m3/certify_q060_stage0_r_quintic.py)，精确多项式库直接导入冻结的
[certify_q060_stage127_r_quintic.py](../scripts/resume_n4/certify_q060_stage127_r_quintic.py)。该库的 stage 127 `main` 没有被调用或修改；首段的真背景覆盖与二次 Gram 合并在本次新源中明确实现。

所有 SHA、实际 exit 0 和输出摘要见
[2026-11-20-warm025-stage0-execution.json](2026-11-20-warm025-stage0-execution.json)。extract、export、certificate 三步均实际完成；最后一步约 8.427 秒，输出 SHA-256：

`dc15bf5a18520590baca931813fa5a47bd322c34062db4143138e4bd7dbe7903`。

~~~bash
python "$TOPIC/scripts/resume_n4/extract_q060_stage_from_native_record.py" \
  --checkpoint "$M3WORK/newg-wide-lambda0p002-m24-actual/tail_0001.json.gz" \
  --native-record "$M3WORK/newg-native-m24/runs/actual-lambda0p002/0009-jac-record.json" \
  --stage 0 --out "$WORK/stage0000-saved-native-input.json"

node "$TOPIC/scripts/resume_n4/export_q060_saved_stage_r_jets.mjs" \
  --input "$WORK/stage0000-saved-native-input.json" \
  --out "$WORK/stage0000-literal-r-data.json"

python "$TOPIC/scripts/resume_m3/certify_q060_stage0_r_quintic.py" \
  --data "$WORK/stage0000-literal-r-data.json" \
  --packet "$WORK/stage0000-saved-native-input.json" \
  --constants "$N4WORK/q060-tail-geometry/constants.json" \
  --normalization-certificate "$N4WORK/q060-tail-geometry/tight-integrals-certificate.json" \
  --library "$TOPIC/scripts/resume_n4/certify_q060_stage127_r_quintic.py" \
  --quadratic-mode-cutoff 12 --out "$WORK/stage0000-shared-r-certificate.json"
~~~

保存数组及完整有理逐片输出只留 scratch；库内仅保留源码、参数、运行绑定和结论摘要。对原 source midpoint 的差也只作为新图与字面有限数据在那些平面的差，不外推为全区间旧 PDE 图的误差证明。
