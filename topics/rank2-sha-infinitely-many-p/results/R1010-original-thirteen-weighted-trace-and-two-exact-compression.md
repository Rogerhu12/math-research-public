# R1010 — 原单来源的十三隔核权、真实第六行下降与两 exact 极帽压缩

日期：2026-11-27 UTC。**已证明：对原 $\mathcal K,\mathcal C_{130}$，两个显示的 Frobenius 权保留同一第六读数，并将适配十三模型的全部剩余支撑下推到原三个二挠点。六次权留下的唯一十三核贡献正是 R1004 已返回的六阶数据；七次权将它全部隔去。下层输入的整个第三 Cartier 为零，两个 exact 层完整保留，第一层上限从原 $p(p-1)/2+60$ 降到 $p(p-1)/2+12$ 或 $+14$。**

这里的下层输入是先于读取明确给出的、随 $p$ 变化的**亚纯 degree10 来源**，不是原全纯 $S_{10}$ 中新增加的一条算术曲线。下面的身份作用于单个原 $f$，不假定平移后的中央和为零；最后仍只在原六位读者中替换第六项，前五项全部精度保持。

## 1. 原来源、适配模型及隔核权

使用 R1005/R1007 的同一原模型

$$
E_1:y^2=x^3+1,\quad X=x^3,\quad
\delta^2=-3,\quad\pi=(7+\delta)/2,\quad p=6s-1>211.
\tag{1}
$$

对 $f=\mathcal K$ 或 $\mathcal C_{130}$，写 $f=\sigma^{130}R_f$。
两来源满足

$$
\operatorname{ord}_Of\ge12,\qquad
(X+1)^2\mid R_f,\qquad
\operatorname{pole}_OR_f\le118.
\tag{2}
$$

第二个整除在 $R_f=x^2P_f(X)$ 的原完整多项式中成立。
具体原首项为
$\mathcal K=51840z^{12}+\cdots$、
$\mathcal C_{130}=-3151872z^{18}+\cdots$。
所有分母、原曲线和 canonical 零值范围仍按 R1005，不由(2)另造中央零。

沿 R1007 置

$$
\begin{aligned}
R_\pi(X)&=X^2+(2+6\delta)X+(40+24\delta)/13,\\
P_{10}&=-(D-10G)^{p-1}Z^{p+9},\\
Z_\pi&=Z(\pi z)/\pi,\qquad
\mathscr P_\pi=\frac{P_{10}(\pi z)}
                       {\pi^{10}R_\pi(X)^{10}},\\
\eta_\pi(f)&=Z_\pi^{-7}\mathscr P_\pi R_f\omega_E,\qquad
\mathcal T_{6,\pi}(f)=[Z_\pi^{6p+6}]\mathscr P_\pi R_f.
\end{aligned}
\tag{3}
$$

以下等式先在特征 $p$ 的原函数域内进行。对 $\ell=6,7$ 定义完整函数

$$
\boxed{g_{\ell,\pi}
=\left(\frac{R_\pi(X)}{(X+1)^2}\right)^\ell.}
\tag{4}
$$

在 $O$，$g_{\ell,\pi}=1+O(Z_\pi^6)$；在每个非零
$T\in\ker\pi$，它恰有 $\ell$ 阶零；在每个原非零二挠点恰有
$4\ell$ 阶极，除此以外无零极。
原核与二挠不相交。显示的
$R_\pi(-1)=-27\omega/\pi$、$R_\pi(0)=-16\omega^2/\pi$
保证这里没有另一个未列出的坏位。

### 1.1 为什么同一个第六读数没有改变

由特征 $p$ 的 Frobenius，

$$
g_{\ell,\pi}^p-1=O(Z_\pi^{6p}).
$$

同时(2)给 $\mathscr P_\pi R_f=O(Z_\pi^{12})$，所以

$$
\boxed{[Z_\pi^{6p+6}]
       g_{\ell,\pi}^p\mathscr P_\pi R_f
=\mathcal T_{6,\pi}(f).}
\tag{5}
$$

差的阶至少 $6p+12$，严格高于目标 $6p+6$。
这是一条模 $p$ 的确切有限窗口身份；没有把特征零的
$g_{\ell,\pi}^p$ 擅自改成 $1$，也没有把它当作完整 Tate 读者的同一来源。

## 2. 未除十三的完整 trace 及其真实支撑

用 $\operatorname{Tr}_{[\pi]}$ 表示函数域的**未平均** trace：

$$
\bigl(\operatorname{Tr}_{[\pi]}a\bigr)(Q)
=\sum_{\pi P=Q}a(P).
$$

对 $\ell=6,7$ 定义唯一的下层有理函数

$$
\boxed{
A_{\ell,p}(f)
=\pi^{-10}\operatorname{Tr}_{[\pi]}
\left(\frac{R_\pi(X)^{\ell p-10}R_f}
                 {(X+1)^{2\ell p}}\right).
}
\tag{6}
$$

其下层亚纯来源记为
$h_{\ell,p}(f)=\sigma^{10}A_{\ell,p}(f)$；
这里只用这一显示函数，不将其宣称为新的全纯 arithmetic primitive。
写

$$
\eta_{10,\ell}(f)=Z^{-7}P_{10}A_{\ell,p}(f)\omega_E,\qquad
\mathcal T_{6,10,\ell}(f)
=[Z^{6p+6}]P_{10}A_{\ell,p}(f).
\tag{7}
$$

完整投影公式给

$$
\boxed{[\pi]_*\bigl(g_{\ell,\pi}^p\eta_\pi(f)\bigr)
=\pi^6\eta_{10,\ell}(f).}
\tag{8}
$$

确实，(3)的全标量为
$\eta_\pi=\pi^{-3}(Z^{-7}P_{10})\circ[\pi]\,
(R_f/R_\pi^{10})\omega_E$，而对微分作 push 时另除 $\pi$。
因此左边准确为
$\pi^{-4}Z^{-7}P_{10}\operatorname{Tr}_{[\pi]}
(g_{\ell,\pi}^pR_f/R_\pi^{10})\omega_E$，即(8)。
这里没有额外的13；它已包含于(6)的未平均 trace 中。

### 2.1 O 及三个原二挠点以外没有极

在原 $O$ 分支，
$R_f/R_\pi^{10}$ 至少二阶零。
在其余十二个 $\pi$ 核分支，(6)括号内至少
$\ell p-10$ 阶零，因 $p>211$ 严格大于所用固定来源的原点阶。
所以

$$
\boxed{\operatorname{ord}_O A_{\ell,p}(f)\ge2,\qquad
       \operatorname{ord}_Oh_{\ell,p}(f)\ge12.}
\tag{9}
$$

更准确，若 $f=c_fz^r+\cdots$，$r=12$ 或18，则
$h_{\ell,p}(f)=c_f\pi^{-r}z^r+\cdots$；
非零十三核分支不能改变这条首项。

(6)括号内仅在原 $E[2]\setminus\{O\}$ 有极，每点极阶至多
$4\ell p-4$，其中 $-4$ 正是(2)的真实二重 $X+1$ 因子。
$[\pi]$ 在这三点上是一个排列；其余 $E[2\pi]$ 分支处括号内正则。
trace 只能将这些极送到原三个二挠点，故

$$
\boxed{\operatorname{Poles}A_{\ell,p}(f)
\subset E[2]\setminus\{O\},\qquad
\operatorname{pole}_{E[2]}A_{\ell,p}(f)\le4\ell p-4.}
\tag{10}
$$

这一步用的是整条函数 trace，不是先删掉另外六个 $E[2\pi]$ 轨道。

## 3. 第一 Cartier 后真正隔离原 O

记 $\mathcal C$ 为 Cartier 算子。准确有

$$
\mathcal C\bigl(g_{\ell,\pi}^p\eta_\pi(f)\bigr)
=g_{\ell,\pi}\mathcal C\eta_\pi(f).
\tag{11}
$$

在每个非零 $T\in\ker\pi$，输入 $\eta_\pi(f)$ 极阶至多7。
因为 $p>7$，其第一 Cartier 仅留简单极，且 R1004 给出了全部留数：

$$
\mathcal C\eta_\pi(f)
=b_T(f)^{1/p}\frac{du}{u}+\text{正则项},\qquad
b_T(f)=c_6(T_Tf).
\tag{12}
$$

这里可以直接取 $u=Z_\pi$ 为该点的原参数：
$du=\omega_E$，且 target 原点参数 $Z$ 的拉回准确等于 $\pi u$。
所以以下读数中的 $\pi^{-6}$ 不依赖一个另选局部坐标。

在 $O$，(5)说明(11)的 $u^5du$ 系数仍为
$\mathcal T_{6,\pi}(f)^{1/p}$。
对 $\ell=7$，(11)在每个非零核点至少从 $u^6du$ 起，
故这些分支全部不贡献 target 的 $Z^5dZ$ 系数。
对 $\ell=6$，唯一能贡献这一系数的是(12)的留数。置

$$
\boxed{c_\pi(T)=
\left(\frac{DR_\pi(T)}{(X(T)+1)^2}\right)^6.}
\tag{13}
$$

该分支的 $u^5du$ 系数准确为
$c_\pi(T)b_T(f)^{1/p}$；(12)的全部正则部分都从更高阶开始。

Cartier 与有限可分 trace 交换。比较(8)两边第一 Cartier 后的
$Z^5dZ$ 系数，先得

$$
\pi^{-6}\left\{\mathcal T_{6,\pi}(f)^{1/p}
 +\mathbf1_{\ell=6}\sum_{0\ne T\in\ker\pi}
                 c_\pi(T)b_T(f)^{1/p}\right\}
=\pi^{6/p}\mathcal T_{6,10,\ell}(f)^{1/p}.
$$

取 $p$ 次方、使用 $\pi^{p+1}=13$，得到本篇的单来源原读者身份：

$$
\boxed{\begin{aligned}
\mathcal T_{6,\pi}(f)
&=13^6\mathcal T_{6,10,7}(f),\\
\mathcal T_{6,\pi}(f)
&=13^6\mathcal T_{6,10,6}(f)-\mathcal B_{\pi,p}(f),\\
\mathcal B_{\pi,p}(f)
&=\sum_{0\ne T\in\ker\pi}c_\pi(T)^p b_T(f).
\end{aligned}}
\tag{14}
$$

第二行的核项是**负号**。式(14)没有用
$j_{T_Tf}=0$，也没有用无权 $\mathsf Q_\pi f$ 的中央零；
它依靠(4)的真实消失阶将原 $O$ 分支隔离出来。

## 4. 六次权的核项由原完整六阶数据直接支付

R1004 已将 $b_T(f)$ 写成整个二次代数中的
$b_\pi(f)\in K[X]/R_\pi$。同一代数中，
$DX=6x^2y$ 给

$$
\boxed{c_\pi(X)=
\frac{6^6X^4R_\pi'(X)^6}{(X+1)^9}
\quad\bmod R_\pi.}
\tag{15}
$$

它在整个每个六点轨道上取同一个值。故(14)中的准确已付项为

$$
\boxed{\mathcal B_{\pi,p}(f)
=6\operatorname{Tr}_{K[X]/R_\pi}
                 \bigl(c_\pi(X)^p b_\pi(f)\bigr).}
\tag{16}
$$

特别可直接代 R1004/R1007 的两条实际 K/C 多项式；
这里没有请求一个新的、随 $p$ 的 kernel jet。
完整 Frobenius 仍按 R1007(20)保持原 $g^2=13$ 和
$\epsilon_p=\pm1$，不能只对 $\delta$ 做共轭而保持 $X$ 不变。

### 4.1 c 的全范数和固定整性

原二次代数中的完整范数为

$$
N(X)=-16\omega^2/\pi,\quad
N(X+1)=-27\omega/\pi,\quad
N(R_\pi')=432/\pi.
$$

最后一式由原判别式 $-432/\pi$ 得到。
逐项代(15)，准确有

$$
\boxed{N(c_\pi)=-2^{52}3^3\omega^2/\pi.}
\tag{17}
$$

所以 $c_\pi$ 对所有本篇好 $p$ 都是整个二次代数的单位；
其分母和范数不引入任何新的变动坏位。
它也不属于 $K$：若 $c_\pi\in K$，其二次范数必为 $K$ 中的平方，
但(17)在 $\pi$ 处赋值为 $-1$。
因而写 $c_\pi=c_0+c_1X$ 时 $c_1\ne0$。

若需把(16)写成原两个固定 Frobenius 类型，令
$t_f=\operatorname{Tr}b_\pi(f)$，
$b_\pi(f)=A_f+B_fX$。R1007(20)直接给

$$
\boxed{\mathcal B_{\pi,p}(f)
=6\{\bar c_0+(-1+3\delta)\bar c_1\}t_f
 +1296\epsilon_p\bar c_1 B_f/g.}
\tag{18}
$$

本式的横线仅对固定 $K$ 系数作 CM 共轭；
$g$ 与 $\epsilon_p$ 仍是原实际根和 Frobenius 符号。
R1004 的两条 K/C 均有 $B_f\ne0$，故(18)的两个特征零值在
$K(g)$ 中都非零。准确的固定删集是在 $p\le211$ 之外再删除

$$
p\mid\prod_{f\in\{\mathcal K,\mathcal C_{130}\}}
\operatorname{num}N_{K(g)/\mathbf Q}
\left(6\{\bar c_0+(-1+3\delta)\bar c_1\}t_f
       +1296\bar c_1B_f/g\right).
\tag{18a}
$$

这两个范数是固定非零正有理数，另一 Frobenius 符号是其同一扩张共轭；
分母素因子都在原 $2,3,5,7,13$ 内。
如此删除后，两条 $\mathcal B_{\pi,p}(f)$ 各自非零。
这仍只是(14)已支付的核补项，不是整个 $\mathcal T_{6,\pi}$ 非零。
不需要这项附加非零性时，(14)–(17)对所有原好 $p$ 成立。

## 5. 下层整个第三 Cartier 为零，两 exact 全读回

原单 $P_{10}$ 的同一极帽及其对所有其它 $Z$ 零点的抵消，结合(9)–(10)，给

$$
\boxed{\operatorname{Poles}\eta_{10,\ell}(f)
\subset E[2]\setminus\{O\},\qquad
d_{\ell,p}=p^3-p^2+(2+4\ell)p-3<p^3.}
\tag{19}
$$

这保留了全部下层输入；其原点正则且从至少 $Z^5dZ$ 起。
它是原几何 $\mu_6$ 不变微分，在 $t=-X^{-1}$ 上下降为

$$
\eta_{10,\ell}(f)
=\sum_{n=1}^{L_{\ell,p}}
       a_{\ell,n,p}(f)(t-1)^{-n}dt,
\qquad
L_{\ell,p}
=\frac{p^3-p^2+(2+4\ell)p-2}{2}.
\tag{20}
$$

$t=\infty$ 和其它点均正则，因此没有未记录的多项式部分。
唯一可能留数在 $t=1$，整个留数定理给
$a_{\ell,1,p}(f)=0$。
由(19)，三次 Cartier 后至多有简单极；它的留数仍为零，故

$$
\boxed{\mathcal C^3\eta_{10,\ell}(f)=0.}
\tag{21}
$$

这不是把 R1007 的有十三核微分三次输出赋零；它是(6)–(10)之后
另一个已明确给定的完整下层输入。

置 $Y=(t-1)^{-1}$，$Y(O)=-1$。原两个 exact 多项式准确为

$$
H_{\ell,0}(Y)
=\sum_{\substack{j\ge1,\ p\nmid j\\1+jp\le L_{\ell,p}}}
 \frac{a_{\ell,1+jp,p}(f)^{1/p}}j
 \{Y^j-(-1)^j\},
$$

$$
H_{\ell,1}(Y)
=\sum_{\substack{j\ge1\\1+jp^2\le L_{\ell,p}}}
 \frac{a_{\ell,1+jp^2,p}(f)^{1/p^2}}j
 \{Y^j-(-1)^j\}.
\tag{22}
$$

其真实上限为

$$
\boxed{\deg H_{\ell,0}\le p(p-1)/2+2\ell,\qquad
       \deg H_{\ell,1}\le(p-1)/2.}
\tag{23}
$$

第一层保 $p\nmid j$，第二层的所有 $j$ 已小于 $p$，所以除数全部是单位。
没有第三 exact 多项式，两个已显示的层却不能删掉。

在原点读第一 Cartier 的 $Z^5dZ$ 系数，准确得

$$
\boxed{\mathcal T_{6,10,\ell}(f)
=-6\left\{H_{\ell,0}'(-1)^p+
          H_{\ell,1}'(-1)^{p^2}\right\}.}
\tag{24}
$$

这里来自(20)的原权都已实付：原 $t=1$ 对应
$X=-1$，R1007(28)的 $X^{2p}$ 和 $X^{p^2+p}$ 都等于1。
没有把一般七个点的权直接设为1；先用(8)真正下推为这个单一支撑后才有(24)。

把(24)代回(14)，原适配第六读者完全为

$$
\boxed{\mathcal T_{6,\pi}(f)
=-6\cdot13^6
 \left\{H_{\ell,0}'(-1)^p+
        H_{\ell,1}'(-1)^{p^2}\right\}
 -\mathbf1_{\ell=6}\mathcal B_{\pi,p}(f).}
\tag{25}
$$

与 R1005 原单 $P_{130}$ 的第一层上限 $p(p-1)/2+60$ 相比，
六次隔核权实际省48、七次隔核权省46；第二层上限保持。
这是一条原读者的真实分母/主部压缩，不把次数节省等同于两个剩余导数消失。

## 6. 原 Gaussian 与六位中央的全部修正

最后回到 R1003/R1005/R1007 的同一特征零原整窗。固定

$$
d=p+1,\quad c=[z^d]\log(\sigma/z),\quad
\kappa=34c,\quad a=p\kappa,\quad q=65/17,
\qquad q\kappa=130c.
\tag{26}
$$

对实际 $f$ 置

$$
g_h(f)=[z^{hd}]e^{-130cz^d}f,\qquad
a^+(f)=[z^{p+7}]e^{-130cz^d}f,
$$

$$
\gamma_\pi=10c(\pi^{p+1}-13),\qquad
\Gamma_{\pi,p}(f)=
\sum_{r=1}^5\frac{(-\overline{\gamma_\pi})^r}{r!}
             \overline{g_{6-r}(f)}.
\tag{27}
$$

本节横线表示原模 $p$ 约化。
$\gamma_\pi$ 保留原除 $p$，不能删；
$a^+(f)$ 是 R1003/R1005 的原低卷积，也不能删。
R1007 的完整模型比较现在准确变为

$$
\boxed{\overline{g_6(f)}
=-6\cdot13^6
 \left\{H_{\ell,0}'(-1)^p+
        H_{\ell,1}'(-1)^{p^2}\right\}
-\mathbf1_{\ell=6}\mathcal B_{\pi,p}(f)
-\Gamma_{\pi,p}(f)
-7\kappa_5\pi^{5p-1}\overline{a^+(f)}.}
\tag{28}
$$

这里的 $\kappa_5$ 仍是原 $Z=z-\kappa_5z^{5p}+\cdots$ 中的同一个系数。
特别不能在(28)把 $\pi^{5p-1}$ 改成1，或把 $\Gamma_{\pi,p}$ 当作质量零而省掉；
质量零只说明完整 Tate 导数在 $J^{(\pi)}=q_\pi^{-v}J$ 下不变，
并不逐块删除这个三角变换。

使用 R989 原尾，定义完整实际六项

$$
F_f^{[6]}(0)=
\sum_{h=1}^6
\frac{(-1)^{h-1}(h-1)!p^{h-1}}{q^ha^{h-1}}g_h(f)
\equiv\frac apj_f\pmod{p^6}.
\tag{29}
$$

令 $F_f^{[5]}(0)$ 为这里真实前五项，仍读取模 $p^6$ 的全部所需精度。
第六项系数是 $-120p^5/(q^6a^5)$，故(28)准确给

$$
\boxed{\begin{aligned}
F_f^{[6]}(0)\equiv F_f^{[5]}(0)
+\frac{p^5}{q^6a^5}\bigg[&
720\cdot13^6
 \left\{H_{\ell,0}'(-1)^p+
        H_{\ell,1}'(-1)^{p^2}\right\}\\
&+120\mathbf1_{\ell=6}\mathcal B_{\pi,p}(f)
 +120\Gamma_{\pi,p}(f)\\
&+840\kappa_5\pi^{5p-1}\overline{a^+(f)}
\bigg]\pmod{p^6}.
\end{aligned}}
\tag{30}
$$

括号内可取任意整提升；其选择差乘 $p^5$ 后落在 $p^6$。
这里仅替换原实际点的第六位，不将(6)的变动亚纯源放进原六位参数族，
也不扩张先前的物理窗口。

## 7. 整个 p 次权的固定十三项返回

上述极帽压缩还可与准确的 Kummer 展开结合，使(6)中增长的 $p$ 次权
在第一 Cartier 之前返回有限个固定 tame 分量。
这一节保留完整13项，不只看 $\pi$ 核的两个 principal 轨道。

在先于 $p$ 固定的原 $13$ 挠点域上，将原 $\pi$-cover 的函数域记为

$$
\mathcal A=k(E_1),\qquad
\mathcal B=[\pi]^*k(E_1),\qquad
[\mathcal A:\mathcal B]=13,\quad
\operatorname{Gal}(\mathcal A/\mathcal B)=\ker\pi.
\tag{31}
$$

该域也含原 Weil 配对的 $\mu_{13}$。
取 $0\ne S\in\ker\bar\pi$，原 target 上的 Miller 函数 $h$ 满足

$$
\operatorname{div}h=13(S)-13(O).
\tag{32}
$$

拉回除子 $[\pi]^*((S)-(O))$ 为 principal，因为在
$\operatorname{Pic}^0$ 中拉回是对偶 $[\bar\pi]$，而 $\bar\pi S=0$。
用原 $\omega_E$ 参数在 $O$ 的 $z^{-13}$ 首系数1规范 $h$，
再用 $z^{-1}$ 首系数 $\pi^{-1}$ 规范该 principal 除子的唯一函数
$\varkappa$，便得

$$
\operatorname{div}\varkappa=[\pi]^*((S)-(O)),\qquad
\varkappa^{13}=[\pi]^*h.
\tag{33}
$$

第二式的两边除子相同，且在 $O$ 的首项都是
$\pi^{-13}z^{-13}$，故常数准确为1；无需另选十三次根。
这些首系数也可用与 $z$ 同首项的原整代数参数 $-x/y$ 读取。
在 $2,3,13$ 外，所用挠点及其两组纤维均 étale 且不相交，
规范首系数是单位，因而这两 Miller 函数没有未列出的垂直零极。
$h$ 在 $\mathcal B$ 中不是十三次幂，否则 $(S)-(O)$ 将是 principal。
因此
$\mathcal A=\mathcal B(\varkappa)$，
$1,\varkappa,\ldots,\varkappa^{12}$ 是完整基。
固定一个原非零 deck 平移 $\tau$，并以其实际比值
$\zeta_{13}=\tau\varkappa/\varkappa$ 定义本节的原十三次根。
所有相位在下面两个 Fourier 展开中采用同一选择；
换 $\varkappa$ 或 $\zeta_{13}$ 只同时重标这些系数，不改变原 trace。

对本篇真实固定函数，准确展开

$$
\frac{R_f}{R_\pi^{10}}
=\sum_{i=0}^{12} f_i\varkappa^i,\qquad
g_{\ell,\pi}=\sum_{j=0}^{12} g_{\ell,j}\varkappa^j,
\qquad f_i,g_{\ell,j}\in\mathcal B.
\tag{34}
$$

系数唯一，并由全部原 deck 平移给出，例如

$$
f_i\varkappa^i
=\frac1{13}\sum_{n=0}^{12}
 \zeta_{13}^{-in}\tau^n(R_f/R_\pi^{10});
\tag{35}
$$

$g_{\ell,j}$ 同式。它们都是先于 $p$ 固定的原有理函数，不是新的可调参数。

令 $i_j$ 是 $-pj\bmod13$ 的 $0,\ldots,12$ 代表，
$e_j=(i_j+pj)/13$。特征 $p$ 中完整十三项 trace 准确为

$$
\boxed{
A_{\ell,p}(f)
=13\pi^{-10}
 \sum_{j=0}^{12}g_{\ell,j}^{\,p}f_{i_j}h^{e_j}.}
\tag{36}
$$

证明是直接展开(34)：$\varkappa^{i+pj}$ 的 trace 仅在
$13\mid i+pj$ 时非零，此时恰为 $13h^{(i+pj)/13}$。
因此(36)保留了原未平均 trace 的完整因子13。
指标重排只依赖 $p\bmod13$，没有把任何非平凡项删成零。

设 $\xi_{i,p}=Z^{-7}P_{10}f_i\omega_E$，仍用原指定 $P_{10}$。
在原 cover 中逐项有

$$
[\pi]^*(h^{e_j}\xi_{i_j,p})
=\varkappa^{i_j}(\varkappa^j)^p[\pi]^*\xi_{i_j,p}.
$$

Cartier 的 $p$ 次幂线性于是给

$$
\boxed{
[\pi]^*\mathcal C(h^{e_j}\xi_{i_j,p})
=\varkappa^j
 \mathcal C\bigl(\varkappa^{i_j}[\pi]^*\xi_{i_j,p}\bigr).}
\tag{37}
$$

右边确实下降到 $\mathcal B$：deck 字符的指数为
$j+p^{-1}i_j\equiv0\pmod{13}$，其中 Cartier 同时对
$\zeta_{13}$ 取 $p$ 次根。由(36)还可将每个
$g_{\ell,j}^p$ 在第一 Cartier 中准确提出。
因而增长指数 $e_j=O(p)$ 已在整条第一 Cartier 身份中替换成固定指数
$0\le i_j,j\le12$，只留下有限个原 tame 字符微分与同一个 $P_{10}$。
在连接形式中，同一事实也表现为
$d\log(h^{e_j})=(i_j/13)d\log h$。

(37)不删除 $\varkappa$ 的所有零极、原 $P_{10}$ 或任何 exact；
尤其这些固定 tame 分量尚不是已知中央零的 holomorphic $S_{10}$ 两列。
所以(36)–(37)是实际变动权的有限返回，而不是新的零传播规则。

## 8. 双支、实际非零范围及接续输入

对 $\bar\pi$ 完整重复(4)–(37)，各函数取原 CM 共轭、各 Frobenius 保原相位。
两支都是真正的原单来源比较；没有假定两个适配模型的 Gaussian 相同。
在两 canonical 坏假设下，R1005 仍给

$$
j_{\mathcal K}=0,\qquad
j_{\mathcal C_{130}}
=-\frac{\delta(p+1)}{112}\log_p(\pi/\bar\pi)\ne0.
\tag{38}
$$

所以(30)对 $\mathcal K$ 的左边为零模 $p^6$；
对 $\mathcal C_{130}$ 则准确为(38)乘 $a/p$ 的模 $p^6$ 类。
它可能在固定六位中尚未检出，完整深度仍由 R1000 的
$L_p=O(p/\log p)$ 保留，不能只用本篇压缩就称它已为单位。

本篇无需新数学执行：(12)、(16)的 $b_\pi(f)$ 直接消费 R1004
原 run 45916324833 / job 140236318135 /
source 56f5c405d885932a9d8b213a5cdb431376fa2ea3 的整个两核六阶输出；
其余身份由原完整函数 trace、局部阶和显示 Cartier 运算证明。
后继可以在(36)–(37)的实际有限 tame 返回或(30)的两个低次数 exact 中继续消元，
不能只沿用无权 trace 的中央零，也不能以已返回的固定核项替代(30)的整条等式。
