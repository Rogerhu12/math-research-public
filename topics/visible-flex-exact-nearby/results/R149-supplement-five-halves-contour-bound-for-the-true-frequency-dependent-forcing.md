# 全高频 genuine 矩阵及有向强迫的复参数接收

令 $j$ 为原带符号物理标签，$|j|\ge97$，$n=4|j|$，$\epsilon=\operatorname{sgn}j$，$\zeta_j=97/|j|$。在真势和其振幅公式中用复参数 $z=\zeta^2/9409$，$n^{-1}=\zeta/388$。原两列 $\Psi_n(T)$、两条 $e^{4ijP_\sigma}$、真实角、所有输入 Fourier 乘子及反射符号仍按各自的原 $j$ 作用。以下的复参数只用于振幅和指定的有限算子乘积。

在完整原实径向域、物理圆及所选实参数族上，对 $|\zeta|\le1$，原 $V(z,T)$ 在其使用域内关于 $\zeta$ 全纯。确实 $|\Re z|,|\Im z|\le1/9409$，而原 A.1–8 给 $|V|<276$、$|T|\le1/2000$ 在真实复像中。$V_{\rm ext}=\chi_V(T)V(z,T)$ 在外域延拓为零，且 $\chi_V$ 与 $\zeta$ 独立。$\mathcal B_{\rm ext}$ 的真积分同样全纯，包括支持外的 $\lambda_j/s$ 长尾。物理角的有限导数只作用于实际 $C^{64}$ 系数的已用阶数。[原完整势预算](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md)

置 $v=\zeta/388$, $H^V(\zeta)=i\epsilon x\,1+y\mathcal K-yV_{\rm ext}(\zeta)v^2 E_{12}$，$B(\zeta)=(H^V(\zeta))^{-1}$。真圆上 $D=x^2+Ty^2=p_+p_-$。支持内 $p_\pm>79/80$、$|y|<7/1000$，故
\[
 |D-v^2 V_{\rm ext}(\zeta)y^2|>
 (79/80)^2-276(7/1000)^2/388^2>97/100.
 \tag{GCD.1}
\]
支持外 $V_{\rm ext}=0$，真域 $D>(1/27)^2$。这给 $B(\zeta)$ 及其每个所需物理角导在整个复圆盘的共同非奇性；不知道原 $T$ 复角延拓也可在每个真实物理角处使用。[GAF](R149-supplement-all-frequency-two-ray-physical-bound-for-both-genuine-Airy-rows.md)；[BPF](R149-supplement-whole-genuine-inverse-deformation-on-the-physical-Fourier-space.md)

令 $U_j(a)=e^{4ijX}a^t\operatorname{diag}(1,n^{-1})\Psi_n(T)$。在真实参数 $\zeta=\zeta_j$，原微分方程给 $\partial_\phi U_j(a)=U_j(a')+nU_j(H^V(\zeta_j)a)$。现在每个 $j$ 单独应用两次，得到
\[
 U_j(w_j)n^2=\partial_\phi^2 U_j(B_j^2w_j)
 -\partial_\phi U_j((B_j^2w_j)'+B_j(B_jw_j)')
 +U_j((B_j(B_jw_j)')'),                                  \tag{GCD.2}
\]
其中 $w_j=w(\zeta_j),B_j=B(\zeta_j)$。这三个幅均包含原真势及正确乘法顺序。适用的具体 $w$ 是 $L_1(\zeta)+vL_2(\zeta)+v^2L_3(\zeta)$，其所有 $\mathfrak C,\mathfrak R$、共同分母、原自由输运及首修正见 [G.4–9](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md)。由 GCD.1 及此前全纯性，三个完整幅和原零阶幅都是 $\zeta$ 的全纯函数。对每个复 $\zeta$ 自行组装这些幅之后，可用真正固定的 $\Psi_n(T)$ 接收。只有在原 $\zeta_j$ 上才使用上述微分恒等式。

## 任意 Hilbert 输出和四个互不相交输入段

设 $K(\zeta)$ 是从完整物理 Fourier 输入 Hilbert 空间到同一 Hilbert 输出的有界全纯算子族。对一组原标签 $S$，若其 $\zeta_j$ 在 $[l,h]$ 中，取 $m=(l+h)/2,R=1-m,b=(h-l)/(2R)<1$。对任一有限输入 $a$，Cauchy 公式把 $\sum_{j\in S}K(\zeta_j)P_j a$ 写为
\[
 \int_0^{2\pi}K(m+Re^{it})D_S(t)a\,dt/(2\pi),\quad
 D_S(t)=\sum_{j\in S}
 \frac{P_j}{1-(\zeta_j-m)e^{-it}/R}.
\]
有向部分均保留在各自的 $K$。可用半径递增到 $R$ 的极限。输入标签彼此正交，Parseval 给出
\[
 \int\|D_S(t)a\|^2\,dt/(2\pi)
 =\sum_{j\in S}\frac{\|P_j a\|^2}{1-(\zeta_j-m)^2/R^2}
 \le\frac{\|P_Sa\|^2}{1-b^2}.
\]
所以本段费用至多 $C_S/\sqrt{1-b^2}$，其中 $C_S$ 可取原 $K$ 在该圆周上的算子范数平方均方根，也可取其上确界。此估计适用于 Bessel 加权输入、两独立参考列、反射或有限头约束所用的配对输入。输出不要求不同频段正交。对原幅的角导和 $P\Lambda^{-2}\partial^k$ 等共同物理算子可直接保在 $K$ 内。

分别取 $|j|=97,98\ldots101,102\ldots122,123\ldots\infty$。第一段只需真实 $K(1)$。后三段令 $h=97/j_{\min},l=97/j_{\max}$，无穷端取 $l=0$。直接用 $b=((1-l)-(1-h))/((1-l)+(1-h))$ 分别得 $b<3/5,5/8,2/3$。对四个输入范数再用 Cauchy–Schwarz，可保各段的实际 $C_i$，全原算子界为
\[
 \left(C_0^2+\frac{25}{16}C_1^2+
                \frac{64}{39}C_2^2+\frac95 C_3^2\right)^{1/2}
 <\tfrac52\max_i C_i \qquad (\max_i C_i>0).
 \tag{GCD.3}
\]
原 $H^{-4/3}$ 输入的 $\mathsf N$ 次幂及 $\operatorname{sgn}j$ 都可在各真对角内保留；在未作投影的真实 $J,I$、物理均值、任意固定有序传播前也适用。GCD.3 的 $5/2$ 对完整算子族只付一次。若只知道有向参数区间内的标量绝对值，而没有上述全纯族或相应实值单标签界，不能把各列区间当作共同角乘子。该判据可在一侧体源中直接用 GCD.2，也可在已分离出真实两输入的非局部有序链上使用。它不移除任何原源或物理端口。
