# 共同 A24 的完整水平乘法、相对 theta 拼接与四个原除 p 行

日期：2026-11-16。**本注证明原共同因子在完整二变量水平格中的绝对乘法恒等式，给出四个原水平来源的固定 CM 收缩、四个真实有限拼接指数、同一三阶切锥及全部混合除 p 端点。四条原除 p 值不能同时为零尚未证明。**

输入只用 [R855 §§9–11](../results/R855-original-full-heat-connection-and-canonical-divided-jet.md)、[R856](../results/R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md) 和[已付的代数水平格](2026-11-16-algebraic-horizontal-theta-frame-and-original-divided-rows.md)。所有冻结都在原 CM 纤维进行；没有把参数曲线上的乘法误当成热连接的水平乘法。

## 1. 原四乘积与绝对水平正规

固定原 $b$、$P=(g_2,g_3)=(0,-4b)$、$\Delta_0=-432b^2$ 及已选的代数水平覆盖点 $\widetilde P$。以下 $L=L_2$ 是同一个参数导子。原共同分解准确为
$$
A_\nu=A\,H_\nu,\qquad A=A_{24},\qquad
(m_\nu,n_\nu)=(34,10),(72,48),(136,112),(66,42),
\tag{1}
$$
其中 $m_\nu=24+n_\nu$，按 $S,T,U,V$ 的顺序排列。所有因式都是原物理 $z$ 的截面，且
$$
A(z)=z^6+O(z^{12}),\qquad H_\nu(z)=1+O(z^6).
\tag{2}
$$
(1)的全部 $b$ 齐次因子及原有限角色仍取 R855 的版本。特别本注没有把 $H_\nu$ 的质量 $1$ 当成其中央值或中央导数。

对任意正偶数 $d$，沿用
$$
F_{d,a}(\tau,z)=c_\lambda
e^{dqz^2/2}\vartheta_{d,a}(\tau,z/\lambda),\qquad
c_\lambda=\sqrt{2\pi}\lambda^{-1/2},\qquad a\pmod d,
\tag{3}
$$
$$
\vartheta_{d,a}(\tau,u)=
\sum_{\ell\in\mathbf Z+a/d}
e^{\pi id\ell^2\tau+2\pi id\ell u},\qquad
f_{d,a}=F_{d,a}(\tau,0)
=\Delta_0^{1/24}\frac{\vartheta_{d,a}(\tau,0)}{\eta(\tau)}.
\tag{4}
$$
这里 $F_{d,a}=\sigma^d h_{d,a}$，$\mathcal H_dh_{d,a}=0$。
(3)中的同一个 $c_\lambda$、同一个平方根及同一个准周期 $q$ 不可各自重新定标。完整 $d$ 个标签均保留；质量函数之间有关系不等于删除 whole 截面中的奇向量。

令 $A^\flat,H_\nu^\flat$ 为原因式在 $\widetilde P$ 的唯一水平延拓。它们有固定代数坐标
$$
A^\flat(z)=\sum_{a\bmod24}a_aF_{24,a}(z),\qquad
H_\nu^\flat(z)=\sum_{b\bmod n_\nu}h_{\nu,b}F_{n_\nu,b}(z).
\tag{5}
$$
$a_a,h_{\nu,b}\in\overline{\mathbf Q}$ 都先于 $p$ 固定。它们保留各原因式的整个 CM 纤维，不仅保留(2)。

## 2. 一般偶 degree 的完整二变量恒等式

暂取任意正偶数 $m,n$，置
$$
M=m+n,\qquad g=\gcd(m,n),\qquad
q_0=M/g,\qquad K=\frac{mnM}{g^2}.
\tag{6}
$$
使用真正的整数同源
$$
z_1=Z+\frac ng\,W,\qquad z_2=Z-\frac mg\,W.
\tag{7}
$$
其行列式为 $-M/g$。相反变换为
$$
Z=\frac{mz_1+nz_2}{M},\qquad W=\frac{g(z_1-z_2)}M.
$$
完整 Hermitian 二次式满足
$$
mz_1^2+nz_2^2=MZ^2+KW^2.
\tag{8}
$$
所以(7)的拉回是 $L_M\boxtimes L_K$，没有交叉 Poincaré 项被省略。

对 $a\bmod m,b\bmod n$ 和 $0\le r<q_0$，定义
$$
c_r=a+b+mr\pmod M,\qquad
e_r=\frac{na-mb+mnr}{g}\pmod K.
\tag{9}
$$
则绝对恒等式为
$$
\boxed{
F_{m,a}(z_1)F_{n,b}(z_2)=
\sum_{r=0}^{M/g-1}F_{M,c_r}(Z)F_{K,e_r}(W).
}
\tag{10}
$$

**证明。** 先在两个原 Fourier 级数中写
$r_1=a+mk,\ r_2=b+n\ell$，并置
$c=r_1+r_2,\ d=nr_1-mr_2$。逐项有
$$
\frac{r_1^2}{m}+\frac{r_2^2}{n}
=\frac{c^2}{M}+\frac{d^2}{mnM},\qquad
r_1z_1+r_2z_2=cZ+\frac dgW.
\tag{11}
$$
先按 $k-\ell\bmod M$ 分组，得到 $M$ 个 degree $mnM$ 的相对 theta。将相差 $M/g$ 的 $g$ 组相加时，总标签 $c$ 相同；相对标签依次相差 $mnM/g$。准确的重索引是
$$
\sum_{j=0}^{g-1}
\vartheta_{mnM,d+mnM j/g}(\tau,W/g)
=\vartheta_{mnM/g^2,d/g}(\tau,W).
\tag{12}
$$
$d/g$ 是整数，故没有未说明的半标签。式(11)–(12)给出(10)的 Fourier 部分。式(8)给出完整 Gaussian 部分；左、右每项都含同一个 $c_\lambda^2$。因此不产生额外 $g$、$M$、周期或根单位倍率。$\square$

(10)是 complete theta-group 恒等式，不是只在 $W=0$ 的四个标量上验证。它在有限代数水平覆盖上成立，因而可在固定坏集以外整下降。该覆盖可以一次性加入本注出现的 $2K$-torsion 及水平基；它固定先于 $p$。这些辅助基不是新的原中央来源，也没有给原系数格增加免费列。

## 3. 四个原相对 degree 和真实拼接指数

把 $m=24$ 代入(6)，得到：

| 原来源 | 伙伴 $n$ | 总 degree $M$ | $g$ | 拼接标签数 $M/g$ | 相对 degree $K$ |
|---|---:|---:|---:|---:|---:|
| $S$ | $10$ | $34$ | $2$ | $17$ | $2040$ |
| $T$ | $48$ | $72$ | $24$ | $3$ | $144$ |
| $U$ | $112$ | $136$ | $8$ | $17$ | $5712$ |
| $V$ | $42$ | $66$ | $6$ | $11$ | $1848$ |

同源(7)的次数分别是 $17^2,3^2,17^2,11^2$。表中的 $17,3,17,11$ 来自实际整数格的行列式，不是从目标曲线的导子反推的标签。它们本身也没有识别任何新的 Hecke 角色。

在原惰性素数处令 $\epsilon_d=(2d/p)$。整平方恒等式给
$$
\boxed{\epsilon_M\epsilon_K=\epsilon_m\epsilon_n},
\qquad
\frac{(2M)(2K)}{(2m)(2n)}=\frac{M^2}{g^2}.
\tag{13}
$$
四个 $\epsilon_K$ 依次是
$$
\chi_{255},\qquad\chi_2,\qquad\chi_{714},\qquad\chi_{231},
\tag{14}
$$
而 $\epsilon_M$ 仍为 $\chi_{17},1,\chi_{17},\chi_{33}$。
这只运输真实二次字符，不增加同余条件。

## 4. 原四水平来源是相对质量在 CM 点的固定收缩

代入(5)、(9)，记
$$
\Gamma_{\nu;a,b,r}=a_a h_{\nu,b}.
$$
同一个完整两参数代数核定义为
$$
\boxed{
\mathcal K_\nu(P_1,P_2)=
\sum_{a,b,r}\Gamma_{\nu;a,b,r}
f_{K_\nu,e_r}(P_1)f_{M_\nu,c_r}(P_2).
}
\tag{15}
$$
$P_1,P_2$ 在同一固定参数曲线的两个覆盖因子上，分别有导子 $L_1,L_2$；这里下标 $2$ 仅表示第二因子，底层导子始终为原 $L=L_2$。

由(10)，对整个参数对角有
$$
\mathcal K_\nu(Q,Q)=
A^\flat(Q,0)H_\nu^\flat(Q,0).
\tag{16}
$$
但四个**原乘积**的水平质量准确为
$$
\boxed{
f_\nu^\flat(Q)=\mathcal K_\nu(\widetilde P,Q).
}
\tag{17}
$$
具体地，其水平截面是
$$
F_\nu^\flat(Q,z)=
\sum_{a,b,r}\Gamma_{\nu;a,b,r}
f_{K_\nu,e_r}(\widetilde P)F_{M_\nu,c_r}(Q,z).
\tag{18}
$$
(18)在 $\widetilde P$ 等于整个 $A(z)H_\nu(z)$，且每个系数
$f_{K,e_r}(\widetilde P)$ 是固定代数常数，因此(18)为真正水平延拓。
唯一性即证明(17)等于上一注定义的原 $f_\nu^\flat$。

相反，$A^\flat(Q,z)H_\nu^\flat(Q,z)$ 在第二参数的 degree $M$ 连接下通常不水平；其相对质量仍是 $f_{K,e_r}(Q)$。将它误换成(18)，正好会删除 R855 的 balanced 相对热项。式(15)–(18)把这一区别保留在明确的同一个有限核中。

特别，所有四个 $f_\nu^\flat$ 的系数同时含同一个真实 $a_a$。本注没有在各 $\nu$ 上重新选择独立的质量、周期、Gaussian 或初始条件。

## 5. 两参数核的完整三阶切锥

在 $\widetilde P$ 的参数邻域取固定特征零流参数 $u,v$，使
$L_1=\partial_u,L_2=\partial_v$ 于对应流中。这只用于有限 Taylor 恒等式；没有在模 $p$ 改用随 $p$ 选择的坐标。

式(10)在原 CM 纤维的物理源是
$$
\mathscr F_\nu(Z,W)
=A\!\left(Z+\frac ngW\right)
H_\nu\!\left(Z-\frac{24}gW\right).
\tag{19}
$$
所有总阶小于 $6$ 的物理 jet 为零，总阶 $6$ 的齐次项准确为
$(Z+(n/g)W)^6$。

用上一注的 $T_r$，完整混合 jet 等式为
$$
\partial_Z^{2r}\partial_W^{2s}\mathscr F_\nu(0,0)
=(2M)^r(2K)^s
\left(T_r^{(2)}T_s^{(1)}\mathcal K_\nu\right)
(\widetilde P,\widetilde P).
\tag{20}
$$
因为 $T_r=L^r+\text{较低阶}$，先由(20)逐阶得到
$$
(L_2^rL_1^s\mathcal K_\nu)(\widetilde P,\widetilde P)=0
\quad(r+s<3).
$$
再对 $r+s=3$，所有低项都严格为零，给
$$
\boxed{
(L_2^rL_1^s\mathcal K_\nu)(\widetilde P,\widetilde P)
=\frac{720(n/g)^{2s}}{(2M)^r(2K)^s}
=\frac{90}{M^3}\left(\frac n{24}\right)^s.
}
\tag{21}
$$
因此原两参数核的三阶切锥是
$$
\boxed{
\mathcal K_\nu(u,v)=
\frac{15}{M^3}
\left(v+\frac n{24}u\right)^3
+O((u,v)^4).
}
\tag{22}
$$
取 $u=0$ 得原 $f_\nu^\flat$ 的第三导数 $90/M^3$；
取 $u=v$ 得 $A^\flat(0)H_\nu^\flat(0)$ 的第三导数 $90/24^3$。
这两个不同方向都来自同一个实际核；不把它们相认。

## 6. 四个原除 p 行及两谱的准确位置

令 $N=(p+1)/2$。式(17)给出原指定行
$$
\boxed{
\mathfrak B_\nu
=(2M_\nu)^N
\frac{
(T_N^{(2)}\mathcal K_\nu)(\widetilde P,\widetilde P)
}{p}\pmod p.
}
\tag{23}
$$
整除 $p$ 的范围仍只是这一原点值。可整下降的版本是
$$
\mathfrak B_\nu=
2M_\nu\epsilon_{M_\nu}
\left(\mathcal Q_{p,\epsilon_{M_\nu}}^{(2)}
\mathcal K_\nu\right)(\widetilde P,\widetilde P),
\tag{24}
$$
其中第二因子上的 $H L+C/2$ subtraction 完整保留。
第一因子 $f_{K,e_r}(\widetilde P)$ 已被冻结；不能再对它施参数导子，
也不能把第一因子的 $\epsilon_K$ 当成第二因子的 $\epsilon_M$。

若改在两参数对角求导，链式法则精确产生全部混合项
$L_1^aL_2^b\mathcal K_\nu$。式(20)给它们的原 whole 来源。
(13)只是这两个实际谱标签与原张量乘法的相容性，
不证明(23)非零，也不赋任何相对 $K$ 行原中央零。
同一两谱的完整函数域投影及保留原 Hasse 缺陷的 CM 除 $p$ 留数式，见
[原半长 Bol 与 CM 留数](2026-11-16-original-half-bol-and-cm-divided-residue.md)；
这里只使用第二因子上原固定收缩的那一行，不把第一因子重新解冻。

## 7. 不能省去的两个混合除 p 端点

这一点可在同一个原源中完全展开，不必引入未明的负矩池。
设
$$
a_j=D_z^jA(0),\qquad h_j=D_z^jH_\nu(0),\qquad
u=\frac ng,\quad v=\frac{24}g,
$$
$$
J_{r,s}=\partial_Z^r\partial_W^s
\{A(Z+uW)H_\nu(Z-vW)\}_{(0,0)}.
\tag{25}
$$
$J_{p+1,0}/p$ 是(23)。相对片
$A(uW)H_\nu(-vW)$ 也是原明确 degree $K$ 中心零来源，所以
$J_{0,p+1}/p$ 同样整。两个混合端点 $J_{p,1},J_{1,p}$ 也被 $p$ 整除，但这里不对奇的偏导截面调用偶格结论。直接使用下文的两个精确微分恒等式：它们把混合端点写成 $J_{p+1,0}$、$J_{0,p+1}$ 与 $D_z^p\{A(xz)H_\nu'(yz)\}(0)$ 的固定有理线性组合。后者的 Leibniz 两个端项因 $A(0)=0$、$H_\nu'(0)=0$ 严格为零，所有中间 $\binom pk$ 都被 $p$ 整除。因此全部混合整性直接来自原两个偶来源的整性和同一个精确低卷积，不需要额外 whole 奇格推广。

它们通常不能在除 $p$ 后置零。定义两个**完整低卷积**
$$
\mathcal L_p(x,y)=
\sum_{k=2}^{p-1}
\frac{(-1)^k}{k(k-1)}
x^k y^{p+1-k}a_kh_{p+1-k},
\tag{26}
$$
$$
\mathcal C_p(x,y)=
\sum_{k=1}^{p-1}
\frac{(-1)^{k-1}}{k}
x^k y^{p-k}a_kh_{p+1-k}.
\tag{27}
$$
(27)不是 R856 的 Hasse 导数 $C$；此处字体和两个自变量区分它。
所有值均在原整格中计算后模 $p$。由
$\binom{p+1}{k}/p$ 与 $\binom pk/p$ 的准确余数，得到
$$
\begin{aligned}
B_M:=J_{p+1,0}/p
&=B_A+\mathcal L_p(1,1),\\
B_K:=J_{0,p+1}/p
&=u^2B_A+\mathcal L_p(u,-v),\\
J_{p,1}/p
&=uB_M-(u+v)\mathcal C_p(1,1),\\
J_{1,p}/p
&=u^{-1}B_K+(1+v/u)\mathcal C_p(u,-v).
\end{aligned}
\tag{28}
$$
这里 $B_A=j_{p+1}(A)/p$，只使用原 $A(0)=A'(0)=0$、
$H_\nu(0)=1,H_\nu'(0)=0$；$u^{p+1}\equiv u^2$ 因 $u$ 是固定有理数。
例如第三式来自真正微分恒等式
$$
\partial_W\mathscr F_\nu(Z,0)
=u\,D_Z(AH_\nu)-(u+v)AH_\nu',
$$
而第四式来自
$$
\partial_Z\mathscr F_\nu(0,W)
=u^{-1}D_W\{A(uW)H_\nu(-vW)\}
+(1+v/u)A(uW)H_\nu'(-vW).
$$
式(28)全部发生在同一个原物理变量中。

因此在(7)下重写 $p+1$ 阶 Hurwitz 行时，
$k=1,p$ 的 binomial 系数为 $p+1$，不是 $p$ 倍；
必须保留(28)的两个混合除 $p$ 端点。
它们可以准确还原成同一个 $B_A$ 和(26)–(27)，
但不能因模 $p$ 时 $J_{p,1}=J_{1,p}=0$ 就删除。

## 8. 已付的实际约束及剩余问题

本注把原共同 $A_{24}$ 从形式乘法提升为：

- 完整二变量、绝对正规、标签数准确的有限 theta 恒等式(10)；
- 四个原水平来源的同一固定 CM 收缩(15)–(18)；
- 保全部伙伴的指定三阶切锥(21)–(22)；
- 与两个实际半长谱相容的字符恒等式(13)；
- 以及对原除 $p$ 行必需的全部混合端点(28)。

这些关系保持每个原来源的所有物理 jet，因此没有改变原 $P_{2,M}$、
CM13 frame、四中央必要条件及其原格成本。辅助相对 theta 空间在本注中只是
同一乘积的有界有限代数呈示；没有把其所有截面加进原来源格。

真正尚须决定的是(23)在这四个**特定固定收缩**上能否同时为零。
(22)的非零切锥不替代这个除 $p$ 结论；(28)仍保全部原低卷积。
若要利用参数方向的 CM13 或其它 Hecke 对应，
还必须付该对应对(10)两因子和原完整 frame 的同步运输；
常系数延拓的有限矩阵不自动等于这一几何对应。
