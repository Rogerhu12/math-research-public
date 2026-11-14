# 同源正交支付最高负 Johnson 通道与交集多项式自由度

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：以下恒等式与非负通道结论已证明。** 它们使用完整回归源的全局正交，把前一分拆稿中偶数出生的 $j=s-1$ 负平方准确支付掉。经过同一个全局二次型的重新分拆，所有剩余负项都在 $j\le s-2$。这里仍没有证明这些剩余项非负，也没有证明高出生加强 S1 或原 graph 的预算。交集多项式的自由度来自 root 提出的同源正交观察；本文保留其合法次数和取值限制。

依赖：[R296 完整回归与真实创新](../results/R296-all-birth-residual-regression-two-band-lift-and-physical-innovation.md)、[R296 同源二阶差](../results/R296-appendix-complete-regression-second-difference-and-common-source-invariance.md)，以及[前一完整 Johnson 分拆稿](2026-11-14-all-degree-pair-splitting-johnson-identity-and-arithmetic-obstruction-789f-next.md)。下面列出全部本稿使用的源和通道公式。

## 1. 原二次型及没有更换的源

取有限 $M$ 个正权 $b_i$，$z_i=b_i^2$，$d=\sum b_iE_i$。固定
$$
s\ge1,\qquad h=M-2s\ge1,\qquad 1\le n\le h,\qquad k=s+n.
$$
对同一个 $f\in K_s(d)$ 令
$$
\Phi(I)=\sum_{J\subset I,\ |J|=s}\frac{f_J}{b_J},\qquad
q_j=\Pi_{\le s-1}^{(j)}\Phi,
$$
$$
p=\Phi-q_k,\qquad g=q_k-q_{k-1},\qquad
\ell=\Pi_{\le s-2}^{(k+1)}(p-g).
\tag{1.1}
$$
这里 $q_j$ 取齐次 $(s-1)$ 次代表，$s=1$ 时 $\ell=0$；$s\ge2$ 时 $\ell$ 取齐次 $(s-2)$ 次代表。常数和所有低次数 nuisance 均保留。准确有
$$
p\perp\mathcal P_{\le s-1}\quad\text{于第 }k\text{ 切片},\qquad
p+g\perp\mathcal P_{\le s-1}\quad\text{于第 }k-1\text{ 切片},
$$
$$
\mathsf Z_nf=p-g-\ell\quad\text{于第 }k+1\text{ 切片}.
\tag{1.2}
$$
记 $C_j=\Gamma_{j,s}^{-1}$，硬端 $C_{h+1}=0$；低出生 Gram 为 $L_j=\Gamma_{j,s-1}$。未归一范数为 $\|a\|_t^2=\sum_{|I|=t}z_I|a(I)|^2$。因此
$$
\|p\|_k^2=\langle C_nf,f\rangle,\quad
\|p+g\|_{k-1}^2=\langle C_{n-1}f,f\rangle,
$$
$$
\|p-g-\ell\|_{k+1}^2
=\langle(C_{n+1}+\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*)f,f\rangle.
\tag{1.3}
$$
所分拆的始终是同一个真实二次型
$$
\boxed{\mathcal A_{s,n}=2e_kC_n-e_{k+1}C_{n-1}
-e_{k-1}(C_{n+1}+\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*).}
\tag{1.4}
$$
这里的 $C_n\Gamma_{n-1}C_n$ 尚未被 (1.4) 取代；算术二次型与原加强目标的区别仍按前稿保留。

## 2. 全局可选择的相位

对任意 $\varepsilon\in\{1,-1\}$，独立求和及 (1.2) 的均值零给
$$
\sum_{|I|=|J|=k}z_Iz_J|p(I)+\varepsilon p(J)|^2
=2e_k\|p\|_k^2,
\tag{2.1}
$$
$$
\begin{aligned}
&\sum_{|I_-|=k-1,\ |I_+|=k+1}z_{I_-}z_{I_+}
|(p+g)(I_-)+\varepsilon(p-g-\ell)(I_+)|^2\\
&\qquad=e_{k+1}\|p+g\|_{k-1}^2+e_{k-1}\|p-g-\ell\|_{k+1}^2.
\end{aligned}
\tag{2.2}
$$
在 (2.2) 中，只需第 $k-1$ 切片上的 $p+g$ 均值零，故 $s=1$ 也无需额外假设 $\mathsf Z_n f$ 的均值。

所以无论选哪个全局相位，(2.1) 减 (2.2) 都准确等于 $\langle\mathcal A_{s,n}f,f\rangle$。这不是逐个交集任意改符号；下一节使用同一个固定 $\varepsilon$。

## 3. 同一条件 Johnson 分解

固定不交集合 $A,D$，$|A|=k-r$、$|D|=2r$。中央对子为
$$
I=A\cup X,\quad J=A\cup(D\setminus X),\quad |X|=r;
$$
相邻对子使用 $|X|=r-1$。两者单项权均为 $z_A^2z_D$。

在 $D$ 上置 $\partial=\sum_{i\in D}E_i$、$U=\partial^*$、$\mathcal K_j=\ker\partial\cap\mathcal H_j(D)$。对局部多项式 $a(A\cup X)$，将其齐次系数 $a_\nu$ 完整分解为
$$
a_\nu=\sum_j\frac{U^{\nu-j}}{(\nu-j)!}a_{j,\nu},\qquad a_{j,\nu}\in\mathcal K_j,
$$
并写
$$
H_j^a(t)=\sum_{\nu=j}^{\min(\deg a,2r-j)}\binom{t-j}{\nu-j}a_{j,\nu}.
\tag{3.1}
$$
不同 $j$ 在切片上正交，且
$$
\sum_{|X|=t}|\Phi_{j,u}(X)|^2=\binom{2r-2j}{t-j}\|u\|^2,
\qquad \Phi_{j,u}(D\setminus X)=(-1)^j\Phi_{j,u}(X).
\tag{3.2}
$$
置 $c_{r,j}=\binom{2r-2j}{r-j}$、$\tau_{r,j}=(r-j)/(r-j+1)$。中央及相邻系数为
$$
S_{j,\varepsilon}^0=(1+\varepsilon(-1)^j)H_j^p(r),
$$
$$
\begin{aligned}
S_{j,\varepsilon}^-={}&H_j^p(r-1)+\varepsilon(-1)^jH_j^p(r+1)\\
&+H_j^g(r-1)-\varepsilon(-1)^jH_j^g(r+1)
-\varepsilon(-1)^jH_j^\ell(r+1).
\end{aligned}
\tag{3.3}
$$
所以每个条件块的差仍为
$$
\sum_{j=0}^r c_{r,j}
\bigl(\|S_{j,\varepsilon}^0\|^2-\tau_{r,j}\|S_{j,\varepsilon}^-\|^2\bigr).
\tag{3.4}
$$
$\tau_{r,r}=0$ 保留真正硬端；当 $r=0$，没有相邻对子，中央项为 $2(1+\varepsilon)|p(A)|^2\ge0$。

### 3.1 同时支付最高两通道

现在固定
$$
\boxed{\varepsilon=(-1)^{s-1}.}
\tag{3.5}
$$
若 $j=s\le r$，$H_s^p$ 为常数且 $H_s^g=H_s^\ell=0$；(3.3) 两个系数都为零。若 $j=s-1\le r$，$H_j^p$ 至多一次、$H_j^g$ 为常数、$H_j^\ell=0$。此时 $\varepsilon(-1)^j=1$，从而
$$
S_{s-1,\varepsilon}^0=S_{s-1,\varepsilon}^-=2H_{s-1}^p(r).
$$
其完整贡献准确为
$$
\boxed{4c_{r,s-1}(1-\tau_{r,s-1})\|H_{s-1}^p(r)\|^2\ge0.}
\tag{3.6}
$$
在 $r=s-1$ 的硬端，公式仍成立，$\tau=0$。若实际分解使一次系数为零，就按零系数理解，不向不存在的局部源延拓。

由于 $\deg p\le s$，不存在 $j>s$ 的通道。因此得到：
$$
\boxed{\text{同一个 }\mathcal A_{s,n}\text{ 有一个完整条件分拆，全部负项均在 }j\le s-2.}
\tag{3.7}
$$
特别地，前稿偶数 $s$ 时的 $j=s-1$ 负平方已被同源全局正交支付。不是把该平方删去；是用 (2.1)—(2.2) 的准确恒等把整个全局二次型重新分拆。

### 3.2 首个尚未支付的通道

设 $s\ge2$、$j=s-2\le r$。则 $H_j^p$ 至多二次、$H_j^g$ 至多一次、$H_j^\ell$ 为常数，且 $\varepsilon(-1)^j=-1$。用通常一元多项式导数 $\partial_t$，准确有
$$
S_{j,\varepsilon}^0=0,
\qquad
S_{j,\varepsilon}^-=2\bigl(H_j^g(r)-\partial_tH_j^p(r)\bigr)+H_j^\ell.
$$
因此该通道是
$$
\boxed{-c_{r,s-2}\tau_{r,s-2}
\left\|2\bigl(H_{s-2}^g(r)-\partial_tH_{s-2}^p(r)\bigr)+H_{s-2}^\ell\right\|^2.}
\tag{3.8}
$$
这里 $\ell$ 是同一个完整新切片正交投影，不可设为零或独立选择。$r=s-2$ 时 $\tau=0$，该相邻通道不存在。

出生一时 (3.7) 已没有剩余负通道，恢复 R295 算术步骤。出生二及以上，(3.8) 明确显示还欠的实际共同项；没有由次数下降直接宣称归纳闭合。

## 4. 两切片共同代表中的同一个结论

将 Boolean 多项式按 $x_i^2=x_i$ 多线性化，定义
$$
p^\sharp(I)=p(I)-(|I|-k)g(I).
\tag{4.1}
$$
它的次数仍不超过 $s$，并且
$$
p^\sharp=p+g\ (|I|=k-1),\qquad
p^\sharp=p\ (|I|=k),\qquad
p^\sharp=p-g\ (|I|=k+1).
\tag{4.2}
$$
所以 $p^\sharp$ 同时正交前两张切片的全部 $\le s-1$ 次特征，且
$$
\mathsf Z_nf=(I-\Pi_{\le s-2}^{(k+1)})p^\sharp,
\qquad \ell=\Pi_{\le s-2}^{(k+1)}p^\sharp.
\tag{4.3}
$$
这也可由 R296 的 $f\mapsto f+d^*u$ 同商代表变换取得；不声称新代表仍在物理 $K_s$。在这一规范中，(3.8) 写成
$$
-c_{r,s-2}\tau_{r,s-2}
\|H_{s-2}^\ell-2\partial_tH_{s-2}^{p^\sharp}(r)\|^2.
\tag{4.4}
$$
$g$ 已进入 $p^\sharp$ 的最高系数，故 (4.4) 不能解释为删除拟合差的费用。

## 5. 合法的交集多项式自由度

令 $q$ 为任意实多项式，$\deg q\le s-1$。固定 $J$ 时，Boolean 函数 $q(|I\cap J|)$ 对 $I$ 是次数至多 $s-1$ 的多项式。因此 (1.2) 逐个 $J$ 给
$$
\sum_{|I|=|J|=k}z_Iz_J q(|I\cap J|)p(I)\overline{p(J)}=0,
\tag{5.1}
$$
$$
\sum_{|I_-|=k-1,\ |I_+|=k+1}z_{I_-}z_{I_+}
q(|I_-\cap I_+|)(p+g)(I_-)\overline{(p-g-\ell)(I_+)}=0.
\tag{5.2}
$$
第二式仍只用左因子的完整低次数正交。

若 $|q(a)|\le1$ 于所用全部整数交集大小，则每一对的表达
$$
|u|^2+|v|^2+2q(a)\operatorname{Re}(u\overline v)
=\frac{1+q(a)}2|u+v|^2+\frac{1-q(a)}2|u-v|^2
\tag{5.3}
$$
为两个平方的非负混合。把 (2.1)、(2.2) 的配对平方分别换为 (5.3)，其全局值仍严格不变。

实际上中央与相邻一侧可以各选一个满足这些条件的 $q_0,q_1$，因为 (5.1)、(5.2) 独立成立。取同一个多项式是其特例。一个简单充分取值范围是 $a=0,1,\ldots,k$；有限 $M$ 时可缩到真正出现的交集范围。

为记录全部次序，令 $\lambda_r=q_0(k-r)$、$\eta_r=q_1(k-r)$，并置
$$
A_j=H_j^p(r-1)+H_j^g(r-1),\qquad
B_j=H_j^p(r+1)-H_j^g(r+1)-H_j^\ell(r+1).
$$
对应的第 $j$ 条件贡献准确为
$$
\boxed{c_{r,j}\left[
2(1+\lambda_r(-1)^j)\|H_j^p(r)\|^2
-\tau_{r,j}\left(\|A_j\|^2+\|B_j\|^2
+2\eta_r(-1)^j\operatorname{Re}\langle A_j,B_j\rangle\right)
\right].}
\tag{5.4}
$$
式 (3.4) 是 $q_0=q_1\equiv\varepsilon$ 的特例。不能任意逐个 $r$ 指定 $\lambda_r,\eta_r$：它们必须来自所述次数以内的实际多项式；超出 $[-1,1]$ 也不能继续称 (5.3) 为正混合。

## 6. 范围

所有公式对向量值源和算子 Gram 同样成立，故 (3.6)—(3.7) 保同一物理源上的二次型，而不是将非交换 Gram 标量化。有限硬端已由 $C_{h+1}=0$ 和 $\tau_{r,r}=0$ 分别保留。

对无限正 $\ell^2$ 权行的固定 $s,n$，只要使用 R296 已合法构造的完整 residual/MP 映射，以上配对和可直接取绝对收敛极限：各固定切片 $e_j<\infty$，残差的 $L^2$ 范数有限；交集函数在 $0,\ldots,k$ 上有界，所以 Fubini 与 Cauchy–Schwarz 支付 (2.1)、(2.2)、(5.1)、(5.2)。每个 $A,D$ 有限，条件 Johnson 身份不变。特别适用于原连续尾的这些固定层。

本文没有从固定层身份推出移动出生的统一常数；没有把 (3.8) 的真实 $\ell$ 换为局部投影；没有声称任意交集符号均被正交性允许。原高出生同源费用和完整 graph 仍待证明。
