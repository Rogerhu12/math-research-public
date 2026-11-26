# R596 同一 R583 尾的有限延伸：$2\le j\le16$

状态：严格有限频率补证；主课题未完成。

这是 [R583](../results/R583-finite-high-mode-flat-kernels-on-the-same-mild-tail.md) 的显式有限常数延伸，用于下一次完整有限角弱边值输入。它不重做旧四模数值口，不给全频逆，也不认证数值 ODE。

固定同一 $r_c=11/50,\ell=1/5,A=4/5$ 与相位 $\varphi\in[0,2\pi]$，
$$
w=Ae^{-u(2-\sin(u+\varphi))},\quad r=r_c+\ell/u,\quad
p=4u^2r^{2\mu}e^{-u(2-\sin(u+\varphi))},\quad
\varepsilon=\frac{\mu(\mu-1)\ell^2}{r^2u^4},
\qquad \mu=j^2.
$$
准确角模方程仍为
$$
(wf')'-\mu w'f/r=0,\qquad f=r^\mu y,\qquad
(py_u)'+\varepsilon p y=0.
$$

对 $4\le\mu\le256,\ u\ge100$，R583 的
$$
\eta=(2-\sin(u+\varphi))/u-2/u^2+2\mu\ell/(ru^3)
$$
满足
$$
0<\eta<.03+\frac{512/5}{(11/50)10^6}<.031,
$$
以及
$$
|\eta'|\le u^{-1}+3u^{-2}+4u^{-3}
+\frac{2\mu\ell^2}{r_c^2u^5}+\frac{6\mu\ell}{r_cu^4}<.011.
$$
因此同一 stationary-point 证明仍给每个 $n\ge17$ 唯一最大点
$$
\pi/2+2\pi n-\varphi-.04<\alpha_n<\pi/2+2\pi n-\varphi,
$$
及对应唯一谷点。全部 cell 仍在 $u>100$，长度在 6 与 7 之间，且权先降后升。

对 cell 左端 $a=\alpha_n$，令 $C_a=4r_c^{2\mu}a^2$。在 $a\le u<a+7$，
$$
1\le\frac{u^2r(u)^{2\mu}}{a^2r_c^{2\mu}}
\le(107/100)^2e^{256/55}<256.
$$
这里指数界来自 $(1+x)^t\le e^{tx}$；
粗略核验 $(107/100)^2<6/5$、$256/55<5$、
$e<11/4$，于是右端小于 $(6/5)(11/4)^5<256$。
故用显式 256 代替 R583 的 4，得到
$$
e^{-21}C_a e^{-a(2-\sin(u+\varphi))}
\le p(u)\le256C_a e^{-a(2-\sin(u+\varphi))}.
$$
准确势满足
$$
a^{-4}\le\varepsilon(u)\le54000a^{-4}.
$$
上界由 $256\cdot255\cdot(1/5)^2/(11/50)^2<54000$；
下界与 R583 相同。单谷 Green 小量为
$$
\frac{49}{2}\varepsilon_{\max}\le
\frac{49\cdot54000}{2\cdot100^4}<.014<\frac12.
$$
因此 R569 已付的 contrast-independent Dirichlet 逆和 Green domination 仍直接适用。

令 $K=(\int p^{-1})^{-1}$。同样的两端长 $1/2$ 窗和中间长 1 谷窗给
$$
K\le256C_a e^{-11a/4},\qquad
\int pH_L^2,\int pH_R^2
\ge\frac{e^{-21}C_a}{16}e^{-5a/4}.
$$
对应零势端值 $H_i\ge1/2$ 的电阻条件现在可用
$128e^{21}e^{-3a/2}<1/2$；
吸收对角 $K$ 项的条件可用
$8192e^{21}a^4e^{-3a/2}<1$。
两式在 $a\ge100$ 均成立，并随 $a$ 递减。

于是准确含势 DtN 仍满足
$$
0<-D_{LR}\le2K,\qquad
D_{LL},D_{RR}\le-\frac{e^{-21}C_a}{32a^4}e^{-5a/4}<0.
$$
写 $k_n=-D_{n,LR}$，$V_n=-(D_{n-1,RR}+D_{n,LL})$。
R583 的前一 cell 估计只把上侧 prefactor 放大 64 倍，故共同保守界为
$$
\frac{k_{n-1}}{V_n},\frac{k_n}{V_n}
\le65536e^{42}a^4e^{-3a/2}<\frac1{64}. \tag{1}
$$
在 $a=100$，左侧上界为 $2^{16}10^8e^{-108}$，
利用 $10^8<2^{27}$ 与 $e>2$ 已小于 $2^{-65}<1/64$；
$a^4e^{-3a/2}$ 在该区间严格递减。

因此在 $0\le\rho\le1/32$ 上，
$$
\rho_n=\frac{k_{n-1}}{V_n-k_n\rho_{n+1}}
$$
保持正小比值区间，导数仍小于 $10^{-3}$。
从准确有限端 $\rho_{M+1}=0$ 反推并取极限，获得实际非零全平解；
并且仍有
$$
|\rho_n-\rho_n^{(M)}|\le\frac1{32}10^{-3(M-n+1)}.
$$
(1) 给节点 $e^{-c\alpha_n^2}$ 衰减，cell 的各固定阶 ODE 延伸损失至多
$e^{C_k\alpha_n}$；故所有固定阶 $r$ 导数全平。
Wronskian 保持证明该归一全平空间一维；
相位连续依赖也由同一一致收缩得到。
此处有限集合扩大至全部整数 $2\le j\le16$，没有对 $j\to\infty$ 作一致断言。

新的 $j=10,12,14,16$ 实现须分别使用本模的 $p,\varepsilon,\alpha_{17}$、
准确索引 $\rho_{M+1}=0$、各自数值传递和独立外口归一；
不允许把旧 $j=2,4,6,8$ 口当作这些高模的口。
上述准确 DtN 截断界仍不包括浮点积分误差。
若在有限非线性候选中用这些齐次口作内端 Robin 行，
未解的非线性内尾和任何显式二 jets 匹配项必须继续保留在完整残差中。

