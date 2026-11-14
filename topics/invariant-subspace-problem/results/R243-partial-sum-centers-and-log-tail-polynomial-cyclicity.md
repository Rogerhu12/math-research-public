# R243：部分和中心、对数慢尾共振及非漂移全多项式循环

日期：2026-11-12（UTC）。作者：kernel。状态：已证明。承接有限头真实进位幂界；对一般有界分支只推出部分和聚点属于其谱，不把它升级为一般单点谱结论。

## 1. 使用的准确输入

令
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,\qquad X=X_u,
$$
并定义
$$
s_m=a_*+\sum_{j<m}a_j,\quad
B_m=\sum_{j<m}|a_j|,\quad
g_m=\|a_{\ge m}\|_2,\quad
A_m=\max(1,6B_m),\quad
\ell_m=1+\log A_m.
\tag{1.1}
$$
$Q_m$ 是全部前 $m$ 位柱函数的正交投影，$Q_m\to I$ 强。

[R241](R241-carry-head-powers-and-drifting-first-polynomial-cyclicity.md)证明了真实分解
$$
X-s_mI=H_m+Z_m,\qquad
H_m=\sum_{j<m}a_j(V_j-I),
\tag{1.2}
$$
以及以下三个输入：

- 当 $k\ge\max(2m,16)$ 时，
  $$
  \|H_m^k\|\le(6B_m)^k e^{-\gamma k^4},
  \qquad \gamma=770/16^4;
  \tag{1.3}
  $$
  对全部 $k\ge0$ 仍有 $\|H_m^k\|\le A_m^k$。
- $H_m$ 与真实闭尾 $Z_m$ 的全部自然幂域交换，$\operatorname{Dom}(X-s_mI)^p=\operatorname{Dom}Z_m^p$，二项式在该域成立。
- R207 附录 A–B 给固定模型常数 $C<\infty$，使
  $$
  \operatorname{Ran}Q_m\subseteq\bigcap_{r\ge1}\operatorname{Dom}Z_m^r,
  \qquad
  \|Z_m^rQ_m\|\le(Cg_m\sqrt r)^r.
  \tag{1.4}
  $$

特别，(1.4) 是尾真空在指数次数权空间中逐次作用真实闭算子得到的自然幂界；它在整个低头空间上一致，未付 $2^m$ 的维数成本。

共同共轭 $C$ 保持 $Q_mH$，且 $X^*=CXC$。所以任何由 (1.2)–(1.4) 得到的具体 $Q_m$ 自然幂界，可以在对应共轭域上同样用于 $X^*$。

## 2. 可调幂次数的实际范数估计

对 $m\ge8$，置
$$
\delta_m=A_m e^{-\gamma(2m)^3}.
\tag{2.1}
$$
由 (1.3)，$k\ge2m$ 时 $\|H_m^k\|\le\delta_m^k$。由于 $B_m\le\|a\|_2\sqrt m$，有 $\delta_m\to0$。

任取整数 $p\ge4m$，记
$$
D=Cg_m\sqrt p,\qquad \theta=2m/p\le1/2.
$$
先假设 $0<D\le1$。自然二项式和 (1.4) 给
$$
\|(X-s_mI)^pQ_m\|
\le\sum_{k=0}^p\binom pk\|H_m^k\|D^{p-k}.
\tag{2.2}
$$
对 $k\ge2m$，其和不超过 $(\delta_m+D)^p$。对 $k<2m$，使用 $A_m\ge1$、$D\le1$，得到
$$
A_m^kD^{p-k}\le A_m^{2m}D^{p-2m}.
$$
令
$$
h(t)=-t\log t-(1-t)\log(1-t),\qquad h(0)=0.
$$
标准有限二项式估计
$$
\binom pk\le e^{p h(k/p)}\le e^{p h(\theta)}
\qquad(0\le k<2m)
$$
可直接由
$1=(t+(1-t))^p\ge\binom pk t^k(1-t)^{p-k}$
取 $t=k/p$ 得到，端点 $k=0$ 单独取 1。因此前半部分至多
$$
(2m)e^{p h(\theta)}A_m^{2m}D^{p-2m}.
$$
取 $p$ 次根并对两块使用三角上界，得到
$$
\boxed{
\|(X-s_mI)^pQ_m\|^{1/p}
\le
(2m)^{1/p}e^{h(\theta)}A_m^\theta D^{1-\theta}
+\delta_m+D.
}
\tag{2.3}
$$
由具体自然域共轭，同一个右端也控制
$\|(X^*-\overline{s_m}I)^pQ_m\|^{1/p}$。

若 $D=0$，则尾为零，且 $p\ge4m$ 已在 (1.3) 的范围内，直接有根界不超过 $\delta_m$。下面的无限支撑情形始终 $g_m>0$。

## 3. 使整个根界趋零的尺度条件

假设在一个趋无穷序列 $m=m_\nu$ 上，
$$
m g_m^2\ell_m\longrightarrow0.
\tag{3.1}
$$
这里只要求该序列，不要求其余指标也满足条件。设 $a$ 有无限支撑，令
$$
t_m=mg_m^2>0,\qquad
L_m=\sqrt{\ell_m/t_m},\qquad
p_m=\lceil mL_m\rceil.
\tag{3.2}
$$
由 (3.1) 和 $\ell_m\ge1$，
$$
L_m\to\infty,\qquad
\frac{\ell_m}{L_m}=\sqrt{t_m\ell_m}\to0,\qquad
t_mL_m=\sqrt{t_m\ell_m}\to0.
\tag{3.3}
$$
故充分大时 $p_m\ge4m$。记
$$
D_m=Cg_m\sqrt{p_m},\qquad \theta_m=2m/p_m.
$$
则
$$
D_m^2
\le C^2(t_mL_m+g_m^2)\longrightarrow0,
\tag{3.4}
$$
并且
$$
\theta_m\to0,\qquad
\theta_m\log A_m
\le2\ell_m/L_m\longrightarrow0.
\tag{3.5}
$$
还因 $p_m\ge4m$，
$$
\frac{\log(2m)}{p_m}\to0,\qquad h(\theta_m)\to0.
$$
所以 (2.3) 中 $D_m^{1-\theta_m}\to0$，其余乘因子趋于 1，且 $\delta_m+D_m\to0$。于是存在明确的 $\varepsilon_m\to0$，使
$$
\boxed{
\|(X^*-\overline{s_m}I)^{p_m}Q_m\|
\le\varepsilon_m^{p_m},
\qquad p_m\to\infty.
}
\tag{3.6}
$$
$\varepsilon_m$ 就是 (2.3) 的右端，不隐藏任何对未知不变空间的依赖。

条件 (3.1) 可等价地使用
$$
m g_m^2\bigl(1+\log(1+B_m)\bigr)\to0,
\tag{3.7}
$$
因为 $\ell_m$ 与括号中的正量互相以固定常数控制。

若 $a$ 只有有限支撑，则 $X=sI+H$，其中 $s=a_*+\sum a_j$，$H$ 是有限解析零常数头，故有界拟幂零。下面关于聚点 $s$ 的结论也直接成立；所有新例均为无限支撑。

## 4. 同一未知闭空间上的谱位置约束

设 $M\ne0$ 为闭空间，满足
$$
M\subseteq\operatorname{Dom}X,\qquad XM\subseteq M.
\tag{4.1}
$$
闭图定理给 $Y=X|_M\in B(M)$。不另行要求 $AM\subseteq M$。

前稿的通常伴随域恒等式为
$$
P_MX^*=Y^*P_M
\qquad\text{在 }\operatorname{Dom}X^*\text{ 上}.
\tag{4.2}
$$
在 (3.6) 的具体自然幂域中迭代。如果 $s_m\in\rho(Y)$，则
$$
\|P_MQ_m\|
\le\left(\|(Y-s_mI)^{-1}\|\varepsilon_m\right)^{p_m}.
\tag{4.3}
$$

现在另假设沿 (3.1) 的同一序列，
$$
s_m\longrightarrow s\in\mathbb C.
\tag{4.4}
$$
若 $s\in\rho(Y)$，则预解集的开放性和预解恒等式保证对充分大 $m$，
$s_m\in\rho(Y)$ 且 $\|(Y-s_mI)^{-1}\|\le R$，其中 $R<\infty$ 固定。由于 $\varepsilon_m\to0$，(4.3) 给 $\|P_MQ_m\|\to0$，而 $Q_m\to I$ 强，矛盾于 $M\ne0$。故
$$
\boxed{s\in\sigma(Y).}
\tag{4.5}
$$

这一论证在 $s\in\sigma(Y)$ 时不能再取逆；因此没有由 (4.5) 对一般有界 $Y$ 宣称 $\sigma(Y)=\{s\}$。

### 4.1 有限谱分支的加强

如果另知 $\sigma(Y)$ 有限，那么确有
$$
\boxed{\sigma(Y)=\{s\}.}
\tag{4.6}
$$
证明如下。对任意 $\lambda\in\sigma(Y)$，其 Riesz 谱投影给非零闭空间 $M_\lambda\subseteq M$，满足
$$
YM_\lambda\subseteq M_\lambda,\qquad
\sigma(Y|_{M_\lambda})=\{\lambda\}.
$$
因为 $M_\lambda\subseteq M\subseteq\operatorname{Dom}X$ 且 $X=Y$ 在 $M$ 上成立，$M_\lambda$ 本身满足 (4.1)。将 (4.5) 作用于这个实际闭空间，得到 $s=\lambda$。每个谱点都如此，遂得 (4.6)。

如果存在两个不同的有限聚点 $s\ne t$，各自沿满足 (3.1) 的序列取得，那么不存在任何非零的有限谱有界 $X$ 限制。因为同一个有限谱分支分别被 (4.6) 迫成 $\{s\}$ 和 $\{t\}$。

## 5. Bell 多项式和任意指数权的正结论

设 $P(X)$ 是最高系数可逆的 $\mathcal A$ 系数自然多项式，字符多项式为
$$
q_0(z)=\sum_k\chi(E_k)z^k.
$$
R176 §§2、3、8 已完整证明：若其核 $M\ne0$，则 $M$ 闭且 $A$ 不变，
$$
M\subseteq\operatorname{Dom}X,\qquad
XM\subseteq M,\qquad
Y=X|_M\in B(M),\qquad
\sigma(Y)\subseteq q_0^{-1}(\{0\}).
\tag{5.1}
$$
最后集合有限。

若有满足 (3.1)、(4.4) 的 $s$ 且 $q_0(s)\ne0$，(4.5) 与 (5.1) 矛盾。所以 $P(X)$ 单射；其完整 $C$ 自伴性给像稠密。

对真正点态多项式 $q(u)$，R176 的 Bell 实现 $P_q(X)$ 满足 $q_0=q$、$P_q(X)1=q(u)$，而常向量产生其真实图核心。因此
$$
\boxed{q(s)\ne0\quad\Longrightarrow\quad q(u)\text{ 循环}.}
\tag{5.2}
$$

同样，对任意
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2,
$$
R176 §10 的加权闭 Bell 实现若有非零核，其上原 $X$ 有界且谱仍包含于 $q$ 的有限零集（该文 (10.16)）。因而
$$
\boxed{q(s)\ne0\quad\Longrightarrow\quad q(u)e^w\text{ 循环}.}
\tag{5.3}
$$
这里保留真实倾斜有界交换扰动与 Bell 系数，没有把点态乘积写作无修正的自然算子幂。

若部分和有两个不同的、分别满足 (3.1) 的有限聚点，则由 §4.1 根本不存在有限谱有界分支，故上述结论不再需要 $q(s)\ne0$：
$$
\boxed{\text{每个非零 }q(u)e^w\text{ 都循环}.}
\tag{5.4}
$$

## 6. 等振幅对数修正交替行：真实危险平方为零核

固定
$$
0<\alpha\le1,\qquad
a_j=\frac{(-1)^j(\log2)^\alpha}
{(j+1)(\log(j+2))^\alpha},\qquad a_*=0.
\tag{6.1}
$$
则 $a_0=1$，$|a_j|$ 严格递减至零，且
$$
a\in\ell^2\setminus\ell^1.
$$
正、负子列的绝对和都发散。交错级数给
$$
s_m\longrightarrow s_\alpha,\qquad
0<s_\alpha<1.
\tag{6.2}
$$
严格上下界可直接由正项两两配对及首项余项符号得到。

积分比较给
$$
g_m^2=O\!\left(\frac1{m(\log m)^{2\alpha}}\right),
\tag{6.3}
$$
并且
$$
B_m=
\begin{cases}
O((\log m)^{1-\alpha}),&0<\alpha<1,\\
O(\log\log m),&\alpha=1.
\end{cases}
\tag{6.4}
$$
例如 (6.3) 可将 $j\ge m$ 分成二进制区间，使用区间内对数下界和
$\sum_{j\ge m}(j+1)^{-2}=O(m^{-1})$；(6.4) 是函数
$1/(x(\log x)^\alpha)$ 的初等积分。由此
$$
m g_m^2(1+\log(1+B_m))\longrightarrow0.
\tag{6.5}
$$
所以 §§3–5 适用。

对原来首位平移碰撞的危险平方
$$
q(z)=z^2-1
$$
有 $q(s_\alpha)\ne0$。因此
$$
\boxed{u^2-1\text{ 对 }A\text{ 循环},}
\tag{6.6}
$$
并且对每个第一阶复 $\ell^2$ 指数权，
$$
\boxed{(u^2-1)e^w\text{ 对 }A\text{ 循环}.}
\tag{6.7}
$$
等价地，实际自然 Bell 算子
$$
X^2+B_2-I,\qquad
B_2=\sum_j a_j^2(I-V_j^2),
$$
在准确域 $\operatorname{Dom}X^2$ 上的核为零。

这里显式使用 $a_*=0$。所以若另写成 R144 平方附录中的
$\ker(X-Y)$、$Y=(I-B_2)^{1/2}$，确实是同一个原危险点态平方分支；并未把一般 $a_*$ 的独立有界分支恒等式冒称为相同危险平方。

这些行的正、负尾各自不可和，R138 给其 first 全平面连续谱。因此 (6.6) 并非空谱相位类的旧结论。

当 $\alpha=0$ 时，退回规范交替调和行，此时 $mg_m^2$ 不趋零，(3.1) 失败。本稿不由 $\alpha>0$ 的结果取无控制极限来关闭 $\alpha=0$。

## 7. 有界非收敛部分和的全平面谱新类

下面给一个完全具体、无漂移到无穷的全多项式实例。置
$$
b_j=\frac{\log2}{(j+1)\log(j+2)}>0,\qquad b_0=1.
\tag{7.1}
$$
则 $b\in\ell^2\setminus\ell^1$、$b_j\downarrow0$，且其 $B_m,g_m$ 满足 (6.5) 的 $\alpha=1$ 版本。

从 $s_0=0$ 开始，以如下递归确定 $\varepsilon_j\in\{1,-1\}$ 和 $a_j=\varepsilon_jb_j$：

- 使用正号，直到部分和首次达到或超过 1；
- 然后使用负号，直到部分和首次达到或低于 0；
- 重复上述两步。

因为每个剩余尾的 $\sum b_j$ 都发散，每个区块都在有限指标结束；如此得到整行无穷序列。各终点的越界量不超过最后一步 $b_j$，所以趋零。部分和始终有界，并具有子序列分别趋于 0 和 1。

事实上每个 $t\in[0,1]$ 都是聚点：在趋向高位的每个上升区块中，取首次跨过 $t$ 的部分和，其误差至多该区块的最大 $b_j$，后者趋零。

每个完整上升或下降区块的绝对质量趋于 1，因此正号、负号系数的绝对和都发散。由 R138，
$$
\sigma(X)=\mathbb C
$$
且全为连续谱。

因为 $|a_j|=b_j$，尺度条件 (3.1) 在整条指标序列上成立。部分和的两个不同聚点已足够使用 (5.4)，得到
$$
\boxed{
q\!\left(\sum_j a_j\chi_j\right)e^w
\text{ 对 }A\text{ 循环}
}
\tag{7.2}
$$
对每个非零标量多项式 $q$ 及每个第一阶复 $\ell^2$ 指数权 $w$ 成立。

也可不使用 Riesz 加强：$q$ 只有有限个根，从 $[0,1]$ 中选一个 $t$ 使 $q(t)\ne0$，再直接使用 (5.3)。两种推导都在原 Haar 空间和同一个实际核上进行。

## 8. 未解决范围

本稿完成了收敛中心的全柱根界，以及两种明确的正向应用：

- 等振幅对数修正交替行的危险平方和全部 $q(s_\alpha)\ne0$ 点态多项式，允许任意第一阶指数权；
- 符号分块、部分和有两个不同聚点的具体非漂移全平面谱行，其全部单模式点态多项式和第一阶指数权。

仍未证明规范交替调和行的危险平方核为零，也未证明任意复 $\ell^2$ first 在全部闭不变限制中像稠密。一般有界分支的谱可能不是有限集，§4 的必要谱位置条件不能自行把它缩成一个点。

