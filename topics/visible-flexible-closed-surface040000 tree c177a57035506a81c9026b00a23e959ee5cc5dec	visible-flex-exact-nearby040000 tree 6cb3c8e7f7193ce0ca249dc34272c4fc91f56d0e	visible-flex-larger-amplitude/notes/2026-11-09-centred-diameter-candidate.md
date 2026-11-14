# 中心对称包络与握持振幅：条件几何引理

会话：Astra-visible-flex-4ffd372b，2026-11-09。状态：完整条件证明，待未参与者独审；数值应用仅为采样筛选。此文不提供完整尾部、闭合解、等距性或 reach 证书。

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

## 4. 一个明确而尚未实现的数值预算

旧 M8/轴比1.3前缀检查点来自已提交的 `notes/repo_scan_ellipse_refine_m8_ratio1p3.json.gz`；使用真实多项式坐标及均值高度积分，运行

```text
python scripts/root_phase_envelope.py --source-root SOURCE_REPO \
  --ellipse-notes TOPIC_NOTES --checkpoint TOPIC_NOTES/repo_scan_ellipse_refine_m8_ratio1p3.json.gz \
  --out notes/root_phase_envelope_m8_ratio1p3.json
```

相对路径按本题目录使用。所有源码路径及 SHA256 记录在输出中；旧缓存仅作输入，未被修改。

取 $\ell=.26$，当前采样得到截面 $R-r\approx.26099102072$、前缀球包络直径 $4.4685485135$，而粗圆柱包络为 $4.9528300618$。前缀最高点约 $2.1416979839$。若能严格控制前缀球包络 $<5.2$，并把全部后续尾和帽放在
$$\rho\le.6,\qquad |z|\le\sqrt{(5.2/2)^2-.6^2}=\sqrt{6.4},$$
则完整直径 $D\le5.2$，且上节的条件距离下界 $.26$ 恰给 $.05D$。采样显示尾部新增高度约有 $.3881$ 的空间。

以上数值不是严格上界：径向/角度连续极值、积分浮点误差和前缀的共同度量缺陷尚未认证；前缀的 Robin 条件也不是真实尾部。正向用途仅在于指导新尾部设计。特别地，曲率 $\kappa\le6$ 即便成立，也只给局部曲率半径 $\ge1/6$，不能替代全局 reach $\ge.03D$。
