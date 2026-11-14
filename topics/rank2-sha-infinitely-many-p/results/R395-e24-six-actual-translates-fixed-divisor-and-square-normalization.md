# R395 — E24 的真实六项 CM 运输、固定挠除子与原平方归一

日期：2026-11-14。**状态：以下原 E−8 ground 来源的完整身份、E24 的
十八项全局运输、保中心的六项合并、规范平方常数、原整来源的
primitive 性及固定代数因子均已证明。尚未证明指定中央观察跨素数
非零；局部来源 primitive 不被当作中央行的单位。主目标未完成。**

固定 R389–R393 的同一 $E_{24}$、$\alpha=1$、原微分和 Gaussian。
先在最大整环格
$$
\Lambda=\mathbf Z+s\mathbf Z,\quad
s=(1+\tau_0)/2,\quad \tau_0=\delta/3,\quad \delta=1+2\omega
$$
上书写；回到 $E_{24}$ 时始终置 $z=\Omega_{24}Z$。
本篇不把旧 degree16 来源认作新曲线。

## 1. 真正的旧 ground 来源属于 E−8

考虑固定参考
$$E_-:y^2=x^3-8.$$
有 $24/(-8)=-3=\delta^2$。
在二处，$\delta\equiv1\pmod2$，其立方根存在于
$1+2\mathcal O_{K_2}$，所以这个比值在 $K_2$ 是六次幂。
因此 $E_-$ 与 $E_{24}$ 的完整二处角色及 R393 的 $\phi_2$ 相同。

在三处 $-8=(-2)^3$，且 $-2$ 是 $\mathbf Q_3$ 的平方，
所以 $E_-$ 的本地角色正是 R389 的基角色 $\chi_{1,3}$：
conductor $\delta$，uniformizer 值 $i$。
其 $\alpha=1$ ground 向量是
$$h_0=\mathbf1_{3^{-1}\mathbf Z_3}.$$
其余有限点取标准球。于是原有理支撑 $x=n/12$，准确有限系数为
$$
a_n^-=v_2(11n\bmod16).
\tag{1}
$$
这里的十一是 $3^{-1}\bmod16$。同 R393 的完整 half-period 计算，
其 reduced theta 是一个 degree8、偶且 $\mu_3$ 不变的非零截面
$S_-(Z)\in H^0(\Lambda,\mathcal O(8O))$。
非零性也直接来自 (1) 的第零 Fourier 系数一。

### 1.1 原三挠零点给完整身份

我们证明
$$
\boxed{
S_-(Z)=\kappa_0 K_8(Z),\qquad
K_8(Z)=\frac{\sigma_\Lambda(3Z)}{3\sigma_\Lambda(Z)},\qquad
\kappa_0=S_-(0)\ne0.
}
\tag{2}
$$
这一步不使用“相同 core”来代替原来源识别。

在 $Z=1/3$，原 Fourier 指数增加 $e^{2\pi i4x}$。
由全局加性角色积公式，这准确等于在三处将
$h_0$ 换成 $m_{-4}h_0$，其中
$m_b f(u)=\psi_3(bu)f(u)$。
二处因为 $4u\in\mathbf Z_2$ 而没有变化，
其余有限标准球也没有变化。

在三个陪集 $u=0,1/3,2/3\bmod\mathbf Z_3$ 上，
该新列为 $(1,\omega,\omega^2)$。
R391 的原核在这三个陪集上准确是
$$
\frac1\delta
 \begin{pmatrix}1&\omega&\omega\\
                 \omega&1&\omega\\
                 \omega&\omega&1\end{pmatrix}.
\tag{3}
$$
列 $(1,\omega,\omega^2)$ 的特征为 $\omega^2$；
这与 ground 列 $(1,1,1)$ 的特征一不同。
全球有理 $\omega$ 保持 theta 求和，二处及其余有限向量不变，
无限 Gaussian 的第零型也不变，所以 $S_-(1/3)=0$。

$\mu_6$ 作用给 $E[3]$ 中六个 generic 非零三挠点的零。
如果 $S_-(O)=0$，原偶性与三次对称要求其阶至少六，
加上这六点就超过 degree8，故 $S_-(O)\ne0$。
剩余两次零必须组成一个 $\mu_6$ 稳定的 degree-two 除子；
它只能是两个非零 $\delta$ 核点，且每个重数一。
因此全部零除子准确是 $E[3]\setminus\{O\}$。
右边 $K_8$ 有完全相同的除子和 line bundle，且 $K_8(0)=1$，
故得到 (2)。

$\kappa_0$ 的准确规范为
$$
\boxed{
\kappa_0=\sum_{n\in\mathbf Z}
 v_2(11n)\exp(-\pi\sqrt3\,n^2/48)\in\mathbf R^\times .
}
\tag{4}
$$
它是原 theta 值，不在这里被冒称为代数数或 p-adic 单位。

## 2. 真正的共同 degree72 参考

令
$B(Z)=K_8(3Z).$
物理格为 $\Omega_{24}\Lambda$，标准 sigma 的准确齐次式是
$
\sigma_\Lambda(Z)=\Omega_{24}^{-1}\sigma_{E_{24}}(\Omega_{24}Z).
$
所以这里没有遗漏一个三或九的变量因子：
$
\boxed{
K_{8,\Lambda}(3Z)=K_{8,E_{24}}(3\Omega_{24}Z)
=\frac{\sigma_{E_{24}}(9\Omega_{24}Z)}
       {3\sigma_{E_{24}}(3\Omega_{24}Z)}.
}
\tag{5a}
$
后文物理表达式中的 $G_{24}(z)$ 指
$G_{24,\Lambda}(z/\Omega_{24})$；原 square 的 $c$ 仍是 (20)。
在 R393 的 $x=n/36$ 格上，以旧 $h_0$ 替换新 $\phi_3$，
三处恰强迫 $3\mid n$。写 $n=3k$，
二处系数变成 $v_2(27k)=v_2(11k)$，
Gaussian 和 Fourier 指数也准确变成旧来源的 $3Z$。
所以这个实际共同来源就是
$$
\boxed{S_-(3Z)=\kappa_0 B(Z)\in H^0(\Lambda,\mathcal O(72O)).}
\tag{5}
$$
这已经付清共同 line bundle，未用 degree16 的假对应。

对任意有理格点 $t$，将 quasi-period 实线性延长为
$$\eta_t=2\sqrt3\pi\,\bar t,$$
并使用原对称 Mumford lift
$$
(\mathsf T_tG)(Z)=
 e^{-72\eta_t(Z+t/2)}G(Z+t).
\tag{6}
$$
若 $t\in E[9]$，该 lift 保持本篇 degree72 line bundle，
且 $\mathsf T_t^9=1$。所有以下公式保留具体的有理代表 $t$，
不在删除中心相位后才归约到 torsion 标签。

## 3. 十八项局部运输的完整全局化

R391 给三处的原式
$$
\phi_3=(I+W_\omega+W_\omega^2)
 \sum_{\varepsilon=\pm1}\sum_{j=0}^2
 \zeta_9^{5\varepsilon j}\,
 \mathcal H(\varepsilon/9,j)h_0.
$$
为将它放进同一全局 theta，不能只把一个三处平移误作全球平移。
对每项准确选择
$$
a=4\varepsilon/9,\qquad b=4j.
$$
二处 $a\in4\mathbf Z_2$ 是 $\phi_2$ 的实际周期，
$b\cdot\operatorname{Supp}\phi_2\subset\mathbf Z_2$；
其他有限标准球也被这两个操作保持。
在三处直接比较未对称的算子，准确有
$$
\tau_a m_bh_0
 =\omega^{\varepsilon j}\tau_{\varepsilon/9}m_jh_0.
\tag{7}
$$
这里 $\tau_a f(u)=f(u-a)$，没有省略来自 $a-\varepsilon/9$ 的常数。

原有理重新编号把全有限 $\tau_a m_b$ 送到
$$
t=\frac{i\kappa a-b}{36}
 =\frac{\varepsilon\tau_0-j}{9},\qquad \kappa=3\sqrt3 .
\tag{8}
$$
完整 Gaussian 比较给
$$
S_{\tau_am_b}(Z)=e^{\pi iab}\mathsf T_tS_{\mathrm{base}}(Z).
\tag{9}
$$
例如其线性指数准确为
$-144\sqrt3\pi tZ+72\pi iaZ=-72\eta_tZ$；
常数与 $-36\eta_tt$ 的差为 $\pi iab$。
所以 (7) 的逆因子和 (9) 相乘恰为
$$
\omega^{-\varepsilon j}e^{16\pi i\varepsilon j/9}
 =\zeta_9^{5\varepsilon j}.
\tag{10}
$$

最后，外层三处 $W_\omega$ 可由全球有理 $\omega$ 转到无限端；
其他有限向量原本不变。它在 reduced 来源上给变量的三次旋转。
因为求和包含全部三次幂，取正或逆旋转得到同一个准确和。
$\eta_{\omega^{-r}t}=\omega^r\eta_t$ 又支付 lift 的旋转。因此
$$
\boxed{
\frac{S_{24,\Lambda}(Z)}{\kappa_0}
 =\sum_{r=0}^2\sum_{\varepsilon=\pm1}\sum_{j=0}^2
   \zeta_9^{5\varepsilon j}
   \mathsf T_{\omega^r(\varepsilon\tau_0-j)/9}B(Z).
}
\tag{11}
$$
这是同一原 rank-two 来源的实际十八项恒等式。
没有将 $\mathsf T_t$ 与 Mellin 观察交换。

## 4. 保留全部中心后的六项合并

首先，$B=K_8(3Z)$ 对每个真实 $E[3]$ lift 都准确不变：
$$\mathsf T_eB=B\qquad(3e\in\Lambda).$$
这由 $K_8$ 的 degree-eight quasi-period 直接得到。
又 (6) 给实际群律
$$
\mathsf T_a\mathsf T_b
 =e^{36(\eta_ab-\eta_ba)}\mathsf T_{a+b}.
\tag{12}
$$

写 $t=(m+ns)/9$。乘 $\omega$ 在整数标签上的矩阵为
$$
(m,n)\longmapsto(-2m-n,\,3m+n).
\tag{13}
$$
若把某个标签 $v$ 减至 $v_0=(m,n)\bmod3$、$0\le m,n\le2$，
写 $v-v_0=3w$，则 $e=w/3$ 是实际三挠点。
由 $\eta_1s-\eta_s=2\pi i$，(12) 给准确中心因子
$$
\mathsf T_{v/9}B
 =\omega^{-\det(v_0,w)}\mathsf T_{v_0/9}B.
\tag{14}
$$

把 (11) 的十八项按 (13)–(14) 收集，令
$$A=1+\zeta_9^4+\zeta_9^5.$$
全部非零系数表是
$$
\boxed{
\begin{array}{c|ccc}
 &m=0&m=1&m=2\\ \hline
n=1&A&\omega A&\omega^2 A\\
n=2&A&\omega A&\omega A .
\end{array}}
\tag{15}
$$
例如 $(0,1)$ 的三个原相位是 $1,\zeta_9^4,\zeta_9^5$；
$(1,1)$ 的三个相位是 $\zeta_9^3,\zeta_9^7,\zeta_9^8$；
$(2,1)$ 的三个相位是 $\zeta_9^6,\zeta_9,\zeta_9^2$。
另一行按 (14) 得到表中所列数，并非把两个坐标当独立循环而猜出。

于是定义真正的规范源
$$
\boxed{
G_{24}=
 \mathsf T_{s/9}B+\omega\mathsf T_{(1+s)/9}B
 +\omega^2\mathsf T_{(2+s)/9}B
 +\mathsf T_{2s/9}B+\omega\mathsf T_{(1+2s)/9}B
 +\omega\mathsf T_{(2+2s)/9}B.
}
\tag{16}
$$
则准确有
$$\boxed{S_{24,\Lambda}=\kappa_0 A\,G_{24}.}\tag{17}$$

在 $\mathbf Q(\zeta_9)$ 中直接约简给
$$
\boxed{
A^3-3A^2+3=0,\quad
N_{\mathbf Q(\zeta_9)^+/\mathbf Q}(A)=-3,\quad
A^2=f_1 .
}
\tag{18}
$$
其中 $f_1$ 是 R391/R393 的同一个范数系数。
特别 $A$ 为实数，非零，且在每个 $p>3$ 都是单位。
$G_{24}$ 因 (17) 是原实、偶、$\mu_3$ 不变来源；
它不是六个独立未知中央量的任意组合。

## 5. 规范平方常数中的代数根准确消去

旧 $E_-$ 来源的有限范数为
$3\cdot\|h_0\|^2=9$。
同 R393 的实际 $S_1=\{2\}$、$c(0)=2/3$、体积比六，
其第零权 Yang 公式为
$$
\boxed{
L(E_-,1)=\frac{\pi\sqrt{6\sqrt3}}{54\sqrt3}\,\kappa_0^2.
}
\tag{19}
$$
所以 (2) 也无条件给 $L(E_-,1)>0$。

保持 R393 原变量
$$
c=\frac{\sqrt{3\sqrt3}}{72\pi i},\qquad
G_{24}(cT)=\sum_{m\ge0}g_m\frac{T^m}{m!}.
\tag{20}
$$
R393 的完整常数、(17)–(19) 联立，准确得到
$$
\boxed{
L(\psi_{24}^{2m+1},m+1)
 =\frac{L(E_-,1)}6\,\frac{(4\pi)^m}{m!}\,g_m^2,
\qquad m\ge0,\quad6\mid m.
}
\tag{21}
$$
这里 $A^2=f_1$ 使原代数范数根完全相消。
$\kappa_0$ 的准确值仍由 (4) 定义；
没有宣称它本身是某个 p-adic 单位。
(16) 独立定义了规范的代数来源，(21) 保留真实的参考复周期常数。
物理变量仍是 $z=\Omega_{24}Z$，不省略 (20) 的尺度。

## 6. 原整 theta 格中的 primitive 性

以下是整个有限来源格的结论，不是中央观察非零。

在 $E_b:y^2=x^3+b$ 的实际 sigma frame 中，取 $b=24$，
令 $\mathcal L=\mathcal O(72O)$。
每个 (16) 的 $t$ 属于固定 $E[9]$，且原 lift 有九阶。
这些 lift 在一个固定代数扩张中都是代数的：
取代数 line-bundle 平移同构，再将其九次复合的标量开九次根；
与 (6) 的九阶 lift 比较，所差只能是九次单位根。
因此可一次固定系数域
$L=K(E_{24}[9],\mu_9,\{c_t^{1/9}\}_t)$：
这里六个 $c_t$ 是任取代数平移同构的九次复合标量，
只取 (16) 所需的固定有限集合。此域与目标素数无关；
改变最初代数同构不改变上述原九阶 lift。
下面的整模型论证进一步给所有好 $p>3$ 的整性，
不只给未指定的有限坏分母集合。

对每个好 $p>3$，$E[9]$ 与其有限 theta 群是 étale。
上述平移同构在整模型上存在；九次复合是单位，
开九次根仍为单位。与原九阶 lift 比较也只差单位根，
故 (16) 的每个 lift 及其逆都保持原整截面格。
这一步同时支付 vertical scalar，不能仅从其复特征值为单位推断。

$B=K_8(3z)$ 是原整截面，且 $B(0)=1$。
也可写成
$$B=\sigma^{72}\frac{r_9}{3r_3},\qquad
r_n=\sigma(nz)/\sigma(z)^{n^2},$$
其中除法多项式商的顶系数为一，只有固定三处分母。
故 $B$ 在每个 $p>3$ 的约化非零。

对 $e\in E[3]$，$\mathsf T_tB$ 的特征由 (12) 的 commutator 给出。
配对
$$E[3]\times(E[9]/E[3])\longrightarrow\mu_3$$
非退化，因为本 line-bundle 的 degree 为 $72$，其除以九所得八
在三处为单位。因此 (16) 的六项属于六个不同特征空间。
在 $p>3$ 的原整模型上，这些特征空间仍互相独立，
每项非零，且系数 $1,\omega,\omega^2$ 都是单位。
所以
$$
\boxed{
G_{24}\text{ 在每个好 }p>3\text{ 的原整 degree72 来源格中非零。}
}
\tag{22}
$$
它的原点质量仍为零，指定高阶中央观察仍可能消失。
(22) 没有把这些不同观察相认，也不把完整 Selmer 条件略去。

## 7. 六项共同零除子给实际固定因子

$B=K_8(3z)$ 的零除子准确为 $E[9]\setminus E[3]$。
所以 $\mathsf T_tB$ 的零除子为
$E[9]\setminus(E[3]-t)$。
(16) 的六个缺失陪集恰为 (15) 中的 $n=1,2$；
余下 $n=0$ 的三个陪集、共二十七点，全部是每项的零。

这些二十七点恰为 $E[3\delta]$。
事实上 $\delta=1+2\omega$ 在 $\{1,s\}$ 基中的矩阵为
$$
\begin{pmatrix}-3&-2\\6&3\end{pmatrix},
$$
所以在 $E[9]$ 上 $[3\delta]$ 的核准确要求 $n\equiv0\pmod3$。
因此
$$
\boxed{G_{24}\text{ 在全部 }E[3\delta]\text{ 上为零。}}
\tag{23}
$$

现在写 $X=x^3$。原 triplication 给
$$
x(3z)=
 \frac{X^3-96bX^2+48b^2X+64b^3}
      {9x^2(X+4b)^2},
\qquad
\sigma(3z)=3\sigma^9x(X+4b).
$$
再用原 CM 三次身份 $\sigma(\delta z)=\delta x\sigma^3$，得到
$$
\boxed{
\sigma(3\delta z)=3\delta\,\sigma^{27}x\,Q_4(X),\quad
Q_4(X)=(X+4b)(X^3-96bX^2+48b^2X+64b^3).
}
\tag{24}
$$
这是全函数恒等式，保持标准 sigma/division 的奇数符号。

由 R393，$G_{24}=\sigma^{72}P_{11}(X)$。
(23) 的二十四个非 $x=0,O$ 点要求 $Q_4\mid P_{11}$；
两个 $x=0$ 的非零三挠点还要求 $P_{11}(0)=0$。
这些根互异，且 $Q_4(0)=256b^4\ne0$，故
$$
\boxed{
G_{24}(z)=\sigma(z)^{72}\,XQ_4(X)\,R_6(X),
\qquad \deg R_6\le6 .
}
\tag{25}
$$
在物理变量中 $b=24$；
换到别的 CM frame 时必须同 R393 保持真实 homothety。
(25) 把实际待求分子降为七个系数，不把它换成任意 degree-six
候选。其系数由 (16) 唯一决定。

由 §6 的原整性、monic 的 $XQ_4$，$R_6$ 也在好 $p>3$ 整；
(22) 保证其约化不恒零。
本篇尚未求出这七个具体系数，也未从这个 primitive 性推出
原中央权的非消失。后续要实际计算同一 $R_6$ 及完整中央运输。

## 8. 可复现输入与后续接口

十八项合并只需固定的九次根及 (13)：
初始整数标签为 $(-\varepsilon-j,2\varepsilon)$，
依次乘 (13) 三次；令 $v_0=v\bmod3$、$w=(v-v_0)/3$，
累加相位
$$\zeta_9^{\,5\varepsilon j-3\det(v_0,w)}.$$
直接收集得到 (15)，在
$\zeta_9^6+\zeta_9^3+1=0$ 下约简得到 (18)。
这些是固定的十八项准确运算，没有按目标素数扫描。

R393 的原普通测度、中央平方与全 Selmer 桥仍须按各自完整规范
建立；本篇只提供可用的实际有限来源、整格与 (21) 的复常数。
尤其不能把任一项 $\mathsf T_t$ 与原 Mellin 泛函直接交换，
也不能从六个独立 theta 特征空间宣布六个中央值独立。

仓库依赖：
[R389](R389-e24-primitive-wild-local-data-and-actual-hermitian-class.md)、
[R391](R391-e24-original-wild-three-schwartz-and-heisenberg-transport.md)、
[R393](R393-e24-original-dyadic-vector-degree-seventytwo-and-full-squares.md)。
原表示与平方公式的已发表输入见这些结果所列 Yang 1997、1999；
本篇的 (2)、(7)–(18)、(23)–(25) 全部在正文直接证明。

提交前 API main 为 $3d17740d56142f55aa8cc63ce394f1651bfcde35$，
两份 README blob 与已读版本一致。
执行终端仍不可用，本篇为根规矩八允许的小文本 Contents API 提交，
不是一次本地 git pull。
