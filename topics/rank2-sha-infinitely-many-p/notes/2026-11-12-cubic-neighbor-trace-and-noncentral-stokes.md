# 三次邻点迹的单位首层与非中央 Stokes 分支

日期：2026-11-12。状态：本文的模 $p$ 比较及固定 CM 扭曲的角色范围
均已证明。没有声称三次迹在特征零中等于某个 Stokes 常数，
也没有由这个非中央单位推出目标中央导数非零。

## 1. 保留两项边界贡献的准确比较

固定惰性素数 $p\ge7$，令 $d=p+1$、$\varpi^d=p$。
沿用同一实际 $M_e,K,L=tJ,s=1-4t^2$ 及
$$
 I(t)=\int_0^t\frac{M_eK}{sL^2}\,dt.
$$
取包含全部固定层标记及 $\mathbb F_{p^2}$ 的有限未分歧系数域 $B$。
[R85 的实际邻点](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)
给出：$K$ 的 $d$ 个最近零点组成 $B(\varpi)/B$ 的完整 Galois 轨道。
对其中任一点 $r$，记
$$
 T_{3,p}=\operatorname{Tr}_{B(\varpi)/B}
                   \frac{I(r)}{L(r)^3}.
 \tag{1.1}
$$

实际中央系数与已经认证的半权截面满足
$$
 A(z)=\sum_{4\mid m}\beta_m z^m=z^4+\cdots,\qquad
 C_m=\frac{m!}{24\cdot17^{m-4}}\beta_m^2.
 \tag{1.2}
$$
因此 $C_4=\beta_4^2=1$，且 $M_e(t)=C_4t^4+O(t^6)$。

[R89 的完整尾界](2026-11-12-actual-weighted-primitive-trace-unit.md)
不是只取 $I$ 的首项：它证明
$$
 \overline{\varpi^{-3}I(\varpi X)}
   =C_4\left(\frac{X^3}{3}
                  +\frac{\kappa_pX^{d+3}}4\right),\qquad
 \overline{K(\varpi X)}=1+\kappa_pX^d,\qquad
 \overline{L(\varpi X)/\varpi}=X,
 \tag{1.3}
$$
其中 $\kappa_p\in\mathbb F_p^\times$。
所有未写出的项在相同 Tate 范数下严格小于一并趋于零；
积分次数 $p$ 的唯一较早除 $p$ 风险已用实际 $C_d\in p\mathbb Z_p$
处理。因此 (1.3) 可以在全部真实邻点取值。

在根上 $X^d=-\kappa_p^{-1}$，两个贡献相加给
$$
 \overline{I(r)/L(r)^3}
   =C_4\left(\frac13-\frac14\right)=\frac{C_4}{12}.
$$
域迹属于 $B$；其误差属于
$\varpi\mathcal O_{B(\varpi)}\cap B=p\mathcal O_B$。
用 $d\equiv1\pmod p$，得到
$$
 \boxed{\quad 12T_{3,p}\equiv C_4=\beta_4^2=1\pmod p.\quad}
 \tag{1.4}
$$
所以这个单位首层准确检测已经固定的最低非零系数 $C_4$。
若舍掉 (1.3) 的第二项，会错误地得到 $1/3$。

## 2. 同一个首层是已知非中央 $\mathcal S_4^2$

[实际全余类 Stokes 分解](2026-11-12-inert-euler-primitive-stokes-decomposition.md)
写成
$$
 A(z)=e^{az^d}G(z),\qquad v_p(a)=-1,\qquad
 g_{j,h}=[z^{dh+j}]G,
$$
$$
 \mathcal J_{p,j}(u)
   =\sum_{h\ge0}a^{-h}g_{j,h}(u)_{\underline h},
 \qquad
 \mathcal S_j=\mathcal J_{p,j}(-j/d)\quad(0<j<d,\ 4\mid j).
 \tag{2.1}
$$
这是真正收敛的解析变换；下标 $j$ 表示 Taylor 余类。
其整估计给 $a^{-h}g_{j,h}\in p\mathbb Z_p$ 对所有 $h\ge1$ 成立。
因为 $j/d\in\mathbb Z_p$，上升阶乘
$(-1)^h(j/d)_{\overline h}$ 也整，于是
$$
 \mathcal S_j\equiv g_{j,0}=\beta_j\pmod p.
 \tag{2.2}
$$
对每个目标 $p$ 都有 $4<d$，故 $j=4$ 可用。结合 (1.4)，
$$
 \boxed{\quad
 12T_{3,p}\equiv\mathcal S_4^2\equiv1\pmod p.
 \quad}
 \tag{2.3}
$$
这是一条模 $p$ 比较；本文没有证明
$12T_{3,p}=\mathcal S_4^2$，也没有证明更高 $p$ 进位只依赖 $\mathcal S_4$。
目标仍是另一余类的
$\mathcal S_0=-\mathcal J_{p,0}'(0)$。
R89 的现有单位证明只提供 (2.3)，未提供这两个余类之间的新关系。

## 3. 中央与 $j=4$ 分支的真实局部角色

角色规范采用
[R50 的实际惰性整格比较 §1.2](2026-11-12-inert-central-reference-curve-comparison.md)。
设 $\psi$ 是曲线的 CM 特征，$\kappa$ 是 $K_p/\mathbb Q_p$
的 Lubin--Tate 特征，$\tau$ 是未分歧二次自同构。
在剩余域的 Teichmüller 单位上，令 $\omega_2$ 为基本二阶特征；
则 $\kappa^\tau$ 的 tame 部分为 $\omega_2^p$。
权 $m$ 的中央 Hecke 特征及其相对基层特征为
$$
 \psi^{m+1}\bar\psi^{-m},\qquad
 (\psi/\bar\psi)^m.
$$
因此相对 tame 角色为
$$
 \omega_2^{(1-p)m},
 \tag{3.1}
$$
其平凡条件准确是 $p+1\mid m$。
若采用相反的 reciprocity 约定，(3.1) 同时取逆，以下阶数不变。

$\mathcal J_{p,j}$ 编码的非负整数权为 $m=dk+j$。
通过 (1.2)，它们所对应的原全权中央数据属于相对 tame 特征
$\omega_2^{(1-p)j}$ 的分支。
在这一全权字符族中继续 wild 参数，不会删除这个 tame 特征。
特别 $j=4$ 所关联的全权数据的相对 tame 角色准确有阶
$$
 \frac{p+1}{\gcd(p+1,4)}=\frac{p+1}{4}>1.
 \tag{3.2}
$$
它不是 R50 用来控制基层 $\Sha[p^\infty]$ 的平凡 tame 中央分支。
这里的角色断言作用于关联的全权 Hecke 数据；
没有另行构造使半因子数值 $\mathcal J_{p,j}$ 或 Stokes 常数
$\mathcal S_j$ 自身成为一维 Galois 特征向量。
特别不能把 $\mathcal S_j=\mathcal J_{p,j}(-j/d)$ 这条解析求值，
未经额外比较便解释成某个 Galois 向量的特化。

## 4. 固定有限候选论证在这里尚缺什么

以下是一个明确而有限的排除范围。取固定有限条
$K=\mathbb Q(i)$-CM 椭圆曲线，以及它们之间的固定有限阶扭曲、
固定同源和固定 prime-to-$p$ 层标记操作。
删除它们的坏约化素数、扭曲导子和同源次数所含的有限集合后：

- 有限阶扭曲在 $p$ 处未分歧，故不改变 (3.1) 的惯性限制；
- 素于 $p$ 的同源给 CM Tate 表示的等变同构；
- prime-to-$p$ 标签运输或相应 Hecke 对应与局部惯性作用相容。

所以对上述关联 CM 字符数据，由这些等变箭头直接形成的比较保持
tame 分量，不能把 (3.2) 的非平凡分量同构到任何候选曲线的基层中央分量。
等价地，在含这些 tame 值的系数域中，不同惯性特征的等变 Hom 为零。
这个结论没有使用任何候选曲线的秩，更不能由它保证存在合适的秩二候选。

固定改变无穷型也不是一个未经说明的椭圆扭曲：例如将 $m$ 从零移到
四，对应 $\psi^5\bar\psi^{-4}$，Hodge 型为 $(5,-4)$；
它不是无穷型 $(1,0)$ 的椭圆曲线 CM 特征。
若改用一个在 $p$ 分歧的扭曲去抵消 (3.2)，该扭曲及其导子将随 $p$ 改变，
已经超出固定有限候选的上述机制。

本节只排除了这些直接的、角色相容的固定箭头。
它没有排除未知的非线性周期恒等式、加入新算术输入后的标量线性关系，
或不同 CM 域/非 CM 曲线的另一路比较。
要把三次迹用于主目标，仍须实际证明它与某些固定秩至少二曲线的
中央导数之间的等式，并支付分支、整格及系数的全部比较。
目前 (2.3) 给出的恒单位已经由已知 $\mathcal S_4$ 解释，
不能单独支付这个缺口。
