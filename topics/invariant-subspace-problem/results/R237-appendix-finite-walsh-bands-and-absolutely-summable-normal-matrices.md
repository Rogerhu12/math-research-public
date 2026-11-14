# R237 附录：实际有限 Walsh 翻转带、绝对可和正常矩阵及表示边界

日期：2026-11-12（UTC）。独占作者：literature。

本稿以 [R237 完整对角右模](../notes/2026-11-12-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion-0c-agent.md) 为已证输入。所有局部矩阵和尾逆均为原 Haar 表示中的真实算子，保留 dyadic carry。下文不使用纯平方零模型来替代实际矩阵元。

## 1. 结论及范围

记 $\mathfrak F$ 为非负整数的有限子集全体，$\{\chi_F:F\in\mathfrak F\}$ 为原 Haar 空间 $H$ 的 Walsh 正交基。内积对第一变量线性。对迹类算子 $\rho$，定义其 Walsh 矩阵绝对和
$$
\|\rho\|_{\mathrm{ent}}
=\sum_{F,G\in\mathfrak F}
|\langle\rho\chi_G,\chi_F\rangle|
\quad\text{（允许为无穷）}.
\tag{1.1}
$$

**主结论。** 对两种实际慢符号
$$
S_N=\sum_{j\ge0}(j+1)^{-2}N_j,\qquad
S_Y=\sum_{j\ge0}(j+1)^{-2}N_j(I+N_j)^{-1},
\tag{1.2}
$$
若 $\|\rho\|_{\mathrm{ent}}<\infty$ 且
$$
\operatorname{Tr}(\rho S_\bullet F)=0
\quad(F\in\mathcal A),
\tag{1.3}
$$
则
$$
\boxed{
\operatorname{Tr}(\rho T)=0\quad(T\in\{A\}'),
\qquad \operatorname{Tr}\rho=0.
}
\tag{1.4}
$$
所以此类中非零的 Hilbert 正迹类算子不能湮灭相应主理想。

这覆盖：

1. 相对于有限个固定 Walsh 翻转差具有有限带宽的全部迹类算子，没有次数或最高位尾率要求；
2. 全部 Walsh 矩阵绝对可和的迹类算子，包括许多无限带宽、无限秩算子；
3. $\rho=|f\rangle\langle f|$ 且 $\sum_F|\widehat f(F)|<\infty$ 的全部非零向量态，以及满足相应绝对和预算的可数正和。

对非对角复迹类算子，(1.4) **不推出** $\rho=0$：非零正常泛函可以在交换子代数上恒零。只有加上 $\rho\ge0$ 后，零迹才迫密度为零。

此外，第7节证明把任意正常泛函化成对角 $\ell^1$ 泛函的映射不可能在全迹类空间上存在并保持这个表示性质。它不构造慢符号的正常湮灭者，只精确说明当前转移方法的边界。

## 2. 需要的真实局部右模

在第 $j$ 位的 Walsh 坐标 $(1,\chi_j)$ 中，置
$$
t_j=\eta_jN_{j+1},\qquad
s_j=(I+t_j)(I-t_j)^{-1}.
$$
其中
$$
N_j^2=\eta_jN_{j+1},\qquad
\|N_j\|=1,\qquad
0<\eta_j\le e^{-770\,16^j}.
\tag{2.1}
$$
令 $H_j$ 为第 $j$ 位起的尾空间，$\mathscr C_j=\{N_j\}'$。
R237 的真实分块恒等式为
$$
T=\begin{pmatrix}A&B\\-B&D\end{pmatrix}\in\mathscr C_j,
\qquad
A,D,B\in\mathscr C_{j+1},
\qquad
B=\frac12s_j^{-1}(A-D).
\tag{2.2}
$$
这里 $s_j$ 与这些块交换，且 $\|A\|,\|D\|\le\|T\|$。

R237 在 $\ell^1(\mathfrak F_j)$ 上构造了递归算子 $\widehat N_j$，满足
$$
\|\widehat N_j\|_{\ell^1\to\ell^1}\le\frac35,\qquad
\widehat N_j^2=\eta_j\widehat N_{j+1},
$$
并对
$$
\Lambda_j(p)(T)=\sum_{F\in\mathfrak F_j}
p_F\langle T\chi_F,\chi_F\rangle
$$
有精确右模式
$$
\Lambda_j(\widehat N_jp)(T)=\Lambda_j(p)(N_jT).
\tag{2.3}
$$
此等式在实际侧和模侧都范数收敛的解析级数下保留。

特别定义真实尾逆的模作用
$$
K_j=(I-\eta_j\widehat N_{j+1})
(I+\eta_j\widehat N_{j+1})^{-1}.
\tag{2.4}
$$
两个逆的 Neumann 级数分别由 $\eta_j<1$、
$\eta_j\|\widehat N_{j+1}\|<1$ 保证范数绝对收敛。于是
$$
\boxed{
\Lambda_{j+1}(K_jp)(R)
=\Lambda_{j+1}(p)(s_j^{-1}R)
\quad(R\in\mathscr C_{j+1}).
}
\tag{2.5}
$$
并有
$$
\|K_j\|_{\ell^1\to\ell^1}
\le k_j:=\frac{1+(3/5)\eta_j}{1-(3/5)\eta_j}.
\tag{2.6}
$$
由于 $\eta_j<1/100$，
$$
\log k_j\le2\eta_j,\qquad
\kappa:=\prod_{j\ge0}k_j
\le\exp\left(2\sum_j\eta_j\right)<2.
\tag{2.7}
$$
最后一个有限常数与翻转集合的大小和位置无关。

## 3. 固定有限翻转差的完整递归

对有限 $D\subset[j,\infty)$ 和 $p\in\ell^1(\mathfrak F_j)$，定义
$$
\Phi_{j,D,p}(T)
=\sum_{F\in\mathfrak F_j}
p_F\langle T\chi_F,\chi_{F\triangle D}\rangle.
\tag{3.1}
$$
该级数绝对收敛，泛函范数至多 $\|p\|_1$。

**命题3.1。** 存在有界线性映射
$$
\mathscr R_{j,D}:\ell^1(\mathfrak F_j)\longrightarrow
\ell^1(\mathfrak F_j)
$$
使
$$
\boxed{
\Phi_{j,D,p}(T)
=\Lambda_j(\mathscr R_{j,D}p)(T)
\quad(T\in\mathscr C_j),
}
\tag{3.2}
$$
并满足
$$
\|\mathscr R_{j,D}\|
\le\prod_{i\in D}k_i\le\kappa.
\tag{3.3}
$$
对于 $D=\varnothing$，可以且取 $\mathscr R_{j,\varnothing}=I$。

**证明。** 选任意 $r>\max D$；若 $D$ 为空，无需递归。
在第 $r$ 位以后取恒等映射。对 $j=r-1,r-2,\ldots$ 逐层向下构造。
在当前位把 $p$ 分成 $(p_0,p_1)$，这里下标表示输入集合是否包含当前位；
两者都是完整无限尾上的 $\ell^1$ 序列。

先记
$$
D'=D\cap[j+1,\infty),\qquad
R=\mathscr R_{j+1,D'}.
$$

若 $j\notin D$，输入与输出在当前位相同。由 (2.2)，
$$
\Phi_{j,D,p}(T)
=\Phi_{j+1,D',p_0}(A)+\Phi_{j+1,D',p_1}(D).
$$
故定义
$$
\mathscr R_{j,D}(p_0,p_1)=(Rp_0,Rp_1).
\tag{3.4}
$$
这一层没有额外范数成本。

若 $j\in D$，输入位 $0$、输出位 $1$ 的块是 $-B$；
输入位 $1$、输出位 $0$ 的块是 $B$。因此
$$
\Phi_{j,D,p}(T)
=\Phi_{j+1,D',p_1-p_0}(B).
\tag{3.5}
$$
先使用已经构造好的**尾翻转转移**，置
$$
q=R(p_1-p_0).
$$
此时 (3.5) 已成为对角尾泛函 $\Lambda_{j+1}(q)(B)$。
然后才使用真实尾逆的右模式 (2.5)：
$$
\begin{aligned}
\Lambda_{j+1}(q)(B)
&=\frac12\Lambda_{j+1}(q)\bigl(s_j^{-1}(A-D)\bigr)\\
&=\frac12\Lambda_{j+1}(K_jq)(A-D).
\end{aligned}
$$
于是定义
$$
\boxed{
\mathscr R_{j,D}(p_0,p_1)
=\left(\frac12K_jR(p_1-p_0),
-\frac12K_jR(p_1-p_0)\right).
}
\tag{3.6}
$$
这两个对角输出的 $\ell^1$ 范数之和为
$\|K_jR(p_1-p_0)\|_1$，所以该层成本至多 $k_j$。

有限次递归给 (3.2)—(3.3)。递归顺序固定为：
**先处理尾部仍存在的翻转，再让已经对角化的尾泛函右乘 $s_j^{-1}$。**
没有假设 $R$ 与 $K_j$ 交换。

终端 $r$ 只是“剩余翻转为空”的位置，不是把真实高尾截成零。
即使原始 $p$ 是单个有限矩阵单位，$K_j$ 也可以产生任意高位的新权重；
这些权重由其完整 $\ell^1$ 算子范数控制。
因此高于 $\max(F\cup G)$ 的真实 carry 已包含在 (2.4)—(2.5) 中。
证毕。

取 $T=I$ 立即得到准确迹恒等式
$$
\sum_F(\mathscr R_{j,D}p)_F
=\begin{cases}
\sum_Fp_F,&D=\varnothing,\\
0,&D\ne\varnothing.
\end{cases}
\tag{3.7}
$$
这不是由估计推断的近似保迹。

在全空间记 $\mathscr R_D=\mathscr R_{0,D}$。
R237 已证明 $\Lambda=\Lambda_0$ 在 $\ell^1$ 上、甚至只在 $\mathcal A$ 测试时单射。
因此任何满足 (3.2) 的 $\ell^1$ 输出都是唯一的；
不同的冗余终端选择不会改变该输出。

## 4. 绝对可和矩阵的真实对角表示

对 $\rho$ 令
$$
p_F^D=\langle\rho\chi_{F\triangle D},\chi_F\rangle.
\tag{4.1}
$$
若 $\|\rho\|_{\mathrm{ent}}<\infty$，则
$$
\sum_D\|p^D\|_1=\|\rho\|_{\mathrm{ent}}.
\tag{4.2}
$$
定义
$$
q_\rho=\sum_{D\in\mathfrak F}\mathscr R_Dp^D.
\tag{4.3}
$$
(3.3) 保证该级数在 $\ell^1$ 中绝对收敛，且
$$
\boxed{
\|q_\rho\|_1\le\kappa\|\rho\|_{\mathrm{ent}}.
}
\tag{4.4}
$$

对应的每条带为
$$
\rho_D=\sum_Fp_F^D|\chi_F\rangle\langle\chi_{F\triangle D}|.
$$
其迹类范数是 $\|p^D\|_1$，因为它是对角算子乘以一个酉 Walsh 翻转。
所以 $\rho=\sum_D\rho_D$ 在迹类范数中绝对收敛。
按本稿的内积约定，
$$
\operatorname{Tr}(\rho_DT)=\Phi_{0,D,p^D}(T).
$$
逐项应用 (3.2)，得到
$$
\boxed{
\operatorname{Tr}(\rho T)=\Lambda(q_\rho)(T)
\quad(T\in\{A\}').
}
\tag{4.5}
$$
特别由 $T=I$，
$$
\boxed{\sum_F(q_\rho)_F=\operatorname{Tr}\rho.}
\tag{4.6}
$$
$q_\rho$ 通常为复序列；即使 $\rho\ge0$，也不声称 $q_\rho\ge0$。

## 5. 主理想湮灭的结论

若 (1.3) 成立，则 (4.5) 给
$$
\Lambda(q_\rho)(S_\bullet F)=0\quad(F\in\mathcal A).
$$
R237 的主定理适用于**任意复** $\ell^1$ 对角权重，故 $q_\rho=0$。
由 (4.5)—(4.6)，得到 (1.4)。

若另有 $\rho\ge0$，则 $\operatorname{Tr}\rho=0$ 迫 $\rho=0$。
这一步才使用正性；前面的实际递归和表示均为复线性论证。

这个推理不要求 $\rho S_\bullet$ 自伴，也不要求湮灭理想对 UHF 左乘稳定。
实际使用的测试代数始终是 $\mathcal A\subset\{A\}'$。

## 6. 有限带宽、向量态及严格扩大范围

### 6.1 任意迹类算子的单带控制

令 $W_D\chi_F=\chi_{F\triangle D}$，则 $W_D$ 是自伴酉算子。
$p^D$ 是迹类算子 $\rho W_D$ 的 Walsh 对角，所以
$$
\boxed{\|p^D\|_1\le\|\rho\|_1.}
\tag{6.1}
$$
一个自含证明是：在任意有限对角集合上选择模为一的相位使对角和变成绝对值和；
相应有限对角算子范数至多一，迹对偶给该有限和不超过 $\|\rho W_D\|_1$。
随后令有限集合增加即可。

假定存在有限集合 $\mathcal D\subset\mathfrak F$，使
$$
\langle\rho\chi_G,\chi_F\rangle=0
\quad\text{只要 }F\triangle G\notin\mathcal D.
$$
则
$$
\|\rho\|_{\mathrm{ent}}
=\sum_{D\in\mathcal D}\|p^D\|_1
\le|\mathcal D|\,\|\rho\|_1<\infty.
\tag{6.2}
$$
因此有限 Walsh 翻转带宽的全部正迹类密度均在排除范围内。
不要求每条带的支撑包含在某个固定有限头，也不要求有限秩。

### 6.2 Walsh 系数绝对可和的向量态

若 $f,g$ 的 Walsh 系数绝对可和，则
$$
\bigl\||f\rangle\langle g|\bigr\|_{\mathrm{ent}}
=\left(\sum_F|\widehat f(F)|\right)
 \left(\sum_G|\widehat g(G)|\right).
\tag{6.3}
$$
特别任意非零这样的 $f$，其正常向量态都不能湮灭 $S_\bullet\mathcal A$。
若 $\rho=\sum_\nu|f_\nu\rangle\langle f_\nu|$ 且
$$
\sum_\nu\left(\sum_F|\widehat f_\nu(F)|\right)^2<\infty,
$$
同样适用。

取互不相交的有限集合 $F_n$、$|F_n|=n$，以及
$$
f=\sum_{n\ge1}\frac{1}{n^2}\chi_{F_n}.
$$
则 $f$ 的 Walsh 系数绝对可和，但对每个 $r>1$，
$$
\|r^{\mathsf N}f\|^2
=\sum_{n\ge1}\frac{r^{2n}}{n^4}=\infty.
$$
所以其正秩一密度不在 R230 的次数指数矩类中。
同时 $\langle f,1\rangle=0$，故 $|f\rangle\langle f|\,1=0$；
非零且保函数正锥的算子不能杀死常函数 $1$，因此它也不在 R235 的保锥类中。
本附录仍排除它成为两种慢符号的正常湮灭者。

这只是此主理想的正常态排除；没有从该结论额外宣称 $f$ 的整个 $A$ 循环子空间必为 $H$。

## 7. 为什么不能按迹范数逼近扩到任意正常态

这里给出上述转移映射在原实际模型上的明确无界成本。
这既避免把有限矩阵逼近当成缺失的统一估计，也不引入慢符号的反例。

取固定整数 $r$ 和远端长度 $r$ 的区块
$$
K=\{m,m+1,\ldots,m+r-1\},
$$
令
$$
v_K=\bigotimes_{j\in K}\frac{1+i\chi_j}{\sqrt2}
$$
并在区块外取参考真空。$\|v_K\|=1$，其 Walsh 支撑有限。
置 $\rho_K=|v_K\rangle\langle v_K|$，
则 $\|\rho_K\|_1=\operatorname{Tr}\rho_K=1$；
第4节给唯一的对角代表 $q_K\in\ell^1$。

使用 R237 的精确测试
$$
J_j=2N_j(I+N_j^2)^{-1}.
$$
由 $N_j-E_j=\eta_jE_j^*N_{j+1}$，
$$
\|J_j-2E_j\|
\le\frac{4\eta_j}{1-\eta_j}\le5\eta_j,
\qquad \|J_j\|\le3.
\tag{7.1}
$$
对模式 $\sigma\in\{\pm1\}^K$，置
$$
Q_{K,\sigma}=\prod_{j\in K}\frac{I+\sigma_jJ_j}{2},
\qquad
Q^0_{K,\sigma}=\prod_{j\in K}\frac{I+\sigma_j2E_j}{2}.
$$
每个实际或纯因子范数至多 $2$，单因子误差至多 $3\eta_j$。
置 $\varepsilon_m=e^{-770\,16^m}$，则 $\sup_{j\ge m}\eta_j\le\varepsilon_m$，不另假定 $\eta_j$ 单调。
有限乘积 telescoping 给
$$
\|Q_{K,\sigma}-Q^0_{K,\sigma}\|
\le3r\,2^{r-1}\varepsilon_m.
\tag{7.2}
$$
纯局部向量满足
$\langle2E_j(1+i\chi_j)/\sqrt2,(1+i\chi_j)/\sqrt2\rangle=i$，
故
$$
\langle Q^0_{K,\sigma}v_K,v_K\rangle
=\prod_{j\in K}\frac{1+\sigma_ji}{2},
\qquad
\sum_\sigma
|\langle Q^0_{K,\sigma}v_K,v_K\rangle|
=2^{r/2}.
\tag{7.3}
$$

另一方面，实际 $Q_{K,\sigma}$ 的 Walsh 对角恰为对应区块模式的示性函数。
由 (4.5)，
$$
\langle Q_{K,\sigma}v_K,v_K\rangle
=\sum_{F:\,(-1)^{1_{j\in F}}=\sigma_j\ (j\in K)}(q_K)_F.
$$
这些模式把全部配置分成互不相交的集合，所以
$$
\begin{aligned}
\|q_K\|_1
&\ge\sum_\sigma|\langle Q_{K,\sigma}v_K,v_K\rangle|\\
&\ge2^{r/2}-3r\,2^{2r-1}\varepsilon_m.
\end{aligned}
\tag{7.4}
$$
每个固定 $r$ 都可令 $m$ 足够大，使最后误差不超过一。因此
$$
\boxed{
\|\rho_K\|_1=1,\qquad
\|q_K\|_1\ge2^{r/2}-1.
}
\tag{7.5}
$$
不存在只依赖迹范数的统一 $\ell^1$ 对角表示界。

事实上，并非所有正常泛函都存在这样的 $\ell^1$ 代表。
若全迹类空间上的每个 $\rho$ 都存在 $q_\rho\in\ell^1$ 满足 (4.5)，
R237 的注入性使代表唯一，因而映射 $\rho\mapsto q_\rho$ 为线性。
若 $\rho_n\to\rho$ 于迹范数且 $q_{\rho_n}\to q$ 于 $\ell^1$，
分别在 (4.5) 的两边取极限，就得到 $q=q_\rho$。
该映射因而具有闭图，闭图定理迫它有界，与 (7.5) 矛盾。

如果每个正迹类算子都有这样的代表，则每个复迹类算子写成四个正迹类算子的复线性组合后也有代表，同样矛盾。
所以存在正常正态无法通过本附录的 $\ell^1$ 对角表示处理。
这并不说该正常正态湮灭 $S_N$ 或 $S_Y$ 的主理想。


障碍还能严格加强到正秩一正常态。假设每个 $|f\rangle\langle f|$ 都有这样的 $\ell^1$ 代表。
由复极化
$$
|f\rangle\langle g|
=\frac14\sum_{k=0}^3 i^k
|f+i^kg\rangle\langle f+i^kg|,
$$
每个秩一算子都有代表，记为 $q(f,g)$。注入性使它对 $f$ 线性、对 $g$ 共轭线性。
固定 $g$ 后，若 $f_n\to f$ 于 $H$、$q(f_n,g)\to q$ 于 $\ell^1$，
则
$$
\bigl\||f_n\rangle\langle g|-|f\rangle\langle g|\bigr\|_1
\le\|f_n-f\|\,\|g\|\to0,
$$
取测试极限和注入性给 $q=q(f,g)$。闭图定理说明 $f\mapsto q(f,g)$ 有界。
对另一变量同样成立；将共轭变量视为共轭 Hilbert 空间即可使用复线性闭图定理。

于是这个处处定义的双线性映射分别连续。
对算子族 $\{f\mapsto q(f,g):\|g\|\le1\}$ 使用一致有界原理，
得到固定常数 $C$ 使
$$
\|q(f,g)\|_1\le C\|f\|\,\|g\|.
$$
取 $f=g=v_K$ 与 (7.5) 矛盾。因此
$$
\boxed{
\text{至少存在一个正秩一正常态，没有满足 (4.5) 的 }\ell^1\text{ 对角代表。}
}
\tag{7.6}
$$
这仍然不是慢符号的正常湮灭者反例；它只排除“所有有限秩都可由当前对角模处理”的无条件延拓。


### 7.1 一个明确的 $C$ 实正秩一例子

上面的存在性障碍可以写成原 Haar 空间中的具体向量。
令
$$
r_n=8n,\qquad m_n=16n^2,\qquad
K_n=[m_n,m_n+r_n)\cap\mathbb N_0,
$$
$$
v_n=\bigotimes_{j\in K_n}\frac{1+i\chi_j}{\sqrt2},
\qquad
\delta_n=2^{-r_n/2},\qquad
w_n=v_n-\delta_n1,
\qquad
f=\sum_{n\ge1}2^{-n}w_n.
\tag{7.7}
$$
各 $K_n$ 互不相交，$\langle w_n,1\rangle=0$，
$\|w_n\|^2=1-\delta_n^2$。
因此 $w_n$ 两两正交，级数在 $H$ 中收敛，并且
$$
0<\|f\|^2=\sum_{n\ge1}4^{-n}(1-\delta_n^2)<\frac13.
\tag{7.8}
$$
原共轭满足 $C\chi_F=(-1)^{|F|}\chi_F$ 并对标量反线性，
所以 $Cv_n=v_n$、$Cw_n=w_n$、$Cf=f$。

固定 $n$，写 $f=2^{-n}w_n+h_n$。
$h_n$ 只使用 $K_n$ 外的变量，且均值为零。
纯测试 $Q^0_{K_n,\sigma}$ 只作用于 $K_n$，所以交叉项精确消失，得到
$$
\langle Q^0_{K_n,\sigma}f,f\rangle
=4^{-n}\langle Q^0_{K_n,\sigma}w_n,w_n\rangle
+\|h_n\|^2\mathbf1_{\{\sigma\equiv+1\}}.
\tag{7.9}
$$
这一步只用于计算纯测试，随后仍支付完整实际误差。

局部两种符号的矩阵直接给
$$
\sum_{\sigma\in\{\pm1\}^{K_n}}
|\langle Q^0_{K_n,\sigma}v_n,1\rangle|
=
\sum_{\sigma\in\{\pm1\}^{K_n}}
|\langle Q^0_{K_n,\sigma}1,v_n\rangle|
=
\left(\frac{\sqrt5+1}{2\sqrt2}\right)^{r_n}.
$$
置 $\theta=(\sqrt5+1)/4<1$，由 $w_n=v_n-\delta_n1$ 和 (7.3)，
$$
\sum_\sigma
|\langle Q^0_{K_n,\sigma}w_n,w_n\rangle|
\ge2^{r_n/2}-2\theta^{r_n}-\delta_n^2
\ge2^{r_n/2}-3.
\tag{7.10}
$$
结合 (7.9)，纯测试的总变差至少为
$$
4^n-3\cdot4^{-n}-\|h_n\|^2>4^n-1.
\tag{7.11}
$$
最后的不等式可由
$\|h_n\|^2<1/3-4^{-n}(1-\delta_n^2)$ 直接检查；
其误差小于 $1/3+4^{-n}(2+\delta_n^2)<1$。

由 (7.2)，实际与纯测试在这个固定向量上的总误差至多
$$
3r_n\,2^{2r_n-1}\varepsilon_{m_n}\|f\|^2<1.
$$
这里 $2r_n=16n$，而
$\varepsilon_{m_n}=\exp(-770\cdot2^{64n^2})$，
所以这个严格界对每个 $n\ge1$ 都成立。
因而
$$
\boxed{
\sum_{\sigma\in\{\pm1\}^{K_n}}
|\langle Q_{K_n,\sigma}f,f\rangle|>4^n-2
\longrightarrow\infty.
}
\tag{7.12}
$$

如果 $|f\rangle\langle f|$ 有 (4.5) 所要求的某个 $q\in\ell^1$，
实际 $Q_{K_n,\sigma}$ 的准确 Walsh 示性对角会使左侧对每个 $n$ 都不超过 $\|q\|_1$，
与 (7.12) 矛盾。
归一化 $f/\|f\|$ 因此给出一个**明确的 $C$ 实正秩一正常态**，
它没有当前 $\ell^1$ 对角表示。

这个向量不是慢符号主理想湮灭者的构造；本段只证明指定表示机制失效。


### 7.2 这个明确向量实际已经循环

对 (7.7) 取互不相交块 $K_n$ 上的零均值符号
$f_n=2^{-n}w_n$。
它们满足 $\sum_n\|f_n\|^2<\infty$。
每个非空 $F\subset K_n$ 的 Walsh 系数绝对值为
$2^{-n}2^{-r_n/2}$。
因此 [R136](../notes/2026-11-12-disjoint-block-carleman-cyclicity-0c-agent.md)
的实际 carry 充分条件 (1.7) 在这里被明确估计为
$$
\begin{aligned}
&\sum_n\sum_{\varnothing\ne F\subset K_n}
|\widehat f_n(F)|\,8^{|F|}\sum_{j\in F}\eta_j\\
&\quad\le
\sum_n2^{-n}2^{-r_n/2}\varepsilon_{m_n}
\sum_{F\subset K_n}|F|8^{|F|}\\
&\quad=
\sum_n2^{-n}2^{-r_n/2}\,
8r_n9^{r_n-1}\varepsilon_{m_n}<\infty.
\end{aligned}
\tag{7.13}
$$
这里使用真实范数差的已证条件，并未把纯块循环性直接迁移。
R136 主定理因而给
$$
\boxed{\operatorname{cyc}_A(f)=H.}
\tag{7.14}
$$

两种实际 $S_N,S_Y$ 均已由 R122 的有限解析 gauge 增量判据证明值域稠密。
若这个特定向量态湮灭 $S_\bullet\mathcal A$，
则 $f$ 与 $S_\bullet\operatorname{cyc}_A(f)$ 正交；
后者稠密于 $H$，迫 $f=0$，与 (7.8) 矛盾。
所以 (7.7) 的明确正常态**确定不是**慢符号主理想的湮灭者。
它只是一个已经循环、却无法由当前 $\ell^1$ 对角表示处理的具体向量。

## 8. 当前闭合与仍开的边界

实际有限翻转的尾逆成本已经完整支付；其常数来自所有 $\eta_j$ 的可和性，
不是来自丢弃 carry。固定有限带宽与矩阵绝对可和类由此闭合。

一般正常正态、任意有限秩见证及最小秩零子商仍未排除。
第7节说明把任意迹类都压成当前 $\ell^1$ 对角右模的统一延拓不可行；
它不排除另一种更大的模、针对特定慢符号的弱估计，或只对湮灭者成立的额外正性结构。
