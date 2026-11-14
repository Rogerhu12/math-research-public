# R141. 固定负七 CM 源点上的实际互反函数简单零点

日期：2026-11-12。**已证明。**

完整证明见
[固定 CM 源点的简单零点与退化素数上界](../notes/2026-11-12-noncm-fixed-cm-source-simple-zero.md)。

固定 R136 的非 CM 曲线 $E389$、$F=\mathbb Q(\sqrt{-7})$
以及两个最大阶 Heegner 源点 $c_\pm$。
R136 已证明 $\pi(c_\pm)=O$ 且 $d\pi(c_\pm)\ne0$。
对 $p$ 在 $F$ 分裂的好素数，原去 $p$ 互反函数是
$$
 g_p=\frac{\Theta^{p-2}\bar f}{H^p},\qquad
 (g_p)_\infty=\sum_{p\nmid n}\frac{\bar a_n}{n}q^n,
 \qquad g_p(\bar c_\pm)=0.
$$
这里 $H$ 是 Hasse invariant，$\Theta$ 是 Katz theta。

固定代数微分 $\omega_0$，在 Igusa 框架中写
$\omega_{\rm ST}=\Omega\omega_0$，则
$\Omega^{p-1}=A_{c,p}:=H(C_c,\omega_0)$。
令 $h=\bar f(c,\omega_{\rm ST})$；固定有限例外集之外 $h\ne0$，且
$$
 h^p=A_{c,p}^{-2}h,\qquad
 \boxed{\quad
 (\mathcal Dg_p)(\bar c)
       =h\bigl(1-a_p(E)/A_{c,p}^2\bigr).
 \quad}
$$
故非简单零的准确条件为 $a_p(E)\equiv A_{c,p}^2\pmod p$。

源的 CM Frobenius 给整数 $u,v$ 满足
$u^2+7v^2=4p$、$A_{c,p}\equiv u\pmod p$。
若上述退化发生，则 $u^2-a_p(E)=kp$，$k=0,1,2,3,4$。
Hasse 界和直接整数格计数给
$$
 \boxed{\quad
 \#\{p\le X:p\text{ 在 }F\text{ 分裂，源零点非简单}\}
                     =O(X^{3/4}).
 \quad}
$$
这是无条件跨素数结论，没有对一般非 CM 固定迹使用幂次界。

对原全部 $\ell+1$ 同源方向，实际权零几何 Hecke 迹满足
$$
              \operatorname{Tr}_{\ell+1}(g_p)
                      =a_\ell(E)g_p.
$$
因此 $a_\ell(E)$ 为 $p$-单位时，这个总迹在上述密度一 split 源点
也有简单零点。**这仍不推出指定 $U$ 迹/$C_p$ 纤维的二阶矩非零**；
证明末节给出连通 étale 覆盖上总迹简单零而整个纤维值为零的
准确对照。主问题尚需原模形式轨道的额外全局关系。
