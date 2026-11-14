# R24：当前固定帽标记的刚体取商变化量上界

**状态：已证明，完整证明与应用经独立全文审查 PASS。** 作者：Astra-visible-flex-db6f0b0e；独审：/root/coupled_prefix；2026-11-09。

当前 R21 闭族严格满足 0<δ_E≤1/2000，且 0<δ_E/D<1/7080。该上界只约束指定小凸起标记和指定相位机制的更强 quotient 目标；原握持指标、同 g 数值加密主线及 G5 要求保持。下列 §§1–4 逐字收入已审完整草稿。

## 1. 抽象集合命题

令 $R_\alpha$ 为绕 z 轴的旋转，$A\subset\mathbb R^3$ 为固定紧集。令下帽 $C_-$ 为旋转不变的紧集，上帽为固定连续图（b 连续）

$$
C_b=\{(w,H+b(w)):w\in\overline{B_r(0)}\},
\qquad 0\le b(w)\le h_*.
$$

假定相位族的像集恰为

$$
\Sigma_\alpha=R_\alpha A\cup C_-\cup C_b.
\tag{1}
$$

则对每个相位都有

$$
\inf_{T\in E(3)}d_H(T\Sigma_\alpha,\Sigma_0)\le h_*.
\tag{2}
$$

这里不要求给定 $T$ 为最佳对齐，也不要求三重对称、凸性或嵌入性；这些条件属于具体应用的其他结论。

### 完整证明

在刚体群中选择一个明确元素 $T=R_{-\alpha}$。由旋转不变性，

$$
T\Sigma_\alpha=A\cup C_-\cup R_{-\alpha}C_b,
\qquad
\Sigma_0=A\cup C_-\cup C_b.
$$

圆盘在平面旋转下不变，因此

$$
R_{-\alpha}C_b
=\{(w,H+b(R_\alpha w)):|w|\le r\}.
$$

对其任意一点，取 $C_b$ 中相同水平坐标 $w$ 的点作为匹配。二者的距离为

$$
|b(R_\alpha w)-b(w)|\le h_*.
$$

反向仍选相同水平坐标，得到另一方向的相同距离界。所以 $d_H(R_{-\alpha}C_b,C_b)\le h_*$。此外对于任意共同集合 $K$，直接按 Hausdorff 距离的两个有向定义有

$$
d_H(K\cup C,K\cup C')\le d_H(C,C').
$$

共同部分上的点距离为零，其他点可使用帽集合的匹配。取 $K=A\cup C_-$ 即得 $d_H(T\Sigma_\alpha,\Sigma_0)\le h_*$，再对所有刚体取下确界得 (2)。若该下确界用最小值表示，上界当然仍成立。逐相位取最大值，亦得 $\delta_E\le h_*$。证毕。

更一般地，只需 $b$ 的值域包含于长度 $h_*$ 的区间；常数高度偏移本身不会增加这个上界。这里使用单边非负凸起，所以界为 $h_*$，无需多乘 2。

## 2. 对 R21 已审 M12 闭族的应用

R21（results/R21-m12-whole-map-and-actual-metric-decrease.md）§§2–4 与 R17 的相位构造给出：除两个帽以外的未标记完整活动像按 $R_\alpha$ 旋转，包含全部镜像前缀、尾与圆领；两个帽固定。活动参数中的角平移是对每圈的双射，故不会改变这个像集陈述。取 $A$ 为去掉帽内部后的闭活动部分，圆周接缝可以同时留在两个集合中，集合并仍恰为整张曲面。

下帽为平圆盘，旋转不变。上帽使用 R16、R17 的同一三个互不相交凸起，

$$
b(w)=\sum_{j=0}^2h(|w-c_j|),
\quad h(\rho)=\frac1{2000}\left(1-\frac{\rho^2}{(3/100)^2}\right)^3
\quad(\rho\le3/100),
$$

支撑圆盘外定义为零。因为三个支撑圆盘互不相交，任意点至多一个加项非零，严格有 $0\le b\le1/2000$。这里不能把三个最大高度相加成 $3/2000$。实际外围 cuff 半径是原二进制输入之差；上界证明只需圆盘旋转不变及三个支撑都在内部，不把它替换为有理 $3/20$。

据第1节，对整个 R21 相位区间有

$$
0<\delta_E^{12}\le\frac1{2000}.
\tag{3}
$$

左侧严格正性来自 R21 已支付的三阶中心矩非全等证明，本稿不另由小正浮点差推导它。R21 §3 的握持区直径下界为

$$
D_{12}\ge\operatorname{diam}F_0^{12}(H)
>3.542609695989968>\frac{177}{50}.
$$

因此得到一个完全有理的保守归一上界

$$
0<\frac{\delta_E^{12}}{D_{12}}
<\frac{1/2000}{177/50}=\frac1{7080}
<1.413\times10^{-4}.
\tag{4}
$$

这不把 R21 的上界 $D\le3.92$ 错用作分母下界。此处使用的是两个固定轴心点给出的已审直径下界。

## 3. 对后续工作的准确含义

式 (4) 说明同一 R21 有限族及同一三小凸起标记不可能达到更强目标 $\delta_E\ge.05D$；它没有排除其他固定帽、其他 g 或其他变形机制达到该目标。对保持同一帽高度函数并满足 (1) 的后续真正高模闭族，(2) 仍逐相位适用；其归一数字须使用该候选自己的直径下界，不能直接挪用 R21 数值。

用户当前主完成门使用不对齐的 $\delta_{hold}$。本稿上界只在先施加明确刚体 $R_{-\alpha}$ 后成立，因而不减少 R21 已审的 $\delta_{hold}/D>.0509926386$。$\delta_E>0$ 仍已严格成立。当前 G5 与最后独立完整重跑均继续；此结论不构成阶段性收尾。

## 4. 冻结应用来源

- results/R16-fixed-cap-volume-moment-noncongruence.md — SHA256 278753736f651a82e64bc9d6de61b290395eb3d48390c7b8aef73f939dd565f1。
- results/R17-exact-finite-visible-closed-geometry.md — SHA256 d7ad70cfb98d552ce0832555c230b644e49a21cd5cef2ae16a291013ad66e725。
- results/R21-m12-whole-map-and-actual-metric-decrease.md — SHA256 3d8e20c610ac322e2f4a7093c44b4b37cde314724136cee489dae73c44497c0c。

## 5. 完整独立审查记录

冻结原稿 notes/2026-11-09-db6f-root-cap-alignment-quotient-upper.md 的 SHA256 为 3d32b256f06b84f3785a3796ddd4820174ce2bdab374d6ba89f747f1ca6d87ab。未参与此推导的 /root/coupled_prefix 完整审阅集合命题、双向 Hausdorff 距离、相位像集分解、真实材料角、非负及互不相交的帽函数、实际 cuff 包含关系、R21 直径下界和所有作用域；又全文阅读并核对三份应用来源。

独审文件 notes/2026-11-09-db6f-prefix-review-cap-alignment-quotient-upper.md，SHA256 3b2876166771e02c9ee7a24410500dbf6944d0ef2e617d6aac0cd02b1f2f7b9f；机读说明为同 stem 的 .json，SHA256 cd0e486c195a62aabd72fa74512f9b014132da543dc78c1e82955f6eeba832f1。结论为 PASS，无必须修改项。root 已全文读取该审稿，核对这里正文与被审稿逐字相同。

本结果没有新增数值求解、改变当前曲面或证明主题完成；它也不排除其他标记和机制达到更强目标。
