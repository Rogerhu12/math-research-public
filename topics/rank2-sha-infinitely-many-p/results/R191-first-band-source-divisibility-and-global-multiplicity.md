# R191. 原源第一带的整块整除与全局二次消失阶界

日期：2026-11-12。**状态：以下第一带整除、严格有限素数界及
全局 $(1+o(1))D^2$ 消失阶界均已证明。** 全部结论针对同一个
原多项式及其完整曲线前缀，不假定其不同齐次块分别消失。
本篇不需要两个中央导数为零，也没有由消失阶界推出严格的
惰性 jet 范数预算。

## 1. 实际源、参数与待检测的系数块

沿用 R188 的原固定函数 $A(w),B(w)\in w\mathbb Q[[w]]$，
其中 $w=z^4$，并令
$$
 C=B-A,\qquad A=w+O(w^2),\qquad C=v_0w^2+O(w^3),
 \qquad v_0=-22.
 \tag{1}
$$
固定惰性素数 $p=4r-1\ge7$，排除 $p=11$，置
$R=r(p-1)$。以下所有原源系数的整性都指 $\mathbb Z_p$；
$v_0$ 及 $17$ 均为单位。

以下取 $D\ge1$；$D=0$ 的非零常数另有消失阶零。
原次数至多 $D$ 的整源可以准确写作
$$
 P_0(A,B)=\sum_{i+j\le D}c_{i,j}A^iC^j
 =\sum_{0\le c\le m\le D}a_{m,c}A^{m-c}C^c.
 \tag{2}
$$
这里 $m=i+j,c=j$，两个基都与原 $A,B$ 单项式基整可逆。
给这一列定义整数
$$
 l=i+2j=m+c.
 \tag{3}
$$
它是该列沿原曲线及径向轴的最低消失阶。本文的“$l$ 块”
仅指 (2) 中具有同一 (3) 的列；没有将它单独置入前缀核。

对 $1\le l\le2D$，该块的径向次数依次为
$$
 m_-(l)=\lceil l/2\rceil,\qquad
 m_+(l)=\min(l,D),\qquad
 q_l=m_+(l)-m_-(l)+1.
 \tag{4}
$$

## 2. 同一个完整前缀给出的第一带整行

R174/R177 的真实 Cartan 坐标满足
$$
 U(w)=u_0w^r+O(w^{r+R}),\qquad
 V(w)=w+O(w^{R+1}),\qquad
 \tau=pu_0\bmod p\in\mathbb F_p^\times.
 \tag{5}
$$
将同一个原 $P_0$ 写成环境级数
$$
 \widetilde P_0(U,V)=\sum_{i,j\ge0}L_{i,j}(P_0)U^iV^j,
 \qquad L_{i,j}(P_0)\in\mathbb Z_p.
 \tag{6}
$$
整性来自原源和真实环境的整可逆坐标，不是从曲线系数的
整性倒推。

设 $0\le l<r$、$h\ge0$，且 $rh+l<R+1$。由 (5)，准确有
$$
 [w^{rh+l}]P_0(A(w),B(w))
 =\sum_{i=0}^{h}u_0^iL_{i,l+r(h-i)}(P_0).
 \tag{7}
$$
乘以 $p^h$ 后所有系数整，且
$$
 \boxed{\quad
 p^h[w^{rh+l}]P_0(A(w),B(w))
       \equiv\tau^hL_{h,l}(P_0)\pmod p.
 \quad}
 \tag{8}
$$
对 $h=0$，这包括 $[w^l]P_0=L_{0,l}$。
式 (7) 保留了全部其他 $L_{i,l+r(h-i)}$；(8) 只因其共同
$p$ 因子而消去它们，没有假设任何 summand 的前缀。

本篇只取
$$
 1\le l<r,\qquad 0\le h<q_l.
 \tag{9}
$$
由于 $q_l-1\le\lfloor l/2\rfloor$，这些行全部满足
$$
 h<p-1,\qquad
 rh+l\le r\lfloor(r-1)/2\rfloor+r-1<R+1.
 \tag{10}
$$
因此它们都位于真正第一带，原 $w$ 输出与 $v=V(w)$ 在
所需系数上也确实相同；这里没有对单个高中央系数偷换参数。

## 3. 最低 l 块的整逆与逐块整除

用 R179 §6.1 的同一整径向坐标，写
$$
 A=\Gamma^{17}f(\zeta),\qquad
 C=\Gamma^{17}h(\zeta),
 \qquad f(y)=y+O(y^2),\quad h(y)=v_0y^2+O(y^3).
 \tag{11}
$$
在 $V$ 次数小于 $r$ 的范围，范数一角色及实际径向轴给
$$
 \Gamma(U,V)=\mathfrak a(U)+O(V^r),\qquad
 \zeta(U,V)=V\mathfrak b(U)^{-1}+O(V^{r+1}),
 \tag{12}
$$
其中 $\mathfrak a,\mathfrak b\in1+U\mathbb Z_p[[U]]$，
$\mathfrak a'(0)=1$。它们是 R175/R179 的真实整级数。

假设 (2) 中所有低于 $l<r$ 的块系数已在 $p\mathbb Z_p$
中。模 $p$ 时，它们对 $V^l$ 行的所有贡献消失；高于 $l$
的块不能贡献该行。由 (11)–(12)，有准确模 $p$ 恒等式
$$
 \sum_{h\ge0}L_{h,l}(P_0)U^h
 \equiv\mathfrak b(U)^{-l}
    \sum_{m=m_-(l)}^{m_+(l)}
       a_{m,l-m}v_0^{l-m}\mathfrak a(U)^{17m}
       \pmod p.
 \tag{13}
$$
先乘去公共整单位 $\mathfrak b^{-l}$，再用整严格参数
$x=\mathfrak a(U)^{17}-1$，不会改变“前 $q_l$ 个系数全为零”
这个条件。读取 $x^h$、$0\le h<q_l$ 的矩阵为
$$
 \left(\binom{m_-(l)+j}{h}\right)_{0\le h,j<q_l}.
 \tag{14}
$$
其行列式准确为一，证明同 R188 §2。故
$$
 L_{h,l}(P_0)\in p\mathbb Z_p\quad(0\le h<q_l)
 \quad\Longrightarrow\quad
 a_{m,l-m}\in p\mathbb Z_p\quad(m_-(l)\le m\le m_+(l)).
 \tag{15}
$$
此处还使用了 $v_0\in\mathbb Z_p^\times$。

**第一带原源整除定理。** 取
$$
 1\le L<r,\qquad
 K_{D,L}=
 \max_{1\le l\le\min(L,2D)}\{l+r(q_l-1)\}.
 \tag{16}
$$
若同一个完整原多项式满足
$$
 \operatorname{ord}_w P_0(A(w),B(w))>K_{D,L},
 \tag{17}
$$
则
$$
 \boxed{\quad
 c_{i,j}\in p\mathbb Z_p\quad
       (i+j\le D,\ i+2j\le L).
 \quad}
 \tag{18}
$$
特别 $c_{0,0}=0$ 准确成立。

**证明。** (17) 先杀掉原常数项。按 $l=1,\ldots,\min(L,2D)$
归纳。该步所需的全部原行 $rh+l$、$0\le h<q_l$ 都在
(17) 的同一前缀内，故 (8) 给 $L_{h,l}\equiv0$。
低 $l$ 的原系数已由归纳进入 $p\mathbb Z_p$，可以在 (13)
中消去；(15) 遂杀掉当前整块。$\square$

例如 $l=1$ 先给原线性 $A$ 系数为零。$l=2$ 的两列是
$C$ 和 $A^2$，前缀超过 $r+2$ 时同时迫使这两列的原系数
被 $p$ 整除。这一最低例没有额外使用中央失败假设。

(18) 也可以写成一个准确原源包含：
$$
 P_0\in pE_D+
 \sum_{\substack{i+j\le D\\i+2j>L}}
        \mathbb Z_p A^iC^j.
 \tag{19}
$$
但 (19) 中的两个 summand 不因此各自满足 (17)。继续到更高
$p$ 层时必须保留同一个完整新源格与共同前缀。

## 4. 任一 p>8D−1 给出的严格有限消失阶界

设 $D\ge1$，并取任一惰性素数 $p\ne11$ 满足
$$
 p>8D-1,
 \qquad\text{即}\qquad 2D<r.
 \tag{20}
$$
现在可在 (16) 中取 $L=2D$。对 $1\le l\le2D$，
$$
 l+r(q_l-1)=l+r\{\min(l,D)-\lceil l/2\rceil\}.
$$
在 $l\le D$ 时它非减；在 $l>D$ 时每前进两步，其值改变
$2-r\le0$。准确最大值为
$$
 \boxed{\quad
 K_D(p)=r\lfloor D/2\rfloor+2\lceil D/2\rceil.
 \quad}
 \tag{21}
$$
$D$ 为偶数时最大值在 $l=D$ 达到；$D$ 为奇数时在
$l=D+1$ 达到。$D=1$ 时后一项为 $l=2$，仍在范围内。

若 $P_0\in\mathbb Q_p[A,B]_{\le D}$ 非零，先乘同一个
$p$ 幂使其成为原 primitive 整多项式。这不改变沿原曲线的
消失阶。若该消失阶大于 (21)，(18) 使所有原系数都被 $p$
整除，与 primitive 性矛盾。因此
$$
 \boxed{\quad
 \operatorname{ord}_w P_0(A(w),B(w))\le K_D(p)
 \quad\text{对全部非零 }P_0\in\mathbb Q_p[A,B]_{\le D}.
 \quad}
 \tag{22}
$$
特别没有非零多项式在原曲线上恒为零。这里的 primitive
规范只施加于完整 $P_0$；没有将其不同次数块分别规范化。

## 5. 有理矩阵降秩与全局二次界

原 $A(w),B(w)$ 的系数都是有理数。固定整数 $K$ 后，原
有限 jet 映射
$$
 \mathbb Q[A,B]_{\le D}\longrightarrow\mathbb Q[[w]]/(w^{K+1})
 \tag{23}
$$
由一个有理矩阵给出。该矩阵的秩在任何特征零扩标量后
相同。因此若存在非零复系数多项式在原曲线上消失到
$K+1$ 阶，(23) 已有非零有理系数核向量。
对这个有理向量应用 (22)，即可排除 $K=K_D(p)$ 的情形。
所以 (22) 同时对全部 $P_0\in\mathbb C[A,B]_{\le D}$ 成立，
不需要把任意复系数直接嵌入 $\mathbb Q_p$。

现沿用本仓 R158/R159 使用的固定剩余类素数定理。
在 $p\equiv3\pmod4$ 的素数中可为每个充分大的 $D$ 选取
$$
 p_D>8D-1,\qquad p_D=(8+o(1))D.
 \tag{24}
$$
删去固定的 $11$ 不影响该结论。故
$r_D=(p_D+1)/4=(2+o(1))D$，代入 (21) 得到
$$
 \boxed{\quad
 \max_{0\ne P_0\in\mathbb C[A,B]_{\le D}}
       \operatorname{ord}_w P_0(A(w),B(w))
       \le(1+o(1))D^2.
 \quad}
 \tag{25}
$$
这里的 $o(1)$ 只随 $D\to\infty$，与 $P_0$ 无关。
等价地，对每个固定 $\varepsilon>0$，充分大的 $D$ 上所有
原次数不超过 $D$ 的非零多项式均满足
$\operatorname{ord}_w P_0\le(1+\varepsilon)D^2$。

原源的维数为 $M_D=\binom{D+2}{2}$。既然全部非零多项式
在上述行号以内被检测，原真实消失旗标的全部 $M_D$ 个
跳跃都发生于
$$
 0\le k_i\le K_D(p_D)=(1+o(1))D^2.
 \tag{26}
$$
这支付了原实际矩阵所需的最大输出行号。它不是逐行单位性
结论；不同 $p$ 的饱和前缀格及其行列式赋值仍需分别计算。

## 6. 与中央条件和严格预算的关系

本篇只使用真实 CM 首带、原整径向轴和连续节点的整数
binomial 逆。两个完整中央导数均未进入假设。
所以不能把 (18) 或 (25) 再记为中央失败所产生的额外收益。

(25) 可将 R189 后续真实 Schur 比较的行范围统一限制在
$O(D^2)$；它并不证明那些行的单位子式，也不减少 Hasse
运输的真实带号和进位成本。特别，R159 的严格惰性斜率门
仍须由完整前缀范数的有效改进支付。

## 7. 依赖

- [R188：全 D 原源检测及整数 Hasse 运输](R188-original-source-detection-and-integral-hasse-transport.md)。
- [R174：真实 CM Cartan 坐标与首带](R174-actual-cm-formal-cartan-and-common-prefix-matrix.md)。
- [R179：全深度共同 core 及原整径向轴 §6.1](../notes/2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
- [R175：原 Euler 行与完整首带](R175-euler-cartan-and-joint-central-prefix-gain.md)。
- [R158：次数敏感整行与固定剩余类的素数求和](R158-ordinary-saturated-jets-and-degree-sensitive-budget.md)。
- [R159：真实消失旗标的次数敏感斜率](R159-degree-sensitive-direct-slope-boundary.md)。

以上证明对完整原源进行；没有用有限素数样本替代任意次数
的消失阶结论。
