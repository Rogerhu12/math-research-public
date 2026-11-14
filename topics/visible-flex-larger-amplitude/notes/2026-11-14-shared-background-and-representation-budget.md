# 同场共享背景规范形与闭曲面的必要表示误差账

2026-11-14，exact_refinement，AI 辅助。

**本次落实一个可执行的有限背景定义，并给出真实接受包到 operator、法向、曲率及 held/reach 输入的误差账。没有本题完整新父场，故尚未执行此准备器，也没有新的几何通过结论。** 不要求额外的机器精度六 jet/九 jet 门；以下界只服务于 README 已有的 C²、等距误差、曲率、reach 和幅度条件。

相关已证公式见 [R245](../results/R245-hermite-compatibility-and-integrated-velocity.md)、[R249](../results/R249-shared-node-inlet-parity-normal-form.md)、[R251](../results/R251-direct-relative-operator-metric-certificate.md)、[R258](../results/R258-complete-field-tail-cardinal-marker-chain.md)。本记录组合其构造与接口，不另占 R261。

## 1. 最小必需的对象区分

最终连续对象取完整共享节点实 Hermite 规范形，记为 $F_*$；实际输出位置和 jets 记为 $\widehat F^{[i,j]}$。后者未必是某一个连续函数的真导数：原节点覆盖、独立舍入系数、clip 和单独背景列都可能破坏字面导数身份。因此

\[
e_{ij}=\sup|\partial_r^i\partial_\theta^jF_*-\widehat F^{[i,j]}|
\]

首先是一张**分片导数/报告值比较账**，不能未经拼接论证就称两个全局 C² 函数的差。

最省计算的认证路线是直接对 $F_*$ 付连续 operator/曲率界，再把现有 cover 的实际浮点中心和法向当作需要误差包络的近似值。这样不必先证明旧 renderer 在全域已是 C²，也不用把旧 A 几何结论移植进来。只有确实复用一个已经严格支付的旧连续几何界时，才需要完整的转移式。

## 2. 原背景的实际接口和一个确定的 C² 替代定义

`exact_20261114_closed_background.mjs` 保存本 plan 请求半径上的 `heightFromRToCut,w,wr`。前两者分别来自原 primitive 与原斜率表达式，`wr` 又由源 geometry 给出；cuff 行显式设 `w=wr=0`，高度取有限 160-cell 和，并保条件性的 deep omission。`RefinedAssembly.tail_jets` 只按半径查这些行，分别用于位置、一导和二导。该表没有定义节点间任意半径上的一个连续位置函数，`splitPrimitiveDifference` 和逆半径 residual 也不是其严格积分误差界。

新增独立准备源：

```text
computations/geometry_20261114_shared_background_normal_form.py
SHA256 da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9
```

它通过已绑定完整 v3/v4 / R249 bundle 的 loader，读取本次全部 `plan.background_radii` 和对应原表。令 $\sigma=-1$，原组装中的 offset 为 $o$，按原 `tail_jets` 相同 NumPy 标量运算生成并保留实际输出位值：

\[
b_i=\operatorname{fl}(o-\sigma h_i),\qquad
v_i=\operatorname{fl}(\sigma w_i),\qquad
a_i=\operatorname{fl}(\sigma w_{r,i}).
\]

每个输出均直接调用其实际 dtype 标量的 `as_integer_ratio()`，不经 Python float 或短小数转换。把这些值解释为精确实数，在相邻共享半径之间定义唯一的实 quintic $B$，匹配 $(b_i,v_i,a_i)$。

由 Hermite 唯一性，$B\in C^2$。准备器逐单元核全部六个端点恒等式，保存精确系数以及 $B,B',B''$ 的整单元 Bernstein 上下界。每个原表节点上，新 $B$ 的三个 jets 与被选中的**实际 scalar 输出值**的差精确为零；这不等于已经证明节点之间与旧 primitive 的差为零。

cuff 的实际原数据必须严格满足

\[
(B,B',B'')(r_{\rm cuff})=(h_{\rm cap},0,0),\qquad h_{\rm cap}>0,
\]

其中 $h_{\rm cap}$ 就是原 assembly 保存的帽高；不重新做绝对高度配准。于是旋转圈背景在 cuff 与原固定帽平接触。非轴 collar 的三个 jets 在 cuff 为零，四个 marker 的支撑又严格在帽内，故这些原件结合时付清 cuff 的 C² 拼接。帽和 marker 坐标保持原件。

这一步定义了新的有限背景场，**没有改变目标 $g$**。不能为了让误差消失，把原 tail 的 $E(r)$ 偷换成 $1+B'(r)^2$。连续 operator 和曲率必须对新 $B$、同一旧固定 $E(r)$ 计算。若当前背景节点不够细，可在相同 frozen source 上增加背景查询节点，再定义更细的 $B$；这不重解非线性 tail，也不更换 $g$。同 g 比较分别绑定各个有限场自己的背景 descriptor。

## 3. cut 绝对均值和整角修补必须一同重定义

设同一完整 prefix 在 cut 的目标径向 jets 为 $T_0(\theta),T_1(\theta),T_2(\theta)$。仍用原 producer 已锁定的非零 chart jets $v=dr/ds<0$、$b=d^2r/ds^2$：

\[
T_0=P,\qquad T_1=P_s/v,\qquad
T_2=P_{ss}/v^2-bP_s/v^3.
\]

这指定了切口的局部坐标转换；不借此把有限 Gauss 标量的独立返回 `ap/app` 冒称为其真实全函数导数。所有固定 metric 的实际定义仍需沿原 scalar descriptor 使用。

令 $U$ 为同一完整 FFT 共享节点扰动。新 native 场是

\[
G_*(r,\theta)=r e_r(\theta)+B(r)e_z+\operatorname{diag}(1,1,\sigma)U(r,\theta).
\]

必须重新定义**完整整角**

\[
\Delta_i^*(\theta)=T_i(\theta)-\partial_r^iG_*(r_{\rm cut},\theta),
\]

再用 R258 的精确起点、精确宽度 Hermite selector 加回。selector 在 cut 的三阶端点矩阵为单位阵，因此最终三个径向 jets 对每个角度都等于 $T_i$，其角导数和绝对材料均值也相同。只保非均值、只修一个平均数或者复用旧独立浮点 delta 数组都不够。

准备器保存完整材料均值的精确公式

\[
\bar Z^{(i)}=z_0^{(i)}+\frac12\sum_{m=1}^M(1-4m^2)c_mz_m^{(i)}
\]

及其径向转换，保存完整 outer FFT 的零模 jets，明确输出需要的三项 mean correction。它还单列原 `native_cut_nine` 所取 readout geometry 的背景 jets 与原 heights 表背景 jets 的差，避免混淆两个实际来源。完整角函数仍按上一式构造；三个均值本身不替代整角匹配。

**为什么不需要重算非平面性。** 改 $B$ 只改共同、与 $\theta$ 无关的高度项；相应重定义 $\Delta_i$ 也只增加共同高度修补。因此对每个固定 $r$，所有

\[
F_*(r,j\pi/2)-F_*(r,0)
\]

严格不变。R258 的全部四角行列式证据原值可保，新增背景节点也不会改变这个恒等式。原帽高保持时，marker 支撑中心证据同样不变。实际转用时须把旧证明 SHA、新背景 descriptor SHA 与“仅共同背景及其 mean cut correction 改变”的构造身份明确绑定，不能只换文件名后声称旧全场几何均已继承。

结合 R249 的 core 反射规范形、共享物理 prefix、共享 FFT tail、上述完整 cut/cuff 匹配和固定 smooth marker，可在精确有限定义中支付整个位置函数的 C²；浸入、等距、曲率、reach 和 held 仍各自计算。无需额外追求一个无限 PDE 解才允许定义这个有限闭面。

## 4. 节点、FFT 和径向系数的最小误差账

### 4.1 哪些数字是定义数据

完整 accepted checkpoint 的共享物理节点、实际 FFT 节点系数及本准备器选择的背景节点，是有限规范形的定义数据。把它们的实际二进制值精确解释为实数，本身没有额外的“FFT roundoff 误差”需要支付。是否逼近真正连续解，属于同 g 精化的另一条实测链。

但不能用原 raw 四角数据冒作浮点 FFT 后的四角。R258 已消费实际全部 FFT 系数；实际 dtype 若只从 complex128 无损扩展到 clongdouble，可用回扩严格相等后的小端 complex128 编码。对真正含额外 longdouble 位的中间 Hermite 系数，须逐实/虚标量取精确整数比；不得先降为 float，也不得把 padding bytes 或显示小数当作可移植实值身份。

### 4.2 精确节点多项式和实际舍入系数 shadow

对某个单元，精确节点为 $r_i,r_{i+1}$，$h=r_{i+1}-r_i$。实 Hermite 规范形写成

\[
P(r,\theta)=\Re\sum_{q=0}^5 C_q(\theta)u^q,\qquad u=(r-r_i)/h.
\]

把原程序实际产生的有限系数 $\widehat C_q$ 和实际宽度 $\widehat h$ 也按其二进制值解释为实数，则其未再舍入求值的单元 shadow 拉回同一个 $u$ 后，系数为 $\widehat C_q(h/\widehat h)^q$。因此

\[
D_q=C_q-\widehat C_q(h/\widehat h)^q
\]

就是同一真实单元的精确系数差；不能忽略薄单元中的宽度误差。

对正频率复系数定义保守而可用有理数计算的角向范数

\[
\|C\|_{(j)}=\sum_{k,\ell}k^j
 (|\Re C_{k\ell}|+|\Im C_{k\ell}|),\qquad 0^0=1.
\]

其中 $\ell$ 遍历三个 Cartesian 分量。则

\[
e_{ij}^{\rm coefficient}\le
h^{-i}\sum_{q=i}^5\frac{q!}{(q-i)!}\|D_q\|_{(j)},
\quad i+j\le2.
\]

更紧的界是先对每个实/虚分量精确求导、转 Bernstein 控制系数，再取凸包最大值和上述角频率权重。这只是有限线性运算。prefix 在 $\phi$ 中的旋转框架须用 R249 的 $(2m+1)^j$ 水平权重，再拉回同一个材料角，不能漏框架频率。

原程序在共享节点直接返回保存 jets 的 override，与规范形在该节点严格相同；单元左右极限则各由其 shadow 界覆盖。小的跳量不能单独被称为“已 C²”，但不妨碍新规范形通过共享节点真正是 C²。

R245 的兼容缺陷另给一个可解释的预算：

\[
E_i=d_{i+1}-d_i-h_i(v_i+v_{i+1})/2-h_i^2(a_i-a_{i+1})/12.
\]

相对于共享三次速度的积分，三个锐系数是 $1,15/(8h_i),10/(\sqrt3h_i^2)$。背景准备器逐单元保存 $E_i$ 和这三个界（最后一个以平方的精确有理数保存），不预先把 $E_i$ 称为舍入误差，也不把它冒作与 native primitive 或目标 $g$ 的误差界。

## 5. 角度、唯一 SE2 和外 patch 的账

材料密度的严格下界仍用原完整核心的 $\rho_*>0$。若在实际近似逆角 $\widehat\phi$ 上，对精确材料表达式得到严格 residual $|\Phi(\widehat\phi)-\theta|\le\varepsilon_\Phi$，则

\[
|\widehat\phi-\phi|\le\varepsilon_\Phi/\rho_*.
\]

用同一完整有限频率给出的导数和 R249 的材料拉回公式，可把这项传播到位置、切向量和二阶 jets。需要时，第三角导数只作为二阶读出误差的 Lipschitz 上界，由有限表达式直接计算；它不是新的曲面正则性或机器精度验收门。

实际 SE2 的数学定义是声明二进制角 $\beta$ 的真 $Q(\beta)$ 和原平移 $b$。用 Arb 包住 $\cos\beta,\sin\beta$，比较原打印矩阵 $\widehat Q$ 得 $\epsilon_Q\ge\|Q-\widehat Q\|_{op}$。位置一项乘 $|F_{xy}-b|$，正阶导数项乘相应 $|\partial F_{xy}|$。原平移保为精确二进制数据；它的求值舍入另计。只对确实同时受同一刚体作用的整块可用不变性消去配准；混合 prefix/native 的外 patch 仍保留这项。

外 patch 的精确起点是 $a=r_{cut}-W$。原程序先算的浮点起点 $\widehat a$、实际 $\widehat W$ 及 longdouble 权重系数都可逐值精确提取。将区间在 $a,\widehat a,a+W,\widehat a+\widehat W$ 处分开，连同 clip 的常数支路，逐段比较实际报告的权重 $\widehat W_k^{[i]}$ 与精确 $W_k^{(i)}$。有些 clip 支路上的原报告导数不等于 clipped 位置的字面导数，因此要逐项比较，不能先假定导数身份。

若

\[
\omega_{ik}=\|W_k^{(i)}-\widehat W_k^{[i]}\|_\infty,\quad
d_{kj}=\|\partial_\theta^j\Delta_k^*\|_\infty,\quad
\delta_{kj}=\|\partial_\theta^j\Delta_k^*-\widehat\Delta_k^{[j]}\|_\infty,
\]

则 patch 误差由

\[
e_{ij}^{patch}\le\sum_{k=0}^2
\bigl(\omega_{ik}d_{kj}+
\|\widehat W_k^{[i]}\|_\infty\delta_{kj}\bigr)
+e_{ij}^{evaluation}
\]

支付。前两项用实多项式 Bernstein、完整 Fourier/材料角和同一严格三角球得到。只需位置的两个角导时，式中会出现既有完整 cut 九 jet；这是所选整角 patch 的计算输入，不是新增的九 jet 机器精度完成门。

## 6. 不必为浮点库假定未经证明的 ulp 界

实际 mesh/normal packet 的点值和法向，可直接与同参数下的精确规范形 Arb 包围盒比较。这样从保存的浮点数减去严格球即可得到真实误差，包含系数求值、trig、材料逆角和一次 SE2 的误差；不必声称 NumPy 的每个三角函数都正确舍入。

反过来，只有已经证明了某个实际算子次序的浮点误差界时，才可用通用 $\gamma_n\sum|a|$ 取代这条比较。参数自身若以理想圆网格定义，也把实际浮点角/半径与声明参数之差计入一次，不能既忽略又在多处重复收费。

新背景在已有表节点的 scalar 输出差为零；任意中间点则由 descriptor 的实 quintic 明确定义。对新场直接计算包络，不必先付一个并未给出的旧 primitive 全域误差。若仍要比较旧 primitive，必须使用它本身的区间表达式或实际可证明的导数/求积界，表中 inverse/split 数字只作原诊断保全。

## 7. 把误差送到已有的几何门

### operator 与浸入

同一参考度量写成 $g_0=\beta^2du^2+a^2d\theta^2$。prefix 为 $\beta=1$；tail/collar 为 $\beta=\sqrt E,a=r$。令 $x=e_{10}/\beta_*$、$y=e_{01}/a_*$、$\epsilon=\sqrt{x^2+y^2}$。若确有旧连续归一化 Gram operator 界 $\eta$，R249 原式给出

\[
\eta_*\le\eta+2\sqrt{1+\eta}\epsilon+\epsilon^2,
\qquad \ell=\sqrt{1-\eta}-\epsilon>0
\]

时还保证新浸入。这里 $\eta$ 必须是 operator 界，不是三个分量或样点最大值。更直接的路线是针对 $F_*$ 用 R251 四正性，绕过旧连续 $\eta$ 的前提。

### 法向与曲率

仍用 R249 的

\[
\gamma=\sqrt{1+\eta}(x+y)+xy,\quad
\nu=\min\{2,2\gamma/(1-\eta)\},
\]

给单位法向的弦距离界；角误差可取 $2\arcsin(\min\{1,\nu/2\})$。对 tail，原归一化二阶向量按

\[
F_{rr}/E,\quad F_{r\theta}/(\sqrt E\,r),\quad F_{\theta\theta}/r^2
\]

排列，$\Delta_H^2=e_{20}^2/E_*^2+2e_{11}^2/(E_*r_*^2)+e_{02}^2/r_*^4$。若旧连续 $K,H_*$ 已付，则

\[
K_*\le\frac{(1+\eta)K+\Delta_H+\nu H_*}{\ell^2}.
\]

比较时保留完整 raw 归一化二阶空间 jets 的 $H_*$；不能把旧面的切向项先删掉，再用新法向而漏掉混合项。每张面自身的法向会消去变基导数带来的切向量，这正是 R249 证明可用于上述 tail 基的原因。帽中心 $r=0$ 用 Cartesian 正规坐标，不能套带 $1/r$ 的公式。

### reach 与 held

不能只给一个 C0 位置误差就把旧 reach 平移过去。应把新位置误差、法向角误差和真正的新 $K$ 送回原 R241 全连续空间 pair/局部门，保原全部门及余量。现有 full-state cover 的 `evaluation_position_error`、`normal_angle_error` 和 geometry envelopes 是这笔账的实际入口；同一个误差只计一次。

若每相位的连续像有 $e_{00}$ 的一致位置差，则两个相位间的 Hausdorff 距离最多差 $2e_{00}$，全族直径上界最多增加 $2e_{00}$。已有严格 held 下界 $L$、直径上界 $D_+$ 转移时可用

\[
\frac{L-2e_{00}}{D_++2e_{00}},
\]

前提是 $L$ 本来是整像连续下界且分子为正。若直接为新规范形更新原 position cover，则在原算法中计位置误差，不再另减一次。R248 的旋转/移角使同一精确有限场的这些解析误差界全相位保持；实际显示旋转的浮点评值仍按原 position/rotation 参数付费。

## 8. 新准备器 CLI、输出与后续唯一必要接线

```bash
python "$C/geometry_20261114_shared_background_normal_form.py" \
  --directory "$CLOSED" --basename surface \
  --checkpoint "$ACTUAL" --port "$PORT" --config "$CONFIG" \
  --tail-response "$FINAL_TAIL" --complete "$ACTUAL_COMPLETE" \
  --source-topic "$SOURCE_TOPIC" --out "$OUT/shared-background.json.gz"
```

只在公开仓库 Actions 执行。输入身份门与 R258 的完整 bundle 一致；完整背景表、完整 prefix、唯一 SE2、R249、same actual tail/config 都绑定。输出 schema 为 `actual-closed-shared-background-quintic-normal-form-v1`；保存所有精确节点/系数/连续单元界、R245 量、cuff 端点及完整 cut mean 账。`SharedBackground.from_record()` 会核 payload hash 并从共享节点重建系数，`evaluate_exact(r,derivative)` 返回精确有理值。

准备器本身不渲染新闭面、不输出 accepted checkpoint。真正接入时只需独立新 wrapper 做三件实质工作：geometry 的 tail 位置/一二导读取这同一个 $B$；`native_cut_nine` 与完整 `cut_difference` 按它重建且清掉旧 delta cache；在新的 plan/assembly/cover 身份中绑定 descriptor。已有 cap_height、markers、prefix、FFT nodes 与原 metric 源保持。

**尤其不能把 `A.height` 中用于参考 metric 的原 w 覆盖成新 B′。** 原 renderer 的 audit 用该表构造 $E_0=1+w^2$；若为图方便覆写它，就悄悄改了验证用的 $g$。应以独立 `shared_background` 几何 API 取 $B$，保原 metric table/source 单独取 $E$。

本次新源 AST 已过，未运行数值，未改任何冻结 producer。尚无完整 accepted 父场时，不调度这份几何准备，也不在旧 A 上补算来制造新结论。
