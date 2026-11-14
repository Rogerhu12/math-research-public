# 普通中央 theta 斜率：加法卷积、对数算子和可用的逐权证书

日期：2026-11-12。**状态：§1–5 的测度公式和界已证明；§6 为原始文献适用范围核查。没有证明无穷素数非零。**

本笔记采用 [R51](../results/R51-explicit-theta-section-and-central-square-constant.md) 已准确识别的固定截面
$$
 A(z)=\frac15\vartheta(z)\vartheta(2z)\sigma(z)^2
                       \sigma((2+i)z)\sigma((2-i)z)
       =\sum_{m\ge0}b_mz^m,\qquad b_4=1.
 \tag{1}
$$
这里所有函数都属于 $E:y^2=x^3-17x$ 的同一复均匀化；
$\vartheta(0)=1$、$\vartheta^2=x\sigma^2$。
固定普通目标素数
$$
 p\ge13,\quad p\equiv1\pmod4,\quad p\ne17,\qquad
 v_p(\pi)=1,\quad\pi\bar\pi=p.
$$
R51 的实际测度 $\nu_p$ 的 Amice 变换为
$$
 \mathcal A_p(Z)=A(\Omega_p\log(1+Z))\in\mathcal O_p[[Z]],
 \qquad\|\nu_p\|\le1,
 \tag{2}
$$
其中 (2) 解释为先在椭圆正式坐标中构造整级数，再沿实际正式群同构拉回。
不能把挠点的正式对数直接代入复表达式。单位上的 principal Mellin 变换记作
$$
 J_p(T)=\int_{\mathbb Z_p^\times}
       (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\nu_p(x).
 \tag{3}
$$
已知 $J_p(0)=0$，而初级有限准确等价 $J_p'(0)\ne0$。

## 1. 乘积给加法卷积，斜率核是六变量的线性和

设 $\mu_\vartheta,\mu_\sigma$ 的 Amice 变换分别为
$\vartheta(\Omega_p\log(1+Z))$、$\sigma(\Omega_p\log(1+Z))$。
二者都是整有界测度：$\Sigma(t)=\sigma(\log_Et)$ 整，
$\vartheta(\log_Et)$ 是 $x(t)\Sigma(t)^2$ 的常数项一整平方根。
对 $a\in\mathbb Z_p$，以 $[a]_*$ 表示乘 $a$ 的推前。
以 $*_{+}$ 表示加法卷积。Amice 变换的乘法给出准确恒等式
$$
 \boxed{\quad
 \nu_p=\frac15\mu_\vartheta*_{+}[2]_*\mu_\vartheta
       *_{+}\mu_\sigma*_{+}\mu_\sigma
       *_{+}[2+i]_*\mu_\sigma*_{+}[2-i]_*\mu_\sigma .
 \quad}
 \tag{4}
$$
两个 $2\pm i$ 已通过所选普通嵌入看成 $\mathbb Z_p^\times$。

令
$$
 L(\mathbf x)=x_1+2x_2+x_3+x_4+(2+i)x_5+(2-i)x_6.
$$
则
$$
 \boxed{\quad
 \log_p(1+p)J_p'(0)=\frac15
 \int_{\mathbb Z_p^6}
 {\bf1}_{L(\mathbf x)\in\mathbb Z_p^\times}
       \log_p\langle L(\mathbf x)\rangle\,
 d\mu_\vartheta(x_1)d\mu_\vartheta(x_2)
 \prod_{j=3}^6d\mu_\sigma(x_j).
 \quad}
 \tag{5}
$$
被积函数是连续函数：单位集合是开闭集，函数在其补集定义为零。
有界测度的积和 Fubini 由局部常值函数的一致逼近构造，因此 (5) 不需引入
不存在的可数可加实测度。

证明 (4) 只需把 $(1+Z)^{x+y}$ 分解成两个指数；(5) 则对 (3) 微分。
特别地，(1) 的乘积没有给出 $J_p$ 的乘积，(5) 也没有给出六个
固定代数数对数的和。原子检验已经辨明两种运算：
$\delta_a*_{+}\delta_b=\delta_{a+b}$，其 Mellin 核涉及
$\log_p(a+b)$，而乘法卷积才给 $\log_p(ab)$。
此外
$$
 \mu_\vartheta(\mathbb Z_p)=1,\qquad
 \mu_\sigma(\mathbb Z_p)=0.
$$
因此四个 sigma 因子的出现尤其不等于四个非零单位对数的乘积。

## 2. 单一固定截面的全权 Newton 差分公式

以下公式给实际 $J_p'$ 的另一种有限证书，不使用有限层挠点 Fourier 和。
记
$$
 m_j=j(p-1),\qquad
 M_j=\int_{\mathbb Z_p^\times}x^{m_j}\,d\nu_p(x),
 \qquad
 \Delta_r=\sum_{j=0}^r(-1)^{r-j}\binom rjM_j .
 \tag{6}
$$
有 $M_0=0$。已证明的
[principal tame 单 Euler 分布](2026-11-12-theta-principal-tame-euler-distribution.md)
在乘单位和常数正规化后仍适用，因而
$$
 \boxed{\quad
 M_j=\left(1-\frac{\pi^{m_j}}{\bar\pi^{m_j+1}}\right)
          \Omega_p^{m_j}m_j!\,b_{m_j}\quad(j\ge1).
 \quad}
 \tag{7}
$$
这里 $\Omega_p$ 是同一个实际局部周期；未把它假定为固定代数数。
(7) 的平方根符号是原分布定理已统一确定的正号。

因为 $x^{p-1}-1\in p\mathbb Z_p$ 对所有单位 $x$ 成立，
$$
 \Delta_r=\int_{\mathbb Z_p^\times}(x^{p-1}-1)^r\,d\nu_p(x),
 \qquad v_p(\Delta_r)\ge r .
 \tag{8}
$$
在整个单位群上，对数级数一致收敛：
$$
 \log_p\langle x\rangle
   =\frac1{p-1}\sum_{r\ge1}\frac{(-1)^{r+1}}r
                   (x^{p-1}-1)^r.
$$
故
$$
 \boxed{\quad
 \log_p(1+p)J_p'(0)=
 \frac1{p-1}\sum_{r\ge1}\frac{(-1)^{r+1}}r\Delta_r .
 \quad}
 \tag{9}
$$
注意 (9) 不是把 $\log$ 作用于某个有限或无限矩的乘积；
它是对同一测度的连续线性泛函。

设
$$
 S_R=\frac1{p-1}\sum_{r=1}^R\frac{(-1)^{r+1}}r\Delta_r,\qquad
 h_p(R)=\min_{r\ge R+1}\bigl(r-v_p(r)\bigr).
 \tag{10}
$$
则严格尾界为
$$
 v_p\bigl(\log_p(1+p)J_p'(0)-S_R\bigr)\ge h_p(R),
 \qquad
 h_p(R)\ge R+1-\lfloor\log_p(R+1)\rfloor .
 \tag{11}
$$
第二个不等式利用
$r-v_p(r)\ge r-\lfloor\log_pr\rfloor$ 及后者随正整数 $r$ 非减。
特别地，当 $1\le R\le p-2$ 时，$h_p(R)=R+1$。
因此准确有限性证书是
$$
 \boxed{\quad
 J_p'(0)\ne0
 \iff \text{存在 }R\ge1\text{ 使 }v_p(S_R)<h_p(R).
 \quad}
 \tag{12}
$$
正向取 $R$ 足够大，使尾界超过非零极限的赋值；反向由超距不等式。

首两项写开为
$$
 S_1=\frac{M_1}{p-1},\qquad
 S_2=\frac{2M_1-M_2/2}{p-1}.
 \tag{13}
$$
$R=1$ 的成功条件正是 $v_p(b_{p-1})=1$，因为 (7) 的周期、Euler 因子
和 $(p-1)!$ 都是单位。更大的 $R$ 能检测斜率有正赋值但非零的情形；
其最高输入权仅为 $R(p-1)$，尾界已经明确。
这改善有限证书的输入组织，但未给任何跨 $p$ 非零定理。

## 3. 斜率是 $\log\Theta$，不是有限次 Coleman 原函数

在单位支撑的测度空间上，令 $\Theta=(1+Z)d/dZ$ 作用于 Amice 变换。
它对应把测度乘以函数 $x$，所以是范数至多一的算子，其逆也存在。
算子 $\Theta^{p-1}-1$ 对此空间的范数至多 $p^{-1}$。于是
$$
 \log\Theta:=\frac1{p-1}
       \sum_{r\ge1}\frac{(-1)^{r+1}}r(\Theta^{p-1}-1)^r
 \tag{14}
$$
在算子范数中收敛，(9) 正是把 $(\log\Theta)\mathcal A_p^\times$
在 $Z=0$ 评价。这里 $\mathcal A_p^\times$ 是实际单位限制的 Amice 变换。
这个定义不声称 $\Theta$ 在所有测度上可逆，原点和非单位部分已经删掉。

一个小而准确的障碍如下。不存在有理函数 $R(X)\in\mathbb C_p(X)$，
使
$$
 R(x)=\log_p x\qquad(x\in1+p\mathbb Z_p)
 \tag{15}
$$
在整个该圆盘成立。否则解析微分及恒等定理给 $R'(X)=1/X$；
有理函数的导数在任何有限点的留数为零，而 $dX/X$ 在零的留数为一，
矛盾。故任何对所有单位测度有效的有限 Laurent 组合
$\sum_j c_j\Theta^j$ 都不能等于 (14)。
更一般的有理函数算子若在这些点定义，也有同样障碍。

因此，已有公式中把 $\Theta^{-j}$ 的整数负幂识别为 Coleman 原函数，
并没有自动识别本题的权导数。这个结论仅排除通用的有限算子替换；
没有排除此特定 $A$ 上存在额外的特殊恒等式。

## 4. 首项为单位的四阶零仍不能单独控制 Mellin 零阶

实际 (2) 满足
$$
 \mathcal A_p(Z)=\Omega_p^4Z^4+O(Z^5);
$$
故其加法 Amice 级数的首个模 $p$ 非零系数恰在四阶。
这是一条很强的整性数据，但不等于 principal Mellin 的中心斜率非零。

下面给出准确局部模型，保留这个四阶信息及真实单 Euler 分布。
固定任意 $r\ge1$，用前述单 Euler 笔记 §6 的构造，取 tame 不变整测度
$\rho_r$，满足
$$
 \rho_r(\mathbb Z_p)=0,\quad
 \rho_r|_{p\mathbb Z_p}=c[a]_*\rho_r,\quad
 a=\pi/\bar\pi,\ c=\bar\pi^{-1},
$$
且其单位 Mellin 变换为 $T^r$。该构造是有界泛函的收敛和，
并已证明没有对单点质量或可数可加性作额外假设。

另取非 principal tame 测度
$$
 \eta_4=\frac1{p-1}\sum_{\epsilon\in\mu_{p-1}}
                  \epsilon^{-4}\delta_\epsilon,\qquad
 \widetilde\nu_r=4!\eta_4+\rho_r.
 \tag{16}
$$
因为 $p\ge13$，角色四非平凡。它满足
$$
 \int x^n\,d\eta_4=
 \begin{cases}1,&n\equiv4\pmod{p-1},\\0,&\text{否则},\end{cases}
$$
而 $\rho_r$ 的低于 $p-1$ 的所有矩为零。
于是 $\widetilde\nu_r$ 的指数生成函数从 $z^4$ 开始且首系数一，
其 Amice 变换也从 $Z^4$ 开始且该系数一；它是整测度。
其 principal tame 投影恰为 $\rho_r$，
所以仍满足单 Euler 分布，而单位 principal Mellin 变换恰为 $T^r$。

这个模型依赖 $p$，不是固定有理截面 (1) 的反例。
它准确说明：有界性、四阶单位首项和 principal 单 Euler 分布三项合在一起，
仍容许任意中心零阶。若使用 (1) 的低阶挠点除子，必须加入进一步的全局比较。

## 5. 辅助二次域的普通 Heegner 点不能直接提供缺失的非零

这是固定秩二条件带来的一个有用限定。由 Gross–Zagier–Kolyvagin，
$\operatorname{rank}E(\mathbb Q)=2$ 排除解析秩零和一，因而
$\operatorname{ord}_{s=1}L(E,s)\ge2$。

设 $F/\mathbb Q$ 是一个虚二次域，满足某个经典 Gross–Zagier 公式的假设，
$P_F$ 为其中平凡类群角色对应的标准 Heegner 点。因
$$
 L(E/F,s)=L(E,s)L(E^{(D_F)},s)
$$
且第二因子在 $s=1$ 全纯，$L'(E/F,1)=0$。
Gross–Zagier 的非零常数乘 Néron–Tate 高度公式遂给
$\widehat h(P_F)=0$，所以 $P_F$ 挠。它在每个适用的 $p$ 处的形式对数均为零。

这一论证不适用于任意非平凡 Heegner 角色：其 Rankin 动机可能不同。
它只说明“另挑一个 Heegner 二次域，再用非挠点对数非零”这条直接路线，
在仍保留 $E$ 的平凡角色因子时不会解决本题。使用其他角色必须另证它们与
(3) 的真正中心导数的比较，不能用泛型非挠代替这个比较。

## 6. 已发表公式的准确中心与边界

以下均已读作者原文对应定理，不由搜索摘要推断。

1. **Bertolini–Darmon–Prasanna，2012，Theorem 1、3.12、3.16。**
   [作者全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/52.BDP2/paper.pdf)，
   *p-adic Rankin L-series and rational points on CM elliptic curves*，
   Pacific J. Math. 260 (2012), 261–303。

   Theorem 1 所述 Rubin 公式给 $L_p(\psi^*)$，
   $\psi^*$ 的无穷型为 $(0,1)$；它是一个全局点对数的平方，
   该点非挠当且仅当 $L(E,s)$ 在一处简单零。
   本曲线该点挠，故公式给零，未给以 $(1,0)$ 为中心的 $J_p'$。
   Theorem 3.12 的输入是权二 $f$ 与有限阶 $\chi$，输出是
   $L_p(f,\chi N_K)$ 的**值**及 Heegner 点对数平方。
   §3.4 Theorem 3.16 的 CM 分解给两个实际 Katz 因子，
   仍没有把值变成任意权方向的导数。
   其推广 Theorem 2 还明列根数负、$K$ 判别式奇及导子条件；
   根数正的 $E_{17}$ 与 $K=\mathbb Q(i)$ 不能直接代入这些假设。

2. **Bertolini–Darmon–Prasanna，2013，Assumption 5.12、Theorem 5.13。**
   [作者全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/51.BDP1/paper.pdf)，
   *Generalised Heegner cycles and p-adic Rankin L-series*，
   Duke Math. J. 162 (2013), 1033–1148。
   定理评价无穷型 $(k-1-j,1+j)$、$0\le j\le k-2$ 的中心临界角色，
   以广义 Heegner cycle 的 Abel–Jacobi 像平方表示该特值。
   其证明中的整数负次 theta 算子是 Coleman 原函数。
   这正是 §3 必须区别的操作；原定理不含
   $\log\Theta$ 的额外非零结论。

3. **Beneish–Darmon–Gehrmann–Roset，2025，Theorem 1.2。**
   [作者发表版](https://www.math.mcgill.ca/darmon/pub/Articles/Research/85.BDGR/BDGR.pdf)，
   *The Gross–Kohnen–Zagier theorem via p-adic uniformization*，
   Math. Ann. 391 (2025), 5581–5629。
   其精确公式是 Heegner 除子生成级数的对数
   $=\operatorname{pr}_1e^{\mathrm{ord}}(\Theta'_0)$；
   $\Theta_k$ 来自正定三元二次空间，权 $k+3/2$，
   $p$ 是固定 Shimura 曲线的分歧素数，使用 Cerednik–Drinfeld 一致化。
   本题 (1) 的普通固定椭圆曲线及一元 theta 核尚未给出这种数据或投影等式。
   该定理是真正的 theta 权导数公式，但不能仅凭“半整数权、中心零”套入 (3)。

这次核查没有找到上述已发表结果对固定 $E_{17}$、无穷变动 $p$
直接给 $J_p'(0)\ne0$ 的输入。可继续保留的具体对象是 (5)、
全权矩 (7) 及有显式尾界的 (9)–(12)，而非未证明的有限代数对数替换。
