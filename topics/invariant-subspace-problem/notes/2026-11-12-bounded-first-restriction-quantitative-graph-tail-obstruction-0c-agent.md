# R193：有界一阶不变限制的实际有限头图尾下界

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R193。

状态：完整证明。新增结论是原 Haar 模型中未知有界一阶限制的定量图尾约束；典型全平面谱的交替幂尾给伸缩指数下界，并排除一个允许无限 Walsh 次数的快速图尾类。证明使用实际 $V_J$ 的精确不同位恒等式，没有把高位强收敛误差除以小系数。一般任意慢图尾的核仍未排除。

## 1. 实际设置和有界限制

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,
$$
令 $X=X_u$ 为 R125 的实际闭第一阶乘子。
记
$$
N_j=A^{2^j}/d_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1},
$$
并记纯张量算子
$$
S_j=I-2E_j.
$$
R125 的构造给
$$
X=X_0+K,\qquad
X_0=\overline{a_*I+\sum_ja_jS_j},
\tag{1.1}
$$
其中
$$
K=\sum_ja_j(V_j-S_j)\in B(H),\qquad
\|K\|\le8\sum_j|a_j|\eta_j
\le8\|a\|_2\|\eta\|_2.
\tag{1.2}
$$
这是有界扰动的真实闭算子等式，故
$$
X^*=X_0^*+K^*
$$
在相同的完整伴随域上成立。

以下记
$$
g=\|a\|_2,\qquad k=\|K\|,\qquad c_0=2g+2k.
\tag{1.3}
$$
每个位有 $\|V_j\|\le6$、$\|S_j\|\le3$。

设 $0\ne M\subset H$ 闭且 $A$ 不变，并假设
$$
M\subseteq\operatorname{Dom}X,\qquad
X|_M\in B(M).
\tag{1.4}
$$
这正是 R176 的 monic 有界交换系数多项式核，或相应实际 Bell 核，已经满足的结构；这里不要求某个特定平方根表达。

R161 已证明
$$
\operatorname{Dom}X=\operatorname{Dom}X^*,\qquad
\|Xf\|^2-\|X^*f\|^2=\langle C_af,f\rangle,
\qquad \|C_a\|\le(4+\varepsilon_{\rm carry})g^2.
$$
所以可以固定
$$
\boxed{
L=\bigl(\|X|_M\|^2+\|C_a\|\bigr)^{1/2}
}
\tag{1.5}
$$
并有
$$
\|X^*x\|\le L\|x\|\qquad(x\in M).
\tag{1.6}
$$
$X^*x$ 不被假定仍在 $M$。

令 $\mathscr H_m$ 为只依赖物理低 $m$ 位的有限柱空间，
$P_m$ 为相应正交条件期望。
对于 $x\in\operatorname{Dom}X^*$，定义真正的有限头图逼近误差
$$
\boxed{
\delta_m(x)
=\inf_{v\in\mathscr H_m}
\bigl(\|x-v\|+\|X^*(x-v)\|\bigr).
}
\tag{1.7}
$$
R125 的有限柱双图核心给 $\delta_m(x)\to0$。
这个事实本身不含收敛速度。

## 2. 高位实际乘积在有限头上精确等于 Walsh 乘法

对有限 $J\subseteq[m,\infty)$，置
$$
T_J=\prod_{j\in J}V_j,\qquad
\mathcal J_J=M_{\chi_J},\qquad r=|J|.
$$
$\mathcal J_J$ 是物理 Walsh 符号乘法的酉算子。
$T_J\in\mathfrak C=\{A\}'$，所以保持 $M$。

R16/R115 的实际不同位恒等式为
$$
\prod_{j\in F}V_j1=\chi_F
\quad(F\text{ 有限、各位不重复}).
\tag{2.1}
$$
若
$$
v=\sum_{F\subseteq[0,m)}\widehat v_F\chi_F\in\mathscr H_m,
$$
则实际因子全都交换，并且 $J\cap F=\varnothing$。
因此
$$
T_Jv
=\sum_F\widehat v_F\prod_{j\in J\cup F}V_j1
=\sum_F\widehat v_F\chi_{J\cup F}
=\chi_Jv.
$$
即
$$
\boxed{
T_Jv=\mathcal J_Jv,\qquad \|T_Jv\|=\|v\|
\quad(v\in\mathscr H_m,\ J\subseteq[m,\infty)).
}
\tag{2.2}
$$

(2.2) 是任意有限 $J$ 的精确真实等式，不是先固定 $r$ 再让各位趋于无穷的强极限。
因而这里没有 $\eta_m6^r$ 或未知强误差需要支付。

另一方面，在任意输入上只使用安全的全空间界
$$
\boxed{\|T_J\|\le6^r.}
\tag{2.3}
$$
不把有限头上的等距性质误用到整个 $H$。

## 3. 真正有界的伴随交换子

R161 给
$$
[X^*,N_j]=D_j
$$
作为完整域上的有界交换子，并且
$$
\|D_j\|\le36\sum_i|a_i|\widetilde R_{ij},
\qquad
\widetilde R_{ij}=
\begin{cases}
1,&i=j,\\
\alpha_{\max(i,j)}/\alpha_{\min(i,j)},&i\ne j.
\end{cases}
$$
因 $\eta_*=\sup_i\eta_i<1/4$，
$$
\sum_i\widetilde R_{ij}^2
\le1+\frac{2\eta_*^2}{1-\eta_*^2}<4.
$$
所以 $\|D_j\|\le72g$。

实际逆 $(I+N_j)^{-1}\in\mathfrak C$ 保持共同域
$\operatorname{Dom}X=\operatorname{Dom}X^*$。
逆交换子恒等式遂给
$$
[X^*,V_j]
=-2(I+N_j)^{-1}D_j(I+N_j)^{-1}.
$$
使用 $\|(I+N_j)^{-1}\|<3$，得到
$$
\boxed{\|[X^*,V_j]\|\le1296g.}
\tag{3.1}
$$
由有限 Leibniz 展开，
$$
\boxed{
\|[X^*,T_J]\|
\le1296g\,r\,6^{r-1}=:b_r.
}
\tag{3.2}
$$
并且
$$
X^*T_Jh=T_JX^*h+[X^*,T_J]h
\qquad(h\in\operatorname{Dom}X^*).
\tag{3.3}
$$
这里所有输入均在已证明保持的完整域中。
没有使用 $X_n^*h\to X^*h$ 在任意 $h$ 上成立这一未经证明的断言。

## 4. 有限头上的伴随范数增量

在单个位的 Walsh 基 $\{1,\chi_j\}$ 中，
$$
S_j=
\begin{pmatrix}0&-1\\1&2\end{pmatrix},
\qquad
S_j^*=
\begin{pmatrix}0&1\\-1&2\end{pmatrix}.
$$
因此
$$
M_{\chi_j}S_j^*M_{\chi_j}=2I-S_j^*.
\tag{4.1}
$$
不同位的纯算子严格张量独立。

若 $v\in\mathscr H_m$、$J\subseteq[m,\infty)$，则
$$
S_j^*v=-\chi_jv\qquad(j\in J).
$$
对有限 $J$ 使用 (4.1)，并对其余平方可和尾用有限柱上的实际强极限，得到
$$
X_0^*\mathcal J_Jv
=
\mathcal J_JX_0^*v
+2\left(\sum_{j\in J}\overline{a_j}\right)\mathcal J_Jv
+2\mathcal J_J\sum_{j\in J}\overline{a_j}\chi_jv.
\tag{4.2}
$$
因 $v$ 不依赖 $J$ 中的位，
$$
\left\|\sum_{j\in J}\overline{a_j}\chi_jv\right\|
=\left(\sum_{j\in J}|a_j|^2\right)^{1/2}\|v\|
\le g\|v\|.
$$

加回真实有界进位 $K^*$：
$$
X^*\mathcal J_Jv
=
\mathcal J_JX^*v
+2\left(\sum_{j\in J}\overline{a_j}\right)\mathcal J_Jv
+2\mathcal J_J\sum_{j\in J}\overline{a_j}\chi_jv
+(K^*\mathcal J_J-\mathcal J_JK^*)v.
$$
最后一项范数至多 $2k\|v\|$。
于是
$$
\boxed{
\|X^*\mathcal J_Jv\|
\ge
2\left|\sum_{j\in J}a_j\right|\|v\|
-\|X^*v\|-c_0\|v\|.
}
\tag{4.3}
$$

常数项 $a_*$ 在共轭差中相消。
(4.3) 保留真实进位的全局有界代价 $2k$，而非忽略进位。

## 5. 主定理：未知有界限制中的统一图尾下界

对 $r\ge1$ 定义
$$
K_r(L,a)
=1+(L+1)6^r+1296g\,r\,6^{r-1},
\qquad
T_0(L,a)=\frac{3L+c_0}{2}.
\tag{5.1}
$$

**定理5.1。**
若 $x\in M$ 且 $\|x\|=1$，则对每个有限非空
$J\subseteq[m,\infty)$，有
$$
\boxed{
\delta_m(x)\ge
\min\left\{
\frac12,\
\frac{\left(\left|\sum_{j\in J}a_j\right|-T_0(L,a)\right)_+}
 {K_{|J|}(L,a)}
\right\}.
}
\tag{5.2}
$$

证明：取任意 $v\in\mathscr H_m$，记
$$
e=x-v,\qquad \delta=\|e\|+\|X^*e\|.
$$
若 $\delta\ge1/2$，(5.2) 的相应下界已成立。

设 $\delta<1/2$。
此时
$$
\|v\|\ge1-\delta>\frac12,\qquad
\|X^*v\|\le L+\delta.
\tag{5.3}
$$
$T_Jx\in M$，所以由 (1.6)、(2.2)—(2.3)、(3.3)，
$$
\begin{aligned}
\|X^*T_Jv\|
&\le\|X^*T_Jx\|+\|X^*T_Je\|\\
&\le L\|T_Jx\|+6^r\|X^*e\|+b_r\|e\|\\
&\le L\|v\|
+\bigl((L+1)6^r+b_r\bigr)\delta.
\end{aligned}
\tag{5.4}
$$
另一方面，(2.2) 和 (4.3) 给
$$
\|X^*T_Jv\|
\ge
\left(2\left|\sum_{j\in J}a_j\right|-c_0\right)\|v\|
-\|X^*v\|.
$$
结合 (5.3)—(5.4)，
$$
\left(2\left|\sum_{j\in J}a_j\right|-L-c_0\right)\|v\|
\le L+K_r(L,a)\delta.
\tag{5.5}
$$
若 (5.2) 的分子非正，没有要证明的正下界。
若它为正，则 (5.5) 左边的系数为正，可以使用 $\|v\|>1/2$，得到
$$
\left|\sum_{j\in J}a_j\right|-\frac{3L+c_0}{2}
\le K_r(L,a)\delta.
$$
对全部 $v$ 取下确界，得到 (5.2)。证毕。

这是对 $M$ 中每个单位向量的同一个定量下界。
它没有把 $X^*$ 的像假定仍在 $M$，也没有使用未知压缩符号的点态谱。

### 5.1 一般非绝对可和复杂尾的代价函数

对 $T>0$ 定义
$$
r_a(m,T)
=\min\left\{|J|:
J\subseteq[m,\infty)\text{ 有限},
\left|\sum_{j\in J}a_j\right|\ge T\right\},
\tag{5.6}
$$
若不存在则记为无穷。

如果 $a\notin\ell^1$，则对每个 $m,T$，
$$
r_a(m,T)<\infty.
$$
确实，将非零系数分入有限个宽度小于 $\pi$ 的相位扇区，
其中至少一个扇区的模长和发散；
沿其中心方向投影得到同号发散实和。
取有限子集即达到任意给定 $T$。

取 $T=T_0(L,a)+1$，由 (5.2)，
$$
\boxed{
\delta_m(x)\ge
\frac{1}{K_{r_a(m,T)}(L,a)}.
}
\tag{5.7}
$$
右边小于 $1/2$，所以无需再保留最小值。
特别，对常数 $C_{L,a}>0$，
$$
\boxed{
\delta_m(x)
\ge
\frac{1}{C_{L,a}\,(r_a(m,T)+1)\,6^{r_a(m,T)}}.
}
\tag{5.8}
$$
这里不要求 $r_a(m,T)$ 与物理位置 $m$ 有任何预先控制。
高度稀疏或极慢累积的复杂尾也满足这个准确版本。

## 6. 全复平面谱的交替幂尾：伸缩指数下界

取
$$
a_j=(-1)^j(j+1)^{-s},\qquad \frac12<s\le1,
\tag{6.1}
$$
常数项 $a_*$ 任意。
它属于 $\ell^2\setminus\ell^1$。
对每个相位 $\theta$，正、负两条子列至少有一条给无限的相位缺陷和：
$$
\sum_j\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right)=\infty.
$$
所以由 R138，这是真正的全复平面谱分支，不属于空谱单相位分支。

### 6.1 $1/2<s<1$

固定 $T>0$。
在 $[m,\infty)$ 的偶数位中，取最先的
$$
r=\left\lceil C_T(m+1)^s\right\rceil
$$
个位。
其最大指标不超过 $m+2r+1$。
因为 $s<1$，充分大的 $m$ 满足 $2r+1\le m+1$，故每个所取模长至少
$(2m+3)^{-s}$。
选取充分大的固定 $C_T$，得到
$$
\sum_{j\in J}a_j\ge T,\qquad
r_a(m,T)\le C'_T(m+1)^s.
\tag{6.2}
$$
有限多个小 $m$ 可通过增大常数吸收。

### 6.2 $s=1$

在 $[m,C_T(m+1)]$ 中选偶数位。
谐和和的下界随固定 $C_T\to\infty$ 增大，渐近为
$\frac12\log C_T$。
用积分比较，选择一个只依赖 $T$ 的充分大常数 $C_T$，即可使该和至少 $T$。
所取位数为 $O_T(m+1)$，所以仍有
$$
r_a(m,T)\le C'_T(m+1)^s
\quad(s=1).
\tag{6.3}
$$

代入 (5.8)，并把多项式因子吸收到指数常数中，得到：

**推论6.1。**
若 (6.1) 的实际一阶 $X$ 在非零闭 $A$ 不变 $M$ 上有界，则存在常数
$c_M,C_M>0$，使每个单位 $x\in M$ 都满足
$$
\boxed{
\delta_m(x)\ge c_M\exp\bigl(-C_M(m+1)^s\bigr)
\qquad(m\ge0).
}
\tag{6.4}
$$
常数允许依赖 $\|X|_M\|$。
当 $M$ 来自某个已知有界代数分支时，可使用该分支的全空间范数上界选择 $L$。

## 7. 一个允许无限 Walsh 次数的实际核排除类

令 $\mathcal N$ 为 Walsh 次数算子，$\Lambda=I+\mathcal N$。
纯模型中
$$
S_j=C_j-A_j+2n_j
$$
为 Boolean 创建、消灭及占据分解。
在纯次数 $q$ 上，创建和消灭的范数分别不超过
$g\sqrt{q+1}$、$g\sqrt q$，
而
$$
\left\|\sum_j\overline{a_j}n_j\right\|_{\mathcal H_q}
\le g\sqrt q.
$$
按三个相邻次数块求和，并加常数与实际有界 $K^*$，得到安全界
$$
\boxed{
\|X^*h\|
\le (|a_*|+8g+k)\|\Lambda^{1/2}h\|,
\qquad h\in\operatorname{Dom}\Lambda^{1/2}.
}
\tag{7.1}
$$
域包含及该界先在有限柱上证明，再用闭性延拓。
没有把 $X^*$ 当成处处有界算子。

$P_m$ 与 $\Lambda$ 交换，故对
$x\in\operatorname{Dom}\Lambda^{1/2}$，
取 $v=P_mx$ 得
$$
\boxed{
\delta_m(x)
\le (1+|a_*|+8g+k)\,
\|\Lambda^{1/2}(I-P_m)x\|.
}
\tag{7.2}
$$

因此对 (6.1) 的行，若某个非零 $x$ 满足
$$
x\in\operatorname{Dom}\Lambda^{1/2},\qquad
\|\Lambda^{1/2}(I-P_m)x\|
\le C\exp(-c(m+1)^t)
\quad\text{某个 }t>s,
\tag{7.3}
$$
则它不可能属于任何满足 (1.4) 的闭 $A$ 不变空间。
因为 (7.2) 与 (6.4) 的指数速度矛盾。

特别：

- $x$ 不属于以该 $X$ 为基础的任何 R176 monic 有界交换系数多项式核；
- 同样排除 R176 的实际倾斜 Bell 核，因为倾斜仅把 $X$ 改为 $X+H$，$H\in\mathcal A$ 有界并保持该核，核上 $X$ 仍有界；
- 不要求 $x$ 有有限 Walsh 次数，不要求它由有限个模式的有限多项式生成。

一个明确的无限次数测试类为
$$
x_t=\sum_{n\ge1}e^{-2n^t}\chi_{\{0,\ldots,n-1\}},
\qquad t>s.
\tag{7.4}
$$
它具有无界 Walsh 次数，但
$$
\|\Lambda^{1/2}(I-P_m)x_t\|^2
=\sum_{n>m}(n+1)e^{-4n^t},
$$
由积分比较满足 (7.3)（适当减小指数常数）。
所以这些非零向量被上述实际核全部排除。

这只是对这些特定算子核的排除，不据此声称所有 $x_t$ 的完整 $A$ 循环性。

## 8. 为什么这还没有排除任意慢核

(5.2) 的损失来自两个真实而不同的事实：

- 在有限头上，$T_Jv=\chi_Jv$ 精确且等距；
- 在任意误差 $x-v$ 上，目前只能使用 $\|T_J\|\le6^{|J|}$ 及对应的有界伴随交换子界。

因此，若只能知道 $\delta_m(x)\to0$，而没有与
$r_a(m,T)$ 比较的速度，(5.8) 不矛盾。
本稿没有从强渐近、全本质支撑或 Calkin 忠实性制造这个缺失的速度。

R176 还给未知核上全部自然幂及几何幂界。
它们使各个固定幂图范数在该核上与 $H$ 范数等价，
但这种等价本身不控制核相对于固定物理头空间的逼近位置。

有一个直接的实际障碍说明不能期待单位球上的统一逼近率：
非零闭 $A$ 不变 $M$ 必无限维，
因为 $A$ 单射且拟幂零，非零有限维不变限制会同时单射和幂零，矛盾。
所以对每个 $m$ 都可取单位
$x_m\in M\cap\mathscr H_m^\perp$。
于是
$$
\delta_m(x_m)\ge\operatorname{dist}(x_m,\mathscr H_m)=1.
\tag{8.1}
$$
换言之，任何直接试图由 $\|X|_M\|$ 推出
$\sup_{\|x\|=1,x\in M}\delta_m(x)\to0$ 的路线必然失败。

甚至给定任意 $\epsilon_m\downarrow0$，
也可在任意这样的无限维 $M$ 中构造单个向量，
其有限头误差沿子序列慢于 $\epsilon_m$：
取平方可和的正数 $c_n$，递归选 $m_n$ 使
$\epsilon_{m_n}\le c_n/2$，再取正交单位
$$
v_n\in M\cap
(\mathscr H_{m_n}+\operatorname{span}\{v_1,\ldots,v_{n-1}\})^\perp.
$$
令 $x=\sum_nc_nv_n$。
因 $v_n\perp\mathscr H_{m_n}$，
$$
\delta_{m_n}(x)\ge|\langle x,v_n\rangle|=c_n\ge2\epsilon_{m_n}.
$$
这个事实不排除 $M$ 中另有某个特殊快速向量；
真正尚缺的是从实际不变性构造那种向量，或直接改进误差上的 $6^r$ 放大。

没有把 (8.1) 当成实际非零核的构造。
本稿只给出在假设核存在时必须满足的图尾下界及一个严格的新排除类。
慢二次单核与完整 Hilbert 不变子空间问题仍然开放。

### 8.1 全空间乘积放大确实可以是指数，不能仅换一个较好常数消去

单个位的纯矩阵满足
$$
\|S_j\|=1+\sqrt2.
$$
不同位严格张量相乘，故
$$
\left\|\prod_{j\in J}S_j\right\|=(1+\sqrt2)^r.
$$
由实际差 $\|V_j-S_j\|\le8\eta_j$ 的有限 telescoping，
$$
\left\|T_J-\prod_{j\in J}S_j\right\|
\le8\,6^{r-1}\sum_{j\in J}\eta_j
\le8r6^{r-1}\eta_m
\quad(J\subseteq[m,\infty)).
$$
对任意固定 $r$，把 $m$ 取得足够大，得到
$$
\boxed{\|T_J\|\ge\frac12(1+\sqrt2)^r.}
\tag{8.2}
$$
所以不存在对所有有限高位集都成立的多项式级全空间范数上界。

这不证明 $T_J|_M$ 也必须如此增长。
它准确说明：若仍把未知图逼近误差 $x-v$ 当成一般 $H$ 向量控制，
仅改善全空间范数估计不能消去指数级代价。
$x-v$ 一般不在 $M$，因为非零有限柱本身循环，不能属于未知真不变 $M$。
要继续排核，必须取得真正适用于该误差或未知 $M$ 的额外结构。


## 9. 依赖范围

- R16/R115：真实不同位 Cayley 乘积作用于 $1$ 的精确恒等式；
- R88：有界交换子保持所有闭 $A$ 不变空间；
- R125：纯模型加有界真实进位、有限柱双图核心；
- R161：完整通常伴随同域、自交换子形式与实际有界交换子；
- R176：monic/Bell 核上的真实有界一阶限制；
- R138：交替非绝对可和行属于全复平面谱分支。

新增定量论证是 §§2—7，特别是实际精确有限头恒等式 (2.2) 与完整域交换子 (3.3) 的组合。
