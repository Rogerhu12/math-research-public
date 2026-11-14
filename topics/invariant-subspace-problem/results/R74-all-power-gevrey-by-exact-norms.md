# R74：精确幂范数与任意幂次的 Gevrey 最小型

日期：2026-11-12（UTC）。主会话独立推导，并经独立交叉核验。**状态：完整证明已经独立交叉核验通过。**

R69/R71 的主算子 Gevrey 引理暂用 $1<p<4$。这里直接使用实际 $A$ 的全幂范数以及 $N_j^2=\eta_jN_{j+1}$，去掉该上限。没有扩大 BW 负积分已经认证的主指数范围 $1<p\le12/5$；新增的是实际横向变量可用的任意大 Gevrey 权。

## 1. 模型及局部函数假设

仍记
$$
W_n=\|A^n\|,\quad d_j=W_{2^j},\quad
N_j=A^{2^j}/d_j,\quad \Lambda_j=-\log d_j.
$$
R13/R65 的精确关系为
$$
W_n=\prod_{j:b_j(n)=1}d_j,\qquad
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j,
$$
$$
20\,16^j\le\Lambda_j\le125\,16^j,
\qquad \eta_j\le e^{-770\,16^j}.
\tag{1.1}
$$
上界由 $(150j+25)\le25\,8^j$ 直接得到；该初等不等式在 $j=0$ 成立，逐次相乘八的余量为 $1050j+25>0$。下界是既有 $\Lambda_j\ge16\Lambda_{j-1}$ 与 $\Lambda_0=20$。

对任意 $n\ge1$，取最高二进位 $h$，则 $2^h\le n<2^{h+1}$，故
$$
-\log W_n\ge20\,16^h\ge\frac54n^4.
\tag{1.2}
$$
同理由所有低位的等比和，存在绝对 $C_W$ 使
$$
\frac54n^4\le-\log W_n\le C_Wn^4.
\tag{1.3}
$$
因此对全部 $j\ge0,n\ge1$，
$$
\boxed{\|N_j^n\|=W_{n2^j}e^{n\Lambda_j}
\le\exp\!\left(n\Lambda_j-\frac54\,16^j n^4\right).}
\tag{1.4}
$$
另有精确进位恒等式带来的粗但统一界
$$
\|N_j^{2q}\|\le\eta_j^q,
\qquad \|N_j^{2q+1}\|\le\eta_j^q.
\tag{1.5}
$$

考虑实际算子
$$
Y=\psi(A)+\sum_{j\ge J}f_j(N_j),
\tag{1.6}
$$
其中 $\psi$ 是零常数标量解析芽，且
$$
f_j(z)=\xi_jz+\sum_{n\ge2}a_{j,n}z^n,
\qquad |a_{j,n}|\le\Gamma S^{n-1},
\tag{1.7}
$$
$\Gamma<\infty$、$S\ge2$ 为固定常数。假设 $\xi\in\ell^1$，并取固定 $J$ 足够大，使 $S^2\eta_j\le1/2$ 对 $j\ge J$ 成立。有限个初始局部芽都能并入 $\psi(A)$，因为 $f_j(z^{2^j}/d_j)$ 是 $z=0$ 处的实际收敛解析芽。

由 (1.5)，$f_j(N_j)$ 的高次部分范数为 $O(\Gamma\eta_j)$，故 (1.6) 按范数绝对收敛。$Y\in\mathcal A$、常数项为零，因而拟幂零。这里允许复系数；没有要求函数格正性。

## 2. 低位指数的统一对数界

### 引理 2.1

若 $H_j=N_jg_j(N_j)$，其中 $\|g_j(N_j)\|\le K$ 共同有界，则存在只依赖 $K$ 的常数 $C_0,C_1$，使对全部复 $t$ 和 $j$，
$$
\log\|e^{tH_j}\|
\le C_0+C_1\left[
16^{-j/3}\log^{4/3}(2+|t|)+16^j\right].
\tag{2.1}
$$

**证明。** 因 $N_j$ 与 $g_j(N_j)$ 交换，
$$
\|H_j^n\|\le K^n\|N_j^n\|.
$$
令 $D=16^j$、$v=\log(2+K|t|)+\Lambda_j\ge0$。由 (1.4) 并删去分母 $n!\ge1$，
$$
\|e^{tH_j}\|
\le1+\sum_{n\ge1}\exp\left(nv-\frac54Dn^4\right).
$$
取 $c=5/4$，初等极值估计给
$$
nv-cDn^4\le -\frac c2Dn^4+C_c v^{4/3}D^{-1/3}.
$$
例如对 $x\ge0$ 最大化 $vx-(cD/2)x^4$ 即得右侧常数。于是求和不超过
$$
C\exp(C'v^{4/3}D^{-1/3}),
$$
其中 $C$ 与 $j,t$ 无关，因为 $D\ge1$。

再用 $\Lambda_j\le125D$ 与 $(x+y)^{4/3}\le2^{1/3}(x^{4/3}+y^{4/3})$，以及固定 $K$ 的
$\log(2+K|t|)\le C_K\log(2+|t|)$，得到 (2.1)。证毕。

对 (1.7)，写
$$
f_j(N_j)=N_jg_j(N_j),\qquad
g_j(N_j)=\xi_jI+N_jh_j(N_j),
$$
$$
h_j(N_j)=\sum_{n\ge2}a_{j,n}N_j^{n-2}.
$$
(1.5) 与 $S^2\eta_j\le1/2$ 给
$$
\|h_j(N_j)\|\le
\Gamma S\frac{1+S}{1-S^2\eta_j}\le2\Gamma S(1+S).
\tag{2.2}
$$
因此全部 $g_j(N_j)$ 范数共同有界，且高次部分有更精确界
$$
\|N_j^2h_j(N_j)\|\le C\eta_j.
\tag{2.3}
$$
对有限前因子 $\psi(A)=Ag(A)$ 也可直接用 (1.2) 和同一极值求和，得到
$$
\log\|e^{t\psi(A)}\|
\le C\log^{4/3}(2+|t|).
\tag{2.4}
$$

## 3. 高位乘积及真正的双对数截断

由 (1.5)，对任意复 $t,\xi$，令 $x=|t\xi|$，则
$$
\begin{aligned}
\|e^{t\xi N_j}\|
&\le\cosh(x\sqrt{\eta_j})+
\frac{\sinh(x\sqrt{\eta_j})}{\sqrt{\eta_j}}\\
&\le(1+x)e^{x\sqrt{\eta_j}}.
\end{aligned}
\tag{3.1}
$$
结合 (2.3) 及同一个 $N_j$ 的函数相互交换，
$$
\log\|e^{tf_j(N_j)}\|
\le\log(1+|t||\xi_j|)
+|t||\xi_j|\sqrt{\eta_j}+C|t|\eta_j.
\tag{3.2}
$$

令 $T=|t|$。对充分大的 $T$，取最小的整数 $k\ge J$ 使
$$
770\,16^k\ge4\log(2+T).
\tag{3.3}
$$
则
$$
16^k=O(\log(2+T)),\qquad
k=O(\log\log(3+T)),
$$
$$
\sum_{j\ge k}\sqrt{\eta_j}\le C(2+T)^{-2},\qquad
\sum_{j\ge k}\eta_j\le C(2+T)^{-4}.
\tag{3.4}
$$
最后两个式子直接把 $e^{-385\,16^j}$、$e^{-770\,16^j}$ 的尾和按首项控制。有限有界时间区间可吸收入常数。

所有局部算子彼此交换，且其和按范数收敛。因此指数可按低位、尾部及前因子分解为范数收敛的乘积。由 (2.1)，低位的对数范数总和不超过
$$
\begin{aligned}
Ck+C\log^{4/3}(2+T)\sum_{j<k}16^{-j/3}
+C\sum_{j<k}16^j
\le C'\log^{4/3}(2+T).
\end{aligned}
$$
(2.4) 给前因子同样的界。高位用 (3.2)—(3.4)，其中 $\sup_j|\xi_j|<\infty$。得到完整且实际的估计：
$$
\boxed{
\log\|e^{tY}\|
\le C\log^{4/3}(2+T)
+\sum_{j\ge k(T)}\log(1+T|\xi_j|).
}
\tag{3.5}
$$
这里不使用 $e^{CT}$ 型 Duhamel 误差，故没有 $p<4$ 的限制。全部真实进位已保留在 (1.4)、(1.5) 和 (3.2) 中。

## 4. 任意 $p>1$ 的实际 Gevrey 幂界

**定理 4.1。** 在 (1.6)—(1.7) 下，若某个有限实数 $p>1$ 满足
$$
|\xi_j|\le C_p(j+2)^{-p},
$$
则存在 $K,C>0$，使
$$
\|e^{tY}\|\le K\exp(C|t|^{1/p})\qquad(t\in\mathbb C),
\tag{4.1}
$$
$$
\boxed{\|Y^n\|\le C_1^n(n!)^{1-p}\qquad(n\ge1).}
\tag{4.2}
$$
没有 $p<4$ 的上限。

若更强地 $\xi_j=o(j^{-p})$，则
$$
\boxed{\log\|e^{tY}\|=o(|t|^{1/p})}
\tag{4.3}
$$
在 $|t|\to\infty$ 时关于方向一致；并且对每个 $\varepsilon>0$，存在有限 $K_\varepsilon$ 使
$$
\boxed{\|Y^n\|\le
K_\varepsilon\varepsilon^n(n!)^{1-p}\qquad(n\ge0).}
\tag{4.4}
$$

**证明。** 对 $p>1$，递减函数和积分比较给
$$
\sum_{j\ge0}\log(1+T C_p(j+2)^{-p})
\le (TC_p)^{1/p}\int_0^\infty\log(1+x^{-p})\,dx.
$$
该积分有限：零附近由 $\log2-p\log x$ 控制，无穷远由 $x^{-p}$ 控制。结合 (3.5)，以及任何固定 $p$ 下
$\log^{4/3}(2+T)=o(T^{1/p})$，得到 (4.1)。

若 $\xi_j=o(j^{-p})$，记
$$
\rho_k=\sup_{j\ge k}(j+2)^p|\xi_j|\to0.
$$
(3.5) 的尾项至多为 $C'_p(T\rho_{k(T)})^{1/p}$；因 $k(T)\to\infty$，得到 (4.3)。算子谱半径给 $\|e^{tY}\|\ge1$，所以这里确是对数的两侧 $o$ 断言。

为得幂界，对算子值整函数 $e^{zY}$ 在 $|z|=R$ 用 Cauchy 系数式：
$$
\|Y^n\|\le n!R^{-n}\sup_{|z|=R}\|e^{zY}\|.
\tag{4.5}
$$
由 (4.1) 取 $R=(pn/C)^p$，得到
$$
\|Y^n\|\le K n!\left(\frac{eC}{pn}\right)^{pn}
\le K\left(\frac{eC}{p}\right)^{pn}(n!)^{1-p}.
$$
最后用 $(n!)^p\le n^{pn}$；固定 $K$ 吸收到指数常数得到 (4.2)。

在最小型情形，对任意 $c>0$ 有全平面界
$\|e^{zY}\|\le K_c e^{c|z|^{1/p}}$。同一选择令幂中的指数常数 $(ec/p)^p$ 任意小，给 (4.4)。反方向也可直接由指数级数与 $\ell^p$ 范数不超过 $\ell^1$ 范数推出 (4.3)。证毕。

此证明对复系数的 $Y$ 直接成立；不需要先把 $Y$ 误当成正算子。若需要共同的函数格正支配，可以在 (1.6)—(1.7) 中逐系数取绝对值，同一证明仍适用。

## 5. 对已证高阶取消工具的意义

R71 的多尺度 Newton 定理只需要各变量的幂界。因此对于满足这里局部函数条件的横向变量，权 $p_\ell-1$ 现在可取任意有限 $p_\ell>1$，无需原来的 $p_\ell<4$。

若一个实际余项的一阶尾比每个负幂都快，即对每个 $p>1$ 都是 $o(j^{-p})$，则该余项具有任意大的 Gevrey 权，且每个权上均为最小型。该结论不要求指数型或双指数型衰减，也不要求相位规则。

应区分两件事：本条去掉的是横向变量增长估计的指数上限；基准主变量的核分离仍须有实际负 BW 条件。这里没有把 $1<p\le12/5$ 的严格负积分证书擅自扩大到别的主指数。

## 6. 对数 $4/3$ 项的实际来源与尖锐性

式 (3.5) 的低位项一般不能统一改为 $O(\log(2+T))$。对实际正算子 $A$，有
$$
\boxed{\log\|e^{tA}\|\asymp(\log t)^{4/3}\qquad(t\to+\infty).}
\tag{6.1}
$$
上界是 (2.4) 的 $\psi(z)=z$。下界由函数格正序
$e^{tA}\ge t^nA^n/n!$ 及 (1.3)：
$$
\log\|e^{tA}\|\ge n\log t-C_Wn^4-\log(n!).
$$
取 $n=\lfloor c(\log t)^{1/3}\rfloor$，其中固定 $c>0$ 足够小，使 $C_Wc^3<1/2$。则前两项至少为正倍数的 $(\log t)^{4/3}$，而 $\log(n!)\le n\log n=o((\log t)^{4/3})$。得到下界。

因此本条选择 $k\asymp\log\log t$ 并保留这个低位量级，是对实际模型的估计，并非只在独立纯位极限中成立。
