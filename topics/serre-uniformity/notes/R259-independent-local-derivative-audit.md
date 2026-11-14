# R259 独立复核：普通圆盘中真实规范 F2 截面的导数

此文供根代理并入 R259，不另占结果编号。采用已固定的 R140/R141
Hecke 相容、对称 Poincaré 对数，以及 R148/R151 的实际规范截面。

## 1. 固定量与变动量

令 $b=P_{-3}$、$u=P_{-12}$、$c=P_{-7}$、
$C(P)=P-b$、$F_2=27T_2+4$。在避开 $T_2$ 自交和各固定极点的普通
开集中，R148 的实际第二除子可写为

$$
D(P)=F_2C(P)+D_b,
$$

其中固定度零除子为

$$
D_b=162(u-b)-54(c-b)-27(Z_{-8}-20b)
       +4(K_{g_1}-106b).
\tag{A.1}
$$

因为 $T_2b=3u$，展开 (A.1) 就是 R260 的
$27T_2P+81u-27Z_{-8}-54c+4P+4b+4K_{g_1}$。
这里 $D_b$ 只微分一次；它不是 $P$ 的移动部分。

记 $\eta_E$ 为这个同一相容连接对实际度零除子 $E$ 的第三类一形式：
它关于除子可加，$\eta_{\operatorname{div}f}=d\log f$，留数为 $E$。
由 R140 §3 的实际 Hecke 相容性及自伴随性，

$$
\eta_{T_2C}=T_2\eta_C.
\tag{A.2}
$$

右边是实际对应上的 pullback–trace 一形式；它包含三个目标分支
的真正参数导数，不是裸函数系数的三项和。

## 2. 两变量的对称因子

先将两个输入 $C(P_1)$ 与 $F_2C(P_2)+D_b$ 分开微分，再限制
$P_1=P_2=P$。第一变量给

$$
27\eta_{T_2C}(P)+4\operatorname{reg}_j\eta_C(P)\,dj
  +\eta_{D_b}(P).
$$

第二变量给

$$
27T_2\eta_C(P)+4\operatorname{reg}_j\eta_C(P)\,dj.
$$

两式中的对角项使用相同的 $j$ 切向首项。对称连接和 (A.2)
因此给

$$
d\Lambda(e(C,D(P)))=
54T_2\eta_C(P)+8\operatorname{reg}_j\eta_C(P)\,dj
 +\eta_{D_b}(P).
\tag{A.3}
$$

系数 54 与 8 均来自两个变量各贡献一次。固定基点 $b$ 的导数
为零，其对配对的贡献已经包含在 $C=P-b$ 中，不应另加一次。

## 3. 规范截面和典范微分尺度的抵消

写 $g_1=a_Q(j)\,dj$。在当前无 $T_2$ 交叉的开集中，R148 的逐
生成元计算给规范截面坐标

$$
s(P)=(-a_b/a_P)^4.
$$

固定 $a_b$ 的导数为零；负号的四次幂为 1。故

$$
d\log s(P)=-4\,d\log a_P.
\tag{A.4}
$$

真正粗曲线的典范关系

$$
6K_{dj}=4\operatorname{div}(j)
 +3\operatorname{div}(j-1728)+35D-4b-3Z_{-4}
$$

和 $K_{g_1}=K_{dj}+\operatorname{div}(g_1/dj)$ 给

$$
\eta_{K_{g_1}-106b}
=d\log(g_1/dj)+\frac23\,d\log j
 +\frac12\,d\log(j-1728)
 +\frac{16}{3}\eta_{D-20b}-\frac12\eta_B,
\quad B=Z_{-4}-D.
\tag{A.5}
$$

核对基点次数时，$35D-3Z_{-4}-640b
=32(D-20b)-3B$，所以 (A.5) 没有缺少基点倍数。
将 (A.1)、(A.4)、(A.5) 代入 (A.3)，$4d\log a_P$ 精确相消，
得到

$$
\boxed{
\begin{aligned}
d\lambda(\sigma_{F_2,b})={}&54T_2\eta_C(P)
 +8\operatorname{reg}_j\eta_C(P)\,dj\\
&+162\eta_{u-b}(P)-27\eta_{Z_{-8}-20b}(P)
 -54\eta_{c-b}(P)\\
&+\frac{64}{3}\eta_{D-20b}(P)-2\eta_B(P)
 +\frac83\frac{dj}{j}+2\frac{dj}{j-1728}.
\end{aligned}}
\tag{A.6}
$$

这正是待核候选公式。所有额外典范尺度、双对称因子和固定基点
项都已逐项核对。原高度差的 800 倍在随后从 $\lambda(\sigma)$
转换到 R133/R228 规范时使用，不应加入 (A.6) 的单截面导数。

## 4. 射影参数下的正规项

以保存的射影参数 $z$ 写移动点为 $z=p$，并设

$$
\eta_C=\left(\frac1{z-p}+r_z(P)+O(z-p)\right)dz.
$$

对同一个点展开

$$
\frac{dj}{j-j(P)}
=\left(\frac1{z-p}+\frac{j''(p)}{2j'(p)}
 +O(z-p)\right)dz.
$$

所以

$$
r_z(P)=\operatorname{reg}_j\eta_C(P)\,j'(p)
       +\frac{j''(p)}{2j'(p)},
$$

即

$$
\boxed{
8\operatorname{reg}_j\eta_C(P)\,dj
 =\left(8r_z(P)-4\frac{j''(p)}{j'(p)}\right)dz.}
\tag{A.7}
$$

负号和 $1/2$ 来自原 simple-pole 核的实际换参；不能只把
正规项当作一形式系数乘 $j'$。程序应先减去真正主部再取正规项，
不应分别代入两个仍有极的表达式。

## 5. 实际 T2 接口的尺度

若实际 T2 取值使用 R254 规范 Vélu 的原始权二目标，则 R218
给 $b_{\rm target}=b_{\rm source}/2$。这个 $1/2$ 属于每分支
一形式的真实 Kodaira–Spencer 换算。它和 (A.3) 的双变量因子 2
来源不同：

- 系数 54 保留，不能改回 27；
- 分支 trace 仍须包含真实参数速度；
- 不得在已完成 pullback–trace 后再补乘或补除一次 2。

R248/R255 提供的 $g_C(P)$ 可以按同一实际第二类基积分
$g_C(P_0)+\int_{P_0}^{P}\nu$ 构造上述相容 $\eta_C$。本次复核
没有重算根代理的 RR 连接族，也没有声称该族的数值输出已完成。

