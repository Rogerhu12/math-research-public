# 指定实际运输递推的近最优 Deddens 成本

作者：OpenAI ChatGPT，`/root/literature_deddens`；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的中间结论。** 对前稿已经实际实现的同一源、同一目标，本稿给所有 Deddens 实现均满足的费用下界；与运输上界相差至多 $2\sqrt{N_n}$，累计对数费用的五次主阶因此准确。没有将结论扩大到其他目标或普通不变子空间。

## 1. 已实际实现的递推

固定原 Haar 算子 $Af(y)=w(y)f(y-1)$，$w(y)=\alpha_{v_2(y)}$、$\alpha_j=e^{-L_j}$，其中
$$
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$
沿用 [同源运输及可持续递推 §6](R12-appendix-same-source-transport-interpolation-and-sustainable-actual-recursion.md)：
$$
f_0=\mathbf1,\qquad
N_n=2^{m_n}=\min\{2^m:2^m\ge4n\},\qquad a_n=2n-1,
$$
$$
f_n(y)=\mathbf1_{\{y\bmod N_n\ge a_n\}}.
\tag{1.1}
$$
前稿已构造真正的有限头下三角 $R_n$，满足
$$
R_nAf_{n-1}=f_n,\qquad
\|R_n\|\le2/\alpha_0,\qquad
c_A(R_n)\le2/\alpha_{m_n-1}.
\tag{1.2}
$$
而 $\|f_n-\mathbf1\|^2=(2n-1)/N_n<1/2$。此处不重新选择 $f_n$，也不改变前稿的实际源。

## 2. 任意实现都必须支付实际逆像

由 [负幂域与等距共轭](R12-appendix-deddens-negative-domains-and-isometric-conjugation.md)，对每个 $R\in\mathcal D_A$，
$$
\|A^{-1}RAu\|\le c_A(R)\|u\|\qquad(u\in H).
\tag{2.1}
$$
因此只要 $RAf_{n-1}=f_n$，便有
$$
\boxed{c_A(R)\ge
\frac{\|A^{-1}f_n\|}{\|f_{n-1}\|}.}
\tag{2.2}
$$
这里没有要求 $R$ 是正算子、有限头、加权复合算子或运输矩阵，也没有要求普通算子范数先有上界。

这个逆像确实有定义。$f_n$ 在模 $N_n$ 的第 $0$ 格为零；在其余每个柱格上，$w$ 恒等于某个 $\alpha_j$、$j<m_n$。因 $A^{-1}=U^{-1}M_{1/w}$ 在原值域上成立，直接积分给
$$
\boxed{\|A^{-1}f_n\|^2
=\frac1{N_n}\sum_{r=a_n}^{N_n-1}\alpha_{v_2(r)}^{-2}.}
\tag{2.3}
$$
这是原 $L^2$ 内积下的准确范数，不是只取某个有利坐标的替代源。

特别地，$a_n=2n-1<N_n/2$，所以该和包含整柱 $r=N_n/2$；其测度是 $1/N_n$，权为 $\alpha_{m_n-1}$。又 $\|f_{n-1}\|\le1$，故
$$
\boxed{c_A(R)\ge\frac1{\sqrt{N_n}\,\alpha_{m_n-1}}.}
\tag{2.4}
$$
更准确的下界当然是 (2.3) 的平方根除以
$\|f_{n-1}\|$；当 $n\ge2$，后者恰为
$\sqrt{1-(2n-3)/N_{n-1}}$，$n=1$ 时为 $1$。

## 3. 真实最优成本的上下夹逼

定义
$$
C_n^{\rm opt}=\inf\{c_A(R):R\in\mathcal D_A,
\ \|R\|\le2/\alpha_0,\ RAf_{n-1}=f_n\}.
$$
前稿保证可行，(1.2) 与 (2.4) 给
$$
\boxed{\frac1{\sqrt{N_n}\,\alpha_{m_n-1}}
\le C_n^{\rm opt}\le\frac2{\alpha_{m_n-1}}.}
\tag{3.1}
$$
因此前稿的显式运输实现比真正最优值最多大 $2\sqrt{N_n}$ 倍。这里没有宣称运输矩阵就是准确极小元。

对任何实际实现这组目标的序列 $(R_i)$，(2.4) 逐步给
$$
\sum_{i=1}^n\log c_A(R_i)
\ge\sum_{i=1}^nL_{m_i-1}-\frac12\sum_{i=1}^n\log N_i.
\tag{3.2}
$$
前稿的选择同时给
$$
\sum_{i=1}^n\log c_A(R_i)
\le\sum_{i=1}^nL_{m_i-1}+n\log2.
\tag{3.3}
$$
两端相差至多 $O(n\log(n+1))$，而中间共同主项为五次阶。

## 4. 五次阶的显式界与适用边界

由 $2^{m_i-1}\ge2i$ 和 $L_j\ge20\,16^j$，(3.2) 给
$$
\sum_{i=1}^n\log c_A(R_i)
\ge320\sum_{i=1}^ni^4-\frac12\sum_{i=1}^n\log N_i
=\Omega(n^5).
\tag{4.1}
$$
所用 $L_j$ 下界可直接检查：$j=0$ 为等号；对 $j\ge1$，
$$
(220/3)16^j-90\,8^j\ge(85/3)16^j>0,\qquad
300\,2^j-850/3>0.
$$
上界由 $2^{m_i-1}<4i$ 给
$$
\sum_{i=1}^n\log c_A(R_i)
\le n\log2+\frac{71680}{3}\sum_{i=1}^ni^4+600n(n+1)
=O(n^5).
\tag{4.2}
$$
因而这组指定实际目标的最优累计对数成本为 $\Theta(n^5)$。即使舍弃运输构造而允许任意 Deddens 算子，也不能保持这组目标并将主阶降为四次。

这一结论的范围是固定的 (1.1)。新的软目标 $g_n$ 可以改变准确逆像范数；本稿没有证明全部留在同一非零球内的递推都有五次下界。不过，任何合法一步 $RAf=g$ 必须保留
$\|A^{-1}g\|/\|f\|$ 这项真实费用。仅让目标在普通 $L^2$ 中接近 $\mathbf1$，不会自动控制这一逆像。

原幂衰减仍有 $-\log\|A^n\|=O(n^4)$，而任意持续非零实际递推本来就满足
$\|A^n\|\prod_i c_A(R_i)\gtrsim1$。本稿与这条必要条件一致，没有用五次构造声称完成普通不变子空间问题。
