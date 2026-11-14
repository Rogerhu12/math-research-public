# R208：实际平方分支核的全等向性与高位删除交换子

日期：2026-11-12（UTC）。作者：critical_kernel。

状态：完整实际必要条件。本文证明指定闭分支的核在本题双线性配对下全等向，并给出其包含于该分支算子闭值域的结论。本文不由全等向性推出核为零；一般慢平方的单核问题仍未解决。

## 1. 定理与实际设置

沿用本题 Haar 表示及记号
$$
H=L^2(\mathbb Z_2,\mu),\qquad
B(f,g)=\langle f,Cg\rangle,\qquad
(Cf)(y)=\overline{f(-1-y)}.
$$
内积对第一变量线性，因此 $B$ 对两个变量都线性。
令
$$
N_j=A^{2^j}/d_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1},\qquad
S_j=I-2E_j.
$$
实际进位及已有统一界为
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
\eta_j=\alpha_{j+1}/\alpha_j,\qquad
\|V_j\|\le6,\qquad
\|V_j-S_j\|\le8\eta_j.
\tag{1.1}
$$
记 $\eta_*=\sup_j\eta_j<1/4$。本题的 $\eta_j$ 超快衰减，特别属于 $\ell^1$。

取任意复系数 $a_*\in\mathbb C$、$a=(a_j)\in\ell^2$，令
$$
X=a_*I+\sum_{j\ge0}a_jV_j
\tag{1.2}
$$
为 R125 的真实闭第一阶算子；该式在有限柱核心上按强收敛理解，再取已证闭实现。置
$$
g=\|a\|_2,\qquad
\mathcal B_2=\sum_{j\ge0}a_j^2(I-V_j^2)\in\mathcal A.
\tag{1.3}
$$
由于 $\|I-V_j^2\|\le37$，(1.3) 绝对范数收敛。其字符为零，所以
$\sigma(\mathcal B_2)=\{0\}$。

**定理 1.1。**
假设存在 $j_n\to\infty$ 满足
$$
a_{j_n}\ne0,\qquad
\frac{\eta_{j_n-1}}{|a_{j_n}|}\longrightarrow0.
\tag{1.4}
$$
令 $\varphi$ 为 $0$ 的某邻域内的标量全纯函数，并以通常全纯演算定义
$$
Y=\varphi(\mathcal B_2)\in\mathcal A,\qquad
T=X-Y,\qquad \operatorname{Dom}T=\operatorname{Dom}X.
$$
则
$$
\boxed{B(\ker T,\ker T)=0.}
\tag{1.5}
$$
等价地，记 $M=\ker T$，有
$$
M\perp CM,\qquad
\boxed{M\subseteq\overline{\operatorname{Ran}T}.}
\tag{1.6}
$$

条件 (1.4) 只要求一个子列。每个
$$
a\in\ell^2\setminus\ell^1
\tag{1.7}
$$
都自动满足该条件；不少慢衰减的 $\ell^1$ 行也满足，例如非零幂尾。

对于首个非零系数 $a=a_{j_0}$，危险平方分支为
$$
Y=(a^2I-\mathcal B_2)^{1/2},\qquad \chi(Y)=a.
\tag{1.8}
$$
平方根取 $0$ 邻域中满足该字符的全纯分支。(1.5) 适用于 (1.8)。
第7节说明它也约束点态符号 $u^2-a^2$ 的真实 Bell 乘子核。

## 2. Walsh 删除算子的准确纯交换子

为避免与 $a_j$ 混淆，记 $b_j$ 为 Walsh 删除算子：
$$
b_j\chi_F=
\begin{cases}
\chi_{F\setminus\{j\}},&j\in F,\\
0,&j\notin F.
\end{cases}
$$
记 $c_j=b_j^*$ 为创建算子，$n_j=c_jb_j$ 为占据投影。
三者范数均为 $1$，且
$$
S_j=c_j-b_j+2n_j.
$$
在单比特 Walsh 基 $(1,\chi_j)$ 下，
$$
S_j=
\begin{pmatrix}0&-1\\1&2\end{pmatrix},\qquad
b_j=
\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$
因此
$$
\boxed{[b_j,S_j]=I-2n_j+2b_j.}
\tag{2.1}
$$
这里及以下均采用 $[R,T]=RT-TR$ 的次序。

每个固定有限柱向量在充分大的 $j$ 上同时被 $n_j,b_j$ 消去。
由有限柱稠密性及统一范数界，
$$
n_j\longrightarrow0,\qquad b_j\longrightarrow0
\quad\text{强收敛}.
$$
故
$$
\boxed{[b_j,S_j]\longrightarrow I\quad\text{强收敛}.}
\tag{2.2}
$$
这只是强收敛；$\|b_j\|=1$，并无范数收敛到零。

## 3. 低位真实进位的交换子预算

对 $k<j$，以 $N_j^{[j]}=0$ 为边界定义有限真实链
$$
N_k^{[j]}=E_k+\eta_kE_k^*N_{k+1}^{[j]},\qquad
V_k^{[j]}=(I-N_k^{[j]})(I+N_k^{[j]})^{-1}.
$$
它们仅作用于位 $[k,j)$，因此与 $b_j$ 精确交换。
逐步相减实际进位式给
$$
N_k-N_k^{[j]}
=\frac{\alpha_j}{\alpha_k}
 E_k^*\cdots E_{j-1}^*N_j,
\qquad
\|N_k-N_k^{[j]}\|\le\frac{\alpha_j}{\alpha_k}.
$$
实际与有限链的逆均有统一界
$\|(I+N_k)^{-1}\|,\|(I+N_k^{[j]})^{-1}\|<3$。
由真实逆差恒等式，
$$
\|V_k-V_k^{[j]}\|
\le18\frac{\alpha_j}{\alpha_k}.
\tag{3.1}
$$
所以
$$
\boxed{\|[b_j,V_k]\|\le36\frac{\alpha_j}{\alpha_k}
\quad(k<j).}
\tag{3.2}
$$

当 $k=j$ 时，(1.1) 给
$$
\|[b_j,V_j]-[b_j,S_j]\|\le16\eta_j.
\tag{3.3}
$$
当 $k>j$ 时，$V_k$ 只作用于从 $k$ 开始的尾位，故
$$
[b_j,V_k]=0
\tag{3.4}
$$
是实际精确等式。

记
$$
D_j=\sum_{k=0}^j a_k[b_j,V_k]\in B(H).
$$
由 (3.2)–(3.4)，
$$
\|D_j-a_j(I-2n_j+2b_j)\|
\le36\alpha_j\sum_{k<j}\frac{|a_k|}{\alpha_k}
 +16|a_j|\eta_j.
\tag{3.5}
$$
对于 $k<j$，
$$
\frac{\alpha_j}{\alpha_k}
=\eta_{j-1}\prod_{\ell=k}^{j-2}\eta_\ell.
$$
Cauchy–Schwarz 因而给出没有 $\sqrt j$ 损失的界
$$
\alpha_j\sum_{k<j}\frac{|a_k|}{\alpha_k}
\le
\frac{g\,\eta_{j-1}}{\sqrt{1-\eta_*^2}}.
$$
综上，
$$
\boxed{
\|D_j-a_j(I-2n_j+2b_j)\|
\le
\frac{36g\,\eta_{j-1}}{\sqrt{1-\eta_*^2}}
+16|a_j|\eta_j.
}
\tag{3.6}
$$

## 4. 闭一阶的真实域保持

对固定 $j$，$b_j$ 保持有限柱空间。
在有限柱核心上，由 R125 的强逐向量收敛和 (3.4)，可以先在有限系数和上计算，再令截断趋于无穷，得到
$$
b_jXv-Xb_jv=D_jv.
\tag{4.1}
$$
此处 $D_j$ 是第3节的有限有界算子和，不含未定义的无穷交换子。

取任意 $v\in\operatorname{Dom}X$。
以有限柱 $v_\nu$ 在 $X$ 图范数中逼近 $v$，则
$$
b_jv_\nu\to b_jv,\qquad
Xb_jv_\nu=b_jXv_\nu-D_jv_\nu\to b_jXv-D_jv.
$$
由 $X$ 闭，
$$
\boxed{
b_j\operatorname{Dom}X\subseteq\operatorname{Dom}X,\qquad
[b_j,X]v=D_jv\quad(v\in\operatorname{Dom}X).
}
\tag{4.2}
$$

沿 (1.4) 的子列，(3.6) 除以 $a_j$ 的范数误差趋于零；
复相位仅通过分母的模进入估计。
结合 (2.2)，得到有界延拓的强极限
$$
\boxed{
\frac{[b_{j_n},X]}{a_{j_n}}\longrightarrow I
\quad\text{强收敛于 }H.
}
\tag{4.3}
$$

## 5. Bell 二阶项及全纯分支的较小交换子

(1.3) 为绝对范数收敛级数，所以可与固定有界 $b_j$ 逐项取交换子。
对 $k<j$，(3.2) 和 $\|V_k\|\le6$ 给
$$
\|[b_j,V_k^2]\|
\le2\|V_k\|\|[b_j,V_k]\|
\le432\frac{\alpha_j}{\alpha_k}.
$$
又 $\alpha_j/\alpha_k\le\eta_{j-1}$，从而
$$
\sum_{k<j}|a_k|^2\|[b_j,V_k^2]\|
\le432g^2\eta_{j-1}.
$$
对同位项，直接用
$$
\|[b_j,V_j^2]\|\le2\|V_j\|^2\le72.
$$
所有高位项 $k>j$ 精确交换。故
$$
\boxed{
\|[b_j,\mathcal B_2]\|
\le432g^2\eta_{j-1}+72|a_j|^2.
}
\tag{5.1}
$$

为 $\varphi$ 选定一条包围 $\sigma(\mathcal B_2)=\{0\}$、且位于其解析邻域内的固定圆周 $\Gamma$。
实际全纯演算和有界逆交换子给
$$
[b_j,Y]
=\frac1{2\pi i}\int_\Gamma
\varphi(z)(z-\mathcal B_2)^{-1}
[b_j,\mathcal B_2]
(z-\mathcal B_2)^{-1}\,dz.
$$
于是存在只依赖固定 $\varphi,\mathcal B_2,\Gamma$ 的有限常数 $C_\varphi$，满足
$$
\|[b_j,Y]\|
\le C_\varphi\bigl(432g^2\eta_{j-1}+72|a_j|^2\bigr).
\tag{5.2}
$$
不要求 $\varphi$ 的 Taylor 收敛半径大于 $\|\mathcal B_2\|$。

由于 $a_j\to0$，条件 (1.4) 和 (5.2) 给
$$
\boxed{
\frac{[b_{j_n},Y]}{a_{j_n}}\longrightarrow0
\quad\text{范数收敛}.
}
\tag{5.3}
$$
故 $T=X-Y$ 满足
$$
b_j\operatorname{Dom}T\subseteq\operatorname{Dom}T,\qquad
\boxed{
\frac{[b_{j_n},T]}{a_{j_n}}\longrightarrow I
\quad\text{强收敛}.
}
\tag{5.4}
$$

## 6. 跨核配对、全等向性及子列存在性

R125 给 $X^*=CXC$。有界 $Y\in\mathcal A$ 满足 $Y^*=CYC$，
所以有界扰动的完整伴随公式给
$$
T^*=X^*-Y^*=CTC.
\tag{6.1}
$$
特别，对 $f,g\in\operatorname{Dom}T$，
$$
B(Tf,g)=B(f,Tg).
\tag{6.2}
$$

取 $v,w\in M=\ker T$。第4节保证 $b_jv\in\operatorname{Dom}T$，所以
$$
\begin{aligned}
B([b_j,T]v,w)
&=B(b_jTv,w)-B(Tb_jv,w)\\
&=-B(b_jv,Tw)=0.
\end{aligned}
\tag{6.3}
$$
(6.3) 不要求 $b_j$ 为 $C$ 对称算子。
沿 (1.4) 除以 $a_j$，再用 (5.4) 的强收敛，即得
$$
B(v,w)=0.
$$
这证明 (1.5)。

由 (6.1)，$\ker T^*=CM$，所以
$$
\overline{\operatorname{Ran}T}=(CM)^\perp.
$$
结合 $M\perp CM$，即得 (1.6)。

最后证明 (1.7) 自动给 (1.4)。
若在非零 $a_j$ 的无限集合上不存在所需子列，则存在 $\varepsilon>0$ 和 $J$，
使得对所有 $j\ge J$ 且 $a_j\ne0$，
$$
\eta_{j-1}/|a_j|\ge\varepsilon.
$$
于是包括零项在内都有 $|a_j|\le\varepsilon^{-1}\eta_{j-1}$。
这迫使 $a\in\ell^1$，与 (1.7) 矛盾。
因此每个复 $\ell^2\setminus\ell^1$ 行都能采用第4–6节的同一机制。

## 7. 危险点态平方的实际应用

令
$$
u=\sum_j a_j\chi_j,\qquad
j_0=\min\{j:a_j\ne0\},\qquad a=a_{j_0}.
$$
此节 $X=X_u$ 不另含常数项。R176 的 Bell 公式给点态
$u^2-a^2$ 的真实闭乘子
$$
P=X^2+\mathcal B_2-a^2I,\qquad
\operatorname{Dom}P=\operatorname{Dom}X^2.
\tag{7.1}
$$
取 (1.8) 的实际平方根 $Y$。它与 $X$ 的完整域及全部自然幂交换。
因而
$$
P=(X+Y)(X-Y)
\quad\text{于 }\operatorname{Dom}X^2.
\tag{7.2}
$$
R142/R144 已证明安全因子 $X+Y$ 单射；其最低实际系数不发生抵消。

这里两种核的相等也有实际域依据。
若 $Px=0$，则 $x\in\operatorname{Dom}X^2$，(7.2) 与安全因子的单射给
$(X-Y)x=0$。
反之，若 $x\in\operatorname{Dom}X$ 且 $Xx=Yx$，
则由 $Y$ 的域交换，$Yx\in\operatorname{Dom}X$，
故 $x\in\operatorname{Dom}X^2$，并且 $Px=0$。
因此
$$
\ker P=\ker(X-Y).
\tag{7.3}
$$

只要 (1.4) 成立，特别对每个复 $\ell^2\setminus\ell^1$ 行，
$$
\boxed{
B(\ker P,\ker P)=0,\qquad
\ker P\subseteq\overline{\operatorname{Ran}(X-Y)}.
}
\tag{7.4}
$$
由于 $P$ 本身也为 $C$ 自伴，(7.3) 还给
$$
\boxed{\ker P\subseteq\overline{\operatorname{Ran}P}.}
\tag{7.5}
$$
对慢 $\ell^1$ 行，只需直接检查 (1.4)，无需假设 $X$ 无界。

## 8. 一般接口和未消除的障碍

第6节使用的准确抽象接口是：$T$ 为 $C$ 自伴闭算子，
存在有界 $b_n$ 保持其域，使真实交换子延为有界算子，
且某非零标量 $\lambda_n$ 满足
$$
[b_n,T]/\lambda_n\to I
\quad\text{强收敛}.
$$
那么 $\ker T$ 全等向。
第2–5节专门证明本题实际平方分支确实满足该接口。

全等向空间可以非零，(1.5) 本身不排除一般慢平方核。
本证明也不产生任意固定柱函数 $\psi$ 的局部化等式
$B(\psi M,M)=0$。
若试图使用 $[\psi b_j,T]$，会出现
$$
[\psi b_j,T]
=\psi[b_j,T]+[\psi,T]b_j.
$$
即使已知 $b_j\to0$ 强收敛，第二项除以 $a_j\to0$ 后也没有自动消失。
未知核向量并无已证的 $\|b_jv\|=o(|a_j|)$ 控制。
因而不能把 (1.5) 加上本质全支撑直接升级为零核。

R207 的有限头成本和其指数权附录仍是独立必要条件。
本文增加的是实际配对约束及闭值域包含；尚未给出与那些成本下界相冲突的统一上界。
