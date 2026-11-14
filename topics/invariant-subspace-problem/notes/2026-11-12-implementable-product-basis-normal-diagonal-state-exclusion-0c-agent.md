# R237 补充：任意可实现正交乘积基的正常对角态

日期：2026-11-12（UTC）。独占作者：literature。

本稿在 [R237 实际对角右模](../notes/2026-11-12-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion-0c-agent.md) 和
[实际有限翻转附录](../notes/2026-11-12-actual-finite-walsh-bands-and-absolutely-summable-normal-matrices-0c-agent.md) 之后，直接改变对角所依据的正交乘积基。
证明重新构造真实右模，不把一般乘积向量先压到原 Walsh 对角 $\ell^1$ 模。
所有 carry 均保留。

## 1. 可实现乘积基及主结论

在原 Haar 空间的每个 Walsh 位 $(1,\chi_j)$ 上，取
$$
h_{j,0}=\mu_j1+\nu_j\chi_j,\qquad
h_{j,1}=-\overline{\nu_j}\,1+\mu_j\chi_j,
$$
$$
\mu_j=(1-|\nu_j|^2)^{1/2}\ge0,\qquad
\sum_j|\nu_j|^2<\infty.
\tag{1.1}
$$
允许任意有限多个局部位另作相位或正交基调整；这些只改变有限头。
对有限 $F\subset\mathbb N_0$，记
$$
h_F=\bigotimes_{j\notin F}h_{j,0}
\otimes\bigotimes_{j\in F}h_{j,1}.
\tag{1.2}
$$
这些是原 $H$ 中的向量，且构成正交基。

为完整支付这个实现，令 $U_m$ 是前 $m$ 个局部酉矩阵的张量积、尾部取恒等。
在每个有限 Walsh 向量上，$U_m$ 的 Cauchy 性归结为
$$
\prod_{j=m}^{n-1}\mu_j\longrightarrow1
\quad(m\to\infty,\ n>m),
$$
由 $\sum_j(1-\mu_j)<\infty$ 成立；有限个 $\mu_j=0$ 不影响尾部论证。
$U_m^*$ 具有相同估计。
所以 $U_m,U_m^*$ 都强收敛，两个极限互为逆，极限 $U$ 是酉算子，且
$U\chi_F=h_F$。没有要求 $\sum_j\|U_j-I\|<\infty$。

**主定理。** 令
$$
S_N=\sum_{j\ge0}(j+1)^{-2}N_j,\qquad
S_Y=\sum_{j\ge0}(j+1)^{-2}N_j(I+N_j)^{-1}.
\tag{1.3}
$$
若 $\rho\ge0$ 为迹类算子，且在某个 (1.2) 的基下对角，则
$$
\boxed{
\operatorname{Tr}(\rho S_\bullet F)=0\quad(F\in\mathcal A)
\quad\Longrightarrow\quad \rho=0.
}
\tag{1.4}
$$
可允许无限秩及任意慢的对角概率尾。没有统一次数指数矩要求。

更一般，在固定有限头上任取正交基，而高尾采用 (1.1) 的乘积基，结论仍成立。
甚至可以让密度在每个高尾配置上具有任意有限头矩阵块：只要它相对于下面的混合基只有有限头翻转带，正迹类情形仍被排除。

这里不声称任意正态都在某个乘积基下对角，也不把不同乘积基下的任意正态混合自动纳入同一个类。

## 2. 有限头规范化

用物理坐标 $e_0,e_1$ 写
$$
h_{j,0}=a_je_0+b_je_1,\qquad
v_j=a_j\overline{b_j}.
$$
$|v_j|\le1/2$。由 (1.1)，
$$
v_j=\frac{|\mu_j|^2-|\nu_j|^2}{2}
+i\,\operatorname{Im}(\nu_j\overline{\mu_j})
\longrightarrow\frac12.
\tag{2.1}
$$
因此可以选固定 $m_0$，使 $|v_j|\ge1/4$ 对所有 $j\ge m_0$ 成立。

先把低 $m_0$ 位的对角基改回标准 Walsh 基，保留全部高尾 $h_{j,\varepsilon}$。
称这个基为混合基 $\{e_F^{(h)}\}$。
在混合基中，低位参数为 $v_j=1/2$，高位仍为 (2.1)，于是全文可以先假定
$$
\boxed{\frac14\le|v_j|\le\frac12\quad(j\ge0),\qquad v_j\to\frac12.}
\tag{2.2}
$$
最后再恢复原有限头。只在有限维头上换基不会使迹类矩阵出现高尾翻转：
原基下的对角密度，相对于混合基的矩阵只允许
$F\triangle G\subset[0,m_0)$。

## 3. 改基后的真实局部矩阵

实际归一化幂满足
$$
N_j=\begin{pmatrix}0&t_j\\I&0\end{pmatrix}_{\rm physical},
\qquad t_j=\eta_jN_{j+1},\qquad
N_j^2=\eta_jN_{j+1},
$$
$$
\|N_j\|=1,\qquad
0<\eta_j\le e^{-770\,16^j}.
\tag{3.1}
$$
局部基调整不会改变这些真实算子的范数、平方关系或尾支撑。

如果 $T\in\mathscr C_j:=\{N_j\}'$，先由 $N_j^2$ 得物理块与 $N_{j+1}$ 交换，
再直接比较 $TN_j=N_jT$，得到
$$
T=\begin{pmatrix}A&t_jB\\B&A\end{pmatrix}_{\rm physical},
\qquad A,B\in\mathscr C_{j+1}.
\tag{3.2}
$$
在新的局部正交基中，其两个对角块为
$$
D_0=A+n_j(t_j)B,\qquad D_1=A-n_j(t_j)B,
\qquad n_j(z)=v_j+\overline{v_j}z.
\tag{3.3}
$$
这是因为 $\langle e_{10}h_{j,0},h_{j,0}\rangle=v_j$，
另一个正交向量给相反的期望；$e_{01}$ 的期望则取共轭。
两个 $D_\varepsilon$ 都在 $\mathscr C_{j+1}$ 中，范数不超过 $\|T\|$。

由 (2.2)，$n_j(t_j)$ 可逆，其逆按 Neumann 级数范数收敛。
定义标量解析函数
$$
a_j(z)=\frac12\left(n_j(z)+\frac{z}{n_j(z)}\right),\qquad
c_j(z)=\frac12\left(n_j(z)-\frac{z}{n_j(z)}\right).
\tag{3.4}
$$
利用 $N_jT$ 在物理块中的表达式，准确得到
$$
(N_jT)_{00}=a_j(t_j)D_0+c_j(t_j)D_1,
$$
$$
(N_jT)_{11}=-c_j(t_j)D_0-a_j(t_j)D_1.
\tag{3.5}
$$
并有
$$
a_j(z)+c_j(z)=n_j(z),\qquad
a_j(z)^2-c_j(z)^2=z.
\tag{3.6}
$$

这些恒等式允许 $v_j$ 为复数；没有假设乘积基与原共轭 $C$ 相容。

## 4. 真正的 $\ell^1$ 右模和注入测试

在系数空间 $\ell^1(\mathfrak F_j)$ 上，从终端 $m$ 的零算子起递归
$$
\widehat N_j^{[m]}=
\begin{pmatrix}
a_j(\eta_j\widehat N_{j+1}^{[m]})
&-c_j(\eta_j\widehat N_{j+1}^{[m]})\\
c_j(\eta_j\widehat N_{j+1}^{[m]})
&-a_j(\eta_j\widehat N_{j+1}^{[m]})
\end{pmatrix}.
\tag{4.1}
$$
同时在辅助 Hilbert 空间 $\mathcal K=\ell^2(\mathfrak F)$ 上使用相同矩阵。

由 $|v_j|\in[1/4,1/2]$，$a_j,c_j$ 的常数项绝对值之和为 $|v_j|\le1/2$；
每个正次数的两个 Taylor 系数绝对值之和不超过 $5$。
具体地，一次项的和不超过 $|v_j|+|v_j|^{-1}\le9/2$，
以后各次的和为 $|v_j|^{-1}\le4$。
因此，在两种空间中都有
$$
\|\widehat N_j^{[m]}\|
\le\frac12+\frac{5\eta_j}{1-\eta_j}<\frac35.
\tag{4.2}
$$
若 $\|R\|,\|Q\|\le1$，则
$$
\|a_j(\eta_jR)-a_j(\eta_jQ)\|
+\|c_j(\eta_jR)-c_j(\eta_jQ)\|
\le\frac{5\eta_j}{(1-\eta_j)^2}\|R-Q\|
\le6\eta_j\|R-Q\|.
\tag{4.3}
$$
从而两种算子范数下都有一致的极限 $\widehat N_j$，并保留
$$
\widehat N_j^2=\eta_j\widehat N_{j+1},\qquad
[\widehat N_j,\widehat N_k]=0.
\tag{4.4}
$$
和 R237 相同的递归还给
$$
\|\widehat N_j-\widehat N_j^{[m]}\|
\le6\eta_{m-1}(6\eta_*)^{m-j-1}\quad(j<m),
\qquad \eta_*=\sup_i\eta_i.
\tag{4.5}
$$

在辅助空间中，用标准两位矩阵
$$
E_j^*=\frac12\begin{pmatrix}1&-1\\1&-1\end{pmatrix}
$$
表示平方零算子，参考向量为配置真空 $1=e_\varnothing$。
这个符号只在辅助空间的本节及第5节使用。
(4.1) 的纯主项与误差为
$$
\boxed{\|\widehat N_j-v_jE_j^*\|\le6\eta_j.}
\tag{4.6}
$$

令
$$
\Lambda_j^{(h)}(p)(T)
=\sum_Fp_F\langle T e_F^{(h)},e_F^{(h)}\rangle.
$$
由 (3.5) 和 R237 的有限终端缺陷论证，缺陷满足
$\delta_j^{[m]}\le6\eta_j\delta_{j+1}^{[m]}$，终端缺陷至多一。
所以
$$
\boxed{
\Lambda_j^{(h)}(\widehat N_jp)(T)
=\Lambda_j^{(h)}(p)(N_jT).
}
\tag{4.7}
$$
这个证明只把 R237 中的常数 $4$ 改成 $6$：
每次幂差至多次数乘上一层缺陷，正 Taylor 系数的加权和由 (4.3) 控制。
因此没有用形式极限代替实际正常泛函极限。

对 $\widehat Y_j=\widehat N_j(I+\widehat N_j)^{-1}$，
实际侧与辅助侧的逆级数都范数收敛，得到相同右模式。
所有高位仍为 $N_0$、$\widehat N_0$ 的对应非零常数倍幂，所以全空间可以同时测试全部高位。

注入性也完全准确。定义原实际算子的有理函数
$$
J_j=N_j\,n_j(N_j^2)^{-1}\in\mathcal A.
\tag{4.8}
$$
它在当前局部基中的两个对角块恰为 $I,-I$。
不同位按最低位剥离，故 $J_K=\prod_{j\in K}J_j$ 的对角恰为
$(-1)^{|K\cap F|}$。
相应有限柱测试在每个配置上的值是准确示性函数。
对 $p\in\ell^1$ 逐原子取极限，证明
$$
\boxed{
\Lambda^{(h)}(p)|_{\mathcal A}=0\Longrightarrow p=0.
}
\tag{4.9}
$$
测试 (4.8) 始终属于原 $\mathcal A$；没有假设改基酉算子与 $A$ 交换。

## 5. 复纯尾的完整双尺度排核

令 $b_j=(j+1)^{-2}$，在辅助 Hilbert 空间定义
$$
\widehat S_N=\sum_jb_j\widehat N_j,\qquad
\widehat S_Y=\sum_jb_j\widehat Y_j.
$$
两者范数小于 $3$。
我们证明
$$
\ker_{\mathcal K}\widehat S_N=\ker_{\mathcal K}\widehat S_Y=0.
\tag{5.1}
$$

### 5.1 真实头、纯中段和纯尾

有限头 $G_k$ 按 R237 取 $\widehat N_j^{[k]}$ 或其 Cayley 项的加权和。
由 (4.4)，$G_k^{2^k}=0$，$\|G_k\|<3$。
(4.5) 给 $N$ 模型低头误差至多 $12\eta_{k-1}$；
两端逆范数至多 $5/2$，使 $Y$ 模型低头误差至多 $75\eta_{k-1}$。

由 (4.6)、$|v_j|\le1/2$ 及 $(E_j^*)^2=0$，
$$
\|\widehat Y_j-v_jE_j^*\|
\le(5/2)(3/2)\,6\eta_j<23\eta_j.
$$
置 $\varepsilon_j=e^{-770\,16^j}$，则 $\eta_i\le\varepsilon_j$ 对所有 $i\ge j$ 成立。
低头末项也有 $\eta_{k-1}\le\varepsilon_{k-1}$；因此下式不需要另假定真实 $\eta_j$ 单调。
两个模型都满足整个算子的范数估计
$$
\boxed{
\left\|\widehat S_\bullet-
\left(G_k+\sum_{j\ge k}b_jv_jE_j^*\right)\right\|
\le200\varepsilon_{k-1}.
}
\tag{5.2}
$$

置 $M=m+1$、$k=\lfloor(3/4)\log_2M\rfloor$，并定义
$$
H_{k,m}=G_k+\sum_{k\le j<m}b_jv_jE_j^*,\qquad
C_m=\sum_{j\ge m}b_jv_jE_j^*.
$$
头、中、尾不交，所以 $H_{k,m}^{2^k+m-k}=0$，
其指数多项式次数至多 $M+M^{3/4}$，且
$\|H_{k,m}\|+\|C_m\|<8$。

### 5.2 新尾与 R60 尾的差仅为 $o(M)$

对 $q\in\mathbb C$ 令
$$
\ell(q)=\frac12\log\frac{1+|q-1|^2}{2}.
$$
作为 $\mathbb R^2$ 上的函数，它的梯度范数至多 $1/2$，
故全局 $1/2$-Lipschitz。

准确尾指数范数为
$$
F_m(t)=\|e^{-tC_m^*}1\|
=\prod_{j\ge m}
\left(1-\operatorname{Re}(tb_j\overline{v_j})
+\frac{t^2b_j^2|v_j|^2}{2}\right)^{1/2}.
\tag{5.3}
$$
置
$$
d_m=\sup_{j\ge m}|v_j-1/2|\longrightarrow0,
\qquad t=2uM^2,\quad1\le u\le20.
$$
与 $v_j\equiv1/2$ 的基准尾相比，全局 Lipschitz 界和
$\sum_{j\ge m}b_j\le1/m$ 给
$$
\left|\log F_m(2uM^2)
-\sum_{j\ge m}\ell(uM^2b_j)\right|
\le uM^2d_m\sum_{j\ge m}b_j
\le40Md_m.
\tag{5.4}
$$
R237 已逐项支付的 Riemann 和误差为至多 $10$，所以
$$
\boxed{|\log F_m(2uM^2)-Mh(u)|\le10+40Md_m,}
\tag{5.5}
$$
其中
$$
h(u)=\frac12\int_1^\infty
\log(1-u/x^2+u^2/(2x^4))\,dx.
$$

### 5.3 多项式估计与全部核

R60 的已证加权 Bernstein–Walsh 式和严格负常数为
$$
\log|p(0)|\le d\,g_0+\int_1^{20}\log|p(u)|\,d\omega_0(u),
\qquad
g_0+\int_1^{20}h(u)\,d\omega_0(u)<-\frac{13}{100}.
\tag{5.6}
$$
完整常数证书见 R237 主稿所引的原证书。

对 $f\in\ker\widehat S_\bullet$，
(5.2) 和真实 Duhamel 式给
$$
\|e^{tH_{k,m}}f-e^{-tC_m}f\|
\le200t e^{8t}\varepsilon_{k-1}\|f\|.
$$
仍有 $\varepsilon_{k-1}\le e^{-3M^3}$。在 $t\le40M^2$ 上，
右侧除以 $\|f\|$ 后不超过
$$
8000M^2e^{320M^2-3M^3}\le e^{-40M}
$$
对充分大的 $M$ 成立。由 $h(u)\ge-u/2$ 和 $d_m\to0$，
它也小于 (5.5) 给出的 $F_m(t)$ 下界。

对多项式 $p_m(u)=\langle e^{2uM^2H_{k,m}}f,1\rangle$ 应用 (5.6)，得到
$$
|\langle f,1\rangle|
\le2\|f\|
\exp\left(10-\frac{13}{100}M+40Md_m+g_0M^{3/4}\right)
\longrightarrow0.
\tag{5.7}
$$
这一步只要求 $v_j\to1/2$，不要求 $\sum_j|v_j-1/2|<\infty$。

最后令
$$
U_j=I-\frac{2}{v_j}\widehat N_j.
$$
它们两两交换并保持上述核，且
$$
\|U_j\|<6,\qquad
\|U_j^*-(I-2E_j)\|\le48\eta_j.
$$
R237 的全次数首次误差合成现在给
$$
\left\|\mathcal W-I\right\|
\le48\sum_j\eta_j37^{j/2}<1,
\qquad \mathcal W\chi_F=U_F^*1.
\tag{5.8}
$$
具体的平方系数和是
$\sum_{K\subset[0,j)}6^{2|K|}=37^j$；
尾纯项先作用于参考真空，故仍保留正交合成。
所以 $\{U_F^*1\}$ 的张成稠密。
对每个 $U_Ff$ 使用 (5.7)，即得 $f=0$，证明 (5.1)。

## 6. 从对角右模返回原正密度

如果 $\rho=\sum_Fp_F|e_F^{(h)}\rangle\langle e_F^{(h)}|$ 相对于混合基对角，
$p\in\ell^1$，则与 R237 相同：
湮灭条件给
$\Lambda^{(h)}(\widehat S_\bullet p)|_{\mathcal A}=0$，
(4.9) 给 $\widehat S_\bullet p=0$，(5.1) 再给 $p=0$。
这是混合基上任意复 $\ell^1$ 对角序列的注入结论。

原基的对角密度只在低 $m_0$ 位换过基，故相对于混合基只含
$D\subset[0,m_0)$ 的有限翻转带。
这些低位仍是标准 Walsh 位，所以 R237 有限翻转附录的精确公式不变：
$$
T_{01}=\frac12s_j^{-1}(T_{00}-T_{11}),\qquad
T_{10}=-T_{01},
\qquad
s_j^{-1}=(I-\eta_jN_{j+1})(I+\eta_jN_{j+1})^{-1}.
$$
先处理尾翻转，再由 (4.7) 将这个真实尾逆送入辅助模。
所有尾权重始终保留，范数成本仍是
$$
\prod_{j<m_0}\frac{1+(3/5)\eta_j}{1-(3/5)\eta_j}<2.
$$
有限带迹类范数控制完全与基无关，因此原 $\rho$ 的正常泛函具有一个
$q_\rho\in\ell^1$ 的混合基对角代表，并满足
$$
\operatorname{Tr}(\rho T)=\Lambda^{(h)}(q_\rho)(T)
\quad(T\in\{A\}'),
\qquad
\sum_F(q_\rho)_F=\operatorname{Tr}\rho.
$$
湮灭条件迫 $q_\rho=0$，因而 $\operatorname{Tr}\rho=0$。
对 $\rho\ge0$ 得 $\rho=0$，主定理完成。

若原有限头某个 $v_j=0$，其原对角泛函可能不注入；
本节只在规范化后的混合基使用注入性，并只把原密度结论传回零迹。
没有将这个有限头退化问题省略。

## 7. 不在前三类中的明确正常正态

以下例子表明，本稿不是只重述 R230、R235 或原 Walsh 矩阵绝对可和类。

取
$$
\theta_j=(j+2)^{-1},\qquad
h_{j,0}=\frac{1+i\theta_j\chi_j}{\sqrt{1+\theta_j^2}},
\qquad
h_{j,1}=\frac{i\theta_j+\chi_j}{\sqrt{1+\theta_j^2}}.
\tag{7.1}
$$
这是 (1.1) 的一个可实现正交乘积基。
把集合 $\{2^k:k\ge1\}$ 依次分成互不相交的有限集合 $F_n$，
使 $|F_n|=n$。令
$$
p_n=\frac{1}{c\,n^2},\qquad c=\sum_{n\ge1}n^{-2},\qquad
\rho=\sum_{n\ge1}p_n|h_{F_n}\rangle\langle h_{F_n}|.
\tag{7.2}
$$
$\rho\ge0$、$\operatorname{Tr}\rho=1$，且主定理排除它成为两个慢主理想的湮灭者。

### 7.1 没有任何次数指数矩

对每个 $r>1$，直接由乘积给
$$
\|r^{\mathsf N}h_F\|^2
=
\prod_{j\notin F}\frac{1+r^2\theta_j^2}{1+\theta_j^2}
\prod_{j\in F}\frac{\theta_j^2+r^2}{1+\theta_j^2}.
\tag{7.3}
$$
$F_n$ 中全部 $j\ge2$，所以 $\theta_j^2\le1/16$；
每个第二乘积因子至少为
$$
c_r=\frac{16r^2+1}{17}>1.
$$
第一乘积因子全部至少一。于是
$$
\operatorname{Tr}(r^{2\mathsf N}\rho)
=\sum_np_n\|r^{\mathsf N}h_{F_n}\|^2
\ge\sum_np_nc_r^n=\infty.
$$

### 7.2 原 Walsh 矩阵不是绝对可和，且不保函数正锥

令
$$
A_0=\prod_j(1+\theta_j^2)^{-1/2}>0,\qquad
P_0=\sum_np_n\prod_{k\in F_n}\theta_k^2>0.
$$
对每个 $j\notin\bigcup_nF_n$，在 (7.2) 中取原 Walsh 的 $(\varnothing,\{j\})$ 矩阵元，准确得到
$$
\boxed{
\langle\rho\chi_{\{j\}},1\rangle=-iA_0^2P_0\theta_j.
}
\tag{7.4}
$$
这是因为 $h_F$ 的真空系数是
$A_0i^{|F|}\prod_{k\in F}\theta_k$，
在 $j\notin F$ 时单比特系数是它的 $i\theta_j$ 倍。
所有求和均由迹类展开绝对控制。

除去二的幂后，$\sum_j\theta_j$ 仍发散，所以 (7.4) 已使
$\|\rho\|_{\mathrm{ent}}=\infty$。
而 (7.4) 是非零纯虚数；保函数正锥的复线性算子必须把实函数送到实函数，
不可能在两个实 Walsh 向量之间出现这样的矩阵元。
所以 $\rho$ 也不属于 R235 的保锥类。

## 8. 当前结论的边界

本稿排除的是某一个可实现正交乘积基下的全部正常对角正态，
及有限头翻转所产生的相应块类。
它允许没有统一次数矩、没有原 Walsh 矩阵绝对和、也不保持函数正锥的正常密度。

仍未证明任意正常有限秩见证或任意正常正态都能通过这种基选择处理。
特别，任意向量未必是乘积向量，任意有限维子空间也未必同时成为某个正交乘积基的有限张成。
没有由本稿得到普通 Hilbert 不变子空间问题的完成结论。
