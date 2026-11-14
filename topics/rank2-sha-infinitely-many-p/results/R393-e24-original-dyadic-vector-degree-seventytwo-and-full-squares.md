# R393 — E24 的原二处向量、真实 degree72 来源与完整全权平方

日期：2026-11-14。**状态：以下原 conductor-eight 二处 Schwartz、
全局有理支撑、真实周期与 half-period、degree72 全纯来源、实际全权
平方常数均已证明。它们属于同一条固定秩至少二曲线 $E_{24}$。
没有由来源存在或两个坏点范数为单位推出原 p-adic 中央非消失；
全 Selmer 的无穷素数目标仍未完成。**

接 [R389](R389-e24-primitive-wild-local-data-and-actual-hermitian-class.md)
和 [R391](R391-e24-original-wild-three-schwartz-and-heisenberg-transport.md)。
固定
$$
E_{24}:y^2=x^3+24,\quad K=\mathbf Q(\delta),\quad
\delta=\sqrt{-3}=1+2\omega,\quad\operatorname{Im}\delta>0,\quad\alpha=1.
\tag{1}
$$
沿用原负有限加性角色、同一 CM type 和 Yang 极化 $X=\mathbf Q\delta$。

## 1. 二处真正的生成元与原 splitting

令
$$
g_2=\frac{1+2\delta}{1-2\delta}=\frac{-11+4\delta}{13}.
\tag{2}
$$
$K_2^1$ 由 $-1,\omega,g_2$ 拓扑生成。
事实上 $\mu_3$ 给模二的全部单位，模四的 norm-one 条件再留下
$\pm1$；余下的 $1+4\mathcal O_{K_2}$ 经对数为 $4\delta\mathbf Z_2$。
而
$$
\log g_2=4\delta(1-4+144/5-\cdots)
$$
的括号为二进单位，故它的幂在此对数格中稠密。

令 $\psi_2(t)=e^{-2\pi i\{t\}_2}$，并记 $W_g=\omega_{1,\chi_{24,2}}(g)$。
原嵌入及 splitting 是
$$
\iota(x+y\delta)=
\begin{pmatrix}x&9y\\-y/3&x\end{pmatrix},
$$
$$
W_g=\mu(g)r_S(\iota(g)),\quad
\mu(g)=\chi_{24,2}(\delta(g-1))
 \gamma_2(y(1-x)\psi_2)(-3,-2y(1-x))_2 .
\tag{3}
$$
写 $\zeta_8=e^{\pi i/4}$，R389 的完整角色给
$$
\boxed{
\mu(\omega)=-\omega^2\zeta_8,\qquad
\mu(\omega^2)=-\omega\zeta_8^{-1},\qquad
\mu(g_2)=\zeta_8.
}
\tag{4}
$$

这里逐项支付最后一个新符号。
$$
\delta(g_2-1)=-\frac{12}{13}(1+2\delta).
$$
它的基 Teichmüller/偶 uniformizer 值为一，二次扭曲值为
$(-2/13)=-1$。又 $y(1-x)=96/169$ 的二进 valuation 为五，
Weil 指数为 $\zeta_8^{-3}$；Hilbert 因子为一。
故 $\mu(g_2)=-\zeta_8^{-3}=\zeta_8$。

对 $\omega$ 和 $\omega^2$，$\delta(g-1)$ 分别为
$3\omega^2,-3\omega$，二次扭曲均为一；
两个 Weil 指数分别为 $\zeta_8,\zeta_8^{-1}$，Hilbert 因子均为负。
这证明 (4)。同一计算给 $\mu(-\omega)=\mu(\omega)$，
从原 Fourier 核得到
$$W_{-1}\phi(u)=\phi(-u).$$
因此这里也没有未付的 projective scalar。

## 2. 从一个实际球构造整个二处向量

设 $h=\mathbf1_{\mathbf Z_2}$，自对偶测度取
$\operatorname{vol}(\mathbf Z_2)=1$。
先完整计算 $W_{g_2}h$。
原 Rao 核的相位为
$$
\frac{33u^2+78uv+33v^2}{8},
$$
外部绝对值因子为二。
若 $u\notin\mathbf Z_2$，在积分内作 $v\mapsto v+4$，
会乘非平凡角色 $\psi_2(39u)$，所以积分为零。
若 $u\in\mathbf Z_2$，模八的二次式恰为 $(v+3u)^2$，故
$$
\int_{\mathbf Z_2}
 \psi_2((33u^2+78uv+33v^2)/8)\,dv
 =\frac18\sum_{v\bmod8}\zeta_8^{-v^2}
 =\frac{\zeta_8^{-1}}2.
$$
由 (4)，准确有
$$\boxed{W_{g_2}h=h.}\tag{5}$$

现在定义
$$
\boxed{\phi_2=(I+W_\omega+W_{\omega^2})h.}
\tag{6}
$$
这是原表示中的真实三项，不是另取一个同次数多项式。
因为 $W_\omega^3=I$，(6) 被 $W_\omega$ 固定；
环面可交换及 (5) 证明它也被 $W_{g_2}$ 固定；
$h$ 偶而 $W_{-1}$ 与各项交换，所以它被 $W_{-1}$ 固定。
§1 的拓扑生成元遂证明它是整个二处原不变向量。

### 2.1 全部支撑与十六个系数

对 $\omega$，原 Fourier 核为
$$
\frac1{\sqrt2}\psi_2\!\left(\frac32(u^2+4uv+v^2)\right).
$$
在 $v\in\mathbf Z_2$ 上，
$\psi_2(3v^2/2)=\psi_2(3v/2)$。
所以积分非零的准确条件为
$3/2+6u\in\mathbf Z_2$，即 $u\in\frac14+\frac12\mathbf Z_2$。
写 $u=a/4$、$a$ 为奇数，代入 (4)，得到
$$
W_\omega h(a/4)=-\frac{\omega^2}{\sqrt2}\zeta_{32}^{a^2},
\qquad
W_{\omega^2}h(a/4)=-\frac{\omega}{\sqrt2}\zeta_{32}^{-a^2}.
$$
其中 $\zeta_{32}=e^{2\pi i/32}$；
使用的是 $4-3a^2\equiv a^2\pmod{32}$，不是删除 Gaussian 相位。

故 $\phi_2$ 以 $4\mathbf Z_2$ 为周期，支撑在 $\frac14\mathbf Z_2$，
准确系数为
$$
\boxed{
v_2(a)=\phi_2(a/4)=
\begin{cases}
1,&a\equiv0\pmod4,\\
0,&a\equiv2\pmod4,\\
-\bigl(\omega^2\zeta_{32}^{a^2}
       +\omega\zeta_{32}^{-a^2}\bigr)/\sqrt2,&a\text{ 奇}.
\end{cases}}
\tag{7}
$$
$a$ 按模十六读取。全部系数实且偶，并满足
$$
\boxed{v_2(a+8)=(-1)^a v_2(a).}
\tag{8}
$$
没有声称所有 $\mathcal S(\frac14\mathbf Z_2/4\mathbf Z_2)$
都被原环面稳定；本篇只用 (6) 的实际三项及已付生成元。

### 2.2 原范数

$h$ 的支撑与 $W_\omega h,W_{\omega^2}h$ 的支撑不相交。
原表示酉且 $W_{\omega^2}=W_\omega^*$，故
$$
\boxed{\|\phi_2\|^2=3.}
\tag{9}
$$
也可由 (7) 直接求和：四个整数陪集贡献四，
八个奇陪集的平方和为八，每个陪集体积 $1/4$，
总数仍为三。

## 3. 合并三处后的完整原有理来源

令 $\zeta=\zeta_9$，并保持 R391 的三个真实实系数
$$
f_1=3+\delta(\zeta-\zeta^8),\quad
f_2=-\delta(\zeta^5-\zeta^4),\quad
f_4=\delta(\zeta-\zeta^8).
$$
定义模九函数
$$
v_3(a)=
\begin{cases}
0,&3\mid a,\\
f_1,&a=\pm1,\\
f_2,&a=\pm2,\\
f_4,&a=\pm4.
\end{cases}
\tag{10}
$$
R391 已证明 $\phi_3(x)=v_3(9x\bmod9)$，支撑
$3^{-2}\mathbf Z_3^\times$，且
$$\|\phi_3\|^2=18f_1.$$

其余有限点取原标准球 $\mathbf1_{\mathbf Z_\ell}$。
因此整个原有理支撑为 $x=n/36$，并准确有
$$
\boxed{
a_n=v_2(9n\bmod16)\,v_3(7n\bmod9).
}
\tag{11}
$$
这里 $4x=n/9$ 在二处使用 $9^{-1}\equiv9\pmod{16}$；
$9x=n/4$ 在三处使用 $4^{-1}\equiv7\pmod9$。
这两个逆元不能直接改成一。

(7)–(11) 给
$$
\boxed{
a_{n+144}=a_n=a_{-n}=\overline{a_n},\qquad
a_{n+72}=(-1)^n a_n.
}
\tag{12}
$$
$a_n=0$ 若 $3\mid n$ 或 $n\equiv2\pmod4$。
例如 $a_4=f_1\ne0$，所以整个来源并不恒零。

所有有限系数在固定域 $\mathbf Q(\zeta_{288})$ 中，
分母仅涉及二。三处范数中的 $f_1$ 满足准确式
$$
\boxed{f_1^3-9f_1^2+18f_1-9=0,\qquad
N_{\mathbf Q(\zeta_9)^+/\mathbf Q}(f_1)=9.}
\tag{13}
$$
在 $1,\zeta,\ldots,\zeta^5$ 基中直接约简即可证明；
该三次式无有理根，因此是最小多项式。
所以 $f_1$ 在每个 $p>3$ 的嵌入中都是单位。
这只支付固定原归一常数，没有推断目标中央量为单位。

## 4. 全 Hermite 来源和唯一的 Gaussian 尺度

置
$$
\kappa=3\sqrt3.
$$
用 Yang 的原 Hermite 规范
$$
\sum_{m\ge0}H_m(X)\frac{T^m}{m!}
 =\exp(XT-T^2/(8\pi)).
$$
原系数准确为
$$
\boxed{
b_m=\sum_{n\in\mathbf Z}a_n
 H_m\!\left(\frac{\sqrt\kappa\,n}{36}\right)
 e^{-\pi\sqrt3\,n^2/432}.
}
\tag{14}
$$
它们都是实数。由有理单位 $-1,\omega$ 的整个 Weil 作用保持
theta 求和、各有限原向量均不变，而无限 Hermite 第 $m$ 型
的相应特征是 $(-1)^m,\omega^{\pm m}$，得到
$$
\boxed{b_m=0\quad\text{若 }6\nmid m.}
\tag{15}
$$
这不是据有限阶数值近零作出的断言。

令
$$
\tau_0=\delta/3,\qquad
F(Z)=\sum_n a_n e^{\pi i\tau_0 n^2/144+2\pi inZ}.
$$
则整个生成函数为
$$
\boxed{
\mathcal B(T)=\sum b_m\frac{T^m}{m!}
 =e^{-T^2/(8\pi)}
 F\!\left(\frac{\sqrt\kappa}{72\pi i}T\right).
}
\tag{16}
$$
这保留了 $36$、$144$、Gaussian 和实际 Fourier 变量，
未把它们从旧 $D_{16}$ 的来源借来。

## 5. 原 half-period 的完整下降：次数恰为七十二

令
$$
s=\frac{1+\tau_0}{2},\qquad
\Lambda=\mathbf Z+s\mathbf Z .
$$
由 (12) 重新编号 $n\mapsto n+72$，准确得到
$$
F(Z+1)=F(Z),\qquad
F(Z+s)=e^{-\pi i72s-2\pi i72Z}F(Z).
\tag{17}
$$
特别半周期常数为正一，与 $72/2=36$ 的偶性相合，
没有留下非平凡 flat characteristic。

在同一最大整环格 $\Lambda$ 上，原 quasi-period 为
$\eta_1=2\sqrt3\pi$。因此
$$
\boxed{
S_{24,\Lambda}(Z)=e^{72\sqrt3\pi Z^2}F(Z)
 \in H^0(\Lambda,\mathcal O(72O)).
}
\tag{18}
$$
这是实际 degree72 来源。把
$c=\sqrt\kappa/(72\pi i)$ 代入，有
$72\sqrt3\pi c^2=-1/(8\pi)$，所以
$$
\boxed{\mathcal B(T)=S_{24,\Lambda}(cT).}
\tag{19}
$$
(18)–(19) 的 Gaussian 恰好相合。

偶性、三次单位不变性给出的完整位置为
$$
S_{24,\Lambda}(Z)
 =\sigma_\Lambda(Z)^{72}
   P_{12}\!\left(\wp_\Lambda(Z)^3\right),
\qquad \deg P_{12}\le12.
\tag{20}
$$
证明是除以 $\sigma^{72}$ 后只有原点至多七十二阶极，
偶性给 $\wp$ 的至多三十六次多项式；
$\mu_3$ 再要求指数为三的倍数。
这里 $P_{12}$ 已由 (7)、(10)、(11) 唯一指定，不是任意环境来源。

若 $\Omega_{24}\Lambda$ 是 $E_{24}$ 对微分 $dx/(2y)$ 的实际周期格，
原曲线变量准确是 $z=\Omega_{24}Z$。
与同一方向的 $E_{17}:y^2=x^3+17$ 周期比较，
$$
\boxed{\Omega_{24}=(17/24)^{1/6}\Omega_{17}.}
\tag{21}
$$
它来自两曲线实际同态 $(x,y)\mapsto(\theta^2x,\theta^3y)$、
$\theta=(24/17)^{1/6}>0$；不变微分乘 $\theta^{-1}$。
后续正式群/中央测度比较必须保持这个尺度；
(21) 本身没有把两个原 Hecke 角色或原测度相认。

## 6. 固定全权角色及完整平方常数

R389 已证明，对 $m\equiv0\pmod6$，
$\chi_{24}^{\,2m+1}$ 的两个坏点完整角色保持不变，
Hermitian 类仍为 $\alpha=1$。
好分裂点未分歧参数虽变化，Yang Corollary 2.14 的标准球仍适用。
因此 (14) 的同一个原有限来源给所有这些权。

全部有限范数是 $3\cdot18f_1=54f_1$。
无限 Hermite 的准确范数为
$$
\|\phi_\infty^{(m)}\|^2
 =\frac1{\sqrt{6\sqrt3}}\frac{m!}{(4\pi)^m}.
$$
故完整原范数为
$$
\mathcal N_m=
 \frac{54f_1}{\sqrt{6\sqrt3}}\frac{m!}{(4\pi)^m}.
\tag{22}
$$

Yang 1997 Theorem 1.11 的 $S_1$ 是未分歧二次但角色分歧的地方：
本处准确为 $\{2\}$。三处扩张本身分歧，所以不属于 $S_1$，
即使角色有 conductor 四，也不能再添一个 $3$ 因子。
没有坏分裂点，故
$$
\boxed{c(0)=(1+2^{-1})^{-1}=2/3.}
\tag{23}
$$
该定理对 $S_1$ 的因子不随角色 conductor exponent 改变；
其原证明的 nonsplit 分支覆盖这里的野角色。

$h_K=1$，与全局 norm-one 有理元素约去好分裂处赋值后，
紧子群与 $K^1$ 的交准确为 $\mu_6$。
因此原紧子群体积乘积与商体积之比为六，
不留下未付的 ideal-class 求和。
由 Yang (2.19)、Theorems 2.6、2.15，取规范化向量
$\phi/\sqrt{\mathcal N_m}$，并用
$L(1,\epsilon_{K/\mathbf Q})=\pi/(3\sqrt3)$，得到
$$
L(\psi_{24}^{2m+1},m+1)
 =\frac{2}{6c(0)}\,\frac{\pi}{3\sqrt3}\,
   \frac{b_m^2}{\mathcal N_m}.
$$
所以完整常数是
$$
\boxed{
L(\psi_{24}^{2m+1},m+1)
 =\frac{\pi\sqrt{6\sqrt3}}{324\sqrt3\,f_1}
   \frac{(4\pi)^m}{m!}\,b_m^2,
\qquad m\ge0,\ 6\mid m.
}
\tag{24}
$$
这是同一实来源的平方，所有 Gaussian、体积、范数和固定根均已保留。

## 7. 同一条秩至少二曲线及目前的边界

[R387 §9](R387-original-degree-sixteen-quartic-core-and-all-ordinary-moving-balls.md)
已自证 $E_{24}(\mathbf Q)$ 的秩至少二：
好约化五、七给无有理 torsion，
两个原有理点在十九处生成非循环 $C_9\times C_3$，
排除秩至多一。该证书不依赖 Sha。

已发表的 CM rank-zero 定理给
$L(E_{24},1)\ne0\Rightarrow\operatorname{rank}E_{24}(\mathbf Q)=0$。
因此 (24) 的 $m=0$ 准确推出 $b_0=0$。
结合 (15) 和 (20)，
$$
\boxed{
\operatorname{ord}_{Z=0}S_{24,\Lambda}\ge6,\qquad
S_{24,\Lambda}
 =\sigma_\Lambda^{72}P_{11}(\wp_\Lambda^3),\quad
\deg P_{11}\le11 .
}
\tag{25}
$$
没有在本篇断言六阶一定非零或凭近零数据删除更高项。
(11) 的非零 Fourier 系数则保证整条 $S_{24,\Lambda}$ 不恒零。

本篇现在给出了同一固定 $E_{24}$ 的真正 primitive 来源及全权
复平方公式，适用素数仍可沿用原普通素数族，并仅排除固定的坏素数。
要把它用于课题完成标准，还须支付该来源的原 p-adic 整格、
Euler/完整中央平方与全 Selmer 接口，以及真正跨 $p$ 非消失。
尤其旧 degree16 来源、其 norm-three 的 degree48 拉回，
都不是本篇已付的 degree72 原来源。

## 出处与同步

- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math.
  **485** (1997), 25–53，Theorem 1.11、Theorems 2.6、2.15、
  Corollary 2.14、(2.19)；
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
  本篇逐项计算其适用的 $S_1,S_2$、体积与原范数。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain
  elliptic curves*, Compositio Math. **117** (1999), 337–359，
  Lemma 1.1、Appendix (A1)–(A3)；
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
- K. Rubin, *Elliptic curves with complex multiplication and the conjecture
  of Birch and Swinnerton-Dyer*, Inventiones Mathematicae **64** (1981),
  455–470，Corollary 2.2。这里只用非零复中央值迫秩零的方向。
- R389、R391 及 R387 §9 分别提供原局部角色、完整三处向量与独立秩证书。

本篇固定有限计算与完整公式都在正文中给出，
没有以新增素数扫描承担跨 $p$ 推断。
提交前 API main 为 $66ec18eda6876a16a508acd91aced9494baf1beb$，
两份 README blob 与已读版本相同。
执行终端仍不可用，本篇按根规矩八用小文本 Contents API 提交，
不冒称本地 git pull。
