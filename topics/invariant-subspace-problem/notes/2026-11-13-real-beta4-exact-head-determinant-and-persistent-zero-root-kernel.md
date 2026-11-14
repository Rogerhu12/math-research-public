# 实 β=4 剪切的准确二维头行列式及保留零根

日期：2026-11-13（UTC）。kernel_resume_1cf / Astra-ISP-1cf8c51d；根独审头矩阵、规范深域与自然平方的首商，并补明尾空谱前提。
性质：开放接口的完整归约和范围审计，不是新的循环性结论。

## 1. 设置和两个条件符号

为简洁令最低主位为0，$a_0=\alpha\ne0$、$c_0=\gamma$。
写
$$
u=\alpha\chi_0+u_t,\qquad
v=\gamma\chi_0+v_t,\qquad
w=b_0\chi_0+w_t,\qquad \tau=e^{-2b_0}.
$$
常数项可留在尾模式内。考虑
$$
F(u,v)=(v-u^2)^2-4\alpha^2u^2-\lambda.
$$
两个真实条件符号为
$$
F_\pm(x,y)
=\bigl[y\pm\gamma-(x\pm\alpha)^2\bigr]^2
-4\alpha^2(x\pm\alpha)^2-\lambda.
\tag{1.1}
$$
令 $P_\pm$ 为尾 first、尾指数 $w_t$ 下
$F_\pm(u_t,v_t)e^{w_t}$ 的完整 Bell 多项式，
始终保全部交叉系数。

把 $\chi_0^2=1$ 作点态有限归约后，
原规范最大实现是
$$
T=A+R_0(b_0)B,\qquad
A=(P_++P_-)/2,\quad B=(P_+-P_-)/2.
\tag{1.2}
$$
这里等式指 R186 的共同自然核心取闭包；
尾模式与头因子支持分离，
且循环指数向量给同一真实图核心。
不把两个点态条件多项式当成未经 Bell 修正的自然式。

## 2. 真实 2×2 矩阵和自然行列式

在首个物理位的二维头基下，
$$
N_0=
\begin{pmatrix}
0&\eta_0N_1\\ I&0
\end{pmatrix},
\qquad
R_0(b_0)=(I-\tau N_0)(I+\tau N_0)^{-1}.
\tag{2.1}
$$
$I+\tau N_0$ 是原 $A'$ 的有界单位，
所以保持全部相关闭图、且不改变核。
在共同深域上，
$$
\boxed{
(I+\tau N_0)T
=P_+I+\tau P_-N_0
=
\begin{pmatrix}
P_+&\tau\eta_0N_1P_-\\
\tau P_-&P_+
\end{pmatrix}.
}
\tag{2.2}
$$
各尾条目在该共同域上交换。
伴随矩阵相乘准确给
$$
\boxed{
D=P_+^2-KP_-^2,\qquad K=\tau^2\eta_0N_1.
}
\tag{2.3}
$$
平方是自然算子乘积，随后取 R186 规范最大闭包。
一般不能换成 $F_\pm^2$ 的点态 Bell 实现。

### 2.1 核归约包含全部实际域

选择只作用尾的 R186 共同正则器 $R_t(s)$。
它是原 $A'$ 的有界算子、保持 $\ker T$，
并强趋于 $I$；其固定深幂使所有 $P_\pm$、
自然平方及伴随矩阵中间词合法。

若 $f=(f_0,f_1)\in\ker T$，
先对 $R_t(s)^Nf$ 使用 (2.2)–(2.3)，再取 $s\downarrow0$。
$\ker D_{\max}$ 闭，因此
$$
f_0,f_1\in\ker D_{\max}.
\tag{2.4}
$$
故 $D_{\max}$ 单射足以推出原 $T$ 单射。

反过来，假设 $P_+$ 的完整尾实现单射。
若 $0\ne z\in\ker D_{\max}$，
用单射 $R_t(s)^N$ 取得非零深域 $z_s$。
则
$$
\begin{pmatrix}P_+z_s\\-\tau P_-z_s\end{pmatrix}
$$
非零，并由伴随矩阵恒等式落在 (2.2) 的核内。
因此在这个已知条件下，
$$
\boxed{\ker T\ne0\quad\Longleftrightarrow\quad\ker D_{\max}\ne0.}
\tag{2.5}
$$
这不是把尾投影未经证明地当作闭图同构。

## 3. 尾空谱前提下，两个单条件向量的已闭互素范围

本节额外假设尾 first $X_{u_t}$ 具有空谱。
当前正非 $\ell^1$ 主行在删除首位后仍满足此条件；
一般主行不能仅凭 $a_0\ne0$ 或 $a_1\ne0$ 自动使用本节。
第2节的矩阵归约本身不要求这个空谱前提。

令 $z=y-x^2$。
(1.1) 在剪切权 $\operatorname{wt}x=\operatorname{wt}z=1$
的二次边为
$$
H_\pm(Z)=Z^2\mp4\alpha Z=Z(Z\mp4\alpha).
\tag{3.1}
$$
若尾的首主系数为 $\beta=a_1\ne0$，
且尾主首位不晚于尾辅助首位，
已发表剪切定理的平移量为 $4\beta$。
因此 $\beta\ne\pm\alpha$ 足以使两个单条件点态向量分别循环
（任意 $\lambda$ 和复 $w_t$ 均允许）。

这并不使原两个头 atom 的和自动循环。
准确整体算子仍是 (2.2)，其核须由 (2.3) 处理。

## 4. 第一个真实尾字符仍留下共同零根

记尾的真实倾斜二阶 Bell 系数为
$$
B_{20,t}=\sum_{j\ge1}a_j^2(I-R_j(b_j)^2).
$$
在 $x=t^{-1},y=t^{-2}+t^{-1}Z$ 的剪切归一中，
完整 Bell 多项式 $P_\pm$ 的实际二次领先项为
$$
\mathscr P_\pm(Z)=Z^2\mp4\alpha Z+4B_{20,t}.
\tag{4.1}
$$
该式来自全部混合 Bell：
$x$ 导数在该标度下领先为 $-2\partial_Z$，
正 $y$ 导数及含 $y$ 的混合导数严格降阶。
故 (2.3) 的领先实际多项式是
$$
\mathscr D(Z)=\mathscr P_+(Z)^2-K\mathscr P_-(Z)^2.
\tag{4.2}
$$
其尾字符为
$$
\chi_t(\mathscr D)=H_+^2
$$
而不是 $H_+H_-$。

取尾 gauge $\Gamma_\zeta(N_1)=\zeta N_1$，
令 $\beta=a_1\ne0$、$\tau_1=e^{-2b_1}$。
对 $\zeta\ne1$，
$$
\kappa_t=\tau_1(\zeta-1),\qquad
k_\zeta=\tau^2\eta_0(\zeta-1)\ne0.
$$
由[完整低权剪切证明](../results/R150-appendix-nonlinear-scalar-shears-degenerate-newton-edges-and-point-powers.md)的真实首位商计算，单条件首位商字符为
$$
q_+(Z)=
\kappa_t[H_+(Z+4\beta)-H_+(Z)].
$$
实际自然平方的第一商字符是乘积求导式，
因而 (4.2) 的第一真实商给
$$
\boxed{
\chi_t\!\left(
\frac{\mathscr D_\zeta-\mathscr D}{N_1}
\right)
=
2H_+(Z)q_+(Z)-k_\zeta H_-(Z)^2.
}
\tag{4.3}
$$
分母先由真实余数除法得到；式中还包括归一变量的实际 first 平移。

在 $H_+=0$ 的两个根：

- $Z=4\alpha$ 时，$H_-(4\alpha)=32\alpha^2\ne0$，
  第二项不为零；
- $Z=0$ 时，$H_-(0)=0$，两项都严格为零。

因此
$$
\boxed{Z=0\text{ 是尚未消去的真实共同字符根}.}
\tag{4.4}
$$
若 $\beta\ne\alpha$，
$q_+(0)=16\kappa_t\beta(\beta-\alpha)\ne0$，
(4.3) 在0的一次系数非零；
但 $\chi_t(\mathscr D)=H_+^2$ 在0仍有重根，
尚不足以得到最高系数单位。

## 5. 两个必须保留的限制

第一，不能把
$$
\Gamma(P_+^2)-P_+^2
$$
的首商字符误写成
$\kappa_t[H_+(Z+4\beta)^2-H_+(Z)^2]$。
真实自然平方的首商是 $2H_+q_+$；
前者属于另一个点态四次符号的 Bell 变换。
换错后会把 (4.4) 的共同零根错误删除。

第二，形式上 $B_{20,t}$ 的最低阶是一个尾步长，
不等于它可被 $N_1$ 作实际有界除法。
高阶头行列式／高阶字符若需要这样的除法，必须重新支付；
R124 只保证实际 gauge 差的余数商。
同理，单条件 $P_\pm$ 在全尾空间单射稠密，
不等于它们在未知 $\ker D_{\max}$ 上有有界逆或稠密像。

[R236 自动好集稿](../results/R236-appendix-nonsummable-main-good-sets-and-simple-character-fibers.md)关闭任意非可和主行的普通简单字符纤维，
但 (2.3) 是两个独立无界模式的自然行列式，
而 (4.4) 又是重数根；不能据此删除。

下一条真实问题是对 $D_{\max}$ 的这个剩余零根排核，
或证明它需要的具体慢尾限制像。
本记录只固定准确矩阵、自然域与残留根，不宣称这一问题已完成。
