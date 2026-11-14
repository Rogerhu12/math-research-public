# R73：退化素数 $49019$ 的实际辅助导数与非零矩阵项

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，并完成全部有限域计算。**
固定
$$p=43,\qquad q=49019,\qquad r=859,\qquad A:y^2=x^3-x.$$
R70 已证明 R65 的基类满足
$\operatorname{loc}_{(q)}\kappa_0=0$、
$\operatorname{loc}_{(r)}\kappa_0\ne0$。
本文计算同一个原始 Euler system 的一阶导数，得到
$$
\boxed{\operatorname{loc}_{(q)}\kappa_{(r)}\ne0.}
\tag{73.1}
$$
具体地，在下文固定的 Kummer 数据基中，其坐标为
$$17+26i\in\mathbb F_{43^2}.$$
所以 $r=859$ 已满足 R65 二阶补救所需的两项实际局部条件。
相应 R60 矩阵的两个非对角项均非零。
该坐标尚不是归一化的 $\mathbb F_{43}$ 矩阵条目；
其完整全局基及 Tate 配对归一化另在 R78 处理。

## 1. 先解决局部下降是否可见

记
$$K=\mathbb Q(i),\quad \mathfrak m=(1+i)^3p,\quad T=K(\mathfrak m).$$
R70 的 primary 生成元证明同样适用于模数 $\mathfrak mr$，给
$$
K(\mathfrak mr)=K(A[pr]),\qquad
\operatorname{Gal}(K(\mathfrak mr)/T)=\mathbb F_{r^2}^{\times}.
\tag{73.2}
$$
在其中取 R65 的唯一次数 $p$ 子扩张 $T(r)/T$。
因为 $p\mid r+1$、$p\nmid r-1$，令
$$
H=\ker\left(\mathbb F_{r^2}^{\times}
\xrightarrow{\,b\mapsto b^{(r^2-1)/p}\,}\mu_p\right),
$$
则
$$
T(r)=K(\mathfrak mr)^H,\qquad
\mathbb F_r^\times\subset H,\qquad
\#H=\frac{r^2-1}{p}=17160.
\tag{73.3}
$$

对任何与 $r$ 不同的候选惰性有理素数 $s$，
素理想 $(s)$ 的算术 Frobenius 在 $r$ 挠点上为标量 $-s$。
它在 $\mathbb F_r^\times$ 中，所以在上述 $p$ 次商为一。
特别地，
$$\boxed{T(r)/T\text{ 在 }(q)\text{ 完全分裂。}} \tag{73.4}$$
这不是说完整的 $r$ 除法域也分裂。实际计算给
$$
\lambda=-49019\bmod859=803,\qquad
\operatorname{ord}_{859}(\lambda)=33.
\tag{73.5}
$$
所以完整点坐标所需剩余域为
$L=\mathbb F_{q^{66}}$，而基域为 $k=\mathbb F_{q^2}$。
扩张 $L/k$ 的次数是 $33$，与 $43$ 互素。

R65 的导数下降满足
$\operatorname{res}(k_r)=[u_r^{D_r}]$；
Hilbert 90 的具体修正是一个 $p$ 次幂。
由 (73.4)，在所选局部完成域上限制映射就是恒等识别，
因此直接计算 $u_r^{D_r}$ 的剩余 Kummer 类确实检测下降后的类。
后面的 $L$ 只用于制造核点；最终范数值已经回到 $k$。
没有通过一个含 $p$ 次数的局部扩域把类杀掉之后再误读零值。

## 2. 同一个原始 Robert 族与 $\Gamma_r$ 生成元

先把 R65 模数中的额外 $(7)$ 因子暂时移除。
令
$$
v_r=N_{K(\mathfrak mr)/T(r)}
\Psi(1;\mathfrak mr,11^{-1}\mathfrak mr).
\tag{73.6}
$$
这个族使用 R65 的 Robert 约定
$N v_{nr}=v_n^{1-\operatorname{Frob}_r^{-1}}$。

在 $\mathbb F_{r^2}=\mathbb F_r[i]$ 中固定
$$
\gamma=2+i,\qquad
\zeta_r=\gamma^{(r^2-1)/p}=97+829i.
\tag{73.7}
$$
程序验证 $\zeta_r$ 的阶恰为 $43$。
令 $\sigma\in\Gamma_r=\operatorname{Gal}(T(r)/T)$
为 $\gamma$ 所对应的算术 Artin 元素。
更明确地，可用 CRT 取一个 Gaussian 整数 $\alpha$，
使 $\alpha\equiv1\bmod\mathfrak m$、
$\alpha\equiv\gamma\bmod r$，再取其主理想的 Artin 类。
它在 $r$ 挠点上的作用是 $[\gamma]$，不是其逆。
这固定
$$D_r=\sum_{j=1}^{p-1}j\sigma^j. \tag{73.8}$$

取 $R\ne O\in A[r]$、$S=[i]R$。因为 $r\equiv3\bmod4$，
$R,S$ 是 $A[r]$ 的 $\mathbb F_r$ 基。
全部 $r+1=860$ 条循环核为
$$
G_s=\langle R+[s]S\rangle\quad(s\in\mathbb F_r),\qquad
G_\infty=\langle S\rangle.
\tag{73.9}
$$
定义相应的权
$$
j_s=\log_{\zeta_r}\bigl((1+si)^{(r^2-1)/p}\bigr),\qquad
j_\infty=\log_{\zeta_r}\bigl(i^{(r^2-1)/p}\bigr).
\tag{73.10}
$$
每个 $j\in\mathbb F_p$ 出现 $(r+1)/p=20$ 次。
这正是展开 (73.6)、(73.8) 后的导数权：
一个 $H$ 陪集包含二十条 $\mathbb F_r$ 直线的全部非零点。
特别地
$$\sum_Gj_G=20\sum_{j=0}^{42}j=0\quad\text{于 }\mathbb F_{43}. \tag{73.11}$$

## 3. 将完整点范数化成 $860$ 个同源函数

对于任意短 Weierstrass 曲线 $E$，写
$$F_E(P)=\frac{\Delta_E^{10}}{\psi_{11,E}(P)}.$$
R70 已证明它与 Robert 函数只差一个十二次单位根。
该单位根在模 $43$ Kummer 群中为零。

给定 (73.9) 的核 $G$，令
$\phi_G:A\to A_G$ 为微分归一化的 Vélu 同源。
因为 $(11,r)=1$，$\phi_G$ 在 $11$ 挠点上是同构。
函数的除数因而给
$$
\prod_{U\in G}F_A(P+U)=c_G F_{A_G}(\phi_G P)
$$
对某个与 $P$ 无关的非零常数 $c_G$ 成立。
这是函数域范数的除数比较：推前
$120(O)-\sum_{T\in A[11]\setminus O}(T)$
恰是目标曲线的对应除数；两函数之比在光滑射影曲线上无零极点，
所以是常数。
去掉 $U=O$ 一项得到
$$
\prod_{U\in G\setminus\{O\}}F_A(P+U)
=c_G\frac{F_{A_G}(\phi_G P)}{F_A(P)}.
\tag{73.12}
$$
无需在商曲线上假定存在原来那个 $[i]$ 自同态。
$F_{A_G}$ 这里只是整数倍映射 $[11]$ 的规范有理函数。

在 (73.12) 中，$G$ 是 $r$ 侧的数据，而 $p$ 侧 Cartan 的作用
由 CRT 单独改变 $P_p$，固定 $G$。
因此 $c_G$ 以及 $\Delta_{A_G}^{10}$ 等常数都在非平凡
$\chi_0=\rho^p$ 投影中消失。
若只在有限域中看，也可直接用
$\sum_{a\in\mathbb F_{p^2}^{\times}}a^{-p}=0$ 消去它们。

### 3.1 原始模数点的一致性

若 $\mathfrak m=(\beta)$，来自
$\Psi(1;\mathfrak mr,11^{-1}\mathfrak mr)$ 的原始点，
其 $\mathfrak m$ 分量为原基点的 $[r^{-1}]$ 倍。
当前 $r\equiv-1\bmod4p$，所以 $r\equiv-1\bmod\mathfrak m$。
该分量因此为 $-P_{\mathfrak m}$。
函数 $F_A$ 为偶函数，而 $-1\in H$，
故把 $-P_{\mathfrak m}+U$ 改写为 $P_{\mathfrak m}-U$
不改变 (73.6) 的范数。于是后文确可使用同一个
$$P_{\mathfrak m}=P_2+P_p$$
来计算原始 Euler system 的导数。

改变非零 $R\in A[r]$ 只相当于在
$\mathbb F_{r^2}^{\times}$ 中作 Galois 共轭。
导数的模 $p$ 类已经在 $\Gamma_r$ 下不变，
故其下降类不变；改变 $\Gamma_r$ 的生成元则会把导数作非零缩放。
本文始终固定 (73.7)，并在证书中保存实际选取的 $R$。

## 4. 正确的 $\chi_0$ 投影及最终求和式

在目标基域 $k=\mathbb F_q[i]$ 中使用 R70 的同一组选择：
$$
P_2=(i,1-i),\qquad P_p=(11536,29305),\qquad
\zeta_q=(2+i)^{(q^2-1)/43}=19416+40301i.
\tag{73.13}
$$
令
$$P_a=P_2+[a]P_p,\qquad a\in\mathbb F_{43^2}^{\times}.$$
如 R70，$a=u+vi$ 表示源曲线上
$[u]P_p+[v][i]P_p$，Artin 标签为 $a$。

对每个核定义
$$
S_G=
\sum_{a\in\mathbb F_{43^2}^{\times}}
a^{-43}
\log_{\zeta_q}
\left(\psi_{11,A_G}(\phi_G P_a)^{(q^2-1)/43}\right).
\tag{73.14}
$$
每个 $\phi_G P_a$ 的整数阶为 $172$，因为 $\deg\phi_G=859$
与 $172$ 互素；故所有求值非零。
所用权确实是
$$a^{-43}=\frac{u+vi}{u^2+v^2},$$
即 $\chi_0(a)^{-1}$，并未替换成无扭曲的单位分量。

在 $\Gamma_r$ 范数及导数展开之后，(73.12) 的原曲线分母项
由 (73.11) 消失。目标曲线 Robert 函数中的 $1/\psi_{11}$
贡献负号；Cartan 投影中的
$[T:K]^{-1}=1848^{-1}=-1\bmod43$ 再贡献一个负号。
所以来自 (73.6) 的原始导数在 $q$ 的坐标是
$$
\boxed{Z_r(q)=\sum_Gj_GS_G.}
\tag{73.15}
$$
这包含原始单位的倒数、Cartan 归一化和 $\Gamma_r$ 权重。

### 4.1 R65 中额外的 $(7)$ 因子

R65 的实际单位族为
$$
u_r=N_{K(7\mathfrak mr)/T(r)}
\Psi(1;7\mathfrak mr,11^{-1}7\mathfrak mr).
$$
其与 (73.6) 的关系是
$$u_r=v_r^{\,1-\operatorname{Frob}_{(7)}^{-1}}.$$
这个 Frobenius 起初是 $C\times\Gamma_r$ 中的元素，
不能在原始层无说明地删去 $\Gamma_r$ 分量。
但 $[v_r^{D_r}]$ 下降后，$\Gamma_r$ 的作用模 $p$ 平凡。
投影到 $\chi_0$ 后便只剩
$$
1-\chi_0(\operatorname{Frob}_{(7)})^{-1}
=1+\frac17=\frac87=38\quad\bmod43.
\tag{73.16}
$$
此外，本例 $(7)$ 在 $r$ 侧的 Frobenius 是标量 $-7$，
本来就在 $H$ 中。这给相同结论的额外交叉检查。
因此 R65 的原始 $\kappa_r$ 的局部 Kummer 数据坐标为
$$\boxed{38Z_r(q).} \tag{73.17}$$

## 5. 扩域只负责核点，全部目标求和回到 $k$

程序找到
$$f(X)=X^{33}+X+41\in\mathbb F_{49019}[X]$$
并用完整 Rabin 判据证明不可约：
$$
X^{q^{33}}\equiv X\bmod f,\qquad
\gcd(f,X^{q^{11}}-X)=\gcd(f,X^{q^3}-X)=1.
\tag{73.18}
$$
因 $\gcd(33,2)=1$，$f$ 在 $k$ 上仍不可约。
取 $L=k[X]/(f)$。
Newton 恒等式给出特别简单的迹公式
$$
\operatorname{Tr}_{L/k}
\left(\sum_{j=0}^{32}z_jX^j\right)=33z_0-32z_{32}.
\tag{73.19}
$$
这里迹的一次到三十一次幂均为零，三十二次幂的迹为 $-32$。

在 $A(L)$ 中，$q^{66}$ 次幂 Frobenius 是
$[-q]^{33}=[-q^{33}]$，所以群指数整除 $q^{33}+1$。
程序从 $x=X$ 的点经有限域平方根算法得到一个点，
再乘 $(q^{33}+1)/859$，得到非零 $R\in A[859]$。
完整坐标保存在 JSON；程序验证
$$
[859]R=O,\qquad
R^{(q^2)}=[803]R.
\tag{73.20}
$$

群 $\langle-1,803\rangle\subset\mathbb F_{859}^{\times}$
阶为 $66$。其十三个陪集代表按最小未覆盖正整数取为
$$
1,2,3,5,6,7,9,10,17,18,25,27,34.
\tag{73.21}
$$
每条核的非零点在取正负号后分为十三个 Frobenius 轨道，
每轨道长度 $33$。因此全部核求和可以用 (73.19) 的迹完成。
十三条序列
$$[k]R+[s][k]S,\qquad s=0,\ldots,858$$
依次遍历全部有限斜率核，无需为每条线重新作大规模点倍乘。

### 5.1 明确的 Vélu 公式

对代表点 $U=(u,v)$，令
$$t_U=6u^2-2,\qquad w_U=10u^3-6u,\qquad v^2=u^3-u.$$
对核的正负号代表求和，有
$$
A_G=-1-5\sum t_U,\qquad B_G=-7\sum w_U,
$$
$$
x(\phi_G P)=x(P)+
\sum\left(\frac{t_U}{x(P)-u}
+\frac{4v^2}{(x(P)-u)^2}\right),
$$
$$
y(\phi_G P)=y(P)\left[
1-\sum\left(\frac{t_U}{(x(P)-u)^2}
+\frac{8v^2}{(x(P)-u)^3}\right)\right].
\tag{73.22}
$$
每个和由十三个代表的迹取代，所得系数和点坐标都在 $k$。

每条同源只计算三个点
$$\phi_G(P_2),\quad\phi_G(P_p),\quad\phi_G([i]P_p).$$
随后用商曲线自己的加法在 $k$ 中枚举 (73.14) 的全部 $1848$ 点。
第三个点保留为源曲线上 $[i]P_p$ 的像；
没有把它替换成目标曲线上未经证明存在的 CM 自同态。

## 6. 实际输出及全范数校验

全部 $860$ 条线完成计算后得到
$$
\boxed{Z_{859}(49019)=31+12i,\qquad
38Z_{859}(49019)=17+26i\ne0.}
\tag{73.23}
$$
部分行便于定位复算：

| 斜率 $s$ | $j_G$ | $S_G$ |
|---:|---:|---|
| $0$ | $0$ | $29i$ |
| $1$ | $0$ | $7+7i$ |
| $2$ | $42$ | $29+5i$ |
| $3$ | $1$ | $3+5i$ |
| $4$ | $4$ | $39+39i$ |
| $\infty$ | $0$ | $29$ |

完整的 $860$ 行都保存在证书中。
程序另外计算得到
$$\sum_GS_G=0. \tag{73.24}$$
这符合一个独立的完整范数恒等式：
把所有循环核的 (73.12) 相乘，每个非零 $r$ 挠点出现一次。
完整 $[r]$ 范数把 $\psi_{11,A}$ 送为其在 $[r]P$ 的值乘常数；
而 $[r]P_a=-P_a$，$\psi_{11,A}$ 为偶函数。
于是
$$
\prod_G\psi_{11,A_G}(\phi_G P_a)
={\rm const}\cdot\psi_{11,A}(P_a)^{r+1}.
$$
投影后得 $\sum_GS_G=(r+1)S_A=0$，因为 $43\mid860$。
该检查同时涉及全部核、目标模型及 Cartan 权，未使用已知的非零答案。

## 7. Selmer 及原始二阶类的实际结论

定义 R65 的 $p$ 校正
$$d_r=\kappa_r^{[p]}.$$
R70 的 $\kappa_0|r\ne0$ 保证 $d_r\ne0$，
且 $d_r$ 生成只松弛 $r$ 的一维 $\mathbb F_{43^2}$ 空间。
在 $q$，由于 $\kappa_0|q=0$，该校正完全不改变局部值。
因此 (73.23) 给
$$\boxed{\operatorname{loc}_{(q)}d_r\ne0.} \tag{73.25}$$
这证明 $r=859$ 是 $q=49019$ 的实际有效辅助素数。

对同一原始 Euler system 的二阶类，有限—奇异关系给
$$
\partial_{(q)}\kappa_{(qr)}
=\Phi_{(q)}(\operatorname{loc}_{(q)}\kappa_r)\ne0.
\tag{73.26}
$$
此处使用的是原始 $\kappa_{qr}$，没有把已经校正的 $d_r$
当作 Euler system 的成员。
在 $r$ 和 $p$ 作 R65 的线性消去之后，(73.26) 仍保留；
因此这里已经有一个确定的、无需继续搜索辅助素数的二阶补救公式。

进一步，$d_r$ 是 $\operatorname{res}_{K/\mathbb Q}c_r$
的非零 $\mathbb F_{43^2}$ 倍。
故 (73.25) 证明 R60 的
$$m_{q,r}\ne0,\qquad m_{r,q}=-m_{q,r}\ne0.$$
在只改变 $r,q$ 两处条件的修改 Selmer 问题中，
二阶交替矩阵满秩，修改 Selmer 群为零。
这只是一个已经由实际全局类控制的修改条件计算，
不构造相应的非 CM 同余椭圆曲线。

## 8. 可重复计算入口与明确范围

- [标准 C++ 源码](../notes/verify_r73_derivative_residue.cpp)。
- [完整有限域证书](../notes/r73_derivative_residue_certificate.json)。
- [推导与实施检查点](../notes/2026-11-12-derivative-residue-computation.md)。

从仓库根目录执行：

~~~bash
g++ -std=c++17 -O3 topics/serre-uniformity/notes/verify_r73_derivative_residue.cpp -o /tmp/verify_r73
/tmp/verify_r73 > /tmp/r73-certificate.json
~~~

程序只用 C++ 标准库。环境中没有 Boost 头文件；
所需大指数改由源码内约三十行的 radix-$2^{32}$ 整数计算，
仅实现乘小整数、加减一、除小整数和二进制展开。
没有安装新的数论系统。

源码保留全部证书断言，禁止用 NDEBUG 关闭它们。
检查包括：三个素数的完整试除；(73.18) 的不可约性；
扩域点的方程、精确 $859$ 阶及 Frobenius；
十三个轨道代表的完备性；
每条 Vélu 同源的三个点像及阶；
全部 $860\cdot1848$ 个目标点的方程、互异性、
非零除法多项式和 $43$ 次剩余符号。
每条线的三个样点另用直接加法核对 $[11]$ 的横坐标，
并比较无除法的快速 $\psi_{11}$ 公式与标准递推。
最后检查 (73.24)。

本轮完整运行约 $10.7$ 秒；这只是所用环境的记录，不是对其他
参数或机器的耗时保证。输出文件为 $13128$ 字节，其 SHA-256 为

~~~text
a8b6401171701f8c7ed173e8019f9ff63bf1d86cddc54cdea118982f0992d6df
~~~

整数命令参数可只计算前若干条线，用于定位问题；
这种输出明确标为不完整，不能替代本证书的全部 $860$ 条线。

本结果已经计算原始导数在另一个素数处的实际非零值，
比 R70 的基单位检测多了一层。
这里仍未展开二阶类的全局根式，也没有计算 $p$ 处的全部线性校正。
归一化的矩阵数值与二阶有限—奇异坐标由 R78 继续处理。
变化 $p$ 的统一排除及实际非 CM 同余曲线的存在性均未解决。

## 9. 已核对的输入

- [R65](R65-elliptic-unit-first-second-derivatives.md)：
  唯一的正确特征下降、原始导数、$p$ 校正和有限—奇异关系。
- [R70](R70-robert-unit-finite-field-certificates.md)：
  完整射线除法域、Robert 倒数归一化和三个基单位局部证书。
- K. Rubin, *The “main conjectures” of Iwasawa theory for imaginary quadratic fields*,
  Inventiones Mathematicae **103** (1991), 25–68，
  [原刊档案](http://resolver.sub.uni-goettingen.de/purl?PPN356556735_0103)：
  Proposition 2.2 的下降及 Proposition 2.4 的局部关系。
  Robert 约定的相同公式核对于
  [Oukhaba–Viguié (2013), §4–5、式 (5.2)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf)。
- J. Vélu, *Isogénies entre courbes elliptiques*,
  C. R. Acad. Sci. Paris Séries A **273** (1971), 238–241。
  (73.22) 的奇数核形式逐式核对于
  [A. Sutherland, 18.783 Lecture 5, Theorem 5.15、Remark 5.16](https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf)，2025；
  除法多项式使用同份讲义的 §5.5、Theorem 5.21。
