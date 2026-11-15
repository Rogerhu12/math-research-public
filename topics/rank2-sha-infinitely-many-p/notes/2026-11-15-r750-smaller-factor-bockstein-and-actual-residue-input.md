# R750 补充：指定值留数的较小因子 Bockstein 与准确低位输入

日期：2026-11-15。**状态：下述同一实际输入的转置和长度界已证明；原留数非零及完整同 R 仍未完成。**

本篇使用 R750 及其 primitive carry 增补。
只在原第二条十三行已经通过之后，读取同一个指定 $P_B=qt^rF\widetilde B$。
没有增加 $F$ 的算术身份或原来源列。

## 1. 原参数及曲线上的固定除子

保持
$$
d_0=r-k,\qquad1\le d_0\le13,\qquad
T=T_M=2h-k-13,\qquad s=2h+r-k,
$$
$$
\operatorname{ord}B_0=h+\rho,\qquad
B_0+2t^huB_1\in t^{T+13},\qquad
0\le\rho\le2\kappa-h<T-h.
\tag{1}
$$
R750 的真实值条件现在是
$$
\operatorname{Res}_P(eB_0\Xi_B\,\omega)=0
\quad(\omega\in\mathcal L_D^{\rm val}),
$$
$$
\Xi_B=\xi-\frac{b_s}{2a}t^{-d_0}u^2.
\tag{2}
$$
其实际符号只差 R750(17) 整体的负号，不改变零条件。

因为 $B_0$ 是 $N^2$ 的非零截面，$P$ 光滑，
$$
\boxed{
D_B=\operatorname{div}(B_0)-(h+\rho)P\ge0,\qquad
\deg D_B=2\kappa-h-\rho,\qquad P\notin D_B.
}
\tag{3}
$$
$D_B$ 是原整曲线上的有效 Cartier 除子；
不将其奇点或重数拆成自由值。
定义严格较短的长度
$$
\boxed{
L=T-h-\rho=h-k-13-\rho.
}
\tag{4}
$$
由 (1)，$0<L<h<s$。

## 2. 真左行的乘法转置

R750 的
$$
\mathcal L_D^{\rm val}\subset
H^0(C,\omega_C N^{-3}(TP))
$$
由实际 $E'$ 主部像定义，已经杀全部原 $\mathcal W_D$。
乘同一个 $B_0$，得到单射
$$
\boxed{
m_{B_0}:\mathcal L_D^{\rm val}\hookrightarrow
H^0(C,\omega_C N^{-1}(LP-D_B)),
\qquad \lambda=B_0\omega.
}
\tag{5}
$$
对整个未加主部约束的空间，准确有
$$
B_0\,H^0(C,\omega_C N^{-3}(TP))
=
H^0(C,\omega_C N^{-1}(LP-D_B)).
\tag{6}
$$
这里等号按同一个局部及全局线束框解释。

**证明。** $B_0$ 的零除子准确为 $(h+\rho)P+D_B$。
乘法先将 $N^{-3}$ 变成 $N^{-1}$，
再按该零除子消掉在 $P$ 的 $h+\rho$ 阶允许极，
并在 $D_B$ 留下相应零。
除同一个非零截面反向恢复原空间，因此 (6) 准确，
对其真实子空间给 (5)。
该证明在原奇异 Gorenstein 曲线上成立，不只在正规化上成立。证毕。

若前一增补所算的
$\delta_C=h^1(X,\mathcal O_X(\mathcal B_D-C))=0$，
R750 的全主部空间已经付清，此时 (5) 的像有更具体的准确式
$$
\boxed{
m_{B_0}(\mathcal L_D^{\rm val})
=
H^0(C,\omega_C N^{-1}(LP-D_B-E')).
}
\tag{7}
$$
一般 $\delta_C>0$ 时仍保实际主部条件，不以 (7) 替换。

## 3. native 项准确是同一 F 的普通首 Bockstein

令 $\widetilde F,\widetilde\psi$ 为原来已经固定的整因子及 Hensel 支，
$g$ 是原实际 regular 函数。
只在长度 $L<h<s$ 定义
$$
\boxed{
v_F=
\pi_L\left(\frac{\widetilde F(t,g(t))}{p}\right)\bmod p.
}
\tag{8}
$$
这里先取 $\pi_L$，再除 $p$；不声称整个形式函数可除 $p$。
因原 $F(t,\bar g)$ 消到 $h$，(8) 的低系数确实全被 $p$ 整除。

由同一个
$$
g=\widetilde\psi\exp(\eta_0+p\xi),\qquad
\eta_0=t^hu,
$$
在长度 $L<h$ 中，$\eta_0$ 完全不出现。
整 Taylor 展开给
$$
\boxed{v_F=e\,\xi\bmod t^L.}
\tag{9}
$$
二次的 $p\xi$ 项在除一次 $p$ 后仍为零；
这里所需 Taylor 阶均小于 $p$。

取原 $\mathcal H_1$ 的同一整角格作为计算呈示，
在这个低普通窗口评价。
由于低于首 Gaussian，该评价的列全整。
$F$ 的约化在其长度 $L$ 首核中，
(8) 正是它的普通首 Bockstein 代表。
这是读取原 $P_B$ 内部因子的较小矩阵；
没有把 $\mathcal H_1$ 额外加入原算术来源。

(5) 中的每个 $\lambda$ 都杀 $\mathcal H_1$ 的普通长度 $L$ 首像。
确实 R495 给
$\mathcal H_1\to H^0(C,N)$ 满射，
而
$H^1(C,N)=0$、$\deg(\omega_C N^{-1})=-\chi<0$。
在光滑原点的 Serre 对偶遂把
$$
H^0(C,\omega_C N^{-1}(LP))
$$
识别为该普通值像的左核。
故
$$
\boxed{
\operatorname{Res}_P(e\xi\,\lambda)
=\operatorname{Res}_P(v_F\lambda)
}
\tag{10}
$$
准确只读较小普通 Bockstein。

如果同时允许改变整因子提升
$\widetilde F\mapsto\widetilde F+pA$，
须保持原角条件并把 $P_B$ 的实际差
$pqt^rA\widetilde B$ 与修正 $R$ 一起运输。
此时 $v_F$ 增加 $A|_C$；
(10) 的真左行杀这个变化，原同修正的值类不变。
本篇未另选一个任意提升来消掉实际 $\xi$。

## 4. Gaussian 项的极部和正则部都不能删

置同一个局部表达
$$
\boxed{
c_B(t)=\frac{e b_s}{2a}t^{-d_0}u^2.
}
\tag{11}
$$
它在 $P$ 至多有 $d_0\le13$ 阶极。
记其 Laurent 分解为
$$
c_B=c_{B,-}+c_{B,+},\qquad
c_{B,-}=\sum_{j=1}^{d_0} c_{-j}t^{-j},
\quad c_{B,+}\in k[[t]].
$$
那么原全部值条件准确为
$$
\boxed{
\operatorname{Res}_P\bigl((v_F-c_B)\lambda\bigr)=0
\quad\text{对全部 }\lambda\in
m_{B_0}(\mathcal L_D^{\rm val}).
}
\tag{12}
$$

(12) 的 native 及 $c_{B,+}$ 部分只用 $t^{<L}$ 系数；
极部则使用同一全局 $\lambda$ 在 $P$ 的
$t^0dt,\ldots,t^{d_0-1}dt$ 系数。
这些正则系数由全局左行确定，不能当成自由补值。
因此只保一个局部主部代表的普通左行，
不足以计算 (12) 的 Gaussian 项。

另外，不存在在这里保一条非零全局左行却完全避开普通 jet 数据的做法：
$$
H^0(C,\omega_C N^{-1})=0
$$
使
$$
H^0(C,\omega_C N^{-1}(LP))
\longrightarrow\{\text{在 }P\text{ 的长度 }L\text{ 主部}\}
$$
单射。故每个非零 (5) 都有非零主部。
这不证明该行对实际 $v_F$ 的取值非零，
只排除了把 (11) 的有限极部单独当成完整障碍。

## 5. 准确有限输入长度

(8) 只需原 $g$ 的 $t^{<L}$ 系数到模 $p^2$，
以及同一个 $\widetilde F$。
它们位于 R687 的原非共振精确前缀，
不需要为此取得整个 CM 分子的高位窗口。

计算 (11) 的正则部至 $t^{L-1}$，
连同其全部极部，
只需 $e,b_s,u^2$ 的乘积至阶
$$
L+d_0-1=T-h-\rho+r-k-1.
\tag{13}
$$
当前范围中
$$
L+d_0\le h-k-\rho\le h<s,
\tag{14}
$$
因为 $d_0\le13$。
所以这些也都在同一个原低窗口内。
$u$ 的所需系数必须按
$\eta_0/t^h$ 从原 $\eta_0$ 读取，不能把其阶号直接当成 $g$ 的阶号。
准确地，所需 $\eta_0$ 的最高阶为
$
\boxed{
h+(L+d_0-1)=s-k-14-\rho<s.
}
\tag{15}
$
因此整个 (12) 的实际函数输入可以如下取得：

| 输入 | 原准确窗口 |
|---|---|
| $v_F$ 的 native 整商 | $g\bmod p^2$，普通阶 $<L$ |
| $u$ 经 $\eta_0$ 返回的模 $p$ 数据 | 原 $\eta_0$ 至阶 $s-k-14-\rho$ |
| $e,b_s$ 及其有限乘法 | 普通阶至 $L+d_0-1<h$ |
| $\lambda$ | 同一个原曲线与实际全来源主部约束；不是新增算术数据 |

所以此值配对没有使用首共振之后的 CM 高分子来补 native 位。
全部仍是同一原对象；所有 $b_s$ 系数继续用真实 $t/w$ 规范，
不删原 $H^{-p}$。

上述缩短只是对 (12) 的实际算术输入作准确定位。
它不证明这个较小普通矩阵的首 Bockstein 为零或非零，
不证明 (5) 的像是其完整左核，
也不把特征零接触终止反读为目标 $p$ 的单位子式。

通过 (12) 后，R750(41)–(44) 的整个同 $R$ 法向、第三块、
两条十三行及下一位仍须同时解决。
本篇不为这些余块另选修正。

依赖：
[R750](../results/R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[前一增补](2026-11-15-r750-whole-divisible-source-and-primitive-carry-filter.md)；
[R687](../results/R687-original-cm-three-digit-matrix-and-complete-same-correction-transport.md)；
[R495](../results/R495-fixed-angular-surface-and-full-triple-source-joint-image.md)。
