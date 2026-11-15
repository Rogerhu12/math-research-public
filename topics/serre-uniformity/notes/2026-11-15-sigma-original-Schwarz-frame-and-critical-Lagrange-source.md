# 原 Cayley 参数的 Picard--Fuchs 标架与临界 Lagrange 留数

日期：2026-11-15。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：下列参数、系数与有限范围内的模 $p$ 留数恒等式已证明；指定系数非零及原 primitive / Legendre 三因子仍开放。**
本文接续 [XF 原全六层函数](2026-11-15-sigma-original-X6-weight-one-and-logarithmic-square.md) 与
[KS 原平方卷积](2026-11-15-sigma-Kronecker-weight-one-square-and-critical-convolution.md)。
没有将固定 Picard--Fuchs 方程误当成原逆 Schwarz 参数下的固定阶标量递推，
也没有运行新素数算术。

## 1. 原标架给出的实际 Picard--Fuchs 方程

保持 XF 的 period-one 权一函数 $\mu,\rho$、全三层参数 $U=\mu/\rho$、
Fermat 坐标 $\mathsf x,\mathsf y$ 与原 CM 点
$$
U=0,\quad \mathsf x=0,\quad\mathsf y=2/\alpha,\qquad
\rho_0:=\rho(\tau_0)=2\Omega\beta/\alpha,\quad
\rho_0^2=3\alpha\Omega^2.
$$
令
$$
D_0=1-8U^3,\qquad
\widehat\rho=\rho/(2\pi i),\quad \widehat\mu=\mu/(2\pi i).
$$
XF 已在原规范证明
$$
\partial_1\widehat\mu
=\frac{\widehat\rho^3-2\widehat\mu^3}{6},\qquad
\partial_1\widehat\rho=\widehat\mu^2\widehat\rho,\qquad
\theta_qU=\frac{\widehat\rho^2D_0}{6},
\tag{PL1}
$$
其中 $\partial_k=\theta_q-kE_2/12$。

为直接导出而非仅命名 Picard--Fuchs，置
$\kappa=E_2/\widehat\rho^2$、$L=\rho'/\rho$，本篇 prime 表示 $d/dU$。
由 (PL1)、Ramanujan 方程及
$E_4=16\widehat\mu(\widehat\rho^3+\widehat\mu^3)$，
$$
L=\frac{6U^2+\kappa/2}{D_0},\qquad
\kappa'=\frac{-\kappa^2/2-12U^2\kappa-8U(1+U^3)}{D_0}.
$$
将 $\kappa=2D_0L-12U^2$ 代回，恰得
$$
\boxed{D_0\rho''-24U^2\rho'-8U\rho=0.}
\tag{PL2}
$$
此外 (PL1) 保留 period-one 因子给
$$
\frac{d\tau}{dU}=\frac{12\pi i}{\rho^2D_0}.
\tag{PL3}
$$
因此 $\tau\rho$ 也是 (PL2) 的解：两者 Wronskian 是常数乘 $D_0^{-1}$，
由标准 reduction of order，或直接代入即可核对。这里没有将原
物理微分 $dz$ 与 $\tau$ 方向混为同一导子。

## 2. 正确的两个局部解与原 Cayley 尺度

定义 (PL2) 的归一解
$$
\mathsf C(U)
={}_2F_1\left(\frac13,\frac13;\frac23;8U^3\right),
$$
$$
\mathsf A(U)
=U\,{}_2F_1\left(\frac23,\frac23;\frac43;8U^3\right).
\tag{PL4}
$$
它们的初值分别是
$$
\mathsf C(0)=1,\quad\mathsf C'(0)=0,\qquad
\mathsf A(0)=0,\quad\mathsf A'(0)=1.
$$
把幂级数代入 (PL2) 逐项比较即得 (PL4)，所以此处超几何函数的
规范由实际初值决定。$\mathsf A,\mathsf C$ 不是在此处另选的原
R812 Hasse 常数或 sigma 系数 $C_k$。

令 $v_0=\tau_0-\overline{\tau_0}=2i\Im\tau_0$。
在原 CM 点 $E_2^*(\tau_0)=0$。由 (PL1)、(PL3) 核对初值，
于是实际两个解恰为
$$
\mathsf C(U)
=\frac{\tau-\overline{\tau_0}}{v_0}\,
                       \frac{\rho(\tau)}{\rho_0},
\qquad
\mathsf A(U)
=\frac{\rho_0^2}{12\pi i}(\tau-\tau_0)
                       \frac{\rho(\tau)}{\rho_0}.
\tag{PL5}
$$
例如第一式的导数为零：$\rho'/\rho$ 的 CM 值是
$-6\pi/(\rho_0^2\Im\tau_0)$，而 (PL3) 对前一因子的导数恰给其相反数。
第二式的导数由 (PL3) 为一。

原 Cayley 参数与 KS 的有理系数参数为
$$
u=\frac{\tau-\tau_0}{\tau-\overline{\tau_0}},\qquad
t=-\frac{\mathcal A}{3}u,\qquad
\mathcal A=\frac{\Omega^2\Im\tau_0}{\pi}.
$$
式 (PL5) 和 $\rho_0^2=3\alpha\Omega^2$ 准确给
$$
\boxed{t=c\,\frac{\mathsf A(U)}{\mathsf C(U)},\qquad
             c=-\frac{2}{3\alpha}.}
\tag{PL6}
$$
两边都是原归一，没有把 $\Omega$ 隐藏成额外的单位选择。

设
$$
\mathscr K(t)=\sum_{m\ge0}C_{m+1}t^m,
$$
其中 $C_{m+1}$ 是 KS / R683 的原十八项，非允许类按零延拓。
由 XF 的 $E=6\rho\mathsf x$ 与 KS 的完整 Cayley 展开，
$$
\boxed{\mathscr K(t)=b\,\mathsf C(U)\mathsf x(U),\qquad b=\alpha/12.}
\tag{PL7}
$$
这里的 $\mathsf x(U)$ 是原 CM 支：
$$
\mathsf x^3=1-\sqrt{1-8U^3},\qquad
\mathsf x=\alpha U+O(U^4),
\quad
\mathsf y=\frac{2U}{\mathsf x}.
\tag{PL8}
$$
特别 (PL6)--(PL8) 的首系数是
$b\alpha/c=-1/2=C_2$，与旧结论一致。

## 3. 不丢标架的完整特征零留数

由 (PL2) 和初值，
$$
\boxed{\mathsf A'\mathsf C-\mathsf A\mathsf C'=D_0^{-1},\qquad
d(\mathsf A/\mathsf C)=\frac{dU}{D_0\mathsf C^2}.}
\tag{PL9}
$$
令
$$
S_n=\sum_{m=0}^nC_{m+1}C_{n-m+1}=[t^n]\mathscr K(t)^2.
$$
合法形式换元 (PL6) 的首项为单位。把 (PL7) 与 (PL9) 代入
$[t^n]\mathscr K^2=\operatorname{Res}_{t=0}\mathscr K^2t^{-n-1}dt$：
$$
\boxed{
S_n=b^2c^{-n}\operatorname{Res}_{U=0}
 \frac{\mathsf x^2\mathsf C^{\,n+1}}
      {D_0\mathsf A^{\,n+1}}\,dU .
}
\tag{PL10}
$$
所有 $\mathsf C^2$ 的约去都写在 (PL9) 中；
剩下的 $\mathsf C^{n+1}$ 是原标架，不能再任意删除。
这是对全部 $n\ge0$ 的有理系数恒等式。

## 4. 首 $p$ 范围、首次分母及小素数边界

以下只取原范围
$$
p=6N+5\ge41,\qquad r=(p-2)/3.
$$
在 $\mathbf Q(\alpha)$ 选择原素点，$\alpha$ 约化为
$\mathbf F_p$ 中唯一的 $4$ 的立方根。

(PL4) 的显式系数分别是
$$
\mathsf C
=\sum_{j\ge0}8^j\frac{(1/3)_j^2}{(2/3)_j\,j!}U^{3j},
\qquad
\mathsf A
=U\sum_{j\ge0}8^j\frac{(2/3)_j^2}{(4/3)_j\,j!}U^{3j}.
\tag{PL11}
$$
当 $0\le j\le r$ 时，上述所有分母均为 $p$ 单位，
所有非零分子因子也避开 $p$。因此：

- $\mathsf C$ 至 $U^{p-1}$ 的截断是 $p$ 整，最后可能出现的次数是 $p-2$；
- $\mathsf A$ 至 $U^{p-1}$ 的截断是 $p$ 整，最高项 $U^{p-1}$ 的系数是单位；
- $\mathsf a:=\mathsf A/U$ 和 $\mathsf C$ 在此范围均首项一。

这里没有把两个完整超几何级数都说成 $p$ 整。
在 $j=r+1=(p+1)/3$，$\mathsf C$ 的分母出现唯一的因子 $p$，
其分子与 $j!$ 均不含 $p$，所以
$$
v_p([U^{p+1}]\mathsf C)=-1.
\tag{PL12}
$$
同一 $j$ 的 $\mathsf A$ 分子含 $p^2$，分母为单位，
故该 $U^{p+2}$ 系数有 valuation $2$。
直接代回 (PL2) 还可核对：$\mathsf A$ 的上述首 $p$ 截断在
$\mathbf F_p[U]$ 中就是一个次数 $p-1$ 的多项式解。
本篇不把它无标量地认作其他文章所用的 Hasse 归一。

原 Fermat 支 (PL8) 在 $p\ne2,3$ 是 etale 局部参数：
$\mathsf y(0)=2/\alpha$ 是单位，$dU/d\mathsf x=\mathsf y(0)/2$ 也是单位。
所以 $\mathsf x(U)$ 的局部级数 $p$ 整，不引入新坏素数。
本篇的 $n=p-6$ 需要 $p>6$；所有实际 $p\ge41$ 满足。
常数仅含 $2,3,\alpha$，故本篇没有在原允许范围内删除额外素数。
不对 $p=5$ 的负指标 $p-6$ 作任何形式外推。

## 5. 精确的五次分母 Cartier 源

在 (PL10) 取 $n=p-6$，并写 $\mathsf A=U\mathsf a$：
$$
\frac{\mathsf x^2\mathsf C^{p-5}}
     {D_0\mathsf A^{p-5}}
=
U^{-p}
\frac{\mathsf x^2\mathsf A^5}{D_0\mathsf C^5}
 \left(\frac{\mathsf C}{\mathsf a}\right)^p.
\tag{PL13}
$$
为了取留数，只需 $U^{p-1}$ 以内的数据。
所以先按 §4 把各因子截断到合法的 $p$ 整范围，再约化；
此时 Frobenius 确实给
$$
\left(\overline{\mathsf C}/\overline{\mathsf a}\right)^p
=1+O(U^p).
$$
右边未乘这个因子的部分
$\mathsf x^2\mathsf A^5/(D_0\mathsf C^5)$ 的阶至少七，
因此 $O(U^p)$ 不可能贡献所取系数。
这一步只用了有限截断，不使用 (PL12) 以后的非整完整级数。

又因 $b,c\in\mathbf F_p^\times$，
$$
b^2c^{-(p-6)}=b^2c^5
=-\frac{2}{3^7\alpha^3}
=-\frac1{2\cdot3^7}=-\frac1{4374}.
$$
因此 (PL10) 严格化为
$$
\boxed{
S_{p-6}
=-\frac1{4374}\,[U^{p-1}]
 \frac{\mathsf x^2\mathsf A^5}
      {(1-8U^3)\mathsf C^5}
 \pmod p.
}
\tag{PL14}
$$
这里 **$\mathsf C^{-5}$ 仍然存在**。只有 (PL13) 明列的 $p$ 次幂
可以在这个有限系数范围移出；不能借此把 $\mathsf C^{-5}$ 也移出。

结合 KS 已证明的原平方公式，$h=6i+7$、$j=N-1-i$，
$$
\boxed{
[U^{p-1}]
 \frac{\mathsf x^2\mathsf A^5}
      {(1-8U^3)\mathsf C^5}
=
2^7 3^8
\sum_{i=0}^{N-1}
 \frac{f_i^2g_j^2}{(h-2)(h-1)h(h+1)(h+2)}
\pmod p .
}
\tag{PL15}
$$
全部外常数和每个五次分母都是单位。
(PL14)--(PL15) 是原指定五次标架源的准确表达，不证明它非零。

用 XF 的 $\alpha_0=d\mathsf y/(\mathsf y^3-1)$，
还有
$$
\alpha_0=-\frac{\mathsf x^2}{1-8U^3}\,dU.
$$
所以 (PL14) 所需的是
$(\mathsf A/\mathsf C)^5\alpha_0$ 的首 Cartier 系数，而不是
$\alpha_0$ 本身的首 Cartier 系数。XF 已证
$\mathcal C(\alpha_0)=\alpha_1$，但没有证明这个带五次
原 period ratio 的微分具有相同的标量 Cartier 公式。

## 6. 保留同标签的双变量形式

单个 $S_{p-6}$ 只保留总次数，可能相消。
为写出每个原标签，令
$$
\mathsf C_\nu=\mathsf C(U_\nu),\quad
\mathsf A_\nu=\mathsf A(U_\nu),\quad
\mathsf x_\nu=\mathsf x(U_\nu),\quad
D_\nu=1-8U_\nu^3,\qquad \nu=1,2.
$$
同一换元 (PL6) 在两个变量上分别作用，给出完全原的系数公式
$$
C_{m_1+1}C_{m_2+1}
=b^2c^{-(m_1+m_2)}
\operatorname{Res}_{U_1=U_2=0}
\frac{\mathsf x_1\mathsf x_2
      \mathsf C_1^{m_1}\mathsf C_2^{m_2}}
 {D_1D_2\mathsf A_1^{m_1+1}\mathsf A_2^{m_2+1}}
             \,dU_1\,dU_2 .
\tag{PL16}
$$
这保留了两个分母标架，不能先令 $U_1=U_2$ 来证明一个筛后的结论。

对实际 $m_1=h-3$、$m_2=p-h-3$，定义
$$
w_h=\mathbf1_{(h,p+1)=1}P_{h-1}(1/s)^2,\qquad
Q_h=(h-2)(h-1)h(h+1)(h+2).
$$
把 (PL16) 逐项乘 $Q_hw_h$，并保持
$t_1^{h-3}t_2^{p-h-3}$ 不同单项式，恰给 XF(32) 的原目标向量。
因此每个原 primitive、Legendre 和两个 sigma 因子都仍在同一 $h$，
没有用两个密度估计的交或整体矩阵可逆来替代它。

固定方程 (PL2) 作用在 $U$ 变量的 period 上；
原系数在 $t=c\mathsf A/\mathsf C$ 这个逆 Schwarz 参数中。
故 (PL2) 本身不提供原 $C_k$、$f_i$、$g_j$ 的固定宽线性系数递推。
本篇也没有证明 (PL16) 的任何指定 primitive 分量必须非零，
没有把它与 R833 的另一实际 unsquared 源无证等同。

## 依赖和未完成入口

- XF(26)--(30)：实际全六层 Serre 导子、原 Fermat test vector
  和完整 Cayley 系数规范。
- KS(11)--(15)：原临界二次卷积及 $-192/Q_h$。
- R683 / R697 / R770：原 $C_k$、平方常数、所需同标签筛。

正文已给出 Picard--Fuchs 推导、初值、Wronskian、全部 $p$ 分母范围、
换元和常数，不需要新的数值验证。
尚须处理的是 (PL16) 的真实筛后向量，或为 (PL14) 的实际
$\mathsf C^{-5}$ Cartier 源找到新的非消失输入；后一个未筛结论即使成立，
也不会自动完成前一个。
