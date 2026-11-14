# 中间自由带再次 Schur：持续算式检查点

2026-11-13 21:39 UTC，boundary_resume_2116。这里记录当前准确接口及尚待估计的原算子，不把它登记成新的三 Gram 估计。已完成的输出切分结论在 `results/R271-appendix-output-cut-schur-localization-and-larger-middle-band.md`，交 root 发布后不再改动该稿。

## 1. 深源最小补全确实扩大自由空间

取原 $m,q,d=2^m$，沿 source-jets 稿写完整 primitive 坐标空间为
$\mathscr P=\mathscr F\oplus\mathscr T$，其中 $\mathscr F=\ker\mathcal B$。
将强制坐标按深度切为 $\mathscr T_{\rm sh}\oplus\mathscr T_{\rm dp}$，深部为 $k\ge h$，$h>\theta_*d$，$\theta_*=(128/770)^{1/3}$；明确版本可取 $h=5d/8$。

原 source Schur 度量中的最小深补全 $y_0=-S_{11}^{-1}S_{10}x$，等价于：先固定浅强制坐标 $x$，再对
$$
\mathscr F_{\rm new}=\mathscr F\oplus\mathscr T_{\rm dp}
$$
全部最小化 $\|\mathcal E p\|^2$。因此补全后的坐标 $\widehat p$ 满足
$$
P_{\mathscr F_{\rm new}}(I+\mathcal C_L^*\mathcal C_L)\widehat p=0.
\tag{1.1}
$$
特别，$\mathscr F_{\rm new}$ 包含**所有头方向**上的 primitive 孔层 $n\le q-h$。这是因为该孔层的深度 $k=q-n\ge h$，其旧自由头 $j\le k$ 与新增深强制头 $j\ge k+1$ 正好补全整个头空间。

深 source 稿已付这个操作的实际源修正：$\widehat r=\mathcal B\widehat p$，若 $v=E_q^\dagger r$、$\widehat v=E_q^\dagger\widehat r$，则
$$
\|v-\widehat v\|\le\varepsilon_d\lambda_{\rm flat}(r),
\qquad\varepsilon_d=e^{-d^4/20}
\tag{1.2}
$$
（$h=5d/8,m\ge8$）。以下始终用这个固定的 $\widehat r,\widehat v$，不继续换源。为简洁省去帽号，写 $v=p+\nu$，$\nu=\mathcal C_Lp$。

## 2. 四个 primitive 带和两个物理输出带

取整数 $1\le r_*<h\le d-2$，按所有头坐标分为
$$
\begin{aligned}
U&:n\le q-d+1,\\
J&:q-d+2\le n\le q-h,\\
K&:q-h+1\le n\le q-r_*,\\
T&:q-r_*+1\le n\le q.
\end{aligned}
\qquad p=u+j+k+t.
\tag{2.1}
$$
$U,J$ 都是实际新增自由空间内的正交子空间。$K,T$ 内仍保留所有自由头分量，不能把它们直接改成强制 jets。

在非 primitive 输出空间，令 $Q_-$ 保留孔数 $\le q-r_*+1$，$Q_+=I-Q_-$。记
$$
A=Q_-\mathcal C_L|_U,\quad B=Q_-\mathcal C_L|_J,
\quad H=Q_-\mathcal C_L|_K,
$$
$$
E=Q_+\mathcal C_L|_U,\quad F=Q_+\mathcal C_L|_J,
\qquad \nu_\pm=Q_\pm\nu.
\tag{2.2}
$$
本节 $A$ 是所显示的输出列，**不是有限头 $A_m$**。顶输入 $T$ 的低输出准确为零。

真实自由正规方程与低输出式为
$$
u+A^*\nu_-+E^*\nu_+=0,
\tag{2.3}
$$
$$
j+B^*\nu_-+F^*\nu_+=0,
\tag{2.4}
$$
$$
\nu_-=Au+Bj+Hk.
\tag{2.5}
$$
这些式子对同一个完整最小补全同时成立；不要求 $\nu_+$ 为零。

## 3. 新自由中间带的完整消元

置
$$
R=(I+BB^*)^{-1}.
$$
由 (2.4)–(2.5)，准确有
$$
\nu_-=R(Au+Hk-BF^*\nu_+).
\tag{3.1}
$$
代入 (2.3)，得到
$$
\boxed{
G_{\rm eff}u=-A^*RHk-E_{\rm eff}^*\nu_+,
}
\tag{3.2}
$$
其中
$$
\boxed{
G_{\rm eff}=I+A^*RA\succeq I,
\qquad E_{\rm eff}=E-FB^*RA.
}
\tag{3.3}
$$
所以令 $T_{\rm eff}=-G_{\rm eff}^{-1}A^*RH$，就有
$$
\|G_{\rm eff}^{1/2}(u-T_{\rm eff}k)\|
\le\|E_{\rm eff}G_{\rm eff}^{-1/2}\|\,\|\nu_+\|.
\tag{3.4}
$$
$G_{\rm eff}$ 正是完整低输出 Gram $I+(A,B)^*(A,B)$ 对 $J$ 的 Schur 补；(3.3) 保留了低输出造成的全部实际反馈。

### 当前必须估计的实际算子

原输出切分稿已经控制直接项 $E$。再消 $J$ 后新增的真正困难是
$$
\boxed{
\Xi_{m,q,h,r_*}
=FB^*(I+BB^*)^{-1}A
\bigl[I+A^*(I+BB^*)^{-1}A\bigr]^{-1/2}.
}
\tag{3.5}
$$
这是按上述原物理带与原 $\mathcal C_L$ 定义的具体算子，未换成任意环境矩阵。

正性本身给
$$
\|B^*RA G_{\rm eff}^{-1/2}\|\le1.
\tag{3.6}
$$
一种证明是将 $R^{1/2}A$ 写为 $Z$：
$\|Z(I+Z^*Z)^{-1/2}\|\le1$，且
$\|B^*(I+BB^*)^{-1/2}\|\le1$。但 (3.6) 不能删除左端的 $F$；它没有证明 $\Xi$ 小。

## 4. 原头幂能够支付到什么位置

对输入 $J$ 中 $n=q-k_0$ 的 primitive 层，$h\le k_0\le d-2$。要到高输出，提升阶必须满足
$$
t\ge k_0-r_*+2\ge h-r_*+2.
\tag{4.1}
$$
因此完整原列有
$$
\|F\|\le\sum_{t\ge h-r_*+2}
\exp[t\Theta-\gamma(t-m)_+^4],
\quad\gamma=770/256,\quad\Theta<d^3/2+11.
\tag{4.2}
$$
只有当 $(h-r_*)/d>\theta_*$ 并保严格余量时，这个直接预算才使 $F$ 指数小。对自然选择 $h=5d/8,r_*=3d/8$，差仅为 $d/4$，不能套深列小量。

同时有准确的原头核：在同一层 $n=q-k_0$，$F$ 杀掉全部
$$
\operatorname{span}\{e_0,\ldots,e_{k_0-r_*+1}\}\otimes K_{q-k_0},
\tag{4.3}
$$
因为原头 $A_m^t$ 杀掉 $e_j$ 当 $j<t$。这可以作为继续将 $J$ 分成 $\ker F$ 及其余头旗的入口。进一步消去 $\ker F$ 时必须同时改变 $B$ 的低输出 Gram；不能只给 $F$ 右乘一个物理投影。

## 5. 后续具体问题

当前路线只剩对 (3.5) 的实际控制，或在同一个 $\nu_+$ 上控制 $\Xi^*\nu_+$；无需再重证直接列 $E$ 小。

可继续使用 (4.3) 的原头核先消去低头自由坐标，保留所产生的正 Schur 补，再检查剩余 $F$ 与 $B$ 的相对能量。任何相邻 inverse Gram 或增长头测试都必须作用于 (3.5) 的真实中间向量，不能用两条独立算子范数界替换。

原 primitive 右逆构造中的 $\sqrt q$ 来自完整创建层的 Cauchy 界；目前没有去掉它的证明。整个孔层 MP 的 $q^{3/2}$ 界已被既有原尾奇异向量排除，不作为下一步假设。
