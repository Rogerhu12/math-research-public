# R236 附录：固定盘核内逆与稀疏线性偏离

日期：2026-11-13（UTC）。状态：已证明；一般首偏离较晚的纯高阶分支仍开放。
完整证明见[固定盘逆、独立辅助与遗漏首位的慢背景](../notes/2026-11-13-fixed-disk-kernel-inverses-and-sparse-linear-deviations-central-review.md)。

## 1. 新充分条件

取任意复 $a,b\in\ell^2$、$c\in\ell^1$，置
$$
u=a_*+\sum a_j\chi_j,\quad w=b_*+\sum b_j\chi_j,\quad
R_j=V(e^{-2b_j}N_j),\quad X=X_b,
$$
$$
Y=\sum c_j(R_j-I),\quad
B=\sum a_j^2(R_j-I)^2,\quad
T=X^2+Y-B,\quad\operatorname{Dom}T=\operatorname{Dom}X^2.
$$
假设存在无限 $S\subseteq\{j:c_j\ne0\}$ 和 $K<\infty$，
使充分高的 $j\in S$ 满足
$$
|a_j/c_j|\le K.
\tag{1.1}
$$
允许 $a_j=0$，此时比值为0。
把 $S$ 上 $|c_j|$ 非增重排为 $\rho_N^{c,S}$，并沿无穷子序列要求
$$
L_N=1+\log^+((\rho_N^{c,S})^{-1})=O(N^{3/2}).
\tag{1.2}
$$

**定理。** 在 (1.1)–(1.2) 下，$T$ 单射稠密，且
$$
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w
$$
非零循环。$S^c$ 上的主行与辅助行分别可为任意 $\ell^2$、$\ell^1$ 行。
无需全空间 first 空谱，也无需 $Y$ 的全空间共同圆预解预算。

## 2. 同一未知核上的准确逆

R176 的自然域、完整 $C$ 自伴和图核心给
$$
M=\ker T\subset\bigcap_n\operatorname{Dom}X^n,\qquad
X_M\in B(M),\qquad X_M^2=(B-Y)|_M.
$$
$B-Y$ 字符为零，故限制仍拟幂零，$r(X_M)=0$。
对每个固定参数盘，真实 Neumann 级数
$$
(I+zX_M)^{-1}=\sum_{n\ge0}(-zX_M)^n
$$
一致绝对范数收敛。因此
$$
C_M:=\sup_{|z|\le2K}\|(I+zX_M)^{-1}\|<\infty.
$$
实际反射一次系数
$$
L_j=8a_jX_M+4c_jI_M
=4c_j(I_M+2(a_j/c_j)X_M)
$$
在同一个 $M$ 上可逆，且
$$
\|L_j^{-1}\|\le C_M/(4|c_j|),\qquad
\mathfrak R_F=\prod_{j\in F}L_j^{-1}.
\tag{2.1}
$$
这些逆与所有核内系数交换。不在全 $H$ 上求逆，也不除以 $a_j$。
$C_M$ 可以依赖假想核，但只产生 $O(|F|)$ 的对数成本。

## 3. 辅助和主行可有不同排序

从 $S$ 上最大的 $N$ 个辅助幅度中，删除完整主行最大的
$\lfloor N/4\rfloor$ 个幅度所在位，再删除物理位小于
$m_N=\lfloor N/4\rfloor$ 的项。剩下可选
$$
|I_N|=Q_N=\lfloor N/2\rfloor,\quad
\min I_N\ge m_N,\quad |c_j|\ge\rho_N^{c,S},\quad
|a_j|\le2\|a\|_2/\sqrt N.
$$
固定小 $\theta>0$、$r=\lceil\sqrt{N/\theta}\rceil$。
每个 $r$ 元 $F\subset I_N$ 满足
$$
\sum_F|a_j|=O_\theta(1),\quad
\sum_F|a_j|^2=O_\theta(N^{-1/2}),\quad
\sum_F|c_j|\le\sum_{j\ge m_N}|c_j|\to0,
$$
以及
$$
\log^+\|\mathfrak R_F\|\le rL_N+C'_Mr.
\tag{3.1}
$$
物理首位、主幅度排序和辅助幅度排序从未混同。

## 4. 完整实际域、carry 和弱平均

R260 的真实高位壳只用 $a\in\ell^2$、$a^2,c\in\ell^1$，
所以全部反射导数误差仍为
$$
s!\epsilon_N,\qquad \epsilon_N\le C e^{-385\,16^{m_N-1}},
$$
不含最大物理位成本。所有 $J_F$ 保持真实深域。

只在 $F$ 内改参数符号，精确有
$$
\widehat B-B
=\sum_{j\in F}16a_j^2(t_jN_j)^3(I-t_j^2N_j^2)^{-2},
\quad t_j=e^{-2b_j}.
$$
因此它没有 Boolean 一次项。
在同一 $M$ 上，主反射差为
$$
8X\sum_Fa_jt_jN_j+
16\left(\sum_Fa_jt_jN_j\right)^2+
4\sum_Fc_jt_jN_j.
$$
其 $r$ 次幂的不同位全列准确为
$r!t_FN_F\prod_FL_j$。
先在 $M$ 内以 (2.1) 消去乘积，再把 $J_F$ 放在左侧；
不将 $J_F$ 或核内逆任意交换。

原平均
$$
\mathcal V_N=(-1)^r(2/Q_N)^r
\sum_{|F|=r}t_F^{-1}J_F\mathfrak R_F
$$
满足 $\log^+\|\mathcal V_N\|\le rL_N+O_M(r)$。
真实重复位 carry 支付后，
$$
T^r\mathcal V_Nf\rightharpoonup e^{-1/\theta}f
\qquad(f\in M).
\tag{4.1}
$$
纯提升始终使用全空间有界的 $r\asymp\sqrt N$ 区间。

对每个固定局部全矩阵 $D$，有限头保真实 $A$ 因子，
完整双侧导子界给
$$
\|(\operatorname{ad}_T^rD)\mathcal V_Nf\|
\le2\|D\|A_NC_{D,M,\theta}^r
 e^{-5r^4/6+105r^3}\|f\|,
\quad \log^+A_N\le rL_N+O_M(r).
\tag{4.2}
$$
若 $L_N\le C_LN^{3/2}$，
则 $\limsup\log A_N/r^4\le C_L\theta^{3/2}$。
先固定足够小的 $\theta$，(4.2) 趋零。
自然域 Leibniz 与完整 $C$ 配对使
$\mathcal B(Df,g)=0$ 对所有局部全矩阵成立，迫 $M=0$。
图核心给所述实际向量的循环性。

## 5. 首偏离较晚的独立例

取
$$
a_j=(-1)^j(j+1)^{-\sigma},\quad \tfrac12<\sigma<1,
\qquad S=\{2^k-1:k\ge1\},
$$
固定 $\kappa>2$、非零 $\beta,\gamma$ 及任意单位相位 $\omega_j$。
令
$$
c_j=
\begin{cases}
0,&j=0,\\
\gamma a_j,&j\in S,\\
\beta |a_j|^\kappa\omega_j,&j\ge1,\ j\notin S.
\end{cases}
$$
则 $c\in\ell^1$，$j_a=0<j_c=1$。
在 $S$ 上 $a_j/c_j=\gamma^{-1}$、
$\rho_N^{c,S}=|\gamma|2^{-\sigma N}$，满足新条件。
因此该输入对所有复 $\ell^2$ 指数权非零循环。

完整主 first 按 R138 属全平面连续谱；
辅助在密度1的剩余位置保慢幂，不是超三次快类。
首位遗漏又使它不属于[首支撑有序定理](R236-appendix-earliest-support-dyadic-quadratic-cyclicity.md)。
这给新核内逆准则的独立范围。

若删去稀疏线性偏离，令 $c_0=0$ 而其余全为
$\beta|a_j|^\kappa\omega_j$，则所有无限子集上 $|a_j/c_j|\to\infty$，
固定盘条件失败。不能把 $C_M$ 免费用于随 $N$ 增大的盘。
该纯高阶首位遗漏情形及一般 ISP 保持开放。
