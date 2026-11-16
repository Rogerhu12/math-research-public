# R422：权负四 hh 正规自然函数的完整两项曲率结构

日期：2026-11-16。**完整原式纸面证明；未执行新的积分、profile 评价、原根恢复、符号消元、秩或人工检查。**

沿 [R419](R419-all-curvature-hh-minus6-natural-cancellation-and-PSD-reduction.md) 的同一原 $hh$ 速度方向，定义
$$
V(k)=[h^{-6}(\log h)^0]\widehat Q_{hh}(h,k,0),\qquad
W=[h^{-6}k^6(\log h)^0]\widehat Q_{hh}(h,k,0).
$$
二者均为原完整正规 $Q_2$ 的真实系数，真权为 $-4$。本稿证明
$$
\boxed{
\mathcal N(V(k))=(1+k^2)^2
\{\mathcal N(V(0))+k^2\mathcal N(W)\}.
}
\tag{1}
$$
该式保 self、原 pure、所有真实三矩有序尾、$N_0,N_2$ 及加速度正规化。不从单个 $k$ 外推；下一真实未知准确只需两个完整自然函数。

[R420](R420-complete-zero-natural-flux-of-W4-and-static-minus4-character-elimination.md) 的静态 $W_4$ 不是这里的动态 $W$。本稿没有将(1)右侧两个函数置零，也不先声称 PSD 的 $hh$ 或 cross 已消去。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R367](R367-exact-N2-Green-contraction-and-nonzero-quartic-velocity-correction.md)的独立原势/Green 身份、[R417](R417-two-term-static-minus4-natural-image-and-one-remaining-anchor.md)、R419及R420。R367 不使用已撤回的旧 H 非零论证。

## 1. 固定方向、原输入和完整场的拆分

保持固定正窗口、共同右 collar 与
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
只在 $k_s=k_{ss}=0,\omega=0$ 的真实切片取 $hh$ 系数；因此
$$
S=1+k^2,\quad e=hx-k,\quad Q=1+e^2,\quad
K_0=kx^2-Sx/h,
$$
$$
\gamma=h_s,\quad\alpha=h_{ss},\quad
X=\partial_h
$$
中 $k$ 固定。此处没有删除一般 $kk$ 方向的水平 $\omega$ 导数。

对实紧 $u$，写
$$
p=u',\quad r=u'',\quad t=u''',\quad
L=p-xr,\quad G=u-xp/2,\quad M=x^2r-2xp+2u.
$$
使用原二次输出
$$
P=J(r^2),\quad C=J(x^2r^2+2p^2),\quad
R=p^2+xP,\quad T=x^2p^2+xC,\quad F=x^2P-C.
\tag{2}
$$
它们右零、左可有真实二次尾。$\mathbf R(f,g)=f'g'+xJ(f''g'')$ 表示原算子，不是响应空间。

第二局部场的分子为
$$
K_Z=(\gamma A,b,e\gamma A),
$$
其中完整状态式为
$$
A=\frac{SR'}{16h^3}
+\frac{k(R-xR')}{8h^2}
+\frac{x^2R'-2xR+F}{16h},
\tag{3}
$$
$$
b=\frac{SR}{8h}
+k\left(\frac{up}{2}-\frac{3xp^2}{8}-\frac{xJ(xr^2)}4\right)
+h\left(\frac{G^2}{2}+\frac T8\right).
\tag{4}
$$
原瞬时第二 history 导数是
$$
q=q_0+\gamma^2D,\qquad
D=\frac{SR}{8h^4}-\frac T{8h^2},
\tag{5}
$$
$$
q_0=-\frac{S^2R}{8h^2}
+\frac{kS E}{h}+k^2V-\frac{ST}{8}
-\frac{kh}{2}\Phi_{p_2}(u,u),
\tag{6}
$$
$$
E=-\frac12\Phi_{p_0}(u,u)+\frac14\Phi_{s_1}(u,u),
\qquad V=\Phi_{p_1}(u,u).
$$
(3)—(6)均来自 R73/R417 完整原式。尤其
$$
A'=\frac{QLt}{8h^3},\qquad
q_0=(kx-S/h)b+G^2/2.
\tag{7}
$$
最后才令累计 second 值为零；其真实导数 $q$ 始终保留。

## 2. 第三局部第一分子的完整二速度式

令
$$
j=J(QtA).
$$
将 R56 的完整 $\eta_0/h$ 用于 $H(Y_u,Z_{u^2})$，并先保真正 $P_s$ 中的 $-P(Y_u,Y_q)$，得到
$$
\boxed{
c=c_0-\frac{\alpha j}{8h^2}
-\gamma^2\left\{\frac{J(QtA_h)}{8h^2}
+\frac{QLA'}{8h^3}\right\}.
}
\tag{8}
$$
这里
$$
c_0=-\frac{Gb'}{4h}+\frac{Lb}{8h}
+\frac{Qr q_0'}{16h^2}
+\frac{(hp-er)q_0}{8h}
+\frac{J(Qr q_0''+2h^2p q_0')}{16h^2}.
\tag{9}
$$
没有把 $D$ 对恢复的贡献删掉。为逐项核对(8)，在尚未用(5)化简时，$\gamma^2$ 项为
$$
c_q(D)+\frac{j}{8h^3}-\frac{j_h}{8h^2}
-\frac{QLA'}{8h^3},
$$
$$
c_q(w)=\frac{Qr w'}{16h^2}
+\frac{(hp-er)w}{8h}
+\frac{J(Qr w''+2h^2p w')}{16h^2}.
$$
将这个完整 $c_q$ 用同锚 IBP 重写为
$$
c_q(w)=\frac{J\{t(2he\,w-Qw')\}}{16h^2}.
$$
又有
$$
16h^3A=QR'-2heR+h^2F,\qquad T=x^2R-xF.
$$
故原(3)(5)逐项给
$$
c_q(D)=\frac{J(Q_h tA)}{8h^2}-\frac{j}{8h^3},
\qquad
j_h=J(Q_h tA)+J(QtA_h),
$$
故得到(8)。所有 primitive 取同一个右零常数。

相应第三 normal 分子为 $\gamma b_1$，其中
$$
b_1=\frac{(-QL+2heG)A+xj}{4h}.
\tag{10}
$$
本节仍不包含随后第四恢复中第三场对累计 second 的 $C_Aq$，也未将第三 history 导数置零。

## 3. 完整 YC 及准确的 s 分部积分

先仅取第三局部状态值 $(c,\gamma b_1,ec)$；另保留下一节的 $C_Aq$ 与 $-Y_n$。

原 $P/B$ 对当前第一分子 $c$ 为
$$
P_c=\frac{(Qr-hep)c+J(Qt c)}{4h},\qquad
B_c=\frac{(heu-Qp/2)c}{2h}.
$$
于是
$$
xP_c+B_c-\frac{eGc}{2}
=\frac{-QLc+xJ(Qt c)}{4h}.
\tag{11}
$$
R56 中 $T_s$ 的 $\gamma b_1$ 状态导数与对应 $-\gamma B_s/h^2$ 合成真正的 $s$ 总导数；两端常值 germ 使这个显式边势为零。原 profile Fubini 为
$$
\int xtJ(Qt c)=-\int QLt c.
\tag{12}
$$
它只用紧 outer $u$，不要求 $c$ 左紧。

将(11)(12)用于其余 $c_s,P_s,B_s$ 项，第一次真实 $s$ 分部积分后，完整局部状态贡献为
$$
\boxed{
\int\frac{Qt}{2h^2}
\left\{\left(S+\frac{2\gamma^2}{h^2}
-\frac{\alpha}{h}\right)L+khM\right\}c.
}
\tag{13}
$$
(13)只是在明确拆出的状态项上使用边势；下文的 history 项未因此消失。

写 $c=c_0+\alpha c_\alpha+\gamma^2c_2$。令
$$
\mathcal M_h(f)=\frac1{2h^2}\int Qt(SL+khM)f.
$$
按 R129 再扣原加速度系数的 $h$ 导数，局部状态的 $hh$ 贡献准确为
$$
\boxed{
Y_{hh}^{\rm state}
=\mathcal M_h(c_2)+h^{-4}\int QLt c_0
-\partial_h\left\{\mathcal M_h(c_\alpha)
-\frac1{2h^3}\int QLt c_0\right\}.
}
\tag{14}
$$
这保留(8)的全部 $\alpha$，不是先令加速度零再收速度平方。

## 4. 全部额外链项与原势

第三场对 second history 的真实导数中，有
$$
-\frac1{2h}\int tG\,b(u,q)
\quad\text{及}\quad
-4\int a'a(u,q),\qquad a=\gamma A.
\tag{15}
$$
其中 $b(u,q)$ 是(4)的原对称极化。第一项在本次二速度权取 $q=\gamma^2D$；它不被删除。

第二项在本次二速度权取 $q=q_0$。R367 的独立完整 Green 身份对任意原八方向 $E$、任意真实状态和速度都成立。取 $q_0=\Phi_{m_0}(u,u)$，其 self、正式 pure 和真实两尾的合成，准确抵消原 $-\mathcal B_{m_0}N_2$ 的自然读出。R419 §4 已显示此同一身份的最低幂；这里使用 R367 的完整外槽式，不把最低幂零外推。

该消去发生在**完整自然配方**中，不保证这对 ambient 项的 raw self、raw pure 或某一尾各自为零。后继若用原 Qhh 的 paid pure 坐标把 raw $\Omega$ 解释为自然值，必须保这对 raw 项；不能删 pair 的 raw self 后仍使用原 pure 校正。

第三 history 的 $n=\gamma n_\gamma+\text{三速度/加速度项}$ 也必须保。第四完整恢复中的 $-Y_n$ 一次给出原
$$
-\Psi_\gamma(u,n_\gamma),\qquad
-\Psi_\gamma(u,w)
=\frac{S}{8h^3}\mathbf R(u,w)
-\frac{k}{4h^2}\mathsf E_u(w)
+\frac1{8h}\mathbf T(u,w),
\tag{16}
$$
$$
\mathsf E_u(w)=xp w'+xJ(xr w'')-pw,\qquad
\mathbf T(u,w)=x^2p w'+xJ(x^2r w''+2p w').
$$
(16)保 R73 原 $\Psi$ 的全部 $P/B$ 和 $T_s$，不是只取其中一项。

R417 的完整独立 outer 公式已付
$$
[N_0]_{h^{-3}}=kS^2\tau_3,\qquad
[N_0]_{h^{-2}}=S(\tau_0+k^2\tau_1),\qquad
[N_0]_{h^{-4}}=0,
$$
$$
[n_\gamma]_{h^{-4}}=-3kS^2\tau_3,\qquad
[n_\gamma]_{h^{-3}}=-2S(\tau_0+k^2\tau_1),\qquad
[n_\gamma]_{h^{-5}}=0.
\tag{17}
$$
因此(16)在本次所需幂为
$$
\boxed{
[h^{-6}]\{-\Psi_\gamma(u,n_\gamma)\}
=S^2\left\{
-\frac14\mathbf R(u,\tau_0+k^2\tau_1)
+\frac{3k^2}{4}\mathsf E_u(\tau_3)
\right\}.
}
\tag{18}
$$
$\tau_i$ 在此表示其实际对角三次值；其原完整 outer/inner 定义仍是 R417(10)—(14)，不能仅用对角值猜 full 响应。

另一份必要势是
$$
\boxed{
[h^{-6}\gamma^2]\{-\mathcal B_{m_2}N_0\}
=-\frac{S^2}{8}\mathcal B_{\mathbf R}(\tau_0+k^2\tau_1).
}
\tag{19}
$$
$m_{2,hh}=S\mathbf R/(8h^4)-\mathbf T/(8h^2)$，且 $N_0$ 没有 $h^{-4}$，故没有漏掉第二个乘积。原 $\Gamma(m_2)$ 对 $m_2$ 线性，最低幂为 $h^{-4}$，不贡献本次 $h^{-6}$；这只是本系数次数判断。

(15)的 $b$ 链在本次准确为
$$
-\frac{S^2}{128}\int tG\,\mathbf R(u,R).
\tag{20}
$$
其原有尾输入 $R$ 保持不变。

## 5. 完整 ZZ 的可逐项取幂式

为使结构检查不依赖只报某个 principal，定义
$$
U=\frac{q_0'}2-kb,\qquad
V=\frac{eq_0'}2-b-hq_0,\qquad
J_s=U+eV,
$$
$$
B_h=A_h+D'/2,\qquad
C_h=xA-hD,\qquad M_h=b_h+hxA.
$$
符号 $J_s$ 只是当前收缩名称，不是 profile primitive 或新的导数。

第二场的真正协变导数为
$$
\nabla_sZ=
(U,0,V)+\alpha(A,0,eA)
+\gamma(0,M_h,0)
+\gamma^2(B_h,0,eB_h+C_h).
\tag{21}
$$
原 $-Y_q$ 已在(21)中，未将 history 导数设零。

置
$$
P_0=\frac{J((b')^2)}{2h},\quad B_0=\frac{b^2}{2h},
$$
$$
P_2=\frac{J((A')^2+(hA+eA')^2)}{2h},\quad
B_2=\frac{QA^2}{2h}.
$$
对 $K_A=(A,0,eA)$ 与 $Y_{q_0}$，原对称配对为
$$
P_{Aq_0}=\frac{(Qq_0''-heq_0')A+J(Qq_0'''A)}{4h},
\qquad
B_{Aq_0}=\frac{(heq_0-Qq_0'/2)A}{2h}.
$$
所以原 $ZZ$ 的二速度与加速度两行准确为
$$
\begin{aligned}
Z_{\gamma^2}^{\rm raw}
=\int t\bigg\{&
\frac{B_hJ_s+C_hV+M_h^2/2}{h^2}
+K_0P_2+\frac{K_0}{x}B_2\\
&-\frac{x}{h^2}\partial_hP_0
-\frac1{h^2}\partial_hB_0
+\frac2{h^2}(xP_{Aq_0}+B_{Aq_0})
\bigg\},\\
Z_\alpha^{\rm raw}&=\int \frac{tAJ_s}{h^2}.
\end{aligned}
\tag{22}
$$
最后两个配对来自 $P_s,B_s$ 的真实 $-2P(K_Z,Y_q),-2B(K_Z,Y_q)$，不能省略。完整正规式为
$$
Z_{hh}=Z_{\gamma^2}^{\rm raw}-\partial_hZ_\alpha^{\rm raw}.
\tag{23}
$$
所有(21)—(23)直接来自 R56 全平方及其完整导数；未把原 $K_0B/x$ 当作独立有理余式删除。

## 6. 两项结构的原 Laurent 支撑核对

以下各大写 profile 系数都由前节完整式定义、与 $h,k$ 无关；它们不是独立可指定的常数。由(3)(8)直接得到必要三行支撑：
$$
\begin{array}{c|ccc}
 &\text{最低幂}&\text{下一幂}&\text{再下一幂}\\ \hline
c_\alpha&
h^{-5}S^2A_5&
h^{-4}kS A_4&
h^{-3}(S A_3+k^2\widetilde A_3)\\
c_2&
h^{-6}S^2B_6&
h^{-5}kS B_5&
h^{-4}(S B_4+k^2\widetilde B_4).
\end{array}
\tag{24}
$$
例如 $A_5=-J(tR')/128$，$B_6=(3J(tR')-LR'')/128$；其余值可以直接按(3)(8)保 primitive，无需求积分。

R417(18)(19)提供
$$
c_0=h^{-4}S^3C_4+h^{-3}kS^2C_3
+h^{-2}S(C_{20}+k^2C_{21})+\text{更高幂}.
\tag{25}
$$
而(14)中的系数
$$
\frac{Q(SL+khM)}{2h^2}
=\frac{S^2L}{2h^2}
+\frac{kS(M-2xL)}{2h}
+\frac{Sx^2L-2k^2xM}{2}
+\frac{khx^2M}{2}.
\tag{26}
$$
因此(24)—(26)对(14)的 $h^{-6}$ 以及加速度行 $h^{-5}$，都给
$$
S^2(\text{固定函数}+k^2\text{固定函数}).
\tag{27}
$$
$h$ 微分不动 $k$，所以正规化保持(27)。

对(22)同样可逐乘积核对。完整 $A,b,q_0$ 的支撑是
$$
A=h^{-3}SA_3+h^{-2}kA_2+h^{-1}A_1,\quad
b=h^{-1}SB_1+kB_0+hB_+,
$$
$$
q_0=-h^{-2}S^2R/8+h^{-1}kSE+k^2V-ST/8-kh\Phi_{p_2}/2.
\tag{28}
$$
例如
$$
\begin{aligned}
[h^{-2}]J_s&=-S^3R'/16,\\
[h^{-1}]J_s&=kS^2(E'/2+xR'/8-R/8).
\end{aligned}
$$
取到 $h^{-6}$ 时，平方、$K_0P_2/K_0B_2$、$P_0/B_0$ 的状态导数和最后的两 history 配对，各自都具有(27)；可能的额外 $S$ 只用 $S=1+k^2$ 合并。加速度 $h^{-5}$ 行也同样。没有假设 $S,k$ 是独立参数，也不将非零左值设零。

链项(18)(20)、势项(19)已显式具有(27)。第4节消去的 $C_A$ 与 $N_2$ 是完整自然身份，因此综合得到
$$
\mathcal N(V(k))=S^2(\mathcal A+k^2\mathcal B)
\tag{29}
$$
对两个固定完整自然函数 $\mathcal A,\mathcal B$。

## 7. 原 pure 和有序尾为何不破坏结构

前面的原 profile 等式对任意实紧 $u$ 成立，包括 $u=su_1+tu_2$；不预设三矩零、相同母形、同宽或同符号。原 $ZZ$、$YC$ 的 pure 对角与原完整势的全部槽也保留。

因此从相同原式取有序 $s^2t^2$ 系数，仍保持(27)。右包依赖按 R352 的真实三矩尾映射先作线性因子化，再代左包三矩；这两个线性操作不产生新 $h,k$ 系数。R367 已单独付清的 $C_A/N_2$ 消去也包括这两尾。

所以(29)是完整自然函数，不是只从 local self 取幂的结论。取 $k=0$ 得 $\mathcal A=\mathcal N(V(0))$；而 $S^2$ 最高 $k^4$，$k^2S^2$ 最高 $k^6$，故
$$
\mathcal B=\mathcal N(W).
$$
证明(1)。等价的原 $U$ 代表为
$$
\mathcal N(W)=\mathcal N\left(\frac14V(1)-V(0)\right).
\tag{30}
$$
这只等同自然函数，不把两个原成本直接认作相等。

## 8. 两个最小新观察与仍未付范围

当前真正尚未知的是
$$
\mathcal N([h^{-6}k^0]\widehat Q_{hh}),\qquad
\mathcal N([h^{-6}k^6]\widehat Q_{hh}).
\tag{31}
$$
R210 的旧 pure 坐标可复用，但它不是这两个完整 natural 值，也不保证旧仓库已保存物化后的完整正规 mixed 根。原源码中 Q2 的三个族由保存的 $v_2,N_0,N_2$ 原因子与参考减项装配；必须先核对实际保存接口。

若公开 Actions 消费(31)，安全的完整目标可取：

1. 保原正规 Qhh 的完整 self，包括全部原势，使用已付 pure 响应坐标校正后，仅新增同锚 $\Omega$；
2. 或直接消费原 $Y-Z$、两真尾和完整势的自然配方，只计算尚未付的两系数。

不能在自然层使用 $C_A/N_2$ 消去，却在 raw 层沿用未经相应修正的旧 pure 坐标。若确需从保存的完整原槽进行本两目标所必需的 self 势收缩，应明确列为新观察费用；不称它为已经保存的正规根，不重编旧 forcing 或旧 pure/rank。

本稿未执行任何新观察。若以后两个自然值在共同查询中都为零，才可用同权 $E$ 响应等像消去正字符的 $hh$ 行，再由真实 PSD 迫 cross 为零。当前(1)本身不授该前提，不把 W4 的静态零代替(31)，也不宣称实际联合截面已完成。
