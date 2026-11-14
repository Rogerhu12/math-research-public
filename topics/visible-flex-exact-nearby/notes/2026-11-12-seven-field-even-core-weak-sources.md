# 2026-11-12 七场乘子与腰偶核心弱残差入口

## 状态与范围

这是在执行器再次失联后完成的源码与完整接口证明。新源码尚未原生执行，不能把它当成已经输出了新的场误差、源Gram或全局逆常数。旧五场入口不修改；新的七场入口和腰偶参考各用独立文件。已有175叶仍是同一 $\delta_5\pm10^{-9}$ 家族。

新增：

- `fourfold_phase_core_source_wiring_polynomial.py`：五个实际PDE系数以及 $\alpha=1/a,v=b/a$ 的完整系数矩形、无限余项和真实 $M_s$；
- `fourfold_phase_core_even_reference.py`：五个归一化角偶、腰偶物理高度输入，两个Cauchy通道全程保留；
- `fourfold_phase_core_even_weak_residual.py`：同一参考的全有限频率强弱源Gram，接受真正完成的旧五场或新七场报告，严格按对应源身份读取。

## 1. 两个额外乘子的真实几何公式

令
$$
X=F_r,\quad Y=F_\theta,\quad C=Y\times X,\quad
R_2=F\cdot F,\quad S=C\cdot F,
$$
$$
m=C\cdot F_{r\theta},\qquad n=C\cdot F_{\theta\theta}.
$$
R37 已使用的原物理系数是
$$
a=-nR_2/S^2,\qquad b=mR_2/S^2.
$$
因此准确地有
$$
\alpha=\frac1a=-\frac{S^2}{nR_2},\qquad
v=\frac ba=-\frac mn. \tag{1}
$$
这两个标量乘子不同于有限Toeplitz矩阵 $P_NaP_N$ 的逆。程序不把它们混为一谈。

同一已有原生 primitive/Taylor 内核先完整形成 $F,X,Y,F_{r\theta},F_{\theta\theta}$，包括真无限角原函数与径向Taylor尾。节点计算用因子形式 $-(S/n)(S/R_2)$ 以避免不必要的复矩形包裹；仍在实际 $n$ 与 $R_2$ 不含零时才计算。

整径向复盘、整角复带使用父内核已经证明的
$$
|n|\ge n_*>0,\qquad |R_2|\ge R_*>0.
$$
这里 $n_*$ 来自真实 moving-frame 乘积无零点门，不能要求宽原始矩形的实部为正来代替。重新求同一域中的实际 $|S|\le S^*$ 和 $|m|\le m^*$ 后，
$$
|\alpha|\le\frac{(S^*)^2}{n_*R_*},\qquad
|v|\le\frac{m^*}{n_*}. \tag{2}
$$
(2) 是整个已声明二复变量域的界，可用于完整Cauchy/DFT费用；它不是只在节点成立的分母判断。腰处使用原内核准确的 $F_z/r$ 可去奇点，未改实际对象。

## 2. 完整矩形和乘子范数

所有角频率是物理频率 $4k$；$x=4\theta$ 只用于保存其 $2\pi$ 周期系数。实际实族中的角奇场为 $b,\sigma,v$，角偶场为 $a,c,\tau,\alpha$。正侧原矩形的径向反射奇场只有 $b,v$，$\sigma$ 径向偶。

程序完全保留所选时间/角矩形，并付：

1. 真角DFT的全部正负 alias；
2. 时间圆周DFT的全部高阶 alias；
3. 所选 dyadic 系数及原生节点/无限原函数误差；
4. 矩形外完整补集：所有高角模，以及保留角模的所有高时间阶。

记余项实际物理导数 Wiener 预算为
$$
E_j\ge\sum_k(4|k|)^j|\widehat e_k|,
\qquad j=0,1,2,
$$
其中 $j=0$ 的零模权为1。系数随实时间的完整上界已经求和，不再漏一个时间因子。对 Sobolev 乘子可用
$$
M_s(f)=\sum_k(1+4|k|)^s|\widehat f_k|.
$$
代码的误差费用是
$$
\begin{array}{c|c}
s& M_s(e)\text{ 的上界}\\ \hline
0&E_0\\
1/2&E_0+\sqrt{E_0E_1}\\
1&E_0+E_1\\
3/2&\sqrt{(E_0+E_1)(E_0+2E_1+E_2)}\\
2&E_0+2E_1+E_2 .
\end{array} \tag{3}
$$
前两种分数阶用加权 Cauchy--Schwarz；整数阶由二项式展开。完整有限多项式则直接对每个准确 dyadic 系数求
$\sum_{i,k}(1+4|k|)^s|c_{ik}|$，对 $|u|\le1$ 有效。相加得到报告的
`complete_true_real_time_multiplier_norms`，尤其明确提供R107所需 $M_{3/2}(\alpha),M_{3/2}(v)$。

这仍不是实际规范角/返回标签的接线常数 $K_{\rm wire}$；该几何坐标变换必须另付。

## 3. 无18输入Dirichlet逆的准确腰偶参考

设 $Q_c$ 为R105的九到五余弦等距映射，$U_c=\operatorname{diag}(Q_c,Q_c)$。将每个原始完整局部转移中心和生成元多项式作准确代数压缩
$$
T_j^c=U_c^*T_jU_c,\qquad B_j^c(u)=U_c^*B_j(u)U_c .
$$
没有再选一个新的浮点压缩中心。每个局部多项式递推得到 $Z_j(u)$ 后定义
$$
R_j(u)=Z_j(u)Z_j(-1)^{-1}
+\frac{u+1}{2}\left(T_j^c-Z_j(1)Z_j(-1)^{-1}\right). \tag{4}
$$
故准确有 $R_j(-1)=I$、$R_j(1)=T_j^c$。这是代数恒等式，不以小数误差“近似相等”代替。

令 $P_j=T_j^c\cdots T_1^c$，最终 $P=\begin{pmatrix}A&B\\C&D\end{pmatrix}$。只使用已经实际通过扰动门的五高度矩阵 $A$，取初始映射
$$
V_0=\frac1{\sqrt2}\binom{A^{-1}}0. \tag{5}
$$
在正半第 $j$ 段，参考状态为
$$
\binom{w}{p/8}=U_cR_j(u)P_{j-1}V_0. \tag{6}
$$
所有径向接缝准确连续，且右端 $w=Q_cv/\sqrt2$。负半定义 $w(-r)=w(r),p(-r)=-p(r)$，所以左端同为 $Q_cv/\sqrt2$。径向导数因 $r=\pm(c+hu)$ 带有准确 $\pm1/h$。腰处 $p(0)=0$，没有跨腰通量跳跃。

输入的五维欧氏范数正是两端配对物理高度的总 $L^2$ 范数，角均值未去掉。regular均值是帽问题的第六个坐标，它在直接核心参考中为零列，但不从完整低块消失。

参考端点投影通量为 $8CA^{-1}$，未先作Hermitian投影。新残差包单独保存这个原始参考通量中心和选择误差；不能把它默认为R105保存的Hermitian DN中心，更不能默认等于实际全频DN。两者的差在最终装配中明确计费。

## 4. 完整弱源恒等式

对分段参考 $w,p_N$ 使用同一实际弱形式
$$
b(w,\varphi)=\int
(a w_r+b w_\theta)\varphi_r+
(bw_r+cw_\theta+\sigma w)\varphi_\theta+
(\sigma w_\theta-\tau w)\varphi .
$$
令
$$
\begin{aligned}
R_r&=aw_r+bw_\theta-p_N,\\
R_\theta&=P_H(bw_r+cw_\theta+\sigma w),\\
R_0&=\sigma w_\theta-\tau w-\partial_rp_N
-\partial_\theta P_N(bw_r+cw_\theta+\sigma w).
\end{aligned} \tag{7}
$$
积分分部给出相对参考端点 $p_N$ 的准确弱负荷
$\int R_r\varphi_r+R_\theta\varphi_\theta+R_0\varphi$。由于 $p_N$ 在所有接缝连续，没有遗漏其内部delta负荷；$R_r$ 可分段不连续，其分布导数已经由弱形式保留。

每个有限Fourier乘积的全部输出 $[-K-N,K+N]$ 都参与。对每种时间幂先形成其输入列 Gram $G_i$。任意正数 $t_i$ 给出
$$
\int_{-h}^{h}\left\|\sum_i u^i V_iv\right\|^2dr
\le
h\left(\sum_i t_i\right)
v^*\left(\sum_i\frac{2G_i}{(2i+1)t_i}\right)v. \tag{8}
$$
这是加权Cauchy--Schwarz后积分，不把不同时间幂的交叉项擅自删掉。源码选
$t_i=\sqrt{2\|G_i\|/(2i+1)}$ 的有向正上界，零行可准确省去。

真系数余项用 (3) 作为乘子作用于完整参考列范数；$P_N,P_H$ 在各 $H^s$ 中收缩，且
$\|\partial_\theta P_N\|\le4N$。因此 (7) 的 scalar-all 要额外付 $4N$ 倍 angular coefficient 误差，scalar-high 没有这项。对有限源到真源的 $L^2_rH^s$ 误差 $E$ 和有限源范数 $L$，Gram差至多
$$
2LE+E^2,
$$
再加完整Gram中心选择费。由此得到对所有输入向量的PSD主控，不声称选定Gram恰好等于真残差Gram。

报告分别输出 $s=0,1/2,1,3/2$ 的 radial-all、radial-high、angular-high、scalar-all、scalar-high。若只计算正半，准确径向奇偶性使负半相同 $H^s$ 平方范数，完整核心可在同一五输入坐标中把正半Gram乘2；这个因子不能与(5)的 $1/\sqrt2$ 归一化混淆。

## 5. 原生恢复后的最短执行

先用已存五命令重放器恢复全局核心及六块完整数据。随后选择一个完整175叶报告作为 `--leaf-report`，用新七场入口实际求一个完整矩形；取其正侧全cover序号作 `--leaf-index`，交给新 `even_weak_residual`。每个入口均拒绝不同对象、不同参数盒、不同实际径向区间、不同依赖源或不完整数组。新弱源可直接读取已有五场矩形，只有在需要额外 $\alpha,v$ 接线时才要求七场包。

当前没有声称新入口已运行。首轮优先一个普通span和腰span，取得实际误差/开销后才决定全覆盖布局；这不是额外批准流程，而是实际确定尚未知的数值成本。

全强源的严格负区、真实转折区、正领圈仍要分别接正确算子。上面的弱源恒等式对整个有限试探有效，不授予跨正领圈使用严格负曲率能量界的权利。
