# R605 — 同一原中央的两个真实像、三域外补偿与原负五矩

日期：2026-11-14。**状态：已证明。**

R601 已在同一个五变量来源上支付完整 $Y$ 一层与 $W$ 四层核心。
本篇对它们产生的两个真实矩形像，直接积分原来的两个分别带单位
指示的中央观察。两像与原矩形的首负三、负五行具有同一比例；
其总比例是一个显示的固定 $\lambda,\kappa$ 有理式。

在原正密度射线中删去一个 $O(\sqrt X\log X)$ 的显示坏集后，
这个总比例是单位。完整三域外积分的相邻深度差因而准确返回
R533/R540 的原负五矩 $I_1$，误差仍为 $p^{4n}$。
R594 的原两个带权补偿通过完整等式接入，七个真实余类矩未被删去。
本篇没有将三域外补集或原 $I_1$ 赋零。

## 1. 同一个来源、原观察与原矩形

沿用
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)、
[R599](R599-original-complement-and-negative-five-return.md)、
[R601](R601-original-q-tensors-complete-y-w-cores-and-fifteen-source-spectrum.md)
的原射线、全部固定坏集和原周期：
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times .
\tag{1}
$$
当前 $p\ge71$、$p\equiv7\bmod64$、$v_p(\kappa)=1$。
在 $(Z,Q,r,c,d)$ 上保持完整来源
$$
\nu^\flat=\frac1{42}
(\nu_{f_1}\otimes\nu_\Sigma-\nu_{f_3}\otimes\nu_\Theta)
\otimes\nu_\sigma^{\otimes3},
\quad
f_1=-x_\wp y_\wp\sigma^6,\ f_3=-y_\wp\sigma^6,\ 
\Sigma=\sigma^2,\ \Theta=x_\wp\sigma^2 .
\tag{2}
$$
置
$$
a_Z=(-2+\omega)/2,\qquad a_Q=(4+3\omega)/2,\qquad
A_0=a_ZZ+a_QQ+2\delta r .
$$
原观察和原中央差仍是
$$
Y=A_0+c+2d,\qquad W=A_0+3\delta c+4d,
$$
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
          -1_{W\ {\rm unit}}\log\langle W\rangle\},\qquad
\mathcal T=\nu^\flat(\ell)=J'_S-6\delta J'_T .
\tag{3}
$$
原矩形及其未附 carry 权的积分为
$$
\mathscr R_n=\{Z\ {\rm unit},\ Q,r,c,d\in p^n\},\qquad
R_n=\int_{\mathscr R_n}\ell\,d\nu^\flat,\quad n\ge1.
\tag{4}
$$
始终区分这个 $R_n$ 与 R594 赋值为 $n$ 的带权积分。

## 2. 两个完整核心与真实像上的单位指示

令 $G_5=\operatorname{diag}(6,2,1,1,1)$，按原 Hermitian 规范
$$
N(Y)=34,\quad N(W)=72,\quad
t_0=\langle Y,W\rangle=37-3\delta .
$$
对实际行 $L$ 定义完整五坐标算子
$$
P_{L,s}=I+(s-1)G_5\bar L^tL/N(L).
\tag{5}
$$
R601 的 whole theta、half-period 中心和绝对锚已经支付
$$
\nu^\flat|_{Y\in p}=\lambda(P_{Y,-\kappa})_*\nu^\flat,\qquad
\nu^\flat|_{W\in p^4}=\lambda^4(P_{W,\kappa^4})_*\nu^\flat .
\tag{6}
$$
因此令
$$
\mathscr R_n^Y=P_{Y,-\kappa}\mathscr R_n,\qquad
\mathscr R_n^W=P_{W,\kappa^4}\mathscr R_n ,
\tag{7}
$$
其逆域准确是 $P_{Y,-\kappa^{-1}}\mathbf x\in\mathscr R_n$
及 $P_{W,\kappa^{-4}}\mathbf x\in\mathscr R_n$，
连同显示的 $Y$ 一层、$W$ 四层深条件。
原五个坐标条件均按这些实际矩阵运输。

R601 已证明
$$
\mathscr R_n^Y\subset\{v_p(Y)=1,\ W\ {\rm unit}\},\qquad
\mathscr R_n^W\subset\{Y\ {\rm unit},\ v_p(W)=4\}.
\tag{8}
$$
它们的原 $Z,Q,r,c,d$ 坐标均为单位。
故 (4)、(7) 三域严格不交。
特别在第一像上只有 (3) 的负 $W$ 行，在第二像上只有正 $Y$ 行；
不能把原 $\log(Y/W)$ 从 (4) 延伸到它们。

定义实际积分
$$
I_n^Y=\int_{\mathscr R_n^Y}\ell\,d\nu^\flat,\qquad
I_n^W=\int_{\mathscr R_n^W}\ell\,d\nu^\flat .
\tag{9}
$$

## 3. 原测试的完整转置与质量项

在固定 $\kappa$ 处定义
$$
h=\frac{(1+\kappa)(37+3\delta)}{34},\qquad
k=\frac{(1-\kappa^4)(37-3\delta)}{72}.
\tag{10}
$$
整个五坐标矩阵给
$$
W(P_{Y,-\kappa}\mathbf x)=W-hY,\qquad
Y(P_{W,\kappa^4}\mathbf x)=Y-kW.
\tag{11}
$$
因此置
$$
s_Y=\frac{3\delta-h}{1-h},\quad
t_Y=\frac{4-2h}{1-h},\qquad
s_W=\frac{1-3\delta k}{1-k},\quad
t_W=\frac{2-4k}{1-k}.
\tag{12}
$$
这些参数属于 $\mathcal O$，不要求其分子是单位。
实际分母均为单位，因为
$$
1-h\equiv-\frac{3(1+\omega)}{17},\qquad
1-k\equiv\frac{19+3\omega}{36}\pmod p,
$$
$$
N(1-h\bmod p)=9/289,\qquad
N(1-k\bmod p)=313/1296 .
\tag{13}
$$
$313\equiv57\bmod64$，已被当前射线排除。

对任意固定于本素数的 $s,t\in\mathcal O$，定义
$$
L_n(s,t)=d_p\int_{\mathscr R_n}
        \log\langle A_0+sc+td\rangle\,d\nu^\flat .
\tag{14}
$$
这里 $A_0+sc+td\equiv a_ZZ\bmod p^n$ 为单位，所以原单位域完整。
三个独立 sigma 的质量都为零；
故在 (14) 中可减去 $\log\langle a_ZZ\rangle$。
同理 (11) 中提出 $1-h$ 或 $1-k$ 所产生的
$\log\langle1-h\rangle$、$\log\langle1-k\rangle$
乘的是整个矩形质量零，准确消失。
这一步没有给某个未知参考的 log 质量赋零。

于是 (6)、(8)–(14) 得到真实测试身份
$$
\boxed{
I_n^Y=-\lambda L_n(s_Y,t_Y),\qquad
I_n^W=\lambda^4 L_n(s_W,t_W),\qquad
R_n=L_n(1,2)-L_n(3\delta,4).
}
\tag{15}
$$
所有参数均与深度 $n$ 无关。

## 4. 两条完整负矩级数及首两行的共同秩一关系

记原单位负矩
$$
I_{1,m}=\int_{Z\ {\rm unit}}Z^{-m}\,d\nu_{f_1},\qquad
I_{3,m}=\int_{Z\ {\rm unit}}Z^{-m}\,d\nu_{f_3}.
$$
特别 $I_1=I_{1,5}$ 是 R533/R540 的原负五矩，
$I_3=I_{3,3}$ 尚无此处可用的零断言。

定义实际四输入生成函数
$$
\mathcal A_{s,t}(z)=
 \Sigma(a_Qz)\sigma(2\delta z)\sigma(sz)\sigma(tz),\qquad
\mathcal B_{s,t}(z)=
 \Theta(a_Qz)\sigma(2\delta z)\sigma(sz)\sigma(tz),
$$
$$
A_m(s,t)=[z^m]\mathcal A_{s,t},\qquad
B_m(s,t)=[z^m]\mathcal B_{s,t}.
\tag{16}
$$
两个完整角型分别只有 $5\bmod6$ 和 $3\bmod6$。
R599 同一个四独立深核心及 log 展开于是给
$$
\boxed{
\begin{aligned}
L_n(s,t)=\frac{d_p\beta^{4n}}{42}\Bigg[
&\sum_{j\ge0}(4+6j)!\Omega^{5+6j}
 A_{5+6j}(s,t)a_Z^{-5-6j}
 \kappa^{(5+6j)n}I_{1,5+6j}\\
-&\sum_{j\ge0}(2+6j)!\Omega^{3+6j}
 B_{3+6j}(s,t)a_Z^{-3-6j}
 \kappa^{(3+6j)n}I_{3,3+6j}\Bigg].
\end{aligned}}
\tag{17}
$$
这是实际四输入矩的整级数，不用一个质量代替 $\Theta$。
每项除 log 的 $m$ 外整有界，其赋值下界为
$mn-v_p(m)$，所以对所有 $n\ge1$ 一致收敛。

最低两系数准确为
$$
B_3(s,t)=2\delta st,\qquad
A_5(s,t)=2\delta a_Q^2 st .
$$
令
$$
\gamma_3=-\frac{2\delta}{21a_Z^3},\qquad
\gamma_5=\frac{8\delta a_Q^2}{7a_Z^5},\qquad
\Delta=2-12\delta=-10-24\omega .
\tag{18}
$$
则
$$
L_n(s,t)=d_p\beta^{4n}st
 \{\gamma_3\Omega^3\kappa^{3n}I_3
   +\gamma_5\Omega^5\kappa^{5n}I_1\}
+p^{9n}\mathcal O .
\tag{19}
$$
R599 的两个原单位系数恰为
$$
c_3=\Delta\gamma_3,\qquad c_5=\Delta\gamma_5,
\quad
c_5=\frac{4312960+1031168\omega}{117649}.
$$
尤其
$$
\boxed{\gamma_5/\gamma_3=-12a_Q^2/a_Z^2}
\tag{20}
$$
与 $s,t$ 无关。
所以单在同一个深度用这两像消去 $I_3$，同时也会消去首 $I_1$；
两行不能被当作独立的二乘二单位矩阵。

为保完整高项，定义真正积分差
$$
J_n(s,t)=L_n(s,t)-\frac{st}{\Delta}R_n .
\tag{21}
$$
其整条级数由 (17) 将 $A_m,B_m$ 分别换成
$$
A_m(s,t)-\frac{st}{\Delta}
   \{A_m(1,2)-A_m(3\delta,4)\},
$$
以及同式的 $B_m$ 得到。
故 $\Theta$ 支从九次开始、$\Sigma$ 支从十一次开始，
准确有
$$
\boxed{
J_n(s,t)\in p^{9n}\mathcal O,\qquad
J_{n+1}(s,t)-\beta^4\kappa^3J_n(s,t)
       \in p^{9n+3}\mathcal O .
}
\tag{22}
$$
第二个界使用每个实际次数 $m\ge9$ 的完整因子
$\beta^{4(n+1)}\kappa^{mn}(\kappa^m-\kappa^3)$，
不能只从第一个界估计得出。
当前 $p\ge71$，$mn-v_p(m)\ge9n$，尾项全受控。

## 5. 三域总系数与无穷多个单位地点

定义完整实际有理式
$$
r_Y(\kappa)=-\frac{s_Yt_Y}{\Delta},\qquad
r_W(\kappa)=\frac{s_Wt_W}{\Delta},\qquad
\boxed{\mathscr C(\lambda,\kappa)=1+\lambda r_Y(\kappa)
                                      +\lambda^4r_W(\kappa).}
\tag{23}
$$
(12) 的全部分母和 $\Delta$ 均为当前单位：
$N\Delta=4\cdot109$，$109\equiv45\bmod64$ 已被排除。
这是固定 $\lambda,\kappa$ 有理式；不含隐藏的 $p$ 依赖矩、深度
或周期系数。

准确的常数项为
$$
r_Y(0)=-\frac{14785+13963\omega}{981},\qquad
r_W(0)=\frac{935106+1970400\omega}{10678621}.
\tag{24}
$$
因而 $\mathscr C(L,0)$ 是常数项一的非零四次多项式。
置 $D_0=96107589=3^2\cdot109\cdot313^2$，清分母后的固定多项式为
$$
\boxed{
\begin{aligned}
F(T)&=D_0T^4\,\mathscr C(-1/T,0)\\
&=96107589T^4+(1448471665+1367941147\omega)T^3\\
&\hspace{25mm}+8415954+17733600\omega .
\end{aligned}}
\tag{25}
$$
它与 $p,n,\lambda,\kappa,\Omega,I_1,I_3$ 均无隐藏依赖。

应用
[固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)，
原射线中满足 $\pi_0\mid F(\bar\pi_0)$ 的素数在 $p\le X$ 内至多
$O_F(\sqrt X\log X)$。
删除这个显示的稀疏坏集后，原正密度射线仍含无穷素数，且
$$
\boxed{\mathscr C(\lambda,\kappa)\in\mathcal O^\times.}
\tag{26}
$$
这是“原射线减去稀疏坏集”的量词，未宣称 (26) 在射线每个素数成立。
式 (25) 只支付当前固定系数，不能用于 $p$ 依赖的 $I_1$ 本身。

## 6. 三域外的真正补集直接返回原负五矩

令
$$
\mathscr D_n=\mathscr R_n\sqcup\mathscr R_n^Y\sqcup\mathscr R_n^W,
\qquad
C_n^{\rm out}=\int_{\mathcal O^5\setminus\mathscr D_n}
                    \ell\,d\nu^\flat .
\tag{27}
$$
(27) 是整个三域外积分，保 (3) 两个分别的单位指示，
没有附加 $F$ 单位条件。
定义
$$
H_n=-\lambda J_n(s_Y,t_Y)+\lambda^4J_n(s_W,t_W).
\tag{28}
$$
(15)、(21)、(23) 给完整同来源等式
$$
\boxed{
\mathcal T=
 \mathscr C(\lambda,\kappa)R_n+H_n+C_n^{\rm out}.
}
\tag{29}
$$
同时
$$
H_n\in p^{9n}\mathcal O,\qquad
H_{n+1}-\beta^4\kappa^3H_n\in p^{9n+3}\mathcal O.
\tag{30}
$$
所有 $n$ 使用同一个 $\mathscr C$。

在 (26) 的无穷素数子集上定义
$$
\boxed{
\mathcal I_n^{[3]}=
\frac{(1-\beta^4\kappa^3)\mathcal T
      -C_{n+1}^{\rm out}+\beta^4\kappa^3C_n^{\rm out}}
{\mathscr C(\lambda,\kappa)\,
 d_pc_5\Omega^5\beta^{4(n+1)}
 \kappa^{5n+3}(\kappa^2-1)} .
}
\tag{31}
$$

**定理。** 对每个 $n\ge1$，
$$
\boxed{
\mathcal I_n^{[3]}\in\mathcal O,\qquad
\mathcal I_n^{[3]}-I_1\in p^{4n}\mathcal O,\qquad
\lim_{n\to\infty}\mathcal I_n^{[3]}=I_1 .
}
\tag{32}
$$

**证明。** 对 (29) 取相邻深度差，
(31) 的分子准确等于
$$
\mathscr C\{R_{n+1}-\beta^4\kappa^3R_n\}
 +H_{n+1}-\beta^4\kappa^3H_n .
$$
第一项由 R599 的原负五返回，除 (31) 分母后为
$I_1+p^{4n}\mathcal O$。
第二项由 (30) 除去显示的 $\kappa^{5n+3}$ 后仍在
$p^{4n}\mathcal O$。
其余分母由 (1)、R599 的 $c_5$ 单位及 (26) 全为单位。
这同时支付 (32) 的整性、误差和极限。证毕。

因此若 $I_1=0$，(31) 的实际分子必须属于
$p^{9n+3}\mathcal O$；
若 $I_1\ne0$，则在 $4n>v_p(I_1)$ 时其准确赋值为
$$
5n+3+v_p(I_1).
\tag{33}
$$
这里比较的是完整原总行与真正三域外补集，不是新增的辅助负矩。

## 7. 原 carry 权和所有补偿的准确接入

仍保 R594 的同一个
$\widetilde{\mathcal W}_n(F,G)$ 及其中七个真实余类矩。
按 R599 原定义
$$
O_n=\int_{\{F\ {\rm unit}\}\setminus\mathscr R_n}
       \widetilde{\mathcal W}_n\ell\,d\nu^\flat,\qquad
K_n=\int_{\mathscr R_n}
       (\widetilde{\mathcal W}_n-\beta^n)\ell\,d\nu^\flat .
$$
已付原四输出返回是
$$
\mathcal E_n=\beta^{-n}(O_n+K_n)=\mathcal T-R_n .
$$
因此 (27) 的完整实际外域准确为
$$
\boxed{
C_n^{\rm out}=\beta^{-n}(O_n+K_n)-I_n^Y-I_n^W .
}
\tag{34}
$$
这先保整个 $O_n+K_n$，再减掉由完整核心识别的两个真实像。
单独的带权 $O_n$ 不能用两个无权像替换。
如果直接在某个像上积分 $\widetilde{\mathcal W}_n\ell$，
则 $F,G$ 及七个余类矩仍须逐个按 (5) 转置。

将 (29) 的高项一并归到补偿中，也可写完全准确的恒等式
$$
C_n^{\rm out}+H_n
=(1-\mathscr C)\mathcal T+\mathscr C\,\beta^{-n}(O_n+K_n).
\tag{35}
$$
R590 的旧六支权若代替新权，其完整 $O_n+K_n$ 不变，
故 (34)、(35) 和 (31) 也不变。
这个结论没有把单独的外域积分或内部权差称为不变。

若作原反证假设 $J'_S=J'_T=0$，
(29) 只给
$$
C_n^{\rm out}=-\mathscr C R_n-H_n .
\tag{36}
$$
(31) 中的显式原中央项此时才消失。
三域对首负三、负五项的总系数为单位，
仍不许可删除 (36) 的完整补偿，也未排除 $I_1=0$。
主目标所需的全中央非零尚须继续处理该真实余域。

## 8. 精确文件与已支付范围

- [check-r605-original-two-core-images-and-complete-complement.js](../scripts/check-r605-original-two-core-images-and-complete-complement.js)
- [check-r605-original-two-core-images-and-complete-complement.json](../scripts/check-r605-original-two-core-images-and-complete-complement.json)

脚本在 $\mathbf Q(\omega)[\kappa]$ 上用 BigInt 有理算术验证
全五坐标的两投影、两个原观察的完整转置、(12) 的实际参数、
两个首矩的共同比例、(24)–(25) 的全部系数及分母范数。
它保存固定 $F\bar F\in\mathbf Z[T]$ 的完整系数，
没有用素数采样代替 (26) 的计数证明。
来源核心引用 R601 的完整中心及 half-period 证明；
所有 log 质量、全负矩级数、相邻深度尾界和原 carry 补偿
均在本文逐项支付。
