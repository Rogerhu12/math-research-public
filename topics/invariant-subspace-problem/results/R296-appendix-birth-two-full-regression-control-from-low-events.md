# 出生二高原子坐标的完整仿射回归控制

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：以下三个相邻切片上的全仿射 Gram 比较与完整最优回归修正公式已证明。** 它把[首事件 ridge 回归](R296-appendix-birth-two-neighbor-regression-and-physical-birth-one-ridge.md)接回全部实际交换事件，不把截断最优系数当成完整系数。真实回归二阶差的最终加强 S1 预算尚未由此关闭。

使用[出生二共同商稿](R296-appendix-birth-two-common-quotient-and-two-exchange-scales.md)的 $S,T,\alpha,\beta,\tau$，假设 $0<\tau\le1$、$|S|,|T|\ge2$。所有内积先使用相对配分的未归一权；各切片归一常数对相应两个 Gram 同时相除，不改变比较。

## 1. 完整仿射 Gram 只比首事件多一个有界正项

在每个切片上，将 $r=0,1$ 的实际事件称为低事件，其余 $r\ge2$ 为高事件。对同一个仿射函数 $\ell$，记其两部分平方费用为 $\Lambda_{\rm low}(\ell)$、$\Lambda_{\rm high}(\ell)$。则三个切片均有
$$
\boxed{\Lambda_{\rm high}\preceq4\tau\Lambda_{\rm low},\qquad
\Lambda_{\rm low}\preceq\Lambda_{\rm full}\preceq(1+4\tau)\Lambda_{\rm low}.}
\tag{1.1}
$$
这些是完整仿射参数空间的二次型比较，保所有非对角项。

### 1.1 中间切片

写 $\ell(\Delta)=c+u\cdot\Delta$。首交换向量以 $\alpha_i\beta_j$ 取值 $-e_i+e_j$，令 $L_1=\ell(\Delta_1)$。低事件费用为
$$
\Lambda_{\rm low}=|c|^2+\tau\mathbb E|L_1|^2.
$$
在 $r$ 次独立重复首交换上，
$$
\ell(\Delta_1+\cdots+\Delta_r)
=\sum_{a=1}^r\ell(\Delta_a)-(r-1)c.
$$
删除互异限制并用 Cauchy–Schwarz，真实第 $r$ 次未归一费用至多
$$
\frac{\tau^r}{(r!)^2}
\{2r^2\mathbb E|L_1|^2+2(r-1)^2|c|^2\}.
$$
而 $\sum_{r\ge2}r^2\tau^r/(r!)^2\le2\tau^2$。故高事件总费至多
$$
4\tau^2\{\mathbb E|L_1|^2+|c|^2\}\le4\tau\Lambda_{\rm low}.
$$

### 1.2 下相邻切片

此处 $|R|=r+1,|Q|=r$。仿射函数可参数化为
$$
\ell(R,Q)=\sum_{i\in R}\eta_i+\sum_{j\in Q}w_j.
$$
记 $L_0=\sum_i\alpha_i|\eta_i|^2$，
$$
L_1=\sum_{P=\{i,i'\},j}\alpha_P\beta_j|\eta_i+\eta_{i'}+w_j|^2,
\qquad\Lambda_{\rm low}=L_0+\tau L_1.
$$
对 $r\ge2$，令 $c_r=\binom{r+1}{2}$。有准确平均式
$$
\ell(R,Q)=\frac1{c_r}\sum_{P=\{i,i'\}\subset R,j\in Q}
(\eta_i+\eta_{i'}+w_j)
-\frac{r-1}{r+1}\sum_{i\in R}\eta_i.
\tag{1.2}
$$
因此其平方至多
$$
\frac4{r+1}\sum_{P\subset R,j\in Q}|\eta_i+\eta_{i'}+w_j|^2
+\frac{2(r-1)^2}{r+1}\sum_{i\in R}|\eta_i|^2.
$$
补全固定 $P,j$ 或固定 $i$ 之外的位，分别给 $1/((r-1)!)^2$ 与 $1/(r!)^2$，所以第 $r$ 层费用至多
$$
\frac{4\tau^r}{(r+1)((r-1)!)^2}L_1
+\frac{2(r-1)^2\tau^r}{(r+1)(r!)^2}L_0.
$$
两系数对 $r\ge2$ 求和分别不超过 $4\tau^2$。于是高事件总费不超过
$4\tau^2(L_1+L_0)\le4\tau\Lambda_{\rm low}$。

### 1.3 上相邻切片和硬端

交换 $S,T$ 及 $\alpha,\beta$，得到同一个证明。若某组只有两位，高交换事件的一部分或全部不存在；删去这些正项不会破坏 (1.1)。特别最高硬端的上切片仍有完整仿射特征空间，不引入非法的二次残差逆。

## 2. 从真实低事件回归到完整回归

模切片上恒零的仿射函数后，$\Lambda_{\rm low}$ 正定。把仿射参数空间按该费用定为 Hilbert 空间 $\mathcal L$。高事件评价算子 $T:\mathcal L\to\mathcal H_{\rm high}$ 由 (1.1) 满足
$$
\boxed{\|T\|\le2\sqrt\tau.}
\tag{2.1}
$$

固定任意共同源函数 $F$，令 $\ell_0$ 为它在低事件上的唯一最优仿射回归修正，写
$$
R_0=\|F+\ell_0\|_{\rm low}^2,\qquad
g=(F+\ell_0)|_{\rm high}.
$$
由于低事件正规方程，任一附加修正 $x\in\mathcal L$ 的完整费用准确为
$$
R_0+\|x\|_{\mathcal L}^2+\|g+Tx\|_{\rm high}^2.
$$
因此完整回归修正和费用分别是
$$
\boxed{\ell_{\rm full}-\ell_0
=-(I+T^*T)^{-1}T^*g,}
\tag{2.2}
$$
$$
\boxed{R_{\rm full}
=R_0+\langle(I+TT^*)^{-1}g,g\rangle.}
\tag{2.3}
$$
特别
$$
\boxed{\|\ell_{\rm full}-\ell_0\|_{\mathcal L}
\le2\sqrt\tau\,\|g\|_{\rm high},}
$$
$$
\boxed{R_0+\frac{\|g\|^2}{1+4\tau}
\le R_{\rm full}\le R_0+\|g\|^2.}
\tag{2.4}
$$
这里所有逆都在同一完整仿射正规方程中；没有把一个独立的高事件最优源相加。

## 3. 中间二次源的显式回归误差

对共同商的 $F_{W,A,D}$，低事件最优修正是 $\ell_0=0$，且 $R_0=\tau G_1$。主稿的高交换估计给
$$
\|g\|_{\rm high}^2\le4\tau^2G_1+6\tau^2G_2.
$$
所以其真正完整最优仿射修正满足
$$
\boxed{\Lambda_{\rm low}(\ell_{\rm full})
\le16\tau^3G_1+24\tau^3G_2.}
\tag{3.1}
$$
这是一条保源商和实际低事件度量的系数预算，不是未经定范的普通坐标系数上界。

相邻两个切片的 $\ell_0$ 可使用[首事件 ridge 稿](R296-appendix-birth-two-neighbor-regression-and-physical-birth-one-ridge.md)的准确 $\eta_*,w_*$。式 (2.2) 则给它们通向完整最优系数的实际修正。要估计加强 S1 中的回归二阶差，仍需将三个系数放在同一物理低出生源里，并支付这些度量之间的变化；本稿未将三个独立的范数预算代替该步骤。
