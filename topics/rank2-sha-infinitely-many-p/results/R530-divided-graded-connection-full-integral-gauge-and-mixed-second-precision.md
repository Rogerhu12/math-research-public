# R530 — p 除分级连接、全目标整共轭与混权第二精度

日期：2026-11-14。**状态：已证明。** R486 的零增权连接不只可以取整系数幂。
其 $p$ 次幂减本身还可以在真实来源中整除 $p$；
在每个齐次权的完整原目标中，同一个除法也由实际整单位共轭支付。

这给同一个 primitive 右核和完整左核的混权模 $p^2$ 关系，
而不是把旧模 $p^2$ 等式直接除 $p$ 后多读一位。
两次 Gaussian 共轭及全部进位都显式保留。
在累计系数次数不超过 $p-2$ 时，还能选同一个整移位，
使这个 $p$ 除来源算子对全部权同时可逆。

若只需模 $p^\nu$，其来源特征值可换成不超过 $p^\nu-1$ 的整数代表，
得到实际同预算、范数至多放大 $p^\nu-1$ 的来源操作。
这个有限精度替代不再被称为特征零微分恒等。
本篇没有由这些操作推断物理像饱和、混权核稳定或新的中央零。

## 1. 同一来源连接与完整 t 坐标目标

保 R486 的实际来源
$$
\mathcal B_m=X_{\rm alg}^{\,m}a(t)^{c_m}
\mathcal O[t]_{\le e_m},
\qquad
c_m=\lceil m/68\rceil,\quad
e_m=\lfloor11m/34\rfloor-4c_m,
$$
$$
a=t(t-1)(7+4t+16t^2),\qquad
b_{m,j}=X_{\rm alg}^{\,m}a^{c_m}t^j .
\tag{1}
$$
$X_{\rm alg}$ 是来源中的独立分级变量；
其物理值仍是 R486 的
$X=\Theta_{\rm reg}\exp(a_0\epsilon/17)$。
原零增权连接满足
$$
\nabla b_{m,j}=j b_{m,j}.
\tag{2}
$$
只在 R486 已付的来源、整性及 conductor 返回范围工作。

令 $\Gamma_+$ 为这份原矩阵实际使用的完整目标。
采用 R486 的整参数变换
$$
\epsilon_t=(t/w)^s\epsilon,\qquad
t^s=p\epsilon_t,
$$
可写成
$$
\Gamma_+=\mathcal O[t,\epsilon_t]/
(t^s-p\epsilon_t,\epsilon_t^3,t^{\ell_+}\epsilon_t^2),
\quad 0<\ell_+<s.
\tag{3}
$$
$\ell_+$ 按原 $m_{13}$ 或含 conductor 的实际目标固定，
没有为本篇另加行。
其合法整基是
$$
t^j\ (0\le j<s),\qquad
t^j\epsilon_t\ (0\le j<s),\qquad
t^j\epsilon_t^2\ (0\le j<\ell_+).
\tag{4}
$$
以 $n=j+is$ 编号，$0\le n<L_+=2s+\ell_+$ 连续。
定义
$$
\delta(t)=t,\qquad \delta(\epsilon_t)=s\epsilon_t.
$$
它保持 (3) 的全部关系，且
$$
\boxed{\delta=\operatorname{diag}(0,1,\ldots,L_+-1)}
\tag{5}
$$
于 (4) 中。
这就是原 $\nu\mathsf D$，不是把 $\epsilon$ 当成微分常量的新导子。

## 2. 原齐次物理矩阵的整单位共轭

若不使用 conductor，取 $r_c=C=0$、$q_{\mathfrak c}=1$。
若使用 R473/R486 的已付返回，则取
$$
\mathfrak c=X_{\rm alg}^{C}q_{\mathfrak c}(t),
\quad C=10980,\quad
r_c=\operatorname{ord}_0q_{\mathfrak c},
\quad q_{\mathfrak c}/t^{r_c}\in\mathcal O[[t]]^\times,
$$
并保原固定有限坏集及完整目标范围。
置
$$
d_0=13+r_c,\qquad A(t)=a(t)/t.
$$
每条实际原列准确为
$$
M_m b_{m,j}=U_m\,t^{d_0+c_m+j},
\tag{6}
$$
其中
$$
\boxed{
U_m=U_*\,X^m A(t)^{c_m},\qquad
U_*=c_*U_0(w/t)^{13}X^C
\frac{q_{\mathfrak c}(t)}{t^{r_c}}.
}
\tag{7}
$$
所有因子都是该原目标中的整单位。
$U_0$ 含完整 $P_{134}$、charge $40$ 和 Gaussian；
conductor 的 $C/17$ 电荷也留在 $U_*$ 中。
(7) 只在这个原局部目标中取逆，不是在整个角曲线上除 conductor。

令
$$
h_m=d_0+c_m,\qquad
\mathscr L_m=
\mathsf M_{U_m}(\delta-h_m)\mathsf M_{U_m}^{-1}.
\tag{8}
$$
等价地
$\mathscr L_m=\delta-\delta U_m/U_m-h_m$。
由 (6) 得
$$
\boxed{M_m\nabla=\mathscr L_mM_m.}
\tag{9}
$$
它是整个三块目标的整身份。
原跨块后的 $t^{h_m+j}$ 仍有导数特征值 $h_m+j$，
并未把其 $p$ 或 $p^2$ 因子删去。

## 3. 来源与目标上的除 p 都有实际整性

对整数 $z$ 定义
$$
Q_p(z)=\frac{z^p-z}{p}\in\mathbf Z.
\tag{10}
$$
分母为 $p$ 的多项式在本篇只通过明确的整数特征值使用；
不能对任意未经支付的矩阵自由调用整数值多项式演算。

固定整数移位 $\alpha$。定义来源算子
$$
\mathscr Q_\alpha=Q_p(\nabla+\alpha).
$$
在原有限基上，
$$
\boxed{
\mathscr Q_\alpha b_{m,j}=Q_p(j+\alpha)b_{m,j}.
}
\tag{11}
$$
因此 $\mathscr Q_\alpha$ 是同预算的实际整来源算子，
并满足特征零的准确等式
$$
p\mathscr Q_\alpha
=(\nabla+\alpha)^p-(\nabla+\alpha).
$$
它不改变权、角因子或次数帽；乘同一个 conductor 后仍按 R486 返回。

目标端定义
$$
\boxed{
\mathscr F_{m,\alpha}
=
\mathsf M_{U_m}\,
Q_p(\delta-h_m+\alpha)\,
\mathsf M_{U_m}^{-1}.
}
\tag{12}
$$
中间矩阵在 (4) 上准确对角，其第 $n$ 项为
$Q_p(n-h_m+\alpha)\in\mathbf Z$。
故 (12) 是整个原目标上的整算子，并且
$$
\boxed{
p\mathscr F_{m,\alpha}
=(\mathscr L_m+\alpha)^p-(\mathscr L_m+\alpha).
}
\tag{13}
$$
单位共轭使取幂的次序严格正确。

**定理 1。**
$$
\boxed{
M_m\mathscr Q_\alpha
=\mathscr F_{m,\alpha}M_m
}
\tag{14}
$$
在完整整目标中准确成立。

**证明。** 对每条真实来源基列用 (6)。
$\delta-h_m+\alpha$ 在 $t^{h_m+j}$ 上的特征值为 $j+\alpha$，
所以两端同为
$Q_p(j+\alpha)U_m t^{h_m+j}$。
若该幂在原目标因截断为零，两端也都为零。$\square$

(11) 和 (12) 同时支付了除 $p$。
仅从一个已知模 $p^2$ 的未除恒等式除 $p$，
通常只剩模 $p$；本定理允许保留原模 $p^2$ 的整精度。

## 4. 同预算、同一左右提升的完整混权关系

本节的“同一个实际 $M$”限定为显示的
$\mathcal B_{\le N}$ 物理矩阵，或同一个
$\mathfrak c\mathcal B_{\le N}$ 返回子格的物理矩阵。
如果手中只有原 $\mathcal A=\mathcal O[S,T,U]$ 呈示的左右核，
尚未证明裸 $\mathscr Q_\alpha$ 保持任意 $\mathcal A$；
不能自动用其左核消去扩大来源中的
$M_{\mathcal B}\mathscr Q_\alpha P$。
使用 conductor 时，右提升也必须属于所声明的同一个返回子格。
本节不把扩大来源的核条件移给未经支付的原来源。

令
$$
P=\sum_mP_m,\qquad Z_m=M_mP_m.
$$
取共同参考算子
$$
\mathscr F_{*,\alpha}
=
\mathsf M_{U_*}Q_p(\delta-d_0+\alpha)
\mathsf M_{U_*}^{-1},
\qquad
\mathscr R_{m,\alpha}=
\mathscr F_{m,\alpha}-\mathscr F_{*,\alpha}.
\tag{15}
$$
不要求 $P$ 只有一个模 $68$ 余类。
将 (14) 逐权相加，得到准确整身份
$$
\boxed{
M\mathscr Q_\alpha P
=
\mathscr F_{*,\alpha}MP+
\sum_m\mathscr R_{m,\alpha}Z_m.
}
\tag{16}
$$

**定理 2。** 若 $P_2$ 是同一个实际 $M$ 的模 $p^2$ 右核提升，
$\lambda_2$ 是该 $M$ 的完整模 $p^2$ 左核提升，
则
$$
\boxed{
\sum_m
\left\langle\lambda_2,\,
\mathscr R_{m,\alpha}M_mP_{2,m}
\right\rangle
=0\pmod{p^2}.
}
\tag{17}
$$

**证明。** (11) 使
$\mathscr Q_\alpha P_2$ 仍是同一个来源中的整向量，
所以左核杀掉 (16) 左边。
$\mathscr F_{*,\alpha}$ 已是整目标算子，
所以真正右核杀掉第一项。余下即 (17)。$\square$

这里没有要求 $\mathscr Q_\alpha P_2$ 仍是右核，
也没有要求某个单独权分量或电荷观察保持右核。
$\mathscr R_{m,\alpha}$ 同时依赖 $m,c_m$ 和原目标单位；
不能将 (17) 拆成每个权或每个电荷分别为零。

若只使用
$(\nabla+\alpha)^p-(\nabla+\alpha)$
的未除版本与同一模 $p^2$ 数据，
只能立即推出 (17) 左边属于 $p\mathcal O$。
这里由真实 (11)–(12) 额外支付了完整模 $p^2$ 关系。
这说明本篇新增的是整精度接口；
不宣称由一个数值未知的配对已经得到了非零矛盾。

同样证明适用于任何已付模 $p^\nu$ 左右提升。
第二、第三障碍的解释仍须按 R479、R481 使用同一个修正，
不能把不同的 $P_\nu,\lambda_\nu$ 拼在一起。

## 5. 两次 Gaussian 共轭和真实 carry

将 (7) 写成
$$
U_m=U_*H_m(t)e^{G_m},\qquad
H_m(t)=\Theta_{\rm reg}(t)^m A(t)^{c_m},
$$
$$
G_m=\frac{ma_0}{17}\epsilon
=\gamma_m(t)\epsilon_t,\qquad
\gamma_m(t)=\frac{ma_0}{17}(w/t)^s .
\tag{18}
$$
$H_m$ 是该目标中的原普通整单位；
$U_*$ 的共同 Gaussian、$P_{134}$ 和 conductor 继续完整保留。

令
$$
Q_h=Q_p(\delta-h_m+\alpha).
$$
它在 (4) 中对角，因而保持 $\epsilon_t$ 的全部幂次滤过。
乘 $G_m$ 至少提高一层，故三次交错乘积全部为零。
因此完整 Gaussian 共轭准确为
$$
\boxed{
e^{G_m}Q_he^{-G_m}
=Q_h+[G_m,Q_h]
+\tfrac12[G_m,[G_m,Q_h]].
}
\tag{19}
$$
这里使用了 $Q_h$ 保滤过，不能仅从 $G_m^3=0$
就对任意目标算子断言同样的三项公式。

令 $g_{n'n}$ 是乘 $G_m$ 的**实际整矩阵项**，
包括 $t^s=p\epsilon_t$ 产生的因子。
写
$q_n=Q_p(n-h_m+\alpha)$。
则
$$
\boxed{
[G_m,Q_h]_{n'n}=g_{n'n}(q_n-q_{n'}),
}
\tag{20}
$$
$$
\boxed{
\tfrac12[G_m,[G_m,Q_h]]_{n'n}
=
\frac12\sum_j g_{n'j}g_{jn}
(q_n-2q_j+q_{n'}).
}
\tag{21}
$$
两条式子都在原完整合法基上读取。

例如乘一个
$\gamma_{m,k}t^k\epsilon_t$
会把总特征值 $n$ 移到 $n+s+k$；
如果普通 $t$ 阶跨过 $s$，该矩阵项同时有一个真实 $p$。
所以第一交换子本身即可产生第三块的 carry。
第二交换子给剩余的二次 Gaussian 项。
(20)–(21) 没有把 $\gamma_m(t)$ 换成它的常量，
也没有删除原 raw 目标中的活高项。

最后还须按 (12)、(18) 共轭全部 $H_m$ 和 $U_*$。
普通单位的高尾同样可以跨块，不能把 (19) 单独当成整个
$\mathscr F_{m,\alpha}$。

## 6. 一个移位使全部来源同时可逆

令
$$
E_N=\max_{m\le N,\ e_m\ge0}e_m.
$$
假设
$$
E_N\le p-2.
\tag{22}
$$
在 $\mathbf F_p$ 中考虑不超过 $E_N+1$ 个值
$$
\{Q_p(j)\bmod p:0\le j\le E_N\}.
$$
可选一个 $z\in\{0,\ldots,p-1\}$ 不属于此集合，
并令
$$
\alpha=pz.
$$
因为
$$
\boxed{Q_p(j+pz)\equiv Q_p(j)-z\pmod p,}
\tag{23}
$$
所有 (11) 的特征值都是 $p$ 单位。
(23) 直接由二项式展开模 $p^2$ 得到。

**定理 3。** 在 (22) 下，可用同一个 $\alpha=pz$ 使
$$
\boxed{
\mathscr Q_\alpha:\mathcal B_{\le N}
\longrightarrow\mathcal B_{\le N}
}
\tag{24}
$$
成为 $\mathcal O$ 整自同构。
它保原 primitive 性、全部权支持和来源预算，
也保同一实际 conductor 返回。

它不使 $\mathscr R_{m,\alpha}$ 分别为零，
不证明 $\mathscr Q_\alpha$ 保实际右核，
更不使原物理评价像自动饱和。
这个移位的作用是支付来源操作本身的可逆性，
不是增加中央条件。

## 7. 有限精度的实际有界系数替代

精确整数 $Q_p(j+\alpha)$ 可能很大。
若当前只使用模 $p^\nu$，对每个真实 $j$ 选择
$$
q_{j,\alpha}^{[\nu]}\in\{0,\ldots,p^\nu-1\},
\qquad
q_{j,\alpha}^{[\nu]}
\equiv Q_p(j+\alpha)\pmod{p^\nu}.
$$
定义同一原来源中的算子
$$
\boxed{
\mathscr Q_\alpha^{[\nu]}b_{m,j}
=q_{j,\alpha}^{[\nu]}b_{m,j}.
}
\tag{25}
$$
它仍是实际整数来源操作，准确有
$$
\mathscr Q_\alpha^{[\nu]}
\equiv\mathscr Q_\alpha\pmod{p^\nu},
\qquad
\|\mathscr Q_\alpha^{[\nu]}f\|_1
\le(p^\nu-1)\|f\|_1
\tag{26}
$$
于同一 canonical 多项式系数范数。
原固定返回和已有 $C^m$ 范数成本继续另计。
使用第6节的移位时，(25) 在模 $p^\nu$ 中也可逆；
其整特征值均为 $p$ 单位。

因此在模 $p^\nu$ 的 (16)、(17) 中，
可用 (25) 代替来源端的精确 $\mathscr Q_\alpha$，
不损失那一位精度。
无需把 $j^p$ 的特征零系数大小强行付给一个只使用有限精度的操作。

但 (25) 不再满足特征零等式
$p\mathscr Q=(\nabla+\alpha)^p-(\nabla+\alpha)$。
若某条全局解析论证需要这个特征零微分身份，
仍必须使用精确算子并支付它的系数增长。
本篇只给所列有限精度的替代，不混淆两种用途。

## 8. 原预算与后续接口

(11)、(25) 不增加来源权或系数次数，
并完整保原角因子和 conductor。
(12) 保原目标所有行，
(17) 保同一 $P_2,\lambda_2$ 的两次进位和第三精度接口。
它们提供比直接除旧模 $p^2$ 等式更完整的一位真实关系。

下一步若要用 (17) 证明非零，
须在原实际混权右核和可提升左核上计算其
$\mathscr R_{m,\alpha}$ 配对，
保 (19)–(21) 及全部普通单位高尾。
不能把任意源自目标的 Fermat 商单位、一个齐次权的 Smith 因子，
或 (24) 的来源可逆性冒称原第二余核非零。

三条原完整中央没有传播到这些操作后的任意来源。
所以无论使用精确系数还是 (25) 的有界代表，
都不能仅凭“零增权”将 R418 的 $a_I,b_I$ 改成更小值。
原主问题仍需实际混权像或完整中央的跨 $p$ 非零输入。
