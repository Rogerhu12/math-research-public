# 原 Hecke 二阶判别式的可分性与 CM 极点检验

日期：2026-11-12。**已证明。** 本篇仅处理 R142 中总迹
$n\ne0$ 的实际非 CM 行。用真正的 full-level 群作用和同一个
Tate 尖点证明 $W,\mathscr D,d\mathscr D,d(\mathscr D/n^2)$
都不恒为零；然后准确说明原 CM 检验等价于哪里出现极点。
它不以泛点的可分性替代指定 CM 点上的非零性。

## 1. 实际函数与不可约 heart 的适用范围

沿用 R139、R141、R142，令 $E=389\mathrm a1$，
$g_p=\Theta^{p-2}\bar f/H^p$，其 q 展开首项为 $q$。
取 $p\ge7$、$\ell\ne p$，满足
$$
       \ell+1=pu,\qquad p\nmid u,\qquad
       a_\ell(E)\not\equiv0\pmod p.
\tag{1}
$$
选择一个固定 fine level $M$，使 $389\mid M$、$p\ell\nmid M$。
例如可用 full $M=3\cdot389$；这个 $3$ 只用于细模覆盖，
**没有**给原类数 $1$ 的 $g_p$ 添加 $V_3g_p$。

在固定 Weil 配对分量的 full $M\ell$ 覆盖上，再除掉只作用于
$\ell$-level 的中心 $\{\pm I\}$，得连通曲线 $\widetilde X$，
其相对 deck 群是
$$
                         G=\mathrm{PSL}_2(\mathbb F_\ell).
\tag{2}
$$
R137 的模型论证保证这一步在特征 $p$ 保持连通；
$p\mid\ell+1$ 不破坏 $\ell$-level 的 étale 性。
对 $v\in\mathbb P^1(\mathbb F_\ell)$，记原 $\ell$ 商支的拉回为
$h_v$。这些都是同一个函数域中的实际函数。
几何 Hecke 总迹准确为
$$
                \sum_vh_v=n
                  =\bar a_\ell\,g_p\circ r_{\rm src}\ne0,
\tag{3}
$$
而 $n$ 被整个 $G$ 固定。

现在令 $k=\overline{\mathbb F}_p$，设
$$
 \mathcal M=k[\mathbb P^1(\mathbb F_\ell)],\qquad
 I=\ker\left(\sum:\mathcal M\longrightarrow k\right),\qquad
 {\bf1}=\sum_ve_v.
\tag{4}
$$
因为 $p\mid\ell+1$，$k{\bf1}\subset I$。所用表示论输入为
$$
                         I/k{\bf1}\ \text{不可约}.
\tag{5}
$$
这里必须保留 $p$ 为奇数、$p\mid\ell+1$ 的 cross-characteristic
条件；没有使用特征二时可能分裂成两个因子的版本。

准确的原始来源是 Jack Saunders，
*Cohomology of $\mathrm{PSL}_2(q)$*，Journal of Algebra
**595** (2022), 347–379，[正式版作者稿](https://arxiv.org/pdf/2002.04183v3)，
§3，印页 8–10：对奇 $r\mid q+1$，principal block 的
$P(k)$ 有 radical factors $[k\mid V\mid k]$，$V$ 不可约。
本篇取其 $q=\ell,r=p$。
为说明这确实给 (5)，Borel 的阶为 $\ell(\ell-1)/2$，素于 $p$，
所以 $\mathcal M=\operatorname{Ind}_B^Gk$ 是 projective。
其秩二置换作用给
$$
 \operatorname{End}_G(\mathcal M)=k\cdot\mathrm{id}+k\cdot J,
                   \qquad J^2=(\ell+1)J=0.
$$
这是局部环，故 $\mathcal M$ 不可分解；其平凡 quotient 表明
$\mathcal M=P(k)$。因此 $I=\operatorname{rad}\mathcal M$，
$k{\bf1}=\operatorname{soc}\mathcal M$，(5) 正是所引三层结构。
没有把普通复 Steinberg 的不可约性错误地沿用到特征 $p$。

## 2. 同一尖点中不可被 $p$ 次幂消掉的阶

在原 Tate 尖点，令 $Q=q^{1/(M\ell)}$ 为真局部参数。
R137 的同源标记给
$$
 h_\infty=g_p(q^\ell),\qquad
 h_a=g_p(\zeta_\ell^a q^{1/\ell}),\quad a\in\mathbb F_\ell.
\tag{6}
$$
因此
$$
 \operatorname{ord}_Q n=M\ell,\qquad
 h_\infty-h_0=-Q^M+\text{高次项}.
\tag{7}
$$
这些展开都在固定配对分量的同一完成域中。
后面的 $G$-作用不更换配对值，也不跨到另一连通分量。

定义 $G$-线性映射
$$
 \mathcal L:\mathcal M\longrightarrow
                   \Omega^1_{k(\widetilde X)/k},\qquad
 (c_v)\longmapsto d\left(\frac{\sum_vc_vh_v}{n}\right).
\tag{8}
$$
由 (3)，$\mathcal L({\bf1})=d1=0$。
另一方面，由 (7)，$(h_\infty-h_0)/n$ 的首阶为
$$
                M(1-\ell)\equiv2M\not\equiv0\pmod p.
\tag{9}
$$
故 $\mathcal L(e_\infty-e_0)\ne0$。
结合 (5)，$(\ker\mathcal L\cap I)/k{\bf1}$ 是不可约
$I/k{\bf1}$ 的真子模，只能为零。因此得到：
$$
 \boxed{\quad
 c\in I\setminus k{\bf1}
   \quad\Longrightarrow\quad
       d\left(\frac{\sum_vc_vh_v}{n}\right)\ne0.
 \quad}
\tag{10}
$$
这证明的是实际函数的可分性，强于只知道其常系数行非零。
整个论证没有对剩余表示的 $\mathrm{GL}_2$ 满像另作假设。

## 3. 原二阶行的 Wronskian 确实非零

保留 R142 的原 $U$ 迹和权：
$$
 B=\sum_{v\in Uv_0}h_v,\qquad
 A=D_1B,\quad F_2=D_2B,\qquad
 \tau A=A-n,\quad\tau F_2=F_2+n-A.
\tag{11}
$$
在 $\tau^jUv_0$ 上，$A$ 的系数为 $j$。
其总和是 $u\sum_jj=0$，且它不是常向量。
于是 (10) 给
$$
                              d(A/n)\ne0.
\tag{12}
$$

令 $W=A\,dF_2-F_2\,dA$。假设 $W=0$，则
$r=F_2/A$ 满足 $dr=0$，且 $d(\tau r)=0$。
这里 $A,F_2$ 均不恒零：任一个恒零都会由 (11) 迫 $n=0$。
置 $x=A/n$，由 (11) 直接算得
$$
                         x-1=\frac{r}{1-r+\tau r}.
\tag{13}
$$
分母不恒零，否则原恒等式迫 $r=0$。对 (13) 微分便得
$dx=0$，与 (12) 矛盾。因此
$$
                               W\ne0.
\tag{14}
$$
它在中间 $C_p$ 覆盖上的非零性由可分拉回单射得到。
仍然不能写成底曲线的微分：R142 的准确式是
$(\tau-1)W=F_2\,dn-n\,dF_2$。
本节依赖 $n\ne0$；不将 (14) 外推给 $E_{17}$ 的零总迹行。

## 4. 判别式及其归一化也真正可分

定义 R142 的底曲线函数
$$
          \mathscr D=A^2-nA-2nF_2,\qquad
                         \mathcal C=\mathscr D/n^2.
\tag{15}
$$
现在证明
$$
                 \mathscr D\ne0,\qquad
                 d\mathscr D\ne0,\qquad
                 d\mathcal C\ne0.
\tag{16}
$$

在 (6) 的固定尖点，以 $\lambda(c)$ 表示
$\sum_vc_vh_v$ 的 $Q^M$ 系数。
由 (7)，$\lambda({\bf1})=0$，且
$\lambda(e_\infty-e_0)=-1$。所以它在不可约
$I/k{\bf1}$ 上是非零线性函数。
$A$ 的权向量在该模中非零，因而其 $G$-轨道张成整个模。
故存在 $\gamma\in G$，使 $\gamma A$ 的 $Q^M$ 系数非零。
与此同时，所有 $h_v$ 至少从 $Q^M$ 起，故
$$
 \operatorname{ord}_Q(\gamma A)=M,\quad
 \operatorname{ord}_Q(\gamma F_2)\ge M,\quad
 \operatorname{ord}_Qn=M\ell.
\tag{17}
$$
$n$ 被 $\gamma$ 固定，$\ell>1$，所以
$$
 \operatorname{ord}_Q(\gamma\mathscr D)=2M,\qquad
 \operatorname{ord}_Q(\gamma\mathcal C)=2M(1-\ell).
\tag{18}
$$
它们的首项系数非零，而且两个阶模 $p$ 分别为 $2M,4M$，
均非零。这证明 (16)。
等价地，这是原 $\mathscr D,\mathcal C$ 在另一个实际尖点的展开；
没有把不同 $G$-共轭行当成指定 CM 点的不同算术输入。

真 full-level 到中心商及其后 $T_0$ 商在这些尖点均无额外分歧：
原忘记 $\ell$-level 的尖点惯性阶为 $\ell$，
与中心及 nonsplit torus 的阶互素。
故 (18) 也给相应中间曲线上的真实阶。
尤其 $\mathscr D$ 的全局零除子已经有重尖点，
不应将“全局平方自由”当作后续需要证明的命题。
所需的是指定 ordinary CM 点的条件。

## 5. 原 CM 检验准确等价于出现一阶或二阶极点

取 R141 的合法源 split 素数，并取原带标记 CM 底点 $z$，
使 $v_z(n)=1$。R142 的整 AS 正规形为
$$
 A=-ny+a,\qquad
 F_2=\frac n2y(y+1)-ay+g,\qquad
 \mathscr D=a^2-na-2ng.
\tag{19}
$$
由此有完整的三种情况：

| 在 $z$ 处的实际值 | $\mathscr D$ 的阶 | $\mathcal C=\mathscr D/n^2$ |
|---|---:|---|
| $A(z)=a(z)\ne0$ | $0$ | 二阶极点 |
| $a(z)=0$，$F_2$ 在整个纤维为非零常数 $g(z)$ | $1$ | 一阶极点 |
| $F_2$ 在整个纤维为零，即 $a(z)=g(z)=0$ | 至少 $2$ | 正则 |

第二行用
$d\mathscr D(z)=-2g(z)\,dn(z)$，不是对一般函数的重零猜测。
因此准确得到
$$
 \boxed{\quad
       F_2|_{\pi^{-1}(z)}\ne0
          \quad\Longleftrightarrow\quad
             \mathcal C\text{ 在 }z\text{ 有极点}.
 \quad}
\tag{20}
$$
左边表示完整纤维向量非零，不表示每个分裂分量都非零。
R142 已付清它与原 $Q$ 半局部二阶检验的群环单位比较，
所以 (20) 的任一个原 CM 极点就给对应 $p$ 的
$\Sha(E/\mathbb Q)[p^\infty]=0$。

(16) 证明 $\mathcal C:Z\to\mathbb P^1$ 是真正可分的非恒定映射，
(18) 还给一处真实尖点极点。它们没有证明该极点除子包含
任何指定 ordinary CM 点。下一项特殊输入应限制
$\mathscr D$ 与原源零除子 $(n)_0$ 在这些 CM 点的共同阶，
或直接证明原 $\mathcal C$ 在其中有极点。
不能把 $\gamma$ 改变的几何 level 标记当成原环类子群的任意变换。

## 来源

- J. Saunders，*Cohomology of $\mathrm{PSL}_2(q)$*，
  Journal of Algebra **595** (2022), 347–379，
  DOI [10.1016/j.jalgebra.2021.11.049](https://doi.org/10.1016/j.jalgebra.2021.11.049)；
  [正式版作者稿](https://arxiv.org/pdf/2002.04183v3)，
  §3 印页 8 的置换模记号、印页 9 的 $r\mid q+1$ case 1，
  及印页 10 的 $P(k)=[k\mid V\mid k]$。
  文中以 $r$ 表示系数特征；这里对应 $p$，并非 $\ell$。
- R137：真实同源支、共同 Tate 参数、连通 full-level 模型和中心商。
- R141：原非 CM 去 $p$ 原函数、准确 Hecke 总迹和指定源简单零。
- [R142 的整 AS 证明](2026-11-12-actual-as-basepoints-and-hecke-discriminant.md)：
  (11)、(15)、(19) 的真实行、群环单位及完整纤维规范。
- (8)–(20) 在本篇直接证明；未引用未证明的 Ihara 饱和、
  指定 CM 特化非零或平方自由定理。
