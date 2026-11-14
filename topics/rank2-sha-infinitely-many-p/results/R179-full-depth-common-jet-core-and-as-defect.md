# R179：全深度共同 jet 核与两层 AS 前缀消元

**状态：已证明。**

固定实际 theta 平面、惰性 $p=4r-1\ge7$，保留原有限次数源
$E_D=\mathbb Z_p[a-1,b]_{\le D}$ 及全部准确前缀。
R177 的整级数 $G$ 给 $U=v^rG(v^{r(p-1)}/p^p)/p$。

若 $k=r\{\alpha+(p-1)t\}+j$，$1\le\alpha\le p-1$、
$0\le j<r$、$e=\alpha+pt$，则同一真实整泛函满足

$$
p^e r_k
=\sum_{b=0}^t\sum_{s=0}^{\alpha+(p-1)b}
p^{b+s}[T^{t-b}]G^{\alpha+(p-1)b-s}
L_{\alpha+(p-1)b-s,j+rs}.
$$

模 $p^N$ 只需 $b+s<N$，故各深度只用至多 $N(N+1)/2$ 个
同源泛函，总 Taylor 阶数为 $O(pN)$。其系数仍含实际 $G$ 的
高阶项；此有限性不删除深层算术输入。

利用两个更早的准确行与 $\bar G+T\bar G^p=\tau$，对原饱和
前缀中的 $P$ 有

$$
v_p(r_k(P))\ge-e+\min(t,2).
$$

除以 $p,p^2$ 前均已证明整条行的整除性。再下一层准确是

$$
\mathscr E=(G+TG^p-G(0))/p\in T\mathbb Z_p[[T]],\qquad
(U^p+pU-G(0)V^r)|_\gamma=pv^r\mathscr E(v^{r(p-1)}/p^p).
$$

该 Cartan 多项式写回原环境一般是形式级数，不能免费当成
原 $E_p$ 的列。对原齐次 theta 源，整径向坐标准确给
$\widetilde H=\Gamma^d g_H(\zeta)$，其中
$\Gamma=\Gamma_*(U,V^r)$、$\zeta=VZ_*(U,V^r)$。
故精度 $p^N$ 的同源输入闭合到 $N$ 套
$g_j,g_{j+r},\ldots,g_{j+r(N-1)}$ 和同一整核；前两带已明确展开，
$j=0$ 恰为 R175 的中央矩。高阶 $G$ 系数仍须另付。
两层收益尚未达到严格全阶预算，也未把原两中央条件扩为乘积
的零性。

完整证明：
[全深度共同 jet 核、两层真实消元与准确 AS 缺陷](../notes/2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
