# R332：真实算子平移与反射使新面积的第1外矩同时为零

日期：2026-11-15。**原式纸面推导。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R331](R331-interior-constant-and-wide-moment-repair-pay-the-new-area-and-old-layer.md) 已经在同一个真实带常项弱圆上支付 $A_{-1,-3}$ 的完整第零外矩。本稿证明：该构造保留的反射与十二副本，实际上也准确支付它的第1外矩，且这一步不需要新增形状参数或重新调整已付门。

证明必须同时搬动原算子的显式 $x$ 因子；不能仅把三个外矩按坐标平移。原 $L,U$ 的平移产生 $R,S,P$，其额外项由此前已付的另一个完整面积准确消去。真正的第2外矩仍未支付，并且在第零、第1矩都为零后，单纯平移不再改变它。

主要来源：[R259 原 E8 式与真实尾](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R317 弱 hook 与 mixed 原式](R317-exact-weak-hook-mixed-correction-and-nonnegative-branch-obstruction.md)、[R325 完整块加法](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、[R328 新面积](R328-another-complete-Gaussian-area-excludes-homogeneous-weak-power-packets.md)及 R331。

## 1. 所用真实对象与两个面积

保持 R331 已选的实际几何、共同物理区间、右锚和 profiles。记
$$
u=f\cos\theta+g\sin\theta,\qquad D=f\odot f-u\odot u,
$$
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\qquad
Z_*=d_*L+e_*U.
$$
定义
$$
\tau_\theta=[Z_*,P](u;D),\qquad
A_j(\theta)=I_j(u,\tau_\theta),\quad j=0,1,2.
\tag{1}
$$
实际 Gaussian 面积另乘非零 $c_P$，因此零条件不变。

原三矩圆、弱 hook 和旧面积已准确给
$$
\mathfrak H(u;D)=0,\qquad
m_j(\theta):=I_j\!\left(u,J\{u''((f'')^2-(u'')^2)\}\right)=0,
\quad j=0,1,2.
\tag{2}
$$
本稿所证新增内容是 $A_1=0$ 对全部 $\theta$。不把 $A_2$ 列入结论。

## 2. 原 E8 在真实平移下怎样变

设 $T_\delta f(x)=f(x-\delta)$，写 $y=x-\delta$。右锚始终在全部输入支撑右方；同锚正 $J$ 的平移不会丢掉原常数。将原 R259 的八算子式逐项代入，得到以下准确算子恒等，右边均先在 $y$ 坐标作用再取 $T_\delta$：
$$
\begin{aligned}
P^{(\delta)}&=P,\\
R^{(\delta)}&=R+\delta P,\qquad
S^{(\delta)}=S+\delta P,\\
L^{(\delta)}&=L+\frac{\delta}{2}(S-R),\\
U^{(\delta)}&=U+\delta(R+2S)+\frac{3\delta^2}{2}P.
\end{aligned}
\tag{3}
$$
例如
$$
L(f,f)=ff'-\frac{x(f')^2}{2}
-\frac{x^2J((f'')^2)}4
+\frac{J(x^2(f'')^2+2(f')^2)}4.
$$
替换 $x=y+\delta$ 后，两个 $\delta^2J((f'')^2)$ 准确相消，剩
$\delta(S-R)/2$。$U$ 的 $\delta^2P$ 系数则确为 $3/2$，不能删除。

原 commutator 全槽身份为
$$
[S,P](u;D)=J(u''D''_{\rm slot}),\qquad
[R,P](u;D)=\frac13\{J(u''D''_{\rm slot})+\mathfrak H(u;D)\},
$$
其中 $D''_{\rm slot}$ 在本圆上表示 $(f'')^2-(u'')^2$，不是对一个 pointwise 平方只求两次导数。由(2)，两式分别为同一个 $J$ 槽及其 $1/3$。

因此(3)在整个真实弱圆上给
$$
\boxed{
\tau_\theta^{(\delta)}
=T_\delta\{\tau_\theta+\delta\zeta J(u''D''_{\rm slot})\},
\qquad \zeta=\frac{d_*+7e_*}{3}.
}
\tag{4}
$$
这里的额外 cubic 槽来自算子本身；并非只搬外积分的 $x$ 权。

## 3. 先付旧面积，才得到新面积的普通三角平移律

将(4)代入原三个 $I_j$，保 $I_2$ 的 $2u'v'$，得到
$$
\begin{aligned}
A_0^{(\delta)}={}&A_0+\delta\zeta m_0,\\
A_1^{(\delta)}={}&A_1+\delta A_0
+\delta\zeta(m_1+\delta m_0),\\
A_2^{(\delta)}={}&A_2+2\delta A_1+\delta^2A_0
+\delta\zeta(m_2+2\delta m_1+\delta^2m_0).
\end{aligned}
\tag{5}
$$
利用此前真正已付的(2)，才可化成
$$
\boxed{
(A_0,A_1,A_2)^{(\delta)}
=(A_0,\ A_1+\delta A_0,\
A_2+2\delta A_1+\delta^2A_0).
}
\tag{6}
$$
(6)不适用于任意尚未通过旧面积的 profiles。它也没有把非仿射变换当作实际几何控制。

## 4. 中心偶 pair 的真实奇偶性，包含所有原尾

现在看 R331 十二副本以前的基圆。它由真实右块、左镜像和成对强修正组成，所以 $f,g$ 都关于实际反射中心 $C_0$ 为偶函数。

暂用中心坐标 $y=x-C_0$ 写原算子，令
$$
d(y)=(f'')^2-(u'')^2.
$$
$f,u$ 偶，故 $d$ 偶。原三矩零使
$$
A=PD=Jd
$$
既紧又奇。另两个实际 primitive 是
$$
J_1^D=J(yd),\qquad
J_2^D=J\{y^2d+2((f')^2-(u')^2)\}.
$$
第一个 integrand 奇、总积分零，故 $J_1^D$ 为真实紧偶函数。第二个 integrand 偶、由第2矩总积分零，故 $J_2^D$ 为真实紧奇函数。这些结论由同一个右锚给出，不任意调整常数。

代入原 $L,U$，
$$
LD=ff'-uu'-\frac y2((f')^2-(u')^2)
-\frac{y^2}{4}A+\frac14J_2^D,
$$
$$
UD=y((f')^2-(u')^2)+yJ_1^D+\frac12J_2^D.
$$
因而
$$
\boxed{PD,\ LD,\ UD\text{ 均为紧奇函数}.}
\tag{7}
$$
单个 $L(f,f)$、$U(f,f)$ 一般不紧；紧性只在完整 $D$ 三矩付清以后成立。

还须核 outer cubic。对偶 $u$ 与奇 $w$，原二导的极化准确为
$$
\begin{aligned}
L(u,w)''={}&
\frac12\{(u-yu')w'''+(w-yw')u'''\}\\
&-\frac y2u''w''-\frac12J(u''w''),
\end{aligned}
\tag{8}
$$
$$
\begin{aligned}
U(u,w)''={}&
(yu'-\tfrac32y^2u'')w'''
+(yw'-\tfrac32y^2w'')u'''\\
&+u'w''+w'u''-2yu''w''.
\end{aligned}
\tag{9}
$$
所有 local 项为偶。式(8)中的 $u''w''$ 为紧奇函数，其总积分为零；同一右原函数准确为偶，不存在遗漏的自由左常数。因此两式整体为偶。

另外
$$
P(u,w)''=-u'''w''-u''w'''
$$
也是偶函数。将 $w=PD$ 或 $w=Z_*D$ 代入，(7)–(9)给
$$
\tau_\theta''\text{ 在中心坐标为偶函数}.
$$
于是
$$
\int y\,u''(y)\tau_\theta''(y)\,dy=0.
\tag{10}
$$
外 $u''$ 紧，所以本式包括真实 primitive 尾，不要求 $\tau_\theta$ 整体紧。

## 5. 物理中心关系及十二副本的准确消元

回到最终物理 $x$ 坐标。原旧面积在中心坐标也为零，因为它自身的同锚变换是三角的。由(6)、(10)，基圆准确有
$$
\boxed{A_1(\theta)=C_0A_0(\theta).}
\tag{11}
$$
若跳过(3)–(5)，不能仅凭“积分中心化”取得(11)。

R331 的内部常数已经使基圆 $A_0(\pi/2)=0$。该圆有弱 hook、旧完整面积及 $\mathcal Q_4=0$；R328 的真实式
$$
A_0=d_*\mathcal K_\theta-4e_*\mathcal J_\theta
-\frac{d_*+7e_*}{3}C_\theta
$$
只有 $\sin^2\theta,\cos\theta\sin\theta$ 两项。因此存在一个实际实数 $b_0$，使
$$
A_0(\theta)=b_0\cos\theta\sin\theta,\qquad
A_1(\theta)=C_0b_0\cos\theta\sin\theta.
\tag{12}
$$

按 R331 的原十二副本，取等差真实位移 $\delta_j$，并令
$$
(f_j,g_j)=\gamma_jT_{\delta_j}(f,(-1)^jg),
\qquad\gamma_j^4=\binom{11}{j}.
$$
每个副本的旧三面积仍零。由(6)、(12)，
$$
A_{0,j}=\gamma_j^4(-1)^j b_0\cos\theta\sin\theta,
$$
$$
A_{1,j}=\gamma_j^4(-1)^j(C_0+\delta_j)b_0
\cos\theta\sin\theta.
$$
十一差分分别清常数和一次位置多项式，准确得到
$$
\boxed{A_0(\theta)=A_1(\theta)=0\quad\text{全部 }\theta.}
\tag{13}
$$

不同完整三矩块之间的加法在此仍是真加法。$PD,XD$ 真紧使不同 inner 块的同点乘积为零；同块 nested 输出的真实二次左尾对另一个紧 outer 的全部 $I_j$ 正交。对面积的两个 directed 方向分别应用这一论证，才能相加(13)，不是只处理其中一侧。

## 6. 后续强正块与有限频率不破新零

R331 随后加入的 R280/R293 强控制宏块，自己的全部72面积已零，包含当前 $A_{-1,-3}$ 的三个外矩。其真实正幅只乘同一四次因子。因此它不改变(13)。

最后的有限频率校正仅作用于强宏块；它保持从起点选定的原 $\mathcal F_\star$，所以该宏块的全部面积继续准确为零。固定弱宏块不动，原跨完整块加法仍成立。因此(13)对 R331 的最终有限 $N$、最终三条 directed 精确根以及最后归一化后的同一个真实圆都成立。

本节不要求最终整个圆继续关于一个中心为偶。反射只在十二副本以前用于(11)；以后使用已经证明的差分与准确面积加法。

**新增结论。** R331 的同一个真实构造无需再调参数，就满足新面积
$$
\boxed{
I_0\{u,[Z_*,P](u;D)\}
=I_1\{u,[Z_*,P](u;D)\}=0
\quad\text{全部 }\theta.
}
\tag{14}
$$
完整三阶、旧面积三矩、$\Psi$、三条 directed 与指定一层保持。

## 7. 第2矩是下一真正剩余门

当 $A_0=A_1=0$ 后，(6)准确变成
$$
A_2^{(\delta)}=A_2.
\tag{15}
$$
所以仅移动已经完成的完整块，不能支付其未零的第2矩。这里的结论已经包含原算子自身的平移项，不是忽略显式 $x$ 后得到的假不变量。

中心偶性也没有使 $A_2$ 的 integrand 为奇：$y^2u''\tau''$ 为偶，原 $2u'\tau'$ 项同样可能贡献。不能从第零、第1矩零删掉它，也不能把本稿写成新面积的全部三矩已经完成。

下一步必须回到原 $I_2$ 的真实 local 与尾项，检验 R331 内部常数、宽 cutoff、矩补偿和其它实际形状参数能否在同一圆上支付这个剩余量。其余 Gaussian 门、全 period 与 joint ruling 范围仍保持 R331 的未付清单。
