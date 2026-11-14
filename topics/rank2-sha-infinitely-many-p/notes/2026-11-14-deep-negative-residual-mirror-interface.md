# 原 3C 的负镜轴 residual 接口（未登记为新结论）

2026-11-14。接 R524。以下是原已付几何真行的准确等价形式；
当前没有由它得到额外的像排除，所以不占 R526 或其他结果编号。

保 $Y_3=3C$、$S=s-r$、$\eta=\eta_0=t^hv$、
$\eta^2=0\bmod t^S$，以及原
$$
I_+=(t^S,(\zeta-\eta)^2).
$$
在 $P$ 处由同一个原参数 $t$ 定义 Cartier 除子
$\widetilde P\subset Y_3$，其长度为三。
它在 $C$ 上限制为 $P$；在 $P$ 外理想取整个结构层。
令 $T_S=S\widetilde P$。

在 $R=k[[t]][\zeta]/(t^S,\zeta^3)$ 中，
$$
\zeta^3=(\zeta-\eta)^2(\zeta+2\eta)
$$
准确成立。逐系数也给
$$
\operatorname{Ann}_R((\zeta-\eta)^2)=(\zeta+2\eta).
$$
确实，对 $a+b\zeta+c\zeta^2$，乘积为零等价于
$a=2b\eta$；剩下的 $\zeta^2$ 也属于
$(\zeta+2\eta)$，因为
$(\zeta+2\eta)(\zeta-2\eta)=\zeta^2$。

所以残余理想准确为
$$
I_-=(t^S,\zeta+2\eta),
$$
其商长为 $S$。
它对应原形式负镜轴
$$
Y_-=\psi e^{-2\eta}=\psi^3/g^2\pmod{t^S},
$$
不同于 R511 的正镜轴 $g^2/\psi$。

由于 $t^S$ 在 $Y_3$ 的局部环中是非零因子，
任一 $I_+\to\mathcal O_{Y_3}$ 的同态由其在 $t^S$ 上的值决定，
嵌入总商环后可写成乘 $a/t^S$。
条件 $aI_+\subset(t^S)$ 恰给 $a\in I_-$。
因此
$$
\operatorname{Hom}_{Y_3}(I_+,K_X|_{Y_3})
=
I_-\otimes K_X|_{Y_3}(T_S).
$$
这里整个正规三层都保留。
在 $P$ 的原框中，
$(A+B\zeta+C_2\zeta^2)$ 乘 $t^S$ 后属于 $I_-$，
准确等价于 R498 的 $A-2\eta B$ 正则，
因为 $\eta^2=0\bmod t^S$。

于是原几何左行可以作为
$H^0(Y_3,K_X|_{Y_3}(T_S))$
在这个负镜轴长度 $S$ 评价的核读取。
它仍须通过全部原列测试，边界行 $\rho$ 仍须通过 R524
的两连接；没有因此多一个可选行。

本等价本身不证明该 canonical 评价核消失，
也没有证明 R521 的单点残数能扩成其中的截面。
原 $g$ 的 Gaussian 和完整中央参数没有变化。

尤其没有将它提升到 $\Gamma/p^2$：
在原 raw $\bar\Gamma$ 中 R502 的 $\zeta^3$ 仍有活项，
只有已取 $t^r$ 高像并通过 R498 的指定三厚化后才可使用上面的等式。
若在模 $p^2$ 强行把 $\zeta^3$ 置零，
会删去活 $V_1$、原 $w^s=p\epsilon$ carry 以及同一首次修正。
因此该负镜轴目前只提供首像对偶的等价读法，
不能借它为任何新的中央零或第二障碍赋值。
