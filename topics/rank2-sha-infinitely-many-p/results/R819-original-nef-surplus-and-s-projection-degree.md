# R819 — 原 nef 余量、S 投影次数与低亏量分量的精确界

后继：[R823 原最小面的完整截面及真实 Serre 行](R823-original-minimal-nef-face-complete-sections-and-serre-rows.md)给最小类的全整基和原r2条件下p≤120D−421；其余正余量类不因此排除。

后继：[R825 全 nef 上缺量及所有有界 S 次数区域](R825-original-nef-upper-gap-and-bounded-s-degree-exclusion.md)给统一实际p界；未排e随D增长的临界区。

日期：2026-11-15。**状态：本篇的全 nef 不等式、精确非负分解、等号类及原分量推论已证明。** 所用曲面、十九角、两个铅笔和全部重数均为 [R815](R815-complete-original-mori-nef-cones-and-s-fibration.md) 的原对象。数值界不代替原接触矩阵、同一修正的返回或 Cartier 非零性。

本篇把 R815 的固定零纤维亏量下界加强为
\[
\boxed{\quad C^2\ \ge\ (b-m)e+bm,\qquad
b=C\cdot f,\quad m=C\cdot f_0,\quad e=C\cdot H_+.\quad}
\tag{1}
\]
这里 \(H_+\) 是实际 \(S=a(t)Y/7\) 铅笔的纤维类，因此在非纤维的不可约曲线上，\(e\) 正是 \(S\) 投影的总次数。不是另选一个有较小次数的有理函数。

## 1. 原十九角和记号

负侧四条链记为
\[
\mathcal N=\{0,\alpha_+,\alpha_-,1\},\qquad
(n_0,n_{\alpha_+},n_{\alpha_-},n_1)=(4,4,4,3);
\]
正侧两链为 \(\mathcal P=\{d,\infty\}\)，长度各二。
使用原全变换的正交异常基 \(E_{ij}\)，写
\[
C=bS_0+(u+4b)f-\sum_{i,j}\mu_{ij}E_{ij},
\qquad
\kappa=C^2=4b^2+2bu-\sum_{i,j}\mu_{ij}^2 .
\tag{2}
\]
本篇首先允许任意实 nef 类，不预设其有不可约代表。
R815 的完整 nef 条件是
\[
b\ge0,\quad
\mu_{i1}\ge\cdots\ge\mu_{in_i}\ge0,\quad
\sum_j\mu_{ij}\le b,\quad
u\ge\mu_{d1}+\mu_{\infty1}.
\tag{3}
\]
特别 \(u\ge0\)。

同一原严格纤维与原 \(S\) 纤维给
\[
f_0=f-\sum_{j=1}^4 E_{0j},\qquad
H_+=S_0+4f-\sum_{i\in\mathcal N}E_{i1},
\]
从而
\[
m=b-\sum_j\mu_{0j},\qquad
e=u+4b-\sum_{i\in\mathcal N}\mu_{i1}.
\tag{4}
\]
所以 \(0\le m\le b\)。以下置
\[
A=b-m,\quad
v_0=A-\mu_{01},\quad
v_i=b-\mu_{i1}\ (i\in\mathcal N\setminus\{0\}),\quad
\sigma=u-\mu_{d1}-\mu_{\infty1}.
\tag{5}
\]
(3) 逐项给它们非负，且准确有
\[
\boxed{e-m=u+v_0+\sum_{i\in\mathcal N\setminus\{0\}}v_i\ge0.}
\tag{6}
\]

## 2. 精确非负分解

为零链定义
\[
D_0=\sum_j\mu_{0j}(\mu_{01}-\mu_{0j})\ge0.
\tag{7}
\]
对于其余五条链定义
\[
D_i=b\mu_{i1}-\sum_j\mu_{ij}^2
=\mu_{i1}\!\left(b-\sum_j\mu_{ij}\right)
+\sum_j\mu_{ij}(\mu_{i1}-\mu_{ij})\ge0.
\tag{8}
\]
每一项都来自原 (3)，没有使用曲线分解、特征零或数值抽样。

**定理 1。** 对全部上述 nef 类，有恒等式
\[
\boxed{
\begin{aligned}
\kappa-\bigl((b-m)e+bm\bigr)
={}&m\!\left(u+\sum_{i\in\mathcal N\setminus\{0\}}v_i\right)
+b\sigma+D_0\\
&+\sum_{i\in\mathcal N\setminus\{0\}}D_i
+\sum_{i\in\mathcal P}D_i .
\end{aligned}}
\tag{9}
\]
特别 (1) 成立，并有较强的
\[
\kappa-(2bm-m^2)\ge
(b-m)(e-m)+m\!\left(u+\sum_{i\ne0,\ i\in\mathcal N}v_i\right).
\tag{10}
\]

**证明。** 零链总重数为 \(A\)，所以
\[
A^2-\sum_j\mu_{0j}^2=Av_0+D_0.
\]
其余三条负链分别满足
\[
b^2-\sum_j\mu_{ij}^2=bv_i+D_i.
\]
正侧两链则有
\[
2bu-\sum_{i\in\mathcal P,j}\mu_{ij}^2
=bu+b\sigma+\sum_{i\in\mathcal P}D_i.
\]
将三式代入 (2)，并用
\(4b^2-A^2-3b^2=2bm-m^2\)，得
\[
\kappa-(2bm-m^2)
=Av_0+b\sum_{i\ne0}v_i+bu+D_0+\sum_{i\ne0}D_i
+b\sigma+\sum_{i\in\mathcal P}D_i.
\]
再减去由 (6) 给出的
\(A(e-m)=Av_0+A\sum_{i\ne0}v_i+Au\)，余项就是 (9)。
所有余项非负，故各不等式同时成立。证毕。

若 \(b>m\)，(1) 等价于实际投影次数界
\[
\boxed{
e\le \frac{\kappa-bm}{b-m}
=m+\frac{\kappa-(2bm-m^2)}{b-m}.}
\tag{11}
\]
当 \(b=m\) 时，只读原不等式 \(\kappa\ge b^2\)，不作除零运算。
当 \(m=0\) 时，(1) 仍给 \(\kappa\ge be\)，但下一节的等号分类不用于此边界。

## 3. 正亏量时的全部等号类

**定理 2。** 设 \(0<m<b\)。等号
\(\kappa=(b-m)e+bm\) 成立，当且仅当存在
\(j\in\{1,2,3,4\}\)，使全部原重数为
\[
u=0,\qquad \boldsymbol\mu_d=\boldsymbol\mu_\infty=0,
\]
\[
\boldsymbol\mu_i=(b,0,\ldots,0)
\quad(i=\alpha_+,\alpha_-,1),
\]
\[
\boldsymbol\mu_0=
(\underbrace{(b-m)/j,\ldots,(b-m)/j}_{j\text{ 项}},0,\ldots,0).
\tag{12}
\]
相应地
\[
\boxed{
e=b-\frac{b-m}{j},\qquad
\kappa=b^2-\frac{(b-m)^2}{j}.}
\tag{13}
\]

**证明。** 由 \(m>0\) 和 (9)，等号先迫
\(u=0\) 及三个 \(v_i=0\)。
于是正侧重数全零；另外三负链的首项为 \(b\)，由总和至多 \(b\)
其余项全零。零链总和 \(A>0\)，故首项正。
\(D_0=0\) 迫每个非零项都等于首项；单调性使它们恰为前 \(j\) 项。
总和 \(A\) 给其值 \(A/j\)。代回 (4)、(2) 就是 (13)。

反之，(12) 的每一个实类都满足全部 (3)，(9) 右侧逐项为零。
故没有遗漏的等号类。证毕。

对整格类，还须 \(j\mid b-m\)；这只是整重数条件。
没有由 (12) 推断该类一定有光滑或几何不可约代表。
\(j=1\) 正好回到 R815 的最小类
\(bH_++mE_{01}\)、\(\kappa=2bm-m^2\)、\(e=m\)。
另外三种等号类说明 (1) 在原数值 nef 锥上已经尖锐，
不能只靠重复 (3) 将右端统一加强。

## 4. 反典范次数及实际曲线的属约束

记 \(\chi=-K_XC\)。由原 Hirzebruch 曲面及十九次吹起，
\[
\chi=6b+2u-\sum_{i,j}\mu_{ij}.
\tag{14}
\]
对另三条负链令 \(m_i=b-\sum_j\mu_{ij}\ge0\)，则
\[
\boxed{
\chi
=2b+m+\sum_{i\in\mathcal N\setminus\{0\}}m_i
+\left(2u-\sum_{i\in\mathcal P,j}\mu_{ij}\right)
\ge2b+m.}
\tag{15}
\]
最后括号非负，因为每条正链长度二、单调，
其总和至多两倍首重数，而两个首重数之和至多 \(u\)。

若 \(C\) 是实际几何不可约曲线，伴随公式因而给
\[
p_a(C)=1+\frac{\kappa-\chi}{2}
\le1+\frac{\kappa-2b-m}{2}.
\tag{16}
\]
这读取的是算术属；正规化的几何属还须减去全部奇点的
\(\delta\) 不变量。不能把本篇的数值等号类预先当成光滑曲线。

## 5. 对原强接触因子与同 R 分量的应用

### 5.1 原 r=2 因子

R792/R797/R810 的实际因子零角满足 \(m_F=3\)。
剩余窗口中 \(b\ge5\)，故 (11) 给
\[
\boxed{
\kappa\ge(b-3)e+3b,\qquad
e\le3+\frac{\kappa-(6b-9)}{b-3},\qquad
\chi\ge2b+3.}
\tag{17}
\]
例如沿任何候选序列，若
\(\kappa-(6b-9)\le L(b-3)\)，则实际 \(S\) 次数
\(e\le3+L\)。因此固定 \(L\) 的近最小自交区域确实只需处理
有界 \(S\) 次数；这是从整个原 nef 锥得到的统一结论，
不限定某个已扫描的 \(b\)。

这个重排不排除这些低次数曲线对真实轴的长接触。
原 \(H(t)\) 的移动根、全部十九角、\(h\ge\kappa+14\)、
同一 \(R\) 的全部 normal/carry 条件仍须继续使用。

### 5.2 同一修正的两种全局分量

R815 已证明：R808 的两个原点光滑支若属于不同的全局几何分量，
各分量定义在原剩余域上且 \(m=1\)；若属于同一分量，则该分量 \(m=2\)。
它们都是原 nef 类。因此各自准确满足
\[
\begin{array}{c|c|c}
m&\text{自交下界}&\text{反典范下界}\\ \hline
1&\kappa\ge(b-1)e+b&\chi\ge2b+1\\
2&\kappa\ge(b-2)e+2b&\chi\ge2b+2.
\end{array}
\tag{18}
\]
投影次数的除法式只在 \(b>m\) 时使用。

若两支同属几何不可约分量 \(A\)，R808 给该点
\(\delta_P(A)=h\)。由几何属非负、(16) 及 \(m=2\)，另有
\[
\boxed{\kappa_A\ge2h+2b_A.}
\tag{19}
\]
若它们属于不同分量，则该点的贡献是两个分量间的交数 \(h\)；
不能对任一单独光滑分量冒用 (19)。

(17)–(19) 均保留原分量及原 \(S\) 投影。
它们不把局部分裂改成全局分解，不把不同候选的数值界混成同一个修正，
也不证明原强窗或原第三精度已经不存在。

## 6. 证明范围与后续接口

整个论证只用原全 nef 条件、交数和伴随公式，适用于 R815
所允许的所有特征；在惰性原域的两个共轭链相等子锥上同样成立。
没有使用数学程序、有限素数扫描、外来曲面或未证整半群生成。

已支付的是：固定 \(m\) 时，自交超过最小值的余量准确控制原
\(S\) 投影次数，并以 (9) 记录每一处链的损失。
后继可据此分别处理有界 \(S\) 次数区域和其余区域。
必须另证的是各区域中原指定接触/完整余像的排除，
以及带权 Cartier 类与同一 \(R\) 的实际配对。主目标仍未完成。

依赖：
[R815 全原 nef 锥与 S 铅笔](R815-complete-original-mori-nef-cones-and-s-fibration.md)；
[R808 同修正二支](R808-original-third-precision-corrector-split-branches-and-near-normal-jet.md)；
[R810 原 r2 四次排除与零角](R810-original-quartic-all-prime-exclusion-and-complete-zero-chain.md)。
