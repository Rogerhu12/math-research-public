# R1098：原 level47 坏素数处的完整 CM–Hecke 交数

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明。** 本文给原坏素数47处的水平交数和垂直修正，不假设 Hecke 对应在坏正则模型上的水平投影公式。尚未计算新的全局高度数值。

## 1. 原对象和结论

沿用 [R1094](R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md)、
[R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md) 的
$$
X=X_{\rm ns}^{+}(47),\quad q=4513,\quad
u_4=23y_4-C_\infty,\quad u_{16}=23y_{16}-C_\infty,
$$
$$
B=q+1-T_q,\qquad D_4=Bu_4,\quad D_{16}=Bu_{16}.
$$
这里 $y_4,y_{16}$ 为原 canonical Cartan 标记的有理 CM 点，
$j(y_4)=1728,\ j(y_{16})=287496$；原23尖点组成 $C_\infty$。
对奇数 $n$ 且 $(n,47q)=1$，令
$$
H(n)=(\overline y_4\cdot\overline {T_ny_{16}})_{\mathcal X,47},
\qquad
b(n)=[\overline E_4]\,T_n[\overline E_{16}],
\tag{1}
$$
其中 $\mathcal X$ 为 [R28](R28-bad-reduction-norm-interface.md) 的原正则模型；
$b(n)$ 是 supersingular 椭圆曲线的标准 Brandt 作用，按核逐一计数。

置
$$
\mathcal D_qf(n)=(q^2+3q+1)f(n)-2(q+1)f(nq)+f(nq^2).
\tag{2}
$$
原 admissible Néron 交数准确为
$$
\boxed{\quad I_{47}(D_4,T_nD_{16})
       =23^2\mathcal D_qH(n)+23\mathcal D_qb(n).\quad}
\tag{3}
$$
第二项是完整垂直修正，不可省略。$T_{q^2}$ 包括非循环子群。

令 $r_2(t)=\#\{(a,b)\in\mathbf Z^2:a^2+b^2=t\}$。
对任意奇 $m$ 且 $47\nmid m$，写 $B_A=8m-A$，则
$$
\boxed{\quad
H(m)=\frac1{16}
 \sum_{\substack{0<A<8m,\ 4\nmid A\\47\mid B_A}}
 r_2(A)\,r_2(B_A/47)\bigl(v_{47}(B_A)-1\bigr),
\quad}
\tag{4}
$$
$$
\boxed{\quad
b(m)=\frac1{16}
 \sum_{\substack{0<A<8m,\ 4\nmid A\\47\mid B_A}}
 r_2(A)\,r_2(B_A/47).
\quad}
\tag{5}
$$
零 $r_2$ 项按零计，不作负权解释。非零项的 $v_{47}(B_A)$ 为奇数，
所以(4)只有 $47^3\mid B_A$ 才可能贡献。
特别地
$$
H(1)=H(q)=0,\qquad b(1)=0.
\tag{6}
$$
这些是小范数界的纸证，不是新数值运行。

## 2. 原 CM 目标在坏模型上落在哪里

所有与47互素的 Hecke 目标在47都未分歧。
确切地，先在有限无分歧扩张上选择 $E_4$ 的 good model；
$E_4[2m]$ 有限 étale，继续无分歧扩张便可定义全部核、商曲线、
以及从原 canonical 标记运输的 necklace。
各目标的 CM 序在47局部仍是最大无分歧二次序。

原 SNC 预模型中，未分歧 $W$-截面只能经过 multiplicity1 分量的光滑点：
若经过 multiplicity 大于1的分量或分量交点，
局部等式对 $47$ 的 valuation 是至少2个正整数之和，或至少2的倍数，
与 $v_W(47)=1$ 矛盾。
因而这些目标避开收缩后尖点的共同点 $P$，
落在 [R28](R28-bad-reduction-norm-interface.md) 的五条 $C_i$ 上；
所落分量由 underlying supersingular $j$ 决定。
这对任意本处 $m$ 成立，不要求 [R33](R33-hecke-norm-and-component-data.md)
小度数窗口 $m<\rho=8$。

原五个 $j$ 为 $0,9,10,36,44$；
$e_i=|\operatorname{Aut}(E_i)|/2$ 在 $j=0$ 为3、$j=36$ 为2，其余为1。
$y_4$ 落在 $j=36$，$y_{16}$ 落在 $j=44$。
于是 $\overline{T_my_{16}}\cdot C_i$ 就是标准 Brandt 列。
所有 CM 闭包与尖点闭包在47不交。

## 3. canonical necklace 的唯一性与真实 coarse 横交长度

这里没有好素处的“模47 normalizer”筛选；
level47 在47不是 étale，必须使用原坏模型。

设 $Y$ 是上节任一未分歧 CM 目标。
扩大无分歧定义域，使其局部 CM 作用定义。
其形式群是 $\mathcal O_{\mathbf Q_{47^2}}$ 的 height-one Lubin–Tate 群。
模47惯性像为整个 $\mathbf F_{47^2}^{\times}$。
一个未分歧 necklace 必须被此 Cartan 固定；
取其 projective 阶48生成元，
正规化子外陪集中的元素都是 involution，
所以任何包含该生成元的 nonsplit Cartan normalizer
具有同一个 Cartan。固定 necklace 因而唯一，是 canonical necklace。

在 $y_4$ 的原 coarse 管内，
[R1074 §9](R1074-certified-original-p47-eight-CM-disks.md) 已给整参数 $z$ 和
整个 $\mathbf C_{47}$ 管的同构
$$
\frac{j-1728}{47^2}=\epsilon z+47R(z),\qquad \epsilon\in W^\times,
\tag{7}
$$
并且此管恰对应 $v_{47}(j-1728)>2$。
同一个未分歧 $j$ 在此管的逆像，因上段唯一性就是原标记的 $Y$；
generic twist 的中心符号不改变 necklace。

取 fine universal 椭圆变形坐标 $t$，使 canonical $E_4$ 为 $t=0$。
$j-1728$ 在此处是 $t^2$ 乘单位，因为 special automorphism
模去中心后阶2、且47不整除2。
若 $Y$ 的 fine canonical 接触长度为 $L$，
$$
v_{47}(j(Y)-1728)=2L.
$$
由(7)，实际原粗曲线上每个相同 supersingular 目标的水平交数为
$$
\begin{cases}
0,&L=1,\\
2(L-1),&L>1.
\end{cases}
\tag{8}
$$
$L=1$ 时 $(j-1728)/47^2$ 是单位，special 点不在 canonical 中心，
所以也准确等于 $2(L-1)$。
这支付了从椭圆 fine 变形到原坏 level47 曲线的全部尺度。

## 4. 四元数枚举、二核与全部重数

把 $\operatorname{End}(\overline E_4)$ 识别为
$$
R=\mathbf Z\left[i,\frac{1+j}{2}\right],
\quad i^2=-1,\quad j^2=-47,\quad ji=-ij.
$$
其元素可唯一写为
$$
\beta=(a+bi+cj+dij)/2,\qquad
a\equiv c,\ b\equiv d\pmod2,
$$
$$
N(\beta)=\frac{a^2+b^2+47(c^2+d^2)}4.
\tag{9}
$$
原 $T_2y_4=y_4+2y_{16}$ 的 Gaussian 核为 $\ker(1+i)$；
其它两个核恰给两个同一 $y_{16}$ 的副本。
因 $m$ 为奇数，degree $2m$ 同源的2-primary 核唯一。
留下这两个非 Gaussian 二核，等价于
$$
N(\beta)=2m,\qquad \beta/(1+i)\notin R.
\tag{10}
$$
compose 后到 $\overline E_4$ 的 isomorphism 有4种，
故每一个 $T_my_{16}$ 核给 $2\cdot4=8$ 个 $\beta$。
这既证明 $b(m)=\#\{\beta\text{ in (10)}\}/8$，
又在逐核计重时给水平交数
$$
H(m)=\frac14\sum_{\beta\text{ in (10)}}(L(\beta)-1).
\tag{11}
$$
奇 $m$ 保留 char0 conductor 的2-primary 序，
所以不存在原 $y_4$ 的 generic 回返；不涉及 self-intersection 或 tangent 选择。

Gross 的 canonical lifting 端态滤过在此为
$$
L(\beta)=1+\min(v_{47}(c),v_{47}(d)).
\tag{12}
$$
因为 $-1$ 在 $\mathbf F_{47}$ 不是平方，
令 $A=a^2+b^2,\ C=c^2+d^2,\ B_A=47C$，
便有
$$
A+B_A=8m,\qquad
L(\beta)=\frac{v_{47}(B_A)+1}{2}.
\tag{13}
$$
此处 canonical CM 序在47最大；可直接用 Gross 的
$R_s=\mathcal O+47^sR$ 端态滤过，任意 $m$ 不需新的 quasi 假设。

为完整计算(10)的 parity 因子，
$$
\frac{\beta}{1+i}
=\frac{(a+b)+(b-a)i+(c-d)j+(c+d)ij}{4}.
\tag{14}
$$
将原 $a\equiv c,b\equiv d$ 代入(14)，逐模4检查，
固定 $A,C$ 下允许而不整除的四元组数为
$$
\begin{cases}
\frac12r_2(A)r_2(C),&4\nmid A,\\
0,&4\mid A.
\end{cases}
\tag{15}
$$
这也可直接消费 [R1097 §5](R1097-original-level47-odd-prime-CM-intersections-and-sparse-norm-sum.md)
已写出的同一 parity 枚举，只有 $j^2$ 从 $-\ell$ 取成 $-47$。
$C=0$ 的 Gaussian 同源全被(10)删去；
$A=0$ 则 $47\mid m$，本处不可能。
将(13)、(15)代入(11)与 $b=\#\beta/8$，得到(4)、(5)。

## 5. 完整 Néron symbol 中的 Hecke 投影

不能先在坏 $\mathcal X$ 上把“水平交数”当成 Hecke 自伴。
正确做法是先将 degree-zero 除子补成 admissible 除子：
$\widehat D=\overline D+\Phi(D)$，使它与每个垂直分量交0。

取原 Hecke 对应 normalization 的共同正则模型，
两投影为 $f,g$。任一垂直曲线 $F$ 满足
$$
f^*\widehat D\cdot F=\widehat D\cdot f_*F=0;
$$
若 $f(F)$ 为点则右边为0，若为分量则由 admissibility 为0。
所以拉回仍 admissible。整曲面的投影公式给完整 Néron symbol 的
pull–push 恒等式。原 $T_q$ 的 transpose 是同一个 correspondence cycle：
dual isogeny 的复合为 $[q]$，其47标记作用是中心标量 $q$，
仍为同一个 necklace。因此对这里的原除子代表有准确等式
$$
I_{47}(Bu_4,T_nBu_{16})
=I_{47}(u_4,T_nB^2u_{16}).
\tag{16}
$$
这不是仅在 Picard 类上的替换，因而没有遗漏 principal-function 项。

$T_qC_\infty=(q+1)C_\infty$，故
$$
T_nB^2u_{16}=23\,T_nB^2y_{16}
$$
是总度0的纯 CM cycle。其 char0 支撑与 $y_4$ 分离，
且由第2节与尖点在47亦不交。
故(16)的水平部分准确为
$$
23^2\bigl(y_4\cdot T_nB^2y_{16}\bigr)_{47}
=23^2\mathcal D_qH(n),
\tag{17}
$$
这里用
$$
B^2=(q^2+3q+1)-2(q+1)T_q+T_{q^2},
$$
以及 $(n,q)=1$。所有非循环 $q^2$ 核均保留。

## 6. 原尖点列和精确垂直修正

[R28](R28-bad-reduction-norm-interface.md) 的原五分量均 multiplicity1，
其负交矩阵为
$$
L=-M=46\operatorname{diag}(1/e_i)-12vv^{\mathsf t},
\qquad v_i=1/e_i.
\tag{18}
$$
若 $z_i=D\cdot C_i$、$\sum_i z_i=0$，
則
$$
\Phi(D)=\sum_i\frac{e_i z_i}{46}C_i
$$
满足 $(\overline D+\Phi(D))\cdot C_i=0$；
完整 Néron 修正是正号
$$
I_{47}(D,E)=(\overline D\cdot\overline E)
+\frac1{46}\sum_i e_i z_iw_i.
\tag{19}
$$

[R30](R30-cusp-balanced-component-correction.md) 的尖点列准确为
$$
c_i=C_\infty\cdot C_i=\frac6{e_i}.
\tag{20}
$$
为指出此处实际几何输入：compactified Tate/Igusa cusp 位于原中央
ordinary Igusa 分量 $A$，diamond 作用在该 cusp 上自由。
$C_\infty$ 在预模型只遇 $A$，
而 $\operatorname{mult}(A)=23,\deg C_\infty=23$，
故 $C_\infty\cdot A=1$。
消去 [R28] 的 $D,E$ 后，
$A^2=-1/3,\ A\cdot F_i=2/e_i$；
最后 $C_i$ 的总拉回在 $A$ 的系数为 $6/e_i$，得到(20)。
这里只使用已登记的原 compactification，未假设尖点在47 étale。

现在取(16)的两个槽。
写 $b_i=[E_i]T_nB^2[E_{16}]$，则 $\sum_i b_i=0$，并且
$$
z_i=23\delta_{i,4}-c_i,\qquad w_i=23b_i.
$$
代入(19)，$e_4=2$，得
$$
\frac1{46}\sum_i e_i(23\delta_{i,4}-c_i)23b_i
=23b_4-3\sum_i b_i=23b_4.
\tag{21}
$$
原 cusp 项确实在总度0的完整 Brandt 列上消去。
$b_4=\mathcal D_qb(n)$，合(17)即为(3)。

## 7. 可直接消费的后继输入与范围

(4)只需枚举 $B_A=47^3s$；
(5)可以用五维实际 Brandt 矩阵读取，
特别是 $T_q^2=T_{q^2}+qI$ 可避免枚举 $q^2$ 的全部核。
任何实现仍需标定 $j=1728$ 的唯一 $e=2$ 基向量，
并由 $T_2[E_4]=[E_4]+2[E_{16}]$ 标定原第二向量；
不能从不明的矩阵排序猜 $y_{16}$。

本文只支付原坏47处的理论公式。2处、实际全局高度值、
八个 CM 管内部排点及所有充分大 $p$ 的主目标，仍接着做。

## 文献与已付来源

- Bas Edixhoven、Pierre Parent，*Semistable reduction of modular curves associated with maximal subgroups in prime level*，
  Documenta Mathematica 29 (2024)，原正则模型及分量交矩阵；这里完整消元见 R28、R30。
  [正式全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。
- Benedict H. Gross，*On canonical and quasi-canonical liftings*，
  Inventiones Mathematicae 84 (1986)，§§2–5，特别是 canonical 端态滤过及 Proposition 4.3。
  [原文附录扫描](https://archive.mpim-bonn.mpg.de/id/eprint/3578/1/preprint_1985_30.pdf)，PDF末尾六页。
- Benedict H. Gross、Don B. Zagier，*Heegner points and derivatives of L-series*，
  Inventiones Mathematicae 84 (1986)，III §§5–8 的 fine deformation 和 isogeny 计重；
  [作者全文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01388809/fulltext.pdf)。
  本文的 level47 bad coarse 尺度单独由 R1074 支付，没有套用无level的 $j$-line 高度。
