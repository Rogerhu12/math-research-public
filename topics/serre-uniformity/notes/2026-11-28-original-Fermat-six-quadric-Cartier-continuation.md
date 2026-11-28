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


## 5. 原 Picard 两个 jet 与一个完整 Leibniz 强迫式

令 $t=\Phi(U^m)$ 为原指定截面。
R1061 的同一 Picard 参数给
$D_Rt(-Q)=e$、$D_R^4t(-Q)=16ve+4\delta^2K_4$。
因此 (Q.2)、(Q.9) 也准确写成
$$
\boxed{
\alpha=-\frac{2\rho}{b_0\delta}D_Rt(-Q),\qquad
\mathfrak a_3=\frac{\rho}{2b_0\delta}D_R^4t(-Q).
}
$$
若 $t=UH_p(U^3)$，则
$$
\mathfrak a_3-6v\alpha
=\frac{192\rho v^4}{b_0\delta}H_p'(0).
\tag{Q.13}
$$
这里的第四阶读数是原固定曲线的 Picard jet；
没有把 Tate normal 方向或辅助谱导数换入。

由 (Q.1)、(Q.3)，
$D^4\mathcal I=v\mathcal B/U-2/b_0$。
先乘 $U$，再完整地四次分部积分，使用
$$
D^4U=120U^3+48v^2,\qquad
C_{\rm rel}(U\omega)=-\delta\omega',
$$
可得
$$
\boxed{
120\,\frac{C_{\rm rel}(U^3\mathcal I\omega)}{\omega'}
+48v^2\beta_{\mathcal I}
=v\alpha+\frac{2\delta}{b_0}.
}
\tag{Q.14}
$$
等式本身证明左侧输出全纯；未先假定高极源的输出是常数。
若 $e=K_4=0$，则 $\alpha=\beta_{\mathcal I}=0$，从而
$C_{\rm rel}(U^3\mathcal I\omega)=\delta\omega'/(60b_0)$。
这给真正的下一强迫列，但并不与已经证明的任何消失界矛盾。

## 6. 极阶 $2p-2$ 的 Lamé 零模及完整上下半段

本节的函数超出
[R1113](../results/R1113-original-finite-Lame-spectrum-and-jet-boundary.md)
中 $W\subset L((p+1)O)$ 的范围。
仍用同一算子
$$
\mathscr L=D^2-2U,\qquad
\ell_\pm=\frac{V\pm v}{U},\qquad
J_\pm=(V\mp v)^{2k}.
$$
原三挠核给 $D J_\pm=\ell_\pm J_\pm$、
$\mathscr L J_\pm=0$。
定义
$$
\boxed{
\mathcal Z=\ell_+^pJ_+-\ell_-^pJ_-
=\frac{V^p(J_+-J_-)-v(J_++J_-)}{U^p}.
}
\tag{Q.15}
$$
末式保留 $v^p=-v$。
由于 $D(\ell_\pm^p)=0$，有 $\mathscr L\mathcal Z=0$。

在 $Q$，$J_+$ 的零阶是 $6k=p+1$，足以消去
$\ell_+^p$ 的 $p$ 阶极；在 $-Q$ 同理。
所以 $\mathcal Z$ 没有有限极点。
它在 $V\mapsto -V$ 下不变，在 $U\mapsto\zeta U$ 下权为 $\zeta$，
故为 $U$ 的多项式，指数皆为 $1\bmod3$。
在 $O$ 展开 (Q.15) 的最高项，得到
$$
\mathcal Z=U\sum_{r=0}^{2k-1}z_rU^{3r},\qquad
\deg_U\mathcal Z=p-1,\qquad
\operatorname{lc}_U\mathcal Z=-\frac{2v}{3}.
$$
实际 $\mathscr L(U^j)$ 公式给
$$
\frac{z_{r+1}}{z_r}
=-\frac{(r+\frac16)(r+\frac23)}
 {v^2(r+1)(r+\frac43)}
\qquad(0\le r<2k-1).
\tag{Q.16}
$$
该有限范围内所有分子分母为单位。
接着的一项恰由 $r+\frac23=0$ 截止。

还有一个不依赖特征零正常性的完整多项式读法。
置
$$
G(z)=\sum_{r=0}^{2k-1}
 \frac{(\frac16)_r(\frac23)_r}{(\frac43)_r\,r!}z^r.
$$
则
$$
\boxed{
\mathcal Z=(2v)^{4k-1}U\,G(-U^3/v^2),\qquad
G(4w(1-w))=(1-w)^{4k-1}+w^{4k-1}.
}
\tag{Q.17}
$$
自足证明是直接在 (Q.15) 中代入
$w=(1-V/v)/2$、$U^3=-4v^2w(1-w)$。
分子变成
$$
-(2v)^{2k+1}w^{2k}(1-w)^{2k}
 \{(1-w)^{4k-1}+w^{4k-1}\},
$$
而 $U^{p+1}=(2v)^{4k}w^{2k}(1-w)^{2k}$。
再用 $(2v)^{p-1}=-1$，便得到 (Q.17) 的规范常数。
右边是 $w\leftrightarrow1-w$ 不变多项式，
其最高奇次项相消；由 (Q.16) 及常数项一，即识别为显示的 $G$。
这也给 $G$ 的最高系数 $-(4k-1)/4^{\,2k-1}$。

现在取 R1113.16、R1113.21 的**原**多项式
$$
\mathscr Lg=U^m,\qquad
g=\sum_{j=0}^Ng_jU^{3j+1},\qquad g_N=\frac14.
$$
它的逐项比正是 (Q.16) 的前 $k$ 项。
记 $z_N=[U^{3N+1}]\mathcal Z\ne0$。
原 $\mathcal B$ 的 (Q.1) 二阶式还给
$$
\mathscr L(U^{m+1}\mathcal B)=-\frac{2v}{b_0}U^m.
$$
完整高低分裂为
$$
\boxed{
\mathcal Z
=4z_Ng+\frac{2b_0z_N}{v}U^{m+1}\mathcal B.
}
\tag{Q.18}
$$
低半段由 $g_N=1/4$ 锁定；
跨中间边界的比值是
$z_{N+1}/z_N=-4/(3v^2)$，
与 $t_0=-2/(3b_0v)$ 给出的上半段首项完全相符。
其余项按 (Q.16) 和原 $t_j$ 递推逐项吻合。
特别，两半的非零 $\mathscr L$ 像互相抵消；
不能各自称为零模。

最后，原对称核在 $Q,-Q$ 的读取为
$C_{\rm rel}(J_\pm\omega)=U'\omega'$。
提出 $\ell_\pm^p$ 时，目标系数分别是
$(V'\mp v)/U'$，故
$$
\boxed{C_{\rm rel}(\mathcal Z\omega)=-2v\,\omega'.}
\tag{Q.19}
$$
此处必须使用相对 Cartier。
(Q.19) 是完整上下半段之和的读数，不把它的单位性归给其中任一半段。

## 7. 同一低半段的有界原函数与原第四 jet

令
$$
l=m+1=3k,\qquad R_0=\frac{g}{U^l},\qquad K=U D R_0,
\qquad F_Q=\left(\frac{V+v}{V-v}\right)^k.
$$
$\mathcal Z/U^l=\ell_+^pF_Q^{-1}-\ell_-^pF_Q$，
而原 $C_{\rm rel}(F_Q^{\pm1}\omega)=0$。
把 (Q.18) 除以 $U^l$ 后取相对 Cartier，得到
$$
\boxed{
C_{\rm rel}(R_0\omega)
=-\frac{b_0\alpha}{2v}\omega'
=\frac{\rho e}{v\delta}\omega'.
}
\tag{Q.20}
$$
这里 $R_0$ 的有限极点恰限制在 $Q,-Q$；
它不是以未指定的第三类微分替代原低半段。

更明确地，置
$$
\begin{aligned}
\mathcal V&=\operatorname{span}
 \{U^{-3k+1+3j}:0\le j\le k-1\},\\
\mathcal U&=\operatorname{span}
 \{VU^{-3k+2+3j}:0\le j\le k-2\}.
\end{aligned}
$$
$\mathcal V\omega$ 在 $Q,-Q$ 的极阶均小于 $p$，
每个 Laurent 指数皆不产生留数，故其 Cartier 输出全纯。
由
$D(V/U)=U-2v^2/U^2$，
$$
C_{\rm rel}(U^{-2}\omega)
=-\frac{\delta}{2v^2}\omega'\ne0.
$$
所以 $C_{\rm rel}|_{\mathcal V\omega}$ 的核维数恰为 $k-1$。
另一方面
$$
D(VU^a)=(2a+3)U^{a+2}+2av^2U^{a-1}
$$
把 $\mathcal U$ 映入 $\mathcal V$，其最底三角系数 $2av^2$ 全为单位，
故该映射单射、像恰为上述 Cartier 核。
因此
$$
\boxed{
e=0\quad\Longleftrightarrow\quad
\exists!\ H_0\in
VU^{-3k+2}\Bbbk[U^3]_{\le k-2},\qquad DH_0=R_0.
}
$$
在 $O$，$g_N=1/4$ 给 $R_0=\tau^4/4+O(\tau^{10})$，
而该空间中没有常数，故
$$
H_0=\frac{\tau^5}{20}+O(\tau^{11}).
\tag{Q.21}
$$
这是具体有限空间的有界原函数结论，没有使用
“pole $<p$ 的 exact differential 总能低阶积分”这一不成立的一般命题。

对 $\mathscr Lg=U^m$ 作同一实际 gauge $g=U^lR_0$，
使用 $2l=1$，得到
$$
D^2R_0+\frac{2V}{U}DR_0-\frac{v^2}{U^2}R_0=\frac1U,
\qquad
\boxed{DK=1+\frac{v^2}{U}R_0.}
\tag{Q.22}
$$
为读取原 $K_4$，使用算子 $\mathscr S=UD-V$。
它满足 $\mathscr S J_+=vJ_+$、$\mathscr S J_-=-vJ_-$，
以及
$\mathscr S(U^l\mathcal B)=vU^l\mathcal A$。
故 (Q.18) 给
$$
U^{-l}\mathscr S\mathcal Z=4z_NK+2b_0z_N\mathcal A.
$$
原四阶 kernel 的第三层准确为
$$
C_{\rm rel}(\Psi^3F_Q\omega)=3U'e\,\omega',
\qquad
C_{\rm rel}(\Psi^3F_Q^{-1}\omega)=-3U'e\,\omega'.
$$
第二式也直接由 $[-1]$ 的奇偶性得到。
于是提出两个 $\ell_\pm^p$ 后，
$$
C_{\rm rel}(\Psi^3U^{-l}\mathscr S\mathcal Z\,\omega)
=6v^2e\,\omega'.
$$
结合 (Q.4)，最终有
$$
\boxed{
\frac{C_{\rm rel}(\Psi^3K\omega)}{\omega'}
=\frac{3v^2e}{2z_N}-\frac{b_0}{2}\mathfrak a_3.
}
$$
特别
$$
\boxed{
e=0\quad\Longrightarrow\quad
C_{\rm rel}(\Psi^3K\omega)=-\rho\delta K_4\,\omega'.
}
\tag{Q.23}
$$
全纯性来自显示的完整函数恒等式。
$\mathscr S$ 的各个有理因子或高插入并未被误当作
R1113 原有限空间的自同态。

(Q.20)–(Q.23) 把两项障碍留在同一个低半段：
第一项检测 $R_0$ 的有界 primitive，
第二项是 $K=UDR_0$ 的第三次 $\Psi$ 插入。
(Q.19)、(Q.21) 的单位首项及 (Q.14) 的下一强迫列仍不足以排除两项同时为零；
原 $e,K_4$ 非同时消失的结论继续开放。

**新增审阅。** o2_high_coefficient 独立纸核新链的关键式，包括相对
$-2v$、完整上下半段、$C(R_0\omega)$、
有界 primitive 空间及 $\Psi^3K$ 的全部尺度与相位。
本节未执行数学程序，未增加有限素数窗口。


## 8. 同一低半段的二次 primitive 与完整五次有界链

保留 §7 的 $R_0,K$，定义实际二次函数
$$
\mathcal M_0=K^2-v^2R_0^2.
$$
由 $DR_0=K/U$、(Q.22) 直接得
$$
\boxed{D\mathcal M_0=2K.}
$$
写 $a_j=-3k+1+3j$，则还有精确有限式
$$
\boxed{
\mathcal M_0
=\sum_{j=0}^N\frac{2a_jg_j}{a_j+1}U^{a_j+1}.
}
\tag{Q.24}
$$
所有 $a_j+1$ 均为单位。
事实上右边的导数也是 $2K$。
左、右两边之差是 $U$ 的 Laurent 多项式，指数完全位于
$-p+1,\ldots,-1$，其中没有 $p$ 的倍数；
导数为零遂迫该差为零。
这直接支付了二次函数最高极部的消去，没有使用未知的 norm 常数。

尤其 $\mathcal M_0$ 在 $Q,-Q$ 的极阶至多 $m-1$，
在 $O$ 为 $\tau^2+O(\tau^8)$。
两个原一阶系统也完整保留：
$$
D(K+vR_0)=1+\frac vU(K+vR_0),\qquad
D(K-vR_0)=1-\frac vU(K-vR_0).
$$
它们不能被替换成齐次方程；二次 primitive 正来自两个常数项。

### 8.1. 第一积分障碍仍准确是原 $e$

在 (Q.23) 之前的完整 $\mathscr S$ 恒等式中，
改读一次 $\Psi$ 插入。
原
$C_{\rm rel}(\Psi F_Q\omega)=e\omega'$、
$C_{\rm rel}(\Psi F_Q^{-1}\omega)=-e\omega'$，
以及 $C_{\rm rel}(\Psi\mathcal A\omega)=0$，给
$$
C_{\rm rel}(\Psi K\omega)
=\frac{v^2e}{2z_NU'}\omega'.
$$
使用 (Q.24) 一次分部积分，准确得到
$$
\boxed{
C_{\rm rel}(\mathcal M_0\omega)
=-\frac{v^2e}{\delta z_NU'}\omega'.
}
\tag{Q.25}
$$
这是两个原三挠点处的第三类项，不是全纯常数。

令
$$
\begin{aligned}
\mathcal E_0&=U^{-3k+2}\Bbbk[U^3]_{\le k-1},\\
\mathcal E_1&=VU^{-3k+3}\Bbbk[U^3]_{\le k-2}.
\end{aligned}
$$
$\mathcal M_0\in\mathcal E_0$。
$\mathcal E_0\omega$ 只有 $Q,-Q$ 两个小于 $p$ 阶的极点，
其 Cartier 输出只有简单极点。
$\mu_3$ 角色排除全纯补项，所以该像包含在
$\Bbbk\,\omega'/U'$。
按两点留数及相对 Frobenius 的 $Q\leftrightarrow -Q$，
$$
C_{\rm rel}(U^{-1}\omega)=-\frac{\omega'}{U'},
$$
故该映射秩一。

$D:\mathcal E_1\to\mathcal E_0$ 的实际公式仍是
$D(VU^a)=(2a+3)U^{a+2}+2av^2U^{a-1}$。
其最底三角系数全为单位，因此它单射，
像恰为上述维数 $k-1$ 的 Cartier 核。
于是
$$
\boxed{
e=0\quad\Longleftrightarrow\quad
\exists!\ \mathcal M_1\in\mathcal E_1,\qquad
D\mathcal M_1=\mathcal M_0.
}
\tag{Q.26}
$$
这同时保留了原第三类障碍及严格极阶。

### 8.2. 下一全纯障碍准确是原 $K_4$

现在假定 $e=0$，写
$\mathcal M_1=V\sum_{j=0}^{k-2}h_jU^{b_j}$，
$b_j=-3k+3+3j$。
可直接逐项取
$$
\mathcal M_2
=\sum_{j=0}^{k-2}\frac{h_j}{2(b_j+1)}U^{b_j+1}
\in U^{-3k+4}\Bbbk[U^3]_{\le k-2},
\qquad D\mathcal M_2=\mathcal M_1.
$$
所有分母均为单位。
$\mathcal M_2\omega$ 在 $Q,-Q$ 的极阶至多 $m-3<p$，
其指数角色排除留数，所以输出全纯。
从 $\mathcal M_0=D\mathcal M_1$、
$\mathcal M_1=D\mathcal M_2$ 及 (Q.24)，
连续三次分部积分给
$$
C_{\rm rel}(\Psi^3K\omega)
=-3\delta^3C_{\rm rel}(\mathcal M_2\omega).
$$
因此 (Q.23) 精确变成
$$
\boxed{
C_{\rm rel}(\mathcal M_2\omega)
=\frac{\rho K_4}{3\delta^2}\omega'
\qquad(e=0).
}
\tag{Q.27}
$$

和 (Q.21) 同样，目标空间包含 $U^{-2}$，
其 Cartier 为 $-\delta\omega'/(2v^2)\ne0$。
逐基的最底三角系数给
$$
\boxed{
K_4=0\quad\Longleftrightarrow\quad
\exists!\ \mathcal M_3\in
VU^{-3k+5}\Bbbk[U^3]_{\le k-3},\qquad
D\mathcal M_3=\mathcal M_2
\quad(e=0).
}
$$
随后再逐项积分，无新障碍地得到唯一
$$
\mathcal M_4\in U^{-3k+6}\Bbbk[U^3]_{\le k-3},
\qquad D\mathcal M_4=\mathcal M_3.
\tag{Q.28}
$$
这里的“唯一”均在显示的空间内；不加入未定常数或 $p$ 次幂。

因此共同消失给出完整的原二次链
$$
\boxed{
D\mathcal M_0=2K,\qquad
D\mathcal M_j=\mathcal M_{j-1}\ (1\le j\le4),\qquad
K=\frac12D^5\mathcal M_4.
}
$$
在两点 $Q,-Q$，
$\mathcal M_j$ 的极阶至多 $m-1-j$；
在 $O$，全部首项由同一 exact 参数锁为
$$
\boxed{
\mathcal M_j=
\frac{2\tau^{j+2}}{(j+2)!}
+O(\tau^{j+8})\qquad(0\le j\le4).
}
\tag{Q.29}
$$
这些不是从局部 primitive 自动延拓到全局的断言：
(Q.26)、(Q.28) 的两个有限矩阵支付了实际全局存在性，
其余两步均为显示的有理 monomial 积分。

用 $D^p=0$，还可把同一结论写为一个确切原函数判据：
$$
\boxed{
e=K_4=0
\quad\Longleftrightarrow\quad
D^{p-5}K=0.
}
\tag{Q.30}
$$
正向由 (Q.29)。
反向若 $D^{p-5}K=0$，则 Leibniz 展开
$D^{p-1}(\Psi^rK)$ 对 $0\le r\le4$ 全为零，
因而这些插入的 Cartier 都为零。
先用 (Q.25) 前的一次读数得 $e=0$，
再由 (Q.23) 的三次读数得 $K_4=0$。
这里 $D$、$K$ 都是原 $E$ 上的实际函数与导子，
不是任意 Jordan 块中的指定坐标。

(Q.24) 的二次关系始终保留，尤其在共同零分支上，
$$
v^2(D^5\mathcal M_4)^2
-U^2(D^6\mathcal M_4-2)^2
=4v^2D^4\mathcal M_4.
$$
它由 $R_0=U(D^6\mathcal M_4-2)/(2v^2)$ 代入原 norm 得到，
并没有省去非齐次常数二。
当前仍须证明这条实际有限链不可能出现，
或利用保留的二次关系取得可消费的新限制。
首项的单位性本身不排除这条链。


**新增纸核。** o2_high_coefficient 独立核 (Q.24)–(Q.29)：
二次 primitive 的全部 $p$ 次核项排除、第三类 $U'^{-1}$ 相位、
两次实际有限空间的核维数、三次分部积分的 $-3\delta^3$，
以及五次链的所有首项均相符。没有数学程序执行。
