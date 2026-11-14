# R581 — 九个真实坐标的截断分母成本与大惰性素位强制非整

日期：2026-11-14。**状态：已证明。**

R574 的短积分分母全素位成本是三，但若某个论证真正把大于
$X$ 的惰性素位全部变成整位，则短分母也只应在 $p\le X$
求和。本文对同一个真实九坐标格证明这个截断成本为
$O(DX+k)$，并在完整饱和旗标上累计，付清每个早期跳跃和全部
真实高接触阶。由此将 R574/R579 中保守的条件阈值
$\vartheta<6$ 改进为 $\vartheta<7$。

更直接的无条件结论是：对每个固定 $C>0$ 和
$0\le\vartheta<7$，每个充分大的次数 $D$ 都有一个好惰性素数
$p>CD^\vartheta$，以及同一个九坐标格的某个非零饱和 jet，
其真实算子范数严格大于一。这里不构造具体素数或具体多项式，
不把这个非整结论认作原中央导数或 $\Sha$ 的结论。

## 1. 整个原九坐标及同一源格

保持 [R575](R575-fixed-primitive-towers-and-complete-ordinary-dirac-defects.md)、
[R574](R574-nine-coordinate-inert-envelope-and-primitive-denominator-cost.md)、
[R579](R579-nine-coordinate-ordinary-divided-difference-and-saturated-jet-budget.md)
的真实坐标
$$
\mathbf G=(S,T,V_{4,1},V_{4,2},V_{1,1},\ldots,V_{1,5}),\qquad w=z^6,
$$
其中 $V_{4,r}=z^{2-r}U_{4,r}$、
$V_{1,r}=z^{5-r}U_{1,r}$。它们有有理系数、原点至少一阶零，
在整个 $w$ 平面有限型增长阶至多 $1/3$，且全部九者代数独立。

对所有整数 $D\ge1$，使用同一个原单项式格和全部前缀：
$$
E_D=\bigoplus_{|\mathbf a|\le D}\mathbf Z\mathbf X^{\mathbf a},
\quad N_D=\binom{D+9}{9},\quad
r_k(P)=[w^k]P(\mathbf G(w)),
$$
$$
K_{D,k}=\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_D,
\qquad \varphi_D^k=r_k|_{K_{D,k}\otimes\mathbf Q}.
\tag{1}
$$
有限位仍是原单项式最大系数范数，实位仍是 Euclidean 范数，
目标仍为系数 $[w^k]$，没有换成导数或自由参数的源格。

固定坏集 $\mathcal S$ 包含 R574/R579 的全部坏位。
可用共同 $b=1$ frame；回 $b=17$ 时完整列和行的变换在
$p\ne17$ 都是单位，且 $17\in\mathcal S$。
不删去任何无限普通或惰性素数集合。

## 2. 对任意截断 X 的实际短分母界

对 $n,K\ge1$，保 R574 的准确包络
$$
\Gamma_p(n,K)=\sum_{a\ge1}
 \min\!\left(K,\left\lfloor\frac n{p^a}\right\rfloor\right).
$$
对所有 $X\ge2$，
$$
\boxed{
\sum_{\substack{p\le X\\p\equiv5\ (6)\\p\notin\mathcal S}}
 \Gamma_p(n,K)\log p
 \le C_1(KX+n).
}
\tag{2}
$$
这里常数绝对，与 $n,K,X$ 无关。

**证明。** 一次素数幂部分至多
$$
K\sum_{p\le X}\log p=O(KX).
$$
对全部高次素数幂，无须截断就有
$$
\sum_p\sum_{a\ge2}\frac n{p^a}\log p
=n\sum_p\frac{\log p}{p(p-1)}=O(n).
$$
右边级数由全整数的 $\sum_{m\ge2}\log m/m^2$ 收敛控制。
两项相加即为 (2)。未将实际有限阶原函数当作有界测度。证毕。

R574 在每个好惰性位给的整个原格估计为
$$
\log\|\varphi_D^k\|_p
\le \left\lfloor\frac{6kp}{p^2-1}\right\rfloor\log p
 +\Gamma_p(6k,\min(D,k))\log p.
\tag{3}
$$
模六素数的 Mertens 公式给
$$
\sum_{\substack{p\le X\\p\equiv5\ (6)}}\frac{\log p}{p}
=\tfrac12\log X+O(1).
$$
而 $\sum_p\log p/[p(p^2-1)]$ 收敛，所以 (2)–(3) 推出
$$
\boxed{
\sum_{\substack{p\le X\\p\equiv5\ (6)\\p\notin\mathcal S}}
 \log\|\varphi_D^k\|_p
\le 3k\log X+C_2(k+DX).
}
\tag{4}
$$
此界对全部 $D,k\ge1,X\ge2$ 同时成立，且从头到尾限制在
(1) 的真实饱和前缀上。

(4) 不声称 $p>X$ 的项非正。只有另有实际整性论证时，
才能将它作为所有惰性位的上界。

## 3. 假定一整个次数 D 的大素位全整时的预算

固定 $C>0$ 和 $\vartheta\ge0$，记
$$
X_D=\max(2,CD^\vartheta).
$$
对一个给定 $D$，考虑以下明确的完整假设：
$$
\boxed{\mathcal H_D:\quad
 \|\varphi_D^k\|_p\le1
 \ \text{对全部 }k\ge1\text{ 以及全部好惰性 }p>X_D.}
\tag{5}
$$
零评价层自动满足，真正约束的是所有非零层。
它不是只控制一个有限矩阵的若干低行，也不是只控制单个坐标。

若 $\mathcal H_D$ 成立，把大素位的非正项保留在求和中，
(4) 给
$$
\sum_{\substack{p\equiv5\ (6)\\p\notin\mathcal S}}
 \log\|\varphi_D^k\|_p
\le3\vartheta k\log D+C_3(k+D^{\vartheta+1}).
\tag{6}
$$
常数允许依赖固定 $C,\vartheta$，但不依赖 $D,k$。

R579 在同一格上已经无条件证明全部好普通位
$$
\sum_{\substack{p\equiv1\ (6)\\p\notin\mathcal S}}
 \log\|\varphi_D^k\|_p
\le3k\log D+O(k+D),
$$
固定坏位总成本为 $O(k+D)$。
九个整坐标的同一 Cauchy 估计给
$$
\log\|\varphi_D^k\|_\infty
\le-3k\log k+3k\log D+O(k+D).
$$
所以 $\mathcal H_D$ 下每一个非零层有
$$
\boxed{
\log\|\varphi_D^k\|_\infty+\sum_p\log\|\varphi_D^k\|_p
\le -3k\log k+(6+3\vartheta)k\log D
 +C_4k+C_4(D+D^{\vartheta+1}).
}
\tag{7}
$$
这里保留了一个不能逐层冒充 $O(k+D)$ 的加项
$D^{\vartheta+1}$。下一节在全部真实层上支付它，
而非任意选择 $D\asymp k^{1/9}$。

## 4. 完整饱和旗标的准确累计

因九坐标代数独立，(1) 恰有 $N_D$ 个秩一跳跃
$$
0=k_1<k_2<\cdots<k_{N_D},\qquad k_i\ge i-1.
\tag{8}
$$
[R159 的完整证明](../notes/2026-11-12-degree-sensitive-jets-and-direct-slope-boundary.md)
在同一个原单项式格上给准确恒等式
$$
\boxed{
\sum_{i=1}^{N_D}
 \left(\log\|\varphi_D^{k_i}\|_\infty+
       \sum_p\log\|\varphi_D^{k_i}\|_p\right)=0.
}
\tag{9}
$$
其理由是：各前缀整数格饱和，逐层原始生成元可组成整幺基；
实 quotient 范数之积为一，有限位 quotient 原始范数均为一。
每层真实有理 jet 值的乘积公式遂给 (9)。
常数层 $k_1=0$ 的全部范数为一，直接贡献零。

设 $0\le\vartheta<7$，令
$$
s=\vartheta+2<9,\qquad
G_D(t)=-3t\log t+(6+3\vartheta)t\log D+C_4t,
$$
约定 $0\log0=0$。直接求导给
$$
\sup_{t\ge0}G_D(t)=O(D^s).
\tag{10}
$$
因此前半跳跃的总贡献至多 $O(N_DD^s)$，
没有假设这些跳跃接近其最小允许阶。

对于后半跳跃，(8) 给
$k_i\ge N_D/2-1\gg D^9$。因而对充分大的 $D$，
$$
3\log k_i-(6+3\vartheta)\log D-C_4
\ge c_\vartheta\log D>0.
$$
这些层的 $G_D(k_i)$ 总和至多
$$
-c'_\vartheta N_D^2\log D.
\tag{11}
$$
每层保留的附加项总计为
$$
O\!\left(N_D(D+D^{\vartheta+1})\right).
\tag{12}
$$
因为 $s=\vartheta+2<9$ 而 $N_D\asymp D^9$，
$$
N_DD^s=o(N_D^2),\qquad
N_D(D+D^{\vartheta+1})=o(N_D^2).
$$
将 (10)–(12) 代入 (7)、(9)，右端对充分大的 $D$ 严格为负，
与左端准确等于零矛盾。

所以对于每个固定 $C>0$、$0\le\vartheta<7$，
$\mathcal H_D$ 在每个充分大的 $D$ 都不成立。
整个论证未使用最大接触阶上界；某个真实 $k_i$ 若更大，
其 $-3k_i\log k_i$ 只会加强同一个矛盾。

## 5. 无条件的大素位非整结论

上节的否定正好给出：

**定理。** 对每个固定 $C>0$、$0\le\vartheta<7$，
存在 $D_0(C,\vartheta)$，使每个整数 $D\ge D_0$ 都有
$$
\boxed{
p\equiv5\pmod6,\quad p\notin\mathcal S,\quad p>CD^\vartheta,
\quad k\ge1,\quad \|\varphi_D^k\|_p>1.
}
\tag{13}
$$
这里的层必为 (8) 中某个真实秩一跳跃。

还可把 (13) 表为同一个整数源内的实际非整系数。
在该层取原始 quotient 生成元的整数提升 $P\in K_{D,k}$，
其单项式系数均整，且
$$
r_0(P)=\cdots=r_{k-1}(P)=0,\qquad v_p(r_k(P))<0.
\tag{14}
$$
这是 R159 的有限位 quotient 范数等于一及
$\|\varphi_D^k\|_p=|r_k(P)|_p$ 的直接结果；
没有因局部张量而换掉全局原格。

R574 还给 $p>6k$ 时 (3) 的右端为零。
故 (13) 中必有
$$
\boxed{k\ge\lceil p/6\rceil=(p+1)/6.}
\tag{15}
$$
这个来源中的非整现象因而不能全部限制在固定数量的低 jet。
当取任何 $0<\vartheta<7$ 时，(13) 中素数随 $D$ 无界；
这只说明这个九坐标格有无穷惰性非整位，不是原固定曲线
$\Sha[p^\infty]$ 的无穷非消失或有限性结论。

## 6. 原算术路线可用的严格接口

如果将来从原完整算术失败条件出发，能够在同一个九坐标格、
所有充分大 $D$ 和所有非零层上证明 (5)，
且某个固定 $\vartheta<7$，则第4节立即反证该失败条件。
这比 R574/R579 中保留全素数短分母成本得到的
$\vartheta<6$ 更宽；后者作为充分条件仍正确，没有被否定。

新增的一单位余量来自把已经整的 $p>X_D$ 真正从
短积分分母求和中移除，并支付剩下的 $O(DX_D)$
在完整九维旗标中的总成本。它不来自删除普通成本三，
不来自把七个原函数认作有界测度，也不来自忽略某些低层。

本文没有证明原中央全失败会蕴含 (5)。
R577/R578 的原有限 $M$、完整 forcing 和同修正 $d_2$，
亦未被扩展成九坐标所有次数的 (5)。
原算术总行与两个负矩 $I_4,I_1$ 的比较、
以及真实三线单位余域仍保持未决。
