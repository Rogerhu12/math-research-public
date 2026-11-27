# 原 type‑4 惰性负二 Newton 读者、完整图迹首层与真实 signed 支

日期：2026-11-27 UTC。

本注保持 [R806](../results/R806-original-type-four-order-eighteen-and-negative-two-katz.md) 的三个实际十八阶角色、原 degree34 截面和全部坏位规范。新增结论是：同一截面有一个完整过收敛的负二 Newton 读者；[R1049](../results/R1049-original-inert-syntomic-graphs-and-crystalline-lattice.md) 的原 full9／54 图迹，模 $p$ 准确读取这个读者的归一端点。图迹首层非零还迫该 Newton 函数为整 Tate 单位，因此同时控制所有合法正整数权。另用已公开预印本的高权 local sign decomposition，核定原 Soulé 来源在这里的真实 signed 支。

本注没有把 type 差为三的表示换成椭圆曲线 Tate 模，也不把同一个局部表示中的两条全局类自动相认。下面的图迹平方、Newton 全权式和原单位 signed 归属分别给出实际公式。

## 1. 固定原来源和三个不同的常数

置
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad
\mathcal J=\{4,10,16\},\quad E_0:y^2=x^3+1,
\qquad dz=\frac{dx}{2y}.
\tag{1}
$$
取原 $x=z^{-2}+\cdots,\ y=-z^{-3}+\cdots,\ \sigma=z+\cdots$。
R806(8) 的有限角色为
$$
\eta_j((a))=
\left[
 \operatorname{Teich}_{\mu_3}(a\bmod2)^{-1}
 (a\bmod17)^{16(j-9)}
\right]^{-1}.
\tag{2}
$$
十七处值取原 $\mu_{18}$ 提升。它们的准确阶为18，导子为 $(34)$，
$\eta_j^c=\eta_j^{-1}$，在有理 idèle 上平凡。
尤其 $\eta_j((p))=1$ 对本注惰性好素数成立。
这与三处的原值 $\eta_j((\delta))=-1$ 并不矛盾。

原完整 finite tensor、Haar 以及 Hermitian 代表 $\alpha=17$ 均沿 R806。
其 monic 规范截面写为
$$
D_j(z)=D_{j,1}(z)=
 \sigma(z)^{34}P_j(x(z)^3)
 =\sum_{m\ge0}d_{j,m}z^m,
\quad
P_j(X)=X^5+\sum_{\ell=0}^4u_{j,\ell}X^\ell,
\quad d_{j,4}=1.
\tag{3}
$$
只有 $m\equiv4\bmod6$ 的系数可能非零。
这些是 R806 的实际三条线，不是另一组具有相同 good eigenvalues 的候选。

固定一个包含全部系数的数域和原 $p$-adic 嵌入。以下删去一个明确的固定有限集合：$2,3,5,17$，三个 $P_j$ 的系数分母、R806 的固定全权常数 $c_j$ 的零极支撑，以及应用 R1049 时原固定有限图、Artin 格和 $\gamma_j$ 的坏支撑。可把此集合定义为这些已指定代数数的分母／分子范数之素因子，无须另作随 $p$ 的选择。再要求
$$
p\ge11,\qquad p\equiv5\bmod6,\qquad d=p+1=6s.
\tag{4}
$$
凡涉及原几何参数 $h_{j,p}$，另保 R1049 的 $p>q_0$ 及其全部整格前提；只论下文 §§2–3 的 Newton 函数时不需要这项条件，也不需要 $c_j,\gamma_j$ 为单位。纯 Newton 结论只需 $p\ge11$、$p\equiv5\bmod6$、$p\nmid34$ 和原 $P_j$ 的系数在该位整。

剩余系数环记为 $\mathcal O$，$v_p(p)=1$。可在排除固定判别式支撑后取其在 $p$ 的不分歧完成，所以以下整系数赋值的向上取整有效。

必须区分三个不同对象：
$$
c_\sigma=[z^{p+1}]\log(\sigma/z),\qquad
c_p=\binom{3s-1}{2s-1}\bmod p,\qquad
c_j\in\overline{\mathbf Q}^{\times}.
\tag{5}
$$
前者是原 Gaussian 的特征零系数，第二个是 R887 的横向 Hasse 值，
第三个是 R806(27) 的固定全权平方常数。
R301(5)、R887(46) 给
$$
v_p(c_\sigma)=-1,\qquad
pc_\sigma\equiv-c_p\pmod p,\qquad
\rho_p=c_p^{-1}.
\tag{6}
$$
其中首个准确剩余类也可写为
$pc_\sigma\equiv-(-1)^s4^{-s}\binom{2s}{s}$。
它不是一个可另选的单位。

## 2. 同一原截面的负二 Newton 函数

令
$$
C_p=34c_\sigma,\qquad
G_j(z)=D_j(z)e^{-C_pz^d},
\qquad
a_{j,h}=C_p^{-h}[z^{dh-2}]G_j(z)
\quad(h\ge0),
\tag{7}
$$
负次系数按零解释。定义下降阶乘和真实级数
$$
(v)_h=v(v-1)\cdots(v-h+1),\qquad
\mathcal J_{j,p}^{[-2]}(v)=\sum_{h\ge0}a_{j,h}(v)_h.
\tag{8}
$$
由于 $D_j$ 从 $z^4$ 起，$a_{j,0}=0$。

这里的指数首先是形式乘积；不要求被单独取出的
$e^{-C_pz^d}$ 在下面整个圆盘收敛。实际解析表达使用
$$
W=z^2x,\quad F=\log(\sigma/z),\quad R=p^{-1/(2p)}.
$$
R301 §§2–4 对原形式对数已完整证明
$\|W\|_R\le1$ 和 $\|F-c_\sigma z^d\|_R<p^{-1/(p-1)}$。
由(3)，
$$
z^2G_j=
z^6\left[
 W^{15}+\sum_{r=1}^{5}u_{j,5-r}z^{6r}W^{15-3r}
\right]e^{34(F-c_\sigma z^d)} .
\tag{9}
$$
全部 $u_{j,\ell}$ 在当前位整，故
$\|z^2G_j\|_R\le R^6$。
因此与 R301 的原估计逐项相同，
$$
\boxed{
v_p(a_{j,h})\ge
B_{p,h}:=
\left\lceil\frac{h(p-1)+6}{2p}\right\rceil
\quad(h\ge1).
}
\tag{10}
$$
这支付了整个 $P_j$ 的高尾，而非只留下首单项。

于是(8)在 $|v|_p<p^{(p-1)/(2p)}$ 上解析，并且
$$
\mathcal J_{j,p}^{[-2]}(v)\in pv\,\mathcal O\langle v\rangle,
\qquad
\boxed{
\mathcal K_{j,p}^{[-2]}(v):=
\frac{\mathcal J_{j,p}^{[-2]}(v)}{pv}
\in\mathcal O\langle v\rangle .
}
\tag{11}
$$
在 $v=0$ 按可去奇点取值。式(9)中的 $z^2$ 仅说明系数平移；
没有把 $z^2D_j$ 宣称为同一 degree34 的代数 theta 截面。

## 3. 全整数权、原 $m!$ 和精确首层

对每个整数 $k\ge1$，$(k)_h=0$ 对 $h>k$。
因此有限 Gaussian 卷积而非无限换序给
$$
\boxed{
\begin{aligned}
\mathcal J_{j,p}^{[-2]}(k)
 &=k!C_p^{-k}d_{j,dk-2},\\
\mathcal K_{j,p}^{[-2]}(k)
 &=\frac{(k-1)!}{p}C_p^{-k}d_{j,dk-2}.
\end{aligned}}
\tag{12}
$$
即使 $p\mid k$，第二式也由(11)的整函数成立；
不将中间的 $1/k$ 当成单位。

R806 的所有合法正权平方是
$$
\mathscr E_{j,m}:=
\frac{(2\pi/\sqrt3)^m
 L(\eta_j\psi_0^{2m+1},m+1)}
 {m!\varpi_0^{2m+1}}
=c_j34^{-m}d_{j,m}^{\,2}.
\tag{13}
$$
$m=dk-2\ge0$ 且 $m\equiv4\bmod6$，所以(12)准确得到
$$
\boxed{
\mathscr E_{j,dk-2}
=34^2c_j
 \left(34^{\,1-p}c_\sigma^2\right)^k
 \frac{p^2}{((k-1)!)^2}
 \mathcal K_{j,p}^{[-2]}(k)^2 .
}
\tag{14}
$$
左边的 $m!$ 与右边的 $(k-1)!$ 是不同的原因子。
没有省去任何一个，也没有对 $p^v$ 或 $c_\sigma^v$ 作未定义的解析延拓。
(14)只在显示的整数权解释幂；其归一后解析函数由(7)–(11)直接构造。

对 $h\ge2$，(10)至少为二。
又 $[z^{d-2}]G_j=d_{j,p-1}$。故在整个 Tate 代数中
$$
\boxed{
\begin{aligned}
\mathcal J_{j,p}^{[-2]}(v)
 &\equiv\frac{d_{j,p-1}}{34c_\sigma}\,v\pmod{p^2},\\
\mathcal K_{j,p}^{[-2]}(v)
 &\equiv
 \frac{d_{j,p-1}}{34pc_\sigma}\pmod p .
\end{aligned}}
\tag{15}
$$
第二式是恒定函数的同余。
它没有断言 $d_{j,p-1}$ 被 $p$ 整除；恰恰因为 $pc_\sigma$ 是单位，
$d_{j,p-1}$ 可以且在非零首层时必须是单位。

于是
$$
\boxed{
d_{j,p-1}\in\mathcal O^\times
\iff\mathcal K_{j,p}^{[-2]}(0)\in\mathcal O^\times
\iff\mathcal K_{j,p}^{[-2]}\in\mathcal O\langle v\rangle^\times .
}
\tag{16}
$$
若这些条件成立，则全部 $k\ge1$ 同时满足
$$
\boxed{
v_p(d_{j,dk-2})
=1-k-v_p((k-1)!).
}
\tag{17}
$$
这给同一截面的整个合法整数支，而非另取随 $k$ 改变的来源。

端点的全部精度也有原有限证书：
$$
\mathcal K_{j,p}^{[-2]}(0)
=\frac1p\sum_{h\ge1}(-1)^{h-1}(h-1)!\,a_{j,h}.
\tag{18}
$$
截到 $h\le H$ 后，误差赋值至少
$$
\boxed{
\left\lceil
 \frac{(H+1)(p-1)+6}{2p}
\right\rceil+v_p(H!)-1 .
}
\tag{19}
$$
它随 $H$ 趋于无穷，允许原首层为零而后续层非零。
这不是把模 $p$ 的图迹式擅自提升为全部 $p$-精度的平方。

### 3.1 已消费的固定 $p=29$ 给出的整个整数权支

[唯一原29消费者](2026-11-27-original-type4-inert29-coefficient.md)§§4–5已经证明：原 CM13 完整整算子、整谱幂等元及三个 $z^4$ 归一量在29均为单位；因此三个原 $P_j$ 在29整，且三个 $d_{j,28}$ 均为29单位。式(10)–(17)仅需这些纯 theta 条件，故对三个原 $j$ 都有
$$
\mathcal K_{j,29}^{[-2]}\in\mathcal O\langle v\rangle^\times,\qquad
v_{29}(d_{j,30k-2})=1-k-v_{29}((k-1)!)\quad(k\ge1).
$$
这消费的是同一份已完成的原29回执，未重新运行，也未增扫素数。
无需在29核 $c_j,\gamma_j$ 的单位性或原几何 $q_0$，因为这里没有向 $h$、临界归一常数或通常 $\Sha$ 外推。

## 4. 原 full9／54 图迹准确读取此端点

保持 R1049 的固定未 depletion 最高循环 $Y_{j,0}$、原54个图、
所有 $\eta_j$-权、完整 $\operatorname{Cor}_{L/K}$、
$P^-$、$e_A^-$ 和原 Artin 基 $a_{j,p}$。
记其已付整参数为 $h_{j,p}$；原 syntomic/Bloch–Kato 对数是
$p h_{j,p}/(p+1)$。

令
$$
\gamma_j=\frac{L(\psi_{27}\eta_j,1)}{\Omega_{27}},
\qquad
r_\infty=\frac{\varpi_0}{\Omega_{27}}
=\epsilon_{\rm per}^{-1}2^{-1/3},
\quad\epsilon_{\rm per}\in\mu_6 .
\tag{20}
$$
这里 $r_\infty$ 与 $\rho_p$ 不同。
R1049 §§12–13 的完整 Manin／toric 比较已给
$$
\begin{aligned}
\bar h_{j,p}^{\,2}
 &=-27\,\bar\alpha_{A,p}^{\,2}\,
   \bar a_{j,p}^{-2}[L:H]^2\,
   \bar U_{j,p}
   \bigl((p-1)!\,\bar d_{j,p-1}\bigr)^2,\\
U_{j,p}
 &=2\omega\,3^{p+1}34^2c_j\gamma_j r_\infty^{\,2p-1}.
\end{aligned}
\tag{21}
$$
$\alpha_{A,p}$ 是同一个 $A=E_{27}$ 的 crystalline Frobenius
在原杯积基中的系数，未重选成任意单位。
式(21)中的 $[L:H]^2$ 正是原全 Cor；没有在此去掉18或243。

(15)已经无条件把(21)变成
$$
\boxed{
\bar h_{j,p}^{\,2}
=-27\bar\alpha_{A,p}^{\,2}\bar a_{j,p}^{-2}[L:H]^2
 \bar U_{j,p}(34\,\overline{pc_\sigma})^2
 \overline{\mathcal K_{j,p}^{[-2]}(0)}^{\,2}.
}
\tag{22}
$$
全部因子都有原来源；当前删集外，显示乘子为单位。
特别
$$
\boxed{
\bar h_{j,p}\ne0
\iff\bar d_{j,p-1}\ne0
\iff\overline{\mathcal K_{j,p}^{[-2]}(0)}\ne0 .
}
\tag{23}
$$

R1049 §14 的同一 Čech／杯积定标进一步给
$$
\bar\alpha_{A,p}
=-2^{(p+1)/3}\rho_p,\qquad
\overline{pc_\sigma}=-\rho_p^{-1}.
\tag{24}
$$
沿 $I_{27}^*\omega_A=t\omega_0$、$I_{27}^*\epsilon_A=t^{-1}\epsilon_0$
而非另选 period，式(22)遂完全化为
$$
\boxed{
\bar h_{j,p}^{\,2}
=
\overline{
 -972\,\omega\,34^4\,\epsilon_{\rm per}^{-3}
 c_j\gamma_j\,a_{j,p}^{-2}[L:H]^2
}
\ \overline{\mathcal K_{j,p}^{[-2]}(0)}^{\,2}.
}
\tag{25}
$$
确切相消是
$2\cdot2^{2(p+1)/3}\cdot2^{-(2p-1)/3}=4$、
$3^{p+1}\equiv9$、
$2p-1\equiv3\bmod6$ 以及 Wilson 阶乘的平方为一。
因此不是“一个可能依赖 $p$ 的未知周期单位”。
(25)仍保真正 Artin $a_{j,p}$ 和全 Cor。

本文始终使用 $D_{j,1}$。若返回原 $b=17$ 模型，
R806(24) 的准确式是
$$
D_{j,17}(z)=\theta^{-4}D_{j,1}(\theta z),\qquad\theta^6=17.
\tag{26}
$$
必须同时令 $c_{\sigma,17}=\theta^d c_\sigma$。
由(7)逐项得到
$\mathcal J_{j,p,17}^{[-2]}=\theta^{-6}\mathcal J_{j,p,1}^{[-2]}
=17^{-1}\mathcal J_{j,p,1}^{[-2]}$，
同样 $\mathcal K_{j,p,17}^{[-2]}=17^{-1}\mathcal K_{j,p,1}^{[-2]}$。
这实际支付原17缩放；若将(25)改写为17模型，右边须相应乘 $17^2$。

## 5. 高权 local sign theorem 在这里的真实支

这里的表示是 R804 的
$$
V_j=\eta_j^{-1}\widehat\psi_0^{\,2}
                 \widehat{\bar\psi}_0^{-1}
=\eta_j^{-1}\widehat\psi_0^{\,3}\chi_{\rm cyc}^{-1}.
\tag{27}
$$
其两 Hodge–Tate 权为 $(2,-1)$。
在惰性 $K_p/\mathbf Q_p$ 上，$\eta_j$ 未分歧且
$\eta_j((p))=1$，所以它的本地有限限制准确平凡。
原良 supersingular 形式群是参数 $-p$ 的 Lubin–Tate 群。
这给(27)在原整基上的 conjugate symplectic self-dual 结构。

使用 Burungale–Kobayashi–Nakamura–Ota，
*A local sign decomposition for symplectic self-dual Galois representations of rank two*，
[arXiv:2508.17776v1](https://arxiv.org/html/2508.17776v1)，
Theorem 3.1、Lemma G.22、Theorems G.25/G.29。
该定理允许任意 $(k+1,-k)$，这里准确是 $k=1$。
为对应作者 $\mathbb T_\phi=T_\phi^{-1}(1)\otimes\Lambda^\iota$，
取 $\phi=V_j^{-1}(1)$，并以共轭嵌入排列其正 Hodge–Tate 权；
不能沿用 HT$(1,0)$ 情形的符号。

记 $\Gamma$ 为原反圆分 $\mathbf Z_p$-群，
$\Lambda=\mathcal O[[\Gamma]]$，
$\mathbb T_j=T_j\otimes\Lambda^\iota$。
Lemma G.22 对 $p>3$ 支付 generic 条件；
本地 $-p$-Lubin–Tate 在有理 uniformizer 上的负号也直接排除模 $p$
不变向量。由上述定理得到真正的整直和
$$
H^1(K_p,\mathbb T_j)=M_{j,p}^{+}\oplus M_{j,p}^{-},
\qquad M_{j,p}^{\pm}\simeq\Lambda .
\tag{28}
$$
它与任意连续 base change 相容，不是只差有限模的分解。

作者 G.29 的 $\delta_{\rm loc}$ 是 $K_p/\mathbf Q_p$ 的 trace-zero
**单位**。本地有限角色在它上的值是1；不能拿(2)的三处
uniformizer 值 $\eta_j((\delta))=-1$ 代入。
在未分歧 augmentation，作者的 completed epsilon 为
$(-1)^k=-1$，所以
$$
\boxed{
M_{j,p}^{+}\otimes_{\Lambda,\mathbf1}\mathcal O
=H_f^1(K_p,T_j).
}
\tag{29}
$$
这里是 **正线**。
若 $\Xi_{2r}$ 是导子指数为 $2r$ 的非平凡反圆分有限角色，
G.29 的准确消失描述是
$$
M_{j,p}^{+}
=\{z:\exp_\chi^*z=0
       \text{ 对全部 }\chi\in\bigcup_{r\ge1}\Xi_{2r}\},
\tag{30}
$$
并可加入平凡角色。负线用奇导子族。
此处 $H_f^1$ 是一维；由于原 crystalline $\varphi^2=-p^{-1}$
没有不变向量，Bloch–Kato 对数在该线上的有理版本为同构。
这没有把其标量定成(25)的平方，也不省略原 Artin 基。

## 6. 原全局单位的实际归属与尚须比较的标量

R804 §§2–3 的**全局单位构造**本身不要求 $p$ split：
保持同一 $34\delta$ ray class 单位、同一 $e_{\eta_j}$，
在完整 $H K(E_0[p^\infty])$ 上扭曲，再投原反圆分商。
辅助 $(5)$ 因子在本篇各自对偶权上仍是
$25-(-5)=30$，所以可整除以30。
这定义原全局 Iwasawa 类及其局部像
$\boldsymbol z_{j,p}$，augmentation 为该原 Soulé 类；
没有用局部对数逆像重新命名一个类。

其 signed 归属可以实际核定。
反射的固定 weight4 角色是 $\eta_j^{-1}\psi_0^3$，R806 已给 root $-1$。
若 $\chi$ 是导子 $p^a$ 的原反圆分 $p$-power 角色，
在2、17的未分歧值为1，因为这两处理想是有理主理想；
在3处，$\chi((\delta))^2=1$ 与其 $p$-power 阶迫值为1。
故全部旧坏位 epsilon 保持。
惰性 $p$ 的 self-dual Gauss 公式准确多出 $(-1)^a$：
trace-zero 单位平方有理，故它在 $\chi$ 下仍取1。
于是整个反射角色的符号为
$$
W(\eta_j^{-1}\psi_0^3\chi)=-(-1)^a.
\tag{31}
$$
对每个偶 $a$，相应临界复值为零。
同一全局单位的 Kato CM 显式互反律
（R303 §4 所核的 Kato (15.16.1)、Theorem 12.5，保全部 finite character）
使 $\exp_\chi^*\boldsymbol z_{j,p}=0$。
将这些完整偶导子值代入(30)，得到
$$
\boxed{\boldsymbol z_{j,p}\in M_{j,p}^{+}.}
\tag{32}
$$
这是真正原单位的支识别，不是只说存在一条局部 rank-one 直线。

正整数权 $m=dk-2$ 同样来自这个单位系统的 tensor twist：
最终表示为
$\eta_j^{-1}\psi_0^{-(2m+1)}\chi_{\rm cyc}^{m+1}$，
其局部 tame 支与(27)相同，因为 $d=p+1$ 杀反圆分有限 torus。
实际 Kato 正权读数因此仍用(13)的原临界值。
其共同惰性 Euler 因子为 $1+1/p$，赋值 $-1$；
临界 $m!$、完整 Tate period 和正负支的 de Rham 基必须保持。
式(14)支付的是原 theta／临界值的完整归一，不以“相同表示”删除这些因子。

选一原始 $\Lambda$-基 $e_p^+$，可写
$\boldsymbol z_{j,p}=A_{j,p}(T)e_p^+$（原 Artin 基相容后）。
Theorem G.29 支付此整坐标的存在和 augmentation，
但不单独证明
$A_{j,p}(0)$ 等于 $\mathcal K_{j,p}^{[-2]}(0)^2$
乘一个已知单位。
同样，R1049 的固定图类和这个全局单位类虽进入同一个(29)，
还需原 global comparison 才能相认。

当前已付的实质结论为(22)／(25)：
**同一个原 full9／54 读数的首层，准确比较到原 type‑4 负二
Newton 端点，并由(16)–(17)控制该 theta 来源的整个合法正权。**
完整图类与原单位 signed 坐标的全精度等式、或由原 canonical
必要行迫这个端点为零，仍须保原连接／伴随费用继续证明。
不能把此处 HT 差三的类当成已有 rank2 椭圆曲线的 usual Selmer 类。

## 7. 与已付原 $p^2$ 全 norm 的相容性

[原惰性 $p^2$ note](2026-11-27-original-inert-p-square-full-norm-and-endpoint-zero.md)
已在同一个 Coleman 对象及全部原54权下证明
$$
p^{-2}\operatorname{AJ}(Z_{j,p^2})=I_{j,p},
\qquad
a_{j,p}^{-1}p^{-2}\operatorname{AJ}(Z_{j,p^2})=h_{j,p}.
\tag{33}
$$
其中原未平均 cyclic $p^2$ norm 为 $p(p+1)$，
而 depleted 的完整 imprimitive norm 恰为零。
本文(22)读取的正是(33)最后的原整参数，
没有另把 primitive $p$-conductor 定理用在 imprimitive 角色上。

因此先作原 raw norm、再除显示 $p^2$、再取首层，
与直接作(22)相同。它不需要对 $p^{\text{weight}}$ 形式微分，
也不把仅在所有高导子角色相同的两个 order-one 分布
自动认作同一 bounded signed 测度。

## 原始依据

- [R806](../results/R806-original-type-four-order-eighteen-and-negative-two-katz.md)，§§1–6：全部十八阶有限角色、原 Schwartz／Haar、固定 $c_j$、degree34 来源、全权平方及17缩放。
- [R301](../results/R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)，§§2–6：原高度二形式对数、准确 $pc_\sigma$、完整 Gauss 圆盘和 Newton 尾。
- [R887](../results/R887-original-z-all-cm-transport-and-exact-hasse-normalization.md)，§§7、11、19：原 $F_p$、$\rho_pc_p=1$、原 $x_{p-1}=c_p$。本文不另改其 $Z$。
- [R1049](../results/R1049-original-inert-syntomic-graphs-and-crystalline-lattice.md)，§§11–14：原 Manin 低行、全部54 toric 权、经典平方、杯积与 crystalline 定标。
- [R804](../results/R804-original-order-eighteen-soule-classes-and-negative-two-localization.md)，§2：同一全局单位、18分量与30平滑因子；其普通位标量公式不在惰性处照抄。
- [Burungale–Kobayashi–Nakamura–Ota, 2508.17776v1](https://arxiv.org/html/2508.17776v1)，Theorem 3.1、Corollary 3.2、Lemma G.22、Theorems G.25/G.29、Corollary G.32：完整高权整 signed 分解、base change 和准确 epsilon。
- [R303](../results/R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)，§4：两条 Kato CM tensor 特化路径的已付逐式比较。本文只复用该互反律路径，不复用 HT$(1,0)$ 的 signed 符号或其通常椭圆 Selmer 结论。

本注没有运行新的数学计算或扫描。
