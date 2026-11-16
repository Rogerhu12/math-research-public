# R868 — 原 t 松弛内的真实首像单位与后续 native 标量

日期：2026-11-16。**状态：下列同一来源中的实际首像方向、精确松弛门及逐位影响已证明。没有证明全第二／第三页可解，也没有排除低松弛的实际候选。**

本篇使用 [R861](R861-original-hasse-aligned-gaussian-and-three-hurwitz-readers.md)、[R865](R865-actual-high-axis-product-and-first-divided-row.md) 的 Hasse 对齐规范和完整物理矩阵。全部 $P_{134},c_*U_0,w^{13}$、总 charge 四十、三条十三行带和第四块末端 carry 保留。这里构造的向量来自原 $\mathcal W_D$，不来自扩大后的环境多项式环。

## 1. 同一来源中的准确 t 松弛

保持共同 $E_1$、$p=6s-1>211$、$1\le\ell<s-13$ 及原固定好位；所有来源整性与次数门沿 R861/R657。原格按 [R657](R657-original-long-ordered-prefix-and-quadratic-contact-bound.md)(2) 为
$$
\mathcal W_D=
\bigoplus_{n=0}^D Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\qquad
q_n=(t h_7)^{A_n}(t-1)^{B_n}d^{-C_n},
\tag{1}
$$
$$
A_n=\left\lfloor\frac{n+1}{4}\right\rfloor,\quad
B_n=\left\lfloor\frac{n+1}{3}\right\rfloor,\quad
C_n=\left\lfloor\frac n2\right\rfloor,
$$
$$
h_7=7+4t+16t^2,\qquad d=1+8t,\qquad
e_{n+1}=\left\lfloor\frac{9n}{2}\right\rfloor+4-3A_n-B_n+C_n .
$$
令 $k$ 为原剩余域。对非零原向量
$$
\bar P=\sum_{n=0}^D Y^nq_n(t)f_n(t)\in\mathcal W_D\otimes k
$$
定义
$$
\boxed{\sigma_t(\bar P)=
\min_{f_n\ne0}\operatorname{ord}_{t=0}f_n(t).}
\tag{2}
$$
等价地，若 $\bar P=\sum Y^nP_n(t)$，则
$\sigma_t(\bar P)=\min_n(\operatorname{ord}_0P_n-A_n)$；
$q_n/t^{A_n}$ 在 $t=0$ 是原单位。

对每个整数 $\tau\ge0$，准确有
$$
\boxed{
t^{-\tau}\bar P\in\mathcal W_D\otimes k
\quad\Longleftrightarrow\quad
\tau\le\sigma_t(\bar P).
}
\tag{3}
$$
证明不只比较普通次数。相对 charge 不改变，故在 (1) 的同一直接和中，
商的第 $n$ 项只能是 $q_n(t)t^{-\tau}f_n(t)$。
它属于原多项式帽，当且仅当 $f_n$ 被 $t^\tau$ 整除；
其次数减去 $\tau$，因而无穷帽同时改善。
$h_7,t-1,d$ 的固定角条件逐项保持不变。零角四步链已经完整包含在
原同一 $q_n$ 中，而 (3) 并未放宽它。
这支付全部十九角，且没有增加 charge 或列数。

(3) 可以只在剩余域上使用。若它成立，把每个
$t^{-\tau}f_n$ 的原标准基坐标任意整提升，即得到
$P_0\in\mathcal W_D$。不需要假设最初选定的整提升 $P$ 本身可在
$\mathcal W_D$ 中被 $t^\tau$ 整除。

## 2. 一个实际 k=13 首像方向

以下条件仅对真正存在的原候选提出，不从中央零构造该因子分解。
假设
$$
\bar P=t^rF^4q\in K_1:=\ker\bar M,\qquad
F(t(w),\bar g(w))=w^hu(w),\qquad h\ge1,
\tag{4}
$$
其中 $\bar g$ 是 Hasse 对齐后的**完整实际**径向级数，
不是删除 $h_\Theta$ 后的参考级数；$u(0)$、
$$
e(0),\qquad e=(Y\partial_YF)(t(w),\bar g(w)),
$$
及 $q(0,1)$ 都是单位。$F,q$ 在零角正则，
$F(0,Y),q(0,Y)$ 均非零。其它有限角仍由实际 (4) 属于 (1) 支付。

令
$$
k_{\rm carry}=r+13+2h-s=13+\tau,\qquad\tau>0.
\tag{5}
$$
假设准确的两个门
$$
\boxed{\tau\le\sigma_t(\bar P),\qquad \ell\le s-h.}
\tag{6}
$$
置
$$
\bar P_0=t^{-\tau}\bar P=t^{r-\tau}F^4q.
\tag{7}
$$
由于 $F(0,Y),q(0,Y)\ne0$，
$\min_n\operatorname{ord}_0P_n=r$，故 (6) 也保证 $r-\tau\ge0$。
由 (3)，$\bar P_0$ 在同一个实际来源内。

**定理 1。** (4)–(6) 下，
$$
\boxed{\bar P_0\in K_1,\qquad
\bar\Lambda_0\beta_1(\bar P_0)\in k^\times.}
\tag{8}
$$
这里 $\Lambda_0$ 是 R865 的原零角整行，
$\beta_1:K_1\to C_1=\operatorname{coker}\bar M$ 是完整物理矩阵的首 Bockstein。

证明令 $\mathcal E=Y\partial_Y$。因 $e(0)$ 是单位，
$$
\operatorname{ord}_w
((\mathcal E+40)^j\bar P_0)(t(w),\bar g(w))
\ge r-\tau+(4-j)h\qquad(0\le j\le3).
\tag{9}
$$
原前三个长块只要求相对阶至少 $s-13$，
而 $j=2$ 的右边由 (5) 准确等于 $s$；
$j=0,1$ 更高。第四块要求相对阶至少 $\ell$，
$j=3$ 的右边是 $s-h$，正由 (6) 支付。
共同 $U_0$ 是已付原单位，不降低这些阶。
最前三条十三行在模 $p$ 的所有原列上本来为零。
因此所有四块及其实际端点均给 $\bar M\bar P_0=0$。
末端四次项至少含 $p^3$，不改变此首核判断；没有将它从更高位删掉。

$\bar P_0$ 的实际 carry 指数是
$$
r-\tau+13+2h-s=13 .
$$
R865 的原首行公式于是准确给
$$
\boxed{
\upsilon:=
\bar\Lambda_0\beta_1(\bar P_0)=
\frac{36c_*U_0(0)}{a_*}
 \left(\frac{t(w)}w\right)_{w=0}^{r-\tau}
 q(0,1)u(0)^2e(0)^2\in k^\times.
}
\tag{10}
$$
$h\ge1$ 保证 $O(F^3)$ 不进入显示的最低 $F^2$ 系数。
此计算使用未分割的完整 $G_0$，包括四十和十三前缀，
不把相对 $J$ 的窗口当作原 $M$。证毕。

特别，$\bar\Lambda_0$ 不杀实际 $\operatorname{im}\beta_1$，
所以它本身不下降为第二 Bockstein 余核的左行。
这项结论来自显示的真向量 (7)，不是由维数猜测首像满射。

## 3. 同一 R 和 S 上究竟允许改变什么

固定一个满足
$$
M(P+pR)\in p^2\Gamma
\tag{11}
$$
的原整 $P,R$。令 $P_0$ 是 (7) 的任意原格整提升。
因为 $\bar P_0\in K_1$，
$$
M(P+p(R+cP_0))\in p^2\Gamma\qquad(c\in\mathcal O).
\tag{12}
$$
所以该改变保持的是**完整的第一提升**，包括全部 normal、
三条十三行与末短块；没有分别改动不同块的修正。

定义已经由 (11) 支付整性的指定第二标量
$$
B_2(P,R)=\frac{\Lambda_0M(P+pR)}{p^2}\pmod p .
$$
由 (10) 得
$$
\boxed{
B_2(P,R+cP_0)=B_2(P,R)+\bar c\,\upsilon .
}
\tag{13}
$$
因此这一个标量可以在同一个原仿射修正空间中取任意值。

但完整第二页向量同时改变为
$$
\left[\frac{M(P+p(R+cP_0))}{p^2}\right]
=
\left[\frac{M(P+pR)}{p^2}\right]
+\bar c\,\beta_1(\bar P_0)\quad\text{于 }C_1.
\tag{14}
$$
不能只改变 (13) 而保持 (14) 的其它分量不动。
特别 (13) 可调不证明能找到同格 $S$ 使全矩阵达到 $p^3$。

同样，若某个固定同源 $P,R,S$ 已满足
$$
M(P+pR+p^2S)\in p^3\Gamma,
$$
则 $S\mapsto S+cP_0$ 保持这一完整 $p^3$ 提升，并使
$$
\boxed{
\frac{\Lambda_0M(P+pR+p^2(S+cP_0))}{p^3}
=
\frac{\Lambda_0M(P+pR+p^2S)}{p^3}
+\bar c\,\upsilon\pmod p.
}
\tag{15}
$$
其它第三页分量仍同时沿 (14) 的实际首像方向移动。
原最终修正 $p^3T$ 对 (15) 模 $p$ 无作用，
因为 $\Lambda_0M(T)\in p\mathcal O$。
它对全矩阵其它行的作用照旧保留。

所有这些改变都用同一个已固定的实际 $H_p$、$B$、$a_*$ 和
完整 $g^\flat$。四个原中央没有被用来给 $P_0$ 添新的算术零。

## 4. 低松弛范围不能从本篇删除

(6) 的第一门不能换成仅仅 $r\ge\tau$。
有一个直接可读的必要上界。置
$$
b_0=\deg_YF(0,Y),\qquad c_0=\deg_Yq(0,Y).
$$
$F(0,Y)^4q(0,Y)$ 的最高项非零，其 charge 为 $4b_0+c_0$，
并且该项在 $\bar P$ 中的 $t$ 阶准确为 $r$。
因此
$$
\boxed{
\sigma_t(\bar P)\le
r-A_{4b_0+c_0}
=r-b_0-\left\lfloor\frac{c_0+1}{4}\right\rfloor.
}
\tag{16}
$$
原所属关系已迫右边非负，但不迫它为正。

例如当
$$
r=b_0+\left\lfloor\frac{c_0+1}{4}\right\rfloor
$$
时，准确有 $\sigma_t(\bar P)=0$；
任何 $\tau>0$ 都不能在同 $\mathcal W_D$ 中作 (7)。
特别 $b_0=3,\ c_0\le2,\ r=3$ 的最小零角 quartic 前缀
属于这一低松弛范围。这里并未声称这些候选已经存在。

即使 (16) 为正，也仍须检查 (2) 的**全部** charge：
更高 $Y$ 系数可能先耗尽零角余量。
所以本篇既不扩大来源，也不排掉原最小前缀的临界候选。
下一步真正要判的仍是这些低松弛候选的联合第二／第三页，
或能够杀完整 $\operatorname{im}\beta_1$ 的真实联合左行。
本篇不以一个可调标量替代原同 $R,S$ 的全像问题。

本篇为完整符号证明，无新增数学数值执行。
