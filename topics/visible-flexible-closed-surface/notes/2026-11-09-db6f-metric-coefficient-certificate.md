# 连续前缀 metric 的系数证书与解析供应器

2026-11-09，independent_geometry。状态：实现及完整条件论证，待未参与实现者审查；真实候选结果由分别冻结的 JSON 给出。此工具不把有限前缀变成完整闭曲面。

## 1. 为什么先相减系数

若直接用坐标区间分别包围 $|F_s|^2$ 与 $1+a^2\theta_s^2$，小网格内两个各自为 $O(1)$ 的量仍有一阶宽度，无法显示 $10^{-7}$ 级差。这里先在同一个径向幂基和有限 Fourier 基中算出二者的差，再包围所得残差多项式。

实际图为保存的共享二阶 jet 五次 Hermite 图，其数学定义见 `2026-11-09-db6f-audit-geometry-proof-and-enclosures.md`。在柱坐标架写
$$X=R e_r+T e_\theta+Z e_z.$$
角导数为 $(R_\psi-T,R+T_\psi,Z_\psi)$，径向导数为 $(R_s,T_s,Z_s)$。因此实际坐标第一形式的三个系数 $E,F,G$ 均是径向多项式、有限角 Fourier 多项式。径向次数分别至多 8、9、10。

`db6f-audit-metric-polynomial.py` 独立从保存的 exact Hermite 定义计算这些系数，不导入非线性求解器或其 frame/metric 评估。

## 2. 目标 metric 与正交框架

给定固定的解析函数 $a(s)>0$、$e(s)$，令
$$\theta=\psi-e(s)\sin(3\psi)/3,\quad
\rho=1-e(s)\cos(3\psi),\quad
\theta_s=-e'(s)\sin(3\psi)/3.$$
原材料 metric 为 $ds^2+a(s)^2d\theta^2$，在 $(s,\psi)$ 坐标中为
$$g_{ss}=1+a^2\theta_s^2,\quad
g_{s\psi}=a^2\theta_s\rho,\quad g_{\psi\psi}=a^2\rho^2.$$

供应器对每个审计段给出 $a,e,e'$ 的区间幂系数和一致余项。将余项作为常数系数的额外区间宽度是合法的点值包围：余项允许随 $s$ 变化，并不假设其真的是一个常数。

记三个坐标残差的一致界为 $b_E,b_F,b_G$。若 $a\ge a_*>0$、$\rho\ge\rho_*>0$，并令 $v_*=\|e'\|_\infty/(3\rho_*)$，在材料正交框架
$$U=\partial_s-(\theta_s/\rho)\partial_\psi,\quad
V=(a\rho)^{-1}\partial_\psi$$
中，残差矩阵三个条目的绝对值分别不超过
$$b_{11}=b_E+2v_*b_F+v_*^2b_G,$$
$$b_{12}=(b_F+v_*b_G)/(a_*\rho_*),\quad
b_{22}=b_G/(a_*\rho_*)^2.$$
故相对 metric 算子范数不超过
$$\max\{b_{11}+b_{12},\ b_{12}+b_{22}\}.$$
脚本对这一步也向外舍入。

## 3. Fourier 相乘与径向 Bernstein 包围

为避免三角求值误差，整个残差计算使用 Laurent 系数，以 $e^{3ij\psi}$ 为基。由于三重/反射对称，$R,Z$ 为实偶系数，$T$ 为纯虚奇系数；$E,G$ 为实系数，$F$ 为纯虚系数。代码保留一个 $i^p$ 标记，不能将正弦系数直接当余弦系数相加。

二维系数卷积用无进位的混合编码：Fourier stride 至少为两个输入的频率长度之和减一。因此一维卷积准确对应径向次数与 Fourier 频率的二维卷积，没有 aliasing。

卷积与小矩阵乘法采用明确舍入模型：每个 dot product 的乘加数目不超过 $2n+2$，正确舍入的 fused multiply-add 也允许。以比 binary64 roundoff unit 更大的 $u=2^{-52}$ 及
$$\gamma_{2n+2}=\frac{(2n+2)u}{1-(2n+2)u}$$
包围舍入误差，并另加 $(2n+2)$ 倍最小正 subnormal 的绝对预算。正项 dot product 的上界按 $(\mathrm{observed}+\mathrm{underflow})/(1-\gamma)$ 计算，所有后续操作向外舍入。输入区间宽度的贡献分别为 $|A|\,\mathrm{rad}(B)$、$\mathrm{rad}(A)|B|$、$\mathrm{rad}(A)\mathrm{rad}(B)$。这不是对浮点结果直接加一个任意经验 epsilon。

残差的每个 Fourier 系数 $p_j(u)=\sum_{k=0}^d c_{kj}u^k$，$0\le u\le1$，转换成 Bernstein 系数
$$b_{kj}=\sum_{i=0}^k c_{ij}\frac{\binom{k}{i}}{\binom di}.$$
每个有理权重先向外转浮点区间，小矩阵乘法仍使用上述误差预算。由 Bernstein 凸包性质，
$$\sup_{u,\psi}\left|\sum_jp_j(u)e^{3ij\psi}\right|
\le\sum_j\max_k|b_{kj}|.$$
这同时控制整个径向段和全圆，未从有限角采样推连续上界。

数值后端假设为通常 IEEE754 binary64 算术、平方根和有限标准乘加 dot product。脚本不提供证明助理级的机器语义形式化。所有有效除数均先证为正，输入/输出要求有限。

## 4. Flat ramp 的解析定义

`db6f-audit-metric-supplier.py` 将保存的主输入 $\delta,v_u,v_d,\varepsilon,\eta$ 解释为精确二进有理数，并以 Fraction 计算
$$T_u=\delta/[v_u(1-\varepsilon)],\quad
T_d=\delta/[v_d(1-\varepsilon)].$$
不把分别舍入的多个冗余派生数误认为精确相等。假设 $\delta>0$、$0<v_u,v_d<1$、$0<\varepsilon,\eta<1/2$，并检查整数正周期数。

源码 `turn_ramp` 的 primitive 是三段多项式：
$$P(t)=\begin{cases}
[t^4/(4\eta^2)-t^5/(10\eta^3)]/(1-\eta),&t\le\eta,\\
[t^2/2-\eta t/2+3\eta^2/20]/(1-\eta),&\eta\le t\le1-\eta,\\
t-1/2+P(1-t),&t\ge1-\eta.
\end{cases}$$
随后 $I(u)=\varepsilon P(u/\varepsilon)$、$u-\varepsilon/2$、$1-\varepsilon-\varepsilon P((1-u)/\varepsilon)$，分别用于上 ramp、平台、下 ramp。半周期的 $a$ 用原参数公式组合，均以 Fraction 精确展开。

段断点本来是有理数，落在 binary64 审计网格时可能产生极小两侧延伸。供应器枚举审计段与**所有**真实解析 pieces 的交叠，把相邻多项式差在实际交叠子区间上用精确有理多项式包围，再加入 uniform remainder。没有把 $0.75$ 与 $0.7500000000000001$ 之类接近但不同的断点默认为相同。

## 5. 角向 spline 与截止函数

保存的 knots、values、末端导数均作为精确二进有理数。供应器用 Fraction 解 clamped cubic spline 的三对角线性系统，首端导数精确为零。它不将独立舍入的 PPoly 系数冒充精确 $C^2$ spline。

以 $x=s/s_{end}$，将该 spline 乘 $8q_{warp}$ 及原 quintic cutoff $1-S(4x-3)$（$x>3/4$），给 $e$ 的至多八次局部多项式。$e'$ 从此**同一个精确多项式**求导；其在端点与 cutoff 的两阶匹配由公式保证。近断点的交叠误差同样精确计入。

这是固定物理度量的一个明确 $C^2$ 参数图；原求解器对 spline 和派生量的数值舍入差反映在实际图与此目标的残差中。

## 6. 桥的真积分与保留的根误差

当前供应器从原 `DirectionalBridge` 提取冻结的 binary64 数 $L,p_t,p_s$，并记录 helper 源哈希。之后定义
$$\phi(t)=p_t(3t^2-2t^3)+Lp_s(t^3-t^2),\quad
a(s)=1+\sigma L\int_0^{(s-s_0)/L}\sin\phi(t)\,dt.$$
**这一次积分是解析真积分，不是保存的 64 点 Gauss 求积值。**

在每个审计段，以该段中点的精确有理相位 $\phi_c$ 展开 $\sin(\phi_c+w)$。$\sin\phi_c,\cos\phi_c$ 由带 Lagrange 余项的 25 阶零点 Taylor 区间包围。外层取至五阶，若 $|w|\le W$，点值余项不超过 $W^6/6!$。积分后加 $\Delta s\,W^6/6!$，再把超过八次的幂系数绝对值和计入一致余项。节点半径通过同一真积分的连续区间累加传递，未每段重新拟合。

若精确 prefix 终点与第一个 bridge 审计端点只差一个浮点 sliver，初始 anchor 用 $|\sin\phi|\le1$ 包围；两种局部延伸的差用 $2\,\mathrm{sliver}$ 包围。前缀导数小于 1 的输入条件在代码中已核查；对伸出原 prefix 的微小多项式延伸，还须检查 $\mathrm{sliver}<\varepsilon\eta T_{last}/4$。此时末端平顶 ramp 的延伸速度也小于 1：其归一化端部参数绝对值不超过 $\eta/4$，代入显式三次/四次速度式即得。实际 coupled M8 的这个附加不等式已经用 Fraction 独立核查，见 `2026-11-09-db6f-audit-metric-flat17-coupled-sliver.json`。新输入需重做此项，不能从“小于一个 ulp”的口头描述省略。

**保留的定义缺口：** 原 helper 的 $L$ 来自浮点求积与 brent 根，$p_t,p_s$ 也被舍入。当前证书对应上述冻结常数定义的真积分前缀；没有证明它们满足最终的精确 cut 匹配根。输出单列端点半径、端点径向速度差和总长坐标差，`exact_bridge_matching_root_certified=false`。要给完整统一的 exact-root $g$，须另加精确根区间及误差传播；不能把目前 $10^{-13}$ 量级差写成零。

## 7. 全相位含义

若已由 $\rho>0$ 定义材料角 $\theta$ 的全局反函数，取相位族
$$F_t(s,\psi)=R_{-t}F_0(s,\psi_t),\qquad
\theta(s,\psi_t)=\theta(s,\psi)+t.$$
原 $ds^2+a^2d\theta^2$ 对此材料角平移不变，环境旋转等距。因此整个相位周期的相对 metric 算子误差与基准相同。这个结论只用于实际按上述公式定义的族，不适用于任意时间线性插值。

这仍不能替代尾、帽、固定握持、非全等、同一精确解的加密收敛及全曲面的几何认证。

## 8. 调用接口

在仓库根执行，先供应后审计：

```text
python topics/visible-flexible-closed-surface/scripts/db6f-audit-metric-supplier.py \
  --geometry <Hermite metadata.json> \
  --source-root topics/visible-flexible-closed-surface/repro/source-root \
  --out-prefix <target-prefix>
python topics/visible-flexible-closed-surface/scripts/db6f-audit-metric-polynomial.py \
  --geometry <同一 Hermite metadata.json> \
  --target <target-prefix.json> --out <metric-certificate.json>
```

全部 JSON 绑定 metadata、压缩数据、实现脚本和算术后台的哈希。供应器与后台的独立全文审查、实际重跑应另外记录，后台本身不自动把外部供应器标成已审。

## 9. 独审发现的分支缺陷及修正版

root 在独立全文审查中发现原供应器 SHA256 `2d4b79f75fe03098d4e2bc5557b706a75e581dfc3e2ca69262a17c9cc8ad63a8` 的一处真实逻辑缺陷：`a_prefix_poly` 虽收到要计算的精确分段编号 $k$，却再次按整个审计段中点选择 primitive 分支。若审计段含一个真实分段断点的微小 sliver，替代分支可能被错误选回主分支，因此原来的重叠误差计算漏项。原报告保留作来源记录，**不视作通过独审的连续证书**。

现按分段编号固定 primitive：上 ramp 的 $k=0,1,2$ 对应 low/middle/high，下 ramp 的 $k=4,5,6$ 对应 high/middle/low。不再让整段中点覆盖传入分支。另把 §6 的 $\mathrm{sliver}<\varepsilon\eta T_{last}/4$ 条件加入程序的强制检查，并记录精确有理 sliver 与允许值。仅当主多项式被延伸到 prefix 右侧时需要这项；若主桥多项式向左跨入原 prefix，则两边真实导数的模本来就不超过 1。

修正后供应器 SHA256 为 `de2cafcb235a843b2f930decb54cf065c6cbc441884b050f09edb900ac196bd0`，残差后台保持 SHA256 `02f9da4d86c7514bf90a3cfd185be85274c7ad0b9b34d3d20ede342d6b8adea4`。用 Fraction 对所有相邻 flat-ramp 多项式的值、一阶、二阶连接条件作了精确核对，均相等。来源和变动账本在 `2026-11-09-db6f-audit-metric-supplier-correction.json`。

真实 coupled M8 的修正只改变八个 `a_remainder` 条目，最大浮点差诊断为 $1.185\times10^{-60}$ 以下；这个微小量不能作为免修缺陷的理由。新目标文件为 `2026-11-09-db6f-audit-metric-flat17-coupled-m8f16-target-v2.json`，其 SHA256 为 `b5bd8a4e8905693e74a3ce98ab8abb07dec095cc3352c017c421c1d56e7622a5`，数据 SHA256 为 `4674eef190bb613fc3953e37fc6f643636c15ecbf45bf97ac2d4f3d1cadf62d2`。

新目标独立于旧输出重新生成，846 个审计段全部重新检查，`2026-11-09-db6f-audit-metric-flat17-coupled-m8f16-v2.json` 给

$$\|g^{-1/2}(F^*\delta-g)g^{-1/2}\|_{op}\le3.622549868552692\times10^{-7}.$$

该数与原来的最坏区间相同。它仍然只属于冻结 binary 桥常数加真积分定义的有限前缀；精确匹配根和全图组装的缺口保持明确未支付。修正版的独立复核由 root 另行记录。
