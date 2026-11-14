# R1：相位族的真实形变上界与窄帽标记的厚度障碍

> 2026-11-09标准更新：本文的旧符号δ均指新版README的δ_E（对完整E(3)取商），不是δ_hold。本文限制或预算的是更强目标，不据此排除新版握持完成标准。
2026-11-08；Astra-visible-flex-effcccee，AI-assisted。

**可信度：已证明的中间结果，未参与推导者独立审查 PASS。不是本题完成。**
构造/证明：repo_amplitude；一般相位上界亦由 geometry_certification 独立得到。
未参与者审查：`notes/2026-11-08-independent-phase-bound-review.md`。
root 核读完整审查后按其第7节修正精确输入、向外端点和适用范围。原推导与脚本在提交 `3b40a5ffb6c048b1f8f9bda719aab7ea8cd61a2b` 中保留；审查列有源码 blob 和 SHA-256。

## 1. 定义和全相位上界

令 $B,C$ 为非空紧集，$R_\alpha$ 为绕固定轴的旋转。设

$$S_\alpha=R_{-\alpha}B\cup C,\qquad S_0=B\cup C.$$

以完整欧氏群（含反射）定义

$$d_{\rm orb}(S,T)=\inf_{A\in E(3)}d_H(AS,T).$$

则对每个实数 $\alpha$，

$$d_{\rm orb}(S_\alpha,S_0)
\le\min\{d_H(R_{-\alpha}B,B),d_H(R_\alpha C,C)\}. \tag{1}$$

**证明。** 同时加入一个共同紧集不增大 Hausdorff 距离。分别以恒等变换和 $R_\alpha$ 作为允许的整体配准，得到两项上界。对更大的群取下确界只能减小结果。证毕。

特别地，假设固定帽由轴对称部分与一个圆盘上的图组成：

$$C_+=\{(x,H+h(x)):|x|\le r_e\},\qquad0\le h\le B_*.$$

旋转图在相同水平点的高度为 $H+h(R_{-\alpha}x)$。两高度都在 $[H,H+B_*]$，逐点配对给

$$d_H(R_\alpha C,C)\le B_*.$$

因此对任何连续相位路径（包括任意多圈），本题定义的形变量满足

$$\boxed{\delta\le B_*.} \tag{2}$$

非径向材料圈的高度峰谷差不进入这个界。此界不要求等距误差已为零，因而对保留同一相位/帽定义的所有数值近似亦成立。

## 2. 窄支撑帽模板的联合障碍

令四个互不重叠的帽标记具有共同支撑半径 $b\le r_e/10$，高度 $a_j\ge0$，形状

$$h(x)=\sum_j a_j\phi_{\beta_j}(|x-x_j|/b),\quad
\phi_\beta(t)=(1-t^2)^4(1+t^{2+\beta})\ (0\le t<1),$$

支撑外为零，$0<\beta<1$。设支撑均在帽圆盘内部。记 $B_*=\max_j a_j$。

令 $u=t^2$。因为 $t^{2+\beta}\le t^2$，

$$0\le\phi_\beta(t)\le(1-u)^4(1+u)\le1;$$

最后一步由导数 $-(1-u)^3(3+5u)\le0$ 得到，中心达到1。因此 $\max h=B_*$。函数在支撑边缘有四阶零；中心的 $|x|^{2+\beta}$ 二阶导数为 $O(|x|^\beta)$，所以图函数为 $C^2$。在最高标记中心，

$$\nabla h=0,\qquad D^2h=-8B_*b^{-2}I.$$

该点第一基本形式为 $I$，故两个实际主曲率绝对值均为 $8B_*/b^2$。

对任意 $C^2$ 闭嵌入曲面及任意实际非零主曲率 $\kappa$，

$$\operatorname{reach}(S)\le1/|\kappa|. \tag{3}$$

为明确不等号方向，取 $0<\rho<\operatorname{reach}(S)$。法向管内最近点唯一，展开以 $p\pm\rho n$ 为球心的空球不等式，得

$$|n\cdot(q-p)|\le |q-p|^2/(2\rho).$$

沿主方向取 $q-p=sv+\kappa s^2n/2+o(s^2)$，先令 $s\to0$ 再令 $\rho\uparrow\operatorname{reach}(S)$，即得(3)。这里使用确切曲率，绝未把一个曲率上界倒用成 reach 上界。

设上述族每个相位都是 $C^2$ 闭嵌入，并令

$$D=\operatorname{diam}S_0,\qquad \rho_*=\inf_t\operatorname{reach}(S_{\alpha(t)}).$$

帽边界含完整半径 $r_e$ 的圆，因此 $D\ge2r_e$。当 $B_*>0$ 时，(2)、(3) 给出

$$\boxed{\frac{\delta\rho_*}{D^2}
\le\frac{B_*}{D^2}\frac{b^2}{8B_*}
\le\frac1{3200}.} \tag{4}$$

当 $B_*=0$ 时固定帽轴对称，(1)给 $\delta=0$，结论仍成立。本题要求的乘积为

$$\frac1{20}\frac3{100}=\frac3{2000}>\frac1{3200},$$

故该模板不能达标。若单独保留全部时刻 reach$\ge3D/100$，则

$$\delta/D\le1/96. \tag{5}$$

这只排除给定整体相位架构和给定窄标记形状。任意宽帽、不同峰顶二阶系数、符号变化或重叠标记、多个独立相位模块均不在(4)的自动适用范围内。保持本节峰顶二阶系数和(2)时，放宽支撑半径的必要条件才是 $b/D\ge\sqrt{3/250}$。

## 3. 应用于当前 wide-m2 的精确数字

实际带的 core、上下 prefix/tail 及圆领均采用

$$F_\alpha(s,\theta)=R_{-\alpha}F_0(s,\theta+\alpha).$$

材料角平移遍历同一圆周，故整个带的像确实为 $R_{-\alpha}B$；下半带固定反射与固定角平移不改变这个全局相位关系。两帽固定。来源与版本由独审报告逐一锁定，尤其是 `large-amplitude-twist-flex/scripts/f6root_closed_wide_m2_model.py` 和 `scripts/f6root_inward_caps.py`。

R35 数学定义使用精确 binary64 输入

$$r_e=\frac{7746191359077253}{9007199254740992},\qquad
\sigma=\frac{2116691824864133}{2251799813685248}.$$

数学帽参数为 $b=\sigma/20$、$A=b^2/(100\sigma)$、四高度 $(A,A,A,2A)$，所以

$$B_*=\frac\sigma{20000},\qquad
D\ge2r_e=\frac{7746191359077253}{4503599627370496},$$

$$\boxed{\frac\delta D\le
\frac{2116691824864133}{77461913590772530000}
<2.7325581396\times10^{-5}.} \tag{6}$$

注意 $2r_e$ 略小于十进制实数 $1.72$，不能把其近似显示替换为严格下界 $D\ge1.72$。Python 中间运算冻结后的最大存储高度比 $\sigma/20000$ 小 $9/92233720368547758080000$，且存储半径仍严格小于 $r_e/10$；因此这些执行舍入不损害(4)、(6)。详情见独审第7节。

运行

```bash
python notes/repo_review_phase_shape_bound.py
```

可复算精确分数和经过 Fraction 比较的向外十进制端点。脚本还显示已有 $H$ 与曲率采样值作数值背景，但它们均未参与(4)、(6)。

## 4. 对继续构造的用途

旧微标记只提供定性的非全等识别。要达到本题宏观形变，至少须让活动带与固定部分都具有宏观旋转不对称性，或使用不能被同一整体旋转同时对齐的多个活动模块。与此同时仍须真正解出完整等距方程、固定几何加密收敛、全时刻嵌入与全局 reach。本文不提供这些尚缺的正向输入；QUEUE 继续为进行中。
