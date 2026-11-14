# R526 — 原 Θ 对数零估计与两权真核排除

日期：2026-11-14。**状态：已证明。** 原 regularized
$\Theta$ 的对数方程有一个此前未在混权比较中使用的简化：
$$
\{6(1-t)\delta^2-(1+2t)\delta\}\log\Theta_{\rm reg}
=\frac23t\pmod{t^s},\qquad \delta=t\partial_t.
$$
全部 $d=1+8t$ 角分母准确相消。

由此得到一个不随非零权差放大的有理接触界。
将它用于 R486 的同一规范化来源，若
$$
N<p,\qquad
s-(13+r_c)>4E_N+C_N+7,
$$
则原完整矩阵的每个非零首核至少含三条非零约化权。
同一结论适用于 primitive 的模 $p^2$、模 $p^3$ 右核提升。
这里 $r_c$ 是实际 conductor 的原点阶；不用 conductor 时取零。
全 $P_{134}/U_0$、Gaussian 和进位未删：
证明仅使用它们完整矩阵的一条必要投影。

该界覆盖 $N\asymp\sqrt p$ 的真临界量级，
不是固定来源维数后排除有限坏素数。
它不证明三权以上的混合已不可能，也没有将两权排除称为主目标完成。

## 1. 原变量与低轴方程的精确相消

保 R507 的原实际参数
$$
p=6s-1>83,\quad d=1+8t,\quad
g=d\,\Theta_{\rm reg}^{17},
$$
$$
\mathcal P=6(1-t)\delta^2-(1+2t)\delta,
\qquad
\mathcal R_g=
\frac{t(154+160t+1792t^2)}{3d^2}.
\tag{1}
$$
原 Gaussian 已删的实际 $g$ 满足
$$
\mathcal P\log g
=\mathcal R_g-a_0s\,\mathsf B\,w^s ,
\tag{2}
$$
其中 $a_0=p\kappa_{\rm Gauss}\in\mathcal O^\times$、
$\mathsf B$ 为 R507 的完整整单位。
所有变量均为原模型中的变量，没有改变 Gaussian 常数或高轴。

直接计算
$$
\delta\log d=\frac{8t}{d},\qquad
\delta^2\log d=\frac{8t}{d^2},
$$
给
$$
\mathcal P\log d
=\frac{40t-128t^2-128t^3}{d^2}.
$$
因此
$$
\boxed{
\mathcal R_g-\mathcal P\log d
=\frac{34}{3}t,
}
\tag{3}
$$
从而原整窗口中准确有
$$
\boxed{
\mathcal P\log\Theta_{\rm reg}
=\frac23t-\frac{a_0s}{17}\mathsf B\,w^s .
}
\tag{4}
$$

$t/w$ 是已付原整单位，所以在普通第一块中 $w^s=0$。
记 $\theta=\overline{\Theta}_{\rm reg}\in k[[t]]/(t^s)$，$\theta(0)=1$，
$k$ 为原完美剩余域。令
$$
b_\theta=\delta\theta/\theta.
$$
下文只用以下准确有理微分身份：
$$
\boxed{
6(1-t)\delta b_\theta-(1+2t)b_\theta
=\frac23t\pmod{t^s}.
}
\tag{5}
$$
不需要正特征完整 log。
(5) 是原实际低轴的方程；
任意改动高轴的形式族只有在保 (5) 时才能调用本篇，
不能把未经原 ODE 约束的参数视为同一个 $\theta$。

## 2. 对任意有理单位的统一接触界

取 $R(t)\in k(t)^\times$，在 $0$ 正规且非零。
令
$$
u_R=\delta R/R.
$$
在非零有限点 $\alpha$，
$u_R$ 的极至多一阶；当且仅当
$\operatorname{ord}_\alpha R$ 在 $k$ 中非零时有极。
记
$$
H_R(t)=
\prod_{\substack{\alpha\ne0\\
 \operatorname{ord}_\alpha R\not\equiv0\ (p)}}(t-\alpha),
\qquad
\Delta_R=\deg H_R ,
\tag{6}
$$
乘积按几何根读取并取 monic 多项式。
它在 $k$ 上有定义且平方自由，$H_R(0)\ne0$。
不计那些只贡献 $p$ 次幂的零极点。

因为对数导数在无穷远有界，且 $u_R(0)=0$，
可写
$$
u_R=N_R/H_R,\qquad
\deg N_R\le\Delta_R.
$$

**定理 1（不随权差放大的零估计）。**
令整数 $a$ 满足 $p\nmid a$。
若 $1\le T\le s$，并且
$$
\theta^a-R=0\pmod{t^T},
\tag{7}
$$
则
$$
\boxed{T\le2\Delta_R+1.}
\tag{8}
$$

**证明。** (7) 给
$u_R-a b_\theta\in t^T k[[t]]$。
$\delta$ 不降低 $t$ 阶，故由 (5)，有理函数
$$
Z_R=
6(1-t)\delta u_R-(1+2t)u_R-\frac{2a}{3}t
\tag{9}
$$
在 $0$ 至少有 $T$ 阶零。
清 $H_R^2$ 后的分子次数不超过
$2\Delta_R+1$；$H_R(0)\ne0$。
若 $T>2\Delta_R+1$，则 (9) 必恒为零。

这不可能。若 $u_R$ 在
$\alpha\notin\{0,1\}$ 有一个简单极，写其首项为
$c/(t-\alpha)$，$c\ne0$，
则 (9) 的二重极首系数为
$-6\alpha(1-\alpha)c\ne0$。
故没有这种极。
若在 $\alpha=1$ 有极，则
$6(1-t)\delta u_R-(1+2t)u_R$
的简单极系数为 $3c\ne0$，同样不允许。
在 $0$ 本来正规，因此 $u_R$ 无任何有限极。
又它在无穷远有界，故为常数；
由 $u_R(0)=0$ 得它为零。
(9) 遂迫 $2a/3=0$，与 $p\nmid a$ 矛盾。$\square$

这个证明保留了 $t=1$ 的原正规奇点，
未把它错误当作任意普通点，也未遗漏一个可抵消的对数极。
它没有要求 $R$ 的全部次数小于 $p$；
$p$ 次幂因子的作用已按 (6) 准确去掉。

$p\nmid a$ 是必需的。
例如 $\theta^p-1$ 的普通低阶项在 $t^p$ 以前全零，
所以不能把 (8) 扩成权差为 $p$ 倍数的结论。

## 3. 原规范化来源的真实两权比较

使用 R486 同一个
$$
a(t)=t(t-1)h_7(t),\qquad
h_7=7+4t+16t^2,
$$
$$
c_m=\lceil m/68\rceil,\qquad
e_m=\lfloor11m/34\rfloor-4c_m,\qquad
\mathcal B_m=\Theta^m a(t)^{c_m}k[t]_{\le e_m}.
\tag{10}
$$
$e_m<0$ 的权不存在。
角多项式 $a(t)$ 与定理1中的指数 $a$ 无关；
以下将权差记为 $\Delta m$。

令 $m\ne n$ 为两个真实非空权，
取非零的实际约化系数多项式
$$
f_m\in k[t]_{\le e_m},\qquad
f_n\in k[t]_{\le e_n}.
$$
写
$$
j_m=\operatorname{ord}_0f_m,\quad
j_n=\operatorname{ord}_0f_n,\quad
v_m=c_m+j_m,\quad v_n=c_n+j_n.
\tag{11}
$$
考虑普通实际组合
$$
F_{\rm ord}=\theta^m a(t)^{c_m}f_m+
\theta^n a(t)^{c_n}f_n.
\tag{12}
$$

若 $F_{\rm ord}=0\bmod t^H$ 且
$H>\max(c_m+e_m,c_n+e_n)$，
则两个首阶都小于 $H$，
所以必须有
$$
v_m=v_n=v<H.
\tag{13}
$$
令 $f_m=t^{j_m}f_m^0$、$f_n=t^{j_n}f_n^0$，
其中两个上标零的多项式在 $0$ 为单位。
再置
$$
A(t)=a(t)/t=(t-1)h_7(t).
$$
由 (12)–(13)，得到
$$
\theta^{n-m}
=
-\frac{A(t)^{c_m-c_n}f_m^0}{f_n^0}
\pmod{t^{H-v}}.
\tag{14}
$$
右边在原点确为有理单位；
所有 $t$ 阶因 (13) 准确相消，未自由除去一个来源因子。

右边有理函数的有效非零有限极点数满足
$$
\boxed{
\Delta_R\le
(\deg f_m-j_m)+(\deg f_n-j_n)
+3\,\mathbf1_{c_m\ne c_n}.
}
\tag{15}
$$
最后的三是 $A=(t-1)h_7$ 的三个不同几何根。
$p>83$ 保它们与 $0$ 的全部原互素性。
共同零因子或 $p$ 重指数只会减小 $\Delta_R$，不会使 (15) 失效。

**定理 2（逐权对的准确充分排除门）。**
在上述条件下，另假设 $H\le s$ 且 $p\nmid(n-m)$，
则必有
$$
\boxed{
H\le
2(\deg f_m+\deg f_n)
+2\min(c_m,c_n)-\max(c_m,c_n)
+6\mathbf1_{c_m\ne c_n}+1.
}
\tag{16}
$$
可将实际多项式次数换为 $e_m,e_n$ 得只依赖权的门。

**证明。** 定理1、(14)、(15) 给
$$
H\le v+2\Delta_R+1
\le
2(\deg f_m+\deg f_n)-3v
+2c_m+2c_n+6\mathbf1_{c_m\ne c_n}+1.
$$
再用 $v\ge\max(c_m,c_n)$，即得 (16)。$\square$

与一般双变量因子次数界不同，
(16) 没有乘 $|n-m|$。
即使只含两项但两个权相距很大，
对数方程仍只产生线性于真实系数次数的门。

## 4. 原完整 M 的必要第一块投影

保原
$$
M=c_*U_0m_{13}J
$$
以及 R486 的实际 conductor 返回。
若不用 conductor，令 $r_c=0$；
若使用原
$\mathfrak c=\Theta^{10980}q_{\mathfrak c}(t)$，
令
$$
r_c=\operatorname{ord}_0q_{\mathfrak c}.
$$
只在 R486 已付的原整单位范围使用其返回：
包括固定首系数的有限坏集排除，以及所需原完整目标范围。
记
$$
d_0=13+r_c,\qquad H=s-d_0.
\tag{17}
$$

在原目标约化后，第一块准确是 $k[t]/t^s$。
共同 $c_*,U_0$、$w^{13}/t^{13}$、
conductor 的 $\theta^{10980}q_{\mathfrak c}/t^{r_c}$
给同一个原单位。
所以对同一来源
$$
P=\sum_{m\le N}\Theta^m a(t)^{c_m}f_m
$$
有必要条件
$$
\boxed{
\bar M P=0
\quad\Longrightarrow\quad
\sum_{m\le N}\theta^m a(t)^{c_m}f_m
=0\bmod t^H ,
}
\tag{18}
$$
只要 $H>0$。

这是一条从完整原矩阵取出的必要投影。
它没有说 $U_0$ 在所有全局角点为单位；
这里只使用原点已付的整单位。
Gaussian 项在第一块的投影为零，
原第二、第三块、两条 $13+r_c$ 进位带、
十三自由行和第三精度仍然存在。
因此用 (18) 排除候选是合法的，
但不能由其可解反推完整 $M$ 可解。

## 5. 累计预算下每个真核至少有三条权

对累计真实来源 $\mathcal B_{\le N}$，定义
$$
E_N=\max_{\substack{0\le m\le N\\e_m\ge0}} e_m,
\qquad C_N=\lceil N/68\rceil .
$$
$0$ 权提供 $e_0=0$，故最大值总有定义。
若 $N=68q+r$、$0\le r<68$，则准确有
$$
\boxed{
E_N=18q+\max\{0,\lfloor11r/34\rfloor-4\},
\qquad
C_N=q+\mathbf1_{r>0}.
}
\tag{19}
$$
这是直接使用 R486 的全部 ceiling 余类；
没有把 $e_N$ 在每个跳跃处误当成累计最大值。

**定理 3。** 保全部原来源和返回条件。
若
$$
\boxed{
N<p,\qquad
s-(13+r_c)>4E_N+C_N+7,
}
\tag{20}
$$
则任何非零
$P\in\ker\bar M$ 在规范化直接和中至少有三条非零权分量。

**证明。** 若只含一条非零权，其普通首阶至多 $C_N+E_N$，
小于 (20) 的 $H$，与 (18) 矛盾。
若恰含两条权，(20) 首先保证定理2所需的
$H>\max(c_m+e_m,c_n+e_n)$。
又 $N<p$ 使非零权差必为 $p$ 单位。
由 (16)，
$$
H\le4E_N+C_N+7,
$$
因为
$2\min(c_m,c_n)-\max(c_m,c_n)\le C_N$。
这再次与 (20) 矛盾。$\square$

同一原有限自由来源中，若 $P_2$ 是 primitive 的模 $p^2$ 右核提升，
或 $P_3$ 是 primitive 的模 $p^3$ 右核提升，
则其非零约化在 $\ker\bar M$，所以约化也至少有三条权。
这里 primitive 指 R486 使用的那份明确来源格；
不把另一个未证明饱和的冗余呈示中的 primitive 性移过来。

(20) 不需要两条完整中央同时失败，
所以在代入三条原完整中央确定的实际参数后仍成立。
它并没有给这些条件增加新的零传播。

## 6. 真临界量级与范围

由 (10)，
$$
e_m=\frac9{34}m+O(1),
\qquad
\dim\mathcal B_{\le N}
=\frac9{68}N^2+O(N).
\tag{21}
$$
若原目标
$L=2s+\ell$ 与这份真实来源维数处于临界量级，
且 $\ell/s\to\lambda$，则
$$
s\sim\frac{9N^2}{68(2+\lambda)}.
\tag{22}
$$
低 $\ell$ 时
$$
p\sim\frac{27}{68}N^2,\qquad
N\sim\sqrt{\frac{68}{27}p}.
$$
而 (19) 给
$$
4E_N+C_N+7=\frac{73}{68}N+O(1).
\tag{23}
$$
固定 conductor 的 $r_c$ 也是固定常数。
因此在 (22) 的真二次临界量级中，(20) 最终严格成立，
且 $N<p$ 也自动成立。

这只是对任何已经存在的真实临界候选给出的支持数限制；
它不从人工选择参数或维数断言该候选存在。
也不把固定 conductor 的 $10980$ 权、原点阶、系数范数和进位成本删除。

## 7. 尚未支付的多权问题

定理3排除了单权及两权支持，
尤其排除了只靠一个很大的权差来制造临界右核的路线。
三个以上不同权的和不能取成一个有理比值，
所以定理1不能直接重复调用来声称它们也已排除。

下一项可研究同一对数方程的多权 Wronskian 或微分消元，
但必须保 (10) 的原系数帽、实际角项、原有限目标长度，
并明确其常数能否覆盖 (22)。
若得到的界仍大于临界长度，就不能把非零 Wronskian
或来源微分饱和称为原中央非零。

本篇为全参数有理极点及真实矩阵必要投影证明，
没有新增素数扫描。
原完整 $M$、两次 carry、同一首次修正及第三精度均按
R479、R481、R486 保留。
