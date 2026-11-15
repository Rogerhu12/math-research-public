# R831：原 EO 通道的完整 Weil 交换代数与六维 old 的绝对不可约性

日期：2026-11-15。**状态：已证明。**

在原模六二次模及原 EO 通道上，完整 Weil 交换代数恰为
$$
 \operatorname{End}_{\rho_{\mathcal A}}(V_{\rm EO})
   =k\,I\oplus k\,\mathscr P.
 \tag{831.1}
$$
这里 $\mathscr P$ 是 R828 的原二部分交换。原六维 old 空间和二维 new 空间分别绝对不可约，且互不等价。此结论在特征零及每个特征 $p>3$ 的域上均成立，按需加入原有限相位后计算并可下降。

因此，不仅 R828 已分类的置换等距，**任意**完整 Weil 交换子的 EO 压缩都在原六维 old 空间上为标量。它不能把原二维 CM 允许空间进一步投到指定 FG 或 HJ 直线。本结果没有证明实际 FG 值非零，没有分类所有其它有限层/Hecke 操作，也没有处理原 primitive/Legendre 筛后的单位问题。

## 1. 保持的原对象

全部对象取 [R828](R828-original-inert-two-primary-parity-and-old-source.md)：
$$
 \mathcal A=(\mathbb Z/6)^2,\qquad
 q(r,s)=(r^2+s^2)/12\pmod{\mathbb Z},
$$
$$
 V_{\rm EO}
 =\{f:f(-r,s)=f(r,s),\ f(r,-s)=-f(r,s)\}.
 \tag{831.2}
$$
设 $\iota_1,\iota_2$ 为这两个反号作用，令
$$
 P_{\rm EO}=\frac{(I+\iota_1)(I-\iota_2)}4.
 \tag{831.3}
$$
它是原 Weil 表示的交换投影，因两个反号均保 $q$ 及其 Fourier 配对。R828 的
$$
 P_2=\begin{pmatrix}4&3\\3&4\end{pmatrix}\pmod6
$$
在二部分交换坐标、在三部分恒等，所诱导的算子为 $\mathscr P$。同一篇已经证明
$$
 V_+=\langle F_{3,1},F_{3,2},F_{3,4},
                 F_{7,1},F_{7,2},F_{7,4}\rangle,\qquad
 V_-=\langle G_1,G_5\rangle,
 \tag{831.4}
$$
分别是 $\mathscr P$ 的 $+1,-1$ 空间，维数 $6,2$；八个源矩阵是原整基。此处 $F_{b,d}$ 指原源矩阵，包含原 oldform 尺度，没有重新定义 theta 形式。

Weil $T$ 是 $e(q)$ 对角作用，$S$ 是原双变量 Fourier 矩阵乘共同非零相位。共同相位与 eta 规范不改变交换代数；下文只省去这一个共同标量，不独立缩放不同基向量或不同源。

## 2. 原二、三部分的显式分块

用唯一的中国剩余表示
$$
 r=3a+4b,\qquad s=3c+4d,
 \quad (a,c)\in(\mathbb Z/2)^2,\quad(b,d)\in(\mathbb Z/3)^2.
$$
直接展开给
$$
 q=q_2+q_3,\qquad
 q_2(a,c)=\frac34(a^2+c^2),\qquad
 q_3(b,d)=\frac13(b^2+d^2)\pmod{\mathbb Z}.
 \tag{831.5}
$$
交叉项是整数。因此原函数空间及 Fourier 核按这两个部分张量分解。这一步是原二次模的分解，不换成其它 level 或其它 torus。

在二部分的四维空间中，记 $e_{ac}$ 为坐标 delta 基，取
$$
 u_0=e_{00},\quad u_1=e_{01}+e_{10},\quad u_2=e_{11},
 \qquad u_-=e_{01}-e_{10}.
 \tag{831.6}
$$
前三者是 $\mathscr P$ 的正空间，末者是负空间。令 $\iota^2=-1$。因为 $e(3/4)=-\iota$，$T_2$ 的准确对角为
$$
 T_{2,+}=\operatorname{diag}(1,-\iota,-1),\qquad
 T_{2,-}=-\iota.
 \tag{831.7}
$$
二部分的未归一 Fourier 核为
$$
 (-1)^{aa'+cc'}.
$$
在 (831.6) 的基上，其矩阵分别为
$$
 M=\begin{pmatrix}
 1&2&1\\
 1&0&-1\\
 1&-2&1
 \end{pmatrix},
 \qquad -2.
 \tag{831.8}
$$
例如 $u_1$ 送到 $2u_0-2u_2$，$u_-$ 送到 $-2u_-$，核定了负块与正块的相对标量。

三部分中，反号只作用于模三坐标，因为模二反号恒等。故原 EO 条件只选三部分的 even-by-odd 二维子空间。令 $\omega^3=1,\omega\ne1$，取
$$
 v_0=e_0\otimes(e_1-e_{-1}),\qquad
 v_1=(e_1+e_{-1})\otimes(e_1-e_{-1}).
 \tag{831.9}
$$
其 $T_3$ 为
$$
 \operatorname{diag}(\omega,\omega^2).
 \tag{831.10}
$$
原三部分 Fourier 核是
$$
 e\!\left(-\frac{2bb'+2dd'}3\right)
 =\omega^{bb'+dd'}.
$$
单份 Fourier 将 $e_1-e_{-1}$ 送到
$(\omega-\omega^2)(e_1-e_{-1})$；在 even 基 $e_0,e_1+e_{-1}$ 上的未归一矩阵为
$$
 K=\begin{pmatrix}1&2\\1&-1\end{pmatrix}.
 \tag{831.11}
$$
所以三部分在 (831.9) 上的 Fourier 矩阵恰为
$(\omega-\omega^2)K$。这里 $\omega-\omega^2\ne0$；所有被省去的共同 Fourier 分母仅涉及 $2,3$。

由此，在
$$
 V_+=\langle u_0,u_1,u_2\rangle\otimes\langle v_0,v_1\rangle,
 \qquad
 V_-=\langle u_-\rangle\otimes\langle v_0,v_1\rangle
 \tag{831.12}
$$
上，原 $S$ 除以同一个非零标量后分别为
$$
 S_+\sim M\otimes K,\qquad S_-\sim-2K.
 \tag{831.13}
$$
这与 (831.4) 是同一个正负分解，只使用了便于读 $S,T$ 的基。

## 3. 六维 old 与二维 new 的绝对不可约性

先在含 $\iota,\omega$ 和原共同相位的代数闭域工作。原 $T$ 在 $V_+$ 上的六个特征值为
$$
 \omega,\ \omega^2,\ -\iota\omega,\ -\iota\omega^2,\
             -\omega,\ -\omega^2.
 \tag{831.14}
$$
它们两两不同：若两个相等，则某个 $\mu_4$ 元等于某个 $\mu_3$ 元，而两个根群的交只有 $1$；再由显示的四次根及三次根的实际不同性即可。特征 $p>3$ 时，这些根仍两两不同。

因此，任一 $T$-稳定子空间都是 (831.12) 中若干坐标特征线的直和。具体地，各坐标投影是 $T$ 的 Lagrange 插值多项式，不需要假设一个未验证的半单分解。

若非零的 $S,T$-稳定子空间包含某个 $u_i\otimes v_j$，则由 (831.8)、(831.11) 的第一行，$S(u_i\otimes v_j)$ 在两个 $u_0\otimes v_b$ 上的系数都非零。用 $T$ 的坐标投影，子空间包含这两条特征线。再对其中任一 $u_0\otimes v_b$ 作用 $S$，由于 $M$ 第一列的三项及 $K$ 的全部四项都非零，得到全部六条特征线。因此
$$
 V_+\ \text{绝对不可约}.
 \tag{831.15}
$$
所用非零整数仅为 $\pm1,\pm2$，故该论证在所有 $p>3$ 原样成立。

在 $V_-$ 上，$T$ 有两个不同特征值
$-\iota\omega,-\iota\omega^2$；$S$ 矩阵 $-2K$ 的四项均非零。同样的两步坐标投影证明
$$
 V_-\ \text{绝对不可约}.
 \tag{831.16}
$$
这两个不可约表示维数不同，因而没有非零相互 intertwiner。非零 intertwiner 的核与像会分别给不可约子模，从而迫同构，与维数 $6\ne2$ 矛盾。

还可直接计算各自的交换代数：与具有互异特征值的 $T$ 交换的矩阵必须对角；与 (831.13) 交换迫所有经非零 Fourier 条目连接的对角值相等。以上连接论证已覆盖全部坐标，故两个块的交换代数各为标量。

于是
$$
 \operatorname{End}_{\rho_{\mathcal A}}(V_{\rm EO})
 = k\,I_{V_+}\oplus k\,I_{V_-}
 = k\,\frac{I+\mathscr P}{2}
     \oplus k\,\frac{I-\mathscr P}{2},
 \tag{831.17}
$$
即 (831.1)。若最初的定义域不含上述所有根，先扩域所得的绝对不可约性仍成立；定义在原域的块标量受 Galois 固定，故 (831.17) 下降。没有依赖某个有限素数窗口或数值拟合。

## 4. 任意完整三十六维交换子的 EO 压缩

令 $C$ 是整个原 $k[\mathcal A]$ 上与 $S,T$ 交换的任意线性算子。这里不要求它来自二次模置换，也不要求它保持 EO。

由 (831.3)，
$$
 P_{\rm EO}CP_{\rm EO}|_{V_{\rm EO}}
$$
仍与原 $S,T$ 交换。故存在唯一 $\alpha_C,\beta_C\in k$ 使
$$
 \boxed{
 P_{\rm EO}CP_{\rm EO}|_{V_{\rm EO}}
   =\alpha_C I_{V_+}\oplus\beta_C I_{V_-}.
 }
 \tag{831.18}
$$
这已经控制了完整三十六维交换代数对原通道的全部作用；无需先分类它对其它奇偶通道的各块。

特别，若 $C$ 保持 EO，则 $C|_{V_+}=\alpha_C I$。若它还是幂等投影，则 $\alpha_C$ 只能为 $0$ 或 $1$；因此在原六维 old 中，它只会投成零或保留整个空间。若不保持 EO 而在作用后压回 EO，结论 (831.18) 同样适用。

## 5. 对原 CM 与同标签问题的准确含义

R828 已用实际固定运输、原共同相位及交零论证证明
$$
 W=\mathcal U^{-1}\langle E_{F,G},E_{H,J}\rangle
       \subset V_+,\qquad\dim W=2.
 \tag{831.19}
$$
本篇没有重新计算 $\widehat U$、八源矩阵或原 CM 值。对每个 (831.18) 的 $C$ 及 $w\in W$，有
$$
 P_{\rm EO}Cw=\alpha_C w.
 \tag{831.20}
$$
若 $C$ 保持 EO，这就是 $Cw=\alpha_Cw$。实际 CM 稳定元本来就是原有限 Weil 作用乘共同相位，所以额外要求与该元交换不会在 (831.17) 中创造新的非标量方向。

因此，**完整 Weil 交换代数也不能把原 $W$ 再分成所需 FG 与 HJ 直线**。R828 中由 $\mathscr P$ 排掉两个 new 值，已经用尽所有此类交换操作在原 EO 内的非标量区分。

这个结论不对只与单个 CM 元交换的任意算子作同样断言，也不排除新的真实 Hecke/CM 配对、非交换运输或算术点值输入。原 Legendre 权及 primitive 筛必须保留自身原算子；不能因本篇交换代数结果而删去它们。

实际目标仍是 [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md) 同一个原 $h$ 的三因子非零，以及 [R826](R826-original-inert-companion-theta-CM-pairing.md) 的指定六项 CM 和。原全局 theta 非零、$V_+$ 不可约与指定点值非零是不同结论；本篇给出前述完整表示结构，没有新增点值非零。

## 来源与复核方式

- [R828](R828-original-inert-two-primary-parity-and-old-source.md)，原二次模、EO、$\mathscr P$、old/new、实际 CM 允许空间及源绑定。
- [GC 固定分解](../notes/2026-11-15-sigma-inert-Gaussian-rayclass-source.md)，八个原矩阵及只含二部分分母的基变换。
- [R826 实际运输](R826-certified-inert-Gaussian-source-transport.md)，run 43725592504、source d3a4216875ffde37005c74a8cf27687e631d935a、canonical SHA256 916e1b951a5acc6c375477ea13078d27a088ffcebac66ab76abf7a91676836a3。

新增论证是 (831.5)–(831.18) 的显式矩阵纸证。没有新数学数值运算，没有重新生成任何已有矩阵，也不另设独立验证 gate。
