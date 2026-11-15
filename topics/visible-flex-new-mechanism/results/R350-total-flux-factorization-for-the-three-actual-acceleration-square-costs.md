# R350：三个真实加速度平方成本的总通量由完整 pure 与有序尾项决定

日期：2026-11-15。**完整纸面证明；没有执行新的 profile 积分、原根恢复、符号消元、秩计算或科学运行。**

[R344](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md) 已从原 Green 式证明：总通量的一个有限读出 $\Lambda_{u,\mathbf v}$ 杀掉整个真实响应空间 $\mathcal R$。在原实际成本空间 $U$ 上，该读出此前仍可能非零。R342 的单个声明 profile 族零值不能决定这一问题。

本稿从 [R56 原分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 直接证明：对 [R134](R134-acceleration-layer-from-complete-local-v4.md) 的三个实际正规生成元，
$$
\boxed{
\Lambda_{u,\mathbf v}(\bar A_{hh})
=\Lambda_{u,\mathbf v}(\bar A_{hk})
=\Lambda_{u,\mathbf v}(\bar A_{kk})=0.
}
\tag{1}
$$
这对每个实际状态 $h>0,k,\omega$、每个实紧 profile $u$，以及 R344 中任意合法的三个右侧辅助包都成立。证明保留一个通常非零的真实左尾乘积；该乘积由 pure 的有序 $2+2$ 项准确恢复，而不是被设为零。

这是原 $U$ 的三类完整 mixed 生成元的新结论，不是只处理 pure 投影或某个权。它同时覆盖这些状态函数的所有有限独立系数跨度。其余 $H_1,H_2$、静态、速度二次及速度四次正规元仍未在本稿支付，不能据此宣称 $\Lambda|_U=0$。

## 1. 同一原锚、状态及正规化对象

固定共同右 collar $r_*$，使用
$$
J(F)(x)=\int_x^{r_*}F(t)\,dt,
\qquad u\in C_c^\infty((\ell,r_*)).
$$
写
$$
z=x+\omega,\qquad e=hz-k,\qquad Q=1+e^2,
\qquad v=u',\quad r=u'',\quad s=u'''.
\tag{2}
$$
因此 $Q'=2he$、$Q''=2h^2$。几何一直满足原水平关系 $\omega_s=k_s/(2h)$；本稿的 $x$ 导数与几何 $s$ 导数不混用。

在 R109/R134 的局部生成元中，先作全部真实几何导数、代入原 history 微分方程，再把累计第二、第三 scalar 值置零；**不把它们的导数置零**。记这个完整第四局部生成元为 $\mathfrak v$，以免与 $v=u'$ 混淆。

取一个固定几何方向 $(c,d)\in\mathbb R^2$。为识别正规系数，可以形式上取
$$
(h_s,k_s)=q(c,d),\quad
(h_{ss},k_{ss})=q'(c,d),\quad
(h_{sss},k_{sss})=q''(c,d),
$$
并按原水平关系处理 $\omega$。这里是在原有限 jet 多项式中提取系数，不是运行一条新路径或声称各 jet 可独立实现。

令
$$
t(x)=c(x+\omega)-\frac d2,\qquad
l(x)=c\,u'(x)-t(x)u''(x).
\tag{3}
$$
有 $t'=c$、$l'=-ts$。该方向的完整正规成本为
$$
\mathcal A_{c,d}
=c^2\bar A_{hh}+cd\,\bar A_{hk}+d^2\bar A_{kk}.
\tag{4}
$$
若原 $\mathfrak v_4$ 的 $q'^2$ 系数为 $A$、$q q''$ 系数为 $\beta$，则 R129/R134 的真实分部积分给
$$
\mathcal A_{c,d}=A-\beta.
\tag{5}
$$
对状态系数作 $s$ 导数只另产生速度平方乘加速度等项，不改变 (5) 中的平方系数。三个方向的极化同时保留原交叉项 $\bar A_{hk}=A_{hk}-\beta_{hk}-\beta_{kh}$。

## 2. 原第二局部场的速度系数

R56 的第一分子是
$$
V_{Y_u}=(-v/2,0,hu-ev/2).
$$
记原第二场的 normal 恢复量为 $P_Z,B_Z$。直接代入其真实二次配对，得到
$$
B_Z=\frac{Qv^2}{8h}-\frac{euv}{2}+\frac{hu^2}{2},
$$
$$
P_Z=\frac{ev^2}{8}+\frac1{8h}J(Qr^2+2h^2v^2).
\tag{6}
$$
这些式子的 primitive 全从同一右 collar 积出。

令 $\gamma=h_s$、$\vartheta=e_s=\gamma z-k_s/2$。由 R56(6)，原 $\eta_{0,Z}$ 准确为
$$
\eta_{0,Z}
=-\frac{\vartheta Qr^2}{16h^2}
+\frac{\gamma Qvr}{8h^2}
-\frac{\gamma ev^2}{8h}
-\frac1{16}\partial_s\!\left\{\frac1hJ(Qr^2+2h^2v^2)\right\}.
\tag{7}
$$
例如 (7) 的推导中，$T_{sx}$、$\vartheta P_x$、$\gamma B_x$ 和 $P_s$ 的局部 $uv$、$ur$、$\vartheta v^2$ 项逐项抵消，不能仅保留某一个 leading jet。

在累计第二 scalar 为零时，第二场的第一分量是 $\eta_{0,Z}/h$。设它沿 (3) 的速度系数为 $a=a_{c,d}(u)$。将 (7) 对 $x$ 求导，全部不含 $u'''$ 的项抵消，得到
$$
\boxed{
a'=\frac{Q\,l\,s}{8h^3},\qquad a(r_*)=0,
\qquad
a=-\frac1{8h^3}J(Qls).
}
\tag{8}
$$
$a$ 是一个真实右零二次 profile 算子，一般有非零常数左尾。它不是任意另选的 primitive。

令原三矩为
$$
\mu(u)=
\left(\int r^2,\ \int xr^2,\ \int(x^2r^2+2v^2)\right).
$$
一次普通分部积分给该左尾的完整表达：
$$
\boxed{
a_{\rm L}(u)
=-\frac{
ch^2\mu_2+h^2(2c\omega-d)\mu_1+
\{c(h^2\omega^2-k^2-1)-hd(h\omega-k)\}\mu_0
}{16h^3}.
}
\tag{9}
$$
特别它只通过原三个真实矩线性依赖输入，没有额外第四矩。验证 (9) 时，
$$
\int Q(c v-t r)s
=\frac12\int(Q't-cQ)r^2+ch^2\int v^2,
$$
而 $Q't-cQ$ 的二次项与后一项恰合成 $\mu_2$；真实 $2v^2$ 不能删掉。

## 3. 原第三局部场的加速度项

固定外 profile $u$ 和任意二次 inner 张量 $D$。记 $a_D=a_{c,d}(D)$。原第二分子的几何导数中，加速度 $q'$ 的系数为
$$
(a_D,0,e a_D).
\tag{10}
$$
原 $m$ 只依赖状态与速度二次，不含加速度；故把真实 history 导数代入后不会另外产生 (10) 型的加速度项。

令
$$
C(u;D)=\operatorname{Range}H(Y_u,Z_D),
$$
其中 $H$ 是原对称双线性 forcing，$H(Y,Y)=(dY)^2$。置
$$
f_1=he v-Qr.
$$
直接使用 R56 的 $T_{sx},P_s$，得到
$$
[T_{sx}(Y_u,Z_D)]_{q'}=\frac{f_1a_D}{4},
$$
$$
[P_{C,s}]_{q'}=
\frac1{4h}\{-f_1a_D+J(Qs\,a_D)\}.
\tag{11}
$$
第二式使用
$$
f_1'=h(hv-er)-Qs,
$$
从而
$$
J\{f_1a_D'+h(hv-er)a_D\}=-f_1a_D+J(Qs\,a_D).
$$
所有端常数都由真实右零场支付；没有在左端重锚。

在 R56(6) 中，(11) 的两项局部 $f_1a_D$ 准确相消。因此第三分子的第一分量的加速度系数为
$$
\boxed{
[A_C]_{q'}=-\frac1{8h^2}J(Qs\,a_D).
}
\tag{12}
$$
这里累计第三 scalar 的值按原局部生成元定义为零。其真实导数含状态、速度与加速度，但不含几何三阶 jet；故后文 $q''$ 系数只需对 (12) 作真实导数。没有把完整第三场或其传入历史在原路径上删掉。

## 4. 完整 self 与 raw pure 的两个正规系数

沿原完整相位规范，令 $F=f^2$、$D=F-\phi^2$。第四 forcing 是
$$
-H(Z_D,Z_D)+4H(Y_\phi,C(\phi;D)).
\tag{13}
$$
raw pure 为 $V(0,u)=16\pi V(u)$，不是正式 pure 本身。

### 4.1. Self

对 $F=u^2,\phi=0$，(13) 只余 $-H(Z_u,Z_u)$。R56 的特征 RHS 中，$q'^2$ 唯一来自 $-T_s/(2h^2)$，由 (10) 得
$$
\boxed{
\mathcal A_{c,d}(u^2,0)=-\frac{Q a^2}{2h^2}.
}
\tag{14}
$$
self 不含 $q q''$：原第二恢复只含速度，第四 forcing 对它作一次几何导数；$P_s,B_s$ 项也至多含加速度。因此 (14) 已是正规后的完整 self。

### 4.2. Raw pure 及其真实 $q q''$ 伙伴

对 $F=0,\phi=u$，$D=-u^2$。第二平方的 $q'^2$ 项仍是 (14)。原 $Y$–$C$ 项在速度零时至多一次加速度，不产生另一个 $q'^2$ 项，但它含必须保留的 $q q''$ 项。

记
$$
j=J(Qs\,a),\qquad k_1=J(Qs\,j).
\tag{15}
$$
由 (12)，此时第三分子的 $q'$ 系数是 $b=j/(8h^2)$；其 $q''$ 分子为 $(b,0,eb)$。对任意这种分子，原双线性恢复给
$$
B(Y_u,b)=\frac{(he u-Qv/2)b}{2h},
$$
$$
P(Y_u,b)=\frac{-f_1b+J(Qs\,b)}{4h}.
\tag{16}
$$
把 (16) 和 $\nabla_sY_u$ 的真实速度项放回 R56(5)，并保留 (13) 的因子 $4$，所有 $u$、$ev$ 的局部项抵消，得到
$$
\boxed{
\beta(u)=
\frac{Ql\,j-t\,k_1}{8h^5}.
}
\tag{17}
$$
这是 raw pure 的 $q q''$ 系数。原 $m$, $n$ 的 history 导数不含 $q''$，故没有漏掉额外三阶几何 jet。

由 (5)，完整 raw pure 正规函数是
$$
\boxed{
\Pi_{c,d}(u):=16\pi\mathcal A_{c,d}(u)
=-\frac{Qa^2}{2h^2}-\beta(u).
}
\tag{18}
$$
(14)、(18) 是完整 profile 函数，不是只比较最高 profile 导数，也没有使用任何旧数值根的表达式。

## 5. 总通量的左尾恰好留下一个乘积

定义
$$
I=\int Qs\,a^2,\qquad
B=a_{\rm L}j_{\rm L}.
$$
由 (8) 和 $j'=-Qs\,a$，
$$
\int Qls\,j
=8h^3\int a'j
=8h^3(I-B).
\tag{19}
$$
右端为零，而左端 $a_{\rm L}j_{\rm L}$ 一般非零，必须保留。

另一方面，$l'=-ts$ 且 $l$ 紧，所以
$$
\int ts\,k_1
=-\int l'k_1
=-\int Qls\,j.
\tag{20}
$$
将 (19)、(20) 代入 (17)，得到
$$
\int s\beta=\frac2{h^2}(I-B).
$$
因此
$$
\boxed{
\int s\,\Pi_{c,d}(u)
=5\Omega_u(\mathcal A_{c,d})+\frac2{h^2}a_{\rm L}j_{\rm L}.
}
\tag{21}
$$
式 (21) 没有推出无尾的 $16/5$ 恒等。它明确给出该误用会遗漏的实际乘积；本稿接下来从同一个 pure 的有序交叉项读取它。

## 6. 有序双包的完整 $2+2$ 项

取实紧 $u,w$，满足
$$
\sup\operatorname{supp}u<\inf\operatorname{supp}w<r_*.
$$
仍使用原右锚。因为 (8) 的 integrand 是局部二次式，对两个实幅度 $\alpha,\beta$，
$$
a(\alpha u+\beta w)=\alpha^2a(u)+\beta^2a(w).
\tag{22}
$$
在整个左包内，$a(w)=a_{\rm L}(w)$；在右包内，$a(u)=0$。没有把右包的常数左尾删掉。

令
$$
F_u=Qr-Q'v+Q''u.
$$
它真紧，且
$$
F_u'=Qs,\qquad J(Qs)=-F_u,\qquad
J\{Qs\,J(Qs)\}=\frac{F_u^2}{2}.
\tag{23}
$$
从原 (17)、(18) 直接按幅度展开，而不是对紧域公式作非紧变分。在左包上得到
$$
\boxed{
[\alpha^2\beta^2]\Pi_{c,d}(\alpha u+\beta w)
=a_{\rm L}(w)
\left\{-\frac{Qa}{h^2}
+\frac{QlF_u}{8h^5}
+\frac{tF_u^2}{16h^5}\right\}.
}
\tag{24}
$$
在右包上没有该系数；在包间虽可能有真实尾，本次 outer $u'''$ 为零。故 (24) 足以准确计算所需完整收缩。

三个实际积分分别为
$$
\int sQa=j_{\rm L},
$$
$$
\int QlsF_u=8h^3\int a'F_u=-8h^3j_{\rm L},
$$
$$
\int tsF_u^2=2\int QlsF_u=-16h^3j_{\rm L}.
\tag{25}
$$
后两式的边项由紧 $F_u,l$ 支付；第一式仍保原 $j_{\rm L}$。因此
$$
\boxed{
\int u'''[\alpha^2\beta^2]\Pi_{c,d}(\alpha u+\beta w)
=-\frac3{h^2}a_{\rm L}(w)j_{\rm L}(u).
}
\tag{26}
$$
三个系数各贡献一个 $-1$，其中第二、第三项均来自正规化必需的三阶几何 jet 伙伴。只保第二场平方会得出错误因子。

## 7. 原三矩匹配准确清掉尾项

按 R344 选择三个实际右包 $w_1,w_2,w_3$，其真实三矩可逆，并取唯一实系数 $\lambda_j$ 满足
$$
\sum_{j=1}^3\lambda_j\mu(w_j)=\mu(u).
\tag{27}
$$
这些是线性读出系数，可以有符号；不是声称某个负幅成本可实现。由 (9)，
$$
\sum_j\lambda_j a_{\rm L}(w_j)=a_{\rm L}(u).
$$
将 (26) 对 (27) 加权，代入 (21)，得到
$$
\boxed{
\Omega_u(\mathcal A_{c,d})
=\frac15\int u'''\Pi_{c,d}(u)
+\frac2{15}\sum_j\lambda_j
\int u'''[\alpha^2\beta^2]\Pi_{c,d}(\alpha u+\beta w_j).
}
\tag{28}
$$
由于 $\Pi=16\pi$，(28) 正好是
$$
\boxed{
\Omega_u(\mathcal A_{c,d})
=\frac{16}{5}\int u'''\pi\mathcal A_{c,d}(u)
+\frac{32}{15}\sum_j\lambda_j
\int u'''\Gamma_{\pi\mathcal A_{c,d}}^\to(u,w_j).
}
\tag{29}
$$
这与 R344 的原 $\Lambda$ 规范完全一致。对 $(c,d)$ 极化，遂得 (1)。$u=0$ 时全部式子直接为零，不必另外作矩求逆。

## 8. 对原实际 U 的准确含义

[R134(12)–(13)](R134-acceleration-layer-from-complete-local-v4.md) 已证明三个正规加速度平方状态值属于真正 $U$，且它们只依赖原 $\mathfrak v_4$；$\mathcal B_{m_2}N_2$ 是速度四次式，不能改变本稿系数。静态八矩修正也只改静态和速度二次层。

因此本稿证明
$$
\Lambda_{u,\mathbf w}=0
\quad\text{于}\quad
\mathcal R+
\operatorname{span}_{h>0,k,\omega}
\{\bar A_{hh},\bar A_{hk},\bar A_{kk}\}.
\tag{30}
$$
若把这些状态函数按有限独立 Laurent/多项式状态单项展开，固定的 $\Lambda$ 由所有状态值为零也逐系数为零。这不需要重新计算某个函数秩或原 root，也不把单个任意几何 monomial 未经 R134 的实际 span 证明直接称为可实现路径。

特别，在 (30) 的 pure 核上，真实总通量恒为零。该结论对任意紧 $u$，不是仅对 R342 的声明多项式族，也不限权 $-6$。

**本稿没有证明 (30) 等于整个 $U$。** R130 的十四类生成元中，$H_1,H_2$、静态正规元、三个速度二次系数和五个速度四次系数尚需原式处理；后两层还保留真实 $N_0,N_2$ 势响应。不能把 $N$ 当成 $W$，也不能由本稿对加速度平方的结论省略 $\mathcal B_mN$。

这里得到的是一个已关闭的实际子层及其完整带尾原因。它不证明原 $U/\mathcal R$ 为零，不证明全部 period 或全部 $L_f$ range 条件，也没有把 whole pure/self 可控与总通量条件无条件叠加。
