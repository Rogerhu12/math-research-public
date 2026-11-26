# 当前尾源码的转角均值与二阶接缝相容

日期：2026-11-26。工作范围：将已登记的 R12/R14 应用于当前恢复的
M24 尾源码，消去不必要的独立 mean 边界条件，并明确近似场真正要支付的误差。
这不是新的存在性结论，不声称 full-H、linear-DN 或 warm 场已经满足连续接缝。

## 1. 已读取的源码和符号

恢复树中的源文件为
`multistage-source/repro/source-root/topics/large-amplitude-twist-flex/scripts/` 下的：

| 文件 | 已读源码 SHA-256 |
| --- | --- |
| `general_root_tail_momentum.mjs` | `182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c` |
| `f6tail_momentum_physical_jets.mjs` | `2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8` |

第一份源码的均值根方程需接到连续转角；第二份源码的 `darboux`
需按它实际使用的归一化支付二阶误差。

令下侧 worker 的高度为 $u$，固定第一基本形式为

$$
g=E\,dR^2+R^2\,d\theta^2,\qquad E=1+w^2.
$$

定义

$$
P=\frac{u_\theta}{Rw},\quad K_m=\frac{u_R}{w}-1,\quad
L=K_m+P_\theta,
$$

其中 $K_m$ 不表示 Gauss 曲率。源码使用的量为

$$
S=1-w^2P^2,\quad
D=1-w^2(2K_m+K_m^2+EP^2),\quad
A=1+K_m+EP_\theta=1+L+w^2P_\theta.
$$

## 2. 原源码的三个分支量恰好给出 R14 的假设

平面投影的度量 $h=g-du^2$ 满足逐点精确等式

$$
h_{\theta\theta}=R^2S,\qquad \det h=R^2D,
\qquad Q:=Eu_{\theta\theta}+Ru_R=RwA.
$$

目标上尾采用 $z=\text{常数}-u$，故上尾的 $Q=-RwA$。
在整个角周期、以及比较所用的完整均值区间上验证 $S,D,A>0$，便同时
给出 R14 的正定平面投影和同一严格负 $Q$ 分支。
无需再添加一个自由 `meanSlope` 或 `meanSecond` 边界参数。
原 Newton 网格的正值只检验了有限个角点，不能代替这里的连续分支验证。

## 3. `moments[0]` 与连续转角的精确联系和误差预算

选择和圆截面一致的正转角方向。连续角速度为

$$
\omega=\frac{1+w^2(1+K_m)P_\theta/S}{\sqrt D}.
$$

令 $T=2K_m+K_m^2+EP^2$、$s=\sqrt{1-w^2T}$。源码中的

$$
f_c=\frac{w^2T(2+s)}{2s(1+s)^2},\qquad
g_c=\frac{w^2\{P^2+ST/(1+s)\}}{Ss},
$$

$$
q=\tfrac12(K_m^2+EP^2)+K_mP_\theta+Tf_c
 +(1+K_m)P_\theta g_c
$$

满足

$$
\tfrac12+f_c=\frac1{s(1+s)},\qquad 1+g_c=\frac1{Ss}.
$$

因此逐点严格有

$$
\boxed{\omega-1=w^2(L+q).}
$$

此等式没有小扰动截断、linear-DN 或采样假设。原 root 的零模方程所针对的
正是转角一周约束的离散版本，不是另一个可任意调节的平均高度斜率。

令 $I=(2\pi)^{-1}\int_0^{2\pi}\omega\,d\theta$。源码的
`moments[0]` 计算 $L_0+\operatorname{avg}_Nq$。若角点是真正等角点，
基表是真正三角函数，且频率不混叠，则

$$
\operatorname{avg}_N(\omega-1)=w^2\operatorname{moments}[0].
$$

实际执行器的角点和三角表是字面 binary64 数，不能直接调用精确正交性。
写源码所用的展开为 $L=L_0+\sum_{j\ge1}L_j\,cs_j$，其中 $cs_j$
包括该源码的基函数归一化。把表中的字面值理解为确定实数时，应保留

$$
\operatorname{avg}_N(\omega-1)=w^2\left(
\operatorname{moments}[0]+\sum_{j\ge1}L_j\operatorname{avg}_N cs_j
\right).
$$

此外，从浮点执行日志推证精确式，还须支付实际运算误差。
一个有效的连续误差预算是

$$
|I-1|\le w^2\bigl(|r_0|+|r_{\cos}|\bigr)
 +\epsilon_{\rm eval}+\epsilon_{\rm quad},\qquad
r_{\cos}=\sum_{j\ge1}L_j\operatorname{avg}_Ncs_j.
$$

这里 $r_0$ 必须是根残差的严格上界；
$\epsilon_{\rm eval}$ 包括从实际字面表及浮点求值到真实等角函数的误差；
$\epsilon_{\rm quad}$ 是真实等角离散平均到连续平均的求积误差。
直接对真实高度 Fourier 迹的 $\omega$ 作外包区间求积，也能支付此项，
无需逐项反推执行日志。已经固定的 `mean1168` 和 `GL6` 定义均不因此改变。

## 4. 平均一阶迹已经由转角一周强制

固定 $u(R_c,\theta)$ 和 $u_R$ 的全部非零 Fourier 系数，
只以 $c=\operatorname{avg}u_R$ 为变量。直接微分得

$$
\boxed{\frac{\partial\omega}{\partial c}=\frac{wA}{D^{3/2}}.}
$$

在同一连通均值括区内有 $S,D>0$、$A\ge a_*>0$ 时，
$I$ 严格递增。由于

$$
D=E-u_R^2-Eu_\theta^2/R^2\le E,
\qquad I'\ge\frac{wa_*}{E^{3/2}},
$$

R14 说明同一分支下、上述完整非均值数据相同的两个精确闭合截面，
必有相同的平均斜率。这里没有向入口 BVP 添加一个独立平均斜率条件。

有限误差版本为

$$
|c_1-c_2|\le\frac{E^{3/2}}{wa_*}
\bigl(|I(c_1)-1|+|I(c_2)-1|\bigr),
$$

前提仍包括连接两个均值的整个括区上的分支界。

在真实 cut $R=\operatorname{binary}(0.3)$、
$w=\operatorname{binary}(0.08)$、$E=1+w^2$，
且**仅条件性假定** $a_*=1/10$ 时，已完成的向外数值常量为

$$
I'>0.007923809845279212,\qquad
\frac{E^{3/2}}{wa_*}<126.20191795689954.
$$

没有当前 full-H 场的连续分支证书时，不得将 $a_*=1/10$ 当成已验事实。

若仅有一个近似 $c$，可取
$m_0=wa_*/(2E^{3/2})$、$\delta=\nu/m_0$，其中
$\nu\ge|I$c$-1|$。再验证整个 $[c-\delta,c+\delta]$ 上
$D>0$、$A\ge a_*/2$，即有
$I(c-\delta)\le1\le I(c+\delta)$。严格单调性给出唯一连续转角均值根。
这只证明局部标量根，不替代完整非线性尾解。

## 5. 当前 `darboux` 的单位与平均二阶迹

记

$$
A_H=u_{RR}-\frac{E'}{2E}u_R,\quad
B_H=u_{R\theta}-\frac{u_\theta}{R},\quad
C_H=u_{\theta\theta}+\frac R E u_R,
\quad K_g=\frac{E'}{2RE^2}.
$$

Darboux 方程为
$A_HC_H-B_H^2-K_g\det(g-du^2)=0$。
当前 `f6tail_momentum_physical_jets.mjs` 的 `darboux` 是

$$
\boxed{\delta_D=
\frac{A_HC_H-B_H^2-K_g\det(g-du^2)}{ER^2}.}
$$

不能误把打印值当成未归一化的分子。
在完整高度一阶迹相同后，$B_H,C_H,h$ 都相同；又
$C_H=RwA/E$，故

$$
|u_{RR}^{(1)}-u_{RR}^{(2)}|
\le\frac{E^2R}{wa_*}
\bigl(|\delta_D^{(1)}|+|\delta_D^{(2)}|\bigr).
$$

在上述 cut 和条件 $a_*=1/10$ 下，该系数的向外上界为 `37.981536`。
精确 Darboux、相同完整一阶迹且处于同严格分支时，二阶迹亦相同；
`meanSecond` 无须另作一个独立边界自由度。
有限谱或 linear-DN 场必须支付自身实际 Darboux 残差。
仅有小的零阶 metric 误差不推出该残差或其导数小。
若完整一阶迹尚有差，则必须另加 $B_H,C_H,h$ 的差异预算，
不能直接使用上面的简式。

## 6. 位置合同和没有支付的项目

位置仍按已登记的真实高度原函数 $Z_c$ 处理。上尾

$$
z=z_b+h(R_c)-h$R$-\mu$R$-H_{\rm nonzero}(R,\theta)
$$

取 $z_b=Z_c+\mu_c$ 后，零模位置严格匹配。
这是唯一的高度加法常数规范，不修复非零模位置、一阶或二阶迹。
实际公共 Cartesian $C^2$ 接缝仍需完整平面/高度迹和公共 $R$ 的
0、1、2 阶匹配。R14 只在精确相同度量、同严格分支和全周转角
均已验明时，消去非独立的均值条件。

当前完成的是源码恒等式、归一化分析和条件数常量，未接受新 full-H 场。
轻量审计应从真实 accepted 原始包中的 `response.jets` 出发
（由请求的完整 jets 选项产生），验证连续
$S,D,A$ 下界、连续转角包围及严格 Laurent Darboux 上界，
然后才可讨论同一 $g$ 下实际接缝的修补预算。
M24、$\lambda=.002$ 的旧证书、`mean1168`、`GL6` 仍只用于各自原范围。

## 7. 重建记录

此前共享环境的 `/tmp` 随环境重置消失。本 note 依据此前实际读取的源码、
已完成代数推导和保留运行输出重建；上列哈希仅指被分析的两份源码，
不表示重建审计脚本和旧临时脚本字节相同。
常量的精确有理数及平方根外包重建记录见
`2026-11-26-seam-mean-source-constants.json`。
