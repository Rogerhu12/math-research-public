# 从 R262 原非圆中央到真三圆弧接柱的同一材料坐标继续

这里证明输入在整个幅度区间的定义和 $C^2$ 连续性。实际新态的度量误差由求解回执分别报告。一次改变幅度会改变几何输入；固定同一 $g$ 的细化从选定最终态以后开始。

令 $A(q,\theta)$ 是原有限前缀的实际 $X+C+W$，$0\le q\le S$。原中央修正与原场的准确边条件给出
$$
A(0,\theta)=\Gamma_0(U_0(\theta)),\quad A_q(0,\theta)=e_z,\quad
 A_{qq}(0,\theta)=A_{q\theta}(0,\theta)=0.
$$
$U_0$ 是原 R262 的真等周长角。拟接的 $\Gamma_1$ 是 R309 的同周长三重中央，作 $\pi/3$ 的材料与空间对齐，使用低曲率 $1/4$ 或 $7/20$。两条曲线均以原点为三重中心，周长均为 $2\pi$，并取逆时针单位速。$P=2\pi/3$。

## 同时规定真实位置及其两阶导

取两条外法向角的连续提升 $\beta_j$，使 $\beta_j(0)=0$。每扇均有 $\beta_j(u+P)=\beta_j(u)+P$，反射使 $\beta_j(-u)=-\beta_j(u)$。定义
$$
\beta_\lambda=(1-\lambda)\beta_0+\lambda\beta_1,\qquad
T_\lambda=i e^{i\beta_\lambda},\quad N_\lambda=e^{i\beta_\lambda}.
$$
令 $\Gamma_\lambda' = T_\lambda$，取唯一满足 $\Gamma_\lambda(u+P)=e^{iP}\Gamma_\lambda(u)$ 的积分常数。它存在且唯一，因为 $e^{iP}-1\ne0$。三扇相加后总增量为零。单位速、真实全周长、反射和三重旋转对称均准确保持。曲率为 $\kappa_\lambda=(1-\lambda)\kappa_0+\lambda\kappa_1>0$，从而这些都是严格凸闭曲线。沿每个方向的支撑函数恰有一个极大点，由外法角严格增一整圈即得单射。

实现对差切向 $T_\lambda-T_0$ 积分，故 $\lambda=0$ 的零位移不会混入两个近似原函数之差。设 $I(t)=\int_0^t(T_\lambda-T_0)du$。首半扇的中心改变量是 $\cot(P/2)\operatorname{Im} I(P/2)-\operatorname{Re} I(P/2)$。将它加到 $I(t)$ 上，再作反射和扇区旋转，即得到 $\Gamma_\lambda-\Gamma_0$。在原生角中两阶导采用
$$
(\Gamma_\lambda\circ U_0)'=T_\lambda U_0',\qquad
(\Gamma_\lambda\circ U_0)''=-\kappa_\lambda N_\lambda(U_0')^2+T_\lambda U_0''.
$$
对应数值入口将半扇积分作原生变量变换，并在两真实过渡边界和所有查询端点细分；有限数值积分是上述连续函数的求值。$\lambda=1$ 直接调用圆弧段的真实闭式原函数和过渡段积分。仅最终态据 R309/R310 的确切圆弧窗口安装两支刚臂。

## 同一 $q$ 的整前缀与端口

记 $\Delta_\lambda=(\Gamma_\lambda-\Gamma_0)\circ U_0$，$c_\lambda=\lambda c$，$d_\lambda=\lambda d$，以及 $S_5(x)=10x^3-15x^4+6x^5$ 在 $x\le0$、$x\ge1$ 的常值延拓。取 $c+d<L<S$。对于 $\lambda>0$，设
$$
 C_\lambda=\Gamma_\lambda\circ U_0+q e_z,\quad
 Y_\lambda=A+\bigl[1-S_5(q/L)\bigr]\Delta_\lambda,\quad
 G_\lambda=S_5((q-c_\lambda)/d_\lambda).
$$
整个半核的前缀位置取 $P_\lambda=C_\lambda+G_\lambda(Y_\lambda-C_\lambda)$。在其上可加真实求解得到的 $V_\lambda$，采用 $(q-c_\lambda)/(S-c_\lambda)$ 的物理样条并在 $q\le c_\lambda$ 续零。去除两端各三项控制，准确保持完整两端的零二阶迹。非零 $V_\lambda$ 只有在其自己实际求得的幅度处使用。$q\ge S$ 这一整个无限尾继续使用同一个原始父场和其实际 $T_1$。两旧帽改为真圆领所围平盘。

置 $P_0=A$。为证明 $P_\lambda\to A$ 于 $C^2$，写
$$
 R(q,\theta)=A(q,\theta)-\Gamma_0(U_0(\theta))-q e_z .
$$
由上述中央迹及紧角圆上的连续二阶导，$R=o(q^2)$、$R_q=o(q)$、$R_{qq}=o(1)$、$R_\theta=o(q)$、$R_{q\theta},R_{\theta\theta}=o(1)$，余项对角一致。又有 $\|\Delta_\lambda\|_{C^2}=O(\lambda)$，因为两个连续提升及其曲率有界。缩小的过渡上 $q=O(\lambda)$，且
$$Y_\lambda-C_\lambda=R-S_5(q/L)\Delta_\lambda.$$
$G_\lambda$ 的一、二阶导分别为 $O(\lambda^{-1})$、$O(\lambda^{-2})$。逐项用乘积法则，所有零、一、二阶差均趋零，包括 $G_\lambda'' R=o(1)$ 及 $G_\lambda' R_\theta=o(1)$。中央真柱区用同一 $R$ 界；过渡之外仅余固定 $C^2$ 截止乘 $\Delta_\lambda$。因此该规定确是一条以整个原始 $A$ 为起点的连续 $C^2$ 输入路径。它没有对尚未求出的各幅度笛卡尔修正作连续性假设。

每个相位仍按真实材料角作 $R_\eta P(q,U_0^{-1}(u-\eta))$。对该幅度选定的正径向目标，全角相对 Gram 谱误差对所有相位的上确界等于参考相位的全角上确界。最后固定 $g$ 后须以同一 $g$ 真正增加径角位置自由度，并分别检验连续误差、整闭几何及形状比例。