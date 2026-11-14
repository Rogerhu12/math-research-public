# 稀疏偏离支撑与任意 ℓ² 共振背景

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065。
状态：完整证明的支撑扩展。承接 [近共振统一准则](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)；其正式版本已在提交 7186a4641df692aafca32ec954780bd0cab808f4 落地。本稿改变的是偏离的支持与主行量词，不把原主行替换成截出的子行。普通 ISP 仍开放。

## 1. 支撑版本的实际预解准则

给定
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad a,b\in\ell^2(\mathbb C).
$$
取任意无限集合
$$
S\subseteq\{j:a_j\ne0\}.
$$
将仅在 $S$ 上的非零幅度 $|a_j|$ 作非增重排，记为
$$
\rho_n^S.
$$
集合 $S$ 可以极稀疏，最大物理位和排序秩之间不要求关系；
$S$ 外的主系数 $a_j$ 只受完整行 $\ell^2$ 条件限制。

固定实数 $\kappa>2$。偏离行 $c$ 满足
$$
c_j=0\quad(j\notin S),\qquad
|c_j|\le C_0|a_j|^\kappa\quad(j\in S),
\tag{1.1}
$$
并对充分大的物理位 $j\in S$ 满足
$$
|c_j|\ge c_0|a_j|^\kappa,\qquad c_0>0.
\tag{1.2}
$$
相位任意；实数 $\kappa$ 只用于绝对幂比较。
令
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad X=X_b,
$$
$$
Y_S=\sum_{j\in S}c_j(R_j-I),\qquad
B=\sum_{j\ge0}a_j^2(R_j-I)^2.
\tag{1.3}
$$
注意 $X$ 和 $B$ 都仍使用整个主行，包含 $S$ 外的全部慢系数。

固定 $0<\varepsilon<c_0^2/64$。
假设沿无穷整数子序列 $N$，以
$$
\delta_N=\rho_N^S,\qquad L_N=1+\log^+(\delta_N^{-1})
$$
有
$$
L_N=O(N^{3/2}),
\tag{1.4}
$$
以及实际预解预算
$$
\boxed{
\sup_{|z|=\varepsilon\delta_N^{\,2\kappa-2}}
\log^+\|z(z-Y_S)^{-1}\|=O(N^2).
}
\tag{1.5}
$$

**定理 1。** 在这些条件下，
$$
T=X^2+Y_S-B,\qquad
\operatorname{Dom}T=\operatorname{Dom}X^2
$$
单射且值域稠密，因而
$$
\boxed{
\left[u^2+2\sum_{j\ge0}a_j^2(\chi_j-1)
+\sum_{j\in S}c_j(\chi_j-1)\right]e^w
\text{ 非零且对原实际 }A\text{ 循环}.
}
\tag{1.6}
$$

这里没有要求在 $S$ 外的非零主系数上也存在偏离下界。
特别允许无限多个非零慢主系数仍恰好处于二次共振值。

## 2. 完整主行的核、选位和预解成本

证明沿统一准则逐项核实，只改选位来源。

[R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)
对完整 $a\in\ell^2$ 给真实闭 $X$、全部自然幂域、
$T$ 的自然二阶域和 $C$ 自伴性。
$c\in\ell^1$ 保证 $Y_S$ 有界；局部二阶消去给完整 $B\in\mathcal G$。
若
$$
M=\ker T,
$$
则
$$
M\subseteq\bigcap_{n\ge0}\operatorname{Dom}X^n,\qquad
X_M\in B(M),\qquad
X_M^2=(B-Y_S)|_M.
\tag{2.1}
$$

从 $S$ 内幅度最大的 $N$ 个物理位中删去其排序前
$\lfloor N/4\rfloor$ 项，再删去所有物理位小于
$m_N=\lfloor N/4\rfloor$ 的项。
两次一共至多删 $2\lfloor N/4\rfloor$ 项。
故剩余足够取一个
$$
I_N\subset S,\qquad |I_N|=Q_N=\lfloor N/2\rfloor
$$
的集合，且
$$
\min I_N\ge m_N,\qquad
\delta_N\le|a_j|\le\frac{2\|a\|_2}{\sqrt N}
\quad(j\in I_N).
\tag{2.2}
$$
上界只使用子行平方和不超过完整主行平方和；
没有对 $S$ 的物理密度作假设。
充分大 $N$ 后，全部选位均满足 (1.2)。

取固定小参数 $\theta>0$，令
$$
r=\lceil\sqrt{N/\theta}\rceil.
$$
对任意 $r$ 元 $F\subset I_N$，
$$
\sum_F|a_j|\le2\|a\|_2r/\sqrt N=O_\theta(1),
$$
$$
\sum_F|a_j|^2=O_\theta(N^{-1/2}),\qquad
\sum_F|c_j|=O_\theta(N^{-(\kappa-1)/2}).
\tag{2.3}
$$
统一准则中所有输入 jets 只需要这些界及完整 $a\in\ell^2$。

定义
$$
\tau_j=c_j/(2a_j),\qquad L_j=8a_j(X+\tau_jI).
$$
(1.2)、(2.2) 给
$|\tau_j|^2\ge(c_0^2/4)\delta_N^{2\kappa-2}$。
使用完整 $B$ 与 $Y_S$ 的同一双圆周，整个函数
$$
G_F(z_B,z_Y)=\prod_{j\in F}(z_B-z_Y-\tau_j^2)^{-1}
$$
只作一次联合 Cauchy 求值。
真正核内算子
$$
\mathfrak R_F=
\left(\prod_{j\in F}(8a_j)^{-1}\right)
\left(\prod_{j\in F}(X_M-\tau_jI)\right)
G_F(B,Y_S)|_M
\tag{2.4}
$$
满足
$$
\left(\prod_{j\in F}L_j\right)\mathfrak R_F=I_M,
$$
$$
\log^+\|\mathfrak R_F\|
\le K_0N^2+(2\kappa-1)rL_N+C_Mr+C.
\tag{2.5}
$$
完整主行在 $S$ 外的系数只影响固定 $B$ 和 $X_M$，
不使联合预解成本重复 $r$ 次。

## 3. 未选主尾为何不破坏高位平均

令 $J_F=\prod_{j\in F}M_{\chi_j}$，并只对 $F$ 内的
$R_j$ 作带帽符号改变。
带帽 $X$ 仍由完整 $X$ 加有限有界差定义；
带帽 $B$ 仍是整个主行的平方和。
准确差式依旧为
$$
\widehat B-B
=\sum_{j\in F}
16a_j^2(t_jN_j)^3(I-t_j^2N_j^2)^{-2}.
\tag{3.1}
$$
$S$ 外的项不在 (3.1) 的形式符号差中；
其真实物理反射误差由壳层估计完整计入。

具体地，[R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)
的最高物理位壳估计只使用
$$
a\in\ell^2,\qquad a^2\in\ell^1,\qquad c\in\ell^1.
$$
对完整主行、包括 $S$ 外的每个主系数，
原误差按最高位 $\ell\ge m_N$ 收集并用真实权比及 Cauchy–Schwarz 控制。
因此各阶 $\delta_X$ 导数仍有
$$
s!\epsilon_N,\qquad
\epsilon_N\le Ce^{-385\,16^{m_N-1}},
\tag{3.2}
$$
的统一界，常数不含 $\max F$。
任意稀疏 $S$ 不改变 (3.2)。

(3.1) 从 $N_j^3$ 开始，故无额外 Boolean 一次项。
对 $f_F=\mathfrak R_Ff\in M$，核内的差主项仍为
$$
8X\sum_Fa_jt_jN_j
+16\left(\sum_Fa_jt_jN_j\right)^2
+4\sum_Fc_jt_jN_j.
$$
其 $r$ 次幂的唯一无重复位项为
$$
r!t_FN_F\prod_{j\in F}L_j.
$$
其余项和全部实际反射误差按统一准则支付。
先在 $M$ 内用 (2.4) 消去乘积，再在左侧作用 $J_F$；
没有把 $\mathfrak R_F$ 穿过反射，也没有假设 $J_FM\subset M$。

故相同的平均
$$
\mathcal V_N=(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}t_F^{-1}J_F\mathfrak R_F
$$
满足完整自然幂域条件与
$$
T^r\mathcal V_Nf\rightharpoonup e^{-1/\theta}f
\quad(f\in M).
\tag{3.3}
$$
高位纯算子的统一范数控制只依赖位数 $Q_N$，
其有限柱弱极限只要求 $\min I_N\to\infty$。
这两个条件已由 (2.2) 保证，不要求选位构成物理连续窗口。

固定任意局部矩阵 $D$。
完整主行的固定物理低头仍可逐项合法移出 $A$，
闭尾仍与 $D$ 完整域交换。
所以同一四次估计给
$$
\|\operatorname{ad}_T^rD\,\mathcal V_Nf\|
\le C_{D,M,\theta}^r A_N
\exp[-5r^4/6+105r^3]\,\|f\|,
\tag{3.4}
$$
其中 $\log A_N\le K_0N^2+K_1rL_N+O(r\log(r+2))$。
由 $L_N=O(N^{3/2})$，
先固定足够小的 $\theta$，(3.4) 趋于零。

完整 $C$ 双线性配对及 (3.3) 遂给
$$
\mathcal B(Df,g)=0\qquad(f,g\in M,\ D\text{ 任意局部矩阵}).
$$
局部全矩阵代数不可约迫 $M=0$。
自然 $C$ 自伴性、图核心和实际作用恒等式给 (1.6)。
这证明的是完整主行的向量，不是仅在 $S$ 上截断的向量。

## 4. 只需对子行验证的四个具体条件

此前实际正锥、实阶乘、指数及头尾 Laplace 预算只涉及偏离行
$c_j$ 的幅度上界。
现在 $c$ 支撑在 $S$，因此这些证明可以直接按
$\rho_n^S$ 的标量排序进行，原物理算子仍保持不动。

于是 (1.6) 在下列任一条件下成立：

1. 对某个实数 $\sigma_S\ge1$，
   $$
   0<\limsup_{n\to\infty}n^{\sigma_S}\rho_n^S
   \le\sup_{n\ge1}n^{\sigma_S}\rho_n^S<\infty.
   $$
   $\sigma_S=1$ 为临界弱 $\ell^1$ 子行，$\sigma_S>1$ 为更快幂子行。
   实际圆周成本的幂为
   $2\sigma_S(\kappa-1)/(\kappa\sigma_S-1)\le2$。

2. 对固定 $0<\alpha\le1$，
   $$
   \rho_n^S\le B_ae^{-\beta_-n^\alpha},
   \qquad
   \rho_N^S\ge b_ae^{-\beta_+N^\alpha}
   $$
   沿无穷子序列有第二个不等式，
   其中 $0<\beta_-\le\beta_+$。
   实际圆周成本为 $O(N^{1+\alpha})$。

3. 沿无穷子序列，
   $$
   1+\log^+((\rho_N^S)^{-1})=O(N),
   \qquad
   \sum_{n>N}(\rho_n^S)^\kappa
   =o((\rho_N^S)^{2\kappa-2}).
   $$
   真实任意物理头加小范数尾的 Laplace 预算给
   $O(N\log(N+1)+NL_N+L_N^{4/3})=O(N^2)$。

第三条包含前稿的长平台子行：
取 $1/2<\sigma_S<1$、
整数 $p>\sigma_S(2\kappa-2)/(\kappa\sigma_S-1)$，
在 $N_{k-1}<n\le N_k$ 上令
$\rho_n^S=N_k^{-\sigma_S}$，$N_k=2^{p^k}$。
它本身可不属于弱 $\ell^1$。
以上四个具体分支是临界弱 $\ell^1$、更快幂、指数及尾间隙；
其外部背景均为任意完整 $\ell^2$ 主行。

## 5. 全支撑规则慢幂主行的新偏离子类

给定
$$
\frac12<\sigma<1,\qquad
a_j=\xi_j(j+1)^{-\sigma},\qquad |\xi_j|=1.
\tag{5.1}
$$
相位任意。
整个主行在 $\ell^2\setminus\ell^1$，
并且其全局排序不属于弱 $\ell^1$。

取
$$
j_k=\lceil k^{1/\sigma}\rceil-1,\qquad
S=\{j_k:k\ge1\}.
\tag{5.2}
$$
因为 $1/\sigma>1$，这些整数严格递增。
有
$$
2^{-\sigma}k^{-1}\le|a_{j_k}|\le k^{-1}.
\tag{5.3}
$$
故 $S$ 上的非零幅度排序满足临界弱 $\ell^1$ 条件。

取任意固定 $\gamma\ne0$ 及任意单位相位 $\omega_k$，令
$$
c_{j_k}=\gamma|a_{j_k}|^\kappa\omega_k,\qquad
c_j=0\quad(j\notin S).
\tag{5.4}
$$
若 $\kappa$ 是整数，也可取 $c_{j_k}=\gamma a_{j_k}^\kappa$。
任意 $a_*\in\mathbb C$、任意 $b\in\ell^2$ 和 $b_*\in\mathbb C$ 下，
定理给
$$
\boxed{
\left[
u^2+2\sum_{j\ge0}a_j^2(\chi_j-1)
+\gamma\sum_{k\ge1}|a_{j_k}|^\kappa\omega_k(\chi_{j_k}-1)
\right]e^w
\text{ 非零且循环}.
}
\tag{5.5}
$$

完整主行的每个慢系数仍被保留。
只在稀疏位置施加偏离，其他无限多个非零位置仍精确共振。

此处相位任意的统一陈述包含旧类，不能把其中的同射线分支重计为新发现。
若存在 $\theta$ 使
$\sum_j(|a_j|-\operatorname{Re}(e^{-i\theta}a_j))<\infty$，
R134/R138 的既有空谱与 R155 的有界辅助定理已经给出更强结论。

一个明确不落旧空谱接口的新例是取
$$
\xi_j=(-1)^j.
$$
对每个 $\theta$，偶数和奇数位上的相位缺陷分别带有
$1-\cos\theta$、$1+\cos\theta$ 两个非负因子。
两条子行的 $(j+1)^{-\sigma}$ 质量都发散，且这两个因子不同时为零，
所以全部相位方向的缺陷都发散。
R138 因而将这个完整主 first 归入全平面连续谱分支。
(5.5) 对它仍成立，且保留任意复指数权。
偏离行的非零排序满足
$$
|c|_k^*\asymp k^{-\kappa},
$$
所以它不是 R270E 的超三次快辅助；
(5.5) 不只是该已闭快类的重述。

这仍没有关闭同一规则慢幂行上
$|c_j|\asymp|a_j|^\kappa$ 对所有充分大物理位成立的全支撑情形。
新结论的量词清楚保留了 (5.2)–(5.4) 的偏离支撑限制。

## 6. 允许支撑外的独立快偏离

还可以在 $S^c$ 上加一个独立快行 $d$：
$$
d_j=0\quad(j\in S),\qquad d\in\ell^1,
$$
并假设实际
$$
D_{\rm fast}=\sum_{j\notin S}d_j(R_j-I)\in\mathcal G.
\tag{6.1}
$$
例如有限非零支撑，或
$-\log d_n^*/n^3\to\infty$，都由 R154 引理2.1 保证 (6.1)。

将
$$
B'=B-D_{\rm fast}\in\mathcal G.
$$
新的目标算子是
$$
X^2+Y_S-B'
=X^2+Y_S+D_{\rm fast}-B.
$$
它的核内平方关系、自然域及快系数预解预算完全相同。
因为选中的 $F\subset S$ 与 $d$ 的支撑不交，
带帽形式差准确有
$$
\widehat D_{\rm fast}-D_{\rm fast}=0.
$$
所以 $\widehat B'-B'$ 的 Boolean 一次项仍为零，
且三次主差仍恰为 (3.1)。
实际反射并不严格消去 $D_{\rm fast}$；
其余差由同一最高物理位壳估计支付，
使用 $d\in\ell^1$，成本仍为 (3.2)。
固定局部头中新增的 $d_j(R_j-I)$ 仍逐项具有真实 $A$ 因子。

故定理保持成立，目标向量在 (1.6) 基础上再加
$$
\left[\sum_{j\notin S}d_j(\chi_j-1)\right]e^w.
$$
本节不声称任意与 $S$ 重叠的快行都能无条件忽略：
重叠会改变选位的实际线性系数，须另外支付或重验下界。

## 7. R259 不能直接补全的剩余分歧

对全支撑规则慢幂 $\rho_n\asymp n^{-\sigma}$、
$1/2<\sigma<1$，现有实际共同圆周上界为
$$
\log\|z(z-Y)^{-1}\|
\lesssim
N^{\,2\sigma(\kappa-1)/(\kappa\sigma-1)}.
$$
该指数严格大于2。
当前 $r\asymp\sqrt N$ 的有界高位弱平均不能支付这个上界。
这说明当前预算不足，并非已证明实际预解必须如此大。

[R259](../results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)
排除的是
$X_b-\Phi(K_2,\ldots,K_d)$ 的原点解析分支核；
它没有给未知二次核 $M$ 上
$\|(X_M+\tau)^{-1}\|$ 的定量界。
当整数 $\kappa\ge3$ 且 $c_j=\gamma a_j^\kappa$ 时，
局部展开的确给
$$
Y=\frac{\gamma}{L_\kappa'(1)}K_\kappa+E,\qquad E\in\mathcal G,
$$
因为差的局部常数项和一次项同时消失。
但
$$
X_M^2=(B-Y)|_M
$$
在零字符处一般需要分歧平方根，不能无证写成一个原点解析
$\Phi(K_2,\ldots,K_d)$。
把已有的单射或循环结论称为这一核内统一预解界，也不成立。

本稿的支撑扩展绕开的是新增子类的选位量词；
它没有借此宣称全支撑分歧已消失，也没有把高提升的弱零列改称近单位。
