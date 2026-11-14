# R63. full Euler 分布、Cartier 与固定原函数连接

日期：2026-11-12。**状态：完整证明；附加中心斜率的全局作用仍待证明。**

使用 $E_{17}$ 上实际截面 $A=A_{17}$ 及整数 $h_m=A^{(m)}(0)$。
对普通目标素数 $p\ge13,p\ne17$，写
$\pi=\psi(\mathfrak p)$、$b=\bar\pi$、$a=\pi/b=p/b^2$、$c=b^{-1}$。
实际 Amice 测度记为 $\nu$，其变换是 $A(\Omega\log(1+Z))$。

## 1. 完整测度上的单 Euler 关系

利用 Agboola–Howard 2006 Theorem 2.1.1 的全 ray 插值，在所有
$4\mid j\pmod{p-1}$ 的 tame 分支保留有限因子 $136^j$，然后在乘法环带
变换的整域中统一确定平方的正号。对 $j>0$ 用 $x^j$ 消去原点原子，得到
$$
\boxed{\nu|_{p\mathbb Z_p}=c[a]_*\nu.}
\tag{1}
$$
因此不经 tame 平均也有全部矩恒等式
$$
\int_{\mathbb Z_p^\times}x^m\,d\nu=(1-ca^m)\Omega^mh_m
\qquad(m\ge0).
\tag{2}
$$
这加强了此前的 principal 版本。对同一实际截面的四阶导数参考
$B=A^{(4)}$，准确有
$$
J_B(0)=24(1-\pi^4/b^5),\qquad
\frac{J_A(T_m)}{J_B(T_m)}
 =\frac{1-ca^m}{1-ca^{m+4}}\frac{h_m}{h_{m+4}}\in\mathbb Q_p.
\tag{3}
$$
R60 的近似证书因而有准确 Euler 版本。

## 2. 真实 Cartier 与首个普通分母

令 $\mathscr A(t)=A(\log_Et)$。用实际正式同构
$\beta:\widehat{\mathbb G}_m\to\widehat E$ 及
$\beta^{\sigma^{-1}}=\beta\circ[b]$，全部周期因子在 Cartier 计算中抵消，得
$$
\boxed{\mathcal C(\mathscr A(t)\omega_E)
       =\mathscr A([b^{-1}]t)\omega_E.}
\tag{4}
$$
这里 $[b^{-1}]$ 是完整 $\mathbb Z_p$ 正式群作用，不是只取其模 $p$ 的线性项。

固定原函数 $Y(z)=\int_0^zA(w)dw$ 与 Euler 原函数 $\int A(w)dw/w$ 不同。
写 $\mathscr Y(t)=Y(\log_Et)=\sum y_nt^n$。由 (4) 的首项，
$$
y_n\in\mathbb Z_p\ (n<5p),\qquad v_p(y_{5p})=-1.
\tag{5}
$$
这个坐标中使 $|y_n|_p\rho^{n-1}\le1$ 的最大半径准确为
$\rho=p^{-1/(5p-1)}$，未声称它是全部代数坐标变化下的最优 jet 范数。
还有准确收敛原函数迹式
$\sum_{Q\in E[\pi]}\mathscr Y(P+Q)=b\mathscr Y([a]P)$。

根端复跑[固定有理系数脚本](../scripts/check-theta-full-cartier.py)，
$p=13,29,37,41$ 的 $u^{5p-1}du$ 系数模 $p$ 分别为 $3,23,7,10$，
均准确为 $\mathsf H_p^{-4}$，并逐项核验 (5)。
脚本不输入 Katz 值、周期或模形式校准。

## 3. 保留实际截面的固定代数微分方程

在固定四次曲线 $\mathcal C:v^2=1-17u^4$ 上，
$$
u'=v,\quad v'=-34u^3,\quad L'=17u^2,\quad
Q(u)=u^4+51u^8/5-289u^{12}/5+4913u^{16}/5.
$$
它经 $(u,v)\mapsto(u^{-2},-v/u^3)$ 二比一映到 $E_{17}$。
由于 $A=\theta^{17}Q(u)$，真实商 $Z=Y/\theta^{17}$ 满足
$$
\boxed{Z'+17LZ=Q(u).}
\tag{6}
$$
这是沿固定向量场的一阶连接，没有宣称在整个曲面上平坦。
用 $x\omega_E$ 非恰当性和有理函数的极点阶可严格证明
$L$ 在 $\mathbb C(\mathcal C)$ 上超越，且 $Z$ 在
$\mathbb C(\mathcal C)(L)$ 上超越。因此实际解析叶在
$\mathcal C\times\mathbb A^2$ 中 Zariski 稠密，并有阶至多二的复亚纯参数化。

(4)–(6) 不依赖 $J_p'(0)$ 是否为零；(5) 在附加中心消失假设下也仍存在。
尚须证明该附加条件对真实整格或 Frobenius 评价映射的额外限制，
不能直接把它改写成上述连接的 $p$-曲率消失。
完整证明、规范及一手来源见
[full Euler 与固定原函数连接](../notes/2026-11-12-full-theta-euler-and-fixed-primitive-connection.md)。
