# R600 — 原 S/T 的全余类中央块、完整次数与真实前缀 Vandermonde

日期：2026-11-14。**状态：已证明。**

本篇在 R596 的同一原评价矩阵中，求出全部原 $S^aT^b$ 在首 $p^2$ 窗口的准确第一层。中央余类和其余 $s-1$ 个余类的正规化相差一阶 $p$；前者准确读取原低卷积 $[w^s]S^aT^b$，后者读取 $[w^r]S^aT^b$。公式对所有来源次数成立，不要求 $a+b<s$，并保留总 Gaussian 权在模 $p$ 下为零及不同列权碰撞。

中央 Euler 观察保留 R598 的真实单位根平均与因子 $p+1$。它的第一层是一个不除以总权的整多项式。最后将这些行限制到原真前缀，说明何时有一阶额外整性，也明确核对了低次数格中该区间可能已经没有非零前缀。本篇不由有限矩阵秩推出 cutoff，不由两原中央零推出任意乘积中央零。

## 1. 两条原来源与完整评价格

取
$$
p=6s-1>71,\qquad b=17,\qquad w=z^6,\qquad d=p+1=6s.
\tag{1}
$$
也可经 R303/R402 已付的共同单位缩放使用 $b=1$。保持 R596 的两条固定来源 $S_b,T_b$，首项都为 $w$。为免将单项式指数与底曲线参数混淆，下文写
$$
P_{\mu,\nu}=S_b^\mu T_b^\nu,\qquad
q=\mu+\nu\ge1,\qquad m_{\mu,\nu}=34\mu+72\nu .
\tag{2}
$$
令
$$
c=[z^d]\log(\sigma/z),\qquad
\zeta_p=pc\in\mathcal O^\times,\qquad
\gamma_{\mu,\nu}=\overline{m_{\mu,\nu}\zeta_p}\in k .
\tag{3}
$$
这里只说两个**单因子**的 $34\zeta_p,72\zeta_p$ 为单位；合成的 $\gamma_{\mu,\nu}$ 可以为零。

原完整分解是
$$
S_b=w e^{34c w^s}G_S(w),\qquad
T_b=w e^{72c w^s}G_T(w),\qquad G_S(0)=G_T(0)=1 .
\tag{4}
$$
R586、R589 与 R596 §6.1 已在同一规范支付：对 $X=S_b,T_b$、$0<k<ps$，写
$$
k=Ls+u,\quad 1\le u\le s,\qquad a_S=34\zeta_p,\ a_T=72\zeta_p.
$$
则
$$
p^L[w^k]X\in\mathcal O,\qquad
\boxed{\;
\overline{p^L[w^k]X}
=\frac{\bar a_X^L}{L!}\overline{[w^u]X}.
\;}
\tag{5}
$$
在这个范围 $L<p$，显示阶乘均为单位。$u=s$ 的低行也是整的原对角；没有将它换成一个自由 Gaussian 系数。

定义原二来源格和真实行
$$
E_{D,2}=\bigoplus_{\mu+\nu\le D}\mathcal O\,P_{\mu,\nu},
\qquad r_n(F)=[w^n]F.
\tag{6}
$$
常数列 $P_{0,0}=1$ 单独保留。此格是 R596 原九来源格的实际子格，未添加投影后的新来源列。

## 2. 全部次数的中央与非中央首层

令
$$
C_{\mu,\nu}=\overline{[w^s]P_{\mu,\nu}},\qquad
B_{\mu,\nu,r}=\overline{[w^r]P_{\mu,\nu}}
\quad(1\le r<s).
\tag{7}
$$
这些都是**整个原乘积**的低阶 Cauchy 卷积，在当前范围整。若 $q>s$，则 $C_{\mu,\nu}=0$；若 $q>r$，则 $B_{\mu,\nu,r}=0$。

**定理 1。** 对任意 $D$、任意非恒原单项式 (2)，有：
$$
\boxed{
p^{h-1}(h-1)!\,[w^{hs}]P_{\mu,\nu}
\equiv\gamma_{\mu,\nu}^{\,h-1}C_{\mu,\nu}\pmod p,
\qquad 1\le h<p ,
}
\tag{8}
$$
以及
$$
\boxed{
p^h h!\,[w^{hs+r}]P_{\mu,\nu}
\equiv\gamma_{\mu,\nu}^{\,h}B_{\mu,\nu,r}\pmod p,
\quad 1\le r<s,\quad 0\le h<p .
}
\tag{9}
$$
每个左边本身整；$0^0=1$。当 $\gamma_{\mu,\nu}=0$，(8) 仍在 $h=1$ 读取 $C_{\mu,\nu}$，其余 $h$ 的右边为零；(9) 在 $h=0$ 保留原低行，其余右边为零。

**证明。** 把 $P=X_1\cdots X_q$ 按真实有序因子展开，不合并掉重复标签的整数重数。每个非零 Cauchy 项都有
$$
k_i=L_i s+u_i,\qquad 1\le u_i\le s.
\tag{10}
$$

若 $\sum k_i=hs$，则 $\sum u_i=C s$，其中 $C\ge1$，故
$$
\sum L_i=h-C\le h-1.
$$
乘 $p^{h-1}$ 后，只有 $C=1$ 可以在模 $p$ 留下首层；所有 $C\ge2$ 的项都多含至少一阶 $p$。对 $C=1$，先固定 $\sum u_i=s$，再由 (5) 对 $\sum L_i=h-1$ 求和，得到
$$
(h-1)!\!
\sum_{\substack{L_i\ge0\\\sum L_i=h-1}}
 \prod_i\frac{\bar a_{X_i}^{L_i}}{L_i!}
=\left(\sum_i\bar a_{X_i}\right)^{h-1}
=\gamma_{\mu,\nu}^{h-1}.
\tag{11}
$$
余下 $\sum u_i=s$ 的完整低卷积正是 $C_{\mu,\nu}$。若 $q>s$，这组正整数分拆为空，故两边都为零；没有用到 $q<s$。

若 $\sum k_i=hs+r$、$1\le r<s$，则
$$
\sum u_i=C s+r,\qquad C\ge0,\qquad
\sum L_i=h-C\le h.
$$
乘 $p^h$ 后只有 $C=0$ 留下；用同一个多项式定理对 $\sum L_i=h$ 求和，余下 $\sum u_i=r$ 的实际卷积正是 $B_{\mu,\nu,r}$。$q>r$ 时分拆为空。所有成本严格较低的项确有额外 $p$，而 (5) 的每个误差也有额外 $p$。这证明全部 $D$ 的 (8)–(9)。$\square$

特别，纯 $S/T$ 子格的统一原行界为
$$
v_p r_{hs}(F)\ge1-h\quad(h\ge1),\qquad
v_p r_{hs+r}(F)\ge-h\quad(1\le r<s).
\tag{12}
$$
中央行比直接使用 R596 九来源通用缩放 $p^h$ 保留了一阶更精确的第一 Bockstein。没有将短 Euler 分母所在的其余七列删掉；(12) 只对 (6) 陈述。

## 3. 同一有限目标中的完整低块

在 R589 的真实目标
$$
\mathcal A_p=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^p)
\tag{13}
$$
中，(12) 保证全部原 $P_{\mu,\nu}$ 的像整。令
$$
e_\gamma(\epsilon)=\sum_{h=0}^{p-1}\frac{\gamma^h}{h!}\epsilon^h,
\qquad
B_{\mu,\nu}(w)=\sum_{r=1}^{s-1}B_{\mu,\nu,r}w^r .
\tag{14}
$$
由 (9)，其完整模 $p$ 像准确是
$$
\boxed{
\overline{\operatorname{ev}_p(P_{\mu,\nu})}
=e_{\gamma_{\mu,\nu}}(\epsilon)B_{\mu,\nu}(w)
\quad\text{于 }k[w,\epsilon]/(w^s,\epsilon^p).
}
\tag{15}
$$
常数列仍映到 $1$。

令 $\operatorname{pr}_0$ 仅选择 (13) 标准基中 $w$ 次数为零的部分。它是线性投影，不是环同态。由 (8)，
$$
\operatorname{pr}_0\operatorname{ev}_p(P_{\mu,\nu})
\in p\mathcal O[\epsilon]/(\epsilon^p),
$$
且其第一 Bockstein 完整为
$$
\boxed{
\overline{p^{-1}\operatorname{pr}_0
 \operatorname{ev}_p(P_{\mu,\nu})}
=C_{\mu,\nu}\,\epsilon e_{\gamma_{\mu,\nu}}(\epsilon)
\pmod{\epsilon^p}.
}
\tag{16}
$$
这保留了从原低乘积系数 $[w^s]P$ 到所有 $hs$ 行的准确次数和阶乘。式 (16) 不是从 (15) 的中央零直接读出；右边多用了一阶实际精度。

## 4. 与原中央 Euler 观察的准确接合

本节保持 R598 的真实 $d$ 次单位根平均
$$
\Pi_0f(z)=\frac1d\sum_{\xi^d=1}f(\xi z),\qquad X=z^d=w^s .
\tag{17}
$$
对每个非恒原单项式定义零初值的固定原函数
$$
U_{\mu,\nu}(z)=\int_0^zP_{\mu,\nu}(t)\,\frac{dt}{t}.
\tag{18}
$$
其来源不依赖 $p$；下面的 $\Pi_0$ 依赖 $p$，不能自由加入原列格。令
$$
H_{\mu,\nu}(X)
=d\,e^{-m_{\mu,\nu}cX}\Pi_0U_{\mu,\nu}.
\tag{19}
$$
因 $d=6s$，若 $A_h=[w^{hs}]P_{\mu,\nu}$，则准确有
$$
d\Pi_0U_{\mu,\nu}=\sum_{h\ge1}\frac{A_h}{h}X^h.
\tag{20}
$$
这里的 $d$ 因子已经消去原积分中的 $6hs$，不能省略。

定义不除以 $\gamma$ 的整多项式
$$
\boxed{
\Phi_\gamma(\epsilon)=
\sum_{h=1}^{p-1}\frac{(-1)^{h-1}\gamma^{h-1}}{h!}\epsilon^h .
}
\tag{21}
$$
若 $\gamma\ne0$，它可写成 $(1-e^{-\gamma\epsilon})/\gamma\bmod\epsilon^p$；若 $\gamma=0$，则准确为 $\epsilon$。

**推论 2。** 对全部 (2)，
$$
\boxed{
H_{\mu,\nu}(p\epsilon)/p\in
\mathcal O[\epsilon]/(\epsilon^p),\qquad
\overline{H_{\mu,\nu}(p\epsilon)/p}
=C_{\mu,\nu}\Phi_{\gamma_{\mu,\nu}}(\epsilon).
}
\tag{22}
$$
证明为将 (8) 代入 (20)，再乘
$e^{-m_{\mu,\nu}\zeta_p\epsilon}$。到次数 $p-1$ 的所有阶乘为单位，准确有限乘积给 (21)，包括 $\gamma=0$。

对两条原线性来源，R409/R598 的完整规范给
$$
j_S=0\Longrightarrow C_{1,0}=0,\qquad
j_T=0\Longrightarrow C_{0,1}=0,
\tag{23}
$$
故其 (22) 的第一层均为零。R598 支付的更强结论是：这两条**完整** $j$ 为零，等价于各自中央 $H$ 的实际大盘延拓。本篇没有把有限的 (22) 反推为完整 $j=0$。

此外，(23) 不决定 $C_{\mu,\nu}$，因为它是原 $S^\mu T^\nu$ 的整个低卷积。这里没有任何逐乘积的算术中央零假设，也没有把 $\Pi_0(PQ)$ 改成 $(\Pi_0P)(\Pi_0Q)$。

## 5. 真前缀上的分组 Vandermonde

定义同一个原饱和前缀
$$
K_{D,n}=E_{D,2}\cap
 \ker(r_0,\ldots,r_{n-1}).
\tag{24}
$$
它用特征零的完整所有行，包括所有非中央余类。以下先从 $F\in K_{D,n}$ 出发，再约化；不从某个模 $p$ 核反向假设存在提升。

写 $F=\sum c_{\mu,\nu}P_{\mu,\nu}$。对固定 $1\le r<s$，按实际不同的 $\gamma\in k$ 分组：
$$
L_{\gamma,r}(F)
=\sum_{\gamma_{\mu,\nu}=\gamma}
 \bar c_{\mu,\nu}B_{\mu,\nu,r}.
\tag{25}
$$
对中央行则定义
$$
L_{\gamma,0}(F)
=\sum_{\gamma_{\mu,\nu}=\gamma}
 \bar c_{\mu,\nu}C_{\mu,\nu}.
\tag{26}
$$
只保该原行实际出现的非零列系数，分别记所涉及的不同 $\gamma$ 集合为 $\Gamma_{D,r}$、基数为 $t_{D,r}$。也可使用包括零列的较大集合，结论只会变弱。$\gamma=0$ 如出现，必须是集合中的一列。

式 (8)–(9) 对原系数线性延伸为
$$
\overline{p^h h!\,r_{hs+r}(F)}
=\sum_{\gamma\in\Gamma_{D,r}}\gamma^hL_{\gamma,r}(F),
\tag{27}
$$
$$
\overline{p^{h-1}(h-1)!\,r_{hs}(F)}
=\sum_{\gamma\in\Gamma_{D,0}}\gamma^{h-1}L_{\gamma,0}(F).
\tag{28}
$$

**推论 3。**

- 若 $1\le r<s$、$h<p$、$h\ge t_{D,r}$，则在真实 $K_{D,hs+r}$ 上，
  $$
  r_{hs+r}(K_{D,hs+r})\subset p^{1-h}\mathcal O.
  \tag{29}
  $$
- 若 $1\le h<p$、$h-1\ge t_{D,0}$，则在真实 $K_{D,hs}$ 上，
  $$
  r_{hs}(K_{D,hs})\subset p^{2-h}\mathcal O.
  \tag{30}
  $$

确实，前一种情形的真实前缀已使同余类的 $0,\ldots,h-1$ 阶行恰为零。取其中前 $t_{D,r}$ 行，(27) 的系数矩阵是不同 $\gamma$ 的 Vandermonde，其行列式
$$
\prod_{\gamma<\gamma'}(\gamma'-\gamma)\ne0
\tag{31}
$$
是域中非零数；这里任意固定排序即可。于是所有 $L_{\gamma,r}$ 为零，再代入当前行得到 (29)。中央情形用前 $h-1$ 个中央行，指数依次为 $0,\ldots,h-2$，同理得 (30)。$t=0$ 时无需行列式，右侧首层本来为零。

这些不是将同权的原列合并成一个自由来源，而只是对其**实际首层观测**分组。对任意 $D$ 都必须按模 $p$ 的实际 $\gamma$ 分组。只有另加明确条件 $p>72D$ 时，模 $p$ 的权碰撞才等价于整数
$34\mu+72\nu$ 相同；即便如此，整数同权列仍不能分开当独立 Vandermonde 列。

## 6. 增益区间与原列格的具体检查

推论 3 没有断言该处 $K_{D,n}$ 非零。这个区别在最小原格上已能明确核出。

由 R403 的原首部，
$$
S_b=w-\frac{988b}{105}w^2+\cdots,\qquad
T_b=w-\frac{2938b}{35}w^2+\cdots,
$$
所以
$$
[w^2](T_b-S_b)=-\frac{1118b}{15}\ne0.
\tag{32}
$$
于是对 $E_{1,2}=\mathcal O\langle1,S_b,T_b\rangle$，
$$
K_{1,1}=\mathcal O\langle S_b,T_b\rangle,\quad
K_{1,2}=\mathcal O(T_b-S_b),\quad
\boxed{K_{1,3}=0.}
\tag{33}
$$
特别，$n\ge s$ 的中央及后续 Vandermonde 返回在这个格上已经是空前缀，不能被记为一项新的高阶饱和成本节约。

对一般 $D$，(29)–(30) 是同一个真正 $K_{D,n}$ 上的有效行界；本篇未证明其非空层统一达到某个长度，也没有证明由此得到逐 $D$ 的惰性 cutoff。若要接 R581/R584 的完整旗标，仍须在原全部行中支付该非空层和后续 Bockstein。

同样，若使用 R596 的九来源格，本篇只能应用于其实际 $S/T$ 子格或已付落入该子格的向量。含七个原 Euler 坐标的列继续服从 R596 的完整 Cauchy 矩阵；不能仅按 (27) 忽略它们的短分母、首极部和进位。

## 7. 与已有结果的范围及精确证书

R403 §5–6 支付的是两条真实来源的共同三块、第二顶行以及原有限矩阵的第二精度比较；R404 §6–7 支付真实十二输入 mixed 来源的完整二维 Gaussian 和二维 Newton；R409 支付两条指定首对角的固定递推。本篇新增的是所有原 $S^\mu T^\nu$、全部来源次数、全部余类在首 $p^2$ 窗口的 (8)–(16)，以及保留真实前缀和 $\gamma=0$ 的 (22)、(29)–(30)。没有重赋 R404 的 mixed 单项中央零。

证书 [check-r600-central-residue-blocks.mjs](../scripts/check-r600-central-residue-blocks.mjs) 只使用此前已有的解析纤维 $p=23$，分别保 $b=1,17$。它从原 Weierstrass 和 sigma 有理递推直接构造 $S,T$，对总次数至六、物理行 $1\le n\le15$ 核对中央、非中央以及完整因子 $d$ 下的 Euler 行。该范围包含 $q>s$、实际总权零的 $ST^4$ 和实际权碰撞；另逐一核有限域全部 $\gamma$ 的整式 (21)、含零权的 Vandermonde，以及 (32) 的特征零行列式。共 1482 项精确检查。一般全次数和全首 $p^2$ 窗口由定理 1 的实际 Cauchy 证明支付，不由这些有限检查外推。

本篇留下的实际对象仍是原全前缀中的 Bockstein 和 R598 的完整中央投影。两条原中央零没有在本篇被提升为所有来源零、完整全函数延拓或指定 forcing 非零；原无穷素数目标仍需这些真实接口之间的进一步关系。
