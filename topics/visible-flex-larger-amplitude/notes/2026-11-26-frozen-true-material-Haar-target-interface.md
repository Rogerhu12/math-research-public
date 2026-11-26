# R691 真材料 Haar 的固定完整目标与全变量数值接口

**状态：完整源及解析接口已形成，只有静态 AST/compile/字面键检查；尚无本入口的 Actions 科学返回。** 当前深谷固定 $g_n=ds^2+a_n^2d\theta^2$ 的实际分支继续。本文入口明确选择另一个完整固定目标，不把它当作原 $g_n$ 的精化，也不把有限角矩误差当成精确非圆解的存在证明。

源码：

- `scripts/resume_20261126/frozen_material_haar_metric.py`，31561 B，SHA-256
  `c5a717dbca55311060207672c703293403c16c6e5142b84cc522e660afc67a64`。
- 必需准确角矩源 `material_haar_moments.py`，32690 B，SHA-256
  `1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010`。
- 向外整数算术仍为 R690 `deep_valley_tail_input.py`，SHA-256
  `e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2`。

## 1. 准确目标、当前材料角与工作求积的区别

冻结一个实际完成报告所对应的完整 canonical 场 $F_*$，包括它的全部 core、共享 quintic $q_*$、$H_*$、准确 scalar/lift、完整 symbolic 节点及来源。设它的材料角为 $\theta=\Theta_*(\phi)$，$\rho_*=\Theta_{*,\phi}>0$。定义同一个准确连续目标

$$
g_*=E_*(s)\,ds^2+C_*(s)\,d\theta^2,
\qquad
E_*=\frac1{2\pi}\int_0^{2\pi}\rho_*|F_{*,s}|^2\,d\phi,
\qquad
C_*=\frac1{2\pi}\int_0^{2\pi}\frac{|F_{*,\phi}|^2}{\rho_*}\,d\phi .
$$

混合项的完整材料平均为 $(2\pi)^{-1}\int F_{*,s}\cdot F_{*,\phi}\,d\phi=0$，由完整反射奇偶性准确成立。后继的当前 core 可改变 $\Theta_{\rm current}$，但目标 $E_*,C_*$、冻结权重 $\rho_*$ 与其准确角矩都不改变。所有当前 Gram 项仍在当前材料坐标下计算。

角矩求积用的 $Q,p$ 及其有效包围是工作精度。它们**不定义这个目标**。提高 $Q$、换成同一准确角积分的更紧合法盒，不改变 target identity；也不能只将某个中点向量命名为“准确 Haar”。当前求解角网格 $N_{\rm current}$ 同样不是目标定义。

这个选择处理 R691 已指出的准确材料平均端部相容恒等式；该必要恒等式不构成任意冻结目标都可精化成精确非圆 flex 的充分定理。程序所有 existence/metric/geometry/refinement 认证旗标初值均为 false。

## 2. 完整物理身份先核定

`freeze_actual_report` 必须消费实际已完成科学报告及其实际 final bundle；先核 bundle SHA 与报告、完整 canonical definition 与其 SHA、bundle 内 literal model 相同。角矩 carrier 还必须来自这个实际 bundle 的全部 core；它的 angular definition 必须与重新读出的完整 core 定义相同。

数学身份绑定五项输入的实际 SHA：

1. 完整 frozen bundle；
2. 对应准确 symbolic node report；
3. 原 scalar input；
4. 当前完整 observation carrier；
5. bundle 自己声明的 reference/lift carrier。

绑定全部实际 evaluator、moments、arithmetic、factory、dense operator、batch、observed、scalar、integer、hold 源。深谷场另绑定原 base factory 与新 deep scalar。各源先对报告里的实际 SHA，再对 canonical 的 scalar/operator/source 记录；没有用一个 factory SHA 冒充另一个。

允许的物理模型为真实 R671 factory `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216`，或新深谷 factory `4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1`。当前角矩入口的 literal 端部检查使用 $\lambda=1$ 的全零末端 $q$ 接口；不以未核过的 $\lambda<1$ 场绕过它。实际 constructor 正常调用相应 `TailLiftContext.from_files/create_pair`，并在构造后再次比较完整 model，不能只核几个自报字段。

manifest 的准确 target identity 为标准排序紧凑 JSON 的 SHA-256，payload 包含：

- schema、完整 canonical model 的已核 SHA、完整 angular definition 的已核 SHA；
- 五项输入 SHA、全部源 SHA；
- 固定 $S,R,\text{width}$ carrier literal、固定前三 core、准确物理 $\eta$ 的 affine 表达；
- 本文准确 mean definition 和 R661 闭面 cap recipe。

所有路径、运行统计、运行号、来源报告、working moment carrier SHA、工作 $Q,p$ 不进入这个 payload。完整 canonical/angular definition 分别经自身已核 SHA 进入。原 bundle 和 reference carrier 是这个实际冻结场的输入，不能在“改善角矩”时替换。只有同一 frozen bundle/core 的更紧完整角矩 carrier 可以作为工作替换。

manifest 创建入口拒绝覆盖既有文件，以免同路径暗换目标。数值消费者还逐个核实际输入与源的 SHA；旧绝对路径消失时，可用 manifest 的 repo-relative 源或显式 byte-equal override 恢复，不伪造旧路径或旧源码身份。

最终 c5a 来源恢复接口也覆盖创建 manifest 之前的实际报告：`source_from_report` 按实际报告记录的源路径、其中 `topics/visible-flex-larger-amplitude/` 的准确仓库后缀，以及显式 role override 寻找同一份源码；每个候选都必须与该报告记录的 SHA 完全一致。成功记录同时保留实际可读路径和原报告路径。创建命令的 `--source-overrides` 接收 physical role 到同字节文件路径的 JSON；`--input-overrides` 只允许非 bundle 的同字节输入恢复。冻结 bundle 仍必须由显式 `--bundle` 指定并与实际 report/final SHA 相符，own reference carrier 还必须与 bundle 内声明的 SHA 相符。数值 constructor 同样接收 `source_overrides`、`input_overrides`。这些工作路径不进入数学 target identity；恢复路径不改变来源、目标或物理场。

## 3. 任意新径向点用完整公式求值

令 $B_i(\phi)$ 为 R691 的完整旋转 Fourier 基，$L_*=\sum q_{*,i}B_i$，并记

$$
P_{ij}=\langle\rho_*B_i\!\cdot B_j\rangle,\quad
Q_{ij}=\langle B_{i,\phi}\!\cdot B_{j,\phi}/\rho_*\rangle,\quad
\ell_i=\langle B_{i,\phi}\!\cdot e_t(\Theta_*)\rangle,\quad
b_i=\langle\rho_*B_i\!\cdot e_z\rangle.
$$

准确分部积分同时给 $\ell_i=\langle\rho_*B_i\cdot e_r(\Theta_*)\rangle$。两式使用同一准确向量，不分别冻结两个有求积差的向量。令 $u_*=q_{*,s}$，$d_*=h_sH_*+k_s$，则

$$
E_*=u_*^TPu_*+2f_s\ell^Tu_*+2d_*b^Tu_*+f_s^2+d_*^2,
$$
$$
C_*=q_*^TQq_*+2f\ell^Tq_*+f^2.
$$

这些是整个连续 $s$ 域的公式，不是已知网格 mean 数组的插值。完整 $P,Q,\ell,b$ 的模式、连接项、reciprocal moments 与完整求积尾已在配套角矩说明证明。

`FrozenHaarTarget` 正常重建冻结原场；一个仅用来满足原 operator 结构的角网格取最小 $2^k>4M_*$。这个 structural grid 不参与上面的积分目标。冻结 q jets 与 frozen core 不从当前场借用。

后继当前 mesh 的每个准确 affine 端点必须位于一个冻结 cell 内；源码先定位候选 cell，再以 Fraction 严格核二元 affine 共线性、$0\le u\le1$ 与正确方向。当前观察位置通过准确 affine 组合映射到冻结 cell。转回 binary64 的 local $u$ 误差有单独精确分数报告，未把它当零。当前 finer $M,N$ 不改变 frozen $M_*$ 与积分权重。

新点的 $q_*,q_{*,s}$ 由该冻结 cell 的完整共享 quintic 六端 jets 求值；$f,f_s,h_s,k_s$ 由同一 canonical analytic profile 求值。若恰好命中冻结场已保存的同 cell/literal-$u$ 观察点，保留该 frozen field 自己的 saved scalar9 working carrier；新点仍使用同一准确 scalar/lift 的数值实现，绝不插值一份旧 mean 数组。

当前 $\lambda$、scalar input/source、准确 $\eta$、domain、固定 core datum 必须与 frozen model 相容。深谷 profile definition/identity、新 deep source 与 base source 也必须逐项相同。当前 $q,H$、非固定 core、精化 $M$ 和 mesh 可以变化。

数值 `evaluate_locations/evaluate_for_operator` 使用完整 moment 中点矩阵。它报告 positivity 的数值值及所有 working identities，但明确 `numeric_matrix_and_radial_arithmetic_certified=false`。严格连续包围另用完整 coefficient intervals 与径向误差；不能因为 moment 自己有严格区间，就将普通 NumPy 二次型当作严格浮点包围。

## 4. 完整固定目标 $J/J^*$ 的准确链

原 full operator 对固定 scalar $a(s)$ 返回

$$
r^{(0)}=\left(G_{ss}-1,\ \frac{G_{s\theta}}a,\
\frac{G_{\theta\theta}}{a^2}-1\right).
$$

在每个当前径向观察点，设冻结正数 $A=E_*(s)$、$D=C_*(s)/a(s)^2$。新完整相对 Gram 为

$$
r^{(*)}_1=\frac{1+r^{(0)}_1}{A}-1,\qquad
r^{(*)}_2=\frac{r^{(0)}_2}{\sqrt{AD}},\qquad
r^{(*)}_3=\frac{1+r^{(0)}_3}{D}-1.
$$

因此 $S_*=\operatorname{diag}(A^{-1},(AD)^{-1/2},D^{-1})$ 为固定行缩放，所有原自由变量的导数准确为

$$
J_*=S_*J_0,\qquad J_*^*=J_0^*S_*.
$$

源码 `FrozenHaarOperator` 保留原 full residual 的每一行、quarter orbit multiplicity、所有原 core/$\rho$/$q,H$ 导数。固定 $A,D,S_*$ 只在建立这个当前网格上的 wrapper 时求一次并设 readonly；没有当前均值微分、均值投影或删 mean 行。原源的 `set_base/clear_base` 仍正常调用。重建更细网格上的 wrapper 求的是同一准确目标在新点的工作值，不是更新目标。

完整 QP driver 若选用本分支，仍需保留原全部变量、原母范数、当前 full Gram、全部 geometric rows、两支 amplitude rows、永久位置与真实线筛。此文件提供可运行 fixed-target operator，不会自动修改已排的 moving-mean 或 deep-fixed-scalar driver，更不会让旧目标的 $\Phi$ 差成为新目标下降证据。新的 driver/source provenance 应如实登记。

## 5. 连续证书的完整区间接口和可用公共项

角矩源的 `MomentKernel.enclose_means(q,qs,f,fs,zs)` 以 72 位向外整数区间消费**所有** $3M_*+2$ 个 frozen $q_*,q_{*,s}$ 和 $f,f_s,d_*$；用完整 interval $P,Q,\ell,b$ 二次型返回 $E_*,C_*$ 的合法包围。其每个输入都必须覆盖准确 symbolic 径向片上的真实量，含 reference/求值误差。未知量用完整区间，不得把 ordinary float 的值当成点区间。

在当前场和 frozen 场具有**同一准确 scalar、$\lambda,\eta$、物理宽度**的条件下，设当前

$$
F=L+f e_r(\Theta)+(hH+k)e_z,\quad
X=L_s,\quad Y=L_\phi/\rho,\quad d=h_sH+k_s.
$$

定义 $u_*=q_{*,s}$。完整材料 Gram 与冻结目标之差可以准确写成

$$
\begin{aligned}
N_{ss}={}&|X|^2-u_*^TPu_*
+2f_s\bigl(e_r(\Theta)\!\cdot X-\ell^Tu_*\bigr)\\
&+2dX_z-2d_*b^Tu_*+(d-d_*)(d+d_*),\\
N_{\theta\theta}={}&|Y|^2-q_*^TQq_*
+2f\bigl(e_t(\Theta)\!\cdot Y-\ell^Tq_*\bigr),\\
N_{s\theta}={}&X\!\cdot Y+fX\!\cdot e_t(\Theta)
+f_se_r(\Theta)\!\cdot Y+dY_z .
\end{aligned}
$$

这里 $f_s^2$ 和 $f^2$ 才是共同准确项，已代数抵消。$H$ 可改变，故 $d$ 与 $d_*$ 一般不同；相关项必须照公式支付。即使 $\eta=1$ 的末尾使某些项为零，也不能把这个局部性质无条件扩到全部 $s$。

严格消费者应使用 current/frozen exact cell、scalar/cutoff、$\eta$ 与准确尾分界的共同分割。在每个共同片上包围上面三个分子及 $E_*,C_*$，先取得 $E_*\ge e>0,C_*\ge c>0$，再由

$$
|r_{ss}|\le\overline{|N_{ss}|}/e,\quad
|r_{\theta\theta}|\le\overline{|N_{\theta\theta}|}/c,\quad
|r_{s\theta}|\le\overline{|N_{s\theta}|}/\sqrt{ec}
$$

取得完整二维相对矩阵上界，例如
$$
\|r\|_{\rm op}\le
\sqrt{r_{ss}^2+2r_{s\theta}^2+r_{\theta\theta}^2}.
$$

它要求覆盖全部径向片、全部角区间、完整 retained Fourier 和所有高模及 infinite scalar tail。该分子恒等式只把 R689 已证明的公共项抵消应用到本次准确 Haar 二次型；它不省去任何几何或归一化责任。本文件尚未把整个 strict common-partition field consumer 跑出一次有效 whole-domain 报告，所有相关标志保持 false。

## 6. 可实际排入 Actions 的调用

先用独立角矩入口消费选定实际 bundle；所有 carrier/journal 放 runner scratch：

```sh
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/material_haar_moments.py \
  --repo "$REPO" --bundle "$ACTUAL_FINAL/final.npz" \
  --angles 8192 --derivative-order 12 --target-moment-error 1e-14 \
  --admission-seconds 900 --maximum-new-orbits 4096 \
  --moments "$WORK/true-Haar/moments.json" \
  --journal "$WORK/true-Haar/journal.json" \
  --out "$WORK/true-Haar/moment-batch-0001.json"
```

若自然预算只返回部分完整 orbit，按同一 journal/实际 source/core/run 续接，换一个新的小 report 路径；不能将 partial carrier 伪装成 complete。请求精度未达而返回合法完整盒时，仍是这个准确目标的有效工作包围；后继数值使用必须看实际宽度。没有另设科学 fixture 或新的必须通过门。

角矩真的 complete 后，冻结实际同场完整目标：

```sh
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/frozen_material_haar_metric.py \
  --repo "$REPO" --report "$ACTUAL_FINAL/report.json" \
  --bundle "$ACTUAL_FINAL/final.npz" \
  --moments "$WORK/true-Haar/moments.json" \
  --out "$WORK/true-Haar/frozen-target.json"
```

这个创建命令本身写小 manifest 与小 stdout identity。numerical consumer 的准确 API 为：

```python
target = haar.FrozenHaarTarget(
    manifest_path, repo=repo,
    input_overrides=optional_same_byte_input_paths,
    source_overrides=optional_same_byte_source_paths,
    moment_carrier=optional_tighter_same_field_moment_carrier,
    stage_block=64)
problem = haar.FrozenHaarOperator(original_complete_current_operator, target,
                                 stage_block=64)
# 原完整 driver 的全部 residual/J/J* 调用使用 problem。
# 形状/幅度/closure 仍使用真实 original_complete_current_operator 对应的同一场。
```

`moment_carrier` 省略则读 manifest 记录的工作 carrier。完整 identity 对上述可替换工作盒不敏感，具体科学报告必须记录实际使用的 moment SHA、工作 $Q,p$、来源 source SHA 和本次 target identity。

## 7. 已做和未声称的边界

已完成：完整准确 Haar 数学定义、角矩严格误差入口、完整冻结来源身份、任意嵌套新点的数值目标求值、原 full $J/J^*$ 的固定正行缩放，以及相应连续分子恒等式。

仅做源级 AST/compile/字面键检查；未在本地科学运行，未产生或伪造实际 moments/target report。尚不声称实际角矩返回、完整 whole-domain target positivity、相对误差证书、同 $g_*$ 多层精化、闭面 geometry、20% held amplitude、reach 或完成课题。

后继若进入这个明确的新目标分支，同场 geometry $D/L/K/\rho/$support 必须来自它自己的实际候选与完整覆盖。原 fixed $g_n$ 或 finite-physical-mean 场的几何和目标残差均不跨场继承；source/report 复用只能复用真实相同的数学与字节依赖。
