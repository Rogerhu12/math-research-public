# R872 补充 — 原三尾调整在 F³ 与 F² 真子格中的精确消去

日期：2026-11-16。**状态：下列同一原 \(\mathcal W_D\) 内的因子层消去及三尾不变性已证明。原全部 \(K_1\) 的尾像和同 \(R,S\) 的完整第二、第三页仍未判定。**

本注接 [R872](../results/R872-actual-quartic-third-carry-and-central-first-digit.md)、
[同一因式提升的完整 normal 段](2026-11-16-r872-factored-corrector-last-row-and-residual-branches.md)
及 [R815](../results/R815-complete-original-mori-nef-cones-and-s-fibration.md) 的严格零纤维。
它剥去的是原首核中整个真实因子子格，不只一个已选的纯幂向量。
以下交数门均为显示的假设，不把它们预先赋给所有候选。

## 1. 原窗口和实际三尾

保持前注的原候选
$$
\bar P=t^3F^4q,\qquad
F(t(w),\bar g(w))=w^h u(w),\qquad
s=2h+2,\qquad 1<\ell\le h-1,
$$
$$
p=6s-1>211,\qquad h<s-4,\qquad
F(0,1)=0,\quad e_0=(EF)(0,1)\ne0,\quad
\deg_YF(0,Y)=3.
\tag{1}
$$
这里 \(E=Y\partial_Y\)，\(\bar g\) 是实际原 \(g\)，没有删除近顶高轴。
曲线 \(C\) 假设为原几何整严格因子；记
$$
\kappa=C^2,\qquad d=B_D\cdot C,\qquad T=s-13=2h-11.
\tag{2}
$$
\(B_D\) 是原 \(\mathcal W_D=H^0(X,\mathcal O_X(B_D))\) 的显示除子。
原 \(K_1=\ker\bar M\) 准确给
$$
W_0,W_1,W_2\in w^T k[[w]],\qquad W_3\in w^\ell k[[w]].
\tag{3}
$$
全部 \(W_i\) 使用原公共 charge 四十、\(c_*U_0\) 和同一实际来源。
本注所说“三尾”是
$$
\Pi(G)=\bigl([w^{s-3}]W_2(G),[w^{s-2}]W_2(G),
                         [w^{s-1}]W_2(G)\bigr).
\tag{4}
$$
即使 \(\ell\le3\)，(4) 仍是原三个系数；它们分别是 R872 的可调
native 行，只在相应 \(j<\ell\) 时才能把参考改动项删掉。
后文证明的 \(\Pi=0\) 是完整实际 \(W_2\) 的消失，不需要这个删项。

记真实因子子格
$$
\mathcal V_i=F^i H^0(X,\mathcal O_X(B_D-iC))
             \ \subset\ \mathcal W_D.
\tag{5}
$$
这使用相同整曲面的截面乘法；不把商先放进较大的矩形多项式空间。

## 2. 严格零纤维实际节省的交数

沿原零角的 Gauss 赋值
$$
v_0\!\left(\sum a_n(t)Y^n\right)
=\min_n\{4\operatorname{ord}_t a_n-n\}
$$
有 \(v_0(\mathcal W_D)\ge-2\)、\(v_0(F)=-3\)。于是若
\(G=F^iA\in\mathcal V_i\)，则
$$
v_0(A)\ge3i-2.
\tag{6}
$$
这些剩余因子在 \(t=0\) 的系数分母均为单位。
因此
$$
i=3\Longrightarrow t^2\mid A,\qquad
i=4\Longrightarrow t^3\mid A.
\tag{7}
$$
这里只用非负 \(Y\) 次数及 \(4\operatorname{ord}_t a_n-n\) 的下界。
商的 \(Y\) 多项式性来自原因子整除；同角乘积和实际分母由
R491 的 Gauss 因子论保证。

由 R815，
$$
f_0=f-\sum_{j=1}^4E_{0,j},\qquad C\cdot f_0=3.
\tag{8}
$$
若一个实际剩余截面 \(A\) 可除 \(t^m\)，则其有效零除子含
\(m f_0\)。只从零除子中移去这些**严格纤维**，不宣称
\(A/t^m\) 仍属于原 \(\mathcal W_D\)，也不移去整个总纤维 \(mf\)。

具体地，若 \(A|_C\ne0\)，令 \(D_A\) 为它的实际线束类，则
$$
\operatorname{ord}_P(A|_C)-m
 \le (D_A-mf_0)\cdot C
 =D_A\cdot C-3m.
$$
故
$$
\boxed{\operatorname{ord}_P(A|_C)+2m\le D_A\cdot C.}
\tag{9}
$$
这是正规化上同一非零截面的零因子次数界；\(C\) 的其它奇点、
其它分支及十九角均仍计入全交数。这里 \(t\) 在 \(P=(0,1)\)
是参数，因为 \(F_Y(P)=e_0\ne0\)。

## 3. 整个 F³ 层只能留下 F⁴

取 \(G=F^3A\in K_1\cap\mathcal V_3\)。
在原实际轴上展开 \((E+40)^2G\)。唯一含一次 \(F\) 的项是
$$
6F(EF)^2A;
$$
其余各项均含 \(F^2\)。公共物理单位不能改变消失阶。
因为 \(T<2h\)，(3) 的第二 Euler 长行强迫
$$
\operatorname{ord}_w A(t(w),\bar g(w))\ge T-h=h-11.
\tag{10}
$$
设 \(\psi(t)\) 为 \(F(t,\psi)=0\)、\(\psi(0)=1\) 的原光滑支。
实际 \(\bar g-\psi\) 阶为 \(h\)，而 \(T-h<h\)，故
$$
\operatorname{ord}_P(A|_C)\ge h-11.
\tag{11}
$$
由 (7) 可取 \(m=2\)。若 \(F\nmid A\)，(9) 给准确必要条件
$$
\boxed{d-3\kappa\ge h-7.}
\tag{12}
$$
因此
$$
\boxed{
h-7>d-3\kappa
\quad\Longrightarrow\quad
K_1\cap\mathcal V_3=\mathcal V_4.
}
\tag{13}
$$

这里反向包含也完整成立。若 \(G=F^4B\in\mathcal V_4\)，
(7) 给 \(t^3\mid B\)，而 \(E\) 保持这条真实 \(t\) 因子。因此
$$
\operatorname{ord}_wW_i(G)\ge3+(4-i)h\quad(0\le i\le3).
\tag{14}
$$
这满足 (3)，且
$$
\boxed{\Pi(G)=0,}
\tag{15}
$$
因为 \(W_2(G)\) 从 \(2h+3=s+1\) 起。
(13) 因而不是只给包含，而是同预算截面子格的准确等式。

## 4. F² 层：短第四行给额外的实际限制

先取任意 \(G=F^2A\in K_1\cap\mathcal V_2\)。
原 \(t^0\) 列帽为二次；(3) 在 \(w^0\) 的四个 charge 行
迫 \(G(0,Y)=0\)。原 \(t^1\) 列帽为六次。
因 \(\ell>1\)，同样四行在已经消去 \(t^0\) 后给
$$
G=tG_1(Y)+O(t^2),\qquad
\deg G_1\le6,\qquad (Y-1)^4\mid G_1.
\tag{16}
$$
这些是原 \(W_i\) 的四行：\((E+40)^i\)、\(0\le i\le3\)，
在 \(Y=1\) 与通常四个 jets 是单位三角等价。
没有把原 charge 四十设成零。

又 \(G_1=F(0,Y)^2A_1(Y)\)。
因 \(\deg F(0,Y)=3\)，次数帽迫 \(A_1\) 为常数；
因 \(F(0,Y)\) 在 \(Y=1\) 恰为单根，(16) 迫该常数为零。
所以得到比 (6) 单独给出的结论更强的
$$
\boxed{t^2\mid A.}
\tag{17}
$$

现在沿 \(C\) 作真实局部展开。可把公共物理框记成
\(c(t)Y^{40}\)，其中 \(c(t)\) 是局部单位。
令
$$
V_j=\left.E^j\!\left(Y^{40}F^2A\right)\right|_C .
$$
则
$$
V_2=2\psi^{40}e^2 A|_C.
\tag{18}
$$
取 \(\eta=(\bar g-\psi)/\psi\)，其阶为 \(h\)。
只需到一次 \(\eta\)；全部二次余项阶至少 \(2h>T\)。
于是同一来源的三阶短行和二阶长行分别给
$$
V_3\in t^\ell k[[t]],\qquad
V_2+\eta V_3\in t^T k[[t]],
\tag{19}
$$
第二式允许一个阶至少 \(2h\) 的余项，已在 \(t^T\) 内。
第一式用的是 \(\ell<h\)，从实际轴运输到 \(C\) 合法。
因此
$$
\boxed{\operatorname{ord}_P(A|_C)\ge
                    \min(T,h+\ell).}
\tag{20}
$$
这里 \(V_2,V_3\) 来自同一个 \(A\)，未独立指定其法向值。

若 \(F\nmid A\)，用 (17)、(9) 得
$$
\boxed{d-2\kappa\ge\min(2h-11,h+\ell)+4.}
\tag{21}
$$
所以在两个显示门
$$
\boxed{
\begin{aligned}
h-7&>d-3\kappa,\\
\min(2h-11,h+\ell)+4&>d-2\kappa
\end{aligned}}
\tag{22}
$$
同时成立时，
$$
\boxed{K_1\cap\mathcal V_2=\mathcal V_4,\qquad
       \Pi(K_1\cap\mathcal V_2)=0.}
\tag{23}
$$
第二行门先把 \(F^2A\) 降入 \(\mathcal V_3\)，再用第一行。
没有把 \(F^2\) 与 \(F^3\) 两个分别处理的像加成全 \(K_1\)。

## 5. 对同一个 R、S 的准确含义

R872 的真正第二页改动 \(R\mapsto R+Y\) 和第三页改动
\(S\mapsto S+Y\)，都须有 \(Y\in K_1\)，且同时改变全
\(\beta_1(Y)\)。本注只证明：

- 在 (13) 下，整个三次因子调整层不能改变 (4) 的任何一项；
- 在 (22) 下，这个结论扩大到整个二次因子调整层；
- 因此，若这些门下原某条尾行可以实际调整，承担该调整的
  \(Y\) 必须来自所剩的非 \(F^3\) 或非 \(F^2\) 原来源。

这没有断言那些剩余来源不存在，也没有断言 (22) 在全部短窗成立。
尤其较小的 \(\ell\) 不能借 (20) 免费获得较长接触。
本注不删 \(R872\) 的 baseline、实际中央第二位、其它 normal、
三条十三 carry、末四次项或同一个 \(R,S\)。

上述证明无新增数学数值执行。
