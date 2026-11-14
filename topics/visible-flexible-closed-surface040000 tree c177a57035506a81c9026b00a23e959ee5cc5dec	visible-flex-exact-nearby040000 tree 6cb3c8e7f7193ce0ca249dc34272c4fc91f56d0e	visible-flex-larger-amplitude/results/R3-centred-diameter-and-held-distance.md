# R3：中心对称直径与握持距离的条件证书

状态：已证明（条件几何引理），2026-11-09。未参与推导者 independent_audit 全文审查 §§1–3 PASS，见 notes/2026-11-09-audit-centred-diameter.md。原候选SHA256 aab6e1db9e5b905d3fb85c0c9ad18f9b1bdd9694486e854bb1d712d64b70c7fe。仅采用以下证明，不将原§4采样预算当作结果；接口半径修正见notes/2026-11-09-centred-diameter-correction.md。

## 1. 中心对称紧集的精确直径

**引理。** 设非空紧集 $S\subset\mathbb R^3$ 满足 $S=-S$，则
$$\operatorname{diam}S=2\max_{x\in S}|x|.$$

证明：三角不等式给 $|x-y|\le |x|+|y|\le2\max_S|x|$。紧性给最大范数点 $x_*$，对称性给 $-x_*\in S$，二者距离等于该上界。

若另一个紧集 $\widetilde S$ 与 $S$ 的 Hausdorff 距离不超过 $\varepsilon$，则
$$|\operatorname{diam}\widetilde S-\operatorname{diam}S|\le2\varepsilon.$$
对每对点分别选择距离不超过 $\varepsilon$ 的对应点，再用三角不等式；反向交换两集。

没有中心对称也总有 $\operatorname{diam}\widetilde S\le2\max_{\widetilde S}|x|$。因此独立分段控制同一个球的包络即可，不必把所有径向最大值与最高点放在同一个不存在的圆柱角点上。

## 2. 反射前缀的应用

设上前缀 $X(s,\theta)$ 满足 $X_z\ge0$ 及
$$X(s,\theta+\pi)=(-X_x(s,\theta),-X_y(s,\theta),X_z(s,\theta)).$$
给定 $\ell>0$，把上前缀沿 $z$ 轴平移 $\ell$，把下前缀取为其关于 $z=0$ 的反射。中央接 $\gamma(\theta)+u e_z$，$|u|\le\ell$，其中 $\gamma(\theta+\pi)=-\gamma(\theta)$。若两尾和未标记两帽也按这一上下反射、半转对称配对，则整个未标记紧像集 $S^0$ 中心对称。

其直径因此由实际球半径决定。对前缀，准确的候选表达式为
$$D^0_{\rm prefix}=2\max_{s,\theta}\sqrt{X_x^2+X_y^2+(X_z+\ell)^2}.$$
该式用于带边前缀及其中央柱时，也须把中央柱的球半径纳入最大值；不能把它漏掉。若前缀的 $s=0$ 恰为完整中央截面，则中央柱的最大范数在 $u=\pm\ell$，已经由前缀端圈覆盖。

若后续尾和帽位于 $\rho\le r_c,\ |z|\le H_c$，它们的球半径不超过 $\sqrt{r_c^2+H_c^2}$，从而整个未标记像集满足
$$D^0\le\max\{D^0_{\rm prefix},\ 2\sqrt{r_c^2+H_c^2}\}.$$
若固定非对称标记只改变帽，并保持整个像落于上述同一球，则同一上界仍成立。若只有相对未标记帽的 Hausdorff 改变量 $\varepsilon$，使用 $D\le D^0+2\varepsilon$。

这些都是几何包含结论；并未假设或推出所有拼缝已存在。

## 3. 握持下的全像距离下界

假设初始完整像包含中央柱
$$C=\{\gamma(\theta)+u e_z:|u|\le\ell\},$$
其中 $(R,0,0)$ 在截面上，整个截面位于 $|y|\le r$，且 $R>r$。假设其余初始像的所有点均满足 $|z|\ge\ell$。若某个允许相位把中央柱的像绕 $z$ 轴转过 $\pi/2$，其像中包含 $p=(0,R,0)$。

对原中央柱中的任一点 $q$，有 $|p-q|\ge|R-q_y|\ge R-r$；对原像中中央柱以外的点，有 $|p-q|\ge|q_z|\ge\ell$。所以
$$d_H(F_t(M),F_0(M))\ge\operatorname{dist}(p,F_0(M))\ge\min\{R-r,\ell\}.$$
此处无需为其他相位作刚体对齐；正是新版 $\delta_{\rm hold}$ 的定义。没有推出 $\delta_E$ 下界。

若两固定帽内分别存在闭片 $H_+,H_-$，各有非空相对内部，且存在 $p_\pm\in H_\pm$ 使 $|F_0(p_+)-F_0(p_-)|\ge.2D$，则 $H=H_+\cup H_-$ 自动满足握持区尺寸要求。无需每个片单独达到 $.2D$。

