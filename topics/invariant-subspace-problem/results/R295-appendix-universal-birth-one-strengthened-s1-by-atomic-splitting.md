# R295 附录：任意正权出生一的统一加强 S1 与真实混合平方

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：以下统一常数定理已证明。** 对任意有限正权 Boolean 行、整个出生一和全部合法高度，R293 的加强 S1 成立，常数可统一取 $\kappa=1024$。有限维缺陷严格正定。任意可数无限正 $\ell^2$ 行也有同一常数的非严格结论。本文保留真实完整 Schur 及实际三次桥创新；没有将这项出生一结论外推到一般出生或 graph $\Gamma$。

输入为[出生一 Turán 余量与参数相关加强 S1](R295-birth-one-turan-remainder-law-and-all-height-strengthened-s1.md)的准确概率目标与 $\kappa=\rho_k$ 结论。本文新增是消去任意正权上无界的 $\rho_k$。证明所用有限常数没有优化。

## 1. 定理及准确目标

取 $M\ge3$ 个正权 $b_i$，$z_i=b_i^2$。在同一个物理 $K_1=b^\perp$ 上使用
$$
\Gamma_n=P_{K_1}\left[\frac{d^n(d^*)^n}{(n!)^2}\bigg|_{\mathcal H_1}\right]^{-1}\bigg|_{K_1},
\qquad C_n=\Gamma_n^{-1},\qquad0\le n\le M-2.
$$
完整矩阵先求逆，再压到 primitive 源。最高处置真实下一精度 $C_{M-1}=0$。令 $L_j=1/e_j(z)$ 为出生零 Gram，$B$ 为真实三次桥，按 R293 定义
$$
\delta_{n+1}=\frac1{n+1}(C_nB^*L_{n+2}-C_{n-1}B^*L_{n+1}),
$$
$$
E_n^{(\kappa)}=\kappa C_n\Gamma_{n-1}C_n-C_{n+1}
-\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*.
\tag{1.1}
$$

**定理。** 对全部 $1\le n\le M-2$，
$$
\boxed{E_n^{(1024)}>0\quad\text{于整个 }K_1.}
\tag{1.2}
$$
特别地，在具有下一合法 Gram 的内部高度，
$$
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\prec1024\Gamma_{n-1}.
\tag{1.3}
$$

以下证明在同一个有限概率坐标空间完成。置 $k=n+1$，故 $2\le k\le M-1$。设
$$
\mu_j(I)=z_I/e_j,\qquad p_j=\mathbb E_{\mu_j}\mathbf1_I,
\qquad\Sigma_j=\operatorname{Cov}_{\mu_j}(\mathbf1_I),
$$
$$
\rho=\frac{e_k^2}{e_{k-1}e_{k+1}},\qquad
q=2p_k-p_{k-1}-p_{k+1}.
$$
上述输入已付完整同余：$E_n^{(\kappa)}>0$ 等价于
$$
\boxed{\mathcal D_k^{(\kappa)}
=\kappa\rho\Sigma_k\Sigma_{k-1}^{\dagger}\Sigma_k
-\Sigma_{k+1}-qq^*>0\quad\text{于 }\mathbf1^\perp.}
\tag{1.4}
$$
这里 $\Sigma_{k-1}>0$ 于 $\mathbf1^\perp$，最高端 $k=M-1$ 使用真实 $\Sigma_M=0$。输入还给 $\mathcal D_k^{(\rho)}>0$：其 Turán 余量测度对所有 $Y=2\mathbf1_I$, $|I|=k$ 都有正质量，所以余量协方差严格正定于 $\mathbf1^\perp$。

## 2. 最大原子分区和准确交换配分

令 $p_{\max}=\max_I\mu_k(I)$。已付的相同交集／对称差分拆给
$$
\rho^{-1}=\mathbb E_{I,J\text{ 独立}\sim\mu_k}\frac{|I\setminus J|}{|I\setminus J|+1}
\ge\frac{1-p_{\max}}2.
\tag{2.1}
$$
因此若 $p_{\max}\le1/2$，已有 $\rho\le4$，(1.4) 由参数相关结论立即成立。以下只研究 $p_{\max}>1/2$。

取最大权 $k$ 元子集 $S$，补集为 $T$，$|T|=M-k\ge1$。记
$$
a_i=z_i^{-1}\ (i\in S),\qquad c_j=z_j\ (j\in T),
\quad A_0=\sum_{i\in S}a_i,\quad C_0=\sum_{j\in T}c_j,
$$
$$
\tau=A_0C_0,\qquad \alpha_i=a_i/A_0,\qquad\beta_j=c_j/C_0.
\tag{2.2}
$$
$\alpha,\beta$ 分别是两个非空组上的严格正概率向量。它们以下作为全 $M$ 维向量时，在另一组上补零。

任何大小 $k$ 的子集都唯一写成从 $S$ 删除 $r$ 位、从 $T$ 加入 $r$ 位。大小 $k-1$、$k+1$ 时，删除／加入数分别为 $(r+1,r)$、$(r,r+1)$。因此定义
$$
W=\sum_{r\ge0}\tau^r e_r(\alpha)e_r(\beta),
$$
$$
W_-=\sum_{r\ge0}\tau^r e_{r+1}(\alpha)e_r(\beta),\qquad
W_+=\sum_{r\ge0}\tau^r e_r(\alpha)e_{r+1}(\beta),
\tag{2.3}
$$
其中超出组大小的项为零。有准确的实际配分式
$$
e_k=z_S W,\qquad e_{k-1}=z_S A_0 W_-,\qquad
e_{k+1}=z_S C_0 W_+,
$$
$$
\boxed{\rho=\frac{W^2}{\tau W_-W_+}.}
\tag{2.4}
$$
又 $p_{\max}=1/W>1/2$，而 $W\ge1+\tau$，所以
$$
1\le W<2,\qquad0<\tau<1.
\tag{2.5}
$$
从概率向量的 $e_r\le1/r!$ 得
$$
1\le W,W_-,W_+\le e^\tau<3.
\tag{2.6}
$$
若 $\tau\ge1/256$，则 (2.4)–(2.5) 已给 $\rho<4/\tau\le1024$，仍由参数相关结论关闭。故只余
$$
\boxed{0<\tau\le1/256.}
\tag{2.7}
$$

## 3. 真实首交换度量的共同正交分解

在 $S$ 与 $T$ 两组上分别定义嵌入的 categorical 协方差
$$
U=\operatorname{diag}(\alpha)-\alpha\alpha^*,\qquad
V=\operatorname{diag}(\beta)-\beta\beta^*,
$$
$$
h=-\alpha+\beta,\qquad H=hh^*,\qquad G=U+V+H.
\tag{3.1}
$$
这些矩阵的共同核含 $\mathbf1$。在 $\mathbf1^\perp$ 上，$G>0$。确切地，$U$ 的像是 $S$ 组内和为零的空间，$V$ 的像是 $T$ 组内和为零的空间，$h$ 在两组上的和分别为 $-1,1$；三者直和的维数为
$$
(k-1)+(M-k-1)+1=M-1.
$$

作同一个与三个高度无关的合同 $G^{-1/2}$，将 $G$ 变成 $I$。此时 $U,V,H$ 变成互相正交的投影。一个直接理由是：取它们的满列秩平方根，合并列后的方阵可逆；用 $G^{-1/2}$ 左乘后，其乘自身伴随等于 $I$，因而该方阵为酉矩阵，三组列彼此正交。

记变换后的 $U$ 为 $\Pi$，则 $V+H$ 变成 $I-\Pi$。定义两个共用实际二次型
$$
K_-=U+\tau(V+H),\qquad K_+=\tau U+V+H.
\tag{3.2}
$$
在上述坐标中它们分别是
$$
K=\Pi+\tau(I-\Pi),\qquad N=\tau\Pi+I-\Pi,
\qquad \boxed{\tau K^{-1}=N.}
\tag{3.3}
$$
这是整个真实源上的共同合同，不是假设原物理坐标中的 $U,V,H$ 欧氏正交。

## 4. 无放回矩与独立重复抽样的严格比较

写 $s_0=\mathbf1_S$。在三个实际子集分布中令
$$
X=\mathbf1_I-s_0,\quad
X_-=\mathbf1_{I_-}-s_0,\quad
X_+=\mathbf1_{I_+}-s_0.
$$
分别按交换数 $r$ 分组。

固定 $r$ 的无放回集合和，乘 $r!$ 或 $(r+1)!$ 后，恰是对应有序互异抽样的和。将互异条件删除，只增加非负的向量外积项。因此每个以下二次矩上界都是矩阵 Loewner 上界，并非逐坐标估计。

对中间层，从 $\alpha$、$\beta$ 各独立重复抽 $r$ 次，所得占据差的均值为 $rh$，协方差为 $r(U+V)$。于是第 $r$ 个未归一无放回二次矩至多
$$
\frac{\tau^r}{(r!)^2}\{r(U+V)+r^2H\}
\preceq\frac{r^2\tau^r}{(r!)^2}G.
\tag{4.1}
$$
$r=1$ 的实际项准确为 $\tau G$。

对下层，重复抽 $r+1$ 次 $\alpha$、$r$ 次 $\beta$，并在占据差上加固定向量 $\alpha$，其均值为 $rh$、协方差为 $(r+1)U+rV$。第 $r$ 项的未归一二次矩至多
$$
\frac{\tau^r}{(r+1)!r!}\{(r+1)U+rV+r^2H\}.
\tag{4.2}
$$
$r=0$ 项的实际均值为零、二次矩为 $U$。

对上层改为从占据差减去 $\beta$，同样得到
$$
\frac{\tau^r}{r!(r+1)!}\{rU+(r+1)V+r^2H\},
\tag{4.3}
$$
而 $r=0$ 的实际均值为零、二次矩为 $V$。当 $|T|=1$ 的最高硬端，有些实际项不存在；删除互异条件后的这些正上界仍然有效。

下面使用 $0<\tau\le1$ 时的简单标量估计
$$
e^\tau<3,\qquad e^\tau-1\le2\tau,
\qquad \sum_{r\ge2}\frac{r^2\tau^r}{(r!)^2}
\le\tau(e^\tau-1)\le2\tau^2.
\tag{4.4}
$$

## 5. 三个真实协方差与实际均值创新的共同预算

### 5.1 中间层是同一度量的可控扰动

由 (4.1)–(4.4)，存在 $0\preceq R\preceq2\tau^2G$，使
$$
\mathbb E XX^*=\frac\tau W G+\frac RW.
$$
令 $m=\mathbb E X$。中间层 $X\ne0$ 的概率为 $(W-1)/W\le2\tau/W$。对这个事件使用向量 Cauchy–Schwarz，得
$$
mm^*\preceq\frac{2\tau}{W}\mathbb E XX^*
\preceq\frac{6\tau^2}{W^2}G.
\tag{5.1}
$$
所以在第3节共同合同坐标中，
$$
\boxed{\Sigma_k=\frac\tau W(I+E),\qquad E=E^*,\qquad\|E\|\le6\tau.}
\tag{5.2}
$$
确切地，减去 $mm^*$ 的下误差在归一后至少为 $-6\tau/W$，正误差至多 $2\tau$，而 $W\ge1$。这里 $E$ 是实际协方差的误差，保留其全部非对角项。

### 5.2 两个相邻层

协方差不超过对任意固定中心的二次矩。将 (4.2)–(4.3) 相加，使用 $W_\pm\ge1$，得到
$$
\boxed{\Sigma_{k-1}\preceq3\{U+\tau V+\tau H\}=3K_-,}
$$
$$
\boxed{\Sigma_{k+1}\preceq3\{\tau U+V+\tau H\}\preceq3K_+.}
\tag{5.3}
$$
例如 (4.2) 的 $U$ 系数由 $\sum\tau^r/(r!)^2\le e^\tau<3$ 控制；$V,H$ 系数分别至多 $\tau e^\tau<3\tau$。其余一式对称。

### 5.3 真正的均值二阶差

令
$$
\varepsilon_- =\mathbb E X_-+\alpha,\qquad
\varepsilon_+ =\mathbb E X_+-\beta.
$$
两者的 $r=0$ 项均值严格为零。$r\ge1$ 的总概率至多 $2\tau/W_\pm$，其相应中心化二次矩由 (4.2)–(4.4) 至多 $3\tau G/W_\pm$。故
$$
\varepsilon_-\varepsilon_-^*\preceq6\tau^2G,\qquad
\varepsilon_+\varepsilon_+^*\preceq6\tau^2G.
\tag{5.4}
$$
实际二阶均值差准确为
$$
\boxed{q=-h+2m-\varepsilon_- -\varepsilon_+.}
\tag{5.5}
$$
由于 $\tau G\preceq K_+$，(5.1)、(5.4) 分别给 $m$、$\varepsilon_-$、$\varepsilon_+$ 的 $K_+^{-1}$ 范数至多 $\sqrt{6\tau}$；$h$ 在该范数中恰为一。因此在 (2.7) 的小 $\tau$ 区间，
$$
\|q\|_{K_+^{-1}}\le1+4\sqrt{6\tau}
\le1+\frac{\sqrt6}{4}<\sqrt3.
$$
所以
$$
\boxed{qq^*\preceq3K_+,\qquad
\Sigma_{k+1}+qq^*\preceq6K_+.}
\tag{5.6}
$$
这一步估计的是同一实际 $q=2p_k-p_{k-1}-p_{k+1}$，没有用独立任取的创新代替它。

## 6. 保真实平方次序的加权扰动下界

继续在第3节的共同合同坐标中。设
$$
A=\Sigma_{k-1},\qquad B=\Sigma_k.
$$
由 (5.3)，$A\preceq3K$ 且 $A>0$。于是对实际 $B$ 作同余，
$$
B A^{-1}B\succeq\frac{\tau^2}{3W^2}(I+E)K^{-1}(I+E).
\tag{6.1}
$$
现在控制其中完整的非交换乘积。$K$ 的谱属于 $\{\tau,1\}$，所以
$$
\|K^{-1/2}E K^{1/2}\|
\le\frac{\|E\|}{\sqrt\tau}\le6\sqrt\tau\le\frac38.
\tag{6.2}
$$
对 (6.1) 中间矩阵作 $K^{1/2}$ 同余，得到
$$
K^{1/2}(I+E)K^{-1}(I+E)K^{1/2}
=\bigl(I+K^{-1/2}EK^{1/2}\bigr)^*
\bigl(I+K^{-1/2}EK^{1/2}\bigr)
\succeq\left(\frac58\right)^2I\succeq\frac13I.
$$
因此
$$
BA^{-1}B\succeq\frac{\tau^2}{9W^2}K^{-1}.
\tag{6.3}
$$
这不是从 $B\succeq cG$ 直接推出平方的错误保序；(6.2) 明确支付了两种度量之间的真实方向变化。

乘准确的 (2.4)，使用 $W_-W_+<9$ 与 $\tau K^{-1}=N$，得到
$$
\boxed{\rho B A^{-1}B
\succeq\frac{\tau}{9W_-W_+}K^{-1}
\succeq\frac1{81}N.}
\tag{6.4}
$$
结合 (5.6)，小 $\tau$ 区间已满足
$$
486\rho B A^{-1}B\succeq\Sigma_{k+1}+qq^*.
\tag{6.5}
$$
取 $\kappa=1024$ 后，因为 $N>0$，缺陷严格正定。其余两区分别由 $\rho\le4$ 或 $\rho\le1024$ 以及 $\mathcal D_k^{(\rho)}>0$ 关闭。这完成 (1.2) 对所有有限正权、全部合法高度的证明。硬端中 $\Sigma_M=0$ 已贯穿所有步骤，没有新增非法高度。

## 7. 任意无限正 $\ell^2$ 行的实际物理极限

取任意可数无限正 $b\in\ell^2$。固定有限 $n\ge1$。[R294 §5](R294-birth-one-uniform-diagonal-gram-comparison-and-common-newton-blocks.md)中独立于外部协方差下界的论证已证明相应完整 $F_j$ 是无核的正 Fredholm 算子，故对每个固定有限 $j$ 有有界逆；同一物理 $\Gamma_j$ 及其精度均有界且严格正。

取首 $N$ 位有限行并令外部权为零。在共同的单孔 $\ell^2$ 空间上，$b^{(N)}$ 的正交补包括首 $N$ 位的真正 $K_1$ 和所有外部单孔坐标。头内已有 (1.2)。在外部单孔坐标上，真实直和延拓为
$$
\Gamma_j^{(N)}=\frac1{e_j(z_1,\ldots,z_N)}I,\qquad
C_j^{(N)}=e_j(z_1,\ldots,z_N)I,\qquad\delta^{(N)}=0.
$$
因此该外部块的加强缺陷为
$$
1024\frac{e_n(z_{\le N})^2}{e_{n-1}(z_{\le N})}
-e_{n+1}(z_{\le N})\ge0,
$$
由标量 Newton 不等式得到。于是有限头结论确实先延到整个共同空间中的 $(b^{(N)})^\perp$。

R294 的固定高度范数极限给 $P_N\to P$、完整 $F_j^{(N)}\to F_j$ 及实际 $\Gamma_j^{(N)}\to\Gamma_j$、$C_j^{(N)}\to C_j$；三次桥及其创新也按相同有限头式收敛。故可直接将上述有界物理缺陷的非负性传到无限行：
$$
\boxed{E_n^{(1024)}\succeq0\qquad(n\ge1).}
\tag{7.1}
$$
继而有整个无限出生一的真实算子相邻序
$$
\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
\preceq1024\Gamma_{n-1}\qquad(n\ge1).}
\tag{7.2}
$$
常数相同覆盖每个有限高度；不宣称增长高度下有限头收敛的额外速率。无限证明完全在有界的原物理算子中取极限，不把无限概率协方差的伪逆或对角 $\operatorname{diag}(b)^{-1}$ 当成有界算子，也不由范数极限免费保留有限维严格号。

## 8. 已完成范围

本稿给任意正权的整个出生一、全部高度、真实三次桥创新与完整同源逆的统一有限加强常数。原连续尾已有更小的 $674/81$，无需用本稿常数覆盖它。一般出生的下层 nuisance 特征并非只有常数，不能把本稿三成分 $U,V,H$ 及首交换矩阵直接移植。R293 的全出生统一常数量词和原 graph 的跨出生返回接口仍需另证。
