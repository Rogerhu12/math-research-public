# 原有限三次零纤维的退化秩与负水平行去重

日期：2026-11-16。**状态：以下全部三次退化类型的两列秩、唯一四行例外与原 $\rho_-$ 的准确重合已证明。完整 $K_1$ 在这些行中的像仍未判定。**

保[原零纤维三层商](2026-11-16-r872-native-zero-fiber-three-layer-quotient.md)的同一
$F_{\rm fin}$、$L=Y\partial_Y+40$、$p>211$、原 $K_1$、全部 Gauss 帽与
$G_1$ 修正。$F_0=F_{\rm fin}(0,Y)$ monic、次数三，物理根 $1$ 简单。
无需假设其它根非零或简单。

## 1. 两个实际 primitive 列的完整秩

定义
$$
b_i=L^{-1}(Y^iF_0^3)\bmod F_0\quad(i=0,1),\qquad
V=\langle b_0,b_1\rangle .
$$
令 $r$ 为 $F_0$ 在代数闭域中的不同非零根数。
因为 $1$ 是简单根，$r\ge1$。

若两列相关，则存在非零 $A\in k[Y]_{\le1}$，使
$$
W=L^{-1}(F_0^3A),\qquad F_0\mid W,\qquad \deg W\le10.
\tag{1}
$$
在非零的 $m$ 重根 $c$ 处，设 $\operatorname{ord}_cW=n$。
原 $F_0\mid W$ 给 $n\ge1$，而 $n\le10<p$，所以
$Y\partial_YW$ 的首项系数 $cn$ 非零，准确有
$$
\operatorname{ord}_c(LW)=n-1.
$$
因此 $n\ge3m+1$。
若零根重数为 $m_0$，原 $40+n$ 全部为单位，$L$ 保持 $Y$ 阶，
故 $Y^{3m_0}\mid W$。合计得到
$$
\deg W\ge3\deg F_0+r=9+r.
\tag{2}
$$
$r\ge2$ 时与 (1) 矛盾。有限域扩张忠实，因此原 $k$ 上也有
$$
\boxed{r\ge2\quad\Longrightarrow\quad\dim_kV=2.}
\tag{3}
$$
这包含另一个非零重根，或一个简单零根；不必使用原较强的
$\gcd(F_0,YF_0')=1$ 门。

若 $r=1$，由于物理根 $1$ 简单，唯一可能是
$$
F_0=Y^2(Y-1).
$$
此时 $L^{-1}(F_0^3)$ 与 $L^{-1}(YF_0^3)$ 都含 $Y^6$，
故在零根的整个二次局部代数中均为零。
物理根的值分别为
$$
v_0=-\frac6{46\cdot47\cdot48\cdot49},\qquad
v_1=-\frac6{47\cdot48\cdot49\cdot50}.
$$
二者为单位。因此
$$
\boxed{
\dim V=1,\qquad
\operatorname{rank}(\operatorname{ev}_1|_V)=1,\qquad V_-=0 .
}
\tag{4}
$$
局部相关式正是
$$
L\!\left(Y^6(Y-1)^4\right)=F_0^3(50Y-46),
$$
与 $v_1/v_0=46/50$ 一致。

## 2. 普通退化仍只有原二／三行

前注的真正低商是
$$
Q_0=(\mathcal A/t^3\mathcal A)/(t^2V),\qquad
\mathcal A=k[[t]][Y]/F_{\rm fin}.
$$
分出同一个物理根后，$K_1$ 的实际读取落
$$
\mathcal B_0\oplus(\mathcal B_0/V_-),\qquad
\mathcal B_0=k[Y]/G_0,\quad G_0=F_0/(Y-1),
$$
其维数为 $4-\dim V+\operatorname{rank}(\operatorname{ev}_1|_V)$。

由 (3)，除 (4) 的唯一情形外，这个目标始终至多三维。
原几何简单性仅在物理根使用；另一二次块可以含幂零元。
这延伸的是同一个真实有限商，并没有增加全来源列或算术测试。

## 3. 唯一四行例外与原负水平行的准确重合

在 (4) 中，$\mathcal B_0=k[Y]/Y^2$，$V_-=0$，
所以完整低商本来具有四个坐标。
对同一个 $W\in K_1$ 写
$$
W=t\,w_1(Y)+t^2w_2(Y)+O(t^3),\qquad
G(t,Y)=Y^2+tG_1(Y)+O(t^2).
$$
准确读取仍为
$$
\boxed{
\beta_1=w_1\bmod Y^2,\qquad
\beta_2=
\left(w_2-G_1\operatorname{quo}_{Y^2}w_1\right)\bmod Y^2.
}
\tag{5}
$$
第二式保同一移动二次因子的完整一次项，不能改成静态 $\operatorname{rem}_{Y^2}w_2$。

此时原 $C$ 在未吹起的 $R_0=(0,0)$ 与严格负水平相交，
所以 $z_-\ge1$；已付的原
$$
\rho_-(W)=[Y^0]W\in t\,k[t]_{\le4}
$$
确实下降到 $K_1/(\mathscr J_3\cap K_1)$。
由 (5)，其中一行**准确重合**：
$$
\boxed{[Y^0]\beta_1=[t]\rho_-(W).}
\tag{6}
$$

因此在同时保留 $\rho_-$ 的实际联合读取时，
本零纤维只需再保三个明确坐标
$$
\boxed{
[Y]\beta_1,\qquad [Y^0]\beta_2,\qquad [Y]\beta_2.
}
\tag{7}
$$
或者限制到真正 $\ker\rho_-\cap K_1$，原四行自动落在 (7) 的三维子空间。
这个减少来自同一个来源系数的恒等式 (6)，不是把两个目标的维数相减。

特别不能继续删除 $[Y^0]\beta_2$。
即使 $\rho_-=0$，也只有
$$
[Y^0]\beta_2
=-G_1(0)\,[Y^2]w_1 ,
$$
右边一般不为零。
原 $w_1=(Y-1)^4a_2(Y)$、$\deg a_2\le2$ 与其它全部前缀仍必须一起使用；
不能把 $G_1$ 或 $[Y^2]w_1$ 独立选取。

## 4. 原商和后续页的范围

有限商读取杀 $\mathscr V_1\cap K_1$ 及 $\mathscr J_3\cap K_1$。
$\rho_-$ 一般只杀后一子格，**不**因此下降到
$\mathcal W_D/(\mathscr V_1+\mathscr J_3)$。
式 (6)–(7) 是同一 $K_1$ 上联合读取的去重，不能改写成这个较小商上的额外自由坐标。

本注没有证明 $\ker\rho_-\cap K_1$ 到 (7) 满射，
没有把物理零纤维当全部 $\mathscr T_D$，
也没有删除全球连接类或指定 $\Pi$ 的响应。
原同一个 $R,S$ 在有限行、$\rho_-$、三尾、normal 与完整
Bockstein 页中仍须联合满足所有方程。

无新增数学数值运行。
