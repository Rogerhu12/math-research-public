# R154：一条真实 Miller 链的双变量搬运与 Hecke 范数复用

日期：2026-11-12。**状态：已证明。** 本文给出同一实际 Poincaré 范数约定下的双变量搬运公式，证明一条已保存主函数的 Miller 链如何经真实对应复用于第二变量，并明确相交支撑及有限精度求值的边界。

这不是已完成的全局高度数值。它消除了每换一个 Hecke 第二变量就重做一次大整数 Jacobian 乘法的需要，但仍保留实际主函数、对应范数、形式终点换框和 R148 的全局截面坐标。

## 1. 范数纤维与主除子的准确方向

设 $k/\mathbb Q_\ell$ 为有限扩张，$X/k$ 光滑射影几何连通，$J=\operatorname{Pic}^0(X)$。使用 R18、R33、R148 的同一双扩张
$$\mathcal P_{[A],[D]}=\operatorname{Norm}_A\mathcal O_X(D)$$
及其相容对数 $\lambda$。对纯标量 $c$，约定
$$\lambda(c\,e)=\log_\ell(c)+\lambda(e).$$
标量对数的分支始终固定。

若度零除子 $A,D$ 支撑不交，记 $e(A,D)$ 为实际有理截面 $1$ 在上述范数纤维中的元素。对有理函数 $f$ 和避开其零极的除子 $D=\sum_Pn_PP$，置
$$f(D)=\prod_P\operatorname N_{k(P)/k}(f(P))^{n_P}.\tag{154.1}$$
所有除子及函数均允许在有限扩域上展开后作 Galois 下降；范数中的闭点次数不可漏掉。

**引理 154.1。** 若 $A'=A+\operatorname{div}f$，则由实际主函数给出的纤维识别将
$$e(A',D)\longmapsto f(D)e(A,D).\tag{154.2}$$
若 $D'=D+\operatorname{div}g$，则同样将
$$e(A,D')\longmapsto g(A)e(A,D).\tag{154.3}$$

**证明。** 第二式直接来自
$$\mathcal O_X(D')=g^{-1}\mathcal O_X(D)
\xrightarrow{\ \cdot g\ }\mathcal O_X(D).$$
其有理截面 $1$ 的像为 $g$，沿 $A$ 的范数正是 $g(A)$。第一式由同一双扩张的规范对称性得到；等价地，在除子范数的符号定义中，
$$\langle f s_A,s_D\rangle=f(\operatorname{div}s_D)
\langle s_A,s_D\rangle.$$
这些符号关系彼此相容正是 Weil 互反律；所用对称性与 R148 的实际范数约定一致。证毕。

因此，若输入元素在旧框架中的坐标为 $u$，且新第一变量代表是 $A'=A+\operatorname{div}f$，则新坐标是 $u/f(D)$。这与已算出的 Miller 终点换框方向一致，不能把除法改为乘法。

## 2. 双变量搬运公式

固定正整数 $m$ 及四个度零除子 $A,D,A_Y,D_Y$，并给出**实际有理函数**
$$\operatorname{div}f=mA-A_Y,\qquad
\operatorname{div}g=mD-D_Y.\tag{154.4}$$
先假设第一组 $A,A_Y$ 的全部支撑与第二组 $D,D_Y$ 的全部支撑不交。于是下列函数范数均有定义。

**定理 154.2。** 在真实双扩张的两次 $[m]$ 群律下，
$$[m]_1[m]_2e(A,D)
=f(D)^m g(A_Y)\,e(A_Y,D_Y).\tag{154.5}$$
因而
$$\boxed{
m^2\lambda(e(A,D))
=\lambda(e(A_Y,D_Y))
+m\log_\ell f(D)+\log_\ell g(A_Y).
}\tag{154.6}$$
若 $\ell\nmid m$，由右端求左端不会因除以 $m^2$ 损失 $\ell$ 进精度。

**证明。** 两次群律先把 $e(A,D)$ 送到 $e(mA,mD)$。由
$$A_Y=mA+\operatorname{div}(f^{-1}),$$
引理 154.1 将这个元素变成
$$f(mD)e(A_Y,mD)=f(D)^m e(A_Y,mD).$$
再用 $D_Y=mD+\operatorname{div}(g^{-1})$ 将其变成 (154.5)。双扩张对数在两个群律上均相加，所以作用两次 $[m]$ 乘以 $m^2$，即得 (154.6)。证毕。

若反过来先搬第二变量，会得到
$$m^2\lambda(e(A,D))
=\lambda(e(A_Y,D_Y))
+m\log_\ell g(A)+\log_\ell f(D_Y).\tag{154.7}$$
两式的等价是准确的符号校验。由 Weil 互反律，
$$f(mD-D_Y)=g(mA-A_Y),$$
即
$$f(D)^m g(A_Y)=g(A)^m f(D_Y).\tag{154.8}$$
所以两条搬运路径给的是同一个实际纤维元素。

把 $f$ 或 $g$ 乘一个非零常数不改变各式，因为被评价的除子次数均为零。这只消除主函数的常数自由度，不允许任意改变起始或终点的线丛框架。

## 3. 对应的主函数范数及伴随

设 $T$ 为若干有限对应的整系数组合。对一个不可约分量的规范化 $C$，记两个投影为 $\pi_1,\pi_2:C\to X$。其除子作用与转置分别是
$$T(D)=\pi_{2*}\pi_1^*D,\qquad
T^\dagger(D)=\pi_{1*}\pi_2^*D.$$
定义有理函数的对应范数
$$N_T(h)=\operatorname N_{k(C)/\pi_2^*k(X)}(\pi_1^*h).
\tag{154.9}$$
对多个分量取乘积，对负整系数取负次幂。对角分量给通常函数本身。因此这允许 $aT_n+c\Delta$，不要求对应没有对角分量。

**引理 154.3。** 有
$$\operatorname{div}N_T(h)=T(\operatorname{div}h),\tag{154.10}$$
而在合法求值的支撑上，
$$\boxed{(N_T h)(D)=h(T^\dagger D).}\tag{154.11}$$

**证明。** 有限映射下函数范数的赋值是各上方点赋值按剩余域次数的和，故其除子是主除子的推前。再用函数拉回与主除子拉回相容，得 (154.10)。

对一个闭点 $P$，沿 $\pi_2$ 的有限代数取行列式范数，再对 $k(P)/k$ 取范数。范数传递性把这个值写成 $\pi_2^{-1}(P)$ 各点上的 $\pi_1^*h$ 值，带全部长度和剩余域次数。沿 $\pi_1$ 推前，正好得到 $h(T^\dagger P)$。按除子系数乘起来即得 (154.11)。这一证明包含分歧长度，没有假定投影处处 étale。证毕。

对对称 Hecke 对应，$T^\dagger=T$。因此计算 $N_{T_2}h$ 在一个 CM 点的值，只需在它的真实三次 Hecke 除子上求 $h$ 的范数；重合的分支须保留实际重数。

## 4. 同一条链复用于 Hecke 第二变量

设已得到第一式 (154.4) 的函数 $f$。另选相同类的实际代表
$$A'=A+\operatorname{div}h,\qquad
A_Y'=A_Y+\operatorname{div}k,\tag{154.12}$$
其中 $h,k$ 都已给定为有理函数。设置
$$D=T(A'),\qquad D_Y=T(A_Y').\tag{154.13}$$
则
$$\operatorname{div}\!\left(\frac{fh^m}{k}\right)=mA'-A_Y',$$
所以可以准确选取
$$\boxed{g=N_T\!\left(\frac{fh^m}{k}\right).}\tag{154.14}$$
由引理 154.3，$\operatorname{div}g=mD-D_Y$，第二条长度约 $\log m$ 的 Jacobian 乘法链因此不再需要。

代入定理 154.2：
$$\boxed{
\begin{aligned}
m^2\lambda(e(A,T A'))
={}&\lambda(e(A_Y,T A_Y'))\\
&+m\log_\ell f(T A')\\
&+\log_\ell\left(\frac{fh^m}{k}\right)(T^\dagger A_Y).
\end{aligned}}
\tag{154.15}$$
这里仍须选择支撑使两个范数合法。最后一行应先把 $fh^m/k$ 作为同一个有理函数求值，不能在某个因子单独有零极时拆成三个未定义的数。

这对含对角的 $T$ 尤其重要：$f$ 在 $A_Y$ 上本来有极点，$k$ 在同一支撑上消去相应极点。直接写 $\log f(A_Y)-\log k(A_Y)$ 会产生两个未定义量；实际商函数及线丛同构却有定义。选两组不交的形式代表 $A_Y,A_Y'$，正是保留这个相消的便利做法。

若只知道 $[D]=T[A]$ 在 $J(k)\otimes\mathbb Q$ 中相等，尚不能使用 (154.14)：须先清掉明确的分母及挠点，给出所用整数倍的真正主函数。仅有对数坐标相等也不能替代这一步。

## 5. 已运行的 AddFlip 链正好保存这个函数

沿用 R121 的度零代表 $A_P=E_P-D_0$。每次 AddFlip 算得
$$R=-(P+Q),\qquad
\psi=s/f_0^3,\qquad
\operatorname{div}\psi=A_P+A_Q+A_R.$$
设整数标签为 $n_P,n_Q$，并已保持
$$\operatorname{div}F_P=n_PA-A_P,\qquad
\operatorname{div}F_Q=n_QA-A_Q.$$
那么 $n_R=-n_P-n_Q$，且
$$\boxed{F_R=(F_PF_Q\psi)^{-1}}\tag{154.16}$$
满足 $\operatorname{div}F_R=n_RA-A_R$；逐项相加主除子即得。

初始 $P=B$ 取 $n_B=1,F_B=1$。真实负点由
$$\operatorname{div}(a/f_0^2)=A+A_{-B}$$
给 $F_{-B}=(a/f_0^2)^{-1}$。因此链到整数 $m$ 的终点时，实际得到
$$\operatorname{div}F_{\rm old}=mA-A_{\rm old}.$$
若端点换框函数满足 $\operatorname{div}g_{\rm tr}=A_Y-A_{\rm old}$，则
$$\boxed{f=F_{\rm old}/g_{\rm tr}.}\tag{154.17}$$
这与程序的坐标 $u_{\rm new}=u_{\rm old}/N(g_{\rm tr})$ 同向。

保存每一步真实三次截面 $s$ 在固定 $H^0(3\mathcal L)$ 基中的系数、负点二次截面、初始 $f_0$ 和终点换框，就得到 $f$ 的有限直线程序：只含乘法、除法及整数次幂，无须展开次数随 $m$ 爆炸的有理函数。

对任何新的合法除子，按同一递推求各步实际范数即可重建 $f(D)$。只保存一个既定除子上的数值，或某一组形式方向的三阶展开，不足以在任意新除子上重新求值；保存主截面系数解决的是这一问题。

当前层41模型中 $H^0(3\mathcal L)$ 的秩为325，每步为325个 $R_2$ 系数。454步的主函数数据可压缩保存，不需要每步的大评价矩阵。R121 点哈希和原随机状态继续逐步约束同一链。

## 6. 相交支撑及有限精度的边界

### 6.1 改换除子必须保留范数

有限个支撑可以用曲线上的移动引理避开。实际算法中，若
$$A_Y=E_1-D_1,\quad A_Y'=E_2-D_2,\quad D_i=\operatorname{div}v_i,$$
并已求得 $\operatorname{div}r=E_2-E_1$，则 $k=r\,v_1/v_2$ 恰满足 (154.12)。这是实际换框函数，不能仅比较理想空间维数。

对于 R148 指定的相交纤维元素，先按其明确局部生成元应用这个换框同构，再用 (154.15)。碰撞处的首单位、典范微分尺度和规范截面坐标均保留，不会因为改成不交代表而自动变为一。

### 6.2 模 $\ell^N$ 的非单位除法

若所有中间求值均为整单位，直线程序和范数乘除保持模 $\ell^N$ 精度。当前 R151 的54个形式移动点已逐步使用这个条件。

换成新 CM 支撑时，最终 $f$ 在该点为单位，并不保证每个中间主截面的值都是单位。若一个值被 $\ell$ 整除，直接在模 $\ell^N$ 表示中除以它会损失精度；不能因后面理论上相消就宣称恢复全部 $N$ 位。

合法处理包括增加实际所需精度、换到在该支撑为单位的线丛框架并计算转换，或在局部函数层面准确消去共享零极因子。最后一种须保留真实局部因子，不能只相减数值赋值。

一个简单零公式说明需要的输入。设 $s(t)=\sum_{j\ge0}s_jt^j$ 为整幂级数，$\alpha\in\ell R$ 是已知简单零，$s(t)=(t-\alpha)u(t)$。则
$$u(0)=\sum_{j\ge1}s_j\alpha^{j-1}.\tag{154.18}$$
证明是对单项式使用
$$\frac{t^j-\alpha^j}{t-\alpha}
=t^{j-1}+t^{j-2}\alpha+\cdots+\alpha^{j-1},$$
再由 $s(\alpha)=0$ 相加。因 $\alpha\in\ell R$，模 $\ell^N$ 只需 $j\le N$ 的项。因此在47处保留四位时，这种简单因子相消需要第四阶局部系数；已有前三阶不能自动当作足够。重根和闭点需另保留真实重数与剩余域范数。

### 6.3 形式终点仍须使用同一框架

即便 $[A_Y],[D_Y]$ 都在形式群内，(154.6) 的首项仍是指定范数元素 $e(A_Y,D_Y)$ 的值。若 R141/R145 使用另一组 Abel 代表，须给出其主函数并取范数。

R140/R141 的真实 Hecke 修正仍应加入该同一框架。仅具有相同 Lie 坐标的任意解析截面不产生相同高度；本文没有将这个转换省略为未知常数。

## 7. 对当前层41计算的作用

取 $m=\#J(\mathbb F_{47})$，R121 已证明 $m\equiv9\pmod{47}$，故 $m^2$ 为47进单位。正在完成的同一 Miller 链给 (154.17)，其主截面直线程序可用于后续真实 CM 除子和 Hecke 像。

先处理 $T_2$：R79 已证明 $Q_2=2P_{-7}+Z_{-8}$，R147/R148 已确定 $P_{-12}$、基点及对角相交单位。对应范数须在这些真实点和实际 Hecke 邻居上求值，保留三重或二重分支。

本结果完成第二变量复用的代数公式。数值上仍须补齐整条直线程序，计算指定 CM/典范除子的范数及碰撞转换，把形式终点放入同一相容框架，再将 R148 的全局规范截面送入该纤维。全部54个高度差、全局系数及 QC 圆盘共同根仍需继续。

## 依赖

- [R18](R18-norm-rigidification-interface.md)、[R33](R33-hecke-norm-and-component-data.md)：实际度零范数与同一符号。
- [R140](R140-integral-hecke-balancing-and-cubic-height-interface-at47.md)、[R141](R141-actual-canonical-t3-hessian-and-integral-height-correction-at47.md)、[R145](R145-actual-hecke-compatible-formal-poincare-value-at47.md)：同一形式框架、真实修正和精度。
- [R148](R148-global-correspondence-section-with-diagonal-and-basepoint.md)：全局截面、局部生成元和800倍率。
- notes/2026-11-12-p41-miller-transport-checkpoint.md、notes/2026-11-12-p41-miller-all54-jets-checkpoint.md：真实负和链、端点主函数及恢复数据。

双变量公式、对应范数复用、负和递推和简单零精度公式均已在正文直接证明。
