# 出生二相邻切片的首事件回归：组内真实出生一精度

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：以下截取实际事件后的完整回归身份与下界已证明。** 使用[出生二共同商及两尺度稿](R296-appendix-birth-two-common-quotient-and-two-exchange-scales.md)的同一个 $(W,A,D)$，准确消去两个相邻切片的首两类事件上的全部仿射 nuisance。交叉块和组内二次块在这个真实 Schur 中正交；组内回归由真正的出生一精度控制。这里是完整残差的下界，不是整个相邻高度加强 S1。

## 1. 同一商与相邻分布

沿用主稿 $S,T,\alpha,\beta,\tau$；$|S|=k\ge3$、$|T|\ge2$，$W$ 在 $\alpha,\beta$ 两侧双中心。三个切片均模仿射函数使用
$$
F(R,Q)=\sum_{P\in\binom R2}A_P+\sum_{L\in\binom Q2}D_L-
\sum_{i\in R,j\in Q}W_{ij}.
$$
下切片 $|I|=k-1$ 对应 $|R|=r+1,|Q|=r$，归一因子是
$$
\mathcal Z_- =\sum_{r\ge0}\tau^r e_{r+1}(\alpha)e_r(\beta).
$$
上切片 $|I|=k+1$ 的计数相反，因子为
$$
\mathcal Z_+ =\sum_{r\ge0}\tau^r e_r(\alpha)e_{r+1}(\beta).
$$
本稿的 $\mathcal R_{k\pm1}$ 指整个对应切片、对全部仿射函数回归后的归一残差平方。

在 $S$ 的二元子集上记
$$
\nu_{\alpha,2}(P)=\alpha_P/e_2(\alpha),\quad
\bar A=\mathbb E_{\nu_{\alpha,2}}A_P,
$$
并写 $W_P(j)=W_{ij}+W_{i'j}$，其中 $P=\{i,i'\}$。

## 2. 下切片低事件的准确 Schur

当 $r=0$，只删除 $i\in S$，相对权为 $\alpha_i$，而 $F=0$。当 $r=1$，删除 $P=\{i,i'\}$ 并加入 $j\in T$，相对权为 $\tau\alpha_P\beta_j$，而
$$
F(P,\{j\})=A_P-W_P(j).
$$
任意仿射 nuisance 在这些事件上可唯一参数化为
$$
\eta_i\quad(r=0),\qquad \eta_i+\eta_{i'}+w_j\quad(r=1),
$$
其中 $\eta$、$w$ 均可自由取值。因此保留这些实际事件后，未归一最小费用准确为
$$
\inf_{\eta,w}\left\{
\sum_i\alpha_i|\eta_i|^2+
\tau\sum_{P,j}\alpha_P\beta_j
|A_P-W_P(j)+\eta_i+\eta_{i'}+w_j|^2\right\}.
\tag{2.1}
$$
先消去每个 $w_j$，就是对 $\nu_{\alpha,2}$ 减去均值。由于 $\sum_j\beta_jW_P(j)=0$ 对每个 $P$ 成立，所得 $A+\eta$ 项与 $W$ 项在 $\beta$ 平均后交叉准确为零。故 (2.1) 等于
$$
\boxed{\mathfrak R_{\alpha,\tau}(A)
+\tau e_2(\alpha)\sum_j\beta_j
\operatorname{Var}_{\nu_{\alpha,2}}W_P(j),}
\tag{2.2}
$$
其中
$$
\boxed{\mathfrak R_{\alpha,\tau}(A)
=\inf_\eta\left\{\|\eta\|_{\ell^2(\alpha)}^2+
\tau e_2(\alpha)\operatorname{Var}_{\nu_{\alpha,2}}
(A_P+\eta_i+\eta_{i'})\right\}.}
\tag{2.3}
$$
没有丢失完整低事件 nuisance，也没有把两个独立最小源的费用相加。

## 3. 回归算子是组内真正出生一精度

令 $\mathcal L_\alpha=\{\eta:\sum_i\alpha_i\eta_i=0\}$，并定义
$$
T_\alpha\eta=\sqrt{e_2(\alpha)}
\left(\eta_i+\eta_{i'}-
\mathbb E_{\nu_{\alpha,2}}(\eta_i+\eta_{i'})\right).
$$
目标 Hilbert 空间是 $L^2_0(\nu_{\alpha,2})$。有
$$
\boxed{\|T_\alpha\|\le1.}
\tag{3.1}
$$
直接证明：对 $\eta\in\mathcal L_\alpha$，
$$
\sum_{i<i'}\alpha_i\alpha_{i'}|\eta_i+\eta_{i'}|^2
=\sum_i\alpha_i(1-2\alpha_i)|\eta_i|^2
\le\sum_i\alpha_i|\eta_i|^2.
$$
再减去均值平方，只会减小左边。这正是 (3.1)。在物理等距变换 $\eta\mapsto(\sqrt{\alpha_i}\eta_i)$ 下，$T_\alpha^*T_\alpha$ 是权 $\sqrt\alpha$ 这一组的完整出生一精度 $C_1$；组只有两位时该精度为真实硬端零。

设
$$
F_A=\sqrt{e_2(\alpha)}(A-\bar A).
$$
(2.3) 中 $\eta$ 的常数部分只增加第一项，故最优 $\eta\in\mathcal L_\alpha$。完整 ridge Schur 给
$$
\boxed{\mathfrak R_{\alpha,\tau}(A)
=\tau\langle(I+\tau T_\alpha T_\alpha^*)^{-1}F_A,F_A\rangle,}
\tag{3.2}
$$
$$
\boxed{\frac\tau{1+\tau}e_2(\alpha)\operatorname{Var}_{\nu_{\alpha,2}}A
\le\mathfrak R_{\alpha,\tau}(A)
\le\tau e_2(\alpha)\operatorname{Var}_{\nu_{\alpha,2}}A.}
\tag{3.3}
$$
最优系数也有准确式
$$
\eta_*=-\tau(I+\tau T_\alpha^*T_\alpha)^{-1}T_\alpha^*F_A,
$$
$$
w_{*,j}=-\bar A-
\mathbb E_{\nu_{\alpha,2}}(\eta_{*,i}+\eta_{*,i'})+
\mathbb E_{\nu_{\alpha,2}}W_P(j).
\tag{3.4}
$$
特别，$\|\eta_*\|_{\ell^2(\alpha)}\le\tau\|F_A\|$，且
$\|\eta_*+\tau T_\alpha^*F_A\|\le\tau^2\|F_A\|$。$W$ 在低事件上只改变各个 $w_j$，不改变 $\eta_*$；这个独立性来自 (2.2) 的真实正交。

## 4. 对完整两个相邻残差的结论

从整个正费用中删除 $r\ge2$ 的项后再对同一 nuisance 取最小，给出
$$
\boxed{\mathcal R_{k-1}(W,A,D)\ge\frac1{\mathcal Z_-}
\left\{\mathfrak R_{\alpha,\tau}(A)+
\tau e_2(\alpha)\sum_j\beta_j
\operatorname{Var}_{\nu_{\alpha,2}}W_P(j)\right\}.}
\tag{4.1}
$$
交换 $S,T$ 以及 $\alpha,\beta,A,D$，同样得到
$$
\boxed{\mathcal R_{k+1}(W,A,D)\ge\frac1{\mathcal Z_+}
\left\{\mathfrak R_{\beta,\tau}(D)+
\tau e_2(\beta)\sum_i\alpha_i
\operatorname{Var}_{\nu_{\beta,2}}(W_{ij}+W_{ij'})\right\}.}
\tag{4.2}
$$
最高硬端 $|T|=2$ 时，$\nu_{\beta,2}$ 只有一个子集，(4.2) 右边准确为零，服从真正的上出生残差消失。

这些式子是相邻完整精度的实际正下界；$A,D$ 的常数 gauge 不改变所列方差。它们还不是所需混合逆的下界，也没有把截取事件上的最优回归系数当成全切片最优系数。要支付真正的 $\mathsf Z_n$，仍须控制其完整回归系数二阶差及高交换事件的反馈。
