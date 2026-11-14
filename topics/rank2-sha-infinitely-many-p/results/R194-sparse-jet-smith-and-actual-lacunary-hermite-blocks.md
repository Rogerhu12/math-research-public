# R194. 原源稀疏 jet 的完整 Smith 指数与多块缺阶 Hermite 矩阵

日期：2026-11-12。**状态：本文的稀疏 Smith 公式、原次数对角除幂格、
关联 Hermite 矩阵及 $p=23,D=7$ 的精确秩证书均已证明。**
稀疏前缀与完整连续前缀始终分开；本文不由稀疏矩阵的 Smith 指数
断言完整前缀的值理想相等，也没有取得严格的全素数范数预算。

## 1. 同一个实际源与第一带范围

沿用 R188/R191 的原函数与整源
$$
 A=w+O(w^2),\qquad C=B-A=v_0w^2+O(w^3),\qquad v_0=-22,
 \qquad E_D=\mathbb Z_p[A,C]_{\le D}.
 \tag{1}
$$
取惰性素数 $p=4r-1\ge7$，排除 $p=11$，置 $R=r(p-1)$。
$17$ 也自动为单位。原整基记作
$$
 e_{m,c}=A^{m-c}C^c,\qquad 0\le c\le m\le D,
 \qquad l=m+c.
 \tag{2}
$$
它与 $A,B$ 的普通次数基之间是整可逆变换；本文不把其次数换成
底层 $a,b$ 的 $17D$ 次数。

真实 Cartan 坐标与径向轴满足
$$
 U(w)=u_0w^r+O(w^{r+R}),\qquad
 V(w)=w+O(w^{R+1}),\qquad
 \tau=pu_0\bmod p\in\mathbb F_p^\times.
 \tag{3}
$$
若 $\widetilde P=\sum L_{i,j}(P)U^iV^j$，则全部 $L_{i,j}$
是原整源上的整线性行。对 $0\le l<r$ 且 $rh+l<R+1$，
R191 的准确原 $w$ 公式是
$$
 p^h[w^{rh+l}]P
 =\sum_{i=0}^h p^{h-i}(pu_0)^iL_{i,l+r(h-i)}(P)
 \equiv\tau^hL_{h,l}(P)\pmod p.
 \tag{4}
$$
这里保留了同一个 $P$ 的所有 summand。

对 $0\le l\le2D$ 置
$$
 m_-(l)=\lceil l/2\rceil,\quad m_+(l)=\min(l,D),\quad
 q_l=m_+(l)-m_-(l)+1.
 \tag{5}
$$
$l=0$ 时 $q_0=1$，对应唯一常数列。

## 2. $2D<r$ 时的完整稀疏 Smith 公式

现在假设 $2D<r$。选取真正原曲线上的 $M_D=\binom{D+2}{2}$ 个行
$$
 \mathcal S_D=\{(h,l):0\le l\le2D,\ 0\le h<q_l\},
 \qquad k(h,l)=rh+l.
 \tag{6}
$$
这些 $k$ 两两不同。R191 的范围核算保证全部 $k<R+1$，故它们
准确是 (4) 的原 $w$ 行，而不是未经证明换参后的单个高系数。

令 $J_D$ 是行 (6)、列 (2) 的矩阵，元素为
$[w^{k(h,l)}]e_{m,c}$，并令
$$
 J_D^*=\operatorname{diag}(p^h)J_D.
 \tag{7}
$$
**定理 1。** $J_D^*\in\operatorname{GL}_{M_D}(\mathbb Z_p)$。
因此 $J_D$ 的分式 Smith 指数准确为
$$
 \boxed{\quad -h\ \text{出现 }2D-4h+1\text{ 次},\qquad
        0\le h\le\lfloor D/2\rfloor.\quad}
 \tag{8}
$$

**证明。** 按 $l$ 排列行与原列。原列 $e_{m,c}$ 的环境 $V$
消失阶是 $m+c$，所以 $J_D^*\bmod p$ 在这个排列下为块下三角。
对固定 $l$，真实整径向轴给其对角块
$$
 \tau^h[U^h]\left\{
       v_0^{l-m}\mathfrak a(U)^{17m}\mathfrak b(U)^{-l}
                     \right\},\qquad
 0\le h<q_l,\quad m_-(l)\le m\le m_+(l).
 \tag{9}
$$
其中 $\mathfrak a(0)=\mathfrak b(0)=1$、$\mathfrak a'(0)=1$，
且两级数都整。乘去共同单位 $\mathfrak b^{-l}$，再用严格变量
$x=\mathfrak a^{17}-1$，把 (9) 化成连续节点矩阵
$\binom{m}{h}$。该矩阵的行列式为一；严格换参的对角因子是
$17^h$。故对角块的行列式模 $p$ 为
$$
 (17\tau)^{q_l(q_l-1)/2}
       v_0^{\sum_{m=m_-(l)}^{m_+(l)}(l-m)}\ne0.
 \tag{10}
$$
这证明 (7) 整可逆，右乘其整逆便把 $J_D$ 化成
$\operatorname{diag}(p^{-h})$。最后，$h<q_l$ 等价于
$2h\le l\le2D-2h$，给出 (8) 的重数。$\square$

特别
$$
 v_p\det J_D=-H_D,\qquad
 H_D=\sum_{h=0}^{\lfloor D/2\rfloor}h(2D-4h+1)
 =\begin{cases}
 d(d+1)(4d-1)/6,&D=2d,\\
 d(d+1)(4d+5)/6,&D=2d+1.
 \end{cases}
 \tag{11}
$$
所以 $H_D=D^3/12+O(D^2)$。

### 2.1 稀疏前缀与完整连续前缀

把 (6) 按真实 $k$ 排序。只要求较早的**已选稀疏行**为零时，
下一行的值理想准确是 $p^{-h}\mathbb Z_p$：在 (7) 的整源坐标中，
这只是把此前若干坐标置零，当前坐标仍可自由取值。

若要求全部 $[w^j]P=0$、$j<k$，其核还包含未选行的条件，因此只能
直接得到下一行值理想包含于 $p^{-h}\mathbb Z_p$。额外行可以造成
更高赋值或使这一行不再是 jump。式 (8) 不能被当成完整连续前缀
的 Smith 指数。

一个确实属于完整前缀的改良仍可严格读出。若
$k=rh+l<R+1$、$0\le l<\min(r,2h)$，且同一个 $P\in E_D$
满足 $\operatorname{ord}_wP\ge k$，则
$$
             v_p([w^k]P)\ge1-h.
 \tag{12}
$$
当 $l>0$ 时，R191 检测原权不超过 $l$ 的所有块所需的最后行不超过
$l+r\lfloor l/2\rfloor<k$；故这些原系数均被 $p$ 整除。
高原权列不贡献 $L_{h,l}$，所以 $L_{h,l}(P)\in p\mathbb Z_p$，
再用 (4) 即得 (12)。$l=0$ 时原常数项准确为零，结论同样成立。
这个一层收益不需要任何中央失败假设。

## 3. 多个 l 块的同原次数对角除幂格

以下不再要求 $2D<r$。置
$$
 \pi_0=u_0^{-1}\in p\mathbb Z_p^\times,\qquad
 \kappa=\pi_0/p\in\mathbb Z_p^\times,\qquad
 \bar\kappa=\tau^{-1}.
 \tag{13}
$$
在真实输出 $v=V(w)$ 中，$U=u_0v^r+O(v^{pr})$。因而真正第一带
的一个整模型是
$$
 \mathcal T=\mathbb Z_p[U,V]/(U^p,V^r-\pi_0U).
 \tag{14}
$$
它以 $U^hV^j$、$0\le h<p,0\le j<r$ 为整基，且其有理化准确
识别为 $\mathbb Q_p[v]/(v^{pr})$。所以 (14) 不是任意自由替代模型。
在 $rh+j<R+1$ 的行上，(3) 还使它与原 $w$ 单系数准确相同；
越过此界时只使用 $v$ 的第一带模型及真实前缀换参，不宣称高单系数
仍等于原 $w$ 系数。

将每个原列的 $l=m+c$ 唯一写成
$$
 l=j+rt,\qquad 0\le j<r,\qquad t=\lfloor(m+c)/r\rfloor,
 \tag{15}
$$
并定义仍位于同一原次数 $D$ 有理空间中的格
$$
 \boxed{\quad
 \mathcal M_D=
 \bigoplus_{0\le c\le m\le D}
      \mathbb Z_p\,p^{-\lfloor(m+c)/r\rfloor}e_{m,c}.
 \quad}
 \tag{16}
$$
这是对原列的明确除幂，不是额外加入任意环境列。其与 $E_D$ 的
指数为
$\operatorname{length}(\mathcal M_D/E_D)=\sum_{m,c}\lfloor(m+c)/r\rfloor$。

**命题 2。** (16) 的实际像落在 $\mathcal T$ 中；约化模 $p$ 后，
按 $j$ 的递减过滤，它对关联次数 $j$ 的对角列准确为
$$
 \kappa^t v_0^c\,
 U^t\mathfrak a(U)^{17m}\mathfrak b(U)^{-j-rt}V^j
      \pmod{p,U^p}.
 \tag{17}
$$
若 $t\ge p$，这一列的整个模 $p$ 像为零。

**证明。** 同一整 flowbox 中，$e_{m,c}$ 的 $V$ 阶恰为 $l$，
所以可写成 $V^l$ 乘整单位。将 $V^r=\pi_0U$ 代入后，
$p^{-t}V^l=\kappa^tU^tV^j$，证明整性。更高 $V$ 次数若回到
较小的余类，必额外跨过一次 $V^r$，因而多出一个 $p$ 因子。
故模 $p$ 的像只向不小于 $j$ 的余类传播。

在相同余类 $j$ 上，额外跨过 $r$ 的项也被 $p$ 消去；只剩原列
的最低 $V^l$ 系数。真实径向轴给该系数准确为
$v_0^c\mathfrak a^{17m}\mathfrak b^{-l}$，即 (17)。
$U^p=0$ 处理最后一句。$\square$

## 4. 关联对角块的准确缺阶 Hermite 形式

在 (17) 中先乘去共同整单位 $\mathfrak b^{-j}$。
置 $\eta=\log\mathfrak a(U)$。在次数小于 $p$ 的截断里，所有
对数及指数阶乘分母都是 $p$ 单位，$\eta=U+O(U^p)$ 是合法严格
换参。R175 的真实径向式
$$
 U=u(\eta)=\sum_{n\equiv1\ (p-1)}\frac{\eta^n}{n!},\qquad
 \mathfrak b(U)=u'(\eta)
 \tag{18}
$$
还给
$$
 U\mathfrak b(U)^{-r}\equiv\eta\pmod{p,U^p}.
 \tag{19}
$$
于是 (17)，除去明确的列单位 $\bar\kappa^t v_0^c$ 后，准确变为
$$
                \eta^t e^{17m\eta}\pmod{\eta^p}.
 \tag{20}
$$
因此固定余类 $j$ 的矩阵是
$$
 \mathcal H_{j,D}(h;(m,t))=
 \begin{cases}
 (17m)^{h-t}/(h-t)!,&h\ge t,\\
 0,&h<t,
 \end{cases}
 \quad 0\le h<p,
 \tag{21}
$$
而允许的列恰为
$$
 0\le m\le D,\qquad
 \max\!\left(0,\left\lceil\frac{m-j}{r}\right\rceil\right)
 \le t\le\left\lfloor\frac{2m-j}{r}\right\rfloor,
 \qquad t<p.
 \tag{22}
$$
这是 $c=j+rt-m\in[0,m]$ 的等价写法。

可以再取严格变量 $\xi=17\eta$，并分别乘列单位 $17^t$，
得到 $\xi^t e^{m\xi}$。将 Taylor 行改为导数行只乘 $h!$；
$h<p$ 时这也是整单位操作。本文没有支付或使用任何 $p!$ 逆元。

式 (22) 的 $t$ 往往从正数开始。因此这是具有缺阶的 Hermite
矩阵，不是每个节点都从导数阶零开始的完整合流 Vandermonde。
即使 $D<p$、全部节点 $17m$ 两两不同模 $p$，其指定前几行的
行列式也不自动为单位。

## 5. 合法实际块：$p=23,D=7$ 的第一处秩损失及恢复

取 $p=23,r=6,D=7,j=3$。式 (22) 给出的全部列正好是
$$
 (m,t)=(2,0),(3,0),(5,1),(6,1),(7,1).
 \tag{23}
$$
它们来自原列
$$
 AC,\ A^3,\ p^{-1}AC^4,\ p^{-1}A^3C^3,\ p^{-1}A^5C^2,
 \tag{24}
$$
每列的原总次数都不超过七。去掉第 4 节已经逐项支付的单位后，
列为 $e^{2\xi},e^{3\xi},\xi e^{5\xi},\xi e^{6\xi},\xi e^{7\xi}$。
其前六个 Taylor 行的有理代表为
$$
 M=\begin{pmatrix}
 1&1&0&0&0\\
 2&3&1&1&1\\
 2&9/2&5&6&7\\
 4/3&9/2&25/2&18&49/2\\
 2/3&27/8&125/6&36&343/6\\
 4/15&81/40&625/24&54&2401/24
 \end{pmatrix}.
 \tag{25}
$$
准确计算给
$$
 \det M_{0,1,2,3,4}=\frac{161}{24}=\frac{7\cdot23}{24},\qquad
 \det M_{0,1,2,3,5}=\frac{3083}{90}\in\mathbb Z_{23}^\times.
 \tag{26}
$$
前五行模 $23$ 的秩是四，前六行模 $23$ 的秩是五。前五行的
一个核向量是 $(5,18,7,20,1)$；第六行不杀它。

这个额外行列式因子也可直接解释。先按前两列消去第一阶条件，
得到的缺阶因子包含
$$
 \int_0^1(3-t)(4-t)(5-t)\,dt=\frac{161}{4}.
 \tag{27}
$$
本例 (26) 的第一行列式恰为 (27) 的 $1/6$。若先将 $3$ 模
$23$ 写成 $1/8$，同一积分的有理代表是 $-115/512$；它与
$161/4$ 模 $23$ 相等，但不是同一个有理数。

这里涉及的真实输出阶依次为 $3,9,15,21,27,33$，均严格小于
$R+1=133$。因此没有用原 $w$ 与 $v$ 高阶差异制造这个反例。
已支付的行变换在每个有限前缀上整可逆，故上述模 $23$ 秩损失
及下一行恢复确实属于 (16) 的实际关联对角块。

这只否定“把所有 (22) 的前若干行免费视为单位合流矩阵”的步骤。
它不声称整个原源在完整前缀中有同样的秩损失：其他余类和后续
实际行仍可能补足条件。也不由 (26) 的有理代表断言实际块的
高于模 $23$ 的全部 Smith 指数。

## 6. 可复跑证书与后续范围

[精确短脚本](../scripts/check-sparse-jet-lacunary-block.py) 只用有理数和
有限域消元，核对 (25)–(27)、合法原列、两个秩、核向量，以及 (8)
的重数和 (11) 的有限整数恒等式；它不扩大素数数值列表。

后续完整 Schur 消元的输入已经是同一原次数空间中的明确格 (16)
及矩阵 (21)–(22)。若继续提高 $p$ 精度，必须把完整源系数和
所有已付前缀行一起保留；不能把 (16) 的不同除幂块各自置入前缀核。

本篇依赖：

- [R174：真实有限 Cartan 作用与坐标](R174-actual-cm-formal-cartan-and-common-prefix-matrix.md)。
- [R175：真实径向轴和中央第一带](../notes/2026-11-12-euler-cartan-rows-and-joint-central-prefix-gain.md)。
- [R179：同一原源的全带 flowbox](../notes/2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
- [R188：全原次数的环境检测和 Hasse 运输](R188-original-source-detection-and-integral-hasse-transport.md)。
- [R191：原第一带整块整除](R191-first-band-source-divisibility-and-global-multiplicity.md)。
