# R271 附录：全部孔层的显式 Schur–companion 来源与真实物理伴随

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 新增内容：将已用的二孔 pair 坐标推广为任意孔数的完整多项式来源；给出原下降与真实物理伴随的显式有限公式，并自足证明所用支化身份。
- 范围：有限 $n$ 个正权的全部完整层。没有证明一般相邻正性、无限图核心或原 $N=M$。

## 1. 完整层、去权与基

取 $n\ge2$，$b_i>0$，$z_i=b_i^2$。先对互异 $z_i$ 建立坐标。
在第 $k$ 孔层把物理坐标写为
\[
u_I=b_I f_I,\qquad b_I=\prod_{i\in I}b_i,\qquad |I|=k.
\]
于是原物理范数和下降为
\[
\|f\|_k^2=\sum_{|I|=k}z_I|f_I|^2,\qquad
(R_kf)_J=\sum_{i\notin J}z_i f_{J\cup\{i\}},
\tag{1.1}
\]
而真实物理伴随是
\[
(R_k^*g)_I=\sum_{i\in I}g_{I\setminus\{i\}}.
\tag{1.2}
\]
星号始终指这两端的物理内积，不指所列坐标矩阵的普通转置。

设
\[
p(x)=\prod_{i=1}^n(x-z_i),\qquad
V=\mathbb Q(e_1,\ldots,e_n)[x]/(p),
\]
以 $1,x,\ldots,x^{n-1}$ 为基，$T$ 为乘 $x$ 的单个 $n$ 维 companion。
第 $k$ 层使用 $\bigwedge^kV$ 的标准基
$e_{a_1}\wedge\cdots\wedge e_{a_k}$，$0\le a_1<\cdots<a_k<n$。
对应的对称多项式为
\[
s_A(x_1,\ldots,x_k)
=\frac{\det[x_i^{a_j}]_{i,j=1}^k}
 {\prod_{i<j}(x_j-x_i)}.
\tag{1.3}
\]
交错分子被每个差因子整除，故这是整系数对称多项式。
用分拆
$\lambda_i=a_{k-i+1}-(k-i)$ 标记时，
$\lambda$ 位于 $k\times(n-k)$ 矩形内；记同一多项式为 $s_\lambda$。

定义完整求值矩阵
\[
(\mathcal E_k)_{I,A}=s_A(z_I).
\]
$k=0$ 时规定 $\mathcal E_0=1$。

**定理 1（完整求值行列式）。**
若
$V_1=[z_i^a]_{1\le i\le n,\ 0\le a<n}$，
并按同一字典序排列所有子集和基，则
\[
\boxed{\det\mathcal E_k
=(\det V_1)^{\binom{n-2}{k-1}}}
\quad(1\le k\le n).
\tag{1.4}
\]
越界二项式为零，故 $k=n$ 时右边为一。
特别，互异根上 $\mathcal E_k$ 是完整维数 $\binom nk$ 的可逆来源，
没有删去任何 primitive、返回或高孔分量。

证明：$\bigwedge^kV_1$ 的行列式为
$(\det V_1)^{\binom{n-1}{k-1}}$。
把第 $I$ 行除以 $\prod_{i<j,\ i,j\in I}(z_j-z_i)$ 后恰为 $\mathcal E_k$。
每一对差因子在这些行中出现 $\binom{n-2}{k-2}$ 次。
用 Pascal 恒等式即得 (1.4)。复合行列式公式可先在对角矩阵上逐项核验，
再由可对角化矩阵的稠密性延拓；这里没有额外范数声明。$\square$

相应真实坐标度量为
\[
\mathcal M_k=\mathcal E_k^*
 \operatorname{diag}(z_I)\mathcal E_k>0.
\tag{1.5}
\]
特别它一般既不是单位阵，也不是单根矩阵度量的普通外幂。

## 2. 两类乘法算子

在 $\bigwedge^kV$ 上记
$\mathsf E_r^{(k)}$ 为 $r$ 次子集基本对称式的乘法，
$\mathsf P_r^{(k)}$ 为子集幂和的乘法。
有直接的有限矩阵公式：
\[
\boxed{\mathsf E_r^{(k)}
=[u^r]\,\bigwedge\nolimits^k(I+uT),}
\tag{2.1}
\]
\[
\boxed{\mathsf P_r^{(k)}
=\sum_{\ell=1}^k
 I\wedge\cdots\wedge T^r\wedge\cdots\wedge I.}
\tag{2.2}
\]
后一式是 $T^r$ 的 additive compound；它表示逐槽求和，
不是把 $\bigwedge^kT$ 取 $r$ 次幂。
规定 $\mathsf P_0^{(k)}=kI$，
$\mathsf E_0^{(k)}=I$，空层的正次幂和为零。

证明只需在完整根求值后看第 $I$ 行：
(2.1) 的乘子是 $\prod_{i\in I}(1+uz_i)$，
(2.2) 的乘子是 $\sum_{i\in I}z_i^r$。
它们在真实物理度量中均自伴。
所有矩阵条目由 $T$ 构成，都是全体基本对称参数的整数多项式。

## 3. 支化身份的有限行列式证明

对递增 $A=(a_1,\ldots,a_k)$，令 $B=(b_1,\ldots,b_{k-1})$
逐段取值
\[
a_j\le b_j<a_{j+1}\qquad(1\le j<k).
\tag{3.1}
\]
这些条件自动使 $B$ 严格递增。直接恒等式为
\[
\boxed{s_A(X,t)
=\sum_Bs_B(X)\,
 t^{\,\sum a_j-\sum b_j-(k-1)}.}
\tag{3.2}
\]
所有指数非负。

为自足核验，将 (3.2) 乘以
$\Delta(X)\prod_{i=1}^{k-1}(t-x_i)$。
行列式多线性把其右边化为
\[
t^{\sum a_j-(k-1)}
\prod_i(t-x_i)
\det\left[\sum_{b=a_j}^{a_{j+1}-1}(x_i/t)^b\right]_{i,j<k}.
\]
有限几何和给
\[
(t-x_i)\sum_{b=a_j}^{a_{j+1}-1}(x_i/t)^b
=t\bigl((x_i/t)^{a_j}-(x_i/t)^{a_{j+1}}\bigr).
\]
故右边等于
$t^{\sum a_j}\det[(x_i/t)^{a_j}-(x_i/t)^{a_{j+1}}]_{i,j<k}$。
另一方面，在左边原 $k\times k$ 交错行列式中，
各列提出 $t^{a_j}$ 后，最后一行全为一；
将前 $k-1$ 列依次改为原第 $j$ 列减原第 $j+1$ 列，
最后一列保留。这个列变换行列式为一。
沿最后一行展开恰得到同式。
先取 $t\ne0$ 的推导是多项式恒等式，故也覆盖 $t=0$。

按分拆记号，(3.1) 恰为
\[
\lambda_1\ge\mu_1\ge\lambda_2\ge\cdots
\ge\mu_{k-1}\ge\lambda_k.
\]
于是 (3.2) 也写成
\[
s_\lambda(X,t)=\sum_{\mu\prec\lambda}
s_\mu(X)t^{|\lambda|-|\mu|}.
\tag{3.3}
\]
其中 $0\le|\lambda|-|\mu|\le\lambda_1\le n-k$。
$\mu$ 全部落在实际 $(k-1)$ 层的基范围内。

## 4. 原完整下降的显式公式

令 $p_r^{\rm all}=\sum_{i=1}^nz_i^r$，由 Newton 递推得到。
将 (3.3) 代入原 (1.1)，固定 $|J|=k-1$，有
\[
\sum_{i\notin J}z_i^{|\lambda|-|\mu|+1}
=p_{|\lambda|-|\mu|+1}^{\rm all}
-\sum_{i\in J}z_i^{|\lambda|-|\mu|+1}.
\]
因此原完整下降矩阵为
\[
\boxed{
R_k s_\lambda
=\sum_{\mu\prec\lambda}
\left(
p_{|\lambda|-|\mu|+1}^{\rm all}I
-\mathsf P_{|\lambda|-|\mu|+1}^{(k-1)}
\right)s_\mu.
}
\tag{4.1}
\]
这里最多只用到 $p_r^{\rm all}$ 的 $r\le n-k+1$。
超过输出基的幂已经由单个 companion $T$ 准确约化。
公式是全部 $\binom nk$ 列的来源，不是 primitive 限制后的猜测。

## 5. 真实物理伴随的显式外幂公式

记 $v_j=T^je_0$，$e_0$ 是常数多项式基向量；
$v\wedge$ 表示在左侧楔入 $v$。
则
\[
\boxed{
R_k^*
=(-1)^{k-1}
\sum_{r=0}^{k-1}(-1)^r
 (v_{k-1-r}\wedge)\,\mathsf E_r^{(k-1)}.
}
\tag{5.1}
\]
乘法次序是先在完整 $(k-1)$ 层乘 $\mathsf E_r$，再楔入。
它是 (1.2) 的实际物理伴随。

证明：设输入的交错多项式为
$\mathcal A(X)=\Delta(X)f(X)$。
(1.2) 的输出乘 $\Delta(Y)$ 后为
\[
\sum_{i=1}^k(-1)^{k-i}
 \left(\prod_{j\ne i}(y_i-y_j)\right)\mathcal A(Y\setminus y_i).
\]
展开括号为
$\sum_{r=0}^{k-1}(-1)^r
 e_r(Y\setminus y_i)y_i^{k-1-r}$。
左楔 $v_j\wedge$ 的第一列余子式符号是 $(-1)^{i+1}$；
乘整体 $(-1)^{k-1}$ 后恰为 $(-1)^{k-i}$。
逐项得到 (5.1)，不需要把坐标度量改成单位阵。$\square$

特别，
\[
R_1^*=v_0,\qquad
R_2^*=v_0\wedge T-v_1\wedge I,
\]
\[
R_3^*=v_2\wedge I-v_1\wedge\mathsf P_1^{(2)}
+v_0\wedge(\bigwedge\nolimits^2T).
\tag{5.2}
\]
二孔式正好返回原已核 pair 来源。
(4.1) 在 $A=(a,b)$ 时也精确化为
\[
R_2s_{a,b}
=\sum_{r=0}^{b-a-1}p_{b-r}^{\rm all}T^{a+r}e_0
 -(b-a)T^{a+b}e_0,
\]
没有改变旧 pair 规范。

## 6. 全部奇数权桥与完整 Gram 的接续

对任何整数 $q\ge1$，原物理
$d_{b^{2q-1}}:\mathcal H_k\to\mathcal H_{k-1}$
在去权后系数为 $z_i^q$。
由 §2 的子集乘子，准确有
\[
\boxed{
C_{k,q}
=R_k\mathsf P_{q-1}^{(k)}
-\mathsf P_{q-1}^{(k-1)}R_k,
}
\tag{6.1}
\]
\[
\boxed{
C_{k,q}^*
=\mathsf P_{q-1}^{(k)}R_k^*
-R_k^*\mathsf P_{q-1}^{(k-1)}.
}
\tag{6.2}
\]
$q=1$ 返回 $R_k$；$q=2$ 返回原三次桥。
这是完整原物理奇数权来源及其真实伴随，未固定或丢掉任一返回孔层。

为说明这些新显式矩阵怎样进入已知真实 MP 规范，
令
\[
D_{j,k}=\frac1{j!}R_{k+1}\cdots R_{k+j},\qquad
F_{j,k}=D_{j,k}D_{j,k}^*.
\]
在 $0\le k\le\lfloor n/2\rfloor$、
$0\le j\le n-2k$ 的完整合法高度，
[R239 的完整 incidence 满射](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)
保证 $F_{j,k}>0$。
当 $k\ge1$，真实 primitive 投影为
\[
\Pi_k=I-R_k^*(R_kR_k^*)^{-1}R_k.
\]
因而原完整最小逆来源可直接构造为
\[
\mathcal J_{j,k}=D_{j,k}^*F_{j,k}^{-1}\Pi_k,
\qquad
\Gamma_{j,k}=\Pi_kF_{j,k}^{-1}\Pi_k
\quad\hbox{再限制于 }\ker R_k.
\tag{6.3}
\]
$k=0$ 时取 $\Pi_0=I$。

如需其精度的零延拓，完整 Schur 公式是
\[
F_{j,k}
-F_{j,k}R_k^*
 (R_kF_{j,k}R_k^*)^{-1}
 R_kF_{j,k},
\tag{6.4}
\]
且中间完整 Gram 准确为
\[
R_kF_{j,k}R_k^*=(j+1)^2F_{j+1,k-1}.
\]
(6.3)–(6.4) 是已知全逆后压缩规则在新显式来源中的应用，
不另算新的相邻正性结果。
它们表明对任意出生，完整来源仍只用同一 $n$ 个基本对称参数、
实际整层逆及严格正 Gram 分母；不能先限制 primitive 列再换成另一最小逆。

## 7. 碰撞权、费用与未付范围

(4.1)、(5.1)、(6.1) 的条目本身是基本对称参数的整数多项式。
实际物理完整 Gram 和合法逆在全部正权域连续，严格正分母不在碰撞处消失。
因此由互异域得到的完整特征或有理参数身份，可按实际原算子延拓到重复权。

但是 $\mathcal E_k$ 在碰撞处退化。
不能宣称它在该点仍是可逆坐标，也不能用退化的 (1.5) 推出新的物理范数等价。
即使互异，(1.4) 也没有支付 $\mathcal E_k$ 的条件数；
本篇不给随 $n$ 或权分离度一致的来源费用，更不把它搬到原无限 carry 或未知 $W$。

新增的是所有孔层的完整显式原来源与真实伴随公式，
以及无需另猜高出生投影的严格连接。
一般 S1、S2、相邻 Gram 正性和原 ISP 完成标准仍须独立支付。
