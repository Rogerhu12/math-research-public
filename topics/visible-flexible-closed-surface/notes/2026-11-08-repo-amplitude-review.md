# 2026-11-08 相邻课题振幅、形状商距离及数值起点审查

会话：Astra-visible-flex-effcccee / 子任务 repo_amplitude；GPT-6 Astra Pro，AI-assisted。
范围：只读核对 main 的四个 HANDOFF/open 和必要脚本，不修改相邻课题，不加载网格或系数大数组。以下两个几何引理有完整短证明，供 root 独审后决定是否进入 results；数值表只标为已报告的数值证据。

## 先给关键结论

当前最完整的全闭候选是 `large-amplitude-twist-flex` 的 wide-m2/q=.024。其相位公式在像集上只是让**整条带作同一刚体旋转**，帽保持固定。采用该刚体旋转对齐后，变化只剩上帽的小标记。由源公式精确推出：

$$\delta\le 2A=\sigma/20000\simeq 0.000047.$$

仅用帽边界圆就有 $D\ge 2r_e\simeq1.72$，所以无需依赖长经线或任何数值几何估计，已经得到

$$\frac\delta D\le 2.7325581396\times10^{-5}<0.05.$$

用已报告的帽面间距 $2H=8.393170164511453$，实际更强的比值上界约为 $5.5997911491\times10^{-6}$。后一个数字使用报告的浮点 $H$；前一个帽圆界可以直接做 Fraction 精确重算。

进一步，**保持现有局部标记形状并只提高标记高度，也不能同时达到本题两项门槛**：对该整个模板族有

$$\frac\delta D\frac{\min_t\operatorname{reach}(F_t(M))}{D}\le\frac1{3200},$$

而本题要求乘积至少 $0.05\cdot0.03=3/2000$，大了 $4.8$ 倍。因此应先改变宏观相位锚定机制或标记支撑几何，再投入降低长经线/尾曲率的昂贵续接；仅改当前带的数值精度、长经线或振幅不会解除第一个商距离上界。

这只排除明确的“单一整体旋转带 + 窄支撑固定帽标记”模板，绝不排除一般闭曲面柔性、宏观宽帽、多个相对运动带或其他真正形状机制。

## 1. 证据来源与版本

已通过 GitHub connector 读取 main；本地缓存只用于小脚本/标量报告交叉检查。

| 文件 | 读取时 Git blob SHA |
|---|---|
| 根 README.md | `f28db43754eef3b9f96d3981a6829f3574d461b9` |
| large-amplitude-twist-flex/HANDOFF.md | `60017c3d7264de831201f4c5b03b23df161bac65` |
| flexible-surface-model/HANDOFF.md | `04e3311f877f4f243293ac627592858eee42f8b2` |
| explicit-flexible-closed-surface/HANDOFF.md | `65c59ef0c6c3b7b88ff8f5758988a1e7aaa2bf0d` |
| quantitative-newton-twist-flex/HANDOFF.md | `0a108d910befa11834533b0a9bd0455214ee725e` |
| large-amplitude scripts/f6root_closed_wide_m2_model.py | `d6af93b9b226bfe268286383ec2c6bef949369f4` |
| large-amplitude scripts/f6root_inward_caps.py | `64fc6398c3512a0b95df53232c496d907628ada4` |
| large-amplitude scripts/f6root_reproduce_wide_m2.py | `27d45482d9ef441b45464aa0678467687d1d1000` |
| large-amplitude notes/f6root_closed_wide_m2_m12_cusp_p128_model.json | `4711c8fb206244b98cf83094eaf5a0a20b2ddfb8` |
| flexible-surface-model/open.md | `bca71cd0456c88e44ec781d5be719aa5be28c5ea` |
| explicit-flexible-closed-surface/open.md | `dc6381ed03b14575472773d43d96151cb1f31374` |
| quantitative-newton-twist-flex/open.md | `58e36ecedeb318913b80c49ade8dabf104b095d3` |

来源入口：[large HANDOFF](../../large-amplitude-twist-flex/HANDOFF.md)、[flex-model HANDOFF](../../flexible-surface-model/HANDOFF.md)、[explicit HANDOFF](../../explicit-flexible-closed-surface/HANDOFF.md)、[quantitative HANDOFF](../../quantitative-newton-twist-flex/HANDOFF.md)。大振幅最新 HANDOFF 本次读取的更新时间为 2026-11-08 23:06 +08。

## 2. 全相位像集上界：完整证明

记 $R_\alpha$ 为绕 $z$ 轴旋转。令 $B$ 为整个 band 的像，包括中央、两个 prefix、两个 tail 及平面环领；帽像为 $C_+\cup C_-$。当前定义在所有角材料坐标上为

$$F_\alpha(s,\theta)=R_{-\alpha}F_0(s,\theta+\alpha).$$

因为 $\theta$ 遍历整个圆，预合成角平移不改变像集，故 $B_\alpha=R_{-\alpha}B$。平面环领本身轴对称，是否计入 $B$ 均不影响该等式。帽固定，因而

$$R_\alpha F_\alpha(M)=B\cup R_\alpha C_+\cup C_-.$$

下帽是圆盘 $z=-H$，旋转不变。上帽为同一圆盘上的图

$$C_+=\{(x,H+h(x)):|x|\le r_e\},\qquad 0\le h(x)\le B_*.$$

旋转帽在相同水平点 $x$ 的高度为 $H+h(R_{-\alpha}x)$。两图在同一水平点成对的距离至多 $B_*$，两个方向均成立；于是

$$d_H(R_\alpha C_+,C_+)\le B_*.$$

加入共同的 $B\cup C_-$ 不增加此上界。因此对任意 $\alpha$，

$$\inf_{A\in E(3)}d_H(AF_\alpha(M),F_0(M))
\le d_H(R_\alpha F_\alpha(M),F_0(M))\le B_*.$$

最大化相位得到 $\delta\le B_*$。反射已被允许在 $E(3)$ 中，只会使下确界更小；证明不依赖某个最佳刚体的唯一性。它也不需要精确等距或 PDE 收敛，故适用于当前有限近似以及保留同一相位/帽公式的任意改良带。

### 应用于实际 cap 公式

`MarkedFlatCap` 给出四个互不重叠支撑，中心位于 $r_e/3$ 处，支撑半径

$$b=\min(r_e/10,\sigma/20),\qquad A=\frac{b^2}{100\sigma},$$

四振幅为 $(A,A,A,2A)$；每个 bump 为

$$a_j\phi_{\beta_j}(|x-x_j|/b),\qquad
\phi_\beta(t)=(1-t^2)^4(1+t^{2+\beta}),\quad0\le t<1,$$

支撑外为零，$0<\beta<1$。令 $u=t^2$；有 $t^{2+\beta}\le t^2$，并且

$$0\le\phi_\beta(t)\le(1-u)^4(1+u)\le1,$$

最后一个函数的导数为 $-(1-u)^3(3+5u)\le0$，其在 $u=0$ 等于1。支撑不重叠，所以 $0\le h\le2A$，在最大 bump 中心达到 $2A$。

当前 $r_e=.86,\sigma=.94$（R35约定为精确 binary64 输入），有 $b=\sigma/20$，$2A=\sigma/20000$。初始像包含半径 $r_e$ 的完整帽边界圆，所以 $D\ge2r_e$，给出前述严格商距离上界。没有用中央 PV 作为 Hausdorff 距离；PV 只是单个形状中一条材料圈的高低差。

## 3. 窄帽标记族的形变量–reach 乘积障碍

此节允许任意修改四个非负振幅，令最大振幅为 $B_*>0$；保持上述 bump 形状、共同支撑半径 $b\le r_e/10$、轴对称圆盘边界和整条带同旋转的相位公式。上节仍给 $\delta\le B_*$。

在最大 bump 中心 $x_*$，其余支撑不相交，且

$$\phi_\beta(t)=1-4t^2+o(t^2),\qquad
\nabla h(x_*)=0,\quad D^2h(x_*)=-\frac{8B_*}{b^2}I.$$

图面在该点的第一基本形式为 $I$，所以两个主曲率绝对值都是 $8B_*/b^2$。对任意 C² 嵌入曲面，reach 不超过每个非零主曲率的倒数。简要证明：若 reach 为 $\rho>0$，法向滚动球性质给 $|n\cdot(q-p)|\le |q-p|^2/(2\rho)$；沿主方向取 $q-p=sv+\kappa s^2n/2+o(s^2)$，得 $|\kappa|\le1/\rho$。令 $\rho$ 趋向 reach 即得结论。

因此每一相位都满足

$$\operatorname{reach}(F_\alpha(M))\le\frac{b^2}{8B_*}.$$

将它与 $\delta\le B_*$、$D\ge2r_e$ 和 $b\le r_e/10$ 相乘：

$$\frac\delta D\frac{\min_\alpha\operatorname{reach}(F_\alpha(M))}{D}
\le\frac{b^2}{8D^2}\le\frac1{3200}.$$

本题需该乘积至少 $3/2000$，矛盾。等价地，如果坚持 reach$\ge.03D$，该模板的商形变量最多 $D/96\simeq1.0417\%D$。这个障碍与带上的 Fourier 阶数、tail 层数、非线性求解器容差、经线长度、上/下坡 profile 无关。

要绕开它，必须改变假设，例如用支撑宏观宽度 $b/D\ge\sqrt{8(.05)(.03)}\simeq.109545$ 的锚定几何（这只是必要条件，不是充分构造），或者采用多个不能被单一旋转同时对齐的活动分量。不能把“微小曲率标记证明非全等”视为“形状商距离有百分之五下界”。

## 4. 当前数值起点比较

| 课题 | 当前最强正向对象 | 固定几何收敛情况 | 本题缺口 |
|---|---|---|---|
| large-amplitude-twist-flex | wide-m2、q=.024、全闭 C² 近似，M12有全相位嵌入证书，M16更细 | prefix+bridge M6→12→16 的 fullD $3.69477e-4\to1.635713e-7\to8.245504e-9$，metric $9.40018e-7\to3.807608e-10\to1.051983e-11$；最新 integrated 重建进一步降低实际导数残差 | 全闭统一 solver 精度及最终独立重跑未完；更根本地受到第2–3节的当前相位/帽模板上界 |
| flexible-surface-model | λ4/q005，$q=5.859892914070882e-5$，实际首段和真尾/圆领圈逐项认证 | K8/r64→K10/r128→K10/r256：D $4.080348e-10\to6.220033e-13\to3.204447e-15$，F $5.304127e-10\to8.100620e-13\to5.042391e-15$；MP100和独立全头扫描吻合 | 强收敛但实际 PV仅.000127251/宽.954355，最终整个闭族、宏观 δ/reach 无证书；固定K10弃频约7.27e-16 |
| explicit-flexible-closed-surface | R7精确嵌入环带、R30十二片嵌入环带、R31–35有限求积/ODE的真实两柱口及四口片 | 等距恒等式与接口已有数学审查，不是最终全闭离散收敛任务 | 至今有未配边界；R7的去刚体变化>2.2608%D仅属环带，reach未证；其课题阈值原为1%/.1%也尚未完成 |
| quantitative-newton-twist-flex | R29–31合法固定metric seed/profile和全频真尾工具 | 固定E Newton仍卡非零 raw；不是已得零残差大幅带 | 全Fourier过渡、真实闭合、δ下界与reach均未付，不能作为比wide-m2更接近完成的数值例 |

所有源 HANDOFF 都明确本课题未完成。flex-model 的工程实体、FEM和视觉文件不是可用于本题的等距正例：原工程运动极小，非等距放大模型不能计入。

### wide-m2 最新细化的实际意义

共同几何参数为 base2、q=.024、δprofile=.8、vu=.85、vd=.98、ramp=.05、cycles5；true tail cut=.98/w=.05、cuff=.90、κ95、cap.5、protect80、δ0=.006、etaRatio=.05，浅 cells0–7 R2，8–15接回R64，之后固定R64无限背景。接缝物理宽度恰为1/25和1/40；帽边界 .86。BVP同时解出 core halfwidth，M6→12→16 为 .3065354699951123→.3065354708091724→.30653547080931504。

最新 HANDOFF 报告 M16 过紧容差时旧 raw Hermite 重建出现 binary 节点误差除以小步长平方的恶化。`f6root_integrated_prefix_map.py` 改为实际函数

$$C(s)=C(0)+\int_0^s P_M V(u,C_{source}(u))\,du.$$

二阶导数使用真实 frozen source 导数，不用 formal ODE jet 偷换；因此它是另一个实际 C² 近似模型。q8→12求积位置系数差≤4.208e-16；prefix D的角 l1约6.74191e-10、metric1.02348e-12；core seam D的角l1约1.25262e-9、metric约2.08694e-12；tail seam角l1约8.44709e-10、metric4.15151e-12。旧R35不能直接继承到这张新映射。

tail M12 p32→64→128 的实际D $1.74795e-8\to1.06420e-8\to2.069824e-9$。M16 p256/s512→s1024 D $2.606185e-10\to8.113779e-11$、metric4.416782e-17；这里 s1024 是**同一非线性节点状态**的 flow 评价细化，不能说又得到一档非线性收敛。cell6 taper成本约2.90e-13、角cut64的Vrr弃项约8.42e-14是当前固定实现中的非零底，若未来容差要求更低必须显式处理，不能以它们很小代替固定几何加密门。M20/tol1e-10 尚在共享大作业，不应重复启动。

更大 q 的探索仅有 prefix：q=.04/M20 PV.08166289、D3.6526e-7；q=.06/M24 PV.122830708、D4.7081e-5；q=.0625/M24 PV.12800239、D1.10e-4；都没有对应完整真尾/帽几何完成证书。vu=.94/c7/q=.030 的新分支为 PV.06006724、D1.34619e-5/metric9.168e-9。不能将这些局部数字拼成一个已完成的闭族。

### reach 的额外数值警报

M12实际tail小报告 `f6tail_wide_m2_r2_cartesian_cusp_repaired_m12_n6_p128_s256_audit.json` 的 `totals.curvatureSampled` 为94.69335042775782。若单点局部曲率通过区间重验，则 reach≤.0105604；结合报告的 $D\ge2H$，reach/D≤.00125822，距离 .03约23.84倍。该报告未保存最坏曲率点坐标，因此这里保留“数值警报”级别，不能把R35的上界κ≤95.102735反过来当κ≥95的证明。新的主曲率单点区间见证无需重新载入整个mesh，可由tail source定位最坏样点后单点复算。

## 5. 最实用的代码入口和小实验

1. 完整映射：`large-amplitude-twist-flex/scripts/f6root_closed_wide_m2_model.py`。唯一已经有全闭几何证书的主基准是 M12/q024 + cusp_p128；M16/integrated是新近似，要更新证书。
2. 可移植重跑器：`scripts/f6root_reproduce_wide_m2.py --checkpoint .../notes/f6root_wide_m2_r2_true_m12_q024.json.gz --out <本题输出路径> --print-command`。去掉 `--print-command` 才真正求解。它保持存储的全部几何/solver参数，只重建本地路径，不覆盖原检查点；有numpy/scipy/mpmath依赖，true-joint另需Node。大求解不属于本子任务本次小实验。
3. BVP入口：`scripts/f6curve_outward_bridge_bvp.py`；参数含 `--linear-port --tail-config --modes --amplitude --delta --v-up --v-down --ramp --cycles --base-mode --tol --bc-tol`。新的低成本几何screen可先用 `f6root_gentle_inner_cycle_scan.screen`；现成`f6root_wide_m2_cycle_scan.py`本身会跑4×4×3×2×4=384个线性配置，且只是线性筛选，不必原样全跑。
4. 最新实际积分重建：`scripts/f6root_integrated_prefix_map.py` 的 `IntegratedPrefix`，保留实际C/C′/C″而非formal jet；此脚本本次只查缓存小源码，收敛数字来自已读取main HANDOFF。
5. 本题无依赖小复算：[repo_review_phase_shape_bound.py](repo_review_phase_shape_bound.py)。运行 `python topics/visible-flexible-closed-surface/notes/repo_review_phase_shape_bound.py`；不导入任何大数组。输出精确帽高度、所有相位的δ上界、单帽圆D下界、乘积障碍以及明确标为报告值的H/曲率数值背景。

本机可用缓存源目录：`/workspace/scratch/f6f33987b45e/math-research/topics/large-amplitude-twist-flex/`；flex-model缓存在`/workspace/scratch/6ed6931381f6/math-research/topics/flexible-surface-model/`。使用缓存求解前必须按Git blob核对需要的主脚本与小manifest；这些路径不是跨机器交付路径。

## 6. 对主线的建议

在当前证明下，单纯缩短19.4257的经线并把95量级曲率降至较小值，仍保留δ≤4.7e-5，所以不能是本题完成路线。它们可以为后续的新宏观机制准备条件，但应先确定能留下宏观相对运动的帽/多带布局。若采用宽帽锚，先做带相位与帽旋转的连续E(3)商距离下界；若用多个活动带，需不同相位不能被同一刚体同时消去，并重新检查所有间隔/接缝的reach。

本审查没有找到满足本题门槛的现成闭族。两个模板障碍仅用于省去明确无效的数值延拓，不是本题收尾答案。
