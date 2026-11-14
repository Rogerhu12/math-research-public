# R55. 普通首权的固定对数级数与实际斜率的有限权证书

日期：2026-11-12。**状态：固定系列、整性及有限证书均已证明；无穷非零仍开。**

## 1. 一个固定有理系列恢复全部普通首权商

沿用 R52 的固定 $F,H,\Theta,P$，置
$$
B(v)=\Theta(v)^{17}P(v),\qquad
W(v)=B(v)(1-v)^{-1/2}=\sum_{n\ge1}w_nv^n,
$$
以及同一个固定有理系列
$$
\boxed{\quad
I(v)=\sum_{n\ge1}\frac{w_n}{4n+1}v^n,\qquad
G_{\rm ord}(v)=I(v)-W(v)\log F(v).
\quad}
\tag{1}
$$
取任何普通目标素数 $p=4r+1\ge13$、$p\ne17$。则
$$
\boxed{\quad
[v^r]G_{\rm ord}\in\mathbb Z_p,\qquad
\frac{b_{p-1}}p\equiv17^{r-1}[v^r]G_{\rm ord}\pmod p.
\quad}
\tag{2}
$$
因此若 (2) 的右端对无穷多个这样的 $p$ 非零，就完成本题；
当前尚未证明它。

### 证明

取 $u=x^{-1/2}$、$v=17u^4$，实际坐标满足
$$
z=uF(v),\qquad dz=du/\sqrt{1-v},\qquad A(z(u))=B(v)/17.
$$
形式 residue 换元准确给
$$
b_{p-1}=17^{r-1}[v^r]W(v)F(v)^{-p}.
\tag{3}
$$
虽然 $[v^r]F=\binom{2r}{r}/(4^rp)$ 可能不整，
但 $W(0)=0$，所以 (3) 只使用 $F$ 到次数 $r-1$。
这段 $F$ 以及 $\log F$ 都整；$\Theta,W$ 到次数 $r$ 也整，
因为所需 $H$ 的分母 $4n+3$ 至多为 $p-2$，递推只除以小于 $p$ 的整数。
在这些有限截断中
$$
F^{-p}\equiv1-p\log F\pmod{p^2}.
$$
由 R51 的实际中央整除 $b_{p-1}\in p\mathbb Z_p$，(3) 因而给
$w_r\in p\mathbb Z_p$，并有
$$
\frac{b_{p-1}}p\equiv17^{r-1}
 \left(\frac{w_r}p-[v^r]W\log F\right)\pmod p.
$$
因为 $p=4r+1$，括号恰为 (1) 的第 $r$ 项，证明 (2)。

这保留了 $w_r/p$ 与 $[v^r]W\log F$ 的相消。
分别证明两项非零不足以证明目标非零。
全文见[固定对数系列](../notes/2026-11-12-ordinary-prime-coefficient-fixed-logarithmic-series.md)，
[精确模 $p^2$ 脚本](../scripts/check-ordinary-fixed-log-series.py)
已根端全文审查并运行；$p=13$ 还与 R51 的独立全局值一致。

## 2. 准确中心斜率还可由有限个正权检测

令 $\nu_p$ 是 R51 实际整测度，$J_p$ 为其单位 principal Mellin 变换。
已知 $J_p(0)=0$，且普通初级有限准确等价 $J_p'(0)\ne0$。
定义实际权矩
$$
M_j=\int_{\mathbb Z_p^\times}x^{j(p-1)}\,d\nu_p(x),\quad M_0=0,\qquad
\Delta_r=\sum_{j=0}^r(-1)^{r-j}\binom rjM_j.
$$
实际单 Euler 分布给
$$
M_j=\left(1-\frac{\pi^{j(p-1)}}{\bar\pi^{j(p-1)+1}}\right)
\Omega_p^{j(p-1)}(j(p-1))!\,b_{j(p-1)}
\quad(j\ge1).
\tag{4}
$$
所有周期、阶乘与 Euler 因子保留在式中。

有 $v_p\Delta_r\ge r$，并有收敛恒等式
$$
\boxed{\quad
\log_p(1+p)J_p'(0)
 =\frac1{p-1}\sum_{r\ge1}\frac{(-1)^{r+1}}r\Delta_r.
\quad}
\tag{5}
$$
若 $S_R$ 为右边前 $R$ 项，置
$$
h_p(R)=\min_{r\ge R+1}(r-v_p(r))
\ge R+1-\lfloor\log_p(R+1)\rfloor,
$$
则
$$
v_p(\log_p(1+p)J_p'(0)-S_R)\ge h_p(R).
$$
故对每个目标普通素数，有完整有限证书
$$
\boxed{\quad
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{ 有限}
\quad\Longleftrightarrow\quad
\exists R\ge1:\ v_pS_R<h_p(R).
\quad}
\tag{6}
$$
最高所需正权只有 $R(p-1)$。

### 证明

整测度范数至多一，而对所有单位 $x$ 有 $x^{p-1}-1\in p\mathbb Z_p$。
所以
$$
\Delta_r=\int(x^{p-1}-1)^r\,d\nu_p,\qquad v_p\Delta_r\ge r.
$$
在单位群上一致收敛的对数展开
$\log\langle x\rangle=(p-1)^{-1}\sum_{r\ge1}(-1)^{r+1}(x^{p-1}-1)^r/r$
可以逐项积分，证明 (5) 与尾界。
非零极限的赋值有限，而 $h_p(R)\to\infty$；
这与超距不等式给 (6) 的两个方向。
全文见[加法卷积、对数算子和逐权证书](../notes/2026-11-12-ordinary-theta-slope-convolution-and-weight-moments.md)。

第一层 $S_1=M_1/(p-1)$、$h_p(1)=2$，
恰好检测 $v_pb_{p-1}=1$，也就是 (2) 非零。
更高层容许首导数有任意有限赋值；首层失败不等于导数为零。

## 3. 后续比较必须保持实际运算与字符

R51 的六因子 sigma 乘积在 Amice 侧给的是加法卷积。
因此斜率的核是六变量线性和上的 $\log\langle x_1+\cdots\rangle$，
不能拆成六个固定代数数对数或各因子 Mellin 变换的乘积。
在单位测度上，(5) 等于收敛算子
$$
\log\Theta=\frac1{p-1}\sum_{r\ge1}
 \frac{(-1)^{r+1}}r(\Theta^{p-1}-1)^r,\qquad
\Theta=(1+Z)d/dZ.
$$
这不是有限次 Coleman 原函数。

同一 CM type 的 Katz 函数方程在 Galois 规范中是
$\xi\mapsto\epsilon(\xi^\tau)^{-1}$。
对本题自对偶中心 $\phi^\tau=\epsilon\phi^{-1}$ 和反圆角色
$\rho^\tau=\rho^{-1}$，它把 $\phi\rho$ 点点固定，
并没有把当前 $J_p(T)$ 的变量反转。
完整字符计算和 BDP、Agboola 等定理的准确范围见
[函数方程与导出单位核查](../notes/2026-11-12-ordinary-katz-functional-equation-and-derived-units.md)。

当前可继续使用的对象是同一个 $G_{\rm ord}$ 和 (5) 的实际正权矩；
未证明的高度非退化、不同角色的非零或有限样本均不替代所缺的无穷性。
