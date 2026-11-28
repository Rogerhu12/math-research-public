# 原 Fermat 六次曲线的 quadric：有界三次原函数与混合 Cartier 第三层

日期：2026-11-28。状态：原 $e,K_4$ 非同时消失仍开放。

本篇接续
[原 genus-four/Fermat-six 笔记 §§14–15](2026-11-28-original-genus-four-global-Raynaud-vanishing.md)，
只使用同一曲线上的原函数和已锁定的相对 Cartier 标架。
新的结论是：原 $K_4$ 在 $e=0$ 时，准确成为
$P^3P_{1,2}\omega_{3,2}$ 的全纯 Cartier 常数；
无条件式还保留一个明确的 $e$ 修正。
这不是原第六混合层 $\mathfrak b_6$ 的重新命名。

## 1. 原模型与两个 quadric 函数

保持
$$
p=6k-1\ge41,\quad N=k-1,\quad m=3k-1,\quad
s^2=-3,\quad v=-6s,\quad c=-4/v,\quad
\rho^3=2,\quad \rho\in\mathbf F_p,\quad b_0^3=c.
$$
在原相位中 $v^p=-v$、$b_0^p=-b_0$。
原椭圆曲线及其不变导子是
$$
E:\ V^2=U^3+v^2,\qquad
\omega=\frac{dU}{2V},\qquad D=d/\omega.
$$
使用原规范
$$
D\Psi=\delta,\qquad D\mathcal R=\Psi,\qquad
\Psi^2=U^p+2\delta\mathcal R,\qquad
\delta\in\mathbf F_p^\times.
$$
在 $O$ 的 exact 参数 $\tau$ 中，$d\tau=\omega$，且
$$
U=\tau^{-2}+O(\tau^4),\quad
V=-\tau^{-3}+O(\tau^3),\quad
\Psi=\tau^{-p}+\delta\tau+O(\tau^{5p}).
$$
这些是原特征 $p$ 函数的展开，不约化完整特征零 elliptic logarithm。

原 Fermat 六次曲线 $Z:x^6+y^6=1$ 上
$h_*=\omega_{2,2}$，$\omega=-b_0h_*$，并有
$$
P=P_{2,2}=-\frac{\Psi}{b_0\delta},\qquad
x^6=\frac{V-v}{V+v}.
$$
保持原 $P_{a,b}$，定义已下降到同一 $E$ 的函数
$$
\mathcal A=xP_{1,2}+x^{-1}P_{3,2},\quad
\mathcal B=xP_{1,2}-x^{-1}P_{3,2},\quad
\mathcal W=P_{1,2}P_{3,2}-P^2.
$$
原 (G4.93)–(G4.98) 给
$$
\begin{aligned}
D\mathcal A&=\frac vU\mathcal B-\frac2{b_0},&
D\mathcal B&=\frac vU\mathcal A,\\
\mathcal B&=\sum_{j=0}^N t_jU^{3j+1},&
\mathcal A&=\frac{2UV}{v}\mathcal B_U,
\end{aligned}
\tag{Q.1}
$$
其中所有 $t_j\in\mathbf F_p^\times$，且
$$
C_{\rm rel}(\mathcal B\omega)=\alpha\omega',\qquad
\alpha=-\frac{2\rho e}{b_0\delta}\in\mathbf F_p.
\tag{Q.2}
$$
这里及以下 prime 表示原相对 Frobenius target；
$C_{\rm rel}$ 对底域常数线性。

## 2. 三次有界积分及真正的第三混合层

先取无常数项的多项式
$$
\mathcal G(U)=\frac1v\sum_{j=0}^N
       \frac{(3j+1)t_j}{3j+2}U^{3j+2}.
$$
由 (Q.1)，$D\mathcal G=\mathcal A$。
再在
$\mathcal H=V\sum_{j=0}^Nh_jU^{3j}$ 中唯一解
$D\mathcal H=\mathcal G$。
实际三角矩阵为
$$
D(VU^{3j})=(6j+3)U^{3j+2}
                  +6jv^2U^{3j-1};
$$
$j=0$ 的第二项为零。
对角 $6j+3$ 从 $3$ 到 $p-2$，全为单位。
最后置
$$
\mathcal I=\sum_{j=0}^N\frac{h_j}{2(3j+1)}U^{3j+1}.
$$
这里的对角 $2(3j+1)$ 从 $2$ 到 $p-3$，同样全为单位。
因此得到了完整原函数链
$$
\boxed{
D\mathcal I=\mathcal H,\qquad
D\mathcal H=\mathcal G,\qquad
D\mathcal G=\mathcal A,\qquad
\mathcal A=D^3\mathcal I,
}
$$
$$
\operatorname{pole}_O(\mathcal G)\le p-1,\quad
\operatorname{pole}_O(\mathcal H)\le p-2,\quad
\operatorname{pole}_O(\mathcal I)\le p-3.
\tag{Q.3}
$$
没有从 $C(\mathcal A\omega)=0$ 抽象假设低极阶原函数；
三个具体矩阵已支付所有极点界及唯一性。

记
$$
C_{\rm rel}(\mathcal I\omega)=\beta_{\mathcal I}\omega',
\qquad
a_{-5}=[\tau^{-5}]\mathcal A,\quad
i_{-2}=[\tau^{-2}]\mathcal I.
$$
由于 $\mathcal I\omega$ 只有阶小于 $p$ 的单个极点，其 Cartier 输出全纯。
$\Psi\mathcal I\omega$ 也只有 $O$ 一个极点，留数定理给
$$
\beta_{\mathcal I}+\delta i_{-2}=0.
$$
又 $D=d/d\tau$，故
$a_{-5}=(-2)(-3)(-4)i_{-2}=-24i_{-2}$。
三次分部积分于是严格得到
$$
\boxed{
C_{\rm rel}(\Psi^3\mathcal A\omega)=\mathfrak a_3\omega',
\qquad
\mathfrak a_3=-6\delta^3\beta_{\mathcal I}
            =-\frac{\delta^4}{4}a_{-5}.
}
\tag{Q.4}
$$
源可有 $4p$ 阶极，但 (Q.3) 证明其输出确为全纯。
仅凭 CM 角色或“只剩一个标量”并不足以得出本式。

更一般，三次分部积分给
$$
C_{\rm rel}(\Psi^r\mathcal A\omega)
=-r(r-1)(r-2)\delta^3
 C_{\rm rel}(\Psi^{r-3}\mathcal I\omega)
\qquad(r\ge3).
$$
对任何 $\mathcal I\in U K[U^3]$、极阶至多 $p-3$，
(G4.99) 同一个 Laurent 留数证明适用，并不要求其系数在 $\mathbf F_p$：
$C(\Psi\mathcal I\omega)=0$、
$C(\Psi^2\mathcal I\omega)=-\beta_{\mathcal I}U'\omega'$、
$C(\Psi^3\mathcal I\omega)=2\beta_{\mathcal I}V'\omega'$。
因此原前七层准确为
$$
\boxed{
\frac{C_{\rm rel}(\Psi^r\mathcal A\omega)}{\omega'}
=
\begin{cases}
0,&r=0,1,2,4,\\
\mathfrak a_3,&r=3,\\
-10\mathfrak a_3U',&r=5,\\
40\mathfrak a_3V',&r=6.
\end{cases}}
\tag{Q.5}
$$
这只陈述显示的有限范围。

## 3. 保留全部 $e$ 项的原 $p-5$ 系数

本节补全 (G4.102) 中先在 $e=0$ 下读取的系数。
在 $Y\to E$ 上令 $x=\eta$，$\nu=x^{-1}\omega$。
原恒等 $\nu=x^pF_Q\omega$，连同
[R1061 §19](../results/R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)
的完整四次 kernel 微分，给出
$$
\frac{C_{\rm rel}(\Psi^r\nu)}{\omega'}
=x'\begin{cases}
e,&r=1,\\
2e(v-V')/U',&r=2,\\
3eU',&r=3,\\
4(v-V')e+4\delta^2K_4,&r=4.
\end{cases}
\tag{Q.6}
$$
$r=0$ 的输出为零。
例如 $r=2,3$ 使用原 $t(-Q)=t''(-Q)=t'''(-Q)=0$、
$t'(-Q)=e$ 及
$D_Rh+h^2=U'$；$r=4$ 保留 R1061.74 之前的全部第三类项。
这里 $x'$ 是 cover 的 relative target 坐标。

在 $D^p=0$、$C(\omega)=0$ 的原标架中，对函数 $f$ 有
$$
-D^{p-1}f=
F_{\rm rel}^*
 \left(\frac{C_{\rm rel}(f\omega)}{\omega'}\right).
$$
右边只拉回 Cartier 的**标量系数**，不是拉回一个微分。
把 (Q.6) 逐次代入 Leibniz 公式，置
$h_p=(v-V^p)/U^p$，得到完整函数恒等式
$$
\boxed{
D^{p-5}x^{-1}
=-\frac{x^p}{6\delta^4}
 \left[
  \delta^2K_4+
  e\{-\Psi^3+3h_p\Psi^2-3U^p\Psi+v-V^p\}
 \right].
}
\tag{Q.7}
$$
它也可逐阶核准：
$D^{p-2}x^{-1}=ex^p/\delta$、
$D^{p-3}x^{-1}=ex^p(\Psi-h_p)/\delta^2$、
$D^{p-4}x^{-1}=ex^p(U^p+\Psi^2-2h_p\Psi)/(2\delta^3)$。
$h_p$ 中的 $v$ 保持底域标量；不能将它改成 $v^p$。

在 $O$ 取 $x=1$ 的不分歧支。
(Q.7) 左边正则，故括号整体正则。
其中所有奇函数项的 Laurent 常数为零；
$\Psi^2/U^p$ 的首常数为一，所以括号的常数准确是
$\delta^2K_4+3ve+ve$。
原 $x(-\tau)=x(\tau)^{-1}$，而 $p-5$ 为偶。
再用 $(p-5)!=-1/24$，可得
$$
\boxed{
[\tau^{p-5}]x
=\frac{4K_4}{\delta^2}+\frac{16ve}{\delta^4}.
}
\tag{Q.8}
$$
只读取低于 $p$ 的阶数，没有坐标 first-$p$ carry。

原 (G4.100)–(G4.102) 的共同负主部
$c_0=-\rho/(b_0\delta)$ 于是给出无条件式
$$
a_{-5}
=-\frac{8\rho K_4}{b_0\delta^3}
 -\frac{32\rho ve}{b_0\delta^5}.
$$
代回 (Q.4) 与 (Q.2)，最终得到
$$
\boxed{
\mathfrak a_3
 =\frac{2\rho\delta}{b_0}K_4-4v\alpha,\qquad
e=K_4=0
\ \Longleftrightarrow\
\alpha=\mathfrak a_3=0.
}
\tag{Q.9}
$$
因此两项原障碍分别是同一 quadric 的零次与第三次混合 Cartier 读数。
(Q.9) 没有将 $\mathfrak b_6$、$\sigma$ 或 $\Lambda$ 认作单位。

## 4. 回到原有序 mixed 槽及 quadric 差

为清楚保留绝对 Cartier 的相位，
以下一律使用原 $Z$ 上的 $C_{\rm abs}$。
由定义
$$
P_{1,2}\omega_{3,2}=\frac{\mathcal A+\mathcal B}{2}h_*,
\qquad
P_{3,2}\omega_{1,2}=\frac{\mathcal A-\mathcal B}{2}h_*.
$$
$P=-\Psi/(b_0\delta)$、$\omega=-b_0h_*$，
并且 $\alpha^p=\alpha$、$\mathfrak a_3^p=-\mathfrak a_3$。
因此 (Q.4)、(G4.99) 给
$$
\boxed{\begin{aligned}
C_{\rm abs}(P^3P_{1,2}\omega_{3,2})
 &=\frac{\mathfrak a_3-2\alpha V}{2b_0^3\delta^3}h_*,\\
C_{\rm abs}(P^3P_{3,2}\omega_{1,2})
 &=\frac{\mathfrak a_3+2\alpha V}{2b_0^3\delta^3}h_* .
\end{aligned}}
\tag{Q.10}
$$
若 $e\ne0$，两个 $Vh_*$ 项一般亚纯，不能先删除。
在 $e=0$ 时二者同时成为全纯，并准确等于
$$
\boxed{
C_{\rm abs}(P^3P_{1,2}\omega_{3,2})
=C_{\rm abs}(P^3P_{3,2}\omega_{1,2})
=\frac{\rho K_4}{b_0^4\delta^2}h_* .
}
\tag{Q.11}
$$

另令 $\mathcal F=P_{1,2}P_{3,2}$。
完整的 $d(P^3\mathcal F)$ 以及
$C(P^4h_*)=C(d(P^5)/5)=0$ 给
$$
\boxed{
C_{\rm abs}(P^2\mathcal W h_*)
=-\frac{\mathfrak a_3}{3b_0^3\delta^3}h_*.
}
\tag{Q.12}
$$
这也是原 $K_4$ 的实际 quadric source；在 $e=0$ 时，其系数为
$-2\rho K_4/(3b_0^4\delta^2)$。
原 $\mathcal W$ 的最高 $U^p$ 项仍完整保留在函数中，
但这类 Cartier 读取不能把那个最高系数的单位性替代为 (Q.12) 非零。

由 (Q.5)、(G4.99)，若 $e=K_4=0$，
则这两个有序 mixed 槽的 $P^r$ 插入对 $0\le r\le5$ 全部为零。
$r=6$ 仍可含原 $\mathfrak b_6$。
故本篇支付了真正的 Leibniz 与相邻槽比较，
没有宣称它已经排除共同零，也没有把未付的高层常数省掉。

## 来源与审阅范围

本篇只消费原 Fermat 笔记 (G4.88)–(G4.104)、
R1061 的同一 relative kernel 与原 $K_4$，
以及具体多项式的三角积分。
o2_high_coefficient 独立纸核 (Q.3)–(Q.9)：
三次有界积分、留数 $-1/4$、全 $4ve$ 常数、
relative Frobenius 标量拉回及 Wilson 因子均相符。
(Q.10)–(Q.12) 显式保留原绝对 Cartier 的 $p$ 次根和有序槽，
不使用一般 Massey、Jacobi 或非退化形式的替代结论。
全篇无数学程序执行、无素数窗口。

root 亲读并核 R1061 §19 的完整第三类 kernel，逐式核三角积分、三次分部积分、Q.7 的三个实际导数、4ve 常数与 Wilson 因子，并从相对 Cartier 到绝对有序槽核全部 p 次根；Q.10–Q.12 的亚纯与全纯范围一致。未增加数学执行。
