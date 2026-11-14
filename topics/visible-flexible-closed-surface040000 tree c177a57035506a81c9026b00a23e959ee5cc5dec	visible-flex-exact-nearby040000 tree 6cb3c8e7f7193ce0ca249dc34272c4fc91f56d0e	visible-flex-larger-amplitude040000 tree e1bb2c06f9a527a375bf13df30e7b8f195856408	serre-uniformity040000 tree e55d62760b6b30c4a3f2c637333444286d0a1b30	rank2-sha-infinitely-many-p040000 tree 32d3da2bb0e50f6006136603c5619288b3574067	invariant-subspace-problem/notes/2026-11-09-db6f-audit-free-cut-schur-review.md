# 自由切口 Schur 方法的独立全文审查

审查者：`/root/independent_geometry`，2026-11-09。**PASS，限于明确条件下的完整线性化消元定理及冻结源码的规范化／接口解释。** 本人未参与该推导或相关数值优化。本次只读方法与源码，没有实现新 worker、线性求解器，没有执行 moment root、flow、联合求解或玩具数值算例，也没有使用正在恢复的作业输出作证明前提。

## 1. 审查对象及唯一修订

最终被审稿为 `tail-free-cut-schur-method-v2.md`，SHA256 `479252a0fbaa8ba4d7299acee038a4b49f22a40e8f3c6cc4b4cff50eb6f16802`；对应 `tail-free-cut-schur-sources-v2.json`，SHA `06c4f4283fa55b13e58950d4d97b6e8c7e28d29fffbfff7c64febcf4e401c528`。本节短名均在 `notes/2026-11-09-db6f-` 下。

已阅读全文，并核对原 core 的 `cellFlow/evaluate/correction/cutJets/tangentGraphAtCut/heightJetJacobian`、原完整 moment root 和 RHS、split factory、prefix 的 `TailMixin`、实际自适应角图、物理弧长及数值 chart、固定 gauge 与入口参数的实现。七个原绑定文件全部 hash／字节数相符；另核七个必要接口来源，合计十四项，详见 `audit-free-cut-schur-review.json`（SHA `3593045114ac4bf1464d314cf6a24731b249b497885213cf8300bfbcdfd22303`）。这些是静态来源核查，不是数值导数精度认证。

原稿 SHA `12b9deadc7f5271acccf19dcf770ab0600f28e34ff5cc03a9cc03cf1198bde9c` 保留。审查指出其“仅当残差均零才保证所有 b 零”一句容易读成必要条件。作者另存 v2，明确改为：**残差均零蕴含所有 b 零；反向一般不成立，非零 forcing 可能相消。** 已用逐字反向替换核实 v2 除这一句外与原稿完全相同，全部十九个编号公式未变。

这个消歧有实际逻辑内容。例如取 $M=d=1$、$G_{\rm deep}=e=0$、

$$
J_0=\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad R_0=(1,2).
$$

则 $X_0=1,Y_0=2,t_0=1,u_0=2$，所以 $\Gamma_0=2,b_0=0$，尽管 $R_0\ne0$。这里仅作手算反例，没有执行新 solver。修订并不改变方法，因为该方法本来就保留全部实际 forcing，而不由 b 的值推断原残差为零。

## 2. 尾内部残差与非齐次递推

原 `evaluate` 保存的确是 out 减当前外节点。`cellFlow` 以 `states[n+1]` 为输入，momentum 输出行和 tangent 的对应行已各除一次 `c.portRatio`。因此文中 $\Phi_n,J_n$ 的节点坐标一致，不应再次缩放 J 的 momentum 行。

独立从 Newton 方程得到

$$
J_n\delta y_{n+1}-\delta y_n=-R_n
\iff
\delta y_n=J_n\delta y_{n+1}+R_n.
$$

深端残差 $e=\Pi_d-G_{\rm deep}Q_d$ 的线性化给

$$
\delta\Pi_d=G_{\rm deep}\delta Q_d-e,
$$

所以 $b_d=-e$ 的符号正确。$G_{\rm deep}$ 在本线性化内固定；若另行变化物理背景、深端图或离散参数，这个方程需要相应参数导数，不属于本文范围。

把下一层关系代入 J 的上下块，正好得到 $X=A+B\Gamma$、$Y=C+D\Gamma$、$t=Bb+R^Q$、$u=Db+R^\Pi$。可逆 X 先解出下一层 $\delta Q$，再得

$$
\Gamma=YX^{-1},\qquad b=u-\Gamma t.
$$

矩阵乘法顺序没有倒置；尤其 $YX^{-1}$ 不是 $X^{-1}Y$。原代码 `gs/bs/cache.Gi/cache.t` 逐项吻合。回代同时重建每个节点的两个块，既不是只传播 homogeneous tangent，也没有遗失深端 forcing。

“完整内部线性化等价于切口仿射图及回代”在所有 X 可逆时是双向命题：原系统解代入即给该图；从该图按回代构造的解逐层满足全部原行及深端行。X 奇异只破坏这种图坐标，不足以判断完整系统奇异，更不能推出非线性无解。

## 3. node0 与物理高度／斜率规范化

原 subdivision 仅在物理 cell 的外 port 设置 `portRatio=2**a`，纯数值内部子段为 1。core 的 node0 使用 $\mu_{-1}=\rho\mu_0$；其 cut 分支显式把 momentum 乘回 $\rho=2^a$。因此局部 engine 输入确为

$$
\widehat y_0=\operatorname{diag}(I,\rho I)y_0.
$$

这与已规范化 stage J 是两件不同的接口操作。局部斜率对 node momentum 的链式导数必须乘 $\rho$，stage 矩阵则不能重复乘除。

非均值高度用普通余弦系数表示为 $H_t=c^4Q_0$。原 RHS 的 shape 行为

$$
f_{Q,j}=\frac{r_x}{c}
\left[(m_j^2-4)Q_j+\frac{\sqrt2 w_c L_j}{c^3}\right].
$$

对 $r^4Q_j$ 求径向导数，得到 $m_j^2c^3Q_j+\sqrt2 w_cL_j$，恰为原 `cutJets.slope`。系数中的 $\sqrt2$ 来自 L 的正交余弦基转为普通余弦系数；它不是 node momentum 的另一缩放。对该式求导，文中 $S_Q,S_\Pi$ 两块和式 (12) 都正确。式 (12) 使用同一局部 profile 的 $r_x$ 和同一 engine 的 RHS；不能把一个 stage 的 $r_x$ 与另一个参数化的 RHS 混用。

moment 的 mean target 为零，其他 target 系数为同一个 $\kappa\widehat\Pi$。隐函数求导中 Q 列的右侧为 $-\mathcal M_Q$，momentum 列为 $+\kappa(0,I)^T$，两种符号正确。求解应保留完整 $(M+1)$ 维 root Jacobian；删掉均值会改变非均值偏导。这里只要求该局部 root 及 Jacobian 可用，不需要全尾已经满足 shooting 方程。

实际 `cutJets` 还会调用物理二 jet evaluator，其内部可能再次求同一节点的 root。文稿的“一个节点的局部 root”是单节点数学问题，不能解读成该现有 API 只发生一次函数调用。本文没有以调用次数获取新的数值证据。

## 4. prefix 的物理角、方向与 gauge

自适应角图在 cut 处消失到二阶，因此 cut 的 $\psi=\theta$，这些非均值 Fourier 系数可以直接匹配。当前固定 g 模式中 `self.q` 是固定 gauge $q_g$；真实 support amplitude 为 `seed_support_amplitude*exp(p[0])`，经 inlet 与 $F_p$ 进入问题，不能把两个 q 混为同一变量。

原 `TailMixin.terminal` 明确请求 $H=\sigma q_gZ_b$，而返回的残差是

$$
(q_g f_z-S_t/\sqrt{E_c})/\mathrm{bcweights}.
$$

此处 $f_z$ 是 **`flow.fun` 的物理弧长 RHS**，不是已乘上数值 chart 的 $ds/dt$ 的 `SupportBVP.fun`。bridge 给 $dr/ds=\sigma/\sqrt{E_c}$，故

$$
\frac{d(\sigma q_g Z)}{dr}
=\frac{\sigma q_g f_z}{\sigma/\sqrt{E_c}}
=\sqrt{E_c}q_g f_z.
$$

这独立验证了 $H_p=\sigma q_g Z_b$ 与 $S_p=\sqrt{E_c}q_gf_z$，斜率不得再乘一次 $\sigma$。原 terminal 与 $S_p-S_t$ 只差固定可逆的正行缩放。这里正 bcweights、$E_c>0$、固定切口／gauge／方向均是明确前提；若另让这些参数变化，就不能仍只用稿中偏导。

## 5. prefix forcing 与最后切口系统

以当前固定 collocation 网格说明维数：状态维数 $n=3M+1$，若有 N 个节点及 M 个自由入口参数，则未知数 $k=nN+M$。移除 M 个 terminal 行后，collocation 加 inlet 共 $nN=k-M$ 行；再加入 M 个高度行正好组成方阵 $J_p$。这里不把自适应网格的位置作为本轮 Newton 的附加未知数。

由 prefix／高度两组原线性行直接得到

$$
J_p\delta z=-\binom{F_p}{r_h}+\binom0{c^4I}\delta Q_0.
$$

所以 $a_p$ 的负号与 $B_p$ 的正号正确。$a_p$ 必须保留当前 collocation、入口和高度缺陷；一个保存 CP 或 warm 不是这些缺陷已严格为零的理由。

再将 $\delta z=a_p+B_p\delta Q_0$ 代入斜率行，可独立写为

$$
\left(S_{p,z}B_p-S_Q-S_\Pi\Gamma_0\right)\delta Q_0
=-r_s-S_{p,z}a_p+S_\Pi b_0.
$$

取 $D_{\rm out}=-S_\Pi$，这与稿中

$$
(C_{\rm out}+D_{\rm out}\Gamma_0)\delta Q_0
=-r_{\rm out}-D_{\rm out}b_0
$$

完全相同。因此最终 forcing 的符号没有错误。特别是不能用 $-r_s$ 替代 $-r_{\rm out}$，也不能删去 $-D_{\rm out}b_0$。

整体未知数为 $k+2M(d+1)$，方程数为

$$
(k-M)+M+M+2Md+M=k+2M(d+1).
$$

可逆 $J_p$ 与各 X 分别给双向消元；仅剩 M 个 $\delta Q_0$ 和 M 个斜率行。最后矩阵可逆给唯一解，逐层回代恢复全部原行。反向代入则任一原解都映到同一个最终解。在这些 chart 条件内，完整 Jacobian 的核与最后矩阵的核一一对应，故非奇异性等价。任一 chart 未证可逆时，不能据此宣称完整系统失败。

## 6. 现有 API 与尚未支付的条件

`evaluate(states,target,true,scales)` 不把 state 强制改成 target；target 只进入原切口残差／尺度，因此能够描述可评价的未收敛状态。可是 `correction` 的 gs/bs/cache 目前是内部变量，其公开返回不提供完整非齐次图；未来如需导出，仍要单独审实现。

`tangentGraphAtCut` 只传播 $\Gamma$，没有 b。`heightJetJacobian` 沿 $(\delta Q,\Gamma\delta Q)$ 作中心差分并除以 $c^4$；其前 M 行对应近似的

$$
c^{-4}(S_Q+S_\Pi\Gamma_0),
$$

而不是两个独立偏导块，也没有当前内部缺陷产生的常数项。在真正已解尾的可逆 chart 中，这才具有相应 DN 导数解释；在未收敛点不能用“DN 已解”的名称代替条件。

同样，`TailMixin.bc_jac` 内部仍调用 `tail.solve`，不能用它取得完整 prefix 消元块而声称已经绕开 DN。固定 g 下的原局部 `fun_jac`、入口参数导数以及端点显式表达式是装配来源，完整 collocation 装配和分解尚未实现。

局部可评价性应同时覆盖所有原 RK 子点评价和独立 cut node0 的 root；stage 输出与 node0 尚未拼合时，不能仅凭某次 stage flow 成功自动保证独立 node0 合法。文中“合法基点／局部 root 可评价”的前提包含这一要求。只读消元定理本身没有支付该前提，也没有支付任何 X、$J_p$ 或最终矩阵的数值可逆性及条件数。

全部行尺度在本次未归一原残差线性化中冻结，与源码把 scales 用作 residual norm 的用途相符。若改为对随未知高度变化的归一 residual 本身求导，额外尺度导数不能省略；那不是当前定理声明的对象。

## 7. 结论的准确范围

本方法在可评价基点及所列可逆性条件下是正确的联合线性化消元，不要求当前 stage、Robin 或 prefix 缺陷先为零。它解释了为什么在数值布局中可以消去内部变量，同时仍让切口高度由原联合匹配决定。

这不把未收敛的局部 Jacobian 或仿射图变成已解 DN，不改变一个本来要求固定 H 的实验的标签。自由 cut 联合 warm 与固定目标对照必须分别记录。若用旧低模／块对角近似替代某个矩阵，代数仍是该提供矩阵的消元，但“真实联合 Newton”准确性需另验。

现有根迭代、有限角求积、RK、rounded 三角表与数值 Jacobian 之间的误差不由本稿认证；理想实算术模型中的恒等式不意味着 literal floating 程序逐位等价。本文所谓完整方程是已明确定义的有限 shape 联合系统；全均值二 jet、全 XYZ seam、连续 metric／曲率及 G5 仍是另外的验收项目。

v2 已消除唯一指出的必要性措辞问题，其余公式、量词与源码接口解释未发现数学错误。审查完成不授权执行新求解或替换活动 engine。
