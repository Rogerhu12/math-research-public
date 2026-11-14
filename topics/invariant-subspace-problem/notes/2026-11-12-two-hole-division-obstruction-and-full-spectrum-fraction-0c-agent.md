# R167：相邻两孔测试、实际无界除法与零形式阶分式的全连续谱

日期：2026-11-12。作者：l2_moments。根代理预留 R167。
状态：完整证明；两孔机制和谱分支已由根代理纸面核验，正文补齐全部实际进位估计。
本稿没有否定未知不变子空间上的受限除法，也没有据此判定慢共振核存在。

## 1. 两个真实算子

记
$$
N_i=A^{2^i}/d_i,\qquad d_i=W_{2^i},\qquad
N_i=E_i+\eta_iE_i^*N_{i+1},
$$
$$
\eta_i=\alpha_{i+1}/\alpha_i,\qquad
N_i^2=\eta_iN_{i+1},\qquad
\|(I+N_i)^{-1}\|<3.
\tag{1.1}
$$
本模型 $\eta_i$ 递减，且
$\eta_i\le e^{-770\,16^i}$。
设非零 $b=(b_i)\in\ell^1$，定义
$$
Y_i=N_i(I+N_i)^{-1},\qquad
K_i=N_i(I+N_i)^{-2},
$$
$$
\boxed{W=\sum_i b_iY_i,\qquad Z=\sum_i b_i^2K_i.}
\tag{1.2}
$$
两级数按范数绝对收敛，属于交换的 $\mathcal A$。
$W1=\frac12\sum_i b_i(1-\chi_i)$ 是非零第一 chaos。
R125 因而给 $W$ 单射且值域稠密。

第一结论是：若 $b_i=(i+1)^{-2}$ 对充分大 $i$ 成立，有限前缀可任意修改，则
$$
\boxed{Z\notin W B(H),\qquad
\operatorname{Ran}Z\not\subseteq\operatorname{Ran}W.}
\tag{1.3}
$$
第二结论取快系数
$$
b_i=e^{-(i+1)^4}.
\tag{1.4}
$$
此时 $W,Z\in\mathcal G$，而 R153 的最大闭分式
$$
T=W^{-1}Z
$$
具有
$$
\boxed{
\operatorname{ord}T=0,\qquad
\text{形式常数 }b_0\ne0,\qquad
T\text{ 无界},\qquad
\sigma(T)=\sigma_c(T)=\mathbb C.
}
\tag{1.5}
$$
这里 $\sigma_c$ 指注入、稠密但非满射的连续谱。
没有声称所有零形式阶分式都具有这种谱。

## 2. 两孔单位向量与逐位进位界

取 $j\ge1$、$k=j+1$、$M>k$。
在低 $M$ 位的物理张量基中，记：

- $h_j$：除第 $j$ 位为0外，其余低 $M$ 位全为1；
- $h_k$：除第 $k$ 位为0外，其余低 $M$ 位全为1；
- $e_M$：低 $M$ 位全为1。

三者的 $j\ge M$ 尾部都取常参考向量。
它们均为单位向量，$h_j,h_k$ 正交。
对任意 $u,v\in\mathbb C$、$|u|^2+|v|^2=1$，置
$$
x=uh_j+vh_k.
\tag{2.1}
$$
纯算子只有两个非零填孔作用：
$$
E_jx=ue_M,\qquad E_kx=ve_M,\qquad
E_ix=0\quad(i<M,\ i\ne j,k).
\tag{2.2}
$$

定义
$$
r_i=
\begin{cases}
\alpha_j/\alpha_i,&i<j,\\
\eta_j,&i=j,\\
\alpha_M/\alpha_i,&j<i<M.
\end{cases}
\tag{2.3}
$$
则
$$
r_i\le\eta_{j-1}\qquad(i<M).
\tag{2.4}
$$

**引理2.1。** 对 (2.1) 的全部单位向量，
$$
\boxed{
\|(N_i-E_i)x\|\le r_i,\qquad
\|N_i^2x\|\le r_i
\quad(i<M).
}
\tag{2.5}
$$
此外，对于 $i=j,k$，
$$
\boxed{\|(N_i-E_i)E_ix\|\le\alpha_M/\alpha_i.}
\tag{2.6}
$$

**证明。**
若 $i<j$，输入第 $i$ 位到第一个孔之间全为1。
逐次使用 (1.1)，$N_i$ 在 $h_j$ 上的非零项正好进位到第 $j$ 位，
系数为 $\alpha_j/\alpha_i$；
在 $h_k$ 上则进位到第 $k$ 位，系数为 $\alpha_k/\alpha_i$。
两输出物理头不同，仍正交，
所以组合的范数至多 $\alpha_j/\alpha_i$。
此时 $E_ix=0$，第一界成立。

若 $i=j$，$N_jh_j=E_jh_j=e_M$；
对 $h_k$，第 $j$ 位为1、下一位是孔，故
$(N_j-E_j)h_k$ 的范数为 $\eta_j$。
这给第二支的第一界。

若 $i=k$，$N_kh_k=E_kh_k=e_M$。
对 $h_j$，第 $k$ 位到第 $M-1$ 位全为1，
进位只能越过整个剩余头，余下尾项系数为 $\alpha_M/\alpha_k$。
若 $k<i<M$，两个输入在第 $i$ 位到第 $M-1$ 位都全为1，
相同递推给
$$
N_ix=\frac{\alpha_M}{\alpha_i}
(E_i^*\cdots E_{M-1}^*)N_Mx,
$$
而 $E_ix=0$。
因 $N_M$ 范数为1，得到第三支的第一界。

平方界不通过一个全局低位误差偷换而来。
用精确 $N_i^2=\eta_iN_{i+1}$：
若 $i<j-1$，刚才的填孔界给
$$
\|N_i^2x\|\le
\eta_i\alpha_j/\alpha_{i+1}=\alpha_j/\alpha_i.
$$
若 $i=j-1$ 或 $i=j$，直接用 $\|N_{i+1}\|\le1$，
分别得到 $\eta_{j-1}$ 与 $\eta_j$。
若 $j<i<M$，则 $i+1>k$，第 $i+1$ 位之后直到 $M-1$ 全为1，
所以同一尾递推给 $\alpha_M/\alpha_i$；
当 $i=M-1$ 时直接使用 $\eta_{M-1}\|N_M\|\le\alpha_M/\alpha_{M-1}$。

最后，$E_jx$ 和 $E_kx$ 各为一个模长不超过1的系数乘 $e_M$。
在全1头上，$E_ie_M=0$，$N_i$ 必进位到尾 $M$，
系数为 $\alpha_M/\alpha_i$，证明 (2.6)。
所以在第 $k=j+1$ 位也没有遗漏先填孔再进位的作用。证毕。

## 3. $Y_i-E_i$ 与 $K_i-E_i$ 的真实作用估计

使用精确恒等式
$$
Y_i-N_i=-N_i^2(I+N_i)^{-1}
$$
以及实际因子互相交换，得到
$$
\|(Y_i-N_i)x\|
\le3\|N_i^2x\|.
$$
这里是把 $(I+N_i)^{-1}$ 与 $N_i^2$ 交换，
没有把它穿过纯 $E_i$。
由 (2.5)，
$$
\boxed{\|(Y_i-E_i)x\|\le4r_i.}
\tag{3.1}
$$

同样有精确式
$$
K_i-N_i
=-N_i^2(2I+N_i)(I+N_i)^{-2}.
$$
因此
$$
\|(K_i-N_i)x\|
\le3\cdot9\,\|N_i^2x\|,
$$
从而
$$
\boxed{\|(K_i-E_i)x\|\le28r_i.}
\tag{3.2}
$$
这付清了两个具体因子的全部高幂修正。
也可把4、28统一换成保守常数100，但无需这样放大。

记
$$
B_1=\sum_i|b_i|,\qquad B_2^2=\sum_i|b_i|^2,\qquad
\tau_M=\sum_{i\ge M}|b_i|.
$$
因 $\|Y_i\|\le3$、$\|K_i\|\le9$，由 (2.2)—(3.2) 得
$$
\boxed{
\|Wx-(b_ju+b_kv)e_M\|
\le4B_1\eta_{j-1}+3\tau_M,
}
\tag{3.3}
$$
$$
\boxed{
\|Zx-(b_j^2u+b_k^2v)e_M\|
\le28B_2^2\eta_{j-1}+9\tau_M^2.
}
\tag{3.4}
$$
最后一项使用
$\sum_{i\ge M}|b_i|^2\le\tau_M^2$。

对每个固定 $j$，可选有限 $M>j+1$ 足够大，使
$$
\tau_M\le\eta_{j-1}.
\tag{3.5}
$$
不对 $M$ 相对 $j$ 的增长速度作假设。
于是 (3.3)—(3.4) 的误差分别至多
$$
C_W\eta_{j-1},\qquad C_Z\eta_{j-1},
\quad
C_W=4B_1+3,\quad C_Z=28B_2^2+9.
\tag{3.6}
$$
这些常数与 $j,M,u,v$ 无关。

## 4. 慢尾的实际有界除法不成立

假定 $b_i=(i+1)^{-2}$ 最终成立。
取充分大的相邻 $j,k=j+1$，并按 (3.5) 选 $M$。
令
$$
x_j=\frac{b_jh_k-b_kh_j}{\sqrt{b_j^2+b_k^2}}.
\tag{4.1}
$$
纯 $W$ 项精确相消，而纯 $Z$ 项为
$$
d_j e_M,\qquad
d_j=\frac{b_jb_k(b_k-b_j)}{\sqrt{b_j^2+b_k^2}}.
\tag{4.2}
$$
由显式系数，
$$
|d_j|\asymp j^{-5}.
\tag{4.3}
$$
例如 $b_j-b_k=(2j+3)/[(j+1)^2(j+2)^2]$，
代入 (4.2) 即得两个正的固定倍数上下界。

由 (3.6)，
$$
\|Wx_j\|\le C_W\eta_{j-1},\qquad
\|Zx_j\|\ge|d_j|-C_Z\eta_{j-1}.
$$
而 $\eta_{j-1}\le e^{-770\,16^{j-1}}$，
所以充分大 $j$ 有
$$
\boxed{
\|Zx_j\|\ge\tfrac12|d_j|,\qquad
\frac{\|Zx_j\|}{\|Wx_j\|}\longrightarrow\infty.
}
\tag{4.4}
$$
若分母偶为零，$W$ 单射将迫 $x_j=0$，与单位范数矛盾；
所以该比值定义良好。

若存在任意 $Q\in B(H)$ 使 $Z=WQ$，
由 $WZ=ZW$ 有
$$
W(QW-WQ)=0.
$$
$W$ 单射，故 $QW=WQ$，于是 $Z=QW$，
这将给 $\|Zx\|\le\|Q\|\|Wx\|$，与 (4.4) 矛盾。
所以 $Z\notin WB(H)$。

若仅假设 $\operatorname{Ran}Z\subseteq\operatorname{Ran}W$，
则 $Q=W^{-1}Z$ 在全 $H$ 有定义且单值。
其图闭：若 $x_n\to x,Qx_n\to y$，则 $Wy=Zx$，
故 $Qx=y$。
闭图定理使 $Q$ 有界，已被排除。
由此完成 (1.3)。

特别，不能在全空间把平方共振修正写成
$W(I+\text{有界小量})$，再用一个未经验证的 Neumann 逆。
这不排除在某个未知不变核 $M$ 上建立新的有界除法。

## 5. 快系数产生零形式阶而全连续谱的闭分式

现在固定
$$
b_i=e^{-(i+1)^4}.
$$
$b_i>0$、严格递减，且
$$
b_{j+1}/b_j\longrightarrow0.
\tag{5.1}
$$
它满足 R154 的超三次重排条件。
$Y_i=N_i(I+N_i)^{-1}$、$K_i=N_i(I+N_i)^{-2}$
的后因子都真解析且一致有界，
所以 R154 带因子尾引理给
$$
W,Z\in\mathcal G.
\tag{5.2}
$$
两者的形式首阶均为1，首系数分别为
$$
[z]\iota(W)=b_0/d_0,\qquad
[z]\iota(Z)=b_0^2/d_0.
$$
因此 R153 的最大闭分式
$$
T=T_{Z/W}=W^{-1}Z
$$
为稠密定义闭算子，
其形式阶为0，形式常数为 $b_0$。

### 5.1 $T$ 本身无界

仍取 (4.1) 的两孔向量。
由 (5.1)，对充分大 $j$ 有 $b_k\le b_j/2$，从而
$$
|d_j|
=\frac{b_jb_k(b_j-b_k)}{\sqrt{b_j^2+b_k^2}}
\ge\frac{b_jb_k}{2\sqrt2}.
\tag{5.3}
$$
右侧为 $\exp[-O(j^4)]$，而
$\eta_{j-1}\le\exp[-770\,16^{j-1}]$。
所以 (4.4) 的发散比值对这个快序列同样成立。
第4节证明无需多项式慢尾的其他性质，因而仍有
$Z\notin WB(H)$。
R153 的最大商有界判据，或直接闭图，说明 $T$ 无界。

### 5.2 每个 $Z-\lambda W$ 都是非零 $\mathcal G$ 元素

若 $\lambda\ne b_0$，其一次系数为
$$
[z]\iota(Z-\lambda W)=b_0(b_0-\lambda)/d_0\ne0.
$$
若 $\lambda=b_0$，一次项消失，但二次系数精确为
$$
\boxed{
[z^2]\iota(Z-b_0W)
=\frac{b_1(b_1-b_0)}{d_1}-\frac{b_0^2}{d_0^2}<0.
}
\tag{5.4}
$$
这是由
$Y_0=N_0-N_0^2+\cdots$、
$K_0=N_0-2N_0^2+\cdots$ 及第1位的首项得到。
$j\ge2$ 位从四次才开始，没有其他二次贡献。
$b_1<b_0$ 保证严格负号。

因此 $Z-\lambda W\in\mathcal G\setminus\{0\}$ 对全部 $\lambda$ 成立。
R153 给
$$
\boxed{\ker(T-\lambda)=0,\qquad
\overline{\operatorname{Ran}(T-\lambda)}=H.}
\tag{5.5}
$$
包括最大域的准确关系
$T-\lambda=T_{(Z-\lambda W)/W}$。

### 5.3 所有预解参数均被两孔向量排除

固定任意 $\lambda\in\mathbb C$，记
$$
c_i=b_i^2-\lambda b_i,\qquad D_\lambda=Z-\lambda W.
$$
取足够大的相邻 $j,k$，使 $(c_j,c_k)\ne(0,0)$，令
$$
x_j^\lambda=
\frac{c_jh_k-c_kh_j}{\sqrt{|c_j|^2+|c_k|^2}},
\tag{5.6}
$$
并仍选 $M$ 满足 (3.5)。
纯 $D_\lambda$ 项相消。
由 (3.6)，
$$
\boxed{
\|D_\lambda x_j^\lambda\|
\le(C_Z+|\lambda|C_W)\eta_{j-1}.
}
\tag{5.7}
$$
纯 $W$ 项模长为
$$
a_j^\lambda
=\frac{b_jb_k(b_j-b_k)}
{\sqrt{|c_j|^2+|c_k|^2}},
$$
故
$$
\|Wx_j^\lambda\|\ge a_j^\lambda-C_W\eta_{j-1}.
\tag{5.8}
$$

必须分两个尺度讨论。

若 $\lambda=0$，由 $b_k\le b_j/2$，
$$
a_j^0
=\frac{b_jb_k(b_j-b_k)}{\sqrt{b_j^4+b_k^4}}
\ge\frac{b_k}{2\sqrt2}.
\tag{5.9}
$$
若 $\lambda\ne0$，取更大 $j$ 使 $b_j\le|\lambda|/2$。
则 $|c_i|\le\frac32|\lambda|b_i$ 对 $i=j,k$ 成立，所以
$$
a_j^\lambda\ge
\frac{b_jb_k}{3\sqrt2|\lambda|}.
\tag{5.10}
$$
两种下界均为 $\exp[-O(j^4)]$，
除以 $\eta_{j-1}$ 都趋于无穷。
结合 (5.7)—(5.8)，得到
$$
\boxed{
\frac{\|Wx_j^\lambda\|}
{\|D_\lambda x_j^\lambda\|}\longrightarrow\infty.
}
\tag{5.11}
$$
分母非零，由 $D_\lambda\in\mathcal G\setminus\{0\}$ 的单射性保证。

另一方面，$Wx\in\operatorname{Dom}T$ 对全部 $x\in H$ 成立，
且最大商的真实恒等式为
$$
\boxed{(T-\lambda)Wx=(Z-\lambda W)x.}
\tag{5.12}
$$
若 $\lambda$ 属于 $T$ 的预解集，令有界全域逆为 $R_\lambda$，
(5.12) 将给
$$
\|Wx\|\le\|R_\lambda\|\,\|D_\lambda x\|,
$$
与 (5.11) 矛盾。
所以每个 $\lambda$ 都不在预解集。

结合 (5.5)，所有参数都是连续谱；
闭算子若在某个参数处同时单射满射，其逆由闭图定理有界，
故这里值域确实不能满射。
这完成
$$
\boxed{\sigma(T)=\sigma_c(T)=\mathbb C.}
\tag{5.13}
$$

## 6. 准确含义

慢尾分支严格排除了全空间的 $Z=WQ$ 有界除法及值域包含。
它没有排除某个未知闭不变 $M$ 上的受限关系；
原共振核若存在，仍可能满足只有在该核上成立的有界商。

快尾分支同时证明：即使分子、分母都属于具有普遍子商性质的 $\mathcal G$，
它们的闭分式仍可能在全空间无界且拥有整个复平面的连续谱。
本例的形式阶为0、形式常数非零；
因此“非负形式阶”或“形式常数非零”不能替代实际有界因式判据。
没有从一个例子反推所有零阶分式都如此。

本稿没有构造原题的非平凡不变子空间，
也没有证明慢共振平方非循环。
完整 Hilbert ISP 仍开放。


## 7. 慢尾最大闭商同样具有全连续谱

日期：2026-11-12。作者：l2_moments。
本补注只加强 R167 的全空间谱结论，不使用或声称慢分母在任意不变限制上的稠密像，也不声称原分母值域是最大商的图核心。

### 7.1. 命题

沿用 R167：
$$
W=\sum_i b_iN_i(I+N_i)^{-1},\qquad
Z=\sum_i b_i^2N_i(I+N_i)^{-2},
$$
其中 $b\in\ell^1$ 且 $b_i=(i+1)^{-2}$ 对充分大 $i$ 成立，有限前缀任意。
定义最大商
$$
\operatorname{Dom}T=\{x\in H:Zx\in\operatorname{Ran}W\},\qquad
Tx=W^{-1}Zx.
\tag{A1.1}
$$
则
$$
\boxed{T\text{ 稠密定义且闭},\qquad
\sigma(T)=\sigma_c(T)=\mathbb C.}
\tag{A1.2}
$$
这里并未把 $T$ 称作 $\operatorname{Frac}\mathcal G$ 元素；慢系数通常不满足该条件。

### 7.2. 每个 $D_\lambda=Z-\lambda W$ 均单射稠密

先证明 $D_\lambda\ne0$，无须分析可能任意的有限前缀。
R167 的填满头部两孔单位向量
$$
x_j=\frac{b_jh_{j+1}-b_{j+1}h_j}
{\sqrt{b_j^2+b_{j+1}^2}}
$$
满足
$$
\|Wx_j\|\le C_W\eta_{j-1},\qquad
\|Zx_j\|\ge c\,j^{-5}-C_Z\eta_{j-1}.
$$
因此对每个固定 $\lambda$，
$$
\|D_\lambda x_j\|
\ge c\,j^{-5}-(C_Z+|\lambda|C_W)\eta_{j-1}>0
$$
当 $j$ 足够大，所以 $D_\lambda\ne0$。

若 $\zeta$ 是阶数整除 $2^m$ 的 dyadic 根，则
$\gamma_\zeta N_i=N_i$ 对全部 $i\ge m$ 成立。
故
$$
\gamma_\zeta D_\lambda-D_\lambda
$$
是只含 $i<m$ 项的有限有理函数之和，在 $A$ 的谱点0附近真解析。
$D_\lambda\in\mathcal A$ 的形式系数忠实，且其常数为0。
令其首非零形式阶为 $r_\lambda\ge1$。
对于 $\zeta^{r_\lambda}\ne1$，上述有限解析差的首项非零，
从而
$$
\gamma_\zeta D_\lambda-D_\lambda
=A^{r_\lambda}U_{\lambda,\zeta}(A),
\qquad U_{\lambda,\zeta}(0)\ne0.
\tag{A2.1}
$$
R122 的有界加性 gauge 排核准则给
$$
\boxed{
\ker D_\lambda=0,\qquad
\overline{\operatorname{Ran}D_\lambda}=H
\quad(\lambda\in\mathbb C).
}
\tag{A2.2}
$$
该步骤只用全空间结论。没有把它传给未知不变限制。

### 7.3. 最大商的闭性及其所有移位的核、值域

R125 给 $W$ 单射稠密，因此 (A1.1) 定义唯一。
若 $x_n\to x$ 且 $Tx_n\to y$，有
$$
Wy=\lim WTx_n=\lim Zx_n=Zx.
$$
故 $x\in\operatorname{Dom}T$ 且 $Tx=y$，所以 $T$ 闭。

交换性给
$$
ZWx=WZx,
$$
故 $Wx\in\operatorname{Dom}T$ 且 $TWx=Zx$。
因此 $\operatorname{Ran}W\subseteq\operatorname{Dom}T$，域稠密，并且
$$
\boxed{(T-\lambda)Wx=D_\lambda x.}
\tag{A3.1}
$$
若 $(T-\lambda)x=0$，乘以 $W$ 得 $D_\lambda x=0$，再由 (A2.2) 得 $x=0$。
另一方面，(A3.1) 与 (A2.2) 给
$$
\overline{\operatorname{Ran}(T-\lambda)}=H.
\tag{A3.2}
$$
这些结论不要求证明 $\operatorname{Ran}W$ 是图核心。

### 7.4. 任意预解参数均被实际两孔估计排除

固定 $\lambda$，令
$$
c_i=b_i^2-\lambda b_i.
$$
取充分大的相邻 $j,k=j+1$，用 R167 的同一物理头部及足够远的尾截断 $M$，置
$$
x_j^\lambda=
\frac{c_jh_k-c_kh_j}{\sqrt{|c_j|^2+|c_k|^2}}.
$$
实际误差估计与 R167 完全相同：
$$
\|D_\lambda x_j^\lambda\|
\le(C_Z+|\lambda|C_W)\eta_{j-1},
\tag{A4.1}
$$
$$
\|Wx_j^\lambda\|
\ge
\frac{b_jb_k(b_j-b_k)}
{\sqrt{|c_j|^2+|c_k|^2}}
-C_W\eta_{j-1}.
\tag{A4.2}
$$

若 $\lambda=0$，
$$
\frac{b_jb_k(b_j-b_k)}{\sqrt{b_j^4+b_k^4}}
\ge\frac{b_k(b_j-b_k)}{\sqrt2\,b_j}
\asymp j^{-3}.
\tag{A4.3}
$$
若 $\lambda\ne0$，取 $j$ 足够大使 $b_j\le|\lambda|/2$，则
$$
\sqrt{|c_j|^2+|c_k|^2}
\le\frac{3\sqrt2}{2}|\lambda|b_j.
$$
所以
$$
\frac{b_jb_k(b_j-b_k)}
{\sqrt{|c_j|^2+|c_k|^2}}
\ge
\frac{2b_k(b_j-b_k)}{3\sqrt2|\lambda|}
\asymp_\lambda j^{-5}.
\tag{A4.4}
$$
两类尺度均远大于
$\eta_{j-1}\le\exp[-770\,16^{j-1}]$，因此
$$
\frac{\|Wx_j^\lambda\|}{\|D_\lambda x_j^\lambda\|}
\longrightarrow\infty.
\tag{A4.5}
$$
分母非零，由 (A2.2) 的单射性保证。

若 $T-\lambda$ 有有界全域逆，则 (A3.1) 给
$$
\|Wx\|\le\|(T-\lambda)^{-1}\|\,\|D_\lambda x\|,
$$
与 (A4.5) 矛盾。
故预解集为空。结合 (A3.2) 和注入性，每个 $\lambda$ 都是连续谱点。
若某个参数处值域等于 $H$，闭图定理将自动给有界全域逆，亦已排除。

### 7.5. 与主稿的区别

快尾主稿另外给 $W,Z\in\mathcal G$，从而可调用 R153 在所有不变子商上的最大分式结构、图核心和循环空间保持。
本补注仅证明慢尾全空间最大商的闭性与全连续谱。
它没有提供慢商的普遍子商性质，也不排除未知不变核上的有界受限商。
