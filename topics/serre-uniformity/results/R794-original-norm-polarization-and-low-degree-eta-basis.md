# R794：原 Hom 范数的极化与有限候选中的低次数 η 基

日期：2026-11-15。状态：**本篇的原范数识别、候选完备性及保规范基变换已证明；所选映射、实际秩和次数由公开 Actions 的真实输出另行登记。**

本篇只读取已完成的 R791 原矩阵、Gram 与极化，以及 R759 原十二个整数 Hom 基。
不重算旧周期、Hom、LLL 或 SVP。
目的在于给 R793 选择次数较小的实际函数输入，保持 R791 的同一个完整 $F^0$；
不把新基的选择称为算出了 $\eta$、高度或全 $p$ 排除。

## 1. 原十二维空间是同一个 CM 域的秩一模

令
$$
V=\mathcal H\otimes_{\mathbb Z}\mathbb Q,\qquad
E=\mathbb Q[T]\simeq\mathbb Q[Z]/\Phi_{21}(Z).
\tag{794.1}
$$
这里 $T$ 为 R791 真实 gamma_matrix 的列作用，
$T^{14}=J$ 是原 $\zeta$ 作用，$T^7=J^2$。
R791 已证明 $E$ 为十二次域，$V$ 为其秩一模。
原 $f=f_4\ne0$，所以
$$
\{f,Tf,\ldots,T^{11}f\}
\tag{794.2}
$$
是 $V$ 的 $\mathbb Q$ 基。
对任意原整数列 $\mathbf v\in\mathbb Z^{12}$，其实际映射 $f_{\mathbf v}$
唯一写成
$$
f_{\mathbf v}=a_{\mathbf v}(T)f,\qquad
a_{\mathbf v}\in E.
\tag{794.3}
$$
实际计算仅需对 (794.2) 的十二阶列矩阵作准确有理解，
并把全部十二个坐标代回；这不是重新求原 Hom 作用矩阵。

原 Rosati 在 $E$ 上为
$$
a\longmapsto a^*,\qquad T^*=T^{-1}=T^{20},
$$
其实子域记作 $F=E^+$，次数六。
使用固定实基
$$
1,\ s_1,\ldots,s_5,\qquad s_j=T^j+T^{-j}.
\tag{794.4}
$$
因此
$$
n_{\mathbf v}=a_{\mathbf v}^*a_{\mathbf v}\in F.
\tag{794.5}
$$
不得把 $a_{\mathbf v}$、$n_{\mathbf v}$ 当成未经运输的另一条 CM 字段坐标。

## 2. 原极化与次数确定准确去迹

沿用 R791 的同一个
$$
e_R=\kappa M_R
=3870+711s_1-801s_2-360s_3+612s_4+864s_5,
\qquad \operatorname{Tr}_{F/\mathbb Q}e_R=25326.
\tag{794.6}
$$
$M_R$ 来自原 $f_R=[1-\zeta^2]f$ 的实际 Weil 映射。
其全部矩阵和标量都读取原成功阶段，不重新把 $\kappa$ 或 $M_R$ 设为一。

将 (794.3) 在原 Weil 映射上运输。准确地，写原
$q_R=v_Rq$、$v_R:A\to A_{42}^{\rm mod}$，
把 $a_{\mathbf v}(\mathcal T)$ 经同一个 $v_R$ 运送为
$a_{\mathbf v}^A\in\operatorname{End}_K^0(A)$。于是
$q_{\mathbf v,R}=v_Ra_{\mathbf v}^Aq$；以下只在这次固定识别后
把上标 $A$ 省略，并记 $v_{\mathbf v,R}=v_Ra_{\mathbf v}$。
这一步对一般 $a_{\mathbf v}\in E$ 先在 $K$ 上进行，使用原
$B_K\simeq\operatorname{Res}_{L/K}C$。复共轭送
$a_{\mathbf v}$ 到 $a_{\mathbf v}^*$；因此
$[1-\zeta^2]f_{\mathbf v}$ 未必在 $\mathbb Q(b)$ 上定义，
$q_{\mathbf v,R}$ 也未必在 $\mathbb Q$ 上定义。
这里的 $R$ 只记录与原 $f_R$ 相同的三次同源，并不宣称所有新映射都是实下降。
因为 $M_R=v_R^\dagger v_R$ 与 $E$ 交换，
$$
v_{\mathbf v,R}^{\dagger}v_{\mathbf v,R}
=a_{\mathbf v}^*M_Ra_{\mathbf v}
=M_Rn_{\mathbf v}.
\tag{794.7}
$$
这里 adjoint 保留原极化，两侧乘法次序已经明确。
对称线丛的这个 NS 识别在原有理线丛群中是准确的：
虽然上述映射先在 $K$ 上，$M_Rn_{\mathbf v}\in F$ 是原有理 NS 元素。
同一个 NS 类的两个对称线丛至多相差 Picard 零次的二挠元，
在原 $\eta\in J_Y(\mathbb Q)\otimes\mathbb Q$ 的定义中为零。
故其对称线丛有理类及所导出的 $\eta$ 类准确下降到 $\mathbb Q$。
这不准许丢掉后面给出的实际主函数常数。

记 $G$ 为 R759 的 twice_degree_Gram_matrix，令
$$
d_{\mathbf v}=\frac12\mathbf v^{\,t}G\mathbf v,\qquad d_f=1206.
$$
由七个 Weil 分量及三次自同源的准确次数，
$$
\operatorname{Tr}_{F/\mathbb Q}(e_Rn_{\mathbf v})=21d_{\mathbf v}.
\tag{794.8}
$$
故原去迹元素及其 NS 输入为
$$
c_{\mathbf v}=n_{\mathbf v}-\frac{d_{\mathbf v}}{1206},
\qquad
\boxed{h_{\mathbf v}=\kappa^{-1}e_Rc_{\mathbf v}\in F^0.}
\tag{794.9}
$$
其中 $F^0=\ker(h\mapsto\operatorname{Tr}(\kappa h))$，仍是原五维空间。
实际核心同时核 (794.8)，将新范数、原 Gram 次数和原极化标度准确接在一起。

对旧五个列 $(I+T^j)e_4$，
$$
n_j=(1+T^{-j})(1+T^j)=2+s_j,
$$
且 $d_j/1206=2+r_j$。
所以 (794.9) 恰回到 R791 的原
$h_j=\kappa^{-1}e_R(s_j-r_j)$，没有改变原高度输入的缩放。

## 3. 对应 η 只需所选实际映射的极除子

记 $P_{\mathbf v}=(y_{f_{\mathbf v}})_\infty$、$P_f=(y_f)_\infty$。
R764 的零平移对全部原整数列成立。
R791 的 Poincaré 拉回公式、(794.7) 和原三次同源给
$$
\boxed{
\eta_{h_{\mathbf v}}=
\left[
\sum_{\sigma\in\operatorname{Gal}(L/K)}P_{\mathbf v^\sigma}
-\frac{d_{\mathbf v}}{1206}\sum_\sigma P_{f^\sigma}
\right].}
\tag{794.10}
$$
它是同一个原 $J_Y(\mathbb Q)\otimes\mathbb Q$ 中的类。
原 $f_{\mathbf v}$ 自身可仅在 $L$ 上定义；
(794.9) 的实、Rosati 自伴 NS 元素以及原有理对称线丛识别给所需下降，
不要求每个单独分量都先成为 $\mathbb Q$ 映射。

主函数仍明确保留。
写 $d_{\mathbf v}/1206=p/q$ 为既约分数、$q>0$，
原三次同源的完整极除子恒等式给
$$
\mathcal R_{\mathbf v}
=\frac{N_{L/K}(y_{f_{\mathbf v}}^2-b)^q}
        {N_{L/K}(y_f^2-b)^p}.
\tag{794.11}
$$
具体地，原 $3q\eta_{h_{\mathbf v}}$ 的三次同源除子，
减去 (794.10) 中除子的 $3q$ 倍，恰为
$\operatorname{div}\mathcal R_{\mathbf v}$。
后继若再采用 R793 的 Jacobian 降次，应一并运输
R793 的 $\mathcal G^3$ 与本式，而不是只留下一个相同的 Picard 类。

(794.11) 精确记录的是 $[1-\zeta^2]f_{\mathbf v}$ 与
$f_{\mathbf v}$ 之间的这一步三同源主函数。
它没有自动给出原选定对称 $\mathcal L_{h_{\mathbf v}}$ 与上述
拉回代表之间可能存在的二挠线丛比较函数。
若后继使用具体线丛或原局部高度规范，须在一个足以消去该二挠差的
整数倍上明确比较截面，并保留其原 $c_0$ 刚性化和函数常数。
本次原五方向的有理基变换及 (794.10) 的 $J\otimes\mathbb Q$ 等式
不需要把该尚未求出的比较函数假定为一；也不声称完整原高度运输已经计算。

## 4. 十二个基与两两和必定覆盖全部五个方向

令 $a_0,\ldots,a_{11}$ 为原十二基在 (794.3) 中的 $E$ 坐标。
这些元素构成 $E$ 的 $\mathbb Q$ 基。

**定理 794.1。** 以下78个范数的 $\mathbb Q$ 张成空间为整个 $F$：
$$
\{a_i^*a_i:0\le i<12\}
\ \cup\
\{(a_i+a_j)^*(a_i+a_j):i<j\}.
\tag{794.12}
$$
因此它们按 (794.9) 去迹后的张成维数严格为五。

**证明。** 极化恒等式
$$
a_i^*a_j+a_j^*a_i
=n(a_i+a_j)-n(a_i)-n(a_j)
$$
表明 (794.12) 张成任意 $a\in E$ 的 $n(a)=a^*a$：
把 $a=\sum q_i a_i$ 展开即可。
反过来，对任意 $c\in F$，
$$
2c=n(1+c)-n(1)-n(c).
$$
所以所有范数张成 $F$。
线性投影
$$
n\longmapsto n-
\frac{\operatorname{Tr}(e_Rn)}{\operatorname{Tr}e_R}
$$
的核为 $\mathbb Q\cdot1$，像为五维超平面。
再乘可逆 $e_R/\kappa$ 就是原 $F^0$。$\square$

这个结论不要求原十二个单独范数已经有满秩；
核心将实际记录它们的秩。
两两和的覆盖是严格保证，不能将未运行的十二个秩预填为五。

## 5. 一个明确、有限的实际选择任务

本次固定候选为：

- 原十二个 $e_i$；
- 66个 $e_i+e_j$、$i<j$；
- 66个 $e_i-e_j$、$i<j$；
- R791 已认证的五个旧列 $(I+T^j)e_4$，$1\le j\le5$。

共149条；允许不同列给同一个 NS 方向。
两两差只帮助降低这份有限清单的次数，不扩展成新的格搜索。
旧五列提供已有完整基的比较上界。
对每条候选准确计算其原 Gram 次数、(794.5) 和 (794.9)，
按“次数、固定候选编号”排序，依次只收会增加当前秩的方向，直到秩五。

线性独立的子集构成线性拟阵。
标准交换论证给：上述贪心规则在**这份明确149候选清单内**
使所选五个次数之和最小，也可在相同总和时取确定的贪心顺序。
证明可逐步进行：任取另一个最小权基，若未包含当前最早可扩充元素，
用它替换该基中保持可扩充所需的一个不更早元素，权不增；
依次固定已选元素即可。
不声称这是完整整数 Hom 格内的全局最优，也不重新求 SVP。

真实输出必须列出：

1. 原十二个、加入两两和后及全部候选的实际秩；
2. 每个所选原整数列、实际次数、$a_{\mathbf v}$、$n_{\mathbf v}$、
   $d_{\mathbf v}/1206$ 与 $\kappa h_{\mathbf v}$ 的完整准确坐标；
3. 所选五列的真实非零五阶 minor；
4. 与 R791 原五个 $h_j$ 之间的准确可逆 $5\times5$ 基变换。

最后一项使已登记的原高度形式和 $h$ 输入可按坐标运输，避免重新命名后丢掉原常数。
该计算只是在原有理矩阵和十二次数域中进行的小线性代数。
它没有生成新映射的 Laurent、极除子、Jacobian 类或高度。

## 6. 直接交给 R793 的精确参数

对实际选出的每条非零整数列，R793 定理793.4给全部 cusp 的 $e=1$。
不需要另判一次是否偶然发生首项取消。
用其真实次数 $d$ 输出
$$
m=\left\lceil\frac{d+254}{272}\right\rceil,\quad
f_0=272m-d,\quad
N=\left\lfloor\frac{272m+d}{20}\right\rfloor+1.
\tag{794.13}
$$
这分别是原普通截面幂、残余除子次数和完整 Laurent 条件数。
实际关系范围为 $-1,\ldots,N-2$，基前缀要到 $q_Y^{N-1}$。
原新微分由所选十二维整数列合成，保持 R764 的零 Abel 常数。
不改变原目标 $b$、微分规范、$c_0$ 或 $c_1$。

只读已经完成的 R791 原矩阵/极化与 R759 原基。
实际任务的脚本、参数、run 及输出 SHA 是后继绑定；
可重算表和证书只作一日当前任务传输，不入仓库或 Release。
五个方向的实际选择完成后继续原 Laurent、RR 除子与高度输入，
不会把这次选择本身当作全课题完成。

## 依据

- R728、R759、R764（2026）：原 Weil 因子、完整整数 Hom 基、
  真实次数 Gram 及完整零平移。
- R785、R791（2026）：原 Rosati、$K[T]$ 作用、实际 $e_R$、
  原完整 $F^0$ 与 Poincaré 极除子公式。
- R793（2026）：原全 cusp 不分歧、完整 Laurent 界、
  固定 RR Jacobian 表示及主函数运输。
