# 实际 support／Robin／bridge 端口：全文独立审查

日期：2026-11-10。审者：Astra-visible-flex-78718bd0 / independent_audit。

## 0. 结论、对象与严格范围

**结论：全文数学与实际源码接口核查通过；正式转录时须补明一处旧桥已审范围。**
被审对象为 [actual-port-transfer-v1](2026-11-10-78718-geometry-actual-port-transfer-v1.md)，13326 字节，SHA256 `4922ab60da4f8f361e21c01df13ec5e0ece4846b5f94c825ca370cb300b89f69`。作者稿保持冻结。本审者没有参与该稿推导，也没有选择或优化主数值候选的任何参数。

本稿确实给出径向背景上的位置 Jacobi 量、第二形式 Sturm 量、平面 support 入口、真实高度 Robin 行、bridge 拉回和实际反馈矩阵的准确关系。所有角阶因子、法向变化项、非齐次列和例外模态均须保留。它不是非径向 M14 当前算子的完整 provider，不证明任何实际反馈分母不为零，不证明新的闭曲面。

**必须澄清的范围。** 作者 §5 关于冻结二进 bridge 并非精确匹配根的论断，适用于 raw `Target` 和所读原数值实现。已审 [R21 §2](../results/R21-m12-whole-map-and-actual-metric-decrease.md) 已以两份 `root-exact-bridge` 证书支付主固定度量的同一个唯一精确桥及目标转移。本审实际重读了该节。因此不能把“主固定 g 尚未有精确匹配桥”列为新缺口，也不重开已审桥存在性门。现在未支付的是把新的传播／普通源／真实反馈表建立在所选实际桥上的论证。作者已同意这一澄清；它不改变本稿任何公式，也不改变主 g。

## 1. 实际阅读与证据

正文全部八节逐句阅读。对其七份源读取了所引用的完整函数，而不是只看注释：

- `PlanarSymmetryFlow` 的构造、`profile`、`linear_rhs`、`linear_terminal`、`backward_line`；
- `PlanarSupportCore` 的构造、`normal_geometry`、`arc`、`evaluate`、`parameter_derivatives`、`inlet`；
- `WarpedFlow.angular` 及 `WarpedBVP` 的构造、`initial`、径向端口；
- adaptive `Flow.geo`、`frame`、`adapt_fun`，以及 BVP 的 cut 角图；
- `TailMixin` 三个接口、完整 `AffineTailForInnerBVP` 和 `solve_with_actual_tail`；
- `DirectionalBridge` 的构造、`turn`、`integral`、`profile`；
- metric supplier 的说明、`Target` 构造、精确前缀与角图定义、边界 sliver 及终点差的输出。

另实际读旧 `finite-head-schur-interface-v2` §§1–5 与 `local-weighted-inverse-v1` §§1–4，用于核对原选定范围和全空间有界逆要求；并非声称重审其所有上游结果。以下七份实际源身份由本次独立重跑记录：

| 源文件（相对本题） | 字节数 | SHA256 |
| --- | ---: | --- |
| `notes/fixed_metric_mode3_flow.py` | 5131 | `0e5555fa23609e2e7154f0e952c6b7ddc402a4cf54be148842f36db886103dc5` |
| `notes/fixed_metric_mode3_core.py` | 10411 | `a529904e265ddc95635c6c6601ea173eb0e1383a75e458d3eaee024fe7078ead` |
| `scripts/950f-prefix-warped-bvp.py` | 19466 | `eb70e36397ea47638e042e7f2ef465ccef30cd853342adf049c2e3718261ac70` |
| `scripts/950f-prefix-adaptive-chart-bvp-v2.py` | 19011 | `958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe` |
| `scripts/db6f-prefix-coupled.py` | 12811 | `37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a` |
| `scripts/db6f-audit-metric-supplier.py` | 17450 | `de2cafcb235a843b2f930decb54cf065c6cbc441884b050f09edb900ac196bd0` |
| `repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_bidirectional_bridge.py` | 5123 | `85b9e746235a32c3e78229d6d1ddc424ee3497db3a8d61c858b14bc6534bf468` |

主要真实读取回执：正文 `777da6`、`3bbeed`、`eb6375`；源 `2b26a6`、`750f83`、`5e1840`、`d562f5`、`e94ca5`、`2b9484`、`4018c6`、`16e20e`；旧接口 `5ce1db`、`705169`；R21 `7529a5`。曾有两条只读请求被 exec-server transport disconnected 拒绝；它们未读取成功，之后 `fa9767` 实际 exit 0 恢复，不以断连推任何数学或求解状态。

## 2. 三个角与真实换元

物理角为 $u$，support 法向角为 $\phi$，数值图角为 $\psi$。代码的固定入口图是
\[
u_{\rm ref}(\psi)=\psi-\frac{8q_{\rm ref}}3\sin3\psi.
\]
`WarpedBVP.initial` 将该物理角传给 core 的真实弧长反解，再投影到有限 warped Fourier 空间；不能删去反解或投影误差。

adaptive `geo` 使用 $S(t)=10t^3-15t^4+6t^5$。在 cut 的 $t=1$，$1-S=S'=S''=0$，所以 $e=e_s=e_{ss}=0$；于是 $u=\psi$、$u_s=u_{ss}=0$、$u_\psi=1$，相应混合导数也一致。二阶恒等来自公式而非注释。内部一般 $u_s\ne0$；在固定物理角下
\[
\partial_s\big|_u=\partial_s\big|_\psi
-\frac{u_s}{u_\psi}\partial_\psi.
\]
源码的速度恰加 $u_sF_\psi/u_\psi$，所以不能将内部数值 $\psi$ 模当作物理 $u$ 模逐模传播。保持三重旋转对称的物理系数仍可有无限多个 $3k$ 模，有限数值表示不等于有限物理 Fourier 表。

## 3. 独立重算线性等距条件与移动法向

写 $N_n=n^2-1$，取 $|n|\ge2$，$a>0$、$c=a'$、$v=\sqrt{1-c^2}>0$。用转动基 $(e_r,e_\theta,e_z)$，对 $e^{inu}$ 模有
\[
\dot F=(f,if/n,h),\quad
\dot F_u=(iN_nf/n,0,inh),\quad
\dot F_s=(f_s,if_s/n,h_s).
\]
故 $\dot g_{uu}=0$，另外两项恰为
\[
cf_s+vh_s=0,\qquad
 af_s+N_ncf+n^2vh=0.
\]
解出作者 (5)，并逐项对照 `linear_rhs` 的 $m=n$：代码的局部 `v` 是本稿 $c$，代码 `b` 是本稿 $v$，记号差没有造成符号差。该恒等在整个允许径向背景上成立，不限于端点。

选 $d=(c,0,v)$、$T=(0,1,0)$、$N=(-v,0,c)$，则
\[
\dot d\cdot N=-f_s/v,\quad
\dot T\cdot N=\frac i a(-N_nvf/n+nch),\quad
\dot N=\frac{f_s}{v}d-rac i a(-N_nvf/n+nch)T.
\]
对于 $C=F_{uu}\cdot N$，先保留两项得到
\[
\dot C=N_nvf-n^2ch-\frac{ac}{v}f_s.
\]
代入线性等距方程后，$h$ 两项抵消，$v^2+c^2=1$ 给 $\dot C=N_nf/v$。

对 $M=F_{su}\cdot N$，两项分别是
\[
\dot F_{su}\cdot N=-\frac{i(N_n+c^2)}{nv}f_s,
\]
\[
F_{su}\cdot\dot N=\frac{icN_nv}{na}f-rac{inc^2}{a}h.
\]
其和减去 $-iN_n(f_s-cf/a)/(nv)$，等于
\[
-\frac{ic^2}{nv}\bigl(f_s+N_ncf/a+n^2vh/a\bigr)=0.
\]
这补全了作者省略的中间代数，并确认移动法向的贡献不可省。

背景 $C=av,M=0$，故
\[
\beta=\dot b=\dot M/v,\quad
\pi=\dot p=-a\dot C/(a^2v^2)=-N_nf/(av^3).
\]
以 $\bar p=1/v$ 归一化，得到
\[
x=av\beta=a\dot M=inN_n(h+cf/v),\qquad y=v^3\pi=-N_nf/a.
\]
反变换、行列式分别为
\[
f=-ay/N_n,\qquad h=x/(inN_n)+acy/(N_nv),\qquad
\det= inN_n^2/a\ne0.
\]
其 $n^2,n^3$ 阶数真实存在，不能在位置范数与第二形式范数之间免费消去。

还直接复核了它与 R75 Sturm 方程的关系。因
\[
H=\frac{dr}{ds}=v/a^2,\qquad V=a^3c'/v^4,
\]
有
\[
y_s=-\frac{N_n}{a}(f_s-cf/a)=-inH x.
\]
又 $h_s+cf_s/v=0$、$(c/v)'=c'/v^3$，所以
\[
x_s=inN_nc'f/v^3=-inH V y.
\]
因此换元后的系统确是 $x_r=-inVy,y_r=-inx$。这里核的是齐次位置 Jacobi 关系；任意不同实现的 inhomogeneous metric source 不能不经相应变换就冒称已付。

$n=0,\pm1$ 的反变换失效，不能令分母取极限来删除低维兼容。非零三重对称物理模为 $n=3k$，均值、刚体以及其它闭合行仍须按原问题保留。

## 4. 真 support 入口与核心端口

对 $H(\phi)=1+\sum c_k\cos(3k\phi)$，位置为
$\gamma=H e_r+H'e_\theta$，故 $\gamma_\phi=(H+H'')e_\theta=\rho e_\theta$。
严格 $\rho>0$ 时弧长提升
\[
A_c(\phi)=\phi+\sum\frac{1-9k^2}{3k}c_k\sin(3k\phi)
\]
满足 $A_c'=\rho$、$A_c(\phi+2\pi)=A_c(\phi)+2\pi$，存在真正周期弧长反解。

柱边 $a=1$、$d=e_z$，取 $N=-e_r(\phi)$。因为
$\gamma_{uu}=-e_r/\rho$，$C_0=1/\rho,M_0=0$，于是 $p_0=\rho\circ A_c^{-1}$、$b_0=0$。
固定 $u$ 微分 $A_c(\phi)=u$，得到 $\dot\phi=-\dot A_c/\rho$，从而
\[
\dot p_0=\dot\rho-\rho_\phi\dot A_c/\rho.
\]
这不是非圆背景下的对角物理 Fourier 乘子。

在圆背景 $c=0,a=v=1$，平面变化 $h(0)=0$ 正好给 $x(0)=0$。在
$z_\pm=(x\pm y)/\sqrt2$ 中就是 $z_-(0)=-z_+(0)$。它是实际反射行，不是允许任意 incoming 数据的声明。

当前固定入口的实际 $q=q_{\rm seed}e^{p_0}$，另外 M14 有 13 个高 support 修正；`initial` 还真实做有限投影。若要求全角恒等 $\phi=\psi$，由 Fourier 唯一性必须 $q=q_{\rm ref}$ 且全部高修正为零。本次没有读候选数组来预设这一特例，也没有把 core 数值反解／投影误差当精确零。

## 5. 任意截面的 Robin 行及强制列

从 $h_s=N_nc^2f/(av)+n^2ch/a$ 与 $h_s-\lambda_nh=\eta_n$，代入反变换，乘 $inN_n$，得到
\[
B_nx+iK_ny=inN_n\eta_n,
\quad B_n=n^2c/a-\lambda_n,
\quad K_n=nc(c-a\lambda_n)/v.
\]
所有因子均与作者 (14) 一致。$c\ne0$、$|n|\ge2$ 时，若 $B_n=0$，则
$K_n=-nN_nc^2/v\ne0$；所以不存在零行，也没有因为除 $B_n$ 而漏掉合法方向。

齐次解线为 $(-iK_n,B_n)t$，它的 $J$ 通量 $2\Re(\bar x y)$ 为零。于是
\[
\mathcal R_n=\frac{B_n-iK_n}{-B_n-iK_n},\qquad |\mathcal R_n|=1.
\]
分母非零由实 $B_n,K_n$ 及不同时零严格保证，不是浮点下界。为完整说明源的符号，本审展开同一行：
\[
z_+(R)=\mathcal R_nz_-(R)
+\frac{\sqrt2\,inN_n}{B_n+iK_n}\eta_n.
\]
因此普通边界源确有三次角因子和真实分母；它不能从齐次反射相位中省掉。

## 6. 理想 cut、真非线性尾与已审精确桥

在作者 (16) 的理想匹配关系下，$\sigma\in\{-1,1\}$（代码 `sign` 加非零检查），$E=1+w^2$、$w>0$。将 $h_s=\sigma D_nh/\sqrt E$ 代入线性位置系统，精确得到
\[
f/h=\sigma w(aD_n-n^2)/N_n.
\]
这就是 `linear_terminal`，其中 $a$ 须真等于 cut 半径。再代入第 3 节得到
\[
(x,y)=h\left(in(aD_n-1),-rac{\sigma w}{a}(aD_n-n^2)\right).
\]
$aD_n=n^2$ 只使 $y=0$，向量仍非零，未发生失效。

**原代码 raw bridge 与主精确目标须区分。** `DirectionalBridge` 用 64 点求积和浮点根产生 $L,p_t,p_s$；`Target` 把所提取的二进常数固定，以真 sine 积分和余项界定义 raw analytic bridge，保存其实际终点半径／导数差及坐标差。由此不能无误差给 raw bridge 强加理想 (16)。但是 R21 §2 已以唯一根证书和同材料坐标的转移给出主 g 所用的同一精确桥；本审接受该已审中间结论。本稿正式版本应将原“若求严格精确闭合……”解释限定于尚未采用该转移的 raw 对象，避免暗示原已审精确桥不存在。

当前 `TailMixin` 的原边界是
\[
H_{\rm tail}=\sigma q,y_{\rm height},\qquad
q,y_{{\rm height},s}-\mathcal T(H_{\rm tail})/\sqrt E=0.
\]
对位置高度 $h=qy_{\rm height}$ 的导数为 $\sigma D\mathcal T/\sqrt E$。对程序状态再乘 $q$，源码 `bc_jac` 恰用完整 `(3M+2)×M` heightJetJacobian 的前 M 行，而非径向 $\operatorname{diag}D_n$。切口的角图二阶恒等说明这里的径向高度导数没有内部角漂移项；它不使真非线性 DN 变成对角算子。

`seam_audit` 另取真尾请求，保留 mean first/second、nonmean first/second 与完整 C1 metric 行。`AffineTailForInnerBVP.solve(audit=True)` 明确拒绝，`solve_with_actual_tail` 在每次内步后恢复真实 tail，再对真实候选调用尾和原 BC；作者对 affine／真尾的作用域判断准确。本审没有触发任何尾请求。

## 7. bridge 回拉、普通源和真正反馈

第一周期的末端是 $T_u+T_d$，不能与 `Target.end` 混同。完整 bridge 用 $a_s=\sigma\sin\varphi$ 接在周期以后；其实际 cut 的 $a,c$ 与周期端的 $1,0$ 不同。`Target.end` 保留几何元数据的二进 end，相关坐标舍入／边界 sliver 在原证书中有账。

在 $a>0,|c|<1$ 的所选真实桥上，第 3 节变换和 Sturm 系统继续有效。记 transformed radial coordinate 的终点为 $r_*$（与 cut 的物理半径区分），则
\[
Z(r_*)=T_n^{\rm br}Z(r_{\rm cyc})
+w_n,\quad w_n=\int_{\rm bridge}T_n^Z(r_*,r)g_n(r)\,dr.
\]
所以原 cut 行回拉为
\[
\ell_n^{\rm cyc}=\ell_n^{\rm cut}T_n^{\rm br},\qquad
\ell_n^{\rm cyc}Z(r_{\rm cyc})=inN_n\eta_n-\ell_n^{\rm cut}w_n.
\]
这给作者 (21)–(22) 的准确源符号；把源项留在左边时为加号。长度有限不允许删除 $w_n$。

真传递保存 $J$，故非零 cut 中性线回拉仍是非零中性线；在 Hadamard 坐标中，如果 $z_-$ 投影为零，中性性迫 $z_+=0$，与非零矛盾。因此回拉后确能写成模一反射。该反射相位须由实际 bridge 传递得到，不能直接把未回拉的 cut 相位贴在周期端。

若辅助散射为 $\mathrm{out}=\mathcal S\mathrm{in}+\mathcal L f$，实际边界为
$\mathrm{out}=\operatorname{diag}(-1,\mathcal R_{\rm right})\mathrm{in}+g_{\rm bd}$，真正方程正是
\[
(\mathcal S-\mathcal R_{\rm bd})\mathrm{in}=g_{\rm bd}-\mathcal L f.
\]
两者分别酉不能证明其差可逆。以总传递 $T^Z$ 连接周期和桥，核心数据为 $(0,y_0)$，cut 为 $(t_{12},t_{22})y_0$，故
\[
\Delta_n=B_nt_{12,n}+iK_nt_{22,n}.
\]
作者没有从 $|D_n|\ge1$ 偷换成 $\Delta_n\ne0$。本审也没有对任何当前模宣告共振或非共振。当前无权传播块 $D_n$ 和原尾的线性乘子 $D_n$ 在不同文脉可能同字母，正式应用须按定义区分。

## 8. 与旧无限维接口的范围

旧 Schur 引理的 $K_0$ 有指定真实源、range、两个运输权；其有限矩阵和无限尾范数均有独立输入。新的辅助端口逆未解第 7 节反馈时，不能直接替换该 $K_0$。原有限 BVP Jacobian 也没有自动成为其正交归一后的真实有限 Schur 矩阵。

旧 weighted inverse §4 要求 cross-block 双向有界可逆。径向散射的 transmission 是 $1/D_n$；每个 $D_n\ne0$ 只支付逐模逆。要该乘子有全空间有界逆，需要相应统一 $\sup_n|D_n|<\infty$ 等真实表，而本稿没有这种结论。有限头部、主返回相位和高频余项仍须在实际端口及同一 norm 下核对。

本稿的逐模表是径向背景表。当前非零非径向 M14 线性化会耦合物理角模，不能据此前者宣称后者已具备完整加权 source 表。上述限制是现有问题的真实接口，并未新增 README 的门，也未否定已审中间结果。

## 9. 冻结有限 checker 的独立实际执行

已全文阅读 `78718-geometry-actual-port-transfer-check.py`，SHA256 `c2bd711cbb3c55c13995f5f10ce90324d8b46d3afb6ef2592f79e43318cbabc5`。它以转动基矩阵微分，保留移动法向项，用多项式余式分别按 $v^2+c^2=1$ 和 $\sigma^2=1$ 归约；分母的非零条件由正文 $a,v>0,|n|\ge2$ 保证。其七源列表是本次实际源的身份记录，不是未声明的七个历史 hardpin 检验，故正文源码逐项阅读仍是必要证据。

本审实际执行：

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
scripts/78718-geometry-actual-port-transfer-check.py
--out notes/2026-11-10-78718-audit-actual-port-transfer-check-01.json
```

cwd 为本题目录，真实回执 **43fde5，自然 exit 0**。12 个符号恒等和 7 份源身份均通过，0 PDE、0 tail、0 候选数组。独立报告为 [audit-actual-port-transfer-check-01.json](2026-11-10-78718-audit-actual-port-transfer-check-01.json)，2206 字节，SHA256 `640ac6cb111dbe65b4e0c3d84f89f5a76d89d06fbb00538b49ff3e60e2d0d3e9`。其与作者报告相同是实际重跑后的确定性结果，不是复制作者回执。

该有限检查不包含全部 support／bridge／反馈／无限维范围证明；这些由本审 §§2–8 的全文推导和实际源码核对支付。通过只可登记为实际端口接线中间模块。
