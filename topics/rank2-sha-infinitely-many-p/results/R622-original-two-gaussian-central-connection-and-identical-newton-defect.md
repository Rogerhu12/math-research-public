# R622 — 原两层 Gaussian 中央连接与同一个完整 Newton 缺陷

日期：2026-11-14。**状态：已证明。**

本篇保持原 $S/T$、原中央投影和原零初值 Euler 原函数。R618 的第二 Gaussian 被除去以后，完整中央方程在一个严格大于第二临界盘的闭盘上有唯一 Tate 解；该解在原点的值仍准确等于 R598 的同一个 $j_m$。第二 Gaussian 没有产生另一条独立中央零。

同时，本篇给出从第二层系数返回原完整 Newton 导数的所有权。它们是显式单位，但并不等于一；首个差异正好出现在 R619 已支付的第 $p+1$ 项精度。

## 1. 固定原来源、两个 Gaussian 与真实中央投影

保持 R618 的同一好惰性模型及已经支付的物理尺度，不再作新的伸缩：
$$
p=6s-1>71,\quad d=p+1=6s,\quad L=s(p-1),\quad
w=z^6,\quad X=z^d=w^s.
\tag{1}
$$
在本题 $b=17$ 的规范下，取原
$$
A_{34}=S,\qquad A_{72}=T,\qquad A_m=z^6+O(z^{12}).
$$
本篇的 $j_m$ 是这个固定模型上 R598/R618 的完整半因子导数；与相应固定算术曲线的已付桥保持原来的全部常数。

令
$$
F=\log(\sigma/z),\quad c=[w^s]F,\quad
\mathcal U(w)=e^{F-cw^s},\quad
U_0=[\mathcal U]_{<L},
$$
$$
\Delta=F-cw^s-\log U_0,\qquad
a_2=[w^{ps}]\Delta,
$$
$$
\alpha_1=mc,\qquad \alpha_2=ma_2,\qquad
\gamma=mpc=p\alpha_1.
\tag{2}
$$
这里 $m=34$ 或 $72$，均为 $p$ 单位。R618 与 R619 已付
$$
v_p(\alpha_1)=-1,\quad v_p(\alpha_2)=-2,\qquad
p^2\alpha_2\equiv \gamma b^L\pmod p.
\tag{3}
$$
$a_2$ 是 $\Delta$ 的真实系数，不能先替换成裸 $F_{ps}$。

保留原投影
$$
\Pi_0f(z)=\frac1d\sum_{\zeta^d=1}f(\zeta z).
\tag{4}
$$
定义整个原来源及其两次规范化
$$
G_{m,1}(z)=e^{-\alpha_1X}A_m(z),\qquad
G_{m,2}(z)=e^{-\alpha_2X^p}G_{m,1}(z).
\tag{5}
$$
因为 $X$ 与 $X^p$ 在 (4) 下均不变，
$$
G_{m,1,0}(X):=\Pi_0G_{m,1}
 =\sum_{h\ge1}g_hX^h,
$$
$$
G_{m,2,0}(X):=\Pi_0G_{m,2}
 =\sum_{k\ge1}\widetilde g_kX^k
 =e^{-\alpha_2X^p}G_{m,1,0}(X).
\tag{6}
$$
两者都无常数项。整个 $G_{m,2}$ 是单位乘 $z^6$，并不意味着它的中央投影是单位。

## 2. 内外半径与完整第二层来源

置
$$
S_z=p^{-p/(p^2-1)},\quad
R_2=p^{-(2p-1)/(p(p^2-1))},
$$
$$
r_1=S_z^d=p^{-p/(p-1)},\qquad
r_2=R_2^d=p^{-(2p-1)/(p(p-1))}.
\tag{7}
$$
R618 的完整无限尾证明给某个 $\rho_+>R_2$，可取 $\rho_+<1$，使
$$
G_{m,2}(z)=z^6V_m(z),\qquad
V_m,V_m^{-1}\in\mathcal T_{\rho_+},\qquad
\|V_m\|_{\rho_+}=\|V_m^{-1}\|_{\rho_+}=1.
\tag{8}
$$
两个 $m$ 可以共同缩小到同一个 $\rho_+$。令 $r_+=\rho_+^d$。必要时再缩小 $\rho_+$，仍保持
$$
r_1<p^{-1}<r_2<r_+<1.
\tag{9}
$$
这里不是只知闭 $R_2$ 的逐系数严格不等式；(8) 使用 R618 已付的略大闭盘。

投影 (4) 保 Gauss 范数，故
$$
G_{m,2,0}\in\mathcal T_{r_+},\qquad
\|G_{m,2,0}\|_{r_+}\le\rho_+^6.
\tag{10}
$$
以下全部 Tate 空间在 $\mathbf C_p$ 上，半径可取在其值群中；原系数仍在原非分歧系数环的分式域内。

## 3. 原中央 Euler 方程的两层规范

取与 $p$ 无关的原零初值 Euler 原函数
$$
\mathscr U_m(z)=\int_0^z\frac{A_m(t)}t\,dt.
$$
R598 的完整第一层解为
$$
H_{m,1}(X)=d\,e^{-\alpha_1X}\Pi_0\mathscr U_m,
$$
$$
H_{m,1}'+\alpha_1H_{m,1}=G_{m,1,0}/X,
\qquad H_{m,1}(0)=0.
\tag{11}
$$
$d$ 因子在此保留。

对同一个原函数再定义
$$
H_{m,2}=e^{-\alpha_2X^p}H_{m,1}.
$$
逐项微分得真正的完整连接
$$
\boxed{
H_{m,2}'
 +\bigl(\alpha_1+p\alpha_2X^{p-1}\bigr)H_{m,2}
 =G_{m,2,0}/X,\qquad H_{m,2}(0)=0.
}
\tag{12}
$$
右端在原点正则。式 (12) 是特征零形式恒等式，并在原收敛小盘中是解析恒等式；以后所说的外盘延拓由它的唯一 Tate 解支付。

## 4. 略大于第二临界盘的唯一 Tate 解

**定理 1。** 对每个 $p^{-1}<r\le r_+$，算子
$$
\mathcal L_2=\partial_X+\alpha_1+p\alpha_2X^{p-1}
$$
在 $\mathcal T_r$ 上可逆。其对 (12) 右端的唯一解在这些盘之间相容，并在闭 $r_+$ 上为 Tate 元。

证明。令
$$
\mathcal B_r=\alpha_1^{-1}
 \bigl(\partial_X+p\alpha_2X^{p-1}\bigr).
$$
在 Tate Gauss 范数下，
$$
\|\partial_X\|\le r^{-1},\qquad
|\alpha_1^{-1}|=p^{-1},\qquad
|\alpha_1^{-1}p\alpha_2|=1.
$$
因此
$$
\boxed{
\|\mathcal B_r\|
 \le \max(p^{-1}r^{-1},\,r^{p-1})<1.
}
\tag{13}
$$
完整 Neumann 级数给
$$
\boxed{
\mathcal R_{m,2}
 =\alpha_1^{-1}
   \sum_{n\ge0}(-\mathcal B_r)^n(G_{m,2,0}/X)
 \in\mathcal T_r .
}
\tag{14}
$$
(13) 同时支付整个算子尾和唯一性，不是有限系数递推。外盘解限制到内盘后仍是同一解。特别
$$
\|\mathcal R_{m,2}\|_{r_+}
 \le p^{-1}\rho_+^6/r_+.
\tag{15}
$$
证毕。

## 5. 唯一外盘解的原点值就是原 j

R598/R618 的同一个完整导数是
$$
j_m=\sum_{h\ge1}(-1)^{h-1}(h-1)!\alpha_1^{-h}g_h.
\tag{16}
$$

**定理 2。**
$$
\boxed{
\mathcal R_{m,2}(0)=j_m,
}
\tag{17}
$$
并且作为原零初值解的形式与小盘恒等式，
$$
\boxed{
H_{m,2}
 =-j_m e^{-\alpha_1X-\alpha_2X^p}
  +\mathcal R_{m,2}.
}
\tag{18}
$$
等价地，
$$
\boxed{
d\,\Pi_0\mathscr U_m
 =e^{\alpha_1X+\alpha_2X^p}\mathcal R_{m,2}-j_m.
}
\tag{19}
$$
式 (19) 不声称两个指数在整个外盘分别解析。

证明。取 $p^{-1}<r<r_2$。第二指数及其逆在闭 $r$ 盘为 Tate 单位，因此
$$
e^{\alpha_2X^p}\mathcal R_{m,2}\in\mathcal T_r
$$
且满足第一层非齐次方程
$$
(\partial_X+\alpha_1)
 (e^{\alpha_2X^p}\mathcal R_{m,2})=G_{m,1,0}/X.
$$
$\alpha_1^{-1}\partial_X$ 的范数小于一，故这一方程的唯一 Tate 解为
$$
\alpha_1^{-1}\sum_{n\ge0}
 (-\alpha_1^{-1}\partial_X)^n(G_{m,1,0}/X).
$$
其原点值准确为 (16)。第二指数常数一，遂得 (17)。
两个 (12) 的形式解之差为常数乘
$e^{-\alpha_1X-\alpha_2X^p}$；由零初值确定该常数为 $-j_m$，得到 (18)、(19)。证毕。

由原第一指数的数字和公式，它在闭 $r_1$ 非 Tate、精确半径为 $r_1$。第二指数在该闭盘是 Tate 单位，所以乘上第二指数不改变这条闭边界。另一方面 $\mathcal R_{m,2}$ 在严格更大的 $r_+$ 盘解析。因此
$$
\boxed{
j_m=0
\iff H_{m,2}\in\mathcal T_{r_1}
\iff H_{m,2}\in\mathcal T_{r_+}.
}
\tag{20}
$$
若 $j_m\ne0$，$H_{m,2}$ 精确半径仍为 $r_1$，且闭 $r_1$ 非 Tate；若 $j_m=0$，第二次规范后的同一中央原函数延拓到严格大于 $r_2$ 的闭盘。

这是原完整零条件的准确运输；没有新增第二条算术零。

## 6. 全部第二层系数如何返回原 Newton 导数

令
$$
q=\frac{\alpha_2}{\alpha_1^p},\qquad v_p(q)=p-2.
$$
以下上升乘积专门写为
$$
(k)^{\overline n}=k(k+1)\cdots(k+n-1),
$$
以免与原 Newton 下降阶乘混淆。定义完整权
$$
\boxed{
\mathcal W_k(q)=
 \sum_{r\ge0}(-1)^r
 \frac{(k)^{\overline{pr}}}{r!}\,q^r
\quad(k\ge1).
}
\tag{21}
$$
因
$$
(k)^{\overline{pr}}
 =(pr)!\binom{k+pr-1}{pr},
\qquad
v_p((pr)!)-v_p(r!)=r,
$$
第 $r$ 项的赋值至少为 $r(p-1)$。所以对全部 $k$ 一致地有
$$
\boxed{
\mathcal W_k(q)\in1+p^{p-1}\mathcal O.
}
\tag{22}
$$

**定理 3。** 原完整导数准确为
$$
\boxed{
j_m=
 \sum_{k\ge1}(-1)^{k-1}(k-1)!
 \alpha_1^{-k}\widetilde g_k\,
 \mathcal W_k(q).
}
\tag{23}
$$
全部 $k,r$ 的尾已收敛，(23) 不只是一条首层关系。

证明。由 (6)，
$$
g_h=\sum_{\substack{k+pr=h\\k\ge1,\ r\ge0}}
 \frac{\alpha_2^r}{r!}\widetilde g_k.
$$
代入 (16)，保 $p$ 为奇数的符号，即得 (23) 的形式。为支付换序，写
$\rho_+=p^{-\tau_+}$、$\delta_+=d\tau_+$。由 (10)，
$$
v_p\bigl((k-1)!\alpha_1^{-k}\widetilde g_k\bigr)
\ge k(1-\delta_+)+6\tau_+ +v_p((k-1)!).
\tag{24}
$$
这里
$$
\delta_+<\frac{2p-1}{p(p-1)}<\frac12.
$$
再加每个 $r$ 项的 $r(p-1)$ 下界，整个二重和随任一指标趋于无穷而趋零。换序及 (23) 因此严格成立。证毕。

单位权 (22) 不能删去。具体地，另记
$$
\widetilde j_m
 =\sum_{k\ge1}(-1)^{k-1}(k-1)!
   \alpha_1^{-k}\widetilde g_k.
\tag{25}
$$
这是对第二层分子重新使用第一层形式所产生的一个收敛值，尚不是原算术中央。式 (24) 使每项赋值至少为一，$k\ge2$ 时至少为二。因此
$$
j_m-\widetilde j_m\in p^p\mathcal O.
$$
模 $p^{p+1}$ 仅 $k=1,r=1$ 可以贡献：
$$
\boxed{
j_m-\widetilde j_m
 \equiv
 -\frac{p!\alpha_2}{\alpha_1^{p+1}}\widetilde g_1
 \equiv
 \frac{p^p b^L}{\gamma^p}\,\overline{g_1}
 \pmod{p^{p+1}}.
}
\tag{26}
$$
这里 $\widetilde g_1=g_1$，第二个同余使用 (3) 及
$(p-1)!\equiv-1\pmod p$。这与 R619 的完整第二块端点相同。

若原 $j_m=0$，则首层 $\overline{g_1}=0$，从而
$\widetilde j_m\in p^{p+1}\mathcal O$；没有得到 $\widetilde j_m=0$。
原条件在第二层的准确形式始终是带全部 $\mathcal W_k$ 的 (23)。

## 7. a₂ 与裸 F_(ps) 的规范比较

由原 $U_0$ 的整性，
$$
v_p\bigl(a_2-F_{ps}\bigr)
 =v_p\bigl(-[w^{ps}]\log U_0\bigr)\ge-1.
\tag{27}
$$
因此相应两种第二层规范之比
$$
\exp\bigl(m(a_2-F_{ps})X^p\bigr)
$$
在某个严格大于 $r_2$ 的闭盘上是 Tate 单位：其指数收敛半径至少为
$p^{-1/(p-1)}>r_2$。可将前述 $r_+$ 共同缩小到这个范围，仍保 $r_+>r_2$。

在这一范围，两种非齐次方程的唯一 Tate 解由这个实际单位相乘互相对应；单位常数一，所以它们在原点的值仍为同一 $j_m$。但是它们的第二层系数和 (21) 的权要同步改变，不能只换 $a_2$ 而保旧系数。

## 8. 原来源与真前缀的范围

所有恒等式都保了实际 $\Pi_0$。第二 Gaussian 的指数次数为 $p(p+1)$，故与该投影交换；本篇没有把任意其他角的测试搬成中央测试。

式 (14) 是同一实际中央连接的完整解析逆，不是原全局有限来源格上的整行变换。式 (23) 的权是整个原导数的准确系数运输，也未被证明保持任意原次数帽、连续真前缀或原 Schwartz 伴随域。特别，原普通 Euler 有限阶分布障碍不会因本篇的惰性规范而消失。

本篇把原完整 $j_m=0$ 继续运输到第二临界盘之外；主目标仍需证明无穷多个不同素数的指定 $j_m$ 非零，或把这条原零条件转成确已支付的真来源矛盾。没有从第二坏带的确定非中央单位替代这一缺口。

## 依赖

- [R598](R598-original-full-newton-derivatives-and-central-euler-stokes.md)：原 Euler 函数、实际 $\Pi_0$、完整 $j_m$ 与第一 Stokes 缺陷。
- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：实际 $a_2$、完整第二 Gaussian、略大闭盘的 Tate 单位及全部原来源尺度。
- [R619](R619-original-cartier-sparse-rows-and-second-newton-block.md)：唯一二阶极部与原 $p+h$ 中央块；式 (26) 保其完整精度。

全篇为原全参数与完整 Banach 算子证明，不依赖新增素数扫描。
