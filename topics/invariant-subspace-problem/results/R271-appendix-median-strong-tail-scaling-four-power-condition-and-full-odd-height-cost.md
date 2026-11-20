# R271 补录：原强尾的中位尺度归一化、$4^R$ 条件数与完整奇高度费用


状态：**已证明**。作者：Astra-ISP-b2a9acde-20261120 / r271_cost，与root；AI-assisted GPT-6 Astra Pro。日期：2026-11-20 UTC。

## 0. 结论范围

本条对原强权 $b_i=(i+1)^{-2}$ 给出精确公共尺度消去。
完整 Boolean 强尾的物理相似条件数可由旧
$\prod b_i^{-1}$ 改为至多 $4^R$，同时把公共尺度准确移到有限头及 $r$ 次幂。
相同归一化也适用于保持孔级的 primitive 代数投影。

随后把它代入已证的最高 carry 奇高度完整 MP 剪切界，得到
$O(R)+(d+r)\log(m+R)$ 的强段对数费用。
本条不证明 Galerkin 源的高阶常数，也不闭合普通 Hilbert ISP。

## 1. 原强尾的精确中位尺度

取整数 $m\ge1$、偶 $R=2q\ge0$，令
$$
x=m+R,\qquad y=m+q,\qquad c=y^{-2}.
$$
强尾为
$$
D_R=\sum_{i=m}^{m+R-1}b_iE_i,\qquad b_i=(i+1)^{-2}.
$$
在完整 Boolean 基中定义
$$
\widetilde T e_I
=\prod_{i\in I}\frac{b_i}{c}\,e_I.
\tag{1.1}
$$
则
$$
D_R=\widetilde T^{-1}(cD_{\rm unw})\widetilde T.
\tag{1.2}
$$

### 定理 1.1

其完整物理条件数恰为
$$
\boxed{
\kappa(\widetilde T)
=\left(\frac{(m+R)!\,m!}{(m+R/2)!^2}\right)^2
\le\binom{R}{R/2}^2\le4^R.
}
\tag{1.3}
$$

**证明。** 写 $j=i+1$，则 $b_i/c=(y/j)^2$。
前 $q$ 个比值至少为 $1$，后 $q$ 个至多为 $1$。
所以最大对角项取前一半所有位，最小对角项取后一半所有位。
它们的比恰为
$$
\frac{y^{2q}/\prod_{j=m+1}^{m+q}j^2}
{y^{2q}/\prod_{j=m+q+1}^{m+2q}j^2}
=\left(\frac{(m+2q)!\,m!}{(m+q)!^2}\right)^2.
$$
并且
$$
\frac{(m+2q)!\,m!}{(m+q)!^2}
=\prod_{j=1}^q\frac{m+q+j}{m+j}
\le\prod_{j=1}^q\frac{q+j}{j}
=\binom{2q}{q}\le2^{2q}.
$$
平方即得 (1.3)。$R=0$ 时均为 $1$。证毕。

这是真实整个强尾的对角条件数，不是低孔压缩的条件数。

## 2. 相同 primitive 投影的公共权因子精确抵消

原未归一化相似为
$$
T e_I=\prod_{i\in I}b_i\,e_I,
\qquad D_R=T^{-1}D_{\rm unw}T.
$$
若 $P$ 是未加权空间中保持尾孔数的任意物理正交投影，
例如完整 Lefschetz 分解中按 primitive 起始孔级选出的投影，
则原代数投影
$$
Q=T^{-1}PT
$$
满足
$$
\boxed{
Q=\widetilde T^{-1}P\widetilde T,\qquad
\|Q\|\le4^R.
}
\tag{2.1}
$$
同样 $\|I-Q\|\le4^R$。

事实上 $\widetilde T=c^{-\mathcal N}T$，且 $P$ 与尾孔数 $\mathcal N$
交换，所以两种还原得到严格相同的 $Q$。
这里没有把 $Q$ 称为原物理正交投影；其非正交范数由 (2.1) 支付。
该恒等式解释了公共强权尺度为什么不应在每一个 primitive 投影上重复支付。

## 3. 有限头也必须使用同一个公共尺度

令 $J_h$ 为单位后移 Jordan 链，
$L_he_j=\sqrt{j(h-j)}e_{j-1}$ 为标准 sl2 降算子。
定义对角矩阵
$$
Q_he_j=c^j\sqrt{\frac{j!(h-1)!}{(h-1-j)!}}\,e_j.
$$
直接逐项核对得
$$
J_h=Q_h(cL_h)Q_h^{-1}.
\tag{3.1}
$$
若 $ch/2\le1$，这些对角项单调不增，所以
$$
\boxed{\kappa(Q_h)=\frac{c^{-(h-1)}}{(h-1)!}.}
\tag{3.2}
$$
因此公共尺度不能只从强尾删去；它在有限头的成本正是 (3.2)。

标准 unitary sl2 张量和的每条链长度为 $L$ 时，
$r$ 次幂的非零奇值为
$$
c^r\sqrt{(j)_r(L-j)^{\overline r}}\ge c^r r!.
\tag{3.3}
$$
这保留全部 primitive 链，不要求选定某个可达子块。

## 4. 原最高 carry 的完整物理 MP 改进

沿用已证
[奇高度最高 carry 完整 MP](R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md)
及
[显式 $883$ 预算](R271-appendix-odd-height-highest-carry-explicit-883-cost-and-d-sized-budget.md)
的原记号。
取
$$
m\ge4,\quad n=2^{m-1},\quad d=2n,\quad
a=16^{m-2},\quad b=b_{m-1}=m^{-2}.
$$
旧头为 $A_{m-1}$，最高参数
$t=d_{m-1}/d_{m-2}^2$，删除最高 Boolean 项后的 $t=1$
参考头为 $\widehat A(1)$。
已证明的完整头条件数为
$$
\kappa(V_{\rm old})\le e^{221a},\qquad
\kappa(\widehat V)\le e^{441a}.
\tag{4.1}
$$
这两条保留真实权位置，并同时适用于原 N、Y 两族。

现在取偶 $R\ge d$，仍用
$y=m+R/2,\ c=y^{-2}$。
对 $h\le d$，有 $ch/2\le d/(2y^2)\le2/d<1$，
所以 (3.2) 适用。
由 (1.3)、(3.1)–(3.3)，对完整
$D=A_{m-1}+D_R$ 得
$$
\|(D^r)^\dagger\|
\le e^{221a}4^R\,
\frac{y^{2(n+r-1)}}{(n-1)!\,r!},
\tag{4.2}
$$
参考完整头得
$$
\|((\widehat A(1)+D_R)^r)^\dagger\|
\le e^{441a}4^R\,
\frac{y^{2(d+r-1)}}{(d-1)!\,r!}.
\tag{4.3}
$$
以上仍是原物理 MP：通过有界可逆相似构造完整真解，再用最小范数性得到。

对奇 $r$，完整最高 carry 剪切界为
$$
\|(C_t^r)^\dagger\|
\le t^{-1}(1+rbM_r)^2
\|((\widehat A(1)+D_R)^r)^\dagger\|,
\tag{4.4}
$$
其中 $M_r=\|D^{r-1}\|\|(D^r)^\dagger\|$，且 $\|D\|<8$。

若 $1\le r\le x=m+R$，(4.2) 的右侧至少为 $1$：
因为 $n\le y,\ x\le2y,\ y\ge2$，
$$
(n-1)!\le y^{n-1},\qquad r!\le(2y)^r\le y^{2r}.
$$
于是将 (4.2) 代入 $M_r$，用
$1+rbM_r\le(1+rb)8^{r-1}\times\text{(4.2 右侧)}$，
再用 (4.3) 得：

### 定理 4.1

对 $m\ge4$、偶 $R\ge d$、奇 $1\le r\le x=m+R$、$0<t\le1$，
$$
\boxed{
\|(C_t^r)^\dagger\|
\le
\frac{
e^{883a}\,64^R\,
(1+rb)^2\,8^{2r-2}\,
y^{4d+6r-6}
}{
t\,((n-1)!)^2(d-1)!(r!)^3
}.
}
\tag{4.5}
$$
同界适用于 $((C_t^*)^r)^\dagger$。

三个 $4^R$ 分别来自两次旧头剪切和一次参考完整 MP；
三个公共尺度也都已移入 $y$ 的幂与阶乘。
没有把整个强头相似或非正交成本省去。

## 5. 可以带出的预算及未闭项

(4.5) 除最高 $t^{-1}$ 外的对数，显式不超过
$$
883a+6R\log2
+(4d+6r-6)\log y
+2\log(1+rb)+(2r-2)\log8,
\tag{5.1}
$$
因为阶乘只降低右端。
因此强段成本为
$O(R)+(d+r)\log(m+R)$，
不必按旧公共权乘积支付 $O(R\log(m+R))$。

这允许重新评估更大的多项式强段；
母窗 $Q$ 仍须逐一满足原支持与 carry 条件。
本条没有证明 Galerkin 的高阶源系数只需付一次 $4^R$，
也没有给出其随 $R,m,r$ 的统一界。
在高 primitive 的源比较中，(2.1) 可立即使用；
其他依赖核框架、Gram 逆或残余系数的常数仍必须单独核清。
