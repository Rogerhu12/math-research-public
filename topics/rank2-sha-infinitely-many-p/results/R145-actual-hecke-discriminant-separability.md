# R145：原 Hecke 判别式可分，实际检验等价于 CM 极点

状态：**已证明**。日期：2026-11-12。

[完整证明](../notes/2026-11-12-actual-hecke-discriminant-separability.md)。
本结果仅适用于 R139、R141、R142 的非 CM 非零总迹，
不外推到 $E_{17}$ 的 $n=0$ 行。

## 实际对象

令 $g_p=\Theta^{p-2}\bar f/H^p$ 是 $E389$ 的原去 $p$ 函数，
$\ell+1=pu$、$p\nmid u a_\ell$。
在固定 fine level $M$ 的连通 full $\ell$-level 中心商上，
$G=\mathrm{PSL}_2(\mathbb F_\ell)$ 作用于原同源支 $h_v$，
其总迹
$$
                      n=\sum_vh_v=\bar a_\ell g_p\ne0
$$
被 $G$ 固定。原 $U$ 迹 $B$ 给
$$
 A=D_1B,\quad F_2=D_2B,\quad
 \tau A=A-n,\quad \tau F_2=F_2+n-A.
\tag{1}
$$

## 完整证明的核心

置 $\mathcal M=k[\mathbb P^1(\mathbb F_\ell)]$、
$I=\ker\sum$。由于奇 $p\mid\ell+1$，
Saunders（2022）§3 印页 8–10 的准确 principal-block 结构给
$I/k{\bf1}$ 不可约。其适用性可直接核定：
Borel 为 $p'$ 群，$\mathcal M$ 是 projective；
其 endomorphism ring 为 $k[J]/(J^2)$，所以
$\mathcal M=P(k)$，而所引结构为 $[k\mid V\mid k]$。

映射
$$
       (c_v)\longmapsto d\left(\sum_vc_vh_v/n\right)
\tag{2}
$$
是 $G$-线性的，且常向量在核。
在同一个 Tate 参数 $Q=q^{1/(M\ell)}$ 中，
$(h_\infty-h_0)/n$ 首阶为
$M(1-\ell)\equiv2M\not\equiv0\pmod p$，故 (2) 不杀掉整个
$I$。不可约性遂说明它在 $I/k{\bf1}$ 上单射。
$A$ 的原权向量在每个 $\tau^jU$ 轨道取值 $j$，
属于 $I\setminus k{\bf1}$，所以
$$
                               d(A/n)\ne0.
\tag{3}
$$

若 $W=A\,dF_2-F_2\,dA$ 恒零，令 $r=F_2/A$、$x=A/n$。
由 (1) 得
$x-1=r/(1-r+\tau r)$，而 $dr=d(\tau r)=0$，
与 (3) 矛盾。因此
$$
                                  W\ne0.
\tag{4}
$$
它一般不下降，仍保留
$(\tau-1)W=F_2\,dn-n\,dF_2$。

对原底曲线不变量
$$
                \mathscr D=A^2-nA-2nF_2,\qquad
                       \mathcal C=\mathscr D/n^2,
\tag{5}
$$
不可约 heart 又保证存在一个实际尖点，使
$A$ 的阶为 $M$、$F_2$ 的阶至少 $M$，而 $n$ 的阶为 $M\ell$。
证明是在固定尖点取首 $Q^M$ 系数这个非零 heart 线性函数，
再作用于 $A$ 的 $G$-轨道；没有更换连通配对分量。
因此该尖点处
$$
                \operatorname{ord}\mathscr D=2M,\qquad
                \operatorname{ord}\mathcal C=2M(1-\ell).
\tag{6}
$$
两阶均不被 $p$ 整除，严格得到
$$
                    \mathscr D\ne0,\quad
                    d\mathscr D\ne0,\quad d\mathcal C\ne0.
\tag{7}
$$
所用中心和 torus 商在尖点无额外分歧，因为相对惯性阶为 $\ell$。
注意 (6) 本身已经给 $\mathscr D$ 的一个重尖点零，
所以不应追求其全局零除子平方自由。

## 原 CM 点上的准确极点判据

对 R141 的真实 CM 底点 $z$，有 $v_z(n)=1$。
R142 正规形给
$$
             A=-ny+a,\quad
             F_2=\tfrac n2y(y+1)-ay+g,\quad
             \mathscr D=a^2-na-2ng.
$$
若 $a(z)\ne0$，$\mathcal C$ 有二阶极点。
若 $a(z)=0$、$g(z)\ne0$，
$d\mathscr D(z)=-2g(z)dn(z)\ne0$，故 $\mathcal C$ 有一阶极点。
若 $a(z)=g(z)=0$，$\mathcal C$ 正则。
于是
$$
 \boxed{\quad
 F_2|_{\pi^{-1}(z)}\ne0
       \quad\Longleftrightarrow\quad
                    \mathcal C\text{ 在 }z\text{ 有极点}.
 \quad}
\tag{8}
$$
R142 保留的原 $Q$ 群环单位比较使任一个这样的 CM 极点
推出该 $p$ 的 $\Sha(E/\mathbb Q)[p^\infty]=0$。

目前 (7) 及真实尖点极点没有证明 (8) 在指定 CM 点发生。
后续必须控制 $\mathscr D$ 与原源零除子在该点的共同阶；
不能把几何 $G$-共轭标记当成原算术环类迹的自由选择。

## 文献

J. Saunders，*Cohomology of $\mathrm{PSL}_2(q)$*，
Journal of Algebra **595** (2022), 347–379，
[§3 正式版作者稿](https://arxiv.org/pdf/2002.04183v3)。
实际覆盖、Hecke 规范和局部整性分别见 R137、R141、R142；
上述可分性与极点判据的其余步骤已在本卡和所链笔记证明。
