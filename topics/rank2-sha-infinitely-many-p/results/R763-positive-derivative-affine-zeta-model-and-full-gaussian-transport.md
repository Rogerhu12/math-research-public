# R763 — 新正导数坐标的完整仿射 ζ 模型、三同源与真实 Gaussian 两位

日期：2026-11-15。**状态：下述原三格的完整来源与有限目标公式已证明；R760 的全惰性斜率改善及原中央非零仍未证明。**

R760 使用实际三坐标 $(S,T,\mathcal U)$，其中
$\mathcal U=(\partial_zS)^6$，不是原第三算术来源 $U_{136}$。
本篇把新增坐标准确写到原椭圆曲线上的一个仿射 ζ 方向，
给出三同源的完整仿射作用，并将其写进同一个 Gaussian carry 环。
特别，去掉其总 charge 的 Gaussian 后，新增坐标仍有一个实际单位
的一次 $p$ 分母；不能把它当成旧 $\mathcal W_D$ 的又一普通列。

## 1. 原全局坐标与已知微分方程

保固定 $b=17$（公式同样适用于原 $b=1$ 框）：
$$
y^2=x^3+b,\quad x'=2y,\quad y'=3x^2,\quad
\zeta'=-x,\quad \sigma'=\zeta\sigma,
$$
$$
t=-b/x^3,\qquad \Theta=x\sigma^2,\qquad
Q=1+\frac{x\zeta}{y}.
\tag{1}
$$
这里 Q 是本篇的仿射坐标，不是前文某个 carry 权或椭圆点。
在原 $z=0$ 支上，$t=-bz^6+\cdots$、$\Theta(0)=1$、$Q(0)=0$。

置 $R=\zeta+y/x$。直接微分得到
$$
R'=-2b/x^2,\qquad \Theta'=2R\Theta,\qquad
t'=-6t\,y/x,\qquad Q=Rx/y.
\tag{2}
$$
故
$$
\boxed{
t\,\partial_t\log\Theta=-Q/3,\qquad
6t(1-t)Q'=(1+2t)Q-2t.
}
\tag{3}
$$
这正是 R305、R525–526 已付的原 Theta 对数方程，
本篇不把 (3) 另认作新独立算术条件。

为核定全部符号，若 $Q=\sum_{n\ge1}q_nt^n$，则
$$
q_1=-2/5,\qquad
(6n-1)q_n=(6n-4)q_{n-1}\quad(n\ge2).
\tag{4}
$$
它与 R305 的
$[t^n]\log\Theta=(3n)^{-1}(1/3)_n/(5/6)_n$
完全相符。惰性 $p=6s-1$ 时，(4) 在 $n=s$ 有真实共振分母；
不能把低于该指标的约化方程延伸为整盘自由 ODE。

## 2. 原新增坐标的准确六次式

用 R305 的同一个完整四次因子
$$
P_4(t)=(1-t)(1+8t)
 \left(1+\frac47t+\frac{16}7t^2\right),
\qquad
S=-\frac tb\,\Theta^{17}P_4(t).
\tag{5}
$$
定义实际多项式
$$
\boxed{B(t,Q)=34Q P_4(t)-6P_4(t)-6tP_4'(t).}
\tag{6}
$$
由 (2)，
$$
S'=-\frac tb\,\Theta^{17}\frac yx\,B(t,Q).
$$
又 $(y/x)^6=-b(1-t)^3/t$，所以完整特征零身份是
$$
\boxed{
\mathcal U=(S')^6
=-\frac{t^5(1-t)^3}{b^5}\,
       \Theta^{102}B(t,Q)^6.
}
\tag{7}
$$
所有原角因子都在 (6) 内，没有先除掉 $P_4$。
原点处 $B(0,0)=-6$，故 (7) 给
$\mathcal U=6^6z^{30}+\cdots$，与 R760 的
$\mathcal U(w)=6^6w^5+\cdots$ 相同。

同一式也核定 R759 的连接截面：
$$
\boxed{
D_S=\zeta S-\frac1{34}S'
=\frac yx\,S\left(\frac3{17}
                 \frac{t(tP_4)' }{tP_4}-1\right).
}
\tag{8}
$$
(8) 中显示的商按完整乘积解释；乘回 S 后所有 $P_4$ 分母消去。
尤其 ζ 在 $D_S$ 中确实消失，但在 $S'$ 及 (7) 中保留。

### 2.1 有限六次覆盖和原点的真实归一化

令 $F=\mathbf C(t,\Theta)$。R760 的周期论证给 Q 在 F 上超越。
因此由 (7)
$$
\boxed{[F(Q):F(\mathcal U)]=6.}
\tag{9}
$$
证明只需作仿射变量 $V=B(t,Q)$；
$\mathcal U=c(t,\Theta)V^6$，其中 $c\in F^\times$，
而 $X^6-\mathcal U/c$ 在 $F(\mathcal U)[X]$ 中不可约。
例如在 $F[\mathcal U]$ 上对素元 $\mathcal U$ 用 Eisenstein。
这是在已付旧场 F 上的六次覆盖，不声称
$\mathbf C(S,T)$ 与 F 已经相等。

在原点完成环内，先准确除出 (7) 的已知五阶零，置
$$
V_U=-\frac{b^5\mathcal U}
          {t^5(1-t)^3\Theta^{102}}=B(t,Q)^6.
\tag{10}
$$
选择常数项 $-6$ 的六次根，便唯一恢复 B，再由
$$
Q=\frac{B+6P_4+6tP_4'}{34P_4}
\tag{11}
$$
恢复实际 Q。对 $p\nmid2\cdot3\cdot7\cdot17b$，
这在形式完成环内为 étale 的单位反演。

(10) 除的是实际已知的 $t^5$，不是一个原来源端的免费单位。
把 (11) 用于全局多项式格时，仍须支付该五阶零、所有分母和
原次数帽；它不将 Q 新列放进旧 $\mathcal W_D$。

## 3. 完整三同源在新增方向上的作用

取原 $\delta^2=-3$，置
$$
v=1-4t,\qquad d=1+8t,\qquad
\varphi(t)=-27t/v^3 .
$$
R756 的同一 absolute sigma 身份为
$$
\sigma(\delta z)=\delta x(z)\sigma(z)^3,\qquad
x(\delta z)=-xv/3,\qquad \Theta(\delta z)=v\Theta^3.
\tag{12}
$$
对其中的 x 式微分，保左边的 $\delta$，得到
$$
y(\delta z)=-\frac{d}{3\delta}y,\qquad
\frac{y(\delta z)}{x(\delta z)}
=\frac d{\delta v}\frac yx.
\tag{13}
$$
对 sigma 式取对数导数则是
$$
\delta\zeta(\delta z)=3\zeta(z)+2y/x.
\tag{14}
$$
代入 (1)，得到完整仿射式
$$
\boxed{
Q(\delta z)=\frac{3vQ+12t}{d}.
}
\tag{15}
$$
于是新增三变量模型上的真正有理映射为
$$
\boxed{
\Psi_3:(t,\Theta,Q)\longmapsto
 \left(\varphi(t),\,v\Theta^3,\,
                  \frac{3vQ+12t}{d}\right).
}
\tag{16}
$$
新的 Q 方向没有被三次幂化；它是保全部常数项的仿射作用。

对任一多项式 $\sum_{j=0}^J f_j(t,\Theta)Q^j$，
其拉回准确为
$$
\sum_{j=0}^J
 f_j(\varphi(t),v\Theta^3)\,
 \frac{(3vQ+12t)^j}{d^j}.
\tag{17}
$$
所以 Q 次数至多 J，有限新分母包含实际 $d^j$；
其余 $f_j$ 的旧角拉回按 R756–758 单独计算。
不能因新增方向是 affine 就删去 (17) 的极帽。

记 $\mathcal E=\Theta\partial_\Theta$。完整法向 jets 满足
$$
\boxed{
\mathcal E\Psi_3^*=3\Psi_3^*\mathcal E,\qquad
\partial_Q\Psi_3^*=\frac{3v}{d}\Psi_3^*\partial_Q,
}
\tag{18}
$$
以及
$$
\mathcal E^i\partial_Q^j\Psi_3^*
=3^i(3v/d)^j\Psi_3^*\mathcal E^i\partial_Q^j.
\tag{19}
$$
(19) 中这些法向导数不作用在 t 上，所以没有漏掉系数的导数。
对另加乘子须再用完整 Leibniz 公式，不把 (19) 当成任意乘子的公式。

原 germ
$(t,\Theta(t),Q(t))$ 满足 (16)，而 $\varphi'(0)=-27$ 为单位。
因此任何在原点正则的实际来源，有限接触阶经 (16) 保持，
不会因最高 Theta charge 乘三而将接触也乘三。
(18) 在好素数处可逆，也没有新增一个独立消失条件。

## 4. 新坐标在完整 Gaussian carry 环中的原两位

现在取原惰性
$$
p=6s-1>101,\qquad L=(p^2-1)/6=s(p-1),\qquad
w=z^6,\quad c=[w^s]\log(\sigma/z).
$$
R614 给 $v_p(c)=-1$。置
$$
\epsilon=w^s/p,\qquad a=34pc\in\mathcal O^\times,\qquad
S=w\,v_S(w)e^{a\epsilon}.
\tag{20}
$$
R614 的完整原分子证明 $v_S(0)=1$，且其所有次数 $<L$ 的系数整。
这里使用原 S 的真实 $v_S$，不把它指定成任意整单位。
令
$$
\partial=w\,d/dw,\qquad B_S=v_S+\partial v_S.
$$
在同一形式特征零式中准确有
$$
S'=6z^5e^{a\epsilon}
       (B_S+as\epsilon v_S),
$$
因此
$$
\boxed{
\mathcal U
=6^6w^5e^{6a\epsilon}
       (B_S+as\epsilon v_S)^6.
}
\tag{21}
$$
它同时保总 charge 的 Gaussian 与真正 affine ζ 项。

特别在 R750 同一目标
$$
\Gamma^+=\mathcal O[w,\epsilon]/
 (w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2)
$$
中，完整两位为
$$
\boxed{
\begin{aligned}
\mathcal U=6^6w^5\bigl\{
&B_S^6
+6a\epsilon(B_S^6+s v_SB_S^5)\\
&+a^2\epsilon^2
 (18B_S^6+36s v_SB_S^5+15s^2v_S^2B_S^4)
\bigr\}.
\end{aligned}}
\tag{22}
$$
所有项来自实际 (21)；不能只保指数的 $6a$ 和 $18a^2$。
Euler 导数 $\partial\epsilon=s\epsilon$ 保该目标的整个定义理想，
因此该计算没有改变两条十三行或原 carry 关系。
目标所需原系数严格低于 $3s<L$，R614 已付的整性足够；
不延伸到其真实首坏端点 L。

在原点按首项正规化后，(21) 还给精确身份
$$
\boxed{
\frac{w\mathcal U}{6^6S^6}
=\left(1+\partial\log v_S+as\epsilon\right)^6.
}
\tag{23}
$$
右侧的常数项为1。在本原单位分支可唯一取六次根；
其 $\epsilon$ 系数为 $as$，是单位。
$\partial\log v_S$ 是实际 regular 新方向，既不是零，也不能免费
当作旧 $F(t,\Theta)$ 的有理元素。

### 4.1 去掉总 Gaussian 后仍有实际首分母

定义真正的原级数
$$
\widetilde{\mathcal U}
=\frac{\mathcal U}{6^6w^5}\,e^{-204cw^s}.
$$
因 $6a\epsilon=204cw^s$，(21) 给
$$
\widetilde{\mathcal U}
=(B_S+as\,w^s v_S/p)^6.
\tag{24}
$$
于是
$$
[w^s]\widetilde{\mathcal U}
=[w^s]B_S^6+\frac{6as}{p}.
$$
第一项整，且 $6s=p+1$，所以
$$
\boxed{
p[w^s]\widetilde{\mathcal U}
\equiv a\not\equiv0\pmod p,\qquad
v_p([w^s]\widetilde{\mathcal U})=-1.
}
\tag{25}
$$
这是每个本范围惰性 p 的原指定系数，不是某个可选择模型。
因此“把新 U 按 charge204 去 Gaussian 后视作 R614 的同类整分子”
确实不成立。正确来源是保全部 affine 因子的 (21)–(24)。
(25) 是非中央分母结论，不能代替原 $J'_S$ 的非零。

## 5. 三同源在去 Gaussian 坐标中的完整修正

令
$$
\sigma^\circ=\sigma e^{-cw^s},\qquad
\zeta^\circ=\zeta-6scz^{6s-1},\qquad
\Theta^\circ=\Theta e^{-2cw^s},
$$
$$
Q^\circ=1+x\zeta^\circ/y,\qquad
\chi(w)=x/(zy)=-1+O(w),\qquad
t_3=c(3-\delta^{p+1})\in\mathcal O.
\tag{26}
$$
$\chi$ 是同一个原点支上的实际单位。
$t_3$ 的整性来自原 $\delta^{p+1}\equiv3\bmod p$，
不宣称它必为单位。

由定义，
$$
Q=Q^\circ+6sc\,\chi w^s,\qquad
\chi(\delta z)=\frac vd\chi(z).
\tag{27}
$$
结合 (12)、(15)，准确得到
$$
\boxed{
\begin{aligned}
\Theta^\circ(\delta z)
 &=v(\Theta^\circ)^3e^{2t_3w^s},\\
Q^\circ(\delta z)
 &=\frac{3vQ^\circ+12t}{d}
   +6s\,t_3\frac vd\,\chi(w)w^s.
\end{aligned}}
\tag{28}
$$
第一行与 R756 的 $Y_U$ 式完全一致；第二行是新增仿射方向的
实际修正。它在 carry 环中为
$$
6sp\,t_3(v/d)\chi\,\epsilon .
\tag{29}
$$
所以模 p 的低轴不见这个项，不代表完整首 Bockstein 或
下一位可删除它。混合 Theta charge 与 Q 次数时，(28) 的指数及
仿射项必须按原单项式一起展开，保同一个实际来源。

## 6. 对 R760 全三格斜率门的使用范围

本篇已经支付：

- 新正导数坐标在原全局三变量上的准确六次来源与有限覆盖；
- 原三同源在新增方向上的全仿射式、真实极点与可逆法向 jets；
- 新坐标进入原有限 carry 环时的全部 $\epsilon,\epsilon^2$ 系数；
- 去掉总 Gaussian 仍然存在的实际单位首分母；
- 去 Gaussian 三同源的完整指数和仿射第二位修正。

这些式子保 R760 已付的普通有界测度和三变量复增长。
它们尚未把原三个固定中央的失败传播为这一个新三格的全惰性
有序饱和范数界。尤其 (10)、(17)、(22)、(28) 都不能作为
删除原次数帽、$G_0/U_0$、十三行或全来源修正 R 的理由。

R760 的严格充分门仍是同一真实三格上的
$a_I+3b_I<6$；无条件惰性包络仍为 $(a_I,b_I)=(0,3)$。
后继若使用 (7) 的新增方向，须在其实际多项式来源上支付
全部行、全部 ordered saturated flag 及原中央算术关系。
本篇没有赋给 $\mathcal U$ 一个原 $U_{136}$ 的中央零，
也没有把 (25) 的非中央分母当作主目标证书。

## 依赖

[R305](R305-jzero-original-first-central-row-and-holomorphic-primitive.md)；
[R525](R525-original-multiweight-wronskian-and-growing-kernel-support.md)；
[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)；
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R756](R756-original-norm-three-map-and-complete-canonical-return.md)；
[R758](R758-full-norm-three-multiplier-space-and-optimal-leading-budget.md)；
[R760](R760-positive-derivative-three-coordinate-grid-and-full-slope-threshold.md)。

全文为原恒等式的符号推导；没有新增数值运行或可重算输出。
