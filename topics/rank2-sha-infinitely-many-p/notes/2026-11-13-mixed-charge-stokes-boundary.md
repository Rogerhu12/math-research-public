# 混合齐次次数的有限 Stokes 核与真实解析 charge 障碍

日期：2026-11-13。**状态：同一原第一带的有限核恒等式，以及任意有限次数原 Newton 数据的完整解析 charge 分类，均已证明。它们没有给新的中央非零或深 Smith 下界。** 本笔记记录 R224 之后检验“只让特定中央行下降到标量前缀”时必须保留的边界。

## 1. 原对象与实际观察行

取 $p=4r-1\ge19$，使用 R185 的全级规范 $b=17u_0$，令 $a=pb=17\tau_p\in O^\times$，并取
$$
                  1\le N\le(p+1)/2.
$$
原整轴满足 $A=e^{bw^r}f(w)$、$C=e^{bw^r}c(w)$，在本笔记使用的第一带有限阶上准确成立。对同一个原正次数源
$$
 P=\sum_{m=1}^D P_m,\qquad P_m\in O[A,C]^{(m)},
$$
记
$$
 g_m(y)=P_m(f(y),c(y)),\qquad
 V_m(Y)=\sum_{h=1}^N[y^{rh}]g_m\,Y^h.
$$
没有把 $g_m$ 或 $V_m$ 选成自由轴数据。原中央系数列满足
$$
 H(Y):=\sum_{h=1}^N[w^{rh}]P\,Y^h
       =\sum_{m=1}^D e^{mbY}V_m(Y)\pmod{Y^{N+1}}.
 \tag{1}
$$
原常数源可由第零行单独读出，故此处先扣除。

定义有限 factorial 核
$$
 L_N^{(b)}(V)=
     \sum_{h=1}^N(-1)^{h-1}(h-1)!b^{1-h}[Y^h]V.
 \tag{2}
$$
它是 R203 使用的规范有限核。它不自行等于所有 charge 上的完整原 Stokes 泛函；原完整权与它的准确有限精度比较仍按 R203 的半带范围使用。

同一个原标量前缀给出共同目标行
$$
 \boxed{\quad
 p\,L_N^{(b)}(e^{-bY}H)
  =\sum_{h=1}^N
       (-1)^{h-1}(h-1)!\binom Nh a^{1-h}J_{rh}(P),
 \quad}
 \tag{3}
$$
这里 $J_{rh}=p^h[w^{rh}]$，所有系数整，且只读至 $rN$。

证明：$[Y^h]H$ 的系数为
$$
 \sum_{j=0}^{N-h}
 (-1)^{h+j-1}(h+j-1)!b^{1-h-j}\frac{(-b)^j}{j!}
 =
 (-1)^{h-1}(h-1)!b^{1-h}
      \sum_{j=0}^{N-h}\binom{h+j-1}{j}.
$$
最后的和是 $\binom Nh$；再代入 $b=a/p$ 得 (3)。

R203 的原有理行 $t_N(P)$ 可对任意 $P$ 用相同公式定义，且
$$
 t_N(P)=\frac{(-b)^{N-1}}{pN!}
                  L_N^{(b)}(e^{-bY}H)
       =\frac1p\sum_{h=1}^N
              \frac{(-b)^{N-h}}{h(N-h)!}[w^{rh}]P.
 \tag{4}
$$
但只有原两个完整中央条件给出 $t_N(A),t_N(C)\in O$；本笔记没有将其扩成所有 $t_N(P)\in O$。

特别，双完整中央零确实使 (3) 在原线性源 $OA+OC$ 上落在 $p^{N+1}O$。它不是整个 $E_D$ 上的新独立中央零条件。

## 2. 每个混合 degree 的准确有限边界

对整数 $m\ge1$，令
$$
 B_{M,k}(x)=\sum_{j=0}^M\binom{k+j-1}{j}x^j,\qquad k\ge1.
$$
直接换序有限求和，得
$$
 \boxed{\quad
 L_N^{(b)}(e^{(m-1)bY}V_m)
  =\sum_{k=1}^N
       (-1)^{k-1}(k-1)!b^{1-k}\,v_{m,k}\,
                   B_{N-k,k}(1-m),
 \quad}
 \tag{5}
$$
其中 $v_{m,k}=[y^{rk}]g_m$ 是原轴系数。

有限负二项式恒等式是
$$
 (1-x)^k B_{M,k}(x)
   =1-x^{M+1}
        \sum_{j=0}^{k-1}\binom{M+j}{j}(1-x)^j.
 \tag{6}
$$
它可由对 $M$ 相减并检查 $M=0$ 证明，或由有限二项式卷积直接得到。

若 $m$ 为 $p$ 单位，则 (6) 准确写成
$$
 B_{M,k}(1-m)
   =m^{-k}
      \left(
        1-(1-m)^{M+1}
             \sum_{j=0}^{k-1}\binom{M+j}{j}m^j
      \right).
 \tag{7}
$$
因此 (5) 的第一项可以形式写作
$m^{-1}L_N^{(mb)}(V_m)$，但还必须保留全部 (7) 的第二项。这个写法仍只是有限核恒等式，不传递完整中央零。

对于 $m=1$，边界准确消失，回到原 $V_1$ 的规范核。对于 $m\not\equiv1\bmod p$，边界中的 $(1-m)^{M+1}$ 是单位，没有随截断长度自动增加的 $p$ 深度。完整中央零是否使其与其余原系数相消，必须另由原几何证明，不能在公式中删除。

## 3. 为什么不能直接使用无限负二项和

常见的形式替换是
$$
 \sum_{j\ge0}\binom{k+j-1}{j}(1-m)^j=m^{-k}.
$$
它在 $m\equiv1\bmod p$ 时可以按 $p$ 进收敛解释；在主区间
$1<m<p$ 时一般不可以。

这不是对原轴作自由反例，而是对所用核变换本身的准确检查。
当 $k=1$ 时，
$$
 B_{M,1}(1-m)=\frac{1-(1-m)^{M+1}}m,
$$
相邻部分和之差为 $(1-m)^{M+1}$。若 $m\not\equiv1\bmod p$，这个差始终为单位，因此核系数序列不收敛。将整个无限和换成 $m^{-1}$ 不是一个合法的有界目标操作。

对实际混合源还必须保留不同 $V_m$ 的原关联，不能据这个核检查宣称已构造原曲线的反例。它证明的范围是：通过 charge-$1$ 的有限 Stokes 核筛掉其他齐次块时，(5)—(7) 的边界没有被既有公式支付。

## 4. 任意有限次数原源的完整解析 charge 分类

这里不再限制 $D<p$。取任意固定有限 $D$，原正次数多项式为
$$
 P=\sum_{m=1}^DP_m,\qquad P_m\in O[A,C]^{(m)}.
$$
对正整数 $k$ 定义原 charge-$1$ 的有限 Newton 数据
$$
 \mathcal N_P(k)=b^{-k}k!\,[w^{rk}]P.
 \tag{8}
$$
它也等于对实际残余 $e^{-bw^r}P$ 所作 Newton 和在 $k$ 处的值，因为下降阶乘 $(k)_h$ 在 $h>k$ 时为零。因此定义 (8) 不假设任何无穷和已收敛。

“在中心附近解析”准确指：存在一个零附近的 $p$ 进解析函数，与 (8) 在该邻域内的全部正整数处一致。原常数源已扣除；若保留常数，应先使用第零行单独处理。

**定理。** 对任意有限 $D$，以下三件事等价：

1. 原数据 $\mathcal N_P(k)$ 在中心附近有解析实现。
2. 所有非零齐次块的次数满足 $m\equiv1\pmod p$。
3. 原同 charge 的完整级数
   $$
   \sum_{h\ge1} b^{-h}[w^{rh}](e^{-bw^r}P)(U)_h
   $$
   在包含 $\mathbf Z_p$ 的圆盘上解析收敛，并实现 (8)。

特别，$D<p$ 时只可能留下原线性块 $P_1$。高次数时允许的同余类准确是 $1\bmod p$，不同次数同落一个非平凡 Teichmüller 类并不能造成逃逸的实际抵消。

### 4.1. 同一个原残余盘对全部次数的估计

记
$$
 d=p+1,\qquad w=z^4,\qquad R=p^{-1/(2p)},\qquad
 \widehat A=e^{-bw^r}A,\quad \widehat C=e^{-bw^r}C.
$$
R185 §2、§6 的实际构造保证 $\widehat A,\widehat C$ 在闭 $z$ 盘 $|z|\le R$ 上解析有界。这里已付的全级规范比较是
$$
 u_0-4c_\sigma\in O.
$$
它与 R54 的原 sigma 规范只差一个整系数指数，且
$$
 v_p(z^d)\ge \frac{p+1}{2p}>\frac1{p-1}.
$$
所以额外指数在这个盘上收敛、范数为一。这不是以第一带近似替代全级原函数。

对每个 $m$，准确有
$$
 G_m=e^{-mbw^r}P_m
       =P_m(\widehat A,\widehat C).
 \tag{9}
$$
因此 $G_m$ 在同一闭盘上有界，**无须假设 $p\nmid m$**。这个步骤只使用固定有限多项式的乘法。

若 $p\nmid m$，自然 charge 的完整函数
$$
 \mathcal J_m(U)
   =\sum_{h\ge1}(mb)^{-h}[w^{rh}]G_m\,(U)_h
 \tag{10}
$$
解析于包含 $\mathbf Z_p$ 的同一圆盘，并满足
$$
 \mathcal J_m(k)=(mb)^{-k}k!\,[w^{rk}]P_m.
 \tag{11}
$$
事实上，若 $\|G_m\|_R\le p^{C_m}$，(10) 的 Newton 系数赋值至少
$$
 \frac{p-1}{2p}h-C_m.
$$
这是严格线性增长；$(U)_h$ 为整多项式，故既给闭单位盘收敛，也给稍大的共同盘。有限个 $m$ 可以取这些盘的交。

若 $p\mid m$，不定义未经支付的单位 charge 函数。但此时 $mb\in O$，所以
$e^{mbz^d}$ 本身在闭 $R$ 盘有界。由 (9)，原 $P_m$ 本身在此盘有界。令
$$
 P_{\mathrm{nu}}=\sum_{p\mid m}P_m.
$$
取一个有限常数 $C$ 控制其 Gauss 范数，得到全部正整数 $k$ 上的准确估计
$$
 \boxed{\quad
 v_p\!\left(b^{-k}k!\,[w^{rk}]P_{\mathrm{nu}}\right)
 \ge\frac{p-1}{2p}k+v_p(k!)-C.
 \quad}
 \tag{12}
$$
零值的赋值按 $+\infty$ 处理。

### 4.2. Teichmüller 分组及非单位块的超线性衰减

对所有 $p\nmid m$ 写
$$
 m=\omega_m\langle m\rangle,\qquad
 \omega_m\in\mu_{p-1},\quad \langle m\rangle\in1+pO.
$$
令
$$
 A_\omega(U)=
   \sum_{\substack{1\le m\le D\\p\nmid m,\ \omega_m=\omega}}
       \langle m\rangle^U\mathcal J_m(U).
 \tag{13}
$$
这些函数在包含 $\mathbf Z_p$ 的共同盘上解析。整数处的原数据分解为
$$
 \mathcal N_P(k)
 =\sum_{\omega\in\mu_{p-1}}\omega^k A_\omega(k)
   +b^{-k}k!\,[w^{rk}]P_{\mathrm{nu}}.
 \tag{14}
$$
这里只是有限个真实齐次块的求和。

假设解析实现 $J(U)$ 存在。对每个
$c_0\in\{1,\ldots,p-1\}$，取
$$
                         k=c_0p^a\longrightarrow0.
$$
由于 $p^a\equiv1\bmod(p-1)$，(14) 给
$$
 J(k)-\sum_\omega\omega^{c_0}A_\omega(k)
       =b^{-k}k!\,[w^{rk}]P_{\mathrm{nu}}.
$$
右端由 (12) 的赋值至少按一个正倍数的 $p^a$ 增长。左端是同一个零附近解析 germ 在 $c_0p^a$ 的值。非零解析 germ 可写成
$U^jH(U)$，其中 $H(0)\ne0$；对充分大 $a$，其在该点的赋值恰为
$ja+v_p(H(0))$，只按 $a$ 线性增长。因此上述解析差必须恒为零：
$$
                 J(U)=\sum_\omega\omega^{c_0}A_\omega(U)
                    \qquad(1\le c_0\le p-1).
 \tag{15}
$$
这一步处理了全部 $p\mid m$ 的实际部分，没有假定它们已有自然解析 Mellin 函数。

对 $c_0$ 作 $(p-1)$ 阶单位 Fourier 反演，得到
$$
              A_\omega=0\quad(\omega\ne1),\qquad J=A_1
 \tag{16}
$$
作为零附近 germ 的恒等式。每个 $A_\omega$ 原本就在包含 $\mathbf Z_p$ 的同一盘解析，所以前者在整个该盘恒为零。

### 4.3. 原中央单射排掉所有不允许的齐次块

固定 $\omega\ne1$，令
$$
 P_\omega=\sum_{\substack{p\nmid m\\\omega_m=\omega}}P_m.
$$
由 (11)、(13)，对每个正整数 $k$，
$$
 A_\omega(k)=\omega^{-k}b^{-k}k!\,[w^{rk}]P_\omega.
$$
式 (16) 因而给 $\mathcal C_rP_\omega=0$，常数项也因正次数为零。R190 §4.1 对**整个原混合次数多项式空间**的中央投影单射，遂给 $P_\omega=0$。

这里即使同一个 Teichmüller 类有多个次数，也不能保留一个非零抵消组合。R190 的实际系数矩阵在 $\mathbf Q$ 上；有限维满秩给一个非零有理 minor，所以同一单射适用于此处的 $\mathbf Q_p$ 原源。再由原齐次块的直和性，所有 $\omega_m\ne1$ 的 $P_m$ 都为零。

还要去掉 $P_{\mathrm{nu}}$。选整数 $s\ge0$，使 $p^sO$ 包含在 $J$ 的解析邻域内。由 (16) 的 $J=A_1$ 及 (14)，对全部正整数 $t$，取 $k=p^st$ 可得
$$
                        [w^{rp^st}]P_{\mathrm{nu}}=0.
$$
因此
$$
                         \mathcal C_{rp^s}P_{\mathrm{nu}}=0.
$$
R190 对每个正整数中央步长都成立，故 $P_{\mathrm{nu}}=0$。这证明 1 推出 2，包括全部非单位次数。

### 4.4. 允许次数确实给原完整级数收敛

反过来，若所有出现的 $m$ 都满足 $m\equiv1\bmod p$，则
$(m-1)b\in O$。由 (9)，
$$
 e^{-bw^r}P
   =\sum_{m\equiv1\ (\mathrm{mod}\ p)}
         e^{(m-1)bw^r}G_m
$$
在同一个闭 $R$ 盘上解析有界。乘 $b^{-h}$ 后的中央系数，仍有
$(p-1)h/(2p)-C$ 的线性赋值下界。因此原 charge-$1$ Newton 级数本身在包含 $\mathbf Z_p$ 的盘上收敛，并在所有非负整数处准确插值。故 2 推出 3，3 推出 1 则直接由定义。$\square$

这个分类保留每个实际 $P_m$、完整残余和所有原中央系数；没有交换不收敛无穷和，没有加入额外中央零，也没有选择未来轴系数。

## 5. 对后续定向下降的具体含义

式 (3) 是可直接在原标量前缀上计算的整行；式 (5) 准确列出它对每个原齐次块的作用。双完整中央零只支付 $m=1$ 的规范核。第 4 节将任意有限次数的同 charge 解析性准确限制到 $m\equiv1\bmod p$；在当前主范围 $D<p$ 中，只保留原线性源。R224 已将全部加权 Hasse 观测压为 Euler ladder，但并未使其他 $m$ 的边界消失。

所以后续若尝试让 R189 的特定中央–Hasse 行下降，必须证明这些实际混合边界在同一个原有限像内可消去，或给其准确的观测损失。不能以无限换序、其他 degree 的中央零、或可任选的未来轴系数代替这个原几何输入。

依赖：
[R185](../results/R185-integral-axis-stokes-functional-and-complete-central-tests.md)、
[R189](../results/R189-complete-central-hasse-families-and-weighted-core.md)、
[R199](../results/R199-exact-first-band-exponential-and-complete-divided-image.md)、
[R203](../results/R203-finite-central-companion-and-rational-row-lattices.md)、
[R224](../results/R224-radial-image-euler-hasse-observation-and-cross-degree-relations.md)、
[R190](../results/R190-central-projection-of-square-theta-sections.md)。
