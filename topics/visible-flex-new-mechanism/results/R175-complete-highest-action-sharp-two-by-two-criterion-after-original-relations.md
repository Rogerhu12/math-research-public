# R175：原式关系之后，完整最高层的锐利二阶矩阵判据

**状态：已证明；纸面恒等式与已付有限真实路径构造，不新增研究计算。**

[R174](R174-nine-original-character-relations-and-rejection-of-the-positive-outer-point.md)
的最高系数关系使一般四单项 Gram 问题进一步化简：在这些原式关系下，
完整最高层对所有真实平端路径非负，当且仅当两条纯 h 条件和一个明确的
二阶矩阵半正定条件成立。证明保留全部面积项、速度四次项与边界导数。

必要性使用 [R148](R148-sharp-one-dimensional-highest-action-positivity.md)
的纯 h 锐利门及 [R169](R169-power-path-sharp-quartic-gate-and-real-Gram-directions.md)
的真实幂路径门；充分性由下面的完整恒等式给出。
旧 R173 指定点已经被原函数关系排除，本结果不重测那个点。

## 1. 记号和定理

沿用 [R165](R165-prescribed-h-quadratic-highest-action-and-loglinear-frequency-gate.md)
的十数
$$
(a,b,c,d,e,f,g,j,\ell,m)
=\nu(90,91,94,96,97,99,100,101,103,104).
$$
本节 a、b 是最高层参数，与静态两参数区分。设
$$
r=\log h,\qquad v=r',\qquad z=v'+v^2,\qquad h>0.
$$
完整最高层密度为
$$
\begin{aligned}
L_4=e^{-2r}\{&
az^2+\ell v^4+d(k'')^2+(cz+ev^2)kk''+fvk'k''\\
&+(gv^2-fz)(k')^2+(jv^3-evz)kk'
 +(bz^2+mv^4)k^2\}.
\end{aligned}                                                     \tag{1}
$$
真实水平约束始终为 $\omega'=k'/(2h)$；这里没有给历史量独立自由度。

R174 已付五条原式关系
$$
c=-b,\quad d=b/4,\quad e=-2b/3-2f,\quad
j=-4b/3-2f-4g,\quad m=3b+4f+4g.                      \tag{2}
$$
以下全部结论以 (2) 为前提。定义
$$
\gamma=\frac{23b}{12}+2f+g,\qquad
\kappa=\frac{3b}{4}+\frac{3f}{2},\qquad
M=\begin{pmatrix}b/4&\kappa\\\kappa&\gamma\end{pmatrix}. \tag{3}
$$

**定理。** 对所有有限区间上的光滑正 h、实 k 平端路径，
$\int L_4\ge0$，当且仅当
$$
\boxed{\quad a\ge0,\qquad\ell+\frac{25a}{9}\ge0,\qquad M\succeq0.\quad}
                                                                    \tag{4}
$$
两端 h、k 各自常值，但不要求左右值相同。这是原完整开路径的测试类；
每条路径都通过积分给出真实 $\omega$。

矩阵条件准确等价于
$$
b\ge0,\qquad\frac{23b}{12}+2f+g\ge0,\qquad
bg-\frac{b^2}{3}-7bf-9f^2\ge0.                        \tag{5}
$$
行列式是最后一式左边的四分之一。若 b>0，可简化为
$$
g\ge b/3+7f+9f^2/b.                                  \tag{6}
$$
若 b=0，准确条件是
$$
f=0,\qquad g\ge0.                                    \tag{7}
$$
不在退化端除 b，也不无条件要求 f、g、$\ell$ 各自非负。

## 2. 保全部边界项的准确恒等式

令
$$
u=k/h^2,\qquad \psi=h u'=h^{-1}(k'-2vk),               \tag{8}
$$
$$
\mathcal B=
\frac{10a}{9}e^{-2r}v^3+
\frac b3e^{2r}v^2u u'-f v\psi^2.                      \tag{9}
$$
则在 (2) 下逐点成立
$$
\boxed{\begin{aligned}
L_4={}&e^{-2r}\left\{
a\left(v'-\frac23v^2\right)^2+
\left(\ell+\frac{25a}{9}\right)v^4\right\}\\
&+\begin{pmatrix}\psi'&v\psi\end{pmatrix}
M\begin{pmatrix}\psi'\\v\psi\end{pmatrix}
+\mathcal B'.
\end{aligned}}                                                     \tag{10}
$$
平端给 v=0 且所有量有限，所以 $\mathcal B$ 两端为零。
(10) 直接证明充分性，并说明 k=K h² 时完整 k 二次部分准确为零；
不能将这一事实只解释为加速度主部退化。

先验证纯 h 部分：
$$
\begin{aligned}
e^{-2r}\{a(v'+v^2)^2+\ell v^4\}
={}&e^{-2r}\left\{
a\left(v'-\frac23v^2\right)^2+
\left(\ell+\frac{25a}{9}\right)v^4\right\}\\
&+\left(\frac{10a}{9}e^{-2r}v^3\right)'.
\end{aligned}                                                     \tag{11}
$$
两边平方项之差为
$e^{-2r}\{(10a/3)v'v^2-(20a/9)v^4\}$，恰是已列导数。

记 (1) 中所有含 k 的项为 $L_k$。用
$$
k'=e^{2r}(u'+2vu),\qquad
k''=e^{2r}\{u''+4vu'+2(v'+2v^2)u\}
$$
并完整代入 (2)，得
$$
\begin{aligned}
e^{-2r}L_k={}&
\frac b4(u'')^2+(2b+f)v u'u''
+\{(4b+3f+g)v^2-fv'\}(u')^2\\
&+\frac b3v^2u u''+\frac{2b}{3}v(v'+v^2)u u'.
\end{aligned}                                                     \tag{12}
$$
所有 u² 系数准确抵消。这里 $e^{-2r}L_k$ 是变换后除去新权
$e^{2r}$ 的表达式，原密度中的权没有遗漏。

最后两个交叉项满足
$$
\begin{aligned}
&e^{2r}\left\{\frac b3v^2u u''
+\frac{2b}{3}v(v'+v^2)u u'\right\}\\
&\qquad=\left(\frac b3e^{2r}v^2u u'\right)'
-\frac b3e^{2r}v^2(u')^2.
\end{aligned}                                                     \tag{13}
$$
然后对剩余 $(2b+f)e^{2r}v u'u''$ 作带权分部积分，得到
$$
Q_h[k]=\int L_k
=\int e^{2r}\left\{\frac b4(u'')^2+
\left[\left(\frac{5b}{3}+2f+g\right)v^2
-\left(b+\frac{3f}{2}\right)v'\right](u')^2\right\}.    \tag{14}
$$
上述导数在平端全部消失；面积 e、f 的贡献已包含在各系数里。

最后用 $e^r u''=\psi'-v\psi$ 和
$v'\psi^2=(v\psi^2)'-2v\psi\psi'$，得
$$
Q_h[k]=\int\left\{\frac b4(\psi')^2+
2\kappa v\psi\psi'+\gamma v^2\psi^2\right\}.           \tag{15}
$$
从 (13) 到 (15) 追踪边界项，正好为
$$
\left(\frac b3e^{2r}v^2u u'-f v\psi^2\right)'.
$$
这与 (11) 合成完整逐点恒等式 (10)。

## 3. 必要性：本结构中幂路径已经穷尽最高层

若全部真实平端路径的最高 action 非负，先取 k=0。
R148 已证的锐利纯 h 判据给
$a\ge0,\ell+25a/9\ge0$，其中有限平端逼近已经支付，
不使用未截断的奇异相等形状。

再用 R169 的真实路径 k=K h^p，p 为任意实数。
真实 $\omega$ 按 $k'/(2h)$ 积分，p=1 的对数情形保持。
R169 给
$$
A(p)=b+cp+dp^2\ge0,\qquad\Omega(p)\ge0
$$
为全部 p 的必要门。代入 (2)，准确化为
$$
A(p)=\frac b4(p-2)^2,                                \tag{16}
$$
$$
\boxed{\quad\Omega(p)=(p-2)^2T(p),\qquad
T(p)=\frac b{36}p^2+
\left(\frac{4b}{9}+f\right)p+\frac{13b}{9}+f+g.\quad}   \tag{17}
$$
所有 f 与面积项仍在；不能由 (16) 的加速度平方替代 (17)。

关键是同一个 M 给出
$$
\boxed{\quad
T(p)=
\begin{pmatrix}(p-1)/3&1\end{pmatrix}
M\begin{pmatrix}(p-1)/3\\1\end{pmatrix}.
\quad}                                                             \tag{18}
$$
例如一次系数为 $-b/18+2\kappa/3=4b/9+f$，
常数项为 $b/36-2\kappa/3+\gamma=13b/9+f+g$。

由 $\Omega(p)\ge0$，所有 p≠2 都有 T(p)≥0，
连续性补上 p=2。随着 p 遍历实数，(p−1)/3 也遍历实数，
所以 (18) 检查了第二坐标为 1 的全部方向。
二次齐次性及极限补上第二坐标为 0 的方向，恰好给出 $M\succeq0$。
b=0 的一次或常数多项式也被覆盖，没有除零。

因此 (4) 全部必要，与第 2 节的充分性合成充要结论。
这一加强依赖真实原关系 (2)；一般十参数问题仍只有 R169 原来的必要范围。

## 4. 失败的有限真实证书与成功的显式平方

若 M 非半正定，(18) 在某个开区间上为负。
可选一个有限有理 p≠2，使 $\Omega(p)<0$。
R169 的锐利有限平端构造给有限正 h，再取足够大但有限的 K，
使完整最高 action 为负。若要排除完整 0/2/4 action，
按既有证明次序先固定形状及 K，再作足够快但有限的时间缩放，
负最高层压过同一乘子下的低层。无限 K、奇异 h 都不当实际路径。

若 a<0 或 $\ell+25a/9<0$，则用纯 h 的 k=0 反例。
这个分支不一定存在负的 $\Omega(p)$，不能混并两种分离证书。

若 b>0 且 M 半正定，(15) 可直接写成
$$
Q_h[k]=\int\left\{
\frac b4\left(\psi'+\frac{4\kappa}{b}v\psi\right)^2+
\left(\gamma-\frac{4\kappa^2}{b}\right)v^2\psi^2
\right\}.                                                         \tag{19}
$$
余系数非负恰是行列式条件。b=0 时由 (7)，
$Q_h[k]=g\int v^2\psi^2\ge0$。
配 (11) 即得全部最高层准确正证，无需再求一般四阶 Gram 参数。

## 5. 界限与可执行后继

R174 必要外空间的最高五参数 $(a,b,f,g,\ell)$ 现在有完整判据 (4)；
静态两参数另有 R174 的 $\alpha,\beta\ge0$。
二次层、完整时长耦合以及原函数赋值良定义性仍须支付。
最高与静态非负不自动给完整 action 非负，
也不无条件强迫二次层逐点非负。

对下一实际新外点，只读这五个最高数：
失败时输出纯 h 线性门或一个有理 p 的 $\Omega(p)\ge0$ 线性门；
成功时以 (10)/(19) 结清该点的完整最高层，转向欠缺部分。
不重跑旧路径、原式、Gram 或已付外点。

本定理不构造非零真实正字符，不提供实际负成本的任意逆元。
连续等距族、闭合嵌入、全时 reach 和宏观振幅仍是主课题未付部分。

