# R116. 相对密度一的完整 Heegner 迹非零及不可 p 除

日期：2026-11-12。**状态：已证明；主目标仍未完成。**

固定
\[
 E:y^2=x^3-17x,\qquad F=\mathbb Q(\sqrt{-15}),\qquad
 \mathcal P_F=\{p\ne17:p\equiv1,17,49,53\pmod{60}\}.
\]
任取 \(32/17<L<2\)。存在一个固定整数 \(C\ge1\)，使对
\(\mathcal P_F\) 中相对密度一的输入素数 \(p\)，存在合法辅助素数
\[
 \ell\equiv-1\pmod{1020Cp},\qquad \ell\ll p^L,
 \qquad v_p(\ell+1)=1,
\]
令 \(u=(\ell+1)/p\)、\(U\subset G_\ell\) 为阶 \(u\) 的子群，
则**实际全部 prime-to-\(p\) 迹**满足
\[
 \boxed{\quad
 Q_{p,\ell}=\operatorname{Tr}_U(1+\tau_3)P[\ell]\ne O,
 \qquad Q_{p,\ell}\notin pE(F[\ell]).\quad}
\]
这一结论已支付 R110 中的非零前提，处理了随 \(p,\ell\) 增长的
完整 \(U\) 迹，不仅是原始点或固定次数子迹。
还可使实际固定首系数 \(b_{c,u}\) 为 \(\ell\)-进单位，因而
\(v_\ell(\log_E([2]Q_{p,\ell}))=1/p\)。

## 证明的三个精确输入

1. 固定 \(q=61\) 的普通 Serre–Tate 盘中，R114 的固定 period
   变量为 \(v=\kappa\log(1+T)\)。实际整微分给有界测度
   \(\mu\)，其矩为 \(\kappa^m h_{c,m}\)，
   \(h_{c,m}=m!b_{c,m}\)。指定分支
   \(M(W)=\int_{\mathbb Z_q^\times}x^{-1}(1+W)^{\log\langle x\rangle/\log(1+q)}d\mu\)
   不恒为零：若为零，原始 Gauss 和杀掉所有新层 wild 对数；
   整数投影 \(q-N\) 和准确原始 Heegner 递推迫所有有限部分全迹
   为扭点，违反 Cornut（2002）的已发表定理。
   首个非零系数给 \(v_q M((1+q)^m-1)=O(\log m)\)，
   而非单位部分的矩赋值至少 \(m-1\)。故可统一取
   \(C=60\cdot61^k\)，使所有充分大 \(C\mid m\) 的
   \(h_{c,m}\ne0\)，对全部固定有限中心成立。
2. 固定代数 Gauss–Manin 系统、period 逆变换及椭圆对数的代数
   微分嵌入一个有限多项式微分系统。直接分母和复增长估计给
   \(A^{dm+1}h_{c,m}\in\mathcal O_K\)，范数的对数为
   \(O(m\log(m+2))\)。这没有把 period 变量中的函数误称为代数。
   对上述非零进程，取全部中心的范数乘积为非零整数 \(J_m\)。
   R114 的真实迹公式给
   \(Q_{p,\ell}=O\Rightarrow\ell\mid J_u\)。
3. Fouvry 的 Lemma 7 给典型 \(p\in(X,2X]\) 各有
   \(\gg X^{L-1}/\log X\) 个候选 \(\ell\in(X^L,2X^L]\)。
   因 \(L<2\)，一个 \(\ell\) 至多属于一个这样的 \(p\)。
   而 \(u\le2X^{L-1}+1\)，所有 \(J_u\) 的对数乘积只有
   \(O(X^{2L-2}\log X)\)，故 \(\ell\mid J_u\) 的坏候选至多
   \(O(X^{2L-2})\) 个。全部候选都坏的输入遂至多
   \(O(X^{L-1}\log X)=o(X/\log X)\) 个。

最后，\(N_pQ=O\) 与 \(E(F^{\rm ab})_{\rm tors}=E[2]\) 使
非零 \(Q\) 为非扭。R110 的真实高度
\(\widehat h(Q)\ll p^{2L-2}\log p=o(p^2)\)，结合 Baker 的
固定正高度下界，推出不可 \(p\) 除。
R110 的 \((2-L)\log_2p-\frac12\log_2\log p+O(1)\)
增广长度下界也因此对所选点无条件成立。

**尚须证明的准确条件**仍是
\[
       Q_{p,\ell}\notin(\tau-1)\ker N_p.
\]
不可 \(p\) 除不等于这个更强的指定增广底层非零，因而本结果
没有证明 \(\Sha(E/\mathbb Q)[p^\infty]\) 有限。

完整证明分为三份，均已交叉独审：
[实际普通盘与整测度](../notes/2026-11-12-fixed-ordinary-st-mellin-branch.md)、
[Cornut 全迹与固定非零进程](../notes/2026-11-12-cornut-fixed-branch-and-nonzero-progression.md)、
[高度及跨素数乘积](../notes/2026-11-12-fixed-cm-jet-heights-and-prime-product.md)。
