# R236 附录：完整下一尾理想的商成本与实际正常锚

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的辅助加强。** 下面优化的是完整下一尾理想中的距离；原始 $G_j$ 范数大不能替代该商距离大。一般正常湮灭者与普通 ISP 仍开。

## 1. 保持全部原来源的记号

设原闭实际理想为
$$
\mathcal I=\overline{S_0\mathcal A'+Z_0\mathcal A'}^{\|\cdot\|},
$$
其中 $S_0$ 首形式阶一。使用 R236 已证的同一真实两生成元递推，
在当前第 $j$ 位写
$$
S_j=D_j(N_j+G_j),\qquad
Z_j=E_j+N_jF_j,
$$
$$
t_j=N_j^2=\eta_jN_{j+1},\qquad
h_j=G_j^2-t_j,\qquad k_j=E_j-G_jF_j.
$$
注意本节 $E_j,F_j$ 只是 $Z_j$ 的实际偶、奇块系数，不是纯产生矩阵单位。

令
$$
\mathcal J_j'=
\{b\in\mathcal C_j:I_{K_j}\otimes b\in\mathcal I\}.
$$
完整一次尾交定理准确给
$$
\mathcal J_{j+1}'
=\overline{h_j\mathcal C_{j+1}+k_j\mathcal C_{j+1}}^{\|\cdot\|}.
\tag{1.1}
$$
所有这些尾交都来自同一个原闭理想，未以某个行列式子理想替代。

定义两个真正的商距离
$$
m_j=\operatorname{dist}(G_j,\mathcal J_{j+1}'),
\qquad
\widetilde m_j=
\operatorname{dist}\left(G_j-\frac{I+t_j}{2},\mathcal J_{j+1}'\right).
\tag{1.2}
$$
当然 $\widetilde m_j\le m_j+(1+\eta_j)/2$。

## 2. 在完整下一尾理想上优化条件锚

取任意 $H\in\mathcal J_{j+1}'$，按恒等延拓到当前空间，置
$$
G_{j,H}=G_j-H,
\qquad
\Theta_{j,H}=2(N_j+G_{j,H})(I+N_j)^{-2}.
\tag{2.1}
$$
$N_j+G_j=D_j^{-1}S_j\in\mathcal J_j'$，而 $H$ 也属于该原闭理想。
所以
$$
\Theta_{j,H}\in\mathcal J_j'.
$$
真实一位压缩恒等式
$$
e^*(I+N_j)^{-2}e=0,\qquad
e^*N_j(I+N_j)^{-2}e=I/2
$$
不依赖尾系数 $G_{j,H}$，故
$$
\omega_j(\Theta_{j,H})=1,
\qquad
\|\Theta_{j,H}\|
\le\frac{8(1+\|G_j-H\|)}{(1-\eta_j)^2}.
\tag{2.2}
$$
以完整尾交的单位球定义
$$
q_j^{\rm joint}=
\sup_{b\in\mathcal J_j',\,\|b\|\le1}|\omega_j(b)|.
$$
对 $H$ 取下确界，不假设距离已达到，得到
$$
\boxed{
q_j^{\rm joint}\ge\frac{(1-\eta_j)^2}{8(1+m_j)}.
}
\tag{2.3}
$$
若 $m_j$ 沿某个无穷子列有界，可在每层选误差不超过 $1/j$ 的 $H_j$，
使对应 $\Theta_{j,H_j}$ 统一有界、位于原闭理想且 WOT 趋 $I$。
故原闭理想不存在任何非零正正常湮灭者。
如需选在未闭代数理想中的目标，每层再以范数误差 $1/j$ 逼近该目标即可，
仍保统一范数与 WOT 极限。

这不支付这些 $H_j$ 的实际有限源费用。
在精确正常湮灭问题中，闭理想归属本来保证准确零配对；
在任何带残量的构造中，必须重新支付 $H_j\approx h_jU_j+k_jV_j$
的全部源范数及各级 $D_l^{-1}$，不能仅用 (2.3) 代替。

## 3. 同一正态迫使商距离发散

假设 $0\ne\rho_0\ge0$ 是原理想的正常湮灭者。
令 $\rho_j$、$\sigma=\rho_{j+1}$ 为同一原正态的实际正部分迹，
$\tau=\operatorname{Tr}\rho_0$，
$r_j=\operatorname{Tr}(\rho_0P_{\chi_j})\to0$。
[同一正密度的交叉块稿](R236-appendix-positive-normal-cross-blocks-and-pure-finite-head-exclusion.md)已证明
$$
\left\|
\operatorname{Tr}\left(\sigma\left(G_j+\frac{I+t_j}{2}\right)\,\cdot\right)
\right\|_{(\mathcal C_{j+1})_*}
\le(1+\eta_j)\sqrt{\tau r_j}.
\tag{3.1}
$$
同一 $\sigma$ 湮灭完整 $\mathcal J_{j+1}'$。
因此对任意 $H\in\mathcal J_{j+1}'$，把 $G_j$ 换成 $G_j-H$
不改变 (3.1) 的泛函。
此外
$$
(G_j-H)^2-t_j
=h_j-2G_jH+H^2\in\mathcal J_{j+1}'.
$$
于是与前稿相同的准确恒等式给
$$
\operatorname{Tr}\left[
\sigma\left(G_j-H+\frac{I+t_j}{2}\right)
\left(G_j-H-\frac{I+t_j}{2}\right)(I-t_j)^{-2}
\right]=-\frac\tau4.
$$
结合 (3.1) 后再对 $H$ 取下确界，得到
$$
\boxed{
\widetilde m_j
\ge\frac{(1-\eta_j)^2}{4(1+\eta_j)}
\sqrt{\frac\tau{r_j}},
\qquad
m_j\ge
\frac{(1-\eta_j)^2}{4(1+\eta_j)}
\sqrt{\frac\tau{r_j}}-\frac{1+\eta_j}{2}.
}
\tag{3.2}
$$
所以真正常湮灭不仅迫使原始 $\|G_j\|\to\infty$，还迫使
$$
\boxed{\operatorname{dist}(G_j,\mathcal J_{j+1}')\to\infty.}
\tag{3.3}
$$
该商距离的发散比原始递推范数的发散更强。

## 4. 与原正慢行大范数的区别

[原正慢行的真实递推稿](R236-appendix-positive-slow-row-true-recursive-quotient-growth.md)已经证明原 $S_N$ 的原始递推商满足
$\|G_j\|\ge\exp[(55-o(1))16^j]$。
这个下界没有对任意 $H\in\mathcal J_{j+1}'$ 作比较，
故不能推断 (1.2) 的商距离大，也不能据此关闭本稿的新充分条件。

下一实际问题已具体化为：能否用全部实际 $h_jU_j+k_jV_j$ 及其范数闭包，
把 $G_j$ 修正到某个一致有界的代表元。
这是一个真实算子范数问题，不能由形式 $G_j^2=t_j$、谱半径、每层非零或原始范数增长代替。
