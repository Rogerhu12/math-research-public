# R182. 真实第一 AS 进位及原完整中央行

日期：2026-11-12。**以下公式和真实第三层消元已证明；
严格全阶预算仍未完成。**

固定惰性 $p=4r-1\ge7$，$R=r(p-1)$。
在原加法参数 $w=z^4$ 写
$$
 U=\frac{w^r}{p}\mathcal G(w^R/p^p),\qquad
 V=w\mathcal V(w^R/p^p).
$$
两级数整，$\mathcal V\equiv1\bmod p$，且与 R177 的
Cartan 输出级数准确满足
$$
 \mathcal G=\mathcal V^rG(T\mathcal V^R).
$$
由真实 sigma 余项的闭盘估计，全部正系数模 $p^2$ 只保留
同一普适 Teich 指数。令 $H=\bar G$、$\tau=H(0)$，Wilson 商
$\mathfrak w_p=((p-1)!+1)/p\bmod p$。则全部 $T$ 上
$$
 \frac{\mathcal V-1}{p}\equiv-TH^{p-1},\qquad
 \frac{\mathcal G+T\mathcal G^p-G(0)}p
                     \equiv-\mathfrak w_pTH^p\pmod p.
$$
所以 R179 的真实缺陷是
$$
 \boxed{\quad
 \bar E=(\tau-H)\left(\frac{r\tau}{H}-\mathfrak w_p\right).
 \quad}
$$
它不是任意的形式余项。

将此式代入同一个全列生成行，以整参数 $q=TG^{p-1}$ 表示，
模 $p^3$ 的完整核心是次数至多二的多项式。
因此同一实际 $t=0,1,2$ 前缀给
$$
 v_p([v^k]P(\gamma_v))
 \ge-\{\alpha+pt\}+\min(t,3),
 \quad k=r\{\alpha+(p-1)t\}+j.
$$
此项无条件收益本身不改变 R159 的严格主项门槛。

原完整中央条件必须保留 $w$，不能用孤立的 $v$ 系数替代。
对原同次数 $68$ 的两个线性截面 $F=A_2,B$，置
$t_n=(p^n-1)/(p-1)$、$e_n=1+pt_n$。存在同一个明确单位
$\epsilon_{p,n}=p^{e_n}(68c)^{p^n}/(p^n)!$，使
$$
 p^{e_n}[w^{rp^n}]F=\epsilon_{p,n}J_F(p^n).
$$
于是
$$
 J_F'(0)=0\quad\Longleftrightarrow\quad
 p^{e_n}[w^{rp^n}]F\in p^{2n+2}\mathbb Z_p
                       \quad\text{对全部 }n\ge0.
$$
它的首两层进一步给真正的原线性轴约束
$$
 c_F=L_{0,r}(F)\in p\mathbb Z_p,\qquad
 L_{0,2r}(F)\equiv17\tau\,c_F/p\pmod p.
$$
没有把此条件外推到原混合源的所有乘积。
两个低 Euler 临界例的实际核为空，未将其计为新的预算收益。

[完整证明](../notes/2026-11-12-actual-first-as-carry-and-complete-central-rows.md)。
[原 sigma／周期独立证书](../scripts/check-actual-first-as-carry.py)
核对 $p=7,t\le8$、$p=11,t\le3$ 的全部相关系数、
下一中央轴式和两个真实空核。
