# R174：指定尖点型行的范数核与同一三色 Fourier 函数

日期：2026-11-13。

**状态：已证明的逐列有限群恒等式及必要共同零条件。** 本文把 R169/R173 的指定尖点型整行直接写成旧三色 Fourier 函数的范数二次曲线加权和。全部公式使用一个固定实际尖点、一个固定加性角色及一个固定剩余嵌入；没有对频率取平均，也没有移动素理想。

有限群恒等式本身不需要中心值假设。将它用于实际分母时，仍须有 R172/R173 的至少一个实际尖点型中心值非零；若同时要求旧三色行消失，还须有 R69/R72 的实际有限三次 Steinberg 商。本文没有从正根数推出非零中心值，也没有证明下面的新旧共同理想总为单位。

## 1. 同一 Cartan 模型和三色函数

设 $p>37$，处于 R166 的实际小惯性分支，写
$$p+1=3d,\qquad 3\nmid d,\qquad d>4.$$
取 $z\in\mathbb F_p^\times$ 非平方，令
$$k=\mathbb F_{p^2}=\mathbb F_p(\tau),\qquad\tau^2=z,
\qquad \operatorname{Tr}(x+y\tau)=2x,
\qquad N(x+y\tau)=x^2-zy^2.$$
在 R169 的同一有限群坐标中，使用
$$
c_t=\begin{pmatrix}t&z\\1&t\end{pmatrix}\quad(t\in\mathbb F_p),
\qquad c_\infty=1,
\qquad
\overline C=\{c_t:t\in\mathbb F_p\cup\{\infty\}\}.
\tag{174.1}
$$
$c_t$ 对应 $k^\times/\mathbb F_p^\times$ 中的 $t+\tau$。仍记
$$u_x=\begin{pmatrix}1&x\\0&1\end{pmatrix},\qquad
 d_s=\begin{pmatrix}s&0\\0&1\end{pmatrix},\qquad
 w_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$
$\psi$ 和 $a\in\mathbb F_p^\times$ 是这个实际尖点已经固定的角色和频率。

令 $\vartheta:k^\times/\mathbb F_p^\times\to\mu_3$ 非平凡，定义
$$
S_\epsilon(y)=\sum_{t\in\mathbb F_p}
\vartheta(t+\tau)^\epsilon\psi(ty),
\qquad \epsilon=1,-1,\ y\in\mathbb F_p.
\tag{174.2}
$$
这就是同一个 Cartan 的两个三色 Fourier 和。准确地，在 $\mathbb P^1$ 的置换模型中，$c_t$ 将 $\infty$ 送到 $t$，$\vartheta$ 角色向量的 $t$ 坐标为 $\vartheta(t+\tau)^{-1}$；其 $\psi(a\cdot)$ Fourier 系数为 $S_{-1}(a)$，逆角色的为 $S_1(a)$。

若旧笔记采用 $\vartheta(1+b\tau)$，则 $\vartheta(\tau)=1$，因为 $\tau^2\in\mathbb F_p^\times$ 而 $\vartheta$ 阶三。因此
$$\vartheta(t+\tau)=\vartheta(1+(t/z)\tau),$$
所以两套书写满足 $S_\epsilon(y)=S^{\rm old}_\epsilon(zy)$。这只是固定模型之间的已知坐标换算，不是自由更换实际频率。

置
$$H=\overline C^3,\qquad
T_H=\{t\in\mathbb F_p:c_t\in H\},
\qquad A_H(y)=\sum_{t\in T_H}\psi(ty).\tag{174.3}$$
$|T_H|=d-1$，因为 $c_\infty\in H$。三色指示函数给精确公式
$$
\boxed{3A_H(y)=p\,1_{y=0}+S_1(y)+S_{-1}(y).}
\tag{174.4}
$$
这里的完整仿射和为 $\sum_{t\in\mathbb F_p}\psi(ty)=p1_{y=0}$；不能误用 $\mathbb F_p^\times$ 的 $-1$ 项。

又 $S_\epsilon(0)=-1$。由于 $\overline{t+\tau}=t-\tau$ 与 $-t+\tau$ 只差一个标量，
$$S_{-1}(y)=S_1(-y).\tag{174.5}$$
于是旧两行共同零严格给 $A_H(a)=A_H(-a)=0$。

## 2. 完整的指定行核

取阶为 $d$ 的 $\theta$，以及 R169 的矩阵行 $\mathcal B_{\theta,\theta\vartheta^\epsilon}(a,b)$。$\theta$ 和 $\vartheta$ 都在 $\mathbb F_p^\times$ 上平凡。

**定理 174.1。** 对每个 $a,b\in\mathbb F_p^\times$ 和 $\epsilon=\pm1$，有
$$
\boxed{
\begin{aligned}
p(p+1)\,\mathcal B_{\theta,\theta\vartheta^\epsilon}(a,b)
={}&p\,1_{a=b}\\
&-\sum_{\substack{\gamma\in k^\times\\N\gamma=ab}}
\theta(\gamma)\,
\psi\bigl(-\operatorname{Tr}(\tau\gamma)\bigr)
S_{-\epsilon}\!\left(\frac{N(\gamma-a)}a\right).
\end{aligned}}
\tag{174.6}
$$
相应的 $H$ 等型合并行满足
$$
\boxed{
\begin{aligned}
pd\,\mathcal C_\theta(a,b)
={}&p\,1_{a=b}\\
&-\sum_{\substack{\gamma\in k^\times\\N\gamma=ab}}
\theta(\gamma)\,
\psi\bigl(-\operatorname{Tr}(\tau\gamma)\bigr)
A_H\!\left(\frac{N(\gamma-a)}a\right).
\end{aligned}}
\tag{174.7}
$$
所有和都在 R169 的有限圆分整数环局部化中成立；在任何 $\ell\nmid p(p^2-1)$ 的指定剩余嵌入下仍成立。

关键的代数恒等式为
$$
\boxed{a+b-\operatorname{Tr}\gamma
=\frac{N(\gamma-a)}a\quad(N\gamma=ab).}
\tag{174.8}
$$
因为 $k$ 是域，右边为零当且仅当 $\gamma=a$；这又迫使 $b=a$。这一个退化点须保留，不能当成一般非零 Fourier 参数处理。

## 3. 由特征标表直接得到 Weyl 核

使用 R169 的整 Kirillov 基 $v_b$，它满足
$$R_\theta(u_x)v_b=\psi(bx)v_b,
\qquad R_\theta(d_s)v_b=v_{b/s}.$$
记 $W_\theta(r,b)$ 为 $R_\theta(w_0)$ 的 $(r,b)$ 矩阵元。则
$$
\boxed{W_\theta(r,b)
=-\frac1p\sum_{N\beta=rb}
\theta(\beta)\psi(-\operatorname{Tr}\beta).}
\tag{174.9}
$$

**证明。** 有
$$d_s w_0 u_x=\begin{pmatrix}0&-s\\1&x\end{pmatrix},$$
其行列式为 $s$、迹为 $x$。由基的两个变换律，
$$\operatorname{Tr}R_\theta(d_s w_0u_x)
=\sum_{b\ne0}\psi(bx)W_\theta(sb,b).$$
对 $x$ 作精确加性 Fourier 反演。R169 的特征标表使右边对应的和为
$$
W_\theta(sb,b)
=-\frac1p\sum_{N\alpha=s}
\theta(\alpha)\psi(-b\operatorname{Tr}\alpha).
$$
非分裂正则元的两个共轭特征值各贡献一次；若判别式为零，则 $\alpha\in\mathbb F_p^\times$，$\theta(\alpha)=1$，恰给非平凡幺幂元特征标 $-1$。分裂正则元贡献零。令 $\beta=b\alpha$，则 $N\beta=b^2s$、$\theta(\beta)=\theta(\alpha)$，得到 (174.9)。证毕。

这从已核特征标表固定了 Weyl 核的符号和 $p^{-1}$；不引用一个可能采用另一 Whittaker 规范的 Bessel 公式。

## 4. Bruhat 分解与权的准确消去

在同一模型中逐矩阵相乘得
$$\boxed{c_t=u_t d_{t^2-z}w_0u_t.}\tag{174.10}$$
由 (174.9)，
$$
R_\theta(c_t)_{a,b}
=-\frac1p\psi(t(a+b))
\sum_{N\beta=ab(t^2-z)}
\theta(\beta)\psi(-\operatorname{Tr}\beta).
\tag{174.11}
$$
注意 $d_{t^2-z}$ 将 Weyl 矩阵的行 $a$ 改为 $a(t^2-z)$，故范数是 $ab(t^2-z)$，不是它的倒数。

在每个内和令
$$\beta=(t+\tau)\gamma.$$
这给 $N\gamma=ab$，并有
$$\operatorname{Tr}\beta=t\operatorname{Tr}\gamma+
\operatorname{Tr}(\tau\gamma).$$
对于 $\varphi=\theta\vartheta^\epsilon$，Cartan 投影权精确抵消为
$$
\varphi(t+\tau)^{-1}\theta(\beta)
=\vartheta(t+\tau)^{-\epsilon}\theta(\gamma).
\tag{174.12}
$$
对全部 $t\in\mathbb F_p$ 求和即给 $S_{-\epsilon}(a+b-\operatorname{Tr}\gamma)$；$c_\infty=1$ 贡献 $p1_{a=b}$。这证明 (174.6)，再由 (174.8) 得所写范数参数。

若只对 $t\in T_H$ 求和并用 $H$ 的 $\theta$ 权，则没有三次剩余权，直接给 $A_H$，证明 (174.7)。

还有一个独立的归一化核对：将 (174.6) 的两个 $\epsilon$ 相加，使用 R173 的 $\mathcal C_\theta=\mathcal B_++\mathcal B_-$ 以及 (174.4)。$S_1+S_{-1}=3A_H-p1_{y=0}$ 中最后一项只在 $\gamma=a,b=a$ 出现，贡献额外 $p1_{a=b}$；于是两个 $p1_{a=b}$ 正好合成 (174.7) 所需的三个，而分母 $p(p+1)=3pd$ 同时消去。这也解释了为何遗漏退化点会导致主项系数错误。

## 5. 同一实际分母必须满足的全行系统

若 R172 的一个实际中心值非零，R173 给整个原始 $\theta^u$ 族及两个三次方向的实际有限商微分。因此实际分母在固定的同一剩余嵌入下必须满足，对每个 $(u,d)=1$、$b\ne0$、$\epsilon=\pm1$，
$$
\sum_{N\gamma=ab}\theta(\gamma)^u
\psi(-\operatorname{Tr}(\tau\gamma))
S_{-\epsilon}\!\left(\frac{N(\gamma-a)}a\right)
=p\,1_{a=b}.
\tag{174.13}
$$
等价地，可以使用 (174.7) 的 $A_H$ 系统和 R173 的整理想等式。

若旧 Steinberg 商也已证明有限，另有 $S_1(a)=S_{-1}(a)=0$。这不是把 (174.13) 中所有参数都换成 $a$：范数曲线上的 $N(\gamma-a)/a$ 会遍历许多不同参数。因而一个旧指定零点并不直接使新核全为零，也不能直接从某个其他参数非零推出指定行非零；必须保留完整加权和。

这些等式只使用实际商中的整微分。反向仍不成立：即使所有所构造行都消失，其他新形式间的整同余可能使整个最优商仍形式浸入。

## 6. 固定范数上的 Mellin 信息，以及二次 twist 的准确边界

令
$$m=d/2=(p+1)/6,\qquad U_1=\{\nu\in k^\times:N\nu=1\}.$$
$U_1$ 阶为 $p+1=6m$。若 $g$ 生成 $k^\times$，则 $g^{p-1}$ 生成 $U_1$，而
$$\theta(g^{p-1})=\theta(g)^{-2}.$$
因此
$$
\boxed{\operatorname{ord}(\theta|_{U_1})=m,
\qquad\ker(\theta|_{U_1})=\mu_6.}
\tag{174.14}
$$
当 $u$ 遍历 $(\mathbb Z/d\mathbb Z)^\times$ 时，$\theta^u|_{U_1}$ 恰遍历 $U_1/\mu_6$ 的全部原始阶 $m$ 字符，可能有重复。不能将它误当阶 $d$ 的全部字符。

对给定 $a,b$，任选 $w_{a,b}$ 满足 $Nw_{a,b}=ab$；在 $b=a$ 时取 $w_{a,a}=a$。对函数 $G(y)$（可取 $S_{\pm1}$ 或 $A_H$），定义 $U_1/\mu_6$ 上的六点和
$$
F^{G}_{a,b}(\bar\nu)=
\sum_{\kappa\in\mu_6}
\psi\bigl(-\operatorname{Tr}(\tau w_{a,b}\nu\kappa)\bigr)
G\!\left(\frac{N(w_{a,b}\nu\kappa-a)}a\right).
\tag{174.15}
$$
于是全部原始 $\theta$ 的全行消失等价于
$$
\sum_{\bar\nu\in U_1/\mu_6}
\chi(\bar\nu)
\bigl(F^G_{a,b}(\bar\nu)-p1_{a=b}1_{\bar\nu=1}\bigr)=0
\tag{174.16}
$$
对该循环群的所有原始阶 $m$ 字符 $\chi$ 成立。$b\ne a$ 时，提出的非零因子 $\theta^u(w_{a,b})$ 对右边零无影响；$b=a$ 时它等于一。

这给了一个无隐藏取向的有限 Mellin 投影形式。例如可用整数 Ramanujan 和 $c_m(j)$ 写其原始幂等元
$$e_m^{\rm prim}=\frac1m\sum_{j=0}^{m-1}c_m(j)[\bar\nu]^j.$$
(174.16) 正是对应函数的原始投影为零。因为 $m$ 在实际 $\ell$ 处为单位，该表述整且可约化。

### 6.1 二次 twist 只乘列单位

令
$$\delta(\gamma)=\left(\frac{N\gamma}{p}\right),
\qquad \theta'=\theta\delta,
\qquad\varphi'=\varphi\delta.$$
这是二次行列式 twist。在范数壳 $N\gamma=ab$ 上，$\delta(\gamma)=(ab/p)$ 固定，且 $a=b$ 时该值为一。所以 (174.6)–(174.7) 立即给
$$
\boxed{
\mathcal B_{\theta',\varphi'}(a,b)
=\left(\frac{ab}{p}\right)\mathcal B_{\theta,\varphi}(a,b),
\qquad
\mathcal C_{\theta'}(a,b)
=\left(\frac{ab}{p}\right)\mathcal C_\theta(a,b).}
\tag{174.17}
$$
因此 R166 的 Dirichlet twist 取消即使提供这些额外有限类型，也只给同一个指定行理想。

$p\equiv1\pmod4$ 时，$d$ 的二部恰为二，$\theta'$ 的阶会从 $d$ 变为 $d/2$；它在 $U_1$ 上的限制却本来与 $\theta$ 一样。$p\equiv3\pmod4$ 时，$\theta'$ 仍为原始阶 $d$。两种情形都不能靠这个 twist 补出独立的 Mellin 字符条件。

## 7. 一个完整 Mellin 特例：$m=(p+1)/6$ 为素数

这个特例不给非消失结论，但把必要条件进一步写成完整的逐点等式。

**推论 174.2。** 若 $m$ 为素数，并且旧三色行及 R173 的全部原始尖点型行在同一剩余嵌入下都消失，则对每个 $w\in k$ 有
$$
\boxed{
\sum_{\kappa\in\mu_6}
\psi(-\operatorname{Tr}(\tau w\kappa))
A_H\!\left(\frac{N(w\kappa-a)}a\right)
=p\,1_{w\in a\mu_6}.}
\tag{174.18}
$$

**证明。** 此时 $d=2m$。阶整除 $d$ 的 Cartan 字符除 $1,\delta$ 外，阶为 $m$ 或 $2m$。原始阶 $2m$ 由 R173 提供；阶 $m$ 的核消失由 (174.17) 得到。因此只需核准两个退化字符。

将特征标公式形式上延拓到 $\theta=1,\delta$，分别得到虚表示
$$R_1=\mathrm{St}-1,\qquad R_\delta=\mathrm{St}\otimes\delta-\delta.$$
非平凡 $U$ 投影 $P_a$ 杀掉两个一维项，所以本文的指定行迹公式恰为相应真实 Steinberg 表示的指定行。$\mathrm{St}|_{\overline C}=\operatorname{Reg}_{\overline C}-1$，其 $H$ 不变部分正是 $\vartheta,\vartheta^{-1}$ 两条线；旧三色共同零使它的指定行全为零。二次 twist 同样成立。

(174.9) 的反演对此也有效：非平凡 Fourier 频率杀掉虚表示中的一维项；Bruhat 分解只使用一次 Weyl 算子，左右的 $U,D$ 保持非平凡 $U$ 子空间。因此 (174.7) 对这两个退化字符仍给正确的行迹，没有把虚表示误当成一个闭合的 $p-1$ 维实际表示。

由此 $U_1/\mu_6$ 的全部 $m$ 个字符都有 (174.16)，包含常数字符。完整有限 Fourier 反演给 $F^{A_H}_{a,b}=p1_{a=b}\delta_1$。令 $b=Nw/a$ 即得所有 $w\ne0$ 的 (174.18)。在 $w=0$ 时左边为 $6A_H(a)=0$，由旧共同零，右边也为零。证毕。

对复合 $m$，仅原始字符与常数字符不一定覆盖全部字符；不能直接作这最后一步完整反演。

即使在本推论的范围，(174.18) 仍是要排除的精确函数等式，而不是已经得到的矛盾。对其作简单求和或 Fourier 变换，会再次产生旧颜色恒等式；不能据此声称完成固定频率非零。

## 8. 精确归一化证书与范围

标准库核验器 `verify_cuspidal_cayley_kernel.py` 使用一个固定模型 $p=41,z=3$ 和一个分裂系数域 $\mathbb F_{1723}$，独立比较：

- R169 特征标双和定义；
- 本文的范数二次曲线核。

只用 $a=1,7$、$\theta$ 指数 $1,3,5$，核完 $240$ 个合并行元与 $480$ 个单独行元。所有运算为整数模素数运算；它只检查符号、逆元、分母、退化点和同一模型归一化。完整一般证明在 §§3–4，不依赖这有限核验。证书 `cuspidal_cayley_kernel_certificate.json` 没有单位性或异常素数搜索结论。

另以先前已保存的 $p=41,\ell=12547$ 单侧 Fourier 零点检查一个容易误猜的因子化：在 $\tau^2=-3$ 模型、同一旧根 $\psi(1)=1692$、$\vartheta$ 根 $6217$ 下，旧 $a_{\rm old}=21$ 对应这里 $a=34$，有 $S_1(34)=0$、$S_{-1}(34)=4541$。取 $k^\times$ 的生成元 $1+2\tau$ 并令 $\theta(1+2\tau)=T$，在 $\mathbb F_{12547}[T]/\Phi_{14}(T)$ 中，相应
$$p(p+1)\mathcal B_{\theta,\theta\vartheta^{-1}}(34,34)
=4064+6166T+5603T^2+4642T^3+2097T^4+9928T^5\ne0.$$
这里 $12547$ 模 $14$ 的阶为六，故 $\Phi_{14}$ 不可约；非零六维系数确证任一该原始角色嵌入处的非零。核验器 `verify_cuspidal_single_zero_nonfactorization.py` 与证书 `cuspidal_kernel_single_zero_certificate.json` 只复用了这一旧零点。因此不能把整个新行当成旧单个 $S_1(34)$ 的整标量倍数。这只否证该简化猜测；没有构造旧两行共同零，也没有扩大实际异常素数窗口。

本文提供的真正新输入是 (174.6)–(174.8) 的**指定频率逐列**连接及 (174.14) 的准确 Mellin 字符范围。剩余工作是排除这些完整加权和在实际剩余特征下的共同零，或者证明至少一个可用实际中心值非零；二者都不能由本篇的有限核验代替。

## 9. 输入定位

全部新增恒等式由以下已经证明的实际输入和本文的有限 Fourier/Bruhat 运算推出：

- [R169](R169-cuspidal-whittaker-lattices-and-the-specified-cusp-row.md) §§4、6：饱和整 Kirillov 基、$U,D$ 变换律、有限特征标表与指定行迹公式。
- [R173](R173-rational-cuspidal-orbits-and-cube-subgroup-row-ideals.md) §§2–5：一个有限有理投影像中的全部原始 $\theta$ 共轭、两个三次方向、精确 $H$ 合并整理想。
- [R172](R172-cuspidal-central-values-and-actual-rank-zero-quotients.md)：非零中心值到实际商有限的已发表一般新形式接口及中央域 Kummer 拼接。
- [R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：同一实际尖点和原始根的旧三色行及形式浸入分母论证。

没有从一个存在的单位频率换成指定频率，没有使用未发表的全称整性结论。
